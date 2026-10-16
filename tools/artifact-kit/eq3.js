/* ---------- data: income shares of five equal groups (poorest to richest) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const BASE = [5, 9, 14, 22, 50], AFTER = [8, 12, 16, 23, 41], halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const cumOf = (s) => { const t = s.reduce((a, b) => a + b, 0); let c = 0; return [0, ...s.map((v) => (c += (v / t) * 100))]; };
const ginOf = (s) => { const y = cumOf([...s].sort((a, b) => a - b)); let sum = 0; for (let i = 1; i < y.length; i++) sum += y[i - 1] / 100 + y[i] / 100; return 1 - 0.2 * sum; };
const FL = { x0: 60, y0: 300, w: 300, h: 250 }, LX = (p) => FL.x0 + (p / 100) * FL.w, LY = (v) => FL.y0 - (v / 100) * FL.h;
const lorAxes = () => SV.line(FL.x0, FL.y0, FL.x0 + FL.w + 8, FL.y0) + SV.line(FL.x0, FL.y0, FL.x0, FL.y0 - FL.h - 8) + SV.text(FL.x0 + FL.w + 8, FL.y0 + 36, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(FL.x0 + 6, FL.y0 - FL.h - 14, "Cumulative % of income", "sm");
function lorenzPath(cum, n) {
  const pts = [], f = Math.floor(n), fr = n - f;
  for (let i = 0; i <= Math.min(f, 5); i++) pts.push([LX(i * 20), LY(cum[i])]);
  if (f < 5 && fr > 0) pts.push([LX(f * 20 + fr * 20), LY(cum[f] + (cum[f + 1] - cum[f]) * fr)]);
  return pts;
}

/* ---------- Watch 3: poverty trap ---------- */
const TX = (e) => 70 + e * 30, TY = (v) => 330 - v * 18;
function trapDraw(s) {
  let o = SV.line(70, 330, 690, 330) + SV.line(70, 330, 70, 40) + SV.text(690, 366, "Earnings ($k)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Net income ($k)", "sm");
  [0, 5, 10, 15, 20].forEach((e) => { o += SV.text(TX(e), 348, e, "sm", { "text-anchor": "middle" }); });
  [0, 4, 8, 12, 16].forEach((v) => { o += SV.text(62, TY(v) + 4, v, "sm", { "text-anchor": "end" }); });
  if (s.b > 0) o += SV.line(TX(0), TY(8), TX(20), TY(8), "gr", { "stroke-dasharray": "5 4", ...op(s.b) }) + SV.circle(TX(0), TY(8), 6, "dot1", op(s.b)) + SV.text(TX(0) + 12, TY(8) - 10, "benefit $8k with no earnings", "lbl bd t1", { ...halo, ...op(s.b) });
  if (s.t > 0) o += SV.line(TX(0), TY(8), TX(20), TY(8 + 0.8 * 20), "c1", { "stroke-dasharray": "6 4", ...op(s.t) }) + SV.text(TX(13) + 4, TY(8 + 0.8 * 13) - 8, "keeps benefit, pays 20% tax", "lbl bd t1", { ...halo, ...op(s.t) });
  if (s.w > 0) {
    const pts = []; for (let e = 0; e <= 20; e += 0.5) pts.push([TX(e), TY(0.8 * e + Math.max(0, 8 - 0.8 * e))]);
    o += SV.path(Lib.ptsPath(pts), "c2", { "stroke-width": 4, ...op(s.w) }) + SV.rect(TX(0), TY(8) - 7, TX(10) - TX(0), 14, "f2", op(s.w)) + SV.text(TX(5), TY(8) + 30, "POVERTY TRAP: earning more gains nothing", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.w) }) + SV.text(TX(17), TY(0.8 * 17) + 22, "benefit exhausted: net income rises again", "sm bd t2", { "text-anchor": "end", ...halo, ...op(s.w) });
  }
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 370, label: "Net income against earnings for a household whose means-tested benefit is withdrawn as earnings rise", base: { b: 0, t: 0, w: 0 }, draw: trapDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The benefit.</b> With no earnings, the household receives a means-tested benefit of $8k.", s: { b: 1 } },
  { cap: "<b>If the benefit were kept</b> and only the 20% income tax applied, each extra $1 earned would add 80 cents of net income. The dashed line slopes up steadily.", s: { b: 1, t: 1 } },
  { cap: "<b>But the benefit is withdrawn</b> at 80 cents for each $1 earned. Together with the 20% tax, the household loses <b>100%</b> of extra earnings (an effective marginal tax rate of 100%). Net income stays flat at $8k until the benefit runs out at $10k of earnings. This is the <b>poverty trap</b>: no incentive to work more.", s: { b: 1, t: 0.3, w: 1 } },
] });

