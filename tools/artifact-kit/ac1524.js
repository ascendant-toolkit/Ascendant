const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

/* circuit drawer: geom comes from ak15.circuit(); vals colours the wires */
function circEval(G, inp, st) {
  const v = Object.assign({}, inp); G.net.forEach(([n]) => v[n] = (st && st[n]) || 0);
  for (let k = 0; k < 8; k++) G.net.forEach(([n, t, s]) => {
    const a = s.map((x) => v[x]); let base = t, neg = false;
    if (t !== "NOT" && t[0] === "N") { base = t.slice(1); neg = true; }
    let r = base === "AND" ? a.every((x) => x) : base === "OR" ? a.some((x) => x) : base === "XOR" ? a.reduce((p, x) => p + x, 0) % 2 === 1 : !a[0];
    r = (neg ? !r : r) ? 1 : 0; v[n] = r;
  });
  return v;
}
function circInner(G, vals, opt) {
  opt = opt || {};
  const cl = (s) => (vals ? (vals[s] ? "w on" : "w off") : "w"); let o = "";
  G.wires.forEach((w) => { o += `<path class="${cl(w.s)}" d="${w.d}"/>`; if (w.dot) o += `<circle class="dot" cx="${w.dot[0]}" cy="${w.dot[1]}" r="3.2"/>`; });
  G.outs.forEach((w) => o += `<path class="${cl(w.s)}" d="${w.d}"/>`);
  G.gates.forEach((g) => { o += g.svg; if (!G.outset.includes(g.n)) o += `<text class="sm" x="${g.ox + 4}" y="${g.cy - 7}">${g.n}${vals && opt.vals ? " = " + vals[g.n] : ""}</text>`; });
  G.inputs.forEach((i) => o += `<text class="lbl bd" x="2" y="${i.y + 4}">${i.n}${vals ? " " + vals[i.n] : ""}</text>`);
  G.outs.forEach((w) => o += `<text class="lbl bd" x="${w.x + 6}" y="${w.y + 4}">${w.s}${vals ? " = " + vals[w.s] : ""}</text>`);
  return o;
}
function circFit(G, vals, W, opt) {
  const k = Math.min(2.2, (W - 20) / G.w), dx = (W - G.w * k) / 2;
  return `<g transform="translate(${dx.toFixed(1)},6) scale(${k.toFixed(3)})">` + circInner(G, vals, opt) + "</g>";
}
function circSvg(G, vals, opt) {
  return `<svg viewBox="0 0 ${G.w} ${G.h}" style="width:${Math.round(G.w * 1.2)}px;max-width:100%;display:block">` + circInner(G, vals, opt) + "</svg>";
}
/* toggle lab: one button per input, live circuit and a table of every row with the current one highlighted */
function circLab(el, G, work, outs) {
  const ins = G.in; let cur = ins.map(() => 0);
  const root = typeof el === "string" ? $(el) : el;
  root.innerHTML = '<div class="btnrow" data-b></div><div data-s></div><div data-t></div>';
  const bw = root.querySelector("[data-b]"), sw = root.querySelector("[data-s]"), tw = root.querySelector("[data-t]");
  function paint() {
    const inp = {}; ins.forEach((n, i) => inp[n] = cur[i]);
    const v = circEval(G, inp);
    sw.innerHTML = circSvg(G, v, { vals: true });
    bw.querySelectorAll("button").forEach((b, i) => { b.textContent = ins[i] + " = " + cur[i]; b.className = cur[i] ? "on" : ""; });
    const cols = ins.concat(work, outs); let h = '<div class="tw"><table class="t mono"><tr>' + cols.map((c) => `<th>${c}</th>`).join("") + "</tr>";
    for (let m = 0; m < 1 << ins.length; m++) {
      const b = ins.map((_, i) => (m >> (ins.length - 1 - i)) & 1), iv = {}; ins.forEach((n, i) => iv[n] = b[i]);
      const r = circEval(G, iv), on = b.every((x, i) => x === cur[i]);
      h += `<tr style="${on ? "background:var(--accent-soft);font-weight:700" : ""}">` + b.map((x) => `<td>${x}</td>`).join("") + work.concat(outs).map((n) => `<td>${r[n]}</td>`).join("") + "</tr>";
    }
    tw.innerHTML = h + "</table></div>";
  }
  ins.forEach((n, i) => { const b = document.createElement("button"); b.onclick = () => { cur[i] ^= 1; paint(); }; bw.appendChild(b); });
  paint();
}

