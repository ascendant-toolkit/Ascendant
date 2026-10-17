"""AS syllabus 4.1.3-4.1.4 Market and basic prices; gross and net. Run: python3 tools/artifact-kit/mk_as41c.py"""
from as6k import *
EY = EYAS("4.1.3 to 4.1.4")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>The same national income figure can be stated in different ways. <b class="kw">Market prices</b> are the prices buyers actually pay, so they <b>include taxes on products</b> (such as sales tax or VAT) and <b>exclude subsidies</b>. <b class="kw">Basic prices</b> are the amounts <b>producers receive</b>: <b>basic price = market price − taxes on products + subsidies on products</b>, so basic prices show the value of production without the effect of government taxes and subsidies on products. A <b class="kw">gross</b> figure is before deducting <b>capital consumption (depreciation)</b>, and a <b class="kw">net</b> figure is after it, so net is always lower than the matching gross figure. Combining the two ideas gives measures such as GDP at market prices, GDP at basic prices, GNI at market prices and NNI, and a careful answer states which one is being used.</p></div>

  <h2>1 · Market prices and basic prices</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Market prices</th><th>Basic prices</th></tr>
    <tr><td><b>Meaning</b></td><td>What the buyer pays</td><td>What the producer receives</td></tr>
    <tr><td><b>Taxes on products</b> (sales tax, VAT, excise)</td><td>Included</td><td>Excluded</td></tr>
    <tr><td><b>Subsidies on products</b></td><td>Excluded (the buyer pays a lower price, the subsidy is paid to the producer)</td><td>Included</td></tr>
    <tr><td><b>Conversion</b></td><td>Basic = market − taxes + subsidies</td><td>Market = basic + taxes − subsidies</td></tr>
  </table></div>
  <ul>
    <li><b>Worked example:</b> a product sells for $100 including $15 sales tax, and the government pays the producer a $5 subsidy. The producer receives $85 from the buyer and $5 from the government, so the <b>basic price is $90</b> (100 − 15 + 5).</li>
    <li><b>Economy-wide:</b> GDP at market prices $120bn; taxes on products $15bn; subsidies $5bn. GDP at basic prices = 120 − 15 + 5 = <b>$110bn</b>.</li>
    <li><b>Why basic prices are used:</b> they show the value of production before the distortion caused by taxes and subsidies, so they allow fairer comparisons of the output of different industries or countries with different tax systems.</li>
    <li>Market prices matter for <b>spending</b>: they are the prices that households and firms actually face.</li>
  </ul>

  <h2>2 · Gross and net</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Gross</b> means before deducting capital consumption. <b>Net</b> means after deducting it: <b>net = gross − capital consumption</b>.</li>
    <li>GDP and GNI are <b>gross</b> measures. NNI is a <b>net</b> measure. There are also net versions of GDP (net domestic product, NDP = GDP − capital consumption).</li>
    <li><b>Why net can be more useful:</b> it shows how much output is available for consumption and new investment after replacing capital that has worn out, so it better indicates whether capacity is being maintained.</li>
    <li><b>Why gross is used more often:</b> capital consumption is difficult to measure accurately, since the lives of machines and buildings vary.</li>
  </ul>

  <h2>3 · Putting the adjustments together</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Calculation</th><th>Example ($bn)</th></tr>
    <tr><td>GDP at market prices</td><td>Given</td><td>120</td></tr>
    <tr><td>GDP at basic prices</td><td>− taxes on products + subsidies</td><td>120 − 15 + 5 = 110</td></tr>
    <tr><td>Net domestic product at market prices</td><td>GDP − capital consumption</td><td>120 − 10 = 110</td></tr>
    <tr><td>GNI at market prices</td><td>GDP + net primary income</td><td>120 − 5 = 115</td></tr>
    <tr><td>NNI at market prices</td><td>GNI − capital consumption</td><td>115 − 10 = 105</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Read which <b>price basis</b> and which <b>gross or net</b> measure the question wants. Remember: <b>market to basic</b> = subtract taxes, add subsidies. <b>Gross to net</b> = subtract depreciation. Write each step.</div>
