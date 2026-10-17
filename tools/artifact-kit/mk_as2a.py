"""AS syllabus 2.2.3 Cross elasticity of demand. Run: python3 tools/artifact-kit/mk_as2a.py"""
from as6k import *
EY = EYAS("2.2.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Cross elasticity of demand (XED)</b> measures how responsive the demand for one good (X) is to a change in the price of another good (Y): <b>XED = % change in quantity demanded of X ÷ % change in price of Y</b>. The <b>sign</b> shows the relationship: <b>positive</b> for <b class="kw">substitutes</b> (a rise in the price of Y raises demand for X) and <b>negative</b> for <b class="kw">complements</b> (a rise in the price of Y lowers demand for X); a value near <b>zero</b> means the goods are <b>unrelated</b>. The <b>size</b> shows how close the relationship is: the closer the substitutes or the stronger the complements, the bigger the number. Businesses use XED to predict the effect of <b>rivals' price changes</b>, to plan <b>pricing</b> and to understand <b>joint demand</b> for complementary products.</p></div>

  <h2>1 · Sign and size</h2>
  <div class="tw"><table class="t">
    <tr><th>XED</th><th>Relationship</th><th>Price of Y rises 10%</th><th>Example</th></tr>
    <tr><td>Positive, large</td><td>Close substitutes</td><td>Demand for X rises by a lot</td><td>Two similar smartphone brands</td></tr>
    <tr><td>Positive, small</td><td>Weak substitutes</td><td>Demand for X rises slightly</td><td>Bread and rice</td></tr>
    <tr><td>Near zero</td><td>Unrelated</td><td>No change</td><td>Cars and pencils</td></tr>
    <tr><td>Negative, small</td><td>Weak complements</td><td>Demand for X falls slightly</td><td>Bread and butter</td></tr>
    <tr><td>Negative, large</td><td>Strong complements</td><td>Demand for X falls by a lot</td><td>Printers and ink cartridges</td></tr>
  </table></div>
  <div id="pic1" class="card"></div>

  <h2>2 · Demand curves and related goods</h2>
  <ul>
    <li>If the price of a <b>substitute</b> rises, demand for X <b>shifts right</b>; if the price of a <b>complement</b> rises, demand for X <b>shifts left</b>.</li>
    <li>Determinants of the <b>size</b> of the coefficient: how <b>close</b> the substitutes are, how <b>important</b> the complement is to using the good, and how <b>broadly</b> the market is defined.</li>
    <li>XED also underlies <b>joint demand</b>, <b>alternative demand</b>, and <b>derived demand</b> ideas covered in the supply and demand chapter.</li>
  </ul>

  <h2>3 · Why it matters</h2>
  <ul>
    <li><b>Pricing:</b> a firm with close substitutes (high positive XED) knows a rival's price cut could take away many customers.</li>
    <li><b>Product strategy:</b> firms selling complements (printers and ink) may price one low and the other high.</li>
    <li><b>Competition policy:</b> XED helps define the market, since close substitutes show who competes.</li>
    <li><b>Limits:</b> estimates may be unreliable, and other factors change at the same time.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Write the formula, then use the <b>sign</b> to say substitute or complement and the <b>size</b> to say how close. Notice <b>which price</b> changes: it is the price of the <b>other</b> good.</div>
'''

watch = '''
  <h2>1 · The price of a substitute rises</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · The price of a complement rises</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Another good's price changes</h2>
  <p>Choose the cross elasticity and the change in the price of good Y to see the effect on demand for good X.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Change in demand for X</small><strong id="r1"></strong></div><div><small>Relationship</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 220" role="img" aria-label="Bars showing the change in the price of Y and in quantity demanded of X"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Pick a pair of goods", "Choose a pair of goods to see the likely sign and size of XED and what a firm might learn.", ["Likely XED", "If the price of Y rises", "Use for a firm"])

