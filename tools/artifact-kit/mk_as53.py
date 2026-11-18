"""AS syllabus 5.2.5-5.2.7 Government spending and fiscal policy. Run: python3 tools/artifact-kit/mk_as53.py"""
from asx import *
EY = EYAS("5.2.5 to 5.2.7")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Fiscal policy</b> is the use of <b>government spending and taxation</b> to influence the economy. Government spending is either <b class="kw">current</b> (day-to-day: wages of public workers, benefits, running costs) or <b class="kw">capital</b> (investment in roads, hospitals, schools), and governments spend to provide <b>public and merit goods</b>, redistribute income, support the economy and raise <b>productive capacity</b>. <b class="kw">Expansionary fiscal policy</b> (higher spending or lower taxes, often a bigger deficit) shifts <b>AD right</b> to raise output and employment; <b class="kw">contractionary fiscal policy</b> (lower spending or higher taxes, a smaller deficit or a surplus) shifts <b>AD left</b> to reduce inflation. The results depend on spare capacity and on limits such as <b>time lags</b>, the <b>cost</b> in higher debt, <b>crowding out</b> of private spending and <b>imports</b> leaking abroad.</p></div>

  <h2>1 · Government spending (5.2.5)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Meaning</th><th>Examples</th></tr>
    <tr><td><b>Current expenditure</b></td><td>Day-to-day spending that does not create a lasting asset</td><td>Salaries of teachers and nurses, running costs, <b>transfer payments</b> (benefits and pensions)</td></tr>
    <tr><td><b>Capital (investment) expenditure</b></td><td>Spending on lasting assets that add to productive capacity</td><td>Roads, railways, schools, hospitals, power networks</td></tr>
  </table></div>
  <ul>
    <li><b>Reasons for spending:</b> provide <b>public goods</b> (defence, street lighting) and <b>merit goods</b> (education, health care); <b>redistribute</b> income; support demand in a recession; invest to raise <b>productive capacity</b>; provide a safety net.</li>
    <li><b>Transfer payments</b> are not part of G in AD; they change AD indirectly through household incomes.</li>
  </ul>

  <h2>2 · Expansionary and contractionary fiscal policy (5.2.6 to 5.2.7)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Expansionary</th><th>Contractionary</th></tr>
    <tr><td><b>Tools</b></td><td>Raise spending, cut taxes</td><td>Cut spending, raise taxes</td></tr>
    <tr><td><b>Budget</b></td><td>Deficit rises (or surplus falls)</td><td>Deficit falls (or surplus rises)</td></tr>
    <tr><td><b>AD</b></td><td>Shifts right</td><td>Shifts left</td></tr>
    <tr><td><b>Real output and employment</b></td><td>Rise (if spare capacity)</td><td>Fall</td></tr>
    <tr><td><b>Price level</b></td><td>Rises (more near full capacity)</td><td>Falls (inflation reduced)</td></tr>
    <tr><td><b>Used when</b></td><td>Recession, high unemployment, deflation</td><td>Boom, high inflation</td></tr>
  </table></div>
  <ul>
    <li><b>Strengths:</b> can be targeted at particular sectors or groups; can act directly on AD; spending on infrastructure and education can also raise AS.</li>
    <li><b>Limits:</b> <b>time lags</b> (recognition, decision, implementation); <b>higher debt</b> and interest costs; <b>crowding out</b> if borrowing raises interest rates; <b>imports</b> leak some of the rise in demand abroad; political pressures to avoid unpopular tax rises; uncertain effect on confidence.</li>
    <li><b>Evaluation:</b> an expansionary policy increases AD only if consumers and firms spend the extra income, and is most effective with spare capacity.</li>
  </ul>

  <h2>3 · Worked examples</h2>
  <p><b>An expansionary fiscal policy.</b> Suppose the government increases spending by $10bn and the economy has spare capacity. If households spend 70% of any extra income, the first round of spending raises incomes by $10bn, of which $7bn is spent again, creating a further $7bn of income, and so on. The total rise in income is larger than the original $10bn. (The multiplier is not required at AS, but you can use the idea that an injection raises incomes by more than the initial amount.)</p>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Initial change</th><th>Effect on AD</th><th>Budget effect</th></tr>
    <tr><td>Spending +$10bn on roads</td><td>G rises directly</td><td>AD shifts right by the whole $10bn at first, and by more as incomes are re-spent</td><td>Deficit rises by $10bn (less any extra tax revenue)</td></tr>
    <tr><td>Income tax cut of $10bn</td><td>Disposable income rises by $10bn</td><td>Only part is spent (say $7bn), so AD rises by less than the tax cut at first</td><td>Revenue falls by $10bn: deficit rises</td></tr>
    <tr><td>Spending cut of $10bn</td><td>G falls directly</td><td>AD shifts left</td><td>Deficit falls</td></tr>
  </table></div>
  <ul>
    <li>A rise in government spending has a bigger direct effect on AD than an equivalent tax cut, because some of the tax cut is <b>saved</b> or spent on <b>imports</b>.</li>
  </ul>

  <h2>4 · Why governments spend</h2>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>Examples</th></tr>
    <tr><td><b>Provide public goods</b></td><td>Defence, police, street lighting, flood defences</td></tr>
    <tr><td><b>Provide or support merit goods</b></td><td>Education, health care, vaccination programmes</td></tr>
    <tr><td><b>Redistribute income</b></td><td>Pensions, unemployment benefit, child benefit</td></tr>
    <tr><td><b>Support aggregate demand</b></td><td>Stimulus spending in a recession; automatic increases in benefits</td></tr>
    <tr><td><b>Raise productive capacity</b></td><td>Roads, ports, broadband, research and training</td></tr>
    <tr><td><b>Support industries</b></td><td>Subsidies for farming, renewable energy, new technology</td></tr>
  </table></div>

  <h2>5 · Discretionary policy and automatic stabilisers</h2>
  <ul>
    <li><b>Discretionary fiscal policy:</b> a deliberate change in taxes or spending decided by the government.</li>
    <li><b>Automatic stabilisers:</b> changes that happen without a decision: in a recession, tax revenue falls and benefit spending rises, supporting demand; in a boom, the reverse. They reduce the size of the swings in the economy.</li>
    <li><b>Time lags:</b> there are delays in recognising a problem, deciding what to do, passing laws and for the money to be spent. A policy aimed at a recession may take effect after the economy has recovered.</li>
  </ul>

  <h2>6 · Limits in more detail</h2>
  <ul>
    <li><b>Crowding out:</b> borrowing to fund a deficit may push up interest rates and reduce private investment, partly offsetting the rise in AD.</li>
    <li><b>Imports:</b> in an open economy part of the extra spending leaks abroad, so the rise in domestic output is smaller.</li>
    <li><b>Saving:</b> if households are worried about debt or taxes, they may save a tax cut rather than spend it (consumers may anticipate that taxes will rise later).</li>
    <li><b>Debt and interest costs:</b> persistent deficits add to the debt, raising the cost of servicing it. Large debts may make it hard to borrow more in the next recession.</li>
    <li><b>Spare capacity:</b> if the economy is near full capacity, extra AD mainly raises prices instead of output.</li>
    <li><b>Political constraints:</b> tax rises and spending cuts are unpopular; governments may time policies for elections rather than the economic cycle.</li>
    <li><b>Quality of spending:</b> a good return from spending on infrastructure or education is not guaranteed; poor projects may waste money.</li>
  </ul>

  <h2>7 · Fiscal policy against other policies</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Fiscal policy</th><th>Monetary policy</th><th>Supply-side policy</th></tr>
    <tr><td><b>Main tools</b></td><td>Taxes and government spending</td><td>Interest rates, money supply, credit regulation</td><td>Education, infrastructure, deregulation</td></tr>
    <tr><td><b>Who decides</b></td><td>The government</td><td>Usually the central bank</td><td>The government</td></tr>
    <tr><td><b>Speed</b></td><td>Slow to legislate; direct once spent</td><td>Quick to decide; slow to work</td><td>Very slow</td></tr>
    <tr><td><b>Targeting</b></td><td>Can be aimed at sectors or groups</td><td>Affects the whole economy</td><td>Aimed at capacity</td></tr>
    <tr><td><b>Main limit</b></td><td>Debt, lags, crowding out</td><td>Lags, confidence, zero bound</td><td>Cost and time</td></tr>
  </table></div>
  <div class="warn"><b class="h">Do not write this</b>Expansionary fiscal policy always raises output: it does so only if there is spare capacity and the extra income is spent. Do not include transfer payments in G in the AD formula. Do not forget that a bigger deficit adds to the national debt.</div>
  <div class="tip"><b class="h">Exam tip</b>Explain the <b>chain</b>: tax cut, higher disposable income, higher consumption, AD shifts right, higher output and prices. Evaluate with spare capacity, time lags and the effect on the budget and debt.</div>
