"""AS syllabus 4.1 National income statistics. Run: python3 tools/artifact-kit/mk_as41.py"""
from asx import *
EY = EYAS("4.1")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">National income</b> is the total value of the goods and services an economy produces in a year, which equals the <b>total income</b> earned and the <b>total expenditure</b> on that output. <b class="kw">Gross Domestic Product (GDP)</b> is the value of final output produced <b>within a country's borders</b>, whoever owns the firms; <b class="kw">Gross National Income (GNI)</b> is GDP plus <b>net primary income from abroad</b> (income earned by residents overseas minus income sent home by foreign owners); and <b class="kw">Net National Income (NNI)</b> is GNI minus <b>capital consumption (depreciation)</b>. Figures can be quoted at <b>market prices</b> (including taxes on products, excluding subsidies) or at <b>basic prices</b> (what producers actually receive: market prices minus taxes on products plus subsidies), and as <b>gross</b> values (before depreciation) or <b>net</b> values (after it).</p></div>

  <h2>1 · The three measures (4.1.1 to 4.1.2)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>What it is</th><th>Calculation</th></tr>
    <tr><td><b>GDP</b></td><td>Value of all final goods and services produced <b>inside</b> the country in a year (C + I + G + X − M)</td><td>Output, income or expenditure</td></tr>
    <tr><td><b>GNI</b></td><td>Income of a country's <b>residents</b>, wherever it is earned</td><td>GDP + net primary income from abroad</td></tr>
    <tr><td><b>NNI</b></td><td>National income after allowing for the wear and tear of capital</td><td>GNI − capital consumption (depreciation)</td></tr>
  </table></div>
  <ul>
    <li><b>Primary income from abroad</b> = profits, interest, dividends and wages earned by residents overseas. <b>Net</b> primary income = income received from abroad − income paid abroad. A country with many foreign-owned firms may have <b>GNI below GDP</b>; one with many citizens working or investing overseas may have GNI above GDP.</li>
    <li><b>Capital consumption</b> is the value of capital goods worn out or made obsolete in the year; subtracting it gives a better picture of the income that can be spent without running down capital.</li>
    <li><b>Per capita</b> figures divide by population, and <b>real</b> figures adjust for inflation. They are used to compare living standards but have limits (they ignore the informal economy, unpaid work, inequality and the environment).</li>
  </ul>

  <h2>2 · Market prices, basic prices, gross and net (4.1.3 to 4.1.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Market prices</b> are what consumers pay: they include <b>taxes on products</b> (such as VAT) and exclude <b>subsidies</b>.</li>
    <li><b>Basic prices</b> are what producers receive: <b>market prices − taxes on products + subsidies on products</b>.</li>
    <li><b>Gross → net:</b> subtract capital consumption (depreciation). A <b>net</b> value is lower than the corresponding <b>gross</b> value.</li>
    <li>Example: GDP at market prices $120bn; taxes on products $15bn; subsidies $5bn. GDP at basic prices = 120 − 15 + 5 = <b>$110bn</b>.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For calculations, write the <b>steps</b>: GDP + net primary income = GNI; GNI − depreciation = NNI. Be careful with <b>signs</b>: net income from abroad can be negative.</div>
'''

watch = '''
  <h2>1 · From GDP to GNI to NNI</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stN"></div>
  <h2>2 · From market prices to basic prices</h2>
  <div id="stP"></div>
'''

explore = '''
  <h2>Lab 1 · Calculate the measures</h2>
  <p>Change the figures ($ billion) and see GNI, NNI and GDP at basic prices.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>GNI</small><strong id="r1"></strong></div><div><small>NNI</small><strong id="r2"></strong></div><div><small>GDP at basic prices</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars for GDP, GNI and NNI"></svg></div></div></div>

  <h2>Lab 2 · Why GNI differs from GDP</h2>
  <p>Choose a country type to see which way GNI differs from GDP.</p>
  <div class="card"><div class="grid2"><div><div id="cB" class="btnrow"></div>
    <div class="readout"><div><small>GDP</small><strong id="t1"></strong></div><div><small>Net income from abroad</small><strong id="t2"></strong></div><div><small>GNI</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="GDP and GNI bars for the chosen country"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which measure is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps from GDP to NNI in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A country with many foreign factories", "Overseas firms own large factories and send their profits home. GDP counts all the output made inside the country, but some income leaves, so net primary income from abroad is negative and GNI is smaller than GDP.", "GDP versus GNI and net primary income.") +
rw("A country with many overseas workers", "Millions of citizens work abroad and send wages home. Those earnings count as primary income from abroad, so GNI exceeds GDP.", "net primary income from abroad being positive.") +
rw("Replacing worn-out machines", "A firm spends $10m a year replacing machinery that wears out. National income after allowing for this wear and tear is lower than the gross figure, which is why NNI is lower than GNI.", "capital consumption.") +
rw("Sales tax and basic prices", "A $100 product includes $15 of sales tax, so the producer receives $85 (before any subsidy). GDP at market prices counts $100, while GDP at basic prices counts the amount producers actually receive.", "market prices versus basic prices.")
)

