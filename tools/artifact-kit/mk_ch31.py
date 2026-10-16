"""Builds the four ch31 part pages (ic1..ic4) from slices of ic.* plus new content. Run: python3 tools/artifact-kit/mk_ch31.py"""
from splitter import Src, page, write, key
S = Src("ic")
HEAD = S.j_((1, 51))
EY = "A Level Economics · 9708 · Syllabus 7.2 · Part {} of 4"
NOTE = '<p class="note">Examples are explained in general terms. The numbers are simple on purpose, to show the idea.</p>\n'
def L(*r): return S.j_(*[(a, b) if isinstance(a, int) else a for a, b in r])
def MCQ(old=(), new=""): return 'Lib.quiz($("#qz2"), { qs: [\n' + S.j_(*[(i, i) for i in old]) + new + '] });\n'
def QZ(old=(), extra=""): return 'Lib.quiz($("#qz1"), { qs: [\n' + S.j_(*[(i, i) for i in old]) + extra + '] });\n'
def CARDS(old=(), extra=""): return 'Lib.cards($("#fc1"), { cards: [\n' + S.j_(*[(i, i) for i in old]) + extra + '] });\n'
def CALC(old=(), extra=""): return 'Lib.calc($("#c1"), { qs: [\n' + S.j_(*[(i, i) for i in old]) + extra + '] });\n'
def TIPS(lis, new, rows): return '<h2>Top tips</h2>\n  <ul class="tips">\n' + (S.b(*lis) if lis else "") + new + '  </ul>\n  <h2>Sentences you can use</h2>\n  <div class="tw"><table class="t">\n    <tr><th>You want to say</th><th>Use this sentence</th></tr>\n' + S.b(*rows) + '  </table></div>\n'
def CMD(*r): return '<h2>Command words</h2>\n  <div class="tw"><table class="t">\n    <tr><th>Command word</th><th>What it asks for</th></tr>\n' + "".join(f"    <tr><td>{a}</td><td>{b}</td></tr>\n" for a, b in r) + '  </table></div>\n'
USE = ("Use ... analysis", "The method must appear: draw and explain the diagram.")
EXP = ("Explain", "Give reasons, with a clear chain of cause and effect.")
DIS = ("Distinguish", "Say clearly how two ideas differ.")
DISC = ("Discuss", "Arguments on both sides, then a judgement.")
EVA = ("Evaluate / Assess", "Weigh the arguments and reach a supported conclusion.")
KEYL = '<div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>\n'
KEYS = '<div class="key"><span class="k"><i></i>K</span><span class="a"><i></i>A</span><span class="n"><i></i>N</span><span class="e"><i></i>E</span></div>\n'
FC = '<h2>Flashcards</h2><div id="fc1"></div>\n'
PP = '<h2>{}</h2>\n  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>\n  <div id="qz2"></div>\n'
EXAMTAIL = lambda lab: PP.format(lab)

# ------------------------------------------------------------------ 31.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>An <b class="kw">indifference curve</b> joins all the combinations of two goods that give a consumer the <b>same satisfaction</b>. It slopes down, is convex to the origin because the <b>marginal rate of substitution</b> diminishes, never crosses another curve, and a curve further from the origin means more satisfaction. A <b>budget line</b> shows all the combinations the consumer can afford with a given income and prices; its slope is <b>Px ÷ Py</b>. A price change pivots the line around one intercept, while an income change shifts it in parallel. Together the two tools set up the consumer's choice in parts 2 to 4.</p></div>
''' + S.b((25, 38), (40, 50))
watch = '''
  <h2>1 · Building the diagram</h2>
  <p>An indifference curve, an indifference map, a budget line and the consumer's affordable choices. Press Play, or click the steps.</p><div id="stI"></div>
'''
explore = '''
  <h2>Lab 1 · Draw the budget line</h2>
  <p>Set income and the two prices. The line joins the most of X you can buy and the most of Y. The shaded triangle is everything you can afford.</p>
  <div class="card"><div class="grid2"><div><div id="g8"></div><div id="g9"></div><div id="g10"></div>
    <div class="readout"><div><small>Maximum X</small><strong id="b1"></strong></div><div><small>Maximum Y</small><strong id="b2"></strong></div><div><small>Slope (Px ÷ Py)</small><strong id="b3"></strong></div><div><small>Can you afford (20 X, 20 Y)?</small><strong id="b4"></strong></div></div>
    <div class="verdict" id="bv"></div></div>
    <div><svg id="labP" viewBox="0 0 420 330" role="img" aria-label="Budget line with the affordable region shaded and a marked bundle"></svg></div></div></div>

  <h2>Lab 2 · Which bundle is better?</h2>
  <p>Pick a bundle of X and Y. The curve through it shows every bundle that is just as good. Compare it with the reference bundle of 20 X and 20 Y (satisfaction 20).</p>
  <div class="card"><div class="grid2"><div><div id="g11"></div><div id="g12"></div>
    <div class="readout"><div><small>Satisfaction (√xy)</small><strong id="c1r"></strong></div><div><small>Compared with the reference</small><strong id="c2r"></strong></div><div><small>MRS (y ÷ x)</small><strong id="c3r"></strong></div></div>
    <div class="verdict" id="cv"></div></div>
    <div><svg id="labQ" viewBox="0 0 420 330" role="img" aria-label="Indifference curve through the chosen bundle and through the reference bundle"></svg></div></div></div>
