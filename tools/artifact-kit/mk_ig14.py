"""Builds the four IGCSE Economics 1.4 Production possibility curve reviews (1.4.1 to 1.4.4).
Run: python3 tools/artifact-kit/mk_ig14.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# Shared PPC drawing: x = consumer goods, y = capital goods, both 0-100.
PPCJS = '''
const PX = (x) => 90 + x * 5.4, PY2 = (y) => 310 - y * 2.3;
function ppcPath(a, b) { let d = ""; for (let i = 0; i <= 40; i++) { const t = (i / 40) * Math.PI / 2, x = a * Math.cos(t), y = b * Math.sin(t); d += (i ? "L" : "M") + PX(x).toFixed(1) + " " + PY2(y).toFixed(1); } return d; }
function ppcAxes(xl, yl) { return SV.line(PX(0), PY2(0), PX(0), PY2(130)) + SV.line(PX(0), PY2(0), PX(118), PY2(0)) + SV.text(PX(0) + 8, 14, yl || "Capital goods", "sm") + SV.text(PX(118), PY2(0) + 24, xl || "Consumer goods", "sm", { "text-anchor": "end" }); }
function ppcDot(x, y, lab, cl, side) { return SV.circle(PX(x), PY2(y), 7, cl || "dot1") + SV.text(PX(x) + (side === "l" ? -12 : 12), PY2(y) + (side === "l" ? -6 : 4), lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }
function ppcDrop(x, y) { return SV.line(PX(0), PY2(y), PX(x), PY2(y), "gr") + SV.line(PX(x), PY2(y), PX(x), PY2(0), "gr"); }
function onPPC(x, y, a, b) { return (x / a) ** 2 + (y / b) ** 2; }
'''

# =========================================================== 1.4.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">production possibility curve (PPC)</span> shows the <b>maximum combinations of two goods or services</b> an economy can produce with its <b>existing resources and technology</b>, when all resources are fully and efficiently used. It is a model of <b>scarcity, choice and opportunity cost</b>: to produce more of one good, the economy must produce less of the other.</p></div>

  <h2>Drawing a PPC</h2>
  <ul>
    <li>Put one type of good on the <b>horizontal axis</b> (for example consumer goods) and the other on the <b>vertical axis</b> (for example capital goods).</li>
    <li>The curve runs from one axis to the other. Where it meets the vertical axis, <b>all</b> resources make capital goods; where it meets the horizontal axis, <b>all</b> make consumer goods.</li>
    <li>It is usually drawn <b>bowed outwards</b> (concave to the origin), because resources are not equally good at making both goods.</li>
    <li>Label both axes and the curve (PPC).</li>
  </ul>

  <h2>Reading a PPC</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>What it shows</th></tr>
    <tr><td><b>A point on the curve</b></td><td>A combination of the two goods that can be produced with all resources used fully and efficiently</td></tr>
    <tr><td><b>Axis intercepts</b></td><td>The maximum of one good if none of the other is made</td></tr>
    <tr><td><b>Slope</b></td><td>The trade-off: how much of one good must be given up for more of the other (opportunity cost)</td></tr>
    <tr><td><b>Shape</b></td><td>Bowed out: opportunity cost rises as more of a good is made. Straight line: constant opportunity cost</td></tr>
  </table></div>
  <p class="note">A PPC is drawn for a given time, resource base and technology. It can show goods in an economy, in a firm, or in a household's use of time, though the syllabus concentrates on whole economies.</p>
'''
js = HEAD + COMMON + PPCJS + '''
Lib.stepper($("#stP"), { w: 760, h: 380, label: "Building a PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes();
  if (s.n >= 1) o += SV.text(PX(0) - 8, PY2(90), "90", "sm", { "text-anchor": "end" }) + SV.text(PX(80), PY2(0) + 40, "80", "sm", { "text-anchor": "middle" }) + ppcDot(0, 90, "", "dot1") + ppcDot(80, 0, "", "dot1");
  if (s.n >= 2) o += SV.path(ppcPath(80, 90), "c1");
  if (s.n >= 2) o += SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  if (s.n >= 3) { const x = 80 * Math.cos(0.7), y = 90 * Math.sin(0.7); o += ppcDrop(x, y) + ppcDot(x, y, "A", "dot2"); }
  return o;
}, steps: [
  { cap: "Put capital goods on the vertical axis and consumer goods on the horizontal axis.", s: { n: 0 } },
  { cap: "If all resources make <b>capital goods</b> the economy makes 90 and no consumer goods. If all make <b>consumer goods</b> it makes 80 and no capital goods.", s: { n: 1 } },
  { cap: "Join the two ends with a curve bowed outwards: the <b>PPC</b>. Every point on it uses resources fully and efficiently.", s: { n: 2 } },
  { cap: "Point <b>A</b> on the curve is one combination of both goods the economy can produce.", s: { n: 3 } },
] });
const OC = ["Resources are scarce", "Choose to make more consumer goods", "Resources move from capital goods production", "Less capital goods are produced", "Opportunity cost = the capital goods given up"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "Opportunity cost on the PPC", base: { n: 0 }, draw: mkChain(OC, "--accent"), steps: chainSteps(["<b>Resources are scarce</b>.", "The economy chooses to make <b>more consumer goods</b>.", "<b>Resources move</b> from capital goods production.", "<b>Less capital goods</b> are produced.", "The opportunity cost is the <b>capital goods given up</b>."]) });

/* Lab 1: draw your own PPC */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc")) return;
  const a = +$("#pa").value, b = +$("#pb").value, share = +$("#pc").value / 100, t = (1 - share) * Math.PI / 2 * 0.99, x = a * Math.cos(Math.PI / 2 * share), y = b * Math.sin(Math.PI / 2 * share);
  const cx = a * Math.sin(Math.PI / 2 * (1 - share)), cy = b * Math.cos(Math.PI / 2 * (1 - share));
  const px = a * Math.cos(Math.PI / 2 * share), py = b * Math.sin(Math.PI / 2 * share);
  $("#pa1").textContent = money(px, 0); $("#pa2").textContent = money(py, 0); $("#pa3").textContent = Math.round(share * 100) + "%";
  $("#pav").textContent = `With ${Math.round(share * 100)}% of resources on capital goods the economy makes ${money(py, 0)} capital goods and ${money(px, 0)} consumer goods. Moving more resources to capital goods raises capital output but lowers consumer goods: that is the trade-off.`;
  $("#labP").innerHTML = ppcAxes() + SV.path(ppcPath(a, b), "c1") + ppcDrop(px, py) + ppcDot(px, py, "", "dot2") + SV.text(PX(a) , PY2(0) + 40, a, "sm", { "text-anchor": "middle" }) + SV.text(PX(0) - 8, PY2(b), b, "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "pa", label: "Maximum consumer goods (all resources on them)", min: 40, max: 100, step: 10, value: 80, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Maximum capital goods (all resources on them)", min: 40, max: 100, step: 10, value: 90, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Share of resources on capital goods", min: 5, max: 95, step: 5, value: 50, fmt: (v) => v + "%", onInput: labP });
const RD = [
  { n: "Both axes", d: "Label the two goods. Always label both axes." },
  { n: "Intercepts", d: "The maximum of one good if none of the other is produced." },
  { n: "Curve shape", d: "Bowed out: resources are not equally suited to both goods, so opportunity cost rises." },
  { n: "Point on the curve", d: "Full and efficient use of all resources." },
  { n: "Slope", d: "The trade-off between the two goods: the opportunity cost." },
];
button_table("rdBtns", "rdOut", RD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Meaning</th></tr><tr><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b> for a PPC?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "It shows the maximum combinations of two goods", b: 0 }, { text: "Every point on it uses resources fully", b: 0 }, { text: "It shows scarcity and opportunity cost", b: 0 }, { text: "It is usually drawn bowed outwards", b: 0 },
  { text: "It shows what consumers want to buy", b: 1 }, { text: "It shows unlimited production", b: 1 }, { text: "It can slope upwards", b: 1 },
], done: "A PPC shows what is possible, not what is wanted." });
Lib.match($("#m1"), { prompt: "Match the PPC term to its meaning.", pairs: [
  ["PPC", "Maximum combinations of two goods with existing resources"],
  ["Intercept", "Maximum of one good if none of the other is made"],
  ["Opportunity cost", "What is given up to produce more of the other good"],
  ["Bowed-out curve", "Opportunity cost rises as more of a good is made"],
  ["Straight-line PPC", "Constant opportunity cost"],
  ["Point on the curve", "Full and efficient use of resources"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>drawing a PPC</b>.", items: [
  "Label the axes with the two goods",
  "Mark the maximum of each good on its axis",
  "Join the points with a curve bowed outwards",
  "Label the curve PPC",
  "Mark and label a point on the curve",
], done: "Always label." });
''' + calc_js([
    ("On a PPC, an economy can make 90 capital goods or 80 consumer goods (not both). It produces 40 consumer goods and 78 capital goods. How many consumer goods are given up compared with the maximum?", 40, "80 − 40 = <b>40</b>.", None, None),
    ("The PPC for good X and good Y: 100 X and 0 Y at one end, 60 X and 30 Y at another. What is the opportunity cost of moving to the second point in units of X?", 40, "100 − 60 = <b>40 X</b> given up for 30 Y.", None, None),
]) + mcq_js("qz1", [
    ("A PPC shows:", ["Maximum combinations of two goods", "The demand curve", "Prices", "Unemployment"], 0, "What the economy can produce."),
    ("A point on the PPC represents:", ["Wasted resources", "Full and efficient use of resources", "Unattainable output", "Inflation"], 1, "Maximum output."),
    ("A PPC is bowed outwards because:", ["Resources are equally good at both", "Resources are not equally good at making both goods", "Prices rise", "Wants are unlimited"], 1, "Resources differ."),
    ("A PPC illustrates:", ["Scarcity, choice and opportunity cost", "Inflation", "Demand and supply", "Trade"], 0, "The economic problem."),
    ("The end of the curve on the vertical axis shows:", ["Zero of both goods", "Maximum of the vertical good with none of the other", "A free good", "Unemployment"], 1, "All resources on one good."),
]) + "\n" + cards_js([("Production possibility curve", "A curve showing the maximum combinations of two goods an economy can produce with existing resources."), ("Consumer goods", "Goods bought by households to satisfy wants."), ("Capital goods", "Goods used to produce other goods and services."), ("Intercept", "The point where the curve meets an axis."), ("Concave", "Curved outwards, away from the origin."), ("Opportunity cost", "The next best alternative given up."), ("Efficiency", "Producing with no waste of resources."), ("Full employment of resources", "All available resources in use."), ("Trade-off", "Giving up one thing to get another.")]) + "labP(); \n"
explore = '''
  <h2>Lab 1 · Draw a PPC</h2>
  <p>Set the maximum of each good, then slide the share of resources between them to move along the curve.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Consumer goods</small><strong id="pa1"></strong></div><div><small>Capital goods</small><strong id="pa2"></strong></div><div><small>Resources on capital</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 340" role="img" aria-label="A production possibility curve"></svg>
  </div>

  <h2>Lab 2 · Reading a PPC</h2>
  <p>Pick a feature to see what it means.</p>
  <div class="card"><div class="row" id="rdBtns"></div><div id="rdOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define a production possibility curve (PPC). (May/June 2021, P22 style)", "Maximum combinations of two goods with existing resources.", "[K|A PPC shows the maximum combinations of two goods or services] [K|that an economy can produce with its existing resources.]"),
    Q(2, "Explain", 4, "Explain why a PPC is usually bowed outwards.", "Resources not equally suited; opportunity cost rises.",
      "[K|Resources are not equally suited to producing both goods.] [N|When an economy makes more of one good it has to use resources less suited to it,] [N|so more of the other good is given up for each extra unit: the opportunity cost rises, giving a bowed-out curve.]"),
    Q(3, "Explain", 4, "Explain how a PPC illustrates scarcity and opportunity cost.", "Limited resources; cannot have more of both; move along the curve.",
      "[K|A PPC shows the limit of what an economy can produce with its scarce resources, so scarcity is shown by the curve itself.] [N|To produce more of one good the economy has to move along the curve, which means producing less of the other.] [N|The amount of the other good given up is the opportunity cost.]"),
    Q(4, "Identify", 2, "Identify two things a point on a PPC tells us.", "Full employment; efficient; combination possible.", "[K|It is a combination of two goods that the economy can produce.] [K|All resources are fully and efficiently used.]"),
)
tp = tips([
    ("Label both axes and the curve.", "Always."),
    ("A PPC shows what is possible.", "Not what consumers want."),
    ("Bowed out means rising opportunity cost.", "Straight line means constant."),
    ("A point on the curve is efficient.", "All resources fully employed."),
    ("Draw it with a ruler for the axes and freehand for the curve.", "Neat diagrams earn marks."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("1.4.1 Production possibility curves (PPC)"), "Production Possibility Curves", "Defining a PPC, drawing it and interpreting what it shows about scarcity and opportunity cost. Syllabus 1.4.1.",
    learn=learn, watch=watch(("Building a PPC", "stP"), ("Opportunity cost on the PPC", "stO")), explore=explore,
    practise=practise(("True or false?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the steps", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Guns or butter", "A government choosing between defence and healthcare faces the PPC trade-off: more of one means less of the other.", "A PPC trade-off in practice."),
        rw("A farmer's field", "A farmer can plant a field with wheat or barley: more of one means less of the other.", "A firm-level PPC."),
        rw("Your time", "A student has 24 hours to divide between study and leisure: a PPC for time.", "A household PPC."),
        rw("Wartime economies", "In wartime, countries shift resources from consumer goods to military goods, moving along their PPC.", "Moving along a PPC.")),
    exam=ex, tips=tp)
write("p41", body, js, "Production Possibility Curves", "ig-ppc-definition")

# =========================================================== 1.4.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Where a production point lies compared with the PPC tells you how well an economy is using its resources. A point <b>on</b> the PPC is <b>efficient</b> (full employment of resources). A point <b>inside</b> (under) the PPC is <b>inefficient</b>: resources are wasted. A point <b>outside</b> (beyond) the PPC is <b>unattainable</b> with current resources and technology.</p></div>

  <h2>Three possible positions</h2>
  <div class="tw"><table class="t">
    <tr><th>Position</th><th>Meaning</th><th>Possible reasons</th></tr>
    <tr><td><b>On the PPC</b></td><td>Full and efficient use of all resources: maximum output</td><td>Full employment; resources allocated efficiently</td></tr>
    <tr><td><b>Inside (under) the PPC</b></td><td>Resources are <b>unemployed or inefficiently used</b>: the economy could produce more of one or both goods</td><td>Unemployment (recession), under-used land or machinery, poor management, lack of skills or mismatch, natural disasters, war</td></tr>
    <tr><td><b>Outside (beyond) the PPC</b></td><td><b>Unattainable</b> with current resources and technology</td><td>Possible only if the PPC shifts outwards (economic growth)</td></tr>
  </table></div>

  <h2>What happens when an economy is inside the PPC?</h2>
  <ul>
    <li>It can move <b>up to the curve</b> by using unemployed resources: it can produce <b>more of one or both goods</b> at <b>no opportunity cost</b>.</li>
    <li>This is what happens when an economy recovers from a <b>recession</b>.</li>
    <li>Moves are caused by changes in the use of resources, not in the quantity or quality of resources.</li>
  </ul>
  <p class="note">An economy can be on the PPC but still produce a combination people do not want. The PPC shows what is possible, not what is best.</p>
'''
js = HEAD + COMMON + PPCJS + '''
Lib.stepper($("#stP"), { w: 760, h: 380, label: "Under, on and beyond the PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  if (s.n >= 1) o += ppcDot(80 * Math.cos(0.7), 90 * Math.sin(0.7), "A (on)", "dot3");
  if (s.n >= 2) o += ppcDot(32, 35, "B (inside)", "dot2");
  if (s.n >= 3) o += ppcDot(72, 78, "C (outside)", "dot4") + SV.text(PX(72) + 12, PY2(78) + 22, "unattainable now", "sm");
  return o;
}, steps: [
  { cap: "The PPC marks the limit of what the economy can produce.", s: { n: 0 } },
  { cap: "Point <b>A</b> is <b>on</b> the PPC: all resources fully and efficiently used.", s: { n: 1 } },
  { cap: "Point <b>B</b> is <b>inside</b> the PPC: resources are unemployed or wasted. The economy could produce more.", s: { n: 2 } },
  { cap: "Point <b>C</b> is <b>outside</b>: it cannot be reached with existing resources and technology.", s: { n: 3 } },
] });
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Recovery from a recession", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1") + ppcDot(32, 35, "B", "dot2");
  if (s.n >= 1) o += SV.line(PX(32), PY2(35), PX(32), PY2(90 * Math.sqrt(1 - (32 / 80) ** 2)), "c3");
  if (s.n >= 2) o += ppcDot(32, 90 * Math.sqrt(1 - (32 / 80) ** 2), "D", "dot3");
  if (s.n >= 3) o += SV.line(PX(32), PY2(35), PX(80 * Math.sqrt(1 - (35 / 90) ** 2)), PY2(35), "c3") + ppcDot(80 * Math.sqrt(1 - (35 / 90) ** 2), 35, "E", "dot3");
  return o;
}, steps: [
  { cap: "In a recession the economy is at <b>B</b>, inside the PPC, with unemployed resources.", s: { n: 0 } },
  { cap: "If unemployed resources are put to use, output can rise to the curve.", s: { n: 1 } },
  { cap: "Moving to <b>D</b> produces <b>more capital goods</b> with the same consumer goods: no opportunity cost.", s: { n: 2 } },
  { cap: "Or to <b>E</b>: more consumer goods with the same capital goods. Any point between D and E gives more of both.", s: { n: 3 } },
] });

/* Lab 1: place a point */
function labL() {
  if (!$("#la") || !$("#lb")) return;
  const x = +$("#la").value, y = +$("#lb").value, r = onPPC(x, y, 80, 90), st = r > 1.02 ? "Outside: unattainable" : r < 0.98 ? "Inside: inefficient" : "On: efficient";
  $("#la1").textContent = st.split(":")[0]; $("#la2").textContent = r < 0.98 ? "Yes" : "No"; $("#la3").textContent = r > 1.02 ? "Yes" : "No";
  $("#lav").textContent = `${x} consumer goods and ${y} capital goods: ${st.toLowerCase()}. ${r < 0.98 ? "Resources are unemployed or wasted: the economy could move up or out to the curve and produce more of one or both goods." : r > 1.02 ? "This is more than the economy can produce now; it needs economic growth to reach it." : "All resources are fully and efficiently used."}`;
  $("#labL").innerHTML = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1") + ppcDrop(x, y) + ppcDot(x, y, "", r > 1.02 ? "dot4" : r < 0.98 ? "dot2" : "dot3");
}
Lib.slider($("#g1"), { id: "la", label: "Consumer goods produced", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Capital goods produced", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labL });
const WH = [
  { n: "A recession with high unemployment", p: "Inside the PPC", e: "Resources are unemployed." },
  { n: "Full employment and efficient production", p: "On the PPC", e: "Maximum output." },
  { n: "A target output beyond current capacity", p: "Outside the PPC", e: "Unattainable without growth." },
  { n: "A war destroys factories", p: "PPC shifts inwards; point may be inside", e: "Fewer resources." },
  { n: "Workers' skills do not match the jobs available", p: "Inside the PPC", e: "Resources are under-used." },
  { n: "Pollution closes farmland", p: "Inside or PPC shifts inwards", e: "Resources lost or wasted." },
];
button_table("whBtns", "whOut", WH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Position</th><th>Why</th></tr><tr><td><b>${p.p}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Where is each point compared with the PPC?", buckets: [{ label: "On the PPC" }, { label: "Inside the PPC" }, { label: "Outside the PPC" }], items: [
  { text: "Full employment of all resources", b: 0 }, { text: "Maximum efficient output", b: 0 },
  { text: "High unemployment in a recession", b: 1 }, { text: "Resources wasted by poor management", b: 1 },
  { text: "Unattainable with current resources", b: 2 }, { text: "Needs economic growth to reach", b: 2 },
], done: "On = efficient; inside = wasteful; outside = unattainable." });
Lib.classify($("#cl2"), { prompt: "Does each cause the economy to be <b>inside</b> its PPC or to <b>move to</b> it?", buckets: [{ label: "Moves inside" }, { label: "Moves to the PPC" }], items: [
  { text: "A rise in unemployment", b: 0 }, { text: "Factories left idle in a recession", b: 0 }, { text: "Skills mismatch", b: 0 },
  { text: "Unemployed workers find jobs", b: 1 }, { text: "Idle factories restart", b: 1 }, { text: "Better management", b: 1 },
], done: "Using resources moves the economy towards the curve." });
Lib.match($("#m1"), { prompt: "Match the position to its meaning.", pairs: [
  ["On the PPC", "Full and efficient use"],
  ["Inside the PPC", "Unemployed or wasted resources"],
  ["Outside the PPC", "Unattainable at present"],
  ["Recession", "The economy is inside its PPC"],
  ["Recovery", "Moving towards the PPC"],
  ["Economic growth", "A shift outwards of the PPC"],
], done: "Know what each position means." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an economy recovers from a recession</b>.", items: [
  "The economy is inside its PPC with unemployed resources",
  "Demand recovers and firms hire",
  "Unemployed resources are used",
  "Output of one or both goods rises",
  "The economy returns to the PPC",
], done: "Recovery uses idle resources." });
''' + calc_js([
    ("A point on an economy's PPC is 60 consumer goods and 70 capital goods. The economy actually produces 60 consumer goods and 40 capital goods. How many more capital goods could it produce with no loss of consumer goods?", 30, "70 − 40 = <b>30</b>.", None, None),
    ("Output is 60% of capacity. Capacity is 200 units. How many units are produced?", 120, "60% × 200 = <b>120</b>.", None, None),
]) + mcq_js("qz1", [
    ("A point inside the PPC shows:", ["Full employment", "Unemployed or wasted resources", "Unattainable output", "Economic growth"], 1, "Inefficiency."),
    ("A point outside the PPC is:", ["Efficient", "Unattainable now", "Inefficient", "A recession"], 1, "Beyond current resources."),
    ("Moving from inside the PPC to the curve has:", ["A high opportunity cost", "No opportunity cost", "Fewer goods", "No benefit"], 1, "Unused resources are put to work."),
    ("Which could cause a point inside the PPC?", ["High unemployment", "New technology", "More workers", "Better education"], 0, "Resources are idle."),
    ("To reach a point outside the PPC an economy needs:", ["Unemployment", "Economic growth", "A recession", "Lower taxes only"], 1, "More or better resources."),
]) + "\n" + cards_js([("On the PPC", "Full and efficient use of resources."), ("Inside the PPC", "Under-used or wasted resources."), ("Outside the PPC", "Unattainable with current resources and technology."), ("Efficiency", "Using resources without waste."), ("Unemployment", "People who want to work but cannot find a job."), ("Recession", "A fall in real GDP for two consecutive quarters."), ("Recovery", "A rise in output after a recession."), ("Productive capacity", "The maximum output an economy can produce."), ("Full employment", "All available resources in use.")]) + "labL(); \n"
explore = '''
  <h2>Lab 1 · Where is the point?</h2>
  <p>Set the output of each good and see whether it is inside, on or outside the PPC.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Position</small><strong id="la1"></strong></div><div><small>Wasted resources?</small><strong id="la2"></strong></div><div><small>Unattainable?</small><strong id="la3"></strong></div></div><div class="verdict" id="lav"></div></div></div>
    <svg id="labL" viewBox="0 0 760 340" role="img" aria-label="A point inside, on or outside a PPC"></svg>
  </div>

  <h2>Lab 2 · What does it mean?</h2>
  <p>Pick a situation to see where it puts the economy.</p>
  <div class="card"><div class="row" id="whBtns"></div><div id="whOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain what is meant by a point inside a PPC.", "Unemployed or inefficiently used resources; could produce more.",
      "[K|A point inside the PPC means resources are not fully or efficiently used,] [N|for example there is unemployment or machinery lies idle.] [N|The economy could produce more of one or both goods by using these resources.]"),
    Q(2, "Explain", 4, "Explain why a point outside a PPC is unattainable.", "Beyond what resources and technology allow.",
      "[K|A PPC shows the maximum output possible with the economy's existing resources and technology.] [N|A point outside it needs more resources or better technology than the economy has,] [N|so it cannot be reached until economic growth shifts the PPC outwards.]"),
    Q(3, "Explain", 4, "Explain why a recession can be shown as a point inside the PPC.", "Unemployment; falling output; resources idle.",
      "[K|In a recession output falls and unemployment rises, so labour and capital are not fully used.] [N|The economy is producing less than its maximum, which is shown by a point inside the PPC.]"),
    Q(4, "Analyse", 6, "Analyse why an economy may be producing at a point inside its PPC and how it could move to the curve. (Oct/Nov 2023, P22 style)", "Causes: unemployment, inefficiency, mismatch; policies: demand, training, efficiency.",
      "[K|An economy could be inside its PPC because of unemployment during a recession, when demand is low.] [N|Skills mismatches and poor management also leave resources under-used.] [N|Government spending, lower interest rates or lower taxes could raise demand so unemployed resources are used.] [N|Training and better organisation could improve how well resources are matched to jobs.] [E|The size of the gain depends on how much spare capacity there is.]", key=True),
)
tp = tips([
    ("On = efficient; inside = wasteful; outside = unattainable.", "Learn these three."),
    ("Moving from inside to the curve has no opportunity cost.", "Idle resources are used."),
    ("Outside the curve needs growth.", "A shift of the PPC."),
    ("Recession = inside the PPC.", "Recovery = move towards it."),
    ("Mark and label points A, B, C.", "Easier to refer to in your answer."),
], cmds("Explain", "Analyse"))
body = page(CL("1.4.2 Points under, on and beyond a PPC"), "Points Under, On and Beyond a PPC", "What it means when an economy produces inside, on or outside its production possibility curve. Syllabus 1.4.2.",
    learn=learn, watch=watch(("Under, on and beyond the PPC", "stP"), ("Recovery from a recession", "stR")), explore=explore,
    practise=practise(("Where is the point?", "cl1", "card"), ("Moves inside or moves to?", "cl2", "card"), ("Match the position", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The 2008 financial crisis", "Output fell and unemployment rose in many countries, leaving them well inside their PPC.", "A recession."),
        rw("COVID-19 lockdowns", "Many economies produced far below capacity in 2020 as factories, shops and services closed.", "Inside the PPC."),
        rw("Recovery after a recession", "As unemployment falls and firms hire again, output rises back towards capacity.", "Moving towards the PPC."),
        rw("War and disasters", "Destroyed factories and farmland reduce capacity and push the PPC inwards.", "A fall in capacity.")),
    exam=ex, tips=tp)
write("p42", body, js, "Points Under, On and Beyond a PPC", "ig-ppc-points")

# =========================================================== 1.4.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <b>movement along the PPC</b> shows the economy <b>reallocating resources</b> from one good to the other. More of one good means <b>less of the other</b>: the amount given up is the <b>opportunity cost</b>. With a bowed-out PPC, the opportunity cost <b>rises</b> as more of a good is produced.</p></div>

  <h2>Calculating opportunity cost from a PPC</h2>
  <div class="formula">Opportunity cost of one more unit of A = units of B given up ÷ extra units of A gained</div>
  <div class="tw"><table class="t">
    <tr><th>Point</th><th>Consumer goods</th><th>Capital goods</th><th>Opportunity cost of the move</th></tr>
    <tr><td>A</td><td>0</td><td>90</td><td></td></tr>
    <tr><td>B</td><td>20</td><td>86</td><td>4 capital goods for 20 consumer goods (0.2 per unit)</td></tr>
    <tr><td>C</td><td>40</td><td>76</td><td>10 for 20 (0.5 per unit)</td></tr>
    <tr><td>D</td><td>60</td><td>60</td><td>16 for 20 (0.8 per unit)</td></tr>
    <tr><td>E</td><td>80</td><td>0</td><td>60 for 20 (3 per unit)</td></tr>
  </table></div>
  <p>The opportunity cost of each extra consumer good rises from 0.2 to 3 capital goods: the more consumer goods are made, the more capital goods must be given up for each extra one. This is why the curve is bowed outwards.</p>

  <h2>Why opportunity cost rises</h2>
  <ul>
    <li>Resources are <b>not perfectly mobile</b>: those best suited to capital goods are used first for them.</li>
    <li>To make more consumer goods, resources less suited to them must be switched, so output per resource falls and more capital goods are given up per extra unit.</li>
    <li>With a <b>straight-line</b> PPC the opportunity cost is constant.</li>
  </ul>
  <h2>Significance</h2>
  <ul>
    <li>Moving along the PPC shows the <b>choice</b> between goods, for example <b>consumption now</b> versus <b>capital goods for the future</b>.</li>
    <li>Producing more capital goods today can <b>shift the PPC outwards</b> in future (economic growth), but means fewer consumer goods now.</li>
  </ul>
'''
js = HEAD + COMMON + PPCJS + '''
Lib.stepper($("#stM"), { w: 760, h: 380, label: "Moving along the PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  const pt = (t) => [80 * Math.cos(t), 90 * Math.sin(t)], a = pt(1.1), b = pt(0.7);
  o += ppcDot(a[0], a[1], "A", "dot1");
  if (s.n >= 1) o += ppcDrop(a[0], a[1]);
  if (s.n >= 2) o += ppcDot(b[0], b[1], "B", "dot2") + SV.line(PX(a[0]), PY2(a[1]), PX(b[0]), PY2(b[1]), "c3");
  if (s.n >= 3) o += ppcDrop(b[0], b[1]) + SV.text(PX(b[0]) - 6, PY2(a[1]) + 24, "gained: " + Math.round(b[0] - a[0]) + " consumer", "sm bd t3", { "text-anchor": "middle" }) + SV.text(PX(0) + 16, PY2((a[1] + b[1]) / 2), "lost: " + Math.round(a[1] - b[1]) + " capital", "sm bd t2");
  return o;
}, steps: [
  { cap: "The economy starts at <b>A</b> on its PPC.", s: { n: 0 } },
  { cap: "It decides to produce more consumer goods.", s: { n: 1 } },
  { cap: "It moves along the PPC to <b>B</b>: more consumer goods, but fewer capital goods.", s: { n: 2 } },
  { cap: "The capital goods given up are the <b>opportunity cost</b> of the extra consumer goods.", s: { n: 3 } },
] });
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Rising opportunity cost", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1");
  const ts = [1.4, 1.1, 0.8, 0.5, 0.2], ps = ts.map((t) => [80 * Math.cos(t), 90 * Math.sin(t)]);
  ps.forEach((p, i) => { if (i <= s.n) o += SV.circle(PX(p[0]), PY2(p[1]), 6, "dot1"); if (i > 0 && i <= s.n) { const q = ps[i - 1], lost = q[1] - p[1], gain = p[0] - q[0]; o += SV.line(PX(q[0]), PY2(q[1]), PX(p[0]), PY2(p[1]), "c3") + SV.text(PX((p[0] + q[0]) / 2) + 10, PY2((p[1] + q[1]) / 2) - 8, money(lost / gain, 1), "sm bd t2"); } });
  return o + SV.text(PX(55), PY2(95), "Labels: capital goods given up per extra consumer good", "sm");
}, steps: [
  { cap: "Start with almost all resources making capital goods.", s: { n: 0 } },
  { cap: "The first moves cost <b>few</b> capital goods per extra consumer good.", s: { n: 1 } },
  { cap: "The cost per extra consumer good rises.", s: { n: 2 } },
  { cap: "Higher still.", s: { n: 3 } },
  { cap: "Near the end, each extra consumer good costs <b>many</b> capital goods: <b>rising opportunity cost</b> gives the bowed-out shape.", s: { n: 4 } },
] });

/* Lab 1: opportunity cost calculator */
function labO() {
  if (!$("#oa")) return;
  const x = +$("#oa").value, y0 = 90, y = 90 * Math.sqrt(1 - (x / 80) ** 2), x1 = Math.min(80, x + 10), y1 = 90 * Math.sqrt(1 - (x1 / 80) ** 2), oc = x1 > x ? (y - y1) / (x1 - x) : 0;
  $("#oa1").textContent = money(y, 0); $("#oa2").textContent = money(y0 - y, 0); $("#oa3").textContent = money(oc, 2);
  $("#oav").textContent = `At ${x} consumer goods the economy can make ${money(y, 0)} capital goods, having given up ${money(y0 - y, 0)} compared with the maximum of 90. Making 10 more consumer goods would cost ${money(y - y1, 0)} more capital goods: ${money(oc, 2)} per extra unit. Move the slider right and the cost per unit rises.`;
  $("#labO").innerHTML = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + ppcDrop(x, y) + ppcDot(x, y, "", "dot2") + SV.circle(PX(x1), PY2(y1), 6, "dot4");
}
Lib.slider($("#g1"), { id: "oa", label: "Consumer goods produced", min: 0, max: 70, step: 5, value: 30, fmt: (v) => v, onInput: labO });
const MV = [
  { n: "More consumer goods", d: "Move down-right along the PPC", e: "Fewer capital goods produced." },
  { n: "More capital goods", d: "Move up-left along the PPC", e: "Fewer consumer goods produced." },
  { n: "Bowed-out PPC", d: "Opportunity cost rises", e: "Resources are not equally good at both." },
  { n: "Straight-line PPC", d: "Constant opportunity cost", e: "Resources equally good at both." },
  { n: "Investing today", d: "Fewer consumer goods now", e: "More capital goods; may shift the PPC later." },
];
button_table("mvBtns", "mvOut", MV, 0, (p) => `<div class="tw"><table class="t"><tr><th>What happens</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>movement along</b> a PPC or a <b>shift</b> of the PPC?", buckets: [{ label: "Movement along" }, { label: "Shift of the PPC" }], items: [
  { text: "Producing more consumer goods and fewer capital goods", b: 0 }, { text: "A government moves resources to healthcare from defence", b: 0 }, { text: "Choosing more capital goods this year", b: 0 },
  { text: "New technology raises capacity", b: 1 }, { text: "A war destroys factories", b: 1 }, { text: "Immigration raises the labour force", b: 1 },
], done: "Movement along means reallocating existing resources." });
Lib.match($("#m1"), { prompt: "Match the PPC shape to its meaning.", pairs: [
  ["Bowed outwards", "Rising opportunity cost"],
  ["Straight line", "Constant opportunity cost"],
  ["Moving along the PPC", "Reallocating resources between goods"],
  ["Gain of one good", "Loss of the other"],
  ["Opportunity cost", "Goods given up when resources are switched"],
  ["Mobility of resources", "How easily they switch between uses"],
], done: "Know the shapes." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why the opportunity cost rises along a bowed PPC</b>.", items: [
  "The economy makes more of one good",
  "Resources less suited to it must be switched",
  "Output per resource falls",
  "More of the other good is given up for each extra unit",
  "Opportunity cost rises",
], done: "The reason for the bowed shape." });
''' + calc_js([
    ("Moving from 20 consumer goods and 86 capital goods to 40 consumer goods and 76 capital goods, how many capital goods are given up?", 10, "86 − 76 = <b>10</b>.", None, None),
    ("In the same move, what is the opportunity cost per extra consumer good (capital goods)?", 0.5, "10 ÷ 20 = <b>0.5</b>.", None, None),
    ("Moving from 60 consumer goods and 60 capital goods to 80 consumer goods and 0 capital goods, what is the opportunity cost per extra consumer good (capital goods)?", 3, "60 ÷ 20 = <b>3</b>.", None, None),
]) + mcq_js("qz1", [
    ("Moving along the PPC means:", ["Using unemployed resources", "Reallocating resources between goods", "Economic growth", "A recession"], 1, "A choice."),
    ("The opportunity cost of more consumer goods is:", ["The extra consumer goods", "The capital goods given up", "Nothing", "Unemployment"], 1, "What is lost."),
    ("A bowed-out PPC shows:", ["Constant opportunity cost", "Rising opportunity cost", "Zero opportunity cost", "Unemployment"], 1, "Resources differ."),
    ("A straight-line PPC shows:", ["Rising opportunity cost", "Constant opportunity cost", "Economic growth", "A free good"], 1, "Resources are equally suitable."),
    ("Choosing more capital goods now means:", ["More consumer goods now", "Fewer consumer goods now", "No change", "A smaller PPC later"], 1, "A trade-off."),
]) + "\n" + cards_js([("Movement along a PPC", "Reallocating resources from one good to another."), ("Opportunity cost", "The next best alternative given up."), ("Rising opportunity cost", "More of one good must be given up for each extra unit of the other."), ("Constant opportunity cost", "A fixed amount given up per extra unit, shown by a straight line."), ("Trade-off", "Giving up one thing for another."), ("Mobility of resources", "How easily resources can switch between uses."), ("Capital goods", "Goods used to produce other goods."), ("Consumer goods", "Goods used by households."), ("Consumption now vs the future", "More consumption now means fewer capital goods and slower growth.")]) + "labO(); \n"
explore = '''
  <h2>Lab 1 · Opportunity cost along the curve</h2>
  <p>Move along the PPC and watch how many capital goods are given up for each extra consumer good.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Capital goods possible</small><strong id="oa1"></strong></div><div><small>Given up so far</small><strong id="oa2"></strong></div><div><small>Cost per extra consumer good</small><strong id="oa3"></strong></div></div><div class="verdict" id="oav"></div></div></div>
    <svg id="labO" viewBox="0 0 760 340" role="img" aria-label="Moving along a PPC"></svg>
  </div>

  <h2>Lab 2 · What does a move show?</h2>
  <p>Pick a situation to see what it shows on the PPC.</p>
  <div class="card"><div class="row" id="mvBtns"></div><div id="mvOut"></div></div>
'''
ex = exam(
    Q(1, "Calculate", 2, "An economy moves along its PPC from 20 consumer goods and 86 capital goods to 40 consumer goods and 76 capital goods. Calculate the opportunity cost of producing the extra consumer goods.", "Capital goods given up: 86 − 76.", "[A|86 − 76] [A|= 10 capital goods.]"),
    Q(2, "Explain", 4, "Explain the opportunity cost to Pakistan of producing more consumer goods. (Oct/Nov 2023, P22 style)", "Capital goods given up; resources switched; slower growth.",
      "[K|To produce more consumer goods Pakistan has to move resources away from capital goods.] [N|The opportunity cost is the capital goods given up, such as machinery and factories.] [N|Fewer capital goods may reduce future growth.]"),
    Q(3, "Explain", 4, "Explain why the opportunity cost rises along a bowed-out PPC.", "Resources not equally suited; less productive switching.",
      "[K|Resources are not equally suited to producing both goods.] [N|As more of one good is made, resources less suited to it must be used,] [N|so more of the other good is given up for each extra unit.]"),
    Q(4, "Analyse", 6, "Analyse, using a PPC, the opportunity cost to an economy of producing more capital goods. (May/June 2022, P22 style)", "Draw PPC; move along; fewer consumer goods; future growth benefit.",
      "[K|A PPC shows the combinations of consumer and capital goods the economy can produce.] [N|If the economy moves along the PPC to produce more capital goods, it gives up consumer goods.] [N|The opportunity cost is the consumer goods lost, so living standards now may be lower.] [N|However, more capital goods may raise productive capacity and shift the PPC outwards in future.] [E|The benefit depends on how productive the new capital is and how long it takes.]", key=True),
)
tp = tips([
    ("Opportunity cost = what is given up.", "Calculate it from the axis values."),
    ("Rising opportunity cost = bowed-out PPC.", "Straight line = constant."),
    ("Use a diagram.", "Mark two points and the move between them."),
    ("Link to the future.", "More capital goods can shift the PPC outwards."),
    ("Show working in calculations.", "Subtract the amounts."),
], cmds("Calculate", "Explain", "Analyse"))
body = page(CL("1.4.3 Movements along a PPC"), "Movements Along a PPC", "What a movement along the PPC shows about choice and opportunity cost, and why the cost rises. Syllabus 1.4.3.",
    learn=learn, watch=watch(("Moving along the PPC", "stM"), ("Rising opportunity cost", "stI")), explore=explore,
    practise=practise(("Movement or shift?", "cl1", "card"), ("Match the shape", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("A government's choice", "A country spending more on defence in wartime has less to spend on consumer goods and services.", "Moving along the PPC."),
        rw("Investing for growth", "Countries such as China have devoted a large share of output to capital goods, giving up some consumption now.", "Capital goods versus consumer goods."),
        rw("A farm's land", "A farmer who plants more wheat has less land for barley.", "A firm-level trade-off."),
        rw("Specialisation", "Resources suited to one use are moved to another and become less productive.", "Why costs rise.")),
    exam=ex, tips=tp)
write("p43", body, js, "Movements Along a PPC", "ig-ppc-movements")

# =========================================================== 1.4.4
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <b>shift of the PPC</b> changes the economy's productive capacity. An <b>outward shift</b> means <b>economic growth</b>: more of both goods can be produced. An <b>inward shift</b> means capacity falls. Shifts are caused by changes in the <b>quantity or quality of factors of production</b>, including technology.</p></div>

  <h2>Outward shifts (economic growth)</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Example</th></tr>
    <tr><td><b>More resources</b> (quantity)</td><td>Immigration, discovery of oil, new factories (investment), more people starting businesses</td></tr>
    <tr><td><b>Better resources</b> (quality)</td><td>Education and training, better healthcare, technology, new methods</td></tr>
    <tr><td><b>Supply-side policies</b></td><td>Investment in infrastructure, training programmes, reducing red tape</td></tr>
  </table></div>
  <h2>Inward shifts</h2>
  <ul>
    <li>War, natural disasters (floods, earthquakes), depletion of resources, emigration or brain drain, population decline.</li>
  </ul>
  <h2>Types of shift</h2>
  <ul>
    <li><b>Parallel outward shift</b>: capacity for <b>both</b> goods rises (general improvement in technology or labour).</li>
    <li><b>One-sided shift</b>: capacity rises for <b>only one</b> good, for example new farming technology: the curve moves out on one axis only.</li>
  </ul>
  <h2>Consequences</h2>
  <ul>
    <li><b>Economic growth</b>: higher potential output, raising incomes and living standards over time.</li>
    <li>Consumers can enjoy <b>more of both</b> goods; the opportunity cost of any given output falls.</li>
    <li>Unemployed resources are not used up: <b>growth</b> (shift) is different from <b>using idle resources</b> (a move to the PPC).</li>
    <li>An inward shift lowers output and living standards.</li>
  </ul>
  <p class="note">Capital goods today make growth tomorrow: producing more of them now can shift the PPC outwards in the future.</p>
'''
js = HEAD + COMMON + PPCJS + '''
function shiftChart(s) {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC₁", "lbl bd t1");
  if (s.g[0] !== 0 || s.g[1] !== 0) { const a2 = 80 * (1 + s.g[0] / 100), b2 = 90 * (1 + s.g[1] / 100); o += SV.path(ppcPath(a2, b2), s.g[0] < 0 || s.g[1] < 0 ? "c4" : "c2") + SV.text(PX(a2 * 0.8) + 6, PY2(b2 * 0.65) - 6, "PPC₂", "lbl bd " + (s.g[0] < 0 || s.g[1] < 0 ? "t4" : "t2")); }
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Shifts of the PPC", base: { g: [0, 0] }, draw: shiftChart, steps: [
  { cap: "The economy's PPC today.", s: { g: [0, 0] } },
  { cap: "New technology and a better-trained workforce raise capacity for <b>both goods</b>: PPC shifts <b>outwards</b>. This is <b>economic growth</b>.", s: { g: [25, 25] } },
  { cap: "A war or natural disaster destroys resources: PPC shifts <b>inwards</b>.", s: { g: [-25, -25] } },
  { cap: "New farming technology raises capacity for <b>only one good</b>: a one-sided shift.", s: { g: [0, 30] } },
] });
const GR = ["Investment in capital and training today", "Capital and labour improve in quantity and quality", "Productive capacity rises", "The PPC shifts outwards", "Economic growth: more of both goods can be produced"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "From investment to growth", base: { n: 0 }, draw: mkChain(GR, "--good"), steps: chainSteps(["<b>Investment</b> in capital and training today.", "Capital and labour improve in <b>quantity and quality</b>.", "<b>Productive capacity</b> rises.", "The <b>PPC shifts outwards</b>.", "<b>Economic growth</b>: more of both goods can be produced."]) });

/* Lab 1 */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const gx = +$("#sa").value, gy = +$("#sb").value, a2 = 80 * (1 + gx / 100), b2 = 90 * (1 + gy / 100);
  $("#sa1").textContent = money(a2, 0); $("#sa2").textContent = money(b2, 0); $("#sa3").textContent = gx === 0 && gy === 0 ? "No change" : gx >= 0 && gy >= 0 ? (gx === gy ? "Parallel outward" : "One-sided / uneven") : "Inward or mixed";
  $("#sav").textContent = `Maximum consumer goods ${money(a2, 0)} (was 80) and maximum capital goods ${money(b2, 0)} (was 90). ${gx > 0 && gy > 0 ? "Capacity rises for both goods: economic growth." : gx < 0 || gy < 0 ? "Capacity falls for at least one good: the economy has lost resources or technology." : "Capacity rises for one good only."}`;
  $("#labS").innerHTML = shiftChart({ g: [gx, gy] });
}
Lib.slider($("#g1"), { id: "sa", label: "Change in capacity for consumer goods", min: -30, max: 40, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Change in capacity for capital goods", min: -30, max: 40, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labS });
const CS = [
  { n: "New technology", d: "Outward shift", e: "Higher productivity." },
  { n: "Immigration of workers", d: "Outward shift", e: "More labour." },
  { n: "Education and training", d: "Outward shift", e: "Better-quality labour." },
  { n: "Discovery of oil", d: "Outward shift", e: "More land." },
  { n: "A major earthquake", d: "Inward shift", e: "Capital and lives lost." },
  { n: "War", d: "Inward shift", e: "Destroyed capacity." },
  { n: "Brain drain", d: "Inward shift", e: "Skills lost." },
  { n: "Unemployment falls", d: "Move to the PPC, not a shift", e: "Idle resources used." },
];
button_table("csBtns", "csOut", CS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the PPC</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Would each shift the PPC <b>outwards</b>, <b>inwards</b>, or just <b>move the economy to the PPC</b>?", buckets: [{ label: "Outwards" }, { label: "Inwards" }, { label: "Move to the PPC" }], items: [
  { text: "New technology", b: 0 }, { text: "More investment in factories", b: 0 }, { text: "Better education", b: 0 },
  { text: "A hurricane destroys factories", b: 1 }, { text: "Skilled workers emigrate", b: 1 },
  { text: "Unemployed workers find jobs", b: 2 }, { text: "Idle machines are used", b: 2 },
], done: "A shift needs a change in resources; a move to the PPC does not." });
Lib.classify($("#cl2"), { prompt: "Is each cause a change in the <b>quantity</b> or <b>quality</b> of resources?", buckets: [{ label: "Quantity" }, { label: "Quality" }], items: [
  { text: "Immigration", b: 0 }, { text: "Oil discovery", b: 0 }, { text: "New factories", b: 0 },
  { text: "Training", b: 1 }, { text: "Better technology", b: 1 }, { text: "Better health", b: 1 },
], done: "More or better resources shift the PPC." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect on the PPC.", pairs: [
  ["New technology", "Outward shift"],
  ["War", "Inward shift"],
  ["Falling unemployment", "Move to the PPC"],
  ["Immigration", "Outward shift (more labour)"],
  ["Depletion of resources", "Inward shift"],
  ["Farming technology only", "One-sided shift"],
], done: "Know the causes." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how education leads to economic growth</b>.", items: [
  "The government invests in education",
  "Workers become more skilled",
  "Productivity rises",
  "Productive capacity increases",
  "The PPC shifts outwards: economic growth",
], done: "Quality leads to growth." });
''' + calc_js([
    ("A country's maximum capital goods rise from 90 to 108 after a shift. What is the percentage increase?", 20, "18 ÷ 90 × 100 = <b>20%</b>.", None, None),
    ("A country's potential output is 200 and grows by 4%. What is the new potential output?", 208, "200 × 1.04 = <b>208</b>.", None, None),
]) + mcq_js("qz1", [
    ("An outward shift of the PPC shows:", ["A recession", "Economic growth", "Unemployment", "Inflation"], 1, "Capacity rises."),
    ("Which could shift the PPC outwards?", ["War", "New technology", "Brain drain", "A flood"], 1, "Raises productivity."),
    ("Which shifts the PPC inwards?", ["Education", "A natural disaster", "Investment", "Immigration of workers"], 1, "Loss of resources."),
    ("A fall in unemployment is shown by:", ["An outward shift", "An inward shift", "A move towards the PPC", "A new axis"], 2, "Idle resources used."),
    ("A shift of the PPC is caused by changes in:", ["Prices", "Quantity or quality of resources", "Demand", "Taxes only"], 1, "Resources and technology."),
]) + "\n" + cards_js([("Outward shift", "An increase in productive capacity: economic growth."), ("Inward shift", "A fall in productive capacity."), ("Economic growth", "An increase in an economy's productive capacity or real GDP."), ("Technology", "Knowledge and methods that raise productivity."), ("Investment", "Spending on capital goods."), ("Productive capacity", "The maximum output an economy can produce."), ("Brain drain", "Skilled workers emigrating."), ("Depletion", "Using up natural resources."), ("One-sided shift", "A shift where capacity rises for only one good.")]) + "labS(); \n"
explore = '''
  <h2>Lab 1 · Shift the PPC</h2>
  <p>Change the capacity for each good and see the new PPC.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Max consumer goods</small><strong id="sa1"></strong></div><div><small>Max capital goods</small><strong id="sa2"></strong></div><div><small>Type of shift</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 340" role="img" aria-label="A shift of the PPC"></svg>
  </div>

  <h2>Lab 2 · Causes of shifts</h2>
  <p>Pick a cause to see its effect on the PPC.</p>
  <div class="card"><div class="row" id="csBtns"></div><div id="csOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two causes of an outward shift of a PPC.", "Technology, education, immigration, investment.",
      "[K|New technology could raise productivity,] [N|so more of both goods can be produced with the same resources.] [K|Immigration increases the labour force,] [N|so the economy has more resources and can produce more.]"),
    Q(2, "Explain", 4, "Explain what an inward shift of a PPC might show. (Feb/Mar 2024, P22 style)", "Loss of resources; war, disaster, depletion; lower capacity.",
      "[K|An inward shift shows a fall in the economy's productive capacity.] [N|It could be caused by war or a natural disaster that destroys factories, or by workers emigrating.] [N|The economy can now produce less of both goods.]"),
    Q(3, "Analyse", 6, "Analyse how economic growth can be shown on a PPC. (Oct/Nov 2021, P22 style)", "Outward shift; causes; effect on output and opportunity cost.",
      "[K|Economic growth is shown by an outward shift of the PPC.] [N|It could be caused by more or better-quality resources, such as new technology or training.] [N|The economy can then produce more of both goods, so living standards could rise.] [E|Growth in capacity only raises output if resources are fully used and demand is sufficient.]", key=True),
    Q(4, "Analyse", 6, "Analyse how advances in technology could affect a country's PPC.", "Productivity; outward shift; possibly one-sided; growth.",
      "[K|New technology can raise productivity and output per worker.] [N|This shifts the PPC outwards, so more goods can be produced with the same resources.] [N|If the technology benefits only one good, such as farming, the curve may shift out on one axis only.] [N|The country can then enjoy more of both goods in future.] [E|The gains depend on how quickly the technology spreads and on the cost of developing it.]", key=True),
)
tp = tips([
    ("A shift needs a change in resources.", "A move to the PPC does not."),
    ("Name the cause and the factor.", "Quantity or quality of land, labour, capital, enterprise."),
    ("Outward shift = economic growth.", "Say it."),
    ("Draw both curves and label PPC₁ and PPC₂.", "Show the direction."),
    ("Evaluate: do the resources get used?", "Capacity is not the same as output."),
], cmds("Explain", "Analyse"))
body = page(CL("1.4.4 Shifts of a PPC"), "Shifts of a PPC", "Causes and consequences of outward and inward shifts of the production possibility curve and what they show about growth. Syllabus 1.4.4.",
    learn=learn, watch=watch(("Shifts of the PPC", "stS"), ("From investment to growth", "stG")), explore=explore,
    practise=practise(("Outwards, inwards or move to?", "cl1", "card"), ("Quantity or quality?", "cl2", "card"), ("Match the cause", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("The Green Revolution", "New seeds and farming methods in the mid-20th century raised food output in many countries, shifting their PPC outwards.", "Technology as a cause of growth."),
        rw("Oil discoveries", "New oil and gas finds add to a country's resources and capacity.", "More land (natural resources)."),
        rw("Natural disasters", "Earthquakes and floods can destroy factories and infrastructure and reduce capacity for some years.", "An inward shift."),
        rw("Education in South Korea", "Heavy investment in education raised productivity and supported fast growth.", "Quality of labour.")),
    exam=ex, tips=tp)
write("p44", body, js, "Shifts of a PPC", "ig-ppc-shifts")
