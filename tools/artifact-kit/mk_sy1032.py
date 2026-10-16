"""Syllabus 10.3.2-10.3.3 Policy conflicts and government failure in macroeconomic policy. Run: python3 tools/artifact-kit/mk_sy1032.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 10.3.2 to 10.3.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Policies aimed at one objective often <b>damage another</b>: cutting inflation may raise unemployment, faster growth may worsen the current account, and tighter environmental rules may slow output. These <b class="kw">conflicts</b> mean governments choose <b>trade-offs</b> and rarely meet every objective at once. <b class="kw">Government failure</b> in macroeconomic policy happens when intervention makes things worse or fails to improve them, because of time lags, poor information and forecasting, political motives, wrong theories, crowding out and unintended effects. A strong answer names the conflict or failure, shows the mechanism and judges how serious it is.</p></div>

  <h2>1 · Conflicts between objectives (10.3.2)</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy used</th><th>Helps</th><th>May harm</th><th>Why</th></tr>
    <tr><td><b>Higher interest rates</b> to cut inflation</td><td>Inflation, possibly the exchange rate</td><td>Growth, unemployment, exports</td><td>Lower spending and investment, a stronger currency makes exports dearer</td></tr>
    <tr><td><b>Expansionary fiscal or monetary policy</b> to cut unemployment</td><td>Growth, unemployment</td><td>Inflation, current account</td><td>Higher demand near capacity raises prices; higher incomes raise imports</td></tr>
    <tr><td><b>Fast growth</b></td><td>Jobs, incomes</td><td>Inflation, current account, environment, equity</td><td>Demand-pull pressure, import suction, resource use, gains may be unevenly shared</td></tr>
    <tr><td><b>Cutting a current account deficit</b> by deflation</td><td>Current account</td><td>Growth, unemployment</td><td>Lower spending cuts imports and also output</td></tr>
    <tr><td><b>Depreciation</b> to improve the current account</td><td>Current account, jobs</td><td>Inflation</td><td>Imported inflation, dearer inputs</td></tr>
    <tr><td><b>Fixed exchange rate</b> and low inflation</td><td>Exchange rate stability</td><td>Independent interest rate policy</td><td>Interest rates must be set to defend the rate, not to control domestic inflation</td></tr>
    <tr><td><b>Market-based supply-side reform</b></td><td>Growth, natural rate, competitiveness</td><td>Equity, short-run unemployment</td><td>Lower benefits and weaker unions may widen inequality and cut jobs in restructuring</td></tr>
    <tr><td><b>Tough environmental policy</b></td><td>Sustainability</td><td>Growth, jobs, prices</td><td>Higher costs for polluting industries</td></tr>
    <tr><td><b>Fiscal consolidation</b> (smaller deficit)</td><td>Debt, perhaps the current account</td><td>Growth, unemployment</td><td>Lower AD through the multiplier</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>
  <h3>Conflicts in the policy mix</h3>
  <p>Governments sometimes use policies that pull in opposite directions. A <b>tax cut</b> (expansionary fiscal) together with <b>higher interest rates</b> (contractionary monetary) may give higher demand from consumers but dearer borrowing for firms and a stronger currency: investment and exports could fall while inflation is only partly controlled. <b>Coordination</b> between fiscal and monetary authorities matters.</p>
  <h3>Can a government meet all objectives at once?</h3>
  <ul>
    <li><b>Usually not in the short run.</b> The Phillips curve, the growth-inflation link and the growth-current account link all imply trade-offs.</li>
    <li><b>Sometimes in the long run:</b> supply-side improvements that shift LRAS can raise growth and cut unemployment without inflation. Good luck (falling world prices), credibility and flexible markets can help.</li>
    <li>It depends on spare capacity: with a large negative output gap, expansion helps growth, jobs and has few costs.</li>
  </ul>

  <h2>2 · Government failure in macroeconomic policy (10.3.3)</h2>
  <p><b>Government failure</b> occurs when intervention fails to achieve its aim or leaves the economy worse off than if the government had done nothing.</p>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it leads to failure</th></tr>
    <tr><td><b>Time lags</b></td><td>Recognition, decision, implementation and effect lags mean policy takes effect after the problem has changed, so it may be pro-cyclical.</td></tr>
    <tr><td><b>Poor information and forecasting</b></td><td>Output gaps, the natural rate and multipliers cannot be measured exactly, so policy may be too weak or too strong.</td></tr>
    <tr><td><b>Political motives</b></td><td>A political business cycle: expansion before elections, cuts afterwards; short-termism; pressure from interest groups such as unions.</td></tr>
    <tr><td><b>Wrong model or theory</b></td><td>A policy based on a Laffer curve peak or on a stable Phillips curve may not produce the expected effect.</td></tr>
    <tr><td><b>Crowding out</b></td><td>Government borrowing raises interest rates and cuts private investment.</td></tr>
    <tr><td><b>Expectations</b></td><td>If people anticipate policy, behaviour changes and the policy's effect is smaller or cancelled (rational expectations).</td></tr>
    <tr><td><b>Unintended consequences</b></td><td>Privatisation creates private monopolies; benefit cuts increase poverty; protectionism triggers retaliation.</td></tr>
    <tr><td><b>Lack of credibility and time inconsistency</b></td><td>If governments are known to change policy, announcements do not change expectations.</td></tr>
    <tr><td><b>External constraints</b></td><td>Global shocks, capital flows and the exchange rate limit what a single government can do.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluating government failure</b>It does not follow that intervention should stop: markets also fail, and doing nothing in a deep recession can be costly. Better design reduces failure: independent central banks, rules or targets for inflation and debt, automatic stabilisers (no lags), transparent forecasts and policy tested against evidence. Compare the cost of failure with the cost of the original problem.</div>
'''

watch = '''
  <h2>1 · The web of conflicts between objectives</h2>
  <p>Green links mean policies help both objectives; red links mean they conflict. Press Play, or click the numbered steps.</p>
  <div id="stW"></div>
  <h2>2 · Time lags and policy that makes things worse</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab 1 · A policy mix and its side effects</h2>
  <p>Choose a change in interest rates, government spending and the exchange rate. The lab uses simple rules of thumb to show the likely effect on four objectives, so you can see where conflicts appear.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Objectives improved</small><strong id="r1"></strong></div><div><small>Objectives worsened</small><strong id="r2"></strong></div><div><small>Conflict?</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars showing the effect of the chosen policies on inflation, unemployment, growth and the current account"></svg></div></div></div>

  <h2>Lab 2 · Which kind of government failure?</h2>
  <p>Pick a scenario to see the type of failure and how it might be reduced.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Do the objectives conflict or reinforce each other?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the political business cycle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The UK 'Lawson boom' and bust, 1980s", "Tax cuts and low interest rates fuelled rapid growth and falling unemployment in the late 1980s, but inflation and the current account deficit rose. Interest rates were then raised sharply and the economy fell into recession in 1990 to 1992.", "a conflict between growth, inflation and the current account, and policy mistakes caused by misjudging the output gap.") +
rw("Austerity in the euro area after 2010", "Several governments cut spending and raised taxes to reduce debt. Output fell, unemployment rose and debt ratios rose in some countries because GDP was falling. Critics said the multiplier had been underestimated.", "fiscal consolidation conflicting with growth and jobs, and a forecasting failure about the multiplier.") +
rw("Tax cuts and rate rises together", "In 2018 the US cut taxes (raising demand) while the central bank raised interest rates (reducing demand). The mix raised the dollar and worsened the trade deficit even as growth stayed strong.", "a policy mix that pulls in two directions, and a conflict with the current account.") +
rw("Elections and the political business cycle", "Governments have been accused of cutting taxes or raising spending just before elections, then tightening afterwards. Economists have found some evidence in some countries, but it is hard to separate from other causes.", "a source of government failure from political motives. Say that independent central banks reduce the problem for monetary policy.")
)

mc_exam = [
  ("Which policy is most likely to conflict with a government's aim of price stability in the short run? (Oct/Nov 2021 · 32 · Q29, reworded)", ["More spending on education and health", "Raising the basic rate of income tax", "Limiting public sector wage rises", "Preventing mergers of large firms"], 0, "More spending raises aggregate demand and, if the economy is near capacity, prices."),
  ("The government raises interest rates to reduce inflation. What else is likely to result? (Feb/March 2024 · 32 · Q23, reworded)", ["A depreciation of the currency", "A fall in savings", "A reduction in economic growth", "A reduction in unemployment"], 2, "Higher interest rates reduce consumption and investment, so growth slows."),
  ("Which policy combination will reduce national income by the greatest amount? (Feb/March 2021 · 32 · Q23, reworded)", ["Cut direct taxes and raise interest rates", "Cut direct taxes and increase quantitative easing", "Raise direct taxes and raise interest rates", "Raise direct taxes and increase quantitative easing"], 2, "Both policies are contractionary and reinforce each other."),
  ("Which statement would both Keynesian and monetarist economists accept? (May/June 2021 · 31 · Q28, reworded)", ["High inflation and high unemployment are undesirable in a properly functioning economy", "Higher government spending on investment always crowds out private investment", "The best way out of recession is higher government spending", "The most effective way to cut inflation is tight control of the money supply"], 0, "Both schools agree these are problems. They disagree about causes and cures."),
  ("Which combination of policies will most likely succeed in reducing both unemployment and inflation? (Feb/March 2020 · 32 · Q30, reworded)", ["Contractionary supply-side policies and higher interest rates", "Expansionary supply-side policies and lower indirect taxes", "Higher direct taxes and lower indirect taxes", "Lower interest rates and a depreciation of the exchange rate"], 1, "Supply-side policy shifts LRAS right, and lower indirect taxes cut prices directly: both aims can improve."),
  ("Which condition attached to an IMF loan to a low-income country conflicts with the infant industry argument? (May/June 2025 · 32 · Q29, reworded)", ["The need to allow free trade", "The need to control inflation", "The need for contractionary fiscal policy", "The need to privatise state firms"], 0, "The infant industry argument supports temporary protection, which free trade rules out."),
  ("Which combination of policies is most likely to increase output? (May/June 2023 · 31 · Q23, reworded)", ["Smaller budget deficit and lower interest rates", "Smaller budget deficit and higher interest rates", "Larger budget deficit and lower interest rates", "Larger budget deficit and higher interest rates"], 2, "Expansionary fiscal and monetary policy both raise aggregate demand."),
  ("What is a reflationary fiscal measure? (Feb/March 2021 · 32 · Q30, reworded)", ["Increasing government spending", "Increasing taxes", "Increasing the money supply", "Reducing interest rates"], 0, "Reflationary fiscal policy raises AD through higher spending or lower taxes. The money supply and interest rates are monetary measures.")
]

exam = exam_page("policy conflicts and government failure in macroeconomic policy",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Conflicts between aims are tested in 13 and 25 mark Paper 4 essays; government failure in macro policy is usually part of the evaluation. Reworded questions are below, with a practice question on government failure and eight Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "2", "May/June 2020 (42) Q5; Oct/Nov 2021 (43) Q7"), ("Essay part, 13 marks", "2", "Feb/March 2022 (42) Q7(b); May/June 2022 (42) Q7(b)"), ("Practice question", "1", "Government failure in macroeconomic policy"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2020 · 9708/42 · Q5", "25 marks", "A government cuts taxes at the same time as its central bank announces that it will raise interest rates. Discuss how these policies may cause conflicts for the government in trying to achieve its macroeconomic aims.",
     ["Name the aims: growth, inflation, unemployment, the balance of payments and development.",
      "Tax cut: higher disposable income, consumption and investment, higher government borrowing; the multiplier raises output and jobs but may raise inflation and imports.",
      "Higher interest rates: lower consumption and investment, more attractive for savers, a higher exchange rate which cuts export competitiveness and import prices.",
      "Conflicts: demand pushed up by one policy and down by the other; growth and the current account; inflation and investment. Level 4 (18 to 25) needs at least three aims, both policies developed and a conclusion (maximum 21 without one)."],
     "Three aims. Tax cut route. Interest rate route. Show the two pull against each other. Conclude on which effect dominates."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q7", "25 marks", "A lender such as the IMF lends to developing countries but requires them to reduce import restrictions, focus on exporting primary goods and accept a devaluation. Assess whether developing countries should continue to borrow from it.",
     ["Examine each condition: removing import restrictions could worsen the balance of payments and hurt infant industries; focusing on primary goods exposes the country to unstable prices and low productivity; devaluation could cause cost-push inflation.",
      "Benefits of the loan: finance for investment, stability, a confidence signal. Weigh the negative effects against the benefits.",
      "Level 4 (18 to 25) needs analysis of each requirement, an evaluation of their combined effect, comment on the benefits and a conclusion."],
     "Three conditions, each with benefit and cost. Benefits of the loan. Weigh them and conclude for a typical developing economy."),
  eq("Based on Feb/March 2022 · 9708/42 · Q7(b)", "13 marks", "Discuss whether there is likely to be a conflict when a government tries to fix its exchange rate while introducing policies to reduce inflation.",
     ["Explain a fixed exchange rate and how the central bank defends it: buy the currency with reserves if it is falling, sell it if it is rising. Interest rates then have to serve the exchange rate.",
      "Conflict: reducing inflation requires higher interest rates or tight demand, which attracts capital and pushes the currency up, so the central bank must sell currency (expanding the money supply) or accept a revaluation; if the currency is under pressure, defending it requires higher rates, which may conflict with growth.",
      "Credit that a fixed rate can help cut inflation by importing low inflation from the anchor currency, so conflict is not certain."],
     "Define the fixed rate. Interest rate dilemma. Case where there is no conflict. Judge."),
  eq("Based on May/June 2022 · 9708/42 · Q7(b)", "13 marks", "Discuss whether monetary policy alone is sufficient for a government to achieve its macroeconomic aims at the same time.",
     ["Identify the aims: employment, inflation, growth and the balance of payments. Explain monetary policy and its limitations (lags, liquidity trap, conflicts).",
      "Impact of monetary policy changes on at least two aims, for example higher interest rates cut inflation but raise unemployment.",
      "Compare an alternative: fiscal policy or supply-side policy, which can address problems monetary policy cannot (structural unemployment, long-run growth).",
      "Level 4 (9 to 13) needs analysis of monetary policy on two aims, comparison with an alternative and an evaluation of the statement."],
     "Monetary policy on two aims. Its limits. Alternative policy. Judge: one instrument rarely meets several aims."),
  eq("Practice (not a past paper question)", "12 marks", "Explain why government intervention in the macroeconomy may fail to achieve its aims.",
     ["Time lags: policy takes effect after the problem has changed and may add to the cycle.",
      "Poor information: forecasting errors about the output gap, the natural rate and the multiplier.",
      "Political motives: policies timed for elections or influenced by interest groups.",
      "Other causes: crowding out, expectations, unintended consequences, external constraints.",
      "Evaluation: markets also fail, and automatic stabilisers, independent central banks and rules reduce the problem."],
     "Three causes, each with a mechanism. A limit on the argument: government failure is not a reason to do nothing.",
     [[("k", "Government failure in macroeconomic policy occurs when intervention fails to achieve its objective or makes the situation worse than it would have been without it."), ("n", "One cause is time lags. It takes time to recognise a problem, decide on a response and for the policy to work, so a stimulus decided in a recession may arrive during the recovery and push inflation up, making the cycle worse. A second cause is poor information: the output gap and the natural rate cannot be observed, so a government that overestimates spare capacity may stimulate demand too much, leading to inflation.")],
      [("n", "A third cause is political motivation. Governments may cut taxes or raise spending before an election and tighten afterwards, which creates a political business cycle that does not reflect the needs of the economy. Policies can also fail because of crowding out, where higher government borrowing raises interest rates and reduces private investment, and because people's expectations may offset policies, such as workers who raise wage demands when they expect inflation."), ("e", "However, government failure does not mean that intervention should be avoided, because markets can also fail and a deep recession can be costly. Independent central banks, rules for inflation and the use of automatic stabilisers, which have no lag, can reduce the risk of failure.")]])
  ],
  )

tips = tips_html(
  [("Name the conflict explicitly.", "For example: reducing inflation with higher interest rates conflicts with growth and employment."),
   ("Use the Phillips curve and the AD and AS model.", "They show conflicts: AD policy moves along the SRPC; AS policy can help both."),
   ("Say it depends on spare capacity.", "With a negative output gap the conflict is smaller; near capacity it is larger."),
   ("Show both policies in a mix.", "Explain what each does and how they pull against each other."),
   ("For government failure, give mechanisms.", "Time lags, forecasting errors, political motives, crowding out, expectations, unintended effects."),
   ("Evaluate: market failure too.", "Government failure does not mean that doing nothing is better."),
   ("Conclude on a mix.", "A set of policies matched to the causes usually works better than one instrument.")],
  [("Conflict", "Higher interest rates could reduce inflation but they may also reduce investment and growth, so the aims conflict."),
   ("Mix", "A tax cut raises demand while higher interest rates reduce it, so the two policies may offset each other."),
   ("Failure", "Time lags may mean that a stimulus takes effect only when the economy is already recovering, which raises inflation."),
   ("Political", "A government may cut taxes before an election, which creates a political business cycle."),
   ("Evaluate", "However, markets can also fail, and rules and independent institutions could reduce the risk of government failure.")],
  [CW["explain"], CW["discuss"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Web of objectives ---------- */
const OBJ = ["Inflation", "Unemployment", "Growth", "Current account", "Sustainability", "Equity"];
const WC = 380, WCY = 165, WR = 120;
const wp = (i) => { const a = -Math.PI / 2 + i * Math.PI / 3; return [WC + Math.cos(a) * WR, WCY + Math.sin(a) * WR]; };
const LINKS = [[0, 1, "c", 1], [2, 0, "c", 2], [2, 3, "c", 2], [2, 4, "c", 3], [2, 5, "c", 3], [3, 0, "c", 3], [2, 1, "g", 4], [4, 0, "g", 4]];
function webDraw(s) {
  let o = "";
  LINKS.forEach(([a, b, k, st]) => { const v = Math.max(0, Math.min(1, s.n - st + 1)); if (v <= 0) return; const A = wp(a), B = wp(b); o += SV.line(A[0], A[1], B[0], B[1], k === "c" ? "c2" : "c3", { "stroke-width": 3.5, ...(k === "c" ? { "stroke-dasharray": "7 5" } : {}), ...op(v) }); });
  OBJ.forEach((n, i) => { const p = wp(i), side = i === 0 ? "t" : i === 3 ? "b" : i < 3 ? "r" : "l"; o += SV.circle(p[0], p[1], 20, "nd"); const tx = side === "r" ? p[0] + 30 : side === "l" ? p[0] - 30 : p[0], ty = side === "t" ? p[1] - 30 : side === "b" ? p[1] + 40 : p[1] + 5, an = side === "r" ? "start" : side === "l" ? "end" : "middle"; o += SV.text(tx, ty, n, "lbl bd", { "text-anchor": an }); });
  return o + tag(40, 24, "red dashed = conflict   green = reinforce", "t1");
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Six macroeconomic objectives joined by lines showing conflicts and links">${webDraw({ n: 4 })}</svg>`;
Lib.stepper($("#stW"), { w: 760, h: 330, label: "Six macroeconomic objectives with red dashed lines for conflicts and green lines for reinforcing links", base: { n: 0 }, draw: webDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Six objectives</b>: inflation, unemployment, growth, the current account, sustainability and equity. No links yet.", s: { n: 0 } },
  { cap: "<b>Inflation and unemployment.</b> In the short run lowering unemployment tends to raise inflation (the Phillips curve). A <b>conflict</b>.", s: { n: 1 } },
  { cap: "<b>Growth and inflation, and growth and the current account.</b> Demand-led growth near capacity raises prices, and higher incomes raise imports. Two more <b>conflicts</b>.", s: { n: 2 } },
  { cap: "<b>Growth and sustainability, growth and equity, the current account and inflation.</b> Faster growth uses resources and may be uneven; a weak currency helps the current account but raises inflation.", s: { n: 3 } },
  { cap: "<b>Reinforcing links.</b> Growth can reduce unemployment, and supply-side growth can <b>reduce</b> inflation by raising capacity. Policy works best when it uses these links.", s: { n: 4 } },
] });

/* ---------- Time lags ---------- */
const TX = (t) => 70 + t * 66, TY = (v) => 170 - v * 70;
const cyc = (t) => Math.sin(2 * Math.PI * t / 6), pol = (t, lag, k) => (t < lag ? 0 : -k * Math.sin(2 * Math.PI * (t - lag) / 6));
function lagDraw(s) {
  let o = SV.line(70, 170, 730, 170) + SV.line(70, 40, 70, 300) + SV.text(730, 190, "Time (years)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Output relative to trend", "sm");
  const line = (fn, cls) => { const pts = []; for (let t = 0; t <= 10; t += 0.1) pts.push([TX(t), TY(fn(t))]); return SV.path(Lib.ptsPath(pts), cls); };
  o += line(cyc, "c1 dash") + tag(TX(1.5), TY(1) - 10, "no policy", "t1", 1, "middle");
  if (s.k > 0) o += line((t) => cyc(t) + pol(t, s.lag, s.k), "c2") + tag(TX(4.5), TY(cyc(4.5) + pol(4.5, s.lag, s.k)) + 26, "with policy", "t2", 1, "middle");
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 320, label: "Business cycle with no policy, well-timed counter-cyclical policy, and policy delayed by time lags that amplifies the cycle", base: { k: 0, lag: 0 }, draw: lagDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The cycle.</b> Output swings around trend (dashed). A government wants to reduce the swings.", s: {} },
  { cap: "<b>Well-timed policy.</b> If the government raises demand just as output falls and cuts it as output rises, the combined line is much flatter: <b>stabilisation</b>.", s: { k: 0.8, lag: 0 } },
  { cap: "<b>Policy with a lag.</b> If it takes about half a cycle to recognise the problem, decide and for the effect to arrive, the stimulus lands when the economy is already recovering. It adds to the boom and the later bust.", s: { k: 0.8, lag: 3 } },
  { cap: "<b>Government failure.</b> With a long lag the policy makes the cycle <b>larger</b>, not smaller. Automatic stabilisers have almost no lag, which is why they help avoid this problem.", s: { k: 0.8, lag: 3 } },
] });

/* ---------- Lab 1: policy mix ---------- */
function labMix() {
  if (!$("#mi") || !$("#mg") || !$("#me")) return;
  const i = +$("#mi").value / 10, g = +$("#mg").value / 10, e = +$("#me").value / 10;
  const coef = { inf: [-0.4, 0.3, 0.08], unemp: [0.3, -0.4, -0.03], gr: [-0.5, 0.8, 0.05], ca: [-0.3, -0.3, 0.08] };
  const eff = (k) => coef[k][0] * i + coef[k][1] * g + coef[k][2] * e;
  const rows = [["Inflation", eff("inf"), -1], ["Unemployment", eff("unemp"), -1], ["Growth", eff("gr"), 1], ["Current account", eff("ca"), 1]];
  const good = rows.filter((r) => r[1] * r[2] > 0.05), bad = rows.filter((r) => r[1] * r[2] < -0.05);
  $("#r1").textContent = good.length; $("#r2").textContent = bad.length; $("#r3").textContent = good.length && bad.length ? "Yes" : good.length ? "No" : bad.length ? "All worse" : "None";
  $("#rv").textContent = !good.length && !bad.length ? "No policy change: nothing moves." : good.length && bad.length ? `Better: ${good.map((r) => r[0].toLowerCase()).join(", ")}. Worse: ${bad.map((r) => r[0].toLowerCase()).join(", ")}. The same package improves some objectives and damages others: a conflict.` : good.length ? `Only improvements: ${good.map((r) => r[0].toLowerCase()).join(", ")}. Check whether this package is realistic in the short run.` : `All affected objectives are worse: ${bad.map((r) => r[0].toLowerCase()).join(", ")}.`;
  const mx = 1.2; let o = SV.line(40, 150, 400, 150) + tag(40, 24, "Change in each indicator (illustrative, per unit)", "t1");
  rows.forEach((r, k) => { const x = 60 + k * 85, h = Math.min(100, Math.abs(r[1]) / mx * 100), y = r[1] >= 0 ? 150 - h : 150, better = r[1] * r[2] > 0.05, worse = r[1] * r[2] < -0.05; o += SV.rect(x, y, 60, Math.max(h, 2), better ? "f3" : worse ? "f2" : "f1") + tag(x + 30, r[1] >= 0 ? y - 6 : y + h + 16, (r[1] >= 0 ? "+" : "") + Lib.fmtN(r[1], 2), better ? "t3" : worse ? "t2" : "t1", 1, "middle") + SV.text(x + 30, 290, r[0], "sm bd", { "text-anchor": "middle" }) + SV.text(x + 30, 270, better ? "better" : worse ? "worse" : "", "sm", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mi", label: "Change in interest rate (points) ", min: -20, max: 40, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labMix });
Lib.slider($("#g2"), { id: "mg", label: "Change in government spending (% of GDP) ", min: -20, max: 40, step: 5, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labMix });
Lib.slider($("#g3"), { id: "me", label: "Change in the exchange rate (% depreciation) ", min: -100, max: 100, step: 10, value: 0, fmt: (v) => Lib.fmtN(v / 10, 0), onInput: labMix });
labMix();
btnTable("lbBtns", "lbOut", [
  ["A stimulus arrives after the recovery has begun", "Time lag", "The policy takes effect after the problem has changed", "Rely more on automatic stabilisers, act early, monitor forecasts"],
  ["A government overestimates spare capacity", "Poor information", "Stimulus is too large and inflation rises", "Use a range of indicators, publish forecasts, review the estimates"],
  ["Tax cuts and public spending timed before an election", "Political motives", "Policy serves the election cycle, not the economy", "Independent central bank, fiscal rules"],
  ["High government borrowing pushes up interest rates", "Crowding out", "Private investment falls, offsetting the stimulus", "Finance deficits in recessions when private demand for funds is low"],
  ["Workers expect inflation and demand higher pay", "Expectations", "Demand policy only has temporary effects", "Credible inflation target, supply-side policy"],
  ["Privatisation creates a private monopoly", "Unintended consequence", "Efficiency gains are lost to higher prices", "Regulation, promote competition"]
], ["Scenario", "Type of failure", "Why it fails", "How to reduce it"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the pair of objectives usually conflict or reinforce each other?", ["Usually conflict (short run)", "Can reinforce each other"],
  [("Low unemployment and low inflation", 0), ("Fast growth and a balanced current account", 0), ("Growth from supply-side improvement and low inflation", 1), ("Growth and sustainability if growth uses fossil fuels", 0), ("Growth and falling unemployment", 1), ("Lower inflation and a stronger currency", 1), ("Fast growth and a more equal income distribution when gains go to owners of capital", 0), ("Fixed exchange rate and independent interest rate policy", 0)],
  "Many pairs conflict in the short run but can be reconciled by supply-side policy.") + MATCH([
  ["Government failure", "Intervention fails to meet its aim or makes things worse"],
  ["Time lag", "Delay between a problem, a policy and its effect"],
  ["Political business cycle", "Policy timed to win elections rather than to suit the economy"],
  ["Crowding out", "Public borrowing reduces private investment"],
  ["Policy mix", "The combination of fiscal, monetary and other policies used together"],
  ["Automatic stabiliser", "A tax or benefit that moves with the cycle without delay"]]) + ORDER(
  "Put the political business cycle in order.",
  ["An election is approaching", "The government cuts taxes and raises spending", "Output and employment rise and the government is popular", "After the election inflation and debt rise and the government tightens policy", "A slowdown follows"],
  "Policy timed for votes can create a cycle.") + CALC([
  {"q": "A government raises spending by 2% of GDP and the multiplier is 1.5. Calculate the rise in output as a % of GDP.", "a": 3, "unit": "%", "tol": 0.05, "hint": "2 × 1.5.", "sol": "2 × 1.5 = <b>3%</b>."},
  {"q": "The true output gap is −2% but the government estimates it at −5% and sets a stimulus to close it using a multiplier of 1.5. By what % of GDP does it overshoot if it fully closes the estimated gap (output rise = 5%)?", "a": 3, "unit": "%", "tol": 0.05, "hint": "Output rise minus true gap.", "sol": "Output rises 5% against a true gap of 2%, so output ends <b>3%</b> above potential, which is inflationary."},
  {"q": "Inflation falls by 3 points when interest rates rise 2 points, and unemployment rises by 1.5 points. Calculate the rise in unemployment per point of fall in inflation.", "a": 0.5, "tol": 0.01, "hint": "1.5 ÷ 3.", "sol": "1.5 ÷ 3 = <b>0.5 points</b> of unemployment per point of inflation."},
  {"q": "A government borrows an extra $40bn. Because of higher interest rates, private investment falls by $12bn. Calculate the crowding out as a percentage of the extra borrowing.", "a": 30, "unit": "%", "tol": 0.05, "hint": "12 ÷ 40.", "sol": "12 ÷ 40 × 100 = <b>30%</b>."}]) + MCQ([
  ("Which is a likely conflict when a government raises interest rates to cut inflation?", ["Lower growth and higher unemployment", "Higher growth", "A weaker currency", "Lower savings"], 0, "Higher rates reduce spending and investment."),
  ("Why may a stimulus package fail to stabilise the economy?", ["Time lags mean it may take effect after the recovery has begun", "Fiscal policy has no effect on AD", "The multiplier is always zero", "The exchange rate is always fixed"], 0, "Lags can turn a counter-cyclical policy into a pro-cyclical one."),
  ("Which is an example of a political business cycle?", ["Tax cuts before an election followed by tighter policy after it", "A central bank setting rates by a rule", "An automatic stabiliser", "A currency intervention"], 0, "Policy timed for votes rather than economic needs."),
  ("Which reduces the risk of government failure caused by lags?", ["Automatic stabilisers", "Larger deficits", "Higher tariffs", "Fewer forecasts"], 0, "Automatic stabilisers respond immediately without any decision."),
  ("Which policy pair is most likely to offset each other?", ["A tax cut and a rise in interest rates", "A tax cut and a rise in government spending", "A rise in interest rates and a cut in government spending", "Quantitative easing and a rate cut"], 0, "One policy raises AD and the other reduces it.")
], "qz1") + CARDS([
  ("Policy conflict", "A policy that helps one objective but harms another."),
  ("Trade-off", "Having to give up some of one objective to gain more of another."),
  ("Government failure", "Intervention that fails or makes things worse."),
  ("Time lag", "Delay before a policy takes effect."),
  ("Political business cycle", "Policy timed to elections."),
  ("Crowding out", "Government borrowing displaces private spending."),
  ("Time inconsistency", "Government announces a policy and then has an incentive to change it."),
  ("Automatic stabiliser", "Moves with the cycle without a decision.")]) + MCQ(mc_exam)

build("sy1032", "policy-conflicts-government-failure", "Policy Conflicts and Government Failure in Macroeconomic Policy", EY,
  "10.3.2 to 10.3.3: the problems and conflicts that arise from macroeconomic policies, and the causes of government failure in macroeconomic policy. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
