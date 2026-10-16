"""Builds IGCSE Economics Topic 7 exam technique reviews: AO1 knowledge and AO2 analysis (AO3 already exists as ig-ao3-evaluation). Run: python3 tools/artifact-kit/mk_ig7.py"""
from igtext import *

# ---------------------------------------------------------------- AO1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><b>AO1 is knowledge and understanding</b>: recalling <b>definitions, formulas, concepts and theories</b> and using <b>economic terminology</b> correctly. It is <b>43% of the whole IGCSE</b>, <b>50% of Paper 1</b> and <b>40% of Paper 2</b>, so it is the largest single source of marks you can secure by learning properly. AO1 questions use command words such as <b>Define, Identify, State, Give, Calculate</b> and <b>Describe</b>.</p></div>

  <h2>Where AO1 marks are</h2>
  <div class="tw"><table class="t">
    <tr><th>Paper</th><th>Format</th><th>AO1 share</th><th>What it looks like</th></tr>
    <tr><td><b>Paper 1</b></td><td>40 multiple-choice questions, 1 hour, 40 marks</td><td>50%</td><td>Recognise definitions, identify terms, choose the correct formula or example</td></tr>
    <tr><td><b>Paper 2, Section A</b></td><td>Question 1 (20 marks), parts (a) to (f), based on an unseen extract</td><td>about 40%</td><td>Short parts: define, identify, state, calculate from the data</td></tr>
    <tr><td><b>Paper 2, Section B</b></td><td>Three questions from four, each 20 marks (a) to (d)</td><td>about 40%</td><td>Parts (a) and (b): definitions, identifications, calculations</td></tr>
  </table></div>

  <h2>Command words that test AO1</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it means</th><th>What to write</th></tr>
    <tr><td><b>Define</b></td><td>Give precise meaning</td><td>One accurate sentence with the key terms; 2 marks: usually one mark for each key idea</td></tr>
    <tr><td><b>Identify</b></td><td>Name, select or recognise</td><td>Just the name or choice; no explanation needed</td></tr>
    <tr><td><b>State</b></td><td>Express in clear terms</td><td>A short, clear statement</td></tr>
    <tr><td><b>Give</b></td><td>Produce an answer from a source or from memory</td><td>The fact or example asked for</td></tr>
    <tr><td><b>Calculate</b></td><td>Work out from given facts or figures</td><td>Formula, working and the answer with units</td></tr>
    <tr><td><b>Describe</b></td><td>State the points of a topic; give characteristics and main features</td><td>The main features, with no need for reasons</td></tr>
  </table></div>

  <h2>Habits that secure AO1 marks</h2>
  <ul>
    <li><b>Learn definitions word for word</b> from the syllabus terms: the exact key words earn the marks.</li>
    <li>Learn the <b>formulas</b> (PED, PES, total revenue, ATC, inflation, unemployment rate) and always show <b>working</b>.</li>
    <li>Use <b>economic terminology</b> in every answer: say "opportunity cost", "quantity demanded", "price elastic", not everyday words.</li>
    <li>Match your answer <b>length to the marks</b>: 1 mark per point, no extras.</li>
    <li>In multiple-choice, <b>cross out wrong options</b>; check units and signs in calculations.</li>
  </ul>
  <p class="note">One mark is roughly <b>1.5 minutes</b> in Paper 2 (80 marks in 120 minutes). A 2-mark define should take about 3 minutes, including reading the question.</p>
