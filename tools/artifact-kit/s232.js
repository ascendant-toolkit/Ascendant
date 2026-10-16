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

const SX = (q) => 90 + q * 4.6, SYP = (p) => 310 - p * 2.7;
function sAxes() { return SV.line(SX(0), SYP(0), SX(0), SYP(108)) + SV.line(SX(0), SYP(0), SX(135), SYP(0)) + SV.text(SX(0) + 8, 14, "Price ($)", "sm") + SV.text(SX(135), SYP(0) + 24, "Quantity supplied", "sm", { "text-anchor": "end" }); }
function sLine(s, cls, lab, tcls) {
  const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100];
  return SV.line(SX(a[0]), SYP(a[1]), SX(b[0]), SYP(b[1]), cls || "c2") + SV.text(SX(b[0]) + 6, SYP(b[1]) + 4, lab || "S", "lbl bd " + (tcls || "t2"));
}
function sDrop(q, p) { return SV.line(SX(0), SYP(p), SX(q), SYP(p), "gr") + SV.line(SX(q), SYP(p), SX(q), SYP(0), "gr"); }
function sDot(q, p, lab, cl, side) { return SV.circle(SX(q), SYP(p), 7, cl || "dot1") + SV.text(SX(q) + (side === "l" ? -12 : 12), SYP(p) + 4, lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }

Lib.stepper($("#stX"), { w: 760, h: 380, label: "Extension and contraction", base: { n: 0 }, draw: (s) => {
  let o = sAxes() + sLine(0, "c2", "S") + sDrop(40, 40) + sDot(40, 40, "A", "dot1", "l");
  if (s.n === 1) o += sDrop(70, 70) + sDot(70, 70, "B", "dot2", "l") + SV.line(SX(40), SYP(40), SX(70), SYP(70), "c3") + SV.text(SX(0) - 8, SYP(70), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(SX(70), SYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  if (s.n === 2) o += sDrop(20, 20) + sDot(20, 20, "C", "dot4", "r") + SV.line(SX(40), SYP(40), SX(20), SYP(20), "c3") + SV.text(SX(0) - 8, SYP(20), "P₂", "sm bd", { "text-anchor": "end" }) + SV.text(SX(20), SYP(0) + 18, "Q₂", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(SX(0) - 8, SYP(40), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(SX(40), SYP(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}, steps: [
  { cap: "Supply curve S. At price P₁ quantity supplied is Q₁ (point A).", s: { n: 0 } },
  { cap: "The price <b>rises</b> to P₂. Move <b>up</b> the same curve to B: an <b>extension in supply</b>.", s: { n: 1 } },
  { cap: "The price <b>falls</b> to P₂. Move <b>down</b> the same curve to C: a <b>contraction in supply</b>.", s: { n: 2 } },
] });
const SP = ["The price of coffee rises", "Growers earn more profit per tonne", "They produce more coffee", "Move up along the same supply curve", "An extension in supply (the curve has not shifted)"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A price rise", base: { n: 0 }, draw: mkChain(SP, "--warn"), steps: chainSteps(["The <b>price of coffee rises</b>.", "Growers earn <b>more profit</b> per tonne.", "They <b>produce more</b> coffee.", "Move <b>up</b> along the same supply curve.", "An <b>extension in supply</b> (the curve has not shifted)."]) });

/* Lab 1 */
function labX() {
  if (!$("#xa")) return;
  const p = +$("#xa").value, q = p, p0 = 40, q0 = p0, dq = q - q0, pct = (dq / q0) * 100, ch = p > p0 ? "Extension" : p < p0 ? "Contraction" : "No change";
  $("#xa1").textContent = q; $("#xa2").textContent = ch; $("#xa3").textContent = (dq >= 0 ? "+" : "−") + Math.abs(Math.round(pct)) + "%";
  $("#xav").textContent = `Price moves from $40 to $${p}: quantity supplied moves from ${q0} to ${q} (${dq >= 0 ? "+" : "−"}${Math.abs(Math.round(pct))}%). ${ch === "No change" ? "No movement." : ch + " in supply: a movement " + (p > p0 ? "up" : "down") + " the same supply curve."} The curve has not shifted.`;
  $("#labX").innerHTML = sAxes() + sLine(0, "c2", "S") + sDrop(q0, p0) + SV.circle(SX(q0), SYP(p0), 6, "dot1") + (p !== p0 ? sDrop(q, p) + SV.circle(SX(q), SYP(p), 7, p > p0 ? "dot2" : "dot4") + SV.line(SX(q0), SYP(p0), SX(q), SYP(p), "c3") : "") + SV.text(SX(0) - 8, SYP(p0), "$40", "sm", { "text-anchor": "end" }) + SV.text(SX(q), SYP(0) + 18, q, "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "xa", label: "New price (starting at $40)", min: 10, max: 90, step: 5, value: 60, fmt: (v) => "$" + v, onInput: labX });
const XM = [
  { n: "The price of the good rises", d: "Extension", w: "Higher profit per unit." },
  { n: "The price of the good falls", d: "Contraction", w: "Lower profit; some firms cut output." },
  { n: "Costs of production fall", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "New technology", d: "Not a movement: a shift", w: "A factor other than price." },
  { n: "A tax on the good", d: "Not a movement: a shift", w: "A factor other than price." },
];
button_table("xmBtns", "xmOut", XM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the supply curve</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>extension</b> or a <b>contraction</b> in supply?", buckets: [{ label: "Extension" }, { label: "Contraction" }], items: [
  { text: "The price of wheat rises and farmers grow more", b: 0 }, { text: "Higher oil prices lead wells to produce more", b: 0 }, { text: "A rise in the price of coffee", b: 0 },
  { text: "The price of milk falls and dairy farms cut output", b: 1 }, { text: "Falling oil prices close high-cost wells", b: 1 }, { text: "A fall in the price of steel", b: 1 },
], done: "Price up: extension. Price down: contraction." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>movement along</b> the supply curve or a <b>shift</b>?", buckets: [{ label: "Movement along" }, { label: "Shift of the curve" }], items: [
  { text: "A rise in the good's own price", b: 0 }, { text: "A fall in the good's own price", b: 0 },
  { text: "A fall in wage costs", b: 1 }, { text: "New technology", b: 1 }, { text: "A new tax on producers", b: 1 },
], done: "Only the good's own price causes a movement along." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Extension in supply", "Quantity supplied rises because the price rises"],
  ["Contraction in supply", "Quantity supplied falls because the price falls"],
  ["Movement along the curve", "Caused by a change in the good's own price"],
  ["Shift of the curve", "Caused by a change in a non-price factor"],
  ["Quantity supplied", "The amount supplied at one price"],
  ["Supply", "The whole relationship between price and quantity"],
], done: "Extension and contraction are movements." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a price fall causes a contraction in supply</b>.", items: [
  "The price of the good falls",
  "Profit per unit falls",
  "Some firms cut output or leave",
  "Quantity supplied falls",
  "Move down along the supply curve: a contraction",
], done: "A movement along the curve." });
Lib.calc($("#c1"), { qs: [
  { q: "Price rises from $40 to $60 and quantity supplied rises from 40 to 60. By what percentage does quantity supplied rise?", a: 50, sol: "20 ÷ 40 × 100 = <b>50%</b>." },
  { q: "Price falls from $50 to $40. What is the percentage change in price?", a: 20, sol: "10 ÷ 50 × 100 = <b>20%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in the price of a good causes:", opts: ["A shift to the right", "An extension in supply", "A contraction in supply", "A shift to the left"], a: 1, why: "Move up the curve." },
  { q: "A contraction in supply is shown by:", opts: ["A move up along the curve", "A shift right", "A shift left", "A move down along the curve"], a: 3, why: "Price falls." },
  { q: "What causes a movement along a supply curve?", opts: ["A change in costs", "A change in the good's own price", "New technology", "A tax"], a: 1, why: "Own price." },
  { q: "An extension in supply means:", opts: ["Supply shifts right", "Quantity supplied rises", "Price falls", "Quantity supplied falls"], a: 1, why: "Price up." },
  { q: "The difference between extension and increase in supply is:", opts: ["Extension is a movement; increase is a shift", "No difference", "Extension is a shift", "Increase is a price change"], a: 0, why: "Movement vs shift." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Extension in supply", "A rise in quantity supplied caused by a rise in price."],
  ["Contraction in supply", "A fall in quantity supplied caused by a fall in price."],
  ["Movement along the supply curve", "A change in quantity supplied caused by a change in the good's own price."],
  ["Quantity supplied", "The amount supplied at one price."],
  ["Own price", "The price of the good itself."],
  ["Profit per unit", "Price minus cost per unit."],
  ["Increase in supply", "A shift of the curve to the right."],
  ["Decrease in supply", "A shift of the curve to the left."],
  ["Marginal cost", "The cost of producing one more unit."],
] });
labX(); 
