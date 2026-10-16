const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

const X = (q) => 90 + q * 4.6, Y = (p) => 310 - p * 2.7;
function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Price ($)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }); }
function dCurve(d, cls, lab, t) { const a = d >= 0 ? [d, 100] : [0, 100 + d], b = [100 + d, 0]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c1") + SV.text(X(b[0]) + 6, Y(b[1]) - 8, lab || "D", "lbl bd " + (t || "t1")); }
function sCurve(s, cls, lab, t) { const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c2") + SV.text(X(b[0]) + 6, Y(b[1]) + 4, lab || "S", "lbl bd " + (t || "t2")); }
function eq(d, s) { const q = (100 + d + s) / 2, p = q - s; return [q, p]; }
function dsDrop(q, p) { return SV.line(X(0), Y(p), X(q), Y(p), "gr") + SV.line(X(q), Y(p), X(q), Y(0), "gr"); }
function qD(p, d) { return Math.max(0, 100 + d - p); }
function qS(p, s) { return Math.max(0, p + s); }

/* PED curves through (50, 50). kind: 0 inelastic perfectly, 1 inelastic, 2 unitary, 3 elastic, 4 perfectly elastic */
function pedCurve(kind, cls, lab, t) {
  let o = "", lx = 0, ly = 0;
  if (kind === 0) { o = SV.line(X(50), Y(0), X(50), Y(105), cls || "c1"); lx = 50; ly = 100; }
  else if (kind === 4) { o = SV.line(X(0), Y(50), X(110), Y(50), cls || "c1"); lx = 112; ly = 50; }
  else if (kind === 2) { let d = ""; for (let q = 25; q <= 105; q += 2) d += (d ? "L" : "M") + X(q).toFixed(1) + " " + Y(2500 / q).toFixed(1); o = SV.path(d, cls || "c1"); lx = 100; ly = 25; }
  else { const k = kind === 1 ? 3 : 0.35, qa = Math.max(0, 50 - 48 / k), qb = Math.min(108, 50 + 48 / k), pa = 50 - k * (qa - 50), pb = 50 - k * (qb - 50); o = SV.line(X(qa), Y(pa), X(qb), Y(pb), cls || "c1"); lx = qb + 1; ly = pb; }
  return o + SV.text(X(lx) + 6, Y(ly), lab || "D", "lbl bd " + (t || "t1"));
}
function pedLabel(v) { if (v === 0) return "perfectly inelastic"; if (v === Infinity) return "perfectly elastic"; const a = Math.abs(v); return a < 0.99 ? "inelastic" : a > 1.01 ? "elastic" : "unitary"; }

const KN = [["Perfectly inelastic: PED = 0", 0], ["Inelastic: PED between 0 and 1", 1], ["Unitary: PED = 1", 2], ["Elastic: PED greater than 1", 3], ["Perfectly elastic: PED = infinity", 4]];
Lib.stepper($("#stK"), { w: 760, h: 380, label: "Five types of PED", base: { k: 0 }, draw: (s) => axes() + pedCurve(s.k, "c1", "D") + SV.text(X(3), Y(106), KN[s.k][0], "lbl bd t1"), steps: KN.map(([c, k]) => ({ cap: "<b>" + c + "</b>.", s: { k } })) });
const CL2 = ["Find the % change in quantity demanded", "Find the % change in price", "Divide: quantity ÷ price", "Ignore the sign; compare with 1", "Say elastic or inelastic"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Calculating PED", base: { n: 0 }, draw: mkChain(CL2, "--accent"), steps: chainSteps(["Find the <b>% change in quantity</b> demanded.", "Find the <b>% change in price</b>.", "<b>Divide</b>: quantity ÷ price.", "Ignore the sign; <b>compare with 1</b>.", "Say <b>elastic or inelastic</b>."]) });

/* Lab 1: calculator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc") || !$("#pd")) return;
  const p0 = +$("#pa").value, p1 = +$("#pb").value, q0 = +$("#pc").value, q1 = +$("#pd").value, dp = (p1 - p0) / p0 * 100, dq = (q1 - q0) / q0 * 100, ped = dp === 0 ? 0 : dq / dp, a = Math.abs(ped);
  $("#pa1").textContent = money(dp, 1) + "%"; $("#pa2").textContent = money(dq, 1) + "%"; $("#pa3").textContent = money(ped, 2);
  $("#pav").textContent = `Price ${p0} → ${p1} is ${money(dp, 1)}%; quantity ${q0} → ${q1} is ${money(dq, 1)}%. PED = ${money(dq, 1)} ÷ ${money(dp, 1)} = ${money(ped, 2)}. Ignoring the sign, ${money(a, 2)}: demand is ${a === 0 ? "perfectly inelastic" : pedLabel(a)}.`;
  const k = a < 0.01 ? 0 : a < 0.99 ? 1 : a < 1.01 ? 2 : 3;
  $("#labP").innerHTML = axes() + pedCurve(k, "c1", "D") + SV.circle(X(50), Y(50), 6, "dot1");
}
[["g1", "pa", "Old price ($)", 10, 5, 20], ["g2", "pb", "New price ($)", 12, 5, 20], ["g3", "pc", "Old quantity", 100, 20, 200], ["g4", "pd", "New quantity", 70, 0, 200]].forEach(([g, id, l, v, mn, mx]) => Lib.slider($("#" + g), { id, label: l, min: mn, max: mx, step: id === "pa" || id === "pb" ? 1 : 10, value: v, fmt: (x) => x, onInput: labP }));
const TY = [
  { n: "PED = 0", t: "Perfectly inelastic", c: "Vertical curve", e: "Insulin, for a patient who must buy a fixed dose." },
  { n: "0 < PED < 1", t: "Inelastic", c: "Steep curve", e: "Petrol, salt, cigarettes." },
  { n: "PED = 1", t: "Unitary", c: "Curved (hyperbola)", e: "Rare; revenue is unchanged by a price change." },
  { n: "PED > 1", t: "Elastic", c: "Flat curve", e: "Holidays, branded goods." },
  { n: "PED = ∞", t: "Perfectly elastic", c: "Horizontal curve", e: "A firm in perfect competition: any higher price loses all sales." },
];
button_table("tyBtns", "tyOut", TY, 0, (p) => `<div class="tw"><table class="t"><tr><th>Name</th><th>Curve</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.c}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of PED</b> is each value (ignoring the sign)?", buckets: [{ label: "Inelastic (0 to 1)" }, { label: "Unitary (1)" }, { label: "Elastic (above 1)" }], items: [
  { text: "0.3", b: 0 }, { text: "0.8", b: 0 }, { text: "1.0", b: 1 }, { text: "1.5", b: 2 }, { text: "3.2", b: 2 }, { text: "0.5", b: 0 },
], done: "Compare the size with 1." });
Lib.classify($("#cl2"), { prompt: "Which <b>curve shape</b> matches each PED?", buckets: [{ label: "Vertical" }, { label: "Steep" }, { label: "Flat" }, { label: "Horizontal" }], items: [
  { text: "PED = 0", b: 0 }, { text: "PED = 0.4", b: 1 }, { text: "PED = 2.5", b: 2 }, { text: "PED = infinity", b: 3 },
], done: "Steeper means more inelastic." });
Lib.match($("#m1"), { prompt: "Match the term to its PED value.", pairs: [
  ["Perfectly inelastic", "PED = 0"],
  ["Inelastic", "PED between 0 and 1"],
  ["Unitary", "PED = 1"],
  ["Elastic", "PED greater than 1"],
  ["Perfectly elastic", "PED = infinity"],
  ["Formula", "% change in Qd ÷ % change in price"],
], done: "Learn the five." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>calculating PED</b>.", items: [
  "Calculate the % change in quantity demanded",
  "Calculate the % change in price",
  "Divide the first by the second",
  "Ignore the sign",
  "State whether demand is elastic or inelastic",
], done: "Show every step." });
Lib.calc($("#c1"), { qs: [
  { q: "Price rises from $10 to $12 and quantity demanded falls from 100 to 70. Calculate PED (ignore the sign, 1 decimal place).", a: 1.5, sol: "%ΔP = 20%, %ΔQ = −30%. PED = −30 ÷ 20 = <b>−1.5</b>." },
  { q: "Price falls from $50 to $45 and quantity demanded rises from 200 to 210. Calculate PED (ignore the sign).", a: 0.5, sol: "%ΔP = −10%, %ΔQ = +5%. PED = 5 ÷ −10 = <b>−0.5</b>." },
  { q: "Price rises 8% and quantity demanded falls 12%. Calculate PED (ignore the sign).", a: 1.5, sol: "12 ÷ 8 = <b>1.5</b>: elastic." },
  { q: "PED is 0.4 and price rises 10%. By what percentage does quantity demanded fall?", a: 4, sol: "0.4 × 10 = <b>4%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "PED is calculated as:", opts: ["%ΔP ÷ %ΔQd", "%ΔQd ÷ %ΔP", "ΔQ ÷ ΔP", "P ÷ Q"], a: 1, why: "Quantity demanded over price." },
  { q: "A PED of −2 means demand is:", opts: ["Inelastic", "Unitary", "Elastic", "Perfectly inelastic"], a: 2, why: "Size 2 is above 1." },
  { q: "A vertical demand curve shows:", opts: ["Perfectly elastic demand", "Perfectly inelastic demand", "Unitary demand", "Elastic demand"], a: 1, why: "Qd does not change." },
  { q: "A PED of 0.6 means demand is:", opts: ["Elastic", "Inelastic", "Unitary", "Perfectly elastic"], a: 1, why: "Between 0 and 1." },
  { q: "A horizontal demand curve shows:", opts: ["Perfectly inelastic demand", "Perfectly elastic demand", "Unitary demand", "No demand"], a: 1, why: "Infinite response." },
] });

Lib.cards($("#fc1"), { cards: [
  ["PED formula", "% change in quantity demanded ÷ % change in price."],
  ["Perfectly inelastic", "PED = 0: quantity does not change."],
  ["Inelastic", "PED between 0 and 1."],
  ["Unitary", "PED = 1."],
  ["Elastic", "PED above 1."],
  ["Perfectly elastic", "PED = infinity: any rise in price cuts quantity to zero."],
  ["Percentage change", "(New − old) ÷ old × 100."],
  ["Ignoring the sign", "PED is negative for a normal good; we use its size."],
  ["Rectangular hyperbola", "The shape of a unitary elastic demand curve."],
] });
labP(); 
