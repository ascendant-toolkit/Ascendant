"""AS syllabus 4.3.6-4.3.10 Aggregate supply. Run: python3 tools/artifact-kit/mk_as44.py"""
from asx import *
EY = EYAS("4.3.6 to 4.3.10")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Aggregate supply (AS)</b> is the <b>total output that firms in an economy are willing and able to supply at each price level</b>. The <b class="kw">short-run aggregate supply (SRAS)</b> curve slopes <b>upward</b> because input prices such as wages are slow to adjust, so a higher price level raises profit and output; it shifts when <b>costs of production</b> change (wages, raw materials, energy, taxes, subsidies, the exchange rate). The <b class="kw">long-run aggregate supply (LRAS)</b> curve is either <b>vertical</b> at the economy's <b>potential output</b> (full employment of resources), or has <b>three sections</b>: highly elastic when there is much spare capacity, upward sloping as capacity tightens, and vertical at full capacity; it shifts when the <b>quantity or quality of factors of production</b> or <b>technology</b> change. A change in the price level causes a movement along AS, and any other determinant shifts it.</p></div>

  <h2>1 · Short-run aggregate supply (4.3.6 to 4.3.9)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Why SRAS slopes up:</b> in the short run some costs, especially <b>wages</b>, are fixed by contracts. When prices rise, <b>revenue rises faster than costs</b>, so firms raise output; as output approaches capacity costs rise, so the curve gets steeper.</li>
    <li><b>Shifts of SRAS (costs):</b> a fall in wages, raw material or energy prices, lower business taxes or higher subsidies, a stronger exchange rate (cheaper imported inputs), higher productivity shift SRAS to the <b>right</b>; the opposite moves it <b>left</b>.</li>
    <li>A <b>leftward shift of SRAS</b> raises the price level and lowers output, called <b>cost-push inflation</b> with falling output (stagflation).</li>
    <li>A change in the <b>price level</b> is a <b>movement along</b> SRAS.</li>
  </ul>

  <h2>2 · Long-run aggregate supply (4.3.7 to 4.3.9)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Vertical LRAS</th><th>Three-section LRAS</th></tr>
    <tr><td><b>View</b></td><td>Output is set by supply-side capacity, not by prices</td><td>Economy has spare capacity at low output and hits a ceiling at full capacity</td></tr>
    <tr><td><b>Shape</b></td><td>Vertical line at potential output</td><td>Highly elastic, then upward sloping, then vertical</td></tr>
    <tr><td><b>An AD increase</b></td><td>Raises only the price level in the long run</td><td>Raises output only (flat part), output and prices (sloping part), or prices only (vertical part)</td></tr>
  </table></div>
  <ul>
    <li><b>Shifts of LRAS (capacity):</b> more or better <b>labour</b> (population, immigration, education, training), more <b>capital</b> (net investment), <b>technology</b>, discovery of <b>resources</b>, better infrastructure, <b>deregulation</b> and competition. Shifting LRAS right is <b>economic growth</b> in potential output.</li>
    <li>The LRAS shifts <b>left</b> if capacity falls: war damage, emigration, resource depletion, or a lasting loss of skills.</li>
    <li><b>Short-run shifts</b> (costs) can be reversed quickly; <b>long-run shifts</b> change potential output.</li>
  </ul>

  <h2>3 · Determinants of aggregate supply in detail</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Curve that shifts</th><th>Direction and reason</th></tr>
    <tr><td><b>Wage rates</b></td><td>SRAS</td><td>Higher wages raise unit costs: left. A wage freeze or fall: right.</td></tr>
    <tr><td><b>Raw material and energy prices</b></td><td>SRAS</td><td>Higher oil prices raise costs: left. Lower prices: right.</td></tr>
    <tr><td><b>Business taxes and subsidies</b></td><td>SRAS</td><td>Higher taxes: left. Subsidies or lower taxes: right.</td></tr>
    <tr><td><b>Exchange rate</b></td><td>SRAS</td><td>A fall in the currency makes imported inputs dearer: left; a rise makes them cheaper: right.</td></tr>
    <tr><td><b>Productivity</b></td><td>SRAS and LRAS</td><td>Higher productivity lowers unit costs and raises capacity: right.</td></tr>
    <tr><td><b>Labour force size and skills</b></td><td>LRAS</td><td>More workers, better training and education: right. Emigration or ageing: may shift left.</td></tr>
    <tr><td><b>Capital stock and technology</b></td><td>LRAS</td><td>Net investment and new technology: right. Capital destroyed (war, disaster): left.</td></tr>
    <tr><td><b>Natural resources</b></td><td>LRAS</td><td>A new discovery: right. Depletion: left.</td></tr>
    <tr><td><b>Institutions and regulation</b></td><td>LRAS</td><td>Better infrastructure, competition and legal systems: right. Excessive regulation: may shift left.</td></tr>
  </table></div>

  <h2>4 · Explaining the shapes</h2>
  <ul>
    <li><b>SRAS upward-sloping:</b> input prices (especially wages) are fixed in the short run, so a higher price level raises profit per unit, and firms raise output. It gets steeper near capacity because firms must pay more for scarce inputs (overtime, less efficient machines).</li>
    <li><b>Three-section LRAS:</b> (1) <b>spare capacity</b>: output can rise with little pressure on costs, so the curve is flat; (2) <b>nearing capacity</b>: bottlenecks push up costs, so output rises less and prices more; (3) <b>full capacity</b>: no more can be produced, so the curve is vertical.</li>
    <li><b>Vertical LRAS:</b> the view that in the long run output depends on productive capacity, not on the price level, because wages and other costs adjust.</li>
    <li><b>Potential output</b> is the maximum output the economy can sustain with full employment of resources and without rising inflation.</li>
  </ul>

  <h2>5 · Worked example: a cost shock and a capacity change</h2>
  <p>Take AD as P = 120 − Y and SRAS as P = 20 + Y. Equilibrium is Y = 50, P = 70.</p>
  <div class="tw"><table class="t">
    <tr><th>Event</th><th>New SRAS</th><th>New equilibrium</th><th>Effect</th></tr>
    <tr><td><b>Oil price rise</b> raises costs</td><td>P = 40 + Y (shift left)</td><td>Y = 40, P = 80</td><td>Output falls, prices rise: cost-push inflation (stagflation)</td></tr>
    <tr><td><b>Fall in raw material prices</b></td><td>P = Y (shift right)</td><td>Y = 60, P = 60</td><td>Output rises, prices fall</td></tr>
  </table></div>
  <ul>
    <li>In the <b>long run</b>, an increase in training and technology shifts LRAS right: potential output rises, so the economy can grow without inflation. A cost shock does not change potential output by itself, but it can reduce actual output.</li>
  </ul>

  <h2>6 · Short run and long run</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Short run</th><th>Long run</th></tr>
    <tr><td><b>Definition</b></td><td>The period in which at least one factor (and some costs such as wages) is fixed</td><td>The period in which all factors can be changed</td></tr>
    <tr><td><b>Key curve</b></td><td>SRAS</td><td>LRAS</td></tr>
    <tr><td><b>Shifts caused by</b></td><td>Changes in costs</td><td>Changes in capacity and productivity</td></tr>
    <tr><td><b>Reversibility</b></td><td>Often temporary (a price spike fades)</td><td>Permanent changes in potential output</td></tr>
  </table></div>
  <div class="warn"><b class="h">Do not write this</b>Do not confuse SRAS with the supply curve of one firm or market: AS is the total output of the economy at each price level. Do not draw a rise in the price level as a shift of AS. Do not say wages rising shift LRAS: higher wages raise costs, so they shift SRAS (unless they change the supply of labour).</div>
  <div class="tip"><b class="h">Exam tip</b>Separate <b>costs</b> (SRAS) from <b>capacity</b> (LRAS). Name a determinant, say which curve moves, and say <b>why</b>: lower costs shift SRAS right; more productive capacity shifts LRAS right.</div>
