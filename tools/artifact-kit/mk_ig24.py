"""Builds the three IGCSE Economics 2.4 Price determination reviews (2.4.1 to 2.4.3).
Run: python3 tools/artifact-kit/mk_ig24.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# Demand: P = 100 - (Q - d). Supply: P = Q - s. d, s shift curves right when positive.
DSJS = '''
const X = (q) => 90 + q * 4.6, Y = (p) => 310 - p * 2.7;
function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Price ($)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }); }
function dCurve(d, cls, lab, t) { const a = d >= 0 ? [d, 100] : [0, 100 + d], b = [100 + d, 0]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c1") + SV.text(X(b[0]) + 6, Y(b[1]) - 8, lab || "D", "lbl bd " + (t || "t1")); }
function sCurve(s, cls, lab, t) { const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c2") + SV.text(X(b[0]) + 6, Y(b[1]) + 4, lab || "S", "lbl bd " + (t || "t2")); }
function eq(d, s) { const q = (100 + d + s) / 2, p = q - s; return [q, p]; }
function dsDrop(q, p) { return SV.line(X(0), Y(p), X(q), Y(p), "gr") + SV.line(X(q), Y(p), X(q), Y(0), "gr"); }
function qD(p, d) { return Math.max(0, 100 + d - p); }
function qS(p, s) { return Math.max(0, p + s); }
'''

# =========================================================== 2.4.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>In a market economy the <span class="kw">price mechanism</span> allocates scarce resources: <b>prices rise and fall</b> as demand and supply change, and these price changes <b>signal</b> to consumers and producers what to do and give them <b>incentives</b> to respond. It answers the three basic questions: <b>what</b> to produce, <b>how</b> to produce and <b>for whom</b> to produce.</p></div>

  <h2>Three functions of prices</h2>
  <div class="tw"><table class="t">
    <tr><th>Function</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Signalling</b></td><td>Prices tell producers and consumers where resources are wanted</td><td>A rising price signals shortage: producers should make more</td></tr>
    <tr><td><b>Incentive</b></td><td>Prices and profits give a reason to change behaviour</td><td>Higher profit encourages firms to produce more; lower prices encourage consumers to buy more</td></tr>
    <tr><td><b>Rationing</b></td><td>When resources are scarce, prices allocate goods to those willing and able to pay</td><td>Limited concert tickets go to those who will pay the most</td></tr>
  </table></div>

  <h2>How the price mechanism answers the three questions</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>How the price mechanism answers it</th></tr>
    <tr><td><b>What to produce?</b></td><td>Consumers show what they want by spending. A rise in demand raises prices and profits, so firms switch resources into that good; a fall in demand pushes resources away</td></tr>
    <tr><td><b>How to produce?</b></td><td>Firms compete, so they choose the cheapest efficient combination of resources (labour, capital, land) to keep costs low and profit high; changes in factor prices change the method</td></tr>
    <tr><td><b>For whom to produce?</b></td><td>Goods go to those <b>willing and able to pay</b> the market price; incomes decide who can afford what</td></tr>
  </table></div>

  <h2>Strengths and weaknesses</h2>
  <div class="grid2">
    <div class="card"><h3>Strengths</h3><ul><li>Resources move automatically to where they are most wanted</li><li>Firms are encouraged to be efficient and to innovate</li><li>No need for a central planner: low administrative cost</li><li>Consumer choice</li></ul></div>
    <div class="card"><h3>Weaknesses</h3><ul><li>Goods go to those with money, not necessarily those in greatest need</li><li>Public goods and merit goods may be under-provided</li><li>Ignores external costs such as pollution</li><li>Can lead to monopoly power and unfair outcomes</li></ul></div>
  </div>
'''
js = HEAD + COMMON + DSJS + '''
const WT = ["Consumers' demand for a good rises", "Its price rises and firms' profits rise", "Higher profit is an incentive for firms to produce more", "Resources move into the good", "The market has answered: produce more of it"];
Lib.stepper($("#stW"), { w: 760, h: 380, label: "What to produce", base: { n: 0 }, draw: mkChain(WT, "--accent"), steps: chainSteps(["Consumers' <b>demand</b> for a good rises.", "Its <b>price</b> rises and firms' <b>profits</b> rise.", "Higher profit is an <b>incentive</b> for firms to produce more.", "<b>Resources move</b> into the good.", "The market has answered: <b>produce more of it</b>."]) });
const HW = ["The price of a factor (e.g. labour) rises", "Using it becomes more expensive", "Firms switch to a cheaper factor (e.g. machines)", "Costs fall; profit is protected", "The market has answered: how to produce"];
Lib.stepper($("#stH"), { w: 760, h: 380, label: "How to produce", base: { n: 0 }, draw: mkChain(HW, "--warn"), steps: chainSteps(["The <b>price of a factor</b> (e.g. labour) rises.", "Using it becomes <b>more expensive</b>.", "Firms switch to a <b>cheaper factor</b> (e.g. machines).", "<b>Costs fall</b>; profit is protected.", "The market has answered <b>how to produce</b>."]) });
const FW = ["Goods have a price", "Consumers with enough income can pay it", "Those unable or unwilling to pay do without", "Goods go to those willing and able to pay", "The market has answered: for whom"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "For whom to produce", base: { n: 0 }, draw: mkChain(FW, "--good"), steps: chainSteps(["Goods have a <b>price</b>.", "Consumers with enough <b>income</b> can pay it.", "Those unable or unwilling to pay <b>do without</b>.", "Goods go to those <b>willing and able to pay</b>.", "The market has answered <b>for whom</b>."]) });

/* Lab 1: demand rises, price signals */
function labP() {
  if (!$("#pa")) return;
  const d = +$("#pa").value, [q, p] = eq(d, 0), [q0, p0] = eq(0, 0);
  $("#pa1").textContent = "$" + money(p, 0); $("#pa2").textContent = money(q, 0); $("#pa3").textContent = money(q - q0, 0) >= 0 ? "+" + money(q - q0, 0) : money(q - q0, 0);
  $("#pav").textContent = `Demand ${d >= 0 ? "rises" : "falls"} by ${Math.abs(d)} at every price: the price moves from $${money(p0, 0)} to $${money(p, 0)} and the quantity from ${money(q0, 0)} to ${money(q, 0)}. The higher price signals firms to produce more, and the higher profit is the incentive: resources move into the good (the answer to 'what to produce').`;
  $("#labP").innerHTML = axes() + sCurve(0, "c2", "S") + dCurve(0, "c3", "D", "t3") + (d !== 0 ? dCurve(d, d > 0 ? "c1" : "c4", "D₁", d > 0 ? "t1" : "t4") : "") + dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 6, "dot1") + (d !== 0 ? dsDrop(q, p) + SV.circle(X(q), Y(p), 7, d > 0 ? "dot2" : "dot4") : "");
}
Lib.slider($("#g1"), { id: "pa", label: "Change in demand (at every price)", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labP });
const QU = [
  { n: "What to produce", a: "Demand and profit", e: "Rising demand raises price and profit; firms make more." },
  { n: "How to produce", a: "Relative factor prices and competition", e: "Firms pick the cheapest efficient method." },
  { n: "For whom to produce", a: "Willingness and ability to pay", e: "Goods go to those who can afford the price." },
];
button_table("quBtns", "quOut", QU, 0, (p) => `<div class="tw"><table class="t"><tr><th>Decided by</th><th>Explanation</th></tr><tr><td><b>${p.a}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>question</b> does each describe?", buckets: [{ label: "What to produce" }, { label: "How to produce" }, { label: "For whom to produce" }], items: [
  { text: "Rising demand raises profit, so firms make more", b: 0 }, { text: "Resources move out of a good with falling demand", b: 0 },
  { text: "Firms use machines because labour has become dearer", b: 1 }, { text: "Firms choose the cheapest efficient method", b: 1 },
  { text: "Goods go to those willing and able to pay", b: 2 }, { text: "Those with low incomes may go without", b: 2 },
], done: "What, how, for whom." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>strength</b> or a <b>weakness</b> of the price mechanism?", buckets: [{ label: "Strength" }, { label: "Weakness" }], items: [
  { text: "Resources move to where they are wanted", b: 0 }, { text: "Encourages efficiency", b: 0 }, { text: "Low administrative cost", b: 0 },
  { text: "Ignores external costs like pollution", b: 1 }, { text: "Low-income households may go without", b: 1 }, { text: "May under-provide public goods", b: 1 },
], done: "Evaluate both sides." });
Lib.match($("#m1"), { prompt: "Match the function of prices to its meaning.", pairs: [
  ["Signalling", "Tells firms and consumers where resources are wanted"],
  ["Incentive", "A reason to change behaviour, such as profit"],
  ["Rationing", "Allocating scarce goods to those who can pay"],
  ["Price mechanism", "Prices adjusting to allocate resources"],
  ["Profit", "An incentive to produce"],
  ["Willing and able to pay", "The test for demand"],
], done: "Know the three functions." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the price mechanism answers 'what to produce'</b>.", items: [
  "Consumers' demand for a good rises",
  "Its price and profit rise",
  "Firms have an incentive to produce more",
  "Resources move into the good",
  "More of the good is produced",
], done: "A market answer." });
''' + calc_js([
    ("A firm's profit per unit rises from $2 to $3 and it sells 100 units. What is the extra profit ($)?", 100, "(3 − 2) × 100 = <b>$100</b>.", None, None),
    ("Production of a good rises from 80 to 100 units after a price rise. What is the percentage increase?", 25, "20 ÷ 80 × 100 = <b>25%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is the role of the price mechanism in a market economy?", ["To plan production", "To allocate resources through price signals and incentives", "To set wages", "To tax goods"], 1, "Prices signal."),
    ("A rise in demand leads firms to produce more because of:", ["Higher profit", "Lower prices", "Government orders", "Lower costs"], 0, "Incentive."),
    ("'For whom to produce' is decided mainly by:", ["The government", "Willingness and ability to pay", "Luck", "Firms' size"], 1, "Income and price."),
    ("Rationing by price means:", ["Scarce goods go to those who can pay", "Equal shares", "Free goods", "Government allocation"], 0, "Price allocates."),
    ("A weakness of the price mechanism is that it:", ["Works too slowly", "Ignores external costs", "Is too cheap", "Has no incentives"], 1, "No account of pollution."),
]) + "\n" + cards_js([("Price mechanism", "How prices adjust to allocate scarce resources."), ("Signalling function", "Prices tell producers and consumers where resources are wanted."), ("Incentive function", "Prices and profits encourage changes in behaviour."), ("Rationing function", "Prices allocate scarce goods to those willing and able to pay."), ("What to produce", "Decided by consumer demand and profit."), ("How to produce", "Decided by competition and relative factor prices."), ("For whom to produce", "Decided by ability to pay."), ("Profit", "Revenue minus costs."), ("External cost", "A cost to third parties, ignored by the market.")]) + "labP(); \n"
explore = '''
  <h2>Lab 1 · Prices as signals</h2>
  <p>Change demand and watch the price signal. A higher price and profit tell firms to produce more.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>New price</small><strong id="pa1"></strong></div><div><small>New quantity</small><strong id="pa2"></strong></div><div><small>Change in output</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 340" role="img" aria-label="Demand and supply with a price signal"></svg>
  </div>

  <h2>Lab 2 · The three questions</h2>
  <p>Pick a question to see how the price mechanism answers it.</p>
  <div class="card"><div class="row" id="quBtns"></div><div id="quOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain the role of the price mechanism in a market economy. (Oct/Nov 2021, P12 style)", "Signals and incentives; allocate resources.",
      "[K|The price mechanism allocates scarce resources through changes in prices.] [N|Rising prices signal that more is wanted and give firms an incentive, higher profit, to produce more.] [N|Falling prices signal that less is wanted, so resources move elsewhere.]"),
    Q(2, "Analyse", 6, "Analyse how the price mechanism answers the three key resource allocation questions. (Oct/Nov 2022, P22 style)", "What: demand and profit; how: cheapest methods; for whom: ability to pay.",
      "[K|The price mechanism decides what to produce through demand: a rise in demand raises price and profit, so firms produce more of that good.] [N|It decides how to produce because competitive firms choose the cheapest methods to keep costs low.] [N|It decides for whom because goods go to those willing and able to pay the price.] [E|However, it ignores need, so low-income households may go without.]", key=True),
    Q(3, "Explain", 4, "Explain why prices are described as signals.", "Rising/falling prices show where resources are wanted.",
      "[K|Prices carry information about the state of the market.] [N|A rising price signals that demand is strong or supply is short, so firms should produce more.] [N|A falling price signals the opposite.]"),
    Q(4, "Discuss", 8, "Discuss whether the price mechanism is the best way of allocating resources.", "For: efficient, incentives, choice. Against: inequality, externalities, public goods. Judgement.",
      "[K|The price mechanism allocates resources through prices, signals and incentives.] [N|It is efficient because resources move to where demand is strongest and firms keep costs low to maximise profit.] [N|It also offers consumer choice and needs no central planning.] [E|However, goods go to those who can afford them, not those in most need.] [N|It ignores external costs such as pollution and may under-provide public goods like street lighting.] [E|Overall, it is effective for many goods, but the government usually needs to correct its weaknesses, so a mixed approach is likely to be best.]", key=True),
)
tp = tips([
    ("Three functions: signalling, incentive, rationing.", "Name them."),
    ("What, how, for whom.", "Link each to a price mechanism answer."),
    ("Say 'willing and able to pay'.", "That is how goods are rationed."),
    ("Evaluate with weaknesses.", "Inequality, externalities, public goods."),
    ("Use a chain.", "Demand up, price up, profit up, output up."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("2.4.1 Price mechanism"), "The Price Mechanism", "How prices signal, incentivise and ration to answer what, how and for whom to produce. Syllabus 2.4.1.",
    learn=learn, watch=watch(("What to produce", "stW"), ("How to produce", "stH"), ("For whom to produce", "stF")), explore=explore,
    practise=practise(("Which question?", "cl1", "card"), ("Strength or weakness?", "cl2", "card"), ("Match the function", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Electric vehicles", "Rising demand for electric cars raised prices and profits, and manufacturers shifted investment towards them.", "What to produce."),
        rw("Automation", "As wages rise, firms in many industries replace workers with machines.", "How to produce."),
        rw("Concert tickets", "Tickets for popular events go to those willing to pay the highest price, often through resale.", "Rationing by price."),
        rw("Surge pricing", "Ride apps raise prices in busy periods, attracting more drivers and rationing demand.", "Signal and incentive.")),
    exam=ex, tips=tp)
write("e241", body, js, "The Price Mechanism", "ig-price-mechanism")

# =========================================================== 2.4.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Market equilibrium</span> is where <b>quantity demanded equals quantity supplied</b>: the market clears with no shortage or surplus. The <b>equilibrium price</b> and <b>equilibrium quantity</b> are found where the demand and supply curves <b>intersect</b>, or from a schedule where the two quantities match.</p></div>

  <h2>Using a schedule</h2>
  <div class="tw"><table class="t">
    <tr><th>Price ($)</th><th>Quantity demanded</th><th>Quantity supplied</th><th>Result</th></tr>
    <tr><td>10</td><td>20</td><td>80</td><td>Surplus of 60</td></tr>
    <tr><td>8</td><td>40</td><td>60</td><td>Surplus of 20</td></tr>
    <tr class="hl"><td><b>6</b></td><td><b>50</b></td><td><b>50</b></td><td><b>Equilibrium</b></td></tr>
    <tr><td>4</td><td>70</td><td>30</td><td>Shortage of 40</td></tr>
    <tr><td>2</td><td>90</td><td>10</td><td>Shortage of 80</td></tr>
  </table></div>
  <p>The equilibrium price is <b>$6</b> and the equilibrium quantity is <b>50</b>.</p>

  <h2>Using a diagram</h2>
  <ul>
    <li>Draw a downward-sloping <b>D</b> and an upward-sloping <b>S</b> on the same axes.</li>
    <li>They cross at the <b>equilibrium point</b>. Read across for the equilibrium price (<b>P</b>) and down for the equilibrium quantity (<b>Q</b>).</li>
    <li>At this price, buyers and sellers are both satisfied: the market is <b>cleared</b>.</li>
  </ul>
  <h2>Why equilibrium is stable</h2>
  <ul>
    <li>If the price is above equilibrium there is a surplus, so sellers cut prices.</li>
    <li>If it is below equilibrium there is a shortage, so the price rises.</li>
    <li>These forces push the market back to equilibrium.</li>
  </ul>
  <p class="note">Equilibrium is <b>not</b> necessarily fair or desirable: it only means demand equals supply. Equilibrium changes when demand or supply shifts (see 2.5).</p>
'''
js = HEAD + COMMON + DSJS + '''
Lib.stepper($("#stE"), { w: 760, h: 380, label: "Finding equilibrium", base: { n: 0 }, draw: (s) => {
  let o = axes() + dCurve(0, "c1", "D") + sCurve(0, "c2", "S");
  if (s.n >= 1) o += SV.circle(X(50), Y(50), 8, "dot2");
  if (s.n >= 2) o += dsDrop(50, 50) + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (s.n >= 3) o += SV.text(X(52), Y(50) - 14, "Equilibrium", "lbl bd t2");
  return o;
}, steps: [
  { cap: "Demand D slopes down; supply S slopes up.", s: { n: 0 } },
  { cap: "They <b>intersect</b>: where quantity demanded equals quantity supplied.", s: { n: 1 } },
  { cap: "Read across for the <b>equilibrium price P</b> and down for the <b>equilibrium quantity Q</b>.", s: { n: 2 } },
  { cap: "At P the market <b>clears</b>: no shortage and no surplus.", s: { n: 3 } },
] });
const SC = ["Demand and supply are not equal at the current price", "Buyers or sellers cannot trade as they wish", "The price moves", "Quantities adjust", "The market settles where demand equals supply"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Why the market settles", base: { n: 0 }, draw: mkChain(SC, "--accent"), steps: chainSteps(["Demand and supply are <b>not equal</b> at the current price.", "Buyers or sellers <b>cannot trade as they wish</b>.", "The <b>price moves</b>.", "<b>Quantities adjust</b>.", "The market settles where <b>demand equals supply</b>."]) });

/* Lab 1: schedule and equilibrium */
function labE() {
  if (!$("#ea") || !$("#eb")) return;
  const d = +$("#ea").value, s = +$("#eb").value, [q, p] = eq(d, s);
  $("#ea1").textContent = "$" + money(p, 0); $("#ea2").textContent = money(q, 0); $("#ea3").textContent = "$" + money(p * q, 0);
  $("#eav").textContent = `With demand shifted by ${d} and supply by ${s}, equilibrium is at a price of $${money(p, 0)} and a quantity of ${money(q, 0)}. At this price quantity demanded (${money(qD(p, d), 0)}) equals quantity supplied (${money(qS(p, s), 0)}). Total spending (revenue) is $${money(p * q, 0)}.`;
  $("#labE").innerHTML = axes() + dCurve(d, "c1", "D") + sCurve(s, "c2", "S") + dsDrop(q, p) + SV.circle(X(q), Y(p), 8, "dot2") + SV.text(X(0) - 8, Y(p), "$" + money(p, 0), "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, money(q, 0), "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ea", label: "Shift in demand (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labE });
Lib.slider($("#g2"), { id: "eb", label: "Shift in supply (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labE });
const SCH = [[10, 20, 80], [8, 40, 60], [6, 50, 50], [4, 70, 30], [2, 90, 10]];
function labT() {
  const el = $("#schOut"); if (!el) return;
  const p = +($("#tp") ? $("#tp").value : 6), r = SCH.find((x) => x[0] === p) || SCH[2], diff = r[1] - r[2];
  $("#tp1").textContent = r[1]; $("#tp2").textContent = r[2]; $("#tp3").textContent = diff === 0 ? "Equilibrium" : diff > 0 ? "Shortage " + diff : "Surplus " + (-diff);
  el.innerHTML = `<div class="tw"><table class="t"><tr><th>Price</th><th>Qd</th><th>Qs</th><th>Result</th></tr>${SCH.map((x) => `<tr${x[0] === p ? ' class="hl"' : ""}><td>$${x[0]}</td><td>${x[1]}</td><td>${x[2]}</td><td>${x[1] === x[2] ? "<b>Equilibrium</b>" : x[1] > x[2] ? "Shortage " + (x[1] - x[2]) : "Surplus " + (x[2] - x[1])}</td></tr>`).join("")}</table></div>`;
}
Lib.slider($("#g3"), { id: "tp", label: "Price from the schedule", min: 2, max: 10, step: 2, value: 6, fmt: (v) => "$" + v, onInput: labT });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "At each price shown in the schedule above, is it a <b>shortage</b>, <b>surplus</b> or <b>equilibrium</b>?", buckets: [{ label: "Surplus" }, { label: "Equilibrium" }, { label: "Shortage" }], items: [
  { text: "$10 (Qd 20, Qs 80)", b: 0 }, { text: "$8 (Qd 40, Qs 60)", b: 0 },
  { text: "$6 (Qd 50, Qs 50)", b: 1 },
  { text: "$4 (Qd 70, Qs 30)", b: 2 }, { text: "$2 (Qd 90, Qs 10)", b: 2 },
], done: "Compare Qd and Qs." });
Lib.classify($("#cl2"), { prompt: "Is each statement about equilibrium <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "At equilibrium, quantity demanded equals quantity supplied", b: 0 }, { text: "Equilibrium is where D and S intersect", b: 0 }, { text: "At equilibrium there is no shortage or surplus", b: 0 },
  { text: "Equilibrium is always fair", b: 1 }, { text: "Equilibrium cannot change", b: 1 }, { text: "At equilibrium there is always a shortage", b: 1 },
], done: "Equilibrium means the market clears." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market equilibrium", "Quantity demanded equals quantity supplied"],
  ["Equilibrium price", "The price at which demand equals supply"],
  ["Equilibrium quantity", "The quantity traded at the equilibrium price"],
  ["Market clearing", "No shortage or surplus"],
  ["Intersection of D and S", "The equilibrium point"],
  ["Schedule", "A table of prices and quantities"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a market moves to equilibrium from a surplus</b>.", items: [
  "The price is above equilibrium",
  "Quantity supplied exceeds quantity demanded",
  "Sellers cut prices to clear stock",
  "Quantity demanded rises; quantity supplied falls",
  "The market reaches equilibrium",
], done: "A surplus pushes price down." });
''' + calc_js([
    ("At a price of $6, quantity demanded is 50 and quantity supplied is 50. What is the equilibrium quantity?", 50, "<b>50</b>: where they are equal.", None, None),
    ("The equilibrium price is $6 and the equilibrium quantity is 50. What is total revenue ($)?", 300, "6 × 50 = <b>$300</b>.", None, None),
    ("At $4, Qd is 70 and Qs is 30. What is the shortage?", 40, "70 − 30 = <b>40</b>.", None, None),
]) + mcq_js("qz1", [
    ("Market equilibrium is where:", ["Demand exceeds supply", "Quantity demanded equals quantity supplied", "Supply exceeds demand", "Prices are zero"], 1, "The market clears."),
    ("On a diagram, equilibrium is found at:", ["The y-axis", "The intersection of D and S", "The x-axis", "The top of D"], 1, "Where the curves cross."),
    ("At the equilibrium price there is:", ["A shortage", "A surplus", "No shortage or surplus", "Unemployment"], 2, "Cleared."),
    ("The equilibrium price in the schedule above is:", ["$10", "$8", "$6", "$2"], 2, "Qd = Qs = 50."),
    ("Equilibrium means:", ["The outcome is fair", "Supply equals demand", "Prices never change", "No one wants to trade"], 1, "No tendency to change."),
]) + "\n" + cards_js([("Market equilibrium", "Where quantity demanded equals quantity supplied."), ("Equilibrium price", "The price at which the market clears."), ("Equilibrium quantity", "The quantity traded at equilibrium."), ("Market clearing", "No shortage or surplus remains."), ("Demand schedule", "A table of quantities demanded at each price."), ("Supply schedule", "A table of quantities supplied at each price."), ("Intersection", "The point where two curves cross."), ("Quantity demanded", "Amount buyers want at a price."), ("Quantity supplied", "Amount sellers offer at a price.")]) + "labE(); labT(); \n"
explore = '''
  <h2>Lab 1 · Find the equilibrium</h2>
  <p>Shift demand and supply and see where they intersect.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Equilibrium price</small><strong id="ea1"></strong></div><div><small>Equilibrium quantity</small><strong id="ea2"></strong></div><div><small>Revenue</small><strong id="ea3"></strong></div></div><div class="verdict" id="eav"></div></div></div>
    <svg id="labE" viewBox="0 0 760 340" role="img" aria-label="Demand and supply equilibrium"></svg>
  </div>

  <h2>Lab 2 · Read the schedule</h2>
  <p>Choose a price to see quantity demanded, quantity supplied and the result.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div></div><div><div class="readout"><div><small>Qd</small><strong id="tp1"></strong></div><div><small>Qs</small><strong id="tp2"></strong></div><div><small>Result</small><strong id="tp3"></strong></div></div></div></div><div id="schOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define market equilibrium.", "Quantity demanded equals quantity supplied.", "[K|Market equilibrium is where quantity demanded equals quantity supplied,] [K|so there is no shortage or surplus.]"),
    Q(2, "Identify", 2, "Using the schedule, identify the equilibrium price and quantity.", "Where Qd = Qs.", "[A|The equilibrium price is $6.] [A|The equilibrium quantity is 50.]"),
    Q(3, "Explain", 4, "Explain why the market tends to move towards equilibrium.", "Shortage raises price; surplus lowers it.",
      "[K|If price is above equilibrium there is a surplus,] [N|so sellers cut prices and quantity demanded rises.] [K|If price is below equilibrium there is a shortage,] [N|so the price rises and quantity supplied rises, restoring equilibrium.]"),
    Q(4, "Explain", 4, "Explain how equilibrium price and quantity are shown on a demand and supply diagram.", "Intersection; read across and down.",
      "[K|Equilibrium is shown where the demand curve crosses the supply curve.] [N|Reading across from this point to the price axis gives the equilibrium price,] [N|and reading down to the quantity axis gives the equilibrium quantity.]"),
)
tp = tips([
    ("Equilibrium: Qd = Qs.", "Say it in full."),
    ("Draw D and S and mark the intersection.", "Label P and Q."),
    ("Use the schedule.", "Find where the two columns match."),
    ("No shortage or surplus.", "The market clears."),
    ("Equilibrium is not necessarily fair.", "Useful for evaluation."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.4.2 Market equilibrium"), "Market Equilibrium", "Equilibrium price and quantity from schedules and from demand and supply diagrams. Syllabus 2.4.2.",
    learn=learn, watch=watch(("Finding equilibrium", "stE"), ("Why the market settles", "stC")), explore=explore,
    practise=practise(("Shortage, surplus or equilibrium?", "cl1", "card"), ("True or false?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Used-car market", "Prices settle where the number of cars buyers want matches the number sellers offer.", "Market clearing."),
        rw("Online auctions", "Auctions let prices rise until buyers and the quantity available match.", "Finding equilibrium."),
        rw("Fresh fish at the end of the day", "Stallholders lower prices until all the fish is sold.", "Surplus pushes the price down."),
        rw("Housing in popular cities", "Prices rise where demand exceeds supply until fewer buyers can afford to buy.", "Shortage pushes the price up.")),
    exam=ex, tips=tp)
write("e242", body, js, "Market Equilibrium", "ig-market-equilibrium")

# =========================================================== 2.4.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Market disequilibrium</span> is when <b>quantity demanded does not equal quantity supplied</b>, so the market does not clear. If the price is <b>below</b> equilibrium, demand exceeds supply: a <b>shortage</b> (excess demand). If the price is <b>above</b> equilibrium, supply exceeds demand: a <b>surplus</b> (excess supply). Price changes push the market back to equilibrium.</p></div>

  <h2>Shortage and surplus</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Shortage (excess demand)</th><th>Surplus (excess supply)</th></tr>
    <tr><td><b>Price compared with equilibrium</b></td><td>Below</td><td>Above</td></tr>
    <tr><td><b>Quantity demanded vs supplied</b></td><td>Qd > Qs</td><td>Qs > Qd</td></tr>
    <tr><td><b>Size</b></td><td>Qd − Qs</td><td>Qs − Qd</td></tr>
    <tr><td><b>What happens next</b></td><td>Buyers compete: price rises</td><td>Sellers compete: price falls</td></tr>
    <tr><td><b>Result</b></td><td>Quantity demanded falls and quantity supplied rises</td><td>Quantity demanded rises and quantity supplied falls</td></tr>
  </table></div>

  <h2>Using a schedule</h2>
  <div class="tw"><table class="t">
    <tr><th>Price ($)</th><th>Qd</th><th>Qs</th><th>Disequilibrium</th></tr>
    <tr><td>8</td><td>40</td><td>60</td><td>Surplus of 20</td></tr>
    <tr class="hl"><td>6</td><td>50</td><td>50</td><td>Equilibrium</td></tr>
    <tr><td>4</td><td>70</td><td>30</td><td>Shortage of 40</td></tr>
  </table></div>

  <h2>On a diagram</h2>
  <ul>
    <li>Draw a price <b>below</b> equilibrium: the gap between S and D (at that price) is the <b>shortage</b>.</li>
    <li>Draw a price <b>above</b> equilibrium: the gap is the <b>surplus</b>.</li>
    <li>Label Qs, Qd and the gap.</li>
  </ul>
  <h2>Why disequilibrium happens</h2>
  <ul>
    <li>A <b>shift in demand or supply</b> makes the old price too high or too low (for example a bumper harvest in a global market for grapes creates a surplus at the old price).</li>
    <li>A <b>price set by the government</b> away from equilibrium (a maximum or minimum price).</li>
  </ul>
  <p class="note">Markets usually move back to equilibrium. The price mechanism works by <b>rationing and signalling</b> until Qd = Qs again.</p>
'''
js = HEAD + COMMON + DSJS + '''
function disChart(p, d, s) {
  const [q, pe] = eq(d, s), qd = qD(p, d), qs = qS(p, s);
  let o = axes() + dCurve(d, "c1", "D") + sCurve(s, "c2", "S") + SV.line(X(0), Y(p), X(Math.max(qd, qs) + 8), Y(p), "gr") + SV.circle(X(q), Y(pe), 6, "dot1");
  if (Math.abs(qd - qs) > 0.5) o += SV.circle(X(qd), Y(p), 6, "dot3") + SV.circle(X(qs), Y(p), 6, "dot4") + SV.line(X(Math.min(qd, qs)), Y(p), X(Math.max(qd, qs)), Y(p), "c3") + SV.text(X((qd + qs) / 2), Y(p) - 12, qd > qs ? "Shortage " + money(qd - qs, 0) : "Surplus " + money(qs - qd, 0), "lbl bd " + (qd > qs ? "t2" : "t4"), { "text-anchor": "middle" }) + SV.text(X(qd), Y(0) + 18, "Qd", "sm bd", { "text-anchor": "middle" }) + SV.text(X(qs), Y(0) + 18, "Qs", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(X(0) - 8, Y(p), "$" + money(p, 0), "sm bd", { "text-anchor": "end" });
}
Lib.stepper($("#stD"), { w: 760, h: 380, label: "Shortage and surplus", base: { p: 50 }, draw: (s) => disChart(s.p, 0, 0), steps: [
  { cap: "At the equilibrium price demand equals supply.", s: { p: 50 } },
  { cap: "A price <b>above</b> equilibrium: quantity supplied exceeds quantity demanded: a <b>surplus</b>.", s: { p: 75 } },
  { cap: "A price <b>below</b> equilibrium: quantity demanded exceeds quantity supplied: a <b>shortage</b>.", s: { p: 25 } },
] });
const AD = ["A surplus exists: the price is above equilibrium", "Sellers have unsold stock", "They cut prices", "Quantity demanded rises; quantity supplied falls", "The surplus disappears at equilibrium"];
Lib.stepper($("#stA"), { w: 760, h: 380, label: "Adjusting from a surplus", base: { n: 0 }, draw: mkChain(AD, "--bad"), steps: chainSteps(["A <b>surplus</b> exists: the price is above equilibrium.", "Sellers have <b>unsold stock</b>.", "They <b>cut prices</b>.", "Quantity demanded <b>rises</b>; quantity supplied <b>falls</b>.", "The surplus disappears at <b>equilibrium</b>."]) });
const SH = ["A shortage exists: the price is below equilibrium", "Buyers compete for limited goods", "Sellers raise prices", "Quantity demanded falls; quantity supplied rises", "The shortage disappears at equilibrium"];
Lib.stepper($("#stB"), { w: 760, h: 380, label: "Adjusting from a shortage", base: { n: 0 }, draw: mkChain(SH, "--warn"), steps: chainSteps(["A <b>shortage</b> exists: the price is below equilibrium.", "Buyers <b>compete</b> for limited goods.", "Sellers <b>raise prices</b>.", "Quantity demanded <b>falls</b>; quantity supplied <b>rises</b>.", "The shortage disappears at <b>equilibrium</b>."]) });

/* Lab 1: choose a price */
function labD() {
  if (!$("#da")) return;
  const p = +$("#da").value, qd = qD(p, 0), qs = qS(p, 0), gap = qd - qs, st = gap > 0.5 ? "Shortage" : gap < -0.5 ? "Surplus" : "Equilibrium";
  $("#da1").textContent = qd; $("#da2").textContent = qs; $("#da3").textContent = st + (Math.abs(gap) > 0.5 ? " " + Math.abs(gap) : "");
  $("#dav").textContent = `At $${p}, quantity demanded is ${qd} and quantity supplied is ${qs}: ${st === "Equilibrium" ? "the market clears." : st === "Shortage" ? "a shortage of " + gap + ". Buyers compete and the price tends to rise." : "a surplus of " + (-gap) + ". Sellers compete and the price tends to fall."}`;
  $("#labD").innerHTML = disChart(p, 0, 0);
}
Lib.slider($("#g1"), { id: "da", label: "Market price", min: 10, max: 90, step: 5, value: 70, fmt: (v) => "$" + v, onInput: labD });
const DQ = [
  { n: "Price above equilibrium", t: "Surplus", e: "Qs > Qd: sellers cut prices." },
  { n: "Price below equilibrium", t: "Shortage", e: "Qd > Qs: buyers bid up the price." },
  { n: "Bumper harvest in a global market", t: "Surplus at the old price", e: "Supply shifts right; the old price is too high." },
  { n: "A surge in demand", t: "Shortage at the old price", e: "Demand shifts right; the old price is too low." },
  { n: "A price ceiling below equilibrium", t: "Persistent shortage", e: "The price cannot rise." },
];
button_table("dqBtns", "dqOut", DQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>Result</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>shortage</b> or a <b>surplus</b>?", buckets: [{ label: "Shortage" }, { label: "Surplus" }], items: [
  { text: "Quantity demanded exceeds quantity supplied", b: 0 }, { text: "Price below equilibrium", b: 0 }, { text: "Excess demand", b: 0 },
  { text: "Quantity supplied exceeds quantity demanded", b: 1 }, { text: "Price above equilibrium", b: 1 }, { text: "Excess supply", b: 1 },
], done: "Shortage means demand exceeds supply." });
Lib.classify($("#cl2"), { prompt: "What happens <b>next</b> to the price?", buckets: [{ label: "Price rises" }, { label: "Price falls" }], items: [
  { text: "There is a shortage", b: 0 }, { text: "Buyers compete for scarce goods", b: 0 },
  { text: "There is a surplus", b: 1 }, { text: "Sellers have unsold stock", b: 1 },
], done: "Markets adjust towards equilibrium." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market disequilibrium", "Quantity demanded does not equal quantity supplied"],
  ["Shortage", "Demand exceeds supply"],
  ["Surplus", "Supply exceeds demand"],
  ["Excess demand", "Another name for a shortage"],
  ["Excess supply", "Another name for a surplus"],
  ["Price mechanism", "Moves the market back to equilibrium"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a market moves from a shortage to equilibrium</b>.", items: [
  "The price is below equilibrium",
  "Quantity demanded exceeds quantity supplied",
  "Buyers compete and the price rises",
  "Quantity demanded falls and quantity supplied rises",
  "The market reaches equilibrium",
], done: "A shortage pushes the price up." });
''' + calc_js([
    ("At $4, quantity demanded is 70 and quantity supplied is 30. What is the shortage?", 40, "70 − 30 = <b>40</b>.", None, None),
    ("At $8, quantity demanded is 40 and quantity supplied is 60. What is the surplus?", 20, "60 − 40 = <b>20</b>.", None, None),
    ("A surplus of 20 on a supply of 60 is what percentage of supply (to the nearest whole number)?", 33, "20 ÷ 60 × 100 = <b>33%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Market disequilibrium means:", ["Demand equals supply", "Quantity demanded does not equal quantity supplied", "Prices are fixed", "No trade"], 1, "The market does not clear."),
    ("A shortage occurs when:", ["Price is above equilibrium", "Price is below equilibrium", "Price equals equilibrium", "Supply is zero"], 1, "Qd > Qs."),
    ("A surplus will cause the price to:", ["Rise", "Fall", "Stay the same", "Double"], 1, "Sellers compete."),
    ("Excess demand is another name for:", ["A surplus", "A shortage", "Equilibrium", "A tax"], 1, "Qd > Qs."),
    ("Which could cause a surplus at the old price?", ["A rise in demand", "A rise in supply", "A fall in supply", "A fall in tax on buyers"], 1, "More supplied than demanded."),
]) + "\n" + cards_js([("Market disequilibrium", "Quantity demanded does not equal quantity supplied."), ("Shortage", "Quantity demanded exceeds quantity supplied (excess demand)."), ("Surplus", "Quantity supplied exceeds quantity demanded (excess supply)."), ("Excess demand", "A shortage."), ("Excess supply", "A surplus."), ("Price above equilibrium", "Leads to a surplus."), ("Price below equilibrium", "Leads to a shortage."), ("Market clearing", "No shortage or surplus remains."), ("Price ceiling", "A government maximum price.")]) + "labD(); \n"
explore = '''
  <h2>Lab 1 · Shortage or surplus?</h2>
  <p>Move the price above or below equilibrium ($50) and see the gap between demand and supply.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Quantity demanded</small><strong id="da1"></strong></div><div><small>Quantity supplied</small><strong id="da2"></strong></div><div><small>Result</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 340" role="img" aria-label="A shortage or surplus on a demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · Causes and results</h2>
  <p>Pick a situation to see whether it creates a shortage or a surplus.</p>
  <div class="card"><div class="row" id="dqBtns"></div><div id="dqOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define market disequilibrium. (Oct/Nov 2021, P22 style)", "Quantity demanded does not equal quantity supplied.", "[K|Market disequilibrium is where quantity demanded] [K|does not equal quantity supplied at the current price.]"),
    Q(2, "State", 2, "State why the global market for grapes was in disequilibrium in 2019. (Oct/Nov 2023, P22 style)", "Supply exceeded demand at the price; surplus.", "[K|Supply of grapes was greater than demand at the price] [K|so there was a surplus.]"),
    Q(3, "Explain", 4, "Explain how a market moves from disequilibrium to equilibrium. (May/June 2022, P22 style)", "Surplus: price falls; shortage: price rises.",
      "[K|If there is a surplus, sellers cut prices to sell stock.] [N|Quantity demanded rises and quantity supplied falls until they are equal.] [K|If there is a shortage, buyers compete and the price rises.] [N|Quantity demanded falls and quantity supplied rises until the market clears.]"),
    Q(4, "Identify", 2, "Using the schedule, identify the size of the shortage at $4.", "Qd − Qs.", "[A|Quantity demanded 70 minus quantity supplied 30] [A|= a shortage of 40.]"),
    Q(5, "Analyse", 6, "Analyse why a market might be in disequilibrium and how it returns to equilibrium.", "Shift in D or S; price above/below; adjustment.",
      "[K|A market may be in disequilibrium after a shift in demand or supply, for example a bumper harvest raises supply.] [N|At the old price quantity supplied exceeds quantity demanded, so there is a surplus.] [N|Sellers cut prices, quantity demanded rises and quantity supplied falls.] [N|The market moves to a new, lower equilibrium price.] [E|Adjustment may be slow if prices are sticky or fixed by the government.]", key=True),
)
tp = tips([
    ("Shortage: Qd > Qs; surplus: Qs > Qd.", "Say which is bigger."),
    ("Price above equilibrium = surplus.", "Price below = shortage."),
    ("Show the gap on the diagram.", "Label Qd, Qs and the gap."),
    ("Explain the adjustment.", "Price falls (surplus) or rises (shortage)."),
    ("Calculate the size.", "Subtract the smaller from the larger."),
], cmds("Define", "Identify", "Explain", "Analyse"))
body = page(CL("2.4.3 Market disequilibrium"), "Market Disequilibrium", "Shortages and surpluses, how to show them on schedules and diagrams, and how markets return to equilibrium. Syllabus 2.4.3.",
    learn=learn, watch=watch(("Shortage and surplus", "stD"), ("Adjusting from a surplus", "stA"), ("Adjusting from a shortage", "stB")), explore=explore,
    practise=practise(("Shortage or surplus?", "cl1", "card"), ("What happens to the price?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("A bumper harvest", "A big grape or wheat harvest raises supply, creating a surplus at the old price and pushing prices down.", "Surplus."),
        rw("Concert tickets", "At a low face value tickets sell out immediately, so a shortage develops and resale prices rise.", "Shortage."),
        rw("End-of-season sales", "Shops cut prices to clear unsold stock.", "Surplus adjusting."),
        rw("Face masks in early 2020", "A surge in demand created shortages and price rises.", "Shortage after a demand shift.")),
    exam=ex, tips=tp)
write("e243", body, js, "Market Disequilibrium", "ig-market-disequilibrium")