'''
practise = S.b((133, 134)) + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((155, 155)) + '''  <div class="rw"><h3>Cinema or a meal out</h3><p>A student with a fixed monthly entertainment budget can go to the cinema more and eat out less, or the reverse. Any pair of choices that feels equally good to the student lies on the same indifference curve, and the cost of the choices sets the budget line.</p><div class="use"><b>Exam use:</b> a simple way to explain an indifference curve and a budget line with two goods.</div></div>
  <div class="rw"><h3>Choosing a phone plan</h3><p>Data and calls cost money from the same budget. A higher income allows more of both (a parallel shift out), while a price rise for data pivots the budget line inwards on the data axis.</p><div class="use"><b>Exam use:</b> a change in price versus a change in income.</div></div>
'''
exam = '''
  <h2>Past paper questions on indifference curves and budget lines</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The June 2020 papers were published but not sat, so they are marked "not sat". Below are the 12 mark question on indifference curves and budget lines and ten Paper 3 multiple choice questions on their properties. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay part, 12 marks</td><td>1</td><td>Feb/March 2022 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>10 shown below</td><td>2021 to 2025</td></tr>
  </table></div>
  <h2>A · A 12 mark question</h2>
''' + KEYL + S.b((229, 232)) + '''
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain what is shown by an indifference curve and by a budget line.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define each curve in a sentence, state two properties of an indifference curve, say what sets the position and slope of the budget line, and say what a price change does.</div>
''' + KEYS + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">An indifference curve shows all the combinations of two goods that give a consumer the same level of satisfaction. Curves further from the origin show higher satisfaction. A budget line shows all the combinations of two goods that a consumer can afford given income and the prices of the goods.</span></p>
    <p><span class="mk n" data-t="N">An indifference curve slopes downward, because getting more of one good means giving up some of the other to stay equally satisfied, and is convex to the origin, because the marginal rate of substitution is likely to diminish as the consumer has more of one good.</span> <span class="mk a" data-t="A">For example, a student may be equally happy with 10 cinema visits and 40 meals out, or 20 visits and 20 meals.</span></p>
    <p><span class="mk n" data-t="N">The budget line is straight, with intercepts at income divided by each price, and its slope is the ratio of the prices. A rise in income shifts it outwards in parallel, while a fall in the price of one good pivots it outwards around the other good's intercept.</span> <span class="mk e" data-t="E">Together the two show what the consumer would like and what the consumer can afford, so the best choice is the highest curve that the budget line allows.</span></p></div>
  </details>
''' + EXAMTAIL("C · Multiple choice questions (Paper 3)")
tips = TIPS([(269, 270)], '''    <li><b>Know the four properties of an indifference curve:</b> downward sloping, convex (diminishing MRS), never crossing, higher curve means more satisfaction.</li>
''', [(282, 282)]) + CMD(USE, EXP, DIS) + FC
js = HEAD + L((52, 60)) + '''
/* ---------- Watch: building the diagram ---------- */
(function () {
  const F = FR(60, 300, 600, 260, 60, 60), M = NORM.M;
  function draw(s) {
    let o = frameAxes(F, "Good X", "Good Y");
    if (s.ic > 0) o += icLine(NORM, F, 20, "c1", op(s.ic)) + SV.text(F.X(52), F.Y(400 / 52) - 12, "IC", "lbl bd t1", op(s.ic));
    if (s.pts > 0) [[10, 40, "a"], [20, 20, "b"], [40, 10, "c"]].forEach(([x, y, l]) => { o += SV.circle(F.X(x), F.Y(y), 6, "dot1", op(s.pts)) + SV.text(F.X(x) + 14, F.Y(y) - 8, l, "lbl bd t1", op(s.pts)); });
    if (s.map > 0) o += icLine(NORM, F, 28, "c4", op(s.map)) + icLine(NORM, F, 12, "c3", op(s.map)) + SV.text(F.X(52), F.Y(784 / 52) - 12, "higher", "sm bd t4", op(s.map)) + SV.text(F.X(40), F.Y(144 / 40) - 12, "lower", "sm bd t3", op(s.map));
    if (s.aff > 0) o += SV.poly([[F.X(0), F.Y(0)], [F.X(30), F.Y(0)], [F.X(0), F.Y(60)]], "f1", { opacity: 0.18 * s.aff });
    if (s.bl > 0) o += bline(F, 4, 2, M, "gr", { "stroke-width": 3, ...op(s.bl) }) + SV.text(F.X(30), F.Y(0) - 8, "30", "sm bd", { "text-anchor": "middle", ...op(s.bl) }) + SV.text(F.X(0) + 8, F.Y(60) + 4, "60", "sm bd", op(s.bl)) + SV.text(F.X(1.5), F.Y(22), "budget line", "lbl bd", { "text-anchor": "start", ...op(s.bl) });
    if (s.eq > 0) o += icLine(NORM, F, Math.sqrt(450), "c2", op(s.eq)) + SV.circle(F.X(15), F.Y(30), 7, "dot2", op(s.eq)) + SV.text(F.X(15) + 16, F.Y(30) - 10, "best choice", "lbl bd t2", op(s.eq));
    return o;
  }
  Lib.stepper($("#stI"), { w: 740, h: 380, label: "Building an indifference curve, an indifference map and a budget line", base: { ic: 0, pts: 0, map: 0, aff: 0, bl: 0, eq: 0 }, draw, tween: 800, dwell: 5600, steps: [
    { cap: "<b>An indifference curve.</b> Points a, b and c are different bundles of X and Y that give the <b>same satisfaction</b>: 10 X with 40 Y, 20 with 20, or 40 with 10. The consumer is indifferent between them.", s: { ic: 1, pts: 1 } },
    { cap: "<b>The curve slopes down and bends in.</b> To keep satisfaction the same, more X means less Y. It is <b>convex</b> because the more X the consumer has, the less Y they will give up for one more X (diminishing MRS).", s: { ic: 1, pts: 1 } },
    { cap: "<b>An indifference map.</b> A curve further from the origin has more of both goods, so it gives <b>more satisfaction</b>. Curves never cross.", s: { ic: 1, pts: 0.4, map: 1 } },
    { cap: "<b>A budget line.</b> With income $120, Px = $4 and Py = $2 the consumer can buy at most 30 X or 60 Y. The line joins these points and the shaded triangle is everything <b>affordable</b>. Its slope is Px ÷ Py = 2.", s: { ic: 0.4, map: 0.4, aff: 1, bl: 1 } },
    { cap: "<b>Putting them together.</b> The best choice is on the <b>highest indifference curve the budget line allows</b>, where the line just touches the curve: 15 X and 30 Y. Part 2 explains why.", s: { ic: 0.3, map: 0.3, aff: 1, bl: 1, eq: 1 } },
  ] });
})();

/* ---------- Lab 1: budget line ---------- */
function labBL() {
  if (!$("#bm") || !$("#bx") || !$("#by")) return;
  const M = +$("#bm").value, px = +$("#bx").value, py = +$("#by").value, mx = M / px, my = M / py, cost = 20 * px + 20 * py, ok = cost <= M, F = FR(50, 290, 340, 250, 80, 80);
  $("#b1").textContent = Lib.fmtN(mx, 1); $("#b2").textContent = Lib.fmtN(my, 1); $("#b3").textContent = Lib.fmtN(px / py, 2); $("#b4").textContent = ok ? "Yes ($" + cost + ")" : "No ($" + cost + ")";
  $("#bv").textContent = `With $${M} the consumer can buy at most ${Lib.fmtN(mx, 1)} X or ${Lib.fmtN(my, 1)} Y. The slope is Px ÷ Py = ${Lib.fmtN(px / py, 2)}: giving up 1 X frees enough money for ${Lib.fmtN(px / py, 2)} Y. The bundle (20, 20) costs $${cost}, so it is ${ok ? "inside the budget" : "beyond the budget line"}.`;
  const x2 = Math.min(mx, 80), y1 = Math.min(my, 80);
  let o = frameAxes(F, "Good X", "Good Y") + SV.poly([[F.X(0), F.Y(0)], [F.X(Math.min(mx, 80)), F.Y(0)], [F.X(0), F.Y(Math.min(my, 80))]], "f1", { opacity: 0.18 }) + bline(F, px, py, M, "c3", { "stroke-width": 3 }) + SV.circle(F.X(20), F.Y(20), 7, ok ? "dot3" : "dot2") + SV.text(F.X(20) + 12, F.Y(20) - 10, "(20, 20)", "lbl bd", {});
  $("#labP").innerHTML = o;
}
Lib.slider($("#g8"), { id: "bm", label: "Income ($): ", min: 40, max: 160, step: 10, value: 120, fmt: (v) => v, onInput: labBL });
Lib.slider($("#g9"), { id: "bx", label: "Price of X ($): ", min: 2, max: 8, step: 1, value: 4, fmt: (v) => v, onInput: labBL });
Lib.slider($("#g10"), { id: "by", label: "Price of Y ($): ", min: 2, max: 8, step: 1, value: 2, fmt: (v) => v, onInput: labBL });

/* ---------- Lab 2: compare bundles ---------- */
function labBun() {
  if (!$("#qx") || !$("#qy")) return;
  const x = +$("#qx").value, y = +$("#qy").value, u = Math.sqrt(x * y), F = FR(50, 290, 340, 250, 60, 60), d = u - 20;
  $("#c1r").textContent = Lib.fmtN(u, 1); $("#c2r").textContent = Math.abs(d) < 0.05 ? "Same" : d > 0 ? "Better" : "Worse"; $("#c3r").textContent = Lib.fmtN(y / x, 2);
  $("#cv").textContent = Math.abs(d) < 0.05 ? "This bundle lies on the same indifference curve as the reference: the consumer is indifferent."
    : d > 0 ? `This bundle is on a higher indifference curve (${Lib.fmtN(u, 1)} against 20): the consumer prefers it. More of both goods always raises satisfaction.`
    : `This bundle is on a lower curve (${Lib.fmtN(u, 1)} against 20): the consumer likes it less. The MRS here is ${Lib.fmtN(y / x, 2)}: the consumer would give up ${Lib.fmtN(y / x, 2)} Y for one more X.`;
  $("#labQ").innerHTML = frameAxes(F, "Good X", "Good Y") + icLine(NORM, F, 20, "c3", { "stroke-dasharray": "6 5" }) + SV.text(F.X(58), F.Y(400 / 58) - 12, "reference curve", "sm bd t3", { "text-anchor": "end" }) + icLine(NORM, F, u, "c1") + SV.circle(F.X(20), F.Y(20), 5, "dot3") + SV.circle(F.X(x), F.Y(y), 7, "dot1") + SV.text(F.X(x) + 12, F.Y(y) - 10, "your bundle", "lbl bd t1");
}
Lib.slider($("#g11"), { id: "qx", label: "Units of X: ", min: 5, max: 50, step: 1, value: 30, fmt: (v) => v, onInput: labBun });
Lib.slider($("#g12"), { id: "qy", label: "Units of Y: ", min: 5, max: 50, step: 1, value: 20, fmt: (v) => v, onInput: labBun });

/* ---------- Practise ---------- */
''' + L((152, 160)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Indifference curve", "A curve joining combinations of two goods that give the same satisfaction"],
  ["Indifference map", "A set of indifference curves; further from the origin means higher satisfaction"],
  ["Marginal rate of substitution", "How much of one good is given up for one more unit of the other, the slope of the curve"],
  ["Diminishing MRS", "The reason indifference curves are convex to the origin"],
  ["Budget line", "All combinations of two goods affordable with a given income and prices"],
  ["Slope of the budget line", "Px ÷ Py"],
  ["Affordable region", "The area on and below the budget line"],
], done: "Seven words for the building blocks." });
''' + CALC((189, 190, 191), extra='''  { q: "Income is $90, Px = $3 and Py = $6. What is the maximum quantity of X?", a: 30, sol: "90 ÷ 3 = <b>30</b>." },
  { q: "An indifference curve passes through 10 X with 40 Y and 20 X with 20 Y. How many units of Y does the consumer give up, on average, for each of the extra 10 units of X?", a: 2, sol: "Y falls by 20 over 10 extra units of X: <b>2 Y for each X</b>. This is the average MRS." },
  { q: "Income rises from $120 to $150 with prices unchanged (Px = $4, Py = $2). What is the new maximum quantity of Y?", a: 75, sol: "150 ÷ 2 = <b>75</b>. The line shifts out in parallel." },
