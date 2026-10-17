"""AS syllabus 6.1.3 Exports, imports and the terms of trade. Run: python3 tools/artifact-kit/mk_as61.py"""
from asx import *
EY = EYAS("6.1.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">terms of trade</b> measure the relationship between the prices a country receives for its <b>exports</b> and the prices it pays for its <b>imports</b>: <b>terms of trade = (index of export prices ÷ index of import prices) × 100</b>. An <b>improvement</b> (a rise in the index) means export prices have risen relative to import prices, so each unit of exports buys more imports; a <b>deterioration</b> (a fall) means the opposite. The terms of trade can change because of the <b>exchange rate</b>, <b>relative inflation</b>, changes in <b>world demand and supply</b> for the goods traded (especially commodity prices), <b>productivity</b> and protectionism by trading partners. An improvement is not always beneficial: it can make exports <b>less competitive</b> and worsen the <b>balance of trade</b>, while a deterioration can help export volumes but means a country must sell more to buy the same imports.</p></div>

  <h2>1 · Measuring the terms of trade (6.1.3)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Formula:</b> terms of trade = (average export price index ÷ average import price index) × 100. The index has no units because it is a ratio of two indices.</li>
    <li><b>Base year = 100.</b> Above 100 means export prices have risen more than import prices (improved); below 100 the reverse (deteriorated).</li>
    <li><b>Not the same as the balance of trade.</b> The terms of trade compare <b>prices</b>; the balance of trade compares the <b>value</b> (price times quantity) of exports and imports of goods.</li>
    <li>The terms of trade must change when the <b>average price</b> of exports changes relative to the average price of imports. They need not change when only the <b>volume</b> of trade changes.</li>
  </ul>

  <h2>2 · Causes and effects of changes (6.1.3)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Effect on export prices relative to import prices</th><th>Terms of trade</th></tr>
    <tr><td><b>Depreciation of the exchange rate</b></td><td>Exports cheaper abroad; imports dearer at home</td><td>Deteriorate</td></tr>
    <tr><td><b>Appreciation</b></td><td>Exports dearer; imports cheaper</td><td>Improve</td></tr>
    <tr><td><b>Higher domestic inflation than trading partners</b></td><td>Export prices rise faster than import prices</td><td>Improve (as measured)</td></tr>
    <tr><td><b>Rising world demand for the country's exports</b></td><td>Export prices rise</td><td>Improve</td></tr>
    <tr><td><b>Rising world prices of imported goods (such as oil)</b></td><td>Import prices rise</td><td>Deteriorate</td></tr>
    <tr><td><b>Falling export prices (a glut of commodities, rival producers)</b></td><td>Export prices fall</td><td>Deteriorate</td></tr>
  </table></div>
  <ul>
    <li><b>Low-income countries</b> often export <b>primary products</b> whose prices are volatile and have low income elasticity of demand, and import manufactures, so their terms of trade can deteriorate over time.</li>
    <li><b>An improvement</b>: higher living standards (more imports per unit exported), lower import costs and inflation. <b>But</b> export prices rise, exports may fall in volume and the current account may worsen if demand is price elastic.</li>
    <li><b>A deterioration</b>: more exports needed to buy the same imports; but it may make exports more competitive. The effect on the trade balance depends on <b>price elasticities of demand</b> for exports and imports.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always write the <b>formula</b>. Say which way <b>each price</b> moves and whether the index <b>rises or falls</b>. Evaluate the benefit using <b>price elasticity</b> and the effect on the balance of trade.</div>
'''

watch = '''
  <h2>1 · Calculating and reading the index</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stF"></div>
  <h2>2 · What a unit of exports buys</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Terms of trade calculator</h2>
  <p>Set the export price index and import price index (base year = 100).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Terms of trade</small><strong id="r1"></strong></div><div><small>Change from 100</small><strong id="r2"></strong></div><div><small>Imports per unit of exports</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Export and import price indices and the terms of trade"></svg></div></div></div>

  <h2>Lab 2 · What caused the change?</h2>
  <p>Choose an event to see its effect on export and import prices and on the terms of trade.</p>
  <div class="card"><div class="grid2"><div><div id="cB" class="btnrow"></div>
    <div class="readout"><div><small>Export prices</small><strong id="t1"></strong></div><div><small>Import prices</small><strong id="t2"></strong></div><div><small>Terms of trade (from 100)</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars of export price, import price and terms of trade after the chosen event"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Improve or deteriorate?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a depreciation on the terms of trade in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A coffee exporter", "A country exports coffee and imports machinery. When coffee prices on world markets halve while machinery prices stay the same, the terms of trade deteriorate: the country must sell twice as much coffee to buy the same machine.", "a fall in export prices worsening the terms of trade.") +
