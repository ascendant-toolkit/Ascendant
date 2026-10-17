"""AS syllabus 1.5.3-1.5.4 PPC shifts and the significance of a position within it. Run: python3 tools/artifact-kit/mk_as17.py"""
from asx import *
EY = EYAS("1.5.3 to 1.5.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">movement along</b> a PPC is a <b>reallocation of existing resources</b> between two goods and involves an opportunity cost, whereas a <b class="kw">shift</b> of the PPC is caused by a change in the <b>quantity or quality of resources or in technology</b>. An <b>outward shift</b> raises potential output and is <b>potential economic growth</b>, while an <b>inward shift</b> (a fall in resources) lowers it. The <b>position</b> of the economy matters too: a point <b>on</b> the curve means resources are fully and efficiently used, a point <b>inside</b> means resources are unused or inefficiently used (unemployment), and a point <b>outside</b> cannot be reached with current resources.</p></div>

  <h2>1 · Shifts of the PPC (1.5.3)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Causes</th><th>Effect on the PPC</th></tr>
    <tr><td><b>Outward shift (growth in potential output)</b></td><td>More resources or better quality: investment in capital, education and training, immigration, discovery of natural resources, a larger labour force, <b>improvements in technology</b></td><td>Curve moves out on both axes: more of both goods can be produced</td></tr>
    <tr><td><b>Biased (one-sided) shift</b></td><td>Technology or resources affecting only one good, such as a new crop variety for wheat or a flood that ruins barley land</td><td>Curve moves out (or in) on one axis only</td></tr>
    <tr><td><b>Inward shift</b></td><td>Fall in the quantity or quality of resources: war, natural disaster, emigration, resource depletion, a rise in the school leaving age (fewer workers)</td><td>Curve moves in: lower potential output</td></tr>
  </table></div>
  <ul>
    <li><b>Quantity and quality:</b> a fall in the quantity of labour but a rise in its quality has opposing effects; the net effect depends on which is larger.</li>
    <li><b>Consequences of an outward shift:</b> more goods and services can be produced, which can raise living standards, give governments more tax revenue and give more choice. A shift does <b>not involve opportunity cost</b>, because with extra resources more of <b>both</b> goods can be made.</li>
    <li><b>Opportunity cost of achieving a shift:</b> to raise future output a country usually has to produce more <b>capital goods</b> now and fewer consumer goods, which is a movement along the current PPC. Growth is not free.</li>
    <li><b>Consequences of an inward shift:</b> lower potential output, lower living standards and fewer choices.</li>
    <li>A shift of the PPC is <b>potential growth</b>. A movement from inside the curve towards it is <b>actual growth</b> without any change in capacity.</li>
  </ul>

  <h2>2 · The significance of a position within a PPC (1.5.4)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Position</th><th>What it means</th><th>Example</th></tr>
    <tr><td><b>On the curve</b></td><td>Resources are <b>fully and efficiently used</b>; more of one good means less of the other (opportunity cost)</td><td>Full employment of labour and capital</td></tr>
    <tr><td><b>Inside the curve</b></td><td>Resources are <b>unused or used inefficiently</b>; output of both goods is lower than possible. <b>More of one or both goods can be produced at no opportunity cost</b></td><td>A recession with high unemployment and idle factories</td></tr>
    <tr><td><b>Outside the curve</b></td><td><b>Unattainable</b> with current resources and technology; possible only after growth (or by temporary means such as borrowing or trade)</td><td>A target that needs more resources than the economy has</td></tr>
  </table></div>
  <ul>
    <li><b>Why inside is inefficient:</b> with the same resources more of one good could be produced without giving up any of the other. The economy is producing less than its potential: this is a <b>negative output gap</b>.</li>
    <li><b>Moving from inside to the curve</b> (for example by cutting unemployment) is <b>actual growth</b>: output rises with no change in capacity and no opportunity cost.</li>
    <li><b>Is an inside position permanent?</b> Often not: in a recession, a market economy may recover as demand returns, but it can persist if there is structural unemployment, low confidence or slow adjustment.</li>
    <li>Knowing the point where an economy operates tells you the <b>level of output of the two goods</b>, but not its trade performance or its growth rate.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Be sure to separate the two ideas. <b>Shift</b> = more resources or better technology, potential growth, no opportunity cost. <b>Movement</b> = reallocation (along) or using idle resources (from inside towards the curve).</div>
'''

watch = '''
  <h2>1 · Shifts of the PPC</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stS"></div>
  <h2>2 · Inside, on and outside the PPC</h2>
  <div id="stP"></div>
'''

explore = '''
  <h2>Lab 1 · What shifts the PPC?</h2>
  <p>Start with a PPC for goods X and Y with maximum output of 100 each. Add labour and technology (which here helps only good Y), or subtract resources lost in a disaster. See the new PPC.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Max X</small><strong id="r1"></strong></div><div><small>Max Y</small><strong id="r2"></strong></div><div><small>Type of shift</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="An original production possibility curve and a new curve after the chosen change in resources and technology"></svg></div></div></div>

  <h2>Lab 2 · Consume now or grow later?</h2>
  <p>An economy puts a share of its resources into capital goods, which raises future growth, and the rest into consumer goods. A bigger share means lower consumption today, but faster growth. When does it overtake an economy that invests only 10%?</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div>
    <div class="readout"><div><small>Consumption today</small><strong id="t1"></strong></div><div><small>Annual growth of capacity</small><strong id="t2"></strong></div><div><small>Overtakes the 10% economy in</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Lines showing consumption over 40 years for an economy investing 10 percent and an economy investing the chosen share"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Movement along, shift or movement towards the curve?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a recession and recovery in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The 2020 recession and idle resources", "When economies were locked down in 2020, many factories, shops and workers were idle. The economy moved to a point inside its PPC. When restrictions ended, output recovered towards the curve, which was actual growth without any new resources.", "a position inside the PPC and the move back towards the curve.") +
