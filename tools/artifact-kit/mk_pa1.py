"""A Level exam technique: AO1 knowledge and understanding for Paper 3 and Paper 4. Run: python3 tools/artifact-kit/mk_pa1.py"""
from pa_common import *

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">AO1 is knowledge and understanding</b>: recalling facts, formulae and definitions, showing understanding with appropriate explanations and examples, and <b>applying</b> that knowledge to economic information in written, numerical and diagrammatic form. It is 35% of the A Level, <b>47% of Paper 3</b> and <b>33% of Paper 4</b>. On Paper 4 it is not marked on its own: in an essay it is combined with AO2 on the 14-mark Table A scale, and in Section A it earns most of the marks in the early parts. The most common reasons for losing it are imprecise terms, a diagram that is missing or wrong, and knowledge that is correct but never applied to the question's context. This page shows what earns it, with examples.</p></div>

  <h2>1 · Where AO1 marks are</h2>
  <div class="tw"><table class="t">
    <tr><th>Where</th><th>What AO1 looks like</th></tr>
    <tr><td><b>Paper 3</b> (30 questions, 30 marks)</td><td>Definitions, relationships, formulae and calculations; reading a table or a diagram and applying a concept to it.</td></tr>
    <tr><td><b>Paper 4 Section A</b>, early parts (usually 2 to 4 marks)</td><td>Identify, define, describe the data. One mark per accurate point, so short and precise answers score best.</td></tr>
    <tr><td><b>Paper 4 Section A</b>, later parts</td><td>Quoting the source accurately and using it. The source is there to be used, and doing so is application, which counts as AO1.</td></tr>
    <tr><td><b>Paper 4 essay</b> (20 marks)</td><td>Part of the 14-mark Table A scale, shared with AO2: accurate concepts, correct and labelled diagrams, and examples that support the explanation.</td></tr>
  </table></div>

  <h2>2 · The three strands of AO1</h2>
  <div class="grid2">
    <div class="card"><h3>Recall</h3><p>Facts, formulae, definitions. Know the exact meaning of terms such as allocative efficiency, the multiplier and the terms of trade, and what each formula measures.</p></div>
    <div class="card"><h3>Understanding</h3><p>An explanation or example that shows you know why, not just what. "A negative externality is a cost to a third party" is recall. Adding "so the market price is too low and output too high" shows understanding.</p></div>
    <div class="card"><h3>Application</h3><p>Using knowledge on the information in front of you: the passage, the table, the country, the good. This is the strand most students leave out, and it is the difference between a topic answer and an answer to this question.</p></div>
  </div>

  <h2>3 · What the three levels of Table A look like for knowledge</h2>
  <p class="note">In our words, from the pattern of the Paper 4 mark scheme. Markers award a best-fit level for the whole answer, with AO2.</p>
  <div class="tw"><table class="t">
    <tr><th>Level (of the 14 marks)</th><th>The knowledge looks like</th></tr>
    <tr><td><b>Level 3</b> (11 to 14)</td><td>Accurate concepts throughout, a correct and fully explained diagram, and examples or context that support the explanation.</td></tr>
    <tr><td><b>Level 2</b> (6 to 10)</td><td>Mostly accurate, but examples are limited or over-generalised, the diagram is thin or lightly used, or one required element is missing.</td></tr>
    <tr><td><b>Level 1</b> (1 to 5)</td><td>Some relevant knowledge with errors, no diagram or a wrong one, and little link to the question.</td></tr>
  </table></div>
  <div class="warn"><b class="h">Hard cap</b>If the question says "with the help of a diagram" and there is no correct, labelled diagram of the required type, the 14-mark scale is capped at Level 2. Draw the diagram the question names.</div>

  <h2>4 · Definitions that score</h2>
  <p>A precise definition has the term, the feature that matters and, if it helps, the contrast with its neighbour. Say it once, early, and move on.</p>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Imprecise</th><th>Precise</th></tr>
    <tr><td>Allocative efficiency</td><td>"Using resources well."</td><td>"Resources are allocated to the goods and services that society values most, where price equals marginal cost (or marginal social benefit equals marginal social cost)."</td></tr>
    <tr><td>Productive efficiency</td><td>"Producing a lot."</td><td>"Output is produced at the lowest possible average cost, at the minimum point of the average cost curve."</td></tr>
    <tr><td>Negative externality</td><td>"Pollution."</td><td>"A cost imposed on a third party that is not reflected in the market price, so social cost exceeds private cost."</td></tr>
    <tr><td>Economic growth</td><td>"The economy getting bigger."</td><td>"An increase in real GDP over time, or in potential output when the PPC shifts outwards."</td></tr>
    <tr><td>Structural unemployment</td><td>"People with no jobs."</td><td>"Unemployment caused by a mismatch between workers' skills or location and the jobs available, usually after a long-term change in the structure of demand."</td></tr>
    <tr><td>Absolute and relative poverty</td><td>"Being poor."</td><td>"Absolute poverty is income below the level needed for basic needs; relative poverty is income below a proportion of the typical income in that society."</td></tr>
  </table></div>

  <h2>5 · Formulae: what to write and what to avoid</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Formula</th><th>Marks lost by</th></tr>
    <tr><td>Price elasticity of demand</td><td>% change in quantity demanded ÷ % change in price</td><td>Forgetting that the sign is negative for most goods, or using absolute changes.</td></tr>
    <tr><td>Income elasticity of demand</td><td>% change in quantity demanded ÷ % change in income</td><td>Not saying what a negative value means (inferior good).</td></tr>
    <tr><td>Cross elasticity of demand</td><td>% change in quantity of A ÷ % change in price of B</td><td>Reversing A and B.</td></tr>
    <tr><td>The multiplier</td><td>1 ÷ (1 − MPC), or 1 ÷ (MPS + MPT + MPM)</td><td>Using the wrong marginal propensity or forgetting leakages.</td></tr>
    <tr><td>Terms of trade</td><td>(index of export prices ÷ index of import prices) × 100</td><td>Inverting the ratio.</td></tr>
    <tr><td>Percentage change</td><td>(new − old) ÷ old × 100</td><td>Dividing by the new value; saying "%" when it is percentage points.</td></tr>
  </table></div>

  <h2>6 · Diagrams: the marks are in the details</h2>
  <ul>
    <li><b>Axes:</b> label both, with the right names (price level and real GDP for AD/AS, not P and Q).</li>
    <li><b>Curves:</b> name each one (AD1, SRAS, MSC, MSB) and make the shape and slope correct.</li>
    <li><b>Equilibrium:</b> mark the original and the new points and project them to the axes.</li>
    <li><b>Shift:</b> use an arrow, say which curve moves and why.</li>
    <li><b>Context:</b> use the good, country or market in a label ("Market for coal-fired electricity").</li>
    <li><b>Match the model to the wording:</b> a consumption externality is not a production externality, a monopsony is not a competitive labour market, and an injections and withdrawals graph is not AD/AS.</li>
  </ul>

  <h2>7 · Application is AO1</h2>
  <div class="grid2">
    <div class="wrong-example">"Higher interest rates reduce investment and consumption."</div>
    <div class="right-example">"With household debt at a high share of income, a higher interest rate could raise repayments quickly, so consumption in this economy may fall more than the textbook suggests."</div>
  </div>
  <p>Two habits make this automatic. First, <b>quote the data</b> with number, unit and year: "GDP per head rose from $9,000 to $11,500 between 2015 and 2020". Second, run the <b>swap test</b>: change the country or the good in a paragraph. If it still reads correctly, it is not applied.</p>

  <h2>8 · Common ways to lose AO1 marks</h2>
  <ul>
    <li><b>Confusing neighbours:</b> equity and equality, production and productivity, free trade area and customs union, takeover and merger, a rise and a fall in the interest rate.</li>
    <li><b>No diagram, or the wrong one,</b> or one that is drawn and never mentioned.</li>
    <li><b>Defining everything,</b> so the first third of an essay earns nothing new.</li>
    <li><b>Leaving out part of the stem:</b> both markets, both income groups, the named policy.</li>
    <li><b>Quoting without using:</b> copying a figure from the data and not saying what it shows.</li>
    <li><b>Percent and percentage points mixed up,</b> or a missing unit.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For a short Section A part, write exactly what the command word asks for and stop. "Identify two" needs two short named points. "Define" needs the meaning, plus one extra feature if there are two marks. Spend the time you save on the last part.</div>
