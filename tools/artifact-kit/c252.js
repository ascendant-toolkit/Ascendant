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

Lib.stepper($("#stR"), { w: 760, h: 380, label: "Revenue after a rise in demand", base: { d: 0, s: 0 }, draw: (s) => {
  let o = shiftChart(s.d, s.s); const [q0, p0] = eq(0, 0), [q1, p1] = eq(s.d, s.s);
  o += SV.text(X(60), Y(104), "Old revenue: " + money(p0 * q0, 0), "sm bd");
  if (s.d !== 0) o += SV.text(X(60), Y(96), "New revenue: " + money(p1 * q1, 0), "lbl bd t2");
  return o;
}, steps: [
  { cap: "Starting equilibrium: price P, quantity Q. Revenue = P × Q.", s: { d: 0, s: 0 } },
  { cap: "Demand <b>increases</b>: both price and quantity rise, so <b>revenue rises</b> (P₁ × Q₁).", s: { d: 30, s: 0 } },
] });
Lib.stepper($("#stU"), { w: 760, h: 380, label: "Supply increase and sales", base: { d: 0, s: 0 }, draw: (s) => {
  let o = shiftChart(s.d, s.s); const [q0, p0] = eq(0, 0), [q1, p1] = eq(s.d, s.s);
  o += SV.text(X(60), Y(104), "Old revenue: " + money(p0 * q0, 0), "sm bd");
  if (s.s !== 0) o += SV.text(X(60), Y(96), "New revenue: " + money(p1 * q1, 0), "lbl bd t2");
  return o;
}, steps: [
  { cap: "Starting equilibrium.", s: { d: 0, s: 0 } },
  { cap: "A subsidy increases supply: the price <b>falls</b> but <b>sales rise</b>. Consumers benefit from lower prices.", s: { d: 0, s: 30 } },
] });
const IM = ["A change in market conditions shifts demand or supply", "The equilibrium price and quantity change", "Sales (quantity) and revenue change for producers", "Consumers pay more or less and buy more or less", "Firms may expand or cut production"];
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Impact of a change", base: { n: 0 }, draw: mkChain(IM, "--accent"), steps: chainSteps(["A change in <b>market conditions</b> shifts demand or supply.", "The <b>equilibrium price and quantity</b> change.", "<b>Sales and revenue</b> change for producers.", "<b>Consumers</b> pay more or less and buy more or less.", "Firms may <b>expand or cut production</b>."]) });