/* ---- Boolean helpers (same notation and logic as the Python side) ---- */
function obJS(s) {
  const neg = (i) => { if (s[i] === "~") { const [h, j] = neg(i + 1); return ['<span class="ob">' + h + "</span>", j]; } if (s[i] === "(") { const [h, j] = seq(i + 1); return ['<span class="ob">' + h + "</span>", j + 1]; } return ['<span class="ob">' + s[i] + "</span>", i + 1]; };
  const seq = (i) => { let o = ""; while (i < s.length && s[i] !== ")") { if (s[i] === "~") { const [h, j] = neg(i + 1); o += h; i = j; } else if (s[i] === "(") { const [h, j] = seq(i + 1); o += "(" + h + ")"; i = j + 1; } else { o += s[i]; i++; } } return [o, i]; };
  return seq(0)[0];
}
const bitsOf = (m, nv) => Array.from({ length: nv }, (_, i) => (m >> (nv - 1 - i)) & 1);
function coverOf(pat, nv) { const r = []; for (let m = 0; m < 1 << nv; m++) { const b = bitsOf(m, nv); if ([...pat].every((p, i) => p === "-" || +p === b[i])) r.push(m); } return r; }
function termOf(pat, names) { const t = [...pat].map((p, i) => (p === "1" ? names[i] : p === "0" ? "~" + names[i] : "")).filter((x) => x); return t.length ? t.join(".") : "1"; }
function primeCover(mins, nv) {
  const ms = new Set(mins), pats = []; const gen = (p) => { if (p.length === nv) { pats.push(p); return; } ["0", "1", "-"].forEach((c) => gen(p + c)); }; gen("");
  const ok = pats.filter((p) => { const c = coverOf(p, nv); return c.length && c.every((m) => ms.has(m)); });
  const cv = {}; ok.forEach((p) => cv[p] = new Set(coverOf(p, nv)));
  const primes = ok.filter((p) => !ok.some((q) => q !== p && cv[q].size > cv[p].size && [...cv[p]].every((m) => cv[q].has(m))));
  let best = null;
  for (let k = 1; k <= primes.length && !best; k++) { const pick = (start, chosen) => { if (chosen.length === k) { const u = new Set(); chosen.forEach((p) => cv[p].forEach((m) => u.add(m))); if (u.size === ms.size && [...ms].every((m) => u.has(m))) { const lit = chosen.reduce((a, p) => a + [...p].filter((c) => c !== "-").length, 0); if (!best || lit < best.lit) best = { lit, chosen: chosen.slice() }; } return; } for (let i = start; i < primes.length; i++) { chosen.push(primes[i]); pick(i + 1, chosen); chosen.pop(); } }; pick(0, []); }
  return best ? best.chosen.map((p) => ({ pat: p, cells: coverOf(p, nv) })) : [];
}
function sopJS(mins, names) { if (!mins.length) return "0"; return [...mins].sort((a, b) => a - b).map((m) => termOf(bitsOf(m, names.length).join(""), names)).join(" + "); }
function simpJS(mins, names) { const nv = names.length; if (!mins.length) return "0"; if (mins.length === 1 << nv) return "1"; return primeCover(mins, nv).map((g) => termOf(g.pat, names)).join(" + "); }
const GRAYS = ["00", "01", "11", "10"], KCOL = ["var(--accent)", "var(--bad)", "var(--good)", "var(--warn)", "var(--k)", "var(--n)"];
/* K-map table as HTML; mins is the set of ones, groups a list of cell lists to ring, click a cell with data-m */
function kmapJS(mins, names, groups, clickable) {
  const nv = names.length, ms = new Set(mins);
  const cols = nv === 4 ? GRAYS : nv === 3 ? GRAYS : ["0", "1"], rows = nv === 4 ? GRAYS : nv === 3 ? ["0", "1"] : ["0", "1"];
  const corner = nv === 4 ? names[2] + names[3] + " \\ " + names[0] + names[1] : nv === 3 ? names[0] + " \\ " + names[1] + names[2] : names[1] + " \\ " + names[0];
  let h = '<div class="tw"><table class="km"><tr><th>' + corner + "</th>" + cols.map((c) => "<th>" + c + "</th>").join("") + "</tr>";
  rows.forEach((r) => { h += "<tr><th>" + r + "</th>"; cols.forEach((c) => { const m = parseInt(nv === 3 ? r + c : c + r, 2); const gi = (groups || []).map((g, k) => (g.includes(m) ? k : -1)).filter((k) => k >= 0); const sh = gi.map((k, j) => "inset 0 0 0 " + (3 + 3 * j) + "px " + KCOL[k % 6]).join(","); h += '<td data-m="' + m + '"' + (sh ? ' style="box-shadow:' + sh + '"' : "") + (clickable ? ' class="clk"' : "") + '><span class="v">' + (ms.has(m) ? 1 : 0) + '</span><span class="n">' + m + "</span></td>"; }); h += "</tr>"; });
  return h + "</table></div>";
}
function kgroupsJS(mins, names) {
  const nv = names.length, cov = (mins.length && mins.length < 1 << nv) ? primeCover(mins, nv) : [];
  const leg = cov.map((g, i) => '<span class="kg" style="--c:' + KCOL[i % 6] + '">' + obJS(termOf(g.pat, names)) + "</span>").join(" ");
  return kmapJS(mins, names, cov.map((g) => g.cells), true) + '<p class="kleg">' + (cov.length ? "Groups: " + leg : mins.length ? "Every cell is 1: the output is always 1." : "No 1s: the output is always 0.") + "</p>";
}
const PRE = [["M/J 2026 P31 6(c)", "ABCD", [3, 5, 7, 11, 12, 13, 14, 15]], ["M/J 2026 P32 7(a)", "ABCD", [1, 4, 5, 6, 7, 9, 12, 13, 14, 15]], ["M/J 2026 P33 6(a)", "ABCD", [4, 5, 6, 7, 12, 14]], ["O/N 2025 P33 6(a)", "ABCD", [1, 5, 7, 10, 11, 13, 14, 15]], ["O/N 2025 P31 6(b)", "ABC", [2, 3, 5, 6]], ["O/N 2025 P32 6(b)", "ABC", [1, 3, 5, 6]], ["M/J 2025 P31 5(b)", "ABCD", [0, 5, 7, 8, 13, 15]], ["O/N 2024 P31/33 7", "ABCD", [1, 3, 9, 11, 13, 15]], ["M/J 2023 P32 9", "ABCD", [0, 1, 2, 3, 6, 7]], ["O/N 2021 P31/32 7(b)", "ABCD", [9, 11, 12, 13, 14, 15]]];

