/* ---------- model: demand P = 100 - Q, supply P = 20 + Q (equilibrium Q = 40, P = 60) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 7.5, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const marketLines = (s) => (s.d > 0 ? SV.line(X(0), Y(100), X(90), Y(10), "c1", op(s.d)) + SV.text(X(90) - 4, Y(10) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) : "") +
  (s.s > 0 ? SV.line(X(0), Y(20), X(80), Y(100), "c2", op(s.s)) + SV.text(X(80) - 4, Y(100) + 16, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) }) : "");
const eqMark = (s) => s.eq > 0 ? SV.line(X(40), Y(60), X(40), 330, "gr", op(s.eq)) + SV.line(70, Y(60), X(40), Y(60), "gr", op(s.eq)) + SV.circle(X(40), Y(60), 6, "dot3", op(s.eq)) + SV.text(66, Y(60) + 4, "60", "sm bd", { "text-anchor": "end", ...op(s.eq) }) + SV.text(X(40), 350, "40", "lbl bd", { "text-anchor": "middle", ...op(s.eq) }) : "";

/* indirect tax (Watch 3) */
function taxDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.tax > 0) o += SV.line(X(0), Y(40), X(80), Y(120), "c4", { "stroke-dasharray": "6 5", ...op(s.tax) }) + SV.text(X(60), Y(100) - 0, "S + tax $20", "lbl bd t4", { ...halo, ...op(s.tax) });
  if (s.res > 0) o += SV.rect(70, Y(70), X(30) - 70, Y(60) - Y(70), "f1", op(s.res)) + SV.rect(70, Y(60), X(30) - 70, Y(50) - Y(60), "f4", op(s.res)) +
    SV.poly([[X(30), Y(70)], [X(30), Y(50)], [X(40), Y(60)]], "f2", op(s.res)) + SV.line(X(30), Y(70), X(30), 330, "gr", op(s.res)) + SV.circle(X(30), Y(70), 6, "dot4", op(s.res)) + SV.circle(X(30), Y(50), 6, "dot4", op(s.res)) +
    SV.text(66, Y(70) + 4, "70", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(66, Y(50) + 4, "50", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(X(30), 350, "30", "lbl bd", { "text-anchor": "middle", ...op(s.res) }) +
    SV.text(X(15), Y(65) + 4, "paid by consumers $10", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(15), Y(55) + 4, "paid by producers $10", "lbl bd t4", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(30) + 12, Y(60) - 14, "welfare loss", "sm bd t2", { ...halo, ...op(s.res) });
  return o;
}
Lib.stepper($("#stC"), { w: 780, h: 370, label: "A per unit tax shifting supply up and the burden shared between consumers and producers", base: { d: 0, s: 0, eq: 0, tax: 0, res: 0 }, draw: taxDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The tax.</b> A tax of $20 on each unit sold raises every supplier's cost by $20, so the supply curve shifts <b>up by $20</b> (a vertical distance equal to the tax).", s: { d: 1, s: 1, eq: 0.6, tax: 1 } },
  { cap: "<b>The new equilibrium.</b> Consumers now pay <b>$70</b> and quantity falls to <b>30</b>. Producers receive $70 − $20 = <b>$50</b> after paying the tax. Each side bears $10 of the $20: the burden is shared equally here because demand and supply have equal slopes.", s: { d: 1, s: 1, eq: 0.6, tax: 1, res: 1 } },
  { cap: "<b>Tax revenue</b> is $20 × 30 = <b>$600</b>. The red triangle is the <b>welfare loss</b> from the fall in output, the units between 30 and 40 that were worth more than they cost. If the tax is set equal to an external cost, this loss is more than offset by correcting the externality.", s: { d: 1, s: 1, eq: 0.6, tax: 1, res: 1 } },
] });

