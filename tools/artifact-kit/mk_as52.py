"""AS syllabus 5.2.4 Taxation: types, marginal and average rates, reasons. Run: python3 tools/artifact-kit/mk_as52.py"""
from asx import *
EY = EYAS("5.2.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments tax to <b>raise revenue</b> to pay for public goods and services, to <b>redistribute income</b>, to <b>discourage demerit goods</b> and <b>correct externalities</b>, and to <b>influence aggregate demand</b>. <b>Direct taxes</b> (income, corporation, inheritance) are paid straight to the government by the person or firm they are levied on, while <b>indirect taxes</b> (VAT, duties) are paid on spending and collected by sellers; a tax can be <b>progressive</b> (the share of income taken rises with income), <b>regressive</b> (it falls) or <b>proportional</b> (it is constant). The <b>marginal rate of taxation (MRT)</b> is the percentage of <b>extra</b> income taken in tax, while the <b>average rate (ART)</b> is the percentage of <b>total</b> income taken; under a progressive tax the MRT is above the ART. When raising revenue, governments weigh how <b>fair</b>, <b>efficient</b>, <b>easy to collect</b> and <b>certain</b> a tax is, and its effects on <b>incentives</b> and on AD.</p></div>

  <h2>1 · Types of tax (5.2.4)</h2>
  <div class="tw"><table class="t">
    <tr><th>Classification</th><th>Meaning</th><th>Examples</th></tr>
    <tr><td><b>Direct</b></td><td>Paid directly to the government by the person or firm taxed; based on income, profit or wealth</td><td>Income tax, corporation tax, inheritance tax, capital gains tax</td></tr>
    <tr><td><b>Indirect</b></td><td>Levied on spending; collected by retailers and passed to the government</td><td>VAT or sales tax, duties on fuel, alcohol and tobacco</td></tr>
    <tr><td><b>Progressive</b></td><td>The proportion of income paid rises as income rises</td><td>Income tax with rising bands</td></tr>
    <tr><td><b>Regressive</b></td><td>The proportion paid falls as income rises</td><td>Fuel duty, tobacco duty, sales taxes</td></tr>
    <tr><td><b>Proportional</b></td><td>The same proportion at every income</td><td>A flat 15% tax</td></tr>
  </table></div>

  <h2>2 · Marginal and average rates (5.2.4)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>MRT</b> = change in tax ÷ change in income × 100. Example: income rises $100 and $40 more is taken in tax: MRT = 40%.</li>
    <li><b>ART</b> = total tax ÷ total income × 100. Example: income $10,000 and tax $3,000: ART = 30%.</li>
    <li><b>Progressive:</b> MRT &gt; ART, so ART rises with income. <b>Regressive:</b> MRT &lt; ART. <b>Proportional:</b> MRT = ART.</li>
    <li>A high MRT can reduce the <b>incentive</b> to earn extra income, which is a possible disincentive effect.</li>
  </ul>

  <h2>3 · Reasons for taxation (5.2.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Raise revenue</b> to fund public goods, merit goods and transfer payments.</li>
    <li><b>Redistribute income and wealth</b> through progressive taxes and benefits.</li>
    <li><b>Discourage consumption of demerit goods</b> and <b>correct externalities</b>, such as taxes on tobacco, alcohol, sugar and carbon.</li>
    <li><b>Influence AD:</b> higher taxes reduce disposable income and spending (contractionary), lower taxes increase them (expansionary).</li>
    <li><b>Protect domestic industries</b> through tariffs on imports.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Direct taxes</th><th>Indirect taxes</th></tr>
    <tr><td><b>Fairness</b></td><td>Can be progressive and fairer</td><td>Often regressive</td></tr>
    <tr><td><b>Incentives</b></td><td>High rates may discourage work and enterprise</td><td>Do not affect pay directly, but raise prices</td></tr>
    <tr><td><b>Collection and avoidance</b></td><td>Costlier to collect; avoidance and evasion are possible</td><td>Easier and quicker to raise; harder to avoid</td></tr>
    <tr><td><b>Effect on demerit goods</b></td><td>None directly</td><td>Can discourage them</td></tr>
  </table></div>

  <h2>4 · Worked examples</h2>
  <p><b>An income tax with three bands.</b> The first $12,000 of income is tax-free, income from $12,000 to $40,000 is taxed at 20%, and income above $40,000 is taxed at 40%.</p>
  <div class="tw"><table class="t">
    <tr><th>Income</th><th>Tax</th><th>Average rate (ART)</th><th>Marginal rate (MRT)</th></tr>
    <tr><td>$12,000</td><td>$0</td><td>0%</td><td>0%</td></tr>
    <tr><td>$30,000</td><td>20% × $18,000 = $3,600</td><td>12%</td><td>20%</td></tr>
    <tr><td>$40,000</td><td>20% × $28,000 = $5,600</td><td>14%</td><td>20%</td></tr>
    <tr><td>$60,000</td><td>$5,600 + 40% × $20,000 = $13,600</td><td>22.7%</td><td>40%</td></tr>
    <tr><td>$100,000</td><td>$5,600 + 40% × $60,000 = $29,600</td><td>29.6%</td><td>40%</td></tr>
  </table></div>
  <ul>
    <li>The tax is <b>progressive</b>: the average rate rises with income, and the marginal rate is always at or above the average rate.</li>
    <li>When income rises from $40,000 to $60,000, the extra tax is $8,000 (13,600 − 5,600), so the MRT = 8,000 ÷ 20,000 = 40%. A worker keeps only 60 cents of each extra dollar, which may reduce the <b>incentive</b> to work more.</li>
  </ul>
  <p><b>A regressive indirect tax.</b> A 10% sales tax is paid on spending. A household with income of $15,000 spends $14,000 and pays $1,400 (9.3% of income). A household with income of $120,000 spends $70,000 and pays $7,000 (5.8% of income). The ART falls as income rises, so the tax is regressive, although it has the same rate on spending.</p>

  <h2>5 · Direct or indirect: raising more revenue</h2>
  <div class="tw"><table class="t">
    <tr><th>Criterion</th><th>Raising direct taxes</th><th>Raising indirect taxes (for example VAT)</th></tr>
    <tr><td><b>Amount raised</b></td><td>Can be large from high earners, but depends on the tax base and avoidance</td><td>Wide base: everyone who spends pays, so revenue is large and stable</td></tr>
    <tr><td><b>Fairness</b></td><td>More progressive: those with more income pay more</td><td>Regressive effect: poorer households pay more as a share of income</td></tr>
    <tr><td><b>Incentives</b></td><td>High marginal rates may reduce work effort and encourage avoidance or emigration</td><td>Do not reduce pay directly, but raise prices and may reduce spending</td></tr>
    <tr><td><b>Collection costs and evasion</b></td><td>Needs a good tax system; informal incomes are hard to tax</td><td>Easier to collect at the point of sale; harder to evade, although black markets exist</td></tr>
    <tr><td><b>Effect on inflation</b></td><td>Little direct effect</td><td>Raises the price level once, may start a wage-price pressure</td></tr>
    <tr><td><b>Effect on AD</b></td><td>Reduces disposable income, consumption</td><td>Raises prices, reduces real spending power</td></tr>
  </table></div>
  <ul>
    <li><b>Developing economies</b> often rely more on indirect taxes and trade taxes because incomes are low and many people work informally, which makes income tax hard to collect.</li>
    <li>Whether an indirect tax raises more revenue depends on the <b>price elasticity of demand</b> for the taxed goods: with inelastic demand, quantity falls little and revenue rises most.</li>
  </ul>

  <h2>6 · The features of a good tax</h2>
  <ul>
    <li><b>Equity (fairness):</b> people should pay according to their ability to pay (vertical equity) and people in similar circumstances should pay the same (horizontal equity).</li>
    <li><b>Efficiency:</b> low cost of collection and little distortion of work, saving and spending choices.</li>
    <li><b>Certainty:</b> taxpayers should know what they have to pay and when.</li>
    <li><b>Convenience:</b> easy to pay.</li>
    <li><b>Flexibility:</b> revenue should respond to the economy and allow governments to change rates.</li>
    <li>No tax is best on all criteria, so governments use a <b>mix</b> of taxes.</li>
  </ul>

  <h2>7 · Taxes and the macroeconomy</h2>
  <ul>
    <li><b>Higher taxes</b> reduce disposable income, consumption and AD: they are contractionary. <b>Lower taxes</b> raise AD: they are expansionary.</li>
    <li><b>Supply-side effects:</b> lower income tax may encourage work; lower business taxes may encourage investment.</li>
    <li><b>Automatic stabilisers:</b> progressive taxes take less revenue in a recession and more in a boom, which cushions the economy without any decision.</li>
    <li><b>Redistribution:</b> progressive taxes, with benefits, reduce inequality.</li>
  </ul>
  <div class="warn"><b class="h">Do not write this</b>Progressive means paid by high earners only: lower earners may pay too, but a smaller proportion. Do not confuse a progressive tax with a direct tax, or a regressive tax with an indirect tax (most indirect taxes are regressive but this is not a definition). Do not use the marginal rate as the average rate.</div>
  <div class="tip"><b class="h">Exam tip</b>Give a worked example when explaining MRT and ART. When asked about <b>raising indirect tax for revenue</b>, weigh ease of collection and revenue against <b>regressivity</b>, the effect on inflation and demand, and elasticity of demand for the taxed goods.</div>
'''

watch = '''
  <h2>1 · Marginal and average tax rates</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · A tax increase and aggregate demand</h2>
  <div id="stA"></div>
'''

explore = '''
  <h2>Lab 1 · Calculate MRT and ART</h2>
  <p>Set the income tax bands: tax free up to $10,000, then rate 1 up to $30,000 and rate 2 above it. Choose an income.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Tax paid</small><strong id="r1"></strong></div><div><small>Average rate (ART)</small><strong id="r2"></strong></div><div><small>Marginal rate (MRT)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Average and marginal tax rates against income"></svg></div></div></div>

  <h2>Lab 2 · Direct and indirect tax compared</h2>
  <p>A 20% income tax is compared with a 10% sales tax, when households spend different shares of their income on taxed goods.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Income tax as % of income</small><strong id="t1"></strong></div><div><small>Sales tax as % of income</small><strong id="t2"></strong></div><div><small>Sales tax pattern</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars comparing income tax and sales tax as a share of income for a low and a high income household"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Direct or indirect, progressive or regressive?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a tax rise on AD in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Income tax bands", "A worker earns $50,000. The first $10,000 is tax free, the next $20,000 is taxed at 20% and the rest at 40%. The total tax is $12,000 (average rate 24%), but the tax on the next dollar is 40% (the marginal rate).", "marginal versus average tax rates.") +
rw("Tax on tobacco", "A duty on cigarettes raises large revenue because demand is inelastic, and also discourages smoking. But it is regressive, because poorer households spend a higher share of their income on tobacco.", "indirect taxes: revenue, demerit goods and regressivity.") +
rw("Raising taxes in a boom", "When the economy is overheating and inflation is rising, a government may raise taxes. Disposable income and spending fall, AD shifts left, and inflationary pressure eases.", "contractionary fiscal policy.") +
rw("Tax avoidance", "High marginal rates give wealthy people an incentive to move income abroad or into lightly taxed forms, so the revenue raised may be less than expected.", "a limit of direct taxes.") +
rw("Income tax bands", "A government taxes the first slice of income at 0%, the next at 20% and income above a threshold at 40%. A worker earning just above the threshold pays 40% on only the extra income, not on all of it.", "marginal and average rates in a progressive tax.") +
rw("VAT in low-income countries", "Where many people are paid in cash and do not file tax returns, a sales tax collected at the till raises more revenue than an income tax. Poorer households, however, pay a larger share of income.", "why indirect taxes are common in developing economies, and their regressive effect.")
)