'''

watch = '''
  <h2>1 · Expansionary policy in a recession</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stE"></div>
  <h2>2 · Contractionary policy when inflation is high</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Change spending and taxes</h2>
  <p>Raise or cut government spending and taxes ($bn). The AD curve shifts and the budget balance changes.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Effect on AD</small><strong id="r1"></strong></div><div><small>Real output and price level</small><strong id="r2"></strong></div><div><small>Change in budget balance</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with AD shifted by the fiscal change"></svg></div></div></div>

  <h2>Lab 2 · Which stance fits the situation?</h2>
  <p>Choose an economic situation to see which kind of fiscal policy is usually used, and the main risk.</p>
  <div class="card"><div class="grid2"><div><div id="sB" class="btnrow"></div>
    <div class="readout"><div><small>Policy stance</small><strong id="t1"></strong></div><div><small>Typical tools</small><strong id="t2"></strong></div><div><small>Main risk</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="The policy stance for the chosen situation"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Expansionary or contractionary?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a tax cut in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A stimulus package", "In a recession a government announces extra spending on infrastructure and cuts income tax. AD shifts right, output and jobs recover, but the budget deficit and the national debt rise.", "expansionary fiscal policy and its cost.") +
rw("Austerity", "To reduce a large deficit, a government cuts spending and raises taxes. AD falls, which reduces borrowing but can slow growth and raise unemployment in the short run.", "contractionary fiscal policy and its short-run cost.") +
rw("Building a rail network", "Capital spending on railways gives jobs in the short run (AD) and improves transport for firms in the long run (AS). Investment spending can therefore serve both demand and supply.", "capital expenditure raising capacity.") +
rw("A tax cut that is saved", "If households save most of a tax cut, or spend it on imports, consumption of domestic goods rises by less, so the policy does not raise AD as much as expected.", "why fiscal policy may not always raise AD.") +
rw("Stimulus spending in a recession", "A government pays for new school buildings and road repairs to support demand and jobs during a downturn. AD shifts right, but the deficit and debt rise and projects may take a long time to start.", "expansionary fiscal policy, the budget and time lags.") +
rw("Austerity", "A government with a large deficit cuts spending and raises taxes. The deficit falls, but AD shifts left, which may reduce growth and raise unemployment in the short run.", "contractionary fiscal policy and its costs.")
)