practise = practise_html("Substitutes or complements?", "Match the term to its description", "Put the effects of a rise in the price of a substitute in order")

real = RWNOTE + (
rw("Two rival streaming services", "If one raises its monthly fee, some customers switch to the other. The rival's demand rises, so XED is positive and fairly large.", "close substitutes.") +
rw("Printers and ink", "A fall in the price of printers raises demand for ink cartridges, since they are used together. XED is negative, and sellers may price printers low and ink high.", "complements.") +
rw("Bread and butter", "A rise in the price of butter may reduce the demand for bread a little. The two are weak complements, so XED is small and negative.", "weak complements.") +
rw("Bread and rice", "A rise in the price of rice may increase demand for bread somewhat. They are substitutes, but not very close ones.", "substitutes with a moderate XED.")
)

mc_exam = [
  mcq("m22_12", 8, "What is the measure of cross-elasticity of demand for good X in terms of good Y?", ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], 2, "XED of X with respect to Y is the % change in demand for X over the % change in the price of Y."),
  mcq("s20_12", 8, "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges?", ["-0.4", "+0.4", "+2.0", "+2.5"], 3, "Demand rose by 25% and the price rose by 10%, so XED = 25 ÷ 10 = +2.5."),
  mcq("s21_11", 10, "A government introduces a subsidy for product X and the market price of X falls by 5%. The cross elasticity of demand for product Y with respect to the price of X is +0.4. What will happen to the demand for product Y?", ["It will decrease by 2%.", "It will decrease by 12.5%.", "It will increase by 2%.", "It will increase by 12.5%."], 0, "0.4 × (-5%) = -2%, so demand for Y falls by 2%."),
  mcq("s22_11", 13, "What can be concluded about a good with a positive cross-price elasticity of demand?", ["Its price will be sensitive to changes in prices of close substitutes.", "Its price will be sensitive to changes in quantity demanded of close substitutes.", "The quantity demanded for this good will be sensitive to changes in prices of close substitutes.", "The quantity demanded for this good will be sensitive to changes in quantity demanded of close substitutes."], 2, "Positive XED means substitutes; the quantity demanded responds to the price of the substitute."),
  mcq("m24_12", 7, "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X?", ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], 0, "XED positive: substitute for Y; YED negative: inferior; PED size 2.4: elastic."),
  mcq("m20_12", 8, "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y)", ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], 2, "X is normal, so higher income raises demand, and a fall in the price of a complement also raises it.")
]

