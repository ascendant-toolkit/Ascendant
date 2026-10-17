"""AS syllabus 2.5.1-2.5.2 Consumer surplus and producer surplus. Run: python3 tools/artifact-kit/mk_as26.py"""
from asx import *
EY = EYAS("2.5.1 to 2.5.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Consumer surplus</b> is the difference between the <b>price consumers are willing to pay</b> and the <b>price they actually pay</b>, shown on a diagram as the triangle <b>below the demand curve and above the price</b>. <b class="kw">Producer surplus</b> is the difference between the <b>price producers receive</b> and the <b>minimum price they would be willing to accept</b>, shown as the triangle <b>above the supply curve and below the price</b>. At the <b>equilibrium</b> price both are at work and the <b>total surplus (economic welfare)</b> is greatest, which is why economists see a competitive market as <b>allocatively efficient</b>. A change in price, or a policy that moves the market away from equilibrium, shifts surplus between consumers and producers and may <b>reduce the total</b>.</p></div>

  <h2>1 · Consumer surplus (2.5.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The demand curve shows the <b>maximum price</b> each consumer is willing to pay for each unit. If the market price is lower, every buyer except the last pays <b>less than they were willing to</b>.</li>
    <li><b>Consumer surplus (CS) = willingness to pay − price paid.</b> On a straight-line demand curve: CS = ½ × quantity × (highest price on the demand curve − market price).</li>
    <li><b>Significance:</b> it measures the <b>benefit (welfare)</b> consumers gain from a market beyond what they pay. A fall in price raises CS; a rise lowers it.</li>
  </ul>

  <h2>2 · Producer surplus (2.5.2)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>The supply curve shows the <b>minimum price</b> producers will accept for each unit (roughly the marginal cost).</li>
    <li><b>Producer surplus (PS) = price received − minimum acceptable price.</b> On a straight-line supply curve: PS = ½ × quantity × (market price − price where supply begins).</li>
    <li><b>Significance:</b> it measures the <b>benefit to producers</b>, a bit like economic profit. A rise in price raises PS; a fall lowers it.</li>
  </ul>

  <div class="tw"><table class="t">
    <tr><th></th><th>Consumer surplus</th><th>Producer surplus</th></tr>
    <tr><td><b>Meaning</b></td><td>Willing to pay − price paid</td><td>Price received − willing to accept</td></tr>
    <tr><td><b>Area on the diagram</b></td><td>Below demand, above price</td><td>Above supply, below price</td></tr>
    <tr><td><b>Price rises</b></td><td>Falls</td><td>Rises</td></tr>
    <tr><td><b>Price falls</b></td><td>Rises</td><td>Falls</td></tr>
    <tr><td><b>Total surplus</b></td><td colspan="2">CS + PS: largest at the equilibrium of a competitive market</td></tr>
  </table></div>
  <ul>
    <li><b>Why it matters:</b> showing who gains and loses from a change in price, subsidy, tax or price control. A policy that cuts output below the equilibrium <b>destroys some total surplus</b> (a welfare loss).</li>
    <li><b>Limits:</b> willingness to pay depends on income; surplus ignores externalities; measuring it exactly in real markets is difficult.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Draw the diagram, <b>shade or label both areas</b> and name them: CS above the price, PS below it. Say whether each area <b>grows or shrinks</b> and why.</div>
'''

watch = '''
  <h2>1 · Building the surplus diagram</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stS"></div>
  <h2>2 · Surplus for individual buyers</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Surplus in the market</h2>
  <p>Shift demand and supply and see consumer surplus, producer surplus and the total in the new equilibrium.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Consumer surplus</small><strong id="r1"></strong></div><div><small>Producer surplus</small><strong id="r2"></strong></div><div><small>Total surplus</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with consumer and producer surplus shaded"></svg></div></div></div>

  <h2>Lab 2 · Set the price</h2>
  <p>Fix the price above or below the equilibrium of $50. Quantity traded is the smaller of the amounts demanded and supplied, so total surplus falls away from equilibrium.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Consumer surplus</small><strong id="t1"></strong></div><div><small>Producer surplus</small><strong id="t2"></strong></div><div><small>Welfare loss</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a fixed price and the consumer and producer surplus shaded"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Consumer or producer surplus?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the construction of the diagram in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A bargain at the shops", "A shopper would pay up to $80 for a coat and finds it on sale for $50. The $30 difference is that shopper's consumer surplus. Summed across every buyer, it measures the benefit consumers get from the market.", "willingness to pay minus price paid.") +
rw("A farmer at harvest", "A farmer would accept as little as $3 per kilo to grow tomatoes but can sell them for $5. The $2 gap is producer surplus on that unit. Over the whole crop it shows how much better off the farmer is for being able to sell at the market price.", "price received minus willingness to accept.") +
rw("Concert ticket prices", "If a promoter sets the ticket price too low, many fans get surplus, but not everyone can buy and the promoter earns less. If it is set too high, fewer people go and total surplus falls. The best level for total surplus is where demand equals supply.", "total surplus is highest at equilibrium.") +
rw("Cheaper flights", "As airfares have fallen over time, passengers who would have paid more now pay less, so consumer surplus has risen for millions of travellers, even before counting new people who can now afford to fly.", "a fall in price raising consumer surplus.")
)