'''

watch = '''
  <h2>1 · From market prices to basic prices</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · From gross to net</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · Market prices to basic prices</h2>
  <p>Change the figures ($ billion) and see GDP at basic prices.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Taxes less subsidies</small><strong id="r1"></strong></div><div><small>GDP at basic prices</small><strong id="r2"></strong></div><div><small>Basic as % of market</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 260" role="img" aria-label="Bars for GDP at market prices and at basic prices"></svg></div></div></div>

  <h2>Lab 2 · Gross to net</h2>
  <p>Change capital consumption to see gross and net values.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Net domestic product</small><strong id="t1"></strong></div><div><small>Depreciation as % of GDP</small><strong id="t2"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars for gross and net values"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Included at market prices or at basic prices?</h2><div id="cl1" class="card"></div>
  <h2>2 · Gross or net?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Sales tax on a phone", "A phone costs $230 in the shop, including $30 of sales tax. The producer receives $200. National income at market prices counts $230; at basic prices, it counts what producers receive.", "market prices versus basic prices.") +
rw("A farm subsidy", "The government pays farmers $10 for each tonne of grain. The market price to the buyer is lower than the amount farmers receive in total, so the basic price includes the subsidy.", "subsidies and basic prices.") +
rw("A factory that wears out", "A factory spends $8m a year just to replace worn-out machines. Gross output counts the $8m of replacement, but the net figure subtracts it, showing the output available to raise living standards or expand capacity.", "gross versus net.") +
rw("Comparing countries with different taxes", "Two countries produce the same goods, but one has a high sales tax. GDP at market prices looks larger there, while GDP at basic prices removes the effect of the tax, making comparison fairer.", "why basic prices are used.")
)

mc_exam = [
  mcq("s24_11", 16, "A country's net national income (NNI) is less than its gross national income (GNI). What does this mean?", ["incomes earned overseas were less than incomes sent overseas", "inflation has been accounted for in NNI but not in GNI", "the country's exports decreased", "there has been a net depreciation in the value of the country's fixed capital assets"], 3, "NNI is GNI minus capital consumption, so NNI is lower when capital has depreciated.")
]

exam = exam_page("market prices, basic prices, gross and net",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Basic prices and the gross and net distinction are rarely tested in past papers, and appear only in short Paper 1 questions, so one is shown below. The Practise tab drills the calculations, because they can appear in any series.",
  [("Multiple choice (Paper 1)", "1 shown below", "2024 to 2024")],
  [],
  )

tips = tips_html(
  [("Market prices include taxes.", "What the buyer pays."),
   ("Basic prices are what producers get.", "Market − taxes + subsidies."),
   ("Gross is before depreciation.", "Net is after."),
   ("Write the steps.", "One adjustment per line."),
   ("Check the direction.", "Basic is below market if taxes exceed subsidies."),
   ("Net is below gross.", "By capital consumption."),
   ("State the basis.", "Say which measure you are using.")],
  [("Market prices", "Market prices include taxes on products and exclude subsidies."),
   ("Basic prices", "Basic prices are what producers receive: market prices minus taxes plus subsidies."),
   ("Gross", "A gross value is before deducting capital consumption."),
   ("Net", "A net value is after deducting capital consumption."),
   ("Capital consumption", "Capital consumption is the value of capital worn out in a year.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = WFJS + CHAINJS + '''
const itemsB = [["GDP at market prices", 120, "t", 120, 0], ["Taxes on products", -15, "d", 120, 105], ["Subsidies on products", 5, "d", 110, 105], ["GDP at basic prices", 110, "t", 110, 0]];
function bDraw(s) { return wfDraw(itemsB, s); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP at market prices of 120, less taxes on products of 15, plus subsidies of 5, gives GDP at basic prices of 110">${bDraw({ k: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 290, label: "GDP from market prices to basic prices", base: { k: 0 }, draw: bDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Market prices</b> are what buyers pay, including sales taxes: $120bn.", s: { k: 1 } },
  { cap: "<b>Subtract taxes on products</b> ($15bn). Producers do not receive this money.", s: { k: 2 } },
  { cap: "<b>Add subsidies on products</b> ($5bn). Producers do receive this money.", s: { k: 3 } },
  { cap: "<b>GDP at basic prices = 120 − 15 + 5 = $110bn</b>, the amount producers actually receive.", s: { k: 4 } },
] });
const itemsG = [["Gross domestic product", 120, "t", 120, 0], ["Capital consumption", -10, "d", 120, 110], ["Net domestic product", 110, "t", 110, 0], ["Net primary income", -5, "d", 110, 105], ["NNI", 105, "t", 105, 0]];
function gDraw(s) { return wfDraw(itemsG, s); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Gross domestic product of 120 less capital consumption of 10 gives net domestic product of 110; adjusting for net primary income of minus 5 gives NNI of 105">${gDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 290, label: "From gross to net", base: { k: 0 }, draw: gDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Gross domestic product</b> counts all output, including output needed to replace worn-out capital: $120bn.", s: { k: 1 } },
  { cap: "<b>Capital consumption</b> of $10bn is the value of capital used up.", s: { k: 2 } },
  { cap: "<b>Net domestic product = $110bn.</b> This is output available to consume or to add to the capital stock.", s: { k: 3 } },
  { cap: "<b>Net primary income from abroad</b> of −$5bn moves from a domestic to a national measure.", s: { k: 4 } },
  { cap: "<b>NNI = $105bn.</b> Both adjustments applied: net and national.", s: { k: 5 } },
] });