exam = exam_page("cross elasticity of demand",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). XED appears as an 8 mark Paper 2 part (formula, sign and determinants) and in 12 mark comparisons with income elasticity or price elasticity. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "May/June 2023 (21) Q3(a); Oct/Nov 2020 (21) Q3(a)"), ("Essay parts, 12 marks", "1", "May/June 2021 (21) Q3(b)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2024")],
  [
  eq(P("s23_21", "3(a)"), "8 marks", "With the help of a formula, explain the meaning of cross elasticity of demand and consider which determinants are most important in establishing the size and sign of its coefficient.",
     ["Knowledge (up to 3): what cross elasticity of demand measures (1), the formula (1), and the distinction between positive and negative XED (1).",
      "Analysis (up to 3): why XED can be positive, for substitutes (1); why it can be negative, for complements (1); and the determinants of its magnitude, where the closer the relationship between two products the greater the size of XED (1).",
      "Evaluation (up to 2): a valid judgement on the relative importance of the determinants of the size and sign of XED (1) and a conclusion (1)."],
     "Formula and meaning. Positive: substitutes. Negative: complements. Size: closeness of the relationship. Judge: closeness of relationship matters most for size; the nature of the link for sign.",
     [[("k", "Cross elasticity of demand measures how responsive the demand for one good is to a change in the price of another. It equals the percentage change in quantity demanded of good X divided by the percentage change in the price of good Y. It is positive for substitutes and negative for complements.")], [("n", "XED is positive when goods are substitutes, because a higher price for Y makes consumers switch to X, and negative for complements, because a higher price for Y lowers demand for the good used with it. The closer the relationship, whether substitutes or complements, the larger the size of the coefficient.")], [("e", "The nature of the relationship, whether the goods are used together or in place of each other, is likely to determine the sign, while how close the substitutes are, and how the market is defined, may be most important for the size. A narrowly defined market is likely to give a larger coefficient.")]]),
  eq(P("w20_21", "3(a)"), "8 marks", "The cross elasticity of demand for bread with respect to the price of rice is +1.4, while the cross elasticity of demand for bread with respect to the price of butter is -0.7. Explain why the cross elasticity of demand figures for bread differ.",
     ["Knowledge (up to 2): what is meant by XED (1) and the formula, the percentage change in the quantity demanded of good A divided by the percentage change in the price of good B (1).",
      "Application (up to 6): application to goods as substitutes or positive XED (1), to bread and rice as substitutes (1) and to the figure showing a strong relationship (1); application to goods as complements or negative XED (1), to bread and butter as complements (1) and to the figure showing a weaker relationship (1)."],
     "XED formula. Bread and rice: positive, substitutes, +1.4 strong. Bread and butter: negative, complements, -0.7 weaker.",
     [[("k", "Cross elasticity of demand is the percentage change in the quantity demanded of one good divided by the percentage change in the price of another good.")], [("n", "The figure for rice is positive because rice and bread are substitutes: if the price of rice rises, consumers buy more bread. The value of 1.4 is above one, which suggests a strong relationship, so a given rise in the price of rice leads to a larger percentage rise in demand for bread. The figure for butter is negative because butter and bread are complements, as they are used together, so a rise in the price of butter lowers demand for bread. The value of 0.7 is smaller in size, which suggests a weaker relationship.")]]),
  eq(P("s21_21", "3(b)"), "12 marks", "Discuss the extent to which knowledge of the income elasticity of demand for its product is likely to be more useful to a business than knowledge of the cross elasticity of demand for its product.",
     ["Analysis (up to 8): the usefulness of YED to a business, with appropriate scenarios (up to 4), such as normal and inferior goods, the development of the economy and planning during a boom or recession; and of XED (up to 4), such as substitutes or alternative demand (positive XED) and complements or joint demand (negative XED).",
      "Evaluation (up to 4): a judgement on whether YED is likely to be more useful than XED, with a conclusion (1 mark reserved)."],
     "YED: boom, recession, normal and inferior goods, planning. XED: rivals' prices, substitutes, complements. Judge: depends on whether income or competitors drive the business.",
     [[("n", "YED helps a business forecast how demand will respond to changes in income, so it can plan production through a boom or a recession and decide whether its product is normal or inferior. XED shows how demand will respond to a change in the price of a substitute or complement, so a firm can predict the effect of a rival's price cut or of price changes of a complementary good.")], [("e", "YED may be more useful for long-term planning, especially where the product is income elastic, such as holidays or cars, while XED is likely to be more useful in a competitive market with close substitutes, where rival pricing matters most. Which is more useful depends on the product and the market.")]])
  ],
  )

tips = tips_html(
  [("Formula first.", "% change in Q of X ÷ % change in price of Y."),
   ("Check which price.", "It is the price of the other good."),
   ("Sign gives the link.", "Positive substitutes, negative complements."),
   ("Size gives closeness.", "Bigger number, closer relationship."),
   ("Use examples.", "Rival brands; printers and ink."),
   ("Say what a firm does.", "Predict rivals' effects, set prices."),
   ("Evaluate.", "Estimates change; markets are defined differently.")],
  [("XED", "Cross elasticity of demand measures the responsiveness of the demand for one good to a change in the price of another."),
   ("Substitutes", "Substitutes have a positive cross elasticity."),
   ("Complements", "Complements have a negative cross elasticity."),
   ("Joint demand", "Goods in joint demand are used together."),
   ("Alternative demand", "Goods in alternative demand can replace each other.")],
  [CW["explain"], CW["consider"], CW["discuss"], CW["assess"]]) + FC

