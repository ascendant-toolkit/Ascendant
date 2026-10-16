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

const G1 = (t) => ({ inputs: t === "NOT" ? ["A"] : ["A", "B"], gates: [{ id: "g1", t, in: t === "NOT" ? ["A"] : ["A", "B"] }], out: "g1" });
const COMBOS = [[0, 0], [0, 1], [1, 0], [1, 1]];
function g1Chart(t) { return function (s) { const a = Math.round(s.a), b = Math.round(s.b), r = circuitSvg(G1(t), { A: a, B: b }); return r.svg; }; }
const stepsFor = (t, name) => COMBOS.map(([a, b], i) => ({ cap: `Inputs <b>A = ${a}</b> and <b>B = ${b}</b>: ${t === "AND" ? (a && b ? "both inputs are 1, so the output is <b>1</b>." : "at least one input is 0, so the output is <b>0</b>.") : (a ^ b ? "the inputs are different, so the output is <b>1</b>." : "the inputs are the same, so the output is <b>0</b>.")}`, s: { a, b } }));
Lib.stepper($("#stA"), { w: 360, h: 130, label: "An AND gate", base: { a: 0, b: 0 }, tween: 1, dwell: 3200, draw: g1Chart("AND"), steps: stepsFor("AND") });
Lib.stepper($("#stB"), { w: 360, h: 130, label: "An XOR gate", base: { a: 0, b: 0 }, tween: 1, dwell: 3200, draw: g1Chart("XOR"), steps: stepsFor("XOR") });
const NANDC = { inputs: ["A", "B"], gates: [{ id: "g1", t: "AND", in: ["A", "B"] }, { id: "g2", t: "NOT", in: ["g1"] }], out: "g2" };
Lib.stepper($("#stC"), { w: 500, h: 130, label: "NAND as AND then NOT", base: { a: 0, b: 0 }, tween: 1, dwell: 3200, draw: (s) => circuitSvg(NANDC, { A: Math.round(s.a), B: Math.round(s.b) }, { names: true, vals: true }).svg, steps: COMBOS.map(([a, b]) => ({ cap: `A = ${a}, B = ${b}. AND gives <b>${a & b}</b>; the NOT inverts it to <b>${1 - (a & b)}</b>. The two gates together make a <b>NAND</b>.`, s: { a, b } })) });

$("#stA").style.maxWidth = $("#stB").style.maxWidth = "460px"; $("#stC").style.maxWidth = "620px";

/* ---------- Lab 1 ---------- */
(() => {
  const sel = $("#gs"); sel.innerHTML = GN.map((g) => `<option>${g}</option>`).join(""); sel.value = "AND"; let T;
  function upd() {
    const t = sel.value, C = G1(t), names = C.inputs; if (!T || T.names !== names.join()) { T = tog($("#gk"), names, upd); T.names = names.join(); }
    const st = T.get(), a = st.A, b = st.B ?? 0, row = names.length === 1 ? a : a * 2 + b;
    $("#gc").innerHTML = circuitEl(C, names.length === 1 ? { A: a } : { A: a, B: b }, { names: true });
    const rows = names.length === 1 ? [[0], [1]] : COMBOS, tb = `<table class="tt"><tr>${names.map((n) => `<th>${n}</th>`).join("")}<th>X</th></tr>` + rows.map((r, i) => { const o = GF[t](...r); return `<tr class="${i === row ? "cur" : ""}">${r.map((v) => `<td>${v}</td>`).join("")}<td class="out ${o ? "one" : "zero"}">${o}</td></tr>`; }).join("") + "</table>"; $("#gtab").innerHTML = tb;
    const o = GF[t](...(names.length === 1 ? [a] : [a, b])); $("#gv").innerHTML = `${t} with ${names.length === 1 ? `A = ${a}` : `A = ${a}, B = ${b}`}: output X = <b>${o}</b>.`;
  }
  sel.onchange = () => { T = null; upd(); }; upd();
})();

/* ---------- Lab 2 ---------- */
chooser($("#sn"), $("#sv"), GN, GN.slice().sort(() => Math.random() - 0.5).map((g) => [`<span class="gsym" data-g="${g}" data-w="110"></span>`, g]));
fillSyms();

