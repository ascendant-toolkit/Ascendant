"""AS exam technique: AO1 knowledge and understanding, how marks are earned. Run: python3 tools/artifact-kit/mk_ex1.py"""
from as6k import *
EY = "AS Level Economics · 9708 · Exam technique"

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">AO1 is knowledge and understanding</b>: showing knowledge of syllabus content (facts, formulae and definitions), demonstrating understanding with <b>appropriate explanations and examples</b>, and <b>applying knowledge and understanding to economic information</b> in written, numerical and diagrammatic form. In the 8 mark part of Paper 2 it is worth <b>3 marks</b> (for papers up to 2022, 2 marks), in the 12 mark part it is combined with analysis in <b>Table A out of 8</b>, in the short data response parts it earns the marks for definitions, comparisons and calculations, and in <b>Paper 1</b> it is tested in every question. Marks are earned for <b>precise definitions</b>, <b>correct formulae</b>, <b>accurately drawn and labelled diagrams</b>, <b>correct calculations</b> and <b>explanations that show a concept is understood</b>, and the generic marking principles say examiners <b>do not credit a key term simply for being used</b> unless there is evidence that it is understood. This page shows what earns each AO1 mark and what separates a Level 1, 2 and 3 knowledge base in a 12 mark answer.</p></div>

  <h2>1 · Where AO1 marks are</h2>
  <div class="tw"><table class="t">
    <tr><th>Where</th><th>AO1 marks</th><th>What they reward</th></tr>
    <tr><td><b>Paper 1</b> (30 questions, 30 marks)</td><td>Throughout</td><td>Recall of definitions and relationships, calculations, and applying a concept to a short scenario or table</td></tr>
    <tr><td><b>Paper 2 data response (a) and (b)</b></td><td>2 each</td><td>Explicit comparison of data, a definition or meaning of a term, a short calculation</td></tr>
    <tr><td><b>Essay part (a)</b> (8 marks)</td><td>3 (2 in papers up to 2022)</td><td>Definition, formula, diagram, distinction between terms: the marks the question text asks for ("with the help of a formula", "with the help of a diagram")</td></tr>
    <tr><td><b>Essay part (b)</b> (12 marks)</td><td>Shared with AO2 in Table A (8)</td><td>Detailed, accurate knowledge and understanding of the relevant concepts, supported by examples</td></tr>
  </table></div>

  <h2>2 · What earns the three AO1 marks in an 8 mark part</h2>
  <p>The mark scheme for the 8 mark part lists the AO1 points. They are almost always <b>a definition, a formula or distinction, and a diagram or a developed meaning</b>. Real examples:</p>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>The three AO1 marks (from the mark scheme)</th></tr>
    <tr><td>Price elasticity of demand, "with the help of a formula"</td><td>(1) It measures the responsiveness of demand to a change in price; (1) the correct formula; (1) the meaning of price elastic and inelastic in terms of percentage or proportionate responses</td></tr>
    <tr><td>Income elasticity of demand, "with the help of a formula"</td><td>(1) An accurate definition; (1) an accurate formula; (1) the difference between normal and inferior goods</td></tr>
    <tr><td>Cross elasticity of demand</td><td>(1) What it measures; (1) the formula; (1) the distinction between positive and negative XED</td></tr>
    <tr><td>Terms of trade</td><td>(1) The ratio of the export price index to the import price index; (1) it measures the number of exports sold to buy a given number of imports; (1) it improves when the ratio rises and deteriorates when it falls</td></tr>
    <tr><td>Depreciation of the exchange rate</td><td>(1) An accurate definition of the exchange rate; (1) a depreciation is likely if demand for the currency falls; (1) or if its supply increases</td></tr>
    <tr><td>Effect of a change in a subsidy, "with the help of a diagram"</td><td>(1) Axes and curves correctly labelled; (1) an increase in subsidy shifts supply right, price falls and quantity rises, new equilibria shown; (1) a decrease shifts supply left, price rises and quantity falls</td></tr>
    <tr><td>Demand-pull and cost-push inflation</td><td>(1) Inflation as a sustained rise in the general price level; (1) cost-push defined; (1) demand-pull defined and distinguished</td></tr>
    <tr><td>Circular flow, open economy, "with the help of a diagram"</td><td>(1) The components of AD or the flows; (1) an accurately labelled diagram with equilibrium; (1) the shifts and their effects</td></tr>
  </table></div>
  <p><b>The pattern:</b> every item in the question ("with the help of a formula", "explain the difference between", "with a diagram") tells you what AO1 marks are available. If you leave one out, you lose a mark that no amount of analysis will replace.</p>

  <h2>3 · The quality of a definition: 0, 1 and full marks</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Not enough (no credit)</th><th>Partial</th><th>Full credit</th></tr>
    <tr><td><b>Price elasticity of demand</b></td><td>"How elastic demand is."</td><td>"How much demand changes when price changes."</td><td>"The responsiveness of quantity demanded to a change in price, measured as the percentage change in quantity demanded divided by the percentage change in price."</td></tr>
    <tr><td><b>Opportunity cost</b></td><td>"The cost of something."</td><td>"What you give up."</td><td>"The value of the next best alternative that is given up when a choice is made."</td></tr>
    <tr><td><b>Merit good</b></td><td>"A good that is good for you."</td><td>"A good that is under-consumed."</td><td>"A good that is more beneficial to consumers than they realise, so it is under-consumed and under-provided by the free market, such as education."</td></tr>
    <tr><td><b>Inflation</b></td><td>"Prices going up."</td><td>"A rise in prices."</td><td>"A sustained rise in the general price level."</td></tr>
    <tr><td><b>Real GDP</b></td><td>"GDP in real terms."</td><td>"GDP adjusted for prices."</td><td>"GDP adjusted for inflation, so that it shows the change in the quantity of output."</td></tr>
  </table></div>
  <p><b>What full credit needs:</b> the <b>key idea</b> (what it measures or is), the <b>qualifier</b> (the direction, the units or the condition) and, where the question allows, a <b>short example</b> or the <b>formula</b>. Repeating the term in the definition ("elastic demand is demand that is elastic") earns nothing.</p>

  <h2>4 · AO1 in Table A: Levels 1, 2 and 3 of knowledge</h2>
  <p>In the 12 mark question the knowledge and understanding in Table A is judged on <b>how many relevant concepts, how accurately and how well explained</b>. Take the question <i>Assess whether the consequences of free trade are always positive for an economy.</i></p>
  <div class="card"><h3>Level 1 knowledge: 1 to 2 marks (about 40 words)</h3>
  <p>Free trade is when countries trade. It means goods are cheaper. Some firms might lose out.</p>
  <p class="note"><b>Why Level 1:</b> a small number of relevant points, each only named; the definition is imprecise (trade, not trade without barriers); no concept is explained and nothing supports the points.</p></div>
  <div class="card"><h3>Level 2 knowledge: 3 to 5 marks (about 100 words)</h3>
  <p>Free trade is trade between countries without barriers such as tariffs. It lets countries specialise in what they are good at, so output rises and consumers get cheaper goods and more choice. Free trade can lead to unemployment in industries that cannot compete. Some countries may depend on a few exports.</p>
  <p class="note"><b>Why Level 2:</b> several relevant concepts (specialisation, choice, unemployment, dependence), generally accurate, but they are <b>over-generalised</b> ("what they are good at" is not comparative advantage; no explanation of why unemployment is structural; no example).</p></div>
  <div class="card"><h3>Level 3 knowledge: 6 to 8 marks (about 220 words, with the analysis)</h3>
  <p>Free trade is trade between countries without barriers such as tariffs and quotas. It allows countries to <b>specialise in goods in which they have a comparative advantage</b>, meaning a lower <b>opportunity cost</b>, so that total output rises and each country can consume beyond its production possibility curve. Consumers gain a wider choice and lower prices, firms gain <b>economies of scale</b> from larger markets, and competition raises efficiency. The costs include <b>structural unemployment</b> when industries decline because workers cannot easily change occupation, <b>over-specialisation</b> and dependence on a few commodities whose prices fall, as with countries that rely on one crop, and a possible <b>current account deficit</b> if imports rise faster than exports. Whether free trade is positive depends on <b>factor endowments</b>, how <b>open</b> the economy already is, and its <b>stage of development</b>...</p>
  <p class="note"><b>Why Level 3:</b> detailed, accurate knowledge of the concepts the question needs (comparative advantage, opportunity cost, structural unemployment, current account), each with an explanation and an example. The knowledge is relevant to <b>this</b> question, not a dump of everything known about trade.</p></div>
  <div class="tw"><table class="t">
    <tr><th>AO1 in Table A</th><th>Level 1</th><th>Level 2</th><th>Level 3</th></tr>
    <tr><td><b>Number of relevant concepts</b></td><td>A small number</td><td>Some</td><td>All that the question needs</td></tr>
    <tr><td><b>Accuracy</b></td><td>Significant errors or omissions</td><td>Over-generalised or some inaccuracies</td><td>Accurate</td></tr>
    <tr><td><b>Explanation and examples</b></td><td>Named, not explained</td><td>Limited</td><td>Relevant explanations supported by examples</td></tr>
    <tr><td><b>Use of terms</b></td><td>Everyday language</td><td>Some precise terms</td><td>Precise throughout</td></tr>
  </table></div>

  <h2>5 · Diagrams: the marking points</h2>
  <div class="tw"><table class="t">
    <tr><th>Diagram</th><th>What to include for the AO1 marks</th></tr>
    <tr><td><b>Supply and demand (shift)</b></td><td>Axes labelled (price, quantity), curves labelled D and S, original equilibrium, the shifted curve labelled (S1), new equilibrium with P and Q marked</td></tr>
    <tr><td><b>Indirect tax or subsidy</b></td><td>The two supply curves, the vertical distance equal to the tax or subsidy, the price paid by consumers and received by producers, the tax revenue or cost area</td></tr>
    <tr><td><b>Maximum or minimum price</b></td><td>The control line on the correct side of equilibrium, quantity demanded and supplied at that price, the shortage or surplus</td></tr>
    <tr><td><b>AD/AS</b></td><td>Axes (price level, real output), AD, SRAS (and LRAS if relevant), equilibrium, the shifted curve and the new price level and output</td></tr>
    <tr><td><b>Currency market</b></td><td>Axes (exchange rate, quantity of currency), demand and supply of the currency, the shift and the new rate</td></tr>
    <tr><td><b>PPC</b></td><td>Axes (two goods), a concave curve, points inside, on and outside, labelled</td></tr>
    <tr><td><b>Tariff</b></td><td>Domestic S and D, world price, price with tariff, quantities supplied, demanded and imported before and after</td></tr>
  </table></div>
  <p class="note">A diagram earns AO1 marks for accuracy and labelling. It earns <b>analysis</b> marks only when the answer <b>uses and explains</b> it in the text: refer to "the shift from S to S1" in your sentences.</p>

  <h2>6 · Formulae to know, with units</h2>
  <div class="tw"><table class="t">
    <tr><th>Concept</th><th>Formula</th><th>Notes</th></tr>
    <tr><td>Price elasticity of demand</td><td>% change in quantity demanded ÷ % change in price</td><td>Negative; discuss the size</td></tr>
    <tr><td>Income elasticity of demand</td><td>% change in quantity demanded ÷ % change in income</td><td>Sign: normal or inferior</td></tr>
    <tr><td>Cross elasticity of demand</td><td>% change in quantity of X ÷ % change in price of Y</td><td>Sign: substitute or complement</td></tr>
    <tr><td>Price elasticity of supply</td><td>% change in quantity supplied ÷ % change in price</td><td>Positive</td></tr>
    <tr><td>Total revenue</td><td>Price × quantity</td><td>Same as consumer expenditure</td></tr>
    <tr><td>Terms of trade</td><td>(Export price index ÷ import price index) × 100</td><td>No units</td></tr>
    <tr><td>Real GDP</td><td>Nominal GDP ÷ price index × 100</td><td>Adjusts for inflation</td></tr>
    <tr><td>GDP (expenditure)</td><td>C + I + G + (X − M)</td><td>GNI = GDP + net primary income; NNI = GNI − depreciation</td></tr>
    <tr><td>Unemployment rate</td><td>Unemployed ÷ labour force × 100</td><td>Labour force = employed + unemployed</td></tr>
    <tr><td>Inflation rate</td><td>(CPI now − CPI before) ÷ CPI before × 100</td><td>Percentage change in the index</td></tr>
    <tr><td>Marginal and average rate of tax</td><td>MRT = change in tax ÷ change in income; ART = total tax ÷ total income</td><td>Progressive: MRT above ART</td></tr>
    <tr><td>Current account balance</td><td>Goods + services + primary income + secondary income</td><td>Negative is a deficit</td></tr>
    <tr><td>Real interest rate</td><td>Nominal rate − inflation rate</td><td>Approximate</td></tr>
  </table></div>

  <h2>7 · Calculations: how the marks go</h2>
  <ul>
    <li>The mark scheme shows the <b>steps</b>, the <b>mark for each step</b> and the <b>mark for the answer</b>. Write the formula, substitute the figures, then give the answer with the unit.</li>
    <li>Unless the question says working is needed, a <b>correct final answer earns full marks</b> even without working; but if the answer is wrong, working earns the method marks.</li>
    <li>The <b>own figure rule</b>: if you use an incorrect figure from earlier in the question, you can still earn the later marks for a correct method.</li>
    <li>Check <b>percentage or percentage point</b>, the <b>sign</b> (a deficit is negative) and whether to <b>round</b> as instructed.</li>
  </ul>

  <h2>8 · Common ways to lose AO1 marks</h2>
  <ul>
    <li><b>Confusing terms:</b> deficit and debt, GDP and GNI, flow and stock, movement along and shift of a curve, budget deficit and current account deficit, real and nominal.</li>
    <li><b>Imprecise definitions:</b> "how much demand changes" for elasticity, with no mention of percentages or price.</li>
    <li><b>Leaving out what the question asked for:</b> no formula when it says "with the help of a formula", no diagram when it says so.</li>
    <li><b>Unlabelled or wrong diagrams:</b> missing axes, a demand curve that slopes the wrong way, a shift in the wrong direction.</li>
    <li><b>Knowledge dumping:</b> writing everything known about a topic, which does not earn Level 3 unless it answers the question.</li>
    <li><b>Using a key term without showing understanding.</b></li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Underline every "with the help of", "define" and "explain the difference" in the question: each is an AO1 mark you can bank. Learn the definitions word for word, and write the formula first in any calculation.</div>
