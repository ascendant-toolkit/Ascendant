"""AS syllabus 3.3.4 Policies to redistribute income and wealth. Run: python3 tools/artifact-kit/mk_as37.py"""
from asx import *
EY = EYAS("3.3.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments redistribute income and wealth to reduce <b>inequality</b> and poverty, using four main policies: a <b class="kw">minimum wage</b>, <b class="kw">transfer payments</b> (benefits and pensions), <b class="kw">progressive taxes</b> (income tax, inheritance and capital taxes) and <b class="kw">state provision of essential goods and services</b> such as education and health care. Progressive taxes take a <b>larger proportion of higher incomes</b>; the <b>marginal rate</b> of tax is higher than the <b>average rate</b>, whereas a <b>regressive</b> tax such as a sales tax takes a larger share of low incomes and a <b>proportional</b> tax takes the same share. Each policy has costs: higher taxes may weaken <b>incentives</b>, benefits cost money and may create <b>dependency</b>, a minimum wage above equilibrium may <b>raise unemployment</b>, and state provision has an <b>opportunity cost</b>. The best mix depends on how large the gap is and how the economy would respond.</p></div>

  <h2>1 · Taxes and rates</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Share of income taken as income rises</th><th>Example</th></tr>
    <tr><td><b>Progressive</b></td><td>Rises: higher earners pay a larger share</td><td>Income tax with bands: 0%, 20%, 40%</td></tr>
    <tr><td><b>Proportional</b></td><td>Stays the same</td><td>A flat 15% tax on income</td></tr>
    <tr><td><b>Regressive</b></td><td>Falls: low earners pay a larger share of income</td><td>Sales tax or a duty on fuel or tobacco</td></tr>
  </table></div>
  <ul>
    <li><b>Marginal rate of tax (MRT)</b> = the tax on the <b>extra</b> income earned = change in tax ÷ change in income. <b>Average rate (ART)</b> = total tax ÷ total income.</li>
    <li>Under a <b>progressive</b> tax the MRT is <b>above</b> the ART; under a <b>regressive</b> tax the MRT is <b>below</b> the ART.</li>
    <li><b>Direct taxes</b> (income, profit, inheritance, capital gains) are paid directly to the government by the person or firm; <b>indirect taxes</b> are on spending (VAT, duties).</li>
    <li><b>Inheritance and capital taxes</b> tax transfers of wealth and gains on assets, so they target <b>wealth</b> inequality; they can be avoided by transferring assets early.</li>
  </ul>

  <h2>2 · The minimum wage</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>A <b>minimum wage</b> is a price floor in the labour market. If set <b>above the equilibrium wage</b>, workers who keep jobs earn more, but <b>quantity of labour demanded falls</b> and quantity supplied rises, so <b>unemployment</b> may rise.</li>
    <li>It matters how elastic labour demand is: if demand is <b>inelastic</b> few jobs are lost and low-paid workers gain; if <b>elastic</b>, more jobs are lost.</li>
    <li>It does not help <b>people without a job</b> or those with <b>wealth</b> differences, so it is a narrow policy.</li>
  </ul>

  <h2>3 · Transfer payments and state provision</h2>
  <ul>
    <li><b>Transfer payments</b> (unemployment benefit, pensions, child benefit) move money from taxpayers to recipients <b>without any output</b> being produced. They raise the incomes of the poorest directly but cost taxpayers, may reduce the <b>incentive to work</b> and need administration.</li>
    <li><b>State provision</b> of essentials (education, health care, housing, free school meals) is redistribution <b>in kind</b>: poorer households gain most because it is a larger share of their income. It is costly and subject to waiting lists.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Advantage</th><th>Disadvantage</th></tr>
    <tr><td><b>Minimum wage</b></td><td>Raises pay of the low-paid without government spending</td><td>May cause unemployment; ignores those out of work</td></tr>
    <tr><td><b>Progressive income tax</b></td><td>Raises revenue fairly; narrows the gap after tax</td><td>May weaken incentives; avoidance and evasion</td></tr>
    <tr><td><b>Inheritance and capital taxes</b></td><td>Target wealth, not just income</td><td>Hard to collect; assets can be moved</td></tr>
    <tr><td><b>Transfer payments</b></td><td>Direct help for the poorest</td><td>Cost; possible dependency</td></tr>
    <tr><td><b>State provision</b></td><td>Gives access to essentials regardless of income</td><td>Opportunity cost; queues; inefficiency</td></tr>
  </table></div>

  <h2>4 · Worked examples</h2>
  <p><b>A progressive income tax.</b> Suppose the first $10,000 of income is tax-free, the next $20,000 is taxed at 20% and income above $30,000 is taxed at 40%.</p>
  <div class="tw"><table class="t">
    <tr><th>Income</th><th>Tax</th><th>Average rate</th><th>Marginal rate</th></tr>
    <tr><td>$10,000</td><td>$0</td><td>0%</td><td>0% up to $10,000</td></tr>
    <tr><td>$30,000</td><td>20% × $20,000 = $4,000</td><td>13.3%</td><td>20% on income from $10,000 to $30,000</td></tr>
    <tr><td>$50,000</td><td>$4,000 + 40% × $20,000 = $12,000</td><td>24%</td><td>40% on income above $30,000</td></tr>
    <tr><td>$100,000</td><td>$4,000 + 40% × $70,000 = $32,000</td><td>32%</td><td>40%</td></tr>
  </table></div>
  <ul>
    <li>The tax is <b>progressive</b> because the <b>average rate rises</b> with income (0%, 13.3%, 24%, 32%), and the marginal rate (40%) is above the average rate.</li>
    <li><b>Marginal rate of tax</b> = change in tax ÷ change in income. From $30,000 to $50,000: ($12,000 − $4,000) ÷ $20,000 = 40%.</li>
  </ul>
  <p><b>A regressive sales tax.</b> A 10% sales tax is paid on spending. A household with income of $10,000 spends $9,000 and pays $900, which is 9% of its income. A household with income of $100,000 spends $60,000 and pays $6,000, which is 6% of its income. The tax takes a smaller share of the higher income, so it is regressive even though the rate on spending is the same.</p>

  <h2>5 · Effects of a minimum wage: a worked example</h2>
  <p>Suppose the equilibrium wage is $8 an hour and 1,000 workers are employed. A minimum wage of $10 is introduced, and labour demand falls to 900 workers, while 1,100 want to work.</p>
  <ul>
    <li><b>Winners:</b> the 900 workers who keep jobs gain $2 an hour (and those on low pay in other jobs may also get a rise).</li>
    <li><b>Losers:</b> 100 workers lose their jobs, and there are 200 unemployed in total (1,100 − 900), so the policy helps some low-paid workers at the cost of others.</li>
    <li><b>Employers:</b> costs rise, so some may cut hours, raise prices or replace labour with machines.</li>
    <li>If demand for labour is inelastic, few jobs are lost; if it is elastic, many jobs are lost.</li>
  </ul>

  <h2>6 · Evaluating redistribution policies</h2>
  <ul>
    <li><b>Incentives:</b> high marginal rates of tax may reduce the reward for working and enterprise; generous benefits may discourage job search.</li>
    <li><b>Avoidance and evasion:</b> high taxes encourage people to move income or assets out of reach.</li>
    <li><b>Cost and funding:</b> transfers and state provision need tax revenue, so there is an opportunity cost.</li>
    <li><b>Targeting:</b> universal benefits help the poor but also go to the better off; means-tested ones are cheaper but may create poverty traps.</li>
    <li><b>Time lags:</b> improving education changes the distribution of income only over many years.</li>
    <li><b>Inequality of wealth:</b> income taxes and benefits do not directly address it; inheritance and capital taxes do, but are hard to collect.</li>
    <li><b>Judgement:</b> a mix of progressive taxes, transfers and provision of education and health is likely to be more effective than any one policy.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name the policy, explain <b>how</b> it narrows the gap, then give a <b>limit</b>. For essays, compare at least two and conclude which is <b>most effective</b> and why. Do not confuse progressive (a feature of a tax) with direct (who pays it).</div>
'''

watch = '''
  <h2>1 · Progressive, proportional and regressive taxes</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · A minimum wage in the labour market</h2>
  <div id="stW"></div>
'''

explore = '''
  <h2>Lab 1 · An income tax calculator</h2>
  <p>The first $10,000 is tax free, the next $20,000 is taxed at 20% and income above $30,000 at 40%. Choose an income.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Tax paid</small><strong id="r1"></strong></div><div><small>Average rate</small><strong id="r2"></strong></div><div><small>Marginal rate</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Average rate of tax rising with income under a progressive income tax"></svg></div></div></div>

  <h2>Lab 2 · Redistribution and the Gini coefficient</h2>
  <p>Five equal groups earn $10k, $20k, $30k, $45k and $95k. Tax the income above $30k and pass some of the revenue to the poorest two groups.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Gini before</small><strong id="t1"></strong></div><div><small>Gini after</small><strong id="t2"></strong></div><div><small>Revenue raised</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of income for five groups before and after redistribution"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Progressive, proportional or regressive?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the policy to its effect</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a minimum wage in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Income tax bands", "A worker earning $20,000 pays tax only on income above the allowance, so the average rate is low. A manager earning $90,000 pays 40% on the top slice, so the average rate is much higher. Both pay the same rate on a given slice, but the average rate rises with income.", "progressive taxation and the marginal versus average rate.") +
