"""AS syllabus 3.2.1 Impact and incidence of specific indirect taxes. Run: python3 tools/artifact-kit/mk_as31.py"""
from asx import *
EY = EYAS("3.2.1")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An <b class="kw">indirect tax</b> is a tax on spending, collected by firms but paid partly or wholly by consumers; a <b class="kw">specific tax</b> is a fixed sum per unit, while an <b>ad valorem</b> tax is a percentage of the price. A tax raises firms' costs, so the <b>supply curve shifts to the left (up)</b> by the amount of the tax, which <b>raises the price and reduces the quantity</b> traded. The <b class="kw">incidence</b> of the tax is who actually bears it: consumers bear the rise in the price they pay, and producers bear the rest of the tax out of the price they keep, with the split depending on the <b>price elasticity of demand and supply</b>. The government gains <b>tax revenue</b> (tax per unit times the quantity sold after the tax), but there is a loss of consumer and producer surplus and some quantity is no longer traded.</p></div>

  <h2>1 · Impact of a specific tax (3.2.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>The vertical gap between the old supply curve and the new one is the <b>tax per unit</b>.</li>
    <li>The <b>price consumers pay</b> rises (but by less than the tax); the <b>price producers keep</b> (price paid minus tax) falls; <b>quantity</b> falls.</li>
    <li><b>Tax revenue = tax per unit × quantity sold after the tax.</b></li>
    <li><b>Specific vs ad valorem:</b> a specific tax shifts supply <b>parallel</b>; an ad valorem tax makes the new curve <b>pivot</b>, getting further from the old curve at higher prices.</li>
  </ul>

  <h2>2 · Incidence and elasticity</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Case</th><th>Who bears more of the tax</th></tr>
    <tr><td><b>Demand inelastic</b> (steep), supply elastic</td><td>Consumers: price rises by almost the whole tax, quantity falls little</td></tr>
    <tr><td><b>Demand elastic</b> (flat), supply inelastic</td><td>Producers: they must cut the price they receive, or lose sales</td></tr>
    <tr><td><b>Demand perfectly inelastic</b></td><td>Consumers bear all of it</td></tr>
    <tr><td><b>Demand perfectly elastic</b> (or supply perfectly inelastic)</td><td>Producers bear all of it</td></tr>
  </table></div>
  <ul>
    <li>Consumer share of the tax = <b>PES ÷ (PES + PED)</b> in size terms; the more inelastic your side, the more of the tax you bear.</li>
    <li><b>Why governments use them:</b> raise revenue; discourage demerit goods (tobacco, alcohol, sugary drinks); make users pay for external costs.</li>
    <li><b>Limitations:</b> if demand is inelastic the tax may <b>not reduce consumption</b> much; they can be <b>regressive</b> (take a bigger share of low incomes); high taxes may cause <b>black markets or avoidance</b>; the correct tax size is hard to estimate; producers' jobs may be hit.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Draw <b>both</b> supply curves, show the tax as a vertical gap, and label the <b>price paid by consumers</b>, the <b>price received by producers</b>, and the <b>tax revenue rectangle</b>. In evaluation, discuss <b>elasticity</b> and say whether the aim is revenue or reducing consumption.</div>
'''

watch = '''
  <h2>1 · A tax shifts supply</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Who pays? Inelastic vs elastic demand</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · Set the tax</h2>
  <p>Change the size of the tax and the steepness of demand and supply. The blue box is what consumers pay, the green box what producers bear.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Consumers pay</small><strong id="r1"></strong></div><div><small>Producers keep</small><strong id="r2"></strong></div><div><small>Tax revenue</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with an indirect tax and the incidence shaded"></svg></div></div></div>

  <h2>Lab 2 · Specific or ad valorem?</h2>
  <p>Compare a specific tax with an ad valorem tax that collects the same amount at a price of $50.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div>
    <div class="readout"><div><small>Specific tax</small><strong id="t1"></strong></div><div><small>Ad valorem rate</small><strong id="t2"></strong></div><div><small>Tax at $80</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Supply curve after a specific tax and after an ad valorem tax"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Who bears more of the tax?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a tax in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Fuel duty", "A fixed amount of tax is added to each litre of petrol. Demand for fuel is inelastic in the short run, so most of the tax is passed on to drivers and consumption falls only a little. The government collects large revenue.", "a specific tax and the incidence on consumers.") +
