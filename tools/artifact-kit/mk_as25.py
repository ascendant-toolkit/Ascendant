"""AS syllabus 2.4.4 Functions of price in resource allocation: rationing, signalling, incentivising. Run: python3 tools/artifact-kit/mk_as25.py"""
from asx import *
EY = EYAS("2.4.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>In a market economy, <b>price does three jobs</b> in allocating resources. It <b class="kw">rations</b> scarce goods, because a higher price discourages demand until the quantity wanted matches the quantity available. It <b class="kw">signals</b> (transmits preferences), because a rising price tells producers that consumers want more of a good and a falling price tells them to cut back. It <b class="kw">incentivises</b>, because higher prices raise profit and so encourage firms to produce more, and lower prices push resources elsewhere; consumers are incentivised to buy less of dearer goods. Together these answer the questions <b>what, how and for whom</b> to produce without central direction, but the price mechanism <b>works poorly</b> where there are public goods, externalities, imperfect information or unequal incomes.</p></div>

  <h2>1 · The three functions (2.4.4)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Function</th><th>What it means</th><th>Example</th></tr>
    <tr><td><b>Rationing</b></td><td>A higher price reduces quantity demanded until it matches the limited supply; those unable or unwilling to pay do without</td><td>A crop failure raises the price of wheat, so only buyers who value it most still buy</td></tr>
    <tr><td><b>Signalling (transmission of preferences)</b></td><td>Price changes tell producers what consumers want and tell consumers about scarcity</td><td>Rising demand for electric cars raises their price, signalling firms to build more</td></tr>
    <tr><td><b>Incentivising</b></td><td>Prices and profits reward producers who respond and encourage consumers to switch</td><td>Higher profit in solar panels attracts new firms; a dearer good pushes buyers to cheaper substitutes</td></tr>
  </table></div>
  <ul>
    <li>The functions work together: <b>demand rises, price rises</b> (rations the limited supply), which <b>signals</b> to firms and <b>incentivises</b> them to produce more, until a new equilibrium is reached.</li>
    <li>Price operates in <b>product markets and factor markets</b> too: high wages signal a shortage of skilled labour and attract workers.</li>
  </ul>

  <h2>2 · When it does not work well</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Price controls.</b> An <b>effective maximum price</b> stops price rising, so there is a <b>shortage</b> and rationing must be done another way (queues, coupons, black markets). The <b>signal is lost</b> and producers lack the incentive to supply more.</li>
    <li><b>Public goods and externalities.</b> Prices do not reflect <b>social</b> costs and benefits, so resources are misallocated (see 1.6 and 3.1).</li>
    <li><b>Ability to pay, not need.</b> Rationing by price favours those with income, so it may be seen as <b>unfair</b>.</li>
    <li><b>Imperfect information and monopoly power</b> distort signals; <b>immobile factors</b> mean resources respond slowly.</li>
    <li><b>Direct provision</b> (free education or health care) is financed by tax, so it is not allocated by the price mechanism. But much of the economy still uses prices.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Name the function, then say <b>who</b> receives the message (consumers or producers) and <b>what they do</b> in response. Use a real chain: demand rises, price rises, firms supply more.</div>
'''

watch = '''
  <h2>1 · Price does three jobs</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · What happens when price is capped</h2>
  <div id="stM"></div>
'''

explore = '''
  <h2>Lab 1 · A change in demand</h2>
  <p>Increase or decrease demand and see how price rations, signals and incentivises.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Price (signal)</small><strong id="r1"></strong></div><div><small>Output change</small><strong id="r2"></strong></div><div><small>Original buyers priced out</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a shifted demand curve and the new price"></svg></div></div></div>

  <h2>Lab 2 · A price cap</h2>
  <p>Set a maximum price. If it is below the equilibrium price of $50, price can no longer ration and a shortage appears.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div>
    <div class="readout"><div><small>Quantity demanded</small><strong id="t1"></strong></div><div><small>Quantity supplied</small><strong id="t2"></strong></div><div><small>Shortage</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a maximum price line and the shortage"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Rationing, signalling or incentivising?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the price mechanism chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Surge pricing for taxis", "When demand jumps (rain or a concert ending), the fare rises. The high price rations seats to those who value them most, signals to drivers that demand is high and attracts more drivers onto the road.", "all three functions in one example.") +
