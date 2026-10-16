/* ---------- model: demand (MPB) P = 100 - Q, private marginal cost MPC = 20 + 0.5Q. External cost / benefit $15 a unit in the animations ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 6.8, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
/* negative production externality */
const QMn = 160 / 3, PMn = 140 / 3, QSn = 130 / 3, PSn = 170 / 3;
function negDraw(s) {
  let o = axes();
  if (s.w > 0) o += SV.poly([[X(QSn), Y(PSn)], [X(QMn), Y(20 + 0.5 * QMn + 15)], [X(QMn), Y(PMn)]], "f2", op(s.w)) + SV.text(X(QMn) + 10, Y(54), "Welfare loss", "lbl bd t2", { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px", ...op(s.w) });
  if (s.d > 0) o += SV.line(X(0), Y(100), X(100), Y(0), "c1", op(s.d)) + SV.text(X(100) - 4, Y(0) - 8, "D = MPB = MSB", "lbl bd t1", { "text-anchor": "end", ...op(s.d) });
  if (s.mpc > 0) o += SV.line(X(0), Y(20), X(100), Y(70), "c3", op(s.mpc)) + SV.text(X(100) - 4, Y(70) + 18, "MPC (supply)", "lbl bd t3", { "text-anchor": "end", ...op(s.mpc) });
  if (s.msc > 0) o += SV.line(X(0), Y(35), X(100), Y(85), "c2", op(s.msc)) + SV.text(X(100) - 4, Y(85) - 8, "MSC = MPC + MEC", "lbl bd t2", { "text-anchor": "end", ...op(s.msc) });
  if (s.tax > 0) o += SV.line(X(15), Y(27.5), X(15), Y(42.5), "c4", { "stroke-width": 5, ...op(s.tax) }) + SV.text(X(15) + 10, Y(20) + 24, "tax = external cost ($15 a unit): shifts MPC up to MSC", "lbl bd t4", { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px", ...op(s.tax) });
  if (s.qm > 0) o += SV.line(X(QMn), Y(PMn), X(QMn), 330, "gr", op(s.qm)) + SV.line(70, Y(PMn), X(QMn), Y(PMn), "gr", op(s.qm)) + SV.circle(X(QMn), Y(PMn), 6, "dot4", op(s.qm)) + SV.text(X(QMn), 350, "Qm = 53", "lbl bd", { "text-anchor": "middle", ...op(s.qm) }) + SV.text(66, Y(PMn) + 4, "47", "sm bd", { "text-anchor": "end", ...op(s.qm) });
  if (s.qs > 0) o += SV.line(X(QSn), Y(PSn), X(QSn), 330, "gr", op(s.qs)) + SV.line(70, Y(PSn), X(QSn), Y(PSn), "gr", op(s.qs)) + SV.circle(X(QSn), Y(PSn), 6, "dot3", op(s.qs)) + SV.text(X(QSn), 350, "Qs = 43", "lbl bd", { "text-anchor": "middle", ...op(s.qs) }) + SV.text(66, Y(PSn) + 4, "57", "sm bd", { "text-anchor": "end", ...op(s.qs) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 370" role="img" aria-label="Demand, private marginal cost and marginal social cost showing overproduction and the welfare loss">${negDraw({ d: 1, mpc: 1, msc: 1, qm: 1, qs: 1, w: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 370, label: "Negative production externality: overproduction, welfare loss and a tax", base: { d: 0, mpc: 0, msc: 0, qm: 0, qs: 0, w: 0, tax: 0 }, draw: negDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Demand and private cost.</b> Demand is the marginal private benefit (and, with no consumption externality, also the marginal social benefit). The supply curve is the firm's <b>marginal private cost</b>.", s: { d: 1, mpc: 1 } },
  { cap: "<b>The free market.</b> Firms produce where MPB = MPC: output <b>53</b>, price <b>$47</b>. The firm ignores the cost that its pollution puts on others.", s: { d: 1, mpc: 1, qm: 1 } },
  { cap: "<b>The external cost.</b> Pollution costs society $15 on every unit. <b>Marginal social cost = MPC + $15</b>, a parallel curve above.", s: { d: 1, mpc: 1, qm: 1, msc: 1 } },
  { cap: "<b>The social optimum.</b> Efficiency needs <b>MSB = MSC</b>: output <b>43</b> and price <b>$57</b>. The market produces 10 units too many at a price that is $10 too low.", s: { d: 1, mpc: 1, qm: 1, msc: 1, qs: 1 } },
  { cap: "<b>Welfare loss.</b> On each unit between 43 and 53 the social cost is greater than the benefit. The triangle (area ½ × 10 × 15 = 75) is the welfare lost through overproduction.", s: { d: 1, mpc: 1, qm: 1, msc: 1, qs: 1, w: 1 } },
  { cap: "<b>Internalising the externality.</b> A tax of $15 a unit, equal to the external cost, shifts the firm's cost curve from MPC up to MSC. The firm now faces the full social cost and the market moves to output 43.", s: { d: 1, mpc: 1, qm: 0.5, msc: 1, qs: 1, w: 0.3, tax: 1 } },
] });

/* positive consumption externality */
const QMp = 160 / 3, PMp = 140 / 3, QSp = 190 / 3, PSp = 155 / 3;
function posDraw(s) {
  let o = axes();
  if (s.w > 0) o += SV.poly([[X(QMp), Y(20 + 0.5 * QMp)], [X(QMp), Y(115 - QMp)], [X(QSp), Y(PSp)]], "f2", op(s.w)) + SV.text(X(QMp) - 10, Y(70), "Welfare loss", "lbl bd t2", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px", ...op(s.w) });
  if (s.mpb > 0) o += SV.line(X(0), Y(100), X(100), Y(0), "c1", op(s.mpb)) + SV.text(X(100) - 4, Y(0) - 8, "D = MPB", "lbl bd t1", { "text-anchor": "end", ...op(s.mpb) });
  if (s.msb > 0) o += SV.line(X(0), Y(115), X(100), Y(15), "c4", op(s.msb)) + SV.text(X(100) - 4, Y(15) - 8, "MSB = MPB + MEB", "lbl bd t4", { "text-anchor": "end", ...op(s.msb) });
  if (s.mc > 0) o += SV.line(X(0), Y(20), X(100), Y(70), "c2", op(s.mc)) + SV.text(X(100) - 4, Y(70) + 18, "MC (supply)", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  if (s.sub > 0) o += SV.line(X(0), Y(5), X(100), Y(55), "c3", { "stroke-dasharray": "6 5", ...op(s.sub) }) + SV.text(X(10), Y(5) + 26, "MC − subsidy of $15", "lbl bd t3", op(s.sub));
  if (s.qm > 0) o += SV.line(X(QMp), Y(PMp), X(QMp), 330, "gr", op(s.qm)) + SV.line(70, Y(PMp), X(QMp), Y(PMp), "gr", op(s.qm)) + SV.circle(X(QMp), Y(PMp), 6, "dot4", op(s.qm)) + SV.text(X(QMp), 350, "Qm = 53", "lbl bd", { "text-anchor": "middle", ...op(s.qm) });
  if (s.qs > 0) o += SV.line(X(QSp), Y(PSp), X(QSp), 330, "gr", op(s.qs)) + SV.circle(X(QSp), Y(PSp), 6, "dot3", op(s.qs)) + SV.text(X(QSp) + 10, 350, "Qs = 63", "lbl bd", { "text-anchor": "start", ...op(s.qs) });
  return o;
}
Lib.stepper($("#stB"), { w: 780, h: 370, label: "Positive consumption externality: underproduction, welfare loss and a subsidy", base: { mpb: 0, msb: 0, mc: 0, qm: 0, qs: 0, w: 0, sub: 0 }, draw: posDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Private benefit and cost.</b> Buyers' demand is the marginal private benefit. The supply curve is marginal cost.", s: { mpb: 1, mc: 1 } },
  { cap: "<b>The free market.</b> Output <b>53</b>, price <b>$47</b>. Buyers only count the benefit to themselves.", s: { mpb: 1, mc: 1, qm: 1 } },
  { cap: "<b>The external benefit.</b> Others gain $15 on every unit (for example from vaccination). <b>MSB = MPB + $15</b>, a parallel curve above demand.", s: { mpb: 1, mc: 1, qm: 1, msb: 1 } },
  { cap: "<b>The social optimum</b> is where MSB = MSC: output <b>63</b>. The market produces <b>too little</b>.", s: { mpb: 1, mc: 1, qm: 1, msb: 1, qs: 1 } },
  { cap: "<b>Welfare loss.</b> On units 53 to 63 the social benefit is greater than the cost, but they are not produced. The triangle (½ × 10 × 15 = 75) is the benefit lost.", s: { mpb: 1, mc: 1, qm: 1, msb: 1, qs: 1, w: 1 } },
  { cap: "<b>Internalising the externality.</b> A subsidy of $15 a unit, equal to the external benefit, lowers the firm's cost curve so that the market moves to the socially best output.", s: { mpb: 1, mc: 1, qm: 0.5, msb: 1, qs: 1, w: 0.3, sub: 1 } },
] });

/* ---------- Lab 1: welfare loss ---------- */
function lab7() {
  if (!$("#mx")) return;
  const m = +$("#mx").value, q = 160 / 3, qs = (80 - m) / 1.5, loss = 0.5 * (q - qs) * m;
  $("#x1").textContent = Lib.fmtN(q, 1); $("#x2").textContent = Lib.fmtN(qs, 1); $("#x3").textContent = Lib.fmtN(q - qs, 1); $("#x4").textContent = Lib.fmtN(loss, 0);
  $("#xv").textContent = m === 0 ? "There is no external cost, so market output and the social optimum are the same: there is no welfare loss."
    : `With an external cost of $${m} a unit the social optimum is ${Lib.fmtN(qs, 1)} units but the market produces ${Lib.fmtN(q, 1)}. The ${Lib.fmtN(q - qs, 1)} extra units each cost society more than they are worth. Welfare loss = ½ × ${Lib.fmtN(q - qs, 1)} × ${m} = ${Lib.fmtN(loss, 0)}. Double the external cost and the loss roughly quadruples.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(qs), y(100 - qs)], [x(q), y(100 - q)], [x(q), y(20 + 0.5 * q + m)]], "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(70), "c3") + SV.line(x(0), y(20 + m), x(100), y(70 + m), "c2");
  o += SV.circle(x(q), y(100 - q), 6, "dot4") + SV.circle(x(qs), y(100 - qs), 6, "dot3") + SV.text(x(q), 288, "Qm", "sm bd t4", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t3", { "text-anchor": "middle" }) + SV.text(x(100) - 4, y(0) - 6, "MPB = MSB", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(70) + 18, "MPC", "sm bd t3", { "text-anchor": "end" }) + (m > 0 ? SV.text(x(100) - 4, y(70 + m) - 6, "MSC", "sm bd t2", { "text-anchor": "end" }) : "");
  $("#labK").innerHTML = o;
}
Lib.slider($("#g12"), { id: "mx", label: "External cost per unit ($): ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab7 });
/* ---------- Lab 4: table of units ---------- */
function lab4() {
  if (!$("#mc4")) return;
  const m = +$("#mc4").value; let priv = 0, soc = 0, rows = "";
  for (let u = 1; u <= 9; u++) {
    const mpb = 100 - 10 * u, mpc = 10 + 10 * u, msc = mpc + m, pOk = mpb >= mpc, sOk = mpb >= msc; if (pOk) priv = u; if (sOk) soc = u;
    rows += `<tr><td>${u}</td><td>${mpb}</td><td>${mpc}</td><td>${msc}</td><td style="color:var(--${pOk ? "good" : "bad"})"><b>${pOk ? "✓ produced" : "✗ stops"}</b></td><td style="color:var(--${sOk ? "good" : "bad"})"><b>${sOk ? "✓ worth it" : "✗ not worth it"}</b></td></tr>`;
  }
  $("#u1").textContent = priv + " units"; $("#u2").textContent = soc + " units"; $("#u3").textContent = (priv - soc) + ((priv - soc) === 1 ? " unit" : " units");
  $("#labD").innerHTML = `<div class="tw"><table class="t"><tr><th>Unit</th><th>MPB</th><th>MPC</th><th>MSC (MPC + ${m})</th><th>Private firm</th><th>Society</th></tr>${rows}</table></div>`;
  $("#uv").textContent = m === 0 ? "No external cost: the private and social optimum are the same." : `The private firm produces while MPB ≥ MPC, so ${priv} units. Society should produce while MPB ≥ MSC, so ${soc} units. The extra ${priv - soc} unit(s) cost more than they are worth: overproduction.`;
}
Lib.slider($("#g7"), { id: "mc4", label: "External cost per unit ($): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does the free market overproduce or underproduce?",
  buckets: [{ label: "Overproduces (or over-consumes)" }, { label: "Underproduces (or under-consumes)" }],
  items: [
    { text: "Smoke from a factory chimney", b: 0 }, { text: "Traffic congestion caused by drivers", b: 0 }, { text: "Noise from aircraft", b: 0 }, { text: "Litter from chewing gum", b: 0 },
    { text: "Vaccination", b: 1 }, { text: "Education", b: 1 }, { text: "A firm training workers who then join rivals", b: 1 }, { text: "Research that other firms can use", b: 1 },
  ], done: "Negative externalities lead to too much, positive externalities to too little.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Qm", "The market output, where the private curves cross"],
  ["Qs", "The socially optimal output, where MSB = MSC"],
  ["Welfare loss", "The loss of net social benefit when output differs from the social optimum"],
  ["Overproduction", "Output above the social optimum, from a negative externality"],
  ["Underproduction", "Output below the social optimum, from a positive externality"],
  ["Allocative efficiency", "Producing where marginal social benefit equals marginal social cost"],
  ["Market failure", "The market allocates resources inefficiently"],
], done: "Seven words for the diagrams." });
Lib.order($("#o1"), { prompt: "Put the explanation of a negative externality of production in order.", items: [
  "The firm produces where MPB = MPC and ignores the cost its pollution puts on others",
  "The marginal social cost is greater than the marginal private cost: MSC = MPC + MEC",
  "The socially efficient output is where MSB = MSC, which is lower than the market output",
  "The market overproduces and the price is too low",
  "The extra units cost more than they are worth, creating a welfare loss",
  "A tax equal to the external cost internalises the externality and moves output to the social optimum",
], done: "This chain works for the 12, 13 and 20 mark diagram questions." });

Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and MPC = 20 + 0.5Q. What is the market output (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives Q = <b>53.3</b>." },
  { q: "The external cost is $15 a unit, so MSC = 35 + 0.5Q. What is the social optimum (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives Q = <b>43.3</b>." },
  { q: "The market overproduces by 10 units. At the market output the gap between MSC and MSB is $15, and it is zero at the social optimum. What is the welfare loss ($)?", a: 75, sol: "A triangle: ½ × 10 × 15 = <b>$75</b>." },
  { q: "The external cost doubles from $15 to $30. The social optimum becomes 33.3 and the market output is still 53.3. What is the welfare loss (½ × base × 30)?", a: 300, sol: "Base = 20, so ½ × 20 × 30 = <b>300</b>, four times the previous loss of 75." },
  { q: "A positive externality of $15 a unit raises the social optimum from 53.3 to 63.3 units. What is the welfare loss (½ × 10 × 15)?", a: 75, sol: "½ × 10 × 15 = <b>$75</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "With a negative production externality, the free market:", opts: ["underproduces", "produces the efficient output", "overproduces", "does not produce"], a: 2, why: "The producer ignores part of the cost, so the price is too low and output too high." },
  { q: "A positive consumption externality leads the market to:", opts: ["overproduce", "underproduce", "produce efficiently", "produce a demerit good"], a: 1, why: "Buyers ignore the external benefit, so MSB > MPB and output is too low." },
  { q: "At the socially optimal output:", opts: ["MPB = MPC", "MSB = MSC", "MSC = MPC", "welfare loss is at its largest"], a: 1, why: "Allocative efficiency needs marginal social benefit equal to marginal social cost." },
  { q: "On a negative externality diagram, the welfare loss is the triangle between:", opts: ["MPC and MPB from 0 to Qs", "MSC and MSB from Qs to Qm", "MSC and MPC at Qs", "the demand curve and the axes"], a: 1, why: "Between Qs and Qm each unit costs society more (MSC) than it is worth (MSB)." },
  { q: "A negative consumption externality shifts which curve?", opts: ["MSB falls below MPB", "MSC rises above MPC", "MSB rises above MPB", "MSC falls below MPC"], a: 0, why: "Consumption harms others, so the social benefit is lower than the private benefit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Qm", "Market output, where MPB = MPC."],
  ["Qs", "Socially optimal output, where MSB = MSC."],
  ["Welfare loss", "Net social benefit lost because output is not at the social optimum."],
  ["Overproduction", "Market output above the social optimum (negative externality)."],
  ["Underproduction", "Market output below the social optimum (positive externality)."],
  ["MSC above MPC", "Negative production externality."],
  ["MSB below MPB", "Negative consumption externality."],
  ["MSC below MPC", "Positive production externality."],
  ["MSB above MPB", "Positive consumption externality."],
  ["Allocative efficiency", "Output where marginal social benefit equals marginal social cost."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q14] When there are positive externalities in consumption, what can be concluded about the output of the market?", opts: ["Output must be above the allocative efficient level.", "Output must be at the allocative efficient level.", "Output must be below the allocative efficient level.", "Output can be above or below the allocative efficient level."], a: 2, why: "Buyers ignore the external benefit, so the market underproduces." },
  { q: "[Oct/Nov 2024 · 32 · Q4] A government makes it compulsory for motorbike riders to wear helmets. What would represent a positive externality of consumption associated with this decision?", opts: ["decreased pressure on the provision of health care", "expenses incurred on surveillance of motorbike riders to ensure compliance", "increased life expectancy of motorbike riders", "increased profits of helmet manufacturers"], a: 0, why: "A benefit that falls on a third party (the health system and taxpayers). C is a private benefit to the riders themselves." },
  { q: "[Oct/Nov 2023 · 32 · Q3] Negative externalities, such as air pollution due to car emissions, can cause damage to people's health in cities. Which response is most likely to occur from this situation?", opts: ["car manufacturers will automatically bear any external costs", "market failure will be resolved when private costs equal external costs", "most people will decide to use buses rather than cars", "some form of government intervention to improve economic efficiency"], a: 3, why: "The market does not correct the external cost on its own, so intervention is likely. A is the opposite of an externality and B confuses private and external costs." },
] });
