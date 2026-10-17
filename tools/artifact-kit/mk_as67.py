"""AS syllabus 6.4.5 Effects of exchange rate changes. Run: python3 tools/artifact-kit/mk_as67.py"""
from as6k import *
EY = EYAS("6.4.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">depreciation</b> makes exports <b>cheaper in foreign currency</b> and imports <b>dearer in domestic currency</b>. If the combined price elasticities of demand for exports and imports exceed one (the <b class="kw">Marshall-Lerner condition</b>), <b>net exports rise</b>, so <b>AD shifts right</b>, raising real output, employment and, close to full capacity, the price level (<b>demand-pull</b>); but dearer imported raw materials and components raise costs, so <b>SRAS may shift left</b> (<b>cost-push</b>). The effect on the current account may be <b>delayed</b>, because demand adjusts slowly (the <b class="kw">J-curve</b>), and the <b>terms of trade</b> usually worsen. An <b>appreciation</b> has the opposite effects: <b>lower import prices</b> and downward pressure on inflation, but <b>less competitive exports</b>, lower net exports, and possible falls in output and employment. The net result depends on <b>elasticities, spare capacity, reliance on imported inputs</b> and <b>time</b>.</p></div>

  <h2>1 · Depreciation through AD and AS</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Depreciation</th><th>Appreciation</th></tr>
    <tr><td><b>Exports</b></td><td>Cheaper abroad, volume may rise</td><td>Dearer abroad, volume may fall</td></tr>
    <tr><td><b>Imports</b></td><td>Dearer, volume may fall</td><td>Cheaper, volume may rise</td></tr>
    <tr><td><b>Net exports and AD</b></td><td>May rise (if PEDx + PEDm &gt; 1)</td><td>May fall</td></tr>
    <tr><td><b>Import costs and SRAS</b></td><td>Costs rise, SRAS may shift left</td><td>Costs fall, SRAS may shift right</td></tr>
    <tr><td><b>Output and jobs</b></td><td>May rise, if spare capacity exists</td><td>May fall</td></tr>
    <tr><td><b>Inflation</b></td><td>May rise (demand-pull and cost-push)</td><td>May fall</td></tr>
    <tr><td><b>Terms of trade</b></td><td>Deteriorate</td><td>Improve</td></tr>
  </table></div>

  <h2>2 · Why the effects may be limited</h2>
  <ul>
    <li><b>Elasticity:</b> if demand for exports and imports is inelastic (sum below one), a depreciation may <b>worsen</b> the trade balance, as import spending rises more than export revenue.</li>
    <li><b>J-curve:</b> in the short run, contracts and habits mean the balance may get worse before it improves.</li>
    <li><b>Spare capacity:</b> if the economy is near full capacity, the extra demand mainly raises prices rather than output.</li>
    <li><b>Imported inputs:</b> a high share of imported raw materials makes cost-push inflation more likely.</li>
    <li><b>Retaliation:</b> other countries may respond by depreciating too.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Trace the <b>chain</b>: exchange rate, then relative prices, then X and M, then AD (and SRAS), then output, jobs and prices. Then <b>evaluate</b>: elasticities, spare capacity, imported inputs, time lags.</div>
'''

watch = '''
  <h2>1 · A depreciation and AD</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · The chain of effects of an appreciation</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Depreciate the currency</h2>
  <p>The economy starts at output 50 and price level 50. A depreciation raises AD only if the sum of the price elasticities is above one, and raises costs if the economy relies on imported inputs.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Net export effect on AD</small><strong id="r1"></strong></div><div><small>New output</small><strong id="r2"></strong></div><div><small>New price level</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS after a depreciation"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Choose an effect", "Choose a possible effect of a depreciation or appreciation to see its direction, the main condition and how large it may be.", ["Direction", "Main condition", "Time frame"])

practise = practise_html("Depreciation or appreciation effect?", "Match the term to its description", "Put the effects of a depreciation in order")

