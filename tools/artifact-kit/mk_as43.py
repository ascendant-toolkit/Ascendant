"""AS syllabus 4.3.1-4.3.5 Aggregate demand. Run: python3 tools/artifact-kit/mk_as43.py"""
from asx import *
EY = EYAS("4.3.1 to 4.3.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Aggregate demand (AD)</b> is the <b>total planned spending on an economy's goods and services at each price level</b> in a given period, and equals <b>C + I + G + (X − M)</b>: consumption, investment, government spending and net exports. The AD curve <b>slopes downward</b> because a lower price level raises <b>real wealth</b>, lowers <b>interest rates</b> and makes <b>exports more competitive</b> and imports less so. A change in the <b>price level</b> causes a <b>movement along</b> the AD curve; a change in <b>any component at every price level</b> (interest rates, income taxes, confidence, the exchange rate, government spending, foreign income) <b>shifts</b> the whole curve right or left. Detailed knowledge of the components is not required, only what they are and what shifts them.</p></div>

  <h2>1 · The components of AD (4.3.1 to 4.3.3)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Component</th><th>Meaning</th><th>Determinants (examples)</th></tr>
    <tr><td><b>C</b> Consumption</td><td>Household spending on goods and services</td><td>Disposable income, income taxes, interest rates, wealth, consumer confidence, credit</td></tr>
    <tr><td><b>I</b> Investment</td><td>Firms' spending on capital goods (and stock building)</td><td>Interest rates, business confidence and expected profits, technology, corporation tax</td></tr>
    <tr><td><b>G</b> Government spending</td><td>Spending on goods, services and infrastructure (not transfer payments)</td><td>Government policy, budget position, political aims</td></tr>
    <tr><td><b>X − M</b> Net exports</td><td>Export spending less import spending</td><td>Exchange rate, foreign incomes, price competitiveness, protectionism</td></tr>
  </table></div>
  <ul>
    <li><b>Closed economy:</b> AD = C + I + G (no trade). <b>Open economy:</b> add X − M.</li>
    <li>Transfer payments are not part of G because they are not spending on output; they affect AD indirectly through disposable income.</li>
  </ul>

  <h2>2 · Shape of the AD curve and shifts (4.3.4 to 4.3.5)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Why AD slopes down:</b> (1) <b>wealth effect</b>: a lower price level raises the real value of savings, so people spend more; (2) <b>interest rate effect</b>: lower prices reduce demand for money and interest rates, raising spending; (3) <b>international trade effect</b>: lower domestic prices make exports cheaper and imports dearer, so net exports rise.</li>
    <li><b>Movement along AD:</b> caused only by a change in the price level.</li>
    <li><b>Shift right (increase):</b> lower interest rates, lower income tax, higher confidence, higher government spending, depreciation of the currency, growth in trading partners' incomes, easier credit.</li>
    <li><b>Shift left (decrease):</b> higher interest rates, higher taxes, falling confidence, cuts in government spending, appreciation, a recession abroad, tighter credit.</li>
    <li>An <b>increase in AD</b> raises real output and the price level; how much of each depends on the shape of the AS curve.</li>
  </ul>

  <h2>3 · Worked example: calculating AD</h2>
  <div class="tw"><table class="t">
    <tr><th>Component</th><th>$bn</th><th>Change</th><th>New $bn</th></tr>
    <tr><td>C</td><td>600</td><td>Consumers' confidence rises: +50</td><td>650</td></tr>
    <tr><td>I</td><td>150</td><td>Interest rates fall: +20</td><td>170</td></tr>
    <tr><td>G</td><td>200</td><td>No change</td><td>200</td></tr>
    <tr><td>X</td><td>180</td><td>Currency falls: +10</td><td>190</td></tr>
    <tr><td>M</td><td>160</td><td>Imports fall as currency falls: −10</td><td>150</td></tr>
    <tr><td><b>AD = C + I + G + (X − M)</b></td><td><b>970</b></td><td></td><td><b>1,060</b></td></tr>
  </table></div>
  <ul>
    <li>AD rises from 970 to 1,060 (a rise of 9.3%). The AD curve shifts to the right. Each change in a component has a cause: confidence (C), lower interest rates (I), and the exchange rate (X and M).</li>
  </ul>

  <h2>4 · Determinants of the components in more detail</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Component affected</th><th>Effect of a rise in the factor</th></tr>
    <tr><td><b>Interest rates</b></td><td>C and I</td><td>Borrowing dearer and saving more attractive, so C and I fall; AD shifts left</td></tr>
    <tr><td><b>Income taxes</b></td><td>C</td><td>Lower disposable income, so C falls; AD shifts left</td></tr>
    <tr><td><b>Consumer and business confidence</b></td><td>C and I</td><td>More optimism: C and I rise; AD shifts right</td></tr>
    <tr><td><b>Household wealth</b> (house and share prices)</td><td>C</td><td>Feeling richer, people spend more; AD shifts right</td></tr>
    <tr><td><b>Availability of credit</b></td><td>C and I</td><td>Easier credit raises spending; AD shifts right</td></tr>
    <tr><td><b>Government spending</b></td><td>G</td><td>Rises: AD shifts right</td></tr>
    <tr><td><b>Exchange rate</b></td><td>X − M</td><td>A rise (appreciation) makes exports dearer and imports cheaper, so X − M falls; AD shifts left</td></tr>
    <tr><td><b>Foreign incomes</b></td><td>X</td><td>Higher incomes abroad raise demand for exports; AD shifts right</td></tr>
    <tr><td><b>Corporation tax and expected profits</b></td><td>I</td><td>Lower tax and higher expected profits raise I</td></tr>
  </table></div>

  <h2>5 · The effect of a change in AD on output and prices</h2>
  <ul>
    <li>The effect depends on the <b>shape of the AS curve</b>: if there is <b>spare capacity</b> (the flat part), a rise in AD mainly raises <b>real output and employment</b>; near <b>full capacity</b> (the steep part), it mainly raises the <b>price level</b>.</li>
    <li><b>Benefits of higher AD:</b> economic growth, falling unemployment, higher incomes and tax revenue.</li>
    <li><b>Problems:</b> inflationary pressure, a worsening current account (more imports), a larger budget deficit if driven by government spending, and possible overheating.</li>
    <li><b>Lower AD</b> reduces inflation but may cause recession and unemployment.</li>
  </ul>

  <h2>6 · Common mistakes</h2>
  <div class="warn"><b class="h">Do not write this</b>A change in the price level shifts the AD curve (it causes a movement along it). Do not include transfer payments in G. Do not say that AD slopes downward for the same reason as a micro demand curve: it slopes down because of the wealth, interest rate and international trade effects.</div>
  <div class="tip"><b class="h">Exam tip</b>Name the <b>component</b> that changes and say which way the AD curve <b>shifts</b>. Do not draw a change in the price level as a shift. For essays, say what then happens to real output and prices using the AS curve.</div>
'''

watch = '''
  <h2>1 · The components add up to AD</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A movement along AD and a shift of AD</h2>
  <div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · Add up the components</h2>
  <p>Set each component ($bn) at the current price level and see total AD.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>AD (open economy)</small><strong id="r1"></strong></div><div><small>Net exports</small><strong id="r2"></strong></div><div><small>Change from 100</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="A stacked bar of the components of aggregate demand"></svg></div></div></div>

  <h2>Lab 2 · What shifts AD?</h2>
  <p>Choose a change. The diagram shows the AD curve shifting and the new short-run equilibrium.</p>
  <div class="card"><div class="grid2"><div><div id="evB" class="btnrow"></div>
    <div class="readout"><div><small>Component</small><strong id="t1"></strong></div><div><small>AD</small><strong id="t2"></strong></div><div><small>Real output and prices</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with the AD curve shifted for the chosen event"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which component changes?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the interest rate effect in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Lower interest rates", "A central bank cuts interest rates. Borrowing becomes cheaper, so households buy more on credit (C) and firms invest more (I). Aggregate demand shifts right, raising real output and, as the economy nears capacity, prices.", "interest rates affecting C and I.") +
