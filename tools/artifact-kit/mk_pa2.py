"""A Level exam technique: AO2 analysis for Paper 3 and Paper 4. Run: python3 tools/artifact-kit/mk_pa2.py"""
from pa_common import *

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">AO2 is analysis</b>: examining economic issues and relationships using relevant concepts, theories and information; selecting, interpreting and organising economic information in written, numerical and diagrammatic form; using information to recognise patterns, relationships, causes and effects; and <b>explaining the impacts and consequences</b> of changes in economic variables. It is 40% of the A Level, 40% of Paper 3 and <b>37% of Paper 4</b>. In a Paper 4 essay it is marked with AO1 on the 14-mark Table A scale, and Level 3 asks for <b>developed, detailed analysis</b> using accurate concepts and diagrams that are fully explained, in a logical, well-organised answer. In practice analysis is a <b>chain</b>: each step is followed by "because" or "so", and the chain ends at the objective the question names. This page shows what separates a statement from a one-step comment from a developed chain.</p></div>

  <h2>1 · Where AO2 marks are</h2>
  <div class="tw"><table class="t">
    <tr><th>Where</th><th>What AO2 looks like</th></tr>
    <tr><td><b>Paper 3</b> (30 marks)</td><td>Working through a calculation or a cause-and-effect chain in the stem to pick the one correct consequence.</td></tr>
    <tr><td><b>Paper 4 Section A</b>, "explain" and "analyse" parts</td><td>Steps in a chain (one mark per step, with development worth up to two marks) and diagram marks.</td></tr>
    <tr><td><b>Paper 4 Section A</b>, data parts</td><td>Selecting and interpreting figures, calculating, and spotting patterns, causes and effects.</td></tr>
    <tr><td><b>Paper 4 essay</b> (20 marks)</td><td>The bulk of the 14-mark Table A scale, together with AO1. Three developed, applied chains is the target.</td></tr>
  </table></div>

  <h2>2 · The three levels of Table A for analysis</h2>
  <p class="note">In our words, from the pattern of the Paper 4 mark scheme. Markers award a best-fit level for the whole answer.</p>
  <div class="tw"><table class="t">
    <tr><th>Level (of the 14 marks)</th><th>The analysis looks like</th></tr>
    <tr><td><b>Level 3</b> (11 to 14)</td><td>Developed and detailed: each chain runs from the trigger to the objective, uses a correct diagram that is explained, is applied to the context, and the answer is well organised.</td></tr>
    <tr><td><b>Level 2</b> (6 to 10)</td><td>Some development, usually one good chain and others thin; a diagram that is drawn but lightly used; limited application. Level 2 tops out at 10.</td></tr>
    <tr><td><b>Level 1</b> (1 to 5)</td><td>Statements and lists, with little or no explanation of why, or analysis of the wrong topic.</td></tr>
  </table></div>
  <div class="tip"><b class="h">The step from Level 2 to Level 3</b>Usually it needs a third developed, applied chain, or one that is deepened from one step to the whole route to the objective. Markers do not award a mark per paragraph, but the pattern is steady.</div>

  <h2>3 · A statement, a step and a chain</h2>
  <div id="pic1" class="card"></div>
  <div class="grid2">
    <div class="wrong-example"><b>Statement:</b> "Higher interest rates reduce investment."</div>
    <div class="wrong-example"><b>One step:</b> "Higher interest rates make borrowing more expensive, so investment falls."</div>
  </div>
  <div class="right-example"><b>Chain:</b> "A higher interest rate raises the cost of borrowing, so fewer projects have an expected return above that cost and firms cut investment. Investment is a component of AD, so AD shifts left, and real GDP and employment are likely to fall; in a country with high business borrowing at variable rates the fall could be larger."</div>

  <h2>4 · How to build a chain</h2>
  <div class="formula">trigger → mechanism → effect on the market or economy → consequence for the objective in the question</div>
  <ul>
    <li><b>Trigger:</b> the policy or change named in the question.</li>
    <li><b>Mechanism:</b> why it matters, using the right concept (cost, incentive, expected return, relative price).</li>
    <li><b>Effect:</b> what moves on the diagram, and in which direction, with figures if you have them.</li>
    <li><b>Consequence:</b> the objective the question asks about (growth, efficiency, equity, inflation, the current account). End the paragraph by naming it.</li>
  </ul>
  <p>Link words do the work: <b>because, so, which means, leading to, as a result, since</b>. If a paragraph has none of these, it is probably a list.</p>

  <h2>5 · Use the diagram as part of the analysis</h2>
  <ul>
    <li>Draw the model the question names. A required diagram that is missing caps the 14-mark scale at Level 2.</li>
    <li>Refer to it in the writing: "the shift from AD1 to AD2 raises the price level from P1 to P2".</li>
    <li>Explain each shift, not just draw it. A diagram with no explanation, or an explanation with no diagram, loses marks.</li>
    <li>Stay inside the model: a micro question answered with macro effects, or an indifference curve question answered with marginal utility, loses the marks even when the reasoning is sound.</li>
  </ul>

  <h2>6 · Use the data as evidence of cause and effect</h2>
  <div class="tw"><table class="t">
    <tr><th>Skill</th><th>Example</th></tr>
    <tr><td><b>Select</b> the relevant figure</td><td>Choose the years or countries that bear on the question, not every number in the table.</td></tr>
    <tr><td><b>Calculate</b></td><td>Percentage change, share of GDP, per head, a ratio. Show the working.</td></tr>
    <tr><td><b>Spot the pattern</b></td><td>"Countries with a higher Gini coefficient also have lower female literacy."</td></tr>
    <tr><td><b>Suggest a cause</b></td><td>"Inequality could limit access to schooling for girls in poorer households."</td></tr>
    <tr><td><b>State the limit</b></td><td>"Five countries show a link but cannot prove that one variable causes the other."</td></tr>
  </table></div>

  <h2>7 · Analysis in short Section A parts</h2>
  <ul>
    <li><b>2 to 4 marks:</b> usually one step per mark, plus a diagram mark if the stem asks for one. Name the step, then its consequence.</li>
    <li><b>"Analyse":</b> break the effect into steps, with a diagram where it helps, and link to the objective named.</li>
    <li><b>"Explain how":</b> two or three linked steps are enough. Do not write an essay.</li>
    <li><b>Last part (7 or 8 marks):</b> develop two points rather than listing four, then use the passage.</li>
  </ul>

  <h2>8 · Common ways to lose AO2 marks</h2>
  <ul>
    <li><b>Stopping after one step:</b> "investment falls" and nothing about AD, output or employment.</li>
    <li><b>Listing:</b> five brief points instead of three developed chains.</li>
    <li><b>Analysing the topic, not the question:</b> discussing GDP when the question said productivity.</li>
    <li><b>Wrong model or wrong policy:</b> fiscal policy in a monetary policy question, or a competitive diagram for a monopsony.</li>
    <li><b>Ignoring the context:</b> treating cost-push inflation as demand-pull, or leaving out the low-income country element.</li>
    <li><b>A diagram drawn and never used.</b></li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Plan each chain in five words on the page: trigger, step, step, effect, objective. If you cannot name the objective at the end, the paragraph will not reach Level 3.</div>
