"""AS syllabus 1.4.1-1.4.2 Resource allocation in market, planned and mixed economies. Run: python3 tools/artifact-kit/mk_as15.py"""
from asx import *
EY = EYAS("1.4.1 to 1.4.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An economic system is the way a society answers the three basic questions of <b>what, how and for whom</b> to produce. In a <b class="kw">market economy</b> private individuals and firms decide, guided by <b>prices</b> that ration scarce goods, signal what consumers want and give an incentive to producers; in a <b class="kw">planned (command) economy</b> the <b>government decides</b> through central planning and usually owns the factors of production; and in a <b class="kw">mixed economy</b> <b>both the price mechanism and the government</b> allocate resources, which is true of nearly every real economy. Each system has strengths and weaknesses, and what matters in practice is <b>how mixed</b> the economy is.</p></div>

  <h2>1 · Market economies (1.4.1 and 1.4.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Who decides:</b> consumers and firms, in markets. The <b>price mechanism</b> brings demand and supply into balance. Firms are mostly privately owned and aim to make profit.</li>
    <li><b>The three functions of price:</b>
      <b>rationing</b> (a higher price limits demand to the amount available), <b>signalling</b> (prices transmit consumer preferences to producers, so a rise tells firms that more is wanted) and <b>incentivising</b> (higher prices and profits encourage firms to produce more, and lower ones to leave).</li>
    <li><b>What, how, for whom:</b> what is produced depends on what consumers will pay for; how depends on which method gives the lowest cost (competition rewards efficiency); for whom depends on <b>ability to pay</b>, not need.</li>
    <li><b>Strengths:</b> efficient use of resources through competition, consumer choice, incentives to innovate and to take risks, little bureaucracy, and quick response to changes in preferences.</li>
    <li><b>Weaknesses (market failure):</b> public goods are not provided; merit goods are under-consumed and demerit goods over-consumed; external costs and benefits are ignored; monopoly power; inequality and little help for those without income; factors may be immobile, causing unemployment; prices do not always reflect all costs and benefits.</li>
  </ul>

  <h2>2 · Planned economies</h2>
  <ul>
    <li><b>Who decides:</b> the <b>government or a central planning authority</b>, which sets output targets, prices and the use of resources. Factors of production are usually <b>state-owned</b>, and most goods and services are produced by the state.</li>
    <li><b>What, how, for whom:</b> planners decide which goods are produced, which methods are used and how output is shared, often aiming to share it according to need and equity.</li>
    <li><b>Strengths:</b> provision of public and merit goods for all; more equal distribution; the ability to direct resources to long-term projects and to avoid unemployment; no wasteful duplication in some cases.</li>
    <li><b>Weaknesses:</b> without price signals planners lack information, so there are <b>shortages and surpluses</b>; weak incentives for workers and managers lead to low efficiency and little innovation; limited consumer choice; bureaucracy and slow decisions; possible lack of freedom.</li>
  </ul>

  <h2>3 · Mixed economies</h2>
  <ul>
    <li><b>Who decides:</b> the price mechanism allocates most goods and services, but the <b>government</b> intervenes to correct market failure and to pursue equity: it provides <b>public goods</b> and some <b>merit goods</b> (such as health and education), regulates markets, taxes and subsidises, and sometimes owns industries.</li>
    <li>Economies lie on a <b>spectrum</b>. How mixed an economy is depends on the share of government spending, the amount of state ownership and the amount of regulation and price control.</li>
    <li><b>Advantages:</b> keeps the efficiency and choice of markets while the government supplies what markets fail to provide and reduces extreme inequality.</li>
    <li><b>Disadvantages:</b> government intervention can itself cause problems (taxes and subsidies distort prices, government failure, high taxes may reduce incentives, state firms may be inefficient), and there is no agreement on the right balance.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Basic question</th><th>Market economy</th><th>Planned economy</th><th>Mixed economy</th></tr>
    <tr><td><b>What to produce?</b></td><td>What consumers will pay for, shown by prices and profit</td><td>Central planners' targets</td><td>Mostly consumer demand, plus government choices (public and merit goods)</td></tr>
    <tr><td><b>How to produce?</b></td><td>Lowest-cost methods chosen by competing firms</td><td>Methods decided by the state</td><td>Mostly firms, with regulation and some state production</td></tr>
    <tr><td><b>For whom?</b></td><td>Those with income and the ability to pay</td><td>Allocated by the state, in principle by need</td><td>By ability to pay, adjusted by taxes, benefits and free services</td></tr>
  </table></div>

  <h2>4 · Changing system</h2>
  <ul>
    <li><b>From planned to market</b> (as in the former Soviet bloc and China's reforms): prices are freed, firms are privatised and competition grows. Benefits can be more efficiency, choice and growth; costs include rising prices, <b>structural unemployment</b>, widening inequality and under-provision of some merit and public goods.</li>
    <li><b>From market towards mixed:</b> governments add provision of public goods and regulation when market failure is serious.</li>
    <li>Whether a change is beneficial <b>depends on how quickly it is done</b>, how well institutions work and who gains and loses.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not write that a planned economy has "no" markets or that a market economy has "no" government. Say <b>who makes the main decisions</b> and what the consequences are, then judge using the degree of mixing.</div>
'''

watch = '''
  <h2>1 · The spectrum of economic systems</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stS"></div>
  <h2>2 · How price allocates resources</h2>
  <div id="stP"></div>
'''

explore = '''
  <h2>Lab 1 · Price and resource allocation</h2>
  <p>Move demand and supply for a good. The price changes to ration the good, signals what consumers want, and gives producers a reason to change output.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Price</small><strong id="r1"></strong></div><div><small>Quantity</small><strong id="r2"></strong></div><div><small>Signal to producers</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Supply and demand with the equilibrium price and quantity"></svg></div></div></div>

  <h2>Lab 2 · Where does the economy sit?</h2>
  <p>Rate an economy on three features. The score places it between a pure market economy (0) and a pure planned economy (100).</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Score (0 market, 100 planned)</small><strong id="t1"></strong></div><div><small>System</small><strong id="t2"></strong></div><div><small>Who mainly decides</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="A bar showing the economy's position between a market economy and a planned economy"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Market, planned or mixed?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the price signal in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Central planning and queues", "In some planned economies of the twentieth century, prices of basic goods were fixed by the state, often below the level that matched demand and supply. Shops ran out of goods and people queued, which showed how hard it is for planners to know what consumers want without price signals.", "the information problem of planning and the role of the price mechanism.") +
rw("A mixed economy in action", "Most countries today let markets set the price of food, clothes and phones, but governments provide defence and street lighting, run or fund schools and hospitals, tax tobacco and regulate banks. Countries differ in how much they do, so some are more market-based than others.", "how mixed economies combine markets and government and why the balance varies.") +
rw("Moving to a market economy", "When former planned economies introduced market reforms in the 1990s, prices rose, many state firms closed and unemployment rose in the short run. Over time, new private firms, more choice and higher productivity brought gains, though some groups lost out.", "the costs and benefits of a transition from a planned to a market economy.") +
rw("A surge in demand", "When a new fashion makes a product popular, its price rises. This rationing effect limits the amount that each buyer can afford. It also signals producers to make more, and the higher profit gives them the incentive to do so. Resources move into the industry without any government order.", "the three functions of price.")
)

mc_exam = [
  mcq("w22_12", 2, "In a planned economy, what will determine the allocation of scarce resources?", ["A mixture of private and central decision making", "The decisions of central government", "The forces of demand and supply", "The revenue generated from direct and indirect taxes"], 1, "In a planned economy the state decides, not the market."),
  mcq("s22_12", 2, "What is the main characteristic of a planned economy?", ["All goods and services are produced by privately-owned firms", "All goods and services are produced by state-owned firms", "Private firms produce private goods and state firms produce public goods", "The price mechanism allocates scarce resources through buyers and sellers"], 1, "State ownership and state decision making are the main characteristics. Option C describes a mixed economy and D a market economy."),
  mcq("s25_11", 6, "What is not a function of the price mechanism?", ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], 1, "Price signals, incentivises and rations. It does not aim to maximise consumer surplus."),
  mcq("s23_12", 5, "Which statement best illustrates the function of price that relies on consumer choice (the incentivising function)?", ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], 1, "A lower price and profit give producers an incentive to leave the market, while a higher one attracts them."),
  mcq("m25_12", 1, "Which statement about a market economy is not correct?", ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], 2, "Prices often ignore external costs and benefits, so they do not always reflect all costs and benefits."),
  mcq("w23_11", 4, "What is least likely to increase as a result of a transition from a planned economy to a free market economy?", ["Prices of goods and services", "Privately owned resources", "Provision of merit goods", "Structural unemployment"], 2, "A free market tends to under-provide merit goods; prices, private ownership and structural unemployment are likely to rise."),
  mcq("m22_12", 9, "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences?", ["When the government removes all price controls", "When the new preferences are for more public goods", "When the supply of factors of production is limited", "When there is a redistribution of income"], 1, "Public goods are not provided through the price mechanism, because of free-riding."),
  mcq("s22_12", 12, "What does not happen when price acts as a means to allocate resources?", ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], 0, "Public goods are not supplied by the price mechanism. The other three do happen."),
  mcq("m24_12", 4, "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources?", ["Demerit goods will be over supplied", "Merit goods will be under supplied", "Private goods will not be supplied", "Public goods will not be supplied"], 3, "Public goods would not be provided at all in a pure market, which is the most serious failure."),
  mcq("s24_12", 2, "What is produced in a mixed economy but not in a free market economy?", ["Demerit goods", "Free goods", "Private goods", "Public goods"], 3, "Governments provide public goods in a mixed economy; a free market would not supply them.")
]

