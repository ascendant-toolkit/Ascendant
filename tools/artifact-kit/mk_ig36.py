"""Builds the five IGCSE Economics 3.6 Firms' costs, revenue and objectives reviews (3.6.1 to 3.6.5). Run: python3 tools/artifact-kit/mk_ig36.py"""
from igtext import *

# ---------------------------------------------------------------- 3.6.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Firms face <b>costs</b> of production. <b>Fixed costs</b> do not change with output; <b>variable costs</b> do. Adding them gives <b>total cost</b>. Dividing each by output gives the <b>average</b> (per unit) costs. Know all six definitions exactly.</p></div>

  <h2>The six cost measures</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Definition</th><th>Formula</th><th>Example</th></tr>
    <tr><td><b>Fixed cost (FC)</b></td><td>Costs that do not change with output in the short run</td><td>—</td><td>Rent, insurance, salaries, loan interest</td></tr>
    <tr><td><b>Variable cost (VC)</b></td><td>Costs that change directly with output</td><td>—</td><td>Raw materials, wages of production workers, energy used</td></tr>
    <tr><td><b>Total cost (TC)</b></td><td>All the costs of producing a given output</td><td>TC = FC + VC</td><td>$100 + $200 = $300</td></tr>
    <tr><td><b>Average fixed cost (AFC)</b></td><td>Fixed cost per unit of output</td><td>AFC = FC ÷ output</td><td>$100 ÷ 50 = $2</td></tr>
    <tr><td><b>Average variable cost (AVC)</b></td><td>Variable cost per unit of output</td><td>AVC = VC ÷ output</td><td>$200 ÷ 50 = $4</td></tr>
    <tr><td><b>Average total cost (ATC)</b></td><td>Total cost per unit of output</td><td>ATC = TC ÷ output = AFC + AVC</td><td>$300 ÷ 50 = $6</td></tr>
  </table></div>
  <ul>
    <li><b>Fixed costs</b> have to be paid even when output is zero; they are only fixed in the <b>short run</b>.</li>
    <li><b>AFC always falls</b> as output rises (fixed cost is spread over more units).</li>
    <li><b>AVC</b> usually falls and then rises (diminishing returns).</li>
    <li><b>ATC</b> is the sum of the two, so it is U-shaped.</li>
  </ul>
  <p class="note">Costs can be paid in cash (explicit) or be the value of owner-supplied resources. Always match a cost to its type with an example from the question.</p>