/* ---------- Lab 3: poverty trap ---------- */
function lab3() {
  if (!$("#wr") || !$("#it")) return;
  const w = +$("#wr").value / 100, t = +$("#it").value / 100, emtr = t + w, net = 1000 * (1 - emtr);
  $("#t1").textContent = Math.round(emtr * 100) + "%"; $("#t2").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 0);
  $("#tv").textContent = emtr >= 1 ? `Effective marginal tax rate ${Math.round(emtr * 100)}%: the worker ${emtr === 1 ? "gains nothing" : "is worse off"} from earning an extra $1,000. This is a poverty trap: there is no financial incentive to earn more.`
    : emtr > 0.7 ? `The worker keeps only $${Lib.fmtN(net, 0)} of an extra $1,000. The incentive to earn more is weak.`
    : `The worker keeps $${Lib.fmtN(net, 0)} of the extra $1,000. Lower withdrawal of benefits means a stronger incentive to work, but the benefit costs the government more to keep paying.`;
  const H = (v) => 150 * (Math.abs(v) / 1000), bw = 70, base = 190;
  let o = SV.line(30, base, 400, base);
  [[30, 1000, "f1", "Extra earnings"], [120, 1000 * t, "f2", "Income tax"], [210, 1000 * w, "f4", "Benefit lost"], [300, net, net >= 0 ? "f3" : "f2", "Extra net income"]].forEach(([x, v, c, l]) => { o += SV.rect(x, v >= 0 ? base - H(v) : base, bw, H(v), c) + SV.text(x + bw / 2, v >= 0 ? base - H(v) - 6 : base + H(v) + 14, (v < 0 ? "−" : "") + "$" + Lib.fmtN(Math.abs(v), 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 244, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "wr", label: "Benefit withdrawn per $1 of extra earnings: ", min: 0, max: 100, step: 5, value: 70, fmt: (v) => v + "%", onInput: lab3 });
Lib.slider($("#g5"), { id: "it", label: "Income tax rate: ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: lab3 });

/* ---------- Lab 4: redistribution ---------- */
function lab4() {
  if (!$("#rt")) return;
  const t = +$("#rt").value / 100, tx = t * 50, fin = [BASE[0] + tx / 2, BASE[1] + tx / 2, BASE[2], BASE[3], BASE[4] - tx], g = ginOf(fin);
  $("#u1").textContent = Lib.fmtN(fin[0], 1) + "%"; $("#u2").textContent = Lib.fmtN(fin[4], 1) + "%"; $("#u3").textContent = Lib.fmtN(g, 2);
  $("#uv").textContent = t === 0 ? `No redistribution: the Gini is ${Lib.fmtN(ginOf(BASE), 2)}.`
    : `The richest 20% pay ${Math.round(t * 100)}% of their income (${Lib.fmtN(tx, 1)} points of national income), and the revenue goes to the poorest 40%. The Gini falls from ${Lib.fmtN(ginOf(BASE), 2)} to ${Lib.fmtN(g, 2)}. A very high rate could reduce the incentive to earn and the revenue, which this simple model ignores.`;
  const H = (v) => (v / 55) * 170, bw = 28; let o = SV.line(30, 220, 400, 220) + SV.text(32, 20, "% of national income", "sm");
  ["poorest", "2nd", "3rd", "4th", "richest"].forEach((l, i) => { const x = 40 + i * 70; o += SV.rect(x, 220 - H(BASE[i]), bw, H(BASE[i]), "f1") + SV.text(x + bw / 2, 220 - H(BASE[i]) - 5, BASE[i], "sm bd t1", { "text-anchor": "middle" }) + SV.rect(x + bw + 2, 220 - H(fin[i]), bw, H(fin[i]), "f3") + SV.text(x + bw + 2 + bw / 2, 220 - H(fin[i]) - 5, Lib.fmtN(fin[i], 0), "sm bd t3", { "text-anchor": "middle" }) + SV.text(x + bw, 238, l, "sm", { "text-anchor": "middle" }); });
  o += SV.text(40, 258, "blue = before, green = after tax and benefits", "sm");
  $("#labD").innerHTML = o;
}
Lib.slider($("#g6"), { id: "rt", label: "Tax on the richest 20% (share of their income): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl2"), {
  prompt: "Which type of policy to reduce inequality is each one?",
  buckets: [{ label: "Fiscal policy (tax and benefits)" }, { label: "Supply-side policy" }, { label: "Labour market policy" }],
  items: [
    { text: "A more progressive income tax", b: 0 }, { text: "Means-tested child benefit", b: 0 }, { text: "An inheritance tax", b: 0 }, { text: "Free school meals paid for by the state", b: 0 },
    { text: "Subsidised training for the unemployed", b: 1 }, { text: "More investment in schools in poor regions", b: 1 }, { text: "Better transport links to deprived areas", b: 1 },
    { text: "A national minimum wage", b: 2 }, { text: "Laws against pay discrimination", b: 2 },
  ], done: "Fiscal policy works through tax and spending; supply-side raises skills and productive capacity; labour market policy changes pay and conditions.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Transfer payment", "A payment such as a benefit with no good or service produced in return"],
  ["Means-tested benefit", "A benefit paid only to people below an income or wealth level"],
  ["Universal benefit", "A benefit paid to everyone who qualifies, whatever their income"],
  ["Poverty trap", "Little gain from earning more because benefits are withdrawn and tax is paid"],
  ["Supply-side policy", "A policy that raises the productive capacity or skills of workers"],
  ["Fiscal policy", "Use of government spending and taxation"],
  ["Equity versus efficiency", "The trade-off between a fairer distribution and incentives"],
], done: "Seven words for redistribution." });
Lib.calc($("#c1"), { qs: [
  { q: "Benefits are withdrawn at 70 cents per $1 earned and income tax is 30%. What share of an extra $100 earned does the worker keep ($)?", a: 0, hint: "Effective marginal tax rate = 70% + 30%.", sol: "Effective rate 100%, so the worker keeps <b>$0</b>: a poverty trap." },
  { q: "A means-tested benefit is withdrawn at 60 cents for each $1 earned and income tax is 20%. How much of an extra $100 of earnings does the worker keep ($)?", a: 20, sol: "Tax $20 + benefit lost $60 = $80 lost. Worker keeps <b>$20</b>." },
  { q: "A worker is offered a job that adds $200 to monthly earnings. Tax is $40 and benefits fall by $120. What is the net gain ($)?", a: 40, sol: "200 − 40 − 120 = <b>$40</b>." },
  { q: "The effective marginal tax rate in that case is (tax + benefit lost) ÷ extra earnings. What is it (%)?", a: 80, sol: "(40 + 120) ÷ 200 × 100 = <b>80%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is most likely to reduce income inequality?", opts: ["A more regressive tax system", "A more progressive income tax with transfer payments", "Cuts in education spending", "Higher sales taxes on necessities"], a: 1, why: "Richer households pay more and poorer ones receive more." },
  { q: "A poverty trap exists when:", opts: ["a worker gains little from earning more because benefits are withdrawn", "income tax is zero", "everyone earns the same", "wealth is equally distributed"], a: 0, why: "A very high effective marginal tax rate removes the incentive to work more." },
  { q: "Which policy is a supply-side way to reduce inequality?", opts: ["a higher top rate of income tax", "free education and training", "a cash benefit for pensioners", "a wealth tax"], a: 1, why: "It raises earning power rather than redistributing existing income." },
  { q: "The poverty trap is most likely when:", opts: ["benefits are universal", "benefits are withdrawn quickly as earnings rise", "income tax is zero", "wages fall"], a: 1, why: "A high withdrawal rate leaves the worker keeping little of any extra earnings." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Transfer payment", "A payment such as a benefit with no good or service produced in return."],
  ["Means-tested benefit", "A benefit paid only to people with income or wealth below a set level."],
  ["Poverty trap", "Little or no gain from earning more because benefits are withdrawn and tax is paid."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2022 · 32 · Q15] When is a policy of income redistribution from rich people to poor people most appropriate?", opts: ["when control of demand-pull inflation is the priority", "when equality is valued more highly than efficiency", "when monetary reward is the best incentive to risk-taking", "when the rich have higher marginal utility curves than the poor"], a: 1, why: "Redistribution trades some efficiency for equity, so it fits best where equality is valued more. D has the marginal utility argument the wrong way round: the rich have lower marginal utility of income." },
  { q: "[Feb/March 2020 · 32 · Q15] Which combination of policy changes is most likely to redistribute income from the richest households to the poorest households in an economy? (indirect taxes / means-tested benefits / benefits for everyone)", opts: ["decrease / increase / decrease", "decrease / increase / increase", "increase / decrease / increase", "increase / decrease / decrease"], a: 0, why: "Lower indirect taxes (often regressive), more targeted means-tested benefits and fewer universal benefits (which also go to the rich) move income towards the poorest." },
  { q: "[Feb/March 2021 · 32 · Q16] In which circumstances is a poverty trap least likely to operate?", opts: ["A female worker is paid less than a male worker for doing the same job.", "A worker is paid the minimum wage and refuses a higher paid job because net income is lower after tax.", "A worker refuses higher paid work as it means more expensive travel and childcare costs.", "An unemployed worker refuses a job because earnings are less than unemployment benefit."], a: 0, why: "B, C and D are all cases where working more brings little or no gain. A is discrimination, not a poverty trap." },
  { q: "[May/June 2020 (not sat) · 31 · Q20] Young workers find it especially difficult to get a job during a recession. A government introduces a transfer payment for those seeking work and provides information on vacancies. What should be a positive outcome for those seeking work?", opts: ["Firms no longer need to advertise jobs because there are few vacancies.", "No production of goods or services is required for a transfer payment.", "Obtaining information on jobs available makes the labour market more perfect.", "Students will leave their studies to join the workforce at an earlier age."], a: 2, why: "Better information moves the labour market towards perfect information, helping match workers to jobs. B is true of transfer payments but is not a benefit for the job seeker." },
  { q: "[Feb/March 2021 · 32 · Q20] The diagram shows Lorenz curves for a developed economy, X (before) and Y (after, closer to the line of equality). Which combination of supply-side policies would shift the Lorenz curve from X to Y? (top rate of income tax, education, national minimum wage)", opts: ["increase, free, increase", "increase, students pay, abolish", "reduce, free, abolish", "reduce, students pay, increase"], a: 0, why: "Moving the curve towards equality needs a higher top tax rate, free education that raises the skills of low earners, and a higher minimum wage." },
] });
