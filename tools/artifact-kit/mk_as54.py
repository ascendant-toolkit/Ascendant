"""AS syllabus 5.3 Monetary policy. Run: python3 tools/artifact-kit/mk_as54.py"""
from asx import *
EY = EYAS("5.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Monetary policy</b> is the use of <b>interest rates, the money supply and credit regulation</b>, usually by the central bank, to influence aggregate demand and meet objectives such as price stability. <b class="kw">Expansionary monetary policy</b> (lower interest rates, a larger money supply, looser credit rules) makes borrowing cheaper and easier, so consumption and investment rise and <b>AD shifts right</b>; <b class="kw">contractionary monetary policy</b> (higher interest rates, a smaller money supply, tighter credit) does the opposite and <b>AD shifts left</b>, reducing inflation. Because interest rates change the cost of borrowing, the reward for saving and the exchange rate, they also affect net exports. The impact is limited by <b>time lags</b>, how <b>responsive</b> households and firms are to interest rates, <b>confidence</b>, and in a deep recession by the fact that rates cannot fall below zero.</p></div>

  <h2>1 · Tools of monetary policy (5.3.1 to 5.3.2)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>How it works</th></tr>
    <tr><td><b>Interest rates</b></td><td>The central bank sets a <b>base (policy) rate</b> that influences all other rates. A cut makes loans cheaper and saving less attractive; a rise does the reverse</td></tr>
    <tr><td><b>Money supply</b></td><td>The bank can increase the amount of money and credit in the economy (for example by buying bonds, <b>quantitative easing</b>) or reduce it</td></tr>
    <tr><td><b>Credit regulation</b></td><td>Rules on lending: capital requirements for banks, limits on loan-to-value for mortgages, and ease of obtaining credit. Relaxing them is expansionary; tightening is contractionary</td></tr>
  </table></div>
  <ul>
    <li>The <b>central bank</b> is usually independent of the government and often has an <b>inflation target</b>.</li>
    <li><b>Real interest rate</b> ≈ nominal rate − inflation: it is the real cost of borrowing that affects decisions.</li>
  </ul>

  <h2>2 · Expansionary and contractionary policy, and AD/AS (5.3.3 to 5.3.4)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Expansionary</th><th>Contractionary</th></tr>
    <tr><td><b>Interest rates</b></td><td>Cut</td><td>Raised</td></tr>
    <tr><td><b>Money supply and credit</b></td><td>Increased, looser</td><td>Reduced, tighter</td></tr>
    <tr><td><b>Effect on spending</b></td><td>More borrowing: consumption and investment rise; a weaker currency raises net exports</td><td>Less borrowing, more saving; a stronger currency lowers net exports</td></tr>
    <tr><td><b>AD</b></td><td>Shifts right</td><td>Shifts left</td></tr>
    <tr><td><b>Output, employment</b></td><td>Rise</td><td>Fall</td></tr>
    <tr><td><b>Price level</b></td><td>Rises</td><td>Falls (inflation reduced)</td></tr>
  </table></div>
  <ul>
    <li><b>Limits of monetary policy:</b> <b>time lags</b> (up to 18 months to take full effect); people may not respond (<b>interest-inelastic</b> demand, low <b>confidence</b>); in a deep recession rates may be near <b>zero</b> and banks reluctant to lend; the <b>exchange rate</b> effect; higher rates hurt borrowers and can push up costs for firms; it affects all sectors rather than being targeted.</li>
    <li><b>Strengths:</b> usually quicker to change than fiscal policy, less politically difficult, and can be adjusted gradually.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Give the full chain: base rate rises, borrowing dearer and saving more attractive, consumption and investment fall, AD shifts left, inflation falls. Evaluate with <b>time lags</b>, <b>responsiveness</b>, the <b>cause of inflation</b> (cost-push is harder to cure) and the effects on growth and unemployment.</div>
'''

watch = '''
  <h2>1 · How a rate cut works through the economy</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Contractionary monetary policy and inflation</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Change the interest rate</h2>
  <p>Cut or raise the base rate. The AD curve shifts according to how responsive households and firms are.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>AD</small><strong id="r1"></strong></div><div><small>Real output</small><strong id="r2"></strong></div><div><small>Price level</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with AD shifted by the interest rate change"></svg></div></div></div>

  <h2>Lab 2 · Real interest rates</h2>
  <p>Households and firms respond to the real interest rate. Set the nominal rate and inflation.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Real interest rate</small><strong id="t1"></strong></div><div><small>Effect on borrowing</small><strong id="t2"></strong></div><div><small>Effect on saving</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars for nominal interest rate, inflation and real interest rate"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Expansionary or contractionary?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a rate rise in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Raising rates to fight inflation", "Inflation is well above target, so the central bank raises its base rate. Mortgage and loan costs rise, households cut spending and firms delay investment, AD falls, and inflation eases, though growth may slow and unemployment rise.", "contractionary monetary policy.") +
