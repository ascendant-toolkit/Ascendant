/* ---------- model: demand (MPB) P = 100 - Q, private marginal cost MPC = 20 + 0.5Q. External cost / benefit $15 a unit in the animations ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 6.8, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
/* ---------- Lab 1: tax ---------- */
function lab1() {
  if (!$("#me") || !$("#tx")) return;
  const m = +$("#me").value, t = +$("#tx").value, q = (80 - t) / 1.5, qs = (80 - m) / 1.5, p = 100 - q;
  const loss = q > qs ? 0.5 * (q - qs) * (1.5 * q - 80 + m) : 0.5 * (qs - q) * (80 - 1.5 * q - m);
  $("#r1").textContent = Lib.fmtN(q, 1); $("#r2").textContent = Lib.fmtN(qs, 1); $("#r3").textContent = Lib.fmtN(Math.max(0, loss), 0); $("#r4").textContent = "$" + Lib.fmtN(t * q, 0);
  $("#rv").textContent = m === 0 ? "There is no external cost, so the free market is already efficient. Any tax creates a welfare loss."
    : Math.abs(t - m) < 0.5 ? "The tax equals the external cost: the externality is internalised, output is at the social optimum and the welfare loss is zero."
    : t < m ? `The tax ($${t}) is below the external cost ($${m}). Output is still above the optimum, so some overproduction and welfare loss remain.`
    : `The tax ($${t}) is above the external cost ($${m}). Output falls below the optimum, so there is now underproduction and a new welfare loss.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(qs), y(100 - qs)], [x(q), y(100 - q)], [x(q), y(20 + 0.5 * q + m)]], "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(70), "c3") + SV.line(x(0), y(20 + m), x(100), y(70 + m), "c2") + (t > 0 ? SV.line(x(0), y(20 + t), x(100), y(70 + t), "c4", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q), y(100 - q), 6, "dot1") + SV.circle(x(qs), y(100 - qs), 5, "dot3") + SV.text(x(q), 288, "Q", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "me", label: "External cost per unit ($): ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab1 });
Lib.slider($("#g2"), { id: "tx", label: "Tax per unit ($): ", min: 0, max: 30, step: 1, value: 0, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: subsidy ---------- */
function lab2() {
  if (!$("#mb") || !$("#sb")) return;
  const m = +$("#mb").value, s = +$("#sb").value, q = (80 + s) / 1.5, qs = (80 + m) / 1.5;
  const loss = q < qs ? 0.5 * (qs - q) * (80 + m - 1.5 * q) : 0.5 * (q - qs) * (1.5 * q - 80 - m);
  $("#s1").textContent = Lib.fmtN(q, 1); $("#s2").textContent = Lib.fmtN(qs, 1); $("#s3").textContent = Lib.fmtN(Math.max(0, loss), 0); $("#s4").textContent = "$" + Lib.fmtN(s * q, 0);
  $("#sv").textContent = m === 0 ? "There is no external benefit, so the free market is already efficient. A subsidy would cause overproduction."
    : Math.abs(s - m) < 0.5 ? "The subsidy equals the external benefit: output is at the social optimum and the welfare loss is zero."
    : s < m ? `The subsidy ($${s}) is below the external benefit ($${m}), so output is still too low.` : `The subsidy ($${s}) is above the external benefit ($${m}), so output overshoots the social optimum.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.2;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(q), y(20 + 0.5 * q)], [x(q), y(100 + m - q)], [x(qs), y(20 + 0.5 * qs)]], "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(100 + m), x(100), y(m), "c4") + SV.line(x(0), y(20), x(100), y(70), "c2") + (s > 0 ? SV.line(x(0), y(20 - s), x(100), y(70 - s), "c3", { "stroke-dasharray": "6 5" }) : "");
  o += SV.circle(x(q), y(100 - q), 6, "dot1") + SV.circle(x(qs), y(20 + 0.5 * qs), 5, "dot3") + SV.text(x(q), 288, "Q", "sm bd", { "text-anchor": "middle" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "mb", label: "External benefit per unit ($): ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab2 });
Lib.slider($("#g4"), { id: "sb", label: "Subsidy per unit ($): ", min: 0, max: 30, step: 1, value: 0, fmt: (v) => v, onInput: lab2 });

/* ---------- Watch: bargaining ---------- */
const BB = 280, HB = (v) => v * 1.4;
function barDraw(s) {
  let o = SV.line(60, BB, 740, BB) + SV.text(62, 24, "$", "sm");
  const grp = (x, dmg, k, lab) => {
    let g = "";
    if (k.a > 0) g += SV.rect(x, BB - HB(100) * k.a, 90, HB(100) * k.a, "f3", op(k.a)) + SV.text(x + 45, BB - HB(100) - 8, "$100", "lbl bd", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 45, BB + 18, "Factory gain", "sm", { "text-anchor": "middle", ...op(k.a) }) +
      SV.rect(x + 110, BB - HB(dmg) * k.a, 90, HB(dmg) * k.a, "f2", op(k.a)) + SV.text(x + 155, BB - HB(dmg) - 8, "$" + dmg, "lbl bd", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 155, BB + 18, "Resident damage", "sm", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 100, BB + 42, lab, "lbl bd", { "text-anchor": "middle", ...op(k.a) });
    if (k.r > 0) g += SV.rect(x + 205, BB - HB(100), 14, HB(100) - HB(dmg), "f1", op(k.r)) + SV.text(x + 226, BB - HB(80) + 4, "payments between $" + dmg + " and $100", "sm bd t1", { ...halo, ...op(k.r) });
    return g;
  };
  o += grp(70, 60, { a: s.a, r: s.r }, "Case A: damage $60");
  o += grp(430, 150, { a: s.b, r: 0 }, "Case B: damage $150");
  return o;
}
Lib.stepper($("#stCo"), { w: 780, h: 340, label: "A factory and a resident bargaining over pollution when the damage is smaller or larger than the factory's gain", base: { a: 0, r: 0, b: 0 }, draw: barDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Case A.</b> The factory gains <b>$100</b> from producing. The pollution does <b>$60</b> of damage to a resident. Production creates a net social gain of $40.", s: { a: 1 } },
  { cap: "<b>The resident holds the right to clean air.</b> The factory must pay to pollute. It will pay up to $100 and the resident will accept anything above $60, so a deal at any amount in between leaves <b>both better off</b>. For example $80 gives each a gain of $20.", s: { a: 1, r: 1 } },
  { cap: "<b>Case B.</b> Now the damage is <b>$150</b>, more than the factory's gain of $100. The resident would refuse any payment under $150, which the factory will not pay, so there is <b>no deal and the factory stops</b>. Again the outcome is efficient: production costs more than it is worth.", s: { a: 1, r: 1, b: 1 } },
  { cap: "<b>The catch.</b> This needs clear property rights, few people involved and low transaction costs. For pollution that affects thousands of people, negotiating is impractical, which is why governments often step in with taxes or regulation.", s: { a: 1, r: 1, b: 1 } },
] });

/* ---------- Lab 3: bargaining ---------- */
function lab8() {
  if (!$("#dmg") || !$("#gn")) return;
  const d = +$("#dmg").value, g = +$("#gn").value, deal = g > d;
  $("#y1").textContent = "$" + g; $("#y2").textContent = "$" + d; $("#y3").textContent = deal ? "$" + d + " to $" + g : "none"; $("#y4").textContent = deal ? "Yes" : "No";
  $("#yv").textContent = deal ? `The factory gains $${g} and the damage is $${d}, so there is room for a deal: any payment from $${d} to $${g} leaves both better off. Production goes ahead and the outcome is efficient (net gain $${g - d}).`
    : `The damage ($${d}) is at least the factory's gain ($${g}), so no payment satisfies both sides. The factory stops. This is also efficient, because production costs society more than it is worth.`;
  const H = (v) => 1.2 * v, base = 190;
  let o = SV.line(30, base, 400, base);
  [[60, g, "f3", "Factory gain"], [220, d, "f2", "Resident damage"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 210, l, "sm", { "text-anchor": "middle" }); });
  if (deal) o += SV.rect(165, base - H(g), 50, H(g) - H(d), "f1") + SV.text(190, base - H(g) - 24, "deal range", "sm bd t1", { "text-anchor": "middle" });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g13"), { id: "gn", label: "Factory's gain from producing ($): ", min: 50, max: 150, step: 10, value: 100, fmt: (v) => v, onInput: lab8 });
Lib.slider($("#g14"), { id: "dmg", label: "Damage to the resident ($): ", min: 0, max: 150, step: 10, value: 60, fmt: (v) => v, onInput: lab8 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which type of policy is each one?",
  buckets: [{ label: "Tax or subsidy" }, { label: "Regulation or ban" }, { label: "Information or persuasion" }, { label: "Property rights and bargaining" }, { label: "Tradable permits" }],
  items: [
    { text: "A per-flight tax on air travel", b: 0 }, { text: "A subsidy for electric cars", b: 0 }, { text: "A congestion charge", b: 0 },
    { text: "A limit on night flights", b: 1 }, { text: "Emission standards for factories", b: 1 }, { text: "A ban on smoking in public places", b: 1 },
    { text: "Negative advertising about flying", b: 2 }, { text: "Health warnings on cigarette packs", b: 2 },
    { text: "A resident and a factory agreeing a payment", b: 3 }, { text: "Giving a community ownership of a river", b: 3 },
    { text: "A cap on emissions with permits firms can trade", b: 4 },
  ], done: "Name the type, then weigh its costs and limits.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Internalise", "Make the decision-maker face the full social cost or benefit"],
  ["Tax equal to the external cost", "Shifts MPC up to MSC so output moves to the social optimum"],
  ["Subsidy equal to the external benefit", "Moves output up to the social optimum"],
  ["Property rights", "Legal ownership that lets people exclude others and be paid for use"],
  ["Transaction costs", "The costs of negotiating and enforcing an agreement"],
  ["Regulation", "Legal limits or bans on harmful activity"],
  ["Government failure", "Intervention that leaves resources less efficiently used"],
], done: "Seven words for policy on externalities." });
Lib.order($("#o1"), { prompt: "Put the analysis of a tax on air travel in order.", items: [
  "Airlines and passengers ignore the external cost of emissions and noise",
  "MSC is above MPC and the market overproduces flights at Qm",
  "A tax equal to the external cost per flight shifts MPC up to MSC",
  "The price rises and the number of flights falls to the social optimum Qs",
  "The welfare loss is removed and the externality is internalised",
  "Evaluate: the external cost is hard to measure, demand may be inelastic, and there may be effects on jobs and tourism",
], done: "A reliable structure for a 20 mark policy answer." });
Lib.calc($("#c1"), { qs: [
  { q: "The marginal external cost is $15 a unit. What per-unit tax would internalise it ($)?", a: 15, sol: "A tax equal to the marginal external cost: <b>$15</b>." },
  { q: "Demand is P = 100 − Q and MPC = 20 + 0.5Q. A tax of $15 shifts supply to 35 + 0.5Q. What is the new output (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives Q = <b>43.3</b>, the social optimum." },
  { q: "What is the government's tax revenue ($, nearest whole number)?", a: 650, tol: 1, sol: "15 × 43.3 = <b>$650</b>." },
  { q: "The tax is set too high at $30. What is the output (units, 1 decimal place)?", a: 33.3, tol: 0.1, sol: "100 − Q = 50 + 0.5Q gives Q = <b>33.3</b>, below the social optimum of 43.3." },
  { q: "A positive externality of $15 and a subsidy of $15 raise output to 63.3 units. What is the subsidy cost ($, nearest whole number)?", a: 950, tol: 1, sol: "15 × 63.3 = <b>$950</b>." },
  { q: "A factory gains $100 from producing and the damage is $60. What is the largest net gain available to be shared between them ($)?", a: 40, sol: "100 − 60 = <b>$40</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A tax set equal to the marginal external cost will:", opts: ["raise output above the optimum", "internalise the externality", "remove all costs", "have no effect on price"], a: 1, why: "It makes the producer face the full social cost." },
  { q: "Which makes bargaining without government more likely to work?", opts: ["Thousands of people affected", "Clear property rights and few parties", "High transaction costs", "No identifiable polluter"], a: 1, why: "Few parties, clear rights and low transaction costs make a deal easy." },
  { q: "A tax is above the external cost. Output will be:", opts: ["above the social optimum", "at the social optimum", "below the social optimum", "unchanged"], a: 2, why: "It overcorrects and creates a new welfare loss." },
  { q: "Which is a weakness of a tax on pollution?", opts: ["It raises revenue", "The external cost is hard to measure so the tax may be wrong", "It changes prices", "It affects incentives"], a: 1, why: "Setting the right level needs information the government may not have." },
  { q: "Which policy gives the most precise control over emissions?", opts: ["Information campaign", "Regulation or a ban", "A small tax", "Nothing"], a: 1, why: "A legal limit sets the quantity directly, though enforcement costs money." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Internalise an externality", "Make the decision-maker bear the full social cost or gain the full social benefit."],
  ["Tax for a negative externality", "A per-unit tax equal to the marginal external cost shifts MPC up to MSC."],
  ["Subsidy for a positive externality", "A per-unit subsidy equal to the marginal external benefit moves output to the social optimum."],
  ["Regulation", "Legal limits, standards or bans."],
  ["Tradable permits", "A cap on pollution with permits that can be traded."],
  ["Property rights", "Legal ownership that lets owners control and charge for use."],
  ["Bargaining", "Parties agree a payment instead of relying on the government."],
  ["Transaction costs", "The costs of negotiating and enforcing an agreement."],
  ["Information failure (policy)", "The external cost cannot be measured accurately, so a tax may be wrong."],
  ["Government failure", "Intervention that makes the allocation of resources worse or no better."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2025 · 32 · Q8] The marginal social benefit of consuming a drink is less than the marginal private benefit. What would be the best policy to improve resource allocation in this market?", opts: ["give a subsidy to the producers of the drink", "increase competition in the drink industry", "impose a maximum price for the drink above the market equilibrium price", "impose a per unit tax on the drink"], a: 3, why: "MSB < MPB means a negative consumption externality: the drink is over-consumed. A tax raises the price and cuts consumption." },
  { q: "[May/June 2025 · 31 · Q8] Good X is a popular product that creates a negative externality when it is consumed. The government wants to reduce the consumption of good X significantly. Under which circumstances is the government most likely to meet its aim?", opts: ["subsidy, price elasticity of demand more than 1", "subsidy, price elasticity of demand less than 1", "indirect tax, price elasticity of demand more than 1", "indirect tax, price elasticity of demand less than 1"], a: 2, why: "A tax raises price. Elastic demand (more than 1) means quantity falls by a larger percentage, so consumption falls significantly." },
  { q: "[May/June 2025 · 34 · Q10] Which policy by a government would increase the negative externalities that result from cigarette smoking?", opts: ["a ban on cigarette advertising", "a ban on cigarette smoking in public places", "a ban on substitutes for cigarettes", "a ban on the sale of cigarettes"], a: 2, why: "Banning substitutes keeps smokers buying cigarettes. A, B and D all aim to reduce smoking." },
  { q: "[May/June 2025 · 31 · Q10] To reduce traffic congestion, a government built a new highway. Some citizens responded by switching from public transport to private cars, which made car journeys take even longer. What can be concluded about government failure?", opts: ["It occurred because the government's opportunity costs were not considered.", "It occurred because the wishes of the majority of citizens were ignored.", "It occurred because the result was unintended.", "It occurred from over-reliance on the market system."], a: 2, why: "The extra traffic was an unintended consequence of the policy." },
  { q: "[Oct/Nov 2022 · 31 · Q15] Too many flights cause unnecessary damage to the environment. Which measure is most likely to result in the socially optimal number of flights?", opts: ["a complete ban on flights removing all private and external costs", "greater deregulation of the global airline industry", "publishing information to highlight the negative effects of flying on the environment", "the payment of a subsidy per passenger equal to the difference between the private and social benefit"], a: 2, why: "Information raises awareness of the external cost and moves choices towards the social optimum. A ban removes all flights, deregulation may increase them, and a subsidy raises flying." },
  { q: "[May/June 2025 · 32 · Q11] What is not an outcome of the existence of private property rights?", opts: ["They encourage private owners to conserve property when its value is expected to rise.", "They give private owners the incentive to manage their property carefully.", "They make private owners accountable for damage to others from property misuse.", "They prevent private owners gaining from using resources to benefit others."], a: 3, why: "Property rights let owners gain from using resources, including by benefiting others, so D is not an outcome." },
  { q: "[May/June 2025 · 34 · Q3] Why does the lack of property rights cause an inefficient allocation of resources?", opts: ["Scarce resources are depleted because the owner has sold them too cheaply.", "Scarce resources are depleted because they had zero cost to the users.", "Scarce resources are under-allocated to the provision of demerit goods.", "Scarce resources are under-allocated to the provision of merit goods."], a: 1, why: "If no one owns a resource, users pay nothing and it may be overused." },
] });