mc_exam = [
  mcq("m24_12", 14, "A country uses an income tax under which the first $10 000 of income is tax-free, the next $20 000 is taxed at 20% and any income over $30 000 is taxed at a top rate of 40%. It also levies a sales tax of 10% on most products. Which combination of tax changes is most likely to create a more equal distribution of income?", ["a higher tax-free allowance and a higher rate of sales tax", "a higher top rate of income tax and a lower rate of sales tax", "a lower tax-free allowance and more goods exempt from sales tax", "a lower top rate of income tax and fewer goods exempt from sales tax"], 1, "A higher top rate takes more from high earners, and a lower sales tax helps the poor, who spend a larger share of their income."),
  mcq("m25_12", 25, "What defines a progressive tax?", ["All taxpayers pay the same proportion of income in taxes", "Low-income earners pay a lower proportion of income in taxes than high-income earners", "Low-income earners pay less in taxes than high-income earners", "Low-income earners pay more in taxes than high-income earners"], 1, "The proportion of income paid rises with income."),
  mcq("s22_12", 14, "Which combination of tax changes is most likely to be regressive in a developed economy?", ["increasing the rate of wealth tax and raising the rate of sales tax (VAT) on luxury products", "introducing a tax on owning property based on its sales value and increasing the rate of income tax", "reducing the basic rate of income tax and increasing the duty on fuel", "removing the tax-free allowance for income tax and extending sales tax (VAT) to include all food"], 3, "Removing the allowance and taxing food take a larger share of low incomes."),
  mcq("s21_12", 17, "The table shows sources of government revenue: sale of government assets 100, tax on self employed 1000, carbon tax on goods produced 100, corporate taxes 500, capital gains tax 100, goods and services tax 1000, air passenger tax 100 ($ billions). What is the total amount of tax revenue raised by indirect taxes?", ["$1,200 billion", "$1,300 billion", "$1,400 billion", "$1,600 billion"], 0, "Indirect taxes: carbon tax 100 + goods and services tax 1000 + air passenger tax 100."),
  mcq("m22_12", 17, "Three types of tax are listed: a sales tax (VAT) on fuel; a specific tax of 10% on cigarettes; the percentage of income tax on individual earnings increases as taxable income increases. Which combination describes the effect of each of these types of tax?", ["VAT progressive, specific tax progressive, income tax regressive", "VAT progressive, specific tax regressive, income tax progressive", "VAT regressive, specific tax progressive, income tax regressive", "VAT regressive, specific tax regressive, income tax progressive"], 3, "Sales taxes and duties are regressive, and an income tax with a rising rate is progressive.")
]

