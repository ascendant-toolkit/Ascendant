"""AS exam technique: Paper 1 multiple choice. Run: python3 tools/artifact-kit/mk_ex4.py"""
from as6k import *
EY = "AS Level Economics · 9708 · Exam technique"

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>Paper 1 is a <b>multiple choice paper of 30 questions in 1 hour</b>, each with four options and worth <b>1 mark</b>, so it carries <b>30 of the 90 marks</b> at AS Level; you answer on a separate sheet in soft pencil, a calculator is allowed, and the instructions say each correct answer scores one mark and mention no deduction for a wrong one, so <b>every question should be answered</b>. The questions cover the <b>whole syllabus</b>, broadly in syllabus order, and test <b>knowledge and understanding, application and analysis</b> through definitions, calculations, tables, short scenarios and diagrams. Each wrong option is built to catch a particular mistake (a reversed relationship, the wrong curve, a true statement that does not answer the question), so the best method is to <b>read the stem carefully, predict the answer, then test every option</b>. Time is not usually the problem: you have <b>2 minutes per question</b>, so the marks are lost to <b>misreading, calculation slips and unfinished elimination</b>. This page sets out the facts, the method, the question types with real examples, and a time plan.</p></div>

  <h2>1 · The facts</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td><b>Paper</b></td><td>Paper 1, AS Level Multiple Choice (variants 11 to 14 in each series)</td></tr>
    <tr><td><b>Questions and time</b></td><td>30 questions, 1 hour: 2 minutes per question</td></tr>
    <tr><td><b>Marks</b></td><td>30 (one for each correct answer); the instructions mention no deduction for wrong answers</td></tr>
    <tr><td><b>Options</b></td><td>Four, labelled A to D; choose the one you consider correct</td></tr>
    <tr><td><b>Equipment</b></td><td>Soft pencil and eraser for the answer sheet; a calculator; rough working on the question paper</td></tr>
    <tr><td><b>Share of AS</b></td><td>30 of 90 marks (Paper 2 is 60)</td></tr>
    <tr><td><b>Syllabus coverage</b></td><td>Topics 1 to 6 of the AS syllabus, broadly in order: early questions on basic ideas and the price system, then government intervention, the macroeconomy, macro policy and international economics towards the end</td></tr>
  </table></div>

  <h2>2 · Using the 60 minutes</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>Time</th><th>What to do</th></tr>
    <tr><td><b>First pass</b></td><td>35 to 40 minutes</td><td>Answer every question you can do with confidence at once (about 1 to 1.5 minutes each). Mark with a tick the ones you are unsure of and leave long diagram or calculation questions for later.</td></tr>
    <tr><td><b>Second pass</b></td><td>15 to 20 minutes</td><td>Return to the marked questions. Do the calculations, sketch the diagrams, eliminate options.</td></tr>
    <tr><td><b>Final check</b></td><td>5 minutes</td><td>Make sure every question has an answer on the sheet (a guess costs nothing). Check that answers are in the right row.</td></tr>
  </table></div>
  <ul>
    <li>Do not spend more than <b>3 minutes</b> on any one question the first time.</li>
    <li>Fill in the answer sheet <b>as you go</b>, not at the end, and check the question number after skipping.</li>
    <li>If two options remain, <b>choose one</b> and move on: you can return if time allows.</li>
  </ul>

  <h2>3 · The four steps</h2>
  <div class="tw"><table class="t">
    <tr><th>Step</th><th>What to do</th><th>Why</th></tr>
    <tr><td><b>1 · Read</b></td><td>Read the stem twice. Underline <b>not</b>, <b>least likely</b>, <b>most likely</b>, <b>always</b>, <b>only</b>, units, and the exact thing asked (price, quantity, revenue).</td><td>Misreading a "not" question turns a right answer into a wrong one.</td></tr>
    <tr><td><b>2 · Predict</b></td><td>Cover the options and decide what the answer should be, or draw a quick diagram.</td><td>It stops you being pulled towards a plausible-looking option.</td></tr>
    <tr><td><b>3 · Test</b></td><td>Read all four options. Cross out the clearly wrong ones and say why each is wrong. Check the remaining ones against the stem.</td><td>The right answer is often only the best of two partly true options.</td></tr>
    <tr><td><b>4 · Check</b></td><td>For calculations, check units, signs and percentage versus percentage point. For policies, check the direction and the time period.</td><td>Many wrong options are the answer with a sign or unit error.</td></tr>
  </table></div>

  <h2>4 · How wrong options are built</h2>
  <div class="tw"><table class="t">
    <tr><th>Distractor</th><th>What it does</th><th>Example</th></tr>
    <tr><td><b>Reversed relationship</b></td><td>Right variables, wrong direction</td><td>"A depreciation lowers the price of imports"</td></tr>
    <tr><td><b>Wrong curve or wrong concept</b></td><td>Shifts demand when supply should shift, or uses a movement for a shift</td><td>A tax shown as a shift of demand</td></tr>
    <tr><td><b>True but irrelevant</b></td><td>A correct statement that does not answer the question asked</td><td>A correct fact about GNI in a GDP question</td></tr>
    <tr><td><b>Partly true</b></td><td>Correct first half, wrong second half</td><td>"A merit good is non-rival and under-consumed"</td></tr>
    <tr><td><b>Calculation slip</b></td><td>The answer you get if you forget a step</td><td>Using the new quantity but forgetting to deflate nominal GDP</td></tr>
    <tr><td><b>Absolute words</b></td><td>"Always" or "only" make a statement false</td><td>"Tariffs always raise welfare"</td></tr>
    <tr><td><b>Similar terms</b></td><td>Swaps related terms</td><td>Budget deficit and current account deficit; real and nominal</td></tr>
  </table></div>

  <h2>5 · Question types and how to attack them</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Typical stem</th><th>How to attack it</th></tr>
    <tr><td><b>1 · Recall and definition</b></td><td>"Which type of good is healthcare?"</td><td>Answer from memory before reading the options; check each option's definition.</td></tr>
    <tr><td><b>2 · Calculation</b></td><td>"What is the real GDP in year 2?"</td><td>Write the formula, substitute, check units; use the options to check your answer.</td></tr>
    <tr><td><b>3 · "Not", "least likely"</b></td><td>"What is not an example of protectionism?"</td><td>Decide whether each option is true, and pick the odd one out. Underline "not".</td></tr>
    <tr><td><b>4 · Statement correct or incorrect</b></td><td>"What does not happen when price allocates resources?"</td><td>Test each statement separately against a definition.</td></tr>
    <tr><td><b>5 · Two-part combination</b></td><td>"How is this likely to affect the exchange rate and cost-push inflation?"</td><td>Work out each part separately, then find the option with both right.</td></tr>
    <tr><td><b>6 · Table or data</b></td><td>"What is the current account balance?"</td><td>Work out what is asked from the table; sum with signs.</td></tr>
    <tr><td><b>7 · Diagram</b></td><td>"Which area represents total revenue?"</td><td>Redraw or mark it; label the curves; identify what shifted and why.</td></tr>
    <tr><td><b>8 · Cause and effect</b></td><td>"Which policy would reduce both unemployment and the deficit?"</td><td>Trace the chain step by step; ask what makes it less effective.</td></tr>
    <tr><td><b>9 · Positive and normative</b></td><td>"Which statement is normative?"</td><td>Positive statements can be tested with evidence; normative ones contain "should" or a value judgement.</td></tr>
  </table></div>

  <h2>6 · Formulae and checks that pay off</h2>
  <div class="tw"><table class="t">
    <tr><th>Concept</th><th>Formula</th><th>Check</th></tr>
    <tr><td>PED, YED, XED, PES</td><td>% change in quantity ÷ % change in price (or income, or the other price)</td><td>Use percentage changes, not absolute ones</td></tr>
    <tr><td>Total revenue</td><td>Price × quantity</td><td>Elastic: price and revenue move in opposite directions</td></tr>
    <tr><td>Terms of trade</td><td>(Export price index ÷ import price index) × 100</td><td>An index, no units</td></tr>
    <tr><td>Real GDP</td><td>Nominal GDP ÷ price index × 100</td><td>Deflate before comparing</td></tr>
    <tr><td>GDP, GNI, NNI</td><td>C + I + G + (X − M); + net primary income; − depreciation</td><td>Ignore items such as national debt</td></tr>
    <tr><td>Unemployment rate</td><td>Unemployed ÷ labour force × 100</td><td>Labour force = employed + unemployed</td></tr>
    <tr><td>Current account</td><td>Goods + services + primary + secondary income</td><td>Sum with signs; negative is a deficit</td></tr>
    <tr><td>Per head</td><td>Total ÷ population</td><td>If income rises 10% and population falls 10%: 1.10 ÷ 0.90</td></tr>
  </table></div>

  <h2>7 · Words in the stem that change the answer</h2>
  <ul>
    <li><b>Not, least likely, except:</b> find the false option; three options will be true.</li>
    <li><b>Most likely, best explains:</b> several options may be partly true; choose the strongest.</li>
    <li><b>Always, only, never:</b> usually make a statement false.</li>
    <li><b>Effective, ineffective:</b> consider whether a policy is above or below equilibrium (price controls), or the elasticity.</li>
    <li><b>Short run or long run:</b> the answer may differ.</li>
    <li><b>Percentage or percentage point:</b> from 4% to 6% is a 2 point rise and a 50% rise.</li>
    <li><b>Nominal or real, gross or net, deficit or debt:</b> check the exact term.</li>
  </ul>

  <h2>8 · Common ways to lose marks</h2>
  <ul>
    <li><b>Misreading "not"</b>, or answering the question you expected.</li>
    <li><b>Not reading all four options</b> after seeing one that looks right.</li>
    <li><b>Calculating with the wrong figures</b> (nominal instead of real; price instead of percentage change).</li>
    <li><b>Spending too long</b> on one question, then guessing the last ones.</li>
    <li><b>Leaving blanks</b>: there is no penalty for a wrong answer.</li>
    <li><b>Shifting the wrong curve</b> in a diagram question.</li>
    <li><b>Changing a right answer</b> without a clear reason.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For every question you get wrong in practice, write down which <b>distractor</b> caught you: a reversed relationship, the wrong curve, a true-but-irrelevant option or a calculation slip. You will see the same traps again.</div>
