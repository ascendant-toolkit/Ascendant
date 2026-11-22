"""Syllabus 9.1.3 (with the national income determination bullet of 9.1.1): equilibrium and full employment national income, inflationary and deflationary gaps (chapter 41.3). Run: python3 tools/artifact-kit/mk_sy913.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.1.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>National income settles where <b class="kw">aggregate expenditure (AE) equals output</b>, which on the Keynesian 45° diagram is where the AE line crosses the 45° line, and this <b>equilibrium</b> need not be at the <b class="kw">full employment level of national income</b>. If AE at full employment is <b>too low</b>, there is a <b class="kw">deflationary gap</b>: output and jobs are below capacity. If AE at full employment is <b>too high</b>, there is an <b class="kw">inflationary gap</b>: demand exceeds what the economy can produce, so the price level rises. The size of either gap is the <b>vertical distance</b> between AE and the 45° line at full employment, and the injection needed to close it is that gap, which the <b>multiplier</b> then magnifies into the required change in national income.</p></div>

  <h2>1 · How national income is determined</h2>
  <p><b>Aggregate expenditure</b> is the total planned spending at each level of national income: <b>AE = C + I + G + (X − M)</b>. If AE is greater than current output, stocks run down, firms produce more and hire more, so output rises. If AE is less than output, stocks build up, firms cut output and jobs, so output falls. Output stops changing where <b>AE = Y</b>, shown on the 45° line (every point on it has expenditure equal to income).</p>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>The AE line slopes up</b> because consumption and imports depend on income. Its slope is the <b>marginal propensity to spend on domestic output</b>, MPC × (1 − mrt) − mpm in an open economy with a government.</li>
    <li><b>Where it cuts the vertical axis</b> is autonomous spending: spending that does not depend on income (autonomous consumption, most investment, government spending, exports).</li>
    <li><b>A change in autonomous spending shifts the whole AE line.</b> A change in income is a movement along it.</li>
    <li><b>The income approach</b> says the same thing in another way: equilibrium is where leakages equal injections (S + T + M = I + G + X), because only then is the flow of income not growing or shrinking.</li>
  </ul>
  <div class="tip"><b class="h">Do not mix up AE and AD</b>The aggregate demand curve shows total spending at different <b>price levels</b>. The aggregate expenditure line shows total spending at different <b>levels of income</b>, with the price level held constant.</div>
  <div class="tw"><table class="t">
    <tr><th>Equilibrium level of income</th><th>Formula</th></tr>
    <tr><td><b>Autonomous spending times the multiplier</b></td><td>Y = A × k, where A is autonomous spending and k = 1 ÷ (1 − slope of AE)</td></tr>
    <tr><td><b>Closed economy, no government</b></td><td>k = 1 ÷ (1 − mpc) = 1 ÷ mps</td></tr>
    <tr><td><b>Open economy with government</b></td><td>k = 1 ÷ (mps + mrt + mpm)</td></tr>
    <tr><td><b>Change in income</b></td><td>ΔY = k × ΔAD (the change in autonomous spending)</td></tr>
  </table></div>

  <h2>2 · Equilibrium and full employment are different things</h2>
  <p>The <b>full employment level of national income</b> (Y<sub>F</sub>) is the output the economy can produce when all resources are in use (potential output). Equilibrium is wherever AE meets the 45° line. Keynesians argue that equilibrium can sit below Y<sub>F</sub> for a long time because wages and prices are slow to adjust and confidence can stay low. Classical and monetarist economists think the economy returns to Y<sub>F</sub> in the long run, which is why the gap analysis is mainly a short-run, Keynesian one.</p>

  <h2>3 · The deflationary gap</h2>
  <div class="grid2">
    <div class="card"><h3>What it is</h3>
      <p>Equilibrium income is <b>below</b> Y<sub>F</sub> because AE at full employment is less than Y<sub>F</sub>. The <b>deflationary gap</b> is the amount by which AE at Y<sub>F</sub> falls short of Y<sub>F</sub>: the vertical distance between the 45° line and the AE line at Y<sub>F</sub>.</p>
      <p><b>Signs:</b> spare capacity, high unemployment, low or falling inflation, weak growth, a negative output gap.</p></div>
    <div class="card"><h3>The Keynesian solution</h3>
      <p>Raise autonomous spending by the size of the gap: more government spending (financed by borrowing), lower taxes, lower interest rates to lift investment. AE shifts up and the multiplier lifts income by <b>gap × k</b>, which closes the distance to Y<sub>F</sub>.</p>
      <p><b>Limits:</b> time lags, higher government debt, crowding out, and weak confidence may mean the extra spending is saved rather than spent.</p></div>
  </div>

  <h2>4 · The inflationary gap</h2>
  <div class="grid2">
    <div class="card"><h3>What it is</h3>
      <p>AE at Y<sub>F</sub> is <b>greater</b> than Y<sub>F</sub>. The economy cannot produce more than Y<sub>F</sub> in real terms, so the excess demand pulls up the price level instead of output. The <b>inflationary gap</b> is the vertical distance between the AE line and the 45° line at Y<sub>F</sub>.</p>
      <p><b>Signs:</b> labour shortages, rising wages and prices, a positive output gap, a worsening trade balance as imports are sucked in.</p></div>
    <div class="card"><h3>The Keynesian solution</h3>
      <p>Cut autonomous spending by the size of the gap: lower government spending, higher taxes, higher interest rates (to reduce consumption and investment). AE shifts down until it cuts the 45° line at Y<sub>F</sub>.</p>
      <p><b>Limits:</b> cuts and tax rises are unpopular, lags may mean the policy arrives when the economy is already slowing, and supply-side policy may be a better long-run answer than squeezing demand.</p></div>
  </div>
  <div class="tip"><b class="h">Two numbers that are easy to mix up</b>The <b>gap</b> (vertical, in expenditure terms) is the injection or cut in AD needed. The <b>difference between Y and Y<sub>F</sub></b> (horizontal) is the change in <b>income</b> that results after the multiplier. So <b>required change in AD = (Y<sub>F</sub> − Y) ÷ k</b>.</div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Deflationary gap</th><th>Inflationary gap</th></tr>
    <tr><td><b>AE at Y<sub>F</sub></b></td><td>Below Y<sub>F</sub> (below the 45° line)</td><td>Above Y<sub>F</sub> (above the 45° line)</td></tr>
    <tr><td><b>Equilibrium income</b></td><td>Less than Y<sub>F</sub></td><td>More than Y<sub>F</sub> in money terms (real output is capped at Y<sub>F</sub>)</td></tr>
    <tr><td><b>Main symptom</b></td><td>Unemployment and spare capacity</td><td>Rising prices and shortages</td></tr>
    <tr><td><b>Keynesian policy</b></td><td>Raise G, cut taxes, cut interest rates</td><td>Cut G, raise taxes, raise interest rates</td></tr>
    <tr><td><b>Size of change needed</b></td><td>(Y<sub>F</sub> − Y) ÷ k</td><td>(Y − Y<sub>F</sub>) ÷ k</td></tr>
  </table></div>
'''

watch = '''
  <h2>1 · A deflationary gap and how government spending closes it</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · An inflationary gap and how a cut in spending closes it</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · Find the gap</h2>
  <p>Set autonomous spending, the marginal propensities and the full employment level of income. The lab finds equilibrium, says which gap there is, and works out how much autonomous spending would have to change to close it.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Slope of AE</small><strong id="r1"></strong></div><div><small>Multiplier</small><strong id="r2"></strong></div><div><small>Equilibrium income</small><strong id="r3"></strong></div><div><small>Change in AD to close the gap</small><strong id="r4"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 440 400" role="img" aria-label="Keynesian 45 degree diagram with equilibrium and full employment income"></svg></div></div></div>

  <h2>Lab 2 · What does the diagram show?</h2>
  <p>Choose a situation and see which gap it is and what the Keynesian policy would be.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which gap?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the closing of a deflationary gap in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Japan from the late 1990s", "For more than two decades Japan had very low growth and spells of falling prices. Households and firms saved rather than spent, even when interest rates were close to zero and the government spent heavily, which suggests a lack of confidence kept expenditure below the level needed for full employment.", "a long-lived deflationary gap. Evaluate how far more government spending could close it when confidence is weak.") +
rw("Reopening after a pandemic", "When restrictions ended, demand in many economies recovered faster than firms could hire workers and rebuild supply chains. Shortages and rising prices followed in several countries.", "demand running ahead of potential output, like an inflationary gap. Say that supply constraints, not only demand, may have been behind inflation.") +
rw("A recession and a stimulus package", "In a deep recession a government may announce extra spending on construction and public services, financed by borrowing. If it is large enough and households spend rather than save the extra income, output could return towards full employment.", "closing a deflationary gap with fiscal policy. Use the multiplier and mention debt and lags as limits.") +
rw("An overheating boom", "In a boom a central bank may raise interest rates and a government may reduce spending growth to cool demand. These measures reduce AE, but they work with a lag and could push the economy into a downturn if overdone.", "closing an inflationary gap, and the risk of overshooting.")
)

mc_exam = [
  ("In a closed economy with no government there is an equilibrium level of national income of $1000 billion. Households always spend 80% of the income they receive. Full employment occurs when national income is $1200 billion. By how much must aggregate demand initially change to close the deflationary gap? (Oct/Nov 2021 · 33 · Q26, reworded)", ["−$200 billion", "−$40 billion", "+$40 billion", "+$200 billion"], 2, "Multiplier = 1 ÷ (1 − 0.8) = 5. Income must rise by $200bn, so AD must rise by 200 ÷ 5 = $40bn."),
  ("Which would be most likely to close an inflationary gap? (Practice, not a past paper question)", ["A rise in government spending", "A cut in income tax", "A rise in the rate of interest", "An increase in the money supply"], 2, "A higher interest rate lowers consumption and investment, so AE falls. The other options raise AE."),
  ("An economy is in equilibrium where national income is below the full employment level. Which is most likely? (Practice, not a past paper question)", ["Inflationary pressure and labour shortages", "A deflationary gap and unemployment", "A government budget surplus only", "Aggregate expenditure above output"], 1, "Equilibrium below full employment means AE at full employment is too low: a deflationary gap, with spare capacity and unemployment.")
]

exam = exam_page("equilibrium and inflationary and deflationary gaps",
  "The gap analysis is tested as a short written explanation on Paper 4 (with a diagram), and as diagram or calculation multiple choice on Paper 3, where you identify the gap or work out the injection needed. One Paper 4 essay and one multiple choice question are below, with practice questions of our own.",
  [("Essay parts, 12 and 13 marks", "2", "May/June 2020 (41 and 43) Q6(a), (b)"), ("Multiple choice (Paper 3)", "gap on a diagram and gap calculations", "2020 to 2025"), ("Practice questions", "2", "Equilibrium and the gap")],
  [
  eq("Based on May/June 2020 · 9708/41 and 43 · Q6(a)", "12 marks", "Explain what economists mean by an inflationary gap and discuss why this is considered to be an economic problem. Use a diagram to support your answer.",
     ["A clear definition: aggregate expenditure at the full employment level of income is greater than full employment output, shown on a labelled 45° diagram with the gap marked.",
      "Reasons it is a problem, at least three for the top level: rising inflation and falling real incomes, damage to expectations and wage demands, higher imports and a worse trade balance, a lower exchange rate, effects on savers and borrowers, and less private investment if uncertainty rises.",
      "Level 4 considers the relative importance of the effects, not just a list."],
     "Define with the diagram first. Then three problems, each with a short chain. Finish by ranking them."),
  eq("Based on May/June 2020 · 9708/41 and 43 · Q6(b)", "13 marks", "How far would you agree that the use of monetary policy is the most effective way to solve the problem of an inflationary gap?",
     ["Explain at least two monetary policy tools (for example a higher interest rate, a smaller money supply or tighter credit) and how each reduces AE.",
      "Explain alternatives: fiscal policy (cut G, raise taxes) and supply-side policy.",
      "Evaluation: lags, the sensitivity of consumption and investment to interest rates, effects on the exchange rate, and the effect of the policy on growth and unemployment. A conclusion comparing monetary with fiscal and supply-side options."],
     "Monetary policy channels first, then two alternatives, then a judgement that depends on the cause of the gap and the time scale.")
  ] + [eq("Practice (not a past paper question)", "8 marks", "An economy has equilibrium national income of $600bn, full employment income of $800bn and a multiplier of 4. Explain what type of gap exists and calculate the injection needed to close it.",
     ["Identify a deflationary gap because equilibrium income is below the full employment level.",
      "Calculate the gap in income as 800 − 600 = $200bn, then the change in AD needed as 200 ÷ 4 = $50bn.",
      "Explain how the multiplier lifts income by more than the initial injection, and name a policy (for example more government spending)."],
     "Name the gap. Show the working in two lines. Say how the injection is magnified and give a policy.",
     [[("k", "A deflationary gap exists because the equilibrium level of national income is below the full employment level, so aggregate expenditure at full employment is too low and the economy has spare capacity."), ("a", "The gap in income is $800bn minus $600bn, which is $200bn. Because the multiplier is 4, the required change in aggregate demand is $200bn divided by 4, which is $50bn.")],
      [("n", "An extra $50bn of government spending could be injected into the circular flow. The people who receive it may spend most of it, and those who receive that spending spend again, so income could rise by four times the injection, which would be enough to reach full employment."), ("e", "However, this would only work if households and firms spend rather than save the extra income, and the policy may take time and add to government debt.")]])],
  mcq_h="Multiple choice questions")

tips = tips_html(
  [("Draw the 45° diagram.", "Axes: income on the horizontal, aggregate expenditure on the vertical. Label the 45° line, the AE line, the equilibrium Y and the full employment Y<sub>F</sub>."),
   ("Mark the gap at Y<sub>F</sub>.", "It is the vertical distance between the AE line and the 45° line at full employment, not the horizontal distance between Y and Y<sub>F</sub>."),
   ("Use the multiplier the right way round.", "Required change in AD = gap in income ÷ multiplier. The multiplier turns a small injection into a larger change in income."),
   ("Say which direction the policy goes.", "A deflationary gap needs more spending, lower taxes or lower interest rates. An inflationary gap needs the opposite."),
   ("Do not call it a gap in output only.", "A deflationary gap is a shortage of expenditure. An output gap is the difference between actual and potential output. They are linked but not the same."),
   ("Evaluate with a Keynesian and a monetarist view.", "Keynesians think the economy can stay below full employment. Monetarists expect it to return to full employment, so they favour supply-side policy."),
   ("Use 'could' about the outcome.", "The effect of a policy depends on confidence, lags and the size of the multiplier.")],
  [("Deflationary gap", "A deflationary gap exists when aggregate expenditure at the full employment level of income is below full employment output."),
   ("Inflationary gap", "An inflationary gap exists when aggregate expenditure at full employment exceeds full employment output, so the excess demand pulls up the price level."),
   ("Closing the gap", "The government could close the gap by changing its own spending by the size of the gap, and the multiplier would then change national income by a multiple."),
   ("Evaluate", "However, if confidence is low, households may save the extra income, so the multiplier could be smaller than expected."),
   ("Link", "The size of the gap matters because a larger multiplier means a smaller injection is needed.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["evaluate"], CW["discuss"]]) + FC

js = '''
/* ---------- 45 degree diagram ---------- */
const GX0 = 70, GMX = 600, GSC = 0.6, GTOP = 36, GY0 = GTOP + GMX * GSC;
const tickSet = (gx, gy, x0, y0, xm, ym, step, grid) => { let o = ""; for (let v = 0; v <= xm + 0.001; v += step) { if (grid && v > 0) o += SV.line(gx(v), y0, gx(v), gy(ym), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(gx(v), y0, gx(v), y0 + 5, "", {}) + SV.text(gx(v), y0 + 18, v, "sm", { "text-anchor": "middle" }); }
  for (let v = step; v <= ym + 0.001; v += step) { if (grid) o += SV.line(x0, gy(v), gx(xm), gy(v), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(x0 - 5, gy(v), x0, gy(v), "", {}) + SV.text(x0 - 9, gy(v) + 4, v, "sm", { "text-anchor": "end" }); } return o; };
const niceStep = (mx) => [10, 20, 50, 100, 200, 500, 1000].find((s) => s >= mx / 6) || 1000;
function gapDraw(cfg, s) {
  const gx = (v) => GX0 + GSC * v, gy = (v) => GY0 - GSC * v, mx = GMX;
  const A = cfg.A0 + (s.sh || 0) * cfg.dA, sl = cfg.s, Y = A / (1 - sl), AEF = A + sl * cfg.YF, gap = AEF - cfg.YF;
  let o = tickSet(gx, gy, GX0, GY0, mx, mx, 100, true) + axes(GX0, GY0, gx(mx) + 8, GTOP - 14, "", "Aggregate expenditure, AE") + SV.text(gx(mx / 2), GY0 + 52, "National income, Y", "sm", { "text-anchor": "middle" });
  o += SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) + 6, gy(mx) + 4, "45° line", "t3", 1);
  o += SV.line(gx(0), gy(A), gx(mx), gy(A + sl * mx), s.sh > 0.01 ? "c2" : "c1", { "stroke-width": 3.5 }) + tag(gx(mx) + 6, gy(A + sl * mx) + 6, "AE", s.sh > 0.01 ? "t2" : "t1", 1);
  const left = Y <= cfg.YF;
  if (s.yf > 0) o += SV.line(gx(cfg.YF), GY0, gx(cfg.YF), gy(mx), "c3 dash", op(s.yf)) + tag(gx(cfg.YF) + (left ? 4 : -4), GY0 + 34, "YF = " + cfg.YF, "t3", s.yf, left ? "start" : "end");
  if (s.eq > 0) o += SV.line(gx(Y), GY0, gx(Y), gy(Y), "c1 dash", op(s.eq)) + SV.circle(gx(Y), gy(Y), 6, "dot1", op(s.eq)) + tag(gx(Y) + (left ? -4 : 4), GY0 + 34, "Y = " + Lib.fmtN(Y, 0), "t1", s.eq, left ? "end" : "start");
  if (s.gap > 0 && Math.abs(gap) > 0.5) { const hi = Math.max(cfg.YF, AEF); o += SV.line(gx(cfg.YF), gy(cfg.YF), gx(cfg.YF), gy(AEF), "c2", { "stroke-width": 8, ...op(s.gap) }) + tag(gx(cfg.YF) - 14, gy(hi) - 16, gap < 0 ? "deflationary gap = " + Lib.fmtN(-gap, 0) : "inflationary gap = " + Lib.fmtN(gap, 0), "t2", s.gap, "end"); }
  return o;
}
const DCFG = { A0: 120, dA: 80, s: 0.6, YF: 500 }, ICFG = { A0: 200, dA: -40, s: 0.6, YF: 400 };
$("#pic1").innerHTML = `<svg viewBox="0 0 620 ${GY0 + 66}" role="img" aria-label="Keynesian 45 degree diagram: aggregate expenditure line crossing the 45 degree line at equilibrium income below full employment">${gapDraw(DCFG, { sh: 0, yf: 1, eq: 1, gap: 1 })}</svg>`;
function gapStepper(el, cfg, label, steps, base) { Lib.stepper(el, { w: 620, h: GY0 + 66, label, base, draw: (s) => gapDraw(cfg, s), tween: 1100, dwell: 5600, steps }); }
gapStepper($("#stD"), DCFG, "AE line below full employment, deflationary gap closed by a rise in government spending", [
  { cap: "<b>The 45° line.</b> Every point has expenditure equal to income. Output settles only where AE meets this line.", s: { sh: 0 } },
  { cap: "<b>The AE line</b> starts at autonomous spending of 120 and slopes up with slope 0.6, because some of each extra dollar of income is spent on domestic output.", s: { sh: 0, eq: 0 } },
  { cap: "<b>Equilibrium.</b> The AE line meets the 45° line at Y = 120 ÷ (1 − 0.6) = <b>300</b>. At lower income AE is greater than output, so firms produce more. At higher income AE is less than output, so they cut back.", s: { sh: 0, eq: 1 } },
  { cap: "<b>Full employment</b> is at 500. The economy is 200 short of it.", s: { sh: 0, eq: 1, yf: 1 } },
  { cap: "<b>The deflationary gap.</b> At 500 AE is only 120 + 0.6 × 500 = 420, so AE is <b>80 short</b> of output. This vertical distance is the deflationary gap.", s: { sh: 0, eq: 1, yf: 1, gap: 1 } },
  { cap: "<b>Government spending rises by 80.</b> Autonomous spending is now 200 and the AE line shifts up. The multiplier is 1 ÷ 0.4 = 2.5, so income rises by 80 × 2.5 = <b>200</b>.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
  { cap: "<b>The gap is closed.</b> The new AE line cuts the 45° line at 500, the full employment level. The injection is the gap, 80, not the income shortfall of 200: the multiplier does the rest.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
], { sh: 0, eq: 0, yf: 0, gap: 0 });
gapStepper($("#stI"), ICFG, "AE line above full employment, inflationary gap closed by a cut in government spending", [
  { cap: "<b>Start.</b> Autonomous spending is 200 and the slope of AE is 0.6, so equilibrium is at 200 ÷ 0.4 = <b>500</b>.", s: { sh: 0, eq: 1 } },
  { cap: "<b>Full employment is only 400.</b> The economy cannot produce 500 in real terms, so extra demand cannot create extra output.", s: { sh: 0, eq: 1, yf: 1 } },
  { cap: "<b>The inflationary gap.</b> At 400 AE is 200 + 0.6 × 400 = 440, so AE is <b>40 above</b> output. This excess demand pulls up the price level.", s: { sh: 0, eq: 1, yf: 1, gap: 1 } },
  { cap: "<b>Government spending is cut by 40</b> (or taxes are raised enough to cut spending by 40). The AE line shifts down. Income falls by 40 × 2.5 = <b>100</b>.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
  { cap: "<b>The gap is closed.</b> The new AE line cuts the 45° line at 400. Inflationary pressure falls, though the cut could also reduce growth and jobs if it goes too far.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
], { sh: 0, eq: 0, yf: 0, gap: 0 });

/* ---------- Lab 1 ---------- */
function labGap() {
  if (!$("#sa") || !$("#sc") || !$("#st") || !$("#sm") || !$("#sf")) return;
  const A = +$("#sa").value, c = +$("#sc").value / 100, t = +$("#st").value / 100, m = +$("#sm").value / 100, YF = +$("#sf").value;
  const sl = c * (1 - t) - m, k = 1 / (1 - sl), Y = A * k, AEF = A + sl * YF, gap = AEF - YF, need = (YF - Y) / k;
  $("#r1").textContent = Lib.fmtN(sl, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = (need >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(need), 0) + "bn";
  const kind = Math.abs(gap) < 0.5 ? "none" : gap < 0 ? "def" : "inf";
  $("#rv").textContent = kind === "none" ? "Equilibrium is at full employment, so there is no gap." : kind === "def" ?
    `Equilibrium income of $${Lib.fmtN(Y, 0)}bn is below full employment of $${YF}bn. There is a deflationary gap of $${Lib.fmtN(-gap, 0)}bn. Autonomous spending would have to rise by $${Lib.fmtN(need, 0)}bn, which the multiplier of ${Lib.fmtN(k, 2)} turns into a rise in income of $${Lib.fmtN(YF - Y, 0)}bn.` :
    `Equilibrium income of $${Lib.fmtN(Y, 0)}bn is above full employment of $${YF}bn. There is an inflationary gap of $${Lib.fmtN(gap, 0)}bn. Autonomous spending would have to fall by $${Lib.fmtN(-need, 0)}bn, cutting income by $${Lib.fmtN(Y - YF, 0)}bn through the multiplier.`;
  const mx = Math.max(Y, YF) * 1.2, sc = 290 / mx, gx = (v) => 70 + sc * v, gy = (v) => 330 - sc * v;
  const stp2 = niceStep(mx);
  let o = tickSet(gx, gy, 70, 330, mx, mx, stp2, true) + axes(70, 330, 400, 25, "", "Expenditure") + SV.text(gx(mx / 2), 388, "National income", "sm", { "text-anchor": "middle" }) + SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) - 4, gy(mx) + 14, "45°", "t3", 1, "end") + SV.line(gx(0), gy(A), gx(mx), gy(A + sl * mx), "c1", { "stroke-width": 3 }) + tag(gx(mx) - 4, gy(A + sl * mx) - 6, "AE", "t1", 1, "end");
  o += SV.line(gx(YF), 330, gx(YF), gy(YF), "c3 dash") + tag(gx(YF), 366, "YF = " + YF, "t3", 1, "middle") + SV.line(gx(Y), 330, gx(Y), gy(Y), "c1 dash") + SV.circle(gx(Y), gy(Y), 6, "dot1") + tag(gx(Y), 380, "Y = " + Lib.fmtN(Y, 0), "t1", 1, "middle");
  if (kind !== "none") o += SV.line(gx(YF), gy(YF), gx(YF), gy(AEF), "c2", { "stroke-width": 6 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sa", label: "Autonomous spending ($bn) ", min: 50, max: 200, step: 10, value: 120, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g2"), { id: "sc", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g3"), { id: "st", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g4"), { id: "sm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g5"), { id: "sf", label: "Full employment income ($bn) ", min: 200, max: 800, step: 20, value: 500, fmt: (v) => v, onInput: labGap });
labGap();
btnTable("lbBtns", "lbOut", [
  ["Unemployment 11%, prices falling, firms have spare machines", "Deflationary gap", "AE at full employment is too low. Keynesian policy: more G, lower taxes, lower interest rates."],
  ["Labour shortages, inflation rising, imports surging", "Inflationary gap", "AE at full employment is too high. Policy: cut G, raise taxes or raise interest rates."],
  ["Output at potential, inflation on target, low unemployment", "No gap", "Equilibrium is at the full employment level of income."],
  ["A rise in the exchange rate cuts exports and raises imports in a boom", "Reduces an inflationary gap", "Net exports fall, so AE shifts down."],
  ["Business confidence collapses and investment falls", "Creates or widens a deflationary gap", "Autonomous investment falls, so AE shifts down and income falls by a multiple."]
], ["Situation", "What it is", "Why and policy"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which gap does each description fit?", ["Deflationary gap", "Inflationary gap"],
  [("Spare capacity and rising unemployment", 0), ("Excess demand pulling up prices", 1), ("AE at full employment is less than full employment output", 0), ("The AE line is above the 45° line at YF", 1), ("Keynesian solution is to cut government spending", 1), ("Keynesian solution is to borrow and spend more", 0), ("Japan's long period of low growth and weak prices", 0), ("A boom with labour shortages and rising wages", 1)],
  "Deflationary means too little expenditure; inflationary means too much.") + MATCH([
  ["Aggregate expenditure", "Planned spending at each level of national income (C + I + G + X − M)"],
  ["45° line", "Every point where expenditure equals income"],
  ["Full employment level of income", "The output when all resources are in use"],
  ["Deflationary gap", "AE at full employment falls short of full employment output"],
  ["Inflationary gap", "AE at full employment exceeds full employment output"],
  ["Autonomous spending", "Spending that does not vary with income; it shifts the AE line"]]) + ORDER(
  "Put the closing of a deflationary gap in order, starting with the first event.",
  ["The government increases its spending and borrows to pay for it", "Aggregate expenditure shifts upwards", "Firms produce more and hire more workers", "Households with more income spend more again", "National income rises by a multiple until it reaches full employment"],
  "The multiplier makes the final change in income larger than the original rise in spending.") + CALC([
  {"q": "Equilibrium national income is $600bn, full employment income is $800bn and the multiplier is 4. By how much must autonomous spending change to reach full employment? Give the answer in $bn.", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Gap in income ÷ multiplier.", "sol": "(800 − 600) ÷ 4 = <b>$50bn</b> (an increase)."},
  {"q": "In a closed economy with no government, mpc = 0.75. Equilibrium income is $1,200bn and full employment income is $1,000bn. By how much must autonomous spending change? Use a minus sign for a fall.", "a": -50, "unit": "$bn", "tol": 0.01, "hint": "k = 1 ÷ (1 − 0.75) = 4. Income must fall by 200.", "sol": "k = 4. Change in AD = (1,000 − 1,200) ÷ 4 = <b>−$50bn</b> (an inflationary gap)."},
  {"q": "An open economy with a government has mps = 0.1, mrt = 0.1 and mpm = 0.2. Full employment income is $540bn and income is $465bn. By how much must government spending rise to reach full employment? Give the answer in $bn.", "a": 30, "unit": "$bn", "tol": 0.01, "hint": "k = 1 ÷ (mps + mrt + mpm). Income gap is 75.", "sol": "k = 1 ÷ 0.4 = 2.5. Change in G = 75 ÷ 2.5 = <b>$30bn</b>."},
  {"q": "The AE line is AE = 100 + 0.5Y. Calculate equilibrium income.", "a": 200, "unit": "$bn", "tol": 0.01, "hint": "Set Y = 100 + 0.5Y.", "sol": "0.5Y = 100, so Y = <b>200</b>."}
]) + MCQ([
  ("The AE line cuts the 45° line at a level of income above the full employment level. What exists?", ["A deflationary gap", "An inflationary gap", "A budget surplus", "A trade deficit only"], 1, "AE at full employment exceeds output, which is an inflationary gap."),
  ("Which is the Keynesian solution to a deflationary gap?", ["Cut government spending", "Raise income tax", "Raise government spending, financed by borrowing", "Raise interest rates"], 2, "More autonomous spending shifts AE up and the multiplier lifts income."),
  ("What does a movement along the AE line show?", ["A change in autonomous spending", "A change in income, with autonomous spending unchanged", "A change in the multiplier", "A change in the price level"], 1, "A change in income moves the economy along the AE line; autonomous spending shifts the line."),
  ("The multiplier is 5 and a deflationary gap in income is $100bn. How much does AD have to rise?", ["$5bn", "$20bn", "$100bn", "$500bn"], 1, "Required change in AD = 100 ÷ 5 = $20bn."),
  ("Why may a deflationary gap persist, according to Keynesians?", ["Wages and prices adjust immediately", "Low confidence and sticky wages keep expenditure low", "The multiplier is zero", "The economy is always at full employment"], 1, "If wages and prices are slow to fall and confidence is weak, equilibrium can stay below full employment.")
], "qz1") + CARDS([
  ("Aggregate expenditure", "Total planned spending at each level of income: C + I + G + (X − M)."),
  ("Equilibrium national income", "The income where AE equals output: the AE line crosses the 45° line."),
  ("Full employment level of income", "Potential output, when all resources are in use."),
  ("Deflationary gap", "AE at full employment is below full employment output; spare capacity and unemployment."),
  ("Inflationary gap", "AE at full employment is above full employment output; the excess demand pulls up the price level."),
  ("Autonomous spending", "Spending that does not depend on income; a change shifts the AE line."),
  ("Required change in AD", "(Y at full employment − equilibrium Y) ÷ multiplier."),
  ("Keynesian view", "The economy can settle below full employment, so government demand management is needed.")]) + MCQ(mc_exam)

build("sy913", "equilibrium-full-employment-gaps", "Full Employment, Equilibrium and Inflationary and Deflationary Gaps", EY,
  "9.1.3 and national income determination: the Keynesian 45° diagram, the full employment level of income, inflationary and deflationary gaps and how to close them. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