mc_exam = [
  mcq("m23_12", 16, "The table shows selected information from a country's national accounts ($ billion): GDP 28, net property income from abroad −3, capital consumption 6, national debt 2. What is the country's net national income?", ["$19 billion", "$25 billion", "$31 billion", "$33 billion"], 0, "GNI = 28 − 3 = 25. NNI = 25 − 6 = 19. National debt is not part of the calculation."),
  mcq("s23_13", 21, "The table gives details of national income statistics ($bn): consumption 2000, investment 500, government expenditure 600, net exports −100, net foreign factor income −200, depreciation 100. What is the net national income for this economy?", ["$2,700bn", "$2,800bn", "$2,900bn", "$3,000bn"], 0, "GDP = 2000 + 500 + 600 − 100 = 3000. GNI = 3000 − 200 = 2800. NNI = 2800 − 100 = 2700."),
  mcq("s24_11", 16, "A country's net national income (NNI) is less than its gross national income (GNI). What does this mean?", ["incomes earned overseas were less than incomes sent overseas", "inflation has been accounted for in NNI but not in GNI", "the country's exports decreased", "there has been a net depreciation in the value of the country's fixed capital assets"], 3, "NNI is GNI minus capital consumption, so NNI is lower when capital has depreciated."),
  mcq("s24_12", 19, "Which factor explains the difference between GDP and GNI?", ["foreign investment in the domestic automobile industry", "revenues received from exporting capital goods", "revenues received from exporting consumer goods", "salaries remitted by those working abroad to their home accounts"], 3, "GNI adds net primary income from abroad, such as wages sent home by residents working overseas. Exports are already in GDP."),
  mcq("m25_12", 19, "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head?", ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], 3, "Income per head = 1.10 ÷ 0.90 = 1.222, a rise of about 22%, which is more than 20%.")
]

exam = exam_page("national income statistics",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). These measures appear almost only in Paper 1, as numerical questions on GDP, GNI and NNI and on real and per capita figures, so this page has five Paper 1 questions. The calculations are drilled in the Practise tab.",
  [("Multiple choice (Paper 1)", "5 shown below", "2023 to 2025")],
  [],
  )

