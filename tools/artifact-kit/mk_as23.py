"""AS syllabus 2.4.1-2.4.2 Market equilibrium, disequilibrium and the effects of shifts. Run: python3 tools/artifact-kit/mk_as23.py"""
from asx import *
EY = EYAS("2.4.1 to 2.4.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Market equilibrium</b> is the price and quantity where <b>quantity demanded equals quantity supplied</b>, so the market <b>clears</b> and there is <b>no tendency to change</b>. If the price is above equilibrium there is <b>excess supply (a surplus)</b>, so the price tends to <b>fall</b>; if it is below there is <b>excess demand (a shortage)</b>, so the price tends to <b>rise</b>, and this is called <b>disequilibrium</b> until the market adjusts. A shift of demand or supply moves the market to a <b>new equilibrium</b>: a right shift of demand raises price and quantity, a left shift lowers both, a right shift of supply lowers price and raises quantity, a left shift raises price and lowers quantity. When <b>both curves shift</b> at once, one of price or quantity is <b>certain</b> and the other depends on the <b>relative size</b> of the shifts.</p></div>

  <h2>1 · Equilibrium and disequilibrium (2.4.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Equilibrium:</b> Qd = Qs at the <b>equilibrium price</b>; no pressure to change while conditions stay the same. All who want to buy at that price can, and all firms can sell what they supply (the market <b>clears</b>).</li>
    <li><b>Price above equilibrium:</b> Qs &gt; Qd, <b>excess supply</b>. Firms cut prices, so quantity demanded rises and quantity supplied falls, until the surplus is gone.</li>
    <li><b>Price below equilibrium:</b> Qd &gt; Qs, <b>excess demand</b>. Buyers compete, so price rises, quantity supplied rises and quantity demanded falls.</li>
    <li>Disequilibrium can arise from a <b>shift</b> in demand or supply, or from a <b>government price control</b> such as a maximum or minimum price.</li>
    <li><b>Calculation:</b> to find the equilibrium from equations, set Qd = Qs and solve for P, then put P into either equation to find Q.</li>
  </ul>

  <h2>2 · Effects of shifts (2.4.2)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Equilibrium price</th><th>Equilibrium quantity</th></tr>
    <tr><td><b>Demand increases</b> (right)</td><td>Rises</td><td>Rises</td></tr>
    <tr><td><b>Demand decreases</b> (left)</td><td>Falls</td><td>Falls</td></tr>
    <tr><td><b>Supply increases</b> (right)</td><td>Falls</td><td>Rises</td></tr>
    <tr><td><b>Supply decreases</b> (left)</td><td>Rises</td><td>Falls</td></tr>
  </table></div>
  <ul>
    <li><b>Both shift together:</b> demand and supply both up: <b>quantity rises</b>, price depends on which shift is bigger. Demand up and supply down: <b>price rises</b>, quantity depends. Demand down and supply up: <b>price falls</b>, quantity depends. Both down: <b>quantity falls</b>, price depends.</li>
    <li>The <b>size</b> of the change in price and quantity depends on the <b>elasticity</b> of the curves: a shift of demand against an inelastic supply curve raises price a lot and quantity a little.</li>
    <li><b>Use a diagram</b>, show the old and new curves, and label the new equilibrium price and quantity.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always give the <b>definition</b> (Qd = Qs, no tendency to change), a labelled diagram, and a clear statement of <b>both</b> price and quantity. If two curves shift, say which is <b>uncertain</b> and why.</div>
'''

watch = '''
  <h2>1 · The market adjusts to equilibrium</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Both curves shift together</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Set the price</h2>
  <p>Choose a price, then click Adjust to let the market move towards equilibrium one step at a time.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><button class="b" id="adj" type="button">Adjust one step</button>
    <div class="readout"><div><small>Quantity demanded</small><strong id="r1"></strong></div><div><small>Quantity supplied</small><strong id="r2"></strong></div><div><small>State</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with the price set and the gap between quantity demanded and quantity supplied"></svg></div></div></div>

  <h2>Lab 2 · Shift both curves</h2>
  <p>Move demand and supply by different amounts to see which of price and quantity is certain and which is not.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>New price</small><strong id="t1"></strong></div><div><small>New quantity</small><strong id="t2"></strong></div><div><small>Price change</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with both curves shifted by the chosen amounts"></svg></div></div></div>
'''

practise = '''
  <h2>1 · What happens to the equilibrium?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put market adjustment in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Concert tickets", "Tickets priced below what people will pay sell out at once, a shortage. Resale sites show a price closer to equilibrium, because demand exceeds supply at the face price.", "excess demand and the tendency for price to rise.") +
rw("Fruit at the end of a market day", "Stall holders cut prices near closing time to clear unsold stock. A surplus at the daytime price pushes the price down until the quantity supplied matches what people will buy.", "excess supply and the fall in price.") +
rw("Housing", "More people moving to a city raises demand for homes. Supply is slow to respond, so prices rise a lot and quantity rises little: a shift of demand against an inelastic supply curve.", "elasticity and the size of price and quantity changes.") +
rw("Coffee crop failure and a new trend", "A frost cuts supply (left) just as a trend raises demand (right). Price rises for certain, but quantity depends on which shift is bigger.", "two shifts at once and which change is uncertain.")
)

mc_exam = [
  mcq("m20_12", 9, "What must be correct when the free market for a good is in disequilibrium?", ["Consumers can buy all of the good that they demand at the market price", "Producers can sell all of the good that they supply at the market price", "The market price of the good will not change", "The quantity of the good demanded differs from the quantity supplied"], 3, "In disequilibrium quantity demanded and quantity supplied differ."),
  mcq("s20_13", 5, "In a free market there is a surplus of a good. Which change would cause the market to come to an equilibrium?", ["a decrease in demand", "a fall in price", "a government minimum price", "an increase in supply"], 1, "A fall in price reduces the surplus. A minimum price would keep it."),
  mcq("s22_12", 13, "Which statement about market disequilibrium is correct?", ["Price is likely to change", "Supply is equal to demand", "The government must intervene", "There must be shortages"], 0, "Disequilibrium puts pressure on price. It could be a surplus or a shortage."),
  mcq("s22_11", 12, "The price of a product is above the market equilibrium price. Which combination of changes is certain to result as the market adjusts towards equilibrium?", ["quantity demanded falls, quantity supplied falls", "quantity demanded falls, quantity supplied rises", "quantity demanded rises, quantity supplied falls", "quantity demanded rises, quantity supplied rises"], 2, "A falling price extends demand and contracts supply."),
  mcq("m25_12", 10, "The quantity demanded of a product is given by QD = 400 − 10P, when P is the price in dollars. Supply of the product is fixed at 100 units. If the price is $20, what will be the position in the market?", ["It will be in disequilibrium with excess demand of 100 units", "It will be in disequilibrium with excess supply of 100 units", "It will be in equilibrium with 100 units traded", "It will be in equilibrium with 200 units traded"], 0, "QD = 400 − 200 = 200, which is 100 more than the supply of 100."),
  mcq("s20_12", 13, "In the market for a good the quantity supplied and the quantity demanded are given by QS = P − 30 and QD = 240 − 2P where P is the price in dollars. A change in the tax on the good makes QS = P − 36. How will the change affect equilibrium price?", ["It will fall by $2", "It will fall by $6", "It will rise by $2", "It will rise by $6"], 2, "Before: P − 30 = 240 − 2P gives P = 90. After: P − 36 = 240 − 2P gives P = 92, a rise of $2."),
  mcq("m20_12", 11, "The table shows the supply and demand for avocados in Mexico City: at $45, demand 170 and supply 230; at $40, 190 and 190; at $35, 210 and 150; at $30, 230 and 110. As a result of lower transport costs, supply rises by 60 kg at all prices. What is the new equilibrium price?", ["$45", "$40", "$35", "$30"], 2, "At $35 new supply is 150 + 60 = 210, equal to demand."),
  mcq("s21_12", 8, "A market is in equilibrium with 100 units of the product sold at a price of US$10 each. The price elasticity of supply is +2.0 and the price elasticity of demand is −1.0. What will be the state of the market if a minimum price of US$11 is imposed?", ["an excess demand of 10 units", "an excess demand of 30 units", "an excess supply of 20 units", "an excess supply of 30 units"], 3, "A 10% price rise raises quantity supplied by 20% (120) and cuts quantity demanded by 10% (90), so excess supply is 30."),
  mcq("s21_12", 10, "Goods X and Y are complements. What will be the effect on the equilibrium price and quantity of good X of an increase in the supply of good Y?", ["price decreases, quantity decreases", "price decreases, quantity increases", "price increases, quantity decreases", "price increases, quantity increases"], 3, "Cheaper Y raises demand for its complement X, so X's price and quantity both rise."),
  mcq("m21_12", 7, "The table shows a competitive market in equilibrium in two periods: in period 1 the price is 50 cents and quantity 10 000, and in period 2 the price is 60 cents and quantity 12 000. What could explain the change from period 1 to period 2?", ["an increase in the price of a complement", "an increase in the price of a substitute", "the imposition of a minimum price of 60 cents by a government", "the imposition of an indirect tax on suppliers"], 1, "Both price and quantity rose, which means demand shifted right. A dearer substitute does that."),
  mcq("w21_13", 12, "The table shows the market demand and supply for kiwifruit. At $3 per kg demand is 160 thousand tonnes and supply 140 thousand tonnes; at $4, 130 and 150; at $2, 190 and 130. At a market price of $3 per kg there is disequilibrium. Which action would the government have to take to achieve market equilibrium at $3 per kg?", ["impose an indirect tax of $2 per kg on kiwifruit", "purchase the entire supply at $3 per kg and sell at $2 per kg", "set a maximum price of $3 per kg", "subsidise kiwifruit production by $2 per kg"], 3, "Producers need an effective price of $5 to supply 160, so a $2 subsidy makes the market clear at $3."),
  mcq("w22_13", 13, "The market for a product is initially in equilibrium. Which combination of changes will cause the price of the product to rise and the quantity sold to fall?", ["a decrease in demand that is larger than a decrease in supply", "a decrease in demand that is smaller than a decrease in supply", "an increase in demand that is larger than an increase in supply", "an increase in demand that is smaller than an increase in supply"], 1, "Supply falls by more than demand falls, so price rises and quantity falls.")
]

exam = exam_page("market equilibrium and the effects of shifts",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Equilibrium and the effect of shifts is a regular 8 mark Paper 2 topic and is in every Paper 1 series with calculations. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "Feb/March 2021 (22) Q4(a); May/June 2023 (22) Q3(a); Oct/Nov 2020 (23) Q2(a)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("m21_22", "4(a)"), "8 marks", "Explain what is meant by equilibrium price and quantity in the market for a good and how price and quantity will be affected by both a rise in the wage rate paid to the workers producing the good and a rise in wages paid to all workers in the economy.",
     ["Knowledge (up to 2): equilibrium occurs where supply equals demand (1); there is no tendency to change (1).",
      "Application (up to 3): a rise in wages for the producers' workers shifts supply to the left (1) because costs rise (1), so the equilibrium price rises and quantity falls (1).",
      "Application (up to 3): a rise in wages across the economy shifts demand to the right, or to the left in the case of an inferior good (1), because incomes rise (1), with the effect on equilibrium price and quantity explained (1)."],
     "Define equilibrium. Wage rise for this industry: supply left, price up, quantity down. Wages across the economy: demand shifts too.",
     [[("k", "Equilibrium price and quantity occur where quantity demanded equals quantity supplied, so there is no tendency for the price to change while conditions stay the same.")], [("n", "A rise in the wage rate paid to the workers producing the good raises costs, so supply shifts to the left, which raises the equilibrium price and lowers the equilibrium quantity. A rise in wages across the economy raises incomes, so demand for a normal good shifts to the right, which raises price and quantity. For an inferior good, demand could shift to the left instead, so price and quantity could fall.")]]),
  eq(P("s23_22", "3(a)"), "8 marks", "With the help of a diagram, explain what is meant by equilibrium in a market and consider the extent to which the equilibrium price and equilibrium quantity are likely to change for a product following an increase in wages for labour across the whole economy.",
     ["Knowledge (up to 3): the equilibrium point is where quantity demanded equals quantity supplied (1), with no tendency to change (1), shown on an accurately labelled diagram with price and quantity (1).",
      "Analysis (up to 3): either a demand-side approach, with demand shifting right for a normal good or left for an inferior good, or a supply-side approach, with supply shifting left because of higher costs; the best response only is marked.",
      "Evaluation (up to 2): the extent of the change depends on factors such as elasticity and whether the good is normal or inferior."],
     "Define and draw. Pick one route: demand (income up) or supply (costs up). Evaluate with elasticity and good type.",
     [[("k", "Equilibrium is where quantity demanded equals quantity supplied, giving the equilibrium price and quantity, with no tendency to change. The diagram shows demand and supply crossing at P1 and Q1.")], [("n", "A rise in wages across the economy may raise incomes, so demand for a normal good shifts to the right and the equilibrium price and quantity rise. Higher wages could also raise firms' costs, which would shift supply to the left and raise the price, but lower the quantity.")], [("e", "The extent depends on the good: for an inferior good demand shifts left, and for a labour-intensive product the supply effect could be larger. The size of the price rise also depends on the price elasticity of demand and supply.")]]),
  eq(P("w20_23", "2(a)"), "8 marks", "Using diagrams, explain what might cause a market to be in disequilibrium and how market forces would lead to equilibrium being restored.",
     ["Knowledge (up to 2): a diagram showing equilibrium (1) with a clear statement of what equilibrium means (1).",
      "Application (up to 4): a diagram showing disequilibrium and why it might arise, with a shift in demand or supply (1) and a cause of the shift (1); the excess demand or excess supply (1); and the new equilibrium price and quantity (1).",
      "Application (up to 2): an explanation of how market forces restore equilibrium. Maximum or minimum prices are accepted as a cause of disequilibrium."],
     "Equilibrium diagram. Shift one curve (with a cause). Excess demand or supply. Price adjusts to a new equilibrium.",
     [[("k", "A market is in equilibrium when, given present conditions, there is no tendency for change: demand equals supply at the equilibrium price and quantity.")], [("n", "Disequilibrium could arise if a drought shifts the supply of wheat to the left. At the old price quantity demanded exceeds quantity supplied, so there is excess demand. Buyers bid the price up, which contracts demand and extends supply, until the market clears at a higher price and a lower quantity. The same process works in reverse for a surplus, with price falling.")]])
  ],
  )