rw("Sales tax on food", "A flat 10% sales tax on food takes the same percentage of each purchase, but low-income households spend most of their income on food, so the tax takes a bigger share of their income. It is regressive.", "why indirect taxes can be regressive.") +
rw("Child benefit and pensions", "These are transfer payments: money is moved from taxpayers to families and pensioners with no output in return. They lift the incomes of low-income groups, but they cost money and may affect work choices.", "transfer payments.") +
rw("A national minimum wage", "Many countries set a legal wage floor. Low-paid workers who keep jobs gain, but some firms may hire fewer workers or replace them with machines, so the overall effect depends on how elastic demand for labour is.", "the minimum wage and the unemployment risk.") +
rw("Progressive income tax bands", "A government taxes the first slice of income at 0%, the next at 20% and income above a higher threshold at 40%. Higher earners pay a larger share of their income, which narrows the gap after tax.", "a progressive tax and the marginal rate.") +
rw("Free school meals", "Providing free meals in school gives children from poorer households a meal worth a larger share of their family's income than for richer households. It is redistribution in kind, paid for by taxpayers.", "state provision as redistribution.")
)

mc_exam = [
  mcq("m22_12", 17, "Three types of tax are listed: a sales tax (VAT) on fuel; a specific tax of 10% on cigarettes; the percentage of income tax on individual earnings increases as taxable income increases. Which combination describes the effect of each of these types of tax?", ["VAT progressive, specific tax progressive, income tax regressive", "VAT progressive, specific tax regressive, income tax progressive", "VAT regressive, specific tax progressive, income tax regressive", "VAT regressive, specific tax regressive, income tax progressive"], 3, "Sales taxes and duties take a larger share of low incomes, so they are regressive. An income tax whose rate rises with income is progressive."),
  mcq("m24_12", 14, "A country uses an income tax under which the first $10 000 of income is tax-free, the next $20 000 is taxed at 20% and any income over $30 000 is taxed at a top rate of 40%. It also levies a sales tax of 10% on most products. Which combination of tax changes is most likely to create a more equal distribution of income?", ["a higher tax-free allowance and a higher rate of sales tax", "a higher top rate of income tax and a lower rate of sales tax", "a lower tax-free allowance and more goods exempt from sales tax", "a lower top rate of income tax and fewer goods exempt from sales tax"], 1, "A higher top rate takes more from the rich, and a lower sales tax (regressive) helps the poor."),
  mcq("m25_12", 25, "What defines a progressive tax?", ["All taxpayers pay the same proportion of income in taxes", "Low-income earners pay a lower proportion of income in taxes than high-income earners", "Low-income earners pay less in taxes than high-income earners", "Low-income earners pay more in taxes than high-income earners"], 1, "Progressive means the proportion of income paid rises with income. Option C only says the amount is lower."),
  mcq("s22_12", 14, "Which combination of tax changes is most likely to be regressive in a developed economy?", ["increasing the rate of wealth tax and raising the rate of sales tax (VAT) on luxury products", "introducing a tax on owning property based on its sales value and increasing the rate of income tax", "reducing the basic rate of income tax and increasing the duty on fuel", "removing the tax-free allowance for income tax and extending sales tax (VAT) to include all food"], 3, "Taxing all food and removing the allowance take a greater share of low incomes."),
  mcq("m24_12", 12, "A policy that aims to reduce the degree of inequality of income will also reduce the level of employment in a country. What is most likely to be such a policy?", ["The effective minimum wage is increased by 25%", "The rate of income tax paid by the lowest band of earners is reduced", "The government increases the level of subsidies given to producers of some merit goods", "The government provides more goods that are regarded as essential"], 0, "A higher minimum wage lifts pay for those in work but may reduce the number of workers employers hire."),
  mcq("s22_11", 18, "What is an example of a transfer payment?", ["government spending on hospitals", "government spending on motorways", "minimum wage", "welfare benefits"], 3, "A transfer payment is made without any good or service being produced in return."),
  mcq("m20_12", 18, "What is an example of a transfer payment?", ["a household moving savings from one bank account to another", "a monthly repayment on a loan used to buy a new cooker", "the amount paid to transport goods from one city to another", "the payment of student grants by the government"], 3, "A student grant is paid by the government with no output in return."),
  mcq("m21_12", 15, "What would be a transfer payment?", ["the payment made by a company to its shareholders out of its profits", "the payment made for a legal document to transfer ownership of a house", "the payment made to a retired person in the form of a pension", "the payment made to a professional sports team for the transfer of a player"], 2, "A pension is a transfer payment: income without current production."),
  mcq("s22_14", 14, "Money is paid by the government to an unemployed worker in the form of a benefit. Why is this called a transfer payment?", ["The payment comes from taxes paid by employed workers", "The payment comes from government savings, not current income", "The payment is made without the production of goods and services taking place", "The payment must be spent as directed by the government"], 2, "A transfer payment is made without production of goods and services."),
  mcq("s21_13", 18, "Government spending for a year includes: pensions for elderly people $200m, welfare payments to sick people $200m, spending on hospitals $150m, payment to unemployed workers $100m, defence spending $100m, teachers' salaries $50m. What is the total of transfer payments by this government?", ["$50m", "$500m", "$750m", "$800m"], 1, "Transfers are pensions, welfare payments and payments to unemployed: 200 + 200 + 100."),
  mcq("s22_13", 15, "The table shows government expenditure in two periods (period 1, period 2, $000): new roads 200, 350; welfare benefits 600, 450; armed forces pay 500, 550; state pensions 1100, 1350. By how much had transfer payments changed between periods 1 and 2?", ["0", "+100", "+150", "+300"], 1, "Transfers are welfare benefits (−150) and state pensions (+250): net +100."),
  mcq("s21_13", 28, "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target?", ["economic growth and deregulation", "full employment and increasing the money supply", "income equality and more progressive taxation", "stable prices and decreasing interest rates"], 0, "Deregulation is a supply-side measure aimed at growth. Progressive taxation and the money supply are not supply-side tools for equality and employment.")
]

