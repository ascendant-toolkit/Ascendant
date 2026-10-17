"""AS exam technique: AO2 analysis, how each level is reached. Run: python3 tools/artifact-kit/mk_ex2.py"""
from as6k import *
EY = "AS Level Economics · 9708 · Exam technique"

def S(kind, t): return f'<span class="mk {kind}" data-t="{kind.upper()}">{t}</span>'

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">AO2 is analysis</b>: using economic concepts, theories and information to show <b>causes, effects and relationships</b>, and explaining the <b>impact of changes in economic variables</b>, in written, numerical and diagrammatic form. In the 12 mark question analysis is marked together with knowledge (AO1) in <b>Table A out of 8</b>, in three levels: <b>Level 1 (1 to 2)</b> is largely descriptive, <b>Level 2 (3 to 5)</b> is generally accurate but limited in development, detail or application, and <b>Level 3 (6 to 8)</b> is developed, detailed, accurate and clearly applied. In the 8 mark part analysis is worth <b>3 marks</b> and in data response parts it is worth <b>3 of 4 marks</b> or <b>4 of 6 marks</b>, each as separate points. What moves an answer up a level is not length for its own sake but <b>how many logical steps are linked</b>, <b>how precisely the economics is used</b>, <b>how clearly it is applied to the context in the question</b>, and (in 12 mark questions) <b>whether both sides or an alternative are analysed</b>. This page shows exactly what each level looks like, with examples at every level.</p></div>

  <h2>1 · Where AO2 marks are, and what they are worth</h2>
  <div class="tw"><table class="t">
    <tr><th>Question type</th><th>Marks</th><th>AO2 share</th><th>How the marks are earned</th></tr>
    <tr><td><b>Paper 2 data response (b)</b>: "explain"</td><td>2</td><td>1 or 2</td><td>1 mark for the point, 1 for a development or reason</td></tr>
    <tr><td><b>Data response (c)</b>: "consider"</td><td>4</td><td>3 (1 more for evaluation)</td><td>Up to 3 marks for linked points, using the data</td></tr>
    <tr><td><b>Data response (d) and (e)</b>: "assess" or "discuss"</td><td>6</td><td>4 (2 for evaluation)</td><td>Analysis of both sides, up to 2 marks per side, each developed</td></tr>
    <tr><td><b>Essay part (a)</b></td><td>8</td><td>3 (AO1 3, AO3 2)</td><td>Point marks: explanation of cause and effect, one mark per developed step</td></tr>
    <tr><td><b>Essay part (b)</b></td><td>12</td><td>AO1 and AO2 together out of 8</td><td>Table A levels (below); evaluation (4) is marked separately in Table B</td></tr>
  </table></div>
  <p class="note">From 2023 the 8 mark part is marked AO1 (3), AO2 (3) and AO3 (2). In papers up to 2022 it was 2 marks for knowledge and 6 for application, with the evaluation inside the application marks. The skill is the same.</p>

  <h2>2 · Table A: the three levels in plain English</h2>
  <div class="tw"><table class="t">
    <tr><th>Level and marks</th><th>What the mark scheme says</th><th>What the answer is like</th></tr>
    <tr><td><b>Level 3</b><br>6 to 8</td><td>Detailed knowledge and understanding of relevant concepts, with relevant explanations supported by examples; the requirements of the question are clearly addressed and the explanations are <b>fully developed</b>; analysis is <b>developed and detailed</b> and makes <b>accurate and relevant use</b> of concepts, theories and tools such as diagrams and formulae, which are <b>fully explained</b>; <b>well organised, well focused</b>, logical and coherent.</td><td>Several points, each carried through a chain of at least three steps to the effect the question asks about, using correct terms, with a diagram or figures explained in words, applied to the named good, policy or country, and covering both sides or an alternative.</td></tr>
    <tr><td><b>Level 2</b><br>3 to 5</td><td>Knowledge of <b>some</b> relevant concepts, with explanations and examples that are <b>limited, over-generalised or contain inaccuracies</b>; the response addresses the <b>general theme</b> with <b>limited development</b>; analysis is <b>generally accurate with some development but little detail</b>; tools such as diagrams are <b>partially accurate or not fully explained</b>; generally logical but sometimes lacking focus or organisation.</td><td>Mostly correct economics, with one or two points explained, but a step is missing, the explanation stops early, an example is generic, a diagram is drawn but not used, or only one side is covered.</td></tr>
    <tr><td><b>Level 1</b><br>1 to 2</td><td>A <b>small number</b> of relevant knowledge points; <b>significant errors or omissions</b>; little relevance to the question; analysis is <b>largely descriptive</b>; diagrams and formulae may contain significant errors or be missing; limited organisation.</td><td>Definitions and assertions ("this will reduce unemployment") with no mechanism, or an answer that describes the topic without answering the question.</td></tr>
  </table></div>
  <p>The marks within a level depend on how fully the descriptors are met: a response at the <b>bottom</b> of a level shows the descriptors only in part; one at the <b>top</b> meets them all and is close to the next level.</p>

  <h2>3 · What changes from level to level: length, depth, context and balance</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>Level 1 (1 to 2)</th><th>Level 2 (3 to 5)</th><th>Level 3 (6 to 8)</th></tr>
    <tr><td><b>Typical length of the analysis</b> (a guide, not a rule)</td><td>1 to 3 sentences, about 40 to 80 words</td><td>One or two paragraphs, about 100 to 200 words</td><td>Two or three developed paragraphs, about 250 to 350 words, plus a diagram</td></tr>
    <tr><td><b>Depth of reasoning</b></td><td>States a result without a reason: "a minimum price raises the price"</td><td>One or two steps of cause and effect, with a missing link: "so quantity demanded falls"</td><td>Three or more linked steps with the mechanism named at each: price floor above equilibrium, contraction of quantity demanded, effect on consumption, effect on health costs</td></tr>
    <tr><td><b>Use of economic terms and tools</b></td><td>Everyday words; key terms named but not used</td><td>Correct terms, sometimes over-generalised ("the economy suffers")</td><td>Precise terms used correctly (price elasticity of demand, excess supply, SRAS shift) and diagrams or formulae explained</td></tr>
    <tr><td><b>Application to the context</b></td><td>None, or could be about any good</td><td>General: "a demerit good such as alcohol" with no specific link</td><td>Specific: uses the named good, policy, country or figures and explains why they matter here</td></tr>
    <tr><td><b>Balance</b></td><td>One idea</td><td>Often one-sided, or both sides stated briefly</td><td>Both sides, or the policy and at least one alternative, each analysed</td></tr>
    <tr><td><b>Errors</b></td><td>Significant errors or irrelevant material</td><td>Some inaccuracies or over-generalisation</td><td>Accurate throughout</td></tr>
    <tr><td><b>Organisation</b></td><td>Limited</td><td>Mostly logical but loses focus</td><td>Well organised: each paragraph has one point and links back to the question</td></tr>
  </table></div>
  <p><b>Caps written into real mark schemes.</b> Examiners are told, for example: <i>"a one-sided response can only reach Level 2"</i>; for a question on a trade-dependent economy, <i>"answers which do not refer to the heavy dependence on international trade cannot gain more than Level 2"</i>; for a question set in a developing economy, <i>"if the analysis is not in the context of a developing economy, then Level 2 maximum"</i>; and <i>"at least one negative effect in addition to positive effects should be considered to gain lower Level 3"</i>. These are the rules that decide the level, so read the question for the <b>who and where</b> as well as the <b>what</b>.</p>

  <h2>4 · One question, three answers: a 12 mark analysis ladder</h2>
  <p><b>Question (Table A part, out of 8):</b> <i>Assess whether fixing a minimum price is likely to be the best policy to reduce the consumption of a demerit good.</i> The mark scheme expects: minimum pricing raises the price and reduces consumption; problems such as inelastic demand, persistent information failure and informal markets; and alternatives such as indirect taxes, education and information, with advantages and disadvantages. (Evaluation is marked separately: see the AO3 review.)</p>
  <div class="card"><h3>Level 1 answer: 1 to 2 marks (about 45 words)</h3>
  <p>A minimum price is a price set by the government. Alcohol is a demerit good. A minimum price makes alcohol cost more so people drink less. A tax can also be used to make people drink less.</p>
  <p class="note"><b>Why Level 1:</b> relevant and correct, but it is assertion. There is no mechanism (no price above equilibrium, no change in quantity demanded), no mention of elasticity or any limit, no diagram, and the alternative is named but not explained. The reader learns that the student knows the terms, not that they can analyse.</p></div>
  <div class="card"><h3>Level 2 answer: 3 to 5 marks (about 120 words)</h3>
  <p>A minimum price is a legal price floor set <b>above</b> the market price. For alcohol, it raises the price of cheap drinks, so the quantity demanded falls and consumption falls. This should reduce the health problems caused by drinking. <b>However</b>, if people are addicted, demand may be inelastic, so they keep buying and consumption may fall only a little. Sellers also gain more revenue from the higher price. A tax could be used instead. A tax would also raise the price, and the government would get the money.</p>
  <p class="note"><b>Why Level 2:</b> the mechanism is stated correctly and one limit (inelastic demand) is given, so the analysis is accurate with some development. But each point stops after one or two steps, there is no diagram, the alternative is undeveloped, and nothing is applied beyond "alcohol". Roughly 4 marks: the top of Level 2 would add a second developed point.</p></div>
  <div class="card"><h3>Level 3 answer: 6 to 8 marks (about 300 words)</h3>
  <p>A minimum price is a legal limit below which a price cannot fall. To be effective for a demerit good such as alcohol it must be set <b>above the equilibrium price</b>. On my diagram the floor is set at P<sub>min</sub>, above P*. At this price, quantity demanded contracts along the demand curve from Q* to Q<sub>d</sub> while quantity supplied extends to Q<sub>s</sub>, so consumption falls by Q* − Q<sub>d</sub>. Because the policy can be aimed at cheap, strong drinks, it targets the products linked to the most harm, which may reduce hospital and other health costs.</p>
  <p>How far consumption falls depends on the <b>price elasticity of demand</b>. Alcohol is habit-forming, so demand is likely to be price inelastic: a 20% rise in price might reduce quantity demanded by only 5%, so the fall in consumption is small and heavy drinkers spend more, leaving less for other goods. The higher price also creates <b>excess supply</b> (Q<sub>s</sub> − Q<sub>d</sub>), and the extra revenue goes to retailers, not the government. <b>Informal markets</b> may develop, and information failure, the root cause of over-consumption, remains.</p>
  <p>An <b>indirect tax</b> would also shift supply left and raise the price, but the revenue goes to the government, which can fund health services, and it applies to all alcohol, not only the cheapest. <b>Education and information</b> tackle the cause by raising awareness of the harm, shifting demand left, but the effect is slow and uncertain. A minimum price is simple and quick to introduce, but its effect is limited when demand is inelastic.</p>
  <p class="note"><b>Why Level 3:</b> three developed chains (minimum price, elasticity limit, alternatives), the diagram is used and explained in words, terms are precise (equilibrium, contraction, excess supply, elasticity, indirect tax), the policy is compared with alternatives, and the paragraphs are organised around the question. This would earn 7 or 8; it would drop to 6 if the alternatives were mentioned but not developed.</p></div>
  <div class="warn"><b class="h">A Level 3 quality answer that is one-sided is still capped</b>If the same student had written three excellent paragraphs only about why minimum prices work, the mark scheme limit for a one-sided response (Level 2) would apply, so the top mark would be 5 however well each point was explained. Balance is part of the level, not an extra.</div>

  <h2>5 · The 8 mark part: how the 3 analysis marks are awarded</h2>
  <p><b>Question:</b> <i>Explain the difference between cost-push and demand-pull inflation and consider which is more likely to occur if there is a depreciation in the exchange rate of a country with few natural resources.</i> The mark scheme gives <b>3 marks for analysis</b>: a depreciation lowers the price of exports and raises the price of imports; this is analysed for demand-pull (net exports and AD, with the price elasticity of demand for exports and imports) and for cost-push (importance of imports; a country with few natural resources must import them). <b>A maximum of 2 marks if only one type of inflation is considered.</b></p>
  <div class="tw"><table class="t">
    <tr><th>AO2 marks</th><th>Example answer</th><th>Why that many</th></tr>
    <tr><td><b>0 to 1</b></td><td>"A depreciation makes imports dearer so prices rise."</td><td>Correct direction, but it is assertion: no link to AD or costs, no type of inflation, no reference to the context.</td></tr>
    <tr><td><b>2</b></td><td>"Cheaper exports and dearer imports raise net exports, so AD shifts right and the price level rises: demand-pull."</td><td>A complete chain for one type only, so the cap of 2 applies.</td></tr>
    <tr><td><b>3</b></td><td>The chain above, <b>and</b> "a country with few natural resources must import raw materials and fuel, so a depreciation raises firms' costs, shifting SRAS left: cost-push."</td><td>Both types analysed, with the context (few natural resources) used to explain why the cost-push link is strong.</td></tr>
  </table></div>

  <h2>6 · Data response: 2, 4 and 6 marks</h2>
  <p><b>2 marks: "Explain one reason why using the CPI to measure inflation may not give an accurate result."</b> The mark scheme gives <b>1 mark for the reason and 1 for the development</b>: the CPI is based on a basket for the average household (1), but buying patterns change so the basket may no longer be typical (1). A one-line answer ("it is not accurate") earns 0.</p>
  <p><b>6 marks: "Use AD/AS analysis to explain how recent interest rate rises might help reduce the annual rate of inflation."</b> The mark scheme rewards an explanation for <b>demand-pull</b> (up to 4) and for <b>cost-push</b> (up to 4), up to 6 in total, with 2 marks available for evaluative comment that the rise might exacerbate inflation.</p>
  <div class="tw"><table class="t">
    <tr><th>Marks</th><th>Example</th><th>Why</th></tr>
    <tr><td><b>2</b></td><td>"Higher interest rates make borrowing dearer, so spending falls and inflation falls."</td><td>A correct but short chain, with no AD/AS, for one type of inflation only.</td></tr>
    <tr><td><b>4</b></td><td>"A rise in interest rates makes borrowing dearer and saving more attractive, so consumption and investment fall and AD shifts left. The price level falls, so demand-pull inflation is reduced. The central bank's higher rate may also raise the exchange rate, cheapening imported inputs and so shifting SRAS right."</td><td>Two chains (demand-pull, cost-push), with AD and SRAS named at the key steps.</td></tr>
    <tr><td><b>6</b></td><td>The answer above, plus: "However, higher borrowing costs raise firms' costs, which could shift SRAS left and worsen cost-push inflation, so the rise may not help."</td><td>The two analysis chains and a developed evaluative comment, as the mark scheme allows.</td></tr>
  </table></div>

  <h2>7 · The building blocks of a Level 3 paragraph</h2>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Job</th><th>Example (minimum price)</th></tr>
    <tr><td><b>Point</b></td><td>One sentence that answers the question using its wording</td><td>"A minimum price could reduce consumption of alcohol, but only if demand responds."</td></tr>
    <tr><td><b>Mechanism</b></td><td>The economic reason, with the concept and the diagram named</td><td>"The floor is above equilibrium, so quantity demanded contracts from Q* to Q<sub>d</sub>."</td></tr>
    <tr><td><b>Apply</b></td><td>Use the named good, country or data</td><td>"Cheap, strong drinks are mainly bought by heavier drinkers, so the policy targets the most harmful consumption."</td></tr>
    <tr><td><b>Consequence chain</b></td><td>Two or three linked steps</td><td>"Lower consumption means fewer alcohol-related illnesses, so health spending falls."</td></tr>
    <tr><td><b>Link</b></td><td>Tie the result back to the question (no judgement yet)</td><td>"So price alone can reduce consumption of this demerit good."</td></tr>
  </table></div>
  <p><b>Linking words that show a chain:</b> because, so, which means, as a result, therefore, this leads to, causing, which in turn. <b>The "so what" test:</b> after each sentence ask "so what happens next?" and write the next step until you reach the effect the question asks about.</p>

  <h2>8 · Generic or applied?</h2>
  <div class="tw"><table class="t">
    <tr><th>Generic (could be about anything)</th><th>Applied (needs this question)</th></tr>
    <tr><td>"The tax makes the good more expensive so people buy less."</td><td>"A 20% tax on cigarettes raises the price, but because smokers are addicted, demand is price inelastic, so quantity falls by less than 20% and total spending on cigarettes rises."</td></tr>
    <tr><td>"The depreciation helps exports."</td><td>"After the depreciation, the country's coffee is cheaper abroad, so export volumes may rise, but if demand for coffee is inelastic, export revenue may fall."</td></tr>
    <tr><td>"Unemployment is bad for the economy."</td><td>"As unemployment rises from 5% to 8%, tax revenue falls and benefit spending rises, so the budget deficit widens."</td></tr>
  </table></div>
  <p><b>Swap test:</b> could this sentence appear unchanged in an answer about a different market? If yes, add the name of the good, the group affected, the figure from the extract or the feature of the economy that makes the point true here.</p>

  <h2>9 · A bank of analysis chains</h2>
  <div class="tw"><table class="t">
    <tr><th>Starting point</th><th>Chain</th><th>Effect to state</th></tr>
    <tr><td>Indirect tax</td><td>Costs rise, supply shifts left by the tax, price rises, quantity demanded contracts; the split depends on elasticity</td><td>Price up, quantity down, revenue = tax × quantity</td></tr>
    <tr><td>Subsidy</td><td>Costs fall, supply shifts right, price falls, quantity rises; cost to the government = subsidy × quantity</td><td>Price down, quantity up</td></tr>
    <tr><td>Maximum price below equilibrium</td><td>Quantity demanded rises, quantity supplied falls, shortage, rationing or a black market</td><td>Shortage; fewer goods traded</td></tr>
    <tr><td>Interest rate rise</td><td>Borrowing dearer, saving more attractive, C and I fall, AD shifts left</td><td>Price level and output fall</td></tr>
    <tr><td>Depreciation</td><td>Exports cheaper, imports dearer, net exports rise if elastic, AD rises; imported inputs dearer, SRAS falls</td><td>Output up, prices up</td></tr>
    <tr><td>Supply-side policy</td><td>Training raises productivity, unit costs fall, SRAS and LRAS shift right</td><td>Output up, price level down, after a lag</td></tr>
    <tr><td>Tariff</td><td>Import price rises, quantity of imports falls, domestic output rises, consumers pay more</td><td>Imports down, revenue, welfare loss</td></tr>
    <tr><td>Rise in government spending</td><td>G rises, AD shifts right, output rises (more if spare capacity), prices rise (more near full capacity)</td><td>Output and price level up; deficit up</td></tr>
  </table></div>

  <h2>10 · Common ways to lose analysis marks</h2>
  <ul>
    <li><b>Description instead of analysis:</b> defining the policy at length and never saying what it does.</li>
    <li><b>Jumping steps:</b> "so unemployment falls" with no reason AD or output changes.</li>
    <li><b>Direction errors:</b> shifting the wrong curve or confusing a movement along a curve with a shift.</li>
    <li><b>Unused diagrams:</b> drawing a diagram but never referring to it, so it earns little.</li>
    <li><b>Answering a different command:</b> explaining when the question says assess, or listing when it says explain a chain.</li>
    <li><b>Missing the scope:</b> ignoring "developing economy", "open economy", "always" or "only".</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Aim for <b>two developed chains per side</b> in a 12 mark answer, not five thin points. Use the question's own noun in each topic sentence, refer to your diagram in the text, and finish each paragraph by linking back to the question.</div>