'''

watch = '''
  <h2>1 · From a bare definition to Level 3 knowledge</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A diagram, mark by mark</h2>
  <div id="stB"></div>
  <h2>3 · Quoting the data: from copying to using</h2>
  <div id="stC"></div>
'''

explore = chooser_html("h", "Lab 1 · Make the definition precise", "Choose a term to see an imprecise answer, a precise one and a question it might appear in.", ["Imprecise", "Precise", "Question it fits"]) + chooser_html("k", "Lab 2 · Formulae and their traps", "Choose a measure to see the formula, the usual slip and a worked check.", ["Formula", "The slip", "Worked check"]) + chooser_html("j", "Lab 3 · From topic knowledge to application", "Choose a topic to see a generic sentence and an applied one.", ["Generic", "Applied", "What was added"])

practise = '''
  <h2>1 · Recall, understanding or application?</h2><div id="cl1" class="card"></div>
  <h2>2 · Precise or imprecise?</h2><div id="cl2" class="card"></div>
  <h2>3 · Build a labelled diagram in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Terms get mixed up", "Examiner reports for Paper 4 list the same confusions each year: free trade area and customs union, takeover and merger, production and productivity, equity and equality, and a rise and a fall in interest rates.", "defining the key term in your opening sentence, precisely, and checking the stem for a near neighbour.") +
