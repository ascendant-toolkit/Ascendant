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

const DX = (q) => 90 + q * 4.6, DYP = (p) => 310 - p * 2.7;
function dAxes() { return SV.line(DX(0), DYP(0), DX(0), DYP(108)) + SV.line(DX(0), DYP(0), DX(135), DYP(0)) + SV.text(DX(0) + 8, 14, "Price ($)", "sm") + SV.text(DX(135), DYP(0) + 24, "Quantity demanded", "sm", { "text-anchor": "end" }); }
function dLine(s, cls, lab, tcls) {
  const q0 = Math.max(0, s), p0 = Math.min(100, 100 + s), pEnd = 100 - Math.max(0, 130 - s - 100) * 0, x1 = 100 + s;
  const a = s >= 0 ? [s, 100] : [0, 100 + s], b = [100 + s, 0];
  return SV.line(DX(a[0]), DYP(a[1]), DX(b[0]), DYP(b[1]), cls || "c1") + SV.text(DX(b[0]) + 6, DYP(b[1]) - 8, lab || "D", "lbl bd " + (tcls || "t1"));
}
function dDrop(q, p) { return SV.line(DX(0), DYP(p), DX(q), DYP(p), "gr") + SV.line(DX(q), DYP(p), DX(q), DYP(0), "gr"); }
function dDot(q, p, lab, cl, side) { return SV.circle(DX(q), DYP(p), 7, cl || "dot1") + SV.text(DX(q) + (side === "l" ? -12 : 12), DYP(p) + 4, lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }

Lib.stepper($("#stX"), { w: 760, h: 380, label: "Extension and contraction", base: { n: 0 }, draw: (s) => {
  let o = dAxes() + dLine(0, "c1", "D");
  const pts = [[40, 60], [70, 30], [20, 80]];
  o += dDrop(40, 60) + dDot(40, 60, "A", "dot1", "r");
  if (s.n === 1) o += dDrop(70, 30) + dDot(70, 30, "B", "dot2", "r") + SV.line(DX(40), DYP(60), DX(70), DYP(30), "c3") + SV.text(DX(0) - 8, DYP(30), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(DX(70), DYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  if (s.n === 2) o += dDrop(20, 80) + dDot(20, 80, "C", "dot4", "r") + SV.line(DX(40), DYP(60), DX(20), DYP(80), "c3") + SV.text(DX(0) - 8, DYP(80), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(DX(20), DYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(DX(0) - 8, DYP(60), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(DX(40), DYP(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}, steps: [
  { cap: "Demand curve D. At price P₁ quantity demanded is Q₁ (point A).", s: { n: 0 } },
  { cap: "The price <b>falls</b> to P₂. Move <b>down</b> the same curve to B: an <b>extension in demand</b> (quantity demanded rises to Q₂).", s: { n: 1 } },
  { cap: "The price <b>rises</b> to P₂. Move <b>up</b> the same curve to C: a <b>contraction in demand</b> (quantity demanded falls to Q₂).", s: { n: 2 } },
] });
const SP = ["The price of a good falls (for example a shop sale)", "Quantity demanded rises", "Move down along the same demand curve", "An extension in demand", "The demand curve has not shifted"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A sale", base: { n: 0 }, draw: mkChain(SP, "--good"), steps: chainSteps(["The <b>price of a good falls</b> (for example a shop sale).", "<b>Quantity demanded rises</b>.", "Move <b>down</b> along the same demand curve.", "An <b>extension in demand</b>.", "The demand curve has <b>not shifted</b>."]) });

/* Lab 1: move along */
function labX() {
  if (!$("#xa")) return;
  const p = +$("#xa").value, q = 100 - p, p0 = 60, q0 = 100 - p0, dq = q - q0, pct = (dq / q0) * 100, ch = p < p0 ? "Extension" : p > p0 ? "Contraction" : "No change";
  $("#xa1").textContent = q; $("#xa2").textContent = ch; $("#xa3").textContent = (dq >= 0 ? "+" : "−") + Math.abs(Math.round(pct)) + "%";
  $("#xav").textContent = `Price moves from $60 to $${p}: quantity demanded moves from ${q0} to ${q} (${dq >= 0 ? "+" : "−"}${Math.abs(Math.round(pct))}%). ${ch === "No change" ? "No movement." : ch + " in demand: a movement " + (p < p0 ? "down" : "up") + " the same demand curve."} The curve has not shifted.`;
  $("#labX").innerHTML = dAxes() + dLine(0, "c1", "D") + dDrop(q0, p0) + SV.circle(DX(q0), DYP(p0), 6, "dot1") + (p !== p0 ? dDrop(q, p) + SV.circle(DX(q), DYP(p), 7, p < p0 ? "dot2" : "dot4") + SV.line(DX(q0), DYP(p0), DX(q), DYP(p), "c3") : "") + SV.text(DX(0) - 8, DYP(p0), "$60", "sm", { "text-anchor": "end" }) + SV.text(DX(q), DYP(0) + 18, q, "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "xa", label: "New price (starting at $60)", min: 10, max: 90, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labX });
const XM = [
  { n: "A shop holds a sale", d: "Extension", w: "The price falls." },
  { n: "A tax raises the price of cigarettes", d: "Contraction", w: "The price rises." },
  { n: "Cheaper production lowers the price", d: "Extension", w: "The price falls." },
  { n: "An increase in income", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "A successful advertising campaign", d: "Not a movement: a shift", w: "A factor other than price." },
];
button_table("xmBtns", "xmOut", XM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the demand curve</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>extension</b> or a <b>contraction</b> in demand?", buckets: [{ label: "Extension" }, { label: "Contraction" }], items: [
  { text: "A shop cuts the price of trainers", b: 0 }, { text: "A fall in the cost of production lowers the price", b: 0 }, { text: "A sale on coats", b: 0 },
  { text: "A tax raises the price of cigarettes", b: 1 }, { text: "A bad harvest raises the price of rice", b: 1 }, { text: "A firm increases its price", b: 1 },
], done: "Price down: extension. Price up: contraction." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>movement along</b> the demand curve or a <b>shift</b>?", buckets: [{ label: "Movement along" }, { label: "Shift of the curve" }], items: [
  { text: "A fall in the good's own price", b: 0 }, { text: "A rise in the good's own price", b: 0 },
  { text: "Consumers' incomes rise", b: 1 }, { text: "A fashion change", b: 1 }, { text: "A rise in the price of a substitute", b: 1 },
], done: "Only the good's own price causes a movement along." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Extension in demand", "Quantity demanded rises because the price falls"],
  ["Contraction in demand", "Quantity demanded falls because the price rises"],
  ["Movement along the curve", "Caused by a change in the good's own price"],
  ["Shift of the curve", "Caused by a change in a factor other than price"],
  ["Quantity demanded", "The amount bought at one price"],
  ["Demand", "The whole relationship between price and quantity"],
], done: "Extension and contraction are movements." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a price rise leads to a contraction in demand</b>.", items: [
  "The price of the good rises",
  "It is dearer than substitutes",
  "Consumers can afford less",
  "Quantity demanded falls",
  "Move up along the demand curve: a contraction",
], done: "A movement along the curve." });
Lib.calc($("#c1"), { qs: [
  { q: "Price falls from $60 to $40 and quantity demanded rises from 40 to 60. By what percentage does quantity demanded rise?", a: 50, sol: "20 ÷ 40 × 100 = <b>50%</b>." },
  { q: "Price rises from $20 to $25. What is the percentage change in price?", a: 25, sol: "5 ÷ 20 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A fall in the price of a good causes:", opts: ["A shift to the right", "An extension in demand", "A contraction in demand", "A shift to the left"], a: 1, why: "Move down the curve." },
  { q: "A contraction in demand is shown by:", opts: ["A move up along the curve", "A shift right", "A shift left", "A move down along the curve"], a: 0, why: "Price rises." },
  { q: "What causes a movement along a demand curve?", opts: ["A change in income", "A change in the good's own price", "A change in tastes", "Advertising"], a: 1, why: "Own price." },
  { q: "An extension in demand means:", opts: ["Demand shifts right", "Quantity demanded rises", "Price rises", "Quantity demanded falls"], a: 1, why: "Price down." },
  { q: "The difference between extension and increase in demand is:", opts: ["Extension is a movement; increase is a shift", "No difference", "Extension is a shift", "Increase is a price change"], a: 0, why: "Movement vs shift." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Extension in demand", "A rise in quantity demanded caused by a fall in price."],
  ["Contraction in demand", "A fall in quantity demanded caused by a rise in price."],
  ["Movement along the demand curve", "A change in quantity demanded caused by a change in the good's own price."],
  ["Quantity demanded", "The amount bought at one specific price."],
  ["Own price", "The price of the good itself."],
  ["Substitution effect", "Switching to a cheaper good."],
  ["Income effect", "A change in purchasing power."],
  ["Increase in demand", "A shift of the curve to the right."],
  ["Decrease in demand", "A shift of the curve to the left."],
] });
labX(); 
