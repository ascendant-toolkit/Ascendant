"""AS syllabus 3.2.5 Buffer stock schemes. Run: python3 tools/artifact-kit/mk_as35.py"""
from asx import *
EY = EYAS("3.2.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">buffer stock scheme</b> aims to <b>stabilise the price</b> of a product, usually an agricultural good, whose supply varies with the weather. A government agency sets a <b>minimum (floor) price</b> and a <b>maximum (ceiling) price</b>: when a good harvest pushes the price down to the floor, it <b>buys the surplus into storage</b>; when a poor harvest pushes the price up to the ceiling, it <b>sells from its stock</b>. This <b>smooths prices and farmers' incomes</b> and protects consumers from price spikes, but it needs <b>money to buy and store the crop</b>, a stock big enough to last, and a correctly judged price band. If the band is set too high, the agency buys too much and costs rise; if poor harvests run on, the <b>stock can run out</b> and the scheme collapses.</p></div>

  <h2>1 · How the scheme works (3.2.5)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Why prices fluctuate:</b> the supply of crops is <b>price inelastic</b> in the short run and affected by weather, while demand for food is also inelastic, so small shifts in supply cause <b>big price swings</b>.</li>
    <li><b>Good harvest:</b> supply shifts right, price would fall below the floor, so the agency <b>buys up the excess</b> at the minimum price.</li>
    <li><b>Poor harvest:</b> supply shifts left, price would rise above the ceiling, so the agency <b>sells from the stock</b> at the maximum price.</li>
    <li>In an average year, little action is needed. Over time the agency should buy and sell about the same amount, so the stock stays close to a safe level.</li>
  </ul>

  <h2>2 · Stock levels over time</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Stable farm incomes</b>: encourages investment and long-run supply of food</td><td><b>Cost</b> of buying and storing; storage space and spoilage (perishable crops)</td></tr>
    <tr><td><b>Stable prices for consumers</b>, especially low-income households spending much on food</td><td><b>Hard to set the right price band</b>; a floor above the long-run equilibrium causes growing surpluses</td></tr>
    <tr><td>Reduces the risk of famine or panic when harvests fail</td><td><b>The stock can run out</b> after a run of bad years, or the agency can run out of money in a run of good years</td></tr>
    <tr><td>Smooths foreign exchange earnings for countries relying on one crop</td><td>May encourage <b>over-production</b> and inefficiency; <b>opportunity cost</b> of the funds; can be affected by corruption</td></tr>
  </table></div>

  <h2>3 · Why are agricultural prices so unstable?</h2>
  <ul>
    <li><b>Supply is unpredictable:</b> weather, disease and pests change the size of the harvest from year to year, shifting the supply curve.</li>
    <li><b>Supply is inelastic in the short run:</b> farmers cannot change output once the crop is planted, so they cannot respond to price within the season.</li>
    <li><b>Demand is inelastic:</b> food is a necessity, so a fall in price does not raise quantity demanded by much.</li>
    <li><b>Result:</b> with both curves steep, a small shift in supply leads to a large change in price. Example: if the quantity supplied falls by 10% and the price elasticity of demand is −0.5, the price must rise by about 20% to restore equilibrium.</li>
    <li><b>Farmers' incomes can fall in a good harvest:</b> if demand is inelastic, price falls by a larger percentage than quantity rises, so total revenue falls.</li>
    <li><b>Planning problem:</b> farmers decide how much to plant on last year's price, so output may overshoot and undershoot, and unstable income discourages investment in the long run.</li>
  </ul>

  <h2>4 · Worked example</h2>
  <p>Demand is P = 90 − Q. The agency sets a floor price of $40 and a ceiling of $60. In a normal year supply is P = 10 + Q (equilibrium $50, quantity 40).</p>
  <div class="tw"><table class="t">
    <tr><th>Year</th><th>Without the scheme</th><th>With the scheme</th></tr>
    <tr><td><b>Good harvest</b>, supply P = Q − 30 (shifts right)</td><td>Supply P = Q − 30 gives 90 − Q = Q − 30, so Q = 60 and the price falls to $30</td><td>At the $40 floor, consumers buy 50 but producers supply 70, so the agency buys 20 units</td></tr>
    <tr><td><b>Poor harvest</b>, supply P = 50 + Q (shifts left)</td><td>Supply P = 50 + Q gives 90 − Q = 50 + Q, so Q = 20 and the price rises to $70</td><td>At the $60 ceiling, consumers want 30 but producers supply only 10, so the agency sells 20 units from stock</td></tr>
    <tr><td><b>Cost of buying 20 units</b> at $40</td><td>None</td><td>$800, to be recovered when the stock is sold at higher prices</td></tr>
  </table></div>
  <ul>
    <li>The scheme works if the agency <b>buys when prices are low and sells when they are high</b>, so the stock cycles around a safe level. If the floor is set above the long-run equilibrium, the agency keeps buying and the stock grows without limit.</li>
  </ul>

  <h2>5 · Why schemes fail, and alternatives</h2>
  <ul>
    <li><b>Running out of stock:</b> several years of poor harvests exhaust the stock, and the agency can no longer hold the price down.</li>
    <li><b>Running out of money:</b> several good harvests require the agency to keep buying, and it may not be able to finance it. For example, the International Tin Council's scheme ended in the mid-1980s when it ran short of funds.</li>
    <li><b>Wrong price band:</b> a floor set too high is just a minimum price with growing surpluses; too low and farmers get no protection.</li>
    <li><b>Storage costs and spoilage</b> for perishable goods; opportunity cost of the money tied up.</li>
    <li><b>Alternatives:</b> subsidies or income support for farmers, crop insurance, futures contracts and diversification into other crops or products, and improved storage and information.</li>
  </ul>

  <h2>6 · Who gains and who loses?</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Effect</th></tr>
    <tr><td><b>Farmers</b></td><td>More stable incomes, a guaranteed minimum price and the confidence to invest; may lose from extra output they cannot sell at a high price</td></tr>
    <tr><td><b>Consumers</b></td><td>Protected from price spikes; may pay higher average prices if the floor is set high</td></tr>
    <tr><td><b>Government or agency</b></td><td>Bears the cost of buying and storing; may gain when it sells at higher prices</td></tr>
    <tr><td><b>Taxpayers</b></td><td>Pay if the scheme makes a loss</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Draw the floor and ceiling prices and show <b>both</b> a good and a poor harvest on supply and demand diagrams, labelling what the agency buys and sells. Evaluate with <b>cost</b>, <b>running out of stock</b>, whether the band is <b>set correctly</b> and alternatives such as <b>subsidies</b> or <b>futures markets</b>.</div>
'''

watch = '''
  <h2>1 · Buying in a good year, selling in a poor year</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stB"></div>
  <h2>2 · Eight years of harvests</h2>
  <div id="stY"></div>
'''

explore = '''
  <h2>Lab 1 · Set the price band</h2>
  <p>Choose the size of the harvest shock (negative = poor harvest) and the price band. Normal price is $50.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Price without scheme</small><strong id="r1"></strong></div><div><small>Price with scheme</small><strong id="r2"></strong></div><div><small>Agency action</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a price band and the agency buying or selling"></svg></div></div></div>

  <h2>Lab 2 · When does the stock run out?</h2>
  <p>A run of poor harvests. The agency starts with some stock and must sell the shortfall each year at the ceiling price of $55.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Sold per year</small><strong id="t1"></strong></div><div><small>Stock lasts</small><strong id="t2"></strong></div><div><small>Price after run-out</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Bars of the stock held each year falling to zero"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Buy or sell?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put a poor harvest in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Grain reserves", "Some countries hold national reserves of rice or wheat. In a good year the government buys grain from farmers at a guaranteed price; in a shortage it releases stock at a set price to keep bread and rice affordable.", "buying at the floor and selling at the ceiling.") +