mc_exam = [
  mcq("s22_13", 11, "What is meant by consumer surplus?", ["It is the amount by which the price consumers are willing to pay exceeds the market price", "It is the difference between the price consumers are willing to pay and the price producers are willing to supply", "It is the discount firms offer to the consumers for buying goods in bulk", "It is the excess of quantity demanded of a product over its quantity supplied at a given price"], 0, "Consumer surplus is willingness to pay minus the price actually paid."),
  mcq("m21_12", 8, "Which example of consumer behaviour would create consumer surplus?", ["when a consumer does not spend all of her income each month", "when a consumer pays less than they are willing to pay for a good", "when a consumer throws away vegetables because they bought too much", "when a good is purchased in order to resell it at a higher price"], 1, "Paying less than the maximum you would pay creates consumer surplus."),
  mcq("w21_13", 5, "What could cause an increase in consumer surplus in the market for a good? (an increase in demand for the good, an increase in supply of the good)", ["no increase in demand, no increase in supply", "no increase in demand, an increase in supply", "an increase in demand, no increase in supply", "an increase in demand and an increase in supply"], 3, "A higher demand lifts the demand curve and so adds willingness to pay, and a rise in supply lowers the price, so both raise consumer surplus."),
  mcq("s21_12", 11, "A private company achieves a producer surplus at the market equilibrium price. What might reduce the size of the private company's producer surplus?", ["Private companies choose to prioritise profits over customer needs", "Private companies start to pay dividends out of profits", "The government fixes the price of electricity below the market price", "The private company supply curve becomes more elastic"], 2, "A price below the market price lowers the price producers receive, so their surplus falls."),
  mcq("s20_13", 26, "An economy with a long history of extensive barriers to trade decides to switch to totally free trade. What is most likely to increase in the short term?", ["consumer surplus", "government revenue", "inflationary pressure", "profits of all domestic companies"], 0, "Removing trade barriers lowers prices for consumers, so consumer surplus rises. Tariff revenue and some domestic profits fall.")
]

