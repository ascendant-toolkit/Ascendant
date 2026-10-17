"""AS syllabus 3.2.2 Impact and incidence of subsidies. Run: python3 tools/artifact-kit/mk_as32.py"""
from asx import *
EY = EYAS("3.2.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">subsidy</b> is a payment by the government to producers (or sometimes consumers) that <b>lowers the cost of production</b>, so the <b>supply curve shifts to the right (down)</b> by the amount of the subsidy per unit. The <b>price consumers pay falls</b>, the <b>price producers receive rises</b> (market price plus subsidy) and the <b>quantity increases</b>, so consumer surplus and producer surplus both rise. The <b>incidence</b> of the subsidy is shared between consumers and producers according to elasticity, and the <b>cost to the government</b> is the subsidy per unit times the quantity sold, which has an <b>opportunity cost</b> in other spending or higher taxes. Subsidies are used to <b>encourage merit goods</b>, support producers and keep prices of essentials low, but they can be costly, hard to target and difficult to remove.</p></div>

  <h2>1 · The impact of a subsidy (3.2.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The vertical gap between the old and new supply curves is the <b>subsidy per unit</b>.</li>
    <li><b>Price paid by consumers falls</b> (but by less than the subsidy); <b>price received by producers</b> rises above the old price; <b>quantity rises</b>.</li>
    <li><b>Cost to the government = subsidy per unit × quantity sold after the subsidy.</b></li>
    <li>It raises <b>consumer and producer surplus</b>, but the cost is more than the gain in private surplus, so unless there are external benefits there is a <b>welfare loss</b> from over-production.</li>
  </ul>

  <h2>2 · Incidence and the cost of a subsidy</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Consumers gain more</b> from a subsidy the more <b>inelastic demand</b> is relative to supply; producers gain more the more inelastic supply is.</li>
    <li>The <b>more elastic demand</b>, the more quantity responds, so the <b>larger the total cost</b> of the subsidy for the same rate per unit.</li>
    <li><b>Subsidising a merit good</b> works best if demand is <b>price elastic</b>; if demand is inelastic, consumption barely rises.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td>Raises consumption of merit goods with external benefits</td><td>Opportunity cost: money could fund hospitals, schools or lower taxes</td></tr>
    <tr><td>Lowers prices for low-income households</td><td>May go to people who would have bought anyway (poor targeting)</td></tr>
    <tr><td>Supports domestic industries and jobs; encourages new technology (e.g. renewables)</td><td>Producers may become inefficient or dependent; hard to remove</td></tr>
    <tr><td>Can offset other market failures</td><td>Does not address information failure on its own; may distort trade</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>Draw the new supply curve <b>below</b> the old one, label the price consumers pay and the price producers get, and shade the <b>cost</b>. Evaluate with <b>elasticity</b>, <b>opportunity cost</b> and whether other policies (information, regulation) might work better.</div>
'''

watch = '''
  <h2>1 · A subsidy shifts supply</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stS"></div>
  <h2>2 · The cost of the subsidy and elasticity</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Set the subsidy</h2>
  <p>Change the subsidy and the steepness of demand and supply. The blue box is the saving to consumers, the green box the gain to producers.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Consumers pay</small><strong id="r1"></strong></div><div><small>Producers receive</small><strong id="r2"></strong></div><div><small>Cost to government</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with a subsidy and the incidence shaded"></svg></div></div></div>

  <h2>Lab 2 · How big should a subsidy be?</h2>
  <p>A merit good brings an external benefit of $E per unit. Set the subsidy and see the net gain to society. The gain is greatest when the subsidy equals the external benefit.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Extra units</small><strong id="t1"></strong></div><div><small>Subsidy cost</small><strong id="t2"></strong></div><div><small>Net gain to society</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="A curve of net gain to society against the size of the subsidy with the chosen subsidy marked"></svg></div></div></div>
'''

practise = '''
  <h2>1 · What does a subsidy do?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a subsidy in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Subsidised public transport", "A government pays bus operators a fixed amount per journey. Fares fall, more people use buses and congestion may fall. The cost to taxpayers is large, and the opportunity cost is spending on other services.", "a subsidy on a merit good and its opportunity cost.") +
rw("Electric vehicle grants", "Grants lower the effective price of electric cars. Demand is fairly elastic, so sales rise by a lot, but some of the money goes to buyers who would have bought one anyway.", "elastic demand raising the cost, and poor targeting.") +
rw("Farm subsidies", "Payments to farmers raise their incomes and keep food cheap, but can lead to over-production and make farmers dependent on support. Removing them can cause hardship.", "producer incidence and the difficulty of removing a subsidy.") +
rw("Free school meals", "Meals are provided at no cost to the pupil. Some of the benefit is private, but better nutrition improves learning, an external benefit that justifies public spending.", "a subsidy on a merit good with external benefits.")
)

mc_exam = [
  mcq("m23_12", 13, "Why do some local governments subsidise the provision of bicycles to encourage their use?", ["Consumers are afraid of having car accidents", "Consumers are unable to afford bicycles", "Consumers are not aware of the external benefits of using bicycles", "Consumers ignore the external costs of using bicycles"], 2, "Cycling brings external benefits that consumers do not fully take into account, a merit good problem."),
  mcq("s20_12", 17, "Which measure would not be part of a government subsidy to protect domestic producers from competition?", ["import quotas", "interest-free loans provided by the government", "reductions in profits (business) taxes", "transfer payments"], 0, "Quotas restrict imports. They are a protectionist measure, not a subsidy."),
  mcq("s22_13", 18, "What is not a producer subsidy?", ["a grant given to cover losses in an essential industry, such as the rail industry", "a guaranteed minimum price paid to farmers to ensure the long run supply of food", "financial assistance given to a pharmaceutical company to develop a new vaccine", "a payment made to the unemployed to allow them to buy essential goods and services"], 3, "A payment to unemployed people is a transfer payment, not a subsidy to producers."),
  mcq("s20_13", 6, "What is most likely to increase the quantity of houses supplied?", ["a policy to help house buyers on modest incomes", "a restriction on the level of rent that can be charged", "a rise in the tax on materials used for building houses", "the removal of a subsidy to house builders"], 0, "Help to buyers raises demand and the price, so quantity supplied rises. A rent limit, a tax and removing a subsidy all cut supply."),
  mcq("s22_11", 6, "What will increase the producer surplus of farmers that grow carrots?", ["a decrease in the demand for carrots", "a decrease in the price of carrot seed", "a decrease in the price of cabbage", "a decrease in the subsidy on carrots"], 1, "Cheaper seed lowers costs, which raises supply and the producer surplus at a given price."),
  mcq("s24_11", 13, "A government wishes to raise the incomes of farmers without raising the price of food to consumers. Which policy should it use?", ["a maximum price below the market price for food", "a minimum price below the market price for food", "a payment of a subsidy to farmers to produce food", "a release of government food stocks onto the market"], 2, "A subsidy lifts what farmers receive while the price paid by consumers does not rise."),
  mcq("s23_12", 16, "Which combination of government measures is most likely to increase the consumption of a merit good?", ["effective maximum price and a subsidy to producers", "effective maximum price and an indirect tax on producers", "effective minimum price and a subsidy to producers", "effective minimum price and an indirect tax on producers"], 0, "A maximum price and a subsidy both push the price consumers pay down, raising consumption.")
]

exam = exam_page("subsidies",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Subsidies appear as 8 or 12 mark Paper 2 parts most years, often as the best way to raise consumption of a merit good, and in several short data-response parts. Reworded past questions are below, with seven Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "2", "May/June 2025 (21) Q3(a); May/June 2024 (22) Q3(a)"), ("Essay parts, 12 marks", "2", "Feb/March 2025 (22) Q3(b); Oct/Nov 2023 (23) Q3(b)"), ("Data response, 2 marks", "1", "Oct/Nov 2022 (23) Q1(a)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2025")],
  [
  eq(P("s25_21", "3(a)"), "8 marks", "With the help of a diagram, explain how changes in a subsidy can influence the price and quantity sold of a product in a market and consider how expenditure on a subsidy is affected by the price elasticity of demand for the product.",
     ["Knowledge (up to 3): a correct diagram with labelled axes, demand and supply (1); an increase in a subsidy shifting supply to the right, lowering price and raising quantity, with new equilibrium positions shown (1); a decrease in a subsidy shifting supply to the left, raising price and lowering quantity (1).",
      "Analysis (up to 3): a subsidy is a sum of money paid by a government to a producer (1); an increase lowers the price charged to consumers and raises quantity (1) and the explanation of how that affects the cost to the government.",
      "Evaluation (up to 2): the cost of a subsidy depends on price elasticity of demand: the more elastic, the more quantity rises and the greater the expenditure, with a justified conclusion."],
     "Diagram: subsidy shifts supply right, price down, quantity up. Cost = subsidy × quantity. Elastic demand: quantity rises more, so cost is higher.",
     [[("k", "A subsidy is a payment by the government to producers per unit of output. On a diagram it shifts the supply curve to the right, by the amount of the subsidy, lowering the equilibrium price and increasing the quantity sold. A bigger subsidy shifts supply further, and removing it shifts supply back to the left, raising price and cutting quantity.")], [("n", "Because the subsidy lowers firms' costs, they supply more at each price, and the price consumers pay falls. The government pays the subsidy on every unit sold, so the cost is the subsidy per unit multiplied by the quantity sold after the subsidy.")], [("e", "The cost depends on the price elasticity of demand. If demand is elastic, the fall in price brings a large rise in quantity, so the total spent on the subsidy is larger. If demand is inelastic, quantity rises less, so the subsidy costs less but also does less to raise consumption.")]]),
  eq(P("s24_22", "3(a)"), "8 marks", "With the help of an example of each, explain the difference between a merit good and a demerit good and consider whether a subsidy given to a merit good will always be effective in increasing its consumption.",
     ["Knowledge (up to 3): a merit good is desirable but under-provided or under-consumed because of information failure or a lack of awareness (1); a demerit good is undesirable but over-consumed because of information failure (1); valid examples of both (1).",
      "Analysis (up to 3): a subsidy may encourage poorer households to consume more because it lowers the price (1); but demand may be price inelastic, so the rise in quantity demanded is less than the fall in price (1); the information failure may persist (1).",
      "Evaluation (up to 2): a judgement on whether a subsidy will always be effective."],
     "Merit: under-consumed. Demerit: over-consumed. Subsidy lowers price, but may not work if demand is inelastic or information is poor.",
     [[("k", "A merit good, such as vaccination, is under-consumed because people do not fully appreciate its benefits. A demerit good, such as tobacco, is over-consumed because people underestimate the harm.")], [("n", "A subsidy lowers the price of a merit good, so poorer households who could not afford it may consume more. But if demand is price inelastic, the rise in quantity will be smaller than the fall in price, and if the problem is a lack of awareness, a lower price may not change behaviour.")], [("e", "So a subsidy will not always be effective. It is most likely to work where cost is the barrier and demand is elastic, and less likely where information failure is the main problem, so information campaigns could do better.")]]),
  eq(P("m25_22", "3(b)"), "12 marks", "Assess the extent to which a subsidy is likely to be the best method to increase the consumption of a merit good.",
     ["Analysis (up to 8): the meaning of a subsidy and a merit good; how a subsidy reduces the costs of production, lowers the price and raises quantity demanded; potential problems such as the opportunity cost of government spending, dependency, incorrect targeting and when to remove provision; alternative methods, such as improved information, analysed for how they would increase consumption.",
      "Evaluation (up to 4): an assessment of whether a subsidy is the best method, perhaps depending on price elasticity of demand, cost and the cause of under-consumption, with a justified conclusion."],
     "Subsidy: lowers price, but cost and targeting. Alternatives: information, direct provision. Judge using elasticity and cause of under-consumption.",
     [[("n", "A merit good, such as education, is under-consumed because consumers do not fully understand its benefits. A subsidy lowers production costs, so the price falls and quantity demanded rises, especially if demand is elastic. But it has an opportunity cost, because the money could be spent elsewhere, it may go to people who would have bought anyway, and it can be hard to remove. Alternative policies include information campaigns, which address the cause of the problem directly but work slowly, and direct provision by the state.")], [("e", "A subsidy is probably most effective where the barrier is cost and demand is elastic, but if under-consumption is mainly due to a lack of information, an information campaign may be better. A combination of a subsidy and information is probably the most effective.")]]),
  eq(P("w22_23", "1(a)"), "2 marks", "Explain what might be the opportunity cost if a government agreed to pay larger subsidies to its farmers.",
     ["Opportunity cost is the cost in terms of the best alternative forgone (1).", "Other areas of government funding, such as healthcare or education, would have less spending allocated to them (1)."],
     "Opportunity cost defined. Name what the money could have been spent on.",
     [[("k", "Opportunity cost is the next best alternative given up. If the government pays more subsidies to farmers, it has less to spend on something else, such as health care or schools, which is the opportunity cost.")]])
  ],
  )