js = SDJS + CHAINJS + '''
const xLab = { x: "Quantity of X", y: "Price of X", D1: "D1", D2: "D2", S1: "S", S2: "S", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function xDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, xLab); }
$("#pic1").innerHTML = (() => {
  const X = (v) => 70 + (v + 3) * 100, Y = (q) => 250 - (q + 60) * 1.6;
  let o = axes(70, 250, 700, 25, "XED", "% change in demand for X (price of Y +10%)");
  o += SV.line(X(-3), Y(-30), X(3), Y(30), "c2", { "stroke-width": 3 }) + SV.line(X(0), 250, X(0), 40, "dash");
  o += SV.text(X(1.5), Y(5), "Substitutes (XED > 0)", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(-1.5), Y(-5), "Complements (XED < 0)", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(0) + 6, 52, "Unrelated", "sm");
  return `<svg viewBox="0 0 760 270" role="img" aria-label="The change in demand for X against XED: positive for substitutes, negative for complements">${o}</svg>`;
})();
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The price of a substitute rises, so demand for X rises", base: { d: 0, n: 0 }, draw: xDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market for good X is in equilibrium at a price of 50 and a quantity of 50.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of a substitute (Y) rises.</b> XED is positive, so consumers switch to X and the demand curve for X shifts right.", s: { d: 20, n: 1 } },
  { cap: "<b>The price of X rises</b> to 58 and the quantity to 60.", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stB"), { w: 760, h: 300, label: "The price of a complement rises, so demand for X falls", base: { d: 0, n: 0 }, draw: xDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The same market for good X.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of a complement (Y) rises.</b> XED is negative, so the combined cost of using X and Y rises and the demand curve for X shifts left.", s: { d: -20, n: 1 } },
  { cap: "<b>The price of X falls</b> to 42 and the quantity to 40.", s: { d: -20, n: 1 } },
] });

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const x = +$("#g1v").value / 10, pc = +$("#g2v").value, qc = x * pc;
  $("#r1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#r2").textContent = Math.abs(x) < 0.05 ? "Unrelated" : (x > 0 ? "Substitutes" : "Complements") + (Math.abs(x) >= 1 ? " (close)" : " (weak)");
  const bar = (yy, lab, v, c) => SV.text(20, yy + 15, lab, "sm") + SV.rect(150, yy, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, yy + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labA").innerHTML = bar(30, "Price of Y", pc, "f3") + bar(90, "Demand for X", qc, "f1");
  $("#rv").textContent = Math.abs(x) < 0.05 ? "XED is about zero: the price of Y does not affect demand for X." : `With XED of ${Lib.fmtN(x, 1)}, a ${pc >= 0 ? "rise" : "fall"} of ${Math.abs(pc)}% in the price of Y changes demand for X by ${Lib.fmtN(qc, 1)}%. ` + (x > 0 ? "The goods are substitutes: consumers switch between them." : "The goods are complements: they are used together.");
}
Lib.slider($("#g1"), { id: "g1v", label: "XED × 10 ", min: -20, max: 20, step: 2, value: 12, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Change in the price of Y, % ", min: -10, max: 10, step: 2, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labA });
labA();

chooser("h", [
  ["Two rival smartphone brands", "Large and positive", "Demand for the other rises sharply", "Predict the effect of a rival's price cut", 5],
  ["Bread and rice", "Moderate and positive", "Demand for bread rises somewhat", "Weak competition; monitor rice prices", 3],
  ["Printers and ink", "Large and negative", "Demand for ink falls sharply", "Price the printer low and ink high", 5],
  ["Bread and butter", "Small and negative", "Demand for bread falls slightly", "Little effect on pricing", 2],
  ["Cars and pencils", "About zero", "No change", "No link to use in pricing", 1],
  ["Tea and coffee", "Positive", "Demand for the other rises", "Watch each other's price changes", 3]
], (it) => `${it[0]}: XED is likely to be ${it[1].toLowerCase()}. If the price of one rises, ${it[2].toLowerCase()}. For a firm: ${it[3].toLowerCase()}.`, "Strength of the link");
''' + CLASSIFY("cl1", "Are the goods more likely to be substitutes or complements?", ["Substitutes (positive XED)", "Complements (negative XED)"],
  [("Tea and coffee", 0), ("Printers and ink cartridges", 1), ("Two rival car brands", 0), ("Cars and petrol", 1), ("Butter and margarine", 0), ("Bread and butter", 1), ("Bus and train travel", 0), ("Games consoles and games", 1)],
  "Substitutes replace each other; complements are used together.") + MATCH([
  ["XED", "% change in Q of X ÷ % change in price of Y"],
  ["Substitutes", "Positive cross elasticity"],
  ["Complements", "Negative cross elasticity"],
  ["Close substitutes", "A large positive XED"],
  ["Unrelated goods", "XED close to zero"],
  ["Joint demand", "Goods used together, such as printers and ink"]]) + ORDER(
  "Put the effects of a rise in the price of a substitute in order.",
  ["The price of good Y rises", "Consumers switch to good X", "The demand curve for X shifts right", "The price and quantity of X rise"],
  "Price of the substitute up, demand for X up, shift right.") + CALC([
  {"q": "The price of Y rises by 10% and demand for X rises by 6%. What is XED?", "a": 0.6, "unit": "", "tol": 0.01, "hint": "6 ÷ 10.", "sol": "<b>+0.6</b>, substitutes."},
  {"q": "XED is -1.5 and the price of Y rises by 4%. By what % does demand for X change?", "a": -6, "unit": "%", "tol": 0.1, "hint": "-1.5 × 4.", "sol": "<b>-6%</b>."},
  {"q": "XED is +2.0 and the price of Y falls by 5%. By what % does demand for X change?", "a": -10, "unit": "%", "tol": 0.1, "hint": "2.0 × -5.", "sol": "<b>-10%</b>."},
  {"q": "The price of Y rises from $4 to $5 and demand for X falls from 200 to 170. What is XED?", "a": -0.6, "unit": "", "tol": 0.01, "hint": "% change in Q = -15%; in price = +25%.", "sol": "<b>-0.6</b>, complements."}]) + MCQ([
  ("A positive XED means the goods are:", ["Substitutes", "Complements", "Unrelated", "Inferior"], 0, "Demand rises when the other's price rises."),
  ("A negative XED means the goods are:", ["Complements", "Substitutes", "Normal", "Luxuries"], 0, "Used together."),
  ("A larger size of XED suggests:", ["A closer relationship", "A weaker relationship", "No relationship", "An inferior good"], 0, "Closer links, bigger responses."),
  ("XED measures the response of demand to:", ["The price of another good", "Income", "The good's own price", "Supply"], 0, "The 'cross' price."),
  ("If the price of a complement rises, demand for X:", ["Falls", "Rises", "Is unchanged", "Becomes perfectly elastic"], 0, "The pair costs more.")
], "qz1") + CARDS([
  ("XED formula", "%ΔQ of X ÷ %ΔP of Y."),
  ("Positive XED", "Substitutes."),
  ("Negative XED", "Complements."),
  ("Zero XED", "Unrelated."),
  ("Large size", "Close relationship."),
  ("Substitute price up", "Demand for X shifts right."),
  ("Complement price up", "Demand for X shifts left."),
  ("Business use", "Predict rivals' effects, price complements.")]) + MCQ(mc_exam)

build("as2a", "as-cross-elasticity-of-demand", "Cross Elasticity of Demand", EY,
  "2.2.3: the sign and size of XED, substitutes and complements, and its uses for businesses. Animated demand shifts, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