/* ---------- Lab 3 ---------- */
chooser($("#sn2"), $("#sv2"), ["AND", "OR", "NAND", "NOR", "XOR"], [["Output: 0 0 0 1", "AND"], ["Output: 0 1 1 1", "OR"], ["Output: 1 1 1 0", "NAND"], ["Output: 1 0 0 0", "NOR"], ["Output: 0 1 1 0", "XOR"]]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which gate does each statement describe?", buckets: [{ label: "NOT" }, { label: "AND" }, { label: "OR" }, { label: "NAND" }, { label: "NOR" }, { label: "XOR" }], items: [
  { text: "The output is the opposite of the single input", b: 0 },
  { text: "Output is 1 only when both inputs are 1", b: 1 },
  { text: "Like two switches in series", b: 1 },
  { text: "Output is 1 when at least one input is 1", b: 2 },
  { text: "Like two switches in parallel", b: 2 },
  { text: "Output is 0 only when both inputs are 1", b: 3 },
  { text: "An AND gate followed by a NOT", b: 3 },
  { text: "Output is 1 only when both inputs are 0", b: 4 },
  { text: "An OR gate followed by a NOT", b: 4 },
  { text: "Output is 1 only when the inputs are different", b: 5 },
  { text: "Exclusive OR", b: 5 },
], done: "Match the behaviour to the gate." });

Lib.match($("#m1"), { prompt: "Match each gate to its output column for A B = 00, 01, 10, 11.", pairs: [
  ["AND", "0 0 0 1"],
  ["OR", "0 1 1 1"],
  ["NAND", "1 1 1 0"],
  ["NOR", "1 0 0 0"],
  ["XOR", "0 1 1 0"]
] });

Lib.calc($("#c1"), { qs: [
  { q: "What is the output of an AND gate with inputs 1 and 0?", a: 0, sol: "Both inputs must be 1, so the output is 0." },
  { q: "What is the output of an OR gate with inputs 1 and 0?", a: 1, sol: "At least one input is 1: output 1." },
  { q: "What is the output of a NAND gate with inputs 1 and 1?", a: 0, sol: "AND gives 1, NOT inverts it: 0." },
  { q: "What is the output of a NOR gate with inputs 0 and 0?", a: 1, sol: "OR gives 0, NOT inverts it: 1." },
  { q: "What is the output of an XOR gate with inputs 1 and 1?", a: 0, sol: "The inputs are the same: 0." },
  { q: "What is the output of a NOT gate with input 1?", a: 0, sol: "NOT inverts: 0." },
  { q: "How many rows does a truth table for two inputs have?", a: 4, sol: "2² = 4." },
  { q: "How many 1s are in the output column of an OR gate (4 rows)?", a: 3, sol: "0 1 1 1 has three 1s." },
  { q: "How many 1s are in the output column of a NOR gate?", a: 1, sol: "1 0 0 0 has one 1." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which gate outputs 1 only when both inputs are 1?", opts: ["AND", "OR", "XOR", "NOR"], a: 0, why: "AND." },
  { q: "What does the bubble on a gate symbol mean?", opts: ["The output is inverted", "The gate is broken", "There are three inputs", "The input is inverted"], a: 0, why: "It means NOT." },
  { q: "Which gate has only one input?", opts: ["NOT", "AND", "NAND", "XOR"], a: 0, why: "NOT." },
  { q: "XOR gives 0 when the inputs are…", opts: ["The same", "Different", "Both 1 only", "Both 0 only"], a: 0, why: "XOR is 1 only when they differ." },
  { q: "What is NAND?", opts: ["AND followed by NOT", "OR followed by NOT", "NOT followed by AND", "Exclusive OR"], a: 0, why: "NOT AND." },
  { q: "A NOR gate outputs 1 when…", opts: ["Both inputs are 0", "Both inputs are 1", "The inputs differ", "Either input is 1"], a: 0, why: "Only 0 and 0 gives 1." },
  { q: "How many input combinations does a two-input gate have?", opts: ["4", "2", "3", "8"], a: 0, why: "2² = 4." },
  { q: "Which gate is like two switches in parallel?", opts: ["OR", "AND", "NOT", "NAND"], a: 0, why: "Either closed switch completes the circuit." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Boolean logic", "Logic using only the values 1 (true) and 0 (false)."],
  ["Logic gate", "An electronic component that takes one or two binary inputs and gives one binary output."],
  ["Truth table", "A table of every combination of inputs and the output for each."],
  ["NOT", "Inverts a single input."],
  ["AND", "Output 1 only if both inputs are 1."],
  ["OR", "Output 1 if at least one input is 1."],
  ["NAND", "NOT AND: output 0 only if both inputs are 1."],
  ["NOR", "NOT OR: output 1 only if both inputs are 0."],
  ["XOR (EOR)", "Exclusive OR: output 1 only if the inputs are different."],
  ["Bubble", "The small circle on a gate output that inverts the signal."]
] });