rw("Coffee exporters", "Countries that depend on coffee exports can see their incomes swing with world prices. A stock scheme can smooth them, but past international schemes failed when prices stayed above the band and stocks grew too large to finance.", "cost and the risk of setting the band too high.") +
rw("Poor harvest years", "After a drought the agency sells stock, so prices rise less than they otherwise would. If droughts last several years the reserve runs out, and prices then jump to the free market level.", "stock running out.") +
rw("Food price spikes", "Rising food prices hit low-income households hardest because they spend a large share of income on food. A release of stored food can hold prices down at a critical time.", "the case for buffer stocks and the equity argument.") +
rw("Coffee and cocoa price swings", "Countries that rely on one crop see export income and farmers' earnings swing with world prices. A stabilisation scheme could smooth these swings, but needs finance and a correct price band.", "price instability for a single-crop economy.") +
rw("A run of poor harvests", "A government agency sells grain from its stock to stop prices rising above the ceiling. After several bad years the stock runs out, the ceiling cannot be defended and prices jump.", "why buffer stocks can fail.")
)

mc_exam = [
  mcq("m21_12", 12, "The market for wheat is in equilibrium at price P with supply at 40 million tonnes. Due to a drought in the growing season, supply falls to 20 million tonnes. Which immediate action should be taken to maintain the equilibrium price of P?", ["grant a subsidy to farmers equivalent to the rise in price", "impose an indirect tax equivalent to the rise in price", "plant more wheat to increase supplies to 40 million tonnes", "use existing stocks of wheat to increase supplies by 20 million tonnes"], 3, "Planting takes a season, and subsidies or taxes would not restore supply at once. Releasing existing stocks does."),
  mcq("w23_11", 12, "Which event is most likely to enable firms to respond to an increase in demand by increasing supply rather than by raising price?", ["Firms reduce their expenditure on the training of workers", "Import duties are increased on machines that increase the speed of production", "The government introduces buffer stock schemes for the goods produced by the firm", "Trade unions become strong, leading to poor labour productivity"], 2, "A buffer stock can be released to meet demand, so supply rises instead of price."),
  mcq("s25_13", 14, "A country depends heavily on the production of an agricultural product, good X. It decides to introduce a buffer stock scheme for good X. The government allocates a fixed amount of money for setting up and running the scheme. In which situation is the scheme least likely to run out of money? (new farmers can start growing good X easily or with difficulty; the cost of storing good X is high or low; global demand for good X is constant or rising)", ["easy to start, high storage cost, constant demand", "easy to start, low storage cost, rising demand", "difficult to start, high storage cost, constant demand", "difficult to start, low storage cost, rising demand"], 3, "Difficult entry limits new supply, low storage costs reduce spending, and rising demand keeps prices above the floor so the agency buys less.")
]