'''
steppers = [
  ("Building a 2-mark definition", "--accent", ["Read the command word: Define", "Recall the key terms from the syllabus", "Write one sentence with both key ideas", "Check each key idea is a separate mark", "Move on: do not add explanation"]),
  ("A full calculation answer", "--good", ["Read the question: Calculate PED", "Write the formula: %ΔQd ÷ %ΔP", "Work out each percentage change", "Divide to get the answer", "State the result with its meaning (e.g. −1.5: elastic)"]),
]
lab1 = dict(title="Time budget for Paper 2", intro="Paper 2 is 80 marks in 120 minutes. Set the marks for a question and see how long to spend, leaving 10 minutes to check.", rl=["Time for the question", "Minutes per mark", "Spare time overall"],
  sliders=[("Marks for the question", 1, 20, 1, 6, "v"), ("Total marks on the paper", 40, 80, 10, 80, "v"), ("Time on the paper (minutes)", 60, 120, 10, 120, "v")],
  fn="const per = (v[2] - 10) / v[1], t = per * v[0]; return { r: [t.toFixed(1) + ' min', per.toFixed(2), '10 min'], t: 'With ' + v[1] + ' marks in ' + v[2] + ' minutes and 10 minutes kept for checking, you have about ' + per.toFixed(2) + ' minutes per mark. A ' + v[0] + '-mark question deserves about ' + t.toFixed(1) + ' minutes. Short AO1 parts (define, identify, calculate) should take less than this, which leaves more time for the longer analysis and evaluation parts.', bars: [['Time for question', t, '--accent', t.toFixed(1) + ' min'], ['Min per mark ×5', per * 5, '--good', per.toFixed(2)], ['Checking time', 10, '--warn']] };")
lab2 = dict(title="Command word decoder", intro="Pick a command word to see what to write and a model start.", h1="What to write", h2="Example",
  items=[("Define", "One precise sentence with the key terms", "Opportunity cost is the next best alternative given up."), ("Identify", "Just the name or choice", "Two free goods: sunlight and air."), ("State", "A short clear statement", "State one function of money: a medium of exchange."), ("Give", "A fact or example asked for", "Give one example of a tertiary sector firm: a bank."), ("Calculate", "Formula, working, answer, units", "PED = −30% ÷ +20% = −1.5."), ("Describe", "Main features or characteristics", "A monopoly has one seller and high barriers to entry.")])
cl = [("Which <b>command word</b> asks for each response?", ["Define", "Identify", "Calculate"], [("A precise meaning in one sentence", 0), ("Just the name of the term", 1), ("Formula, working and answer", 2), ("The key terms in a sentence", 0), ("Pick the correct item from the data", 1), ("Work out from given figures", 2)], "Match the command word."),
      ("Is each skill <b>AO1</b>, <b>AO2</b> or <b>AO3</b>?", ["AO1 Knowledge", "AO2 Analysis", "AO3 Evaluation"], [("Define inflation", 0), ("Use the formula for total revenue", 0), ("Explain how a tax raises prices using a chain of reasoning", 1), ("Interpret data from an extract", 1), ("Weigh two sides and reach a conclusion", 2), ("Recognise that outcomes are uncertain", 2)], "Know the three objectives.")]
match = [["Define", "Give precise meaning"], ["Identify", "Name, select or recognise"], ["State", "Express in clear terms"], ["Give", "Produce an answer from a source or memory"], ["Calculate", "Work out from given facts or figures"], ["Describe", "State the points or features of a topic"]]
order = ("Put the steps in order: <b>answering a calculate question</b>.", ["Read the question and find the data", "Write the formula", "Substitute the figures", "Work out the answer", "Add the unit or a short interpretation"], "Show the working.")
calcs = [("Paper 2 is 80 marks in 120 minutes. How many minutes per mark (1 decimal place)?", 1.5, "120 ÷ 80 = <b>1.5</b>.", None, None), ("A question is worth 6 marks. How many minutes should you spend at 1.5 minutes per mark?", 9, "6 × 1.5 = <b>9</b>.", None, None), ("AO1 is 43% of a qualification. Out of 100 marks of weighting, how many are AO1?", 43, "<b>43</b>.", None, None)]
mcq = [("AO1 stands for:", ["Analysis", "Knowledge and understanding", "Evaluation", "Application"], 1, "Assessment Objective 1."), ("Which command word asks for a precise meaning?", ["Describe", "Define", "Discuss", "Analyse"], 1, "Define."), ("In a Calculate question you should show:", ["Only the answer", "Formula, working and answer", "A diagram", "A conclusion"], 1, "Working earns marks."), ("What share of Paper 1 is AO1?", ["10%", "40%", "50%", "100%"], 2, "Paper 1 is 50% AO1."), ("A 2-mark Identify question needs:", ["A long paragraph", "Two names or choices", "An evaluation", "A diagram"], 1, "Keep it short.")]
cards = [("AO1", "Knowledge and understanding of definitions, formulas, concepts and theories, and use of terminology."), ("Define", "Give precise meaning."), ("Identify", "Name, select or recognise."), ("State", "Express in clear terms."), ("Give", "Produce an answer from a given source or from memory."), ("Calculate", "Work out from given facts, figures or information."), ("Describe", "State the points of a topic; give characteristics and main features."), ("Terminology", "Using the correct economic words."), ("Formula", "A rule for calculating a quantity.")]
exam_qs = [
  Q(1, "Define", 2, "Define opportunity cost.", "Next best alternative given up.", "[K|Opportunity cost is the next best alternative] [K|given up when a choice is made.]"),
  Q(2, "Define", 2, "Define price elasticity of demand.", "Responsiveness of quantity demanded to price.", "[K|Price elasticity of demand is a measure of the responsiveness] [K|of quantity demanded to a change in price.]"),
  Q(3, "Identify", 2, "Identify two functions of money.", "Medium of exchange, store of value.", "[K|Medium of exchange.] [K|Store of value (or measure of value or deferred payment).]"),
  Q(4, "Calculate", 3, "The price of a good rises from $10 to $12 and quantity demanded falls from 100 to 70. Calculate price elasticity of demand.", "%ΔQd ÷ %ΔP.", "[A|%ΔP = 2 ÷ 10 × 100 = 20%; %ΔQd = −30 ÷ 100 × 100 = −30%.] [A|PED = −30 ÷ 20] [A|= −1.5.]"),
  Q(5, "Calculate", 2, "A firm sells 200 units at $5 each and has total costs of $700. Calculate its profit.", "TR − TC.", "[A|TR = 5 × 200 = $1,000.] [A|Profit = 1,000 − 700 = $300.]"),
]
tips_ = [("Learn the exact definitions.", "Key terms earn the marks."), ("Show formula, working and unit.", "Even for 1 mark."), ("Match length to marks.", "1.5 minutes per mark."), ("Use terminology.", "Not everyday words."), ("In Paper 1, eliminate wrong options.", "Then check the calculation.")]
real_items = [("Past-paper define questions", "Questions such as 'Define market failure' or 'Define a free good' appear in every series and are worth 2 marks.", "AO1 recall."), ("Calculation parts", "Many Section A parts ask you to calculate a balance or a percentage from the extract.", "Calculate."), ("Multiple choice", "Paper 1 questions test definitions and formulas across all 40 questions.", "AO1 in Paper 1."), ("Revision flashcards", "Learning definitions with cards is one of the quickest ways to gain AO1 marks.", "Retrieval practice.")]
review("ig-ao1-knowledge", "z71", "Exam technique", "AO1 Knowledge and Understanding: Securing the Recall Marks", "Definitions, formulas and terminology: what AO1 tests, which command words signal it and how to earn every mark. Assessment Objective 1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Identify", "Calculate"], real_items)

# ---------------------------------------------------------------- AO2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><b>AO2 is analysis</b>: selecting and using information and data, applying economics to the <b>context</b> (written, numerical, diagrammatic and graphical) and <b>developing links and relationships</b>, that is, showing <b>why</b> and <b>how</b> one thing leads to another. It is <b>47% of the whole IGCSE</b>, <b>50% of Paper 1</b> and <b>45% of Paper 2</b>, the largest AO. Command words: <b>Explain</b> and <b>Analyse</b>.</p></div>

  <h2>Explain and analyse</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it means</th><th>What earns marks</th></tr>
    <tr><td><b>Explain</b></td><td>Set out purposes or reasons; make relationships clear; say why or how, supported with evidence</td><td>A point plus a <b>developed reason</b>: "because… so…" (about 2 marks per developed point)</td></tr>
    <tr><td><b>Analyse</b></td><td>Examine in detail to show meaning, identify elements and the relationships between them</td><td>A <b>chain of reasoning</b> of at least three links, <b>applied to the context</b>; for 6 marks usually two chains</td></tr>
  </table></div>

  <h2>The chain of reasoning</h2>
  <p>A good analysis follows a <b>chain</b>: <b>Point → Because → Therefore → So</b>.</p>
  <div class="card"><p><b>Question:</b> Analyse how a rise in the price of oil may affect a country's inflation rate.<br>
  <b>Chain:</b> Oil is a cost of production for many firms → higher oil prices raise costs → firms cut supply or raise prices → the general price level rises → inflation increases (cost-push).</p></div>
  <ul>
    <li><b>Start with the cause</b> from the question, not with a definition.</li>
    <li>Each link should <b>follow logically</b> from the one before.</li>
    <li>End with the <b>effect asked for</b> (inflation, unemployment, price, quantity).</li>
  </ul>

  <h2>Using the context, data and diagrams</h2>
  <ul>
    <li><b>Select</b> the relevant figures from the extract and <b>quote</b> them.</li>
    <li><b>Interpret</b> trends (rising, falling, compared with another country) and calculate if asked.</li>
    <li><b>Apply</b> theory to the named country, industry or firm.</li>
    <li>In <b>diagram</b> questions: draw the curves, label axes and curves, show the shift, mark the new equilibrium and <b>explain it in words</b>.</li>
  </ul>
  <p class="note">An answer that could be about any country scores less than one that mentions the <b>named product, place or figures</b> in the question.</p>
'''
steppers = [
  ("A developed chain of reasoning", "--accent", ["Oil prices rise (the cause in the question)", "Firms' costs of production increase", "Firms raise prices or cut supply", "The general price level rises", "Inflation increases: the effect asked for"]),
  ("Using data from the extract", "--good", ["Read the extract and find the relevant figures", "Quote them: 'unemployment rose from 5% to 8%'", "Interpret the trend: fewer people in work", "Link to the economics: lower spending, lower AD", "Use it to support the argument"]),
  ("A demand and supply diagram answer", "--warn", ["Draw D and S with axes labelled", "Mark the original equilibrium P, Q", "Shift the curve affected and label it (S₁)", "Mark the new equilibrium P₁, Q₁", "Explain the change in words"]),
]
lab1 = dict(title="Marks for an analysis answer", intro="Estimate the marks for a 6-mark Analyse answer from the quality of the chain (a simple model of how examiners reward development).", rl=["Estimated marks", "Level of analysis", "Next step"],
  sliders=[("Number of separate points made", 1, 4, 1, 2, "v"), ("Links developed per point (1 to 5)", 1, 5, 1, 3, "v"), ("Use of the context or data (1 none, 5 strong)", 1, 5, 1, 3, "v")],
  fn="const dev = Math.min(v[0], 2) * Math.min(v[1], 3), ctx = v[2] >= 3 ? 1 : 0, m = Math.min(6, Math.round(dev * 0.7 + ctx + (v[0] > 2 ? 0 : 0))), lvl = m >= 5 ? 'Developed and applied' : m >= 3 ? 'Some development' : 'Mostly description', nx = v[1] < 3 ? 'Develop each point into at least three links' : v[2] < 3 ? 'Use figures or names from the extract' : v[0] < 2 ? 'Add a second chain' : 'Add a diagram or check the logic'; return { r: [m + '/6', lvl, nx], t: v[0] + ' point' + (v[0] > 1 ? 's' : '') + ' with ' + v[1] + ' link' + (v[1] > 1 ? 's' : '') + ' each and ' + (v[2] >= 3 ? 'good' : 'weak') + ' use of context score about ' + m + ' out of 6 (illustrative). More than two points does not raise the mark; deeper chains and use of context do. Next: ' + nx.toLowerCase() + '.', bars: [['Points (max 2 count)', Math.min(v[0], 2), '--accent'], ['Links per point', Math.min(v[1], 5), '--good'], ['Context use', v[2], '--warn'], ['Marks', m, '--bad']] };")
