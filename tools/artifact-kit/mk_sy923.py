"""Syllabus 9.2.3 The business cycle (chapter 42). Run: python3 tools/artifact-kit/mk_sy923.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.2.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">business (trade) cycle</b> is the regular but uneven fluctuation of actual output around its long-run <b>trend</b>, with four phases: <b>boom</b>, <b>downturn or recession</b>, <b>trough or slump</b> and <b>recovery</b>. Cycles are caused by swings in <b>aggregate demand</b> (confidence, credit, investment and stock cycles, policy) and by <b>supply shocks</b> and technology. <b class="kw">Automatic stabilisers</b> such as progressive income tax and unemployment benefits smooth the cycle without any new decision. They reduce the size of swings but do not remove them.</p></div>

  <h2>1 · The four phases</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Phase</th><th>Output</th><th>Unemployment</th><th>Inflation</th><th>Typical mood</th></tr>
    <tr><td><b>Boom (peak)</b></td><td>Fast growth, output above trend, positive gap</td><td>Low, labour shortages</td><td>Rising</td><td>High confidence, rising investment and credit</td></tr>
    <tr><td><b>Downturn / recession</b></td><td>Growth slows then turns negative</td><td>Starts to rise</td><td>Slowing</td><td>Confidence falls, firms cut investment and stocks</td></tr>
    <tr><td><b>Trough (slump)</b></td><td>Lowest output, negative gap</td><td>High</td><td>Low, maybe deflation</td><td>Spare capacity everywhere, profits low</td></tr>
    <tr><td><b>Recovery (upturn)</b></td><td>Growth returns, gap narrows</td><td>Falls slowly (it lags)</td><td>Still low, then rising</td><td>Stocks rebuilt, confidence returns</td></tr>
  </table></div>
  <div class="tip"><b class="h">Know the definitions</b>A <b>recession</b> is usually two or more consecutive quarters of falling real GDP. A <b>depression</b> is a deep and long recession. <b>Trend growth</b> is the long-run average rate of growth of potential output. The cycle is the movement of <b>actual</b> output around that trend, which is why it links to the output gap (9.2.2).</div>

  <h2>2 · Causes of the cycle</h2>
  <div class="grid2">
    <div class="card"><h3>Demand-side causes</h3><ul>
      <li><b>Confidence and expectations:</b> optimism and pessimism can spread and feed on themselves (Keynes called these animal spirits).</li>
      <li><b>Multiplier and accelerator:</b> a change in spending changes income by a multiple, and a change in income changes investment by more (part of 41.3).</li>
      <li><b>Credit and interest rates:</b> easy credit fuels booms, a credit crunch or rate rises deepen downturns.</li>
      <li><b>Stock (inventory) cycle:</b> firms cut orders sharply in a downturn to run down stocks, then rebuild them.</li>
      <li><b>Policy:</b> late or wrong fiscal and monetary changes can add to swings.</li>
    </ul></div>
    <div class="card"><h3>Supply-side and external causes</h3><ul>
      <li><b>Oil and commodity price shocks</b> raise costs and cut output.</li>
      <li><b>Technology waves:</b> bursts of innovation raise potential output and investment, then fade (the real business cycle view).</li>
      <li><b>Global shocks:</b> a recession abroad cuts exports; a financial crisis spreads across borders.</li>
      <li><b>Natural disasters and pandemics</b> hit supply and demand together.</li>
    </ul></div>
  </div>

  <h2>3 · Automatic stabilisers</h2>
  <p><b>Automatic stabilisers</b> are features of the tax and benefit system that move the budget in the opposite direction to the cycle <b>without any government decision</b>.</p>
  <ul>
    <li><b>Progressive income tax:</b> in a boom more income is taxed at higher rates, so tax revenue rises faster than income, which dampens spending. In a downturn it falls faster, which cushions disposable income.</li>
    <li><b>Unemployment and means-tested benefits:</b> they rise in a downturn as more people qualify and fall in a boom.</li>
    <li><b>Corporation tax and VAT</b> also move with profits and spending.</li>
  </ul>
  <div class="tip"><b class="h">What they do and do not do</b>They lower the <b>multiplier</b> (higher tax rates and benefits mean less of each extra dollar is spent), so swings in income are smaller. The budget goes into <b>deficit in recessions</b> and towards <b>surplus in booms</b> automatically. They cannot stop a recession or give the economy a push to recover; that needs <b>discretionary</b> policy (a deliberate decision to change spending or taxes).</div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Automatic stabilisers</th><th>Discretionary fiscal policy</th></tr>
    <tr><td><b>Decision</b></td><td>None needed, built into the system</td><td>Government chooses to change G or T</td></tr>
    <tr><td><b>Timing</b></td><td>Immediate, no lag in decision</td><td>Lags in recognising, deciding and acting</td></tr>
    <tr><td><b>Strength</b></td><td>Cushions but does not reverse a downturn</td><td>Can be large and targeted</td></tr>
    <tr><td><b>Budget</b></td><td>Deficit in recession, surplus in boom, automatically</td><td>Deficit or surplus by choice</td></tr>
  </table></div>
'''

watch = '''
  <h2>1 · One business cycle, phase by phase</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Automatic stabilisers in a downturn</h2>
  <p>A fall in income hits households. See what the tax and benefit system does without any new decision.</p>
  <div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · How much do automatic stabilisers reduce a recession?</h2>
  <p>A fall in spending starts a downturn. Choose the size of the shock, the marginal propensity to consume and the average tax rate. Compare the fall in income without and with taxes acting as a stabiliser.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Multiplier, no tax</small><strong id="r1"></strong></div><div><small>Multiplier with tax</small><strong id="r2"></strong></div><div><small>Income saved by stabiliser</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 290" role="img" aria-label="Bars showing the fall in national income without and with a tax stabiliser"></svg></div></div></div>

  <h2>Lab 2 · Which phase of the cycle?</h2>
  <p>Choose a set of indicators and see which phase fits, and why.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which phase of the cycle?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the downturn in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The global financial crisis, 2008 to 2009", "A boom in housing credit ended when borrowers began to default. Banks cut lending, firms and households cut spending, world trade fell and many economies had their deepest recession since the 1930s. Unemployment rose for years afterwards, even once output began to recover.", "a credit-driven cycle with a severe downturn. Use it for causes (credit, confidence), the multiplier, hysteresis and the case for stimulus.") +
rw("The pandemic recession, 2020", "Lockdowns cut output sharply within weeks, then a fast recovery followed in many economies as restrictions eased and governments supported incomes. The fall was far deeper than normal but also shorter.", "a supply-and-demand shock rather than a normal credit cycle. Evaluate the idea that all recessions look the same.") +
rw("Tax receipts and benefits in a downturn", "In a recession income tax and VAT receipts fall and spending on unemployment benefits rises, so the budget deficit widens without any new law. Governments sometimes add to this with stimulus, but part of the widening is automatic.", "an example of automatic stabilisers. Say that a rising deficit in a recession is partly a result of the cycle, not only of policy choices.") +
rw("A stock cycle in manufacturing", "When car makers expect weak sales they cut orders for parts and run down stocks. Suppliers see a much larger fall in orders than the fall in final sales, so output drops sharply before it recovers.", "the stock cycle as a cause of swings. Link to the accelerator.")
)

mc_exam = [
  ("The table shows real GDP growth for three countries. What can be concluded? Brazil: 2014 +0.5%, 2015 −3.5%, 2016 −3.3%, 2017 +1.1%. Spain: 2012 −2.9%, 2013 −1.7%, 2014 +1.4%, 2015 +3.7%. (May/June 2022 · 31 · Q18, reworded)", ["Brazil was in the downturn of its trade cycle in 2015", "Spain's real GDP was smallest in 2014", "Brazil experienced the best recovery of the period", "Spain was in the downturn of its trade cycle in 2014"], 0, "Brazil's growth turned sharply negative in 2015, so it was in the downturn. Spain's growth turned positive in 2014, which is a recovery."),
  ("Which would be the least likely consequence of a large rise in unemployment during a recession? (May/June 2022 · 32 · Q23, reworded)", ["A fall in aggregate demand", "A fall in expenditure on welfare", "A fall in income tax revenue", "A fall in the rate of economic growth"], 1, "Welfare spending rises when more people are unemployed. The other three all follow from a downturn."),
  ("Higher government borrowing raises interest charges and reduces private investment. What is this an example of? (May/June 2023 · 32 · Q23, reworded)", ["An automatic stabiliser", "Crowding out", "The accelerator", "The substitution effect"], 1, "Crowding out is when government borrowing reduces private sector spending, often through higher interest rates."),
  ("Which pair of tax and benefit systems produces automatic stabilisation? (May/June 2025 · 32 · Q17, reworded)", ["A progressive income tax and means-tested benefits", "A progressive income tax and a universal flat-rate benefit", "A regressive income tax and means-tested benefits", "A regressive income tax and a universal benefit"], 0, "Progressive taxes and means-tested benefits respond most strongly to changes in income, so they move the budget against the cycle."),
  ("Which combination would be most likely to bring a country out of recession? (May/June 2024 · 32 · Q22, reworded)", ["Expansionary fiscal and monetary policy together with supply-side policies", "Expansionary fiscal policy and tight monetary policy", "Tight fiscal and monetary policy", "Supply-side policy alone"], 0, "Demand needs a boost now (fiscal and monetary) and supply-side policies raise capacity for later. Supply-side alone is too slow."),
  ("An economy has a sudden rise in inflation from higher energy prices and also enters a recession with rising unemployment. A fall in which would most reduce the recession without pushing prices up further? (May/June 2024 · 31 · Q22, reworded)", ["Direct taxation", "Government spending", "Indirect taxation", "The interest rate"], 2, "Cutting indirect taxes lowers prices directly while also raising real incomes. Cutting direct taxes, raising spending or cutting interest rates would add to demand-pull pressure."),
  ("What is the most likely result of a period of negative actual growth? (Oct/Nov 2024 · 33 · Q22, reworded)", ["A rise in the surplus on the financial account", "A rise in the deficit on the current account", "A rise in the rate of inflation", "A rise in the rate of unemployment"], 3, "Falling output means firms cut jobs, so unemployment is likely to rise."),
  ("Why might a cut in the interest rate fail to boost aggregate demand in a recession? (Oct/Nov 2024 · 33 · Q18, reworded)", ["Business confidence is low", "It causes deflation", "It raises the exchange rate", "It reduces the money supply"], 0, "If firms and households expect weak demand they may not borrow or spend even at low interest rates.")
]

exam = exam_page("the business cycle and recessions",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The cycle itself is mostly tested in data response parts, in Paper 3 multiple choice and as background to longer questions on policy in a recession. Reworded Paper 4 questions are below, with a practice question and model answer on automatic stabilisers, and eight Paper 3 multiple choice questions.",
  [("Data response parts, 3 to 6 marks", "3", "Feb/March 2023 (42) 1(a), (b), (c)"), ("Essay, 25 marks", "1", "Feb/March 2021 (42) Q6"), ("Essay part, 12 marks", "1", "Oct/Nov 2022 (43) Q5(a)"), ("Practice question", "1", "Automatic stabilisers"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on Feb/March 2023 · 9708/42 · Q1(a)", "3 marks", "State what is meant by a recession.",
     ["A recession is a period when real GDP (national output) falls (1), measured as negative growth (1), for at least two successive quarters (1)."],
     "Three short points: output, negative growth, two quarters. No need to explain causes."),
  eq("Based on Feb/March 2023 · 9708/42 · Q1(b)", "5 marks", "Analyse why governments borrow, and why some economists say a government should increase spending during a recession.",
     ["Governments borrow to finance spending that tax revenue does not cover, that is a budget deficit (about 2 marks).",
      "In a recession higher government spending raises aggregate demand, which raises income, output and employment, magnified by the multiplier, so actual growth could rise (about 3 marks).",
      "Credit that there is spare capacity in a recession, so extra demand is unlikely to raise prices much."],
     "Why borrow. Then a chain: G up, AD up, income, output and jobs up, multiplier. One sentence on spare capacity."),
  eq("Based on Feb/March 2023 · 9708/42 · Q1(c)", "6 marks", "Consider what is meant by the phrase 'government borrowing could crowd out the private sector'.",
     ["Crowding out means higher government spending uses up resources or finance that would have gone to private firms and households (2 marks).",
      "Mechanism: to fund a deficit the government sells bonds; to attract buyers it may have to offer higher interest rates (1), and this makes private borrowing dearer, so private investment and consumption fall (1 to 2).",
      "Credit evaluation: little crowding out in a deep recession, when there is plenty of spare capacity and low private demand for loans, but more near full employment."],
     "Define. Interest rate mechanism. Then when it is likely or unlikely to happen."),
  eq("Based on Feb/March 2021 · 9708/42 · Q6", "25 marks", "Explain why an economy might be in equilibrium at less than the full employment level of output, and critically evaluate alternative policies that might be used to move the economy to full employment output.",
     ["Explain with AD and AS or a Keynesian cross: equilibrium can settle where AD is too low (a deflationary gap), because wages and prices are sticky and spending (confidence, investment) can fall.",
      "Policies: fiscal (higher G, lower taxes), monetary (lower interest rates, quantitative easing), supply-side (to raise potential output), exchange rate and trade policy. Each should be explained with its channel.",
      "Critical evaluation: time lags, crowding out, the size of the multiplier, liquidity trap, debt, the risk of inflation near full employment, and whether the problem is demand or supply. A clear judgement on which works best in which circumstances."],
     "Explain the gap with a diagram. Two or three policies, each with channel then weakness. Compare them and conclude."),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q5(a)", "12 marks", "Consider, with the help of a circular flow diagram, why a policy of export-led growth is likely to work when a developed economy is in recession.",
     ["Circular flow with the recession shown as equilibrium below full employment, and exports as an injection raising income through the multiplier.",
      "Spare capacity means extra export orders can be met without much inflation.",
      "Evaluation: it depends on demand abroad (partners may also be in recession), the exchange rate, the price and quality of exports, and the time that firms take to find new markets."],
     "Draw the flow. Exports up, J greater than W, multiplier, spare capacity. Then foreign demand and the exchange rate.")
  ] + [eq("Practice (not a past paper question)", "8 marks", "Explain what is meant by automatic stabilisers and how they reduce the severity of the business cycle.",
     ["Definition: features of the tax and benefit system that change government spending and revenue automatically as income changes.",
      "Examples: progressive income tax and unemployment benefits, with direction of change in a downturn and a boom.",
      "Effect: lower multiplier, smaller swings in income, budget moves into deficit in a recession and towards surplus in a boom.",
      "Evaluation: they dampen but do not remove cycles and cannot drive a recovery."],
     "Define. Two examples with direction. Multiplier link. One limitation.",
     [[("k", "Automatic stabilisers are features of the tax and benefit system that move government revenue and spending in the opposite direction to the business cycle without any new government decision."), ("a", "For example, a progressive income tax takes a larger share of income in a boom and a smaller share in a downturn, and unemployment benefits rise when more people lose their jobs.")],
      [("n", "In a recession tax receipts fall faster than income and benefit payments rise, so households have more disposable income than they would otherwise, which limits the fall in consumption. Because part of each extra dollar of income is taxed, the multiplier is smaller, so any shock to spending changes national income by less. The budget moves automatically into deficit in a downturn and towards surplus in a boom."), ("e", "However, stabilisers only reduce the size of swings. They cannot bring about a recovery, so a deep recession may still need discretionary stimulus, and the larger deficit could build up debt if the downturn lasts.")]])],
  mcq_h="Multiple choice questions (Paper 3)")

tips = tips_html(
  [("Name the phase and give the evidence.", "Say boom, recession, trough or recovery, then link it to output, unemployment and inflation."),
   ("Recession means falling real GDP for two or more quarters.", "Do not use it for any slowdown in growth."),
   ("Unemployment lags.", "It keeps rising after output starts to recover, and keeps falling in a boom. This is why a recovery can feel like a recession."),
   ("Give causes in two groups.", "Demand-side (confidence, credit, the multiplier and accelerator, policy) and supply-side or external (oil prices, technology, global shocks)."),
   ("For stabilisers, say 'automatic'.", "No new decision is needed. Give progressive taxes and benefits, and the direction of change in both phases."),
   ("Say what they cannot do.", "Stabilisers reduce swings. They do not end a recession."),
   ("Use 'could' about crowding out.", "In a deep recession there is spare capacity, so crowding out may be small.")],
  [("Recession", "A recession is a period of falling real GDP for at least two consecutive quarters."),
   ("Phases", "As the economy moves from recovery to boom, output rises above trend, unemployment falls and inflationary pressure builds."),
   ("Stabilisers", "Progressive income tax acts as an automatic stabiliser because revenue falls faster than income in a downturn."),
   ("Multiplier link", "Because part of any extra income is taxed, the multiplier is smaller, so swings in income are reduced."),
   ("Evaluate", "However, stabilisers cannot bring about a recovery, so discretionary policy may still be needed.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture and Watch 1: the cycle ---------- */
const CX = (t) => 70 + t * 660, TR = (t) => 250 - t * 70, WV = (t) => TR(t) - 70 * Math.sin(2 * Math.PI * 1.5 * t);
function cycPath(p) { const pts = []; for (let t = 0; t <= p + 1e-9; t += 0.01) pts.push([CX(t), WV(t)]); return Lib.ptsPath(pts); }
function cycDraw(s) {
  let o = axes(70, 330, 740, 40, "Time", "Real GDP") + SV.line(CX(0), TR(0), CX(1), TR(1), "c3 dash") + tag(CX(1) - 4, TR(1) + 22, "trend growth", "t3", 1, "end");
  o += SV.path(cycPath(s.p), "c1");
  const mk = [[1 / 6, "Boom (peak)", -22, 1], [1 / 3, "Downturn / recession", -34, 2], [0.5, "Trough (slump)", 28, 3], [2 / 3, "Recovery", 28, 4], [5 / 6, "Boom (peak)", -22, 5]];
  mk.forEach(([t, l, dy, k]) => { const v = Math.max(0, Math.min(1, (s.p - t) / 0.03 + 0.5)); if (v > 0 && s.p >= t - 0.001) o += SV.circle(CX(t), WV(t), 6, k % 2 ? "dot4" : "dot2", op(v)) + tag(CX(t), WV(t) + dy, l, k === 1 || k === 5 ? "t4" : k === 3 ? "t2" : "t1", v, "middle"); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="Business cycle: output rising and falling around a rising trend through boom, recession, trough and recovery">${cycDraw({ p: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 360, label: "Business cycle drawn phase by phase around a rising trend line", base: { p: 0.01 }, draw: cycDraw, tween: 1400, dwell: 5600, steps: [
  { cap: "<b>Trend growth.</b> Potential output grows steadily over time (the dashed line). Actual output does not follow it exactly: it swings above and below, and that swing is the business cycle.", s: { p: 0.01 } },
  { cap: "<b>Boom.</b> Spending, investment and credit rise, output moves above trend (a positive output gap), unemployment is low and inflation rises.", s: { p: 0.17 } },
  { cap: "<b>Downturn and recession.</b> Confidence drops, firms cut investment and stocks, and growth slows then turns negative. If real GDP falls for two quarters or more, it is a <b>recession</b>.", s: { p: 0.34 } },
  { cap: "<b>Trough.</b> Output is at its lowest, well below trend (a negative gap). Unemployment is high, inflation is low and profits are poor.", s: { p: 0.5 } },
  { cap: "<b>Recovery.</b> Stocks are rebuilt and demand returns. Growth is positive again, the gap narrows, and unemployment falls slowly because firms hire late.", s: { p: 0.68 } },
  { cap: "<b>The next boom.</b> The cycle repeats, but never exactly. The length and size of each phase differ, which is why governments use policy and automatic stabilisers to smooth it.", s: { p: 0.84 } },
] });

/* ---------- Watch 2: automatic stabilisers ---------- */
function stabDraw(s) {
  const names = ["Income", "Tax paid", "Benefits received", "Disposable income"], base = 280, k = 7, xs = [110, 270, 430, 590];
  let o = SV.line(60, base, 740, base) + tag(60, 36, "Change in a household group's finances, $ per month", "t1");
  [s.a, s.b, s.c, s.d].forEach((v, i) => { const h = Math.abs(v) * k, y = v >= 0 ? base - h : base, cls = i === 3 ? "f3" : v >= 0 ? "f1" : "f2"; o += SV.rect(xs[i], y, 90, Math.max(h, 2), cls) + tag(xs[i] + 45, v >= 0 ? y - 8 : y + h + 16, (v > 0 ? "+" : "") + Lib.fmtN(v, 0), i === 3 ? "t3" : v >= 0 ? "t1" : "t2", 1, "middle") + SV.text(xs[i] + 45, base + 24, names[i], "sm bd", { "text-anchor": "middle" }); });
  if (s.n > 0) o += tag(400, 70, "Without stabilisers disposable income would fall by 10", "t2", s.n, "middle");
  if (s.m > 0) o += tag(400, 96, "The tax and benefit system cushions the fall", "t3", s.m, "middle");
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 330, label: "Bars showing income falling, tax paid falling, benefits rising and disposable income falling by less", base: { a: 0, b: 0, c: 0, d: 0, n: 0, m: 0 }, draw: stabDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>The downturn hits.</b> Households' pre-tax income falls by 10 a month as firms cut hours and jobs.", s: { a: -10 } },
  { cap: "<b>Tax paid falls.</b> With a progressive income tax, the loss of income pushes people into lower tax bands, so tax paid falls by <b>more than proportionally</b>.", s: { a: -10, b: -3, n: 1 } },
  { cap: "<b>Benefits rise.</b> More people qualify for unemployment and means-tested benefits, so benefits received rise.", s: { a: -10, b: -3, c: 2, n: 1 } },
  { cap: "<b>Disposable income falls by less.</b> The fall is 10 − 3 (less tax) − 2 (more benefits) = 5, half of what it would have been. Households keep spending more than they otherwise would, so the recession is milder.", s: { a: -10, b: -3, c: 2, d: -5, n: 1, m: 1 } },
  { cap: "<b>The budget moves automatically.</b> Lower tax receipts and higher benefit payments push the government budget towards a <b>deficit</b> with no new law. In a boom the reverse happens and the budget moves towards surplus.", s: { a: -10, b: -3, c: 2, d: -5, n: 1, m: 1 } },
] });

/* ---------- Lab 1: stabilisers ---------- */
function labStab() {
  if (!$("#sh") || !$("#mp") || !$("#tx")) return;
  const S = +$("#sh").value, c = +$("#mp").value / 100, t = +$("#tx").value / 100, k0 = 1 / (1 - c), k1 = 1 / (1 - c * (1 - t)), f0 = S * k0, f1 = S * k1;
  $("#r1").textContent = Lib.fmtN(k0, 2); $("#r2").textContent = Lib.fmtN(k1, 2); $("#r3").textContent = "$" + Lib.fmtN(f0 - f1, 0) + "bn";
  $("#rv").textContent = `A $${S}bn fall in spending cuts national income by $${Lib.fmtN(f0, 0)}bn with no tax and $${Lib.fmtN(f1, 0)}bn with a ${Math.round(t * 100)}% tax rate. The tax system saves $${Lib.fmtN(f0 - f1, 0)}bn of lost output, which is why a more progressive system smooths the cycle.`;
  const mx = Math.max(f0, 1), y = (v) => 250 - v / mx * 200;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, y(f0), 90, 250 - y(f0), "f2") + SV.rect(240, y(f1), 90, 250 - y(f1), "f3") + tag(135, y(f0) - 6, "$" + Lib.fmtN(f0, 0) + "bn", "t2", 1, "middle") + tag(285, y(f1) - 6, "$" + Lib.fmtN(f1, 0) + "bn", "t3", 1, "middle") + SV.text(135, 272, "No tax", "sm bd", { "text-anchor": "middle" }) + SV.text(285, 272, "With tax rate", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sh", label: "Fall in spending ($bn) ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labStab });
Lib.slider($("#g2"), { id: "mp", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 75, fmt: (v) => v, onInput: labStab });
Lib.slider($("#g3"), { id: "tx", label: "Average tax rate (%) ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v, onInput: labStab });
labStab();
btnTable("lbBtns", "lbOut", [
  ["Growth 4.5%, unemployment 3.8%, inflation rising", "Boom (peak)", "Above-trend growth, a positive output gap, tight labour market and rising prices"],
  ["Growth slowing to 0.3%, firms cutting orders", "Downturn", "Growth is still positive but falling fast; confidence and investment are dropping"],
  ["GDP down for two quarters, unemployment rising", "Recession", "Negative growth for two or more quarters, unemployment rising, inflation slowing"],
  ["Output at its lowest, unemployment 9%, inflation near zero", "Trough (slump)", "Lowest output, a large negative gap and heavy spare capacity"],
  ["Growth back to 2%, stocks rebuilt, unemployment still high", "Recovery", "Output rising again but unemployment lags behind and the gap is still negative"]
], ["Indicators", "Phase", "Why"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which phase of the cycle is each description of?", ["Boom", "Recession / trough", "Recovery"],
  [("Unemployment at a record low and firms cannot find workers", 0), ("Output falling for two quarters in a row", 1), ("Growth returns but unemployment is still falling slowly", 2), ("Inflation rising and the output gap positive", 0), ("Firms running down stocks and cutting investment", 1), ("Stocks being rebuilt and orders picking up", 2), ("Output at its lowest, profits poor, large spare capacity", 1), ("Housing prices and credit growing fast, confidence high", 0)],
  "Match output, unemployment and mood to the phase.") + MATCH([
  ["Recession", "Falling real GDP for at least two consecutive quarters"],
  ["Trend growth", "The long-run average rate of growth of potential output"],
  ["Automatic stabiliser", "A tax or benefit that offsets the cycle without a new decision"],
  ["Discretionary policy", "A deliberate change in government spending or taxes"],
  ["Stock cycle", "Swings in output caused by firms building up and running down stocks"],
  ["Animal spirits", "Waves of optimism and pessimism that drive spending"]]) + ORDER(
  "Put a downturn in order, starting with the first event.",
  ["Consumer and business confidence falls", "Households cut spending and firms cut investment and stocks", "Firms produce less and cut jobs", "Unemployment rises and incomes fall further", "Tax revenue falls and benefits rise, so the deficit widens"],
  "The multiplier makes each round of lost income reduce spending again, until stabilisers and policy cushion the fall.") + CALC([
  {"q": "A closed economy has a marginal propensity to consume of 0.75 and an average tax rate of 20%. Calculate the multiplier. Use 1 ÷ (1 − MPC × (1 − t)).", "a": 2.5, "tol": 0.01, "hint": "MPC × (1 − t) = 0.75 × 0.8.", "sol": "0.75 × 0.8 = 0.6, so multiplier = 1 ÷ (1 − 0.6) = <b>2.5</b>."},
  {"q": "Using the multiplier in the previous question, by how much does national income fall (in $bn) if spending falls by $20bn?", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Change in income = multiplier × change in spending.", "sol": "2.5 × 20 = <b>$50bn</b>."},
  {"q": "Real GDP growth in four quarters is −0.3%, −0.8%, −0.5% and +0.4%. How many consecutive quarters of negative growth were there?", "a": 3, "tol": 0.01, "hint": "Count the run before growth turns positive.", "sol": "Quarters 1 to 3 were negative: <b>3</b>, so the economy was in recession."},
  {"q": "Potential GDP is $1,000bn and grows at 2.5% a year. After two years actual GDP is $1,020bn. Calculate the output gap as a percentage of potential GDP (use a minus sign if negative, one decimal place).", "a": -2.9, "tol": 0.1, "hint": "Potential after two years is 1000 × 1.025².", "sol": "Potential = 1000 × 1.050625 = 1050.6. Gap = (1020 − 1050.6) ÷ 1050.6 × 100 = <b>−2.9%</b>."}]) + MCQ([
  ("Which is most likely to be found at the trough of a business cycle?", ["A positive output gap", "Rapidly rising inflation", "Spare capacity and high unemployment", "Labour shortages"], 2, "At the trough output is far below trend, so there is spare capacity and unemployment is high."),
  ("A recession is normally defined as:", ["Any fall in the rate of inflation", "A fall in real GDP for two or more consecutive quarters", "A fall in the stock market", "Growth below 2% for a year"], 1, "A recession is a period of negative real growth, usually two quarters or more."),
  ("Which is an automatic stabiliser?", ["A cut in interest rates by the central bank", "A new spending programme announced in a budget", "Unemployment benefits that rise as unemployment rises", "A fall in the exchange rate"], 2, "Benefits change without any new decision when unemployment changes."),
  ("What effect do automatic stabilisers have on the multiplier?", ["They raise it", "They reduce it", "They have no effect", "They make it negative"], 1, "Taxes and benefits mean less of each extra dollar of income is spent, so the multiplier is lower."),
  ("Which would be a cause of the business cycle from the supply side?", ["A fall in consumer confidence", "A sharp rise in oil prices", "A rise in the interest rate", "A stock cycle"], 1, "An oil price shock raises costs and cuts output. The others are demand-side causes.")
], "qz1") + CARDS([
  ("Business cycle", "Fluctuations of actual output around the long-run trend."),
  ("Boom", "Phase with above-trend growth, low unemployment and rising inflation."),
  ("Recession", "Falling real GDP for two or more consecutive quarters."),
  ("Trough", "Lowest point of the cycle: spare capacity, high unemployment."),
  ("Recovery", "Growth returns and the output gap narrows; unemployment lags."),
  ("Automatic stabiliser", "Tax or benefit that cushions the cycle without any new decision."),
  ("Discretionary policy", "A deliberate change in G or T to influence demand."),
  ("Crowding out", "Government borrowing reducing private sector spending, usually via higher interest rates.")]) + MCQ(mc_exam)

build("sy923", "business-cycle", "The Business Cycle and Automatic Stabilisers", EY,
  "9.2.3: the phases of the business cycle, its demand-side and supply-side causes and how automatic stabilisers cushion it. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
