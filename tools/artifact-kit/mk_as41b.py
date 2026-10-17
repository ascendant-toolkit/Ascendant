"""AS syllabus 4.1.2 GNI and NNI. Run: python3 tools/artifact-kit/mk_as41b.py"""
from as6k import *
EY = EYAS("4.1.2")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p><b class="kw">Gross National Income (GNI)</b> is the income earned by a country's <b>residents</b>, wherever in the world it is earned: <b>GNI = GDP + net primary income from abroad</b>. <b class="kw">Primary income</b> is income from <b>factors of production</b>: wages of residents working abroad, and profits, interest and dividends from investments overseas; <b>net</b> primary income is what residents receive from abroad minus what is paid to foreign owners and workers at home. GNI is above GDP if a country receives more than it pays, and below GDP if foreign-owned firms send large profits home. <b class="kw">Net National Income (NNI)</b> is <b>GNI minus capital consumption (depreciation)</b>, the value of capital worn out in producing the output. NNI is therefore the income that could be consumed in a year without reducing the economy's capacity to produce.</p></div>

  <h2>1 · From GDP to GNI</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>GDP</b> measures output <b>produced inside</b> the country (including by foreign-owned firms). <b>GNI</b> measures the income of the country's <b>residents</b> (including from abroad).</li>
    <li><b>Primary income received from abroad</b> includes: wages of citizens working temporarily overseas, profits and dividends from firms owned overseas, and interest on foreign investments.</li>
    <li><b>Primary income paid abroad</b> includes: profits sent home by foreign-owned firms, interest paid on foreign loans, and wages paid to foreign workers.</li>
    <li><b>Net primary income from abroad</b> = income received − income paid. It can be positive or negative.</li>
    <li><b>Secondary income</b> (transfers such as aid and remittances sent as gifts) is a different part of the balance of payments and is not part of GNI as defined here.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Net primary income</th><th>GNI compared with GDP</th><th>Typical country</th></tr>
    <tr><td>Positive</td><td>GNI above GDP</td><td>Many citizens working or investing abroad; the country owns assets overseas</td></tr>
    <tr><td>Negative</td><td>GNI below GDP</td><td>Much of industry is foreign-owned; large foreign debts</td></tr>
    <tr><td>Zero</td><td>GNI equals GDP</td><td>Income flows in and out are balanced</td></tr>
  </table></div>

  <h2>2 · From GNI to NNI</h2>
  <ul>
    <li><b>Capital consumption</b> (depreciation) is the value of capital goods worn out, damaged or made obsolete during the year.</li>
    <li><b>NNI = GNI − capital consumption.</b> It is the more accurate measure of income that can be spent without reducing the capital stock.</li>
    <li>A <b>gross</b> figure counts all output, including that needed to replace worn-out capital. A <b>net</b> figure deducts it.</li>
    <li>Because depreciation is hard to measure accurately, GDP and GNI are used more often in practice.</li>
  </ul>

  <h2>3 · Why the difference matters</h2>
  <ul>
    <li><b>Living standards:</b> GNI (per head) shows the income actually available to residents, so it may be a better guide than GDP in countries with large foreign ownership or large overseas earnings.</li>
    <li><b>Sustainability:</b> NNI shows whether output is being used to replace capital. If capital consumption is high, a lot of production is only maintaining the existing capital stock.</li>
    <li><b>Limits:</b> primary income data can be unreliable; none of the measures covers inequality, the informal economy or the environment.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Write the <b>steps</b>: GDP + net primary income from abroad = GNI; GNI − capital consumption = NNI. Watch the <b>sign</b> of net income (it can be negative), and ignore items such as national debt, which are not in the calculation.</div>
'''

watch = '''
  <h2>1 · From GDP to GNI to NNI</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stN"></div>
  <h2>2 · Why GNI can differ from GDP</h2>
  <div id="stF"></div>
'''

explore = '''
  <h2>Lab 1 · Calculate GNI and NNI</h2>
  <p>Change the figures ($ billion) and see GNI and NNI.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Net primary income</small><strong id="r1"></strong></div><div><small>GNI</small><strong id="r2"></strong></div><div><small>NNI</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars for GDP, GNI and NNI"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Why GNI differs from GDP", "Choose a country type to see which way GNI differs from GDP.", ["Net income from abroad", "GNI compared with GDP", "Why"])

