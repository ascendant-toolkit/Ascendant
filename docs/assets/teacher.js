// Teacher dashboard, drawn into the Dashboard page for staff. Three kinds of teacher:
//   school or tutor teacher: their own classes, students, trackers, adding students (data from the v12 RPCs)
//   admin:                   the same trackers over their IG1/IG2/AL class groups; managing students stays in the admin console
//   co-teacher:              topic tests and mark schemes only (no student data by design)
(function () {
  const K = window.TrackerKit, R = window.Roster;
  const { esc, fmt } = K;
  const pct = (done, total) => (total ? Math.round((100 * done) / total) : 0);
  const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;
  const avg = (xs) => (xs.length ? Math.round(xs.reduce((t, v) => t + v, 0) / xs.length) : null);
  const show = (v, suffix = "%") => (v === null || v === undefined ? "–" : v + suffix);
  const msg = (el, text, ok) => { el.textContent = text; el.className = "msg " + (ok ? "ok" : "err"); el.hidden = !text; };
  const DAY = 864e5;

  async function run(root, me, S, catalog) {
    const sb = S.sb, sc = me.school, school = !!me.is_school_teacher, admin = !!me.is_admin;
    const tutor = school && sc.kind === "tutor";
    const classWord = tutor ? "group" : "class", classesWord = tutor ? "Groups" : "Classes";
    const $ = (sel, el = root) => el.querySelector(sel);
    const hasData = school || admin;           // co-teachers get tests and mark schemes only
    const courseKeys = me.subjects.filter((k) => catalog.courses[k]);
    let st = { students: [], classes: [], progress: new Map(), assess: [], tests: [], taught: new Map(), sent: [], schemaMissing: false };
    let q = "";                                // student filter text
    let cf = "";                               // class or subject filter: "c:<class id>" or "s:<subject>"

    // ---------- data ----------
    async function load() {
      if (school) {
        const [d, c, t] = await Promise.all([sb.rpc("school_dashboard"), sb.rpc("teacher_classes"), sb.rpc("school_test_attempts")]);
        if (d.error) throw d.error;
        st.schemaMissing = !!(c.error || t.error);
        st.students = d.data.students.map((p) => ({ ...p, subs: R.schoolSubs(sc, p).filter((k) => catalog.courses[k]) }));
        st.assess = d.data.attempts;
        st.progress = new Map();
        d.data.progress.forEach((r) => { if (!st.progress.has(r.email)) st.progress.set(r.email, new Map()); st.progress.get(r.email).set(r.slug, r.done_at); });
        st.classes = c.data || [];
        st.tests = t.data || [];
      } else if (admin) {
        const [p, prog, att, tests, schools] = await Promise.all([sb.from("profiles").select("*").order("name"), sb.rpc("admin_progress"), sb.rpc("admin_attempts"),
          sb.rpc("admin_test_attempts"), sb.from("schools").select("*")]);
        if (p.error) throw p.error;
        const lic = new Map((schools.data || []).map((x) => [x.id, x]));
        st.students = p.data.map((x) => {
          const l = x.school_id && lic.get(x.school_id);
          const subs = [...new Set([...(x.subjects || []), ...(l && R.isLive(l) ? R.schoolSubs(l, x) : [])])].filter((k) => catalog.courses[k]);
          return { ...x, subs };
        });
        st.progress = new Map();
        (prog.data || []).forEach((r) => { if (!st.progress.has(r.email)) st.progress.set(r.email, new Map()); st.progress.get(r.email).set(r.slug, r.done_at); });
        st.assess = (att.data || []).filter((a) => !a.reset_at);
        st.tests = [...(tests.data || [])].reverse().map((r) => ({ ...r, course: r.test.split("/")[0] }));
        st.classes = S.adminGroups.map((g) => ({ ...g, members: st.students.filter((x) => (x.classes || []).includes(g.id)).map((x) => x.email) })).filter((g) => g.members.length);
      }
    }

    async function loadTaught() {
      st.taught = new Map();
      if (hasData) { const r = await sb.rpc("my_sent_reminders"); st.sent = r.error ? [] : r.data || []; }
      if (!st.classes.length) return;
      const { data } = await sb.rpc("my_taught");
      (data || []).forEach((r) => { if (!st.taught.has(r.class)) st.taught.set(r.class, new Map()); st.taught.get(r.class).set(r.slug, r.at); });
    }
    const taughtOf = (c) => st.taught.get(String(c.id)) || new Map();

    // ---------- small calculators ----------
    const byEmail = (email) => st.students.find((s) => s.email === email);
    const doneOf = (email) => st.progress.get(email) || new Map();
    const slugsOf = (p, subject) => {
      const out = new Set();
      (subject ? [subject] : p.subs).forEach((k) => catalog.courses[k]?.slugs.forEach((s) => out.add(s)));
      return out;
    };
    const lessonPct = (p, subject) => { const all = slugsOf(p, subject), d = doneOf(p.email); return pct([...all].filter((s) => d.has(s)).length, all.size); };
    const testsOf = (emails) => { const set = new Set(emails); return st.tests.filter((t) => set.has(t.email)); };
    const lastTest = (email) => { const r = st.tests.filter((t) => t.email === email); return r.length ? r[r.length - 1] : null; };
    const activeLabel = (p) => (p.signed_up_at || p.last_seen ? (p.last_seen ? "Active " + fmt(p.last_seen) : "Signed up") : "Not signed up");

    // ---------- shared pieces ----------
    const greet = () => { const h = new Date().getHours(); return h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : "Good evening"; };
    const first = (me.name || "").trim().split(/\s+/)[0] || me.name;
    const tile = (accent, big, label, hint) => `<div class="stat" data-accent="${accent}"><span class="statbig">${big}</span><b>${label}</b><span class="hint">${hint}</span></div>`;

    function alerts() {
      const a = [];
      if (school) {
        const resets = st.students.filter((p) => p.reset_requested_at);
        if (!R.isLive(sc)) a.push(`<b>Your licence has ended.</b> Students cannot open lessons until it is renewed. Their progress is kept. <a class="lnk" href="${S.base}plan/">See your plan</a>`);
        else if (sc.expires_at && new Date(sc.expires_at) - Date.now() < 30 * DAY) a.push(`<b>Your licence ends ${fmt(sc.expires_at)}.</b> <a class="lnk" href="${S.base}plan/">Renewal options</a>`);
        if (resets.length) a.push(`<b>${plural(resets.length, "student")}</b> asked for a password reset: ${resets.map((p) => `<a class="lnk" href="#students">${esc(p.name)}</a>`).join(", ")}.`);
        const unsigned = st.students.filter((p) => !p.signed_up_at).length;
        if (unsigned) a.push(`${plural(unsigned, "student")} ${unsigned === 1 ? "has" : "have"} not signed in yet. Their logins are on the Students tab.`);
      }
      if (st.schemaMissing) a.push(`<b>Classes and test results need a database update.</b> Run the latest <code>supabase/schema.sql</code> in the Supabase SQL Editor.`);
      return a.length ? `<section class="card block attn"><ul class="plain">${a.map((x) => `<li>${x}</li>`).join("")}</ul></section>` : "";
    }

    function header(active) {
      const tabs = [];
      if (hasData) tabs.push(["classes", classesWord], ["students", tutor ? `Students (${st.students.length})` : "Students"]);
      if (school) tabs.push(["add", "Add students"]);
      tabs.push(["tests", "Tests & mark schemes"]);
      const week = Date.now() - 7 * DAY, monthAvg = avg(st.tests.filter((t) => new Date(t.at) > Date.now() - 30 * DAY).map((t) => t.pct));
      const tiles = hasData ? `<div class="stat-tiles">
        ${tile("teal", st.students.length, "Students", school ? esc(R.seatText(catalog, sc, st.students)) : "on the roster")}
        ${tile("indigo", st.classes.length, classesWord, st.classes.length ? "tap one to see its tracker" : "none yet")}
        ${tile("green", st.students.filter((p) => p.last_seen && new Date(p.last_seen).getTime() >= week).length, "Active this week", "signed in within 7 days")}
        ${tile("amber", show(monthAvg), "Topic test average", "last 30 days")}</div>` : "";
      return `<section class="dash-head"><p class="kicker">${admin ? "Teacher dashboard" : tutor ? "Tutor dashboard" : school ? "Teacher dashboard" : "Teaching resources"}</p><h1>${greet()}, ${esc(first)}</h1>
        <p class="hint">${school ? esc(sc.name) + " · " + esc(R.licenceLine(catalog, sc, st.students)) : courseKeys.map((k) => esc(catalog.courses[k].title)).join(" · ")}</p>
        ${admin ? `<p class="hint"><a class="lnk" href="${S.profileUrl}">Admin console: add students, passwords, schools, approvals →</a></p>` : ""}
        ${school ? `<p class="hint"><a class="lnk" href="${S.base}plan/">Your plan and licence →</a></p>` : ""}</section>
        ${alerts()}${tiles}
        ${tabs.length > 1 ? `<div class="tabs dtabs" role="tablist">${tabs.map(([k, l]) => `<button role="tab" data-tab="${k}" class="${k === active ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}`;
    }

    // ---------- classes ----------
    // What a class has been taught: ticks from the lesson pages, against the lessons in the class's subject.
    function coverage(c) {
      if (!c.subject || !catalog.courses[c.subject]) return null;
      const course = catalog.courses[c.subject], t = taughtOf(c), n = course.slugs.filter((s) => t.has(s)).length;
      const next = catalog.order.find((s) => course.slugs.includes(s) && !t.has(s));
      const recent = [...t.entries()].filter(([s]) => catalog.artifacts[s]).sort((a, b) => (b[1] || "").localeCompare(a[1] || "")).slice(0, 5);
      return { course, t, n, total: course.slugs.length, pct: pct(n, course.slugs.length), next, recent };
    }

    function classCard(c) {
      const members = c.members.map(byEmail).filter(Boolean);
      const lp = avg(members.map((p) => lessonPct(p, c.subject))), tavg = avg(testsOf(c.members).map((t) => t.pct));
      const cov = coverage(c);
      const acc = c.subject ? catalog.courses[c.subject]?.accent : "teal";
      return `<article class="card" data-accent="${acc}"><span class="tag">${c.subject ? esc(R.shortTitle(catalog, c.subject)) : "Mixed"}</span>
        <a class="t" href="#class=${c.id}">${esc(c.name)}</a>
        <span class="sub">${plural(members.length, "student")} · taught ${cov ? cov.pct + "%" : "–"} · student lessons ${show(lp)} · test average ${show(tavg)}</span>
        <span class="foot"><a class="go" href="#class=${c.id}">Open tracker →</a></span></article>`;
    }

    function viewClasses() {
      root.innerHTML = header("classes") + (st.classes.length
        ? `<div class="grid arts">${st.classes.map(classCard).join("")}</div>`
        : `<section class="card block"><h3>No ${classesWord.toLowerCase()} yet</h3><p class="hint">${admin
            ? "Classes come from the groups you tick on each student in the admin console (IG1, IG2, AL)."
            : tutor ? "A group is a few students you track together, for example a Tuesday session. You can also open any student on their own from the Students tab."
              : "Make a class for each teaching group, add its students, and you get a tracker for the whole class: who has finished lessons, topic test scores and trends."}</p></section>`)
        + (school ? `<p><button class="btn" id="newclass">New ${classWord}</button></p>` : "")
        + `<dialog id="dlg" class="wide"><form method="dialog" id="f-dlg"></form></dialog>`;
      $("#newclass")?.addEventListener("click", () => classEditor(null));
    }

    function classEditor(c) {
      const f = $("#f-dlg"), picked = new Set(c ? c.members : []);
      f.innerHTML = `<div class="row"><h3>${c ? "Edit" : "New"} ${classWord}</h3><button class="btn ghost" value="close" formnovalidate>Close</button></div>
        <label>Name<input name="name" required maxlength="60" value="${esc(c ? c.name : "")}" placeholder="${tutor ? "Tuesday after-school" : "Year 12 Economics"}"></label>
        <label>Subject <span class="hint">(optional: used for lesson progress)</span><select name="subject"><option value="">Mixed or not set</option>
          ${sc.products.filter((k) => catalog.courses[k]).map((k) => `<option value="${k}" ${c && c.subject === k ? "selected" : ""}>${esc(catalog.courses[k].title)}</option>`).join("")}</select></label>
        <p class="hint" style="margin-top:12px">Students</p>
        ${st.students.length ? `<div class="chks pickstu">${st.students.map((p) => `<label class="chk"><input type="checkbox" value="${esc(p.email)}" ${picked.has(p.email) ? "checked" : ""}> ${esc(p.name)}</label>`).join("")}</div>`
          : `<p class="hint">Add students first, then put them in a ${classWord}.</p>`}
        <p class="msg err" hidden></p><p><button class="btn" value="save">Save</button></p>`;
      $("#dlg").showModal();
      f.onsubmit = async (ev) => {
        if (ev.submitter?.value !== "save") return;
        ev.preventDefault();
        const m = $(".msg", f), members = [...f.querySelectorAll(".pickstu input:checked")].map((x) => x.value);
        const { data, error } = await sb.rpc("teacher_save_class", { _id: c ? c.id : null, _name: f.elements.name.value, _subject: f.elements.subject.value || null, _members: members });
        if (error) return msg(m, error.message, false);
        $("#dlg").close();
        await refresh();
        location.hash = "class=" + data;
      };
    }

    // ---------- reminders ----------
    // Pick an assessment or topic test; students in `emails` who have not taken it are listed with a Remind button.
    // A reminder shows on the student's own dashboard until they take it. The server allows one per student and item a day.
    const dayAgo = () => Date.now() - DAY;
    function remindCard(emails, subjects) {
      const groups = subjects.filter((k) => catalog.courses[k]).map((k) => {
        const course = catalog.courses[k];
        const as = Object.keys(catalog.assessed || {}).filter((x) => course.slugs.includes(x) && catalog.artifacts[x]);
        const ts = Object.keys(catalog.tests || {}).filter((id) => id.split("/")[0] === k).sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
        return `${as.length ? `<optgroup label="${esc(course.title)}: assessments">${as.map((x) => `<option value="a:${esc(x)}">${esc(catalog.artifacts[x].title)}</option>`).join("")}</optgroup>` : ""}
          ${ts.length ? `<optgroup label="${esc(course.title)}: topic tests">${ts.map((id) => `<option value="t:${esc(id)}">${esc(catalog.tests[id].title.replace(/: topic test$/, ""))}</option>`).join("")}</optgroup>` : ""}`;
      }).join("");
      return `<section class="card block remind" data-emails="${esc(emails.join(","))}"><h3>Send a reminder</h3>
        <p class="hint">Choose an assessment or topic test. Anyone who has not taken it is listed. A reminder appears on their dashboard until they take it.</p>
        <label class="hint">Assessment or test<select class="rem-item"><option value="">Choose one…</option>${groups}</select></label><div class="rem-list"></div></section>`;
    }

    function wireRemind() {
      const card = $(".remind");
      if (!card) return;
      const emails = card.dataset.emails.split(",").filter(Boolean), sel = $(".rem-item", card), list = $(".rem-list", card);
      const draw = () => {
        if (!sel.value) { list.innerHTML = ""; return; }
        const kind = sel.value[0] === "a" ? "assessment" : "test", item = sel.value.slice(2);
        const taken = (e) => (kind === "assessment" ? st.assess.some((a) => a.email === e && a.slug === item) : st.tests.some((t) => t.email === e && t.test === item));
        const pending = emails.filter((e) => byEmail(e) && !taken(e));
        const last = (e) => st.sent.find((r) => r.email === e && r.kind === kind && r.item === item);
        const fresh = (e) => { const r = last(e); return r && new Date(r.at).getTime() > dayAgo(); };
        const todo = pending.filter((e) => !fresh(e));
        list.innerHTML = !pending.length ? `<p class="hint">Everyone has taken this. Nothing to send.</p>`
          : `<div class="row" style="margin-top:12px"><span class="hint">${pending.length} of ${emails.length} not taken yet</span>${todo.length > 1 ? `<button class="mini ok" data-all="1">Remind all (${todo.length})</button>` : ""}</div>
            <div class="tablewrap"><table class="tbl"><tbody>${pending.map((e) => {
              const r = last(e), p = byEmail(e);
              return `<tr data-e="${esc(e)}"><td><b>${esc(p.name)}</b></td><td class="hint">${r ? "Reminded " + fmt(r.at) : "Not reminded yet"}</td>
                <td class="acts">${fresh(e) ? '<span class="hint">Reminded today</span>' : '<button class="mini ok" data-one="1">Remind</button>'}</td></tr>`;
            }).join("")}</tbody></table></div><p class="msg" hidden></p>`;
        const send = async (who) => {
          const m = $(".msg", list), { data, error } = await sb.rpc("send_reminders", { _emails: who, _kind: kind, _item: item });
          if (error) { if (m) msg(m, error.message, false); return; }
          const now = new Date().toISOString();
          who.forEach((e) => { st.sent = st.sent.filter((r) => !(r.email === e && r.kind === kind && r.item === item)); st.sent.push({ email: e, kind, item, at: now }); });
          draw();
          const m2 = $(".msg", list);
          if (m2) msg(m2, data ? `Reminder sent to ${plural(data, "student")}.` : "No new reminders were needed.", true);
        };
        list.querySelector("[data-all]")?.addEventListener("click", (ev) => { ev.target.disabled = true; send(todo); });
        list.querySelectorAll("[data-one]").forEach((b) => b.addEventListener("click", () => { b.disabled = true; send([b.closest("tr").dataset.e]); }));
      };
      sel.addEventListener("change", draw);
    }

    function coverageCard(c) {
      const cv = coverage(c);
      if (!cv) return `<section class="card block"><h3>What you have taught</h3><p class="hint">${school ? `Set a subject on this ${classWord} (Edit ${classWord}) to track what you have taught it.` : "No subject for this class."}</p></section>`;
      const nx = cv.next && catalog.artifacts[cv.next];
      return `<section class="card block" data-accent="${cv.course.accent}"><div class="row"><h3>What you have taught</h3><span class="big">${cv.pct}%</span></div>
        <div class="bar2"><i style="width:${cv.pct}%"></i></div><p class="hint">${cv.n} of ${cv.total} lessons in ${esc(cv.course.title)}. Tick "Mark taught" on a lesson page and choose this ${classWord}.</p>
        ${K.chapterMap(cv.course, cv.t, S.base)}
        ${nx ? `<p style="margin-top:14px"><b>Next lesson:</b> <a class="lnk" href="${S.base}${nx.url}">${esc(nx.title)}</a> <span class="hint">${esc(nx.chapterTitle)}</span></p>` : '<p class="hint" style="margin-top:14px">Every lesson in this subject is marked taught.</p>'}
        ${cv.recent.length ? `<p class="hint" style="margin-top:10px">Recently taught: ${cv.recent.map(([s, d]) => `<a class="lnk" href="${S.base}${catalog.artifacts[s].url}">${esc(catalog.artifacts[s].title)}</a> <span class="hint">${fmt(d)}</span>`).join(" · ")}</p>` : ""}</section>`;
    }

    function viewClass(id) {
      const c = st.classes.find((x) => String(x.id) === String(id));
      if (!c) { location.hash = "classes"; return; }
      const members = c.members.map(byEmail).filter(Boolean), tl = testsOf(c.members);
      const taken = new Set(tl.map((t) => t.email)).size;
      const topics = new Map();
      tl.forEach((t) => { if (!topics.has(t.test)) topics.set(t.test, { title: t.title, by: new Map() }); topics.get(t.test).by.set(t.email, t); });
      const topicRows = [...topics.entries()].map(([test, o]) => {
        const rs = tl.filter((t) => t.test === test), bests = [...o.by.keys()].map((e) => Math.max(...rs.filter((r) => r.email === e).map((r) => r.pct)));
        return `<tr><td><a class="lnk" href="${S.base}${test}/">${esc(o.title)}</a></td><td>${o.by.size} of ${members.length}</td><td>${avg(bests)}%</td><td>${Math.min(...bests)}%</td><td>${rs.length}</td></tr>`;
      }).join("");
      const rows = members.map((p) => {
        const mine = tl.filter((t) => t.email === p.email), lt = mine[mine.length - 1];
        return `<tr><td><a class="lnk" href="#student=${encodeURIComponent(p.email)}"><b>${esc(p.name)}</b></a></td><td>${lessonPct(p, c.subject)}%</td>
          <td>${new Set(mine.map((t) => t.test)).size}</td><td>${lt ? `<b>${lt.pct}%</b>` : "–"}</td><td>${show(avg(mine.map((t) => t.pct)))}</td>
          <td class="hint">${p.last_seen ? fmt(p.last_seen) : "–"}</td></tr>`;
      }).join("");
      root.innerHTML = `<p class="hint"><a class="lnk" href="#classes">← ${classesWord}</a></p>
        <section class="dash-head"><p class="kicker">${tutor ? "Group" : "Class"} tracker</p><h1>${esc(c.name)}</h1>
          <p class="hint">${c.subject ? esc(catalog.courses[c.subject].title) + " · " : ""}${plural(members.length, "student")}</p>
          ${school ? `<p><button class="mini" id="editclass">Edit ${classWord}</button> <button class="mini danger" id="delclass">Delete ${classWord}</button></p>` : ""}</section>
        <div class="stat-tiles">
          ${tile("teal", show(avg(members.map((p) => lessonPct(p, c.subject)))), "Lesson progress", "average across the " + classWord)}
          ${tile("indigo", `${taken}/${members.length}`, "Taken a topic test", "students with at least one")}
          ${tile("green", show(avg(tl.map((t) => t.pct))), "Test average", plural(tl.length, "attempt") + " in all")}
          ${tile("amber", show(tl.length ? Math.max(...tl.map((t) => t.pct)) : null), "Best score", "highest attempt")}</div>
        ${coverageCard(c)}
        ${remindCard(c.members, c.subject ? [c.subject] : courseKeys)}
        <section class="card block"><h3>Test scores over time</h3><p class="hint">One point per week per subject: the average of every attempt that week. Hover a dot for the detail.</p>
          ${tl.length ? K.chart(K.weekly(tl), catalog, "Class topic test average by week") : '<p class="hint">No topic test attempts from this ' + classWord + " yet.</p>"}</section>
        <section class="card block"><h3>Students</h3>${members.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Student</th><th>Lessons</th><th>Topics tested</th><th>Latest test</th><th>Test average</th><th>Last active</th></tr></thead><tbody>${rows}</tbody></table></div>
          <p class="hint">Select a name for that student's full tracker.</p>` : `<p class="hint">No students in this ${classWord} yet.</p>`}</section>
        ${topicRows ? `<section class="card block"><h3>Topic by topic</h3><p class="hint">Where the ${classWord} is strong and where it is not. Each student counts once, at their best score on the topic.</p>
          <div class="tablewrap"><table class="tbl"><thead><tr><th>Topic</th><th>Taken by</th><th>Average best</th><th>Lowest best</th><th>Attempts</th></tr></thead><tbody>${topicRows}</tbody></table></div></section>` : ""}
        <dialog id="dlg" class="wide"><form method="dialog" id="f-dlg"></form></dialog>`;
      wireRemind();
      $("#editclass")?.addEventListener("click", () => classEditor(c));
      $("#delclass")?.addEventListener("click", async () => {
        if (!confirm(`Delete the ${classWord} "${c.name}"? The students and their progress are not affected.`)) return;
        const { error } = await sb.rpc("teacher_delete_class", { _id: c.id });
        if (error) return alert(error.message);
        await refresh(); location.hash = "classes";
      });
    }

    // ---------- one student ----------
    function viewStudent(email) {
      const p = byEmail(email);
      if (!p) { location.hash = "students"; return; }
      const mine = st.tests.filter((t) => t.email === email), d = doneOf(email);
      const inClasses = st.classes.filter((c) => c.members.includes(email));
      const asses = st.assess.filter((a) => a.email === email && catalog.artifacts[a.slug]);
      const subjectBlocks = p.subs.map((k) => {
        const c = catalog.courses[k], n = c.slugs.filter((s) => d.has(s)).length;
        return `<section class="card block" data-accent="${c.accent}"><div class="row"><h3><a href="${S.base}${c.url}">${esc(c.title)}</a></h3><span class="big">${pct(n, c.slugs.length)}%</span></div>
          <div class="bar2"><i style="width:${pct(n, c.slugs.length)}%"></i></div><p class="hint">${n} of ${c.slugs.length} activities done.</p>${K.chapterMap(c, d, S.base)}</section>`;
      }).join("");
      const lt = mine[mine.length - 1];
      root.innerHTML = `<p class="hint"><a class="lnk" href="#students">← Students</a></p>
        <section class="dash-head"><p class="kicker">${tutor ? "Student tracker" : "Student"}</p><h1>${esc(p.name)}</h1>
          <p class="hint">${esc(p.email)}${p.email2 ? " · " + esc(p.email2) : ""} · ${esc(activeLabel(p))}</p>
          ${inClasses.length ? `<p class="hint">${inClasses.map((c) => `<a class="pill soft" href="#class=${c.id}">${esc(c.name)}</a>`).join(" ")}</p>` : ""}</section>
        <div class="stat-tiles">
          ${tile("teal", show(p.subs.length ? lessonPct(p) : null), "Lesson progress", p.subs.map((k) => esc(R.shortTitle(catalog, k))).join(", ") || "no subjects")}
          ${tile("indigo", new Set(mine.map((t) => t.test)).size, "Topics tested", plural(mine.length, "attempt"))}
          ${tile("green", show(avg(mine.map((t) => t.pct))), "Test average", lt ? "latest " + lt.pct + "%" : "no attempts yet")}
          ${tile("amber", show(mine.length ? Math.max(...mine.map((t) => t.pct)) : null), "Best score", "highest attempt")}</div>
        <section class="card block"><h3>Topic test scores over time</h3><p class="hint">Every attempt is kept. Hover a dot for the detail.</p>
          ${mine.length ? K.chart(mine, catalog, "Topic test scores over time") : '<p class="hint">No topic tests taken yet.</p>'}</section>
        ${mine.length ? `<section class="card block"><h3>By topic</h3><p class="hint">First attempt against best and latest, to show improvement.</p>
          <div class="tablewrap"><table class="tbl"><thead><tr><th>Topic</th><th>Attempts</th><th>First</th><th>Best</th><th>Latest</th><th>Change</th></tr></thead><tbody>${K.byTopic(mine, (t) => S.base + t + "/")}</tbody></table></div></section>
          <section class="card block"><h3>All attempts</h3><div class="tablewrap"><table class="tbl"><thead><tr><th>Topic</th><th>Score</th><th>Multiple choice</th><th>Written</th><th>When</th></tr></thead><tbody>
          ${[...mine].reverse().map((r) => `<tr><td>${esc(r.title)}</td><td><b>${r.pct}%</b> <span class="hint">${r.score}/${r.max}</span></td><td>${r.mcq ?? "–"}${r.mcq_max ? "/" + r.mcq_max : ""}</td><td>${r.written ?? "–"}${r.written_max ? "/" + r.written_max : ""}</td><td class="hint">${fmt(r.at)}</td></tr>`).join("")}</tbody></table></div></section>` : ""}
        ${asses.length ? `<section class="card block"><h3>Lesson assessments</h3><div class="tablewrap"><table class="tbl"><thead><tr><th>Lesson</th><th>Score</th><th>When</th></tr></thead><tbody>
          ${asses.map((a) => `<tr><td>${esc(catalog.artifacts[a.slug].title)}</td><td><b class="${a.pct >= (catalog.assessed[a.slug]?.pass ?? 80) ? "ok-txt" : "no-txt"}">${a.pct}%</b></td><td class="hint">${fmt(a.at)}</td></tr>`).join("")}</tbody></table></div></section>` : ""}
        ${remindCard([p.email], p.subs)}
        <h2 class="dash-h2" style="margin-top:28px">Lesson progress</h2>${subjectBlocks || '<p class="hint">No subjects on this student yet.</p>'}`;
      wireRemind();
    }

    // ---------- students ----------
    function viewStudents() {
      const needle = q.trim().toLowerCase();
      // Filter options fill themselves from the data: every class that has students, and each subject more than one student takes.
      const subjCount = {};
      st.students.forEach((p) => p.subs.forEach((k) => { subjCount[k] = (subjCount[k] || 0) + 1; }));
      const subjOpts = Object.keys(subjCount).filter((k) => catalog.courses[k]);
      if (cf && !(cf.startsWith("c:") ? st.classes.some((c) => "c:" + c.id === cf) : subjOpts.includes(cf.slice(2)))) cf = "";
      const inFilter = (p) => !cf || (cf.startsWith("c:") ? st.classes.find((c) => "c:" + c.id === cf).members.includes(p.email) : p.subs.includes(cf.slice(2)));
      const list = st.students.filter((p) => inFilter(p) && (!needle || p.name.toLowerCase().includes(needle) || p.email.includes(needle)));
      list.sort((a, b) => (b.reset_requested_at ? 1 : 0) - (a.reset_requested_at ? 1 : 0));
      const rows = list.map((p) => {
        const lt = lastTest(p.email), cls = st.classes.filter((c) => c.members.includes(p.email));
        return `<tr data-email="${esc(p.email)}"><td><a class="lnk" href="#student=${encodeURIComponent(p.email)}"><b>${esc(p.name)}</b></a>${p.reset_requested_at ? ' <span class="pill soft">Password reset requested</span>' : ""}<br>
          <span class="hint">${esc(p.email)}${p.email2 ? `<br>${esc(p.email2)}` : ""}</span>${cls.length ? `<br>${cls.map((c) => `<span class="pill soft">${esc(c.name)}</span>`).join(" ")}` : ""}</td>
          ${school ? `<td><code>${esc(p.password)}</code></td>` : ""}${school && sc.per_subject ? `<td>${p.subs.map((k) => esc(R.shortTitle(catalog, k))).join(", ") || "None"}</td>` : ""}
          <td>${esc(activeLabel(p))}</td><td>${lessonPct(p)}%</td><td>${lt ? `<b>${lt.pct}%</b>` : "–"}</td>
          <td class="acts"><a class="mini ok" href="#student=${encodeURIComponent(p.email)}">Tracker</a>${school ? `${sc.per_subject ? '<button class="mini" data-act="subs">Subjects</button>' : ""}<button class="mini" data-act="reset">Reset login</button><button class="mini danger" data-act="rm">Remove</button>` : ""}</td></tr>`;
      }).join("");
      root.innerHTML = header("students") + `<section class="card block"><div class="row"><h3>Students (${list.length === st.students.length ? list.length : list.length + " of " + st.students.length})</h3>
          <span>${school && st.students.length ? '<button class="mini" id="copypw">Copy logins as table</button>' : ""}</span></div>
        ${st.students.length ? `<div class="filters"><label class="hint">Find a student<input type="search" id="find" value="${esc(q)}" placeholder="Name or email"></label>
          ${st.classes.length || subjOpts.length > 1 ? `<label class="hint">${classesWord} or subject<select id="cfilter"><option value="">All students</option>
            ${st.classes.length ? `<optgroup label="${classesWord}">${st.classes.map((c) => `<option value="c:${c.id}" ${cf === "c:" + c.id ? "selected" : ""}>${esc(c.name)} (${c.members.length})</option>`).join("")}</optgroup>` : ""}
            ${subjOpts.length > 1 ? `<optgroup label="Subject">${subjOpts.map((k) => `<option value="s:${k}" ${cf === "s:" + k ? "selected" : ""}>${esc(catalog.courses[k].title)} (${subjCount[k]})</option>`).join("")}</optgroup>` : ""}</select></label>` : ""}</div>
          <div class="tablewrap"><table class="tbl"><thead><tr><th>Student</th>${school ? "<th>Password</th>" : ""}${school && sc.per_subject ? "<th>Subjects</th>" : ""}<th>Status</th><th>Lessons</th><th>Latest test</th><th></th></tr></thead><tbody id="sstu">${rows}</tbody></table></div>
          ${school ? '<p class="hint">If a student changes their own password, the one listed here is out of date. Reset login puts it back to the listed one.</p>' : ""}`
          : `<p class="hint">No students yet.${school ? " Use the Add students tab." : ""}</p>`}</section>
        <dialog id="dlg" class="wide"><form method="dialog" id="f-dlg"></form></dialog>`;
      const find = $("#find");
      find?.addEventListener("input", () => { q = find.value; const pos = find.selectionStart; viewStudents(); const f2 = $("#find"); f2.focus(); f2.setSelectionRange(pos, pos); });
      $("#cfilter")?.addEventListener("change", (e) => { cf = e.target.value; viewStudents(); });
      $("#copypw")?.addEventListener("click", async () => {
        await navigator.clipboard.writeText(["Name\tEmail\tEmail 2\tPassword", ...st.students.map((p) => [p.name, p.email, p.email2 || "", p.password].join("\t"))].join("\n"));
        $("#copypw").textContent = "Copied";
      });
      $("#sstu")?.addEventListener("click", async (e) => {
        const btn = e.target.closest("[data-act]");
        if (!btn) return;
        const p = byEmail(btn.closest("tr").dataset.email);
        if (btn.dataset.act === "subs") {
          const have = R.schoolSubs(sc, p), f = $("#f-dlg");
          f.innerHTML = `<div class="row"><h3>${esc(p.name)}: subjects</h3><button class="btn ghost" value="close" formnovalidate>Close</button></div>
            <p class="hint">Tick the subjects this student takes. Changing them uses or frees a seat in each subject.</p>
            <div class="chks" id="subsbox">${sc.products.filter((k) => catalog.courses[k]).map((k) => `<label class="chk"><input type="checkbox" value="${k}" ${have.includes(k) ? "checked" : ""}> ${esc(catalog.courses[k].title)}</label>`).join("")}</div>
            <p><button class="btn" type="button" id="savesubs">Save subjects</button> <span class="msg" id="subsmsg" hidden></span></p>`;
          $("#dlg").showModal();
          $("#savesubs").addEventListener("click", async () => {
            const chosen = [...$("#subsbox").querySelectorAll("input:checked")].map((c) => c.value), m = $("#subsmsg");
            if (!chosen.length) return msg(m, "Tick at least one subject.", false);
            const { error } = await sb.rpc("school_set_student_subjects", { _email: p.email, _subjects: chosen });
            if (error) return msg(m, error.message.replace(/^.*?All /, "All "), false);
            $("#dlg").close(); await refresh();
          });
        } else if (btn.dataset.act === "reset") {
          if (!confirm(`Recreate the login for ${p.name} with the listed password? Their progress is kept.`)) return;
          const { error } = await sb.rpc("school_reset_login", { _email: p.email });
          alert(error ? "Could not reset: " + error.message : `Done. ${p.name} can sign in with: ${p.password}`);
          if (!error) await refresh();
        } else if (confirm(`Remove ${p.name} from ${sc.name}? This frees their seat. They lose access to these lessons; their progress is kept if they're added back.`)) {
          const { error } = await sb.rpc("school_remove_student", { _email: p.email });
          if (error) alert(error.message); else await refresh();
        }
      });
    }

    // ---------- add students ----------
    function viewAdd() {
      const left = sc.per_subject ? null : Math.max(0, sc.seats - st.students.length), subjects = sc.products.filter((k) => catalog.courses[k]);
      root.innerHTML = header("add") + `<section class="card block"><h3>Add students</h3>
        <p class="hint">${sc.per_subject ? esc(R.seatText(catalog, sc, st.students)) + "." : plural(left, "seat") + " free of " + sc.seats + "."} A password is generated for each student; give it to them with their email.</p>
        ${sc.per_subject ? `<p class="hint">Subjects for the students you add</p><div class="chks" id="addsubs">${subjects.map((k) => `<label class="chk"><input type="checkbox" value="${k}" checked> ${esc(catalog.courses[k].title)}</label>`).join("")}</div>` : ""}
        <form id="f-sadd"><label>One student per line: <b>Name, email</b> or <b>Name, email, second email</b>
          <textarea name="lines" rows="6" required placeholder="An Nguyen, an@gmail.com"></textarea></label>
          ${st.classes.length ? `<label>Add them to a ${classWord} <span class="hint">(optional)</span><select name="cls"><option value="">None</option>${st.classes.map((c) => `<option value="${c.id}">${esc(c.name)}</option>`).join("")}</select></label>` : ""}
          <button class="btn" type="submit" ${(sc.per_subject || left) && R.isLive(sc) ? "" : "disabled"}>Add students</button><p class="msg" hidden></p></form></section>`;
      $("#f-sadd").addEventListener("submit", async (e) => {
        e.preventDefault();
        const f = e.target, m = $(".msg", f), { rows: list, bad } = R.parseStudentLines(f.lines.value);
        if (bad.length) return msg(m, `Check these lines (need a name and one or two valid emails): ${bad.join(" | ")}`, false);
        const picked = sc.per_subject ? [...root.querySelectorAll("#addsubs input:checked")].map((c) => c.value) : null;
        if (sc.per_subject) {
          if (!picked.length) return msg(m, "Tick at least one subject.", false);
          const full = picked.find((k) => R.seatCap(sc, k) - R.seatsUsed(sc, st.students, k) < list.length);
          if (full) return msg(m, `That's ${list.length} students but ${catalog.courses[full].title} has only ${plural(Math.max(0, R.seatCap(sc, full) - R.seatsUsed(sc, st.students, full)), "seat")} left.`, false);
        } else if (list.length > left) return msg(m, `That's ${list.length} students but only ${plural(left, "seat")} left.`, false);
        const taken = new Set(st.students.map((x) => x.password)), added = [];
        for (const [i, r] of list.entries()) {
          const password = R.genPassword(taken); taken.add(password);
          const { error } = await sb.rpc("school_add_student", { _name: r.name, _email: r.email, _email2: r.email2, _password: password, _subjects: picked });
          if (error) { msg(m, `${i ? `Added ${plural(i, "student")}. ` : ""}Stopped at "${r.line}": ${error.message}`, false); await refresh(false); return; }
          added.push(r.email);
        }
        const c = st.classes.find((x) => String(x.id) === f.elements.cls?.value);
        if (c) await sb.rpc("teacher_save_class", { _id: c.id, _name: c.name, _subject: c.subject, _members: [...c.members, ...added] });
        await refresh(false);
        location.hash = "students";
      });
    }

    // ---------- tests and mark schemes ----------
    function viewTests() {
      const tests = catalog.tests || {};
      const groups = courseKeys.map((k) => {
        const ids = Object.keys(tests).filter((id) => id.split("/")[0] === k).sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
        return { k, ids };
      }).filter((g) => g.ids.length);
      root.innerHTML = header("tests") + `<section class="card block"><h3>Topic tests and mark schemes</h3>
        <p class="hint">Each test has ten multiple choice questions and written questions. Open one to see the answer key, mark points and model answers, then print it as a mark scheme or a student copy.</p>
        ${groups.length ? groups.map((g, i) => `<details class="tsub" ${i === 0 ? "open" : ""}><summary><b>${esc(catalog.courses[g.k].title)}</b> <span class="hint">${plural(g.ids.length, "test")}</span></summary>
          <ul class="plain tlist">${g.ids.map((id) => `<li><a class="lnk" href="${S.base}tests/?t=${encodeURIComponent(id)}">${esc(tests[id].title.replace(/: topic test$/, ""))}</a> <span class="hint">${tests[id].marks} marks</span></li>`).join("")}</ul></details>`).join("")
          : '<p class="hint">No topic tests for your subjects yet.</p>'}</section>
        ${courseKeys.length ? `<h2 class="dash-h2" style="margin-top:28px">Course maps</h2><div class="grid two">${courseKeys.map((k) => { const c = catalog.courses[k];
          return `<section class="card block" data-accent="${c.accent}"><h3><a href="${S.base}${c.url}">${esc(c.title)}</a></h3>${K.chapterMap(c, new Map(), S.base)}</section>`; }).join("")}</div>` : ""}`;
    }

    // ---------- routing ----------
    function view() {
      const h = decodeURIComponent(location.hash.slice(1));
      if (hasData && h.startsWith("class=")) return viewClass(h.slice(6));
      if (hasData && h.startsWith("student=")) return viewStudent(h.slice(8));
      const tab = h || (hasData ? (tutor ? "students" : "classes") : "tests");
      if (tab === "students" && hasData) viewStudents();
      else if (tab === "add" && school) viewAdd();
      else if (tab === "tests" || !hasData) viewTests();
      else viewClasses();
      window.scrollTo(0, 0);
    }
    async function refresh(redraw = true) { await load(); await loadTaught(); if (redraw) view(); }

    root.innerHTML = '<p class="hint">Loading your dashboard…</p>';
    try { if (hasData) { await load(); await loadTaught(); } }
    catch (e) { root.innerHTML = `<p class="msg err">Could not load your dashboard: ${esc(e.message || String(e))}</p>`; return; }
    // Delegated, so the tabs keep working after a view redraws itself (filters, search).
    root.addEventListener("click", (e) => {
      const b = e.target.closest(".dtabs [data-tab]");
      if (b) { if (location.hash.slice(1) === b.dataset.tab) view(); else location.hash = b.dataset.tab; }
    });
    window.addEventListener("hashchange", view);
    view();
  }

  window.TeacherDash = { run };
})();
