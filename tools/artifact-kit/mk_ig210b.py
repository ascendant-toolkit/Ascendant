"""Builds IGCSE Economics 2.10.3 Government intervention to address market failure. Run: python3 tools/artifact-kit/mk_ig210b.py"""
from igsy import *
F = Old("fisc"); M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"
DSJS = open(D / "mk_ig24.py").read().split("DSJS = '''")[1].split("'''")[0]

learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Governments intervene to <b>correct market failure</b>. They can control prices (<b>maximum</b> and <b>minimum prices</b>), change prices and output with <b>indirect taxes</b> and <b>subsidies</b>, or use <b>regulation</b>, <b>privatisation</b>, <b>nationalisation</b>, <b>direct provision</b> and <b>quotas</b>. Each has advantages and disadvantages; the best choice depends on the failure being tackled.</p></div>

  <h2>Price controls and taxes (with diagrams)</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Definition</th><th>Effect</th><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Maximum price</b> (price ceiling)</td><td>A legal limit on how high a price may be, set <b>below</b> equilibrium</td><td>Quantity demanded &gt; quantity supplied: <b>shortage</b></td><td>Keeps essential goods affordable (rent, food)</td><td>Shortages, queues, black markets, less supply</td></tr>
    <tr><td><b>Minimum price</b> (price floor)</td><td>A legal limit on how low a price may be, set <b>above</b> equilibrium</td><td>Quantity supplied &gt; quantity demanded: <b>surplus</b></td><td>Protects producers' incomes (farm prices) or discourages demerit goods (minimum price for alcohol)</td><td>Surpluses, cost to store or buy them, higher prices for consumers</td></tr>
    <tr><td><b>Indirect tax</b></td><td>A tax on goods and services, paid by consumers or producers to the government</td><td>Supply shifts <b>left</b>: price up, quantity down</td><td>Reduces demerit goods; raises revenue; internalises external costs</td><td>Regressive; may be passed to consumers; smuggling; hurts jobs</td></tr>
    <tr><td><b>Subsidy</b></td><td>A payment to producers (or consumers) to lower prices and raise output</td><td>Supply shifts <b>right</b>: price down, quantity up</td><td>Encourages merit goods and external benefits; helps new industries</td><td>Costs taxpayers; opportunity cost; may be inefficient; hard to remove</td></tr>
  </table></div>

  <h2>Other forms of intervention</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Definition</th><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Regulation</b></td><td>Laws and rules that firms and consumers must follow</td><td>Controls pollution, protects consumers and workers, limits monopoly</td><td>Costs of compliance and enforcement; red tape; may be ignored</td></tr>
    <tr><td><b>Privatisation</b></td><td>Selling state-owned firms to the private sector</td><td>Competition and profit may raise efficiency; raises revenue</td><td>Loss of public control; job losses; private monopolies; neglect of unprofitable services</td></tr>
    <tr><td><b>Nationalisation</b></td><td>The government takes over private firms</td><td>Protects essential services; avoids private monopoly power; considers social benefit</td><td>Possible inefficiency; losses funded by taxpayers; compensation costs</td></tr>
    <tr><td><b>Direct provision</b></td><td>The government supplies goods and services itself (public goods, merit goods)</td><td>Ensures provision of public and merit goods for all</td><td>High tax cost; may be inefficient; no choice</td></tr>
    <tr><td><b>Quotas</b> (e.g. natural resources)</td><td>A legal limit on the quantity that may be produced or extracted</td><td>Protects scarce resources (fish, timber) and the environment</td><td>Higher prices; illegal extraction; enforcement cost; job losses</td></tr>
  </table></div>
  <p class="note">Use an <b>example</b> and a <b>judgement</b>: intervention works if the benefits exceed the costs and the policy targets the failure.</p>