rw("A weaker currency", "If the exchange rate falls, exports become cheaper abroad and imports dearer at home, so net exports (X − M) rise and AD shifts right, other things equal.", "the exchange rate affecting net exports.") +
rw("A fall in consumer confidence", "Households fear job losses, so they cut spending and save more. Consumption falls, AD shifts left, and output and employment tend to fall.", "confidence as a determinant of consumption.") +
rw("Government road building", "State spending on infrastructure is part of G. It raises AD directly, and also supports the economy's capacity if it improves transport, so it may also shift AS in the long run.", "G as a component of AD.") +
rw("A cut in interest rates", "A central bank cuts interest rates. Borrowing becomes cheaper, so households spend more on credit and firms invest more, and a weaker currency helps exports. AD shifts right.", "interest rates changing C, I and net exports.") +
rw("A fall in consumer confidence", "News of job losses makes households pessimistic. They cut back on big purchases and save more, so consumption falls and AD shifts left, even though prices and incomes have not yet changed.", "confidence as a determinant of AD.")
)

mc_exam = [
  mcq("s22_13", 21, "What is a correct description of an aggregate demand (AD) curve?", ["It is a curve obtained by adding the market demand curves of all consumer goods traded in an economy", "It is a curve determined by the horizontal summation of all individual consumer demand curves for a product", "It is a curve that shows the total amount of goods and services firms are willing to buy at a given price in an economy", "It is a curve that shows the total demand of all goods and services produced at all price levels in an economy"], 3, "AD shows total planned spending on domestic output at each price level."),
  mcq("s22_13", 19, "The diagram shows an aggregate demand (AD) curve with X on the horizontal axis and Y on the vertical axis. What is measured on each axis?", ["X: money national output, Y: real disposable income", "X: price level, Y: real GDP", "X: real GDP, Y: price level", "X: real disposable income, Y: money national output"], 2, "AD is drawn with real GDP (output) on the horizontal axis and the price level on the vertical axis."),
  mcq("w21_13", 30, "What are the components of aggregate demand?", ["consumption + investment + government spending + (exports − imports)", "consumption + investment + taxation − (exports − imports)", "consumption + saving + taxation − (exports − imports)", "consumption + saving + taxation + (exports − imports)"], 0, "AD = C + I + G + (X − M)."),
  mcq("s23_11", 18, "Which statement explains why the aggregate demand curve is downward sloping?", ["As prices fall, the demand for exports becomes more elastic", "As prices fall, fewer goods are imported", "As prices fall, the rate of interest will rise", "As prices fall, real wealth rises and so spending increases"], 3, "The wealth effect: a lower price level raises the real value of savings, so spending rises."),
  mcq("s24_11", 19, "Why would a fall in a country's average price level cause its aggregate demand curve to slope downwards?", ["It leads to an increase in interest rates", "It reduces the real value of money balances", "It makes the country's goods cheaper relative to foreign goods", "It leads to the expectation of further price falls"], 2, "Cheaper domestic goods boost exports and cut imports, raising net exports."),
  mcq("s25_12", 18, "The aggregate demand curve is typically downward sloping. What is one possible explanation for this?", ["A fall in the price level will lead to a rise in demand for imports", "As the price level falls, improved productivity will reduce unit costs", "If the price level is high, any interest rate changes will encourage consumption", "The real value of assets increases as the price level falls"], 3, "A lower price level raises the real value of assets, which raises spending (the wealth effect)."),
  mcq("s23_12", 19, "Why might aggregate demand increase when a country's price level falls?", ["Domestic interest rates will tend to fall", "Imports become more price competitive", "Real incomes fall", "The purchasing power of savings falls"], 0, "A lower price level reduces demand for money, so interest rates tend to fall and spending rises."),
  mcq("s23_13", 25, "What is the most likely cause of an outward shift of a country's aggregate demand curve?", ["a decrease in the competitiveness of domestically produced products", "a decrease in the general price level", "a decrease in the money supply", "a depreciation of the country's exchange rate"], 3, "A depreciation raises net exports. A price-level fall is a movement along."),
  mcq("w22_12", 20, "An increase in what will shift the aggregate demand curve in an economy to the right?", ["budget deficit", "consumer savings", "general price level", "interest rate"], 0, "A larger deficit means higher government spending or lower taxes, raising AD."),
  mcq("s20_12", 19, "What is likely to cause a decrease in aggregate demand?", ["an appreciation in the exchange rate", "an improvement in consumer confidence", "an increase in government expenditure", "an increase in the money supply"], 0, "An appreciation makes exports dearer and imports cheaper, lowering net exports."),
  mcq("m24_12", 19, "Aggregate demand in an economy may decrease as a result of an increase in which of the following?", ["consumption expenditure", "government expenditure", "import expenditure", "investment expenditure"], 2, "Imports are subtracted in AD, so higher spending on imports lowers it."),
  mcq("w23_12", 24, "A government increases the rate of income tax. What is the effect, in the short run, on the aggregate demand curve or the aggregate supply curve?", ["The aggregate demand curve shifts left", "The aggregate demand curve shifts right", "The aggregate supply curve shifts left", "The aggregate supply curve shifts right"], 0, "Higher income tax cuts disposable income and consumption, so AD shifts left.")
]