tips = tips_html(
  [("GDP is inside the borders.", "Whoever owns the firms."),
   ("GNI adds net primary income.", "Income from abroad less income paid abroad. It may be negative."),
   ("NNI subtracts depreciation.", "Capital consumption: the wear and tear of capital."),
   ("Write the steps.", "GDP, then GNI, then NNI. Mark the signs."),
   ("Market to basic prices.", "Subtract taxes on products, add subsidies."),
   ("Gross is bigger than net.", "Net means after depreciation."),
   ("Know the limits.", "Informal output, inequality and the environment are missed.")],
  [("GDP", "GDP is the value of output produced within a country in a year."),
   ("GNI", "GNI adds net primary income from abroad to GDP."),
   ("NNI", "NNI is GNI less capital consumption."),
   ("Basic prices", "Basic prices exclude taxes on products and include subsidies."),
   ("Per capita", "National income per head is national income divided by population.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- waterfall ---------- */
function wfDraw(items, s) {
  // items: [label, value, kind] kind: "t" total, "d" delta; s.k = number of items visible
  const max = Math.max(...items.map((it) => it[3] || 0)) * 1.15, Y = (v) => 250 - (v / max) * 190, w = 600 / items.length; let o = SV.line(50, 250, 740, 250);
  items.forEach((it, i) => {
    const [lab, val, kind, top, bot] = it, x = 70 + i * (w + 8), v = Math.max(0, Math.min(1, s.k - i));
    if (v <= 0) return;
    o += SV.rect(x, Y(top), w - 20, Math.max(2, Y(bot) - Y(top)), kind === "t" ? "f1" : val < 0 ? "f3" : "f2", op(0.65 * v)) + SV.text(x + (w - 20) / 2, Y(top) - 8, (kind === "d" && val > 0 ? "+" : "") + Lib.fmtN(val, 0), "lbl bd", { "text-anchor": "middle", ...op(v) }) + SV.text(x + (w - 20) / 2, 270, lab, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return o;
}
const A = { gdp: 100, net: -5, dep: 10 };
const itemsA = [["GDP", 100, "t", 100, 0], ["Net income from abroad", -5, "d", 100, 95], ["GNI", 95, "t", 95, 0], ["Capital consumption", -10, "d", 95, 85], ["NNI", 85, "t", 85, 0]];
function nDraw(s) { return wfDraw(itemsA, s); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP of 100, minus net income paid abroad of 5, gives GNI of 95, minus capital consumption of 10 gives NNI of 85">${nDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stN"), { w: 760, h: 290, label: "GDP to GNI to NNI", base: { k: 0 }, draw: nDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>GDP</b> counts all final output produced inside the country: $100bn here.", s: { k: 1 } },
  { cap: "<b>Net primary income from abroad.</b> Residents earn $15bn overseas but foreign owners take $20bn out, a net <b>−$5bn</b>.", s: { k: 2 } },
  { cap: "<b>GNI = GDP + net primary income from abroad = $95bn.</b> This is the income of residents.", s: { k: 3 } },
  { cap: "<b>Capital consumption</b> of $10bn (wear and tear of machinery) is subtracted.", s: { k: 4 } },
  { cap: "<b>NNI = GNI − capital consumption = $85bn.</b> A net figure is always below the gross one.", s: { k: 5 } },
] });
const itemsB = [["GDP at market prices", 120, "t", 120, 0], ["Taxes on products", -15, "d", 120, 105], ["Subsidies on products", 5, "d", 110, 105], ["GDP at basic prices", 110, "t", 110, 0]];
function bDraw(s) { return wfDraw(itemsB, s); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP at market prices of 120, less taxes on products of 15, plus subsidies of 5, gives GDP at basic prices of 110">${bDraw({ k: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 290, label: "GDP from market prices to basic prices", base: { k: 0 }, draw: bDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Market prices</b> are what buyers pay, including sales taxes: $120bn.", s: { k: 1 } },
  { cap: "<b>Subtract taxes on products</b> ($15bn). Producers do not receive this money.", s: { k: 2 } },
  { cap: "<b>Add subsidies on products</b> ($5bn). Producers do receive this money.", s: { k: 3 } },
  { cap: "<b>GDP at basic prices = 120 − 15 + 5 = $110bn</b>, the amount producers actually receive.", s: { k: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labN() {
  if (!["gd", "nt", "dp", "tx", "sb"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, net = +$("#nt").value, dep = +$("#dp").value, tx = +$("#tx").value, sb = +$("#sb").value, gni = gdp + net, nni = gni - dep, basic = gdp - tx + sb;
  $("#r1").textContent = "$" + gni + "bn"; $("#r2").textContent = "$" + nni + "bn"; $("#r3").textContent = "$" + basic + "bn";
  $("#rv").textContent = `GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}. NNI = ${gni} − ${dep} = ${nni}. GDP at basic prices = ${gdp} − ${tx} + ${sb} = ${basic}. ${net < 0 ? "Net primary income from abroad is negative, so GNI is below GDP." : net > 0 ? "Net primary income from abroad is positive, so GNI is above GDP." : "There is no net income from abroad, so GNI equals GDP."}`;
  const Y = (v) => 250 - v * 1.5, bars = [["GDP", gdp, "f1"], ["GNI", gni, "f2"], ["NNI", nni, "f3"], ["Basic", basic, "f1"]]; let o = SV.line(40, 250, 400, 250);
  bars.forEach(([l, v, c], i) => (o += SV.rect(60 + i * 85, Y(v), 60, 250 - Y(v), c, op(0.65)) + SV.text(90 + i * 85, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 85, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP at market prices, $bn ", min: 80, max: 160, step: 5, value: 120, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "nt", label: "Net primary income from abroad, $bn ", min: -20, max: 20, step: 1, value: -5, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "dp", label: "Capital consumption (depreciation), $bn ", min: 0, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labN });
Lib.slider($("#g4"), { id: "tx", label: "Taxes on products, $bn ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: labN });
Lib.slider($("#g5"), { id: "sb", label: "Subsidies on products, $bn ", min: 0, max: 20, step: 1, value: 5, fmt: (v) => v, onInput: labN });
labN();

/* ---------- Lab 2 ---------- */
const CTY = [["Host to foreign firms", 100, -12, "Foreign-owned factories send profits home, so more income leaves than arrives."], ["Many citizens working abroad", 100, 10, "Remittances and overseas earnings flow in, so GNI is above GDP."], ["Balanced flows", 100, 0, "Income received from abroad matches income paid abroad."]];
function showCty(i) {
  const [n, gdp, net, why] = CTY[i], gni = gdp + net; $$("#cB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = "$" + gdp + "bn"; $("#t2").textContent = (net > 0 ? "+" : "") + net; $("#t3").textContent = "$" + gni + "bn";
  $("#tv").textContent = `${n}: ${why} GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}.`;
  const Y = (v) => 170 - v * 1.2; $("#labB").innerHTML = SV.line(40, 170, 400, 170) + SV.rect(100, Y(gdp), 80, 170 - Y(gdp), "f1", op(0.65)) + SV.rect(240, Y(gni), 80, 170 - Y(gni), "f2", op(0.65)) + SV.text(140, 190, "GDP", "sm", { "text-anchor": "middle" }) + SV.text(280, 190, "GNI", "sm", { "text-anchor": "middle" }) + SV.text(140, Y(gdp) - 6, gdp, "lbl bd", { "text-anchor": "middle" }) + SV.text(280, Y(gni) - 6, gni, "lbl bd", { "text-anchor": "middle" });
}
$("#cB").innerHTML = CTY.map((c, i) => `<button class="b" data-i="${i}">${c[0]}</button>`).join("");
$$("#cB button").forEach((b) => (b.onclick = () => showCty(+b.dataset.i)));
showCty(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which measure is it?", ["GDP", "GNI", "NNI"],
  [("Output produced inside the country's borders", 0), ("Income of a country's residents wherever earned", 1), ("GNI less capital consumption", 2), ("GDP plus net primary income from abroad", 1), ("Includes output of foreign-owned firms located here", 0), ("The measure adjusted for depreciation of capital", 2), ("Wages sent home by citizens working overseas are added", 1), ("C + I + G + (X − M)", 0)],
  "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation.") + MATCH([
  ["GDP", "Value of output produced within a country in a year"],
  ["GNI", "GDP plus net primary income from abroad"],
  ["NNI", "GNI minus capital consumption"],
  ["Basic prices", "Market prices minus taxes on products plus subsidies"],
  ["Net primary income", "Income received from abroad less income paid abroad"],
  ["Capital consumption", "The value of capital worn out in a year"]]) + ORDER(
  "Put the steps from GDP to NNI in order.",
  ["Start with GDP", "Add net primary income from abroad", "This gives GNI", "Subtract capital consumption", "This gives NNI"],
  "GDP + net income from abroad = GNI; GNI − depreciation = NNI.") + CALC([
  {"q": "GDP is $500bn, net primary income from abroad is −$30bn. What is GNI ($bn)?", "a": 470, "unit": "$bn", "tol": 0.5, "hint": "500 − 30.", "sol": "<b>$470bn</b>."},
  {"q": "Capital consumption is $45bn. What is NNI ($bn)?", "a": 425, "unit": "$bn", "tol": 0.5, "hint": "470 − 45.", "sol": "<b>$425bn</b>."},
  {"q": "GDP at market prices is $200bn, taxes on products $25bn and subsidies $10bn. What is GDP at basic prices ($bn)?", "a": 185, "unit": "$bn", "tol": 0.5, "hint": "200 − 25 + 10.", "sol": "<b>$185bn</b>."},
  {"q": "National income is $900bn and population is 30 million. What is national income per head ($)?", "a": 30000, "unit": "$", "tol": 50, "hint": "900,000m ÷ 30m.", "sol": "<b>$30,000</b>."}]) + MCQ([
  ("GNI equals:", ["GDP plus net primary income from abroad", "GDP minus depreciation", "GDP plus taxes", "Exports minus imports"], 0, "Income of residents."),
  ("NNI is calculated by:", ["Subtracting capital consumption from GNI", "Adding subsidies to GDP", "Adding net exports", "Subtracting taxes from GNI"], 0, "Net of depreciation."),
  ("GDP at basic prices is found by:", ["Subtracting taxes on products and adding subsidies", "Adding taxes on products", "Subtracting depreciation", "Adding net income from abroad"], 0, "What producers receive."),
  ("A country whose firms are mostly foreign-owned is likely to have:", ["GNI below GDP", "GNI above GDP", "NNI above GNI", "GDP of zero"], 0, "Profits flow out."),
  ("Which is a stock rather than a flow?", ["Capital goods", "GDP", "NNI", "Consumption"], 0, "Output measures are flows; capital is a stock that depreciates.")
], "qz1") + CARDS([
  ("GDP", "Output inside the borders."),
  ("GNI", "GDP + net primary income."),
  ("NNI", "GNI − depreciation."),
  ("Net primary income", "Received − paid abroad."),
  ("Market prices", "Include product taxes."),
  ("Basic prices", "Market − taxes + subsidies."),
  ("Gross", "Before depreciation."),
  ("Net", "After depreciation.")]) + MCQ(mc_exam)

build("as41", "as-national-income-statistics", "National Income Statistics: GDP, GNI and NNI", EY,
  "4.1.1 to 4.1.4: national income, GDP, GNI and NNI, adjusting from market prices to basic prices and from gross to net values. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