lab2 = dict(title="Weak versus strong", intro="Pick a question to see a weak answer and how to improve it.", h1="Weak answer", h2="Stronger answer",
  items=[("Analyse how a subsidy affects the market for solar panels", "A subsidy is money from the government.", "A subsidy lowers costs, so supply shifts right; price falls and quantity rises, so more solar panels are bought."), ("Explain why unemployment may rise in a recession", "Unemployment is people without jobs.", "Falling demand makes firms cut output, so they need fewer workers and lay some off."), ("Analyse a rise in the price of milk on producers' revenue", "Milk is a food.", "A higher price means each litre earns more, but quantity falls; if demand is inelastic, revenue rises."), ("Explain why a monopoly may charge a high price", "A monopoly is one firm.", "With no rivals and high barriers to entry, it can raise the price without losing customers."), ("Analyse how a fall in the exchange rate affects exports", "The exchange rate is the price of a currency.", "Exports become cheaper abroad, so foreign demand rises and export revenue increases.")])
cl = [("Is each a <b>description</b> or <b>analysis</b>?", ["Description", "Analysis"], [("A subsidy is a payment to producers", 0), ("Unemployment is people without jobs", 0), ("Higher costs mean firms cut supply, so prices rise", 1), ("Falling demand leads to job cuts and lower incomes", 1), ("Inflation is a rise in the price level", 0), ("Higher wages raise costs, so firms raise prices, so inflation rises", 1)], "Analysis shows how and why."),
      ("Which <b>connective</b> signals a link in a chain?", ["Links in a chain", "Not a link"], [("because", 0), ("so", 0), ("which leads to", 0), ("as a result", 0), ("for example", 1), ("also", 1)], "Use linking words.")]