/* K-map drawn as SVG: o.shown = set of cells whose value is shown, o.groups = [{cells, k}] */
function kmDraw(names, mins, o) {
  const nv = names.length, cols = GRAYS, rows = nv === 4 ? GRAYS : ["0", "1"], X0 = (o.ox || 0) + 96, Y0 = (o.oy || 0) + 40, cw = 70, ch = 52; let s = "";
  const idx = (c, r) => parseInt(nv === 3 ? r + c : c + r, 2), cell = (m) => { for (let ri = 0; ri < rows.length; ri++) for (let ci = 0; ci < 4; ci++) if (idx(cols[ci], rows[ri]) === m) return [ci, ri]; };
  s += SV.text(X0 - 8, Y0 - 24, nv === 4 ? "CD \\ AB" : "A \\ BC", "sm", { "text-anchor": "end" });
  cols.forEach((c, i) => (s += SV.text(X0 + i * cw + cw / 2, Y0 - 10, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" })));
  rows.forEach((r, i) => (s += SV.text(X0 - 14, Y0 + i * ch + ch / 2 + 5, r, "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono)" })));
  rows.forEach((r, ri) => cols.forEach((c, ci) => { const m = idx(c, r), shown = !o.shown || o.shown.has(m); s += SV.rect(X0 + ci * cw, Y0 + ri * ch, cw, ch, "cell", { rx: 2 }) + (shown ? SV.text(X0 + ci * cw + cw / 2, Y0 + ri * ch + ch / 2 + 7, mins.includes(m) ? "1" : "0", "lbl bd", { "text-anchor": "middle", style: "font-size:22px;font-family:var(--mono)" }) : "") + SV.text(X0 + ci * cw + cw - 5, Y0 + ri * ch + ch - 5, String(m), "sm", { "text-anchor": "end", style: "font-size:9px" }); }));
  (o.groups || []).forEach((g, k) => g.cells.forEach((m) => { const [ci, ri] = cell(m); s += SV.rect(X0 + ci * cw + 3 + 3 * g.k, Y0 + ri * ch + 3 + 3 * g.k, cw - 6 - 6 * g.k, ch - 6 - 6 * g.k, "ax", { rx: 8, fill: "none", style: "stroke:" + KCOL[g.k % 6] + ";stroke-width:3" }); }));
  return s;
}
/* 1: truth table to map */
(function () {
  const names = ["A", "B", "C", "D"], mins = [0, 5, 7, 8, 13, 15], order = [0, 5, 7, 8, 13, 15];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 20, "A B C D   Z", "lbl bd", { style: "font-family:var(--mono)" });
    for (let m = 0; m < 16; m++) { const one = mins.includes(m), at = order.indexOf(m), cur = one && at === k - 1, done = one && at < k - 1; o += SV.rect(8, 28 + m * 22, 150, 20, cur ? "cell-warn" : done ? "cell-ok" : "cell", { rx: 3 }) + SV.text(14, 43 + m * 22, bitsOf(m, 4).join(" ") + "   " + (one ? 1 : 0), "lbl", { style: "font-family:var(--mono);font-size:12px" }); }
    const mm = mins.filter((m) => order.indexOf(m) < k);
    return o + kmDraw(names, mm, { ox: 170, oy: 0, shown: k === 0 ? new Set() : k === 6 ? undefined : new Set(mm) }); };
  const caps = ["Each row of the truth table has a cell on the map. Columns are A B and rows are C D, both in Gray code order.", "Row 0000 (Z = 1) goes in column AB = 00, row CD = 00.", "Row 0101 (Z = 1): AB = 01, CD = 01.", "Row 0111: AB = 01, CD = 11.", "Row 1000: AB = 10, CD = 00. This cell is at the far right of the map.", "Row 1101: AB = 11, CD = 01.", "Row 1111: AB = 11, CD = 11. All six 1s are placed; every other cell is 0."];
  Lib.stepper($("#stA"), { w: 560, h: 400, label: "Truth table to K-map", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: caps.map((c, i) => ({ cap: c, s: { i } })) });
})();
/* 2: loops on the map */
(function () {
  const names = ["A", "B", "C", "D"], mins = [3, 5, 7, 11, 12, 13, 14, 15];
  const gs = [{ cells: [3, 7, 15, 11], k: 0, t: "C.D" }, { cells: [12, 13, 15, 14], k: 1, t: "A.B" }, { cells: [5, 7, 13, 15], k: 2, t: "B.D" }];
  const draw = (s) => { const k = Math.round(s.i); let o = kmDraw(names, mins, { ox: 40, oy: 0, groups: gs.slice(0, k) });
    gs.slice(0, k).forEach((g, i) => (o += SV.text(430, 60 + i * 30, "loop " + (i + 1) + ": " + g.t.replace(/~/g, "¬"), "lbl bd", { style: "fill:" + KCOL[i] + ";font-family:var(--mono)" })));
    if (k === 3) o += SV.text(430, 160, "X = A.B + B.D + C.D", "lbl bd t3", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 300, label: "Loops", base: { i: 0 }, draw, tween: 150, dwell: 3000, steps: [{ cap: "The 1s of the map from M/J 2026 Paper 31. Look for the biggest groups.", s: { i: 0 } }, { cap: "Loop 1: the CD = 11 row is a group of four. C = 1 and D = 1 all along, A and B change: the term is <b>C.D</b>.", s: { i: 1 } }, { cap: "Loop 2: the AB = 11 column is a group of four. A = 1, B = 1, C and D change: <b>A.B</b>.", s: { i: 2 } }, { cap: "Loop 3: the block B = 1, D = 1 (cells 5, 7, 13, 15) overlaps the others: <b>B.D</b>. Every 1 is now looped. X = A.B + B.D + C.D.", s: { i: 3 } }] });
})();
/* 3: wrap-around */
(function () {
  const names = ["A", "B", "C", "D"], mins = [4, 5, 6, 7, 12, 14];
  const gs = [{ cells: [4, 5, 7, 6], k: 0 }, { cells: [4, 6, 12, 14], k: 1 }];
  const draw = (s) => { const k = Math.round(s.i); let o = kmDraw(names, mins, { ox: 40, oy: 0, groups: gs.slice(0, k) });
    if (k >= 1) o += SV.text(430, 60, "¬A.B  (column AB = 01)", "lbl bd", { style: "fill:" + KCOL[0] + ";font-family:var(--mono)" }); if (k >= 2) o += SV.text(430, 90, "B.¬D  (rows 00 and 10 wrap)", "lbl bd", { style: "fill:" + KCOL[1] + ";font-family:var(--mono)" }); if (k >= 3) o += SV.text(430, 130, "¬A.B + B.¬D = B.(¬A + ¬D)", "lbl bd t3", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stC"), { w: 700, h: 300, label: "Wrap-around", base: { i: 0 }, draw, tween: 150, dwell: 3000, steps: [{ cap: "A K-map for M/J 2026 Paper 33. The 1s in cells 4, 5, 6, 7, 12 and 14.", s: { i: 0 } }, { cap: "The whole AB = 01 column is a group of four: A = 0 and B = 1 throughout, so <b>¬A.B</b>.", s: { i: 1 } }, { cap: "Cells 4, 6, 12 and 14 form a group of four <b>that wraps</b>: the top row (CD = 00) and the bottom row (CD = 10) are neighbours. B = 1 and D = 0 throughout: <b>B.¬D</b>.", s: { i: 2 } }, { cap: "Then algebra: take out B. The simplest form is <b>B.(¬A + ¬D)</b>.", s: { i: 3 } }] });
})();

/* lab 1 */
(function () {
  let nv = 4, mins = [3, 5, 7, 11, 12, 13, 14, 15]; const b = $("#kB");
  const names = () => ["A", "B", "C", "D"].slice(0, nv);
  const paint = () => { $("#kM").innerHTML = kgroupsJS(mins, names()); $("#kM").querySelectorAll("td[data-m]").forEach((td) => (td.onclick = () => { const m = +td.dataset.m; mins = mins.includes(m) ? mins.filter((x) => x !== m) : mins.concat(m); paint(); }));
    $("#kV").innerHTML = "Simplified sum-of-products: <b>" + obJS(simpJS(mins, names())) + "</b><br>Full sum-of-products has " + mins.length + " term" + (mins.length === 1 ? "" : "s") + "."; };
  [[3, "3 inputs"], [4, "4 inputs"]].forEach(([n, t]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { nv = n; mins = mins.filter((m) => m < 1 << n); b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; paint(); }; b.appendChild(x); });
  const cl = document.createElement("button"); cl.textContent = "Clear"; cl.onclick = () => { mins = []; paint(); }; b.appendChild(cl); b.children[1].className = "on"; paint();
})();
/* lab 2 */
(function () {
  const b = $("#pB");
  const show = (i) => { const [n, nm, m] = PRE[i], names = nm.split(""); $("#pM").innerHTML = "<p><b>" + n + "</b></p>" + kgroupsJS(m, names); $("#pV").innerHTML = "Simplified sum-of-products: <b>" + obJS(simpJS(m, names)) + "</b>"; };
  PRE.forEach((p, i) => { const x = document.createElement("button"); x.textContent = p[0]; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
/* lab 3 */
(function () {
  let k = 2;
  const info = [["1 cell", "no inputs dropped", "a full product term, e.g. A.~B.C.D"], ["2 cells", "1 input dropped", "a term of 3 inputs"], ["4 cells", "2 inputs dropped", "a term of 2 inputs"], ["8 cells", "3 inputs dropped", "a term of 1 input"], ["16 cells", "4 inputs dropped", "the constant 1"]];
  const paint = () => { const [a, b, c] = info[k]; $("#gO").innerHTML = '<div class="verdict">A loop of <b>' + a + "</b> in a 4-input map: <b>" + b + "</b>, so the term is " + c + ". Each doubling of the loop removes one more input.</div>"; };
  Lib.slider($("#gS"), { id: "gss", label: "Loop size (power of 2): ", min: 0, max: 4, value: k, fmt: (x) => Math.pow(2, x), onInput: (v) => { k = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Is the group a valid K-map loop?", buckets: [{"label": "Valid"}, {"label": "Not valid"}], items: [{"text": "Two 1s side by side", "b": 0}, {"text": "Three 1s in a row", "b": 1}, {"text": "A 2 by 2 block of 1s", "b": 0}, {"text": "Two 1s joined diagonally", "b": 1}, {"text": "Left-hand and right-hand 1s in the same row (wrapping)", "b": 0}, {"text": "A block containing a 0", "b": 1}, {"text": "All eight 1s of two adjacent columns", "b": 0}], done: "A loop is a rectangle of 1s with 1, 2, 4, 8 or 16 cells." });
Lib.classify($("#cl2"), { prompt: "How many inputs does the loop drop on a 4-input map?", buckets: [{"label": "One"}, {"label": "Two"}, {"label": "Three"}], items: [{"text": "A loop of two cells", "b": 0}, {"text": "A loop of four cells", "b": 1}, {"text": "A loop of eight cells", "b": 2}, {"text": "The four corner cells", "b": 1}, {"text": "A full row of four", "b": 1}, {"text": "Two full columns", "b": 2}], done: "2 cells: one input; 4 cells: two; 8 cells: three." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Gray code", "The label order 00, 01, 11, 10"], ["A loop of four", "Drops two inputs"], ["Wrap-around", "Left and right edges are neighbours, and top and bottom"], ["Simplified sum-of-products", "One AND term per loop, joined by OR"], ["Optimal", "Fewest and largest loops"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for using a K-map in order.", items: ["Write the output of each row in its cell, with the 0s as well", "Loop groups of 1s: the largest powers of two, wrapping round the edges", "For each loop keep the inputs that do not change", "Join the terms with OR", "Use Boolean algebra only if asked for the simplest form"], done: "Fill, loop, read, join, factor." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many cells does a K-map for four inputs have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2 to the power 4.", "sol": "<b>16</b>."},
  {"q": "A loop of eight cells on a four-input map: how many inputs are in its term?", "a": 1, "unit": "", "tol": 0.01, "hint": "Three are dropped.", "sol": "<b>1</b>."},
  {"q": "A loop of four cells on a four-input map: how many inputs are in its term?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two are dropped.", "sol": "<b>2</b>."},
  {"q": "How many cells does a three-input K-map have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 cubed.", "sol": "<b>8</b>."},
  {"q": "The four corner cells of a four-input map are looped. How many inputs are in the term?", "a": 2, "unit": "", "tol": 0.01, "hint": "~B.~D.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the correct column order for a K-map?", opts: ["00 01 10 11", "00 01 11 10", "00 10 01 11", "01 00 10 11"], a: 1, why: "Gray code." },
  { q: "Which loop size is NOT allowed?", opts: ["2", "4", "6", "8"], a: 2, why: "Powers of two only." },
  { q: "A loop's term contains the inputs that:", opts: ["change inside the loop", "do not change inside the loop", "are all 0", "are all 1"], a: 1, why: "The constant ones." },
  { q: "A benefit of a K-map is that it:", opts: ["Is faster to draw than a truth table", "Is guaranteed to give an optimal solution", "Uses fewer inputs", "Always gives a single term"], a: 1, why: "Guaranteed optimal." },
  { q: "Can loops overlap?", opts: ["No", "Yes", "Only in 3-input maps", "Only with 8 cells"], a: 1, why: "Overlapping is allowed." },
  { q: "Cells 0000 and 1000 on a 4-input map are:", opts: ["Not neighbours", "Neighbours (the edges wrap)", "Neighbours only diagonally", "The same cell"], a: 1, why: "Edges wrap round." },
] });
Lib.cards($("#fc1"), { cards: [
  ["K-map", "Grid of a truth table in Gray code order."],
  ["Gray code", "00, 01, 11, 10."],
  ["Loop", "Rectangle of 1, 2, 4, 8 or 16 cells containing only 1s."],
  ["Wrap", "Left and right, top and bottom and the corners."],
  ["Reading a loop", "Keep inputs that do not change: 1 plain, 0 barred."],
  ["Loop of 2", "Drops one input."],
  ["Loop of 4", "Drops two inputs."],
  ["Benefit", "No Boolean algebra; guaranteed optimal solution."],
] });
