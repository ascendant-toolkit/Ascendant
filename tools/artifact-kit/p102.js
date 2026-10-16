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
  E2: { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "OR", in: ["B", "C"] }, { id: "g2", t: "AND", in: ["A", "g1"] }], out: "g2" },
  E3: { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "OR", in: ["A", "B"] }, { id: "g2", t: "AND", in: ["B", "C"] }, { id: "g3", t: "NOT", in: ["g2"] }, { id: "g4", t: "AND", in: ["g1", "g3"] }], out: "g4" },
  Q1: { inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "AND", in: ["A", "B"] }, { id: "g2", t: "OR", in: ["g1", "C"] }], out: "g2" },
  Q5: { name: "L", inputs: ["A", "B", "C"], gates: [{ id: "g1", t: "AND", in: ["B", "C"] }, { id: "g2", t: "OR", in: ["A", "g1"] }], out: "g2" },
};
$$(".ckt[data-c]").forEach((e) => (e.innerHTML = circuitEl(CK[e.dataset.c], null, {})));

/* ---------- 1. build from expression ---------- */
const BS = [new Set([]), new Set(["g1"]), new Set(["g1", "g2"]), new Set(["g1", "g2", "g3"]), new Set(["g1", "g2", "g3"])];
const BH = [null, "g1", "g2", "g3", null];
Lib.stepper($("#stA"), { w: 520, h: 230, label: "Building a circuit for X = (A AND B) OR NOT C", base: { k: 0 }, tween: 1, dwell: 3800, draw: (s) => { const k = Math.round(s.k); return circuitSvg(CK.E1, k === 4 ? { A: 1, B: 1, C: 0 } : null, { show: BS[k], hi: BH[k], names: k >= 1, vals: k === 4 }).svg; }, steps: [
  { cap: "Expression: <b>X = (A AND B) OR NOT C</b>. Three inputs, and three operators, so <b>three gates</b>.", s: { k: 0 } },
  { cap: "Start with the brackets: <b>(A AND B)</b> is an AND gate with inputs A and B.", s: { k: 1 } },
  { cap: "<b>NOT C</b> is a NOT gate on input C. It is a separate gate.", s: { k: 2 } },
  { cap: "The two results are combined by <b>OR</b>. The OR gate's output is X.", s: { k: 3 } },
  { cap: "Check it: with A = 1, B = 1, C = 0: A AND B = 1, NOT C = 1, so 1 OR 1 gives <b>X = 1</b>.", s: { k: 4 } },
] });
$("#stA").style.maxWidth = "720px";

/* ---------- 2. statement to circuit ---------- */
const SH = [new Set([]), new Set(["g1"]), new Set(["g1", "g2"]), new Set(["g1", "g2"])];
Lib.stepper($("#stB"), { w: 520, h: 230, label: "A burglar alarm circuit from a statement", base: { k: 0 }, tween: 1, dwell: 4200, draw: (s) => { const k = Math.round(s.k); return circuitSvg(CK.E2, k === 3 ? { A: 1, B: 0, C: 1 } : null, { show: SH[k], hi: k === 1 ? "g1" : k === 2 ? "g2" : null, names: k >= 1, vals: k === 3 }).svg; }, steps: [
  { cap: "\"The alarm X sounds if the door sensor <b>A</b> is on <b>and</b> <b>either</b> the window sensor <b>B</b> <b>or</b> the motion sensor <b>C</b> is on.\"", s: { k: 0 } },
  { cap: "\"<b>either</b> B <b>or</b> C\" is one part: an <b>OR</b> gate with inputs B and C.", s: { k: 1 } },
  { cap: "\"door sensor <b>and</b> (that part)\" is an <b>AND</b> gate with A and the OR output. Expression: <b>X = A AND (B OR C)</b>.", s: { k: 2 } },
  { cap: "Test: door on (A = 1), window off (B = 0), motion on (C = 1): B OR C = 1, A AND 1 = 1, so the alarm <b>sounds</b>.", s: { k: 3 } },
] });
$("#stB").style.maxWidth = "720px";

/* ---------- Lab 1 ---------- */
(() => {
  const inp = $("#ex"); let T = null, key = "";
  function upd() {
    const r = parseExpr(inp.value);
    if (r.err) { $("#ec").innerHTML = ""; $("#ek").innerHTML = ""; $("#ev").innerHTML = `<span class="flag">Check the expression</span> ${esc(r.err)}`; return; }
    const C = r.C; if (key !== C.inputs.join()) { key = C.inputs.join(); T = tog($("#ek"), C.inputs, upd); }
    const st = T.get(); $("#ec").innerHTML = circuitEl(C, st, { names: true, vals: true }); const V = evalC(C, st);
    $("#ev").innerHTML = `<b>${C.gates.length}</b> gate${C.gates.length > 1 ? "s" : ""}, <b>${C.inputs.length}</b> input${C.inputs.length > 1 ? "s" : ""}. With ${C.inputs.map((n) => `${n} = ${st[n]}`).join(", ")} the output is <b>X = ${V[C.out]}</b>.<br>${ttHTML(C, { work: true })}`;
  }
  inp.addEventListener("input", () => { key = ""; upd(); }); upd();
})();

