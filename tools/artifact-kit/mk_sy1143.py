"""Syllabus 11.4.3 Economic structure: employment composition and the pattern of trade. Run: python3 tools/artifact-kit/mk_sy1143.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.4.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>As an economy develops, <b class="kw">employment shifts from the primary sector</b> (farming, mining, fishing) <b>to the secondary sector</b> (manufacturing and construction) <b>and then to the tertiary sector</b> (services), because farming productivity rises and the demand for manufactures and services grows faster than the demand for food. The <b class="kw">pattern of trade</b> changes too: low-income countries <b>export primary products and import manufactures</b>, newly industrialising countries export labour-intensive manufactures, and high-income countries export capital-intensive goods and services. Dependence on a few primary exports exposes a country to <b>price volatility and a long-run fall in its terms of trade</b>, which is why many governments try to <b>diversify</b>.</p></div>

  <h2>1 · Employment composition by sector</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Sector</th><th>Activities</th><th>Typical share of employment</th></tr>
    <tr><td><b>Primary</b></td><td>Agriculture, forestry, fishing, mining and oil extraction</td><td>Large in low-income countries (often over half), tiny in high-income countries</td></tr>
    <tr><td><b>Secondary</b></td><td>Manufacturing, construction, utilities</td><td>Rises in the middle of development, then flattens or falls (de-industrialisation)</td></tr>
    <tr><td><b>Tertiary</b></td><td>Retail, banking, health, education, tourism and other services</td><td>Small in low-income countries, largest by far in high-income countries</td></tr>
  </table></div>
  <h3>Why the shares change</h3>
  <ul>
    <li><b>Rising farm productivity</b> (better seeds, machinery, irrigation) means fewer workers are needed on the land, so labour is released to other sectors.</li>
    <li><b>Income elasticity of demand:</b> as incomes rise, spending on food rises slowly (it is a necessity, income inelastic: Engel's law), while spending on manufactures and especially services rises faster (income elastic). Output and jobs follow demand.</li>
    <li><b>Urbanisation and investment</b> in infrastructure, education and technology make non-farm jobs more productive and attractive.</li>
    <li>In rich countries <b>automation and offshoring</b> have reduced manufacturing jobs while services grow, which is sometimes called de-industrialisation.</li>
  </ul>
  <ul>
    <li><b>Implications:</b> moving workers from low-productivity farming to higher-productivity industry and services raises average output per worker (structural change contributes to growth). But rapid shifts can cause <b>structural unemployment</b> and a large <b>informal sector</b> if jobs are not created fast enough.</li>
  </ul>

  <h2>2 · The pattern of trade at different levels of development</h2>
  <div class="tw"><table class="t">
    <tr><th>Level of development</th><th>Main exports</th><th>Main imports</th><th>Features</th></tr>
    <tr><td><b>Low-income</b></td><td>Primary products: crops, minerals, oil, raw materials; some basic textiles</td><td>Manufactures, machinery, fuel, food (some)</td><td>Few exports, narrow range, volatile earnings, dependence on a few buyers</td></tr>
    <tr><td><b>Emerging and newly industrialised</b></td><td>Labour-intensive manufactures (clothing, electronics assembly), then more complex goods</td><td>Capital goods, technology, raw materials and energy</td><td>Fast growth in exports and in the share of manufactures</td></tr>
    <tr><td><b>High-income</b></td><td>Capital- and skill-intensive manufactures, high technology, services (finance, design, software)</td><td>Raw materials, energy, labour-intensive goods</td><td>Wide variety; large intra-industry trade (similar goods both ways)</td></tr>
  </table></div>
  <ul>
    <li>Most trade by value is among high-income countries and between rich and poor (North-South). Trade among developing countries (South-South) has been growing, especially with China and other emerging economies.</li>
    <li><b>Comparative advantage</b> explains specialisation: land and labour-rich countries export primary and labour-intensive goods; capital- and skill-rich countries export capital- and knowledge-intensive goods.</li>
  </ul>

  <h2>3 · Dependence on primary exports: the problems</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Price volatility:</b> demand for many primary goods is <b>income and price inelastic</b> and supply is <b>unpredictable (weather, harvests)</b>. Small shifts in supply or demand cause large price swings, so export earnings, farmers' incomes, tax revenue and investment fluctuate.</li>
    <li><b>Long-run decline in the terms of trade (Prebisch-Singer):</b> as world incomes rise, demand for manufactures grows faster than for primary goods, so primary prices tend to fall relative to manufactured prices. Terms of trade = (index of export prices ÷ index of import prices) × 100. A fall means a country must export more to buy the same imports.</li>
    <li><b>Low value added and limited linkages:</b> few jobs and little technology transfer compared with manufacturing.</li>
    <li><b>Dutch disease</b> and resource dependence: a booming natural resource sector can raise the exchange rate and hurt other exports.</li>
    <li><b>Policies:</b> diversify into manufactures and services, add value locally (processing), invest in education and infrastructure, stabilise prices (buffer stocks, hedging), use trade agreements and export-led growth, and protect infant industries temporarily. Each has costs and time lags.</li>
  </ul>
  <div class="tip"><b class="h">Evaluation point</b>Reliance on primary products is a cause of low growth in many developing countries, but it is not the only one: low investment, poor infrastructure, weak education, conflict and governance also matter, and some countries with primary exports have grown strongly. Also, rich resource exporters (such as oil producers) can have high incomes, so the answer depends on the product and the policy.</div>
'''

watch = '''
  <h2>1 · Employment shifts as incomes rise</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stE"></div>
  <h2>2 · Volatile primary prices and falling terms of trade</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab 1 · The terms of trade</h2>
  <p>Terms of trade = (export price index ÷ import price index) × 100, starting at 100. Change the two price indices and see the terms of trade and how much extra must be exported to buy the same imports.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Terms of trade</small><strong id="r1"></strong></div><div><small>Change</small><strong id="r2"></strong></div><div><small>Exports needed per unit imported</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the export price index, the import price index and the terms of trade"></svg></div></div></div>

  <h2>Lab 2 · What does the structure suggest?</h2>
  <p>Set the share of workers in the primary and secondary sectors. The rest are in services. See the pattern and which group it most resembles.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Tertiary share</small><strong id="t1"></strong></div><div><small>Looks most like</small><strong id="t2"></strong></div><div><small>Typical exports</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="A stacked bar of primary, secondary and tertiary employment shares"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which sector?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the chain from higher incomes to a shift in jobs in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Coffee, cocoa and copper", "Countries that depend on one or two crops or minerals see their export earnings rise and fall with world prices. When coffee or copper prices drop sharply, farm incomes, government revenue and the exchange rate all fall, which makes planning and investment hard.", "price volatility and why diversification is a common policy aim.") +
rw("South Korea and Taiwan", "Both economies moved from agriculture and light industry to electronics, ships, cars and later services, with exports of manufactures driving growth. The share of workers in farming fell sharply over a few decades while productivity and incomes rose.", "structural change and export-led growth as part of development.") +
rw("Bangladesh and garments", "Bangladesh has built a large clothing industry, which now supplies most of its exports and employs millions of workers, many of them women. It moved the economy away from agriculture, though it depends heavily on a single sector and on buyers in rich countries.", "a pattern of trade at an early stage of industrialisation, with the risk of dependence.") +
rw("Oil exporters and diversification", "Many oil-exporting countries have high incomes but rely on oil for most export revenue and government income. Plans to build tourism, finance and manufacturing aim to reduce the exposure to oil price swings.", "resource dependence versus diversification, and why income and development can differ.")
)

mc_exam = [
  ("Which is the most accurate statement about developing economies? (Oct/Nov 2020 · 33 · Q20, reworded)", ["Dependence on primary products for export revenue leaves them reliant on the industrialised world for manufactured goods", "High capital per head means they must trade to grow", "High real GDP per head and high population growth reduce their ability to raise living standards", "Migration from rural to urban areas matters only if it causes labour shortages in rural areas"], 0, "Developing countries often export primary goods and import manufactures. Capital per head is low, and the other statements are not accurate."),
  ("In a developing economy, which policy is most likely to increase the rate of growth but restrict economic development? (Oct/Nov 2021 · 32 · Q28, reworded)", ["More health care provision", "A higher school leaving age", "Removing health and safety regulations", "Promoting export-led growth"], 2, "Removing safety rules may cut costs and raise output, but worsens working conditions and health, so well-being does not improve."),
  ("The current account of the balance of payments moves into deficit. What is a possible reason? (Feb/March 2025 · 32 · Q22, reworded)", ["A decrease in tax revenue", "Export-led growth", "Repaying debts to other countries", "The import of new technology"], 3, "Imports of new technology raise import spending, which can cause a deficit. Export-led growth and debt repayments do not directly add to the current account deficit."),
  ("A low-income economy heavily dependent on primary products receives a car factory built by a foreign company. What will not be a long-lasting benefit? (Oct/Nov 2022 · 31 · Q27, reworded)", ["The company introduces new technology", "The company diversifies the economy's production", "The company provides skills training for local workers", "The company buys non-renewable local construction materials"], 3, "Using up non-renewable materials is a one-off, not a lasting benefit. The other three improve productivity and diversification."),
  ("What has not accompanied global economic growth over the last 25 years? (Oct/Nov 2023 · 32 · Q26, reworded)", ["A depletion of non-renewable resources", "A decrease in international trade", "Growing urbanisation", "More atmospheric pollution"], 1, "International trade has expanded."),
  ("The table shows urbanisation rates for more developed (75% to 86%), less developed (45% to 66%) and least developed (29% to 55%) regions between 2010 and 2050. Which relationship can be confirmed? (May/June 2023 · 31 · Q29, reworded)", ["The least developed regions have the largest urban populations in both years", "The more developed regions have the lowest growth rate of urbanisation between 2010 and 2050", "The largest region in 2010 will have the fastest population growth", "The region with the largest urban population in 2010 will have the highest urbanisation by 2050"], 1, "Urbanisation is already high in more developed regions, so it rises by only 11 points, against 21 and 26 elsewhere.")
]

exam = exam_page("economic structure, primary exports and export-led growth",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Reliance on primary products and export-led growth appear in 12 and 25 mark essays, and the changing structure of employment is tested in Paper 3. Reworded past questions are below, with six Paper 3 multiple choice questions.",
  [("Essays, 25 marks", "2", "Feb/March 2022 (42) Q5; May/June 2022 (41) Q5(a)"), ("Essay part, 12 marks", "1", "Oct/Nov 2022 (43) Q5(a)"), ("Multiple choice (Paper 3)", "6 shown below", "2020 to 2025")],
  [
  eq("Based on Feb/March 2022 · 9708/42 · Q5", "25 marks", "Many developing countries rely heavily on the production and export of primary products. This is the main cause of low growth in developing countries and therefore the main explanation for their low standard of living. Discuss the extent to which you agree.",
     ["Three elements: first, many developing countries do rely on primary products, which have inelastic demand (food is a necessity) and supply that varies with the weather, giving price and income volatility.",
      "Second, reliance on primary goods with small secondary and tertiary sectors links to low growth through low investment and low productivity in the primary sector, and low saving from low incomes.",
      "Third, other factors may contribute (for example education and training), and the link between growth and living standards is not automatic: high growth can reduce living standards (negative externalities), and living standards depend on more than goods and services (use alternative measures).",
      "Level 4 (18 to 25) analyses the links and assesses how far each is supported, with a conclusion."],
     "Primary dependence and volatility. Link to low growth (investment and productivity). Other causes of low growth. Growth versus living standards. Conclude.",
     [[("k", "Many developing countries rely on primary products. Demand for food and raw materials is inelastic and supply varies with the weather, so prices and export earnings are volatile."), ("n", "Volatile income may discourage investment, and low incomes in the primary sector mean low saving and low productivity, which could keep growth low. Over the long run the terms of trade could fall as demand for manufactures grows faster than demand for primary goods. Low growth then limits the rise in incomes and so living standards.")],
      [("e", "However, this may not be the main cause. Low levels of education and training, weak infrastructure, poor governance and conflict also reduce growth, and some countries with primary exports have grown quickly. In addition, the link from growth to living standards is not automatic, because the gains may be unequally shared and growth can damage the environment, and living standards depend on health and education as well as income. So primary dependence is probably an important but not the only cause.")]]),
  eq("Based on May/June 2022 · 9708/41 · Q5", "25 marks", "With the help of a circular flow diagram, discuss how a policy of export-led growth might affect the standard of living in a developing economy.",
     ["Export-led growth uses an outward-looking strategy relying on openness and trade; a successful policy raises national income, output and employment.",
      "Circular flow diagram with all injections and withdrawals: an increase in exports (an injection) raises output and income by a multiple through the multiplier, so real GDP per head rises and access to goods and services improves.",
      "Evaluation: a developing economy is likely to rely on primary goods with income-inelastic demand and volatile supply, so the growth effect may be small; the effect on living standards depends on the distribution of income, loss of leisure and effects on long-term growth of focusing on primary products."],
     "Define export-led growth. Circular flow diagram: exports as an injection, with a multiplier. Standard of living. Primary goods and volatility. Distribution. Conclude.",
     [[("k", "Export-led growth is a strategy of expanding output for sale abroad. In the circular flow, exports are an injection, so the national income equilibrium moves to a higher level, with a multiplier effect that raises output, employment and income by more than the original rise in exports."), ("n", "Higher real GDP per head could give people access to more goods and services, so the material standard of living may rise. Extra export earnings also help to pay for imported capital goods and technology, which may raise productivity.")],
      [("e", "However, a developing economy may export mainly primary goods with income-inelastic demand and volatile prices, so the gain in income may be small and unstable. The standard of living also depends on how the extra income is distributed, on working conditions and on the environment, so exports could raise GDP without much improvement for the poorest.")]]),
  eq("Based on Oct/Nov 2022 · 9708/43 · Q5(a)", "12 marks", "Consider, with the help of a circular flow diagram, why an export-led growth policy is likely to be successful when a developed economy is in a recession.",
     ["Describe export-led growth and show on a labelled circular flow diagram an increase in injections (exports), with a larger effect on output, income and employment through the multiplier.",
      "Recession: GDP falling for two successive quarters, rising unemployment from falling aggregate demand.",
      "Compare alternatives: lower interest rates may be ineffective with low confidence, and higher government spending is limited if public debt is high; a policy that boosts exports avoids those problems and may protect the currency and the balance of payments; its success depends on the exchange rate regime and policy used, for example lowering interest rates to depreciate a floating currency."],
     "Diagram with exports as an injection. Recession and unemployment. Why it beats other policies when rates are low and debt is high. Depends on exchange rate.",
     [[("k", "In a recession, falling aggregate demand reduces output and raises unemployment. Export-led growth boosts demand from abroad: in the circular flow exports are an injection, so national income, output and employment increase through the multiplier."), ("n", "Other policies may be limited in a recession. Lower interest rates may not work if confidence is low, and a larger budget deficit may be hard to finance if debt is already high. Raising exports does not depend on domestic confidence or on public borrowing, and it improves the balance of payments.")],
      [("e", "It is more likely to succeed if the exchange rate can fall, for example in a floating system after interest rate cuts, and if trading partners are growing. If they are also in recession, demand for exports may be weak.")]])
  ],
  )

tips = tips_html(
  [("Name the three sectors.", "Primary, secondary and tertiary, and what each includes."),
   ("Explain why the shares change.", "Farm productivity, income elasticity (Engel's law) and technology."),
   ("Compare patterns of trade.", "Low-income: primary exports. Newly industrialised: manufactures. High-income: capital goods and services."),
   ("Give the volatility reason.", "Inelastic demand plus supply that varies with the weather means price swings."),
   ("Quote the terms of trade.", "(Export prices ÷ import prices) × 100. A fall is a deterioration."),
   ("Use the circular flow for exports.", "Exports are an injection. Show the multiplier effect on income."),
   ("Evaluate the link to living standards.", "Growth may not reach the poor; other factors also matter.")],
  [("Structure", "As incomes rise, employment could shift from the primary sector to manufacturing and then to services."),
   ("Engel", "Demand for food is income inelastic, so spending on manufactures and services may grow faster as incomes rise."),
   ("Primary", "Dependence on primary exports may expose a country to price volatility and a falling terms of trade."),
   ("Terms of trade", "A deterioration in the terms of trade means a country may have to export more to buy the same imports."),
   ("Diversify", "Diversification could reduce exposure to the price of a single commodity.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Employment shares ---------- */
const ES = [["Low", [65, 10, 25]], ["Lower-middle", [40, 20, 40]], ["Upper-middle", [20, 28, 52]], ["High", [3, 20, 77]]], EC = ["f2", "f1", "f3"], EN = ["Primary", "Secondary", "Tertiary"];
function empDraw(s) {
  let o = SV.line(70, 290, 730, 290) + SV.line(70, 290, 70, 30) + SV.text(76, 24, "Share of employment (%)", "sm"); [0, 50, 100].forEach((v) => (o += SV.text(64, 290 - v * 2.4 + 4, v, "sm", { "text-anchor": "end" })));
  ES.forEach(([g, v], i) => { const k = Math.max(0, Math.min(1, s.i - i)); if (k <= 0) return; let c = 0; v.forEach((p, j) => { const h = p * 2.4 * k; o += SV.rect(130 + i * 155, 290 - c * 2.4 * k - h, 100, h, EC[j], op(0.75)); if (p >= 8) o += SV.text(180 + i * 155, 290 - c * 2.4 * k - h / 2 + 5, p + "%", "lbl bd", { "text-anchor": "middle", ...op(k) }); c += p; }); o += SV.text(180 + i * 155, 312, g + " income", "sm", { "text-anchor": "middle", ...op(k) }); });
  EN.forEach((n, j) => { o += SV.rect(520 + j * 70, 332 - 0, 10, 10, EC[j], op(0.75)) + SV.text(534 + j * 70, 341, n, "sm"); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Stacked bars of employment shares in the primary, secondary and tertiary sectors for low, lower-middle, upper-middle and high-income countries">${empDraw({ i: 4 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 350, label: "Employment shares by sector in four income groups", base: { i: 0 }, draw: empDraw, tween: 1200, dwell: 5600, steps: [
  { cap: "<b>Low income.</b> About 65% of workers are in the primary sector, mostly farming, with productivity low.", s: { i: 1 } },
  { cap: "<b>Lower-middle income.</b> Farm productivity rises, labour is released, and manufacturing and services grow: primary falls to about 40%.", s: { i: 2 } },
  { cap: "<b>Upper-middle income.</b> The secondary sector peaks (about 28%) while services take over as the main source of jobs.", s: { i: 3 } },
  { cap: "<b>High income.</b> The primary share is tiny (3%), manufacturing falls back (de-industrialisation) and services employ over three quarters. (Illustrative typical values.)", s: { i: 4 } },
] });

/* ---------- Commodity prices and terms of trade ---------- */
const CP = [100, 118, 95, 122, 90, 108, 84, 96, 80], MP = [100, 102, 105, 107, 110, 113, 116, 119, 122], TX = (i) => 90 + i * 76, TY = (v) => 300 - (v - 60) * 3.4;
function totDraw(s) {
  let o = axes(70, 300, 730, 30, "Time (years)", "Price index"); [60, 80, 100, 120].forEach((v) => (o += SV.text(64, TY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TY(v), 730, TY(v), "gr", op(0.3))));
  const ln = (arr, c, k) => { const n = Math.max(0, Math.min(8, k * 8)), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([TX(i), TY(arr[i])]); if (n % 1 > 0 && Math.floor(n) < 8) { const a = Math.floor(n), f = n - a; pts.push([TX(a + f), TY(arr[a] + (arr[a + 1] - arr[a]) * f)]); } return pts.length > 1 ? SV.path(Lib.ptsPath(pts), c) : ""; };
  o += ln(CP, "c2", s.a) + (s.a > 0 ? tag(TX(8) + 6, TY(CP[8]) - 18, "Commodity price index", "t2", s.a, "end") : "");
  if (s.b > 0) o += ln(MP, "c1", s.b) + tag(TX(8) + 6, TY(MP[8]) - 8, "Manufactures price index", "t1", s.b, "end");
  if (s.c > 0) { const tt = CP.map((v, i) => v / MP[i] * 100); o += ln(tt, "c4 dash", s.c) + tag(TX(8) - 10, TY(tt[8]) - 12, "Terms of trade: " + Lib.fmtN(tt[8], 0), "t4", s.c, "end"); }
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 345, label: "A primary commodity price index swinging, manufactured prices rising steadily and the terms of trade falling", base: { a: 0, b: 0, c: 0 }, draw: totDraw, tween: 1500, dwell: 5800, steps: [
  { cap: "<b>Volatile prices.</b> Demand for a primary good is inelastic and its supply changes with the weather, so the price swings widely from year to year, with no clear rise over time.", s: { a: 1 } },
  { cap: "<b>Manufactures</b> are priced steadily and tend to rise as technology and brand strength keep prices up.", s: { a: 1, b: 1 } },
  { cap: "<b>The terms of trade</b> (commodity prices ÷ manufacture prices × 100) fall from 100 to about 66. The country must now export about 50% more to pay for the same imports.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#xp") || !$("#mp")) return;
  const x = +$("#xp").value, m = +$("#mp").value, tot = x / m * 100, need = m / x;
  $("#r1").textContent = Lib.fmtN(tot, 1); $("#r2").textContent = (tot >= 100 ? "+" : "") + Lib.fmtN(tot - 100, 1) + "%"; $("#r3").textContent = Lib.fmtN(need, 2) + " units";
  $("#rv").textContent = tot < 99.5 ? `The terms of trade have deteriorated to ${Lib.fmtN(tot, 1)}: import prices have risen more (or export prices fallen more) than the other. The country needs ${Lib.fmtN(need, 2)} units of exports to buy each unit of imports it used to get for 1 unit.` : tot > 100.5 ? `The terms of trade have improved to ${Lib.fmtN(tot, 1)}: each unit of exports now buys more imports, about ${Lib.fmtN(1 / need, 2)} units.` : "The terms of trade are unchanged, so each unit of exports buys the same amount of imports.";
  const Y = (v) => 270 - v * 1.25; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Index", "sm");
  [["Export prices", x, "f1"], ["Import prices", m, "f2"], ["Terms of trade", tot, "f3"]].forEach(([l, v, c], i) => { const px = 60 + i * 115, y = Y(Math.min(v, 200)); o += SV.rect(px, y, 80, 270 - y, c) + SV.text(px + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(px + 40, y - 6, Lib.fmtN(v, 0), "t1", 1, "middle"); });
  $("#labA").innerHTML = o + SV.line(40, Y(100), 400, Y(100), "gr dash");
}
Lib.slider($("#g1"), { id: "xp", label: "Export price index (base 100) ", min: 50, max: 160, step: 5, value: 80, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "mp", label: "Import price index (base 100) ", min: 60, max: 160, step: 5, value: 110, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labS() {
  if (!$("#sp") || !$("#ss")) return;
  const p = +$("#sp").value; let sec = +$("#ss").value; if (p + sec > 98) sec = 98 - p; const ter = 100 - p - sec, grp = p >= 50 ? "Low-income" : p >= 30 ? "Lower-middle income" : p >= 12 ? "Upper-middle income" : "High-income", ex = p >= 50 ? "Primary products" : p >= 30 ? "Primary and simple manufactures" : p >= 12 ? "Manufactures" : "Capital goods and services";
  $("#t1").textContent = ter + "%"; $("#t2").textContent = grp; $("#t3").textContent = ex;
  $("#tv").textContent = `With ${p}% in the primary sector, ${sec}% in the secondary sector and ${ter}% in services, this structure looks most like a ${grp.toLowerCase()} economy. A high primary share usually means low-productivity farming and exports of primary goods; a large services share is typical of high-income countries. These are tendencies, not rules: oil exporters can be rich with a large primary sector.`;
  const X = (v) => 40 + v * 3.4; let o = SV.line(40, 200, 400, 200) + SV.text(40, 20, "Share of employment (%)", "sm");
  [["Primary", p, "f2"], ["Secondary", sec, "f1"], ["Tertiary", ter, "f3"]].forEach(([l, v, c], i, arr) => { const x0 = arr.slice(0, i).reduce((a, q) => a + q[1], 0); o += SV.rect(X(x0), 120, v * 3.4, 80, c, op(0.7)) + (v > 6 ? SV.text(X(x0 + v / 2), 164, v + "%", "lbl bd", { "text-anchor": "middle" }) : "") + SV.text(X(x0 + v / 2), 220 + i * 18, l, "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "sp", label: "Primary sector share, % ", min: 2, max: 80, step: 1, value: 40, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g4"), { id: "ss", label: "Secondary sector share, % ", min: 5, max: 40, step: 1, value: 20, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which sector is it?", ["Primary", "Secondary", "Tertiary"],
  [("Growing coffee", 0), ("Assembling cars in a factory", 1), ("A bank branch", 2), ("Copper mining", 0), ("Building houses", 1), ("A hotel and tourism business", 2), ("Fishing", 0), ("A software firm", 2)],
  "Primary: extraction and farming. Secondary: making and building. Tertiary: services.") + MATCH([
  ["Primary sector", "Farming, fishing, forestry and mining"],
  ["De-industrialisation", "A fall in the share of manufacturing in output or jobs"],
  ["Terms of trade", "Export price index divided by import price index, times 100"],
  ["Engel's law", "As incomes rise, the share spent on food falls"],
  ["Diversification", "Spreading production and exports across more products"],
  ["Intra-industry trade", "Two-way trade in similar goods between countries"]]) + ORDER(
  "Put the chain from higher incomes to a shift in jobs in order.",
  ["Incomes rise", "Spending on food rises slowly but spending on manufactures and services rises faster", "Demand for non-farm output grows", "Farm productivity rises so fewer farm workers are needed", "Labour moves from the primary sector to industry and services"],
  "Income elasticity and productivity both push labour out of farming.") + CALC([
  {"q": "Export prices rise from 100 to 108 and import prices rise from 100 to 120. Calculate the terms of trade index.", "a": 90, "unit": "", "tol": 0.5, "hint": "108 ÷ 120 × 100.", "sol": "<b>90</b>: a deterioration of 10%."},
  {"q": "A country's terms of trade fall from 100 to 80. By what percentage have they fallen (%)?", "a": 20, "unit": "%", "tol": 0.5, "hint": "20 ÷ 100.", "sol": "<b>20%</b>."},
  {"q": "Of 40 million workers, 14 million work in agriculture. Calculate the share of employment in the primary sector (%).", "a": 35, "unit": "%", "tol": 0.5, "hint": "14 ÷ 40.", "sol": "<b>35%</b>."},
  {"q": "A country earns $12bn from exports of coffee out of total exports of $15bn. Calculate the share of coffee in exports (%).", "a": 80, "unit": "%", "tol": 0.5, "hint": "12 ÷ 15.", "sol": "<b>80%</b>: a high degree of dependence."}]) + MCQ([
  ("Which sector includes manufacturing?", ["Primary", "Secondary", "Tertiary", "Informal"], 1, "Making goods is the secondary sector."),
  ("Low-income countries typically export mainly:", ["Primary products", "Capital goods", "Financial services", "Software"], 0, "They have few manufactured exports."),
  ("A fall in the terms of trade means:", ["More exports must be sold to buy the same imports", "Fewer exports are needed per unit of imports", "Export prices rise faster than import prices", "The exchange rate has been fixed"], 0, "Import prices have risen relative to export prices."),
  ("Which makes primary product prices volatile?", ["Inelastic demand and supply that varies with the weather", "Elastic demand and steady supply", "Fixed prices", "Government price setting"], 0, "Small shifts cause large price changes."),
  ("As an economy develops, the share of agriculture in employment usually:", ["Falls", "Rises", "Stays the same", "Doubles"], 0, "Labour moves to industry and services.")
], "qz1") + CARDS([
  ("Primary sector", "Farming, mining, fishing."),
  ("Secondary sector", "Manufacturing and construction."),
  ("Tertiary sector", "Services."),
  ("Engel's law", "Food share of spending falls as income rises."),
  ("Terms of trade", "(Export prices ÷ import prices) × 100."),
  ("Prebisch-Singer", "Primary prices fall relative to manufactures."),
  ("Diversification", "Many products, not one commodity."),
  ("Export-led growth", "Exports as an injection with a multiplier.")]) + MCQ(mc_exam)

build("sy1143", "economic-structure-pattern-of-trade", "Economic Structure and the Pattern of Trade", EY,
  "11.4.3: employment in the primary, secondary and tertiary sectors, how the pattern of trade changes with development, primary product dependence and the terms of trade. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