'''

watch = '''
  <h2>1 · The same paragraph, level by level</h2>
  <p>Press Play, or click the numbered steps. Each step adds one thing that an examiner can credit.</p>
  <div id="stA"></div>
  <h2>2 · How the 3 analysis marks build in an 8 mark part</h2>
  <div id="stB"></div>
  <h2>3 · A Level 3 diagram answer: minimum price</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Which level is this analysis?</h2>
  <p>Describe an answer to a 12 mark question (the AO1 and AO2 part, out of 8). The lab applies the Table A descriptors and the caps used in real mark schemes. It is a teaching model, not an official mark.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Estimated mark (out of 8)</small><strong id="r1"></strong></div><div><small>Level</small><strong id="r2"></strong></div><div><small>To reach the next level</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 240" role="img" aria-label="A bar showing the estimated mark against the Level 1, 2 and 3 bands"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Choose an analysis chain", "Choose a starting point to see the chain, the context to add and the usual slip.", ["Chain of reasoning", "Context to add", "Usual slip"]) + chooser_html("k", "Lab 3 · What would the examiner write?", "Choose a sentence to see the annotation it earns and how to improve it.", ["Annotation", "Why", "How to improve it"])

practise = '''
  <h2>1 · Description or analysis?</h2><div id="cl1" class="card"></div>
  <h2>2 · Generic or applied?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the level to its feature</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A cap that decides the level", "In one series, the mark scheme for a question on terms of trade in an economy heavily dependent on trade said that answers not referring to that dependence could not exceed Level 2, and answers considering only a rise or only a fall could not exceed Level 2.", "reading the question for the context and covering both sides.") +
rw("Balance in a one-sided answer", "A question on whether free trade is always positive carried the note that a one-sided response cannot gain any evaluation marks, and the Level 2 descriptor says answers 'may be one-sided'. Both sides, each explained, are needed for Level 3.", "why one-sided analysis stops at Level 2.") +
rw("Diagrams that earn marks only if used", "Mark schemes say 'an accurate diagram should not be expected but would enhance the quality of the analysis' for some questions, and require the diagram to be explained for the top level.", "drawing, labelling and referring to a diagram.") +
rw("Point marks in an 8 mark part", "For a question on the effect of an interest rate fall, the analysis marks were: explain how lower rates affect saving and borrowing (1), the effect on consumption, investment or net exports (1) and the effect on growth (1).", "one mark per developed step in the chain.") +
rw("Key terms alone are not credited", "The generic marking principles say examiners do not credit an answer simply for using a key term unless there is evidence it is understood and not used wrongly.", "explaining, not just naming.")
)

mc_exam = [
  mcq("s21_12", 27, "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation)", ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], 3, "A worse current account tends to lower the exchange rate, which raises import costs and cost-push inflation: a three-step chain."),
  mcq("s22_11", 29, "Why will a contractionary monetary policy reduce inflation?", ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], 3, "Higher interest rates encourage saving and reduce spending, lowering AD."),
  mcq("m24_12", 21, "An economy has an unemployment rate of 8%, an increase of 2% from the previous year. At the same time, the current account deficit rose from 3% of GDP to 4% of GDP. What would be most likely to reduce both unemployment and the current account deficit?", ["decrease government spending", "depreciation of the currency", "increase indirect taxation", "increase interest rates"], 1, "A depreciation could raise exports and reduce imports, boosting AD, output and employment while narrowing the deficit."),
  mcq("s25_12", 11, "An indirect tax is imposed on good X. Which situation is most likely to result in producers bearing a higher burden of the tax?", ["price elasticity of demand is elastic", "price elasticity of demand is inelastic", "price elasticity of supply is elastic", "price elasticity of supply is inelastic"], 0, "With elastic demand, a price rise cuts quantity a lot, so producers absorb more of the tax."),
  mcq("m20_12", 5, "In which circumstance will the total expenditure by consumers on a good increase when its price increases?", ["Demand for the good is income elastic.", "Demand for the good is price inelastic.", "The price of a complementary good also increases.", "The price of substitute goods also increases."], 1, "With inelastic demand quantity falls by a smaller percentage than price rises, so expenditure rises."),
  mcq("s21_13", 25, "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency?", ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], 1, "If the sum of the elasticities is below one, the Marshall-Lerner condition fails.")
]

exam = exam_page("analysis: how each level is reached",
  "We chose past questions where the mark scheme shows clearly what earns analysis marks: a 12 mark discussion with explicit level descriptors and caps, an 8 mark part with three analysis marks, and two data response parts. Open each one and compare the answer with the Level 3 description; the key shows the parts marked for knowledge (K), analysis (N) and evaluation (E).",
  exam_rows([("s23_22","5(a)",8),("m24_22","5(a)",8),("s24_22","3(b)",12),("w23_22","4(b)",12),("m25_22","4(b)",12),("s25_21","1(b)",2),("s20_22","1(d)",6)], ["s21_12","s22_11","m24_12","s25_12","m20_12","s21_13"]),
  [
  grab("s23_22", "5(a)"),
  grab("m24_22", "5(a)"),
  grab("s24_22", "3(b)"),
  grab("w23_22", "4(b)"),
  grab("m25_22", "4(b)"),
  grab("s25_21", "1(b)"),
  grab("s20_22", "1(d)")
  ],
  )

tips = tips_html(
  [("Link at least three steps.", "Cause, mechanism, effect: one step is Level 1."),
   ("Name the concept at each step.", "Elasticity, AD, SRAS, excess supply."),
   ("Use and explain the diagram.", "A drawn diagram that is not referred to earns little."),
   ("Apply to the context.", "The named good, country or figures."),
   ("Cover both sides or an alternative.", "One-sided analysis is capped at Level 2."),
   ("Two developed chains beat five thin points.", "Depth, not a list."),
   ("End each paragraph back at the question.", "Use its key noun and verb.")],
  [("Analysis", "Analysis explains causes, effects and relationships using economic concepts, not just describes them."),
   ("Chain of reasoning", "A chain of reasoning links each step to the next from cause to effect."),
   ("Application", "Application is using the context in the question, not general statements."),
   ("Level 3", "Level 3 analysis is developed, detailed, accurate, applied and balanced."),
   ("One-sided", "A one-sided response cannot exceed Level 2.")],
  [CW["explain"], CW["analyse"], CW["assess"], CW["discuss"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const L = [["Level 1", "1 to 2 marks", "Assertion, no mechanism", 30, "f3"], ["Level 2", "3 to 5 marks", "Mechanism, limited detail", 270, "f1"], ["Level 3", "6 to 8 marks", "Developed chains, applied, balanced", 510, "f2"]];
  let o = ""; L.forEach(([n, m, d, x, c]) => { o += SV.rect(x, 12, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 110, 62, m, "sm", { "text-anchor": "middle" }) + SV.text(x + 110, 84, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="The three levels of Table A">${o}</svg>`;
})();
chainStep("#stA", "The same paragraph, level by level", ["Level 1: 'A minimum price makes alcohol cost more so people drink less.' (assertion)", "Add the mechanism: the floor is above equilibrium, so quantity demanded contracts (Level 2)", "Add a limit with a reason: inelastic demand means consumption falls only a little", "Add the effect on others: excess supply and extra revenue to retailers; informal markets", "Add an alternative and compare: a tax gives the government revenue (Level 3)"], [
  "<b>1 to 2 marks:</b> correct, but there is no reason why.", "<b>3 to 4 marks:</b> the economics is stated and linked.", "<b>5 marks:</b> a second developed point, using elasticity.", "<b>6 marks:</b> both sides of the policy are analysed.", "<b>7 to 8 marks:</b> an alternative is analysed, with a diagram explained in the text."]);
chainStep("#stB", "How the 3 analysis marks build", ["Mark 1: a correct statement of cause and effect: a depreciation makes imports dearer", "Mark 2: a complete chain for demand-pull: exports cheaper, net exports rise, AD shifts right, prices rise", "Mark 3: a second chain for cost-push, using the context: few natural resources, so costs rise and SRAS shifts left", "Cap: only one type of inflation considered means a maximum of 2 analysis marks"], [
  "<b>1 mark:</b> the idea, with no development.", "<b>2 marks:</b> one chain to the end.", "<b>3 marks:</b> both types, applied to the country with few natural resources.", "<b>Read the mark scheme caps:</b> they say what stops marks at the next boundary."]);
const mpLab = { x: "Quantity of alcohol", y: "Price", D1: "D", S1: "S", P1: "P*", Q1: "Q*" };
function mpDraw(f, k) {
  const qd = (90 - f) / 0.8, qs = (f - 10) / 0.8; // D: p=90-0.8q ; S: p=10+0.8q
  let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, mpLab);
  if (k >= 1) o += SV.line(70, SDY(f), 720, SDY(f), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(f) - 6, "Minimum price", "c3", k, "end");
  if (k >= 2) o += SV.line(SDX(qd), SDY(f), SDX(qd), 270, "dash", op(1)) + SV.text(SDX(qd), 286, "Qd", "sm", { "text-anchor": "middle" }) + SV.line(SDX(qs), SDY(f), SDX(qs), 270, "dash", op(1)) + SV.text(SDX(qs), 286, "Qs", "sm", { "text-anchor": "middle" });
  if (k >= 3) o += SV.line(SDX(qd), SDY(f) + 14, SDX(qs), SDY(f) + 14, "c4", { "stroke-width": 3 }) + SV.text(SDX((qd + qs) / 2), SDY(f) + 32, "Excess supply", "sm", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A minimum price diagram", base: { f: 65, k: 0 }, draw: (s) => mpDraw(s.f, s.k), tween: 800, dwell: 5600, steps: [
  { cap: "<b>1 knowledge mark:</b> axes, D and S labelled, equilibrium P* and Q* marked.", s: { f: 65, k: 0 } },
  { cap: "<b>Draw the floor above P*</b>: a minimum price is only effective above equilibrium.", s: { f: 65, k: 1 } },
  { cap: "<b>Show the two quantities:</b> quantity demanded contracts to Qd, quantity supplied extends to Qs.", s: { f: 65, k: 2 } },
  { cap: "<b>Mark the excess supply</b> (Qs − Qd) and say in words what it means: consumption falls, but the extra supply is unsold. Refer to the diagram in the text for analysis marks.", s: { f: 65, k: 3 } },
] });

/* ---------- Lab 1: level checker ---------- */
function lvl() {
  const ids = ["st", "cx", "dg", "er", "sd"];
  if (!ids.every((i) => $("#" + i))) return;
  const [steps, ctx, dia, err, both] = ids.map((i) => +$("#" + i).value);
  let sc = steps * 1.0 + ctx * 1.0 + dia * 0.75 + (both ? 1.5 : 0) - err * 0.8, cap = 8, why = [];
  if (!both) { cap = Math.min(cap, 5); why.push("one-sided analysis is capped at Level 2 (5)"); }
  if (ctx === 0) { cap = Math.min(cap, 5); why.push("no application to the context caps the answer at Level 2"); }
  if (err >= 2) { cap = Math.min(cap, 5); why.push("several inaccuracies keep it at Level 2"); }
  if (steps <= 1) { cap = Math.min(cap, 2); why.push("a single step is assertion (Level 1)"); }
  let m = Math.max(0, Math.min(Math.round(sc), cap, 8)), L = m >= 6 ? 3 : m >= 3 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 8"; $("#r2").textContent = L ? "Level " + L : "No credit";
  let nx = L === 3 ? "Already at the top band: make every step precise" : L === 2 ? (!both ? "Analyse the other side or an alternative" : ctx < 2 ? "Use the named good, country or figures" : steps < 4 ? "Add another linked step" : "Explain the diagram and remove inaccuracies") : "Add a mechanism: say why, in at least three linked steps";
  $("#r3").textContent = nx;
  $("#rv").textContent = `${steps} linked step(s), ${["no", "general", "specific"][ctx]} application, diagram ${["absent", "drawn but not explained", "correct and explained"][dia]}, ${err} error(s), ${both ? "both sides or an alternative" : "one side only"}: about ${m} out of 8 (Level ${L || 0}).` + (why.length ? " Capped because " + why.join("; ") + "." : "");
  const W = 380, X = (v) => 20 + (v / 8) * W;
  let o = SV.rect(X(0), 60, X(2) - X(0), 40, "f3", op(0.4)) + SV.rect(X(2), 60, X(5) - X(2), 40, "f1", op(0.4)) + SV.rect(X(5), 60, X(8) - X(5), 40, "f2", op(0.4));
  o += SV.text(X(1), 85, "L1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(3.5), 85, "L2", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(6.5), 85, "L3", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 40, X(m), 125, "c4", { "stroke-width": 3 }) + SV.text(X(m), 34, m + "", "lbl bd", { "text-anchor": "middle" }) + SV.text(20, 160, "0", "sm") + SV.text(X(8), 160, "8", "sm", { "text-anchor": "end" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "st", label: "Linked steps in the best chain (0 to 5) ", min: 0, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: lvl });
Lib.slider($("#g2"), { id: "cx", label: "Application: 0 none, 1 general, 2 specific ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "general", "specific"][v], onInput: lvl });
Lib.slider($("#g3"), { id: "dg", label: "Diagram: 0 none, 1 not explained, 2 explained ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "not explained", "explained"][v], onInput: lvl });
Lib.slider($("#g4"), { id: "er", label: "Inaccuracies or irrelevant points ", min: 0, max: 3, step: 1, value: 0, fmt: (v) => v, onInput: lvl });
Lib.slider($("#g5"), { id: "sd", label: "Other side or alternative analysed? (0 no, 1 yes) ", min: 0, max: 1, step: 1, value: 0, fmt: (v) => (v ? "yes" : "no"), onInput: lvl });
lvl();

chooser("h", [
  ["Indirect tax", "Costs rise, supply shifts left by the tax, price rises, quantity demanded contracts; elasticity decides who pays", "Name the good and its elasticity (for example cigarettes: addictive, inelastic)", "Shifting the demand curve instead of supply", 5],
  ["Interest rate rise", "Borrowing dearer, saving more attractive, C and I fall, AD shifts left, price level falls", "Use the data or country: who has variable-rate mortgages", "Stopping at 'spending falls' without reaching AD and prices", 5],
  ["Depreciation", "Exports cheaper, imports dearer, net exports rise if elastic, AD rises; dearer inputs shift SRAS left", "State what the country exports and imports", "Assuming net exports always rise", 4],
  ["Supply-side policy", "Training raises productivity, unit costs fall, SRAS and LRAS shift right", "Name the policy, such as apprenticeships, and the time lag", "Forgetting the short-run AD effect of government spending", 4],
  ["Tariff", "Import price rises, imports fall, domestic output rises, consumers lose, revenue gained", "Use the elasticity of demand for imports and possible retaliation", "Ignoring the welfare loss", 4],
  ["Maximum price", "Set below equilibrium: quantity demanded rises, quantity supplied falls, shortage, rationing", "Name the good (rent, bread) and who is protected", "Drawing the line above equilibrium", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. To apply it: ${it[2].toLowerCase()}. A usual slip: ${it[3].toLowerCase()}.`, "How often this chain is asked");
chooser("k", [
  ["'A minimum price makes the price go up.'", "Correct but descriptive: no AO2 credit beyond a knowledge point", "It states the result without why or what follows", "Add: the floor is above equilibrium, so quantity demanded falls", 1],
  ["'Quantity demanded falls, so consumption of the demerit good falls.'", "One analysis step", "A correct link, but short", "Add why the quantity falls and what limits it (elasticity)", 2],
  ["'If demand is inelastic, a 20% rise in price cuts quantity by only 5%, so consumption falls little and spending rises.'", "Developed analysis with a figure", "A mechanism, a number and a consequence", "Link back to the policy question and add the effect on health costs", 4],
  ["'The extra revenue goes to retailers, not the government, unlike a tax.'", "Analysis that also begins a comparison", "It brings in an alternative and a reason", "Develop the tax alternative fully for Level 3", 4],
  ["'So this shows a minimum price is not the best policy.'", "A judgement (evaluation), not analysis", "It answers the question but is not an explanation", "Keep for the conclusion; support it with a condition", 3]
], (it) => `${it[0]} Annotation: ${it[1].toLowerCase()}. Why: ${it[2].toLowerCase()}. To improve: ${it[3].toLowerCase()}.`, "Strength of the sentence");
''' + CLASSIFY("cl1", "Is the sentence description or analysis?", ["Description", "Analysis"],
  [("A minimum price is a legal floor on a price.", 0), ("Because the floor is above equilibrium, quantity demanded contracts, so consumption of alcohol falls.", 1), ("Unemployment is people without a job.", 0), ("As unemployment rises, income tax receipts fall and benefit spending rises, so the budget deficit widens.", 1), ("A tariff is a tax on imports.", 0), ("A tariff raises the import price, so imports fall and domestic output rises.", 1)],
  "Description says what something is; analysis says why and what follows.") + CLASSIFY("cl2", "Is the sentence generic or applied?", ["Generic", "Applied"],
  [("The tax makes the good more expensive.", 0), ("A 20% tax on cigarettes raises their price, but addicted smokers keep buying, so demand is inelastic.", 1), ("The depreciation helps exports.", 0), ("After the depreciation the country's coffee is cheaper abroad, but demand for coffee is inelastic, so revenue may fall.", 1), ("Unemployment harms the economy.", 0), ("Unemployment rose from 5% to 8%, so tax revenue falls.", 1)],
  "Applied sentences use the named good, country or figures; generic ones could appear in any answer.") + ORDER(
  "Put the chain in order: a rise in interest rates reduces inflation.",
  ["The central bank raises the base rate", "Borrowing is dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left", "The price level falls, so inflation is reduced"],
  "A chain is a sequence of linked steps from cause to the effect asked for.") + MATCH([
  ["Level 1 analysis", "Largely descriptive; significant errors or omissions"],
  ["Level 2 analysis", "Generally accurate, some development but little detail"],
  ["Level 3 analysis", "Developed and detailed, accurate use of concepts and tools, fully explained"],
  ["One-sided response", "Capped at Level 2 in the mark scheme"],
  ["Application", "Using the good, policy, country or data in the question"],
  ["Chain of reasoning", "Linked steps from cause to effect"]]) + CALC([
  {"q": "A 12 mark question is marked out of 8 for AO1 and AO2 and 4 for AO3. What fraction of the marks is for AO3 (%)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4 ÷ 12.", "sol": "<b>33.3%</b>."},
  {"q": "Level 2 in Table A is 3 to 5 marks. How many marks lie in the Level 2 band (count inclusive)?", "a": 3, "unit": "marks", "tol": 0.1, "hint": "3, 4, 5.", "sol": "<b>3</b> marks."},
  {"q": "Paper 2 is 60 marks in 120 minutes. How many minutes per mark?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2 minutes</b>."},
  {"q": "A 12 mark answer is to take 20 minutes. What fraction of a 6 mark question's time (at 2 minutes a mark) is that?", "a": 1.67, "unit": "", "tol": 0.05, "hint": "20 ÷ 12 minutes.", "sol": "A 6 mark question takes 12 minutes, so 20 ÷ 12 = <b>1.67</b>."}]) + MCQ([
  ("A response is correct but states only that 'a tax raises the price'. At which level is its analysis?", ["Level 1", "Level 2", "Level 3", "No credit"], 0, "A statement without a mechanism is largely descriptive."),
  ("Which feature most clearly separates Level 3 from Level 2 analysis?", ["Developed, detailed analysis with tools fully explained", "A longer definition", "More facts in the introduction", "A summary at the end"], 0, "Level 3 develops and explains; Level 2 is accurate but limited."),
  ("A mark scheme says a one-sided response cannot exceed Level 2. What does this mean?", ["Even excellent one-sided analysis stops at the top of Level 2", "Level 3 is for long answers only", "Only evaluation is capped", "It does not affect analysis"], 0, "Balance is part of the Level 3 descriptor."),
  ("Which is an applied sentence?", ["The tax raises the price.", "The 20% tax on cigarettes hits addicted smokers whose demand is inelastic.", "Taxes exist in most countries.", "Elasticity measures responsiveness."], 1, "It uses the good and the specific market feature."),
  ("A diagram is drawn with labelled axes but never mentioned in the text. Likely credit?", ["Partly credited for knowledge but the analysis is limited", "Full analysis marks", "No marks for anything", "Evaluation marks"], 0, "Diagrams must be used and explained to earn analysis credit.")
], "qz1") + CARDS([
  ("Level 1", "Assertion, no mechanism."),
  ("Level 2", "Mechanism, limited detail."),
  ("Level 3", "Developed, accurate, applied, balanced."),
  ("Chain", "Cause, mechanism, effect: 3+ steps."),
  ("Applied", "Uses the named good, country or data."),
  ("One-sided", "Capped at Level 2."),
  ("8 mark part", "3 analysis marks."),
  ("12 mark part", "AO1 and AO2 out of 8.")]) + MCQ(mc_exam)

build("ex2", "as-ao2-analysis", "AO2 Analysis: How Each Level Is Reached", EY,
  "Exactly what separates Level 1, 2 and 3 analysis: length, depth of reasoning, use of terms, application to context and balance, with examples at every level for the 8 mark, 12 mark and data response questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
