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

/* ---------- Laffer curve ---------- */
const LX = (t) => 70 + t * 6.2, LY = (r) => 300 - r * 2.5, LR = (t, k = 1) => t * (100 - k * t) / 25;
function lafDraw(s) {
  const k = 1, pk = 50;
  let o = axes(70, 300, 700, 30, "Tax rate (%)", "Tax revenue"); [0, 25, 50, 75, 100].forEach((t) => (o += SV.text(LX(t), 316, t, "sm", { "text-anchor": "middle" })));
  const pts = []; for (let t = 0; t <= s.n + 1e-9; t += 2) pts.push([LX(t), LY(LR(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  if (s.p > 0) o += SV.circle(LX(pk), LY(LR(pk)), 8, "dot3", op(s.p)) + SV.line(LX(pk), LY(LR(pk)), LX(pk), 300, "gr", op(s.p)) + tag(LX(pk), LY(LR(pk)) - 14, "revenue-maximising rate", "t3", s.p, "middle");
  if (s.c > 0) o += SV.circle(LX(75), LY(LR(75)), 8, "dot2", op(s.c)) + tag(LX(75) + 12, LY(LR(75)) - 10, "A: high rate", "t2", s.c) + SV.circle(LX(55), LY(LR(55)), 8, "dot4", op(s.c)) + tag(LX(55) + 12, LY(LR(55)) - 12, "B: after a cut", "t4", s.c) + arrow(LX(73), LY(LR(75)) - 4, LX(57), LY(LR(55)) - 8, "l", "c4", s.c);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Laffer curve with tax revenue against tax rate peaking at an optimum rate">${lafDraw({ n: 100, p: 1, c: 0 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 340, label: "Laffer curve showing revenue rising, peaking and falling as the tax rate rises", base: { n: 0, p: 0, c: 0 }, draw: lafDraw, tween: 1200, dwell: 5600, steps: [
  { cap: "<b>A zero tax rate</b> raises no revenue. As the rate rises from zero, revenue rises, because there is still a strong incentive to work and declare income.", s: { n: 30 } },
  { cap: "<b>The peak.</b> At some rate revenue is at its maximum. Beyond this point further increases cause people to work less, avoid or evade tax, or move abroad, so the gains from the higher rate are offset.", s: { n: 52, p: 1 } },
  { cap: "<b>Too high.</b> At very high rates revenue falls, and at 100% it would be close to zero because nobody would have a reason to declare income.", s: { n: 100, p: 1 } },
  { cap: "<b>Supply-side logic.</b> If the rate is already above the peak (A), <b>cutting</b> it to B raises effort and enterprise and could <b>raise revenue</b> and output. Below the peak a cut would lose revenue, so the position of the peak matters.", s: { n: 100, p: 1, c: 1 } },
] });

/* ---------- J curve ---------- */
const JX = (t) => 70 + t * 62, JY = (v) => 170 - v * 28;
const jc = (t) => -2 + 4 * (1 - Math.exp(-0.45 * t)) - 6 * Math.exp(-0.7 * t) * (1 - Math.exp(-3 * t));
function jDraw(s) {
  let o = SV.line(70, 170, 700, 170) + SV.line(70, 40, 70, 300) + SV.text(700, 190, "Time after depreciation (quarters)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Current account balance", "sm");
  o += SV.line(70, JY(-2), 700, JY(-2), "c3 dash") + tag(696, JY(-2) + 16, "balance before the depreciation", "t3", 1, "end");
  const pts = []; for (let t = 0; t <= s.n + 1e-9; t += 0.1) pts.push([JX(t), JY(jc(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2") + SV.circle(pts[pts.length - 1][0], pts[pts.length - 1][1], 6, "dot4");
  if (s.a > 0) o += tag(JX(1.3), JY(-5.2), "dearer imports, volumes slow to change", "t2", s.a, "start");
  if (s.b > 0) o += tag(JX(6.2), JY(-0.2), "volumes adjust: balance improves", "t1", s.b, "middle");
  return o;
}
Lib.stepper($("#stJ"), { w: 760, h: 330, label: "J curve: the current account worsens after a depreciation before it improves", base: { n: 0, a: 0, b: 0 }, draw: jDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>The starting point.</b> The country has a current account deficit and its government depreciates or devalues the currency to correct it.", s: { n: 0.05 } },
  { cap: "<b>Short run: it gets worse.</b> Import prices rise at once in domestic currency, while volumes of imports and exports are held by contracts and habit. The import bill rises faster than export revenue, so the deficit <b>widens</b>.", s: { n: 1.2, a: 1 } },
  { cap: "<b>Medium run: volumes adjust.</b> Buyers switch to cheaper home goods and foreigners buy more exports. The deficit narrows and passes its starting level, <b>if</b> the Marshall-Lerner condition holds.", s: { n: 4, a: 1, b: 0 } },
  { cap: "<b>Long run: improvement.</b> The current account settles at a better balance than before. The full pattern is a <b>J shape</b>. Evaluation: imported inflation and retaliation may reduce the gain.", s: { n: 9.9, a: 1, b: 1 } },
] });

/* ---------- Lab 1: Laffer ---------- */
function labLaf() {
  if (!$("#lt") || !$("#lk")) return;
  const t = +$("#lt").value, k = +$("#lk").value / 10, R = (x) => x * (100 - k * x) / 25, pk = 50 / k;
  $("#r1").textContent = Lib.fmtN(R(t), 0); $("#r2").textContent = Lib.fmtN(pk, 0) + "%"; const above = t > pk + 0.5;
  $("#r3").textContent = t > pk + 0.5 ? "raise revenue" : t < pk - 0.5 ? "cut revenue" : "leave revenue the same";
  $("#rv").textContent = above ? `The tax rate of ${t}% is above the revenue-maximising rate of ${Lib.fmtN(pk, 0)}%, so cutting the rate would raise revenue as well as work effort. This is the case for supply-side tax cuts.` : t < pk - 0.5 ? `The rate of ${t}% is below the peak of ${Lib.fmtN(pk, 0)}%, so a tax cut would reduce revenue. Raising the rate towards the peak would raise revenue, though it could harm incentives.` : "The rate is at the revenue-maximising point: changes in either direction reduce revenue.";
  const X = (x) => 40 + x * 3.5, Y = (v) => 270 - v / 110 * 230; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Tax rate (%)", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Revenue", "sm");
  const pts = []; for (let x = 0; x <= 100.01; x += 2) pts.push([X(x), Y(Math.max(0, R(x)))]); o += SV.path(Lib.ptsPath(pts), "c1");
  o += SV.circle(X(pk), Y(R(pk)), 7, "dot3") + tag(X(pk), Y(R(pk)) - 12, "peak", "t3", 1, "middle") + SV.circle(X(t), Y(Math.max(0, R(t))), 8, above ? "dot2" : "dot4") + SV.line(X(t), Y(Math.max(0, R(t))), X(t), 270, "gr");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "lt", label: "Tax rate (%) ", min: 0, max: 100, step: 5, value: 70, fmt: (v) => v, onInput: labLaf });
Lib.slider($("#g2"), { id: "lk", label: "Taxpayer responsiveness (higher = lower peak) ", min: 7, max: 15, step: 1, value: 10, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labLaf });
labLaf();
btnTable("lbBtns", "lbOut", [
  ["Expansionary fiscal policy", "Inflation: up near capacity", "Unemployment: down (cyclical)", "Growth: up short run", "Current account: worse (imports)", "Debt and crowding out; time lags"],
  ["Higher interest rates", "Inflation: down", "Unemployment: up", "Growth: down", "Current account: worse if the currency appreciates", "Lags 12 to 24 months; hurts borrowers"],
  ["Market-based supply-side policy", "Inflation: down long run", "Unemployment: natural rate down", "Growth: up long run", "Current account: better (competitiveness)", "Slow; may widen inequality"],
  ["Interventionist supply-side policy", "Inflation: down long run", "Unemployment: structural down", "Growth: up long run", "Current account: better", "Costly; may be badly targeted"],
  ["Devaluation / depreciation", "Inflation: up (imported)", "Unemployment: down (net exports)", "Growth: up if exports respond", "Current account: J curve, then better", "Marshall-Lerner; retaliation"],
  ["Tariffs and quotas", "Inflation: up (dearer imports)", "Unemployment: down in protected industries", "Growth: uncertain, efficiency falls", "Current account: better if no retaliation", "Retaliation; higher prices"]
], ["Policy", "Inflation", "Unemployment", "Growth", "Current account", "Main limit"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which type of policy is it?", buckets: [{"label": "Fiscal"}, {"label": "Monetary"}, {"label": "Supply-side (market-based)"}, {"label": "Supply-side (interventionist)"}, {"label": "Exchange rate / trade"}], items: [{"text": "Cut the top rate of income tax", "b": 0}, {"text": "Raise the central bank's interest rate", "b": 1}, {"text": "Privatise a state industry", "b": 2}, {"text": "Fund apprenticeships and training", "b": 3}, {"text": "Devalue the currency", "b": 4}, {"text": "Impose a tariff on imported steel", "b": 4}, {"text": "Raise government spending on roads", "b": 0}, {"text": "Quantitative easing", "b": 1}, {"text": "Weaken union power", "b": 2}, {"text": "Subsidise R&D", "b": 3}], done: "Match each measure to its policy family." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Laffer curve", "Relationship between tax rates and tax revenue"], ["Expenditure-switching", "A policy that shifts spending from imports to domestic goods"], ["Expenditure-reducing", "A policy that cuts total spending and so imports"], ["Marshall-Lerner condition", "Depreciation improves the current account if PEDx + PEDm is greater than 1"], ["J curve", "The current account worsens before it improves after a depreciation"], ["Transmission mechanism", "The way interest rate changes reach spending and inflation"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a depreciation on the current account in order.", items: ["The currency's value falls", "Exports become cheaper abroad and imports dearer at home", "Export volumes rise and import volumes fall over time", "Net exports and AD rise", "The current account improves, if elasticities are high enough"], done: "A depreciation works through relative prices." });
Lib.calc($("#c1"), { qs: [
  {"q": "A tariff of 15% is placed on imports of $200m. Calculate the tariff revenue ($m), assuming imports do not change.", "a": 30, "unit": "$m", "tol": 0.05, "hint": "15% of 200.", "sol": "0.15 × 200 = <b>$30m</b>."},
  {"q": "The price elasticity of demand for exports is 0.8 and for imports is 0.4. Does the Marshall-Lerner condition hold? Type 1 for yes and 0 for no.", "a": 1, "tol": 0.01, "hint": "Add the two elasticities and compare with 1.", "sol": "0.8 + 0.4 = 1.2, which is greater than 1, so the condition holds: <b>yes (1)</b>."},
  {"q": "A country's exports are priced at $100 each. Its currency depreciates by 10% against the dollar, and the foreign price of exports falls by the same amount. What is the new foreign price ($)?", "a": 90, "unit": "$", "tol": 0.05, "hint": "100 × 0.9.", "sol": "<b>$90</b>."},
  {"q": "Taxpayers earn $10,000m of taxable income and the average tax rate is 40%. The government raises the rate to 50% and taxable income falls to $7,600m. Calculate the change in tax revenue ($m).", "a": -200, "unit": "$m", "tol": 0.5, "hint": "Revenue before = 4,000. After = 50% × 7,600.", "sol": "Before: 4,000. After: 3,800. Change = <b>−$200m</b>, a Laffer-type effect."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is expenditure-switching?", opts: ["A rise in income tax", "A rise in the interest rate", "A devaluation of the currency", "A cut in government spending"], a: 2, why: "A devaluation changes relative prices and switches spending to domestic goods." },
  { q: "The J curve describes:", opts: ["Inflation rising then falling", "The current account worsening then improving after a depreciation", "Tax revenue rising then falling", "Unemployment falling then rising"], a: 1, why: "In the short run inelastic demand makes the deficit widen." },
  { q: "According to Laffer analysis, a cut in the tax rate raises revenue when:", opts: ["The rate is below the revenue-maximising rate", "The rate is above the revenue-maximising rate", "Taxpayers do not respond to the rate", "Revenue is already zero"], a: 1, why: "Above the peak, a lower rate reduces avoidance and raises effort enough to raise revenue." },
  { q: "Which policy is best suited to long-run non-inflationary growth?", opts: ["Higher interest rates", "Supply-side policy", "A depreciation", "Tariffs"], a: 1, why: "Supply-side policy raises capacity so that output can grow without inflation." },
  { q: "A major cost of imposing tariffs is that:", opts: ["Trading partners may retaliate and consumers pay higher prices", "Imports rise", "Domestic competition increases", "The exchange rate always falls"], a: 0, why: "Retaliation and higher prices are the main costs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Fiscal policy", "Changes in government spending and taxes."],
  ["Monetary policy", "Interest rates, money supply, QE."],
  ["Supply-side policy", "Raises capacity: market-based or interventionist."],
  ["Laffer curve", "Tax revenue against tax rate; peaks at an optimum rate."],
  ["Expenditure-switching", "Moves spending from imports to home goods."],
  ["Marshall-Lerner", "PEDx + PEDm > 1 for a depreciation to help the current account."],
  ["J curve", "Current account worsens then improves."],
  ["Tariff", "Tax on imports."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What does the Laffer curve show? (Feb/March 2022 · 32 · Q29, reworded)", opts: ["The relationship between inflation and unemployment", "The relationship between the interest rate and the demand for money", "The relationship between tax rates and tax revenue", "The relationship between how two goods can be produced with given resources"], a: 2, why: "The Laffer curve plots tax revenue against the tax rate." },
  { q: "What is illustrated by the Laffer curve? (Oct/Nov 2022 · 33 · Q28, reworded)", opts: ["As income rises, fewer hours will be worked", "As income rises, tax revenue will rise", "As the tax rate rises, tax revenue always rises", "As the tax rate rises, tax revenue will eventually fall"], a: 3, why: "Beyond some rate, higher rates reduce effort and increase avoidance, so revenue falls." },
  { q: "Which policy to encourage growth might be based on the Laffer curve? (Oct/Nov 2023 · 32 · Q23, reworded)", opts: ["Cuts in direct taxes", "Exchange rate depreciation", "Investment subsidies", "Quantitative easing"], a: 0, why: "Laffer analysis suggests that lowering high tax rates could raise effort, growth and revenue." },
  { q: "The chief economist says that raising the top rate of income tax from 40% to 45% is likely to cut tax revenue by 2%. Which concept explains this? (May/June 2022 · 32 · Q29, reworded)", opts: ["The Kuznets curve", "The Laffer curve", "The Lorenz curve", "The Phillips curve"], a: 1, why: "The Laffer curve explains why higher rates can reduce revenue." },
  { q: "Which macroeconomic policy is most likely to be used as a long-run means of reducing inflationary pressures? (Feb/March 2020 · 32 · Q29, reworded)", opts: ["Exchange rate policy", "Fiscal policy", "Monetary policy", "Supply-side policy"], a: 3, why: "Supply-side policy raises capacity and productivity, which lowers cost pressure in the long run." },
  { q: "What is an example of an expenditure-switching policy? (Feb/March 2023 · 32 · Q29, reworded)", opts: ["A rise in income tax rates", "A rise in interest rates", "A rise in tariff rates", "A rise in the money supply"], a: 2, why: "Tariffs switch spending from imports to home-produced goods. Higher taxes and interest rates are expenditure-reducing." },
  { q: "In 2018 the US imposed a tariff on steel imports. What is the likely impact on the US economy? (May/June 2020 · 31 · Q30, reworded)", opts: ["US steel exports become more price competitive", "Productive inefficiency in the US steel industry", "A deterioration in the US terms of trade", "A fall in producer surplus for US steel producers"], a: 1, why: "Protection reduces competitive pressure, so domestic producers become less efficient." },
  { q: "Which policy may increase economic growth without causing inflation? (Feb/March 2025 · 32 · Q21, reworded)", opts: ["Subsidies to producers", "Higher government spending", "Lower direct taxes", "Lower interest rates"], a: 0, why: "Subsidies to producers lower costs and shift supply to the right, so they raise output without adding to demand." },
] });
