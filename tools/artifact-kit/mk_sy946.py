"""Syllabus 9.4.6 Policies to reduce inflation and their effectiveness. Run: python3 tools/artifact-kit/mk_sy946.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.4.6"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The best policy to reduce inflation depends on its <b>cause</b>. <b>Demand-pull</b> inflation is tackled by cutting aggregate demand: <b>higher interest rates</b> and a tighter money supply (monetary policy), and <b>lower government spending or higher taxes</b> (fiscal policy). <b>Cost-push</b> inflation needs policies that cut costs or raise supply: <b>supply-side policy</b>, an <b>appreciation</b> of the exchange rate and <b>incomes policy</b>. Every policy has costs, especially <b>lost output and jobs</b>, <b>time lags</b> and uncertainty, so effectiveness depends on the cause, the credibility of the policy and expectations.</p></div>

  <h2>1 · Match the policy to the cause</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause of inflation</th><th>What is happening</th><th>Appropriate policies</th></tr>
    <tr><td><b>Demand-pull</b></td><td>AD rises faster than productive capacity (a positive output gap)</td><td>Higher interest rates, slower money growth, lower government spending, higher taxes</td></tr>
    <tr><td><b>Cost-push</b></td><td>Higher wages, import prices, oil or taxes shift SRAS left</td><td>Supply-side policy, exchange rate appreciation, wage restraint; demand cuts only at a high cost in output</td></tr>
    <tr><td><b>Imported</b></td><td>A weak currency or higher world prices raise import costs</td><td>Higher interest rates to support the currency, supply-side policy</td></tr>
    <tr><td><b>Expectations</b> (wage-price spiral)</td><td>People expect inflation and bargain accordingly</td><td>A credible inflation target, independent central bank, forward guidance</td></tr>
    <tr><td><b>Excess money growth</b> (monetarist)</td><td>Money supply growing faster than output</td><td>Control the money supply (rules, higher rates, reduced QE)</td></tr>
  </table></div>

  <h2>2 · Monetary policy</h2>
  <ul>
    <li><b>Raise the interest rate.</b> Borrowing is dearer, saving more rewarding, so consumption and investment fall and AD shifts left. A higher rate may attract hot money, raising the exchange rate, which lowers import prices and exports.</li>
    <li><b>Control the money supply:</b> sell government bonds, raise reserve requirements, reverse quantitative easing.</li>
    <li><b>Inflation targeting and an independent central bank:</b> a clear target (such as 2%) and independence from politicians increase credibility, which lowers expected inflation.</li>
  </ul>
  <h3>The monetary transmission mechanism</h3>
  <div id="pic1" class="card"></div>
  <p>A rise in the central bank's rate works through several <b>channels</b>: the <b>borrowing channel</b> (loan and mortgage rates rise), the <b>saving channel</b> (saving is more attractive), the <b>asset price and wealth channel</b> (bond, share and house prices fall), the <b>exchange rate channel</b> (the currency rises, so import prices fall and exports are less competitive) and the <b>expectations channel</b> (people expect lower inflation). The effect takes <b>12 to 24 months</b>.</p>
  <p><b>Why it may not work in practice:</b> time lags; consumers and firms may be insensitive to rates (interest inelastic) or already heavily in debt; banks may not pass on the change; low confidence or a liquidity trap when cutting rates; the change may affect cost-push inflation little; the exchange rate may not respond as expected.</p>

  <h2>3 · Fiscal policy</h2>
  <ul>
    <li><b>Lower government spending or higher taxes</b> reduce AD (contractionary or deflationary fiscal policy), helped by the multiplier.</li>
    <li>Strengths: direct effect on demand; it can be targeted.</li>
    <li>Limits: politically difficult (unpopular), time lags in decisions, can harm growth and jobs, and does not tackle cost-push inflation. Higher indirect taxes can <b>raise</b> prices directly.</li>
  </ul>

  <h2>4 · Supply-side policy, the exchange rate and incomes policy</h2>
  <ul>
    <li><b>Supply-side:</b> training, competition, infrastructure and flexible labour markets shift SRAS and LRAS right, which cuts cost pressure and raises output at the same time. It is the most sustainable but the slowest.</li>
    <li><b>Exchange rate appreciation:</b> lowers the price of imported goods and raw materials, so it reduces cost-push and imported inflation, but it harms exporters and the current account.</li>
    <li><b>Incomes policy and wage and price controls:</b> limits on pay rises (especially in the public sector) cut wage-push pressure and expectations, but are hard to enforce and can distort markets or lead to strikes.</li>
  </ul>

  <h2>5 · Effectiveness</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Why it matters</th></tr>
    <tr><td><b>The cause</b></td><td>Tight demand policy cures demand-pull inflation, but it is a costly cure for cost-push inflation (stagflation).</td></tr>
    <tr><td><b>Costs</b></td><td>Lower output and higher unemployment (the Phillips curve trade-off; the sacrifice ratio).</td></tr>
    <tr><td><b>Time lags</b></td><td>Monetary policy takes 12 to 24 months, fiscal decisions take time, supply-side policy takes years.</td></tr>
    <tr><td><b>Credibility and expectations</b></td><td>If people believe the target, they moderate wage demands and the cost of disinflation falls.</td></tr>
    <tr><td><b>Side effects</b></td><td>Higher rates hurt borrowers and exporters and can raise the exchange rate; spending cuts hit public services and equity.</td></tr>
    <tr><td><b>Global factors</b></td><td>Imported inflation from world commodity prices is outside domestic control.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Conclusion for essays</b>Say which cause you are tackling. Use demand-side tools for demand-pull and supply-side tools for cost-push, and credibility to lower the cost. A mix, plus patience, is usually needed.</div>
'''

watch = '''
  <h2>1 · The monetary transmission mechanism</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Demand-pull versus cost-push: the right cure</h2>
  <div id="stA"></div>
'''

explore = '''
  <h2>Lab 1 · A rise in interest rates</h2>
  <p>Choose the rate rise and how sensitive spending is. The lab shows the fall in AD, the fall in inflation and the cost in unemployment, using simple rules of thumb.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Fall in aggregate demand</small><strong id="r1"></strong></div><div><small>Fall in inflation</small><strong id="r2"></strong></div><div><small>Rise in unemployment</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars showing the fall in consumption, investment and total aggregate demand after a rise in interest rates"></svg></div></div></div>

  <h2>Lab 2 · Policy profile</h2>
  <p>Pick a policy to see which type of inflation it tackles, how fast it works and its main cost.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which policy fits which cause?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the transmission mechanism in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The Volcker disinflation, 1979 to 1982", "The US Federal Reserve raised its interest rate to about 20% to end high inflation. Inflation fell from over 13% to under 4%, but unemployment rose to nearly 11% and the economy had a deep recession.", "monetary policy working but at a heavy cost in output and jobs. A good example for the sacrifice ratio and credibility.") +
rw("Inflation targeting in the UK, 1992 to now", "The UK adopted an inflation target after leaving the exchange rate mechanism, and gave the Bank of England independence in 1997. Inflation was close to target for many years until global energy and supply shocks in 2021 to 2022.", "credibility and an independent central bank. Evaluate with the 2021 to 2022 supply-driven inflation, which interest rates could not fix quickly.") +
rw("The 2022 inflation surge", "Inflation reached 9% or more in many economies, driven partly by supply shocks (energy prices, supply chains) and partly by strong demand. Central banks raised interest rates rapidly, while some governments also used price caps and subsidies.", "the cause matters: rate rises work on the demand side but cannot cut the world price of gas.") +
rw("Wage restraint and incomes policy in the 1970s", "Several governments used wage and price controls to fight inflation. The controls held down prices for a time, but when they were removed pay and prices jumped, and the underlying causes were not addressed.", "incomes policy as a short-term cure for cost-push inflation, with the risk of distortion and a rebound.")
)

mc_exam = [
  ("In a closed economy the central bank raises interest rates to reduce rising inflation. Which policy objective is it targeting? (May/June 2025 · 32 · Q21, reworded)", ["A current account surplus", "Faster economic growth", "Full employment", "Stable prices"], 3, "Higher rates reduce demand and are used to control inflation."),
  ("An economy is operating at full employment. Which policy is most likely to raise real output without raising inflation in the short term? (Oct/Nov 2022 · 31 · Q30, reworded)", ["Subsidies to increase export earnings", "Quantitative easing", "Labour market reforms that raise output per hour", "A cut in income tax"], 2, "Supply-side reforms raise productivity and capacity, so output rises without extra demand."),
  ("A government cuts its main interest rate to stimulate growth. What might reduce the effectiveness of this? (May/June 2021 · 31 · Q18, reworded)", ["Rising investor expectations", "More borrowing taking place", "Falling savings", "A falling marginal propensity to consume"], 3, "If households spend a smaller share of any extra income, cheaper borrowing raises spending less."),
  ("A government wants to raise real GDP using only fiscal and monetary policies. Which combination is most effective? (May/June 2021 · 31 · Q23, reworded)", ["A bigger budget deficit and the central bank buying back government bonds", "A smaller budget deficit and the central bank selling bonds", "A smaller deficit and lower rates", "A bigger deficit and higher interest rates"], 0, "A larger deficit raises AD and the central bank buying bonds lowers interest rates and raises the money supply."),
  ("The government raises interest rates to reduce inflation. What will also result? (Feb/March 2024 · 32 · Q23, reworded)", ["A depreciation of the currency", "A fall in savings", "A reduction in economic growth", "A reduction in unemployment"], 2, "Higher rates cut spending and investment so growth slows."),
  ("Which macroeconomic policy is most likely to be used as a long-run means of reducing inflationary pressure? (Feb/March 2020 · 32 · Q29, reworded)", ["Exchange rate policy", "Fiscal policy", "Monetary policy", "Supply-side policy"], 3, "Supply-side policy raises capacity and productivity, which reduces cost pressure over time.")
]

exam = exam_page("policies to reduce inflation and the monetary transmission mechanism",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Inflation policy and the transmission mechanism appear as 12 and 13 mark Paper 4 questions and in 20 mark essays on monetary policy. Reworded questions are below, with a practice question and six Paper 3 multiple choice questions.",
  [("Essay parts, 12 and 13 marks", "3", "May/June 2020 (41) Q6(b); May/June 2021 (43) Q7(b); May/June 2022 (41, 43) Q6(a)"), ("Practice question", "1", "Policies for cost-push inflation"), ("Multiple choice (Paper 3)", "6 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2022 · 9708/41 and 43 · Q6(a)", "12 marks", "Explain what is meant by a transmission mechanism of monetary policy and consider why it might not work in practice.",
     ["The mechanism is the chain of effects from a change in the policy interest rate to spending, output and inflation: loan and deposit rates, saving and borrowing, asset prices and wealth, the exchange rate and expectations, leading to a change in AD and prices.",
      "Why it might not work: time lags; consumers and firms with low interest elasticity of demand; banks not passing on rate changes; confidence and expectations; liquidity trap; saving behaviour; global factors that dominate (the exchange rate or world prices).",
      "Level 4 (9 to 12) needs a clear explanation of the chain and at least two reasons it might fail."],
     "Draw the chain in words. Then three reasons it may break down."),
  eq("Based on May/June 2021 · 9708/43 · Q7(b)", "13 marks", "Monetary policy relies heavily on the theory of a monetary transmission mechanism. Explain how a monetary transmission mechanism works and discuss its effectiveness.",
     ["Explain the mechanism with the main channels: borrowing, saving, wealth or asset prices, exchange rate and expectations; show the effect on AD and the price level.",
      "Effectiveness: works well on demand-pull inflation when interest rates are well above zero; lags of 12 to 24 months; weaker with a low confidence, high debt, a liquidity trap or QE with weak lending; little power over cost-push inflation.",
      "A conclusion about overall effectiveness."],
     "Channels first. Then when it works, when it fails. Judge."),
  eq("Based on May/June 2020 · 9708/41 · Q6(b)", "13 marks", "How far would you agree that monetary policy is the most effective way to solve the problem of an inflationary gap?",
     ["Define the inflationary gap (actual output above potential, AD too high) and show it on a diagram.",
      "Monetary policy: higher interest rates, slower money growth, a stronger currency; works through the transmission mechanism to cut AD.",
      "Alternatives: contractionary fiscal policy (immediate effect on spending, politically difficult), supply-side policy (raises potential output, slow).",
      "Compare effectiveness: speed, cost in output and jobs, ease of use and credibility, and conclude on which is best for this problem."],
     "Gap diagram. Monetary policy and its limits. Fiscal and supply-side alternatives. Compare and judge."),
  eq("Practice (not a past paper question)", "12 marks", "Explain why policies that reduce aggregate demand may be an inefficient way to tackle cost-push inflation, and suggest better alternatives.",
     ["Cost-push inflation comes from a leftward shift of SRAS (higher costs), not from excess demand. On an AD and AS diagram it gives a higher price level and lower output.",
      "Cutting AD reduces prices a little but cuts output and jobs further: a large cost for a small gain in prices (a worse Phillips curve trade-off).",
      "Alternatives: supply-side policy to cut costs, an appreciating exchange rate (for imported costs), wage restraint or competition policy; lowering expectations by credible policy.",
      "Evaluation: some demand tightening may be needed if expectations are rising; supply-side policy is slow; appreciation harms exports."],
     "Diagram. Why AD cuts are costly. Alternatives. A limit.",
     [[("k", "Cost-push inflation occurs when firms' costs rise, for example because of dearer oil or higher wages, which shifts the short-run aggregate supply curve to the left. This raises the price level and reduces output, so the economy has higher inflation and a negative output gap at the same time (stagflation)."), ("n", "Policies that reduce aggregate demand, such as higher interest rates, would lower the price level a little but also reduce output and employment still further. Because the problem is on the supply side, a large rise in unemployment would be needed to achieve a small fall in inflation, so it is an inefficient policy.")],
      [("n", "Better alternatives would deal with costs directly. Supply-side policies such as training and competition could raise productivity and shift the supply curves back to the right; an appreciating exchange rate would reduce the cost of imported inputs; and wage restraint or a credible inflation target could reduce wage pressure and expectations."), ("e", "However, supply-side policies take years to work and an appreciation would hurt exporters, and if workers have begun to expect higher inflation, some tightening of demand may also be needed to stop a wage-price spiral.")]])
  ],
  )

tips = tips_html(
  [("Start by diagnosing the cause.", "Demand-pull or cost-push? The answer decides which policy is appropriate."),
   ("Draw AD and AS.", "AD shifting left for demand-pull cures; SRAS shifting left for cost-push, which demand cuts cannot fix cheaply."),
   ("Explain the transmission mechanism step by step.", "Rate up, borrowing and saving, spending down, AD down, price level down."),
   ("Mention the lag.", "12 to 24 months for monetary policy."),
   ("State the cost.", "Lost output and jobs. Link to the Phillips curve."),
   ("Credibility lowers the cost.", "An independent central bank and a clear target reduce expectations."),
   ("Compare policies.", "Monetary: fast to change but lagged. Fiscal: direct but political. Supply-side: slow but lasting.")],
  [("Cause", "Because this is cost-push inflation, a fall in aggregate demand would reduce output as well as prices."),
   ("Transmission", "A rise in the interest rate raises the cost of borrowing, so consumption and investment could fall, shifting AD to the left."),
   ("Lag", "However, monetary policy works with a time lag of one to two years, so the effect may arrive when the economy has already slowed."),
   ("Credibility", "If the central bank is credible, expected inflation falls, which reduces the cost of lowering inflation."),
   ("Judge", "On balance, the most effective policy depends on the cause and a mix of policies is likely to be needed.")],
  [CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Transmission chain ---------- */
const TB = [["Central bank raises the policy rate", 40, 30, "f4"], ["Loan and mortgage rates rise; saving pays more", 40, 120, "f1"], ["Consumption and investment fall; asset prices fall", 40, 210, "f1"], ["Aggregate demand shifts left", 400, 210, "f2"], ["Output gap narrows, price pressure falls", 400, 120, "f3"], ["Inflation falls (after 12 to 24 months)", 400, 30, "f3"]];
function transDraw(s) {
  let o = "";
  TB.forEach(([l, x, y, c], i) => { const v = Math.max(0, Math.min(1, s.n - i)); if (v <= 0) return; o += SV.rect(x, y, 320, 62, c, op(v)) + SV.text(x + 160, y + 36, l, "lbl bd", { "text-anchor": "middle", ...op(v) }); });
  const AR = [[200, 94, 200, 118, "d"], [200, 184, 200, 208, "d"], [365, 241, 395, 241, "r"], [560, 208, 560, 184, "u"], [560, 118, 560, 94, "u"]];
  AR.forEach((a, i) => { const v = Math.max(0, Math.min(1, s.n - i - 0.5)); if (v > 0) o += arrow(a[0], a[1], a[2], a[3], a[4], "c1", v); });
  if (s.x > 0) o += tag(380, 316, "also: exchange rate rises, import prices fall, and expectations of inflation fall", "t3", s.x, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Chain from a rise in the policy interest rate to lower inflation">${transDraw({ n: 7, x: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 330, label: "Monetary transmission mechanism from a higher interest rate to lower inflation", base: { n: 0, x: 0 }, draw: transDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The decision.</b> Inflation is above target, so the central bank raises its policy interest rate.", s: { n: 1.4 } },
  { cap: "<b>Market rates.</b> Banks raise lending rates, so loans and mortgages are dearer. Saving earns more.", s: { n: 2.4 } },
  { cap: "<b>Spending.</b> Households cut consumption, firms cut investment, and the value of bonds, shares and houses falls, reducing wealth and spending.", s: { n: 3.4 } },
  { cap: "<b>Aggregate demand falls.</b> The AD curve shifts to the left. A stronger currency and lower inflation expectations also work in the same direction.", s: { n: 4.4, x: 1 } },
  { cap: "<b>Prices.</b> Demand falls back towards capacity and inflation falls, but only after a lag of 12 to 24 months, at the cost of lower growth and higher unemployment.", s: { n: 6.5, x: 1 } },
] });

/* ---------- AD and AS: demand-pull and cost-push ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adasDraw(s) {
  const a = s.a, sh = s.sh, lr = 60, Q = (a - 15 + 0.7 * sh) / 1.6, P = 15 + 0.7 * (Q - sh);
  let o = axes(70, 320, 740, 30, "Real GDP", "Price level") + SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  o += SV.line(AX(0), AY(15 + 0.7 * (0 - sh)), AX(100), AY(15 + 0.7 * (100 - sh)), "c2") + tag(AX(100) - 4, AY(15 + 0.7 * (100 - sh)) - 8, "SRAS", "t2", 1, "end");
  o += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  o += SV.circle(AX(Q), AY(P), 7, "dot4") + SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + tag(AX(Q) + 10, AY(P) + 22, "P " + Lib.fmtN(P, 0) + ", Q " + Lib.fmtN(Q, 0), "t4");
  return o + tag(380, 345, s.l, "t1", 1, "middle");
}
Lib.stepper($("#stA"), { w: 760, h: 360, label: "AD and AS showing demand-pull inflation cured by lower AD, and cost-push inflation where lower AD cuts output", base: { a: 111, sh: 0, l: "" }, draw: adasDraw, tween: 1000, dwell: 6000, steps: [
  { cap: "<b>Starting point.</b> AD, SRAS and LRAS meet at potential output (60) with price level 57.", s: { l: "stable prices at potential output" } },
  { cap: "<b>Demand-pull.</b> AD rises (booming spending). Output goes above potential and the price level rises to about 66: <b>demand-pull inflation</b>.", s: { a: 128, l: "demand-pull: AD shifts right" } },
  { cap: "<b>The cure.</b> Higher interest rates and tighter fiscal policy shift AD back to the left. Prices fall back and output returns to potential, with little lasting loss. The right tool for this cause.", s: { a: 111, l: "AD back: prices and output normal" } },
  { cap: "<b>Cost-push.</b> Dearer oil shifts SRAS to the left. The price level rises and output <b>falls</b> below potential: stagflation.", s: { a: 111, sh: -12, l: "cost-push: SRAS shifts left" } },
  { cap: "<b>The wrong cure.</b> Cutting AD to bring prices down would lower output <b>even further</b> and raise unemployment. Supply-side policy, a stronger currency or wage restraint (shifting SRAS right) would be better.", s: { a: 100, sh: -12, l: "cutting AD: prices fall a little, output falls a lot" } },
] });

/* ---------- Lab 1: interest rate rise ---------- */
function labIR() {
  if (!$("#ir") || !$("#cs") || !$("#is")) return;
  const d = +$("#ir").value / 10, cs = +$("#cs").value / 10, is = +$("#is").value / 10, dC = cs * d * 0.6, dI = is * d * 0.2, dAD = dC + dI;
  const dInf = 0.4 * dAD, dU = 0.5 * dAD;
  $("#r1").textContent = "−" + Lib.fmtN(dAD, 1) + "%"; $("#r2").textContent = "−" + Lib.fmtN(dInf, 1) + " pts"; $("#r3").textContent = "+" + Lib.fmtN(dU, 1) + " pts";
  $("#rv").textContent = d === 0 ? "No change in the interest rate." : `A ${Lib.fmtN(d, 1)} point rise cuts consumption (60% of AD) by ${Lib.fmtN(dC / 0.6, 1)}% and investment (20% of AD) by ${Lib.fmtN(dI / 0.2, 1)}%, so AD falls ${Lib.fmtN(dAD, 1)}%. Inflation falls about ${Lib.fmtN(dInf, 1)} points, but unemployment rises about ${Lib.fmtN(dU, 1)} points (Okun's law). If spending is insensitive to interest rates, the policy is weak and needs a larger rate rise.`;
  const mx = Math.max(dAD, 1) * 1.2, Y = (v) => 250 - v / mx * 200; let o = SV.line(40, 250, 400, 250);
  [["Consumption", dC, "f1"], ["Investment", dI, "f4"], ["Total AD", dAD, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 110, h = v / mx * 200; o += SV.rect(x, 250 - h, 80, Math.max(h, 2), c) + tag(x + 40, 250 - h - 6, "−" + Lib.fmtN(v, 1) + "%", "t1", 1, "middle") + SV.text(x + 40, 270, l, "sm bd", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ir", label: "Rise in interest rate (points) ", min: 0, max: 60, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
Lib.slider($("#g2"), { id: "cs", label: "Sensitivity of consumption (% fall per point) ", min: 2, max: 20, step: 1, value: 8, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
Lib.slider($("#g3"), { id: "is", label: "Sensitivity of investment (% fall per point) ", min: 5, max: 60, step: 5, value: 30, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labIR });
labIR();
btnTable("lbBtns", "lbOut", [
  ["Raise interest rates", "Demand-pull (and expectations)", "12 to 24 months", "Lower growth and jobs; stronger currency hurts exporters"],
  ["Cut government spending / raise taxes", "Demand-pull", "6 to 18 months", "Political resistance; harms public services and growth"],
  ["Supply-side reform", "Cost-push; long-run inflation", "3 to 10 years", "Slow and costly"],
  ["Appreciation of the exchange rate", "Imported and cost-push", "Months", "Hurts exports and the current account"],
  ["Wage restraint / incomes policy", "Wage-push, expectations", "Months", "Hard to enforce; may cause a rebound or strikes"],
  ["Inflation target and central bank independence", "Expectations", "Builds over years", "Needs credibility; conflicts with jobs in the short run"],
  ["Reverse quantitative easing / slower money growth", "Excess money growth", "12 to 24 months", "Harder to control; may raise long-term rates"]
], ["Policy", "Mainly tackles", "Time lag", "Main cost"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which policy is best suited to the cause?", ["Cut AD (monetary or fiscal tightening)", "Supply-side / cost-side policy"],
  [("Spending is booming and output is above potential", 0), ("Oil prices double and firms' costs rise", 1), ("Wages are growing faster than productivity", 1), ("A positive output gap with rising demand for credit", 0), ("A weak currency makes imported raw materials dearer", 1), ("Consumers borrow heavily as interest rates stay low", 0), ("High taxes on fuel raise production costs", 1), ("Government spending has risen sharply in an economy at full employment", 0)],
  "Cut AD for demand-pull. Cut costs or raise supply for cost-push.") + MATCH([
  ["Transmission mechanism", "The chain from an interest rate change to spending and prices"],
  ["Demand-pull inflation", "Inflation because AD exceeds capacity"],
  ["Cost-push inflation", "Inflation because costs rise and SRAS shifts left"],
  ["Inflation target", "A declared level of inflation the central bank aims at"],
  ["Incomes policy", "Restraint on wage and price rises"],
  ["Sacrifice ratio", "Output or jobs lost per point of inflation removed"]]) + ORDER(
  "Put the transmission mechanism in order.",
  ["The central bank raises the policy interest rate", "Borrowing costs rise and saving becomes more rewarding", "Consumption and investment fall", "Aggregate demand shifts left", "Inflationary pressure falls, after a lag"],
  "Policy works through borrowing, spending and AD.") + CALC([
  {"q": "Nominal interest rate is 6% and inflation is 2.5%. Calculate the real interest rate (%).", "a": 3.5, "unit": "%", "tol": 0.05, "hint": "Nominal minus inflation.", "sol": "6 − 2.5 = <b>3.5%</b>."},
  {"q": "A government cuts spending by $20bn. The multiplier is 1.5. Calculate the fall in national income ($bn).", "a": 30, "unit": "$bn", "tol": 0.05, "hint": "20 × 1.5.", "sol": "<b>$30bn</b>."},
  {"q": "Imports are 25% of the price index. The currency appreciates and import prices fall 8%. Calculate the effect on the price level (%), ignoring other changes.", "a": -2, "unit": "%", "tol": 0.05, "hint": "25% of −8%.", "sol": "0.25 × −8 = <b>−2%</b>."},
  {"q": "Investment falls by 6% when interest rates rise 2 points. Calculate the interest elasticity of investment (% change in investment per point).", "a": -3, "tol": 0.05, "hint": "−6 ÷ 2.", "sol": "<b>−3% per point</b>."}]) + MCQ([
  ("Which policy is best suited to demand-pull inflation?", ["Higher interest rates", "Supply-side policy only", "A depreciation", "Lower taxes"], 0, "Higher rates reduce AD."),
  ("Which would be the least costly way to reduce cost-push inflation?", ["Cutting AD sharply", "Supply-side policy that raises productivity", "Lower taxes", "More money supply"], 1, "Raising productivity shifts supply right and cuts costs."),
  ("Which is a reason monetary policy may not work?", ["Time lags and low interest elasticity of spending", "Interest rates have no effect on borrowing", "Central banks cannot set rates", "Inflation is always demand-pull"], 0, "Lags and insensitivity to rates reduce effectiveness."),
  ("An independent central bank with a clear inflation target tends to:", ["Lower expected inflation", "Raise expected inflation", "Remove all lags", "Eliminate unemployment"], 0, "Credibility lowers expectations and so the cost of disinflation."),
  ("A cost of using a stronger currency to cut inflation is:", ["Lower export competitiveness", "Higher import prices", "Higher inflation", "More imported inflation"], 0, "A higher exchange rate makes exports dearer abroad.")
], "qz1") + CARDS([
  ("Demand-pull", "AD above capacity pushes prices up."),
  ("Cost-push", "Higher costs shift SRAS left."),
  ("Transmission mechanism", "Chain from interest rate to inflation."),
  ("Inflation target", "Declared level of inflation to aim for."),
  ("Incomes policy", "Limits on wage and price rises."),
  ("Credibility", "Belief that policy will be followed."),
  ("Sacrifice ratio", "Cost in output of cutting inflation."),
  ("Imported inflation", "Dearer imports raise prices.")]) + MCQ(mc_exam)

build("sy946", "policies-to-reduce-inflation", "Policies to Reduce Inflation and Their Effectiveness", EY,
  "9.4.6: monetary, fiscal, supply-side, exchange rate and incomes policies to reduce inflation, the transmission mechanism, and how to judge effectiveness. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
