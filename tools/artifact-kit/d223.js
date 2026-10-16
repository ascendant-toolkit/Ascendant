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

Lib.stepper($("#stH"), { w: 760, h: 380, label: "Shifts of demand", base: { s: 0 }, draw: (s) => {
  let o = dAxes() + dLine(0, s.s === 0 ? "c1" : "c3", "D");
  if (s.s !== 0) o += dLine(s.s, s.s > 0 ? "c2" : "c4", s.s > 0 ? "D₁" : "D₂", s.s > 0 ? "t2" : "t4") + dDrop(50, 50) + dDot(50, 50, "", "dot1") + dDot(50 + s.s * 0.5 + 0, 50, "", s.s > 0 ? "dot2" : "dot4") + SV.line(DX(50), DYP(50), DX(50 + s.s), DYP(50), "c3");
  return o + SV.text(DX(0) - 8, DYP(50), "P", "sm bd", { "text-anchor": "end" });
}, steps: [
  { cap: "Demand curve D.", s: { s: 0 } },
  { cap: "Incomes rise, or a good becomes fashionable: demand <b>increases</b> and the curve shifts <b>right</b> to D₁. <b>More is demanded at every price</b>.", s: { s: 30 } },
  { cap: "The good goes out of fashion: demand <b>decreases</b> and the curve shifts <b>left</b> to D₂. <b>Less is demanded at every price</b>.", s: { s: -30 } },
] });
const IN = ["Consumers' incomes rise", "They can afford more of a normal good", "More is demanded at every price", "The demand curve shifts right", "An increase in demand"];
Lib.stepper($("#stI"), { w: 760, h: 380, label: "A rise in income", base: { n: 0 }, draw: mkChain(IN, "--good"), steps: chainSteps(["Consumers' <b>incomes rise</b>.", "They can afford more of a <b>normal good</b>.", "<b>More is demanded at every price</b>.", "The demand curve <b>shifts right</b>.", "An <b>increase in demand</b>."]) });
const SB = ["The price of tea rises", "Tea is now dearer relative to coffee", "Consumers switch to coffee", "Demand for coffee rises at every price", "The coffee demand curve shifts right"];
Lib.stepper($("#stB"), { w: 760, h: 380, label: "A substitute's price rises", base: { n: 0 }, draw: mkChain(SB, "--accent"), steps: chainSteps(["The <b>price of tea</b> rises.", "Tea is dearer relative to coffee.", "Consumers <b>switch to coffee</b>.", "Demand for coffee rises <b>at every price</b>.", "The coffee demand curve <b>shifts right</b>."]) });

