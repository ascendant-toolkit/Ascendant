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

/* ---------- Lorenz curve from quintile data ---------- */
const QC = [0, 5, 15, 30, 55, 100], LX = (x) => 90 + x * 3.6, LY = (y) => 300 - y * 2.6;
function lorDraw(s) {
  let o = axes(90, 300, 450, 30, "Cumulative % of households", "Cumulative % of income"); [0, 20, 40, 60, 80, 100].forEach((v) => (o += SV.text(LX(v), 311, v, "sm", { "text-anchor": "middle" }) + SV.text(84, LY(v) + 4, v, "sm", { "text-anchor": "end" })));
  o += SV.line(LX(0), LY(0), LX(100), LY(100), "c3 dash") + tag(LX(52), LY(58) - 8, "line of perfect equality", "t3", 1, "end");
  const n = Math.max(0, Math.min(5, s.n)), pts = [[LX(0), LY(0)]]; for (let i = 1; i <= 5; i++) { if (n >= i) pts.push([LX(i * 20), LY(QC[i])]); else if (n > i - 1) { const f = n - (i - 1); pts.push([LX((i - 1) * 20 + 20 * f), LY(QC[i - 1] + (QC[i] - QC[i - 1]) * f)]); } }
  if (s.a > 0 && n >= 5) { const eqp = [], lp = []; for (let i = 0; i <= 5; i++) { eqp.push([LX(i * 20), LY(i * 20)]); lp.push([LX(i * 20), LY(QC[i])]); } o += SV.poly([...eqp, ...lp.slice().reverse()], "f1", op(0.35 * s.a)); }
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1"); for (let i = 1; i <= 5; i++) if (n >= i) o += SV.circle(LX(i * 20), LY(QC[i]), 5, "dot4") + tag(LX(i * 20) + 4, LY(QC[i]) + 20, QC[i] + "%", "sm", 1, "start");
  if (s.a > 0 && n >= 5) o += tag(LX(70), LY(35), "A", "t1", s.a, "middle") + tag(LX(80), LY(14), "B", "t2", s.a, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 520 345" role="img" aria-label="Lorenz curve through the points 5, 15, 30, 55 and 100 percent below the line of equality">${lorDraw({ n: 5, a: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 520, h: 345, label: "Building a Lorenz curve from quintile income data and finding the Gini coefficient", base: { n: 0, a: 0 }, draw: lorDraw, tween: 1300, dwell: 5600, steps: [
  { cap: "<b>The axes.</b> Households are ranked from poorest to richest along the bottom. The dashed 45° line shows perfect equality: the poorest 20% would have 20% of income, the poorest 40% would have 40%.", s: { n: 0, a: 0 } },
  { cap: "<b>The poorest 20%</b> receive only 5% of income, and the poorest 40% together receive 15%.", s: { n: 2, a: 0 } },
  { cap: "<b>The poorest 60% and 80%</b> have 30% and 55% of total income. The curve bows below the line of equality.", s: { n: 4, a: 0 } },
  { cap: "<b>The richest 20%</b> take the remaining 45%, ending the curve at (100, 100).", s: { n: 5, a: 0 } },
  { cap: "<b>The Gini coefficient.</b> Area A (between the line and the curve) divided by A + B (the whole triangle) = 0.38. A larger bow would give a higher Gini; a curve on the line would give 0.", s: { n: 5, a: 1 } },
] });

/* ---------- Policy shifts ---------- */
const lk = (x, k) => Math.pow(x / 100, k) * 100;
function polDraw(s) {
  let o = axes(90, 300, 450, 30, "Cumulative % of households", "Cumulative % of income"); [0, 50, 100].forEach((v) => (o += SV.text(LX(v), 311, v, "sm", { "text-anchor": "middle" }) + SV.text(84, LY(v) + 4, v, "sm", { "text-anchor": "end" })));
  o += SV.line(LX(0), LY(0), LX(100), LY(100), "c3 dash");
  const cv = (k, c, d) => { const p = []; for (let x = 0; x <= 100; x += 4) p.push([LX(x), LY(lk(x, k))]); return SV.path(Lib.ptsPath(p), c, d); };
  o += cv(2.4, "c1", s.k !== 2.4 ? op(0.4) : {}) + tag(LX(100) - 4, LY(lk(80, 2.4)) + 36, "Start: Gini " + Lib.fmtN((2.4 - 1) / (2.4 + 1), 2), "t1", 1, "end");
  if (s.k !== 2.4) o += cv(s.k, "c4") + tag(LX(100) - 4, LY(lk(80, s.k)) - 2, "After: Gini " + Lib.fmtN((s.k - 1) / (s.k + 1), 2), "t4", 1, "end");
  return o;
}
Lib.stepper($("#stP"), { w: 520, h: 345, label: "Lorenz curve before and after progressive taxes and transfers, and after changes that raise inequality", base: { k: 2.4 }, draw: polDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>The starting distribution.</b> The curve bows well below the line of equality: the Gini coefficient is about 0.41.", s: { k: 2.4 } },
  { cap: "<b>Progressive taxes, transfers, a minimum wage and public services</b> raise the share of income going to the poor. The curve moves towards the line of equality and the Gini falls to about 0.31.", s: { k: 1.9 } },
  { cap: "<b>The opposite.</b> If top tax rates are cut, benefits fall and skill-biased technology rewards the highly skilled, the curve moves away from the line and the Gini rises to about 0.49.", s: { k: 2.95 } },
] });