real = RWNOTE + (
rw("A weaker currency helps exporters", "When a currency falls, exporters can cut their prices abroad, or keep the same price and earn more at home. Orders may rise, but only if buyers respond to the lower prices.", "a depreciation and export competitiveness.") +
rw("Dearer imported fuel", "A country that imports most of its fuel finds petrol and heating costs rise after a depreciation. Firms and households face higher costs, adding to inflation.", "imported inputs and cost-push inflation.") +
rw("The J-curve", "After a currency falls, existing import and export contracts continue for months. The trade deficit may widen at first and only narrow later as volumes adjust.", "the J-curve.") +
rw("A strong currency squeezes manufacturers", "When a currency rises, manufacturers selling abroad face dearer exports and may lose orders, while consumers enjoy cheaper imports and lower inflation.", "an appreciation and its effects.")
)

mc_exam = [
  mcq("m24_12", 21, "An economy has an unemployment rate of 8%, an increase of 2% from the previous year. At the same time, the current account deficit rose from 3% of GDP to 4% of GDP. What would be most likely to reduce both unemployment and the current account deficit?", ["decrease government spending", "depreciation of the currency", "increase indirect taxation", "increase interest rates"], 1, "A depreciation could raise exports and reduce imports, boosting AD, output and employment while narrowing the deficit."),
  mcq("m24_12", 25, "A government decides to allow the country's currency to depreciate to remove the deficit on its current account of the balance of payments. What is the most likely reason why this would not work?", ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], 3, "High trade barriers could limit the rise in exports."),
  mcq("s21_12", 27, "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation)", ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], 3, "A worse current account tends to lower the exchange rate, which raises import costs and cost-push inflation."),
  mcq("s21_13", 25, "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency?", ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], 1, "If the sum of the elasticities is below one, the Marshall-Lerner condition fails."),
  mcq("s22_12", 24, "The table gives combinations of the price elasticity of demand for exports and for imports. Following a devaluation, under which combination would the current account worsen? (exports, imports)", ["0.3 and 0.3", "0.2 and 0.9", "0.6 and 0.5", "1.2 and 1.2"], 0, "The sum is 0.6, which is below one, so the trade balance worsens."),
  mcq("s21_11", 22, "Why might a government wish to increase the value of its foreign exchange rate when the sum of the price elasticity of demand for imports and exports is greater than 1?", ["to attract more tourists into the country", "to improve the current account of the balance of payments in the long run", "to increase inflation if the country is in recession", "to make imported raw materials cheaper"], 3, "A higher exchange rate lowers import prices, including raw materials."),
  mcq("s21_12", 20, "A government devalues its fixed exchange rate. What is most likely to be its aim?", ["to improve the terms of trade", "to increase the level of aggregate demand", "to reduce a current account surplus", "to reduce demand-pull inflation"], 1, "A devaluation aims to raise net exports and so AD.")
]