practise = '''
  <h2>1 · Which measure is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Primary income received or paid abroad?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps from GDP to NNI in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A country with many foreign factories", "Overseas firms own large factories and send their profits home. GDP counts all the output made inside the country, but some income leaves, so net primary income from abroad is negative and GNI is smaller than GDP.", "GDP versus GNI and net primary income.") +
rw("A country with many overseas workers", "Many citizens work abroad and send wages home. Those earnings count as primary income from abroad, so GNI exceeds GDP.", "net primary income from abroad being positive.") +
rw("A country that has invested overseas", "A country whose firms and investors own assets abroad receives profits, interest and dividends, which raise GNI above GDP.", "primary income from investment abroad.") +
rw("Replacing worn-out machines", "A firm spends $10m a year replacing machinery that wears out. National income after allowing for this wear and tear is lower than the gross figure, which is why NNI is lower than GNI.", "capital consumption.")
)

mc_exam = [
  mcq("m23_12", 16, "The table shows selected information from a country's national accounts ($ billion): GDP 28, net property income from abroad −3, capital consumption 6, national debt 2. What is the country's net national income?", ["$19 billion", "$25 billion", "$31 billion", "$33 billion"], 0, "GNI = 28 − 3 = 25. NNI = 25 − 6 = 19. National debt is not part of the calculation."),
  mcq("s23_13", 21, "The table gives details of national income statistics ($bn): consumption 2000, investment 500, government expenditure 600, net exports −100, net foreign factor income −200, depreciation 100. What is the net national income for this economy?", ["$2,700bn", "$2,800bn", "$2,900bn", "$3,000bn"], 0, "GDP = 2000 + 500 + 600 − 100 = 3000. GNI = 3000 − 200 = 2800. NNI = 2800 − 100 = 2700."),
  mcq("s24_12", 19, "Which factor explains the difference between GDP and GNI?", ["foreign investment in the domestic automobile industry", "revenues received from exporting capital goods", "revenues received from exporting consumer goods", "salaries remitted by those working abroad to their home accounts"], 3, "GNI adds net primary income from abroad, such as wages sent home by residents working overseas. Exports are already in GDP.")
]

exam = exam_page("GNI and NNI",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). GNI and NNI are tested almost entirely in Paper 1, as short calculations and as questions on what separates GDP from GNI. Three Paper 1 multiple choice questions are shown below; the Practise tab drills the calculations.",
  [("Multiple choice (Paper 1)", "3 shown below", "2023 to 2024")],
  [],
  )

tips = tips_html(
  [("GNI is about residents.", "Where the income is earned does not matter."),
   ("Net primary income.", "Received from abroad minus paid abroad; may be negative."),
   ("NNI subtracts depreciation.", "Capital consumption."),
   ("Write the steps.", "GDP, then GNI, then NNI."),
   ("Ignore irrelevant items.", "National debt is not in the calculation."),
   ("Say what it shows.", "NNI: income that can be spent without running down capital."),
   ("Compare with GDP.", "Foreign ownership lowers GNI; overseas earnings raise it.")],
  [("GNI", "GNI is GDP plus net primary income from abroad."),
   ("Primary income", "Primary income is income from factors of production, such as wages, profits and interest."),
   ("NNI", "NNI is GNI less capital consumption."),
   ("Capital consumption", "Capital consumption is the value of capital worn out in a year."),
   ("Gross and net", "A net value is after depreciation; a gross value is before it.")],
  [CW["define"], CW["explain"], CW["calculate"] if "calculate" in CW else CW["explain"], CW["assess"]]) + FC

js = WFJS + CHAINJS + '''
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
chainStep("#stF", "Why GNI can differ from GDP", ["Foreign-owned factories produce output inside the country", "Their output counts in GDP (inside the borders)", "Profits are sent to owners abroad (primary income paid abroad)", "Residents' income is lower than the output produced here", "GNI is below GDP"], [
  "<b>Foreign ownership</b> of firms located in the country.", "<b>GDP</b> counts the output wherever the owner lives.", "<b>The profits</b> leave the country.", "<b>Residents</b> receive less than the output value.", "<b>The reverse</b> happens when residents earn income abroad."]);