exam = exam_page("market, planned and mixed economies",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Economic systems are among the most common 12 mark AS essays, with questions on mixed economies, transition and the role of price in almost every series, and they are tested in Paper 1 every year. Reworded past questions are below, with ten Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2021 (23) Q2(a); Feb/March 2023 (22) Q2(a)"), ("Essay parts, 12 marks", "3", "Feb/March 2023 (22) Q2(b); May/June 2024 (21) Q2(b); Oct/Nov 2021 (21) Q2(b)"), ("Multiple choice (Paper 1)", "10 shown below", "2021 to 2025")],
  [
  eq(P("w21_23", "2(a)"), "8 marks", "Explain how the fundamental economic problem is addressed in a planned economy and in a market economy.",
     ["Knowledge (up to 2): the fundamental economic problem is scarce resources (1) but unlimited wants (1).",
      "Application to a planned economy (up to 3): central planning and government allocation of resources, perhaps with an emphasis on welfare.",
      "Application to a market economy (up to 3): the price mechanism, with rationing, signalling and the interaction of demand and supply."],
     "Scarcity. Planned: government decides what, how and for whom. Market: price mechanism and profit.",
     [[("k", "The fundamental economic problem is that resources are scarce but wants are unlimited, so choices must be made about what, how and for whom to produce.")], [("n", "In a planned economy the government decides. A central authority sets output targets, directs resources to chosen industries and decides how output is shared, often aiming for a fairer distribution.")], [("n", "In a market economy the price mechanism decides. Prices ration scarce goods to those willing and able to pay, signal consumer preferences to firms and give firms an incentive to supply what is profitable, so demand and supply allocate resources.")]]),
  eq(P("m23_22", "2(a)"), "8 marks", "Explain the functions of price in resource allocation and consider the importance of these functions in relation to the potential effectiveness of a market economy.",
     ["Knowledge (up to 3): at least two functions of price: rationing (1), signalling or transmitting preferences (1), incentivising (1); two functions well explained can gain 3.",
      "Analysis (up to 3): the importance of rationing, signalling and incentivising to the operation of a market economy, in the context of a market economy.",
      "Evaluation (up to 2): a judgement on the importance of at least two functions for the effectiveness of a market economy, and a justified conclusion."],
     "Rationing. Signalling. Incentive. Why each matters for a market economy. Judge which matters most.",
     [[("k", "Price has three functions in allocating resources. Rationing means a higher price reduces demand to match the limited supply. Signalling means prices pass information about consumers' preferences to producers, so that a rise in price shows that more of the good is wanted. Incentivising means higher prices and profits encourage firms to produce more, while lower prices push them to leave."), ("n", "Together they let a market economy work without central direction: scarce goods go to those who value them most, firms produce what is wanted, and resources move into growing industries automatically.")], [("e", "The functions are important for effectiveness, but they only work well if prices reflect all costs and benefits and if consumers and producers can respond. Signalling and incentives are probably the most important for long-run efficiency, while rationing is the most immediate. Therefore the market may be effective but not perfect.")]]),
  eq(P("m23_22", "2(b)"), "12 marks", "Assess whether all market economies should become mixed economies.",
     ["Analysis (up to 8): for staying a market economy: little government intervention, decisions based on demand and supply, competition makes production more efficient, consumers and producers act in their own interests.",
      "For becoming mixed: market economies fail to provide public goods, under-consume merit goods, over-consume demerit goods and may have prices that are too low, too high or too unstable.",
      "A one-sided response can only reach Level 2.",
      "Evaluation (up to 4): whether all market economies should become mixed, leading to a justified conclusion; a one-sided answer cannot gain evaluation marks."],
     "Case for staying market. Case for mixed (market failure). Judge: how much government is needed.",
     [[("k", "A market economy relies on the price mechanism and private firms. The argument for staying as it is rests on competition, which encourages productive efficiency and innovation, and on consumers' freedom to choose, with little bureaucracy."), ("n", "The argument for becoming mixed is that markets fail. They do not provide public goods because of free riders, they under-consume merit goods such as education and over-consume demerit goods such as tobacco, and prices of essentials may be too high or unstable. Government provision, taxes, subsidies and regulation can correct these problems.")], [("e", "Most economies are already mixed, so the real question is how mixed. If a market economy already has strong institutions and few failures, it may need only limited intervention. But because public goods will not be provided in a pure market, some government role is probably needed everywhere, so most market economies should be at least partly mixed.")]]),
  eq(P("s24_21", "2(b)"), "12 marks", "Assess whether a planned economic system should always switch to a mixed economy.",
     ["Analysis (up to 8): advantages and disadvantages of a planned system, including its emphasis on welfare and the provision of public and merit goods, but the lack of competition may mean inefficient allocation.",
      "Advantages and disadvantages of a mixed economy: it may contain the best of both systems, but this depends on how mixed it is; the ease of the switch can also be assessed.",
      "Balanced analysis reaches the top level; one-sided answers are limited. Evaluation (up to 4): a valid conclusion."],
     "Planned: pros and cons. Mixed: pros and cons. Judge: depends on the starting point and the speed of the switch.",
     [[("k", "A planned economy has strengths: the state can provide public and merit goods for everyone, aim for equity and direct resources to long-term goals. Its weaknesses are the lack of price signals and competition, which can cause shortages, inefficiency and limited choice."), ("n", "A mixed economy keeps the efficiency and choice of markets, while the government provides public goods and corrects market failure. Its disadvantages are possible government failure, and that the outcome depends on how the balance is set.")], [("e", "A switch is probably beneficial if the planned economy suffers from inefficiency and shortages, but it may bring unemployment and inequality in the short run, and the benefit depends on how quickly it is done. So a planned economy should not always switch, but a move towards mixed is likely to help where the planning system is failing.")]]),
  eq(P("w21_21", "2(b)"), "12 marks", "Discuss whether the advantages of a transition from a planned economy to a market economy always outweigh the disadvantages.",
     ["Analysis (up to 8): advantages of a market economy: the price mechanism, prices as signals of consumer preferences, private ownership and decision-making with little government intervention, competition leading to efficiency.",
      "Disadvantages: some products under-provided and under-consumed (merit goods), some over-provided (demerit goods), some not provided at all (public goods), and further consequences of the transition.",
      "Evaluation (up to 4): judgement on whether the advantages always outweigh the disadvantages; reserve 1 mark for a conclusion."],
     "Advantages (prices, competition). Disadvantages (market failure, unemployment, inequality). Judge: depends on speed and institutions.",
     [[("k", "A transition to a market economy introduces a price mechanism that signals what consumers want. Private ownership and competition give firms an incentive to be efficient and to innovate, and resources can move quickly to where they are most valued.")], [("n", "But a market economy may under-provide merit goods, over-provide demerit goods and fail to provide public goods. In the transition, state firms may close and cause structural unemployment, prices may rise and inequality may widen.")], [("e", "The advantages do not always outweigh the disadvantages. Gains in efficiency may take years, while the costs fall quickly on workers and the poor. A gradual change with strong institutions and a government that still provides public and merit goods is likely to give the best result.")]])
  ],
  )