'''

watch = '''
  <h2>1 · A cost shock shifts SRAS</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stS"></div>
  <h2>2 · LRAS: potential output and its three-section shape</h2>
  <div id="stL"></div>
'''

explore = '''
  <h2>Lab 1 · Short-run cost changes</h2>
  <p>Change costs and see SRAS shift against a fixed AD curve. (Positive = costs fall.)</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>SRAS</small><strong id="r1"></strong></div><div><small>Real output</small><strong id="r2"></strong></div><div><small>Price level</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with SRAS shifted by the chosen cost changes"></svg></div></div></div>

  <h2>Lab 2 · Long-run capacity</h2>
  <p>Raise the quantity and quality of resources and see LRAS shift. The economy's actual output is where AD meets SRAS.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Potential output</small><strong id="t1"></strong></div><div><small>Actual output</small><strong id="t2"></strong></div><div><small>Output gap</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with LRAS shifted by the chosen changes"></svg></div></div></div>
'''

practise = '''
  <h2>1 · SRAS or LRAS?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a rise in raw material costs in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("An oil price shock", "Oil is an input for transport and many products. When its price jumps, firms' costs rise at every level of output, so SRAS shifts left. Prices rise while output falls, which is cost-push inflation with weaker growth.", "SRAS shifting left from higher costs.") +
