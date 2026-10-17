"""AS syllabus 1.4.1-1.4.2 The market economy. Run: python3 tools/artifact-kit/mk_as1m.py"""
from as6k import *
EY = EYAS("1.4.1 to 1.4.2")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>In a <b class="kw">market economy</b> resources are allocated by the <b class="kw">price mechanism</b>: private individuals and firms own the factors of production and make their own decisions, consumers decide <b>what</b> is produced by spending their money, firms choose <b>how</b> to produce in the cheapest way to make a profit, and output goes to those <b>able and willing to pay</b>. Price does three jobs: it <b class="kw">rations</b> scarce goods, <b class="kw">signals</b> what consumers want and <b class="kw">incentivises</b> producers to supply it. The system rewards <b>efficiency, innovation and risk-taking</b> and responds quickly to changes in preferences, with little need for central planning. But markets can <b>fail</b>: they do not provide <b>public goods</b>, under-consume <b>merit goods</b>, over-consume <b>demerit goods</b>, may give <b>monopoly power</b> and <b>inequality</b>, and cannot reach those with no income. In practice no economy is a pure market economy, which is why governments intervene and most economies are <b>mixed</b>.</p></div>

  <h2>1 · Features of a market economy</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Private ownership</b> of factors of production and firms.</li>
    <li><b>Profit motive:</b> firms produce what earns a profit and exit if they make losses.</li>
    <li><b>Consumer sovereignty:</b> consumers' spending decides what is produced.</li>
    <li><b>Competition:</b> many firms compete for customers, which pushes them to cut costs and improve quality.</li>
    <li><b>Price mechanism:</b> prices set by demand and supply allocate resources, with little government intervention.</li>
    <li><b>Freedom:</b> people choose their jobs, what to buy and whether to start a firm.</li>
  </ul>

  <h2>2 · The functions of price</h2>
  <div class="tw"><table class="t">
    <tr><th>Function</th><th>What it means</th><th>Example</th></tr>
    <tr><td><b>Rationing</b></td><td>A higher price reduces quantity demanded so that scarce supplies go to those willing and able to pay</td><td>A rise in the price of concert tickets after a sell-out</td></tr>
    <tr><td><b>Signalling</b> (transmitting preferences)</td><td>Price movements pass information: a higher price shows rising demand or scarcity, a lower price a surplus or falling demand</td><td>A rising price of electric cars tells firms consumers want more</td></tr>
    <tr><td><b>Incentivising</b></td><td>A higher price and profit encourage firms to produce more and new firms to enter; a lower price encourages firms to cut output or leave</td><td>Firms switch to producing what is profitable</td></tr>
  </table></div>
  <ul>
    <li><b>Price as a signal of scarcity:</b> where resources are limited and wants unlimited, price rations the supply among competing buyers; rising demand relative to supply pushes up price, which attracts more supply.</li>
    <li>These functions operate in <b>goods markets</b> and in <b>factor markets</b> (wages, rent, interest), which is how resources move to where they are most valued.</li>
  </ul>

  <h2>3 · How the market answers the three questions</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>Answer in a market economy</th></tr>
    <tr><td><b>What to produce?</b></td><td>What consumers will pay for, shown by prices and profits</td></tr>
    <tr><td><b>How to produce?</b></td><td>The lowest-cost method chosen by competing firms</td></tr>
    <tr><td><b>For whom?</b></td><td>Those with income and the ability to pay, not necessarily those with need</td></tr>
  </table></div>
  <div id="pic2" class="card"></div>

  <h2>4 · Strengths of a market economy</h2>
  <ul>
    <li><b>Efficiency:</b> competition pushes firms to use resources efficiently and to keep costs down.</li>
    <li><b>Consumer choice:</b> firms produce a wide range of goods that people want.</li>
    <li><b>Innovation and enterprise:</b> profit rewards risk-taking and new ideas.</li>
    <li><b>Flexibility:</b> prices adjust quickly to changes in preferences and costs, so resources move without waiting for instructions.</li>
    <li><b>Low bureaucracy:</b> no need for a large planning authority; decisions are decentralised.</li>
  </ul>

  <h2>5 · Weaknesses of a market economy (market failure)</h2>
  <ul>
    <li><b>Public goods</b> are not provided (non-excludable, non-rival, so free riders).</li>
    <li><b>Merit goods</b> such as education and healthcare are under-consumed and under-provided; <b>demerit goods</b> such as tobacco are over-consumed (see 3.1).</li>
    <li><b>Prices do not always reflect all costs and benefits</b> (external costs such as pollution are ignored).</li>
    <li><b>Monopoly power:</b> a firm with little competition can raise prices and restrict output.</li>
    <li><b>Inequality:</b> output goes to those with money; people with little income may lack essentials.</li>
    <li><b>Immobility of factors</b> (workers cannot move quickly) can cause unemployment.</li>
    <li><b>Instability:</b> prices of some goods, such as farm products, are unstable, and the economy may suffer booms and slumps.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name the <b>function of price</b> and explain it with an example. When discussing weaknesses, always say what the market does wrongly (under-supplies, over-supplies, not at all). Do not say a market economy has "no" government; say it has <b>little</b> intervention.</div>