exam = exam_page("policies to redistribute income and wealth",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Redistribution is a regular 12 mark Paper 2 discussion (minimum wage, which policies work best), with 8 mark parts on progressive and regressive taxes. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2022 (23) Q3(a); Oct/Nov 2023 (21) Q4(a)"), ("Essay parts, 12 marks", "2", "May/June 2025 (24) Q3(b); May/June 2024 (22) Q2(b)"), ("Data response, 6 marks", "1", "Oct/Nov 2024 (22) Q1(d)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("w22_23", "3(a)"), "8 marks", "Explain the difference between a progressive direct tax and a regressive indirect tax, with an example of each.",
     ["Knowledge (up to 2): a direct tax is a tax on income and wealth (1) and an indirect tax is a tax on the sale of or spending on goods and services (1).",
      "Application (up to 3): a valid direct tax, such as income tax (1); why it may be progressive, with reference to the burden of tax as income rises (1) and the marginal rate of taxation being higher than the average rate (1).",
      "Application (up to 3): a valid indirect tax, such as VAT or a duty (1); why it is regressive, with reference to the relative burden on higher and lower income groups (1) and the marginal rate being lower than the average rate (1)."],
     "Direct: income tax, rate rises with income, MRT above ART. Indirect: sales tax, takes more of low incomes, MRT below ART.",
     [[("k", "A direct tax is paid directly to the government by the person or firm on their income or wealth, while an indirect tax is placed on spending on goods and services and collected by retailers.")], [("n", "Income tax is a progressive direct tax: the rate rises with income, so higher earners pay a larger share. The marginal rate, the tax on the next dollar, is above the average rate. VAT or a fuel duty is an indirect tax that is regressive: everyone pays the same amount on the same purchase, but it takes a larger share of a low income because the poor spend a higher proportion of income. The marginal rate is lower than the average rate as income rises.")]]),
  eq(P("s25_24", "3(b)"), "12 marks", "Assess whether a minimum wage policy is the best way to redistribute income in an economy.",
     ["Analysis (up to 8): how a minimum wage works, as a price floor in the labour market, raising the pay of low-paid workers; the possible costs, such as unemployment if set above the equilibrium wage and its limited effect on those out of work; alternative policies, such as progressive taxes, transfer payments or state provision, analysed for how they would redistribute income. Indicative content may include these points.",
      "Evaluation (up to 4): a judgement on whether the minimum wage is the best method, which may depend on its level, labour demand elasticity and the aims of the policy, with a conclusion."],
     "Min wage: raises pay, unemployment risk, ignores unemployed. Alternatives: progressive tax, transfers, state provision. Judge: a mix.",
     [[("n", "A minimum wage is a floor below which pay cannot fall. If set above the equilibrium wage it raises the incomes of low-paid workers who keep their jobs, at no cost to the government. But employers may hire fewer workers, which could raise unemployment, especially if demand for labour is elastic, and it does nothing for the unemployed. Progressive income taxes narrow the gap after tax and fund transfer payments to the poorest, but may weaken incentives. State provision of education and health care helps poorer households in kind, but it has an opportunity cost.")], [("e", "A minimum wage is unlikely to be the best method on its own, because it affects only those in work. It is probably most effective as part of a mix with progressive taxes and transfers, and its success depends on the level at which it is set.")]]),
  eq(P("s24_22", "2(b)"), "12 marks", "Assess the extent to which government policies to redistribute income and wealth are likely to be successful.",
     ["Analysis (up to 8): an explanation of at least two policies, such as progressive taxes, inheritance and capital taxes, transfer payments, a minimum wage and state provision of essential goods, and how each could reduce inequality; the limits on each, such as avoidance, disincentive effects, dependency, cost and unemployment.",
      "Evaluation (up to 4): a judgement on the likely success, based on factors such as the size of the policies, how the economy responds and time lags, with a conclusion."],
     "Two or more policies, each with how it narrows the gap and a limit. Judge: partly successful, depends on size and design.",
     [[("n", "A progressive income tax takes a larger share from higher earners, and the revenue can fund transfer payments such as unemployment benefit, which raise the incomes of the poorest. State provision of education and health care can help poorer households gain skills and good health. But high marginal tax rates could reduce the incentive to work and encourage avoidance, benefits cost money and may create dependency, and wealth is difficult to tax because assets can be hidden or moved.")], [("e", "Such policies are likely to reduce inequality to some extent, but are rarely fully successful. How successful depends on how well they are targeted, how much the economy responds, and how long they take to work. A combination is probably more effective than any single policy.")]]),
  eq(P("w23_21", "4(a)"), "8 marks", "Explain the reasons why governments impose taxes and consider whether an increase in income tax is fairer than an increase in sales taxes.",
     ["Knowledge (up to 3): a clear understanding of the various reasons why governments impose taxes.",
      "Analysis (up to 3): the distinction between a direct tax, such as income tax, and an indirect tax, such as a sales tax, with appropriate reference to fairness.",
      "Evaluation (up to 2): a valid judgement on whether an increase in income tax is fairer than an increase in sales taxes, and a conclusion."],
     "Reasons for tax: revenue, redistribution, discourage demerit goods. Income tax progressive; sales tax regressive. Judge on fairness.",
     [[("k", "Governments tax to raise revenue to pay for public goods and services, to redistribute income, and to discourage consumption of demerit goods.")], [("n", "An increase in income tax is direct and usually progressive: those with higher incomes pay a larger share, so it is generally seen as fairer. An increase in sales taxes is indirect and tends to be regressive, because people on low incomes spend a larger share of their income and so lose a larger share to the tax.")], [("e", "Income tax is therefore likely to be fairer, although high rates may reduce the incentive to work. A sales tax is easier to collect, and exemptions for essentials such as basic foods could make it less regressive.")]]),
  eq(P("w24_22", "1(d)"), "6 marks", "Assess the extent to which the government increasing its education spending may improve the incomes of poorer households.",
     ["Analysis (up to 4): reasons and benefits of the government increasing education spending to improve the incomes of poorer households (up to 3): education is a merit good beneficial to the individual and to society, raising income levels through a better educated and skilled workforce; additional spending may increase the availability of provision and free tuition may make it more affordable to poorer households; it may also reduce other costs of education and raise awareness of its benefits.",
      "Evaluation (up to 2): a judgement on the extent to which the spending improves the incomes of poorer households, with a conclusion."],
     "Benefits: skills, access, lower cost, awareness. Limits: time lag, cost, quality, other barriers. Judge: helps in the long run, not quickly.",
     [[("n", "Spending on education raises the supply and affordability of schooling for poorer households. A better educated, more skilled worker can earn more, so household incomes may rise, and free tuition removes a financial barrier."), ("e", "The effect takes many years and depends on the quality of the education and on the availability of jobs. It improves the incomes of poorer households to some extent, but other policies such as transfers may be needed in the short run.")]])
  ],
  )