exam = exam_page("exchange rate changes and the wider economy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The effects of an exchange rate change on trade, AD, inflation and employment are common 8 and 12 mark Paper 2 parts. Reworded past questions are below, with seven Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "Feb/March 2024 (22) Q4(a); May/June 2023 (21) Q5(a); May/June 2023 (22) Q5(a)"), ("Essay parts, 12 marks", "2", "May/June 2020 (21) Q4(b); May/June 2025 (24) Q5(b)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2025")],
  [
  eq(P("m24_22", "4(a)"), "8 marks", "Explain what is meant by a depreciation of the exchange rate and consider whether a depreciation is likely to increase domestic real output.",
     ["Knowledge (up to 3): an accurate definition of the exchange rate (1); a depreciation is likely if the demand for a currency falls (1) or its supply increases (1).",
      "Analysis (up to 3): a depreciation reduces the perceived price of exports and increases the perceived price of imports (1), which raises net exports (X - M) and aggregate demand (1) and so the level of domestic real output (1).",
      "Evaluation (up to 2): this assumes the economy is not at full capacity (1) or depends on the elasticity of demand for traded goods (1); the second mark is for a justified conclusion."],
     "Define the exchange rate and depreciation. Cheaper exports, dearer imports: X-M up, AD up, output up. Evaluate: spare capacity, elasticities.",
     [[("k", "The exchange rate is the price of one currency in terms of another. A depreciation is a fall in the value of a floating currency, which may be caused by a fall in demand for it or an increase in its supply.")], [("n", "A depreciation makes exports cheaper abroad and imports dearer at home. If demand for them is elastic enough, exports rise and imports fall, so net exports increase. This raises aggregate demand, which could increase real output and employment.")], [("e", "The rise in output depends on spare capacity: if the economy is already near full capacity, the extra AD may raise prices rather than output. It also depends on elasticities, since if the sum of the price elasticities is below one, net exports may fall. Overall, a depreciation could raise output, but not always.")]]),
  eq(P("s23_22", "5(a)"), "8 marks", "Explain the difference between cost-push and demand-pull inflation and consider which is more likely to occur if there is a depreciation in the exchange rate of a country with few natural resources.",
     ["Knowledge (up to 3): cost-push inflation is caused by rises in the costs of production (1); demand-pull inflation is caused by increases in AD not matched by increases in AS (1); a clear explanation of the differences (1).",
      "Analysis (up to 3): a depreciation lowers the price of exports for trading partners and raises the price of imports. Demand-pull: the effect on X - M and AD, with reference to the PED of exports and imports (maximum 2 if only this is considered). Cost-push: the importance of imports, and that a country with few natural resources probably must import its inputs (maximum 2 if only this is considered).",
      "Evaluation (up to 2): considers that the country has few natural resources (1) and reaches a justified conclusion on which type of inflation is more likely (1)."],
     "Define both types. Depreciation: AD up (demand-pull) and import costs up (cost-push). Few resources: imported inputs, so cost-push is likely.",
     [[("k", "Cost-push inflation is caused by a rise in the costs of production, which shifts SRAS to the left. Demand-pull inflation is caused by a rise in aggregate demand that is not matched by a rise in aggregate supply.")], [("n", "A depreciation raises the price of imports and lowers the price of exports for foreigners. Cheaper exports and dearer imports may raise net exports, increasing AD and creating demand-pull pressure, depending on the elasticities of demand. At the same time a country with few natural resources probably has to import raw materials and fuel, so its costs of production rise, which shifts SRAS left and creates cost-push inflation.")], [("e", "Cost-push inflation is probably the more likely outcome, because the country relies on imported inputs, so the rise in costs is likely to be large and immediate. Demand-pull pressure may be smaller if demand for exports is inelastic or if there is spare capacity.")]]),
  eq(P("s23_21", "5(a)"), "8 marks", "With the help of a diagram(s), explain the likely causes of a depreciation of a floating exchange rate and consider whether such a depreciation is always beneficial to an economy.",
     ["Knowledge (up to 3): a correctly labelled diagram of the demand for and supply of a currency (1), with appropriate shifts (1) and a fall in the exchange rate (1).",
      "Analysis (up to 3): uses the diagram to explain what could shift demand for the currency left and/or supply right, and analyses the potential advantages and disadvantages of a depreciation.",
      "Evaluation (up to 2): a valid judgement on whether the benefits of a depreciation always outweigh the disadvantages (1) and a conclusion (1)."],
     "Diagram: D left or S right. Causes: lower exports, lower interest rates, more imports. Benefits: exports, AD. Costs: import prices, inflation. Judge: not always.",
     [[("k", "The diagram shows the exchange rate against the quantity of the currency, with demand and supply curves. The demand curve shifts left or the supply curve shifts right, so the equilibrium exchange rate falls.")], [("n", "Demand for the currency may fall if foreign demand for exports falls or interest rates are cut, and supply may rise if imports increase. A depreciation makes exports cheaper, which could raise AD, output and employment, and may help reduce a current account deficit. But imports become dearer, which may raise costs and prices and reduce living standards.")], [("e", "A depreciation is not always beneficial. It is more likely to help if demand for exports and imports is elastic and there is spare capacity, and less beneficial if the economy relies on imported inputs.")]]),
  eq(P("s20_21", "4(b)"), "12 marks", "Discuss whether an appreciation of a country's foreign exchange rate is likely to cause both a rise in inflation and a decrease in employment in its economy.",
     ["Analysis (up to 8): the effect of an appreciation on the level of inflation (up to 4); the effect of an appreciation on the level of employment (up to 4).",
      "Evaluation (up to 4): a judgement on whether an appreciation is likely to cause both a rise in inflation and a fall in employment, with a conclusion (1 mark reserved)."],
     "Appreciation: imports cheaper, so inflation may fall, not rise. Exports dearer, so net exports and employment may fall. Judge: not both.",
     [[("n", "An appreciation makes imports cheaper in domestic currency, which lowers the cost of imported raw materials and goods, so cost-push inflation could fall rather than rise. It also reduces the price of imported goods in the price index. Exports become dearer abroad, so demand for them may fall, and imports become cheaper so more are bought. Net exports fall, AD may fall, and output and employment in export industries could decrease.")], [("e", "An appreciation is likely to decrease employment, especially in export-led industries, but it is unlikely to cause a rise in inflation, because import prices fall and AD is lower. So the two effects are unlikely to occur together. The effect on employment depends on elasticities and spare capacity.")]]),
  eq(P("s25_24", "5(b)"), "12 marks", "Assess whether the depreciation of an exchange rate is always beneficial to an economy.",
     ["Analysis (up to 8): what a depreciation means; the potential advantages, such as an increase in exports as prices fall, which can help reduce a current account deficit and raise AD; and the potential disadvantages, such as dearer imports of finished goods and raw materials, higher costs of production and cost-push inflation.",
      "Evaluation (up to 4): balance, considering alternatives and the conditions in which a depreciation may or may not be beneficial, with a conclusion."],
     "Define. Benefits: cheaper exports, deficit narrows, AD up. Costs: dearer imports, cost-push inflation. Judge: depends on elasticities, spare capacity, imported inputs.",
     [[("n", "A depreciation is a fall in the value of a floating currency. It makes exports cheaper abroad, which could increase export sales, narrow a current account deficit and raise AD, output and employment. But it also makes imports dearer, including raw materials, so costs of production could rise and cause cost-push inflation, and households may see their living standards fall because imported goods are dearer.")], [("e", "A depreciation is not always beneficial. It is more likely to help when demand for exports and imports is elastic, there is spare capacity, and the economy does not depend heavily on imported inputs. If those conditions do not hold, the costs may outweigh the benefits.")]])
  ],
  )

