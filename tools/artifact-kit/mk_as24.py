"""AS syllabus 2.4.3 Relationships between markets: joint demand, alternative demand, derived demand, joint supply. Run: python3 tools/artifact-kit/mk_as24.py"""
from asx import *
EY = EYAS("2.4.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Markets are linked, so a change in one market can <b>shift a curve in another</b>. <b class="kw">Joint demand</b> (complements) means goods are used together, so a rise in the price of one lowers demand for the other; <b class="kw">alternative demand</b> (substitutes) means goods can replace each other, so a rise in the price of one raises demand for the other. <b class="kw">Derived demand</b> means demand for an input exists because of demand for the final product it helps make, and <b class="kw">joint supply</b> means producing more of one good automatically produces more of another (a by-product). The <b>cross elasticity of demand</b> (XED) measures the strength and sign of the link: positive for substitutes, negative for complements, zero for unrelated goods.</p></div>

  <h2>1 · Joint demand and alternative demand (2.4.3)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Joint demand (complements)</th><th>Alternative demand (substitutes)</th></tr>
    <tr><td><b>Meaning</b></td><td>Goods used together</td><td>Goods that can replace one another</td></tr>
    <tr><td><b>Examples</b></td><td>Cars and petrol, printers and ink, smartphones and data</td><td>Tea and coffee, bus and train, butter and margarine</td></tr>
    <tr><td><b>Price of X rises</b></td><td>Demand for Y <b>falls</b> (left shift)</td><td>Demand for Y <b>rises</b> (right shift)</td></tr>
    <tr><td><b>Cross elasticity (XED)</b></td><td><b>Negative</b></td><td><b>Positive</b></td></tr>
    <tr><td><b>Strength</b></td><td>The larger the number (ignoring the sign), the stronger the link</td><td>The larger the number, the closer the substitutes</td></tr>
  </table></div>
  <ul>
    <li><b>XED = % change in quantity demanded of Y ÷ % change in price of X.</b> Example: price of rice rises 10% and demand for bread rises 14%: XED = +1.4, strong substitutes. Price of butter rises 10% and demand for bread falls 7%: XED = −0.7, weaker complements.</li>
    <li>A value of <b>zero</b> means the goods are unrelated.</li>
  </ul>

  <h2>2 · Derived demand</h2>
  <div class="card"><div id="pic2"></div></div>
  <ul>
    <li>Demand for <b>steel</b> is derived from demand for cars, buildings and appliances. Demand for <b>labour</b> is derived from demand for what workers make.</li>
    <li>A rise in demand for the final product raises demand for the inputs, so their <b>prices and quantities</b> tend to rise.</li>
    <li>The more <b>inelastic</b> the supply of the input, the more its price rises.</li>
  </ul>

  <h2>3 · Joint supply</h2>
  <ul>
    <li>Goods are in joint supply when producing one <b>necessarily produces another</b>: beef and leather, butter and buttermilk, petrol and diesel from crude oil.</li>
    <li>A rise in demand for beef raises the price of beef, so farmers supply <b>more beef and more leather</b>. The supply of leather shifts <b>right</b>, so leather becomes <b>cheaper</b> and its quantity rises.</li>
    <li>In the market for the product whose demand changed, there is a <b>movement along</b> supply; in the by-product's market there is a <b>shift</b> of supply.</li>
    <li>Joint supply goods are also in <b>joint demand</b> only if consumers buy them together, which is usually not the case.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always say which <b>curve shifts</b> in the second market and why. For XED, give the <b>formula</b>, the <b>sign</b> and what the <b>size</b> means.</div>
'''

watch = '''
  <h2>1 · A rise in the price of a complement or a substitute</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Joint supply: beef and leather</h2>
  <div id="stJ"></div>
'''

explore = '''
  <h2>Lab 1 · How are the markets linked?</h2>
  <p>Choose a relationship, then change the trigger. The diagram shows the market that reacts (the second good).</p>
  <div class="card"><div class="grid2"><div><div id="relB" class="btnrow"></div><div id="g1"></div>
    <div class="readout"><div><small>What shifts</small><strong id="r1"></strong></div><div><small>Price of the second good</small><strong id="r2"></strong></div><div><small>Quantity</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Supply and demand in the second market with the curve that shifts"></svg></div></div></div>

  <h2>Lab 2 · Calculate cross elasticity</h2>
  <p>Change the percentage rise in the price of good X and the percentage change in demand for good Y.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>XED</small><strong id="t1"></strong></div><div><small>Relationship</small><strong id="t2"></strong></div><div><small>Strength</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A number line from negative three to positive three with the cross elasticity marked"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Complement, substitute or unrelated?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the joint supply chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Printers and ink", "Printers are cheap but ink cartridges are dear. Printers and ink are complements: if the price of ink rises, fewer printers are bought. Firms may sell the printer at a low price to earn profit from the ink, which is why demand for one affects the other.", "joint demand and the negative cross elasticity.") +
