// Profile page: sign in, student dashboard, admin console.
(function () {
  const S = window.Site;
  const root = document.getElementById("profile-root");
  const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
  const COURSE_KEYS = ["ig-econ", "ig-cs", "a-econ", "a-cs"];
  let catalog, adminMe = "", adminTab = (() => { try { const t = sessionStorage.getItem("site.admintab"); sessionStorage.removeItem("site.admintab"); return t; } catch (e) { return null; } })(), openClass = null;

  // Three classes, five class-subject groups. Student membership is stored per group (the ids below);
  // joining a group gives the student that group's course.
  const CLASS_LIST = [
    { id: "ig1", title: "IG1", groups: [{ id: "ig1-cs", label: "CS", subject: "ig-cs" }] },
    { id: "ig2", title: "IG2", groups: [{ id: "ig2-cs", label: "CS", subject: "ig-cs" }, { id: "ig2-econ", label: "Econ", subject: "ig-econ" }] },
    { id: "al", title: "AL", groups: [{ id: "a-cs", label: "CS", subject: "a-cs" }, { id: "a-econ", label: "Econ", subject: "a-econ" }] },
  ];
  const CLASSES = CLASS_LIST.flatMap((c) => c.groups.map((g) => ({ ...g, cls: c.title, title: `${c.title} ${g.label}` })));
  const classSubjects = (ids) => [...new Set(CLASSES.filter((c) => ids.includes(c.id)).map((c) => c.subject))];
  const union = (a, b) => [...new Set([...a, ...b])];

  const TIERS = ["free", "basic", "full", "vip"], TIER_NAMES = { free: "Free", basic: "Basic", full: "Full", vip: "VIP" };
  const tierSelect = (name, v = "full", label = "Tier") =>
    `<label>${label}<select name="${name}">${TIERS.map((t) => `<option value="${t}" ${t === v ? "selected" : ""}>${TIER_NAMES[t]}</option>`).join("")}</select></label>`;
  const isLive = (sc) => !sc.expires_at || new Date(sc.expires_at) > new Date();
  const licenceLine = (sc, used) => `${TIER_NAMES[sc.tier]} · ${used} of ${sc.seats} seats used · ${sc.expires_at ? (isLive(sc) ? "ends " : "ended ") + fmt(sc.expires_at) : "no end date"}`;

  // Academic words for assigned passwords: two words and two digits, e.g. OutcomeMethod47.
  const WORDS = ("analyse approach assess assume benefit concept consist context contrast create data define derive "
    + "design device distinct economy element evaluate evidence factor feature final focus formula function "
    + "framework hypothesis identify illustrate impact indicate input interpret issue labour layer logic margin "
    + "method model monitor network norm obtain outcome output parallel phase policy predict principle process "
    + "project quote range ratio region relevant research resource response restrict role sector select sequence "
    + "source specific structure survey symbol target theory tradition transfer trend unique valid variable version "
    + "volume").split(" ");
  const cap = (w) => w[0].toUpperCase() + w.slice(1);
  const rnd = (n) => crypto.getRandomValues(new Uint32Array(1))[0] % n;
  function genPassword(taken = new Set()) {
    for (;;) {
      const a = WORDS[rnd(WORDS.length)], b = WORDS[rnd(WORDS.length)];
      const pw = cap(a) + cap(b) + String(10 + rnd(90));
      if (a !== b && !taken.has(pw)) return pw;
    }
  }

  // "Name, email" or "Name, email, second email" per line, as typed into the add-students boxes.
  function parseStudentLines(text) {
    const rows = [], bad = [];
    text.split("\n").map((l) => l.trim()).filter(Boolean).forEach((l) => {
      const parts = l.split(/[,\t;]/).map((x) => x.trim()).filter(Boolean);
      const emails = parts.filter((x) => x.includes("@")).map((x) => x.toLowerCase());
      const name = parts.filter((x) => !x.includes("@")).join(" ").trim();
      const [email, email2] = emails;
      if (!name || !email || emails.length > 2 || !emails.every((x) => EMAIL_RE.test(x)) || email === email2) bad.push(l);
      else rows.push({ line: l, name, email, email2: email2 || null });
    });
    return { rows, bad };
  }

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => (d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "");
  const $ = (sel, el = root) => el.querySelector(sel);
  const msg = (el, text, ok) => { el.textContent = text; el.className = "msg " + (ok ? "ok" : "err"); el.hidden = !text; };

  if (!S.configured) {
    root.innerHTML = `<div class="placeholder"><h2>Accounts are not switched on yet</h2>
      <p>The site owner still needs to connect the account service. See <b>README.md</b>, section "Profile setup".</p></div>`;
    return;
  }
  const sb = S.sb;

  // A reset link lands back on the Profile page carrying a recovery token. Catch it before the normal boot
  // so the user sets a new password instead of being bounced to the dashboard.
  let recovering = location.hash.includes("type=recovery");
  sb.auth.onAuthStateChange((event) => { if (event === "PASSWORD_RECOVERY") { recovering = true; viewRecovery(); } });

  // ---------- signed-out view ----------
  // Class logins are created by the admin panel; anyone with a real email can reset their own password.
  function viewSignedOut() {
    root.innerHTML = `
      <div class="auth-card"><h2>Sign in</h2>
        <form id="f-in">
          <label>Email<input type="email" name="email" autocomplete="username" required></label>
          <label>Password<input type="password" name="password" autocomplete="current-password" required></label>
          <button class="btn" type="submit">Sign in</button><p class="msg" hidden></p>
          <p class="hint">Use the email and password your teacher gave you. If you cannot sign in, ask your teacher.</p>
          <p class="hint"><a href="#" id="forgot">Forgot your password?</a></p>
        </form>
      </div>`;
    $("#forgot").addEventListener("click", (e) => { e.preventDefault(); viewForgot(); });
    $("#f-in").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), btn = $("button", f);
      const email = f.email.value.trim().toLowerCase(), password = f.password.value;
      btn.disabled = true;
      const { error } = await sb.auth.signInWithPassword({ email, password });
      if (error) { btn.disabled = false; return msg(m, "Wrong email or password.", false); }
      // First page after signing in is the dashboard (students); teachers/admins stay on their Profile console.
      const who = await S.whoami(true);
      const next = sessionStorage.getItem("site.next");
      if (next && next.startsWith(S.base)) { sessionStorage.removeItem("site.next"); location.href = next; return; }
      if (who && !who.is_admin && !who.is_teacher && !who.is_school_teacher) { location.href = S.base + "dashboard/"; return; }
      boot();
    });
  }

  // Ask Supabase to email a reset link. The reply never says whether the email exists, to avoid leaking accounts.
  function viewForgot() {
    root.innerHTML = `
      <div class="auth-card"><h2>Reset your password</h2>
        <form id="f-forgot">
          <label>Email<input type="email" name="email" autocomplete="username" required></label>
          <button class="btn" type="submit">Email me a reset link</button><p class="msg" hidden></p>
          <p class="hint">We'll send a link to set a new password. If it doesn't arrive, check your spam folder. Class students can also ask their teacher.</p>
          <p class="hint"><a href="#" id="back">Back to sign in</a></p>
        </form>
      </div>`;
    $("#back").addEventListener("click", (e) => { e.preventDefault(); viewSignedOut(); });
    $("#f-forgot").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), btn = $("button", f);
      const email = f.email.value.trim().toLowerCase();
      btn.disabled = true;
      const { error } = await sb.auth.resetPasswordForEmail(email, { redirectTo: new URL(S.base + "profile/", location.href).href });
      btn.disabled = false;
      if (error && /rate|limit|too many/i.test(error.message)) return msg(m, "Too many attempts. Wait a few minutes and try again.", false);
      msg(m, "If that email has an account, a reset link is on its way.", true);
    });
  }

  // Reached from the emailed link: Supabase signs the user in just long enough to set a new password.
  function viewRecovery() {
    root.innerHTML = `
      <div class="auth-card"><h2>Set a new password</h2>
        <form id="f-rec">
          <label>New password<input type="password" name="password" autocomplete="new-password" minlength="8" required></label>
          <label>Confirm<input type="password" name="confirm" autocomplete="new-password" minlength="8" required></label>
          <button class="btn" type="submit">Save password</button><p class="msg" hidden></p>
        </form>
      </div>`;
    $("#f-rec").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), btn = $("button", f);
      if (f.password.value !== f.confirm.value) return msg(m, "Passwords do not match.", false);
      btn.disabled = true;
      const { error } = await sb.auth.updateUser({ password: f.password.value });
      if (error) { btn.disabled = false; return msg(m, error.message, false); }
      history.replaceState(null, "", location.pathname);  // drop the token from the URL
      recovering = false;
      msg(m, "Password saved. Signing you in…", true);
      const who = await S.whoami(true);
      location.href = who && !who.is_admin && !who.is_teacher && !who.is_school_teacher ? S.base + "dashboard/" : S.base + "profile/";
    });
  }

  // ---------- progress helpers ----------
  const subjectSlugs = (subjects) => {
    const out = new Set();
    subjects.forEach((k) => catalog.courses[k]?.slugs.forEach((s) => out.add(s)));
    return out;
  };
  const pct = (done, total) => (total ? Math.round((100 * done) / total) : 0);

  function pills(subjects) {
    return subjects.length
      ? subjects.filter((k) => catalog.courses[k]).map((k) => `<a class="pill" data-accent="${catalog.courses[k].accent}" href="${S.base}${catalog.courses[k].url}">${esc(catalog.courses[k].title)}</a>`).join("")
      : `<span class="hint">No subjects yet.</span>`;
  }

  function subjectPanel(me) {
    const pend = (me.requested || []).filter((k) => catalog.courses[k]);
    const avail = COURSE_KEYS.filter((k) => !me.subjects.includes(k) && !pend.includes(k));
    const pendHtml = pend.map((k) => `<span class="pill pending" data-accent="${catalog.courses[k].accent}">${esc(catalog.courses[k].title)} · waiting for approval <button class="x" data-cancel="${k}" title="Cancel request">×</button></span>`).join("");
    const req = !me.is_admin && !me.is_teacher && avail.length
      ? `<p class="hint">Join a subject: ${avail.map((k) => `<button class="mini" data-req="${k}">+ ${esc(catalog.courses[k].title)}</button>`).join(" ")}</p>` : "";
    return `<div class="pills">${pills(me.subjects.filter((k) => catalog.courses[k]))}${pendHtml}</div>${req}`;
  }

  function chapterMap(course, done) {
    return course.groups.map((g) => `
      <div class="mapgroup"><h4>${esc(g.title)}</h4><div class="tiles">
      ${g.chapters.map((ch) => {
        const total = ch.slugs.length, n = ch.slugs.filter((s) => done.has(s)).length;
        const st = !total ? "empty" : n === total ? "full" : n ? "part" : "none";
        return `<a class="tile ${st}" href="${S.base}${ch.url}" title="${esc(ch.title)}${total ? ` (${n}/${total} done)` : " (nothing yet)"}">${esc(ch.label)}</a>`;
      }).join("")}</div></div>`).join("");
  }

  const accountCard = () => `<section class="card block"><h3>Account</h3>
        <form id="f-pw" class="inline"><label>New password<input type="password" name="password" autocomplete="new-password" minlength="8" required></label>
        <label>Confirm<input type="password" name="confirm" autocomplete="new-password" minlength="8" required></label>
        <button class="btn" type="submit">Change password</button><p class="msg" hidden></p></form>
        <p><button class="btn ghost" id="signout">Sign out</button></p></section>`;

  const courseTitle = (p) => catalog.courses[p]?.title || (p === "school-all" ? "All subjects" : p);
  function planCard(me) {
    const seen = new Set();
    const ents = (me.entitlements || []).filter((e) => { const k = e.product + "|" + e.tier; if (seen.has(k)) return false; seen.add(k); return true; });
    const body = ents.length
      ? `<ul class="plain">${ents.map((e) => `<li>${esc(courseTitle(e.product))} · <b>${TIER_NAMES[e.tier] || e.tier}</b>${e.expires_at ? ` <span class="hint">until ${fmt(e.expires_at)}</span>` : ""}</li>`).join("")}</ul>`
      : `<p class="hint">You have full access while the site is in its launch period.</p>`;
    return `<section class="card block"><h3>Your plan</h3>${body}<p><a class="lnk" href="${S.base}pricing/">See all plans →</a></p></section>`;
  }

  // ---------- student dashboard ----------
  function viewDashboard(me, done, attempts = []) {
    const mine = me.subjects.filter((k) => catalog.courses[k]);
    const all = subjectSlugs(mine);
    const doneN = [...all].filter((s) => done.has(s)).length;
    const next = catalog.order.find((s) => all.has(s) && !done.has(s));
    const recent = [...done.entries()].filter(([s]) => catalog.artifacts[s]).sort((a, b) => b[1].localeCompare(a[1])).slice(0, 5);
    const perSubject = mine.map((k) => {
      const c = catalog.courses[k], t = c.slugs.length, n = c.slugs.filter((s) => done.has(s)).length;
      return `<section class="card block" data-accent="${c.accent}">
        <div class="row"><h3><a href="${S.base}${c.url}">${esc(c.title)}</a></h3><span class="big">${pct(n, t)}%</span></div>
        <div class="bar2"><i style="width:${pct(n, t)}%"></i></div>
        <p class="hint">${n} of ${t} activities done. Each square is a chapter or syllabus section: filled is all done, half is started, grey has nothing yet.</p>
        ${chapterMap(c, done)}</section>`;
    }).join("");
    const nextA = next && catalog.artifacts[next];

    const account = accountCard();

    // Teachers get the chapter map only: no percentages, up next, history or scores.
    if (me.is_admin || me.is_teacher) {
      const maps = mine.map((k) => {
        const c = catalog.courses[k];
        return `<section class="card block" data-accent="${c.accent}"><h3><a href="${S.base}${c.url}">${esc(c.title)}</a></h3>${chapterMap(c, done)}</section>`;
      }).join("");
      return `<section class="idcard"><h1>${esc(me.name)}</h1><p class="email">${esc(me.email)}${me.email2 ? ` · ${esc(me.email2)}` : ""}</p>${me.is_teacher ? '<p class="hint">Co-teacher: every subject is open to you.</p>' : ""}${subjectPanel(me)}</section><!--split-->
        <p class="hint">Course map. Each square is a chapter or syllabus section: filled means every activity is done, half means started, grey means nothing there yet.</p>${maps}${account}`;
    }

    // The progress overview lives on the dashboard now; the profile keeps subjects, plan and account.
    return `
      <section class="idcard"><h1>${esc(me.name)}</h1><p class="email">${esc(me.email)}${me.email2 ? ` · ${esc(me.email2)}` : ""}${me.school ? ` · ${esc(me.school)}` : ""}</p>${subjectPanel(me)}
        <p class="hint"><a class="btn" href="${S.base}dashboard/">Open your dashboard →</a></p></section><!--split-->
      ${planCard(me)}
      ${account}`;
  }

  function wireAccount() {
    root.querySelectorAll("[data-req],[data-cancel]").forEach((b) => b.addEventListener("click", async () => {
      b.disabled = true;
      const { error } = b.dataset.req ? await sb.rpc("request_subject", { subject: b.dataset.req }) : await sb.rpc("cancel_request", { subject: b.dataset.cancel });
      if (error) { alert(error.message); b.disabled = false; return; }
      boot();
    }));
    $("#f-pw")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f);
      if (f.password.value !== f.confirm.value) return msg(m, "Passwords do not match.", false);
      const { error } = await sb.rpc("set_my_password", { new_password: f.password.value });
      if (error) return msg(m, error.message, false);
      f.reset();
      msg(m, "Password changed.", true);
    });
    $("#signout")?.addEventListener("click", async () => { await sb.auth.signOut(); S.me = null; boot(); });
  }

  // ---------- admin console ----------
  async function loadAdmin() {
    const [{ data: people, error }, { data: prog }, { data: teachers }, { data: attempts }, { data: schools }, { data: schoolTeachers }, { data: ents }] = await Promise.all([
      sb.from("profiles").select("*").order("name"),
      sb.rpc("admin_progress"),
      sb.from("teachers").select("*").order("name"),
      sb.rpc("admin_attempts"),
      sb.from("schools").select("*").order("name"),
      sb.from("school_teachers").select("*").order("name"),
      sb.from("entitlements").select("email,product,tier"),
    ]);
    if (error) throw error;
    const byEmail = new Map();
    (prog || []).forEach((r) => { if (!byEmail.has(r.email)) byEmail.set(r.email, new Map()); byEmail.get(r.email).set(r.slug, r.done_at); });
    return { people: people || [], teachers: teachers || [], byEmail, attempts: attempts || [],
             schools: schools || [], schoolTeachers: schoolTeachers || [], ents: ents || [] };
  }

  // A student's subjects: their own plus their school's while its licence runs.
  const subjectsOf = (state, p) => {
    const sc = p.school_id && state.schools.find((x) => x.id === p.school_id);
    return sc && isLive(sc) ? union(p.subjects, sc.products) : p.subjects;
  };

  const subjectBoxes = (chosen = []) => COURSE_KEYS.map((k) =>
    `<label class="chk"><input type="checkbox" name="subj" value="${k}" ${chosen.includes(k) ? "checked" : ""}> ${esc(catalog.courses[k].title)}</label>`).join("");

  const classBoxes = (chosen = []) => CLASS_LIST.map((c) =>
    `<div class="clsrow"><b>${esc(c.title)}</b>${c.groups.map((g) =>
      `<label class="chk"><input type="checkbox" name="cls" value="${g.id}" ${chosen.includes(g.id) ? "checked" : ""}> ${esc(g.label)}</label>`).join("")}</div>`).join("");

  const progressOf = (state, p) => {
    const all = subjectSlugs(subjectsOf(state, p)), d = state.byEmail.get(p.email) || new Map();
    const n = [...all].filter((s) => d.has(s)).length;
    return { n, total: all.size, pct: pct(n, all.size) };
  };

  function classTable(state, list) {
    return `<div class="tablewrap"><table class="tbl"><thead><tr><th>Student</th><th>Subjects</th><th>Status</th><th>Progress</th><th></th></tr></thead>
      <tbody class="stu">${adminRows(state, list)}</tbody></table></div>`;
  }

  function classAccordion(state) {
    const avgOf = (list) => (list.length ? Math.round(list.reduce((t, p) => t + progressOf(state, p).pct, 0) / list.length) : 0);
    const bar = (id, title, list, inner) => `<details class="card block cls" name="cls" data-cls="${id}" ${openClass === id ? "open" : ""}>
        <summary><h3>${esc(title)}</h3>${list.length ? `<span class="hint">average progress ${avgOf(list)}%</span>` : ""}</summary>${inner}</details>`;
    const out = [];
    const loose = state.people.filter((p) => !(p.classes || []).length && !p.school_id);
    if (loose.length) out.push(bar("none", "Not in a class", loose, classTable(state, loose)));
    CLASS_LIST.forEach((c) => {
      const ids = c.groups.map((g) => g.id);
      const everyone = state.people.filter((p) => (p.classes || []).some((x) => ids.includes(x)));
      const inner = everyone.length ? classTable(state, everyone) : '<p class="hint">No students in this class yet.</p>';
      out.push(bar(c.id, c.title, everyone, inner));
    });
    return out.join("");
  }
  const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;

  function pwGroups(state) {
    const rows = (list) => `<div class="tablewrap"><table class="tbl"><thead><tr><th>Student</th><th>Email</th><th>Password</th></tr></thead><tbody>${list.map((p) => `<tr><td>${esc(p.name)}</td><td>${esc(p.email)}${p.email2 ? `<br>${esc(p.email2)}` : ""}</td><td><code>${esc(p.password)}</code></td></tr>`).join("")}</tbody></table></div>`;
    const group = (title, list) => `<details class="cls pwgrp"><summary><h3>${esc(title)}</h3><span class="hint">${plural(list.length, "student")}</span></summary>${list.length ? rows(list) : '<p class="hint">No students in this class yet.</p>'}</details>`;
    const out = CLASS_LIST.map((c) => {
      const ids = c.groups.map((g) => g.id);
      return group(c.title, state.people.filter((p) => (p.classes || []).some((x) => ids.includes(x))));
    });
    const loose = state.people.filter((p) => !(p.classes || []).length && !p.school_id);
    if (loose.length) out.unshift(group("Not in a class", loose));
    return out.join("");
  }

  function adminRows(state, list) {
    return list.map((p) => {
      const mine = subjectsOf(state, p), all = subjectSlugs(mine), d = state.byEmail.get(p.email) || new Map();
      const n = [...all].filter((s) => d.has(s)).length;
      const status = p.signed_up_at ? (p.last_seen ? "Active " + fmt(p.last_seen) : "Signed up") : "Not signed up";
      return `<tr data-email="${esc(p.email)}"><td><b>${esc(p.name)}</b><br><span class="hint">${esc(p.email)}${p.email2 ? `<br>${esc(p.email2)}` : ""}</span></td>
        <td><div class="pills">${pills(mine)}</div></td><td>${esc(status)}</td><td>${pct(n, all.size)}%<br><span class="hint">${n}/${all.size}</span></td>
        <td class="acts"><button class="mini ok" data-act="view">Progress</button><button class="mini" data-act="edit">Edit</button><button class="mini" data-act="reset">Reset login</button><button class="mini danger" data-act="del">Delete</button></td></tr>`;
    }).join("");
  }

  // One student's lessons, assessment scores and feedback. Re-rendered in place after each change.
  function studentDetail(state, p, onChange) {
    const done = state.byEmail.get(p.email) || new Map();
    const mine = state.attempts.filter((a) => a.email === p.email);
    const live = (slug) => mine.find((a) => a.slug === slug && !a.reset_at);
    const olds = (slug) => mine.filter((a) => a.slug === slug && a.reset_at);
    const review = (a) => `<details class="attempt"><summary><b>${a.pct}%</b> <span class="hint">${a.score}/${a.max} · ${fmt(a.at)}${a.reset_at ? " · reset " + fmt(a.reset_at) : ""}</span></summary>
      ${a.result.items.map((it, i) => `<div class="lessonrow"><b>${i + 1}. ${esc(it.q)}</b> <span class="${it.got >= it.max ? "ok-txt" : "no-txt"}">${it.got}/${it.max}</span><br>
        <span class="hint">Answered:</span> ${it.typed ? esc(it.typed) : "<i>blank</i>"}<br>${it.got >= it.max ? "" : `<span class="hint">Model:</span> ${esc(it.model)}<br>`}<span class="hint">Feedback:</span> ${esc(it.feedback)}</div>`).join("")}</details>`;
    const lesson = (slug) => {
      const a = catalog.artifacts[slug], q = catalog.assessed[slug], t = live(slug), isDone = done.has(slug);
      return `<div class="lessonrow" data-slug="${esc(slug)}"><div class="row"><span><b>${esc(a.title)}</b> <span class="hint">${esc(a.chapterTitle)}</span></span>
        <span>${isDone ? `<span class="ok-txt">✓ Complete</span>` : '<span class="no-txt">Not complete</span>'}
        <button class="mini" data-dn="${isDone ? "0" : "1"}">${isDone ? "Mark not done" : "Mark done"}</button></span></div>
        ${q ? (t ? review(t) + `${t.requested_at && !t.reset_at ? '<span class="pill soft">Retake requested</span> ' : ""}<button class="mini" data-reset="${t.id}">Allow retake</button>` : '<p class="hint">Assessment not attempted.</p>') : '<p class="hint">No assessment on this lesson.</p>'}
        ${olds(slug).length ? `<p class="hint">Earlier attempts</p>${olds(slug).map(review).join("")}` : ""}</div>`;
    };
    const subj = subjectsOf(state, p).filter((k) => catalog.courses[k]).map((k) => {
      const c = catalog.courses[k], n = c.slugs.filter((x) => done.has(x)).length;
      return `<section class="subj"><h4>${esc(c.title)} · ${n}/${c.slugs.length} complete</h4>${chapterMap(c, done)}
        ${c.slugs.map(lesson).join("") || '<p class="hint">No lessons yet.</p>'}</section>`;
    }).join("") || '<p class="hint">No subjects assigned.</p>';
    return `<div class="row"><h3>${esc(p.name)}</h3><button class="btn ghost" value="close" formnovalidate>Close</button></div><p class="hint">${esc(p.email)}</p>${subj}`;
  }

  const schoolOptions = (state, v = "") => `<option value="">None</option>` +
    state.schools.map((sc) => `<option value="${esc(sc.id)}" ${sc.id === v ? "selected" : ""}>${esc(sc.name)}</option>`).join("");
  const dateValue = (d) => (d ? new Date(d).toISOString().slice(0, 10) : "");
  const endOfDay = (v) => (v ? new Date(v + "T23:59:59").toISOString() : null);

  const licenceFields = (sc = {}) => `
    <div class="fields3"><label>Type<select name="kind">${[["school", "School"], ["tutor", "Tutor"]].map(([k, l]) => `<option value="${k}" ${k === (sc.kind || "school") ? "selected" : ""}>${l}</option>`).join("")}</select></label>
      <label>Name<input name="sname" value="${esc(sc.name || "")}" required placeholder="School, or the tutor's name or business"></label></div>
    <p class="hint">Subjects on the licence</p><div class="chks">${subjectBoxes(sc.products || [])}</div>
    <div class="fields3">${tierSelect("tier", sc.tier || "full")}
      <label>Seats<input type="number" name="seats" min="0" value="${sc.seats ?? 30}" required></label>
      <label>End date<input type="date" name="ends" value="${dateValue(sc.expires_at)}"></label></div>
    <label>Note (optional)<input name="snote" value="${esc(sc.note || "")}"></label>`;
  const licenceValues = (f) => ({
    kind: f.elements.kind.value, name: f.elements.sname.value.trim(), products: [...f.querySelectorAll("[name=subj]:checked")].map((c) => c.value),
    tier: f.elements.tier.value, seats: Number(f.elements.seats.value), expires_at: endOfDay(f.elements.ends.value), note: f.elements.snote.value.trim() || null,
  });

  function schoolsPanel(state) {
    const list = state.schools.map((sc) => {
      const studs = state.people.filter((p) => p.school_id === sc.id), tch = state.schoolTeachers.filter((t) => t.school_id === sc.id);
      const warn = !isLive(sc) || studs.length >= sc.seats;
      return `<details class="card block cls ${warn ? "attn" : ""}" name="cls" data-cls="sch-${esc(sc.id)}" ${openClass === "sch-" + sc.id ? "open" : ""}>
        <summary><h3>${esc(sc.name)}</h3>${sc.kind === "tutor" ? '<span class="pill soft">Tutor</span>' : ""}<span class="hint">${esc(licenceLine(sc, studs.length))}</span></summary>
        <div class="row"><div class="pills">${pills(sc.products)}</div>
          <span class="acts"><button class="mini" data-sedit="${esc(sc.id)}">Edit licence</button> <button class="mini danger" data-sdel="${esc(sc.id)}">Delete</button></span></div>
        ${sc.note ? `<p class="hint">${esc(sc.note)}</p>` : ""}
        <div class="subj"><h4>Teachers (${tch.length})</h4></div>
        ${tch.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Name</th><th>Email</th><th>Password</th><th></th></tr></thead><tbody>
          ${tch.map((t) => `<tr data-email="${esc(t.email)}"><td>${esc(t.name)}</td><td>${esc(t.email)}</td><td><code>${esc(t.password)}</code></td><td><button class="mini danger" data-strm="1">Remove</button></td></tr>`).join("")}</tbody></table></div>`
          : '<p class="hint">No teachers yet. Add one so they can manage their own students.</p>'}
        <form class="inline f-steach" data-school="${esc(sc.id)}"><label>Name<input name="tname" required></label><label>Email<input type="email" name="temail" required></label>
          <button class="btn" type="submit">Add teacher</button><p class="msg" hidden></p></form>
        <div class="subj"><h4>Students (${studs.length} of ${sc.seats})</h4></div>
        ${studs.length ? classTable(state, studs) : '<p class="hint">No students yet. Its teachers add them from their profile page.</p>'}
      </details>`;
    }).join("");
    return `<section class="card block"><h3>New school or tutor</h3>
        <p class="hint">A licence, for a school or a private tutor, covers the ticked subjects at one tier for a number of student seats. Its teachers sign in on the Profile page and add their own students, up to the seat limit. Students lose access when the end date passes; their progress is kept.</p>
        <form id="f-school">${licenceFields()}<button class="btn" type="submit">Create licence</button><p class="msg" hidden></p></form></section>
      ${list || '<p class="hint">No schools or tutors yet.</p>'}`;
  }

  async function renderAdmin(host) {
    host.innerHTML = `<p class="hint">Loading students…</p>`;
    let state;
    try { state = await loadAdmin(); }
    catch (e) { host.innerHTML = `<p class="msg err">Could not load students: ${esc(e.message)}. Has schema.sql been run?</p>`; return; }

    const pending = state.people.flatMap((p) => (p.requested || []).filter((k) => catalog.courses[k]).map((k) => ({ p, k })));
    const retakes = state.attempts.filter((a) => a.requested_at && !a.reset_at).map((a) => ({ a, p: state.people.find((x) => x.email === a.email) })).filter((r) => r.p);
    const alerts = pending.length + retakes.length;
    const tab = adminTab || (alerts ? "approvals" : "students");
    const toggleClass = (d) => d.addEventListener("toggle", () => { if (d.open) openClass = d.dataset.cls; else if (openClass === d.dataset.cls) openClass = null; });
    host.innerHTML = `
      <div class="tabs admintabs" role="tablist">
        <button data-at="approvals">Approvals${alerts ? ` (${alerts})` : ""}</button><button data-at="students">Classes</button>
        <button data-at="schools">Schools &amp; tutors</button><button data-at="add">Add students</button><button data-at="pw">Passwords</button><button data-at="me">My profile</button></div>
      <div class="tabpanel" data-panel="approvals"><section class="card block ${retakes.length ? "attn" : ""}"><h3>Retake requests (${retakes.length})</h3>
        ${retakes.length ? `<ul class="plain">${retakes.map(({ a, p }) => `<li class="row" data-id="${a.id}"><span><b>${esc(p.name)}</b> <span class="hint">${esc(catalog.artifacts[a.slug]?.title || a.slug)} · scored ${a.pct}% · asked ${fmt(a.requested_at)}</span></span>
          <span><button class="mini ok" data-rt="yes">Allow retake</button> <button class="mini danger" data-rt="no">Decline</button></span></li>`).join("")}</ul>` : '<p class="hint">Nothing waiting.</p>'}</section>
        <section class="card block ${pending.length ? "attn" : ""}"><div class="row"><h3>Pending approvals (${pending.length})</h3>${pending.length > 1 ? '<button class="mini" id="approveall">Approve all</button>' : ""}</div>
        ${pending.length ? `<ul class="plain">${pending.map(({ p, k }) => `<li class="row" data-email="${esc(p.email)}" data-subj="${k}">
          <span><b>${esc(p.name)}</b> <span class="hint">${esc(p.email)}</span> wants <span class="pill" data-accent="${catalog.courses[k].accent}">${esc(catalog.courses[k].title)}</span></span>
          <span><button class="mini ok" data-ap="yes">Approve</button> <button class="mini danger" data-ap="no">Decline</button></span></li>`).join("")}</ul>` : '<p class="hint">Nothing waiting.</p>'}</section></div>
      <div class="tabpanel" data-panel="add"><section class="card block"><h3>Add students</h3>
        <form id="f-add"><label>One student per line: <b>Name, email</b> or <b>Name, email, second email</b> (a password is generated for each)
          <textarea name="lines" rows="5" required placeholder="An Nguyen, an@school.edu.vn, parent@gmail.com"></textarea></label>
          <div class="chks">${classBoxes()}</div>
          ${state.schools.length ? `<label>School or tutor (optional: puts them on that licence)<select name="school">${schoolOptions(state)}</select></label>` : ""}
          <button class="btn" type="submit">Add students</button><p class="msg" hidden></p></form></section></div>
      <div class="tabpanel" data-panel="pw"><section class="card block"><h3>Student passwords (${state.people.length})</h3>
        <p class="hint">Assigned passwords, visible to admins only. Students sign in with these. If a student changes their own password this list is out of date; Reset login puts it back to the listed one.</p>
        <div class="row"><span></span><button class="mini" id="copypw">Copy as table</button></div>
        ${pwGroups(state)}</section>
      <section class="card block"><h3>Co-teachers</h3>
        <p class="hint">Can open every subject and class content. No admin panel and no student data.</p>
        ${state.teachers.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Name</th><th>Email</th><th>Password</th><th></th></tr></thead><tbody id="tch">
          ${state.teachers.map((t) => `<tr data-email="${esc(t.email)}"><td>${esc(t.name)}</td><td>${esc(t.email)}</td><td><code>${esc(t.password)}</code></td><td><button class="mini danger" data-rm="1">Remove</button></td></tr>`).join("")}</tbody></table></div>` : '<p class="hint">None yet.</p>'}
        <form id="f-teacher" class="inline"><label>Name<input name="tname" required></label><label>Email<input type="email" name="temail" required></label>
          <button class="btn" type="submit">Add co-teacher</button><p class="msg" hidden></p></form></section></div>
      <div class="tabpanel" data-panel="students"><div class="row"><h3>Classes</h3><button class="mini" id="csv">Export CSV</button></div>
        <p class="hint">Open a class to manage its students.</p>${classAccordion(state)}</div>
      <div class="tabpanel" data-panel="schools">${schoolsPanel(state)}</div>
      <div class="tabpanel" data-panel="me">${adminMe}</div>
      <dialog id="dlg"><form method="dialog" id="f-edit"></form></dialog>
      <dialog id="dlg2" class="wide"><form method="dialog" id="f-view"></form></dialog>`;
    const showTab = (t) => {
      adminTab = t;
      host.querySelectorAll("[data-at]").forEach((b) => b.classList.toggle("on", b.dataset.at === t));
      host.querySelectorAll(".tabpanel").forEach((d) => (d.hidden = d.dataset.panel !== t));
    };
    host.querySelectorAll("[data-at]").forEach((b) => b.addEventListener("click", () => showTab(b.dataset.at)));
    showTab(tab);
    wireAccount();

    $("#f-add").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f);
      const classes = [...f.querySelectorAll("[name=cls]:checked")].map((c) => c.value);
      const school_id = f.elements.school?.value || null;
      if (!classes.length && !school_id) return msg(m, "Tick at least one class or pick a school.", false);
      const subjects = classSubjects(classes);
      const taken = new Set(state.people.map((x) => x.password));
      const have = new Map(state.people.map((x) => [x.email, x]));
      const used = new Set(state.people.flatMap((x) => [x.email, x.email2].filter(Boolean)));
      const fresh = [], existing = [], { rows, bad } = parseStudentLines(f.lines.value);
      rows.forEach(({ line, name, email, email2 }) => {
        if (have.has(email)) return existing.push({ email, name, subjects, classes, school_id });
        if ([email, email2].some((x) => x && used.has(x))) return bad.push(line + " (email already in use)");
        [email, email2].filter(Boolean).forEach((x) => used.add(x));
        const password = genPassword(taken); taken.add(password);
        fresh.push({ email, email2, name, subjects, classes, password, school_id });
      });
      if (bad.length) return msg(m, `Check these lines (need a name and one or two valid emails): ${bad.join(" | ")}`, false);
      if (fresh.length) {
        const { error } = await sb.from("profiles").insert(fresh);
        if (error) return msg(m, error.message, false);
        for (const r of fresh) {
          for (const addr of [r.email, r.email2].filter(Boolean)) {
            const { error: e2 } = await sb.rpc("admin_create_login", { target: addr });
            if (e2) return msg(m, `Added ${r.name} but could not create the login for ${addr}: ${e2.message}`, false);
          }
        }
      }
      for (const r of existing) {
        const old = have.get(r.email);
        const { error } = await sb.from("profiles").update({ name: r.name, subjects: union(old.subjects, r.subjects), classes: union(old.classes || [], r.classes), school_id: r.school_id || old.school_id }).eq("email", r.email);
        if (error) return msg(m, error.message, false);
      }
      renderAdmin(host);
    });

    $("#copypw").addEventListener("click", async () => {
      const text = ["Name\tEmail\tEmail 2\tPassword", ...state.people.map((p) => [p.name, p.email, p.email2 || "", p.password].join("\t"))].join("\n");
      await navigator.clipboard.writeText(text);
      $("#copypw").textContent = "Copied";
    });

    const decide = async (p, k, yes) => {
      const subjects = yes && !p.subjects.includes(k) ? [...p.subjects, k] : p.subjects;
      const { error } = await sb.from("profiles").update({ subjects, requested: (p.requested || []).filter((x) => x !== k) }).eq("email", p.email);
      if (error) alert(error.message);
      p.subjects = subjects; p.requested = (p.requested || []).filter((x) => x !== k);
    };
    host.querySelectorAll("[data-ap]").forEach((b) => b.addEventListener("click", async () => {
      const li = b.closest("li");
      await decide(state.people.find((x) => x.email === li.dataset.email), li.dataset.subj, b.dataset.ap === "yes");
      renderAdmin(host);
    }));
    host.querySelectorAll("[data-rt]").forEach((b) => b.addEventListener("click", async () => {
      const id = Number(b.closest("li").dataset.id);
      const { error } = await sb.rpc(b.dataset.rt === "yes" ? "admin_reset_attempt" : "admin_decline_retake", { _id: id });
      if (error) alert(error.message); else { S.refreshBell?.(); renderAdmin(host); }
    }));
    $("#approveall")?.addEventListener("click", async () => { for (const { p, k } of pending) await decide(p, k, true); renderAdmin(host); });

    $("#csv").addEventListener("click", () => {
      const head = ["Name", "Email", "Email 2", "Classes", "Subjects", "Done", "Total", "Percent"];
      const lines = state.people.map((p) => {
        const all = subjectSlugs(subjectsOf(state, p)), d = state.byEmail.get(p.email) || new Map(), n = [...all].filter((s) => d.has(s)).length;
        return [p.name, p.email, p.email2 || "", (p.classes || []).join(" "), p.subjects.join(" "), n, all.size, pct(n, all.size)].map((v) => `"${String(v).replace(/"/g, '""')}"`).join(",");
      });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([[head.join(","), ...lines].join("\n")], { type: "text/csv" }));
      a.download = "progress.csv"; a.click();
    });

    $("#f-teacher").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), email = f.temail.value.trim().toLowerCase();
      if (!EMAIL_RE.test(email)) return msg(m, "Enter a valid email.", false);
      const taken = new Set([...state.people, ...state.teachers].map((x) => x.password));
      const { error } = await sb.rpc("admin_add_teacher", { t_name: f.tname.value.trim(), t_email: email, t_password: genPassword(taken) });
      if (error) return msg(m, error.message, false);
      renderAdmin(host);
    });
    $("#tch")?.addEventListener("click", async (e) => {
      const btn = e.target.closest("[data-rm]");
      if (!btn) return;
      const email = btn.closest("tr").dataset.email;
      if (!confirm(`Remove co-teacher ${email}? Their login is deleted.`)) return;
      const { error } = await sb.rpc("admin_remove_teacher", { t_email: email });
      if (error) alert(error.message); else renderAdmin(host);
    });

    $("#f-school").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), v = licenceValues(f);
      if (!v.products.length) return msg(m, "Tick at least one subject.", false);
      const base = v.name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "school";
      let id = base;
      for (let i = 2; state.schools.some((x) => x.id === id); i++) id = `${base}-${i}`;
      const { error } = await sb.from("schools").insert({ id, ...v });
      if (error) return msg(m, error.message, false);
      openClass = "sch-" + id;
      renderAdmin(host);
    });
    host.querySelectorAll("[data-sedit]").forEach((b) => b.addEventListener("click", () => {
      const sc = state.schools.find((x) => x.id === b.dataset.sedit), dlg = $("#dlg"), f = $("#f-edit");
      f.innerHTML = `<h3>Edit licence</h3>${licenceFields(sc)}
        <p class="hint">Lowering seats below the number of students doesn't remove anyone, but no one can be added until there's room.</p>
        <div class="row"><button class="btn" value="save">Save</button><button class="btn ghost" value="cancel" formnovalidate>Cancel</button></div>`;
      dlg.showModal();
      f.onsubmit = async (ev) => {
        if (ev.submitter?.value !== "save") return;
        const v = licenceValues(f);
        if (!v.products.length) { ev.preventDefault(); return alert("Tick at least one subject."); }
        const { error } = await sb.from("schools").update(v).eq("id", sc.id);
        if (error) return alert(error.message);
        renderAdmin(host);
      };
    }));
    host.querySelectorAll("[data-sdel]").forEach((b) => b.addEventListener("click", async () => {
      const sc = state.schools.find((x) => x.id === b.dataset.sdel);
      if (!confirm(`Delete ${sc.name}? Its teacher logins are deleted. Its students stay on the site with no licence (and lose its subjects).`)) return;
      const { error } = await sb.rpc("admin_delete_school", { _school: sc.id });
      if (error) alert(error.message); else renderAdmin(host);
    }));
    host.querySelectorAll(".f-steach").forEach((f) => f.addEventListener("submit", async (e) => {
      e.preventDefault();
      const m = $(".msg", f), email = f.temail.value.trim().toLowerCase();
      if (!EMAIL_RE.test(email)) return msg(m, "Enter a valid email.", false);
      const taken = new Set([...state.people, ...state.teachers, ...state.schoolTeachers].map((x) => x.password));
      const { error } = await sb.rpc("admin_add_school_teacher", { _school: f.dataset.school, t_name: f.tname.value.trim(), t_email: email, t_password: genPassword(taken) });
      if (error) return msg(m, error.message, false);
      renderAdmin(host);
    }));
    host.querySelectorAll("[data-strm]").forEach((b) => b.addEventListener("click", async () => {
      const email = b.closest("tr").dataset.email;
      if (!confirm(`Remove teacher ${email}? Their login is deleted. Their students are not affected.`)) return;
      const { error } = await sb.rpc("admin_remove_school_teacher", { t_email: email });
      if (error) alert(error.message); else renderAdmin(host);
    }));

    host.querySelectorAll("details.cls").forEach(toggleClass);
    host.querySelectorAll(".stu").forEach((tb) => tb.addEventListener("click", async (e) => {
      const btn = e.target.closest("[data-act]");
      if (!btn) return;
      const email = btn.closest("tr").dataset.email, p = state.people.find((x) => x.email === email);
      if (btn.dataset.act === "view") {
        const dlg2 = $("#dlg2"), fv = $("#f-view");
        const draw = () => {
          const y = dlg2.scrollTop;
          fv.innerHTML = studentDetail(state, p);
          dlg2.scrollTop = y;
        };
        draw();
        if (!dlg2.open) dlg2.showModal();
        const refresh = async () => { Object.assign(state, await loadAdmin()); draw(); };
        fv.onclick = async (ev) => {
          const dn = ev.target.closest("[data-dn]"), rs = ev.target.closest("[data-reset]");
          if (dn) {
            const slug = dn.closest("[data-slug]").dataset.slug;
            const { error } = await sb.rpc("admin_set_done", { _email: p.email, _slug: slug, _done: dn.dataset.dn === "1" });
            if (error) return alert(error.message);
            await refresh();
          } else if (rs) {
            if (!confirm(`Allow ${p.name} to retake this assessment? The current attempt is kept in their history.`)) return;
            const { error } = await sb.rpc("admin_reset_attempt", { _id: Number(rs.dataset.reset) });
            if (error) return alert(error.message);
            await refresh();
          }
        };
        dlg2.addEventListener("close", () => renderAdmin(host), { once: true });
      } else if (btn.dataset.act === "reset") {
        if (!confirm(`Recreate the login(s) for ${p.name} with the password on the list? They keep their progress.`)) return;
        const { error } = await sb.rpc("admin_reset_login", { target: email });
        alert(error ? "Could not reset: " + error.message : "Done. " + p.name + " can sign in with: " + p.password);
        if (!error) renderAdmin(host);
      } else if (btn.dataset.act === "del") {
        if (!confirm(`Delete ${p.name} (${email}) and all their progress? This cannot be undone.`)) return;
        const { error } = await sb.rpc("admin_delete_student", { target: email });
        if (error) alert(error.message); else renderAdmin(host);
      } else {
        const dlg = $("#dlg"), f = $("#f-edit");
        f.innerHTML = `<h3>Edit student</h3><p class="hint">${esc(email)}</p>
          <label>Name<input name="name" value="${esc(p.name)}" required></label>
          <label>Second email (optional)<input type="email" name="email2" value="${esc(p.email2 || "")}"></label>
          <label>Assigned password<input name="password" value="${esc(p.password)}" required minlength="8"></label>
          <p class="hint">Changing the password only affects new logins. Use Reset login to apply it to a student who already has one.</p>
          <p class="hint">Classes</p><div class="chks">${classBoxes(p.classes || [])}</div>
          <p class="hint">Subjects (a class adds its own subject automatically)</p><div class="chks">${subjectBoxes(p.subjects)}</div>
          ${tierSelect("tier", state.ents.find((x) => x.email === email)?.tier || "full", "Tier for these subjects")}
          ${state.schools.length ? `<label>School or tutor<select name="school">${schoolOptions(state, p.school_id || "")}</select></label>
          <p class="hint">A school or tutor licence gives its own subjects at its tier, on top of the ones ticked above.</p>` : ""}
          <p class="hint">To change the main email address, delete the student and add them again. A second email gets its own login with the same password.</p>
          <div class="row"><button class="btn" value="save">Save</button><button class="btn ghost" value="cancel" formnovalidate>Cancel</button></div>`;
        dlg.showModal();
        f.onsubmit = async (ev) => {
          if (ev.submitter?.value !== "save") return;
          const classes = [...f.querySelectorAll("[name=cls]:checked")].map((c) => c.value);
          const subjects = union([...f.querySelectorAll("[name=subj]:checked")].map((c) => c.value), classSubjects(classes));
          const e2 = f.elements.email2.value.trim().toLowerCase();
          if (e2 && !EMAIL_RE.test(e2)) return alert("Second email is not valid.");
          const school_id = f.elements.school ? f.elements.school.value || null : p.school_id;
          const { error } = await sb.from("profiles").update({ name: f.elements.name.value.trim(), subjects, classes, school_id, password: f.elements.password.value.trim() }).eq("email", email);
          if (error) return alert(error.message);
          // Subject changes write entitlement rows (trigger), so set the tier after the profile update.
          const { error: et } = await sb.from("entitlements").update({ tier: f.elements.tier.value }).eq("email", email).neq("plan", "school");
          if (et) alert("Saved, but the tier failed: " + et.message);
          if (e2 !== (p.email2 || "")) {
            const { error: e3 } = await sb.rpc("admin_set_email2", { target: email, new_email2: e2 });
            if (e3) alert("Saved, but the second email failed: " + e3.message);
          }
          renderAdmin(host);
        };
      }
    }));
  }

  // ---------- school or tutor teacher ----------
  // Manages their own licence's students within the licence's seats and sees only their progress.
  async function viewSchool(me) {
    const sc = me.school, subjects = sc.products.filter((k) => catalog.courses[k]);
    root.innerHTML = `<p class="hint">Loading your students…</p>`;
    const { data, error } = await sb.rpc("school_dashboard");
    if (error) { root.innerHTML = `<p class="msg err">Could not load your students: ${esc(error.message)}</p>`; return; }
    const students = data.students, byEmail = new Map();
    data.progress.forEach((r) => { if (!byEmail.has(r.email)) byEmail.set(r.email, new Map()); byEmail.get(r.email).set(r.slug, r.done_at); });
    const all = subjectSlugs(subjects), left = Math.max(0, sc.seats - students.length);
    const doneOf = (p) => byEmail.get(p.email) || new Map();
    const rows = students.map((p) => {
      const d = doneOf(p), n = [...all].filter((x) => d.has(x)).length;
      const status = p.signed_up_at ? (p.last_seen ? "Active " + fmt(p.last_seen) : "Signed up") : "Not signed up";
      return `<tr data-email="${esc(p.email)}"><td><b>${esc(p.name)}</b><br><span class="hint">${esc(p.email)}${p.email2 ? `<br>${esc(p.email2)}` : ""}</span></td>
        <td><code>${esc(p.password)}</code></td><td>${esc(status)}</td><td>${pct(n, all.size)}%<br><span class="hint">${n}/${all.size}</span></td>
        <td class="acts"><button class="mini ok" data-act="view">Progress</button><button class="mini" data-act="reset">Reset login</button><button class="mini danger" data-act="rm">Remove</button></td></tr>`;
    }).join("");
    root.innerHTML = `
      <section class="idcard"><h1>${esc(me.name)}</h1><p class="email">${esc(me.email)} · ${esc(sc.name)}</p>
        <div class="pills">${pills(subjects)}</div><p class="hint">${esc(licenceLine(sc, students.length))}</p></section>
      ${sc.active ? "" : `<section class="card block attn"><h3>This licence has ended</h3><p>Your students can't open lessons until it is renewed. Their progress is kept.</p></section>`}
      <section class="card block"><h3>Add students</h3><p class="hint">${plural(left, "seat")} free of ${sc.seats}. A password is generated for each student; give it to them with their email.</p>
        <form id="f-sadd"><label>One student per line: <b>Name, email</b> or <b>Name, email, second email</b>
          <textarea name="lines" rows="5" required placeholder="An Nguyen, an@gmail.com"></textarea></label>
          <button class="btn" type="submit" ${left && sc.active ? "" : "disabled"}>Add students</button><p class="msg" hidden></p></form></section>
      <section class="card block"><div class="row"><h3>Students (${students.length})</h3>${students.length ? '<button class="mini" id="copypw">Copy logins as table</button>' : ""}</div>
        ${students.length ? `<div class="tablewrap"><table class="tbl"><thead><tr><th>Student</th><th>Password</th><th>Status</th><th>Progress</th><th></th></tr></thead><tbody id="sstu">${rows}</tbody></table></div>`
          : '<p class="hint">No students yet.</p>'}
        <p class="hint">If a student changes their own password, the one listed here is out of date. Reset login puts it back to the listed one.</p></section>
      ${accountCard()}
      <dialog id="dlg2" class="wide"><form method="dialog" id="f-view"></form></dialog>`;
    wireAccount();

    $("#f-sadd").addEventListener("submit", async (e) => {
      e.preventDefault();
      const f = e.target, m = $(".msg", f), { rows: list, bad } = parseStudentLines(f.lines.value);
      if (bad.length) return msg(m, `Check these lines (need a name and one or two valid emails): ${bad.join(" | ")}`, false);
      if (list.length > left) return msg(m, `That's ${list.length} students but only ${plural(left, "seat")} left.`, false);
      const taken = new Set(students.map((x) => x.password));
      for (const [i, r] of list.entries()) {
        const password = genPassword(taken); taken.add(password);
        const { error } = await sb.rpc("school_add_student", { _name: r.name, _email: r.email, _email2: r.email2, _password: password });
        if (error) { msg(m, `${i ? `Added ${plural(i, "student")}. ` : ""}Stopped at "${r.line}": ${error.message}`, false); return setTimeout(() => viewSchool(me), 2500); }
      }
      viewSchool(me);
    });
    $("#copypw")?.addEventListener("click", async () => {
      await navigator.clipboard.writeText(["Name\tEmail\tEmail 2\tPassword", ...students.map((p) => [p.name, p.email, p.email2 || "", p.password].join("\t"))].join("\n"));
      $("#copypw").textContent = "Copied";
    });
    $("#sstu")?.addEventListener("click", async (e) => {
      const btn = e.target.closest("[data-act]");
      if (!btn) return;
      const p = students.find((x) => x.email === btn.closest("tr").dataset.email);
      if (btn.dataset.act === "view") {
        const d = doneOf(p), score = (slug) => data.attempts.find((a) => a.email === p.email && a.slug === slug);
        $("#f-view").innerHTML = `<div class="row"><h3>${esc(p.name)}</h3><button class="btn ghost" value="close" formnovalidate>Close</button></div><p class="hint">${esc(p.email)}</p>
          ${subjects.map((k) => {
            const c = catalog.courses[k], n = c.slugs.filter((x) => d.has(x)).length;
            return `<section class="subj"><h4>${esc(c.title)} · ${n}/${c.slugs.length} complete</h4>${chapterMap(c, d)}
              ${c.slugs.map((slug) => {
                const a = catalog.artifacts[slug], t = score(slug);
                return `<div class="lessonrow"><div class="row"><span><b>${esc(a.title)}</b> <span class="hint">${esc(a.chapterTitle)}</span></span>
                  <span>${t ? `<b>${t.pct}%</b> <span class="hint">${fmt(t.at)}</span> ` : ""}${d.has(slug) ? '<span class="ok-txt">✓ Complete</span>' : '<span class="no-txt">Not complete</span>'}</span></div></div>`;
              }).join("")}</section>`;
          }).join("") || '<p class="hint">No subjects on this licence.</p>'}`;
        $("#dlg2").showModal();
      } else if (btn.dataset.act === "reset") {
        if (!confirm(`Recreate the login for ${p.name} with the listed password? Their progress is kept.`)) return;
        const { error } = await sb.rpc("school_reset_login", { _email: p.email });
        alert(error ? "Could not reset: " + error.message : `Done. ${p.name} can sign in with: ${p.password}`);
      } else if (confirm(`Remove ${p.name} from ${sc.name}? This frees their seat. They lose access to these lessons; their progress is kept if they're added back.`)) {
        const { error } = await sb.rpc("school_remove_student", { _email: p.email });
        if (error) alert(error.message); else viewSchool(me);
      }
    });
  }

  // ---------- boot ----------
  async function boot() {
    if (recovering) return viewRecovery();
    const me = await S.whoami(true);
    if (!me && !(await S.session())) return viewSignedOut();  // sign-in needs nothing else, so show it straight away
    try { catalog = catalog || (await S.catalog()); } catch (e) {
      root.innerHTML = `<div class="placeholder"><h2>Could not load</h2><p>Check your connection and refresh the page.</p></div>`;
      return;
    }
    if (me) {
      const next = sessionStorage.getItem("site.next");
      if (next) { sessionStorage.removeItem("site.next"); if (next.startsWith(S.base)) { location.href = next; return; } }
    }
    if (!me) {
      if (await S.session()) {
        root.innerHTML = `<div class="placeholder"><h2>Not on the class list</h2><p>You are signed in, but this email has not been added by your teacher.</p>
          <p><button class="btn ghost" id="signout">Sign out</button></p></div>`;
        return wireAccount();
      }
      return viewSignedOut();
    }
    if (me.is_school_teacher) return viewSchool(me);
    const done = await S.loadProgress();
    let attempts = [];
    if (!me.is_admin && !me.is_teacher) attempts = (await S.sb.rpc("my_attempts")).data || [];
    const [head, body] = viewDashboard(me, done, attempts).split("<!--split-->");
    if (me.is_admin) {
      adminMe = body;
      root.innerHTML = head + `<div id="admin"></div>`;
      renderAdmin($("#admin"));
    } else {
      root.innerHTML = head + body;
      wireAccount();
    }
  }

  boot();
})();