exam = exam_page("consumer surplus and producer surplus",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Consumer surplus is in an 8 mark Paper 2 part most years and in Paper 1 every year, often with a diagram. Reworded past questions are below, with five Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "1", "May/June 2023 (22) Q2(a)"), ("Data response, 4 marks", "1", "Feb/March 2025 (22) Q1(c)"), ("Multiple choice (Paper 1)", "5 shown below", "2020 to 2025")],
  [
  eq(P("s23_22", "2(a)"), "8 marks", "With the help of a diagram, explain what is meant by consumer surplus and producer surplus and consider whether a rise in the price of a product because of higher costs of production is likely to always reduce the consumer surplus.",
     ["Knowledge (up to 3): consumer surplus is the difference between the price a consumer is willing to pay and the market price (1); producer surplus is the difference between the price a producer is willing to accept and what is actually paid (1); both shown on an accurately labelled diagram (1).",
      "Analysis (up to 3): a diagram showing the supply curve shifting left (1), explaining and showing the change in consumer surplus for a product with elastic demand (1) compared with one with inelastic demand (1).",
      "Evaluation (up to 2): consumer surplus will always fall (1), but the extent of the fall depends on the value of the price elasticity of demand (1)."],
     "Define CS and PS on a diagram. Supply shifts left, price up, CS falls. Elastic vs inelastic. Evaluate: always falls, size depends on PED.",
     [[("k", "Consumer surplus is the gap between the price consumers are willing to pay and the price they actually pay, the area under the demand curve above the price. Producer surplus is the gap between the price producers receive and the lowest price they would accept, the area above the supply curve below the price.")], [("n", "A rise in the costs of production shifts the supply curve to the left. The equilibrium price rises and quantity falls, so the consumer surplus triangle becomes smaller. If demand is price elastic, quantity falls a lot and consumer surplus falls by more. If demand is inelastic, quantity falls less but the price rise is larger, so the loss is still substantial.")], [("e", "Consumer surplus is likely to fall in either case, since the price rises and quantity falls. But the extent of the fall depends on the price elasticity of demand, so it is a matter of degree and not whether it falls.")]]),
  eq(P("m25_22", "1(c)"), "4 marks", "A drought pushes up the cost of producing olive oil and the market price rises. With the help of a demand and supply diagram, consider the possible impact on consumer surplus.",
     ["A correctly labelled diagram showing the initial consumer surplus (1).", "A leftward shift of the supply curve establishing the new consumer surplus because of the price rise and fall in quantity (1).", "An explanation that the difference between the price consumers are willing to pay and the market price falls, so consumer surplus falls (1).", "Up to 1 mark for valid evaluation, for example that the impact depends on the price elasticity of demand, with some explanation (1)."],
     "Diagram with initial CS. Supply shifts left. CS falls. Depends on PED.",
     [[("k", "On a demand and supply diagram, the initial consumer surplus is the triangle between the demand curve and the equilibrium price. A rise in production costs shifts the supply curve to the left, raising the price and reducing quantity."), ("n", "The new consumer surplus triangle is smaller, because the gap between what consumers are willing to pay and the market price has fallen, so consumer surplus will fall. The size of the fall depends on how price elastic demand for olive oil is: if buyers have good substitutes, quantity falls more and the price rises less.")]])
  ],
  )