rw("Technology and a shift outwards", "Computers, the internet and automation raised the amount of goods and services that the same labour could produce, shifting the PPC outwards over time. People could consume more of both goods and services without giving anything up, in contrast to a simple reallocation.", "an outward shift caused by better technology, with no opportunity cost.") +
rw("A flood destroys farmland", "A flood that ruins land used for barley lowers the maximum output of barley. If the farmer switches to a new variety of wheat that gives higher yields on the rest of the land, wheat capacity rises. The PPC pivots: barley falls, wheat rises.", "a biased shift: one axis moves out and the other moves in.") +
rw("A higher school leaving age", "Raising the age at which students can leave school lowers the size of the working population in the short run, shifting the PPC inwards. In the long run better-educated workers raise the quality of labour and may shift the PPC outwards.", "quantity versus quality of labour and the time period.")
)

mc_exam = [
  mcq("s24_11", 5, "An economist knows the current point at which an economy operates within its production possibility curve. What can the economist conclude about this economy?", ["Its degree of self-sufficiency", "Its international competitiveness", "Its level of output of the two goods", "Its rate of economic growth"], 2, "A point on the diagram gives the output of the two goods. It says nothing about trade or growth."),
  mcq("w20_13", 1, "An economy is operating at a point inside its production possibility curve. Why is this described as inefficient?", ["Individuals are enjoying too much leisure", "More of one good can be produced without decreasing production of another", "The combination of labour and capital is wrong", "There are shortages of some goods and an excess supply of others"], 1, "Inside the curve resources are unused or wasted, so output of one good could rise at no cost to the other."),
  mcq("s23_12", 2, "Assuming nothing else changes, which change in an economy's labour market will cause the PPC to shift to the left?", ["An increase in worker immigration", "An increase in the retirement age", "An increase in labour productivity", "An increase in the school leaving age"], 3, "A higher school leaving age keeps young people out of the workforce, so the quantity of labour falls. The other three raise it."),
  mcq("s25_12", 5, "A PPC for consumer goods and capital goods shifts outwards. What could have caused this shift?", ["A decrease in mineral resources", "A decrease in prices of consumer goods", "An increase in employment", "An increase in technology"], 3, "Technology raises the economy's capacity. A rise in employment moves the economy towards the curve but does not shift it."),
  mcq("s24_12", 1, "A PPC shows the combinations of consumer goods and capital goods produced using all available resources. Position X lies outside the curve. What does position X indicate?", ["A lower ratio of capital to consumer goods is needed for growth", "Increasing levels of unemployment", "Insufficient factors of production are available", "Too many consumer goods are produced"], 2, "A point outside the PPC cannot be reached because the economy does not have enough factors of production."),
  mcq("w21_13", 1, "An economy's PPC for computers and cars is JK. It pivots inwards on the cars axis only. What could cause this?", ["A fall in output per worker in the car industry", "A fall in the level of competition in the car industry", "A rise in the potential workforce of the economy", "A rise in the price of cars"], 0, "Only the maximum output of cars falls, so a fall in productivity in the car industry is the cause. A rise in the workforce would shift the curve out on both axes."),
  mcq("w24_11", 5, "Farmers using traditional methods lack finance and often employ family members part-time. If working practices in agriculture are improved, how is this likely to be shown on the PPC?", ["By a movement along the PPC", "By an outward shift of the PPC on both axes", "By a movement from a point inside the PPC to a point on the PPC", "By an inward shift of the PPC"], 2, "Better use of existing resources moves the economy from inside the curve towards it: actual growth."),
  mcq("s22_14", 2, "A farmer with fixed land grows wheat and barley. Some barley land is flooded and cannot be used. The farmer then plants genetically modified wheat that gives higher yields on the remaining land. What is the likely effect on the farmer's PPC?", ["Both the maximum wheat and the maximum barley rise", "Both fall", "The maximum wheat rises and the maximum barley falls", "The maximum wheat falls and the maximum barley rises"], 2, "The flood reduces barley capacity and GM wheat raises wheat capacity, so the PPC pivots.")
]

