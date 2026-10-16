"""Builds the IGCSE Economics 2.1.1 How markets work review.
Run: python3 tools/artifact-kit/mk_ig21.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">market</span> is where <b>buyers and sellers meet</b> to trade goods, services or resources. It does not have to be a place: it can be online or by phone. Buyers (demand) want goods at low prices; sellers (supply) want high prices. <b>Prices</b> send signals that help answer the three basic economic questions: what, how and who to produce for.</p></div>

  <h2>Buyers and sellers</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Buyers (consumers)</th><th>Sellers (producers)</th></tr>
    <tr><td><b>Role</b></td><td>Demand goods and services to satisfy wants</td><td>Supply goods and services to earn income and profit</td></tr>
    <tr><td><b>Aim</b></td><td>Get the most satisfaction for their money; pay a low price</td><td>Maximise revenue and profit; charge a high price</td></tr>
    <tr><td><b>Reaction to a higher price</b></td><td>Buy less</td><td>Supply more</td></tr>
    <tr><td><b>Examples</b></td><td>Households, firms buying inputs, governments</td><td>Shops, farmers, manufacturers, workers selling labour</td></tr>
  </table></div>

  <h2>Examples of markets</h2>
  <ul>
    <li><b>Goods markets:</b> the market for cars, coffee or smartphones.</li>
    <li><b>Services markets:</b> hairdressing, banking, tourism.</li>
    <li><b>Factor (resource) markets:</b> the labour market (firms buy labour, workers sell it), the land market, the capital goods market.</li>
    <li><b>Financial markets:</b> shares, loans, foreign exchange.</li>
    <li><b>Local and global:</b> a farmers' market, an online shop, the world oil market.</li>
  </ul>

  <h2>The price mechanism</h2>
  <p>The <span class="kw">price mechanism</span> is how <b>prices adjust</b> to the actions of buyers and sellers, allocating scarce resources. Prices act as <b>signals</b> and <b>incentives</b>:</p>
  <ul>
    <li>A <b>rise in demand</b> raises the price and profit, so firms produce more of that good (what to produce).</li>
    <li>Firms use the <b>cheapest methods</b> to keep costs low and profit high (how to produce).</li>
    <li>Goods go to those <b>willing and able to pay</b> the price (who to produce for).</li>
  </ul>
  <p class="note">Demand means <b>willing and able to pay</b>: wanting a good is not enough without the money to buy it.</p>
'''
js = HEAD + COMMON + '''
const TR = ["Buyers want goods and are willing and able to pay", "Sellers offer goods at the price they need to cover costs and make profit", "They agree a price and trade", "Buyers receive goods; sellers receive income", "The price tells both sides how to act next"];
Lib.stepper($("#stT"), { w: 760, h: 380, label: "A market transaction", base: { n: 0 }, draw: mkChain(TR, "--accent"), steps: chainSteps(["<b>Buyers</b> want goods and are willing and able to pay.", "<b>Sellers</b> offer goods at a price that covers costs and makes a profit.", "They <b>agree a price</b> and trade.", "Buyers receive goods; sellers receive <b>income</b>.", "The <b>price</b> tells both sides how to act next."]) });
const PM = ["Consumers want more of a good", "Demand rises and the price rises", "Higher profit attracts firms: they produce more", "Resources move into this good", "The market has answered 'what to produce'"];
Lib.stepper($("#stP"), { w: 760, h: 380, label: "The price mechanism at work", base: { n: 0 }, draw: mkChain(PM, "--good"), steps: chainSteps(["Consumers want <b>more of a good</b>.", "Demand rises and the <b>price rises</b>.", "Higher profit attracts firms: they <b>produce more</b>.", "<b>Resources move</b> into this good.", "The market has answered <b>what to produce</b>."]) });

/* Lab 1: market price and trades */
const BUY = [90, 80, 70, 60, 50, 40, 30, 20], SELL = [20, 30, 40, 50, 60, 70, 80, 90];
function labM() {
  if (!$("#pa")) return;
  const p = +$("#pa").value, nb = BUY.filter((v) => v >= p).length, ns = SELL.filter((v) => v <= p).length, q = Math.min(nb, ns), rev = q * p;
  $("#pa1").textContent = nb; $("#pa2").textContent = ns; $("#pa3").textContent = q;
  $("#pav").textContent = `At a price of $${p}, ${nb} buyers are willing to buy and ${ns} sellers are willing to sell. ${nb > ns ? "More want to buy than sell: a shortage, so the price tends to rise." : nb < ns ? "More want to sell than buy: a surplus, so the price tends to fall." : "Buyers and sellers match: the market clears."} ${q} trades take place (revenue $${rev}).`;
  const base = 290; let o = SV.line(60, base, 700, base);
  BUY.forEach((v, i) => { const x = 80 + i * 76, ok = v >= p, h = v * 2; o += SV.rect(x, base - h, 30, h, "", { style: "fill:var(--accent)", opacity: ok ? 0.85 : 0.25 }) + SV.rect(x + 32, base - SELL[i] * 2, 30, SELL[i] * 2, "", { style: "fill:var(--warn)", opacity: SELL[i] <= p ? 0.85 : 0.25 }); });
  o += SV.line(60, base - p * 2, 700, base - p * 2, "gr") + SV.text(700, base - p * 2 - 6, "Price $" + p, "lbl bd", { "text-anchor": "end" }) + SV.text(60, 24, "Blue: most each buyer will pay. Orange: least each seller will accept.", "sm");
  $("#labM").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Market price", min: 10, max: 100, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labM });
const MK = [
  { n: "A farmers' market", t: "Goods market", b: "Shoppers", s: "Farmers" },
  { n: "An online shop", t: "Goods market", b: "Online shoppers", s: "The retailer" },
  { n: "Hairdressing", t: "Services market", b: "Customers", s: "Hairdressers" },
  { n: "The labour market", t: "Factor market", b: "Firms (buy labour)", s: "Workers (sell labour)" },
  { n: "The stock market", t: "Financial market", b: "Investors", s: "Share owners" },
  { n: "The world oil market", t: "Global commodity market", b: "Importing countries and firms", s: "Oil producers" },
];
button_table("mkBtns", "mkOut", MK, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Buyers</th><th>Sellers</th></tr><tr><td><b>${p.t}</b></td><td>${p.b}</td><td>${p.s}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of market</b> is each?", buckets: [{ label: "Goods market" }, { label: "Services market" }, { label: "Factor market" }, { label: "Financial market" }], items: [
  { text: "Cars", b: 0 }, { text: "Coffee", b: 0 },
  { text: "Hairdressing", b: 1 }, { text: "Tourism", b: 1 },
  { text: "The labour market", b: 2 }, { text: "Rented farmland", b: 2 },
  { text: "Foreign exchange", b: 3 }, { text: "Shares", b: 3 },
], done: "Goods, services, factors, finance." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>buyer</b> or a <b>seller</b> in the market named?", buckets: [{ label: "Buyer" }, { label: "Seller" }], items: [
  { text: "A shopper in a supermarket", b: 0 }, { text: "A firm hiring workers (labour market)", b: 0 }, { text: "A government buying medicines", b: 0 },
  { text: "A farmer selling wheat", b: 1 }, { text: "A worker offering labour (labour market)", b: 1 }, { text: "A shop selling clothes", b: 1 },
], done: "Both sides are needed for a market." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market", "Where buyers and sellers meet to trade"],
  ["Demand", "Willingness and ability to buy at a price"],
  ["Supply", "Willingness and ability to sell at a price"],
  ["Price mechanism", "Prices adjusting to allocate resources"],
  ["Price signal", "Information from prices to buyers and sellers"],
  ["Incentive", "A reason to act, such as profit"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the price mechanism reallocates resources</b>.", items: [
  "Consumers want more of a good",
  "Demand rises and the price rises",
  "Profit in that market rises",
  "Firms produce more of it",
  "Resources move into its production",
], done: "The price mechanism in action." });
''' + calc_js([
    ("At a price of $50, 5 buyers want to buy and 4 sellers want to sell. How many units are in shortage?", 1, "5 − 4 = <b>1</b>.", None, None),
    ("A market sells 200 units at $12. What is the total revenue ($)?", 2400, "200 × 12 = <b>$2,400</b>.", None, None),
]) + mcq_js("qz1", [
    ("A market is:", ["A place only", "Where buyers and sellers meet to trade", "A shop", "A government"], 1, "It can be online."),
    ("Which is a factor market?", ["The labour market", "The car market", "The coffee market", "A hairdresser"], 0, "Resources are bought and sold."),
    ("Buyers in a market want:", ["High prices", "Low prices", "No goods", "Taxes"], 1, "Get the most for their money."),
    ("What is the role of the price mechanism in a market economy?", ["To allocate resources through prices", "To plan output", "To set wages", "To collect taxes"], 0, "Prices signal and incentivise."),
    ("Demand requires consumers to be:", ["Willing only", "Able only", "Willing and able to pay", "Rich"], 2, "Both."),
]) + "\n" + cards_js([("Market", "Where buyers and sellers meet to trade goods, services or resources."), ("Buyer (consumer)", "Someone who demands goods and services."), ("Seller (producer)", "Someone who supplies goods and services."), ("Demand", "The quantity buyers are willing and able to buy at each price."), ("Supply", "The quantity sellers are willing and able to sell at each price."), ("Price mechanism", "The way prices adjust to allocate resources."), ("Price signal", "Information from price changes."), ("Incentive", "A reason to change behaviour, such as profit."), ("Factor market", "A market for the factors of production.")]) + "labM(); \n"
explore = '''
  <h2>Lab 1 · A market at different prices</h2>
  <p>Eight buyers and eight sellers have a highest price and a lowest price. Move the price and see who trades.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Willing buyers</small><strong id="pa1"></strong></div><div><small>Willing sellers</small><strong id="pa2"></strong></div><div><small>Trades</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labM" viewBox="0 0 760 320" role="img" aria-label="Buyers and sellers at a given price"></svg>
  </div>

  <h2>Lab 2 · Examples of markets</h2>
  <p>Pick a market to see its type, buyers and sellers.</p>
  <div class="card"><div class="row" id="mkBtns"></div><div id="mkOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define a market.", "Where buyers and sellers meet to trade.", "[K|A market is where buyers and sellers come together] [K|to trade goods, services or resources.]"),
    Q(2, "Identify", 2, "Identify two examples of markets.", "Any two: labour market, car market, foreign exchange.", "[K|The labour market.] [K|The market for cars (or foreign exchange).]"),
    Q(3, "Explain", 4, "Explain the roles of buyers and sellers in a market.", "Buyers demand, pay; sellers supply, earn; price is set between.",
      "[K|Buyers demand goods and services and are willing and able to pay for them.] [N|They want low prices and the most satisfaction.] [K|Sellers supply goods and services to earn revenue and profit.] [N|They want high prices, and the price is set by the interaction of the two.]"),
    Q(4, "Explain", 4, "What is the role of the price mechanism in a market economy? Explain. (Oct/Nov 2021, P12 style)", "Prices signal and give incentives; allocate resources.",
      "[K|The price mechanism allocates scarce resources through changes in prices.] [N|When demand rises, the price and profit rise, which signals firms to produce more.] [N|When demand falls, price falls and resources move elsewhere.]"),
    Q(5, "Analyse", 6, "Analyse how the price mechanism answers the three key resource allocation questions. (Oct/Nov 2022, P22 style)", "What: demand and profit; how: lowest cost methods; who: ability to pay.",
      "[K|The price mechanism decides what to produce through consumer demand: a rise in demand raises price and profit, so firms make more of that good.] [N|It decides how to produce because firms use the cheapest methods to keep costs low and profit high.] [N|It decides who to produce for because goods go to those willing and able to pay the price.] [E|However, those with low incomes may be left out, so the market may not give a fair outcome.]", key=True),
)
tp = tips([
    ("A market is buyers and sellers meeting.", "Not necessarily a place."),
    ("Demand = willing AND able to pay.", "Both."),
    ("Prices signal and give incentives.", "Say both words."),
    ("Link the price mechanism to what, how, who.", "A common question."),
    ("Use named examples.", "Labour market, car market, foreign exchange."),
], cmds("Define", "Identify", "Explain", "Analyse"))
body = page(CL("2.1.1 How markets work"), "How Markets Work", "What a market is, examples of markets, and the roles of buyers and sellers. Syllabus 2.1.1.",
    learn=learn, watch=watch(("A market transaction", "stT"), ("The price mechanism at work", "stP")), explore=explore,
    practise=practise(("Type of market?", "cl1", "card"), ("Buyer or seller?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Online marketplaces", "Websites such as Amazon and eBay bring millions of buyers and sellers together without a physical meeting place.", "A market need not be a place."),
        rw("The labour market", "Firms advertise jobs and workers apply: firms are buyers of labour and workers are sellers.", "A factor market."),
        rw("Ticket prices", "Prices for popular events rise when demand is high, signalling sellers to supply more.", "The price mechanism."),
        rw("Foreign exchange", "Currencies are bought and sold around the clock in a global financial market.", "A financial market.")),
    exam=ex, tips=tp)
write("m211", body, js, "How Markets Work", "ig-how-markets-work")