'''

watch = '''
  <h2>1 · Building a full-mark definition</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · The three AO1 marks for an elasticity answer</h2>
  <div id="stB"></div>
  <h2>3 · Drawing a diagram for full marks</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · AO1 marks in an elasticity answer</h2>
  <p>Tick what your answer includes. The lab shows the AO1 marks (out of 3), using the mark scheme pattern for a "with the help of a formula" question.</p>
  <div class="card"><div class="grid2"><div id="chk"></div>
    <div><div class="readout"><div><small>AO1 marks (out of 3)</small><strong id="r1"></strong></div><div><small>Still missing</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div></div></div>
''' + chooser_html("h", "Lab 2 · Definition checker", "Choose a term to see the weak, partial and full-mark definitions.", ["Weak (no credit)", "Partial", "Full credit"]) + chooser_html("k", "Lab 3 · What would a diagram earn?", "Choose a diagram to see the marking points and common slips.", ["Marking points", "Common slip", "Marks at stake"])

practise = '''
  <h2>1 · AO1, AO2 or AO3?</h2><div id="cl1" class="card"></div>
  <h2>2 · Full-mark definition or not?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the calculation steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the formula to the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("An explicit comparison", "A 2 mark data part asked students to compare changes in two series. The mark scheme said marks were for an explicit comparison, not for describing each in turn: 'the inflation rate rose then fell while the interest rate rose continuously'.", "comparing, not describing twice.") +