match = [["Explain", "Say why or how, with support"], ["Analyse", "Examine in detail to show relationships"], ["Chain of reasoning", "Linked steps from cause to effect"], ["Application", "Using the context in the question"], ["Data interpretation", "Selecting and reading figures"], ["Diagram", "A labelled graph showing an economic change"]]
order = ("Put the chain in order: <b>how a tax on cigarettes reduces smoking</b>.", ["The government raises the tax on cigarettes", "Producers' costs rise, so supply shifts left", "The market price of cigarettes rises", "Smokers can afford fewer cigarettes", "Quantity demanded falls"], "Link each step.")
calcs = [("An extract says GDP rose from $200bn to $212bn. What is the growth rate (%)?", 6, "12 ÷ 200 × 100 = <b>6%</b>.", None, None), ("Unemployment rose from 5% to 8%. By how many percentage points?", 3, "8 − 5 = <b>3</b> percentage points.", None, None), ("Prices rose from an index of 100 to 104. What is the inflation rate (%)?", 4, "4 ÷ 100 × 100 = <b>4%</b>.", None, None)]
mcq = [("AO2 stands for:", ["Knowledge", "Analysis", "Evaluation", "Recall"], 1, "Assessment Objective 2."), ("A chain of reasoning means:", ["One long sentence about definitions", "Linked steps from cause to effect", "A list of facts", "A conclusion only"], 1, "Point, because, so."), ("In an extract question you should:", ["Ignore the data", "Use figures and names from the extract", "Write about another country", "Draw only"], 1, "Application."), ("Analyse means:", ["Give a short answer", "Examine in detail to show relationships", "Name a term", "State a value"], 1, "Detailed relationships."), ("In a diagram answer you should also:", ["Say nothing", "Explain the change in words", "Add three more diagrams", "Skip labels"], 1, "Diagram plus words.")]
cards = [("AO2", "Analysis: selecting and applying economic information and developing links and relationships."), ("Explain", "Set out reasons; say why or how, supported with evidence."), ("Analyse", "Examine in detail to show meaning and the relationships between elements."), ("Chain of reasoning", "A sequence of linked steps from cause to effect."), ("Application", "Using the context in the question."), ("Context", "The country, industry or information given."), ("Data", "Figures in the extract, tables or graphs."), ("Link", "A step that connects one idea to the next."), ("Diagram", "A labelled graph showing an economic change.")]
exam_qs = [
  Q(1, "Explain", 4, "Explain why a rise in the price of a good may reduce the quantity demanded.", "Substitution; income; reasoning.", "[K|A higher price makes the good dearer relative to substitutes.] [N|Consumers switch to cheaper alternatives, so they buy less.] [K|Their income buys fewer units at a higher price.] [N|So quantity demanded falls, a movement up along the demand curve.]"),
  Q(2, "Analyse", 6, "Analyse how a rise in the price of oil may affect a country's inflation rate.", "Cost-push chain.", "[K|Oil is a cost for many firms, such as transport and manufacturing.] [N|A higher oil price raises their costs of production.] [N|Firms raise prices or cut supply to protect profit.] [N|The general price level rises, so inflation increases (cost-push inflation).] [E|The effect depends on how much firms rely on oil and on whether costs are passed on.]", key=True),
  Q(3, "Analyse", 6, "Analyse, using a demand and supply diagram, how a subsidy for solar panels could affect the market.", "S right; lower price; higher quantity.", "[K|A subsidy lowers producers' costs, so supply increases and S shifts right to S₁.] [N|At the old price there is a surplus, so the price falls to P₁.] [N|The quantity bought and sold rises to Q₁.] [N|Consumers pay less and buy more solar panels.] [E|The cost to the government is an opportunity cost.]", key=True),
  Q(4, "Analyse", 4, "The extract says unemployment rose from 5% to 8% in 2020. Analyse how higher unemployment may affect a country's economy.", "Use the data; link to income and demand.", "[K|Unemployment rose by 3 percentage points to 8%, so more people have no earned income.] [N|Their spending falls, so firms lose sales.] [N|Firms cut output and may lay off more workers, so aggregate demand and growth fall.]"),
]
tips_ = [("Use a chain: cause, because, so, therefore.", "At least three links."), ("Use the context.", "Quote figures and names."), ("Label diagrams and explain them in words.", "Both earn marks."), ("Explain and analyse: stay on the question.", "No long definitions."), ("Check the final link answers the question.", "Inflation, price, jobs.")]
real_items = [("Section A extracts", "Question 1 gives a real economic situation with text and data to analyse.", "Context and data."), ("Diagram parts", "Section B often asks to analyse using a demand and supply diagram.", "Diagram analysis."), ("Oil price shocks", "A classic chain: costs, prices, inflation.", "Chain of reasoning."), ("Calculation then analysis", "Calculate a change from the extract, then explain its effect.", "Data plus theory.")]
review("ig-ao2-analysis", "z72", "Exam technique", "AO2 Analysis: Chains of Reasoning and Context", "Explain and Analyse: building developed chains of reasoning and applying them to data, context and diagrams. Assessment Objective 2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Explain", "Analyse"], real_items)