rw("Bus and train", "A rise in train fares sends some commuters to buses. Demand for buses shifts right, so the bus company may raise fares. The positive cross elasticity between them shows how close the substitutes are.", "alternative demand and substitutes.") +
rw("Steel and cars", "When car sales fall, car makers order less steel. The fall in demand for the input is derived from the fall in demand for the final product, so steel prices and output both tend to fall.", "derived demand.") +
rw("Beef and leather", "More demand for beef raises beef output, which produces more hides. The supply of leather rises, so the price of leather falls without any change in demand for leather.", "joint supply and the movement along one curve with a shift in the other.")
)

mc_exam = [
  mcq("m22_12", 8, "What is the measure of cross-elasticity of demand for good X in terms of good Y?", ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], 2, "XED of X with respect to Y is the percentage change in demand for X divided by the percentage change in the price of Y."),
  mcq("s23_11", 5, "Which row correctly describes the relationship between two goods implied by the value of the cross elasticity of demand?", ["−2.0: weak complements", "−0.5: weak substitutes", "+0.5: weak substitutes", "+2.0: strong complements"], 2, "A positive value means substitutes and a value near zero means a weak link. A negative value means complements."),
  mcq("s20_12", 8, "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges?", ["−0.4", "+0.4", "+2.0", "+2.5"], 3, "Quantity demanded rose 25% (200 ÷ 800) and the price rose 10%, so XED = +25 ÷ 10 = +2.5."),
  mcq("s23_12", 8, "The cross elasticity of demand between bus travel and rail travel is +2. A rise in the price of bus fares caused the demand for rail travel to rise by 10%. Which change in bus fares would have caused this?", ["from 20 cents to 21 cents", "from 30 cents to 33 cents", "from 40 cents to 45 cents", "from 50 cents to 60 cents"], 0, "A 10% rise in rail demand with XED +2 needs a 5% rise in bus fares, which is 20 to 21."),
  mcq("s22_12", 10, "The cross-elasticity of demand of good S with respect to the price of good P is +1.5. The cross-elasticity of demand of good S with respect to the price of good R is −1.5. The cross-elasticity of demand of good P with respect to the price of good R is −1.5. What can be concluded about goods P, R and S?", ["S and P are complements; P and R are substitutes", "S and P are complements; R is an inferior good", "S and P are substitutes; P and R are complements", "S and P are substitutes; R is an inferior good"], 2, "Positive values mean substitutes (S and P) and negative values mean complements (S and R, P and R)."),
  mcq("s24_12", 11, "Which reason for the increase in demand for a smartphone is an example of joint demand?", ["a fall in its price", "a fall in the price of connecting to a network", "a fall in the price of parts used to make smartphones", "a rise in the price of a substitute"], 1, "Network connection is a complement, so its price falling raises demand for the phone."),
  mcq("s22_14", 5, "Goods X and Y are complements and have upward-sloping supply curves. What will be the effect on the equilibrium price and quantity of good X of an increase in the supply of good Y?", ["price decreases, quantity decreases", "price increases, quantity decreases", "price decreases, quantity increases", "price increases, quantity increases"], 3, "Cheaper Y raises demand for X, so price and quantity of X both rise."),
  mcq("s23_13", 9, "What does joint supply mean?", ["A firm can choose between producing a range of different goods", "A good has multiple uses", "A good is a by-product of the production process of another good", "Consumers consider two goods as complements"], 2, "Joint supply is where a by-product is produced with the main product."),
  mcq("m23_12", 11, "Butter and buttermilk are goods in joint supply. Supply curves in both markets slope upwards to the right. Health concerns cause people to reduce their consumption of butter. What are the initial consequences of this for supply in the markets for butter and buttermilk?", ["butter: move left along supply curve; buttermilk: move left along supply curve", "butter: move left along supply curve; buttermilk: shift left of the supply curve", "butter: shift left of the supply curve; buttermilk: move left along supply curve", "butter: shift left of the supply curve; buttermilk: shift left of the supply curve"], 1, "Lower butter demand cuts the price, a movement along butter's supply. Less butter means less buttermilk at every price, a left shift of its supply."),
  mcq("m24_12", 10, "Butter is a normal good. It is in joint demand with bread and in joint supply with buttermilk. The demand for butter increases because of a rise in consumer incomes. What are the effects of this increase on the prices of bread and buttermilk?", ["bread price decreases, buttermilk price decreases", "bread price decreases, buttermilk price increases", "bread price increases, buttermilk price decreases", "bread price increases, buttermilk price increases"], 2, "More butter demand raises bread demand (complement), so bread price rises. Butter output rises, so buttermilk supply rises and its price falls."),
  mcq("s22_13", 10, "Goods X, Y and Z all have downward-sloping demand curves and upward-sloping supply curves. Good X is in joint supply with good Y and in joint demand with good Z. There is an increase in the demand for good X. What will happen to the prices and sales of goods Y and Z?", ["Y: price falls, sales fall; Z: price rises, sales rise", "Y: price falls, sales rise; Z: price rises, sales rise", "Y: price rises, sales fall; Z: price falls, sales rise", "Y: price rises, sales rise; Z: price falls, sales fall"], 1, "More X means more of its by-product Y, so Y's supply rises (price falls, sales rise). Z is a complement of X, so demand for Z rises (price and sales rise)."),
  mcq("s23_12", 6, "Which pair of products are substitutes both in consumption and production?", ["barley and cotton", "gold and silver", "soap and toothpaste", "spinach and cabbage"], 3, "Consumers can replace one leafy vegetable with another and farmers can switch land between them.")
]