tips = tips_html(
  [("Know both definitions exactly.", "CS: willing to pay minus price. PS: price minus willing to accept."),
   ("Name the areas.", "CS above the price, below demand. PS below the price, above supply."),
   ("Draw and label.", "Axes, D, S, equilibrium, price line, shaded areas."),
   ("Price rise lowers CS.", "And raises PS (for the same quantity)."),
   ("Say total surplus is largest at equilibrium.", "Away from it, some surplus is lost."),
   ("Don't confuse with revenue or profit.", "Surplus is a gain beyond what is paid or the minimum accepted."),
   ("Mention elasticity.", "It decides how big the change is.")],
  [("Consumer surplus", "Consumer surplus is the difference between what consumers are willing to pay and what they pay."),
   ("Producer surplus", "Producer surplus is the difference between the price producers receive and the minimum they would accept."),
   ("Equilibrium", "Total surplus is highest at the market equilibrium."),
   ("Shift", "A shift of supply to the left could reduce consumer surplus."),
   ("Extent", "The fall depends on the price elasticity of demand.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
const poly = (pts, c, v) => SV.poly(pts.map(([q, p]) => [SDX(q), SDY(p)]), c, op(v));
function sfDraw(s) {
  let o = sdPlot({ d: 0, s: 0, g: 0 }) + SV.line(70, SDY(50), SDX(50), SDY(50), "dash") + SV.text(62, SDY(50) + 4, "P", "sm", { "text-anchor": "end" }) + SV.text(SDX(50), 286, "Q", "sm", { "text-anchor": "middle" });
  o += poly([[0, 90], [0, 50], [50, 50]], "f3", 0.5 * s.c) + poly([[0, 10], [0, 50], [50, 50]], "f2", 0.5 * s.p);
  if (s.c > 0.2) o += SV.text(SDX(14), SDY(60) + 4, "Consumer surplus", "lbl bd", { ...halo, ...op(s.c) });
  if (s.p > 0.2) o += SV.text(SDX(14), SDY(40) + 4, "Producer surplus", "lbl bd", { ...halo, ...op(s.p) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Consumer surplus is the triangle below the demand curve and above the price">${sfDraw({ c: 1, p: 0 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Producer surplus is the triangle above the supply curve and below the price">${sfDraw({ c: 0, p: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "Consumer and producer surplus on a supply and demand diagram", base: { c: 0, p: 0 }, draw: sfDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The market.</b> Demand shows what buyers are willing to pay; supply shows the lowest price sellers will accept. The equilibrium price is $50.", s: { c: 0, p: 0 } },
  { cap: "<b>Consumer surplus.</b> Buyers on the upper part of the demand curve would pay more than $50, so they gain the gap. The triangle below demand and above the price is <b>consumer surplus</b>.", s: { c: 1, p: 0 } },
  { cap: "<b>Producer surplus.</b> Sellers on the lower part of the supply curve would accept less than $50. The triangle above supply and below the price is <b>producer surplus</b>.", s: { c: 1, p: 1 } },
  { cap: "<b>Total surplus</b> is the two areas together. It is greatest at the equilibrium, where every unit worth more to buyers than it costs to produce is traded.", s: { c: 1, p: 1 } },
] });

/* ---------- individual buyers ---------- */
function bbDraw(s) {
  const W = [90, 80, 70, 60, 50], px = 60, y = (v) => 270 - v * 2.4; let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Willingness to pay ($)", "sm");
  W.forEach((w, i) => { const x = 90 + i * 120, buys = w >= px; o += SV.rect(x, y(w), 70, 270 - y(w), "f1", op(0.35 * s.a)); if (buys && s.c > 0) o += SV.rect(x, y(w), 70, y(px) - y(w), "f3", op(0.7 * s.c)) + SV.text(x + 35, (y(w) + y(px)) / 2 + 5, "$" + (w - px), "lbl bd", { "text-anchor": "middle", ...op(s.c) }); o += SV.text(x + 35, 286, "Buyer " + "ABCDE"[i], "sm", { "text-anchor": "middle", ...op(s.a) }) + SV.text(x + 35, y(w) - 6, "$" + w, "sm", { "text-anchor": "middle", ...op(s.a) }); });
  if (s.b > 0) o += SV.line(60, y(px), 700, y(px), "c4", { "stroke-width": 2.5, ...op(s.b) }) + tag(696, y(px) - 6, "Market price $60", "c4", s.b, "end");
  if (s.c > 0.5) o += tag(380, 50, "Consumer surplus = 30 + 20 + 10 + 0 = $60. Buyer E (willing to pay $50) does not buy.", "c3", s.c, "middle");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 300, label: "Five buyers, a market price of $60 and their surplus", base: { a: 0, b: 0, c: 0 }, draw: bbDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Willingness to pay.</b> Five buyers would pay at most $90, $80, $70, $60 and $50 for one unit.", s: { a: 1 } },
  { cap: "<b>A market price of $60.</b> Buyers A to D are willing to pay at least $60, so they buy. Buyer E would pay only $50, so does not.", s: { a: 1, b: 1 } },
  { cap: "<b>Surplus.</b> A gains $30, B $20, C $10 and D nothing (the marginal buyer): consumer surplus is <b>$60</b>.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, e = sdEq(d, s), di = 90 + 0.8 * d, si = 10 - 0.8 * s, cs = 0.5 * e.q * (di - e.p), ps = 0.5 * e.q * (e.p - si), base = 0.5 * 50 * 40;
  $("#r1").textContent = Lib.fmtN(cs, 0); $("#r2").textContent = Lib.fmtN(ps, 0); $("#r3").textContent = Lib.fmtN(cs + ps, 0);
  $("#rv").textContent = d === 0 && s === 0 ? "In the starting equilibrium (price $50, quantity 50) consumer and producer surplus are each 1,000 and the total is 2,000." : `At the new equilibrium (price $${Lib.fmtN(e.p, 0)}, quantity ${Lib.fmtN(e.q, 0)}) consumer surplus is ${Lib.fmtN(cs, 0)} (${cs > base ? "up" : "down"} from 1,000) and producer surplus is ${Lib.fmtN(ps, 0)} (${ps > base ? "up" : "down"} from 1,000). ${d > 0 ? "More demand raises both surpluses. " : ""}${s > 0 ? "More supply lowers the price, raising consumer surplus. " : ""}${d < 0 ? "Less demand lowers both surpluses. " : ""}${s < 0 ? "Less supply raises the price, lowering consumer surplus. " : ""}`;
  let o = sdPlot({ d, s, g: 0, n: 1 }) + poly([[0, di], [0, e.p], [e.q, e.p]], "f3", 0.5) + poly([[0, si], [0, e.p], [e.q, e.p]], "f2", 0.5) + SV.circle(SDX(e.q), SDY(e.p), 5, "dot3");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dd", label: "Demand shift (negative = left, positive = right) ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "ss", label: "Supply shift (negative = left, positive = right) ", min: -20, max: 10, step: 5, value: 0, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!$("#pf")) return;
  const p = +$("#pf").value, up = p > 50, Q = up ? (90 - p) / 0.8 : (p - 10) / 0.8, cs = up ? 0.5 * Q * (90 - p) : 90 * Q - 0.4 * Q * Q - p * Q, ps = up ? p * Q - (10 * Q + 0.4 * Q * Q) : 0.5 * Q * (p - 10), loss = 2000 - cs - ps;
  $("#t1").textContent = Lib.fmtN(cs, 0); $("#t2").textContent = Lib.fmtN(ps, 0); $("#t3").textContent = Lib.fmtN(Math.max(0, loss), 0);
  $("#tv").textContent = p === 50 ? "At the equilibrium price of $50, 50 units are traded and total surplus is at its maximum of 2,000." : `At $${p} only ${Lib.fmtN(Q, 0)} units are traded because ${up ? "buyers will not buy more at this high price" : "firms will not supply more at this low price"}. Consumer surplus is ${Lib.fmtN(cs, 0)} and producer surplus ${Lib.fmtN(ps, 0)}, so ${Lib.fmtN(loss, 0)} of total surplus is lost (the welfare loss).`;
  const pts = up ? [[[0, 90], [0, p], [Q, p]], [[0, 10], [0, p], [Q, p], [Q, 10 + 0.8 * Q]]] : [[[0, 90], [0, p], [Q, p], [Q, 90 - 0.8 * Q]], [[0, 10], [0, p], [Q, p]]];
  $("#labB").innerHTML = sdPlot({ d: 0, s: 0, g: 0 }) + poly(pts[0], "f3", 0.5) + poly(pts[1], "f2", 0.5) + SV.line(70, SDY(p), SDX(Math.max(Q, 50)), SDY(p), "c4", { "stroke-width": 2.5 }) + tag(SDX(Math.max(Q, 50)) + 6, SDY(p) + 4, "$" + p, "c4");
}
Lib.slider($("#g3"), { id: "pf", label: "Fixed price, $ ", min: 20, max: 80, step: 5, value: 50, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which surplus is it?", ["Consumer surplus", "Producer surplus", "Neither"],
  [("A shopper would pay $80 but pays $50", 0), ("A farmer would accept $3 but sells at $5", 1), ("The total revenue of a firm", 2), ("The area below demand and above the price", 0), ("The area above supply and below the price", 1), ("A firm's profit after all costs", 2), ("Passengers who gain when airfares fall", 0), ("Sellers who gain when the market price rises", 1)],
  "Consumers gain below demand and above the price. Producers gain above supply and below the price. Revenue and profit are not surpluses.") + MATCH([
  ["Consumer surplus", "Willingness to pay minus price paid"],
  ["Producer surplus", "Price received minus the minimum acceptable price"],
  ["Total surplus", "Consumer plus producer surplus"],
  ["Welfare loss", "Total surplus lost when output is below the equilibrium"],
  ["Marginal buyer", "The last buyer, whose surplus is zero"],
  ["Equilibrium", "Where total surplus is greatest in a competitive market"]]) + ORDER(
  "Put the steps of drawing the surplus diagram in order.",
  ["Draw and label the axes, demand and supply", "Mark the equilibrium price and quantity", "Draw a horizontal line at the market price", "Shade the triangle below demand and above the price", "Shade the triangle above supply and below the price"],
  "Consumer surplus is above the price line; producer surplus is below it.") + CALC([
  {"q": "Demand: P = 100 − 2Q. Supply: P = 10 + Q. What is the equilibrium quantity?", "a": 30, "unit": "units", "tol": 0.5, "hint": "100 − 2Q = 10 + Q.", "sol": "90 = 3Q, so Q = <b>30</b> and P = $40."},
  {"q": "Using the same curves, what is the consumer surplus? (½ × Q × (100 − P))", "a": 900, "unit": "$", "tol": 1, "hint": "½ × 30 × 60.", "sol": "<b>$900</b>."},
  {"q": "What is the producer surplus? (½ × Q × (P − 10))", "a": 450, "unit": "$", "tol": 1, "hint": "½ × 30 × 30.", "sol": "<b>$450</b>."},
  {"q": "A buyer would pay up to $75 and pays $52. What is that buyer's consumer surplus?", "a": 23, "unit": "$", "tol": 0.5, "hint": "75 − 52.", "sol": "<b>$23</b>."}]) + MCQ([
  ("Consumer surplus is the area:", ["Below demand and above the price", "Above demand and below the price", "Below supply and above the price", "Under the supply curve"], 0, "Willingness to pay minus price."),
  ("A fall in price will usually:", ["Raise consumer surplus", "Lower consumer surplus", "Raise producer surplus for the same quantity", "Not change either"], 0, "Buyers pay less than before."),
  ("Producer surplus is:", ["Price received minus the minimum price producers would accept", "Total revenue", "Profit", "Price paid minus willingness to pay"], 0, "Above supply, below price."),
  ("Total surplus is greatest:", ["At the equilibrium", "When price is fixed above equilibrium", "When price is fixed below equilibrium", "When the government sets price"], 0, "Allocative efficiency."),
  ("Which would reduce consumer surplus?", ["A leftward shift of supply", "A rightward shift of supply", "A subsidy to producers", "A fall in costs"], 0, "Price rises and quantity falls.")
], "qz1") + CARDS([
  ("Consumer surplus", "Willing to pay − price paid."),
  ("Producer surplus", "Price received − willing to accept."),
  ("CS area", "Below demand, above price."),
  ("PS area", "Above supply, below price."),
  ("Total surplus", "CS + PS."),
  ("Max at", "Equilibrium."),
  ("Price up", "CS down, PS up."),
  ("Elasticity", "Decides the size of the change.")]) + MCQ(mc_exam)

build("as26", "as-consumer-producer-surplus", "Consumer and Producer Surplus", EY,
  "2.5.1 to 2.5.2: the meaning and significance of consumer surplus and producer surplus, shown on supply and demand diagrams. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