exam = exam_page("aggregate demand",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Aggregate demand is an 8 mark Paper 2 part most years, and a 12 mark discussion on whether more AD is beneficial, and it appears in nearly every Paper 1. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "May/June 2024 (21) Q4(a); May/June 2024 (23) Q4(a); Oct/Nov 2023 (22) Q5(a)"), ("Essay parts, 12 marks", "2", "May/June 2024 (23) Q4(b); May/June 2021 (23) Q3(b)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("s24_21", "4(a)"), "8 marks", "Explain three of the components of aggregate demand and consider the extent to which they may be increased without leading to inflation.",
     ["Knowledge (up to 3): a clear and accurate explanation of three components of AD: consumer spending, investment, government spending and net exports (1 each). Simply mentioning a component does not earn a mark.",
      "Analysis (up to 3): one cause of inflation is where AD rises more than AS (1), but it considers why this may or may not occur, for example the economy is operating below capacity or some of the increase in AD also increases AS. If both scenarios are considered, full marks may be awarded; one-sided answers get a maximum of 1.",
      "Evaluation (up to 2): consideration of both sides (1), leading to a valid conclusion (1)."],
     "Three components explained. Inflation if AD rises faster than AS. No inflation if spare capacity or AS also rises. Judge.",
     [[("k", "Consumption is household spending on goods and services, such as cars and holidays. Investment is firms' spending on capital goods, such as machinery. Government spending includes spending on public services and infrastructure, such as schools and roads.")], [("n", "If these components increase and the economy has spare capacity, firms can raise output without raising prices, so little inflation results. If AD rises faster than AS, as when the economy is near full capacity, the extra demand pulls up prices.")], [("e", "Whether inflation follows depends on how much spare capacity there is and whether the rise in AD, for example from investment, also raises AS. Investment is the most likely to be increased without inflation, because it adds to capacity.")]]),
  eq(P("s24_23", "4(a)"), "8 marks", "With the help of a diagram, explain how increases in aggregate demand affect the level of real output and the price level in an economy and consider when such increases may become a problem.",
     ["Knowledge (up to 3): the components of AD, C + G + I + X − M (1); an accurately labelled AD/AS diagram with the initial equilibrium (1); a rightward shift of AD and the subsequent changes in the price level and real GDP (1).",
      "Analysis (up to 3): an explanation of why AD might increase (1); why the increase may not cause problems such as inflation, for example because of the shape of the AS curve or because AS may increase in line with AD if the cause is investment (1); why it may cause problems, for example the economy is at full capacity and AS cannot increase (1).",
      "Evaluation (up to 2): a recognition that increases in AD may cause an inflationary rise in the price level beyond the full-employment level of output (1), with a justified conclusion (1)."],
     "Diagram: AD shifts right, output and price level rise. No problem with spare capacity. Problem at full capacity: inflation only.",
     [[("k", "Aggregate demand is C + I + G + (X − M). On an AD/AS diagram, the initial equilibrium is where AD meets short-run AS. An increase in AD shifts the curve right, so real output and the price level both rise.")], [("n", "AD may increase because of lower interest rates, which raise consumption and investment. If the economy has spare capacity, output rises a lot and prices little, which is beneficial. But at or near full capacity AS cannot increase, so extra AD mainly raises prices.")], [("e", "The increases become a problem when output cannot rise further, as then the rise in AD is inflationary beyond the full-employment level of output. The result depends on the position of the economy and the shape of the AS curve.")]]),
  eq(P("w23_22", "5(a)"), "8 marks", "With the help of a diagram, explain one reason for an increase in aggregate demand and one reason for an increase in aggregate supply and consider whether an increase in aggregate demand will always lead to inflation.",
     ["Knowledge (up to 3): AD is the total demand for an economy's goods and services at a given price level, or C + I + G + (X − M) (1); AS is the total output producers are willing and able to supply at a given price level (1); an accurate diagram showing AD and AS curves (1).",
      "Analysis (up to 3): a valid cause of an increase in AD (1); a valid cause of an increase in AS (1); both increases shown by rightward shifts, with the resulting impact on the price level on an accurate diagram (1).",
      "Evaluation (up to 2): whether an increase in AD always leads to inflation depends on the increase in AS and the shape of or position on the AS curve."],
     "Define AD and AS. One cause each, shown as right shifts. AD rise leads to inflation only if AS does not rise or the economy is near capacity.",
     [[("k", "Aggregate demand is total spending on a country's output at each price level, C + I + G + (X − M). Aggregate supply is the total output firms are willing and able to produce at each price level.")], [("n", "AD might increase because of lower interest rates, which raise consumption and investment, shifting AD to the right. AS might increase because of better technology, which lowers costs, shifting SRAS to the right. Together they raise real output, and the price level may rise only a little, or fall.")], [("e", "An increase in AD does not always lead to inflation. If there is spare capacity, or AS also increases, output rises with little change in the price level, but if the economy is near full capacity, inflation is more likely.")]]),
  eq(P("s24_23", "4(b)"), "12 marks", "Assess whether increases in aggregate demand are the best way of reducing unemployment in a high-income country.",
     ["Analysis (up to 8): what is meant by unemployment and its main types in a high-income economy; increases in AD arise from fiscal and monetary policy; policies such as lower taxes, higher government spending and lower interest rates may reduce cyclical unemployment but may not reduce structural unemployment; supply-side policy may reduce unemployment by influencing AS, through training, education and deregulation, but is a long-term approach, may be costly and does not address falls in AD behind cyclical unemployment.",
      "Evaluation (up to 4): considers alternative policies and balances them; a judgement on whether AD is the best way, with a conclusion."],
     "AD: cuts cyclical unemployment, quick, but not structural; inflation, deficit. Supply-side: structural, slow, costly. Judge by type of unemployment.",
     [[("n", "Increasing AD through lower interest rates, tax cuts or more government spending raises output, so firms need more workers and cyclical unemployment falls, and this can work quickly. But if unemployment is structural, because workers' skills do not match vacancies, more spending creates little employment and may only raise prices. Higher AD can also worsen the budget deficit and the current account. Supply-side policy, such as training and education, tackles structural unemployment but takes years, costs money and does not help where the problem is weak demand.")], [("e", "Increasing AD is the best way when unemployment is mainly cyclical and there is spare capacity, but not when it is structural. A high-income country is likely to have both types, so a mix of demand-side and supply-side policies is likely to be most effective.")]]),
  eq(P("s21_23", "3(b)"), "12 marks", "Discuss whether an increase in aggregate demand would be of overall benefit for an economy.",
     ["Analysis (up to 8): the benefits of an increase in AD to the economy (up to 4), such as economic growth and higher employment, considering firms, government and consumers or workers; the possible problems (up to 4), such as inflation and a current account deficit.",
      "Evaluation (up to 4): clearly compares the benefits and the problems resulting from an increase in AD, with one mark reserved for a reasoned conclusion. No KU marks for merely explaining terms in the question."],
     "Benefits: growth, jobs, profits, tax revenue. Problems: inflation, current account deficit, overheating. Judge: depends on spare capacity.",
     [[("n", "A rise in AD raises real output, which creates jobs for workers, higher profits for firms and more tax revenue for the government. But if the economy is near full capacity the extra demand mainly raises prices, causing inflation, and higher incomes raise spending on imports, worsening the current account.")], [("e", "The overall benefit is likely to be greatest when there is spare capacity and unemployment is high, and smallest when the economy is already near full capacity. So an increase in AD is beneficial overall, but not always, and its benefits depend on how much capacity is available.")]])
  ],
  )

