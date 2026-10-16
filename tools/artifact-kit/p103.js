const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}

const GN = ["NOT", "AND", "OR", "NAND", "NOR", "XOR"];
const GF = { NOT: (a) => 1 - a, AND: (a, b) => a & b, OR: (a, b) => a | b, NAND: (a, b) => 1 - (a & b), NOR: (a, b) => 1 - (a | b), XOR: (a, b) => a ^ b };
const GP = { AND: "M0 0 H25 A25 20 0 0 1 25 40 H0 Z", OR: "M0 0 Q28 0 50 20 Q28 40 0 40 Q12 20 0 0 Z", NOT: "M0 0 L40 20 L0 40 Z" };
function shape(t, x, y, col, fillc) {
  const st = `fill:${fillc || "var(--surface)"};stroke:${col};stroke-width:2.5`, base = { NAND: "AND", NOR: "OR", XOR: "OR" }[t] || t; let o = `<path d="${GP[base]}" transform="translate(${x} ${y})" style="${st}"/>`;
  if (t === "XOR") o += `<path d="M-8 0 Q4 20 -8 40" transform="translate(${x} ${y})" style="fill:none;stroke:${col};stroke-width:2.5"/>`;
  if (t === "NOT") o += `<circle cx="${x + 45}" cy="${y + 20}" r="5" style="${st}"/>`;
  if (t === "NAND" || t === "NOR") o += `<circle cx="${x + 55}" cy="${y + 20}" r="5" style="${st}"/>`;
  return o;
}
const gateEnd = (t) => (t === "NAND" || t === "NOR" ? 60 : 50);
function gateSym(t, w) { const two = t !== "NOT", e = gateEnd(t), c = "currentColor"; return `<svg viewBox="-14 -4 100 48" width="${w || 86}" role="img" aria-label="${t} gate" style="color:var(--ink)">` + (two ? `<line x1="-12" y1="10" x2="2" y2="10" stroke="${c}" stroke-width="2.5"/><line x1="-12" y1="30" x2="2" y2="30" stroke="${c}" stroke-width="2.5"/>` : `<line x1="-12" y1="20" x2="0" y2="20" stroke="${c}" stroke-width="2.5"/>`) + shape(t, 0, 0, c) + `<line x1="${e}" y1="20" x2="${e + 20}" y2="20" stroke="${c}" stroke-width="2.5"/></svg>`; }
const fillSyms = (root) => $$(".gsym", root || document).forEach((e) => { if (!e.innerHTML) e.innerHTML = gateSym(e.dataset.g, +e.dataset.w || 0); });
function evalC(C, a) { const v = { ...a }; C.gates.forEach((g) => { v[g.id] = GF[g.t](...g.in.map((r) => v[r])); }); return v; }
function lay(C) {
  const dep = {}, ys = {}; C.inputs.forEach((n, i) => { dep[n] = 0; ys[n] = 40 + i * 70; }); C.gates.forEach((g) => (dep[g.id] = 1 + Math.max(...g.in.map((r) => dep[r]))));
  const maxD = Math.max(1, ...C.gates.map((g) => dep[g.id]));
  for (let d = 1; d <= maxD; d++) { const gs = C.gates.filter((g) => dep[g.id] === d); gs.forEach((g) => (ys[g.id] = g.in.reduce((a, r) => a + ys[r], 0) / g.in.length)); gs.sort((a, b) => ys[a.id] - ys[b.id]); for (let i = 1; i < gs.length; i++) if (ys[gs[i].id] - ys[gs[i - 1].id] < 60) ys[gs[i].id] = ys[gs[i - 1].id] + 60; }
  return { dep, ys, maxD };
}
function circuitSvg(C, assign, o = {}) {
  const L = lay(C), V = assign ? evalC(C, assign) : null, show = o.show || null, gx = (g) => 110 + (L.dep[g.id] - 1) * 130, col = (r) => (V ? (V[r] ? "var(--good)" : "var(--muted)") : "var(--muted)"), sw = (r) => (V && V[r] ? 4 : 2.5);
  const vis = (g) => !show || show.has(g.id), src = (r) => (C.inputs.includes(r) ? [60, L.ys[r]] : [gx(C.gates.find((g) => g.id === r)) + 60, L.ys[r]]);
  let wires = "", shapes = "";
  const maxY = Math.max(...Object.values(L.ys)) + 50, W = 110 + L.maxD * 130 + 70;
  C.inputs.forEach((n) => { shapes += SV.text(24, L.ys[n] + 5, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); if (V) shapes += SV.text(46, L.ys[n] - 8, V[n], "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:12px;fill:${V[n] ? "var(--good)" : "var(--muted)"}` }); wires += SV.line(38, L.ys[n], 60, L.ys[n], "", { style: `stroke:${col(n)};stroke-width:${sw(n)}` }); });
  C.gates.forEach((g) => {
    if (!vis(g)) return; const x = gx(g), cy = L.ys[g.id], y = cy - 20, hi = o.hi === g.id;
    g.in.forEach((r, k) => { const s = src(r), dy = cy + (g.in.length === 1 ? 0 : k ? 10 : -10), mx = x - (k ? 14 : 30); wires += SV.path(`M${s[0]} ${s[1]} L${mx} ${s[1]} L${mx} ${dy} L${x} ${dy}`, "", { style: `fill:none;stroke:${col(r)};stroke-width:${sw(r)};stroke-linejoin:round` }); });
    wires += SV.line(x + gateEnd(g.t), cy, x + 60, cy, "", { style: `stroke:${col(g.id)};stroke-width:${sw(g.id)}` });
    shapes += shape(g.t, x, y, hi ? "var(--accent)" : "var(--ink)", hi ? "var(--accent-soft)" : null);
    if (o.names) shapes += SV.text(x + 28, y - 6, g.t, "sm", { "text-anchor": "middle" });
    if (o.vals && V) shapes += SV.text(x + 66, cy - 7, V[g.id], "lbl bd", { "text-anchor": "start", style: `font-family:var(--mono);font-size:12px;fill:${V[g.id] ? "var(--good)" : "var(--muted)"}` });
  });
  const og = C.gates.find((g) => g.id === C.out);
  if (og && vis(og)) { const x = gx(og) + 60, cy = L.ys[og.id]; wires += SV.line(x, cy, x + 36, cy, "", { style: `stroke:${col(og.id)};stroke-width:${sw(og.id)}` }); shapes += SV.text(x + 52, cy + 6, (C.name || "X") + (V ? " = " + V[og.id] : ""), "lbl bd", { "text-anchor": "start", style: `font-size:16px;fill:${V ? (V[og.id] ? "var(--good)" : "var(--muted)") : "var(--ink)"}` }); }
  return { svg: wires + shapes, w: W + (V ? 50 : 20), h: maxY };
}
const circuitEl = (C, assign, o) => { const r = circuitSvg(C, assign, o); return `<svg viewBox="0 0 ${r.w} ${r.h}" style="width:100%;max-width:${Math.max(Math.round(r.w * 1.35), 380)}px;height:auto" role="img" aria-label="Logic circuit">${r.svg}</svg>`; };
function exprOf(C, ref, top = true) {
  if (C.inputs.includes(ref)) return ref; const g = C.gates.find((x) => x.id === ref);
  const sub = (r) => { const s = exprOf(C, r, false), gg = C.gates.find((x) => x.id === r); return gg && gg.t !== "NOT" ? "(" + s + ")" : s; };
  if (g.t === "NOT") { const c = C.gates.find((x) => x.id === g.in[0]); return c && c.t !== "NOT" ? `NOT (${exprOf(C, g.in[0], true)})` : `NOT ${sub(g.in[0])}`; }
  return `${sub(g.in[0])} ${g.t} ${sub(g.in[1])}`;
}
const binRows = (n) => Array.from({ length: 1 << n }, (_, i) => Array.from({ length: n }, (_, k) => (i >> (n - 1 - k)) & 1));
function ttHTML(C, o = {}) {
  const rows = binRows(C.inputs.length), work = o.work !== false ? C.gates.filter((g) => g.id !== C.out) : [], cur = o.cur;
  let h = `<table class="tt"><tr>${C.inputs.map((n) => `<th>${n}</th>`).join("")}${work.map((g) => `<th>${exprOf(C, g.id)}</th>`).join("")}<th>${C.name || "X"}</th></tr>`;
  rows.forEach((r, i) => { const a = Object.fromEntries(C.inputs.map((n, k) => [n, r[k]])), V = evalC(C, a), c = (v) => `<td class="${v ? "one" : "zero"}">${v}</td>`; h += `<tr class="${cur === i ? "cur" : ""}">${r.map((v) => `<td>${v}</td>`).join("")}${work.map((g) => c(V[g.id])).join("")}<td class="out ${V[C.out] ? "one" : "zero"}">${V[C.out]}</td></tr>`; });
  return h + "</table>";
}
function parseExpr(src) {
  const toks = src.toUpperCase().match(/[A-Z]+|\(|\)/g) || [], KW = ["AND", "OR", "NOT", "NAND", "NOR", "XOR"]; let p = 0; const gates = [], vars = new Set(); let n = 0;
  const peek = () => toks[p], mk = (t, ins) => { const id = "g" + ++n; gates.push({ id, t, in: ins }); return id; };
  const prim = () => { const t = toks[p++]; if (t === undefined) throw new Error("The expression ends too early."); if (t === "(") { const r = orE(); if (toks[p++] !== ")") throw new Error("A bracket is not closed."); return r; } if (t === "NOT") return mk("NOT", [prim()]); if (KW.includes(t) || t === ")") throw new Error(`Unexpected "${t}".`); if (t.length > 1) throw new Error(`"${t}" is not an input. Use single letters such as A, B, C.`); vars.add(t); return t; };
  const andE = () => { let l = prim(); while (peek() === "AND" || peek() === "NAND") { const t = toks[p++]; l = mk(t, [l, prim()]); } return l; };
  const xorE = () => { let l = andE(); while (peek() === "XOR") { p++; l = mk("XOR", [l, andE()]); } return l; };
  const orE = () => { let l = xorE(); while (peek() === "OR" || peek() === "NOR") { const t = toks[p++]; l = mk(t, [l, xorE()]); } return l; };
  try { if (!toks.length) throw new Error("Type an expression."); const r = orE(); if (p < toks.length) throw new Error(`Unexpected "${toks[p]}".`); if (!gates.length) throw new Error("Use at least one gate."); const inputs = [...vars].sort(); if (inputs.length > 3) throw new Error("Use at most three inputs."); if (gates.length > 9) throw new Error("That needs too many gates for this page."); return { C: { inputs, gates, out: r } }; } catch (e) { return { err: e.message }; }
}
const tog = (el, names, cb) => { const st = Object.fromEntries(names.map((n) => [n, 0])); el.innerHTML = names.map((n) => `<span class="tog"><b>${n}</b> <button type="button" class="b" data-n="${n}">0</button></span>`).join(""); $$("button", el).forEach((b) => (b.onclick = () => { st[b.dataset.n] ^= 1; b.textContent = st[b.dataset.n]; b.classList.toggle("pri", !!st[b.dataset.n]); cb(st); })); return { get: () => ({ ...st }), set: (k, v) => { st[k] = v; $$("button", el).forEach((b) => { b.textContent = st[b.dataset.n]; b.classList.toggle("pri", !!st[b.dataset.n]); }); } }; };
document.addEventListener("DOMContentLoaded", () => fillSyms());

const CK = {
  E1: { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "AND", in: ["A", "B"] }, { id: "g2", t: "NOT", in: ["C"] }, { id: "g3", t: "OR", in: ["g1", "g2"] }], out: "g3" },
  E3: { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "OR", in: ["A", "B"] }, { id: "g2", t: "AND", in: ["B", "C"] }, { id: "g3", t: "NOT", in: ["g2"] }, { id: "g4", t: "AND", in: ["g1", "g3"] }], out: "g4" },
  E4: { inputs: ["A", "B"], gates: [{ id: "g1", t: "NOT", in: ["B"] }, { id: "g2", t: "NOT", in: ["A"] }, { id: "g3", t: "AND", in: ["A", "g1"] }, { id: "g4", t: "AND", in: ["g2", "B"] }, { id: "g5", t: "OR", in: ["g3", "g4"] }], out: "g5" },
};
$$(".ckt[data-c]").forEach((e) => (e.innerHTML = circuitEl(CK[e.dataset.c], null, {})));
$$(".ttw[data-c]").forEach((e) => (e.innerHTML = ttHTML(CK[e.dataset.c])));

