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
const GH = {"w": 264, "h": 141.0, "inputs": [{"n": "A", "y": 24}, {"n": "B", "y": 70}], "gates": [{"n": "S", "x": 94, "cy": 34, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,13.0 Q126.4,13.0 148,34 Q126.4,55.0 94,55.0 Q109.12,34 94,13.0 Z\"/><path class=\"ax\" d=\"M87,13.0 Q99,34 87,55.0\"/>", "ox": 148}, {"n": "C", "x": 94, "cy": 96, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,75.0 H121.0 A27.0,21.0 0 0 1 121.0,117.0 H94 Z\"/>", "ox": 148}], "wires": [{"d": "M58,24 H82 V23.0 H92.48571428571428", "s": "A", "dot": null}, {"d": "M58,70 H77 V45.0 H92.48571428571428", "s": "B", "dot": null}, {"d": "M58,24 H82 V85.0 H94", "s": "A", "dot": null}, {"d": "M58,70 H77 V107.0 H94", "s": "B", "dot": null}, {"d": "M50,24 H58", "s": "A", "dot": null}, {"d": "M50,70 H58", "s": "B", "dot": null}], "outs": [{"d": "M148,34 H178", "s": "S", "x": 178, "y": 34}, {"d": "M148,96 H178", "s": "C", "x": 178, "y": 96}], "outset": ["C", "S"], "net": [["S", "XOR", ["A", "B"]], ["C", "AND", ["A", "B"]]], "in": ["A", "B"]}, GF = {"w": 500, "h": 241.0, "inputs": [{"n": "A", "y": 22}, {"n": "B", "y": 62}, {"n": "Cin", "y": 118}], "gates": [{"n": "P", "x": 94, "cy": 40, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,19.0 Q126.4,19.0 148,40 Q126.4,61.0 94,61.0 Q109.12,40 94,19.0 Z\"/><path class=\"ax\" d=\"M87,19.0 Q99,40 87,61.0\"/>", "ox": 148}, {"n": "Q", "x": 94, "cy": 196, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,175.0 H121.0 A27.0,21.0 0 0 1 121.0,217.0 H94 Z\"/>", "ox": 148}, {"n": "Sum", "x": 212, "cy": 74, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,53.0 Q244.4,53.0 266,74 Q244.4,95.0 212,95.0 Q227.12,74 212,53.0 Z\"/><path class=\"ax\" d=\"M205,53.0 Q217,74 205,95.0\"/>", "ox": 266}, {"n": "R", "x": 212, "cy": 140, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,119.0 H239.0 A27.0,21.0 0 0 1 239.0,161.0 H212 Z\"/>", "ox": 266}, {"n": "Cout", "x": 330, "cy": 168, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M330,147.0 Q362.4,147.0 384,168 Q362.4,189.0 330,189.0 Q345.12,168 330,147.0 Z\"/>", "ox": 384}], "wires": [{"d": "M58,22 H82 V29.0 H92.48571428571428", "s": "A", "dot": null}, {"d": "M58,62 H77 V51.0 H92.48571428571428", "s": "B", "dot": null}, {"d": "M58,22 H82 V185.0 H94", "s": "A", "dot": null}, {"d": "M58,62 H77 V207.0 H94", "s": "B", "dot": null}, {"d": "M148,40 H200 V63.0 H210.4857142857143", "s": "P", "dot": [200, 40]}, {"d": "M58,118 H195 V85.0 H210.4857142857143", "s": "Cin", "dot": null}, {"d": "M148,40 H200 V129.0 H212", "s": "P", "dot": [200, 40]}, {"d": "M58,118 H195 V151.0 H212", "s": "Cin", "dot": null}, {"d": "M266,140 H318 V157.0 H335.48571428571427", "s": "R", "dot": null}, {"d": "M148,196 H313 V179.0 H335.48571428571427", "s": "Q", "dot": null}, {"d": "M50,22 H58", "s": "A", "dot": null}, {"d": "M50,62 H58", "s": "B", "dot": null}, {"d": "M50,118 H58", "s": "Cin", "dot": null}], "outs": [{"d": "M266,74 H414", "s": "Sum", "x": 414, "y": 74}, {"d": "M384,168 H414", "s": "Cout", "x": 414, "y": 168}], "outset": ["Cout", "Sum"], "net": [["P", "XOR", ["A", "B"]], ["Q", "AND", ["A", "B"]], ["Sum", "XOR", ["P", "Cin"]], ["R", "AND", ["P", "Cin"]], ["Cout", "OR", ["R", "Q"]]], "in": ["A", "B", "Cin"]};

