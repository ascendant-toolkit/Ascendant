"""Syllabus 11.5.5-11.5.7 External debt, the IMF and the World Bank. Run: python3 tools/artifact-kit/mk_sy1155.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.5.5 to 11.5.7"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">External debt</b> is the money a country (its government, firms and households) owes to foreign lenders; it arises from <b>persistent current account deficits, borrowing for investment or consumption, shocks such as falling export prices or rising interest rates, and a falling currency when the debt is in foreign currency</b>. The burden is shown by the <b class="kw">debt service ratio</b> (interest and repayments as a share of export earnings), and heavy debt can <b>divert spending from health and education, force austerity and reduce investment</b>. The <b class="kw">International Monetary Fund (IMF)</b> promotes <b>exchange rate stability and lends short-term to countries with balance of payments problems</b>, usually with conditions, whereas the <b class="kw">World Bank</b> provides <b>long-term loans and grants for development projects</b> and poverty reduction.</p></div>

  <h2>1 · Causes of external debt (11.5.5)</h2>
  <ul>
    <li><b>Persistent current account deficits:</b> importing more than is earned from exports means borrowing from abroad to pay for the difference.</li>
    <li><b>Borrowing for investment or consumption:</b> developing countries borrow because domestic saving is low (the savings gap), to build infrastructure or industry, or to fund government deficits. Borrowing is sound if the investment earns a return above the interest cost.</li>
    <li><b>Shocks:</b> a fall in the price of the main export (commodity prices), a rise in oil import prices, a rise in world interest rates (variable-rate debt), a recession in key trading partners, natural disasters or war.</li>
    <li><b>Exchange rate falls:</b> when debt is owed in dollars and the local currency depreciates, the debt costs more in local currency.</li>
    <li><b>Poor management and corruption:</b> wasteful projects, capital flight and unsound lending.</li>
  </ul>

  <h2>2 · Consequences of external debt</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Debt service ratio</b> = (interest + repayments on external debt in a year) ÷ export earnings × 100. A high ratio (often above about 20%) leaves little foreign exchange for imports of capital goods and essentials. The debt-to-GDP ratio is another common measure.</li>
    <li><b>Opportunity cost:</b> money for debt service is not available for <b>health, education and infrastructure</b>, lowering human capital and growth.</li>
    <li><b>Austerity:</b> to find the funds, governments may cut spending and raise taxes, which reduces aggregate demand and growth.</li>
    <li><b>Investment and confidence:</b> a high debt burden raises the risk premium and the interest rate on new borrowing, discourages foreign investors and may cause the currency to fall, which raises the cost of foreign-currency debt (a <b>debt trap</b>).</li>
    <li><b>Loss of independence:</b> countries in difficulty must turn to the IMF or other lenders, accepting conditions.</li>
    <li><b>Benefits if used well:</b> borrowed funds invested in productive assets raise future output and exports, so debt can be repaid from the extra income.</li>
    <li><b>Solutions:</b> debt relief or cancellation (for example the HIPC initiative), rescheduling and restructuring, shifting to grants and concessional loans, raising exports and growth, and improving governance. Relief may cause moral hazard (encouraging irresponsible borrowing in future).</li>
  </ul>

  <h2>3 · The International Monetary Fund (11.5.6)</h2>
  <ul>
    <li>Set up in 1944 with over 190 member countries. Its main roles: <b>promote international monetary cooperation and exchange rate stability</b>; <b>surveillance</b> of members' economies and advice; <b>lending to countries with balance of payments problems</b> (as a short- to medium-term lender when private lenders will not); and <b>technical assistance and training</b> in central banking and public finance.</li>
    <li><b>Conditionality:</b> loans usually come with conditions, often called <b>structural adjustment</b>: cut the budget deficit (expenditure reducing), control inflation, <b>free trade and reduce import restrictions</b>, privatise state firms, deregulate markets, and sometimes devalue the currency or expand exports.</li>
    <li><b>Arguments for:</b> restores confidence and stabilises the economy; gives access to funds when no one else will lend; reforms may raise efficiency and growth.</li>
    <li><b>Arguments against:</b> austerity can deepen recessions and raise unemployment and poverty; devaluation raises import prices (cost-push inflation); opening to imports can hurt infant industries and widen the current account deficit; advice may be one-size-fits-all and ignore social effects and environmental costs; it limits national sovereignty.</li>
  </ul>

  <h2>4 · The World Bank (11.5.7)</h2>
  <ul>
    <li>Consists of the <b>IBRD</b> (loans to middle-income countries) and the <b>IDA</b> (grants and interest-free or very low-interest loans to the poorest countries). It raises funds on world capital markets and from donor governments.</li>
    <li><b>Roles:</b> <b>long-term loans and grants for development projects</b> such as roads, power, water, schools and health; reducing poverty; technical advice and research; and helping with debt and policy reform. It also provides guarantees that reduce risk for private investors.</li>
    <li><b>Criticisms:</b> conditions may be similar to the IMF's, projects may harm the environment or displace people, loans add to debt, and richer countries have more voting power.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>IMF</th><th>World Bank</th></tr>
    <tr><td><b>Main purpose</b></td><td>Monetary stability and balance of payments support</td><td>Long-term economic development and poverty reduction</td></tr>
    <tr><td><b>Lending</b></td><td>Short- to medium-term loans to countries in balance of payments difficulty</td><td>Long-term loans and grants for projects and programmes</td></tr>
    <tr><td><b>Typical use</b></td><td>Stabilise the currency, finance a deficit, restore confidence</td><td>Build infrastructure, health and education</td></tr>
    <tr><td><b>Conditions</b></td><td>Macroeconomic policy reform (deficit, inflation, exchange rate, trade)</td><td>Project and sector reforms, governance</td></tr>
  </table></div>
  <div id="pic2" class="card"></div>
  <div class="tip"><b class="h">Evaluation point</b>The IMF and World Bank may help poorer countries to stabilise and invest, but their conditions can have costs that fall on the poorest. Judge by the type of country, how bad the crisis was, how strict the conditions were and whether the alternatives (default, private borrowing or grants) were better.</div>
'''

watch = '''
  <h2>1 · How debt becomes a burden</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · An IMF loan with conditions</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · The debt service ratio</h2>
  <p>A country owes foreign lenders. Set the debt, the interest rate, the amount repaid each year and its export earnings.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g3b"></div>
    <div class="readout"><div><small>Debt service</small><strong id="r1"></strong></div><div><small>Debt service ratio</small><strong id="r2"></strong></div><div><small>Left for imports</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of export earnings, debt service and the amount left"></svg></div></div></div>

  <h2>Lab 2 · Debt in dollars when the currency falls</h2>
  <p>A government owes $10bn. At first the rate is 10 local units to the dollar, so the debt is 100bn local units against government revenue of 50bn. Move the fall in the currency.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div>
    <div class="readout"><div><small>Exchange rate</small><strong id="t1"></strong></div><div><small>Debt in local currency</small><strong id="t2"></strong></div><div><small>Debt ÷ revenue</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the debt in local currency before and after a fall in the currency"></svg></div></div></div>
'''

practise = '''
  <h2>1 · IMF or World Bank?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the debt trap in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The Latin American debt crisis, 1980s", "Many countries borrowed heavily in dollars in the 1970s. When world interest rates rose sharply and commodity prices fell, they could not repay. The IMF lent on condition of austerity and reforms, and growth and living standards fell in what is often called a lost decade.", "causes of debt, the debt service burden and IMF conditionality.") +
rw("Asian financial crisis, 1997 to 1998", "Several East Asian economies had borrowed short-term in dollars. When their currencies collapsed, the cost of the debt in local money soared. IMF loans came with conditions such as high interest rates and spending cuts, which many argued made the recession deeper.", "the effect of depreciation on foreign-currency debt and criticism of IMF conditions.") +
rw("Debt relief for the poorest", "Under the Heavily Indebted Poor Countries initiative and later programmes, creditors cancelled part of the debts of dozens of the poorest countries on condition that the money saved went to health and education. Some countries saw spending on social services rise.", "debt relief as a solution, with moral hazard as a limit.") +
rw("World Bank infrastructure loans", "The World Bank has lent for projects such as roads, hydropower, water systems and schools in low- and middle-income countries. Where well designed they raise productivity and incomes, but some large projects have been criticised for displacing communities or damaging the environment.", "the World Bank's role in long-term development lending and the costs that can come with it.")
)

mc_exam = [
  ("Which role is performed by the World Bank but not by the International Monetary Fund? (Feb/March 2025 · 32 · Q29, reworded)", ["Facilitating free trade among member countries", "Helping member countries to plan fiscal policy", "Providing bailout packages to countries facing external account problems", "Providing money to member countries to build infrastructure"], 3, "The World Bank lends for long-term development projects. The IMF handles balance of payments support and monetary cooperation."),
  ("What is not a function of the International Monetary Fund? (May/June 2025 · 31 · Q28, reworded)", ["Encouraging exchange rate stability", "Providing financial assistance to a country with failed economic policies", "Providing funds for a water purification plant in a developing country", "Providing loans to countries after a natural disaster"], 2, "Funding specific water projects is a development role of the World Bank."),
  ("What is the role of the International Monetary Fund? (Oct/Nov 2023 · 33 · Q28, reworded)", ["To advise countries with trade disputes", "To help charities providing emergency aid", "To offer short-term help to countries with balance of payments problems", "To provide interest-free credit to developing countries for infrastructure"], 2, "The IMF supports countries with balance of payments difficulties in the short term."),
  ("Low-income countries that asked the IMF for loans usually had to introduce structural adjustment programmes promoting a free-market economy. Which action would be included? (Oct/Nov 2021 · 31 · Q23, reworded)", ["Deregulation of agricultural markets", "Extending food subsidies", "Nationalising the water supply", "Restricting the flow of international capital"], 0, "Structural adjustment promoted markets, privatisation and deregulation, not subsidies, nationalisation or controls."),
  ("Which condition attached to IMF loans would conflict with the infant industry argument? (May/June 2025 · 32 · Q29, reworded)", ["The need to allow free trade", "The need to control inflation", "A contractionary fiscal policy", "The need to privatise state firms"], 0, "The infant industry argument supports temporary protection, which free trade conditions would remove."),
  ("What are the characteristics of most developing economies? Ratio of government debt to GDP, and average propensity to save. (Oct/Nov 2021 · 31 · Q27, reworded)", ["High debt ratio, high propensity to save", "High debt ratio, low propensity to save", "Low debt ratio, high propensity to save", "Low debt ratio, low propensity to save"], 1, "Developing countries often borrow heavily, and low incomes mean little saving.")
]

exam = exam_page("external debt, the IMF and the World Bank",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The IMF appears in a 25 mark discussion of conditions on loans and in data response on debt and growth. Reworded past questions are below, with one practice question and six Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "1", "Oct/Nov 2021 (43) Q7"), ("Data response, 8 marks", "1", "Oct/Nov 2022 (43) Q1(d)"), ("Multiple choice (Paper 3)", "6 shown below", "2021 to 2025")],
  [
  eq("Based on Oct/Nov 2021 · 9708/43 · Q7", "25 marks", "The IMF lends money to developing countries but requires that these countries reduce restrictions on imports, focus on the export of primary goods and accept a devaluation of their currencies. Based on this, assess whether developing countries should continue to borrow from the IMF.",
     ["Examine the likely effect on a developing country of each of the three conditions, and assess whether the negative effects might outweigh the benefits of the loan.",
      "Removing import restrictions may cause balance of payments problems; focusing on primary exports may lead to unstable incomes and low productivity; devaluation may cause cost-push inflation.",
      "Level 4 (18 to 25) analyses each requirement, weighs their combined effect against the benefits of the loan and reaches a conclusion."],
     "Condition 1: free trade. Condition 2: primary exports. Condition 3: devaluation. Benefits of the loan. Judge.",
     [[("k", "The IMF lends to countries with balance of payments difficulties, usually on condition of policy changes. Removing import restrictions could expose infant industries to competition and raise imports, which may worsen the current account in the short run."), ("n", "Focusing on primary exports may leave the economy dependent on volatile prices with low productivity, so incomes could be unstable. A devaluation makes imports dearer and may cause cost-push inflation, especially if the country relies on imported inputs, although it could also make exports more competitive if the Marshall-Lerner condition holds.")],
      [("e", "The loan may still be worth taking. It restores confidence, supplies foreign exchange to pay for essential imports and avoids a default, which could be worse. The answer may depend on how severe the crisis is, whether other sources of finance exist and how flexible the conditions are. Overall, borrowing from the IMF may be reasonable as a last resort, but the conditions suggest that developing countries should try to avoid needing the loan.")]]),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q1(d)", "8 marks", "The IMF encouraged Indonesia to expand its production of palm oil, a major export, to help to solve its external debt problems. To what extent do you agree with this advice?",
     ["In support: the country had external debt problems and palm oil was a big earner of foreign exchange, which could repay debt and raise incomes at home (up to 4 marks).",
      "Against: expansion destroys rainforest; fires add to greenhouse gases and destroy habitats; external costs exceed private costs; dependence on one crop (monoculture) leaves prices influenced by foreign buyers."],
     "For: foreign exchange and incomes. Against: environmental costs and monoculture. Judge.",
     [[("k", "The IMF advice could help the debt problem. Palm oil is a large earner of foreign currency, so higher exports may reduce the current account deficit and provide funds to repay external debt, and may raise rural incomes."), ("e", "However, clearing rainforest creates external costs such as lost habitats and greenhouse gas emissions that may exceed the private benefits. Dependence on one crop also leaves earnings exposed to price falls. So the advice may help in the short run but be less sound for sustainable growth.")]]),
  eq("Practice question · modelled on the 12 mark style (no past paper)", "12 marks", "Explain the causes of a developing country's external debt and consider the consequences of a high debt service ratio.",
     ["Causes: persistent current account deficits, borrowing for investment and government spending, shocks (falling commodity prices, rising interest rates), a falling exchange rate when the debt is in foreign currency, poor management.",
      "Debt service ratio: (interest and repayments) ÷ export earnings; consequences: less foreign exchange for imports, less spending on health and education, austerity, lower investment, a weaker currency and loss of independence.",
      "Judgement: depends on how the borrowed money was used and the size of the ratio."],
     "Causes. Define the ratio. Consequences. Judge.",
     [[("k", "External debt may arise because a developing country has a persistent current account deficit or low saving, so it borrows abroad to invest or to fund the government. Shocks such as a fall in commodity prices, a rise in world interest rates or a fall in the currency (when debt is in dollars) could make the debt harder to repay."), ("n", "The debt service ratio is interest and repayments as a share of export earnings. A high ratio means a large part of foreign exchange earnings goes on the debt, leaving less for imports of capital goods. The government may also cut spending on health and education or raise taxes, which could reduce growth and human capital.")],
      [("e", "The burden could cause the currency to fall and investors to leave, making the debt even costlier. However, if the borrowing was invested in productive assets that raise exports and output, the debt may be manageable. So the consequences may depend on how the funds were used and on how large the ratio is.")]])
  ],
  )

tips = tips_html(
  [("Separate causes and consequences.", "Deficits, shocks and a weaker currency cause debt. Austerity, lower investment and dependence follow."),
   ("Define the ratio.", "Debt service ratio = (interest + repayments) ÷ export earnings."),
   ("Mention foreign-currency debt.", "A fall in the exchange rate raises the cost of debt owed in dollars."),
   ("Split IMF and World Bank.", "IMF: short-term, balance of payments, monetary stability. World Bank: long-term development."),
   ("Name the conditions.", "Cut the deficit, free trade, privatisation, sometimes devaluation."),
   ("Weigh benefits against costs.", "The loan avoids default but conditions may bring austerity and inflation."),
   ("Use the three conditions in 25 marks.", "Analyse each, then compare to the benefits.")],
  [("Debt", "External debt may rise when a country has a persistent current account deficit or when its currency falls."),
   ("Burden", "A high debt service ratio could leave less foreign exchange for imports and less government spending on health and education."),
   ("IMF", "The IMF may provide short-term loans for balance of payments problems, usually with conditions."),
   ("World Bank", "The World Bank provides long-term loans and grants for development projects."),
   ("Judge", "Conditions may reduce growth in the short run but could restore confidence and stability.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Debt burden ---------- */
const DY = (v) => 300 - v * 2.4, DB = [["Start", 100, 15], ["Export prices fall", 70, 15], ["Interest rates rise", 70, 21], ["Currency falls 20%", 70, 26]];
function debtDraw(s) {
  let o = axes(70, 300, 730, 30, "", "$bn a year"); [0, 25, 50, 75, 100].forEach((v) => (o += SV.text(64, DY(v) + 4, v, "sm", { "text-anchor": "end" })));
  DB.forEach(([l, ex, ds], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 110 + i * 150; o += SV.rect(x, DY(ex * k), 50, ex * k * 2.4, "f1", op(0.75)) + SV.rect(x + 56, DY(ds * k), 50, ds * k * 2.4, "f2", op(0.75)) + tag(x + 25, DY(ex * k) - 6, ex, "t1", k, "middle") + tag(x + 81, DY(ds * k) - 6, ds, "t2", k, "middle") + tag(x + 53, 320, l, "sm", k, "middle") + tag(x + 53, DY(ex * k) - 24, "ratio " + Lib.fmtN(ds / ex * 100, 0) + "%", "t4", k, "middle"); });
  o += SV.rect(520, 330, 10, 10, "f1", op(0.75)) + SV.text(536, 339, "Export earnings", "sm") + SV.rect(640, 330, 10, 10, "f2", op(0.75)) + SV.text(656, 339, "Debt service", "sm");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Export earnings and debt service over four stages with the debt service ratio rising from 15 to 37 percent">${debtDraw({ n: 4 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 350, label: "Export earnings and debt service: the debt service ratio rises after shocks", base: { n: 0 }, draw: debtDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Start.</b> Export earnings are $100bn and debt service (interest plus repayments) is $15bn: a debt service ratio of 15%.", s: { n: 1 } },
  { cap: "<b>Export prices fall.</b> A drop in the world price of the main export cuts earnings to $70bn. The debt service is unchanged, so the ratio rises to 21%.", s: { n: 2 } },
  { cap: "<b>Interest rates rise.</b> If part of the debt has variable interest, debt service rises to $21bn: a ratio of 30%.", s: { n: 3 } },
  { cap: "<b>The currency falls.</b> The debt is in dollars, so a 20% fall in the currency raises the debt service in local terms and the ratio climbs to 37%. Less is left for imports, health and education.", s: { n: 4 } },
] });

/* ---------- IMF loan flow ---------- */
function imfDraw(s) {
  const box = (x, y, w, h, t, c, k) => { if (k <= 0) return ""; const L = t.split("|"); return SV.rect(x, y, w, h, c, op(0.5 * k)) + L.map((ln, i) => SV.text(x + w / 2, y + h / 2 - (L.length - 1) * 8 + i * 16 + 5, ln, "lbl bd", { "text-anchor": "middle", ...op(k) })).join(""); };
  const ar = (x1, y1, x2, y2, d, k) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, d, "dot1") : "");
  let o = box(20, 115, 130, 70, "Balance of|payments crisis", "f2", s.a);
  o += ar(150, 150, 190, 150, "r", s.b) + box(190, 115, 130, 70, "IMF short-term|loan", "f1", s.b);
  o += ar(320, 150, 360, 150, "r", s.c) + box(360, 95, 150, 110, "Conditions:|cut the deficit,|free trade, devalue", "f3", s.c);
  o += ar(510, 150, 550, 150, "r", s.d) + box(550, 40, 190, 80, "Benefits: confidence|and stability", "f1", s.d) + box(550, 180, 190, 80, "Costs: austerity,|inflation, unemployment", "f2", s.d);
  if (s.d > 0) o += ar(530, 130, 550, 85, "r", s.d) + ar(530, 170, 550, 215, "r", s.d);
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A balance of payments crisis, an IMF loan, conditions and the resulting benefits and costs">${imfDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "From a balance of payments crisis to an IMF loan with conditions and their effects", base: { a: 0, b: 0, c: 0, d: 0 }, draw: imfDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>The crisis.</b> Foreign exchange reserves run low, the currency is under attack and lenders refuse to lend.", s: { a: 1 } },
  { cap: "<b>The IMF steps in</b> with a short-term loan so the country can pay for essential imports and meet its foreign debts.", s: { a: 1, b: 1 } },
  { cap: "<b>Conditions.</b> The loan comes with structural adjustment: cut the budget deficit, reduce import restrictions, privatise and often devalue the currency.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Effects.</b> Confidence and stability may return, but austerity can raise unemployment, and devaluation can raise import prices. The net effect depends on how severe the crisis was.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labD() {
  if (!$("#db") || !$("#ir") || !$("#rp") || !$("#ex")) return;
  const d = +$("#db").value, r = +$("#ir").value / 10, rep = +$("#rp").value, ex = +$("#ex").value, ds = d * r / 100 + rep, ratio = ds / ex * 100;
  $("#r1").textContent = "$" + Lib.fmtN(ds, 1) + "bn"; $("#r2").textContent = Lib.fmtN(ratio, 1) + "%"; $("#r3").textContent = "$" + Lib.fmtN(ex - ds, 1) + "bn";
  $("#rv").textContent = `Debt service = interest ($${Lib.fmtN(d * r / 100, 1)}bn) + repayments ($${rep}bn) = $${Lib.fmtN(ds, 1)}bn, which is ${Lib.fmtN(ratio, 1)}% of export earnings of $${ex}bn. ${ratio > 30 ? "This is a very heavy burden: little foreign exchange is left for imports, and the country is likely to need rescheduling or relief." : ratio > 20 ? "This ratio is high by many standards, so a fall in export earnings could create a crisis." : "This ratio looks manageable, though it would rise if exports fell or rates rose."}`;
  const Y = (v) => 270 - v * 1.1; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$bn", "sm");
  [["Exports", ex, "f1"], ["Debt service", ds, "f2"], ["Left over", Math.max(0, ex - ds), "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 230)); o += SV.rect(x, yy, 80, 270 - yy, c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "db", label: "External debt, $bn ", min: 20, max: 150, step: 5, value: 100, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "ir", label: "Interest rate, % ", min: 10, max: 120, step: 5, value: 50, fmt: (v) => (v / 10).toFixed(1) + "%", onInput: labD });
Lib.slider($("#g3"), { id: "rp", label: "Repayments of principal, $bn a year ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3b"), { id: "ex", label: "Export earnings, $bn ", min: 30, max: 200, step: 5, value: 100, fmt: (v) => v, onInput: labD });
labD();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#cf")) return;
  const f = +$("#cf").value / 100, rate = 10 / (1 - f), debt = 10 * rate, ratio = debt / 50;
  $("#t1").textContent = Lib.fmtN(rate, 1) + " per $"; $("#t2").textContent = Lib.fmtN(debt, 0) + "bn"; $("#t3").textContent = Lib.fmtN(ratio, 2) + " times";
  $("#tv").textContent = f === 0 ? "At 10 local units per dollar, $10bn of debt is 100bn local units, twice annual government revenue of 50bn." : `A ${Lib.fmtN(f * 100, 0)}% fall in the currency takes the rate to ${Lib.fmtN(rate, 1)} units per dollar. The dollar debt of $10bn is now ${Lib.fmtN(debt, 0)}bn in local units, ${Lib.fmtN(ratio, 2)} times government revenue, even though the government has borrowed nothing more.`;
  const Y = (v) => 270 - v * 0.9; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Local currency, bn", "sm");
  [["Revenue", 50, "f1"], ["Debt before", 100, "f1"], ["Debt after", debt, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 270)); o += SV.rect(x, yy, 80, 270 - yy, c, op(i === 1 ? 0.5 : 0.85)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, Lib.fmtN(v, 0), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "cf", label: "Fall in the currency against the dollar, % ", min: 0, max: 60, step: 5, value: 25, fmt: (v) => v + "%", onInput: labC });
labC();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "IMF or World Bank?", ["IMF", "World Bank"],
  [("Short-term loan to a country short of foreign exchange", 0), ("Long-term loan to build a road network", 1), ("Promotes exchange rate stability", 0), ("Loans and grants through the IBRD and IDA", 1), ("Attaches conditions such as cutting the budget deficit", 0), ("Funds schools, clinics and water supplies", 1), ("Surveillance of members' economic policies", 0), ("Aims mainly at reducing poverty and long-term development", 1)],
  "IMF: monetary stability and balance of payments. World Bank: long-term development projects.") + MATCH([
  ["External debt", "Money owed by residents of a country to foreign lenders"],
  ["Debt service ratio", "Interest plus repayments as a percentage of export earnings"],
  ["Conditionality", "Policy changes a lender requires in return for a loan"],
  ["Debt relief", "Cancelling or reducing a country's debt"],
  ["Structural adjustment", "Market-oriented reforms required by the IMF"],
  ["Moral hazard", "Debt relief may encourage irresponsible borrowing later"]]) + ORDER(
  "Put the debt trap in order.",
  ["A country borrows in dollars", "Export prices fall or interest rates rise", "The currency falls, so the debt costs more in local currency", "More is spent on debt service and less on health and education", "Growth slows, making the debt harder to repay"],
  "A cycle: heavy debt, less investment, weaker growth, heavier debt.") + CALC([
  {"q": "Debt service is $8bn and export earnings are $40bn. Calculate the debt service ratio (%).", "a": 20, "unit": "%", "tol": 0.5, "hint": "8 ÷ 40.", "sol": "<b>20%</b>."},
  {"q": "A country owes $60bn and its GDP is $150bn. Calculate the debt-to-GDP ratio (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "60 ÷ 150.", "sol": "<b>40%</b>."},
  {"q": "A government owes $8bn. The exchange rate rises from 10 to 12.5 local units per dollar. By how much does the debt rise in local currency (bn units)?", "a": 20, "unit": "bn", "tol": 0.5, "hint": "8 × 12.5 − 8 × 10.", "sol": "100 − 80 = <b>20bn</b> local units."},
  {"q": "Interest on a $100bn debt at 5% is added to $10bn of repayments. Export earnings are $100bn. Calculate the debt service ratio (%).", "a": 15, "unit": "%", "tol": 0.5, "hint": "(5 + 10) ÷ 100.", "sol": "<b>15%</b>."}]) + MCQ([
  ("The debt service ratio is:", ["Interest and repayments as a % of export earnings", "Debt as a % of GDP", "Exports as a % of imports", "Aid as a % of GNI"], 0, "It shows how much foreign exchange earnings are used to service debt."),
  ("The IMF mainly:", ["Lends short term to countries with balance of payments problems", "Builds roads", "Sets tariffs", "Pays for schools"], 0, "It supports monetary stability and the balance of payments."),
  ("The World Bank mainly provides:", ["Long-term loans and grants for development", "Short-term loans for currency crises only", "Exchange rate fixes", "Tax advice"], 0, "It focuses on development and poverty reduction."),
  ("Debt owed in dollars becomes more expensive in local currency when:", ["The local currency falls", "The local currency rises", "Exports rise", "Inflation falls"], 0, "More local currency is needed to buy each dollar."),
  ("A possible cost of IMF conditions is:", ["Austerity and higher unemployment", "Larger reserves", "No change in policy", "Cheaper imports in all cases"], 0, "Cutting the deficit can reduce demand.")
], "qz1") + CARDS([
  ("External debt", "Owed to foreign lenders."),
  ("Debt service ratio", "(Interest + repayments) ÷ exports."),
  ("IMF", "Short-term BoP help; monetary stability."),
  ("World Bank", "Long-term development loans and grants."),
  ("Conditionality", "Policy conditions on loans."),
  ("Structural adjustment", "Free-market reforms."),
  ("Debt relief", "Cancelling debt; moral hazard risk."),
  ("Debt trap", "Debt, weak growth, more debt.")]) + MCQ(mc_exam)

build("sy1155", "external-debt-imf-world-bank", "External Debt, the IMF and the World Bank", EY,
  "11.5.5 to 11.5.7: why countries build up external debt, the consequences of a high debt burden, and the roles of the IMF and the World Bank. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
