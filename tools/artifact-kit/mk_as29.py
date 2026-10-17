"""AS syllabus 2.2.2 Income elasticity of demand. Run: python3 tools/artifact-kit/mk_as29.py"""
from as6k import *
EY = EYAS("2.2.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Income elasticity of demand (YED)</b> measures how responsive demand is to a change in income: <b>YED = % change in quantity demanded ÷ % change in income</b>. The <b>sign</b> classifies the good: <b>positive</b> for <b class="kw">normal goods</b> (demand rises as income rises) and <b>negative</b> for <b class="kw">inferior goods</b> (demand falls as income rises). The <b>size</b> shows how strongly: between 0 and 1 the good is a <b>necessity</b> (demand rises by a smaller percentage than income), and above 1 it is a <b>luxury</b> or <b>superior good</b> (demand rises by a bigger percentage). YED helps businesses forecast sales over the <b>business cycle</b> and during <b>economic growth or recession</b>, and plan which products to expand.</p></div>

  <h2>1 · Sign and size</h2>
  <div class="tw"><table class="t">
    <tr><th>YED</th><th>Type of good</th><th>Income rises 10%</th><th>Example</th></tr>
    <tr><td>Negative</td><td>Inferior good</td><td>Demand falls</td><td>Basic own-brand goods, bus travel for some</td></tr>
    <tr><td>0 to +1</td><td>Normal necessity</td><td>Demand rises by less than 10%</td><td>Basic food, electricity</td></tr>
    <tr><td>Above +1</td><td>Normal luxury (superior)</td><td>Demand rises by more than 10%</td><td>Foreign holidays, designer goods</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>

  <h2>2 · Demand curves and income</h2>
  <ul>
    <li>When income <b>rises</b>, the demand curve for a <b>normal</b> good <b>shifts right</b>, raising equilibrium price and quantity; for an <b>inferior</b> good it <b>shifts left</b>, lowering them.</li>
    <li>When income <b>falls</b>, the effects are reversed: a normal good's demand shifts left, an inferior good's shifts right.</li>
    <li>A good can change category: demand for a good may be a luxury at low incomes but a necessity or even inferior at high incomes.</li>
  </ul>

  <h2>3 · Why it matters</h2>
  <ul>
    <li><b>Planning:</b> firms selling income-elastic goods (cars, holidays) are hit hard in a recession and gain most in a boom; those selling necessities are more stable.</li>
    <li><b>Product mix:</b> as an economy develops, demand shifts towards luxuries and services and away from inferior goods.</li>
    <li><b>Government:</b> shows how tax and benefit changes affect spending on different goods.</li>
    <li><b>Limits:</b> estimates may be inaccurate, and other factors (tastes, prices) change at the same time.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Use the <b>sign</b> to classify the good and the <b>size</b> to say necessity or luxury. Give an <b>example</b>, and say that the classification may change with income, place and time.</div>
'''

watch = '''
  <h2>1 · A rise in income and a normal good</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · A rise in income and an inferior good</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Income and demand</h2>
  <p>Choose a YED and an income change to see the change in demand and the type of good.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Change in quantity demanded</small><strong id="r1"></strong></div><div><small>Type of good</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 220" role="img" aria-label="Bars showing the change in income and in quantity demanded"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Classify the good", "Choose a good to see its likely YED sign and size, and how it behaves in a boom and a recession.", ["Likely YED", "In a boom", "In a recession"])

practise = practise_html("Normal or inferior?", "Match the term to its description", "Put the effects of a rise in income on a normal good in order")

real = RWNOTE + (
rw("Budget supermarkets in a recession", "When incomes fall, some households switch from branded to own-brand goods. Demand for those own-brand goods rises as incomes fall, so they behave as inferior goods.", "an inferior good.") +
rw("Foreign holidays", "As incomes rise, spending on foreign holidays tends to rise by a larger percentage. Travel firms may hire more in a boom and cut back sharply in a recession.", "a luxury with high YED.") +
rw("Basic foods", "Bread and rice are bought whatever the income level, so demand rises only slightly as incomes grow. YED is positive but low.", "a necessity.") +
rw("Cars in an expanding economy", "Car makers watch income growth closely. High YED means sales could grow quickly in a boom and fall quickly in a downturn, so they may plan production carefully.", "using YED for business planning.")
)

