"""AS syllabus 5.4.1-5.4.3 Supply-side policy: meaning, objectives and tools. Run: python3 tools/artifact-kit/mk_as55.py"""
from as6k import *
EY = EYAS("5.4.1 to 5.4.3")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">Supply-side policy</b> consists of government measures designed to <b>increase aggregate supply</b> by raising the <b>quantity and quality of the factors of production</b> and the <b>efficiency</b> with which they are used, so that <b>potential output</b> (the LRAS curve) shifts to the right. Its objectives are to raise <b>productivity</b> and <b>productive capacity</b>, which supports <b>economic growth</b>, lowers <b>structural unemployment</b> and <b>inflationary pressure</b>, and improves <b>international competitiveness</b>. The tools fall into two broad groups: <b class="kw">interventionist</b> measures, in which the government spends to improve the supply side (education, training, health, infrastructure, support for research), and <b class="kw">market-based</b> measures, which aim to increase incentives and competition (lower taxes, deregulation, privatisation, labour market reform, free trade zones). Supply-side policy differs from <b>demand-side</b> policy (fiscal and monetary), which changes spending rather than capacity. Its effects are usually <b>long term</b>, <b>costly</b> and <b>uncertain</b>, and the effects on AD and AS are covered on the next page.</p></div>

  <h2>1 · Meaning and objectives</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Meaning:</b> policies that shift the <b>LRAS curve to the right</b> by raising the economy's productive capacity and productivity. They are also called <b>aggregate supply policies</b>.</li>
    <li><b>Productivity:</b> output per unit of input, such as output per worker.</li>
    <li><b>Productive capacity (potential output):</b> the maximum the economy can produce using all its resources efficiently.</li>
    <li><b>Objectives:</b> higher <b>long-run economic growth</b>; lower <b>structural and long-term unemployment</b>; lower <b>inflation</b> (costs fall, capacity rises); more <b>competitive</b> firms and a stronger <b>current account</b>; more enterprise and innovation.</li>
  </ul>

  <h2>2 · Supply-side policy or demand-side policy?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Supply-side</th><th>Demand-side (fiscal and monetary)</th></tr>
    <tr><td><b>Aim</b></td><td>Raise capacity and productivity</td><td>Change the level of total spending</td></tr>
    <tr><td><b>Main curve</b></td><td>LRAS (and SRAS) shifts</td><td>AD shifts</td></tr>
    <tr><td><b>Timescale</b></td><td>Long run</td><td>Short to medium run</td></tr>
    <tr><td><b>Examples</b></td><td>Training, infrastructure, deregulation</td><td>Interest rate changes, tax and spending changes</td></tr>
    <tr><td><b>Best for</b></td><td>Structural unemployment, cost-push inflation, long-run growth</td><td>Cyclical unemployment, demand-pull inflation, short-run stabilisation</td></tr>
  </table></div>
  <ul>
    <li><b>Be careful:</b> a tax cut can be demand-side if the aim is to boost spending, or supply-side if the aim is to raise incentives to work and invest. Say which aim you are discussing.</li>
  </ul>

  <h2>3 · Interventionist tools</h2>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>What the government does</th><th>How it raises supply</th><th>Drawbacks</th></tr>
    <tr><td><b>Education</b></td><td>Funds schools and universities</td><td>Higher quality of labour, more skilled, productive workers</td><td>Costly; years before payoff; may not match employers' needs</td></tr>
    <tr><td><b>Training and apprenticeships</b></td><td>Funds or subsidises training for workers</td><td>Reduces skill mismatch; raises occupational mobility</td><td>Workers may not take part; training may be poor quality</td></tr>
    <tr><td><b>Health care</b></td><td>Funds health services</td><td>Healthier workforce, fewer days lost, longer working lives</td><td>High opportunity cost</td></tr>
    <tr><td><b>Infrastructure</b></td><td>Builds roads, ports, rail, broadband</td><td>Lowers firms' costs and raises capital productivity; opens markets</td><td>Large cost; long delay; may raise the deficit</td></tr>
    <tr><td><b>Research and technology</b></td><td>Grants, tax relief for R&amp;D, support for innovation</td><td>Faster innovation and better capital</td><td>Uncertain results; firms may not use the support well</td></tr>
    <tr><td><b>Information and job matching</b></td><td>Job centres and vacancy information</td><td>Reduces frictional unemployment</td><td>Limited effect on structural problems</td></tr>
    <tr><td><b>Start-up support</b></td><td>Grants, advice, loans for new firms</td><td>More and better enterprise</td><td>Firms may depend on support or fail</td></tr>
  </table></div>

  <h2>4 · Market-based tools</h2>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>What the government does</th><th>How it raises supply</th><th>Drawbacks</th></tr>
    <tr><td><b>Lower income tax</b></td><td>Cuts rates on earnings</td><td>Raises the reward for working, so more people work and work harder</td><td>Revenue falls; may widen inequality; may not change behaviour</td></tr>
    <tr><td><b>Lower business taxes</b></td><td>Cuts corporation tax or gives investment allowances</td><td>More money for investment and more incentive to start firms</td><td>Revenue falls; the benefit may go to profits or shareholders</td></tr>
    <tr><td><b>Reduced benefits</b></td><td>Limits unemployment benefits or their duration</td><td>Increases the incentive to look for work</td><td>Hardship; may not create jobs</td></tr>
    <tr><td><b>Deregulation</b></td><td>Removes rules and red tape; reduces barriers to entry</td><td>More competition and lower costs</td><td>Weaker consumer, worker or environmental protection</td></tr>
    <tr><td><b>Privatisation</b></td><td>Sells state-owned firms to private owners</td><td>Profit motive and competition cut costs and raise efficiency</td><td>May create private monopolies; loss of public service goals</td></tr>
    <tr><td><b>Labour market reform</b></td><td>Reduces trade union power; makes hiring and firing easier</td><td>More flexible labour; fewer disputes</td><td>Less job security; lower wages for some</td></tr>
    <tr><td><b>Free trade zones</b></td><td>Tax incentives and fewer controls in a defined area</td><td>Attract investment, lower costs and remove bureaucracy</td><td>May simply move activity rather than create it</td></tr>
  </table></div>

  <h2>5 · Which factor of production is affected?</h2>
  <ul>
    <li><b>Labour:</b> quantity (tax and benefit incentives, immigration policy, retirement age) and quality (education, training, health).</li>
    <li><b>Capital:</b> infrastructure, investment allowances, research support, technology.</li>
    <li><b>Enterprise:</b> lower business taxes, start-up grants, deregulation, training in management skills.</li>
    <li><b>Land and natural resources:</b> planning and property rules, environmental policy, resource management.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For each tool, explain <b>how</b> it raises productivity or capacity (which factor, and why), classify it as <b>market-based</b> or <b>interventionist</b>, and give one <b>limitation</b>. Say whether a tax cut is meant to raise incentives (supply-side) or spending (demand-side).</div>
