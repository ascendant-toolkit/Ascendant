"""AS syllabus 1.1.1-1.1.4 Scarcity, choice, opportunity cost and the basic questions. Run: python3 tools/artifact-kit/mk_as11.py"""
from asx import *
EY = EYAS("1.1.1 to 1.1.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">fundamental economic problem</b> is <b>scarcity</b>: human wants are unlimited but the resources to satisfy them are limited, and this is true for rich and poor alike. Scarcity forces <b class="kw">choice</b> at every level, by individuals, firms and governments, because choosing one thing means going without another. The <b class="kw">opportunity cost</b> of a choice is the <b>value of the next best alternative that is given up</b>. Every economy has to answer three <b>basic questions</b>: <b>what</b> to produce, <b>how</b> to produce it and <b>for whom</b> to produce.</p></div>

  <h2>1 · Scarcity (1.1.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Wants</b> are unlimited: people always want more or better goods and services. <b>Resources</b> (land, labour, capital and enterprise) are limited. Scarcity is the gap between the two.</li>
    <li>Scarcity applies to <b>every society</b>, rich or poor, because wants are never completely satisfied. It is a permanent problem, not a temporary one.</li>
    <li><b>Scarcity is not the same as a shortage.</b> A shortage is a situation in a market where demand is greater than supply at the current price and can be removed by a price rise. Scarcity cannot be removed.</li>
    <li>Scarce resources have a <b>cost</b>. A <b>free good</b> is a rare case with no scarcity and no opportunity cost (see syllabus 1.6).</li>
  </ul>

  <h2>2 · Choice (1.1.2)</h2>
  <div class="tw"><table class="t">
    <tr><th>Who chooses</th><th>Example of a choice</th><th>What is given up</th></tr>
    <tr><td><b>Individuals</b></td><td>How to spend a month's income; how to spend an evening</td><td>The next best use of the money or time</td></tr>
    <tr><td><b>Firms</b></td><td>Which product to make, whether to buy a machine or hire workers</td><td>The profit from the alternative use of the same resources</td></tr>
    <tr><td><b>Governments</b></td><td>Spending on hospitals or on schools; cutting taxes or building roads</td><td>The services that the money could have funded</td></tr>
  </table></div>

  <h2>3 · Opportunity cost (1.1.3)</h2>
  <ul>
    <li><b>Opportunity cost</b> is the value of the <b>next best alternative forgone</b> when a choice is made. It is not the total of all alternatives, only the single best one that is given up.</li>
    <li>It is often <b>not the money price</b>. The opportunity cost of studying all evening is the best other use of the evening. For a firm it may be the profit from the next best product.</li>
    <li>It can be measured in <b>units of the other good</b>. If a firm produces 100 units of Y and 200 of X, and moving to 120 of Y leaves only 170 of X, the opportunity cost of the extra 20 Y is <b>30 units of X</b>.</li>
    <li>For a government, spending $800,000 of a $1.2m buildings budget on cancer care means the opportunity cost is the <b>lost new buildings</b> (the next best use), not the cancer care itself.</li>
    <li>Opportunity cost explains why every choice has a cost, even when the good seems free.</li>
  </ul>

  <h2>4 · The basic questions of resource allocation (1.1.4)</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>What it asks</th><th>Example</th></tr>
    <tr><td><b>What to produce?</b></td><td>Which goods and services, and how much of each</td><td>More food or more cars; more hospitals or more roads</td></tr>
    <tr><td><b>How to produce?</b></td><td>Which methods and resources: labour-intensive or capital-intensive, which technology</td><td>Hand-picking crops or using harvesting machines</td></tr>
    <tr><td><b>For whom to produce?</b></td><td>Who gets the output: how income and goods are shared</td><td>Whether goods go to those who can pay, or are shared by need</td></tr>
  </table></div>
  <p>Different economic systems answer these questions in different ways (syllabus 1.4): the price mechanism in a market economy, central planning in a planned economy, and a mixture in most economies today.</p>
  <div class="tip"><b class="h">Exam tip</b>Do not write that scarcity means "not enough". Say that <b>wants are unlimited and resources are limited</b>, so choices must be made, and that every choice has an opportunity cost.</div>
'''

watch = '''
  <h2>1 · From scarcity to choice to opportunity cost</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · What is the opportunity cost?</h2>
  <div id="stO"></div>
'''

explore = '''
  <h2>Lab 1 · A government budget</h2>
  <p>A government has $100m for hospitals and schools only. Choose how much goes to each. Every extra $10m for one is $10m taken from the other.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Hospitals</small><strong id="r1"></strong></div><div><small>Schools</small><strong id="r2"></strong></div><div><small>Opportunity cost of the last $10m</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="A bar split between hospital spending and school spending that adds up to the budget"></svg></div></div></div>

  <h2>Lab 2 · Find the next best alternative</h2>
  <p>A family can afford only one of four holidays, each at the same price. Score each destination from 1 to 10. The family picks its favourite. The opportunity cost is the next best alternative, not all the others.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Chosen</small><strong id="t1"></strong></div><div><small>Opportunity cost</small><strong id="t2"></strong></div><div><small>Others given up</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars for four holiday options with the chosen option and the next best marked"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Individual, firm or government?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A pandemic lockdown", "In 2020 governments ordered non-essential businesses to close to save lives. The benefit was fewer infections; the opportunity cost included the output, jobs and incomes of the closed businesses, and the services that the extra spending could have funded.", "opportunity cost at the level of a government, where both the benefits and the cost are large.") +
rw("A hospital budget", "A hospital board has a fixed budget and must decide between new buildings and cancer treatment. Spending more on one leaves less for the other. The opportunity cost of the choice is the buildings that are not built, which is the next best use of the money.", "opportunity cost is the next best alternative, shown in the form of what is lost.") +
rw("A doctor becoming a teacher", "A doctor with long hours and high stress could become a teacher instead. Staying a doctor has the opportunity cost of the salary and the lifestyle she would have as a teacher, which is the next best job, not every possible job.", "opportunity cost for an individual, in terms of income and satisfaction.") +
rw("Fossil fuels", "Oil and coal are limited in supply, while demand for energy grows. They are scarce because supply is not enough to meet all wants at a zero price. Using more fossil fuels for electricity leaves less for plastics and transport, so each use has an opportunity cost.", "scarcity of a natural resource and the choice of how to use it.")
)

