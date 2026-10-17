"""AS syllabus 4.6.4 Causes of inflation: demand-pull and cost-push. Run: python3 tools/artifact-kit/mk_as4b.py"""
from asx import *
EY = EYAS("4.6.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Demand-pull inflation</b> is caused by a <b>rise in aggregate demand</b> that is not matched by a rise in aggregate supply, so the <b>AD curve shifts right</b> and the price level rises; it is most likely when the economy is <b>near full capacity</b>. <b class="kw">Cost-push inflation</b> is caused by a <b>rise in firms' costs</b> (wages above productivity, raw materials, energy, import prices after a depreciation, indirect taxes), so the <b>SRAS curve shifts left</b>, raising the price level and <b>reducing output</b>. The two can feed each other in a <b>wage-price spiral</b>, where higher prices lead to wage demands, which raise costs and prices again. Identify the type by the <b>curve that shifts</b>: if output rises with prices, it is likely demand-pull; if output falls while prices rise, it is cost-push.</p></div>

  <h2>1 · Demand-pull inflation (4.6.4)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Cause:</b> a rise in C, I, G or X, or a fall in M: lower interest rates, tax cuts, higher confidence, a boom in exports, rapid growth in the money supply, a depreciation that raises net exports.</li>
    <li><b>Diagram:</b> AD shifts right along SRAS; output and the price level both rise. The nearer to full capacity (or LRAS), the more the effect is on <b>prices</b> rather than output.</li>
    <li>With spare capacity, a rise in AD is mainly <b>growth</b>; at full employment it is mainly <b>inflation</b>.</li>
  </ul>

  <h2>2 · Cost-push inflation</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Cause:</b> a rise in the costs of production: <b>wage rises</b> larger than productivity growth, higher <b>raw material or energy prices</b>, a <b>depreciation</b> that makes imported inputs dearer, higher <b>indirect taxes</b>, labour shortages, supply disruptions.</li>
    <li><b>Diagram:</b> SRAS shifts left; the price level rises and real output falls: <b>stagflation</b> (inflation with stagnant growth and rising unemployment).</li>
    <li><b>Wage-price spiral:</b> workers demand higher pay to match prices, raising costs, raising prices again.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Demand-pull</th><th>Cost-push</th></tr>
    <tr><td><b>Shift</b></td><td>AD right</td><td>SRAS left</td></tr>
    <tr><td><b>Real output</b></td><td>Rises</td><td>Falls</td></tr>
    <tr><td><b>Unemployment</b></td><td>Falls</td><td>Rises</td></tr>
    <tr><td><b>Examples of causes</b></td><td>Lower interest rates, tax cuts, higher government spending, export boom</td><td>Oil price shock, wage rises above productivity, depreciation, higher indirect taxes</td></tr>
    <tr><td><b>Which is worse?</b></td><td>Depends on capacity; usually shows a strong economy</td><td>Often worse: prices rise while output falls</td></tr>
  </table></div>

  <h2>3 · Worked example: identifying the type of inflation</h2>
  <p>Take AD as P = 120 − Y and SRAS as P = 20 + Y. Equilibrium is Y = 50, P = 70.</p>
  <div class="tw"><table class="t">
    <tr><th>Event</th><th>Curve shift</th><th>New equilibrium</th><th>Type of inflation</th></tr>
    <tr><td>Lower interest rates raise AD</td><td>AD: P = 140 − Y</td><td>Y = 60, P = 80</td><td><b>Demand-pull</b>: output up 10, prices up 10 (14%)</td></tr>
    <tr><td>An oil price rise raises costs</td><td>SRAS: P = 40 + Y</td><td>Y = 40, P = 80</td><td><b>Cost-push</b>: output down 10, prices up 10 (14%)</td></tr>
    <tr><td>Both happen together</td><td>AD: P = 140 − Y, SRAS: P = 40 + Y</td><td>Y = 50, P = 90</td><td>Both: output unchanged, prices up 20 (29%)</td></tr>
  </table></div>
  <ul>
    <li>The price rise is the same in the first two rows, but <b>output moves in opposite directions</b>. Output and unemployment tell you which type it is.</li>
    <li>Near full capacity (potential output), the AD rise in row 1 would raise prices by more and output by less.</li>
  </ul>

  <h2>4 · Causes in more detail</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Cause</th><th>Why it raises prices</th></tr>
    <tr><td><b>Demand-pull</b></td><td>Lower interest rates, easy credit</td><td>Spending rises faster than capacity</td></tr>
    <tr><td><b>Demand-pull</b></td><td>Tax cuts, higher government spending</td><td>Households and the state demand more output</td></tr>
    <tr><td><b>Demand-pull</b></td><td>Export boom or a depreciation</td><td>Net exports rise, adding to AD</td></tr>
    <tr><td><b>Demand-pull</b></td><td>Rapid growth in the money supply</td><td>More money chasing the same goods</td></tr>
    <tr><td><b>Cost-push</b></td><td>Wage rises above productivity</td><td>Unit labour costs rise</td></tr>
    <tr><td><b>Cost-push</b></td><td>Raw material and energy prices</td><td>Production costs rise</td></tr>
    <tr><td><b>Cost-push</b></td><td>Depreciation of the currency</td><td>Imported inputs and goods cost more</td></tr>
    <tr><td><b>Cost-push</b></td><td>Higher indirect taxes or regulation</td><td>Firms' costs rise</td></tr>
    <tr><td><b>Cost-push</b></td><td>Labour or supply shortages</td><td>Firms bid up wages and input prices</td></tr>
  </table></div>

  <h2>5 · How wages can cause both types</h2>
  <ul>
    <li><b>Cost-push:</b> a pay rise raises firms' costs, so SRAS shifts left.</li>
    <li><b>Demand-pull:</b> workers with more pay spend more, so AD shifts right.</li>
    <li>If wages rise faster than productivity, the result is a higher price level. If workers then demand more to keep up with prices, a <b>wage-price spiral</b> develops.</li>
  </ul>

  <h2>6 · Expectations and the role of the money supply</h2>
  <ul>
    <li><b>Inflation expectations:</b> if people expect prices to rise, they bring forward purchases (raising AD) and demand higher wages (raising costs), so expected inflation tends to become real.</li>
    <li><b>Money supply:</b> if the money supply grows faster than output, there is more money chasing the same goods, which raises prices. Persistent high inflation is usually linked to rapid growth of the money supply.</li>
    <li><b>Imported inflation:</b> higher world prices for oil or food raise costs. A weak currency makes it worse.</li>
  </ul>

  <h2>7 · Which type is more likely, and how should policy respond?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Demand-pull</th><th>Cost-push</th></tr>
    <tr><td><b>More likely when</b></td><td>The economy is near full capacity and AD is strong</td><td>Costs rise sharply, as in an energy shock or after a depreciation</td></tr>
    <tr><td><b>Best policy</b></td><td>Contractionary fiscal or monetary policy to reduce AD</td><td>Supply-side policy to lower costs; contractionary policy would also cut output</td></tr>
    <tr><td><b>Cost of the policy</b></td><td>Lower growth and higher unemployment for a time</td><td>Slow results for supply-side policy; reducing AD may deepen a downturn</td></tr>
  </table></div>
  <div class="warn"><b class="h">Do not write this</b>Do not draw inflation with demand and supply for one good: use the price level and real output on the axes of an AD/AS diagram. Do not say a shift of AD to the left causes cost-push inflation. Do not forget that a single event can affect both AD and AS.</div>
  <div class="tip"><b class="h">Exam tip</b>Draw <b>AD/AS</b> diagrams with general price level and real output on the axes, and <b>not</b> supply and demand for one product. Give a specific cause, explain how it moves a curve, and state the effect on the price level.</div>
'''

watch = '''
  <h2>1 · Demand-pull inflation</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · Cost-push inflation and the wage-price spiral</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · What caused it?</h2>
  <p>Choose a cause. The diagram shows which curve shifts and the effect on the price level.</p>
  <div class="card"><div class="grid2"><div><div id="evB" class="btnrow"></div>
    <div class="readout"><div><small>Type</small><strong id="r1"></strong></div><div><small>Price level</small><strong id="r2"></strong></div><div><small>Real output</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with the curve for the chosen cause shifted"></svg></div></div></div>

  <h2>Lab 2 · Demand or cost?</h2>
  <p>Shift AD and SRAS by different amounts and see which type of inflation dominates.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Price level change</small><strong id="t1"></strong></div><div><small>Output change</small><strong id="t2"></strong></div><div><small>Main cause</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS both shifted"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Demand-pull or cost-push?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the wage-price spiral in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("An oil price spike", "A jump in world oil prices raises the cost of transport and production in an oil-importing country. SRAS shifts left, so prices rise while output and employment fall: cost-push inflation and stagflation.", "cost-push inflation from higher input prices.") +
rw("A consumer boom", "Low interest rates and rising house prices make households confident and they spend more. AD rises faster than capacity, so firms raise prices: demand-pull inflation.", "demand-pull inflation from rising consumption.") +
rw("A weak currency", "When the currency depreciates, imports cost more, raising the costs of firms that rely on imported inputs (cost-push), while exports become cheaper and demand rises (demand-pull). Both curves can shift.", "a depreciation causing both types of inflation.") +
rw("Wage-price spiral", "Prices rise 6%, so unions demand 6% pay rises. Firms pass the higher costs on in higher prices, workers demand more, and inflation becomes embedded.", "a cost-push spiral.") +
rw("An energy price shock", "Oil and gas prices double. Transport and production costs rise across industries, SRAS shifts left, and consumers face both higher prices and weaker output: cost-push inflation.", "cost-push inflation and stagflation.") +
rw("A consumer boom", "Cheap credit and tax cuts boost spending. Firms cannot raise output fast enough, so they raise prices instead: demand-pull inflation.", "demand-pull inflation near capacity.")
)