mc_exam = [
  mcq("s24_11", 10, "A firm calculates that the income elasticity of demand for its product is -3.0. What can be deduced from this information?", ["In a period of economic growth, its total revenue should increase.", "In a period of economic recession, its total revenue should increase.", "It has few substitutes so it should increase its price to increase total revenue.", "It has many substitutes so it should decrease price to increase total revenue."], 1, "A negative YED means an inferior good: demand rises when incomes fall."),
  mcq("m24_12", 7, "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X?", ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], 0, "YED negative: inferior; PED size 2.4: elastic; XED positive: substitute."),
  mcq("m22_12", 12, "What causes the demand curve for an inferior good to shift to the right?", ["a decrease in consumer incomes", "a decrease in income tax", "a decrease in the price of a substitute good", "a decrease in the price of the good"], 0, "Demand for an inferior good rises when incomes fall."),
  mcq("s20_13", 10, "Which combination of the classification of a good and market change will cause the demand curve for the good to shift right? (classification, market change)", ["inferior good, income decrease", "inferior good, price decrease", "normal good, income decrease", "normal good, price decrease"], 0, "A fall in income raises demand for an inferior good. A price change is a movement along the curve."),
  mcq("m20_12", 8, "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y)", ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], 2, "A normal good gains from higher income, and a fall in the price of a complement raises demand for X."),
  mcq("m21_12", 16, "The government redistributes income by raising the top rate of income tax and using the money raised to finance additional benefits to students and the unemployed. Under which conditions will total spending in the economy increase the most? (YED of top-rate taxpayers, YED of students and the unemployed)", [">1 and >1", ">1 and <1", "<1 and >1", "<1 and <1"], 2, "Spending falls little where taxpayers' YED is low and rises most where recipients' YED is high.")
]

