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

/* ---------- Watch 2: tax systems ---------- */
const INC = [10, 30, 60, 100], TAX = { prog: [0, 4, 14, 30], prop: [2, 6, 12, 20], reg: [1.0, 2.7, 4.8, 6.0] };
function taxBars(s) {
  const H = (r) => (r / 35) * 220; let o = SV.line(60, 300, 740, 300) + SV.line(60, 300, 60, 50) + SV.text(66, 44, "Average tax rate (% of income)", "sm");
  INC.forEach((y, i) => {
    const gx = 100 + i * 160; o += SV.text(gx + 55, 322, "income $" + y + "k", "sm", { "text-anchor": "middle" });
    [["prog", "f1", "t1", s.p], ["prop", "f3", "t3", s.q], ["reg", "f2", "t2", s.r]].forEach(([k, c, t, v], j) => {
      if (v <= 0) return; const r = (TAX[k][i] / y) * 100, x = gx + j * 36;
      o += SV.rect(x, 300 - H(r), 30, H(r), c, op(v)) + SV.text(x + 15, 300 - H(r) - 6, Lib.fmtN(r, 0) + "%", "sm bd " + t, { "text-anchor": "middle", ...op(v) });
    });
  });
  if (s.p > 0) o += SV.text(80, 70, "progressive", "lbl bd t1", op(s.p)); if (s.q > 0) o += SV.text(80, 92, "proportional", "lbl bd t3", op(s.q)); if (s.r > 0) o += SV.text(80, 114, "regressive", "lbl bd t2", op(s.r));
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 345, label: "Average tax rate by income for progressive, proportional and regressive tax systems", base: { p: 0, q: 0, r: 0 }, draw: taxBars, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A progressive income tax.</b> No tax on the first $10k, 20% on income from $10k to $40k, 40% above $40k. Average rates <b>rise</b> with income: 0%, 13%, 23%, 30%. Richer households pay a larger <b>share</b>. The marginal rate (20% then 40%) is above the average rate.", s: { p: 1 } },
  { cap: "<b>A proportional tax.</b> A flat 20% of income. The average rate is the <b>same</b> at every income level.", s: { p: 1, q: 1 } },
  { cap: "<b>A regressive tax.</b> A 10% sales tax, where poorer households spend all their income and richer households save part. The tax takes 10%, 9%, 8% and 6% of income: the average rate <b>falls</b> as income rises.", s: { p: 1, q: 1, r: 1 } },
] });