tips = tips_html(
  [("Draw supply shifting down and right.", "By the subsidy per unit."),
   ("Label both prices.", "Paid by consumers, received by producers."),
   ("Cost = subsidy × new quantity.", "Shade the rectangle."),
   ("Use elasticity.", "Elastic demand: a bigger rise in quantity and a bigger cost."),
   ("Always mention opportunity cost.", "What else could the money buy?"),
   ("Consider targeting.", "Some benefit goes to people who would have bought anyway."),
   ("Compare with other policies.", "Information, regulation, direct provision.")],
  [("Subsidy", "A subsidy is a payment by the government that lowers producers' costs."),
   ("Merit good", "A subsidy may increase consumption of a merit good."),
   ("Opportunity cost", "The cost of a subsidy is the other spending given up."),
   ("Incidence", "The benefit of a subsidy is shared between consumers and producers."),
   ("Assess", "A subsidy is likely to be effective where demand is elastic and cost is the barrier.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + INCJS + '''
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A subsidy shifts supply down, lowering the price consumers pay and raising the price producers receive">${incPlot(70, 640, 0.8, 0.8, -10, 1, "")}</svg>`;
function s1Draw(s) { const e = incEq(0.8, 0.8, -10); return incPlot(70, 640, 0.8, 0.8, -10, s.k, "") + (s.v > 0 ? SV.text(380, 292, "Cost to government = $10 × " + Lib.fmtN(e.q, 1) + " = $" + Lib.fmtN(10 * e.q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.v) }) : ""); }
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A subsidy of $10 per unit", base: { k: 0, v: 0 }, draw: s1Draw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> The market is in equilibrium at $50 and 50 units.", s: { k: 0, v: 0 } },
  { cap: "<b>A subsidy of $10 per unit</b> lowers each firm's costs. The supply curve shifts down (right) by $10.", s: { k: 1, v: 0 } },
  { cap: "<b>The new equilibrium.</b> Consumers pay $45 (down $5). Producers receive $45 + $10 = $55 (up $5). Quantity rises to 56.25. Here the benefit is shared equally.", s: { k: 1, v: 0 } },
  { cap: "<b>The cost</b> to the government is the subsidy per unit times the quantity: the rectangle between the two prices, over the new quantity.", s: { k: 1, v: 1 } },
] });
function sTwo(s) { return incPlot(30, 330, 1.2, 0.6, -10, s.k, "Inelastic demand (steep)") + incPlot(400, 330, 0.4, 0.6, -10, s.k, "Elastic demand (flat)") + (s.k > 0.5 ? SV.text(195, 288, "Quantity " + Lib.fmtN(incEq(1.2, 0.6, -10).q, 1) + ", cost $" + Lib.fmtN(10 * incEq(1.2, 0.6, -10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.k) }) + SV.text(565, 288, "Quantity " + Lib.fmtN(incEq(0.4, 0.6, -10).q, 1) + ", cost $" + Lib.fmtN(10 * incEq(0.4, 0.6, -10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.k) }) : ""); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same subsidy with inelastic demand and with elastic demand, and the cost of each">${sTwo({ k: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The same subsidy with inelastic and with elastic demand", base: { k: 0 }, draw: sTwo, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Two markets</b> with the same supply curve. Demand is steep (inelastic) on the left and flat (elastic) on the right.", s: { k: 0 } },
  { cap: "<b>The same $10 subsidy.</b> With <b>elastic</b> demand the price fall brings a bigger rise in quantity (60 units), so the subsidy costs more ($600) and does more to raise consumption. With <b>inelastic</b> demand quantity rises less (55.6 units), the cost is $556, and consumers gain more per unit.", s: { k: 1 } },
] });