'''

watch = '''
  <h2>1 · A chain from trigger to objective</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A chain with an externality diagram</h2>
  <div id="stB"></div>
  <h2>3 · From a number to a cause</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · How strong is the analysis?</h2>
  <p>Describe the analysis in a 20-mark essay. The lab applies the Table A idea that developed, applied chains with a correct diagram earn the top level. It is a teaching model, not an official mark.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Estimated Table A mark (out of 14, AO1 and AO2)</small><strong id="r1"></strong></div><div><small>Level</small><strong id="r2"></strong></div><div><small>To gain more</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="A bar showing the estimated Table A mark out of fourteen"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Link words that build a chain", "Choose a link word to see a weak sentence, a developed one and where it fits.", ["Without the link", "With the link", "What the link adds"]) + chooser_html("k", "Lab 3 · Find the missing step", "Choose a broken chain to see the gap and the repaired chain.", ["Broken chain", "The missing step", "Repaired chain"])

practise = '''
  <h2>1 · Statement, one step or developed chain?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which part of the chain is it?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the analysis skill</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Answering the topic, not the question", "Reports describe efficiency never developed, policies described with no link to allocative efficiency, and GDP discussed when the question said productivity.", "underlining the key phrases and ending every paragraph by using them to answer the question.") +
rw("Analysis stops after one step", "A common comment is that analysis is a single step, or a list of points, with no development to the objective. This keeps answers at Level 2.", "using trigger, mechanism, effect and consequence, with because or so between them.") +
rw("The wrong model", "A marginal utility essay when indifference curves were asked was capped at Level 1 for that answer, and micro questions were answered with macro effects.", "naming the model in the question and staying inside it.") +
rw("Diagram drawn but not used", "Reports note diagrams that are drawn and never referred to, and explanations of shifts that have no diagram where one was required.", "referring to the diagram by its labels in the text.") +
rw("Correlation treated as proof", "In data response, answers that treat a pattern across a handful of countries as proof of cause lose marks. The best answers say what the pattern suggests and what it cannot show.", "writing 'this suggests' and giving one limit.")
)

mc_exam = [
  ("An increase in government spending on infrastructure raises AD. In the short run the economy has a large negative output gap. What is the most likely result?", ["real GDP rises with little change in the price level", "the price level rises with no change in real GDP", "real GDP falls", "the price level falls"], 0, "With spare capacity, extra AD mainly raises output."),
  ("The marginal propensity to consume is 0.8 and government spending rises by $4bn. By how much could national income rise, ignoring other leakages?", ["$20bn", "$5bn", "$3.2bn", "$4bn"], 0, "Multiplier 5 × $4bn = $20bn."),
  ("A subsidy is given to producers of a good with a positive externality in consumption. Which result is most likely?", ["output rises towards the social optimum", "output falls", "price rises", "the externality disappears entirely"], 0, "The subsidy lowers cost, raising output towards where MSB = MSC."),
  ("A country's currency depreciates. Why might the current account fail to improve in the short run?", ["demand for exports and imports may be inelastic", "exports become more expensive", "imports become cheaper", "the multiplier falls"], 0, "If the sum of elasticities is below one, the Marshall–Lerner condition is not met."),
  ("Which would most strengthen the link between higher interest rates and lower inflation?", ["a large share of household borrowing at variable rates", "firms with large cash reserves", "most spending financed by savings", "an open economy with a fixed exchange rate"], 0, "Variable-rate debt passes the change quickly to spending."),
]

exam = exam_page("analysis: how the marks are reached",
  exam_intro("Compare your chain with the mark scheme points, marked N for analysis."),
  [("Section A analysis parts", "2 below", "4 to 8 marks, 'explain' and 'analyse'"),
   ("Section A data part", "1 below", "6 marks, 'consider with reference to the table'"),
   ("Essay", "1 below", "20 marks, analysis in the 14-mark Table A"),
   ("Multiple choice (Paper 3 style)", "5 below", "Cause and effect, calculation")],
  [
  eq("Practice question", "4 marks", "Explain how an increase in the central bank's interest rate may affect aggregate demand.",
     ["One mark for the higher cost of borrowing or reward to saving.", "One mark for the effect on consumption and investment.", "Up to 2 further marks for development: AD is lowered, and the effect on output, employment or the price level."],
     "Four steps in two or three sentences. Do not evaluate: this part is not asking for it.",
     [[('n', 'A higher interest rate raises the cost of borrowing and increases the reward for saving, so households and firms are less willing to borrow. Households may cut spending on durable goods bought on credit, such as cars, and save more, while firms may postpone investment because fewer projects earn a return above the higher cost of funds.')], [('n', 'Consumption and investment are components of aggregate demand, so AD may shift to the left. Real GDP, employment and the price level are therefore likely to be lower than they would otherwise have been, although a higher interest rate may also raise the exchange rate, which reduces net exports and adds to the fall.')]]),
  eq("Practice question", "8 marks", "Analyse how a tax on a good with a negative consumption externality could move a market closer to allocative efficiency, using a diagram.",
     ["Diagram: MPB, MSB below MPB, supply (MPC = MSC), and the tax shifting supply.", "Over-consumption at the free market output, where MPB meets MPC.", "The tax raises price and lowers quantity towards the social optimum (MSB = MSC).", "Link to allocative efficiency and the welfare loss removed."],
     "Draw first, then three linked steps: free market output, the effect of the tax, the efficiency gain.",
     [[('k', 'A negative consumption externality exists when consuming the good harms third parties, so marginal social benefit (MSB) is below marginal private benefit (MPB). Examples are alcohol or cigarettes. In the diagram the MSB curve lies below the demand curve (MPB), and supply is MPC = MSC.'), ('n', 'In a free market, output is where MPB meets supply, at Q1. At Q1 the social benefit of the last unit is below its cost, because MSB is lower than MPB, so the market over-consumes and there is a welfare loss triangle between Q2 and Q1.')], [('n', 'An indirect tax raises the cost of supply, so the supply curve shifts left by the amount of the tax. The price rises from P1 to P2 and the quantity falls towards Q2, where MSB equals marginal social cost. If the tax is set equal to the gap between MPB and MSB at Q2, the market could reach the social optimum, so the welfare loss is removed.'), ('n', 'This moves the market towards allocative efficiency, because resources are no longer over-allocated to the good. The government also gains tax revenue, which could be spent on treating the harm. The size of the improvement depends on how close the tax is to the external cost and on how responsive demand is.')]]),
  eq("Practice question", "6 marks", "Table: in five countries, a higher Gini coefficient is associated with a lower ratio of female to male literacy. Consider whether the table shows that inequality causes lower female literacy.",
     ["Select and quote two countries' figures.", "Describe the pattern across the five.", "Suggest a link: unequal access to schooling for girls in poor households.", "State a limit: five countries cannot prove cause; other factors such as income may be responsible."],
     "Quote, interpret, then say what the table cannot show.",
     [[('k', 'In the table, the country with the highest Gini coefficient has the lowest ratio of female to male literacy, and the country with the lowest Gini coefficient has the highest ratio. Across all five countries, a higher Gini coefficient goes with a lower ratio, so there is a negative relationship.'), ('n', "This pattern suggests that inequality may limit girls' access to schooling. In an unequal country, poorer households may be unable to afford fees, uniforms or transport, and when families must choose, they may send boys to school before girls. If poorer girls leave school early, literacy among women falls relative to men. Lower literacy then limits women's later earnings, which could keep inequality high, so the link could run in both directions.")], [('e', "However, the table does not show that inequality causes lower female literacy. Five countries is a very small sample, and a correlation only shows that two variables move together. Other factors, such as average income, cultural attitudes to girls' education, or government spending on schools, could explain both a high Gini coefficient and low literacy. The table also gives one year, so it cannot show whether changes in inequality led to changes in literacy over time."), ('e', "Therefore the table supports the claim only weakly: it is consistent with inequality reducing girls' schooling, but more countries, several years and controls for income would be needed to show cause.")]]),
  eq("Practice question", "20 marks", "Assess whether a government should use an increase in public spending to reduce unemployment in a country with a negative output gap.",
     ["Chain 1: spending raises AD, the multiplier raises income, output and employment rise with spare capacity.", "Chain 2: the effect on the budget deficit and borrowing costs, and crowding out.", "Chain 3: the supply-side effect if the spending is on infrastructure or training.", "Diagram: AD and AS with the negative output gap, or an injections and withdrawals diagram if the stem asks for it.", "Evaluation (6 marks): time lags, the size of the multiplier, the state of public finances, alternatives."],
     "Three developed chains, each ending at employment. Name the country context in each paragraph.",
     [[('n', "An increase in public spending is a component of AD, so AD shifts right. In an economy with a negative output gap there are unemployed workers and spare capacity, so firms can raise output without much pressure on prices. Real GDP rises, and firms take on more workers, so unemployment falls. The multiplier strengthens the effect: wages paid to newly employed workers are partly spent, which raises demand for other firms' products and creates further jobs. If the marginal propensity to consume is 0.75, the multiplier is 4, so $5bn of spending could raise income by up to $20bn, although leakages such as taxes and imports reduce this.")], [('n', 'A second chain concerns the budget. As employment rises, income tax and VAT receipts rise and spending on unemployment benefits falls, so part of the cost is recovered. But if the spending is financed by borrowing, the deficit and the national debt rise. The government may have to pay higher interest, or borrow from the private sector, which could push up interest rates and crowd out private investment. That would lower the net effect on jobs.')], [('n', 'A third chain depends on the type of spending. If the money goes into infrastructure, training or technology, it raises the productive capacity of the economy as well as demand, so LRAS shifts right. This means that employment gains could last, and lower costs could help firms compete, so the extra jobs are less likely to disappear when the stimulus ends. Spending on transfer payments or public sector wages, by contrast, may raise demand only temporarily.')], [('e', 'However, there are limits. Time lags in planning and building projects could mean that the spending arrives after the recession is over, so it could add to inflation instead. The multiplier may be small in an open economy where much of the extra income is spent on imports, or where firms and households save the money because they are uncertain about the future. If unemployment is structural, because workers lack the skills required, extra demand may not reduce it.'), ('e', "On balance, increased public spending is likely to reduce unemployment in this economy, because the negative output gap means extra demand mainly raises output. It is most effective if the spending is on productive projects that can start quickly and if the government's borrowing costs remain low. Where unemployment is structural, supply-side policies could be more effective than extra spending.")]]),
  ],
  )

tips = tips_html(
  [("Name the objective at the end.", "Growth, efficiency, equity, inflation, the current account."),
   ("Use link words.", "Because, so, which means, leading to."),
   ("Three chains beat five.", "Develop each, and apply each to the context."),
   ("Draw and use the diagram.", "Refer to its labels in your writing."),
   ("Stay inside the model.", "Micro with micro, the named policy only."),
   ("Say what the data suggest.", "And what it cannot show.")],
  [("Starting a chain", "[Change] raises [cost / return / price], so [response]."),
   ("Linking to the model", "This shifts [curve] from X1 to X2, which raises [variable] from A to B."),
   ("Reaching the objective", "As a result, [objective in the question's words] is likely to [rise / fall]."),
   ("Interpreting data", "The table shows [figure], which suggests [relationship], although [limit].")],
  [CW["explain"], CW["analyse"], CW["assess"], CW["discuss"]]) + FC

js = CHAINJS + STRIP + '''
strip("#pic1", "From a statement to a developed chain", [["Statement", "a claim | no reason"], ["One step", "a claim | and a reason"], ["Chain", "linked steps | to the objective"], ["Applied chain", "linked steps | in this context"]]);
chainStep("#stA", "A chain from trigger to objective", ["Trigger: the central bank raises the interest rate", "Mechanism: borrowing costs rise and saving pays more", "Effect: consumption and investment fall, so AD shifts left", "Consequence: real GDP and the price level fall", "Objective: inflation falls, but unemployment may rise"],
  ["<b>Trigger</b> named in the question.", "<b>Mechanism</b>: why behaviour changes.", "<b>Effect</b> on the diagram.", "<b>Consequence</b> for the economy.", "<b>Objective</b> named, with the trade-off."]);
