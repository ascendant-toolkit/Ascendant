"""Syllabus 11.2.2-11.2.4 Fixed and managed exchange rate systems, revaluation and devaluation. Run: python3 tools/artifact-kit/mk_sy1122.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.2.2 to 11.2.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Under a <b class="kw">fixed exchange rate</b> the central bank sets the rate (a <b>peg</b>) and defends it by <b>buying or selling its own currency using foreign exchange reserves</b> and by adjusting interest rates. Under a <b class="kw">managed float</b> the market sets the rate day to day, but the central bank <b>intervenes to keep it within a band</b> or to smooth sharp swings. A fixed rate can only be changed by an official decision: a <b class="kw">revaluation</b> (raise the peg) or a <b class="kw">devaluation</b> (lower it), whereas a floating rate rises and falls by market forces as <b>appreciation</b> and <b>depreciation</b>. Each system gives a different answer to the same shock, and the exam asks you to compare them.</p></div>

  <h2>1 · Determination of the exchange rate (11.2.2)</h2>
  <div id="pic1" class="card"></div>
  <h3>The currency market</h3>
  <ul>
    <li>The <b>demand for a currency</b> comes from foreign buyers of the country's exports, investors who want its assets, tourists and speculators. The <b>supply</b> comes from residents buying imports and foreign assets. On a diagram the exchange rate is on the vertical axis and the quantity of the currency on the horizontal axis.</li>
    <li>In a <b>free float</b>, the equilibrium rate is where demand meets supply. A shift in demand or supply (for example higher interest rates abroad) changes the rate with no official action.</li>
  </ul>
  <h3>Fixed exchange rates</h3>
  <ul>
    <li>The government <b>announces a rate</b> (often against the US dollar, the euro or a basket) and the central bank defends it. The rate may be exactly fixed (a currency board or a peg) or held in a <b>narrow band</b>.</li>
    <li><b>If the peg is above the equilibrium</b> (the currency is over-valued): supply exceeds demand at the pegged rate. The central bank must <b>buy the excess currency</b>, paying with its foreign exchange reserves, and may <b>raise interest rates</b> to attract demand.</li>
    <li><b>If the peg is below the equilibrium</b> (under-valued): demand exceeds supply. The central bank <b>sells its currency</b> and builds up reserves, and may cut interest rates.</li>
    <li>If reserves run low and the pressure continues, the government must <b>devalue</b> or give up the peg.</li>
  </ul>
  <h3>Managed float</h3>
  <ul>
    <li>The rate is <b>mainly set by the market</b> but the central bank intervenes, often within an <b>unannounced or announced band</b>, to stop it from rising or falling too far, too quickly. This is sometimes called a <b>dirty float</b>.</li>
    <li>The tools are <b>buying or selling reserves</b> and changing <b>interest rates</b>. Within the band the market decides; at the edges the central bank acts.</li>
    <li>A <b>managed system gives some stability and some policy freedom</b> but needs reserves and can be hard to run if markets think the band will not hold.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Fixed</th><th>Managed float</th><th>Free float</th></tr>
    <tr><td><b>Who sets the rate?</b></td><td>The government and central bank</td><td>The market, with intervention</td><td>The market only</td></tr>
    <tr><td><b>Reserves needed</b></td><td>Large</td><td>Moderate</td><td>Small</td></tr>
    <tr><td><b>Interest rates</b></td><td>Used to defend the peg, so less domestic freedom</td><td>Some freedom, but the band limits it</td><td>Free to target inflation and growth</td></tr>
    <tr><td><b>Certainty for trade</b></td><td>High</td><td>Medium</td><td>Low (volatile)</td></tr>
    <tr><td><b>Balance of payments</b></td><td>No automatic adjustment; needs policy or a devaluation</td><td>Partial adjustment</td><td>Rate adjusts and tends to correct deficits</td></tr>
    <tr><td><b>Risk</b></td><td>Speculative attack if the peg looks unsustainable</td><td>Intervention may fail</td><td>Volatility, possible overshooting</td></tr>
  </table></div>

  <h2>2 · Revaluation and devaluation (11.2.3)</h2>
  <ul>
    <li><b>Devaluation</b> is a deliberate cut in the official value of a currency in a fixed (or managed) system. <b>Revaluation</b> is a deliberate rise.</li>
    <li><b>Depreciation</b> and <b>appreciation</b> are changes in the value of a <b>floating</b> currency caused by market forces. Examiners expect the right word for the system.</li>
    <li>A devaluation makes exports cheaper abroad and imports dearer at home, aiming to <b>improve the current account</b> and raise aggregate demand, at the cost of <b>imported inflation</b>. A revaluation does the opposite: it helps to lower inflation (cheaper imports and inputs) but may reduce export competitiveness.</li>
  </ul>

  <h2>3 · Changes in the exchange rate under different systems (11.2.4)</h2>
  <div class="tw"><table class="t">
    <tr><th>Shock</th><th>Floating</th><th>Fixed</th><th>Managed float</th></tr>
    <tr><td><b>Rise in demand for imports</b> (more supply of the currency)</td><td>Currency depreciates</td><td>Central bank buys currency; reserves fall; may raise interest rates</td><td>Rate falls to the band floor, then intervention</td></tr>
    <tr><td><b>Higher interest rates at home</b> (hot money inflow)</td><td>Currency appreciates</td><td>Central bank sells currency, reserves rise; interest rate gap may need to be matched</td><td>Rate rises within the band; sells currency at the ceiling</td></tr>
    <tr><td><b>Higher inflation than partners</b></td><td>Gradual depreciation</td><td>Peg becomes over-valued; devaluation likely</td><td>Band may have to be lowered</td></tr>
    <tr><td><b>Export boom</b> (more demand)</td><td>Currency appreciates</td><td>Central bank sells currency; reserves rise; risk of inflation</td><td>Rate rises within the band</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluation point</b>A fixed rate gives certainty and helps to control inflation (it forces discipline), but the country loses its own monetary policy and cannot easily adjust to shocks. A floating rate gives freedom and an automatic adjuster for the balance of payments but may be volatile. Most economies choose a managed float as a compromise.</div>
'''

watch = '''
  <h2>1 · Defending a fixed exchange rate</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stF"></div>
  <h2>2 · A managed float within a band</h2>
  <div id="stM"></div>
'''

explore = '''
  <h2>Lab 1 · Defend the peg</h2>
  <p>The currency's market equilibrium is $1.40. Shift the demand for the currency and set the official peg. See how much the central bank has to buy or sell and what happens to reserves.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Market rate</small><strong id="r1"></strong></div><div><small>Official rate</small><strong id="r2"></strong></div><div><small>Central bank action</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Currency market with the pegged exchange rate and the amount the central bank must buy or sell"></svg></div></div></div>

  <h2>Lab 2 · The same shock under three systems</h2>
  <p>A shock shifts the demand for the currency. See where the rate ends up, and what the central bank must do, under a float, a managed float (band of 1.30 to 1.50) and a peg at 1.40.</p>
  <div class="card"><div id="g3"></div><div id="tbl"></div><div class="verdict" id="tv"></div></div>
'''

practise = '''
  <h2>1 · Which system?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the defence of an over-valued peg in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Hong Kong's peg to the US dollar", "Hong Kong's currency is allowed to move only in a narrow band against the US dollar. The monetary authority buys or sells Hong Kong dollars at the edges of the band, so interest rates in Hong Kong tend to follow US rates closely and local monetary policy has little independence.", "a fixed (pegged) system: how intervention defends the rate and why the country gives up monetary independence.") +
rw("Black Wednesday, 1992", "The UK was in the European Exchange Rate Mechanism, with sterling pegged within a band. As speculators sold pounds, the Bank of England spent large reserves and raised interest rates, but the peg became impossible to hold and sterling left the system. The pound then floated down.", "a speculative attack on an over-valued peg, the limits of reserves and a forced devaluation.") +
rw("The Swiss franc floor", "From 2011 to 2015 the Swiss National Bank held a minimum rate of 1.20 francs per euro, selling francs to stop the franc from rising. In 2015 it removed the floor and the franc jumped sharply, showing how costly it can be to hold a rate far from the market level.", "a managed or semi-fixed rate with a floor, the size of intervention needed and the risk of ending it.") +
rw("China's managed float", "China sets a daily central rate for the yuan against the dollar and allows the market rate to move within a band around it, with the central bank intervening at times. The yuan has appreciated gradually over the long run while remaining tightly managed.", "a managed float: market forces within limits, with policy influence over the rate.")
)

mc_exam = [
  ("An increase or decrease in the exchange rate can occur in both floating and fixed systems, but different terms are used. Which correctly names a decrease under a floating rate and an increase under a fixed rate? (Oct/Nov 2024 · 32 · Q27, reworded)", ["Depreciation; appreciation", "Depreciation; revaluation", "Devaluation; appreciation", "Devaluation; revaluation"], 1, "A fall in a floating rate is depreciation. A deliberate rise in a fixed rate is a revaluation."),
  ("A country keeps its exchange rate against the US dollar within a narrow but changing band. What type of exchange rate is this? (Feb/March 2024 · 32 · Q28, reworded)", ["Fixed", "Floating", "Managed float", "Trade-weighted"], 2, "The rate is held within a band by the central bank but the band moves, which is a managed float."),
  ("In an open economy with a fixed exchange rate, the currency is significantly below its purchasing power parity value. If the country moves to a floating rate, which macroeconomic aim is most likely to benefit? (May/June 2025 · 32 · Q26, reworded)", ["Low inflation", "Low unemployment", "A smaller current account deficit", "Steady economic growth"], 0, "An undervalued currency would tend to appreciate when floated, making imports cheaper and lowering imported inflation, but making exports dearer."),
  ("A country devalues its currency to eliminate a balance of payments deficit. Why might this have a positive macroeconomic effect? (Feb/March 2023 · 32 · Q24, reworded)", ["Competitive pricing of exports may create employment", "Foreign importers may depreciate their own currencies and remove the advantage", "Inelastic demand for imported raw materials may cause cost inflation", "Lost import duties may reduce government support for trade promotion"], 0, "Cheaper exports can raise export sales and create jobs. The other options describe drawbacks."),
  ("In which situation is a devaluation of the currency most likely to cause inflation? (Feb/March 2024 · 32 · Q25, reworded)", ["Excess capacity is available", "Import tariffs are reduced", "Local substitutes for imported raw materials are unavailable", "The demand for exports is price inelastic"], 2, "If firms cannot replace imported inputs, the dearer imports raise costs and prices directly."),
  ("A government sets an inflation target of 3% or less. Which circumstance would make it difficult to achieve? (May/June 2025 · 32 · Q22, reworded)", ["A devaluation of the currency leads to a trade surplus", "Interest rates are raised to control demand", "The government increases its tax revenue", "Wage rises are kept in line with productivity"], 0, "A devaluation-driven rise in net exports raises aggregate demand, and dearer imports add to cost pressure, both pushing inflation up.")
]

exam = exam_page("fixed and managed exchange rates, devaluation and revaluation",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Exchange rate systems appear in the long answer questions on policy and the balance of payments, and in comparison questions. One past question is reworded below, with practice questions that follow the mark scheme style and six Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "1", "Oct/Nov 2022 (43) Q7"), ("Essay or data response, other", "see 11.2.5, 11.5.6", "Oct/Nov 2021 (43) Q7; May/June 2023 (42) Q4"), ("Multiple choice (Paper 3)", "6 shown below", "2023 to 2025")],
  [
  eq("Based on Oct/Nov 2022 · 9708/43 · Q7", "25 marks", "A government's decision to move from a fixed exchange rate to a floating exchange rate will solve unemployment in the short run but cause higher inflation in the long run. Evaluate this statement.",
     ["Explain the difference between fixed and floating exchange rates: a fixed rate is held by the central bank buying and selling currency, while a floating rate is set by supply and demand.",
      "Unemployment: under a fixed rate, lower interest rates to raise demand put downward pressure on the currency, so the central bank must sell currency or raise rates, undermining the policy. Under a float, lower interest rates cause depreciation, which also raises export demand, so policy is more effective, mainly for cyclical unemployment.",
      "Inflation: depreciation raises import prices and may cause cost-push inflation, and the central bank loses control over the money supply, which could be inflationary.",
      "Evaluation: it works for cyclical but not structural or frictional unemployment, the size of the inflation depends on import dependence, global conditions and commodity prices, and the time frame matters."],
     "Define both systems. Policy under fixed (interest rate conflict). Policy under float (depreciation helps). Inflation risk. When it does and does not work."),
  eq("Practice question · modelled on the 12 mark style (no past paper)", "12 marks", "Explain how a central bank can maintain a fixed exchange rate that is above the equilibrium rate.",
     ["Diagram: demand and supply of the currency with the peg above equilibrium, showing excess supply.",
      "The central bank buys the excess currency using foreign exchange reserves.",
      "It may raise interest rates to attract capital inflows and raise demand for the currency, and use other policies to reduce imports.",
      "Limits: reserves are finite; the cost to the domestic economy; eventually a devaluation may be needed."],
     "Diagram with excess supply. Buy currency with reserves. Raise interest rates. Limits and devaluation.",
     [[("k", "A fixed rate set above the equilibrium rate means that, at the official rate, the supply of the currency is greater than the demand. This is an over-valued currency."), ("n", "To stop the rate from falling, the central bank could buy the surplus currency in the foreign exchange market, paying for it with its reserves of foreign currency. This raises demand for the currency until it matches supply at the pegged rate.")],
      [("n", "The central bank may also raise interest rates to attract hot money inflows, which raises demand for the currency. This could reduce domestic spending and growth."), ("e", "However, reserves are limited and high interest rates are costly to the domestic economy, so if the pressure continues the government may have to devalue.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Distinguish between a depreciation and a devaluation of a currency, and explain one effect of a devaluation on an economy.",
     ["Depreciation: a fall in the value of a floating currency caused by market forces. Devaluation: a deliberate cut in the official rate by the government or central bank in a fixed system.",
      "Effect: exports become cheaper and imports dearer, so net exports may rise (current account improves), AD and employment may rise, but import prices and inflation may rise.",
      "Developed with a short chain of analysis."],
     "Two definitions. One effect with a chain.",
     [[("k", "A depreciation is a fall in the value of a floating currency due to changes in supply and demand. A devaluation is a deliberate cut in the official exchange rate under a fixed system.")],
      [("n", "A devaluation lowers the foreign price of exports and raises the home price of imports. If the Marshall-Lerner condition holds, net exports could rise, which may raise aggregate demand, output and employment."), ("e", "However, dearer imports could cause imported inflation, so the net effect may depend on the elasticities and the economy's spare capacity.")]])
  ],
  )

tips = tips_html(
  [("Use the right word.", "Floating rate: appreciation and depreciation. Fixed rate: revaluation and devaluation."),
   ("Draw the currency market.", "Exchange rate on the vertical axis, quantity of currency on the horizontal axis. Show the peg as a horizontal line."),
   ("Show the gap.", "The distance between demand and supply at the peg is what the central bank must buy or sell."),
   ("Say what pays for it.", "Buying the currency uses foreign exchange reserves, which are limited."),
   ("Link to interest rates.", "Defending a peg often means giving up an independent interest rate."),
   ("Compare, then judge.", "Fixed gives certainty but less freedom; floating gives freedom but volatility; managed is a mix."),
   ("Effects of devaluation.", "Cheaper exports and dearer imports: net exports up if elasticities are high enough, imported inflation as the cost.")],
  [("Peg", "A fixed exchange rate is maintained by the central bank buying and selling its currency using foreign exchange reserves."),
   ("Managed", "A managed float lets the market set the rate within a band, with the central bank intervening at the edges."),
   ("Devaluation", "A devaluation is a deliberate reduction in the official value of a currency under a fixed system."),
   ("Limits", "Reserves are finite, so a peg that is far from the equilibrium rate may not be sustainable."),
   ("Compare", "A floating rate may adjust automatically, whereas a fixed rate may give greater certainty but less policy independence.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Currency market ---------- */
const EQ = (sh, ss) => ({ q: 50 + (sh + ss) / 2, e: 1.4 + 0.006 * (sh - ss) });
const FX = (q) => 70 + q * 6.2, FY = (e) => 300 - (e - 0.8) * 220;
function fxDraw(s) {
  const sh = s.sh || 0, ss = s.ss || 0, eq = EQ(sh, ss), peg = s.peg || 0, lo = s.lo || 0, hi = s.hi || 0;
  let o = axes(70, 300, 730, 30, "Quantity of the currency", "Exchange rate ($ per £)"); [1.0, 1.2, 1.4, 1.6, 1.8].forEach((v) => (o += SV.text(64, FY(v) + 4, v.toFixed(1), "sm", { "text-anchor": "end" })));
  const D = (dd) => [[FX(0), FY(2.0 + 0.012 * dd)], [FX(100), FY(2.0 - 1.2 + 0.012 * dd)]], S = (dd) => [[FX(0), FY(0.8 - 0.012 * dd)], [FX(100), FY(2.0 - 0.012 * dd)]];
  if (sh) o += SV.line(...D(0)[0], ...D(0)[1], "c1 dash", op(0.35)); if (ss) o += SV.line(...S(0)[0], ...S(0)[1], "c3 dash", op(0.35));
  const d = D(sh), sp = S(ss);
  o += SV.line(...d[0], ...d[1], "c1") + tag(FX(90), FY(2.0 - 0.012 * (90 - sh)) - 8, "D", "t1", 1, "middle") + SV.line(...sp[0], ...sp[1], "c3") + tag(FX(100) - 4, sp[1][1] - 8, "S", "t3", 1, "end");
  if (lo > 0) o += SV.line(70, FY(lo), 730, FY(lo), "c4 dash", op(0.8)) + SV.line(70, FY(hi), 730, FY(hi), "c4 dash", op(0.8)) + tag(726, FY(hi) - 6, "upper limit " + hi.toFixed(2), "t4", 1, "end") + tag(726, FY(lo) + 16, "lower limit " + lo.toFixed(2), "t4", 1, "end");
  let r = eq.e; if (peg > 0) r = peg; else if (lo > 0) r = Math.max(lo, Math.min(hi, eq.e));
  const qd = (2.0 - r) / 0.012 + sh, qs = (r - 0.8) / 0.012 + ss, gap = qd - qs;
  if (peg > 0) o += SV.line(70, FY(peg), 730, FY(peg), "c4") + tag(80, FY(peg) - 8, "Peg " + peg.toFixed(2), "t4");
  o += SV.circle(FX(eq.q), FY(eq.e), 6, "dot2") + tag(FX(eq.q) + 8, FY(eq.e) + 20, "market " + eq.e.toFixed(2), "t2");
  if ((peg > 0 || lo > 0) && Math.abs(gap) > 1 && (peg > 0 || r !== eq.e)) {
    const a = Math.min(qd, qs), b = Math.max(qd, qs); o += SV.line(FX(a), FY(r), FX(b), FY(r), "c2", { "stroke-width": 5 }) + tag((FX(a) + FX(b)) / 2, FY(r) + (gap > 0 ? 28 : -14), gap > 0 ? "excess demand " + Lib.fmtN(gap, 0) + ": bank SELLS currency" : "excess supply " + Lib.fmtN(-gap, 0) + ": bank BUYS currency", "t2", 1, "middle");
  }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Currency market with a peg above the equilibrium exchange rate and the excess supply the central bank must buy">${fxDraw({ peg: 1.6 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 340, label: "A fixed exchange rate above equilibrium: excess supply, central bank buying the currency and eventual devaluation", base: { sh: 0, ss: 0, peg: 0, lo: 0, hi: 0 }, draw: fxDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>Market equilibrium.</b> Demand for and supply of the currency meet at $1.40. In a free float this would be the exchange rate.", s: {} },
  { cap: "<b>The peg.</b> The government fixes the rate at $1.60, above equilibrium. At that rate the supply of pounds (67) is greater than the demand (33): excess supply of 33.", s: { peg: 1.6 } },
  { cap: "<b>Defending the peg.</b> To stop the pound from falling, the central bank <b>buys the 33 surplus units</b> with foreign exchange reserves, and may raise interest rates to attract demand.", s: { peg: 1.6 } },
  { cap: "<b>Devaluation.</b> If reserves run low and pressure continues, the government lowers the official rate. A fall to about $1.40 removes the gap and ends the need to intervene.", s: { peg: 1.4 } },
] });
Lib.stepper($("#stM"), { w: 760, h: 340, label: "A managed float with a band: market movement inside the band and intervention at the upper limit", base: { sh: 0, ss: 0, peg: 0, lo: 1.3, hi: 1.5 }, draw: fxDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>A band.</b> The central bank allows the rate to float between $1.30 and $1.50. At equilibrium ($1.40) there is no intervention.", s: { sh: 0, lo: 1.3, hi: 1.5 } },
  { cap: "<b>A small rise in demand</b> moves the market rate to about $1.46. This is inside the band, so the market decides and the central bank does nothing.", s: { sh: 10, lo: 1.3, hi: 1.5 } },
  { cap: "<b>A large rise in demand</b> would push the rate to about $1.58, above the upper limit. The central bank <b>sells the currency</b> to hold the rate at $1.50 (excess demand of about 13 is met).", s: { sh: 30, lo: 1.3, hi: 1.5 } },
  { cap: "<b>The judgement.</b> A managed float gives stability while the market rate is in the band, but if the shock is lasting the central bank may need to move the band, which is like a revaluation.", s: { sh: 30, lo: 1.4, hi: 1.6 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#sd") || !$("#pg")) return;
  const sh = +$("#sd").value, pg = +$("#pg").value / 100, eq = EQ(sh, 0), qd = (2.0 - pg) / 0.012 + sh, qs = (pg - 0.8) / 0.012, gap = qd - qs;
  $("#r1").textContent = "$" + eq.e.toFixed(2); $("#r2").textContent = "$" + pg.toFixed(2); $("#r3").textContent = Math.abs(gap) < 0.5 ? "None needed" : gap > 0 ? "Sells " + Lib.fmtN(gap, 0) : "Buys " + Lib.fmtN(-gap, 0);
  $("#rv").textContent = Math.abs(gap) < 0.5 ? "The peg equals the market rate, so no intervention is needed." : gap > 0 ? `The peg ($${pg.toFixed(2)}) is below the market rate ($${eq.e.toFixed(2)}): demand for the currency exceeds supply by ${Lib.fmtN(gap, 0)}. The central bank sells its currency and its reserves of foreign exchange rise. The currency is under-valued.` : `The peg ($${pg.toFixed(2)}) is above the market rate ($${eq.e.toFixed(2)}): supply of the currency exceeds demand by ${Lib.fmtN(-gap, 0)}. The central bank must buy the excess using its reserves. The currency is over-valued and reserves will fall.`;
  $("#labA").innerHTML = (() => { const X = (q) => 40 + q * 3.5, Y = (e) => 270 - (e - 0.8) * 200; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Quantity of the currency", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Exchange rate ($ per £)", "sm");
    o += SV.line(X(0), Y(2.0 + 0.012 * sh), X(100), Y(0.8 + 0.012 * sh), "c1") + SV.line(X(0), Y(0.8), X(100), Y(2.0), "c3") + SV.line(40, Y(pg), 400, Y(pg), "c4") + SV.circle(X(eq.q), Y(eq.e), 6, "dot2");
    if (Math.abs(gap) > 0.5) o += SV.line(X(Math.min(qd, qs)), Y(pg), X(Math.max(qd, qs)), Y(pg), "c2", { "stroke-width": 5 });
    return o + tag(44, Y(pg) - 8, "peg " + pg.toFixed(2), "t4"); })();
}
Lib.slider($("#g1"), { id: "sd", label: "Shift in demand for the currency ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labF });
Lib.slider($("#g2"), { id: "pg", label: "Pegged rate, $ per £ × 100 ", min: 120, max: 170, step: 5, value: 160, fmt: (v) => (v / 100).toFixed(2), onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labS() {
  if (!$("#sk")) return;
  const sh = +$("#sk").value, eq = EQ(sh, 0), band = Math.max(1.3, Math.min(1.5, eq.e)), act = (r) => { const g = (2.0 - r) / 0.012 + sh - (r - 0.8) / 0.012; return Math.abs(g) < 0.5 ? "none" : g > 0 ? "sells " + Lib.fmtN(g, 0) : "buys " + Lib.fmtN(-g, 0); };
  const rows = [["Floating", "$" + eq.e.toFixed(2), "none", eq.e > 1.41 ? "appreciation" : eq.e < 1.39 ? "depreciation" : "no change"], ["Managed (1.30 to 1.50)", "$" + band.toFixed(2), act(band), band > 1.41 ? "rises within the limits" : band < 1.39 ? "falls within the limits" : "no change"], ["Fixed at 1.40", "$1.40", act(1.4), "no change in the rate; reserves move"]];
  $("#tbl").innerHTML = `<div class="tw"><table class="t"><tr><th>System</th><th>Exchange rate</th><th>Central bank</th><th>What happens</th></tr>${rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("")}</table></div>`;
  $("#tv").textContent = sh === 0 ? "No shock: all three systems have the same rate." : Math.abs(eq.e - 1.4) < 0.101 ? "A small shock stays inside the band, so the managed float lets the market decide and does not need to intervene. The peg needs intervention from the first unit." : "A large shock: the float moves furthest, the managed float is held at its limit by intervention, and the peg is held at 1.40 by the biggest intervention. This shows the trade-off between stability and reserves.";
}
Lib.slider($("#g3"), { id: "sk", label: "Shift in demand for the currency (shock) ", min: -40, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which exchange rate system is it?", ["Fixed", "Managed float", "Free float"],
  [("The central bank holds the rate at exactly $1.60 by buying and selling", 0), ("The rate moves within a band; the central bank steps in at the limits", 1), ("Only market supply and demand set the rate", 2), ("Requires a large stock of foreign exchange reserves", 0), ("Gives the country the most freedom to set its own interest rates", 2), ("A 'dirty' float", 1), ("A devaluation changes the official rate", 0), ("Offers a compromise between stability and flexibility", 1)],
  "Fixed: the central bank sets it. Managed: market within limits. Free float: market only.") + MATCH([
  ["Peg", "An official exchange rate maintained by the central bank"],
  ["Devaluation", "A deliberate cut in the official rate of a fixed currency"],
  ["Revaluation", "A deliberate rise in the official rate of a fixed currency"],
  ["Depreciation", "A market-driven fall in a floating currency"],
  ["Managed float", "A market rate with central bank intervention to limit moves"],
  ["Foreign exchange reserves", "Stocks of foreign currency held by the central bank"]]) + ORDER(
  "Put the defence of an over-valued peg in order.",
  ["The peg is set above the equilibrium rate", "Supply of the currency exceeds demand at the peg", "The central bank buys the surplus currency", "Foreign exchange reserves fall", "If reserves run low, the currency is devalued"],
  "Excess supply, intervention, falling reserves, possible devaluation.") + CALC([
  {"q": "A fixed rate of $1.60 is devalued to $1.40. Calculate the percentage devaluation (%).", "a": 12.5, "unit": "%", "tol": 0.05, "hint": "Change ÷ original.", "sol": "(1.60 − 1.40) ÷ 1.60 = <b>12.5%</b>."},
  {"q": "A currency pegged at €1.20 is revalued to €1.26. Calculate the percentage revaluation (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "6 cents on 120.", "sol": "0.06 ÷ 1.20 = <b>5%</b>."},
  {"q": "At the pegged rate the demand for a currency is 30m units and supply is 45m units. How many units must the central bank buy (m)?", "a": 15, "unit": "m", "tol": 0.05, "hint": "Excess supply.", "sol": "45 − 30 = <b>15m</b> units."},
  {"q": "A central bank holds $90bn of reserves and sells $6bn a month to defend a peg. For how many months can it continue (months)?", "a": 15, "unit": "months", "tol": 0.05, "hint": "90 ÷ 6.", "sol": "<b>15 months</b>, if the pressure stays the same."}]) + MCQ([
  ("A rise in a fixed exchange rate decided by the government is called:", ["Appreciation", "Revaluation", "Devaluation", "Depreciation"], 1, "Revaluation is the official rise under a fixed system."),
  ("To defend a peg that is above the equilibrium rate, the central bank must:", ["Sell its currency", "Buy its currency", "Cut interest rates", "Print more money"], 1, "Buying the surplus currency raises demand to match supply at the peg."),
  ("A feature of a managed float is that:", ["The central bank intervenes to keep the rate within limits", "The rate never moves", "Reserves are never used", "The government sets all prices"], 0, "The market sets the rate within a band, with intervention at the edges."),
  ("Which is an advantage of a fixed exchange rate?", ["Certainty for traders", "Independent interest rates", "Automatic adjustment of the balance of payments", "No need for reserves"], 0, "A stable rate reduces risk for trade and investment."),
  ("A devaluation is most likely to:", ["Raise the price of imports", "Lower the price of imports", "Lower the price of exports at home", "End inflation"], 0, "The home currency price of imports rises.")
], "qz1") + CARDS([
  ("Fixed exchange rate", "Central bank sets and defends the rate."),
  ("Managed float", "Market within a band, with intervention."),
  ("Devaluation", "Deliberate fall in the official rate."),
  ("Revaluation", "Deliberate rise in the official rate."),
  ("Over-valued peg", "Peg above equilibrium: bank buys the currency."),
  ("Under-valued peg", "Peg below equilibrium: bank sells the currency."),
  ("Reserves", "Foreign currency held by the central bank."),
  ("Trade-off", "Fixed: stability but less freedom. Float: freedom but volatility.")]) + MCQ(mc_exam)

build("sy1122", "fixed-managed-exchange-rate-systems", "Fixed and Managed Exchange Rate Systems", EY,
  "11.2.2 to 11.2.4: how the exchange rate is determined under fixed and managed systems, how central banks defend a peg, devaluation and revaluation, and how the rate changes under each system. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