tips = tips_html(
  [("AD = C + I + G + (X − M).", "Know each component and an example of what shifts it."),
   ("Price level moves along; everything else shifts.", "A fall in prices is a movement, not a shift."),
   ("Explain the downward slope.", "Wealth, interest rate and international trade effects."),
   ("Name the component.", "Interest rates affect C and I; the exchange rate affects X − M."),
   ("Say what happens next.", "Output and price level, depending on AS."),
   ("Transfer payments are not G.", "They affect AD through income."),
   ("Judge with capacity.", "Spare capacity means growth; full capacity means inflation.")],
  [("Aggregate demand", "Aggregate demand is total planned spending on an economy's output at each price level."),
   ("Shift", "A fall in interest rates could shift the AD curve to the right."),
   ("Components", "AD is made up of consumption, investment, government spending and net exports."),
   ("Slope", "The AD curve slopes down because of the wealth, interest rate and trade effects."),
   ("Consider", "The effect on prices depends on how close the economy is to capacity.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- components stack ---------- */
function acDraw(s) {
  const Y = (v) => 250 - v * 1.7; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn at the current price level", "sm");
  const parts = [["C", s.c, "f1"], ["I", s.i, "f2"], ["G", s.g, "f3"], ["X", s.x, "f1"]]; let y = 250;
  parts.forEach(([l, v, c], k) => { const h = v * 1.7; if (v > 0.5) o += SV.rect(150 + k * 0, y - h, 140, h, c, op(0.65)) + SV.text(220, y - h / 2 + 5, l + " " + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }); y -= h; });
  if (s.m > 0.5) { const h = s.m * 1.7; o += SV.rect(340, 250 - h, 140, h, "f3", op(0.65)) + SV.text(410, 250 - h / 2 + 5, "M " + Lib.fmtN(s.m, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(410, 270, "Imports (subtracted)", "sm", { "text-anchor": "middle" }); }
  const ad = s.c + s.i + s.g + s.x - s.m; o += SV.text(220, 270, "Gross spending", "sm", { "text-anchor": "middle" }) + SV.line(500, Y(ad), 700, Y(ad), "c4", { "stroke-dasharray": "6 4", "stroke-width": 2 }) + tag(704, Y(ad) + 4, "AD = " + Lib.fmtN(ad, 0), "c4", 1, "end");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Consumption, investment, government spending and exports add up, with imports subtracted, to aggregate demand">${acDraw({ c: 60, i: 20, g: 25, x: 25, m: 30 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 290, label: "C + I + G + X − M", base: { c: 0, i: 0, g: 0, x: 0, m: 0 }, draw: acDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Consumption (C)</b>: household spending, the largest component, here $60bn.", s: { c: 60 } },
  { cap: "<b>Investment (I)</b>: firms' spending on capital, $20bn.", s: { c: 60, i: 20 } },
  { cap: "<b>Government spending (G)</b> on public services and infrastructure, $25bn.", s: { c: 60, i: 20, g: 25 } },
  { cap: "<b>Exports (X)</b>: foreign spending on domestic output, $25bn.", s: { c: 60, i: 20, g: 25, x: 25 } },
  { cap: "<b>Imports (M)</b> are subtracted, because they are spending that does not go to domestic output. AD = 60 + 20 + 25 + 25 − 30 = $100bn.", s: { c: 60, i: 20, g: 25, x: 25, m: 30 } },
] });

/* ---------- movement and shift ---------- */
function msDraw(s) {
  let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level") + sdCurve("D", 0, "c2", s.a > 0.05 ? 0.4 : 1, "AD1");
  if (s.a > 0.05) o += sdCurve("D", s.a, "c2", 1, "AD2");
  const p = s.p, q = (90 - p) / 0.8 + (s.a > 0.05 ? s.a * (s.k || 0) : 0); o += SV.line(SDX(q), SDY(p), SDX(q), 270, "dash") + SV.line(70, SDY(p), SDX(q), SDY(p), "dash") + SV.circle(SDX(q), SDY(p), 7, "dot3") + SV.text(62, SDY(p) + 4, Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in the price level moves along AD, while a rise in a component shifts AD right">${msDraw({ p: 40, a: 20, k: 0 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A movement along AD and a shift of AD", base: { p: 50, a: 0, k: 0 }, draw: msDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> At a price level of 50, planned spending on domestic output is 50 units.", s: { p: 50, a: 0, k: 0 } },
  { cap: "<b>The price level falls to 35.</b> Real wealth rises, interest rates fall and exports become cheaper, so spending rises along the same AD curve: a <b>movement along</b>.", s: { p: 35, a: 0, k: 0 } },
  { cap: "<b>Interest rates fall.</b> At every price level consumers and firms want to spend more, so the whole AD curve <b>shifts right</b> to AD2. At a price level of 35 spending is now higher still.", s: { p: 35, a: 20, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  const ids = ["cc", "ii", "gg", "xx", "mm"]; if (!ids.every((i) => $("#" + i))) return;
  const [c, i, g, x, m] = ids.map((k) => +$("#" + k).value), ad = c + i + g + x - m;
  $("#r1").textContent = "$" + ad + "bn"; $("#r2").textContent = (x - m >= 0 ? "+" : "") + (x - m); $("#r3").textContent = (ad - 100 >= 0 ? "+" : "") + (ad - 100);
  $("#rv").textContent = `AD = ${c} + ${i} + ${g} + (${x} − ${m}) = ${ad}. ${ad > 100 ? "Higher than the starting $100bn: the AD curve has shifted to the right." : ad < 100 ? "Lower than the starting $100bn: the AD curve has shifted to the left." : "Equal to the starting $100bn: no shift."} Net exports are ${x - m >= 0 ? "a surplus" : "a deficit"} of ${Math.abs(x - m)}.`;
  $("#labA").innerHTML = acDraw({ c, i, g, x, m });
}
[["g1", "cc", "Consumption (C), $bn ", 60], ["g2", "ii", "Investment (I), $bn ", 20], ["g3", "gg", "Government spending (G), $bn ", 25], ["g4", "xx", "Exports (X), $bn ", 25], ["g5", "mm", "Imports (M), $bn ", 30]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 80, step: 5, value: v, fmt: (z) => z, onInput: labC }));
labC();

/* ---------- Lab 2 ---------- */
const EVA = [["Interest rates fall", "C and I", 15], ["Income tax rises", "C", -15], ["Consumer confidence falls", "C", -20], ["Currency depreciates", "X − M", 15], ["Government spends more on roads", "G", 15], ["Trading partners' incomes rise", "X", 15], ["Business confidence rises", "I", 15], ["Currency appreciates", "X − M", -15]];
function showA(i) {
  const [n, comp, a] = EVA[i], e = sdEq(a, 0), e0 = sdEq(0, 0); $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = comp; $("#t2").textContent = a > 0 ? "Shifts right" : "Shifts left"; $("#t3").textContent = (e.q > e0.q ? "Output up, " : "Output down, ") + (e.p > e0.p ? "prices up" : "prices down");
  $("#tv").textContent = `${n}: this changes ${comp}, so AD shifts ${a > 0 ? "right" : "left"} at every price level. In the short run real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 0)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 0)} (from 50 each), using an upward-sloping SRAS curve.`;
  $("#labB").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 }, { lras: false });
}
$("#evB").innerHTML = EVA.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showA(+b.dataset.i)));
showA(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which component of AD changes?", ["Consumption (C)", "Investment (I)", "Government spending (G)", "Net exports (X − M)"],
  [("Households spend more after an income tax cut", 0), ("A firm buys new machinery", 1), ("The state builds a new hospital", 2), ("Foreign buyers purchase more of the country's cars", 3), ("Consumer confidence falls", 0), ("Business confidence rises", 1), ("The currency depreciates", 3), ("The government employs more teachers", 2)],
  "C: households. I: firms' capital. G: government. X − M: trade.") + MATCH([
  ["Aggregate demand", "Total planned spending on an economy's output at each price level"],
  ["Wealth effect", "A lower price level raises the real value of savings"],
  ["Shift of AD", "A change in a component at every price level"],
  ["Movement along AD", "Caused only by a change in the price level"],
  ["Net exports", "Exports minus imports"],
  ["Interest rate effect", "A lower price level lowers interest rates and raises spending"]]) + ORDER(
  "Put the effect of lower interest rates on output in order.",
  ["The central bank cuts interest rates", "Borrowing becomes cheaper", "Consumption and investment rise", "The AD curve shifts to the right", "Real output rises and the price level may rise"],
  "Lower rates raise C and I, shifting AD right.") + CALC([
  {"q": "C = 400, I = 120, G = 150, X = 130, M = 140. What is AD ($bn)?", "a": 660, "unit": "$bn", "tol": 0.5, "hint": "400 + 120 + 150 + 130 − 140.", "sol": "<b>$660bn</b>."},
  {"q": "In the same economy, what are net exports ($bn)? (use a minus sign for a deficit)", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "130 − 140.", "sol": "<b>−$10bn</b>, a deficit."},
  {"q": "Investment rises by $30bn. What is the new AD ($bn)?", "a": 690, "unit": "$bn", "tol": 0.5, "hint": "660 + 30.", "sol": "<b>$690bn</b>."},
  {"q": "What is the percentage rise in AD (to one decimal place)?", "a": 4.5, "unit": "%", "tol": 0.1, "hint": "30 ÷ 660.", "sol": "<b>4.5%</b>."}]) + MCQ([
  ("AD equals:", ["C + I + G + (X − M)", "C + S + T", "I + G + X", "C − I − G"], 0, "The four components."),
  ("A fall in the price level causes:", ["A movement along AD", "A leftward shift of AD", "A rightward shift of AD", "A fall in G"], 0, "Only the price level moves along the curve."),
  ("Which would shift AD to the right?", ["A fall in interest rates", "A rise in income tax", "An appreciation", "A cut in government spending"], 0, "Cheaper borrowing."),
  ("Imports are:", ["Subtracted in AD", "Added in AD", "Part of G", "Part of C only"], 0, "They are spending that leaks abroad."),
  ("A fall in consumer confidence would:", ["Shift AD left", "Shift AD right", "Shift AS right", "Shift LRAS"], 0, "Consumption falls.")
], "qz1") + CARDS([
  ("AD", "C + I + G + (X − M)."),
  ("Slope", "Wealth, interest, trade effects."),
  ("Shift right", "Lower rates, lower taxes, confidence."),
  ("Shift left", "Higher rates, cuts, appreciation."),
  ("Movement along", "Price level only."),
  ("Not in G", "Transfer payments."),
  ("Net exports", "X − M."),
  ("Effect", "Depends on the AS curve.")]) + MCQ(mc_exam)

build("as43", "as-aggregate-demand", "Aggregate Demand", EY,
  "4.3.1 to 4.3.5: aggregate demand and its components, the shape of the AD curve, and the causes of shifts in AD. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