chainStep("#stB", "A chain with an externality diagram", ["Free market: output where MPB = MPC, above the social optimum", "Marginal social cost is above MPC because of the pollution", "A tax equal to the external cost shifts supply left", "Price rises and output falls towards MSB = MSC", "The welfare loss triangle disappears: allocative efficiency"],
  ["<b>Free market</b> over-produces.", "<b>The gap</b> between MSC and MPC is the external cost.", "<b>The tax</b> internalises it.", "<b>The result</b> is on the diagram.", "<b>The objective</b> in the question's words."]);
chainStep("#stC", "From a number to a cause", ["Select: unemployment fell from 9.1% to 7.4% between 2015 and 2019", "Calculate: a fall of 1.7 percentage points", "Pattern: growth in the same period averaged 3.2% a year", "Cause: with growth above trend, firms may have hired more workers", "Limit: other factors such as emigration could also have lowered the rate"],
  ["<b>Select</b> the relevant figures.", "<b>Calculate</b> with the correct unit.", "<b>Pattern</b> across the data.", "<b>Cause</b> suggested, not asserted.", "<b>Limit</b> stated."]);

function ev() {
  const ids = ["ch", "dv", "dg", "ap"];
  if (!ids.every((i) => $("#" + i))) return;
  const [ch, dv, dg, ap] = ids.map((i) => +$("#" + i).value);
  let m = Math.min(3, ch) * 2.2 * (0.55 + 0.25 * dv) + dg * 1.2 + ap * 1.2 + Math.min(ch, 1) * 0.6;
  m = Math.round(Math.max(0, Math.min(14, m)));
  if (dg === 0) m = Math.min(m, 10);
  if (ch === 0) m = Math.min(m, 3);
  if (dv === 0) m = Math.min(m, 7);
  const L = m >= 11 ? 3 : m >= 6 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 14"; $("#r2").textContent = L ? "Level " + L : "No credit";
  $("#r3").textContent = dg === 0 ? "Add the diagram the question names (capped at Level 2 without it)" : ch < 3 ? "Add a third chain" : dv < 2 ? "Take each chain all the way to the objective" : ap < 2 ? "Apply each chain to the context" : m >= 14 ? "At the top" : "Check the logic and organisation";
  $("#rv").textContent = `${ch} chain(s), development ${["thin", "some", "full"][dv]}, diagram ${["missing", "partly used", "correct and used"][dg]}, application ${["none", "some", "throughout"][ap]}: about ${m} out of 14 (${L ? "Level " + L : "no credit"}).`;
  const W = 340, X = (v) => 40 + (v / 14) * W;
  let o = SV.rect(X(0), 70, X(5) - X(0), 40, "f2", op(0.4)) + SV.rect(X(5), 70, X(10) - X(5), 40, "f1", op(0.4)) + SV.rect(X(10), 70, X(14) - X(10), 40, "f3", op(0.4)) + SV.text(X(2.5), 95, "L1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(7.5), 95, "L2", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(12), 95, "L3", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 50, X(m), 130, "c4", { "stroke-width": 3 }) + SV.text(X(m), 44, m + "", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ch", label: "Developed chains (0 to 4) ", min: 0, max: 4, step: 1, value: 2, fmt: (v) => v, onInput: ev });
