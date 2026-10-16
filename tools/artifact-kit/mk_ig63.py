"""Builds the four IGCSE Economics 6.3 Foreign exchange rates reviews (6.3.1 to 6.3.4), written from scratch.
Run: python3 tools/artifact-kit/mk_ig63.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

FXM = '''
function fxm(s) {
  const d = s.d || 0, sp = s.s || 0, q0 = 50, p0 = 60, q1 = (100 + d + sp) / 2, p1 = 60 + (d - sp) / 2, lab = (p) => "$" + (p / 50).toFixed(2), moved = Math.abs(d) + Math.abs(sp) > 1;
  let o = SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) + SV.text(QX(0) + 6, PY(120) + 6, "Exchange rate ($ per £1)", "sm") + SV.text(QX(104), PY(0) + 22, "Quantity of pounds traded", "sm", { "text-anchor": "end" });
  o += curve(-1, 110, "c1", "D", { t: "t1", attrs: { opacity: d ? 0.4 : 1 } }) + curve(1, 10, "c3", "S", { t: "t3", attrs: { opacity: sp ? 0.4 : 1 } });
  if (d) o += curve(-1, 110 + d, "c2", "D₁", { t: "t2" });
  if (sp) o += curve(1, 10 - sp, "c4", "S₁", { t: "t4", dx: 4, dy: 10 });
  o += SV.line(QX(0), PY(p0), QX(q0), PY(p0), "gr") + SV.line(QX(q0), PY(p0), QX(q0), PY(0), "gr") + SV.circle(QX(q0), PY(p0), 6, "dot1", { opacity: moved ? 0.45 : 1 }) + ylab(p0, lab(p0)) + xlab(q0, "Q");
  if (moved) o += SV.line(QX(0), PY(p1), QX(q1), PY(p1), "gr") + SV.line(QX(q1), PY(p1), QX(q1), PY(0), "gr") + SV.circle(QX(q1), PY(p1), 6, "dot2") + ylab(p1, lab(p1), "sm bd") + xlab(q1, "Q₁", "sm bd");
  if (s.t) o += SV.text(380, 30, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
'''

# =========================================================== 6.3.1 Definition
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The <span class="kw">foreign exchange rate</span> is the <b>price (or value) of one currency in terms of another currency</b>. It tells you how much of one currency you need to buy one unit of another. For example, £1 = $1.50 means one pound costs one and a half US dollars. The rate matters because it decides what foreign goods cost, what exports earn abroad, and what holidays, loans and investments abroad cost.</p></div>

  <h2>Quoting and reading an exchange rate</h2>
  <p>An exchange rate can be written <b>two ways</b>. If £1 = $1.50, then $1 = £0.67 (1 ÷ 1.50). The same rate is just viewed from the other side.</p>
  <div class="tw"><table class="t">
    <tr><th>Rate</th><th>Meaning</th><th>Conversion</th></tr>
    <tr><td>£1 = $1.50</td><td>One pound buys 1.50 dollars</td><td>Multiply pounds by 1.50 to get dollars; divide dollars by 1.50 to get pounds</td></tr>
    <tr><td>$1 = £0.67</td><td>One dollar buys 0.67 pounds</td><td>Multiply dollars by 0.67 to get pounds</td></tr>
  </table></div>

  <h2>A rise or a fall in a currency?</h2>
  <p>A currency <b>rises</b> if one unit buys <b>more</b> of another currency, and <b>falls</b> if it buys <b>less</b>. Look at the currency whose value you are measuring.</p>
  <div class="grid2">
    <div class="card"><h3>£1 = $1.50 → £1 = $1.20</h3><p>One pound now buys fewer dollars: the pound has <b>fallen</b>. It takes more pounds to buy a dollar ($1 = £0.67 becomes $1 = £0.83), so the dollar has <b>risen</b> against the pound.</p></div>
    <div class="card"><h3>1 US dollar = 15,000 dong → 23,000 dong</h3><p>More dong are needed to buy a dollar, so the <b>dong has fallen</b> and the dollar has risen. (This is the Vietnam question from a past paper.)</p></div>
  </div>

  <h2>Using exchange rates</h2>
  <ul>
    <li><b>Price of an export abroad:</b> price in home currency × exchange rate (foreign currency per unit of home currency).</li>
    <li><b>Price of an import at home:</b> price in foreign currency ÷ exchange rate.</li>
    <li><b>Holidays and investment abroad</b> are cheaper when your currency is strong.</li>
  </ul>
  <div class="formula">Price in $ = price in £ × ($ per £) &nbsp;·&nbsp; Price in £ = price in $ ÷ ($ per £)</div>
  <p class="note">Check which currency is 'one unit'. If the question says €1 = $1.25, multiply euros by 1.25 to get dollars.</p>

  <h2>Why it matters</h2>
  <ul>
    <li>The exchange rate affects <b>exports and imports</b> and so the current account, jobs and inflation (see 6.3.4).</li>
    <li>It is set by supply and demand for a currency in a floating system, or by the government in a fixed system (6.3.3).</li>
  </ul>
'''
js = HEAD + COMMON + '''
function convChart(s) {
  const r = s.r, base = 320, k = 1.7; let o = SV.line(60, base, 710, base) + SV.text(60, 26, "A €100 good sold to a US buyer", "sm");
  [["Price in euros (€)", 100, "--muted"], ["Price in US dollars ($)", 100 * r, "--accent"]].forEach(([n, v, c], i) => { const x = 150 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, (i ? "$" : "€") + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  return o + SV.text(380, 56, "€1 = $" + r.toFixed(2), "lbl bd t3", { "text-anchor": "middle", style: "font-size:20px" });
}
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Converting a price", base: { r: 1 }, draw: convChart, steps: [
  { cap: "A good costs <b>€100</b> in Germany. At <b>€1 = $1.00</b> an American pays <b>$100</b>.", s: { r: 1 } },
  { cap: "The euro <b>rises</b> to <b>€1 = $1.25</b>. One euro now buys more dollars, so the same good costs <b>$125</b> for the American buyer.", s: { r: 1.25 } },
  { cap: "The euro <b>falls</b> to <b>€1 = $0.80</b>. The good now costs only <b>$80</b> for Americans, so a falling currency makes <b>exports cheaper</b> for foreign buyers.", s: { r: 0.8 } },
] });
function quoteChart(s) {
  const r = s.r, inv = 1 / r; let o = "";
  const box = (y, t, c) => SV.rect(130, y, 500, 90, "", { rx: 12, style: `fill:var(${c});fill-opacity:0.15;stroke:var(${c});stroke-width:2.5` }) + SV.text(380, y + 56, t, "lbl bd", { "text-anchor": "middle", style: "font-size:28px" });
  o += SV.text(380, 40, "The same rate, two ways", "sm", { "text-anchor": "middle" }) + box(60, "£1 = $" + r.toFixed(2), "--accent") + SV.line(380, 154, 380, 186, "ax", { style: "stroke-width:2.5" }) + SV.arrowHead(380, 190, "d", "dot1") + SV.text(400, 176, "invert (1 ÷ rate)", "sm") + box(200, "$1 = £" + inv.toFixed(2), "--warn");
  if (s.t) o += SV.text(380, 340, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stQ"), { w: 760, h: 370, label: "Two ways of quoting a rate", base: { r: 1.5, t: "" }, draw: quoteChart, steps: [
  { cap: "The rate <b>£1 = $1.50</b> says what one pound buys.", s: { r: 1.5, t: "" } },
  { cap: "Turn it round: <b>$1 = £0.67</b> (1 ÷ 1.50). It is the same rate, from the dollar's side.", s: { r: 1.5, t: "Same rate, different view" } },
  { cap: "Now £1 = <b>$1.20</b>. The pound buys fewer dollars: the <b>pound has fallen</b>.", s: { r: 1.2, t: "The pound has fallen" } },
  { cap: "Turn it round: $1 = <b>£0.83</b>. More pounds are needed for a dollar: the <b>dollar has risen</b> against the pound.", s: { r: 1.2, t: "The dollar has risen against the pound" } },
] });

/* Lab 1: converter */
function labV() {
  if (!$("#va") || !$("#vb")) return;
  const r = +$("#va").value, p = +$("#vb").value;
  $("#va1").textContent = "$" + money(p * r, 2); $("#va2").textContent = "£" + money(p / r, 2); $("#va3").textContent = "$1 = £" + money(1 / r, 2);
  $("#vav").textContent = `At £1 = $${r.toFixed(2)}: a £${p} British good costs $${money(p * r, 2)} for a US buyer (£ × ${r.toFixed(2)}). A $${p} US good costs £${money(p / r, 2)} for a British buyer ($ ÷ ${r.toFixed(2)}). A higher £ rate makes UK exports dearer in dollars and US goods cheaper in pounds.`;
  const base = 290, k = 1.5; let o = SV.line(60, base, 700, base);
  [["£" + p + " UK good, in $", p * r, "--accent"], ["$" + p + " US good, in £", p / r, "--warn"]].forEach(([n, v, c], i) => { const x = 150 + i * 260, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, (i ? "£" : "$") + money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labV").innerHTML = o;
}
Lib.slider($("#g1"), { id: "va", label: "Exchange rate ($ per £1)", min: 1, max: 2, step: 0.05, value: 1.5, fmt: (v) => "$" + v.toFixed(2), onInput: labV });
Lib.slider($("#g2"), { id: "vb", label: "Price of the good (in its home currency)", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labV });
const DR = [
  { n: "£1 = $1.50 → £1 = $1.80", a: "The pound rose", w: "One pound buys more dollars. The dollar fell." },
  { n: "£1 = $1.50 → £1 = $1.20", a: "The pound fell", w: "One pound buys fewer dollars. The dollar rose." },
  { n: "$1 = 15,000 dong → $1 = 23,000 dong", a: "The dong fell", w: "More dong are needed to buy a dollar." },
  { n: "€1 = $1.10 → €1 = $1.05", a: "The euro fell", w: "One euro buys fewer dollars." },
  { n: "$1 = ¥110 → $1 = ¥100", a: "The dollar fell (yen rose)", w: "A dollar buys fewer yen." },
];
button_table("drBtns", "drOut", DR, 0, (p) => `<div class="tw"><table class="t"><tr><th>What happened</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Did the <b>first-named currency</b> rise or fall?", buckets: [{ label: "Rose" }, { label: "Fell" }], items: [
  { text: "£1 = $1.50 changes to £1 = $1.70", b: 0 }, { text: "€1 = $1.10 changes to €1 = $1.25", b: 0 }, { text: "$1 = 100 rupees changes to $1 = 80 rupees (the rupee)", b: 0 },
  { text: "£1 = $1.50 changes to £1 = $1.30", b: 1 }, { text: "€1 = $1.10 changes to €1 = $0.95", b: 1 }, { text: "$1 = 100 rupees changes to $1 = 120 rupees (the rupee)", b: 1 },
], done: "A currency rises when one unit buys more of another." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Foreign exchange rate", "The price of one currency in terms of another"],
  ["Currency", "The money used in a country"],
  ["Exchange rate quote", "A statement such as £1 = $1.50"],
  ["Rise in a currency", "One unit buys more of another currency"],
  ["Fall in a currency", "One unit buys less of another currency"],
  ["Foreign currency", "Money of another country"],
], done: "Good vocabulary scores marks." });
''' + calc_js([
    ("£1 = $1.50. A UK good costs £200. What does a US buyer pay in dollars?", 300, "200 × 1.50 = <b>$300</b>.", None, None),
    ("£1 = $1.50. A US good costs $240. What does a UK buyer pay in pounds?", 160, "240 ÷ 1.50 = <b>£160</b>.", None, None),
    ("€1 = $1.25. A car costs €20,000. What is the price in dollars?", 25000, "20,000 × 1.25 = <b>$25,000</b>.", None, None),
    ("£1 = $1.50 falls to £1 = $1.20. By what percentage does the pound fall against the dollar?", 20, "0.30 ÷ 1.50 × 100 = <b>20%</b>.", None, None),
    ("£1 = $1.25. What is $1 in pounds (2 d.p.)?", 0.8, "1 ÷ 1.25 = <b>£0.80</b>.", None, 0.01),
]) + mcq_js("qz1", [
    ("What is a foreign exchange rate?", ["The price of one good in terms of another", "The price of one currency in terms of another", "The rate of interest abroad", "The cost of importing"], 1, "Currency for currency."),
    ("£1 = $1.50 changes to £1 = $1.30. The pound has:", ["Risen", "Fallen", "Not changed", "Doubled"], 1, "One pound buys fewer dollars."),
    ("If £1 = $2, how many pounds do you get for $10?", ["£20", "£5", "£2", "£0.5"], 1, "10 ÷ 2."),
    ("If the euro rises against the dollar, European exports to the US:", ["Become cheaper", "Become dearer in dollars", "Do not change", "Double"], 1, "Dollar price rises."),
    ("$1 = 10 pesos changes to $1 = 12 pesos. The peso has:", ["Risen", "Fallen", "Not changed", "Doubled"], 1, "More pesos for a dollar."),
]) + "\n" + cards_js([("Foreign exchange rate", "The price (value) of one currency in terms of another currency."), ("Currency", "The money used in a country."), ("Exchange rate quote", "A statement of how much of one currency one unit of another buys, such as £1 = $1.50."), ("Appreciation", "A rise in the value of a currency in a floating system."), ("Depreciation", "A fall in the value of a currency in a floating system."), ("Foreign currency", "The money of another country."), ("Strong currency", "A currency with a high value against others."), ("Weak currency", "A currency with a low value against others.")]) + "labV(); \n"
explore = '''
  <h2>Lab 1 · Currency converter</h2>
  <p>Set the exchange rate and a price. See what each good costs in the other country's currency.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>UK good in dollars</small><strong id="va1"></strong></div><div><small>US good in pounds</small><strong id="va2"></strong></div><div><small>Inverted rate</small><strong id="va3"></strong></div></div><div class="verdict" id="vav"></div></div></div>
    <svg id="labV" viewBox="0 0 760 330" role="img" aria-label="Prices in the other currency"></svg>
  </div>

  <h2>Lab 2 · Did it rise or fall?</h2>
  <p>Pick a case to see how to read the change.</p>
  <div class="card"><div class="row" id="drBtns"></div><div id="drOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define foreign exchange rate. (May/June 2022, P21)", "Price or value of a currency in terms of another currency.", "[K|The foreign exchange rate is the price (value) of one currency] [K|in terms of another currency (or currencies).]"),
    Q(2, "Explain", 2, "In 2010 one US dollar bought 18,000 Vietnamese dong. In 2017 it bought 22,700 dong. Explain what happened to the foreign exchange rate of the dong. (May/June 2020, P21 style)", "The dong fell: more dong needed for a dollar.", "[K|The dong fell (depreciated) against the dollar] [N|because more dong had to be given to buy one dollar.]"),
    Q(3, "Calculate", 2, "£1 = $1.50. Calculate the price in dollars of a UK car costing £20,000, and the price in pounds of a US phone costing $450.", "Multiply pounds by the rate; divide dollars by the rate.", "[A|20,000 × 1.50 = $30,000.] [A|450 ÷ 1.50 = £300.]"),
    Q(4, "Explain", 4, "Explain what is meant by the exchange rate £1 = $1.25 and how a change to £1 = $1.00 affects a US importer of UK goods.", "Meaning, then effect: pound falls so UK goods cost fewer dollars.",
      "[K|It means that one pound can be exchanged for 1.25 US dollars.] [N|If it changes to £1 = $1.00, the pound has fallen.] [N|A UK good priced at £100 falls in price for the US importer from $125 to $100,] [N|so UK goods become cheaper for US buyers and they may buy more.]"),
)
tp = tips([
    ("Define it as 'the price of one currency in terms of another'.", "Two ideas, two marks."),
    ("Check what is 'one unit'.", "£1 = $1.50: multiply pounds, divide dollars."),
    ("Rise or fall: look at the first currency.", "If one unit buys less, it has fallen."),
    ("Invert by dividing 1 by the rate.", "£1 = $1.25 is $1 = £0.80."),
    ("Link to prices.", "A falling currency makes exports cheaper abroad and imports dearer."),
], cmds("Define", "Calculate", "Explain"))
body = page(CL("6.3.1 Definition of foreign exchange rate"), "Definition of Foreign Exchange Rate", "What a foreign exchange rate is, how to read and convert it, and what a rise or fall means. Syllabus 6.3.1.",
    learn=learn, watch=watch(("Converting a price", "stC"), ("Two ways of quoting a rate", "stQ")), explore=explore,
    practise=practise(("Did the currency rise or fall?", "cl1", "card"), ("Match the term", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Holiday money", "When the pound fell sharply against the euro after 2016, holidays in Spain and France became more expensive for British tourists, while visits to the UK became cheaper for Europeans.", "Exchange rates and the price of services abroad."),
        rw("Vietnam's dong", "A past paper asks what happened to Vietnam's exchange rate between 2010 and 2017: the dong fell against the US dollar.", "Reading a rate change."),
        rw("Buying imports", "A UK firm importing machinery from the US priced in dollars pays more pounds when the pound falls.", "Exchange rates and import prices."),
        rw("Sending money home", "A worker in the UK sending pounds to the Philippines gets more pesos if the pound rises against the peso.", "Exchange rates and remittances.")),
    exam=ex, tips=tp)
write("fx1", body, js, "Definition of Foreign Exchange Rate", "ig-fx-definition")

# =========================================================== 6.3.2 Reasons
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>People, firms and governments buy and sell foreign currencies because they need them to pay for things abroad, to invest, or to make money. The syllabus lists six reasons: <b>trade in goods and services</b>, <b>speculation</b>, <b>government intervention in currency markets</b>, <b>payment of profit, interest and dividends</b>, <b>workers' remittances</b> and <b>investment in capital goods between countries</b>. Each creates demand for or supply of a currency, which in a floating system sets its price.</p></div>

  <h2>The six reasons</h2>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>Demand for the UK pound (foreigners buying £)</th><th>Supply of the UK pound (UK residents selling £)</th></tr>
    <tr><td><b>Trade in goods and services</b></td><td>Foreigners buy UK exports and need pounds to pay UK firms; foreign tourists in the UK</td><td>UK firms and people buy imports and need foreign currency; UK tourists abroad</td></tr>
    <tr><td><b>Speculation</b></td><td>Speculators buy pounds expecting the pound to rise, to sell later at a profit</td><td>Speculators sell pounds expecting it to fall</td></tr>
    <tr><td><b>Government intervention</b></td><td>The central bank buys pounds with its foreign currency reserves to raise or defend the rate</td><td>The central bank sells pounds (buys foreign currency) to lower the rate</td></tr>
    <tr><td><b>Payment of profit, interest and dividends</b></td><td>UK firms and investors abroad send profits, interest and dividends home (converted into pounds)</td><td>Foreign firms and investors in the UK send profits, interest and dividends abroad</td></tr>
    <tr><td><b>Workers' remittances</b></td><td>UK workers abroad send money home</td><td>Migrants in the UK send money to their home countries</td></tr>
    <tr><td><b>Investment in capital goods and firms between countries</b></td><td>Foreign firms invest in UK factories and shares: they need pounds</td><td>UK firms invest abroad: they need foreign currency</td></tr>
  </table></div>

  <h2>Demand for and supply of a currency</h2>
  <div class="grid2">
    <div class="card"><h3>Demand for a country's currency comes from…</h3><ul><li>Foreigners buying its exports and services</li><li>Foreign tourists and students</li><li>Foreign investment into the country</li><li>Profits and remittances sent home from abroad</li><li>Speculators expecting it to rise</li><li>The central bank buying it</li></ul></div>
    <div class="card"><h3>Supply of a country's currency comes from…</h3><ul><li>Residents buying imports</li><li>Residents travelling and studying abroad</li><li>Investment by residents and firms abroad</li><li>Profits and remittances sent abroad</li><li>Speculators expecting it to fall</li><li>The central bank selling it</li></ul></div>
  </div>
  <p class="note">The key idea: when you buy something from another country you <b>supply</b> your own currency and <b>demand</b> theirs. When foreigners buy from you they <b>demand</b> your currency.</p>

  <h2>Examples</h2>
  <ul>
    <li>A US importer buying British cars must sell dollars and buy pounds: it increases the <b>demand for pounds</b>.</li>
    <li>A British family going on holiday to Spain sells pounds and buys euros: it increases the <b>supply of pounds</b> and the <b>demand for euros</b>.</li>
    <li>A foreign investor buying shares in a UK company must buy pounds: <b>demand for pounds</b> rises.</li>
    <li>A Filipino nurse working in London sends money home: she sells pounds and buys pesos.</li>
    <li>A speculator who expects the Turkish lira to fall sells lira: the <b>supply of lira</b> rises and the rate may fall.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const DE = ["A US importer wants to buy British cars", "It must pay in pounds, so it sells dollars and buys pounds", "Demand for pounds rises", "The same happens with foreign tourists, investors and speculators", "More buyers want pounds than before", "The pound's value tends to rise"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Why foreigners demand a currency", base: { n: 0 }, draw: mkChain(DE, "--good"), steps: chainSteps(["A <b>US importer</b> wants to buy British cars.", "It must pay in pounds, so it <b>sells dollars and buys pounds</b>.", "The <b>demand for pounds</b> rises.", "The same applies to <b>foreign tourists, investors</b> and <b>speculators</b>.", "More buyers want pounds than before.", "The pound's <b>value tends to rise</b>."]) });
const SU = ["A British family books a holiday in Spain", "They must pay in euros, so they sell pounds and buy euros", "Supply of pounds rises", "The same happens when UK firms import goods or invest abroad", "More pounds are offered for sale", "The pound's value tends to fall"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Why residents supply a currency", base: { n: 0 }, draw: mkChain(SU, "--bad"), steps: chainSteps(["A <b>British family</b> books a holiday in Spain.", "They must pay in euros, so they <b>sell pounds and buy euros</b>.", "The <b>supply of pounds</b> rises.", "The same applies to <b>UK firms importing</b> or <b>investing abroad</b>.", "More pounds are offered for sale.", "The pound's <b>value tends to fall</b>."]) });
const SP = ["Speculators expect the lira to fall in value", "They sell lira now to buy it back cheaper later", "The supply of lira on the market rises", "Others follow and the lira falls", "The expectation becomes self-fulfilling", "The central bank may intervene to buy lira"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Speculation", base: { n: 0 }, draw: mkChain(SP, "--warn"), steps: chainSteps(["Speculators <b>expect the lira to fall</b> in value.", "They <b>sell lira now</b> to buy it back cheaper later.", "The <b>supply of lira</b> on the market rises.", "<b>Others follow</b> and the lira falls.", "The expectation becomes <b>self-fulfilling</b>.", "The central bank may <b>intervene</b> to buy lira with its reserves."]) });

/* Lab 1: flows */
const FL = [["Exports bought by foreigners", 60], ["Foreign investment in the country", 20], ["Profits, interest and dividends sent in", 10], ["Remittances sent in", 5], ["Foreign tourists' spending", 15]], FO = [["Imports bought by residents", 70], ["Investment abroad by residents", 15], ["Profits, interest and dividends sent out", 12], ["Remittances sent out", 3], ["Residents' spending abroad on tourism", 18]];
function labF() {
  const ids = ["fa", "fb", "fc", "fd", "fe", "ff", "fg", "fh", "fi", "fj"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), inn = v.slice(0, 5).reduce((a, b) => a + b, 0), out = v.slice(5).reduce((a, b) => a + b, 0), net = inn - out;
  $("#fa1").textContent = "$" + inn + "bn"; $("#fa2").textContent = "$" + out + "bn"; $("#fa3").textContent = net > 2 ? "Rises" : net < -2 ? "Falls" : "Stable";
  $("#fav").textContent = `Demand for the currency (inflows) is $${inn}bn and supply (outflows) is $${out}bn. ${net > 2 ? `Demand exceeds supply by $${net}bn: the currency is under pressure to appreciate.` : net < -2 ? `Supply exceeds demand by $${-net}bn: the currency is under pressure to depreciate.` : "Demand and supply are roughly balanced: little pressure on the rate."} In a fixed system the central bank would have to buy or sell currency to stop the rate moving.`;
  const base = 290, k = 1.5; let o = SV.line(60, base, 700, base);
  [["Demand (inflows)", inn, "--good"], ["Supply (outflows)", out, "--bad"]].forEach(([n, x, c], i) => { const px = 190 + i * 260, h = x * k; o += SV.rect(px, base - h, 140, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(px + 70, base - h - 8, "$" + x + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(px + 70, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labF").innerHTML = o;
}
FL.forEach(([l, v], i) => Lib.slider($("#gi" + (i + 1)), { id: ["fa", "fb", "fc", "fd", "fe"][i], label: "Demand: " + l, min: 0, max: 120, step: 5, value: v, fmt: (x) => "$" + x, onInput: labF }));
FO.forEach(([l, v], i) => Lib.slider($("#go" + (i + 1)), { id: ["ff", "fg", "fh", "fi", "fj"][i], label: "Supply: " + l, min: 0, max: 120, step: 5, value: v, fmt: (x) => "$" + x, onInput: labF }));
const TX = [
  { n: "A US firm buys British cars", a: "Demand for pounds", w: "It sells dollars to buy pounds to pay the exporter." },
  { n: "A British firm imports Japanese machinery", a: "Supply of pounds", w: "It sells pounds to buy yen." },
  { n: "A French tourist spends in London", a: "Demand for pounds", w: "Euros are exchanged for pounds." },
  { n: "A foreign investor buys UK shares", a: "Demand for pounds", w: "Foreign currency is sold to buy pounds." },
  { n: "A UK firm builds a factory in Poland", a: "Supply of pounds", w: "Pounds are sold to buy zloty." },
  { n: "A migrant in London sends money to India", a: "Supply of pounds", w: "Pounds are exchanged for rupees." },
  { n: "The Bank of England buys pounds with its reserves", a: "Demand for pounds", w: "Government intervention to raise the rate." },
  { n: "Speculators expect the pound to fall and sell it", a: "Supply of pounds", w: "Speculation increases supply." },
];
button_table("txBtns", "txOut", TX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the UK pound</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each increase the <b>demand for</b> or the <b>supply of</b> a country's currency (the home currency)?", buckets: [{ label: "Demand for the home currency" }, { label: "Supply of the home currency" }], items: [
  { text: "Foreigners buy the country's exports", b: 0 }, { text: "Foreign tourists visit", b: 0 }, { text: "Foreign firms invest in the country", b: 0 }, { text: "Remittances sent home by workers abroad", b: 0 },
  { text: "Residents buy imports", b: 1 }, { text: "Residents go on holiday abroad", b: 1 }, { text: "Home firms invest abroad", b: 1 }, { text: "Foreign firms send profits home", b: 1 },
], done: "Foreigners buying from us demand our currency; we buying from them supply it." });
Lib.classify($("#cl2"), { prompt: "Which <b>reason for buying or selling currency</b> is each?", buckets: [{ label: "Trade" }, { label: "Speculation" }, { label: "Government intervention" }, { label: "Profits, remittances, investment" }], items: [
  { text: "A shop imports clothes", b: 0 }, { text: "A hotel receives foreign tourists", b: 0 },
  { text: "A trader buys a currency expecting it to rise", b: 1 }, { text: "A hedge fund sells a currency it expects to fall", b: 1 },
  { text: "A central bank sells reserves to lower the rate", b: 2 }, { text: "A central bank buys its own currency", b: 2 },
  { text: "Dividends sent to a foreign shareholder", b: 3 }, { text: "A worker abroad sending money home", b: 3 }, { text: "A firm buying a factory in another country", b: 3 },
], done: "Six reasons in the syllabus." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Speculation", "Buying or selling a currency to make a profit from expected changes in its value"],
  ["Remittances", "Money sent home by workers abroad"],
  ["Dividends", "Payments of profit to shareholders"],
  ["Foreign direct investment", "Investment in factories and firms in another country"],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency"],
  ["Hot money", "Funds that move quickly between countries to earn the highest interest rate"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>how an export creates demand for a currency</b>.", items: [
  "A foreign buyer orders goods from a UK firm",
  "The UK firm prices the goods in pounds",
  "The foreign buyer sells its own currency and buys pounds",
  "Demand for pounds rises",
  "The pound tends to appreciate",
], done: "Exports increase demand for the exporter's currency." });
''' + calc_js([
    ("Foreigners buy $80bn of a country's exports and $20bn of its services. Residents buy $90bn of imports. What is the net demand for the country's currency from trade ($bn)?", 10, "(80 + 20) − 90 = <b>$10bn</b> net demand.", None, None),
    ("A country receives $12bn of remittances and sends $4bn abroad. What is the net flow in ($bn)?", 8, "12 − 4 = <b>$8bn</b> inflow.", None, None),
    ("Foreign investment into a country is $25bn and its residents invest $30bn abroad. What is the net effect on demand for the currency ($bn)?", -5, "25 − 30 = <b>−$5bn</b>: supply exceeds demand.", None, None),
]) + mcq_js("qz1", [
    ("Which increases the demand for a country's currency?", ["Residents buying imports", "Foreigners buying its exports", "Residents investing abroad", "Profits sent abroad"], 1, "Foreigners need its currency."),
    ("A British tourist visiting Spain:", ["Increases demand for pounds", "Increases supply of pounds", "Has no effect", "Raises the pound"], 1, "Sells pounds to buy euros."),
    ("Speculation can cause a currency to fall when speculators:", ["Expect it to rise", "Expect it to fall and sell it", "Buy it", "Ignore it"], 1, "Selling raises supply."),
    ("Workers' remittances sent to a country:", ["Reduce demand for its currency", "Increase demand for its currency", "Reduce supply", "Have no effect"], 1, "Foreign currency is converted into home currency."),
    ("Government intervention in currency markets means:", ["The central bank buys or sells currency", "Firms trade only", "Tourists exchange money", "Banks set interest rates only"], 0, "Using reserves to move the rate."),
]) + "\n" + cards_js([("Demand for a currency", "The amount of a currency that people want to buy at each exchange rate."), ("Supply of a currency", "The amount of a currency that people want to sell at each exchange rate."), ("Speculation", "Buying or selling a currency to profit from expected changes in its value."), ("Government intervention", "A central bank buying or selling currency to influence its value."), ("Remittances", "Money sent home by workers abroad."), ("Dividends", "Payments of profit by firms to shareholders."), ("Foreign exchange reserves", "A central bank's holdings of foreign currency."), ("Foreign direct investment (FDI)", "Investment by firms in factories and offices abroad."), ("Hot money", "Funds that move between countries seeking the highest interest rates.")]) + "labF(); \n"
explore = '''
  <h2>Lab 1 · Demand and supply of a currency</h2>
  <p>Set the inflows (demand for the currency) and outflows (supply). See which way the currency is likely to move.</p>
  <div class="card"><div class="grid2"><div><div id="gi1"></div><div id="gi2"></div><div id="gi3"></div><div id="gi4"></div><div id="gi5"></div></div>
    <div><div id="go1"></div><div id="go2"></div><div id="go3"></div><div id="go4"></div><div id="go5"></div></div></div>
    <div class="grid2"><div class="readout"><div><small>Demand (inflows)</small><strong id="fa1"></strong></div><div><small>Supply (outflows)</small><strong id="fa2"></strong></div><div><small>Pressure on the rate</small><strong id="fa3"></strong></div></div><div class="verdict" id="fav"></div></div>
    <svg id="labF" viewBox="0 0 760 330" role="img" aria-label="Demand and supply of the currency"></svg>
  </div>

  <h2>Lab 2 · Demand or supply?</h2>
  <p>Pick a transaction to see its effect on the pound.</p>
  <div class="card"><div class="row" id="txBtns"></div><div id="txOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two reasons why people buy foreign currency.", "Imports, tourism abroad, investment abroad, remittances, speculation.", "[K|To pay for imports of goods and services.] [K|To invest abroad (or to go on holiday abroad, or speculate).]"),
    Q(2, "Explain", 4, "Explain two reasons why foreigners may want to buy a country's currency.", "Exports, tourism, investment, remittances, speculation.",
      "[K|Foreigners buy the currency to pay for the country's exports.] [N|An importer in another country must exchange its own currency for the exporter's to pay, so demand for the exporter's currency rises.] [K|Foreign firms and investors buy it to invest in the country.] [N|To build factories or buy shares they need local currency, increasing demand.]"),
    Q(3, "Analyse", 6, "Analyse the causes of an increase in the demand for foreign currency. (Feb/Mar 2025, P22)", "From a country's view: imports, investment abroad, tourism abroad, remittances out, profits out, speculation. Chain each.",
      "[K|Residents need foreign currency to pay for imports.] [N|If incomes rise, spending on imports rises, so more foreign currency is demanded.] [N|Firms and individuals investing abroad must buy foreign currency, so greater investment overseas increases demand for it.] [N|More citizens travelling abroad on holiday or to study need foreign currency.] [N|Foreign firms sending profits home and workers sending remittances abroad convert domestic currency to foreign currency.] [E|If speculators expect the foreign currency to rise, they also buy it.]", key=True),
    Q(4, "Explain", 4, "Explain how speculation can change an exchange rate.", "Expect a rise: buy; expect a fall: sell; self-fulfilling.",
      "[K|Speculators buy or sell a currency to make a profit from expected changes in its value.] [N|If they expect a currency to fall, they sell it, increasing its supply, which lowers its value.] [N|Others may follow, so the fall can be self-fulfilling.] [A|The central bank may have to intervene by buying the currency.]"),
)
tp = tips([
    ("Six reasons:", "trade, speculation, government intervention, profits and dividends, remittances, investment."),
    ("Foreigners buying from us demand our currency.", "Us buying from them supplies ours."),
    ("Give both demand and supply examples.", "Exports and imports, investment in and out."),
    ("Speculation can be self-fulfilling.", "Expectations move the rate."),
    ("In a floating system these flows set the rate.", "In a fixed system the central bank offsets them."),
], cmds("Identify", "Explain", "Analyse"))
body = page(CL("6.3.2 Reasons for buying and selling foreign currencies"), "Reasons for Buying and Selling Foreign Currencies", "Trade, speculation, government intervention, profits and dividends, remittances and investment: why currencies are bought and sold. Syllabus 6.3.2.",
    learn=learn, watch=watch(("Why foreigners demand a currency", "stD"), ("Why residents supply a currency", "stS"), ("Speculation", "stP")), explore=explore,
    practise=practise(("Demand or supply of the home currency?", "cl1", "card"), ("Which reason?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the export chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Tourism and the Thai baht", "Millions of tourists must buy Thai baht to pay for hotels and meals in Thailand, supporting demand for the currency.", "Demand from tourism."),
        rw("Remittances to the Philippines and Nepal", "Money sent home by workers abroad is a large share of GDP in several countries, adding to the demand for their currencies.", "Workers' remittances."),
        rw("Black Wednesday, 1992", "Speculators sold large amounts of pounds expecting a fall, and the UK was forced out of the European exchange rate mechanism.", "Speculation moving a currency."),
        rw("Central bank intervention", "Switzerland and Japan have sold their own currency to stop it rising too fast and hurting exporters.", "Government intervention in currency markets.")),
    exam=ex, tips=tp)
write("fx2", body, js, "Reasons for Buying and Selling Foreign Currencies", "ig-fx-reasons")

# =========================================================== 6.3.3 Determination
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>In a <span class="kw">floating exchange rate</span> system the rate is set by the <b>demand for and supply of the currency</b> in the foreign exchange market. A rise in the value of a floating currency is an <span class="kw">appreciation</span>; a fall is a <span class="kw">depreciation</span>. The equilibrium rate is where demand equals supply. Changes in demand or supply, from <b>exports and imports, interest rates and speculation</b>, move the rate. In a <b>fixed</b> system the government or central bank sets the rate.</p></div>

  <h2>The foreign exchange market for a currency</h2>
  <p>On the diagram the vertical axis is the <b>price of the currency</b> (for example dollars per pound) and the horizontal axis is the <b>quantity of pounds traded</b>. Demand slopes down (a cheaper pound makes UK goods cheaper for foreigners, so they buy more pounds). Supply slopes up (a dearer pound makes imports cheaper for UK residents, so they sell more pounds).</p>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Shift</th><th>Effect on the exchange rate</th></tr>
    <tr><td>Increase in demand for the currency (more exports, foreign investment, speculation that it will rise)</td><td>Demand shifts right</td><td>Appreciation</td></tr>
    <tr><td>Decrease in demand for the currency</td><td>Demand shifts left</td><td>Depreciation</td></tr>
    <tr><td>Increase in supply of the currency (more imports, investment abroad, speculation that it will fall)</td><td>Supply shifts right</td><td>Depreciation</td></tr>
    <tr><td>Decrease in supply of the currency</td><td>Supply shifts left</td><td>Appreciation</td></tr>
  </table></div>

  <h2>Causes of fluctuations</h2>
  <div class="grid2">
    <div class="card"><h3>Changes in demand for exports and imports</h3><p>If foreigners buy more of a country's exports (higher incomes abroad, better quality, lower prices, lower inflation), demand for the currency rises: <b>appreciation</b>. If residents buy more imports (higher incomes at home), supply of the currency rises: <b>depreciation</b>.</p></div>
    <div class="card"><h3>Changes in the interest rate</h3><p>A <b>higher interest rate</b> attracts foreign savers and 'hot money': demand for the currency rises and supply falls, so it <b>appreciates</b>. A lower rate has the opposite effect.</p></div>
    <div class="card"><h3>Speculation</h3><p>If speculators expect a currency to rise they buy it, pushing it up; if they expect it to fall they sell it, pushing it down. Expectations can be <b>self-fulfilling</b>.</p></div>
    <div class="card"><h3>Other causes</h3><p>Lower inflation than other countries (exports more competitive), more foreign investment, remittances, and central bank intervention.</p></div>
  </div>

  <h2>Floating and fixed systems</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Floating exchange rate</th><th>Fixed exchange rate</th></tr>
    <tr><td><b>Who sets it</b></td><td>Market forces: demand and supply</td><td>The government or central bank</td></tr>
    <tr><td><b>How it changes</b></td><td>Constantly, even day to day</td><td>Rarely; by government decision</td></tr>
    <tr><td><b>Terms</b></td><td>Appreciation and depreciation</td><td>Revaluation (raised) and devaluation (lowered)</td></tr>
    <tr><td><b>How it is kept</b></td><td>No need: it adjusts itself</td><td>Central bank buys or sells currency from its reserves and changes interest rates</td></tr>
    <tr><td><b>Advantages</b></td><td>Adjusts automatically to trade imbalances; no need for large reserves; freedom to set interest rates</td><td>Certainty for traders and investors; less speculation; discipline on policy; helps keep inflation low</td></tr>
    <tr><td><b>Disadvantages</b></td><td>Uncertainty and risk for traders; speculation; may be volatile</td><td>Needs large reserves; speculative attacks; loses control of interest rates; rate may be set at the wrong level</td></tr>
  </table></div>
  <p>In a fixed system, if demand for the currency falls the central bank must <b>buy its own currency</b> using reserves or <b>raise interest rates</b>, otherwise the rate would fall.</p>
'''
js = HEAD + COMMON + FXM + '''
Lib.stepper($("#stM"), { w: 760, h: 400, label: "The market for a currency", base: { d: 0, s: 0, t: "" }, draw: fxm, steps: [
  { cap: "Demand for pounds slopes down and supply slopes up. They meet at an <b>equilibrium exchange rate of $1.20 per £1</b>.", s: { d: 0, s: 0, t: "" } },
  { cap: "<b>Higher demand for UK exports</b> (or a higher UK interest rate, or speculation that the pound will rise) shifts <b>demand right</b> to D₁. The rate rises to about <b>$1.40</b>: an <b>appreciation</b>.", s: { d: 20, s: 0, t: "Appreciation" } },
  { cap: "Instead <b>more imports</b> (or UK investment abroad) shifts <b>supply right</b> to S₁. The pound falls to about <b>$1.00</b>: a <b>depreciation</b>.", s: { d: 0, s: 20, t: "Depreciation" } },
  { cap: "A <b>cut in the interest rate</b> reduces demand and raises supply as hot money leaves: the pound <b>depreciates</b> sharply.", s: { d: -16, s: 16, t: "Depreciation" } },
  { cap: "A <b>rise in the interest rate</b> does the opposite: demand shifts right, supply shifts left and the pound <b>appreciates</b>.", s: { d: 16, s: -16, t: "Appreciation" } },
] });
function fixChart(s) {
  const pf = s.pf, qd = 110 - pf, qs = pf - 10; let o = SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) + SV.text(QX(0) + 6, PY(120) + 6, "Exchange rate ($ per £1)", "sm") + SV.text(QX(104), PY(0) + 22, "Quantity of pounds", "sm", { "text-anchor": "end" });
  o += curve(-1, 110, "c1", "D", { t: "t1" }) + curve(1, 10, "c3", "S", { t: "t3" }) + SV.line(QX(0), PY(pf), QX(100), PY(pf), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(pf) - 8, "Fixed rate $" + (pf / 50).toFixed(2), "lbl bd t2", { "text-anchor": "end" });
  o += SV.circle(QX(qd), PY(pf), 6, "dot2") + SV.circle(QX(qs), PY(pf), 6, "dot2") + SV.text(QX(qd), PY(0) + 18, "Qd " + Math.round(qd), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(qs), PY(0) + 18, "Qs " + Math.round(qs), "sm bd", { "text-anchor": "middle" });
  if (Math.abs(qd - qs) > 1) o += SV.text(380, 32, qs > qd ? "Excess supply " + Math.round(qs - qd) + ": central bank must buy pounds" : "Excess demand " + Math.round(qd - qs) + ": central bank must sell pounds", "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 400, label: "A fixed exchange rate", base: { pf: 60 }, draw: fixChart, steps: [
  { cap: "The government <b>fixes</b> the rate at the equilibrium level, $1.20 per £1. Demand equals supply.", s: { pf: 60 } },
  { cap: "It fixes the rate <b>higher</b>, at $1.50. At that price people want to <b>sell more pounds than are demanded</b>: excess supply.", s: { pf: 75 } },
  { cap: "To keep the rate, the central bank must <b>buy the surplus pounds</b> using its foreign currency reserves, or raise interest rates. Reserves can run out: then the rate is <b>devalued</b>.", s: { pf: 75 } },
  { cap: "If it fixes the rate <b>lower</b> (below equilibrium), there is excess demand and the central bank must <b>sell pounds</b>, building up reserves.", s: { pf: 45 } },
] });
const AP = ["Higher incomes abroad raise demand for the country's exports", "Foreigners need more of the currency to pay for them", "Demand for the currency shifts right", "The exchange rate rises: an appreciation", "Exports become dearer abroad and imports cheaper at home", "Evaluation: effect on trade depends on elasticity; inflation may fall"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Causes and effects of an appreciation", base: { n: 0 }, draw: mkChain(AP, "--good"), steps: chainSteps(["<b>Higher incomes abroad</b> raise demand for the country's exports.", "Foreigners need <b>more of the currency</b> to pay for them.", "<b>Demand for the currency</b> shifts right.", "The exchange rate rises: an <b>appreciation</b>.", "Exports become <b>dearer abroad</b> and imports <b>cheaper</b> at home.", "<b>Evaluate:</b> the effect on trade depends on elasticity; inflation may fall."]) });

/* Lab 1: market simulator */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc") || !$("#md")) return;
  const ex = +$("#ma").value, im = +$("#mb").value, ir = +$("#mc").value, sp = +$("#md").value;
  const d = ex + 3 * ir + sp, s = im - 3 * ir - sp, q1 = (100 + d + s) / 2, p1 = 60 + (d - s) / 2, rate = p1 / 50, ch = ((rate - 1.2) / 1.2) * 100;
  $("#ma1").textContent = "$" + rate.toFixed(2); $("#ma2").textContent = (ch >= 0 ? "+" : "−") + money(Math.abs(ch), 1) + "%"; $("#ma3").textContent = ch > 1 ? "Appreciation" : ch < -1 ? "Depreciation" : "Stable";
  $("#mav").textContent = `Demand for the pound shifts by ${money(d, 0)} and supply by ${money(s, 0)}. The equilibrium rate moves from $1.20 to $${rate.toFixed(2)}: ${ch > 1 ? "an appreciation" : ch < -1 ? "a depreciation" : "almost no change"}. Higher exports, higher interest rates and speculation that the pound will rise push the rate up; more imports and expectations of a fall push it down.`;
  $("#labM").innerHTML = fxm({ d, s });
}
Lib.slider($("#g1"), { id: "ma", label: "Change in demand for UK exports", min: -20, max: 20, step: 2, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Change in UK imports (supply of pounds)", min: -20, max: 20, step: 2, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Change in UK interest rate relative to abroad", min: -5, max: 5, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v + " pts", onInput: labM });
Lib.slider($("#g4"), { id: "md", label: "Speculation (+ expect rise, − expect fall)", min: -15, max: 15, step: 3, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
const CF = [
  { n: "Rise in exports", d: "Demand ↑", r: "Appreciation", w: "Foreigners buy more pounds to pay for UK goods." },
  { n: "Rise in imports", d: "Supply ↑", r: "Depreciation", w: "UK residents sell more pounds to buy foreign currency." },
  { n: "Higher interest rate", d: "Demand ↑, supply ↓", r: "Appreciation", w: "Hot money flows in for higher returns." },
  { n: "Lower interest rate", d: "Demand ↓, supply ↑", r: "Depreciation", w: "Hot money flows out to higher rates elsewhere." },
  { n: "Speculation: expect a rise", d: "Demand ↑", r: "Appreciation", w: "Speculators buy now to sell later at a profit." },
  { n: "Speculation: expect a fall", d: "Supply ↑", r: "Depreciation", w: "Speculators sell now to avoid loss." },
  { n: "Lower inflation than other countries", d: "Demand ↑", r: "Appreciation", w: "UK exports are more competitive." },
  { n: "Foreign investment into the UK", d: "Demand ↑", r: "Appreciation", w: "Investors buy pounds to invest." },
];
button_table("cfBtns", "cfOut", CF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Shift</th><th>Effect on the pound</th><th>Why</th></tr><tr><td>${p.d}</td><td><b>${p.r}</b></td><td>${p.w}</td></tr></table></div>`);
const FF = [
  { n: "Floating: advantages", t: "Adjusts automatically to trade imbalances; no need for big reserves; central bank can set interest rates for the domestic economy." },
  { n: "Floating: disadvantages", t: "Uncertainty for traders; volatile; speculation; may rise or fall too far; imported inflation after a fall." },
  { n: "Fixed: advantages", t: "Certainty for exporters and investors; less speculation; discipline on inflation; stable trade planning." },
  { n: "Fixed: disadvantages", t: "Needs large reserves; speculative attacks; interest rates tied to defending the rate; the rate may be wrong (overvalued or undervalued); devaluation may be forced." },
];
button_table("ffBtns", "ffOut", FF, 0, (p) => `<div class="tw"><table class="t"><tr><th>${p.n}</th></tr><tr><td>${p.t}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Would each cause the <b>pound</b> to <b>appreciate</b> or <b>depreciate</b> in a floating system?", buckets: [{ label: "Appreciate" }, { label: "Depreciate" }], items: [
  { text: "Foreigners buy more UK exports", b: 0 }, { text: "UK interest rates rise above other countries'", b: 0 }, { text: "Speculators expect the pound to rise", b: 0 }, { text: "More foreign investment in the UK", b: 0 },
  { text: "UK residents buy more imports", b: 1 }, { text: "UK interest rates fall", b: 1 }, { text: "Speculators expect the pound to fall", b: 1 }, { text: "UK firms invest more abroad", b: 1 },
], done: "Demand up or supply down: appreciation. Demand down or supply up: depreciation." });
Lib.classify($("#cl2"), { prompt: "Does each describe a <b>floating</b> or a <b>fixed</b> exchange rate?", buckets: [{ label: "Floating" }, { label: "Fixed" }], items: [
  { text: "Set by demand and supply", b: 0 }, { text: "Changes every day", b: 0 }, { text: "Rise is an appreciation", b: 0 }, { text: "No need for large reserves", b: 0 },
  { text: "Set by the central bank", b: 1 }, { text: "Rarely changes", b: 1 }, { text: "Fall is a devaluation", b: 1 }, { text: "Central bank must buy or sell currency to keep it", b: 1 },
], done: "Know the differences and the terms." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Floating exchange rate", "A rate determined by demand and supply in the foreign exchange market"],
  ["Fixed exchange rate", "A rate set and maintained by the government or central bank"],
  ["Appreciation", "A rise in the value of a floating currency"],
  ["Depreciation", "A fall in the value of a floating currency"],
  ["Devaluation", "A fall in the value of a fixed currency by decision"],
  ["Revaluation", "A rise in the value of a fixed currency by decision"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in the interest rate causes an appreciation</b>.", items: [
  "The central bank raises the interest rate",
  "Foreign savers can earn more in the country",
  "Hot money flows in: demand for the currency rises",
  "Fewer residents send money abroad: supply falls",
  "The exchange rate appreciates",
], done: "An interest rate chain." });
''' + calc_js([
    ("The exchange rate rises from £1 = $1.20 to £1 = $1.50. By what percentage has the pound appreciated?", 25, "0.30 ÷ 1.20 × 100 = <b>25%</b>.", None, None),
    ("The rate falls from $1.60 to $1.20 per £1. By what percentage has the pound depreciated?", 25, "0.40 ÷ 1.60 × 100 = <b>25%</b>.", None, None),
    ("Demand for a currency is 80 units at the current rate and supply is 100 units. What is the excess supply the central bank must buy to fix the rate?", 20, "100 − 80 = <b>20 units</b>.", None, None),
]) + mcq_js("qz1", [
    ("In a floating system, an increase in demand for a currency leads to:", ["A depreciation", "An appreciation", "A devaluation", "No change"], 1, "The price of the currency rises."),
    ("Which could cause a depreciation?", ["A rise in exports", "A rise in interest rates", "A rise in imports", "Speculation that it will rise"], 2, "More supply of the currency."),
    ("A fall in the value of a fixed exchange rate is called:", ["Depreciation", "Devaluation", "Revaluation", "Appreciation"], 1, "Government decision."),
    ("A central bank trying to defend a fixed rate that is too high must:", ["Sell its own currency", "Buy its own currency with reserves", "Ignore the market", "Cut interest rates"], 1, "Use reserves to raise demand."),
    ("One advantage of a fixed exchange rate is:", ["It changes every day", "Certainty for traders", "No need for reserves", "No central bank role"], 1, "Reduces risk."),
]) + "\n" + cards_js([("Floating exchange rate", "A rate determined by the demand for and supply of a currency."), ("Fixed exchange rate", "A rate set and maintained by the government or central bank."), ("Appreciation", "A rise in the value of a floating currency."), ("Depreciation", "A fall in the value of a floating currency."), ("Devaluation", "A government lowering the value of a fixed currency."), ("Revaluation", "A government raising the value of a fixed currency."), ("Equilibrium exchange rate", "The rate at which demand for a currency equals supply."), ("Hot money", "Funds that move between countries to earn the highest interest."), ("Foreign exchange reserves", "A central bank's holdings of foreign currency used to manage the rate.")]) + "labM(); \n"
explore = '''
  <h2>Lab 1 · The foreign exchange market</h2>
  <p>Change exports, imports, interest rates and speculation. See how the equilibrium exchange rate moves from $1.20 per £1.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Exchange rate</small><strong id="ma1"></strong></div><div><small>Change</small><strong id="ma2"></strong></div><div><small>Result</small><strong id="ma3"></strong></div></div><div class="verdict" id="mav"></div></div></div>
    <svg id="labM" viewBox="0 0 760 400" role="img" aria-label="Foreign exchange market"></svg>
  </div>

  <h2>Lab 2 · Causes of fluctuations</h2>
  <p>Pick a cause to see how it shifts demand or supply and what happens to the pound.</p>
  <div class="card"><div class="row" id="cfBtns"></div><div id="cfOut"></div></div>

  <h2>Lab 3 · Floating and fixed</h2>
  <p>Pick a box to see advantages and disadvantages of each system.</p>
  <div class="card"><div class="row" id="ffBtns"></div><div id="ffOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by a floating exchange rate, an appreciation and a depreciation?", "Rate set by market forces; rise in value; fall in value.", "[K|A floating exchange rate is one determined by the demand for and supply of the currency in the foreign exchange market.] [K|An appreciation is a rise in its value; a depreciation is a fall.]"),
    Q(2, "Explain", 4, "Explain two reasons why a country's foreign exchange rate may depreciate. (May/June 2022, P22)", "Increase in imports; lower interest rates; speculation; fall in exports; investment abroad.",
      "[K|A rise in imports is one reason.] [N|Residents sell more of their currency to buy foreign currency to pay for imports, so supply rises and the value falls.] [K|A fall in interest rates is another.] [N|Foreign savers and hot money move to countries with higher returns, reducing demand for the currency and increasing supply.]"),
    Q(3, "Explain", 4, "Explain two causes of an increase in the value of a country's floating foreign exchange rate. (May/June 2023, P22)", "Higher exports, higher interest rates, speculation, foreign investment, lower inflation.",
      "[K|An increase in exports is one cause.] [N|Foreign buyers need more of the currency to pay for them, so demand for it rises and its value increases.] [K|A higher interest rate is another.] [N|It attracts foreign savers and hot money, raising demand for the currency and so its value.]"),
    Q(4, "Explain", 4, "Explain two differences between a floating foreign exchange rate and a fixed foreign exchange rate. (Oct/Nov 2021, P23)", "Who sets it; how often it changes; terms (appreciation/depreciation vs revaluation/devaluation).",
      "[K|A floating exchange rate is determined by market forces,] [K|whereas a fixed exchange rate is set by the government or central bank.] [N|A floating rate can change every day,] [N|whereas a fixed rate does not change often and a rise in value is a revaluation and a fall a devaluation.]"),
    Q(5, "Analyse", 6, "Analyse the possible causes of a fall in a country's foreign exchange rate. (Oct/Nov 2024, P23)", "Fixed: government devalues. Floating: lower interest rate, more imports or investment abroad (supply up), fewer exports or remittances (demand down), speculation.",
      "[K|In a fixed system the central bank may devalue the currency,] [N|for example to correct a balance of payments deficit.] [N|In a floating system a lower interest rate reduces hot money inflows, lowering demand and raising supply, so the currency depreciates.] [N|More imports, or investment abroad by residents, increase the supply of the currency.] [N|Fewer exports or lower remittances from workers abroad reduce demand for it.] [N|Speculators who expect it to fall sell it, which could make it fall.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not a country will benefit from having a fixed foreign exchange rate system. (Oct/Nov 2022, P21)", "For: certainty, less speculation, discipline. Against: reserves, no control of interest rates, rate may be wrong, speculation.",
      "[K|A fixed exchange rate is set by the government or central bank.] [N|It could benefit a country by giving traders and investors certainty about prices, making trade and investment less risky.] [N|There may be less speculation, and the government may be forced to follow sensible policies, which could keep inflation low.] [E|This is more useful for a small country that trades mostly with one partner.] [N|However, defending the rate can use up reserves and if people expect a devaluation, speculation could force one.] [N|The country may also lose control of its interest rates, and the fixed rate may be set at the wrong level, hurting exports.] [E|Overall, a fixed rate is more likely to benefit a small open economy with large reserves, but a large diverse economy may prefer a floating rate.]", key=True),
    Q(7, "Discuss", 8, "Discuss whether or not a country should switch from a fixed foreign exchange rate system to a floating system. (Oct/Nov 2020, P22)", "For floating: automatic adjustment, interest rate freedom, no reserves. Against: uncertainty, volatility, imported inflation.",
      "[K|Under a floating system the exchange rate is set by demand and supply.] [N|Switching could allow the rate to adjust automatically to trade imbalances, remove the need to hold large reserves, and let the central bank use interest rates to manage the domestic economy.] [N|It would also avoid forced devaluations and speculative attacks on the fixed rate.] [E|These benefits are larger if the fixed rate has been overvalued.] [N|However, a floating rate can be volatile and uncertain for traders and investors, and a sharp fall could raise import prices and inflation.] [E|Overall, a switch is likely to benefit a country that cannot defend its fixed rate, but a small country may prefer certainty. It depends on reserves, trade pattern and inflation.]", key=True),
)
tp = tips([
    ("Floating: market sets it. Fixed: government sets it.", "Know the vocabulary: appreciation, depreciation, revaluation, devaluation."),
    ("Draw the currency market.", "Label the axes: exchange rate and quantity of the currency; shift D or S."),
    ("Three causes:", "exports and imports, interest rates, speculation."),
    ("Higher interest rate = appreciation.", "Hot money flows in."),
    ("For fixed rates, mention reserves.", "The central bank must buy or sell currency."),
], cmds("Define", "Explain", "Analyse", "Discuss"))
body = page(CL("6.3.3 Determination of foreign exchange rate in foreign exchange market"), "Determination of the Foreign Exchange Rate", "Floating and fixed exchange rates, demand and supply of a currency, equilibrium, appreciation and depreciation, and the causes of fluctuations. Syllabus 6.3.3.",
    learn=learn, watch=watch(("The market for a currency", "stM"), ("A fixed exchange rate", "stF"), ("Causes and effects of an appreciation", "stA")), explore=explore,
    practise=practise(("Appreciate or depreciate?", "cl1", "card"), ("Floating or fixed?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the interest rate chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The pound after the Brexit vote", "After the June 2016 referendum the pound fell about 10% against the dollar within days, as speculators sold pounds and investors worried about trade and investment.", "Speculation and expectations."),
        rw("Hong Kong's peg", "Hong Kong has kept its dollar fixed to the US dollar for decades, so its interest rates follow US rates closely.", "A fixed exchange rate and loss of independent interest rates."),
        rw("Thailand 1997", "Thailand fixed the baht to the dollar but ran short of reserves while speculators sold baht. It was forced to float the baht, which fell sharply, triggering the Asian financial crisis.", "A failed fixed rate."),
        rw("Jordan's peg", "A past paper notes that Jordan fixes its currency to the US dollar and follows US interest rates, because it wants certainty for trade.", "Advantages and costs of a fixed rate.")),
    exam=ex, tips=tp)
write("fx3", body, js, "Determination of the Foreign Exchange Rate", "ig-fx-determination")

# =========================================================== 6.3.4 Consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A change in the exchange rate changes <b>prices</b> and so the <b>demand for exports and imports</b>. A <b>fall</b> (depreciation or devaluation) makes exports <b>cheaper</b> for foreigners and imports <b>dearer</b> at home: exports may rise, imports may fall, jobs may increase and the current account may improve, but import prices and inflation may rise. A <b>rise</b> (appreciation or revaluation) does the reverse: imports and holidays abroad are cheaper and inflation may fall, but exports become dearer, exporters may lose sales and jobs, and the current account may worsen.</p></div>

  <h2>Effects of a fall in the exchange rate</h2>
  <div class="grid2">
    <div class="card"><h3>Possible benefits</h3><ul><li><b>Exports cheaper</b> in foreign currency: exports could rise</li><li><b>Imports dearer</b>: demand for imports could fall; domestic goods more competitive</li><li>Current account may improve; AD rises; <b>output and jobs</b> may rise</li><li>Tourism becomes cheaper for foreign visitors</li></ul></div>
    <div class="card"><h3>Possible costs</h3><ul><li><b>Imported inflation:</b> imported raw materials, fuel and food cost more; cost-push inflation</li><li><b>Firms using imports</b> face higher costs</li><li>Debts and repayments in foreign currency cost more</li><li>Holidays abroad dearer; living standards may fall</li><li>The current account may worsen at first if demand for imports is inelastic</li></ul></div>
  </div>
  <h2>Effects of a rise in the exchange rate</h2>
  <div class="grid2">
    <div class="card"><h3>Possible benefits</h3><ul><li><b>Imports cheaper</b>: lower inflation, lower costs for firms using imports</li><li>Holidays and investment abroad are cheaper</li><li>Greater competition forces domestic firms to improve efficiency</li><li>Foreign debts easier to repay</li></ul></div>
    <div class="card"><h3>Possible costs</h3><ul><li><b>Exports dearer</b> abroad: exports may fall, exporters lose sales and jobs</li><li>Imports cheaper: domestic firms face more competition</li><li>Current account may worsen; lower AD, growth and employment</li><li>Tourism dearer for foreign visitors</li></ul></div>
  </div>

  <h2>How big is the effect? Elasticity</h2>
  <p>How much a fall improves the current account depends on how <b>price elastic</b> the demand for exports and imports is. If demand is <b>elastic</b>, cheaper exports and dearer imports bring large changes in quantity, so the trade balance improves. If demand is <b>inelastic</b>, quantities barely change, so the fall mainly raises the price of imports and the current account may not improve (at least in the short run).</p>

  <h2>Who gains and who loses?</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>When the currency falls</th><th>When the currency rises</th></tr>
    <tr><td><b>Exporters</b></td><td>Gain: more competitive abroad</td><td>Lose: prices rise in foreign currency</td></tr>
    <tr><td><b>Importers and firms using imports</b></td><td>Lose: higher costs</td><td>Gain: lower costs</td></tr>
    <tr><td><b>Consumers</b></td><td>Lose: dearer imports and holidays abroad</td><td>Gain: cheaper imports and holidays abroad</td></tr>
    <tr><td><b>Foreign tourists</b></td><td>Gain: the country is cheaper</td><td>Lose: dearer</td></tr>
    <tr><td><b>Those with foreign-currency debts</b></td><td>Lose: debts cost more</td><td>Gain: debts cost less</td></tr>
    <tr><td><b>The government</b></td><td>Higher growth and revenue; but inflation</td><td>Lower inflation; but slower growth</td></tr>
  </table></div>
'''
js = HEAD + COMMON + '''
function priceChart(s) {
  const r = s.r, base = 320, k = 0.3; let o = SV.line(60, base, 710, base) + SV.text(380, 40, "£1 = $" + r.toFixed(2), "lbl bd " + (r < 1.45 ? "t2" : r > 1.55 ? "t4" : "t1"), { "text-anchor": "middle", style: "font-size:20px" });
  const xp = 1000 * r, mp = 600 / r;
  [["UK car price in US dollars", xp, "--good", "$"], ["US machine price in pounds", mp, "--warn", "£"]].forEach(([n, v, c, pre], i) => { const x = 140 + i * 280, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.rect(x, base - (i ? 400 : 1500) * k, 150, (i ? 400 : 1500) * k, "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4" }) + SV.text(x + 75, base - Math.max(v, i ? 400 : 1500) * k - 8, pre + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  return o + SV.text(60, 66, "Dashed outline: prices at £1 = $1.50 (a £1,000 car and a $600 machine)", "sm");
}
Lib.stepper($("#stP"), { w: 760, h: 380, label: "Exchange rate changes and prices", base: { r: 1.5 }, draw: priceChart, steps: [
  { cap: "At <b>£1 = $1.50</b> a UK car priced at £1,000 costs a US buyer <b>$1,500</b>. A US machine priced at $600 costs a UK buyer <b>£400</b>.", s: { r: 1.5 } },
  { cap: "The pound <b>falls</b> to <b>£1 = $1.20</b>. The UK car now costs <b>$1,200</b> in the US: <b>cheaper</b>, so exports may rise. The US machine now costs <b>£500</b> in the UK: <b>dearer</b>, so imports may fall.", s: { r: 1.2 } },
  { cap: "The pound <b>rises</b> to <b>£1 = $1.80</b>. The UK car costs <b>$1,800</b>: <b>dearer</b>, so exports may fall. The US machine costs <b>£333</b>: <b>cheaper</b>, so imports may rise.", s: { r: 1.8 } },
] });
const DP = ["The currency falls (depreciation)", "Exports become cheaper in foreign currency", "Imports become dearer in the home currency", "Export demand rises; import demand falls (if elastic)", "Net exports rise: AD shifts right", "Output and jobs rise; the current account may improve"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "A fall in the exchange rate and the economy", base: { n: 0 }, draw: mkChain(DP, "--good"), steps: chainSteps(["The currency <b>falls</b> (depreciation).", "Exports become <b>cheaper</b> in foreign currency.", "Imports become <b>dearer</b> in the home currency.", "<b>Export demand rises and import demand falls</b> (if demand is elastic).", "<b>Net exports rise</b>: AD shifts right.", "<b>Output and jobs rise</b>; the current account may improve. <b>Evaluate:</b> imported inflation and elasticity."]) });
const AC = ["The currency rises (appreciation)", "Imported raw materials, fuel and goods become cheaper", "Firms' costs fall and import prices fall", "Inflation is lower", "But exports are dearer abroad and sales fall", "Exporters lose jobs; the current account may worsen"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "A rise in the exchange rate and the economy", base: { n: 0 }, draw: mkChain(AC, "--warn"), steps: chainSteps(["The currency <b>rises</b> (appreciation).", "Imported raw materials, fuel and goods become <b>cheaper</b>.", "<b>Firms' costs fall</b> and import prices fall.", "<b>Inflation is lower</b>.", "But <b>exports are dearer</b> abroad and sales fall.", "<b>Exporters lose jobs</b>; the current account may worsen."]) });

/* Lab 1: effect simulator */
function labE() {
  if (!$("#ea") || !$("#eb")) return;
  const r = +$("#ea").value, e = +$("#eb").value, r0 = 1.5, xp = 1000 * r, mp = 600 / r, xv = 100 * Math.pow(r / r0, -e), mv = 100 * Math.pow(r / r0, e), exp = (1000 * xv) / 1000, imp = (mp * mv) / 1000, net = exp - imp, bal0 = (1000 * 100 - 400 * 100) / 1000;
  $("#ea1").textContent = "$" + money(xp, 0); $("#ea2").textContent = "£" + money(mp, 0); $("#ea3").textContent = (net - bal0 >= 0 ? "+" : "−") + money(Math.abs(net - bal0), 1);
  $("#eav").textContent = r < 1.45 ? `The pound has fallen to $${r.toFixed(2)}. UK cars cost $${money(xp, 0)} (cheaper abroad, ${money(xv, 0)} sold) and US machines cost £${money(mp, 0)} (dearer, ${money(mv, 0)} bought). ${net > bal0 ? "Net exports improve because demand is elastic enough." : "With inelastic demand, the dearer imports outweigh the extra exports: net exports get worse in the short run."}` : r > 1.55 ? `The pound has risen to $${r.toFixed(2)}. UK cars cost $${money(xp, 0)} (dearer, ${money(xv, 0)} sold) and US machines cost £${money(mp, 0)} (cheaper, ${money(mv, 0)} bought). ${net < bal0 ? "Net exports worsen: exporters lose out, but imports are cheaper and help against inflation." : "Because demand is inelastic, net exports still improve in this model."}` : "No change from £1 = $1.50.";
  const base = 290; let o = SV.line(60, base, 700, base);
  [["Car price in $", xp, "--good", 0.18], ["Machine price in £", mp, "--warn", 0.5], ["Cars sold", xv, "--accent", 1.5], ["Machines bought", mv, "--n", 1.5]].forEach(([n, v, c, k], i) => { const x = 90 + i * 150, h = v * k; o += SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labE").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ea", label: "Exchange rate ($ per £1), starting at 1.50", min: 1, max: 2, step: 0.05, value: 1.2, fmt: (v) => "$" + v.toFixed(2), onInput: labE });
Lib.slider($("#g2"), { id: "eb", label: "Price elasticity of demand for exports and imports", min: 0.2, max: 2, step: 0.2, value: 1.4, fmt: (v) => v.toFixed(1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : ""), onInput: labE });
const WG = [
  { n: "Exporters", f: "Gain: cheaper abroad, more sales.", r: "Lose: dearer abroad, fewer sales and jobs." },
  { n: "Importers and firms using imported inputs", f: "Lose: higher costs.", r: "Gain: lower costs." },
  { n: "Consumers", f: "Lose: imports and foreign holidays cost more.", r: "Gain: cheaper imports and holidays." },
  { n: "Foreign tourists", f: "Gain: the country is cheaper.", r: "Lose: the country is dearer." },
  { n: "Borrowers with debts in foreign currency", f: "Lose: debts cost more.", r: "Gain: debts cost less." },
  { n: "The government", f: "More growth and tax revenue; but inflation.", r: "Lower inflation; but slower growth." },
];
button_table("wgBtns", "wgOut", WG, 0, (p) => `<div class="tw"><table class="t"><tr><th>If the currency falls</th><th>If the currency rises</th></tr><tr><td>${p.f}</td><td>${p.r}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a likely effect of a <b>fall</b> or a <b>rise</b> in the exchange rate?", buckets: [{ label: "Fall in the exchange rate" }, { label: "Rise in the exchange rate" }], items: [
  { text: "Exports become cheaper for foreigners", b: 0 }, { text: "Imported raw materials cost more", b: 0 }, { text: "Exporters could take on more workers", b: 0 }, { text: "Cost-push inflation risk", b: 0 },
  { text: "Foreign holidays become cheaper", b: 1 }, { text: "Imports are cheaper, helping to reduce inflation", b: 1 }, { text: "Exporters may lose sales and jobs", b: 1 }, { text: "Domestic firms face more competition from imports", b: 1 },
], done: "Fall: exports cheaper, imports dearer. Rise: the reverse." });
Lib.classify($("#cl2"), { prompt: "Who <b>gains</b> and who <b>loses</b> when a country's currency <b>falls</b>?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "Exporters", b: 0 }, { text: "Foreign tourists visiting", b: 0 }, { text: "Domestic firms competing with imports", b: 0 },
  { text: "Consumers buying imports", b: 1 }, { text: "Firms using imported raw materials", b: 1 }, { text: "People holidaying abroad", b: 1 }, { text: "Borrowers with foreign-currency debts", b: 1 },
], done: "Winners and losers." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Imported inflation", "A rise in prices caused by dearer imports after a fall in the exchange rate"],
  ["Price competitiveness", "How cheap a country's goods are in foreign markets"],
  ["Net exports", "Exports minus imports"],
  ["Elasticity of demand", "The responsiveness of quantity demanded to a price change"],
  ["Current account", "Part of the balance of payments for trade, income and transfers"],
  ["Exchange rate effect", "The change in prices and trade caused by a change in the rate"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could reduce a current account deficit</b>.", items: [
  "The exchange rate falls",
  "Exports become cheaper in foreign currency; imports become dearer",
  "Demand for exports rises and demand for imports falls",
  "Export revenue rises and import spending falls",
  "The current account deficit narrows",
], done: "A chain for a 6-mark answer." });
''' + calc_js([
    ("£1 = $1.50 falls to £1 = $1.20. A UK good costs £500. What is the dollar price before and after (answer: fall in dollar price, $)?", 150, "Before: 500 × 1.50 = $750. After: 500 × 1.20 = $600. Fall = <b>$150</b>.", None, None),
    ("£1 = $1.50 falls to £1 = $1.20. A US good costs $300. By how much does its price in pounds rise (£)?", 50, "Before: 300 ÷ 1.50 = £200. After: 300 ÷ 1.20 = £250. Rise = <b>£50</b>.", None, None),
    ("Exports rise from 100 to 120 units after a currency fall. What is the percentage increase?", 20, "20 ÷ 100 × 100 = <b>20%</b>.", None, None),
    ("Import prices rise by 10% and imports make up 30% of consumer spending. By roughly how much do consumer prices rise (%)?", 3, "30% × 10% = <b>3%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A fall in the exchange rate is likely to:", ["Make exports dearer for foreigners", "Make exports cheaper for foreigners", "Make imports cheaper", "Reduce inflation"], 1, "Foreign currency price of exports falls."),
    ("A rise in the exchange rate is most likely to:", ["Raise imported inflation", "Help to reduce inflation", "Make exports cheaper", "Increase export demand"], 1, "Imports are cheaper."),
    ("A fall in the exchange rate may fail to improve the current account if demand for exports and imports is:", ["Elastic", "Inelastic", "Unit elastic", "Rising"], 1, "Quantities barely change."),
    ("Who gains from a fall in the value of the pound?", ["UK importers", "UK exporters", "UK tourists abroad", "People with dollar debts"], 1, "Exports become more competitive."),
    ("Which is a possible cost of a fall in the exchange rate?", ["Cheaper exports", "Imported inflation", "More jobs", "Better current account"], 1, "Dearer imports raise costs."),
]) + "\n" + cards_js([("Imported inflation", "A rise in prices caused by dearer imports, often after a fall in the exchange rate."), ("Price competitiveness", "How cheap a country's goods are compared with rivals' goods."), ("Net exports", "The value of exports minus imports."), ("Elastic demand", "Quantity demanded changes by a larger percentage than the price change."), ("Inelastic demand", "Quantity demanded changes by a smaller percentage than the price change."), ("Current account", "The part of the balance of payments for trade in goods and services and income flows."), ("Cost-push inflation", "A rise in the price level caused by higher costs of production."), ("Exchange rate effect", "The effect of a change in the exchange rate on prices and trade."), ("Tourism", "Spending by visitors, affected by the exchange rate.")]) + "labE(); \n"
explore = '''
  <h2>Lab 1 · What happens to prices and trade?</h2>
  <p>A UK car costs £1,000 and a US machine costs $600. At £1 = $1.50 the UK sells 100 cars and buys 100 machines. Move the exchange rate and set how sensitive buyers are to price.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>UK car price in $</small><strong id="ea1"></strong></div><div><small>US machine price in £</small><strong id="ea2"></strong></div><div><small>Change in net exports (£000s)</small><strong id="ea3"></strong></div></div><div class="verdict" id="eav"></div></div></div>
    <svg id="labE" viewBox="0 0 760 330" role="img" aria-label="Prices and quantities after an exchange rate change"></svg>
    <p class="note">Illustrative model. Net exports are measured in £ thousands: car receipts minus machine spending.</p>
  </div>

  <h2>Lab 2 · Who gains and who loses?</h2>
  <p>Pick a group to see the effect of a fall or a rise in the currency.</p>
  <div class="card"><div class="row" id="wgBtns"></div><div id="wgOut"></div></div>
'''
ex = exam(
    Q(1, "Analyse", 6, "Analyse how a fall in a country's foreign exchange rate could reduce a deficit on the current account of its balance of payments. (Feb/Mar 2022, P22)", "Exports cheaper, imports dearer, quantities change, revenue and spending change. Elasticity.",
      "[K|A fall in the exchange rate lowers the foreign currency price of exports and raises the home currency price of imports.] [N|Exports become more price competitive, so demand for exports could rise and export revenue increase.] [N|Imports become dearer, so demand for imports could fall, reducing spending on imports.] [N|Higher exports and lower imports reduce the deficit.] [E|This depends on demand for exports and imports being elastic; if inelastic, the deficit might not narrow, at least in the short run.]", key=True),
    Q(2, "Analyse", 6, "Analyse how a fall in a country's foreign exchange rate could increase its inflation rate. (Oct/Nov 2022, P22)", "Imports dearer, raw materials, cost-push; exports cheaper raise demand; less pressure to cut costs.",
      "[K|A fall in the exchange rate makes imports dearer in the home currency.] [N|Imported raw materials, fuel and components cost firms more, so costs of production rise and AS could shift left, causing cost-push inflation.] [N|Imported consumer goods cost more, directly raising the price level.] [N|At the same time exports are cheaper, so demand for them could rise, increasing AD and causing demand-pull inflation.] [E|The effect depends on how much the country imports.]", key=True),
    Q(3, "Analyse", 6, "Analyse how an increase in a country's foreign exchange rate could reduce inflation. (Oct/Nov 2023, P23)", "Imports cheaper, input costs fall, competition, exports dearer reduce AD.",
      "[K|A higher exchange rate makes imports cheaper in the home currency.] [N|Imported raw materials and goods cost less, so firms' costs fall and prices may fall.] [N|More competition from cheaper imports may force domestic firms to hold prices down.] [N|Exports become dearer, so net exports and AD may fall, reducing demand-pull inflation.] [E|But exports and jobs may suffer.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not a rise in a country's foreign exchange rate would benefit its economy. (May/June 2023, P21)", "For: lower inflation, cheaper imports, cheaper holidays, efficiency. Against: exports dearer, jobs, current account, growth.",
      "[K|A rise in the exchange rate means the currency buys more foreign currency.] [N|It could benefit the economy by making imports cheaper, lowering firms' costs and consumer prices, and reducing inflation.] [N|Holidays and investment abroad are cheaper, and competition from imports may raise efficiency.] [E|This is more likely if the country relies heavily on imports.] [N|However, exports become dearer abroad, so exporters may lose sales and cut jobs, and the current account may worsen.] [N|Lower net exports reduce AD, which could slow growth.] [E|Overall, a rise is likely to benefit consumers and importers but harm exporters, so it depends on how much the country exports, the size of the rise and the state of the economy.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not an appreciation of a country's domestic currency will have negative effects on its economy. (Oct/Nov 2021, P21)", "Negative: exports fall, unemployment, current account. Positive: cheaper imports, lower inflation. Judge.",
      "[K|An appreciation is a rise in the value of a floating currency.] [N|It could have negative effects because exports become dearer to foreign buyers, so export sales fall and exporting firms may cut output and jobs, reducing growth and worsening the current account.] [N|Domestic firms also face more competition from cheaper imports.] [E|The effect is larger where demand for exports is elastic.] [N|However, cheaper imports reduce costs and inflation, and consumers can buy more imports and travel abroad more cheaply.] [E|Overall, an appreciation is likely to harm exporters but help consumers and importers, so the effect on the economy depends on the size of the appreciation and how dependent the country is on exports.]", key=True),
    Q(6, "Discuss", 6, "Discuss whether or not having a strong foreign exchange rate is a problem for a country such as Greece. (May/June 2020, P23)", "Strong rate: dearer exports, fewer tourists; cheaper imports. Greece depends on tourism and exports.",
      "[K|A strong exchange rate means the currency buys a lot of foreign currency.] [N|It could be a problem for a country that depends on tourism and exports, because foreign visitors find it dearer and exports are less competitive, so earnings and jobs fall.] [N|The current account could worsen.] [E|This is more serious if demand is elastic.] [N|However, a strong currency makes imports cheaper and reduces inflation, and residents can buy foreign goods and holidays more cheaply.] [E|Overall, it is more likely to be a problem for a tourism and export-dependent economy, but benefits consumers.]", key=True),
)
tp = tips([
    ("Fall: exports cheaper abroad, imports dearer at home.", "Rise: the reverse. Say 'in foreign currency' and 'in home currency'."),
    ("Link to the current account, jobs and inflation.", "Chains for each."),
    ("Elasticity decides the size.", "Inelastic demand may mean the current account does not improve."),
    ("Name who gains and loses.", "Exporters, importers, consumers, tourists, borrowers."),
    ("Evaluate with 'it depends on…'.", "Elasticity, size of change, how much the country trades."),
], cmds("Analyse", "Discuss"))
body = page(CL("6.3.4 Consequences of changes in foreign exchange rates"), "Consequences of Changes in Foreign Exchange Rates", "How a rise or fall in the exchange rate changes prices and the demand for exports and imports, and who gains and loses. Syllabus 6.3.4.",
    learn=learn, watch=watch(("Exchange rate changes and prices", "stP"), ("A fall in the exchange rate and the economy", "stD"), ("A rise in the exchange rate and the economy", "stA")), explore=explore,
    practise=practise(("Fall or rise?", "cl1", "card"), ("Who gains and who loses?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The pound after 2016", "The pound fell after the Brexit vote, boosting some exporters and tourism but raising the cost of imported food and fuel, adding to inflation.", "Both sides of a fall."),
        rw("Swiss franc surge, 2015", "When the Swiss central bank stopped capping the franc, it rose sharply, making Swiss exports and tourism dearer and hurting exporters.", "A rise hurting exporters."),
        rw("Turkey's lira", "After the lira fell sharply in 2018 and again in 2021, imported energy and goods became much dearer and inflation rose.", "Imported inflation."),
        rw("Japan's weak yen", "A weak yen has boosted Japanese exporters' profits and tourism, but raised the cost of imported energy and food.", "Winners and losers from a fall.")),
    exam=ex, tips=tp)
write("fx4", body, js, "Consequences of Changes in Foreign Exchange Rates", "ig-fx-consequences")
