"""Resource: the Keynesian 45 degree diagram explained from scratch (9.1.1 national income determination, 9.1.3 gaps). Run: python3 tools/artifact-kit/mk_sy9145.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.1 · Explainer"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">Keynesian 45° diagram</b> (also called the Keynesian cross) plots <b>aggregate expenditure (AE)</b> on the vertical axis against <b>national income (Y)</b> on the horizontal axis. The <b>45° line</b> is the set of points where expenditure equals income, so it shows every possible equilibrium. The <b>AE line</b> shows how much people, firms, the government and foreigners would <b>plan to spend</b> at each level of income, and <b>equilibrium is where the two lines cross</b>. Everything else in 9.1, the multiplier, the gaps, saving and injections, can be read off this one diagram.</p></div>

  <h2>1 · What the axes measure</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Horizontal axis: national income, Y.</b> In a closed circular flow, income, output and expenditure are three ways of measuring the same thing, so Y is also the value of output. It is real income, because the price level is held constant in this model.</li>
    <li><b>Vertical axis: aggregate expenditure, AE.</b> The total planned spending in the economy: <b>AE = C + I + G + (X − M)</b>.</li>
    <li><b>Both axes use the same scale.</b> This is what makes the line at 45° meaningful.</li>
  </ul>
  <div class="tip"><b class="h">AE is not AD</b>The aggregate demand curve has the <b>price level</b> on the vertical axis and shows total spending at different price levels. The AE line has <b>expenditure</b> on the vertical axis and shows total spending at different levels of <b>income</b>, with the price level fixed. They look different on the page and answer different questions.</div>

  <h2>2 · The 45° line</h2>
  <p>Because both axes have the same scale, any point on a line from the origin at 45° has a horizontal value equal to its vertical value. So at every point on the 45° line, <b>expenditure equals income</b>: 200 on one axis is 200 on the other. It is not a behavioural line. It is a <b>reference line</b> that answers one question: <b>at what levels of income would spending exactly match the output produced?</b></p>
  <p>That matters because output only stays at a steady level when buyers purchase all of it. If spending is greater than output, stocks (inventories) run down and firms produce more. If spending is less than output, unsold goods pile up and firms cut production. National income can therefore only settle at a point <b>on the 45° line</b>.</p>

  <h2>3 · The consumption line</h2>
  <p>Consumption depends on income. Using the consumption function <b>C = a + cY</b> with autonomous consumption <b>a = 100</b> and an MPC of <b>c = 0.6</b>, households spend 100 even at zero income and 60 cents of each extra dollar of income.</p>
  <ul>
    <li><b>The intercept (100)</b> is autonomous consumption. It sets where the line starts on the vertical axis.</li>
    <li><b>The slope (0.6)</b> is the MPC. A steeper line means that more of each extra dollar is spent.</li>
    <li><b>Where C meets the 45° line</b> (Y = 250 here, because 100 + 0.6Y = Y) is the <b>break-even level</b> of income: households spend exactly what they earn, so saving is zero. Below it they dissave. Above it they save.</li>
    <li><b>Saving at any income is the vertical gap between the 45° line and the C line</b>, because S = Y − C. This is why the C line is always flatter than the 45° line: the MPC is less than 1.</li>
  </ul>
  <div class="tip"><b class="h">Same line as on the consumption page</b>The dotted C = Y line on the consumption function chart in the consumption, saving and investment page is this 45° line, and the break-even point is the same idea.</div>

  <h2>4 · Adding investment, government spending and net exports</h2>
  <p>Aggregate expenditure adds the other components on top of C.</p>
  <div class="tw"><table class="t">
    <tr><th>Add this</th><th>Treated as</th><th>What happens to the line</th></tr>
    <tr><td><b>Investment, I</b></td><td>Autonomous (set by interest rates, confidence and expected profit, not by current income)</td><td>The C line shifts <b>up in parallel</b> by the amount of I. The line is now C + I.</td></tr>
    <tr><td><b>Government spending, G</b></td><td>Autonomous (set by policy)</td><td>Shifts up again in parallel: C + I + G.</td></tr>
    <tr><td><b>Net exports, X − M</b></td><td>Exports are autonomous (set by foreign income and competitiveness). Imports rise with income.</td><td>Exports shift the line up. Imports <b>flatten the slope</b>, because part of each extra dollar of income is spent abroad. If net exports are negative the line shifts down.</td></tr>
    <tr><td><b>Taxes</b></td><td>Part of income is taxed, so disposable income rises by less than income</td><td>Flattens the slope. The slope becomes c(1 − t) − m.</td></tr>
  </table></div>
  <p>The top line is <b>AE = C + I + G + (X − M)</b>. Its <b>intercept</b> is total autonomous spending, and its <b>slope</b> is the share of each extra dollar of income that is spent on <b>domestic</b> output: MPC × (1 − MRT) − MPM. Because every leakage reduces the slope, the AE line is always flatter than the 45° line, so the two lines must cross somewhere.</p>

  <h2>5 · Equilibrium, and why it is stable</h2>
  <p>Equilibrium national income is where the AE line crosses the 45° line. With C = 100 + 0.6Y, I = 50 and G = 50 the AE line is 200 + 0.6Y, so equilibrium is where Y = 200 + 0.6Y, which gives <b>Y = 500</b> (that is Y = autonomous spending × multiplier = 200 × 2.5).</p>
  <ul>
    <li><b>Below equilibrium (for example Y = 300):</b> AE = 200 + 0.6 × 300 = 380, which is more than output. Stocks fall unexpectedly, so firms raise production and hire more. Income rises towards 500.</li>
    <li><b>Above equilibrium (for example Y = 700):</b> AE = 620, which is less than output. Unsold stocks build up, so firms cut production. Income falls towards 500.</li>
  </ul>
  <p>The economy moves towards equilibrium from either side, so the equilibrium is stable. The AE line is <b>planned</b> spending. Differences between planned and actual spending show up as <b>unplanned changes in stocks</b>, which is the signal firms respond to.</p>

  <h2>6 · A shift versus a movement along the line</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Movement along the AE line</th><th>Shift of the AE line</th></tr>
    <tr><td><b>Caused by</b></td><td>A change in <b>income</b></td><td>A change in <b>autonomous spending</b> (confidence, interest rates, G, taxes, exports, wealth)</td></tr>
    <tr><td><b>Example</b></td><td>Income rises, so induced consumption rises</td><td>A fall in the interest rate raises investment</td></tr>
    <tr><td><b>Effect on equilibrium</b></td><td>None by itself. It is how the economy moves to equilibrium.</td><td>A new equilibrium at a different income</td></tr>
  </table></div>
  <p>A rise in autonomous spending shifts AE up by, say, 20. Equilibrium income does not rise by 20. It rises by <b>20 × the multiplier</b>, which is 50 when the multiplier is 2.5. On the diagram the <b>vertical</b> shift is small and the <b>horizontal</b> change in equilibrium is larger. The reason is the chain of spending: the extra 20 becomes income, 60% of it is spent, that becomes income, and so on. In the third animation you can see the staircase between the AE line and the 45° line that closes in on the new equilibrium.</p>

  <h2>7 · Saving, leakages and injections on the same diagram</h2>
  <p>At equilibrium AE = Y, so C + I + G = Y. Subtract C from both sides: <b>I + G = Y − C = S</b>. In an economy with no tax and no trade, <b>saving equals investment plus government spending</b>. With taxes and trade the condition becomes the familiar one:</p>
  <div class="formula">Equilibrium: S + T + M = I + G + X (leakages = injections)</div>
  <p>The two ways of finding equilibrium always give the same answer. The 45° approach looks at <b>expenditure against output</b>. The injections and withdrawals approach looks at <b>what is put into the circular flow against what leaks out</b>. In the fourth animation, the vertical gap between the C line and the 45° line at Y = 500 (saving) is exactly the gap between C and the AE line (I + G).</p>

  <h2>8 · The full employment level and the gaps</h2>
  <p>Mark the <b>full employment level of national income</b> (YF) on the horizontal axis. If the AE line cuts the 45° line to the left of YF, AE at YF is below the 45° line and there is a <b>deflationary gap</b>, measured as the vertical distance at YF. If it cuts to the right of YF, there is an <b>inflationary gap</b>. These are covered in detail in the page on equilibrium and the gaps, and you can experiment with them there.</p>

  <h2>9 · What the model assumes</h2>
  <ul>
    <li><b>The price level is fixed</b> and firms respond to a rise in spending by producing more, not by raising prices. This is realistic when there is spare capacity (a deflationary gap), and not near full employment.</li>
    <li><b>Interest rates, expectations and the money supply are held constant</b>, so investment is treated as autonomous.</li>
    <li><b>Planned spending is what matters</b>, and the model says nothing about how long the adjustment takes.</li>
    <li><b>The multiplier is the same for every injection</b>, which ignores differences between spending on imports and on home goods.</li>
  </ul>
  <p>It is a <b>Keynesian</b> model. Classical and monetarist economists argue that the economy self-corrects to full employment, so for them the cross does not describe the long run.</p>

  <h2>10 · Common mistakes</h2>
  <div class="tw"><table class="t">
    <tr><th>Mistake</th><th>Fix</th></tr>
    <tr><td>Drawing an AD curve with the price level on the axis</td><td>Label the vertical axis <b>aggregate expenditure</b> and the horizontal axis <b>national income</b></td></tr>
    <tr><td>An AE line steeper than the 45° line</td><td>It must be flatter, because the MPC is below 1 and leakages reduce the slope</td></tr>
    <tr><td>Starting the AE line at the origin</td><td>It starts on the vertical axis at autonomous spending</td></tr>
    <tr><td>Saying a rise in investment raises income by the same amount</td><td>Income rises by the change in investment <b>times the multiplier</b></td></tr>
    <tr><td>Measuring the gap horizontally</td><td>The gap is the <b>vertical</b> distance at full employment. The horizontal distance is the change in income needed.</td></tr>
    <tr><td>Confusing the shift with the movement</td><td>Autonomous spending shifts the line. A change in income moves along it.</td></tr>
  </table></div>

  <h2>11 · How to draw it in an exam</h2>
  <ol>
    <li>Label the axes: <b>national income (Y)</b> and <b>aggregate expenditure (AE)</b>.</li>
    <li>Draw the <b>45° line</b> from the origin and label it.</li>
    <li>Draw the <b>AE line</b> starting above the origin, sloping up more gently than the 45° line.</li>
    <li>Mark <b>equilibrium</b> where they cross and drop a dashed line to the axis (Y).</li>
    <li>If the question is about the gap, mark <b>YF</b> and show the <b>vertical distance</b> between the lines at YF.</li>
    <li>For a change, draw the <b>new AE line</b> parallel to the old and mark the <b>new equilibrium</b>, showing that income rises by more than the shift.</li>
  </ol>
'''

watch = '''
  <h2>1 · Building the diagram</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stB"></div>
  <h2>2 · Why equilibrium is stable</h2>
  <div id="stE"></div>
  <h2>3 · A rise in investment and the multiplier</h2>
  <div id="stM"></div>
  <h2>4 · Saving equals investment plus government spending</h2>
  <div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · Build your own 45° diagram</h2>
  <p>Set the components of expenditure and the propensities. The diagram draws the C line, then adds I, G and net exports, and finds equilibrium. The readout checks that leakages equal injections at equilibrium.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Slope of AE</small><strong id="r1"></strong></div><div><small>Multiplier</small><strong id="r2"></strong></div><div><small>Equilibrium income</small><strong id="r3"></strong></div></div>
    <div class="readout"><div><small>Leakages S + T + M</small><strong id="r4"></strong></div><div><small>Injections I + G + X</small><strong id="r5"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 440 390" role="img" aria-label="Keynesian 45 degree diagram built from consumption, investment, government spending and net exports"></svg></div></div></div>

  <h2>Lab 2 · What does this distance on the diagram represent?</h2>
  <p>Choose a distance and see what it means.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Movement along the line or shift of the line?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the adjustment to a point below equilibrium in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A recession and the shape of the diagram", "When confidence collapses, firms cut investment and households cut spending, so autonomous spending falls. The AE line shifts down, equilibrium income falls by a multiple of the shift, and a deflationary gap may open if income falls below the full employment level.", "using the diagram to show how a fall in confidence causes a downturn. Mention the multiplier.") +
rw("A fiscal stimulus", "A government raises its spending to lift a weak economy. In the diagram this shifts AE up, and income rises by the injection times the multiplier. If households save a large share of the extra income, the multiplier is smaller and the effect weaker.", "evaluating fiscal policy. Say that the size of the effect depends on the slope of the AE line.") +
rw("A boom in a trading partner", "If a country's main customers grow quickly, their demand for its exports rises. Exports are autonomous, so the AE line shifts up and equilibrium income rises by a multiple of the extra exports.", "showing how foreign income feeds into national income through net exports.") +
rw("A rise in interest rates", "Higher interest rates make borrowing dearer and raise the reward for saving, so autonomous investment and consumption may fall. The AE line shifts down and equilibrium income falls.", "showing how monetary policy may work through AE. Mention lags and uncertainty.")
)

mc_exam = [
  ("In a closed economy the aggregate expenditure line (C + I + G) cuts the 45° line at a level of income below the full employment level. What measures the deflationary gap? (Based on May/June 2023 · 33 · Q20)", ["The horizontal distance between equilibrium income and full employment income", "The vertical distance between the C + I + G line and the 45° line at full employment income", "The vertical distance between the C line and the C + I line", "The vertical distance between the C line and the 45° line at equilibrium income"], 1, "The deflationary gap is the vertical distance between the 45° line and the AE line (C + I + G) at the full employment level of income."),
  ("A closed economy has an AD line that cuts the 45° line at income N, and full employment income YF is above N. Which distance measures the deflationary gap? (Based on Oct/Nov 2023 · 31 · Q18)", ["The horizontal distance from N to YF", "The vertical distance between the 45° line and the AD line at YF", "The vertical distance between the AD line and the consumption line at YF", "The height of the AD line at the vertical axis"], 1, "Measure the gap vertically at full employment, between the 45° line and AD. The horizontal distance is the change in income needed."),
  ("Which is true at the equilibrium level of national income on the 45° diagram? (Practice, not a past paper question)", ["Planned expenditure is greater than output", "Planned expenditure equals output and there is no unplanned change in stocks", "Output is always at the full employment level", "Saving is zero"], 1, "At equilibrium AE = Y, so firms sell what they produce and stocks do not change unexpectedly.")
]

exam = exam_page("the 45° diagram",
  "The diagram appears in Paper 3 multiple choice, where you identify the gap or the effect of a shift, and in Paper 4 essays that ask you to explain equilibrium below full employment. Two multiple choice questions are reworded below, with written practice questions of our own.",
  [("Multiple choice (Paper 3)", "gap on the 45° diagram", "May/June 2023 (31, 33) Q20, Oct/Nov 2023 (31) Q18, Oct/Nov 2020 (33) Q24"), ("Essay, 25 marks", "1", "Feb/March 2021 (42) Q6 (equilibrium below full employment)"), ("Practice questions", "2", "Draw and explain")],
  [
  eq("Practice (not a past paper question)", "8 marks", "Using a 45° diagram, explain how an increase in investment could raise national income by more than the increase in investment.",
     ["A labelled 45° diagram with an AE line shifting upwards, the old and new equilibrium marked.",
      "The rise in investment is an increase in autonomous spending, which shifts the AE line up.",
      "National income rises by the multiplier times the increase, because each round of extra income leads to further spending, with leakages reducing each round.",
      "Evaluation: the effect is smaller if the multiplier is small, and may be mostly price rises near full employment."],
     "Diagram. Shift. The chain of spending. A limit.",
     [[("k", "Aggregate expenditure is the total planned spending in an economy at each level of income, and equilibrium national income is where the AE line cuts the 45° line, because only there does expenditure equal output."), ("a", "Investment is autonomous spending, so a rise in investment shifts the AE line upwards in parallel. At the old level of income, expenditure is now greater than output, stocks fall and firms produce more.")],
      [("n", "The extra output creates extra income for workers and owners, who spend a proportion of it, and this becomes income for others, so national income rises through several rounds until the new AE line cuts the 45° line at a higher level of income. The final rise is the change in investment multiplied by the multiplier, which is greater than the original rise."), ("e", "However, the rounds get smaller because part of each extra dollar leaks out in saving, taxes and imports, and if the economy is near full employment, much of the extra spending may raise prices rather than output.")]]),
  eq("Practice (not a past paper question)", "6 marks", "Explain why the AE line is flatter than the 45° line.",
     ["The slope of AE is the share of each extra dollar of income that is spent on domestic goods and services.",
      "Part of each extra dollar is saved, taxed or spent on imports, so the slope is less than 1.",
      "The 45° line has a slope of 1, so AE is flatter, and the two lines cross."],
     "Slope as the share spent at home. Three leakages. The 45° line has a slope of 1.")
  ], mcq_h="Multiple choice questions")

tips = tips_html(
  [("Say what each axis measures.", "National income on the horizontal and aggregate expenditure on the vertical."),
   ("Keep the AE line flatter than the 45° line.", "A line steeper than the 45° line would imply an MPC above 1."),
   ("Start AE above the origin.", "The intercept is autonomous spending."),
   ("Show the new equilibrium, not only the shift.", "Draw the new AE line parallel to the old, then mark where it crosses the 45° line."),
   ("Say income rises by a multiple.", "The horizontal change in income is larger than the vertical shift."),
   ("Measure the gap vertically.", "At full employment, between the 45° line and AE."),
   ("Link to leakages and injections.", "At equilibrium S + T + M = I + G + X. It is the same equilibrium from another angle.")],
  [("The line", "The 45° line shows all the points where aggregate expenditure equals national income."),
   ("Equilibrium", "Equilibrium national income is where the aggregate expenditure line cuts the 45° line, and there is no unplanned change in stocks."),
   ("Adjustment", "If expenditure exceeds output, stocks fall, so firms raise production and income rises."),
   ("A shift", "A rise in autonomous spending shifts the AE line upwards, and national income rises by a multiple of the change."),
   ("Evaluate", "However, the model assumes the price level is fixed, so near full employment a rise in expenditure could mainly raise prices.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["evaluate"]]) + FC

js = '''
/* ---------- the 45 degree diagram ---------- */
const E0 = 70, SC = 0.6, MX = 600, TOP = 36, F0 = TOP + MX * SC, px = (v) => E0 + SC * v, py = (v) => F0 - SC * v, SL = 0.6;
const tickSet = (gx, gy, x0, y0, xm, ym, step, grid) => { let o = ""; for (let v = 0; v <= xm + 0.001; v += step) { if (grid && v > 0) o += SV.line(gx(v), y0, gx(v), gy(ym), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(gx(v), y0, gx(v), y0 + 5, "", {}) + SV.text(gx(v), y0 + 18, v, "sm", { "text-anchor": "middle" }); }
  for (let v = step; v <= ym + 0.001; v += step) { if (grid) o += SV.line(x0, gy(v), gx(xm), gy(v), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(x0 - 5, gy(v), x0, gy(v), "", {}) + SV.text(x0 - 9, gy(v) + 4, v, "sm", { "text-anchor": "end" }); } return o; };
const niceStep = (mx) => [10, 20, 50, 100, 200, 500, 1000].find((s) => s >= mx / 6) || 1000;
function d45(s) {
  const dI = (s.dI || 0) * 20, aAE = 100 + (s.I ? 50 : 0) + (s.G ? 50 : 0) + dI, top = s.G ? 200 : s.I ? 150 : 100;
  let o = tickSet(px, py, E0, F0, MX, MX, 100, true) + axes(E0, F0, px(MX) + 8, TOP - 14, "", "Aggregate expenditure, AE") + SV.text(px(MX / 2), F0 + 52, "National income, Y", "sm", { "text-anchor": "middle" });
  if (s.l45 > 0) o += SV.line(px(0), py(0), px(MX), py(MX), "c3", op(s.l45)) + tag(px(MX) + 6, py(MX) - 8, "45° line (AE = Y)", "t3", s.l45);
  const ln = (a, c, lab, dash, dy) => SV.line(px(0), py(a), px(MX), py(a + SL * MX), c + (dash ? " dash" : ""), op(1)) + tag(px(MX) + 6, py(a + SL * MX) + (dy || 4), lab, c === "c1" ? "t1" : c === "c2" ? "t2" : "t4", 1);
  if (s.C > 0) o += SV.line(px(0), py(100), px(MX), py(100 + SL * MX), "c4", op(s.C)) + tag(px(MX) + 6, py(100 + SL * MX) + 5, "C = 100 + 0.6Y", "t4", s.C);
  if (s.I > 0) o += SV.line(px(0), py(150), px(MX), py(150 + SL * MX), "c1", op(s.I)) + tag(px(MX) + 6, py(150 + SL * MX) + 5, "C + I", "t1", s.I);
  if (s.G > 0) o += SV.line(px(0), py(200), px(MX), py(200 + SL * MX), "c1", { ...op(s.G), ...(dI > 0 ? { "stroke-dasharray": "6 5" } : {}) }) + tag(px(MX) + 6, py(200 + SL * MX) + (dI > 0 ? 15 : 5), "C + I + G (AE)", "t1", s.G);
  if (dI > 0) o += SV.line(px(0), py(aAE), px(MX), py(aAE + SL * MX), "c2") + tag(px(MX) + 6, py(aAE + SL * MX) + 3, "AE after I up 20", "t2", 1);
  if (s.be > 0) o += SV.line(px(250), F0, px(250), py(250), "c4 dash", op(s.be)) + SV.circle(px(250), py(250), 5, "dot4", op(s.be)) + SV.line(E0, py(250), px(250), py(250), "c4 dash", op(s.be)) + tag(px(250) - 8, py(250) - 12, "break-even: C = Y = 250", "t4", s.be, "end");
  const Y0 = top === 200 ? 500 : 0;
  if (s.eq > 0) o += SV.line(px(Y0), F0, px(Y0), py(Y0), "c1 dash", op(s.eq)) + SV.circle(px(Y0), py(Y0), 6, "dot1", op(s.eq)) + SV.line(E0, py(Y0), px(Y0), py(Y0), "c1 dash", op(s.eq)) + tag(px(Y0) - 10, py(Y0) - 12, "equilibrium: Y = AE = 500", "t1", s.eq, "end");
  if (s.y > 0) { const Y = s.yv, a = 200 + SL * Y, c = Y < 500 ? "t2" : "t4";
    o += SV.line(px(Y), py(Y), px(Y), py(a), "c2", { "stroke-width": 6, ...op(s.y) }) + SV.circle(px(Y), py(Y), 5, "dot3", op(s.y)) + SV.circle(px(Y), py(a), 5, "dot1", op(s.y));
    o += SV.line(px(Y), F0 - 8, px(Y + (Y < 500 ? 150 : -150)), F0 - 8, "c2", op(s.y)) + SV.arrowHead(px(Y + (Y < 500 ? 150 : -150)), F0 - 8, Y < 500 ? "r" : "l", "dot2");
    if (s.t) o += tag(px(Y) + (Y < 500 ? -10 : 10), py(Math.max(Y, a)) - 14, s.t, c, s.y, Y < 500 ? "end" : "start"); }
  if (s.st > 0) { const Ys = [500, 520, 532, 539.2, 543.52]; let d = "";
    for (let k = 0; k < Math.min(4, s.st); k++) { const a = Ys[k], b = Ys[k + 1]; d += SV.line(px(a), py(a), px(a), py(b), "c2", { "stroke-width": 3 }) + SV.line(px(a), py(b), px(b), py(b), "c2", { "stroke-width": 3 }); }
    o += d; }
  if (s.sv > 0) { const a = 500, cc = 400;
    o += SV.line(px(a) - 10, py(cc), px(a) - 10, py(a), "c3", { "stroke-width": 8, ...op(s.sv) }) + tag(px(30), py(596), "Green bar: saving S = Y − C = 100", "t3", s.sv);
    o += SV.line(px(a) + 10, py(cc), px(a) + 10, py(a), "c1", { "stroke-width": 8, ...op(s.sv) }) + tag(px(30), py(566), "Blue bar: I + G = AE − C = 100", "t1", s.sv); }
  return o;
}
const D0 = { l45: 0, C: 0, I: 0, G: 0, be: 0, eq: 0, y: 0, yv: 300, t: "", dI: 0, st: 0, sv: 0 };
const st = (o) => Object.assign({}, D0, o);
$("#pic1").innerHTML = `<svg viewBox="0 0 620 ${F0 + 66}" role="img" aria-label="Axes of the Keynesian diagram with the 45 degree line, the aggregate expenditure line and equilibrium">${d45(st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }))}</svg>`;
const stp = (id, label, steps) => Lib.stepper($(id), { w: 620, h: F0 + 66, label, base: D0, draw: d45, tween: 900, dwell: 6200, steps });

stp("#stB", "Building the 45 degree diagram: the 45 degree line, then C, C plus I, C plus I plus G and equilibrium", [
  { cap: "<b>The axes.</b> National income on the horizontal axis, aggregate expenditure on the vertical, both on the <b>same scale</b>.", s: st({}) },
  { cap: "<b>The 45° line.</b> With equal scales, every point on it has expenditure equal to income. It marks the only places where spending matches output.", s: st({ l45: 1 }) },
  { cap: "<b>Consumption: C = 100 + 0.6Y.</b> It starts at 100 (autonomous consumption) and slopes up with the MPC of 0.6, so it is flatter than the 45° line.", s: st({ l45: 1, C: 1 }) },
  { cap: "<b>Break-even.</b> C meets the 45° line at Y = 250. Below it households spend more than they earn. Above it the vertical gap between the lines is saving.", s: st({ l45: 1, C: 1, be: 1 }) },
  { cap: "<b>Add investment of 50.</b> It is autonomous, so the line shifts up in parallel to C + I.", s: st({ l45: 1, C: 1, I: 1 }) },
  { cap: "<b>Add government spending of 50.</b> Another parallel shift: C + I + G = 200 + 0.6Y. This is the aggregate expenditure line.", s: st({ l45: 1, C: 1, I: 1, G: 1 }) },
  { cap: "<b>Equilibrium.</b> AE crosses the 45° line at Y = 200 ÷ (1 − 0.6) = <b>500</b>. Only here does planned expenditure equal output.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
]);
stp("#stE", "Below equilibrium aggregate expenditure exceeds output so income rises, and above it income falls", [
  { cap: "<b>Equilibrium is 500.</b> At 500 planned spending is 200 + 0.6 × 500 = 500: it matches output.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Income of 300.</b> AE is 200 + 0.6 × 300 = 380, which is <b>80 more than output</b>. Shops sell more than expected, so stocks fall.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 300, t: "AE > output: stocks fall" }) },
  { cap: "<b>Firms respond</b> by raising output and hiring. Income rises, which is a movement along the AE line towards 500, and the gap gets smaller as it goes.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 300, t: "output rises" }) },
  { cap: "<b>Income of 600.</b> AE is 200 + 0.6 × 600 = 560, which is <b>40 less than output</b>. Unsold stocks pile up.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 600, t: "AE < output: stocks rise" }) },
  { cap: "<b>Firms cut production</b> and income falls back towards 500. From either side the economy moves to the point where the lines cross, so the equilibrium is stable.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 600, t: "output falls" }) },
]);
stp("#stM", "A rise in investment of 20 shifts the aggregate expenditure line up and income rises by 50 through rounds of spending", [
  { cap: "<b>Start at equilibrium, Y = 500.</b>", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Investment rises by 20.</b> Autonomous spending is now 220, so the whole AE line shifts <b>up by 20</b> (the red line).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1 }) },
  { cap: "<b>Round 1.</b> At Y = 500, AE is now 520, so firms produce 520. The 20 of extra output is 20 of extra income.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 1 }) },
  { cap: "<b>Round 2.</b> People spend 60% of that extra 20, which is 12. AE at 520 is 532, so output rises to 532.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 2 }) },
  { cap: "<b>Rounds 3 and 4.</b> Each step is 60% of the one before: 7.2, then 4.3. The staircase between the AE line and the 45° line gets smaller and smaller.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 4 }) },
  { cap: "<b>The new equilibrium is 550.</b> The vertical shift was 20, but income rose by 50 = 20 × 2.5, because the multiplier is 1 ÷ (1 − 0.6). The horizontal change is larger than the vertical shift.", s: st({ l45: 1, C: 1, I: 1, G: 1, dI: 1, st: 4 }) },
]);
stp("#stS", "At equilibrium the gap between C and the 45 degree line equals the gap between C and aggregate expenditure", [
  { cap: "<b>At equilibrium (500)</b> consumption is 100 + 0.6 × 500 = 400.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Saving is income minus consumption</b>: 500 − 400 = <b>100</b>. On the diagram it is the vertical gap between the 45° line and the C line (green).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 0.01 }) },
  { cap: "<b>Investment plus government spending</b> is 50 + 50 = <b>100</b>. It is the vertical gap between the C line and the AE line (blue).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 1 }) },
  { cap: "<b>The same height.</b> At equilibrium AE lies on the 45° line, so the two gaps are equal: S = I + G. With taxes and trade, leakages S + T + M equal injections I + G + X. The 45° diagram and the circular flow give the same equilibrium.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 1 }) },
]);

/* ---------- Lab 1 ---------- */
function lab45() {
  if (!$("#la") || !$("#lc") || !$("#li") || !$("#lg") || !$("#lx") || !$("#lt") || !$("#lm")) return;
  const a = +$("#la").value, c = +$("#lc").value / 100, I = +$("#li").value, G = +$("#lg").value, X = +$("#lx").value, t = +$("#lt").value / 100, m = +$("#lm").value / 100;
  const sl = c * (1 - t) - m, k = 1 / (1 - sl), A = a + I + G + X, Y = A * k;
  const S = -a + (1 - c) * (1 - t) * Y, T = t * Y, M = m * Y, lk = S + T + M, inj = I + G + X;
  $("#r1").textContent = Lib.fmtN(sl, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = "$" + Lib.fmtN(lk, 0) + "bn"; $("#r5").textContent = "$" + Lib.fmtN(inj, 0) + "bn";
  $("#rv").textContent = `AE = ${Lib.fmtN(A, 0)} + ${Lib.fmtN(sl, 2)}Y crosses the 45° line at Y = ${Lib.fmtN(A, 0)} × ${Lib.fmtN(k, 2)} = $${Lib.fmtN(Y, 0)}bn. At that income leakages (${Lib.fmtN(lk, 0)}) equal injections (${Lib.fmtN(inj, 0)}).`;
  const mx = Math.max(Y * 1.3, 100), sc = 300 / mx, gx = (v) => 70 + sc * v, gy = (v) => 340 - sc * v, ln = (b) => [gx(0), gy(b), gx(mx), gy(b + sl * mx)];
  const lines = [[a, "c4", "C", "t4"], [a + I, "c1", "C+I", "t1"], [a + I + G, "c1", "C+I+G", "t1"], [A, "c2", "AE", "t2"]];
  const stp2 = niceStep(mx);
  let o = tickSet(gx, gy, 70, 340, mx, mx, stp2, true) + axes(70, 340, 410, 25, "", "Expenditure, AE") + SV.text(gx(mx / 2), 378, "Income, Y", "sm", { "text-anchor": "middle" }) + SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) - 2, gy(mx) + 16, "45°", "t3", 1, "end");
  let prev = -1;
  lines.forEach(([b, cl, lab, tc], i) => { if (i > 0 && Math.abs(b - prev) < 0.01) return; prev = b; const [x1, y1, x2, y2] = ln(b); o += SV.line(x1, y1, x2, y2, cl, i === 3 ? { "stroke-width": 4 } : {}) + (i === 3 ? tag(x2 + 4, y2 + 4, lab, tc, 1) : tag(x2 - 4, y2 - 6, lab, tc, 1, "end")); });
  o += SV.line(gx(Y), 340, gx(Y), gy(Y), "c1 dash") + SV.circle(gx(Y), gy(Y), 6, "dot1") + tag(gx(Y) - 10, gy(Y) - 12, "Y = " + Lib.fmtN(Y, 0), "t1", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la", label: "Autonomous consumption a ($bn) ", min: 20, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g2"), { id: "lc", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g3"), { id: "li", label: "Investment I ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g4"), { id: "lg", label: "Government spending G ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g5"), { id: "lx", label: "Exports X ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g6"), { id: "lt", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 10, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g7"), { id: "lm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: lab45 });
lab45();
btnTable("lbBtns", "lbOut", [
  ["Vertical distance from the horizontal axis up to the C line at income Y", "Consumption at Y", "Read the height of the C line."],
  ["Vertical distance between the 45° line and the C line", "Saving at Y", "S = Y − C. At break-even the distance is zero."],
  ["Vertical distance between the C line and the AE line", "I + G + net exports at Y", "The other components of AE added to consumption."],
  ["Vertical distance between the 45° line and the AE line at income below equilibrium", "Unplanned fall in stocks (AE exceeds output)", "A signal for firms to raise production."],
  ["Vertical distance between the 45° line and the AE line at full employment income", "The inflationary or deflationary gap", "The injection or cut in AD needed to reach full employment."],
  ["Horizontal distance between the old and the new equilibrium", "The change in national income", "Equals the vertical shift of AE times the multiplier."],
  ["Vertical distance between the old and the new AE line", "The change in autonomous spending", "Equals the change in income divided by the multiplier."]
], ["Distance on the diagram", "What it represents", "Note"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does each change cause a movement along the AE line or a shift of the AE line?", ["Movement along the AE line", "Shift of the AE line"],
  [("Income rises because firms hire more workers", 0), ("A fall in the interest rate raises investment", 1), ("The government cuts its spending", 1), ("A rise in foreign income raises exports", 1), ("Consumption rises because income has risen", 0), ("Business confidence falls", 1), ("Income falls from 700 towards 500 as stocks pile up", 0), ("A rise in house prices makes households feel wealthier", 1)],
  "Autonomous spending shifts the line. A change in income moves you along it.") + MATCH([
  ["45° line", "All the points where aggregate expenditure equals national income"],
  ["Aggregate expenditure", "Total planned spending: C + I + G + (X − M)"],
  ["Break-even income", "The income at which consumption equals income and saving is zero"],
  ["Autonomous spending", "Spending that does not depend on income; it sets the intercept"],
  ["Slope of the AE line", "The share of extra income spent on domestic output"],
  ["Equilibrium national income", "The income where the AE line cuts the 45° line"]]) + ORDER(
  "An economy is at an income below equilibrium. Put the adjustment in order.",
  ["Planned expenditure is greater than output", "Stocks fall unexpectedly", "Firms raise output and employ more workers", "Income rises along the AE line", "The economy reaches the income where AE equals output"],
  "The gap between AE and output gets smaller each round until the lines cross.") + CALC([
  {"q": "C = 100 + 0.6Y, I = 50 and G = 50. Calculate equilibrium national income.", "a": 500, "unit": "$bn", "tol": 0.01, "hint": "Y = 200 + 0.6Y.", "sol": "0.4Y = 200, so Y = <b>500</b>."},
  {"q": "C = 100 + 0.6Y. At what income does saving equal zero (break-even)?", "a": 250, "unit": "$bn", "tol": 0.01, "hint": "Set Y = 100 + 0.6Y.", "sol": "0.4Y = 100, so Y = <b>250</b>."},
  {"q": "With C = 100 + 0.6Y, what is saving when income is 500?", "a": 100, "unit": "$bn", "tol": 0.01, "hint": "S = Y − C.", "sol": "C = 400, so S = 500 − 400 = <b>100</b>."},
  {"q": "AE = 200 + 0.6Y. What is aggregate expenditure at an income of 300?", "a": 380, "unit": "$bn", "tol": 0.01, "hint": "200 + 0.6 × 300.", "sol": "200 + 180 = <b>380</b>, which is 80 more than output."},
  {"q": "Autonomous spending rises by 20 and the slope of the AE line is 0.6. By how much does equilibrium income rise?", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Multiplier = 1 ÷ (1 − 0.6).", "sol": "k = 2.5, so the rise is 20 × 2.5 = <b>50</b>."}
]) + MCQ([
  ("What does every point on the 45° line show?", ["Saving equals investment", "Aggregate expenditure equals national income", "Full employment", "Zero inflation"], 1, "With equal scales, expenditure equals income at every point."),
  ("Why must the AE line be flatter than the 45° line?", ["Because investment is autonomous", "Because the MPC is less than 1 and leakages take part of each extra dollar", "Because government spending is fixed", "Because the multiplier is greater than 1"], 1, "Only part of each extra dollar of income is spent on domestic output, so the slope is below 1."),
  ("A rise in autonomous consumption does what on the 45° diagram?", ["Moves the economy along the AE line", "Shifts the AE line upwards", "Rotates the 45° line", "Shifts the 45° line downwards"], 1, "Autonomous spending sets the intercept, so a rise shifts the line up."),
  ("At an income above equilibrium, what happens to stocks?", ["They fall unexpectedly", "They rise unexpectedly", "They stay the same", "They are not affected"], 1, "AE is below output, so unsold goods build up and firms cut production."),
  ("At equilibrium in a closed economy with no government, which is true?", ["S = I", "S > I", "S < I", "S = 0"], 0, "C + I = Y means that I = Y − C = S.")
], "qz1") + CARDS([
  ("Keynesian 45° diagram", "Expenditure (vertical) against income (horizontal); equilibrium where AE cuts the 45° line."),
  ("45° line", "Points where AE = Y; the only places where output is fully sold."),
  ("AE line", "Planned spending at each income: C + I + G + (X − M). Starts at autonomous spending."),
  ("Slope of AE", "c(1 − t) − m: the share of extra income spent on domestic output."),
  ("Break-even income", "Where C = Y and saving is zero."),
  ("Stable equilibrium", "Below it stocks fall and output rises; above it stocks rise and output falls."),
  ("Shift versus movement", "Autonomous spending shifts the line; income moves you along it."),
  ("Leakages = injections", "S + T + M = I + G + X at equilibrium; the same point as AE = Y.")]) + MCQ(mc_exam)

build("sy9145", "keynesian-45-degree-diagram", "The Keynesian 45° Diagram Explained", EY,
  "A step-by-step explainer of the Keynesian 45° diagram: what the axes show, the 45° line, building the AE line, equilibrium, shifts and the multiplier, saving and injections, and the gaps. With animations, a build-your-own lab, drills and exam questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
