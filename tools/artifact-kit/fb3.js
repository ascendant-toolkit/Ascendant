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
const D = (b) => [-b, 50 + 50 * b], S = (d, shift = 0) => [d, 50 - 50 * d + shift];
const fmtSteep = (v) => (v < 0.8 ? "flat (elastic)" : v > 1.4 ? "steep (inelastic)" : "medium");
const money = (v, d = 1) => Lib.fmtN(v, d);
/* ---------- 3. progressive, proportional, regressive ---------- */
const RX = (inc) => 70 + inc * 0.55, RY = (r) => 330 - r * 5.4;
const SERIES = {
  pr: { name: "Progressive", c: "c1", t: "t1", pts: [[100, 10, 10], [500, 20, 100], [1000, 40, 400]] },
  pp: { name: "Proportional", c: "c3", t: "t3", pts: [[100, 25, 25], [500, 25, 125], [1000, 25, 250]] },
  rg: { name: "Regressive", c: "c2", t: "t2", pts: [[100, 40, 40], [500, 30, 150], [1000, 20, 200]] },
};
function ratesChart(s) {
  let o = SV.line(RX(0), RY(55), RX(0), RY(0)) + SV.line(RX(0), RY(0), RX(1060), RY(0));
  [10, 20, 30, 40, 50].forEach((r) => (o += SV.line(RX(0), RY(r), RX(1000), RY(r), "gr") + SV.text(RX(0) - 8, RY(r) + 4, r + "%", "sm", { "text-anchor": "end" })));
  [100, 500, 1000].forEach((i) => (o += SV.text(RX(i), RY(0) + 18, "$" + i, "sm", { "text-anchor": "middle" })));
  o += SV.text(RX(0) + 6, RY(55) + 4, "Tax paid as % of income", "sm") + SV.text(RX(1060), RY(0) + 38, "Income", "sm", { "text-anchor": "end" });
  Object.keys(SERIES).forEach((key) => {
    const sr = SERIES[key], v = s[key];
    if (v <= 0.02) return;
    let g = SV.path(ptsPath(sr.pts.map((p) => [RX(p[0]), RY(p[1])])), sr.c);
    sr.pts.forEach((p) => (g += SV.circle(RX(p[0]), RY(p[1]), 5, "dot" + sr.c.slice(1)) + SV.text(RX(p[0]) + 9, RY(p[1]) + (key === "pr" ? 20 : -9), "$" + p[2] + " tax", "sm bd", { "text-anchor": "start", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" })));
    g += SV.text(RX(1000) + 16, RY(sr.pts[2][1]) + 4, sr.name, "lbl bd " + sr.t);
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Progressive, proportional and regressive taxes", base: { pr: 0, pp: 0, rg: 0 }, draw: ratesChart, steps: [
  { cap: "<b>Progressive:</b> as income rises from $100 to $500 to $1,000 the <b>percentage</b> paid rises from 10% to 20% to 40%. Income tax usually works like this. The rich pay more dollars and a bigger share.", s: { pr: 1, pp: 0, rg: 0 } },
  { cap: "<b>Proportional:</b> the percentage stays at <b>25%</b> whatever the income. The dollar amount still rises ($25, $125, $250) but the share does not.", s: { pr: 1, pp: 1, rg: 0 } },
  { cap: "<b>Regressive:</b> the percentage <b>falls</b> as income rises, from 40% to 30% to 20%. The poor pay a bigger share of their income. A fixed charge per litre of petrol is an example: the rich buy more litres but not in proportion to their income.", s: { pr: 1, pp: 1, rg: 1 } },
  { cap: "In all three the <b>total tax paid</b> usually rises with income. What differs is the <b>percentage</b>. Only a progressive tax redistributes from rich to poor.", s: { pr: 1, pp: 1, rg: 1 } },
] });

/* ---------- 4. incidence ---------- */
function taxChart(s) {
  const b = s.b, d = s.d, t = s.t, q1 = 50 - t / (b + d), pc = 50 + (b * t) / (b + d), pp = pc - t;
  let o = axes();
  if (t > 0.01) {
    o += SV.rect(QX(0), PY(pc), QX(q1) - QX(0), PY(50) - PY(pc), "f2");
    o += SV.rect(QX(0), PY(50), QX(q1) - QX(0), PY(pp) - PY(50), "f4");
    if (s.inc > 0.5) {
      o += SV.text(QX(q1 / 2), (PY(pc) + PY(50)) / 2 + 4, "Consumers' share: " + money(pc - 50), "lbl bd t2", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
      o += SV.text(QX(q1 / 2), (PY(50) + PY(pp)) / 2 + 4, "Producers' share: " + money(50 - pp), "lbl bd t4", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
      o += SV.text(QX(q1 / 2), PY(pp) + 22, "Tax revenue = " + money(t * q1, 0), "lbl bd", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
    }
  }
  const [dm, dc] = D(b), [sm, sc] = S(d), [tm, tc] = S(d, t);
  o += curve(dm, dc, "c1", "D", { t: "t1" }) + curve(sm, sc, "c3", "S₁", { t: "t3", attrs: { opacity: t > 0.01 ? 0.55 : 1 } });
  if (t > 0.01) o += curve(tm, tc, "c2", "S₂", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P = 50") + xlab(50, "Q = 50");
  o += SV.circle(QX(50), PY(50), 6, "dot1", { opacity: t > 0.01 ? 0.5 : 1 });
  if (t > 0.01) { o += hline(pc, "gr", q1) + vline(q1, pc) + SV.circle(QX(q1), PY(pc), 6, "dot2") + ylab(pc, "P₁ = " + money(pc)) + ylab(pp, "Pp = " + money(pp)) + hline(pp, "gr", q1) + SV.text(QX(q1), PY(0) + (Math.abs(q1 - 50) < 9 ? 34 : 18), "Q₁ = " + money(q1), "sm", { "text-anchor": "middle" }); }
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Incidence of an indirect tax", base: { b: 1, d: 1, t: 0, inc: 0 }, draw: taxChart, steps: [
  { cap: "A market for a good in equilibrium at <b>price 50, quantity 50</b>. Demand D and supply S₁.", s: { b: 1, d: 1, t: 0, inc: 0 } },
  { cap: "The government puts an <b>indirect tax of 20 per unit</b> on the good. Firms' costs rise by 20 at every quantity, so supply shifts <b>to the left</b> (up) by the amount of the tax, to S₂.", s: { t: 20, inc: 0 } },
  { cap: "The new equilibrium: consumers pay a <b>higher price (60)</b> and buy <b>less (40)</b>. Producers hand 20 to the government, so they keep 60 − 20 = <b>40</b>.", s: { t: 20, inc: 0 } },
  { cap: "<b>Incidence</b> is who bears the burden. Consumers bear the rise in price (10), producers bear the rest (10). <b>Tax revenue</b> = 20 × 40 = 800.", s: { t: 20, inc: 1 } },
  { cap: "Make demand <b>steeper (inelastic)</b>. Buyers have few alternatives, so producers can pass on most of the tax: <b>consumers bear most of it</b>. Cigarettes and petrol are examples.", s: { t: 20, inc: 1, b: 3 } },
  { cap: "Make demand <b>flatter (elastic)</b>. Buyers would switch away, so firms cannot raise the price much and <b>producers bear most of the tax</b>.", s: { t: 20, inc: 1, b: 0.3 } },
] });

/* Lab 3: tax systems. Progressive: 10% to 200, 30% 200-600, 50% above. Regressive: fuel duty 16 + 0.02 * income. */
const taxProg = (y) => 0.1 * Math.min(y, 200) + 0.3 * clamp(y - 200, 0, 400) + 0.5 * Math.max(0, y - 600);
const taxProp = (y) => 0.25 * y;
const taxReg = (y) => 16 + 0.02 * y;
const LX = (i) => 70 + i * 0.28, LY = (r) => 330 - r * 6;
function labR() {
  if (!$("#ra")) return;
  const y = +$("#ra").value, rows = [["Progressive", taxProg, "t1", "c1"], ["Proportional", taxProp, "t3", "c3"], ["Regressive", taxReg, "t2", "c2"]];
  rows.forEach((r, i) => { $("#r" + (i + 1)).textContent = "$" + money(r[1](y), 0) + " (" + money((r[1](y) / y) * 100, 1) + "%)"; });
  $("#rv").textContent = `At an income of $${y} the progressive tax takes ${money((taxProg(y) / y) * 100, 1)}%, the proportional tax 25% and the regressive tax ${money((taxReg(y) / y) * 100, 1)}%. Slide the income up: the progressive rate climbs, the proportional rate stays put and the regressive rate falls. (The regressive example is fuel duty at $2 a litre; at this income a household buys about ${money(8 + 0.01 * y, 0)} litres.)`;
  let o = SV.line(LX(0), LY(60), LX(0), LY(0)) + SV.line(LX(0), LY(0), LX(2050), LY(0));
  [10, 20, 30, 40, 50].forEach((r) => (o += SV.line(LX(0), LY(r), LX(2000), LY(r), "gr") + SV.text(LX(0) - 8, LY(r) + 4, r + "%", "sm", { "text-anchor": "end" })));
  [500, 1000, 1500, 2000].forEach((i) => (o += SV.text(LX(i), LY(0) + 18, "$" + i, "sm", { "text-anchor": "middle" })));
  o += SV.text(LX(0) + 6, LY(60) + 4, "Tax paid as % of income", "sm") + SV.text(LX(2050), LY(0) + 38, "Income", "sm", { "text-anchor": "end" });
  rows.forEach((r) => {
    const pts = []; for (let i = 60; i <= 2000; i += 20) pts.push([LX(i), LY(Math.min(55, (r[1](i) / i) * 100))]);
    o += SV.path(ptsPath(pts), r[3]) + SV.text(LX(2000) + 6, LY((r[1](2000) / 2000) * 100) + 4, r[0], "lbl bd " + r[2]);
  });
  o += SV.line(LX(y), LY(0), LX(y), LY(55), "dash", { style: "stroke:var(--muted);stroke-width:1.5" });
  rows.forEach((r) => (o += SV.circle(LX(y), LY(Math.min(55, (r[1](y) / y) * 100)), 6, "dot" + r[3].slice(1))));
  $("#labR").innerHTML = o;
}
Lib.slider($("#g6"), { id: "ra", label: "Income", min: 60, max: 2000, step: 20, value: 500, fmt: (v) => "$" + v, onInput: labR });


function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const b = +$("#ta").value, d = +$("#tb").value, t = 20, q1 = 50 - t / (b + d), pc = 50 + (b * t) / (b + d), cs = pc - 50, ps = 50 - (pc - t);
  $("#ta1").textContent = money(cs); $("#ta2").textContent = money((cs / t) * 100, 0) + "% (" + money(cs) + ")"; $("#ta3").textContent = money((ps / t) * 100, 0) + "% (" + money(ps) + ")"; $("#ta4").textContent = money(t * q1, 0);
  $("#tav").textContent = cs > ps + 1 ? "Demand is steep relative to supply (inelastic): buyers keep buying, so firms pass on most of the tax. Consumers bear the greater share." : ps > cs + 1 ? "Demand is flat relative to supply (elastic): buyers would switch away, so firms absorb most of the tax. Producers bear the greater share." : "Demand and supply are similarly responsive, so the burden is shared about equally.";
  $("#labT").innerHTML = taxChart({ b, d, t, inc: 1 });
}
Lib.slider($("#g11"), { id: "ta", label: "Demand steepness (higher = more inelastic)", min: 0.3, max: 3, step: 0.1, value: 1, fmt: (v) => v.toFixed(1) + " " + fmtSteep(v), onInput: labT });
Lib.slider($("#g12"), { id: "tb", label: "Supply steepness (higher = more inelastic)", min: 0.3, max: 3, step: 0.1, value: 1, fmt: (v) => v.toFixed(1) + " " + fmtSteep(v), onInput: labT });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each tax <b>direct</b> (on income or wealth) or <b>indirect</b> (on spending)?", buckets: [{ label: "Direct tax" }, { label: "Indirect tax" }], items: [
  { text: "Income tax", b: 0 }, { text: "Corporation tax", b: 0 }, { text: "Capital gains tax", b: 0 }, { text: "Inheritance tax", b: 0 },
  { text: "VAT / GST (sales tax)", b: 1 }, { text: "Excise duty on petrol", b: 1 }, { text: "Customs duty (tariff)", b: 1 }, { text: "Licence to own a car", b: 1 },
], done: "Direct taxes hit income and wealth; indirect taxes hit what you buy." });
Lib.classify($("#cl2"), { prompt: "Progressive, proportional or regressive?", buckets: [{ label: "Progressive" }, { label: "Proportional" }, { label: "Regressive" }], items: [
  { text: "Tax rate rises from 10% to 20% to 40% as income rises", b: 0 }, { text: "Inheritance tax on large estates, higher rates on larger sums", b: 0 },
  { text: "Everyone pays 25% of their income", b: 1 }, { text: "A flat 15% corporation tax on all firms' profits", b: 1 },
  { text: "A $20 annual licence fee that everyone pays", b: 2 }, { text: "Excise duty per litre of petrol: richer people pay a smaller share of income", b: 2 },
  { text: "Tax takes 40% of a $100 income but 20% of a $1,000 income", b: 2 }, { text: "Egypt's income tax rate rising from 10% to 15% to 20% to 22.5%", b: 0 },
], done: "Compare the percentage taken, not the dollars." });
Lib.match($("#m1"), { prompt: "Match each principle of a good tax to what it means.", pairs: [
  ["Equity", "Tax is based on ability to pay: fair"],
  ["Certainty", "Taxpayers can understand and calculate what they owe"],
  ["Convenience", "The tax is easy to pay"],
  ["Economy", "Costs of collecting are much less than the revenue raised"],
  ["Flexibility", "Can be changed, or changes automatically, as the economy changes"],
  ["Efficiency", "Improves, or does not damage, the way markets work"],
], done: "Six qualities, six marks of vocabulary." });
Lib.classify($("#cl3"), { prompt: "Which <b>reason for taxation</b> fits each tax?", buckets: [{ label: "Raise revenue" }, { label: "Discourage demerit goods" }, { label: "Redistribute income" }, { label: "Protect environment or reduce imports" }], items: [
  { text: "Income tax paid by almost every worker", b: 0 }, { text: "VAT on most goods", b: 0 },
  { text: "Excise duty on cigarettes", b: 1 }, { text: "A high tax on alcohol", b: 1 },
  { text: "Higher rates of income tax on high earners", b: 2 }, { text: "Inheritance tax on large estates", b: 2 },
  { text: "A tax on plastic bags", b: 3 }, { text: "A tariff on imported steel", b: 3 },
], done: "Taxes often have more than one aim: say which one the question asks about." });
Lib.calc($("#c1"), { qs: [
  { q: "Income tax was NZ$32.5bn out of total revenue of NZ$78.5bn. What percentage of revenue came from income tax? (1 d.p.)", a: 41.4, tol: 0.1, sol: "32.5 ÷ 78.5 × 100 = <b>41.4%</b>." },
  { q: "A worker earns $30,000. The tax allowance is $10,000 and the income tax rate on taxable income is 20%. How much tax does she pay ($)?", a: 4000, hint: "Only income above the allowance is taxed.", sol: "Taxable income = 30,000 − 10,000 = 20,000. Tax = 20% × 20,000 = <b>$4,000</b>." },
  { q: "A tax of $4 per unit raises the price consumers pay from $10 to $13. What percentage of the tax do consumers bear?", a: 75, sol: "Consumers pay $3 of the $4: 3 ÷ 4 × 100 = <b>75%</b> (so producers bear 25%)." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is meant by a regressive tax?", opts: ["A tax that falls in line with inflation", "A tax that takes a larger percentage of income from the poor than the rich", "A tax that reduces government revenue over time", "A tax that is replaced by a bigger one"], a: 1, why: "Regressive: the percentage taken falls as income rises." },
  { q: "A government wants to redistribute income from the rich to the poor. Which tax changes would help?", opts: ["Cut corporation tax, raise sales tax", "Cut VAT, raise income tax", "Cut capital gains tax and inheritance tax", "Raise customs duties and excise duties"], a: 1, why: "Cutting an indirect (regressive) tax and raising a progressive direct tax moves the burden to the rich." },
  { q: "In which situation will consumers bear the greatest share of an indirect tax?", opts: ["Elastic demand, inelastic supply", "Inelastic demand, inelastic supply", "Inelastic demand, elastic supply", "Elastic demand, elastic supply"], a: 2, why: "When demand is inelastic buyers keep buying, and when supply is elastic firms cut output rather than absorb the tax." },
  { q: "Which is an example of a direct tax?", opts: ["VAT", "Excise duty on alcohol", "Customs duty", "Capital gains tax"], a: 3, why: "Capital gains tax is a tax on profit from selling an asset." },
  { q: "Tax revenue from income tax rises in a boom with no change in tax rates. This is an example of:", opts: ["An automatic stabiliser", "A flat tax", "A windfall tax", "A regressive tax"], a: 0, why: "Revenue rising automatically in a boom cushions swings in demand." },
  { q: "Which is an advantage of indirect taxes?", opts: ["They are always progressive", "They are relatively cheap and easy to collect", "They cannot raise prices", "They redistribute income to the poor"], a: 1, why: "Firms do much of the collecting, and they are harder to evade, but they tend to be regressive." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Direct tax", "A tax on income and wealth, such as income tax and corporation tax."],
  ["Indirect tax", "A tax on expenditure, such as VAT, excise duties and customs duties."],
  ["Progressive tax", "Takes a larger percentage of the income or wealth of the rich."],
  ["Proportional tax", "Takes the same percentage of income or wealth from all taxpayers."],
  ["Regressive tax", "Takes a larger percentage of the income or wealth of the poor."],
  ["Income tax", "A tax on income from employment and investments, above a tax allowance."],
  ["Corporation tax", "A tax on the profits of firms."],
  ["Capital gains tax", "A tax on profit made when an asset is sold for more than it cost."],
  ["Inheritance tax", "A tax on wealth above a certain amount passed on when someone dies."],
  ["Excise duty", "An indirect tax on certain goods such as alcohol, petrol and tobacco."],
  ["Customs duty", "A tax on imports, also called a tariff."],
  ["Tax allowance", "An amount of income that can be earned free of tax."],
  ["Tax base", "The source of tax revenue: what is taxed."],
  ["Tax burden", "The amount of tax paid, often shown as a percentage of GDP."],
  ["Incidence of tax", "How the burden of an indirect tax is shared between consumers and producers."],
  ["Flat tax", "A tax system with a single rate."],
  ["Windfall tax", "An extra one-off tax on very high profits."],
  ["Informal economy", "The part of the economy not regulated, protected or taxed by the government."],
] });
labR(); labT();