rw("A sugar tax", "A tax on sugary drinks aims to cut over-consumption of a demerit good. Producers may absorb some of it by changing recipes or cutting margins, and prices of the highest-sugar drinks rise.", "using an indirect tax to correct information failure, and incidence shared with producers.") +
rw("Value added tax", "A percentage added to the price of most goods. It is an ad valorem tax, so the amount of tax rises with the price. It raises a lot of revenue but takes a larger share of low incomes, so it can be regressive.", "ad valorem tax and its fairness.") +
rw("Tax on a luxury good", "A tax on yachts is paid mostly by sellers if buyers can easily switch to other luxuries (elastic demand). Fewer boats are sold, so producers lose volume as well as price.", "elastic demand and a greater producer share.")
)

mc_exam = [
  mcq("m20_12", 17, "Which type of tax is the 15% sales tax levied in South Africa?", ["ad valorem direct", "ad valorem indirect", "specific direct", "specific indirect"], 1, "A percentage of the price is ad valorem, and a sales tax on spending is indirect."),
  mcq("s20_11", 14, "A specific tax is imposed on a product for which the elasticity of supply is zero. Which statement is correct?", ["The burden of this tax will fall entirely on consumers", "The burden of this tax will fall entirely on suppliers", "The burden of this tax will fall mainly on consumers", "The burden of this tax will fall mainly on suppliers"], 1, "If supply is perfectly inelastic, the price cannot rise, so producers bear all of the tax."),
  mcq("s20_12", 12, "The supply curve of a product passes through the origin. The government imposes a specific indirect tax of $5 on the product. How will the price elasticity of supply of the product change?", ["from elastic to inelastic", "from inelastic to elastic", "from inelastic to unitary", "from unitary to elastic"], 3, "A curve through the origin has unit elasticity. A parallel shift up by $5 gives a positive price intercept, so supply becomes elastic."),
  mcq("s21_12", 17, "The table shows sources of government revenue: sale of government assets 100, tax on self employed 1000, carbon tax on goods produced 100, corporate taxes 500, capital gains tax 100, goods and services tax 1000, air passenger tax 100 ($ billions). What is the total amount of tax revenue raised by indirect taxes?", ["$1,200 billion", "$1,300 billion", "$1,400 billion", "$1,600 billion"], 0, "Indirect taxes are the carbon tax, goods and services tax and air passenger tax: 100 + 1000 + 100."),
  mcq("s20_11", 9, "An indirect tax is imposed on a product in a competitive market. Under which circumstances would the value of the consumer surplus be most likely to remain unchanged?", ["New substitutes are developed for the product and production costs rise", "Some producers merge so there is less competition in the market", "The product is an inferior good, consumer incomes increase and production costs rise", "The product is a normal good, consumer incomes increase and production costs fall"], 3, "Higher demand raises consumer surplus, while a tax lowers it, so the effects can offset. Falling costs raise supply as well.")
]

