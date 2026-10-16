"""Syllabus 10.2.1-10.2.4 Links between internal and external value of money, the balance of payments, inflation and growth. Run: python3 tools/artifact-kit/mk_sy1021.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 10.2.1 to 10.2.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Macroeconomic problems are <b>interrelated</b>. The <b class="kw">internal value of money</b> (its purchasing power at home, the inverse of the price level) and its <b class="kw">external value</b> (the exchange rate and purchasing power abroad) move together: higher inflation at home tends to weaken the currency, and a weaker currency raises import prices and inflation. Inflation worsens the <b>balance of payments</b> by hurting competitiveness. Fast <b>growth</b> raises inflation once the economy nears capacity, and raises <b>imports</b>, so it can worsen the current account. A good answer traces these chains and says when each link is strong or weak.</p></div>

  <h2>1 · Internal and external value of money (10.2.1)</h2>
  <div class="grid2">
    <div class="card"><h3>Internal value</h3><p>What a unit of the currency buys <b>at home</b>. It falls when the price level rises: <b>inflation reduces the internal value</b>.</p></div>
    <div class="card"><h3>External value</h3><p>What the currency buys <b>abroad</b>, shown by the <b>exchange rate</b>. A <b>depreciation</b> lowers the external value, an <b>appreciation</b> raises it.</p></div>
  </div>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Inflation to the exchange rate:</b> if prices rise faster at home than abroad, exports become dearer and imports cheaper. Demand for the currency falls and supply rises, so the currency tends to <b>depreciate</b>. The theory of <b>purchasing power parity</b> says the exchange rate should adjust until the same goods cost the same in both currencies.</li>
    <li><b>Exchange rate to inflation:</b> a depreciation raises the price of imported goods and raw materials, which raises the price level (<b>imported inflation</b>). An appreciation lowers import prices and helps cut inflation, but makes exports dearer.</li>
    <li><b>Vicious and virtuous circles:</b> inflation, depreciation and more inflation can feed on one another. Low inflation, a stronger currency and cheaper imports can do the same in reverse.</li>
    <li><b>Fixed rates:</b> under a fixed or managed rate a high-inflation country's currency becomes <b>overvalued</b>, which causes a deficit and pressure to devalue.</li>
  </ul>

  <h2>2 · The balance of payments and inflation (10.2.2)</h2>
  <ul>
    <li><b>Inflation leads to a deficit:</b> if domestic prices rise faster than those of trading partners, price competitiveness falls, exports fall and imports rise. The size of the effect depends on price elasticities (Marshall-Lerner condition).</li>
    <li><b>A deficit can lead to inflation:</b> a falling currency raises import prices. Persistent deficits also lead to depreciation and cost-push inflation.</li>
    <li><b>Tackling inflation can help the current account:</b> deflationary policy lowers spending on imports and prices at home. But higher interest rates may attract hot money and raise the exchange rate, which could <b>hurt</b> exports.</li>
    <li><b>Low inflation and a surplus</b> may reinforce each other, as in some export-led economies.</li>
  </ul>

  <h2>3 · Growth and inflation (10.2.3)</h2>
  <ul>
    <li><b>Demand-led growth:</b> when AD rises with spare capacity, output rises with little inflation. Near full capacity (the vertical LRAS), extra demand raises prices, so growth above the sustainable rate brings <b>demand-pull inflation</b>.</li>
    <li><b>Supply-led growth:</b> growth from productivity and capacity (an LRAS shift) allows faster growth without inflation.</li>
    <li><b>Inflation can harm growth:</b> uncertainty raises the risk of investment, savings lose value, and tight policy to curb inflation slows growth. Moderate stable inflation is consistent with growth.</li>
    <li><b>Cost-push shocks</b> (oil prices) cause inflation and lower growth together (stagflation).</li>
  </ul>

  <h2>4 · Growth and the balance of payments (10.2.4)</h2>
  <ul>
    <li><b>Growth raises imports:</b> higher incomes increase demand for imports, especially if the <b>marginal propensity to import</b> or the income elasticity of demand for imports is high, so the current account worsens. This is the <b>import suction</b> effect.</li>
    <li><b>Export-led growth:</b> growth driven by exports improves the current account and raises income through the multiplier.</li>
    <li><b>Supply-side growth</b> raises competitiveness, which can improve the current account.</li>
    <li><b>Developing economies</b> may need to import capital goods to grow, which widens the deficit until the new capacity raises exports. FDI inflows can finance the gap.</li>
  </ul>
  <div class="tip"><b class="h">Exam habit</b>Write each link as a chain with a direction and a condition: "higher inflation <b>could</b> worsen the current account <b>if</b> export and import demand are price elastic". Then say what policy could break the chain and what it costs.</div>
'''

watch = '''
  <h2>1 · The inflation and exchange rate circle</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Growth, inflation and the current account together</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · Inflation differences and the exchange rate</h2>
  <p>Purchasing power parity says a currency should lose value when its inflation is higher than abroad. Set the two inflation rates and the number of years.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Home prices after</small><strong id="r1"></strong></div><div><small>Foreign prices after</small><strong id="r2"></strong></div><div><small>Exchange rate (home per foreign)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Home and foreign price indexes and the implied exchange rate over time"></svg></div></div></div>

  <h2>Lab 2 · Growth, imports and the current account</h2>
  <p>An economy has GDP of 1,000 and exports and imports of 200 each. Choose its growth, how much of extra income is spent on imports and how fast export markets grow.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Extra imports</small><strong id="t1"></strong></div><div><small>Extra exports</small><strong id="t2"></strong></div><div><small>Current account balance</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of exports and imports before and after growth"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which direction does the link run?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the vicious circle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Turkey's currency and inflation", "In the early 2020s the Turkish lira lost most of its value against the dollar while inflation rose above 50%. Import prices rose with the falling currency, and the higher prices added to pressure on the lira.", "a vicious circle between the external and internal value of money. Add that policy choices on interest rates mattered.") +
rw("The UK after the 2016 vote to leave the EU", "The pound fell sharply after the referendum. Import prices rose, which added to inflation over the next two years, while exports became cheaper to buyers abroad.", "depreciation raising inflation and the slow effect on the current account (J curve). Note that other factors also moved.") +
rw("China's rapid growth and imports", "As incomes rose, China's demand for raw materials, energy and capital goods rose strongly. Its surpluses stayed large because exports grew even faster, but countries that sold it commodities benefited.", "growth raising imports, and why export growth can offset it. Link to the marginal propensity to import.") +
rw("Overheating in an emerging economy", "When growth is well above the trend rate, firms and workers can raise prices and wages, inflation rises and imports surge. Central banks often respond by raising interest rates.", "growth above capacity causing inflation and a deficit together, which links all three objectives.")
)

mc_exam = [
  ("If prices increase in country X but stay the same in country Y, what is the most likely effect on the internal and external value of money in country X? (Feb/March 2025 · 32 · Q20, reworded)", ["Internal value falls and external value falls", "Internal value falls and external value rises", "Internal value rises and external value falls", "Internal value rises and external value rises"], 0, "Higher prices reduce purchasing power at home, and higher relative prices weaken demand for the currency."),
  ("A government uses quantitative easing to raise growth. What is the most likely effect on the internal and external value of its currency? (May/June 2020 · 31 · Q29, reworded)", ["Both fall", "Internal value falls and external value rises", "Both rise", "Internal value rises and external value falls"], 0, "More money and lower interest rates raise prices and weaken the exchange rate."),
  ("In which situation is devaluation most likely to cause inflation? (Feb/March 2024 · 32 · Q25, reworded)", ["Excess capacity is available", "Import tariffs are cut", "Local substitutes for imported raw materials are unavailable", "Demand for exports is price inelastic"], 2, "If firms cannot replace imported inputs, higher import prices feed straight into costs and prices."),
  ("A country imports most of its raw materials. Which policy is most likely to control cost-push inflation? (Feb/March 2024 · 32 · Q26, reworded)", ["An appreciation of the exchange rate", "A rise in income tax", "A rise in interest rates", "A rise in sales tax"], 0, "A stronger currency makes imported inputs cheaper."),
  ("Which would be the most effective policy to reduce inflation caused by a rapid rise in import prices? (Feb/March 2024 · 32 · Q20, reworded)", ["A fall in the interest rate", "A fall in income tax", "A rise in tariffs", "A revaluation of the exchange rate"], 3, "Revaluation lowers the domestic price of imports. Tariffs would raise them."),
  ("Which would not lead to a rise in the value of a country's currency? (Feb/March 2025 · 32 · Q23, reworded)", ["A rise in domestic inflation", "A rise in domestic interest rates", "A rise in incomes abroad", "More tourists visiting"], 0, "Higher inflation weakens competitiveness and so lowers demand for the currency."),
  ("Nominal national income rose 2% in a year, inflation was 3% and population rose 1%. What happened to real income per head? (Feb/March 2024 · 32 · Q19, reworded)", ["It fell by 2%", "It rose by 1%", "It rose by 4%", "It did not change"], 0, "Real national income fell about 1%, and with 1% more people real income per head fell about 2%."),
  ("The current account moves into deficit. What is a possible reason? (Feb/March 2025 · 32 · Q22, reworded)", ["A fall in tax revenue", "Export-led growth", "Repaying debts to other countries", "Imports of new technology"], 3, "Imports of goods raise the import bill; debt repayment is in the financial account and export-led growth tends to improve the current account.")
]

exam = exam_page("the links between macroeconomic problems",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The internal and external value of money and the links between aims appear in Paper 4 essays, usually as 12 or 13 mark questions. Reworded questions are below, with two practice questions and eight Paper 3 multiple choice questions.",
  [("Essay part, 12 marks", "1", "Oct/Nov 2022 (42) Q6(a)"), ("Essay part, 13 marks", "2", "Feb/March 2021 (42) Q7(b); Oct/Nov 2022 (42) Q6(b)"), ("Practice questions", "2", "Growth and the current account; inflation and the balance of payments"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on Oct/Nov 2022 · 9708/42 · Q6(a)", "12 marks", "Explain how changes in the internal value of a country's currency can affect the external value of that currency.",
     ["Define the internal value (purchasing power at home, linked to inflation) and the external value (the exchange rate). Define both terms clearly for the top levels.",
      "Link: higher inflation than trading partners makes exports dearer and imports cheaper, which reduces demand for the currency and raises its supply, so it depreciates. Use purchasing power parity.",
      "Comment on the exchange rate regime: under a floating rate the rate adjusts; under a fixed rate pressure builds for devaluation or reserves fall.",
      "Level 4 (9 to 12) needs the relationship analysed, not just the two definitions."],
     "Define both. Chain from inflation to competitiveness to demand for the currency. Fixed versus floating. Possible reverse link."),
  eq("Based on Feb/March 2021 · 9708/42 · Q7(b)", "13 marks", "To what extent do you agree that it is not possible to solve a persistent balance of payments deficit without sacrificing other key macroeconomic aims?",
     ["Explain what a persistent deficit is and emphasise the word 'persistent'.",
      "Policies: expenditure-reducing (higher taxes, higher interest rates) which cut imports but may hurt growth and employment while helping inflation; expenditure-switching (depreciation, tariffs) which may raise inflation or provoke retaliation; supply-side policy which improves competitiveness without those costs but works slowly.",
      "A conclusion that weighs the conflicts: it is largely true in the short run, less so if supply-side policy raises competitiveness."],
     "Persistent deficit. Three policy types and what each costs. Time horizon. Judgement."),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q6(b)", "13 marks", "Discuss whether a government can achieve all its key macroeconomic aims at the same time.",
     ["State the aims: low unemployment, low inflation, growth and a balanced current account (and sometimes distribution and sustainability).",
      "Use AD and AS to show what happens with spare capacity and near full employment. The Phillips curve trade-off, growth causing imports and inflation, and policy conflicts are examples.",
      "Level 4 needs two conflicts analysed with a diagram or other analysis, and a conclusion on whether all aims can be met together (rarely, though supply-side growth and good luck may allow it for a time)."],
     "Two conflicts with diagrams. Role of spare capacity and time. Conclude 'rarely, and only temporarily'."),
  eq("Practice (not a past paper question)", "8 marks", "Explain why economic growth might lead to a deficit on the current account.",
     ["Growth raises incomes, which raises spending on imports; the effect depends on the marginal propensity to import or income elasticity of demand for imports.",
      "If exports do not grow as fast as imports, X − M falls. Inflation from fast growth can also reduce competitiveness.",
      "Evaluation: export-led or supply-side growth may improve the current account, and capital goods imports may raise future exports."],
     "Higher income, higher imports. Condition on exports and competitiveness. One reason the deficit might not appear.",
     [[("k", "Economic growth is a rise in real GDP, and a deficit on the current account means that the value of imports of goods and services plus net income and transfers exceeds exports."), ("n", "As real incomes rise, households and firms spend more, and part of the extra spending goes on imports. If the marginal propensity to import is high, as it is when the economy does not make many of the goods people want, imports could rise faster than exports. Fast growth may also raise inflation, so exports become less competitive, which adds to the deficit.")],
      [("e", "However, the deficit is not inevitable. If growth is export-led, exports rise with output and the current account may improve, and if the economy imports capital goods that raise productive capacity, exports could grow later. The effect therefore depends on the source of growth and the elasticities.")]]),
  eq("Practice (not a past paper question)", "8 marks", "Explain how high inflation might affect a country's balance of payments.",
     ["Domestic prices rising faster than abroad reduce price competitiveness: exports fall and imports rise.",
      "The size depends on price elasticities of demand for exports and imports (Marshall-Lerner).",
      "Currency effect: the current account deficit and weaker demand may cause depreciation, which can partly restore competitiveness but raises import prices.",
      "Evaluation: non-price factors, long-term contracts and time lags (J curve) mean the effect may be small or delayed."],
     "Competitiveness chain. Elasticity condition. Exchange rate response. A limit.",
     [[("k", "High inflation reduces the internal value of a country's money and can reduce the external value too."), ("n", "If prices in the country rise faster than in its trading partners, its exports become more expensive for foreign buyers and imports become cheaper for domestic consumers, so export volumes fall and import volumes rise and the current account moves towards deficit. The size of the effect depends on price elasticities: if demand for exports and imports is elastic, the volume changes are large.")],
      [("n", "The deficit also increases the supply of the currency relative to demand, so the exchange rate may depreciate, which restores some competitiveness but raises the price of imported goods and could add to inflation again."), ("e", "However, if exports are mainly differentiated goods where quality matters more than price, or if demand is inelastic in the short run, the current account may change little for a time, so the link is weaker than the simple theory suggests.")]])
  ],
  )

tips = tips_html(
  [("Define both values of money.", "Internal: purchasing power at home, linked to inflation. External: the exchange rate and purchasing power abroad."),
   ("Show the chain.", "Inflation, then competitiveness, then demand for the currency, then the exchange rate, then import prices, then inflation again."),
   ("Add the condition.", "Elasticities of demand (Marshall-Lerner), spare capacity, or the exchange rate system."),
   ("Growth and BoP: say 'import suction'.", "Higher income raises imports, depending on the marginal propensity to import."),
   ("Growth and inflation: mention capacity.", "Demand-led growth is inflationary near the LRAS, supply-led growth is not."),
   ("Use both directions.", "The links run both ways, and policy can reverse them."),
   ("Name a policy and a cost.", "Raising interest rates fights inflation and may attract hot money, which could hurt exports.")],
  [("Internal and external", "A rise in the price level reduces the internal value of money, and if prices rise faster than abroad the external value may also fall."),
   ("Chain", "Higher inflation could reduce price competitiveness, which may lead to a deficit on the current account if demand for exports is elastic."),
   ("Circle", "A depreciation raises the price of imports, which could add to inflation, so the effects may reinforce each other."),
   ("Growth", "Faster growth raises incomes, and if the marginal propensity to import is high, imports may rise by more than exports."),
   ("Evaluate", "However, the link is weaker if growth is export-led or comes from supply-side improvements.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture: two values of money ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Link between the internal value of money, inflation, the exchange rate and import prices">${(() => { let o = ""; const box = (x, y, w, l, c) => SV.rect(x, y, w, 56, c) + SV.text(x + w / 2, y + 33, l, "lbl bd", { "text-anchor": "middle" }); o += box(40, 40, 190, "Higher domestic inflation", "f2") + box(285, 40, 190, "Exports dearer, imports cheaper", "f4") + box(530, 40, 190, "Demand for currency falls", "f1") + box(530, 220, 190, "Currency depreciates", "f2") + box(285, 220, 190, "Import prices rise", "f4") + box(40, 220, 190, "Domestic inflation rises again", "f2"); o += arrow(235, 68, 280, 68, "r", "c1", 1) + arrow(480, 68, 525, 68, "r", "c1", 1) + arrow(625, 100, 625, 215, "d", "c1", 1) + arrow(525, 248, 480, 248, "l", "c1", 1) + arrow(280, 248, 235, 248, "l", "c1", 1) + arrow(135, 215, 135, 100, "u", "c2", 1); o += tag(380, 170, "a vicious circle", "t2", 1, "middle") + tag(380, 192, "low inflation and an appreciation can run the same loop in reverse", "t3", 1, "middle"); return o; })()}</svg>`;

/* ---------- Watch 1: circle animation ---------- */
const CBOX = [[40, 40], [285, 40], [530, 40], [530, 220], [285, 220], [40, 220]];
const LV = ["Higher domestic inflation", "Exports dearer, imports cheaper", "Demand for currency falls", "Currency depreciates", "Import prices rise", "Domestic inflation rises again"];
const LV2 = ["Lower domestic inflation", "Exports cheaper, imports dearer", "Demand for currency rises", "Currency appreciates", "Import prices fall", "Domestic inflation falls further"];
function circDraw(s) {
  const lab = s.m > 0.5 ? LV2 : LV; let o = "";
  CBOX.forEach((b, i) => { const v = Math.max(0, Math.min(1, s.n - i)); if (v <= 0) return; o += SV.rect(b[0], b[1], 190, 56, s.m > 0.5 ? "f3" : i === 5 || i === 0 || i === 3 ? "f2" : "f4", op(v)) + SV.text(b[0] + 95, b[1] + 33, lab[i], "lbl bd", { "text-anchor": "middle", ...op(v) }); });
  const AR = [[235, 68, 280, 68, "r"], [480, 68, 525, 68, "r"], [625, 100, 625, 215, "d"], [525, 248, 480, 248, "l"], [280, 248, 235, 248, "l"], [135, 215, 135, 100, "u"]];
  AR.forEach((a, i) => { const v = Math.max(0, Math.min(1, s.n - i - 0.5)); if (v > 0) o += arrow(a[0], a[1], a[2], a[3], a[4], s.m > 0.5 ? "c3" : "c2", v); });
  if (s.n >= 6.4) o += tag(380, 170, s.m > 0.5 ? "a virtuous circle" : "a vicious circle", s.m > 0.5 ? "t3" : "t2", 1, "middle");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 310, label: "Vicious circle linking inflation and the exchange rate, then the virtuous circle in reverse", base: { n: 0, m: 0 }, draw: circDraw, tween: 1400, dwell: 5600, steps: [
  { cap: "<b>The start.</b> Domestic prices rise faster than prices abroad. The internal value of money falls.", s: { n: 1.2 } },
  { cap: "<b>Competitiveness.</b> Exports become dearer for foreign buyers and imports cheaper for home buyers, so the current account worsens and demand for the currency falls.", s: { n: 3 } },
  { cap: "<b>Depreciation.</b> The currency's external value falls. Import prices in domestic currency rise.", s: { n: 5 } },
  { cap: "<b>The circle closes.</b> Dearer imports raise costs and prices, so domestic inflation rises again. The loop feeds itself: a <b>vicious circle</b>. Policy may need a tighter stance or a credible target to break it.", s: { n: 6.6 } },
  { cap: "<b>The reverse.</b> Low inflation, an appreciating currency and falling import prices can reinforce each other: a <b>virtuous circle</b>. The cost is that exporters become less competitive.", s: { n: 6.6, m: 1 } },
] });

/* ---------- Watch 2: growth, inflation and current account ---------- */
const GXX = (x) => 90 + x * 62, GYY = (v) => 170 - v * 30;
const gg = (x) => (x <= 3 ? x : 3 + 0.1 * (x - 3)), ii = (x) => 1.5 + (x <= 3 ? 0.1 * x : 0.3 + 0.9 * (x - 3)), cc = (x) => 0.5 - 0.5 * x;
function triDraw(s) {
  let o = SV.line(70, 170, 740, 170) + SV.line(70, 40, 70, 320) + SV.text(740, 190, "Growth of aggregate demand (% a year)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "% (growth, inflation) and % of GDP (current account)", "sm");
  [0, 2, 4, 6, 8, 10].forEach((x) => (o += SV.text(GXX(x), 186, x, "sm", { "text-anchor": "middle" })));
  const draw = (f, cls, tcls, label, v) => { if (v <= 0) return ""; const pts = []; for (let x = 0; x <= 10.001; x += 0.2) pts.push([GXX(x), GYY(f(x))]); return SV.path(Lib.ptsPath(pts), cls, op(v)) + tag(GXX(10) + 4, GYY(f(10)) + 4, label, tcls, v); };
  o += draw(gg, "c1", "t1", "growth", s.a) + draw(ii, "c2", "t2", "inflation", s.b) + draw(cc, "c4", "t4", "current account", s.c);
  if (s.d > 0) o += SV.line(GXX(3), 40, GXX(3), 320, "gr", op(s.d)) + tag(GXX(3) + 6, 56, "capacity reached", "t3", s.d);
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "Growth, inflation and the current account as aggregate demand grows faster", base: { a: 0, b: 0, c: 0, d: 0 }, draw: triDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Growth.</b> With spare capacity, faster demand growth gives faster real growth. Once the economy reaches <b>capacity</b>, further demand adds little to output.", s: { a: 1, d: 1 } },
  { cap: "<b>Inflation.</b> Below capacity inflation stays low. Beyond it, extra demand raises prices instead of output, so inflation accelerates: growth above the sustainable rate brings <b>demand-pull inflation</b>.", s: { a: 1, b: 1, d: 1 } },
  { cap: "<b>The current account.</b> Faster growth in income raises imports all the way, so the current account moves into deficit, and more rapidly once inflation hits competitiveness.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The trade-off.</b> The best range for demand growth is near the capacity point: more growth than that brings little extra output but costs inflation and a larger deficit. Supply-side growth (a higher capacity point) is how to get both.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1: PPP ---------- */
function labPPP() {
  if (!$("#pd") || !$("#pf") || !$("#py")) return;
  const d = +$("#pd").value / 10, f = +$("#pf").value / 10, yrs = +$("#py").value;
  const Pd = (t) => 100 * Math.pow(1 + d / 100, t), Pf = (t) => 100 * Math.pow(1 + f / 100, t), E = (t) => 100 * Pd(t) / Pf(t) / 1;
  const e = (t) => 100 * Math.pow((1 + d / 100) / (1 + f / 100), t);
  $("#r1").textContent = Lib.fmtN(Pd(yrs), 0); $("#r2").textContent = Lib.fmtN(Pf(yrs), 0); $("#r3").textContent = Lib.fmtN(e(yrs), 0);
  const chg = (e(yrs) / 100 - 1) * 100;
  $("#rv").textContent = Math.abs(chg) < 0.5 ? "Inflation is about the same at home and abroad, so there is no pressure on the exchange rate." : chg > 0 ? `Home prices rose ${Lib.fmtN(Pd(yrs) - 100, 0)}% against ${Lib.fmtN(Pf(yrs) - 100, 0)}% abroad. To keep the same goods costing the same, the home currency would need to depreciate: the rate moves from 100 to ${Lib.fmtN(e(yrs), 0)} units of home currency per unit of foreign currency (a ${Lib.fmtN(chg, 0)}% fall in its external value).` : `Home inflation is lower than abroad, so purchasing power parity points to an appreciation: the rate falls to ${Lib.fmtN(e(yrs), 0)} units of home currency per unit of foreign currency.`;
  const X = (t) => 50 + t * 34, Y = (v) => 260 - (v - 80) * 0.9; const mx = Math.max(Pd(yrs), Pf(yrs), e(yrs), 130);
  const Y2 = (v) => 260 - (v - 80) / (mx - 80) * 210;
  let o = SV.line(50, 260, 400, 260) + SV.line(50, 260, 50, 30) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" });
  const line = (fn, c) => { const pts = []; for (let t = 0; t <= yrs; t += 0.25) pts.push([50 + t / yrs * 340, Y2(fn(t))]); return SV.path(Lib.ptsPath(pts), c); };
  o += line(Pd, "c2") + line(Pf, "c1") + line(e, "c4") + tag(396, Y2(Pd(yrs)) - 6, "home prices", "t2", 1, "end") + tag(396, Y2(Pf(yrs)) + 14, "foreign prices", "t1", 1, "end") + tag(396, Y2(e(yrs)) + (e(yrs) > Pd(yrs) ? -6 : 14), "exchange rate", "t4", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pd", label: "Home inflation (%) ", min: 0, max: 200, step: 5, value: 80, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPPP });
Lib.slider($("#g2"), { id: "pf", label: "Foreign inflation (%) ", min: 0, max: 100, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPPP });
Lib.slider($("#g3"), { id: "py", label: "Years ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labPPP });
labPPP();

/* ---------- Lab 2: growth and imports ---------- */
function labGI() {
  if (!$("#gg") || !$("#gm") || !$("#gx")) return;
  const g = +$("#gg").value / 10 / 100, m = +$("#gm").value / 100, x = +$("#gx").value / 10 / 100, dY = 1000 * g, dM = m * dY, dX = 200 * x, ca = 200 + dX - (200 + dM);
  $("#t1").textContent = "+" + Lib.fmtN(dM, 1); $("#t2").textContent = "+" + Lib.fmtN(dX, 1); $("#t3").textContent = (ca >= 0 ? "+" : "") + Lib.fmtN(ca, 1) + " (" + Lib.fmtN(ca / (1000 + dY) * 100, 1) + "% of GDP)";
  $("#tv").textContent = ca < -0.5 ? `GDP grows by ${Lib.fmtN(dY, 0)}. With ${Math.round(m * 100)}% of extra income spent on imports, imports rise by ${Lib.fmtN(dM, 1)}, more than the ${Lib.fmtN(dX, 1)} rise in exports: the current account moves into deficit.` : ca > 0.5 ? `Exports rise by ${Lib.fmtN(dX, 1)}, more than the ${Lib.fmtN(dM, 1)} rise in imports, so the current account moves into surplus: this is export-led growth.` : "Extra imports and extra exports roughly cancel, so the current account stays close to balance.";
  const mx = Math.max(200 + dX, 200 + dM, 220) * 1.1, Y = (v) => 250 - v / mx * 200; let o = SV.line(40, 250, 400, 250);
  const bars = [["Exports before", 200, "f1"], ["Imports before", 200, "f2"], ["Exports after", 200 + dX, "f1"], ["Imports after", 200 + dM, "f2"]];
  bars.forEach((b, i) => { const xx = 60 + i * 85; o += SV.rect(xx, Y(b[1]), 60, 250 - Y(b[1]), b[2], { opacity: i < 2 ? 0.5 : 0.9 }) + tag(xx + 30, Y(b[1]) - 6, Lib.fmtN(b[1], 0), i % 2 ? "t2" : "t1", 1, "middle") + SV.text(xx + 30, 268, b[0], "sm bd", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Real GDP growth (%) ", min: 0, max: 80, step: 5, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labGI });
Lib.slider($("#g5"), { id: "gm", label: "Share of extra income spent on imports (%) ", min: 10, max: 60, step: 5, value: 35, fmt: (v) => v, onInput: labGI });
Lib.slider($("#g6"), { id: "gx", label: "Export growth (%) ", min: 0, max: 80, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labGI });
labGI();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the change tend to raise or lower the external value of the currency (the exchange rate)?", ["Raises external value", "Lowers external value"],
  [("Home inflation falls below that of trading partners", 0), ("Home inflation rises well above that of trading partners", 1), ("Interest rates rise and attract foreign savers", 0), ("A large current account deficit emerges", 1), ("Foreign demand for exports rises", 0), ("Quantitative easing expands the money supply", 1), ("Investors expect the currency to appreciate", 0), ("Capital flows out of the country", 1)],
  "Higher demand for the currency raises its value; higher supply lowers it.") + MATCH([
  ["Internal value of money", "Purchasing power at home, the inverse of the price level"],
  ["External value of money", "The exchange rate: what the currency buys abroad"],
  ["Purchasing power parity", "The idea that the exchange rate adjusts so that price levels are equal"],
  ["Imported inflation", "Higher prices caused by dearer imports after a depreciation"],
  ["Marginal propensity to import", "Share of extra income spent on imports"],
  ["Import suction", "Rise in imports caused by rising national income"]]) + ORDER(
  "Put the vicious circle in order, starting with higher inflation.",
  ["Domestic inflation is higher than abroad", "Exports become less competitive and imports cheaper", "Demand for the currency falls and it depreciates", "Imported raw materials and goods cost more", "Domestic inflation rises again"],
  "Depreciation feeds inflation and inflation feeds depreciation.") + CALC([
  {"q": "Home prices rise 6% a year and foreign prices 2% a year. Using PPP, calculate the approximate annual fall in the external value of the home currency (%).", "a": 4, "unit": "%", "tol": 0.05, "hint": "Inflation differential.", "sol": "6 − 2 = <b>4%</b> a year (approximately)."},
  {"q": "A country's exchange rate is 1.00 foreign currency units per unit of home currency. It depreciates by 12%. How many foreign currency units does one unit of home currency now buy?", "a": 0.88, "tol": 0.005, "hint": "1.00 × (1 − 0.12).", "sol": "1.00 × 0.88 = <b>0.88</b>."},
  {"q": "GDP grows by $50bn and the marginal propensity to import is 0.3. Calculate the extra imports ($bn).", "a": 15, "unit": "$bn", "tol": 0.05, "hint": "MPM × change in income.", "sol": "0.3 × 50 = <b>$15bn</b>."},
  {"q": "A country's price index is 100 at home and 100 abroad, and the exchange rate is 1. After a year home prices are 105 and foreign prices are 102 with the nominal rate unchanged. What is the real exchange rate index (home price level × rate ÷ foreign price level × 100)?", "a": 102.9, "tol": 0.1, "hint": "105 × 1 ÷ 102 × 100.", "sol": "105 ÷ 102 × 100 = <b>102.9</b>: the home country has become about 3% less competitive."}]) + MCQ([
  ("Which is true of purchasing power parity?", ["Exchange rates do not change", "The exchange rate adjusts so that the same goods cost the same in different countries", "Interest rates equal inflation", "Imports equal exports"], 1, "PPP links the exchange rate to relative price levels."),
  ("A depreciation of the currency is most likely to cause:", ["Higher import prices and a rise in the price level", "Lower export volumes immediately", "Lower inflation", "A rise in the external value"], 0, "Imports cost more in domestic currency, which raises the price level."),
  ("Growth is likely to worsen the current account when:", ["The marginal propensity to import is high", "Exports grow faster than income", "Imports are inelastic and unaffected by income", "Growth comes entirely from export demand"], 0, "A high propensity to import means extra income is spent on imports."),
  ("Which is the best example of supply-side growth that need not cause inflation?", ["A rise in consumer confidence", "Investment in education and infrastructure that raises capacity", "A cut in interest rates", "A rise in government spending"], 1, "LRAS shifts right, allowing output to rise without pressure on prices."),
  ("A government raises interest rates to cut inflation. What effect could this have on the current account?", ["Higher interest rates could attract hot money, raise the exchange rate and reduce export competitiveness", "No effect at all", "It always improves exports", "It always raises imports"], 0, "A stronger currency makes exports dearer and imports cheaper, which could worsen the current account.")
], "qz1") + CARDS([
  ("Internal value of money", "Purchasing power at home; falls with inflation."),
  ("External value of money", "Exchange rate; what the currency buys abroad."),
  ("Purchasing power parity", "Exchange rate adjusts so price levels are equal."),
  ("Imported inflation", "Rise in domestic prices from dearer imports."),
  ("Marginal propensity to import", "Share of extra income spent on imports."),
  ("Marshall-Lerner condition", "A depreciation improves the current account if PEDx + PEDm > 1."),
  ("Demand-pull inflation", "Prices rise because AD exceeds capacity."),
  ("Export-led growth", "Growth driven by rising exports.")]) + MCQ(mc_exam)

build("sy1021", "links-between-macro-problems", "Links between the Value of Money, the Balance of Payments, Inflation and Growth", EY,
  "10.2.1 to 10.2.4: the internal and external value of money, inflation and the balance of payments, growth and inflation, and growth and the balance of payments. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