rw("Diagrams are the common cap", "Reports describe AD and AS curves labelled D and S, a negative output gap drawn as positive, a production externality drawn for air travel, and a competitive diagram used for a monopsony.", "matching the diagram to the exact wording of the question and labelling it with the context.") +
rw("Context gets ignored", "Reports describe an answer that treated cost-push inflation as demand-pull, and answers that left out the low-income country or the standard of living element of the question.", "putting the context nouns in every paragraph and running the swap test.") +
rw("Data is copied, not used", "In Section A, answers that quote the source without saying what it shows earn only part of the data marks. Answers that ignore a passage when the stem says 'using the information' lose marks.", "quoting the number, unit and year, and adding a few words on what it shows or cannot show.") +
rw("Missing parts of a long stem", "A question on productivity in perfect and imperfect labour markets was often answered for one market only, and mark schemes capped it.", "ticking off each element of the stem in your five-minute plan.")
)

mc_exam = [
  ("Which statement is a precise definition of productive efficiency?", ["Output is produced at the lowest possible average cost", "Firms make a large profit", "Resources are used in a way that is fair", "Output rises over time"], 0, "Productive efficiency is lowest average cost, at the minimum of the AC curve."),
  ("A firm's price elasticity of demand for its product is -2.5. A 4% price rise leads to what change in quantity demanded?", ["a fall of 10%", "a fall of 1.6%", "a rise of 10%", "a fall of 4%"], 0, "-2.5 × 4% = -10%."),
  ("The marginal propensity to consume is 0.75 and there are no other leakages. What is the multiplier?", ["4", "1.33", "0.75", "0.25"], 0, "1 ÷ (1 − 0.75) = 4."),
  ("The export price index is 120 and the import price index is 100. What is the terms of trade?", ["120", "83.3", "100", "20"], 0, "(120 ÷ 100) × 100 = 120, an improvement from a base of 100."),
  ("Unemployment rises from 5% to 6%. Which description is correct?", ["a rise of 1 percentage point", "a rise of 1%", "a rise of 6%", "a fall of 1 point"], 0, "A change in a rate is described in percentage points; in relative terms it is 20%."),
]