function labP() {
  if (!["gd", "tx", "sb"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, tx = +$("#tx").value, sb = +$("#sb").value, basic = gdp - tx + sb, ts = tx - sb;
  $("#r1").textContent = (ts >= 0 ? "" : "−") + "$" + Math.abs(ts) + "bn"; $("#r2").textContent = "$" + basic + "bn"; $("#r3").textContent = Lib.fmtN((basic / gdp) * 100, 1) + "%";
  $("#rv").textContent = `GDP at basic prices = ${gdp} − ${tx} + ${sb} = ${basic}. ${ts > 0 ? "Taxes on products exceed subsidies, so basic prices are below market prices." : ts < 0 ? "Subsidies exceed taxes, so basic prices are above market prices." : "Taxes equal subsidies, so the two are equal."}`;
  const Y = (v) => 240 - v * 1.2; let o = SV.line(40, 240, 400, 240);
  [["Market", gdp, "f1"], ["Basic", basic, "f2"]].forEach(([l, v, c], i) => (o += SV.rect(90 + i * 140, Y(v), 90, 240 - Y(v), c, op(0.65)) + SV.text(135 + i * 140, 258, l, "sm", { "text-anchor": "middle" }) + SV.text(135 + i * 140, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP at market prices, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "tx", label: "Taxes on products, $bn ", min: 0, max: 40, step: 1, value: 15, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "sb", label: "Subsidies on products, $bn ", min: 0, max: 30, step: 1, value: 5, fmt: (v) => v, onInput: labP });
labP();
function labG() {
  if (!["gg", "cc"].every((i) => $("#" + i))) return;
  const g = +$("#gg").value, c = +$("#cc").value, n = g - c;
  $("#t1").textContent = "$" + n + "bn"; $("#t2").textContent = Lib.fmtN((c / g) * 100, 1) + "%";
  $("#tv").textContent = `Net domestic product = ${g} − ${c} = ${n}. Capital consumption is ${Lib.fmtN((c / g) * 100, 1)}% of GDP. ${c / g > 0.15 ? "A large share of output is only replacing worn-out capital, leaving less for consumption and growth." : "A small share of output is needed to replace capital."}`;
  const Y = (v) => 190 - v * 0.9; let o = SV.line(40, 190, 400, 190);
  [["Gross", g, "f1"], ["Depreciation", c, "f3"], ["Net", n, "f2"]].forEach(([l, v, k], i) => (o += SV.rect(60 + i * 110, Y(v), 80, 190 - Y(v), k, op(0.65)) + SV.text(100 + i * 110, 208, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Gross domestic product, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labG });
Lib.slider($("#g5"), { id: "cc", label: "Capital consumption, $bn ", min: 0, max: 40, step: 1, value: 10, fmt: (v) => v, onInput: labG });
labG();
''' + CLASSIFY("cl1", "Is it included at market prices or at basic prices?", ["Market prices only", "Basic prices only"],
  [("Sales tax paid by the buyer", 0), ("A subsidy paid to the producer", 1), ("VAT collected on a purchase", 0), ("Government payment per tonne of grain produced", 1), ("The price printed on the shop label", 0), ("The amount the producer actually receives for the good", 1)],
  "Market prices include taxes on products; basic prices include subsidies.") + CLASSIFY("cl2", "Is it a gross or a net measure?", ["Gross", "Net"],
  [("GDP", 0), ("NNI", 1), ("GNI", 0), ("Net domestic product", 1), ("A figure before deducting depreciation", 0), ("A figure after deducting capital consumption", 1)],
  "Gross is before depreciation; net is after.") + ORDER(
  "Put the steps from GDP at market prices to NNI in order.",
  ["Start with GDP at market prices", "Adjust for net primary income from abroad to reach GNI", "Subtract capital consumption", "This gives NNI at market prices"],
  "GDP + net primary income − capital consumption = NNI.") + MATCH([
  ["Market prices", "Prices buyers pay, including product taxes"],
  ["Basic prices", "Market prices minus taxes plus subsidies"],
  ["Gross", "Before deducting capital consumption"],
  ["Net", "After deducting capital consumption"],
  ["Taxes on products", "Sales taxes such as VAT"],
  ["Subsidies on products", "Payments to producers per unit produced"]]) + CALC([
  {"q": "GDP at market prices is $200bn, taxes on products $25bn and subsidies $10bn. What is GDP at basic prices ($bn)?", "a": 185, "unit": "$bn", "tol": 0.5, "hint": "200 − 25 + 10.", "sol": "<b>$185bn</b>."},
  {"q": "A good costs $120 in the shop including $20 of sales tax. There is no subsidy. What is the basic price ($)?", "a": 100, "unit": "$", "tol": 0.5, "hint": "120 − 20.", "sol": "<b>$100</b>."},
  {"q": "GDP at basic prices is $450bn, taxes on products $60bn and subsidies $20bn. What is GDP at market prices ($bn)?", "a": 490, "unit": "$bn", "tol": 0.5, "hint": "450 + 60 − 20.", "sol": "<b>$490bn</b>."},
  {"q": "GDP is $300bn and capital consumption is $36bn. What is net domestic product ($bn)?", "a": 264, "unit": "$bn", "tol": 0.5, "hint": "300 − 36.", "sol": "<b>$264bn</b>."},
  {"q": "What percentage of GDP is capital consumption?", "a": 12, "unit": "%", "tol": 0.1, "hint": "36 ÷ 300.", "sol": "<b>12%</b>."}]) + MCQ([
  ("Basic prices equal:", ["Market prices − taxes on products + subsidies", "Market prices + taxes", "Market prices − subsidies", "Market prices + depreciation"], 0, "What producers receive."),
  ("Market prices include:", ["Taxes on products", "Subsidies only", "Depreciation", "Net primary income"], 0, "What buyers pay."),
  ("A net figure is:", ["After deducting capital consumption", "Before deducting capital consumption", "Adjusted for inflation", "Adjusted for population"], 0, "Gross minus depreciation."),
  ("Net national income is lower than gross national income because of:", ["Capital consumption", "Taxes", "Subsidies", "Exports"], 0, "Depreciation."),
  ("If subsidies exceed taxes on products, basic prices are:", ["Above market prices", "Below market prices", "Equal to market prices", "Zero"], 0, "More is added than subtracted.")
], "qz1") + CARDS([
  ("Market prices", "What the buyer pays."),
  ("Basic prices", "Market − taxes + subsidies."),
  ("Gross", "Before depreciation."),
  ("Net", "After depreciation."),
  ("NDP", "GDP − depreciation."),
  ("NNI", "GNI − depreciation."),
  ("Taxes on products", "VAT and similar."),
  ("Why basic?", "Removes the effect of product taxes.")]) + MCQ(mc_exam)

build("as41c", "as-market-basic-prices-gross-net", "Market Prices, Basic Prices, Gross and Net", EY,
  "4.1.3 to 4.1.4: converting national income between market and basic prices and between gross and net values. Animated diagrams, labs, drills and the past paper question.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