exam = exam_page("relationships between markets",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Cross elasticity, joint demand and joint supply are tested in every Paper 1 series and in an 8 mark Paper 2 part nearly every year. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "Oct/Nov 2020 (21) Q3(a); Feb/March 2021 (22) Q3(a); May/June 2021 (22) Q3(a)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("w20_21", "3(a)"), "8 marks", "Cross elasticity of demand for bread with respect to the price of rice is +1.4 while the cross elasticity of demand for bread with respect to the price of butter is −0.7. Explain why the cross elasticity of demand figures for bread differ.",
     ["Knowledge (up to 2): what is meant by XED (1) and the formula (1).",
      "Application (up to 6): bread and rice as substitutes with a positive XED (1 each for the goods as substitutes and applying it to bread and rice), and a strong relationship (1); bread and butter as complements with a negative XED (1 each), and a weak relationship (1)."],
     "Define XED and give the formula. Rice: positive, substitute, strong. Butter: negative, complement, weak.",
     [[("k", "Cross elasticity of demand measures the responsiveness of the quantity demanded of one good to a change in the price of another: the percentage change in quantity demanded of good A divided by the percentage change in the price of good B.")], [("n", "The figure for rice is positive because rice and bread are substitutes: if rice becomes dearer, consumers buy more bread. A value of 1.4 means demand for bread is quite responsive, so they are close substitutes. The figure for butter is negative because bread and butter are complements, bought together: if butter becomes dearer, people buy less bread. The value of 0.7 is smaller in size, so the link is weaker.")]]),
  eq(P("s21_22", "3(a)"), "8 marks", "Explain how the concept of cross-elasticity of demand can be used to distinguish between goods that are substitutes, those that are complements and those that have no relationship.",
     ["Knowledge (up to 2): what XED measures, with the idea of responsiveness (1), and an accurate formula (1).",
      "Application (up to 6): a positive value indicates substitutes and why (2); a negative value indicates complements and why (2); a value of zero indicates unrelated goods and why (2)."],
     "Define and give the formula. Positive: substitutes. Negative: complements. Zero: unrelated. Explain each.",
     [[("k", "Cross elasticity of demand measures how far the quantity demanded of one good responds to a change in the price of another, calculated as the percentage change in quantity demanded of A divided by the percentage change in the price of B.")], [("n", "A positive value shows the goods are substitutes, because a rise in the price of B makes consumers switch to A. A negative value shows they are complements, because a rise in the price of B lowers demand for the good used with it. A value of zero means the quantity demanded of A does not respond to the price of B, so the goods are unrelated.")]]),
  eq(P("m21_22", "3(a)"), "8 marks", "Explain how you would use the concept of cross-elasticity of demand to measure the impact on the demand for cars when there is a rise in the price of fuel for cars and when there is a rise in the price of public transport.",
     ["Knowledge (up to 2): what XED measures (1) and the formula (1).",
      "Application (up to 3): cars and fuel are complements so the coefficient is negative (1), explained (1), and the impact is greater the closer the relationship (1).",
      "Application (up to 3): cars and public transport are substitutes so the coefficient is positive (1), explained (1), and the impact is greater the closer the relationship (1)."],
     "Formula. Fuel: complement, negative, demand for cars falls. Public transport: substitute, positive, demand for cars rises.",
     [[("k", "Cross elasticity of demand is the percentage change in the quantity demanded of cars divided by the percentage change in the price of the other good.")], [("n", "Cars and fuel are complements, so the coefficient is negative: a rise in the price of fuel makes motoring dearer, so demand for cars falls. The closer the relationship, the larger the negative value and the bigger the fall. Cars and public transport are substitutes, so the coefficient is positive: a rise in the price of public transport makes cars more attractive and demand for cars rises, by more if the link is stronger.")]])
  ],
  )