'''
steppers = [
  ("Fixed and variable costs", "--accent", ["A bakery pays rent of $100 a day whatever it bakes", "It also pays $2 of flour and energy per loaf", "Rent is a fixed cost; flour is a variable cost", "TC = FC + VC", "Total cost rises as output rises"]),
  ("Why AFC falls with output", "--good", ["Fixed cost is $100", "At 10 units, AFC = $10", "At 50 units, AFC = $2", "At 100 units, AFC = $1", "Fixed cost is spread over more units"]),
]
lab1 = dict(title="Cost calculator", intro="Set fixed cost, variable cost per unit and output. See all six cost measures.", rl=["Total cost", "ATC", "AFC + AVC"],
  sliders=[("Fixed cost ($)", 0, 500, 50, 100, "'$' + v"), ("Variable cost per unit ($)", 1, 20, 1, 4, "'$' + v"), ("Output (units)", 10, 200, 10, 50, "v")],
  fn="const vc = v[1] * v[2], tc = v[0] + vc, atc = tc / v[2], afc = v[0] / v[2], avc = vc / v[2]; return { r: ['$' + tc, '$' + atc.toFixed(2), '$' + afc.toFixed(2) + ' + $' + avc.toFixed(2)], t: 'FC = $' + v[0] + '; VC = $' + v[1] + ' × ' + v[2] + ' = $' + vc + '; TC = $' + tc + '. AFC = ' + v[0] + ' ÷ ' + v[2] + ' = $' + afc.toFixed(2) + '; AVC = $' + avc.toFixed(2) + '; ATC = ' + tc + ' ÷ ' + v[2] + ' = $' + atc.toFixed(2) + ' (which equals AFC + AVC). Raise output and AFC falls while AVC stays the same here.', bars: [['AFC', afc, '--warn', '$' + afc.toFixed(2)], ['AVC', avc, '--accent', '$' + avc.toFixed(2)], ['ATC', atc, '--good', '$' + atc.toFixed(2)]] };")
lab2 = dict(title="Fixed or variable?", intro="Pick a cost to see whether it is fixed or variable.", h1="Type", h2="Why",
  items=[("Factory rent", "Fixed", "Same whatever the output."), ("Raw materials", "Variable", "Rises with output."), ("Manager's salary", "Fixed", "Paid regardless of output."), ("Piece-rate wages", "Variable", "Linked to output."), ("Electricity for machines", "Variable", "More output, more power."), ("Loan interest", "Fixed", "Does not change with output.")])
cl = [("Is each a <b>fixed</b> or <b>variable</b> cost?", ["Fixed cost", "Variable cost"], [("Rent", 0), ("Insurance", 0), ("Manager's salary", 0), ("Raw materials", 1), ("Packaging", 1), ("Wages paid per item made", 1)], "Does it change with output?"),
      ("Which <b>cost measure</b> is each formula?", ["TC", "AFC", "AVC", "ATC"], [("FC + VC", 0), ("FC ÷ output", 1), ("VC ÷ output", 2), ("TC ÷ output", 3), ("AFC + AVC", 3)], "Learn the formulas.")]
match = [["Fixed cost", "Does not change with output"], ["Variable cost", "Changes with output"], ["Total cost", "FC + VC"], ["Average total cost", "TC ÷ output"], ["Average fixed cost", "FC ÷ output"], ["Average variable cost", "VC ÷ output"]]
order = ("Put the steps in order: <b>calculating ATC</b>.", ["Find fixed cost", "Find variable cost", "Add them to get total cost", "Divide total cost by output", "The result is average total cost"], "ATC = TC ÷ output.")
calcs = [("FC is $100 and VC is $200. What is TC ($)?", 300, "100 + 200 = <b>$300</b>.", None, None), ("TC is $300 and output is 50 units. What is ATC ($)?", 6, "300 ÷ 50 = <b>$6</b>.", None, None), ("FC is $100 and output is 50. What is AFC ($)?", 2, "100 ÷ 50 = <b>$2</b>.", None, None), ("VC is $200 and output is 50. What is AVC ($)?", 4, "200 ÷ 50 = <b>$4</b>.", None, None)]
mcq = [("Total cost is:", ["FC − VC", "FC + VC", "FC × VC", "VC ÷ FC"], 1, "Sum."), ("Which is a fixed cost?", ["Raw materials", "Rent", "Packaging", "Piece-rate pay"], 1, "Does not vary."), ("ATC equals:", ["TC ÷ output", "FC ÷ VC", "VC ÷ TC", "Output ÷ TC"], 0, "Per unit."), ("As output rises, AFC:", ["Rises", "Falls", "Stays constant", "Doubles"], 1, "Spread over more units."), ("ATC =", ["AFC + AVC", "AFC − AVC", "AFC × AVC", "AVC ÷ AFC"], 0, "Sum of averages.")]
cards = [("Fixed cost", "A cost that does not change with output."), ("Variable cost", "A cost that changes with output."), ("Total cost", "Fixed cost plus variable cost."), ("Average fixed cost", "Fixed cost divided by output."), ("Average variable cost", "Variable cost divided by output."), ("Average total cost", "Total cost divided by output."), ("Output", "The quantity produced."), ("Short run", "A period in which some costs are fixed."), ("Unit cost", "Cost per item.")]
exam_qs = [
  Q(1, "Define", 2, "Define fixed costs.", "Do not change with output.", "[K|Fixed costs are costs that do not change] [K|when output changes in the short run.]"),
  Q(2, "Define", 2, "Define average total cost.", "Total cost per unit.", "[K|Average total cost is total cost] [K|divided by the number of units produced.]"),
  Q(3, "Identify", 2, "Identify one fixed cost and one variable cost for a bakery.", "Rent; flour.", "[K|Fixed cost: rent of the bakery.] [K|Variable cost: flour.]"),
  Q(4, "Explain", 4, "Explain the difference between fixed and variable costs.", "Fixed constant; variable change with output.", "[K|Fixed costs do not change with output,] [N|for example rent has to be paid even if no goods are made.] [K|Variable costs change with output,] [N|for example more raw materials are needed when output rises.]"),
]
tips_ = [("Six definitions.", "FC, VC, TC, AFC, AVC, ATC."), ("Give a business example.", "Rent vs flour."), ("TC = FC + VC; ATC = TC ÷ Q.", "Memorise."), ("Fixed in the short run only.", "All costs vary in the long run.")]
real_items = [("Airlines", "Aircraft leases and airport fees are fixed; fuel and meals are variable.", "Fixed and variable costs."), ("Restaurants", "Rent is fixed; ingredients are variable.", "Cost types."), ("Software firms", "High fixed development costs, very low variable cost per copy.", "AFC falls as sales rise."), ("Car factories", "Big fixed costs for plant, variable costs for parts.", "Cost structure.")]
review("ig-costs-definitions", "k361", "3.6.1", "Definitions of Costs of Production", "Total, fixed, variable, average fixed, average variable and average total cost. Syllabus 3.6.1.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Identify", "Explain"], real_items)

# ---------------------------------------------------------------- 3.6.2
CJS = '''
const QS = [2, 3, 4, 5, 6, 7, 8, 9, 10], VCS = [50, 66, 80, 100, 126, 160, 204, 260, 330], FCc = 100;
const cx = (q) => 90 + q * 60, cy = (c) => 310 - c * 3;
const AFCf = (i) => FCc / QS[i], AVCf = (i) => VCS[i] / QS[i], ATCf = (i) => AFCf(i) + AVCf(i);
function costAxes() { return SV.line(cx(0), cy(0), cx(0), cy(80)) + SV.line(cx(0), cy(0), cx(11), cy(0)) + SV.text(cx(0) + 8, 14, "Cost per unit ($)", "sm") + SV.text(cx(11), cy(0) + 24, "Output (units)", "sm", { "text-anchor": "end" }); }
function costLine(fn, cls, lab, tcl) { let d = ""; QS.forEach((q, i) => d += (d ? "L" : "M") + cx(q).toFixed(1) + " " + cy(fn(i)).toFixed(1)); const li = QS.length - 1; return SV.path(d, cls) + SV.text(cx(QS[li]) + 6, cy(fn(li)) + 4, lab, "lbl bd " + tcl); }
function costDraw(show, sel) {
  let o = costAxes();
  if (show >= 1) o += costLine(AFCf, "c3", "AFC", "t3");
  if (show >= 2) o += costLine(AVCf, "c2", "AVC", "t2");
  if (show >= 3) o += costLine(ATCf, "c1", "ATC", "t1");
  if (sel !== undefined && sel >= 0) { const q = QS[sel]; o += SV.line(cx(q), cy(0), cx(q), cy(ATCf(sel)), "gr") + SV.circle(cx(q), cy(ATCf(sel)), 6, "dot2") + SV.circle(cx(q), cy(AVCf(sel)), 5, "dot1") + SV.circle(cx(q), cy(AFCf(sel)), 5, "dot3") + SV.text(cx(q), cy(0) + 18, q, "sm bd", { "text-anchor": "middle" }); }
  return o;
}
'''
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Costs are <b>calculated</b> from the definitions (TC = FC + VC; ATC = TC ÷ output) and shown on <b>diagrams</b>. As output rises, <b>AFC falls</b>, <b>AVC</b> falls then rises and <b>ATC</b> is U-shaped, because ATC = AFC + AVC. The U shape comes from <b>economies</b> then <b>diseconomies</b> of scale (and diminishing returns in the short run).</p></div>

  <h2>Worked example (fixed cost = $100)</h2>
  <div class="tw"><table class="t">
    <tr><th>Output</th><th>FC</th><th>VC</th><th>TC</th><th>AFC</th><th>AVC</th><th>ATC</th></tr>
    <tr><td>2</td><td>100</td><td>50</td><td>150</td><td>50.0</td><td>25.0</td><td>75.0</td></tr>
    <tr><td>4</td><td>100</td><td>80</td><td>180</td><td>25.0</td><td>20.0</td><td>45.0</td></tr>
    <tr class="hl"><td>6</td><td>100</td><td>126</td><td>226</td><td>16.7</td><td>21.0</td><td>37.7</td></tr>
    <tr><td>8</td><td>100</td><td>204</td><td>304</td><td>12.5</td><td>25.5</td><td>38.0</td></tr>
    <tr><td>10</td><td>100</td><td>330</td><td>430</td><td>10.0</td><td>33.0</td><td>43.0</td></tr>
  </table></div>
  <p>ATC is lowest (about $37.7) around 6 to 7 units: this is the most efficient output.</p>

  <h2>Diagrams of costs</h2>
  <ul>
    <li><b>AFC</b> slopes <b>downwards</b> all the way (a rectangular hyperbola).</li>
    <li><b>AVC</b> is <b>U-shaped</b>: falls with specialisation, then rises with diminishing returns.</li>
    <li><b>ATC</b> is <b>U-shaped</b> and lies above AVC; the gap between them is AFC, which shrinks as output rises.</li>
    <li>The <b>lowest ATC</b> is at the <b>minimum efficient scale</b>.</li>
  </ul>
  <p class="note">When reading a table, compute each average by dividing by output, and check that ATC = AFC + AVC.</p>
'''
steppers = [
  dict(title="Average cost curves", base="{ show: 0 }", draw="(s) => costDraw(s.show)", steps="""[
  { cap: "Output on the horizontal axis; cost per unit on the vertical axis.", s: { show: 0 } },
  { cap: "<b>AFC</b> always falls: fixed cost is spread over more units.", s: { show: 1 } },
  { cap: "<b>AVC</b> falls, then rises as diminishing returns set in: U-shaped.", s: { show: 2 } },
  { cap: "<b>ATC = AFC + AVC</b> is U-shaped. Its lowest point is the most efficient output.", s: { show: 3 } },
] """),
  ("From table to diagram", "--accent", ["Find FC and VC at each output", "Add to get TC", "Divide FC, VC and TC by output for AFC, AVC and ATC", "Plot each against output", "Join the points to draw the cost curves"]),
]
lab1 = dict(title="Costs at each output", intro="Move along the output scale to read each cost measure from the table and diagram.", rl=["TC", "ATC", "AFC / AVC"],
  sliders=[("Output (units, 2 to 10)", 2, 10, 1, 6, "v")],
  fn="const i = QS.indexOf(v[0]), tc = FCc + VCS[i], mn = ATCf(QS.indexOf(6)); return { r: ['$' + tc, '$' + ATCf(i).toFixed(1), '$' + AFCf(i).toFixed(1) + ' / $' + AVCf(i).toFixed(1)], t: 'At ' + v[0] + ' units: FC $' + FCc + ', VC $' + VCS[i] + ', TC $' + tc + '. AFC = ' + FCc + ' ÷ ' + v[0] + ' = $' + AFCf(i).toFixed(1) + '; AVC = ' + VCS[i] + ' ÷ ' + v[0] + ' = $' + AVCf(i).toFixed(1) + '; ATC = $' + ATCf(i).toFixed(1) + '. ' + (v[0] < 6 ? 'ATC is still falling: economies of scale.' : v[0] <= 7 ? 'This is near the lowest ATC.' : 'ATC is rising: diseconomies of scale.'), svg: costDraw(3, i) };")
