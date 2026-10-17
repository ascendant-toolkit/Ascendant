"""AS syllabus 2.1.5-2.1.7 Shifts of demand and supply and movements along the curves. Run: python3 tools/artifact-kit/mk_as22.py"""
from asx import *
EY = EYAS("2.1.5 to 2.1.7")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">movement along</b> a demand or supply curve is caused <b>only by a change in the price of the good itself</b>, and is called an <b>extension or contraction</b> of demand, or an <b>expansion or contraction</b> of supply. A <b class="kw">shift</b> of the curve is caused by a change in <b>any other determinant</b>: income, the prices of related goods, tastes, population or expectations for demand; costs, technology, taxes and subsidies, the number of firms and weather for supply. A shift to the <b>right</b> is an <b>increase</b> in demand or supply (more at every price); a shift to the <b>left</b> is a <b>decrease</b>. Always draw the new curve, label the new equilibrium and say which way price and quantity move.</p></div>

  <h2>1 · Movement along a curve (2.1.7)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>Price falls: <b>extension</b> of demand (quantity demanded rises) and <b>contraction</b> of supply (quantity supplied falls).</li>
    <li>Price rises: <b>contraction</b> of demand and <b>extension (expansion)</b> of supply.</li>
    <li>The curve itself does <b>not move</b>. A fall in price caused by a rise in supply moves you along the demand curve.</li>
    <li>Terminology: say <b>quantity demanded</b> or <b>quantity supplied</b> changes for a movement; say <b>demand</b> or <b>supply</b> changes for a shift.</li>
  </ul>

  <h2>2 · Shifts of demand (2.1.5)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Shift right (increase)</th><th>Shift left (decrease)</th></tr>
    <tr><td>Higher income (normal good) or lower income (inferior good)</td><td>Lower income (normal good) or higher income (inferior good)</td></tr>
    <tr><td>Rise in the price of a substitute</td><td>Fall in the price of a substitute</td></tr>
    <tr><td>Fall in the price of a complement</td><td>Rise in the price of a complement</td></tr>
    <tr><td>Favourable tastes, advertising</td><td>Unfavourable tastes or health scares</td></tr>
    <tr><td>Population growth, expected price rise, cheaper credit</td><td>Falling population, expected price fall, higher interest rates</td></tr>
  </table></div>

  <h2>3 · Shifts of supply (2.1.6)</h2>
  <div class="tw"><table class="t">
    <tr><th>Shift right (increase)</th><th>Shift left (decrease)</th></tr>
    <tr><td>Lower costs: wages, materials, energy</td><td>Higher costs</td></tr>
    <tr><td>Better technology, higher productivity</td><td>Poorer technology or lower productivity</td></tr>
    <tr><td>Subsidy</td><td>Indirect tax</td></tr>
    <tr><td>More firms entering the market</td><td>Firms leaving the market</td></tr>
    <tr><td>Good weather or harvest</td><td>Drought, flood or natural disaster</td></tr>
  </table></div>
  <ul>
    <li><b>Effects on equilibrium:</b> demand right: price and quantity up. Demand left: both down. Supply right: price down, quantity up. Supply left: price up, quantity down.</li>
    <li>A shift of one curve causes a <b>movement along the other</b> (a rise in demand moves you up the supply curve).</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Check the <b>cause</b> in the question: if the price of the good changes, it is a movement; if anything else changes, it is a shift. Draw <b>one diagram per change</b> unless the question allows two together.</div>
'''

watch = '''
  <h2>1 · A movement along the demand curve</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · A shift of the demand curve</h2>
  <div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · Move along the curves</h2>
  <p>Change the price and see quantity demanded and quantity supplied. The curves stay still.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Quantity demanded</small><strong id="r1"></strong></div><div><small>Quantity supplied</small><strong id="r2"></strong></div><div><small>Result</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with the market price marked and quantity demanded and supplied shown"></svg></div></div></div>

  <h2>Lab 2 · Which curve moves?</h2>
  <p>Choose a change. The diagram shows which curve shifts and the new equilibrium.</p>
  <div class="card"><div class="grid2"><div><div id="evB" class="btnrow"></div>
    <div class="readout"><div><small>Curve</small><strong id="t1"></strong></div><div><small>New price</small><strong id="t2"></strong></div><div><small>New quantity</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with the curve for the chosen event shifted"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Shift or movement?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the change to its effect</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps of a diagram answer in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Petrol and public transport", "A rise in the price of petrol moves drivers up the supply curve for petrol (contraction of demand) but shifts the demand curve for bus journeys to the right, because buses are a substitute for driving.", "separating the price of the good (movement) from the price of a related good (shift).") +