/* ---------- Lab 2 ---------- */
Lib.quiz($("#qx"), { qs: [
  { q: "A heater H is on if the temperature is low (T) <b>and</b> it is <b>not</b> daytime (D).", opts: ["H = T AND NOT D", "H = NOT T AND D", "H = T OR NOT D", "H = NOT (T AND D)"], a: 0, why: "Both conditions: T and NOT D." },
  { q: "A light L comes on if <b>either</b> switch A <b>or</b> switch B is on.", opts: ["L = A AND B", "L = A OR B", "L = NOT A", "L = A XOR B"], a: 1, why: "Either one (or both) is OR." },
  { q: "An alarm X sounds if door A is open <b>and</b> <b>either</b> B <b>or</b> C is on.", opts: ["X = (A AND B) OR C", "X = A AND (B OR C)", "X = A OR (B AND C)", "X = A AND B AND C"], a: 1, why: "The \"either...or\" is bracketed, then ANDed with A." },
  { q: "A machine stops (S) if <b>neither</b> sensor A <b>nor</b> sensor B is on.", opts: ["S = NOT (A OR B)", "S = A AND B", "S = NOT A OR NOT B", "S = A XOR B"], a: 0, why: "Neither...nor is NOT (A OR B), which is a NOR." },
  { q: "A door D opens if switch A <b>or</b> switch B is pressed, <b>but not both</b>.", opts: ["D = A OR B", "D = A AND B", "D = A XOR B", "D = NOT (A OR B)"], a: 2, why: "One or the other but not both is XOR." },
] });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which gate do the words in each statement suggest?", buckets: [{ label: "AND" }, { label: "OR" }, { label: "NOT" }, { label: "NOR" }, { label: "NAND" }, { label: "XOR" }], items: [
  { text: "both the key and the card are used", b: 0 },
  { text: "both inputs must be on", b: 0 },
  { text: "either the front or the back sensor", b: 1 },
  { text: "at least one switch is on", b: 1 },
  { text: "the machine is not running", b: 2 },
  { text: "the lid is not closed", b: 2 },
  { text: "neither sensor is triggered", b: 3 },
  { text: "not both buttons are pressed together", b: 4 },
  { text: "one switch or the other, but not both", b: 5 },
  { text: "exactly one input is on", b: 5 },
], done: "Match the key words to the gate." });

Lib.match($("#m1"), { prompt: "Match each statement to its expression.", pairs: [
  ["A and B are both on", "A AND B"],
  ["A or B is on", "A OR B"],
  ["A is not on", "NOT A"],
  ["A is on and either B or C is on", "A AND (B OR C)"],
  ["A is on or both B and C are on", "A OR (B AND C)"],
  ["A or B, but not both", "A XOR B"]
] });

Lib.order($("#o1"), { prompt: "Put the steps of drawing a circuit from an expression in order.", items: [
  "Read the expression and find each operator",
  "Draw the gates inside the brackets first",
  "Draw the remaining gates, left to right",
  "Join each gate's output to the next gate's input",
  "Label the inputs and the output X"
], done: "Find, brackets, remaining, wires, labels." });

Lib.calc($("#c1"), { qs: [
  { q: "How many gates are needed for X = (A AND B) OR NOT C?", a: 3, sol: "AND, NOT and OR: 3." },
  { q: "How many gates are needed for X = A AND (B OR C)?", a: 2, sol: "OR and AND: 2." },
  { q: "How many gates are needed for X = NOT (A AND B)?", a: 2, sol: "AND and NOT: 2 (or one NAND).", hint: "Draw it as written: AND then NOT." },
  { q: "For X = A AND (B OR C), A = 1, B = 0, C = 1: what is X?", a: 1, sol: "B OR C = 1; 1 AND 1 = 1." },
  { q: "For X = (A AND B) OR NOT C, A = 0, B = 1, C = 1: what is X?", a: 0, sol: "0 OR 0 = 0." },
  { q: "For X = NOT (A OR B), A = 0, B = 0: what is X?", a: 1, sol: "A OR B = 0; NOT 0 = 1." },
  { q: "What is the maximum number of inputs to the circuits in this course?", a: 3, sol: "Up to three inputs, one output." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does one NOT in an expression need in a circuit?", opts: ["One NOT gate", "No gate", "Two gates", "A wire only"], a: 0, why: "Every NOT is its own gate." },
  { q: "Which expression needs the OR gate drawn first?", opts: ["A AND (B OR C)", "(A AND B) OR C", "A AND B", "NOT A"], a: 0, why: "The bracket is drawn first." },
  { q: "Which words suggest AND?", opts: ["Both ... and", "Either ... or", "Not", "Neither"], a: 0, why: "AND needs both." },
  { q: "Which words suggest NOR?", opts: ["Neither ... nor", "Both", "Either", "But not both"], a: 0, why: "Neither...nor is NOR." },
  { q: "How many outputs does the circuit have in this course?", opts: ["One", "Two", "Three", "Four"], a: 0, why: "One output, X." },
  { q: "Should you simplify the circuit?", opts: ["No, draw it as the statement is written", "Always", "Only with NOT", "Only with OR"], a: 0, why: "Circuits are drawn without simplification." },
  { q: "Where are the inputs normally drawn?", opts: ["On the left", "On the right", "Above", "Below"], a: 0, why: "Inputs left, output right." },
  { q: "A circuit for X = A OR B has how many gates?", opts: ["1", "2", "3", "0"], a: 0, why: "A single OR gate." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Logic circuit", "A set of logic gates joined so that outputs feed other gates' inputs."],
  ["Logic expression", "A way of writing a circuit using AND, OR, NOT and so on, such as X = A AND (B OR C)."],
  ["Input", "A signal fed into a circuit (A, B or C)."],
  ["Output", "The result of a circuit (X)."],
  ["Brackets", "In an expression they show which gate is worked out first."],
  ["Problem statement", "A description in words of when an output should be 1."],
  ["Trace", "Follow signals through a circuit gate by gate to find its output."]
] });