tips = tips_html(
  [("Give the formula for XED.", "% change in quantity of Y ÷ % change in price of X."),
   ("Sign tells the relationship.", "Positive: substitutes. Negative: complements. Zero: unrelated."),
   ("Size tells the strength.", "A larger number means a closer link."),
   ("Name the curve that shifts.", "A rise in a substitute's price shifts demand right."),
   ("Derived demand needs a final product.", "Steel demand follows car demand."),
   ("Joint supply is a by-product.", "More beef means more leather: supply shifts right."),
   ("Use examples.", "Cars and petrol, tea and coffee, beef and leather.")],
  [("Joint demand", "Joint demand means two goods are used together, so a rise in the price of one lowers demand for the other."),
   ("Alternative demand", "Alternative demand means consumers can substitute one good for the other."),
   ("Derived demand", "Demand for an input is derived from demand for the final product."),
   ("Joint supply", "Producing more of one good produces more of a by-product."),
   ("Cross elasticity", "The sign shows whether goods are substitutes or complements.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- complement and substitute ---------- */
function csDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, { y: "Price of cars", D1: "D1", D2: "D2" }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand for cars falls when the price of fuel, a complement, rises">${csDraw({ d: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The market for cars when the price of a related good rises", base: { d: 0, n: 0 }, draw: csDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market for cars is in equilibrium.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of petrol (a complement) rises.</b> Driving costs more, so demand for cars shifts <b>left</b>. XED for cars with respect to petrol is <b>negative</b>.", s: { d: -20, n: 1 } },
  { cap: "<b>The price of public transport (a substitute) rises.</b> Cars look cheaper by comparison, so demand shifts <b>right</b>. XED is <b>positive</b>.", s: { d: 20, n: 1 } },
] });

