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
  const corner = nv === 4 ? names[2] + names[3] + " \\ " + names[0] + names[1] : nv === 3 ? names[2] + " \\ " + names[0] + names[1] : names[1] + " \\ " + names[0];
  let h = '<div class="tw"><table class="km"><tr><th>' + corner + "</th>" + cols.map((c) => "<th>" + c + "</th>").join("") + "</tr>";
  rows.forEach((r) => { h += "<tr><th>" + r + "</th>"; cols.forEach((c) => { const m = parseInt(c + r, 2); const gi = (groups || []).map((g, k) => (g.includes(m) ? k : -1)).filter((k) => k >= 0); const sh = gi.map((k, j) => "inset 0 0 0 " + (3 + 3 * j) + "px " + KCOL[k % 6]).join(","); h += '<td data-m="' + m + '"' + (sh ? ' style="box-shadow:' + sh + '"' : "") + (clickable ? ' class="clk"' : "") + '><span class="v">' + (ms.has(m) ? 1 : 0) + '</span><span class="n">' + m + "</span></td>"; }); h += "</tr>"; });
  return h + "</table></div>";
}
function kgroupsJS(mins, names) {
  const nv = names.length, cov = (mins.length && mins.length < 1 << nv) ? primeCover(mins, nv) : [];
  const leg = cov.map((g, i) => '<span class="kg" style="--c:' + KCOL[i % 6] + '">' + obJS(termOf(g.pat, names)) + "</span>").join(" ");
  return kmapJS(mins, names, cov.map((g) => g.cells), true) + '<p class="kleg">' + (cov.length ? "Groups: " + leg : mins.length ? "Every cell is 1: the output is always 1." : "No 1s: the output is always 0.") + "</p>";
}
const SIMP = [{"n": "M/J 2026 P33 6(b)", "a": "~(A+B+C) + ~(B+C)", "b": "~B.~C", "f": "(a,b,c)=>!(a|b|c)|!(b|c)", "g": "(a,b,c)=>!b&!c", "nv": 3}, {"n": "O/N 2025 P33 6(b)", "a": "~(A+B+C) + ~(~B+C)", "b": "~C.(~A+B)", "f": "(a,b,c)=>!(a|b|c)|!(!b|c)", "g": "(a,b,c)=>!c&(!a|b)", "nv": 3}, {"n": "O/N 2022 P32 8(c)", "a": "~(~(A.B).~(A.C).~(B.D))", "b": "A.(B+C) + B.D", "f": "(a,b,c,d)=>!(!(a&b)&!(a&c)&!(b&d))", "g": "(a,b,c,d)=>(a&(b|c))|(b&d)", "nv": 4}, {"n": "O/N 2023 P31 6(b)", "a": "~A.~B.~C.~D + ~A.~B.C.~D + ~A.B.~C.~D + ~A.B.C.~D", "b": "~A.~D", "f": "(a,b,c,d)=>(!a&!b&!c&!d)|(!a&!b&c&!d)|(!a&b&!c&!d)|(!a&b&c&!d)", "g": "(a,b,c,d)=>!a&!d", "nv": 4}, {"n": "M/J 2025 P32 7(c)", "a": "~(A+B) . (~(A.B) + ~(B.C))", "b": "~A.~B", "f": "(a,b,c)=>!(a|b)&(!(a&b)|!(b&c))", "g": "(a,b,c)=>!a&!b", "nv": 3}];