tips = tips_html(
  [("Know the three tax types.", "Progressive, proportional, regressive: describe what happens to the share of income."),
   ("Marginal versus average.", "Progressive: MRT above ART. Regressive: MRT below ART."),
   ("Direct is not the same as progressive.", "Progressive describes the rate pattern; direct describes who pays."),
   ("Transfer payments have no output.", "Pensions and benefits, not hospital spending."),
   ("Minimum wage: say above equilibrium.", "Then unemployment may rise."),
   ("Always give a limit.", "Incentives, avoidance, cost, dependency."),
   ("Judge with a mix.", "No single policy is usually best.")],
  [("Progressive tax", "A progressive tax takes a larger proportion of income as income rises."),
   ("Regressive tax", "A regressive tax takes a larger proportion of low incomes."),
   ("Transfer payment", "A transfer payment is a payment with no output produced in return."),
   ("Minimum wage", "A minimum wage may raise the incomes of low-paid workers but could raise unemployment."),
   ("Assess", "Redistribution policies are likely to work best in combination.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
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
''' + CLASSIFY("cl1", "What kind of tax is it?", ["Progressive", "Proportional", "Regressive"],
  [("An income tax with rates of 0%, 20% and 40% in bands", 0), ("A flat 15% tax on all income", 1), ("A sales tax on food", 2), ("An inheritance tax with rates rising with the estate's value", 0), ("A fuel duty of a fixed amount per litre", 2), ("A flat 10% tax on company profits", 1), ("A tax on tobacco paid per packet", 2), ("A capital gains tax charged at higher rates on bigger gains", 0)],
  "Progressive: share rises with income. Proportional: same share. Regressive: share falls as income rises.") + MATCH([
  ["Progressive tax", "Takes a larger share of higher incomes"],
  ["Regressive tax", "Takes a larger share of lower incomes"],
  ["Marginal rate of tax", "Tax on the extra income earned"],
  ["Average rate of tax", "Total tax ÷ total income"],
  ["Transfer payment", "A payment with no output in return, such as a pension"],
  ["Minimum wage", "A price floor in the labour market"]]) + ORDER(
  "Put the effects of a minimum wage above equilibrium in order.",
  ["The government sets a minimum wage above the equilibrium wage", "Quantity of labour supplied rises", "Quantity of labour demanded falls", "Unemployment may rise", "Workers who keep their jobs earn more"],
  "Wage floor above equilibrium creates excess supply of labour.") + CALC([
  {"q": "Income tax: 0% on the first $10,000, 20% on the next $20,000, 40% above $30,000. How much tax does someone earning $50,000 pay ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.2 × 20,000 + 0.4 × 20,000.", "sol": "4,000 + 8,000 = <b>$12,000</b>."},
  {"q": "What is the average rate of tax on $50,000 (%)?", "a": 24, "unit": "%", "tol": 0.2, "hint": "12,000 ÷ 50,000.", "sol": "<b>24%</b>."},
  {"q": "What is the marginal rate for that person (%)?", "a": 40, "unit": "%", "tol": 0.2, "hint": "The top band.", "sol": "<b>40%</b>, above the average, so progressive."},
  {"q": "A worker's income rises from $20,000 to $28,000 and tax paid rises from $2,000 to $3,600. What is the marginal rate (%)?", "a": 20, "unit": "%", "tol": 0.2, "hint": "1,600 ÷ 8,000.", "sol": "<b>20%</b>."}]) + MCQ([
  ("A tax that takes a larger share of income from high earners is:", ["Progressive", "Regressive", "Proportional", "Indirect"], 0, "Rate rises with income."),
  ("A sales tax is usually:", ["Regressive", "Progressive", "Proportional only", "A transfer payment"], 0, "Poor households spend more of their income."),
  ("A transfer payment is:", ["A payment with no output in return", "A payment for work", "A tax", "A subsidy to a firm"], 0, "For example a pension."),
  ("A minimum wage above equilibrium may cause:", ["Unemployment", "A shortage of labour", "Lower wages", "A fall in supply"], 0, "Excess supply of labour."),
  ("Under a progressive tax the marginal rate is:", ["Above the average rate", "Below the average rate", "Zero", "Always equal to it"], 0, "The next dollar is taxed more.")
], "qz1") + CARDS([
  ("Progressive", "Rate rises with income."),
  ("Regressive", "Rate falls with income."),
  ("MRT", "Tax on extra income."),
  ("ART", "Total tax ÷ income."),
  ("Transfer payment", "No output in return."),
  ("Minimum wage", "Floor in the labour market."),
  ("State provision", "Help in kind."),
  ("Limits", "Incentives, cost, avoidance.")]) + MCQ(mc_exam)

build("as37", "as-redistribution-policies", "Policies to Redistribute Income and Wealth", EY,
  "3.3.4: progressive, proportional and regressive taxes, marginal and average rates, transfer payments, the minimum wage and state provision. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
