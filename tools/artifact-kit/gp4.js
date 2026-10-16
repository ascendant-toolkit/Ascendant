/* ---------- model: demand P = 100 - Q, supply P = 20 + Q (equilibrium Q = 40, P = 60) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 7.5, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const marketLines = (s) => (s.d > 0 ? SV.line(X(0), Y(100), X(90), Y(10), "c1", op(s.d)) + SV.text(X(90) - 4, Y(10) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) : "") +
  (s.s > 0 ? SV.line(X(0), Y(20), X(80), Y(100), "c2", op(s.s)) + SV.text(X(80) - 4, Y(100) + 16, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) }) : "");
const eqMark = (s) => s.eq > 0 ? SV.line(X(40), Y(60), X(40), 330, "gr", op(s.eq)) + SV.line(70, Y(60), X(40), Y(60), "gr", op(s.eq)) + SV.circle(X(40), Y(60), 6, "dot3", op(s.eq)) + SV.text(66, Y(60) + 4, "60", "sm bd", { "text-anchor": "end", ...op(s.eq) }) + SV.text(X(40), 350, "40", "lbl bd", { "text-anchor": "middle", ...op(s.eq) }) : "";


/* ---------- wrong tax (Watch) : D = 100 - Q, MPC = 20 + 0.5Q, external cost 15 ---------- */
const GX = (q) => 70 + q * 7, GY = (p) => 330 - p * 3;
function wrongDraw(s) {
  let o = axes() + SV.line(GX(0), GY(100), GX(88), GY(12), "c1", op(s.d)) + SV.line(GX(0), GY(20), GX(88), GY(64), "c2", op(s.d)) +
    SV.text(GX(88) + 6, GY(12) + 4, "D = MSB", "lbl bd t1", op(s.d)) + SV.text(GX(88) + 6, GY(64) + 4, "S = MPC", "lbl bd t2", op(s.d));
  if (s.eq > 0) o += SV.line(GX(53.3), GY(46.7), GX(53.3), 330, "gr", op(s.eq)) + SV.line(70, GY(46.7), GX(53.3), GY(46.7), "gr", op(s.eq)) + SV.circle(GX(53.3), GY(46.7), 6, "dot3", op(s.eq)) + SV.text(GX(53.3), 350, "53", "lbl bd", { "text-anchor": "middle", ...op(s.eq) });
  if (s.msc > 0) o += SV.line(GX(0), GY(35), GX(88), GY(79), "c3", { "stroke-width": 2.5, ...op(s.msc) }) + SV.text(GX(88) + 6, GY(79) + 4, "MSC", "lbl bd t3", op(s.msc)) +
    SV.line(GX(43.3), GY(56.7), GX(43.3), 330, "gr", op(s.msc)) + SV.circle(GX(43.3), GY(56.7), 6, "dot1", op(s.msc)) + SV.text(GX(43.3), 350, "43", "lbl bd", { "text-anchor": "middle", ...op(s.msc) });
  if (s.l1 > 0) o += SV.poly([[GX(43.3), GY(56.7)], [GX(53.3), GY(46.7)], [GX(53.3), GY(61.7)]], "f2", op(s.l1)) + SV.text(GX(53.3) + 12, GY(46.7) + 16, "welfare loss 75", "lbl bd t2", { ...halo, ...op(s.l1) });
  if (s.t30 > 0) o += SV.line(GX(0), GY(50), GX(88), GY(94), "c4", { "stroke-dasharray": "6 5", ...op(s.t30) }) + SV.text(GX(88) + 6, GY(94) + 4, "S + tax $30", "lbl bd t4", op(s.t30)) + SV.line(GX(33.3), GY(66.7), GX(33.3), 330, "gr", op(s.t30)) + SV.circle(GX(33.3), GY(66.7), 6, "dot4", op(s.t30)) + SV.text(GX(33.3), 350, "33", "lbl bd", { "text-anchor": "middle", ...op(s.t30) });
  if (s.l2 > 0) o += SV.poly([[GX(33.3), GY(51.7)], [GX(33.3), GY(66.7)], [GX(43.3), GY(56.7)]], "f2", op(s.l2)) + SV.text(GX(33.3) - 10, GY(51.7) + 22, "loss 75", "lbl bd t2", { "text-anchor": "end", ...halo, ...op(s.l2) });
  return o;
}
Lib.stepper($("#stG"), { w: 780, h: 370, label: "A tax set too low, correctly and too high compared with the external cost", base: { d: 0, eq: 0, msc: 0, l1: 0, t30: 0, l2: 0 }, draw: wrongDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market</b> ignores the external cost. Demand meets private marginal cost at <b>53 units</b> and $46.67.", s: { d: 1, eq: 1 } },
  { cap: "<b>The social optimum.</b> Adding the external cost of $15 gives marginal social cost (MSC). It meets demand at <b>43 units</b>. The market overproduces by 10 units, and the triangle is a <b>welfare loss of 75</b>.", s: { d: 1, eq: 1, msc: 1, l1: 1 } },
  { cap: "<b>The right tax.</b> A tax of exactly $15 shifts supply up to the MSC curve. Output falls to 43 and the welfare loss is removed. This needs the government to know the external cost exactly.", s: { d: 1, eq: 0.4, msc: 1, l1: 0.2 } },
  { cap: "<b>A tax set too high.</b> Suppose the government overestimates the external cost and taxes at $30. Output falls to <b>33</b>, below the optimum, and there is a new welfare loss, again <b>75</b>.", s: { d: 1, eq: 0.4, msc: 1, l1: 0, t30: 1, l2: 1 } },
  { cap: "<b>Government failure.</b> The over-tax leaves society no better off than doing nothing, because of poor information. A tax between about $0 and $30 would reduce the loss; one above $30 is worse than no tax.", s: { d: 1, eq: 0.4, msc: 1, l1: 0, t30: 1, l2: 1 } },
] });
/* ---------- Lab 4: getting the tax right ---------- */
function lab4() {
  if (!$("#ge")) return;
  const e = +$("#ge").value, q = (80 - e) / 1.5, qs = 65 / 1.5;
  const loss = q > qs ? 0.5 * (q - qs) * (1.5 * q - 65) : 0.5 * (qs - q) * (65 - 1.5 * q), better = loss < 74.9;
  $("#u1").textContent = Lib.fmtN(q, 1); $("#u2").textContent = Lib.fmtN(loss, 0); $("#u3").textContent = Math.abs(loss - 75) < 0.5 ? "Same" : better ? "Yes" : "No: worse";
  $("#uv").textContent = e === 15 ? "The estimate equals the true external cost ($15): output is at the social optimum and the welfare loss is zero."
    : e === 0 ? "No tax. Output is above the optimum and the welfare loss is 75."
    : e < 15 ? `The tax ($${e}) is too low. Output is still above the optimum, but the loss is smaller than with no tax.`
    : better ? `The tax ($${e}) is too high. It overcorrects: output is now below the optimum. The loss is still less than doing nothing.`
    : `The tax ($${e}) is far too high. It cuts output well below the social optimum, and the welfare loss ($${Lib.fmtN(loss, 0)}) is greater than doing nothing. This is government failure caused by poor information.`;
  const H = (v) => 170 * (v / 300), bw = 90;
  let o = SV.line(30, 200, 400, 200) + SV.text(32, 22, "Welfare loss", "sm");
  [[60, 75, "f2", "No tax"], [210, loss, better ? "f3" : "f4", "With the government's tax"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 200 - H(v), bw, H(v), c) + SV.text(x + bw / 2, 200 - H(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 218, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "ge", label: "Government's estimate of the external cost ($): ", min: 0, max: 45, step: 1, value: 25, fmt: (v) => v, onInput: lab4 });

/* ---------- Lab 2: is it worth it ---------- */
function labW() {
  if (!$("#wl") || !$("#ws") || !$("#wc")) return;
  const L = +$("#wl").value, sh = +$("#ws").value / 100, c = +$("#wc").value, rem = L * sh, net = rem - c;
  $("#w1").textContent = Math.round(rem); $("#w2").textContent = c; $("#w3").textContent = (net >= 0 ? "+" : "−") + Math.abs(Math.round(net));
  $("#wv").textContent = net > 0.5 ? `The policy removes ${Math.round(rem)} of welfare loss and costs ${c}, so society gains ${Math.round(net)}. Intervention is justified here.`
    : net < -0.5 ? `The policy removes ${Math.round(rem)} but costs ${c}: society loses ${Math.abs(Math.round(net))}. This is government failure, even though the market failure is real.`
    : "The benefit equals the cost: the policy is not clearly worthwhile.";
  const H = (v) => 150 * (v / 250);
  let o = SV.line(30, 200, 400, 200);
  [[60, rem, "f3", "Loss removed"], [210, c, net >= 0 ? "f4" : "f2", "Cost of policy"]].forEach(([x, v, col, l]) => { o += SV.rect(x, 200 - H(v), 100, H(v), col) + SV.text(x + 50, 200 - H(v) - 8, Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labI").innerHTML = o;
}
Lib.slider($("#g11"), { id: "wl", label: "Size of the market failure (welfare loss): ", min: 0, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labW });
Lib.slider($("#g12"), { id: "ws", label: "Share the policy removes: ", min: 0, max: 100, step: 10, value: 60, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g13"), { id: "wc", label: "Cost of running the policy: ", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labW });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which cause of government failure does each example show?",
  buckets: [{ label: "Poor information" }, { label: "Time lags" }, { label: "Unintended consequences" }, { label: "Cost of administration" }, { label: "Political pressure" }],
  items: [
    { text: "The external cost cannot be measured, so the tax is set wrongly", b: 0 }, { text: "The government does not know firms' true costs when setting a price cap", b: 0 },
    { text: "Years pass between spotting a problem and the law taking effect", b: 1 }, { text: "A policy fits last year's conditions, not this year's", b: 1 },
    { text: "A tax on rubbish leads to fly-tipping", b: 2 }, { text: "Subsidised fuel is mostly used by richer households", b: 2 },
    { text: "Inspectors are needed to check every factory", b: 3 }, { text: "Running a permit market needs monitoring staff", b: 3 },
    { text: "Firms lobby for weaker standards", b: 4 }, { text: "A policy is chosen for votes, not efficiency", b: 4 },
  ], done: "Name the cause, then give an example from the question.",
});
Lib.classify($("#cl2"), {
  prompt: "Which market failure does each policy best fit?",
  buckets: [{ label: "Negative externality" }, { label: "Merit good / positive externality" }, { label: "Public good" }, { label: "Monopoly power" }, { label: "Information failure" }],
  items: [
    { text: "A per-unit tax on pollution", b: 0 }, { text: "Tradable emission permits", b: 0 },
    { text: "A subsidy for vaccination", b: 1 }, { text: "Free state education", b: 1 },
    { text: "Street lighting provided by the local authority", b: 2 }, { text: "National defence funded by taxation", b: 2 },
    { text: "A price cap on a water monopoly", b: 3 }, { text: "Breaking up a cartel", b: 3 },
    { text: "Compulsory nutrition labels", b: 4 }, { text: "An advertising campaign on the risks of smoking", b: 4 },
  ], done: "Match the tool to the cause, then weigh it against its costs and government failure.",
});

Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Government failure", "Intervention that leaves resources less efficiently used"],
  ["Market failure", "When the market leaves resources allocated inefficiently"],
  ["Time lag", "Delay between a problem arising and a policy taking effect"],
  ["Unintended consequence", "A side effect that the policy-maker did not plan for"],
  ["Regulatory capture", "When the regulator ends up serving the firms it regulates"],
  ["Mixed economy", "An economy with both market forces and government intervention"],
  ["Regressive", "Takes a larger share of income from low earners"],
], done: "Seven words for evaluating policy." });
Lib.order($("#o1"), { prompt: "Put the evaluation of a policy in order.", items: [
  "Identify the market failure and the policy aimed at it",
  "Explain how the policy should work and what it changes",
  "Consider how well it fits the cause and how large the effect is",
  "Weigh the costs: administration, side effects, who pays",
  "Consider information, time lags and alternatives",
  "Reach a judgement comparing market failure with government failure",
], done: "A reliable structure for policy evaluation." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and private marginal cost is P = 20 + 0.5Q. What output does the free market produce (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives 1.5Q = 80, Q = <b>53.3</b>." },
  { q: "The external cost is $15, so MSC = 35 + 0.5Q. What is the socially optimal output (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives 1.5Q = 65, Q = <b>43.3</b>." },
  { q: "The welfare loss from the free market is a triangle with base 10 (53.3 − 43.3) and height 15. What is its area?", a: 75, sol: "0.5 x 10 x 15 = <b>75</b>." },
  { q: "The government wrongly sets a tax of $30. What is the output after the tax (units, 1 decimal place)?", a: 33.3, tol: 0.1, sol: "100 − Q = 50 + 0.5Q gives Q = <b>33.3</b>." },
  { q: "What is the new welfare loss (a triangle with base 10 and height 15)?", a: 75, sol: "0.5 x 10 x 15 = <b>75</b>, no better than doing nothing." },
  { q: "A policy removes 60% of a welfare loss of 150 and costs 100 to run. What is the net gain (negative if a loss)?", a: -10, sol: "0.6 x 150 = 90; 90 − 100 = <b>−10</b>: government failure." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of government failure?", opts: ["Perfect information", "Time lags between a problem and a policy's effect", "An externality", "Public goods"], a: 1, why: "Delays can mean the policy fits conditions that have already changed. Externalities and public goods are market failures." },
  { q: "A tax set above the external cost will most likely:", opts: ["raise output above the optimum", "cut output below the optimum", "leave output unchanged", "remove all external costs"], a: 1, why: "It overcorrects, so output falls below the social optimum." },
  { q: "Regulatory capture means:", opts: ["firms capture more of the market", "regulators serve the interests of the firms they regulate", "regulators close firms down", "the government buys a firm"], a: 1, why: "The regulator's decisions favour the industry rather than the public." },
  { q: "Which is a reason to prefer a nudge to a tax?", opts: ["It always works better", "It keeps people free to choose and may cost less", "It raises revenue", "It changes the price"], a: 1, why: "Nudges leave choice intact and are often cheap, though the effect can be uncertain." },
  { q: "An economy that uses both markets and government intervention is:", opts: ["a free market economy", "a command economy", "a mixed economy", "a subsistence economy"], a: 2, why: "Almost all real economies are mixed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Government failure", "Intervention that makes the allocation of resources worse or no better."],
  ["Information failure (government)", "The government cannot measure costs and benefits well enough to set the right policy."],
  ["Time lag", "Delay between the problem arising and the policy working."],
  ["Unintended consequence", "A side effect the policy-maker did not plan for."],
  ["Regulatory capture", "Regulators serve the firms they regulate rather than the public."],
  ["Opportunity cost of policy", "What else the money could have done."],
  ["Mixed economy", "An economy with both markets and government intervention."],
  ["Free market", "Resources allocated by prices and private decisions, with no government role."],
  ["Regressive tax", "Takes a larger share of income from low earners."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2024 · 32 · Q13] What is a failure of government microeconomic intervention?", opts: ["An indirect tax equal to external costs is imposed on cigarettes and the demand falls.", "Limits are placed on a trade union's restrictions that increase labour mobility.", "Price controls on bread are removed which allow a free market to operate.", "Tariffs are imposed on imported goods which cause the Gini coefficient to increase."], a: 3, why: "The tariffs made inequality worse: an unintended harmful side-effect. A, B and C are successful or neutral." },
  { q: "[May/June 2024 · 33 · Q11] The government can use policies to reduce the environmental damage caused by the amount of rubbish created by firms and households. Which policy is most likely to lead to government failure?", opts: ["an incentive payment for firms who reduce the levels of rubbish", "a tax on the amount of rubbish a firm or household creates", "an advertising campaign about the problems created by rubbish", "government grants to firms researching how to safely dispose of rubbish"], a: 1, why: "Taxing rubbish can lead to fly-tipping, so it may increase the problem and be costly to monitor." },
  { q: "[May/June 2020 (not sat) · 31 · Q13] Which policy is not designed to correct a market failure?", opts: ["government provision of healthcare", "price controls on large firms", "regulations to limit smoke pollution", "removing import quotas"], a: 3, why: "Removing import quotas is a trade liberalisation measure. The others address merit goods, monopoly power and an externality." },
  { q: "[Feb/March 2025 · 32 · Q8] What is not an example of government failure?", opts: ["decreased maximum price causing producers to leave the market", "higher guaranteed price encouraging suppliers to overproduce", "increased minimum wage leading to employers dismissing workers", "increased subsidies encouraging the consumption of a socially desirable product"], a: 3, why: "Encouraging consumption of a socially desirable good is the aim of a subsidy. A, B and C are harmful side effects." },
  { q: "[Oct/Nov 2022 · 33 · Q13] A government regards fresh fruit and vegetables as merit goods, and subsidises agriculture to boost their production. What could be a government failure arising from these subsidies?", opts: ["cheaper fresh fruit and vegetables", "land clearance reducing wildlife", "lower spending on treating dietary illnesses", "more jobs picking fruit and vegetables"], a: 1, why: "Land clearance is an unintended external cost. A, C and D are intended benefits." },
] });