tips = tips_html(
  [("Define equilibrium properly.", "Qd = Qs and no tendency to change. Say the market clears."),
   ("Say what is certain.", "For two shifts, one of price and quantity is certain."),
   ("Name surplus and shortage correctly.", "Above equilibrium: excess supply. Below: excess demand."),
   ("Draw before and after.", "Label old and new curves and the new equilibrium price and quantity."),
   ("Calculate with equations.", "Set Qd = Qs, solve for P, then find Q."),
   ("Bring in elasticity.", "Steep curves mean bigger price changes."),
   ("Use the sequence.", "Shift, disequilibrium, price change, new equilibrium.")],
  [("Equilibrium", "Equilibrium is where quantity demanded equals quantity supplied."),
   ("Surplus", "A price above equilibrium creates excess supply, so the price may fall."),
   ("Shortage", "A price below equilibrium creates excess demand, so price could rise."),
   ("Both shift", "When both curves shift, the effect on one of price or quantity is uncertain."),
   ("Consider", "The extent depends on elasticity and on the type of good.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- adjustment ---------- */
function adjDraw(s) {
  const a = (90 - s.p) / 0.8, b = (s.p - 10) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 0 });
  const lo = Math.min(a, b), hi = Math.max(a, b);
  o += SV.rect(SDX(lo), SDY(s.p) - 6, Math.abs(SDX(hi) - SDX(lo)), 12, s.p > 50 ? "f2" : "f3", op(0.7)) + SV.line(70, SDY(s.p), SDX(hi), SDY(s.p), "dash") + SV.circle(SDX(a), SDY(s.p), 6, "dot2") + SV.circle(SDX(b), SDY(s.p), 6, "dot1") + SV.text(62, SDY(s.p) + 4, "$" + Lib.fmtN(s.p, 0), "sm", { "text-anchor": "end" });
  const gap = Math.abs(a - b); if (gap > 1) o += tag(SDX(hi) + 10, SDY(s.p) + 4, (s.p > 50 ? "excess supply " : "excess demand ") + Lib.fmtN(gap, 0), s.p > 50 ? "c2" : "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A price above equilibrium creates excess supply">${adjDraw({ p: 70 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The market adjusts from a price above equilibrium", base: { p: 70 }, draw: adjDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Price too high ($70).</b> Quantity supplied (75) exceeds quantity demanded (25): <b>excess supply</b> of 50 units. Stock piles up.", s: { p: 70 } },
  { cap: "<b>Price falls to $60.</b> Firms cut prices to sell stock. Quantity demanded rises and quantity supplied falls, so the surplus narrows.", s: { p: 60 } },
  { cap: "<b>Price reaches $50.</b> Quantity demanded equals quantity supplied (50). This is the <b>equilibrium</b>: the market clears and there is no tendency to change.", s: { p: 50 } },
  { cap: "<b>Price too low ($30).</b> Quantity demanded (75) exceeds quantity supplied (25): <b>excess demand</b>. Buyers bid the price back up.", s: { p: 30 } },
] });

/* ---------- both shift ---------- */
function bothDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand and supply both shift right, quantity rises and price is uncertain">${bothDraw({ d: 25, s: 10, n: 1 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 300, label: "Demand and supply shift at the same time", base: { d: 0, s: 0, n: 0 }, draw: bothDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market is in equilibrium at $50 and 50 units.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Demand shifts right a lot, supply a little.</b> Quantity rises for certain. Price rises as well because the demand shift is bigger.", s: { d: 25, s: 10, n: 1 } },
  { cap: "<b>Supply shifts right more than demand.</b> Quantity still rises. Now price <b>falls</b>. The direction of price depends on the relative size of the shifts.", s: { d: 10, s: 25, n: 1 } },
  { cap: "<b>Equal shifts.</b> Quantity rises by the size of the shift and the price stays the same.", s: { d: 20, s: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, a = Math.max(0, (90 - p) / 0.8), b = Math.max(0, (p - 10) / 0.8), st = Math.abs(a - b) < 0.5 ? "Equilibrium" : a > b ? "Shortage" : "Surplus";
  $("#r1").textContent = Lib.fmtN(a, 0); $("#r2").textContent = Lib.fmtN(b, 0); $("#r3").textContent = st;
  $("#rv").textContent = st === "Equilibrium" ? "Quantity demanded equals quantity supplied at $50. The market clears and nothing pushes the price to change." : st === "Shortage" ? `At $${p} there is a shortage (excess demand) of ${Lib.fmtN(a - b, 0)} units. Buyers compete, so the price tends to rise.` : `At $${p} there is a surplus (excess supply) of ${Lib.fmtN(b - a, 0)} units. Sellers compete, so the price tends to fall.`;
  $("#labA").innerHTML = adjDraw({ p });
}
Lib.slider($("#g1"), { id: "pp", label: "Price, $ ", min: 10, max: 90, step: 5, value: 80, fmt: (v) => "$" + v, onInput: labA });
$("#adj").onclick = () => { const el = $("#pp"), p = +el.value, t = Math.abs(p - 50) < 3 ? 50 : p + (50 - p) * 0.4; el.value = Math.round(t / 5) * 5 === p ? (p > 50 ? p - 5 : p + 5) : Math.round(t / 5) * 5; el.dispatchEvent(new Event("input", { bubbles: true })); };
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, e = sdEq(d, s), e0 = sdEq(0, 0), dp = e.p - e0.p, dq = e.q - e0.q;
  $("#t1").textContent = "$" + Lib.fmtN(e.p, 0); $("#t2").textContent = Lib.fmtN(e.q, 0); $("#t3").textContent = Math.abs(dp) < 0.5 ? "None" : dp > 0 ? "Up" : "Down";
  let msg = "";
  if (d === 0 && s === 0) msg = "Neither curve has moved, so the equilibrium is still $50 and 50 units.";
  else if (d * s > 0) msg = `Both curves shift the same way, so quantity ${dq > 0 ? "rises" : "falls"} for certain. The price ${Math.abs(dp) < 0.5 ? "stays the same because the shifts are equal" : dp > 0 ? "rises because demand moved more" : "falls because supply moved more"}.`;
  else if (d * s < 0) msg = `The curves shift in opposite directions, so price ${dp > 0 ? "rises" : "falls"} for certain. The quantity ${Math.abs(dq) < 0.5 ? "stays the same because the shifts are equal" : dq > 0 ? "rises because the demand shift is larger" : "falls because the supply shift is larger"}.`;
  else msg = `Only ${d !== 0 ? "demand" : "supply"} shifts: price ${dp > 0 ? "rises" : "falls"} and quantity ${dq > 0 ? "rises" : "falls"}.`;
  $("#tv").textContent = msg;
  $("#labB").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
Lib.slider($("#g2"), { id: "dd", label: "Demand shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labB });
Lib.slider($("#g3"), { id: "ss", label: "Supply shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to price and quantity?", ["Both rise", "Both fall", "Price falls, quantity rises", "Price rises, quantity falls"],
  [("Demand shifts right", 0), ("Demand shifts left", 1), ("Supply shifts right", 2), ("Supply shifts left", 3), ("A successful advertising campaign", 0), ("A fall in the cost of raw materials", 2), ("A drought hits a crop", 3), ("Incomes fall (normal good)", 1)],
  "Demand moves price and quantity in the same direction; supply moves them in opposite directions.") + MATCH([
  ["Equilibrium", "Quantity demanded equals quantity supplied"],
  ["Excess supply", "Price is above equilibrium; Qs exceeds Qd"],
  ["Excess demand", "Price is below equilibrium; Qd exceeds Qs"],
  ["Market clearing", "No buyer or seller is left unsatisfied at that price"],
  ["Disequilibrium", "Quantity demanded differs from quantity supplied"],
  ["Equilibrium price", "The price at which the market has no tendency to change"]]) + ORDER(
  "Put the adjustment to a surplus in order.",
  ["The price is above equilibrium", "Quantity supplied exceeds quantity demanded", "Firms cut price to clear stock", "Quantity demanded rises and quantity supplied falls", "The market reaches equilibrium where Qd = Qs"],
  "Surplus pushes the price down until the market clears.") + CALC([
  {"q": "Qd = 120 − 2P and Qs = 3P − 30. What is the equilibrium price ($)?", "a": 30, "unit": "$", "tol": 0.5, "hint": "Set 120 − 2P = 3P − 30.", "sol": "150 = 5P, so P = <b>$30</b>."},
  {"q": "Using the same equations, what is the equilibrium quantity?", "a": 60, "unit": "units", "tol": 0.5, "hint": "Put P = 30 into Qd.", "sol": "120 − 60 = <b>60</b>."},
  {"q": "At a price of $40, what is the excess supply (units)?", "a": 40, "unit": "units", "tol": 0.5, "hint": "Qs = 90, Qd = 40.", "sol": "Qs = 3 × 40 − 30 = 90 and Qd = 120 − 80 = 40, so excess supply is <b>50</b>."},
  {"q": "Qd = 100 − P and Qs = 2P − 20. Find the equilibrium price ($).", "a": 40, "unit": "$", "tol": 0.5, "hint": "100 − P = 2P − 20.", "sol": "120 = 3P, so P = <b>$40</b>."}]) + MCQ([
  ("Equilibrium is where:", ["Quantity demanded equals quantity supplied", "Price is zero", "The government sets the price", "Producers earn maximum revenue"], 0, "The market clears."),
  ("Price above equilibrium causes:", ["Excess supply", "Excess demand", "A shift of demand", "No change"], 0, "Qs exceeds Qd."),
  ("A rise in supply with demand unchanged will:", ["Lower price and raise quantity", "Raise price and lower quantity", "Raise both", "Lower both"], 0, "Right shift of supply."),
  ("Demand and supply both shift right. What is certain?", ["Quantity rises", "Price rises", "Price falls", "Quantity falls"], 0, "Only quantity is certain."),
  ("A market's equilibrium quantity falls and price rises. This is consistent with:", ["A left shift of supply", "A right shift of supply", "A right shift of demand", "A left shift of demand"], 0, "Higher costs reduce supply.")
], "qz1") + CARDS([
  ("Equilibrium", "Qd = Qs, no tendency to change."),
  ("Excess supply", "Price above equilibrium."),
  ("Excess demand", "Price below equilibrium."),
  ("Demand shift", "Price and quantity move together."),
  ("Supply shift", "Price and quantity move oppositely."),
  ("Two shifts", "One of price or quantity is uncertain."),
  ("Solve", "Qd = Qs for P, then Q."),
  ("Market clears", "No one left unsatisfied.")]) + MCQ(mc_exam)

build("as23", "as-market-equilibrium", "Market Equilibrium and the Effects of Shifts", EY,
  "2.4.1 to 2.4.2: equilibrium and disequilibrium, excess supply and excess demand, single and combined shifts of demand and supply. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