rw("Quantitative easing", "With interest rates close to zero, a central bank creates money to buy bonds, lowering longer-term interest rates and raising the money supply to encourage spending and lending.", "money supply as a tool of expansionary policy.") +
rw("Easier credit rules", "A central bank relaxes the deposit rules for mortgages. More households can borrow to buy homes, spending rises and house prices may rise. This is expansionary credit regulation.", "credit regulation.") +
rw("Rates cut but nobody borrows", "After a financial crisis rates fall to near zero, but households fear job losses and banks lend cautiously, so spending barely rises. This shows the limits of monetary policy when confidence is low.", "why monetary policy may be ineffective.")
)

mc_exam = [
  mcq("m25_12", 23, "A country's central bank decides to reduce the level of credit regulation. What is this an example of?", ["contractionary fiscal policy", "contractionary monetary policy", "expansionary fiscal policy", "expansionary monetary policy"], 3, "Looser credit rules make borrowing easier, which is expansionary monetary policy."),
  mcq("s24_11", 20, "To counter deflation a central bank uses expansionary monetary policy. What is likely to result?", ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], 1, "Lower interest rates and more credit raise AD."),
  mcq("s22_11", 29, "Why will a contractionary monetary policy reduce inflation?", ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], 3, "Higher interest rates encourage saving and reduce spending, lowering AD."),
  mcq("s23_12", 27, "The diagram shows the current equilibrium of an economy. The government introduces a contractionary monetary policy. What is the most likely outcome?", ["a fall in investment and a fall in inflation", "a fall in investment and a rise in inflation", "a rise in investment and a fall in inflation", "a rise in investment and a rise in inflation"], 0, "Higher interest rates raise the cost of borrowing, so investment falls, AD shifts left and inflationary pressure falls."),
  mcq("s25_13", 25, "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target?", ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], 1, "Higher rates raise firms' borrowing costs and can reduce investment, which may reduce capacity (aggregate supply), shifting SRAS left and worsening cost-push inflation."),
  mcq("w21_12", 29, "What would make a policy of raising interest rates less likely to be effective in reducing inflation?", ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], 1, "If consumers expect faster price rises, they bring forward spending, offsetting the effect of higher rates."),
  mcq("s21_12", 28, "Why are higher interest rates together with increased taxation on expenditure likely to cause domestic deflation?", ["because the contractionary monetary policy will over-ride the expansionary fiscal policy", "because the monetary and fiscal policies involved will reinforce each other", "because the expansionary monetary policy will over-ride the contractionary fiscal policy", "because the monetary and fiscal policies involved will cancel each other out"], 1, "Both are contractionary, so they reinforce each other, strongly reducing AD."),
  mcq("s21_13", 27, "Which type of policy would have the most immediate effect in dealing with a deflationary economic downturn?", ["increasing the government's budget surplus", "increasing borrowing by assisting banks to lend more", "investing in long-term projects to improve transport networks", "switching the burden of taxation from earning to spending"], 1, "Helping banks to lend more raises credit and spending quickly. Long-term projects take years.")
]

