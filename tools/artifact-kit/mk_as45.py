"""AS syllabus 4.3.11-4.3.12 AD/AS equilibrium and the effects of shifts. Run: python3 tools/artifact-kit/mk_as45.py"""
from asx import *
EY = EYAS("4.3.11 to 4.3.12")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Macroeconomic equilibrium</b> is where <b>aggregate demand equals short-run aggregate supply</b>, and it determines the <b>level of real output</b> (and so employment) and the <b>price level</b>; <b>long-run equilibrium</b> is where AD, SRAS and LRAS all meet, so output is at <b>potential</b>. A <b>shift of AD to the right</b> raises real output, employment and the price level (and left does the opposite); a <b>shift of SRAS to the left</b> raises the price level and lowers output and employment (<b>stagflation</b>); a <b>shift of SRAS or LRAS to the right</b> raises output and lowers the price level. How the effect splits between <b>output and prices</b> depends on the shape of AS and on the <b>spare capacity</b>: with much spare capacity extra demand mainly raises output, near full capacity it mainly raises prices. When output is below potential there is a <b>negative output gap</b> and unemployment; above it, an <b>inflationary gap</b>.</p></div>

  <h2>1 · Equilibrium (4.3.11)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Short-run equilibrium:</b> AD = SRAS gives the <b>price level</b> and <b>real output</b>. More output means more labour demanded, so <b>employment</b> is higher where output is higher.</li>
    <li><b>Long-run equilibrium:</b> AD = SRAS = LRAS, with output at <b>potential</b> (full employment).</li>
    <li>If equilibrium output is <b>below potential</b> (a <b>negative output gap</b>, recessionary gap) there is spare capacity and cyclical unemployment; if <b>above</b> potential (an <b>inflationary gap</b>), resources are overstretched and prices rise.</li>
  </ul>

  <h2>2 · The effects of shifts (4.3.12)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Shift</th><th>Real output (employment)</th><th>Price level</th></tr>
    <tr><td><b>AD right</b></td><td>Up</td><td>Up (little if lots of spare capacity)</td></tr>
    <tr><td><b>AD left</b></td><td>Down</td><td>Down (or fall only a little: prices are sticky)</td></tr>
    <tr><td><b>SRAS left</b> (costs rise)</td><td>Down</td><td>Up (cost-push, stagflation)</td></tr>
    <tr><td><b>SRAS right</b> (costs fall)</td><td>Up</td><td>Down</td></tr>
    <tr><td><b>LRAS right</b> (more capacity)</td><td>Up (higher potential)</td><td>Down</td></tr>
    <tr><td><b>AD and SRAS both right</b></td><td>Up</td><td>Uncertain</td></tr>
  </table></div>
  <ul>
    <li><b>Shape matters:</b> on the <b>flat</b> part of AS an AD rise increases output only; on the <b>sloping</b> part both rise; on the <b>vertical</b> part only prices rise (pure demand-pull inflation).</li>
    <li><b>Employment</b> is not shown on the diagram directly: infer it from output.</li>
  </ul>

  <h2>3 · Worked example: effects of shifts in numbers</h2>
  <p>Take AD as P = 120 − Y and SRAS as P = 20 + Y. Equilibrium is Y = 50, P = 70 and suppose potential output is 70.</p>
  <div class="tw"><table class="t">
    <tr><th>Shift</th><th>New curve</th><th>New equilibrium</th><th>Change in output and prices</th></tr>
    <tr><td><b>AD right</b> by 20</td><td>P = 140 − Y</td><td>Y = 60, P = 80</td><td>Output +10, prices +10</td></tr>
    <tr><td><b>AD left</b> by 20</td><td>P = 100 − Y</td><td>Y = 40, P = 60</td><td>Output −10, prices −10</td></tr>
    <tr><td><b>SRAS left</b> by 20</td><td>P = 40 + Y</td><td>Y = 40, P = 80</td><td>Output −10, prices +10</td></tr>
    <tr><td><b>SRAS right</b> by 20</td><td>P = Y</td><td>Y = 60, P = 60</td><td>Output +10, prices −10</td></tr>
  </table></div>
  <ul>
    <li>With equilibrium output of 50 and potential output of 70, there is a <b>negative output gap</b> of 20 (28.6% of potential), so spare capacity and cyclical unemployment exist.</li>
    <li>After AD shifts right, output of 60 is closer to potential: the output gap narrows to 10.</li>
  </ul>

  <h2>4 · Types of gap and what to do about them</h2>
  <div class="tw"><table class="t">
    <tr><th>Situation</th><th>Output compared with potential</th><th>Features</th><th>Policy response</th></tr>
    <tr><td><b>Negative (recessionary) output gap</b></td><td>Below potential</td><td>Spare capacity, high unemployment, low inflation</td><td>Raise AD (expansionary fiscal or monetary policy)</td></tr>
    <tr><td><b>At potential output</b></td><td>Equal</td><td>Full employment, stable prices</td><td>Maintain; use supply-side policy for growth</td></tr>
    <tr><td><b>Positive (inflationary) output gap</b></td><td>Above potential</td><td>Overheating, rising inflation, labour shortages</td><td>Reduce AD (contractionary policy)</td></tr>
  </table></div>

  <h2>5 · Using AD/AS analysis: a method</h2>
  <ul>
    <li><b>Step 1:</b> draw the original AD, SRAS (and LRAS if relevant) and label the equilibrium, price level and real output.</li>
    <li><b>Step 2:</b> identify the event and say which curve it moves and why (for example, a rise in oil costs moves SRAS).</li>
    <li><b>Step 3:</b> draw the new curve and equilibrium, and describe the change in real output, the price level and employment.</li>
    <li><b>Step 4:</b> evaluate: how big the effect is depends on spare capacity, the slope of AS, and whether other curves also move; also consider the time period and what policies might respond.</li>
  </ul>

  <h2>6 · Combining shifts</h2>
  <ul>
    <li><b>AD right and SRAS right</b> (for example, higher confidence and lower oil prices): output rises; the price level may rise, stay the same or fall, depending on which shift is larger.</li>
    <li><b>AD left and SRAS left</b> (for example, a world recession and higher costs): output falls; the price effect is uncertain.</li>
    <li><b>AD right and SRAS left</b>: the price level rises sharply; the effect on output is uncertain.</li>
    <li>Real examples nearly always have <b>more than one change at once</b>, so exam questions often ask for the net effect.</li>
  </ul>
  <div class="warn"><b class="h">Do not write this</b>Do not say that a rise in AD always causes inflation: with spare capacity it mainly raises output. Do not treat stagflation as demand-pull: it comes from SRAS shifting left. Do not forget to label the axes: the vertical axis is the price level and the horizontal axis is real output, not price and quantity.</div>
  <div class="tip"><b class="h">Exam tip</b>Always label the axes (price level, real output), the original and new curves and the new equilibrium, and state the change in <b>output, prices and employment</b>. Mention the <b>shape of AS</b> or <b>spare capacity</b> when judging how big each change is.</div>