rw("Rising house prices in a city", "Higher prices signal that homes are scarce there. Builders are incentivised by profit to build more, and some buyers are priced out or choose cheaper towns.", "signalling, incentivising and rationing.") +
rw("Rent controls", "A maximum rent below the market level cuts the signal to landlords, so fewer homes are built and let. A shortage follows, and rationing happens through waiting lists, contacts or illegal payments.", "how price controls stop the mechanism from working.") +
rw("Wages and skills", "A shortage of engineers raises their wages. The high pay signals to students that the career is rewarding and incentivises them to train, while firms hire fewer people at the higher cost.", "price in factor markets.")
)

mc_exam = [
  mcq("s20_12", 11, "What is a major function of the price mechanism?", ["providing incentive for government intervention to reduce income inequality", "removing shortages by creating incentives for market prices to fall", "removing surpluses by creating incentives for market prices to rise", "signalling changes in market conditions to producers and consumers"], 3, "Signalling is a main function. Shortages are removed by prices rising and surpluses by prices falling."),
  mcq("w20_12", 12, "When demand for a good falls, its price falls. What is the function of the price fall?", ["to eliminate shortages", "to reduce consumer surplus", "to send a signal to producers", "to stimulate a further fall in demand"], 2, "A falling price tells producers that demand has fallen."),
  mcq("s25_11", 6, "What is not a function of the price mechanism?", ["to act as a signal to firms when allocating resources", "to maximise consumer surplus", "to provide an incentive to firms to produce goods", "to ration scarce resources"], 1, "The three functions are signalling, incentivising and rationing. Maximising consumer surplus is not one."),
  mcq("s23_12", 5, "Price plays a number of functions in the allocation of resources. Which statement best illustrates the function that relies upon consumer choice (sometimes known as the incentivising function)?", ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], 1, "The incentivising function means price changes reward or discourage producers, here pushing some to leave the market."),
  mcq("s22_12", 12, "What does not happen when price acts as a means to allocate resources?", ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than consumers' needs", "Price signals to producers which goods are most profitable"], 0, "Public goods are not supplied through the price mechanism."),
  mcq("s21_11", 6, "When will it not be possible to use price as a rationing mechanism?", ["when a good has a number of close substitutes", "when a good is an inferior good", "when the demand for a good is perfectly inelastic", "when the quantity of a good is in fixed supply"], 2, "If demand is perfectly inelastic, a price rise does not reduce quantity demanded, so price cannot ration."),
  mcq("s22_11", 11, "When will the price mechanism not function as a system for allocating goods?", ["when the government bans advertising", "when the government maintains an effective maximum price", "when there is a limited supply of the good", "when there is a powerful company able to set the market price"], 1, "An effective maximum price stops price from adjusting to clear the market."),
  mcq("m21_12", 14, "After a series of poor harvests, a government imposes an effective maximum price on cereals. What would be a consequence of this policy?", ["Both rich and poor people would satisfy their demands equally", "Illegal buying and selling through a black market would be prevented", "Rationing would be necessary to ensure a fair distribution of cereals", "The market would fail to clear leaving a surplus of cereals"], 2, "A price cap below equilibrium causes a shortage, so rationing by other means is needed."),
  mcq("m22_12", 9, "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences?", ["when the government removes all price controls", "when the new preferences are for more public goods", "when the supply of factors of production is limited", "when there is a redistribution of income"], 1, "Public goods cannot be supplied through prices."),
  mcq("m23_12", 7, "In which case is the price system not a possible method of allocating resources?", ["in the distribution of foodstuff among the population", "in the hiring of workers by employers", "in the ownership of land for agricultural use", "in the provision of public goods by the government"], 3, "Public goods are non-excludable, so prices cannot allocate them."),
  mcq("s22_13", 9, "What is necessary to achieve the best allocation of resources using the price mechanism?", ["Producers can maximise their collective interest", "Consumers and producers must have perfect knowledge", "The government must be able to apply maximum and minimum prices", "The value of the price elasticity of supply must be greater than one"], 1, "Correct signals need good information."),
  mcq("s22_12", 7, "What can be concluded about the roles of demand and supply in a free market?", ["They allocate resources to the greatest needs", "They ensure that goods and services are distributed equally", "They are both significant in setting the market price", "They ensure that everyone can benefit from the good or service provided"], 2, "Price comes from the interaction of both demand and supply. The market allocates by ability to pay, not by need.")
]