exam = exam_page("monetary policy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Monetary policy appears as an 8 mark explanation part and a 12 mark discussion in most series, nearly always linked to inflation or deflation, and in 6 mark AD/AS data-response parts. Reworded past questions are below, with eight Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "1", "May/June 2023 (23) Q5(a)"), ("Essay parts, 12 marks", "5", "Oct/Nov 2021 (23) Q4(b); Oct/Nov 2020 (22) Q3(b); May/June 2022 (23) Q3(b); Feb/March 2020 (22) Q4(b); Oct/Nov 2022 (22) Q4(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("s23_23", "5(a)"), "8 marks", "Explain how monetary policy may be able to reduce the rate of inflation in an economy and consider the likely success of this policy.",
     ["Knowledge (up to 3): an understanding of monetary policy (1); the tools of monetary policy: interest rates, the supply of money and regulations (1); the nature of a contractionary monetary policy (1).",
      "Analysis (up to 3): an explanation of how the tools can be applied to reduce inflation (1); analysis of the changes on aggregate demand and the price level (1); analysis of the effects on output and employment (1).",
      "Evaluation (up to 2): the effectiveness of monetary policy depends on the response of consumers and firms, in particular to higher interest rates (1), and may also depend on the rate of inflation and its causes (1), with a justified conclusion (1 reserved)."],
     "Define monetary policy and its tools. Contractionary: higher rates, AD falls, price level falls, output and jobs fall. Evaluate: responsiveness, causes of inflation.",
     [[("k", "Monetary policy is the use of interest rates, the money supply and credit regulation, normally by the central bank, to influence the economy. A contractionary policy involves raising interest rates, restricting the money supply or tightening credit.")], [("n", "Higher interest rates make borrowing dearer and saving more attractive, so consumption and investment fall and AD shifts to the left. The price level falls, reducing inflation, but real output and employment also fall in the short run.")], [("e", "How successful it is depends on how strongly consumers and firms respond to higher rates and on the cause of inflation. It works best against demand-pull inflation; against cost-push inflation it may cut output without lowering costs, so it may be less successful.")]]),
  eq(P("w21_23", "4(b)"), "12 marks", "Discuss whether a policy of increasing interest rates is the best way of controlling a rising rate of inflation in an economy.",
     ["Analysis (up to 8): how higher interest rates reduce AD and so inflation: dearer borrowing, more saving, lower consumption and investment, a stronger exchange rate lowering import prices and net exports (up to 4); at least one alternative, such as contractionary fiscal policy or supply-side policy, with how it would work, and the limits of each (up to 4).",
      "Evaluation (up to 4): a judgement on whether higher interest rates are the best method, depending on the cause of inflation, time lags, responsiveness and costs to growth and unemployment, with a conclusion."],
     "Rates up: borrowing dearer, AD left. Limits: lags, expectations, cost-push. Alternatives: fiscal, supply-side. Judge by cause of inflation.",
     [[("n", "A rise in interest rates makes borrowing more expensive and saving more attractive, so consumption and investment fall and AD shifts left, reducing demand-pull inflation. A higher exchange rate may also reduce import prices. But the effect takes time, households with fixed-rate loans may not respond, and higher rates raise firms' costs and slow growth. Contractionary fiscal policy could cut AD more directly, and supply-side policy could address cost-push inflation by raising productivity, but each has its own costs and lags.")], [("e", "Raising interest rates is probably the most flexible tool against demand-pull inflation, but it is less effective against cost-push inflation, so it is not always the best. The most effective response probably combines monetary policy with supply-side measures, depending on the cause.")]]),
  eq(P("m20_22", "4(b)"), "12 marks", "Discuss whether monetary policy measures are always effective in correcting a high rate of inflation.",
     ["Analysis (up to 8): monetary policy must be deflationary: a reduction in the money supply, a rise in the rate of interest or a rise in the exchange rate, aiming to control AD (up to 4); reasons why it might be ineffective, such as time lags, consumers' and firms' limited response, expectations of inflation and cost-push causes (up to 4).",
      "Evaluation (up to 4): a judgement on whether monetary policy is always effective, with a conclusion."],
     "Measures: interest rates, money supply, exchange rate. Limits: lags, response, expectations, cost-push. Judge: not always effective.",
     [[("n", "Monetary policy tackles inflation by controlling AD: a rise in interest rates or a reduction in the money supply makes credit dearer and reduces spending, and a higher exchange rate lowers import prices and demand for exports. But it may be ineffective if consumers and firms do not respond to interest rates, if there are time lags, if people expect inflation to continue, or if inflation is caused by rising costs rather than strong demand.")], [("e", "Monetary policy is therefore not always effective. It works best against demand-pull inflation when the central bank is credible, but it can be slow and costly for growth, and other policies may be needed for cost-push inflation.")]]),
  eq(P("w22_22", "4(b)"), "12 marks", "Discuss whether an expansionary monetary policy will be successful in correcting deflation.",
     ["Analysis (up to 8): how expansionary monetary policy works against deflation: lower interest rates, more money and credit, raising consumption, investment and AD, and so the price level (up to 4); why it may fail, such as consumers expecting prices to fall further, low confidence, banks unwilling to lend, interest rates already near zero (up to 4).",
      "Evaluation (up to 4): a judgement on whether it will succeed, taking into account the cause of deflation, confidence and alternative policies such as fiscal stimulus, with a conclusion."],
     "Low rates, more money: AD up. Limits: expectations, low confidence, rates near zero. Alternatives: fiscal policy. Judge.",
     [[("n", "Expansionary monetary policy cuts interest rates and increases the money supply, so borrowing becomes cheaper, consumption and investment rise, AD shifts right and the price level rises, ending deflation. But in deflation consumers expect prices to fall further and delay spending, banks may be reluctant to lend, and interest rates may already be close to zero so cannot be cut further, so the policy may not work.")], [("e", "Expansionary monetary policy is more likely to succeed if confidence is restored and banks lend, but in a deep deflation it may need to be combined with fiscal policy, such as higher government spending, to raise AD directly.")]])
  ],
  )

