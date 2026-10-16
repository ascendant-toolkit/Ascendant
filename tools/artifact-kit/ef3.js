/* ---------- model: market D: P = 100 - Q, MC = 20 + 0.5Q. Firm: TC = 600 + 20Q + 0.25Q^2 (AC min at Q = 49, about $44.5) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const QS = 160 / 3, PS = 140 / 3;                       // allocatively efficient output and price (P = MC)
const QM = 32, PM = 68, MCM = 20 + 0.5 * 32;             // monopoly output, price, marginal cost there
const TSF = (q) => 80 * q - 0.75 * q * q, TSMAX = TSF(QS);
const ACF = (q) => 600 / q + 20 + 0.25 * q, MCF = (q) => 20 + 0.5 * q, QMIN = Math.sqrt(2400), ACMIN = ACF(QMIN);


/* ---------- Watch: free rider ---------- */
const FH = (v) => 1.3 * v, FB = 270;
function frDraw(s) {
  let o = SV.line(60, FB, 740, FB) + SV.text(62, 24, "$", "sm");
  if (s.u > 0) { for (let i = 0; i < 10; i++) o += SV.rect(80 + i * 36, FB - FH(15) * s.u, 26, FH(15) * s.u, "f1", { opacity: (s.f > 0.5 ? 0.3 : 0.85) * s.u }); o += SV.text(250, FB + 22, "10 users, $15 each", "sm bd", { "text-anchor": "middle", ...op(s.u) }); }
  if (s.f > 0) o += SV.text(250, FB - FH(15) - 14, "each hopes someone else pays", "lbl bd t2", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px", ...op(s.f) });
  if (s.t > 0) o += SV.rect(480, FB - FH(150) * s.t, 80, FH(150) * s.t, "f3", op(s.t)) + SV.text(520, FB - FH(150) - 8, "benefit $150", "lbl bd t3", { "text-anchor": "middle", ...op(s.t) }) + SV.text(520, FB + 22, "total benefit", "sm bd", { "text-anchor": "middle", ...op(s.t) });
  if (s.c > 0) o += SV.rect(600, FB - FH(100) * s.c, 80, FH(100) * s.c, "f2", op(s.c)) + SV.text(640, FB - FH(100) - 8, "cost $100", "lbl bd t2", { "text-anchor": "middle", ...op(s.c) }) + SV.text(640, FB + 22, "cost to build", "sm bd", { "text-anchor": "middle", ...op(s.c) });
  if (s.s > 0) o += SV.text(400, 50, "State provides, tax $10 each: net social benefit +$50", "lbl bd t3", { "text-anchor": "middle", ...op(s.s) });
  return o;
}
Lib.stepper($("#stF"), { w: 780, h: 310, label: "A public good with ten users who each value it at $15, a cost of $100 and the free-rider problem", base: { u: 0, f: 0, t: 0, c: 0, s: 0 }, draw: frDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The good.</b> A lighthouse would give each of ten ships a benefit worth <b>$15</b>. It is <b>non-excludable</b> (no ship can be stopped from using the light) and <b>non-rival</b> (one ship's use does not reduce another's).", s: { u: 1 } },
  { cap: "<b>Worth building.</b> The total benefit is 10 × $15 = <b>$150</b> and the cost is <b>$100</b>, so society gains $50 if it is built.", s: { u: 1, t: 1, c: 1 } },
  { cap: "<b>The free-rider problem.</b> Each ship gets the light whether it pays or not, so each hopes the others will pay. No one pays, a private firm cannot earn revenue, and the lighthouse is <b>not built</b>. The market fails to supply a good that is worth more than it costs.", s: { u: 1, t: 1, c: 1, f: 1 } },
  { cap: "<b>State provision.</b> The government builds it and funds it with taxation, here $10 from each of the ten users. Everyone pays, the free-rider problem is overcome and society gains $50. The difficulty in practice is knowing how much to spend.", s: { u: 1, t: 1, c: 1, f: 1, s: 1 } },
] });
/* ---------- Lab 4: free rider ---------- */
function lab4() {
  if (!$("#fv") || !$("#fn")) return;
  const v = +$("#fv").value, n = +$("#fn").value, tot = v * n, net = tot - 100;
  $("#u1").textContent = "$" + tot; $("#u2").textContent = (net >= 0 ? "+$" : "−$") + Math.abs(net); $("#u3").textContent = "No";
  $("#uv").textContent = net > 0 ? `Total benefit ($${tot}) is greater than the cost ($100), so building it is worth $${net} to society. But a private firm cannot charge: once built, everyone can use it without paying (non-excludable), and each user hopes others will pay (free riding). The market fails to provide a good that society values: a missing market. The government could provide it, funded by tax.`
    : net === 0 ? "Benefit equals cost, so society is indifferent. A private firm still could not charge for it." : `Total benefit ($${tot}) is below the cost ($100), so it is efficient not to build it. Move the sliders until total benefit exceeds $100.`;
  const m = Math.max(100, tot), H = (x) => 190 * (x / m), bw = 70;
  let o = SV.line(30, 210, 400, 210) + SV.text(32, 22, "$", "sm");
  [[40, 100, "f2", "Cost to build"], [150, v, "f1", "One user's value"], [260, tot, net > 0 ? "f3" : "f4", "Total benefit"]].forEach(([x, val, c, l]) => { o += SV.rect(x, 210 - H(val), bw, H(val), c) + SV.text(x + bw / 2, 210 - H(val) - 6, "$" + val, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 228, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "fv", label: "Value to each user ($): ", min: 2, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab4 });
Lib.slider($("#g6"), { id: "fn", label: "Number of users: ", min: 2, max: 20, step: 1, value: 10, fmt: (v) => v, onInput: lab4 });


/* ---------- Lab 2: used cars ---------- */
function labCar() {
  if (!$("#gc")) return;
  const g = +$("#gc").value / 100, avg = g * 10000 + (1 - g) * 5000, ok = avg >= 8000;
  $("#h1").textContent = "$" + Lib.fmtN(avg, 0); $("#h2").textContent = "$8,000"; $("#h3").textContent = ok ? "Yes" : "No";
  $("#hv").textContent = ok ? `With ${Math.round(g * 100)}% good cars, buyers will pay an average of $${Lib.fmtN(avg, 0)}, enough for owners of good cars (who want $8,000) to sell. Both types of car are traded.`
    : `With ${Math.round(g * 100)}% good cars, buyers will pay only $${Lib.fmtN(avg, 0)} on average, less than the $8,000 owners of good cars want. They withdraw, the average quality of cars for sale falls, and offers fall further. Information failure can make a market shrink or disappear.`;
  const H = (v) => v / 50, base = 200;
  let o = SV.line(30, base, 400, base);
  [[70, avg, ok ? "f3" : "f2", "Buyers' average offer"], [230, 8000, "f4", "Good sellers' minimum"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 222, l, "sm", { "text-anchor": "middle" }); });
  $("#labU").innerHTML = o;
}
Lib.slider($("#g10"), { id: "gc", label: "Share of good cars for sale: ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labCar });

/* ---------- Practise ---------- */
Lib.classify($("#cl2"), {
  prompt: "Which cause of market failure is each example?",
  buckets: [{ label: "Externality" }, { label: "Public good" }, { label: "Merit or demerit good" }, { label: "Information failure" }, { label: "Monopoly power" }],
  items: [
    { text: "A factory's smoke harms nearby residents", b: 0 }, { text: "Traffic congestion slows other drivers", b: 0 },
    { text: "Street lighting that cannot be charged for", b: 1 }, { text: "National defence: free riders benefit without paying", b: 1 },
    { text: "Vaccinations are under-consumed", b: 2 }, { text: "Cigarettes are over-consumed", b: 2 },
    { text: "A used car buyer cannot tell the car's quality", b: 3 }, { text: "A smoker underestimates the health risk", b: 3 },
    { text: "A sole supplier restricts output and raises price", b: 4 },
  ], done: "Name the cause, then explain how it leads to allocative inefficiency.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Public good", "Non-rival and non-excludable, so the market will not supply it"],
  ["Free rider", "Someone who benefits without paying"],
  ["Merit good", "Under-consumed because people underestimate the benefit"],
  ["Demerit good", "Over-consumed because people underestimate the harm"],
  ["Asymmetric information", "One party knows more than the other"],
  ["Market failure", "The free market does not allocate resources efficiently"],
  ["Government failure", "Intervention that leaves resources less efficiently used"],
], done: "Seven words for the causes of market failure." });
Lib.calc($("#c1"), { qs: [
  { q: "A lighthouse costs $100. Ten users each value it at $15. What is the net social benefit ($)?", a: 50, sol: "Total benefit 150 − cost 100 = <b>$50</b>. Worth building, but a private firm could not charge for it." },
  { q: "A street light costs $400. Twenty residents each gain $30 from it. What is the net social benefit ($)?", a: 200, sol: "20 × 30 = 600 benefit; 600 − 400 = <b>$200</b>. It should be built, but a private firm cannot charge for it." },
  { q: "The state funds that street light by taxing each of the 20 residents equally. How much does each pay ($)?", a: 20, sol: "400 ÷ 20 = <b>$20</b>, less than each resident's benefit of $30." },
  { q: "Good cars are worth $12,000 to buyers and bad cars $4,000. Half the cars for sale are good. What is the average value buyers will pay ($)?", a: 8000, sol: "0.5 × 12,000 + 0.5 × 4,000 = <b>$8,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A public good is:", opts: ["rival and excludable", "non-rival and non-excludable", "rival and non-excludable", "provided by the government only"], a: 1, why: "Because non-payers cannot be excluded, free riders mean the market does not provide it." },
  { q: "Which would NOT be a source of market failure in the efficiency sense?", opts: ["Externalities", "Monopoly power", "Asymmetric information", "A free market with perfect information and no externalities"], a: 3, why: "Market failure arises when the conditions for efficiency are not met." },
  { q: "The free-rider problem occurs because:", opts: ["goods are rival", "people can use a non-excludable good without paying", "prices are too high", "firms have monopoly power"], a: 1, why: "If no one can be stopped from using it, no one has an incentive to pay." },
  { q: "Asymmetric information means:", opts: ["buyers and sellers have equal information", "one side of the market knows more than the other", "prices are fixed", "goods are non-rival"], a: 1, why: "A seller who knows more than the buyer can distort the market." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market failure", "The free market does not allocate resources efficiently."],
  ["Public good", "Non-rival and non-excludable. Leads to the free-rider problem."],
  ["Merit good", "Under-consumed because consumers undervalue the benefit (education, vaccination)."],
  ["Demerit good", "Over-consumed because consumers undervalue the harm (cigarettes)."],
  ["Asymmetric information", "One party knows more than the other, which can distort choices."],
  ["Government failure", "Intervention that leaves resources less efficiently allocated, or no better than before."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 31 · Q13] What is not a source of market failure?", opts: ["imperfect information", "income inequality", "monopoly", "non-excludability"], a: 1, why: "Income inequality is an equity issue. The others stop the market allocating resources efficiently." },
  { q: "[Oct/Nov 2020 · 33 · Q3] Which situation should not lead to market failure?", opts: ["Managers in a firm have information unavailable to shareholders.", "Resources such as solar energy can be continuously renewed.", "Resource allocation is not always Pareto efficient.", "Undesirable goods are overproduced."], a: 1, why: "A renewable resource does not by itself cause market failure. A is information failure, C is the definition of failure, D is demerit goods." },
  { q: "[Oct/Nov 2021 · 33 · Q2] Why are public goods an example of market failure?", opts: ["Producers undervalue the benefits of a public good.", "Public goods have high fixed costs of production.", "The non-excludability of a public good leads to the free rider problem.", "When a public good is consumed by one person, it is not available to others."], a: 2, why: "Non-excludability means people can use the good without paying, so the market does not provide it. D describes a rival good." },
] });
