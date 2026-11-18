"""AS syllabus 5.4.4 Supply-side policy: AD/AS analysis and evaluation. Run: python3 tools/artifact-kit/mk_as55b.py"""
from as6k import *
EY = EYAS("5.4.4")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>On an AD/AS diagram a successful supply-side policy shifts <b>LRAS</b> (and usually <b>SRAS</b>) to the <b>right</b>, so <b>real output rises, the price level falls (or rises by less)</b> and employment increases, which is <b>long-run economic growth</b> with lower inflationary pressure. In the <b>short run</b>, however, much supply-side spending (on education, training, roads) is also <b>government spending</b>, so it raises <b>AD</b> first, which may raise prices before capacity improves. The policy is best suited to <b>structural unemployment</b>, <b>cost-push inflation</b> and <b>long-run growth</b>, and is less suited to <b>cyclical (demand-deficient) unemployment</b>, where AD is the problem. Evaluation points are <b>cost and opportunity cost</b>, <b>time lags</b>, <b>uncertainty</b>, <b>side effects</b> (inequality, damage to consumers or the environment) and whether <b>AD is high enough</b> to use the new capacity. A balanced answer compares supply-side policy with <b>fiscal and monetary</b> policy and often concludes that a <b>mix</b> works best.</p></div>

  <h2>1 · The effect on the AD/AS diagram</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>LRAS shifts right:</b> potential output rises, so the economy can grow without running into capacity limits.</li>
    <li><b>SRAS shifts right:</b> lower unit costs let firms supply more at each price level.</li>
    <li><b>Result:</b> real output up, price level down, unemployment (especially structural) down. Compare with demand-side policy, which raises output but also raises prices.</li>
    <li><b>Net effect on prices depends on AD:</b> if AD also rises, the price level may stay stable while output grows.</li>
  </ul>

  <h2>2 · Short run and long run</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Short run</th><th>Long run</th></tr>
    <tr><td><b>Effect on AD</b></td><td>Government spending on schools, roads and training raises AD</td><td>Little further effect</td></tr>
    <tr><td><b>Effect on AS</b></td><td>Small: capacity takes time to build</td><td>LRAS and SRAS shift right</td></tr>
    <tr><td><b>Output</b></td><td>Rises (from higher AD)</td><td>Rises further (capacity)</td></tr>
    <tr><td><b>Price level</b></td><td>May rise</td><td>Falls, or rises by less</td></tr>
  </table></div>

  <h2>3 · Which problems is it suited to?</h2>
  <div class="tw"><table class="t">
    <tr><th>Problem</th><th>How supply-side policy helps</th><th>How well?</th></tr>
    <tr><td><b>Structural unemployment</b></td><td>Retraining, mobility, information and incentives match workers to jobs</td><td>Well suited, but slow</td></tr>
    <tr><td><b>Cyclical (demand-deficient) unemployment</b></td><td>Little direct effect on AD, except through spending on projects</td><td>Poorly suited: demand-side policy needed</td></tr>
    <tr><td><b>Cost-push inflation</b></td><td>Lower unit costs and higher productivity shift SRAS right</td><td>Well suited in the long run</td></tr>
    <tr><td><b>Demand-pull inflation</b></td><td>Raises capacity so AD runs into fewer limits</td><td>Slow; contractionary policy acts faster</td></tr>
    <tr><td><b>Long-run growth</b></td><td>Raises potential output</td><td>Most suited: the only way to raise capacity</td></tr>
    <tr><td><b>Current account deficit</b></td><td>Raises competitiveness through lower costs and better quality</td><td>Slow; tackles the cause</td></tr>
  </table></div>

  <h2>4 · Evaluating supply-side policy</h2>
  <ul>
    <li><b>Time lags:</b> education and training take years to raise productivity; infrastructure takes years to build.</li>
    <li><b>Cost and opportunity cost:</b> the money could be spent elsewhere; large budget deficits may result, especially in countries with a small tax base.</li>
    <li><b>Uncertainty:</b> training may not match the skills employers want; workers may not respond; tax cuts may be saved or spent on imports rather than increasing work.</li>
    <li><b>Side effects:</b> tax cuts may widen inequality; deregulation may harm consumers or the environment; privatisation may create private monopolies; cutting benefits causes hardship.</li>
    <li><b>Demand also matters:</b> extra capacity is only used if AD is high enough; otherwise output stays below potential.</li>
    <li><b>Compare with alternatives:</b> fiscal and monetary policy act faster but cannot raise potential output; supply-side policy works over the long run. A <b>mix</b> of policies is usually most effective.</li>
    <li><b>Context:</b> in developing economies, funding is the main limit; inward investment and the private sector may help.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always separate the <b>short-run AD effect</b> from the <b>long-run supply effect</b>. Draw LRAS shifting right, say what happens to output and the price level, and then evaluate with <b>time lags, cost, uncertainty</b> and the <b>type of problem</b>. Conclude with a judgement, ideally a mix of policies.</div>