exam = exam_page("buffer stock schemes",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Buffer stocks are a 12 mark Paper 2 discussion in some series, with a 4 mark data-response version, and appear in Paper 1 occasionally. Reworded past questions are below, with three Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 12 marks", "2", "May/June 2023 (21) Q3(b); May/June 2023 (23) Q3(b)"), ("Data response, 4 marks", "1", "Oct/Nov 2024 (23) Q1(c)"), ("Multiple choice (Paper 1)", "3 shown below", "2020 to 2025")],
  [
  eq(P("s23_21", "3(b)"), "12 marks", "With the help of a diagram, assess whether the benefits of a buffer stock scheme for an agricultural product always outweigh its disadvantages.",
     ["Analysis (up to 8): a correctly labelled diagram showing a price band, with the agency buying in a good harvest and selling in a poor one; the benefits, such as stable prices and farm incomes, encouraging investment and long-term supply, and protecting consumers (up to 4); the disadvantages, such as the cost of buying and storing, spoilage, setting the band wrongly, running out of stock or money, and the opportunity cost (up to 4). Indicative content may include these points.",
      "Evaluation (up to 4): a judgement on whether the benefits always outweigh the disadvantages, which may depend on the size of the stock, the length of the run of harvests and the price band, with a conclusion."],
     "Diagram with floor and ceiling. Benefits: stable prices, income, investment. Disadvantages: cost, run out, wrong band. Judge: not always.",
     [[("n", "A buffer stock agency sets a minimum and a maximum price. In a good harvest supply shifts right, so it buys the surplus to hold the price at the floor, and in a poor harvest supply shifts left and it sells from the stock to hold the price at the ceiling. Stable prices protect farmers' incomes, encourage investment in the long run and keep food affordable for poor households. But buying and storing is costly, crops may spoil, the agency must judge the right price band, and a series of poor harvests could exhaust the stock, while a floor set too high would build up surpluses.")], [("e", "The benefits are likely to outweigh the costs when harvests fluctuate around a stable average and the band is well chosen. They may not if the floor is above the long-run equilibrium, if the stock is too small, or if storage is very expensive, so the benefits do not always outweigh the disadvantages.")]]),
  eq(P("s23_23", "3(b)"), "12 marks", "Assess the effectiveness of government intervention through buffer stock schemes in agricultural markets.",
     ["Analysis (up to 8): how the scheme works and why agricultural prices fluctuate (inelastic supply and demand, weather); how it stabilises prices and incomes (up to 4); the limits on effectiveness, such as the cost, finite stocks, errors in setting the band, perishability, and the effect on producers' incentives (up to 4).",
      "Evaluation (up to 4): a judgement on how effective the schemes are, with reasons and a conclusion."],
     "How it works. Effective in stabilising price and income. Limits: cost, stock, wrong band. Judge: effective for short-term fluctuations, less for long-run trends.",
     [[("n", "Agricultural prices swing because supply depends on the weather and both supply and demand are inelastic. A buffer stock buys when the price falls to the floor and sells when it reaches the ceiling, which reduces swings and gives farmers stable incomes, so they invest more and supply is more reliable. However, running the scheme costs money for purchases, storage and administration, the stock is finite, and an incorrect price band either wastes money or fails to stabilise.")], [("e", "Buffer stocks are likely to be effective at smoothing short-run fluctuations, but not at dealing with a long-term fall in demand or prices, since the stock would grow without limit. Overall, effectiveness depends on correctly forecasting the long-run price and on the scheme having enough funds.")]]),
  eq(P("w24_23", "1(c)"), "4 marks", "Prices of a country's main export crop, coffee beans, have fluctuated sharply over the past decade. Consider whether a buffer stock scheme is likely to be successful in reducing these price fluctuations.",
     ["Up to 2 marks for explaining how a buffer stock scheme works to reduce price fluctuations: buying in a surplus at the floor price and selling in a shortage at the ceiling (up to 2).", "Up to 2 marks for considering whether it will be successful, such as the cost, the size of stocks, difficulties setting the price band, storage and the length of price swings (up to 2)."],
     "How it works (floor and ceiling). Limits: cost, stock, band. Conclude.",
     [[("k", "A buffer stock scheme buys coffee beans when the price falls to a set minimum and sells from the stock when it reaches a set maximum, which should narrow price swings."), ("n", "It would probably help in the short run, if swings come from harvest variation. But storing coffee is costly, the stock may run out after several poor years, and if the price falls for a long period the agency would have to keep buying, so its success is uncertain.")]])
  ],
  )

