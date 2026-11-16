// Test tracker: every finished topic test attempt, charted over time, with a per-topic summary.
(function () {
  const S = window.Site;
  const root = document.getElementById("tr-root");
  if (!root) return;
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
  const short = (d) => new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short" });
  let rows = [], catalog, filter = "all";

  function chart(list) {
    if (!list.length) return "";
    const W = 720, H = 300, L = 40, R = 16, T = 14, B = 34;
    const ts = list.map((r) => new Date(r.at).getTime());
    let t0 = Math.min(...ts), t1 = Math.max(...ts);
    if (t1 - t0 < 864e5) { t0 -= 432e5; t1 += 432e5; }
    const x = (t) => L + ((t - t0) / (t1 - t0)) * (W - L - R);
    const y = (p) => T + (1 - p / 100) * (H - T - B);
    const grid = [0, 25, 50, 75, 100].map((p) => `<line class="gl" x1="${L}" x2="${W - R}" y1="${y(p)}" y2="${y(p)}"/><text class="gt" x="${L - 6}" y="${y(p) + 4}" text-anchor="end">${p}%</text>`).join("");
    const ticks = [0, 1, 2, 3, 4].map((i) => { const t = t0 + ((t1 - t0) * i) / 4; return `<text class="gt" x="${x(t)}" y="${H - 10}" text-anchor="middle">${short(t)}</text>`; }).join("");
    const byCourse = {};
    list.forEach((r) => (byCourse[r.course] ||= []).push(r));
    const series = Object.entries(byCourse).map(([k, rs]) => {
      const acc = catalog.courses[k]?.accent || "green";
      const path = rs.map((r, i) => `${i ? "L" : "M"}${x(new Date(r.at).getTime()).toFixed(1)},${y(r.pct).toFixed(1)}`).join("");
      const dots = rs.map((r) => `<circle cx="${x(new Date(r.at).getTime()).toFixed(1)}" cy="${y(r.pct).toFixed(1)}" r="5"><title>${esc(r.title)}: ${r.pct}% (${r.score}/${r.max}) on ${fmt(r.at)}</title></circle>`).join("");
      return `<g data-accent="${acc}" class="series"><path d="${path}"/>${dots}</g>`;
    }).join("");
    const avg = Math.round(list.reduce((t, r) => t + r.pct, 0) / list.length);
    return `<svg class="trchart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Topic test scores over time">${grid}${ticks}
      <line class="avg" x1="${L}" x2="${W - R}" y1="${y(avg)}" y2="${y(avg)}"/><text class="gt" x="${W - R}" y="${y(avg) - 5}" text-anchor="end">average ${avg}%</text>${series}</svg>`;
  }

  function byTopic(list) {
    const m = new Map();
    list.forEach((r) => { if (!m.has(r.test)) m.set(r.test, []); m.get(r.test).push(r); });
    return [...m.entries()].map(([test, rs]) => {
      const first = rs[0].pct, last = rs[rs.length - 1].pct, best = Math.max(...rs.map((r) => r.pct)), d = last - first;
      return `<tr><td><a class="lnk" href="${S.base}${test}/">${esc(rs[0].title)}</a></td><td>${rs.length}</td><td>${first}%</td><td>${best}%</td><td><b>${last}%</b></td>
        <td class="${d > 0 ? "ok-txt" : "no-txt"}">${rs.length > 1 ? (d > 0 ? "+" : "") + d : "–"}</td>
        <td><a class="lnk" href="${S.base}tests/?t=${encodeURIComponent(test)}">Retake</a></td></tr>`;
    }).join("");
  }

  function render() {
    const list = filter === "all" ? rows : rows.filter((r) => r.course === filter);
    const courses = [...new Set(rows.map((r) => r.course))];
    const avg = list.length ? Math.round(list.reduce((t, r) => t + r.pct, 0) / list.length) : null;
    const latest = list[list.length - 1], best = list.length ? Math.max(...list.map((r) => r.pct)) : null;
    const topics = new Set(list.map((r) => r.test)).size;
    root.innerHTML = rows.length ? `
      ${courses.length > 1 ? `<div class="tabs" role="tablist"><button class="${filter === "all" ? "on" : ""}" data-f="all">All subjects</button>${courses.map((c) => `<button class="${filter === c ? "on" : ""}" data-f="${c}">${esc(catalog.courses[c]?.title || c)}</button>`).join("")}</div>` : ""}
      <div class="stat-tiles">
        <div class="stat" data-accent="indigo"><span class="statbig">${list.length}</span><b>Attempts</b><span class="hint">${topics} topic${topics === 1 ? "" : "s"} tested</span></div>
        <div class="stat" data-accent="green"><span class="statbig">${avg}%</span><b>Average score</b><span class="hint">across these attempts</span></div>
        <div class="stat" data-accent="amber"><span class="statbig">${latest.pct}%</span><b>Latest score</b><span class="hint">${esc(latest.title)}</span></div>
        <div class="stat" data-accent="plum"><span class="statbig">${best}%</span><b>Best score</b><span class="hint">your high point</span></div></div>
      <section class="card block"><h3>Scores over time</h3><p class="hint">Each dot is one attempt. The dashed line is your average. Hover a dot for the details.</p>${chart(list)}</section>
      <section class="card block"><h3>By topic</h3><p class="hint">First attempt against your best and latest, so you can see how much a topic has improved.</p>
        <div class="tablewrap"><table class="tbl"><thead><tr><th>Topic</th><th>Attempts</th><th>First</th><th>Best</th><th>Latest</th><th>Change</th><th></th></tr></thead><tbody>${byTopic(list)}</tbody></table></div></section>
      <section class="card block"><h3>All attempts</h3><div class="tablewrap"><table class="tbl"><thead><tr><th>Topic</th><th>Score</th><th>Multiple choice</th><th>Written</th><th>When</th></tr></thead><tbody>
        ${[...list].reverse().map((r) => `<tr><td>${esc(r.title)}</td><td><b>${r.pct}%</b> <span class="hint">${r.score}/${r.max}</span></td><td>${r.mcq}/${r.mcq_max}</td><td>${r.written}/${r.written_max}</td><td class="hint">${fmt(r.at)}</td></tr>`).join("")}</tbody></table></div></section>`
      : `<section class="card block"><h3>No topic tests yet</h3><p class="hint">Finish a chapter, then take its topic test from the chapter page. Each attempt shows up here, so you can watch your scores rise.</p>
        <p><a class="btn" href="${S.base}dashboard/">Go to my dashboard</a></p></section>`;
    root.querySelectorAll("[data-f]").forEach((b) => (b.onclick = () => { filter = b.dataset.f; render(); }));
  }

  async function boot() {
    const me = await S.whoami();
    if (!me) {
      try { sessionStorage.setItem("site.next", location.href); } catch (e) {}
      root.innerHTML = `<section class="card block"><h3>Sign in to see your tracker</h3><p><a class="btn" href="${S.profileUrl}">Sign in</a></p></section>`;
      return;
    }
    if (me.is_admin || me.is_teacher || me.is_school_teacher) { root.innerHTML = `<section class="card block"><h3>Students only</h3><p class="hint">The tracker shows a student's own topic test scores. Class views for teachers are coming.</p></section>`; return; }
    try { catalog = await S.catalog(); } catch (e) { root.innerHTML = `<p class="msg err">Could not load. Check your connection and refresh.</p>`; return; }
    const { data, error } = await S.sb.rpc("my_test_attempts");
    if (error) { root.innerHTML = `<p class="msg err">${esc(error.message)}</p>`; return; }
    rows = data || [];
    render();
  }
  if (S && S.configured) boot();
})();
