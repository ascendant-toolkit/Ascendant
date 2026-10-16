/* ---------- model: demand (MPB) P = 100 - Q, private marginal cost MPC = 20 + 0.5Q. External cost / benefit $15 a unit in the animations ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 6.8, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };

/* ---------- Watch: private + external = social ---------- */
const H1 = (v) => v * 3.2, B0 = 290;
function psDraw(s) {
  let o = SV.line(60, B0, 740, B0) + SV.text(62, 24, "$ per unit", "sm");
  if (s.pc > 0) o += SV.rect(110, B0 - H1(40) * s.pc, 110, H1(40) * s.pc, "f4", op(s.pc)) + SV.text(228, B0 - H1(40) / 2, "private cost $40", "lbl bd t4", { ...halo, ...op(s.pc) });
  if (s.ec > 0) o += SV.rect(110, B0 - H1(40) - H1(15) * s.ec, 110, H1(15) * s.ec, "f2", op(s.ec)) + SV.text(228, B0 - H1(40) - H1(15) / 2 + 4, "external cost $15", "lbl bd t2", { ...halo, ...op(s.ec) });
  if (s.sc > 0) o += SV.text(165, B0 - H1(55) - 10, "social cost $55", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.sc) });
  if (s.pb > 0) o += SV.rect(470, B0 - H1(60) * s.pb, 110, H1(60) * s.pb, "f1", op(s.pb)) + SV.text(588, B0 - H1(60) / 2, "private benefit $60", "lbl bd t1", { ...halo, ...op(s.pb) });
  if (s.eb > 0) o += SV.rect(470, B0 - H1(60) - H1(15) * s.eb, 110, H1(15) * s.eb, "f3", op(s.eb)) + SV.text(588, B0 - H1(60) - H1(15) / 2 + 4, "external benefit $15", "lbl bd t3", { ...halo, ...op(s.eb) });
  if (s.sb > 0) o += SV.text(525, B0 - H1(75) - 10, "social benefit $75", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.sb) });
  o += SV.text(165, B0 + 22, "Factory: cost of one more unit", "sm", { "text-anchor": "middle" }) + SV.text(525, B0 + 22, "Vaccination: benefit of one more", "sm", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stP1"), { w: 780, h: 320, label: "Private cost plus external cost equals social cost; private benefit plus external benefit equals social benefit", base: { pc: 0, ec: 0, sc: 0, pb: 0, eb: 0, sb: 0 }, draw: psDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Private cost.</b> A factory pays $40 in wages, materials and energy to make one more unit. This is what its decisions are based on.", s: { pc: 1 } },
  { cap: "<b>External cost.</b> Making that unit also pollutes the air, costing nearby residents $15. The factory does not pay it, so it is an <b>external cost</b>. <b>Social cost = $40 + $15 = $55</b>.", s: { pc: 1, ec: 1, sc: 1 } },
  { cap: "<b>Private benefit.</b> Now the benefit side. A person who is vaccinated values the protection at $60. This is what the buyer considers.", s: { pc: 1, ec: 1, sc: 1, pb: 1 } },
  { cap: "<b>External benefit.</b> Others in the community are less likely to catch the disease, worth $15 to them. <b>Social benefit = $60 + $15 = $75</b>.", s: { pc: 1, ec: 1, sc: 1, pb: 1, eb: 1, sb: 1 } },
  { cap: "<b>Why it matters.</b> Decision-makers see only the lower parts of each bar. They produce too much of the polluting good (price too low) and buy too little of the vaccination (price too high for the social benefit). Part 2 shows this on a diagram.", s: { pc: 1, ec: 1, sc: 1, pb: 1, eb: 1, sb: 1 } },
] });