/* ---------- Lab 1 ---------- */
function labL() {
  if (!$("#kv")) return;
  const k = +$("#kv").value / 10, gini = (k - 1) / (k + 1), b40 = Math.pow(0.4, k) * 100, t20 = (1 - Math.pow(0.8, k)) * 100;
  $("#r1").textContent = gini.toFixed(2); $("#r2").textContent = Lib.fmtN(b40, 1) + "%"; $("#r3").textContent = Lib.fmtN(t20, 1) + "%";
  $("#rv").textContent = k <= 1.001 ? "The curve lies on the line of equality: everyone has the same income, Gini = 0." : `At this setting the poorest 40% of households get ${Lib.fmtN(b40, 1)}% of income and the richest 20% get ${Lib.fmtN(t20, 1)}%. The Gini coefficient is ${gini.toFixed(2)}. ${gini > 0.5 ? "This is a very unequal distribution." : gini > 0.35 ? "This is a moderately unequal distribution." : "This is a fairly equal distribution."}`;
  const X = (x) => 50 + x * 3.2, Y = (y) => 280 - y * 2.6; let o = SV.line(50, 280, 370, 280) + SV.line(50, 280, 50, 20) + SV.text(370, 304, "Cumulative % of households", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Cumulative % of income", "sm");
  const eqp = [], lp = []; for (let x = 0; x <= 100; x += 4) { eqp.push([X(x), Y(x)]); lp.push([X(x), Y(Math.pow(x / 100, k) * 100)]); }
  o += SV.poly([...eqp, ...lp.slice().reverse()], "f1", op(0.3)) + SV.line(X(0), Y(0), X(100), Y(100), "c3 dash") + SV.path(Lib.ptsPath(lp), "c1") + tag(X(66), Y(34) + 4, "A", "t1", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "kv", label: "Inequality setting (1.0 = equal) ", min: 10, max: 40, step: 1, value: 24, fmt: (v) => (v / 10).toFixed(1), onInput: labL });
labL();

/* ---------- Lab 2 ---------- */
const gOf = (sh) => { let c = 0, area = 0; sh.forEach((v) => { area += 0.2 * (c + c + v / 100) / 2; c += v / 100; }); return 1 - 2 * area; };
function labT() {
  if (!$("#tx")) return;
  const t = +$("#tx").value / 100, base = [5, 10, 15, 25, 45], tax = 45 * t, after = [5 + tax / 2, 10 + tax / 2, 15, 25, 45 - tax], g0 = gOf(base), g1 = gOf(after);
  $("#t1").textContent = after.map((v) => Lib.fmtN(v, 1)).join(", "); $("#t2").textContent = g0.toFixed(3) + " → " + g1.toFixed(3); $("#t3").textContent = (g1 - g0 >= 0 ? "+" : "") + (g1 - g0).toFixed(3);
  $("#tv").textContent = t === 0 ? "No tax: the Gini coefficient is 0.380 (the table from the Learn tab)." : `Taxing ${Lib.fmtN(t * 100, 0)}% of the richest quintile's income collects ${Lib.fmtN(tax, 1)} units, which is shared by the poorest 40%. The richest 20% fall from 45 to ${Lib.fmtN(45 - tax, 1)} units of income and the Gini falls from 0.380 to ${g1.toFixed(3)}. A real policy would also need to consider incentives to work and save.`;
  const X = (x) => 50 + x * 3.2, Y = (y) => 280 - y * 2.6; let o = SV.line(50, 280, 370, 280) + SV.line(50, 280, 50, 20) + SV.text(370, 304, "Cumulative % of households", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Cumulative % of income", "sm") + SV.line(X(0), Y(0), X(100), Y(100), "c3 dash");
  const cp = (sh) => { let c = 0; const p = [[X(0), Y(0)]]; sh.forEach((v, i) => { c += v; p.push([X((i + 1) * 20), Y(c)]); }); return p; };
  o += SV.path(Lib.ptsPath(cp(base)), "c1", op(0.5)) + SV.path(Lib.ptsPath(cp(after)), "c4") + tag(X(100) - 4, Y(30), "before", "t1", 0.7, "end") + tag(X(100) - 4, Y(45), "after", "t4", 1, "end");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "tx", label: "Tax on the richest quintile's income, % ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Towards equality or away from equality?", buckets: [{"label": "Towards equality"}, {"label": "Away from equality"}], items: [{"text": "A more progressive income tax", "b": 0}, {"text": "A cut in the top rate of income tax", "b": 1}, {"text": "A higher national minimum wage", "b": 0}, {"text": "Cutting welfare benefits", "b": 1}, {"text": "More spending on free education and health", "b": 0}, {"text": "A rise in indirect taxes on basic goods", "b": 1}, {"text": "Skill-biased technology that raises the pay of the highly skilled", "b": 1}, {"text": "Land reform that gives small farmers more land", "b": 0}], done: "Progressive taxes, transfers and public services move the curve towards the line of equality." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Lorenz curve", "Cumulative share of income plotted against cumulative share of households"], ["Gini coefficient", "Area between the line of equality and the Lorenz curve divided by the area under the line"], ["Line of perfect equality", "The 45° line where each group has an equal share"], ["Absolute poverty", "Income below a fixed level needed for basic needs"], ["Relative poverty", "Income low compared with others in the same society"], ["Progressive tax", "A tax that takes a higher percentage of higher incomes"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps to draw a Lorenz curve in order.", items: ["Rank households from poorest to richest", "Work out each group's share of income", "Calculate the cumulative shares", "Plot cumulative households against cumulative income", "Compare the curve with the 45° line"], done: "The more the curve bows away from the line, the higher the Gini." });
Lib.calc($("#c1"), { qs: [
  {"q": "In a Lorenz diagram the area between the line of equality and the curve (A) is 0.15 and the area under the curve (B) is 0.35. Calculate the Gini coefficient.", "a": 0.3, "unit": "", "tol": 0.005, "hint": "A ÷ (A + B).", "sol": "0.15 ÷ 0.50 = <b>0.30</b>."},
  {"q": "The poorest 20%, 40%, 60% and 80% have 8%, 20%, 38% and 62% of income. What share of income does the richest 20% have (%)?", "a": 38, "unit": "%", "tol": 0.5, "hint": "100 − 62.", "sol": "<b>38%</b>."},
  {"q": "The area under a Lorenz curve is 0.28. Calculate the Gini coefficient.", "a": 0.44, "unit": "", "tol": 0.005, "hint": "1 − 2 × 0.28.", "sol": "<b>0.44</b>."},
  {"q": "Median income is $20,000. Relative poverty is defined as below 60% of the median. What is the poverty line ($)?", "a": 12000, "unit": "$", "tol": 0.5, "hint": "0.6 × 20,000.", "sol": "<b>$12,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A Gini coefficient of zero means:", opts: ["Perfect equality", "Perfect inequality", "No poverty", "No inflation"], a: 0, why: "Everyone has the same income." },
  { q: "A Lorenz curve that moves closer to the 45° line shows:", opts: ["More equality", "More inequality", "No change", "Higher growth"], a: 0, why: "A smaller area A and a lower Gini." },
  { q: "Which policy is most likely to lower the Gini coefficient?", opts: ["A more progressive income tax", "Cutting the top tax rate", "Cutting benefits", "A flat tax"], a: 0, why: "Progressive taxes take more from higher incomes." },
  { q: "Relative poverty is best described as:", opts: ["Income low compared with others in the society", "Income below $2 a day", "Having no income", "A high inflation rate"], a: 0, why: "It is measured against typical incomes." },
  { q: "Economic growth could reduce absolute poverty while:", opts: ["Raising inequality", "Always lowering inequality", "Removing all poverty", "Increasing the Lorenz curve area to zero"], a: 0, why: "The rich may gain faster than the poor." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Lorenz curve", "Cumulative income vs cumulative households."],
  ["Gini coefficient", "A ÷ (A + B); 0 to 1."],
  ["Line of equality", "The 45° line."],
  ["Absolute poverty", "Below a fixed income line."],
  ["Relative poverty", "Low compared with society's typical income."],
  ["Progressive tax", "Higher percentage on higher incomes."],
  ["Equity vs efficiency", "Redistribution may reduce incentives."],
  ["Gini from B", "Gini = 1 − 2B."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The diagram shows a Lorenz curve with area X between the line of equality and the curve and area Y under the curve. How is the Gini coefficient calculated? (Oct/Nov 2023 · 31 · Q30 and Oct/Nov 2020 · 33 · Q14, reworded)", opts: ["X divided by (X plus Y)", "(X plus Y) divided by X", "(X plus Y) divided by Y", "Y divided by (X plus Y)"], a: 0, why: "The Gini coefficient is the area between the line of equality and the curve as a share of the whole triangle under the line of equality." },
  { q: "On a Lorenz curve diagram the area X between the line of equality and the curve is one third of the area Y below the curve. What is the Gini coefficient? (Oct/Nov 2021 · 31 · Q15, reworded)", opts: ["1/3", "1/4", "3/4", "3"], a: 1, why: "The whole triangle is X + Y = 4 parts, of which X is 1 part, so the Gini coefficient is 1/4." },
  { q: "The Gini coefficient is 24.7 for Denmark, 32.7 for France, 50.4 for Zambia and 74.3 for Namibia. Which statement is correct? (May/June 2024 · 31 · Q30, reworded)", opts: ["Income is distributed more equally in Denmark than in France", "Income is distributed more equally in Namibia than in Zambia", "Income per capita is higher in Zambia than in Namibia", "A larger share of people are below the poverty line in Zambia than in France"], a: 0, why: "A lower Gini means more equal. The table gives no information about income per head or poverty." },
  { q: "When assessing income distribution, which change in the Gini coefficient suggests more equal distribution? (Oct/Nov 2023 · 32 · Q27, reworded)", opts: ["It has moved closer to one", "It has moved closer to zero", "It has moved from negative to positive", "It has moved from positive to negative"], a: 1, why: "Zero is perfect equality. The Gini coefficient cannot be negative." },
  { q: "A country's Gini coefficient is 0.40. The poorest earners pay no income tax. The government raises the tax rate on the highest earners and income becomes more equal. What can be concluded? (May/June 2021 · 31 · Q15, reworded)", opts: ["The Gini coefficient falls and the tax system is more progressive", "The Gini coefficient falls and the tax system is more regressive", "The Gini coefficient rises and the tax system is more progressive", "The Gini coefficient rises and the tax system is more regressive"], a: 0, why: "Taxing high earners more makes the system more progressive and reduces inequality." },
  { q: "The Lorenz curves show Norway (N) and India (I), with Norway closer to the line of equality. What can be concluded? (May/June 2023 · 31 · Q16, reworded)", opts: ["India is more likely to have lower indirect taxes and public education than Norway", "India is more likely to have a progressive income tax and means-tested benefits than Norway", "Norway is more likely to have a progressive tax system and public sector pensions than India", "Norway is likely to rely more on indirect taxes and private pensions than India"], a: 2, why: "A more equal distribution is consistent with progressive taxes and public provision." },
  { q: "Which combination of fiscal measures would be most effective in reducing income inequality? Top rates of income tax, indirect taxes, value of state benefits. (Oct/Nov 2023 · 32 · Q13, reworded)", opts: ["Increase, increase, increase", "Increase, reduce, increase", "Reduce, increase, reduce", "Reduce, reduce, reduce"], a: 1, why: "Higher top income tax, lower indirect taxes (which are regressive) and higher benefits all reduce inequality." },
  { q: "What is most likely to increase relative poverty in a country? (Oct/Nov 2023 · 33 · Q13, reworded)", opts: ["Increasing means-tested benefits", "Increasing the power of trade unions", "Making the tax system more progressive", "Removing the national minimum wage"], a: 3, why: "Without a minimum wage, the lowest pay may fall relative to median incomes." },
  { q: "Which policy could reduce income inequality in the short run in a country with high inequality? (Oct/Nov 2024 · 32 · Q15, reworded)", opts: ["Raise VAT on luxury goods", "Introduce a minimum wage", "Invest heavily in schools", "Stimulate growth through skills training"], a: 1, why: "A minimum wage raises low pay quickly. Education and training take years to affect incomes." },
] });