rw("An oil importer", "When world oil prices rise sharply, an oil-importing country's import price index rises, so its terms of trade deteriorate even if its export prices are unchanged.", "rising import prices.") +
rw("A stronger currency", "If the currency appreciates, exports become dearer in foreign currency and imports cheaper in home currency. The terms of trade improve, but exporters may lose sales.", "an appreciation improving the terms of trade but hurting competitiveness.") +
rw("A primary product exporter", "Many low-income countries rely on exporting raw materials. Demand for these grows slowly as world incomes rise, while manufactured imports rise in price, so their terms of trade can deteriorate over time.", "why low-income countries may suffer.")
)

mc_exam = [
  mcq("m21_12", 20, "A country's terms of trade changed from 100 to 95. What is most likely to have caused this change?", ["a depreciation of the country's currency", "a reduction in import tariffs", "a rise in the price of exported goods", "an improvement in the balance of trade"], 0, "A depreciation lowers export prices relative to import prices, so the index falls."),
  mcq("m22_12", 21, "The terms of trade index for Mauritius fell from 111.2 in the first quarter of 2018 to 106.1 in the second quarter. Which combination could have produced this outcome? (export prices, import prices)", ["rose, fell", "rose, rose", "rose, unchanged", "unchanged, fell"], 1, "The index falls only if import prices rise by more than export prices. Both could rise, with imports rising faster."),
  mcq("m22_12", 25, "The prices of a country's exports rise by 5% while the prices of its imports fall by 5%. What will definitely improve in the country as a result of these changes?", ["balance of trade", "current account balance", "exchange rate", "terms of trade"], 3, "Export prices rising relative to import prices improves the terms of trade. The effect on the trade balance depends on elasticities."),
  mcq("m23_12", 24, "What can be best understood from a knowledge of a country's terms of trade?", ["its balance of payments performance", "the purchasing power of its exports", "the standard of living within the country", "the value of its real exchange rate"], 1, "The terms of trade show how many imports a unit of exports can buy."),
  mcq("m24_12", 26, "When must the terms of trade of a country change?", ["when the volume of exports falls and the volume of imports rises", "when the total value of exports falls and the total value of imports rises", "when the balance of trade in goods moves from deficit to surplus", "when the average price of exports rises and the average price of imports falls"], 3, "The terms of trade depend on prices, not volumes or values."),
  mcq("m25_12", 26, "Country X trades with country Y. What are the terms of trade for country X?", ["the average price of country X's exports divided by the average price of country Y's exports", "the ratio of an index of country X's export prices to an index of its import prices", "the value of country X's exports divided by the value of country Y's exports", "the value of country X's imports divided by the value of country Y's imports"], 1, "Terms of trade = export price index ÷ import price index."),
  mcq("s20_12", 25, "Why does the value of a country's terms of trade have no monetary units?", ["It cannot be calculated accurately enough", "It includes more than one currency", "It is a ratio of two index numbers", "It measures change over time"], 2, "A ratio of two indices has no units."),
  mcq("s20_13", 23, "The table shows the relative price of exports compared with imports as an index (2013 = 100): 2013 is 100, 2014 is 97 and 2015 is 95. Which statement about the period 2013 to 2015 is correct?", ["Export prices have increased each year", "The general level of prices has fallen", "The terms of trade have deteriorated", "The volume of imports increasingly exceeds the volume of exports"], 2, "A falling index of export prices relative to import prices is a deterioration."),
  mcq("s21_11", 20, "Why might an unfavourable movement in a country's terms of trade benefit its economy?", ["It would force inefficient firms out of business", "It would increase the quantity of goods available for domestic consumption", "It would make domestically-produced goods more expensive than imports", "It would make the country's exports relative to imports more competitive internationally"], 3, "Lower export prices relative to import prices improve competitiveness."),
  mcq("s22_11", 24, "What leads to a fall in a country's terms of trade?", ["a fall in the price of exports relative to the price of imports", "a fall in the price of imports relative to the price of exports", "a fall in the quantity of exports relative to the quantity of imports", "a fall in the quantity of imports relative to the quantity of exports"], 0, "The terms of trade are based on relative prices."),
  mcq("s22_12", 21, "What will lead to an improvement in the terms of trade?", ["Export prices fall by 10% and import prices fall by 5%", "Export prices fall by 10% and import prices rise by 5%", "Export prices rise by 5% and import prices rise by 10%", "Export prices rise by 10% and import prices rise by 5%"], 3, "The index rises only if export prices rise by more than (or fall by less than) import prices."),
  mcq("s22_13", 20, "What could explain an improvement in the terms of trade for a country?", ["an increase in tariffs on imports", "a decrease in the volume of imports sold", "an increase in the prices of exports", "a decrease in the volume of exports sold"], 2, "Higher export prices improve the terms of trade. Volumes and tariffs do not change the price ratio directly.")
]

