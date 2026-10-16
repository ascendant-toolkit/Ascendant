"""Syllabus 11.4.2 Income distribution: Gini coefficient and Lorenz curve. Run: python3 tools/artifact-kit/mk_sy1142.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.4.2"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">Lorenz curve</b> plots the <b>cumulative percentage of income</b> against the <b>cumulative percentage of households</b> (ranked from poorest to richest); the further it bows below the <b>45° line of perfect equality</b>, the more unequal the distribution. The <b class="kw">Gini coefficient</b> measures this as <b>the area between the line of equality and the Lorenz curve divided by the whole area under the line of equality</b>, giving a value from <b>0 (perfect equality) to 1 (perfect inequality)</b>. Developing countries often have high inequality, which affects poverty and growth, and <b>taxes, benefits and public services shift the curve</b>. <b>Absolute poverty</b> is living below a fixed minimum income, whereas <b>relative poverty</b> is having much less than the typical household in the same society.</p></div>

  <h2>1 · Drawing the Lorenz curve</h2>
  <div id="pic1" class="card"></div>
  <ol>
    <li>Rank households from the <b>poorest to the richest</b>, usually in five groups (quintiles) of 20% each.</li>
    <li>Work out the <b>cumulative share of income</b> each group has received (for example the poorest 20% have 5%, the poorest 40% have 15%).</li>
    <li>Plot cumulative % of households on the horizontal axis and cumulative % of income on the vertical axis, starting at (0,0) and ending at (100,100).</li>
    <li>The <b>line of perfect equality</b> is the 45° diagonal (the poorest 20% have 20% of income). The <b>Lorenz curve lies below it</b>.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th>Quintile</th><th>Share of income</th><th>Cumulative households</th><th>Cumulative income</th></tr>
    <tr><td>Poorest 20%</td><td>5%</td><td>20%</td><td>5%</td></tr>
    <tr><td>Second 20%</td><td>10%</td><td>40%</td><td>15%</td></tr>
    <tr><td>Middle 20%</td><td>15%</td><td>60%</td><td>30%</td></tr>
    <tr><td>Fourth 20%</td><td>25%</td><td>80%</td><td>55%</td></tr>
    <tr><td>Richest 20%</td><td>45%</td><td>100%</td><td>100%</td></tr>
  </table></div>

  <h2>2 · The Gini coefficient</h2>
  <ul>
    <li><b>Gini = A ÷ (A + B)</b>, where A is the area between the line of equality and the Lorenz curve and B is the area under the Lorenz curve. Since A + B is half the square (0.5), <b>Gini = 2 × A = 1 − 2 × B</b>.</li>
    <li><b>Calculation from quintile data:</b> find the area under the Lorenz curve (B) by adding trapezoids. For the table above: 0.2 × (0 + 0.05) ÷ 2 = 0.005; 0.2 × (0.05 + 0.15) ÷ 2 = 0.02; 0.045; 0.085; 0.155. B = 0.31, so <b>Gini = 1 − 2 × 0.31 = 0.38</b>.</li>
    <li><b>Interpretation:</b> a lower Gini means a more equal distribution; 0 means everyone has the same income, and 1 means one person has everything. It is sometimes given as a percentage (0 to 100). Values for countries range roughly from the 0.25s (very equal) to above 0.6 (very unequal).</li>
    <li><b>Limits:</b> different Lorenz curves can give the same Gini; it measures <b>income</b> before or after tax depending on the data used, and says nothing about wealth unless the wealth is measured; it is affected by the informal economy and by data quality; it does not show how many people are poor in absolute terms.</li>
  </ul>

  <h2>3 · Policies and the shift of the Lorenz curve</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Towards equality</b> (curve moves towards the 45° line, Gini falls): <b>progressive income tax</b>, higher benefits and transfers, a <b>minimum wage</b>, free education and health care (supply-side, raises the earnings of the poor), land reform and support for small farmers, stronger trade unions.</li>
    <li><b>Away from equality</b> (Gini rises): cuts in top tax rates and benefits, more regressive indirect taxes, skill-biased technology and globalisation that rewards the highly skilled, and inheritance of wealth.</li>
    <li><b>Trade-off:</b> high marginal tax rates and benefits may reduce incentives to work and invest (efficiency), so governments balance <b>equity and efficiency</b>.</li>
  </ul>

  <h2>4 · Poverty</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Absolute poverty</th><th>Relative poverty</th></tr>
    <tr><td><b>Meaning</b></td><td>Not having the income to meet basic needs such as food, water and shelter; below a fixed line such as the World Bank's international poverty line of a few dollars a day</td><td>Income well below the typical income in the same society (often below 50% to 60% of the median)</td></tr>
    <tr><td><b>Where it is most common</b></td><td>Low-income countries</td><td>All countries, including rich ones</td></tr>
    <tr><td><b>Falls when</b></td><td>Economic growth raises the incomes of the poor</td><td>Income distribution becomes more equal</td></tr>
  </table></div>
  <ul>
    <li>Economic growth can reduce absolute poverty while <b>relative poverty and inequality rise</b>, if the rich gain faster.</li>
    <li>Causes of high inequality in low-income countries include unequal land and capital ownership, differences in education and health, a dual economy (a small modern sector and a large low-income informal sector), corruption and weak tax systems.</li>
    <li>Inequality can affect growth in both directions: it may raise saving by the rich and give incentives, but it can also limit education and health for the poor, create social tension and reduce demand.</li>
  </ul>
  <div class="tip"><b class="h">Evaluation point</b>A fall in the Gini coefficient is good if it comes from raising the incomes of the poor, but not if it comes from reducing everyone's income. Always say whether absolute poverty has also fallen, and note that a single number hides the shape of the distribution.</div>
'''

watch = '''
  <h2>1 · Building a Lorenz curve and finding the Gini</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · Policies that shift the curve</h2>
  <div id="stP"></div>
'''

explore = '''
  <h2>Lab 1 · The Lorenz curve designer</h2>
  <p>Raise the inequality setting to bow the curve away from equality. See the Gini coefficient and the shares of the poorest 40% and the richest 20%.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Gini coefficient</small><strong id="r1"></strong></div><div><small>Poorest 40% get</small><strong id="r2"></strong></div><div><small>Richest 20% get</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 320" role="img" aria-label="Lorenz curve with the line of perfect equality and the shaded area between"></svg></div></div></div>

  <h2>Lab 2 · Tax the rich, transfer to the poor</h2>
  <p>Start from the quintile shares 5, 10, 15, 25 and 45. Tax part of the richest 20%'s income and pay it equally to the poorest 40%. See the new Gini coefficient.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div>
    <div class="readout"><div><small>Shares after</small><strong id="t1"></strong></div><div><small>Gini before / after</small><strong id="t2"></strong></div><div><small>Change</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 320" role="img" aria-label="Lorenz curves before and after taxing the richest quintile and transferring to the poorest 40 percent"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Does it move the Lorenz curve towards or away from equality?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps to draw a Lorenz curve in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Latin America and inequality", "Several Latin American countries have had Gini coefficients above 0.5 for decades. Cash transfer programmes to poor families and higher minimum wages in some countries in the 2000s lowered inequality, showing how policy can move the Lorenz curve.", "fiscal and supply-side policies for equality, and the Gini coefficient as evidence.") +
rw("Nordic countries", "Countries such as Denmark and Norway have Gini coefficients in the low 0.2s to 0.3s after taxes and transfers. High progressive taxes, generous benefits and strong public education are the main reasons, but tax rates are high and these countries also have strong productivity.", "a low Gini achieved through taxation and public spending, and the equity versus efficiency debate.") +
rw("Fast growth with rising inequality", "In several rapidly growing Asian economies, absolute poverty fell sharply while inequality rose because workers with skills and owners of capital gained fastest. Poverty fell, yet the Gini coefficient and the share of the richest rose.", "growth reducing absolute poverty but not relative poverty.") +
rw("Wealth and income", "Wealth (assets such as property and shares) is usually distributed much more unequally than income. A country's income Gini can look moderate while its wealth Gini is far higher, so the distribution of wealth also matters for equity.", "the distinction between income and wealth distribution.")
)

mc_exam = [
  ("The diagram shows a Lorenz curve with area X between the line of equality and the curve and area Y under the curve. How is the Gini coefficient calculated? (Oct/Nov 2023 · 31 · Q30 and Oct/Nov 2020 · 33 · Q14, reworded)", ["X divided by (X plus Y)", "(X plus Y) divided by X", "(X plus Y) divided by Y", "Y divided by (X plus Y)"], 0, "The Gini coefficient is the area between the line of equality and the curve as a share of the whole triangle under the line of equality."),
  ("On a Lorenz curve diagram the area X between the line of equality and the curve is one third of the area Y below the curve. What is the Gini coefficient? (Oct/Nov 2021 · 31 · Q15, reworded)", ["1/3", "1/4", "3/4", "3"], 1, "The whole triangle is X + Y = 4 parts, of which X is 1 part, so the Gini coefficient is 1/4."),
  ("The Gini coefficient is 24.7 for Denmark, 32.7 for France, 50.4 for Zambia and 74.3 for Namibia. Which statement is correct? (May/June 2024 · 31 · Q30, reworded)", ["Income is distributed more equally in Denmark than in France", "Income is distributed more equally in Namibia than in Zambia", "Income per capita is higher in Zambia than in Namibia", "A larger share of people are below the poverty line in Zambia than in France"], 0, "A lower Gini means more equal. The table gives no information about income per head or poverty."),
  ("When assessing income distribution, which change in the Gini coefficient suggests more equal distribution? (Oct/Nov 2023 · 32 · Q27, reworded)", ["It has moved closer to one", "It has moved closer to zero", "It has moved from negative to positive", "It has moved from positive to negative"], 1, "Zero is perfect equality. The Gini coefficient cannot be negative."),
  ("A country's Gini coefficient is 0.40. The poorest earners pay no income tax. The government raises the tax rate on the highest earners and income becomes more equal. What can be concluded? (May/June 2021 · 31 · Q15, reworded)", ["The Gini coefficient falls and the tax system is more progressive", "The Gini coefficient falls and the tax system is more regressive", "The Gini coefficient rises and the tax system is more progressive", "The Gini coefficient rises and the tax system is more regressive"], 0, "Taxing high earners more makes the system more progressive and reduces inequality."),
  ("The Lorenz curves show Norway (N) and India (I), with Norway closer to the line of equality. What can be concluded? (May/June 2023 · 31 · Q16, reworded)", ["India is more likely to have lower indirect taxes and public education than Norway", "India is more likely to have a progressive income tax and means-tested benefits than Norway", "Norway is more likely to have a progressive tax system and public sector pensions than India", "Norway is likely to rely more on indirect taxes and private pensions than India"], 2, "A more equal distribution is consistent with progressive taxes and public provision."),
  ("Which combination of fiscal measures would be most effective in reducing income inequality? Top rates of income tax, indirect taxes, value of state benefits. (Oct/Nov 2023 · 32 · Q13, reworded)", ["Increase, increase, increase", "Increase, reduce, increase", "Reduce, increase, reduce", "Reduce, reduce, reduce"], 1, "Higher top income tax, lower indirect taxes (which are regressive) and higher benefits all reduce inequality."),
  ("What is most likely to increase relative poverty in a country? (Oct/Nov 2023 · 33 · Q13, reworded)", ["Increasing means-tested benefits", "Increasing the power of trade unions", "Making the tax system more progressive", "Removing the national minimum wage"], 3, "Without a minimum wage, the lowest pay may fall relative to median incomes."),
  ("Which policy could reduce income inequality in the short run in a country with high inequality? (Oct/Nov 2024 · 32 · Q15, reworded)", ["Raise VAT on luxury goods", "Introduce a minimum wage", "Invest heavily in schools", "Stimulate growth through skills training"], 1, "A minimum wage raises low pay quickly. Education and training take years to affect incomes.")
]

exam = exam_page("income distribution, the Gini coefficient, the Lorenz curve and poverty",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The Gini coefficient and poverty appear in data response parts and in Paper 3 every year, and income distribution policy is a regular essay topic. Reworded past questions are below, with nine Paper 3 multiple choice questions.",
  [("Data response parts, 3 to 8 marks", "4", "May/June 2024 (41) Q1(a), (b), (c), (d)"), ("Multiple choice (Paper 3)", "9 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2024 · 9708/41 · Q1(a)", "3 marks", "Describe what is meant by the Gini coefficient and its possible range of values.",
     ["A measure of income inequality (or less commonly wealth) among a population (1).",
      "It ranges from 0 (or 0%) to 1 (or 100%) (1), where 0 is perfect equality and 1 is perfect inequality (1)."],
     "What it measures. The range. What 0 and 1 mean.",
     [[("k", "The Gini coefficient measures the inequality of income, or less often wealth, in a population. It ranges from 0 to 1, where 0 means everyone has the same income and 1 means one person has all the income.")]]),
  eq("Based on May/June 2024 · 9708/41 · Q1(b)", "3 marks", "Distinguish between absolute poverty and relative poverty.",
     ["Absolute: not having the income to buy the commodities needed to sustain life, often shown as a level of income per day below a poverty line (World Bank definition accepted).",
      "Relative: income low compared with the income of other groups in the same society."],
     "Absolute against a fixed line. Relative against others in society.",
     [[("k", "Absolute poverty means having an income below the level needed for basic needs, such as the World Bank's international poverty line. Relative poverty means having an income that is low compared with the typical income in the same society, so it can exist in rich countries.")]]),
  eq("Based on May/June 2024 · 9708/41 · Q1(c)", "6 marks", "A table shows five countries. Country A: Gini 0.52, female to male literacy ratio 1.00, 5% of people below the poverty line. Country B: 0.41, 0.97, 8%. Country C: 0.38, 0.93, 12%. Country D: 0.34, 0.88, 22%. Country E: 0.29, 0.70, 31%. Consider whether the table supports the conclusion that greater inequality is linked to lower female to male literacy ratios and leads to greater poverty.",
     ["No apparent link to poor literacy ratios: the countries with higher Gini coefficients have better literacy ratios.",
      "Higher Gini coefficients are also found where a smaller percentage is below the poverty line, so there is no link to absolute poverty.",
      "A cause and effect cannot be determined; the table says nothing about relative poverty.",
      "Up to 2 marks for correct use of the data."],
     "Quote data: Gini 0.52 with literacy 1.00 and poverty 5%; Gini 0.29 with literacy 0.70 and poverty 31%. Say there is no link, and a correlation does not show cause. Mention what is missing.",
     [[("n", "The table does not support the conclusion. The country with the highest Gini coefficient (A, 0.52) has the best literacy ratio (1.00) and the lowest share of people in poverty (5%), whereas the country with the lowest Gini (E, 0.29) has the lowest literacy ratio (0.70) and 31% in poverty. The pattern is the opposite of the claim, since higher inequality goes with better literacy and less absolute poverty.")],
      [("e", "In any case, five countries are too few to prove a cause, and a link between two variables does not show that one causes the other. The table says nothing about relative poverty, and other factors such as the level of income, education spending and policy could explain the differences.")]]),
  eq("Based on May/June 2024 · 9708/41 · Q1(d)", "8 marks", "Use one example of a supply-side policy and one example of a fiscal policy to assess how a government might achieve a more equal distribution of income.",
     ["Fiscal policy: a correct example (1), developed (2) and a link to equality (1), for example progressive income tax and higher transfers to the poor.",
      "Supply-side policy: a correct example (1), developed (2) and a link to equality (1), for example investment in education and training.",
      "Evaluation points may gain credit within the development."],
     "Fiscal: progressive tax and transfers, so poorer households gain and richer households lose. Supply-side: education, so low-paid workers gain skills and earn more over time.",
     [[("k", "A fiscal policy is a more progressive income tax with higher benefits for low-income households."), ("n", "Taking a larger share of the incomes of the rich and transferring it to the poor could reduce the Gini coefficient and move the Lorenz curve towards the line of equality. It works quickly, but high marginal tax rates could reduce incentives to work.")],
      [("k", "A supply-side policy is greater spending on education and training."), ("n", "This may raise the productivity and wages of low-paid workers, so their incomes rise relative to those of the highly skilled, which could make distribution more equal in the long run. The benefit may take many years and depends on jobs being available.")]])
  ],
  )

tips = tips_html(
  [("Label the Lorenz axes.", "Cumulative % of households along the bottom, cumulative % of income up the side, and the 45° line of equality."),
   ("Gini equals A over A plus B.", "Area between the curves divided by the whole triangle. A bigger curve bow means a higher Gini."),
   ("Quote the range.", "Zero is perfect equality, one is perfect inequality."),
   ("Do the trapezoids.", "In a calculation find the area under the curve, then Gini = 1 − 2 × that area."),
   ("Pair absolute with relative poverty.", "Fixed line against comparison with others."),
   ("Name policy and mechanism.", "Progressive tax: takes more from high earners. Education: raises earnings of the poor over time."),
   ("Mention the trade-off.", "Equity against efficiency, and the time lags.")],
  [("Lorenz", "The Lorenz curve may show how far the cumulative share of income differs from perfect equality."),
   ("Gini", "A rise in the Gini coefficient could indicate that income has become more unequal."),
   ("Absolute", "Absolute poverty is measured against a fixed level of income needed for basic needs."),
   ("Relative", "Relative poverty compares income with the typical income in the same society."),
   ("Policy", "Progressive taxes and transfers may reduce inequality quickly, while education may raise the incomes of the poor over time.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
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
''' + CLASSIFY("cl1", "Towards equality or away from equality?", ["Towards equality", "Away from equality"],
  [("A more progressive income tax", 0), ("A cut in the top rate of income tax", 1), ("A higher national minimum wage", 0), ("Cutting welfare benefits", 1), ("More spending on free education and health", 0), ("A rise in indirect taxes on basic goods", 1), ("Skill-biased technology that raises the pay of the highly skilled", 1), ("Land reform that gives small farmers more land", 0)],
  "Progressive taxes, transfers and public services move the curve towards the line of equality.") + MATCH([
  ["Lorenz curve", "Cumulative share of income plotted against cumulative share of households"],
  ["Gini coefficient", "Area between the line of equality and the Lorenz curve divided by the area under the line"],
  ["Line of perfect equality", "The 45° line where each group has an equal share"],
  ["Absolute poverty", "Income below a fixed level needed for basic needs"],
  ["Relative poverty", "Income low compared with others in the same society"],
  ["Progressive tax", "A tax that takes a higher percentage of higher incomes"]]) + ORDER(
  "Put the steps to draw a Lorenz curve in order.",
  ["Rank households from poorest to richest", "Work out each group's share of income", "Calculate the cumulative shares", "Plot cumulative households against cumulative income", "Compare the curve with the 45° line"],
  "The more the curve bows away from the line, the higher the Gini.") + CALC([
  {"q": "In a Lorenz diagram the area between the line of equality and the curve (A) is 0.15 and the area under the curve (B) is 0.35. Calculate the Gini coefficient.", "a": 0.3, "unit": "", "tol": 0.005, "hint": "A ÷ (A + B).", "sol": "0.15 ÷ 0.50 = <b>0.30</b>."},
  {"q": "The poorest 20%, 40%, 60% and 80% have 8%, 20%, 38% and 62% of income. What share of income does the richest 20% have (%)?", "a": 38, "unit": "%", "tol": 0.5, "hint": "100 − 62.", "sol": "<b>38%</b>."},
  {"q": "The area under a Lorenz curve is 0.28. Calculate the Gini coefficient.", "a": 0.44, "unit": "", "tol": 0.005, "hint": "1 − 2 × 0.28.", "sol": "<b>0.44</b>."},
  {"q": "Median income is $20,000. Relative poverty is defined as below 60% of the median. What is the poverty line ($)?", "a": 12000, "unit": "$", "tol": 0.5, "hint": "0.6 × 20,000.", "sol": "<b>$12,000</b>."}]) + MCQ([
  ("A Gini coefficient of zero means:", ["Perfect equality", "Perfect inequality", "No poverty", "No inflation"], 0, "Everyone has the same income."),
  ("A Lorenz curve that moves closer to the 45° line shows:", ["More equality", "More inequality", "No change", "Higher growth"], 0, "A smaller area A and a lower Gini."),
  ("Which policy is most likely to lower the Gini coefficient?", ["A more progressive income tax", "Cutting the top tax rate", "Cutting benefits", "A flat tax"], 0, "Progressive taxes take more from higher incomes."),
  ("Relative poverty is best described as:", ["Income low compared with others in the society", "Income below $2 a day", "Having no income", "A high inflation rate"], 0, "It is measured against typical incomes."),
  ("Economic growth could reduce absolute poverty while:", ["Raising inequality", "Always lowering inequality", "Removing all poverty", "Increasing the Lorenz curve area to zero"], 0, "The rich may gain faster than the poor.")
], "qz1") + CARDS([
  ("Lorenz curve", "Cumulative income vs cumulative households."),
  ("Gini coefficient", "A ÷ (A + B); 0 to 1."),
  ("Line of equality", "The 45° line."),
  ("Absolute poverty", "Below a fixed income line."),
  ("Relative poverty", "Low compared with society's typical income."),
  ("Progressive tax", "Higher percentage on higher incomes."),
  ("Equity vs efficiency", "Redistribution may reduce incentives."),
  ("Gini from B", "Gini = 1 − 2B.")]) + MCQ(mc_exam)

build("sy1142", "income-distribution-gini-lorenz", "Income Distribution: Gini Coefficient and Lorenz Curve", EY,
  "11.4.2: drawing and reading a Lorenz curve, calculating the Gini coefficient, poverty, and the policies that change the distribution of income. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