'''

watch = '''
  <h2>1 · The same AD increase in three parts of the economy</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stZ"></div>
  <h2>2 · Shifts of AD and SRAS</h2>
  <div id="stX"></div>
'''

explore = '''
  <h2>Lab 1 · Shift AD and SRAS together</h2>
  <p>Move AD and SRAS by different amounts. LRAS (potential output) is at 75.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Real output</small><strong id="r1"></strong></div><div><small>Price level</small><strong id="r2"></strong></div><div><small>Output gap</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with both AD and SRAS shifted"></svg></div></div></div>

  <h2>Lab 2 · Where is the economy?</h2>
  <p>Move AD along a three-section AS curve and see how an increase splits between output and prices.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Real output</small><strong id="t1"></strong></div><div><small>Price level</small><strong id="t2"></strong></div><div><small>Zone</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="AD moving along a three-section aggregate supply curve"></svg></div></div></div>
'''

practise = '''
  <h2>1 · What happens to output and prices?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of an AD increase in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Recovery from a recession", "After a recession many workers and factories are idle. When AD recovers, output and employment rise strongly but prices rise only a little, because there is spare capacity.", "an AD increase on the flat part of AS.") +
rw("An economy at full capacity", "In a boom, factories are running flat out and unemployment is very low. More spending cannot raise output much, so it mostly raises prices.", "an AD increase on the vertical part of AS.") +
rw("Stagflation after an energy shock", "A sharp rise in energy prices raises costs. SRAS shifts left: prices rise while output and employment fall, a combination called stagflation.", "SRAS shifting left.") +
rw("Technology boosts supply", "New technology lowers costs and raises potential output. SRAS and LRAS shift right, so output rises and the price level can fall, even while AD is growing.", "SRAS and LRAS shifting right.") +
rw("A fall in oil prices", "Lower fuel costs reduce firms' costs, so SRAS shifts right. Output rises and the price level falls, a positive supply shock.", "a rightward shift of SRAS.") +
rw("A recession after a financial crisis", "Banks cut lending and households lose confidence. AD shifts left, so real output falls, unemployment rises and price rises slow or reverse.", "a leftward shift of AD and a negative output gap.")
)

