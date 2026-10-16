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

const QA = [16, 18, 20, 22, 24], QB = [4, 8, 14, 24, 50], QN = ["Poorest 20%", "Next 20%", "Middle 20%", "Next 20%", "Richest 20%"];
function quintChart(s) {
  const base = 320, k = 5; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Average income per head in each fifth of the population ($ thousand)", "sm");
  s.q.forEach((v, i) => { const x = 90 + i * 120, h = v * k; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${i === 0 ? "--bad" : i === 4 ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 45, base - h - 8, "$" + money(v, 0) + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, QN[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  if (s.t) o += SV.text(380, 58, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
const AFTER = [10.75, 14.75, 14, 24, 35];
Lib.stepper($("#stX"), { w: 760, h: 400, label: "Progressive taxes and benefits", base: { q: QB, t: "" }, draw: quintChart, steps: [
  { cap: "Before government action income is <b>very unequal</b>: the richest fifth gets $50,000 a head, the poorest fifth only $4,000.", s: { q: QB, t: "Before tax and benefits" } },
  { cap: "A <b>progressive income tax</b> takes a larger share from high earners: the richest fifth now keeps about $35,000.", s: { q: [4, 8, 14, 24, 35], t: "After progressive tax on the rich" } },
  { cap: "The revenue pays <b>benefits and services</b> to the poorest two fifths. Their incomes rise to about $10,750 and $14,750. The gap narrows: <b>relative poverty falls</b>.", s: { q: AFTER, t: "After benefits: gap narrowed" } },
  { cap: "<b>Evaluate:</b> high tax rates may reduce incentives to work; benefits cost money; administration takes some revenue.", s: { q: AFTER, t: "" } },
] });
function nmwChart(s) {
  const w = s.w, ld = 110 - w, ls = w - 10; let o = axes("Wage", "Number of workers");
  o += curve(-1, 110, "c1", "Demand for labour", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Supply of labour", { t: "t3", dx: -100, dy: 14 });
  o += hline(60, "gr", 50) + vline(50, 60) + SV.circle(QX(50), PY(60), 6, "dot1") + ylab(60, "$60");
  if (s.m > 0.02) { o += `<g opacity="${s.m}">` + SV.line(QX(0), PY(w), QX(100), PY(w), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(w) - 8, "Minimum wage $" + Math.round(w), "lbl bd t2", { "text-anchor": "end" }) + SV.line(QX(ld), PY(w), QX(ld), PY(0), "gr") + SV.line(QX(ls), PY(w), QX(ls), PY(0), "gr") + SV.circle(QX(ld), PY(w), 6, "dot2") + SV.circle(QX(ls), PY(w), 6, "dot2") + SV.text(QX(ld), PY(0) + 18, "Employed " + Math.round(ld), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(ls), PY(0) + 18, "Want work " + Math.round(ls), "sm bd", { "text-anchor": "middle" }) + SV.text(QX((ld + ls) / 2), PY(w) + 22, "Unemployed: " + Math.round(ls - ld), "lbl bd t2", { "text-anchor": "middle", style: halo }) + "</g>"; }
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 400, label: "National minimum wage", base: { w: 80, m: 0 }, draw: nmwChart, steps: [
  { cap: "In a market for low-skilled labour the equilibrium wage is <b>$60</b> and <b>50</b> workers are employed.", s: { w: 80, m: 0 } },
  { cap: "The government sets a <b>national minimum wage of $80</b>, above the equilibrium wage. The low-paid who keep their jobs now earn <b>more</b>: this can reduce poverty.", s: { w: 80, m: 1 } },
  { cap: "But firms demand <b>fewer workers</b> (30) while more people want jobs (70). There are <b>40 unemployed</b>. Those who lose jobs may become poorer.", s: { w: 80, m: 1 } },
  { cap: "If the minimum wage were set <b>below $60</b> it would have no effect. <b>Evaluate:</b> the effect depends on the level, on how sensitive firms are, and it does not help those unable to work.", s: { w: 80, m: 1 } },
] });
const EDU = ["Government spends more on schools and training", "More children and adults gain skills and qualifications", "Workers become more productive", "They can get better-paid jobs and are less likely to be unemployed", "Household incomes rise above the poverty line", "Better health knowledge and the next generation also gain"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "How education reduces poverty", base: { n: 0 }, draw: mkChain(EDU, "--good"), steps: chainSteps(["The government <b>spends more on schools and training</b>.", "More people gain <b>skills and qualifications</b>.", "Workers become <b>more productive</b>.", "They find <b>better-paid jobs</b> and are less likely to be unemployed.", "<b>Household income rises</b> above the poverty line.", "<b>Evaluate:</b> it takes years and costs money, but it helps the next generation too."]) });

/* Lab 1: NMW */
function labN() {
  if (!$("#na")) return;
  const w = +$("#na").value, ld = Math.min(50, 110 - w), ls = Math.max(50, w - 10), un = w > 60 ? ls - ld : 0, wage = Math.max(60, w);
  $("#na1").textContent = "$" + wage; $("#na2").textContent = Math.round(ld); $("#na3").textContent = Math.round(un);
  $("#nav").textContent = w <= 60 ? `A minimum wage of $${w} is at or below the market wage of $60: it has no effect.` : `A minimum wage of $${w} raises pay for the ${Math.round(ld)} workers who keep jobs but ${Math.round(50 - ld)} jobs are lost and ${Math.round(un)} people are unemployed. Whether poverty falls depends on whether the gain to those in work outweighs the loss to those who lose jobs and on the size of the minimum wage.`;
  $("#labN").innerHTML = nmwChart({ w, m: 1 });
}
Lib.slider($("#g1"), { id: "na", label: "National minimum wage", min: 40, max: 100, step: 5, value: 80, fmt: (v) => "$" + v, onInput: labN });
/* Lab 2: tax and benefits */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const t = +$("#ta").value / 100, eff = 1 - +$("#tb").value / 100, rev = QB[4] * t, pool = rev * eff * 5, q = QB.slice();
  q[4] = QB[4] - rev; q[0] = QB[0] + pool / 2; q[1] = QB[1] + pool / 2;
  $("#ta1").textContent = "$" + money(q[0], 1) + "k"; $("#ta2").textContent = "$" + money(q[4], 1) + "k"; $("#ta3").textContent = money(q[4] / q[0], 1) + " times";
  $("#tav").textContent = t === 0 ? "No tax on the richest fifth, so no redistribution. Raise the tax rate." : `The tax raises $${money(rev, 1)}k per rich person; after administration costs it is shared between the poorest two fifths. The poorest fifth rises from $4k to $${money(q[0], 1)}k and the gap falls from ${money(QB[4] / QB[0], 1)} to ${money(q[4] / q[0], 1)} times. ${t > 0.35 ? "At high rates, incentives to work and invest may fall, which is not shown here." : ""}`;
  $("#labT").innerHTML = quintChart({ q, t: "" });
}
Lib.slider($("#g2"), { id: "ta", label: "Progressive tax on the richest fifth", min: 0, max: 60, step: 5, value: 20, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g3"), { id: "tb", label: "Share of revenue lost to administration", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labT });
const PO = [
  { n: "Economic growth", a: "Helps absolute poverty if the poor gain", w: "Jobs and incomes rise; tax revenue pays for services.", c: "Gains may go to the rich; slow; environmental cost." },
  { n: "Education", a: "Both, long run", w: "Skills raise productivity and wages.", c: "Costly; takes years; must match jobs." },
  { n: "Healthcare", a: "Both, long run", w: "Healthy people can work; lower medical costs.", c: "Costly; slow." },
  { n: "State benefits", a: "Absolute, immediately", w: "Direct income for those who cannot earn enough.", c: "Cost to taxpayers; may reduce incentives to work." },
  { n: "Progressive taxation", a: "Relative", w: "Takes more from the rich to fund help for the poor.", c: "May reduce incentives; tax avoidance." },
  { n: "National minimum wage", a: "Relative, for those in work", w: "Raises the pay of the lowest paid.", c: "May cause unemployment; no help for people who cannot work." },
];
button_table("poBtns", "poOut", PO, 0, (p) => `<div class="tw"><table class="t"><tr><th>Mainly helps</th><th>How it works</th><th>The catch</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>policy</b> is each?", buckets: [{ label: "Economic growth" }, { label: "Education or healthcare" }, { label: "Benefits or tax" }, { label: "Minimum wage" }], items: [
  { text: "Policies to raise real GDP and create jobs", b: 0 }, { text: "Investment to expand output and incomes", b: 0 },
  { text: "Free schooling and training", b: 1 }, { text: "Free or subsidised hospital care", b: 1 },
  { text: "Higher unemployment benefit", b: 2 }, { text: "A higher rate of tax on high incomes", b: 2 },
  { text: "A legal lowest hourly wage", b: 3 }, { text: "Raising the wage floor above the market wage", b: 3 },
], done: "Six policies in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>benefit</b> or a <b>cost / problem</b> of the policy?", buckets: [{ label: "Benefit" }, { label: "Cost or problem" }], items: [
  { text: "Raises the pay of the lowest-paid workers", b: 0 }, { text: "Gives income to people who cannot work", b: 0 }, { text: "Raises skills and productivity in the long run", b: 0 }, { text: "Narrows the gap between rich and poor", b: 0 },
  { text: "May cause unemployment among low-skilled workers", b: 1 }, { text: "Costs taxpayers more and may reduce incentives to work", b: 1 }, { text: "Takes years to have an effect", b: 1 }, { text: "High taxes may discourage effort and investment", b: 1 },
], done: "Every policy needs a cost: that is evaluation." });
Lib.match($("#m1"), { prompt: "Match the policy to how it reduces poverty.", pairs: [
  ["Education", "Raises skills so people earn more and find jobs"],
  ["Healthcare", "Healthier people can work and avoid medical bills"],
  ["State benefits", "Gives income to people who cannot earn enough"],
  ["Progressive taxation", "Takes more from the rich to pay for help for the poor"],
  ["National minimum wage", "Sets a floor under pay for the lowest paid"],
  ["Economic growth", "Creates jobs and raises incomes and tax revenue"],
], done: "Link each policy to a mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in government spending might increase poverty</b>.", items: [
  "The government cuts spending on benefits, healthcare and education",
  "Poor households receive less income and fewer services",
  "Their income falls below what they need for basic necessities",
  "Reduced schooling and health care lower skills and productivity",
  "Households find it harder to earn: poverty rises and lasts longer",
], done: "Fiscal policy can reduce or raise poverty." });
Lib.calc($("#c1"), { qs: [
  { q: "The government raises a tax on the rich that brings in $2bn and spends it all on benefits for 1 million poor households. How much extra does each household get ($)?", a: 2000, sol: "$2bn ÷ 1m = <b>$2,000</b>." },
  { q: "A minimum wage of $8 an hour is introduced and a worker works 40 hours. What is her weekly pay ($)?", a: 320, sol: "8 × 40 = <b>$320</b>." },
  { q: "A progressive tax takes 10% of a $20,000 income and 40% of a $100,000 income. How much tax does the high earner pay ($)?", a: 40000, sol: "40% × 100,000 = <b>$40,000</b>." },
  { q: "A benefit raises a poor household's income from $200 to $260 a week. By what percentage has it risen?", a: 30, sol: "60 ÷ 200 × 100 = <b>30%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy would most directly raise the incomes of unemployed people?", opts: ["A cut in income tax for the rich", "An increase in unemployment benefit", "A rise in VAT", "A rise in interest rates"], a: 1, why: "Benefits transfer income to the unemployed." },
  { q: "A possible drawback of a national minimum wage is:", opts: ["It lowers pay", "It may cause unemployment if set too high", "It increases benefits", "It cuts taxes"], a: 1, why: "Firms may hire fewer workers." },
  { q: "Which tax system is most likely to reduce relative poverty?", opts: ["Regressive taxes", "Progressive taxes", "No taxes", "Flat taxes on necessities"], a: 1, why: "Higher rates on high earners fund help for the poor." },
  { q: "How can education reduce poverty?", opts: ["It lowers productivity", "It raises skills and earnings", "It raises prices", "It reduces jobs"], a: 1, why: "Higher skills mean higher wages." },
  { q: "A cut in government spending on benefits is most likely to:", opts: ["Reduce poverty", "Increase poverty", "Raise the minimum wage", "Have no effect"], a: 1, why: "Poor households lose income." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Redistribution of income", "The transfer of income from some people to others, usually from richer to poorer."],
  ["State benefits", "Payments by the government, such as unemployment benefit and pensions."],
  ["Progressive tax", "A tax that takes a larger percentage of income from the rich than the poor."],
  ["National minimum wage", "A legal lowest rate of pay."],
  ["Education", "Learning that raises skills and productivity."],
  ["Healthcare provision", "Government spending on health services."],
  ["Economic growth", "A rise in real GDP over time."],
  ["Fiscal policy", "Government spending and taxation used to influence the economy."],
  ["Targeting", "Aiming help at the households that need it most."],
] });
labN(); labT();