exam = exam_page("the terms of trade",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The terms of trade is one of the most common Paper 2 topics: an 8 mark part on causes and benefits in most series, a 12 mark assessment and a 3 mark distinction from the balance of trade. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "5", "Feb/March 2025 (22) Q4(a); Oct/Nov 2022 (23) Q4(a); Oct/Nov 2023 (22) Q4(a); May/June 2025 (24) Q5(a); May/June 2024 (23) Q5(a)"), ("Essay parts, 12 marks", "1", "Oct/Nov 2023 (22) Q4(b)"), ("Data response, 3 marks", "1", "May/June 2020 (21) Q1(b)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("m25_22", "4(a)"), "8 marks", "With the help of a formula, explain two reasons for an improvement in the terms of trade and consider the extent to which an improvement in the terms of trade will benefit an economy.",
     ["Knowledge (up to 3): an accurate definition of the terms of trade or an accurate formula (1); an improvement is likely if export prices rise (1) relative to import prices (1).",
      "Analysis (up to 3): an improvement means a unit of exports buys relatively more imports (1), which may improve living standards (1) as imported goods appear cheaper (1), but it may lead to a current account deficit (1). Maximum 2 if only benefits are considered.",
      "Evaluation (up to 2): an assessment of the advantages and disadvantages, for example in terms of unemployment and price elasticity values, with a valid conclusion."],
     "Formula: export price index ÷ import price index × 100. Two reasons: export prices rise, import prices fall. Benefit: more imports per export. Risk: less competitive, current account deficit. Judge using elasticity.",
     [[("k", "The terms of trade are the ratio of an index of export prices to an index of import prices, multiplied by 100. An improvement occurs when export prices rise relative to import prices. This could be because world demand for the country's exports rises, pushing up their price, or because the price of imported raw materials falls.")], [("n", "An improvement means each unit of exports buys more imports, which may raise living standards because imported goods become relatively cheaper. But higher export prices can reduce export sales if foreign demand is price elastic, which could lead to a current account deficit.")], [("e", "Whether an improvement is beneficial depends on the price elasticity of demand for exports and on the effect on employment in export industries. If demand is inelastic, revenue from exports rises, so it is likely to be of overall benefit; if elastic, the loss of competitiveness may outweigh the gain.")]]),
  eq(P("w22_23", "4(a)"), "8 marks", "Explain how a higher rate of inflation in an economy compared to its trading partners and a decline in the exchange rate will each affect the terms of trade in an economy.",
     ["Knowledge (up to 2): the terms of trade measure the ratio of export to import prices (1) with an accurate formula, index of export prices ÷ index of import prices (1).",
      "Application (up to 3): a higher rate of inflation than trading partners raises the relative price of exports (1) and reduces the relative price of imports (1), so the terms of trade improve (1).",
      "Application (up to 3): a decline in the exchange rate reduces the relative price of exports (1) and raises the relative price of imports (1), so the terms of trade deteriorate (1)."],
     "Formula. Higher relative inflation: export prices rise faster, ToT improve. Lower exchange rate: exports cheaper, imports dearer, ToT deteriorate.",
     [[("k", "The terms of trade are the index of export prices divided by the index of import prices, times 100.")], [("n", "If a country's inflation is higher than its trading partners', its export prices rise faster than the prices of its imports, so the index rises and the terms of trade improve. If the exchange rate declines, exports become cheaper in foreign currency and imports dearer in domestic currency, so export prices fall relative to import prices and the terms of trade deteriorate.")]]),
  eq(P("w23_22", "4(a)"), "8 marks", "Explain the difference between the terms of trade and the balance of trade in goods and consider whether an economy should be more concerned about its terms of trade than its balance of trade in goods.",
     ["Knowledge (up to 3): the terms of trade is a numerical measure of the ratio between export and import prices (1) with an accurate formula showing it as an index (1); the balance of trade in goods is the revenue from exports of goods minus expenditure on imports of goods (1).",
      "Analysis (up to 3): both measures analysed: effects of changes in the terms of trade (relative competitiveness, cost-push inflation, effects on the trade balance) up to 2; effects of changes in the balance of trade (employment, growth, inflation) up to 2. Maximum 3.",
      "Evaluation (up to 2): a judgement on which the economy should be more concerned about, with a conclusion."],
     "ToT: ratio of prices. BoT: value of exports minus imports. Compare effects. Judge: BoT matters more for jobs and growth; ToT matters for living standards.",
     [[("k", "The terms of trade is the ratio of export prices to import prices: (export price index ÷ import price index) × 100. The balance of trade in goods is the value of exports of goods minus the value of imports of goods.")], [("n", "A deterioration in the terms of trade means more exports are needed to buy the same imports, and rising import prices can add to cost-push inflation. A deficit on the balance of trade in goods means more is spent on imports than earned from exports, which may reduce AD and employment and may put pressure on the exchange rate.")], [("e", "An economy is probably more concerned about its trade balance, because a persistent deficit affects output, jobs and the exchange rate, while the terms of trade affect purchasing power and matter most to countries that depend on a few commodities. The importance depends on the economy.")]]),
  eq(P("s20_21", "1(b)"), "3 marks", "Distinguish between a country's balance of trade and its terms of trade.",
     ["An explanation of a country's balance of trade: the difference in the value of exported and imported goods and services (1).", "An explanation of the terms of trade: the difference in the average prices of exports and imports, an index of export prices divided by an index of import prices (1).", "An explicit distinction stressing that one involves values and the other prices (1)."],
     "Balance of trade: value of exports minus imports. Terms of trade: ratio of export prices to import prices. Values versus prices.",
     [[("k", "The balance of trade is the value of exports of goods and services minus the value of imports, so it measures revenue and spending. The terms of trade measure the average price of exports relative to the average price of imports, as an index. The first is about values, the second is about prices.")]])
  ],
  )