rw("Health scare for eggs", "A health scare lowers demand for eggs at every price, so the demand curve shifts left. The price falls, which moves farmers down their supply curve: a contraction in supply.", "a shift of demand leading to a movement along supply.") +
rw("Cheaper smartphones", "Cheaper components and better production methods shift the supply curve for smartphones to the right. The price falls and the quantity sold rises, an extension of demand along an unchanged demand curve.", "a shift of supply causing a movement along demand.") +
rw("Cinema ticket discount", "A cinema cuts ticket prices by 20%. More people go (extension along the demand curve). If it launched an advertising campaign instead, the whole curve would move right.", "the difference between a price change and an advertising campaign.")
)

mc_exam = [
  mcq("m21_12", 5, "What could not cause a shift in an individual's demand curve for good Z?", ["a change in advertising expenditure on Z", "a change in the individual's income", "a change in the individual's tastes", "a change in the price of Z"], 3, "The price of Z moves along the curve. The others shift it."),
  mcq("m22_12", 12, "What causes the demand curve for an inferior good to shift to the right?", ["a decrease in consumer incomes", "a decrease in income tax", "a decrease in the price of a substitute good", "a decrease in the price of the good"], 0, "Falling incomes raise demand for inferior goods. A lower tax raises income, and a price change is a movement."),
  mcq("s20_13", 10, "Which combination of the classification of a good and market change will cause the demand curve for the good to shift right?", ["inferior good, income decrease", "inferior good, price decrease", "normal good, income decrease", "normal good, price decrease"], 0, "An income fall shifts demand right for an inferior good. A price decrease is a movement."),
  mcq("s21_12", 7, "What leads to a downward shift of a normal supply curve?", ["a rise in the cost of transporting goods", "a rise in the productivity of the labour force", "a rise in the rate of sales tax on the good", "a rise in the wage rate paid to workers"], 1, "A downward shift of supply (to the right) results from lower costs, so higher productivity."),
  mcq("s21_13", 6, "What will not cause a shift in the market supply curve of a commodity?", ["a change in technology", "a rise in the price of a factor input", "a rise in the price of the commodity", "the introduction of a specific tax on the commodity"], 2, "The commodity's own price causes a movement along."),
  mcq("s22_13", 7, "Which change would cause the supply curve of sugar-sweetened drinks to shift to the right?", ["a fall in the price of sugar", "a removal of a subsidy on sugar", "an increase in consumer income", "an increase of a specific tax on sugar"], 0, "Cheaper sugar lowers costs, so supply shifts right."),
  mcq("s23_13", 6, "What is most likely to cause a shift in the supply curve for rice?", ["a change in the price of the rice", "a change in the price of meat", "a change in the size of the rice industry", "a change in tastes and preferences for rice"], 2, "More firms or farms change supply at every price."),
  mcq("s23_13", 8, "What would not cause a shift in the demand curve for a good?", ["a change in the price of a complement", "a change in the price of a substitute", "a change in the price of the good itself", "a change in consumers' incomes"], 2, "The good's own price moves along the curve."),
  mcq("w20_11", 12, "The demand curve for new cars in a country shifted to the left. Which change could have caused such a shift?", ["an increase in real disposable income", "an increase in the cost of borrowing", "an increase in the price of new cars", "an increase in the price of train travel"], 1, "Dearer credit lowers demand for cars bought on credit. Higher income and a dearer substitute would raise demand."),
  mcq("w20_13", 10, "A bus journey is considered an inferior good in a relatively rich country such as Singapore but a normal good in a relatively poor country such as Tanzania. In which direction would an increase in incomes in both countries cause the demand curve for bus journeys in Singapore and Tanzania to shift?", ["Singapore left, Tanzania left", "Singapore left, Tanzania right", "Singapore right, Tanzania left", "Singapore right, Tanzania right"], 1, "Higher income lowers demand for an inferior good and raises it for a normal good."),
  mcq("s24_11", 6, "An increase in which factor is likely to cause a shift to the left of the demand curve for cinema movies?", ["expenses for the heating system in the cinema", "payments charged by movie scriptwriters", "the cost of transport to the cinema", "taxes on the incomes of cinema operators"], 2, "Transport to the cinema is a complement, so its cost rising lowers demand. The others are costs for the cinema, which affect supply."),
  mcq("s20_11", 11, "Shoe manufacturers often use leather to make their most expensive shoes. Due to a world shortage of leather, the price of leather has risen. What will be the effect of this price change?", ["The demand curve for leather shoes will shift to the left", "The demand curve for a substitute for leather shoes will shift to the right", "The supply curve for leather shoes will shift to the right", "The supply curve for a substitute for leather to make expensive shoes will shift to the left"], 1, "Dearer leather shoes make substitutes more attractive, so their demand rises. The supply of leather shoes shifts left.")
]