''') + QZ((198, 200), extra='''  { q: "Indifference curves never cross because:", opts: ["income is constant", "a crossing point would be on two different levels of satisfaction", "prices are constant", "MRS is zero"], a: 1, why: "If they crossed, one bundle would give two different levels of satisfaction." },
  { q: "The slope of the budget line is:", opts: ["Py ÷ Px", "Px ÷ Py", "income ÷ price", "MUx ÷ MUy"], a: 1, why: "It shows how many units of Y must be given up for one more X." },
''') + CARDS((206, 207, 208, 209, 210, 211)) + MCQ((225, 228, 229, 230, 231, 234, 235, 236), '''  { q: "[Oct/Nov 2021 · 32 · Q4] A consumer currently consumes 10 units of good X and 10 units of good Y at point Z on an indifference curve. The consumer's marginal utilities from consuming both good X and good Y are positive. Which combination of good X and good Y could be on the same indifference curve as point Z?", opts: ["9 units of X and 11 of Y", "10 units of X and 11 of Y", "11 units of X and 10 of Y", "12 units of X and 12 of Y"], a: 0, why: "On the same curve, less of one good must be offset by more of the other. B, C and D have at least as much of both goods, so they give more satisfaction." },
  { q: "[May/June 2022 · 32 · Q5] What does a budget line show?", opts: ["the behaviour of a utility-maximising consumer", "the difference between an individual's consumption and saving", "the monetary value of the disposable income of a consumer", "the maximum combinations of two products that a consumer can buy with a given level of income"], a: 3, why: "The budget line shows the affordable combinations of two goods." },
