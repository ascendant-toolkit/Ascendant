"""Builds the four IGCSE Economics 6.4 Current account of the balance of payments reviews (6.4.1 to 6.4.4), written from scratch.
Run: python3 tools/artifact-kit/mk_ig64.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

WF = '''
function wfChart(s) {
  const items = s.items, base0 = 190, k = s.k || 3.2; let o = SV.line(40, base0, 720, base0) + SV.text(40, 26, "$bn", "sm");
  let cum = 0; const w = 100, gap = 30;
  items.forEach(([n, v, c], i) => {
    const op = clamp(s.n - i, 0, 1); const x = 60 + i * (w + gap);
    if (op > 0) { const y0 = base0 - cum * k, y1 = base0 - (cum + v) * k, top = Math.min(y0, y1), h = Math.abs(y1 - y0); o += `<g opacity="${op}">` + SV.rect(x, top, w, Math.max(h, 2), "", { style: `fill:var(${v >= 0 ? "--good" : "--bad"})`, opacity: 0.85 }) + SV.text(x + w / 2, v >= 0 ? top - 8 : top + h + 16, (v >= 0 ? "+" : "−") + Math.abs(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, 330, n, "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; }
    cum += v;
  });
  const tot = items.reduce((a, b) => a + b[1], 0), x = 60 + items.length * (w + gap), op = clamp(s.n - items.length, 0, 1);
  if (op > 0) { const y1 = base0 - tot * k, top = Math.min(base0, y1), h = Math.abs(y1 - base0); o += `<g opacity="${op}">` + SV.rect(x, top, w, Math.max(h, 2), "", { style: `fill:var(${tot >= 0 ? "--accent" : "--warn"})`, opacity: 0.9 }) + SV.text(x + w / 2, tot >= 0 ? top - 8 : top + h + 16, (tot >= 0 ? "+" : "−") + Math.abs(tot), "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + w / 2, 330, "Current account", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + w / 2, 346, tot >= 0 ? "SURPLUS" : "DEFICIT", "lbl bd " + (tot >= 0 ? "t3" : "t2"), { "text-anchor": "middle", style: "font-size:13px" }) + "</g>"; }
  return o;
}
'''

# =========================================================== 6.4.1 Structure
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">current account</span> of the balance of payments records a country's <b>trade in goods, trade in services, primary income and secondary income</b> with the rest of the world over a year. It shows money flowing <b>in</b> (receipts) and <b>out</b> (payments). If receipts are greater than payments there is a <b>surplus</b>; if payments are greater there is a <b>deficit</b>. Each component has its own balance, and the four balances add up to the current account balance.</p></div>

  <h2>The four components</h2>
  <div class="tw"><table class="t">
    <tr><th>Component</th><th>What it records</th><th>Examples</th></tr>
    <tr><td><b>Trade in goods</b> (visible trade)</td><td>Exports of goods minus imports of goods</td><td>Cars, oil, machinery, food</td></tr>
    <tr><td><b>Trade in services</b> (invisible trade)</td><td>Exports of services minus imports of services</td><td>Tourism, banking, insurance, education, shipping</td></tr>
    <tr><td><b>Primary income</b></td><td>Income earned from abroad minus income paid abroad: wages, profits, interest and dividends from owning assets or working abroad</td><td>Profits sent home by a country's firms abroad; dividends paid to foreign shareholders; interest on foreign loans</td></tr>
    <tr><td><b>Secondary income</b></td><td>Transfers with no good or service in return: money sent or received by governments and individuals</td><td>Workers' remittances, foreign aid, government contributions to international bodies</td></tr>
  </table></div>

  <h2>Calculating balances</h2>
  <div class="formula">Trade in goods balance = exports of goods − imports of goods<br>Current account balance = goods balance + services balance + primary income balance + secondary income balance</div>
  <p>A <b>positive</b> answer is a <b>surplus</b>; a <b>negative</b> answer is a <b>deficit</b>. A <b>trade in goods deficit</b> is when expenditure on imports of goods exceeds revenue from exports of goods.</p>
  <div class="tw"><table class="t">
    <tr><th>Item ($bn)</th><th>Receipts (in)</th><th>Payments (out)</th><th>Balance</th></tr>
    <tr><td>Trade in goods</td><td>200</td><td>230</td><td><b>−30</b></td></tr>
    <tr><td>Trade in services</td><td>90</td><td>65</td><td><b>+25</b></td></tr>
    <tr><td>Primary income</td><td>20</td><td>28</td><td><b>−8</b></td></tr>
    <tr><td>Secondary income</td><td>12</td><td>9</td><td><b>+3</b></td></tr>
    <tr><td><b>Current account</b></td><td></td><td></td><td><b>−10</b> (deficit)</td></tr>
  </table></div>

  <h2>Where the current account fits</h2>
  <p>The <b>balance of payments</b> also includes the capital and financial accounts (investment flows, loans and changes in reserves). If there is a deficit on the current account, it must be <b>financed</b> by a surplus on the financial account (borrowing from abroad, selling assets, or using reserves). The current account is the part you are asked about in IGCSE.</p>
  <p class="note">Services are a large share of exports for many rich countries (for example banking and tourism), so a country can have a deficit in goods but a surplus in services.</p>
'''
js = HEAD + COMMON + WF + '''
const ITEMS = [["Goods", -30, ""], ["Services", 25, ""], ["Primary income", -8, ""], ["Secondary income", 3, ""]];
Lib.stepper($("#stW"), { w: 760, h: 360, label: "Building the current account", base: { items: ITEMS, n: 0, k: 3.2 }, draw: wfChart, steps: [
  { cap: "<b>Trade in goods:</b> the country exports $200bn and imports $230bn of goods: a <b>deficit of $30bn</b>.", s: { items: ITEMS, n: 1, k: 3.2 } },
  { cap: "<b>Trade in services:</b> exports of $90bn and imports of $65bn: a <b>surplus of $25bn</b>, which offsets most of the goods deficit.", s: { items: ITEMS, n: 2, k: 3.2 } },
  { cap: "<b>Primary income:</b> $20bn comes in from investments and work abroad but $28bn goes out as profits and interest to foreigners: a <b>deficit of $8bn</b>.", s: { items: ITEMS, n: 3, k: 3.2 } },
  { cap: "<b>Secondary income:</b> transfers such as remittances and aid net +$3bn.", s: { items: ITEMS, n: 4, k: 3.2 } },
  { cap: "<b>Current account balance</b> = −30 + 25 − 8 + 3 = <b>−$10bn</b>: a <b>deficit</b>. It has to be financed by borrowing or selling assets.", s: { items: ITEMS, n: 5, k: 3.2 } },
] });
function trChart(s) {
  const base = 300, k = 1.1; let o = SV.line(60, base, 710, base) + SV.text(60, 26, "Value of goods and services traded ($bn)", "sm");
  [["Goods exports", 200, "--good"], ["Goods imports", 230, "--bad"], ["Services exports", 90, "--good"], ["Services imports", 65, "--bad"]].forEach(([n, v, c], i) => { const op = clamp(s.n - i * 0.5, 0, 1); if (op <= 0) return; const x = 90 + i * 150, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 110, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 55, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 55, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:12px" }) + "</g>"; });
  if (s.n >= 2) o += SV.text(370, 70, "Goods: " + (200 - 230) + "  ·  Services: +" + (90 - 65), "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 350, label: "Goods and services", base: { n: 0 }, draw: trChart, steps: [
  { cap: "<b>Goods</b> are physical items. Exports of $200bn are less than imports of $230bn.", s: { n: 1 } },
  { cap: "<b>Services</b> are things like tourism and banking. Exports of $90bn exceed imports of $65bn.", s: { n: 4 } },
  { cap: "A country can run a <b>deficit in goods</b> and a <b>surplus in services</b> at the same time. Always calculate each balance separately.", s: { n: 4 } },
] });

/* Lab 1 */
function labC() {
  const ids = ["xa", "xb", "xc", "xd", "xe", "xf", "xg", "xh"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), gb = v[0] - v[1], sb = v[2] - v[3], pb = v[4] - v[5], sc = v[6] - v[7], ca = gb + sb + pb + sc;
  $("#xa1").textContent = (gb >= 0 ? "+" : "−") + Math.abs(gb); $("#xa2").textContent = (sb >= 0 ? "+" : "−") + Math.abs(sb); $("#xa3").textContent = (pb + sc >= 0 ? "+" : "−") + Math.abs(pb + sc); $("#xa4").textContent = (ca >= 0 ? "+" : "−") + Math.abs(ca);
  $("#xav").textContent = `Goods ${gb >= 0 ? "+" : "−"}${Math.abs(gb)}, services ${sb >= 0 ? "+" : "−"}${Math.abs(sb)}, primary income ${pb >= 0 ? "+" : "−"}${Math.abs(pb)}, secondary income ${sc >= 0 ? "+" : "−"}${Math.abs(sc)}. Current account = ${ca >= 0 ? "+" : "−"}${Math.abs(ca)}: a ${ca > 0 ? "surplus" : ca < 0 ? "deficit" : "balance"}. ${gb < 0 && sb > 0 ? "A goods deficit may be partly offset by a services surplus." : ""}`;
  $("#labC").innerHTML = wfChart({ items: [["Goods", gb, ""], ["Services", sb, ""], ["Primary income", pb, ""], ["Secondary income", sc, ""]], n: 5, k: 2 });
}
[["xa", "g1", "Exports of goods", 200], ["xb", "g2", "Imports of goods", 230], ["xc", "g3", "Exports of services", 90], ["xd", "g4", "Imports of services", 65], ["xe", "g5", "Primary income received", 20], ["xf", "g6", "Primary income paid", 28], ["xg", "g7", "Secondary income received", 12], ["xh", "g8", "Secondary income paid", 9]].forEach(([id, g, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 300, step: 5, value: v, fmt: (x) => "$" + x, onInput: labC }));
const TX = [
  { n: "A country exports cars", a: "Trade in goods", w: "Physical product sold abroad." },
  { n: "Foreign tourists stay in its hotels", a: "Trade in services (export)", w: "Tourism is a service sold to foreigners." },
  { n: "A firm pays interest on a loan from a foreign bank", a: "Primary income (payment)", w: "Interest paid to foreign owners of capital." },
  { n: "A foreign company sends profits home", a: "Primary income (payment)", w: "Profits flow out to foreign owners." },
  { n: "Migrant workers send money to families at home", a: "Secondary income (receipt)", w: "A transfer with nothing exchanged." },
  { n: "The government gives aid to another country", a: "Secondary income (payment)", w: "Transfers with no good or service in return." },
  { n: "A UK bank sells insurance to a foreign firm", a: "Trade in services (export)", w: "Financial services sold abroad." },
  { n: "A shop imports clothing", a: "Trade in goods (import)", w: "Physical goods bought from abroad." },
];
button_table("txBtns", "txOut", TX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Component</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>component of the current account</b> is each?", buckets: [{ label: "Trade in goods" }, { label: "Trade in services" }, { label: "Primary income" }, { label: "Secondary income" }], items: [
  { text: "Exports of steel", b: 0 }, { text: "Imports of smartphones", b: 0 },
  { text: "Tourism spending by visitors", b: 1 }, { text: "Insurance sold to foreign firms", b: 1 },
  { text: "Dividends paid to foreign shareholders", b: 2 }, { text: "Interest received from loans abroad", b: 2 },
  { text: "Workers' remittances", b: 3 }, { text: "Foreign aid", b: 3 },
], done: "Four components: goods, services, primary income, secondary income." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>receipt (money in)</b> or a <b>payment (money out)</b> for the UK current account?", buckets: [{ label: "Receipt (in)" }, { label: "Payment (out)" }], items: [
  { text: "A US firm buys British cars", b: 0 }, { text: "French tourists spend in London", b: 0 }, { text: "A UK firm's profits from its Indian factory", b: 0 }, { text: "A UK worker in Dubai sends money home", b: 0 },
  { text: "A UK shop buys Chinese clothing", b: 1 }, { text: "British tourists spend in Spain", b: 1 }, { text: "Profits sent by a foreign-owned UK firm to its parent abroad", b: 1 }, { text: "UK foreign aid", b: 1 },
], done: "Receipts add to the balance; payments subtract." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Current account", "Record of trade in goods and services, primary income and secondary income"],
  ["Trade in goods balance", "Exports of goods minus imports of goods"],
  ["Primary income", "Wages, profits, interest and dividends earned from and paid abroad"],
  ["Secondary income", "Transfers such as remittances and aid"],
  ["Current account deficit", "Payments to the rest of the world exceed receipts"],
  ["Current account surplus", "Receipts from the rest of the world exceed payments"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("Exports of goods are $120bn and imports of goods are $150bn. What is the trade in goods balance ($bn)?", -30, "120 − 150 = <b>−$30bn</b>: a deficit.", None, None),
    ("Goods balance −$30bn, services balance +$22bn, primary income −$6bn, secondary income +$4bn. What is the current account balance ($bn)?", -10, "−30 + 22 − 6 + 4 = <b>−$10bn</b>.", None, None),
    ("A country earns $15bn of primary income from abroad and pays $20bn abroad. What is the primary income balance ($bn)?", -5, "15 − 20 = <b>−$5bn</b>.", None, None),
    ("Exports of goods and services are $300bn and imports are $280bn. Primary and secondary income net to −$12bn. What is the current account balance ($bn)?", 8, "(300 − 280) − 12 = <b>+$8bn</b>: a surplus.", None, None),
    ("A current account deficit is $12bn and GDP is $400bn. What is the deficit as a percentage of GDP?", 3, "12 ÷ 400 × 100 = <b>3%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is a component of the current account?", ["Government spending", "Trade in goods", "Inflation", "Unemployment"], 1, "Goods, services, primary income, secondary income."),
    ("Workers' remittances are part of:", ["Trade in goods", "Trade in services", "Primary income", "Secondary income"], 3, "Transfers with no good in return."),
    ("A trade in goods deficit means:", ["Exports exceed imports of goods", "Imports of goods exceed exports of goods", "Services imports exceed exports", "No trade"], 1, "Expenditure on goods imports is greater than revenue from exports."),
    ("Profits sent abroad by foreign-owned firms are part of:", ["Trade in goods", "Secondary income", "Primary income", "Trade in services"], 2, "Income paid to foreign owners."),
    ("The current account balance is:", ["Goods + services only", "Goods + services + primary income + secondary income", "Exports + imports", "Government revenue − spending"], 1, "All four components."),
]) + "\n" + cards_js([("Current account", "The part of the balance of payments that records trade in goods and services, primary income and secondary income."), ("Trade in goods", "Exports and imports of physical goods (visible trade)."), ("Trade in services", "Exports and imports of services such as tourism and banking (invisible trade)."), ("Primary income", "Wages, profits, interest and dividends earned from and paid abroad."), ("Secondary income", "Transfers with nothing received in return, such as remittances and aid."), ("Current account deficit", "When payments to the rest of the world exceed receipts."), ("Current account surplus", "When receipts from the rest of the world exceed payments."), ("Balance of payments", "A record of all payments between a country and the rest of the world."), ("Visible trade", "Trade in goods.")]) + "labC(); \n"
explore = '''
  <h2>Lab 1 · Current account calculator</h2>
  <p>Set the receipts and payments in each component ($bn). The chart builds up the current account balance.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div><div><div id="g5"></div><div id="g6"></div><div id="g7"></div><div id="g8"></div></div></div>
    <div class="grid2"><div class="readout"><div><small>Goods balance</small><strong id="xa1"></strong></div><div><small>Services balance</small><strong id="xa2"></strong></div><div><small>Income balances</small><strong id="xa3"></strong></div><div><small>Current account</small><strong id="xa4"></strong></div></div><div class="verdict" id="xav"></div></div>
    <svg id="labC" viewBox="0 0 760 360" role="img" aria-label="Current account balance built from its components"></svg>
  </div>

  <h2>Lab 2 · Which component?</h2>
  <p>Pick a transaction to see which component of the current account it belongs to.</p>
  <div class="card"><div class="row" id="txBtns"></div><div id="txOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "State two components of the current account. (Oct/Nov 2020, P21; Oct/Nov 2022, P23; Oct/Nov 2024, P22)", "Any two from trade in goods, trade in services, primary income, secondary income.", "[K|Trade in goods.] [K|Trade in services (or primary income, secondary income).]"),
    Q(2, "Define", 2, "Define trade in goods balance. (Oct/Nov 2020, P22)", "Exports of goods minus imports of goods.", "[K|The value of exports of goods] [K|minus the value of imports of goods.]"),
    Q(3, "Define", 2, "Define a trade in goods deficit. (May/June 2024, P23)", "Expenditure on imports of goods exceeds revenue from exports of goods.", "[K|A trade in goods deficit is when expenditure on imports of goods] [K|exceeds revenue from exports of goods.]"),
    Q(4, "Calculate", 1, "Exports of goods are $120bn and imports of goods are $150bn. Calculate the trade in goods balance. (May/June 2020, P22 style)", "Exports − imports; deficit is negative.", "[A|120 − 150 = −$30bn (a deficit of $30bn).]"),
    Q(5, "Calculate", 2, "Goods balance −$30bn; services balance +$22bn; primary income −$6bn; secondary income +$4bn. Calculate the current account balance. (May/June 2024, P22 style)", "Add the four balances.", "[A|−30 + 22 − 6 + 4] [A|= −$10bn (a deficit).]"),
    Q(6, "Explain", 4, "Explain the difference between primary income and secondary income.", "Primary: earnings from work and assets abroad. Secondary: transfers with nothing in return.",
      "[K|Primary income is income earned from, and paid to, other countries from work and assets,] [A|such as profits, interest and dividends.] [K|Secondary income is transfers of money with nothing received in return,] [A|such as workers' remittances and foreign aid.]"),
)
tp = tips([
    ("Four components:", "goods, services, primary income, secondary income."),
    ("Balance = receipts − payments.", "Positive is a surplus; negative is a deficit."),
    ("Calculate each balance separately.", "Then add them for the current account."),
    ("Services are invisible trade.", "Tourism, banking, insurance."),
    ("Show working and units.", "Even for a 1-mark calculation."),
], cmds("Identify", "Define", "Calculate", "Explain"))
body = page(CL("6.4.1 Structure of the current account of the balance of payments"), "Structure of the Current Account", "The four components of the current account, how to calculate balances and what deficits and surpluses mean. Syllabus 6.4.1.",
    learn=learn, watch=watch(("Building the current account", "stW"), ("Goods and services", "stT")), explore=explore,
    practise=practise(("Which component?", "cl1", "card"), ("Receipt or payment?", "cl2", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The UK: goods deficit, services surplus", "The UK has run a large deficit in trade in goods for many years, partly offset by a surplus in services such as finance, insurance and business services.", "Calculating each balance separately."),
        rw("Remittances to the Philippines", "Workers abroad send tens of billions of dollars home each year, a large part of the Philippines' secondary income.", "Secondary income."),
        rw("Primary income from investments", "Countries with large overseas investments, such as the UK and Japan, earn substantial primary income from profits and interest.", "Primary income."),
        rw("Jordan's current account", "A past paper asks students to identify components of Jordan's current account using a table of data.", "Reading and calculating from a table.")),
    exam=ex, tips=tp)
write("bp1", body, js, "Structure of the Current Account", "ig-bop-structure")

# =========================================================== 6.4.2 Causes
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A current account <b>deficit</b> arises when a country spends more on imports and payments abroad than it earns from exports and receipts. A <b>surplus</b> is the reverse. The main causes are differences in <b>competitiveness</b> (prices, quality, productivity, exchange rate), <b>demand</b> at home and abroad (incomes, growth), the prices of key exports and imports (such as oil), and flows of income and transfers. Always link a cause to exports, imports or income flows.</p></div>

  <h2>Causes of a current account deficit</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it leads to a deficit</th></tr>
    <tr><td><b>Rising incomes and spending at home</b></td><td>People buy more goods, including imports, so imports rise faster than exports</td></tr>
    <tr><td><b>Low price and non-price competitiveness</b></td><td>Higher costs and inflation than rivals, low productivity, poor quality or limited variety make exports less attractive and imports more attractive</td></tr>
    <tr><td><b>A high exchange rate</b></td><td>Exports dearer abroad, imports cheaper</td></tr>
    <tr><td><b>Weak demand abroad</b></td><td>Recession in trading partners cuts demand for exports</td></tr>
    <tr><td><b>Falling prices of main exports</b> or <b>rising import prices</b></td><td>Export revenue falls; import bill (for example oil) rises</td></tr>
    <tr><td><b>Dependence on imports</b></td><td>Few domestic alternatives for oil, food or machinery</td></tr>
    <tr><td><b>Primary income deficits</b></td><td>Profits and interest paid abroad (to foreign firms and lenders) exceed income received</td></tr>
    <tr><td><b>Secondary income outflows</b></td><td>Aid given and remittances sent abroad exceed receipts</td></tr>
  </table></div>

  <h2>Causes of a current account surplus</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>How it leads to a surplus</th></tr>
    <tr><td><b>Strong competitiveness</b></td><td>Low costs, high productivity, advanced technology, high quality: exports strong, fewer imports</td></tr>
    <tr><td><b>A low or undervalued exchange rate</b></td><td>Exports cheap abroad, imports dear</td></tr>
    <tr><td><b>High demand abroad</b>, <b>high export prices</b></td><td>More export revenue (for example oil exporters when oil prices are high)</td></tr>
    <tr><td><b>Low domestic spending or high saving</b></td><td>Fewer imports</td></tr>
    <tr><td><b>Primary and secondary income inflows</b></td><td>Large overseas investments, remittances from workers abroad</td></tr>
    <tr><td><b>Protection</b></td><td>Tariffs and quotas reduce imports</td></tr>
  </table></div>

  <h2>Examples of specific links</h2>
  <ul>
    <li><b>Oil price and the UAE:</b> an oil exporter's export revenue rises when the oil price rises, so its current account moves towards <b>surplus</b>; when the price falls it moves towards deficit.</li>
    <li><b>Inflation and the current account:</b> higher inflation than competitors makes exports dearer, so a higher inflation rate tends to go with a worse current account.</li>
    <li><b>Technology:</b> advances that raise productivity and quality make exports more competitive and imports less necessary.</li>
    <li><b>Economic growth:</b> fast growth raises incomes and imports, which can worsen the current account (a conflict of aims).</li>
  </ul>
'''
js = HEAD + COMMON + '''
const DC = ["Incomes and spending at home rise", "Consumers and firms buy more imports", "Meanwhile exports are held back by dear prices or weak demand abroad", "Imports grow faster than exports", "The current account moves towards deficit", "Primary income outflows (profits, interest) can add to it"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Causes of a deficit", base: { n: 0 }, draw: mkChain(DC, "--bad"), steps: chainSteps(["<b>Incomes and spending</b> at home rise.", "Consumers and firms <b>buy more imports</b>.", "Meanwhile <b>exports</b> are held back by dear prices or weak demand abroad.", "<b>Imports grow faster</b> than exports.", "The current account moves towards <b>deficit</b>.", "<b>Primary income outflows</b> (profits, interest) can add to it."]) });
const SC = ["Productivity rises and costs fall; quality improves", "Exports become cheaper and more attractive abroad", "Demand for imports falls as home firms compete", "Export revenue rises and import spending falls", "The current account moves towards surplus", "Remittances and overseas investments add further income"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Causes of a surplus", base: { n: 0 }, draw: mkChain(SC, "--good"), steps: chainSteps(["<b>Productivity rises</b> and costs fall; quality improves.", "Exports become <b>cheaper and more attractive</b> abroad.", "<b>Demand for imports falls</b> as home firms compete.", "<b>Export revenue rises</b> and import spending falls.", "The current account moves towards <b>surplus</b>.", "<b>Remittances and overseas investments</b> add further income."]) });
function oilChart(s) {
  const pr = [50, 80, 110, 60, 40], ca = [4, 9, 15, 6, 1], X = (i) => 110 + i * 130; let o = SV.line(60, 320, 710, 320) + SV.text(60, 28, "An oil exporter: oil price and the current account", "sm");
  const lab = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"];
  pr.forEach((p, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = X(i) - 50, h = p * 1.6; o += `<g opacity="${op}">` + SV.rect(x, 320 - h, 44, h, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 22, 320 - h - 6, "$" + p, "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.rect(x + 50, 320 - ca[i] * 8, 44, ca[i] * 8, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 72, 320 - ca[i] * 8 - 6, "+" + ca[i] + "%", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 47, 340, lab[i], "sm", { "text-anchor": "middle" }) + "</g>"; });
  o += SV.rect(480, 40, 14, 14, "", { style: "fill:var(--warn)" }) + SV.text(500, 52, "Oil price ($ a barrel)", "sm") + SV.rect(480, 62, 14, 14, "", { style: "fill:var(--accent)" }) + SV.text(500, 74, "Current account surplus (% of GDP)", "sm");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 360, label: "Oil price and an oil exporter's current account", base: { n: 0 }, draw: oilChart, steps: [
  { cap: "An oil exporter earns most of its export revenue from oil. At <b>$50 a barrel</b> the current account has a small surplus (4% of GDP).", s: { n: 1 } },
  { cap: "The oil price rises to <b>$80</b>: export revenue rises, so the <b>surplus widens</b> to 9%.", s: { n: 2 } },
  { cap: "At <b>$110</b> the surplus is 15% of GDP.", s: { n: 3 } },
  { cap: "The price falls back to <b>$60</b> and then <b>$40</b>: export revenue falls and the surplus <b>shrinks</b> to 1%. There is a <b>positive relationship</b> between the oil price and the current account balance of an oil exporter (illustrative figures).", s: { n: 5 } },
] });

/* Lab 1: causes */
function labK() {
  if (!$("#ka") || !$("#kb") || !$("#kc")) return;
  const gy = +$("#ka").value / 100, gw = +$("#kb").value / 100, rp = +$("#kc").value / 100, X = 100 * (1 + 1.5 * gw) * (1 - 0.8 * rp), Mi = 100 * (1 + 1.4 * gy) * (1 + 0.6 * rp), bal = X - Mi;
  $("#ka1").textContent = money(X, 0); $("#ka2").textContent = money(Mi, 0); $("#ka3").textContent = (bal >= 0 ? "+" : "−") + money(Math.abs(bal), 0);
  $("#kav").textContent = `Exports ${money(X, 0)} and imports ${money(Mi, 0)}: balance ${bal >= 0 ? "+" : "−"}${money(Math.abs(bal), 0)} (a ${bal > 0.5 ? "surplus" : bal < -0.5 ? "deficit" : "balance"}). Faster home growth raises imports; stronger world demand raises exports; being less price-competitive than rivals (higher relative prices) cuts exports and raises imports.`;
  const base = 290, k = 1.8; let o = SV.line(60, base, 700, base);
  [["Exports", X, "--good"], ["Imports", Mi, "--bad"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labK").innerHTML = o + SV.text(60, 24, "Baseline: exports 100, imports 100", "sm");
}
Lib.slider($("#g1"), { id: "ka", label: "Growth in home incomes (raises imports)", min: 0, max: 15, step: 1, value: 5, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g2"), { id: "kb", label: "Growth in demand abroad (raises exports)", min: -10, max: 15, step: 1, value: 2, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g3"), { id: "kc", label: "Domestic prices relative to rivals (higher = less competitive)", min: -10, max: 20, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labK });
const CS = [
  { n: "Rising incomes at home", t: "Deficit", e: "Imports rise faster than exports." },
  { n: "Low productivity and high costs", t: "Deficit", e: "Exports uncompetitive; imports more attractive." },
  { n: "High exchange rate", t: "Deficit", e: "Exports dearer abroad, imports cheaper at home." },
  { n: "Recession in trading partners", t: "Deficit", e: "Foreign demand for exports falls." },
  { n: "High export prices (such as oil)", t: "Surplus", e: "Export revenue rises." },
  { n: "Low exchange rate", t: "Surplus", e: "Exports cheap, imports dear." },
  { n: "High saving and low home spending", t: "Surplus", e: "Fewer imports." },
  { n: "Remittances and overseas investment income", t: "Surplus", e: "Large inflows of secondary and primary income." },
];
button_table("csBtns", "csOut", CS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Tends to cause</th><th>How</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each tend to cause a current account <b>deficit</b> or a <b>surplus</b>?", buckets: [{ label: "Deficit" }, { label: "Surplus" }], items: [
  { text: "Fast rise in consumer spending on imports", b: 0 }, { text: "Costs and prices rising faster than rivals'", b: 0 }, { text: "A very high exchange rate", b: 0 }, { text: "A recession in the main trading partner", b: 0 },
  { text: "Highly competitive, high-quality exports", b: 1 }, { text: "A low exchange rate", b: 1 }, { text: "A rise in the price of the main export", b: 1 }, { text: "Large remittances from workers abroad", b: 1 },
], done: "Think: exports up or imports down gives a surplus." });
Lib.classify($("#cl2"), { prompt: "Which <b>type of cause</b> is each?", buckets: [{ label: "Competitiveness" }, { label: "Demand at home or abroad" }, { label: "Prices of exports or imports" }, { label: "Income flows" }], items: [
  { text: "Higher productivity and lower costs", b: 0 }, { text: "Better quality products", b: 0 },
  { text: "A boom at home raising imports", b: 1 }, { text: "A recession abroad cutting demand for exports", b: 1 },
  { text: "A fall in the world price of the main export", b: 2 }, { text: "A rise in the price of imported oil", b: 2 },
  { text: "Profits sent abroad by foreign firms", b: 3 }, { text: "Remittances from workers overseas", b: 3 },
], done: "Link each cause to exports, imports or income flows." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect.", pairs: [
  ["Higher home incomes", "More imports, so the deficit widens"],
  ["Higher productivity", "More competitive exports"],
  ["Higher oil price (oil exporter)", "More export revenue"],
  ["Recession abroad", "Lower demand for exports"],
  ["High exchange rate", "Exports dearer, imports cheaper"],
  ["Remittances", "Secondary income inflow"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a high exchange rate could cause a current account deficit</b>.", items: [
  "The exchange rate rises",
  "Exports become dearer for foreign buyers",
  "Imports become cheaper for domestic buyers",
  "Export sales fall and imports rise",
  "The current account moves towards deficit",
], done: "A causal chain." });
''' + calc_js([
    ("Exports are $200bn and imports $220bn. Higher incomes raise imports by 10%, with exports unchanged. What is the new balance ($bn)?", -42, "Imports = 242; 200 − 242 = <b>−$42bn</b>.", None, None),
    ("An oil exporter's oil revenue is $60bn at $60 a barrel. The price rises to $90 with the same quantity. What is the new revenue ($bn)?", 90, "60 × 90/60 = <b>$90bn</b>.", None, None),
    ("Export prices rise 5% while import prices rise 10%. What happens to the terms of trade: by roughly how many percentage points do export prices lag import prices?", 5, "10 − 5 = <b>5 percentage points</b>: the deficit may widen.", None, None),
]) + mcq_js("qz1", [
    ("Which is most likely to cause a current account deficit?", ["Higher productivity", "Rising incomes leading to more imports", "A low exchange rate", "Higher export prices"], 1, "Imports rise."),
    ("A rise in the oil price will most likely:", ["Reduce an oil exporter's surplus", "Increase an oil exporter's surplus", "Have no effect", "Reduce its exports"], 1, "More export revenue."),
    ("Higher inflation than competitors tends to:", ["Improve the current account", "Worsen the current account", "Have no effect", "Raise exports"], 1, "Exports become dearer."),
    ("Technology that raises productivity can improve the current account because:", ["Exports become more competitive", "Imports become cheaper", "Exports fall", "Spending rises"], 0, "Lower costs and better quality."),
    ("Which could cause a surplus?", ["A high exchange rate", "A recession abroad", "Remittances from workers abroad", "Higher imports"], 2, "Income inflows."),
]) + "\n" + cards_js([("Competitiveness", "How attractive a country's goods and services are in terms of price and quality compared with rivals'."), ("Terms of trade", "The ratio of export prices to import prices."), ("Productivity", "Output per worker."), ("Price elasticity of demand", "How responsive quantity demanded is to a price change."), ("Overvalued exchange rate", "A rate that is higher than its competitive level, making exports dear."), ("Oil exporter", "A country that earns much of its export revenue from oil."), ("Import dependence", "Reliance on imports for key goods such as oil and food."), ("Hot money", "Funds that move quickly between countries to earn higher returns."), ("Net primary income", "Primary income received minus primary income paid.")]) + "labK(); \n"
explore = '''
  <h2>Lab 1 · What drives the balance?</h2>
  <p>Exports and imports start at 100 each. Change home income growth, demand abroad and competitiveness and see the balance.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Exports</small><strong id="ka1"></strong></div><div><small>Imports</small><strong id="ka2"></strong></div><div><small>Balance</small><strong id="ka3"></strong></div></div><div class="verdict" id="kav"></div></div></div>
    <svg id="labK" viewBox="0 0 760 330" role="img" aria-label="Exports and imports"></svg>
  </div>

  <h2>Lab 2 · Causes of deficits and surpluses</h2>
  <p>Pick a cause to see whether it tends to cause a deficit or a surplus.</p>
  <div class="card"><div class="row" id="csBtns"></div><div id="csOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two causes of a current account deficit.", "Two different causes, each linked to exports, imports or income flows.",
      "[K|One cause is rising incomes at home.] [N|People spend more, including on imports, so imports could rise faster than exports.] [K|Another is a lack of competitiveness.] [N|If costs and prices are higher than rivals' or quality is lower, exports are less attractive and imports more attractive, so the deficit widens.]"),
    Q(2, "Explain", 4, "Explain the relationship between the oil price and the UAE's current account balance. (Oct/Nov 2024, P21)", "Oil is a major export: price up, export revenue up, surplus; price down, revenue down, smaller surplus or deficit.",
      "[K|The UAE exports a lot of oil, so oil is a large part of its export revenue.] [N|When the oil price rises, export revenue rises, so the current account surplus widens (or deficit narrows).] [N|When the oil price falls, export revenue falls, so the surplus shrinks or a deficit may appear.] [A|There is therefore a positive relationship between the oil price and the current account balance.]"),
    Q(3, "Analyse", 6, "Analyse how advances in technology may improve the current account balance of a country. (Feb/Mar 2023, P22)", "Productivity, quality, lower costs, new products; imports substituted.",
      "[K|Advances in technology can raise productivity and lower costs of production.] [N|Firms can cut prices or improve quality, so exports become more competitive and demand for them could rise, increasing export revenue.] [N|New products and better quality may also make domestic goods more attractive than imports, reducing import spending.] [N|Technology exports, such as software, may become a new source of services income.] [E|The effect depends on how quickly firms adopt technology and on competitors' progress.]", key=True),
    Q(4, "Analyse", 5, "Analyse the relationship between inflation rates and current account balances. (May/June 2022, P21 style)", "Use data: typically higher inflation goes with a worse balance. Explain via competitiveness.",
      "[A|Generally countries with higher inflation rates tend to have current account deficits, whereas countries with low inflation tend to have surpluses.] [A|For example, a country with 10% inflation may have a deficit of 4% of GDP and one with 1% inflation a surplus of 3%.] [N|Higher inflation makes a country's exports dearer than rivals', so export demand falls, and imports become cheaper in comparison, so they rise.] [E|There are exceptions, for example an oil exporter with high inflation but a surplus because of high oil revenue.]", key=True),
    Q(5, "Analyse", 6, "Analyse how a country's current account deficit might be reduced if its firms become more competitive. (Oct/Nov 2020, P21)", "Competitiveness: price, quality, productivity; exports rise, imports fall; link to the deficit.",
      "[K|If firms become more competitive their products are cheaper or better.] [N|Foreign buyers are more likely to buy them, so demand for exports and export revenue rise.] [N|Domestic consumers may switch from imports to home-produced goods, reducing import spending.] [N|Higher exports and lower imports narrow the trade in goods deficit and so the current account deficit.] [E|However, it may take time to improve competitiveness and rivals may improve too.]", key=True),
)
tp = tips([
    ("Causes of a deficit:", "high home spending, low competitiveness, high exchange rate, weak demand abroad, falling export prices, income outflows."),
    ("Link each cause to exports, imports or income.", "Do not just name it."),
    ("Know examples.", "Oil price and oil exporters; inflation and competitiveness; technology."),
    ("Surplus causes are the reverse.", "Plus remittances and investment income."),
    ("Evaluate with time lags and elasticity.", "Competitiveness takes years to build."),
], cmds("Explain", "Analyse"))
body = page(CL("6.4.2 Causes of current account deficit and surplus"), "Causes of Current Account Deficits and Surpluses", "Why a country may run a current account deficit or surplus: competitiveness, demand, prices, exchange rates and income flows. Syllabus 6.4.2.",
    learn=learn, watch=watch(("Causes of a deficit", "stD"), ("Causes of a surplus", "stS"), ("Oil price and an oil exporter's current account", "stO")), explore=explore,
    practise=practise(("Deficit or surplus?", "cl1", "card"), ("Which type of cause?", "cl2", "card"), ("Match the cause to the effect", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("China and Germany's surpluses", "China and Germany run large current account surpluses, driven by strong, competitive manufactured exports and relatively high saving.", "Competitiveness and saving as causes of a surplus."),
        rw("The US deficit", "The United States has run a large current account deficit for decades, because Americans spend more on imports than the country earns from exports.", "High spending causing a deficit."),
        rw("Oil exporters", "Saudi Arabia and the UAE move between surplus and deficit as oil prices change.", "Export prices and the current account."),
        rw("Greece before 2010", "Greece ran a large current account deficit in the 2000s, with fast-growing imports and high costs that made exports uncompetitive.", "A deficit from low competitiveness and strong demand."),
        rw("Remittance-dependent economies", "Countries such as Nepal and the Philippines receive large remittances, which offset trade deficits.", "Secondary income inflows.")),
    exam=ex, tips=tp)
write("bp2", body, js, "Causes of Current Account Deficits and Surpluses", "ig-bop-causes")

# =========================================================== 6.4.3 Consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A current account deficit or surplus affects <b>GDP, employment, inflation and the foreign exchange rate</b>. Net exports (X − M) are part of aggregate demand, so a surplus adds to AD and a deficit subtracts from it. A <b>deficit</b> must be financed by borrowing, selling assets or using reserves, and tends to put <b>downward pressure on the exchange rate</b>. A <b>surplus</b> tends to push the exchange rate <b>up</b>. Whether a deficit or surplus is a problem depends on its <b>size</b>, how <b>long</b> it lasts and <b>what causes</b> it.</p></div>

  <h2>Effects of a current account deficit</h2>
  <div class="grid2">
    <div class="card"><h3>Possible harms</h3><ul><li><b>Lower AD:</b> net exports are negative, so GDP and jobs in export and import-competing industries may be lower</li><li><b>Exchange rate pressure:</b> more of the currency is supplied than demanded, so it tends to fall; a fall raises import prices and <b>inflation</b></li><li><b>Financing:</b> the country must borrow, sell assets or use reserves; debt and interest payments build up</li><li>May signal an uncompetitive economy</li><li>The government may be forced to cut spending or raise interest rates, slowing growth and raising unemployment</li></ul></div>
    <div class="card"><h3>Possible benefits or not a problem</h3><ul><li>If caused by imports of <b>capital goods</b>, it can raise future output and growth</li><li>Cheap imports can lower prices and raise living standards</li><li>If small, or financed by <b>foreign investment</b>, it may be sustainable</li><li>A fast-growing country may attract investment and run a deficit safely</li></ul></div>
  </div>
  <h2>Effects of a current account surplus</h2>
  <div class="grid2">
    <div class="card"><h3>Possible benefits</h3><ul><li><b>Higher AD:</b> net exports add to GDP and jobs in exporting industries</li><li>Builds up <b>reserves</b> and overseas assets; can lend abroad</li><li>Supports a <b>strong exchange rate</b>, making imports cheaper and reducing inflation</li><li>Reduces dependence on foreign borrowing</li></ul></div>
    <div class="card"><h3>Possible harms</h3><ul><li><b>Exchange rate pressure upwards:</b> more demand for the currency raises it, which makes exports dearer and reduces the surplus</li><li><b>Inflation:</b> extra demand may raise demand-pull inflation, especially near full capacity</li><li>Low spending by residents: the country is <b>exporting resources</b> instead of enjoying more goods</li><li>Trading partners may complain or retaliate; trade tensions</li></ul></div>
  </div>

  <h2>Impact summary</h2>
  <div class="tw"><table class="t">
    <tr><th>Variable</th><th>Persistent deficit</th><th>Persistent surplus</th></tr>
    <tr><td><b>GDP</b></td><td>Lower net exports reduce AD; growth may slow</td><td>Higher net exports raise AD and growth</td></tr>
    <tr><td><b>Employment</b></td><td>Jobs lost in industries hit by imports; may rise if forced to cut demand</td><td>More jobs in export industries</td></tr>
    <tr><td><b>Inflation</b></td><td>Imported inflation if the currency falls</td><td>Demand-pull pressure; but a strong currency lowers import prices</td></tr>
    <tr><td><b>Exchange rate</b></td><td>Downward pressure (depreciation)</td><td>Upward pressure (appreciation)</td></tr>
  </table></div>
  <p class="note">In a <b>fixed</b> system, a deficit is handled by the central bank using up its <b>reserves</b>, and a surplus adds to them.</p>
'''
js = HEAD + COMMON + '''
const DF = ["The country runs a persistent current account deficit", "More of the currency is supplied than demanded", "The exchange rate falls", "Imports become dearer: imported inflation", "The deficit must be financed by borrowing or selling assets", "Debt and interest payments rise; the government may have to cut spending"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Consequences of a persistent deficit", base: { n: 0 }, draw: mkChain(DF, "--bad"), steps: chainSteps(["The country runs a <b>persistent current account deficit</b>.", "<b>More of the currency is supplied</b> than demanded (imports exceed exports).", "The <b>exchange rate falls</b>.", "Imports become dearer: <b>imported inflation</b>.", "The deficit must be <b>financed</b> by borrowing, selling assets or using reserves.", "<b>Debt and interest payments rise</b>; the government may have to cut spending, slowing growth."]) });
const SF = ["The country runs a persistent surplus", "Foreigners demand more of its currency", "The exchange rate rises", "Exports become dearer; imports cheaper: inflation falls", "Net exports add to AD: GDP and jobs rise", "But exporters may lose competitiveness and the surplus shrinks"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Consequences of a persistent surplus", base: { n: 0 }, draw: mkChain(SF, "--good"), steps: chainSteps(["The country runs a <b>persistent surplus</b>.", "Foreigners <b>demand more of its currency</b>.", "The <b>exchange rate rises</b>.", "Exports become dearer; <b>imports cheaper</b>: inflation falls.", "Net exports add to <b>AD</b>: GDP and jobs rise.", "But exporters may lose competitiveness and <b>the surplus shrinks</b>."]) });
function adChart2(s) {
  const nx = s.nx, c = 90 + 0.8 * nx; let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: Math.abs(nx) > 1 ? 0.4 : 1 } });
  if (Math.abs(nx) > 1) { const [y1, p1] = solveAD(nx); o += adLine(c, nx > 0 ? "c2" : "c4", nx > 0 ? "AD₁" : "AD₂", { t: nx > 0 ? "t2" : "t4" }) + hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, nx > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd"); }
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: Math.abs(nx) > 1 ? 0.45 : 1 });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Net exports and aggregate demand", base: { nx: 0 }, draw: adChart2, steps: [
  { cap: "AD = C + I + G + <b>(X − M)</b>. Net exports are part of aggregate demand.", s: { nx: 0 } },
  { cap: "A current account <b>surplus</b> (exports exceed imports) <b>raises net exports</b>: AD shifts right. Real GDP and jobs rise, and the price level rises.", s: { nx: 14 } },
  { cap: "A <b>deficit</b> reduces net exports: AD shifts <b>left</b>. Real GDP and employment fall, and inflationary pressure eases.", s: { nx: -14 } },
] });

/* Lab 1: financing */
function labF() {
  if (!$("#fa") || !$("#fb") || !$("#fc")) return;
  const def = +$("#fa").value, yrs = +$("#fb").value, rate = +$("#fc").value / 100, gdp = 400; let debt = 0; const ds = [0]; for (let i = 1; i <= yrs; i++) { debt = debt * (1 + rate) + def; ds.push(debt); }
  $("#fa1").textContent = "$" + money(debt, 0) + "bn"; $("#fa2").textContent = money((debt / gdp) * 100, 0) + "%"; $("#fa3").textContent = "$" + money(debt * rate, 1) + "bn";
  $("#fav").textContent = `A deficit of $${def}bn a year for ${yrs} years, financed by borrowing at ${Math.round(rate * 100)}%, builds up foreign debt of $${money(debt, 0)}bn (${money((debt / gdp) * 100, 0)}% of a $${gdp}bn GDP). Interest payments are now $${money(debt * rate, 1)}bn a year, which are a primary income outflow that makes the current account worse. This is why persistent, large deficits are a concern.`;
  const base = 290, mx = Math.max(...ds, 10), k = 220 / mx, w = Math.min(50, 600 / (ds.length + 1)); let o = SV.line(60, base, 700, base);
  ds.forEach((v, i) => { const x = 80 + i * (w + 8), h = Math.max(2, v * k); o += SV.rect(x, base - h, w, h, "", { style: "fill:var(--bad)", opacity: 0.75 }) + SV.text(x + w / 2, base + 18, i, "sm", { "text-anchor": "middle" }); if (i % Math.max(1, Math.floor(ds.length / 8)) === 0 || i === ds.length - 1) o += SV.text(x + w / 2, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:10px" }); });
  $("#labF").innerHTML = o + SV.text(60, 24, "Foreign debt after each year ($bn)", "sm");
}
Lib.slider($("#g1"), { id: "fa", label: "Current account deficit per year ($bn)", min: 5, max: 40, step: 5, value: 20, fmt: (v) => "$" + v, onInput: labF });
Lib.slider($("#g2"), { id: "fb", label: "Number of years", min: 1, max: 15, step: 1, value: 8, fmt: (v) => v + " years", onInput: labF });
Lib.slider($("#g3"), { id: "fc", label: "Interest rate on the borrowing", min: 1, max: 10, step: 1, value: 4, fmt: (v) => v + "%", onInput: labF });
const EC = [
  { n: "GDP", d: "Net exports reduce AD, so GDP growth may slow; but imported capital goods can raise future output.", s: "Net exports add to AD, so GDP rises." },
  { n: "Employment", d: "Jobs may be lost in industries hit by imports; the government may have to cut demand.", s: "More jobs in export industries." },
  { n: "Inflation", d: "A falling currency raises import prices: imported inflation. Weaker AD may reduce demand-pull pressure.", s: "More demand-pull pressure, but a strong currency lowers import prices." },
  { n: "Exchange rate", d: "More supply of the currency than demand: it tends to fall.", s: "More demand for the currency: it tends to rise." },
  { n: "Financing and reserves", d: "Borrowing, selling assets or using reserves; debt and interest rise.", s: "Reserves and overseas assets grow; the country can lend abroad." },
];
button_table("ecBtns", "ecOut", EC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Persistent deficit</th><th>Persistent surplus</th></tr><tr><td>${p.d}</td><td>${p.s}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each effect more likely with a <b>deficit</b> or a <b>surplus</b>?", buckets: [{ label: "Current account deficit" }, { label: "Current account surplus" }], items: [
  { text: "Downward pressure on the exchange rate", b: 0 }, { text: "Need to borrow or use reserves", b: 0 }, { text: "Lower AD from net exports", b: 0 }, { text: "Risk of imported inflation", b: 0 },
  { text: "Upward pressure on the exchange rate", b: 1 }, { text: "Reserves and overseas assets grow", b: 1 }, { text: "Net exports add to AD and jobs", b: 1 }, { text: "Risk of demand-pull inflation near full capacity", b: 1 },
], done: "Know the effects on AD, the exchange rate, financing and inflation." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>reason a deficit may not be a problem</b> or a <b>reason it is</b>?", buckets: [{ label: "May not be a problem" }, { label: "Is a problem" }], items: [
  { text: "It is small relative to GDP", b: 0 }, { text: "It is caused by imports of machinery that raise future output", b: 0 }, { text: "It is financed by foreign investment", b: 0 }, { text: "It is temporary", b: 0 },
  { text: "It is large and lasts for many years", b: 1 }, { text: "It is financed by borrowing at high interest", b: 1 }, { text: "It puts pressure on the currency to fall", b: 1 }, { text: "It reflects uncompetitive exports", b: 1 },
], done: "Size, duration and cause decide." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Net exports", "Exports minus imports: part of AD"],
  ["Financing a deficit", "Borrowing, selling assets or using reserves to pay for it"],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency"],
  ["Imported inflation", "A rise in prices from dearer imports"],
  ["Persistent deficit", "A deficit lasting for many years"],
  ["Hot money", "Funds that move to earn the highest return"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a persistent deficit could cause a fall in the exchange rate</b>.", items: [
  "Imports exceed exports for many years",
  "Residents sell more of their currency than foreigners buy",
  "Supply of the currency exceeds demand",
  "The exchange rate depreciates",
  "Imports become dearer: inflation may rise",
], done: "The link from a deficit to the exchange rate." });
''' + calc_js([
    ("A deficit of $20bn a year is financed by borrowing for 5 years with no interest. How much foreign debt builds up ($bn)?", 100, "20 × 5 = <b>$100bn</b>.", None, None),
    ("Foreign debt is $120bn and the interest rate is 5%. What are the interest payments ($bn)?", 6, "5% × 120 = <b>$6bn</b>.", None, None),
    ("A country's net exports rise from −$10bn to +$5bn in an economy with GDP $300bn. By what percentage of GDP does AD rise?", 5, "15 ÷ 300 × 100 = <b>5%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A current account deficit is most likely to put the exchange rate under pressure to:", ["Rise", "Fall", "Stay the same", "Double"], 1, "More supply of the currency."),
    ("Net exports are part of:", ["Consumption", "Aggregate demand", "Government spending only", "Investment only"], 1, "AD = C + I + G + (X − M)."),
    ("A surplus is most likely to:", ["Reduce AD", "Raise AD", "Reduce reserves", "Cut employment"], 1, "Net exports add to AD."),
    ("A deficit must be financed by:", ["Selling more goods", "Borrowing, selling assets or using reserves", "Raising exports only", "Cutting taxes"], 1, "Capital must flow in."),
    ("A fall in the exchange rate after a deficit could cause:", ["Imported inflation", "Lower import prices", "Fewer exports", "Lower inflation"], 0, "Dearer imports."),
]) + "\n" + cards_js([("Net exports", "Exports minus imports; part of aggregate demand."), ("Financing a deficit", "Paying for a deficit by borrowing, selling assets or using reserves."), ("Foreign exchange reserves", "A central bank's holdings of foreign currency."), ("Imported inflation", "A rise in prices caused by dearer imports, often after a fall in the exchange rate."), ("Persistent deficit", "A current account deficit that lasts for many years."), ("Debt servicing", "Making interest and capital payments on debts."), ("Sustainable deficit", "A deficit that can be financed without causing problems."), ("Competitiveness", "How attractive a country's goods are compared with rivals'."), ("Hot money", "Short-term funds that move between countries seeking higher returns.")]) + "labF(); \n"
explore = '''
  <h2>Lab 1 · Financing a deficit</h2>
  <p>A deficit has to be financed. Borrowing builds up foreign debt and interest payments, which then worsen the current account.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Foreign debt at the end</small><strong id="fa1"></strong></div><div><small>Debt as % of GDP ($400bn)</small><strong id="fa2"></strong></div><div><small>Yearly interest</small><strong id="fa3"></strong></div></div><div class="verdict" id="fav"></div></div></div>
    <svg id="labF" viewBox="0 0 760 330" role="img" aria-label="Foreign debt after each year"></svg>
  </div>

  <h2>Lab 2 · Effects on the economy</h2>
  <p>Pick a variable to see the effect of a persistent deficit and of a persistent surplus.</p>
  <div class="card"><div class="row" id="ecBtns"></div><div id="ecOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two possible consequences of a persistent current account deficit.", "Pressure on the exchange rate and imported inflation; need to borrow or use reserves; slower growth.",
      "[K|A persistent deficit puts downward pressure on the exchange rate,] [N|because more of the currency is supplied by residents buying imports than demanded by foreign buyers; a fall in the rate raises import prices and could cause inflation.] [K|The deficit has to be financed by borrowing, selling assets or using reserves,] [N|so foreign debt and interest payments build up and the government may have to cut spending.]"),
    Q(2, "Analyse", 6, "Analyse how a current account surplus could affect GDP, employment and the exchange rate.", "Net exports add to AD; export jobs; demand for currency up; appreciation.",
      "[K|A surplus means exports exceed imports, so net exports are positive.] [N|Net exports are part of aggregate demand, so AD shifts right and real GDP could rise.] [N|Firms in export industries need more workers, so employment could rise.] [N|Foreigners need more of the country's currency to pay for exports, so demand for it increases and the exchange rate tends to rise.] [E|A higher exchange rate makes exports dearer and imports cheaper, which could reduce the surplus.]", key=True),
    Q(3, "Discuss", 8, "Discuss whether or not a current account deficit on its balance of payments harms an economy. (May/June 2020, P21)", "Harm: lower AD, currency falls, inflation, debt, uncompetitive. Not harm: capital imports, cheap imports, financed by FDI, small, temporary.",
      "[K|A current account deficit means payments to the rest of the world exceed receipts.] [N|It could harm an economy because net exports reduce aggregate demand, so growth and jobs may be lower, and the deficit puts downward pressure on the exchange rate, raising import prices and inflation.] [N|It has to be financed by borrowing or selling assets, building up debt and interest payments.] [E|A large, persistent deficit is more harmful.] [N|However, a deficit may not be a problem if it is small, temporary, or caused by imports of capital goods that raise future output, or if it is financed by foreign investment.] [N|Cheap imports can also raise living standards.] [E|Overall, a large persistent deficit is likely to harm an economy, but a small one financed by investment may not, so it depends on its size, cause and financing.]", key=True),
    Q(4, "Discuss", 6, "Discuss whether or not a surplus on the current account of its balance of payments would benefit an economy. (Feb/Mar 2024, P22)", "Benefit: AD, jobs, reserves, strong currency. Not: inflation, exchange rate rise hurts exporters, low living standards, trade tensions.",
      "[K|A current account surplus means receipts exceed payments.] [N|It could benefit an economy because net exports add to AD, raising GDP and employment in exporting industries, and builds up reserves and overseas assets.] [N|A stronger currency would make imports cheaper and reduce inflation.] [E|The benefit is larger if the surplus reflects competitive industries.] [N|However, the extra demand could raise demand-pull inflation, a rising exchange rate could make exports dearer and reduce the surplus, and residents may enjoy fewer goods because output is exported.] [E|Overall, a surplus is likely to benefit an economy, particularly if caused by competitiveness, but a very large surplus may bring problems and trade tensions.]", key=True),
    Q(5, "Discuss", 6, "Discuss whether or not India is likely to experience a deficit on the current account of its balance of payments. (Feb/Mar 2020, P22)", "Use evidence from the data: growth, imports, oil, exports, remittances, services. Judge likelihood.",
      "[K|A current account deficit means imports and payments abroad exceed exports and receipts.] [N|India could experience a deficit because fast growth raises incomes and imports, and it imports large amounts of oil and machinery.] [N|Heavy dependence on imports and a high exchange rate could make exports less competitive.] [E|However, India earns large amounts from services exports such as IT, and receives large remittances, which could offset the goods deficit.] [E|Overall, a deficit in goods is likely, but the overall current account could be smaller depending on services and remittances.]", key=True),
)
tp = tips([
    ("Net exports are part of AD.", "Surplus raises AD; deficit lowers it."),
    ("Deficit: exchange rate pressure down; surplus: up.", "Say why: supply and demand for the currency."),
    ("A deficit has to be financed.", "Borrowing, selling assets, reserves."),
    ("Is it a problem? 'It depends on…'", "Size, how long it lasts, what causes it, how it is financed."),
    ("Cover GDP, employment, inflation and exchange rate.", "The four the syllabus names."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("6.4.3 Consequences of current account deficit and surplus"), "Consequences of Current Account Deficits and Surpluses", "How a deficit or surplus affects GDP, employment, inflation and the exchange rate, and when it is a problem. Syllabus 6.4.3.",
    learn=learn, watch=watch(("Consequences of a persistent deficit", "stD"), ("Consequences of a persistent surplus", "stS"), ("Net exports and aggregate demand", "stA")), explore=explore,
    practise=practise(("Deficit or surplus?", "cl1", "card"), ("Problem or not?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The US deficit and the dollar", "Despite large US deficits, foreigners have been willing to lend to the US and hold dollars, so the deficit has been financed without a collapse of the currency.", "A deficit that is financed and sustainable."),
        rw("Greece and Spain after 2008", "Large deficits financed by borrowing left Greece and Spain exposed when lenders lost confidence, forcing cuts in spending and rising unemployment.", "A deficit becoming a problem."),
        rw("Germany's surplus", "Germany's large surplus has been criticised for reflecting low domestic demand, and it adds to pressure on other countries' trade balances.", "Surplus: benefits and tensions."),
        rw("Thailand 1997", "A large deficit and lost confidence led to a sharp fall in the baht and a wider financial crisis.", "Deficit, exchange rate and financing.")),
    exam=ex, tips=tp)
write("bp3", body, js, "Consequences of Current Account Deficits and Surpluses", "ig-bop-consequences")

# =========================================================== 6.4.4 Policies
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The aim is <b>balance of payments stability</b>: avoiding a large persistent deficit (or surplus). Governments can use three groups of policies: <b>expenditure-reducing</b> (cutting demand to cut imports), <b>expenditure-switching</b> (making imports dearer or exports cheaper so spending switches to home goods) and <b>supply-side</b> (raising competitiveness). Each has costs: some cut growth and jobs, some invite retaliation, and some take years. Match the policy to the cause and weigh its effectiveness.</p></div>

  <h2>Policies to reduce a deficit</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Policy</th><th>How it works</th><th>Problems</th></tr>
    <tr><td rowspan="2"><b>Expenditure-reducing</b></td><td>Contractionary fiscal policy (cut government spending, raise taxes)</td><td>Lower incomes reduce spending on imports</td><td>Lower growth and higher unemployment; slow to work</td></tr>
    <tr><td>Contractionary monetary policy (raise interest rates)</td><td>Less borrowing and spending, so fewer imports; may raise the exchange rate</td><td>Slows growth; a higher exchange rate hurts exports</td></tr>
    <tr><td rowspan="3"><b>Expenditure-switching</b></td><td>Lower the exchange rate (or devalue)</td><td>Exports cheaper abroad, imports dearer</td><td>Imported inflation; depends on elasticity; may be slow (J-curve)</td></tr>
    <tr><td>Tariffs and quotas</td><td>Make imports dearer or limit them</td><td>Retaliation; higher prices; inefficiency</td></tr>
    <tr><td>Export subsidies</td><td>Lower exporters' costs</td><td>Cost to taxpayers; trade disputes</td></tr>
    <tr><td><b>Supply-side</b></td><td>Education and training, investment, infrastructure, innovation, lower costs</td><td>Raise productivity and quality, so exports more competitive and imports less needed</td><td>Slow; costly; uncertain</td></tr>
  </table></div>

  <h2>Policies to reduce a surplus</h2>
  <ul>
    <li>Expansionary demand policy (cut taxes, raise spending, cut interest rates) to raise spending on imports.</li>
    <li>A higher exchange rate (revaluation) to raise the price of exports and cut the price of imports.</li>
    <li>Reducing trade restrictions and encouraging imports and overseas investment.</li>
  </ul>

  <h2>How effective are they?</h2>
  <ul>
    <li><b>Elasticity:</b> a lower exchange rate or tariffs only cut a deficit if demand for imports and exports is elastic enough.</li>
    <li><b>Time lags:</b> supply-side policy takes years; fiscal policy takes months.</li>
    <li><b>Conflicts of aims:</b> cutting demand lowers growth and raises unemployment; a lower exchange rate raises inflation.</li>
    <li><b>Retaliation:</b> trade restrictions may lead others to retaliate, cutting exports.</li>
    <li><b>Cause matters:</b> a deficit caused by a fast-growing economy importing capital goods may need no policy; one caused by weak competitiveness needs supply-side policy.</li>
    <li>A <b>mix</b> of policies is often best.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const RD = ["The government cuts spending and raises taxes (or raises interest rates)", "Households have less income to spend", "Spending on imports falls", "The current account deficit narrows", "But AD, growth and jobs also fall", "A conflict between BoP stability and growth and employment"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Expenditure-reducing policy", base: { n: 0 }, draw: mkChain(RD, "--warn"), steps: chainSteps(["The government <b>cuts spending and raises taxes</b> (or the central bank raises interest rates).", "Households have <b>less income</b> to spend.", "<b>Spending on imports falls</b>.", "The <b>current account deficit narrows</b>.", "But <b>AD, growth and jobs also fall</b>.", "A <b>conflict of aims</b>: balance of payments stability against growth and employment."]) });
const SW = ["The government lowers the exchange rate or puts tariffs on imports", "Imports become dearer; exports become cheaper abroad", "Demand switches from imports to home-made goods; export demand rises", "Import spending falls and export earnings rise", "The deficit narrows", "But imported inflation, retaliation and elasticity limit the effect"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "Expenditure-switching policy", base: { n: 0 }, draw: mkChain(SW, "--accent"), steps: chainSteps(["The government <b>lowers the exchange rate</b> or puts <b>tariffs on imports</b>.", "Imports become <b>dearer</b>; exports become <b>cheaper</b> abroad.", "Demand <b>switches</b> from imports to home-made goods; export demand rises.", "<b>Import spending falls</b> and export earnings rise.", "The <b>deficit narrows</b>.", "<b>Evaluate:</b> imported inflation, retaliation and elasticity limit the effect."]) });
const SS = ["The government invests in education, infrastructure and technology", "Productivity rises and costs fall; quality improves", "Exports become more competitive; imports less necessary", "Export revenue rises and import spending falls over time", "The deficit narrows without cutting growth", "Evaluation: slow, costly and uncertain"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy", base: { n: 0 }, draw: mkChain(SS, "--good"), steps: chainSteps(["The government invests in <b>education, infrastructure and technology</b>.", "<b>Productivity rises</b> and costs fall; quality improves.", "Exports become <b>more competitive</b>; imports less necessary.", "<b>Export revenue rises</b> and import spending falls over time.", "The deficit narrows <b>without cutting growth</b>.", "<b>Evaluate:</b> slow, costly and uncertain."]) });

/* Lab 1: mix */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc")) return;
  const c = +$("#ma").value, d = +$("#mb").value, s = +$("#mc").value, def0 = 20, def = def0 - 0.8 * c - 0.5 * d * 1 - 0.4 * s, gdp = -0.5 * c + 0.2 * d + 0.1 * s, inf = 0.3 * d - 0.2 * c - 0.05 * s;
  $("#ma1").textContent = "$" + money(Math.max(def, -10), 1) + "bn"; $("#ma2").textContent = (gdp >= 0 ? "+" : "−") + money(Math.abs(gdp), 1) + "%"; $("#ma3").textContent = (inf >= 0 ? "+" : "−") + money(Math.abs(inf), 1) + " pts";
  $("#mav").textContent = `Starting from a $20bn deficit: cutting demand by ${c} reduces imports but also GDP by ${money(Math.abs(0.5 * c), 1)}%. A ${d}% fall in the exchange rate narrows the deficit but adds ${money(0.3 * d, 1)} points to inflation. Supply-side effort of ${s} helps most slowly (and is shown at full effect here). The best mix depends on which aims matter most: use more than one policy and watch the trade-offs.`;
  const base = 290, k = 8; let o = SV.line(60, base, 700, base);
  [["Deficit ($bn)", Math.max(def, 0), "--bad"], ["Change in GDP (%)", gdp, "--accent"], ["Change in inflation (pts)", inf, "--warn"]].forEach(([n, v, cl], i) => { const x = 110 + i * 190, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, 120, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 60, v >= 0 ? y - 8 : y + h + 16, (v >= 0 ? "" : "−") + money(Math.abs(v), 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 40, n, "sm", { "text-anchor": "middle" }); });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ma", label: "Expenditure-reducing: cut in demand", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Expenditure-switching: fall in the exchange rate (%)", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Supply-side: investment in competitiveness", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v, onInput: labM });
const PP = [
  { n: "Cut government spending / raise taxes", t: "Expenditure-reducing", w: "Lower incomes cut spending on imports.", p: "Lower growth, higher unemployment." },
  { n: "Raise interest rates", t: "Expenditure-reducing", w: "Less borrowing and spending; hot money may raise the currency.", p: "Slows growth; a higher rate may hurt exports." },
  { n: "Lower the exchange rate", t: "Expenditure-switching", w: "Exports cheaper, imports dearer.", p: "Imported inflation; depends on elasticity." },
  { n: "Tariffs and quotas", t: "Expenditure-switching", w: "Imports dearer or limited.", p: "Retaliation; higher prices." },
  { n: "Export subsidies", t: "Expenditure-switching", w: "Lower costs for exporters.", p: "Cost to taxpayers; trade disputes." },
  { n: "Education, investment and infrastructure", t: "Supply-side", w: "Raises productivity and competitiveness.", p: "Slow, costly, uncertain." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it works</th><th>Problems</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td><td>${p.p}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of policy</b> to reduce a current account deficit is each?", buckets: [{ label: "Expenditure-reducing" }, { label: "Expenditure-switching" }, { label: "Supply-side" }], items: [
  { text: "Raise taxes and cut government spending", b: 0 }, { text: "Raise interest rates", b: 0 },
  { text: "Lower the exchange rate", b: 1 }, { text: "Impose import tariffs", b: 1 }, { text: "Subsidise exporters", b: 1 },
  { text: "Invest in education and infrastructure", b: 2 }, { text: "Encourage innovation and lower business costs", b: 2 },
], done: "Reduce demand, switch demand, or raise competitiveness." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>problem</b> with the policy to reduce a deficit, and which policy?", buckets: [{ label: "Slows growth and raises unemployment" }, { label: "Imported inflation or retaliation" }, { label: "Slow to work" }], items: [
  { text: "Cutting government spending", b: 0 }, { text: "Raising interest rates", b: 0 },
  { text: "Lowering the exchange rate", b: 1 }, { text: "Raising tariffs", b: 1 },
  { text: "Investing in education", b: 2 }, { text: "Building new infrastructure", b: 2 },
], done: "Every policy has a cost." });
Lib.match($("#m1"), { prompt: "Match the policy to its main effect on the current account.", pairs: [
  ["Contractionary fiscal policy", "Lower incomes reduce spending on imports"],
  ["Lower exchange rate", "Exports cheaper abroad, imports dearer"],
  ["Tariffs", "Imports dearer, so fewer imported"],
  ["Export subsidies", "Lower costs for exporters"],
  ["Education and training", "Raise productivity and competitiveness"],
  ["Expansionary policy (for a surplus)", "Raises spending on imports"],
], done: "Link each policy to the mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could reduce a deficit</b>.", items: [
  "The government allows or causes the exchange rate to fall",
  "Exports become cheaper in foreign currency; imports become dearer",
  "Demand for exports rises and demand for imports falls",
  "Export revenue rises and import spending falls",
  "The current account deficit narrows",
], done: "An expenditure-switching chain." });
''' + calc_js([
    ("A deficit is $20bn. A policy cuts import spending by $6bn and raises exports by $4bn. What is the new deficit ($bn)?", 10, "20 − 6 − 4 = <b>$10bn</b>.", None, None),
    ("Incomes fall by $10bn and households spend 30% of any change on imports. By how much do imports fall ($bn)?", 3, "30% × 10 = <b>$3bn</b>.", None, None),
    ("A tariff of 10% raises the price of imports and imports fall from $100bn to $90bn. By what percentage did imports fall?", 10, "10 ÷ 100 × 100 = <b>10%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which is an expenditure-reducing policy?", ["A lower exchange rate", "Raising government spending on infrastructure", "Raising taxes and cutting government spending", "Tariffs"], 2, "Reduces demand and imports."),
    ("Which is a supply-side policy to improve the current account?", ["A tariff", "Education and training that raise productivity", "A quota", "Raising interest rates"], 1, "Raises competitiveness."),
    ("A disadvantage of cutting government spending to reduce a deficit is:", ["Higher growth", "Higher unemployment and lower growth", "Cheaper imports", "More exports"], 1, "AD falls."),
    ("A lower exchange rate may fail to reduce a deficit if demand for imports is:", ["Elastic", "Inelastic", "Unit elastic", "Rising"], 1, "Quantities barely change."),
    ("To reduce a large surplus a government could:", ["Raise tariffs", "Cut taxes to raise spending on imports", "Cut government spending", "Lower the exchange rate"], 1, "Expansionary policy."),
]) + "\n" + cards_js([("Expenditure-reducing policy", "Policy that cuts demand, including spending on imports, such as higher taxes or interest rates."), ("Expenditure-switching policy", "Policy that switches spending from imports to home-produced goods, such as a lower exchange rate or tariffs."), ("Supply-side policy", "Policy that raises productive capacity and competitiveness."), ("Devaluation", "A government lowering the value of a fixed currency."), ("Revaluation", "A government raising the value of a fixed currency."), ("Tariff", "A tax on imports."), ("Subsidy", "A payment by the government to lower producers' costs."), ("Retaliation", "Responding to a trade restriction with another."), ("Balance of payments stability", "Avoiding large persistent deficits or surpluses on the current account.")]) + "labM(); \n"
explore = '''
  <h2>Lab 1 · Choosing a policy mix</h2>
  <p>A country has a $20bn deficit. Try cutting demand, lowering the exchange rate and investing in competitiveness, and see the trade-offs. (Illustrative model.)</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Deficit</small><strong id="ma1"></strong></div><div><small>Change in GDP</small><strong id="ma2"></strong></div><div><small>Change in inflation</small><strong id="ma3"></strong></div></div><div class="verdict" id="mav"></div></div></div>
    <svg id="labM" viewBox="0 0 760 330" role="img" aria-label="Deficit, GDP and inflation after policy"></svg>
  </div>

  <h2>Lab 2 · Policy picker</h2>
  <p>Pick a policy to see its type, how it works and its problems.</p>
  <div class="card"><div class="row" id="ppBtns"></div><div id="ppOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two policy measures a government could use to reduce a current account deficit.", "Different types, each with a chain: cut demand, lower exchange rate, tariffs, supply-side.",
      "[K|A government could raise taxes or cut its spending (contractionary fiscal policy).] [N|Households have less income, so spending on imports falls and the deficit narrows.] [K|It could allow the exchange rate to fall.] [N|Exports become cheaper abroad and imports dearer, so export demand could rise and import demand fall.]"),
    Q(2, "Analyse", 6, "Analyse how a country's current account deficit might be reduced if its firms become more competitive. (Oct/Nov 2020, P21)", "See 6.4.2. Competitiveness: price, quality, productivity; exports rise, imports fall.",
      "[K|If firms become more competitive their goods are cheaper or better.] [N|Foreign demand for exports rises, increasing export revenue.] [N|Domestic buyers switch from imports to home-produced goods, so import spending falls.] [N|The goods deficit narrows, and so does the current account deficit.] [E|It takes time to build competitiveness.]", key=True),
    Q(3, "Analyse", 6, "Analyse how a government could use supply-side policy to improve the current account.", "Education, investment, technology, infrastructure; productivity, costs, quality; exports up, imports down.",
      "[K|Supply-side policy aims to raise productivity and lower costs.] [N|Spending on education and training makes workers more skilled, and investment in infrastructure and technology cuts firms' costs.] [N|Goods become cheaper and better, so export demand and revenue rise, and domestic firms replace some imports.] [N|The current account improves without cutting growth.] [E|But it takes years and is costly.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not a fall in a country's foreign exchange rate will improve its current account position.", "For: exports cheaper, imports dearer. Against: elasticity, imported inflation, retaliation, time lag, higher import costs for inputs.",
      "[K|A fall in the exchange rate makes exports cheaper in foreign currency and imports dearer.] [N|Export demand could rise and import demand fall, increasing export revenue and reducing import spending, so the current account could improve.] [E|This is more likely if demand is elastic and if the country has spare capacity.] [N|However, if demand is inelastic, the quantity of imports hardly falls but each import costs more, so the deficit could widen at first.] [N|Dearer imported raw materials raise costs and cause inflation, which reduces the competitive advantage.] [E|Overall, a fall is likely to help in the longer run if demand is elastic, but not for sure: it depends on elasticity, import dependence and time.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not an increase in foreign MNCs will reduce a deficit on the current account. (Oct/Nov 2021, P23)", "For: exports, import substitution, technology, jobs. Against: profits sent home (primary income), imported inputs, may import more.",
      "[K|MNCs are firms that operate in several countries.] [N|They could reduce a deficit by producing goods in the country for export, increasing export revenue, and by producing goods that replace imports.] [N|They may bring technology and investment that raise productivity and competitiveness.] [E|This is more likely if they export most of their output.] [N|However, MNCs send profits home, which is a primary income outflow, and may import raw materials and machinery, increasing imports.] [N|They may produce mainly for the local market.] [E|Overall, MNCs may reduce the goods deficit but their profit outflows could worsen the current account, so the net effect is uncertain.]", key=True),
)
tp = tips([
    ("Three groups of policies:", "expenditure-reducing, expenditure-switching, supply-side."),
    ("Match the policy to the cause.", "Competitiveness problem: supply-side. Overspending: demand-side."),
    ("Always evaluate.", "Growth and jobs, inflation, retaliation, elasticity, time."),
    ("For a surplus, do the opposite.", "Expansionary policy, higher exchange rate, free trade."),
    ("A mix of policies is often best.", "Mention both short-run and long-run measures."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("6.4.4 Policies to achieve balance of payments stability"), "Policies to Achieve Balance of Payments Stability", "Expenditure-reducing, expenditure-switching and supply-side policies to reduce a deficit or surplus, and how effective each is. Syllabus 6.4.4.",
    learn=learn, watch=watch(("Expenditure-reducing policy", "stR"), ("Expenditure-switching policy", "stW"), ("Supply-side policy", "stS")), explore=explore,
    practise=practise(("Which type of policy?", "cl1", "card"), ("What is the problem?", "cl2", "card"), ("Match the policy", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Austerity to close deficits", "After 2010 countries such as Greece and Spain cut spending and raised taxes. Imports fell and deficits narrowed, but output fell and unemployment rose sharply.", "Expenditure-reducing policy and its cost."),
        rw("Devaluations and depreciations", "After the pound fell in 2016 and in earlier episodes, exports rose slowly while import prices rose quickly, showing that effects take time.", "Expenditure-switching policy."),
        rw("Germany's supply-side strategy", "Germany invested in skills, apprenticeships and high-quality engineering, helping it build a persistent surplus.", "Supply-side policy raising competitiveness."),
        rw("Trade wars", "When the US raised tariffs in 2018 to cut its deficit, other countries retaliated and the overall deficit did not fall.", "Why tariffs may fail.")),
    exam=ex, tips=tp)
write("bp4", body, js, "Policies to Achieve Balance of Payments Stability", "ig-bop-policies")