exam = exam_page("shifts of demand and supply and movements along curves",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The movement versus shift distinction is tested in nearly every Paper 1 and in 8 mark Paper 2 parts. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2024 (22) Q2(a); May/June 2022 (22) Q3(a)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("w24_22", "2(a)"), "8 marks", "With the help of a diagram, briefly explain how the cause of a movement along the demand curve differs from the cause of a shift in the demand curve and consider the impact on the demand for one good of price changes in other goods.",
     ["Knowledge (up to 3): an accurate demand diagram, or two diagrams, showing a movement and a shift (1); a movement occurs because of a change in price (1); a shift occurs because of a change in a non-price factor (1).",
      "Analysis (up to 3): the impact on demand for one good depending on whether other goods are substitutes or complements: a rise in the price of a complement lowers demand because of joint demand (up to 2); a rise in the price of a substitute raises demand because consumers switch (up to 2). Maximum 2 if only one relationship is analysed. Changes in income, fashion or tastes are not rewarded.",
      "Evaluation (up to 2): the overall impact depends on the size of the cross elasticity values (1) and a valid conclusion about the size of the impact (1)."],
     "Diagram: movement along (price), shift (non-price). Substitute up: demand up. Complement up: demand down. Judge using XED size.",
     [[("k", "A movement along the demand curve happens when the price of the good itself changes, so quantity demanded changes, for example from a fall in price causing an extension. A shift happens when a non-price factor changes, such as income or the price of a related good, so demand changes at every price and the curve moves left or right.")], [("n", "If the price of a substitute such as tea rises, some consumers switch to coffee, so demand for coffee shifts to the right. If the price of a complement such as milk rises, coffee drinking becomes more expensive, so demand for coffee shifts to the left because of joint demand.")], [("e", "The overall impact depends on the cross elasticity of demand: if the XED coefficients are small, the substitutes or complements are weakly related and the shift will be small, while large values mean a large shift. So price changes in other goods could matter a great deal for some products and hardly at all for others.")]]),
  eq(P("s22_22", "3(a)"), "8 marks", "With the help of diagrams, use the concept of income elasticity of demand to explain the impact of a fall in incomes on the equilibrium price and equilibrium quantity of a normal good and an inferior good.",
     ["Knowledge (up to 2): the meaning of income elasticity of demand (1) with an accurate formula (1).",
      "Application (up to 6): for a normal good, its meaning (1), a diagram showing the demand curve shifting left (1) and a fall in equilibrium price and quantity (1); for an inferior good, its meaning (1), a separate diagram showing the demand curve shifting right (1) and a rise in equilibrium price and quantity (1). One diagram for both goods is not rewarded."],
     "Formula and meaning. Normal good: left shift, price and quantity fall. Inferior good: right shift, price and quantity rise. Two diagrams.",
     [[("k", "Income elasticity of demand measures how demand responds to a change in income: percentage change in quantity demanded divided by percentage change in income.")], [("n", "For a normal good, income elasticity is positive, because demand rises as income rises. A fall in incomes therefore shifts demand to the left and, with supply unchanged, the equilibrium price and quantity both fall. For an inferior good, income elasticity is negative, so a fall in incomes shifts demand to the right, and the equilibrium price and quantity both rise. Each effect should be shown on a separate diagram.")]])
  ],
  )