/* 1: sum-of-products from the truth table 011, 101, 110 */
(function () {
  const names = ["A", "B", "C"], mins = [3, 5, 6];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; o += SV.text(14, 18, "A  B  C   X", "lbl bd", { style: "font-family:var(--mono)" });
    for (let m = 0; m < 8; m++) { const b = bitsOf(m, 3), one = mins.includes(m), hit = one && mins.indexOf(m) < k; o += SV.rect(8, 28 + m * 30, 190, 26, hit ? "cell-ok" : "cell", { rx: 4 }) + SV.text(14, 46 + m * 30, b.join("  ") + "   " + (one ? 1 : 0), "lbl", { style: "font-family:var(--mono)" }); if (hit) o += SV.text(220, 46 + m * 30, "→ " + [...b].map((x, i) => (x ? names[i] : "~" + names[i])).join("."), "lbl bd t3", { style: "font-family:var(--mono)" }); }
    if (k >= 3) o += SV.text(8, 285, "X = ~A.B.C + A.~B.C + A.B.~C", "lbl bd", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 300, label: "Sum-of-products", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: [{ cap: "Find every row where X = 1: rows 011, 101 and 110.", s: { i: 0 } }, { cap: "Row 011: A = 0, B = 1, C = 1 gives <b>~A.B.C</b>.", s: { i: 1 } }, { cap: "Row 101 gives <b>A.~B.C</b>.", s: { i: 2 } }, { cap: "Row 110 gives <b>A.B.~C</b>. Join the terms with OR.", s: { i: 3 } }] });
})();
/* 2: De Morgan, row by row */
(function () {
  const rows = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 20, "A B   ~(A.B)   ~A + ~B", "lbl bd", { style: "font-family:var(--mono)" });
    rows.forEach(([a, b], i) => { const nand = 1 - (a & b), or = (1 - a) | (1 - b), on = i <= k; o += SV.rect(8, 30 + i * 40, 420, 34, on ? "cell-ok" : "cell", { rx: 6, ...op(on ? 1 : 0.4) }) + SV.text(18, 53 + i * 40, a + " " + b, "lbl bd", { style: "font-family:var(--mono)" }) + (on ? SV.text(110, 53 + i * 40, String(nand), "lbl bd", { style: "font-family:var(--mono)" }) + SV.text(250, 53 + i * 40, String(or), "lbl bd", { style: "font-family:var(--mono)" }) + SV.text(330, 53 + i * 40, "equal", "sm t3") : ""); });
    return o; };
  Lib.stepper($("#stB"), { w: 440, h: 200, label: "De Morgan", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: rows.map(([a, b], i) => ({ cap: `A = ${a}, B = ${b}: ~(A.B) = <b>${1 - (a & b)}</b> and ~A + ~B = <b>${(1 - a) | (1 - b)}</b>. The two sides agree in every row, which proves De Morgan's law for AND.`, s: { i } })) });
})();
/* 3: simplifying X = ~(A+B+C) + ~(B+C) */
(function () {
  const lines = [["X = ~(A+B+C) + ~(B+C)", "start"], ["X = ~A.~B.~C + ~B.~C", "De Morgan's laws"], ["X = ~B.~C.(~A + 1)", "distributive law"], ["X = ~B.~C", "annulment: ~A + 1 = 1"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; lines.forEach(([e, l], i) => { if (i > k) return; o += SV.rect(10, 14 + i * 56, 420, 46, i === k ? "cell-warn" : "cell-ok", { rx: 8 }) + SV.text(24, 43 + i * 56, e.replace(/~/g, "¬"), "lbl bd", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(446, 43 + i * 56, l, "sm"); }); return o; };
  Lib.stepper($("#stC"), { w: 700, h: 240, label: "Simplifying", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [{ cap: "Start from the given expression. In the exam, ¬ is written as a bar above the letters.", s: { i: 0 } }, { cap: "Break each bar with De Morgan's law: a bar over OR becomes AND of the barred terms.", s: { i: 1 } }, { cap: "~B.~C is common to both terms, so take it out with the distributive law.", s: { i: 2 } }, { cap: "~A + 1 is always 1 (annulment). The answer is <b>~B.~C</b>.", s: { i: 3 } }] });
})();

/* lab 1 */
(function () {
  const names = ["A", "B", "C"]; let out = [0, 0, 0, 0, 0, 0, 0, 0]; const el = $("#sopT");
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>A</th><th>B</th><th>C</th><th>X (click)</th></tr>'; for (let m = 0; m < 8; m++) h += "<tr>" + bitsOf(m, 3).map((x) => "<td>" + x + "</td>").join("") + `<td><button data-m="${m}" class="${out[m] ? "on" : ""}">${out[m]}</button></td></tr>`; el.innerHTML = h + "</table></div>";
    const mins = out.map((v, i) => (v ? i : -1)).filter((x) => x >= 0); $("#sopV").innerHTML = "Sum-of-products: <b>X = " + obJS(sopJS(mins, names)) + "</b><br>Simplified: <b>X = " + obJS(simpJS(mins, names)) + "</b>";
    el.querySelectorAll("button").forEach((b) => b.onclick = () => { out[+b.dataset.m] ^= 1; paint(); }); };
  out[1] = out[4] = out[5] = out[7] = 1; paint();
})();
/* lab 2 */
(function () {
  const L = [["De Morgan (AND)", "~(A.B)", "~A + ~B", (a, b) => 1 - (a & b), (a, b) => (1 - a) | (1 - b)], ["De Morgan (OR)", "~(A+B)", "~A . ~B", (a, b) => 1 - (a | b), (a, b) => (1 - a) & (1 - b)], ["Absorption", "A + A.B", "A", (a, b) => a | (a & b), (a, b) => a], ["Distributive", "A.(A+B)", "A", (a, b) => a & (a | b), (a, b) => a], ["Redundancy", "A + ~A.B", "A + B", (a, b) => a | ((1 - a) & b), (a, b) => a | b], ["Idempotent", "A.A", "A", (a, b) => a & a, (a, b) => a]];
  const show = (i) => { const [n, l, r, f, g] = L[i]; let h = `<h3>${n}</h3><div class="tw"><table class="t mono"><tr><th>A</th><th>B</th><th>${obJS(l)}</th><th>${obJS(r)}</th><th></th></tr>`; for (let m = 0; m < 4; m++) { const a = m >> 1, b = m & 1, x = f(a, b), y = g(a, b); h += `<tr><td>${a}</td><td>${b}</td><td>${x}</td><td>${y}</td><td>${x === y ? "equal" : "different"}</td></tr>`; } $("#lwO").innerHTML = h + "</table></div>"; };
  const b = $("#lwB"); L.forEach((l, i) => { const x = document.createElement("button"); x.textContent = l[0]; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
/* lab 3 */
(function () {
  const b = $("#spB");
  const show = (i) => { const e = SIMP[i], f = eval(e.f), g = eval(e.g), nv = e.nv, names = ["A", "B", "C", "D"].slice(0, nv);
    let h = `<p><b>${e.n}</b></p><p>Original: <span class="bx">${obJS(e.a)}</span><br>Simplified: <span class="bx">${obJS(e.b)}</span></p><div class="tw"><table class="t mono"><tr>` + names.map((n) => `<th>${n}</th>`).join("") + "<th>original</th><th>simplified</th></tr>";
    for (let m = 0; m < 1 << nv; m++) { const bb = bitsOf(m, nv), x = +!!f(...bb), y = +!!g(...bb); h += "<tr>" + bb.map((v) => `<td>${v}</td>`).join("") + `<td>${x}</td><td>${y}</td></tr>`; }
    $("#spO").innerHTML = h + "</table></div>"; };
  SIMP.forEach((e, i) => { const x = document.createElement("button"); x.textContent = e.n; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
Lib.classify($("#cl1"), { prompt: "Which law is used?", buckets: [{"label": "De Morgan"}, {"label": "Double negation"}, {"label": "Absorption"}, {"label": "Distributive"}], items: [{"text": "~(A + B) = ~A . ~B", "b": 0}, {"text": "~~A = A", "b": 1}, {"text": "A + A.B = A", "b": 2}, {"text": "A.(B + C) = A.B + A.C", "b": 3}, {"text": "~(A . B) = ~A + ~B", "b": 0}, {"text": "A . (A + B) = A", "b": 2}], done: "De Morgan breaks a bar, double negation cancels two bars, absorption removes a term that contains another, distributive takes out a common factor." });
Lib.classify($("#cl2"), { prompt: "Does the statement apply De Morgan's law correctly?", buckets: [{"label": "Correct"}, {"label": "Incorrect"}], items: [{"text": "~(A + B) = ~A . ~B", "b": 0}, {"text": "~(A + B) = ~A + ~B", "b": 1}, {"text": "~(A . B) = ~A + ~B", "b": 0}, {"text": "~(A . B) = ~A . ~B", "b": 1}, {"text": "~(~A . B) = A + ~B", "b": 0}, {"text": "~(~A + B) = A + ~B", "b": 1}], done: "Change the operator and bar each term; ~(~A + B) = A . ~B." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["A + A.B", "A (absorption)"], ["~(A.B)", "~A + ~B"], ["A.~A", "0 (inverse)"], ["A + ~A", "1 (inverse)"], ["A + ~A.B", "A + B (redundancy)"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for simplifying a bar over a group in order.", items: ["Break the bar with De Morgan's law", "Cancel any double bars", "Take out a common factor", "Use the inverse, absorption or annulment law to remove terms", "State the simplified expression"], done: "Break, cancel, factor, remove, state." });
Lib.calc($("#c1"), { qs: [
  {"q": "A truth table has 16 rows and the output is 1 in six rows. How many terms does the sum-of-products have?", "a": 6, "unit": "", "tol": 0.01, "hint": "One term per 1.", "sol": "<b>6</b>."},
  {"q": "How many rows does a truth table for three inputs have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 cubed.", "sol": "<b>8</b>."},
  {"q": "How many literals (letters, counting bars) are in the term ~A.B.~C.D?", "a": 4, "unit": "", "tol": 0.01, "hint": "One per variable.", "sol": "<b>4</b>."},
  {"q": "Using absorption, simplify A + A.B. How many literals remain?", "a": 1, "unit": "", "tol": 0.01, "hint": "The answer is A.", "sol": "<b>1</b>."},
  {"q": "~(A + B) = ~A . ~B. For A = 1 and B = 0, what is the value of the left-hand side?", "a": 0, "unit": "", "tol": 0.01, "hint": "1 + 0 = 1, then NOT.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is ~(A . B) equal to?", opts: ["~A . ~B", "~A + ~B", "A + B", "A . B"], a: 1, why: "Bar over AND becomes OR of barred terms." },
  { q: "A sum-of-products has a term for every row where the output is:", opts: ["0", "1", "either", "neither"], a: 1, why: "The rows with output 1." },
  { q: "What does the absorption law say?", opts: ["A + A.B = A", "A + A = 1", "A.A = 0", "A + 1 = A"], a: 0, why: "A + A.B = A." },
  { q: "Which is the same as ~~A?", opts: ["~A", "A", "0", "1"], a: 1, why: "Double negation." },
  { q: "The annulment law says A + 1 equals:", opts: ["A", "0", "1", "~A"], a: 2, why: "OR with 1 is always 1." },
  { q: "Which gate is the same as ~(A + B)?", opts: ["AND", "NOR", "NAND", "XOR"], a: 1, why: "NOR." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Sum-of-products", "One AND term per 1 in the output, joined by OR."],
  ["De Morgan", "~(A+B) = ~A.~B and ~(A.B) = ~A+~B."],
  ["Double negation", "~~A = A."],
  ["Absorption", "A + A.B = A."],
  ["Distributive", "A.(B+C) = A.B + A.C."],
  ["Annulment", "A + 1 = 1 and A.0 = 0."],
  ["Inverse", "A.~A = 0 and A + ~A = 1."],
  ["Redundancy", "A + ~A.B = A + B."],
] });