/* ---------- Lab 2: tax systems ---------- */
const SYS = ["progressive income tax", "proportional (flat) tax", "regressive sales tax"];
function lab2() {
  if (!$("#sy")) return;
  const k = +$("#sy").value, key = ["prog", "prop", "reg"][k - 1], tx = TAX[key];
  tx.forEach((v, i) => { $("#s" + (i + 1)).textContent = "$" + Lib.fmtN(v, 1) + "k (" + Lib.fmtN((v / INC[i]) * 100, 0) + "%)"; });
  $("#sv").textContent = k === 1 ? "Progressive: the average rate rises from 0% to 30% as income rises. Richer households pay a larger share, so it reduces inequality of disposable income."
    : k === 2 ? "Proportional: everyone pays 20% of income. The rich pay more dollars but the same share."
    : "Regressive: the sales tax takes 10% of spending, but richer households spend a smaller share of their income, so the average rate falls with income. It widens inequality of disposable income.";
  const H = (r) => (r / 35) * 200, cls = ["f1", "f3", "f2"][k - 1];
  let o = SV.line(40, 230, 400, 230) + SV.line(40, 230, 40, 20) + SV.text(46, 18, "Average tax rate (%)", "sm");
  INC.forEach((y, i) => { const r = (tx[i] / y) * 100, x = 60 + i * 85; o += SV.rect(x, 230 - H(r), 50, H(r), cls) + SV.text(x + 25, 230 - H(r) - 6, Lib.fmtN(r, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 25, 250, "$" + y + "k", "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "sy", label: "Tax system: ", min: 1, max: 3, step: 1, value: 1, fmt: (v) => SYS[v - 1], onInput: lab2 });

/* ---------- Lab 2: allowance ---------- */
function labAllow() {
  if (!$("#ai") || !$("#ar")) return;
  const inc = +$("#ai").value, r = +$("#ar").value / 100, tax = Math.max(0, inc - 10000) * r, avg = inc ? tax / inc : 0;
  $("#x1").textContent = "$" + Lib.fmtN(tax, 0); $("#x2").textContent = Lib.fmtN(avg * 100, 1) + "%"; $("#x3").textContent = inc > 10000 ? Math.round(r * 100) + "%" : "0%"; $("#x4").textContent = "$" + Lib.fmtN(inc - tax, 0);
  $("#xv").textContent = inc <= 10000 ? "Income is within the tax-free allowance, so no tax is paid: average and marginal rates are zero."
    : `Tax is ${Math.round(r * 100)}% of the $${Lib.fmtN(inc - 10000, 0)} above the allowance, $${Lib.fmtN(tax, 0)}. The average rate (${Lib.fmtN(avg * 100, 1)}%) is below the marginal rate (${Math.round(r * 100)}%) and rises with income: a progressive tax.`;
  const H = (v) => v / 600, base = 200;
  let o = SV.line(30, base, 400, base);
  [[60, inc, "f1", "Income"], [160, tax, "f2", "Tax"], [260, inc - tax, "f3", "After tax"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 70, H(v), c) + SV.text(x + 35, base - H(v) - 6, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 35, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labX").innerHTML = o;
}
Lib.slider($("#g8"), { id: "ai", label: "Income ($): ", min: 5000, max: 100000, step: 5000, value: 30000, fmt: (v) => v.toLocaleString(), onInput: labAllow });
Lib.slider($("#g9"), { id: "ar", label: "Tax rate above $10,000: ", min: 10, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labAllow });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each tax progressive, proportional or regressive (in its effect on the average tax rate)?",
  buckets: [{ label: "Progressive" }, { label: "Proportional" }, { label: "Regressive" }],
  items: [
    { text: "Income tax with higher rates on higher bands", b: 0 }, { text: "Inheritance tax with an exempt first amount", b: 0 }, { text: "A tax-free allowance on income", b: 0 }, { text: "A tax on high-value property", b: 0 },
    { text: "A flat 20% tax on all income", b: 1 }, { text: "A flat 15% tax on profits", b: 1 },
    { text: "A sales tax on food and clothing", b: 2 }, { text: "Tobacco duty", b: 2 }, { text: "A fixed $50 vehicle licence fee", b: 2 },
  ], done: "Look at what happens to the share of income paid as income rises.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Progressive tax", "The average tax rate rises as income rises"],
  ["Proportional tax", "The average tax rate is the same at all incomes"],
  ["Regressive tax", "The average tax rate falls as income rises"],
  ["Direct tax", "A tax on income or wealth"],
  ["Indirect tax", "A tax on spending"],
  ["Average tax rate", "Total tax divided by income"],
  ["Marginal tax rate", "The tax on the next dollar earned"],
  ["Tax-free allowance", "A slice of income on which no tax is paid"],
], done: "Eight words for the tax system." });
Lib.calc($("#c1"), { qs: [
  { q: "A household earning $30,000 pays $6,000 in tax. What is the average tax rate (%)?", a: 20, sol: "6,000 ÷ 30,000 × 100 = <b>20%</b>." },
  { q: "A tax is 0% on income up to $10,000 and 20% above that. How much tax does a person on $30,000 pay ($)?", a: 4000, sol: "20% × (30,000 − 10,000) = <b>$4,000</b>." },
  { q: "The same person's income rises from $30,000 to $40,000 and tax rises from $4,000 to $6,000. What is the marginal tax rate (%)?", a: 20, sol: "Extra tax 2,000 ÷ extra income 10,000 × 100 = <b>20%</b>." },
  { q: "The top 20% of earners pay 45% of their income in income tax and receive 5% in cash benefits. What percentage of their income is disposable?", a: 60, sol: "100 − 45 + 5 = <b>60%</b>." },
  { q: "With a $10,000 allowance and a 20% rate above it, what is the average tax rate for a person on $50,000 (%)?", a: 16, sol: "Tax = 20% × 40,000 = $8,000; 8,000 ÷ 50,000 = <b>16%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A tax whose average rate falls as income rises is:", opts: ["progressive", "proportional", "regressive", "direct"], a: 2, why: "Poorer people pay a bigger share of their income." },
  { q: "A tax with a tax-free allowance and a flat rate above it is:", opts: ["regressive", "proportional", "progressive", "indirect"], a: 2, why: "The average rate rises with income, towards the flat rate." },
  { q: "A sales tax takes a larger share of income from poor households because:", opts: ["the rate is higher for the poor", "poor households spend a larger share of income", "the poor pay more income tax", "it is a direct tax"], a: 1, why: "Spending is a bigger share of a low income, so a tax on spending is regressive." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Progressive tax", "The average tax rate rises as income rises."],
  ["Regressive tax", "The average tax rate falls as income rises."],
  ["Proportional tax", "The average tax rate stays the same at all incomes."],
  ["Average tax rate", "Total tax divided by income."],
  ["Marginal tax rate", "The tax on the next dollar of income."],
  ["Tax-free allowance", "Income below which no tax is paid, making an income tax progressive."],
  ["Disposable income", "Income minus direct taxes plus cash benefits."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2023 · 32 · Q14] Which changes in direct and indirect tax are likely to increase the inequality in the distribution of income in a developed economy? (direct / indirect)", opts: ["fall / fall", "fall / rise", "rise / fall", "rise / remain constant"], a: 1, why: "Cutting progressive direct taxes while raising often-regressive indirect taxes shifts the burden onto lower incomes." },
  { q: "[Feb/March 2023 · 32 · Q16] In a country, the top 20% of earners pay 45% in income tax and 25% on sales taxes, and receive 5% in cash benefits. What is the percentage of disposable income for this group?", opts: ["30%", "55%", "60%", "80%"], a: 2, why: "Disposable income is income minus income tax plus benefits: 100 − 45 + 5 = 60%. Sales taxes are paid out of disposable income and are not subtracted." },
] });