exam = exam_page("indirect taxes and their incidence",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Taxes and incidence are in an 8 or 12 mark Paper 2 part most years, usually with a diagram and elasticity. Reworded past questions are below, with five Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "1", "Feb/March 2024 (22) Q2(a)"), ("Essay parts, 12 marks", "2", "Oct/Nov 2020 (23) Q2(b); Oct/Nov 2020 (22) Q2(b)"), ("Data response, 2 marks", "1", "May/June 2020 (23) Q1(b)"), ("Multiple choice (Paper 1)", "5 shown below", "2020 to 2025")],
  [
  eq(P("m24_22", "2(a)"), "8 marks", "With the help of a demand and supply diagram, explain how the introduction of an indirect tax affects equilibrium in a market and consider the extent to which the incidence of the tax will fall on the consumer.",
     ["Knowledge (up to 3): an accurate definition of an indirect tax (1); an accurate diagram with labelled axes and equilibrium price and quantity (1); understanding that indirect taxes are used to discourage consumption of demerit goods (1).",
      "Analysis (up to 3): the diagram shows an indirect tax shifting the supply curve to the left (1), raising the price to the consumer (1) and reducing the quantity demanded (1).",
      "Evaluation (up to 2): the incidence on the consumer depends on the price elasticity of demand: the more inelastic demand, the more of the tax is passed to the consumer (1), and a justified conclusion (1)."],
     "Define the tax. Diagram: supply left, price up, quantity down. Evaluate: incidence depends on PED.",
     [[("k", "An indirect tax is a tax on spending, such as VAT or a duty on cigarettes, collected by the seller but ultimately paid by consumers or producers. On a diagram, the original equilibrium is where demand meets supply at P1 and Q1. Governments often use indirect taxes to discourage consumption of demerit goods.")], [("n", "The tax raises costs by a fixed amount for each unit, so the supply curve shifts to the left. The equilibrium price paid by consumers rises to P2 and the quantity falls to Q2.")], [("e", "How much of the tax falls on consumers depends on the price elasticity of demand. If demand is inelastic, consumers have few substitutes, so the price rises by nearly the whole tax and consumers bear most of it. If demand is elastic, producers absorb more of it. So the incidence is likely to fall mainly on consumers for goods such as cigarettes, but not for goods with close substitutes.")]]),
  eq(P("w20_23", "2(b)"), "12 marks", "Discuss whether the incidence of an indirect tax on a product always affects its consumers more than its producers.",
     ["Analysis (up to 8): an explanation of the incidence of an indirect tax and how it affects consumers in terms of the price paid and the quantity they buy (up to 4); how it affects producers in terms of the price they receive, revenue and sales (up to 4). The incidence depends on the price elasticity of demand and supply: the more inelastic PED, the greater the burden on consumers.",
      "Evaluation (up to 4): judgement on whether consumers always bear more, supported by consideration of elasticity values, and a conclusion (1)."],
     "Incidence depends on elasticity. Inelastic demand: consumers. Elastic demand or inelastic supply: producers. Judge: not always.",
     [[("n", "The incidence of an indirect tax is the way the burden is divided between consumers, through a higher price, and producers, through a lower price kept after the tax. The tax shifts supply to the left and raises the price, but by less than the tax. If demand is inelastic, such as for fuel, the price rises by nearly the whole tax and quantity falls little, so consumers bear most of it. If demand is elastic, or supply inelastic, consumers can switch away, so the price rises little and producers absorb more, and lose sales.")], [("e", "So consumers do not always bear more of the tax. It depends on the relative elasticities of demand and supply and on how quickly firms can adjust. The tax is more likely to fall on consumers for necessities and addictive goods, and on producers where there are close substitutes.")]]),
  eq(P("s20_23", "1(b)"), "2 marks", "Distinguish between an ad valorem tax and a specific tax.",
     ["An ad valorem tax is a proportion or percentage of the price, such as VAT (1).", "A specific tax is a fixed amount per unit, such as a duty on fuel or alcohol (1)."],
     "Percentage of price versus fixed amount per unit.",
     [[("k", "An ad valorem tax is a percentage of the price, so the tax rises with the price, as VAT does. A specific tax is a fixed sum on each unit sold, such as a duty of a set amount per litre of fuel.")]]),
  eq(P("w20_22", "2(b)"), "12 marks", "If the cost of a subsidy is to be paid from tax revenues, discuss whether the revenue should be raised through direct taxes or indirect taxes.",
     ["Analysis (up to 8): how direct taxes (such as income tax) work, their effect on incentives and income distribution, and the problems of collecting them (up to 4); how indirect taxes work, their effect on prices and on different income groups, and their problems (up to 4). Indicative content may include progressive and regressive effects, ease of collection and effect on consumption.",
      "Evaluation (up to 4): judgement on which tax is more suitable, such as using equity, efficiency and the purpose of the subsidy, with a conclusion."],
     "Direct tax: progressive, equity, disincentive. Indirect tax: easy to collect, regressive. Judge: a mix, depending on aims.",
     [[("n", "Direct taxes, such as income tax, can be progressive, taking a larger share from high earners, which is fairer, and they may be a stable source of revenue. But they may reduce the incentive to work and can be avoided. Indirect taxes are easy to collect and can be set to discourage demerit goods, and spending can be hard to hide. But they are regressive, taking a larger share of low incomes, and raise prices, which could reduce spending.")], [("e", "A mix is probably best. If the subsidy helps low-income households, as with vaccinations, funding it mainly from progressive direct taxes seems fairer, though indirect taxes might be preferred if the aim is to raise revenue quickly with fewer disincentives to work.")]])
  ],
  )