'''
js = HEAD + COMMON + DSJS + '''
function ctrl(kind, amt) {
  // kind: 0 none, 1 max price, 2 min price, 3 indirect tax, 4 subsidy
  let o = axes(), [q0, p0] = eq(0, 0);
  if (kind === 3) { o += dCurve(0, "c1", "D") + sCurve(0, "c3", "S", "t3") + sCurve(-amt, "c4", "S₁ (with tax)", "t4"); const [q, p] = eq(0, -amt); o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1") + dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.line(X(q), Y(p), X(q), Y(p - amt), "c3") + SV.text(X(q) - 8, Y(p - amt / 2), "tax $" + amt, "sm bd t4", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }); return o; }
  if (kind === 4) { o += dCurve(0, "c1", "D") + sCurve(0, "c3", "S", "t3") + sCurve(amt, "c2", "S₁ (with subsidy)", "t2"); const [q, p] = eq(0, amt); o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1") + dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.text(X(0) - 8, Y(p), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }); return o; }
  o += dCurve(0, "c1", "D") + sCurve(0, "c2", "S") + dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1");
  if (kind === 1 || kind === 2) { const pc = p0 + (kind === 1 ? -amt : amt), qd = qD(pc, 0), qs = qS(pc, 0); o += SV.line(X(0), Y(pc), X(Math.max(qd, qs) + 8), Y(pc), "c4") + SV.circle(X(qd), Y(pc), 6, "dot3") + SV.circle(X(qs), Y(pc), 6, "dot4") + SV.text(X(0) - 8, Y(pc), (kind === 1 ? "Max $" : "Min $") + Math.round(pc), "sm bd t4", { "text-anchor": "end" }) + SV.text(X((qd + qs) / 2), Y(pc) - 12, kind === 1 ? "Shortage " + Math.round(qd - qs) : "Surplus " + Math.round(qs - qd), "lbl bd t4", { "text-anchor": "middle" }) + SV.text(X(qd), Y(0) + 18, "Qd", "sm bd", { "text-anchor": "middle" }) + SV.text(X(qs), Y(0) + 18, "Qs", "sm bd", { "text-anchor": "middle" }); }
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 380, label: "Maximum price", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "The government sets a <b>maximum price</b> below equilibrium (to keep rents affordable). At this price quantity demanded exceeds quantity supplied: a <b>shortage</b>.", s: { k: 1, a: 20 } },
  { cap: "Shortages lead to queues, rationing and possibly a <b>black market</b>, and suppliers may cut supply further.", s: { k: 1, a: 20 } },
] });
Lib.stepper($("#stN"), { w: 760, h: 380, label: "Minimum price", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "The government sets a <b>minimum price</b> above equilibrium (to protect farmers' incomes). Quantity supplied exceeds quantity demanded: a <b>surplus</b>.", s: { k: 2, a: 20 } },
  { cap: "The surplus must be bought, stored or destroyed: a <b>cost</b> to taxpayers, and consumers pay a higher price.", s: { k: 2, a: 20 } },
] });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Indirect tax", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "An <b>indirect tax</b> raises producers' costs: supply shifts <b>left</b> to S₁.", s: { k: 3, a: 20 } },
  { cap: "The price <b>rises</b> to P₁ and the quantity <b>falls</b> to Q₁. The government raises tax revenue and consumption of the taxed good falls.", s: { k: 3, a: 20 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Subsidy", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "A <b>subsidy</b> lowers producers' costs: supply shifts <b>right</b> to S₁.", s: { k: 4, a: 20 } },
  { cap: "The price <b>falls</b> to P₁ and the quantity <b>rises</b> to Q₁. Consumers buy more of the subsidised good; the cost falls on taxpayers.", s: { k: 4, a: 20 } },
] });