Lib.slider($("#g2"), { id: "dv", label: "Development: 0 thin, 1 some, 2 full to the objective ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["thin", "some", "full"][v], onInput: ev });
Lib.slider($("#g3"), { id: "dg", label: "Diagram: 0 missing, 1 partly used, 2 correct and used ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["missing", "partly used", "correct and used"][v], onInput: ev });
Lib.slider($("#g4"), { id: "ap", label: "Application: 0 none, 1 some, 2 throughout ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "some", "throughout"][v], onInput: ev });
ev();

chooser("h", [
  ["because", "Firms cut investment.", "Firms cut investment because the cost of borrowing exceeds the expected return on more projects.", "A reason for the first step", 5],
  ["so", "AD falls.", "Investment is a component of AD, so AD shifts left.", "A consequence on the model", 5],
  ["which means", "Output rises.", "Output rises, which means more workers are needed.", "The next effect", 4],
  ["leading to", "Prices fall.", "Lower AD reduces demand-pull pressure, leading to a lower price level.", "The route to the objective", 4],
  ["as a result", "Inflation is lower.", "As a result, inflation falls towards the target, although unemployment could rise.", "The objective in the question", 5]
], (it) => `Link: ${it[0]}. Without: "${it[1]}" With: "${it[2]}" Adds: ${it[3].toLowerCase()}.`, "How often this link is needed");
chooser("k", [
  ["Tax cut to inflation", "Tax cut → inflation rises", "The step through disposable income, spending and AD", "A tax cut raises disposable income, so spending rises, shifting AD right and pushing the price level up.", 5],
  ["Subsidy to output", "Subsidy → output rises", "Why costs fall and which curve shifts", "A subsidy lowers marginal cost, shifting supply right, so price falls and output rises.", 4],
  ["Depreciation to current account", "Depreciation → exports rise", "Price in foreign currency and elasticity", "A depreciation lowers export prices abroad, so the quantity sold may rise if demand is elastic.", 5],
  ["Training to growth", "Training → growth", "Productivity and LRAS", "Training raises productivity, shifting LRAS right, so potential output and growth rise.", 4],
  ["Minimum wage to jobs", "Minimum wage → unemployment", "Wage above equilibrium, labour demand and supply", "A minimum wage above equilibrium raises supply and lowers demand, creating a surplus of labour.", 5]
], (it) => `Broken: ${it[0]} (${it[1]}). Missing: ${it[2]}. Repaired: ${it[3]}`, "Marks gained by repairing it");
''' + CLASSIFY("cl1", "Statement, one step or developed chain?", ["Statement", "One step", "Developed chain"],
  [("Higher taxes reduce spending.", 0), ("Higher income tax reduces disposable income, so spending falls.", 1), ("Higher income tax reduces disposable income, so consumption falls, shifting AD left and lowering output and employment.", 2), ("Subsidies increase output.", 0), ("A subsidy lowers costs, so supply shifts right.", 1), ("A subsidy lowers costs and shifts supply right, so price falls and output rises, which could help the poorest households if the good is a necessity.", 2)],
  "A statement claims, a step gives a reason, a chain reaches the objective.") + CLASSIFY("cl2", "Which part of the chain is it?", ["Trigger", "Mechanism", "Effect", "Consequence"],
  [("The central bank raises the interest rate.", 0), ("Borrowing becomes more expensive.", 1), ("AD shifts left.", 2), ("Inflation falls towards the target.", 3), ("The government introduces a tax on sugary drinks.", 0), ("The price of the drinks rises relative to substitutes.", 1)],
  "Trigger, mechanism, effect, consequence.") + ORDER(
  "Put the chain in order.",
  ["Government cuts income tax", "Disposable income rises", "Consumption rises", "AD shifts right", "Real GDP and the price level rise"],
  "Each step leads to the next.") + MATCH([
  ["Select", "Pick the figures that bear on the question"],
  ["Calculate", "Show a percentage change or ratio with its unit"],
  ["Interpret", "Say what the figure means"],
  ["Suggest a cause", "Offer a reason the pattern may exist"],
  ["State a limit", "Say what the data cannot show"],
  ["Link", "Because, so, which means"]]) + CALC([
  {"q": "MPC is 0.75 and investment rises by $6bn. Calculate the largest rise in national income (ignore other leakages).", "a": 24, "unit": "$bn", "tol": 0.1, "hint": "k = 1 ÷ 0.25 = 4.", "sol": "<b>$24bn</b>."},
  {"q": "Unemployment falls from 8.0% to 6.4%. By how many percentage points?", "a": 1.6, "unit": "points", "tol": 0.01, "hint": "8.0 − 6.4.", "sol": "<b>1.6 percentage points</b>."},
  {"q": "Real GDP rises from $500bn to $515bn. Calculate the percentage growth.", "a": 3, "unit": "%", "tol": 0.05, "hint": "15 ÷ 500.", "sol": "<b>3%</b>."},
  {"q": "Exports are $60bn and GDP is $240bn. What share of GDP is exports?", "a": 25, "unit": "%", "tol": 0.1, "hint": "60 ÷ 240.", "sol": "<b>25%</b>."}]) + MCQ([
  ("Which is a developed chain?", ["A subsidy lowers costs, shifting supply right, so price falls and output rises.", "A subsidy is good.", "Subsidies cost the government.", "Output may change."], 0, "It has steps with because/so logic."),
  ("The best way to end an analysis paragraph is to:", ["name the objective in the question", "start a new topic", "define a term", "write 'in conclusion'"], 0, "The chain is complete when it reaches the objective."),
  ("A required diagram is missing from a 20-mark essay. What is the effect?", ["The 14-mark scale is capped at Level 2", "No effect", "Evaluation is lost", "The essay is marked out of 10"], 0, "The cap applies to the 14-mark scale."),
  ("A correlation across five countries shows:", ["A pattern that suggests a link but does not prove cause", "Proof of cause", "That the data are wrong", "No relationship"], 0, "Say what it suggests and what it cannot show."),
  ("How many developed chains are usually needed to move from Level 2 into Level 3?", ["Three, applied to the context", "One", "Six", "None"], 0, "A third developed, applied chain is the usual step.")
], "qz1") + CARDS([
  ("AO2", "Analysis: causes, effects, consequences."),
  ("Weighting", "40% overall, 37% of Paper 4, 40% of Paper 3."),
  ("Chain", "Trigger, mechanism, effect, consequence."),
  ("Link words", "Because, so, which means, leading to."),
  ("Level 3", "Developed, detailed, accurate, diagram explained."),
  ("Three chains", "Target for a 20-mark essay."),
  ("Diagram", "Required diagram missing: capped at Level 2."),
  ("Data", "Select, calculate, interpret, limit.")]) + MCQ(mc_exam)

build("pa2", "a-level-ao2-analysis", "AO2 Analysis: Building Chains of Reasoning in Paper 4", EYP,
  "What separates a statement, a one-step comment and a developed chain, how Table A rewards analysis, using diagrams and data, and short Section A parts. Animations, labs and practice.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