exam = exam_page("the functions of price",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The price mechanism is tested in every Paper 1 series and in 6 and 12 mark Paper 2 parts, often linked to direct provision or mixed economies. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 12 marks", "2", "May/June 2021 (21) Q2(b); Oct/Nov 2020 (21) Q2(b)"), ("Data response, 6 marks", "1", "May/June 2022 (23) Q1(e)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("s22_23", "1(e)"), "6 marks", "A market report says a country's avocado market is not allocating resources successfully, because rising prices are encouraging farmers to clear forests. Discuss whether the price mechanism in the avocado market is working to allocate resources successfully.",
     ["Analysis (up to 3): the market is working successfully, because price signals consumer preferences and responds to demand and supply (up to 3).",
      "Analysis (up to 3): why it may not work successfully, such as environmental damage from clearing forests and strain on water supplies, a collapse in prices if new producers flood the market, or a change in health beliefs (up to 3). Maximum 5 for analysis.",
      "Judgement (1): a valid conclusion about whether the price mechanism is working to allocate resources successfully."],
     "Works: price signals demand and attracts producers. Fails: ignores environmental costs. Conclude.",
     [[("n", "The price mechanism appears to be working in one way: rising prices signal strong consumer demand and incentivise more farmers to switch to avocados, so supply responds. But prices do not capture the environmental cost of clearing forests and using scarce water, so too many resources may be directed to avocados. New producers could flood the market and cause prices to fall, which would leave farmers with losses.")], [("e", "Overall the mechanism is probably working for consumers and producers in the short term, but not for society, because external costs are ignored. It is not allocating resources successfully in the long run.")]]),
  eq(P("s21_21", "2(b)"), "12 marks", "Discuss whether the direct provision of goods and services by the government prevents the price mechanism from working effectively.",
     ["Analysis (up to 8): how direct provision prevents the price mechanism from working effectively, for example it does not ration, signal or transmit preferences when goods are paid for by taxation (up to 4); and how it does not prevent it, for example education and health care can also be provided through prices, alongside the state (up to 4).",
      "Evaluation (up to 4): judgement on whether direct provision prevents the price mechanism from working effectively, with a conclusion (1)."],
     "Provision financed by tax: no rationing or signal. But private provision also exists. Judge: depends on how much is provided.",
     [[("n", "When the government provides education or health care free at the point of use, financed through taxation, price does not ration demand, signal what consumers want or incentivise producers, so the price mechanism does not operate for these goods. There may be over-consumption and long waiting lists. However, in many countries private schools and hospitals charge prices alongside state provision, so the price mechanism still rations, signals and transmits preferences in those markets. Direct provision usually covers only a small part of the economy.")], [("e", "Direct provision prevents the price mechanism from working for the goods the government supplies, but does not stop it elsewhere. The effect depends on how large the state sector is, so in most mixed economies the mechanism still works effectively overall.")]]),
  eq(P("w20_21", "2(b)"), "12 marks", "Discuss why in most mixed economies resources are mainly allocated using market forces and the price mechanism.",
     ["Analysis (up to 8): market forces and the price mechanism, such as prices as signals and private decision-making (up to 4); government intervention, since 'mainly' makes clear that the market is not the only method, for example public and merit goods (up to 4).",
      "Evaluation (up to 4): judgement on why resources are mainly but not exclusively allocated by market forces, with a conclusion (1)."],
     "Why markets: signals, incentives, efficiency. Why state too: public and merit goods, equity. Judge: mainly, not only.",
     [[("n", "Market forces allocate most resources in a mixed economy because prices signal what consumers want, incentivise firms to produce it efficiently and ration scarce goods, without costly central planning. Private ownership gives firms a profit motive to innovate. But the government also intervenes, because markets will not provide public goods, under-provide merit goods and ignore externalities, and because incomes may be very unequal.")], [("e", "Resources are mainly allocated by prices because they work well for most goods, but not exclusively, because market failure and equity concerns justify state provision and regulation for some goods. The balance differs between countries.")]])
  ],
  )

