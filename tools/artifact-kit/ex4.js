/* ---------- model: demand (MPB) P = 100 - Q, private marginal cost MPC = 20 + 0.5Q. External cost / benefit $15 a unit in the animations ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 6.8, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
/* ---------- Watch 3: cost-benefit analysis ---------- */
const R = 0.05, f = (t) => 1 / (1 + R) ** t, PVA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].reduce((a, t) => a + f(t), 0);
const CX = (t) => 90 + t * 58, SC = 0.3, BASE = 150;
function cbaDraw(s) {
  let o = SV.line(60, BASE, 700, BASE) + SV.text(700, BASE - 8, "Years", "sm", { "text-anchor": "end" });
  for (let t = 0; t <= 10; t++) o += SV.text(CX(t), 366, t, "sm", { "text-anchor": "middle" });
  o += SV.rect(CX(0) - 18, BASE, 36, 600 * SC, "f2", op(s.c)) + SV.text(CX(0), BASE + 600 * SC + 16, "−600", "lbl bd t2", { "text-anchor": "middle", ...op(s.c) });
  for (let t = 1; t <= 10; t++) {
    const k = 1 - s.disc * (1 - f(t));
    if (s.b > 0) o += SV.rect(CX(t) - 16, BASE - 120 * SC * k, 32, 120 * SC * k, "f1", op(s.b)) + (t === 10 ? SV.text(CX(t), BASE - 120 * SC * k - 8, s.disc > 0.5 ? "+" + Lib.fmtN(120 * f(10), 0) : "+120", "sm bd t1", { "text-anchor": "middle", ...op(s.b) }) : "");
    if (s.e > 0) o += SV.rect(CX(t) - 16, BASE, 32, 36 * SC * k, "f2", { opacity: s.e * 0.85 });
  }
  if (s.b > 0) o += SV.text(CX(5), BASE - 120 * SC - 24, "private benefit $120 a year", "lbl bd t1", { "text-anchor": "middle", ...op(s.b) });
  if (s.e > 0) o += SV.text(CX(5), BASE + 36 * SC + 22, "external cost $36 a year", "lbl bd t2", { "text-anchor": "middle", ...op(s.e) });
  if (s.res > 0) o += SV.text(380, 290, `PV of private benefits ${Lib.fmtN(120 * PVA, 0)} − PV of external costs ${Lib.fmtN(36 * PVA, 0)} − cost 600`, "lbl bd", { "text-anchor": "middle", ...op(s.res) }) + SV.text(380, 316, `Private NPV = +${Lib.fmtN(120 * PVA - 600, 0)}   ·   Social NPV = +${Lib.fmtN(84 * PVA - 600, 0)}`, "lbl bd t3", { "text-anchor": "middle", ...op(s.res) });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Cost benefit analysis with private benefits, external costs and discounting over ten years", base: { c: 0, b: 0, e: 0, disc: 0, res: 0 }, draw: cbaDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The cost.</b> The project costs $600 now, in year 0.", s: { c: 1 } },
  { cap: "<b>Private benefits.</b> It earns $120 a year for ten years: $1,200 in total, more than the cost.", s: { c: 1, b: 1 } },
  { cap: "<b>External costs.</b> It also imposes $36 a year of external cost (pollution, noise). The net benefit per year is $84, or $840 in total.", s: { c: 1, b: 1, e: 1 } },
  { cap: "<b>Discounting.</b> Money in the future is worth less than money now. At 5%, $120 in year 10 has a present value of about $74. Every bar shrinks, later years the most.", s: { c: 1, b: 1, e: 1, disc: 1 } },
  { cap: `<b>The result.</b> Private NPV is +${Lib.fmtN(120 * PVA - 600, 0)}. Social NPV is +${Lib.fmtN(84 * PVA - 600, 0)}: still positive, so the project is worthwhile, but much less than the private figure suggests. If the external cost were $45 a year, the social NPV would be negative.`, s: { c: 1, b: 1, e: 1, disc: 1, res: 1 } },
] });
/* ---------- Lab 3: CBA ---------- */
function lab3() {
  if (!$("#ec") || !$("#dr")) return;
  const e = +$("#ec").value, r = +$("#dr").value / 100; let A = 0; for (let t = 1; t <= 10; t++) A += 1 / (1 + r) ** t;
  const pn = 120 * A - 600, sn = (120 - e) * A - 600;
  $("#t1").textContent = (pn >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(pn), 0); $("#t2").textContent = (sn >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(sn), 0); $("#t3").textContent = sn > 0 ? "Yes" : "No";
  $("#tv").textContent = sn > 0 ? `Social NPV is positive, so the benefits to society exceed the costs. External costs of $${e} a year cut the NPV from $${Lib.fmtN(pn, 0)} to $${Lib.fmtN(sn, 0)}.`
    : `Social NPV is negative. The project looks profitable privately (NPV $${Lib.fmtN(pn, 0)}) but once the external costs are counted it should not go ahead. A higher discount rate or higher external cost makes this more likely.`;
  const mx = Math.max(Math.abs(pn), Math.abs(sn), 100), H = (v) => 90 * (v / mx), base = 120, bw = 90;
  let o = SV.line(30, base, 400, base);
  [[80, pn, "Private NPV"], [230, sn, "Social NPV"]].forEach(([x, v, l]) => { o += SV.rect(x, v >= 0 ? base - H(v) : base, bw, Math.abs(H(v)), v >= 0 ? "f3" : "f2") + SV.text(x + bw / 2, v >= 0 ? base - H(v) - 8 : base + Math.abs(H(v)) + 16, (v >= 0 ? "+" : "−") + Lib.fmtN(Math.abs(v), 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 245, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g5"), { id: "ec", label: "External cost per year ($): ", min: 0, max: 60, step: 1, value: 36, fmt: (v) => v, onInput: lab3 });
Lib.slider($("#g6"), { id: "dr", label: "Discount rate: ", min: 0, max: 12, step: 1, value: 5, fmt: (v) => v + "%", onInput: lab3 });

/* ---------- Watch 2: discount rate ---------- */
const AF = (r) => { let a = 0; for (let t = 1; t <= 10; t++) a += 1 / (1 + r) ** t; return a; };
function rateDraw(s) {
  const base = 190, H = (v) => v * 0.8, bw = 90;
  let o = SV.line(60, base, 740, base) + SV.text(62, 24, "Social NPV ($)", "sm");
  [[0.02, 90], [0.05, 230], [0.08, 370], [0.1, 510]].forEach(([r, x], i) => {
    const k = s["b" + i] || 0; if (k <= 0) return;
    const v = 84 * AF(r) - 600, up = v >= 0, h = H(Math.abs(v)) * k;
    o += SV.rect(x, up ? base - h : base, bw, h, up ? "f3" : "f2", op(k)) + SV.text(x + bw / 2, up ? base - h - 8 : base + h + 16, (up ? "+" : "−") + Lib.fmtN(Math.abs(v), 0), "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + bw / 2, 296, "r = " + Math.round(r * 100) + "%", "lbl bd", { "text-anchor": "middle", ...op(k) });
  });
  return o;
}
Lib.stepper($("#stR"), { w: 780, h: 320, label: "Social net present value of the same project at four discount rates", base: { b0: 0, b1: 0, b2: 0, b3: 0 }, draw: rateDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The project.</b> Cost $600 now, benefits $120 a year for ten years, external cost $36 a year. The only thing that changes below is the <b>discount rate</b>.", s: {} },
  { cap: "<b>At 2%</b> the future counts for a lot. Social NPV is about <b>+$155</b>: go ahead.", s: { b0: 1 } },
  { cap: "<b>At 5%</b> social NPV falls to about <b>+$49</b>. Still positive, but only just.", s: { b0: 1, b1: 1 } },
  { cap: "<b>At 8%</b> distant benefits shrink further and social NPV turns <b>negative, about −$36</b>. The project should not go ahead.", s: { b0: 1, b1: 1, b2: 1 } },
  { cap: "<b>At 10%</b> the NPV is about <b>−$84</b>. The same project, the same costs and benefits, but the decision flips. This is why the choice of discount rate is a key criticism of CBA.", s: { b0: 1, b1: 1, b2: 1, b3: 1 } },
] });

/* ---------- Lab 2: present value ---------- */
function labPV() {
  if (!$("#pva") || !$("#pvt") || !$("#pvr")) return;
  const a = +$("#pva").value, t = +$("#pvt").value, r = +$("#pvr").value / 100, pv = a / (1 + r) ** t;
  $("#z1").textContent = "$" + Lib.fmtN(pv, 0); $("#z2").textContent = Math.round((1 - pv / a) * 100) + "%";
  $("#zv").textContent = t === 0 || r === 0 ? "With no waiting or a zero rate, there is no discounting: the present value equals the amount."
    : `$${a} received in ${t} years is worth $${Lib.fmtN(pv, 0)} today at ${Math.round(r * 100)}%. Waiting costs ${Math.round((1 - pv / a) * 100)}% of the value. The longer the wait and the higher the rate, the smaller the present value.`;
  const x = (v) => 50 + v * 11.5, y = (v) => 235 - 200 * v / 1000;
  let o = SV.line(50, 235, 395, 235) + SV.line(50, 235, 50, 20) + SV.text(392, 258, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Present value ($)", "sm");
  const pts = []; for (let k = 0; k <= 30; k++) pts.push([x(k), y(a / (1 + r) ** k)]);
  o += SV.path(ptsPath(pts), "c1") + SV.line(x(t), y(pv), x(t), 235, "gr") + SV.line(50, y(pv), x(t), y(pv), "gr") + SV.circle(x(t), y(pv), 6, "dot1") + SV.text(x(t) + 8, y(pv) - 8, "$" + Lib.fmtN(pv, 0), "lbl bd", { ...halo });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g15"), { id: "pva", label: "Future amount ($): ", min: 200, max: 1000, step: 100, value: 1000, fmt: (v) => v, onInput: labPV });
Lib.slider($("#g16"), { id: "pvt", label: "Years until it is received: ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labPV });
Lib.slider($("#g17"), { id: "pvr", label: "Discount rate: ", min: 0, max: 12, step: 1, value: 5, fmt: (v) => v + "%", onInput: labPV });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "In a CBA of a new airport, which items are easy to value in money and which are hard?",
  buckets: [{ label: "Easier to value" }, { label: "Hard to value" }],
  items: [
    { text: "Construction cost of the terminal", b: 0 }, { text: "Landing fees and ticket revenue", b: 0 }, { text: "Wages of airport staff", b: 0 }, { text: "Cost of buying the land", b: 0 },
    { text: "Noise for people living nearby", b: 1 }, { text: "Loss of countryside and wildlife", b: 1 }, { text: "Time saved by passengers", b: 1 }, { text: "Effect on local climate and health", b: 1 },
  ], done: "Prices exist for market items. External effects need estimates, which is the main weakness of CBA.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Cost-benefit analysis", "Counting all private and external costs and benefits of a project in money terms"],
  ["Discounting", "Converting future amounts to present value"],
  ["Present value", "What a future amount is worth today"],
  ["Net present value", "Discounted benefits minus discounted costs"],
  ["Discount rate", "The rate used to reduce the value of future amounts"],
  ["Social NPV", "NPV after including external costs and benefits"],
  ["Opportunity cost of funds", "What else the money could have achieved"],
], done: "Seven words for CBA." });
Lib.order($("#o1"), { prompt: "Put the steps of a cost-benefit analysis in order.", items: [
  "Identify the private costs and benefits of the project",
  "Identify the external costs and benefits",
  "Give each a money value, using estimates where needed",
  "Discount future amounts to present values",
  "Calculate the net present value",
  "Decide, and evaluate the difficulties and the effect of the discount rate",
], done: "A reliable structure for a CBA answer." });
Lib.calc($("#c1"), { qs: [
  { q: "A benefit of $110 arrives in one year. The discount rate is 10%. What is its present value ($)?", a: 100, sol: "110 ÷ 1.10 = <b>$100</b>." },
  { q: "A payment of $1,000 arrives in two years. The discount rate is 10%. What is its present value ($, nearest whole number)?", a: 826, tol: 1, sol: "1,000 ÷ 1.21 = <b>$826</b>." },
  { q: "A project costs $500 now and has a present value of benefits of $540. What is the NPV ($)?", a: 40, sol: "540 − 500 = <b>+$40</b>: go ahead." },
  { q: "The same project has external costs with a present value of $70. What is the social NPV ($)?", a: -30, sol: "40 − 70 = <b>−$30</b>: not worthwhile once external costs are counted." },
  { q: "A project has private cost 400, private benefit 440, social cost 450 and social benefit 480. What is the net external cost ($ million)?", a: 10, hint: "External cost = social cost − private cost. External benefit = social benefit − private benefit.", sol: "External cost 50, external benefit 40, so net external cost is <b>$10 million</b>." },
  { q: "Present value of benefits is $800 and of costs is $600. What is the ratio of discounted benefits to costs (1 decimal place)?", a: 1.3, tol: 0.05, sol: "800 ÷ 600 = <b>1.3</b>. Above 1 means NPV is positive." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Why is cost-benefit analysis difficult?", opts: ["Future benefits do not need discounting", "External costs and benefits are hard to value in money", "Private costs are unknown", "It ignores externalities"], a: 1, why: "Putting a monetary value on pollution, time or health is difficult and uncertain." },
  { q: "Why are future benefits discounted?", opts: ["Because they are certain", "Because money received later is worth less than money now", "Because costs always come first", "Because external costs are small"], a: 1, why: "A dollar now can be used or invested, so a dollar later has a lower present value." },
  { q: "A higher discount rate will usually:", opts: ["raise the value of benefits many years away", "reduce the value of benefits many years away", "have no effect on NPV", "remove external costs"], a: 1, why: "Distant amounts are divided by a larger number." },
  { q: "A project has a positive private NPV but a negative social NPV. What does this suggest?", opts: ["It is worth doing for everyone", "External costs outweigh the private gain", "The discount rate is zero", "Costs are underestimated"], a: 1, why: "Counting external costs turns the net benefit negative." },
  { q: "Which is a limitation of CBA?", opts: ["It ignores externalities", "It cannot compare projects", "External effects are hard to value in money", "It shows who gains and loses"], a: 2, why: "Valuing noise, health or a view involves estimates and judgement." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Cost-benefit analysis", "A method of valuing all private and external costs and benefits of a project over time."],
  ["Discounting", "Converting future amounts to present value."],
  ["Present value", "Future value ÷ (1 + r)^t."],
  ["Net present value", "Present value of benefits minus present value of costs. Go ahead if positive."],
  ["Social NPV", "NPV including external costs and benefits."],
  ["Private NPV", "NPV counting only the costs and benefits to the owner."],
  ["Discount rate", "The rate used to reduce the value of future amounts."],
  ["Intangibles", "Effects with no market price, such as noise or a view."],
  ["Distribution", "Who gains and who loses, which CBA totals can hide."],
  ["Benefit-cost ratio", "Discounted benefits divided by discounted costs."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2023 · 32 · Q9] The result of a cost-benefit analysis of a proposed government road-building project is that there will be a positive net social benefit of $50 million. Why might the government not proceed with the project?", opts: ["The project would not be profitable for a private firm.", "The project would cause negative externalities.", "There is limited capital available for government projects.", "There would be more who lost than gained."], a: 2, why: "A positive NPV does not guarantee funding: the government may have limited capital and better uses for it." },
  { q: "[Oct/Nov 2020 · 31 · Q1] What is the main aim of cost-benefit analysis?", opts: ["to allow firms to maximise their private benefit and minimise the external cost", "to equate total social benefit to the total social cost of a project", "to find the correct level of direct tax to internalise the external cost of a project", "to find the highest positive difference between total benefit and total cost"], a: 3, why: "CBA looks for the net benefit (benefit minus cost) to society. B describes zero net benefit." },
  { q: "[Oct/Nov 2022 · 32 · Q3] What could be included in a cost-benefit analysis of a project to build a road bridge connecting an island community to the mainland? (a fall in employment for ferry services, an increase in carbon emissions, a reduction in travel time for work, an increase in incomes for the community)", opts: ["yes, no, no, yes", "yes, yes, no, no", "yes, yes, yes, yes", "no, no, yes, yes"], a: 2, why: "CBA counts all costs and benefits, so all four effects are included." },
  { q: "[Oct/Nov 2023 · 33 · Q9] Which conditions are most likely to reduce the accuracy of cost-benefit analysis in decision making?", opts: ["a high proportion of external costs and benefits, and a high share of total costs and benefits in the future", "a high proportion of external costs and benefits, and a low share in the future", "a low proportion of external costs and benefits, and a high share in the future", "a low proportion of external costs and benefits, and a low share in the future"], a: 0, why: "External effects are hard to value and distant amounts are uncertain and sensitive to the discount rate, so both together reduce accuracy." },
  { q: "[May/June 2023 · 32 · Q12] A government hopes to build an athletics stadium to hold the World Games. The stadium would have high private and external costs, but it would increase national pride. Why would it be difficult to use cost-benefit analysis to decide whether to build the stadium?", opts: ["The materials needed to build the stadium will need to be imported.", "The external costs of clearing land for building will outweigh the private costs.", "The stadium will not be used much for athletics after the World Games.", "The valuation of national pride will be complex to assess."], a: 3, why: "National pride has no market price, so valuing it is hard." },
  { q: "[Oct/Nov 2024 · 32 · Q11] What is not a valid comment economists may make regarding the need to subsidise a green energy market that uses solar and wind power?", opts: ["It is cheaper to use the plentiful supply of coal.", "Markets will become more efficient.", "The value of the positive externalities cannot be estimated.", "The value of the negative externalities cannot be estimated."], a: 1, why: "Claiming that markets will become more efficient is not a valid comment on the need for the subsidy. A, C and D are valid points about the cost of coal and the difficulty of measuring externalities." },
] });