lab2 = dict(title="Reading cost diagrams", intro="Pick a curve to see its shape and why.", h1="Shape", h2="Why",
  items=[("AFC", "Falls all the way", "Fixed cost spread over more units."), ("AVC", "U-shaped", "Specialisation, then diminishing returns."), ("ATC", "U-shaped", "ATC = AFC + AVC."), ("Gap between ATC and AVC", "Shrinks as output rises", "It equals AFC."), ("Lowest point of ATC", "Minimum efficient scale", "Lowest cost per unit."), ("Beyond the minimum", "ATC rises", "Diseconomies of scale.")])
cl = [("Does each cost <b>rise</b>, <b>fall</b> or have a <b>U shape</b> as output rises?", ["Falls", "U-shaped", "Rises"], [("Average fixed cost", 0), ("Average total cost", 1), ("Average variable cost", 1), ("Total cost", 2), ("Total variable cost", 2), ("Fixed cost per unit", 0)], "Shapes of cost curves."),
      ("Is each calculation <b>correct</b> or <b>incorrect</b> for FC $100, VC $50, output 10?", ["Correct", "Incorrect"], [("TC = $150", 0), ("AFC = $10", 0), ("AVC = $5", 0), ("ATC = $15", 0), ("ATC = $5", 1), ("AFC = $100", 1)], "Check each formula.")]