(function () {
  const cases = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const draw = (s) => { const [a, b] = cases[Math.round(s.i)]; const v = circEval(GH, { A: a, B: b }); return circFit(GH, v, 560, { vals: true }); };
  Lib.stepper($("#stA"), { w: 560, h: Math.round(GH.h * 2.2) + 12, label: "Half adder", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: cases.map(([a, b], i) => ({ cap: `A = ${a}, B = ${b}: sum = ${a} XOR ${b} = <b>${a ^ b}</b>, carry = ${a} AND ${b} = <b>${a & b}</b>. ` + (i === 3 ? "Binary 1 + 1 = 10: the sum bit is 0 and a 1 is carried." : i === 0 ? "Nothing to add, nothing to carry." : "Only one input is 1: sum 1, no carry."), s: { i } })) });
})();
(function () {
  const draw = (s) => { const v = circEval(GF, { A: 1, B: 1, Cin: 1 }); const k = Math.round(s.i), show = {}; ["A", "B", "Cin"].forEach((n) => show[n] = 1);
    const on = { 0: [], 1: ["P", "Q"], 2: ["P", "Q", "R", "Sum"], 3: ["P", "Q", "R", "Sum", "Cout"] }[k]; Object.keys(v).forEach((n) => { if (!["A", "B", "Cin"].includes(n) && !on.includes(n)) v[n] = 0; }); return circFit(GF, v, 620, { vals: true }); };
  Lib.stepper($("#stB"), { w: 620, h: Math.round(GF.h * Math.min(2.2, 600 / GF.w)) + 12, label: "Full adder", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [
    { cap: "Inputs A = 1, B = 1 and carry in = 1.", s: { i: 0 } },
    { cap: "The first half adder: P = 1 XOR 1 = <b>0</b>, Q = 1 AND 1 = <b>1</b>.", s: { i: 1 } },
    { cap: "The second half adder adds P and the carry in: Sum = 0 XOR 1 = <b>1</b>, R = 0 AND 1 = <b>0</b>.", s: { i: 2 } },
    { cap: "The OR gate combines the carries: carry out = R OR Q = 0 OR 1 = <b>1</b>. Result 11 (binary), which is 3: 1 + 1 + 1 = 3.", s: { i: 3 } }] });
})();
(function () {
  const A = [0, 1, 1, 0], B = [0, 1, 1, 1];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "", c = 0; const sums = [], cs = [];
    for (let i = 3; i >= 0; i--) { const t = A[i] + B[i] + c; sums[i] = t % 2; c = t >> 1; cs[i] = c; }
    const lab = ["bit 3", "bit 2", "bit 1", "bit 0"];
    [0, 1, 2, 3].forEach((i) => { const x = 50 + i * 150; o += SV.text(x + 40, 18, lab[i], "sm", { "text-anchor": "middle" }); const col = 3 - i; const doneCol = k > col;
      o += SV.rect(x, 30, 80, 38, "cell", { rx: 6 }) + SV.text(x + 40, 56, "A " + A[i], "lbl bd", { "text-anchor": "middle" });
      o += SV.rect(x, 76, 80, 38, "cell", { rx: 6 }) + SV.text(x + 40, 102, "B " + B[i], "lbl bd", { "text-anchor": "middle" });
      o += SV.rect(x, 130, 80, 40, doneCol ? "cell-ok" : (k === col ? "cell-warn" : "cell"), { rx: 6 }) + (doneCol || k === col ? SV.text(x + 40, 156, "sum " + sums[i], "lbl bd", { "text-anchor": "middle" }) : "");
      if (doneCol || k === col) o += SV.text(x - 14, 150, cs[i] ? "carry " + cs[i] + " ←" : "", "sm t3", { "text-anchor": "end" });
    });
    o += SV.text(14, 56, "", "sm"); if (k > 3) o += SV.text(50, 205, "0110 + 0111 = 1101 (6 + 7 = 13)", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 700, h: 225, label: "Ripple-carry addition", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [
    { cap: "Add 0110 and 0111 one column at a time, starting on the right. Bit 0 uses a half adder.", s: { i: 0 } },
    { cap: "Bit 0: 0 + 1 = 1, no carry.", s: { i: 1 } }, { cap: "Bit 1: 1 + 1 + carry 0 = 0, <b>carry 1</b> into bit 2.", s: { i: 2 } },
    { cap: "Bit 2: 1 + 1 + carry 1 = 1, <b>carry 1</b> into bit 3.", s: { i: 3 } }, { cap: "Bit 3: 0 + 0 + carry 1 = 1, no further carry. The answer is 1101.", s: { i: 4 } }] });
})();