mc_exam = [
  mcq("m20_12", 27, "In a closed economy a rise in aggregate demand is needed to increase output in the country. What is necessary to achieve this increase in output in the economy?", ["enough capacity to produce the extra goods and services demanded", "free trade to allow imports to make up any shortages in supply", "government spending to be less than tax revenue", "reduced credit to lower inflation"], 0, "Output can rise only if the economy has spare capacity to produce the extra goods and services."),
  mcq("s24_13", 16, "The diagram shows that when aggregate demand increases from AD1 to AD2 the average price level rises from P1 to P2, along a vertical LRAS curve. Which statement relating to this change in aggregate demand is correct?", ["Nominal GDP has increased", "Nominal GDP is unchanged", "Real GDP has increased", "Real GDP has fallen"], 0, "On a vertical LRAS, real GDP stays at its potential level while prices rise, so nominal GDP (output times price) rises."),
  mcq("s25_11", 16, "Which statement correctly describes an increase in real GDP?", ["Nominal GDP rising faster than nominal income", "Nominal GDP rising faster than the rate of inflation", "The rate of inflation rising faster than aggregate demand", "The rate of inflation rising faster than nominal income"], 1, "Real GDP rises when nominal GDP grows by more than the price level."),
  mcq("s25_11", 23, "A government uses expansionary monetary policy over a three-year period. Which combination identifies the likely impact of such a policy on real GDP, the price level and unemployment?", ["falling, rising, falling", "rising, rising, rising", "rising, rising, falling", "rising, falling, rising"], 2, "Expansionary policy shifts AD right, raising real GDP and the price level, so unemployment falls."),
  mcq("m23_12", 28, "What is least likely to rise as a result of the use of expansionary fiscal policy?", ["aggregate demand", "budget surplus", "nominal income", "inflation"], 1, "Higher spending or lower taxes raise AD, nominal income and inflation, but reduce any budget surplus."),
  mcq("s24_11", 20, "To counter deflation a central bank uses expansionary monetary policy. What is likely to result?", ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], 1, "Lower interest rates raise AD."),
  mcq("w20_12", 19, "Under which combination of circumstances will a policy of increasing the money supply be most effective at moving an economy out of recession? (circumstance one, circumstance two)", ["depreciating exchange rate, global financial crisis", "high nominal interest rates, appreciating exchange rate", "low aggregate demand, inflation rate above the target level", "low nominal interest rates, no spare capacity available"], 1, "High interest rates leave room to cut them, and a currency that appreciates is not the constraint, so more money supply can raise AD."),
  mcq("w21_11", 30, "The government wishes to increase aggregate demand. Which actions would be most likely to succeed?", ["a reduction in income tax and an increase in interest rates", "a reduction in income tax and an increase in production subsidies", "an increase in corporate tax and an increase in government spending", "an increase in value added tax and a reduction in government spending"], 1, "Lower income tax raises consumption, and subsidies boost production, raising spending.")
]

