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

function disChart(p, d, s) {
  const [q, pe] = eq(d, s), qd = qD(p, d), qs = qS(p, s);
  let o = axes() + dCurve(d, "c1", "D") + sCurve(s, "c2", "S") + SV.line(X(0), Y(p), X(Math.max(qd, qs) + 8), Y(p), "gr") + SV.circle(X(q), Y(pe), 6, "dot1");
  if (Math.abs(qd - qs) > 0.5) o += SV.circle(X(qd), Y(p), 6, "dot3") + SV.circle(X(qs), Y(p), 6, "dot4") + SV.line(X(Math.min(qd, qs)), Y(p), X(Math.max(qd, qs)), Y(p), "c3") + SV.text(X((qd + qs) / 2), Y(p) - 12, qd > qs ? "Shortage " + money(qd - qs, 0) : "Surplus " + money(qs - qd, 0), "lbl bd " + (qd > qs ? "t2" : "t4"), { "text-anchor": "middle" }) + SV.text(X(qd), Y(0) + 18, "Qd", "sm bd", { "text-anchor": "middle" }) + SV.text(X(qs), Y(0) + 18, "Qs", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(X(0) - 8, Y(p), "$" + money(p, 0), "sm bd", { "text-anchor": "end" });
}
Lib.stepper($("#stD"), { w: 760, h: 380, label: "Shortage and surplus", base: { p: 50 }, draw: (s) => disChart(s.p, 0, 0), steps: [
  { cap: "At the equilibrium price demand equals supply.", s: { p: 50 } },
  { cap: "A price <b>above</b> equilibrium: quantity supplied exceeds quantity demanded: a <b>surplus</b>.", s: { p: 75 } },
  { cap: "A price <b>below</b> equilibrium: quantity demanded exceeds quantity supplied: a <b>shortage</b>.", s: { p: 25 } },
] });
const AD = ["A surplus exists: the price is above equilibrium", "Sellers have unsold stock", "They cut prices", "Quantity demanded rises; quantity supplied falls", "The surplus disappears at equilibrium"];
Lib.stepper($("#stA"), { w: 760, h: 380, label: "Adjusting from a surplus", base: { n: 0 }, draw: mkChain(AD, "--bad"), steps: chainSteps(["A <b>surplus</b> exists: the price is above equilibrium.", "Sellers have <b>unsold stock</b>.", "They <b>cut prices</b>.", "Quantity demanded <b>rises</b>; quantity supplied <b>falls</b>.", "The surplus disappears at <b>equilibrium</b>."]) });
const SH = ["A shortage exists: the price is below equilibrium", "Buyers compete for limited goods", "Sellers raise prices", "Quantity demanded falls; quantity supplied rises", "The shortage disappears at equilibrium"];
Lib.stepper($("#stB"), { w: 760, h: 380, label: "Adjusting from a shortage", base: { n: 0 }, draw: mkChain(SH, "--warn"), steps: chainSteps(["A <b>shortage</b> exists: the price is below equilibrium.", "Buyers <b>compete</b> for limited goods.", "Sellers <b>raise prices</b>.", "Quantity demanded <b>falls</b>; quantity supplied <b>rises</b>.", "The shortage disappears at <b>equilibrium</b>."]) });

/* Lab 1: choose a price */
function labD() {
  if (!$("#da")) return;
  const p = +$("#da").value, qd = qD(p, 0), qs = qS(p, 0), gap = qd - qs, st = gap > 0.5 ? "Shortage" : gap < -0.5 ? "Surplus" : "Equilibrium";
  $("#da1").textContent = qd; $("#da2").textContent = qs; $("#da3").textContent = st + (Math.abs(gap) > 0.5 ? " " + Math.abs(gap) : "");
  $("#dav").textContent = `At $${p}, quantity demanded is ${qd} and quantity supplied is ${qs}: ${st === "Equilibrium" ? "the market clears." : st === "Shortage" ? "a shortage of " + gap + ". Buyers compete and the price tends to rise." : "a surplus of " + (-gap) + ". Sellers compete and the price tends to fall."}`;
  $("#labD").innerHTML = disChart(p, 0, 0);
}
Lib.slider($("#g1"), { id: "da", label: "Market price", min: 10, max: 90, step: 5, value: 70, fmt: (v) => "$" + v, onInput: labD });
const DQ = [
  { n: "Price above equilibrium", t: "Surplus", e: "Qs > Qd: sellers cut prices." },
  { n: "Price below equilibrium", t: "Shortage", e: "Qd > Qs: buyers bid up the price." },
  { n: "Bumper harvest in a global market", t: "Surplus at the old price", e: "Supply shifts right; the old price is too high." },
  { n: "A surge in demand", t: "Shortage at the old price", e: "Demand shifts right; the old price is too low." },
  { n: "A price ceiling below equilibrium", t: "Persistent shortage", e: "The price cannot rise." },
];
button_table("dqBtns", "dqOut", DQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>Result</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>shortage</b> or a <b>surplus</b>?", buckets: [{ label: "Shortage" }, { label: "Surplus" }], items: [
  { text: "Quantity demanded exceeds quantity supplied", b: 0 }, { text: "Price below equilibrium", b: 0 }, { text: "Excess demand", b: 0 },
  { text: "Quantity supplied exceeds quantity demanded", b: 1 }, { text: "Price above equilibrium", b: 1 }, { text: "Excess supply", b: 1 },
], done: "Shortage means demand exceeds supply." });
Lib.classify($("#cl2"), { prompt: "What happens <b>next</b> to the price?", buckets: [{ label: "Price rises" }, { label: "Price falls" }], items: [
  { text: "There is a shortage", b: 0 }, { text: "Buyers compete for scarce goods", b: 0 },
  { text: "There is a surplus", b: 1 }, { text: "Sellers have unsold stock", b: 1 },
], done: "Markets adjust towards equilibrium." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market disequilibrium", "Quantity demanded does not equal quantity supplied"],
  ["Shortage", "Demand exceeds supply"],
  ["Surplus", "Supply exceeds demand"],
  ["Excess demand", "Another name for a shortage"],
  ["Excess supply", "Another name for a surplus"],
  ["Price mechanism", "Moves the market back to equilibrium"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a market moves from a shortage to equilibrium</b>.", items: [
  "The price is below equilibrium",
  "Quantity demanded exceeds quantity supplied",
  "Buyers compete and the price rises",
  "Quantity demanded falls and quantity supplied rises",
  "The market reaches equilibrium",
], done: "A shortage pushes the price up." });
Lib.calc($("#c1"), { qs: [
  { q: "At $4, quantity demanded is 70 and quantity supplied is 30. What is the shortage?", a: 40, sol: "70 − 30 = <b>40</b>." },
  { q: "At $8, quantity demanded is 40 and quantity supplied is 60. What is the surplus?", a: 20, sol: "60 − 40 = <b>20</b>." },
  { q: "A surplus of 20 on a supply of 60 is what percentage of supply (to the nearest whole number)?", a: 33, sol: "20 ÷ 60 × 100 = <b>33%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Market disequilibrium means:", opts: ["Demand equals supply", "Quantity demanded does not equal quantity supplied", "Prices are fixed", "No trade"], a: 1, why: "The market does not clear." },
  { q: "A shortage occurs when:", opts: ["Price is above equilibrium", "Price is below equilibrium", "Price equals equilibrium", "Supply is zero"], a: 1, why: "Qd > Qs." },
  { q: "A surplus will cause the price to:", opts: ["Rise", "Fall", "Stay the same", "Double"], a: 1, why: "Sellers compete." },
  { q: "Excess demand is another name for:", opts: ["A surplus", "A shortage", "Equilibrium", "A tax"], a: 1, why: "Qd > Qs." },
  { q: "Which could cause a surplus at the old price?", opts: ["A rise in demand", "A rise in supply", "A fall in supply", "A fall in tax on buyers"], a: 1, why: "More supplied than demanded." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Market disequilibrium", "Quantity demanded does not equal quantity supplied."],
  ["Shortage", "Quantity demanded exceeds quantity supplied (excess demand)."],
  ["Surplus", "Quantity supplied exceeds quantity demanded (excess supply)."],
  ["Excess demand", "A shortage."],
  ["Excess supply", "A surplus."],
  ["Price above equilibrium", "Leads to a surplus."],
  ["Price below equilibrium", "Leads to a shortage."],
  ["Market clearing", "No shortage or surplus remains."],
  ["Price ceiling", "A government maximum price."],
] });
labD(); 