/* ---------- Lab 1: one more unit ---------- */
function lab6() {
  if (!$("#pcs") || !$("#mec") || !$("#pbs") || !$("#meb")) return;
  const pc = +$("#pcs").value, ec = +$("#mec").value, pb = +$("#pbs").value, eb = +$("#meb").value, sc = pc + ec, sb = pb + eb, priv = pb >= pc, soc = sb >= sc;
  $("#v1").textContent = "$" + sc; $("#v2").textContent = "$" + sb; $("#v3").textContent = priv ? "Produce" : "Do not"; $("#v4").textContent = soc ? "Worth it" : "Not worth it";
  $("#vv").innerHTML = priv && soc ? "The unit is worth producing for the decision-maker and for society."
    : priv && !soc ? `The decision-maker sees a gain of $${pb - pc}, but society loses $${sc - sb} once the external cost is counted. This is <b>overproduction</b>: the unit is made but should not be.`
    : !priv && soc ? `The decision-maker sees a loss of $${pc - pb}, but society would gain $${sb - sc} once the external benefit is counted. This is <b>underproduction</b>: the unit is not made but should be.`
    : "The unit is not worth producing for the decision-maker or for society.";
  const H = (v) => 1.6 * v, base = 215;
  let o = SV.line(30, base, 400, base);
  [[70, pc, ec, "f4", "f2", "Cost of one more unit"], [250, pb, eb, "f1", "f3", "Benefit of one more unit"]].forEach(([x, p, e, c1, c2, l]) => {
    o += SV.rect(x, base - H(p), 100, H(p), c1) + SV.rect(x, base - H(p) - H(e), 100, H(e), c2) + SV.text(x + 50, base - H(p + e) - 8, "$" + (p + e), "lbl bd", { "text-anchor": "middle" }) +
      SV.text(x + 50, base - H(p) / 2 + 4, "private $" + p, "sm bd", { "text-anchor": "middle", ...halo }) + (e > 0 ? SV.text(x + 50, base - H(p) - H(e) / 2 + 4, "external $" + e, "sm bd", { "text-anchor": "middle", ...halo }) : "") + SV.text(x + 50, 238, l, "sm", { "text-anchor": "middle" });
  });
  $("#labJ").innerHTML = o;
}
Lib.slider($("#g8"), { id: "pcs", label: "Private cost ($): ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g9"), { id: "mec", label: "External cost ($): ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g10"), { id: "pbs", label: "Private benefit ($): ", min: 30, max: 90, step: 5, value: 50, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g11"), { id: "meb", label: "External benefit ($): ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: lab6 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which type of externality is each example?",
  buckets: [{ label: "Negative production" }, { label: "Negative consumption" }, { label: "Positive production" }, { label: "Positive consumption" }],
  items: [
    { text: "Smoke from a factory chimney", b: 0 }, { text: "Noise from aircraft over a city", b: 0 },
    { text: "Litter from chewing gum", b: 1 }, { text: "Second-hand smoke from a smoker", b: 1 }, { text: "Traffic congestion caused by drivers", b: 1 },
    { text: "A firm trains workers who later join rivals", b: 2 }, { text: "A firm rebuilds a local road when building a factory", b: 2 }, { text: "Research that other firms can use", b: 2 },
    { text: "A person gets vaccinated, protecting others", b: 3 }, { text: "A person completes education and later pays more tax", b: 3 },
  ], done: "Ask who creates the effect (producer or consumer) and whether it harms or helps others.",
});
Lib.classify($("#cl2"), {
  prompt: "Is each item a private or an external cost or benefit? (Think of a factory that pollutes.)",
  buckets: [{ label: "Private cost" }, { label: "External cost" }, { label: "Private benefit" }, { label: "External benefit" }],
  items: [
    { text: "Wages paid by the factory", b: 0 }, { text: "The cost of raw materials", b: 0 },
    { text: "Illness among nearby residents from the smoke", b: 1 }, { text: "The cost of cleaning a polluted river, paid by the town", b: 1 },
    { text: "Profit earned by the factory owner", b: 2 }, { text: "A customer's satisfaction from the product", b: 2 },
    { text: "Local shops gain customers from the factory's workers", b: 3 }, { text: "A neighbour is protected because you are vaccinated", b: 3 },
  ], done: "Private means the decision-maker pays or gains. External means a third party does.",
});

Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Externality", "A cost or benefit that falls on a third party and is not in the price"],
  ["Third party", "Someone who is not the buyer or the seller"],
  ["Marginal social cost", "Marginal private cost plus marginal external cost"],
  ["Marginal social benefit", "Marginal private benefit plus marginal external benefit"],
  ["Negative externality", "A third party suffers a cost they did not agree to"],
  ["Positive externality", "A third party gains a benefit they did not pay for"],
  ["Spill-over", "Another word for an externality: an effect that spills onto others"],
], done: "Seven words that define the chapter." });
Lib.calc($("#c1"), { qs: [
  { q: "MPC is $40 and the marginal external cost is $12. What is the marginal social cost ($)?", a: 52, sol: "MSC = MPC + MEC = 40 + 12 = <b>$52</b>." },
  { q: "MPB is $60 and the marginal external benefit is $15. What is the marginal social benefit ($)?", a: 75, sol: "MSB = MPB + MEB = <b>$75</b>." },
  { q: "A factory's private cost of a unit is $40 and the social cost is $52. What is the marginal external cost ($)?", a: 12, sol: "External cost = social cost − private cost = <b>$12</b>." },
  { q: "A project has private cost 400, private benefit 440, social cost 450 and social benefit 480. What is the net external cost ($ million)?", a: 10, hint: "External cost = social cost − private cost. External benefit = social benefit − private benefit.", sol: "External cost 50, external benefit 40, so the net external cost is <b>$10 million</b>." },
  { q: "A vaccination has a private benefit of $60 and a social benefit of $75. What is the external benefit ($)?", a: 15, sol: "75 − 60 = <b>$15</b>." },
  { q: "A unit has MPB $50, MPC $40 and a marginal external cost of $20. What is the net social benefit of producing it ($, negative for a loss)?", a: -10, hint: "MSC = 40 + 20.", sol: "MSB 50 − MSC 60 = <b>−$10</b>: society loses, though the firm gains $10." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Social cost equals:", opts: ["private cost minus external cost", "private cost plus external cost", "external cost only", "private benefit plus external cost"], a: 1, why: "Social cost = private cost + external cost." },
  { q: "With a negative production externality, the free market:", opts: ["underproduces", "produces the efficient output", "overproduces", "does not produce"], a: 2, why: "The producer ignores part of the cost, so the price is too low and output too high." },
  { q: "Vaccination is an example of:", opts: ["a negative production externality", "a positive consumption externality", "a public good", "a demerit good"], a: 1, why: "The consumer's action benefits third parties, so MSB > MPB." },
  { q: "Which is an external cost?", opts: ["Wages paid by a factory", "Cost of raw materials", "Illness among nearby residents from the factory's smoke", "The factory's advertising spend"], a: 2, why: "Only the residents' illness falls on a third party." },
  { q: "A positive consumption externality means:", opts: ["MSB is greater than MPB", "MSC is greater than MPC", "MSB equals MPB", "MPC equals MPB"], a: 0, why: "Others gain from consumption, so the social benefit is greater than the private benefit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Private cost", "Cost paid by the producer or consumer making the decision."],
  ["External cost", "Cost imposed on a third party and not paid by the decision-maker."],
  ["Social cost", "Private cost plus external cost."],
  ["Private benefit", "Benefit received by the consumer or producer."],
  ["External benefit", "Benefit received by a third party who did not pay."],
  ["Social benefit", "Private benefit plus external benefit."],
  ["Externality", "A spill-over cost or benefit to a third party that is not reflected in the market price."],
  ["Third party", "Someone who is neither buyer nor seller in a transaction."],
  ["MSC = MPC + MEC", "Marginal social cost is private plus external cost."],
  ["MSB = MPB + MEB", "Marginal social benefit is private plus external benefit."],
  ["Production externality", "Created by a producer's activity."],
  ["Consumption externality", "Created by a consumer's activity."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2020 (not sat) · 32 · Q1] What is an example of a negative externality?", opts: ["Lower profit due to increased competition from new firms entering the market.", "Reduced government funding for a museum.", "The increase in noise levels from aircraft due to the expansion of a large city airport.", "The increase in production costs due to an increase in the cost of importing raw materials."], a: 2, why: "Noise is a cost imposed on third parties. A, B and D are costs that fall on the firm or the museum itself." },
  { q: "[May/June 2020 (not sat) · 31 · Q1] A medical team provides vaccinations for children to prevent an outbreak of an infectious disease. Why would this be described as a positive externality?", opts: ["Additional benefit might be gained as the disease no longer spreads.", "Any kind of medical help will improve the condition of the children.", "No action would be taken unless the medical team intervened.", "The social benefits of vaccination are less than the social costs."], a: 0, why: "Third parties gain because the disease does not spread. D is the opposite of the case." },
  { q: "[May/June 2021 · 31 · Q1] What is a negative consumption externality associated with chewing gum?", opts: ["better dental hygiene from chewing gum", "costs of the ingredients in chewing gum", "discarded chewing gum on pavements", "smells from chewing gum factories"], a: 2, why: "The litter arises from consumption. D is a production externality, B is a private cost and A a benefit." },
  { q: "[Oct/Nov 2021 · 31 · Q2] What is an example of a negative externality?", opts: ["the non-provision of public goods by the market", "indirect taxation that fails to internalise the external cost", "monopoly power leading to reduced output and a higher price", "the production of a good that has a harmful effect on a third party"], a: 3, why: "A negative externality is a harmful effect on a third party. A, B and C are other causes of or responses to market failure." },
  { q: "[May/June 2022 · 31 · Q3] The private benefit of an activity is greater than the private cost. The social benefit of the same activity is less than the social cost. What must be true of the activity?", opts: ["external benefit = external cost", "external benefit > external cost", "external benefit < external cost", "external benefit > private benefit"], a: 2, why: "Private benefit − private cost > 0 but social benefit − social cost < 0, so the external effects (benefit − cost) must be negative." },
  { q: "[Feb/March 2022 · 32 · Q2] What is equivalent to social benefits?", opts: ["the amount that the government spends on social security benefits", "the benefit gained by society from total government spending", "the benefit to third parties from household consumption of a good", "the private and external benefits from household consumption of a good"], a: 3, why: "Social benefit = private benefit + external benefit. C is only the external part." },
  { q: "[May/June 2023 · 32 · Q6] Which statement is correct?", opts: ["External benefit minus private benefit equals social benefit.", "Private benefit minus external benefit equals social benefit.", "Social benefit minus external benefit equals private benefit.", "Social benefit plus private benefit equals external benefit."], a: 2, why: "Rearranging social benefit = private benefit + external benefit gives private benefit = social benefit − external benefit." },
  { q: "[Oct/Nov 2020 · 33 · Q1] Which statement is correct?", opts: ["marginal social benefit = marginal private benefit – marginal external benefit", "marginal social cost = marginal private cost + marginal external cost", "negative externality = marginal social benefit – marginal social cost", "positive externality = marginal private benefit"], a: 1, why: "MSC = MPC + MEC. In A the sign is wrong." },
  { q: "[Feb/March 2020 · 32 · Q1] Which statement about a product with external costs must be correct?", opts: ["The consumption of the product has positive effects on third parties.", "The private costs of its production exceed the social costs of its production.", "The production of the product has negative effects on third parties.", "The social costs of its production exceed the social benefits of its production."], a: 2, why: "External costs are negative effects on third parties. Social cost exceeds private cost, not the other way round, and D does not follow." },
  { q: "[May/June 2023 · 32 · Q8] Which action would produce a positive externality of production?", opts: ["A child is vaccinated against measles.", "A consumer donates products to a local food bank.", "A firm rebuilds a local road when constructing its new factory.", "A government pays a subsidy to firms producing cars."], a: 2, why: "The firm's production helps third parties who use the road. A is a consumption externality." },
] });
