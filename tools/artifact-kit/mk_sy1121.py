"""Syllabus 11.2.1 Measurement of exchange rates: nominal and real, trade-weighted. Run: python3 tools/artifact-kit/mk_sy1121.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.2.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">nominal exchange rate</b> is the price of one currency in terms of another (for example $1.25 per £1). The <b class="kw">real exchange rate</b> adjusts the nominal rate for differences in <b>price levels</b>, so it shows whether a country's goods have become <b>dearer or cheaper relative to its trading partners'</b>, which is what matters for competitiveness. A <b class="kw">trade-weighted exchange rate</b> (effective exchange rate) is an <b>index of the currency against a basket of partner currencies</b>, each weighted by the share of trade with that partner, so it shows the overall movement rather than the rate against one currency. The <b>real effective exchange rate</b> combines both ideas.</p></div>

  <h2>1 · The nominal exchange rate</h2>
  <ul>
    <li>The <b>nominal exchange rate</b> is the price of one currency in terms of another, quoted as, say, £1 = $1.25. It is set by supply and demand in a floating system, or fixed by the central bank in a fixed system.</li>
    <li>If £1 buys more dollars (for example $1.25 rising to $1.40) the pound has <b>appreciated</b> (under a floating rate) or been <b>revalued</b> (under a fixed rate). If it buys fewer, it has <b>depreciated</b> or been <b>devalued</b>. The difference between these terms is covered in 11.2.3.</li>
    <li>The weakness of the nominal rate on its own is that it <b>ignores inflation</b>. If a currency's nominal rate is constant but domestic prices rise faster than abroad, exports are becoming less competitive even though the exchange rate looks unchanged.</li>
  </ul>

  <h2>2 · The real exchange rate</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The <b>real exchange rate</b> adjusts the nominal rate for relative price levels:
      <b>real rate index = nominal rate index × (domestic price index ÷ foreign price index)</b>, with the nominal rate measured as foreign currency per unit of domestic currency, so a rise means appreciation.</li>
    <li>A <b>rise in the real exchange rate (real appreciation)</b> means domestic goods have become relatively dearer: exports are less competitive and imports are cheaper in real terms. A <b>fall (real depreciation)</b> makes domestic goods relatively cheaper.</li>
    <li><b>Worked idea:</b> the nominal rate is unchanged, domestic inflation is 6% and foreign inflation is 2%. The real exchange rate rises by about 4% (6% − 2%), so the country has lost competitiveness even though the nominal rate has not moved.</li>
    <li>A nominal depreciation can be <b>cancelled out</b> if domestic inflation rises by more than foreign inflation, so the real rate (and competitiveness) hardly changes. This is why devaluations in high-inflation countries often fail to last.</li>
    <li>The real rate links to <b>purchasing power parity (PPP)</b>: if the real rate stays constant, the nominal rate is moving in line with relative inflation. A currency is said to be <b>overvalued</b> if it is above its PPP value and <b>undervalued</b> if below.</li>
  </ul>

  <h2>3 · The trade-weighted exchange rate</h2>
  <ul>
    <li>A country trades with many partners and its currency can rise against some and fall against others. The <b>trade-weighted exchange rate index (TWI, or effective exchange rate)</b> measures the currency against a <b>basket</b> of other currencies.</li>
    <li>Each partner's currency is <b>weighted by that partner's share in the country's trade</b> (exports plus imports). A currency movement against a major partner counts for more than a movement against a minor partner.</li>
    <li><b>Calculation:</b> TWI = (weight A × index against A) + (weight B × index against B) + ... The weights add to 1 (or 100%) and the index starts at 100 in a base year.</li>
    <li>The <b>real effective exchange rate (REER)</b> is the trade-weighted index adjusted for each partner's relative price level. Many central banks and the BIS publish it as the best single guide to price competitiveness.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>What it shows</th><th>Main use</th><th>Main limitation</th></tr>
    <tr><td><b>Nominal exchange rate</b></td><td>Price of one currency in another</td><td>Converting prices, trade and investment values; the market rate</td><td>Ignores inflation, and covers one partner only</td></tr>
    <tr><td><b>Real exchange rate</b></td><td>Nominal rate adjusted for relative price levels</td><td>Judging price competitiveness against one country</td><td>Depends on the price index chosen; ignores quality</td></tr>
    <tr><td><b>Trade-weighted (nominal effective)</b></td><td>The currency against a basket, weighted by trade shares</td><td>Overall movement of the currency</td><td>Ignores inflation; weights change over time</td></tr>
    <tr><td><b>Real effective (REER)</b></td><td>Trade-weighted index adjusted for relative prices</td><td>Overall price competitiveness</td><td>Needs good price data; ignores non-price competitiveness</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluation point</b>Price competitiveness is only part of competitiveness. Quality, design, delivery, brand and the dependence on imported inputs also matter. A real depreciation also raises the price of imported inputs, so the net gain to exporters may be smaller than the index suggests.</div>
'''

watch = '''
  <h2>1 · Nominal rate, prices and the real rate</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stR"></div>
  <h2>2 · Building a trade-weighted index</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab 1 · From the nominal to the real exchange rate</h2>
  <p>Set the change in the nominal rate and the inflation rates at home and abroad over one year. See what happens to the real exchange rate and to competitiveness.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Nominal change</small><strong id="r1"></strong></div><div><small>Relative price change</small><strong id="r2"></strong></div><div><small>Real change</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars for the nominal change, the relative inflation effect and the resulting real exchange rate change"></svg></div></div></div>

  <h2>Lab 2 · A trade-weighted index</h2>
  <p>A country sends 50% of its trade to partner A, 30% to partner B and 20% to partner C. Move its currency against each partner (index 100 = last year) and see the effective rate.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Trade-weighted index</small><strong id="t1"></strong></div><div><small>Change</small><strong id="t2"></strong></div><div><small>Overall</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the currency index against three partners and the weighted index"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which measure is being described?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps for finding a real exchange rate change in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Switzerland and the strong franc", "The Swiss franc has tended to appreciate during global uncertainty, because investors treat it as a safe haven. Even with low Swiss inflation, the real value of the franc has risen over time, which squeezes exporters and tourism and has led the central bank to intervene in currency markets at times.", "a real appreciation and its effect on competitiveness. Link to exports, employment and imported inflation.") +
rw("High inflation, falling currency", "In countries with very high inflation, such as Argentina or Turkey at times, the nominal currency can fall sharply while the real exchange rate changes much less, because domestic prices rise quickly too. Exporters may gain less than the headline fall in the currency suggests.", "why the real rate is a better guide to competitiveness than the nominal rate, and why a depreciation may be eroded by inflation.") +
rw("Sterling's fall after 2016", "After the 2016 Brexit vote the pound fell against the US dollar and the euro, and the trade-weighted index fell too. The fall made UK exports cheaper abroad and imports dearer, but the effect on the trade balance was slower than many expected, and imported inflation rose.", "a trade-weighted index, the J curve (see 11.2.5) and imported inflation.") +
rw("The Big Mac index", "The Economist compares the price of a burger in dollars across countries. If a burger costs less in dollars in a country, its currency may be undervalued against the dollar on a simple purchasing power basis, though differences in wages, taxes and rents limit the accuracy.", "purchasing power parity as a benchmark for over- and under-valued currencies, with its limitations.")
)

mc_exam = [
  ("An economy imports a large proportion of its raw materials. Its exchange rate depreciates. What is the effect on the external value and the internal value of its money? (May/June 2025 · 31 · Q24, reworded)", ["External value rises; internal value rises", "External value rises; internal value falls", "External value falls; internal value rises", "External value falls; internal value falls"], 3, "A depreciation is a fall in the external value of the currency. Dearer imported raw materials raise costs and prices, so the internal value (purchasing power at home) also falls."),
  ("An economy's currency appreciates and the Marshall-Lerner condition holds. What is the likely effect on imported inflation and on unemployment? (Oct/Nov 2023 · 32 · Q24, reworded)", ["Imported inflation falls; unemployment falls", "Imported inflation falls; unemployment rises", "Imported inflation rises; unemployment falls", "Imported inflation rises; unemployment rises"], 1, "A stronger currency makes imports cheaper, so imported inflation falls. Exports become dearer, so net exports and employment may fall."),
  ("An economy imports most of the factors of production used to make its exports. What effect would a depreciation of its exchange rate have on the price of imported goods and on the price of exported goods, in the domestic currency? (May/June 2023 · 32 · Q26, reworded)", ["Imported goods fall; exported goods fall", "Imported goods fall; exported goods rise", "Imported goods rise; exported goods fall", "Imported goods rise; exported goods rise"], 3, "The depreciation raises the price of imports. Because export producers rely on imported inputs, their costs rise too, so export prices in the domestic currency rise as well."),
  ("A country imports most of the raw materials used as factor inputs. Which policy is most likely to control cost-push inflation? (Feb/March 2024 · 32 · Q26, reworded)", ["An appreciation of the exchange rate", "An increase in the rate of income tax", "An increase in the rate of interest", "An increase in the rate of sales tax"], 0, "A stronger currency lowers the domestic price of imported inputs, which reduces cost-push pressure directly."),
  ("What is likely to be the most effective policy to reduce inflation caused by a rapid rise in import prices? (Feb/March 2024 · 32 · Q20, reworded)", ["A decrease in the domestic rate of interest", "A decrease in the rate of income tax", "An increase in trade tariffs on imports", "A revaluation of the exchange rate"], 3, "A revaluation lowers the domestic currency price of imports, tackling the source of the inflation. Tariffs would raise import prices further."),
  ("Which change would most likely increase structural unemployment in the manufacturing sector of the US? (Oct/Nov 2021 · 33 · Q21, reworded)", ["Asian exporters of manufactured goods to the US experience a fall in labour costs per unit of output", "Tariffs on Asian manufacturing imports increase", "The share of US manufacturing workers in trade unions falls", "The US dollar's real effective exchange rate against Asian currencies falls"], 0, "Cheaper Asian output makes US producers less competitive. A fall in the US real effective exchange rate would make US goods more competitive, and tariffs would protect them.")
]

exam = exam_page("exchange rate measurement, competitiveness and the value of a currency",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Exchange rate measurement is rarely asked as a stand-alone Paper 4 question, but the internal and external value of a currency, overvaluation and competitiveness appear regularly, and the real and trade-weighted ideas support every exchange rate essay. Reworded past questions are below, with a practice question and six Paper 3 multiple choice questions.",
  [("Essay parts, 12 marks", "1", "Oct/Nov 2022 (42) Q6(a)"), ("Data response, 4 marks", "1", "Oct/Nov 2022 (42) Q1(c)"), ("Multiple choice (Paper 3)", "6 shown below", "2021 to 2025")],
  [
  eq("Based on Oct/Nov 2022 · 9708/42 · Q6(a)", "12 marks", "Explain how changes in the internal value of a country's currency can affect the external value of that currency.",
     ["Define the internal value (purchasing power at home, the inverse of the price level, so linked to inflation) and the external value (the exchange rate against other currencies).",
      "Explain the link: if inflation is higher than in partner countries, exports become dearer and imports cheaper, so demand for the currency falls and supply rises, lowering the exchange rate (the idea behind purchasing power parity).",
      "Explain the reverse link: a fall in the exchange rate raises import prices and can cause inflation, lowering the internal value.",
      "Comment on the exchange rate system: under a floating rate the market adjusts the rate; under a fixed rate the central bank must defend it, so the link works through reserves, interest rates or a devaluation."],
     "Define internal and external value. Higher inflation leads to a weaker currency. A weaker currency leads to higher inflation. Fixed against floating.",
     [[("k", "The internal value of a currency is what it can buy at home, so it falls when the price level rises. The external value is the exchange rate, or what it can buy of other currencies."), ("n", "If domestic inflation is higher than in partner countries, home goods may become dearer relative to foreign goods. Exports could fall and imports could rise, so demand for the currency may fall and supply may rise, putting downward pressure on the exchange rate."), ("e", "This is the logic of purchasing power parity, although the link may be weak in the short run because capital flows and interest rates can matter more.")],
      [("n", "The link may also run the other way. A depreciation raises import prices, and if imports are a large share of spending or are used as inputs, it could raise inflation and lower the internal value."), ("e", "Under a floating rate the market adjusts, while under a fixed rate the central bank would need to use reserves or interest rates to defend the rate, or devalue.")]]),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q1(c)", "4 marks", "Explain how an over-valuation of a country's exchange rate may affect its economy.",
     ["A currency above its equilibrium makes import prices fall and export prices rise (1), so imports tend to rise and exports fall (1). Maximum 2 marks for this.",
      "Development: up to 2 marks for the effect on one of the balance of payments, inflation, unemployment, growth or foreign direct investment."],
     "Import prices fall, export prices rise. Imports up, exports down. Then one macro effect.",
     [[("k", "An over-valued currency makes imports cheaper and exports dearer in foreign currency."), ("n", "Spending may switch towards imports and away from exports, so the current account could worsen and, because exports are part of aggregate demand, growth and employment may fall in export industries.")]]),
  eq("Practice question · modelled on the 12 mark style (no past paper)", "12 marks", "Explain the difference between a nominal and a real exchange rate and why a trade-weighted index is useful.",
     ["The nominal rate is the price of one currency in another; the real rate adjusts for relative price levels.",
      "Why the real rate matters: it shows competitiveness, so a nominal depreciation can be offset by higher domestic inflation.",
      "Trade-weighted index: a basket of partner currencies weighted by trade shares, giving the overall movement.",
      "Evaluation: weights change, price indices differ, and non-price competitiveness matters."],
     "Nominal. Real. Example with inflation. TWI and weights. Limits.",
     [[("k", "The nominal exchange rate is the price of one currency in terms of another, such as $1.25 per pound. The real exchange rate adjusts this for the price levels in the two countries."), ("n", "If the nominal rate is unchanged but domestic inflation is higher than abroad, the real rate rises. Home goods become relatively dearer, so competitiveness could fall even though the nominal rate looks stable. In the same way a nominal depreciation may be offset if domestic prices rise faster.")],
      [("k", "A trade-weighted index measures the currency against a basket of partner currencies, with each weighted by its share of trade."), ("n", "This is useful because a currency can rise against one partner and fall against another. A movement against a major trading partner will count for more, so the index gives a better picture of the overall effect on exports and imports.")],
      [("e", "However, the weights change over time, price indices may not be comparable and quality and other non-price factors also affect competitiveness, so the index may only be a guide.")]])
  ],
  )

tips = tips_html(
  [("Nominal first, then real.", "Give the nominal definition, then say the real rate adjusts for relative inflation. That is the extra mark."),
   ("Always say which way it moves.", "Appreciation is a rise in the currency's value. A real appreciation makes the country's goods relatively dearer."),
   ("Use a simple number.", "Nominal unchanged, home inflation 6%, foreign 2%: real rate up about 4%."),
   ("Explain the weights.", "In a trade-weighted index each currency is weighted by its share of trade, so major partners count for more."),
   ("Link to competitiveness.", "Real appreciation hurts export competitiveness, real depreciation helps it, subject to elasticities."),
   ("Evaluate with limits.", "Price indices, changing weights and non-price competitiveness."),
   ("Appreciation or revaluation?", "Floating rate: appreciation or depreciation. Fixed rate: revaluation or devaluation.")],
  [("Nominal", "The nominal exchange rate is the price of one currency in terms of another, without adjusting for inflation."),
   ("Real", "The real exchange rate adjusts the nominal rate for relative price levels, so it may be a better guide to competitiveness."),
   ("Weights", "A trade-weighted index gives more weight to the currencies of a country's major trading partners."),
   ("Inflation", "A nominal depreciation could be offset if domestic inflation is higher than abroad."),
   ("Limits", "Competitiveness also depends on quality and other non-price factors, so a real exchange rate index may only be a guide.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Nominal, prices, real ---------- */
const RX = (i) => 90 + i * 130, RY = (v) => 300 - (v - 94) * 13;
const YRS = [0, 1, 2, 3, 4], NOM = [100, 99, 98, 97, 96], PR = [100, 103, 106.1, 109.3, 112.6];
function realDraw(s) {
  let o = axes(70, 300, 730, 30, "Year", "Index (year 0 = 100)"); [100, 104, 108, 112].forEach((v) => (o += SV.text(64, RY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, RY(v), 730, RY(v), "gr", op(0.35))));
  YRS.forEach((i) => (o += SV.text(RX(i), 322, "Y" + i, "sm", { "text-anchor": "middle" })));
  const ln = (arr, c, k) => { const n = Math.max(0, Math.min(4, k * 4)), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([RX(i), RY(arr[i])]); if (n % 1 > 0 && Math.floor(n) < 4) { const a = Math.floor(n), f = n - a; pts.push([RX(a + f), RY(arr[a] + (arr[a + 1] - arr[a]) * f)]); } return pts.length > 1 ? SV.path(Lib.ptsPath(pts), c) : ""; };
  o += ln(NOM, "c1", s.a) + (s.a > 0 ? tag(RX(4) + 4, RY(NOM[4]) - 8, "Nominal rate index", "t1", s.a, "end") : "");
  if (s.b > 0) o += ln(PR, "c3 dash", s.b) + tag(RX(4) + 4, RY(PR[4]) - 4, "Domestic ÷ foreign prices", "t3", s.b, "end");
  if (s.c > 0) { const real = NOM.map((n, i) => n * PR[i] / 100); o += ln(real, "c4", s.c) + SV.circle(RX(4), RY(real[4]), 7, "dot4", op(s.c)) + tag(RX(4) - 12, RY(real[4]) + 22, "Real rate up " + Lib.fmtN(real[4] - 100, 1) + "%", "t4", s.c, "end"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Nominal exchange rate index falling to 96, relative prices rising to 112.6 and the real exchange rate rising to 108.1">${realDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 340, label: "Nominal rate falling, relative prices rising and the real exchange rate rising", base: { a: 0, b: 0, c: 0 }, draw: realDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The nominal exchange rate</b> falls by 1% a year: the index drops from 100 to 96, a 4% depreciation. Looking only at this line, home goods look cheaper abroad.", s: { a: 1 } },
  { cap: "<b>Relative prices.</b> The home country has 3% inflation a year while its partner has none. The ratio of domestic to foreign prices climbs to about 112.6, so home goods are dearer at home relative to abroad.", s: { a: 1, b: 1 } },
  { cap: "<b>The real exchange rate</b> is the nominal rate multiplied by the price ratio: 96 × 112.6 ÷ 100 = 108.1. It has risen about 8%, a real appreciation.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The meaning.</b> The 4% nominal depreciation was more than cancelled out by higher inflation at home. Home goods are about 8% dearer relative to foreign goods, so competitiveness has fallen even though the currency has depreciated.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Trade-weighted index ---------- */
const TW = [0.5, 0.3, 0.2], TN = ["Partner A (50%)", "Partner B (30%)", "Partner C (20%)"], TI = [110, 95, 100];
const TX = (i) => 130 + i * 150, TY = (v) => 300 - (v - 80) * 7.5;
function twDraw(s) {
  let o = axes(70, 300, 730, 30, "", "Index (last year = 100)"); [80, 90, 100, 110, 120].forEach((v) => (o += SV.text(64, TY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TY(v), 730, TY(v), v === 100 ? "ax" : "gr", op(0.4))));
  const tw = TW.reduce((a, w, i) => a + w * TI[i], 0);
  TI.forEach((v, i) => { const k = [s.a, s.b, s.c][i]; if (k > 0) { const y = TY(100 + (v - 100) * k); o += SV.rect(TX(i) - 28, Math.min(y, TY(100)), 56, Math.abs(y - TY(100)), i === 1 ? "f2" : "f1", op(k)) + tag(TX(i), 320, TN[i], "t1", k, "middle") + tag(TX(i), (v >= 100 ? y - 8 : y + 18), v, "t1", k, "middle"); } });
  if (s.d > 0) { const y = TY(100 + (tw - 100) * s.d); o += SV.rect(TX(3) - 28, Math.min(y, TY(100)), 56, Math.abs(y - TY(100)), "f3", op(s.d)) + tag(TX(3), 320, "Weighted index", "t4", s.d, "middle") + tag(TX(3), y - 8, Lib.fmtN(tw, 1), "t4", s.d, "middle"); }
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 340, label: "Three bilateral currency indices combined into a trade-weighted index", base: { a: 0, b: 0, c: 0, d: 0 }, draw: twDraw, tween: 1200, dwell: 6000, steps: [
  { cap: "<b>Against partner A</b> (half of all trade) the currency has risen 10%: the index is 110.", s: { a: 1 } },
  { cap: "<b>Against partner B</b> (30% of trade) it has fallen 5%: the index is 95.", s: { a: 1, b: 1 } },
  { cap: "<b>Against partner C</b> (20% of trade) it is unchanged at 100.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The weighted index.</b> 0.5 × 110 + 0.3 × 95 + 0.2 × 100 = 103.5. The currency has risen 3.5% overall, because the biggest partner counts for most.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#nm") || !$("#id") || !$("#if")) return;
  const n = +$("#nm").value, pd = +$("#id").value, pf = +$("#if").value, real = ((1 + n / 100) * (1 + pd / 100) / (1 + pf / 100) - 1) * 100, rel = ((1 + pd / 100) / (1 + pf / 100) - 1) * 100;
  $("#r1").textContent = (n >= 0 ? "+" : "") + Lib.fmtN(n, 1) + "%"; $("#r2").textContent = (rel >= 0 ? "+" : "") + Lib.fmtN(rel, 1) + "%"; $("#r3").textContent = (real >= 0 ? "+" : "") + Lib.fmtN(real, 1) + "%";
  $("#rv").textContent = real > 0.5 ? `The real exchange rate has risen about ${Lib.fmtN(real, 1)}%: home goods are relatively dearer, so price competitiveness has fallen.` : real < -0.5 ? `The real exchange rate has fallen about ${Lib.fmtN(-real, 1)}%: home goods are relatively cheaper, so price competitiveness has improved.` : "The real exchange rate is almost unchanged: the nominal movement and the inflation gap cancel out, so competitiveness is about the same.";
  const Y = (v) => 150 - v * 5; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "Change (%)", "sm");
  [["Nominal", n, "f1"], ["Relative prices", rel, "f2"], ["Real", real, "f3"]].forEach(([l, v, c], i) => { const x = 70 + i * 115, y = Y(Math.max(-26, Math.min(26, v))); o += SV.rect(x, Math.min(y, 150), 70, Math.abs(y - 150), c) + SV.text(x + 35, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 35, v >= 0 ? y - 8 : y + 18, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "nm", label: "Change in the nominal rate, % (+ = appreciation) ", min: -20, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labR });
Lib.slider($("#g2"), { id: "id", label: "Domestic inflation, % ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: labR });
Lib.slider($("#g3"), { id: "if", label: "Foreign inflation, % ", min: 0, max: 15, step: 1, value: 2, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#ta") || !$("#tb") || !$("#tc")) return;
  const v = [+$("#ta").value, +$("#tb").value, +$("#tc").value], tw = 0.5 * v[0] + 0.3 * v[1] + 0.2 * v[2];
  $("#t1").textContent = Lib.fmtN(tw, 1); $("#t2").textContent = (tw >= 100 ? "+" : "") + Lib.fmtN(tw - 100, 1) + "%"; $("#t3").textContent = tw > 100.2 ? "Appreciation" : tw < 99.8 ? "Depreciation" : "No change";
  $("#tv").textContent = `Weighted index = 0.5 × ${v[0]} + 0.3 × ${v[1]} + 0.2 × ${v[2]} = ${Lib.fmtN(tw, 1)}. ${Math.abs(v[0] - 100) > Math.abs(v[2] - 100) ? "Partner A has the biggest weight, so its movement counts most." : "Partner C has the smallest weight, so its movement counts least."}`;
  const Y = (x) => 150 - (x - 100) * 5; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "Index (100 = last year)", "sm");
  [["A", v[0], "f1"], ["B", v[1], "f1"], ["C", v[2], "f1"], ["TWI", tw, "f3"]].forEach(([l, x, c], i) => { const px = 60 + i * 85, y = Y(Math.max(75, Math.min(125, x))); o += SV.rect(px, Math.min(y, 150), 55, Math.abs(y - 150), c) + SV.text(px + 27, 296, l, "sm", { "text-anchor": "middle" }) + tag(px + 27, x >= 100 ? y - 8 : y + 18, Lib.fmtN(x, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "ta", label: "Index against partner A (50% weight) ", min: 80, max: 120, step: 1, value: 110, fmt: (v) => v, onInput: labT });
Lib.slider($("#g5"), { id: "tb", label: "Index against partner B (30% weight) ", min: 80, max: 120, step: 1, value: 95, fmt: (v) => v, onInput: labT });
Lib.slider($("#g6"), { id: "tc", label: "Index against partner C (20% weight) ", min: 80, max: 120, step: 1, value: 100, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which measure is it?", ["Nominal rate", "Real rate", "Trade-weighted index"],
  [("The price of the pound in US dollars on the market today", 0), ("An exchange rate that adjusts for differences in inflation between countries", 1), ("A basket of partner currencies weighted by trade shares", 2), ("£1 = €1.15", 0), ("Shows whether home goods have become dearer relative to foreign goods", 1), ("Counts a fall against the largest trading partner more heavily", 2), ("Unchanged while home inflation is higher than abroad", 0), ("Rises when domestic prices rise faster than foreign prices at a constant nominal rate", 1)],
  "Nominal: price of one currency in another. Real: adjusts for prices. Trade-weighted: a basket, weighted by trade.") + MATCH([
  ["Nominal exchange rate", "The price of one currency in terms of another"],
  ["Real exchange rate", "The nominal rate adjusted for relative price levels"],
  ["Trade-weighted index", "The currency against a basket, weighted by trade shares"],
  ["Real effective exchange rate", "The trade-weighted index adjusted for relative prices"],
  ["Real appreciation", "Home goods become relatively dearer"],
  ["Purchasing power parity", "A theory that exchange rates move to equalise the price of goods"]]) + ORDER(
  "Put the steps for finding the change in a real exchange rate in order.",
  ["Find the change in the nominal exchange rate", "Find domestic and foreign inflation", "Work out the relative price change (domestic divided by foreign)", "Multiply the nominal index by the relative price index", "Judge the effect on competitiveness"],
  "Real rate = nominal rate × domestic prices ÷ foreign prices.") + CALC([
  {"q": "The pound rises from $1.50 to $1.65. Calculate the percentage appreciation of the pound against the dollar (%).", "a": 10, "unit": "%", "tol": 0.05, "hint": "Change ÷ original.", "sol": "(1.65 − 1.50) ÷ 1.50 = <b>10%</b>."},
  {"q": "The nominal exchange rate index rises from 100 to 105. Domestic prices rise from 100 to 108 and foreign prices from 100 to 103. Calculate the real exchange rate index (1 decimal place).", "a": 110.1, "unit": "", "tol": 0.1, "hint": "105 × 108 ÷ 103.", "sol": "105 × 108 ÷ 103 = <b>110.1</b>: a real appreciation of about 10%."},
  {"q": "A trade-weighted index uses weights of 0.5, 0.3 and 0.2. The currency indices against the three partners are 110, 95 and 100. Calculate the trade-weighted index (1 decimal place).", "a": 103.5, "unit": "", "tol": 0.05, "hint": "Multiply each index by its weight and add.", "sol": "55 + 28.5 + 20 = <b>103.5</b>."},
  {"q": "The nominal exchange rate falls by 5%. Domestic and foreign inflation are both 3%. By roughly what percentage does the real exchange rate fall (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "No relative price change.", "sol": "With equal inflation the relative price change is 0, so the real fall is <b>5%</b>."}]) + MCQ([
  ("A real exchange rate adjusts the nominal rate for:", ["Interest rates", "Relative price levels", "Trade shares", "Tariffs"], 1, "Real = nominal × domestic prices ÷ foreign prices."),
  ("A country's nominal exchange rate is unchanged and its inflation is higher than its partners'. Its real exchange rate:", ["Rises", "Falls", "Is unchanged", "Cannot be known"], 0, "Home goods have become relatively dearer, a real appreciation."),
  ("The weights in a trade-weighted exchange rate index depend on:", ["Each partner's share of the country's trade", "Each partner's population", "Each partner's inflation", "The interest rates abroad"], 0, "Larger trading partners count for more."),
  ("A real depreciation will most likely:", ["Raise price competitiveness", "Lower price competitiveness", "Have no effect", "Raise imports by itself"], 0, "Home goods become relatively cheaper for foreigners."),
  ("A country's currency rises 8% against one partner and falls 2% against another. The best summary of the overall change is:", ["A trade-weighted index", "The nominal rate against one partner", "The balance of payments", "The terms of trade"], 0, "A weighted index combines bilateral movements by trade share.")
], "qz1") + CARDS([
  ("Nominal exchange rate", "Price of one currency in another."),
  ("Real exchange rate", "Nominal rate adjusted for relative prices."),
  ("Real appreciation", "Home goods become relatively dearer; competitiveness falls."),
  ("Trade-weighted index", "Basket of currencies weighted by trade shares."),
  ("REER", "Trade-weighted index adjusted for relative prices."),
  ("Purchasing power parity", "Exchange rates adjust to equalise prices of goods."),
  ("Over-valued currency", "Above its equilibrium or PPP value."),
  ("Appreciation vs revaluation", "Floating rate vs fixed rate.")]) + MCQ(mc_exam)

build("sy1121", "measuring-exchange-rates", "Measuring Exchange Rates: Nominal, Real and Trade-Weighted", EY,
  "11.2.1: the nominal exchange rate, the real exchange rate that adjusts for relative prices, and the trade-weighted index of a currency against a basket. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