match = [["AFC curve", "Always falls as output rises"], ["AVC curve", "U-shaped"], ["ATC curve", "U-shaped; AFC + AVC"], ["Minimum efficient scale", "Output with the lowest ATC"], ["Diminishing returns", "Extra output costs more per unit"], ["Economies of scale", "Falling unit cost as output rises"]]
order = ("Put the chain in order: <b>why ATC is U-shaped</b>.", ["Output starts low", "AFC falls quickly and AVC falls: ATC falls", "Output reaches its efficient level: ATC is lowest", "Diminishing returns push AVC up", "ATC rises: a U shape"], "AFC + AVC.")
calcs = [("At output 6, VC is $126 and FC is $100. What is ATC (1 decimal place, $)?", 37.7, "226 ÷ 6 = <b>$37.7</b>.", None, None), ("At output 4, VC is $80. What is AVC ($)?", 20, "80 ÷ 4 = <b>$20</b>.", None, None), ("At output 10, TC is $430. What is ATC ($)?", 43, "430 ÷ 10 = <b>$43</b>.", None, None), ("AFC is $12.5 and AVC is $25.5. What is ATC ($)?", 38, "12.5 + 25.5 = <b>$38</b>.", None, None)]
mcq = [("The AFC curve:", ["Rises", "Falls throughout", "Is U-shaped", "Is flat"], 1, "Spread over more units."), ("ATC is:", ["Downward-sloping only", "U-shaped", "Upward-sloping only", "Vertical"], 1, "Falls then rises."), ("The gap between ATC and AVC is:", ["VC", "AFC", "FC", "TC"], 1, "ATC − AVC = AFC."), ("ATC rises at high output because of:", ["Economies of scale", "Diseconomies of scale", "Lower FC", "Subsidies"], 1, "Too big."), ("The lowest point of ATC is the:", ["Maximum output", "Minimum efficient scale", "Break-even only", "Highest profit"], 1, "Lowest unit cost.")]
cards = [("Average cost curves", "Curves showing AFC, AVC and ATC at each output."), ("Minimum efficient scale", "The output at which ATC is lowest."), ("Diminishing returns", "Each extra input adds less to output, raising marginal cost."), ("Economies of scale", "Falling unit cost with higher output."), ("Diseconomies of scale", "Rising unit cost with higher output."), ("U-shaped", "A curve that falls and then rises."), ("Rectangular hyperbola", "The shape of the AFC curve."), ("Marginal cost", "The cost of one more unit."), ("Efficiency", "Producing at the lowest unit cost.")]
exam_qs = [
  Q(1, "Calculate", 3, "A firm has fixed costs of $100 and variable costs of $126 when it makes 6 units. Calculate average total cost.", "TC ÷ output.", "[A|TC = 100 + 126 = $226.] [A|ATC = 226 ÷ 6] [A|= $37.67.]"),
  Q(2, "Explain", 4, "Explain why average fixed cost falls as output rises.", "Fixed cost spread over more units.", "[K|Fixed costs do not change with output.] [N|As output rises the same fixed cost is shared across more units,] [N|so fixed cost per unit falls.]"),
  Q(3, "Analyse", 6, "Analyse, using a diagram, why average total cost is U-shaped.", "AFC falls; AVC U-shaped; economies then diseconomies.", "[K|ATC is the sum of AFC and AVC.] [N|At low output both AFC and AVC fall, so ATC falls (economies of scale).] [N|At higher output diminishing returns raise AVC faster than AFC falls, so ATC rises (diseconomies of scale).] [E|The lowest ATC shows the most efficient output.]", key=True),
  Q(4, "Calculate", 3, "Complete the table: output 8, FC $100, VC $204. Calculate TC, AVC and ATC.", "Show each step.", "[A|TC = 100 + 204 = $304.] [A|AVC = 204 ÷ 8 = $25.5.] [A|ATC = 304 ÷ 8 = $38.]"),
]
tips_ = [("Show the formula.", "Then the working."), ("ATC = AFC + AVC.", "Use it to check."), ("Draw three curves.", "AFC down, AVC and ATC U-shaped."), ("ATC above AVC.", "The gap is AFC.")]
real_items = [("Airline seats", "Selling more seats spreads huge fixed costs over more passengers.", "AFC falls."), ("Car production", "Unit costs fall as a plant reaches full capacity, then rise if overcrowded.", "U-shaped ATC."), ("Bakery ovens", "More loaves make each loaf cheaper until the kitchen is crowded.", "Falling then rising ATC."), ("Software", "The first copy is costly; later copies cost almost nothing.", "Falling AFC.")]
review("ig-costs-calculation", "k362", "3.6.2", "Calculation of Costs of Production", "Calculating TC, ATC, FC, AFC, VC and AVC and drawing the cost curves. Syllabus 3.6.2.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Calculate", "Explain", "Analyse"], real_items, prelude=CJS)

# ---------------------------------------------------------------- 3.6.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Revenue</span> is the money a firm receives from selling its output. <b>Total revenue (TR)</b> is the <b>total</b> received; <b>average revenue (AR)</b> is the revenue <b>per unit</b> sold. For a firm selling at one price, <b>AR equals the price</b>.</p></div>

  <h2>Definitions</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Definition</th><th>Formula</th><th>Example</th></tr>
    <tr><td><b>Total revenue (TR)</b></td><td>The total money a firm receives from selling its output</td><td>TR = price × quantity sold</td><td>$5 × 200 = $1,000</td></tr>
    <tr><td><b>Average revenue (AR)</b></td><td>Revenue per unit sold</td><td>AR = TR ÷ quantity sold = price</td><td>$1,000 ÷ 200 = $5</td></tr>
  </table></div>

  <h2>Revenue is not profit</h2>
  <ul>
    <li>Revenue is the money <b>coming in</b>; costs are the money <b>going out</b>.</li>
    <li><b>Profit = total revenue − total cost.</b></li>
    <li>A firm can have high revenue but low (or negative) profit if its costs are high.</li>
  </ul>
  <h2>What revenue depends on</h2>
  <ul>
    <li>The <b>price</b> the firm charges.</li>
    <li>The <b>quantity sold</b>, which depends on demand, marketing and the price of rivals.</li>
    <li>For a firm with a demand curve, price and quantity move in opposite directions, so the effect of a price change on revenue depends on PED (see 2.6.4).</li>
  </ul>
