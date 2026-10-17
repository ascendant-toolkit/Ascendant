"""AS syllabus 5.3.3-5.3.4 Effects of monetary policy and its limits. Run: python3 tools/artifact-kit/mk_as54b.py"""
from as6k import *
EY = EYAS("5.3.3 to 5.3.4")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">Expansionary monetary policy</b> (lower interest rates, a larger money supply, looser credit) raises consumption, investment and sometimes net exports, so <b>AD shifts right</b> and real output, employment and the price level rise; <b class="kw">contractionary monetary policy</b> (higher rates, a smaller money supply, tighter credit) does the reverse, so <b>AD shifts left</b> and inflation falls at the cost of lower output and employment. It is used to control <b>inflation</b> (contractionary), to end <b>deflation</b> or support recovery from a <b>recession</b> (expansionary), and to keep growth steady. How well it works depends on <b>how responsive</b> spending is to interest rates, <b>confidence and expectations</b>, <b>time lags</b>, the <b>cause</b> of the problem, the <b>exchange rate</b> and whether rates are already close to <b>zero</b>. It is best judged against <b>fiscal</b> and <b>supply-side</b> alternatives, and against the effects on different groups and on other objectives.</p></div>

  <h2>1 · Expansionary and contractionary policy</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Expansionary</th><th>Contractionary</th></tr>
    <tr><td><b>Interest rates</b></td><td>Cut</td><td>Raised</td></tr>
    <tr><td><b>Money supply and credit</b></td><td>Increased, looser</td><td>Reduced, tighter</td></tr>
    <tr><td><b>Consumption</b></td><td>Rises: cheaper credit, less incentive to save, wealth effects</td><td>Falls: dearer credit, more saving</td></tr>
    <tr><td><b>Investment</b></td><td>Rises: cheaper finance</td><td>Falls: dearer finance</td></tr>
    <tr><td><b>Exchange rate and net exports</b></td><td>Currency may weaken, net exports rise</td><td>Currency may strengthen, net exports fall</td></tr>
    <tr><td><b>AD</b></td><td>Shifts right</td><td>Shifts left</td></tr>
    <tr><td><b>Real output, employment</b></td><td>Rise</td><td>Fall</td></tr>
    <tr><td><b>Price level, inflation</b></td><td>Rise</td><td>Fall</td></tr>
    <tr><td><b>Used for</b></td><td>Recession, deflation, high unemployment</td><td>High inflation, an overheating economy</td></tr>
  </table></div>

  <h2>2 · Using AD and AS diagrams</h2>
  <ul>
    <li><b>Contractionary:</b> AD shifts left along SRAS, so the price level and real output fall. This lowers <b>demand-pull</b> inflation, but also lowers output and employment in the short run.</li>
    <li><b>Expansionary:</b> AD shifts right. If there is <b>spare capacity</b> (the flat part of the AS curve), output rises with little effect on prices; near <b>full capacity</b> (the steep part), mostly the price level rises.</li>
    <li><b>Long run:</b> monetary policy shifts AD, not LRAS, so in the long run it cannot permanently raise output; sustained growth needs supply-side policies. Stable, low inflation can create a good environment for investment.</li>
  </ul>

  <h2>3 · Which problem is it suited to?</h2>
  <div class="tw"><table class="t">
    <tr><th>Problem</th><th>Monetary response</th><th>Why it may work or not</th></tr>
    <tr><td><b>Demand-pull inflation</b></td><td>Contractionary</td><td>Works well: reduces the excess demand</td></tr>
    <tr><td><b>Cost-push inflation</b></td><td>Contractionary</td><td>Less effective: cuts output without lowering the costs causing the rise</td></tr>
    <tr><td><b>Deflation or recession</b></td><td>Expansionary</td><td>May fail if confidence is low, people expect prices to fall, banks will not lend or rates are near zero</td></tr>
    <tr><td><b>Housing bubble</b></td><td>Tighter credit regulation</td><td>Targets lending directly rather than all spending</td></tr>
  </table></div>

  <h2>4 · Evaluating monetary policy</h2>
  <ul>
    <li><b>Strengths:</b> quick to decide and adjust, often independent of politics, can be changed in small steps, works through the market, and does not need the government to borrow or tax.</li>
    <li><b>Time lags:</b> it can take 12 to 18 months or more for a rate change to affect spending and inflation fully.</li>
    <li><b>Responsiveness:</b> if households and firms are not sensitive to interest rates (interest-inelastic), or many borrow at fixed rates, the effect is smaller.</li>
    <li><b>Confidence and expectations:</b> pessimistic households will not borrow even when rates are low; if people expect inflation to rise, they may spend sooner, offsetting higher rates.</li>
    <li><b>Zero lower bound:</b> rates cannot fall much below zero, so other tools such as QE may be needed.</li>
    <li><b>Exchange rate:</b> higher rates may raise the currency and hurt exporters; lower rates may weaken it and raise import costs.</li>
    <li><b>Unequal effects:</b> borrowers and savers, indebted firms and exporters are affected differently.</li>
    <li><b>Conflicts:</b> reducing inflation may cost growth and jobs, and expansion may risk inflation and asset bubbles. <b>Compare</b> with fiscal policy (more targeted but slower to decide) and supply-side policy (long-term).</li>
  </ul>
  <div id="pic2" class="card"></div>
  <div class="tip"><b class="h">Exam tip</b>Give the full chain: base rate rises, borrowing dearer and saving more attractive, consumption and investment fall, AD shifts left, inflation falls. Evaluate with <b>time lags</b>, <b>responsiveness</b>, the <b>cause of inflation</b> (cost-push is harder to cure) and the effects on growth and unemployment, then <b>compare</b> with another policy.</div>
