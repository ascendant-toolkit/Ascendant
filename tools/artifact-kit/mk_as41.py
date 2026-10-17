"""AS syllabus 4.1.1 National income and GDP. Run: python3 tools/artifact-kit/mk_as41.py"""
from as6k import *
EY = EYAS("4.1.1")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">National income</b> is the total value of the goods and services an economy produces in a period, normally a year. <b class="kw">Gross Domestic Product (GDP)</b> is the <b>value of all final goods and services produced within a country's borders</b>, whoever owns the firms. Because every pound or dollar spent is also income for someone, there are <b>three ways to measure it</b> that should give the same total: the <b>output (value added) method</b>, the <b>income method</b> and the <b>expenditure method</b>, where <b>GDP = C + I + G + (X − M)</b>. Only <b>final</b> goods are counted, to avoid <b>double counting</b> of intermediate goods. <b>Real</b> GDP adjusts for inflation and <b>GDP per capita</b> divides by population, but GDP has limits as a measure of living standards, since it misses the <b>informal economy</b>, unpaid work, inequality and damage to the environment.</p></div>

  <h2>1 · What GDP measures</h2>
  <ul>
    <li><b>Flow of output:</b> GDP is a <b>flow</b> (value per year), not a stock of wealth.</li>
    <li><b>Inside the borders:</b> GDP counts output produced in the country, including that of <b>foreign-owned firms</b> located there, and excludes output of the country's firms abroad. (GNI, on the next page, adjusts for this.)</li>
    <li><b>Final goods only:</b> goods bought for consumption, investment, government use or export. <b>Intermediate goods</b> (flour bought by a baker) are used up in making other goods and are not counted separately, because their value is already in the final price.</li>
    <li><b>Market value:</b> goods are valued at prices. Output not sold for money (home production, voluntary work) is generally excluded.</li>
    <li><b>Circular flow link:</b> the value of output equals the incomes paid to factors of production, which equals the spending on that output.</li>
  </ul>

  <h2>2 · Three ways to measure GDP</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>What is added up</th><th>Example</th></tr>
    <tr><td><b>Output (value added)</b></td><td>The value added at each stage of production in every industry: value of output minus the cost of intermediate goods</td><td>Farm $40 + mill $30 + bakery $50 = $120</td></tr>
    <tr><td><b>Income</b></td><td>Incomes earned from producing output: wages, rent, interest and profit (before tax)</td><td>Wages + rent + interest + profit</td></tr>
    <tr><td><b>Expenditure</b></td><td>Total spending on final goods and services: <b>C + I + G + (X − M)</b></td><td>Consumption + investment + government spending + net exports</td></tr>
  </table></div>
  <ul>
    <li><b>C:</b> household consumption; <b>I:</b> investment by firms (capital goods, stocks); <b>G:</b> government spending on goods and services (not transfer payments such as pensions, which are not payment for output); <b>X − M:</b> exports minus imports, so that spending on imports is removed and foreign spending on exports is added.</li>
    <li>In practice the three measures differ a little because of data errors; a <b>statistical discrepancy</b> is used to reconcile them.</li>
  </ul>

  <h2>3 · Value added and double counting</h2>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>Sells for</th><th>Cost of inputs</th><th>Value added</th></tr>
    <tr><td>Farmer (wheat)</td><td>$40</td><td>$0</td><td>$40</td></tr>
    <tr><td>Miller (flour)</td><td>$70</td><td>$40</td><td>$30</td></tr>
    <tr><td>Baker (bread)</td><td>$120</td><td>$70</td><td>$50</td></tr>
    <tr><td>Total</td><td>Final price $120</td><td></td><td>$120</td></tr>
  </table></div>
  <ul>
    <li>If every sale were added ($40 + $70 + $120 = $230), the output of the farmer and miller would be counted <b>more than once</b>. The correct addition is the final price, $120, which equals the sum of value added.</li>
  </ul>

  <h2>4 · Real GDP and GDP per capita</h2>
  <ul>
    <li><b>Nominal (money) GDP</b> is measured at current prices, so it can rise because prices rise. <b>Real GDP</b> is adjusted for inflation using a price index (the GDP deflator): <b>real GDP = nominal GDP ÷ price index × 100</b>. Real GDP shows changes in the actual quantity of output.</li>
    <li><b>GDP per capita</b> = GDP ÷ population. It is a better indicator of average living standards than total GDP, since a country can have a large GDP and a low income per person.</li>
    <li>Example: nominal GDP $550bn with a price index of 110 gives real GDP of $500bn.</li>
  </ul>

  <h2>5 · Limits of GDP as a measure of living standards</h2>
  <ul>
    <li><b>Informal and illegal activity</b> is not recorded, so poorer economies may be understated.</li>
    <li><b>Unpaid work</b> (housework, voluntary work) is excluded.</li>
    <li><b>Distribution:</b> an average hides inequality.</li>
    <li><b>Quality and variety</b> of goods, leisure time and working conditions are not captured.</li>
    <li><b>Environmental damage</b> and resource depletion are not deducted, and goods that harm welfare still raise GDP.</li>
    <li><b>Different price levels</b> across countries make exchange-rate comparisons misleading, which is why purchasing power adjustments are used.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>State the <b>formula</b> and say that it measures <b>final</b> goods <b>inside the borders</b>. For limits, give two or three developed points and say what they mean for <b>comparing living standards</b>. Use "may" and "likely".</div>