tips = tips_html(
  [("Say who decides.", "Market: consumers and firms through prices. Planned: the government. Mixed: both."),
   ("Name the three functions of price.", "Rationing, signalling and incentivising."),
   ("Use the three basic questions.", "What, how and for whom, for each system."),
   ("Always give both sides.", "Each system has strengths and weaknesses."),
   ("Mention market failure.", "Public goods, merit and demerit goods, external effects, inequality."),
   ("Say 'how mixed'.", "Economies are on a spectrum; the balance matters."),
   ("Judge with 'depends on'.", "The speed of change, institutions and who gains or loses.")],
  [("Market", "In a market economy the price mechanism allocates resources through demand and supply."),
   ("Planned", "In a planned economy the government decides what, how and for whom to produce."),
   ("Mixed", "A mixed economy might combine the efficiency of markets with government provision of public goods."),
   ("Price", "A rise in price could signal to producers that consumers want more of the good."),
   ("Evaluation", "The right balance may depend on how well markets work in that economy.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- spectrum ---------- */
function spDraw(s) {
  let o = SV.rect(70, 100, 620, 36, "f1", op(0.25)) + SV.rect(70, 100, 620 * s.w, 36, "f3", op(0.55)); o += SV.text(70, 90, "Pure market", "lbl bd") + SV.text(690, 90, "Pure planned", "lbl bd", { "text-anchor": "end" });
  const m = (x, t, sub, k) => (k > 0 ? SV.line(x, 96, x, 150, "c1", { "stroke-width": 2.4, ...op(k) }) + SV.circle(x, 118, 9, "dot4", op(k)) + SV.text(x, 176, t, "lbl bd", { "text-anchor": x < 100 ? "start" : x > 650 ? "end" : "middle", ...op(k) }) + SV.text(x, 194, sub, "sm", { "text-anchor": x < 100 ? "start" : x > 650 ? "end" : "middle", ...op(k) }) : "");
  o += m(70, "Market economy", "prices and private firms decide", s.a) + m(380, "Mixed economies", "both decide; the mix varies", s.b) + m(690, "Planned economy", "the state decides", s.c);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 230" role="img" aria-label="Spectrum from a pure market economy through mixed economies to a pure planned economy">${spDraw({ w: 0.5, a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 230, label: "The spectrum of economic systems", base: { w: 0, a: 0, b: 0, c: 0 }, draw: spDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Market economy.</b> Prices set by demand and supply allocate resources. Firms are private and the government does little.", s: { w: 0, a: 1 } },
  { cap: "<b>Planned economy.</b> The government decides what, how and for whom to produce and usually owns the factors of production.", s: { w: 1, a: 1, c: 1 } },
  { cap: "<b>Mixed economies.</b> In between, markets allocate most goods, while the government provides public goods and corrects market failure. Where an economy sits on the line shows <b>how mixed</b> it is.", s: { w: 0.5, a: 1, b: 1, c: 1 } },
] });