circLab("#labH", GH, [], ["S", "C"]);
circLab("#labF", GF, ["P", "Q", "R"], ["Sum", "Cout"]);

btnTable("gB", "gO", [
  ["NOT", "1 when the input is 0", "0 0→1, 1→0", "One input only"],
  ["AND", "1 only when both inputs are 1", "0 0 0 1", "Both"],
  ["OR", "1 when at least one input is 1", "0 1 1 1", "Either"],
  ["NAND", "0 only when both inputs are 1", "1 1 1 0", "AND then NOT"],
  ["NOR", "1 only when both inputs are 0", "1 0 0 0", "OR then NOT"],
  ["XOR", "1 when the inputs are different", "0 1 1 0", "Different"]
], ["Gate", "Output is 1 when", "Output for AB = 00, 01, 10, 11", "Remember"]);

(function () {
  let a = 6, b = 7;
  const paint = () => {
    const ab = bin(a, 4), bb = bin(b, 4); let c = 0, h = '<div class="tw"><table class="t mono"><tr><th></th><th>bit 3</th><th>bit 2</th><th>bit 1</th><th>bit 0</th></tr>';
    const sums = [], cs = [0, 0, 0, 0, 0];
    for (let i = 3; i >= 0; i--) { const t = +ab[i] + +bb[i] + c; sums[i] = t % 2; c = t >> 1; cs[i] = c; }
    h += "<tr><td>carry out</td>" + [0, 1, 2, 3].map((i) => `<td>${cs[i]}</td>`).join("") + "</tr>";
    h += "<tr><td>A</td>" + ab.split("").map((x) => `<td>${x}</td>`).join("") + "</tr><tr><td>B</td>" + bb.split("").map((x) => `<td>${x}</td>`).join("") + "</tr>";
    h += "<tr><td><b>sum</b></td>" + sums.map((x) => `<td><b>${x}</b></td>`).join("") + "</tr></table></div>";
    $("#rT").innerHTML = h + `<div class="verdict">${a} + ${b} = ${a + b}. Four bits show ${sums.join("")} (${parseInt(sums.join(""), 2)})` + (a + b > 15 ? `. <b>Overflow</b>: the carry out of bit 3 is 1, so the true answer needs a fifth bit.` : ".") + "</div>";
  };
  Lib.slider($("#rA"), { id: "ra", label: "A ", min: 0, max: 15, value: a, fmt: (x) => x + " = " + bin(x, 4), onInput: (v) => { a = v; paint(); } });
  Lib.slider($("#rB"), { id: "rb", label: "B ", min: 0, max: 15, value: b, fmt: (x) => x + " = " + bin(x, 4), onInput: (v) => { b = v; paint(); } }); paint();
})();
Lib.classify($("#cl1"), { prompt: "Which gate does the description give?", buckets: [{"label": "AND"}, {"label": "OR"}, {"label": "XOR"}, {"label": "NAND"}], items: [{"text": "Output is 1 only when both inputs are 1", "b": 0}, {"text": "Output is 1 when at least one input is 1", "b": 1}, {"text": "Output is 1 when the inputs are different", "b": 2}, {"text": "Output is 0 only when both inputs are 1", "b": 3}, {"text": "A light that is on when the car is in park and the brake is pressed", "b": 0}, {"text": "An alarm that sounds if either door is open", "b": 1}], done: "AND all, OR any, XOR different, NAND the opposite of AND." });
Lib.classify($("#cl2"), { prompt: "Which circuit has this property?", buckets: [{"label": "Half adder"}, {"label": "Full adder"}], items: [{"text": "Has three inputs", "b": 1}, {"text": "Has two inputs", "b": 0}, {"text": "Is built from two half adders and an OR gate", "b": 1}, {"text": "Is built from an XOR gate and an AND gate", "b": 0}, {"text": "Has a carry in", "b": 1}, {"text": "Used for the least significant column only", "b": 0}], done: "A half adder has no carry in. A full adder does." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["XOR", "1 when the inputs are different"], ["NAND", "AND followed by NOT"], ["Half adder", "Sum is A XOR B, carry is A AND B"], ["Full adder", "Adds A, B and a carry in"], ["Ripple carry", "Each carry out feeds the next carry in"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for finding a truth table in order.", items: ["List every combination of the inputs", "Name the output of each gate and add a working column", "Fill the working columns from left to right", "Read the output column(s) from the final gates"], done: "Rows, names, working, outputs." });
Lib.calc($("#c1"), { qs: [
  {"q": "A full adder has A = 1, B = 1 and Cin = 0. What is the sum bit?", "a": 0, "unit": "", "tol": 0.01, "hint": "1 XOR 1 XOR 0.", "sol": "<b>0</b>."},
  {"q": "The same inputs: what is the carry out?", "a": 1, "unit": "", "tol": 0.01, "hint": "Two inputs are 1.", "sol": "<b>1</b>."},
  {"q": "A full adder has A = 1, B = 1 and Cin = 1. What is the sum bit?", "a": 1, "unit": "", "tol": 0.01, "hint": "Three 1s is an odd number.", "sol": "<b>1</b>."},
  {"q": "How many rows does the truth table of a circuit with four inputs have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2 to the power 4.", "sol": "<b>16</b>."},
  {"q": "Adding 0111 and 0001 with a ripple-carry adder: how many columns produce a carry out?", "a": 3, "unit": "", "tol": 0.01, "hint": "Bits 0, 1 and 2 each carry.", "sol": "<b>3</b>: the answer is 1000."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which gate gives 1 for the inputs 0 and 1 but 0 for 1 and 1?", opts: ["OR", "XOR", "NAND", "AND"], a: 1, why: "XOR." },
  { q: "What does the AND gate in a half adder produce?", opts: ["The sum", "The carry", "The inverse of the sum", "The overflow"], a: 1, why: "The carry." },
  { q: "How many inputs does a full adder have?", opts: ["2", "3", "4", "1"], a: 1, why: "A, B and the carry in." },
  { q: "A NOR gate outputs 1 when:", opts: ["Both inputs are 1", "At least one input is 1", "Both inputs are 0", "The inputs differ"], a: 2, why: "NOR is NOT (A OR B)." },
  { q: "In a ripple-carry adder the carry out of one column goes to:", opts: ["The sum output", "The next column's carry in", "Memory", "The same column"], a: 1, why: "It ripples to the next column." },
  { q: "In a truth table, a working column is used for:", opts: ["The final output only", "The output of a gate inside the circuit", "The input labels", "The number of rows"], a: 1, why: "Intermediate gate outputs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["NOT", "Inverts the input."],
  ["AND", "1 only when all inputs are 1."],
  ["OR", "1 when at least one input is 1."],
  ["XOR", "1 when the inputs are different."],
  ["NAND / NOR", "AND / OR followed by NOT."],
  ["Half adder", "Sum = A XOR B, carry = A AND B."],
  ["Full adder", "Sum = A XOR B XOR Cin; carry out when two or more inputs are 1."],
  ["Ripple carry", "Chain of full adders, carry out to carry in."],
] });