'''

watch = '''
  <h2>1 · Value added in a chain of production</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Building GDP by the expenditure method</h2>
  <div id="stB"></div>
  <h2>3 · The same total three ways</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Expenditure method</h2>
  <p>Change the components ($ billion) to see GDP and the share of each part.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>GDP</small><strong id="r1"></strong></div><div><small>Net exports</small><strong id="r2"></strong></div><div><small>Consumption share</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 260" role="img" aria-label="Bars for the components of GDP and the total"></svg></div></div></div>

  <h2>Lab 2 · Real GDP and GDP per head</h2>
  <p>Set nominal GDP, the price index and population to see real GDP and income per head.</p>
  <div class="card"><div class="grid2"><div><div id="g6"></div><div id="g7"></div><div id="g8"></div>
    <div class="readout"><div><small>Real GDP</small><strong id="t1"></strong></div><div><small>Real GDP per head</small><strong id="t2"></strong></div><div><small>Inflation effect</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars comparing nominal and real GDP"></svg></div></div></div>
''' + chooser_html("h", "Lab 3 · Is it counted in GDP?", "Choose a transaction to see whether it is counted in GDP, and why.", ["Counted?", "Reason", "Which component"])

practise = '''
  <h2>1 · Is it a component of expenditure?</h2><div id="cl1" class="card"></div>
  <h2>2 · Counted in GDP or not?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Bread from field to shop", "A farmer, a miller and a baker each add value. Only the final price of the loaf enters GDP, which equals the sum of value added, so the wheat and flour are not counted twice.", "value added and double counting.") +
rw("A foreign-owned car plant", "A car factory owned by an overseas firm produces cars in the country. The output counts in GDP because it is produced inside the borders, even though the profits go abroad.", "GDP counts output inside the borders, whoever owns the firm.") +
rw("Unpaid care and the informal economy", "Parents caring for children, volunteers and street traders paid in cash may not appear in official figures. GDP may understate output and living standards, especially in lower-income economies.", "limits of GDP as a measure.") +
rw("Rebuilding after a flood", "Spending on repairs raises recorded GDP, but people are no better off than before the flood. GDP counts the spending, not the loss of wealth.", "why higher GDP does not always mean higher welfare.") +
rw("Comparing two countries", "One country has a larger GDP but a much bigger population, so GDP per head is lower. Comparing per head figures, and using purchasing power adjustments, gives a better picture of average living standards.", "GDP per capita and its use.")
)

mc_exam = [
  mcq("m25_12", 19, "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head?", ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], 3, "Income per head = 1.10 ÷ 0.90 = 1.222, a rise of about 22%, which is more than 20%."),
  mcq("s23_12", 20, "What is used to convert nominal GDP to real GDP?", ["exchange rates", "changes in the price level", "interest rates", "taxation"], 1, "A price index adjusts nominal values for inflation."),
  mcq("s23_13", 20, "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2?", ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], 3, "Real GDP = 577.5 ÷ 1.05 = 550."),
  mcq("s20_13", 25, "The real national income of a country fell by 3%. What could have caused this?", ["Money national income fell by 3% when the rate of inflation was 6%.", "Money national income fell by 6% when the rate of inflation was 3%.", "Money national income rose by 3% when the rate of inflation was 6%.", "Money national income rose by 6% when the rate of inflation was 3%."], 2, "Real income falls by about 3% when money income rises 3% and prices rise 6%.")
]

exam = exam_page("national income and GDP",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). National income and GDP appear mostly in Paper 1, as calculations and as questions on real and nominal figures, with short data-response parts in Paper 2. Four Paper 1 multiple choice questions are shown below; the Practise tab drills the calculations.",
  [("Multiple choice (Paper 1)", "4 shown below", "2020 to 2025")],
  [],
  )