rw("Real GDP in two marks", "Asked what is meant by real GDP, the answer needs GDP and the adjustment for inflation (or prices). 'GDP in real terms' is not enough.", "a precise definition with the qualifier.") +
rw("The formula mark", "In several 8 mark parts a mark is given for the correct formula, such as percentage change in quantity demanded divided by percentage change in price. Writing 'quantity over price' loses it.", "learning formulae exactly.") +
rw("Distinguish questions", "A 'distinguish between a budget deficit and a current account deficit' question gave one mark for each side: government spending exceeds revenue, and payments to the rest of the world exceed receipts.", "one mark per term, so define both.") +
rw("A calculation with steps", "An extract question on GNI and NNI awards a mark for adding net primary income and a mark for subtracting depreciation; a student who writes the steps can earn marks even if the final number is wrong.", "showing working for method marks.")
)

mc_exam = [
  mcq("s20_13", 3, "Which type of good is healthcare?", ["demerit", "free", "merit", "public"], 2, "Healthcare is more beneficial than consumers realise, so it is a merit good."),
  mcq("s20_11", 18, "What is a necessary characteristic of a public good?", ["It has a fixed maximum price.", "It has an opportunity cost of production of zero.", "It is non-excludable.", "It is an essential good."], 2, "Non-excludability is a defining characteristic."),
  mcq("m22_12", 8, "What is the measure of cross-elasticity of demand for good X in terms of good Y?", ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], 2, "A percentage formula, with X's demand on top and Y's price below."),
  mcq("s25_12", 3, "What is a statement of the non-rivalrous nature of public goods?", ["It is not possible to stop a non-payer from using the product.", "One person consuming the product does not reduce the amount of it available to others.", "People consume too little of the product because they are unaware of its true benefits.", "There is an unlimited supply of the product."], 1, "Non-rival means one person's use does not reduce what is available to others."),
  mcq("w20_12", 2, "Which statement is correct?", ["Private goods are both non-rival and non-excludable.", "Private goods are only provided by the private sector.", "Public goods are both non-rival and non-excludable.", "Public goods do not incur opportunity costs."], 2, "A definition recall question."),
  mcq("m23_12", 2, "What is the definition of long run?", ["the time period when all factors of production are specialised", "the time period when all factors of production are variable", "the time period when all key inputs into production are variable", "the time period when at least one factor of production is fixed"], 1, "In the long run all factors can be varied."),
  mcq("s24_13", 1, "What is not an example of a public good?", ["education", "flood control systems", "national defence", "street lighting"], 0, "Education is a merit good.")
]

