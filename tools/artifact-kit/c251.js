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

function shiftChart(d, s) {
  const [q0, p0] = eq(0, 0), [q1, p1] = eq(d, s);
  let o = axes() + dCurve(0, d !== 0 ? "c3" : "c1", "D", d !== 0 ? "t3" : "t1") + sCurve(0, s !== 0 ? "c3" : "c2", "S", s !== 0 ? "t3" : "t2");
  if (d !== 0) o += dCurve(d, d > 0 ? "c1" : "c4", d > 0 ? "D₁" : "D₂", d > 0 ? "t1" : "t4");
  if (s !== 0) o += sCurve(s, s > 0 ? "c2" : "c4", s > 0 ? "S₁" : "S₂", s > 0 ? "t2" : "t4");
  o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 6, "dot1") + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (d !== 0 || s !== 0) o += dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
  return o;
}
function dirWord(a, b) { return Math.abs(b - a) < 0.5 ? "unchanged" : b > a ? "rises" : "falls"; }

Lib.stepper($("#stD"), { w: 760, h: 380, label: "A rise in demand", base: { d: 0, s: 0 }, draw: (s) => shiftChart(s.d, s.s), steps: [
  { cap: "Starting equilibrium at price P and quantity Q.", s: { d: 0, s: 0 } },
  { cap: "Incomes rise: demand <b>increases</b>. D shifts right to D₁.", s: { d: 30, s: 0 } },
  { cap: "At P there is now a shortage, so the price rises to the new equilibrium <b>P₁</b>, and quantity rises to <b>Q₁</b>.", s: { d: 30, s: 0 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A fall in supply", base: { d: 0, s: 0 }, draw: (s) => shiftChart(s.d, s.s), steps: [
  { cap: "Starting equilibrium at price P and quantity Q.", s: { d: 0, s: 0 } },
  { cap: "A tax raises costs: supply <b>decreases</b>. S shifts left to S₂.", s: { d: 0, s: -30 } },
  { cap: "At P there is now a shortage, so the price <b>rises</b> to P₁ and quantity <b>falls</b> to Q₁.", s: { d: 0, s: -30 } },
] });
const CH = ["Demand or supply shifts", "At the old price quantity demanded no longer equals quantity supplied", "A shortage or surplus appears", "The price adjusts", "A new equilibrium is reached"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "How a shift changes the price", base: { n: 0 }, draw: mkChain(CH, "--accent"), steps: chainSteps(["<b>Demand or supply shifts</b>.", "At the old price quantity demanded no longer equals quantity supplied.", "A <b>shortage or surplus</b> appears.", "The <b>price adjusts</b>.", "A <b>new equilibrium</b> is reached."]) });

/* Lab 1: shift both */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const d = +$("#sa").value, s = +$("#sb").value, [q0, p0] = eq(0, 0), [q1, p1] = eq(d, s);
  $("#sa1").textContent = "$" + money(p1, 0) + " (" + dirWord(p0, p1) + ")"; $("#sa2").textContent = money(q1, 0) + " (" + dirWord(q0, q1) + ")"; $("#sa3").textContent = d === 0 && s === 0 ? "None" : d !== 0 && s !== 0 ? "Both" : d !== 0 ? "Demand" : "Supply";
  $("#sav").textContent = `Equilibrium moves from price $${money(p0, 0)}, quantity ${money(q0, 0)} to price $${money(p1, 0)}, quantity ${money(q1, 0)}. ` + (d !== 0 && s === 0 ? "Only demand shifts: price and quantity move in the same direction." : s !== 0 && d === 0 ? "Only supply shifts: price and quantity move in opposite directions." : d !== 0 && s !== 0 ? "Both curves shift: the effect on one variable depends on which shift is bigger." : "No shift: no change.");
  $("#labS").innerHTML = shiftChart(d, s);
}
Lib.slider($("#g1"), { id: "sa", label: "Shift in demand (right +, left −)", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Shift in supply (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labS });
const CAUSE = [
  { n: "Incomes rise", c: "Demand increases", p: "Price rises", q: "Quantity rises" },
  { n: "A health warning on a product", c: "Demand decreases", p: "Price falls", q: "Quantity falls" },
  { n: "Costs of production rise", c: "Supply decreases", p: "Price rises", q: "Quantity falls" },
  { n: "New technology", c: "Supply increases", p: "Price falls", q: "Quantity rises" },
  { n: "A subsidy to producers", c: "Supply increases", p: "Price falls", q: "Quantity rises" },
  { n: "A drought hits farms", c: "Supply decreases", p: "Price rises", q: "Quantity falls" },
];
button_table("caBtns", "caOut", CAUSE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Curve</th><th>Price</th><th>Quantity</th></tr><tr><td><b>${p.c}</b></td><td>${p.p}</td><td>${p.q}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>price</b> in each case?", buckets: [{ label: "Price rises" }, { label: "Price falls" }], items: [
  { text: "Demand increases", b: 0 }, { text: "Supply decreases", b: 0 }, { text: "A drought hits the harvest", b: 0 }, { text: "Incomes rise (normal good)", b: 0 },
  { text: "Demand decreases", b: 1 }, { text: "Supply increases", b: 1 }, { text: "New technology cuts costs", b: 1 }, { text: "A subsidy to producers", b: 1 },
], done: "Think: which curve, which way?" });
Lib.classify($("#cl2"), { prompt: "Which <b>curve shifts</b>?", buckets: [{ label: "Demand" }, { label: "Supply" }], items: [
  { text: "Incomes rise", b: 0 }, { text: "Fashion changes", b: 0 }, { text: "Price of a substitute rises", b: 0 },
  { text: "Wages rise", b: 1 }, { text: "A tax on producers", b: 1 }, { text: "New technology", b: 1 },
], done: "Demand: buyers. Supply: producers." });
Lib.match($("#m1"), { prompt: "Match the change to its effect.", pairs: [
  ["Demand right", "Price and quantity rise"],
  ["Demand left", "Price and quantity fall"],
  ["Supply right", "Price falls, quantity rises"],
  ["Supply left", "Price rises, quantity falls"],
  ["Both D and S right", "Quantity rises for sure"],
  ["D right, S left", "Price rises for sure"],
], done: "Learn the four basic cases." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an increase in incomes raises the price of a good</b>.", items: [
  "Incomes rise",
  "Demand for the good increases: D shifts right",
  "At the old price there is a shortage",
  "Price rises",
  "A new equilibrium at a higher price and quantity",
], done: "Demand up, price up." });
Lib.calc($("#c1"), { qs: [
  { q: "The equilibrium price rises from $50 to $60. What is the percentage rise?", a: 20, sol: "10 ÷ 50 × 100 = <b>20%</b>." },
  { q: "The equilibrium quantity rises from 50 to 60 units. What is the percentage rise?", a: 20, sol: "10 ÷ 50 × 100 = <b>20%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An increase in demand will cause the equilibrium price to:", opts: ["Rise", "Fall", "Stay the same", "Fall and quantity fall"], a: 0, why: "Shortage at the old price." },
  { q: "A fall in supply will cause price to:", opts: ["Rise", "Fall", "Stay the same", "Halve"], a: 0, why: "Shortage at the old price." },
  { q: "An increase in supply will cause quantity to:", opts: ["Rise", "Fall", "Stay the same", "Disappear"], a: 0, why: "More is supplied and bought." },
  { q: "A new tax on producers shifts:", opts: ["Demand right", "Supply left", "Supply right", "Demand left"], a: 1, why: "Costs rise." },
  { q: "If both demand and supply increase, equilibrium quantity:", opts: ["Rises", "Falls", "Is unchanged", "Is uncertain"], a: 0, why: "Both push quantity up." },
] });

Lib.cards($("#fc1"), { cards: [
  ["New equilibrium", "The equilibrium reached after a shift in demand or supply."],
  ["Increase in demand", "D shifts right."],
  ["Decrease in demand", "D shifts left."],
  ["Increase in supply", "S shifts right."],
  ["Decrease in supply", "S shifts left."],
  ["Shortage", "Quantity demanded exceeds quantity supplied."],
  ["Surplus", "Quantity supplied exceeds quantity demanded."],
  ["Equilibrium price", "The price at which the market clears."],
  ["Ceteris paribus", "All other things unchanged."],
] });
labS(); 