tips = tips_html(
  [("Say 'final' and 'inside the borders'.", "The two key words in the definition."),
   ("Write the formula.", "C + I + G + (X − M)."),
   ("Three methods, one total.", "Output, income, expenditure."),
   ("Avoid double counting.", "Count final goods or value added, not every sale."),
   ("Real not nominal.", "Adjust for inflation with a price index."),
   ("Per head.", "Divide by population to compare living standards."),
   ("Give limits.", "Informal economy, inequality, environment, unpaid work.")],
  [("GDP", "GDP is the value of final goods and services produced within a country in a year."),
   ("Value added", "Value added is the value of output minus the cost of intermediate goods."),
   ("Double counting", "Double counting is counting the same output more than once."),
   ("Real GDP", "Real GDP is GDP adjusted for inflation."),
   ("GDP per capita", "GDP per capita is GDP divided by population.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = WFJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Output", "Value added in every industry", 30, "f1"], ["Income", "Wages, rent, interest, profit", 270, "f2"], ["Expenditure", "C + I + G + (X − M)", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 55, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 82, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 142, "Same total: value of output = incomes earned = spending on final output", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 160" role="img" aria-label="The output, income and expenditure methods give the same GDP">${o}</svg>`;
})();
chainStep("#stA", "Value added in a chain of production", ["Farmer grows wheat and sells it for $40: value added $40", "Miller buys wheat for $40, sells flour for $70: value added $30", "Baker buys flour for $70, sells bread for $120: value added $50", "Total value added: 40 + 30 + 50 = $120", "Only the final price ($120) is counted; adding all sales ($230) would double count"], [
  "<b>The first stage:</b> no intermediate inputs, so value added is the whole $40.", "<b>The mill</b> adds $30 to the $40 wheat.", "<b>The bakery</b> adds $50 to the $70 flour.", "<b>Sum of value added</b> equals the value of the final loaf.", "<b>Double counting</b> would overstate GDP by counting wheat and flour twice."]);
const itemsE = [["C", 600, "t", 600, 0], ["I", 150, "d", 750, 600], ["G", 200, "d", 950, 750], ["X", 180, "d", 1130, 950], ["M", -160, "d", 1130, 970], ["GDP", 970, "t", 970, 0]];
function eDraw(s) { return wfDraw(itemsE, s); }
Lib.stepper($("#stB"), { w: 760, h: 290, label: "GDP by the expenditure method", base: { k: 0 }, draw: eDraw, tween: 800, dwell: 4800, steps: [
  { cap: "<b>Consumption (C)</b> is household spending: $600bn.", s: { k: 1 } },
  { cap: "<b>Investment (I)</b> by firms in capital goods and stocks adds $150bn.", s: { k: 2 } },
  { cap: "<b>Government spending (G)</b> on goods and services adds $200bn.", s: { k: 3 } },
  { cap: "<b>Exports (X)</b> are spending by foreigners on domestic output: +$180bn.", s: { k: 4 } },
  { cap: "<b>Imports (M)</b> are spending on foreign output and are subtracted: −$160bn.", s: { k: 5 } },
  { cap: "<b>GDP = 600 + 150 + 200 + (180 − 160) = $970bn.</b>", s: { k: 6 } },
] });
chainStep("#stC", "The same total three ways", ["Firms produce $970bn of final output (output method: sum of value added)", "They pay out $970bn as wages, rent, interest and profit (income method)", "Households, firms, government and foreigners spend $970bn on it (expenditure method)", "Output = income = expenditure, so GDP can be measured from any side"], [
  "<b>Output</b> is produced by firms.", "<b>Income</b> is paid to the owners of factors of production.", "<b>Expenditure</b> is the total spent on the final output.", "<b>Circular flow of income:</b> all three describe the same flow."]);

/* ---------- Lab 1 ---------- */
function labE() {
  const ids = ["gc", "gi", "gg", "gx", "gm"];
  if (!ids.every((i) => $("#" + i))) return;
  const [c, i, g, x, m] = ids.map((k) => +$("#" + k).value), gdp = c + i + g + x - m;
  $("#r1").textContent = "$" + gdp + "bn"; $("#r2").textContent = (x - m >= 0 ? "+" : "") + (x - m); $("#r3").textContent = Lib.fmtN((c / gdp) * 100, 0) + "%";
  $("#rv").textContent = `GDP = ${c} + ${i} + ${g} + (${x} − ${m}) = ${gdp}. ${x - m >= 0 ? "Net exports are positive, a trade surplus that adds to GDP." : "Net exports are negative, a trade deficit that subtracts from GDP."} Consumption is ${Lib.fmtN((c / gdp) * 100, 0)}% of GDP.`;
  const mx = Math.max(gdp, c, 1), W = (v) => (Math.abs(v) / mx) * 250, row = (y, l, v, k) => SV.text(10, y + 15, l, "sm") + SV.rect(100, y, Math.max(2, W(v)), 22, k, op(0.7)) + SV.text(106 + W(v), y + 16, (v < 0 ? "−" : "") + Math.abs(v), "lbl bd");
  $("#labA").innerHTML = row(10, "C", c, "f1") + row(48, "I", i, "f2") + row(86, "G", g, "f3") + row(124, "X", x, "f1") + row(162, "M", -m, "f3") + row(210, "GDP", gdp, "f2");
}
[["g1", "gc", "Consumption (C), $bn ", 300, 900, 600], ["g2", "gi", "Investment (I), $bn ", 50, 300, 150], ["g3", "gg", "Government spending (G), $bn ", 50, 400, 200], ["g4", "gx", "Exports (X), $bn ", 50, 400, 180], ["g5", "gm", "Imports (M), $bn ", 50, 400, 160]].forEach(([el, id, lab, mn, mx, v]) => Lib.slider($("#" + el), { id, label: lab, min: mn, max: mx, step: 10, value: v, fmt: (z) => z, onInput: labE }));
labE();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!["ng", "pi", "pp"].every((i) => $("#" + i))) return;
  const n = +$("#ng").value, pi = +$("#pi").value, pop = +$("#pp").value, real = (n / pi) * 100, ph = (real * 1000) / pop;
  $("#t1").textContent = "$" + Lib.fmtN(real, 1) + "bn"; $("#t2").textContent = "$" + Lib.fmtN(ph, 0); $("#t3").textContent = Lib.fmtN(n - real, 1) + "bn";
  $("#tv").textContent = `Real GDP = ${n} ÷ ${pi} × 100 = ${Lib.fmtN(real, 1)}. ${pi > 100 ? `Prices have risen, so nominal GDP overstates the growth in output by $${Lib.fmtN(n - real, 1)}bn.` : "Prices have not risen, so nominal and real GDP are the same."} Real GDP per head is $${Lib.fmtN(ph, 0)} for a population of ${pop} million.`;
  const mx = Math.max(n, real), W = (v) => (v / mx) * 280, bar = (y, l, v, k) => SV.text(10, y + 15, l, "sm") + SV.rect(110, y, W(v), 24, k, op(0.7)) + SV.text(116 + W(v), y + 17, Lib.fmtN(v, 0), "lbl bd");
  $("#labB").innerHTML = bar(40, "Nominal", n, "f3") + bar(100, "Real", real, "f1");
}
Lib.slider($("#g6"), { id: "ng", label: "Nominal GDP, $bn ", min: 200, max: 1000, step: 10, value: 550, fmt: (v) => v, onInput: labR });
Lib.slider($("#g7"), { id: "pi", label: "Price index (base year 100) ", min: 80, max: 160, step: 5, value: 110, fmt: (v) => v, onInput: labR });
Lib.slider($("#g8"), { id: "pp", label: "Population, millions ", min: 5, max: 100, step: 5, value: 25, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 3 ---------- */
chooser("h", [
  ["A new car sold to a household", "Yes", "Final good produced this year", "Consumption (C)"],
  ["Flour bought by a bakery", "No (on its own)", "Intermediate good: its value is in the price of the bread", "Not counted separately"],
  ["A firm buys a new machine", "Yes", "Capital good for production", "Investment (I)"],
  ["A government pays teachers and builds schools", "Yes", "Government spending on goods and services", "Government (G)"],
  ["A pension payment to a retired person", "No", "A transfer payment: not payment for current output", "Not counted"],
  ["A second-hand car sold between households", "No", "Not produced this year; the dealer's margin is counted", "Only the margin"],
  ["Housework done by a parent", "No", "Unpaid and not recorded", "Not counted"]
].map((r) => [r[0], r[1], r[2], r[3], r[1].startsWith("Yes") ? 5 : r[1].startsWith("No (on") ? 2 : 1]), (it) => `${it[0]}: ${it[1].toLowerCase()}. ${it[2]}. ${it[3] === "Not counted" || it[3].startsWith("Not") || it[3].startsWith("Only") ? "" : "Component: " + it[3] + "."}`, "Clarity of inclusion (5 = clearly counted)");
''' + CLASSIFY("cl1", "Which component of expenditure is it?", ["C", "I", "G", "X − M"],
  [("Households buy food and clothing", 0), ("A firm buys a new factory machine", 1), ("The government pays for road building", 2), ("Foreign customers buy the country's cars", 3), ("Households buy imported phones", 3), ("A firm adds to its stock of unsold goods", 1), ("The government pays doctors' salaries", 2), ("A household buys a holiday at home", 0)],
  "C consumption, I investment, G government spending, X − M net exports (imports are subtracted).") + CLASSIFY("cl2", "Is it counted in GDP?", ["Counted", "Not counted"],
  [("A new house built this year", 0), ("Steel sold to a car maker (an intermediate good)", 1), ("A haircut paid for in cash and recorded", 0), ("Unpaid voluntary work", 1), ("A pension payment (transfer)", 1), ("A new school built by the government", 0), ("The sale of a second-hand car (only the dealer's margin counts)", 1), ("Output of a foreign-owned factory in the country", 0)],
  "GDP counts final goods and services produced inside the borders this year; transfers, intermediate goods, unpaid work and second-hand sales (except margins) are excluded.") + ORDER(
  "Put the steps in order for measuring GDP by the expenditure method.",
  ["Measure consumption (C)", "Add investment (I)", "Add government spending (G)", "Add exports and subtract imports (X − M)", "The total is GDP"],
  "C + I + G + (X − M) = GDP.") + MATCH([
  ["GDP", "Value of final output produced within a country in a year"],
  ["Value added", "Value of output minus the cost of intermediate goods"],
  ["Double counting", "Counting the same output more than once"],
  ["Real GDP", "GDP adjusted for inflation"],
  ["GDP per capita", "GDP divided by population"],
  ["Transfer payment", "Money paid without output in return, such as a pension"]]) + CALC([
  {"q": "C = 700, I = 200, G = 250, X = 220, M = 190 ($bn). What is GDP ($bn)?", "a": 1180, "unit": "$bn", "tol": 0.5, "hint": "700 + 200 + 250 + 220 − 190.", "sol": "<b>$1180bn</b>."},
  {"q": "A farmer sells wheat for $30, a miller sells flour for $55 and a baker sells bread for $100. What is the value added by the baker ($)?", "a": 45, "unit": "$", "tol": 0.5, "hint": "100 − 55.", "sol": "<b>$45</b>."},
  {"q": "What is the total value added in the chain ($)?", "a": 100, "unit": "$", "tol": 0.5, "hint": "30 + 25 + 45.", "sol": "<b>$100</b>, equal to the final price."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "Real GDP is $550bn and the population is 11 million. What is real GDP per head ($)?", "a": 50000, "unit": "$", "tol": 50, "hint": "550,000m ÷ 11m.", "sol": "<b>$50,000</b>."}]) + MCQ([
  ("GDP measures:", ["Final goods and services produced inside the country", "All sales including intermediate goods", "Wealth", "Output of the country's firms abroad only"], 0, "A flow of final output inside the borders."),
  ("Expenditure GDP is:", ["C + I + G + (X − M)", "C + I + G − X + M", "C + S + T", "X − M"], 0, "The expenditure formula."),
  ("Counting the output of the miller and the baker in full would cause:", ["Double counting", "Underestimation", "Deflation", "A transfer"], 0, "Intermediate goods counted twice."),
  ("Real GDP is calculated by:", ["Adjusting nominal GDP for inflation", "Adding net exports", "Dividing by population", "Adding taxes"], 0, "Divide by the price index."),
  ("A limit of GDP as a welfare measure is:", ["It ignores unpaid work and the informal economy", "It counts every activity", "It is adjusted for inequality", "It deducts pollution"], 0, "Many activities are not recorded.")
], "qz1") + CARDS([
  ("GDP", "Final output inside the borders."),
  ("Three methods", "Output, income, expenditure."),
  ("Expenditure", "C + I + G + (X − M)."),
  ("Value added", "Output minus intermediate inputs."),
  ("Double counting", "Counting intermediate goods too."),
  ("Real GDP", "Nominal ÷ price index × 100."),
  ("Per capita", "GDP ÷ population."),
  ("Limits", "Informal, unpaid, inequality, environment.")]) + MCQ(mc_exam)

build("as41", "as-national-income-statistics", "National Income and GDP", EY,
  "4.1.1: national income, the output, income and expenditure methods of measuring GDP, value added, real GDP and GDP per head, and the limits of GDP. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
