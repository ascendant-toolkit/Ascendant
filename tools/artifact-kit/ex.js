/* ---------- model: demand (MPB) P = 100 - Q, private marginal cost MPC = 20 + 0.5Q. External cost / benefit $15 a unit in the animations ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 6.8, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price and cost ($)", "sm");

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

/* ---------- Watch 3: cost-benefit analysis ---------- */
const R = 0.05, f = (t) => 1 / (1 + R) ** t, PVA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].reduce((a, t) => a + f(t), 0);
const CX = (t) => 90 + t * 58, SC = 0.3, BASE = 150;
function cbaDraw(s) {
  let o = SV.line(60, BASE, 700, BASE) + SV.text(745, 366, "Years", "sm", { "text-anchor": "end" });
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
  ["Marginal social cost", "Marginal private cost plus marginal external cost"],
  ["Marginal social benefit", "Marginal private benefit plus marginal external benefit"],
  ["Negative externality", "A third party suffers a cost they did not agree to"],
  ["Internalise an externality", "Make the decision-maker face the full social cost or benefit"],
  ["Welfare loss", "The loss of net social benefit when output differs from the social optimum"],
  ["Cost-benefit analysis", "Counting all private and external costs and benefits of a project in money terms"],
  ["Net present value", "Discounted benefits minus discounted costs"],
], done: "These eight cover most of the chapter." });
Lib.order($("#o1"), { prompt: "Put the explanation of a negative externality of production in order.", items: [
  "The firm produces where MPB = MPC and ignores the cost its pollution puts on others",
  "The marginal social cost is greater than the marginal private cost: MSC = MPC + MEC",
  "The socially efficient output is where MSB = MSC, which is lower than the market output",
  "The market overproduces and the price is too low",
  "The extra units cost more than they are worth, creating a welfare loss",
  "A tax equal to the external cost internalises the externality and moves output to the social optimum",
], done: "This chain works for the 12, 13 and 20 mark diagram questions." });
Lib.calc($("#c1"), { qs: [
  { q: "MPC is $40 and the marginal external cost is $12. What is the marginal social cost ($)?", a: 52, sol: "MSC = MPC + MEC = 40 + 12 = <b>$52</b>." },
  { q: "MPB is $60 and the marginal external benefit is $15. What is the marginal social benefit ($)?", a: 75, sol: "MSB = MPB + MEB = <b>$75</b>." },
  { q: "A project has private cost 400, private benefit 440, social cost 450 and social benefit 480. What is the net external cost ($ million)?", a: 10, hint: "External cost = social cost − private cost. External benefit = social benefit − private benefit.", sol: "External cost 50, external benefit 40, so the net external cost is <b>$10 million</b>." },
  { q: "The marginal external cost is $15 a unit. What per-unit tax would internalise it ($)?", a: 15, sol: "A tax equal to the marginal external cost: <b>$15</b>." },
  { q: "The market overproduces by 10 units. At the market output the gap between MSC and MSB is $15, and it is zero at the social optimum. What is the welfare loss ($)?", a: 75, sol: "A triangle: ½ × 10 × 15 = <b>$75</b>." },
  { q: "A benefit of $110 arrives in one year. The discount rate is 10%. What is its present value ($)?", a: 100, sol: "110 ÷ 1.10 = <b>$100</b>." },
  { q: "The marginal external benefit is $15 a unit. What per-unit subsidy would internalise it ($)?", a: 15, sol: "A subsidy equal to the marginal external benefit: <b>$15</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Social cost equals:", opts: ["private cost minus external cost", "private cost plus external cost", "external cost only", "private benefit plus external cost"], a: 1, why: "Social cost = private cost + external cost." },
  { q: "With a negative production externality, the free market:", opts: ["underproduces", "produces the efficient output", "overproduces", "does not produce"], a: 2, why: "The producer ignores part of the cost, so the price is too low and output too high." },
  { q: "Vaccination is an example of:", opts: ["a negative production externality", "a positive consumption externality", "a public good", "a demerit good"], a: 1, why: "The consumer's action benefits third parties, so MSB > MPB." },
  { q: "A tax equal to the marginal external cost:", opts: ["raises output to the social optimum", "internalises the externality", "removes all costs", "makes the good a public good"], a: 1, why: "The firm now faces the full social cost." },
  { q: "Why is cost-benefit analysis difficult?", opts: ["Future benefits do not need discounting", "External costs and benefits are hard to value in money", "Private costs are unknown", "It ignores externalities"], a: 1, why: "Putting a monetary value on pollution, time or health is difficult and uncertain." },
  { q: "A positive consumption externality leads the market to:", opts: ["overproduce", "underproduce", "produce efficiently", "produce a demerit good"], a: 1, why: "Buyers ignore the external benefit, so MSB > MPB and output is too low." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Private cost", "Cost paid by the producer or consumer making the decision."],
  ["External cost", "Cost imposed on a third party and not paid by the decision-maker."],
  ["Social cost", "Private cost plus external cost."],
  ["Private benefit", "Benefit received by the consumer or producer."],
  ["External benefit", "Benefit received by a third party who did not pay."],
  ["Social benefit", "Private benefit plus external benefit."],
  ["Externality", "A spill-over cost or benefit to a third party that is not reflected in the market price."],
  ["MSC = MPC + MEC", "Marginal social cost is private plus external cost."],
  ["MSB = MPB + MEB", "Marginal social benefit is private plus external benefit."],
  ["Welfare loss", "The loss of net social benefit when output differs from the social optimum (MSB = MSC)."],
  ["Internalising the externality", "Making the decision-maker bear the full social cost or gain the full social benefit."],
  ["Tax for a negative externality", "A per-unit tax equal to the marginal external cost shifts MPC up to MSC."],
  ["Subsidy for a positive externality", "A per-unit subsidy equal to the marginal external benefit moves output to the social optimum."],
  ["Cost-benefit analysis", "A method of valuing all private and external costs and benefits of a project over time."],
  ["Net present value", "Present value of benefits minus present value of costs. Go ahead if positive."],
] });

/* ---------- Past paper MCQ (text) ---------- */
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
  { q: "[May/June 2021 · 31 · Q14] When there are positive externalities in consumption, what can be concluded about the output of the market?", opts: ["Output must be above the allocative efficient level.", "Output must be at the allocative efficient level.", "Output must be below the allocative efficient level.", "Output can be above or below the allocative efficient level."], a: 2, why: "Buyers ignore the external benefit, so the market underproduces." },
  { q: "[May/June 2025 · 32 · Q8] The marginal social benefit of consuming a drink is less than the marginal private benefit. What would be the best policy to improve resource allocation in this market?", opts: ["give a subsidy to the producers of the drink", "increase competition in the drink industry", "impose a maximum price for the drink above the market equilibrium price", "impose a per unit tax on the drink"], a: 3, why: "MSB < MPB means a negative consumption externality: the drink is over-consumed. A tax raises the price and cuts consumption." },
] });