/* subsidy (Watch 2) */
function subDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.sub > 0) o += SV.line(X(0), Y(0), X(80), Y(80), "c3", { "stroke-dasharray": "6 5", ...op(s.sub) }) + SV.text(X(68), Y(68) + 22, "S − subsidy $20", "lbl bd t3", { ...halo, ...op(s.sub) });
  if (s.res > 0) o += SV.rect(70, Y(60), X(50) - 70, Y(50) - Y(60), "f1", op(s.res)) + SV.rect(70, Y(70), X(50) - 70, Y(60) - Y(70), "f4", op(s.res)) + SV.line(X(50), Y(70), X(50), 330, "gr", op(s.res)) +
    SV.circle(X(50), Y(50), 6, "dot1", op(s.res)) + SV.circle(X(50), Y(70), 6, "dot4", op(s.res)) + SV.text(66, Y(70) + 4, "70", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(66, Y(50) + 4, "50", "sm bd", { "text-anchor": "end", ...op(s.res) }) + SV.text(X(50), 350, "50", "lbl bd", { "text-anchor": "middle", ...op(s.res) }) +
    SV.text(X(25), Y(55) + 4, "consumers gain $10 a unit", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.res) }) + SV.text(X(25), Y(65) + 4, "producers gain $10 a unit", "lbl bd t4", { "text-anchor": "middle", ...halo, ...op(s.res) });
  return o;
}
Lib.stepper($("#stS"), { w: 780, h: 370, label: "A per unit subsidy shifting supply down and the gain shared between consumers and producers", base: { d: 0, s: 0, eq: 0, sub: 0, res: 0 }, draw: subDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The subsidy.</b> A payment of $20 on each unit lowers every supplier's cost by $20, so the supply curve shifts <b>down by $20</b>.", s: { d: 1, s: 1, eq: 0.6, sub: 1 } },
  { cap: "<b>The new equilibrium.</b> Quantity rises to <b>50</b>. Consumers pay <b>$50</b>, a fall of $10. Producers receive $50 + $20 = <b>$70</b>, a rise of $10. Each side gains half of the subsidy here because demand and supply have equal slopes.", s: { d: 1, s: 1, eq: 0.6, sub: 1, res: 1 } },
  { cap: "<b>The cost to the government</b> is $20 × 50 = <b>$1000</b>, paid by taxpayers. For a good with a positive externality, the extra output moves the market towards the social optimum.", s: { d: 1, s: 1, eq: 0.6, sub: 1, res: 1 } },
] });