exam = exam_page("income elasticity of demand",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). YED is a regular 8 mark Paper 2 part (formula, normal and inferior goods) and appears in 12 mark comparisons with PED or XED. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "5", "Feb/March 2024 (22) Q3(a); May/June 2024 (21) Q3(a); Oct/Nov 2020 (23) Q3(a); May/June 2022 (22) Q3(a); May/June 2023 (23) Q2(a)"), ("Essay parts, 12 marks", "2", "Oct/Nov 2022 (21) Q2(b); Oct/Nov 2020 (21) Q3(b)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2024")],
  [
  eq(P("m24_22", "3(a)"), "8 marks", "With the help of a formula, explain the meaning of income elasticity of demand and consider the extent to which a rise in income will increase the consumption of all goods and services.",
     ["Knowledge (up to 3): an accurate definition of YED (1), an accurate formula (1), and the difference between normal and inferior goods (1).",
      "Analysis (up to 3): normal goods have a positive value (1); uses a diagram (an upward-sloping income demand curve) or the formula to show why a rise in income increases consumption of such goods (1), justified with an example (1).",
      "Evaluation (up to 2): if the good is inferior, demand falls when income rises (1) as consumers switch to normal or luxury goods; the second mark is for a justified conclusion."],
     "Define and formula. Normal: positive, demand rises. Inferior: negative, demand falls. Conclude: not all goods rise.",
     [[("k", "Income elasticity of demand measures how responsive demand is to a change in income. It equals the percentage change in quantity demanded divided by the percentage change in income. Normal goods have a positive YED and inferior goods a negative one.")], [("n", "For a normal good such as foreign holidays, a rise in income raises demand, because consumers can afford more of them, so a positive YED shows that consumption increases as incomes rise.")], [("e", "Not all goods will rise. For an inferior good such as a basic own-brand product, a rise in income may lead consumers to switch to better goods, so consumption falls. Overall, a rise in income increases the consumption of normal goods but not of all goods and services.")]]),
  eq(P("s24_21", "3(a)"), "8 marks", "With the help of a formula, explain what is meant by the income elasticity of demand for a product and consider the extent to which demand for the product will always rise at the same rate as the income of its consumers.",
     ["Knowledge (up to 3): an accurate formula (1); clear knowledge of what YED means (1), including the difference between elastic and inelastic YED (1).",
      "Analysis (up to 3): this depends on the coefficient of YED (1), and analysis of the outcomes for a normal good, with a positive coefficient (1), and an inferior good, with a negative coefficient (1).",
      "Evaluation (up to 2): considered evaluation of the possible outcomes (1) leading to a valid conclusion (1)."],
     "Formula and meaning. Demand rises at the same rate only if YED = 1. Necessity: slower. Luxury: faster. Inferior: falls.",
     [[("k", "Income elasticity of demand equals the percentage change in quantity demanded divided by the percentage change in income. If its size is greater than one, demand is income elastic, and if it is between zero and one, it is income inelastic.")], [("n", "Demand rises at the same rate as income only if YED equals one. For a necessity, with a YED between zero and one, demand rises by a smaller percentage. For a luxury, with a YED above one, it rises by a larger percentage, and for an inferior good, with a negative YED, demand falls as income rises.")], [("e", "Demand will not always rise at the same rate as income. It is only likely for goods with a YED close to one, and the YED may change as incomes rise and tastes change.")]]),
  eq(P("w20_23", "3(a)"), "8 marks", "Explain what is meant by income elasticity of demand and, with the help of examples, show how it can be used to determine whether a good is normal or inferior.",
     ["Knowledge (up to 2): what YED measures (1) and the formula (1).",
      "Application (up to 6): normal goods have a positive sign (1) and why this comes about (1), justified with an example (1); inferior goods have a negative sign (1) and why this comes about (1), justified with an example (1)."],
     "What it measures and formula. Normal: positive sign, example. Inferior: negative sign, example.",
     [[("k", "Income elasticity of demand measures the responsiveness of demand to a change in income, and equals the percentage change in quantity demanded divided by the percentage change in income.")], [("n", "A normal good has a positive YED because consumers buy more of it as their income rises, for example restaurant meals. An inferior good has a negative YED because consumers buy less of it as their income rises, since they can afford better alternatives, for example low-cost own-brand food. The sign of the YED therefore shows whether a good is normal or inferior.")]]),
  eq(P("s22_22", "3(a)"), "8 marks", "With the help of diagrams, use the concept of income elasticity of demand to explain the impact of a fall in incomes on the equilibrium price and equilibrium quantity of a normal good and an inferior good.",
     ["Knowledge (up to 2): the meaning of income elasticity of demand (1) with an accurate formula (1).",
      "Application (up to 6): for a normal good, the meaning of a normal good (1), a diagram showing the demand curve shifting left (1) and a fall in equilibrium price and quantity (1); for an inferior good, the meaning (1), a separate diagram showing the demand curve shifting right (1) and a rise in equilibrium price and quantity (1). Two separate diagrams are required."],
     "YED definition and formula. Normal: income falls, D left, price and quantity fall. Inferior: D right, price and quantity rise. Two diagrams.",
     [[("k", "Income elasticity of demand is the percentage change in quantity demanded divided by the percentage change in income. A positive value means a normal good and a negative value an inferior good.")], [("n", "For a normal good, a fall in incomes reduces demand, so the demand curve shifts left on its own diagram, and the equilibrium price and quantity both fall. For an inferior good, the fall in incomes leads consumers to buy more of it in place of dearer goods, so the demand curve shifts right on a separate diagram, and the equilibrium price and quantity both rise.")]]),
  eq(P("s23_23", "2(a)"), "8 marks", "Explain, with the help of examples, the significance of the size and sign of the coefficient of income elasticity of demand for the classification of a good and consider how confident you are of this classification.",
     ["Knowledge (up to 3): what YED means (1), the formula (1), and the meaning of elastic and inelastic YED (1).",
      "Analysis (up to 3): the significance of the size and sign for normal goods with examples (1), necessity goods (1), inferior goods (1) and superior goods (1); a maximum of 1 mark for two types of good with no examples and 2 marks for three types with no examples.",
      "Evaluation (up to 2): a judgement on how confident one can be in the classification, with a conclusion."],
     "YED meaning and formula. Positive normal; 0 to 1 necessity; above 1 superior; negative inferior, with examples. Confidence: classification may change with income, place and time.",
     [[("k", "Income elasticity of demand is the percentage change in quantity demanded divided by the percentage change in income. It is income elastic if its size is above one and inelastic if between zero and one.")], [("n", "A positive sign means a normal good. If the size is between zero and one, such as basic food, it is a necessity, and if it is above one, such as foreign holidays, it is a superior good or luxury. A negative sign means an inferior good, such as own-brand budget goods, as demand falls when income rises.")], [("e", "The classification may not be fully reliable. A good could be a luxury at low incomes and a necessity at high incomes, and it can differ between countries and over time as tastes change, so the classification is only as confident as the data and period allow.")]]),
  eq(P("w22_21", "2(b)"), "12 marks", "Discuss whether knowledge of price elasticity of demand or income elasticity of demand would be of greater use to a business that produces cars.",
     ["Analysis (up to 8): the usefulness of PED to a car producer (up to 4), such as predicting the effect of a price change on revenue, and of YED (up to 4), such as the effect of changes in income, planning for the future and shifting production between basic and more expensive cars.",
      "Evaluation (up to 4): a judgement on whether PED or YED would be of greater use to a car business, with a conclusion (1 mark reserved)."],
     "PED: price changes and revenue. YED: growth and recession, product mix. Judge: PED for pricing, YED for planning; which is greater depends on the aim.",
     [[("n", "Knowledge of PED lets a car producer predict how a price change may affect demand and revenue: if demand is elastic, a price cut may raise revenue, and if inelastic, a price rise may. Knowledge of YED shows how demand could change when incomes change, so the firm can plan production for a boom or recession and decide whether to shift towards more expensive models as incomes rise.")], [("e", "Both are useful, but since cars are expensive and demand is likely to be income elastic, YED may be of greater use for long-term planning. PED may be more useful for short-term pricing, so the greater use may depend on the firm's aim and on the accuracy of the estimates.")]]),
  eq(P("w20_21", "3(b)"), "12 marks", "Explain the implications of price elasticity of demand and income elasticity of demand for business decisions. Discuss which measure is likely to be more useful to a business.",
     ["Analysis (up to 8): the usefulness of PED to a business (up to 4), for example showing how a price change may affect revenue, with the price of an elastic good reduced and an inelastic good raised, though substitutes, definition of the product, share of income and time must be considered; and of YED (up to 4), showing how a change in income may affect revenue, though whether the good is normal or inferior and the proportion of income must be considered.",
      "Evaluation (up to 4): a judgement on the relative extent to which PED and YED are useful, with a conclusion (1 mark reserved)."],
     "PED: pricing and revenue. YED: forecast sales as incomes change. Limits for each. Judge which helps more given the business.",
     [[("n", "PED helps a business decide whether to raise or cut prices to increase revenue, but it needs to take account of the availability of substitutes and the time period. YED helps a business forecast how sales may change as incomes change, so it can decide whether to expand or reduce production, but it must allow for whether the good is normal or inferior.")], [("e", "PED is likely to be more useful for short-term pricing decisions, while YED may be more useful for long-term planning, particularly in a growing economy. Which is more useful depends on the type of product and the firm's aims.")]])
  ],
  )

