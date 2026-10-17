"""AS syllabus 1.5.1-1.5.2 PPC: meaning and shape, constant and increasing opportunity cost. Run: python3 tools/artifact-kit/mk_as16.py"""
from asx import *
EY = EYAS("1.5.1 to 1.5.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">production possibility curve (PPC)</b> shows the <b>maximum combinations of two goods</b> that an economy (or firm) can produce with its <b>given resources and technology</b>, when all resources are fully and efficiently used. Moving along the curve means producing more of one good and <b>less of the other</b>, and the <b>slope shows the opportunity cost</b>. A <b>straight-line PPC</b> has <b>constant opportunity cost</b> because resources are equally suited to both goods, whereas the usual <b>concave (bowed-out) PPC</b> has <b>increasing opportunity cost</b> because resources are <b>specialised</b> and the ones moved later are less suited to the new use.</p></div>

  <h2>1 · What a PPC shows (1.5.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>Draw it with <b>two named goods on the axes</b> (for example consumer goods and capital goods, or wheat and cotton), and the curve should <b>touch both axes</b>. Axes labelled only "X and Y" lose marks in some mark schemes.</li>
    <li>Every point <b>on</b> the curve is the maximum output of the two goods together, when resources are fully and efficiently used. A point <b>outside</b> is unattainable with current resources, and a point <b>inside</b> means resources are unused or used inefficiently (see syllabus 1.5.4).</li>
    <li>It illustrates <b>scarcity</b> (the frontier is a limit), <b>choice</b> (picking a point) and <b>opportunity cost</b> (what is given up when moving along the curve).</li>
    <li>The opportunity cost of moving from one point to another is the <b>units of one good given up per unit of the other gained</b> (the slope of the curve).</li>
  </ul>

  <h2>2 · The shape of the PPC (1.5.2)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Straight-line PPC</th><th>Concave (bowed-out) PPC</th></tr>
    <tr><td><b>Opportunity cost</b></td><td><b>Constant</b>: each extra unit of X always costs the same number of units of Y</td><td><b>Increasing</b>: each extra unit of X costs more and more of Y</td></tr>
    <tr><td><b>Why</b></td><td>Resources are <b>equally suited</b> to making either good and can be switched without loss</td><td>Resources are <b>specialised</b>: the first ones moved are best suited to the new good, later ones are less suited, so output of the other good falls faster</td></tr>
    <tr><td><b>Realism</b></td><td>Rare, a simplification</td><td>The usual case, because land, labour and capital differ in what they are good at</td></tr>
    <tr><td><b>Slope</b></td><td>The same everywhere</td><td>Gets steeper as more X is produced</td></tr>
  </table></div>
  <ul>
    <li><b>Increasing opportunity cost</b> arises because resources are not perfectly mobile or equally productive in all uses. Farmland that is best for wheat is poor for cotton: switching the best wheat land first loses little wheat, but switching the last plots loses a lot.</li>
    <li>A <b>convex</b> PPC (bowed in) would mean decreasing opportunity cost, which would be unusual and is not expected at AS Level.</li>
    <li>In a <b>mixed</b> economy the government might choose a different mix of goods (such as more consumer goods and fewer capital goods) by moving along the same curve.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For "why is a PPC usually concave?", say that <b>resources cannot easily be switched between products</b>, so the cost in terms of the other good <b>rises</b> as more is produced.</div>
'''

watch = '''
  <h2>1 · Reading opportunity cost off a PPC</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stO"></div>
  <h2>2 · Constant and increasing opportunity cost</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · The shape of the PPC</h2>
  <p>Choose how curved the PPC is (1 is a straight line) and the amount of good X. See the amount of Y and the cost of the next 10 units of X.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Y at this point</small><strong id="r1"></strong></div><div><small>Y given up for next 10 X</small><strong id="r2"></strong></div><div><small>Opportunity cost per X</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="A production possibility curve with a chosen point and the loss of good Y when 10 more units of X are made"></svg></div></div></div>

  <h2>Lab 2 · Why the cost rises: specialised land</h2>
  <p>A farm has 8 plots. Each plot gives different yields of wheat and cotton. The farmer switches plots from wheat to cotton, best-suited first. Watch the opportunity cost per unit of cotton rise.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div>
    <div class="readout"><div><small>Wheat</small><strong id="t1"></strong></div><div><small>Cotton</small><strong id="t2"></strong></div><div><small>Wheat lost per cotton (last plot)</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="A production possibility curve built from eight plots of land with increasing opportunity cost"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Constant or increasing opportunity cost?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the explanation of increasing opportunity cost in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A farm choosing crops", "A farmer has land that suits both wheat and potatoes. At first she plants potatoes on the plots that are best for them, and she loses little wheat. As she puts potatoes on plots better suited to wheat, each extra tonne of potatoes costs more wheat. This is increasing opportunity cost.", "why a PPC is usually concave: resources are better suited to some uses than others.") +
rw("A country choosing between consumer and capital goods", "A country can make fewer consumer goods now and more factory machinery, or the reverse. If it moves resources into machinery, it gives up shops and clothes. The PPC shows the trade-off, and the choice affects future growth.", "choice along the PPC and the consumer goods and capital goods axes.") +
rw("Straight-line trade-offs", "A firm that can switch identical workers and machines between two similar products, such as two kinds of box, loses a fixed number of boxes of one type for each extra box of the other. This is close to a straight-line PPC with constant opportunity cost.", "constant opportunity cost when resources are equally suited to both goods.") +
rw("A desert island economy", "People on an island can catch fish or gather coconuts. If all the islanders are equally good at both, the trade-off is constant, so the PPC is a straight line. If some are good climbers and others good fishers, the PPC is bowed out.", "how the nature of the resources determines the shape of the PPC.")
)

mc_exam = [
  mcq("m20_12", 1, "The PPC of a desert island economy, where the inhabitants produce coconuts and fish, is a straight line. What explains the shape of the PPC?", ["Coconuts and fish are perfect complements", "Coconuts and fish are perfect substitutes", "The inhabitants consume more fish than coconuts", "The opportunity cost of increasing fish production is constant"], 3, "A straight line means each extra unit of fish costs the same number of coconuts: constant opportunity cost."),
  mcq("m23_12", 4, "The PPC for wheat and corn has a straight section from point M to point N. What can be deduced?", ["As the price of corn falls, more of it is demanded", "Resources used in producing corn are more efficient than in producing wheat", "The opportunity cost of producing corn falls when moving from M to N", "The opportunity cost of producing corn is constant when moving from M to N"], 3, "A straight line segment shows a constant trade-off between the two goods."),
  mcq("w20_12", 1, "A PPC for goods X and Y is bowed outwards (concave to the origin). What can be deduced from the shape of this curve?", ["Decreasing marginal returns to consumption", "Decreasing opportunity costs of consumption", "Increasing opportunity costs of production", "Increasing returns to scale"], 2, "A bowed-out PPC shows rising opportunity costs of production. It says nothing about consumption."),
  mcq("w22_13", 4, "A PPC for goods X and Y is bowed outwards. What happens to the opportunity cost of producing more of good Y and of producing more of good X?", ["Decreases; decreases", "Decreases; increases", "Increases; decreases", "Increases; increases"], 3, "On a concave PPC the opportunity cost of expanding either good rises."),
  mcq("w23_12", 1, "Country T's PPC is bowed outwards. What happens to country T's opportunity costs of producing X as it increases production of X?", ["Constant between points 1 and 2 and between points 3 and 4", "Decrease between points 1 and 2 and increase between points 3 and 4", "Decrease between both pairs of points", "Increase between points 1 and 2 and between points 3 and 4"], 3, "On a concave curve the opportunity cost of X keeps rising throughout."),
  mcq("w24_13", 1, "A country's PPC is a straight line from 100 units of food to 50 units of drink. What can be concluded?", ["Food and drink are normal goods", "The country is self-sufficient in food and drink", "The opportunity cost of food falls as more drink is produced", "There is a constant opportunity cost between food and drink"], 3, "A straight-line PPC has the same slope throughout: constant opportunity cost."),
  mcq("w24_12", 1, "A PPC for a country shows manufactured goods against agricultural goods. What can be determined from the diagram?", ["The consumers' preferred combination of output", "The level of economic growth", "The opportunity cost of manufactured goods in terms of agricultural products", "The preference for present consumption rather than future consumption"], 2, "The slope of the PPC gives the opportunity cost. The curve alone does not show preferences or growth."),
  mcq("w23_13", 3, "Luke can produce 18 rings and 0 bracelets, 12 and 6, 6 and 12, or 0 and 18. Zoe can produce 20 rings and 0 bracelets, 16 and 8, 12 and 16, or 8 and 24. Which statement is not correct?", ["Luke has a larger opportunity cost than Zoe for making bracelets", "The opportunity cost of producing rings is constant for both Luke and Zoe", "Zoe should specialise in making bracelets", "Zoe's opportunity cost for each bracelet is 2 rings"], 3, "Zoe gives up 4 rings for 8 bracelets, so each bracelet costs 0.5 ring, not 2. Luke gives up 1 ring per bracelet, so Zoe has the lower cost for bracelets.")
]

exam = exam_page("the production possibility curve: meaning, shape and opportunity cost",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The PPC is the most reliable 8 mark question in Paper 2: nearly every series has one on opportunity cost, shape, shifts or position, and it also appears as a 2 to 4 mark diagram in data response. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2021 (22) Q2(a); Oct/Nov 2024 (22) Q3(a)"), ("Data response, 3 marks", "1", "May/June 2022 (23) Q1(d)"), ("Data response, 4 marks", "1", "May/June 2025 (23) Q1(c)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2024")],
  [
  eq(P("w21_22", "2(a)"), "8 marks", "Use a diagram to explain how a production possibility curve can be used to show opportunity cost and why such a curve is usually drawn with increasing opportunity costs.",
     ["Knowledge (up to 2): a PPC diagram with correctly labelled axes.",
      "Application (up to 3): what opportunity cost is, in terms of the products on the diagram (1); a movement along the curve and its effect on the output of the two goods (1); how this shows opportunity cost (1).",
      "Application (up to 3): why increasing opportunity cost is expected, so the curve must be concave (1); increasing opportunity cost clearly shown on the diagram (1); explained, for example because resources cannot easily be switched between products (1).",
      "If the only diagram shows a straight line, the maximum is 5 marks."],
     "Concave PPC with named goods. A movement along it shows the loss of one good. Why the cost rises: resources are not equally suited.",
     [[("k", "A production possibility curve shows the maximum combinations of two goods that can be produced with the available resources. If the axes are labelled consumer goods and capital goods, the curve slopes downwards, touching both axes."), ("n", "A movement along the curve from point A to point B means more capital goods and fewer consumer goods, and the consumer goods given up are the opportunity cost.")], [("n", "The curve is usually drawn concave to show increasing opportunity cost. This is because resources are not equally suited to making both goods, so they cannot easily be switched. The first resources moved to capital goods are best suited to them and little consumer output is lost, but later resources are less suited, so each extra unit of capital goods costs more consumer goods. The curve gets steeper as more capital goods are produced.")]]),
  eq(P("w24_22", "3(a)"), "8 marks", "With the help of a PPC diagram, explain the difference between constant and increasing opportunity costs and consider how choices in deciding which type of goods to produce in the short run may influence future economic growth.",
     ["Knowledge (3): an accurate PPC with named goods on the axes: curved to show increasing opportunity cost and a straight line to show constant (the curves must touch both axes); an explanation of the difference: constant means no change in the rate of trade-off, increasing means the trade-off rises.",
      "Analysis (3): future growth depends on the split between consumer goods and capital goods; choosing consumer goods may bring short-run growth that may not be sustainable; choosing capital goods may have a short-run negative impact but create long-term sustainable growth as output expands.",
      "Evaluation (2): valid evaluation based on the analysis, leading to a conclusion."],
     "Two PPCs or two lines. Straight: constant. Curved: increasing. Consumer or capital goods now: effect on growth later. Judge.",
     [[("k", "A straight-line PPC shows constant opportunity cost: each extra unit of good X always means giving up the same number of units of Y. A concave PPC shows increasing opportunity cost: each extra unit of X costs more and more of Y, because resources are not equally suited to the two goods.")], [("n", "The choice of goods now influences future growth. If the economy chooses more consumer goods, living standards rise in the short run, but with fewer capital goods the productive capacity may grow slowly. If it chooses more capital goods, consumption is lower now, but the stock of capital expands, which shifts the PPC outwards in the future.")], [("e", "So a choice for capital goods is likely to give more sustainable long-run growth, but at a cost in the short run. The best choice may depend on how urgent current consumption is and how well the capital is used.")]]),
  eq(P("s22_23", "1(d)"), "3 marks", "Explain, with the help of a production possibility curve diagram, the opportunity cost to a farmer of converting from dairy to avocado production.",
     ["PPC diagram with the axes correctly labelled (1).", "Diagram used to show the choice between dairy and avocados, with at least two points on the curve (1).", "Application of opportunity cost to the shape of the PPC: constant (straight line) or increasing (concave) (1)."],
     "Draw a PPC with dairy and avocados. Show two points. Say what is given up and whether the cost rises.",
     [[("k", "A PPC with dairy on one axis and avocados on the other shows the combinations the farmer can produce. Moving from a point with lots of dairy to one with more avocados shows the choice."), ("n", "The dairy output given up as avocado production rises is the opportunity cost. On a concave PPC, each extra tonne of avocados costs more dairy output than the last.")]]),
  eq(P("s25_23", "1(c)"), "4 marks", "With the help of a production possibility curve diagram, consider the impact on the opportunity cost to a farmer of starting to grow red onions.",
     ["Correctly labelled axes (one must be red onions) and a PPC that touches both axes, either straight or concave (1).",
      "An initial production combination at which all resources produce the other good with no red onions (1).",
      "A second combination with some red onions and less of the other good (1).",
      "For valid evaluation: for example whether the opportunity cost is constant or increasing."],
     "PPC with red onions. Start at zero onions. Move along the curve. Say what is given up.",
     [[("k", "On a PPC with red onions on one axis and the farmer's other crop on the other, the farmer starts at the point where all resources produce the other crop and no onions are grown."), ("n", "Starting to grow onions means moving along the curve to a point with some onions and less of the other crop, and the crop given up is the opportunity cost. On a concave curve the cost of each extra tonne of onions rises, so it could become expensive to expand much.")]])
  ],
  )

tips = tips_html(
  [("Name the goods on the axes.", "Consumer goods and capital goods, not just X and Y."),
   ("Touch both axes.", "The curve must meet each axis."),
   ("Slope equals opportunity cost.", "Say how many units of one good are given up for the other."),
   ("Straight means constant.", "Resources equally suited to both goods."),
   ("Concave means increasing.", "Resources are specialised and not easily switched."),
   ("Use a movement along the curve.", "A movement along shows choice and opportunity cost; a shift is covered in the next topic."),
   ("Link to scarcity.", "A point outside the curve is unattainable.")],
  [("PPC", "A production possibility curve shows the maximum combinations of two goods that an economy can produce with its resources."),
   ("Opportunity cost", "A movement along the PPC shows the opportunity cost, which is the amount of one good given up to produce more of the other."),
   ("Increasing", "The PPC is concave because resources are not equally suited to producing both goods, so the opportunity cost increases."),
   ("Constant", "A straight line PPC shows a constant opportunity cost because resources can be switched without a loss in efficiency."),
   ("Choice", "Choosing more capital goods may reduce consumption now but could raise future output.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- helpers ---------- */
const yk = (x, k) => 100 * Math.pow(Math.max(0, 1 - Math.pow(x / 100, k)), 1 / k);
const PXX = (x) => 90 + x * 5.2, PYY = (y) => 300 - y * 2.6;
function axesP(xl, yl) { return SV.line(90, 300, 640, 300) + SV.line(90, 300, 90, 30) + SV.text(640, 326, xl, "sm", { "text-anchor": "end" }) + SV.text(96, 24, yl, "sm"); }
const curve = (k, c, d) => { const p = []; for (let x = 0; x <= 100; x += 2) p.push([PXX(x), PYY(yk(x, k))]); return SV.path(Lib.ptsPath(p), c, d); };

/* ---------- opportunity cost on a PPC ---------- */
function ocDraw(s) {
  let o = axesP("Capital goods", "Consumer goods") + curve(2, "c1");
  const pts = [[20, "A"], [60, "B"], [90, "C"]];
  pts.forEach(([x, l], i) => { if (s.p > i) o += SV.circle(PXX(x), PYY(yk(x, 2)), 7, "dot4") + tag(PXX(x) + 10, PYY(yk(x, 2)) - 10, l, "t4"); });
  if (s.m > 0) { const x1 = 20, x2 = 60, y1 = yk(x1, 2), y2 = yk(x2, 2); o += SV.line(PXX(x1), PYY(y1), PXX(x2), PYY(y1), "c3", op(s.m)) + SV.line(PXX(x2), PYY(y1), PXX(x2), PYY(y2), "c2", { "stroke-width": 4, ...op(s.m) }) + tag(PXX(40), PYY(y1) - 8, "+40 capital goods", "t3", s.m, "middle") + tag(PXX(x2) - 8, PYY((y1 + y2) / 2) + 4, "−" + Lib.fmtN(y1 - y2, 0) + " consumer goods", "t2", s.m, "end"); }
  if (s.n > 0) { const x1 = 60, x2 = 90, y1 = yk(x1, 2), y2 = yk(x2, 2); o += SV.line(PXX(x1), PYY(y1), PXX(x2), PYY(y1), "c3", op(s.n)) + SV.line(PXX(x2), PYY(y1), PXX(x2), PYY(y2), "c2", { "stroke-width": 4, ...op(s.n) }) + tag(PXX(75), PYY(y1) - 8, "+30 capital goods", "t3", s.n, "middle") + tag(PXX(x2) + 8, PYY((y1 + y2) / 2) + 4, "−" + Lib.fmtN(y1 - y2, 0) + " consumer goods", "t2", s.n); }
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 345, label: "A PPC with three points and the consumer goods given up as capital goods rise", base: { p: 0, m: 0, n: 0 }, draw: ocDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The curve.</b> It shows the most consumer goods and capital goods that the economy can produce together with its resources.", s: { p: 0, m: 0, n: 0 } },
  { cap: "<b>Point A</b> has few capital goods and many consumer goods: about 98 consumer goods and 20 capital goods.", s: { p: 1, m: 0, n: 0 } },
  { cap: "<b>Moving from A to B</b> adds 40 capital goods but costs about 18 consumer goods: the opportunity cost is about 0.45 consumer goods per capital good.", s: { p: 2, m: 1, n: 0 } },
  { cap: "<b>Moving from B to C</b> adds only 30 capital goods but costs about 36 consumer goods: about 1.2 per capital good. The opportunity cost has risen.", s: { p: 3, m: 1, n: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="A concave production possibility curve with three points">${ocDraw({ p: 3, m: 1, n: 1 })}</svg>`;

/* ---------- straight vs concave ---------- */
function scDraw(s) {
  let o = axesP("Good X", "Good Y");
  if (s.l > 0) o += curve(1, "c3", op(s.l)) + tag(PXX(58), PYY(40) - 8, "Straight line: constant opportunity cost", "t3", s.l, "start");
  if (s.c > 0) o += curve(2, "c1", op(s.c)) + tag(PXX(60), PYY(yk(60, 2)) - 12, "Concave: increasing opportunity cost", "t1", s.c, "start");
  if (s.b > 0) { [[0, 25], [25, 50], [50, 75], [75, 100]].forEach(([a, b], i) => { const dy = yk(a, 2) - yk(b, 2), dl = 25, x = PXX(b); o += SV.rect(x - 8, PYY(yk(a, 2)), 16, dy * 2.6, "f2", op(0.6 * s.b)) + tag(x, PYY(yk(a, 2)) + dy * 2.6 + 16, Lib.fmtN(dy, 0), "t2", s.b, "middle"); }); o += tag(PXX(60), PYY(95), "Y lost for each extra 25 units of X", "t2", s.b, "start"); }
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 345, label: "A straight-line PPC with constant opportunity cost and a concave PPC with increasing opportunity cost", base: { l: 0, c: 0, b: 0 }, draw: scDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Straight line.</b> If resources are equally suited to both goods, each extra 25 units of X costs 25 units of Y: constant opportunity cost.", s: { l: 1, c: 0, b: 0 } },
  { cap: "<b>Concave curve.</b> If resources are specialised, the curve bows out. The opportunity cost is not the same along it.", s: { l: 1, c: 1, b: 0 } },
  { cap: "<b>Increasing cost.</b> The first 25 units of X cost only 3 units of Y, but the last 25 cost 66. Each unit of X costs more Y as resources less suited to X are moved.", s: { l: 0, c: 1, b: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Straight-line and concave PPCs">${scDraw({ l: 1, c: 1, b: 0 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#kk") || !$("#xx")) return;
  const k = +$("#kk").value / 10, x = +$("#xx").value, y = yk(x, k), y2 = yk(Math.min(100, x + 10), k), oc = y - y2;
  $("#r1").textContent = Lib.fmtN(y, 1); $("#r2").textContent = Lib.fmtN(oc, 1); $("#r3").textContent = x >= 100 ? "–" : Lib.fmtN(oc / 10, 2) + " Y";
  $("#rv").textContent = k <= 1.05 ? `With a straight-line PPC the next 10 units of X always cost ${Lib.fmtN(oc, 1)} units of Y: the opportunity cost is constant at ${Lib.fmtN(oc / 10, 2)} units of Y per unit of X.` : `At X = ${x}, Y is ${Lib.fmtN(y, 1)}. Producing 10 more units of X means giving up ${Lib.fmtN(oc, 1)} units of Y, or ${Lib.fmtN(oc / 10, 2)} per unit of X. Move the point to the right and the cost rises: increasing opportunity cost. The more curved the PPC, the faster it rises.`;
  const X = (v) => 40 + v * 3.4, Y = (v) => 270 - v * 2.4; let o = SV.line(40, 270, 390, 270) + SV.line(40, 270, 40, 30) + SV.text(390, 292, "Good X", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Good Y", "sm");
  const p = []; for (let v = 0; v <= 100; v += 2) p.push([X(v), Y(yk(v, k))]); o += SV.path(Lib.ptsPath(p), "c1") + SV.circle(X(x), Y(y), 7, "dot4");
  if (x < 100) o += SV.line(X(x), Y(y), X(x + 10), Y(y), "c3", { "stroke-width": 3 }) + SV.line(X(x + 10), Y(y), X(x + 10), Y(y2), "c2", { "stroke-width": 4 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "kk", label: "Curvature (1.0 = straight line) ", min: 10, max: 40, step: 1, value: 20, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
Lib.slider($("#g2"), { id: "xx", label: "Units of good X ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const PL = [[2, 12], [3, 11], [4, 10], [6, 8], [8, 6], [10, 4], [11, 3], [12, 2]];
function labL() {
  if (!$("#pn")) return;
  const n = +$("#pn").value; let w = 56, c = 0; for (let i = 0; i < n; i++) { w -= PL[i][0]; c += PL[i][1]; }
  const last = n > 0 ? PL[n - 1][0] / PL[n - 1][1] : 0;
  $("#t1").textContent = w; $("#t2").textContent = c; $("#t3").textContent = n === 0 ? "–" : Lib.fmtN(last, 2);
  $("#tv").textContent = n === 0 ? "All 8 plots grow wheat (56 units). Cotton output is zero." : `${n} plot${n > 1 ? "s are" : " is"} now growing cotton. Wheat is ${w} and cotton is ${c}. The last plot switched gave up ${PL[n - 1][0]} wheat to gain ${PL[n - 1][1]} cotton, an opportunity cost of ${Lib.fmtN(last, 2)} wheat per unit of cotton. Plots are switched in order of how well suited they are to cotton, so the cost of each extra unit of cotton keeps rising: that is increasing opportunity cost.`;
  const X = (v) => 40 + v * 5.6, Y = (v) => 270 - v * 4.4; let o = SV.line(40, 270, 390, 270) + SV.line(40, 270, 40, 30) + SV.text(390, 292, "Cotton", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Wheat", "sm");
  const pts = [[X(0), Y(56)]]; let ww = 56, cc = 0; PL.forEach(([a, b]) => { ww -= a; cc += b; pts.push([X(cc), Y(ww)]); });
  o += SV.path(Lib.ptsPath(pts), "c1");
  let w2 = 56, c2 = 0; for (let i = 0; i < n; i++) { w2 -= PL[i][0]; c2 += PL[i][1]; } o += SV.circle(X(c2), Y(w2), 7, "dot4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "pn", label: "Plots switched to cotton ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: labL });
labL();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the situation give constant or increasing opportunity cost?", ["Constant", "Increasing"],
  [("Identical workers who can make either of two similar products equally well", 0), ("Land that is much better for wheat than for cotton", 1), ("A straight-line PPC", 0), ("A PPC that gets steeper as more of one good is produced", 1), ("Resources that are specialised and cannot easily be switched", 1), ("Machines that make either product with no change in efficiency", 0), ("Moving the last skilled farmers from wheat to cotton", 1), ("Each extra unit of X always costs 2 units of Y", 0)],
  "Constant: resources equally suited to both goods. Increasing: resources specialised.") + MATCH([
  ["Production possibility curve", "Maximum combinations of two goods with given resources and technology"],
  ["Opportunity cost on a PPC", "Units of one good given up to gain units of the other"],
  ["Straight-line PPC", "Constant opportunity cost"],
  ["Concave PPC", "Increasing opportunity cost"],
  ["Specialised resources", "Better suited to some uses than others"],
  ["Point on the PPC", "Maximum output using resources fully and efficiently"]]) + ORDER(
  "Put the explanation of increasing opportunity cost in order.",
  ["Resources are specialised, not equally suited to both goods", "The best-suited resources are moved to the new good first", "Later resources moved are less suited to the new good", "Each extra unit of the new good costs more of the other good", "The PPC becomes steeper and bowed out"],
  "Specialised resources make the cost of switching rise.") + CALC([
  {"q": "A country moves along its PPC. Consumer goods fall from 100 to 85 as capital goods rise from 20 to 50. Calculate the opportunity cost of one capital good in consumer goods (1 decimal place).", "a": 0.5, "unit": "units", "tol": 0.05, "hint": "15 ÷ 30.", "sol": "15 ÷ 30 = <b>0.5 consumer goods</b> per capital good."},
  {"q": "Later, consumer goods fall from 85 to 55 as capital goods rise from 50 to 80 (30 more). Calculate the opportunity cost per capital good.", "a": 1, "unit": "units", "tol": 0.05, "hint": "30 ÷ 30.", "sol": "<b>1.0</b>: the cost has doubled, so opportunity cost is increasing."},
  {"q": "A straight-line PPC runs from 100 units of Y to 50 units of X. What is the opportunity cost of one unit of X in units of Y?", "a": 2, "unit": "units", "tol": 0.05, "hint": "100 ÷ 50.", "sol": "<b>2 units of Y</b>, constant everywhere."},
  {"q": "A farmer switches a plot from wheat to cotton: wheat falls from 56 to 54 and cotton rises from 0 to 12. What is the wheat given up per unit of cotton (2 decimal places)?", "a": 0.17, "unit": "units", "tol": 0.01, "hint": "2 ÷ 12.", "sol": "2 ÷ 12 = <b>0.17</b>. The first plot costs little."}]) + MCQ([
  ("A straight-line PPC shows:", ["Constant opportunity cost", "Increasing opportunity cost", "Decreasing opportunity cost", "No opportunity cost"], 0, "The trade-off is the same along the line."),
  ("Why is a PPC usually concave?", ["Resources cannot be switched easily between uses", "Resources are equally suited to both goods", "There is no scarcity", "Technology always changes"], 0, "Specialised resources make the cost of switching rise."),
  ("A point outside a PPC is:", ["Unattainable with current resources", "Efficient", "Inefficient", "On the curve"], 0, "The curve is the limit of what resources allow."),
  ("The axes of a PPC should show:", ["Two named goods", "Price and quantity", "Cost and revenue", "Time and output"], 0, "Name the goods, such as consumer goods and capital goods."),
  ("Moving along a PPC from consumer goods to capital goods:", ["Reduces consumer goods", "Increases both goods", "Shifts the curve", "Removes scarcity"], 0, "More of one good means less of the other.")
], "qz1") + CARDS([
  ("PPC", "Maximum combinations of two goods."),
  ("Slope", "Shows the opportunity cost."),
  ("Straight line", "Constant opportunity cost."),
  ("Concave curve", "Increasing opportunity cost."),
  ("Why concave", "Resources are specialised."),
  ("On the curve", "Resources fully and efficiently used."),
  ("Outside", "Unattainable."),
  ("Label the axes", "Name the two goods; touch both axes.")]) + MCQ(mc_exam)

build("as16", "as-ppc-shape-opportunity-cost", "The PPC: Shape and Opportunity Cost", EY,
  "1.5.1 to 1.5.2: what a production possibility curve shows, how to read opportunity cost from it, and why it is straight (constant cost) or concave (increasing cost). Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
