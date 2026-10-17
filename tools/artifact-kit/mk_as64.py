"""AS syllabus 6.2.3 Arguments for and against protectionism. Run: python3 tools/artifact-kit/mk_as64.py"""
from as6k import *
EY = EYAS("6.2.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Governments use protectionism for several reasons. The main <b>arguments for</b> are to protect <b class="kw">infant (sunrise) industries</b> while they grow to a size where they can compete, to give <b class="kw">declining (sunset) industries</b> time to adjust and for workers to find new jobs, to protect <b class="kw">strategic industries</b> (such as defence or food) that matter for national security, to prevent <b class="kw">dumping</b> (selling below cost in another country), to <b>reduce a current account deficit</b> and to <b>raise government revenue</b> through tariffs. The main <b>arguments against</b> (and for free trade) are that protection <b>reduces specialisation</b> and so output, <b>misallocates resources</b>, <b>raises prices</b> and <b>limits consumer choice</b>, may protect <b>inefficient firms</b>, invites <b>retaliation</b> and lowers living standards. Whether the case for protection is stronger depends on the <b>industry, the country, the size of the effects and how long the protection lasts</b>.</p></div>

  <h2>1 · Arguments for protectionism</h2>
  <div class="tw"><table class="t">
    <tr><th>Argument</th><th>The idea</th><th>The weakness</th></tr>
    <tr><td><b>Infant industry</b></td><td>A new industry cannot yet get economies of scale, so temporary protection lets it grow</td><td>It may never become efficient, and the protection can be hard to remove</td></tr>
    <tr><td><b>Declining industry</b></td><td>Slows the decline so that workers and capital can move to other uses gradually</td><td>Delays necessary change and keeps resources in a failing industry</td></tr>
    <tr><td><b>Strategic industry</b></td><td>Keeps control of industries vital for security, such as defence, energy or food</td><td>"Strategic" can be stretched to cover almost any industry</td></tr>
    <tr><td><b>Anti-dumping</b></td><td>Prevents foreign firms selling below cost to drive out domestic rivals</td><td>Hard to prove dumping; consumers lose cheap goods</td></tr>
    <tr><td><b>Current account deficit</b></td><td>Cutting imports can reduce a deficit</td><td>Retaliation and inelastic demand for imports can cancel the effect</td></tr>
    <tr><td><b>Government revenue</b></td><td>Tariffs raise tax income, especially where other taxes are hard to collect</td><td>The revenue falls if the tariff is high enough to cut imports sharply</td></tr>
  </table></div>

  <h2>2 · Arguments against protectionism</h2>
  <ul>
    <li><b>Lower specialisation and output:</b> the gains from comparative advantage are reduced, so world output and growth are lower.</li>
    <li><b>Misallocation of resources:</b> resources stay in less efficient domestic industries.</li>
    <li><b>Higher prices and less choice</b> for consumers, which can lower living standards.</li>
    <li><b>Reduced competition:</b> protected firms may have less incentive to cut costs or innovate (X-inefficiency).</li>
    <li><b>Retaliation and trade wars:</b> exporters in the protecting country may lose markets.</li>
    <li><b>Higher costs</b> for firms that use imported inputs.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For "assess" questions, <b>explain both sides in context</b> (a developing economy, a particular industry), then <b>judge</b>: the case for protection is strongest for <b>temporary</b> support of a <b>specific</b> industry, and weaker as a long-term, wide policy. Use "may" and "could".</div>
'''

watch = watch_html("Infant industry protection", "How protection can backfire")

explore = chooser_html("g", "Lab 1 · Judge the argument", "Choose an argument for protectionism to see its best case, its limit and how strong it tends to be.", ["Best case", "Main limit", "Key condition"]) + chooser_html("h", "Lab 2 · Which side is stronger here?", "Choose a situation to see which side of the debate may be stronger and why.", ["Likely stronger side", "Main reason", "What would change this"])

practise = practise_html("Argument for or against protectionism?", "Match the argument to its description", "Put infant industry protection in order")

real = RWNOTE + (
rw("A new car maker", "A country with no car industry protects a start-up manufacturer with a tariff while it builds scale. If its costs fall, it may compete without help; if they do not, consumers may be paying more for years.", "the infant industry argument and its risk.") +
rw("Farming and food security", "Many governments support domestic farming to protect food supply in a crisis. Critics say the support raises prices and protects less efficient farms.", "the strategic industry argument.") +
rw("Cheap steel imports", "Domestic producers claim foreign steel is sold below cost. An anti-dumping duty may protect jobs but raises costs for car and construction firms.", "dumping and its trade-offs.") +
rw("A shrinking coal industry", "A government slows the closure of mines to give workers time to retrain. Critics say it delays change and costs taxpayers.", "the declining industry argument.")
)

mc_exam = [
  mcq("s25_12", 26, "Which statement is not a valid reason why a country may impose protectionist measures?", ["to allow a newly developed domestic industry to grow to a viable size", "to enable a country to retain control of an industry it regards as being of strategic importance", "to give consumers a wider choice of goods and services", "to give time for workers in a declining domestic industry to find alternative employment"], 2, "Protection restricts imports, so it narrows rather than widens consumer choice."),
  mcq("s25_13", 26, "Which argument in favour of protectionism is not generally regarded as economically valid?", ["Once the protected industry becomes established, it will produce efficiently.", "It prevents heavily subsidised imports from competing unfairly against domestic goods.", "It provides time for the protected industry's workers to be retrained for other work.", "It increases the standard of living of the population in general."], 3, "Protection usually raises prices, so it is not generally accepted that it raises living standards across the population."),
  mcq("s21_13", 20, "What is not an aim of protectionism?", ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], 1, "Protectionism aims to cut imports and protect industries, not to raise export prices."),
  mcq("w20_12", 20, "In which economic context is the term 'protectionism' usually applied?", ["the protection of consumers against excessive prices", "the protection of employees against exploitation by multinational companies", "the protection of local producers against foreign competitors", "the protection of the foreign exchange rate against currency speculators"], 2, "Protectionism shields local producers from foreign competition."),
  mcq("w24_12", 28, "What is not an example of protectionism?", ["the European Union (EU) requiring goods imported into member states to meet safety standards", "the Pakistan government increasing the rate of goods and services tax (GST) on some exported goods from 2% to 5%", "the Nigeria government banning the import of packaged sugar", "the US imposing a 35% tariff on tyres imported from China"], 1, "A tax on exports does not protect domestic producers from import competition."),
  mcq("w24_13", 28, "Two statements describing forms of protectionism a government can use are listed. Statement 1: there is a total ban on imports. Statement 2: all imported goods have to be of a specified standard. Which combination correctly describes these two statements? (statement 1, statement 2)", ["administrative barrier, import quota", "administrative barrier, embargo", "embargo, administrative barrier", "embargo, import quota"], 2, "A total ban is an embargo; a required standard is an administrative barrier.")
]

exam = exam_page("arguments for and against protectionism",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). This topic appears as a 12 mark Paper 2 evaluation question in most series, each asking whether the arguments for protection or free trade are stronger. The three questions below are reworded, together with six Paper 1 multiple choice questions.",
  [("Essay parts, 12 marks", "3", "May/June 2023 (21) Q5(b); May/June 2024 (22) Q5(b); May/June 2025 (21) Q4(b)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2025")],
  [
  eq(P("s23_21", "5(b)"), "12 marks", "Assess whether the arguments for protectionism in the context of international trade are always stronger than the arguments against.",
     ["Analysis (up to 8): explanation of the arguments for protectionism, such as infant and sunrise industries, declining and sunset industries, strategic industries, preventing dumping, reducing a current account deficit and raising revenue (up to 4); the arguments against, such as greater specialisation and output from free trade, more efficient resource allocation, wider consumer choice and higher living standards (up to 4).",
      "Evaluation (up to 4): considers the issues with protectionism and the relative strength of the arguments, and concludes which approach could be better for particular economic situations."],
     "For: infant, declining, strategic, dumping, deficit, revenue. Against: lost specialisation, misallocation, prices, choice. Judge: depends on the situation.",
     [[("n", "Protectionism may be justified to protect an infant industry that needs time to reach economies of scale, to slow the decline of a sunset industry so that workers can retrain, to protect strategic industries and to stop dumping. But protection reduces the gains from specialisation, keeps resources in less efficient firms, raises prices and reduces consumer choice, so living standards could fall.")], [("e", "The arguments for protection are not always stronger. They are most convincing for temporary help to a specific industry or for security, and least convincing as a broad long-term policy that could invite retaliation. Which side is stronger may depend on the industry, the length of protection and the country's circumstances.")]]),
  eq(P("s24_22", "5(b)"), "12 marks", "Assess whether free trade is always better than a policy of protectionism for a developing economy that wishes to trade internationally.",
     ["Analysis (up to 8): the advantages and disadvantages of free trade and of protectionism, both in the context of a developing economy. Advantages of free trade may include efficient allocation from specialisation, use of different factor endowments, competitive pressure on costs and prices, and economies of scale and choice; disadvantages may include over-exploitation of scarce resources, closure of domestic industries and unemployment, and dumping or unfair competition. Maximum Level 2 if not in the context of a developing economy.",
      "Evaluation (up to 4): a judgement on whether free trade is always better, with a conclusion."],
     "Free trade: specialisation, competition, scale. Risks: industries close, dumping, resource use. Protection: infant industries. Judge: depends on the economy and time.",
     [[("n", "For a developing economy, free trade may allow it to use its factor endowments, such as cheap labour or natural resources, and to gain from specialisation. Competition from abroad could push domestic firms to lower costs and consumers may get lower prices and more choice. But young industries may be unable to compete and could close, raising unemployment, and dumping by foreign firms may be a risk. Protection could give infant industries time to grow, but could raise prices, reduce competition and lead to inefficient firms.")], [("e", "Free trade is not always better. It may be more beneficial for developing economies with a clear comparative advantage, while temporary and targeted protection could help young industries. The best policy may be a mix that changes as the economy develops.")]]),
  eq(P("s25_21", "4(b)"), "12 marks", "Assess whether the potential benefits of free trade always outweigh the arguments for protectionism.",
     ["Analysis (up to 8): the potential benefits of free trade, such as an increase in world output, more efficient allocation through specialisation, lower costs, wider choice, economic growth and improved living standards (up to 4); the arguments for protectionism, such as the infant industry argument, declining or sunset industries, strategic industries, a current account deficit and anti-dumping (up to 4).",
      "Evaluation (up to 4): balanced consideration of alternatives, explaining which is stronger in particular circumstances, with a conclusion."],
     "Free trade: output, efficiency, cost, choice, growth. Protection: infant, sunset, strategic, deficit, dumping. Judge: benefits may usually outweigh, but not always.",
     [[("n", "Free trade could raise world output because countries specialise where they have a comparative advantage. Resources are allocated more efficiently, costs may fall and consumers may enjoy a wider choice and higher living standards. But infant industries may need temporary protection to grow, sunset industries may need time to adjust, strategic industries may matter for security and a deficit could be reduced by cutting imports. Anti-dumping measures may stop unfair competition.")], [("e", "The benefits of free trade may often outweigh the case for protection, especially over a long time, but not always. Protection can be justified when it is temporary, targeted and unlikely to provoke retaliation, such as support for a genuinely strategic industry.")]])
  ],
  )

tips = tips_html(
  [("Give both sides.", "Arguments for and against, in context."),
   ("Name the arguments.", "Infant, sunset, strategic, dumping, deficit, revenue."),
   ("Explain, don't list.", "One or two developed points, not a long list."),
   ("Use the context.", "A developing economy or a named industry."),
   ("Evaluate.", "Temporary versus permanent, targeted versus broad."),
   ("Mention retaliation.", "Exporters may lose markets."),
   ("Conclude.", "Which side is stronger, and when.")],
  [("Infant industry", "An infant industry is a new industry that may need temporary protection to grow."),
   ("Sunset industry", "A sunset industry is in long-term decline."),
   ("Strategic industry", "A strategic industry is important for national security."),
   ("Dumping", "Dumping is selling goods abroad at below cost."),
   ("Retaliation", "Retaliation is when trading partners respond with their own barriers.")],
  [CW["define"], CW["explain"], CW["assess"], CW["discuss"]]) + FC

js = CHAINJS + '''
chainStep("#stA", "How infant industry protection is meant to work", ["A new industry cannot compete with established foreign firms", "A tariff or quota protects it from import competition", "It grows and gains economies of scale", "Costs fall and it becomes efficient", "Protection is removed and the industry competes alone"], [
  "<b>The problem:</b> a new industry has high unit costs because it is small.", "<b>Temporary protection</b> raises the price of imports, so domestic sales can grow.", "<b>Growth</b> lets the firm spread its fixed costs and gain economies of scale.", "<b>Falling unit costs</b> may allow it to match foreign prices.", "<b>In theory</b> the protection ends and the industry competes without help."]);
chainStep("#stB", "How protection may reduce welfare", ["The government protects an industry for a long time", "Less competition reduces the pressure to cut costs", "The industry may remain inefficient (X-inefficiency)", "Consumers pay higher prices and have less choice", "Trading partners may retaliate against exports"], [
  "<b>Long protection</b> may become hard to remove because the industry lobbies to keep it.", "<b>Less competition</b> reduces the incentive to innovate.", "<b>Costs stay high</b>, so the industry may never become competitive.", "<b>Higher prices</b> reduce real incomes and living standards.", "<b>Retaliation</b> can hurt exporters, and the country may end up worse off overall."]);

chooser("g", [
  ["Infant industry", "Temporary support lets a new industry reach scale", "May never become efficient; hard to remove", "Time limit and a realistic path to lower costs", 4],
  ["Declining industry", "Gives workers and capital time to move", "Delays change and wastes resources", "Support should be short and linked to retraining", 3],
  ["Strategic industry", "Secures supply of defence or food", "Almost any industry may be called strategic", "A genuine security risk and no alternative suppliers", 4],
  ["Anti-dumping", "Stops sales below cost that drive out rivals", "Hard to prove; consumers lose cheap goods", "Clear evidence of below-cost selling", 3],
  ["Current account deficit", "Fewer imports may narrow the deficit", "Retaliation; inelastic demand; does not fix the cause", "Elastic demand for imports and no retaliation", 2],
  ["Government revenue", "Tariffs can raise tax income", "A high tariff reduces imports and so revenue", "Limited alternative sources of tax", 2]
], (it) => `${it[0]}: the best case is that ${it[1].toLowerCase()}. The limit is that ${it[2].toLowerCase()}. It is strongest when ${it[3].toLowerCase()}.`);

chooser("h", [
  ["Young manufacturing industry in a developing economy", "Protection (temporary and targeted)", "Cannot reach scale against established foreign firms", "A clear plan for removal, and whether costs actually fall", 4],
  ["Large efficient exporter", "Free trade", "Gains from specialisation are large and retaliation would hurt exports", "A sudden surge of dumped imports", 4],
  ["Food supply in a small island economy", "Some protection (strategic)", "Security of supply matters in a crisis", "Whether imports can be stored or diversified", 3],
  ["Long-declining coal industry", "Short-term protection, then free trade", "Gives workers time to retrain", "Whether the support lasts for decades", 3],
  ["Country with a large current account deficit", "Depends on causes", "Protection may not fix weak competitiveness", "Elasticity of demand for imports and retaliation", 2]
], (it) => `In "${it[0].toLowerCase()}", the stronger side may be: ${it[1].toLowerCase()}. The main reason: ${it[2].toLowerCase()}. This could change with: ${it[3].toLowerCase()}.`);
''' + CLASSIFY("cl1", "Is this an argument for or against protectionism?", ["For protectionism", "Against protectionism"],
  [("It gives a new industry time to reach economies of scale", 0), ("It reduces specialisation and world output", 1), ("It stops foreign firms selling below cost", 0), ("It raises prices and reduces choice for consumers", 1), ("It protects industries vital for security", 0), ("It may provoke retaliation from trading partners", 1), ("It gives workers in a declining industry time to retrain", 0), ("It protects inefficient firms from competition", 1)],
  "The arguments for protect particular industries or aims; the arguments against stress efficiency, prices and retaliation.") + MATCH([
  ["Infant industry", "A new industry that may need temporary protection to grow"],
  ["Sunset industry", "An industry in long-term decline"],
  ["Strategic industry", "An industry important for national security"],
  ["Dumping", "Selling abroad at a price below cost"],
  ["Retaliation", "A trading partner's response with its own trade barriers"],
  ["X-inefficiency", "Lack of cost-cutting pressure when firms are protected from competition"]]) + ORDER(
  "Put the steps in the infant industry argument in order.",
  ["A new industry has high costs because it is small", "A tariff protects it from foreign competition", "Its sales grow and it gains economies of scale", "Unit costs fall", "Protection is removed and it competes on its own"],
  "Temporary protection should allow growth, scale and lower costs.") + CALC([
  {"q": "A country exports $600m and imports $800m of goods. What is the trade deficit ($m)?", "a": 200, "unit": "$m", "tol": 0.5, "hint": "800 - 600.", "sol": "<b>$200m</b>."},
  {"q": "A tariff cuts imports by 15% from $800m (exports unchanged at $600m). What is the new trade deficit ($m)?", "a": 80, "unit": "$m", "tol": 0.5, "hint": "Imports = 0.85 × 800 = 680.", "sol": "Imports $680m, so the deficit is <b>$80m</b>."},
  {"q": "A 20% tariff is charged on $500m of imports. What is the tariff revenue ($m)?", "a": 100, "unit": "$m", "tol": 0.5, "hint": "0.2 × 500.", "sol": "<b>$100m</b>."},
  {"q": "A foreign firm sells 1000 units at $60 against a cost of $80. How much below cost is the firm selling in total ($)?", "a": 20000, "unit": "$", "tol": 1, "hint": "(80 - 60) × 1000.", "sol": "<b>$20 000</b>."}]) + MCQ([
  ("An infant industry is:", ["A new industry that may need temporary protection", "A declining industry", "A foreign industry", "A government-owned industry"], 0, "Young and small."),
  ("Dumping means:", ["Selling below cost in another country", "Selling at high prices", "Banning imports", "Taxing exports"], 0, "A below-cost export."),
  ("An argument against protectionism is:", ["It may raise prices for consumers", "It protects infant industries", "It guards strategic industries", "It stops dumping"], 0, "Higher prices and less choice."),
  ("Protecting a sunset industry mainly aims to:", ["Give workers time to adjust", "Raise exports", "Cut taxes", "Increase competition"], 0, "Slows the decline."),
  ("A risk of protectionism is:", ["Retaliation by trading partners", "Lower tariffs abroad", "More competition", "Lower costs for protected firms"], 0, "Trading partners may respond.")
], "qz1") + CARDS([
  ("Infant industry", "New; needs time."),
  ("Sunset industry", "Declining; slow the fall."),
  ("Strategic industry", "Security."),
  ("Dumping", "Below-cost exports."),
  ("For protection", "Targeted and temporary."),
  ("Against protection", "Prices, efficiency, retaliation."),
  ("X-inefficiency", "No pressure to cut costs."),
  ("Judgement", "Depends on the context.")]) + MCQ(mc_exam)

build("as64", "as-protectionism-arguments", "Arguments for and Against Protectionism", EY,
  "6.2.3: the case for protecting infant, declining and strategic industries, the case against, and how to judge between them. Animated chains, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