/* ---------- 1. column by column ---------- */
function tsvg(C, ncols, hiRows, terms, foot) {
  const rows = binRows(C.inputs.length), work = C.gates.filter((g) => g.id !== C.out), cols = [...C.inputs.map((n) => ({ h: n, f: (a) => a[n] })), ...work.map((g) => ({ h: exprOf(C, g.id), f: (a, V) => V[g.id] })), { h: "X", f: (a, V) => V[C.out] }];
  const cw = cols.map((c, i) => (i < C.inputs.length ? 50 : c.h.length * 8 + 40)); let x = 30; const xs = cw.map((w) => { const r = x; x += w; return r; });
  let s = ""; cols.forEach((c, i) => { if (i >= ncols) return; s += SV.rect(xs[i], 8, cw[i] - 4, 28, "", { rx: 5, style: "fill:var(--soft)" }) + SV.text(xs[i] + cw[i] / 2 - 2, 27, c.h, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" }); });
  rows.forEach((r, ri) => { const a = Object.fromEntries(C.inputs.map((n, k) => [n, r[k]])), V = evalC(C, a), y = 44 + ri * 26; if (hiRows && hiRows.includes(ri)) s += SV.rect(26, y - 2, x - 26, 24, "", { rx: 5, style: "fill:var(--warn-soft)" });
    cols.forEach((c, i) => { if (i >= ncols) return; const v = c.f(a, V); s += SV.text(xs[i] + cw[i] / 2 - 2, y + 16, v, "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:14px;fill:${i >= C.inputs.length ? (v ? "var(--good)" : "var(--muted)") : "var(--ink)"}` }); });
    if (terms && terms[ri]) s += SV.text(x + 6, y + 16, terms[ri], "lbl bd t3", { "text-anchor": "start", style: "font-family:var(--mono);font-size:12px" }); });
  if (foot) s += SV.text(30, 44 + rows.length * 26 + 26, foot, "lbl bd t1", { "text-anchor": "start", style: "font-family:var(--mono);font-size:12px" });
  return s;
}
const nIn = CK.E1.inputs.length;
Lib.stepper($("#stA"), { w: 520, h: 270, label: "Completing a truth table column by column", base: { k: 0 }, tween: 1, dwell: 3600, draw: (s) => tsvg(CK.E1, nIn + Math.round(s.k), null, null, null), steps: [
  { cap: "<b>X = (A AND B) OR NOT C</b>. List all <b>8</b> input combinations in binary order.", s: { k: 0 } },
  { cap: "Working column 1: <b>A AND B</b> is 1 only when A and B are both 1 (rows 110 and 111).", s: { k: 1 } },
  { cap: "Working column 2: <b>NOT C</b> is the opposite of C, so it is 1 when C is 0.", s: { k: 2 } },
  { cap: "Output <b>X</b>: OR the two working columns. X is 1 when either is 1, so it is 0 only for rows 001, 011 and 101.", s: { k: 3 } },
] });
$("#stA").style.maxWidth = "720px";

/* ---------- 2. table to expression ---------- */
const AC = { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "OR", in: ["B", "C"] }, { id: "g2", t: "AND", in: ["A", "g1"] }], out: "g2" };
const TERMS = { 5: "A AND NOT B AND C", 6: "A AND B AND NOT C", 7: "A AND B AND C" };
Lib.stepper($("#stB"), { w: 640, h: 290, label: "Writing an expression from a truth table", base: { k: 0 }, tween: 1, dwell: 4000, draw: (s) => { const k = Math.round(s.k); return tsvg(AC, 5, k >= 1 ? [5, 6, 7] : null, k >= 2 ? TERMS : null, k >= 3 ? "X = (A AND NOT B AND C) OR (A AND B AND NOT C) OR (A AND B AND C)" : null); }, steps: [
  { cap: "A truth table with output X. Which rows have <b>X = 1</b>?", s: { k: 0 } },
  { cap: "The output is 1 in rows <b>101, 110 and 111</b>. Only these rows matter.", s: { k: 1 } },
  { cap: "For each of these rows, AND the inputs together: write the name where the input is <b>1</b> and <b>NOT</b> where it is <b>0</b>.", s: { k: 2 } },
  { cap: "OR the terms: <b>X = (A AND NOT B AND C) OR (A AND B AND NOT C) OR (A AND B AND C)</b>. This simplifies to A AND (B OR C), but you do not have to simplify.", s: { k: 3 } },
] });
$("#stB").style.maxWidth = "820px";

/* ---------- Lab 1 ---------- */
const PRE = ["(A AND B) OR NOT C", "A AND (B OR C)", "NOT (A AND B)", "(A OR B) AND NOT C", "A XOR B", "NOT A OR B", "(A AND NOT B) OR (NOT A AND B)", "NOT (A OR B)"];
(() => {
  const sel = $("#tp"), inp = $("#ti"); sel.innerHTML = `<option value="">Choose a preset…</option>` + PRE.map((p) => `<option>${p}</option>`).join("");
  function upd() { const r = parseExpr(inp.value); if (r.err) { $("#tout").innerHTML = ""; $("#tv").innerHTML = `<span class="flag">Check the expression</span> ${esc(r.err)}`; return; } const C = r.C; $("#tout").innerHTML = ttHTML(C); const ones = binRows(C.inputs.length).filter((row) => evalC(C, Object.fromEntries(C.inputs.map((n, k) => [n, row[k]])))[C.out]).length; $("#tv").innerHTML = `<b>${1 << C.inputs.length}</b> rows, <b>${C.gates.length}</b> gates, so <b>${C.gates.length - 1}</b> working column${C.gates.length === 2 ? "" : "s"}. The output is 1 in <b>${ones}</b> row${ones === 1 ? "" : "s"}.`; }
  sel.onchange = () => { if (sel.value) { inp.value = sel.value; upd(); } }; inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const sel = $("#cp"); sel.innerHTML = PRE.map((p, i) => `<option value="${i}">X = ${p}</option>`).join(""); let C, ans, user;
  function load() { C = parseExpr(PRE[+sel.value]).C; ans = binRows(C.inputs.length).map((row) => evalC(C, Object.fromEntries(C.inputs.map((n, k) => [n, row[k]])))[C.out]); user = ans.map(() => ""); $("#cck").innerHTML = circuitEl(C, null, {}); draw(); $("#cv").textContent = "Click the Output cells to fill them in."; }
  function draw(chk) {
    const rows = binRows(C.inputs.length), work = C.gates.filter((g) => g.id !== C.out);
    $("#ctab").innerHTML = `<table class="tt"><tr>${C.inputs.map((n) => `<th>${n}</th>`).join("")}${work.map((g) => `<th>${exprOf(C, g.id)}</th>`).join("")}<th>X</th></tr>` + rows.map((r, i) => { const V = evalC(C, Object.fromEntries(C.inputs.map((n, k) => [n, r[k]]))); return `<tr>${r.map((v) => `<td>${v}</td>`).join("")}${work.map((g) => `<td class="${V[g.id] ? "one" : "zero"}">${V[g.id]}</td>`).join("")}<td class="pick out" data-i="${i}" style="min-width:44px;${chk ? (user[i] === ans[i] ? "background:var(--good-soft)" : "background:var(--bad-soft)") : ""}">${user[i]}</td></tr>`; }).join("") + "</table>";
    $$(".pick", $("#ctab")).forEach((c) => (c.onclick = () => { const i = +c.dataset.i; user[i] = user[i] === "" ? 0 : user[i] === 0 ? 1 : ""; draw(); }));
  }
  $("#cc").onclick = () => { const ok = user.filter((v, i) => v === ans[i]).length; draw(true); $("#cv").innerHTML = ok === ans.length ? `<span class="okf">All correct</span> every output is right.` : `${ok} of ${ans.length} correct. Red cells are wrong or empty.`; };
  $("#cr").onclick = () => { user = [...ans]; draw(true); $("#cv").textContent = "The correct outputs are shown."; }; $("#cn").onclick = () => { user = ans.map(() => ""); draw(); $("#cv").textContent = ""; };
  sel.onchange = load; load();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let n = 2, out = [0, 1, 1, 0]; const GATES2 = { "0001": "AND", "0111": "OR", "1110": "NAND", "1000": "NOR", "0110": "XOR" };
  function draw() {
    const names = ["A", "B", "C"].slice(0, n), rows = binRows(n);
    $("#btab").innerHTML = `<table class="tt"><tr>${names.map((x) => `<th>${x}</th>`).join("")}<th>X</th></tr>` + rows.map((r, i) => `<tr>${r.map((v) => `<td>${v}</td>`).join("")}<td class="pick out ${out[i] ? "one" : "zero"}" data-i="${i}" style="min-width:44px">${out[i]}</td></tr>`).join("") + "</table>";
    $$(".pick", $("#btab")).forEach((c) => (c.onclick = () => { out[+c.dataset.i] ^= 1; draw(); }));
    const ones = rows.filter((_, i) => out[i]), key = out.join("");
    $("#bck").innerHTML = "";
    if (!ones.length) { $("#bv").innerHTML = "The output is <b>0 in every row</b>, so there is no AND term to write: X is always 0."; return; }
    if (ones.length === rows.length) { $("#bv").innerHTML = "The output is <b>1 in every row</b>: X is always 1, whatever the inputs."; return; }
    const terms = ones.map((r) => r.map((v, k) => (v ? names[k] : "NOT " + names[k])).join(" AND ")), expr = terms.map((t) => (ones.length > 1 ? `(${t})` : t)).join(" OR ");
    let msg = `<b>Rows where X = 1:</b> ${ones.map((r) => r.join("")).join(", ")}.<br><b>AND terms:</b> ${terms.map((t) => `<span class="ln2">${t}</span>`).join("; ")}<br><b>Expression:</b> <span class="ln2">X = ${expr}</span>`;
    if (n === 2 && GATES2[key]) msg += `<br><span class="okf">Known pattern</span> The output column ${out.join(" ")} is a single <b>${GATES2[key]}</b> gate.`;
    $("#bv").innerHTML = msg; const r = parseExpr(expr); if (r.C) $("#bck").innerHTML = circuitEl(r.C, null, {}); else $("#bck").innerHTML = `<p class="note">${esc(r.err)} This circuit is too big to draw here, but the expression is correct.</p>`;
  }
  $("#bn").onchange = (e) => { n = +e.target.value; out = n === 2 ? [0, 1, 1, 0] : [0, 0, 0, 0, 0, 1, 1, 1]; draw(); }; $("#bz").onclick = () => { out = out.map(() => 0); draw(); }; draw();
})();

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each expression to its output column for the rows A B C = 000, 001, 010, 011, 100, 101, 110, 111.", pairs: [
  ["A AND (B OR C)", "0 0 0 0 0 1 1 1"],
  ["(A AND B) OR C", "0 1 0 1 0 1 1 1"],
  ["A AND B AND C", "0 0 0 0 0 0 0 1"],
  ["NOT A", "1 1 1 1 0 0 0 0"],
  ["A OR B OR C", "0 1 1 1 1 1 1 1"],
  ["(A AND B) OR NOT C", "1 0 1 0 1 0 1 1"]
] });

Lib.order($("#o1"), { prompt: "Put the steps of completing a truth table from a circuit in order.", items: [
  "List every combination of the inputs in binary order",
  "Add a working column for each gate",
  "Fill each working column, left to right through the circuit",
  "Fill the output column from the final gate",
  "Check the number of rows is 2 to the power of the inputs"
], done: "Inputs, working columns, fill, output, check." });

Lib.order($("#o2"), { prompt: "Put the steps of writing an expression from a truth table in order.", items: [
  "Find the rows where the output is 1",
  "For each row, write an AND term using every input",
  "Write NOT in front of any input that is 0 in that row",
  "OR all the terms together",
  "Check the expression against the table"
], done: "Find, AND term, NOT zeros, OR, check." });

Lib.calc($("#c1"), { qs: [
  { q: "How many rows are in a truth table for three inputs?", a: 8, sol: "2³ = 8." },
  { q: "For X = A AND (B OR C), how many rows give X = 1?", a: 3, sol: "Rows 101, 110 and 111." },
  { q: "For X = (A AND B) OR NOT C, how many rows give X = 1?", a: 5, sol: "Rows 000, 010, 100, 110, 111.", hint: "Count the 1s in 1 0 1 0 1 0 1 1." },
  { q: "For X = A XOR B, how many rows give X = 1?", a: 2, sol: "Rows 01 and 10." },
  { q: "For X = NOT (A OR B), what is X when A = 0 and B = 0?", a: 1, sol: "A OR B = 0, so X = 1." },
  { q: "For X = A AND NOT B, what is X when A = 1 and B = 1?", a: 0, sol: "NOT B = 0, so X = 0." },
  { q: "How many AND terms are needed to write X = 1 for rows 011, 101 and 111?", a: 3, sol: "One AND term for each row with output 1." },
  { q: "How many working columns does X = (A OR B) AND NOT C need? (one per gate except the output gate)", a: 2, sol: "OR and NOT: 2 working columns." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "How many rows does a two-input truth table have?", opts: ["4", "2", "3", "8"], a: 0, why: "2² = 4." },
  { q: "In which order are rows listed?", opts: ["Binary counting order", "Any order", "Reverse order only", "Alphabetical"], a: 0, why: "000, 001, 010 ..." },
  { q: "Which rows are used to write an expression?", opts: ["Rows where the output is 1", "Rows where the output is 0", "All rows", "The last row only"], a: 0, why: "Rows with X = 1." },
  { q: "How are inputs written in a row's AND term?", opts: ["Name if 1, NOT name if 0", "Name if 0, NOT name if 1", "Always the name", "Always NOT"], a: 0, why: "NOT is used for inputs that are 0." },
  { q: "An output column 0 1 1 0 is which gate?", opts: ["XOR", "OR", "AND", "NOR"], a: 0, why: "Exactly one input is 1." },
  { q: "What joins the AND terms together?", opts: ["OR", "AND", "XOR", "NOT"], a: 0, why: "OR the terms." },
  { q: "What is a working column?", opts: ["The result of one gate, for checking", "The output", "An input", "A comment"], a: 0, why: "It shows an intermediate result." },
  { q: "Must you simplify the expression?", opts: ["No, unless asked", "Always", "Only for 3 inputs", "Only with NOT"], a: 0, why: "Unsimplified answers are accepted." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Truth table", "A table showing the output for every combination of inputs."],
  ["Working column", "A column holding the output of one gate, to help complete a truth table."],
  ["Binary counting order", "Listing input combinations as 000, 001, 010 and so on."],
  ["AND term", "The inputs of one row ANDed together, with NOT for inputs that are 0."],
  ["Sum of products", "Writing an expression by ORing the AND terms of the rows where the output is 1."],
  ["Logic expression", "A circuit or table written in AND, OR and NOT, such as X = (A AND B) OR NOT C."],
  ["Simplify", "Rewriting an expression in a shorter equivalent form; not required in this course."]
] });