'''
steppers = [
  ("Total and average revenue", "--accent", ["A bakery sells 200 loaves at $5 each", "TR = price × quantity = $1,000", "AR = TR ÷ quantity = $5", "AR equals the price", "Revenue is money in; profit also needs costs"]),
  ("From revenue to profit", "--good", ["Revenue (TR) = $1,000", "Total cost (TC) = $700", "Profit = TR − TC", "Profit = $300", "If costs exceeded $1,000 the firm would make a loss"]),
]
lab1 = dict(title="Revenue and profit", intro="Set the price, quantity and total cost. See TR, AR and profit.", rl=["Total revenue", "Average revenue", "Profit"],
  sliders=[("Price ($)", 1, 20, 1, 5, "'$' + v"), ("Quantity sold", 10, 500, 10, 200, "v"), ("Total cost ($)", 0, 5000, 100, 700, "'$' + v")],
  fn="const tr = v[0] * v[1], ar = tr / v[1], pr = tr - v[2]; return { r: ['$' + tr, '$' + ar.toFixed(2), (pr >= 0 ? '+' : '−') + '$' + Math.abs(pr)], t: 'TR = $' + v[0] + ' × ' + v[1] + ' = $' + tr + '. AR = $' + tr + ' ÷ ' + v[1] + ' = $' + ar.toFixed(2) + ', which equals the price. With total cost $' + v[2] + ', profit = $' + tr + ' − $' + v[2] + ' = ' + (pr >= 0 ? '+' : '−') + '$' + Math.abs(pr) + (pr < 0 ? ' (a loss)' : '') + '.', bars: [['TR', tr / 10, '--good', '$' + tr], ['TC', v[2] / 10, '--warn', '$' + v[2]], ['Profit', Math.max(0, pr) / 10, '--accent', '$' + pr]] };")
lab2 = dict(title="Revenue terms", intro="Pick a term to see its meaning and formula.", h1="Formula", h2="Meaning",
  items=[("Total revenue", "TR = P × Q", "Total money received from sales."), ("Average revenue", "AR = TR ÷ Q", "Revenue per unit; equals price."), ("Profit", "TR − TC", "Revenue minus total cost."), ("Loss", "TC > TR", "Costs exceed revenue."), ("Break-even", "TR = TC", "Neither profit nor loss."), ("Sales", "Quantity sold", "The number of units sold.")])
cl = [("Is each <b>revenue</b> or a <b>cost</b>?", ["Revenue", "Cost"], [("Money from selling goods", 0), ("Price × quantity", 0), ("Sales receipts", 0), ("Wages paid", 1), ("Rent", 1), ("Raw materials", 1)], "In or out."),
      ("Which <b>formula</b> matches?", ["TR", "AR", "Profit"], [("Price × quantity", 0), ("TR ÷ quantity", 1), ("TR − TC", 2), ("Equals the price", 1), ("Revenue minus costs", 2)], "Learn the formulas.")]
match = [["Total revenue", "Price × quantity sold"], ["Average revenue", "Revenue per unit sold"], ["Profit", "TR − TC"], ["Loss", "TC greater than TR"], ["Break-even", "TR equals TC"], ["Sales", "Quantity sold"]]
order = ("Put the steps in order: <b>calculating profit</b>.", ["Find the price", "Find the quantity sold", "Multiply to get total revenue", "Subtract total cost", "The result is profit (or loss)"], "Profit = TR − TC.")
calcs = [("Price is $5 and quantity sold is 200. What is TR ($)?", 1000, "5 × 200 = <b>$1,000</b>.", None, None), ("TR is $1,000 and quantity is 200. What is AR ($)?", 5, "1,000 ÷ 200 = <b>$5</b>.", None, None), ("TR is $1,000 and TC is $700. What is profit ($)?", 300, "1,000 − 700 = <b>$300</b>.", None, None)]
mcq = [("Total revenue is:", ["Price + quantity", "Price × quantity", "Price − cost", "Quantity ÷ price"], 1, "P × Q."), ("Average revenue is:", ["TR × quantity", "TR ÷ quantity", "TC ÷ quantity", "Price − quantity"], 1, "Per unit."), ("AR equals:", ["The price", "The cost", "The profit", "The tax"], 0, "For single-price sales."), ("Profit is:", ["TR + TC", "TR − TC", "TC − TR", "AR − AFC"], 1, "Revenue minus cost."), ("A firm makes a loss when:", ["TR > TC", "TR = TC", "TR < TC", "AR = P"], 2, "Costs exceed revenue.")]
cards = [("Total revenue (TR)", "Price × quantity sold."), ("Average revenue (AR)", "Total revenue divided by quantity; equals price."), ("Profit", "Total revenue minus total cost."), ("Loss", "When total cost exceeds total revenue."), ("Break-even", "Where total revenue equals total cost."), ("Sales", "The quantity sold."), ("Price", "The amount paid per unit."), ("Quantity sold", "The number of units sold."), ("Turnover", "Another word for revenue.")]
exam_qs = [
  Q(1, "Define", 2, "Define total revenue.", "Price × quantity.", "[K|Total revenue is the money a firm receives from selling its output,] [K|calculated as price multiplied by quantity sold.]"),
  Q(2, "Define", 2, "Define average revenue.", "Revenue per unit.", "[K|Average revenue is total revenue divided by the quantity sold,] [K|that is, revenue per unit.]"),
  Q(3, "Calculate", 2, "A firm sells 200 units at $5 each. Calculate total revenue and average revenue.", "TR = 1,000; AR = 5.", "[A|TR = 5 × 200 = $1,000.] [A|AR = 1,000 ÷ 200 = $5.]"),
  Q(4, "Explain", 4, "Explain the difference between revenue and profit.", "Money in vs revenue minus cost.", "[K|Revenue is the money a firm receives from selling its goods.] [N|It does not take account of costs.] [K|Profit is total revenue minus total costs.] [N|A firm with high revenue may still make a loss if costs are high.]"),
]
tips_ = [("TR = P × Q; AR = TR ÷ Q.", "AR equals price."), ("Revenue is not profit.", "Subtract cost."), ("Show working.", "Units and $."), ("Define with formula.", "Both words and symbols.")]
real_items = [("Supermarkets", "Very large revenues but low profit margins.", "Revenue vs profit."), ("Ticket sales", "Price per ticket times number sold gives box-office revenue.", "TR."), ("Online shops", "Average revenue per order is tracked closely.", "AR."), ("Start-ups", "Many early-stage firms have rising revenue but still make losses.", "Revenue vs profit.")]
review("ig-revenue-definitions", "k363", "3.6.3", "Definitions of Revenue", "Total revenue and average revenue, and how revenue differs from profit. Syllabus 3.6.3.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Define", "Calculate", "Explain"], real_items)

# ---------------------------------------------------------------- 3.6.4
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Revenue is <b>calculated</b> with <b>TR = price × quantity</b> and <b>AR = TR ÷ quantity</b>. The <b>influence of sales</b> on revenue is direct: for a given price, more sales mean more revenue. But to sell more a firm may need to <b>lower its price</b>, so what happens to revenue depends on the <b>elasticity of demand</b> and on <b>costs</b>.</p></div>

  <h2>Calculating revenue</h2>
  <div class="tw"><table class="t">
    <tr><th>Price ($)</th><th>Quantity sold</th><th>Total revenue ($)</th><th>Average revenue ($)</th></tr>
    <tr><td>10</td><td>20</td><td>200</td><td>10</td></tr>
    <tr><td>8</td><td>40</td><td>320</td><td>8</td></tr>
    <tr class="hl"><td>6</td><td>60</td><td>360</td><td>6</td></tr>
    <tr><td>4</td><td>70</td><td>280</td><td>4</td></tr>
    <tr><td>2</td><td>80</td><td>160</td><td>2</td></tr>
  </table></div>
  <p>In this table total revenue rises as price falls from $10 to $6 (demand is elastic over that range) and then falls (demand becomes inelastic).</p>

  <h2>The influence of sales on revenue</h2>
  <ul>
    <li>If the price is constant, a <b>rise in sales raises TR</b> in proportion: 10% more units means 10% more revenue.</li>
    <li>If a firm cuts its price to sell more, revenue rises only if the <b>quantity rises by a bigger percentage</b> than the price falls (elastic demand).</li>
    <li>Sales can be increased by <b>advertising</b>, better quality, wider distribution or a <b>shift in demand</b>, which raises revenue at every price.</li>
    <li>Revenue is not the same as <b>profit</b>: more sales at a lower price may increase revenue but not profit.</li>
  </ul>
'''
steppers = [
  ("Sales and revenue at a fixed price", "--good", ["A shop sells 100 items at $10: TR = $1,000", "Advertising lifts sales to 150", "TR = 150 × $10 = $1,500", "Revenue rises with sales", "AR is still $10"]),
  ("A price cut and revenue", "--warn", ["A firm cuts price from $10 to $8", "Quantity sold rises from 20 to 40", "TR rises from $200 to $320", "Demand is elastic: revenue rises", "Beyond a point further cuts reduce revenue"]),
]
lab1 = dict(title="Price, sales and revenue", intro="Choose a price from the demand schedule and see sales, TR and AR. Find the price that gives the highest revenue.", rl=["Quantity sold", "Total revenue", "Average revenue"],
  sliders=[("Price ($)", 2, 10, 2, 6, "'$' + v")],
  fn="const q = { 10: 20, 8: 40, 6: 60, 4: 70, 2: 80 }[v[0]], tr = v[0] * q, best = Math.max(200, 320, 360, 280, 160); return { r: [q, '$' + tr, '$' + v[0]], t: 'At $' + v[0] + ' the firm sells ' + q + ' units: TR = $' + v[0] + ' × ' + q + ' = $' + tr + ' and AR = $' + v[0] + '. ' + (tr === best ? 'This is the highest revenue in the table.' : 'Revenue would be higher at $6 ($360).') + ' Lowering price raises sales, but revenue only rises while the quantity gain is proportionately bigger than the price fall.', bars: [[ '$10', 200, '--accent'], ['$8', 320, '--accent'], ['$6', 360, '--accent'], ['$4', 280, '--accent'], ['$2', 160, '--accent']].map((b, i) => [b[0], b[1], [10, 8, 6, 4, 2][i] === v[0] ? '--good' : '--accent', '$' + b[1]]) };")