exam = exam_page("knowledge and understanding: how AO1 marks are earned",
  "We chose past questions where the mark scheme spells out the AO1 marks: 8 mark parts that ask for a formula, a definition or a distinction, and short data response parts for meanings and comparisons. Open each key and find the knowledge marks (K), then check them against your own definitions.",
  exam_rows([("s25_24","2(a)",8),("m24_22","3(a)",8),("s23_21","3(a)",8),("s24_23","5(a)",8),("s20_23","1(b)",2),("s25_24","1(b)",2),("w23_23","1(a)",2),("w20_21","1(d)",2),("w24_21","1(b)",2),("s20_22","1(c)(i)",2)], ["s20_13","s20_11","m22_12","s25_12","w20_12","m23_12","s24_13"]),
  [
  grab("s25_24", "2(a)"),
  grab("m24_22", "3(a)"),
  grab("s23_21", "3(a)"),
  grab("s24_23", "5(a)"),
  grab("s20_23", "1(b)"),
  grab("s25_24", "1(b)"),
  grab("w23_23", "1(a)"),
  grab("w20_21", "1(d)"),
  grab("w24_21", "1(b)"),
  grab("s20_22", "1(c)(i)")
  ],
  )

tips = tips_html(
  [("Learn definitions word for word.", "Key idea, qualifier, example."),
   ("Write the formula first.", "In words or symbols, exactly."),
   ("Do what 'with the help of' asks.", "Each phrase is a mark."),
   ("Label every diagram.", "Axes, curves, equilibrium, shift."),
   ("Show working.", "Method marks and the own figure rule."),
   ("Explain, don't just name.", "A key term alone earns nothing."),
   ("Match knowledge to the question.", "Relevant concepts, not everything you know.")],
  [("AO1", "AO1 is knowledge and understanding: definitions, formulae and explanations."),
   ("Definition", "A precise definition gives the key idea and the qualifier."),
   ("Formula", "State the formula exactly, such as percentage change in quantity demanded divided by percentage change in price."),
   ("Diagram", "A diagram must have labelled axes and curves to earn marks."),
   ("Application", "AO1 includes applying knowledge to written, numerical and diagrammatic information.")],
  [CW["define"], CW["explain"], CW["calculate"] if "calculate" in CW else CW["explain"], CW["distinguish"] if "distinguish" in CW else CW["explain"]]) + FC