exam = exam_page("macroeconomic equilibrium and the effects of shifts",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). AD and AS analysis is used in Paper 2 parts of 6 and 8 marks nearly every series, and in a large share of Paper 1. Reworded past questions are below, with eight Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "2", "Feb/March 2024 (22) Q5(a); May/June 2024 (23) Q4(a)"), ("Data response, 6 marks", "2", "May/June 2021 (21) Q1(e); May/June 2020 (22) Q1(d)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("m24_22", "5(a)"), "8 marks", "With the help of an aggregate demand and aggregate supply diagram, explain how a decrease in interest rates could cause economic growth and consider whether economic growth will always result in inflation.",
     ["Knowledge (up to 3): a clear understanding of economic growth (1), inflation (1) and interest rates (1); an accurate diagram with labelled axes and equilibrium price level and real GDP (1).",
      "Analysis (up to 3): using the diagram to explain how a decrease in interest rates affects saving and borrowing (1), which causes an increase in consumption, investment or net exports (1), and so an increase in economic growth or real GDP (1).",
      "Evaluation (up to 2): a rise in inflation assumes that the economy is operating at full capacity; growth may be focused on capital intensive industries or its source may be long term (1), and a justified conclusion (1)."],
     "Define growth, inflation, interest rates. Diagram: lower rates raise C and I, AD right, output up. Inflation only if near full capacity.",
     [[("k", "Economic growth is an increase in real GDP, inflation is a sustained rise in the general price level, and the interest rate is the cost of borrowing and the reward for saving. On an AD/AS diagram the equilibrium is where AD meets SRAS at the price level P1 and real GDP Y1.")], [("n", "A lower interest rate reduces the reward for saving and the cost of borrowing, so households borrow and spend more and firms invest more. Consumption and investment are components of AD, so the AD curve shifts to the right and real GDP rises to Y2, which is economic growth.")], [("e", "Growth will not always result in inflation. If the economy has spare capacity, output rises with little change in prices, and if the growth comes from investment that raises capacity, AS also rises. Inflation is more likely when the economy is near full capacity.")]]),
  eq(P("s21_21", "1(e)"), "6 marks", "Using aggregate demand and aggregate supply analysis, discuss the possible impact on an economy of a sustained increase in its net exports.",
     ["Analysis (up to 3): an explanation of the potential advantages of a sustained increase in net exports using AD/AS analysis, such as a rise in AD, a rise in real output, incomes and employment, and a boost to the current account balance.",
      "Analysis (up to 3): an explanation of the potential disadvantages using AD/AS analysis, such as less being available for the domestic market and a rise in the rate of domestic inflation.",
      "Judgement (1): reserve 1 mark for a conclusion."],
     "Net exports up: AD right, output and employment up, current account improves. But prices may rise, goods diverted from home market. Conclude.",
     [[("n", "A sustained rise in net exports shifts AD to the right, because net exports are a component of AD. Real output and employment rise, and incomes increase, as well as the current account balance improving. But if the economy is near full capacity, the extra demand mainly pulls up the price level, so inflation could rise, and more output sold abroad may mean less available at home.")], [("e", "Overall the effect is likely to be beneficial if there is spare capacity, because output and jobs rise with little inflation. It may become a problem if capacity is limited, when prices rise.")]]),
  eq(P("s24_23", "4(a)"), "8 marks", "With the help of a diagram, explain how increases in aggregate demand affect the level of real output and the price level in an economy and consider when such increases may become a problem.",
     ["Knowledge (up to 3): the components of AD, C + G + I + X − M (1); an accurately labelled AD/AS diagram showing the initial equilibrium (1); a shift or shifts of the AD curve to the right and the resulting changes in the price level and real GDP (1).",
      "Analysis (up to 3): an explanation of why AD might increase (1); why this increase may not cause problems such as inflation, for example because of the shape of the AS curve or because AS may increase in line with AD if the increase is due to investment (1); why it may cause problems, for example if the economy is at full capacity and AS cannot increase (1).",
      "Evaluation (up to 2): a recognition that increases in AD may cause an inflationary rise in the price level beyond the full employment level of output, and a justified conclusion."],
     "Components and diagram. AD right: output and price level up. No problem with spare capacity; problem at full capacity: inflation. Judge.",
     [[("k", "Aggregate demand is C + I + G + (X − M). On an AD/AS diagram with price level and real output on the axes, a rise in AD shifts the AD curve to the right, so the equilibrium moves to a higher price level and higher real GDP.")], [("n", "AD might rise because of lower interest rates, which raise consumption and investment. If there is spare capacity, output can increase with little rise in prices, and if the increase is due to investment, AS may also rise. But if the economy is at full capacity, AS cannot rise, so the extra demand only raises the price level.")], [("e", "Increases in AD become a problem when they push output beyond the full employment level, creating inflation. Below full capacity they are likely to be beneficial.")]]),
  eq(P("s20_22", "1(d)"), "6 marks", "Use aggregate demand and aggregate supply analysis to explain how recent interest rate rises might help a country to reduce its annual rate of inflation and achieve its target.",
     ["Analysis: an explanation of how the interest rate rise might help to reduce inflation caused by demand-pull factors (up to 4 marks) and by cost-push factors (up to 4 marks); 2 marks are allowed for evaluative comment that the rise might exacerbate inflation. 6 marks maximum."],
     "Demand-pull: rate rise, C and I fall, AD left, price level falls. Cost-push: higher exchange rate, cheaper imports, SRAS right. Evaluate: higher rates raise firms' costs.",
     [[("n", "Higher interest rates make borrowing dearer and saving more attractive, so consumption and investment fall and AD shifts left, which reduces the price level and so demand-pull inflation. Higher rates may also raise the exchange rate, making imported raw materials cheaper, which lowers firms' costs, shifting SRAS right and reducing cost-push inflation."), ("e", "However, higher interest rates raise firms' borrowing costs, which could shift SRAS left and worsen cost-push inflation, so the policy might exacerbate inflation.")]])
  ],
  )