'''

watch = '''
  <h2>1 · Contractionary policy to reduce inflation</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Expansionary policy and spare capacity</h2>
  <div id="stE"></div>
  <h2>3 · Why expansionary policy may fail in a deflation</h2>
  <div id="stF"></div>
'''

explore = '''
  <h2>Lab 1 · Change the interest rate</h2>
  <p>Cut or raise the base rate. The AD curve shifts according to how responsive households and firms are.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>AD</small><strong id="r1"></strong></div><div><small>Real output</small><strong id="r2"></strong></div><div><small>Price level</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with AD shifted by the interest rate change"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Which policy for which problem?", "Choose a problem to see the monetary response and how effective it is likely to be.", ["Monetary response", "Likely effect", "Main limit"])

practise = '''
  <h2>1 · Effect of a rise or a cut in interest rates</h2><div id="cl1" class="card"></div>
  <h2>2 · Strength or limit of monetary policy?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the effect of a rate cut in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Raising rates to fight inflation", "Inflation is well above target, so the central bank raises its base rate. Mortgage and loan costs rise, households cut spending and firms delay investment, AD falls, and inflation eases, though growth may slow and unemployment rise.", "contractionary monetary policy.") +
rw("Rates cut but nobody borrows", "After a financial crisis rates fall to near zero, but households fear job losses and banks lend cautiously, so spending barely rises. This shows the limits of monetary policy when confidence is low.", "why monetary policy may be ineffective.") +
rw("Cost-push inflation from energy prices", "When inflation comes from higher energy costs, raising rates reduces spending but does not lower energy prices. Output and jobs may fall while inflation stays high.", "why monetary policy suits demand-pull better than cost-push inflation.") +
rw("Deflation and falling prices", "When prices fall, consumers delay purchases in expectation of lower prices. Lower interest rates may not change this, so governments may also use spending or QE.", "limits of expansionary policy in deflation.") +
rw("Time lags in practice", "A central bank raises rates today, but many borrowers are on fixed-rate loans that reset only months later, so the full effect takes a year or more.", "time lags.")
)

mc_exam = [
  mcq("s24_11", 20, "To counter deflation a central bank uses expansionary monetary policy. What is likely to result?", ["a higher cost of borrowing", "an increase in aggregate demand", "an appreciation of the exchange rate", "an increase in government debt"], 1, "Lower interest rates and more credit raise AD."),
  mcq("s22_11", 29, "Why will a contractionary monetary policy reduce inflation?", ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], 3, "Higher interest rates encourage saving and reduce spending, lowering AD."),
  mcq("s23_12", 27, "The diagram shows the current equilibrium of an economy. The government introduces a contractionary monetary policy. What is the most likely outcome?", ["a fall in investment and a fall in inflation", "a fall in investment and a rise in inflation", "a rise in investment and a fall in inflation", "a rise in investment and a rise in inflation"], 0, "Higher interest rates raise the cost of borrowing, so investment falls, AD shifts left and inflationary pressure falls."),
  mcq("s25_13", 25, "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target?", ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], 1, "Higher rates raise firms' borrowing costs and can reduce investment, which may reduce capacity, shifting SRAS left."),
  mcq("w21_12", 29, "What would make a policy of raising interest rates less likely to be effective in reducing inflation?", ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], 1, "If consumers expect faster price rises, they bring forward spending, offsetting the effect of higher rates."),
  mcq("s21_12", 28, "Why are higher interest rates together with increased taxation on expenditure likely to cause domestic deflation?", ["because the contractionary monetary policy will over-ride the expansionary fiscal policy", "because the monetary and fiscal policies involved will reinforce each other", "because the expansionary monetary policy will over-ride the contractionary fiscal policy", "because the monetary and fiscal policies involved will cancel each other out"], 1, "Both are contractionary, so they reinforce each other, strongly reducing AD."),
  mcq("s21_13", 27, "Which type of policy would have the most immediate effect in dealing with a deflationary economic downturn?", ["increasing the government's budget surplus", "increasing borrowing by assisting banks to lend more", "investing in long-term projects to improve transport networks", "switching the burden of taxation from earning to spending"], 1, "Helping banks to lend more raises credit and spending quickly. Long-term projects take years."),
  mcq("s21_11", 28, "Japan is suffering from deflation. Which government policy would not help to overcome this problem?", ["encouraging domestic savings rather than consumption", "increasing incentives for business start-ups by lowering profits tax", "lowering interest rates and increasing the money supply", "promoting more innovation in technical industries"], 0, "Encouraging saving instead of spending would reduce AD further, worsening deflation."),
  mcq("s20_13", 29, "Which combination of fiscal and monetary policies is most likely to be effective in the short run for tackling deflation in a closed economy? (fiscal policy, monetary policy)", ["decreasing the budget deficit, decreasing the interest rate", "decreasing the budget deficit, decreasing the money supply", "increasing the budget deficit, decreasing the interest rate", "increasing the budget deficit, decreasing the money supply"], 2, "A larger budget deficit (expansionary fiscal) and lower interest rates (expansionary monetary) both raise AD.")
]

exam = exam_page("effects of monetary policy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Monetary policy is a regular 8 mark explanation and a very common 12 mark discussion in Paper 2, nearly always linked to inflation or deflation, and appears in 6 mark data-response parts. Reworded past questions are below, with eight Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "2", "May/June 2023 (23) Q5(a); Feb/March 2024 (22) Q5(a)"), ("Essay parts, 12 marks", "5", "Oct/Nov 2021 (23) Q4(b); Feb/March 2020 (22) Q4(b); Oct/Nov 2022 (22) Q4(b); May/June 2022 (23) Q3(b); May/June 2021 (21) Q4(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("s23_23", "5(a)"), "8 marks", "Explain how monetary policy may be able to reduce the rate of inflation in an economy and consider the likely success of this policy.",
     ["Knowledge (up to 3): an understanding of monetary policy (1); the tools of monetary policy: interest rates, the supply of money and regulations (1); the nature of a contractionary monetary policy (1).",
      "Analysis (up to 3): an explanation of how the tools can be applied to reduce inflation (1); analysis of the changes on aggregate demand and the price level (1); analysis of the effects on output and employment (1).",
      "Evaluation (up to 2): the effectiveness depends on the response of consumers and firms, in particular to higher interest rates (1), and may also depend on the rate of inflation and its causes (1), with a justified conclusion (1 reserved)."],
     "Define monetary policy and its tools. Contractionary: higher rates, AD falls, price level falls, output and jobs fall. Evaluate: responsiveness, causes of inflation.",
     [[("k", "Monetary policy is the use of interest rates, the money supply and credit regulation, normally by the central bank, to influence the economy. A contractionary policy involves raising interest rates, restricting the money supply or tightening credit.")], [("n", "Higher interest rates make borrowing dearer and saving more attractive, so consumption and investment fall and AD shifts to the left. The price level falls, reducing inflation, but real output and employment also fall in the short run.")], [("e", "How successful it is depends on how strongly consumers and firms respond to higher rates and on the cause of inflation. It works best against demand-pull inflation; against cost-push inflation it may cut output without lowering costs, so it may be less successful.")]]),
  eq(P("m24_22", "5(a)"), "8 marks", "With the help of an aggregate demand and aggregate supply diagram, explain how a decrease in interest rates could cause economic growth and consider whether economic growth will always result in inflation.",
     ["Knowledge (up to 3): a clear understanding of what is meant by economic growth (1), inflation (1) and interest rates (1), and an accurate diagram with correctly labelled axes and the equilibrium price level and real GDP (1; a maximum of 3 marks in total).",
      "Analysis (up to 3): using the diagram to explain how a decrease in interest rates affects saving and borrowing (1), causing an increase in consumption, investment or net exports (1), which causes an increase in economic growth or real GDP (1).",
      "Evaluation (up to 2): a rise in inflation assumes the economy is operating at full capacity; the growth may be focused on capital-intensive industries, or the source of the growth may be long term in nature (1); the second mark is for a justified conclusion."],
     "Diagram: AD right. Lower rates: less saving, more borrowing, C and I up, real GDP up. Evaluate: only inflation if near full capacity; supply-side growth does not.",
     [[("k", "Economic growth is an increase in real GDP. Inflation is a sustained rise in the general price level. The interest rate is the cost of borrowing and the reward for saving. The AD/AS diagram has the price level and real GDP on the axes, with AD, SRAS and the equilibrium shown.")], [("n", "A decrease in interest rates reduces the reward for saving and makes borrowing cheaper, so consumption and investment rise, and a weaker currency may raise net exports. AD shifts right on the diagram, so real GDP increases: economic growth.")], [("e", "Growth will not always cause inflation. If there is spare capacity, output can rise with little change in prices, and if the growth comes from improved productivity, SRAS and LRAS also shift right, holding prices down. Inflation is more likely when the economy is near full capacity.")]]),
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
     [[("n", "Expansionary monetary policy cuts interest rates and increases the money supply, so borrowing becomes cheaper, consumption and investment rise, AD shifts right and the price level rises, ending deflation. But in deflation consumers expect prices to fall further and delay spending, banks may be reluctant to lend, and interest rates may already be close to zero so cannot be cut further, so the policy may not work.")], [("e", "Expansionary monetary policy is more likely to succeed if confidence is restored and banks lend, but in a deep deflation it may need to be combined with fiscal policy, such as higher government spending, to raise AD directly.")]]),
  eq(P("s22_23", "3(b)"), "12 marks", "Discuss whether a contractionary monetary policy is the best way to reduce the rate of inflation.",
     ["Analysis (up to 8): the advantages and disadvantages of monetary policy in reducing inflation (up to 4; a maximum of 3 if only advantages or only disadvantages); and of at least one other policy, such as fiscal or supply-side policy (up to 4 per policy; a maximum of 3 if one-sided). In theory a rise in the interest rate encourages saving and reduces funding for investment, reducing inflation; fiscal policy raises taxes or cuts spending, at the cost of higher unemployment; supply-side policies may help where there are structural weaknesses.",
      "Evaluation (up to 4): consideration of which is the best way (up to 3) and a justified conclusion (1). There are no marks for merely defining terms in the question."],
     "Monetary: rates up, AD down; lags, cost-push. Fiscal: taxes up, spending down; unemployment. Supply-side: costs down; slow. Judge by cause and time.",
     [[("n", "A rise in the interest rate encourages saving and reduces borrowing and investment, so AD falls and inflation eases. It is flexible and independent of politics, but it works with a lag, may be offset by expectations and does little against cost-push inflation. Fiscal policy, raising taxes or cutting spending, also reduces AD and can be targeted, but cuts output and employment and takes time to legislate. Supply-side policy can lower costs and tackle structural causes, but takes years.")], [("e", "Contractionary monetary policy is probably the best short-run tool for demand-pull inflation because it can be changed quickly, but for cost-push or structural inflation supply-side measures may be better. A combination is likely to be best.")]]),
  eq(P("s21_21", "4(b)"), "12 marks", "Discuss how likely it is that monetary policy would be successful in reducing inflation in an economy with a floating exchange rate.",
     ["Analysis (up to 8): the likely success of monetary policy in an economy with a floating exchange rate (up to 4), through a rise in interest rates or a reduction in the money supply; for cost-push inflation, an appreciation lowers import prices of finished products and raw materials; for demand-pull inflation, higher rates or a smaller money supply reduce AD and appreciate the currency; and the likely difficulties (up to 4).",
      "Evaluation (up to 4): a judgement on how likely it is that monetary policy would succeed, with reference to elasticities, the J-curve effect and the Marshall-Lerner condition, and a reserved mark for a conclusion."],
     "Higher rates: AD down, currency up, import prices down. Floating rate helps: appreciation lowers costs. Difficulties: exporters hit, elasticities, lags. Judge.",
     [[("n", "With a floating exchange rate, higher interest rates attract funds, so the currency may appreciate. This lowers the price of imported goods and raw materials, which helps against cost-push inflation, and the fall in AD reduces demand-pull inflation. But a stronger currency makes exports dearer and reduces net exports, which may lower output and employment, and the effects take time.")], [("e", "Monetary policy is likely to be fairly successful with a floating exchange rate, because the currency effect reinforces the fall in AD, but the success depends on the elasticities of demand for exports and imports, time lags and the cause of the inflation.")]])
  ],
  )

tips = tips_html(
  [("Give the full chain.", "Rate change, borrowing, C and I, AD, output and prices."),
   ("Use AD/AS diagrams.", "Left shift for contractionary, right for expansionary."),
   ("Match policy to problem.", "Demand-pull versus cost-push."),
   ("Mention time lags.", "Effects can take 12 to 18 months."),
   ("Mention the limits.", "Zero bound, confidence, expectations."),
   ("Use the exchange rate.", "It can reinforce or offset the policy."),
   ("Compare and conclude.", "Fiscal and supply-side alternatives.")],
  [("Expansionary", "Expansionary monetary policy shifts AD to the right."),
   ("Contractionary", "Contractionary monetary policy shifts AD to the left."),
   ("Time lags", "Monetary policy takes time to affect the economy."),
   ("Zero lower bound", "Interest rates cannot usually fall far below zero."),
   ("Evaluation", "It depends on how consumers and firms respond and on the cause of inflation.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"], CW["discuss"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
function mcDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: false }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A higher interest rate shifts AD to the left, lowering the price level and output">${mcDraw({ a: -20, n: 1 })}</svg>`;
$("#pic2").innerHTML = (() => {
  const B = [["Quick to change", "Often independent of politics", 30, "f2"], ["Time lags", "12 to 18 months", 270, "f3"], ["Weak when", "Low confidence, near zero rates, cost-push", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Strengths and limits of monetary policy">${o}</svg>`;
})();
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary monetary policy to reduce inflation", base: { a: 0, n: 0 }, draw: mcDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Inflation is above target and AD is strong.", s: { a: 0, n: 0 } },
  { cap: "<b>The central bank raises interest rates.</b> Borrowing is dearer, saving is more attractive and the currency may rise. Consumption, investment and net exports fall: AD shifts <b>left</b>. The price level falls (inflation eases) but so does output.", s: { a: -20, n: 1 } },
  { cap: "<b>The trade-off.</b> Lower inflation comes with slower growth and possibly higher unemployment in the short run, and the effect appears only after a time lag.", s: { a: -20, n: 1 } },
] });
const flatDraw = (s) => adasPlot({ a: s.a, s: 0, g: 1, n: s.n }, { lras: true });
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Expansionary monetary policy and capacity", base: { a: 0, n: 0 }, draw: flatDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Start.</b> Equilibrium is below potential output (the dashed LRAS line): there is spare capacity.", s: { a: 0, n: 0 } },
  { cap: "<b>Rates are cut.</b> AD shifts <b>right</b>: real output and employment rise, with a rise in the price level.", s: { a: 20, n: 1 } },
  { cap: "<b>Near full capacity</b> the same shift would raise prices by more and output by less. That is why spare capacity matters for evaluation.", s: { a: 20, n: 1 } },
] });
chainStep("#stF", "Why expansionary policy may fail in a deflation", ["The central bank cuts rates close to zero", "Households expect prices to fall further, so they delay spending", "Firms are pessimistic and do not invest; banks lend cautiously", "Borrowing and spending barely rise", "AD stays weak; fiscal policy or QE may be needed"], [
  "<b>The usual tool is nearly exhausted.</b>", "<b>Expectations</b> work against the policy.", "<b>Low confidence</b> reduces the response to cheaper credit.", "<b>The AD shift is small.</b>", "<b>Other tools</b> (government spending, QE) may be needed."]);

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

chooser("h", [
  ["Demand-pull inflation", "Raise interest rates (contractionary)", "AD falls, so prices stabilise", "Time lags; lower growth and jobs", 5],
  ["Cost-push inflation", "Raise interest rates", "Output falls but costs remain high", "Does not address the source of the rise in costs", 2],
  ["Recession with spare capacity", "Cut rates and loosen credit", "AD rises, output and jobs recover", "Low confidence may limit the response", 3],
  ["Deflation", "Cut rates, QE", "AD rises and prices stop falling", "Rates near zero; expectations of falling prices", 2],
  ["Housing bubble", "Tighter credit regulation", "Slower lending and house price rises", "May hit first-time buyers; avoidance", 4],
  ["Overheating economy near full capacity", "Raise rates", "Slows AD growth to reduce inflation risk", "May slow the economy too much", 4]
], (it) => `${it[0]}: the monetary response is to ${it[1].toLowerCase()}. Likely effect: ${it[2].toLowerCase()}. Main limit: ${it[3].toLowerCase()}.`, "How effective monetary policy is likely to be");
''' + CLASSIFY("cl1", "Effect of a rise or a cut in interest rates?", ["Effect of a rise", "Effect of a cut"],
  [("Borrowing becomes dearer", 0), ("Saving becomes less attractive", 1), ("Consumption and investment fall", 0), ("The currency may weaken", 1), ("AD shifts left", 0), ("AD shifts right", 1), ("Mortgage payments fall for borrowers", 1), ("Savers earn more", 0)],
  "A rise makes credit dearer and saving more attractive; a cut does the reverse.") + CLASSIFY("cl2", "Is it a strength or a limit of monetary policy?", ["Strength", "Limit"],
  [("Interest rates can be changed quickly", 0), ("It can take 12 to 18 months to work fully", 1), ("Central banks are often independent of politics", 0), ("Pessimistic households may not borrow even at low rates", 1), ("Rates are close to zero and cannot fall further", 1), ("It can be adjusted in small steps", 0), ("It is less effective against cost-push inflation", 1), ("People may expect inflation and spend sooner", 1)],
  "Strengths: speed and flexibility. Limits: lags, confidence, expectations, zero bound, cost-push.") + ORDER(
  "Put the effect of a cut in interest rates in order.",
  ["The central bank cuts the base rate", "Borrowing becomes cheaper and saving less attractive", "Consumption and investment rise", "AD shifts to the right", "Real output rises and the price level may rise"],
  "Lower rates raise spending and AD.") + MATCH([
  ["Expansionary policy", "Lower rates or looser credit that raise AD"],
  ["Contractionary policy", "Higher rates or tighter credit that reduce AD"],
  ["Time lag", "Delay before a policy takes full effect"],
  ["Zero lower bound", "Interest rates cannot usually fall far below zero"],
  ["Demand-pull inflation", "Inflation caused by AD growing faster than AS"],
  ["Cost-push inflation", "Inflation caused by rising costs of production"]]) + CALC([
  {"q": "AD is 50 and spending is 70% responsive. A 2 point rate rise shifts AD left by 8 × 2 × 0.7 units. By how many units?", "a": 11.2, "unit": "", "tol": 0.1, "hint": "8 × 2 × 0.7.", "sol": "<b>11.2</b> units."},
  {"q": "A household with a $150,000 variable mortgage sees the rate rise from 4% to 6%. By how much do yearly interest payments rise ($)?", "a": 3000, "unit": "$", "tol": 1, "hint": "0.02 × 150,000.", "sol": "<b>$3,000</b> a year."},
  {"q": "That is how much more per month ($)?", "a": 250, "unit": "$", "tol": 1, "hint": "3,000 ÷ 12.", "sol": "<b>$250</b>."},
  {"q": "Inflation is 7% and the central bank's target is 2%. By how many percentage points is it above target?", "a": 5, "unit": "points", "tol": 0.1, "hint": "7 − 2.", "sol": "<b>5 points</b>."}]) + MCQ([
  ("A rise in interest rates will usually:", ["Shift AD left", "Shift AD right", "Shift LRAS right", "Raise investment"], 0, "Borrowing dearer."),
  ("Which inflation is monetary policy least suited to?", ["Cost-push", "Demand-pull", "Both equally", "Neither"], 0, "Higher rates do not cut costs."),
  ("A limit of monetary policy is:", ["Time lags", "Instant effect", "No effect on AD", "It lowers the deficit"], 0, "Delays."),
  ("Expansionary policy is most effective when:", ["There is spare capacity", "The economy is at full capacity", "Rates are negative", "Confidence is falling"], 0, "Output can rise without much inflation."),
  ("A higher interest rate may cause the currency to:", ["Appreciate", "Depreciate", "Be fixed", "Disappear"], 0, "Attracts funds from abroad.")
], "qz1") + CARDS([
  ("Expansionary", "AD right."),
  ("Contractionary", "AD left."),
  ("Time lags", "12 to 18 months."),
  ("Demand-pull", "Monetary policy works best."),
  ("Cost-push", "Monetary policy is weak."),
  ("Zero bound", "Rates cannot fall far below zero."),
  ("Exchange rate", "Can reinforce or offset."),
  ("Compare", "Fiscal and supply-side policy.")]) + MCQ(mc_exam)

build("as54b", "as-monetary-policy-effects", "Monetary Policy: Effects and Limitations", EY,
  "5.3.3 to 5.3.4: expansionary and contractionary policy in AD/AS analysis, which problems it suits, and its limits. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