/* permits (Watch 3) */
function permDraw(s) {
  const base = 250, H = (v) => v * 4;
  let o = SV.line(60, base, 740, base) + SV.text(62, 24, "Cost ($)", "sm");
  [["Firm A", 110, 10, -5], ["Firm B", 330, 40, 25], ["Total", 550, 50, 20]].forEach(([l, x, n, t]) => {
    if (s.n > 0) { const h = H(n) * s.n; o += SV.rect(x, base - h, 70, h, "f2", op(s.n)) + SV.text(x + 35, base - h - 6, "$" + n, "lbl bd", { "text-anchor": "middle", ...op(s.n) }) + SV.text(x + 35, 304, "No trading", "sm", { "text-anchor": "middle", ...op(s.n) }); }
    if (s.t > 0) { const h = H(Math.abs(t)) * s.t, up = t >= 0; o += SV.rect(x + 80, up ? base - h : base, 70, h, "f3", op(s.t)) + SV.text(x + 115, up ? base - h - 6 : base + h + 16, (t < 0 ? "−" : "") + "$" + Math.abs(t), "lbl bd", { "text-anchor": "middle", ...op(s.t) }) + SV.text(x + 115, 304, "Trading at $5", "sm", { "text-anchor": "middle", ...op(s.t) }); }
    o += SV.text(x + 75, 332, l, "lbl bd", { "text-anchor": "middle" });
  });
  return o;
}
Lib.stepper($("#stP"), { w: 780, h: 345, label: "Costs of cutting pollution for two firms with and without permit trading", base: { n: 0, t: 0 }, draw: permDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The cap.</b> Each firm emits 10 units. The government wants no more than 10 in total, so it issues <b>5 permits to each firm</b>.", s: { n: 0, t: 0 } },
  { cap: "<b>No trading.</b> Each firm must cut 5 units. A pays 5 × $2 = $10, B pays 5 × $8 = $40: a total cost of <b>$50</b>.", s: { n: 1, t: 0 } },
  { cap: "<b>Trading at $5.</b> A cuts all 10 units for $20 and sells 5 spare permits for $25, so its net cost is <b>−$5</b>. B buys 5 permits for $25 instead of cutting its own pollution at $8 a unit.", s: { n: 1, t: 1 } },
  { cap: "<b>The same cap, a lower cost.</b> The real cost of cutting falls from $50 to <b>$20</b>, a saving of $30, because cuts are made where they are cheapest. Both firms are better off than with no trading.", s: { n: 1, t: 1 } },
] });
/* ---------- Lab 2: tax incidence ---------- */
function lab2() {
  if (!$("#tx") || !$("#kk")) return;
  const t = +$("#tx").value, k = +$("#kk").value, q0 = 80 / (1 + k), p0 = 100 - q0, q1 = (80 - t) / (1 + k), pc = 100 - q1, pp = pc - t;
  $("#s1").textContent = "$" + Lib.fmtN(pc, 1); $("#s2").textContent = "$" + Lib.fmtN(pp, 1); $("#s3").textContent = t === 0 ? "–" : Math.round(((pc - p0) / t) * 100) + "%"; $("#s4").textContent = "$" + Lib.fmtN(t * q1, 0);
  $("#sv").textContent = t === 0 ? "No tax: the market is at its equilibrium."
    : k < 0.9 ? `Supply is flat (elastic). Producers can cut output easily, so most of the tax is passed on: consumers pay $${Lib.fmtN(pc - p0, 1)} of the $${t}. Quantity falls from ${Lib.fmtN(q0, 1)} to ${Lib.fmtN(q1, 1)}.`
    : k > 1.1 ? `Supply is steep (inelastic). Producers cannot adjust output easily, so they bear most of the tax: consumers pay $${Lib.fmtN(pc - p0, 1)} of the $${t}.`
    : `Supply and demand have equal slopes, so the tax is shared equally: consumers pay $${Lib.fmtN(pc - p0, 1)} and producers $${Lib.fmtN(p0 - pp, 1)}.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, y(pc), x(q1) - 40, y(p0) - y(pc), "f1") + SV.rect(40, y(p0), x(q1) - 40, y(pp) - y(p0), "f4");
  const sy = (q, add) => 20 + add + k * q;
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(Math.min(100, 80 / k)), y(sy(Math.min(100, 80 / k), 0)), "c2") + (t > 0 ? SV.line(x(0), y(20 + t), x(Math.min(100, (100 - 20 - t) / k)), y(sy(Math.min(100, (100 - 20 - t) / k), t)), "c4", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q1), y(pc), 6, "dot1") + SV.circle(x(q1), y(pp), 6, "dot4") + SV.text(x(q1) + 10, y(pc) - 6, "consumers pay", "sm bd t1") + SV.text(x(q1) + 10, y(pp) + 16, "producers receive", "sm bd t4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "tx", label: "Tax per unit ($): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g3"), { id: "kk", label: "Supply steepness (1 = same as demand): ", min: 0.25, max: 4, step: 0.25, value: 1, fmt: (v) => Lib.fmtN(v, 2), onInput: lab2 });

/* ---------- Lab 3: permits ---------- */
function lab3() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, trade = p > 2 && p < 8, a = trade ? 20 - 5 * p : 10, b = trade ? 5 * p : 40, tot = trade ? 20 : 50;
  $("#t1").textContent = "$" + Lib.fmtN(a, 1); $("#t2").textContent = "$" + Lib.fmtN(b, 1); $("#t3").textContent = "$" + tot;
  $("#tv").textContent = trade ? `At $${p} a permit, A abates all 10 units (cost $20) and sells 5 permits for $${Lib.fmtN(5 * p, 1)}. B buys them instead of cutting its own pollution. The cap of 10 is still met, but the real cost falls from $50 to $20 and both firms gain: a saving of $30 shared out by the permit price.`
    : p <= 2 ? "At $2 or less, A will not sell permits (it costs A $2 to cut a unit, so the permit must fetch more than that). No trade: each firm cuts 5 units, costing $50 in all."
    : "At $8 or more, B will not buy (it is cheaper for B to cut a unit at $8). No trade: each firm cuts 5 units, costing $50 in all.";
  const H = (v) => 150 * (v / 50), bw = 70;
  let o = SV.line(30, 190, 400, 190) + SV.text(32, 22, "Cost ($)", "sm");
  [[40, a, "f1", "Firm A net"], [140, b, "f4", "Firm B net"], [240, tot, trade ? "f3" : "f2", "Total real cost"]].forEach(([x, v, c, l]) => { const up = v >= 0, h = Math.abs(H(v)); o += SV.rect(x, up ? 190 - h : 190, bw, h, c) + SV.text(x + bw / 2, up ? 190 - h - 6 : 190 + h + 14, (up ? "" : "−") + "$" + Lib.fmtN(Math.abs(v), 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 236, l, "sm", { "text-anchor": "middle" }); });
  o += SV.line(240, 190 - H(50), 240 + bw, 190 - H(50), "gr", { "stroke-dasharray": "4 3" }) + SV.text(240 + bw + 6, 190 - H(50) + 4, "no trade: 50", "sm");
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "pp", label: "Permit price ($): ", min: 0, max: 10, step: 0.5, value: 5, fmt: (v) => v, onInput: lab3 });

/* ---------- Lab 3: subsidy ---------- */
function lab6() {
  if (!$("#sb")) return;
  const s = +$("#sb").value, q = (80 + s) / 2, pc = 100 - q, pp = pc + s, cost = s * q;
  $("#b1").textContent = "$" + Lib.fmtN(pc, 1); $("#b2").textContent = "$" + Lib.fmtN(pp, 1); $("#b3").textContent = Lib.fmtN(q, 1); $("#b4").textContent = "$" + Lib.fmtN(cost, 0);
  $("#bv").textContent = s === 0 ? "No subsidy: the market is at its equilibrium of $60 and 40 units."
    : `Consumers pay $${Lib.fmtN(pc, 1)}, $${Lib.fmtN(60 - pc, 1)} less than before, and producers receive $${Lib.fmtN(pp, 1)}, $${Lib.fmtN(pp - 60, 1)} more. Output rises from 40 to ${Lib.fmtN(q, 1)}. The government pays ${s} on each of ${Lib.fmtN(q, 1)} units: $${Lib.fmtN(cost, 0)}.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, y(60), x(q) - 40, y(pc) - y(60), "f1") + SV.rect(40, y(pp), x(q) - 40, y(60) - y(pp), "f4");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + (s > 0 ? SV.line(x(0), y(20 - s), x(80), y(100 - s), "c3", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q), y(pc), 6, "dot1") + SV.circle(x(q), y(pp), 6, "dot4") + SV.text(x(q) + 10, y(pc) + 16, "consumers pay", "sm bd t1") + SV.text(x(q) + 10, y(pp) - 6, "producers receive", "sm bd t4");
  $("#labF").innerHTML = o;
}
Lib.slider($("#g7"), { id: "sb", label: "Subsidy per unit ($): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: lab6 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which tool fits each problem best?",
  buckets: [{ label: "Indirect tax" }, { label: "Subsidy" }, { label: "Tradable permits" }],
  items: [
    { text: "Cigarettes (a demerit good)", b: 0 }, { text: "Plastic bags", b: 0 }, { text: "Fuel with a carbon cost", b: 0 },
    { text: "Vaccinations (positive externality)", b: 1 }, { text: "Rooftop solar panels", b: 1 }, { text: "Public transport use", b: 1 },
    { text: "Power stations with a fixed national limit on emissions", b: 2 }, { text: "Factories that can cut pollution at very different costs", b: 2 },
  ], done: "Tax and permits for negative externalities, subsidy for positive ones.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Indirect tax", "A tax on spending that raises the cost of supply"],
  ["Specific tax", "A fixed amount per unit"],
  ["Ad valorem tax", "A percentage of the price"],
  ["Tax incidence", "How the burden of a tax is shared between buyers and sellers"],
  ["Subsidy", "A payment that lowers the cost of supply or consumption"],
  ["Tradable permits", "A cap on pollution with permits that firms can buy and sell"],
  ["Internalise an externality", "Make the decision maker pay the external cost"],
], done: "Seven words that cover the price tools." });
Lib.order($("#o1"), { prompt: "Put the explanation of a per-unit tax in order.", items: [
  "The government imposes a tax per unit on producers",
  "Costs of supply rise by the amount of the tax, so the supply curve shifts up",
  "The market price rises and the equilibrium quantity falls",
  "The burden is shared between consumers and producers, depending on elasticities",
  "The government collects revenue equal to the tax times the new quantity",
  "Evaluate: elasticity, whether the tax equals the external cost, and who is hit hardest",
], done: "This chain works for any indirect tax question." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and supply is P = 20 + Q. A $20 tax shifts supply to P = 40 + Q. What is the new quantity?", a: 30, sol: "100 − Q = 40 + Q gives Q = <b>30</b>." },
  { q: "What is the government's tax revenue ($)?", a: 600, sol: "20 x 30 = <b>$600</b>." },
  { q: "The price consumers pay rises from $60 to $70. What share of the $20 tax do consumers bear (%)?", a: 50, sol: "10 ÷ 20 x 100 = <b>50%</b>." },
  { q: "A $20 subsidy shifts supply to P = Q. What is the new quantity?", a: 50, sol: "100 − Q = Q gives Q = <b>50</b>." },
  { q: "What is the cost of the subsidy to the government ($)?", a: 1000, sol: "20 x 50 = <b>$1000</b>." },
  { q: "What price do producers receive after the subsidy ($)?", a: 70, hint: "Consumers pay 50. Add the subsidy.", sol: "50 + 20 = <b>$70</b>." },
  { q: "Without trading each firm cuts 5 units: A at $2 and B at $8 a unit. With trading A cuts all 10 units. By how much does the total cost fall ($)?", a: 30, sol: "Before: 5 x 2 + 5 x 8 = 50. After: 10 x 2 = 20. Fall = <b>$30</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An indirect tax shifts the supply curve:", opts: ["up by the amount of the tax", "down by the amount of the tax", "to the right", "not at all"], a: 0, why: "The tax is a cost to producers, so supply moves up (to the left)." },
  { q: "A per-unit tax on a good with inelastic demand will mostly:", opts: ["cut quantity sharply", "raise the price paid by consumers and cut quantity little", "reduce the price paid by consumers", "have no effect on government revenue"], a: 1, why: "Consumers bear most of the burden and quantity changes little." },
  { q: "A subsidy to producers:", opts: ["raises price and lowers quantity", "lowers price and raises quantity", "lowers price and quantity", "has no effect on price"], a: 1, why: "Supply shifts down, so price falls and quantity rises." },
  { q: "Tradable pollution permits are most likely to:", opts: ["remove the cap on emissions", "meet a pollution cap at lower total cost", "raise emissions", "make permits free for ever"], a: 1, why: "Firms with low abatement costs cut more and sell permits." },
  { q: "The best reason for a tax set equal to the external cost is that it:", opts: ["raises more revenue than any other", "makes the decision maker pay the full cost", "stops all pollution", "has no effect on prices"], a: 1, why: "It internalises the externality." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indirect tax", "A tax on spending, which shifts supply up by the amount of the tax."],
  ["Specific tax", "A fixed amount per unit sold."],
  ["Ad valorem tax", "A percentage of the price."],
  ["Subsidy", "A payment that lowers firms' costs, shifting supply down."],
  ["Tax incidence", "Who actually bears the burden of a tax, decided by elasticities."],
  ["Tax revenue", "Tax per unit times quantity sold after the tax."],
  ["Internalise", "Make the producer or consumer pay the external cost."],
  ["Tradable permits", "A cap on total pollution with permits that can be traded."],
  ["Abatement cost", "The cost of reducing a unit of pollution."],
  ["Regressive tax", "Takes a larger share of income from low earners."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2024 · 32 · Q11] A government wishes to use market forces to remove a negative externality in the consumption of a good. Which policy is likely to be the most effective?", opts: ["It should provide information about the undesirable side-effects of the good.", "It should give producers a subsidy, to allow consumers to purchase the product more cheaply.", "It should impose an indirect tax on consumers, to reduce consumption to the socially efficient level.", "It should not interfere at all, to allow the free market to generate maximum efficiency."], a: 2, why: "A tax uses the price mechanism (market forces) to cut consumption to the efficient level. A subsidy would raise it." },
  { q: "[Feb/March 2025 · 32 · Q10] What is not a reason for imposing a tax on producers based on the amount of pollution caused in the production process?", opts: ["Firms have a financial incentive to reduce pollution.", "It is relatively hard to administer and monitor this tax scheme.", "Some firms cause less pollution than others.", "Taxes on pollution reduce negative production externalities."], a: 1, why: "Difficulty of administration is a drawback, not a reason for the tax. A, C and D are arguments in its favour." },
  { q: "[Feb/March 2025 · 32 · Q11] A government introduced a tax on soft drinks containing sugar. It was forecast that the tax would raise £520m per year, but the tax received was £240m. What is the most likely reason why the tax collected was lower than forecast?", opts: ["a specific tax instead of an ad valorem tax was introduced", "fewer drinks than originally forecast contained sugar", "most retailers did not increase the price of soft drinks", "the demand for soft drinks was price inelastic"], a: 1, why: "If firms reduced the sugar in their drinks, fewer products were taxed. Inelastic demand would have kept revenue high." },
  { q: "[Feb/March 2022 · 32 · Q13] A government wishes to reduce the negative externalities caused by the use of coal. Which policy should the government use?", opts: ["Impose an indirect tax on the production of hydroelectric power.", "Increase income tax.", "Remove any restrictions on coal production.", "Subsidise wind-powered electricity production."], a: 3, why: "Subsidising a cleaner substitute reduces the use of coal. A and C would increase or not change the use of coal." },
  { q: "[May/June 2022 · 31 · Q14] A government issues free non-tradeable pollution permits to firms. In a change in legislation, the permits can be traded with other firms. What will be the impact on the profits of the firms that are now buyers or sellers of the permits?", opts: ["buyers decrease, sellers decrease", "buyers decrease, sellers increase", "buyers increase, sellers decrease", "buyers increase, sellers increase"], a: 1, why: "Buyers now pay for permits they used to receive free, so their profit falls; sellers earn revenue from permits they no longer need." },
  { q: "[May/June 2022 · 32 · Q13] To reduce road congestion caused by parked cars, a local government introduced a system of tradable parking permits. Households were given a permit allowing them to park one car. Households with more than one car could buy extra permits from households with no cars. What is the most likely reason for this policy to fail?", opts: ["Fines for drivers parking without a permit will internalise the externality.", "The local government has a monopoly over the issue of parking permits.", "Those suffering from too many parked cars are compensated by the households owning extra cars.", "Too many households own cars so the market in permits is very small."], a: 3, why: "A permit market needs buyers and sellers. If few households have spare permits to sell, trading cannot work well." },
] });