exam = exam_page("taxation",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Taxation appears as an 8 mark part on MRT and ART or on the reasons for taxes, and in several 6 mark data-response parts. Reworded past questions are below, with five Paper 1 multiple choice questions (some also relevant to redistribution).",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2024 (22) Q5(a); Oct/Nov 2023 (21) Q4(a)"), ("Data response, 6 marks", "1", "May/June 2023 (22) Q1(e)"), ("Multiple choice (Paper 1)", "5 shown below", "2021 to 2025")],
  [
  eq(P("w24_22", "5(a)"), "8 marks", "With the help of examples, explain the difference between the marginal rate of taxation and the average rate of taxation and consider whether a government should decide to increase the rate of indirect tax to raise additional revenue.",
     ["Knowledge (up to 3): the marginal rate of tax is the proportion of extra income taken in tax (1); the average rate is the proportion of the whole of income that is taxed (1); an accurate example of each, for example an extra £100 with £40 taken as tax is a marginal rate of 40%, and total earnings of £10 000 with £3000 tax is an average rate of 30% (1).",
      "Analysis (up to 3): discussion focuses on whether the gains in revenue exceed the disadvantages of indirect taxes: they are easier and quicker to put in place than direct taxes; they may be less easy to avoid; but they are regressive, may raise prices and inflation, and reduce spending.",
      "Evaluation (up to 2): a judgement on whether indirect tax should be increased, with a conclusion."],
     "MRT: tax on extra income, with example. ART: total tax ÷ total income, with example. Indirect tax: easy to raise, hard to avoid, but regressive and inflationary. Judge.",
     [[("k", "The marginal rate of taxation is the proportion of extra income taken in tax: if someone earns an extra $100 and $40 is taxed, the MRT is 40%. The average rate is total tax divided by total income: if total earnings are $10,000 and tax is $3,000, the ART is 30%.")], [("n", "Raising indirect taxes such as VAT can bring in revenue quickly, is relatively hard to avoid and does not reduce the incentive to work. But indirect taxes are usually regressive, because low-income households spend a larger share of income, they raise prices and can add to inflation, and they reduce spending on the taxed goods.")], [("e", "An increase in indirect tax may be a reasonable way to raise revenue if demand for the taxed goods is inelastic and some necessities are exempt, but if equity matters more, increasing progressive direct taxes may be fairer. The best choice depends on the government's aims.")]]),
  eq(P("w23_21", "4(a)"), "8 marks", "Explain the reasons why governments impose taxes and consider whether an increase in income tax is fairer than an increase in sales taxes.",
     ["Knowledge (up to 3): a clear understanding of the various reasons why governments impose taxes.",
      "Analysis (up to 3): the distinction between a direct tax, such as income tax, and an indirect tax, such as a sales tax, with appropriate reference to fairness.",
      "Evaluation (up to 2): a valid judgement on whether an increase in income tax is fairer than an increase in sales taxes, with a conclusion."],
     "Reasons: revenue, redistribution, discourage demerit goods, influence AD. Income tax progressive; sales tax regressive. Judge.",
     [[("k", "Governments impose taxes to raise revenue for public services, to redistribute income, to discourage consumption of demerit goods and to influence aggregate demand.")], [("n", "An increase in income tax usually falls more heavily on those with higher incomes, because the marginal rate is above the average rate, which makes it progressive and generally seen as fairer. Sales taxes are indirect and tend to be regressive, because poorer households spend a larger share of their income on goods and services.")], [("e", "On grounds of fairness an increase in income tax is probably fairer, but it may reduce the incentive to work and can be avoided, while sales taxes are easier to collect. The answer depends on whether fairness or simplicity matters more.")]]),
  eq(P("s23_22", "1(e)"), "6 marks", "Assess whether adjusting the collection of direct tax or indirect tax is likely to be more effective in increasing the tax revenue collected by a government.",
     ["Analysis (up to 4): one method of adjusting direct tax, such as introducing a more progressive income tax, with the advantages and disadvantages for raising revenue (up to 3; 1 mark if only advantages or only disadvantages); one method of adjusting indirect tax, such as raising the rate of VAT, with the advantages and disadvantages (up to 3; 1 mark if one-sided); a maximum of 3 marks if only one type of tax is analysed. Issues include fairness and equality, the amount that may be raised and the costs of ensuring compliance.",
      "Evaluation (up to 2): compare and weigh up the likely effectiveness of both types of tax in raising revenue, considering the problems the government faces in raising more, and reach an overall conclusion on which is more effective."],
     "Direct: progressive rates raise revenue from high earners, avoidance, incentives. Indirect: VAT wide base, easy to collect, regressive. Compare and conclude.",
     [[("n", "A more progressive income tax would raise more revenue from higher earners, which is fairer, but high marginal rates may reduce work effort, encourage avoidance, and in a country with a large informal sector few people would pay. Raising VAT would raise revenue from all spending and is easy to collect, but it is regressive, hitting poorer households hardest, and could raise inflation and reduce demand."), ("e", "In a country with a large informal economy, indirect taxes are probably more effective at raising revenue because they are easier to collect, although direct taxes are fairer. A combination is likely to work best.")]])
  ],
  )