exam = exam_page("shifts of the PPC and the significance of a position within it",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Shifts of the PPC, growth and unused resources are among the most frequent 8 mark questions in Paper 2 and often appear as 2 mark diagram parts in data response. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "5", "Feb/March 2022 (22) Q2(a); May/June 2020 (22) Q2(a); May/June 2023 (21) Q2(a); Oct/Nov 2022 (21) Q3(a); Oct/Nov 2024 (21) Q3(a)"), ("Data response, 2 marks", "2", "May/June 2023 (22) Q1(b); Feb/March 2024 (22) Q1(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("m22_22", "2(a)"), "8 marks", "Explain, with the help of a PPC diagram, how a decision to re-allocate resources in an economy to produce more capital goods and fewer consumer goods would affect consumers in both the short run and the long run.",
     ["Knowledge (up to 2): an accurate diagram labelled consumer goods and capital goods, with the PPC touching both axes.",
      "Application, short run (3): a movement along the curve (1), meaning fewer consumer goods and services available (1), leading to less choice, higher prices or lower living standards (1).",
      "Application, long run (3): an outward shift of the curve (1), perhaps leading to more consumer goods due to a larger capacity (1) and a rise in living standards (1)."],
     "PPC with consumer and capital goods. Short run: movement along. Long run: outward shift.",
     [[("k", "A PPC with consumer goods on one axis and capital goods on the other shows the combinations the economy can produce. Re-allocating resources to capital goods is a movement along the curve from a point with many consumer goods to a point with more capital goods.")], [("n", "In the short run consumers are worse off: fewer consumer goods and services are available, so there is less choice and prices may be higher, and living standards may fall.")], [("n", "In the long run the larger stock of capital expands the economy's capacity, so the PPC shifts outwards. The economy could then produce more of both goods, including more consumer goods than before, so living standards may rise above their original level.")]]),
  eq(P("s20_22", "2(a)"), "8 marks", "Use a PPC diagram to distinguish between the growth of an economy and a reduction in the number of unused resources in an economy, and explain one reason that might cause each to occur.",
     ["Knowledge (2): a PPC with appropriately labelled axes.",
      "Application, growth (up to 3): an outward shift of the curve with a valid example (1) and an explanation of what might cause it (1) and the diagram (1).",
      "Application, fewer unused resources (up to 3): a movement from within the curve to a point on or nearer the curve with a valid example (1) and an explanation of what might cause it (1) and the diagram (1)."],
     "One diagram: shift outward (e.g. new technology) and movement from inside the curve (e.g. higher demand cuts unemployment).",
     [[("k", "On a PPC for consumer goods and capital goods, growth of the economy's potential output is shown by an outward shift of the whole curve. A reduction in unused resources is shown by a movement from a point inside the curve to a point on or nearer the curve.")], [("n", "Growth might be caused by an improvement in technology, which raises the amount that can be produced with the same resources, so both outputs can rise.")], [("n", "A reduction in unused resources might be caused by higher aggregate demand, which leads firms to hire the unemployed, so output of both goods rises with no new resources and no opportunity cost.")]]),
  eq(P("s23_21", "2(a)"), "8 marks", "With the help of a diagram, explain the difference between the causes of a movement along, and a shift of, a PPC and consider which is likely to have the most immediate impact on an economy.",
     ["Knowledge (3): a PPC with labelled axes (1); a movement along it showing a trade-off between the two goods (1); a shift showing more of both goods with no trade-off (1).",
      "Analysis (3): a movement along is caused by a reallocation of resources between goods and involves an opportunity cost (2); a shift is caused by an increase in the quantity or quality of resources and allows more of both goods (1).",
      "Evaluation (2): a valid judgement on which has the most immediate impact, and a conclusion."],
     "Movement: reallocation, opportunity cost. Shift: more or better resources, technology. Judge which is quicker.",
     [[("k", "A movement along a PPC, for example from more consumer goods to more capital goods, is caused by a reallocation of resources, and it involves a trade-off: more of one good means less of the other. A shift of the PPC outwards allows more of both goods with no trade-off.")], [("n", "A movement is caused by a decision to use existing resources differently, whereas a shift is caused by an increase in the quantity or quality of resources, such as investment in machinery, training or new technology.")], [("e", "A reallocation can be made almost immediately by a change in spending or policy, so it is likely to have the most immediate impact. A shift takes years of investment, education or innovation to build capacity, so its effect is slower, though more lasting.")]]),
  eq(P("w22_21", "3(a)"), "8 marks", "Explain, with the use of a diagram, how the PPC of an economy could be affected by a decrease in the quantity of labour available but an increase in its quality.",
     ["Knowledge (up to 2): a PPC for an economy with two goods that shows the maximum combinations with resources fully used.",
      "Application, fall in quantity (up to 3): the PPC shifts to the left (1), with a diagram (1) and an explanation that the productive potential of the economy falls (1).",
      "Application, rise in quality (up to 3): the PPC shifts to the right (1), with a diagram and an explanation that productive potential increases (2)."],
     "Fewer workers: shift in. Better skills: shift out. Net effect depends on the size of each.",
     [[("k", "A PPC shows the maximum combinations of two goods that an economy can produce with its resources fully used.")], [("n", "A decrease in the quantity of labour reduces the economy's productive potential, so the PPC shifts to the left, with lower possible output of both goods. An increase in the quality of labour, through better training or education, raises productivity, so the PPC shifts to the right, with higher possible output of both goods.")], [("e", "The overall effect depends on which change is larger. If the improvement in quality outweighs the fall in numbers, the PPC will shift outwards overall, but if not it will shift inwards.")]]),
  eq(P("w24_21", "3(a)"), "8 marks", "With the help of a diagram, explain the significance of a position within a market economy's PPC and consider whether such a position is likely to be permanent.",
     ["Knowledge (3): a PPC with labelled axes (1), touching both axes (1), and a position inside the curve clearly shown (1).",
      "Analysis (3): inside the PPC, resources are being used inefficiently or not all are used; output of both goods is lower than if all were used; some reference to permanence.",
      "Evaluation (2): a valid judgement on whether such a position is likely to be permanent, and a conclusion."],
     "Diagram with a point inside. Meaning: unused resources, lower output of both goods. Permanent? In a market economy, recovery may happen but may be slow.",
     [[("k", "On a PPC for manufactured goods and agricultural goods, a point inside the curve shows that the economy is not using all of its resources, or is using them inefficiently.")], [("n", "Output of both goods is lower than possible. For example, workers are unemployed or factories are idle, so the economy could produce more of one or both goods without giving anything up.")], [("e", "Such a position may not be permanent. In a market economy, demand may recover and firms hire again, moving the economy towards the curve. However it could persist if unemployment is structural, if confidence is low or if markets adjust slowly, so the length of time depends on the cause.")]]),
  eq(P("s23_22", "1(b)"), "2 marks", "Using a PPC diagram, demonstrate the impact of the rising level of unemployment on an economy.",
     ["A fully and accurately labelled PPC with both axes labelled as products and the curve touching both (1).", "Showing a movement to the left within the curve, or from the curve to a position within the curve (1)."],
     "Draw and label. Show a move from the curve to a point inside it.",
     [[("k", "A PPC with two named goods on the axes, the curve touching both axes, and an arrow from a point on the curve to a point inside it, showing lower output of both goods as unemployment rises.")]])
  ],
  )