/* Lab 1: events */
const EV = [
  { n: "Incomes rise (normal good)", d: 25, s: 0 }, { n: "A health warning", d: -25, s: 0 }, { n: "A subsidy to producers", d: 0, s: 25 }, { n: "A tax on producers", d: 0, s: -25 },
  { n: "New technology", d: 0, s: 30 }, { n: "A drought", d: 0, s: -30 }, { n: "Demand and supply both rise", d: 20, s: 20 },
];
function labV() {
  if (!$("#va")) return;
  const e = EV[+$("#va").value], [q0, p0] = eq(0, 0), [q1, p1] = eq(e.d, e.s), r0 = p0 * q0, r1 = p1 * q1;
  $("#va1").textContent = "$" + money(p1, 0) + " (" + dirWord(p0, p1) + ")"; $("#va2").textContent = money(q1, 0) + " (" + dirWord(q0, q1) + ")"; $("#va3").textContent = money(r1, 0) + " (" + dirWord(r0, r1) + ")";
  $("#vav").textContent = `${e.n}: price ${dirWord(p0, p1)}, sales ${dirWord(q0, q1)}, revenue ${dirWord(r0, r1)} (from ${money(r0, 0)} to ${money(r1, 0)}). ${p1 < p0 ? "Consumers gain from lower prices." : p1 > p0 ? "Consumers pay more." : ""}`;
  $("#labV").innerHTML = shiftChart(e.d, e.s);
}
Lib.slider($("#g1"), { id: "va", label: "Choose an event (0 to 6)", min: 0, max: 6, step: 1, value: 0, fmt: (v) => EV[v].n, onInput: labV });
const WB = [
  { n: "Consumers", b: "Lower prices and more choice after a supply increase", c: "Higher prices and less choice after a supply decrease" },
  { n: "Producers", b: "Higher revenue after a demand increase; subsidies", c: "Taxes and higher costs; falling demand" },
  { n: "Workers", b: "More jobs when sales rise", c: "Job losses when sales fall" },
  { n: "Government", b: "More tax revenue when sales rise", c: "Pays subsidies; may lose tax revenue" },
];
button_table("wbBtns", "wbOut", WB, 0, (p) => `<div class="tw"><table class="t"><tr><th>Gains</th><th>Loses</th></tr><tr><td>${p.b}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>sales</b> (quantity)?", buckets: [{ label: "Sales rise" }, { label: "Sales fall" }], items: [
  { text: "Demand increases", b: 0 }, { text: "Supply increases", b: 0 }, { text: "A subsidy to producers", b: 0 }, { text: "New technology cuts costs", b: 0 },
  { text: "Demand decreases", b: 1 }, { text: "Supply decreases", b: 1 }, { text: "A tax on producers", b: 1 }, { text: "A drought", b: 1 },
], done: "Right shifts raise quantity; left shifts lower it." });
Lib.classify($("#cl2"), { prompt: "Who <b>benefits</b> from each?", buckets: [{ label: "Consumers" }, { label: "Producers" }], items: [
  { text: "A fall in price after supply increases", b: 0 }, { text: "More choice and lower prices", b: 0 },
  { text: "A rise in revenue after demand increases", b: 1 }, { text: "A subsidy that lowers costs", b: 1 },
], done: "Think about who gains from the change." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Revenue", "Price multiplied by quantity sold"],
  ["Sales", "The quantity sold"],
  ["Subsidy", "A payment to producers that lowers costs"],
  ["Indirect tax", "A tax that raises producers' costs"],
  ["Market conditions", "Factors that shift demand or supply"],
  ["New equilibrium", "The result of a shift"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a subsidy changes the market for solar panels</b>.", items: [
  "The government gives a subsidy to producers",
  "Costs fall: supply increases",
  "The price falls and the quantity rises",
  "Consumers buy more at a lower price",
  "Producers' sales rise",
], done: "A supply increase." });
Lib.calc($("#c1"), { qs: [
  { q: "Price is $50 and quantity is 50. What is the revenue ($)?", a: 2500, sol: "50 × 50 = <b>$2,500</b>." },
  { q: "After a rise in demand, price is $60 and quantity is 60. By how much does revenue rise ($) from $2,500?", a: 1100, sol: "60 × 60 = 3,600; 3,600 − 2,500 = <b>$1,100</b>." },
  { q: "After a supply increase, price is $40 and quantity is 60. By how much does revenue change ($) from $2,500? (enter the change)", a: -100, sol: "40 × 60 = 2,400; 2,400 − 2,500 = <b>−$100</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Total revenue is:", opts: ["Price + quantity", "Price × quantity", "Price − cost", "Quantity ÷ price"], a: 1, why: "Revenue = P × Q." },
  { q: "An increase in supply causes:", opts: ["Higher price, lower quantity", "Lower price, higher quantity", "Higher price, higher quantity", "No change"], a: 1, why: "Surplus at the old price." },
  { q: "A subsidy to producers:", opts: ["Raises prices", "Lowers costs and increases supply", "Reduces sales", "Shifts demand"], a: 1, why: "Lower costs." },
  { q: "After a rise in demand, producers' revenue:", opts: ["Rises", "Falls", "Is unchanged", "Is zero"], a: 0, why: "P and Q both rise." },
  { q: "Consumers gain from:", opts: ["A fall in supply", "An increase in supply", "A tax on producers", "A drought"], a: 1, why: "Lower prices." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Total revenue", "Price multiplied by quantity sold."],
  ["Sales", "The quantity of a good sold."],
  ["Market conditions", "Factors that shift demand or supply."],
  ["Subsidy", "A payment to producers that lowers costs."],
  ["Indirect tax", "A tax on goods that raises costs."],
  ["Consumer", "A buyer of goods and services."],
  ["Producer", "A seller or maker of goods and services."],
  ["New equilibrium", "The result of a shift in demand or supply."],
  ["Living standards", "The quality of life, linked to what people can buy."],
] });
labV(); 