''')
write("ic1", page(EY.format(1), "Indifference Curves and Budget Lines: the Building Blocks",
  "What an indifference curve and an indifference map show, why the curves slope down and bend in, how a budget line is drawn and what shifts or pivots it. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Indifference Curves and Budget Lines: the Building Blocks", "indifference-curves-budget-lines-basics")

# ------------------------------------------------------------------ 31.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The consumer maximises satisfaction by choosing the bundle on the <b>highest indifference curve the budget line allows</b>. That is where the budget line is a <b>tangent</b> to the curve, so the slope of the curve (the <b>MRS</b>) equals the slope of the line (<b>Px ÷ Py</b>). Change the price of X and the budget line pivots to a new tangency; plotting each price against the quantity of X bought gives the <b>individual demand curve</b>, and a change in income shifts the line in parallel. The tool therefore explains demand without measuring utility in numbers.</p></div>
''' + S.b((51, 55)).replace("3 · Consumer", "1 · Consumer") + '''
  <h2>2 · Equilibrium in numbers</h2>
  <p>Income $120, Px = $4, Py = $2. With the preferences used on this page (equal weight on both goods) the consumer spends half of income on each good: 15 X and 30 Y. The MRS there is 30 ÷ 15 = 2, equal to Px ÷ Py = 4 ÷ 2 = 2. At any other point on the budget line the MRS differs from 2, and a higher curve is not affordable.</p>
''' + S.b((70, 77)).replace("5 · Deriving", "3 · Deriving") + '''
  <div class="tw"><table class="t">
    <tr><th>Price of X</th><th>Units of X bought</th><th>What the diagram does</th></tr>
    <tr><td>$6</td><td>10</td><td>Steep budget line, low curve</td></tr>
    <tr><td>$4</td><td>15</td><td>Line pivots out around the Y intercept</td></tr>
    <tr><td>$3</td><td>20</td><td>Pivots again</td></tr>
    <tr><td>$2</td><td>30</td><td>Highest curve reached</td></tr>
  </table></div>
  <p>Plot the four points (quantity, price) and join them: that is the demand curve for X. It slopes downward for a normal good.</p>
  <div class="tip"><b class="h">Income changes</b>A rise in income shifts the budget line out in parallel, and the new tangency shows how much more of each good is bought. Joining those points gives the income consumption curve, the basis for telling normal goods from inferior goods (part 4).</div>
'''
watch = S.b((95, 97))
explore = S.b((102, 107)) + '''
  <h2>Lab 2 · More income</h2>
  <p>Prices stay at Px = $4 and Py = $2. Raise income and watch the budget line shift out in parallel and the tangency move to a higher curve. For these preferences both goods are normal.</p>
  <div class="card"><div class="grid2"><div><div id="g13"></div>
    <div class="readout"><div><small>Bundle chosen</small><strong id="i1"></strong></div><div><small>Satisfaction</small><strong id="i2"></strong></div><div><small>Slope of the line</small><strong id="i3"></strong></div></div>
    <div class="verdict" id="iv"></div></div>
    <div><svg id="labR" viewBox="0 0 420 330" role="img" aria-label="Budget lines shifting outward with income and the tangency path"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>2 · Put the equilibrium argument in order</h2><div id="o1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((155, 155)) + '''  <div class="rw"><h3>A pay rise</h3><p>When wages rise and prices stay the same, the budget line shifts out. A person who buys more of most goods is treating them as normal goods. The new tangency is on a higher indifference curve.</p><div class="use"><b>Exam use:</b> an income change: parallel shift, new equilibrium, higher curve.</div></div>
  <div class="rw"><h3>Seasonal fruit prices</h3><p>When strawberries are cheap in season, shoppers buy more of them. Each price gives a new tangency, and joining the price and quantity pairs traces the demand curve.</p><div class="use"><b>Exam use:</b> deriving an individual demand curve from a series of budget line pivots.</div></div>