lab2 = dict(title="What raises revenue?", intro="Pick an action to see its effect on sales and revenue.", h1="Effect on revenue", h2="Why",
  items=[("Successful advertising", "Revenue rises", "More sold at the same price (demand shifts right)."), ("A price cut with elastic demand", "Revenue rises", "Quantity rises by more than price falls."), ("A price cut with inelastic demand", "Revenue falls", "Quantity rises by less than price falls."), ("A price rise with elastic demand", "Revenue falls", "Quantity falls by more."), ("A price rise with inelastic demand", "Revenue rises", "Quantity falls by less."), ("A rival cuts its price", "Revenue falls", "Customers switch away.")])
cl = [("What happens to <b>total revenue</b>?", ["Rises", "Falls"], [("Sales rise at a constant price", 0), ("Price cut, elastic demand", 0), ("Price rise, inelastic demand", 0), ("Sales fall at a constant price", 1), ("Price cut, inelastic demand", 1), ("Price rise, elastic demand", 1)], "Link to PED."),
      ("Is each way to <b>increase sales</b> or a <b>result</b> of higher sales?", ["Way to increase sales", "Result of higher sales"], [("Advertising", 0), ("Lower price", 0), ("Better quality", 0), ("Higher total revenue", 1), ("Larger market share", 1), ("More production needed", 1)], "Cause and effect.")]