mc_exam = [
  mcq("m21_12", 1, "An American family chooses between four holiday destinations at the same price. Their order of preference is Barcelona 1st, Paris 2nd, London and Venice joint 3rd. If they go to Barcelona, what is the opportunity cost?", ["Barcelona", "London and Venice", "Paris", "London, Paris and Venice"], 2, "Opportunity cost is the next best alternative given up, which is the second choice, Paris. It is not all the others."),
  mcq("m23_12", 10, "Why does the basic economic problem of scarcity apply to both the rich and the poor?", ["The choices people make do not depend on income inequalities", "Consumers pay the same prices for goods and services", "Human wants exceed what can be produced from available resources", "Natural resources are unevenly distributed among nations"], 2, "Scarcity comes from unlimited wants and limited resources, so it applies at every income level."),
  mcq("m24_12", 3, "Which combination best describes the basic economic problem? Resources, and wants.", ["Limited, limited", "Limited, unlimited", "Unlimited, limited", "Unlimited, unlimited"], 1, "Limited resources cannot meet unlimited wants."),
  mcq("m24_12", 5, "What is the opportunity cost to a person of spending $20 on a new pair of sports shoes?", ["All the other things the person could have bought", "The cost of getting to the shop", "The current value of the old pair of shoes", "The next best thing that could have been bought with the $20"], 3, "Opportunity cost is the single next best alternative, not all alternatives and not a related cost."),
  mcq("s22_13", 3, "What does opportunity cost measure?", ["The benefits of a good compared with the next choice", "The benefits given up by not consuming the next best alternative", "The costs of any good not chosen", "The financial costs of consuming a good"], 1, "It is the benefit of the next best alternative that is forgone."),
  mcq("s22_11", 3, "Complete the sentence: the three basic questions arising from scarcity are ___ to produce, ___ to produce and ___ to produce.", ["How, when, where", "How, where, for whom", "What, how, for whom", "What, when, where"], 2, "The three basic questions are what, how and for whom."),
  mcq("s23_11", 2, "A hospital board reallocates $800,000 of its $1.2m new buildings budget to cancer care. What is the opportunity cost of this decision?", ["A cost of $400,000", "A cost of $800,000", "The cost of healthcare for cancer patients", "The loss of some new buildings"], 3, "The opportunity cost is the next best use that is given up: some of the new buildings."),
  mcq("s24_11", 4, "Why does the concept of scarcity apply to the use of fossil fuels?", ["Demand fluctuates according to price changes", "Supply is insufficient to meet demand", "Their use is restricted because of pollution", "They are being replaced by renewable energy"], 1, "Scarcity means supply cannot meet all wants, which is the case with a limited resource."),
  mcq("s24_13", 4, "What is essential to eliminate scarcity?", ["The existence of sufficient resources to meet all needs and wants", "Producers consistently produce more than demand", "The government has a budget surplus", "There is equilibrium in all markets"], 0, "Only resources sufficient for all wants would remove scarcity, which in practice never happens."),
  mcq("s25_12", 2, "A textbook diagram should show the terms opportunity cost, scarcity and choice in the order that identifies the fundamental economic problem. What is the correct order?", ["Choice, opportunity cost, scarcity", "Choice, scarcity, opportunity cost", "Scarcity, choice, opportunity cost", "Scarcity, opportunity cost, choice"], 2, "Scarcity forces choice, and each choice has an opportunity cost."),
  mcq("s25_13", 3, "A firm produces 100 units of good Y and 200 of good X with fixed resources. To raise Y to 120 units, it can produce only 170 units of X. What is the opportunity cost of the extra 20 units of Y?", ["20 units of X", "30 units of X", "120 units of X", "170 units of X"], 1, "X falls from 200 to 170, so 30 units of X are given up."),
  mcq("w22_11", 4, "A doctor with long hours and a stressful job can become a teacher. What is the opportunity cost of continuing as a doctor?", ["The risk of mistakes caused by tiredness", "The possible costs of illness from stress", "The potential salary as a teacher", "The retraining costs of becoming a teacher"], 2, "The next best alternative is working as a teacher, so the opportunity cost is the salary (and benefits) of that job.")
]

