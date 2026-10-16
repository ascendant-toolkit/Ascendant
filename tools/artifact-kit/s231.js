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

Lib.stepper($("#stD"), { w: 760, h: 380, label: "Drawing a supply curve", base: { n: 0 }, draw: (s) => {
  let o = sAxes();
  if (s.n >= 1) o += SV.text(SX(0) - 8, SYP(40), "$40", "sm", { "text-anchor": "end" }) + SV.text(SX(0) - 8, SYP(80), "$80", "sm", { "text-anchor": "end" }) + sDot(40, 40, "", "dot1") + sDot(80, 80, "", "dot1");
  if (s.n >= 2) o += sLine(0, "c2", "S");
  if (s.n >= 3) o += sDrop(40, 40) + sDrop(80, 80) + SV.text(SX(40), SYP(0) + 18, "40", "sm", { "text-anchor": "middle" }) + SV.text(SX(80), SYP(0) + 18, "80", "sm", { "text-anchor": "middle" });
  return o;
}, steps: [
  { cap: "Price on the vertical axis; quantity supplied on the horizontal axis.", s: { n: 0 } },
  { cap: "At $40 firms supply 40; at $80 they supply 80. Plot the points.", s: { n: 1 } },
  { cap: "Join them: an <b>upward-sloping supply curve</b>, labelled S.", s: { n: 2 } },
  { cap: "A <b>higher price</b> means a <b>higher quantity supplied</b>.", s: { n: 3 } },
] });
const LS = ["The price of a good rises", "Profit per unit rises", "Firms want to produce more; new firms may enter", "Higher price covers rising marginal cost", "Quantity supplied rises: supply slopes upwards"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Why supply slopes up", base: { n: 0 }, draw: mkChain(LS, "--warn"), steps: chainSteps(["The <b>price</b> of a good rises.", "<b>Profit per unit</b> rises.", "Firms want to <b>produce more</b>; new firms may enter.", "The higher price covers <b>rising marginal costs</b>.", "<b>Quantity supplied rises</b>: the curve slopes upwards."]) });

/* Lab 1: individual to market supply */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const n = +$("#sa").value, p = +$("#sb").value, qi = p, qm = n * qi;
  $("#sa1").textContent = qi; $("#sa2").textContent = n; $("#sa3").textContent = qm;
  $("#sav").textContent = `At a price of $${p} one firm supplies ${qi}. With ${n} identical firms in the market, market supply is ${n} × ${qi} = ${qm}. More firms shift the market supply curve to the right (more supplied at every price).`;
  const X = (q) => 90 + q * (500 / Math.max(100, 100 * n)), Y = (pp) => 310 - pp * 2.7;
  let d = SV.line(90, Y(0), 90, Y(108)) + SV.line(90, Y(0), 640, Y(0)) + SV.text(98, 14, "Price ($)", "sm") + SV.text(640, Y(0) + 24, "Quantity supplied", "sm", { "text-anchor": "end" });
  d += SV.line(X(0), Y(0), X(100), Y(100), "c2") + SV.text(X(100) + 6, Y(100) + 4, "Individual", "sm bd t2");
  d += SV.line(X(0), Y(0), X(100 * n), Y(100), "c1") + SV.text(X(85 * n) - 8, Y(85) - 10, n > 1 ? "Market" : "", "sm bd t1", { "text-anchor": "end" });
  d += SV.line(X(0), Y(p), X(qm), Y(p), "gr") + SV.circle(X(qi), Y(p), 6, "dot1") + SV.circle(X(qm), Y(p), 7, "dot2") + SV.text(X(qm), Y(0) + 18, qm, "sm bd", { "text-anchor": "middle" });
  $("#labS").innerHTML = d;
}
Lib.slider($("#g1"), { id: "sa", label: "Number of identical firms in the market", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Price", min: 10, max: 90, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labS });
const AS = [
  { n: "Price rises", d: "Quantity supplied rises", w: "Higher profit per unit." },
  { n: "Price falls", d: "Quantity supplied falls", w: "Lower profit; some firms leave." },
  { n: "More firms", d: "Market supply rises", w: "Add up individual quantities at each price." },
  { n: "Fewer firms", d: "Market supply falls", w: "Less supplied at each price." },
  { n: "Costs fall", d: "Supply curve shifts right", w: "(Covered in 2.3.3.)" },
];
button_table("asBtns", "asOut", AS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "A supply curve slopes upwards", b: 0 }, { text: "Supply means willing AND able to sell", b: 0 }, { text: "Market supply is the sum of individual supplies", b: 0 }, { text: "A rise in price raises quantity supplied", b: 0 },
  { text: "A supply curve slopes downwards", b: 1 }, { text: "A higher price lowers quantity supplied", b: 1 }, { text: "Quantity supplied is on the vertical axis", b: 1 },
], done: "Law of supply: price up, quantity supplied up." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Supply", "Quantity willing and able to sell at a given price"],
  ["Law of supply", "Higher price, higher quantity supplied"],
  ["Market supply", "Sum of all individual supplies"],
  ["Profit motive", "Higher prices give higher profit per unit"],
  ["Marginal cost", "Cost of producing one more unit"],
  ["Ceteris paribus", "All other things unchanged"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price rise increases quantity supplied</b>.", items: [
  "The price of the good rises",
  "Profit per unit rises",
  "Firms want to produce more",
  "Firms supply more",
  "Quantity supplied rises",
], done: "The law of supply." });
Lib.calc($("#c1"), { qs: [
  { q: "At $6 firm A supplies 10, B supplies 8 and C supplies 12. What is market supply?", a: 30, sol: "10 + 8 + 12 = <b>30</b>." },
  { q: "Market supply at $4 is 24 and at $6 it is 30. By what percentage does quantity supplied rise?", a: 25, sol: "6 ÷ 24 × 100 = <b>25%</b>." },
  { q: "20 identical farms each supply 50 tonnes at $200. What is market supply (tonnes)?", a: 1000, sol: "20 × 50 = <b>1,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a supply curve show?", opts: ["Quantities demanded", "Quantities supplied at each price", "Costs", "Taxes"], a: 1, why: "Supply at each price." },
  { q: "Which describes the law of supply?", opts: ["Price up, quantity supplied up", "Price up, quantity supplied down", "Income up, price up", "Demand up, supply down"], a: 0, why: "Direct relationship." },
  { q: "Market supply is found by:", opts: ["Adding individual supplies", "Subtracting", "Averaging", "Multiplying price"], a: 0, why: "Add quantities." },
  { q: "The supply curve slopes upwards because:", opts: ["Higher prices give higher profit per unit", "Costs fall", "Demand falls", "Taxes rise"], a: 0, why: "Incentive to produce more." },
  { q: "Supply requires producers to be:", opts: ["Willing only", "Willing and able to sell", "Large", "Foreign"], a: 1, why: "Both." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Supply", "The quantity producers are willing and able to sell at a given price in a given period."],
  ["Law of supply", "As price rises, quantity supplied rises, ceteris paribus."],
  ["Supply curve", "A curve showing the quantity supplied at each price."],
  ["Market supply", "The sum of all individual firms' supplies."],
  ["Quantity supplied", "The amount supplied at one specific price."],
  ["Profit motive", "The aim of earning profit."],
  ["Marginal cost", "The cost of producing one extra unit."],
  ["New entrants", "Firms that enter a market."],
  ["Ceteris paribus", "All other things remaining unchanged."],
] });
labS(); 