exam = exam_page("knowledge and understanding: how the marks are reached",
  exam_intro("Compare each of your answers with the mark scheme points, marked K for knowledge."),
  [("Section A early parts", "3 below", "Identify, define and describe-the-data questions, 2 to 4 marks"),
   ("Essay with a required diagram", "1 below", "20 marks, with the hard cap for a missing or wrong diagram"),
   ("Multiple choice (Paper 3 style)", "5 below", "Definitions, calculations and application")],
  [
  eq("Practice question", "2 marks", "Identify two ways in which a government could measure a country's economic development.",
     ["One mark for each valid measure, for example the Human Development Index, real GDP per head, the Gini coefficient or life expectancy.", "No explanation is needed, and no credit for repeating one measure in other words."],
     "Write two short items on two lines. Do not explain. Two marks need two different measures.",
     [[("k", "The Human Development Index. Real GDP per head.")]]),
  eq("Practice question", "3 marks", "Distinguish between absolute poverty and relative poverty.",
     ["One mark for a correct meaning of absolute poverty, for example income below the level needed for basic needs.", "One mark for a correct meaning of relative poverty, for example income below a proportion of the typical income in that society.", "One mark for the distinction: relative poverty can exist in a rich country and changes as incomes in society change, while absolute poverty relates to a fixed standard."],
     "Define each, then add the contrast in one sentence. Three marks, three sentences.",
     [[("k", "Absolute poverty is income below the level needed to meet basic needs such as food and shelter."), ("k", "Relative poverty is income below a set share of the typical income in that society."), ("k", "Relative poverty could remain in a wealthy country, whereas absolute poverty relates to a fixed standard of living.")]]),
  eq("Practice question", "4 marks", "Table: real GDP was $80bn in 2020 and $84bn in 2021; the population was 10 million in 2020 and 10.2 million in 2021. Calculate the percentage change in real GDP per head between 2020 and 2021.",
     ["One mark for real GDP per head in 2020 ($8,000) and one for 2021 (about $8,235).", "One mark for the correct percentage change formula and one for the answer, about 2.9%.", "Marks are for working, so show each step."],
     "Divide, then apply (new minus old) over old, times 100. State the unit.",
     [[("k", "GDP per head in 2020 = $80bn ÷ 10m = $8,000."), ("k", "In 2021 = $84bn ÷ 10.2m = about $8,235."), ("n", "The change is (8,235 − 8,000) ÷ 8,000 × 100 = about 2.9%.")]]),
  eq("Practice question", "20 marks (AO1 and AO2 on the 14-mark scale)", "With the help of a diagram, assess whether a tax on a good with a negative externality in production will make a market allocatively efficient.",
     ["Hard cap: a correct, labelled diagram of a production externality (MPC, MSC, demand) is needed to reach Level 3 on the 14-mark scale.", "Accurate definition of a negative externality in production and of allocative efficiency.", "Application to a named market, such as coal-fired electricity or a chemical plant.", "Evaluation (6 marks): the size of the tax against the external cost, elasticity, the difficulty of measuring the cost, and alternatives."],
     "Opening: define the externality and efficiency. Diagram with MPC, MSC, D. Chain: tax raises costs, supply shifts, output falls to the social optimum. Then evaluate and conclude.",
     [[("k", "A negative externality in production is a cost imposed on third parties that is not reflected in the firm's private cost."), ("a", "In a coal-fired power market, the diagram shows MSC above MPC."), ("n", "A tax equal to the external cost shifts MPC up to MSC, so output falls towards the social optimum.")]]),
  ],
  )

tips = tips_html(
  [("Say it precisely, once.", "One definition, early, with the feature that matters."),
   ("Draw what the stem names.", "Right model, right axes, labelled with the context."),
   ("Use the data.", "Number, unit and year, then what it shows."),
   ("Check the units.", "Percent against percentage points."),
   ("Cover every element of the stem.", "Both markets, both groups, the named policy."),
   ("Short parts need short answers.", "Write what the command word asks for and stop.")],
  [("Defining a term", "X is [what it is], which means [the feature that matters]."),
   ("Using the data", "The source shows that [figure, unit, year], which means [what it shows]."),
   ("Referring to the diagram", "In the diagram, the shift from X1 to X2 raises [variable] from A to B."),
   ("Stating a limit", "The data cover only [period or group], so they cannot show [what is missing].")],
  [CW["define"], CW["explain"], CW["analyse"], CW["assess"]]) + FC