/* ---------- derived demand chain ---------- */
const bx = (x, y, w, t, v, c = "f1") => SV.rect(x, y, w, 46, c, { rx: 8, ...op(0.55 * v) }) + SV.text(x + w / 2, y + 28, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
function chDraw(s) {
  const ar = (x1, x2, v) => SV.line(x1, 70, x2 - 8, 70, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, 70, "r", "dot4");
  let o = bx(20, 47, 150, "Demand for cars rises", s.a, "f3") + ar(172, 210, s.b) + bx(212, 47, 160, "Car firms order more steel", s.b) + ar(374, 412, s.c) + bx(414, 47, 150, "Demand for steel rises", s.c, "f2") + ar(566, 604, s.d) + bx(606, 47, 130, "Steel price up", s.d, "f1");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 120" role="img" aria-label="Demand for cars rises so car firms order more steel, so demand and price for steel rise">${chDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;

/* ---------- joint supply chain ---------- */
function jsDraw(s) {
  const ar = (x1, x2, y, v) => SV.line(x1, y, x2 - 8, y, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y, "r", "dot4");
  let o = bx(20, 20, 190, "Demand for beef rises", s.a, "f3") + ar(212, 260, 43, s.a) + bx(262, 20, 190, "Beef price and output rise", s.b) + ar(454, 502, 43, s.b);
  o += bx(504, 20, 230, "Movement along beef supply", s.b, "f1");
  o += SV.line(357, 68, 357, 112, "c4", { "stroke-width": 2.5, ...op(s.c) }) + SV.arrowHead(357, 120, "d", "dot4") + bx(20, 124, 200, "More hides are produced", s.c);
  o += ar(222, 262, 147, s.d) + bx(264, 124, 190, "Leather supply shifts right", s.d, "f2") + ar(456, 502, 147, s.e) + bx(504, 124, 230, "Leather price falls", s.e, "f1");
  return o;
}
Lib.stepper($("#stJ"), { w: 760, h: 190, label: "Joint supply of beef and leather", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: jsDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>Demand for beef rises.</b> This is the main product, and the first change in the chain.", s: { a: 1 } },
  { cap: "<b>Beef price and output rise.</b> Farmers move along their beef supply curve.", s: { a: 1, b: 1 } },
  { cap: "<b>More cattle are slaughtered,</b> so more hides are produced as a by-product.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The supply of leather shifts right</b> at every price, because the hides come with the beef.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The price of leather falls</b> and the quantity rises, with no change in demand for leather.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- Lab 1 ---------- */
const REL = [
  ["Complements (joint demand)", "price of the first good", "Demand", -0.6, "A rise in the price of a complement lowers demand for this good."],
  ["Substitutes (alternative demand)", "price of the first good", "Demand", 0.6, "A rise in the price of a substitute raises demand for this good."],
  ["Derived demand", "demand for the final product", "Demand", 0.6, "More demand for the final product raises demand for the input."],
  ["Joint supply", "demand for the main product", "Supply", 0.6, "More of the main product means more of the by-product at every price."],
];
let relI = 0;
function labR() {
  if (!$("#rr")) return;
  const [nm, trig, curve, k, why] = REL[relI], t = +$("#rr").value, sh = Math.max(-30, Math.min(30, k * t)), d = curve === "Demand" ? sh : 0, s = curve === "Supply" ? sh : 0, e = sdEq(d, s), e0 = sdEq(0, 0);
  $$("#relB button").forEach((b, k2) => b.classList.toggle("pri", k2 === relI));
  $("#r1").textContent = Math.abs(sh) < 0.5 ? "Nothing" : curve + (sh > 0 ? " right" : " left"); $("#r2").textContent = "$" + Lib.fmtN(e.p, 0); $("#r3").textContent = Lib.fmtN(e.q, 0);
  $("#rv").textContent = Math.abs(sh) < 0.5 ? `The ${trig} is unchanged, so the second market does not move.` : `${nm}: a ${t > 0 ? "rise" : "fall"} of ${Math.abs(t)}% in the ${trig}. ${why} The curve moves ${sh > 0 ? "right" : "left"}, so the price ${e.p > e0.p ? "rises" : "falls"} and the quantity ${e.q > e0.q ? "rises" : "falls"} in the second market.`.replace(why, t > 0 ? why : "The opposite happens: " + why.charAt(0).toLowerCase() + why.slice(1));
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
$("#relB").innerHTML = REL.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
$$("#relB button").forEach((b) => (b.onclick = () => { relI = +b.dataset.i; labR(); }));
Lib.slider($("#g1"), { id: "rr", label: "Change in the trigger, % ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labX() {
  if (!$("#xp") || !$("#xq")) return;
  const p = +$("#xp").value, q = +$("#xq").value, x = p === 0 ? 0 : q / p, a = Math.abs(x);
  $("#t1").textContent = (x > 0 ? "+" : "") + Lib.fmtN(x, 2); $("#t2").textContent = a < 0.05 ? "Unrelated" : x > 0 ? "Substitutes" : "Complements"; $("#t3").textContent = a < 0.05 ? "None" : a < 1 ? "Weak" : "Strong";
  $("#tv").textContent = a < 0.05 ? `A ${p}% price rise leaves demand unchanged, so XED is about zero and the goods are unrelated.` : `XED = ${q}% ÷ ${p}% = ${x > 0 ? "+" : ""}${Lib.fmtN(x, 2)}. ${x > 0 ? "Positive, so the goods are substitutes" : "Negative, so the goods are complements"}; ${a < 1 ? "the value is below 1 in size, so the link is fairly weak." : "the value is above 1 in size, so the link is strong."}`;
  const X = (v) => 30 + (v + 3) * 60, mx = Math.max(-3, Math.min(3, x));
  let o = SV.line(30, 100, 390, 100) + [-3, -2, -1, 0, 1, 2, 3].map((v) => SV.line(X(v), 94, X(v), 106) + SV.text(X(v), 124, (v > 0 ? "+" : "") + v, "sm", { "text-anchor": "middle" })).join("");
  o += SV.text(X(-1.5), 70, "Complements", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(1.5), 70, "Substitutes", "lbl bd", { "text-anchor": "middle" }) + SV.circle(X(mx), 100, 9, "dot3") + SV.text(X(mx), 82, (x > 0 ? "+" : "") + Lib.fmtN(x, 2), "lbl bd", { "text-anchor": "middle", ...halo });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "xp", label: "% change in the price of good X ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labX });
Lib.slider($("#g3"), { id: "xq", label: "% change in quantity demanded of good Y ", min: -30, max: 30, step: 1, value: 14, fmt: (v) => v + "%", onInput: labX });
labX();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "How are the two goods related?", ["Complements", "Substitutes", "Unrelated"],
  [("Cars and petrol", 0), ("Tea and coffee", 1), ("Printers and ink cartridges", 0), ("Bus travel and train travel", 1), ("Butter and margarine", 1), ("Bread and butter", 0), ("A guitar and a bag of rice", 2), ("Smartphones and mobile data", 0)],
  "Used together: complements. Replace each other: substitutes. No link: unrelated.") + MATCH([
  ["Joint demand", "Goods used together, so demand moves together"],
  ["Alternative demand", "Goods that can replace each other"],
  ["Derived demand", "Demand for an input that comes from demand for the final good"],
  ["Joint supply", "Producing one good also produces another"],
  ["Positive XED", "Substitutes"],
  ["Negative XED", "Complements"]]) + ORDER(
  "Put the joint supply chain in order.",
  ["Demand for beef rises", "Beef price and output rise", "More hides are produced", "The supply of leather shifts to the right", "The price of leather falls"],
  "A by-product's supply shifts when the main product's output changes.") + CALC([
  {"q": "The price of rice rises 10% and demand for bread rises 14%. What is the cross elasticity of demand?", "a": 1.4, "unit": "", "tol": 0.05, "hint": "14 ÷ 10.", "sol": "<b>+1.4</b>: strong substitutes."},
  {"q": "The price of butter rises 10% and demand for bread falls 7%. What is the cross elasticity (include the sign)?", "a": -0.7, "unit": "", "tol": 0.05, "hint": "−7 ÷ 10.", "sol": "<b>−0.7</b>: weaker complements."},
  {"q": "XED between two goods is +0.4. The price of one rises 15%. By what % does demand for the other change?", "a": 6, "unit": "%", "tol": 0.2, "hint": "0.4 × 15.", "sol": "<b>+6%</b>."},
  {"q": "XED of cars with respect to petrol is −0.5. Petrol prices rise 40%. What is the % change in demand for cars (include the sign)?", "a": -20, "unit": "%", "tol": 0.5, "hint": "−0.5 × 40.", "sol": "<b>−20%</b>."}]) + MCQ([
  ("A positive cross elasticity of demand means the goods are:", ["Substitutes", "Complements", "Unrelated", "Inferior"], 0, "Positive XED: substitutes."),
  ("A rise in the price of a complement:", ["Lowers demand for this good", "Raises demand for this good", "Raises supply of this good", "Has no effect"], 0, "Used together."),
  ("Demand for steel is an example of:", ["Derived demand", "Joint supply", "Alternative demand", "Effective demand"], 0, "Steel is demanded because of what it makes."),
  ("Beef and leather are an example of:", ["Joint supply", "Joint demand", "Derived demand", "Alternative demand"], 0, "Leather is a by-product."),
  ("XED = +3 compared with +0.5 shows:", ["A closer substitute", "A weaker substitute", "A complement", "An inferior good"], 0, "A larger positive value means a stronger link.")
], "qz1") + CARDS([
  ("Joint demand", "Complements: used together."),
  ("Alternative demand", "Substitutes: replace each other."),
  ("Derived demand", "Input demand comes from final demand."),
  ("Joint supply", "By-products: one output brings another."),
  ("XED formula", "% change Qd of A ÷ % change price of B."),
  ("Positive XED", "Substitutes."),
  ("Negative XED", "Complements."),
  ("Zero XED", "Unrelated.")]) + MCQ(mc_exam)

build("as24", "as-related-markets", "Relationships Between Markets", EY,
  "2.4.3: joint demand, alternative demand, derived demand and joint supply, with cross elasticity of demand. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