tips = tips_html(
  [("Equilibrium is AD = SRAS.", "Add LRAS for long-run equilibrium."),
   ("Label everything.", "Axes, curves, old and new equilibrium."),
   ("State output, prices and employment.", "All three changes."),
   ("Use the shape of AS.", "Flat: output. Sloping: both. Vertical: prices."),
   ("SRAS left is stagflation.", "Prices up, output and employment down."),
   ("Use the output gap.", "Spare capacity means growth with low inflation."),
   ("Judge with capacity.", "Will growth always cause inflation? Not if capacity exists.")],
  [("Equilibrium", "Macroeconomic equilibrium is where AD equals SRAS."),
   ("Output gap", "A negative output gap means actual output is below potential."),
   ("Stagflation", "A leftward shift of SRAS raises prices and cuts output."),
   ("Spare capacity", "With spare capacity an increase in AD may raise output more than prices."),
   ("Evaluation", "Growth will not always cause inflation.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- equilibrium picture ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with equilibrium output below potential output">${adasPlot({ a: 0, s: 0, l: 0, g: 1, n: 0 })}</svg>`;
function ex2(s) { return adasPlot({ a: s.a, s: s.s, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifts right and output and the price level rise">${ex2({ a: 20, s: 0, n: 1 })}</svg>`;
Lib.stepper($("#stX"), { w: 760, h: 300, label: "Shifts of AD and SRAS and their effects", base: { a: 0, s: 0, n: 0 }, draw: ex2, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50, below potential output (LRAS at 75): there is spare capacity.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>AD shifts right</b> (for example lower interest rates). Real output and employment rise and the price level rises: <b>demand-pull</b>.", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>SRAS shifts left</b> (costs rise). The price level rises and output falls: <b>stagflation</b>.", s: { a: 0, s: -20, n: 1 } },
  { cap: "<b>AD and SRAS both shift right.</b> Output rises for certain. The price level is uncertain: here AD rises more than SRAS, so prices rise slightly.", s: { a: 25, s: 15, n: 1 } },
] });

/* ---------- three-section AS ---------- */
const ASP = [[0, 14], [10, 15], [35, 18], [60, 35], [72, 65], [75, 100]];
const asf = (q) => { if (q > 75) return 1000; for (let i = 1; i < ASP.length; i++) if (q <= ASP[i][0]) { const [x0, y0] = ASP[i - 1], [x1, y1] = ASP[i]; return y0 + (y1 - y0) * (q - x0) / (x1 - x0); } return 100; };
function eqAS(c) { let q = 0; for (; q <= 75; q += 0.05) if (asf(q) >= c - 0.8 * q) break; q = Math.min(q, 75); return { q, p: Math.max(0, Math.min(c - 0.8 * q, 110)) }; }
function zoneOf(q) { return q < 40 ? "Flat: spare capacity" : q < 70 ? "Upward sloping" : "Vertical: full capacity"; }
function azDraw(s) {
  const e = eqAS(s.c); let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level");
  o += SV.path("M" + ASP.map(([q, p]) => SDX(q) + "," + SDY(p)).join(" L"), "c1", { fill: "none", "stroke-width": 3.5 }) + tag(SDX(75) + 8, SDY(95), "AS (three sections)", "c1");
  o += SV.line(SDX(0), SDY(s.c), SDX(Math.min(100, s.c / 0.8)), SDY(0), "c2", { "stroke-width": 3 }) + tag(SDX(Math.min(100, s.c / 0.8)) - 40, SDY(8), "AD", "c2");
  o += SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash") + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash") + SV.circle(SDX(e.q), SDY(e.p), 7, "dot3") + SV.text(SDX(e.q), 286, Lib.fmtN(e.q, 0), "sm", { "text-anchor": "middle" }) + SV.text(62, SDY(e.p) + 4, Lib.fmtN(e.p, 0), "sm", { "text-anchor": "end" });
  return o;
}
$("#pic1").innerHTML = $("#pic1").innerHTML;
Lib.stepper($("#stZ"), { w: 760, h: 300, label: "An AD increase on three parts of the AS curve", base: { c: 45 }, draw: azDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>Deep recession.</b> The economy is on the flat part of AS with plenty of spare capacity (output about 34, price level about 18).", s: { c: 45 } },
  { cap: "<b>AD rises on the flat part.</b> Output rises from about 34 to 43, while the price level rises only from about 18 to 24. Unemployment falls.", s: { c: 58 } },
  { cap: "<b>Normal conditions (sloping part).</b> Equilibrium output is 60 and the price level 35.", s: { c: 83 } },
  { cap: "<b>AD rises on the sloping part.</b> Output rises from 60 to about 65 and the price level from 35 to about 48: both rise.", s: { c: 100 } },
  { cap: "<b>Near full capacity.</b> AD rises on the vertical part: output can barely rise (about 74 at most) so the price level shoots up, to about 91. This is <b>demand-pull inflation</b>.", s: { c: 150 } },
] });