js = CHAINJS + STRIP + '''
strip("#pic1", "A precise definition has three parts", [["The term", "name it exactly"], ["The feature", "the idea that matters"], ["The contrast", "how it differs from its neighbour"]]);
chainStep("#stA", "From a bare definition to Level 3 knowledge", ["Bare: 'A negative externality is pollution.'", "Precise: 'A cost to a third party not in the market price.'", "Add the effect: 'So social cost exceeds private cost.'", "Add the context: 'In coal-fired power, the cost is local air pollution.'", "Add the diagram: MPC, MSC, D labelled for the market"],
  ["<b>Level 1 knowledge:</b> an example is not a definition.", "<b>Accurate:</b> third party and 'not in the price' are the key features.", "<b>Understanding:</b> the consequence shows you know why it matters.", "<b>Application:</b> the market named in the question.", "<b>Level 3:</b> accurate, applied and drawn."]);
chainStep("#stB", "A diagram, mark by mark", ["Label both axes: price level and real GDP", "Draw and name AD1 and SRAS", "Mark the equilibrium and project to both axes", "Shift AD to AD2 with an arrow and say why", "Mark the new equilibrium and the change in price level and output"],
  ["<b>Axes:</b> price level and real GDP, not P and Q.", "<b>Curves:</b> named, with the correct slope.", "<b>Equilibrium:</b> original point P1, Y1.", "<b>Shift:</b> one curve moves, with a reason.", "<b>Result:</b> new equilibrium, and the text refers to it."]);
chainStep("#stC", "Quoting the data: from copying to using", ["Copy: 'Exports were $12bn.'", "Add unit and year: 'Exports were $12bn in 2022.'", "Add the change: 'up from $9bn in 2019, a rise of 33%.'", "Say what it shows: 'so export growth outpaced GDP growth.'", "Say what it cannot show: 'but it says nothing about export prices.'"],
  ["<b>Copying</b> earns little.", "<b>Precise</b> but still only a fact.", "<b>Calculation</b> turns it into evidence.", "<b>Interpretation</b> makes it analysis.", "<b>Limit</b> is the start of evaluation."]);

chooser("h", [
  ["Allocative efficiency", "Using resources well.", "Resources go to the goods society values most, where price equals marginal cost.", "Define allocative efficiency (2 marks).", 5],
  ["Positive externality", "Something good for society.", "A benefit to a third party that is not reflected in the price, so social benefit exceeds private benefit.", "What is meant by a positive externality (2 marks)?", 4],
  ["Structural unemployment", "People with no jobs.", "Unemployment from a mismatch between skills or location and the jobs available after a lasting change in demand.", "Distinguish between structural and cyclical unemployment (3 marks).", 4],
  ["Comparative advantage", "Being better at making something.", "A country can produce a good at a lower opportunity cost than another country.", "Explain comparative advantage (4 marks).", 5],
  ["Government failure", "When the government makes mistakes.", "Government intervention that leads to a net welfare loss, or a less efficient allocation of resources than before.", "What is meant by government failure (2 marks)?", 4]
], (it) => `${it[0]}. Imprecise: "${it[1]}" Precise: "${it[2]}" Fits: ${it[3]}`, "How often this is tested");
chooser("k", [
  ["PED", "% change in quantity demanded ÷ % change in price", "Reversing the fraction, or using absolute changes", "Price up 10%, quantity down 15%: PED = -15 ÷ 10 = -1.5, which is elastic.", 5],
  ["YED", "% change in quantity demanded ÷ % change in income", "Not stating what a negative value means", "Income up 5%, quantity down 2%: YED = -0.4, so an inferior good.", 4],
  ["XED", "% change in quantity of A ÷ % change in price of B", "Using the price of A in the denominator", "Price of B up 10%, quantity of A up 6%: XED = +0.6, so the goods are substitutes.", 4],
  ["Multiplier", "1 ÷ (1 − MPC)", "Using MPC in the denominator, or ignoring withdrawals", "MPC 0.8: k = 1 ÷ 0.2 = 5, so a $2bn injection could raise income by up to $10bn.", 5],
  ["Terms of trade", "Export price index ÷ import price index × 100", "Inverting the fraction", "Exports 110, imports 125: 88, a deterioration.", 4]
], (it) => `${it[0]}: ${it[1]}. Slip: ${it[2]}. Check: ${it[3]}`, "How often this is tested");
chooser("j", [
  ["Interest rates", "A higher interest rate reduces consumption.", "With most borrowing at variable rates, a higher rate could raise repayments quickly, so consumption in this economy may fall sharply.", "The country's borrowing at variable rates", 5],
  ["Exchange rate", "A depreciation makes exports cheaper.", "A depreciation lowers the price of the country's coffee exports in dollars, which could raise sales if foreign demand is elastic.", "The named export and its buyers", 5],
  ["Tax", "A tax reduces demand for a product.", "A 20% tax on cigarettes could cut the quantity bought by long-term smokers only slightly if their demand is inelastic.", "The good, the group and the figure", 4],
  ["Subsidy", "A subsidy lowers costs.", "A subsidy on electric vehicles lowers the price to buyers in this market, shifting supply right and raising sales.", "The market named in the question", 4],
  ["Inflation", "Inflation reduces purchasing power.", "With prices rising 8% a year and wages up 3%, real incomes in this country are falling, particularly for pensioners.", "The figures in the source", 5]
], (it) => `${it[0]}. Generic: "${it[1]}" Applied: "${it[2]}" Added: ${it[3].toLowerCase()}.`, "Application marks earned");
''' + CLASSIFY("cl1", "Recall, understanding or application?", ["Recall", "Understanding", "Application"],
  [("Real GDP is GDP adjusted for inflation.", 0), ("A tax raises the cost of production, so supply shifts left and price rises.", 1), ("Between 2019 and 2022 this country's exports rose from $9bn to $12bn.", 2), ("The multiplier is 1 ÷ (1 − MPC).", 0), ("Because this economy's MPC is 0.6, the $5bn project is likely to raise income by about $12.5bn.", 2), ("A merger reduces competition because it removes a rival.", 1)],
  "Recall states the fact, understanding explains it, application uses the information given.") + CLASSIFY("cl2", "Precise or imprecise?", ["Imprecise", "Precise"],
  [("Inflation is when things get expensive.", 0), ("Inflation is a sustained rise in the general price level over time.", 1), ("An externality is pollution.", 0), ("An externality is a cost or benefit to a third party that is not reflected in the market price.", 1), ("Productive efficiency is producing a lot.", 0), ("Productive efficiency is producing at the lowest average cost.", 1)],
  "A precise definition names the feature that matters.") + ORDER(
  "Put the steps for drawing a diagram in order.",
  ["Label the axes", "Draw and name the curves", "Mark the original equilibrium", "Shift the curve with an arrow and a label", "Mark the new equilibrium", "Write a sentence that refers to the shift"],
  "Axes, curves, equilibrium, shift, new equilibrium, then use it in the text.") + MATCH([
  ["Allocative efficiency", "Price equals marginal cost"],
  ["Productive efficiency", "Output at the minimum of average cost"],
  ["Negative externality", "A cost to a third party not in the price"],
  ["Structural unemployment", "A mismatch of skills or location with the jobs available"],
  ["Terms of trade", "Export price index ÷ import price index × 100"],
  ["Multiplier", "1 ÷ (1 − MPC)"]]) + CALC([
  {"q": "A price rise of 8% reduces quantity demanded by 12%. Calculate PED (1 decimal place, with sign).", "a": -1.5, "unit": "", "tol": 0.05, "hint": "-12 ÷ 8.", "sol": "<b>-1.5</b>, elastic."},
  {"q": "MPC is 0.9 and there are no other leakages. Calculate the multiplier.", "a": 10, "unit": "", "tol": 0.05, "hint": "1 ÷ (1 − 0.9).", "sol": "<b>10</b>."},
  {"q": "Export prices index 130, import prices index 104. Calculate the terms of trade.", "a": 125, "unit": "", "tol": 0.2, "hint": "130 ÷ 104 × 100.", "sol": "<b>125</b>, an improvement."},
  {"q": "Real GDP rises from $200bn to $208bn. Calculate the percentage change.", "a": 4, "unit": "%", "tol": 0.05, "hint": "8 ÷ 200.", "sol": "<b>4%</b>."}]) + MCQ([
  ("A diagram is asked for and none is drawn. What is the likely effect on a 20-mark essay?", ["The 14-mark scale is capped at Level 2", "No effect", "The essay is marked out of 10", "The evaluation marks are lost"], 0, "Missing required diagrams cap the 14-mark scale at Level 2."),
  ("Which sentence shows application?", ["Exports rose from $9bn in 2019 to $12bn in 2022, so they grew faster than GDP.", "Exports are goods sold abroad.", "Exports are a component of AD.", "Exports can rise or fall."], 0, "It uses the information in the source."),
  ("Which is the most precise definition?", ["Allocative efficiency occurs where price equals marginal cost.", "Allocative efficiency means being efficient.", "Allocative efficiency is good for society.", "Allocative efficiency is about prices."], 0, "It names the condition."),
  ("Unemployment falls from 6.0% to 5.5%. Which is correct?", ["A fall of 0.5 percentage points", "A fall of 0.5%", "A fall of 5.5%", "A rise of 0.5 points"], 0, "Rates change in percentage points."),
  ("For a 2-mark 'identify two' part, the best answer is:", ["Two short named points", "A paragraph of analysis", "One long sentence", "A diagram"], 0, "Identify needs names, not explanation.")
], "qz1") + CARDS([
  ("AO1", "Recall, understanding, application."),
  ("Weighting", "35% overall, 33% of Paper 4, 47% of Paper 3."),
  ("Diagram cap", "No required diagram: 14-mark scale capped at Level 2."),
  ("Percentage points", "For changes in a rate."),
  ("Swap test", "Change the country. If it still reads, it is not applied."),
  ("Define once", "Early, precisely, then move on."),
  ("Quote data", "Number, unit, year, what it shows."),
  ("Multiplier", "1 ÷ (1 − MPC).")]) + MCQ(mc_exam)

build("pa1", "a-level-ao1-knowledge", "AO1 Knowledge and Understanding: How Paper 4 Marks Are Earned", EYP,
  "What earns AO1 marks on Paper 3 and Paper 4: precise definitions, formulae, labelled diagrams, using the data, and what Level 1, 2 and 3 knowledge looks like. Animations, labs and practice.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