function labS() {
  if (!$("#sb") || !$("#dm") || !$("#sn")) return;
  const t = -(+$("#sb").value), m = +$("#dm").value / 10, n = +$("#sn").value / 10, e = incEq(m, n, t), cost = -t * e.q;
  $("#r1").textContent = "$" + Lib.fmtN(e.pc, 1) + " (" + Lib.fmtN(e.pc - 50, 1) + ")"; $("#r2").textContent = "$" + Lib.fmtN(e.pp, 1) + " (+" + Lib.fmtN(e.pp - 50, 1) + ")"; $("#r3").textContent = "$" + Lib.fmtN(cost, 0);
  $("#rv").textContent = t === 0 ? "No subsidy, so nothing changes." : `Of the $${-t} subsidy per unit, consumers gain $${Lib.fmtN(50 - e.pc, 1)} (${Lib.fmtN(e.sc * 100, 0)}%) and producers $${Lib.fmtN(e.pp - 50, 1)} (${Lib.fmtN((1 - e.sc) * 100, 0)}%). Quantity rises from 50 to ${Lib.fmtN(e.q, 1)} and the government pays $${Lib.fmtN(cost, 0)}. ${m > n ? "Demand is steeper than supply, so consumers gain more." : m < n ? "Supply is steeper than demand, so producers gain more." : "The gain is shared equally."}`;
  $("#labA").innerHTML = incPlot(70, 640, m, n, t, 1, "");
}
Lib.slider($("#g1"), { id: "sb", label: "Subsidy per unit, $ ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labS });
Lib.slider($("#g2"), { id: "dm", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 8, fmt: (v) => v, onInput: labS });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = flat and elastic, 10 = steep and inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labS });
labS();