tips = tips_html(
  [("Separate shift from movement.", "Shift: more or better resources or technology. Movement along: reallocation. From inside to the curve: using idle resources."),
   ("Say a shift has no opportunity cost.", "More of both goods can be made."),
   ("Use consumer and capital goods.", "Capital goods now can shift the PPC out later."),
   ("State what inside means.", "Unused or inefficiently used resources; output of both goods could rise."),
   ("Outside is unattainable.", "Not enough resources now."),
   ("Mention actual and potential growth.", "Actual growth: movement towards the curve. Potential growth: an outward shift."),
   ("Judge permanence.", "A position inside may be temporary, but can persist with structural problems.")],
  [("Shift", "An outward shift of the PPC could be caused by an increase in the quantity or quality of resources or by better technology."),
   ("Inside", "A point inside the PPC could show that resources are unemployed or used inefficiently."),
   ("Growth", "Moving from inside the curve towards it could raise output without any opportunity cost."),
   ("Cost", "Producing more capital goods now might reduce consumption in the short run but could shift the PPC outwards in the future."),
   ("Permanent", "A position inside the PPC may not be permanent if demand recovers.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- PPC drawing ---------- */
const fy = (x, xm, ym) => ym * Math.sqrt(Math.max(0, 1 - (x / xm) * (x / xm)));
const QX = (x) => 90 + x * 4.0, QY = (y) => 300 - y * 2.0;
function pAxes(xl, yl) { return SV.line(90, 300, 650, 300) + SV.line(90, 300, 90, 30) + SV.text(650, 326, xl, "sm", { "text-anchor": "end" }) + SV.text(96, 24, yl, "sm"); }
const pcurve = (xm, ym, c, d) => { const p = []; for (let x = 0; x <= xm; x += 2) p.push([QX(x), QY(fy(x, xm, ym))]); p.push([QX(xm), QY(0)]); return SV.path(Lib.ptsPath(p), c, d); };

function shDraw(s) {
  let o = pAxes("Good X", "Good Y") + pcurve(100, 100, "c1", op(s.o > 0 || s.b > 0 || s.i > 0 ? 0.35 : 1)) + tag(QX(60), QY(fy(60, 100, 100)) - 10, "PPC₁", "t1", 1, "start");
  if (s.o > 0) o += pcurve(100 + 30 * s.o, 100 + 30 * s.o, "c3", op(1)) + tag(QX(95), QY(fy(95, 130, 130)) - 18, "PPC₂ (outward)", "t3", s.o, "start");
  if (s.b > 0) o += pcurve(100, 100 + 30 * s.b, "c2", op(1)) + tag(QX(30), QY(fy(30, 100, 130)) - 10, "PPC₃ (Y only)", "t2", s.b, "start");
  if (s.i > 0) o += pcurve(100 - 30 * s.i, 100 - 30 * s.i, "c4", op(1)) + tag(QX(40), QY(fy(40, 70, 70)) + 4, "PPC₄ (inward)", "t4", s.i, "middle");
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 345, label: "An outward shift of the PPC, a one-sided shift and an inward shift", base: { o: 0, b: 0, i: 0 }, draw: shDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The original PPC</b> for goods X and Y with maximum outputs of 100 of each.", s: { o: 0, b: 0, i: 0 } },
  { cap: "<b>An outward shift</b> (growth in potential output): more resources or better technology. The curve moves out on both axes, so more of both goods can be made, with no opportunity cost.", s: { o: 1, b: 0, i: 0 } },
  { cap: "<b>A one-sided shift.</b> A technology that helps only good Y raises the maximum Y but not X: the curve pivots on the Y axis.", s: { o: 0, b: 1, i: 0 } },
  { cap: "<b>An inward shift.</b> War, a natural disaster or a fall in the labour force reduces resources, so the whole curve moves in and potential output falls.", s: { o: 0, b: 0, i: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="An original PPC with an outward shift, a pivot on one axis and an inward shift">${shDraw({ o: 1, b: 1, i: 1 })}</svg>`;

function posDraw(s) {
  let o = pAxes("Good X", "Good Y") + pcurve(100, 100, "c1");
  const P = (x, y, c, l, k, dx, dy, an) => (k > 0 ? SV.circle(QX(x), QY(y), 8, c, op(k)) + tag(QX(x) + dx, QY(y) + dy, l, "t1", k, an) : "");
  o += P(50, 50, "dot2", "A: inside (unused resources)", s.a, -12, -10, "end") + P(70.7, 70.7, "dot4", "B: on the curve (efficient)", s.b, 12, 26, "start") + P(90, 90, "dot1", "C: outside (unattainable)", s.c, 12, -8, "start");
  if (s.m > 0) o += SV.line(QX(50), QY(50), QX(70.7), QY(70.7), "c3", { "stroke-width": 3, ...op(s.m) }) + SV.arrowHead(QX(70.7), QY(70.7), "r", "dot3") + tag(QX(50) + 4, QY(50) + 30, "actual growth: idle resources put to work", "t3", s.m, "start");
  if (s.g > 0) o += pcurve(135, 135, "c3 dash", op(s.g)) + tag(QX(4), QY(122), "potential growth: the curve shifts out, so C becomes attainable", "t3", s.g, "start");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 345, label: "Points inside, on and outside a PPC, with actual growth and potential growth", base: { a: 0, b: 0, c: 0, m: 0, g: 0 }, draw: posDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Inside the curve (A).</b> Some resources are unemployed or inefficiently used. More of one or both goods could be made at no opportunity cost.", s: { a: 1 } },
  { cap: "<b>On the curve (B).</b> Resources are fully and efficiently used. More of one good now means less of the other.", s: { a: 1, b: 1 } },
  { cap: "<b>Outside the curve (C).</b> Unattainable with existing resources and technology.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Actual growth.</b> Moving from A towards B uses idle resources, so output rises without any new resources.", s: { a: 1, b: 1, c: 1, m: 1 } },
  { cap: "<b>Potential growth.</b> Only a shift of the whole curve outwards (more or better resources) makes point C attainable.", s: { a: 1, b: 1, c: 1, m: 1, g: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Points inside, on and outside a PPC">${posDraw({ a: 1, b: 1, c: 1, m: 1, g: 0 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#lb") || !$("#tc") || !$("#ds")) return;
  const lb = +$("#lb").value / 100, tc = +$("#tc").value / 100, ds = +$("#ds").value / 100, xm = 100 * (1 + lb) * (1 - ds), ym = 100 * (1 + lb) * (1 + tc) * (1 - ds);
  $("#r1").textContent = Lib.fmtN(xm, 0) + " (" + (xm >= 100 ? "+" : "") + Lib.fmtN(xm - 100, 0) + ")"; $("#r2").textContent = Lib.fmtN(ym, 0) + " (" + (ym >= 100 ? "+" : "") + Lib.fmtN(ym - 100, 0) + ")"; $("#r3").textContent = xm > 100.5 && ym > 100.5 ? "Outward" : xm < 99.5 && ym < 99.5 ? "Inward" : Math.abs(xm - 100) < 0.5 && Math.abs(ym - 100) < 0.5 ? "None" : "One-sided / mixed";
  $("#rv").textContent = `Maximum X is now ${Lib.fmtN(xm, 0)} and maximum Y is ${Lib.fmtN(ym, 0)}. ${xm > 100.5 && ym > 100.5 ? "More of both goods can be made, an outward shift (potential growth) that does not involve an opportunity cost." : xm < 99.5 && ym < 99.5 ? "Less of both goods can be made: an inward shift, lower potential output." : "The curve has moved out on one axis and in (or not at all) on the other: a biased shift."}`;
  const X = (x) => 40 + x * 2.6, Y = (y) => 270 - y * 1.7; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Good X", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Good Y", "sm");
  const c = (xm_, ym_, cl, d) => { const p = []; for (let x = 0; x <= xm_; x += 2) p.push([X(x), Y(fy(x, xm_, ym_))]); p.push([X(xm_), Y(0)]); return SV.path(Lib.ptsPath(p), cl, d); };
  $("#labA").innerHTML = o + c(100, 100, "c1", op(0.45)) + c(xm, ym, "c3");
}
Lib.slider($("#g1"), { id: "lb", label: "More labour and capital (both goods), % ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "tc", label: "Technology raising Y only, % ", min: 0, max: 40, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "ds", label: "Resources lost in a disaster, % ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labG() {
  if (!$("#ks")) return;
  const k = +$("#ks").value / 100, c0 = 100 * (1 - k), g = 0.06 * k, cb0 = 90, gb = 0.006;
  let cross = null; for (let t = 0; t <= 80; t++) if (c0 * Math.pow(1 + g, t) >= cb0 * Math.pow(1 + gb, t)) { cross = t; break; }
  $("#t1").textContent = Lib.fmtN(c0, 0); $("#t2").textContent = Lib.fmtN(g * 100, 1) + "%"; $("#t3").textContent = k <= 0.1 ? "–" : cross === null ? "over 80 yrs" : (cross === 0 ? "0" : cross) + " yrs";
  $("#tv").textContent = k <= 0.1 ? "This is the same as the baseline economy: 10% of resources in capital goods." : `Putting ${Lib.fmtN(k * 100, 0)}% of resources into capital goods cuts consumption today to ${Lib.fmtN(c0, 0)} (against 90), but raises growth of capacity to ${Lib.fmtN(g * 100, 1)}% a year. ${cross === null ? "It never catches up within 80 years in this model." : "Consumption overtakes the 10% economy after about " + cross + " years."} This is the opportunity cost of growth: less consumption now for more later. (Illustrative model.)`;
  const X = (t) => 40 + t * 8.4, mx = 220, Y = (v) => 270 - v / mx * 230; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Consumption", "sm");
  const pa = [], pb = []; for (let t = 0; t <= 40; t++) { pa.push([X(t), Y(Math.min(mx, cb0 * Math.pow(1 + gb, t)))]); pb.push([X(t), Y(Math.min(mx, c0 * Math.pow(1 + g, t)))]); }
  o += SV.path(Lib.ptsPath(pa), "c2 dash") + SV.path(Lib.ptsPath(pb), "c1") + tag(396, Y(cb0 * Math.pow(1 + gb, 40)) - 8, "10% invested", "t2", 1, "end") + tag(396, Math.max(40, Y(Math.min(mx, c0 * Math.pow(1 + g, 40)))) + 18, "your choice", "t1", 1, "end");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "ks", label: "Share of resources in capital goods, % ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v + "%", onInput: labG });
labG();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What does it show on a PPC?", ["Movement along", "Shift", "Movement towards the curve"],
  [("A government moves resources from consumer goods to capital goods", 0), ("New technology raises the output of all goods", 1), ("Unemployed workers find jobs as demand recovers", 2), ("More immigration increases the labour force", 1), ("A farmer switches land from wheat to barley", 0), ("Idle factories are put back into use", 2), ("A flood destroys part of a country's farmland", 1), ("Producing more cars and fewer trucks with the same resources", 0)],
  "Reallocation is a movement along; more or better resources shift the curve; idle resources move the economy from inside towards the curve.") + MATCH([
  ["Outward shift", "More of both goods can be made: potential growth"],
  ["Inward shift", "Potential output falls because resources are lost"],
  ["Inside the PPC", "Resources are unused or used inefficiently"],
  ["On the PPC", "Resources are fully and efficiently used"],
  ["Outside the PPC", "Unattainable with current resources"],
  ["Actual growth", "Using idle resources, moving towards the curve"]]) + ORDER(
  "Put the effects of a recession and recovery in order.",
  ["Demand falls and firms cut output", "Unemployment rises and some factories sit idle", "The economy moves to a point inside the PPC", "Demand recovers and firms hire workers again", "The economy moves back towards the PPC: actual growth"],
  "A recession is a move inside the curve; recovery is a move back towards it.") + CALC([
  {"q": "An economy's maximum output of Y rises from 100 to 130 after a technology boost. Calculate the percentage increase in the maximum output of Y (%).", "a": 30, "unit": "%", "tol": 0.5, "hint": "30 ÷ 100.", "sol": "<b>30%</b>."},
  {"q": "An economy operating inside its PPC produces 60 units of Y when it could produce 80. By what percentage is actual output below potential (%)?", "a": 25, "unit": "%", "tol": 0.5, "hint": "(80 − 60) ÷ 80.", "sol": "<b>25%</b> below potential."},
  {"q": "Moving to the curve, actual output of Y rises from 60 to 80. Calculate the percentage increase in actual output (%, 1 decimal place).", "a": 33.3, "unit": "%", "tol": 0.1, "hint": "20 ÷ 60.", "sol": "<b>33.3%</b>."},
  {"q": "An economy that puts 40% of its resources into capital goods has consumption of 60 each year. The baseline economy has 90. By how many units is consumption lower today?", "a": 30, "unit": "units", "tol": 0.5, "hint": "90 − 60.", "sol": "<b>30 units</b>: the opportunity cost of faster future growth."}]) + MCQ([
  ("An outward shift of the PPC could be caused by:", ["Investment in new technology", "A fall in the labour force", "A recession", "A move along the curve"], 0, "Better technology raises potential output."),
  ("A point inside the PPC means that:", ["Resources are unused or inefficiently used", "Resources are fully used", "The point cannot be reached", "Opportunity cost is zero everywhere"], 0, "Output could be raised without giving anything up."),
  ("Which is a movement along the PPC?", ["Moving resources from food to cars", "New technology in all industries", "A rise in the labour force", "A fall in unemployment"], 0, "Reallocating existing resources is a movement along the curve."),
  ("Producing more capital goods now is likely to:", ["Shift the PPC outwards in the future", "Shift the PPC inwards", "Move the economy outside the PPC immediately", "Have no effect on consumption"], 0, "More capital raises future capacity, at the cost of current consumption."),
  ("A point outside the PPC is:", ["Unattainable now", "Inefficient", "On the curve", "A movement along"], 0, "Not enough resources.")
], "qz1") + CARDS([
  ("Outward shift", "More resources or better technology; potential growth."),
  ("Inward shift", "Fall in resources; lower potential output."),
  ("Movement along", "Reallocation; opportunity cost."),
  ("Inside", "Unused or inefficient resources."),
  ("On", "Full and efficient use."),
  ("Outside", "Unattainable."),
  ("Actual growth", "From inside towards the curve."),
  ("Cost of growth", "Fewer consumer goods now.")]) + MCQ(mc_exam)

build("as17", "as-ppc-shifts-position", "The PPC: Shifts and Position", EY,
  "1.5.3 to 1.5.4: the causes and consequences of shifts of the PPC, and the significance of being inside, on or outside it. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