/* ---------- Lab 1 ---------- */
function labE() {
  if (!["ad", "sr"].every((i) => $("#" + i))) return;
  const a = +$("#ad").value, s = +$("#sr").value, e = sdEq(a, s), gap = 75 - e.q;
  $("#r1").textContent = Lib.fmtN(e.q, 1); $("#r2").textContent = Lib.fmtN(e.p, 1); $("#r3").textContent = gap > 0 ? "Spare capacity " + Lib.fmtN(gap, 1) : "Inflationary " + Lib.fmtN(-gap, 1);
  $("#rv").textContent = `AD shifts ${a > 0 ? "right" : a < 0 ? "left" : "not at all"} and SRAS ${s > 0 ? "right" : s < 0 ? "left" : "not at all"}. Real output is ${Lib.fmtN(e.q, 1)} (from 50) and the price level ${Lib.fmtN(e.p, 1)} (from 50). Output is ${gap > 0 ? Lib.fmtN(gap, 1) + " below potential (75), so there is spare capacity and unemployment" : "at or above potential output, so the economy is overheating and inflationary pressure builds"}. ${a * s > 0 ? "With both curves moving the same way one effect is certain (output), while the other depends on which shift is bigger." : ""}`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "ad", label: "AD shift (negative = left, positive = right) ", min: -30, max: 40, step: 5, value: 15, fmt: (v) => v, onInput: labE });