tips = tips_html(
  [("Formula first.", "% change in quantity demanded ÷ % change in income."),
   ("Sign classifies.", "Positive normal, negative inferior."),
   ("Size grades.", "0 to 1 necessity, above 1 luxury."),
   ("Give examples.", "Own-brand food, foreign holidays."),
   ("Use shifts.", "Normal: D right when income rises. Inferior: D left."),
   ("Business use.", "Forecasting in boom and recession."),
   ("Evaluate.", "Estimates change; tastes and prices also move.")],
  [("YED", "Income elasticity of demand measures the responsiveness of demand to a change in income."),
   ("Normal good", "A normal good has positive income elasticity of demand."),
   ("Inferior good", "An inferior good has negative income elasticity of demand."),
   ("Luxury good", "A luxury has income elasticity of demand above one."),
   ("Necessity", "A necessity has income elasticity of demand between zero and one.")],
  [CW["explain"], CW["consider"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
const incLab = { x: "Quantity", y: "Price", D1: "D1", D2: "D2", S1: "S", S2: "S", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function inDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, incLab); }
$("#pic1").innerHTML = (() => {
  const X = (v) => 70 + v * 6, Y = (q) => 250 - q * 2;
  let o = axes(70, 250, 700, 25, "Income", "Quantity demanded");
  o += SV.line(X(0), Y(20), X(100), Y(95), "c2", { "stroke-width": 3 }) + tag(X(100) + 4, Y(95), "Luxury (YED > 1)", "c2");
  o += SV.line(X(0), Y(30), X(100), Y(55), "c1", { "stroke-width": 3 }) + tag(X(100) + 4, Y(55), "Necessity (0 to 1)", "c1");
  o += SV.line(X(0), Y(80), X(100), Y(30), "c3", { "stroke-width": 3 }) + tag(X(100) + 4, Y(30), "Inferior (YED < 0)", "c3");
  return `<svg viewBox="0 0 760 270" role="img" aria-label="Quantity demanded against income for a luxury, a necessity and an inferior good">${o}</svg>`;
})();
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in income increases demand for a normal good", base: { d: 0, n: 0 }, draw: inDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand and supply for a normal good meet at a price of 50 and a quantity of 50.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise.</b> YED is positive, so demand increases and the demand curve shifts right.", s: { d: 20, n: 1 } },
  { cap: "<b>The equilibrium moves</b> to a higher price (58) and quantity (60).", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A rise in income decreases demand for an inferior good", base: { d: 0, n: 0 }, draw: inDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The same market, now for an inferior good.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise.</b> YED is negative: consumers switch to better goods, so demand falls and the curve shifts left.", s: { d: -20, n: 1 } },
  { cap: "<b>The equilibrium moves</b> to a lower price (42) and quantity (40).", s: { d: -20, n: 1 } },
] });

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const y = +$("#g1v").value / 10, ic = +$("#g2v").value, qc = y * ic;
  $("#r1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#r2").textContent = y < 0 ? "Inferior" : y < 1 ? "Normal (necessity)" : "Normal (luxury)";
  const bar = (yy, lab, v, c) => SV.text(20, yy + 15, lab, "sm") + SV.rect(150, yy, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, yy + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labA").innerHTML = bar(30, "Income", ic, "f3") + bar(90, "Quantity", qc, "f1");
  $("#rv").textContent = `With YED of ${Lib.fmtN(y, 1)} a ${ic >= 0 ? "rise" : "fall"} of ${Math.abs(ic)}% in income changes quantity demanded by ${Lib.fmtN(qc, 1)}%. ` + (y < 0 ? "The good is inferior: demand moves in the opposite direction to income." : y < 1 ? "The good is a necessity: demand changes by a smaller percentage than income." : "The good is a luxury: demand changes by a larger percentage than income.");
}
Lib.slider($("#g1"), { id: "g1v", label: "YED × 10 ", min: -15, max: 30, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Change in income, % ", min: -10, max: 10, step: 2, value: 6, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labA });
labA();

chooser("h", [
  ["Foreign holidays", "Above +1 (luxury)", "Demand rises strongly", "Demand falls sharply", 5],
  ["Basic food (bread, rice)", "0 to +1 (necessity)", "Demand rises slightly", "Demand barely falls", 2],
  ["Own-brand budget goods", "Below 0 (inferior)", "Demand falls", "Demand rises", 3],
  ["New cars", "Above +1 (luxury)", "Demand rises strongly", "Demand falls sharply", 5],
  ["Restaurant meals", "Above +1", "Demand rises", "Demand falls", 4],
  ["Public bus travel (for some)", "Below 0 (may be inferior)", "May fall as people buy cars", "May rise", 2]
], (it) => `${it[0]}: likely YED is ${it[1].toLowerCase()}. In a boom, ${it[2].toLowerCase()}; in a recession, ${it[3].toLowerCase()}.`, "Strength of the response to income");
''' + CLASSIFY("cl1", "Is the good more likely to be normal or inferior?", ["Normal good", "Inferior good"],
  [("Foreign holidays", 0), ("Own-brand budget cereal", 1), ("Designer clothes", 0), ("Cheap instant noodles", 1), ("New cars", 0), ("Low-quality own-label ready meals", 1), ("Restaurant meals", 0), ("Basic bread", 0)],
  "Normal goods are bought more as income rises; inferior goods are bought less because better alternatives become affordable. Basic bread is usually a normal necessity.") + MATCH([
  ["YED", "% change in quantity demanded ÷ % change in income"],
  ["Normal good", "YED is positive"],
  ["Inferior good", "YED is negative"],
  ["Luxury", "YED is above 1"],
  ["Necessity", "YED is between 0 and 1"],
  ["Income elastic", "Quantity changes by a greater percentage than income"]]) + ORDER(
  "Put the effects of a rise in income on a normal good in order.",
  ["Incomes rise", "Demand for the normal good increases", "The demand curve shifts right", "Equilibrium price and quantity rise"],
  "Income up, demand up, shift right, price and quantity up.") + CALC([
  {"q": "Income rises by 5% and quantity demanded rises by 15%. What is YED?", "a": 3, "unit": "", "tol": 0.05, "hint": "15 ÷ 5.", "sol": "<b>3</b>, a luxury."},
  {"q": "YED is -0.5 and income rises by 8%. By what % does quantity demanded change?", "a": -4, "unit": "%", "tol": 0.1, "hint": "-0.5 × 8.", "sol": "<b>-4%</b>."},
  {"q": "YED is +0.4 and income falls by 10%. By what % does quantity demanded change?", "a": -4, "unit": "%", "tol": 0.1, "hint": "0.4 × -10.", "sol": "<b>-4%</b>."},
  {"q": "Income rises from $2000 to $2200 and quantity demanded rises from 50 to 60. What is YED?", "a": 2, "unit": "", "tol": 0.05, "hint": "% change in Q = 20%; in income = 10%.", "sol": "<b>2</b>."}]) + MCQ([
  ("A negative YED means the good is:", ["Inferior", "Normal", "A luxury", "A necessity"], 0, "Demand falls as income rises."),
  ("A YED of +1.8 suggests:", ["A luxury", "A necessity", "An inferior good", "Unit elastic demand"], 0, "Above one."),
  ("In a recession, demand for an inferior good is likely to:", ["Rise", "Fall", "Stay the same", "Disappear"], 0, "People trade down."),
  ("YED = ", ["% change in Q demanded ÷ % change in income", "% change in Q ÷ % change in price", "Change in income ÷ change in Q", "Price × quantity"], 0, "The YED formula."),
  ("A rise in income shifts the demand curve for a normal good:", ["Right", "Left", "Not at all", "Up only"], 0, "Demand increases.")
], "qz1") + CARDS([
  ("YED formula", "%ΔQd ÷ %Δincome."),
  ("Normal good", "Positive YED."),
  ("Inferior good", "Negative YED."),
  ("Necessity", "0 to +1."),
  ("Luxury", "Above +1."),
  ("Income rises, normal", "Demand shifts right."),
  ("Income rises, inferior", "Demand shifts left."),
  ("Business use", "Forecast sales through the cycle.")]) + MCQ(mc_exam)

build("as29", "as-income-elasticity-of-demand", "Income Elasticity of Demand", EY,
  "2.2.2: the sign and size of YED, normal and inferior goods, and its uses for businesses. Animated demand shifts, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