'''

watch = '''
  <h2>1 · The four steps on a real question</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A calculation question</h2>
  <div id="stB"></div>
  <h2>3 · A two-part combination question</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Time plan for the 60 minutes</h2>
  <p>Set how long you spend on the first pass and see the time left per question for the rest.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Time per question, first pass</small><strong id="r1"></strong></div><div><small>Time left for the second pass</small><strong id="r2"></strong></div><div><small>Questions left for pass two</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="A bar divided into first pass, second pass and final check"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · What type of question is it?", "Choose a stem to see its type and the best first move.", ["Type", "First move", "Trap to avoid"]) + chooser_html("k", "Lab 3 · Calculation traps", "Choose a calculation to see the correct method and the wrong answer examiners expect.", ["Correct method", "Trap answer", "Why it is wrong"])

practise = '''
  <h2>1 · Which type of question is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which distractor is it?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the four steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the stem word to what it tells you</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A 'not' question", "'What is not an example of protectionism?' Options included export subsidies, import subsidies, quotas and tariffs. Three are protectionist; subsidising imports would encourage imports, so it is the odd one out.", "reading 'not' and finding the false option.") +
rw("A calculation with a table", "A table gives exports, imports, services and income. The current account balance is the sum of the four balances with signs: (150 − 200) + (70 − 50) + (120 − 100) + (15 − 20) = −15.", "summing with signs and checking the units.") +
rw("A two-part combination", "'A worsening current account will affect the exchange rate and cost-push inflation how?' A fall in the exchange rate raises import prices, so cost-push inflation rises: depreciate and increase.", "working each part separately.") +
rw("A true statement that does not answer", "In a question on why a government would devalue, an option about reducing demand-pull inflation is true of other policies but is the opposite of the aim of a devaluation.", "a true-but-irrelevant distractor.") +
rw("Normative or positive", "'The rate of interest should be reduced' is normative because it contains a value judgement; 'if interest rates fall, consumption is likely to increase' can be tested with evidence.", "spotting 'should'.")
)

mc_exam = [
  mcq("s20_13", 3, "Which type of good is healthcare?", ["demerit", "free", "merit", "public"], 2, "Recall: healthcare is more beneficial than consumers realise."),
  mcq("s23_13", 20, "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2?", ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], 3, "Calculation: 577.5 ÷ 1.05 = 550. The $476 billion option multiplies by 0.825 instead of dividing."),
  mcq("s20_12", 8, "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges?", ["-0.4", "+0.4", "+2.0", "+2.5"], 3, "Calculation: demand rose 25%; the price rose 10%; XED = 25 ÷ 10 = +2.5. Options -0.4 and +0.4 come from inverting the ratio."),
  mcq("s21_11", 10, "A government introduces a subsidy for product X and the market price of X falls by 5%. The cross elasticity of demand for product Y, with respect to the price of X, is +0.4. What will happen to the demand for product Y?", ["It will decrease by 2%.", "It will decrease by 12.5%.", "It will increase by 2%.", "It will increase by 12.5%."], 0, "Calculation with a sign: 0.4 × (−5%) = −2%."),
  mcq("m24_12", 27, "An extract from a country's balance of payments ($ billion): trade in goods, exports 150 and imports 200; trade in services, exports 70 and imports 50; primary income, receipts 120 and payments 100; secondary income, receipts 15 and payments 20. What is the current account balance?", ["-$10bn", "-$15bn", "-$30bn", "-$50bn"], 1, "Table: (150 − 200) + (70 − 50) + (120 − 100) + (15 − 20) = −50 + 20 + 20 − 5 = −15."),
  mcq("s20_12", 10, "A good has a price elasticity of supply of 2.0. The current quantity supplied is 300 units per week at a market price of $20 per unit. The firm raises the price to $25 per unit. What will the new quantity supplied be per week?", ["150 units", "375 units", "400 units", "450 units"], 3, "Calculation: price +25%, so quantity +50%: 300 × 1.5 = 450."),
  mcq("s20_12", 6, "A manufacturer progressively reduces the price of his product. The table shows total revenue of $750 (000s) at prices of $10, $9 and $8. What is the price elasticity of demand for the product?", ["perfectly inelastic", "relatively inelastic", "perfectly elastic", "unitary"], 3, "Table: revenue is constant as price falls, so demand is unitary."),
  mcq("m25_12", 1, "Which statement about a market economy is not correct?", ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], 2, "'Not correct': 'always' makes C false, since prices ignore external costs."),
  mcq("s21_13", 20, "What is not an aim of protectionism?", ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], 1, "'Not an aim': protectionism aims to cut imports and protect industries, not to raise export prices."),
  mcq("s22_12", 12, "What does not happen when price acts as a means to allocate resources?", ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], 0, "Test each statement: public goods are not supplied through the price mechanism."),
  mcq("s21_12", 27, "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation)", ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], 3, "Two parts: worse current account lowers the rate; a lower rate raises import costs and cost-push inflation."),
  mcq("m24_12", 7, "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X?", ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], 0, "Three parts: YED negative: inferior; PED size 2.4: elastic; XED positive: substitute."),
  mcq("m20_12", 8, "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y)", ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], 2, "Two parts: higher income raises demand for a normal good; a fall in the price of a complement raises demand for X."),
  mcq("s20_13", 4, "Which is a normative statement?", ["If interest rates fall consumption is likely to increase.", "If interest rates fall consumption will definitely increase.", "Interest rates and consumption are usually inversely related.", "The rate of interest should be reduced."], 3, "Normative: 'should' is a value judgement."),
  mcq("m24_12", 25, "A government decides to allow the country's currency to depreciate to remove the deficit on its current account. What is the most likely reason why this would not work?", ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], 3, "Cause and effect: options A and C would help; trade barriers limit export gains."),
  mcq("m25_12", 19, "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head?", ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], 3, "Calculation trap: 1.10 ÷ 0.90 = 1.22, which is more than 20%, not exactly 20%.")
]

exam = exam_page("Paper 1 technique",
  "Sixteen past Paper 1 questions grouped by the type they illustrate: recall, calculations (with the usual trap), tables, 'not' questions, statements, two-part combinations, a normative statement and cause and effect. Work each one with the four steps before opening the reason. The reason says what the question tests and which wrong option catches which mistake.",
  [("Multiple choice (Paper 1)", "16 shown below", "2020 to 2025")],
  [],
  )

tips = tips_html(
  [("Underline 'not', 'always', 'only', 'most likely'.", "Misreading costs the mark."),
   ("Predict, then look.", "Cover the options first."),
   ("Test all four options.", "The best of two partly true ones."),
   ("Calculate with the formula.", "Percentages, real values, signs."),
   ("Draw a quick diagram.", "Shift or movement, which curve."),
   ("Never leave a blank.", "A wrong answer is not penalised in the instructions."),
   ("Two minutes a question.", "Mark and return after 3 minutes.")],
  [("Distractor", "A distractor is a wrong option designed to catch a common mistake."),
   ("Stem", "The stem is the question text before the options."),
   ("Normative", "A normative statement contains a value judgement."),
   ("Elastic", "Demand is elastic if the percentage change in quantity exceeds the percentage change in price."),
   ("Real GDP", "Real GDP is nominal GDP divided by the price index times 100.")],
  [CW["define"], CW["calculate"] if "calculate" in CW else CW["explain"], CW["explain"]]) + FC

js = SDJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["First pass", "35 to 40 min", "Do the sure ones, tick the doubtful", 20, "f2", 330], ["Second pass", "15 to 20 min", "Calculations, diagrams, elimination", 360, "f1", 230], ["Check", "5 min", "No blanks; right row", 600, "f3", 140]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Plan for the 60 minutes of Paper 1">${o}</svg>`;
})();
chainStep("#stA", "The four steps on a real question", ["Read: 'What is not an example of protectionism?' Underline 'not'", "Predict: three options restrict imports or help exporters; one does the opposite", "Test: export subsidies help exporters; quotas and tariffs restrict imports; import subsidies encourage imports", "Check: the odd one out is import subsidies"], [
  "<b>Step 1:</b> the word 'not' reverses the usual question.", "<b>Step 2:</b> decide what the answer should look like.", "<b>Step 3:</b> test every option against the definition.", "<b>Step 4:</b> answer B (import subsidies)."]);
chainStep("#stB", "A calculation question", ["Question: nominal GDP rose to $577.5bn and prices rose 5%. What is real GDP?", "Write the formula: real GDP = nominal GDP ÷ price index × 100", "Substitute: 577.5 ÷ 1.05", "Answer: $550bn; check the options for it", "Trap: multiplying by 0.95 or by 1.05 gives wrong options"], [
  "<b>Read:</b> the data is nominal; the question asks for real.", "<b>Formula first.</b>", "<b>Substitute</b> carefully.", "<b>Check</b> that the answer is in the options.", "<b>Wrong options</b> come from the wrong operation."]);
chainStep("#stC", "A two-part combination question", ["Question: a worse current account: effect on the exchange rate and on cost-push inflation?", "Part 1: more imports and fewer exports, so the currency falls (depreciate)", "Part 2: a weaker currency makes imports dearer, so costs rise (inflation increases)", "Find the option with both: depreciate and increase", "The other options each have one part wrong"], [
  "<b>Split the question.</b>", "<b>Work out part 1.</b>", "<b>Work out part 2.</b>", "<b>Match both parts</b> to one option.", "<b>Half-right options</b> are the distractors."]);

function tp() {
  const ids = ["fp", "ex"];
  if (!ids.every((i) => $("#" + i))) return;
  const fp = +$("#fp").value, ex = +$("#ex").value, ck = 5, sp = 60 - fp - ck;
  const per = fp / 30; $("#r1").textContent = Lib.fmtN(per, 1) + " min";
  $("#r2").textContent = sp + " min"; $("#r3").textContent = ex + " (about " + Lib.fmtN(sp / Math.max(ex, 1), 1) + " min each)";
  $("#rv").textContent = `With ${fp} minutes on the first pass (${Lib.fmtN(per, 1)} minutes per question) and ${ck} minutes to check, you have ${sp} minutes for the ${ex} questions you postponed: about ${Lib.fmtN(sp / Math.max(ex, 1), 1)} minutes each. ` + (per > 1.4 ? "The first pass is slow; leave long questions earlier." : per < 1 ? "The first pass is quick: check each answer as you go." : "A balanced plan.");
  const W = 380, X = (v) => 20 + (v / 60) * W;
  $("#labA").innerHTML = SV.rect(X(0), 70, X(fp) - X(0), 50, "f2", op(0.5)) + SV.rect(X(fp), 70, X(fp + sp) - X(fp), 50, "f1", op(0.5)) + SV.rect(X(fp + sp), 70, X(60) - X(fp + sp), 50, "f3", op(0.5)) + SV.text(X(fp / 2), 100, "Pass 1: " + fp, "sm", { "text-anchor": "middle" }) + SV.text(X(fp + sp / 2), 100, "Pass 2: " + sp, "sm", { "text-anchor": "middle" }) + SV.text(X(60) - 6, 160, "Check " + ck, "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "fp", label: "Minutes on the first pass ", min: 25, max: 45, step: 1, value: 38, fmt: (v) => v, onInput: tp });
Lib.slider($("#g2"), { id: "ex", label: "Questions postponed to the second pass ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: tp });
tp();

chooser("h", [
  ["'Which type of good is healthcare?'", "Recall and definition", "Answer before looking at the options", "Mixing merit and public goods", 5],
  ["'What is the real GDP in year 2?'", "Calculation", "Write the formula and substitute", "Using nominal instead of real figures", 5],
  ["'What is not an example of protectionism?'", "'Not' question", "Test each option; find the odd one", "Choosing the first option that is true", 5],
  ["'How will this affect the exchange rate and inflation?'", "Two-part combination", "Work out each part separately", "Getting one part right and guessing the other", 4],
  ["'What is the current account balance?' (table)", "Table or data", "Sum the balances with signs", "Forgetting a deficit is negative", 4],
  ["'Which statement is normative?'", "Positive or normative", "Look for 'should' or a value judgement", "Choosing a prediction with 'definitely'", 3],
  ["'Which area represents total revenue?' (diagram)", "Diagram", "Mark price × quantity on the diagram", "Using the wrong price or quantity", 4]
], (it) => `${it[0]} Type: ${it[1].toLowerCase()}. First move: ${it[2].toLowerCase()}. Trap: ${it[3].toLowerCase()}.`, "How often this type appears");
chooser("k", [
  ["Real GDP from nominal GDP", "Nominal ÷ price index × 100", "Nominal × price index ÷ 100", "It inflates the figure instead of removing the price rise", 5],
  ["Price elasticity of demand", "% change in quantity ÷ % change in price", "Change in quantity ÷ change in price (absolute)", "Elasticity uses percentages", 5],
  ["Income per head when income +10% and population −10%", "1.10 ÷ 0.90 = 1.22 (up 22%)", "10% + 10% = 20%", "A fall in the denominator raises the ratio by more than 20%", 4],
  ["Percentage change from 4% to 6%", "50% rise (2 ÷ 4)", "2% rise", "Two percentage points is not the same as 2%", 4],
  ["Terms of trade index", "(Export price index ÷ import price index) × 100", "Import ÷ export", "It reverses the meaning of improvement", 4],
  ["Current account balance from a table", "Sum the balances: goods, services, primary and secondary income, with signs", "Add exports only", "Ignores imports and payments", 4]
], (it) => `${it[0]}: ${it[1]}. Trap: ${it[2]}. ${it[3]}.`, "How common the trap is");
''' + CLASSIFY("cl1", "Which type of question is it?", ["Recall", "Calculation", "'Not' question", "Combination"],
  [("Which type of good is healthcare?", 0), ("What is the real GDP in year 2?", 1), ("What is not an aim of protectionism?", 2), ("How is this likely to affect the exchange rate and inflation?", 3), ("What is the definition of long run?", 0), ("What is the unemployment rate for these figures?", 1), ("Which statement is least likely to be true?", 2), ("Which combination correctly describes good X?", 3)],
  "Recall questions ask for a fact; calculations need numbers; 'not' questions need the false option; combinations have two parts.") + CLASSIFY("cl2", "Which distractor is it?", ["Reversed relationship", "True but irrelevant", "Calculation slip"],
  [("A depreciation makes imports cheaper", 0), ("Nominal GDP is higher than real GDP when prices rise (a true statement in a question about growth)", 1), ("Choosing 20% when the answer needs 1.10 ÷ 0.90", 2), ("A rise in interest rates lowers the cost of borrowing", 0), ("A correct fact about GNI in a question on GDP", 1), ("Forgetting to deflate before comparing", 2)],
  "Wrong options are built to catch particular mistakes.") + ORDER(
  "Put the four steps in order.",
  ["Read the stem twice and underline the key words", "Predict the answer before looking at the options", "Test every option and cross out the wrong ones", "Check units, signs and direction, then answer"],
  "Read, predict, test, check.") + MATCH([
  ["Not, least likely", "Find the false option"],
  ["Always, only", "Usually makes a statement false"],
  ["Most likely", "Several options may be true; choose the best"],
  ["Percentage point", "A difference between two percentages"],
  ["Normative", "Contains a value judgement such as 'should'"],
  ["Real", "Adjusted for inflation"]]) + CALC([
  {"q": "Paper 1 has 30 questions in 60 minutes. How many minutes per question?", "a": 2, "unit": "min", "tol": 0.05, "hint": "60 ÷ 30.", "sol": "<b>2 minutes</b>."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "Price rises 20% and quantity demanded falls 30%. What is the price elasticity of demand (size)?", "a": 1.5, "unit": "", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5</b>."},
  {"q": "A rate rises from 4% to 6%. By what percentage has it risen?", "a": 50, "unit": "%", "tol": 0.5, "hint": "2 ÷ 4.", "sol": "<b>50%</b>, a rise of 2 percentage points."},
  {"q": "Goods −30, services +10, primary income +15, secondary income −5 ($bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "−30 + 10 + 15 − 5.", "sol": "<b>−$10bn</b>."}]) + MCQ([
  ("How many marks does Paper 1 carry at AS Level?", ["20", "30", "40", "60"], 1, "30 questions, 1 mark each."),
  ("According to the paper instructions, how is a correct answer rewarded?", ["One mark, with no deduction mentioned for a wrong answer", "Two marks", "Half a mark", "One mark minus a penalty for errors"], 0, "Each correct answer will score one mark; no penalty is stated."),
  ("A question says 'which is not...'. What should you do?", ["Find the false option", "Find the true option", "Skip it", "Choose the longest option"], 0, "Three options will be true."),
  ("Why predict the answer before reading the options?", ["It stops you being pulled to a plausible distractor", "It saves paper", "It is compulsory", "Options are random"], 0, "A prediction guards against distractors."),
  ("About how long is available for each question on average?", ["1 minute", "2 minutes", "4 minutes", "5 minutes"], 1, "60 minutes for 30 questions.")
], "qz1") + CARDS([
  ("Paper 1", "30 questions, 60 minutes, 30 marks."),
  ("Four steps", "Read, predict, test, check."),
  ("No penalty", "Answer every question."),
  ("Distractors", "Reversed, wrong curve, true but irrelevant, slip."),
  ("Not question", "Find the false option."),
  ("Calculations", "Formula, percentages, signs."),
  ("Time", "2 minutes each; leave and return."),
  ("Normative", "'Should' = value judgement.")]) + MCQ(mc_exam)

build("ex4", "as-paper1-technique", "Paper 1 Multiple Choice: Technique and Practice", EY,
  "How Paper 1 works, a 60 minute plan, the four-step method, how wrong options are built, nine question types with a way to attack each, and sixteen real past questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
