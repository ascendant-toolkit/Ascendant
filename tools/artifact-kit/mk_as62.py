"""AS syllabus 6.1.2 and 6.1.4 Benefits of free trade and limitations of comparative advantage. Run: python3 tools/artifact-kit/mk_as62.py"""
from asx import *
EY = EYAS("6.1.2 and 6.1.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>When countries <b>specialise</b> in goods in which they have a <b>comparative advantage</b> (a lower opportunity cost) and then trade, total output rises and each country can consume <b>beyond its production possibility curve</b>, shown by the <b class="kw">trading possibility curve (TPC)</b>. <b>Free trade (trade liberalisation)</b> brings gains such as <b>greater choice, lower prices, economies of scale, more competition and efficiency</b>, access to resources and technology, and higher living standards. The theory rests on <b>assumptions</b>: only two goods and countries, constant opportunity costs, no transport costs, mobile factors, full employment and no trade barriers, and in practice these <b>limit</b> the benefits. Free trade can also bring <b>costs</b>: job losses in declining industries, <b>over-specialisation</b> and dependence on a few exports, the risk to <b>infant industries</b>, environmental costs and an uneven sharing of gains.</p></div>

  <h2>1 · Specialisation and the gains from trade (6.1.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Absolute advantage:</b> a country can produce more of a good with the same resources. <b>Comparative advantage:</b> a country can produce a good at a <b>lower opportunity cost</b> than another. Even a country with an absolute advantage in everything gains from trade.</li>
    <li><b>Specialise in the good with the lower opportunity cost</b>, then trade at a price between the two countries' opportunity costs. Both gain.</li>
    <li>The <b>trading possibility curve</b> lies <b>outside</b> the PPC: it shows the combinations a country can consume after specialising and trading at the terms of trade.</li>
  </ul>

  <h2>2 · Free trade: advantages and disadvantages</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Higher world output</b> and living standards</td><td><b>Job losses</b> in industries that cannot compete; structural unemployment</td></tr>
    <tr><td><b>Greater choice</b> and <b>lower prices</b> for consumers</td><td><b>Over-specialisation and dependence</b> on a few commodities or trading partners</td></tr>
    <tr><td><b>Economies of scale</b> from larger markets</td><td><b>Infant industries</b> may not survive competition from established firms</td></tr>
    <tr><td><b>Competition</b> forces efficiency and innovation</td><td>Possible <b>security risk</b> if vital goods are imported</td></tr>
    <tr><td>Access to resources, technology and ideas</td><td><b>Environmental damage</b> and unequal distribution of gains</td></tr>
  </table></div>

  <h2>3 · Limitations of comparative advantage (6.1.4)</h2>
  <ul>
    <li><b>Transport costs and trade barriers</b> reduce or remove the gains from trade.</li>
    <li><b>Opportunity costs are not constant:</b> as a country specialises, costs may rise (diminishing returns), reducing the advantage.</li>
    <li><b>Factors are not perfectly mobile:</b> workers displaced from one industry cannot easily move into another.</li>
    <li><b>Comparative advantage changes over time</b> (a dynamic, not a static, advantage) and can be created by policy, education and investment.</li>
    <li><b>Over-specialisation</b> is risky when demand or prices for the specialised good collapse, and the <b>terms of trade</b> may worsen for primary producers.</li>
    <li><b>The theory ignores</b> externalities, exchange rate movements, imperfect competition, the distribution of the gains and non-economic aims such as security.</li>
    <li><b>Many goods</b> are not homogeneous, and trade is also determined by tastes and brands, not just costs.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Define comparative advantage with <b>opportunity cost</b>. For limitations, give <b>developed</b> reasons (each worth marks) such as transport costs, immobility, changing opportunity costs and over-specialisation. In evaluation, say the theory is a useful guide but its assumptions limit how far it applies.</div>
'''

watch = '''
  <h2>1 · Specialisation raises total output</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · The trading possibility curve</h2>
  <div id="stT"></div>
'''

explore = '''
  <h2>Lab 1 · Do the gains exist?</h2>
  <p>Country A can make 10 cars or 20 wheat. Country B can make 12 cars or a number of wheat that you choose. Set B's wheat output and see who has the comparative advantage and the gain from specialising.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Opportunity cost of a car: A</small><strong id="r1"></strong></div><div><small>Opportunity cost of a car: B</small><strong id="r2"></strong></div><div><small>Gain from specialising</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of the opportunity cost of cars in each country"></svg></div></div></div>

  <h2>Lab 2 · What limits the gains?</h2>
  <p>Choose a limitation. The diagram shows how much of the potential gain survives.</p>
  <div class="card"><div class="grid2"><div><div id="lB" class="btnrow"></div>
    <div class="readout"><div><small>Limitation</small><strong id="t1"></strong></div><div><small>Gain left</small><strong id="t2"></strong></div><div><small>Who is hurt</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="A bar of the gains from trade remaining after the chosen limitation"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Advantage or disadvantage of free trade?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the gains from specialisation in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Tea and cars", "A country with fertile land and a climate suited to tea produces it at a low opportunity cost, while a country with skilled engineers produces cars cheaply. If each specialises and trades, both can consume more tea and more cars.", "comparative advantage and gains from trade.") +
rw("Transport costs", "Heavy, low-value goods such as bricks cost so much to ship that trade is unprofitable. Transport costs reduce the benefits of specialisation and are a limit of the theory.", "limitations of comparative advantage.") +
rw("A one-product economy", "A country that specialises in exporting copper depends on its price. When copper prices fall, incomes, jobs and the exchange rate all suffer: the risk of over-specialisation.", "over-specialisation and dependence.") +
rw("Infant industries", "A new domestic car industry cannot compete with established foreign producers that have huge economies of scale. Free trade could kill it before it has the chance to grow, a case for temporary protection.", "disadvantages of free trade.")
)

mc_exam = [
  mcq("s21_12", 24, "Two statements are shown. 1: A country can produce a good at a lower opportunity cost than another country. 2: A country can produce a greater quantity of a good for the same quantity of inputs than another country. What do these two statements describe? (1, 2)", ["absolute advantage, comparative advantage", "absolute advantage, the terms of trade", "comparative advantage, absolute advantage", "the terms of trade, comparative advantage"], 2, "A lower opportunity cost is comparative advantage; more output from the same inputs is absolute advantage."),
  mcq("s20_12", 22, "Which argument is an importer most likely to use to gain the support of consumers for free trade?", ["More imports allow the government to raise revenue from tariffs", "More imports improve the country's terms of trade", "More imports increase competition in the domestic economy", "More imports raise total employment in the domestic economy"], 2, "Consumers benefit from competition, which brings lower prices and more choice."),
  mcq("s20_12", 26, "The statements relate to possible gains from an increase in free trade. Which gain is least certain to result in the short run?", ["a reduction in costs of production", "a rise in the number of jobs", "a wider choice of goods available to consumers", "an increase in the level of competition"], 1, "In the short run, imports may displace domestic jobs, so a rise in jobs is least certain."),
  mcq("s20_13", 26, "An economy with a long history of extensive barriers to trade decides to switch to totally free trade. What is most likely to increase in the short term?", ["consumer surplus", "government revenue", "inflationary pressure", "profits of all domestic companies"], 0, "Cheaper imports raise consumer surplus. Tariff revenue falls and some domestic firms lose."),
  mcq("s21_13", 23, "What may increase the benefits a country gains from international trade?", ["a reduction in transportation costs because of a fall in world oil prices", "domestic wage rates increase at a faster rate than output per worker", "the domestic labour force becomes more occupationally immobile", "trading partners increase tariffs on imported goods"], 0, "Lower transport costs raise the gains from trade. Rising unit labour costs, immobility and tariffs reduce them."),
  mcq("m20_12", 21, "Four countries, A, B, C and D, trade internationally. Each circle in the diagram represents a free trade area between the countries within the circle. A country can belong to more than one free trade area. Countries outside of a circle face trade barriers. Which country has the greatest opportunity to benefit from free international trade?", ["A", "D", "C", "B"], 1, "The country that belongs to the most free trade areas has the greatest tariff-free access."),
  mcq("m20_12", 27, "In a closed economy a rise in aggregate demand is needed to increase output in the country. What is necessary to achieve this increase in output in the economy?", ["enough capacity to produce the extra goods and services demanded", "free trade to allow imports to make up any shortages in supply", "government spending to be less than tax revenue", "reduced credit to lower inflation"], 0, "In a closed economy there are no imports, so output can only rise if capacity exists.")
]

exam = exam_page("the benefits of free trade and the limits of comparative advantage",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Comparative advantage, free trade and their limits are a regular 8 or 12 mark Paper 2 part and a 2 mark definition in the data response. Reworded past questions are below, with seven Paper 1 multiple choice questions that do not need a diagram.",
  [("Essay parts, 8 marks", "3", "May/June 2020 (23) Q4(a); Oct/Nov 2024 (21) Q5(a); May/June 2021 (23) Q4(a)"), ("Essay parts, 12 marks", "1", "Feb/March 2025 (22) Q4(b)"), ("Data response, 2 marks", "1", "May/June 2024 (21) Q1(b)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2024")],
  [
  eq(P("s20_23", "4(a)"), "8 marks", "Explain why the theory of comparative advantage may not give a true account of the benefits of free trade.",
     ["Knowledge (up to 2): a lower opportunity cost of producing a product because of differing resources (1), which leads to specialisation and trade (1).",
      "Application (up to 6): consideration of reasons why the law of comparative advantage may not lead to benefits through trade, up to 2 marks for each reason explained, for example transport costs, trade barriers, immobility of factors, changing opportunity costs and over-specialisation."],
     "Define comparative advantage (opportunity cost). Then three developed limits: transport costs, immobility, increasing opportunity costs or over-specialisation.",
     [[("k", "A country has a comparative advantage in a good if it can produce it at a lower opportunity cost than another country because of its resources. It should specialise in that good and trade for others.")], [("n", "The benefits may be smaller than the theory suggests. Transport costs and tariffs raise the price of traded goods and can remove the gain. Factors are not perfectly mobile: workers who lose their jobs in one industry may not have the skills to move into another, so unemployment results. Opportunity costs may rise as a country specialises, because the best resources are used first, which weakens the advantage, and over-specialisation makes an economy vulnerable to a fall in the price of its main export.")]]),
  eq(P("w24_21", "5(a)"), "8 marks", "Explain the potential advantages of free trade and consider whether such advantages are always greater than the potential disadvantages of free trade.",
     ["Knowledge (up to 3): at least two advantages of free trade, such as an increase in world output, a wider range of products for consumers and an improved standard of living.",
      "Analysis (up to 3): at least two disadvantages and how they contrast with the advantages: specialisation could cause some sectors to run down, with higher unemployment; overreliance on some commodities is risky; there is a security risk if vital resources are imported.",
      "Evaluation (up to 2): a valid judgement on whether the advantages are always greater than the disadvantages, with a conclusion."],
     "Two advantages: world output, choice, living standards. Two disadvantages: unemployment in declining sectors, dependence. Judge: advantages usually bigger, but not always.",
     [[("k", "Free trade allows countries to specialise in goods in which they have a comparative advantage, which raises world output. Consumers get a wider choice of goods at lower prices, and living standards can rise.")], [("n", "But free trade can cause some industries to decline when they cannot compete with cheaper imports, which raises unemployment in those sectors. Countries that specialise in a few commodities depend heavily on their prices, and relying on imports of vital resources may be a security risk.")], [("e", "The advantages are probably greater for most countries over time, because of higher output and lower prices, but they are not always greater: the costs fall on particular workers and regions and can be severe for developing countries that depend on one export.")]]),
  eq(P("s21_23", "4(a)"), "8 marks", "Explain how a free trade area differs from a customs union and explain two reasons why countries move towards tariff-free trade.",
     ["Knowledge (up to 2): what a free trade area is (1) and how a customs union differs from it (1): the main difference is a common external tariff in a customs union.",
      "Application (up to 6): identification of a reason countries move to tariff-free trade (1) and up to 2 marks for explaining the benefits, for each of two reasons (3 maximum per reason). Benefits include specialisation, higher living standards, cheaper and better quality products and more choice, increased employment and benefiting from comparative advantage."],
     "FTA: no tariffs between members, each sets its own external tariffs. Customs union: common external tariff. Two benefits: specialisation, choice and lower prices.",
     [[("k", "In a free trade area, members trade with each other without tariffs, but each member sets its own tariffs on trade with non-members. A customs union goes further by adopting a common external tariff.")], [("n", "Countries move towards tariff-free trade to benefit from specialisation: each can concentrate on goods with a comparative advantage, raising output and incomes. They also give consumers cheaper and better products, with greater choice, because competition from imports forces domestic firms to improve.")]]),
  eq(P("s24_21", "1(b)"), "2 marks", "Explain what is meant by 'a country has enjoyed a comparative advantage in growing and exporting tea'.",
     ["The country can grow and export tea at a lower opportunity cost (1) than another country (1). Both parts must be clear for full marks."],
     "Lower opportunity cost than another country.",
     [[("k", "It means the country can grow and export tea at a lower opportunity cost than other countries, giving up less of other goods to produce each tonne of tea.")]])
  ],
  )

tips = tips_html(
  [("Define with opportunity cost.", "Comparative advantage is a lower opportunity cost."),
   ("Show specialisation and trade.", "Both countries can consume beyond their PPC."),
   ("List gains.", "Output, choice, prices, scale, competition."),
   ("List costs.", "Job losses, dependence, infant industries."),
   ("Give developed limits.", "Transport costs, immobility, rising opportunity costs."),
   ("Mention dynamic change.", "Comparative advantage changes and can be created."),
   ("Judge.", "Gains usually exceed costs overall, but not for everyone.")],
  [("Comparative advantage", "A country has a comparative advantage if it can produce a good at a lower opportunity cost."),
   ("Specialisation", "Specialisation allows countries to produce more in total."),
   ("TPC", "The trading possibility curve lies outside the PPC."),
   ("Limits", "Transport costs and factor immobility reduce the gains."),
   ("Judge", "The advantages may not always be greater than the disadvantages.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- specialisation bars ---------- */
function spDraw(s) {
  const Y = (v) => 250 - v * 8; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 30) + SV.text(66, 24, "Units of output", "sm");
  const bar = (x, v, c, l) => SV.rect(x, Y(v), 40, 250 - Y(v), c, op(0.7)) + SV.text(x + 20, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 20, 268, l, "sm", { "text-anchor": "middle" });
  const before = s.k < 0.5, carsA = before ? 5 : 0, whA = before ? 10 : 20, carsB = before ? 6 : 12, whB = before ? 6 : 0;
  o += bar(100, carsA, "f3", "A cars") + bar(150, whA, "f2", "A wheat") + bar(230, carsB, "f3", "B cars") + bar(280, whB, "f2", "B wheat");
  o += bar(400, carsA + carsB, "f3", "Total cars") + bar(450, whA + whB, "f2", "Total wheat");
  o += tag(560, 80, before ? "Each splits its resources" : "Each specialises", "c3", 1, "start") + tag(560, 100, before ? "11 cars, 16 wheat" : "12 cars, 20 wheat", "c1", 1, "start") + (before ? "" : tag(560, 122, "More of both", "c2", 1, "start"));
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 285" role="img" aria-label="After specialisation world output rises from 11 cars and 16 wheat to 12 cars and 20 wheat">${spDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 285, label: "Specialising raises world output", base: { k: 0 }, draw: spDraw, tween: 700, dwell: 5400, steps: [
  { cap: "<b>Before trade.</b> Country A (10 cars or 20 wheat) and country B (12 cars or 12 wheat) each use half their resources on each good. Totals: 11 cars and 16 wheat. A's opportunity cost of a car is 2 wheat; B's is 1 wheat.", s: { k: 0 } },
  { cap: "<b>After specialisation.</b> B has the comparative advantage in cars (lower opportunity cost) and A in wheat. B makes 12 cars and A 20 wheat. Total output is 12 cars and 20 wheat: <b>more of both</b>, so there are gains to share through trade.", s: { k: 1 } },
] });

function tpDraw(s) {
  const X = (q) => 80 + q * 36, Y = (p) => 260 - p * 10; let o = axes(80, 260, 560, 30, "Cars", "Wheat");
  o += SV.line(X(0), Y(20), X(10), Y(0), "c1", { "stroke-width": 3 }) + tag(X(10) + 6, Y(0) - 4, "PPC", "c1");
  if (s.t > 0) o += SV.line(X(0), Y(20), X(13.33), Y(0), "c2", { "stroke-width": 3, "stroke-dasharray": "7 4", ...op(s.t) }) + tag(X(13.33) + 6, Y(0) - 4, "TPC", "c2", s.t);
  if (s.p > 0) o += SV.circle(X(4), Y(10), 6, "dot1", op(s.p)) + SV.text(X(4) - 8, Y(10) - 10, "Without trade", "sm", { "text-anchor": "end", ...op(s.p) }) + SV.circle(X(6), Y(11), 8, "dot3", op(s.p)) + SV.text(X(6) + 14, Y(11) - 10, "With trade: more cars and wheat", "lbl bd", { ...halo, ...op(s.p) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="The trading possibility curve lies outside the production possibility curve">${tpDraw({ t: 1, p: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 290, label: "The PPC and the trading possibility curve for country A", base: { t: 0, p: 0 }, draw: tpDraw, tween: 800, dwell: 5400, steps: [
  { cap: "<b>The PPC.</b> Country A can produce 20 wheat or 10 cars (or combinations). Without trade it can only consume on or inside this line.", s: { t: 0, p: 0 } },
  { cap: "<b>Specialise and trade.</b> A specialises in wheat and trades at a price of 1 car for 1.5 wheat. It can now reach any point on the <b>trading possibility curve</b>, which lies outside the PPC.", s: { t: 1, p: 0 } },
  { cap: "<b>Gains from trade.</b> A can consume 6 cars and 11 wheat, more of both than the 4 cars and 10 wheat it could have had without trade.", s: { t: 1, p: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#bw")) return;
  const w = +$("#bw").value, ocA = 2, ocB = w / 12, gain = Math.abs(ocA - ocB), who = ocB < ocA ? "B" : ocB > ocA ? "A" : "Neither";
  $("#r1").textContent = "2 wheat"; $("#r2").textContent = Lib.fmtN(ocB, 2) + " wheat"; $("#r3").textContent = gain < 0.01 ? "None" : "Possible";
  $("#rv").textContent = gain < 0.01 ? "Both countries have the same opportunity cost, so neither has a comparative advantage and there is no gain from specialising." : `A gives up 2 wheat per car and B gives up ${Lib.fmtN(ocB, 2)}. ${who === "B" ? "B has the comparative advantage in cars, and A has it in wheat." : "A has the comparative advantage in cars, and B in wheat."} Each should specialise where its opportunity cost is lower, and trade at a price between ${Lib.fmtN(Math.min(2, ocB), 2)} and ${Lib.fmtN(Math.max(2, ocB), 2)} wheat per car. B ${w >= 20 ? "even has an absolute advantage in both goods" : w < 20 ? "has an absolute advantage in cars but not in wheat" : ""}.`;
  const Y = (v) => 250 - v * 40; let o = SV.line(40, 250, 400, 250);
  [["A: cost of a car", ocA, "f3"], ["B: cost of a car", ocB, "f2"]].forEach(([l, v, c], i) => (o += SV.rect(80 + i * 150, Y(v), 100, 250 - Y(v), c, op(0.65)) + SV.text(130 + i * 150, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(130 + i * 150, Y(v) - 6, Lib.fmtN(v, 2) + " wheat", "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "bw", label: "B's maximum wheat output, units ", min: 6, max: 30, step: 2, value: 12, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
const LM = [["No limits (the theory)", 100, "Nobody", "Both countries gain the full amount."], ["Transport costs", 60, "Both countries", "Shipping costs eat into the price advantage, so less trade is worthwhile."], ["Tariffs and trade barriers", 50, "Consumers and exporters", "Taxes on imports raise prices and invite retaliation."], ["Immobile workers", 55, "Displaced workers", "Workers in declining industries cannot easily move to expanding ones, so unemployment results."], ["Rising opportunity costs", 65, "The specialising country", "As output of one good expands, resources become less suited, reducing the advantage."], ["Over-specialisation", 45, "Countries dependent on one export", "A fall in the world price of the main export causes a collapse in incomes."]];
function showL(i) {
  const [n, g, who, why] = LM[i]; $$("#lB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = n; $("#t2").textContent = g + "%"; $("#t3").textContent = who; $("#tv").textContent = `${n}: ${why} About ${g}% of the potential gain from trade remains in this illustration.`;
  $("#labB").innerHTML = SV.rect(60, 70, 300, 40, "f1", op(0.2)) + SV.rect(60, 70, 3 * g, 40, g > 60 ? "f2" : "f3", op(0.7)) + SV.text(210, 60, "Potential gain from trade = 100%", "lbl bd", { "text-anchor": "middle" }) + SV.text(210, 140, g + "% remains", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
}
$("#lB").innerHTML = LM.map((l, i) => `<button class="b" data-i="${i}">${l[0]}</button>`).join("");
$$("#lB button").forEach((b) => (b.onclick = () => showL(+b.dataset.i)));
showL(1);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Advantage or disadvantage of free trade?", ["Advantage", "Disadvantage"],
  [("Greater choice for consumers", 0), ("Job losses in industries that cannot compete", 1), ("Lower prices from competition", 0), ("Over-reliance on a few exports", 1), ("Economies of scale from larger markets", 0), ("Infant industries may fail", 1), ("Higher world output", 0), ("Security risk if vital resources are imported", 1)],
  "Free trade raises output and choice but may harm uncompetitive industries and create dependence.") + MATCH([
  ["Comparative advantage", "Lower opportunity cost of producing a good"],
  ["Absolute advantage", "Can produce more with the same resources"],
  ["Specialisation", "Concentrating on the good with the lower opportunity cost"],
  ["Trading possibility curve", "What a country can consume after specialising and trading"],
  ["Infant industry", "A new industry that cannot yet compete with established rivals"],
  ["Over-specialisation", "Dependence on one or a few exports"]]) + ORDER(
  "Put the gains from specialisation in order.",
  ["Each country finds its lower opportunity cost good", "Each specialises in that good", "Total output rises", "The countries trade at a price between their opportunity costs", "Both can consume more than before"],
  "Specialise, produce more in total, trade, both gain.") + CALC([
  {"q": "A can make 10 cars or 20 wheat. What is A's opportunity cost of one car (wheat)?", "a": 2, "unit": "wheat", "tol": 0.05, "hint": "20 ÷ 10.", "sol": "<b>2 wheat</b>."},
  {"q": "B can make 12 cars or 12 wheat. What is B's opportunity cost of one car (wheat)?", "a": 1, "unit": "wheat", "tol": 0.05, "hint": "12 ÷ 12.", "sol": "<b>1 wheat</b>: B has the comparative advantage in cars."},
  {"q": "What is A's opportunity cost of one wheat in cars?", "a": 0.5, "unit": "cars", "tol": 0.02, "hint": "10 ÷ 20.", "sol": "<b>0.5 cars</b>."},
  {"q": "Before trade the two countries together produce 16 wheat. After specialising A makes 20 wheat. How many more wheat is that?", "a": 4, "unit": "wheat", "tol": 0.2, "hint": "20 − 16.", "sol": "<b>4</b>, with 1 more car too."}]) + MCQ([
  ("Comparative advantage means a lower:", ["Opportunity cost", "Price", "Wage", "Tax"], 0, "Opportunity cost."),
  ("The trading possibility curve is:", ["Outside the PPC", "Inside the PPC", "The same as the PPC", "Below the axes"], 0, "Gains from trade."),
  ("A limitation of comparative advantage is:", ["Transport costs", "Perfect mobility", "No trade barriers", "Constant costs"], 0, "Reduce gains."),
  ("An infant industry is at risk from:", ["Free trade", "Protection", "Subsidies", "Tariffs"], 0, "Established competitors."),
  ("A benefit of free trade is:", ["Greater choice for consumers", "Higher unemployment always", "Fewer exports", "Less competition"], 0, "Variety and lower prices.")
], "qz1") + CARDS([
  ("Comparative advantage", "Lower opportunity cost."),
  ("Absolute advantage", "More output per input."),
  ("TPC", "Outside the PPC."),
  ("Gains", "Output, choice, prices, scale."),
  ("Costs", "Jobs, dependence, infant industries."),
  ("Limits", "Transport, immobility, rising costs."),
  ("Dynamic", "Advantage can change."),
  ("Judge", "Usually positive, not for everyone.")]) + MCQ(mc_exam)

build("as62", "as-free-trade-comparative-advantage-limits", "Free Trade and the Limits of Comparative Advantage", EY,
  "6.1.2 and 6.1.4: specialisation, the trading possibility curve, the advantages and disadvantages of free trade, and the limitations of the theories of absolute and comparative advantage. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