rw("A stronger currency", "A higher exchange rate makes imported raw materials and components cheaper, lowering costs. SRAS shifts right, helping to lower prices and raise output in the short run.", "the exchange rate as a cost determinant of SRAS.") +
rw("Investing in education", "Better education and training raise the skills and productivity of workers, so the economy can produce more even at full employment. LRAS shifts right over time.", "a long-run supply-side shift in LRAS.") +
rw("A recession with spare capacity", "After a deep recession many factories and workers are idle. Output can rise a lot without much pressure on prices, the flat part of the three-section LRAS. Later, as spare capacity disappears, extra demand mostly raises prices.", "the three-section LRAS.") +
rw("An oil price shock", "A sharp rise in oil prices raises transport and production costs for firms across the economy. SRAS shifts left, so output falls and the price level rises at the same time.", "a leftward shift of SRAS and cost-push inflation.") +
rw("A new technology", "Widespread broadband and automation allow firms to produce more with the same inputs. Productivity rises and both SRAS and LRAS shift right, raising potential output.", "capacity growth and LRAS.")
)

mc_exam = [
  mcq("s21_12", 19, "What will cause a movement along an aggregate supply curve?", ["a rise in the demand for exports", "a rise in the price of raw materials", "a rise in the productivity of labour", "a rise in the rate of sales tax"], 0, "A rise in export demand raises AD and the price level, which moves the economy along the AS curve. The other options shift AS."),
  mcq("s22_12", 27, "A country imports oil. Why might an increase in the world price of oil have caused a shift in its short-run aggregate supply curve to the left?", ["A rise in inflation is expected", "Consumers face a fall in their disposable income", "Domestic firms' costs have increased", "The government reduces tax on oil and petroleum products"], 2, "Dearer oil raises firms' costs at every output level, which shifts SRAS."),
  mcq("s22_13", 24, "What is a certain outcome on an aggregate demand and aggregate supply diagram of an increase in factor productivity?", ["downward shift of the aggregate demand curve", "downward shift of the aggregate supply curve", "an upward shift of the aggregate demand curve", "an upward shift of the aggregate supply curve"], 1, "Higher productivity lowers unit costs, so AS shifts down (to the right)."),
  mcq("s25_11", 19, "Which statement is not correct?", ["The long-run aggregate supply curve can be downward sloping", "The long-run aggregate supply curve can be horizontal", "The long-run aggregate supply curve can be upward sloping", "The long-run aggregate supply curve can be vertical"], 0, "LRAS may be vertical, horizontal (at low output), or upward sloping in the three-section model, but not downward sloping."),
  mcq("w23_12", 26, "Which supply-side measure is most likely to produce short-run growth in a country's aggregate supply?", ["easing of controls on immigration of workers", "expenditure on primary education", "expenditure on research and development", "privatisation of public utilities"], 0, "More workers raise the available labour quickly. Education and R&D take years."),
  mcq("m25_12", 24, "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level?", ["Aggregate demand will also increase", "Labour productivity levels will increase", "Workers will save any extra wages they earn", "Workers will spend any extra wages on imports"], 0, "Higher incomes raise AD, which offsets the downward pressure on prices from higher AS."),
  mcq("s23_12", 18, "Which change is shown directly by the use of aggregate demand and aggregate supply analysis?", ["the nominal income level", "the price level", "the unemployment level", "the wage level"], 1, "The vertical axis is the price level. Unemployment and wages are inferred."),
  mcq("s20_13", 21, "What will increase if aggregate demand rises when aggregate supply is perfectly elastic?", ["labour shortages", "real output", "the price level", "wage rates"], 1, "With perfectly elastic AS, extra demand raises output but not prices."),
  mcq("w22_13", 21, "An economy is initially in equilibrium. Which combination of events will definitely cause an increase in the general price level of the economy and a decrease in its real output?", ["aggregate demand decreases, short-run aggregate supply decreases", "aggregate demand decreases, short-run aggregate supply unchanged", "aggregate demand increases, short-run aggregate supply decreases", "aggregate demand unchanged, short-run aggregate supply decreases"], 3, "A fall in SRAS with unchanged AD raises the price level and lowers output for certain. In the other cases one of the two effects is uncertain.")
]

