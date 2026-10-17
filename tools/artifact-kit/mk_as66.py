"""AS syllabus 6.4.1-6.4.4 Exchange rate systems and determination. Run: python3 tools/artifact-kit/mk_as66.py"""
from as6k import *
EY = EYAS("6.4.1 to 6.4.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An <b class="kw">exchange rate</b> is the price of one currency in terms of another. In a <b class="kw">floating</b> system it is determined by the <b>demand for and supply of the currency</b>: demand comes from overseas buyers of the country's <b>exports</b>, <b>inward investment</b>, <b>deposits attracted by higher interest rates</b> and speculators; supply comes from residents buying <b>imports</b>, <b>investing abroad</b> and moving savings to higher interest rates elsewhere. A <b class="kw">depreciation</b> (a fall) is caused by a fall in demand or a rise in supply; an <b class="kw">appreciation</b> by a rise in demand or a fall in supply. In a <b class="kw">fixed</b> system the government or central bank sets the rate and defends it by <b>buying or selling the currency using reserves</b> or by <b>changing interest rates</b>, while a <b class="kw">managed float</b> lets the rate move but with occasional intervention.</p></div>

  <h2>1 · Floating exchange rates</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Effect on the currency</th><th>Examples</th></tr>
    <tr><td><b>Demand for the currency rises</b></td><td>Appreciation</td><td>Higher export demand, inward investment, higher interest rates, speculation that it will rise</td></tr>
    <tr><td><b>Demand falls</b></td><td>Depreciation</td><td>Lower export demand, a fall in interest rates, loss of confidence</td></tr>
    <tr><td><b>Supply rises</b></td><td>Depreciation</td><td>More imports, investment abroad, higher interest rates abroad (savers move funds)</td></tr>
    <tr><td><b>Supply falls</b></td><td>Appreciation</td><td>Fewer imports, less investment abroad</td></tr>
  </table></div>
  <ul>
    <li><b>Relative inflation:</b> if a country's inflation is above that of its trading partners, its exports become less competitive and imports more attractive, so demand falls, supply rises and the currency may depreciate.</li>
    <li><b>Relative interest rates:</b> higher rates may attract "hot money", raising demand for the currency, but the effect depends on confidence and expectations.</li>
    <li><b>Trade-weighted exchange rate:</b> an average of exchange rates against several currencies, weighted by the amount of trade with each.</li>
  </ul>

  <h2>2 · Fixed and managed rates</h2>
  <ul>
    <li><b>How a fixed rate is defended:</b> if the currency is falling, the central bank <b>buys it using reserves</b> (raising demand) and/or <b>raises interest rates</b>; if rising, it <b>sells it</b> and/or lowers interest rates.</li>
    <li><b>Devaluation and revaluation:</b> an official lowering or raising of a fixed rate.</li>
    <li><b>Advantages:</b> certainty for traders and investors, and may help control inflation.</li>
    <li><b>Disadvantages:</b> needs <b>large reserves</b>; interest rates may have to be set to defend the rate rather than for domestic aims; may become misaligned with the rate the market would set.</li>
    <li><b>Floating:</b> adjusts automatically and needs fewer reserves, but is more volatile and uncertain for traders.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Draw the diagram with <b>exchange rate</b> on the vertical axis and <b>quantity of the currency</b> on the horizontal axis, label D and S, and explain <b>which curve shifts and why</b> before stating the change in the rate. For a fixed rate, explain intervention using <b>reserves and interest rates</b>.</div>
'''

watch = '''
  <h2>1 · A depreciation of a floating exchange rate</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Defending a fixed exchange rate</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Shift demand and supply for the currency</h2>
  <p>Equilibrium starts at an exchange rate of 50 (an index). Move the two curves to see what happens.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Exchange rate</small><strong id="r1"></strong></div><div><small>Quantity traded</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand and supply of a currency with the exchange rate on the vertical axis"></svg></div></div></div>

  <h2>Lab 2 · Defend a fixed rate</h2>
  <p>The rate is fixed at 50. Lower the demand for the currency to see how much the central bank must buy.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Excess supply of currency</small><strong id="t1"></strong></div><div><small>Market rate without the peg</small><strong id="t2"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="A fixed exchange rate above the market rate, with excess supply of the currency"></svg></div></div></div>
'''

practise = practise_html("Demand for or supply of the currency?", "Match the term to its description", "Put a depreciation in order")

real = RWNOTE + (
rw("Rising interest rates", "When a central bank raises interest rates, overseas savers may move money into that currency, raising demand and the exchange rate. The effect depends on confidence and what is expected next.", "interest rates and the demand for a currency.") +
rw("A boom in imports", "Households and firms buy more foreign goods and need foreign currency, so supply of the domestic currency rises and the exchange rate may fall.", "imports and the supply of a currency.") +
rw("A central bank defends a peg", "A country that fixes its currency to the dollar must buy its own currency when it is under pressure. If reserves run low, it may have to devalue or raise interest rates sharply.", "fixed exchange rates and reserves.") +
rw("Speculation", "If traders expect a currency to fall, they sell it, which can push the rate down further and faster than the fundamentals alone would suggest.", "speculation and exchange rates.")
)

mc_exam = [
  mcq("m25_12", 27, "When is a country's exchange rate most likely to fall?", ["When its current account surplus exceeds that of its trading partners.", "When its inflation rate exceeds that of its trading partners.", "When its interest rate exceeds that of its trading partners.", "When its unemployment rate exceeds that of its trading partners."], 1, "Higher relative inflation reduces competitiveness, lowering demand for the currency and raising supply."),
  mcq("s22_12", 20, "What does a trade-weighted exchange rate attempt to take account of?", ["a country's terms of trade", "international trade as a proportion of a country's national income", "the relative value of international trade done with a country's trading partners", "the size of a country's current account surplus or deficit"], 2, "It weights each exchange rate by the amount of trade with that partner."),
  mcq("s22_12", 23, "A country operates a fixed exchange rate system. What will put pressure on the country to devalue its currency?", ["a decrease in the country's inflation rate relative to the inflation rates of other countries", "a decrease in the tariffs on its products imposed by other countries", "an increase in its current account balance of payments deficit with other countries", "an increase in the country's interest rate relative to the interest rates of other countries"], 2, "A bigger deficit raises supply of the currency relative to demand, putting downward pressure on the rate."),
  mcq("s22_11", 27, "The central bank of an economy decides to raise interest rates in order to attract capital inflows and improve the financial account of the balance of payments. When is the central bank's decision least likely to be effective?", ["when the currency of the economy is expected to lose its value", "when the economy is politically and economically stable", "when the interest rate of the economy is higher than that of other countries", "when the reserves of foreign currencies held by the central bank are high and rising"], 0, "If the currency is expected to fall, investors may not move funds in even at higher rates."),
  mcq("m20_12", 30, "A country with a fixed exchange rate experiences a balance of payments surplus. Which policy measure will enable it to maintain its exchange rate?", ["decreasing government borrowing", "decreasing government spending", "decreasing the interest rate", "decreasing the money supply"], 2, "Lower interest rates reduce demand for the currency, offsetting the upward pressure.")
]

exam = exam_page("exchange rate determination and systems",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Exchange rate determination is a very common 8 mark Paper 2 part, often with a diagram of the currency market. Reworded past questions are below, with five Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "4", "May/June 2021 (21) Q4(a); Oct/Nov 2021 (21) Q4(a); May/June 2022 (21) Q4(a); May/June 2025 (22) Q5(a)"), ("Multiple choice (Paper 1)", "5 shown below", "2020 to 2025")],
  [
  eq(P("s21_21", "4(a)"), "8 marks", "With the aid of a diagram(s), explain one demand factor and one supply factor that would cause the value of a currency in a floating exchange rate system to depreciate.",
     ["Knowledge (up to 2): a correctly labelled diagram with the exchange rate (the price of one currency in terms of another) on the vertical axis and the quantity of currency on the horizontal axis (1), with market equilibrium shown (1).",
      "Application (up to 6): an explanation of one reason for a fall in demand for the currency, such as less demand for the country's goods and services or a fall in its interest rate (1 for identification and up to 2 for explanation); and one reason for an increase in supply of the currency, such as higher interest rates in other countries or more demand for imports (1 + up to 2)."],
     "Diagram: axes, D, S, equilibrium. Demand factor: less demand for exports or a lower interest rate. Supply factor: more imports or higher foreign rates.",
     [[("k", "In a floating system the exchange rate is the price of one currency in terms of another, set by demand and supply. The diagram shows the exchange rate on the vertical axis, the quantity of the currency on the horizontal axis, a downward-sloping demand curve and an upward-sloping supply curve meeting at the equilibrium rate.")], [("n", "A fall in demand for the currency could come from lower foreign demand for the country's exports. Fewer overseas buyers need the currency, so demand shifts left and the rate falls. A rise in supply could come from higher interest rates in other countries, as savers sell the domestic currency to move funds abroad, or from more spending on imports, so supply shifts right and the rate falls further.")]]),
  eq(P("w21_21", "4(a)"), "8 marks", "With the aid of a diagram, explain how a central bank intervenes to maintain a fixed exchange rate when the economy is experiencing a current account deficit on its balance of payments.",
     ["Knowledge (up to 2): a correct diagram with the axes labelled (exchange rate or price of one currency in terms of another, and quantity of currency) (1), and demand and supply curves labelled (1).",
      "Application (up to 6): an explanation that a current account deficit puts downward pressure on the exchange rate (up to 3): demand for imports exceeds foreign demand for exports, so domestic demand for foreign currency exceeds foreign demand for the domestic currency; and an explanation of how the central bank intervenes (up to 3): by buying the domestic currency using its foreign currency reserves and/or by raising interest rates."],
     "Diagram with the fixed rate above the market rate. Deficit: supply of currency exceeds demand. Intervention: buy the currency with reserves, raise interest rates.",
     [[("k", "The diagram shows the exchange rate against the quantity of the currency, with demand and supply curves. The fixed rate is held above the rate the market would set, so at the fixed rate the supply of the currency exceeds the demand for it.")], [("n", "A current account deficit means spending on imports is greater than receipts from exports, so more of the domestic currency is supplied to buy foreign currency than is demanded by foreigners. This puts downward pressure on the exchange rate. To maintain the rate, the central bank may buy the domestic currency using its reserves of foreign currency, which raises demand, and may raise interest rates to attract foreign savings, which also raises demand. Both have costs, as reserves are limited and higher interest rates may slow the economy.")]]),
  eq(P("s22_21", "4(a)"), "8 marks", "Explain why fixed exchange rates could cause difficulties for a country that has one.",
     ["Knowledge (up to 2): a fixed exchange rate is determined by the government or central bank (1) and is therefore not determined by demand and supply (1).",
      "Application (up to 6): one difficulty applied to a country with a fixed rate (1 for identification and up to 2 for explanation), such as the need for sufficient reserves to intervene, and another difficulty (1 + up to 2), such as being reluctant to change interest rates because it conflicts with other economic aims."],
     "Define a fixed rate. Difficulties: needs reserves; interest rates tied to the peg; the rate may become misaligned.",
     [[("k", "A fixed exchange rate is a rate set by the government or central bank rather than by the forces of demand and supply in the foreign exchange market.")], [("n", "A country may need large reserves of foreign currency to intervene by buying its own currency when it comes under downward pressure, and if these run out it may be forced to devalue. The central bank may also have to use interest rates to defend the rate. For example, it may need to raise rates to attract funds even when the economy is weak and lower rates would be better for growth and employment, so domestic aims could conflict with the exchange rate target.")]]),
  eq(P("s25_22", "5(a)"), "8 marks", "With the help of a diagram, explain two ways in which a fall in the balance of trade in goods may affect the value of a floating exchange rate and consider the extent to which a change in the relative rate of interest between two countries may have a greater impact on the exchange rate.",
     ["Knowledge (up to 3): a fully labelled diagram (1), showing that an increase in demand for imports may increase the supply of the currency and lower its price (1), and that a fall in demand for exports may reduce the demand for the currency and lower its price (1).",
      "Analysis (up to 3): the impact of a change in relative interest rates on the demand and supply of the currency through hot money flows, for example a higher relative rate attracting savings, raising demand for the currency (up to 2); and that the extent depends on confidence in the country and other factors (up to 2).",
      "Evaluation (up to 2): a judgement on whether interest rates could have a greater impact, with a conclusion."],
     "Imports up: supply of currency up. Exports down: demand down. Both lower the rate. Interest rates: hot money, but depends on confidence and other factors. Judge.",
     [[("k", "The diagram shows demand and supply of the currency. A rise in imports increases the supply of the domestic currency, as more is sold to buy foreign currency, and a fall in exports reduces demand for it, as fewer foreigners need it. Both lower the equilibrium exchange rate.")], [("n", "A higher interest rate relative to another country may attract savings from abroad, raising demand for the currency and its value. But this depends on confidence in the economy and on expectations about the currency, and other factors such as a large trade deficit may offset it.")], [("e", "Relative interest rates could have a greater impact in the short run, because funds can move quickly, while trade effects may matter more over time. The extent depends on how large the interest rate difference is and how confident investors are.")]])
  ],
  )

tips = tips_html(
  [("Axes right.", "Exchange rate vertical; quantity of currency horizontal."),
   ("Label D and S.", "Demand and supply of the currency, with equilibrium."),
   ("Name the shift.", "Which curve moves and why, then the new rate."),
   ("Demand and supply factors.", "Exports, investment, interest rates; imports, investing abroad."),
   ("Fixed rate.", "Reserves and interest rates."),
   ("Costs of a fixed rate.", "Reserves run out; interest rates conflict."),
   ("Hedge.", "Use may and could for effects.")],
  [("Exchange rate", "The exchange rate is the price of one currency in terms of another."),
   ("Appreciation", "An appreciation is a rise in the value of a floating currency."),
   ("Depreciation", "A depreciation is a fall in the value of a floating currency."),
   ("Devaluation", "A devaluation is an official fall in a fixed exchange rate."),
   ("Hot money", "Hot money is short-term funds that move between countries for higher interest.")],
  [CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
const exLab = { x: "Quantity of currency", y: "Exchange rate", D1: "D", D2: "D1", S1: "S", S2: "S1", P1: "R", Q1: "Q", P2: "R1", Q2: "Q1" };
function exDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }, exLab); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in demand for a currency lowers the exchange rate">${exDraw({ d: -20, s: 0, n: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A fall in demand for the currency lowers the exchange rate", base: { d: 0, s: 0, n: 0 }, draw: exDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The demand for and supply of the currency meet at an exchange rate of 50.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Demand falls</b>, for example because foreigners buy fewer of the country's exports. The demand curve shifts left.", s: { d: -20, s: 0, n: 1 } },
  { cap: "<b>The exchange rate falls</b> to 42: a <b>depreciation</b>. Exports now look cheaper abroad and imports dearer at home.", s: { d: -20, s: 0, n: 1 } },
  { cap: "<b>Alternatively, supply rises</b> (more imports or higher interest rates abroad). The supply curve shifts right and the rate also falls to 42.", s: { d: 0, s: 20, n: 1 } },
] });

function pegDraw(s) {
  const d = s.d, qd = d + 50, qs = 50, e = sdEq(d, 0);
  let o = sdPlot({ d: d, s: 0, g: 0, n: 1 }, exLab) + SV.line(70, SDY(50), 720, SDY(50), "c3", { "stroke-width": 2.5, ...op(s.k) }) + tag(724, SDY(50) - 6, "Fixed rate", "c3", s.k, "end");
  if (s.k > 0 && d < -0.5) o += SV.line(SDX(qd), SDY(50) + 16, SDX(qs), SDY(50) + 16, "c4", { "stroke-width": 3, ...op(s.k) }) + SV.text(SDX((qd + qs) / 2), SDY(50) + 32, "Excess supply: bank buys " + Lib.fmtN(qs - qd, 0), "sm", { "text-anchor": "middle", ...op(s.k) });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A central bank defends a fixed exchange rate", base: { d: 0, k: 0 }, draw: pegDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The rate is fixed at 50</b>, which is the market rate at the start.", s: { d: 0, k: 1 } },
  { cap: "<b>Demand for the currency falls</b>, for example after a rise in the current account deficit. At the fixed rate the supply of the currency exceeds demand.", s: { d: -20, k: 1 } },
  { cap: "<b>The central bank buys the surplus currency</b> using its foreign currency reserves (20 units here), and may raise interest rates, until demand matches supply at 50.", s: { d: -20, k: 1 } },
  { cap: "<b>The limit:</b> reserves are finite. If they run low, the country may have to devalue or accept higher interest rates.", s: { d: -20, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const d = +$("#g1v").value, s = +$("#g2v").value, e = sdEq(d, s);
  $("#r1").textContent = Lib.fmtN(e.p, 1); $("#r2").textContent = Lib.fmtN(e.q, 1);
  const ch = e.p - 50;
  $("#rv").textContent = Math.abs(ch) < 0.5 ? "The exchange rate is roughly unchanged at 50." : (ch < 0 ? "Depreciation" : "Appreciation") + `: the rate moves from 50 to ${Lib.fmtN(e.p, 1)}. ` + (d < -0.5 ? "Demand for the currency has fallen (e.g. fewer exports or lower interest rates). " : d > 0.5 ? "Demand for the currency has risen (e.g. more exports or higher interest rates). " : "") + (s > 0.5 ? "Supply has risen (e.g. more imports or higher foreign interest rates)." : s < -0.5 ? "Supply has fallen (e.g. fewer imports)." : "");
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 }, exLab);
}
Lib.slider($("#g1"), { id: "g1v", label: "Shift in demand for the currency ", min: -30, max: 30, step: 5, value: -20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Shift in supply of the currency ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labA });
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#g3v")) return;
  const d = +$("#g3v").value, e = sdEq(d, 0), ex = -d;
  $("#t1").textContent = ex > 0 ? Lib.fmtN(ex, 0) + " units" : "None"; $("#t2").textContent = Lib.fmtN(e.p, 1);
  $("#tv").textContent = ex > 0 ? `With demand down by ${ex}, the market rate would fall to ${Lib.fmtN(e.p, 1)}. To hold the rate at 50 the central bank must buy ${ex} units of its own currency using reserves, and may raise interest rates. The larger the shift, the faster reserves fall.` : "Demand has not changed, so the fixed rate matches the market rate and no intervention is needed.";
  $("#labB").innerHTML = pegDraw({ d, k: 1 });
}
Lib.slider($("#g3"), { id: "g3v", label: "Fall in demand for the currency ", min: -30, max: 0, step: 5, value: -20, fmt: (v) => v, onInput: labB });
labB();
''' + CLASSIFY("cl1", "Does it affect the demand for or the supply of the currency?", ["Demand for the currency", "Supply of the currency"],
  [("Foreigners buy more of the country's exports", 0), ("Residents buy more imports", 1), ("A higher interest rate attracts foreign savings", 0), ("Residents invest in firms abroad", 1), ("Inward foreign direct investment rises", 0), ("Savers move funds abroad for higher interest", 1), ("Speculators expect the currency to rise", 0), ("Tourists from this country spend more overseas", 1)],
  "Demand comes from foreign buyers who need the currency; supply comes from residents who sell the currency to buy foreign currency.") + MATCH([
  ["Appreciation", "A rise in the value of a floating currency"],
  ["Depreciation", "A fall in the value of a floating currency"],
  ["Devaluation", "An official fall in a fixed exchange rate"],
  ["Trade-weighted rate", "An average of rates weighted by trade with each partner"],
  ["Hot money", "Short-term funds that move for higher interest"],
  ["Reserves", "Foreign currency held by the central bank"]]) + ORDER(
  "Put the steps in a depreciation in order.",
  ["Foreign demand for exports falls", "Demand for the currency falls", "The demand curve shifts left", "The exchange rate falls", "Exports become cheaper abroad"],
  "Demand falls, the curve shifts and the rate falls.") + CALC([
  {"q": "£1 = $1.25. A UK good costs £200. What is its price in $?", "a": 250, "unit": "$", "tol": 0.5, "hint": "200 × 1.25.", "sol": "<b>$250</b>."},
  {"q": "The pound depreciates to £1 = $1.10. What is the $ price of the £200 good?", "a": 220, "unit": "$", "tol": 0.5, "hint": "200 × 1.10.", "sol": "<b>$220</b>."},
  {"q": "What is the % change in the exchange rate from $1.25 to $1.10?", "a": -12, "unit": "%", "tol": 0.1, "hint": "(1.10 − 1.25) ÷ 1.25.", "sol": "<b>-12%</b>."},
  {"q": "At £1 = $1.10, a US good costs $330. What is its price in £?", "a": 300, "unit": "£", "tol": 0.5, "hint": "330 ÷ 1.10.", "sol": "<b>£300</b>."}]) + MCQ([
  ("The exchange rate is:", ["The price of one currency in terms of another", "The interest rate", "The inflation rate", "A tax on imports"], 0, "The price of a currency."),
  ("A rise in demand for a currency causes:", ["An appreciation", "A depreciation", "A devaluation", "No change"], 0, "Higher demand raises its value."),
  ("A fixed rate is defended by:", ["Buying or selling the currency and changing interest rates", "Tariffs only", "Lowering taxes", "Letting demand and supply decide"], 0, "Intervention with reserves and interest rates."),
  ("Higher inflation than trading partners is likely to:", ["Lower the exchange rate", "Raise the exchange rate", "Fix the exchange rate", "Not matter"], 0, "Exports lose competitiveness."),
  ("A devaluation is:", ["An official fall in a fixed rate", "A market fall in a floating rate", "A rise in the rate", "A tax"], 0, "Set by the authorities.")
], "qz1") + CARDS([
  ("Exchange rate", "Price of a currency."),
  ("Appreciation", "Floating rate rises."),
  ("Depreciation", "Floating rate falls."),
  ("Demand for currency", "Exports, investment, interest rates."),
  ("Supply of currency", "Imports, investing abroad."),
  ("Fixed rate", "Set and defended."),
  ("Intervention", "Reserves and interest rates."),
  ("Hot money", "Moves for interest rates.")]) + MCQ(mc_exam)

build("as66", "as-exchange-rate-determination", "Exchange Rates: Systems and Determination", EY,
  "6.4.1 to 6.4.4: floating, fixed and managed exchange rates and what moves them, with currency market diagrams. Animations, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