function labW() {
  if (!$("#eb") || !$("#sx")) return;
  const E = +$("#eb").value, s = +$("#sx").value, k = 1.6, dq = s / k, cost = s * (50 + dq), net = dq * (E - s / 2);
  $("#t1").textContent = Lib.fmtN(dq, 1); $("#t2").textContent = "$" + Lib.fmtN(cost, 0); $("#t3").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 1);
  $("#tv").textContent = s === 0 ? "No subsidy, so there is no extra consumption and no gain. The best subsidy equals the external benefit, $" + E + "." : `The subsidy raises output by ${Lib.fmtN(dq, 1)} units. Each extra unit brings an external benefit of $${E}, but costs the government a subsidy of $${s} on top of private gains, so the net gain is ${Lib.fmtN(net, 1)}. ${s === E ? "The subsidy equals the external benefit, so the net gain is at its maximum." : s > E ? "The subsidy is larger than the external benefit, so too much is paid and the net gain falls." : "The subsidy is smaller than the external benefit, so it could be raised for a bigger net gain."}`;
  const X = (v) => 40 + v * 17, Y = (v) => 250 - v * 1; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 40) + SV.text(400, 272, "Subsidy per unit", "sm", { "text-anchor": "end" }) + SV.text(46, 36, "Net gain", "sm"), pts = [];
  for (let v = 0; v <= 20; v += 1) pts.push([X(v), Math.min(290, 250 - (v / k) * (E - v / 2) * 2)]);
  o += SV.path("M" + pts.map((p) => p.join(",")).join(" L"), "c2", { fill: "none", "stroke-width": 3 }) + SV.circle(X(s), 250 - dq * (E - s / 2) * 2, 7, "dot3") + SV.line(X(E), 250, X(E), 250 - (E / k) * (E / 2) * 2, "dash") + SV.text(X(E), 268, "best = " + E, "sm", { "text-anchor": "middle" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "eb", label: "External benefit per unit, $ ", min: 4, max: 16, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labW });