js = SDJS + CHAINJS + '''
chainStep("#stA", "Building a full-mark definition: price elasticity of demand", ["Start with the idea: the responsiveness of quantity demanded to a change in price", "Add the measure: percentage change in quantity demanded divided by percentage change in price", "Add the size meaning: elastic if the percentage change in quantity is greater than the change in price", "Check: no repeating the term, no vague words like 'how much'"], [
  "<b>Key idea (1 mark).</b>", "<b>Formula (1 mark).</b>", "<b>Meaning of elastic and inelastic in percentage terms (1 mark).</b>", "<b>Three AO1 marks</b> for a full answer."]);
chainStep("#stB", "The three AO1 marks for an elasticity answer", ["Mark 1: what it measures: responsiveness of demand to price", "Mark 2: the correct formula", "Mark 3: elastic and inelastic in percentage terms", "Then move to analysis: effect on revenue; evaluation: elasticity changes along the curve"], [
  "<b>Meaning.</b>", "<b>Formula.</b>", "<b>Interpretation.</b>", "<b>AO1 is the base; analysis builds on it.</b>"]);
const dgLab = { x: "Quantity", y: "Price", D1: "D", S1: "S", S2: "S1", P1: "P", Q1: "Q", P2: "P1", Q2: "Q1" };
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Drawing a subsidy diagram for the AO1 marks", base: { s: 0, n: 0, g: 0 }, draw: (s) => sdPlot({ d: 0, s: s.s, g: s.g, n: s.n }, dgLab), tween: 800, dwell: 5200, steps: [
  { cap: "<b>1 mark:</b> axes labelled (price, quantity); D and S labelled; original equilibrium shown with P and Q marked.", s: { s: 0, n: 0, g: 1 } },
  { cap: "<b>An increase in subsidy shifts supply to the right</b> (to S1): costs fall.", s: { s: 20, n: 1, g: 1 } },
  { cap: "<b>Mark the new equilibrium</b> (P1, Q1): price falls and quantity rises. This earns the diagram mark; the analysis marks need the explanation in words.", s: { s: 20, n: 1, g: 1 } },
] });

function ao1() {
  const items = [["m", "What it measures: the responsiveness of quantity demanded to a change in price"], ["f", "The correct formula: % change in quantity demanded ÷ % change in price"], ["i", "Elastic and inelastic explained in percentage terms"], ["x", "A vague phrase like 'how much demand changes' only"], ["e", "An example with no definition"]];
  const on = items.map((it, i) => !!$("#ck" + i) && $("#ck" + i).checked);
  const m = on[0] ? 1 : 0, f = on[1] ? 1 : 0, i = on[2] ? 1 : 0, total = m + f + i;
  $("#r1").textContent = total + " / 3";
  const miss = [m ? "" : "meaning", f ? "" : "formula", i ? "" : "elastic and inelastic in % terms"].filter(Boolean);
  $("#r2").textContent = miss.length ? miss.join(", ") : "Nothing: full AO1 marks";
  $("#rv").textContent = `Ticked: ${on.filter(Boolean).length} item(s). ` + (on[3] && !on[0] ? "A vague phrase is not credited as the meaning. " : "") + (on[4] && !on[0] ? "An example without a definition does not earn the meaning mark. " : "") + (total === 3 ? "All three AO1 marks are earned; the next step is analysis (the effect on revenue) and evaluation." : `${total} AO1 mark(s). Add: ${miss.join("; ")}.`);
}
$("#chk").innerHTML = ["What it measures: the responsiveness of quantity demanded to a change in price", "The correct formula: % change in quantity demanded ÷ % change in price", "Elastic and inelastic explained in percentage terms", "A vague phrase like 'how much demand changes' only", "An example with no definition"].map((t, i) => `<label style="display:block;margin:6px 0"><input type="checkbox" id="ck${i}"> ${t}</label>`).join("");
[0, 1, 2, 3, 4].forEach((i) => ($("#ck" + i).onchange = ao1));
ao1();

chooser("h", [
  ["Price elasticity of demand", "How elastic demand is.", "How much demand changes when price changes.", "The responsiveness of quantity demanded to a change in price: % change in quantity demanded ÷ % change in price.", 5],
  ["Opportunity cost", "The cost of something.", "What you give up.", "The value of the next best alternative given up when a choice is made.", 4],
  ["Merit good", "A good that is good for you.", "A good that is under-consumed.", "A good more beneficial than consumers realise, so under-consumed and under-provided in a free market.", 4],
  ["Inflation", "Prices going up.", "A rise in prices.", "A sustained rise in the general price level.", 3],
  ["Real GDP", "GDP in real terms.", "GDP adjusted for prices.", "GDP adjusted for inflation, so it shows the change in the quantity of output.", 4],
  ["Terms of trade", "How good trade is.", "Export prices and import prices.", "The ratio of export prices to import prices, (export price index ÷ import price index) × 100.", 4]
], (it) => `${it[0]}. Weak: "${it[1]}" Partial: "${it[2]}" Full: "${it[3]}"`, "Marks at stake for the definition");
chooser("k", [
  ["Supply and demand shift", "Axes, D and S labelled, equilibrium, the shift labelled, new equilibrium", "Forgetting to label the shifted curve or the new price and quantity", "1 to 2", 3],
  ["Indirect tax", "Supply shifts left by the tax, vertical gap equal to the tax, prices paid and received", "Showing the demand curve shifting", "2", 4],
  ["Maximum price", "Control line below equilibrium, shortage shown", "Drawing the line above equilibrium", "2", 4],
  ["AD/AS", "Price level and real output on axes, AD and SRAS, the shift and new equilibrium", "Using price and quantity as the axes", "2", 4],
  ["Currency market", "Exchange rate on the vertical axis, demand and supply of the currency, the shift", "Shifting the wrong curve for the cause", "1 to 2", 3],
  ["Tariff", "World price, price with tariff, the quantities of imports before and after", "Drawing a tariff without labelling quantities", "2", 3]
], (it) => `${it[0]}: include ${it[1].toLowerCase()}. Common slip: ${it[2].toLowerCase()}. Marks at stake: about ${it[3]}.`, "Importance of labelling");
''' + CLASSIFY("cl1", "Which assessment objective does the skill show?", ["AO1 Knowledge", "AO2 Analysis", "AO3 Evaluation"],
  [("Define price elasticity of demand", 0), ("Write the formula for real GDP", 0), ("Explain why a tax raises price and cuts quantity", 1), ("Show that a rise in AD raises output and prices using a diagram", 1), ("Judge whether a policy is the best option and say why", 2), ("Conclude that it depends on the elasticity of demand", 2)],
  "AO1 is recall and understanding; AO2 explains causes and effects; AO3 weighs and judges.") + CLASSIFY("cl2", "Is it a full-mark definition?", ["Full credit", "Not enough"],
  [("Inflation is a sustained rise in the general price level.", 0), ("Inflation is prices going up.", 1), ("Real GDP is GDP adjusted for inflation.", 0), ("Real GDP is real.", 1), ("A merit good is more beneficial than consumers realise, so it is under-consumed.", 0), ("A merit good is a good that is good.", 1)],
  "A full definition gives the key idea and the qualifier.") + ORDER(
  "Put the calculation steps in order.",
  ["Write the formula", "Substitute the figures", "Work out the answer", "Add the unit and check the sign", "Check it is sensible"],
  "Formula, substitute, answer, units.") + MATCH([
  ["Price elasticity of demand", "% change in quantity demanded ÷ % change in price"],
  ["Terms of trade", "(export price index ÷ import price index) × 100"],
  ["Real GDP", "Nominal GDP ÷ price index × 100"],
  ["Unemployment rate", "Unemployed ÷ labour force × 100"],
  ["GDP by expenditure", "C + I + G + (X − M)"],
  ["Marginal rate of tax", "Change in tax ÷ change in income"]]) + CALC([
  {"q": "Price rises 10% and quantity demanded falls 25%. What is the price elasticity of demand (size)?", "a": 2.5, "unit": "", "tol": 0.05, "hint": "25 ÷ 10.", "sol": "<b>2.5</b>, elastic."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "The export price index is 105 and the import price index is 95. What are the terms of trade (1 decimal place)?", "a": 110.5, "unit": "", "tol": 0.1, "hint": "(105 ÷ 95) × 100.", "sol": "<b>110.5</b>."},
  {"q": "Goods balance −40, services +25, primary income +10, secondary income −5 ($bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "−40 + 25 + 10 − 5.", "sol": "<b>−$10bn</b>."},
  {"q": "2 million are unemployed and 30 million are employed. What is the unemployment rate (%, 2 decimal places)?", "a": 6.25, "unit": "%", "tol": 0.05, "hint": "2 ÷ 32.", "sol": "<b>6.25%</b>."}]) + MCQ([
  ("How many AO1 marks are typically available in an 8 mark essay part from 2023?", ["1", "2", "3", "5"], 2, "AO1 3, AO2 3, AO3 2."),
  ("Which earns full credit as a definition of inflation?", ["Prices going up", "A sustained rise in the general price level", "Inflation is inflation", "The cost of living"], 1, "Key idea with the qualifier 'sustained'."),
  ("A question says 'with the help of a formula'. What is it signalling?", ["A mark is available for a correct formula", "Only a calculation is needed", "No definition is needed", "Evaluation marks"], 0, "It is an AO1 mark."),
  ("Why is a key term used without understanding not credited?", ["The generic principles say examiners need evidence it is understood", "Examiners dislike key terms", "Terms are not marked", "It is repeated"], 0, "Credit needs evidence of understanding."),
  ("A diagram has no labels. Likely AO1 credit?", ["Little or none", "Full marks", "Evaluation marks", "Double marks"], 0, "Labelling is part of accuracy.")
], "qz1") + CARDS([
  ("AO1", "Knowledge and understanding."),
  ("8 mark part", "3 AO1 marks (2 before 2023)."),
  ("12 mark part", "AO1 + AO2 in Table A out of 8."),
  ("Definition", "Key idea + qualifier."),
  ("Formula", "Learn exactly."),
  ("Diagram", "Axes, curves, shift, equilibrium."),
  ("Calculation", "Formula, working, unit."),
  ("Key terms", "Credit needs understanding.")]) + MCQ(mc_exam)

build("ex1", "as-ao1-knowledge", "AO1 Knowledge and Understanding: How the Marks Are Earned", EY,
  "What earns AO1 marks in Paper 1 and Paper 2: definitions, formulae, diagrams and calculations, how the three marks in an 8 mark part are awarded, and what Level 1, 2 and 3 knowledge looks like in a 12 mark answer.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
