// Student dashboard: the first page after signing in. Reads the same data the profile page loads
// (whoami, loadProgress, my_attempts, catalog) and lays it out visually. Teachers/admins are sent to
// Profile, where their consoles live; signed-out visitors are sent to sign in.
(function () {
  const S = window.Site;
  const root = document.getElementById("dashboard-root");
  if (!root) return;
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => (d ? new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : "");
  const pct = (done, total) => (total ? Math.round((100 * done) / total) : 0);
  let catalog;

  if (!S || !S.configured) {
    root.innerHTML = `<div class="placeholder"><h2>Accounts are not switched on yet</h2></div>`;
    return;
  }

  const ring = (p) => {
    const c = 2 * Math.PI * 34, off = c * (1 - p / 100);
    return `<svg class="ring" viewBox="0 0 80 80" width="76" height="76" aria-hidden="true">
      <circle cx="40" cy="40" r="34" class="ring-bg"/>
      <circle cx="40" cy="40" r="34" class="ring-fg" stroke-dasharray="${c.toFixed(1)}" stroke-dashoffset="${off.toFixed(1)}"/>
      <text x="40" y="45" class="ring-num">${p}%</text></svg>`;
  };

  const subjectSlugs = (subjects) => {
    const out = new Set();
    subjects.forEach((k) => catalog.courses[k]?.slugs.forEach((s) => out.add(s)));
    return out;
  };

  function chapterMap(course, done) {
    return course.groups.map((g) => `<div class="mapgroup"><h4>${esc(g.title)}</h4><div class="tiles">
      ${g.chapters.map((ch) => {
        const total = ch.slugs.length, n = ch.slugs.filter((s) => done.has(s)).length;
        const st = !total ? "empty" : n === total ? "full" : n ? "part" : "none";
        return `<a class="tile ${st}" href="${S.base}${ch.url}" title="${esc(ch.title)}${total ? ` (${n}/${total} done)` : " (nothing yet)"}">${esc(ch.label)}</a>`;
      }).join("")}</div></div>`).join("");
  }

  function render(me, done, attempts) {
    const mine = me.subjects.filter((k) => catalog.courses[k]);
    const all = subjectSlugs(mine), total = all.size;
    const doneN = [...all].filter((s) => done.has(s)).length;
    const overall = pct(doneN, total);
    const weekAgo = Date.now() - 7 * 864e5;
    const week = [...done.values()].filter((d) => d && new Date(d).getTime() >= weekAgo).length;
    const scored = attempts.filter((t) => catalog.artifacts[t.slug]);
    const avg = scored.length ? Math.round(scored.reduce((s, t) => s + t.pct, 0) / scored.length) : null;
    const recent = [...done.entries()].filter(([s]) => catalog.artifacts[s]).sort((a, b) => (b[1] || "").localeCompare(a[1] || "")).slice(0, 4);
    const first = (me.name || "").trim().split(/\s+/)[0] || me.name;
    const h = new Date().getHours();
    const greet = h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : "Good evening";

    const IC = {
      star: `<svg class="stat-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z" stroke-linejoin="round"/></svg>`,
      check: `<svg class="stat-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12l2.5 2.5L16 9" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
      cal: `<svg class="stat-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4" stroke-linecap="round"/></svg>`,
    };

    const tiles = [
      `<div class="stat ring-tile">${ring(overall)}<div><b>Overall progress</b><span class="hint">${doneN} of ${total} activities</span></div></div>`,
      `<div class="stat" data-accent="green">${IC.star}<span class="statbig">${avg === null ? "–" : avg + "%"}</span><b>Average score</b><span class="hint">${scored.length ? "across " + scored.length + " assessment" + (scored.length === 1 ? "" : "s") : "no assessments yet"}</span></div>`,
      `<div class="stat" data-accent="indigo">${IC.check}<span class="statbig">${doneN}</span><b>Lessons complete</b><span class="hint">${Math.max(0, total - doneN)} still to finish</span></div>`,
      `<div class="stat" data-accent="amber">${IC.cal}<span class="statbig">${week}</span><b>Lessons this week</b><span class="hint">completed in the last 7 days</span></div>`,
    ].join("");

    const resumeCard = (k) => {
      const c = catalog.courses[k], set = new Set(c.slugs);
      const nx = catalog.order.find((s) => set.has(s) && !done.has(s));
      const a = nx && catalog.artifacts[nx];
      return a
        ? `<section class="card block dash-resume" data-accent="${c.accent}"><div><p class="kicker">Pick up where you left off</p>
            <h3>${esc(a.title)}</h3><p class="hint">${esc(a.chapterTitle)}</p></div>
            <a class="btn" href="${S.base}${a.url}">Continue →</a></section>`
        : `<section class="card block dash-resume" data-accent="${c.accent}"><div><p class="kicker">Nice work</p>
            <h3>All caught up in ${esc(c.title)}</h3><p class="hint">You’ve finished every lesson available in this subject.</p></div>
            <a class="btn" href="${S.base}${c.url}">Review →</a></section>`;
    };
    const resume = mine.length
      ? `<div class="dash-resume-stack">${mine.map(resumeCard).join("")}</div>`
      : `<section class="card block dash-resume" data-accent="teal"><div><p class="kicker">Welcome</p>
          <h3>No subjects yet</h3><p class="hint">Ask for your subjects on the Profile page.</p></div>
          <a class="btn" href="${S.profileUrl}">Go to Profile</a></section>`;

    const subjectCards = mine.map((k) => {
      const c = catalog.courses[k], t = c.slugs.length, n = c.slugs.filter((s) => done.has(s)).length;
      return `<section class="card block" data-accent="${c.accent}"><div class="row"><h3><a href="${S.base}${c.url}">${esc(c.title)}</a></h3><span class="big">${pct(n, t)}%</span></div>
        <div class="bar2"><i style="width:${pct(n, t)}%"></i></div><p class="hint">${n} of ${t} activities done.</p>${chapterMap(c, done)}</section>`;
    }).join("");

    const scoresCard = `<section class="card block"><div class="row"><h3>Assessment scores</h3>${avg === null ? "" : `<span class="big">${avg}%</span>`}</div>
      ${scored.length ? `<p class="hint">Average across your attempts. Score the pass mark or more to complete a lesson.</p>
        <div class="tablewrap"><table class="tbl"><thead><tr><th>Lesson</th><th>Score</th><th>When</th></tr></thead><tbody>
        ${scored.map((t) => `<tr><td><a class="lnk" href="${S.base}assess/?a=${encodeURIComponent(t.slug)}">${esc(catalog.artifacts[t.slug].title)}</a></td>
          <td><b class="${t.pct >= (catalog.assessed[t.slug]?.pass ?? 80) ? "ok-txt" : "no-txt"}">${t.pct}%</b></td><td class="hint">${fmt(t.at)}</td></tr>`).join("")}</tbody></table></div>`
        : `<p class="hint">Lessons with an assessment show your score and feedback here once you’ve taken one.</p>`}</section>`;

    const recentCard = `<section class="card block"><h3>Recently completed</h3>
      ${recent.length ? `<ul class="plain">${recent.map(([s, d]) => `<li><a class="lnk" href="${S.base}${catalog.artifacts[s].url}">${esc(catalog.artifacts[s].title)}</a> <span class="hint">${fmt(d)}</span></li>`).join("")}</ul>`
        : `<p class="hint">Finish a lesson and it shows up here.</p>`}
      <p class="hint" style="margin-top:14px"><a class="lnk" href="${S.profileUrl}">Manage your account, plan and password on your Profile →</a></p></section>`;

    root.innerHTML = `
      <section class="dash-head"><p class="kicker">Dashboard</p><h1>${greet}, ${esc(first)}</h1>
        <p class="hint">${me.school ? esc(me.school) + " · " : ""}${mine.length ? mine.map((k) => esc(catalog.courses[k].title)).join(" · ") : "No subjects yet"}</p></section>
      ${resume}
      <div class="stat-tiles">${tiles}</div>
      ${mine.length ? `<h2 class="dash-h2">Your subjects</h2><div class="grid two">${subjectCards}</div>` : ""}
      <div class="grid two dash">${scoresCard}${recentCard}</div>`;
  }

  async function boot() {
    const me = await S.whoami(true);
    if (!me) {
      if (await S.session()) {
        root.innerHTML = `<div class="placeholder"><h2>Not on the class list</h2><p>You are signed in, but this email has not been added by a teacher yet.</p></div>`;
        return;
      }
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      root.innerHTML = `<section class="card block"><h3>Sign in to see your dashboard</h3>
        <p>Use the email and password your teacher gave you.</p><p><a class="btn" href="${S.profileUrl}">Sign in</a></p></section>`;
      return;
    }
    // Teachers, co-teachers and admins manage their classes and account on the Profile page.
    if (me.is_admin || me.is_teacher || me.is_school_teacher) { location.href = S.profileUrl; return; }
    try { catalog = await S.catalog(); }
    catch (e) { root.innerHTML = `<div class="placeholder"><h2>Could not load</h2><p>Check your connection and refresh.</p></div>`; return; }
    const done = await S.loadProgress();
    const attempts = (await S.sb.rpc("my_attempts")).data || [];
    render(me, done, attempts);
  }
  boot();
})();