mc_exam = [
  mcq("m24_12", 16, "What is least likely to cause a simultaneous increase in demand-pull and cost-push inflation?", ["depreciation of currency", "increased import tariffs", "decreased spending on infrastructure", "increased wages"], 2, "Less spending on infrastructure reduces AD, so is least likely to cause either. Depreciation, tariffs and wage rises can raise both demand and costs."),
  mcq("m23_12", 20, "In an economy, wages and prices are both rising but wages are rising faster. Which features are likely to exist in this economy? (cost-push inflation, rise in real incomes)", ["no, no", "no, yes", "yes, no", "yes, yes"], 3, "Rising wages raise costs (cost-push), and wages rising faster than prices means real incomes are rising."),
  mcq("s21_11", 27, "What would be likely to increase inflation in an economy?", ["an increase in consumer saving", "an increase in interest rates", "an increase in labour productivity", "an increase in taxes on imports"], 3, "Taxes on imports raise the cost of imported inputs, shifting SRAS left. Saving, higher rates and productivity reduce inflation."),
  mcq("s21_12", 22, "What is correct about the causes of inflation?", ["Cost-push inflation can be caused by a rising exchange rate", "Cost-push inflation can be caused by lower indirect taxes", "Demand-pull inflation can be caused by a rising exchange rate", "Demand-pull inflation can be caused by lower direct taxes"], 3, "Lower direct taxes raise disposable income and consumption, so AD rises."),
  mcq("m20_12", 20, "An appreciation of the South African rand in the foreign exchange markets is most likely to assist the South African government achieve which policy objective?", ["a redistribution of income", "a reduction in the rate of inflation", "a reduction in the volume of imports", "an increase in the level of employment"], 1, "A stronger rand makes imports cheaper, reducing costs and inflation.")
]

