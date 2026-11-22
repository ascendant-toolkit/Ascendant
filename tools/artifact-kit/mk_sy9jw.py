"""Resource: the injections and withdrawals (J and W) diagram explained (9.1.1, 9.1.3; coursebook Figure 9.16). Run: python3 tools/artifact-kit/mk_sy9jw.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.1 · Explainer"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">injections and withdrawals (J and W) diagram</b> plots <b>injections J = I + G + X</b> and <b>withdrawals W = S + T + M</b> against national income. <b>J is a horizontal line</b> because injections are assumed not to depend on domestic income, and <b>W slopes upwards</b> because saving, taxes and imports all rise with income. <b>Equilibrium is where J = W</b>: if J is greater than W, spending is being added faster than it leaks out, so income rises, and if W is greater than J, income falls. A change in injections shifts the J line, and national income changes by the <b>multiplier</b> times the shift, which is why the horizontal distance between the two equilibria is larger than the vertical shift.</p></div>

  <h2>1 · What the diagram shows</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Horizontal axis: national income, Y.</b> The same income, output and expenditure measure as on the 45° diagram.</li>
    <li><b>Vertical axis: injections and withdrawals (J and W).</b> Both are flows of money per year, in the same units as income.</li>
    <li><b>J</b> is the horizontal line. <b>J1</b> in the textbook figure is a higher horizontal line after a rise in injections.</li>
    <li><b>W</b> is the upward-sloping line. Notice that it <b>starts below the horizontal axis</b>. The next two sections explain why.</li>
    <li><b>Y and Y1</b> are the equilibrium incomes where W crosses J and J1.</li>
  </ul>
  <div class="tip"><b class="h">Where this fits</b>This is the leakages and injections approach to national income. The 45° (Keynesian cross) diagram gives the same equilibrium from the expenditure side. Both are in the syllabus under 9.1.1, and a question may name either one, so you need to be able to draw both.</div>

  <h2>2 · Building the lines</h2>
  <div class="grid2">
    <div class="card"><h3>Injections: J = I + G + X</h3><ul>
      <li><b>I</b> investment by firms in capital goods</li>
      <li><b>G</b> government spending on goods and services</li>
      <li><b>X</b> exports, spending by foreigners on the country's output</li>
    </ul>
    <p>Each is assumed to be decided by factors other than <b>domestic</b> income: interest rates and expected profit (I), government policy (G), and foreign incomes and competitiveness (X). So J is <b>autonomous</b>, which is why the line is flat.</p></div>
    <div class="card"><h3>Withdrawals: W = S + T + M</h3><ul>
      <li><b>S</b> saving, income not spent</li>
      <li><b>T</b> taxes, which take income out of the flow (net of government transfers)</li>
      <li><b>M</b> imports, spending that leaves the domestic economy</li>
    </ul>
    <p>All three rise as income rises, so W slopes <b>upward</b>. Its slope is the <b>marginal propensity to withdraw</b>: MPW = MPS + MRT + MPM.</p></div>
  </div>
  <p>Throughout this page the numbers are: <b>I = 100, G = 70, X = 30</b>, so <b>J = 200</b>. <b>S = −50 + 0.1Y, T = 0.25Y, M = 0.15Y</b>, so <b>W = −50 + 0.5Y</b>. The MPW is 0.1 + 0.25 + 0.15 = 0.5.</p>
  <div class="tw"><table class="t">
    <tr><th>Income Y</th><th>S = −50 + 0.1Y</th><th>T = 0.25Y</th><th>M = 0.15Y</th><th>W (total)</th><th>J</th><th>Net injection (J − W)</th></tr>
    <tr><td>0</td><td>−50</td><td>0</td><td>0</td><td>−50</td><td>200</td><td>+250</td></tr>
    <tr><td>300</td><td>−20</td><td>75</td><td>45</td><td>100</td><td>200</td><td>+100</td></tr>
    <tr><td><b>500</b></td><td>0</td><td>125</td><td>75</td><td><b>200</b></td><td><b>200</b></td><td><b>0</b></td></tr>
    <tr><td>700</td><td>20</td><td>175</td><td>105</td><td>300</td><td>200</td><td>−100</td></tr>
  </table></div>

  <h2>3 · Why does W start below zero?</h2>
  <p>This is the feature of the textbook figure that is easy to miss. At zero income there are <b>no taxes and no imports</b>, because both are a share of income. But households still need to spend, so they <b>draw on past savings or borrow</b>. That is <b>dissaving</b>, negative saving. It is the <b>autonomous</b> part of the saving function, S = −a + sY (the mirror image of the consumption function C = a + cY).</p>
  <ul>
    <li>With <b>a = 50</b>, W is <b>−50</b> where the line meets the vertical axis.</li>
    <li>The line crosses the horizontal axis at <b>Y = 100</b> (where 0.5Y = 50). Below that income, withdrawals are negative: households dissave by more than taxes and imports take out.</li>
    <li>A W line drawn from the <b>origin</b> assumes there is no autonomous dissaving, which is a common simplification. A negative intercept is more accurate and matches the consumption function.</li>
  </ul>

  <h2>4 · Equilibrium, and why it is stable</h2>
  <p>Equilibrium national income is where <b>J = W</b>. With J = 200: 200 = −50 + 0.5Y, so <b>Y = 500</b>.</p>
  <ul>
    <li><b>Below equilibrium (Y = 300):</b> J = 200 but W = 100. There is a <b>net injection of 100</b>: more money is being put into the circular flow than leaves it. Firms sell more than they planned, stocks fall, output and incomes rise, and as income rises W rises with it, until it reaches J.</li>
    <li><b>Above equilibrium (Y = 700):</b> W = 300 is greater than J = 200, a <b>net withdrawal of 100</b>. Spending falls short of output, stocks build up, firms cut production and income falls until W comes back to J.</li>
  </ul>
  <p>Notice that <b>planned</b> injections and withdrawals are only equal at equilibrium. In the national accounts, after the event, they are always equal because any difference shows up as unplanned changes in stocks.</p>

  <h2>5 · A rise in injections: J to J1</h2>
  <p>Suppose the government raises spending by 50, so <b>J rises from 200 to 250</b>. J1 is a higher horizontal line.</p>
  <ul>
    <li>At the old equilibrium (500) the new J1 is 250 but W is still 200, so there is a <b>net injection of 50</b>.</li>
    <li>Income rises. For every 1 of extra income, W rises by 0.5 (the MPW), so W only catches up with J1 when income has risen by 50 ÷ 0.5 = <b>100</b>.</li>
    <li>The new equilibrium is <b>Y1 = 600</b>, where −50 + 0.5Y = 250.</li>
  </ul>
  <div class="formula">ΔY = ΔJ ÷ MPW = ΔJ × k, where k = 1 ÷ MPW = 1 ÷ (MPS + MRT + MPM)</div>
  <p>Here k = 1 ÷ 0.5 = 2, so 50 × 2 = 100. On the diagram the <b>vertical</b> shift of J is 50, and the <b>horizontal</b> distance between Y and Y1 is 100. The slope of W tells you the multiplier: <b>a flatter W means a larger multiplier</b>, because withdrawals take longer to catch up with the new injections. A fall in injections is the same in reverse: J shifts down and income falls by a multiple. The negative intercept does <b>not</b> change the multiplier, only the level of income.</p>

  <h2>6 · Changes in withdrawals</h2>
  <div class="grid2">
    <div class="card"><h3>A shift of W (a change in the intercept)</h3>
      <p>A change in <b>autonomous</b> saving, taxes or imports moves the line up or down in parallel. For example, if households become more cautious, autonomous dissaving falls from 50 to 30, so W shifts <b>up</b> by 20 (it is now −30 + 0.5Y). Equilibrium falls to (200 + 30) ÷ 0.5 = <b>460</b>, a fall of 40, which is 20 × 2.</p>
      <p>A shift <b>down</b> would raise income.</p></div>
    <div class="card"><h3>A rotation of W (a change in the slope)</h3>
      <p>A change in the <b>marginal</b> propensities changes the steepness. For example, a rise in the marginal rate of income tax from 0.25 to 0.35 raises MPW from 0.5 to 0.6, so W is <b>steeper</b>, pivoting around its intercept (−50). Equilibrium falls to 250 ÷ 0.6 ≈ <b>417</b>, and the multiplier falls from 2 to 1.67.</p>
      <p>A <b>flatter</b> W (for instance a lower MPM after import substitution) raises both income and the multiplier.</p></div>
  </div>
  <div class="tw"><table class="t">
    <tr><th>Event</th><th>Line that changes</th><th>Equilibrium income</th></tr>
    <tr><td>Government spending rises</td><td>J shifts up</td><td>Rises by ΔJ × k</td></tr>
    <tr><td>Exports fall after a recession abroad</td><td>J shifts down</td><td>Falls by ΔJ × k</td></tr>
    <tr><td>Interest rates fall, so investment rises</td><td>J shifts up</td><td>Rises</td></tr>
    <tr><td>Households raise autonomous saving</td><td>W shifts up</td><td>Falls</td></tr>
    <tr><td>Marginal rate of tax rises</td><td>W becomes steeper</td><td>Falls, and the multiplier falls</td></tr>
    <tr><td>Marginal propensity to import falls</td><td>W becomes flatter</td><td>Rises, and the multiplier rises</td></tr>
    <tr><td>Income rises because J rose</td><td>Neither line moves: movement along W</td><td>The result, not a cause</td></tr>
  </table></div>

  <h2>7 · Full employment and the gaps on this diagram</h2>
  <p>Mark the <b>full employment level of income</b>, YF, on the horizontal axis and compare J and W <b>at YF</b>.</p>
  <ul>
    <li><b>W is above J at YF: a deflationary gap.</b> Equilibrium is below YF. The <b>vertical distance between W and J at YF</b> is the shortfall in injections. With YF = 600, W = 250 and J = 200, so the gap is 50, which is exactly the rise in J that moves equilibrium to 600.</li>
    <li><b>J is above W at YF: an inflationary gap.</b> Equilibrium would be above YF, but real output cannot exceed YF, so the excess demand pulls up prices. With YF = 400, W = 150 and J = 200, the gap is 50 and a <b>fall in J of 50</b> would close it.</li>
  </ul>
  <div class="tip"><b class="h">Same gap as on the 45° diagram</b>The vertical gap between W and J at YF has exactly the same size as the vertical gap between the AE line and the 45° line at YF. The two diagrams are two views of the same economy. The required change in injections is the gap, and the change in income is the gap times the multiplier.</div>

  <h2>8 · J and W compared with the 45° diagram</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>45° (expenditure) diagram</th><th>Injections and withdrawals diagram</th></tr>
    <tr><td><b>Vertical axis</b></td><td>Aggregate expenditure, AE</td><td>Injections J and withdrawals W</td></tr>
    <tr><td><b>Equilibrium</b></td><td>AE = Y (AE line crosses the 45° line)</td><td>J = W (the lines cross)</td></tr>
    <tr><td><b>Autonomous items</b></td><td>The AE line's intercept is autonomous spending (positive)</td><td>J is a flat line. W has a negative intercept (autonomous dissaving).</td></tr>
    <tr><td><b>Slope</b></td><td>AE slope = 1 − MPW (share of extra income spent at home)</td><td>W slope = MPW (share of extra income that leaks)</td></tr>
    <tr><td><b>Gap at full employment</b></td><td>Vertical distance between AE and the 45° line at YF</td><td>Vertical distance between W and J at YF</td></tr>
    <tr><td><b>Multiplier</b></td><td>1 ÷ (1 − slope of AE)</td><td>1 ÷ slope of W</td></tr>
    <tr><td><b>Best for showing</b></td><td>Components of expenditure (C, I, G, X − M)</td><td>The leakages and injections and the multiplier</td></tr>
  </table></div>

  <h2>9 · Related ideas</h2>
  <h3>The paradox of thrift</h3>
  <p>If households try to save more, W shifts up. In a closed economy without a government, equilibrium needs saving to equal investment (S = I), and J (= I) has not changed. So income falls until saving is back to the original level: <b>everyone tries to save more, but total saving does not rise</b> and income is lower. This is a Keynesian result and it depends on there being spare capacity.</p>
  <h3>Net injection and the multiplier rounds</h3>
  <p>The net injection at the old equilibrium (50 in section 5) is the first round of extra spending. Each round of income creates a smaller net injection, until the net injection is zero. The multiplier is the total of all the rounds.</p>
  <h3>Taxes and transfers</h3>
  <p>Strictly, taxes are net of transfer payments (pensions, benefits), which add to income. Benefits that rise in a recession make W lower than it would otherwise be, which is part of why automatic stabilisers help.</p>
  <h3>Opening the economy</h3>
  <p>Adding imports (M) makes W steeper and the multiplier smaller. Adding exports (X) raises J. This is why a country that opens to trade has a smaller multiplier but gains a new injection.</p>

  <h2>10 · What the model assumes</h2>
  <ul>
    <li><b>Injections are autonomous</b>, so J is flat. In reality, investment also depends on income (the accelerator), so J could slope upwards.</li>
    <li><b>The price level is fixed</b>. Near full employment, extra demand may raise prices instead of output.</li>
    <li><b>Withdrawals are a stable share of income</b>, so the slope of W is constant. The propensities change over time, so the multiplier is only an estimate.</li>
    <li><b>The adjustment takes time</b>, which the diagram does not show.</li>
  </ul>

  <h2>11 · Common mistakes</h2>
  <div class="tw"><table class="t">
    <tr><th>Mistake</th><th>Fix</th></tr>
    <tr><td>Drawing an AD/AS diagram when the question says "injections and withdrawals graph"</td><td>The mark scheme names the J/W graph as a requirement. With no J/W graph, the maximum is Level 2 (8 of 14) for the question below.</td></tr>
    <tr><td>Drawing J as a sloping line, or W as a horizontal one</td><td>J is flat. W slopes up.</td></tr>
    <tr><td>Using the wrong axis labels</td><td>Vertical: injections and withdrawals (J and W). Horizontal: national income.</td></tr>
    <tr><td>Saying a rise in J raises income by the same amount</td><td>Income rises by ΔJ × the multiplier</td></tr>
    <tr><td>Treating saving as the only withdrawal</td><td>W = S + T + M</td></tr>
    <tr><td>Measuring the gap horizontally</td><td>The gap is the vertical distance between W and J at YF</td></tr>
    <tr><td>Showing the new equilibrium without the new line</td><td>Draw J1 as well as J, and label both Y and Y1</td></tr>
  </table></div>

  <h2>12 · How to draw it in an exam</h2>
  <ol>
    <li>Label the axes: <b>J and W</b> (vertical) and <b>national income</b> (horizontal).</li>
    <li>Draw <b>W</b> sloping up (start it below the axis if you want to show dissaving) and label it.</li>
    <li>Draw <b>J</b> as a horizontal line and label it.</li>
    <li>Mark the equilibrium <b>Y</b> where they cross, with a dashed line to the axis.</li>
    <li>For a change in injections, draw <b>J1</b> and mark <b>Y1</b>. For a change in W, show the new <b>W1</b>.</li>
    <li>For employment or gap questions, mark <b>YF</b> and show the vertical gap, and write the chain in words: J up, net injection, income and output up, employment up, multiplier.</li>
  </ol>
'''

watch = '''
  <h2>1 · Building the diagram</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stB"></div>
  <h2>2 · Why equilibrium is stable</h2>
  <div id="stE"></div>
  <h2>3 · A rise in injections: J to J1</h2>
  <div id="stM"></div>
  <h2>4 · A change in withdrawals: a shift and a rotation</h2>
  <div id="stW"></div>
  <h2>5 · Full employment and the gaps</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · Build your own J and W diagram</h2>
  <p>Set the injections, the withdrawal propensities, autonomous dissaving and the full employment level of income. The lab draws J and W, finds equilibrium, checks that S + T + M equals I + G + X, and measures the gap at full employment.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div><div id="g7"></div><div id="g8"></div>
    <div class="readout"><div><small>MPW (slope of W)</small><strong id="r1"></strong></div><div><small>Multiplier</small><strong id="r2"></strong></div><div><small>Equilibrium income</small><strong id="r3"></strong></div></div>
    <div class="readout"><div><small>S + T + M at equilibrium</small><strong id="r4"></strong></div><div><small>I + G + X</small><strong id="r5"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 460 400" role="img" aria-label="Injections and withdrawals diagram built from the chosen values"></svg></div></div></div>

  <h2>Lab 2 · What does this distance on the diagram represent?</h2>
  <p>Choose a distance and see what it means.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which line moves?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the adjustment to a rise in injections in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A lower interest rate and employment", "When a central bank cuts interest rates, borrowing becomes cheaper, so firms may raise investment and households may spend more and save less. J shifts up (and W may shift down), income and output rise by a multiple, and firms may hire more workers.", "a question on the effect of an interest rate cut on employment. Draw the J/W graph, then say that the effect depends on how sensitive investment is to interest rates and on the multiplier.") +
rw("A recession abroad", "If a country's main trading partners fall into recession, they buy fewer of its exports. J shifts down, equilibrium income falls by a multiple, and unemployment may rise in export industries.", "showing how foreign incomes feed into national income. Mention the multiplier and the share of exports in GDP.") +
rw("Rising saving after a crisis", "In a financial crisis, households and firms may try to save more to rebuild their finances. W shifts up, income falls, and total saving may not rise as much as people planned because lower income cuts saving too.", "the paradox of thrift. Link to a deflationary gap and to why governments may raise spending in a downturn.") +
rw("Benefits and automatic stabilisers", "In a downturn tax revenue falls and benefit payments rise automatically, so net taxes fall. W is lower than it would otherwise be, which means income falls by less than it would otherwise do.", "automatic stabilisers. Say that they lower the slope of W and therefore the multiplier.")
)

mc_exam = [
  ("In a closed economy, the marginal propensity to save is 0.1 and the marginal propensity to pay taxes is also 0.1. These values are constant. What is the increase in national income if there is an injection of $100 million? (Based on May/June 2021 · 32 · Q24)", ["$1000 million", "$500 million", "$100 million", "$80 million"], 1, "MPW = 0.1 + 0.1 = 0.2, so the multiplier is 1 ÷ 0.2 = 5. Income rises by 5 × $100m = $500m."),
  ("Which does not change the level of withdrawals from the circular flow of income? (Based on May/June 2022 · 32 · Q25)", ["Households having more of their income taken in tax after a rise in the rate of income tax", "Households spending more on imported cars after a currency appreciation", "Households taking money from their savings to spend on a celebration", "Households transferring money from an account in one bank to an account in another bank"], 3, "Moving money between banks is not a withdrawal. The others change taxes, imports or saving."),
  ("What could be used to offset a leakage from the circular flow of income? (Based on May/June 2022 · 32 · Q27)", ["A reduction in domestic consumption", "A reduction in government expenditure", "An increase in the rate of interest", "An increase in investment"], 3, "An injection offsets a leakage. Investment is an injection. The other options reduce spending."),
  ("What might decrease if a closed economy with a government sector decides to allow international trade? (Based on Oct/Nov 2023 · 31 · Q17)", ["Components of aggregate expenditure", "The number of injections into the circular flow", "The number of leakages from the circular flow", "The value of the economy's multiplier"], 3, "Trade adds exports (an injection) and imports (a leakage). The extra leakage lowers the multiplier."),
  ("An economy has falling incomes and rising unemployment. The central bank cuts the interest rate. When is this most likely to succeed? (Based on Oct/Nov 2024 · 33 · Q23)", ["When spending by consumers is income elastic", "When spending by firms on capital goods is interest rate elastic", "When the leakage on additional national income is high", "When overseas demand for exports is price inelastic"], 1, "If investment responds strongly to interest rates, J shifts up by more. A high leakage lowers the multiplier, so it makes the policy less effective.")
]

exam = exam_page("the injections and withdrawals diagram",
  "This diagram is tested in Paper 3 multiple choice on leakages, injections and the multiplier, and in Paper 4. One 20-mark Paper 4 essay names the graph and makes it a requirement. It is below with its mark scheme points, a plan and a model answer, followed by reworded multiple choice questions.",
  [("Essay, 20 marks", "1", "May/June 2025 (42) Q4"), ("Multiple choice (Paper 3)", "5 shown below", "2021 to 2024")],
  [
  eq("Based on May/June 2025 · 9708/42 · Q4", "20 marks", "With the help of an injections and withdrawals graph, assess the impact of a decrease in interest rates on the level of employment in an economy.",
     ["Knowledge and analysis (14): explain injections, withdrawals and employment, describe the circular flow, and analyse with an accurately labelled injections and withdrawals graph how a fall in interest rates affects employment through components of aggregate demand. A J/W graph can show full employment equilibrium and the links between expenditure, income, output and employment. Credit for the multiplier and accelerator.",
      "<b>Caps:</b> no J/W graph, maximum Level 2 (8 marks). A general monetary policy answer is also capped at Level 2. No credit for alternative policies such as supply-side or fiscal policy.",
      "Evaluation (6): inflation if the economy is near full employment; depreciation raising import costs (cost-push); house price inflation; the type of unemployment (less effective for structural); the MPS and MPC and the size of the multiplier and accelerator; time lags."],
     "Define injections, withdrawals and employment. Draw the J/W graph first, with J and J1, W, Y and Y1. Chain: lower rate, cheaper borrowing, I up (and C up, S down), J shifts up (and W may shift down), net injection, income and output up, employment up, multiplier. Then evaluate and judge.",
     [[("k", "Injections (J = I + G + X) are spending added to the circular flow of income and withdrawals (W = S + T + M) are income taken out of it, and national income is in equilibrium where J = W. Employment depends on output, because firms need labour to produce."), ("a", "A fall in the central bank's interest rate makes borrowing cheaper, so firms are more likely to invest in new machinery and households are more likely to borrow to spend, and the reward for saving is lower.")],
      [("n", "On the graph, higher investment shifts J up to J1, and lower saving may shift W down. At the old level of income, J1 is greater than W, so there is a net injection. Firms sell more than they planned and raise output, income rises, and as income rises W rises, until W equals J1 at a higher level Y1. Because the increase in income is a multiple of the change in injections, employment could rise by more than the initial boost to investment. Higher output leads firms to employ more workers, and extra income and demand may encourage more investment through the accelerator.")],
      [("e", "However, the effect depends on how sensitive investment is to interest rates. If firms are pessimistic, they may not borrow even at low rates and J may shift by only a little. The multiplier depends on the MPW: if households save a large share of extra income, or buy many imports, the rise in income is smaller. Interest rate changes take time to work, and if unemployment is structural, extra demand cannot create jobs for workers without the right skills. If the economy is close to full employment, extra demand may mainly raise prices, and a lower exchange rate may raise import costs."), ("e", "Overall, a cut in interest rates is likely to raise employment when there is spare capacity and cyclical unemployment, but the size depends on the interest elasticity of investment, the multiplier and the cause of unemployment.")]]),
  eq("Practice (not a past paper question)", "8 marks", "Explain, using an injections and withdrawals graph, why a rise in government spending of $50bn could raise national income by more than $50bn.",
     ["A labelled J/W graph with J, J1, W, Y and Y1.",
      "A rise in G raises J, so at the old Y injections exceed withdrawals and there is a net injection.",
      "Income rises, and each extra dollar of income leads to further spending and to further withdrawals, until W equals J1 again. The rise in income is ΔJ × 1 ÷ MPW.",
      "A limit: the size of the rise depends on the MPW."],
     "Draw J and J1 and W. Say what happens at the old equilibrium. Say how W catches up. Give the formula and a number.")
  ], mcq_h="Multiple choice questions")

tips = tips_html(
  [("Name the graph in the answer.", "Write J and W, label J1 and W1 where lines change, and label Y and Y1."),
   ("J is flat, W slopes up.", "Do not draw J as a sloping line unless the question says investment depends on income."),
   ("Show the net injection.", "At the old Y after a rise in J, say that J1 is greater than W, so income rises."),
   ("Use the multiplier from the slope.", "k = 1 ÷ MPW. A flatter W means a bigger multiplier."),
   ("Separate a shift from a rotation.", "Autonomous items shift a line. A change in a propensity rotates W."),
   ("Mark the gap vertically at YF.", "The size of the gap is the change in injections needed."),
   ("Evaluate with the propensities and the cause.", "The MPW, the type of unemployment, lags, and whether there is spare capacity.")],
  [("Equilibrium", "Equilibrium national income is where injections equal withdrawals, so there is no net injection."),
   ("Net injection", "If injections exceed withdrawals, income rises until withdrawals have risen by enough to equal injections."),
   ("Multiplier", "The multiplier is the reciprocal of the marginal propensity to withdraw, so a flatter W line gives a larger multiplier."),
   ("Shift", "A rise in autonomous saving shifts the withdrawals line upwards, which could reduce national income."),
   ("Evaluate", "However, if the economy is close to full employment, the extra demand may raise prices rather than output.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["assess"], CW["evaluate"]]) + FC

js = '''
const GRID = { style: "stroke:var(--line);stroke-width:1;opacity:.6" };
/* ---------- the J and W diagram ---------- */
const JL = 70, JSC = 0.7, JTOP = 36, JYMAX = 350, JYMIN = -100, JXMAX = 800, JY0 = JTOP + JYMAX * JSC, JBOT = JY0 - JYMIN * JSC;
const jx = (v) => JL + JSC * v, jy = (v) => JY0 - JSC * v;
function jwFrame() {
  let o = "";
  for (let v = 100; v <= JXMAX; v += 100) o += SV.line(jx(v), jy(JYMAX), jx(v), JBOT, "", GRID);
  for (let v = 0; v <= JXMAX; v += 100) o += SV.line(jx(v), JBOT, jx(v), JBOT + 5, "", {}) + SV.text(jx(v), JBOT + 19, v, "sm", { "text-anchor": "middle" });
  for (let v = JYMIN; v <= JYMAX; v += 50) o += SV.line(JL, jy(v), jx(JXMAX), jy(v), "", GRID) + SV.line(JL - 5, jy(v), JL, jy(v), "", {}) + SV.text(JL - 9, jy(v) + 4, v, "sm", { "text-anchor": "end" });
  return o + SV.line(JL, JBOT, JL, JTOP - 12) + SV.line(JL, jy(0), jx(JXMAX) + 10, jy(0)) + SV.text(JL + 8, JTOP - 18, "Injections and withdrawals, J and W ($bn)", "sm") + SV.text(jx(JXMAX / 2), JBOT + 62, "National income, Y ($bn)", "sm", { "text-anchor": "middle" });
}
function jwDraw(s) {
  const vj = s.vj, vw = s.vw, J = 200 + 50 * s.dJ, wi = -50 + 20 * s.wsh, ws = 0.5 + 0.1 * s.wrot, Y = (J - wi) / ws, Y0 = 500, W = (y) => wi + ws * y;
  const yEnd = (i, sl) => Math.min(JXMAX, (JYMAX - i) / sl);
  let o = jwFrame();
  const wLine = (i, sl, cls, extra) => { const e = yEnd(i, sl); return SV.line(jx(0), jy(i), jx(e), jy(i + sl * e), cls, extra || {}); };
  const wMoved = Math.abs(s.wsh) + Math.abs(s.wrot) > 0.01, jMoved = Math.abs(s.dJ) > 0.01;
  if (wMoved) o += wLine(-50, 0.5, "c2 dash", { "stroke-width": 2.5, opacity: 0.55 * vw }) + tag(jx(yEnd(-50, 0.5)) + 6, jy(-50 + 0.5 * yEnd(-50, 0.5)) + 4, "W", "t2", 1);
  o += wLine(wi, ws, wMoved ? "c4" : "c2", { "stroke-width": 3.5, ...op(vw) }) + tag(jx(yEnd(wi, ws)) + 6, jy(wi + ws * yEnd(wi, ws)) + 4, wMoved ? "W1" : "W", wMoved ? "t4" : "t2", vw);
  if (jMoved) o += SV.line(jx(0), jy(200), jx(JXMAX), jy(200), "c1 dash", { "stroke-width": 2.5, opacity: 0.55 * vj }) + tag(jx(JXMAX) + 6, jy(200) + 4, "J", "t1", 1);
  o += SV.line(jx(0), jy(J), jx(JXMAX), jy(J), jMoved ? "c3" : "c1", { "stroke-width": 3.5, ...op(vj) }) + tag(jx(JXMAX) + 6, jy(J) + 4, jMoved ? "J1" : "J", jMoved ? "t3" : "t1", vj);
  if (s.int > 0) o += SV.circle(jx(0), jy(wi), 6, "dot2", op(s.int)) + tag(jx(0) + 12, jy(wi) + 24, "−50: autonomous dissaving", "t2", s.int) + tag(jx(100), jy(0) - 10, "W = 0 at Y = 100", "t2", s.int, "middle");
  const mv = Math.abs(Y - Y0) > 1;
  if (s.eq > 0) {
    if (mv) o += SV.line(jx(Y0), jy(200), jx(Y0), JBOT, "c1 dash", { opacity: 0.4 * s.eq }) + SV.circle(jx(Y0), jy(200), 5, "dot1", { opacity: 0.45 * s.eq }) + tag(jx(Y0) + (Y > Y0 ? -4 : 4), JBOT + 34, "Y = 500", "t1", 0.6 * s.eq, Y > Y0 ? "end" : "start");
    o += SV.line(jx(Y), jy(J), jx(Y), JBOT, "c1 dash", op(s.eq)) + SV.circle(jx(Y), jy(J), 7, "dot1", op(s.eq)) + tag(jx(Y) + (mv && Y > Y0 ? 4 : mv ? -4 : 0), JBOT + 34, (mv ? "Y1 = " : "Y = ") + Lib.fmtN(Y, 0), "t1", s.eq, mv ? (Y > Y0 ? "start" : "end") : "middle");
  }
  if (s.yv > 0) { const w = W(s.yv), up = J > w, c = up ? "t3" : "t2", dir = up ? 1 : -1;
    o += SV.line(jx(s.yv), jy(w), jx(s.yv), jy(J), "c2", { "stroke-width": 7, ...op(s.a) }) + SV.circle(jx(s.yv), jy(w), 5, "dot2", op(s.a)) + SV.circle(jx(s.yv), jy(J), 5, "dot1", op(s.a));
    o += SV.line(jx(s.yv), jy(0) - 14, jx(s.yv + dir * 130), jy(0) - 14, "c2", op(s.a)) + SV.arrowHead(jx(s.yv + dir * 130), jy(0) - 14, up ? "r" : "l", "dot2");
    if (s.t) o += tag(jx(s.yv) + (up ? 12 : -12), jy((w + J) / 2) + 4, s.t, c, s.a, up ? "start" : "end"); }
  if (s.dy > 0) { const a = Math.min(Y0, Y), b = Math.max(Y0, Y);
    o += SV.line(jx(a), jy(0) + 24, jx(b), jy(0) + 24, "c3", { "stroke-width": 3, ...op(s.dy) }) + SV.line(jx(a), jy(0) + 18, jx(a), jy(0) + 30, "c3", op(s.dy)) + SV.line(jx(b), jy(0) + 18, jx(b), jy(0) + 30, "c3", op(s.dy)) + tag((jx(a) + jx(b)) / 2, jy(0) + 46, s.dyt, "t3", s.dy, "middle");
    if (s.dJt) o += SV.line(jx(740), jy(200), jx(740), jy(J), "c3", { "stroke-width": 5, ...op(s.dy) }) + tag(jx(740) - 8, (jy(200) + jy(J)) / 2 + 4, s.dJt, "t3", s.dy, "end"); }
  if (s.yf > 0) { const YF = s.yfv, w = W(YF), gap = w - J, c = gap > 0 ? "t2" : "t4";
    o += SV.line(jx(YF), jy(JYMAX), jx(YF), JBOT, "c4 dash", op(s.yf)) + tag(jx(YF), JBOT + 50, "YF = " + Lib.fmtN(YF, 0), "t4", s.yf, "middle");
    if (Math.abs(gap) > 0.5 && s.gp > 0) o += SV.line(jx(YF), jy(w), jx(YF), jy(J), "c2", { "stroke-width": 8, ...op(s.gp) }) + tag(jx(YF) + (gap > 0 ? 12 : -12), jy((w + J) / 2) + 4, (gap > 0 ? "deflationary gap = " : "inflationary gap = ") + Lib.fmtN(Math.abs(gap), 0), "t2", s.gp, gap > 0 ? "start" : "end"); }
  return o;
}
const D0 = { vj: 1, vw: 1, dJ: 0, wsh: 0, wrot: 0, int: 0, eq: 0, yv: 0, a: 0, t: "", dy: 0, dyt: "", dJt: "", yf: 0, yfv: 600, gp: 0 };
const st = (o) => Object.assign({}, D0, o);
$("#pic1").innerHTML = `<svg viewBox="0 0 720 ${JBOT + 84}" role="img" aria-label="Injections and withdrawals diagram: a horizontal J line, an upward sloping W line starting below the axis, and two equilibrium incomes">${jwDraw(st({ dJ: 1, int: 1, eq: 1, dy: 1, dyt: "ΔY = 100", dJt: "ΔJ = 50" }))}</svg>`;
const stp = (id, label, steps) => Lib.stepper($(id), { w: 720, h: JBOT + 84, label, base: D0, draw: jwDraw, tween: 1000, dwell: 6200, steps });

stp("#stB", "Building the injections and withdrawals diagram: J, W with a negative intercept, and equilibrium", [
  { cap: "<b>The axes.</b> National income on the horizontal axis, injections and withdrawals (J and W) on the vertical. The vertical axis runs below zero because W can be negative.", s: st({ vj: 0, vw: 0 }) },
  { cap: "<b>Injections J = I + G + X = 100 + 70 + 30 = 200.</b> A horizontal line: injections do not depend on domestic income.", s: st({ vj: 1, vw: 0 }) },
  { cap: "<b>Withdrawals W = S + T + M = −50 + 0.5Y.</b> It slopes up because saving, tax and imports rise with income. The slope is the MPW: 0.1 + 0.25 + 0.15 = 0.5.", s: st({ vj: 1, vw: 1 }) },
  { cap: "<b>The negative intercept.</b> At zero income there is no tax and no imports, but households dissave 50 (spend from past savings). So W is −50 where it meets the vertical axis, and crosses the horizontal axis at Y = 100.", s: st({ int: 1 }) },
  { cap: "<b>Equilibrium.</b> J = W where 200 = −50 + 0.5Y, so Y = <b>500</b>. At that income S = 0, T = 125 and M = 75, which total 200.", s: st({ int: 1, eq: 1 }) },
]);
stp("#stE", "Below equilibrium injections exceed withdrawals so income rises; above it withdrawals exceed injections so income falls", [
  { cap: "<b>Equilibrium at 500.</b> J = W = 200.", s: st({ eq: 1 }) },
  { cap: "<b>Income of 300.</b> J = 200 but W = −50 + 150 = 100, a <b>net injection of 100</b>. More is going into the circular flow than leaves it.", s: st({ eq: 1, yv: 300, a: 1, t: "J > W: net injection of 100" }) },
  { cap: "<b>Income rises.</b> Firms sell more than planned, so output and incomes rise. As income rises W rises with it, so the net injection shrinks, until W = J at 500.", s: st({ eq: 1, yv: 300, a: 1, t: "income rises" }) },
  { cap: "<b>Income of 700.</b> W = −50 + 350 = 300, which is <b>100 more than J</b>: a net withdrawal. Spending falls short of output.", s: st({ eq: 1, yv: 700, a: 1, t: "W > J: net withdrawal of 100" }) },
  { cap: "<b>Income falls</b> back to 500. From either side the economy moves to the point where J = W, so the equilibrium is stable.", s: st({ eq: 1, yv: 700, a: 1, t: "income falls" }) },
]);
stp("#stM", "A rise in injections of 50 shifts J up to J1 and income rises by 100", [
  { cap: "<b>Start at equilibrium, Y = 500.</b> J = 200, W = −50 + 0.5Y.", s: st({ eq: 1 }) },
  { cap: "<b>Government spending rises by 50.</b> J shifts up to J1 = 250. The old J is shown dashed.", s: st({ dJ: 1, eq: 0.01 }) },
  { cap: "<b>A net injection of 50.</b> At Y = 500, J1 = 250 but W is still 200. Injections exceed withdrawals, so income begins to rise.", s: st({ dJ: 1, eq: 0.01, yv: 500, a: 1, t: "net injection of 50" }) },
  { cap: "<b>W catches up.</b> For each 1 of extra income, W rises by only 0.5, so it needs income to rise by 50 ÷ 0.5 = 100 before W reaches J1. The new equilibrium is Y1 = 600.", s: st({ dJ: 1, eq: 1 }) },
  { cap: "<b>The multiplier.</b> The vertical shift of J is 50, the horizontal change in income is 100. ΔY = ΔJ × 1 ÷ MPW = 50 × 2 = 100.", s: st({ dJ: 1, eq: 1, dy: 1, dyt: "ΔY = 100 = 50 × 2", dJt: "ΔJ = 50" }) },
]);
stp("#stW", "A rise in autonomous saving shifts W up; a rise in the tax rate makes W steeper", [
  { cap: "<b>Start.</b> W = −50 + 0.5Y and J = 200, so Y = 500.", s: st({ eq: 1 }) },
  { cap: "<b>A shift of W.</b> Households become more cautious and autonomous dissaving falls from 50 to 30, so W shifts <b>up by 20</b> (W1 = −30 + 0.5Y). The slope is unchanged.", s: st({ wsh: 1, eq: 0.01 }) },
  { cap: "<b>Equilibrium falls.</b> Y = (200 + 30) ÷ 0.5 = <b>460</b>, a fall of 40, which is 20 × 2 (the same multiplier).", s: st({ wsh: 1, eq: 1 }) },
  { cap: "<b>A rotation of W.</b> The marginal rate of income tax rises from 0.25 to 0.35, so the MPW is 0.6. W becomes <b>steeper</b>, pivoting around its intercept at −50.", s: st({ wrot: 1, eq: 0.01 }) },
  { cap: "<b>Equilibrium falls and the multiplier falls.</b> Y = 250 ÷ 0.6 ≈ <b>417</b>. The multiplier is now 1 ÷ 0.6 ≈ 1.67 instead of 2.", s: st({ wrot: 1, eq: 1 }) },
]);
stp("#stG", "Full employment: W above J at YF is a deflationary gap and J above W is an inflationary gap", [
  { cap: "<b>Equilibrium is 500</b> with J = 200.", s: st({ eq: 1 }) },
  { cap: "<b>Full employment is at 600.</b> The economy is 100 below it.", s: st({ eq: 1, yf: 1, yfv: 600 }) },
  { cap: "<b>Compare J and W at YF.</b> W = −50 + 0.5 × 600 = 250, which is <b>50 above J</b>. Withdrawals exceed injections at full employment: a <b>deflationary gap of 50</b>, the vertical distance between W and J.", s: st({ eq: 1, yf: 1, yfv: 600, gp: 1 }) },
  { cap: "<b>Close it.</b> Raise injections by 50 (more G, lower interest rates for investment). J1 = 250 meets W at 600, so the gap disappears. Income rises by 50 × 2 = 100.", s: st({ dJ: 1, eq: 1, yf: 1, yfv: 600, gp: 1 }) },
  { cap: "<b>An inflationary gap.</b> If full employment were 400, W would be 150 at YF, which is <b>50 below J</b>. Injections exceed withdrawals at full employment, so the excess demand pulls up prices.", s: st({ eq: 1, yf: 1, yfv: 400, gp: 1 }) },
  { cap: "<b>Close it.</b> Cut injections by 50 (less G, higher interest rates). J falls to 150, meeting W at 400, and income falls by 100.", s: st({ dJ: -1, eq: 1, yf: 1, yfv: 400, gp: 1 }) },
]);

/* ---------- Lab 1 ---------- */
const nice = (mx) => [10, 20, 25, 50, 100, 200, 250, 500, 1000].find((s) => s >= mx / 6) || 1000;
function labJW() {
  if (!["#li", "#lg", "#lx", "#la", "#lps", "#ltx", "#lm", "#lf"].every((id) => $(id))) return;
  const I = +$("#li").value, G = +$("#lg").value, X = +$("#lx").value, a = +$("#la").value, mps = +$("#lps").value / 100, mrt = +$("#ltx").value / 100, mpm = +$("#lm").value / 100, YF = +$("#lf").value;
  const J = I + G + X, w = mps + mrt + mpm, Y = (J + a) / w, k = 1 / w, S = -a + mps * Y, T = mrt * Y, M = mpm * Y, WF = -a + w * YF, gap = WF - J;
  $("#r1").textContent = Lib.fmtN(w, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = "$" + Lib.fmtN(S + T + M, 0) + "bn"; $("#r5").textContent = "$" + Lib.fmtN(J, 0) + "bn";
  $("#rv").textContent = `W = ${a ? "−" + a + " + " : ""}${Lib.fmtN(w, 2)}Y meets J = ${J} at Y = $${Lib.fmtN(Y, 0)}bn. At that income S = ${Lib.fmtN(S, 0)}, T = ${Lib.fmtN(T, 0)} and M = ${Lib.fmtN(M, 0)}. ` + (Math.abs(gap) < 0.5 ? "Equilibrium is at full employment." : gap > 0 ? `At full employment W is above J by ${Lib.fmtN(gap, 0)}: a deflationary gap. Injections would have to rise by ${Lib.fmtN(gap, 0)}, which the multiplier turns into an income rise of ${Lib.fmtN(gap * k, 0)}.` : `At full employment J is above W by ${Lib.fmtN(-gap, 0)}: an inflationary gap. Injections would have to fall by ${Lib.fmtN(-gap, 0)}.`);
  const xm = Math.max(Y * 1.25, YF * 1.15, 100), ymax = Math.max(J * 1.35, 60), ymin = -a - 10, sx = 340 / xm, sy = 270 / (ymax - ymin), gx = (v) => 70 + sx * v, gy = (v) => 20 + sy * (ymax - v), yb = gy(ymin), xs = nice(xm), ys = nice(ymax - ymin);
  let o = "";
  for (let v = xs; v <= xm; v += xs) o += SV.line(gx(v), yb, gx(v), gy(ymax), "", GRID);
  for (let v = 0; v <= xm; v += xs) o += SV.line(gx(v), yb, gx(v), yb + 5, "", {}) + SV.text(gx(v), yb + 18, v, "sm", { "text-anchor": "middle" });
  for (let v = Math.ceil(ymin / ys) * ys; v <= ymax; v += ys) o += SV.line(70, gy(v), gx(xm), gy(v), "", GRID) + SV.line(65, gy(v), 70, gy(v), "", {}) + SV.text(61, gy(v) + 4, v, "sm", { "text-anchor": "end" });
  o += SV.line(70, yb, 70, gy(ymax) - 8) + SV.line(70, gy(0), gx(xm) + 8, gy(0)) + SV.text(76, 16, "J and W ($bn)", "sm") + SV.text(gx(xm / 2), yb + 64, "National income ($bn)", "sm", { "text-anchor": "middle" });
  const yEndW = Math.min(xm, (ymax + a) / w);
  o += SV.line(gx(0), gy(-a), gx(yEndW), gy(-a + w * yEndW), "c2", { "stroke-width": 3.5 }) + tag(gx(yEndW) + 4, gy(-a + w * yEndW) + 4, "W", "t2", 1) + SV.line(gx(0), gy(J), gx(xm), gy(J), "c1", { "stroke-width": 3.5 }) + tag(gx(xm) + 4, gy(J) + 4, "J", "t1", 1);
  o += SV.line(gx(Y), gy(J), gx(Y), yb, "c1 dash") + SV.circle(gx(Y), gy(J), 6, "dot1") + tag(gx(Y), yb + 32, "Y = " + Lib.fmtN(Y, 0), "t1", 1, "middle");
  o += SV.line(gx(YF), yb, gx(YF), gy(ymax), "c4 dash") + tag(gx(YF), yb + 46, "YF = " + YF, "t4", 1, "middle");
  if (Math.abs(gap) > 0.5) o += SV.line(gx(YF), gy(WF), gx(YF), gy(J), "c2", { "stroke-width": 7 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "li", label: "Investment I ($bn) ", min: 0, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g2"), { id: "lg", label: "Government spending G ($bn) ", min: 0, max: 200, step: 10, value: 70, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g3"), { id: "lx", label: "Exports X ($bn) ", min: 0, max: 200, step: 10, value: 30, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g4"), { id: "la", label: "Autonomous dissaving a ($bn) ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g5"), { id: "lps", label: "Marginal propensity to save (%) ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g6"), { id: "ltx", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 25, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g7"), { id: "lm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g8"), { id: "lf", label: "Full employment income ($bn) ", min: 200, max: 1000, step: 50, value: 600, fmt: (v) => v, onInput: labJW });
labJW();
btnTable("lbBtns", "lbOut", [
  ["Vertical distance between J and W at an income below equilibrium", "A net injection", "J > W, so income rises towards equilibrium."],
  ["Vertical distance between W and J at an income above equilibrium", "A net withdrawal", "W > J, so income falls towards equilibrium."],
  ["Vertical shift of J to J1", "The change in injections, ΔJ", "From a change in I, G or X."],
  ["Horizontal distance between Y and Y1", "The change in national income, ΔY", "ΔY = ΔJ × multiplier = ΔJ ÷ MPW."],
  ["Where W cuts the vertical axis (below zero)", "Autonomous dissaving", "The a in S = −a + sY, since T and M are zero at zero income."],
  ["Where W cuts the horizontal axis", "Income at which withdrawals are zero", "Here dissaving exactly offsets taxes and imports."],
  ["Vertical distance between W and J at full employment income", "The inflationary or deflationary gap", "W above J is deflationary. J above W is inflationary. The size is the injection needed."]
], ["Distance on the diagram", "What it represents", "Note"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens on the J and W diagram in each case?", ["J shifts", "W shifts", "W rotates (slope changes)", "Movement along a line"],
  [("The government raises spending on infrastructure", 0), ("Exports fall after a recession abroad", 0), ("Households raise their autonomous saving", 1), ("The marginal rate of income tax rises", 2), ("Income rises because J has risen", 3), ("Tariffs lower the marginal propensity to import", 2), ("Firms invest more because interest rates have fallen", 0), ("Households draw less on past savings when income is zero", 1)],
  "Autonomous items shift a line. A change in a marginal propensity rotates W. A change in income moves you along a line.") + MATCH([
  ["Injections (J)", "I + G + X: spending added to the circular flow"],
  ["Withdrawals (W)", "S + T + M: income taken out of the circular flow"],
  ["Net injection", "Injections minus withdrawals at an income below equilibrium"],
  ["Autonomous dissaving", "Spending from past savings at zero income; the negative intercept of W"],
  ["Marginal propensity to withdraw", "MPS + MRT + MPM; the slope of W"],
  ["Multiplier", "1 ÷ MPW; the number of times a change in J is multiplied into a change in income"]]) + ORDER(
  "Put the adjustment to a rise in injections in order, starting with the first event.",
  ["Injections rise, so J shifts up to J1", "At the old income, J1 exceeds W: a net injection", "Firms sell more than planned and raise output and employment", "Income rises and withdrawals rise with it along the W line", "W equals J1 at a higher income and the economy is in equilibrium again"],
  "Income rises until withdrawals have caught up with the new injections. The change is a multiple of the rise in J.") + CALC([
  {"q": "MPS = 0.1, MRT = 0.25 and MPM = 0.15. What is the multiplier?", "a": 2, "tol": 0.01, "hint": "1 ÷ MPW.", "sol": "MPW = 0.5, so k = <b>2</b>."},
  {"q": "W = −50 + 0.5Y and J = 200. What is equilibrium income ($bn)?", "a": 500, "tol": 0.01, "hint": "Set −50 + 0.5Y = 200.", "sol": "0.5Y = 250, so Y = <b>500</b>."},
  {"q": "J rises from 200 to 250 and W = −50 + 0.5Y. What is the new equilibrium income ($bn)?", "a": 600, "tol": 0.01, "hint": "−50 + 0.5Y = 250.", "sol": "0.5Y = 300, so Y = <b>600</b>."},
  {"q": "At an income of 300, W = −50 + 0.5Y and J = 200. What is the net injection ($bn)?", "a": 100, "tol": 0.01, "hint": "J − W.", "sol": "W = 100, so the net injection is 200 − 100 = <b>100</b>."},
  {"q": "Full employment income is 600, W = −50 + 0.5Y and J = 200. What is the deflationary gap, the vertical distance between W and J at 600 ($bn)?", "a": 50, "tol": 0.01, "hint": "W at 600 minus J.", "sol": "W = 250, so the gap is 250 − 200 = <b>50</b>."},
  {"q": "In a closed economy MPS = 0.1 and MRT = 0.1. By how much does income rise ($m) if injections rise by $100m?", "a": 500, "tol": 0.01, "hint": "k = 1 ÷ 0.2.", "sol": "k = 5, so the rise is 5 × 100 = <b>$500m</b>."}
]) + MCQ([
  ("What does a horizontal J line assume?", ["Injections rise with income", "Injections do not depend on domestic income", "Injections equal withdrawals at every income", "There is no government"], 1, "J is flat because I, G and X are assumed to be set by factors other than domestic income."),
  ("Why does W slope upwards?", ["Because saving, taxes and imports all rise with income", "Because injections rise with income", "Because prices rise", "Because the multiplier is greater than one"], 0, "Each of S, T and M increases as income rises."),
  ("At an income below equilibrium, which is true?", ["W > J and income rises", "J > W and income rises", "J > W and income falls", "J = W"], 1, "A net injection raises output and income."),
  ("A flatter W line means:", ["A smaller multiplier", "A larger multiplier", "No change in the multiplier", "No equilibrium"], 1, "The multiplier is 1 ÷ MPW, and a flatter line is a smaller MPW."),
  ("Which is shown by the negative intercept of W?", ["Autonomous dissaving", "Autonomous investment", "The marginal rate of tax", "Net exports"], 0, "At zero income taxes and imports are zero, so the negative withdrawal is dissaving.")
], "qz1") + CARDS([
  ("Injections J", "I + G + X; spending added to the circular flow; shown as a horizontal line."),
  ("Withdrawals W", "S + T + M; income taken out of the circular flow; slopes up."),
  ("Equilibrium", "J = W; no net injection or withdrawal."),
  ("Net injection", "J minus W at an income below equilibrium; income rises."),
  ("MPW", "MPS + MRT + MPM; the slope of W."),
  ("Multiplier", "1 ÷ MPW; ΔY = ΔJ × k."),
  ("Shift vs rotation of W", "Autonomous items shift it; a change in a marginal propensity rotates it."),
  ("Gap at YF", "W − J > 0 is deflationary; J − W > 0 is inflationary.")]) + MCQ(mc_exam)

build("sy9jw", "injections-withdrawals-diagram", "The Injections and Withdrawals Diagram Explained", EY,
  "A step-by-step explainer of the injections and withdrawals (J and W) graph: building J and W, why W starts below zero, equilibrium and stability, rises in injections and the multiplier, shifts and rotations of W, the gaps at full employment and how it compares with the 45° diagram. With animations, a build-your-own lab, drills and exam questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