tips = tips_html(
  [("Own price: movement. Anything else: shift.", "This is the most tested rule in the topic."),
   ("Use the right terms.", "Extension and contraction for movements; increase and decrease for shifts."),
   ("Name the direction of both price and quantity.", "Right shift of demand: price and quantity rise."),
   ("Draw a separate diagram for each change.", "Two goods or two changes mean two diagrams unless told otherwise."),
   ("Normal and inferior goods differ.", "A fall in income shifts demand left for a normal good, right for an inferior good."),
   ("Costs shift supply, not demand.", "A cost for the producer never shifts the demand curve."),
   ("One shift causes a movement on the other curve.", "A demand rise moves you up the supply curve.")],
  [("Movement along", "A fall in the price of the good could cause an extension of demand."),
   ("Shift", "A change in a non-price factor may shift the demand curve to the right."),
   ("Substitute", "A rise in the price of a substitute is likely to shift demand to the right."),
   ("Complement", "A rise in the price of a complement may shift demand to the left."),
   ("Consider", "The impact depends on the size of the cross elasticity of demand.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- movement along demand ---------- */
function mvDraw(s) {
  const q = (90 - s.p) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(SDX(q), SDY(s.p), SDX(q), 270, "dash") + SV.line(70, SDY(s.p), SDX(q), SDY(s.p), "dash") + SV.circle(SDX(q), SDY(s.p), 7, "dot3") + SV.text(62, SDY(s.p) + 4, "$" + Lib.fmtN(s.p, 0), "sm", { "text-anchor": "end" }) + SV.text(SDX(q), 286, Lib.fmtN(q, 0), "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in price moves the market down the demand curve">${mvDraw({ p: 30 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A movement along the demand curve caused by a change in price", base: { p: 50 }, draw: mvDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Start.</b> At a price of $50 the quantity demanded is 50 units.", s: { p: 50 } },
  { cap: "<b>Price falls to $30.</b> Quantity demanded rises to 75: an <b>extension</b> of demand. The demand curve has not moved.", s: { p: 30 } },
  { cap: "<b>Price rises to $70.</b> Quantity demanded falls to 25: a <b>contraction</b> of demand. Still the same curve.", s: { p: 70 } },
] });

/* ---------- shift of demand ---------- */
function shDraw(s) { return sdPlot({ d: s.d, s: 0, g: s.g, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rise in demand shifts the curve right and raises price and quantity">${shDraw({ d: 20, g: 1, n: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A shift of the demand curve caused by a change in income", base: { d: 0, g: 1, n: 0 }, draw: shDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand D1 and supply S1 give an equilibrium price P1 and quantity Q1.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise</b> (the good is normal). People want more at every price, so demand <b>shifts right</b> to D2. Price and quantity rise to P2 and Q2.", s: { d: 20, n: 1 } },
  { cap: "<b>A health scare</b> would shift demand <b>left</b> instead, lowering price and quantity. The shift changes demand, not just quantity demanded.", s: { d: -20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8), res = Math.abs(qd - qs) < 0.5 ? "Balanced" : qd > qs ? "Shortage" : "Surplus";
  $("#r1").textContent = Lib.fmtN(qd, 0); $("#r2").textContent = Lib.fmtN(qs, 0); $("#r3").textContent = res;
  $("#rv").textContent = `At $${p}, buyers want ${Lib.fmtN(qd, 0)} units and sellers offer ${Lib.fmtN(qs, 0)}. ${res === "Balanced" ? "This is the equilibrium price: nothing pushes it to change." : res === "Shortage" ? "Quantity demanded exceeds quantity supplied (excess demand), so price tends to rise: extension of supply, contraction of demand." : "Quantity supplied exceeds quantity demanded (excess supply), so price tends to fall: contraction of supply, extension of demand."} The curves themselves have not moved.`;
  let o = sdPlot({ d: 0, s: 0, g: 0 }); const a = (90 - p) / 0.8, b = (p - 10) / 0.8;
  o += SV.line(70, SDY(p), SDX(Math.max(a, b, 0)), SDY(p), "dash") + SV.circle(SDX(Math.max(0, a)), SDY(p), 6, "dot2") + SV.circle(SDX(Math.max(0, b)), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + p, "sm", { "text-anchor": "end" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pp", label: "Market price, $ ", min: 10, max: 90, step: 5, value: 70, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const EV = [
  ["Incomes rise (normal good)", 20, 0, "Demand", "A rise in income raises demand for a normal good at every price, so demand shifts right."],
  ["Price of a substitute rises", 15, 0, "Demand", "Consumers switch to this good, so demand shifts right."],
  ["Price of a complement rises", -15, 0, "Demand", "The pair becomes dearer to buy, so demand shifts left."],
  ["Health scare about the good", -20, 0, "Demand", "Tastes turn against the good, so demand shifts left."],
  ["Cost of raw materials falls", 0, 20, "Supply", "Production costs fall, so supply shifts right."],
  ["New technology introduced", 0, 25, "Supply", "Output per unit of input rises and unit costs fall, so supply shifts right."],
  ["Indirect tax imposed", 0, -20, "Supply", "The tax raises each firm's cost, so supply shifts left."],
  ["Drought hits the harvest", 0, -25, "Supply", "Output falls at every price, so supply shifts left."],
];
function showEv(i) {
  const [t, d, s, c, why] = EV[i], e = sdEq(d, s), e0 = sdEq(0, 0);
  $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = c + (d + s > 0 ? " right" : " left"); $("#t2").textContent = "$" + Lib.fmtN(e.p, 0); $("#t3").textContent = Lib.fmtN(e.q, 0);
  $("#tv").textContent = `${t}. ${why} The equilibrium price ${e.p > e0.p ? "rises" : "falls"} from $50 to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 0)}.`;
  $("#labB").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
$("#evB").innerHTML = EV.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showEv(+b.dataset.i)));
showEv(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is it a shift or a movement?", ["Shift of demand", "Movement along demand", "Shift of supply"],
  [("A rise in income (normal good)", 0), ("The good's price falls", 1), ("Wages in the industry rise", 2), ("A successful advertising campaign", 0), ("A fall in the price of a complement", 0), ("A new tax on the good", 2), ("The good's price rises", 1), ("Better technology for producers", 2)],
  "Own price: movement. Other demand determinants: demand shifts. Cost, tax and technology changes: supply shifts.") + MATCH([
  ["Extension of demand", "Quantity demanded rises because price falls"],
  ["Contraction of demand", "Quantity demanded falls because price rises"],
  ["Increase in demand", "Right shift of the demand curve"],
  ["Decrease in supply", "Left shift of the supply curve"],
  ["Subsidy", "Shifts the supply curve to the right"],
  ["Indirect tax", "Shifts the supply curve to the left"]]) + ORDER(
  "Put the steps of a diagram answer in order.",
  ["Draw and label the axes: price and quantity", "Draw the original demand and supply curves and mark the equilibrium", "Shift the curve that has changed and label it", "Mark the new equilibrium price and quantity", "Explain the change in price and quantity in words"],
  "Always label the new equilibrium and say what happens to price and quantity.") + CALC([
  {"q": "Demand shifts right by 20 units at every price. Demand before: Qd = 100 − 2P. At P = 20, what is the new quantity demanded?", "a": 80, "unit": "units", "tol": 1, "hint": "Old Qd at P=20 is 60. Add 20.", "sol": "60 + 20 = <b>80</b>."},
  {"q": "Supply is Qs = 4P. A subsidy shifts supply right by 30 units at every price. At P = 10, what is the new quantity supplied?", "a": 70, "unit": "units", "tol": 1, "hint": "40 + 30.", "sol": "<b>70</b>."},
  {"q": "Price falls from $20 to $15 and quantity demanded rises from 40 to 50. What is the percentage change in quantity demanded?", "a": 25, "unit": "%", "tol": 0.5, "hint": "(50 − 40) ÷ 40.", "sol": "<b>25%</b>, an extension of demand."},
  {"q": "Equilibrium before: P = $50, Q = 50. After demand shifts right, Q = 60. What is the percentage rise in the equilibrium quantity?", "a": 20, "unit": "%", "tol": 0.5, "hint": "(60 − 50) ÷ 50.", "sol": "<b>20%</b>."}]) + MCQ([
  ("A fall in the price of a good causes:", ["A movement along the demand curve", "A shift of the demand curve to the right", "A shift of the supply curve to the left", "A fall in income"], 0, "Own price: movement."),
  ("What is the effect of a rise in demand and no change in supply?", ["Price and quantity both rise", "Price falls and quantity rises", "Price rises and quantity falls", "Price and quantity both fall"], 0, "Right shift of demand moves along supply."),
  ("A new indirect tax on a good will:", ["Shift the supply curve to the left", "Shift the demand curve to the left", "Shift the supply curve to the right", "Cause a movement along demand only"], 0, "A tax raises costs."),
  ("Which would cause demand for an inferior good to rise?", ["A fall in consumers' incomes", "A rise in consumers' incomes", "A fall in its own price", "A subsidy to producers"], 0, "Negative income elasticity."),
  ("A supply shift to the right causes quantity demanded to:", ["Extend along the demand curve", "Shift demand left", "Contract along demand", "Stay the same"], 0, "Price falls, so quantity demanded rises.")
], "qz1") + CARDS([
  ("Movement", "Caused only by the good's own price."),
  ("Shift", "Caused by any other determinant."),
  ("Increase in demand", "Right shift."),
  ("Decrease in supply", "Left shift."),
  ("Extension", "Quantity demanded rises as price falls."),
  ("Contraction", "Quantity falls as price rises."),
  ("Cost fall", "Supply shifts right."),
  ("Draw", "Label the new equilibrium.")]) + MCQ(mc_exam)

build("as22", "as-shifts-movements-demand-supply", "Shifts of Demand and Supply and Movements Along Curves", EY,
  "2.1.5 to 2.1.7: causes of shifts of the demand and supply curves and the distinction between a shift and a movement along a curve. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