tips = tips_html(
  [("Draw floor and ceiling.", "Show buying in a good harvest and selling in a poor one."),
   ("Explain why prices swing.", "Weather shifts supply; supply and demand are inelastic."),
   ("Name the aim.", "Stabilise prices and farmers' incomes."),
   ("List costs.", "Buying, storage, spoilage, administration."),
   ("Mention running out.", "A run of bad harvests empties the stock."),
   ("Band must be right.", "A floor above the long-run price builds surpluses."),
   ("Compare with alternatives.", "Subsidies, futures markets, diversification.")],
  [("Buffer stock", "A buffer stock scheme aims to stabilise the price by buying and selling."),
   ("Floor price", "At the minimum price the agency buys the surplus."),
   ("Ceiling price", "At the maximum price the agency sells from its stock."),
   ("Cost", "The scheme is costly to run and the stock is finite."),
   ("Assess", "The benefits may not always outweigh the disadvantages.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
function bsDraw(s) {
  const fl = 45, ce = 55; let o = sdPlot({ d: 0, s: s.s, g: 0, n: 1 }, { S1: "S (normal)", S2: "S (this year)" });
  o += SV.line(70, SDY(fl), 720, SDY(fl), "c4", { "stroke-width": 2, "stroke-dasharray": "7 4" }) + tag(724, SDY(fl) + 14, "Floor $45", "c4", 1, "end") + SV.line(70, SDY(ce), 720, SDY(ce), "c4", { "stroke-width": 2, "stroke-dasharray": "7 4" }) + tag(724, SDY(ce) - 6, "Ceiling $55", "c4", 1, "end");
  const ec = sdEq(0, s.s);
  if (ec.p < fl - 0.5) { const qd = (90 - fl) / 0.8, qs = (fl - 10) / 0.8 + s.s; o += SV.rect(SDX(qd), SDY(fl) - 8, SDX(qs) - SDX(qd), 16, "f2", op(0.75)) + tag(SDX(qs) + 8, SDY(fl) + 4, "agency buys " + Lib.fmtN(qs - qd, 1), "c2"); }
  if (ec.p > ce + 0.5) { const qd = (90 - ce) / 0.8, qs = (ce - 10) / 0.8 + s.s; o += SV.rect(SDX(qs), SDY(ce) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.75)) + tag(SDX(qd) + 8, SDY(ce) + 4, "agency sells " + Lib.fmtN(qd - qs, 1), "c3"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A good harvest shifts supply right and the agency buys the surplus at the floor price">${bsDraw({ s: 25 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A buffer stock scheme with a price band of $45 to $55", base: { s: 0 }, draw: bsDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A normal year.</b> The market clears at $50, inside the price band of $45 to $55, so the agency does nothing.", s: { s: 0 } },
  { cap: "<b>A good harvest.</b> Supply shifts right and the price would fall to $40, below the floor. The agency buys about 12.5 units at $45 and stores them.", s: { s: 25 } },
  { cap: "<b>A poor harvest.</b> Supply shifts left and the price would rise to $60, above the ceiling. The agency sells about 12.5 units from its stock at $55.", s: { s: -25 } },
] });

/* ---------- eight years ---------- */
const SH = [0, 25, -25, 10, -25, -25, 25, 0], FLO = 45, CEI = 55;
function yearSim() { let stock = 20, out = []; SH.forEach((s) => { const free = 50 - 0.4 * s; let buy = 0, sell = 0, p = free; if (free < FLO) { buy = Math.max(0, s - 12.5); p = FLO; } else if (free > CEI) { sell = Math.max(0, -s - 12.5); if (sell > stock) { sell = stock; p = free; } else p = CEI; } stock = stock + buy - sell; out.push({ free, p, stock }); }); return out; }
const SIM = yearSim();
function yrDraw(s) {
  const x = (i) => 90 + i * 80, y = (p) => 200 - (p - 35) * 5; let o = SV.line(60, 200, 740, 200) + SV.line(60, 40, 60, 200) + SV.text(66, 34, "Price ($)", "sm") + SV.line(60, y(FLO), 740, y(FLO), "c4", { "stroke-dasharray": "6 4" }) + SV.line(60, y(CEI), 740, y(CEI), "c4", { "stroke-dasharray": "6 4" }) + SV.text(56, y(FLO) + 4, "45", "sm", { "text-anchor": "end" }) + SV.text(56, y(CEI) + 4, "55", "sm", { "text-anchor": "end" });
  const n = Math.round(s.t); let a = "", b = "";
  SIM.forEach((r, i) => { if (i < n) { a += (i ? " L" : "M") + x(i) + "," + y(r.free); b += (i ? " L" : "M") + x(i) + "," + y(r.p); o += SV.rect(x(i) - 14, 270 - r.stock * 2, 28, r.stock * 2, "f2", op(0.6)) + SV.text(x(i), 286, "Y" + (i + 1), "sm", { "text-anchor": "middle" }) + SV.text(x(i), 264 - r.stock * 2, Lib.fmtN(r.stock, 0), "sm", { "text-anchor": "middle" }); } });
  if (a) o += SV.path(a, "c1", { fill: "none", "stroke-width": 2, "stroke-dasharray": "5 4" }) + SV.path(b, "c2", { fill: "none", "stroke-width": 3 }) + tag(742, 60, "Stock (bars)", "c2", 1, "end");
  return o + SV.text(60, 226, "Dashed = free-market price; solid = price with the scheme", "sm");
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Price with and without the scheme over eight years, with stock levels as bars">${yrDraw({ t: 8 })}</svg>`;
Lib.stepper($("#stY"), { w: 760, h: 300, label: "Harvests, prices and stocks over eight years", base: { t: 0 }, draw: yrDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The band</b> is $45 to $55. The agency starts with 20 units of stock.", s: { t: 0 } },
  { cap: "<b>Years 1 to 3.</b> A good harvest in year 2 (price would be $40): the agency buys and stock rises. A poor harvest in year 3 (price would be $60): it sells and stock falls. Prices stay in the band.", s: { t: 3 } },
  { cap: "<b>Years 4 to 5.</b> Another poor harvest in year 5 draws the stock down further, to a low level.", s: { t: 5 } },
  { cap: "<b>Years 6 to 8.</b> Another poor harvest in year 6 <b>exhausts the stock</b>: the agency can no longer hold the price, which jumps to the free-market level.", s: { t: 8 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!$("#sh") || !$("#fl") || !$("#ce")) return;
  const s = +$("#sh").value, fl = +$("#fl").value, ce = +$("#ce").value, free = 50 - 0.4 * s, qd = (p) => (90 - p) / 0.8, qs = (p) => (p - 10) / 0.8 + s;
  let p = free, act = "None";
  if (free < fl) { p = fl; act = "Buys " + Lib.fmtN(qs(fl) - qd(fl), 1); } else if (free > ce) { p = ce; act = "Sells " + Lib.fmtN(qd(ce) - qs(ce), 1); }
  $("#r1").textContent = "$" + Lib.fmtN(free, 1); $("#r2").textContent = "$" + Lib.fmtN(p, 1); $("#r3").textContent = act;
  $("#rv").textContent = fl >= ce ? "The floor must be below the ceiling." : act === "None" ? `The free-market price of $${Lib.fmtN(free, 1)} is inside the band of $${fl} to $${ce}, so the agency does nothing.` : free < fl ? `The harvest would push the price down to $${Lib.fmtN(free, 1)}, below the floor of $${fl}. The agency buys ${act.slice(5)} units and stores them, holding the price at $${fl}.` : `The shortfall would push the price up to $${Lib.fmtN(free, 1)}, above the ceiling of $${ce}. The agency sells ${act.slice(6)} units from stock, holding the price at $${ce}.`;
  let o = sdPlot({ d: 0, s, g: 0, n: 1 }) + SV.line(70, SDY(fl), 720, SDY(fl), "c4", { "stroke-dasharray": "7 4", "stroke-width": 2 }) + SV.line(70, SDY(ce), 720, SDY(ce), "c4", { "stroke-dasharray": "7 4", "stroke-width": 2 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sh", label: "Harvest shock (negative = poor, positive = good) ", min: -30, max: 30, step: 5, value: 25, fmt: (v) => v, onInput: labB });
Lib.slider($("#g2"), { id: "fl", label: "Floor price, $ ", min: 35, max: 50, step: 1, value: 45, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "ce", label: "Ceiling price, $ ", min: 50, max: 65, step: 1, value: 55, fmt: (v) => "$" + v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!$("#st0") || !$("#bad")) return;
  const S0 = +$("#st0").value, s = +$("#bad").value, sell = Math.max(0, s - 12.5), yrs = sell > 0 ? Math.floor(S0 / sell) : Infinity, free = 50 + 0.4 * s;
  $("#t1").textContent = sell > 0 ? Lib.fmtN(sell, 1) : "None"; $("#t2").textContent = sell > 0 ? yrs + " year" + (yrs === 1 ? "" : "s") : "Indefinitely"; $("#t3").textContent = "$" + Lib.fmtN(free, 0);
  $("#tv").textContent = sell <= 0 ? "The shortfall is small enough that the price stays inside the band without any sales, so the stock is not used." : `Each poor year the agency must sell ${Lib.fmtN(sell, 1)} units to hold the price at $55. A stock of ${S0} lasts about ${yrs} year${yrs === 1 ? "" : "s"}. After that the scheme cannot hold the price and it jumps to about $${Lib.fmtN(free, 0)}.`;
  let o = SV.line(60, 250, 740, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Stock (units)", "sm"), st = S0;
  for (let i = 0; i < 8; i++) { const h = Math.max(0, st) * (200 / 80); o += SV.rect(90 + i * 80 - 16, 250 - h, 32, h, "f2", op(0.65)) + SV.text(90 + i * 80, 268, "Year " + (i + 1), "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 80, 244 - h, Lib.fmtN(Math.max(0, st), 0), "sm", { "text-anchor": "middle" }); st = Math.max(0, st - sell); }
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "st0", label: "Starting stock, units ", min: 10, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labR });
Lib.slider($("#g5"), { id: "bad", label: "Size of the poor harvest each year (units of supply lost) ", min: 15, max: 40, step: 1, value: 25, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What does the agency do?", ["Buys into stock", "Sells from stock", "Does nothing"],
  [("Good harvest: price falls to the floor", 0), ("Poor harvest: price rises to the ceiling", 1), ("Price is inside the band", 2), ("Bumper crop pushes price below the minimum", 0), ("Drought pushes price above the maximum", 1), ("Market price equals the long-run average", 2), ("A surplus builds up at the floor price", 0), ("Stocks are released to hold the price down", 1)],
  "Buy at the floor, sell at the ceiling, do nothing in between.") + MATCH([
  ["Buffer stock scheme", "A scheme that buys and sells to stabilise a price"],
  ["Floor price", "The minimum price at which the agency buys"],
  ["Ceiling price", "The maximum price at which the agency sells"],
  ["Price band", "The range between the floor and the ceiling"],
  ["Run out of stock", "A risk after a series of poor harvests"],
  ["Storage cost", "A cost of buying surplus in good years"]]) + ORDER(
  "Put what happens after a poor harvest in order.",
  ["A drought cuts the harvest", "Supply shifts to the left", "The price rises towards the ceiling", "The agency sells from its stock", "The price is held at the ceiling"],
  "Poor harvest, price up, agency sells.") + CALC([
  {"q": "At the floor price of $45 the agency buys 12.5 units. How much does it spend ($)?", "a": 562.5, "unit": "$", "tol": 1, "hint": "45 × 12.5.", "sol": "<b>$562.50</b>."},
  {"q": "The agency holds 20 units and must sell 12.5 each poor year. How many full years does the stock last?", "a": 1, "unit": "years", "tol": 0.1, "hint": "20 ÷ 12.5 rounded down.", "sol": "<b>1 year</b>, with 7.5 left."},
  {"q": "The free-market price would be $60 but the ceiling is $55. By what percentage does the scheme cut the price?", "a": 8.3, "unit": "%", "tol": 0.2, "hint": "5 ÷ 60.", "sol": "<b>8.3%</b>."},
  {"q": "A scheme sells 12.5 units at $55. What revenue does the agency receive ($)?", "a": 687.5, "unit": "$", "tol": 1, "hint": "55 × 12.5.", "sol": "<b>$687.50</b>."}]) + MCQ([
  ("A buffer stock scheme aims to:", ["Stabilise price", "Raise price permanently", "Lower price permanently", "Ban imports"], 0, "Stability."),
  ("In a good harvest the agency:", ["Buys the surplus", "Sells stock", "Cuts the floor", "Taxes farmers"], 0, "Price is pushed down."),
  ("A main risk of a buffer stock scheme is:", ["Running out of stock or money", "Too little storage demand", "Lower taxes", "Fewer buyers"], 0, "Finite stock."),
  ("Agricultural prices fluctuate because:", ["Supply varies and demand and supply are inelastic", "Demand is always elastic", "Supply is fixed", "Prices are set by the government"], 0, "Weather and inelasticity."),
  ("A floor price above the long-run equilibrium will:", ["Build up growing surpluses", "Cut surpluses", "Raise demand", "Have no effect"], 0, "The agency keeps buying.")
], "qz1") + CARDS([
  ("Buffer stock", "Buy and sell to stabilise price."),
  ("Floor", "Buy at the minimum price."),
  ("Ceiling", "Sell at the maximum price."),
  ("Good harvest", "Agency buys."),
  ("Poor harvest", "Agency sells."),
  ("Cost", "Buying, storage, spoilage."),
  ("Risk", "Stock or money runs out."),
  ("Alternatives", "Subsidies, futures markets.")]) + MCQ(mc_exam)

build("as35", "as-buffer-stocks", "Buffer Stock Schemes", EY,
  "3.2.5: how buffer stock schemes use a price floor and ceiling to stabilise agricultural prices, with the costs, risks and limits. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