match = [["Total revenue", "Price × quantity"], ["Average revenue", "TR ÷ quantity"], ["Elastic demand", "Price cut raises revenue"], ["Inelastic demand", "Price cut lowers revenue"], ["Advertising", "Aims to raise sales at every price"], ["Sales", "Quantity sold"]]
order = ("Put the chain in order: <b>how advertising raises revenue</b>.", ["A firm runs an advertising campaign", "Demand for its product rises", "More units are sold at the same price", "Total revenue = price × higher quantity", "Revenue rises"], "Sales up, revenue up.")
calcs = [("Price falls from $8 to $6 and quantity rises from 40 to 60. What is the new TR ($)?", 360, "6 × 60 = <b>$360</b>.", None, None), ("Price is $6 and TR is $360. How many units were sold?", 60, "360 ÷ 6 = <b>60</b>.", None, None), ("Sales rise from 150 to 180 at a constant price of $10. By how much does TR rise ($)?", 300, "30 × 10 = <b>$300</b>.", None, None), ("A firm sells 400 units for TR of $2,000. What is AR ($)?", 5, "2,000 ÷ 400 = <b>$5</b>.", None, None)]
mcq = [("If price is constant, a rise in sales:", ["Raises TR", "Lowers TR", "Leaves TR unchanged", "Lowers AR"], 0, "More units, same price."), ("A price cut raises revenue when demand is:", ["Inelastic", "Elastic", "Zero", "Fixed"], 1, "Quantity gain bigger."), ("AR =", ["TR ÷ quantity", "TR × quantity", "TC ÷ quantity", "Price × cost"], 0, "Per unit."), ("Advertising aims to:", ["Raise demand and sales", "Cut costs", "Raise taxes", "Lower AR"], 0, "More sales."), ("Revenue is the same as profit:", ["True", "False", "Only for large firms", "Only in the long run"], 1, "Profit is revenue minus costs.")]
cards = [("Total revenue", "Price × quantity sold."), ("Average revenue", "Total revenue ÷ quantity."), ("Sales", "The quantity sold."), ("Elastic demand", "Quantity responds strongly to price."), ("Inelastic demand", "Quantity responds weakly to price."), ("Advertising", "Promotion to raise demand."), ("Market share", "A firm's share of total sales."), ("Demand schedule", "A table of prices and quantities."), ("Profit", "TR − TC.")]
exam_qs = [
  Q(1, "Calculate", 3, "A firm cuts its price from $8 to $6 and sales rise from 40 to 60. Calculate the change in total revenue.", "320 → 360.", "[A|Old TR = 8 × 40 = $320.] [A|New TR = 6 × 60 = $360.] [A|TR rises by $40.]"),
  Q(2, "Explain", 4, "Explain how an increase in sales may affect a firm's revenue.", "Higher quantity at same price raises TR; price cuts need elasticity.", "[K|Total revenue is price multiplied by quantity sold.] [N|If price stays the same, more sales raise revenue.] [N|If the firm cut its price to sell more, revenue rises only if the percentage rise in quantity exceeds the percentage fall in price.]"),
  Q(3, "Analyse", 6, "Analyse how advertising may influence a firm's revenue.", "Demand right; sales up; costs.", "[K|Advertising aims to change tastes and raise demand for the product.] [N|More units are sold at each price, so total revenue rises.] [N|It may also allow the firm to raise its price.] [E|However, advertising costs money, so profit may not rise as much as revenue.]", key=True),
  Q(4, "Discuss", 6, "Discuss whether a firm should cut its prices to raise revenue.", "PED, costs, rivals. Judgement.", "[K|A price cut raises sales, but revenue only rises if demand is elastic.] [N|If demand is inelastic, revenue falls.] [N|Rivals may also cut prices, cancelling the gain.] [E|Costs also matter: extra sales may raise costs and lower profit. Overall, it depends on elasticity and costs.]", key=True),
]
tips_ = [("TR = P × Q; AR = TR ÷ Q.", "Show working."), ("Price constant: sales up, revenue up.", "Say it."), ("Link price cuts to PED.", "Elastic or inelastic."), ("Revenue is not profit.", "Mention costs in evaluation.")]
real_items = [("Black Friday", "Deep discounts raise sales and often revenue.", "Elastic demand."), ("Advertising campaigns", "Big launches lift sales of new phones.", "Demand shifts right."), ("Cinema off-peak tickets", "Lower prices fill seats and raise takings.", "Price cuts."), ("Luxury brands", "Higher prices keep revenue strong because demand is inelastic.", "Inelastic demand.")]
review("ig-revenue-calculation", "k364", "3.6.4", "Calculation of Revenue", "Calculating TR and AR and how sales influence revenue. Syllabus 3.6.4.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Calculate", "Explain", "Analyse", "Discuss"], real_items)

# ---------------------------------------------------------------- 3.6.5
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Firms have different <b>objectives</b>. The main ones are <b>survival</b>, <b>profit maximisation</b>, <b>growth</b> and <b>social welfare</b>. The objective chosen depends on the type of firm, its size, its age and who owns it.</p></div>

  <h2>Objectives of firms</h2>
  <div class="tw"><table class="t">
    <tr><th>Objective</th><th>Meaning</th><th>Typical firm</th><th>Why chosen</th></tr>
    <tr><td><b>Survival</b></td><td>Staying in business (covering costs and avoiding bankruptcy)</td><td>New firms, firms in a recession or fierce competition</td><td>Cannot achieve other aims if it fails</td></tr>
    <tr><td><b>Profit maximisation</b></td><td>Making the largest possible profit (TR − TC)</td><td>Most private firms, especially with shareholders</td><td>Rewards owners and funds investment</td></tr>
    <tr><td><b>Growth</b></td><td>Increasing the size of the firm (sales, market share, output)</td><td>Firms seeking economies of scale and market power</td><td>Lower costs, more power, higher long-run profit, more security</td></tr>
    <tr><td><b>Social welfare</b></td><td>Providing benefits for society, not only profit</td><td>Public sector firms, charities, social enterprises, some ethical firms</td><td>Aims include jobs, the environment, community service</td></tr>
  </table></div>

  <h2>Do objectives conflict?</h2>
  <ul>
    <li><b>Growth</b> may reduce short-run profit (spending on expansion), but raise long-run profit.</li>
    <li><b>Social welfare</b> aims (fair wages, green production) may raise costs and cut profit.</li>
    <li><b>Survival</b> may require cutting prices or profit in the short run.</li>
    <li>Firms may combine objectives, for example <b>satisficing</b> (making enough profit while pursuing other aims).</li>
  </ul>
  <p class="note">Public sector firms usually aim for <b>social welfare</b>; private firms usually aim for <b>profit</b> and <b>growth</b>; new firms aim to <b>survive</b>.</p>