tips = tips_html(
  [("Name all three functions.", "Rationing, signalling (transmission of preferences) and incentivising."),
   ("Say who gets the message.", "Signals go to producers and consumers; incentives reward or discourage them."),
   ("Use a chain.", "Demand rises, price rises, firms supply more, a new equilibrium."),
   ("Price rations by ability to pay.", "That can be unfair, which is a limit of the mechanism."),
   ("Price caps break the mechanism.", "Shortage and no signal."),
   ("Public goods cannot be priced.", "The mechanism fails for non-excludable goods."),
   ("Evaluate with 'mainly'.", "Most economies use both markets and government.")],
  [("Rationing", "Price rations scarce goods by reducing quantity demanded."),
   ("Signalling", "A price rise signals to producers that demand has increased."),
   ("Incentivising", "Higher profit encourages firms to produce more."),
   ("Price mechanism", "The price mechanism may not work well for public goods."),
   ("Judge", "The price mechanism probably works for most goods but not for all.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- three functions ---------- */
function fnDraw(s) {
  const d = 20, p = s.p, qd = d + (90 - p) / 0.8, qs = (p - 10) / 0.8; let o = sdPlot({ d: s.n * d, s: 0, g: 0, n: s.n });
  o += SV.line(70, SDY(p), SDX(Math.max(qd, qs)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(qs), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  if (qd - qs > 1) o += SV.rect(SDX(qs), SDY(p) - 6, SDX(qd) - SDX(qs), 12, "f3", op(0.7)) + tag(SDX(qd) + 10, SDY(p) + 4, "shortage " + Lib.fmtN(qd - qs, 0), "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand rises, the price rises and the shortage disappears as price rations, signals and incentivises">${fnDraw({ p: 58, n: 1 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Demand rises and the price mechanism responds", base: { p: 50, n: 0 }, draw: fnDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Start.</b> The market is in equilibrium at $50 and 50 units.", s: { p: 50, n: 0 } },
  { cap: "<b>Demand rises.</b> At the old price of $50 buyers want 70 units but firms supply only 50: a <b>shortage</b> of 20.", s: { p: 50, n: 1 } },
  { cap: "<b>Rationing.</b> The price rises to $54. Buyers with a lower willingness to pay drop out, so quantity demanded falls from 70 to 65 while the shortage narrows.", s: { p: 54, n: 1 } },
  { cap: "<b>Signalling and incentivising.</b> At $58 the higher price signals to firms that consumers want more and the higher profit <b>incentivises</b> them to supply 60 units. The market clears.", s: { p: 58, n: 1 } },
] });

/* ---------- price cap ---------- */
function capDraw(s) {
  const p = s.p, qd = (90 - p) / 0.8, qs = Math.max(0, (p - 10) / 0.8); let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, ...op(s.v) }) + tag(724, SDY(p) - 6, "Max price", "c4", s.v, "end");
  if (s.v > 0.2 && qd - qs > 1) o += SV.rect(SDX(qs), SDY(p) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.7 * s.v)) + SV.circle(SDX(qd), SDY(p), 6, "dot2", op(s.v)) + SV.circle(SDX(qs), SDY(p), 6, "dot1", op(s.v)) + tag(SDX(qd) + 10, SDY(p) + 22, "shortage " + Lib.fmtN(qd - qs, 0), "c3", s.v);
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${capDraw({ p: 35, v: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A maximum price creates a shortage", base: { p: 35, v: 0 }, draw: capDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The free market clears at $50 and 50 units.", s: { p: 35, v: 0 } },
  { cap: "<b>A maximum price of $35</b> is set below equilibrium. At $35 buyers want 69 units but firms supply only 31: a <b>shortage</b> of 38 units.", s: { p: 35, v: 1 } },
  { cap: "<b>The price can no longer ration or signal.</b> Queues, waiting lists or black markets must ration the goods, and firms lack the incentive to supply more.", s: { p: 35, v: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#dm")) return;
  const d = +$("#dm").value, e = sdEq(d, 0), e0 = sdEq(0, 0), dq = (e.q - e0.q) / e0.q * 100, out = Math.max(0, 50 - (90 - e.p) / 0.8);
  $("#r1").textContent = "$" + Lib.fmtN(e.p, 0); $("#r2").textContent = (dq > 0 ? "+" : "") + Lib.fmtN(dq, 0) + "%"; $("#r3").textContent = Lib.fmtN(out, 0);
  $("#rv").textContent = Math.abs(d) < 0.5 ? "Demand has not changed, so the price stays at $50 and nothing needs to adjust." : d > 0 ? `Demand rises, so the price rises to $${Lib.fmtN(e.p, 0)}. That rations the good (${Lib.fmtN(out, 0)} of the original buyers are priced out), signals firms that consumers want more and incentivises them to raise output by ${Lib.fmtN(dq, 0)}%.` : `Demand falls, so the price falls to $${Lib.fmtN(e.p, 0)}. The lower price signals to firms that consumers want less and incentivises them to cut output by ${Lib.fmtN(-dq, 0)}%. No original buyer is priced out.`;
  $("#labA").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "dm", label: "Demand shift (negative = fall, positive = rise) ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#cp")) return;
  const p = +$("#cp").value, qd = (90 - p) / 0.8, qs = Math.max(0, (p - 10) / 0.8), eff = p < 50, sh = eff ? qd - qs : 0;
  $("#t1").textContent = Lib.fmtN(eff ? qd : 50, 0); $("#t2").textContent = Lib.fmtN(eff ? qs : 50, 0); $("#t3").textContent = Lib.fmtN(sh, 0);
  $("#tv").textContent = eff ? `A maximum price of $${p} is below the equilibrium of $50, so it is effective. Buyers want ${Lib.fmtN(qd, 0)} units but firms supply only ${Lib.fmtN(qs, 0)}, a shortage of ${Lib.fmtN(sh, 0)}. Price can no longer ration, so queues, coupons or black markets must.` : `A maximum price of $${p} is at or above the equilibrium of $50, so it has no effect: the market still clears at $50 and 50 units.`;
  let o = sdPlot({ d: 0, s: 0, g: 0 }) + SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5 }) + tag(724, SDY(p) - 6, "Max price $" + p, "c4", 1, "end");
  if (eff) o += SV.rect(SDX(qs), SDY(p) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.7)) + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(qs), SDY(p), 6, "dot1");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "cp", label: "Maximum price, $ ", min: 20, max: 70, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labC });