exam = exam_page("the causes of inflation",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Demand-pull and cost-push inflation are an 8 mark Paper 2 part in most series (with diagrams) and short 6 mark data-response parts. Reworded past questions are below, with five Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "4", "May/June 2023 (21) Q4(a); Oct/Nov 2021 (22) Q4(a); Feb/March 2020 (22) Q4(a); May/June 2022 (23) Q3(a)"), ("Data response, 6 marks", "2", "May/June 2022 (21) Q1(d); Feb/March 2023 (22) Q1(d)"), ("Multiple choice (Paper 1)", "5 shown below", "2020 to 2024")],
  [
  eq(P("s23_21", "4(a)"), "8 marks", "With the help of an AD/AS diagram, explain cost-push inflation and demand-pull inflation in an economy and consider in what circumstances one may be more damaging than the other.",
     ["Knowledge (up to 3): an accurate diagram with correctly labelled axes of price level and real output (1), cost-push inflation shown by a leftward shift of AS (1) and demand-pull inflation shown by a rightward shift of AD (1).",
      "Analysis (up to 3): using the diagram to explain the possible damaging effects of cost-push inflation (up to 2) and of demand-pull inflation (up to 2), maximum 3.",
      "Evaluation (up to 2): a valid judgement on the comparison, including the factors that could make one cause more damaging than the other (1), and a conclusion (1)."],
     "Diagram: AS left (cost-push), AD right (demand-pull). Effects: cost-push: price up, output down. Demand-pull: price up, output up until capacity. Judge.",
     [[("k", "On an AD/AS diagram with the price level and real output on the axes, cost-push inflation is shown by a leftward shift of the SRAS curve, and demand-pull inflation by a rightward shift of the AD curve.")], [("n", "Cost-push inflation raises the price level while real output falls, which can mean falling employment as well as rising prices: stagflation. Demand-pull inflation raises the price level but also raises output and employment at first, though if the economy is at full capacity it only raises prices and may harm competitiveness and savers.")], [("e", "Cost-push inflation is probably more damaging when it comes with falling output and rising unemployment, since the economy gets worse in two ways. Demand-pull inflation can be more damaging if the economy is already at full capacity and the inflation becomes persistent, so it depends on the position of the economy.")]]),
  eq(P("w21_22", "4(a)"), "8 marks", "Explain what is meant by inflation and, using diagrams, show how it can arise both as a result of a shift in the aggregate demand curve and a shift in the aggregate supply curve.",
     ["Knowledge (up to 2): inflation defined as a continuous or sustained rise (1) in the general or average level of prices (1).",
      "Application (up to 3): a diagram showing inflation caused by a rightward shift of AD, with an explanation of why AD might increase (1), an accurately labelled diagram showing the rightward shift and rise in the general price level (1), and a clear explanation that inflation occurs due to excess aggregate demand (1).",
      "Application (up to 3): a diagram showing inflation caused by a leftward shift of AS, with an explanation of why AS may fall, such as higher costs or taxes, and the resulting rise in the general price level. Micro (supply and demand) diagrams are not rewarded."],
     "Inflation: sustained rise in general price level. AD diagram with a cause (e.g. lower interest rates). AS diagram with a cause (e.g. higher costs).",
     [[("k", "Inflation is a sustained rise in the general level of prices. On an AD/AS diagram, the price level is on the vertical axis and real output on the horizontal axis.")], [("n", "Lower interest rates make borrowing cheaper, so consumption and investment rise and AD shifts to the right. The price level rises along SRAS, and inflation results from this excess demand. If firms' costs rise, for example because oil prices increase, SRAS shifts left and the price level rises again, even though demand has not increased.")]]),
  eq(P("m20_22", "4(a)"), "8 marks", "Explain, using aggregate demand and aggregate supply diagrams, the distinction between cost-push inflation and demand-pull inflation and explain one cause of each.",
     ["Cost-push inflation: an accurately labelled diagram showing a shift left of the aggregate supply curve (2) and up to 2 marks for an explanation of one cause, such as a decline in the exchange rate that raises the price of imported raw materials or a rise in wage rates above increases in productivity.",
      "Demand-pull inflation: an accurately labelled diagram showing a shift right of the aggregate demand curve (2) and up to 2 marks for an explanation of one cause, such as increased exports or increased government spending."],
     "Two diagrams. Cost-push: SRAS left, cause: depreciation or wages. Demand-pull: AD right, cause: exports or government spending.",
     [[("k", "Cost-push inflation is shown by a leftward shift of SRAS, which raises the price level and lowers real output. A depreciation of the currency is one cause: imported raw materials become dearer, raising firms' costs at every level of output.")], [("n", "Demand-pull inflation is shown by a rightward shift of AD, which raises the price level and output. Higher government spending is one cause: it adds to AD, and if the economy is near full capacity, firms respond mainly by raising prices.")]]),
  eq(P("s22_21", "1(d)"), "6 marks", "Analyse, with the help of AD/AS diagrams, how increasing wages can cause both demand-pull and cost-push inflation.",
     ["Demand-pull (up to 3): an analysis of demand-pull inflation from wage increases (1), such as greater consumer spending and confidence from higher incomes; an AD/AS diagram showing AD shifting right, labelled correctly (1) and the shift to the right with the rise in the price level (1).",
      "Cost-push (up to 3): an analysis of cost-push inflation from wage increases not linked to higher productivity (1); an AD/AS diagram showing AS shifting left (up to 2): correct labelling (1) and the shift left showing the rise in the price level (1)."],
     "Higher wages: more income and spending (AD right, demand-pull). Higher wages: higher costs (AS left, cost-push). Two diagrams.",
     [[("n", "Higher wages raise households' incomes, so consumption increases and the AD curve shifts to the right, which raises the price level: demand-pull inflation. Higher wages also raise firms' costs of production, especially if not matched by productivity, so the SRAS curve shifts to the left, which raises the price level again: cost-push inflation. Each is shown on its own AD/AS diagram with the price level and real output on the axes.")]]),
  eq(P("s22_23", "3(a)"), "8 marks", "Explain the difference between cost-push and demand-pull inflation.",
     ["Knowledge (up to 2): inflation is a sustained or persistent rise (1) in the general or average price level (1).",
      "Application (up to 6): what is meant by cost-push inflation (1), an appropriate example of a cause (1) and why it causes inflation (1); what is meant by demand-pull inflation (1), an appropriate example of a cause (1) and why this differs from cost-push (1)."],
     "Define inflation. Cost-push: costs rise, SRAS left (wages, raw materials). Demand-pull: AD rises faster than AS (spending, tax cuts, exports).",
     [[("k", "Inflation is a sustained rise in the general price level.")], [("n", "Cost-push inflation is caused by a rise in firms' costs of production, such as higher raw material prices or wages that rise faster than productivity. SRAS shifts left, so the price level rises while output falls. Demand-pull inflation is caused by a rise in aggregate demand that is not matched by a rise in aggregate supply, for example after a cut in taxes or an export boom. AD shifts right, so the price level and output both rise, particularly strongly if the economy is close to full employment.")]]),
  eq(P("m23_22", "1(d)"), "6 marks", "With the help of an AD/AS diagram, assess whether a rising inflation rate has been caused by changes to the demand side or changes to the supply side of the economy.",
     ["Analysis (up to 4): an AD/AS diagram with correctly labelled axes (price level and real GDP) (1) showing AD moving right and SRAS moving left with a rise in the price level (1); an explanation of how the rise in inflation may be caused by an increase in aggregate demand (1) and a decrease in aggregate supply (1).",
      "Evaluation (up to 2): relevant evaluation that considers both AD and AS and weighs up the factors in each; a justified conclusion on the extent to which inflation has been caused by the demand side or the supply side, which may be a combination of both."],
     "Diagram: AD right and SRAS left. Demand: stimulus, low rates. Supply: energy and supply costs. Judge: usually a combination; evidence needed.",
     [[("n", "On an AD/AS diagram with the price level and real GDP on the axes, AD shifts right and SRAS shifts left, so the price level rises. Higher AD could come from government stimulus and low interest rates, which raise spending. A fall in SRAS could come from higher energy and shipping costs. Both raise the price level."), ("e", "Inflation is likely to have been caused by both. Which is more important depends on the evidence: if output has also fallen, supply-side causes are more likely; if output and spending have risen strongly, demand is more likely.")]])
  ],
  )