exam = exam_page("scarcity, choice and opportunity cost",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Scarcity, choice and opportunity cost are tested as 8 mark PPC explanations, as short data response parts of 2 to 4 marks, and in Paper 1 every series. Reworded past questions are below, with twelve Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "May/June 2020 (21) Q2(a); Feb/March 2025 (22) Q2(a); Oct/Nov 2022 (22) Q3(a)"), ("Data response, 2 marks", "2", "Oct/Nov 2022 (23) Q1(a); May/June 2021 (23) Q1(b)"), ("Multiple choice (Paper 1)", "12 shown below", "2020 to 2025")],
  [
  eq(P("s20_21", "2(a)"), "8 marks", "Explain, with the aid of a production possibility curve diagram, why scarcity makes choice inevitable for firms and how each choice has an opportunity cost.",
     ["Diagram: both axes labelled with named goods (for example consumer goods and capital goods) and the PPC drawn as a curve or straight line showing a trade-off (2 marks).",
      "Use the curve to explain scarcity (up to 2 marks), choice (up to 2) and opportunity cost (up to 2)."],
     "PPC with labelled axes. Scarcity: only points on or inside are possible. Choice: pick a point. Opportunity cost: movement along the curve.",
     [[("k", "A production possibility curve shows the maximum combinations of two goods a firm can produce with its limited resources. Points on the curve are the most the firm can produce, and points outside are unattainable, which shows scarcity."), ("n", "Because resources are scarce, the firm must choose a point, for example more of good A means fewer of good B. Moving along the curve from one point to another is a choice, and the units of B that must be given up to get more A are the opportunity cost.")]]),
  eq(P("m25_22", "2(a)"), "8 marks", "With the help of a PPC diagram, explain the terms scarcity and choice and consider the extent to which every choice has an equal opportunity cost.",
     ["Accurate diagram: concave or straight line meeting both axes with labelled goods (1); explanation of scarcity and opportunity cost (1) and how scarce resources and infinite wants result in choices (1).",
      "Analysis: scarcity is a point on the PPC; the opportunity cost is shown by a movement along it; for a straight line the cost is equal, for a concave PPC it increases the more resources are moved (3 marks).",
      "Evaluation (up to 2): whether opportunity cost is equal depends on the shape of the PPC, or on whether there are unused resources at the time of the choice; reserve one mark for a justified conclusion."],
     "PPC. Define scarcity and choice. Straight line: constant cost. Concave: rising cost. Judge: depends on shape and on unused resources.",
     [[("k", "Scarcity is the problem that wants are unlimited while resources are limited. On a PPC with consumer goods and capital goods on the axes, the curve shows the most that can be produced, so scarcity forces a choice of one point."), ("n", "Moving along the curve towards more capital goods means fewer consumer goods, and this loss is the opportunity cost. If the PPC is a straight line the opportunity cost is equal for each unit, but on a concave curve the cost rises as more resources are moved because they are less suited to the new use.")], [("e", "So not every choice has an equal opportunity cost: it depends on the shape of the PPC. Also if the economy is inside the curve with unused resources, the opportunity cost of using them could be very small or zero.")]]),
  eq(P("w22_22", "3(a)"), "8 marks", "Explain how a production possibility curve can be used to demonstrate scarcity, choice and opportunity cost.",
     ["Knowledge of a PPC (up to 2): a curve showing the maximum output with current resources and technology; correct labels for two goods and the curve touching both axes.",
      "Application: scarcity understood and shown as the frontier, with a position outside the curve unattainable (2 marks); choice as a movement along the curve (2); opportunity cost as the next best alternative given up as one product is sacrificed for the other (2).",
      "A diagram is likely but is not essential if the idea is clear; each of the three ideas should be clearly separated."],
     "Three short paragraphs: scarcity, choice, opportunity cost, each tied to the diagram.",
     [[("k", "A production possibility curve is a line showing the maximum combinations of two goods an economy can produce given its resources and technology. With the axes labelled as agricultural goods and manufactured goods, the curve touches both axes."), ("n", "It shows scarcity because the frontier is a limit: points beyond it are not attainable with the existing resources. It shows choice because the economy has to pick one point on the curve, and moving from one point to another is a choice about what to produce. It shows opportunity cost because producing more manufactured goods means moving along the curve and giving up some agricultural goods, which is the next best alternative forgone.")]]),
  eq(P("w22_23", "1(a)"), "2 marks", "Explain what might be the opportunity cost if the government of a country agreed to pay subsidies to its farmers comparable to those paid to farmers in a neighbouring country.",
     ["Opportunity cost is the cost in terms of the best alternative that is forgone (1).", "The decision means other areas of government funding, with a specific example such as health, education or infrastructure, would have less money (1)."],
     "Define opportunity cost. Name what the subsidy money could have bought instead.",
     [[("k", "Opportunity cost is the value of the next best alternative given up."), ("n", "The money spent on subsidies could have funded health care or education, so those services would have less funding.")]]),
  eq(P("s21_23", "1(b)"), "2 marks", "Explain how opportunity cost can be applied to the government's decision to subsidise public transport.",
     ["A simple understanding of opportunity cost (1).", "Applied to a valid example in context (1), for example money used for transport subsidies could have been used for new roads, education or health."],
     "Say what opportunity cost is, then name a specific alternative use of the subsidy.",
     [[("k", "Opportunity cost is what is given up when a choice is made."), ("n", "The money used to subsidise public transport could have been spent on education or health services, so the government loses those benefits.")]])
  ],
  )