exam = exam_page("aggregate supply",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Aggregate supply is an 8 mark Paper 2 part in several series, often linked to supply-side policy, and it appears in Paper 1 most years. Reworded past questions are below, with nine Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "May/June 2021 (23) Q3(a); Oct/Nov 2020 (22) Q3(a); May/June 2025 (24) Q4(a)"), ("Multiple choice (Paper 1)", "9 shown below", "2020 to 2025")],
  [
  eq(P("s21_23", "3(a)"), "8 marks", "Explain what is meant by aggregate supply and explain one reason why the aggregate supply curve of an economy would shift outwards in (i) the short run and (ii) the long run.",
     ["Knowledge (up to 2): an explanation of aggregate supply, such as total output in an economy (1), that distinguishes between the short run and the long run (1).",
      "Application (up to 3): a reason for an outward shift of SRAS (1) plus up to 2 marks for explaining why this moves SRAS outwards.",
      "Application (up to 3): a reason for an outward shift of LRAS (1) plus up to 2 marks for explaining why. Indicative reasons include an increase in the supply of labour, net investment, other factor inputs, devaluation of the exchange rate, government regulations, discovery of new resources, better education and training, and advances in technology."],
     "Define AS (total output; short vs long run). Short run: a cost fall shifts SRAS. Long run: more or better resources shifts LRAS.",
     [[("k", "Aggregate supply is the total output firms in an economy are willing and able to supply at each price level. In the short run, some costs such as wages are fixed, while in the long run all inputs can change, so output depends on the economy's capacity.")], [("n", "In the short run, a fall in the price of raw materials or energy lowers firms' costs, so they supply more at every price level and SRAS shifts to the right. In the long run, better education and training raise the skills and productivity of the workforce, which increases the economy's productive capacity, so LRAS shifts to the right.")]]),
  eq(P("w20_22", "3(a)"), "8 marks", "Explain how the factor of production enterprise contributes to aggregate supply in a modern economy and how it differs from the other factors of production in terms of the reward for its services.",
     ["Knowledge (up to 2): enterprise organises the other factors of production (1) and bears the risk of production (1).",
      "Application (up to 6): profit is the reward to enterprise (1); labour is rewarded with wages (1), land with rent (1) and capital with interest (1); enterprise uses the other factors to produce goods and services that increase aggregate supply (1), through an increase in productive potential or a fall in unused resources (1)."],
     "Enterprise organises and takes risk. Reward: profit (which may be a loss), unlike wages, rent, interest. It raises AS by using resources.",
     [[("k", "Enterprise organises the other factors of production, bringing together land, labour and capital, and bears the risk that costs will exceed revenue.")], [("n", "Profit is the reward for enterprise, and it is not guaranteed, whereas labour earns wages, land earns rent and capital earns interest, which are paid whether or not the firm makes a profit. By using the other factors to produce goods and services, enterprise raises aggregate supply, either by increasing productive potential, through new products and methods, or by reducing unused resources.")]]),
  eq(P("s25_24", "4(a)"), "8 marks", "Explain why expenditure on education and training is a supply-side policy and consider why its impact on the general price level may differ between the short run and the long run.",
     ["Knowledge (up to 3): supply-side policy consists of government tools designed to increase aggregate supply (1); the effect is to shift the AS curve to the right (1); spending on education and training increases worker skills and productivity, so raises productive capacity and shifts LRAS to the right (1).",
      "Analysis (up to 3): in the short run, increased government expenditure increases AD, which may raise inflation and the price level (up to 2); in the long run, higher productivity and capacity shift LRAS and should lower the price level (up to 2).",
      "Evaluation (up to 2): an overall assessment of whether the impact differs between the short and long run, for example if the spending is ineffective, or time lags mean the short-run impact is minimal; a justified conclusion (1)."],
     "Supply-side: raises AS. Short run: spending raises AD, prices up. Long run: LRAS shifts right, prices lower. Evaluate: time lags, effectiveness.",
     [[("k", "Supply-side policies aim to raise aggregate supply. Spending on education and training raises workers' skills and productivity, which increases the economy's productive capacity and shifts LRAS to the right.")], [("n", "In the short run, the extra government spending adds to AD, which may raise the price level, since the benefits to supply take time. In the long run, higher productivity and capacity shift LRAS right, which should lower the price level and raise output.")], [("e", "The long-run effect depends on the spending being effective and on time lags, so the short-run effect may be small. If it does not raise productivity, the policy may simply push up prices.")]])
  ],
  )