function labN() {
  if (!["gd", "rc", "pd", "dp"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, rc = +$("#rc").value, pd = +$("#pd").value, dep = +$("#dp").value, net = rc - pd, gni = gdp + net, nni = gni - dep;
  $("#r1").textContent = (net >= 0 ? "+" : "−") + "$" + Math.abs(net) + "bn"; $("#r2").textContent = "$" + gni + "bn"; $("#r3").textContent = "$" + nni + "bn";
  $("#rv").textContent = `Net primary income = ${rc} − ${pd} = ${net}. GNI = ${gdp} ${net >= 0 ? "+" : "−"} ${Math.abs(net)} = ${gni}. NNI = ${gni} − ${dep} = ${nni}. ${net < 0 ? "More income is paid abroad than received, so GNI is below GDP." : net > 0 ? "More income is received from abroad than paid, so GNI is above GDP." : "Income flows balance, so GNI equals GDP."}`;
  const Y = (v) => 250 - v * 1.5; let o = SV.line(40, 250, 400, 250);
  [["GDP", gdp, "f1"], ["GNI", gni, "f2"], ["NNI", nni, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "rc", label: "Primary income received from abroad, $bn ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "pd", label: "Primary income paid abroad, $bn ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: labN });
Lib.slider($("#g4"), { id: "dp", label: "Capital consumption, $bn ", min: 0, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labN });
labN();

chooser("h", [
  ["Host to foreign firms", "Negative", "GNI below GDP", "Foreign-owned factories send profits home", 4],
  ["Many citizens working abroad", "Positive", "GNI above GDP", "Wages and remittances flow in", 4],
  ["Large overseas investments", "Positive", "GNI above GDP", "Profits, interest and dividends flow in", 5],
  ["Heavy foreign borrowing", "Negative", "GNI below GDP", "Interest payments flow out", 3],
  ["Balanced flows", "About zero", "GNI equals GDP", "Income received matches income paid", 1]
], (it) => `${it[0]}: net primary income is ${it[1].toLowerCase()}, so ${it[2].toLowerCase()}. Reason: ${it[3].toLowerCase()}.`, "Size of the gap between GNI and GDP");
''' + CLASSIFY("cl1", "Which measure is it?", ["GDP", "GNI", "NNI"],
  [("Output produced inside the country's borders", 0), ("Income of a country's residents wherever earned", 1), ("GNI less capital consumption", 2), ("GDP plus net primary income from abroad", 1), ("Includes output of foreign-owned firms located here", 0), ("The measure adjusted for depreciation of capital", 2), ("Wages sent home by citizens working overseas are added", 1), ("C + I + G + (X − M)", 0)],
  "GDP: inside the borders. GNI: residents' income. NNI: GNI minus depreciation.") + CLASSIFY("cl2", "Is it primary income received from abroad or paid abroad?", ["Received from abroad", "Paid abroad"],
  [("Dividends from shares a resident owns in a foreign firm", 0), ("Profits sent home by a foreign-owned factory", 1), ("Wages earned by a resident working overseas", 0), ("Interest paid on a loan from a foreign bank", 1), ("Wages paid to a foreign worker in the country", 1), ("Interest on foreign bonds owned by a resident", 0)],
  "Received: earned by residents abroad. Paid: earned by foreign owners and workers here.") + ORDER(
  "Put the steps from GDP to NNI in order.",
  ["Start with GDP", "Add primary income received from abroad", "Subtract primary income paid abroad", "This gives GNI", "Subtract capital consumption to get NNI"],
  "GDP + net primary income = GNI; GNI − depreciation = NNI.") + MATCH([
  ["GNI", "GDP plus net primary income from abroad"],
  ["NNI", "GNI minus capital consumption"],
  ["Primary income", "Income from factors of production such as wages, profit and interest"],
  ["Net primary income", "Income received from abroad less income paid abroad"],
  ["Capital consumption", "The value of capital worn out in a year"],
  ["Gross", "Before deducting depreciation"]]) + CALC([
  {"q": "GDP is $500bn, income received from abroad is $40bn and income paid abroad is $70bn. What is GNI ($bn)?", "a": 470, "unit": "$bn", "tol": 0.5, "hint": "500 + 40 − 70.", "sol": "<b>$470bn</b>."},
  {"q": "Capital consumption is $45bn. What is NNI ($bn)?", "a": 425, "unit": "$bn", "tol": 0.5, "hint": "470 − 45.", "sol": "<b>$425bn</b>."},
  {"q": "GDP is $30bn, net primary income from abroad −$3bn and capital consumption $6bn. What is NNI ($bn)?", "a": 21, "unit": "$bn", "tol": 0.5, "hint": "30 − 3 − 6.", "sol": "<b>$21bn</b>."},
  {"q": "GNI is $800bn and population is 20 million. What is GNI per head ($)?", "a": 40000, "unit": "$", "tol": 50, "hint": "800,000m ÷ 20m.", "sol": "<b>$40,000</b>."}]) + MCQ([
  ("GNI equals:", ["GDP plus net primary income from abroad", "GDP minus depreciation", "GDP plus taxes", "Exports minus imports"], 0, "Income of residents."),
  ("NNI is calculated by:", ["Subtracting capital consumption from GNI", "Adding subsidies to GDP", "Adding net exports", "Subtracting taxes from GNI"], 0, "Net of depreciation."),
  ("A country with mostly foreign-owned firms is likely to have:", ["GNI below GDP", "GNI above GDP", "NNI above GNI", "GDP of zero"], 0, "Profits flow out."),
  ("Wages sent home by citizens working abroad:", ["Raise GNI", "Lower GDP", "Are not income", "Raise depreciation"], 0, "Primary income from abroad."),
  ("Which is not needed to calculate NNI?", ["National debt", "GDP", "Net primary income", "Capital consumption"], 0, "Debt is not part of the calculation.")
], "qz1") + CARDS([
  ("GNI", "GDP + net primary income."),
  ("NNI", "GNI − depreciation."),
  ("Primary income", "Wages, profit, interest."),
  ("Net primary income", "Received − paid abroad."),
  ("Capital consumption", "Wear and tear of capital."),
  ("Foreign ownership", "GNI below GDP."),
  ("Overseas earnings", "GNI above GDP."),
  ("NNI use", "Sustainable income.")]) + MCQ(mc_exam)

build("as41b", "as-gni-and-nni", "Gross National Income and Net National Income", EY,
  "4.1.2: how GDP becomes GNI through net primary income from abroad and NNI through capital consumption. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