tips = tips_html(
  [("Write the formula.", "Export price index ÷ import price index × 100."),
   ("Say which prices move.", "Export prices up or import prices down is an improvement."),
   ("It is about prices, not values.", "Do not mix with the balance of trade."),
   ("Exchange rate falls: ToT deteriorate.", "Exports cheaper, imports dearer."),
   ("Higher relative inflation raises export prices.", "ToT improve as measured."),
   ("An improvement is not always good.", "Exports may become uncompetitive."),
   ("Use elasticity.", "It decides the effect on the trade balance.")],
  [("Terms of trade", "The terms of trade measure export prices relative to import prices."),
   ("Improvement", "An improvement means a unit of exports buys more imports."),
   ("Deterioration", "A deterioration means more exports are needed to buy the same imports."),
   ("Elasticity", "The effect on the trade balance depends on price elasticity of demand."),
   ("Judge", "An improvement may harm competitiveness.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- formula bars ---------- */
function tfDraw(s) {
  const Y = (v) => 250 - v * 1.6; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Index (base year = 100)", "sm");
  const e = s.e, m = s.m, t = e / m * 100;
  o += SV.rect(120, Y(e), 100, 250 - Y(e), "f2", op(0.65)) + SV.text(170, 270, "Export price index", "sm", { "text-anchor": "middle" }) + SV.text(170, Y(e) - 6, Lib.fmtN(e, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(280, Y(m), 100, 250 - Y(m), "f3", op(0.65)) + SV.text(330, 270, "Import price index", "sm", { "text-anchor": "middle" }) + SV.text(330, Y(m) - 6, Lib.fmtN(m, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(440, Y(t), 100, 250 - Y(t), t >= 100 ? "f1" : "f3", op(0.65)) + SV.text(490, 270, "Terms of trade", "sm", { "text-anchor": "middle" }) + SV.text(490, Y(t) - 6, Lib.fmtN(t, 1), "lbl bd", { "text-anchor": "middle" }) + SV.line(60, Y(100), 700, Y(100), "dash") + SV.text(698, Y(100) - 6, "100", "sm", { "text-anchor": "end" });
  o += tag(620, 70, t > 100.5 ? "Improvement" : t < 99.5 ? "Deterioration" : "No change", t > 100.5 ? "c2" : "c3", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="An export price index of 110 and an import price index of 100 give terms of trade of 110">${tfDraw({ e: 110, m: 100 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 290, label: "The terms of trade from two price indices", base: { e: 100, m: 100 }, draw: tfDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Base year.</b> Export and import price indices are both 100, so the terms of trade are 100.", s: { e: 100, m: 100 } },
  { cap: "<b>Export prices rise 10%</b> and import prices are unchanged: terms of trade = 110 ÷ 100 × 100 = <b>110</b>. This is an <b>improvement</b>.", s: { e: 110, m: 100 } },
  { cap: "<b>Import prices now rise 25%</b> (an oil price shock): terms of trade = 110 ÷ 125 × 100 = <b>88</b>. A <b>deterioration</b>.", s: { e: 110, m: 125 } },
] });

/* ---------- what a unit buys ---------- */
function ubDraw(s) {
  const t = s.t, bar = (n, c, y, lab) => { let o = SV.text(40, y + 14, lab, "lbl bd"); for (let i = 0; i < Math.floor(n); i++) o += SV.rect(300 + i * 36, y, 28, 22, c, { rx: 4, ...op(0.7) }); const f = n - Math.floor(n); if (f > 0.05) o += SV.rect(300 + Math.floor(n) * 36, y, 28 * f, 22, c, { rx: 4, ...op(0.7) }); return o + SV.text(300 + Math.ceil(n) * 36 + 10, y + 16, Lib.fmtN(n, 1), "lbl bd"); };
  return bar(1, "f2", 60, "1 unit of exports (a car)") + bar(2 * t / 100, "f3", 120, "buys imports (barrels of oil)") + SV.text(40, 190, "Terms of trade = " + Lib.fmtN(t, 0), "lbl bd", { style: "fill:var(--accent)" });
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 220" role="img" aria-label="At terms of trade of 100 one car buys two barrels of oil, at 70 it buys 1.4">${ubDraw({ t: 70 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 220, label: "Imports bought per unit of exports as the terms of trade change", base: { t: 100 }, draw: ubDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Terms of trade 100.</b> One car exchanges for two barrels of oil.", s: { t: 100 } },
  { cap: "<b>Terms of trade fall to 70.</b> Oil has become dearer relative to cars, so one car now buys only 1.4 barrels: a <b>deterioration</b>. The country must export more to buy the same imports.", s: { t: 70 } },
  { cap: "<b>Terms of trade rise to 130.</b> One car now buys 2.6 barrels: an <b>improvement</b>, which raises purchasing power, but if the higher export price cuts sales, the trade balance may worsen.", s: { t: 130 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!["xp", "mp"].every((i) => $("#" + i))) return;
  const e = +$("#xp").value, m = +$("#mp").value, t = e / m * 100, ch = t - 100;
  $("#r1").textContent = Lib.fmtN(t, 1); $("#r2").textContent = (ch >= 0 ? "+" : "") + Lib.fmtN(ch, 1) + "%"; $("#r3").textContent = Lib.fmtN(2 * t / 100, 2);
  $("#rv").textContent = `Terms of trade = ${e} ÷ ${m} × 100 = ${Lib.fmtN(t, 1)}. ${ch > 0.05 ? "The index is above 100: an improvement. Each unit of exports buys more imports." : ch < -0.05 ? "The index is below 100: a deterioration. More exports are needed to buy the same imports." : "No change from the base year."} If one unit of exports bought 2 units of imports in the base year it now buys ${Lib.fmtN(2 * t / 100, 2)}.`;
  $("#labA").innerHTML = tfDraw({ e, m });
}
Lib.slider($("#g1"), { id: "xp", label: "Export price index ", min: 70, max: 140, step: 5, value: 110, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "mp", label: "Import price index ", min: 70, max: 140, step: 5, value: 100, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
const CS = [["Currency depreciates 10%", -8, 6, "A weaker currency makes exports cheaper abroad and imports dearer at home."], ["Currency appreciates 10%", 8, -6, "A stronger currency makes exports dearer abroad and imports cheaper."], ["Higher inflation at home than abroad", 6, 0, "Export prices rise faster than import prices."], ["World demand for exports rises", 12, 0, "Higher demand raises export prices."], ["World oil price jumps", 0, 15, "Import prices rise."], ["A glut of the country's commodity exports", -15, 0, "Export prices fall."]];
function showE(i) {
  const [n, e, m, why] = CS[i], t = (100 + e) / (100 + m) * 100; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = (e >= 0 ? "+" : "") + e + "%"; $("#t2").textContent = (m >= 0 ? "+" : "") + m + "%"; $("#t3").textContent = Lib.fmtN(t, 1) + " (" + (t > 100 ? "improves" : "deteriorates") + ")";
  $("#tv").textContent = `${n}: ${why} Export prices change by ${e}% and import prices by ${m}%, so the terms of trade = ${100 + e} ÷ ${100 + m} × 100 = ${Lib.fmtN(t, 1)}, an ${t > 100 ? "improvement" : "deterioration"}.`;
  const Y = (v) => 180 - v * 1.2; $("#labB").innerHTML = SV.line(40, 180, 400, 180) + [["Export price", 100 + e, "f2"], ["Import price", 100 + m, "f3"], ["Terms of trade", t, t >= 100 ? "f1" : "f3"]].map(([l, v, c], k) => SV.rect(70 + k * 110, Y(v), 80, 180 - Y(v), c, op(0.65)) + SV.text(110 + k * 110, 198, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + k * 110, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" })).join("");
}
$("#cB").innerHTML = CS.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showE(+b.dataset.i)));
showE(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to the terms of trade?", ["Improve", "Deteriorate"],
  [("Export prices rise, import prices unchanged", 0), ("The exchange rate depreciates", 1), ("World oil prices rise (country imports oil)", 1), ("Higher inflation than trading partners", 0), ("The currency appreciates", 0), ("Export prices fall", 1), ("Import prices fall", 0), ("A glut lowers the price of the main export", 1)],
  "The index rises when export prices rise relative to import prices.") + MATCH([
  ["Terms of trade", "Export price index ÷ import price index × 100"],
  ["Improvement", "Index rises; a unit of exports buys more imports"],
  ["Deterioration", "Index falls; more exports needed per import"],
  ["Balance of trade", "Value of exports minus value of imports"],
  ["Primary products", "Raw materials and farm goods with volatile prices"],
  ["Price elasticity", "Decides the effect of price changes on trade volumes"]]) + ORDER(
  "Put the effect of a depreciation on the terms of trade in order.",
  ["The exchange rate depreciates", "Export prices fall in foreign currency", "Import prices rise in home currency", "Export price index falls relative to import price index", "The terms of trade deteriorate"],
  "Cheaper exports and dearer imports lower the index.") + CALC([
  {"q": "Export price index 120 and import price index 100. What is the terms of trade?", "a": 120, "unit": "", "tol": 0.5, "hint": "120 ÷ 100 × 100.", "sol": "<b>120</b>: an improvement."},
  {"q": "Export price index 105, import price index 125. What are the terms of trade (to one decimal place)?", "a": 84, "unit": "", "tol": 0.2, "hint": "105 ÷ 125 × 100.", "sol": "<b>84</b>: a deterioration."},
  {"q": "The terms of trade index rises from 100 to 110. By what % have the terms of trade improved?", "a": 10, "unit": "%", "tol": 0.1, "hint": "10 ÷ 100.", "sol": "<b>10%</b>."},
  {"q": "Export prices rise 6% and import prices rise 10%. Approximately what is the change in the terms of trade (%)?", "a": -3.6, "unit": "%", "tol": 0.3, "hint": "1.06 ÷ 1.10 − 1.", "sol": "<b>−3.6%</b>: a deterioration."}]) + MCQ([
  ("The terms of trade are measured as:", ["Export price index ÷ import price index × 100", "Value of exports − value of imports", "Exports ÷ imports in volume", "Export income ÷ GDP"], 0, "A ratio of price indices."),
  ("An improvement in the terms of trade means:", ["Export prices rise relative to import prices", "The trade balance improves", "Imports fall", "Exports rise in volume"], 0, "Relative prices."),
  ("A depreciation will usually:", ["Worsen the terms of trade", "Improve the terms of trade", "Not affect the terms of trade", "Raise the index above 100"], 0, "Exports cheaper, imports dearer."),
  ("The terms of trade have no units because:", ["They are a ratio of two indices", "They use several currencies", "They are not measurable", "They are a percentage of GDP"], 0, "Index ÷ index."),
  ("A country that exports primary products may find its terms of trade:", ["Deteriorate over time", "Always improve", "Never change", "Equal the trade balance"], 0, "Volatile prices and slow demand growth.")
], "qz1") + CARDS([
  ("ToT formula", "Export index ÷ import index × 100."),
  ("Improvement", "Index rises."),
  ("Deterioration", "Index falls."),
  ("Depreciation", "ToT deteriorate."),
  ("Appreciation", "ToT improve."),
  ("Higher inflation", "Export prices up, ToT improve."),
  ("Not BoT", "ToT is prices; BoT is values."),
  ("Evaluate", "Elasticity and competitiveness.")]) + MCQ(mc_exam)

build("as61", "as-terms-of-trade", "Exports, Imports and the Terms of Trade", EY,
  "6.1.3: measuring the terms of trade, the causes of changes and their effects. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