Lib.slider($("#g2"), { id: "sr", label: "SRAS shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labE });
labE();

/* ---------- Lab 2 ---------- */
function labZ() {
  if (!$("#cz")) return;
  const c = +$("#cz").value, e = eqAS(c), e0 = eqAS(c - 20), dq = e.q - e0.q, dp = e.p - e0.p;
  $("#t1").textContent = Lib.fmtN(e.q, 1); $("#t2").textContent = Lib.fmtN(e.p, 1); $("#t3").textContent = zoneOf(e.q);
  $("#tv").textContent = `Equilibrium output is ${Lib.fmtN(e.q, 1)} and the price level ${Lib.fmtN(e.p, 1)}: ${zoneOf(e.q).toLowerCase()}. A further rise in AD of 20 at this point would change output by ${Lib.fmtN(dq, 1)} and prices by ${Lib.fmtN(dp, 1)} (compared with the position at AD 20 lower): ${dq > dp * 0.5 && e.q < 70 ? "mostly output" : e.q >= 70 ? "mostly prices" : "both"}.`;
  $("#labB").innerHTML = azDraw({ c });
}
Lib.slider($("#g3"), { id: "cz", label: "Position of AD (higher = more demand) ", min: 45, max: 160, step: 5, value: 80, fmt: (v) => v, onInput: labZ });
labZ();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to real output and the price level?", ["Output up, price level up", "Output down, price level up", "Output up, price level down", "Output down, price level down"],
  [("AD shifts right", 0), ("SRAS shifts left", 1), ("SRAS shifts right", 2), ("AD shifts left", 3), ("Lower interest rates", 0), ("A rise in raw material prices", 1), ("Falling energy costs", 2), ("A fall in consumer confidence", 3)],
  "AD moves output and prices the same way; SRAS moves them in opposite ways.") + MATCH([
  ["Macroeconomic equilibrium", "Where AD equals short-run aggregate supply"],
  ["Negative output gap", "Actual output below potential output"],
  ["Stagflation", "Rising prices with falling output"],
  ["Demand-pull inflation", "Prices rise because AD rises when capacity is limited"],
  ["Potential output", "Output at full employment: LRAS"],
  ["Inflationary gap", "Actual output above potential output"]]) + ORDER(
  "Put the effect of an AD increase near full capacity in order.",
  ["AD shifts to the right", "Firms cannot raise output because resources are fully employed", "Competition for resources pushes up costs", "The price level rises", "Real output rises little or not at all"],
  "At full capacity extra demand is inflationary.") + CALC([
  {"q": "Equilibrium output is 880 and potential output is 1,000. What is the output gap (negative means spare capacity)?", "a": -120, "unit": "", "tol": 0.5, "hint": "880 − 1,000.", "sol": "<b>−120</b>, a negative output gap."},
  {"q": "Real GDP rises from 900 to 927 after AD shifts right. What is the % growth?", "a": 3, "unit": "%", "tol": 0.1, "hint": "27 ÷ 900.", "sol": "<b>3%</b>."},
  {"q": "The price level index rises from 100 to 104 over the same period. What is the % change in the price level?", "a": 4, "unit": "%", "tol": 0.1, "hint": "4 ÷ 100.", "sol": "<b>4%</b>."},
  {"q": "Using the output gap of −120 on potential output of 1,000, what is the gap as a percentage of potential output?", "a": -12, "unit": "%", "tol": 0.2, "hint": "−120 ÷ 1,000.", "sol": "<b>−12%</b>."}]) + MCQ([
  ("Macroeconomic equilibrium is where:", ["AD equals SRAS", "AD equals LRAS only", "SRAS equals LRAS only", "Output is zero"], 0, "Intersection of AD and SRAS."),
  ("A leftward shift of SRAS causes:", ["Higher prices and lower output", "Lower prices and higher output", "Higher prices and higher output", "No change"], 0, "Cost-push."),
  ("An AD increase raises mainly prices when:", ["The economy is near full capacity", "There is much spare capacity", "SRAS is flat", "Unemployment is high"], 0, "Output cannot rise."),
  ("Real output is below potential. This means:", ["Spare capacity", "Overheating", "Zero unemployment", "Full employment"], 0, "A negative output gap."),
  ("Stagflation is:", ["Rising prices and falling output", "Falling prices and rising output", "Rising prices and rising output", "Falling prices and falling output"], 0, "SRAS shifts left.")
], "qz1") + CARDS([
  ("Equilibrium", "AD = SRAS."),
  ("Long-run", "AD = SRAS = LRAS."),
  ("AD right", "Output and prices up."),
  ("SRAS left", "Prices up, output down."),
  ("Flat AS", "AD rise: output."),
  ("Vertical AS", "AD rise: prices."),
  ("Output gap", "Actual minus potential."),
  ("Employment", "Follows output.")]) + MCQ(mc_exam)

build("as45", "as-ad-as-equilibrium", "AD/AS Equilibrium and the Effects of Shifts", EY,
  "4.3.11 to 4.3.12: macroeconomic equilibrium, output, the price level and employment, and the effect of shifts in AD and AS. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