tips = tips_html(
  [("Name the three tools.", "Interest rates, money supply, credit regulation."),
   ("Give the full chain.", "Rate change, borrowing, C and I, AD, output and prices."),
   ("Distinguish the two stances.", "Cut rates and loosen credit; raise rates and tighten credit."),
   ("Use AD/AS diagrams.", "Left shift for contractionary."),
   ("Mention time lags.", "Effects can take 12 to 18 months."),
   ("Consider the cause of inflation.", "Monetary policy suits demand-pull, not cost-push."),
   ("Mention the limits.", "Zero bound, confidence, expectations.")],
  [("Monetary policy", "Monetary policy uses interest rates, the money supply and credit regulation."),
   ("Base rate", "A rise in the base rate makes borrowing dearer."),
   ("Contractionary", "Contractionary monetary policy shifts AD to the left."),
   ("Time lags", "Monetary policy takes time to affect the economy."),
   ("Evaluation", "It depends on how consumers and firms respond and on the cause of inflation.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- transmission chain ---------- */
function trDraw(s) {
  const bx = (x, y, w, t, k, v) => SV.rect(x, y, w, 46, k, { rx: 8, ...op(0.55 * v) }) + SV.text(x + w / 2, y + 28, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  const ar = (x1, y1, x2, y2, d, v) => SV.line(x1, y1, x2, y2, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y2, d, "dot4");
  let o = bx(20, 20, 180, "Central bank cuts the base rate", "f3", s.a) + ar(202, 43, 250, 43, "r", s.b) + bx(252, 20, 220, "Borrowing cheaper, saving less attractive", "f1", s.b) + ar(474, 43, 522, 43, "r", s.c) + bx(524, 20, 220, "Consumption and investment rise", "f2", s.c);
  o += ar(634, 68, 634, 118, "d", s.d) + bx(480, 122, 264, "AD shifts right; currency may weaken", "f1", s.d) + ar(478, 145, 430, 145, "l", s.e) + bx(140, 122, 288, "Output and employment rise; prices may rise", "f3", s.e);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 190" role="img" aria-label="A cut in the base rate lowers borrowing costs, raises consumption and investment, and shifts AD right">${trDraw({ a: 1, b: 1, c: 1, d: 1, e: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 190, label: "The transmission of an interest rate cut", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: trDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>The central bank cuts its base rate.</b> This is expansionary monetary policy.", s: { a: 1 } },
  { cap: "<b>Borrowing becomes cheaper</b> (loans, mortgages) and saving less rewarding, so people have an incentive to spend.", s: { a: 1, b: 1 } },
  { cap: "<b>Consumption and investment rise.</b> Households borrow to buy and firms to expand.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>AD shifts right.</b> Lower interest rates may also weaken the currency, raising net exports.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>Output and employment rise,</b> and prices may rise if there is little spare capacity.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

function mcDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A higher interest rate shifts AD to the left, lowering the price level and output">${mcDraw({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary monetary policy to reduce inflation", base: { a: 0, n: 0 }, draw: mcDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Inflation is above target and AD is strong.", s: { a: 0, n: 0 } },
  { cap: "<b>The central bank raises interest rates.</b> Borrowing is dearer, saving is more attractive and the currency may rise. Consumption, investment and net exports fall: AD shifts <b>left</b>. The price level falls (inflation eases) but so does output.", s: { a: -20, n: 1 } },
  { cap: "<b>The trade-off.</b> Lower inflation comes with slower growth and possibly higher unemployment in the short run, and the effect appears only after a time lag.", s: { a: -20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!["ch", "rs"].every((i) => $("#" + i))) return;
  const c = +$("#ch").value, r = +$("#rs").value / 100, a = Math.max(-30, Math.min(30, -c * 8 * r)), e = sdEq(a, 0), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(a) < 0.5 ? "No shift" : a > 0 ? "Shifts right" : "Shifts left"; $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = Math.abs(a) < 0.5 ? "Either the base rate is unchanged or spending does not respond to it, so AD does not shift." : `A ${c < 0 ? "cut" : "rise"} of ${Math.abs(c)} percentage points, with spending ${Lib.fmtN(r * 100, 0)}% responsive to interest rates, shifts AD ${a > 0 ? "right (expansionary)" : "left (contractionary)"}. Real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. ${r < 0.4 ? "Households and firms respond weakly, so the policy has a small effect: a limit of monetary policy." : ""}`;
  $("#labA").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 }, { lras: false });
}
Lib.slider($("#g1"), { id: "ch", label: "Change in the base rate, percentage points ", min: -3, max: 3, step: 0.5, value: 2, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "rs", label: "How responsive spending is to interest rates, % ", min: 10, max: 100, step: 10, value: 70, fmt: (v) => v + "%", onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labI() {
  if (!["nm", "fl"].every((i) => $("#" + i))) return;
  const n = +$("#nm").value, f = +$("#fl").value, r = n - f;
  $("#t1").textContent = (r >= 0 ? "+" : "") + Lib.fmtN(r, 1) + "%"; $("#t2").textContent = r < 0 ? "Very attractive" : r < 2 ? "Moderate" : "Discouraged"; $("#t3").textContent = r < 0 ? "Savers lose" : r < 2 ? "Modest reward" : "Rewarded";
  $("#tv").textContent = `A nominal rate of ${n}% with inflation of ${f}% gives a real rate of ${Lib.fmtN(r, 1)}%. ${r < 0 ? "Borrowing costs less than inflation: the real value of debt falls, so borrowing is attractive and savers lose in real terms." : r < 2 ? "A low real rate keeps borrowing fairly cheap." : "A high real rate makes borrowing costly and saving rewarding, which reduces spending."}`;
  const Y = (v) => 120 - v * 8; let o = SV.line(40, 120, 400, 120) + SV.line(40, 20, 40, 190);
  [["Nominal rate", n, "f1"], ["Inflation", f, "f3"], ["Real rate", r, r >= 0 ? "f2" : "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 120, 80, Math.abs(Y(v) - 120), c, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, v >= 0 ? Y(v) - 6 : 120 + Math.abs(Y(v) - 120) + 14, Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "nm", label: "Nominal interest rate, % ", min: 0, max: 12, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labI });
Lib.slider($("#g4"), { id: "fl", label: "Inflation rate, % ", min: 0, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labI });
labI();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Expansionary or contractionary monetary policy?", ["Expansionary", "Contractionary"],
  [("A cut in the base rate", 0), ("A rise in the base rate", 1), ("Quantitative easing", 0), ("Reducing the money supply", 1), ("Looser rules on mortgage lending", 0), ("Tighter credit regulation for banks", 1), ("Lowering interest rates to end deflation", 0), ("Raising rates to reduce inflation", 1)],
  "Expansionary: cheaper, easier credit. Contractionary: dearer, tighter credit.") + MATCH([
  ["Monetary policy", "Use of interest rates, money supply and credit regulation"],
  ["Base rate", "The central bank's policy interest rate"],
  ["Quantitative easing", "Creating money to buy bonds and raise the money supply"],
  ["Credit regulation", "Rules on how banks lend"],
  ["Real interest rate", "Nominal rate minus inflation"],
  ["Time lag", "Delay before a policy takes full effect"]]) + ORDER(
  "Put the effect of a rise in interest rates in order.",
  ["The central bank raises the base rate", "Borrowing becomes dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left", "The price level and inflation fall"],
  "Higher rates reduce spending and AD, lowering inflation.") + CALC([
  {"q": "The nominal interest rate is 5% and inflation 3%. What is the real interest rate (%)?", "a": 2, "unit": "%", "tol": 0.1, "hint": "5 − 3.", "sol": "<b>2%</b>."},
  {"q": "A firm borrows $200,000 at 6%. What is the yearly interest ($)?", "a": 12000, "unit": "$", "tol": 1, "hint": "0.06 × 200,000.", "sol": "<b>$12,000</b>."},
  {"q": "The rate rises to 8%. What is the new yearly interest ($)?", "a": 16000, "unit": "$", "tol": 1, "hint": "0.08 × 200,000.", "sol": "<b>$16,000</b>."},
  {"q": "By what % has the cost of borrowing risen?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4,000 ÷ 12,000.", "sol": "<b>33.3%</b>."}]) + MCQ([
  ("Monetary policy uses:", ["Interest rates, money supply and credit regulation", "Taxes and spending", "Training schemes", "Tariffs"], 0, "Not fiscal."),
  ("A rise in interest rates will usually:", ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise investment"], 0, "Borrowing dearer."),
  ("Quantitative easing is:", ["Expansionary", "Contractionary", "A tax", "A subsidy"], 0, "Raises the money supply."),
  ("A limit of monetary policy is:", ["Time lags", "Instant effect", "No effect on AD", "It lowers the deficit"], 0, "Delays."),
  ("Which inflation is monetary policy least suited to?", ["Cost-push", "Demand-pull", "Both equally", "Neither"], 0, "Higher rates do not cut costs.")
], "qz1") + CARDS([
  ("Tools", "Rates, money supply, credit rules."),
  ("Expansionary", "AD right."),
  ("Contractionary", "AD left."),
  ("QE", "Creates money for bonds."),
  ("Credit rules", "Looser = expansionary."),
  ("Real rate", "Nominal − inflation."),
  ("Lags", "12 to 18 months."),
  ("Limits", "Confidence, zero bound.")]) + MCQ(mc_exam)

build("as54", "as-monetary-policy", "Monetary Policy", EY,
  "5.3: the tools of monetary policy, expansionary and contractionary policy, and AD/AS analysis of their effects. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