tips = tips_html(
  [("Define scarcity properly.", "Unlimited wants and limited resources. Not 'not enough'."),
   ("One alternative only.", "Opportunity cost is the next best alternative, not a list of everything given up."),
   ("Use a PPC.", "Label both axes with named goods and make the curve touch both axes. Show scarcity, choice and opportunity cost on it."),
   ("Give three levels of choice.", "Individuals, firms and governments, each with an example."),
   ("Say what is given up.", "In context, name the specific alternative: schools, buildings, wages, time."),
   ("Do not confuse scarcity and shortage.", "A shortage can be removed by a price change. Scarcity cannot."),
   ("Learn the three questions.", "What, how and for whom.")],
  [("Scarcity", "Scarcity arises because wants are unlimited but resources are limited."),
   ("Choice", "Because of scarcity, individuals, firms and governments must choose between alternatives."),
   ("Opportunity cost", "The opportunity cost of the choice is the next best alternative that is given up."),
   ("Context", "Spending on a subsidy has an opportunity cost, which could be less spending on health or education."),
   ("PPC", "A movement along the PPC shows an opportunity cost, because more of one good means less of the other.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- scarcity -> choice -> opportunity cost ---------- */
function chainDraw(s) {
  const box = (x, y, w, h, t, sub, c, k) => (k > 0 ? SV.rect(x, y, w, h, c, op(0.5 * k)) + SV.text(x + w / 2, y + 30, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + sub.split("|").map((l, i) => SV.text(x + w / 2, y + 56 + i * 17, l, "sm", { "text-anchor": "middle", ...op(k) })).join("") : "");
  const ar = (x1, x2, k) => (k > 0 ? SV.line(x1, 100, x2, 100, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, 100, "r", "dot1") : "");
  let o = box(30, 50, 200, 100, "Scarcity", "Wants are unlimited,|resources are limited", "f2", s.a) + ar(232, 272, s.b) + box(274, 50, 200, 100, "Choice", "Individuals, firms and|governments must pick", "f1", s.b) + ar(476, 516, s.c) + box(518, 50, 210, 100, "Opportunity cost", "The next best alternative|that is given up", "f3", s.c);
  if (s.d > 0) o += tag(380, 200, "Every choice has a cost, even when the price is zero.", "t4", s.d, "middle") + SV.line(60, 176, 700, 176, "c4 dash", op(s.d));
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 230, label: "Scarcity leads to choice and choice has an opportunity cost", base: { a: 0, b: 0, c: 0, d: 0 }, draw: chainDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Scarcity.</b> People want more than can be produced. Resources (land, labour, capital, enterprise) are limited, so not every want can be satisfied.", s: { a: 1 } },
  { cap: "<b>Choice.</b> Because of scarcity, individuals must choose how to spend income and time, firms how to use resources, and governments how to spend the budget.", s: { a: 1, b: 1 } },
  { cap: "<b>Opportunity cost.</b> Choosing one thing means giving up others. The opportunity cost is the value of the next best alternative that is given up.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The result.</b> Every choice has a cost, even if the price is zero, because the resources used could have been used another way.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 230" role="img" aria-label="Scarcity leads to choice and choice has an opportunity cost">${chainDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;

/* ---------- the next best alternative ---------- */
const HOL = [["Barcelona", 9], ["Paris", 8], ["London", 6], ["Venice", 6]];
function holDraw(s) {
  let o = SV.line(60, 250, 730, 250) + SV.line(60, 250, 60, 30) + SV.text(66, 22, "Family's preference score (10 = best)", "sm");
  HOL.forEach(([n, v], i) => { const k = Math.max(0, Math.min(1, s.a - i * 0.0)), x = 110 + i * 150, h = v * 20; o += SV.rect(x, 250 - h, 90, h, i === 0 && s.b > 0 ? "f3" : i === 1 && s.c > 0 ? "f2" : "f1", op(0.7)) + SV.text(x + 45, 270, n, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, 250 - h - 8, v, "lbl bd", { "text-anchor": "middle" }); });
  if (s.b > 0) o += tag(155, 250 - 9 * 20 - 28, "chosen", "t3", s.b, "middle");
  if (s.c > 0) o += tag(305, 250 - 8 * 20 - 28, "opportunity cost", "t2", s.c, "middle");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 285, label: "Four holiday options ranked by preference with the chosen option and its opportunity cost", base: { a: 1, b: 0, c: 0 }, draw: holDraw, tween: 700, dwell: 5600, steps: [
  { cap: "<b>Four options.</b> The family ranks them by preference. Each costs the same, so only one can be chosen.", s: { a: 1 } },
  { cap: "<b>The choice.</b> The family goes to Barcelona, its first preference.", s: { a: 1, b: 1 } },
  { cap: "<b>The opportunity cost</b> is the next best alternative given up: <b>Paris</b>, the second preference. The family gives up all three other holidays, but the opportunity cost is the value of only the best of them.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!$("#hs")) return;
  const h = +$("#hs").value, sch = 100 - h;
  $("#r1").textContent = "$" + h + "m"; $("#r2").textContent = "$" + sch + "m"; $("#r3").textContent = "$10m of the other";
  $("#rv").textContent = `With $${h}m on hospitals, only $${sch}m is left for schools. Each extra $10m for hospitals means $10m less for schools, so the opportunity cost of more hospital spending is the schools forgone. The total never rises above $100m: that is scarcity.`;
  let o = SV.line(40, 120, 400, 120) + SV.text(40, 40, "Budget: $100m", "lbl bd");
  o += SV.rect(40, 130, h * 3.6, 60, "f1", op(0.7)) + SV.rect(40 + h * 3.6, 130, sch * 3.6, 60, "f3", op(0.7)) + SV.text(40 + h * 1.8, 166, "Hospitals $" + h + "m", "lbl bd", { "text-anchor": "middle" }) + (sch > 14 ? SV.text(40 + h * 3.6 + sch * 1.8, 166, "Schools $" + sch + "m", "lbl bd", { "text-anchor": "middle" }) : "");
  o += SV.line(40, 200, 400, 200, "ax") + tag(220, 226, "Every $10m moved to one is $10m taken from the other", "t4", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "hs", label: "Spending on hospitals, $m ", min: 0, max: 100, step: 10, value: 60, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
const HN = ["Barcelona", "London", "Paris", "Venice"];
function labH() {
  if (!$("#h0") || !$("#h1") || !$("#h2") || !$("#h3")) return;
  const v = [0, 1, 2, 3].map((i) => +$("#h" + i).value), mx = Math.max(...v), best = v.map((x, i) => (x === mx ? i : -1)).filter((i) => i >= 0), rest = v.map((x, i) => (best.includes(i) ? -1 : x));
  const mx2 = Math.max(...rest), second = mx2 < 0 ? [] : rest.map((x, i) => (x === mx2 ? i : -1)).filter((i) => i >= 0);
  $("#t1").textContent = best.length > 1 ? "Tie: " + best.map((i) => HN[i]).join(" / ") : HN[best[0]]; $("#t2").textContent = best.length > 1 ? "Another top option" : second.map((i) => HN[i]).join(" and ") || "none"; $("#t3").textContent = "3 options";
  $("#tv").textContent = best.length > 1 ? "Two or more destinations tie for first place, so the family must still pick one; the opportunity cost is then the tied option given up." : `The family chooses ${HN[best[0]]} (score ${mx}). The opportunity cost is the next best alternative, ${second.map((i) => HN[i]).join(" and ")} (score ${mx2}), not the total of everything else given up.`;
  const Y = (x) => 250 - x * 20; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30);
  v.forEach((x, i) => { const px = 60 + i * 85, cls = best.includes(i) ? "f3" : second.includes(i) ? "f2" : "f1"; o += SV.rect(px, Y(x), 60, 250 - Y(x), cls, op(0.75)) + SV.text(px + 30, 270, HN[i], "sm", { "text-anchor": "middle" }) + tag(px + 30, Y(x) - 6, x, "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
HN.forEach((n, i) => Lib.slider($("#g" + (3 + i)), { id: "h" + i, label: n + " ", min: 1, max: 10, step: 1, value: [9, 6, 8, 6][i], fmt: (v) => v, onInput: labH }));
labH();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Who is making the choice?", ["Individual", "Firm", "Government"],
  [("Deciding whether to spend a weekend studying or working", 0), ("Choosing between buying a new machine and hiring more workers", 1), ("Deciding whether to spend more on hospitals or on defence", 2), ("Choosing which phone to buy with a birthday gift", 0), ("Deciding which of two products to make with limited factory space", 1), ("Choosing between cutting taxes and building new roads", 2), ("Deciding between a job offer and further study", 0), ("Choosing between expanding abroad and raising output at home", 1)],
  "Individuals, firms and governments all face scarcity and make choices.") + MATCH([
  ["Scarcity", "Unlimited wants but limited resources"],
  ["Choice", "Selecting between alternatives because of scarcity"],
  ["Opportunity cost", "The next best alternative given up"],
  ["What to produce", "Which goods and services, and how much of each"],
  ["How to produce", "Which methods and resources to use"],
  ["For whom to produce", "Who receives the output"]]) + ORDER(
  "Put the chain in order.",
  ["Wants are unlimited", "Resources are limited, so scarcity exists", "Individuals, firms and governments must choose", "Choosing one option means giving up others", "The value of the next best alternative is the opportunity cost"],
  "Scarcity leads to choice, and choice has an opportunity cost.") + CALC([
  {"q": "A firm makes 100 units of Y and 200 units of X. To make 120 units of Y it can make only 170 units of X. How many units of X are given up (opportunity cost of the extra Y)?", "a": 30, "unit": "units", "tol": 0.5, "hint": "200 − 170.", "sol": "<b>30 units of X</b>."},
  {"q": "In that example, what is the opportunity cost of one extra unit of Y, in units of X (1 decimal place)?", "a": 1.5, "unit": "units", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "30 ÷ 20 = <b>1.5 units of X</b>."},
  {"q": "A government has $200m and spends $120m on hospitals. How much is left for schools ($m)?", "a": 80, "unit": "$m", "tol": 0.5, "hint": "200 − 120.", "sol": "<b>$80m</b>. The opportunity cost of the hospital spending is the schools that $120m could have funded."},
  {"q": "A worker earns $30 an hour and spends 4 hours at a concert instead of working. How much pay is given up ($)?", "a": 120, "unit": "$", "tol": 0.5, "hint": "30 × 4.", "sol": "<b>$120</b> of forgone pay: part of the opportunity cost."}]) + MCQ([
  ("Scarcity exists because:", ["Wants are unlimited and resources are limited", "Prices are too high", "Governments restrict supply", "Income is unequally shared"], 0, "Scarcity is the gap between limitless wants and limited resources."),
  ("Which is an opportunity cost of a government building a new road?", ["The hospitals that the money could have paid for", "The cost of the road in taxes", "All other uses of the money together", "The profit of the road builder"], 0, "It is the next best use of the funds."),
  ("Scarcity differs from a shortage because scarcity:", ["Cannot be removed by a price change", "Only affects poor countries", "Is temporary", "Applies only to goods that are imported"], 0, "A shortage is a market condition at a price, whereas scarcity is permanent."),
  ("Which is NOT one of the three basic economic questions?", ["Where to produce", "What to produce", "How to produce", "For whom to produce"], 0, "The three questions are what, how and for whom."),
  ("Opportunity cost is best defined as:", ["The value of the next best alternative given up", "The money price of a good", "The cost of producing a good", "The total cost of all alternatives"], 0, "It is the single next best alternative.")
], "qz1") + CARDS([
  ("Fundamental economic problem", "Scarcity: unlimited wants, limited resources."),
  ("Choice", "Needed at every level: individuals, firms, governments."),
  ("Opportunity cost", "The next best alternative given up."),
  ("Scarcity vs shortage", "Scarcity is permanent; a shortage is a market condition."),
  ("What to produce", "Which goods and how much."),
  ("How to produce", "Methods and resources used."),
  ("For whom to produce", "Who gets the output."),
  ("Opportunity cost in units", "Units of one good given up for units of another.")]) + MCQ(mc_exam)

build("as11", "as-scarcity-choice-opportunity-cost", "Scarcity, Choice and Opportunity Cost", EY,
  "1.1.1 to 1.1.4: the fundamental economic problem of scarcity, why choice is needed at every level, opportunity cost and the three basic questions of resource allocation. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