tips = tips_html(
  [("Costs move SRAS; capacity moves LRAS.", "State which curve before you describe the shift."),
   ("Say why SRAS slopes up.", "Sticky wages mean higher prices raise profit."),
   ("Left shift: price up, output down.", "Cost-push inflation."),
   ("LRAS is potential output.", "Full employment of resources."),
   ("Know both LRAS shapes.", "Vertical, or three sections."),
   ("Shifting LRAS right is growth.", "More potential output."),
   ("Movement along is price level only.", "Do not draw it as a shift.")],
  [("Aggregate supply", "Aggregate supply is the total output firms are willing and able to supply at each price level."),
   ("SRAS", "A rise in raw material costs may shift SRAS to the left."),
   ("LRAS", "LRAS shows potential output and shifts with the quantity and quality of resources."),
   ("Productivity", "Higher productivity may shift AS to the right."),
   ("Three sections", "The three-section LRAS is elastic, then upward sloping, then vertical.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- SRAS shift ---------- */
function cuDraw(s) { return adasPlot({ a: 0, s: s.s, g: 1, n: s.n, l: 0 }, { lras: false }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rise in costs shifts SRAS to the left, raising the price level and reducing output">${cuDraw({ s: -20, n: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A rise in costs shifts SRAS to the left", base: { s: 0, n: 0 }, draw: cuDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD1 and SRAS1 meet at a price level of 50 and real output of 50.", s: { s: 0, n: 0 } },
  { cap: "<b>A rise in raw material and energy prices</b> raises costs at every output. SRAS shifts <b>left</b>. The price level rises and real output falls: <b>cost-push inflation</b>.", s: { s: -20, n: 1 } },
  { cap: "<b>A fall in costs</b> (or a stronger currency, or higher productivity) shifts SRAS <b>right</b>: lower prices and higher output.", s: { s: 20, n: 1 } },
] });

/* ---------- LRAS ---------- */
function lrDraw(s) {
  let o = axes(70, 270, 720, 25, "Real output (Y)", "Price level");
  const x1 = SDX(75), x2 = SDX(75 + s.l);
  if (s.t < 0.5) { o += SV.line(x1, SDY(0), x1, SDY(100), "c4", { "stroke-width": 3.5, "stroke-dasharray": "7 4" }) + tag(x1 + 6, SDY(98), "LRAS1: potential output", "c4"); if (s.l > 0.5) o += SV.line(x2, SDY(0), x2, SDY(100), "c4", { "stroke-width": 3.5 }) + tag(x2 + 6, SDY(88), "LRAS2", "c4", 1) + arrow(x1 + 4, SDY(60), x2 - 6, SDY(60), "r", "c4", 1); }
  else { const P = [[SDX(10), SDY(15)], [SDX(35), SDY(18)], [SDX(60), SDY(35)], [SDX(72), SDY(65)], [SDX(75), SDY(100)]]; o += SV.path("M" + P.map((p) => p.join(",")).join(" L"), "c4", { fill: "none", "stroke-width": 3.5 }) + tag(SDX(12), SDY(10), "Highly elastic: spare capacity", "c4") + tag(SDX(38), SDY(48), "Upward sloping", "c4") + tag(SDX(75) + 8, SDY(90), "Vertical: full capacity", "c4"); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="LRAS as a vertical line at potential output shifting right">${lrDraw({ t: 0, l: 15 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "LRAS: potential output and the three-section view", base: { t: 0, l: 0 }, draw: lrDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The vertical LRAS</b> sits at the economy's <b>potential output</b>: what it can produce when all resources are fully employed. In the long run, output does not depend on the price level.", s: { t: 0, l: 0 } },
  { cap: "<b>Shifting LRAS right.</b> Better education, more capital, new technology or a bigger labour force raise potential output. This is long-run <b>economic growth</b>.", s: { t: 0, l: 15 } },
  { cap: "<b>The three-section view.</b> With much spare capacity, output can rise without raising prices (flat). As capacity tightens, prices begin to rise (sloping). At full capacity, only prices rise (vertical).", s: { t: 1, l: 0 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!["wg", "rm", "pd"].every((i) => $("#" + i))) return;
  const w = +$("#wg").value, r = +$("#rm").value, p = +$("#pd").value, s = Math.max(-30, Math.min(30, 0.5 * w + 0.5 * r + 0.8 * p)), e = sdEq(0, s), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(s) < 0.5 ? "No shift" : s > 0 ? "Right" : "Left"; $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = Math.abs(s) < 0.5 ? "Costs are unchanged, so SRAS stays put (price level 50, output 50)." : `${s > 0 ? "Lower costs or higher productivity" : "Higher costs"} shift SRAS to the ${s > 0 ? "right" : "left"}: real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. ${s < 0 ? "This is cost-push inflation with lower output." : "Prices fall and output rises."}`;
  $("#labA").innerHTML = adasPlot({ a: 0, s, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "wg", label: "Fall in wage costs (negative = rise), % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "rm", label: "Fall in raw material costs (negative = rise), % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "pd", label: "Rise in productivity, % ", min: -10, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["lb", "cp", "tc"].every((i) => $("#" + i))) return;
  const l = +$("#lb").value, c = +$("#cp").value, t = +$("#tc").value, sh = Math.min(20, 0.4 * l + 0.4 * c + 0.6 * t), pot = 75 + sh, e = sdEq(0, 0), gap = pot - e.q;
  $("#t1").textContent = Lib.fmtN(pot, 1); $("#t2").textContent = Lib.fmtN(e.q, 1); $("#t3").textContent = Lib.fmtN(gap, 1);
  $("#tv").textContent = sh <= 0.5 ? "No change in the quantity or quality of resources, so LRAS stays at 75 units of potential output. The economy produces 50 now, so it has spare capacity of 25." : `Better resources shift LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(pot, 1)}: potential output has grown. Actual output is still ${Lib.fmtN(e.q, 1)}, so spare capacity is ${Lib.fmtN(gap, 1)}. To use the extra capacity AD would also need to rise.`;
  $("#labB").innerHTML = adasPlot({ a: 0, s: 0, l: sh, g: 1, n: 1 });
}
Lib.slider($("#g4"), { id: "lb", label: "Growth in the labour force or skills, % ", min: 0, max: 20, step: 5, value: 10, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g5"), { id: "cp", label: "Net investment in capital, % ", min: 0, max: 20, step: 5, value: 10, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g6"), { id: "tc", label: "Technological progress, % ", min: 0, max: 20, step: 5, value: 5, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which curve shifts?", ["SRAS", "LRAS"],
  [("A rise in oil prices", 0), ("A rise in the size of the labour force", 1), ("A fall in wage costs", 0), ("Net investment in new factories", 1), ("A cut in business taxes", 0), ("Better education and training", 1), ("A stronger exchange rate lowers import costs", 0), ("A new technology raises potential output", 1)],
  "Costs and short-term factors shift SRAS. The quantity and quality of resources shift LRAS.") + MATCH([
  ["Aggregate supply", "Total output firms will supply at each price level"],
  ["SRAS", "Slopes up because wages and other costs are slow to adjust"],
  ["LRAS", "Potential output when resources are fully employed"],
  ["Cost-push inflation", "A rise in costs shifts SRAS left, raising prices"],
  ["Productivity", "Output per worker or per unit of input"],
  ["Potential output", "What the economy can produce at full employment"]]) + ORDER(
  "Put the effect of higher raw material costs in order.",
  ["Raw material prices rise", "Firms' costs rise at every level of output", "SRAS shifts to the left", "The price level rises", "Real output falls"],
  "Higher costs shift SRAS left: prices up, output down.") + CALC([
  {"q": "Equilibrium before: price level 50, output 50. After SRAS shifts left, price level 60 and output 40. What is the % rise in the price level?", "a": 20, "unit": "%", "tol": 0.2, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "What is the % fall in output?", "a": 20, "unit": "%", "tol": 0.2, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "Potential output is 800 and actual output is 740. What is the output gap (units)?", "a": 60, "unit": "", "tol": 0.5, "hint": "800 − 740.", "sol": "<b>60</b> units of spare capacity."},
  {"q": "Potential output rises from 800 to 840. What is the % growth in potential output?", "a": 5, "unit": "%", "tol": 0.1, "hint": "40 ÷ 800.", "sol": "<b>5%</b>."}]) + MCQ([
  ("A rise in wage costs will:", ["Shift SRAS to the left", "Shift SRAS to the right", "Shift AD to the right", "Shift LRAS right"], 0, "Costs rise."),
  ("The LRAS curve shows:", ["Potential output", "Planned spending", "Short-run output", "Unemployment"], 0, "Full employment output."),
  ("An increase in the labour force shifts:", ["LRAS to the right", "SRAS to the left", "AD to the left", "Nothing"], 0, "More resources."),
  ("Cost-push inflation is caused by:", ["A leftward shift of SRAS", "A rightward shift of AD", "A fall in costs", "Rising productivity"], 0, "Higher costs."),
  ("The three-section LRAS is flat when:", ["There is much spare capacity", "The economy is at full capacity", "Inflation is high", "Prices are falling"], 0, "Output can rise without price pressure.")
], "qz1") + CARDS([
  ("AS", "Output supplied at each price level."),
  ("SRAS", "Upward sloping; shifts with costs."),
  ("LRAS", "Potential output; shifts with capacity."),
  ("Costs rise", "SRAS left."),
  ("Productivity rises", "AS right."),
  ("Three sections", "Flat, sloping, vertical."),
  ("Cost-push", "SRAS left raises prices."),
  ("Growth", "LRAS shifts right.")]) + MCQ(mc_exam)

build("as44", "as-aggregate-supply", "Aggregate Supply", EY,
  "4.3.6 to 4.3.10: aggregate supply, the shape of the short-run and long-run AS curves, and the causes of shifts in SRAS and LRAS. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