/* ---------- price signals ---------- */
const PX = (q) => 70 + q * 6, PY = (p) => 290 - p * 3.4;
function prDraw(s) {
  const dsh = 18 * s.d; let o = SV.line(70, 290, 700, 290) + SV.line(70, 290, 70, 30) + SV.text(700, 316, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price", "sm");
  const D = (sh) => [[PX(0 + sh), PY(80)], [PX(80 + sh), PY(0)]], Sl = [[PX(0), PY(0)], [PX(80), PY(80)]];
  if (s.d > 0) o += SV.line(...D(0)[0], ...D(0)[1], "c1 dash", op(0.45));
  o += SV.line(...D(dsh)[0], ...D(dsh)[1], "c1") + SV.line(...Sl[0], ...Sl[1], "c3") + tag(PX(78) + 6, PY(2), "D", "t1", 1, "start") + tag(PX(80), PY(80) - 6, "S", "t3", 1, "end");
  const q = 40 + dsh / 2, p = 40 + dsh / 2; o += SV.circle(PX(q), PY(p), 7, "dot4") + tag(PX(q) + 10, PY(p) + 20, "price " + Lib.fmtN(p, 0), "t4");
  if (s.l > 0) o += tag(PX(10), PY(75), "Rationing: price limits demand", "t2", s.l);
  if (s.l > 1) o += tag(PX(10), PY(68), "Signal: consumers want more", "t1", Math.min(1, s.l - 1));
  if (s.l > 2) o += tag(PX(10), PY(61), "Incentive: producers expand output", "t3", Math.min(1, s.l - 2));
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 330, label: "A rise in demand raises the price, which rations, signals and gives producers an incentive", base: { d: 0, l: 0 }, draw: prDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Equilibrium.</b> Demand and supply meet at a price of 40.", s: { d: 0, l: 0 } },
  { cap: "<b>Demand rises</b> (a new fashion). Without any government order, the price rises to about 49.", s: { d: 1, l: 0 } },
  { cap: "<b>Rationing.</b> The higher price limits demand to the amount available: those who value the good least drop out.", s: { d: 1, l: 1 } },
  { cap: "<b>Signalling.</b> The price rise tells producers that consumers want more of this good.", s: { d: 1, l: 2 } },
  { cap: "<b>Incentive.</b> Higher profits encourage firms to expand supply and attract new firms, so resources move into the industry.", s: { d: 1, l: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, q = 40 + (d - s) / 2 * 1, p = 40 + (d + s) * 0 + (d - s) / 2;
  const P2 = 40 + (d + (-s)) / 2 * 1, Q2 = 40 + (d + s) / 2;
  const peq = 40 + (d - s) * 0.5 * 1, qeq = 40 + (d + s) * 0.5 * 1;
  $("#r1").textContent = Lib.fmtN(peq, 0); $("#r2").textContent = Lib.fmtN(qeq, 0); $("#r3").textContent = d - s > 2 ? "Produce more" : d - s < -2 ? "Produce less" : "No change";
  $("#rv").textContent = `Demand has shifted by ${d} and supply by ${s}. The new price is ${Lib.fmtN(peq, 0)} and the quantity ${Lib.fmtN(qeq, 0)}. ${d - s > 2 ? "The price has risen, which rations demand and signals firms to produce more." : d - s < -2 ? "The price has fallen, which signals firms to produce less." : "Price is about the same, so there is little signal to change output."}`;
  const X = (v) => 40 + v * 3.2, Y = (v) => 270 - v * 3.0; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Price", "sm");
  o += SV.line(X(0 + d), Y(80), X(80 + d), Y(0), "c1") + SV.line(X(0 + s), Y(0), X(80 + s), Y(80), "c3") + SV.circle(X(qeq), Y(peq), 7, "dot4") + tag(X(qeq) + 10, Y(peq) + 18, "P " + Lib.fmtN(peq, 0) + ", Q " + Lib.fmtN(qeq, 0), "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dd", label: "Change in demand (shift right +) ", min: -20, max: 20, step: 2, value: 10, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "ss", label: "Change in supply (shift right +) ", min: -20, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labY() {
  if (!$("#so") || !$("#pcn") || !$("#gs")) return;
  const so = +$("#so").value, pcn = +$("#pcn").value, gs = +$("#gs").value, sc = (so * 0.4 + pcn * 0.3 + gs * 0.3);
  $("#t1").textContent = Lib.fmtN(sc, 0); const sys = sc < 15 ? "Market economy" : sc < 40 ? "Mostly market, mixed" : sc < 65 ? "Mixed economy" : sc < 85 ? "Mostly planned, mixed" : "Planned economy";
  $("#t2").textContent = sys; $("#t3").textContent = sc < 15 ? "Prices and firms" : sc < 65 ? "Prices and government" : "The state";
  $("#tv").textContent = `With ${so}% of production state-owned, ${pcn}% of prices controlled and government spending at ${gs}% of the economy's output, the score is ${Lib.fmtN(sc, 0)}: a ${sys.toLowerCase()}. This weights state ownership at 40% and the other two at 30% each, which is a simple teaching rule, not an official index. Real economies differ in how mixed they are, and the answer to 'what, how and for whom' lies between the two extremes.`;
  let o = SV.rect(40, 120, 340, 40, "f1", op(0.25)) + SV.rect(40, 120, 340 * sc / 100, 40, "f3", op(0.6)) + SV.text(40, 108, "Market", "lbl bd") + SV.text(380, 108, "Planned", "lbl bd", { "text-anchor": "end" }) + SV.circle(40 + 340 * sc / 100, 140, 9, "dot4") + tag(40 + 340 * sc / 100, 190, Lib.fmtN(sc, 0), "t4", 1, "middle");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "so", label: "State-owned share of production, % ", min: 0, max: 100, step: 5, value: 25, fmt: (v) => v + "%", onInput: labY });
Lib.slider($("#g4"), { id: "pcn", label: "Prices set or controlled by the government, % ", min: 0, max: 100, step: 5, value: 15, fmt: (v) => v + "%", onInput: labY });
Lib.slider($("#g5"), { id: "gs", label: "Government spending, % of output ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v + "%", onInput: labY });
labY();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which system does it describe?", ["Market", "Planned", "Mixed"],
  [("Prices set by demand and supply allocate most resources", 0), ("A central authority sets output targets for each industry", 1), ("Private firms sell most goods, but the government provides defence and public education", 2), ("Resources go to those with the ability to pay", 0), ("Factors of production are mostly state-owned", 1), ("Governments tax demerit goods and subsidise merit goods", 2), ("Firms decide what to produce to make a profit", 0), ("Planners may fail to match output to what consumers want", 1)],
  "Market: prices decide. Planned: the state decides. Mixed: both.") + MATCH([
  ["Rationing", "Price limits demand to the amount available"],
  ["Signalling", "Price passes information on consumers' preferences to firms"],
  ["Incentivising", "Profit and price changes encourage firms to produce more or less"],
  ["Command economy", "The government makes the main economic decisions"],
  ["Mixed economy", "Prices and government both allocate resources"],
  ["Consumer sovereignty", "Consumers' spending decides what is produced"]]) + ORDER(
  "Put the price signal in order.",
  ["Consumers want more of a good", "Demand rises and the price rises", "Producers see higher profit", "Firms expand output and new firms enter", "Resources move into the industry"],
  "Price rises signal, ration and incentivise.") + CALC([
  {"q": "A government spends $450bn and the economy's output is $1,500bn. What share of output is government spending (%)?", "a": 30, "unit": "%", "tol": 0.5, "hint": "450 ÷ 1,500.", "sol": "<b>30%</b>."},
  {"q": "The price of a product rises from $40 to $48. Calculate the percentage change (%).", "a": 20, "unit": "%", "tol": 0.5, "hint": "8 ÷ 40.", "sol": "<b>20%</b>."},
  {"q": "State-owned firms produce $300bn of an economy's $1,200bn output. What share is state-owned (%)?", "a": 25, "unit": "%", "tol": 0.5, "hint": "300 ÷ 1,200.", "sol": "<b>25%</b>."},
  {"q": "A planner sets a maximum price of $5 when demand is 120 and supply is 80 at that price. What is the shortage (units)?", "a": 40, "unit": "units", "tol": 0.5, "hint": "120 − 80.", "sol": "<b>40 units</b>: planners without price signals can produce shortages."}]) + MCQ([
  ("In a market economy, what mainly decides what is produced?", ["Consumers' spending and firms' profit", "A central planning body", "The government budget", "Trade unions"], 0, "Demand and supply, through prices."),
  ("Which is a weakness of a planned economy?", ["Lack of price signals and incentives", "Too much consumer choice", "Excessive competition", "No provision of public goods"], 0, "Without prices planners lack information and workers lack incentives."),
  ("A mixed economy usually has:", ["Both markets and government provision", "No private firms", "No government", "Only public goods"], 0, "It combines the price mechanism with a role for government."),
  ("The signalling function of price means that:", ["Prices tell producers what consumers want", "Prices are fixed by the state", "Prices ration goods by queue", "Prices show costs only"], 0, "A price rise signals that more is wanted."),
  ("Which is least likely after a move from planning to a market economy?", ["Provision of merit goods rises", "Prices of goods rise", "Private ownership grows", "Some workers become unemployed"], 0, "Markets tend to under-provide merit goods.")
], "qz1") + CARDS([
  ("Market economy", "Price mechanism and private firms decide."),
  ("Planned economy", "Government decides what, how, for whom."),
  ("Mixed economy", "Both; most real economies."),
  ("Functions of price", "Rationing, signalling, incentivising."),
  ("Market failure", "Public goods, merit/demerit goods, externalities."),
  ("Planned weakness", "No price signals; poor incentives."),
  ("Transition", "Planned to market: prices up, unemployment, inequality."),
  ("How mixed?", "Depends on state ownership, spending, regulation.")]) + MCQ(mc_exam)

build("as15", "as-economic-systems", "Market, Planned and Mixed Economies", EY,
  "1.4.1 to 1.4.2: how decisions about what, how and for whom are made in market, planned and mixed economies, the functions of price, and the strengths and weaknesses of each system. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
