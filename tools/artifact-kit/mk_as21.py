"""AS syllabus 2.1.1-2.1.4 Demand and supply: effective demand, individual vs market, determinants. Run: python3 tools/artifact-kit/mk_as21.py"""
from asx import *
EY = EYAS("2.1.1 to 2.1.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Effective demand</b> is the quantity people are <b>willing and able</b> to buy at each price, so a want with no money behind it is not effective demand. <b>Individual demand</b> is one consumer's demand; <b>market demand</b> is the <b>horizontal sum</b> of all the individual demand curves, and the same is true of supply. Demand slopes downward because a lower price makes people <b>able and willing to buy more</b> (income and substitution effects), and supply slopes upward because a higher price makes extra output <b>more profitable</b> and covers rising costs. A change in the <b>price of the good itself</b> moves along the curve, while a change in any other <b>determinant</b> shifts the curve.</p></div>

  <h2>1 · Effective demand (2.1.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Wants and needs are not demand.</b> A student wants a sports car, but without the income to buy it there is no effective demand.</li>
    <li>Demand needs <b>willingness</b> (the preference) <b>and ability to pay</b> (income, savings or credit), at a given price and in a given time period.</li>
    <li>A <b>demand curve</b> shows the quantity demanded at each price, <b>ceteris paribus</b> (other things equal). It slopes down: the <b>law of demand</b>.</li>
  </ul>

  <h2>2 · Individual and market demand and supply (2.1.2)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Market demand</b> = the sum of everyone's quantity demanded <b>at each price</b>, which is a <b>horizontal addition</b> of individual curves.</li>
    <li><b>Market supply</b> = the sum of all firms' quantities supplied at each price.</li>
    <li>More buyers (or firms) shift the market curve to the right, but do not change an individual's curve.</li>
    <li>Some factors affect an individual curve more than the market curve, for example a change in one person's tastes or income.</li>
  </ul>

  <h2>3 · Determinants of demand (2.1.3)</h2>
  <div class="tw"><table class="t">
    <tr><th>Determinant</th><th>Effect on demand</th></tr>
    <tr><td><b>Price of the good</b></td><td>Movement along the curve (not a shift)</td></tr>
    <tr><td><b>Income</b></td><td>Normal good: income up, demand up. Inferior good: income up, demand down</td></tr>
    <tr><td><b>Price of substitutes</b></td><td>Substitute price up, demand for this good up</td></tr>
    <tr><td><b>Price of complements</b></td><td>Complement price up, demand for this good down</td></tr>
    <tr><td><b>Tastes, fashion, advertising</b></td><td>Favourable change shifts demand to the right</td></tr>
    <tr><td><b>Population and its age structure</b></td><td>More buyers raise market demand</td></tr>
    <tr><td><b>Expectations</b></td><td>Expected price rise tomorrow raises demand today</td></tr>
    <tr><td><b>Interest rates and credit</b></td><td>Cheaper credit raises demand for goods bought on credit</td></tr>
    <tr><td><b>Government policy and seasons</b></td><td>Taxes on income, restrictions, seasonal patterns</td></tr>
  </table></div>

  <h2>4 · Determinants of supply (2.1.4)</h2>
  <div class="tw"><table class="t">
    <tr><th>Determinant</th><th>Effect on supply</th></tr>
    <tr><td><b>Price of the good</b></td><td>Movement along the curve</td></tr>
    <tr><td><b>Costs of production</b> (wages, materials, energy, rent)</td><td>Lower costs shift supply to the right</td></tr>
    <tr><td><b>Technology and productivity</b></td><td>Better methods lower unit cost, supply rises</td></tr>
    <tr><td><b>Indirect taxes and subsidies</b></td><td>Tax raises costs (left); subsidy lowers them (right)</td></tr>
    <tr><td><b>Number of firms</b></td><td>More firms shift market supply to the right</td></tr>
    <tr><td><b>Weather and natural events</b></td><td>Especially for agricultural goods</td></tr>
    <tr><td><b>Prices of other goods</b></td><td>Firms switch to more profitable goods; joint supply by-products</td></tr>
    <tr><td><b>Expectations and regulation</b></td><td>Expected higher prices may hold back supply; rules raise or lower costs</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Say what the determinant does to <b>cost</b> or <b>willingness and ability to pay</b>, then name the <b>direction of the shift</b>. Do not list factors without explaining the link.</div>
'''

watch = '''
  <h2>1 · Willing and able</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stE"></div>
  <h2>2 · Adding individual demand curves</h2>
  <div id="stH"></div>
'''

explore = '''
  <h2>Lab 1 · What shifts demand?</h2>
  <p>A good such as coffee. Change the determinants and see how the demand curve moves and what happens to the equilibrium price and quantity (supply unchanged).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Demand shift</small><strong id="r1"></strong></div><div><small>New price</small><strong id="r2"></strong></div><div><small>New quantity</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with the demand curve shifted by the chosen determinants"></svg></div></div></div>

  <h2>Lab 2 · What shifts supply?</h2>
  <p>Change costs, technology and the government's tax or subsidy to see how supply moves.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Supply shift</small><strong id="t1"></strong></div><div><small>New price</small><strong id="t2"></strong></div><div><small>New quantity</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with the supply curve shifted by the chosen determinants"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which way does demand shift?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put market demand in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A student and a sports car", "A student wants a luxury car but cannot afford one, so adds nothing to market demand. When the student gets a well-paid job, the want becomes effective demand. The wish was always there; the ability to pay arrived.", "effective demand needs willingness and ability to pay.") +
rw("Coffee prices and tea", "A poor coffee harvest raises coffee prices. Many drinkers switch to tea, so demand for tea shifts to the right, while demand for coffee mugs and filter paper (complements) may fall.", "substitutes, complements and the difference between a movement and a shift.") +
rw("Solar panels", "Better technology and economies of scale have cut the cost of making solar panels. Supply shifts to the right, the price falls and the quantity sold rises. Government subsidies in some countries have pushed supply further.", "technology and subsidies shifting the supply curve.") +
rw("Drought and wheat", "A drought cuts the wheat harvest, so supply shifts to the left and the price rises. Farmers who expect higher prices next year may store grain, which can reduce supply further.", "weather as a supply determinant and the role of expectations.")
)

mc_exam = [
  mcq("m24_12", 6, "What is the definition of effective demand?", ["demand that is speculative", "demand that is supported by the ability to pay", "the relationship between price and quantity demanded", "the total amount demanded by consumers"], 1, "Effective demand needs willingness and ability to pay."),
  mcq("s21_12", 12, "How would an economist establish the market demand curve for a private good?", ["by adding consumer surplus to total expenditure", "by combining individual demand curves horizontally", "by combining the price elasticity of individual demands", "by multiplying price by quantity demanded"], 1, "Market demand is found by summing quantities horizontally at each price."),
  mcq("s20_11", 5, "What describes a market supply curve?", ["It is downward sloping", "It is the same as the aggregate supply curve", "It is the sum of all firms' supply curves for a product", "It is the supply of all products within an economy"], 2, "Market supply sums the supply of all firms for one product. Aggregate supply covers the whole economy."),
  mcq("m25_12", 9, "What is likely to have a greater effect on an individual demand curve than on a market demand curve?", ["changing weather patterns", "government policy to promote consumption", "growth in population", "more expensive substitutes"], 3, "An individual's demand responds strongly to relative prices of substitutes, while weather, policy and population act on the market as a whole."),
  mcq("w20_11", 13, "What is correct about market supply?", ["Market supply can increase only when all individual firms increase their output", "Market supply is effective when consumers have sufficient income to buy the good", "Market supply is the result of aggregating the supply of all individual firms", "Market supply of an inferior good falls as price increases"], 2, "Market supply is the sum of firms' supplies. More firms entering can raise it too."),
  mcq("s24_13", 10, "What most accurately describes a market supply curve?", ["supply at different income levels, assuming product prices remain unchanged", "supply at different levels of factor prices, assuming product prices remain unchanged", "supply at different prices, assuming no changes in technology", "supply at different time periods, assuming no changes in technology"], 2, "A supply curve relates price to quantity supplied, ceteris paribus, including technology."),
  mcq("w24_11", 9, "What is not held constant when aggregating individual firms' supply curves to give the short-run market supply curve?", ["the number of firms in the industry", "the price of the product", "the prices of factors of production", "the state of technology"], 1, "Price is the variable on the vertical axis, so it changes along the curve."),
  mcq("s23_11", 13, "Demand for medical face masks exceeds supply during a disease outbreak. What is the most likely cause of this excess demand?", ["Some consumers do not have effective demand", "The demand for medical face masks is price inelastic in the short run", "The price of medical face masks is fixed below the equilibrium price", "The supply of medical face masks is inelastic in the short run"], 2, "Excess demand at a fixed price below equilibrium creates a shortage."),
  mcq("m20_12", 8, "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X?", ["Good X an inferior good, good Y a complement", "Good X an inferior good, good Y a substitute", "Good X a normal good, good Y a complement", "Good X a normal good, good Y a substitute"], 2, "Rising income raises demand for a normal good. A fall in the price of a complement also raises demand for X."),
  mcq("s24_12", 9, "In Asia, instant noodles is an inferior good because dried fruit is a better quality substitute. What could have caused demand for instant noodles to shift to the right?", ["a fall in the price of dried fruit", "a rise in real income", "a rise in unemployment", "a successful advertising campaign by dried fruit producers"], 2, "A rise in unemployment lowers incomes, which raises demand for an inferior good."),
  mcq("s21_11", 5, "What could explain a shift of an upward-sloping supply curve to the right?", ["an increase in firms' unit labour costs", "an increase in the number of firms in the industry", "an increase in the price of the good", "an indirect tax imposed on the good"], 1, "More firms raise supply at every price. A rise in price is a movement along."),
  mcq("s24_12", 11, "Which reason for the increase in demand for a smartphone is an example of joint demand?", ["a fall in its price", "a fall in the price of connecting to a network", "a fall in the price of parts used to make smartphones", "a rise in the price of a substitute"], 1, "Network connection is a complement, so a fall in its price raises demand for the phone.")
]

exam = exam_page("demand and supply curves and their determinants",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Determinants of demand and supply appear in nearly every Paper 1 and often as the first marks of an 8 mark Paper 2 part. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "May/June 2025 (22) Q3(a); Feb/March 2020 (22) Q2(a)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("s25_22", "3(a)"), "8 marks", "Explain three reasons, associated with costs of production, why the supply curve for a particular market may shift to the right and consider the extent to which government microeconomic policy may also shift the supply curve for that market to the right.",
     ["Knowledge (up to 3): three explanations, such as a fall in wage rates, an increase in worker productivity, a fall in raw material costs, a fall in distribution costs or improved technology, each explaining why the supply curve shifts to the right (1 each).",
      "Analysis (up to 3): government policy targeted at the market, such as subsidies, indirect taxes, price controls, regulation, provision of information or buffer stocks; at least one analysed for how it may shift supply to the right (for example a subsidy to education providers).",
      "Evaluation (up to 2): the extent depends on the size of the subsidy, how firms respond and other factors."],
     "Three cost reasons, each linked to a right shift. Then a policy such as a subsidy, with its limits.",
     [[("k", "Supply could shift to the right if wage rates fall, because unit costs fall and firms are willing to supply more at each price. Greater worker productivity has a similar effect, since output per worker rises. A fall in raw material prices also lowers costs, so firms supply more at every price.")], [("n", "Government policy might also shift supply to the right. A subsidy for each unit lowers the producer's cost, so the supply curve moves to the right by the amount of the subsidy. A government could also reduce regulation or provide training grants.")], [("e", "However, the extent depends on the size of the subsidy and on whether firms pass the lower costs into more output, and a tax on the same market would work in the opposite direction.")]]),
  eq(P("m20_22", "2(a)"), "8 marks", "Explain what determines the change in equilibrium price and equilibrium quantity of a good when there is a rise in incomes in an economy.",
     ["Knowledge (up to 2): income elasticity of demand (1) and how it is measured (1).",
      "Application (up to 6): impact on equilibrium price and quantity for a normal good (2), a necessity (2) and an inferior good (2)."],
     "Income elasticity of demand decides the shift. Normal: right, price and quantity up. Necessity: small shift. Inferior: left.",
     [[("k", "Income elasticity of demand measures the responsiveness of demand to a change in income, as the percentage change in quantity demanded divided by the percentage change in income.")], [("n", "For a normal good, income elasticity is positive, so demand shifts to the right and both equilibrium price and quantity rise. For a necessity, the elasticity is positive but below one, so demand rises only a little and price and quantity increase slightly. For an inferior good, the elasticity is negative, so demand shifts to the left and both equilibrium price and quantity fall.")]])
  ],
  )

