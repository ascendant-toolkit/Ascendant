"""Syllabus 10.3.1 Effectiveness of policy options. Run: python3 tools/artifact-kit/mk_sy1031.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 10.3.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Each policy works best on some objectives and badly or not at all on others. <b>Fiscal policy</b> (including the <b class="kw">Laffer curve</b> argument for lower tax rates) and <b>monetary policy</b> act mainly on aggregate demand. <b>Supply-side policy</b>, <b>market-based</b> or <b>interventionist</b>, shifts aggregate supply and acts slowly. <b>Exchange rate policy</b> and <b>international trade policy</b> work mostly through the balance of payments and are <b>expenditure-switching</b>. To judge effectiveness, ask which objective the policy targets, how big and how fast the effect is, what it costs and what it does to the other objectives.</p></div>

  <h2>1 · The policy options</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it works</th><th>Works best on</th><th>Main limits</th></tr>
    <tr><td><b>Fiscal</b></td><td>Government spending and taxes change AD (and sometimes AS); the multiplier magnifies the effect</td><td>Cyclical unemployment and a negative output gap; inflation when tightened</td><td>Time lags, debt and crowding out, leakages to imports, inflation near capacity, political limits</td></tr>
    <tr><td><b>Monetary</b></td><td>Interest rates, money supply and QE change borrowing and spending, and the exchange rate</td><td>Inflation; short-run demand management</td><td>Lags, weak in a liquidity trap or when confidence is low, conflicts with growth, jobs and the exchange rate</td></tr>
    <tr><td><b>Supply-side, market-based</b></td><td>Deregulation, privatisation, lower taxes, weaker unions: incentives and competition</td><td>Long-run growth, the natural rate of unemployment, inflation without lost output</td><td>Slow, may widen inequality, politically hard, little help in a demand-led recession</td></tr>
    <tr><td><b>Supply-side, interventionist</b></td><td>Education, training, infrastructure, R&amp;D subsidies, regional policy</td><td>Structural unemployment, productivity, competitiveness</td><td>Costly, slow, may be badly targeted (government failure)</td></tr>
    <tr><td><b>Exchange rate</b></td><td>Depreciate or devalue to make exports cheaper and imports dearer; appreciate to cut import prices</td><td>The current account (expenditure-switching), growth from net exports; inflation when appreciating</td><td>Marshall-Lerner condition, J curve, imported inflation, retaliation, loss of reserves to defend a rate</td></tr>
    <tr><td><b>International trade</b></td><td>Tariffs, quotas, subsidies and trade agreements change the relative price of imports</td><td>The current account, protecting jobs in some industries; growth from trade liberalisation</td><td>Higher prices, retaliation, inefficiency, WTO rules, hurts consumers and exporters</td></tr>
  </table></div>

  <h2>2 · Fiscal policy and the Laffer curve</h2>
  <ul>
    <li><b>Fiscal policy</b> raises or lowers AD by changing spending or taxes. In a downturn a larger budget deficit raises output and jobs; near capacity a smaller deficit cools inflation.</li>
    <li>The <b>Laffer curve</b> shows tax revenue against the tax rate. At 0% revenue is zero; at 100% nobody has an incentive to work legally so revenue is also near zero. <b>Revenue is highest at an optimum rate.</b></li>
    <li>If the rate is <b>above the peak</b>, <b>cutting</b> the tax could <b>raise revenue</b>, because lower rates reduce avoidance and evasion and increase work effort, saving and enterprise. This supports <b>supply-side tax cuts</b>.</li>
    <li><b>Evaluate:</b> where the peak lies is uncertain (estimates vary), most countries are probably left of it, labour supply may be inelastic, cuts may widen inequality, and effects take time.</li>
  </ul>
  <div id="pic1" class="card"></div>

  <h2>3 · Monetary policy</h2>
  <ul>
    <li>Raising <b>interest rates</b> reduces consumption and investment (the transmission mechanism), attracts hot money and may raise the exchange rate, so inflation falls but <b>growth and jobs may fall</b>.</li>
    <li>Lowering rates or <b>quantitative easing</b> boosts AD and may depreciate the currency, but may be ineffective if confidence is low (liquidity trap) and may raise inflation or asset prices.</li>
    <li>It can be changed quickly by an independent central bank, but with a lag of 12 to 24 months.</li>
  </ul>

  <h2>4 · Supply-side policy</h2>
  <ul>
    <li><b>Market-based:</b> privatisation, deregulation, labour market reform, lower income and corporation taxes (using Laffer logic), competition policy.</li>
    <li><b>Interventionist:</b> investment in education, training, infrastructure, R&amp;D, regional policy.</li>
    <li>The best policy for <b>long-run, non-inflationary growth</b> and a lower natural rate, but slow and costly, and it does not solve a lack of demand.</li>
  </ul>

  <h2>5 · Exchange rate policy and the J curve</h2>
  <ul>
    <li>A <b>depreciation or devaluation</b> makes exports cheaper abroad and imports dearer at home (<b>expenditure-switching</b>). The current account improves if the <b>Marshall-Lerner condition</b> holds: the sum of the price elasticities of demand for exports and imports is greater than 1.</li>
    <li>The <b>J curve</b>: in the short run the current account often <b>worsens first</b>, because demand is inelastic and import prices rise at once, then improves as volumes adjust.</li>
    <li>Costs: imported inflation, higher costs of imported inputs, retaliation, and loss of reserves if a rate is defended. An <b>appreciation</b> lowers inflation but hurts exporters.</li>
  </ul>

  <h2>6 · International trade policy</h2>
  <ul>
    <li><b>Protection</b> (tariffs, quotas, export subsidies) switches spending from imports to domestic goods, which can improve the current account and protect jobs and infant industries.</li>
    <li>Costs: higher prices for consumers and firms using imported inputs, retaliation by trading partners, protected firms become inefficient, WTO rules limit it.</li>
    <li><b>Trade liberalisation</b> raises competition and efficiency and may raise long-run growth, but job losses in uncompetitive industries (structural unemployment) can follow.</li>
  </ul>
  <div class="tip"><b class="h">How to evaluate effectiveness</b>Match the policy to the cause, quantify its size (multiplier, elasticities), consider timing, cost, and the effect on the other objectives (see 10.3.2). A mix of policies is usually needed.</div>
'''

watch = '''
  <h2>1 · The Laffer curve</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · A devaluation and the J curve</h2>
  <div id="stJ"></div>
'''

explore = '''
  <h2>Lab 1 · Where is the economy on the Laffer curve?</h2>
  <p>Choose the tax rate and how responsive taxpayers are (avoidance and effort). Find the revenue-maximising rate and see whether a cut would raise or lower revenue.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Tax revenue (index)</small><strong id="r1"></strong></div><div><small>Revenue-maximising rate</small><strong id="r2"></strong></div><div><small>A small tax cut would</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Laffer curve with the chosen tax rate marked"></svg></div></div></div>

  <h2>Lab 2 · Policy and objectives</h2>
  <p>Pick a policy to see what it is likely to do to each objective in the short run and the long run.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which policy is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a depreciation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("US tax cuts in the 1980s and 2017", "Supporters of the Laffer curve argued that cutting top tax rates would raise revenue. Studies of both periods generally found that revenue fell compared with what would otherwise have been collected, suggesting rates were below the peak.", "an example for Laffer analysis, with evaluation that most economies are left of the peak.") +
rw("UK devaluation in 1967 and the pound after 2016", "After the pound fell in 1967 and again in 2016 the trade balance did not improve immediately. Import prices rose first and export volumes responded over a longer period.", "the J curve and the Marshall-Lerner condition. Use it to say the short-run effect may be the opposite of the long-run effect.") +
rw("US tariffs on steel and aluminium", "In 2018 the US imposed tariffs on steel and aluminium to protect domestic producers. Steel prices rose for US manufacturers, some trading partners retaliated, and employment gains in steel were small compared with job losses elsewhere.", "trade policy and its costs. Evaluate on retaliation, higher costs for users and consumers, and the effect on competitiveness.") +
rw("Quantitative easing after 2008", "Central banks bought government bonds to push down long-term interest rates when official rates were already near zero. It helped to stabilise financial markets, but its effect on spending was modest and it raised asset prices.", "monetary policy limits: a liquidity trap and distributional effects.")
)

mc_exam = [
  ("What does the Laffer curve show? (Feb/March 2022 · 32 · Q29, reworded)", ["The relationship between inflation and unemployment", "The relationship between the interest rate and the demand for money", "The relationship between tax rates and tax revenue", "The relationship between how two goods can be produced with given resources"], 2, "The Laffer curve plots tax revenue against the tax rate."),
  ("What is illustrated by the Laffer curve? (Oct/Nov 2022 · 33 · Q28, reworded)", ["As income rises, fewer hours will be worked", "As income rises, tax revenue will rise", "As the tax rate rises, tax revenue always rises", "As the tax rate rises, tax revenue will eventually fall"], 3, "Beyond some rate, higher rates reduce effort and increase avoidance, so revenue falls."),
  ("Which policy to encourage growth might be based on the Laffer curve? (Oct/Nov 2023 · 32 · Q23, reworded)", ["Cuts in direct taxes", "Exchange rate depreciation", "Investment subsidies", "Quantitative easing"], 0, "Laffer analysis suggests that lowering high tax rates could raise effort, growth and revenue."),
  ("The chief economist says that raising the top rate of income tax from 40% to 45% is likely to cut tax revenue by 2%. Which concept explains this? (May/June 2022 · 32 · Q29, reworded)", ["The Kuznets curve", "The Laffer curve", "The Lorenz curve", "The Phillips curve"], 1, "The Laffer curve explains why higher rates can reduce revenue."),
  ("Which macroeconomic policy is most likely to be used as a long-run means of reducing inflationary pressures? (Feb/March 2020 · 32 · Q29, reworded)", ["Exchange rate policy", "Fiscal policy", "Monetary policy", "Supply-side policy"], 3, "Supply-side policy raises capacity and productivity, which lowers cost pressure in the long run."),
  ("What is an example of an expenditure-switching policy? (Feb/March 2023 · 32 · Q29, reworded)", ["A rise in income tax rates", "A rise in interest rates", "A rise in tariff rates", "A rise in the money supply"], 2, "Tariffs switch spending from imports to home-produced goods. Higher taxes and interest rates are expenditure-reducing."),
  ("In 2018 the US imposed a tariff on steel imports. What is the likely impact on the US economy? (May/June 2020 · 31 · Q30, reworded)", ["US steel exports become more price competitive", "Productive inefficiency in the US steel industry", "A deterioration in the US terms of trade", "A fall in producer surplus for US steel producers"], 1, "Protection reduces competitive pressure, so domestic producers become less efficient."),
  ("Which policy may increase economic growth without causing inflation? (Feb/March 2025 · 32 · Q21, reworded)", ["Subsidies to producers", "Higher government spending", "Lower direct taxes", "Lower interest rates"], 0, "Subsidies to producers lower costs and shift supply to the right, so they raise output without adding to demand.")
]

exam = exam_page("the effectiveness of macroeconomic policies",
  "We searched the A Level Economics papers in the folder (2020 to 2025). These are some of the most important Paper 4 questions: 12, 13, 20 and 25 mark essays on fiscal, monetary, supply-side, exchange rate and trade policy. Reworded questions are below, with eight Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "1", "Oct/Nov 2020 (43) Q7"), ("Essay, 20 marks", "3", "May/June 2023 (42) Q4, Q5; Oct/Nov 2024 (43) Q5"), ("Essay part, 12 marks", "1", "Feb/March 2020 (42) Q7(a)"), ("Practice question", "1", "Exchange rate policy and the J curve"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on Feb/March 2020 · 9708/42 · Q7(a)", "12 marks", "With the help of a diagram, explain Laffer curve analysis and consider its link to supply-side policies.",
     ["A correctly drawn and labelled Laffer curve showing tax revenue against the tax rate, with the revenue-maximising rate.",
      "Link to supply-side policy: cutting tax rates that are above the peak could raise work effort, saving and enterprise, reducing avoidance and raising output and revenue. This is a market-based supply-side policy.",
      "Examples of alternative taxation policies and their outcomes. Level 4 (9 to 12) needs a clear understanding of the potential importance of the analysis for tax policy, and some discussion of its limits (the peak is uncertain, equity, time lags)."],
     "Draw. Explain both sides of the peak. Link to tax cuts as supply-side policy. Evaluate: uncertain peak, equity."),
  eq("Based on May/June 2023 · 9708/42 · Q5", "20 marks", "Evaluate the effectiveness of using monetary policy to reduce inflation and how this may affect the government's ability to achieve its other macroeconomic aims.",
     ["<b>Knowledge and analysis (14):</b> monetary instruments (interest rates, money supply, exchange rate, reserve asset ratio); define inflation and state the other aims; transmission mechanism of higher interest rates through consumption and investment, shown with AD and AS; apply the same model to growth, unemployment and the balance of payments; Phillips curve analysis of the trade-off between inflation and employment.",
      "<b>Evaluation (6):</b> time lags; the cause of inflation (demand-pull or cost-push); a higher exchange rate may reduce exports; impact on borrowers and investment; the central bank's independence and credibility; conflicts between the aims."],
     "Instruments, then transmission. Apply to the other aims. Evaluate with cause of inflation, lags and conflicts. Judge."),
  eq("Based on May/June 2023 · 9708/42 · Q4", "20 marks", "Consider the extent to which depreciation of its exchange rate contributes to economic growth in a low-income country.",
     ["<b>Knowledge and analysis (14):</b> a depreciation lowers the external value; export prices fall abroad and import prices rise; effect on demand for exports and imports; net exports (X − M) raise AD, shown with an AD and AS diagram or the multiplier; link to actual growth and, through investment, potential growth.",
      "<b>Evaluation (6):</b> Marshall-Lerner and the J curve; low-income countries export primary products with inelastic demand and import capital goods; imported inflation; foreign-currency debt becomes dearer; capacity limits; retaliation."],
     "Chain to net exports and AD. Actual then potential growth. Evaluate with elasticities, imported inputs and foreign debt."),
  eq("Based on Oct/Nov 2024 · 9708/43 · Q5", "20 marks", "Some high-income countries have introduced high tariffs on some imports to reduce the negative effects of globalisation on their economies. With the help of a diagram, evaluate this policy.",
     ["<b>Knowledge and analysis (14):</b> globalisation (free trade, movement of capital and labour, technology transfer); characteristics of high-income economies; the negative effect of cheap imports on jobs and some industries; selective tariffs with an accurately labelled diagram (price rises, imports fall, domestic output rises, tariff revenue, deadweight loss).",
      "<b>Evaluation (6):</b> retaliation and a trade war, higher prices for consumers and firms, inefficiency of protected firms, WTO rules, effect on the current account and employment overall, alternatives such as retraining and supply-side measures."],
     "Define globalisation. Tariff diagram. Winners and losers. Evaluate with retaliation and alternatives."),
  eq("Based on Oct/Nov 2020 · 9708/43 · Q7", "25 marks", "'The rate of interest is one of the most important macroeconomic variables because changes in it have a significant impact on each of the key macroeconomic aims.' To what extent do you agree?",
     ["Explain the aims and how the interest rate affects each: inflation (spending, investment), growth, unemployment, the exchange rate and the balance of payments, and possibly equity.",
      "Evaluation: the size of each effect depends on interest elasticity, confidence, time lags and the state of the economy; other variables (fiscal policy, exchange rate, supply-side factors, global demand) can matter more; conflicts between aims when rates change.",
      "A conclusion that weighs the importance of interest rates against other variables."],
     "Show effect on each aim. Then show where it is weak. Compare with other variables. Judge."),
  eq("Practice (not a past paper question)", "8 marks", "Explain why a devaluation might make the current account worse before it improves.",
     ["Immediately after a devaluation, import prices rise in domestic currency while the volumes bought are fixed by existing contracts and habits, so the import bill rises. Export prices in foreign currency fall, so export receipts may fall initially.",
      "Over time demand for exports rises and demand for imports falls as buyers switch, so volumes adjust.",
      "The J curve and the Marshall-Lerner condition: the current account improves in the long run if PEDx + PEDm is greater than 1.",
      "Evaluation: imported inflation and retaliation may cancel the benefits."],
     "Price effect first. Volume effect later. Marshall-Lerner. One limit.",
     [[("k", "A devaluation is a fall in the value of a fixed exchange rate. It makes exports cheaper for foreign buyers and imports dearer for domestic buyers."), ("n", "In the short run, demand for both is inelastic because contracts are already agreed and it takes time to find new suppliers and customers. Import prices rise immediately in domestic currency, so the import bill goes up, and export revenue may fall because each export earns less foreign currency. The current account therefore worsens first, which gives the J-shaped path.")],
      [("n", "As time passes, buyers at home switch to domestic goods and foreigners buy more exports, so the volumes adjust and the current account improves. Over the long run this happens only if the sum of the price elasticities of demand for exports and imports is greater than one, the Marshall-Lerner condition."), ("e", "However, dearer imported inputs raise costs and could cause inflation, and trading partners might retaliate, so the improvement may be smaller than the simple theory suggests.")]])
  ],
  )

tips = tips_html(
  [("Always link policy to objective.", "Say which objective, the mechanism and the size of the effect."),
   ("Draw the diagram the question asks for.", "Laffer curve, AD and AS, tariff diagram or the J curve. Without a diagram 20 mark answers are capped."),
   ("Say expenditure-switching or expenditure-reducing.", "Exchange rate and trade policy switch spending. Fiscal and monetary tightening reduce it."),
   ("Use Marshall-Lerner and the J curve.", "Depreciation works only if PEDx + PEDm is greater than 1, and the current account may worsen first."),
   ("Laffer: say 'above the peak'.", "Tax cuts raise revenue only if the rate is above the revenue-maximising rate. Most countries are probably below it."),
   ("Compare policies.", "Fiscal and monetary are fast but short-run. Supply-side is slow but permanent. Choose by cause and time horizon."),
   ("Evaluate with cost, lags and other aims.", "Every policy has a price. Name it.")],
  [("Laffer", "If the tax rate is above the revenue-maximising rate, a cut could raise tax revenue because avoidance and disincentives fall."),
   ("Expenditure-switching", "A depreciation could improve the current account by switching spending from imports to domestic output, if the Marshall-Lerner condition holds."),
   ("J curve", "In the short run demand is inelastic, so the current account may worsen before it improves."),
   ("Compare", "Monetary policy acts quickly but with a lag, whereas supply-side policy takes years but raises capacity."),
   ("Evaluate", "However, the effectiveness of the policy depends on the cause of the problem and may conflict with other objectives.")],
  [CW["explain"], CW["consider"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Laffer curve ---------- */
const LX = (t) => 70 + t * 6.2, LY = (r) => 300 - r * 2.5, LR = (t, k = 1) => t * (100 - k * t) / 25;
function lafDraw(s) {
  const k = 1, pk = 50;
  let o = axes(70, 300, 700, 30, "Tax rate (%)", "Tax revenue"); [0, 25, 50, 75, 100].forEach((t) => (o += SV.text(LX(t), 316, t, "sm", { "text-anchor": "middle" })));
  const pts = []; for (let t = 0; t <= s.n + 1e-9; t += 2) pts.push([LX(t), LY(LR(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  if (s.p > 0) o += SV.circle(LX(pk), LY(LR(pk)), 8, "dot3", op(s.p)) + SV.line(LX(pk), LY(LR(pk)), LX(pk), 300, "gr", op(s.p)) + tag(LX(pk), LY(LR(pk)) - 14, "revenue-maximising rate", "t3", s.p, "middle");
  if (s.c > 0) o += SV.circle(LX(75), LY(LR(75)), 8, "dot2", op(s.c)) + tag(LX(75) + 12, LY(LR(75)) - 10, "A: high rate", "t2", s.c) + SV.circle(LX(55), LY(LR(55)), 8, "dot4", op(s.c)) + tag(LX(55) + 12, LY(LR(55)) - 12, "B: after a cut", "t4", s.c) + arrow(LX(73), LY(LR(75)) - 4, LX(57), LY(LR(55)) - 8, "l", "c4", s.c);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Laffer curve with tax revenue against tax rate peaking at an optimum rate">${lafDraw({ n: 100, p: 1, c: 0 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 340, label: "Laffer curve showing revenue rising, peaking and falling as the tax rate rises", base: { n: 0, p: 0, c: 0 }, draw: lafDraw, tween: 1200, dwell: 5600, steps: [
  { cap: "<b>A zero tax rate</b> raises no revenue. As the rate rises from zero, revenue rises, because there is still a strong incentive to work and declare income.", s: { n: 30 } },
  { cap: "<b>The peak.</b> At some rate revenue is at its maximum. Beyond this point further increases cause people to work less, avoid or evade tax, or move abroad, so the gains from the higher rate are offset.", s: { n: 52, p: 1 } },
  { cap: "<b>Too high.</b> At very high rates revenue falls, and at 100% it would be close to zero because nobody would have a reason to declare income.", s: { n: 100, p: 1 } },
  { cap: "<b>Supply-side logic.</b> If the rate is already above the peak (A), <b>cutting</b> it to B raises effort and enterprise and could <b>raise revenue</b> and output. Below the peak a cut would lose revenue, so the position of the peak matters.", s: { n: 100, p: 1, c: 1 } },
] });

/* ---------- J curve ---------- */
const JX = (t) => 70 + t * 62, JY = (v) => 170 - v * 28;
const jc = (t) => -2 + 4 * (1 - Math.exp(-0.45 * t)) - 6 * Math.exp(-0.7 * t) * (1 - Math.exp(-3 * t));
function jDraw(s) {
  let o = SV.line(70, 170, 700, 170) + SV.line(70, 40, 70, 300) + SV.text(700, 190, "Time after depreciation (quarters)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Current account balance", "sm");
  o += SV.line(70, JY(-2), 700, JY(-2), "c3 dash") + tag(696, JY(-2) + 16, "balance before the depreciation", "t3", 1, "end");
  const pts = []; for (let t = 0; t <= s.n + 1e-9; t += 0.1) pts.push([JX(t), JY(jc(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2") + SV.circle(pts[pts.length - 1][0], pts[pts.length - 1][1], 6, "dot4");
  if (s.a > 0) o += tag(JX(1.3), JY(-5.2), "dearer imports, volumes slow to change", "t2", s.a, "start");
  if (s.b > 0) o += tag(JX(6.2), JY(-0.2), "volumes adjust: balance improves", "t1", s.b, "middle");
  return o;
}
Lib.stepper($("#stJ"), { w: 760, h: 330, label: "J curve: the current account worsens after a depreciation before it improves", base: { n: 0, a: 0, b: 0 }, draw: jDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>The starting point.</b> The country has a current account deficit and its government depreciates or devalues the currency to correct it.", s: { n: 0.05 } },
  { cap: "<b>Short run: it gets worse.</b> Import prices rise at once in domestic currency, while volumes of imports and exports are held by contracts and habit. The import bill rises faster than export revenue, so the deficit <b>widens</b>.", s: { n: 1.2, a: 1 } },
  { cap: "<b>Medium run: volumes adjust.</b> Buyers switch to cheaper home goods and foreigners buy more exports. The deficit narrows and passes its starting level, <b>if</b> the Marshall-Lerner condition holds.", s: { n: 4, a: 1, b: 0 } },
  { cap: "<b>Long run: improvement.</b> The current account settles at a better balance than before. The full pattern is a <b>J shape</b>. Evaluation: imported inflation and retaliation may reduce the gain.", s: { n: 9.9, a: 1, b: 1 } },
] });

/* ---------- Lab 1: Laffer ---------- */
function labLaf() {
  if (!$("#lt") || !$("#lk")) return;
  const t = +$("#lt").value, k = +$("#lk").value / 10, R = (x) => x * (100 - k * x) / 25, pk = 50 / k;
  $("#r1").textContent = Lib.fmtN(R(t), 0); $("#r2").textContent = Lib.fmtN(pk, 0) + "%"; const above = t > pk + 0.5;
  $("#r3").textContent = t > pk + 0.5 ? "raise revenue" : t < pk - 0.5 ? "cut revenue" : "leave revenue the same";
  $("#rv").textContent = above ? `The tax rate of ${t}% is above the revenue-maximising rate of ${Lib.fmtN(pk, 0)}%, so cutting the rate would raise revenue as well as work effort. This is the case for supply-side tax cuts.` : t < pk - 0.5 ? `The rate of ${t}% is below the peak of ${Lib.fmtN(pk, 0)}%, so a tax cut would reduce revenue. Raising the rate towards the peak would raise revenue, though it could harm incentives.` : "The rate is at the revenue-maximising point: changes in either direction reduce revenue.";
  const X = (x) => 40 + x * 3.5, Y = (v) => 270 - v / 110 * 230; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Tax rate (%)", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Revenue", "sm");
  const pts = []; for (let x = 0; x <= 100.01; x += 2) pts.push([X(x), Y(Math.max(0, R(x)))]); o += SV.path(Lib.ptsPath(pts), "c1");
  o += SV.circle(X(pk), Y(R(pk)), 7, "dot3") + tag(X(pk), Y(R(pk)) - 12, "peak", "t3", 1, "middle") + SV.circle(X(t), Y(Math.max(0, R(t))), 8, above ? "dot2" : "dot4") + SV.line(X(t), Y(Math.max(0, R(t))), X(t), 270, "gr");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "lt", label: "Tax rate (%) ", min: 0, max: 100, step: 5, value: 70, fmt: (v) => v, onInput: labLaf });
Lib.slider($("#g2"), { id: "lk", label: "Taxpayer responsiveness (higher = lower peak) ", min: 7, max: 15, step: 1, value: 10, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labLaf });
labLaf();
btnTable("lbBtns", "lbOut", [
  ["Expansionary fiscal policy", "Inflation: up near capacity", "Unemployment: down (cyclical)", "Growth: up short run", "Current account: worse (imports)", "Debt and crowding out; time lags"],
  ["Higher interest rates", "Inflation: down", "Unemployment: up", "Growth: down", "Current account: worse if the currency appreciates", "Lags 12 to 24 months; hurts borrowers"],
  ["Market-based supply-side policy", "Inflation: down long run", "Unemployment: natural rate down", "Growth: up long run", "Current account: better (competitiveness)", "Slow; may widen inequality"],
  ["Interventionist supply-side policy", "Inflation: down long run", "Unemployment: structural down", "Growth: up long run", "Current account: better", "Costly; may be badly targeted"],
  ["Devaluation / depreciation", "Inflation: up (imported)", "Unemployment: down (net exports)", "Growth: up if exports respond", "Current account: J curve, then better", "Marshall-Lerner; retaliation"],
  ["Tariffs and quotas", "Inflation: up (dearer imports)", "Unemployment: down in protected industries", "Growth: uncertain, efficiency falls", "Current account: better if no retaliation", "Retaliation; higher prices"]
], ["Policy", "Inflation", "Unemployment", "Growth", "Current account", "Main limit"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of policy is it?", ["Fiscal", "Monetary", "Supply-side (market-based)", "Supply-side (interventionist)", "Exchange rate / trade"],
  [("Cut the top rate of income tax", 0), ("Raise the central bank's interest rate", 1), ("Privatise a state industry", 2), ("Fund apprenticeships and training", 3), ("Devalue the currency", 4), ("Impose a tariff on imported steel", 4), ("Raise government spending on roads", 0), ("Quantitative easing", 1), ("Weaken union power", 2), ("Subsidise R&D", 3)],
  "Match each measure to its policy family.") + MATCH([
  ["Laffer curve", "Relationship between tax rates and tax revenue"],
  ["Expenditure-switching", "A policy that shifts spending from imports to domestic goods"],
  ["Expenditure-reducing", "A policy that cuts total spending and so imports"],
  ["Marshall-Lerner condition", "Depreciation improves the current account if PEDx + PEDm is greater than 1"],
  ["J curve", "The current account worsens before it improves after a depreciation"],
  ["Transmission mechanism", "The way interest rate changes reach spending and inflation"]]) + ORDER(
  "Put the effect of a depreciation on the current account in order.",
  ["The currency's value falls", "Exports become cheaper abroad and imports dearer at home", "Export volumes rise and import volumes fall over time", "Net exports and AD rise", "The current account improves, if elasticities are high enough"],
  "A depreciation works through relative prices.") + CALC([
  {"q": "A tariff of 15% is placed on imports of $200m. Calculate the tariff revenue ($m), assuming imports do not change.", "a": 30, "unit": "$m", "tol": 0.05, "hint": "15% of 200.", "sol": "0.15 × 200 = <b>$30m</b>."},
  {"q": "The price elasticity of demand for exports is 0.8 and for imports is 0.4. Does the Marshall-Lerner condition hold? Type 1 for yes and 0 for no.", "a": 1, "tol": 0.01, "hint": "Add the two elasticities and compare with 1.", "sol": "0.8 + 0.4 = 1.2, which is greater than 1, so the condition holds: <b>yes (1)</b>."},
  {"q": "A country's exports are priced at $100 each. Its currency depreciates by 10% against the dollar, and the foreign price of exports falls by the same amount. What is the new foreign price ($)?", "a": 90, "unit": "$", "tol": 0.05, "hint": "100 × 0.9.", "sol": "<b>$90</b>."},
  {"q": "Taxpayers earn $10,000m of taxable income and the average tax rate is 40%. The government raises the rate to 50% and taxable income falls to $7,600m. Calculate the change in tax revenue ($m).", "a": -200, "unit": "$m", "tol": 0.5, "hint": "Revenue before = 4,000. After = 50% × 7,600.", "sol": "Before: 4,000. After: 3,800. Change = <b>−$200m</b>, a Laffer-type effect."}]) + MCQ([
  ("Which policy is expenditure-switching?", ["A rise in income tax", "A rise in the interest rate", "A devaluation of the currency", "A cut in government spending"], 2, "A devaluation changes relative prices and switches spending to domestic goods."),
  ("The J curve describes:", ["Inflation rising then falling", "The current account worsening then improving after a depreciation", "Tax revenue rising then falling", "Unemployment falling then rising"], 1, "In the short run inelastic demand makes the deficit widen."),
  ("According to Laffer analysis, a cut in the tax rate raises revenue when:", ["The rate is below the revenue-maximising rate", "The rate is above the revenue-maximising rate", "Taxpayers do not respond to the rate", "Revenue is already zero"], 1, "Above the peak, a lower rate reduces avoidance and raises effort enough to raise revenue."),
  ("Which policy is best suited to long-run non-inflationary growth?", ["Higher interest rates", "Supply-side policy", "A depreciation", "Tariffs"], 1, "Supply-side policy raises capacity so that output can grow without inflation."),
  ("A major cost of imposing tariffs is that:", ["Trading partners may retaliate and consumers pay higher prices", "Imports rise", "Domestic competition increases", "The exchange rate always falls"], 0, "Retaliation and higher prices are the main costs.")
], "qz1") + CARDS([
  ("Fiscal policy", "Changes in government spending and taxes."),
  ("Monetary policy", "Interest rates, money supply, QE."),
  ("Supply-side policy", "Raises capacity: market-based or interventionist."),
  ("Laffer curve", "Tax revenue against tax rate; peaks at an optimum rate."),
  ("Expenditure-switching", "Moves spending from imports to home goods."),
  ("Marshall-Lerner", "PEDx + PEDm > 1 for a depreciation to help the current account."),
  ("J curve", "Current account worsens then improves."),
  ("Tariff", "Tax on imports.")]) + MCQ(mc_exam)

build("sy1031", "effectiveness-of-macro-policies", "Effectiveness of Policy Options to Meet Macroeconomic Objectives", EY,
  "10.3.1: how effective fiscal policy (with the Laffer curve), monetary policy, supply-side policy, exchange rate policy and trade policy are for each objective. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
