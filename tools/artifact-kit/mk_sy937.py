"""Syllabus 9.3.7 Policies to reduce unemployment and their effectiveness (chapter 43). Run: python3 tools/artifact-kit/mk_sy937.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.3.7"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The right policy depends on the <b>type</b> of unemployment. <b>Demand-side policies</b> (expansionary fiscal and monetary policy, a lower exchange rate) raise aggregate demand and work on <b>cyclical</b> (demand-deficient) unemployment. <b>Supply-side policies</b> improve how the labour market works and work on <b>frictional, structural and real wage</b> unemployment, so they lower the natural rate. Each policy has limits: <b>time lags, cost, crowding out, inflation, balance of payments effects</b> and fairness. A strong answer matches policy to cause and judges effectiveness.</p></div>

  <h2>1 · Match the policy to the cause</h2>
  <div class="tw"><table class="t">
    <tr><th>Type of unemployment</th><th>Best policy</th><th>Why</th></tr>
    <tr><td><b>Cyclical</b> (demand-deficient)</td><td>Demand-side: fiscal and monetary stimulus, lower exchange rate</td><td>The problem is too little spending in the economy</td></tr>
    <tr><td><b>Frictional</b></td><td>Better information (job centres, online vacancies), lower benefits or job-search conditions</td><td>Cut the search time and the incentive to delay</td></tr>
    <tr><td><b>Structural</b></td><td>Education, retraining, relocation help, regional investment, subsidies for new industries</td><td>The unemployed have the wrong skills or location</td></tr>
    <tr><td><b>Real wage</b> (classical)</td><td>Reduce union power, reform or freeze the minimum wage, improve productivity</td><td>The wage is above equilibrium</td></tr>
    <tr><td><b>Seasonal</b></td><td>Diversify local industry, training for off-season work</td><td>Demand for labour is concentrated in one season</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>

  <h2>2 · Demand-side policies</h2>
  <div class="grid2">
    <div class="card"><h3>Fiscal policy</h3><p><b>Raise government spending or cut taxes</b> (a bigger budget deficit). AD shifts right, the multiplier raises income and output, and firms hire more.</p><ul>
      <li><b>Strengths:</b> direct, can be targeted (public works), works well with spare capacity.</li>
      <li><b>Weaknesses:</b> time lags, crowding out, debt and interest costs, may raise inflation near full capacity, leakages (saving, imports), no effect on structural unemployment.</li></ul></div>
    <div class="card"><h3>Monetary policy</h3><p><b>Lower interest rates, quantitative easing or a lower exchange rate.</b> Cheaper borrowing raises consumption and investment, and a lower exchange rate raises exports.</p><ul>
      <li><b>Strengths:</b> quick to change, independent of politics.</li>
      <li><b>Weaknesses:</b> weak when confidence is low or interest rates are already near zero (liquidity trap), lags, inflation and asset price risks, a lower exchange rate raises import costs.</li></ul></div>
  </div>
  <div class="tip"><b class="h">Keynesian and monetarist views</b>Keynesians support demand management when there is a negative output gap and wages are sticky. Monetarists argue demand policy cannot cut unemployment below the natural rate for long without inflation, so the answer is the supply side (see 9.3.4).</div>

  <h2>3 · Supply-side policies</h2>
  <div class="grid2">
    <div class="card"><h3>Interventionist</h3><ul>
      <li><b>Education and training, apprenticeships:</b> better skills, occupational mobility.</li>
      <li><b>Job centres and information:</b> shorter search.</li>
      <li><b>Subsidies</b> for hiring the long-term unemployed or for new industries; <b>regional policy</b> and enterprise zones.</li>
      <li><b>Relocation grants and housing support:</b> geographical mobility.</li>
      <li><b>Infrastructure:</b> jobs now and capacity later.</li>
    </ul></div>
    <div class="card"><h3>Market-based</h3><ul>
      <li><b>Reduce unemployment benefits</b> or tighten conditions: stronger incentive to work.</li>
      <li><b>Cut income tax</b> and employers' payroll taxes: more incentive to work and to hire.</li>
      <li><b>Weaken union power;</b> reform or restrain the minimum wage: lower real wage unemployment.</li>
      <li><b>Deregulate and ease hiring and firing:</b> firms hire more readily.</li>
      <li><b>Competition and free trade:</b> efficiency, new jobs in competitive industries.</li>
    </ul></div>
  </div>
  <div class="tip"><b class="h">Weaknesses of supply-side policy</b>Slow (training takes years, mobility improves slowly), costly, may be unfair (lower benefits, weaker unions may increase hardship and inequality), cannot create jobs if demand is weak, and uncertain: retraining may not match the jobs that exist.</div>

  <h2>4 · Judging effectiveness</h2>
  <ul>
    <li><b>Cause:</b> does the policy fit the type of unemployment?</li>
    <li><b>Speed:</b> demand policy acts within months to a few years; supply-side policy takes years.</li>
    <li><b>Cost and funding:</b> deficits, debt and crowding out, or the cost of training.</li>
    <li><b>Side effects:</b> inflation, current account deficit, inequality, environment.</li>
    <li><b>Conflicts between aims:</b> cutting unemployment may raise inflation (Phillips curve trade-off) or worsen the balance of payments.</li>
    <li><b>Scale of the problem:</b> a small negative gap needs a small stimulus; hysteresis or deep structural change needs targeted help.</li>
    <li><b>Conclusion:</b> usually a <b>mix</b> of demand and supply-side policy matched to the causes.</li>
  </ul>
'''

watch = '''
  <h2>1 · A demand stimulus closes a negative output gap</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · Matching policy to the type of unemployment</h2>
  <div id="stM"></div>
'''

explore = '''
  <h2>Lab 1 · How big a stimulus?</h2>
  <p>An economy has a negative output gap. Choose the size of the fiscal stimulus and the multiplier. See what happens to the gap, unemployment, inflation pressure and the deficit.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Unemployment</small><strong id="r1"></strong></div><div><small>Output gap after</small><strong id="r2"></strong></div><div><small>Extra deficit (% of GDP)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars showing the output gap before and after the stimulus"></svg></div></div></div>

  <h2>Lab 2 · Policy effectiveness table</h2>
  <p>Pick a policy to see which unemployment it targets, how fast it acts and what limits it.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which kind of policy?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a fiscal stimulus in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Germany's short-time work scheme", "In the 2008 to 2009 recession, German firms cut hours instead of jobs, with the state paying part of the lost wages. Unemployment barely rose even though output fell sharply, and firms kept skilled workers for the recovery.", "a targeted policy for cyclical unemployment that also prevented hysteresis. Evaluate on cost to the government and whether it delays needed structural change.") +
rw("Fiscal stimulus after the financial crisis", "Many governments cut taxes and raised spending in 2009, and central banks cut rates to near zero and began quantitative easing. Output recovered but budget deficits and debt rose sharply and the recovery in jobs was slow in some countries.", "demand-side policy with deficit and debt costs. Say effectiveness depended on the size of the gap, confidence and the multiplier.") +
rw("Apprenticeships and youth training", "Countries such as Germany and Switzerland run apprenticeships that combine work and study, and have low youth unemployment. Other countries have tried to copy them with mixed results.", "a supply-side policy for structural and youth unemployment. Evaluate on time lags, employer participation and how well training matches the jobs on offer.") +
rw("Benefit reform", "Several countries have shortened the period for which unemployment benefits are paid or linked benefits to job-search requirements. Unemployment fell in some cases, but critics point to lower pay, hardship and more low-quality jobs.", "market-based supply-side policy. Give both sides: stronger incentives against greater hardship and inequality.")
)

mc_exam = [
  ("What is an example of a Keynesian policy that would reduce cyclical unemployment? (Feb/March 2020 · 32 · Q23, reworded)", ["Government spending on new infrastructure such as roads", "Government spending on retraining workers", "A cut in the tax on imports", "A cut in the tax on goods and services"], 0, "Keynesian policy raises aggregate demand directly. Retraining is supply-side."),
  ("Which of these is a Keynesian measure to reduce cyclical unemployment? (Oct/Nov 2020 · 33 · Q28, reworded)", ["Retraining unskilled workers", "Letting the private sector supply merit goods", "Using more capital equipment per worker", "Using fiscal policy to increase effective demand"], 3, "Keynesian policy tackles deficient demand through fiscal policy."),
  ("Which combination of fiscal, monetary and supply-side policies is most likely to reduce unemployment? (Feb/March 2021 · 32 · Q22, reworded)", ["Raise taxes, raise interest rates, increase labour market flexibility", "Raise government spending, cut the money supply, more education and training", "Cut taxes, cut interest rates, more labour market flexibility", "Cut government spending, raise the money supply, more education and training"], 2, "Cutting taxes and rates boosts demand, and labour market flexibility improves the supply side."),
  ("Which statement is correct about government policy to reduce unemployment? (Oct/Nov 2021 · 33 · Q22, reworded)", ["A government cannot reduce seasonal unemployment", "Changing interest rates is the best way to reduce the natural rate", "A change in the exchange rate cannot reduce demand-deficient unemployment", "Supply-side policy can be used to reduce frictional unemployment"], 3, "Better job information is supply-side and cuts frictional unemployment."),
  ("What is the most effective policy a government could introduce to reduce frictional unemployment? (May/June 2023 · 31 · Q21, reworded)", ["Cut welfare spending", "Improve information about job vacancies", "Reduce tax rates", "Raise interest rates"], 1, "Frictional unemployment is about search time, so better information is the most direct policy."),
  ("There has been a switch in demand from labour-intensive products to products made using high technology. Unemployment has risen. What is the best policy to reduce this unemployment? (May/June 2022 · 31 · Q22, reworded)", ["Cut the rate of income tax", "Raise the interest rate on borrowing for investment", "Subsidise products made by labour-intensive methods", "Subsidise exports of high-technology industries"], 2, "A subsidy for labour-intensive products raises demand for the labour that was displaced. The other options do not target the mismatch."),
  ("Which policy is likely to increase unemployment? (Feb/March 2023 · 32 · Q20, reworded)", ["More retraining facilities", "A large rise in indirect taxes", "Selective import controls", "A larger public sector deficit"], 1, "Higher indirect taxes cut real incomes and demand, so firms cut jobs."),
  ("In an economy with unemployed resources the marginal propensity to consume is 0.2. The government raises its deficit and borrows from the non-bank public. What is the likely consequence? (Feb/March 2025 · 32 · Q24, reworded)", ["The currency will depreciate and the trade deficit will fall", "The rise in real output will be limited because the multiplier is low", "The money supply will fall, reducing aggregate demand", "Interest rates will fall, causing demand-pull inflation"], 1, "With an MPC of 0.2 the multiplier is only 1.25, so the stimulus has a small effect on output.")
]

exam = exam_page("policies to reduce unemployment",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Questions on policy and unemployment are among the most common in Paper 4, as 12, 13, 20 and 25 mark essays. Reworded questions are below, with eight Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "2", "Feb/March 2022 (42) Q6; May/June 2022 (41) Q7 (see the 9.3.4 page)"), ("Essay, 20 marks", "2", "Oct/Nov 2023 (41) Q4; May/June 2023 (41) Q4"), ("Essay part, 13 marks", "4", "Oct/Nov 2020 (42, 43); Oct/Nov 2021 (42); Oct/Nov 2022 (43)"), ("Data response part, 6 marks", "1", "May/June 2025 (41, 43) 1(b)"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2025 · 9708/41 and 43 · Q1(b)", "6 marks", "A government uses fiscal policy to keep unemployment low. Analyse how this policy can affect the unemployment rate.",
     ["Explain fiscal policy: changes in government spending and taxation (2 marks).",
      "A correct diagram explained (up to 4 marks), for example AD shifting right towards LRAS, or the Keynesian cross with a deflationary gap closing.",
      "Analysis: higher spending or lower taxes raise AD, output rises through the multiplier, firms hire more, so cyclical unemployment falls. Up to 2 marks for each developed example."],
     "Define fiscal policy. AD diagram. Spending route and tax route. Multiplier. Short link to jobs."),
  eq("Based on Oct/Nov 2020 · 9708/43 · Q6(b)", "13 marks", "Critically evaluate the use of Keynesian demand management policies to solve the problem of unemployment.",
     ["Explain the theory: the government uses budget deficits to raise AD, supported by a diagram (AD and AS, or Keynesian cross).",
      "Evaluation: crowding out, risk of inflation, balance of payments problems as spending leaks into imports, growth of national debt, time lags, and little effect on structural or frictional unemployment.",
      "Level 4 (9 to 13) needs at least two problems identified and their significance explained, and a conclusion."],
     "Theory with diagram. Two or three problems, each explained. Conclusion on when it works."),
  eq("Based on Oct/Nov 2021 · 9708/42 · Q6(b)", "13 marks", "Evaluate the policies a government could use to reduce structural unemployment.",
     ["Define structural unemployment and its causes.",
      "Evaluate at least three policies: education and training, lower taxes or subsidies for businesses in affected areas, housing support or relocation grants to raise mobility, reducing union power or the wage floor, tariffs for declining industries.",
      "Level 4 (9 to 13) needs three policies evaluated: cost, time lags, whether the new jobs exist, fairness."],
     "Define. Three policies, each with a strength and weakness. Choose the most effective."),
  eq("Based on Oct/Nov 2020 · 9708/42 · Q5(b)", "13 marks", "Discuss whether supply-side policies are the most appropriate way to reduce unemployment.",
     ["Explain a range of supply-side policies (training, education, lower taxes, limits on union power, subsidies, information) and their impact on different types of unemployment.",
      "Consider fiscal and monetary policy: where supply-side policy is not appropriate, such as cyclical unemployment in a recession.",
      "Level 4 needs the idea that supply-side policy suits some causes and demand policy others. Maximum 11 without a conclusion."],
     "Which causes each policy fits. Where supply-side fails. Conclude with a mix."),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q5(b)", "13 marks", "'The introduction of new technology will increase efficiency but will also cause an increase in unemployment.' Discuss the extent to which you agree.",
     ["Technology raises productivity (output per worker), which makes production more efficient and can lower costs and prices.",
      "Substituting machines for labour can cause structural unemployment, especially for routine jobs.",
      "Counter: new industries and jobs are created, lower prices raise demand, growth creates jobs, and retraining can reduce unemployment. Other types of unemployment (cyclical, frictional) are unrelated to technology.",
      "Conclude by weighing the short-run job losses against the long-run gains in output and jobs, and the role of policy."],
     "Efficiency. Job loss. Job creation. Role of retraining. Judgement."),
  eq("Based on Oct/Nov 2023 · 9708/41 · Q4", "20 marks", "Assess the extent to which monetary policy can be used effectively to reduce unemployment.",
     ["<b>Knowledge and analysis (14):</b> instruments (interest rates, the money supply including quantitative easing, the exchange rate); why unemployment is a problem (waste of resources); causes of unemployment; how lower interest rates raise consumption and investment, and how a lower exchange rate raises exports.",
      "<b>Evaluation (6):</b> works best on cyclical unemployment and little on structural or frictional unemployment, where supply-side policy fits better; lags; low confidence or a liquidity trap; side effects on inflation and the exchange rate."],
     "Instruments, then the link to jobs. Match to type of unemployment. Limits. Judge."),
  eq("Based on May/June 2023 · 9708/41 · Q4", "20 marks", "A government increases its budget surplus. Evaluate the statement that this will increase unemployment in the short run but make it easier to control a balance of payments deficit in the long run.",
     ["<b>Knowledge and analysis (14):</b> a budget surplus (revenue above spending); lower government spending or higher taxes reduce AD and, through the multiplier, output, so demand-deficient unemployment may rise; links to interest rates and the exchange rate; the balance of payments accounts.",
      "<b>Evaluation (6):</b> the short-run rise in unemployment depends on spare capacity and how the surplus is achieved; lower AD reduces imports and inflation, which improves competitiveness and the current account only over time; other causes of a current account deficit (structural competitiveness, exchange rate); a lower deficit may also lower debt and interest rates."],
     "Surplus, AD, jobs. Then imports, inflation, competitiveness. Evaluate with spare capacity and time. Judge both halves of the statement.")
  ] + [
  eq("Practice (not a past paper question)", "8 marks", "Explain why a fiscal stimulus is more effective at reducing cyclical unemployment than structural unemployment.",
     ["Cyclical unemployment is caused by a lack of demand, so raising AD with government spending or tax cuts creates demand for labour (about 3 marks).",
      "Structural unemployment is caused by a mismatch of skills or location, so extra demand does not match the unemployed to vacancies; training or mobility policies are needed (about 3 marks).",
      "Evaluation: a stimulus may help some structural unemployment if it creates jobs in the right region, and if it is too large it may only raise inflation (about 2 marks)."],
     "Cause of cyclical, so the stimulus fits. Cause of structural, so it does not. One evaluative point.",
     [[("k", "Cyclical unemployment arises because aggregate demand is too low, so firms cut output and jobs."), ("n", "A fiscal stimulus, such as higher government spending or lower taxes, raises aggregate demand, and with the multiplier effect national income, output and employment all rise, so firms need more workers and cyclical unemployment falls.")],
      [("n", "Structural unemployment is different because it is caused by a mismatch between the skills or location of workers and the jobs available. If a coal miner has no electrical qualifications, extra demand for installers will not employ him, because he is not able to do the work. The vacancies and the unemployed exist side by side, so raising demand has little effect and may only raise wages and prices. Retraining or help to move would be more effective.")],
      [("e", "However, a stimulus aimed at jobs in the declining region, such as public works there, could still reduce some structural unemployment, and a deep recession can turn into structural unemployment through hysteresis, so early demand support may prevent that.")]])
  ],
  )

tips = tips_html(
  [("Match policy to cause first.", "Say which type of unemployment you are tackling before you name the policy."),
   ("Draw the diagram.", "AD shifting right towards LRAS for demand-side policy. LRAS or labour market diagrams for supply-side policy."),
   ("Give the chain.", "Policy, then AD or labour market change, then output or jobs. Do not just list the policy."),
   ("Name two or three limits.", "Time lags, crowding out, inflation, balance of payments, debt, cost, fairness."),
   ("Split supply-side into two groups.", "Interventionist (training, subsidies) and market-based (benefits, taxes, unions). Examiners reward the distinction."),
   ("Say that a mix usually works best.", "A conclusion that matches different policies to different causes shows judgement."),
   ("Use 'could' and 'depends on'.", "The effect depends on spare capacity, the size of the multiplier and the time horizon.")],
  [("Match", "A fiscal stimulus is likely to be most effective for cyclical unemployment, because the cause is a lack of aggregate demand."),
   ("Chain", "Higher government spending could shift AD to the right, raising output and, through the multiplier, employment."),
   ("Limit", "However, borrowing to finance the deficit may raise interest rates and crowd out private investment."),
   ("Supply-side", "Retraining could reduce structural unemployment by improving the occupational mobility of workers."),
   ("Judge", "On balance, a mix of demand-side and supply-side policy is most likely to work, because most economies have more than one type of unemployment.")],
  [CW["explain"], CW["analyse"], CW["discuss"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- AD and AS helper ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adas(a, lr) {
  const Q = (a - 15) / 1.6, P = 15 + 0.7 * Q; let s = axes(70, 320, 740, 30, "Real GDP", "Price level");
  s += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  s += SV.line(AX(0), AY(15), AX(100), AY(85), "c2") + tag(AX(100) - 4, AY(85) - 8, "SRAS", "t2", 1, "end");
  s += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  s += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4");
  return { s, Q, P };
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Policy map: demand-side policy shifts AD for cyclical unemployment, supply-side policy shifts LRAS and lowers the natural rate">${(() => { let o = tag(380, 24, "Match the policy to the cause", "t1", 1, "middle"); const rows = [["Cyclical", "AD policy", "fiscal, monetary, exchange rate", "t2"], ["Frictional", "Information", "job centres, vacancy sites", "t1"], ["Structural", "Skills and mobility", "training, housing, regional aid", "t4"], ["Real wage", "Wage flexibility", "union reform, minimum wage review", "t3"], ["Seasonal", "Diversify", "year-round jobs, off-season training", "t1"]]; rows.forEach(([a, b, c, t], i) => { const y = 50 + i * 54; o += SV.rect(60, y, 150, 40, "f1") + SV.text(135, y + 26, a, "lbl bd", { "text-anchor": "middle" }) + arrow(215, y + 20, 290, y + 20, "r", "c1", 1) + SV.rect(295, y, 170, 40, "f4") + SV.text(380, y + 26, b, "lbl bd", { "text-anchor": "middle" }) + tag(480, y + 25, c, t); }); return o; })()}</svg>`;

/* ---------- Watch 1: fiscal stimulus ---------- */
function stimDraw(s) {
  const r = adas(s.a, 60), gap = r.Q - 60, u = gap < 0 ? 5 + 0.6 * -gap : Math.max(2.5, 5 - 0.2 * gap);
  let o = r.s;
  if (Math.abs(gap) > 0.8) o += SV.line(AX(Math.min(r.Q, 60)), 296, AX(Math.max(r.Q, 60)), 296, gap < 0 ? "c2" : "c4", { "stroke-width": 5 }) + tag(AX((r.Q + 60) / 2), 288, gap < 0 ? "negative gap" : "positive gap", gap < 0 ? "t2" : "t4", 1, "middle");
  o += SV.rect(300, 36, 150, 54, "f1") + tag(375, 58, "Unemployment", "t1", 1, "middle") + SV.text(375, 82, Lib.fmtN(u, 1) + "%", "lbl bd", { "text-anchor": "middle", style: "font-size:20px" });
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 365, label: "AD shifting right with a fiscal stimulus: unemployment falls, then inflation rises if the stimulus overshoots", base: { a: 100 }, draw: stimDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>Cyclical unemployment.</b> AD is too low, so equilibrium output is below the LRAS: a negative output gap and unemployment of about 9%, well above the natural rate of 5%.", s: {} },
  { cap: "<b>A fiscal stimulus.</b> The government raises spending or cuts taxes. AD shifts right. Output rises through the multiplier, firms hire and unemployment falls towards the natural rate.", s: { a: 111 } },
  { cap: "<b>The right size.</b> The gap is closed and unemployment is at the natural rate of 5%. A stimulus sized to the gap cuts cyclical unemployment without raising prices much.", s: { a: 111 } },
  { cap: "<b>Overshooting.</b> If the stimulus is too big, output goes above potential. Unemployment can only dip below the natural rate temporarily, and the price level rises: inflation. This is the limit of demand-side policy.", s: { a: 128 } },
] });

/* ---------- Watch 2: policy match ---------- */
function mtDraw(s) {
  const rows = [["Cyclical", "raise AD: fiscal and monetary policy", "t2"], ["Frictional", "better job information", "t1"], ["Structural", "retraining, relocation, regional aid", "t4"], ["Real wage", "union reform, wage flexibility", "t3"], ["Seasonal", "diversify, off-season training", "t1"]];
  let o = ""; rows.forEach(([a, b, t], i) => { const v = Math.max(0, Math.min(1, s.n - i)); const y = 30 + i * 56; o += SV.rect(50, y, 150, 40, "f1") + SV.text(125, y + 26, a, "lbl bd", { "text-anchor": "middle" }); if (v > 0) o += arrow(205, y + 20, 270, y + 20, "r", "c1", v) + SV.rect(275, y, 190, 40, "f4", op(v)) + SV.text(370, y + 26, ["demand-side", "supply-side: information", "supply-side: skills", "supply-side: market-based", "supply-side: structure"][i], "lbl bd", { "text-anchor": "middle", ...op(v) }) + tag(480, y + 25, b, t, v); }); return o;
}
Lib.stepper($("#stM"), { w: 760, h: 320, label: "Each type of unemployment matched to the policy that tackles its cause", base: { n: 0 }, draw: mtDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Cyclical.</b> The cause is too little spending, so the cure is demand-side: more government spending or lower taxes and interest rates.", s: { n: 1 } },
  { cap: "<b>Frictional.</b> The cause is search time, so the cure is information: job centres and online vacancy sites. Extra demand is not needed.", s: { n: 2 } },
  { cap: "<b>Structural.</b> The cause is a skills or location mismatch, so the cure is retraining, relocation help and regional investment.", s: { n: 3 } },
  { cap: "<b>Real wage.</b> The cause is a wage above equilibrium, so the cure is wage flexibility: union reform or a more careful minimum wage.", s: { n: 4 } },
  { cap: "<b>Seasonal.</b> The cause is seasonal demand, so the cure is diversifying local industry and training for off-season work. <b>Using the wrong policy wastes money:</b> demand stimulus does little for structural unemployment.", s: { n: 5 } },
] });

/* ---------- Lab 1: fiscal stimulus size ---------- */
function labStim() {
  if (!$("#gp") || !$("#st") || !$("#km")) return;
  const gap = -+$("#gp").value, S = +$("#st").value / 10, k = +$("#km").value / 10, rise = S * k, after = gap + rise;
  const u = after < 0 ? 5 + 0.6 * -after : Math.max(2.5, 5 - 0.2 * after), infl = after > 0 ? 2 + 0.8 * after : 2, def = S;
  $("#r1").textContent = Lib.fmtN(u, 1) + "%"; $("#r2").textContent = (after >= 0 ? "+" : "") + Lib.fmtN(after, 1) + "%"; $("#r3").textContent = "+" + Lib.fmtN(def, 1) + "%";
  $("#rv").textContent = after < -0.5 ? `A stimulus of ${Lib.fmtN(S, 1)}% of GDP with a multiplier of ${Lib.fmtN(k, 1)} raises output by ${Lib.fmtN(rise, 1)}%. The gap narrows from ${Lib.fmtN(gap, 1)}% to ${Lib.fmtN(after, 1)}%, but unemployment is still ${Lib.fmtN(u - 5, 1)} points above the natural rate. The stimulus is too small, or the multiplier too weak.` : after <= 1 ? `The stimulus raises output by ${Lib.fmtN(rise, 1)}% and almost closes the gap. Unemployment is back at about the natural rate with little inflation pressure. The deficit is ${Lib.fmtN(def, 1)}% of GDP higher.` : `The stimulus raises output by ${Lib.fmtN(rise, 1)}%, pushing output ${Lib.fmtN(after, 1)}% above potential. Unemployment dips below the natural rate temporarily and inflation pressure rises to about ${Lib.fmtN(infl, 1)}%. The stimulus is too large.`;
  const bars = [["Gap before", gap, gap < 0 ? "f2" : "f4"], ["Gap after", after, after < -0.5 ? "f2" : after <= 1 ? "f3" : "f4"]], mx = 12, base = 150, sc = 100 / mx;
  let o = SV.line(40, base, 400, base);
  bars.forEach((b, i) => { const x = 90 + i * 150, h = Math.abs(b[1]) * sc, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, 90, Math.max(h, 2), b[2]) + tag(x + 45, b[1] >= 0 ? y - 8 : y + h + 18, (b[1] >= 0 ? "+" : "") + Lib.fmtN(b[1], 1) + "%", "t1", 1, "middle") + SV.text(x + 45, 280, b[0], "sm bd", { "text-anchor": "middle" }); });
  o += tag(40, 24, "Output gap, % of potential", "t1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gp", label: "Size of negative output gap (%) ", min: 1, max: 10, step: 1, value: 6, fmt: (v) => v, onInput: labStim });
Lib.slider($("#g2"), { id: "st", label: "Stimulus (% of GDP, x10) ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labStim });
Lib.slider($("#g3"), { id: "km", label: "Multiplier (x10) ", min: 8, max: 25, step: 1, value: 15, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labStim });
labStim();
btnTable("lbBtns", "lbOut", [
  ["Increase government spending", "Cyclical", "Months to 2 years", "Deficit, crowding out, leakages, inflation near capacity"],
  ["Cut interest rates / QE", "Cyclical", "6 to 18 months", "Weak in a liquidity trap or low confidence; asset bubbles"],
  ["Retraining and apprenticeships", "Structural, youth", "2 to 10 years", "Costly, slow, may not match vacancies"],
  ["Job centres and vacancy information", "Frictional", "Months", "Limited effect if the cause is a skills mismatch"],
  ["Cut benefits or tighten job-search conditions", "Frictional, voluntary, natural rate", "1 to 3 years", "Hardship, inequality, low-quality jobs"],
  ["Cut payroll taxes / hiring subsidies", "Structural, natural rate", "1 to 3 years", "Cost to the government, may subsidise jobs that would exist anyway"],
  ["Weaken union power / reform the minimum wage", "Real wage", "2 to 5 years", "Lower wages, inequality, political resistance"]
], ["Policy", "Mainly targets", "Time lag", "Main weaknesses"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What kind of policy is it?", ["Demand-side", "Supply-side (interventionist)", "Supply-side (market-based)"],
  [("Cut income tax and raise government spending to boost AD", 0), ("Fund an apprenticeship scheme", 1), ("Shorten the period for which unemployment benefits are paid", 2), ("Cut interest rates", 0), ("Relocation grants for workers moving to vacancies", 1), ("Weaken the legal power of trade unions", 2), ("Quantitative easing", 0), ("Build a job centre network with vacancy information", 1)],
  "Demand-side moves AD. Interventionist supply-side uses government spending on skills and information. Market-based supply-side relies on incentives and competition.") + MATCH([
  ["Cyclical unemployment", "Caused by a fall in aggregate demand"],
  ["Structural unemployment", "Caused by a mismatch of skills or location"],
  ["Crowding out", "Government borrowing reduces private investment"],
  ["Multiplier", "Total rise in income is a multiple of the initial rise in spending"],
  ["Active labour market policy", "Training, job-search help and subsidies for hiring"],
  ["Hysteresis", "Cyclical unemployment that becomes long-term"]]) + ORDER(
  "Put the effect of a fiscal stimulus on cyclical unemployment in order.",
  ["The government raises spending or cuts taxes", "Aggregate demand rises", "Firms see higher sales and increase output", "Firms hire more workers", "Unemployment falls, helped by the multiplier"],
  "The stimulus works through demand for output, then demand for labour.") + CALC([
  {"q": "The multiplier is 2 and the government raises spending by $5bn. Calculate the rise in national income ($bn).", "a": 10, "unit": "$bn", "tol": 0.05, "hint": "Multiplier × change in spending.", "sol": "2 × 5 = <b>$10bn</b>."},
  {"q": "The output gap is −6% of potential GDP and the multiplier is 1.5. By what percentage of GDP must government spending rise to close the gap?", "a": 4, "unit": "%", "tol": 0.05, "hint": "Gap ÷ multiplier.", "sol": "6 ÷ 1.5 = <b>4% of GDP</b>."},
  {"q": "A retraining scheme costs the government $12,000 per trainee. 500 of 2,000 trainees find jobs they would not have found otherwise. Calculate the cost per extra job ($).", "a": 48000, "unit": "$", "tol": 1, "hint": "Total cost ÷ extra jobs.", "sol": "Total cost = 2,000 × 12,000 = $24m. Cost per extra job = 24,000,000 ÷ 500 = <b>$48,000</b>."},
  {"q": "Unemployment is 9% and the natural rate is 5%. Using Okun's law (2% of output per point of cyclical unemployment), by what percentage must output rise to remove cyclical unemployment?", "a": 8, "unit": "%", "tol": 0.05, "hint": "4 points × 2.", "sol": "4 × 2 = <b>8%</b>."}]) + MCQ([
  ("Which policy is most likely to reduce cyclical unemployment?", ["Retraining", "A fall in interest rates", "Relocation grants", "A cut in unemployment benefit"], 1, "Lower interest rates raise AD, which raises demand for labour."),
  ("Which policy best matches structural unemployment?", ["Quantitative easing", "Retraining and relocation support", "A fall in the exchange rate", "A rise in government spending on defence"], 1, "Structural unemployment is a skills or location mismatch."),
  ("What is a main weakness of fiscal stimulus?", ["It cannot raise AD", "It may crowd out private investment and raise debt", "It always lowers prices", "It only affects imports"], 1, "Borrowing can raise interest rates and the national debt."),
  ("What is a main weakness of supply-side policy?", ["It lowers potential output", "It takes a long time to work", "It always raises inflation", "It only affects cyclical unemployment"], 1, "Skills, mobility and incentives change slowly."),
  ("Which would most reduce frictional unemployment?", ["A rise in government spending", "A better online vacancy service", "A fall in interest rates", "A weaker currency"], 1, "Faster matching of workers and vacancies shortens search time.")
], "qz1") + CARDS([
  ("Demand-side policy", "Fiscal, monetary or exchange rate policy to raise AD."),
  ("Supply-side policy", "Policy to improve the labour market and raise capacity."),
  ("Interventionist supply-side", "Training, subsidies, job centres, infrastructure."),
  ("Market-based supply-side", "Lower benefits and taxes, weaker unions, deregulation."),
  ("Multiplier", "Total rise in income as a multiple of the initial injection."),
  ("Crowding out", "Government borrowing reduces private investment."),
  ("Active labour market policy", "Training, job-search help and hiring subsidies."),
  ("Time lag", "Delay before a policy takes full effect.")]) + MCQ(mc_exam)

build("sy937", "policies-to-reduce-unemployment", "Policies to Reduce Unemployment and Their Effectiveness", EY,
  "9.3.7: demand-side and supply-side policies for each type of unemployment, and how to judge how effective they are. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