tips = tips_html(
  [("Effective demand needs money.", "Willing and able. A want alone is not demand."),
   ("Market curve = horizontal sum.", "Add quantities at each price."),
   ("Price of the good moves along.", "Every other determinant shifts the curve."),
   ("Link every factor to cost or income.", "Say why the curve shifts, then which way."),
   ("Name normal and inferior.", "Rising income can lower demand for inferior goods."),
   ("Substitute up, complement down.", "A rise in a substitute's price raises demand for this good."),
   ("Supply shifts with costs.", "Lower costs, technology, subsidies and more firms shift supply right.")],
  [("Effective demand", "Effective demand is willingness backed by ability to pay."),
   ("Market demand", "Market demand is the horizontal sum of individual demand curves."),
   ("Determinant", "A change in income could shift the demand curve to the right for a normal good."),
   ("Supply", "A fall in costs may shift the supply curve to the right."),
   ("Expectation", "An expected price rise may raise current demand.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- effective demand venn ---------- */
function evDraw(s) {
  let o = SV.circle(290, 160, 110, "dot1", op(0.3 * s.a)) + SV.circle(470, 160, 110, "dot3", op(0.3 * s.b));
  o += SV.text(220, 150, "Willing", "lbl bd", { "text-anchor": "middle", ...op(s.a) }) + SV.text(220, 172, "(wants it)", "sm", { "text-anchor": "middle", ...op(s.a) });
  o += SV.text(540, 150, "Able to pay", "lbl bd", { "text-anchor": "middle", ...op(s.b) }) + SV.text(540, 172, "(income, savings)", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.c > 0) o += SV.text(380, 150, "EFFECTIVE", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.c) }) + SV.text(380, 172, "DEMAND", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.c) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Willingness and ability to pay overlap as effective demand">${evDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Effective demand is where willingness and ability to pay overlap", base: { a: 0, b: 0, c: 0 }, draw: evDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Willingness.</b> Many people would like a good. A want or a need alone is not demand.", s: { a: 1 } },
  { cap: "<b>Ability to pay.</b> Some people have the income or credit to buy at the price, whether or not they want the good.", s: { a: 1, b: 1 } },
  { cap: "<b>The overlap</b> is effective demand: people who both want the good and can pay for it at that price.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- horizontal sum ---------- */
const hx = (q) => 70 + q * 12, hy = (p) => 270 - p * 2.4;
function hsDraw(s) {
  let o = axes(70, 270, 700, 25, "Quantity", "Price ($)");
  const ln = (k, c, v, lab) => SV.line(hx(0), hy(100), hx(k), hy(0), c, { "stroke-width": 3, ...op(v) }) + tag(hx(k) + 4, hy(0) - 6, lab, c, v);
  o += ln(20, "c1", s.a, "A") + ln(30, "c3", s.b, "B") + ln(50, "c2", s.m, "Market");
  if (s.m > 0.2) { const pr = 40, qa = 20 - 0.2 * pr, qb = 30 - 0.3 * pr; o += SV.line(70, hy(pr), hx(qa + qb), hy(pr), "dash", op(s.m)) + SV.text(62, hy(pr) + 4, "$40", "sm", { "text-anchor": "end", ...op(s.m) }) + tag(hx(qa / 2), hy(pr) - 6, "A " + qa, "c1", s.m, "middle") + tag(hx(qa + qb / 2), hy(pr) - 6, "B " + qb, "c3", s.m, "middle") + tag(hx(qa + qb) + 4, hy(pr) + 4, "= " + (qa + qb), "c2", s.m); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Two individual demand curves added horizontally to give market demand">${hsDraw({ a: 1, b: 1, m: 1 })}</svg>`;
Lib.stepper($("#stH"), { w: 760, h: 300, label: "Two individual demand curves added horizontally", base: { a: 0, b: 0, m: 0 }, draw: hsDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Consumer A</b> demands 12 units at a price of $40.", s: { a: 1 } },
  { cap: "<b>Consumer B</b> demands 18 units at $40.", s: { a: 1, b: 1 } },
  { cap: "<b>Market demand</b> adds the quantities at each price: 12 + 18 = 30 at $40. The curve is the <b>horizontal sum</b>, not a vertical one.", s: { a: 1, b: 1, m: 1 } },
] });

/* ---------- Lab 1: demand determinants ---------- */
function labD() {
  if (!$("#inc") || !$("#sub") || !$("#cmp") || !$("#tst")) return;
  const raw = 0.9 * +$("#inc").value + 0.6 * +$("#sub").value - 0.6 * +$("#cmp").value + 0.8 * +$("#tst").value, d = Math.max(-30, Math.min(30, raw)), e = sdEq(d, 0), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(d) < 0.5 ? "None" : d > 0 ? "Right" : "Left"; $("#r2").textContent = "$" + Lib.fmtN(e.p, 0); $("#r3").textContent = Lib.fmtN(e.q, 0);
  $("#rv").textContent = Math.abs(d) < 0.5 ? "No determinant has changed, so demand and the equilibrium stay at $50 and 50 units." : `${d > 0 ? "A rise" : "A fall"} in demand shifts the curve to the ${d > 0 ? "right" : "left"}: the equilibrium price ${e.p > e0.p ? "rises" : "falls"} from $50 to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 0)}. A change in the price of the good itself would be a movement along a curve, not a shift.`;
  $("#labA").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "inc", label: "Change in consumers' income, % (normal good) ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g2"), { id: "sub", label: "Change in price of a substitute, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g3"), { id: "cmp", label: "Change in price of a complement, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "tst", label: "Change in tastes (advertising, fashion), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Lab 2: supply determinants ---------- */
function labS() {
  if (!$("#cst") || !$("#tch") || !$("#tax")) return;
  const raw = -0.9 * +$("#cst").value + 0.9 * +$("#tch").value - 0.9 * +$("#tax").value, s = Math.max(-30, Math.min(30, raw)), e = sdEq(0, s), e0 = sdEq(0, 0);
  $("#t1").textContent = Math.abs(s) < 0.5 ? "None" : s > 0 ? "Right" : "Left"; $("#t2").textContent = "$" + Lib.fmtN(e.p, 0); $("#t3").textContent = Lib.fmtN(e.q, 0);
  $("#tv").textContent = Math.abs(s) < 0.5 ? "Costs, technology and taxes are unchanged, so supply does not shift." : `${s > 0 ? "Lower costs, better technology or a subsidy" : "Higher costs or a tax"} shift supply to the ${s > 0 ? "right" : "left"}. The equilibrium price ${e.p > e0.p ? "rises" : "falls"} to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 0)}.`;
  $("#labB").innerHTML = sdPlot({ d: 0, s, g: 1, n: 1 });
}
Lib.slider($("#g5"), { id: "cst", label: "Change in costs (wages, materials), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g6"), { id: "tch", label: "Improvement in technology, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g7"), { id: "tax", label: "Indirect tax (positive) or subsidy (negative), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to demand for coffee?", ["Shifts right", "Shifts left", "Movement along the curve"],
  [("Income rises (coffee is a normal good)", 0), ("Price of tea (a substitute) falls", 1), ("The price of coffee falls", 2), ("Consumers expect coffee prices to rise next month", 0), ("A successful advertising campaign for coffee", 0), ("Price of milk (a complement) rises", 1), ("Population grows", 0), ("The price of coffee rises", 2)],
  "Only the price of coffee itself causes a movement along the curve. Every other determinant shifts it.") + MATCH([
  ["Effective demand", "Willingness backed by ability to pay"],
  ["Market demand", "Horizontal sum of individual demand"],
  ["Substitute", "A rise in its price raises demand for this good"],
  ["Complement", "A rise in its price lowers demand for this good"],
  ["Normal good", "Demand rises as income rises"],
  ["Inferior good", "Demand falls as income rises"]]) + ORDER(
  "Put the steps of finding market demand in order.",
  ["Choose a price", "Read each individual's quantity demanded at that price", "Add the quantities together", "Plot the total against that price", "Repeat for other prices and join the points"],
  "Add quantities horizontally at each price.") + CALC([
  {"q": "At a price of $5, three consumers demand 8, 12 and 20 units. What is market demand?", "a": 40, "unit": "units", "tol": 0.5, "hint": "Add the quantities.", "sol": "8 + 12 + 20 = <b>40 units</b>."},
  {"q": "Market demand is Qd = 500 − 20P. What quantity is demanded at P = 10?", "a": 300, "unit": "units", "tol": 1, "hint": "500 − 200.", "sol": "<b>300</b>."},
  {"q": "At P = 15, using the same demand function, what is the quantity demanded?", "a": 200, "unit": "units", "tol": 1, "hint": "500 − 300.", "sol": "<b>200</b>."},
  {"q": "Market supply is Qs = 20P − 100. What quantity is supplied at P = 15?", "a": 200, "unit": "units", "tol": 1, "hint": "300 − 100.", "sol": "<b>200</b>, so at $15 the market clears."}]) + MCQ([
  ("Effective demand requires:", ["Willingness and ability to pay", "Only a need for the good", "A fall in price", "Government support"], 0, "Both willingness and ability to pay."),
  ("Market demand is found by:", ["Adding quantities at each price", "Adding prices at each quantity", "Multiplying individual demands", "Averaging the demand curves"], 0, "Horizontal summation."),
  ("A fall in the price of a complement will:", ["Shift demand for the good to the right", "Shift demand for the good to the left", "Cause a movement along the demand curve", "Shift supply to the right"], 0, "Cheaper complement raises demand for this good."),
  ("Which change will shift the supply curve to the right?", ["A fall in raw material costs", "A rise in the price of the good", "A rise in the wage rate", "An indirect tax on the good"], 0, "Lower costs raise supply at every price."),
  ("A rise in the price of a good causes:", ["A movement along the demand curve", "A shift of the demand curve to the left", "A shift of supply to the right", "A rise in income"], 0, "Price changes cause movements.")
], "qz1") + CARDS([
  ("Effective demand", "Willing and able to pay."),
  ("Market demand", "Horizontal sum."),
  ("Normal good", "Income up, demand up."),
  ("Inferior good", "Income up, demand down."),
  ("Substitute", "Its price up, demand up."),
  ("Complement", "Its price up, demand down."),
  ("Cost fall", "Supply shifts right."),
  ("Price of the good", "Movement along, not a shift.")]) + MCQ(mc_exam)

build("as21", "as-demand-supply-curves", "Demand and Supply Curves and Their Determinants", EY,
  "2.1.1 to 2.1.4: effective demand, individual and market demand and supply, and the determinants of each. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
