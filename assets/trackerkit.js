// Shared by the student tracker and the teacher dashboard: the scores-over-time chart and per-topic summary rows.
(function () {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const fmt = (d) => new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
  const short = (d) => new Date(d).toLocaleDateString("en-GB", { day: "numeric", month: "short" });

  // list: attempts oldest first ({at, pct, score, max, title, course}). One dot per attempt, one line per subject.
  function chart(list, catalog, label = "Topic test scores over time") {
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
    return `<svg class="trchart" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(label)}">${grid}${ticks}
      <line class="avg" x1="${L}" x2="${W - R}" y1="${y(avg)}" y2="${y(avg)}"/><text class="gt" x="${W - R}" y="${y(avg) - 5}" text-anchor="end">average ${avg}%</text>${series}</svg>`;
  }

  // Collapse many students' attempts into one point per week per subject (the week's average), so a class reads as a trend.
  function weekly(list) {
    const buckets = new Map();
    list.forEach((r) => {
      const d = new Date(r.at), day = (d.getDay() + 6) % 7;
      const mon = new Date(d.getFullYear(), d.getMonth(), d.getDate() - day).getTime();
      const k = r.course + "|" + mon;
      if (!buckets.has(k)) buckets.set(k, { course: r.course, at: mon, ps: [], n: 0 });
      const b = buckets.get(k); b.ps.push(r.pct); b.n++;
    });
    return [...buckets.values()].sort((a, b) => a.at - b.at).map((b) => {
      const pct = Math.round(b.ps.reduce((t, v) => t + v, 0) / b.ps.length);
      return { course: b.course, at: new Date(b.at).toISOString(), pct, score: pct, max: 100, title: `Week of ${short(b.at)} (${b.n} attempt${b.n === 1 ? "" : "s"}, class average)` };
    });
  }

  // One row per topic: attempts, first, best, latest and change. link(test) builds the topic link; extra is an optional last cell.
  function byTopic(list, link, extra) {
    const m = new Map();
    list.forEach((r) => { if (!m.has(r.test)) m.set(r.test, []); m.get(r.test).push(r); });
    return [...m.entries()].map(([test, rs]) => {
      const first = rs[0].pct, last = rs[rs.length - 1].pct, best = Math.max(...rs.map((r) => r.pct)), d = last - first;
      return `<tr><td><a class="lnk" href="${link(test)}">${esc(rs[0].title)}</a></td><td>${rs.length}</td><td>${first}%</td><td>${best}%</td><td><b>${last}%</b></td>
        <td class="${d > 0 ? "ok-txt" : "no-txt"}">${rs.length > 1 ? (d > 0 ? "+" : "") + d : "–"}</td>${extra ? `<td>${extra(test)}</td>` : ""}</tr>`;
    }).join("");
  }

  // Chapter squares for one course: filled = every activity done, half = started, grey = nothing yet.
  function chapterMap(course, done, base) {
    return course.groups.map((g) => `<div class="mapgroup"><h4>${esc(g.title)}</h4><div class="tiles">
      ${g.chapters.map((ch) => {
        const total = ch.slugs.length, n = ch.slugs.filter((s) => done.has(s)).length;
        const st = !total ? "empty" : n === total ? "full" : n ? "part" : "none";
        return `<a class="tile ${st}" href="${base}${ch.url}" title="${esc(ch.title)}${total ? ` (${n}/${total} done)` : " (nothing yet)"}">${esc(ch.label)}</a>`;
      }).join("")}</div></div>`).join("");
  }

  window.TrackerKit = { esc, fmt, short, chart, weekly, byTopic, chapterMap };
})();