'''
steppers = [
  ("Survival first", "--bad", ["A new restaurant opens", "Customers are few and costs are high", "The owner cuts costs and offers discounts to stay open", "Profit is low but the business survives", "Later it can aim for growth and profit"]),
  ("Growth and long-run profit", "--good", ["A firm reinvests profit instead of paying it out", "It expands and wins more customers", "Economies of scale cut unit costs", "Market power rises", "Higher profit in the long run"]),
  ("Social welfare as an objective", "--accent", ["A state-owned bus company serves rural routes", "These routes make a loss", "It keeps them running for the community", "Profit is sacrificed", "Social welfare is achieved"]),
]
lab1 = dict(title="Choose the objective", intro="Set the features of a firm and see which objective it is most likely to pursue.", rl=["Most likely objective", "Profit focus", "Welfare focus"],
  sliders=[("Is the firm new or struggling? (1 no, 10 yes)", 1, 10, 1, 3, "v"), ("Owned by shareholders seeking returns (1 no, 10 yes)", 1, 10, 1, 7, "v"), ("Wants to expand and win market share (1 no, 10 yes)", 1, 10, 1, 5, "v"), ("Owned by government or a charity (1 no, 10 yes)", 1, 10, 1, 2, "v")],
  fn="const sc = [['Survival', v[0]], ['Profit maximisation', v[1]], ['Growth', v[2]], ['Social welfare', v[3]]], top = sc.reduce((a, b) => b[1] > a[1] ? b : a); return { r: [top[0], v[1] + '/10', v[3] + '/10'], t: 'The strongest pull is towards ' + top[0].toLowerCase() + '. New or struggling firms prioritise survival, shareholder-owned firms profit, expanding firms growth, and public or charitable firms social welfare. Real firms usually pursue a mix (illustrative model).', bars: sc.map((s, i) => [s[0], s[1], ['--bad', '--good', '--accent', '--warn'][i]]) };")
lab2 = dict(title="Which firm, which objective?", intro="Pick a firm to see its most likely objective.", h1="Likely objective", h2="Why",
  items=[("A new start-up", "Survival", "Must stay open."), ("A listed company", "Profit maximisation", "Shareholders want returns."), ("A supermarket opening new stores", "Growth", "Larger market share."), ("A state hospital", "Social welfare", "Provides a public service."), ("A charity shop", "Social welfare", "Raises money for a cause."), ("A firm in a deep recession", "Survival", "Avoid bankruptcy.")])
cl = [("Which <b>objective</b> does each describe?", ["Survival", "Profit maximisation", "Growth", "Social welfare"], [("Staying in business through a recession", 0), ("Making the largest possible profit", 1), ("Increasing market share", 2), ("Providing free services to the community", 3), ("Avoiding bankruptcy", 0), ("Opening new branches to expand", 2)], "Four objectives."),
      ("Is each firm more likely to be <b>private</b> or <b>public/charity</b>?", ["Private (profit, growth)", "Public/charity (social welfare)"], [("A listed technology company", 0), ("A shareholder-owned bank", 0), ("A fast-food chain", 0), ("A state hospital", 1), ("A charity", 1), ("A state school", 1)], "Ownership and aims.")]
match = [["Survival", "Staying in business"], ["Profit maximisation", "Making the largest profit possible"], ["Growth", "Increasing the size of the firm"], ["Social welfare", "Benefiting society, not just profit"], ["Satisficing", "Making enough profit while pursuing other aims"], ["Market share", "A firm's share of total sales"]]
order = ("Put the chain in order: <b>why firms may pursue growth</b>.", ["The firm expands output", "It gains economies of scale", "Unit costs fall", "Its market share and power rise", "Long-run profit rises"], "Growth pays off.")
calcs = [("A firm's market share rises from 10% to 14%. By how many percentage points?", 4, "14 − 10 = <b>4</b> percentage points.", None, None), ("A start-up has revenue of $60,000 and costs of $65,000. What is the profit or loss ($)? Enter the figure.", -5000, "60,000 − 65,000 = <b>−$5,000</b>: a loss.", None, None)]
mcq = [("A new firm's most likely first objective is:", ["Growth", "Survival", "Social welfare", "Monopoly"], 1, "Stay open."), ("Public sector firms often aim for:", ["Profit maximisation", "Social welfare", "Bankruptcy", "Tax avoidance"], 1, "Public service."), ("Profit maximisation means:", ["Largest possible profit", "Largest firm", "Lowest price", "Highest wages"], 0, "TR − TC largest."), ("Growth may:", ["Lower short-run profit but raise long-run profit", "Always raise short-run profit", "Reduce sales", "Remove costs"], 0, "Investment."), ("Satisficing is:", ["Maximum profit only", "Making enough profit while pursuing other aims", "Closing down", "Raising prices"], 1, "Good enough.")]
cards = [("Survival", "The objective of staying in business."), ("Profit maximisation", "The objective of making the largest profit."), ("Growth", "The objective of increasing the firm's size."), ("Social welfare", "The objective of benefiting society."), ("Satisficing", "Making an acceptable profit while pursuing other aims."), ("Market share", "A firm's share of total market sales."), ("Shareholder", "An owner of part of a company."), ("Social enterprise", "A business with social aims."), ("Bankruptcy", "When a firm cannot pay its debts.")]
exam_qs = [
  Q(1, "Identify", 2, "Identify two objectives of firms.", "Survival, profit maximisation, growth, social welfare.", "[K|Profit maximisation.] [K|Growth (or survival or social welfare).]"),
  Q(2, "Explain", 4, "Explain why a new firm may have survival as its main objective.", "Low sales, high costs, risk of failure.", "[K|A new firm has few customers and high start-up costs.] [N|It risks running out of money and going bankrupt,] [N|so it aims to cover costs and stay in business before pursuing other objectives.]"),
  Q(3, "Explain", 4, "Explain why a public sector firm may aim for social welfare rather than profit.", "Provide services; government ownership.", "[K|Public sector firms are owned by the government to provide services.] [N|They may serve unprofitable routes or areas because the community needs them,] [N|so they sacrifice profit for social welfare.]"),
  Q(4, "Discuss", 8, "Discuss whether profit maximisation is the most important objective of a firm.", "Profit vs growth, survival, welfare. Judgement.", "[K|Profit maximisation rewards owners and funds investment.] [N|Most private firms aim for profit because shareholders demand returns.] [N|However, new firms may prioritise survival, some prioritise growth for the long run, and public firms prioritise social welfare.] [E|Overall, profit is the main objective for most private firms in the long run, but it is not always the most important in the short run or for firms with other owners.]", key=True),
]
tips_ = [("Four objectives.", "Survival, profit, growth, social welfare."), ("Link objective to type of firm.", "New, private, public."), ("Objectives can conflict.", "Growth vs short-run profit."), ("Use examples.", "Start-up, listed company, state hospital.")]
real_items = [("Start-ups", "Many young firms aim first to survive.", "Survival."), ("Amazon", "Reinvested profits for decades to achieve growth.", "Growth."), ("NHS and public services", "Aim to provide care for all, not profit.", "Social welfare."), ("Listed companies", "Shareholders push for higher profit and dividends.", "Profit maximisation.")]
review("ig-firm-objectives", "k365", "3.6.5", "Objectives of Firms", "Survival, social welfare, profit maximisation and growth. Syllabus 3.6.5.", learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, ["Identify", "Explain", "Discuss"], real_items)
