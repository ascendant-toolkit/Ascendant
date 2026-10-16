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

Lib.stepper($("#stD"), { w: 760, h: 380, label: "Drawing a demand curve", base: { n: 0 }, draw: (s) => {
  let o = dAxes();
  if (s.n >= 1) o += SV.text(DX(0) - 8, DYP(80), "$80", "sm", { "text-anchor": "end" }) + SV.text(DX(0) - 8, DYP(40), "$40", "sm", { "text-anchor": "end" }) + dDot(20, 80, "", "dot1") + dDot(60, 40, "", "dot1");
  if (s.n >= 2) o += dLine(0, "c1", "D");
  if (s.n >= 3) o += dDrop(20, 80) + dDrop(60, 40) + SV.text(DX(20), DYP(0) + 18, "20", "sm", { "text-anchor": "middle" }) + SV.text(DX(60), DYP(0) + 18, "60", "sm", { "text-anchor": "middle" });
  return o;
}, steps: [
  { cap: "Price on the vertical axis; quantity demanded on the horizontal axis.", s: { n: 0 } },
  { cap: "At $80 consumers buy 20; at $40 they buy 60. Plot the two points.", s: { n: 1 } },
  { cap: "Join them: a <b>downward-sloping demand curve</b>, labelled D.", s: { n: 2 } },
  { cap: "Read across and down: a <b>lower price</b> means a <b>higher quantity demanded</b>.", s: { n: 3 } },
] });
const LW = ["The price of a good falls", "It is cheaper than substitutes: substitution effect", "Consumers' money buys more: income effect", "Each extra unit gives less satisfaction, but is now worth buying", "Quantity demanded rises: demand slopes downwards"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Why demand slopes down", base: { n: 0 }, draw: mkChain(LW, "--accent"), steps: chainSteps(["The <b>price</b> of a good falls.", "It is cheaper than substitutes: <b>substitution effect</b>.", "Consumers' money buys more: <b>income effect</b>.", "Each extra unit gives less satisfaction (<b>diminishing marginal utility</b>) but is now worth buying.", "<b>Quantity demanded rises</b>: the curve slopes downwards."]) });

/* Lab 1: individual to market demand */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const n = +$("#da").value, p = +$("#db").value, qi = Math.max(0, 100 - p), qm = n * qi / 1, scale = Math.max(1, n);
  $("#da1").textContent = qi; $("#da2").textContent = n; $("#da3").textContent = qm;
  $("#dav").textContent = `At a price of $${p} one consumer buys ${qi}. With ${n} identical consumers in the market, market demand is ${n} × ${qi} = ${qm}. More consumers shift the market demand curve to the right (more bought at every price).`;
  const X = (q) => 90 + q * (500 / Math.max(100, 100 * n)), Y = (pp) => 310 - pp * 2.7;
  let d = SV.line(90, Y(0), 90, Y(108)) + SV.line(90, Y(0), 640, Y(0)) + SV.text(98, 14, "Price ($)", "sm") + SV.text(640, Y(0) + 24, "Quantity demanded", "sm", { "text-anchor": "end" });
  d += SV.line(X(0), Y(100), X(100), Y(0), "c1") + SV.text(X(100) + 6, Y(0) - 8, "Individual", "sm bd t1");
  d += SV.line(X(0), Y(100), X(100 * n), Y(0), "c2") + SV.text(X(100 * n) - 6, Y(0) - 26, n > 1 ? "Market" : "", "sm bd t2", { "text-anchor": "end" });
  d += SV.line(X(0), Y(p), X(qm), Y(p), "gr") + SV.circle(X(qi), Y(p), 6, "dot1") + SV.circle(X(qm), Y(p), 7, "dot2") + SV.text(X(qm), Y(0) + 18, qm, "sm bd", { "text-anchor": "middle" });
  $("#labD").innerHTML = d;
}
Lib.slider($("#g1"), { id: "da", label: "Number of identical consumers in the market", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Price", min: 10, max: 90, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labD });
const AD = [
  { n: "Price falls", d: "Quantity demanded rises", w: "Substitution and income effects." },
  { n: "Price rises", d: "Quantity demanded falls", w: "Dearer than substitutes; less affordable." },
  { n: "More consumers", d: "Market demand rises", w: "Add up individual quantities at each price." },
  { n: "Fewer consumers", d: "Market demand falls", w: "Less bought at each price." },
  { n: "Consumers' incomes rise", d: "Demand curve shifts right", w: "(Covered in 2.2.3.)" },
];
button_table("adBtns", "adOut", AD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "A demand curve slopes downwards", b: 0 }, { text: "Demand means willing AND able to pay", b: 0 }, { text: "Market demand is the sum of individual demands", b: 0 }, { text: "A fall in price raises quantity demanded", b: 0 },
  { text: "Demand is just what people want", b: 1 }, { text: "A higher price raises quantity demanded", b: 1 }, { text: "Price is on the horizontal axis", b: 1 },
], done: "Law of demand: price up, quantity demanded down." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Demand", "Quantity willing and able to buy at a given price"],
  ["Law of demand", "Higher price, lower quantity demanded"],
  ["Market demand", "Sum of all individual demands"],
  ["Substitution effect", "Switching to a cheaper good"],
  ["Income effect", "Money buys more when price falls"],
  ["Ceteris paribus", "All other things unchanged"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price fall increases quantity demanded</b>.", items: [
  "The price of the good falls",
  "It is cheaper relative to substitutes",
  "Consumers' money goes further",
  "Consumers buy more",
  "Quantity demanded rises",
], done: "The law of demand." });
Lib.calc($("#c1"), { qs: [
  { q: "At $6 consumer A demands 12, B demands 10 and C demands 14. What is market demand?", a: 36, sol: "12 + 10 + 14 = <b>36</b>." },
  { q: "Market demand at $10 is 24 and at $8 it is 30. By what percentage does quantity demanded rise?", a: 25, sol: "6 ÷ 24 × 100 = <b>25%</b>." },
  { q: "10 identical consumers each buy 3 units at $5. What is market demand?", a: 30, sol: "10 × 3 = <b>30</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a demand curve show?", opts: ["Quantities supplied at each price", "Quantities demanded at each price", "Costs", "Profit"], a: 1, why: "Demand at each price." },
  { q: "Which describes the law of demand?", opts: ["Price up, quantity demanded up", "Price up, quantity demanded down", "Income up, price up", "Supply up, price down"], a: 1, why: "Inverse relationship." },
  { q: "Market demand is found by:", opts: ["Adding individual demands", "Subtracting", "Averaging prices", "Multiplying price"], a: 0, why: "Add quantities." },
  { q: "The demand curve slopes downwards because of:", opts: ["Substitution and income effects", "Rising costs", "Taxes", "Advertising"], a: 0, why: "Cheaper means more affordable." },
  { q: "Demand requires consumers to be:", opts: ["Willing only", "Willing and able to pay", "Wealthy", "Able only"], a: 1, why: "Both." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand", "The quantity consumers are willing and able to buy at a given price in a given period."],
  ["Law of demand", "As price rises, quantity demanded falls, ceteris paribus."],
  ["Demand curve", "A curve showing the quantity demanded at each price."],
  ["Market demand", "The sum of all individual demands."],
  ["Quantity demanded", "The amount bought at one specific price."],
  ["Substitution effect", "Switching to a good that has become relatively cheaper."],
  ["Income effect", "A change in real income when a price changes."],
  ["Diminishing marginal utility", "Each extra unit gives less satisfaction."],
  ["Ceteris paribus", "All other things remaining unchanged."],
] });
labD(); 