tips = tips_html(
  [("Follow the chain.", "Rate, relative prices, X and M, AD, output."),
   ("Mention elasticity.", "Sum above one (Marshall-Lerner) for a better trade balance."),
   ("Mention time.", "J-curve: it may worsen before it improves."),
   ("Both AD and AS.", "AD right, but SRAS may shift left."),
   ("Use the context.", "Few natural resources: imported inputs."),
   ("Spare capacity.", "Near full capacity, prices rise more than output."),
   ("Judge.", "Not always beneficial; depends on conditions.")],
  [("Marshall-Lerner condition", "The Marshall-Lerner condition is that the sum of the price elasticities of demand for exports and imports exceeds one."),
   ("J-curve", "The J-curve shows the trade balance worsening before it improves after a depreciation."),
   ("Cost-push inflation", "Cost-push inflation is caused by rising costs of production."),
   ("Terms of trade", "The terms of trade are export prices relative to import prices."),
   ("Net exports", "Net exports are exports minus imports.")],
  [CW["explain"], CW["assess"], CW["discuss"], CW["consider"]]) + FC

js = SDJS + ADASJS + CHAINJS + '''
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A depreciation shifts AD to the right and may shift SRAS to the left">${adasPlot({ a: 20, s: -20, g: 1, n: 1, lras: false })}</svg>`;
function dpDraw(s) { return adasPlot({ a: s.a, s: s.s, g: 1, n: s.n, lras: false }); }
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A depreciation shifts AD right and may shift SRAS left", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD and SRAS meet at output 50 and price level 50.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>The currency depreciates.</b> Exports are cheaper, imports dearer, net exports rise and <b>AD shifts right</b>. Output rises to 60 and the price level to 58 (demand-pull).", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>Imported inputs cost more.</b> If the economy depends on imports, <b>SRAS shifts left</b> as well, adding cost-push pressure.", s: { a: 20, s: -20, n: 1 } },
  { cap: "<b>Net effect:</b> the price level rises to 66 and output stays at 50: the cost-push effect has offset the output gain.", s: { a: 20, s: -20, n: 1 } },
] });
chainStep("#stB", "The chain of effects of an appreciation", ["The exchange rate rises", "Imports are cheaper; exports are dearer abroad", "Net exports fall and AD shifts left", "Output and employment may fall", "Import costs fall, so inflation may be lower"], [
  "<b>An appreciation</b> raises the value of the currency.", "<b>Relative prices change:</b> import prices fall and export prices rise in foreign currency.", "<b>Net exports fall</b> if demand is elastic enough, shifting AD left.", "<b>Lower AD</b> could reduce output and jobs, especially in export industries.", "<b>Cheaper imports</b> lower costs, so SRAS may shift right and inflation falls."]);

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const sum = +$("#g1v").value / 10, imp = +$("#g2v").value, a = Math.max(-15, 30 * (sum - 1)), s = -imp, e = sdEq(a, s);
  $("#r1").textContent = (a >= 0 ? "+" : "") + Lib.fmtN(a, 1); $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = (sum > 1 ? `The sum of the elasticities is ${Lib.fmtN(sum, 1)}, above one, so net exports rise and AD shifts right. ` : sum < 1 ? `The sum of the elasticities is ${Lib.fmtN(sum, 1)}, below one, so the trade balance may worsen and AD shifts left. ` : "The sum of the elasticities is one, so net exports are unchanged. ") + (imp > 0 ? `Dearer imported inputs shift SRAS left by ${imp}. ` : "No reliance on imported inputs, so SRAS is unchanged. ") + `Output is ${Lib.fmtN(e.q, 1)} and the price level ${Lib.fmtN(e.p, 1)}.`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1, lras: false });
}
Lib.slider($("#g1"), { id: "g1v", label: "Sum of price elasticities (PEDx + PEDm) × 10 ", min: 4, max: 20, step: 2, value: 14, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Reliance on imported inputs (SRAS shift left) ", min: 0, max: 20, step: 5, value: 5, fmt: (v) => v, onInput: labA });
labA();

chooser("h", [
  ["Exports rise (depreciation)", "Up", "Demand for exports is elastic", "Short run slow; long run larger", 4],
  ["Imports fall (depreciation)", "Down in volume, up in price", "Few close domestic substitutes weakens this", "Short run slow; long run larger", 3],
  ["Cost-push inflation (depreciation)", "Up", "Reliance on imported inputs", "Short run, fast", 4],
  ["AD rises (depreciation)", "Up", "PEDx + PEDm above one and spare capacity", "Medium run", 4],
  ["Trade balance worsens first (J-curve)", "Down, then up", "Contracts and habits delay adjustment", "Months to a few years", 3],
  ["Lower inflation (appreciation)", "Down", "Imports are a large share of spending", "Short run", 3],
  ["Exporters lose orders (appreciation)", "Down", "Demand for exports is elastic", "Short to medium run", 4]
], (it) => `${it[0]}: the direction is ${it[1].toLowerCase()}. It mainly depends on this condition: ${it[2].toLowerCase()}. Time frame: ${it[3].toLowerCase()}.`, "Likely size of the effect");
''' + CLASSIFY("cl1", "Is the effect more likely after a depreciation or after an appreciation?", ["Depreciation", "Appreciation"],
  [("Exports become cheaper abroad", 0), ("Imported raw materials become cheaper", 1), ("Cost-push inflation pressure rises", 0), ("Net exports and AD may fall", 1), ("The terms of trade deteriorate", 0), ("Manufacturers selling abroad lose orders", 1), ("A current account deficit may narrow", 0), ("Downward pressure on the price level", 1)],
  "A depreciation helps exports and raises import prices; an appreciation does the reverse.") + MATCH([
  ["Marshall-Lerner condition", "The sum of the price elasticities of exports and imports exceeds one"],
  ["J-curve", "The trade balance worsens before it improves after a depreciation"],
  ["Net exports", "Exports minus imports"],
  ["Cost-push inflation", "Inflation caused by rising costs of production"],
  ["Terms of trade", "The ratio of export prices to import prices"],
  ["Expenditure switching", "Moving spending from imports to domestic goods"]]) + ORDER(
  "Put the effects of a depreciation on output in order.",
  ["The exchange rate falls", "Exports become cheaper and imports dearer", "Net exports rise", "AD shifts right", "Real output and employment may rise"],
  "Relative prices change, net exports rise, AD and output rise.") + CALC([
  {"q": "PED of exports is 0.8 and PED of imports is 0.5. What is the sum?", "a": 1.3, "unit": "", "tol": 0.01, "hint": "0.8 + 0.5.", "sol": "<b>1.3</b>, above one, so the Marshall-Lerner condition is met."},
  {"q": "The terms of trade index was 100 and the price of exports falls 8% with import prices unchanged. What is the new index?", "a": 92, "unit": "", "tol": 0.1, "hint": "100 × 0.92.", "sol": "<b>92</b>."},
  {"q": "Exports are $120bn, imports $150bn. After a depreciation, exports rise by 10% and imports fall by 5% in value. What is the new trade balance ($bn)?", "a": -10.5, "unit": "$bn", "tol": 0.1, "hint": "132 − 142.5.", "sol": "Exports $132bn, imports $142.5bn, so <b>-$10.5bn</b>."},
  {"q": "A firm imports inputs costing $1000 and the currency depreciates by 10% against the supplier's currency (so inputs cost 10% more). What is the new cost ($)?", "a": 1100, "unit": "$", "tol": 0.5, "hint": "1000 × 1.10.", "sol": "<b>$1100</b>."}]) + MCQ([
  ("A depreciation makes imports:", ["Dearer in domestic currency", "Cheaper", "Unchanged", "Free"], 0, "Each unit of foreign currency costs more."),
  ("The Marshall-Lerner condition is that:", ["PEDx + PEDm is above 1", "PEDx is above 1 only", "PEDm is below 1", "Elasticities are zero"], 0, "Then net exports improve."),
  ("An appreciation is likely to:", ["Lower import prices", "Raise import prices", "Lift exports", "Raise inflation"], 0, "Imports cost less in domestic currency."),
  ("Cost-push inflation after a depreciation is more likely if:", ["The economy relies on imported inputs", "It has many natural resources", "Imports are small", "There is spare capacity"], 0, "Imported inputs cost more."),
  ("A depreciation will usually cause the terms of trade to:", ["Deteriorate", "Improve", "Stay the same", "Double"], 0, "Export prices fall relative to import prices.")
], "qz1") + CARDS([
  ("Depreciation", "Cheaper exports, dearer imports."),
  ("Appreciation", "Dearer exports, cheaper imports."),
  ("Marshall-Lerner", "PEDx + PEDm above 1."),
  ("J-curve", "Worse first, then better."),
  ("AD effect", "Net exports up, AD right."),
  ("AS effect", "Import costs up, SRAS left."),
  ("Spare capacity", "Output rises; else prices rise."),
  ("Judge", "Elasticity, time, inputs.")]) + MCQ(mc_exam)

build("as67", "as-exchange-rate-changes-ad-as", "Effects of Exchange Rate Changes", EY,
  "6.4.5: how a depreciation or appreciation affects trade, AD, AS, inflation and employment. AD/AS animations, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