'''
exam = '''
  <h2>Past paper questions on equilibrium and demand curves</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the questions that ask for the consumer's equilibrium and the derivation of the demand curve using indifference curves, and a Paper 3 multiple choice question. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>Oct/Nov 2023 (42)</td></tr>
    <tr><td>Essay part, 12 marks</td><td>2</td><td>May/June 2021 (42); May/June 2020 (not sat, 41, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>1 shown below</td><td>2022</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((200, 206), (244, 244), (258, 258)) + '''
  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(271, 271), (275, 275)], '''    <li><b>Equilibrium is a tangency:</b> say MRS = Px ÷ Py and draw the budget line just touching the highest curve it can reach.</li>
''', [(283, 283)]) + CMD(USE, EXP, DISC) + FC
js = HEAD + L((84, 120)) + '''
/* ---------- Lab 2: more income ---------- */
function labInc() {
  if (!$("#im")) return;
  const M = +$("#im").value, x = M / 8, y = M / 4, u = Math.sqrt(x * y), F = FR(50, 290, 340, 250, 80, 80);
  $("#i1").textContent = `${Lib.fmtN(x, 1)} X, ${Lib.fmtN(y, 1)} Y`; $("#i2").textContent = Lib.fmtN(u, 1); $("#i3").textContent = "2.00";
  $("#iv").textContent = `With income $${M} the consumer buys ${Lib.fmtN(x, 1)} X and ${Lib.fmtN(y, 1)} Y. Because prices have not changed, the slope stays at 2: the line shifts in parallel. Both goods rise with income, so both are normal goods here.`;
  let o = frameAxes(F, "Good X", "Good Y");
  [40, 80, 120, 160].forEach((m) => { const on = m === M; o += bline(F, 4, 2, m, on ? "c3" : "gr", on ? { "stroke-width": 3 } : { opacity: 0.35 }); });
  const path = []; for (let m = 40; m <= 160; m += 10) path.push([F.X(m / 8), F.Y(m / 4)]);
  o += SV.path(Lib.ptsPath(path), "c4", { "stroke-dasharray": "5 4", opacity: 0.8 }) + icLine(NORM, F, u, "c1") + SV.circle(F.X(x), F.Y(y), 7, "dot2") + SV.text(F.X(x) + 12, F.Y(y) - 10, "equilibrium", "lbl bd t2");
  $("#labR").innerHTML = o;
}
Lib.slider($("#g13"), { id: "im", label: "Income ($): ", min: 40, max: 160, step: 10, value: 80, fmt: (v) => v, onInput: labInc });

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Consumer equilibrium", "The bundle on the highest indifference curve the budget line allows"],
  ["Tangent", "A line that touches a curve at one point without crossing it"],
  ["MRS = Px ÷ Py", "The condition at the consumer's equilibrium"],
  ["Price consumption curve", "The path of equilibria as the price of one good changes"],
  ["Individual demand curve", "Price against quantity bought at each equilibrium"],
  ["Income consumption curve", "The path of equilibria as income changes"],
], done: "Six words for equilibrium and demand." });
Lib.order($("#o1"), { prompt: "Put the derivation of a demand curve with indifference curves in order.", items: [
  "Draw an indifference map and a budget line, and mark the tangency as equilibrium A",
  "Lower the price of X so the budget line pivots outwards around the Y-axis intercept",
  "Find the new tangency on a higher indifference curve: equilibrium B",
  "Note the quantity of X bought at each price",
  "Plot each price against its quantity on a second diagram",
  "Join the points to give the individual demand curve, which slopes down for a normal good",
], done: "Repeat for several prices, then add across consumers for the market demand curve." });
''' + CALC((192, 195), extra='''  { q: "Income is $120, Px = $4 and Py = $2. The consumer spends half of income on each good. How many units of X are bought?", a: 15, sol: "$60 ÷ $4 = <b>15</b>." },
  { q: "How many units of Y are bought?", a: 30, sol: "$60 ÷ $2 = <b>30</b>." },
  { q: "Using the same rule, the price of X falls to $2. How many units of X are now bought?", a: 30, sol: "$60 ÷ $2 = <b>30</b>. The demand curve gains a second point: (30, $2)." },
  { q: "Income rises from $120 to $160 with prices unchanged. How many units of X are bought (same half-and-half rule)?", a: 20, sol: "$80 ÷ $4 = <b>20</b>: a normal good." },
''') + QZ((199,), extra='''  { q: "At the consumer's equilibrium, the MRS equals:", opts: ["Py ÷ Px", "Px ÷ Py", "income", "1"], a: 1, why: "The curve and the budget line have the same slope at a tangent." },
  { q: "A fall in the price of X will pivot the budget line:", opts: ["inwards around the X intercept", "outwards around the Y intercept", "outwards in parallel", "inwards in parallel"], a: 1, why: "The Y intercept (income ÷ Py) is unchanged; the X intercept moves out." },
  { q: "Joining the equilibria found at different prices of X gives:", opts: ["the budget line", "the indifference map", "the individual demand curve (via price and quantity)", "total utility"], a: 2, why: "Price against the quantity bought forms the demand curve." },