mc_exam = [
  mcq("m20_12", 29, "What is an example of fiscal policy aimed at increasing aggregate demand in an economy?", ["increasing expenditure by firms on skills training programmes for unskilled workers", "increasing the commercial banks' lending ability", "reducing the rate of income tax for all income earners", "reducing the rate of interest on loans to manufacturing companies"], 2, "A lower rate of income tax is a fiscal policy measure that raises disposable income and spending. The others are firm spending or monetary policy."),
  mcq("m23_12", 28, "What is least likely to rise as a result of the use of expansionary fiscal policy?", ["aggregate demand", "budget surplus", "nominal income", "inflation"], 1, "Higher spending or lower taxes reduce a surplus (or raise the deficit)."),
  mcq("s24_11", 22, "What is most likely to decrease if a government uses expansionary fiscal policy?", ["a balance of payments deficit", "cyclical unemployment", "the level of wages", "the rate of inflation"], 1, "Higher AD creates jobs and reduces cyclical unemployment."),
  mcq("m25_12", 22, "Which combination of fiscal policy measures will reduce both the inflation rate and income inequality? (subsidies on food and public transport, direct taxes, indirect taxes)", ["decrease, decrease, increase", "decrease, increase, increase", "increase, decrease, increase", "increase, increase, decrease"], 3, "Higher direct taxes and lower indirect taxes cut AD (lower inflation) and are progressive, while higher subsidies help the poor."),
  mcq("s20_13", 29, "Which combination of fiscal and monetary policies is most likely to be effective in the short run for tackling deflation in a closed economy? (fiscal policy, monetary policy)", ["decreasing the budget deficit, decreasing the interest rate", "decreasing the budget deficit, decreasing the money supply", "increasing the budget deficit, decreasing the interest rate", "increasing the budget deficit, decreasing the money supply"], 2, "A bigger deficit and a lower interest rate both raise AD and so counter deflation."),
  mcq("s21_12", 30, "Which policy will not cause a reduction in the rate of inflation?", ["increasing income tax", "reducing government spending", "reducing interest rates", "removing subsidies"], 2, "Lower interest rates raise AD. The other policies are contractionary or raise costs."),
  mcq("s20_12", 28, "Which combination correctly classifies an expansionary fiscal measure and its impact on a budget deficit? (fiscal policy, budget deficit)", ["increased quantitative easing, unchanged", "increased welfare spending, increased", "lower income tax, reduced", "lower interest rates, unchanged"], 1, "Higher welfare spending is fiscal and raises the deficit. Quantitative easing and interest rates are monetary policy, and a lower income tax would raise the deficit."),
  mcq("s21_13", 17, "A government decides to build additional public sector housing to be rented to people receiving low incomes. What is most likely to fall as a result of this increase in public sector housing?", ["employment in the construction industry", "land prices in towns and cities", "rents of houses in the private sector", "total government spending"], 2, "More public rental housing increases supply of rented homes and lowers private sector rents.")
]