tips = tips_html(
  [("Give examples of MRT and ART.", "Use numbers: extra $100, $40 tax."),
   ("MRT is tax on extra income.", "ART is total tax ÷ total income."),
   ("Progressive: MRT above ART.", "Regressive: MRT below ART."),
   ("Direct versus indirect.", "Who pays and how it is collected."),
   ("List several reasons for tax.", "Revenue, redistribution, demerit goods, AD."),
   ("Evaluate indirect taxes.", "Easy to collect but regressive and may raise prices."),
   ("Mention incentives.", "High MRT can discourage work.")],
  [("MRT", "The marginal rate of taxation is the proportion of extra income taken in tax."),
   ("ART", "The average rate of taxation is the proportion of total income paid in tax."),
   ("Progressive", "A progressive tax has a marginal rate above the average rate."),
   ("Indirect tax", "Indirect taxes are easier to collect but are often regressive."),
   ("Reasons", "Governments tax to raise revenue and to influence demand.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- MRT and ART ---------- */
const taxA = (y) => 0.2 * Math.max(0, Math.min(y, 30000) - 10000) + 0.4 * Math.max(0, y - 30000);
function mrDraw(s) {
  const X = (v) => 80 + v / 100000 * 600, Y = (v) => 250 - v * 5; let o = axes(80, 250, 700, 30, "Income ($)", "Tax rate (%)"), a = "", m = "";
  for (let v = 0; v <= 100000; v += 1000) { if (v <= s.k * 1000) { a += (a ? " L" : "M") + X(v) + "," + Y(v ? taxA(v) / v * 100 : 0); const mr = v < 10000 ? 0 : v < 30000 ? 20 : 40; m += (m ? " L" : "M") + X(v) + "," + Y(mr); } }
  if (m) o += SV.path(m, "c3", { fill: "none", "stroke-width": 3 }) + SV.path(a, "c2", { fill: "none", "stroke-width": 3 });
  o += tag(660, Y(40) - 6, "MRT (steps)", "c3", s.k > 90 ? 1 : 0, "end") + tag(660, Y(taxA(100000) / 1000) + 18, "ART", "c2", s.k > 90 ? 1 : 0, "end");
  return o + [0, 20, 40, 60, 80, 100].map((v) => SV.text(X(v * 1000), 268, v + "k", "sm", { "text-anchor": "middle" })).join("");
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Marginal tax rate rising in steps and average tax rate rising smoothly below it">${mrDraw({ k: 100 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 290, label: "MRT and ART under a progressive income tax", base: { k: 0 }, draw: mrDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>The tax.</b> 0% on the first $10,000, 20% on the next $20,000 and 40% above $30,000.", s: { k: 0 } },
  { cap: "<b>Up to $10,000</b> both rates are zero: no tax is paid.", s: { k: 10 } },
  { cap: "<b>From $10,000 to $30,000</b> the marginal rate is 20% but the average rate is lower because part of the income is untaxed; the ART rises towards 13%.", s: { k: 30 } },
  { cap: "<b>Above $30,000</b> the marginal rate jumps to 40%. The average rate keeps rising, always below the MRT: the sign of a <b>progressive</b> tax.", s: { k: 100 } },
] });