/* Lab 1: factors */
const FACT = [
  { n: "Income rises (normal good)", s: 25 }, { n: "Income rises (inferior good)", s: -25 }, { n: "Becomes fashionable", s: 30 }, { n: "Goes out of fashion", s: -30 },
  { n: "Substitute becomes dearer", s: 20 }, { n: "Complement becomes dearer", s: -20 }, { n: "Population grows", s: 20 }, { n: "Expected price rise", s: 15 },
];
function labF() {
  const i = +($("#fa") ? $("#fa").value : 0), f = FACT[i]; if (!$("#fa")) return;
  const s = f.s;
  $("#fa1").textContent = s > 0 ? "Increase" : "Decrease"; $("#fa2").textContent = s > 0 ? "Right" : "Left"; $("#fa3").textContent = (s > 0 ? "+" : "−") + Math.abs(s);
  $("#fav").textContent = `${f.n}: demand ${s > 0 ? "increases" : "decreases"} and the curve shifts ${s > 0 ? "right" : "left"}. At the same price of $50 the quantity demanded changes from 50 to ${50 + s}.`;
  $("#labF").innerHTML = dAxes() + dLine(0, "c3", "D") + dLine(s, s > 0 ? "c2" : "c4", s > 0 ? "D₁" : "D₂", s > 0 ? "t2" : "t4") + dDrop(50, 50) + SV.circle(DX(50), DYP(50), 6, "dot1") + SV.circle(DX(50 + s), DYP(50), 7, s > 0 ? "dot2" : "dot4") + SV.line(DX(50), DYP(50), DX(50 + s), DYP(50), "c3");
}
Lib.slider($("#g1"), { id: "fa", label: "Choose a factor (0 to 7)", min: 0, max: 7, step: 1, value: 0, fmt: (v) => FACT[v].n, onInput: labF });
const SH = [
  { n: "Substitutes", d: "Butter and margarine", e: "A rise in the price of one raises demand for the other." },
  { n: "Complements", d: "Cars and petrol", e: "A rise in the price of one lowers demand for the other." },
  { n: "Normal good", d: "Restaurant meals", e: "Demand rises as income rises." },
  { n: "Inferior good", d: "Own-brand cheap bread", e: "Demand falls as income rises." },
  { n: "Advertising", d: "A successful campaign", e: "Raises demand at every price." },
];
button_table("shBtns", "shOut", SH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Example</th><th>Effect</th></tr><tr><td>${p.d}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each <b>increase</b> or <b>decrease</b> demand for the good named?", buckets: [{ label: "Increase in demand" }, { label: "Decrease in demand" }], items: [
  { text: "Incomes rise: demand for holidays", b: 0 }, { text: "A successful advertising campaign for a drink", b: 0 }, { text: "The price of tea rises: demand for coffee", b: 0 }, { text: "Hot weather: demand for ice cream", b: 0 },
  { text: "A fall in the price of a substitute", b: 1 }, { text: "A rise in the price of a complement", b: 1 }, { text: "A health warning about a snack", b: 1 }, { text: "Population falls", b: 1 },
], done: "Right means increase; left means decrease." });
Lib.classify($("#cl2"), { prompt: "Are the two goods <b>substitutes</b> or <b>complements</b>?", buckets: [{ label: "Substitutes" }, { label: "Complements" }], items: [
  { text: "Tea and coffee", b: 0 }, { text: "Butter and margarine", b: 0 }, { text: "Buses and trains", b: 0 },
  { text: "Cars and petrol", b: 1 }, { text: "Printers and ink", b: 1 }, { text: "Bread and butter", b: 1 },
], done: "Substitutes replace; complements go together." });
Lib.match($("#m1"), { prompt: "Match the cause to the effect on demand.", pairs: [
  ["Income rises (normal good)", "Demand shifts right"],
  ["Income rises (inferior good)", "Demand shifts left"],
  ["Price of a substitute rises", "Demand shifts right"],
  ["Price of a complement rises", "Demand shifts left"],
  ["Good goes out of fashion", "Demand shifts left"],
  ["Population rises", "Demand shifts right"],
], done: "Learn the pairs." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how advertising increases demand</b>.", items: [
  "A successful advertising campaign runs",
  "Consumers' tastes change in favour of the good",
  "More is demanded at every price",
  "The demand curve shifts right",
  "An increase in demand",
], done: "A change in tastes." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand at $50 rises from 50 to 80 units after an advertising campaign. What is the percentage increase?", a: 60, sol: "30 ÷ 50 × 100 = <b>60%</b>." },
  { q: "A good is dearer by 10% and demand for its substitute rises by 8%. What is the new demand for the substitute if it was 200?", a: 216, sol: "200 × 1.08 = <b>216</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A shift of the demand curve to the right shows:", opts: ["A fall in price", "An increase in demand", "A decrease in demand", "A contraction"], a: 1, why: "More at every price." },
  { q: "Which would shift a demand curve to the left?", opts: ["Rising incomes (normal good)", "A fall in the price of a substitute", "A successful advert", "Population growth"], a: 1, why: "Consumers switch away." },
  { q: "A rise in the price of a complement:", opts: ["Raises demand for the good", "Lowers demand for the good", "Has no effect", "Raises supply"], a: 1, why: "They are used together." },
  { q: "An inferior good is one whose demand:", opts: ["Rises as income rises", "Falls as income rises", "Is unaffected by income", "Is zero"], a: 1, why: "Consumers switch to better goods." },
  { q: "A shift of a demand curve is caused by:", opts: ["A change in the good's own price", "A change in a factor other than price", "A tax on supply", "A movement along"], a: 1, why: "Non-price factors." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Increase in demand", "A shift of the demand curve to the right."],
  ["Decrease in demand", "A shift of the demand curve to the left."],
  ["Substitute", "A good that can be used in place of another."],
  ["Complement", "A good used together with another."],
  ["Normal good", "A good for which demand rises as income rises."],
  ["Inferior good", "A good for which demand falls as income rises."],
  ["Tastes", "Consumers' preferences and fashion."],
  ["Expectations", "Beliefs about future prices or incomes."],
  ["Non-price factor", "A factor other than the good's own price that affects demand."],
] });
labF(); 