'''

watch = '''
  <h2>1 · A supply-side policy shifts LRAS and SRAS</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · The short-run demand effect and the long-run supply effect</h2>
  <div id="stS"></div>
  <h2>3 · Why supply-side policy may not cure cyclical unemployment</h2>
  <div id="stU"></div>
'''

explore = '''
  <h2>Lab 1 · Build a supply-side package</h2>
  <p>Increase spending on each tool. The long-run effect shifts LRAS to the right, with diminishing returns and a cost.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>LRAS shift</small><strong id="r1"></strong></div><div><small>Potential output</small><strong id="r2"></strong></div><div><small>Total cost</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with LRAS shifted by the supply-side package"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Which problem is it suited to?", "Choose a problem to see how well supply-side policy tackles it, and what else may be needed.", ["Supply-side response", "How well it works", "What else may be needed"]) + chooser_html("k", "Lab 3 · Evaluate the policy", "Choose an evaluation point to see how it limits supply-side policy.", ["Why it limits the policy", "Example", "How it may be reduced"])

practise = '''
  <h2>1 · Short-run demand effect or long-run supply effect?</h2><div id="cl1" class="card"></div>
  <h2>2 · Well suited or poorly suited?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the short run and long run in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Roads and training as a package", "A government funds new roads and training. At first, spending raises AD and may push up prices; later, better roads and skills lower firms' costs and raise capacity, shifting AS right and holding down prices.", "the short-run AD effect and long-run AS effect.") +
rw("Retraining after a factory closes", "Workers laid off in a declining industry have skills that no longer match vacancies. Retraining schemes help them move into growing sectors, reducing structural unemployment, but only after months or years.", "supply-side policy and structural unemployment.") +
rw("A recession with falling spending", "When unemployment is high because spending has collapsed, training alone cannot create jobs. Firms will not hire if they cannot sell, so demand-side policy is also needed.", "why supply-side policy suits structural, not cyclical, unemployment.") +
rw("Cost-push inflation and productivity", "Energy and wage costs rise, shifting SRAS left. Over the long run, investment in technology and training can raise productivity and reduce unit costs, easing the inflation.", "supply-side policy and cost-push inflation.") +
rw("A developing economy with little revenue", "A government wants to build schools and roads but has a small tax base. It may seek inward investment or aid, and phases spending, showing how funding limits supply-side policy.", "cost as a limit.")
)

mc_exam = [
  mcq("m25_12", 24, "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level?", ["Aggregate demand will also increase.", "Labour productivity levels will increase.", "Workers will save any extra wages they earn.", "Workers will spend any extra wages on imports."], 0, "Policies such as spending on training also raise AD, which offsets the downward effect of higher supply on prices."),
  mcq("m23_12", 26, "Under which current conditions will supply-side policy measures be most likely to achieve a country's key macroeconomic goals? (unemployment, price level)", ["high, stable", "high, rising", "low, stable", "low, rising"], 1, "Supply-side policy can reduce unemployment and ease price rises at the same time, so it is most useful when unemployment is high and prices are rising."),
  mcq("m21_12", 29, "Other things being equal, what is most likely to be reduced by falling labour productivity?", ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], 1, "Lower productivity raises unit costs and prices, so the internal value of money falls.")
]

exam = exam_page("supply-side policy: AD/AS analysis and evaluation",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Supply-side policy is a 12 mark Paper 2 discussion in most series (long-run growth, unemployment, inflation) and an 8 mark AD/AS explanation, with 6 mark data-response parts. Reworded past questions are below, with three Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2020 (23) Q4(a); May/June 2025 (24) Q4(a)"), ("Essay parts, 12 marks", "5", "Oct/Nov 2020 (23) Q4(b); May/June 2024 (22) Q4(b); Feb/March 2025 (22) Q5(b); Oct/Nov 2024 (22) Q4(b); Oct/Nov 2023 (23) Q4(b)"), ("Data response, 6 marks", "1", "May/June 2024 (21) Q1(e)"), ("Multiple choice (Paper 1)", "3 shown below", "2021 to 2025")],
  [
  eq(P("w20_23", "4(a)"), "8 marks", "A government embarks on a supply-side policy involving substantial additional funding for new road schemes and for new training schemes designed to raise labour productivity. Use an AD/AS diagram to explain the effects of this funding on the level of output in the economy.",
     ["Knowledge (up to 2): an accurate AD/AS diagram showing national output in equilibrium (2).",
      "Application (up to 6): a clear understanding of aggregate demand (1), with the diagram showing that the AD curve shifts right because of the increase in government spending (1) and that this increases national output (1); a clear understanding of aggregate supply (1), with the diagram showing that the AS curve shifts right because of the increase in productivity (1) and that this increases national output (1)."],
     "AD/AS diagram. Short run: spending shifts AD right, output up. Long run: productivity shifts AS right, output up again.",
     [[('k', 'On an AD/AS diagram with the price level on the vertical axis and real output on the horizontal axis, the economy is initially in equilibrium where the AD curve meets the SRAS curve, at price level P1 and output Y1. Aggregate demand is the total planned spending in the economy, and aggregate supply is the total output firms are willing and able to supply at each price level.')], [('n', 'Funding for new roads and training schemes is government spending, which is a component of AD. AD therefore shifts to the right, from AD1 to AD2, so national output rises in the short run, from Y1 to Y2, and the price level rises somewhat. Building roads also creates jobs and incomes for construction workers, and through the multiplier the increase in demand is larger than the initial spending.'), ('n', "Over the longer term, the supply effects appear. The training raises labour productivity, so workers produce more in the same time, and the roads lower firms' transport costs and make distribution quicker. Both raise the economy's productive capacity, so AS shifts to the right, from AS1 to AS2, and LRAS shifts right as well. Output rises again, to Y3, and the price level falls back, so output rises without inflation. The final level of output is higher than if only AD had increased, because the increase in capacity allows demand to be met without raising prices.")]]),
  eq(P("s25_24", "4(a)"), "8 marks", "Explain why expenditure on education and training is a supply-side policy and consider why its impact on the general price level may differ between the short run and the long run.",
     ["Knowledge (up to 3): supply-side policy consists of government policy tools designed to increase aggregate supply (1); the effect is to shift the aggregate supply curve to the right (1); government spending on education and training should increase worker skills and productivity and so productive capacity, shifting LRAS to the right (1).",
      "Analysis (up to 3): in the short run, increased government expenditure will increase AD, which may lead to an increase in the general price level (up to 2); in the long run, higher productivity and capacity shift LRAS right, which should lower the general price level (up to 2).",
      "Evaluation (up to 2): an overall assessment of the effect of expenditure on education and training on the price level, with a conclusion."],
     "Define supply-side policy; training raises productivity, LRAS right. Short run: spending raises AD, prices may rise. Long run: LRAS right, prices fall. Judge.",
     [[("k", "Supply-side policy consists of measures designed to increase aggregate supply and shift the AS curve to the right. Spending on education and training raises workers' skills and productivity, which increases productive capacity and shifts LRAS to the right.")], [("n", "In the short run the government spending is an injection that raises AD, so the price level may rise before any extra capacity appears. In the long run, higher productivity lowers unit costs and raises potential output, so the LRAS shift should lower the price level.")], [("e", "Overall the long-run effect on prices is likely to be downward, but the short-run effect could be inflationary if the economy is near full capacity. The net result depends on spare capacity and on how effective the training is.")]]),
  eq(P("w20_23", "4(b)"), "12 marks", "Discuss the extent to which a supply-side policy involving new road schemes and new training schemes will increase the rate of inflation in the economy.",
     ["Analysis (up to 8): the short-run effect: spending raises AD, which may raise prices if there is no spare capacity (up to 4); the long-run effect: higher productivity and capacity raise AS, which reduces inflationary pressure (up to 4).",
      "Evaluation (up to 4): a judgement on the extent to which the policy increases inflation, depending on spare capacity, time lags and the size of the AS effect, with a conclusion."],
     "Short run: AD up, inflation risk if at capacity. Long run: AS up, price level falls. Judge: depends on spare capacity and time lags.",
     [[('k', "Spending on new roads and training schemes is government spending, financed through taxation or borrowing, and is an example of supply-side policy because it aims to raise the economy's productive capacity.")], [('n', 'In the short run, the spending is an injection and raises AD, so the AD curve shifts to the right. Construction firms hire more workers, who spend their incomes, so the multiplier boosts demand further. If the economy has no spare capacity, the rise in AD mainly raises the price level, because firms cannot increase output enough to meet demand, so inflation could increase. Competition for scarce workers could also raise wages. Training schemes take workers out of employment while they learn, which could reduce labour supply at first.'), ('n', "In the long run, better roads reduce firms' transport costs and speed up deliveries, and a more productive workforce lowers unit labour costs and raises capacity. Both shift SRAS and LRAS to the right, so output rises and the price level is lower than it would otherwise have been. This reduces inflationary pressure, so over time the policy may help to hold down inflation.")], [('e', 'The extent to which the policy increases inflation depends on spare capacity: with high unemployment and unused resources the short-run increase in prices is small. It also depends on time lags, because if the capacity effects come quickly the inflation risk is short-lived, but if projects are delayed, the inflationary effect of the demand could last longer. The size of the spending relative to GDP, how it is financed, and the effectiveness of the training matter as well.'), ('e', 'Overall, the policy is likely to raise inflation slightly in the short run if the economy is near capacity, but it is unlikely to increase it much in the long run, since it raises AS, so the extent to which it increases inflation is likely to be limited and temporary.')]]),
  eq(P("s24_22", "4(b)"), "12 marks", "Assess whether supply-side policy is the most effective way to achieve long-run economic growth.",
     ["Analysis (up to 8): how supply-side policies, such as education, training, infrastructure and technology, raise productive capacity and shift LRAS right, giving sustainable growth (up to 4); the limits of supply-side policy (cost, time lags, uncertainty) and alternatives such as expansionary fiscal or monetary policy and their limits (up to 4).",
      "Evaluation (up to 4): a judgement on whether supply-side policy is the most effective way to achieve long-run growth, with a conclusion."],
     "Supply-side: LRAS shifts right, sustainable. Limits: lags, cost. Demand-side: raises growth only if spare capacity. Judge: best for long-run growth, with demand support.",
     [[('k', "Supply-side policies are government measures that aim to raise the economy's productive capacity, shifting the LRAS curve to the right. Long-run economic growth is an increase in the economy's potential output over time.")], [('n', "Supply-side policies such as spending on education and training raise labour productivity, investment in infrastructure and technology lowers costs and raises efficiency, and incentives for enterprise raise the amount of capital and innovation. These shift LRAS to the right, so the economy's potential output rises, and growth can occur without inflation, because capacity expands as demand increases. This type of growth is sustainable and raises living standards in the long run."), ('n', 'However, supply-side policies have limits. They take years to work, because skills and infrastructure take time to build, they cost money and may not be well targeted, and there is no guarantee that workers and firms will respond. Some policies, such as deregulation or lower taxes, may increase inequality or damage the environment.')], [('n', 'Alternatives include expansionary fiscal policy (higher government spending or lower taxes) and monetary policy (lower interest rates), which raise AD and can raise output in the short run when there is spare capacity. But without supply-side improvements, an increase in AD would eventually cause inflation as the economy reaches full capacity, and higher government borrowing could crowd out private investment, so they cannot achieve long-run growth alone.'), ('e', 'Supply-side policy is likely to be the most effective way to raise long-run growth, because it addresses the capacity of the economy, whereas demand policies affect only the short run. However, it works best in combination with stable demand, so the best strategy is a mix. Overall, supply-side policy is the most effective policy for long-run growth, provided that it is well designed and given enough time, but it is not the only requirement.')]]),
  eq(P("m25_22", "5(b)"), "12 marks", "Assess the extent to which supply-side policy is the best method to reduce the rate of inflation.",
     ["Analysis (up to 8): how supply-side policy reduces inflation by shifting AS to the right, lowering costs and the price level (up to 4); at least one alternative, such as contractionary monetary or fiscal policy, analysed, with the limits of each (up to 4).",
      "Evaluation (up to 4): a judgement depending on the cause of inflation, time lags and the costs of each policy, with a conclusion."],
     "Supply-side: lowers costs, price level falls, long run. Alternatives: monetary, fiscal: quicker but cut output. Judge by cause of inflation and time horizon.",
     [[('k', "Supply-side policies are government measures to raise the economy's productive capacity and efficiency, shifting aggregate supply to the right. Inflation is a sustained rise in the general price level.")], [('n', 'Supply-side policies such as spending on training, investment in technology and deregulation raise productivity and lower unit costs. As costs fall, firms are willing to supply more at each price level, so AS shifts to the right, and the price level falls, without reducing output, so they are particularly suited to cost-push inflation. They also raise capacity, so growth can occur without inflation, and they do not raise unemployment. However, they take years to work and are costly, so they cannot reduce inflation quickly.'), ('n', 'Contractionary monetary policy, with higher interest rates, reduces AD more quickly by raising the cost of borrowing and reducing consumption and investment, so it works well against demand-pull inflation. But it can reduce growth and raise unemployment, works with a lag of 12 to 18 months, and does little for cost-push inflation. Contractionary fiscal policy also reduces AD, but is politically unpopular, cuts output and jobs, and takes time to legislate.')], [('e', 'Supply-side policy is not the best method in every case. If inflation is caused by excess demand, monetary or fiscal policy is quicker and more suitable. If it is caused by costs, or if the aim is lasting low inflation, supply-side policy tackles the cause. The time available and the costs of each policy matter, since supply-side policy is slow.'), ('e', 'Overall, supply-side policy is likely to be the best method for lasting control of inflation caused by costs, but it is not the best way to reduce high inflation quickly, so it is best used together with monetary policy.')]]),
  eq(P("w24_22", "4(b)"), "12 marks", "Assess whether supply-side policy is likely to be equally successful in reducing both structural and cyclical unemployment.",
     ["Analysis (up to 8): the strengths and weaknesses of supply-side policy in solving both cyclical (demand-deficient) and structural unemployment: for example, investment in education, training and infrastructure can address structural problems, but supply-side policies are less successful against cyclical unemployment as they have less impact on AD, unless they involve a direct injection of government spending; other disadvantages include cost and the time taken to be effective. Analysing demand-side policies is acceptable.",
      "Evaluation (up to 4): a judgement on whether supply-side policy is equally successful for both, with a conclusion."],
     "Structural: retraining, mobility, information, works but slowly. Cyclical: AD is the problem, so supply-side is weak. Judge: not equally successful.",
     [[('k', "Structural unemployment is caused by a mismatch between the skills or location of workers and the jobs available, usually after a long-term change in the structure of the economy. Cyclical unemployment is caused by a lack of AD during a recession. Supply-side policies are measures to raise the economy's productive capacity and improve the working of markets.")], [('n', 'Supply-side policies are well suited to structural unemployment. Retraining and education give workers the skills that firms need, better information about vacancies and help with relocation allow them to move to available jobs, and investment in infrastructure in depressed areas can attract firms. These policies tackle the cause of the problem, so the reduction can be long-lasting. However, they work slowly, as retraining takes months or years, are costly, and depend on workers being willing to take part, and older workers may find it hard to retrain.'), ('n', 'Supply-side policies are much less successful against cyclical unemployment. This arises from a lack of AD, so there are too few jobs for the workers available. Raising skills or productivity does not create demand for labour, so workers who are retrained would still find no jobs. Some supply-side measures, such as lower taxes or infrastructure spending, may also raise AD, but any such effect is small. Expansionary fiscal or monetary policy, which raises AD, is more effective against cyclical unemployment.')], [('e', 'Supply-side policy is therefore not likely to be equally successful. It is likely to be much more successful for structural unemployment than for cyclical unemployment. The balance in a particular economy depends on the cause of unemployment: in a deep recession, cyclical unemployment dominates, whereas in a growing economy with changing industries, structural unemployment is more important.'), ('e', 'Overall, supply-side policy is only likely to be successful against structural unemployment, so a combination of demand-side and supply-side policies is needed to deal with both.')]]),
  eq(P("w23_23", "4(b)"), "12 marks", "Assess whether supply-side policy is the only way of reducing long-term unemployment in an economy.",
     ["Analysis (up to 8): what is meant by supply-side policy and how it can reduce long-term unemployment, for example by retraining and updating skills, providing information on job vacancies and encouraging business start-ups; the advantages (may be non-inflationary, long term) and disadvantages (a long time to have an effect, opportunity cost, receptiveness of the workforce, may not work depending on the type of unemployment); and the advantages and disadvantages of at least one alternative macroeconomic policy. Maximum Level 3 (lower) if only supply-side policy is analysed.",
      "Evaluation (up to 4): a judgement on whether supply-side policy is the only way of reducing long-term unemployment, with a conclusion."],
     "Supply-side: retraining, information, start-ups: non-inflationary but slow. Alternatives: fiscal and monetary raise AD. Judge: not the only way; depends on type of unemployment.",
     [[('k', 'Supply-side policy is the use of government measures to raise the productive capacity of the economy and improve the working of markets. Long-term unemployment means being out of work for a long period, usually more than a year.')], [('n', 'Supply-side policies may reduce long-term unemployment in several ways. Retraining and updating skills help workers whose old jobs have disappeared to meet the needs of employers. Providing better information on job vacancies helps matching, and encouraging business start-ups through grants and lower taxes can create new jobs. These policies tackle structural causes, may be non-inflationary, and have long-lasting effects. But they take a long time to have an effect, cost the government money, and rely on the unemployed taking part and employers being willing to hire them, and some of the long-term unemployed may face barriers such as age or health.'), ('n', 'Other policies can also help. Expansionary fiscal or monetary policy raises AD and creates jobs more quickly, particularly where unemployment is cyclical, because it increases the demand for labour. Changes to benefits, so that they are less generous or are conditional on job search, may reduce the time people spend unemployed. Government job creation schemes provide work directly.')], [('e', 'Supply-side policy is not the only way. If long-term unemployment is structural, supply-side measures are likely to be most effective, but if it results from a deep recession, demand management is needed. Its effectiveness also depends on the time available.'), ('e', 'Overall, supply-side policy is likely to be an important way of reducing long-term unemployment, but not the only way, and a combination with policies to raise AD is likely to work best.')]]),
  eq(P("s24_21", "1(e)"), "6 marks", "Assess the extent to which supply-side policies will be able to lead an economy back into economic growth.",
     ["Analysis (up to 4): possible benefits, such as a better trained, educated and healthier workforce that is more productive and an environment more suited to enterprise (up to 2); possible drawbacks, such as the cost of provision, the time lag and the receptiveness of the workforce (up to 2).",
      "Evaluation (up to 2): a full consideration of both benefits and drawbacks to reach a valid conclusion on the extent to which supply-side policies can lead the economy back into growth (1 mark reserved)."],
     "Benefits: productivity, skills, enterprise. Drawbacks: cost, lag, response. Judge: helps over time, not quickly.",
     [[('n', "Supply-side policies may help an economy return to growth. Spending on education, training and health care can create a better trained, educated and healthier workforce that is more productive, and investment in infrastructure and technology lowers firms' costs. Lower taxes, less regulation and support for start-ups create an environment more suited to enterprise, which raises investment and innovation. These policies raise the economy's productive potential, so the LRAS curve shifts right and growth can be sustained without inflation.")], [('n', 'However, there are drawbacks. The policies are costly, so they may raise government borrowing, and they take years to work, because skills and infrastructure take time to build. They depend on workers and firms responding: trained workers may not find jobs if demand is weak, and tax cuts may not raise investment if firms are pessimistic. In a recession, the problem may be a lack of demand rather than a lack of capacity.'), ('e', 'Supply-side policies can help to lead an economy back into growth in the longer term, but they are unlikely to do so quickly, and so may need to be used with policies to raise AD, such as lower interest rates, so the extent to which they lead the economy back to growth depends on the cause of the downturn.')]])
  ],
  )

tips = tips_html(
  [("Draw LRAS shifting right.", "Output up, price level down."),
   ("Separate short run from long run.", "Spending raises AD first; supply improves later."),
   ("Say which problem it suits.", "Structural unemployment, cost-push inflation, long-run growth."),
   ("Say which it does not suit.", "Cyclical unemployment: AD is the problem."),
   ("Evaluate.", "Time lags, cost, uncertainty, side effects."),
   ("Compare.", "Weigh against fiscal and monetary policy."),
   ("Conclude with a mix.", "Supply needs demand to be used.")],
  [("LRAS", "A supply-side policy shifts the LRAS curve to the right."),
   ("Time lag", "The effects of supply-side policy often take years to appear."),
   ("Structural unemployment", "Structural unemployment is caused by a mismatch of skills or location."),
   ("Cyclical unemployment", "Cyclical unemployment is caused by a lack of aggregate demand."),
   ("Evaluation", "It depends on spare capacity, cost and how well the policy is targeted.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"], CW["discuss"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
function slDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="LRAS and SRAS shifting right, raising output and lowering the price level">${slDraw({ a: 0, s: 15, l: 15, n: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifts right first, then supply shifts right">${slDraw({ a: 10, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "A supply-side policy shifts LRAS and SRAS to the right", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD and SRAS meet at output 50 and price level 50. Potential output (LRAS) is 75.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Supply-side policy.</b> Better training, infrastructure and technology raise productivity and capacity. SRAS and LRAS shift <b>right</b>.", s: { a: 0, s: 15, l: 15, n: 1 } },
  { cap: "<b>The result:</b> real output rises, the price level falls and employment rises. Potential output has increased: long-run economic growth.", s: { a: 0, s: 15, l: 15, n: 1 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 300, label: "The short-run demand effect and the long-run supply effect", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Short run.</b> The government spends on roads and training. This is government spending, so <b>AD shifts right</b> first: output rises but so may the price level.", s: { a: 10, s: 0, l: 0, n: 1 } },
  { cap: "<b>Long run.</b> As workers become more productive and transport improves, <b>SRAS and LRAS shift right</b>. Output rises further and the price level is held down.", s: { a: 10, s: 15, l: 15, n: 1 } },
] });
chainStep("#stU", "Why supply-side policy may not cure cyclical unemployment", ["Unemployment is high because spending has fallen (AD is weak)", "The government provides training to raise skills", "Workers are better qualified, but firms cannot sell more goods", "Firms do not hire, because demand has not risen", "Unemployment stays high: demand-side policy is needed as well"], [
  "<b>Cyclical unemployment:</b> the problem is a lack of demand.", "<b>A supply-side response:</b> improve skills.", "<b>Capacity is not the constraint</b>: sales are.", "<b>No extra jobs</b> without extra demand.", "<b>A mix of policies:</b> raise AD and improve the supply side."]);

function labP() {
  if (!["tr", "in", "rd", "dr"].every((i) => $("#" + i))) return;
  const [t, f, r, d] = ["tr", "in", "rd", "dr"].map((k) => +$("#" + k).value), raw = 0.5 * t + 0.4 * f + 0.5 * r + 0.3 * d, sh = Math.min(25, raw), cost = t + f + r + d * 0.5;
  $("#r1").textContent = Lib.fmtN(sh, 1) + " units right"; $("#r2").textContent = Lib.fmtN(75 + sh, 1); $("#r3").textContent = "$" + Lib.fmtN(cost, 0) + "bn";
  $("#rv").textContent = sh < 0.5 ? "No spending on the tools, so LRAS stays at 75." : `Spending of $${Lib.fmtN(cost, 0)}bn shifts LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(75 + sh, 1)}. The effect takes years and has diminishing returns (it is capped at 25). In the short run the spending also raises AD, so inflation could rise before capacity grows.`;
  $("#labA").innerHTML = adasPlot({ a: 0, s: sh * 0.6, l: sh, g: 1, n: 1 });
}
[["g1", "tr", "Education and training, $bn ", 10], ["g2", "in", "Infrastructure, $bn ", 10], ["g3", "rd", "Technology and R&D support, $bn ", 5], ["g4", "dr", "Deregulation and reforms (effort), index ", 10]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 30, step: 5, value: v, fmt: (z) => z, onInput: labP }));
labP();

chooser("h", [
  ["Structural unemployment", "Retraining, mobility, information", "Well suited, but slow", "Time and funding; some demand support", 4],
  ["Cyclical unemployment", "Little direct effect on AD", "Poorly suited", "Fiscal or monetary policy to raise AD", 1],
  ["Cost-push inflation", "Lower unit costs shift SRAS right", "Well suited in the long run", "Short-run measures for urgent cases", 4],
  ["Demand-pull inflation", "Raises capacity over time", "Slow", "Contractionary monetary or fiscal policy", 2],
  ["Low long-run growth", "Raises potential output (LRAS)", "Best suited", "Enough AD to use the capacity", 5],
  ["Current account deficit", "Improves competitiveness", "Slow but addresses the cause", "Exchange rate or expenditure-reducing policy for the short run", 3]
], (it) => `${it[0]}: supply-side policy ${it[1].toLowerCase()}. It is ${it[2].toLowerCase()}. What else may be needed: ${it[3].toLowerCase()}.`, "How well suited supply-side policy is");
chooser("k", [
  ["Time lags", "Capacity takes years to build", "Training and school reform take a generation to work", "Start early; target quick-acting measures", 5],
  ["Cost and opportunity cost", "Money spent here cannot be spent elsewhere", "A low-income country cannot afford large programmes", "Inward investment, private sector partnerships", 5],
  ["Uncertainty", "Results are not guaranteed", "Workers may not take part or skills may not match jobs", "Consult employers; target schemes", 4],
  ["Side effects", "Policies can harm some groups", "Tax cuts widen inequality; deregulation harms consumers", "Safeguards and targeted help", 3],
  ["Weak demand", "Extra capacity needs demand", "No hiring if firms cannot sell", "Combine with fiscal or monetary policy", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. Example: ${it[2].toLowerCase()}. It may be reduced by: ${it[3].toLowerCase()}.`, "How strongly it limits the policy");
''' + CLASSIFY("cl1", "Short-run demand effect or long-run supply effect?", ["Short-run demand effect", "Long-run supply effect"],
  [("Government spending on schools raises AD", 0), ("Workers' skills and productivity rise", 1), ("Construction of roads creates jobs and income", 0), ("Firms' unit costs fall", 1), ("The price level may rise at first", 0), ("LRAS shifts to the right", 1), ("Potential output increases", 1), ("Total spending in the economy rises", 0)],
  "In the short run, spending raises AD; in the long run, productivity and capacity raise AS.") + CLASSIFY("cl2", "Is supply-side policy well suited or poorly suited?", ["Well suited", "Poorly suited"],
  [("Structural unemployment", 0), ("Cyclical (demand-deficient) unemployment", 1), ("Cost-push inflation", 0), ("A sudden fall in spending", 1), ("Low long-run growth", 0), ("A short-term shortage of demand for exports", 1)],
  "Supply-side policy tackles capacity and structure; it does little when AD is the problem.") + ORDER(
  "Put the short-run and long-run effects of road and training spending in order.",
  ["The government spends on roads and training", "AD shifts right and output rises", "The price level may rise in the short run", "Productivity and capacity increase over time", "LRAS shifts right and the price level falls"],
  "AD first, then AS.") + MATCH([
  ["LRAS", "Potential output; shifted by supply-side policy"],
  ["Structural unemployment", "Unemployment from a mismatch of skills or location"],
  ["Cyclical unemployment", "Unemployment from a lack of aggregate demand"],
  ["Time lag", "Delay before supply improvements appear"],
  ["Cost-push inflation", "Inflation from rising costs of production"],
  ["Potential output", "The maximum sustainable output of the economy"]]) + CALC([
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "Actual output is 760. What is the output gap before the policy (potential minus actual)?", "a": 40, "unit": "", "tol": 0.5, "hint": "800 − 760.", "sol": "<b>40</b>."},
  {"q": "After the policy potential output is 840 and actual output is 800. What is the output gap now?", "a": 40, "unit": "", "tol": 0.5, "hint": "840 − 800.", "sol": "<b>40</b>: capacity has grown, but demand must also grow to use it."},
  {"q": "A government spends $20bn on training and AD rises by 1.5 times that amount in the short run. By how much does AD rise ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "20 × 1.5.", "sol": "<b>$30bn</b>."},
  {"q": "A firm's unit cost is $50 and falls 8% after a productivity gain. What is the new unit cost ($)?", "a": 46, "unit": "$", "tol": 0.1, "hint": "50 × 0.92.", "sol": "<b>$46</b>."}]) + MCQ([
  ("A successful supply-side policy shifts:", ["LRAS to the right", "AD to the right only", "LRAS to the left", "SRAS to the left"], 0, "More capacity."),
  ("In the short run, government spending on training:", ["Raises AD", "Lowers AD", "Raises LRAS immediately", "Has no effect"], 0, "Government spending is a component of AD."),
  ("Supply-side policy is best suited to:", ["Structural unemployment", "Cyclical unemployment", "A sudden fall in AD", "A trade surplus"], 0, "Skills and mobility."),
  ("A limit of supply-side policy is:", ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], 0, "Time lags."),
  ("Extra capacity is fully used only if:", ["AD is high enough", "Interest rates are zero", "Taxes rise", "Exports fall"], 0, "Demand must match capacity.")
], "qz1") + CARDS([
  ("Effect", "Output up, price level down."),
  ("Short run", "Spending raises AD."),
  ("Long run", "LRAS shifts right."),
  ("Suits", "Structural unemployment, cost-push, growth."),
  ("Poor for", "Cyclical unemployment."),
  ("Limits", "Lags, cost, uncertainty, side effects."),
  ("Needs", "Demand to use the capacity."),
  ("Evaluate", "Mix of policies.")]) + MCQ(mc_exam)

build("as55b", "as-supply-side-policy-effects", "Supply-Side Policy: Effects and Evaluation", EY,
  "5.4.4: the effects of supply-side policy in AD/AS analysis, the short-run and long-run effects, the problems it suits and how to evaluate it. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