exam = exam_page("government spending and fiscal policy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Fiscal policy is an 8 or 12 mark part nearly every series: expansionary policy and AD, whether it always benefits an economy, and whether it is the best way to deal with inflation or deflation. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "Feb/March 2025 (22) Q5(a)"), ("Essay parts, 12 marks", "5", "May/June 2025 (21) Q5(b); Oct/Nov 2024 (21) Q5(b); Feb/March 2022 (22) Q3(b); May/June 2025 (22) Q4(b); May/June 2021 (22) Q4(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("m25_22", "5(a)"), "8 marks", "With the help of an AD/AS diagram, explain what is meant by an expansionary fiscal policy and consider the extent to which an expansionary fiscal policy will always increase the level of aggregate demand.",
     ["Knowledge (up to 3): expansionary fiscal policy is an increase in government spending and/or a reduction in tax rates (1); aggregate demand is the total demand for an economy's goods and services at a given price level, or C + I + G + (X − M) (1); an accurate diagram showing AD and AS curves (1).",
      "Analysis (up to 3): an explanation of how a decrease in income tax, for example, increases disposable income (1), which increases consumption and so aggregate demand (1); a diagram showing a rightward shift of the AD curve (1).",
      "Evaluation (up to 2): an explanation of whether expansionary fiscal policy will increase AD (1) and a justified conclusion (1)."],
     "Define expansionary policy and AD. Tax cut: more disposable income, more consumption, AD right, with diagram. Evaluate: savings, imports, confidence.",
     [[("k", "Expansionary fiscal policy is a rise in government spending or a cut in taxes. Aggregate demand is total spending on an economy's output, C + I + G + (X − M). The diagram shows AD and SRAS meeting at the initial price level and output.")], [("n", "A cut in income tax raises households' disposable income, so consumption rises, and as consumption is a component of AD the AD curve shifts to the right, raising real output and the price level.")], [("e", "AD will not always rise by as much as expected. Households may save the tax cut or spend it on imports, and higher government borrowing could raise interest rates and crowd out private spending. The effect is largest when there is spare capacity and consumers are confident.")]]),
  eq(P("s25_21", "5(b)"), "12 marks", "Assess whether expansionary fiscal policy always benefits an economy.",
     ["Analysis (up to 8): the benefits, such as a rise in AD, real output and employment, and a fall in cyclical unemployment, with a diagram (up to 4); the costs and limits, such as a higher budget deficit and national debt, inflation near full capacity, crowding out, imports and time lags (up to 4).",
      "Evaluation (up to 4): a judgement on whether expansionary policy always benefits the economy, depending on spare capacity, the size and type of spending and the level of debt, with a conclusion."],
     "Benefits: AD, output, jobs. Costs: deficit, debt, inflation, crowding out, time lags. Judge: depends on spare capacity and debt.",
     [[('n', 'Expansionary fiscal policy involves higher government spending, lower taxes or both. This raises AD, so with the AD curve shifting right, real output increases, firms need more workers and cyclical unemployment falls. The multiplier means that the final increase in income is greater than the initial injection. In a recession with spare capacity, the policy may raise output with little effect on prices, so the economy benefits, and tax revenue rises as incomes grow, so the net cost may be smaller than first thought.')], [('n', 'However, there are costs. Spending more or taxing less increases the budget deficit and the national debt, which has to be repaid, so future taxes may rise, and interest payments take a larger share of spending. If the economy is near full capacity, the rise in AD mainly raises prices instead of output, so there is inflation. Borrowing may crowd out private investment by raising interest rates. Some of the extra demand leaks abroad as imports, particularly in an open economy, worsening the current account, and time lags in deciding and carrying out the policy mean it may take effect when the economy has already recovered.')], [('e', 'Expansionary policy does not always benefit an economy. It is most likely to benefit it when there is a large negative output gap, when the multiplier is high, when government debt is low and when the money is spent on projects that also raise AS, such as infrastructure. It is less beneficial when the economy is near full employment or when debt is already high.'), ('e', 'So expansionary fiscal policy is likely to benefit an economy in a recession, but not always, and the benefits depend on spare capacity, the size and type of spending, and the effect on the deficit.')]]),
  eq(P("w24_21", "5(b)"), "12 marks", "Assess whether a government should always aim for an expansionary fiscal policy rather than a contractionary fiscal policy.",
     ["Analysis (up to 8): the case for expansionary policy: raises AD, output and employment, useful in a recession (up to 4); the case for contractionary policy: reduces inflation and the budget deficit and debt (up to 4).",
      "Evaluation (up to 4): a judgement, depending on the economic situation (recession or boom), inflation, unemployment and debt, with a conclusion that neither should be used always."],
     "Expansionary: recession, jobs. Contractionary: inflation, debt. Judge: depends on the stage of the cycle and the objectives.",
     [[('n', 'Expansionary fiscal policy raises government spending or cuts taxes, so AD shifts right. In a recession with a negative output gap, this raises real output and employment and, with the multiplier, helps the economy recover. Tax revenue rises as incomes grow and the cost of unemployment benefits falls. Contractionary fiscal policy cuts spending or raises taxes, so AD shifts left. It reduces demand-pull inflation, lowers the budget deficit and national debt, and may create room for future borrowing, so it is useful in a boom or when debt is high.')], [('n', 'Both have costs. Expansionary policy adds to the deficit and debt, may crowd out private investment, and could cause inflation if used near full capacity. It also takes time to work and may be hard to reverse. Contractionary policy slows growth, may raise unemployment and reduce spending on public services, which could harm the poorest, and can be politically unpopular. If used during a recession, it could deepen the downturn.')], [('e', 'A government should not always choose expansion. The right policy depends on where the economy is in the cycle, on inflation and unemployment, and on the level of debt. Expansion suits a recession with spare capacity and low debt; contraction suits an overheating economy with high inflation or very high debt. In the long run, a government needs to balance the budget over the economic cycle.'), ('e', 'Overall, neither should always be chosen: a government should aim for expansionary policy when output is below capacity and contractionary policy when AD is too high, so the choice depends on conditions.')]]),
  eq(P("m22_22", "3(b)"), "12 marks", "Discuss the ways in which fiscal policy can be used to increase the aggregate supply of products in an economy and consider whether this approach is likely to be effective.",
     ["Analysis (up to 8): ways fiscal policy can raise AS, such as capital spending on infrastructure, spending on education, training and health, tax incentives for investment and research, lower income tax to encourage work, and subsidies for technology (up to 4 for explaining ways, up to 4 for how each raises AS).",
      "Evaluation (up to 4): whether the approach is likely to be effective: time lags, cost and opportunity cost, uncertainty about returns, the possibility of crowding out, the need for matching AD, with a conclusion."],
     "Ways: infrastructure, education, tax incentives. Effect: shifts LRAS right. Limits: time lags, cost, uncertain return.",
     [[('k', 'Fiscal policy uses government spending and taxation. It can be used to increase aggregate supply by raising the productive capacity of the economy, shifting LRAS to the right.')], [('n', "Capital spending on infrastructure, such as roads, railways and broadband, lowers firms' costs and makes them more productive, which encourages private investment. Spending on education, training and health care raises the skills and productivity of labour and means workers are available for more of the time. Tax incentives for investment and research encourage firms to buy machinery and develop new products, raising capacity. Subsidies for technology help firms adopt new methods. Lower income taxes may increase the incentive to work or to be self-employed, raising the labour supply. Each shifts LRAS to the right, raising potential output and growth without inflation.")], [('e', 'However, the approach may not be fully effective. These policies take years to work, so the benefit is far in the future, and training may not match the skills firms need. They cost money and have an opportunity cost, and if financed by borrowing could crowd out private investment. The returns are uncertain: tax cuts may not raise work effort, and subsidies may be wasted. Spending also adds to AD in the short run, which could raise prices if the economy is near full capacity.'), ('e', 'Overall, fiscal policy is likely to be effective in raising aggregate supply in the long run if it is well targeted, particularly on infrastructure and education, but it is not a quick solution and its success depends on design, cost and the state of the economy.')]]),
  eq(P("s25_22", "4(b)"), "12 marks", "Assess the extent to which using fiscal policy would be the best way to reduce a high rate of inflation.",
     ["Analysis (up to 8): fiscal policy involves raising taxation and reducing government spending; the advantages include being relatively quick and effective, particularly against demand-pull inflation; the disadvantages include reducing economic growth, possibly causing unemployment, and being less effective if the main cause is cost-push inflation; these must be analysed against an alternative policy, likely to be supply-side or monetary, with a focus on its likely success in reducing a high rather than a low or sustainable rate of inflation.",
      "Evaluation (up to 4): a clear comparison of fiscal policy with at least one other policy and a justified conclusion as to which is best."],
     "Fiscal: tax up, spending down, AD left; effective for demand-pull, costs growth and jobs, weak for cost-push. Alternative: monetary or supply-side. Judge by cause.",
     [[('k', "Contractionary fiscal policy means raising taxes or reducing government spending to reduce AD. A high rate of inflation is a rapid sustained rise in the price level, which causes problems for savers, firms and the economy's competitiveness.")], [('n', 'Higher taxes reduce disposable income and cuts in government spending reduce AD directly, so AD shifts left and demand-pull inflation falls. Fiscal policy can be targeted at particular sectors, and it also reduces the budget deficit. It acts relatively quickly on demand once passed, although legislation takes time. However, it reduces output and employment, so growth slows and unemployment may rise, and cuts in spending may hit the poor and public services. It does little against cost-push inflation, where the cause is higher costs on the supply side, so lower AD would reduce output without removing the pressure on costs.')], [('n', 'Alternatives include contractionary monetary policy, with higher interest rates, which also lowers AD. Interest rate changes can be made quickly by an independent central bank, and they are less affected by politics, but they work with a lag of up to 18 months and affect borrowers most. Supply-side policy, such as training and deregulation, addresses cost-push inflation by lowering costs and raising capacity, but takes years to work.'), ('e', 'Fiscal policy is unlikely to be the best way to reduce a high rate of inflation in every case. It is effective against demand-pull inflation and when the budget deficit is large, but not against cost-push inflation, and it has costs for growth and jobs. Monetary policy is likely to be quicker to implement, though similar in its effects, so a combination may work best, with supply-side policy for the long term. The best policy depends on the cause of the inflation.')]]),
  eq(P("s21_22", "4(b)"), "12 marks", "Discuss whether a government should use monetary policy or fiscal policy to solve the problem of deflation in an economy.",
     ["Analysis (up to 8): how monetary policy can stimulate aggregate demand, with its strengths and weaknesses (up to 4; a maximum of 3 if only strengths or only weaknesses); how fiscal policy can stimulate aggregate demand, with its strengths and weaknesses (up to 4; a maximum of 3 if one-sided).",
      "Evaluation (up to 4): a clear comparison of the use of each policy to solve deflation (up to 3) leading to a reasoned conclusion as to which may be the most appropriate (1). No knowledge marks for merely defining terms in the question."],
     "Monetary: lower rates, more credit; quick to decide, limited if rates near zero or confidence low. Fiscal: higher spending, tax cuts; direct, but debt and lags. Judge.",
     [[('k', 'Deflation is a sustained fall in the general price level. It is a problem because consumers may delay spending in the hope of lower prices, so AD falls, output and employment fall and debts become harder to repay.')], [('n', 'Monetary policy can stimulate AD by cutting interest rates and increasing the money supply, for example through quantitative easing. Borrowing is cheaper, so consumption and investment rise and savings pay less, and a lower exchange rate could raise exports. Interest rates can be changed quickly by an independent central bank, and the policy is less affected by politics. But in deflation, consumers and firms expect prices to fall and may not borrow, banks may not lend, and rates may already be near zero, so the policy can be ineffective, as in a liquidity trap. It also works with a lag.')], [('n', 'Fiscal policy can raise government spending or cut taxes, which adds to AD directly. Spending can be targeted at projects that create jobs, and it can be effective when the central bank has no room to cut rates. The multiplier raises the effect, and it does not depend on banks lending. But it increases the budget deficit and debt, takes time to plan and implement, may crowd out private spending, and consumers may save tax cuts instead of spending them.'), ('e', 'In a deflation caused by weak demand, fiscal policy may be more effective than monetary policy if interest rates are already close to zero, because it works directly on spending. Monetary policy is quicker and cheaper if there is room to cut rates. The best choice depends on the level of interest rates, the size of the deficit and debt, and the causes of the deflation. Overall, a government is likely to need both, with monetary policy used first and fiscal policy where monetary policy has run out of scope.')]])
  ],
  )