''') + CARDS((212, 220), extra='''  ["Income consumption curve", "The path of equilibria as income changes, prices fixed."],
  ["Tangent", "A line touching a curve at one point."],
''') + MCQ((), '''  { q: "[Oct/Nov 2022 · 31 · Q6] The diagram shows two budget lines for a consumer of product X when its price changes, with two indifference curves and equilibria E1 and E2 (E2 is further to the right than E1). What is not a valid statement?", opts: ["Product X must be a Giffen good, since the consumer spends more on other goods after the price change.", "The consumer has greater satisfaction at E2 than at E1.", "The prices of other goods are assumed to be held constant when drawing the budget lines.", "The shift from the first budget line to the second represents a fall in the price of product X."], a: 0, why: "Spending more on other goods after a price fall does not make X a Giffen good: the quantity of X still rises. B, C and D are valid." },
''')
write("ic2", page(EY.format(2), "Consumer Equilibrium and Deriving Demand with Indifference Curves",
  "Where the budget line touches the highest reachable indifference curve, why MRS equals Px ÷ Py, and how a series of price changes builds the individual demand curve. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Consumer Equilibrium and Deriving Demand with Indifference Curves", "consumer-equilibrium-deriving-demand-ic")

# ------------------------------------------------------------------ 31.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>When the price of X falls, the total change in the quantity of X is the <b>price effect</b>, and economists split it into two. The <b>substitution effect (SE)</b> is the move along the <b>original</b> indifference curve to the new relative prices, found with a <b>compensating budget line</b> parallel to the new line; it always raises the quantity of the cheaper good. The <b>income effect (IE)</b> is the move from that point to the new equilibrium on a higher curve, caused by the rise in <b>real income</b>. For a normal good both effects raise quantity, so the demand curve slopes down.</p></div>
''' + S.b((56, 69)).replace("4 · A change", "1 · A change") + '''
  <h2>2 · The numbers for a normal good</h2>
  <p>Income $120, Py = $2, and Px falls from $4 to $2. The consumer moves from A (15 X) to B (30 X), a rise of 15. The compensating line is parallel to the new budget line and touches the original curve at C, 21.2 X. So the <b>substitution effect is +6.2</b> (A to C) and the <b>income effect is +8.8</b> (C to B), and 6.2 + 8.8 = 15.</p>
  <div class="tw"><table class="t">
    <tr><th>Step</th><th>Point</th><th>Units of X</th><th>Change</th></tr>
    <tr><td>Original equilibrium</td><td>A</td><td>15</td><td></td></tr>
    <tr><td>Compensated (same satisfaction)</td><td>C</td><td>21.2</td><td>SE = +6.2</td></tr>
    <tr><td>New equilibrium</td><td>B</td><td>30</td><td>IE = +8.8</td></tr>
    <tr><td>Total</td><td></td><td></td><td>+15</td></tr>
  </table></div>
  <div class="tip"><b class="h">Drawing it</b>Draw BL1 and IC1 touching at A. Pivot BL2 outwards. Draw IC2 touching BL2 at B. Draw the dashed compensating line parallel to BL2 touching IC1 at C. Label SE (A to C) and IE (C to B). The order matters: SE first, then IE.</div>
  <h2>3 · A price rise</h2>
  <p>For a price rise the same logic runs in reverse: the budget line pivots inwards, the consumer is poorer in real terms, the SE moves along the original curve away from X, and the IE for a normal good cuts quantity further. A tax on a good works like a price rise, which is why sales tax questions use this diagram.</p>
'''
watch = S.b((87, 89))
explore = S.b((109, 114)).replace("Lab 2 ·", "Lab 1 ·")
practise = S.b((142, 143)).replace("4 · Put", "1 · Put") + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((156, 156), (159, 159)) + '''  <div class="rw"><h3>A rise in rent</h3><p>When rent rises, tenants can afford less of everything else (the income effect) and may switch to cheaper housing or move out (the substitution effect). Both effects cut quantity for a normal good.</p><div class="use"><b>Exam use:</b> a price rise: budget line pivots inwards, SE and IE both reduce quantity of a normal good.</div></div>
'''
exam = '''
  <h2>Past paper questions on substitution and income effects</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The June 2020 papers were published but not sat, so they are marked "not sat". Below are the questions on splitting a price change into income and substitution effects, including price rises and sales tax, a practice question with a model answer and a Paper 3 multiple choice question. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2025 (41, 43)</td></tr>
    <tr><td>Essay parts, 13 marks</td><td>3</td><td>May/June 2021 (41, 43); Oct/Nov 2020 (41); Oct/Nov 2021 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>1 shown below</td><td>2022</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((193, 198), (239, 242), (246, 249), (253, 256)) + '''
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Using an indifference curve diagram, explain the income and substitution effects of a fall in the price of a normal good.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define both effects. Diagram: BL1, IC1, A; BL2, IC2, B; compensating line, C. Describe SE (A to C) then IE (C to B). Say both raise quantity for a normal good.</div>
''' + KEYS + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">The substitution effect is the change in the quantity demanded caused by the change in relative prices, with satisfaction held constant. The income effect is the change in quantity caused by the change in real income that follows the price change.</span></p>
    <p><span class="mk n" data-t="N">Suppose the price of good X falls. The budget line pivots outwards around the intercept on the Y axis and the consumer moves from equilibrium A on IC1 to equilibrium B on a higher curve IC2. To separate the effects, draw a compensating budget line parallel to the new budget line that just touches IC1 at point C.</span></p>
    <p><span class="mk n" data-t="N">The move from A to C is the substitution effect: X is now relatively cheaper, so the consumer is likely to buy more X and less Y while staying on the same indifference curve. The move from C to B is the income effect: the price fall raises real income, so the consumer reaches a higher curve.</span> <span class="mk a" data-t="A">For a normal good, such as restaurant meals, a higher real income may lead to more being bought, so the income effect also raises quantity.</span> <span class="mk e" data-t="E">The two effects therefore reinforce each other and the demand curve slopes downward, although the size of each effect depends on the shape of the indifference curves, which may differ between consumers.</span></p></div>
  </div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(272, 273)], '''    <li><b>Label the three points A, B and C</b> and name each move: A to C is the substitution effect, C to B is the income effect.</li>
    <li><b>The compensating line is parallel to the new budget line</b> and touches the original curve. Do not draw it through B.</li>
