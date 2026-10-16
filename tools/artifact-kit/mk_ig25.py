"""Builds the two IGCSE Economics 2.5 Price changes reviews (2.5.1, 2.5.2).
Run: python3 tools/artifact-kit/mk_ig25.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"
DSJS = open(D / "mk_ig24.py").read().split("DSJS = '''")[1].split("'''")[0]
SHIFTJS = '''
function shiftChart(d, s) {
  const [q0, p0] = eq(0, 0), [q1, p1] = eq(d, s);
  let o = axes() + dCurve(0, d !== 0 ? "c3" : "c1", "D", d !== 0 ? "t3" : "t1") + sCurve(0, s !== 0 ? "c3" : "c2", "S", s !== 0 ? "t3" : "t2");
  if (d !== 0) o += dCurve(d, d > 0 ? "c1" : "c4", d > 0 ? "D₁" : "D₂", d > 0 ? "t1" : "t4");
  if (s !== 0) o += sCurve(s, s > 0 ? "c2" : "c4", s > 0 ? "S₁" : "S₂", s > 0 ? "t2" : "t4");
  o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 6, "dot1") + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (d !== 0 || s !== 0) o += dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
  return o;
}
function dirWord(a, b) { return Math.abs(b - a) < 0.5 ? "unchanged" : b > a ? "rises" : "falls"; }
'''

# =========================================================== 2.5.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Prices change when <b>demand or supply shifts</b>, moving the equilibrium. A shift in <b>demand</b> moves price and quantity in the <b>same</b> direction. A shift in <b>supply</b> moves price and quantity in <b>opposite</b> directions. To explain a price change, say <b>which curve shifts</b>, <b>why</b>, which way, and what happens to the <b>new equilibrium</b>.</p></div>

  <h2>The four basic cases</h2>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Curve</th><th>New equilibrium price</th><th>New equilibrium quantity</th></tr>
    <tr><td><b>Increase in demand</b></td><td>D shifts right</td><td>Rises</td><td>Rises</td></tr>
    <tr><td><b>Decrease in demand</b></td><td>D shifts left</td><td>Falls</td><td>Falls</td></tr>
    <tr><td><b>Increase in supply</b></td><td>S shifts right</td><td>Falls</td><td>Rises</td></tr>
    <tr><td><b>Decrease in supply</b></td><td>S shifts left</td><td>Rises</td><td>Falls</td></tr>
  </table></div>

  <h2>Causes of price changes</h2>
  <div class="tw"><table class="t">
    <tr><th>Price rises because…</th><th>Price falls because…</th></tr>
    <tr><td><b>Demand increases:</b> higher incomes, fashion, advertising, price of a substitute rises, population rises</td><td><b>Demand decreases:</b> lower incomes, bad publicity or health warning, price of a substitute falls, population falls</td></tr>
    <tr><td><b>Supply decreases:</b> higher costs, a tax, a drought, new regulations, fewer firms</td><td><b>Supply increases:</b> lower costs, new technology, a subsidy, good weather, more firms</td></tr>
  </table></div>

  <h2>Both curves shift</h2>
  <ul>
    <li>If demand and supply <b>both increase</b>, quantity rises for sure; the price change depends on which shifts more.</li>
    <li>If <b>demand increases</b> and <b>supply decreases</b>, price rises for sure; the quantity change depends on which shifts more.</li>
  </ul>
  <h2>How to answer a diagram question</h2>
  <ul>
    <li>Draw D and S with the original equilibrium (P, Q).</li>
    <li>Shift the relevant curve and label it (D₁ or S₁).</li>
    <li>Mark the new equilibrium (P₁, Q₁) and state the change.</li>
  </ul>
  <p class="note">A change in <b>the good's own price</b> never shifts its own demand or supply curve: price changes are the <b>result</b> of shifts.</p>
'''
js = HEAD + COMMON + DSJS + SHIFTJS + '''
Lib.stepper($("#stD"), { w: 760, h: 380, label: "A rise in demand", base: { d: 0, s: 0 }, draw: (s) => shiftChart(s.d, s.s), steps: [
  { cap: "Starting equilibrium at price P and quantity Q.", s: { d: 0, s: 0 } },
  { cap: "Incomes rise: demand <b>increases</b>. D shifts right to D₁.", s: { d: 30, s: 0 } },
  { cap: "At P there is now a shortage, so the price rises to the new equilibrium <b>P₁</b>, and quantity rises to <b>Q₁</b>.", s: { d: 30, s: 0 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 380, label: "A fall in supply", base: { d: 0, s: 0 }, draw: (s) => shiftChart(s.d, s.s), steps: [
  { cap: "Starting equilibrium at price P and quantity Q.", s: { d: 0, s: 0 } },
  { cap: "A tax raises costs: supply <b>decreases</b>. S shifts left to S₂.", s: { d: 0, s: -30 } },
  { cap: "At P there is now a shortage, so the price <b>rises</b> to P₁ and quantity <b>falls</b> to Q₁.", s: { d: 0, s: -30 } },
] });
const CH = ["Demand or supply shifts", "At the old price quantity demanded no longer equals quantity supplied", "A shortage or surplus appears", "The price adjusts", "A new equilibrium is reached"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "How a shift changes the price", base: { n: 0 }, draw: mkChain(CH, "--accent"), steps: chainSteps(["<b>Demand or supply shifts</b>.", "At the old price quantity demanded no longer equals quantity supplied.", "A <b>shortage or surplus</b> appears.", "The <b>price adjusts</b>.", "A <b>new equilibrium</b> is reached."]) });

/* Lab 1: shift both */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const d = +$("#sa").value, s = +$("#sb").value, [q0, p0] = eq(0, 0), [q1, p1] = eq(d, s);
  $("#sa1").textContent = "$" + money(p1, 0) + " (" + dirWord(p0, p1) + ")"; $("#sa2").textContent = money(q1, 0) + " (" + dirWord(q0, q1) + ")"; $("#sa3").textContent = d === 0 && s === 0 ? "None" : d !== 0 && s !== 0 ? "Both" : d !== 0 ? "Demand" : "Supply";
  $("#sav").textContent = `Equilibrium moves from price $${money(p0, 0)}, quantity ${money(q0, 0)} to price $${money(p1, 0)}, quantity ${money(q1, 0)}. ` + (d !== 0 && s === 0 ? "Only demand shifts: price and quantity move in the same direction." : s !== 0 && d === 0 ? "Only supply shifts: price and quantity move in opposite directions." : d !== 0 && s !== 0 ? "Both curves shift: the effect on one variable depends on which shift is bigger." : "No shift: no change.");
  $("#labS").innerHTML = shiftChart(d, s);
}
Lib.slider($("#g1"), { id: "sa", label: "Shift in demand (right +, left −)", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Shift in supply (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labS });
const CAUSE = [
  { n: "Incomes rise", c: "Demand increases", p: "Price rises", q: "Quantity rises" },
  { n: "A health warning on a product", c: "Demand decreases", p: "Price falls", q: "Quantity falls" },
  { n: "Costs of production rise", c: "Supply decreases", p: "Price rises", q: "Quantity falls" },
  { n: "New technology", c: "Supply increases", p: "Price falls", q: "Quantity rises" },
  { n: "A subsidy to producers", c: "Supply increases", p: "Price falls", q: "Quantity rises" },
  { n: "A drought hits farms", c: "Supply decreases", p: "Price rises", q: "Quantity falls" },
];
button_table("caBtns", "caOut", CAUSE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Curve</th><th>Price</th><th>Quantity</th></tr><tr><td><b>${p.c}</b></td><td>${p.p}</td><td>${p.q}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>price</b> in each case?", buckets: [{ label: "Price rises" }, { label: "Price falls" }], items: [
  { text: "Demand increases", b: 0 }, { text: "Supply decreases", b: 0 }, { text: "A drought hits the harvest", b: 0 }, { text: "Incomes rise (normal good)", b: 0 },
  { text: "Demand decreases", b: 1 }, { text: "Supply increases", b: 1 }, { text: "New technology cuts costs", b: 1 }, { text: "A subsidy to producers", b: 1 },
], done: "Think: which curve, which way?" });
Lib.classify($("#cl2"), { prompt: "Which <b>curve shifts</b>?", buckets: [{ label: "Demand" }, { label: "Supply" }], items: [
  { text: "Incomes rise", b: 0 }, { text: "Fashion changes", b: 0 }, { text: "Price of a substitute rises", b: 0 },
  { text: "Wages rise", b: 1 }, { text: "A tax on producers", b: 1 }, { text: "New technology", b: 1 },
], done: "Demand: buyers. Supply: producers." });
Lib.match($("#m1"), { prompt: "Match the change to its effect.", pairs: [
  ["Demand right", "Price and quantity rise"],
  ["Demand left", "Price and quantity fall"],
  ["Supply right", "Price falls, quantity rises"],
  ["Supply left", "Price rises, quantity falls"],
  ["Both D and S right", "Quantity rises for sure"],
  ["D right, S left", "Price rises for sure"],
], done: "Learn the four basic cases." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an increase in incomes raises the price of a good</b>.", items: [
  "Incomes rise",
  "Demand for the good increases: D shifts right",
  "At the old price there is a shortage",
  "Price rises",
  "A new equilibrium at a higher price and quantity",
], done: "Demand up, price up." });
''' + calc_js([
    ("The equilibrium price rises from $50 to $60. What is the percentage rise?", 20, "10 ÷ 50 × 100 = <b>20%</b>.", None, None),
    ("The equilibrium quantity rises from 50 to 60 units. What is the percentage rise?", 20, "10 ÷ 50 × 100 = <b>20%</b>.", None, None),
]) + mcq_js("qz1", [
    ("An increase in demand will cause the equilibrium price to:", ["Rise", "Fall", "Stay the same", "Fall and quantity fall"], 0, "Shortage at the old price."),
    ("A fall in supply will cause price to:", ["Rise", "Fall", "Stay the same", "Halve"], 0, "Shortage at the old price."),
    ("An increase in supply will cause quantity to:", ["Rise", "Fall", "Stay the same", "Disappear"], 0, "More is supplied and bought."),
    ("A new tax on producers shifts:", ["Demand right", "Supply left", "Supply right", "Demand left"], 1, "Costs rise."),
    ("If both demand and supply increase, equilibrium quantity:", ["Rises", "Falls", "Is unchanged", "Is uncertain"], 0, "Both push quantity up."),
]) + "\n" + cards_js([("New equilibrium", "The equilibrium reached after a shift in demand or supply."), ("Increase in demand", "D shifts right."), ("Decrease in demand", "D shifts left."), ("Increase in supply", "S shifts right."), ("Decrease in supply", "S shifts left."), ("Shortage", "Quantity demanded exceeds quantity supplied."), ("Surplus", "Quantity supplied exceeds quantity demanded."), ("Equilibrium price", "The price at which the market clears."), ("Ceteris paribus", "All other things unchanged.")]) + "labS(); \n"
explore = '''
  <h2>Lab 1 · Shift demand and supply</h2>
  <p>Shift either or both curves and watch the equilibrium price and quantity change.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>New price</small><strong id="sa1"></strong></div><div><small>New quantity</small><strong id="sa2"></strong></div><div><small>Shifted</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 340" role="img" aria-label="Demand and supply shifts"></svg>
  </div>

  <h2>Lab 2 · Causes of price changes</h2>
  <p>Pick an event to see which curve shifts and the effect on price and quantity.</p>
  <div class="card"><div class="row" id="caBtns"></div><div id="caOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how an increase in income may affect the price of a normal good.", "Demand rises; shortage; price rises.",
      "[K|A rise in income increases demand for a normal good, shifting the demand curve to the right.] [N|At the original price quantity demanded exceeds quantity supplied, so there is a shortage.] [N|The price rises until a new equilibrium is reached at a higher price and quantity.]"),
    Q(2, "Analyse", 4, "Analyse why the price of German luxury cars may have increased in 2018. (Oct/Nov 2020, P22 style)", "Demand up (incomes, exports) or supply down (costs, tariffs).",
      "[K|Demand for luxury cars may have increased because incomes in key markets rose,] [N|shifting the demand curve right and raising the equilibrium price.] [K|Supply may have fallen because of higher costs or trade tariffs,] [N|shifting supply left and raising the price.]"),
    Q(3, "Analyse", 6, "Analyse, using a demand and supply diagram, how a drought could affect the market for wheat. (Oct/Nov 2023, P22 style)", "Supply left; shortage; price up; quantity down.",
      "[K|A drought reduces the harvest, so supply of wheat decreases and S shifts left.] [N|At the original price quantity demanded exceeds quantity supplied: a shortage.] [N|The price rises to a new equilibrium P₁ and quantity falls to Q₁.] [E|Because wheat is a necessity the rise in price may be large.]", key=True),
    Q(4, "Analyse", 6, "Analyse, using a demand and supply diagram, how an increase in population size will affect the market for housing. (Feb/Mar 2024, P22 style)", "Demand right; price up; quantity up.",
      "[K|A larger population increases demand for housing, so D shifts right.] [N|At the old price there is a shortage, so the price rises to P₁ and the quantity traded rises to Q₁.] [E|The quantity rise depends on how quickly new housing can be supplied.]", key=True),
    Q(5, "Analyse", 6, "Analyse, using a demand and supply diagram, how a subsidy given to producers could affect the market for solar panels.", "Supply right; price falls; quantity rises.",
      "[K|A subsidy lowers producers' costs, so supply increases and S shifts right.] [N|At the old price there is a surplus, so price falls to P₁ and quantity rises to Q₁.] [N|Consumers pay a lower price and buy more.] [E|The effect depends on how much of the subsidy is passed on in lower prices.]", key=True),
)
tp = tips([
    ("Say which curve shifts.", "And which way, and why."),
    ("Draw D, S, then the shift.", "Label D₁ or S₁, P₁ and Q₁."),
    ("Describe the new equilibrium.", "Price and quantity, both."),
    ("Demand shifts: P and Q same direction.", "Supply shifts: opposite."),
    ("Use a shortage or surplus link.", "It explains why the price moves."),
], cmds("Explain", "Analyse"))
body = page(CL("2.5.1 Causes of price changes"), "Causes of Price Changes", "How shifts in demand and supply change the equilibrium price and quantity. Syllabus 2.5.1.",
    learn=learn, watch=watch(("A rise in demand", "stD"), ("A fall in supply", "stS"), ("How a shift changes the price", "stC")), explore=explore,
    practise=practise(("Price rises or falls?", "cl1", "card"), ("Which curve shifts?", "cl2", "card"), ("Match the change", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Housing in growing cities", "A rising population raises demand for homes and pushes up prices and rents.", "Demand increase."),
        rw("Oil prices", "A cut in output by producers shifts supply left, raising the world oil price.", "Supply decrease."),
        rw("Falling cost of electronics", "Technology has lowered the cost of making phones and TVs, so prices fall.", "Supply increase."),
        rw("Weather and food prices", "A poor harvest cuts supply and raises food prices.", "Supply decrease.")),
    exam=ex, tips=tp)
write("c251", body, js, "Causes of Price Changes", "ig-price-causes")

# =========================================================== 2.5.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A change in price affects <b>sales</b> (the quantity sold) and the revenue and profit of <b>producers</b>, as well as the quantity and choices of <b>consumers</b>. Demand and supply diagrams show the impact of a change in market conditions, such as a rise in income, a tax, a subsidy or a change in costs.</p></div>

  <h2>Effects on sales and revenue</h2>
  <div class="formula">Total revenue = price × quantity sold</div>
  <ul>
    <li>When the <b>price rises</b> (movement along demand), quantity demanded <b>falls</b>. Revenue changes depend on how responsive demand is (see PED in 2.6).</li>
    <li>When <b>demand shifts right</b>, both price and quantity rise, so <b>revenue rises</b>.</li>
    <li>When <b>supply shifts right</b> (increase), price falls but quantity rises: <b>sales</b> rise, and revenue may rise or fall.</li>
    <li>When <b>supply shifts left</b> (decrease), price rises and sales fall.</li>
  </ul>

  <h2>Effects on consumers and producers</h2>
  <div class="tw"><table class="t">
    <tr><th>Market change</th><th>Consumers</th><th>Producers</th></tr>
    <tr><td><b>Price rises</b> (demand up)</td><td>Pay more; some buy less or switch to substitutes</td><td>Higher revenue and profit per unit; more sales; incentive to produce more</td></tr>
    <tr><td><b>Price falls</b> (supply up)</td><td>Pay less; can buy more; living standards may rise</td><td>Lower price per unit but more sales; profit depends on costs</td></tr>
    <tr><td><b>Price rises</b> (supply down)</td><td>Pay more and buy less</td><td>Higher price per unit but lower quantity; costs have risen</td></tr>
  </table></div>

  <h2>Using diagrams for different market conditions</h2>
  <div class="tw"><table class="t">
    <tr><th>Market condition</th><th>Curve</th><th>Effect</th></tr>
    <tr><td>Higher incomes, fashion, advertising</td><td>D right</td><td>Price and quantity rise</td></tr>
    <tr><td>Health warning, falling incomes</td><td>D left</td><td>Price and quantity fall</td></tr>
    <tr><td>Subsidy, new technology, lower costs</td><td>S right</td><td>Price falls, quantity rises</td></tr>
    <tr><td>Tax, higher costs, drought</td><td>S left</td><td>Price rises, quantity falls</td></tr>
  </table></div>
  <p class="note">An effect on <b>revenue</b> needs both price and quantity: multiply the new price by the new quantity and compare with the old.</p>
'''
js = HEAD + COMMON + DSJS + SHIFTJS + '''
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Revenue after a rise in demand", base: { d: 0, s: 0 }, draw: (s) => {
  let o = shiftChart(s.d, s.s); const [q0, p0] = eq(0, 0), [q1, p1] = eq(s.d, s.s);
  o += SV.text(X(60), Y(104), "Old revenue: " + money(p0 * q0, 0), "sm bd");
  if (s.d !== 0) o += SV.text(X(60), Y(96), "New revenue: " + money(p1 * q1, 0), "lbl bd t2");
  return o;
}, steps: [
  { cap: "Starting equilibrium: price P, quantity Q. Revenue = P × Q.", s: { d: 0, s: 0 } },
  { cap: "Demand <b>increases</b>: both price and quantity rise, so <b>revenue rises</b> (P₁ × Q₁).", s: { d: 30, s: 0 } },
] });
Lib.stepper($("#stU"), { w: 760, h: 380, label: "Supply increase and sales", base: { d: 0, s: 0 }, draw: (s) => {
  let o = shiftChart(s.d, s.s); const [q0, p0] = eq(0, 0), [q1, p1] = eq(s.d, s.s);
  o += SV.text(X(60), Y(104), "Old revenue: " + money(p0 * q0, 0), "sm bd");
  if (s.s !== 0) o += SV.text(X(60), Y(96), "New revenue: " + money(p1 * q1, 0), "lbl bd t2");
  return o;
}, steps: [
  { cap: "Starting equilibrium.", s: { d: 0, s: 0 } },
  { cap: "A subsidy increases supply: the price <b>falls</b> but <b>sales rise</b>. Consumers benefit from lower prices.", s: { d: 0, s: 30 } },
] });
const IM = ["A change in market conditions shifts demand or supply", "The equilibrium price and quantity change", "Sales (quantity) and revenue change for producers", "Consumers pay more or less and buy more or less", "Firms may expand or cut production"];
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Impact of a change", base: { n: 0 }, draw: mkChain(IM, "--accent"), steps: chainSteps(["A change in <b>market conditions</b> shifts demand or supply.", "The <b>equilibrium price and quantity</b> change.", "<b>Sales and revenue</b> change for producers.", "<b>Consumers</b> pay more or less and buy more or less.", "Firms may <b>expand or cut production</b>."]) });

/* Lab 1: events */
const EV = [
  { n: "Incomes rise (normal good)", d: 25, s: 0 }, { n: "A health warning", d: -25, s: 0 }, { n: "A subsidy to producers", d: 0, s: 25 }, { n: "A tax on producers", d: 0, s: -25 },
  { n: "New technology", d: 0, s: 30 }, { n: "A drought", d: 0, s: -30 }, { n: "Demand and supply both rise", d: 20, s: 20 },
];
function labV() {
  if (!$("#va")) return;
  const e = EV[+$("#va").value], [q0, p0] = eq(0, 0), [q1, p1] = eq(e.d, e.s), r0 = p0 * q0, r1 = p1 * q1;
  $("#va1").textContent = "$" + money(p1, 0) + " (" + dirWord(p0, p1) + ")"; $("#va2").textContent = money(q1, 0) + " (" + dirWord(q0, q1) + ")"; $("#va3").textContent = money(r1, 0) + " (" + dirWord(r0, r1) + ")";
  $("#vav").textContent = `${e.n}: price ${dirWord(p0, p1)}, sales ${dirWord(q0, q1)}, revenue ${dirWord(r0, r1)} (from ${money(r0, 0)} to ${money(r1, 0)}). ${p1 < p0 ? "Consumers gain from lower prices." : p1 > p0 ? "Consumers pay more." : ""}`;
  $("#labV").innerHTML = shiftChart(e.d, e.s);
}
Lib.slider($("#g1"), { id: "va", label: "Choose an event (0 to 6)", min: 0, max: 6, step: 1, value: 0, fmt: (v) => EV[v].n, onInput: labV });
const WB = [
  { n: "Consumers", b: "Lower prices and more choice after a supply increase", c: "Higher prices and less choice after a supply decrease" },
  { n: "Producers", b: "Higher revenue after a demand increase; subsidies", c: "Taxes and higher costs; falling demand" },
  { n: "Workers", b: "More jobs when sales rise", c: "Job losses when sales fall" },
  { n: "Government", b: "More tax revenue when sales rise", c: "Pays subsidies; may lose tax revenue" },
];
button_table("wbBtns", "wbOut", WB, 0, (p) => `<div class="tw"><table class="t"><tr><th>Gains</th><th>Loses</th></tr><tr><td>${p.b}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>sales</b> (quantity)?", buckets: [{ label: "Sales rise" }, { label: "Sales fall" }], items: [
  { text: "Demand increases", b: 0 }, { text: "Supply increases", b: 0 }, { text: "A subsidy to producers", b: 0 }, { text: "New technology cuts costs", b: 0 },
  { text: "Demand decreases", b: 1 }, { text: "Supply decreases", b: 1 }, { text: "A tax on producers", b: 1 }, { text: "A drought", b: 1 },
], done: "Right shifts raise quantity; left shifts lower it." });
Lib.classify($("#cl2"), { prompt: "Who <b>benefits</b> from each?", buckets: [{ label: "Consumers" }, { label: "Producers" }], items: [
  { text: "A fall in price after supply increases", b: 0 }, { text: "More choice and lower prices", b: 0 },
  { text: "A rise in revenue after demand increases", b: 1 }, { text: "A subsidy that lowers costs", b: 1 },
], done: "Think about who gains from the change." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Revenue", "Price multiplied by quantity sold"],
  ["Sales", "The quantity sold"],
  ["Subsidy", "A payment to producers that lowers costs"],
  ["Indirect tax", "A tax that raises producers' costs"],
  ["Market conditions", "Factors that shift demand or supply"],
  ["New equilibrium", "The result of a shift"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a subsidy changes the market for solar panels</b>.", items: [
  "The government gives a subsidy to producers",
  "Costs fall: supply increases",
  "The price falls and the quantity rises",
  "Consumers buy more at a lower price",
  "Producers' sales rise",
], done: "A supply increase." });
''' + calc_js([
    ("Price is $50 and quantity is 50. What is the revenue ($)?", 2500, "50 × 50 = <b>$2,500</b>.", None, None),
    ("After a rise in demand, price is $60 and quantity is 60. By how much does revenue rise ($) from $2,500?", 1100, "60 × 60 = 3,600; 3,600 − 2,500 = <b>$1,100</b>.", None, None),
    ("After a supply increase, price is $40 and quantity is 60. By how much does revenue change ($) from $2,500? (enter the change)", -100, "40 × 60 = 2,400; 2,400 − 2,500 = <b>−$100</b>.", None, None),
]) + mcq_js("qz1", [
    ("Total revenue is:", ["Price + quantity", "Price × quantity", "Price − cost", "Quantity ÷ price"], 1, "Revenue = P × Q."),
    ("An increase in supply causes:", ["Higher price, lower quantity", "Lower price, higher quantity", "Higher price, higher quantity", "No change"], 1, "Surplus at the old price."),
    ("A subsidy to producers:", ["Raises prices", "Lowers costs and increases supply", "Reduces sales", "Shifts demand"], 1, "Lower costs."),
    ("After a rise in demand, producers' revenue:", ["Rises", "Falls", "Is unchanged", "Is zero"], 0, "P and Q both rise."),
    ("Consumers gain from:", ["A fall in supply", "An increase in supply", "A tax on producers", "A drought"], 1, "Lower prices."),
]) + "\n" + cards_js([("Total revenue", "Price multiplied by quantity sold."), ("Sales", "The quantity of a good sold."), ("Market conditions", "Factors that shift demand or supply."), ("Subsidy", "A payment to producers that lowers costs."), ("Indirect tax", "A tax on goods that raises costs."), ("Consumer", "A buyer of goods and services."), ("Producer", "A seller or maker of goods and services."), ("New equilibrium", "The result of a shift in demand or supply."), ("Living standards", "The quality of life, linked to what people can buy.")]) + "labV(); \n"
explore = '''
  <h2>Lab 1 · Events in a market</h2>
  <p>Pick an event and see its effect on price, sales and revenue.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>New price</small><strong id="va1"></strong></div><div><small>New sales</small><strong id="va2"></strong></div><div><small>New revenue</small><strong id="va3"></strong></div></div><div class="verdict" id="vav"></div></div></div>
    <svg id="labV" viewBox="0 0 760 340" role="img" aria-label="Effect of an event on a market"></svg>
  </div>

  <h2>Lab 2 · Who gains and who loses?</h2>
  <p>Pick a group to see how changes in price affect them.</p>
  <div class="card"><div class="row" id="wbBtns"></div><div id="wbOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how an increase in the price of milk may affect the revenue earned by milk producers.", "Quantity falls; revenue depends on PED.",
      "[K|Revenue is price multiplied by quantity sold.] [N|A higher price means each litre earns more, but quantity demanded falls.] [N|If demand is inelastic, revenue rises; if elastic, revenue falls.]"),
    Q(2, "Analyse", 6, "Analyse, using a demand and supply diagram, how a greater awareness of the health benefits of a product will affect its market. (Oct/Nov 2022, P22 style)", "Tastes: D right; price and quantity up; revenue up.",
      "[K|Greater awareness changes tastes in favour of the product, so demand increases and D shifts right.] [N|At the old price there is a shortage, so the price rises to P₁ and quantity to Q₁.] [N|Producers' sales and revenue rise.] [E|Producers may increase supply in time, limiting the rise in price.]", key=True),
    Q(3, "Analyse", 6, "Analyse how a subsidy given to producers could affect consumers and producers. (Feb/Mar 2022, P22 style)", "S right; price falls, quantity up; consumers gain; producers' costs fall.",
      "[K|A subsidy lowers production costs, so supply increases and S shifts right.] [N|The price falls and the quantity rises, so consumers pay less and can buy more.] [N|Producers' costs are lower and sales rise, though the price per unit is lower.] [E|The cost to the government is an opportunity cost.]", key=True),
    Q(4, "Analyse", 6, "Analyse, using a demand and supply diagram, the effects of higher quality products on the market. (Oct/Nov 2024, P22 style)", "Better quality: D right; price and quantity up.",
      "[K|Higher quality makes the product more attractive, so demand increases and D shifts right.] [N|The equilibrium price and quantity rise.] [N|Producers' sales and revenue rise.] [E|If quality needs costly inputs, supply may fall, reducing the increase in quantity.]", key=True),
)
tp = tips([
    ("Revenue = price × quantity.", "Compare old and new."),
    ("Name the change in market conditions.", "Then which curve it shifts."),
    ("Discuss consumers and producers.", "Both gain or lose differently."),
    ("Use a diagram.", "Label D₁, S₁, P₁, Q₁."),
    ("Evaluate with elasticity or time.", "Effects vary."),
], cmds("Explain", "Analyse"))
body = page(CL("2.5.2 Consequences of price changes"), "Consequences of Price Changes", "How price changes affect sales, revenue, consumers and producers, and how to show changes in market conditions on diagrams. Syllabus 2.5.2.",
    learn=learn, watch=watch(("Revenue after a rise in demand", "stR"), ("Supply increase and sales", "stU"), ("Impact of a change", "stI")), explore=explore,
    practise=practise(("Sales rise or fall?", "cl1", "card"), ("Who benefits?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Solar panels", "Falling costs and subsidies have lowered prices and sharply increased sales.", "A supply increase."),
        rw("Housing booms", "Rising demand raises prices and builders' revenue, but makes homes less affordable.", "Winners and losers."),
        rw("Fuel taxes", "Taxes on producers raise costs and reduce supply, so prices rise and sales fall.", "A supply decrease."),
        rw("Health campaigns", "Warnings on sugary drinks have reduced demand and sales.", "A demand decrease.")),
    exam=ex, tips=tp)
write("c252", body, js, "Consequences of Price Changes", "ig-price-consequences")