tips = tips_html(
  [("Use AD/AS diagrams.", "Price level and real output, not a single market."),
   ("Demand-pull: AD right.", "Output and prices both rise."),
   ("Cost-push: SRAS left.", "Prices rise, output falls."),
   ("Give a cause and explain it.", "Name the cost or the spending change."),
   ("Mention capacity.", "Demand-pull is more inflationary near full capacity."),
   ("Mention the spiral.", "Wages and prices can chase each other."),
   ("Compare which is more damaging.", "Stagflation is often worse.")],
  [("Demand-pull", "Demand-pull inflation is caused by a rise in aggregate demand not matched by supply."),
   ("Cost-push", "Cost-push inflation is caused by a rise in firms' costs shifting SRAS to the left."),
   ("Stagflation", "Stagflation is rising prices with falling output."),
   ("Wage-price spiral", "A wage-price spiral raises costs and prices repeatedly."),
   ("Capacity", "The effect depends on how close the economy is to full capacity.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
function dpDraw(s) { return adasPlot({ a: s.a, s: s.s, l: 0, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rightward shift of AD raises the price level and output">${dpDraw({ a: 20, s: 0, n: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A leftward shift of SRAS raises the price level and lowers output">${dpDraw({ a: 0, s: -20, n: 1 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 300, label: "Demand-pull inflation", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>A rise in AD.</b> Lower interest rates raise consumption and investment, shifting AD to the right. The price level rises to about 58 and output rises: <b>demand-pull inflation</b>.", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>A larger rise in AD</b> pushes the price level up further, and nearer to potential output (the LRAS) the effect is increasingly on prices rather than output.", s: { a: 35, s: 0, n: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Cost-push inflation and a wage-price spiral", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>A rise in costs</b> (oil prices, wages above productivity) shifts SRAS left. The price level rises to about 58 and output falls: <b>cost-push inflation</b> and stagflation.", s: { a: 0, s: -20, n: 1 } },
  { cap: "<b>The spiral.</b> Workers demand higher wages to keep up with prices. Higher wages raise costs (SRAS shifts left again) and also raise spending (AD shifts right): prices rise further and inflation becomes embedded.", s: { a: 15, s: -35, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
const CAU = [["Lower interest rates", 20, 0, "Demand-pull"], ["Tax cuts raise incomes", 15, 0, "Demand-pull"], ["Export boom", 20, 0, "Demand-pull"], ["Higher government spending", 20, 0, "Demand-pull"], ["Oil price rise", 0, -20, "Cost-push"], ["Wages rise faster than productivity", 0, -15, "Cost-push"], ["Higher indirect taxes", 0, -15, "Cost-push"], ["Depreciation raises import costs", 8, -12, "Both (mainly cost-push)"]];
function showC(i) {
  const [n, a, s, t] = CAU[i], e = sdEq(a, s), e0 = sdEq(0, 0); $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#r1").textContent = t; $("#r2").textContent = (e.p > e0.p ? "Up to " : "Down to ") + Lib.fmtN(e.p, 1); $("#r3").textContent = (e.q > e0.q ? "Up to " : "Down to ") + Lib.fmtN(e.q, 1);
  $("#rv").textContent = `${n}: ${a > 0 && s < 0 ? "AD shifts right (higher export demand) and SRAS shifts left (dearer imported inputs)" : a > 0 ? "AD shifts right" : "SRAS shifts left"}. The price level rises from 50 to ${Lib.fmtN(e.p, 1)} and real output ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 1)}: ${t.toLowerCase()} inflation.`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1 }, { lras: false });
}
$("#evB").innerHTML = CAU.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showC(+b.dataset.i)));
showC(0);

/* ---------- Lab 2 ---------- */
function labT() {
  if (!["ad", "sr"].every((i) => $("#" + i))) return;
  const a = +$("#ad").value, s = +$("#sr").value, e = sdEq(a, s), pc = (e.p - 50) / 50 * 100, qc = (e.q - 50) / 50 * 100, dp = 0.4 * a, cp = -0.4 * s;
  $("#t1").textContent = (pc >= 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%"; $("#t2").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#t3").textContent = pc <= 0.5 ? "Little inflation" : dp > cp * 1.3 ? "Demand-pull" : cp > dp * 1.3 ? "Cost-push" : "Both";
  $("#tv").textContent = `The AD shift adds about ${Lib.fmtN(dp / 50 * 100, 1)} points to the price level and the SRAS shift ${Lib.fmtN(cp / 50 * 100, 1)} points. Price level ${Lib.fmtN(pc, 1)}%, real output ${Lib.fmtN(qc, 1)}%. ${qc > 1 ? "Output rises with prices: more like demand-pull." : qc < -1 ? "Output falls as prices rise: more like cost-push (stagflation)." : "Output is roughly unchanged."}`;
  $("#labB").innerHTML = adasPlot({ a, s, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "ad", label: "AD shift (positive = right) ", min: -20, max: 40, step: 5, value: 15, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "sr", label: "SRAS shift (negative = left, costs rising) ", min: -30, max: 20, step: 5, value: -15, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Demand-pull or cost-push?", ["Demand-pull", "Cost-push"],
  [("A cut in interest rates raises spending", 0), ("A rise in oil prices", 1), ("An export boom", 0), ("Wages rise faster than productivity", 1), ("A cut in income tax", 0), ("A rise in indirect taxes on firms", 1), ("Government spending rises near full capacity", 0), ("A depreciation raises the price of imported raw materials", 1)],
  "Demand-pull: AD shifts right. Cost-push: SRAS shifts left.") + MATCH([
  ["Demand-pull inflation", "AD rises faster than AS"],
  ["Cost-push inflation", "Higher costs shift SRAS left"],
  ["Stagflation", "Rising prices with falling output"],
  ["Wage-price spiral", "Higher prices lead to higher wages, then higher prices"],
  ["Full capacity", "Output cannot rise, so extra demand raises prices"],
  ["Depreciation", "Can raise import costs and export demand"]]) + ORDER(
  "Put the wage-price spiral in order.",
  ["Prices rise", "Workers demand higher wages", "Firms' costs rise", "Firms raise prices again", "Inflation becomes embedded"],
  "Prices lead to wages, which lead to prices again.") + CALC([
  {"q": "The price level index rises from 100 to 108 after AD shifts right and output rises 2%. What is the inflation rate (%)?", "a": 8, "unit": "%", "tol": 0.1, "hint": "8 ÷ 100.", "sol": "<b>8%</b>."},
  {"q": "After a cost shock the price level rises from 100 to 106 and output falls from 500 to 485. What is the % fall in output?", "a": 3, "unit": "%", "tol": 0.1, "hint": "15 ÷ 500.", "sol": "<b>3%</b>."},
  {"q": "In the second case, are output and prices moving in the same direction (yes = 1, no = 0)?", "a": 0, "unit": "", "tol": 0.1, "hint": "Prices up, output down.", "sol": "<b>No (0)</b>: stagflation, a sign of cost-push."},
  {"q": "A firm's wage bill is 60% of costs and wages rise 5% with no productivity gain. By how much do its costs rise (%)?", "a": 3, "unit": "%", "tol": 0.1, "hint": "0.6 × 5.", "sol": "<b>3%</b>."}]) + MCQ([
  ("Demand-pull inflation is shown by:", ["A rightward shift of AD", "A leftward shift of SRAS", "A rightward shift of LRAS", "A fall in AD"], 0, "AD rises."),
  ("Cost-push inflation is shown by:", ["A leftward shift of SRAS", "A rightward shift of AD", "A rightward shift of SRAS", "A fall in costs"], 0, "Higher costs."),
  ("Stagflation means:", ["Rising prices and falling output", "Falling prices and rising output", "Rising prices and rising output", "Falling prices and falling output"], 0, "Cost-push."),
  ("Which could cause cost-push inflation?", ["Higher oil prices", "A cut in interest rates", "A rise in exports", "A tax cut"], 0, "Raises costs."),
  ("Extra AD is most likely to cause only inflation when:", ["The economy is at full capacity", "There is much spare capacity", "Unemployment is high", "SRAS is flat"], 0, "Output cannot rise.")
], "qz1") + CARDS([
  ("Demand-pull", "AD right."),
  ("Cost-push", "SRAS left."),
  ("Stagflation", "Prices up, output down."),
  ("Spiral", "Wages and prices chase."),
  ("Capacity", "Near full: inflationary."),
  ("Diagram", "AD/AS, general price level."),
  ("Cause", "Name and explain."),
  ("Compare", "Which is worse?")]) + MCQ(mc_exam)

build("as4b", "as-causes-of-inflation", "Causes of Inflation: Demand-Pull and Cost-Push", EY,
  "4.6.4: demand-pull and cost-push inflation shown with AD/AS diagrams, their causes, and the wage-price spiral. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