tips = tips_html(
  [("Define expansionary and contractionary.", "Spending up or taxes down; spending down or taxes up."),
   ("Show the chain.", "Tax cut, income, consumption, AD, output."),
   ("Use an AD/AS diagram.", "Right shift for expansionary, left for contractionary."),
   ("Say when each is used.", "Recession versus inflation."),
   ("Evaluate with spare capacity.", "Output rises most if there is spare capacity."),
   ("Mention limits.", "Time lags, debt, crowding out, imports."),
   ("Capital spending can raise AS.", "Infrastructure, education.")],
  [("Fiscal policy", "Fiscal policy uses government spending and taxation to influence the economy."),
   ("Capital spending", "Capital expenditure adds to productive capacity."),
   ("Expansionary", "Expansionary fiscal policy shifts AD to the right."),
   ("Contractionary", "Contractionary fiscal policy can reduce inflationary pressure."),
   ("Evaluation", "The impact depends on spare capacity, time lags and the level of debt.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- spending composition ---------- */
function spDraw(s) {
  const Y = (v) => 250 - v * 3; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "% of government spending", "sm");
  const parts = [["Transfer payments", 35, "f1"], ["Current spending (wages, running costs)", 45, "f2"], ["Capital spending", 20, "f3"]]; let y = 250;
  parts.forEach(([n, v, c], i) => { const k = Math.max(0, Math.min(1, s.k - i)); if (k > 0) { const h = v * 3 * k; o += SV.rect(240, y - h, 170, h, c, op(0.65)) + SV.text(325, y - h / 2 + 5, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(430, y - h / 2 + 5, n, "sm"); y -= h; } });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Government spending split into transfer payments, current spending and capital spending">${spDraw({ k: 3 })}</svg>`;
function fpDraw(s) { return adasPlot({ a: s.a, s: 0, l: s.l, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Expansionary fiscal policy shifts AD to the right">${fpDraw({ a: 20, l: 0, n: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Expansionary fiscal policy in a recession", base: { a: 0, l: 0, n: 0 }, draw: fpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A recession.</b> Equilibrium output (50) is well below potential output (75): spare capacity and cyclical unemployment.", s: { a: 0, l: 0, n: 0 } },
  { cap: "<b>The government cuts income tax and raises spending.</b> Disposable income and demand rise: AD shifts <b>right</b>. Real output rises towards potential and employment rises, with only a modest rise in the price level.", s: { a: 20, l: 0, n: 1 } },
  { cap: "<b>The cost.</b> The budget deficit and the national debt rise, and some of the extra spending leaks abroad as imports.", s: { a: 20, l: 0, n: 1 } },
] });
function cpDraw(s) { return adasPlot({ a: s.a, s: 0, l: -15, g: 1, n: s.n }); }
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary fiscal policy when the economy is overheating", base: { a: 25, n: 0 }, draw: cpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A boom.</b> AD has risen so that output (about 62) is above the sustainable level (the LRAS at 60) and prices are rising: an inflationary gap.", s: { a: 25, n: 0 } },
  { cap: "<b>The government raises taxes and cuts spending.</b> AD shifts <b>left</b>: output falls back to the sustainable level and the price level falls, reducing inflation.", s: { a: 8, n: 1 } },
  { cap: "<b>The cost.</b> Slower growth and some unemployment in the short run, but a smaller deficit.", s: { a: 8, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!["dg", "dt"].every((i) => $("#" + i))) return;
  const g = +$("#dg").value, t = +$("#dt").value, a = Math.max(-30, Math.min(40, 1.0 * g - 0.6 * t)), e = sdEq(a, 0), e0 = sdEq(0, 0), bal = -(g) + t;
  $("#r1").textContent = Math.abs(a) < 0.5 ? "No change" : a > 0 ? "Shifts right" : "Shifts left"; $("#r2").textContent = "Y " + Lib.fmtN(e.q, 1) + ", P " + Lib.fmtN(e.p, 1); $("#r3").textContent = (bal >= 0 ? "+" : "−") + "$" + Math.abs(bal) + "bn";
  $("#rv").textContent = Math.abs(a) < 0.5 ? "The changes offset each other (or are zero), so AD does not shift." : `${g > 0 ? "Spending rises by $" + g + "bn. " : g < 0 ? "Spending falls by $" + -g + "bn. " : ""}${t > 0 ? "Taxes rise by $" + t + "bn. " : t < 0 ? "Taxes fall by $" + -t + "bn. " : ""}AD shifts ${a > 0 ? "right (expansionary)" : "left (contractionary)"}: real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. The budget balance moves by ${bal >= 0 ? "+" : "−"}$${Math.abs(bal)}bn (before any change in tax revenue caused by the new output). (Government spending changes AD fully; a tax change affects it by less, because some of the extra income is saved.)`;
  $("#labA").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "dg", label: "Change in government spending, $bn ", min: -20, max: 30, step: 5, value: 20, fmt: (v) => v, onInput: labF });
Lib.slider($("#g2"), { id: "dt", label: "Change in taxes, $bn ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
const SIT = [["A deep recession with high unemployment", "Expansionary", "Raise spending, cut taxes", "Higher deficit and debt", "AD is far below capacity, so a boost to demand raises output and jobs with little inflation."], ["A boom with rising inflation", "Contractionary", "Cut spending, raise taxes", "Slower growth, rising unemployment", "AD is above capacity, so reducing it lowers inflation."], ["Deflation and falling spending", "Expansionary", "Tax cuts, infrastructure spending", "May not raise confidence", "More spending counters falling prices and demand."], ["A large budget deficit and high debt, steady growth", "Contractionary", "Gradual spending cuts, tax rises", "May slow growth", "The aim is to reduce borrowing and debt over time."], ["Weak growth but low spare capacity", "Supply-side focused", "Spending on education and infrastructure", "Takes years to work", "Capital spending raises productive capacity (LRAS), not only AD."]];
function showS(i) {
  const [n, st, tl, rk, why] = SIT[i]; $$("#sB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = st; $("#t2").textContent = tl; $("#t3").textContent = rk; $("#tv").textContent = `${n}: ${why}`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, st === "Expansionary" ? "f2" : st === "Contractionary" ? "f3" : "f1", { rx: 12, ...op(0.45) }) + SV.text(210, 105, st, "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(210, 170, tl, "sm", { "text-anchor": "middle" });
}
$("#sB").innerHTML = SIT.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
$$("#sB button").forEach((b) => (b.onclick = () => showS(+b.dataset.i)));
showS(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Expansionary or contractionary fiscal policy?", ["Expansionary", "Contractionary"],
  [("A cut in income tax", 0), ("Higher government spending on roads", 0), ("A rise in VAT", 1), ("Cutting public sector spending", 1), ("A tax rise to reduce the deficit", 1), ("Increasing welfare payments", 0), ("A government stimulus package", 0), ("Reducing a budget deficit to curb inflation", 1)],
  "Expansionary: more spending or lower taxes. Contractionary: less spending or higher taxes.") + MATCH([
  ["Fiscal policy", "Use of government spending and taxation"],
  ["Capital expenditure", "Spending on lasting assets such as roads"],
  ["Current expenditure", "Day-to-day spending such as wages"],
  ["Expansionary fiscal policy", "Raises AD through higher spending or lower taxes"],
  ["Crowding out", "Government borrowing reduces private spending"],
  ["Time lag", "Delay between a problem and the effect of a policy"]]) + ORDER(
  "Put the effect of a cut in income tax in order.",
  ["The government cuts income tax", "Disposable income rises", "Consumption rises", "AD shifts to the right", "Real output and employment rise"],
  "Tax cut raises spending and AD.") + CALC([
  {"q": "Government spending is $500bn, of which $90bn is capital spending. What share is capital spending (%)?", "a": 18, "unit": "%", "tol": 0.1, "hint": "90 ÷ 500.", "sol": "<b>18%</b>."},
  {"q": "Spending rises by $20bn and taxes are unchanged. What is the change in the budget balance ($bn)?", "a": -20, "unit": "$bn", "tol": 0.5, "hint": "More spending, same revenue.", "sol": "<b>−$20bn</b>: the deficit rises."},
  {"q": "A tax cut of $10bn raises consumption by $6bn (the rest is saved). By how much does AD rise at first ($bn)?", "a": 6, "unit": "$bn", "tol": 0.1, "hint": "Only the spent part.", "sol": "<b>$6bn</b>."},
  {"q": "Real GDP is $800bn and rises 2.5% after a stimulus. What is the new real GDP ($bn)?", "a": 820, "unit": "$bn", "tol": 0.5, "hint": "800 × 1.025.", "sol": "<b>$820bn</b>."}]) + MCQ([
  ("Which is an expansionary fiscal measure?", ["A cut in income tax", "A rise in interest rates", "A cut in government spending", "A rise in VAT"], 0, "Lower taxes raise AD."),
  ("Contractionary fiscal policy would be used to:", ["Reduce inflation", "Reduce unemployment", "Raise AD", "Raise the deficit"], 0, "It lowers AD."),
  ("Capital expenditure is:", ["Spending on lasting assets", "Spending on wages", "Benefits", "Interest on debt"], 0, "Roads, schools, hospitals."),
  ("A limit of fiscal policy is:", ["Time lags", "Always works immediately", "No effect on the deficit", "Lowers debt always"], 0, "Delays."),
  ("Expansionary fiscal policy most likely:", ["Raises the budget deficit", "Cuts the national debt", "Reduces AD", "Raises unemployment"], 0, "More spending, less tax.")
], "qz1") + CARDS([
  ("Fiscal policy", "Spending and taxes."),
  ("Expansionary", "AD right."),
  ("Contractionary", "AD left."),
  ("Capital spending", "Raises capacity."),
  ("Current spending", "Day-to-day."),
  ("Use in recession", "Expansionary."),
  ("Use in boom", "Contractionary."),
  ("Limits", "Lags, debt, crowding out.")]) + MCQ(mc_exam)

build("as53", "as-fiscal-policy", "Government Spending and Fiscal Policy", EY,
  "5.2.5 to 5.2.7: current and capital government spending, expansionary and contractionary fiscal policy, and AD/AS analysis of their effects. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