tips = tips_html(
  [("Draw the tax as a vertical gap.", "Between the old and new supply curves."),
   ("Label three things.", "Price paid by consumers, price received by producers, tax revenue."),
   ("Say the price rises by less than the tax.", "Unless demand is perfectly inelastic."),
   ("Use elasticity for incidence.", "More inelastic demand means a bigger consumer share."),
   ("Revenue = tax × quantity after.", "Use the new quantity, not the old one."),
   ("Match tax to aim.", "Revenue: inelastic demand works. Cutting use: needs elastic demand."),
   ("Mention fairness.", "Indirect taxes can be regressive.")],
  [("Indirect tax", "An indirect tax is a tax on spending that raises firms' costs."),
   ("Incidence", "The incidence of a tax is the way the burden is shared between consumers and producers."),
   ("Specific tax", "A specific tax is a fixed amount per unit."),
   ("Ad valorem tax", "An ad valorem tax is a percentage of the price."),
   ("Elasticity", "The incidence on consumers depends on the price elasticity of demand.")],
  [CW["define"], CW["distinguish"] if "distinguish" in CW else CW["explain"], CW["explain"], CW["consider"], CW["discuss"] if "discuss" in CW else CW["assess"]]) + FC

js = SDJS + INCJS + '''
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="An indirect tax shifts supply up, raising the price consumers pay and lowering the price producers keep">${incPlot(70, 640, 0.8, 0.8, 10, 1, "")}</svg>`;
function t1Draw(s) { return incPlot(70, 640, 0.8, 0.8, 10, s.k, "") + (s.v > 0 ? SV.text(380, 292, "Tax revenue = $10 × " + Lib.fmtN(incEq(0.8, 0.8, 10).q, 1) + " = $" + Lib.fmtN(10 * incEq(0.8, 0.8, 10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.v) }) : ""); }
Lib.stepper($("#stT"), { w: 760, h: 300, label: "An indirect tax of $10 per unit", base: { k: 0, v: 0 }, draw: t1Draw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before the tax.</b> The market is in equilibrium at $50 and 50 units.", s: { k: 0, v: 0 } },
  { cap: "<b>The tax raises each firm's cost by $10.</b> The supply curve shifts up (left) by $10: the vertical gap is the tax.", s: { k: 1, v: 0 } },
  { cap: "<b>The new equilibrium.</b> Consumers now pay $55 (up $5). Producers receive $55 − $10 = $45 (down $5). Quantity falls to 43.75. Each side bears half the tax here.", s: { k: 1, v: 0 } },
  { cap: "<b>Tax revenue</b> is the tax per unit times the quantity sold after the tax. The blue box is the consumers' share, the green box the producers' share.", s: { k: 1, v: 1 } },
] });

function incTwo(s) { return incPlot(30, 330, 1.2, 0.6, 10, s.k, "Inelastic demand (steep)") + incPlot(400, 330, 0.4, 0.6, 10, s.k, "Elastic demand (flat)") + (s.k > 0.5 ? SV.text(195, 288, "Consumers bear " + Lib.fmtN(incEq(1.2, 0.6, 10).sc * 100, 0) + "%", "lbl bd", { "text-anchor": "middle", ...op(s.k) }) + SV.text(565, 288, "Consumers bear " + Lib.fmtN(incEq(0.4, 0.6, 10).sc * 100, 0) + "%", "lbl bd", { "text-anchor": "middle", ...op(s.k) }) : ""); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same tax on a market with inelastic demand and on one with elastic demand">${incTwo({ k: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "The same tax with inelastic and with elastic demand", base: { k: 0 }, draw: incTwo, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Two markets</b> with the same supply curve and equilibrium. Demand is steep (inelastic) on the left and flat (elastic) on the right.", s: { k: 0 } },
  { cap: "<b>The same $10 tax.</b> With <b>inelastic</b> demand, consumers keep buying, so the price rises by about two thirds of the tax and the quantity falls little. With <b>elastic</b> demand the price rises only by about 40% of the tax and the quantity falls more.", s: { k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#tx") || !$("#dm") || !$("#sn")) return;
  const t = +$("#tx").value, m = +$("#dm").value / 10, n = +$("#sn").value / 10, e = incEq(m, n, t), rev = t * e.q;
  $("#r1").textContent = "$" + Lib.fmtN(e.pc, 1) + " (+" + Lib.fmtN(e.pc - 50, 1) + ")"; $("#r2").textContent = "$" + Lib.fmtN(e.pp, 1) + " (" + Lib.fmtN(e.pp - 50, 1) + ")"; $("#r3").textContent = "$" + Lib.fmtN(rev, 0);
  $("#rv").textContent = t === 0 ? "No tax, so nothing changes." : `Of the $${t} tax, consumers bear $${Lib.fmtN(e.pc - 50, 1)} (${Lib.fmtN(e.sc * 100, 0)}%) and producers $${Lib.fmtN(50 - e.pp, 1)} (${Lib.fmtN((1 - e.sc) * 100, 0)}%). Quantity falls from 50 to ${Lib.fmtN(e.q, 1)} and the government raises $${Lib.fmtN(rev, 0)}. ${m > n ? "Demand is steeper than supply (more inelastic), so consumers bear more." : m < n ? "Supply is steeper than demand (more inelastic), so producers bear more." : "Demand and supply are equally steep, so the burden is shared equally."}`;
  $("#labA").innerHTML = incPlot(70, 640, m, n, t, 1, "");
}
Lib.slider($("#g1"), { id: "tx", label: "Tax per unit, $ ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g2"), { id: "dm", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 8, fmt: (v) => v, onInput: labT });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = flat and elastic, 10 = steep and inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labV() {
  if (!$("#st")) return;
  const t = +$("#st").value, r = t / 50 * 100, X = (q) => 70 + q * 6, Y = (p) => 270 - p * 2.2; let o = SV.line(70, 270, 700, 270) + SV.line(70, 270, 70, 40);
  o += SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3, ...op(0.45) }) + SV.line(X(0), Y(10 + t), X(100), Y(90 + t), "c3", { "stroke-width": 3 }) + SV.line(X(0), Y(10 * (1 + r / 100)), X(100), Y(90 * (1 + r / 100)), "c2", { "stroke-width": 3, "stroke-dasharray": "6 4" });
  o += tag(X(100) + 4, Y(90), "S", "c1", 0.6) + tag(X(100) + 4, Y(90 + t) - 4, "S + specific", "c3") + tag(X(100) + 4, Y(90 * (1 + r / 100)) + 14, "S + ad valorem", "c2");
  $("#t1").textContent = "$" + t; $("#t2").textContent = Lib.fmtN(r, 0) + "%"; $("#t3").textContent = "Specific $" + t + " vs ad valorem $" + Lib.fmtN(80 * r / 100, 1);
  $("#tv").textContent = `A specific tax of $${t} is the same at every price, so the supply curve moves up in parallel. An ad valorem tax of ${Lib.fmtN(r, 0)}% raises the same amount at $50 but takes $${Lib.fmtN(80 * r / 100, 1)} at $80, so the new curve pivots and gets further from the old one as price rises.`;
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "st", label: "Specific tax, $ (equal to an ad valorem tax at a price of $50) ", min: 2, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labV });
labV();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Who bears more of the tax?", ["Consumers", "Producers"],
  [("Demand is inelastic and supply is elastic", 0), ("Demand is elastic and supply is inelastic", 1), ("Cigarettes (addictive, few substitutes)", 0), ("A luxury good with many substitutes", 1), ("Demand is perfectly inelastic", 0), ("Supply is perfectly inelastic", 1), ("Petrol in the short run", 0), ("A product facing close competitors", 1)],
  "The side with the less elastic curve bears the larger share of the tax.") + MATCH([
  ["Indirect tax", "A tax on spending that raises firms' costs"],
  ["Specific tax", "A fixed amount per unit"],
  ["Ad valorem tax", "A percentage of the price"],
  ["Incidence", "How the burden of a tax is shared"],
  ["Tax revenue", "Tax per unit × quantity sold after the tax"],
  ["Regressive tax", "Takes a larger share of low incomes"]]) + ORDER(
  "Put the effects of an indirect tax in order.",
  ["The government imposes a tax per unit", "The supply curve shifts to the left", "The price paid by consumers rises", "The quantity traded falls", "The government collects tax revenue and the burden is shared by elasticity"],
  "Tax, supply shifts, price up, quantity down, revenue.") + CALC([
  {"q": "A tax of $3 per unit raises the price from $40 to $42. How much of the tax per unit is paid by consumers?", "a": 2, "unit": "$", "tol": 0.05, "hint": "New price minus old price.", "sol": "<b>$2</b> per unit."},
  {"q": "In the same example, how much per unit is borne by producers?", "a": 1, "unit": "$", "tol": 0.05, "hint": "3 − 2.", "sol": "<b>$1</b> per unit."},
  {"q": "Quantity falls from 100 to 90 units. What is the tax revenue ($)?", "a": 270, "unit": "$", "tol": 1, "hint": "3 × 90.", "sol": "<b>$270</b>."},
  {"q": "What percentage of the tax is borne by consumers?", "a": 66.7, "unit": "%", "tol": 0.5, "hint": "2 ÷ 3.", "sol": "<b>66.7%</b>."}]) + MCQ([
  ("A specific tax is:", ["A fixed amount per unit", "A percentage of the price", "A tax on income", "A tax on profits only"], 0, "Per unit."),
  ("An indirect tax shifts the supply curve:", ["To the left", "To the right", "Not at all", "To a vertical line"], 0, "Costs rise."),
  ("Consumers bear most of a tax when demand is:", ["Inelastic", "Elastic", "Unit elastic only", "Perfectly elastic"], 0, "They have few alternatives."),
  ("The price consumers pay after a tax rises by:", ["Less than the tax, unless demand is perfectly inelastic", "More than the tax", "Exactly the tax always", "Nothing"], 0, "The burden is shared."),
  ("Tax revenue equals:", ["Tax per unit × quantity after the tax", "Tax per unit × quantity before the tax", "Price × quantity", "Consumer surplus"], 0, "Use the new quantity.")
], "qz1") + CARDS([
  ("Indirect tax", "Tax on spending; shifts supply left."),
  ("Specific", "Fixed sum per unit."),
  ("Ad valorem", "Percentage of price."),
  ("Incidence", "Who bears the tax."),
  ("Inelastic demand", "Consumers bear more."),
  ("Revenue", "Tax × new quantity."),
  ("Demerit goods", "Taxed to cut consumption."),
  ("Regressive", "Hits low incomes harder.")]) + MCQ(mc_exam)

build("as31", "as-indirect-taxes", "Indirect Taxes: Impact and Incidence", EY,
  "3.2.1: specific and ad valorem indirect taxes, their effect on price and quantity, incidence and elasticity, and tax revenue. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
