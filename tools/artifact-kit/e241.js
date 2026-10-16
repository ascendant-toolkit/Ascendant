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

const WT = ["Consumers' demand for a good rises", "Its price rises and firms' profits rise", "Higher profit is an incentive for firms to produce more", "Resources move into the good", "The market has answered: produce more of it"];
Lib.stepper($("#stW"), { w: 760, h: 380, label: "What to produce", base: { n: 0 }, draw: mkChain(WT, "--accent"), steps: chainSteps(["Consumers' <b>demand</b> for a good rises.", "Its <b>price</b> rises and firms' <b>profits</b> rise.", "Higher profit is an <b>incentive</b> for firms to produce more.", "<b>Resources move</b> into the good.", "The market has answered: <b>produce more of it</b>."]) });
const HW = ["The price of a factor (e.g. labour) rises", "Using it becomes more expensive", "Firms switch to a cheaper factor (e.g. machines)", "Costs fall; profit is protected", "The market has answered: how to produce"];
Lib.stepper($("#stH"), { w: 760, h: 380, label: "How to produce", base: { n: 0 }, draw: mkChain(HW, "--warn"), steps: chainSteps(["The <b>price of a factor</b> (e.g. labour) rises.", "Using it becomes <b>more expensive</b>.", "Firms switch to a <b>cheaper factor</b> (e.g. machines).", "<b>Costs fall</b>; profit is protected.", "The market has answered <b>how to produce</b>."]) });
const FW = ["Goods have a price", "Consumers with enough income can pay it", "Those unable or unwilling to pay do without", "Goods go to those willing and able to pay", "The market has answered: for whom"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "For whom to produce", base: { n: 0 }, draw: mkChain(FW, "--good"), steps: chainSteps(["Goods have a <b>price</b>.", "Consumers with enough <b>income</b> can pay it.", "Those unable or unwilling to pay <b>do without</b>.", "Goods go to those <b>willing and able to pay</b>.", "The market has answered <b>for whom</b>."]) });

/* Lab 1: demand rises, price signals */
function labP() {
  if (!$("#pa")) return;
  const d = +$("#pa").value, [q, p] = eq(d, 0), [q0, p0] = eq(0, 0);
  $("#pa1").textContent = "$" + money(p, 0); $("#pa2").textContent = money(q, 0); $("#pa3").textContent = money(q - q0, 0) >= 0 ? "+" + money(q - q0, 0) : money(q - q0, 0);
  $("#pav").textContent = `Demand ${d >= 0 ? "rises" : "falls"} by ${Math.abs(d)} at every price: the price moves from $${money(p0, 0)} to $${money(p, 0)} and the quantity from ${money(q0, 0)} to ${money(q, 0)}. The higher price signals firms to produce more, and the higher profit is the incentive: resources move into the good (the answer to 'what to produce').`;
  $("#labP").innerHTML = axes() + sCurve(0, "c2", "S") + dCurve(0, "c3", "D", "t3") + (d !== 0 ? dCurve(d, d > 0 ? "c1" : "c4", "D₁", d > 0 ? "t1" : "t4") : "") + dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 6, "dot1") + (d !== 0 ? dsDrop(q, p) + SV.circle(X(q), Y(p), 7, d > 0 ? "dot2" : "dot4") : "");
}
Lib.slider($("#g1"), { id: "pa", label: "Change in demand (at every price)", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labP });
const QU = [
  { n: "What to produce", a: "Demand and profit", e: "Rising demand raises price and profit; firms make more." },
  { n: "How to produce", a: "Relative factor prices and competition", e: "Firms pick the cheapest efficient method." },
  { n: "For whom to produce", a: "Willingness and ability to pay", e: "Goods go to those who can afford the price." },
];
button_table("quBtns", "quOut", QU, 0, (p) => `<div class="tw"><table class="t"><tr><th>Decided by</th><th>Explanation</th></tr><tr><td><b>${p.a}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>question</b> does each describe?", buckets: [{ label: "What to produce" }, { label: "How to produce" }, { label: "For whom to produce" }], items: [
  { text: "Rising demand raises profit, so firms make more", b: 0 }, { text: "Resources move out of a good with falling demand", b: 0 },
  { text: "Firms use machines because labour has become dearer", b: 1 }, { text: "Firms choose the cheapest efficient method", b: 1 },
  { text: "Goods go to those willing and able to pay", b: 2 }, { text: "Those with low incomes may go without", b: 2 },
], done: "What, how, for whom." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>strength</b> or a <b>weakness</b> of the price mechanism?", buckets: [{ label: "Strength" }, { label: "Weakness" }], items: [
  { text: "Resources move to where they are wanted", b: 0 }, { text: "Encourages efficiency", b: 0 }, { text: "Low administrative cost", b: 0 },
  { text: "Ignores external costs like pollution", b: 1 }, { text: "Low-income households may go without", b: 1 }, { text: "May under-provide public goods", b: 1 },
], done: "Evaluate both sides." });
Lib.match($("#m1"), { prompt: "Match the function of prices to its meaning.", pairs: [
  ["Signalling", "Tells firms and consumers where resources are wanted"],
  ["Incentive", "A reason to change behaviour, such as profit"],
  ["Rationing", "Allocating scarce goods to those who can pay"],
  ["Price mechanism", "Prices adjusting to allocate resources"],
  ["Profit", "An incentive to produce"],
  ["Willing and able to pay", "The test for demand"],
], done: "Know the three functions." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the price mechanism answers 'what to produce'</b>.", items: [
  "Consumers' demand for a good rises",
  "Its price and profit rise",
  "Firms have an incentive to produce more",
  "Resources move into the good",
  "More of the good is produced",
], done: "A market answer." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm's profit per unit rises from $2 to $3 and it sells 100 units. What is the extra profit ($)?", a: 100, sol: "(3 − 2) × 100 = <b>$100</b>." },
  { q: "Production of a good rises from 80 to 100 units after a price rise. What is the percentage increase?", a: 25, sol: "20 ÷ 80 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the role of the price mechanism in a market economy?", opts: ["To plan production", "To allocate resources through price signals and incentives", "To set wages", "To tax goods"], a: 1, why: "Prices signal." },
  { q: "A rise in demand leads firms to produce more because of:", opts: ["Higher profit", "Lower prices", "Government orders", "Lower costs"], a: 0, why: "Incentive." },
  { q: "'For whom to produce' is decided mainly by:", opts: ["The government", "Willingness and ability to pay", "Luck", "Firms' size"], a: 1, why: "Income and price." },
  { q: "Rationing by price means:", opts: ["Scarce goods go to those who can pay", "Equal shares", "Free goods", "Government allocation"], a: 0, why: "Price allocates." },
  { q: "A weakness of the price mechanism is that it:", opts: ["Works too slowly", "Ignores external costs", "Is too cheap", "Has no incentives"], a: 1, why: "No account of pollution." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Price mechanism", "How prices adjust to allocate scarce resources."],
  ["Signalling function", "Prices tell producers and consumers where resources are wanted."],
  ["Incentive function", "Prices and profits encourage changes in behaviour."],
  ["Rationing function", "Prices allocate scarce goods to those willing and able to pay."],
  ["What to produce", "Decided by consumer demand and profit."],
  ["How to produce", "Decided by competition and relative factor prices."],
  ["For whom to produce", "Decided by ability to pay."],
  ["Profit", "Revenue minus costs."],
  ["External cost", "A cost to third parties, ignored by the market."],
] });
labP(); 