''', [(284, 284)]) + CMD(USE, DIS, DISC, EXP) + FC
js = HEAD + L((61, 74), (122, 131)) + '''const l2 = () => decompLab(NORM, "np", "s", "labB", vNorm);
Lib.slider($("#g4"), { id: "np", label: "New price of X ($): ", min: 1.5, max: 8, step: 0.5, value: 2, fmt: (v) => v, onInput: l2 });

/* ---------- Practise ---------- */
''' + L((180, 187)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Price effect", "The total change in quantity from a price change: SE plus IE"],
  ["Substitution effect", "The change in quantity from the change in relative prices, along the same indifference curve"],
  ["Income effect", "The change in quantity from the change in real income caused by the price change"],
  ["Compensating budget line", "A line parallel to the new budget line that touches the original curve"],
  ["Real income", "What income can buy, after allowing for prices"],
  ["Normal good", "A good for which quantity demanded rises when income rises"],
], done: "Six words for the price effect." });
''' + CALC((), extra='''  { q: "A fall in the price of X moves the consumer from 15 units to 30 units. What is the price effect (units)?", a: 15, sol: "30 − 15 = <b>+15</b>." },
  { q: "The compensated point C is at 21.2 units. What is the substitution effect (units, 1 decimal place)?", a: 6.2, tol: 0.1, sol: "21.2 − 15 = <b>+6.2</b>." },
  { q: "What is the income effect (units, 1 decimal place)?", a: 8.8, tol: 0.1, sol: "30 − 21.2 = <b>+8.8</b>." },
  { q: "A rise in the price of a normal good has a substitution effect of −4 units. The income effect is −3 units. What is the price effect?", a: -7, sol: "−4 − 3 = <b>−7</b>: both effects cut quantity." },
  { q: "The price of X falls from $4 to $3 and income is $120. By how much does the X-axis intercept of the budget line rise (units)?", a: 10, sol: "120 ÷ 3 = 40; before 120 ÷ 4 = 30. A rise of <b>10</b>." },
''') + QZ((201,), extra='''  { q: "The income effect of a price fall for a normal good:", opts: ["raises the quantity bought", "lowers the quantity bought", "is always zero", "is the same as the substitution effect"], a: 0, why: "Real income rises, and a normal good is bought more as income rises." },
  { q: "The compensating budget line is:", opts: ["parallel to the original budget line", "parallel to the new budget line and tangent to the original curve", "tangent to the new curve and parallel to the original line", "vertical"], a: 1, why: "It keeps satisfaction at the original level at the new relative prices." },
  { q: "The substitution effect of a price rise for X:", opts: ["raises the quantity of X", "lowers the quantity of X", "depends on the good", "is zero"], a: 1, why: "X becomes relatively dearer, so the consumer moves away from it along the same curve." },
''') + CARDS((213, 214, 215, 216), extra='''  ["Real income", "Income measured by what it can buy at current prices."],
''') + MCQ((232,))
write("ic3", page(EY.format(3), "The Price Effect: Substitution and Income Effects",
  "How a price change is split into a substitution effect along the original curve and an income effect to a new curve, with the compensating budget line, for price falls and price rises. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "The Price Effect: Substitution and Income Effects", "price-effect-substitution-income")

# ------------------------------------------------------------------ 31.4
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The sign and size of the <b>income effect</b> decide what kind of good it is. A <b>normal good</b> has a positive income effect, so both effects raise quantity when the price falls. An <b>inferior good</b> has a negative income effect, which works against the substitution effect but is smaller, so the demand curve still slopes down, though more steeply. A <b>Giffen good</b> is an inferior good whose negative income effect is <b>bigger</b> than the substitution effect, so a price fall cuts the quantity bought and the demand curve slopes up. Evaluation asks how realistic the assumptions behind the analysis are.</p></div>

  <h2>1 · Three kinds of good compared</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Normal good</th><th>Inferior good</th><th>Giffen good</th></tr>
    <tr><td><b>Substitution effect of a price fall</b></td><td>Raises quantity</td><td>Raises quantity</td><td>Raises quantity</td></tr>
    <tr><td><b>Income effect</b></td><td>Positive: raises quantity</td><td>Negative, smaller than the SE</td><td>Negative, larger than the SE</td></tr>
    <tr><td><b>Net effect of a price fall</b></td><td>Quantity rises a lot</td><td>Quantity rises, by less</td><td>Quantity falls</td></tr>
    <tr><td><b>Demand curve</b></td><td>Downward sloping</td><td>Downward sloping, steeper</td><td>Upward sloping</td></tr>
  </table></div>
  <h2>2 · The numbers for an inferior good</h2>
  <p>Income $60, Py = $1, and Px falls from $3 to $1.50. The consumer moves from A (5.7 X) to B (9.3 X), a rise of 3.7. The compensated point C is at 11.1 X, so the <b>substitution effect is +5.4</b> and the <b>income effect is −1.7</b>: the consumer is richer in real terms and buys <b>less</b> X because X is inferior. The IE is smaller than the SE, so the net change (+3.7) is still positive and the demand curve slopes down. If the IE were larger than +5.4 in size, the net change would be negative and the good would be Giffen.</p>
  <div class="tip"><b class="h">Giffen goods are rare</b>A Giffen good needs a strongly inferior good that takes a large part of a poor household's budget and has few substitutes. No convincing example is widely accepted today, and the textbook story is the staple food of a very poor household. The Giffen good is still examined because it is the one case where the law of demand fails.</div>
''' + S.b((78, 85)).replace("6 · Assumptions and evaluation", "3 · Assumptions and evaluation")
watch = S.b((91, 93))
explore = S.b((116, 121)).replace("Lab 3 ·", "Lab 1 ·") + S.b((123, 128)).replace("Lab 4 ·", "Lab 2 ·")
practise = S.b((136, 137)).replace("2 · Normal", "1 · Normal") + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((157, 158), (160, 160))
exam = '''
  <h2>Past paper questions on inferior goods, Giffen goods and evaluation</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays on normal, inferior and Giffen goods and the limits of the analysis, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2024 (41, 43)</td></tr>
    <tr><td>Essay, 25 marks</td><td>1</td><td>May/June 2022 (42)</td></tr>
    <tr><td>Essay parts, 13 marks</td><td>3</td><td>Oct/Nov 2021 (42); Feb/March 2022 (42); Oct/Nov 2020 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>3 shown below</td><td>2022 to 2025</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((178, 191), (208, 215)) + '''
  <h2>B · 13 mark questions</h2>
''' + S.b((218, 227), (234, 237), (251, 251)) + '''
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = TIPS([(274, 274), (276, 276)], '''    <li><b>Say which effect is bigger.</b> The sign of the IE alone does not make a good Giffen: the negative IE has to exceed the SE.</li>
    <li><b>Use the inferior good diagram to explain a steeper demand curve:</b> the IE offsets part of the SE, so quantity rises by less.</li>
''', [(285, 287)]) + CMD(USE, DISC, EVA) + FC
js = HEAD + L((61, 66), (75, 82), (122, 129), (131, 131)) + '''const l3 = () => decompLab(INF, "ip", "t", "labC", vInf);
Lib.slider($("#g5"), { id: "ip", label: "New price of X ($): ", min: 1, max: 5, step: 0.1, value: 1.5, fmt: (v) => Lib.fmtN(v, 1), onInput: l3 });

''' + L((136, 149)) + '''
/* ---------- Practise ---------- */
''' + L((161, 169)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Normal good", "Demand rises with income; both effects raise quantity when the price falls"],
  ["Inferior good", "Demand falls as income rises; the income effect works against the substitution effect"],
  ["Giffen good", "An inferior good whose negative income effect is larger than the substitution effect"],
  ["Law of demand", "Quantity demanded falls as price rises, other things equal"],
  ["Net effect", "The substitution effect plus the income effect"],
  ["Staple food", "A basic food that takes a large part of a poor household's budget"],
], done: "Six words for the kinds of good." });
''' + CALC((193, 194), extra='''  { q: "A good has SE = +12 units and IE = −4 units after a price fall. What is the net change?", a: 8, sol: "12 − 4 = <b>+8</b>: inferior, not Giffen." },
  { q: "A good has SE = +5.4 and IE = −1.7. By how much would the IE have to change in size before the good became Giffen (units, 1 decimal place)?", a: 3.7, tol: 0.1, hint: "The net change must fall below zero.", sol: "The IE would need to exceed 5.4 in size, so it must grow by more than 5.4 − 1.7 = <b>3.7</b> units." },
  { q: "SE = +10 and IE = −10. What is the net change (units)?", a: 0, sol: "10 − 10 = <b>0</b>. The borderline case: any larger negative IE makes the good Giffen." },
''') + QZ((202, 203), extra='''  { q: "The demand curve for an inferior good (not Giffen) is:", opts: ["upward sloping", "downward sloping", "vertical", "horizontal"], a: 1, why: "The net effect of a price fall is still a rise in quantity." },
  { q: "A Giffen good must be:", opts: ["a normal good", "an inferior good", "a luxury", "a public good"], a: 1, why: "The negative income effect that overrides the SE comes from the good being inferior." },
  { q: "If the substitution effect of a price rise is −3 and the income effect is +5 (for a Giffen good), the net change in quantity is:", opts: ["−8", "−2", "+2", "+8"], a: 2, why: "−3 + 5 = +2: quantity rises when price rises." },
''') + CARDS((217, 218, 219), extra='''  ["Law of demand", "Quantity demanded falls as price rises, other things equal."],
  ["Net effect", "The substitution effect plus the income effect."],
''') + MCQ((226, 227), '''  { q: "[May/June 2022 · 31 · Q6] Broken rice is an inferior good. What would be the resulting income and substitution effect on the quantity demanded of broken rice if its price falls? (quantity demanded due to income effect, quantity demanded due to substitution effect)", opts: ["falls, falls", "falls, rises", "rises, falls", "rises, rises"], a: 1, why: "For an inferior good a rise in real income lowers quantity, while the cheaper relative price raises it through the substitution effect." },
''')
write("ic4", page(EY.format(4), "Inferior Goods, Giffen Goods and Evaluation",
  "How the sign and size of the income effect separate normal, inferior and Giffen goods, why demand for most inferior goods still slopes down, and how to evaluate indifference curve analysis. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Inferior Goods, Giffen Goods and Evaluation", "inferior-giffen-goods-evaluation")