/* Lab 1 */
const KN = ["No policy", "Maximum price", "Minimum price", "Indirect tax", "Subsidy"];
function labI() {
  if (!$("#ia") || !$("#ib")) return;
  const k = +$("#ia").value, a = +$("#ib").value, [q0, p0] = eq(0, 0); let r = ["$" + p0, q0, "None"], t = "Equilibrium: price $" + p0 + ", quantity " + q0 + ".";
  if (k === 1) { const pc = p0 - a, qd = qD(pc, 0), qs = qS(pc, 0); r = ["$" + pc, qs + " supplied", "Shortage " + (qd - qs)]; t = "A maximum price of $" + pc + " (below $" + p0 + ") means " + qd + " demanded but only " + qs + " supplied: a shortage of " + (qd - qs) + ". It helps buyers who can find the good, but leads to queues and black markets."; }
  if (k === 2) { const pc = p0 + a, qd = qD(pc, 0), qs = qS(pc, 0); r = ["$" + pc, qd + " demanded", "Surplus " + (qs - qd)]; t = "A minimum price of $" + pc + " (above $" + p0 + ") means " + qs + " supplied but only " + qd + " demanded: a surplus of " + (qs - qd) + ". Producers earn more per unit but consumers pay more and the surplus has to be dealt with."; }
  if (k === 3) { const [q, p] = eq(0, -a); r = ["$" + p.toFixed(0), q.toFixed(0), "$" + (a * q).toFixed(0)]; t = "A $" + a + " tax per unit shifts supply left: price rises from $" + p0 + " to $" + p.toFixed(0) + " and quantity falls from " + q0 + " to " + q.toFixed(0) + ". Tax revenue is $" + a + " × " + q.toFixed(0) + " = $" + (a * q).toFixed(0) + "."; }
  if (k === 4) { const [q, p] = eq(0, a); r = ["$" + p.toFixed(0), q.toFixed(0), "$" + (a * q).toFixed(0)]; t = "A $" + a + " subsidy per unit shifts supply right: price falls from $" + p0 + " to $" + p.toFixed(0) + " and quantity rises from " + q0 + " to " + q.toFixed(0) + ". The subsidy costs the government $" + a + " × " + q.toFixed(0) + " = $" + (a * q).toFixed(0) + "."; }
  $("#ia1").textContent = r[0]; $("#ia2").textContent = r[1]; $("#ia3").textContent = r[2]; $("#iav").textContent = t;
  $("#labI").innerHTML = ctrl(k, a);
}
Lib.slider($("#g1"), { id: "ia", label: "Policy (0 none, 1 max price, 2 min price, 3 tax, 4 subsidy)", min: 0, max: 4, step: 1, value: 3, fmt: (v) => KN[v], onInput: labI });
Lib.slider($("#g2"), { id: "ib", label: "Size of the policy ($)", min: 5, max: 30, step: 5, value: 20, fmt: (v) => "$" + v, onInput: labI });
const OT = [
  { n: "Regulation", a: "Laws and rules", b: "Controls pollution and monopoly; costs of compliance." },
  { n: "Privatisation", a: "Selling state firms", b: "May raise efficiency; risk of private monopoly and job losses." },
  { n: "Nationalisation", a: "State takeover of firms", b: "Protects essential services; possible inefficiency and taxpayer cost." },
  { n: "Direct provision", a: "The state supplies the good", b: "Ensures public and merit goods for all; high tax cost." },
  { n: "Quotas", a: "Limits on quantity extracted or produced", b: "Protects resources; raises prices; illegal extraction." },
];
button_table("otBtns", "otOut", OT, 0, (p) => `<div class="tw"><table class="t"><tr><th>Meaning</th><th>Advantages and disadvantages</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What is the <b>effect</b> of each policy?", buckets: [{ label: "Shortage" }, { label: "Surplus" }, { label: "Price up, quantity down" }, { label: "Price down, quantity up" }], items: [
  { text: "Maximum price below equilibrium", b: 0 }, { text: "Minimum price above equilibrium", b: 1 }, { text: "Indirect tax", b: 2 }, { text: "Subsidy", b: 3 },
  { text: "Rent control", b: 0 }, { text: "A guaranteed price for wheat above the market price", b: 1 }, { text: "A tax on cigarettes", b: 2 }, { text: "A subsidy for solar panels", b: 3 },
], done: "Know the effects." });
Lib.classify($("#cl2"), { prompt: "Which <b>policy</b> fits each aim?", buckets: [{ label: "Tax or quota" }, { label: "Subsidy or direct provision" }, { label: "Regulation" }], items: [
  { text: "Reduce consumption of a demerit good", b: 0 }, { text: "Protect fish stocks", b: 0 }, { text: "Increase use of a merit good", b: 1 }, { text: "Provide street lighting", b: 1 }, { text: "Limit pollution from factories", b: 2 }, { text: "Stop a monopoly abusing consumers", b: 2 },
], done: "Match policy to failure." });
Lib.match($("#m1"), { prompt: "Match the policy to its definition.", pairs: [
  ["Maximum price", "A legal limit on how high a price may go"],
  ["Minimum price", "A legal limit on how low a price may go"],
  ["Indirect tax", "A tax on goods and services"],
  ["Subsidy", "A government payment to lower producers' costs"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Nationalisation", "The government takes over a private firm"],
  ["Regulation", "Laws and rules firms must follow"],
  ["Quota", "A legal limit on quantity"],
], done: "Definitions score marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a subsidy increases consumption of a merit good</b>.", items: [
  "The government pays a subsidy to producers",
  "Producers' costs fall: supply shifts right",
  "The price falls",
  "Quantity demanded rises",
  "More of the merit good is consumed",
], done: "A supply increase." });
''' + calc_js([
    ("A tax of $20 a unit is placed on 40 units sold. What is the tax revenue ($)?", 800, "20 × 40 = <b>$800</b>.", None, None),
    ("A subsidy of $5 a unit is paid on 600 units. What does it cost the government ($)?", 3000, "5 × 600 = <b>$3,000</b>.", None, None),
    ("At a maximum price, quantity demanded is 70 and quantity supplied is 30. What is the shortage?", 40, "70 − 30 = <b>40</b>.", None, None),
    ("At a minimum price, quantity supplied is 80 and quantity demanded is 45. What is the surplus?", 35, "80 − 45 = <b>35</b>.", None, None),
]) + mcq_js("qz1", [
    ("A maximum price set below equilibrium causes:", ["A surplus", "A shortage", "Equilibrium", "A tax"], 1, "Qd > Qs."),
    ("A minimum price set above equilibrium causes:", ["A shortage", "A surplus", "Lower prices", "No change"], 1, "Qs > Qd."),
    ("An indirect tax shifts:", ["Demand right", "Supply left", "Supply right", "Demand left"], 1, "Costs rise."),
    ("Which is privatisation?", ["Selling a state firm to private owners", "A government taking over a firm", "A tax", "A quota"], 0, "State to private."),
    ("A disadvantage of subsidies is:", ["Lower prices", "Cost to taxpayers", "More output", "Wider choice"], 1, "Opportunity cost."),
]) + "\n" + cards_js([("Maximum price", "A legal limit on how high a price may be."), ("Minimum price", "A legal limit on how low a price may be."), ("Indirect tax", "A tax on goods and services."), ("Subsidy", "A government payment to lower producers' costs."), ("Regulation", "Laws and rules that firms must follow."), ("Privatisation", "Selling state-owned firms to the private sector."), ("Nationalisation", "The government taking over private firms."), ("Direct provision", "The government supplying goods and services itself."), ("Quota", "A legal limit on the quantity produced or extracted.")]) + "labI(); \n"
explore = '''
  <h2>Lab 1 · Try a policy</h2>
  <p>Choose a policy and its size and see its effect on the market (equilibrium price $50, quantity 50).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Price</small><strong id="ia1"></strong></div><div><small>Quantity</small><strong id="ia2"></strong></div><div><small>Result</small><strong id="ia3"></strong></div></div><div class="verdict" id="iav"></div></div></div>
    <svg id="labI" viewBox="0 0 760 340" role="img" aria-label="A market with a government policy"></svg>
  </div>

  <h2>Lab 2 · Other forms of intervention</h2>
  <p>Pick a policy to see its meaning, advantages and disadvantages.</p>
  <div class="card"><div class="row" id="otBtns"></div><div id="otOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define a maximum price.", "A legal limit on how high a price may be.", "[K|A maximum price is a legal limit on how high a price can be] [K|set below the equilibrium price.]"),
    Q(2, "Explain", 4, "Explain how a maximum price on rent could affect the housing market.", "Shortage; black market; less supply; affordable for some.", "[K|A maximum price set below equilibrium means quantity demanded exceeds quantity supplied.] [N|There is a shortage of rented housing, so landlords may supply less and a black market may develop.] [N|Some tenants benefit from lower rents but others cannot find homes.]"),
    Q(3, "Analyse", 6, "Analyse, using a demand and supply diagram, how an indirect tax on cigarettes could affect the market. (Oct/Nov 2023, P22 style)", "S left; price up; quantity down; revenue; inelastic demand.", "[K|An indirect tax raises producers' costs, so supply shifts left from S to S₁.] [N|The equilibrium price rises to P₁ and the quantity falls to Q₁.] [N|Consumption of cigarettes falls and the government raises tax revenue.] [E|Because demand for cigarettes is inelastic, quantity falls only a little.]", key=True),
    Q(4, "Analyse", 6, "Analyse, using a demand and supply diagram, how a subsidy given to producers could affect the market for solar panels. (Feb/Mar 2022, P22 style)", "S right; price down; quantity up; cost to government.", "[K|A subsidy lowers producers' costs, so supply shifts right from S to S₁.] [N|The price falls to P₁ and the quantity rises to Q₁.] [N|Consumers buy more solar panels at a lower price.] [E|The cost to taxpayers is an opportunity cost.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether a government should nationalise essential industries.", "For: affordable, social benefit, no monopoly profit; against: inefficiency, cost, compensation. Judgement.", "[K|Nationalisation is when the government takes over private firms.] [N|It can protect essential services such as water and railways, and stop a private monopoly raising prices.] [N|It allows the government to consider social benefits.] [E|However, state-run firms may be inefficient because there is no competition or profit motive.] [N|Losses are paid by taxpayers and compensation to owners is costly.] [E|Overall, nationalisation may suit natural monopolies with big social importance, but regulation or competition may achieve the same aims more cheaply.]", key=True),
)
tp = tips([
    ("Max price below equilibrium; min price above.", "Learn which is which."),
    ("Tax shifts S left; subsidy shifts S right.", "Draw the shift and label S₁."),
    ("Always give an advantage and a disadvantage.", "Then judge."),
    ("Link each policy to a market failure.", "Demerit goods, merit goods, public goods."),
    ("Use examples.", "Rent control, tobacco tax, solar subsidy."),
], cmds("Define", "Explain", "Analyse", "Discuss"))
body = page(CL("2.10.3 Government intervention to address market failure"), "Government Intervention to Address Market Failure", "Maximum and minimum prices, indirect taxes, subsidies, regulation, privatisation, nationalisation, direct provision and quotas. Syllabus 2.10.3.",
    learn=learn, watch=watch(("Maximum price", "stM"), ("Minimum price", "stN"), ("Indirect tax", "stT"), ("Subsidy", "stS")), explore=explore,
    practise=practise(("What is the effect?", "cl1", "card"), ("Which policy fits?", "cl2", "card"), ("Match the policy", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Rent controls", "Cities such as New York and Berlin have limited rents; the policy helps tenants but can reduce the supply of rental homes.", "A maximum price."),
        rw("Minimum alcohol prices", "Scotland introduced a minimum price per unit of alcohol to cut harmful drinking.", "A minimum price."),
        rw("Tobacco and sugar taxes", "Taxes on cigarettes and sugary drinks raise prices and funds.", "Indirect taxes."),
        rw("Renewable energy subsidies", "Payments for solar and wind helped cut prices and expand use.", "Subsidies."),
        rw("Fishing quotas", "Limits on catches aim to protect fish stocks.", "Quotas.")),
    exam=ex, tips=tp)
write("x2103", body, js, "Government Intervention to Address Market Failure", "ig-government-intervention")