'''

watch = '''
  <h2>1 · A rise in demand and the price signal</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · How resources move without planning</h2>
  <div id="stB"></div>
  <h2>3 · Why a market fails to supply a public good</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Price and resource allocation</h2>
  <p>Shift demand and supply and watch the price signal. Equilibrium starts at price 50, quantity 50.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Price</small><strong id="r1"></strong></div><div><small>Quantity</small><strong id="r2"></strong></div><div><small>Signal to firms</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with the equilibrium price and quantity"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Which function of price?", "Choose a situation to see which function of price it illustrates.", ["Function", "How it works", "Result"]) + chooser_html("k", "Lab 3 · Strength or weakness?", "Choose a feature to see whether it is a strength or a weakness of a market economy.", ["Strength or weakness", "Why", "Government response"])

practise = '''
  <h2>1 · Which function of price is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Strength or weakness of a market economy?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the price signal in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A surge in demand", "A sudden rise in demand for hand sanitiser pushed up its price. The higher price rationed the scarce supply and signalled to firms that more was wanted, so firms switched production to it.", "rationing, signalling and incentivising together.") +
rw("Rising rents attract builders", "When rents in a city rise, builders see higher profits from housing and build more. The price signal moves resources into housing without any planner deciding.", "the incentive function of price.") +
rw("Ticket prices for popular events", "Tickets for a popular concert are quickly sold at a high price. Price rations the limited seats to those most willing to pay, but those with less income are excluded.", "rationing and the 'for whom' question: ability to pay.") +
rw("Hong Kong and Singapore", "These economies are often described as close to the market end of the spectrum: low taxes, limited regulation and open trade. Even so, both governments provide public goods and housing, so neither is a pure market economy.", "no real economy is purely a market economy.") +
rw("Street lighting that nobody pays for", "A private firm cannot charge for street lighting, since everyone nearby benefits whether they pay or not. The market does not supply it, so governments do.", "a market failure: public goods.")
)

mc_exam = [
  mcq("s25_11", 6, "What is not a function of the price mechanism?", ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], 1, "Price signals, incentivises and rations. It does not aim to maximise consumer surplus."),
  mcq("s23_12", 5, "Which statement best illustrates the function of price that relies on consumer choice (the incentivising function)?", ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], 1, "A lower price and profit give producers an incentive to leave the market, while a higher one attracts them."),
  mcq("m25_12", 1, "Which statement about a market economy is not correct?", ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], 2, "Prices often ignore external costs and benefits, so they do not always reflect all costs and benefits."),
  mcq("m22_12", 9, "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences?", ["When the government removes all price controls", "When the new preferences are for more public goods", "When the supply of factors of production is limited", "When there is a redistribution of income"], 1, "Public goods are not provided through the price mechanism, because of free-riding."),
  mcq("s22_12", 12, "What does not happen when price acts as a means to allocate resources?", ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], 0, "Public goods are not supplied by the price mechanism. The other three do happen."),
  mcq("s20_12", 11, "What is a major function of the price mechanism?", ["providing incentive for government intervention to reduce income inequality", "removing shortages by creating incentives for market prices to fall", "removing surpluses by creating incentives for market prices to rise", "signalling changes in market conditions to producers and consumers"], 3, "Signalling is a major function of price. Shortages push prices up and surpluses push them down, so the first three are wrong."),
  mcq("s22_12", 7, "What can be concluded about the roles of demand and supply in a free market?", ["They allocate resources to the greatest needs.", "They ensure that goods and services are distributed equally.", "They are both significant in setting the market price.", "They ensure that everyone can benefit from the good or service provided."], 2, "Market price is set by the interaction of both demand and supply. Markets respond to ability to pay, not need, and do not distribute equally."),
  mcq("m23_12", 7, "In which case is the price system not a possible method of allocating resources?", ["in the distribution of foodstuff among the population", "in the hiring of workers by employers", "in the ownership of land for agricultural use", "in the provision of public goods by the government"], 3, "Public goods cannot be sold, so the price system cannot allocate them.")
]

exam = exam_page("the market economy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The market economy and the functions of price appear in short Paper 2 parts, in 8 and 12 mark questions, and in Paper 1 every year. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Data response, 2 marks", "1", "Oct/Nov 2022 (21) Q1(a)"), ("Essay parts, 8 marks", "1", "Feb/March 2023 (22) Q2(a)"), ("Essay parts, 12 marks", "1", "Oct/Nov 2020 (21) Q2(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("w22_21", "1(a)"), "2 marks", "Explain how 'a product's price acts as a signal of its scarcity'.",
     ["A reference to limited resources to satisfy unlimited wants and needs, so price rations the available resources among competing buyers (1).", "A development: rising demand for a product relative to its supply will push up the price and act as an incentive to increase the quantity supplied; scarcity gives rise to the need to make choices between uses of scarce resources (1)."],
     "Scarcity: limited supply, unlimited wants, price rations. Higher demand pushes the price up, which signals scarcity and encourages more supply.",
     [[("k", "Resources are limited but wants are unlimited, so price rations the available supply among competing buyers."), ("n", "When demand for a product rises relative to supply, its price goes up. The higher price signals that the good is scarce and gives firms an incentive to supply more.")]]),
  eq(P("m23_22", "2(a)"), "8 marks", "Explain the functions of price in resource allocation and consider the importance of these functions in relation to the potential effectiveness of a market economy.",
     ["Knowledge (up to 3): at least two functions of price: rationing (1), signalling or transmitting preferences (1), incentivising (1); two functions well explained can gain 3.",
      "Analysis (up to 3): the importance of rationing, signalling and incentivising to the operation of a market economy, in the context of a market economy.",
      "Evaluation (up to 2): a judgement on the importance of at least two functions for the effectiveness of a market economy, and a justified conclusion."],
     "Rationing. Signalling. Incentive. Why each matters for a market economy. Judge which matters most.",
     [[("k", "Price has three functions in allocating resources. Rationing means a higher price reduces demand to match the limited supply. Signalling means prices pass information about consumers' preferences to producers, so that a rise in price shows that more of the good is wanted. Incentivising means higher prices and profits encourage firms to produce more, while lower prices push them to leave."), ("n", "Together they let a market economy work without central direction: scarce goods go to those who value them most, firms produce what is wanted, and resources move into growing industries automatically.")], [("e", "The functions are important for effectiveness, but they only work well if prices reflect all costs and benefits and if consumers and producers can respond. Signalling and incentives are probably the most important for long-run efficiency, while rationing is the most immediate. Where markets fail, as with public goods, price cannot do these jobs.")]]),
  eq(P("w20_21", "2(b)"), "12 marks", "Discuss why in most mixed economies, resources are mainly allocated using market forces and the price mechanism.",
     ["Analysis (up to 8): analysis of the market forces and price mechanism element (up to 4): the price mechanism, prices as signals of consumer preferences, private ownership and decision-making with little government intervention; and of the government intervention element (up to 4): the use of the word 'mainly' makes clear that market forces are not the exclusive method, with a public sector providing public and merit goods.",
      "Evaluation (up to 4): a judgement on why resources are mainly, but not exclusively, allocated using market forces and the price mechanism, with a reserved mark for a conclusion."],
     "Market: price signals, efficiency, choice, incentives. Government: public and merit goods, regulation. Judge: markets are efficient for most goods, but fail for some.",
     [[("n", "Most resources are allocated by markets because the price mechanism rations scarce goods, signals consumer preferences and gives firms an incentive to be efficient, with little need for central planning. Private ownership and competition encourage innovation and choice. But markets fail to provide public goods, under-consume merit goods and over-consume demerit goods, so governments provide or regulate these, which is why resources are only mainly, not entirely, allocated by markets.")], [("e", "The market is the main method because it is generally efficient and flexible, whereas heavy government control tends to be slow and inefficient. A government role remains necessary where markets fail, so a mixed system, with the market doing most of the allocation, is likely to work best.")]])
  ],
  )

tips = tips_html(
  [("Name the three functions.", "Rationing, signalling, incentivising."),
   ("Use an example for each.", "A price rise after a surge in demand."),
   ("Answer what, how, for whom.", "Consumer spending, lowest cost, ability to pay."),
   ("Give both sides.", "Strengths and market failure."),
   ("Be precise on weaknesses.", "Say which goods are under-, over- or not supplied."),
   ("Avoid 'no government'.", "Say 'little intervention'."),
   ("Link to mixed.", "Market failure is why governments intervene.")],
  [("Market economy", "In a market economy the price mechanism allocates resources with little government intervention."),
   ("Rationing", "Rationing is the function of price that matches limited supply to demand."),
   ("Signalling", "Signalling is the transmission of consumer preferences through prices."),
   ("Incentivising", "Incentivising is the way price and profit encourage firms to supply."),
   ("Consumer sovereignty", "Consumer sovereignty means consumers' spending decides what is produced.")],
  [CW["define"], CW["explain"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Private ownership", "Firms and factors owned privately", 20, "f1"], ["Profit motive", "Firms supply what pays", 270, "f2"], ["Competition", "Rivals cut costs and improve quality", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Private ownership, profit motive and competition are features of a market economy">${o}</svg>`;
})();
$("#pic2").innerHTML = (() => {
  const B = [["What?", "What consumers will pay for", 20, "f1"], ["How?", "The cheapest method wins", 270, "f2"], ["For whom?", "Those able to pay", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="The market answers what, how and for whom through prices">${o}</svg>`;
})();
const mkLab = { x: "Quantity", y: "Price", D1: "D1", D2: "D2", S1: "S1", S2: "S2", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function mkDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }, mkLab); }
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in demand and the price signal", base: { d: 0, s: 0, n: 0 }, draw: mkDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand and supply give an equilibrium price of 50 and quantity of 50.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Consumers want more.</b> Demand shifts right. At the old price there is a shortage.", s: { d: 20, s: 0, n: 1 } },
  { cap: "<b>The price rises</b> to 58. It <b>rations</b> the scarce good, <b>signals</b> that more is wanted and <b>incentivises</b> firms to supply more: quantity rises to 60.", s: { d: 20, s: 0, n: 1 } },
  { cap: "<b>If supply also expands</b> in response to profits, the price stops rising and quantity rises further.", s: { d: 20, s: 20, n: 1 } },
] });
chainStep("#stB", "How resources move without planning", ["Consumers' tastes shift towards a product", "Demand rises and the price goes up", "Profits in that industry rise", "Firms expand and new firms enter; resources move in", "Other industries lose resources: the market has reallocated them"], [
  "<b>Consumer sovereignty</b> drives the change.", "<b>Price signals</b> the new preference.", "<b>Profit</b> is the incentive.", "<b>Supply</b> expands.", "<b>No central planner</b> was needed."]);
chainStep("#stC", "Why a market fails to supply a public good", ["A good is non-excludable and non-rival", "People can use it without paying (free riders)", "Few people pay voluntarily, so revenue is low", "A private firm makes a loss and does not supply it", "The market fails; the government provides it"], [
  "<b>Street lighting</b> or defence.", "<b>Free riders:</b> why pay if others do?", "<b>No revenue</b> for the firm.", "<b>No supply</b> from the market.", "<b>Government provision</b> financed by taxes (see 3.1)."]);

function labM() {
  if (!["gd", "gs"].every((i) => $("#" + i))) return;
  const d = +$("#gd").value, s = +$("#gs").value, e = sdEq(d, s);
  $("#r1").textContent = Lib.fmtN(e.p, 1); $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = e.p > 50.5 ? "Price up: produce more" : e.p < 49.5 ? "Price down: produce less" : "No change";
  $("#rv").textContent = (Math.abs(d) < 0.5 && Math.abs(s) < 0.5) ? "No change in demand or supply, so the price signal is unchanged." : `Price moves from 50 to ${Lib.fmtN(e.p, 1)} and quantity from 50 to ${Lib.fmtN(e.q, 1)}. ${e.p > 50.5 ? "The higher price rations the good, signals higher demand or scarcity and gives firms an incentive to supply more." : e.p < 49.5 ? "The lower price signals falling demand or a surplus and gives firms an incentive to cut output or leave." : "The two changes offset each other in price."}`;
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 }, mkLab);
}
Lib.slider($("#g1"), { id: "gd", label: "Shift in demand ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "gs", label: "Shift in supply ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
labM();

chooser("h", [
  ["Concert tickets sell out and the price rises", "Rationing", "The higher price limits demand to the available seats", "Those most willing and able to pay get tickets", 5],
  ["The price of electric cars keeps rising", "Signalling", "The price passes information about growing demand", "Firms learn what consumers want", 5],
  ["Rising profits attract new bakeries", "Incentivising", "Higher prices and profit encourage more supply", "More firms enter the market", 5],
  ["A bumper harvest cuts wheat prices", "Signalling and incentive", "Lower prices signal a surplus and discourage production", "Farmers may switch crops", 4],
  ["A hotel doubles its room rate in a busy week", "Rationing", "The price rise limits demand", "Rooms go to those willing and able to pay", 4]
], (it) => `${it[0]}: this is the ${it[1].toLowerCase()} function. ${it[2]}. Result: ${it[3].toLowerCase()}.`, "How clearly it fits the function");
chooser("k", [
  ["Competition between firms", "Strength", "Keeps costs and prices down and raises quality", "Competition policy if monopoly appears", 5],
  ["Consumer choice", "Strength", "Firms produce a wide range of goods", "None needed", 4],
  ["Profit as an incentive to innovate", "Strength", "Rewards new ideas and risk-taking", "Patents, R&D support", 4],
  ["No provision of public goods", "Weakness", "Free riders mean no revenue for firms", "Government provision from taxes", 5],
  ["Under-consumption of merit goods", "Weakness", "Consumers lack information or income", "Subsidies, direct provision", 4],
  ["Inequality of income", "Weakness", "Output goes to those who can pay", "Taxes, benefits, free services", 4],
  ["Monopoly power", "Weakness", "A firm with no rivals can raise prices", "Regulation, competition law", 3]
], (it) => `${it[0]}: a ${it[1].toLowerCase()} of a market economy. ${it[2]}. Government response: ${it[3].toLowerCase()}.`, "Importance");
''' + CLASSIFY("cl1", "Which function of price is it?", ["Rationing", "Signalling", "Incentivising"],
  [("A higher price limits demand to the available supply", 0), ("A rising price tells firms consumers want more", 1), ("Higher profits encourage firms to produce more", 2), ("Scarce tickets go to those willing and able to pay", 0), ("Falling prices show demand has dropped", 1), ("Low prices push firms to leave a market", 2)],
  "Rationing allocates limited supply; signalling transmits information; incentivising changes producers' behaviour.") + CLASSIFY("cl2", "Strength or weakness of a market economy?", ["Strength", "Weakness"],
  [("Competition encourages efficiency", 0), ("Public goods are not provided", 1), ("Wide consumer choice", 0), ("Output goes to those who can pay, so inequality", 1), ("Prices adjust quickly to new preferences", 0), ("Prices may not reflect external costs", 1), ("Profit rewards innovation", 0), ("Merit goods are under-consumed", 1)],
  "Strengths: efficiency, choice, innovation, flexibility. Weaknesses: market failure and inequality.") + ORDER(
  "Put the price signal in order.",
  ["Consumer demand for a good rises", "The price rises", "Firms' profits rise", "More firms produce the good", "Supply increases and the price stabilises"],
  "Demand up, price up, profit up, supply up.") + MATCH([
  ["Market economy", "An economy where the price mechanism allocates resources"],
  ["Rationing", "Price limits demand to the available supply"],
  ["Signalling", "Prices transmit information about preferences"],
  ["Incentivising", "Prices and profit encourage production"],
  ["Consumer sovereignty", "Consumers' spending decides what is produced"],
  ["Market failure", "An inefficient allocation of resources by the market"]]) + CALC([
  {"q": "Demand is P = 90 − Q and supply P = 10 + Q. What is the equilibrium price?", "a": 50, "unit": "", "tol": 0.5, "hint": "90 − Q = 10 + Q gives Q = 40.", "sol": "<b>50</b>, with quantity 40."},
  {"q": "Demand rises so that P = 110 − Q (supply unchanged). What is the new equilibrium price?", "a": 60, "unit": "", "tol": 0.5, "hint": "110 − Q = 10 + Q gives Q = 50.", "sol": "<b>60</b>, with quantity 50."},
  {"q": "By what % does the price rise from 50 to 60?", "a": 20, "unit": "%", "tol": 0.1, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "A firm sells 500 units at a price of $12 with costs of $9 per unit. What is its profit ($)?", "a": 1500, "unit": "$", "tol": 0.5, "hint": "(12 − 9) × 500.", "sol": "<b>$1,500</b>."}]) + MCQ([
  ("The price mechanism allocates resources through:", ["Demand and supply", "Central planning", "Government orders", "Tax revenue"], 0, "Prices signal scarcity and preferences."),
  ("Rationing means:", ["Price limits demand to the available supply", "Government gives out goods", "Price falls to zero", "Output is planned"], 0, "A function of price."),
  ("In a market economy 'for whom' is decided by:", ["Ability to pay", "Need", "Planners", "Age"], 0, "Those with income get the goods."),
  ("A weakness of a market economy is:", ["Public goods are not provided", "Competition", "Consumer choice", "Innovation"], 0, "Market failure."),
  ("Profit acts as:", ["An incentive to produce", "A ration", "A tax", "A subsidy"], 0, "Incentivising function.")
], "qz1") + CARDS([
  ("Market economy", "Price mechanism, private ownership."),
  ("Rationing", "Limits demand to supply."),
  ("Signalling", "Prices pass information."),
  ("Incentivising", "Profit drives supply."),
  ("What / how / for whom", "Spending, lowest cost, ability to pay."),
  ("Strengths", "Efficiency, choice, innovation."),
  ("Weaknesses", "Public goods, merit goods, inequality, monopoly."),
  ("Reality", "No pure market economy.")]) + MCQ(mc_exam)

build("as1m", "as-market-economy", "The Market Economy and the Price Mechanism", EY,
  "1.4.1 to 1.4.2: how a market economy allocates resources, the functions of price, and its strengths and weaknesses. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
