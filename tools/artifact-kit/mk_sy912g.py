"""Syllabus 9.1.2 government spending and net exports as components of AD (chapter 41.2). Run: python3 tools/artifact-kit/mk_sy912g.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.1.2"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Government spending (G)</b> is not driven by income the way consumption is. It is set by <b>policy choices</b>, the <b>stage of the business cycle</b>, the <b>size of the state</b>, the population and unexpected events such as disasters or conflict. <b class="kw">Net exports (X − M)</b> are exports minus imports, and depend on <b>price and quality competitiveness</b> (productivity, relative inflation and the exchange rate) and on <b>incomes at home and abroad</b>. Both are <b>injections or withdrawals</b> that shift aggregate demand, so any change in them is magnified by the <b>multiplier</b>. For the exam you need the determinants of each, and a view on how far each can be controlled.</p></div>

  <h2>1 · Government spending</h2>
  <div id="pic1" class="card"></div>
  <div class="grid2">
    <div class="card"><h3>What decides how much a government spends</h3><ul>
      <li><b>The business cycle:</b> a government may raise spending in a downturn to lift AD and employment (and automatic stabilisers such as benefits rise on their own).</li>
      <li><b>The view of the state:</b> spending is a higher share of GDP where the government sees a greater risk of market failure and provides education, healthcare and pensions.</li>
      <li><b>Technology:</b> new equipment for schools and hospitals, and more complex treatments, push up the cost of public services.</li>
      <li><b>Population:</b> an ageing population raises health and pension spending. A young or growing one raises school and housing spending. Net immigration may raise spending and also raise tax revenue if the migrants find jobs.</li>
      <li><b>Unexpected events:</b> natural disasters, pandemics and military conflict.</li>
      <li><b>The budget position:</b> how much the government can raise in tax or borrow, and the cost of servicing existing debt.</li>
    </ul></div>
    <div class="card"><h3>Why it matters for AD</h3><ul>
      <li>G is a <b>direct injection</b>: every dollar spent adds to AD at once, unlike a tax cut, where part of the extra income may be saved.</li>
      <li>It is <b>mostly autonomous</b>: it does not move automatically with income (apart from benefits), so a change in G shifts the AE line.</li>
      <li>The final effect is G × <b>multiplier</b>, which is smaller if the money goes on imports or if the extra income is heavily taxed.</li>
      <li>It could <b>crowd out</b> private spending if it is financed by borrowing that raises interest rates.</li>
    </ul></div>
  </div>
  <div class="tip"><b class="h">Types of spending</b>Current spending (wages, goods and services, benefits) is used up in the year. Capital spending (roads, schools, hospitals) adds to the economy's productive capacity, so it can raise <b>AS as well as AD</b> in the long run. Transfer payments (pensions, benefits) are not included in G in the national accounts, because nothing is produced in exchange, but they do raise households' disposable income and consumption.</div>

  <h2>2 · Net exports</h2>
  <div id="pic2" class="card"></div>
  <p><b>Net exports = exports (X) − imports (M).</b> When X is greater than M there is a trade surplus and net exports add to AD. When M is greater than X, net exports are negative and subtract from it.</p>
  <div class="grid2">
    <div class="card"><h3>Price competitiveness</h3><ul>
      <li><b>Relative productivity:</b> if a country's output per worker rises faster than its rivals', unit costs fall and exports become cheaper.</li>
      <li><b>Relative inflation:</b> a lower inflation rate than trading partners makes exports cheaper in foreign markets and imports dearer at home.</li>
      <li><b>The exchange rate:</b> a fall in value makes exports cheaper abroad and imports dearer at home, which could raise net exports. Whether it does depends on the price elasticities (the Marshall-Lerner condition) and the lag (the J curve).</li>
    </ul></div>
    <div class="card"><h3>Quality competitiveness and incomes</h3><ul>
      <li><b>Quality and design:</b> rises with net investment, education and training, and innovation. These matter more for goods with few close substitutes.</li>
      <li><b>Foreign incomes:</b> higher GDP abroad raises demand for exports, especially goods with a high income elasticity of demand.</li>
      <li><b>Domestic income:</b> higher home income raises spending on imports (the marginal propensity to import), so a fast-growing economy may see net exports fall.</li>
      <li><b>Trade policy:</b> tariffs, quotas, subsidies and trade agreements.</li>
    </ul></div>
  </div>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Effect on net exports</th><th>Why</th></tr>
    <tr><td>Productivity rises faster than abroad</td><td>Up</td><td>Lower unit costs, cheaper exports</td></tr>
    <tr><td>Home inflation above trading partners'</td><td>Down</td><td>Exports dearer, imports relatively cheaper</td></tr>
    <tr><td>Exchange rate falls</td><td>Up (if elasticities are high enough)</td><td>Exports cheaper abroad, imports dearer</td></tr>
    <tr><td>Foreign GDP rises</td><td>Up</td><td>Foreign buyers have more to spend</td></tr>
    <tr><td>Home GDP rises</td><td>Down</td><td>Households and firms buy more imports</td></tr>
    <tr><td>Quality improves</td><td>Up</td><td>Demand is less sensitive to price</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exports and imports are different kinds of flow</b>Exports are an <b>injection</b> and imports are a <b>withdrawal</b>. In the multiplier, imports matter through the <b>marginal propensity to import (mpm)</b>. The <b>average propensity to import</b> is imports ÷ income (for example 630 ÷ 3,200 ≈ 0.2 for an economy that imports $630bn of a $3,200bn income), and the <b>marginal propensity to import</b> is the change in imports ÷ the change in income.</div>
'''

watch = '''
  <h2>1 · What shifts net exports</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stN"></div>
  <h2>2 · A rise in government spending and the multiplier</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · Net exports</h2>
  <p>Choose the change in the exchange rate and in foreign income. The lab shows the change in exports and imports and what happens to net exports.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Exports</small><strong id="r1"></strong></div><div><small>Imports</small><strong id="r2"></strong></div><div><small>Net exports</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 290" role="img" aria-label="Bars showing exports, imports and net exports before and after a change"></svg></div></div></div>

  <h2>Lab 2 · Does it raise or lower net exports?</h2>
  <p>Choose a change and see the effect on exports, imports and net exports.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Raises or lowers net exports?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a depreciation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Spending after a natural disaster", "A government that rebuilds roads, homes and power lines after a hurricane or earthquake spends more than planned. That raises AD and, if there is spare capacity, output and jobs may rise, though the spending may also be financed by higher borrowing.", "unexpected events as a determinant of G. Link to the multiplier and to the budget deficit.") +
rw("An ageing population", "In countries with a falling death rate and a shrinking working-age share, spending on pensions and healthcare tends to rise while tax revenue growth slows.", "population as a determinant. Say that spending may rise faster than GDP and that this puts pressure on the budget.") +
rw("A weaker currency and exports", "When a currency loses value, exporters can cut prices abroad or earn more per sale in their own currency. Imports become dearer, so households may buy fewer of them. In practice the effect on net exports may take months to appear.", "the exchange rate and the Marshall-Lerner condition. Mention the J curve.") +
rw("A trading partner enters a boom", "If an economy's main customers grow faster, their households and firms buy more of its goods, especially luxuries and capital goods with a high income elasticity of demand.", "foreign income as a determinant. Say that the effect may be smaller for necessities.")
)

mc_exam = [
  ("Which change is most likely to increase a country's net exports? (Practice, not a past paper question)", ["A rise in its inflation rate relative to its trading partners", "A rise in incomes in its main trading partners", "A rise in the value of its exchange rate", "A fall in its labour productivity"], 1, "Higher foreign incomes raise demand for exports. The other options make exports dearer or less competitive."),
  ("Which is most likely to lead to higher government spending as a share of GDP? (Practice, not a past paper question)", ["A fall in the death rate leading to an older population", "A rise in net emigration of young workers", "A decision to privatise health services", "A fall in the unemployment rate"], 0, "An older population raises health and pension spending."),
  ("An economy's marginal propensity to import is 0.3. Income rises by $200bn. By how much do imports rise? (Practice, not a past paper question)", ["$30bn", "$60bn", "$140bn", "$200bn"], 1, "Change in imports = mpm × change in income = 0.3 × 200 = $60bn.")
]

exam = exam_page("government spending and net exports",
  "These components of AD are usually tested within wider questions on aggregate demand, fiscal policy and the balance of payments, and in Paper 3 multiple choice on the multiplier and the exchange rate. The questions below are our own, in the style of the exam.",
  [("Short written parts", "2", "Practice questions"), ("Multiple choice (Paper 3)", "3", "Practice questions")],
  [
  eq("Practice (not a past paper question)", "8 marks", "Explain two factors that could cause a rise in a country's net exports.",
     ["Identify two factors (for example a lower relative inflation rate, a fall in the exchange rate, higher productivity, higher foreign incomes).",
      "Explain how each changes exports or imports and so (X − M).",
      "Credit a brief evaluation, for example the Marshall-Lerner condition or the time lag."],
     "Two factors, each with a chain of cause and effect. One sentence of evaluation.",
     [[("k", "Net exports are the value of exports minus the value of imports, so a rise in net exports means exports rise by more than imports, or imports fall by more than exports."), ("a", "One factor is a fall in the exchange rate. A lower value of the currency makes exports cheaper for foreign buyers and imports dearer for domestic buyers, so the volume of exports could rise and the volume of imports could fall.")],
      [("a", "A second factor is higher income in the country's main trading partners. Their households and firms have more to spend, so demand for the country's exports rises, especially for products with a high income elasticity of demand."), ("e", "However, a fall in the exchange rate only raises net exports if the sum of the price elasticities of demand for exports and imports is greater than one, and the effect may take time to appear.")]]),
  eq("Practice (not a past paper question)", "12 marks", "Discuss the factors that determine the level of government spending in a country.",
     ["Explain at least three determinants: the stage of the business cycle, the role of the government (market failure, provision of education and healthcare), technology, population, unexpected events and the budget constraint.",
      "Link to AD and the multiplier.",
      "Evaluation: which factors the government can control and which it cannot, and a judgement on the most important one."],
     "Three factors with direction of effect. Then which are controllable and which are not, and a judgement.")
  ], mcq_h="Multiple choice questions")

tips = tips_html(
  [("Give G its determinants in groups.", "Policy and the cycle, the size of the state, population and technology, and unexpected events."),
   ("State the direction of each factor.", "Say whether the change raises or lowers net exports, and why."),
   ("Split net exports into exports and imports.", "A change in the exchange rate could change both, so say which effect is larger."),
   ("Use the right propensity.", "The marginal propensity to import is the change in imports divided by the change in income. It reduces the multiplier."),
   ("Mention the elasticity condition.", "A depreciation may not raise net exports if demand is inelastic, at least in the short run."),
   ("Be careful with transfer payments.", "They are not part of G in the national accounts, though they affect consumption."),
   ("Say what you cannot control.", "Governments do not decide the foreign income or the exchange rate on their own, so the effect of policy on net exports is uncertain.")],
  [("Government spending", "Government spending is determined by the stage of the business cycle, the role of the state, population changes and unexpected events."),
   ("Net exports", "Net exports depend on relative price and quality competitiveness and on incomes at home and abroad."),
   ("Exchange rate", "A fall in the exchange rate could raise net exports if the combined price elasticity of demand for exports and imports is greater than one."),
   ("Multiplier", "The final change in income is the change in G or net exports multiplied by the multiplier."),
   ("Evaluate", "However, the effect may be smaller if imports rise or if households save the extra income.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn pictures ---------- */
function bars(items, base, k, w) {
  let o = SV.line(40, base, 720, base);
  items.forEach((it, i) => { const x = 70 + i * (w + 25), v = it.v, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), it.c) + tag(x + w / 2, v >= 0 ? y - 8 : y + h + 16, it.t, it.cls, 1, "middle") + SV.text(x + w / 2, base + (v >= 0 ? 20 : -6), it.l, "sm", { "text-anchor": "middle" }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 250" role="img" aria-label="Components of aggregate demand: consumption, investment, government spending and net exports">${bars([
  { v: 60, c: "f1", t: "C", l: "Consumption", cls: "t1" }, { v: 18, c: "f4", t: "I", l: "Investment", cls: "t4" }, { v: 20, c: "f3", t: "G", l: "Government spending", cls: "t3" }, { v: 6, c: "f2", t: "X", l: "Exports", cls: "t2" }, { v: -7, c: "f2", t: "M", l: "Imports", cls: "t2" }], 190, 2.6, 100)}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 270" role="img" aria-label="Net exports as exports minus imports">${SV.line(60, 220, 700, 220) + SV.rect(120, 90, 130, 130, "f3") + SV.rect(330, 120, 130, 100, "f2") + SV.rect(540, 190, 130, 30, "f1") + tag(185, 80, "Exports X", "t3", 1, "middle") + tag(395, 110, "Imports M", "t2", 1, "middle") + tag(605, 180, "Net exports X − M", "t1", 1, "middle") + tag(185, 245, "130", "t3", 1, "middle") + tag(395, 245, "100", "t2", 1, "middle") + tag(605, 245, "+30 (a surplus)", "t1", 1, "middle")}</svg>`;

/* ---------- Watch 1: net exports ---------- */
function neDraw(s) {
  const base = 250, k = 1.3, xs = [110, 270, 430, 590], X = 100 + s.x, M = 90 + s.m, N = X - M;
  const vals = [["Exports X", X, "f3", "t3"], ["Imports M", M, "f2", "t2"], ["Net exports", N, N >= 0 ? "f1" : "f2", N >= 0 ? "t1" : "t2"]];
  let o = SV.line(60, base, 600, base);
  vals.forEach(([l, v, c, t], i) => { const h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(xs[i] - 40, y, 80, Math.max(h, 2), c) + tag(xs[i], v >= 0 ? y - 8 : y + h + 16, Lib.fmtN(v, 0), t, 1, "middle") + SV.text(xs[i], base + 22, l, "sm", { "text-anchor": "middle" }); });
  if (s.n) o += tag(640, 60, s.n, "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 300, label: "Exports, imports and net exports before and after a fall in the exchange rate and a rise in foreign income", base: { x: 0, m: 0 }, draw: neDraw, tween: 1000, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Exports are 100, imports are 90, so net exports are +10, a small surplus.", s: { x: 0, m: 0 } },
  { cap: "<b>The exchange rate falls.</b> Exports are cheaper abroad, so foreign buyers purchase more: exports rise to 112. Imports are dearer, so households buy slightly fewer: imports fall to 86.", s: { x: 12, m: -4 } },
  { cap: "<b>Foreign income rises.</b> Customers abroad have more to spend, so exports rise further, to 120.", s: { x: 20, m: -4 } },
  { cap: "<b>Home income rises.</b> The economy grows, and part of the extra income is spent on imports (the marginal propensity to import), so imports rise to 98.", s: { x: 20, m: 8 } },
  { cap: "<b>Net exports are +22.</b> The fall in the exchange rate and the rise in foreign income raised X. Growth at home pulled in imports, which cut part of the gain. Net exports are a balance of both flows.", s: { x: 20, m: 8 } },
] });

/* ---------- Watch 2: government spending and the multiplier ---------- */
function gmDraw(s) {
  const base = 270, xs = [90, 220, 350, 480, 610], vals = [["G rises", 20, "f3"], ["Round 2", 12, "f1"], ["Round 3", 7.2, "f1"], ["Round 4", 4.3, "f1"], ["All later", 6.5, "f1"]];
  let o = SV.line(60, base, 720, base) + tag(60, 34, "Extra income created, $bn (G rises by 20, mpc and tax leave 0.6 spent)", "t1");
  vals.forEach(([l, v, c], i) => { const f = Math.max(0, Math.min(1, s.n - i)); if (f <= 0) return; const h = v * 9 * f; o += SV.rect(xs[i] - 40, base - h, 80, h, c, op(f)) + tag(xs[i], base - h - 8, Lib.fmtN(v, 1), "t1", f, "middle") + SV.text(xs[i], base + 20, l, "sm", { "text-anchor": "middle", ...op(f) }); });
  if (s.t) o += tag(400, 70, "Total rise in income = 20 + 12 + 7.2 + 4.3 + 6.5 = 50 = 20 × 2.5", "t3", 1, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 310, label: "Rounds of extra spending after a rise in government spending of 20", base: { n: 0, t: 0 }, draw: gmDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>The government spends 20.</b> The firms and workers who receive it have 20 of extra income.", s: { n: 1 } },
  { cap: "<b>Round 2.</b> They spend 60% of the extra income (the rest is saved, taxed or spent on imports): 12 of new spending.", s: { n: 2 } },
  { cap: "<b>Round 3.</b> Those who receive the 12 spend 60% of it: 7.2.", s: { n: 3 } },
  { cap: "<b>Round 4.</b> And again: 4.3. Each round is smaller, because part leaks out.", s: { n: 4 } },
  { cap: "<b>The later rounds</b> add up to about 6.5.", s: { n: 5 } },
  { cap: "<b>The total.</b> Income rises by 50, which is 20 × 2.5. The multiplier is 1 ÷ (1 − 0.6). A larger share spent on imports or taxed would shrink it.", s: { n: 5, t: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labNe() {
  if (!$("#fx") || !$("#fi") || !$("#hi")) return;
  const fx = +$("#fx").value, fi = +$("#fi").value, hi = +$("#hi").value, X0 = 100, M0 = 90;
  const X = X0 * (1 + 0.8 * fx / 100 + 0.9 * fi / 100), M = M0 * (1 - 0.7 * fx / 100 + 0.8 * hi / 100), N = X - M, N0 = X0 - M0;
  $("#r1").textContent = Lib.fmtN(X, 1); $("#r2").textContent = Lib.fmtN(M, 1); $("#r3").textContent = (N >= 0 ? "+" : "−") + Lib.fmtN(Math.abs(N), 1);
  $("#rv").textContent = `Net exports change from +${N0} to ${N >= 0 ? "+" : "−"}${Lib.fmtN(Math.abs(N), 1)}. ` + (N > N0 ? "Net exports rise, which adds to aggregate demand." : N < N0 ? "Net exports fall, which reduces aggregate demand." : "Net exports are unchanged.");
  const base = 245, k = 1.2, vals = [[X0, "f3", 90, "X"], [X, "f3", 130, "X"], [M0, "f2", 220, "M"], [M, "f2", 260, "M"]];
  let o = SV.line(30, base, 400, base);
  vals.forEach(([v, c, x, l], i) => { const h = v * k; o += SV.rect(x - 14, base - h, 28, h, c, i % 2 ? {} : { opacity: 0.45 }) + tag(x, base - h - 6, Lib.fmtN(v, 0), i < 2 ? "t3" : "t2", 1, "middle"); });
  o += SV.text(110, 268, "Exports before and after", "sm", { "text-anchor": "middle" }) + SV.text(240, 268, "Imports before and after", "sm", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fx", label: "Change in the exchange rate (% fall, negative is a rise) ", min: -10, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labNe });
Lib.slider($("#g2"), { id: "fi", label: "Rise in foreign income (%) ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labNe });
Lib.slider($("#g3"), { id: "hi", label: "Rise in home income (%) ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labNe });
labNe();
btnTable("lbBtns", "lbOut", [
  ["Exchange rate falls 10%", "Net exports rise (if elastic)", "Exports cheaper abroad, imports dearer at home; check the Marshall-Lerner condition."],
  ["Home inflation above trading partners'", "Net exports fall", "Exports are relatively dearer and imports relatively cheaper."],
  ["A recession abroad", "Net exports fall", "Foreign incomes fall, so demand for exports falls."],
  ["Productivity rises faster than rivals'", "Net exports rise", "Lower unit costs, so exports are more price competitive."],
  ["Home income grows quickly", "Net exports fall", "A share of the extra income is spent on imports (mpm)."]
], ["Change", "Effect on net exports", "Why"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does each change raise or lower net exports?", ["Raises net exports", "Lowers net exports"],
  [("A recession in the main export markets", 1), ("A fall in the exchange rate (with elastic demand)", 0), ("Higher productivity than competitors", 0), ("Home inflation higher than that of trading partners", 1), ("A boom in a trading partner's economy", 0), ("Fast growth in home income that raises imports", 1), ("Better quality and design of exports", 0), ("A rise in the value of the currency", 1)],
  "Think about price competitiveness and incomes at home and abroad.") + MATCH([
  ["Net exports", "Exports minus imports (X − M)"],
  ["Marginal propensity to import", "The change in imports divided by the change in income"],
  ["Average propensity to import", "Imports divided by income"],
  ["Price competitiveness", "How cheap a country's goods are relative to those of rivals"],
  ["Autonomous government spending", "Spending set by policy, not by the level of income"],
  ["Transfer payment", "A payment such as a benefit or pension where nothing is produced in exchange"]]) + ORDER(
  "Put the effect of a fall in the exchange rate in order, starting with the first event.",
  ["The exchange rate falls", "Exports become cheaper for foreign buyers and imports dearer for home buyers", "The volume of exports rises and the volume of imports falls", "Net exports rise, which raises aggregate demand", "National income rises by a multiple of the change in net exports"],
  "The effect depends on elasticities, spare capacity and the time lag.") + CALC([
  {"q": "A country exports $250bn and imports $210bn. Calculate net exports in $bn.", "a": 40, "unit": "$bn", "tol": 0.01, "hint": "X − M.", "sol": "250 − 210 = <b>+$40bn</b>."},
  {"q": "An economy has a national income of $3,200bn and imports of $630bn. Calculate the average propensity to import to two decimal places.", "a": 0.2, "tol": 0.01, "hint": "Imports ÷ income.", "sol": "630 ÷ 3200 = 0.197, so <b>0.20</b>."},
  {"q": "Income rises by $400bn and imports rise by $80bn. Calculate the marginal propensity to import.", "a": 0.2, "tol": 0.01, "hint": "Change in imports ÷ change in income.", "sol": "80 ÷ 400 = <b>0.2</b>."},
  {"q": "The government raises its spending by $30bn. The multiplier is 2.5. By how much does national income rise? Give the answer in $bn.", "a": 75, "unit": "$bn", "tol": 0.01, "hint": "Change in income = injection × multiplier.", "sol": "30 × 2.5 = <b>$75bn</b>."}
]) + MCQ([
  ("Which would be most likely to reduce a country's net exports?", ["A fall in the exchange rate", "Faster productivity growth than its rivals", "A higher rate of inflation than its trading partners", "A boom in its main export markets"], 2, "Higher relative inflation makes exports dearer and imports relatively cheaper."),
  ("Which is a determinant of government spending?", ["The marginal propensity to consume", "The age structure of the population", "The exchange rate alone", "The profits of firms"], 1, "An older population raises spending on health and pensions."),
  ("What is the main effect of government spending on aggregate demand?", ["It is a withdrawal", "It is an injection", "It has no effect", "It is a leakage"], 1, "G is an injection into the circular flow."),
  ("Why may a rise in home income reduce net exports?", ["Imports are an injection", "Part of extra income is spent on imports", "Exports fall automatically", "The exchange rate rises automatically"], 1, "The marginal propensity to import means imports rise with income."),
  ("A fall in the exchange rate will increase net exports if:", ["The sum of the price elasticities of demand for exports and imports is greater than one", "Demand for exports is perfectly inelastic", "Imports are essential goods with inelastic demand", "Foreign incomes fall"], 0, "This is the Marshall-Lerner condition.")
], "qz1") + CARDS([
  ("Net exports", "Exports minus imports (X − M); a component of AD."),
  ("Price competitiveness", "Depends on relative productivity, relative inflation and the exchange rate."),
  ("Quality competitiveness", "Rises with net investment, training and innovation."),
  ("Marginal propensity to import", "Change in imports ÷ change in income."),
  ("Average propensity to import", "Imports ÷ income."),
  ("Government spending", "An injection set by policy, the cycle, the size of the state, population and shocks."),
  ("Marshall-Lerner condition", "A fall in the exchange rate improves the trade balance if the sum of the price elasticities of exports and imports exceeds one."),
  ("Capital vs current spending", "Capital spending raises productive capacity; current spending is used up in the year.")]) + MCQ(mc_exam)

build("sy912g", "government-spending-net-exports", "Government Spending and Net Exports", EY,
  "9.1.2: the determinants of government spending and net exports as components of aggregate demand and how a change in either feeds through the multiplier. Animated diagrams, labs, drills and exam questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