Lib.slider($("#g5"), { id: "sx", label: "Subsidy per unit, $ ", min: 0, max: 20, step: 1, value: 6, fmt: (v) => "$" + v, onInput: labW });
labW();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What does a subsidy do?", ["Shifts supply right", "Shifts supply left", "Neither"],
  [("A grant lowers farmers' costs", 0), ("An indirect tax on the good", 1), ("A government payment per unit to producers", 0), ("A fall in the price of the good itself", 2), ("Cheaper inputs for producers", 0), ("A rise in wages", 1), ("Removing an existing subsidy", 1), ("Advertising by consumers' groups", 2)],
  "A subsidy lowers costs and shifts supply right. Removing it shifts supply left.") + MATCH([
  ["Subsidy", "Payment to producers that lowers costs"],
  ["Cost of a subsidy", "Subsidy per unit × quantity sold"],
  ["Merit good", "Under-consumed good that a subsidy may help"],
  ["Opportunity cost", "Other spending given up to pay for the subsidy"],
  ["Poor targeting", "Benefits go to people who would have bought anyway"],
  ["Transfer payment", "Payment to individuals with no output in return"]]) + ORDER(
  "Put the effects of a subsidy in order.",
  ["The government pays a subsidy per unit", "Producers' costs fall and supply shifts to the right", "The price paid by consumers falls", "Quantity sold rises", "Consumer and producer surplus rise but the government bears the cost"],
  "Subsidy, supply shifts right, price falls, quantity rises.") + CALC([
  {"q": "A subsidy of $4 per unit lowers the price from $20 to $17 and quantity rises from 100 to 120. What is the cost to the government ($)?", "a": 480, "unit": "$", "tol": 1, "hint": "4 × 120.", "sol": "<b>$480</b>."},
  {"q": "How much per unit do consumers gain?", "a": 3, "unit": "$", "tol": 0.05, "hint": "20 − 17.", "sol": "<b>$3</b>."},
  {"q": "How much per unit do producers gain?", "a": 1, "unit": "$", "tol": 0.05, "hint": "Subsidy minus the consumers' gain: 4 − 3.", "sol": "<b>$1</b>."},
  {"q": "What percentage of the subsidy goes to consumers?", "a": 75, "unit": "%", "tol": 0.5, "hint": "3 ÷ 4.", "sol": "<b>75%</b>."}]) + MCQ([
  ("A subsidy shifts the supply curve:", ["To the right", "To the left", "Not at all", "Vertically upward only"], 0, "Costs fall."),
  ("A subsidy to producers will usually:", ["Lower the price and raise quantity", "Raise the price and lower quantity", "Raise both", "Lower both"], 0, "Supply moves right."),
  ("The cost of a subsidy rises if demand is more:", ["Elastic", "Inelastic", "Unit inelastic", "Fixed"], 0, "Quantity rises more."),
  ("The opportunity cost of a subsidy is:", ["The other spending or tax cuts forgone", "The price fall", "The rise in quantity", "The producer's profit"], 0, "Best alternative given up."),
  ("A subsidy is most justified for a:", ["Merit good with external benefits", "Demerit good", "Free good", "Good with no substitutes"], 0, "To correct under-consumption.")
], "qz1") + CARDS([
  ("Subsidy", "Payment that lowers costs."),
  ("Supply", "Shifts right."),
  ("Price", "Consumers pay less."),
  ("Quantity", "Rises."),
  ("Cost", "Subsidy × quantity."),
  ("Elastic demand", "Bigger rise and cost."),
  ("Opportunity cost", "Other spending lost."),
  ("Merit goods", "Main reason to subsidise.")]) + MCQ(mc_exam)

build("as32", "as-subsidies", "Subsidies: Impact and Incidence", EY,
  "3.2.2: how a subsidy shifts supply, who gains, the cost to the government and the role of elasticity, with the advantages and disadvantages. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