'''

watch = '''
  <h2>1 · Training raises potential output</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Deregulation and competition</h2>
  <div id="stB"></div>
  <h2>3 · A tax cut as a supply-side incentive</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Is training worth the money?</h2>
  <p>A training programme costs money now but raises output for many years. Choose the cost, the yearly gain and the delay before the gains start.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Payback (years of gains)</small><strong id="r1"></strong></div><div><small>Net gain after 10 years</small><strong id="r2"></strong></div><div><small>First year with a net gain</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 220" role="img" aria-label="Cumulative cost and gain of the training programme over ten years"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Choose a tool", "Choose a supply-side tool to see its type, the factor it affects and its main drawback.", ["Type and factor", "How it raises supply", "Main drawback"]) + chooser_html("k", "Lab 3 · Supply-side or demand-side?", "Choose a policy to see whether its aim is on the supply side or the demand side.", ["Classification", "Aim", "Curve that shifts"])

practise = '''
  <h2>1 · Market-based or interventionist?</h2><div id="cl1" class="card"></div>
  <h2>2 · Supply-side or demand-side?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the long-run effect of training in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Apprenticeships and training", "A government funds training programmes so workers gain skills that employers need. Productivity rises and structural unemployment falls, shifting LRAS right, but the benefits take years to appear.", "human capital as a supply-side tool.") +
rw("Broadband and transport links", "New rail and fibre networks lower firms' costs and open new markets. Capital spending adds to AD at once and to productive capacity over the long run.", "infrastructure raising AS.") +
rw("Cutting red tape", "Simplifying the rules for starting a business makes it quicker and cheaper to set up firms, encouraging enterprise and competition. But less regulation might reduce consumer protection or environmental standards.", "deregulation and its drawbacks.") +
rw("Privatisation", "Selling a state-owned industry to private owners gives managers a profit motive and exposes the industry to competition, which may cut costs. It can also create a private monopoly that raises prices.", "market-based supply-side policy and its risks.") +
rw("Free trade zones", "A region offers firms tax incentives and fewer controls to attract investment. Costs fall and bureaucracy is reduced, but some activity may just move from elsewhere in the country.", "free trade zones as a supply-side policy.") +
rw("Tax cuts to encourage work", "A government cuts the income tax rate on earnings to make work more rewarding. More people may enter the labour force, but if they simply spend the extra income the effect is on demand rather than supply.", "the incentive effect and its limits.")
)

mc_exam = [
  mcq("m24_12", 23, "What can be considered an expansionary supply-side policy?", ["an increase in government expenditure on training", "an increase in sales tax", "an increase in the rate of interest", "an increase of the exchange rate"], 0, "Training raises productivity and capacity, shifting aggregate supply right."),
  mcq("s25_11", 24, "What is not an example of an expansionary supply-side policy?", ["a reduction in government spending on training", "an increase in support for technological improvement", "a reduction in payments to the unemployed", "an increase in privatisation of industry"], 0, "Cutting training would reduce skills. The others aim to raise supply."),
  mcq("m25_12", 21, "A government cuts income tax. Why might this be seen as an example of a supply-side policy?", ["Real incomes are increased", "The costs of businesses are reduced", "The opportunity cost of unemployment has increased", "The standard of living has improved"], 2, "Lower income tax raises the reward for working, so the opportunity cost of not working rises, encouraging people into work."),
  mcq("s20_13", 14, "What is most likely to occur when the government privatises public sector organisations?", ["Consumer choice will increase", "Employment will increase in the short run", "Innovation will be discouraged", "The production of public goods will increase"], 0, "Privatisation usually increases competition and choice."),
  mcq("m20_12", 14, "Which argument has often been used to justify the privatisation of state enterprises?", ["Private firms can produce the same outputs using fewer inputs.", "Private firms try to earn large profits.", "State enterprises are always monopolies which exploit consumers.", "State enterprises cannot operate without government subsidies."], 0, "The efficiency argument: the profit motive and competition reduce costs."),
  mcq("s21_13", 28, "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target? (main aim, policy measure)", ["economic growth, deregulation", "full employment, increasing the money supply", "income equality, more progressive taxation", "stable prices, decreasing interest rates"], 0, "Deregulation is a supply-side measure aimed at growth. The others are demand-side or distribution policies."),
  mcq("s25_12", 4, "A country increases its spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect of these changes on human capital and physical capital?", ["human capital decreases, physical capital decreases", "human capital decreases, physical capital increases", "human capital increases, physical capital decreases", "human capital increases, physical capital increases"], 2, "Education and training raise human capital. Taxes on imported machinery make capital goods dearer, so physical capital is likely to fall."),
  mcq("s20_11", 16, "What would supporters of a nationalised public transport service expect to be the most likely outcome from the privatisation of train and bus services?", ["fewer destinations served by trains and buses", "lower fares", "more frequent services to all destinations", "more people employed in public transport services"], 0, "Supporters of nationalisation would expect private firms to drop unprofitable routes.")
]

exam = exam_page("supply-side policy: meaning, objectives and tools",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The tools of supply-side policy appear in short data-response parts and in 12 mark Paper 2 questions about enterprise, labour and the difficulties of adopting these policies. Reworded past questions are below, with eight Paper 1 multiple choice questions that do not need a diagram.",
  [("Data response, 2 to 3 marks", "2", "Oct/Nov 2021 (22) Q1(c); May/June 2020 (21) Q1(d)(i)"), ("Essay parts, 12 marks", "3", "Oct/Nov 2022 (21) Q3(b); Feb/March 2021 (22) Q2(b); Oct/Nov 2022 (22) Q3(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("w21_22", "1(c)"), "3 marks", "Identify one policy that could be considered a supply-side measure and explain how this policy could make a country's businesses more competitive.",
     ["Identification of a valid supply-side measure that could make businesses more competitive (1 mark), for example cutting business taxes, cutting income taxes or improving infrastructure; it must be explained as a supply-side tool, not as a demand-side one.",
      "An explanation of how this makes businesses more competitive (up to 2 marks), the third mark referring specifically to being more competitive: for example, reducing business taxes (1) gives more money to invest in new technology (1), which improves quality or allows lower prices, making the business more competitive (1)."],
     "Policy, then how: lower business tax, more investment, better quality or lower prices, more competitive.",
     [[("k", "One supply-side policy is a cut in business taxes."), ("n", "Firms keep more of their profits, so they have more money to invest in new technology. This raises the quality of their goods and can allow them to cut prices, which makes them more competitive against foreign rivals.")]]),
  eq(P("s20_21", "1(d)(i)"), "2 marks", "Explain why 'free trade zones' can be considered a supply-side policy.",
     ["Up to 2 marks for an explanation of free trade zones as a supply-side policy: for example, generous tax incentives leave firms with more funds to finance development and expansion; they help to lower costs, remove bureaucracy and make the economy more flexible and efficient; and they promote the role of the private sector in raising productivity."],
     "Tax incentives, lower costs, less red tape: raises productivity and capacity.",
     [[("n", "Free trade zones give firms tax incentives and fewer controls, which lowers their costs and removes bureaucracy. This encourages investment and raises productivity and productive capacity, so they are a supply-side policy.")]]),
  eq(P("w22_21", "3(b)"), "12 marks", "Discuss whether supply-side policies will be successful in increasing the quantity and quality of the factor enterprise in a modern economy.",
     ["Analysis (up to 8): the potential advantages of supply-side policies in increasing the quantity and quality of enterprise (up to 4), such as lower taxes encouraging entrepreneurs, expenditure on education and training improving quality, deregulation making it easier to set up, and financial support so that firms survive; and the potential limitations (up to 4), such as long delays, dependence on government support and no guarantee of success.",
      "Evaluation (up to 4): a judgement on whether the policies will be successful, with a conclusion (1 mark reserved)."],
     "Tax cuts, training, deregulation, start-up support raise enterprise. Limits: slow, dependence, no guarantee. Judge: partly successful.",
     [[("n", "Lower taxes on profits raise the reward for taking risks, so more people may become entrepreneurs, and training in management and innovation could improve their quality. Deregulation makes it easier and cheaper to set up a business, and financial support helps new firms survive. But the effects take a long time, some entrepreneurs may become dependent on government support and inefficient, and policies cannot guarantee that firms will succeed.")], [("e", "Supply-side policies are likely to be partly successful, since they improve the environment for enterprise, but the outcome depends on culture, access to finance and the state of demand. They are more likely to increase the quantity than guarantee the quality.")]]),
  eq(P("m21_22", "2(b)"), "12 marks", "Discuss the view that supply-side policies to increase the supply of labour to an economy are likely to be more successful than those designed to increase the supply of entrepreneurship.",
     ["Analysis (up to 8): at least two supply-side measures designed to increase the supply of labour (up to 4; a maximum of 3 if only one), and at least two designed to increase the supply of entrepreneurship, such as training in management skills, lower business taxes, subsidies and start-up grants (up to 4; a maximum of 3 if only one).",
      "Evaluation (up to 4): evaluative comment on which policies are likely to be successful (up to 3), leading to a reasoned conclusion (1)."],
     "Labour: tax and benefit incentives, training. Enterprise: start-up grants, lower business tax, training. Judge which is more likely to succeed and why.",
     [[("n", "Policies to increase the supply of labour include cutting income tax and benefits to raise the reward for work, and training to raise skills, which can have a fairly direct effect on the labour force. Policies for entrepreneurship include start-up grants, lower business taxes and training in management skills, but success depends on attitudes to risk, access to finance and market conditions, which policy cannot easily change.")], [("e", "Labour supply policies are probably more reliably successful because incentives and training affect a large number of people directly, while entrepreneurship is harder to influence. But enterprise policies could have a bigger effect on growth if they succeed, so the answer depends on the economy.")]]),
  eq(P("w22_22", "3(b)"), "12 marks", "Discuss the difficulties that might be encountered when adopting supply-side policies to expand the productive capacity of an economy and consider whether these difficulties can be overcome.",
     ["Analysis (up to 8): how supply-side policies may expand productive capacity and the difficulties of adopting them (up to 4; a maximum of 3 if only one policy and one difficulty are discussed), such as cost and the long time before they take effect; possible methods of overcoming these difficulties (up to 4; a maximum of 3 if only one method is discussed), for example inward investment where funds are short in developing economies.",
      "Evaluation (up to 4): the likely success of adopting supply-side policies, taking into account the difficulties (up to 3), with a reasoned conclusion (1)."],
     "Difficulties: cost, time lags, uncertainty, resistance. Overcoming: inward investment, private sector, phasing, targeting. Judge.",
     [[("n", "Supply-side policies such as spending on education and infrastructure expand capacity, but they are costly, which is a major problem for countries with limited tax revenue, and they take many years to work. Workers may not respond to training, and some policies, such as privatisation, can face political opposition. Costs may be overcome by inward investment from abroad, partnerships with private firms or phasing spending over time, and delays by targeting the policies where they have the biggest effect.")], [("e", "The difficulties can be partly overcome, but not fully, since long time lags are unavoidable. Success is likely to depend on the country's resources and on how well the policies are chosen and managed.")]])
  ],
  )

tips = tips_html(
  [("Define it.", "Policies to increase aggregate supply, shifting LRAS right."),
   ("Name the tool and the factor.", "Which factor of production, and why productivity rises."),
   ("Classify.", "Market-based or interventionist."),
   ("Say the aim of a tax cut.", "Incentive (supply-side) or spending (demand-side)."),
   ("Give a limitation for each.", "Cost, time, uncertainty, side effects."),
   ("Link to objectives.", "Growth, structural unemployment, inflation, competitiveness."),
   ("Be specific.", "Name the policy and say how it works.")],
  [("Supply-side policy", "Supply-side policy is designed to increase aggregate supply and shift LRAS to the right."),
   ("Productivity", "Productivity is output per unit of input."),
   ("Productive capacity", "Productive capacity is the maximum output an economy can produce."),
   ("Deregulation", "Deregulation is the removal of rules to increase competition and efficiency."),
   ("Privatisation", "Privatisation is the transfer of state-owned firms to private ownership."),
   ("Human capital", "Human capital is the skills and knowledge of the workforce.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Interventionist", "Government spends: education, training, infrastructure, research", 30, "f1"], ["Market-based", "Incentives and competition: tax cuts, deregulation, privatisation", 270, "f2"], ["Result", "Productivity and capacity rise: LRAS shifts right", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 110, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 52, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }); d.split(": ").forEach((p, i) => { o += SV.text(x + 110, 80 + i * 20, i === 0 ? p + ":" : p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 150" role="img" aria-label="Interventionist and market-based tools both raise productivity and capacity">${o}</svg>`;
})();
chainStep("#stA", "Government spending on training", ["The government funds training and apprenticeships", "Workers gain skills that employers need", "Labour productivity rises and structural unemployment falls", "Unit costs fall and potential output rises", "LRAS shifts to the right: long-run growth"], [
  "<b>Interventionist policy:</b> the state pays for training.", "<b>Human capital</b> improves: the quality of labour rises.", "<b>More output per worker</b> and a better match of skills and jobs.", "<b>Firms can produce more</b> at lower cost.", "<b>Potential output grows</b>, but only after years of delay."]);
chainStep("#stB", "Deregulation and competition", ["The government removes barriers to entry and red tape", "More firms can enter the market", "Competition increases", "Firms cut costs and innovate to survive", "Efficiency and capacity rise; prices may fall"], [
  "<b>Market-based policy</b> that reduces the role of rules.", "<b>Entry</b> becomes cheaper and easier.", "<b>Rivals</b> compete for customers.", "<b>Efficiency</b> rises under pressure.", "<b>The risk:</b> weaker consumer, worker or environmental protection."]);
chainStep("#stC", "A tax cut as a supply-side incentive", ["Income tax rates on earnings are cut", "The reward for working rises; the opportunity cost of leisure rises", "More people join the labour force and some work longer hours", "The quantity of labour supplied rises", "Potential output rises, if jobs are available"], [
  "<b>Supply-side aim:</b> incentives, not spending.", "<b>Incentive effect</b> on work effort.", "<b>Participation</b> and hours increase.", "<b>The labour supply</b> grows.", "<b>The limit:</b> people may simply spend the extra income (a demand effect), and jobs must exist."]);

function labT() {
  if (!["cs", "gn", "dl"].every((i) => $("#" + i))) return;
  const cost = +$("#cs").value, gain = +$("#gn").value, dl = +$("#dl").value; let cum = -cost, first = null, rows = [];
  for (let y = 1; y <= 10; y++) { if (y > dl) cum += gain; rows.push(cum); if (cum >= 0 && first === null) first = y; }
  $("#r1").textContent = Lib.fmtN(cost / gain, 1) + " years"; $("#r2").textContent = (cum >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(cum), 0) + "m"; $("#r3").textContent = first === null ? "None in 10 years" : "Year " + first;
  $("#rv").textContent = `The programme costs $${cost}m now and raises output by $${gain}m a year, starting after a delay of ${dl} years. It takes ${Lib.fmtN(cost / gain, 1)} years of gains to repay the cost, so the first net gain is ${first === null ? "beyond year 10" : "in year " + first}. After 10 years the net result is ${cum >= 0 ? "+" : "−"}$${Lib.fmtN(Math.abs(cum), 0)}m. A longer delay or lower gain makes supply-side spending harder to justify.`;
  const mx = Math.max(cost, Math.abs(Math.min(...rows)), Math.max(...rows), 1), Y = (v) => 110 - (v / mx) * 85; let o = SV.line(30, Y(0), 400, Y(0));
  rows.forEach((v, i) => (o += SV.rect(40 + i * 35, v >= 0 ? Y(v) : Y(0), 26, Math.max(2, Math.abs(Y(v) - Y(0))), v >= 0 ? "f2" : "f3", op(0.7))));
  o += SV.text(30, 205, "Cumulative net gain by year (1 to 10)", "sm"); $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "cs", label: "Cost of the programme, $m ", min: 20, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "gn", label: "Yearly gain once it works, $m ", min: 5, max: 60, step: 5, value: 25, fmt: (v) => v, onInput: labT });
Lib.slider($("#g3"), { id: "dl", label: "Delay before gains start, years ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: labT });
labT();

chooser("h", [
  ["Education and training", "Interventionist; labour (quality)", "Raises skills and productivity", "Costly; years before payoff; skills may not match", 5],
  ["Infrastructure", "Interventionist; capital", "Lowers costs and opens markets", "High cost; long delay; raises the deficit", 4],
  ["Research and technology support", "Interventionist; capital and enterprise", "Faster innovation", "Uncertain returns", 3],
  ["Lower income tax", "Market-based; labour (quantity)", "Raises the reward for work", "Revenue falls; may widen inequality", 3],
  ["Deregulation", "Market-based; enterprise", "More competition and lower costs", "Weaker consumer or environmental protection", 4],
  ["Privatisation", "Market-based; capital and enterprise", "Profit motive and competition cut costs", "Possible private monopoly power", 4],
  ["Reduced benefits for the long-term unemployed", "Market-based; labour (quantity)", "Encourages people to look for work", "Hardship; may not create jobs", 2],
  ["Free trade zones", "Market-based; capital and enterprise", "Attract investment and cut bureaucracy", "May only move activity around", 3]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. It raises supply by ${it[2].toLowerCase()}. The main drawback is that it ${it[3].toLowerCase()}.`, "Long-run effect on capacity");
chooser("k", [
  ["Funding apprenticeships", "Supply-side", "Raise skills and productivity", "LRAS and SRAS", 5],
  ["Cutting the interest rate to boost spending", "Demand-side", "Raise total spending", "AD", 1],
  ["A tax cut to raise work incentives", "Supply-side", "Raise labour supply", "LRAS", 4],
  ["A tax cut to boost spending in a recession", "Demand-side", "Raise consumption", "AD", 1],
  ["Building new railways to cut firms' costs", "Supply-side (also boosts AD in the short run)", "Raise productive capacity", "LRAS (and AD at first)", 4],
  ["Raising benefits to support spending", "Demand-side", "Raise consumption", "AD", 1]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. Its aim is to ${it[2].toLowerCase()}, so the curve that shifts is ${it[3]}.`, "How supply-side the policy is (5 = fully)");
''' + CLASSIFY("cl1", "Market-based or interventionist?", ["Market-based", "Interventionist"],
  [("Cutting income tax rates", 0), ("Government funding for apprenticeships", 1), ("Privatising a state-owned railway", 0), ("Building a new port", 1), ("Removing barriers to entry for new firms", 0), ("Grants for research and development", 1), ("Making it easier to hire and fire workers", 0), ("Funding health services", 1)],
  "Market-based measures change incentives and competition; interventionist measures involve the government spending to improve the supply side.") + CLASSIFY("cl2", "Supply-side or demand-side?", ["Supply-side", "Demand-side"],
  [("Funding apprenticeships", 0), ("Cutting interest rates", 1), ("Building new ports", 0), ("A cut in VAT to boost spending", 1), ("Tax relief for R&D", 0), ("Deregulating industries", 0), ("Higher government spending on benefits", 1), ("Privatising state industries", 0)],
  "Supply-side policies raise capacity and productivity; demand-side policies change spending.") + ORDER(
  "Put the long-run effect of training in order.",
  ["The government funds training", "Workers' skills and productivity rise", "Unit costs fall and capacity rises", "LRAS shifts to the right", "Real output rises and the price level falls"],
  "Training raises productivity, shifting LRAS right.") + MATCH([
  ["Supply-side policy", "Measures to increase aggregate supply"],
  ["Productivity", "Output per unit of input"],
  ["Human capital", "Skills and knowledge of the workforce"],
  ["Deregulation", "Removing rules to increase competition and efficiency"],
  ["Privatisation", "Transferring state industries to private ownership"],
  ["Productive capacity", "The maximum output the economy can produce"]]) + CALC([
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "A training programme costs $30m and raises output per worker by $200 for 100,000 workers. What is the extra output ($m)?", "a": 20, "unit": "$m", "tol": 0.1, "hint": "200 × 100,000.", "sol": "<b>$20m</b> a year."},
  {"q": "How many years does it take for the extra output to cover the cost?", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5 years</b>."},
  {"q": "A worker produces 40 units a day and productivity rises 15%. How many units a day now?", "a": 46, "unit": "units", "tol": 0.1, "hint": "40 × 1.15.", "sol": "<b>46 units</b>."},
  {"q": "A firm's labour costs are 50% of its costs. Productivity rises 10%, so labour cost per unit falls 9.1%. By roughly how much do total unit costs fall (%)?", "a": 4.5, "unit": "%", "tol": 0.2, "hint": "0.5 × 9.1.", "sol": "<b>4.5%</b>."}]) + MCQ([
  ("A supply-side policy aims to:", ["Increase aggregate supply", "Reduce aggregate supply", "Raise interest rates", "Cut government spending only"], 0, "Raise capacity."),
  ("Which is a supply-side policy?", ["Spending on education and training", "A cut in interest rates", "A rise in VAT", "A rise in the money supply"], 0, "Human capital."),
  ("Privatisation is:", ["A market-based supply-side policy", "A demand-side policy", "An interventionist policy", "A tax"], 0, "It aims to raise efficiency."),
  ("A limit of supply-side policy is:", ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], 0, "Time lags."),
  ("A tax cut is supply-side if its aim is to:", ["Raise incentives to work and invest", "Boost spending in a recession", "Reduce the budget deficit", "Raise import demand"], 0, "Incentive effect.")
], "qz1") + CARDS([
  ("Supply-side", "Raise AS and LRAS."),
  ("Interventionist", "Government spends: training, infrastructure."),
  ("Market-based", "Incentives and competition."),
  ("Productivity", "Output per unit of input."),
  ("Deregulation", "Remove rules, raise competition."),
  ("Privatisation", "Sell state firms."),
  ("Limits", "Cost, time lags, uncertainty."),
  ("Demand-side", "Changes spending, not capacity.")]) + MCQ(mc_exam)

build("as55", "as-supply-side-policy", "Supply-Side Policy: Meaning, Objectives and Tools", EY,
  "5.4.1 to 5.4.3: what supply-side policy is, its objectives, and the interventionist and market-based tools. Animated chains, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
