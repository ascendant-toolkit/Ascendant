const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}

/* ---------- tax types ---------- */
function ttDraw(s) {
  const X = (v) => 80 + v * 6.4, Y = (v) => 250 - v * 4.4; let o = axes(80, 250, 720, 30, "Income", "Tax paid as % of income");
  const L = (f, c, v, name) => { let d = ""; for (let i = 0; i <= 100; i += 4) d += (i ? " L" : "M") + X(i) + "," + Y(f(i)); return SV.path(d, c, { fill: "none", "stroke-width": 3.5, ...op(v) }) + tag(X(100) + 6, Y(f(100)) + 4, name, c, v); };
  o += L((i) => 4 + i * 0.35, "c3", s.a, "Progressive") + L(() => 20, "c4", s.b, "Proportional") + L((i) => 38 - i * 0.24, "c2", s.c, "Regressive");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Tax as a percentage of income rising, flat and falling for progressive, proportional and regressive taxes">${ttDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 300, label: "Tax as a percentage of income under three kinds of tax", base: { a: 0, b: 0, c: 0 }, draw: ttDraw, tween: 800, dwell: 5400, steps: [
  { cap: "<b>Progressive.</b> The share of income paid in tax <b>rises</b> with income, as in an income tax with higher bands. Higher earners pay a bigger proportion.", s: { a: 1 } },
  { cap: "<b>Proportional.</b> Everyone pays the <b>same share</b> of income, for example a flat 20% tax.", s: { a: 1, b: 1 } },
  { cap: "<b>Regressive.</b> The share of income paid in tax <b>falls</b> as income rises, as with sales taxes or fuel duty, because low earners spend more of their income.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- minimum wage ---------- */
function mwDraw(s) {
  const w = s.w, qd = Math.max(0, (90 - w) / 0.8), qs = Math.max(0, (w - 10) / 0.8); let o = axes(70, 270, 720, 25, "Number of workers", "Wage");
  o += SV.line(SDX(0), SDY(90), SDX(100), SDY(10), "c2", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(10) - 4, "Demand for labour", "c2") + SV.line(SDX(0), SDY(10), SDX(100), SDY(90), "c1", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(90), "Supply of labour", "c1");
  o += SV.circle(SDX(50), SDY(50), 5, "dot1");
  if (s.v > 0) { o += SV.line(70, SDY(w), 720, SDY(w), "c4", { "stroke-width": 2.5, ...op(s.v) }) + tag(724, SDY(w) - 6, "Minimum wage", "c4", s.v, "end"); if (qs - qd > 1) o += SV.rect(SDX(qd), SDY(w) - 8, SDX(qs) - SDX(qd), 16, "f3", op(0.7 * s.v)) + SV.circle(SDX(qd), SDY(w), 6, "dot2", op(s.v)) + SV.circle(SDX(qs), SDY(w), 6, "dot1", op(s.v)) + tag(SDX(qs) + 8, SDY(w) + 22, "unemployment " + Lib.fmtN(qs - qd, 0), "c3", s.v); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A minimum wage above the equilibrium wage causes more workers to want jobs than firms will hire">${mwDraw({ w: 65, v: 1 })}</svg>`;
Lib.stepper($("#stW"), { w: 760, h: 300, label: "A minimum wage above the equilibrium wage", base: { w: 65, v: 0 }, draw: mwDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The labour market.</b> Demand for labour slopes down and supply slopes up. The equilibrium wage is $50 for 50 workers.", s: { w: 65, v: 0 } },
  { cap: "<b>A minimum wage of $65</b> is above equilibrium. More people want to work (69) but firms want to hire fewer (31): <b>unemployment</b> of 38.", s: { w: 65, v: 1 } },
  { cap: "<b>Winners and losers.</b> The 31 workers who keep their jobs earn more. Those who lose their jobs, or cannot find one, are worse off. How many jobs are lost depends on the elasticity of demand for labour.", s: { w: 65, v: 1 } },
] });

/* ---------- Lab 1 ---------- */
const taxOf = (y) => 0.2 * Math.max(0, Math.min(y, 30000) - 10000) + 0.4 * Math.max(0, y - 30000);
function labI() {
  if (!$("#iy")) return;
  const y = +$("#iy").value, t = taxOf(y), a = y ? t / y * 100 : 0, m = y < 10000 ? 0 : y < 30000 ? 20 : 40;
  $("#r1").textContent = "$" + Lib.fmtN(t, 0); $("#r2").textContent = Lib.fmtN(a, 1) + "%"; $("#r3").textContent = m + "%";
  $("#rv").textContent = `On $${Lib.fmtN(y, 0)} the tax is $${Lib.fmtN(t, 0)}, an average rate of ${Lib.fmtN(a, 1)}%. The tax on the next dollar (the marginal rate) is ${m}%, ${m > a ? "above" : "equal to"} the average, so the tax is progressive: the average rate rises as income rises, and takes a larger share from higher earners.`;
  const X = (v) => 50 + v / 100000 * 340, Y = (v) => 250 - v * 5; let d = "", o = SV.line(50, 250, 400, 250) + SV.line(50, 250, 50, 40) + SV.text(400, 272, "Income ($)", "sm", { "text-anchor": "end" }) + SV.text(56, 36, "Average tax rate (%)", "sm");
  for (let v = 0; v <= 100000; v += 2000) d += (v ? " L" : "M") + X(v) + "," + Y(v ? taxOf(v) / v * 100 : 0);
  o += SV.path(d, "c3", { fill: "none", "stroke-width": 3 }) + SV.circle(X(y), Y(a), 7, "dot3") + [0, 20, 40, 60, 80, 100].map((v) => SV.text(X(v * 1000), 266, v + "k", "sm", { "text-anchor": "middle" })).join("");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "iy", label: "Income, $ ", min: 5000, max: 100000, step: 5000, value: 45000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labI });
labI();

/* ---------- Lab 2 ---------- */
const INC = [10, 20, 30, 45, 95];
function ginI(arr) { const tot = arr.reduce((a, b) => a + b, 0), c = [0]; arr.slice().sort((a, b) => a - b).forEach((v) => c.push(c[c.length - 1] + v / tot * 100)); let a = 0; for (let i = 1; i < c.length; i++) a += ((c[i - 1] + c[i]) / 2) * 20; return 1 - a / 5000; }
function labR() {
  if (!$("#tr") || !$("#sh")) return;
  const r = +$("#tr").value / 100, sh = +$("#sh").value / 100, rev = r * (15 + 65), post = INC.slice(); post[3] -= r * 15; post[4] -= r * 65; post[0] += rev * sh / 2; post[1] += rev * sh / 2;
  const g0 = ginI(INC), g1 = ginI(post);
  $("#t1").textContent = g0.toFixed(3); $("#t2").textContent = g1.toFixed(3); $("#t3").textContent = "$" + Lib.fmtN(rev, 1) + "k";
  $("#tv").textContent = r === 0 ? "With no tax there is no redistribution and the Gini stays at " + g0.toFixed(3) + "." : `A ${Lib.fmtN(r * 100, 0)}% tax on income above $30k raises $${Lib.fmtN(rev, 1)}k. ${Lib.fmtN(sh * 100, 0)}% of it goes to the poorest two groups, and the Gini falls from ${g0.toFixed(3)} to ${g1.toFixed(3)}. ${sh < 1 ? "The rest is spent on other things, such as public services, which are not counted here." : ""} In practice high rates might also reduce work effort and the revenue raised.`;
  const X = (i) => 50 + i * 70, Y = (v) => 250 - v * 2; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 40) + SV.text(46, 36, "Income ($000)", "sm");
  post.forEach((v, i) => (o += SV.rect(X(i), Y(INC[i]), 24, INC[i] * 2, "f1", op(0.5)) + SV.rect(X(i) + 26, Y(v), 24, v * 2, "f3", op(0.7)) + SV.text(X(i) + 25, 268, "G" + (i + 1), "sm", { "text-anchor": "middle" }) + SV.text(X(i) + 38, Y(v) - 4, Lib.fmtN(v, 0), "sm", { "text-anchor": "middle" })));
  o += SV.text(360, 60, "Left bar: before", "sm", { "text-anchor": "end" }) + SV.text(360, 76, "Right bar: after", "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "tr", label: "Tax rate on income above $30k, % ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g3"), { id: "sh", label: "Share of revenue transferred to the poorest two groups, % ", min: 0, max: 100, step: 10, value: 70, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What kind of tax is it?", buckets: [{"label": "Progressive"}, {"label": "Proportional"}, {"label": "Regressive"}], items: [{"text": "An income tax with rates of 0%, 20% and 40% in bands", "b": 0}, {"text": "A flat 15% tax on all income", "b": 1}, {"text": "A sales tax on food", "b": 2}, {"text": "An inheritance tax with rates rising with the estate's value", "b": 0}, {"text": "A fuel duty of a fixed amount per litre", "b": 2}, {"text": "A flat 10% tax on company profits", "b": 1}, {"text": "A tax on tobacco paid per packet", "b": 2}, {"text": "A capital gains tax charged at higher rates on bigger gains", "b": 0}], done: "Progressive: share rises with income. Proportional: same share. Regressive: share falls as income rises." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Progressive tax", "Takes a larger share of higher incomes"], ["Regressive tax", "Takes a larger share of lower incomes"], ["Marginal rate of tax", "Tax on the extra income earned"], ["Average rate of tax", "Total tax ÷ total income"], ["Transfer payment", "A payment with no output in return, such as a pension"], ["Minimum wage", "A price floor in the labour market"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a minimum wage above equilibrium in order.", items: ["The government sets a minimum wage above the equilibrium wage", "Quantity of labour supplied rises", "Quantity of labour demanded falls", "Unemployment may rise", "Workers who keep their jobs earn more"], done: "Wage floor above equilibrium creates excess supply of labour." });
Lib.calc($("#c1"), { qs: [
  {"q": "Income tax: 0% on the first $10,000, 20% on the next $20,000, 40% above $30,000. How much tax does someone earning $50,000 pay ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.2 × 20,000 + 0.4 × 20,000.", "sol": "4,000 + 8,000 = <b>$12,000</b>."},
  {"q": "What is the average rate of tax on $50,000 (%)?", "a": 24, "unit": "%", "tol": 0.2, "hint": "12,000 ÷ 50,000.", "sol": "<b>24%</b>."},
  {"q": "What is the marginal rate for that person (%)?", "a": 40, "unit": "%", "tol": 0.2, "hint": "The top band.", "sol": "<b>40%</b>, above the average, so progressive."},
  {"q": "A worker's income rises from $20,000 to $28,000 and tax paid rises from $2,000 to $3,600. What is the marginal rate (%)?", "a": 20, "unit": "%", "tol": 0.2, "hint": "1,600 ÷ 8,000.", "sol": "<b>20%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A tax that takes a larger share of income from high earners is:", opts: ["Progressive", "Regressive", "Proportional", "Indirect"], a: 0, why: "Rate rises with income." },
  { q: "A sales tax is usually:", opts: ["Regressive", "Progressive", "Proportional only", "A transfer payment"], a: 0, why: "Poor households spend more of their income." },
  { q: "A transfer payment is:", opts: ["A payment with no output in return", "A payment for work", "A tax", "A subsidy to a firm"], a: 0, why: "For example a pension." },
  { q: "A minimum wage above equilibrium may cause:", opts: ["Unemployment", "A shortage of labour", "Lower wages", "A fall in supply"], a: 0, why: "Excess supply of labour." },
  { q: "Under a progressive tax the marginal rate is:", opts: ["Above the average rate", "Below the average rate", "Zero", "Always equal to it"], a: 0, why: "The next dollar is taxed more." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Progressive", "Rate rises with income."],
  ["Regressive", "Rate falls with income."],
  ["MRT", "Tax on extra income."],
  ["ART", "Total tax ÷ income."],
  ["Transfer payment", "No output in return."],
  ["Minimum wage", "Floor in the labour market."],
  ["State provision", "Help in kind."],
  ["Limits", "Incentives, cost, avoidance."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Three types of tax are listed: a sales tax (VAT) on fuel; a specific tax of 10% on cigarettes; the percentage of income tax on individual earnings increases as taxable income increases. Which combination describes the effect of each of these types of tax? (Feb/March 2022 · 12 · Q17, reworded)", opts: ["VAT progressive, specific tax progressive, income tax regressive", "VAT progressive, specific tax regressive, income tax progressive", "VAT regressive, specific tax progressive, income tax regressive", "VAT regressive, specific tax regressive, income tax progressive"], a: 3, why: "Sales taxes and duties take a larger share of low incomes, so they are regressive. An income tax whose rate rises with income is progressive." },
  { q: "A country uses an income tax under which the first $10 000 of income is tax-free, the next $20 000 is taxed at 20% and any income over $30 000 is taxed at a top rate of 40%. It also levies a sales tax of 10% on most products. Which combination of tax changes is most likely to create a more equal distribution of income? (Feb/March 2024 · 12 · Q14, reworded)", opts: ["a higher tax-free allowance and a higher rate of sales tax", "a higher top rate of income tax and a lower rate of sales tax", "a lower tax-free allowance and more goods exempt from sales tax", "a lower top rate of income tax and fewer goods exempt from sales tax"], a: 1, why: "A higher top rate takes more from the rich, and a lower sales tax (regressive) helps the poor." },
  { q: "What defines a progressive tax? (Feb/March 2025 · 12 · Q25, reworded)", opts: ["All taxpayers pay the same proportion of income in taxes", "Low-income earners pay a lower proportion of income in taxes than high-income earners", "Low-income earners pay less in taxes than high-income earners", "Low-income earners pay more in taxes than high-income earners"], a: 1, why: "Progressive means the proportion of income paid rises with income. Option C only says the amount is lower." },
  { q: "Which combination of tax changes is most likely to be regressive in a developed economy? (May/June 2022 · 12 · Q14, reworded)", opts: ["increasing the rate of wealth tax and raising the rate of sales tax (VAT) on luxury products", "introducing a tax on owning property based on its sales value and increasing the rate of income tax", "reducing the basic rate of income tax and increasing the duty on fuel", "removing the tax-free allowance for income tax and extending sales tax (VAT) to include all food"], a: 3, why: "Taxing all food and removing the allowance take a greater share of low incomes." },
  { q: "A policy that aims to reduce the degree of inequality of income will also reduce the level of employment in a country. What is most likely to be such a policy? (Feb/March 2024 · 12 · Q12, reworded)", opts: ["The effective minimum wage is increased by 25%", "The rate of income tax paid by the lowest band of earners is reduced", "The government increases the level of subsidies given to producers of some merit goods", "The government provides more goods that are regarded as essential"], a: 0, why: "A higher minimum wage lifts pay for those in work but may reduce the number of workers employers hire." },
  { q: "What is an example of a transfer payment? (May/June 2022 · 11 · Q18, reworded)", opts: ["government spending on hospitals", "government spending on motorways", "minimum wage", "welfare benefits"], a: 3, why: "A transfer payment is made without any good or service being produced in return." },
  { q: "What is an example of a transfer payment? (Feb/March 2020 · 12 · Q18, reworded)", opts: ["a household moving savings from one bank account to another", "a monthly repayment on a loan used to buy a new cooker", "the amount paid to transport goods from one city to another", "the payment of student grants by the government"], a: 3, why: "A student grant is paid by the government with no output in return." },
  { q: "What would be a transfer payment? (Feb/March 2021 · 12 · Q15, reworded)", opts: ["the payment made by a company to its shareholders out of its profits", "the payment made for a legal document to transfer ownership of a house", "the payment made to a retired person in the form of a pension", "the payment made to a professional sports team for the transfer of a player"], a: 2, why: "A pension is a transfer payment: income without current production." },
  { q: "Money is paid by the government to an unemployed worker in the form of a benefit. Why is this called a transfer payment? (May/June 2022 · 14 · Q14, reworded)", opts: ["The payment comes from taxes paid by employed workers", "The payment comes from government savings, not current income", "The payment is made without the production of goods and services taking place", "The payment must be spent as directed by the government"], a: 2, why: "A transfer payment is made without production of goods and services." },
  { q: "Government spending for a year includes: pensions for elderly people $200m, welfare payments to sick people $200m, spending on hospitals $150m, payment to unemployed workers $100m, defence spending $100m, teachers' salaries $50m. What is the total of transfer payments by this government? (May/June 2021 · 13 · Q18, reworded)", opts: ["$50m", "$500m", "$750m", "$800m"], a: 1, why: "Transfers are pensions, welfare payments and payments to unemployed: 200 + 200 + 100." },
  { q: "The table shows government expenditure in two periods (period 1, period 2, $000): new roads 200, 350; welfare benefits 600, 450; armed forces pay 500, 550; state pensions 1100, 1350. By how much had transfer payments changed between periods 1 and 2? (May/June 2022 · 13 · Q15, reworded)", opts: ["0", "+100", "+150", "+300"], a: 1, why: "Transfers are welfare benefits (−150) and state pensions (+250): net +100." },
  { q: "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target? (May/June 2021 · 13 · Q28, reworded)", opts: ["economic growth and deregulation", "full employment and increasing the money supply", "income equality and more progressive taxation", "stable prices and decreasing interest rates"], a: 0, why: "Deregulation is a supply-side measure aimed at growth. Progressive taxation and the money supply are not supply-side tools for equality and employment." },
] });