/* ---------- tax and AD ---------- */
function taxAD(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tax rise shifts AD to the left">${taxAD({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in income tax shifts AD to the left", base: { a: 0, n: 0 }, draw: taxAD, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, n: 0 } },
  { cap: "<b>Income tax rises.</b> Disposable income falls, so households spend less. AD shifts <b>left</b>: real output and the price level fall. This is <b>contractionary</b> fiscal policy and could be used to reduce inflation.", s: { a: -20, n: 1 } },
  { cap: "<b>An income tax cut</b> does the opposite: more disposable income, more spending, AD shifts right (<b>expansionary</b>).", s: { a: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!["inc", "r1x", "r2x"].every((i) => $("#" + i))) return;
  const y = +$("#inc").value, a = +$("#r1x").value / 100, b = +$("#r2x").value / 100, t = a * Math.max(0, Math.min(y, 30000) - 10000) + b * Math.max(0, y - 30000), art = y ? t / y * 100 : 0, mrt = (y < 10000 ? 0 : y < 30000 ? a : b) * 100;
  $("#r1").textContent = "$" + Lib.fmtN(t, 0); $("#r2").textContent = Lib.fmtN(art, 1) + "%"; $("#r3").textContent = Lib.fmtN(mrt, 0) + "%";
  $("#rv").textContent = `On $${Lib.fmtN(y, 0)} tax is $${Lib.fmtN(t, 0)}: ART = ${Lib.fmtN(art, 1)}%. The tax on the next dollar is ${Lib.fmtN(mrt, 0)}% (MRT). ${mrt > art + 0.05 ? "MRT is above ART, so the tax is progressive." : mrt === art ? "MRT equals ART: proportional." : "MRT is below ART."} ${mrt >= 40 ? "A high MRT may reduce the incentive to earn extra income." : ""}`;
  const X = (v) => 50 + v / 100000 * 340, Y = (v) => 250 - v * 5; let ar = "", mr = "", o = SV.line(50, 250, 400, 250) + SV.line(50, 250, 50, 40);
  for (let v = 0; v <= 100000; v += 2000) { const tt = a * Math.max(0, Math.min(v, 30000) - 10000) + b * Math.max(0, v - 30000); ar += (v ? " L" : "M") + X(v) + "," + Y(v ? tt / v * 100 : 0); mr += (v ? " L" : "M") + X(v) + "," + Y((v < 10000 ? 0 : v < 30000 ? a : b) * 100); }
  o += SV.path(mr, "c3", { fill: "none", "stroke-width": 2.5 }) + SV.path(ar, "c2", { fill: "none", "stroke-width": 3 }) + SV.circle(X(y), Y(art), 6, "dot2") + SV.circle(X(y), Y(mrt), 6, "dot3") + tag(390, 60, "MRT", "c3", 1, "end") + tag(390, 78, "ART", "c2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "inc", label: "Income, $ ", min: 5000, max: 100000, step: 5000, value: 50000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labT });
Lib.slider($("#g2"), { id: "r1x", label: "Rate 1 (on $10k to $30k), % ", min: 5, max: 30, step: 5, value: 20, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g3"), { id: "r2x", label: "Rate 2 (above $30k), % ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v + "%", onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labD() {
  if (!["lw", "hg"].every((i) => $("#" + i))) return;
  const sl = +$("#lw").value / 100, sh = +$("#hg").value / 100, lowY = 20000, highY = 100000, itL = Math.max(0, lowY - 10000) * 0.2 / lowY * 100, itH = (0.2 * 20000 + 0.4 * 70000) / highY * 100, saL = 10 * sl, saH = 10 * sh;
  $("#t1").textContent = "Low " + Lib.fmtN(itL, 1) + "%, high " + Lib.fmtN(itH, 1) + "%"; $("#t2").textContent = "Low " + Lib.fmtN(saL, 1) + "%, high " + Lib.fmtN(saH, 1) + "%"; $("#t3").textContent = saL > saH ? "Regressive" : saL < saH ? "Progressive" : "Proportional";
  $("#tv").textContent = `The income tax takes ${Lib.fmtN(itL, 1)}% of the low earner's income and ${Lib.fmtN(itH, 1)}% of the high earner's: progressive. A 10% sales tax on taxed goods bought with ${Lib.fmtN(sl * 100, 0)}% of the low earner's income and ${Lib.fmtN(sh * 100, 0)}% of the high earner's takes ${Lib.fmtN(saL, 1)}% and ${Lib.fmtN(saH, 1)}% of income: ${saL > saH ? "regressive, because the poorer household spends a larger share of its income" : saL < saH ? "progressive" : "proportional"}.`;
  const Y = (v) => 180 - v * 4; let o = SV.line(40, 180, 400, 180) + SV.line(40, 180, 40, 20);
  [["Income tax, low", itL, "f2"], ["Income tax, high", itH, "f2"], ["Sales tax, low", saL, "f3"], ["Sales tax, high", saH, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(60 + i * 85, Y(v), 60, 180 - Y(v), c, op(0.65)) + SV.text(90 + i * 85, 198, l, "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 85, Y(v) - 6, Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "lw", label: "Share of the low earner's income spent on taxed goods, % ", min: 40, max: 100, step: 5, value: 90, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g5"), { id: "hg", label: "Share of the high earner's income spent on taxed goods, % ", min: 20, max: 100, step: 5, value: 50, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What kind of tax is it?", ["Direct", "Indirect"],
  [("Income tax", 0), ("VAT", 1), ("Corporation tax", 0), ("Fuel duty", 1), ("Inheritance tax", 0), ("A duty on tobacco", 1), ("Capital gains tax", 0), ("A sales tax on food", 1)],
  "Direct taxes fall on income or wealth. Indirect taxes fall on spending.") + MATCH([
  ["Marginal rate of tax", "The proportion of extra income taken in tax"],
  ["Average rate of tax", "Total tax as a proportion of total income"],
  ["Progressive tax", "MRT above ART; share of income rises with income"],
  ["Regressive tax", "Share of income paid falls as income rises"],
  ["Direct tax", "Paid directly by the person or firm taxed"],
  ["Indirect tax", "Levied on spending and collected by sellers"]]) + ORDER(
  "Put the effect of a rise in income tax on AD in order.",
  ["The government raises income tax", "Disposable income falls", "Consumption falls", "AD shifts to the left", "Real output and the price level fall"],
  "Higher tax reduces spending and AD.") + CALC([
  {"q": "A person earns $40,000 and pays $9,000 in tax. What is the average rate of tax (%)?", "a": 22.5, "unit": "%", "tol": 0.1, "hint": "9,000 ÷ 40,000.", "sol": "<b>22.5%</b>."},
  {"q": "Their income rises to $44,000 and tax to $10,600. What is the marginal rate (%)?", "a": 40, "unit": "%", "tol": 0.1, "hint": "1,600 ÷ 4,000.", "sol": "<b>40%</b>."},
  {"q": "Is the tax progressive? Answer 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.1, "hint": "Compare MRT with ART.", "sol": "<b>Yes (1)</b>: MRT (40%) is above ART (22.5%)."},
  {"q": "A household spends $20,000 of a $25,000 income on goods with a 10% sales tax. What share of income does the sales tax take (%)?", "a": 8, "unit": "%", "tol": 0.1, "hint": "2,000 ÷ 25,000.", "sol": "<b>8%</b>."}]) + MCQ([
  ("The marginal rate of tax is:", ["The tax on extra income", "Total tax ÷ total income", "The lowest rate", "The sales tax rate"], 0, "Tax on the next dollar."),
  ("A regressive tax takes:", ["A larger share of low incomes", "A larger share of high incomes", "The same share", "No tax"], 0, "Share falls as income rises."),
  ("Which is an indirect tax?", ["VAT", "Income tax", "Corporation tax", "Inheritance tax"], 0, "On spending."),
  ("A reason governments tax is:", ["To discourage demerit goods", "To increase AD always", "To lower revenue", "To raise imports"], 0, "Correct market failure."),
  ("An increase in income tax will usually:", ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise exports"], 0, "Lower disposable income.")
], "qz1") + CARDS([
  ("MRT", "Tax on extra income."),
  ("ART", "Total tax ÷ income."),
  ("Progressive", "MRT > ART."),
  ("Regressive", "MRT < ART."),
  ("Direct", "On income and wealth."),
  ("Indirect", "On spending."),
  ("Reasons", "Revenue, equity, demerit, AD."),
  ("Tax rise", "AD shifts left.")]) + MCQ(mc_exam)

build("as52", "as-taxation", "Taxation: Types, Rates and Reasons", EY,
  "5.2.4: direct and indirect, progressive, regressive and proportional taxes, marginal and average rates of taxation, and the reasons for taxation. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
