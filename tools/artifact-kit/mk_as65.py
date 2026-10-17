"""AS syllabus 6.3.3-6.3.4 Causes and consequences of current account imbalances. Run: python3 tools/artifact-kit/mk_as65.py"""
from as6k import *
EY = EYAS("6.3.3 to 6.3.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">current account deficit</b> means payments to the rest of the world for goods, services, income and transfers exceed receipts; a <b class="kw">surplus</b> means the opposite. Deficits may be caused by <b>strong domestic demand</b> and rising incomes (which pull in imports), <b>poor price or non-price competitiveness</b> (high costs, inflation, low productivity, low quality), a <b>high exchange rate</b>, a <b>deterioration in the terms of trade</b>, <b>weak world demand</b> for a country's exports, and <b>net outflows of income</b> such as profits sent abroad; surpluses are the opposite, often with <b>low domestic demand</b> or <b>high saving</b>. A persistent deficit could lead to <b>downward pressure on the exchange rate</b>, falling reserves or rising borrowing, <b>lower AD, output and jobs</b>, and pressure for contractionary policy; a surplus could raise AD and jobs but may also reflect weak spending and <b>harm trading partners</b>. How serious either is depends on <b>size, cause, how long it lasts and how it is financed</b>.</p></div>

  <h2>1 · Causes</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Effect on the current account</th></tr>
    <tr><td><b>Rapid growth and high consumer spending</b></td><td>Income elasticity of demand for imports pulls in imports (deficit)</td></tr>
    <tr><td><b>Low competitiveness</b> (high costs, low productivity, inflation above trading partners')</td><td>Exports fall and imports rise (deficit)</td></tr>
    <tr><td><b>High exchange rate</b></td><td>Exports dearer and imports cheaper (deficit)</td></tr>
    <tr><td><b>Fall in the terms of trade</b> or commodity prices</td><td>Export revenue falls relative to import costs (deficit)</td></tr>
    <tr><td><b>Weak growth abroad</b></td><td>Lower demand for exports (deficit)</td></tr>
    <tr><td><b>Primary income outflows</b></td><td>Profits and interest paid abroad exceed those received (deficit, even with a trade surplus)</td></tr>
    <tr><td><b>Low domestic spending or high saving</b></td><td>Low imports (surplus)</td></tr>
    <tr><td><b>Strong competitiveness or undervalued currency</b></td><td>Exports rise (surplus)</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>

  <h2>2 · Consequences</h2>
  <ul>
    <li><b>Deficit, domestic:</b> net exports lower AD, which could reduce output and employment; imports may raise living standards in the short run; if the deficit is persistent, contractionary policy may be needed to reduce it.</li>
    <li><b>Deficit, external:</b> a floating currency tends to <b>depreciate</b>; under a fixed rate the <b>reserves fall</b>; the country may need to <b>borrow or sell assets</b>, so more future income goes abroad as interest and profits.</li>
    <li><b>Surplus, domestic:</b> exports and AD may rise, with more jobs and growth; but a surplus can reflect weak domestic demand, and resources are used to produce for others rather than for domestic living standards.</li>
    <li><b>Surplus, external:</b> upward pressure on the exchange rate, which may erode competitiveness; partners' deficits may rise and lead to trade tension.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name the <b>cause</b> and say which part of the current account it affects (goods, services, primary or secondary income). For consequences, separate <b>domestic</b> and <b>external</b> effects, and evaluate with <b>size</b> and <b>persistence</b>.</div>
'''

watch = watch_html("How a deficit can build up", "What a persistent deficit may lead to")

explore = chooser_html("g", "Lab 1 · Choose a cause", "Choose a possible cause of a current account deficit to see how it works and how likely it is to be a persistent cause.", ["Effect on imports and exports", "Part of the account", "Why it may last"]) + chooser_html("h", "Lab 2 · Choose a consequence", "Choose a consequence to see who it affects, its likely size and what limits it.", ["Who is affected", "Direction", "What limits it"])

practise = practise_html("Deficit cause or surplus cause?", "Match the term to its description", "Put the effects of a persistent deficit in order")

real = RWNOTE + (
rw("A consumer boom", "Rising incomes and cheap credit lead households to buy more imported cars and electronics. Imports grow faster than exports, and the current account moves into deficit.", "strong demand pulling in imports.") +
rw("A commodity exporter", "A country selling mainly oil sees export income fall when oil prices drop. Its terms of trade worsen and the current account could move into deficit.", "a fall in commodity prices.") +
rw("A manufacturing exporter", "A country with high saving, strong exports and subdued consumer spending runs a surplus year after year. Its partners may complain, and its currency may be under upward pressure.", "a persistent surplus and its external effects.") +
rw("Profits sent abroad", "A country can have a surplus in goods but a current account deficit if foreign firms send large profits and interest abroad. This is a deficit on primary income.", "primary income outflows.")
)

mc_exam = [
  mcq("m24_12", 30, "What is not a likely cause of a deficit in the current account of the balance of payments?", ["Consumer spending is low.", "Primary incomes in the form of investment income are low.", "The rate of exchange is high.", "Wage costs of production are high."], 0, "Low consumer spending means fewer imports, which would tend to help the current account."),
  mcq("m25_12", 20, "High economic growth is often accompanied by a worsening of the current account of the balance of payments. Which reason for this trend is not valid?", ["Economic growth raises domestic consumption, leaving very little to sell to overseas consumers.", "Economic growth raises domestic output, leading to lower prices and more price-competitive goods both at home and abroad.", "Economic growth raises incomes and leads to rising demand for foreign goods.", "Economic growth results in rising requirements of inputs from other countries."], 1, "Lower prices and greater competitiveness would help rather than worsen the current account."),
  mcq("m24_12", 27, "An extract from a country's balance of payments ($ billion): trade in goods, exports 150 and imports 200; trade in services, exports 70 and imports 50; primary (investment) income, receipts 120 and payments 100; secondary (transfer) income, receipts 15 and payments 20. What is the current account balance?", ["-$10bn", "-$15bn", "-$30bn", "-$50bn"], 1, "(150 - 200) + (70 - 50) + (120 - 100) + (15 - 20) = -50 + 20 + 20 - 5 = -15."),
  mcq("s21_12", 23, "The figures are from New Zealand's balance of payments for 2017 (NZ$m): capital account balance 1300, current account balance -7000, financial account balance 7600, goods balance -3000, services balance 5000. What was the value of the balancing item (net errors and omissions) in NZ$m?", ["-3900", "-2000", "-1900", "5700"], 2, "The accounts sum to zero: -7000 + 1300 + 7600 + balancing item = 0, so the balancing item is -1900."),
  mcq("m20_12", 24, "A country with a floating exchange rate experiences a large surplus on the current account of its balance of payments. What is likely to decrease as a consequence?", ["exports of capital from the country", "the level of employment in the country", "the prices of imports into the country", "the value of the country's currency"], 2, "A surplus tends to raise demand for the currency, so the exchange rate rises and import prices fall."),
  mcq("s20_13", 27, "Why is a balance of payments deficit a potential problem for an economy with a fixed exchange rate?", ["Domestic money supply will increase.", "Rival economies may react with trade protection measures.", "The economy's foreign exchange reserves may decrease.", "The economy's short-run standard of living will be reduced."], 2, "Under a fixed rate the central bank buys the currency using reserves, which fall."),
  mcq("m21_12", 29, "Other things being equal, what is most likely to be reduced by falling labour productivity?", ["the balance of trade deficit", "the internal value of money", "the level of unemployment", "the rate of domestic inflation"], 1, "Lower productivity raises unit costs and prices, so the internal value of money falls.")
]

exam = exam_page("causes and consequences of current account imbalances",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Causes of a persistent deficit and the consequences of deficits and surpluses appear as 8 and 12 mark Paper 2 parts. Reworded past questions are below, with seven Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "May/June 2022 (23) Q4(a)"), ("Essay parts, 12 marks", "2", "Oct/Nov 2023 (23) Q5(b); Oct/Nov 2024 (21) Q5(b)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2025")],
  [
  eq(P("s22_23", "4(a)"), "8 marks", "Explain why some countries consistently have a deficit on the current account of the balance of payments.",
     ["Knowledge (up to 2): the current account is trade in goods, services plus other income (1); a deficit is where payments made by a country exceed payments received, or where income from exports is exceeded by expenditure on imports (1).",
      "Application (up to 6): explanation of causes of a current account deficit (up to 3), such as an appreciation of the exchange rate, a reduced supply of primary goods for export, a deterioration in the terms of trade, reduced aid, reduced transfers from migrant workers and increased protection from trading partners; and why some countries may experience a persistent deficit (up to 3)."],
     "Define the current account and a deficit. Causes: high exchange rate, falling terms of trade, weak exports. Persistence: structural weaknesses such as low productivity.",
     [[("k", "The current account measures trade in goods and services together with primary and secondary income. A deficit means that payments made by the country exceed payments received, so spending on imports and other outflows is greater than income from exports.")], [("n", "A country may have a persistent deficit if its exchange rate is too high, making exports dear and imports cheap, or if its terms of trade have deteriorated, so that export earnings buy fewer imports. A reliance on a few primary exports that earn little, or low productivity and poor quality that reduce competitiveness, could make the problem structural. Trade barriers imposed by trading partners, and profits sent abroad by foreign-owned firms, could add to it.")]]),
  eq(P("w23_23", "5(b)"), "12 marks", "A country has a persistent deficit on the current account of its balance of payments. Assess the likely consequences for the domestic and external economy of this country.",
     ["Analysis (up to 8): what a persistent deficit means; the domestic consequences, such as employment, growth, inflation, living standards, the government budget, business confidence and a need to restructure the economy; and the external consequences, such as the exchange rate, ability to trade, need for imports and debt interest. Maximum Level 2 if only the domestic or only the external economy is considered.",
      "Evaluation (up to 4): clearly considers the likely consequences for both parts of the economy and reaches a conclusion on the most likely consequences. A one-sided response cannot gain evaluation marks."],
     "Define persistent deficit. Domestic: lower AD, output and jobs; contractionary policy. External: depreciation, debt, reserves. Judge by size and financing.",
     [[("n", "A persistent deficit means imports and outflows of income exceed exports and inflows year after year. Domestically, net exports are negative, so AD and output could be lower, with weaker employment and growth, and the government may feel pressure to adopt contractionary policy. On the other hand, imports may raise living standards in the short run. Externally, a floating currency could depreciate, raising import prices and inflation, while under a fixed rate the reserves may fall. The country may need to borrow or sell assets, so more income could flow abroad as interest and profits.")], [("e", "The consequences are likely to be more serious the larger and longer the deficit, and the weaker the way it is financed. A deficit financed by long-term investment into productive capacity may be less damaging than one financed by short-term borrowing. Overall the likely consequences are slower growth and external pressure, but they could be limited if the deficit is small.")]]),
  eq(P("w24_21", "5(b)"), "12 marks", "Assess whether an economy will always benefit from having a surplus on the current account of its balance of payments.",
     ["Analysis (up to 8): the potential benefits, such as surplus foreign exchange to invest abroad, more jobs in the export sector, more domestic purchasing and employment, and possible growth (up to 4); the potential disadvantages, such as weak domestic demand and lower employment, lower growth, a surplus caused by recession, and lower output and employment in deficit countries (up to 4).",
      "Evaluation (up to 4): considers both the benefits and disadvantages, the size of the surplus and its possible causes, and concludes whether an economy will always benefit. A one-sided response cannot gain evaluation marks."],
     "Benefits: exchange earnings, export jobs, growth. Disadvantages: may reflect weak demand or recession; harm to partners. Judge by size and cause.",
     [[("n", "A surplus could give a country foreign exchange to invest abroad, and high exports may create jobs in the export sector and support growth. If imports are low because people buy domestic goods, employment at home could rise too. But a surplus could also be a sign of weak domestic demand, with low consumer spending reducing employment and growth, or even of a recession that cuts imports. It could also lower output and jobs in countries with deficits.")], [("e", "An economy will not always benefit. A surplus caused by strong competitiveness is likely to be good, while one caused by weak demand may not be. The size of the surplus and the reason for it are likely to matter most.")]])
  ],
  )

tips = tips_html(
  [("Say which part.", "Goods, services, primary or secondary income."),
   ("Cause then effect.", "State the cause, then what it does to X and M."),
   ("Explain persistence.", "Structural: competitiveness, productivity, terms of trade."),
   ("Split the consequences.", "Domestic and external."),
   ("Both sides for a surplus.", "Not always good: weak demand, partners hurt."),
   ("Use size and cause.", "A small deficit funded by investment is less serious."),
   ("Hedge.", "Use may, could, likely.")],
  [("Current account", "The current account records trade in goods and services and primary and secondary income."),
   ("Deficit", "A deficit is where payments exceed receipts."),
   ("Persistent deficit", "A persistent deficit lasts for many years."),
   ("Competitiveness", "Competitiveness is the ability to sell goods at attractive prices and quality."),
   ("Primary income", "Primary income is investment income and wages from abroad.")],
  [CW["explain"], CW["assess"], CW["consider"], CW["discuss"]]) + FC

js = CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const items = [["Imports rise", "Strong demand, high exchange rate, high costs", "f3"], ["Exports fall", "Poor competitiveness, weak demand abroad", "f3"], ["Income outflows", "Profits and interest paid abroad", "f3"], ["Current account deficit", "Payments exceed receipts", "f2"]];
  let o = ""; items.forEach(([n, d, c], i) => { const y = 12 + i * 58; o += SV.rect(30, y, 700, 46, c, { rx: 8, ...op(0.45) }) + SV.text(50, y + 20, n, "lbl bd") + SV.text(50, y + 38, d, "sm"); });
  return `<svg viewBox="0 0 760 252" role="img" aria-label="Causes of a current account deficit: higher imports, lower exports and income outflows">${o}</svg>`;
})();
chainStep("#stA", "How a deficit can build up", ["Incomes and consumer spending rise strongly", "Households buy more imports (high income elasticity)", "Domestic firms are less competitive, so exports lag", "Imports exceed exports", "A current account deficit appears and persists"], [
  "<b>Strong growth</b> and cheap credit raise spending.", "<b>More spending on imports</b> as people buy foreign goods and services.", "<b>High costs or a high exchange rate</b> make exports dearer abroad.", "<b>The trade balance</b> moves into deficit.", "<b>If the structure does not change</b>, the deficit may last."]);
chainStep("#stB", "What a persistent deficit may lead to", ["Net exports are negative, so AD is lower", "Output and employment could be weaker", "The currency may come under downward pressure", "The country may borrow or run down reserves", "Policy makers may adopt contractionary or supply-side policies"], [
  "<b>Net exports</b> subtract from AD.", "<b>Lower AD</b> could reduce output and jobs.", "<b>Demand for the currency</b> falls relative to supply.", "<b>Financing the gap</b> may mean more debt or lost reserves.", "<b>Policies to correct the deficit</b> may be needed, with their own costs."]);

chooser("g", [
  ["Strong consumer spending", "Imports rise because of high incomes", "Goods and services", "Persistent if growth is led by consumption, not investment", 3],
  ["Poor competitiveness", "Exports fall and imports rise", "Goods and services", "Low productivity and quality are slow to fix", 5],
  ["High exchange rate", "Exports dearer, imports cheaper", "Goods and services", "May reverse as the currency adjusts, unless fixed", 3],
  ["Falling terms of trade", "Export revenue buys fewer imports", "Goods mainly", "Persistent if commodity prices stay low", 4],
  ["Weak world demand", "Exports fall", "Goods and services", "Usually temporary, as it follows the world cycle", 2],
  ["Profits sent abroad", "Primary income outflow rises", "Primary income", "Persistent when much of industry is foreign-owned", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}, mainly affecting ${it[2].toLowerCase()}. ${it[3]}.`);

chooser("h", [
  ["Lower AD and output (deficit)", "Domestic households and firms", "Down: negative net exports", "Size of the deficit and spare capacity", 4],
  ["Currency depreciation (deficit)", "Importers, exporters, consumers", "Down: higher import prices, cheaper exports", "Fixed exchange rate; central bank action", 3],
  ["Debt and asset sales (deficit)", "Future generations, the external sector", "Up: more income flows abroad later", "Whether borrowing funds investment", 4],
  ["Higher AD and jobs (surplus)", "Exporters and their workers", "Up: net exports are positive", "Whether the surplus comes from weak demand", 3],
  ["Currency appreciation (surplus)", "Exporters; importers gain", "Up: export prices rise abroad", "Central bank intervention", 3],
  ["Harm to trading partners (surplus)", "Deficit countries", "Their deficits and unemployment rise", "Size of the surplus; retaliation risk", 3]
], (it) => `${it[0]}: this affects ${it[1].toLowerCase()}, with the direction: ${it[2].toLowerCase()}. It may be limited by ${it[3].toLowerCase()}.`);
''' + CLASSIFY("cl1", "Is it a possible cause of a deficit or of a surplus?", ["Deficit", "Surplus"],
  [("Rapid growth in consumer spending", 0), ("Low productivity and high costs", 0), ("Strong price competitiveness", 1), ("A high exchange rate", 0), ("High household saving and weak spending", 1), ("A fall in commodity export prices", 0), ("Low value of the currency", 1), ("Large profits sent to foreign owners", 0)],
  "Deficit causes raise imports or lower exports; surplus causes do the opposite.") + MATCH([
  ["Current account deficit", "Payments to the rest of the world exceed receipts"],
  ["Persistent deficit", "A deficit that lasts for many years"],
  ["Primary income", "Investment income and employee pay from abroad"],
  ["Secondary income", "Transfers such as aid and remittances"],
  ["Competitiveness", "Ability to sell goods at attractive price and quality"],
  ["Reserves", "Foreign currency held by the central bank"]]) + ORDER(
  "Put the effects of a persistent deficit in order.",
  ["Imports exceed exports", "Net exports lower AD", "The currency comes under downward pressure", "The country borrows or uses reserves", "Policy makers consider corrective policies"],
  "Deficit lowers AD, pressures the currency and needs financing.") + CALC([
  {"q": "Goods balance -40, services balance +25, primary income +10, secondary income -5 (all $bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "-40 + 25 + 10 - 5.", "sol": "<b>-$10bn</b>, a deficit."},
  {"q": "GDP is $500bn and the current account deficit is $20bn. What is the deficit as a % of GDP?", "a": 4, "unit": "%", "tol": 0.05, "hint": "20 ÷ 500.", "sol": "<b>4%</b>."},
  {"q": "The accounts sum to zero. Current account -30, capital account +5, financial account +20. What is the balancing item?", "a": 5, "unit": "", "tol": 0.5, "hint": "-30 + 5 + 20 + b = 0.", "sol": "<b>+5</b>."},
  {"q": "Exports are $250bn and imports $200bn of goods and services. What is the surplus ($bn)?", "a": 50, "unit": "$bn", "tol": 0.5, "hint": "250 - 200.", "sol": "<b>$50bn</b>."}]) + MCQ([
  ("A current account deficit means:", ["Payments exceed receipts", "Receipts exceed payments", "Exports exceed imports", "No trade"], 0, "Outflows are larger."),
  ("A likely cause of a deficit is:", ["A high exchange rate", "A low exchange rate", "High saving", "Weak imports"], 0, "Exports dear, imports cheap."),
  ("A fixed exchange rate with a deficit may cause:", ["Falling reserves", "Rising reserves", "No effect", "Lower imports"], 0, "The central bank buys the currency."),
  ("A surplus could be a sign of:", ["Weak domestic demand", "Strong imports", "Falling exports", "A depreciation only"], 0, "Low spending reduces imports."),
  ("A persistent deficit could lead to:", ["More debt or asset sales", "Higher reserves", "Lower AD only if exports rise", "No consequences"], 0, "The gap has to be financed.")
], "qz1") + CARDS([
  ("Deficit", "Payments exceed receipts."),
  ("Surplus", "Receipts exceed payments."),
  ("Cause: competitiveness", "Costs, quality, productivity."),
  ("Cause: exchange rate", "High rate hurts exports."),
  ("Cause: terms of trade", "Export revenue buys less."),
  ("Consequence", "Lower AD, depreciation, debt."),
  ("Surplus risk", "Weak demand; partners hurt."),
  ("Judge", "Size, cause, persistence.")]) + MCQ(mc_exam)

build("as65", "as-current-account-imbalances", "Causes and Consequences of Current Account Imbalances", EY,
  "6.3.3 to 6.3.4: why deficits and surpluses arise and what they may mean for the domestic and external economy. Animated chains, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