labC();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which function of price is it?", ["Rationing", "Signalling", "Incentivising"],
  [("A higher price for concert tickets means only those willing to pay can buy", 0), ("A rising price tells farmers that consumers want more wheat", 1), ("Higher profits attract new firms into the solar panel market", 2), ("A price fall tells firms that demand has fallen", 1), ("A crop failure raises the price, so people buy less", 0), ("A rising wage encourages students to train as engineers", 2), ("Dearer petrol pushes drivers to switch to public transport", 2), ("Rising house prices show a city has a shortage of homes", 1)],
  "Rationing reduces demand to match supply. Signalling gives information. Incentivising rewards or discourages action.") + MATCH([
  ["Rationing", "Price reduces quantity demanded to match scarce supply"],
  ["Signalling", "Price tells producers and consumers about changes in the market"],
  ["Incentivising", "Price changes reward or discourage production and consumption"],
  ["Transmission of preferences", "Consumers' wishes are communicated to producers through price"],
  ["Maximum price", "Prevents price from rationing, causing a shortage"],
  ["Price mechanism", "Allocation of resources through the interaction of demand and supply"]]) + ORDER(
  "Put the price mechanism chain in order.",
  ["Consumer demand for a good rises", "A shortage appears at the old price", "The price rises", "Producers see the signal and higher profit and raise output", "A new equilibrium is reached with a higher price and quantity"],
  "Demand leads to a shortage, then price, then supply responds.") + CALC([
  {"q": "The price rises from $50 to $58. What is the % rise?", "a": 16, "unit": "%", "tol": 0.5, "hint": "(58 − 50) ÷ 50.", "sol": "<b>16%</b>."},
  {"q": "Qd = 140 − 2P and Qs = 3P − 10. What is the equilibrium price ($)?", "a": 30, "unit": "$", "tol": 0.5, "hint": "140 − 2P = 3P − 10.", "sol": "150 = 5P, so P = <b>$30</b>."},
  {"q": "A maximum price of $20 is set on the market above. What is the shortage (units)?", "a": 50, "unit": "units", "tol": 0.5, "hint": "Qd = 100, Qs = 50.", "sol": "Qd = 140 − 40 = 100 and Qs = 60 − 10 = 50, so the shortage is <b>50</b>."},
  {"q": "In the same market the price rises from $30 to $33. Quantity supplied rises from 80 to 89. What is the % rise in quantity supplied?", "a": 11.25, "unit": "%", "tol": 0.3, "hint": "9 ÷ 80.", "sol": "<b>11.25%</b>."}]) + MCQ([
  ("A higher price reduces demand until it matches supply. This is the function of:", ["Rationing", "Signalling", "Incentivising", "Redistribution"], 0, "Rationing."),
  ("Rising prices telling firms that consumers want more is:", ["Signalling", "Rationing", "Taxation", "Direct provision"], 0, "Signalling or transmission of preferences."),
  ("Higher profits attracting new firms is:", ["Incentivising", "Rationing", "Signalling to consumers", "Price fixing"], 0, "Incentive to supply."),
  ("An effective maximum price will:", ["Create a shortage", "Create a surplus", "Raise quantity supplied", "Have no effect"], 0, "Below equilibrium."),
  ("Which good cannot be allocated through the price mechanism?", ["A public good", "Bread", "A haircut", "A car"], 0, "Non-excludable.")
], "qz1") + CARDS([
  ("Rationing", "Price limits demand to scarce supply."),
  ("Signalling", "Price tells firms what consumers want."),
  ("Incentivising", "Profit encourages production."),
  ("Max price", "Shortage and no signal."),
  ("Public good", "Price mechanism fails."),
  ("Factor markets", "Wages signal and incentivise too."),
  ("Mixed economy", "Mainly markets, plus government."),
  ("Limits", "Ability to pay, externalities, information.")]) + MCQ(mc_exam)

build("as25", "as-price-functions", "Functions of Price in Resource Allocation", EY,
  "2.4.4: rationing, signalling (transmission of preferences) and incentivising, and what happens when price cannot work. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
