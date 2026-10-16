"""Builds the four ch33 part pages (ex1..ex4) from slices of ex.* plus new content. Run: python3 tools/artifact-kit/mk_ch33.py"""
from splitter import Src, page, write, key
S = Src("ex")
HEAD = S.j_((1, 4)) + 'const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };\n'
EY = "A Level Economics · 9708 · Syllabus 7.4 · Part {} of 4"
NOTE = '<p class="note">Examples are explained in general terms. The numbers are simple on purpose, to show the idea.</p>\n'
def MCQ(old=(), new=""):
    return 'Lib.quiz($("#qz2"), { qs: [\n' + S.j_(*[(i, i) for i in old]) + new + '] });\n'
CMD = lambda *rows: '<h2>Command words</h2>\n  <div class="tw"><table class="t">\n    <tr><th>Command word</th><th>What it asks for</th></tr>\n' + "".join(f"    <tr><td>{a}</td><td>{b}</td></tr>\n" for a, b in rows) + '  </table></div>\n'
EXPLAIN = ("Explain", "Give reasons, with a clear chain of cause and effect.")
EVAL = ("Assess / Evaluate", "Weigh the arguments and reach a supported conclusion.")
DISC = ("Discuss", "Arguments on both sides, then a judgement.")
CONS = ("Consider", "Look at the issue from several sides and judge how strong each is.")
def tips(items, sents):
    return '<h2>Top tips</h2>\n  <ul class="tips">\n' + "".join(f"    <li><b>{a}</b> {b}</li>\n" for a, b in items) + '  </ul>\n  <h2>Sentences you can use</h2>\n  <div class="tw"><table class="t">\n    <tr><th>You want to say</th><th>Use this sentence</th></tr>\n' + "".join(f'    <tr><td>{a}</td><td>"{b}"</td></tr>\n' for a, b in sents) + '  </table></div>\n'

# ---------------------------------------------------------------- 33.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Every decision has <b>private</b> costs and benefits that fall on the buyer or seller, and sometimes <b>external</b> ones that fall on a <b>third party</b> who is not part of the deal. <b>Social cost = private cost + external cost</b> and <b>social benefit = private benefit + external benefit</b>. Externalities can be <b>negative or positive</b> and can come from <b>production or consumption</b>, giving four types. Because the market price ignores the external part, decision-makers use the wrong numbers, which is why externalities lead to market failure (shown on diagrams in part 2).</p></div>
''' + S.b((25, 36), (38, 45)).replace("1 · Private, external and social", "1 · Private, external and social").replace("2 · The four types", "2 · The four types") + '''
  <h2>3 · Why the market ignores them</h2>
  <p>A price is agreed between a buyer and a seller. Anyone else who is helped or harmed has no say and is not paid or charged, so the price carries no signal about their costs or benefits. A smoker weighs the price of cigarettes against the pleasure, not the effect of smoke on others. Externalities are often <b>spill-overs</b> that are hard to measure and hard to charge for, which is also why governments find them hard to correct. The next parts show the diagrams, the policies and cost-benefit analysis.</p>
'''
watch = '''
  <h2>1 · Private cost plus external cost, private benefit plus external benefit</h2>
  <p>Two examples, one for each side. On the cost side, a factory whose production causes pollution. On the benefit side, a vaccination. Press Play, or click the steps.</p><div id="stP1"></div>
'''
explore = '''
  <h2>Lab 1 · One more unit: private against social</h2>
  <p>Set the private cost and benefit of one more unit, then add an external cost or benefit. The private decision-maker looks at the left numbers in each pair; society looks at the totals.</p>
  <div class="card"><div class="grid2"><div><div id="g8"></div><div id="g9"></div><div id="g10"></div><div id="g11"></div>
    <div class="readout"><div><small>Marginal social cost</small><strong id="v1"></strong></div><div><small>Marginal social benefit</small><strong id="v2"></strong></div><div><small>Private decision</small><strong id="v3"></strong></div><div><small>Social verdict</small><strong id="v4"></strong></div></div>
    <div class="verdict" id="vv"></div></div>
    <div><svg id="labJ" viewBox="0 0 420 270" role="img" aria-label="Stacked bars of private and external cost, and private and external benefit of one more unit"></svg></div></div></div>
'''
practise = S.b((129, 133)) + '''
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((153, 155)) + '''  <div class="rw"><h3>Second-hand smoke and noisy neighbours</h3><p>Noise from a neighbour's party or smoke drifting from a smoker are costs to people who did not agree to them. The party-goer enjoys the benefit and the neighbours bear the cost.</p><div class="use"><b>Exam use:</b> a negative consumption externality, MSB less than MPB, with the decision-maker ignoring the third party.</div></div>
'''
exam = '''
  <h2>Past paper questions on private and external costs and benefits</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the questions that ask for the meaning of externalities and social costs and benefits, plus ten Paper 3 multiple choice questions. The questions on diagrams are in part 2 of this chapter, policy questions in part 3 and cost-benefit analysis in part 4. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay part, 12 marks</td><td>1</td><td>Oct/Nov 2022 (42)</td></tr>
    <tr><td>Data response parts</td><td>2</td><td>May/June 2023 (41, 43); Oct/Nov 2023 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>10 shown below</td><td>2020 to 2023</td></tr>
  </table></div>
  <h2>A · A 12 mark question with a model answer</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((220, 228)) + '''
  <h2>B · Data response parts</h2>
  <details class="eq"><summary>Data response parts on the meaning of externalities</summary><div class="body"><ul>
    <li><b>May/June 2023 · 41 and 43 · Q1(b) [4]:</b> explain, with an example, whether the article is right that neither the producer nor the consumer pays for negative externalities.</li>
    <li><b>Oct/Nov 2023 · 42 · Q1(b) [6]:</b> explain with a diagram what a negative externality is and identify two examples from the article.</li></ul></div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips_html = tips([
  ("Define an externality as a cost or benefit to a third party that is not reflected in the price.", 'Add "spill-over" and "marginal social cost greater than marginal private cost".'),
  ("State the identities:", "MSC = MPC + MEC, MSB = MPB + MEB. Use MSB = MSC for efficiency."),
  ("Ask who creates the effect.", "A producer's activity is a production externality, a consumer's a consumption externality. Then ask whether it harms or helps third parties."),
  ("Give a specific example for each type,", "and say who the third party is. Vaccination, congestion, aircraft noise and chewing gum litter are all in the papers."),
  ("Do not confuse external with private.", "A cost the factory pays itself, such as wages, is private. A cost paid by the town is external."),
], [
  ("Define the term", "A negative externality is a cost imposed on a third party that is not paid by the producer or consumer, so the marginal social cost exceeds the marginal private cost."),
  ("Social cost", "Social cost equals private cost plus external cost, so the decision-maker ignores part of the true cost."),
  ("Positive", "A positive externality is a benefit to a third party, so the marginal social benefit exceeds the marginal private benefit."),
]) + CMD(EXPLAIN, ("Define / What is meant by", "A short, accurate meaning, with an example if asked."), EVAL) + '  <h2>Flashcards</h2><div id="fc1"></div>\n'
js = HEAD + '''
/* ---------- Watch: private + external = social ---------- */
const H1 = (v) => v * 3.2, B0 = 290;
function psDraw(s) {
  let o = SV.line(60, B0, 740, B0) + SV.text(62, 24, "$ per unit", "sm");
  if (s.pc > 0) o += SV.rect(110, B0 - H1(40) * s.pc, 110, H1(40) * s.pc, "f4", op(s.pc)) + SV.text(228, B0 - H1(40) / 2, "private cost $40", "lbl bd t4", { ...halo, ...op(s.pc) });
  if (s.ec > 0) o += SV.rect(110, B0 - H1(40) - H1(15) * s.ec, 110, H1(15) * s.ec, "f2", op(s.ec)) + SV.text(228, B0 - H1(40) - H1(15) / 2 + 4, "external cost $15", "lbl bd t2", { ...halo, ...op(s.ec) });
  if (s.sc > 0) o += SV.text(165, B0 - H1(55) - 10, "social cost $55", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.sc) });
  if (s.pb > 0) o += SV.rect(470, B0 - H1(60) * s.pb, 110, H1(60) * s.pb, "f1", op(s.pb)) + SV.text(588, B0 - H1(60) / 2, "private benefit $60", "lbl bd t1", { ...halo, ...op(s.pb) });
  if (s.eb > 0) o += SV.rect(470, B0 - H1(60) - H1(15) * s.eb, 110, H1(15) * s.eb, "f3", op(s.eb)) + SV.text(588, B0 - H1(60) - H1(15) / 2 + 4, "external benefit $15", "lbl bd t3", { ...halo, ...op(s.eb) });
  if (s.sb > 0) o += SV.text(525, B0 - H1(75) - 10, "social benefit $75", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.sb) });
  o += SV.text(165, B0 + 22, "Factory: cost of one more unit", "sm", { "text-anchor": "middle" }) + SV.text(525, B0 + 22, "Vaccination: benefit of one more", "sm", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stP1"), { w: 780, h: 320, label: "Private cost plus external cost equals social cost; private benefit plus external benefit equals social benefit", base: { pc: 0, ec: 0, sc: 0, pb: 0, eb: 0, sb: 0 }, draw: psDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Private cost.</b> A factory pays $40 in wages, materials and energy to make one more unit. This is what its decisions are based on.", s: { pc: 1 } },
  { cap: "<b>External cost.</b> Making that unit also pollutes the air, costing nearby residents $15. The factory does not pay it, so it is an <b>external cost</b>. <b>Social cost = $40 + $15 = $55</b>.", s: { pc: 1, ec: 1, sc: 1 } },
  { cap: "<b>Private benefit.</b> Now the benefit side. A person who is vaccinated values the protection at $60. This is what the buyer considers.", s: { pc: 1, ec: 1, sc: 1, pb: 1 } },
  { cap: "<b>External benefit.</b> Others in the community are less likely to catch the disease, worth $15 to them. <b>Social benefit = $60 + $15 = $75</b>.", s: { pc: 1, ec: 1, sc: 1, pb: 1, eb: 1, sb: 1 } },
  { cap: "<b>Why it matters.</b> Decision-makers see only the lower parts of each bar. They produce too much of the polluting good (price too low) and buy too little of the vaccination (price too high for the social benefit). Part 2 shows this on a diagram.", s: { pc: 1, ec: 1, sc: 1, pb: 1, eb: 1, sb: 1 } },
] });

/* ---------- Lab 1: one more unit ---------- */
function lab6() {
  if (!$("#pcs") || !$("#mec") || !$("#pbs") || !$("#meb")) return;
  const pc = +$("#pcs").value, ec = +$("#mec").value, pb = +$("#pbs").value, eb = +$("#meb").value, sc = pc + ec, sb = pb + eb, priv = pb >= pc, soc = sb >= sc;
  $("#v1").textContent = "$" + sc; $("#v2").textContent = "$" + sb; $("#v3").textContent = priv ? "Produce" : "Do not"; $("#v4").textContent = soc ? "Worth it" : "Not worth it";
  $("#vv").innerHTML = priv && soc ? "The unit is worth producing for the decision-maker and for society."
    : priv && !soc ? `The decision-maker sees a gain of $${pb - pc}, but society loses $${sc - sb} once the external cost is counted. This is <b>overproduction</b>: the unit is made but should not be.`
    : !priv && soc ? `The decision-maker sees a loss of $${pc - pb}, but society would gain $${sb - sc} once the external benefit is counted. This is <b>underproduction</b>: the unit is not made but should be.`
    : "The unit is not worth producing for the decision-maker or for society.";
  const H = (v) => 1.6 * v, base = 215;
  let o = SV.line(30, base, 400, base);
  [[70, pc, ec, "f4", "f2", "Cost of one more unit"], [250, pb, eb, "f1", "f3", "Benefit of one more unit"]].forEach(([x, p, e, c1, c2, l]) => {
    o += SV.rect(x, base - H(p), 100, H(p), c1) + SV.rect(x, base - H(p) - H(e), 100, H(e), c2) + SV.text(x + 50, base - H(p + e) - 8, "$" + (p + e), "lbl bd", { "text-anchor": "middle" }) +
      SV.text(x + 50, base - H(p) / 2 + 4, "private $" + p, "sm bd", { "text-anchor": "middle", ...halo }) + (e > 0 ? SV.text(x + 50, base - H(p) - H(e) / 2 + 4, "external $" + e, "sm bd", { "text-anchor": "middle", ...halo }) : "") + SV.text(x + 50, 238, l, "sm", { "text-anchor": "middle" });
  });
  $("#labJ").innerHTML = o;
}
Lib.slider($("#g8"), { id: "pcs", label: "Private cost ($): ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g9"), { id: "mec", label: "External cost ($): ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g10"), { id: "pbs", label: "Private benefit ($): ", min: 30, max: 90, step: 5, value: 50, fmt: (v) => v, onInput: lab6 });
Lib.slider($("#g11"), { id: "meb", label: "External benefit ($): ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: lab6 });

/* ---------- Practise ---------- */
''' + S.j_((146, 165)) + '''
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Externality", "A cost or benefit that falls on a third party and is not in the price"],
  ["Third party", "Someone who is not the buyer or the seller"],
  ["Marginal social cost", "Marginal private cost plus marginal external cost"],
  ["Marginal social benefit", "Marginal private benefit plus marginal external benefit"],
  ["Negative externality", "A third party suffers a cost they did not agree to"],
  ["Positive externality", "A third party gains a benefit they did not pay for"],
  ["Spill-over", "Another word for an externality: an effect that spills onto others"],
], done: "Seven words that define the chapter." });
Lib.calc($("#c1"), { qs: [
''' + S.j_((185, 186)) + '''  { q: "A factory's private cost of a unit is $40 and the social cost is $52. What is the marginal external cost ($)?", a: 12, sol: "External cost = social cost − private cost = <b>$12</b>." },
''' + S.j_((187, 187)) + '''  { q: "A vaccination has a private benefit of $60 and a social benefit of $75. What is the external benefit ($)?", a: 15, sol: "75 − 60 = <b>$15</b>." },
  { q: "A unit has MPB $50, MPC $40 and a marginal external cost of $20. What is the net social benefit of producing it ($, negative for a loss)?", a: -10, hint: "MSC = 40 + 20.", sol: "MSB 50 − MSC 60 = <b>−$10</b>: society loses, though the firm gains $10." },
] });
Lib.quiz($("#qz1"), { qs: [
''' + S.j_((194, 196)) + '''  { q: "Which is an external cost?", opts: ["Wages paid by a factory", "Cost of raw materials", "Illness among nearby residents from the factory's smoke", "The factory's advertising spend"], a: 2, why: "Only the residents' illness falls on a third party." },
  { q: "A positive consumption externality means:", opts: ["MSB is greater than MPB", "MSC is greater than MPC", "MSB equals MPB", "MPC equals MPB"], a: 0, why: "Others gain from consumption, so the social benefit is greater than the private benefit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Private cost", "Cost paid by the producer or consumer making the decision."],
  ["External cost", "Cost imposed on a third party and not paid by the decision-maker."],
  ["Social cost", "Private cost plus external cost."],
  ["Private benefit", "Benefit received by the consumer or producer."],
  ["External benefit", "Benefit received by a third party who did not pay."],
  ["Social benefit", "Private benefit plus external benefit."],
  ["Externality", "A spill-over cost or benefit to a third party that is not reflected in the market price."],
  ["Third party", "Someone who is neither buyer nor seller in a transaction."],
  ["MSC = MPC + MEC", "Marginal social cost is private plus external cost."],
  ["MSB = MPB + MEB", "Marginal social benefit is private plus external benefit."],
  ["Production externality", "Created by a producer's activity."],
  ["Consumption externality", "Created by a consumer's activity."],
] });
''' + MCQ(range(221, 231))
write("ex1", page(EY.format(1), "Private and External Costs and Benefits",
  "What an externality is, how private and external combine into social costs and benefits, and the four types. Animated stacked bars, labs, drills and the past paper questions on definitions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips_html), js,
  "Private and External Costs and Benefits", "private-external-costs-benefits")

# ---------------------------------------------------------------- 33.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The firm's supply curve is its <b>private</b> marginal cost (MPC) and demand is the <b>private</b> marginal benefit (MPB). With a <b>negative externality</b> the social cost curve (MSC) lies <b>above</b> MPC, so the market produces more than the social optimum, where MSB = MSC. With a <b>positive externality</b> the social benefit curve (MSB) lies <b>above</b> MPB, so the market produces less than the optimum. In both cases the triangle between the two outputs is a <b>welfare loss</b>, the net social benefit that is thrown away.</p></div>
''' + S.b((47, 58)).replace("3 · The diagram", "1 · The diagram") + '''
  <h2>2 · The positive externality diagram in numbers</h2>
  <p>Demand (MPB) is P = 100 − Q, marginal cost is 20 + 0.5Q and the external benefit is $15 a unit, so MSB = 115 − Q. The market output is where MPB = MC: <b>Q = 53</b>. The social optimum is where MSB = MC: <b>Q = 63</b>. On each unit from 53 to 63 the social benefit is more than the cost, but the unit is not produced. The triangle has base 10 and height 15, so the welfare loss is <b>75</b>.</p>
  <h2>3 · All four types at a glance</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Curve that shifts</th><th>Market output compared with the social optimum</th></tr>
    <tr><td>Negative production</td><td>MSC above MPC</td><td>Too high (overproduction), price too low</td></tr>
    <tr><td>Negative consumption</td><td>MSB below MPB</td><td>Too high (over-consumption)</td></tr>
    <tr><td>Positive production</td><td>MSC below MPC</td><td>Too low (underproduction)</td></tr>
    <tr><td>Positive consumption</td><td>MSB above MPB</td><td>Too low (under-consumption)</td></tr>
  </table></div>
  <div class="tip"><b class="h">How to draw it in an exam</b>Draw demand and supply, label them MPB and MPC. Add the extra curve (MSC or MSB) in the right place. Mark Q<sub>m</sub> where the private curves cross and Q<sub>s</sub> where the social curves cross, then shade the welfare loss triangle between them. Label the axes and the curves. Several 20-mark answers are capped at Level 2 without a diagram.</div>
'''
watch = '''
  <h2>1 · Negative production externality</h2>
  <p>Demand P = 100 − Q. Private marginal cost = 20 + 0.5Q. External cost = $15 per unit. Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Positive consumption externality</h2>
  <p>Private marginal benefit P = 100 − Q. External benefit = $15 per unit. Marginal cost = 20 + 0.5Q.</p><div id="stB"></div>
'''
explore = '''
  <h2>Lab 1 · How big is the welfare loss?</h2>
  <p>Move the external cost per unit and watch the social optimum move away from the market output. The welfare loss is the triangle between them. Demand is P = 100 − Q and private marginal cost is 20 + 0.5Q.</p>
  <div class="card"><div class="grid2"><div><div id="g12"></div>
    <div class="readout"><div><small>Market output</small><strong id="x1"></strong></div><div><small>Social optimum</small><strong id="x2"></strong></div><div><small>Overproduction</small><strong id="x3"></strong></div><div><small>Welfare loss</small><strong id="x4"></strong></div></div>
    <div class="verdict" id="xv"></div></div>
    <div><svg id="labK" viewBox="0 0 420 320" role="img" aria-label="Market with a negative externality showing market output, social optimum and welfare loss"></svg></div></div></div>

''' + S.b((120, 124)).replace("Lab 4 · Private", "Lab 2 · Private")
practise = '''
  <h2>1 · Overproduction or underproduction?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the externality argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((151, 151)) + '''  <div class="rw"><h3>Education</h3><p>An educated person earns more, but others also gain from a more skilled workforce, lower crime and more tax revenue. Because individuals consider only their own return, too little education may be bought without help.</p><div class="use"><b>Exam use:</b> a positive consumption externality, MSB above MPB, with under-consumption and a welfare loss.</div></div>
  <div class="rw"><h3>An orchard and a beekeeper</h3><p>An orchard owner's trees give bees nectar, and bees pollinate the trees of neighbouring growers. Each side benefits without paying, so both may produce too little.</p><div class="use"><b>Exam use:</b> a standard positive production externality, MSC below MPC.</div></div>
  <div class="rw"><h3>Pollution from a chemical plant</h3><p>A plant that discharges waste into a river pays for chemicals and labour, but the town downstream pays for water treatment. Output is higher than is best for society.</p><div class="use"><b>Exam use:</b> a negative production externality: draw MPC and MSC, show Q<sub>m</sub> above Q<sub>s</sub>.</div></div>
'''
exam = '''
  <h2>Past paper questions on externality diagrams</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the questions that ask for diagrams of externalities and market failure, plus Paper 3 multiple choice questions, and a practice question with a model answer. Several policy questions also ask for the same diagram; they are in part 3. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>Oct/Nov 2022 (42)</td></tr>
    <tr><td>Data response part, 10 marks</td><td>1</td><td>May/June 2025 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>3 shown below</td><td>2021 to 2024</td></tr>
  </table></div>
  <h2>A · Written questions</h2>
''' + S.b((230, 233)) + '''
  <details class="eq"><summary>Data response part on a diagram</summary><div class="body"><ul>
    <li><b>May/June 2025 · 42 · Q1(d) [10]:</b> with a marginal social cost and benefit diagram, discuss whether continued use of coal for electricity makes allocative efficiency less likely. <i>Key points:</i> coal has external costs (air pollution, health costs, climate effects), so MSC is above MPC, output is above the social optimum and there is a welfare loss; evaluate by considering the cost of alternatives and how large the external cost is.</li></ul></div></details>
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Using a diagram, explain why a positive consumption externality such as education may lead to market failure.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define a positive consumption externality. Diagram: MPB, MSB above it, MC, Q<sub>m</sub>, Q<sub>s</sub> and the welfare loss triangle. Explain under-consumption, then one evaluative comment on measurement.</div>
''' + key() + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">A positive consumption externality is a benefit to a third party that arises when someone consumes a good and that is not reflected in the price, so the marginal social benefit (MSB) is greater than the marginal private benefit (MPB).</span></p>
    <p><span class="mk a" data-t="A">Education is an example: an educated person earns more, but the community may also gain from a more skilled workforce and lower crime.</span> <span class="mk n" data-t="N">On a diagram, MSB lies above MPB by the external benefit per unit. Buyers decide using MPB, so the market output Q<sub>m</sub> is where MPB meets marginal cost. The social optimum Q<sub>s</sub> is where MSB meets marginal cost and is greater than Q<sub>m</sub>.</span></p>
    <p><span class="mk n" data-t="N">Between Q<sub>m</sub> and Q<sub>s</sub> each unit gives society a benefit greater than its cost, but is not consumed, so there is a welfare loss shown by the triangle between MSB and marginal cost. The market under-allocates resources to education, which is market failure.</span> <span class="mk e" data-t="E">The size of the welfare loss may depend on how large the external benefit is, which could be hard to measure, so the under-consumption could be smaller or larger than the diagram suggests.</span></p></div>
  </div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips_html = tips([
  ("Draw the diagram, and label it.", "Q<sub>m</sub>, Q<sub>s</sub>, MPC, MSC, MPB, MSB and the welfare loss triangle. Several 20-mark answers are capped at Level 2 without one."),
  ("Put the extra curve on the right side.", "MSC is above MPC for an external cost. MSB is above MPB for an external benefit."),
  ("Say which way the market goes wrong:", "negative externality, overproduction and price too low; positive externality, underproduction."),
  ("Explain the welfare loss as units that cost more than they are worth", "(negative) or are worth more than they cost but are not made (positive)."),
  ("Refer to the diagram in your writing,", "not only draw it. Mark schemes ask for diagrams referred to in the text."),
], [
  ("Overproduction", "The market produces where MPB equals MPC, which is more than the socially efficient output where MSB equals MSC, so there is a welfare loss."),
  ("Positive externality", "The market under-produces because consumers ignore the external benefit, so a subsidy could raise output to the social optimum."),
  ("Welfare loss", "The triangle shows the net benefit to society that is lost because output is not at the social optimum."),
]) + CMD(EXPLAIN, EVAL, DISC) + '  <h2>Flashcards</h2><div id="fc1"></div>\n'
js = HEAD + S.j_((6, 49)) + '''
/* ---------- Lab 1: welfare loss ---------- */
function lab7() {
  if (!$("#mx")) return;
  const m = +$("#mx").value, q = 160 / 3, qs = (80 - m) / 1.5, loss = 0.5 * (q - qs) * m;
  $("#x1").textContent = Lib.fmtN(q, 1); $("#x2").textContent = Lib.fmtN(qs, 1); $("#x3").textContent = Lib.fmtN(q - qs, 1); $("#x4").textContent = Lib.fmtN(loss, 0);
  $("#xv").textContent = m === 0 ? "There is no external cost, so market output and the social optimum are the same: there is no welfare loss."
    : `With an external cost of $${m} a unit the social optimum is ${Lib.fmtN(qs, 1)} units but the market produces ${Lib.fmtN(q, 1)}. The ${Lib.fmtN(q - qs, 1)} extra units each cost society more than they are worth. Welfare loss = ½ × ${Lib.fmtN(q - qs, 1)} × ${m} = ${Lib.fmtN(loss, 0)}. Double the external cost and the loss roughly quadruples.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(qs), y(100 - qs)], [x(q), y(100 - q)], [x(q), y(20 + 0.5 * q + m)]], "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(70), "c3") + SV.line(x(0), y(20 + m), x(100), y(70 + m), "c2");
  o += SV.circle(x(q), y(100 - q), 6, "dot4") + SV.circle(x(qs), y(100 - qs), 6, "dot3") + SV.text(x(q), 288, "Qm", "sm bd t4", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t3", { "text-anchor": "middle" }) + SV.text(x(100) - 4, y(0) - 6, "MPB = MSB", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(70) + 18, "MPC", "sm bd t3", { "text-anchor": "end" }) + (m > 0 ? SV.text(x(100) - 4, y(70 + m) - 6, "MSC", "sm bd t2", { "text-anchor": "end" }) : "");
  $("#labK").innerHTML = o;
}
Lib.slider($("#g12"), { id: "mx", label: "External cost per unit ($): ", min: 0, max: 30, step: 1, value: 15, fmt: (v) => v, onInput: lab7 });
''' + S.j_((131, 143)) + '''
/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does the free market overproduce or underproduce?",
  buckets: [{ label: "Overproduces (or over-consumes)" }, { label: "Underproduces (or under-consumes)" }],
  items: [
    { text: "Smoke from a factory chimney", b: 0 }, { text: "Traffic congestion caused by drivers", b: 0 }, { text: "Noise from aircraft", b: 0 }, { text: "Litter from chewing gum", b: 0 },
    { text: "Vaccination", b: 1 }, { text: "Education", b: 1 }, { text: "A firm training workers who then join rivals", b: 1 }, { text: "Research that other firms can use", b: 1 },
  ], done: "Negative externalities lead to too much, positive externalities to too little.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Qm", "The market output, where the private curves cross"],
  ["Qs", "The socially optimal output, where MSB = MSC"],
  ["Welfare loss", "The loss of net social benefit when output differs from the social optimum"],
  ["Overproduction", "Output above the social optimum, from a negative externality"],
  ["Underproduction", "Output below the social optimum, from a positive externality"],
  ["Allocative efficiency", "Producing where marginal social benefit equals marginal social cost"],
  ["Market failure", "The market allocates resources inefficiently"],
], done: "Seven words for the diagrams." });
''' + S.j_((176, 183)) + '''
Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and MPC = 20 + 0.5Q. What is the market output (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives Q = <b>53.3</b>." },
  { q: "The external cost is $15 a unit, so MSC = 35 + 0.5Q. What is the social optimum (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives Q = <b>43.3</b>." },
''' + S.j_((189, 189)) + '''  { q: "The external cost doubles from $15 to $30. The social optimum becomes 33.3 and the market output is still 53.3. What is the welfare loss (½ × base × 30)?", a: 300, sol: "Base = 20, so ½ × 20 × 30 = <b>300</b>, four times the previous loss of 75." },
  { q: "A positive externality of $15 a unit raises the social optimum from 53.3 to 63.3 units. What is the welfare loss (½ × 10 × 15)?", a: 75, sol: "½ × 10 × 15 = <b>$75</b>." },
''' + '''] });
Lib.quiz($("#qz1"), { qs: [
''' + S.j_((195, 195), (199, 199)) + '''  { q: "At the socially optimal output:", opts: ["MPB = MPC", "MSB = MSC", "MSC = MPC", "welfare loss is at its largest"], a: 1, why: "Allocative efficiency needs marginal social benefit equal to marginal social cost." },
  { q: "On a negative externality diagram, the welfare loss is the triangle between:", opts: ["MPC and MPB from 0 to Qs", "MSC and MSB from Qs to Qm", "MSC and MPC at Qs", "the demand curve and the axes"], a: 1, why: "Between Qs and Qm each unit costs society more (MSC) than it is worth (MSB)." },
  { q: "A negative consumption externality shifts which curve?", opts: ["MSB falls below MPB", "MSC rises above MPC", "MSB rises above MPB", "MSC falls below MPC"], a: 0, why: "Consumption harms others, so the social benefit is lower than the private benefit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Qm", "Market output, where MPB = MPC."],
  ["Qs", "Socially optimal output, where MSB = MSC."],
  ["Welfare loss", "Net social benefit lost because output is not at the social optimum."],
  ["Overproduction", "Market output above the social optimum (negative externality)."],
  ["Underproduction", "Market output below the social optimum (positive externality)."],
  ["MSC above MPC", "Negative production externality."],
  ["MSB below MPB", "Negative consumption externality."],
  ["MSC below MPC", "Positive production externality."],
  ["MSB above MPB", "Positive consumption externality."],
  ["Allocative efficiency", "Output where marginal social benefit equals marginal social cost."],
] });
''' + MCQ((231,), '''  { q: "[Oct/Nov 2024 · 32 · Q4] A government makes it compulsory for motorbike riders to wear helmets. What would represent a positive externality of consumption associated with this decision?", opts: ["decreased pressure on the provision of health care", "expenses incurred on surveillance of motorbike riders to ensure compliance", "increased life expectancy of motorbike riders", "increased profits of helmet manufacturers"], a: 0, why: "A benefit that falls on a third party (the health system and taxpayers). C is a private benefit to the riders themselves." },
  { q: "[Oct/Nov 2023 · 32 · Q3] Negative externalities, such as air pollution due to car emissions, can cause damage to people's health in cities. Which response is most likely to occur from this situation?", opts: ["car manufacturers will automatically bear any external costs", "market failure will be resolved when private costs equal external costs", "most people will decide to use buses rather than cars", "some form of government intervention to improve economic efficiency"], a: 3, why: "The market does not correct the external cost on its own, so intervention is likely. A is the opposite of an externality and B confuses private and external costs." },
''')
write("ex2", page(EY.format(2), "Externalities and Welfare Loss: the Diagrams",
  "Negative and positive externalities on MPB, MPC, MSB and MSC diagrams: market output against the social optimum, overproduction, underproduction and the welfare loss triangle. Animated diagrams built from numbers, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips_html), js,
  "Externalities and Welfare Loss: the Diagrams", "externalities-welfare-loss-diagrams")

# ---------------------------------------------------------------- 33.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>To correct an externality the government can <b>internalise</b> it: a <b>tax equal to the external cost</b> moves MPC up to MSC, and a <b>subsidy equal to the external benefit</b> moves output up to the social optimum. It can also use <b>regulation</b>, <b>tradable permits</b>, <b>information</b> and <b>state provision</b>, or leave it to <b>property rights and bargaining</b> between the parties. Each approach has costs, and the right level is hard to find because external costs and benefits are hard to measure. A good answer chooses a tool, explains it with a diagram, and then weighs its limits.</p></div>

  <h2>1 · Internalising with a tax or a subsidy</h2>
  <ul>
    <li><b>Tax on a negative externality.</b> With an external cost of $15 a unit, a tax of $15 shifts supply up to MSC, so the market output falls from 53 to the social optimum of 43 and the welfare loss of 75 disappears.</li>
    <li><b>Subsidy for a positive externality.</b> With an external benefit of $15, a subsidy of $15 shifts supply down so that output rises from 53 to the social optimum of 63.</li>
    <li><b>Too low or too high.</b> A tax below the external cost leaves some overproduction. A tax above it overcorrects, so output falls below the optimum and a new welfare loss appears. The Explore tab lets you test this.</li>
  </ul>
  <div class="tip"><b class="h">Link to syllabus 8.1</b>Tax incidence, how subsidies work and how permits cap pollution are explained in syllabus 8.1 part 2. Here the focus is on why the tax or subsidy is set equal to the external cost.</div>

  <h2>2 · Other policies</h2>
  <div class="grid2">
    <div class="card"><h3>Regulation and bans</h3><p>Standards, limits on emissions or night flights, and bans. Precise and quick, but costly to monitor and with no reward for doing better than the limit.</p></div>
    <div class="card"><h3>Tradable permits</h3><p>A cap on total pollution with permits that firms can trade, so the cap is met at the lowest cost. The cap may be set wrongly.</p></div>
    <div class="card"><h3>Information and persuasion</h3><p>Warnings, campaigns and negative advertising can change behaviour cheaply, but the effect may be small, especially for addictive goods.</p></div>
    <div class="card"><h3>Public provision and transport policy</h3><p>Building public transport or providing the service directly, or congestion charges and quotas for road use. Costs fall on taxpayers.</p></div>
  </div>

  <h2>3 · Property rights and bargaining</h2>
  <p>If property rights are clear and few people are involved, the parties may bargain without the government. Suppose a factory gains $100 from producing and the damage to a resident is $60. If the resident holds the right to clean air, the factory can pay any amount between $60 and $100 and both gain, so production goes ahead. If the damage is $150, no payment can satisfy both, and the factory stops. Either way the outcome is efficient, but it needs clear rights, few parties and low <b>transaction costs</b>, which is rarely true for pollution that affects thousands of people.</p>
''' + S.b((73, 79)).replace("5 · Evaluating externality arguments", "4 · Evaluating the policy options")
watch = '''
  <h2>1 · Bargaining over pollution</h2>
  <p>A factory gains from producing and a resident suffers damage. If the resident holds the right to clean air, can they settle without the government? Press Play, or click the steps.</p><div id="stCo"></div>
'''
explore = S.b((99, 104)).replace("Lab 1 · Tax", "Lab 1 · Tax") + "\n" + S.b((106, 111)) + '''
  <h2>Lab 3 · Can the parties bargain?</h2>
  <p>A factory gains from producing and a resident suffers damage. Set both and see whether a deal exists when the resident holds the right to clean air.</p>
  <div class="card"><div class="grid2"><div><div id="g13"></div><div id="g14"></div>
    <div class="readout"><div><small>Factory gain</small><strong id="y1"></strong></div><div><small>Resident damage</small><strong id="y2"></strong></div><div><small>Payments both accept</small><strong id="y3"></strong></div><div><small>Production goes ahead?</small><strong id="y4"></strong></div></div>
    <div class="verdict" id="yv"></div></div>
    <div><svg id="labL" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the factory's gain with the resident's damage and the range of payments both accept"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Which policy?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the answer in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((152, 152)) + '''  <div class="rw"><h3>Charges for plastic bags</h3><p>Several countries put a small charge on single-use plastic bags. It acts like a tax on the external cost of litter and waste, and use of bags fell sharply in many places.</p><div class="use"><b>Exam use:</b> a tax on a negative consumption externality. Evaluate: the charge may be far from the true external cost, and substitutes (thicker bags) may have costs of their own.</div></div>
  <div class="rw"><h3>Carbon pricing</h3><p>Some governments tax carbon emissions or run cap and trade schemes, so that the price of emitting reflects the damage that emissions cause.</p><div class="use"><b>Exam use:</b> internalising an external cost. Compare a tax (certain price, uncertain quantity) with permits (certain quantity, uncertain price).</div></div>
  <div class="rw"><h3>Neighbours who settle by agreement</h3><p>Disputes over noise or shared boundaries are sometimes settled by the parties themselves, perhaps with a payment. This works because few people are involved and rights are clear.</p><div class="use"><b>Exam use:</b> an alternative to government intervention, for the "only solved by government" style of question.</div></div>
'''
exam = '''
  <h2>Past paper questions on policies for externalities</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essay and data response questions asking how a government can deal with negative externalities and whether it must, plus Paper 3 multiple choice questions on policies and property rights. Mark scheme points are summarised in our own words, not copied. Tax incidence, permits and government failure are covered in syllabus 8.1.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>4</td><td>Feb/March 2023 (42); Oct/Nov 2023 (43); Oct/Nov 2024 (41, 43)</td></tr>
    <tr><td>Essay, 25 marks</td><td>2</td><td>Feb/March 2020 (42); Feb/March 2021 (42)</td></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>Feb/March 2022 (42)</td></tr>
    <tr><td>Data response parts</td><td>2</td><td>May/June 2020 (not sat); Oct/Nov 2021</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2022 to 2025</td></tr>
  </table></div>
  <h2>A · 20 and 25 mark essays</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((175, 187), (189, 192), (194, 197), (199, 202), (204, 207), (209, 212)) + '''
  <h2>B · A 13 mark question</h2>
''' + S.b((237, 240)) + '''
  <h2>C · Data response parts</h2>
  <details class="eq"><summary>Data response parts on reducing externalities</summary><div class="body"><ul>
    <li><b>May/June 2020 (not sat) · 42 · Q1(d) [7]:</b> consider how the negative externalities of concentrated industrial production can be reduced.</li>
    <li><b>Oct/Nov 2021 · 41 · Q1(d) [7]:</b> assess the effects on the social costs of transport of replacing diesel and petrol cars with all-electric cars.</li></ul></div></details>
  <h2>D · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips_html = tips([
  ("Match the policy to the failure:", "a tax equal to the external cost for negative externalities, a subsidy for positive ones. Use the words \"internalise the externality\"."),
  ("Draw the diagram with the tax or subsidy on it:", "shift MPC up to MSC (tax) or down (subsidy) and show the new output at the social optimum."),
  ("Always evaluate with measurement problems:", "the external cost is hard to value, so a tax may be too high or too low. Add elasticity, government failure and alternatives."),
  ("Consider non-government solutions.", "Property rights and bargaining, private action and persuasion are needed for \"only solved by government\" questions."),
  ("Compare two or more policies", "when asked for two. State which you think is better and why."),
  ("Test strong words:", "\"only\", \"necessarily\", \"all\". Show other causes and other solutions."),
], [
  ("Tax", "A tax equal to the external cost per unit would internalise the externality and move output to the socially efficient level."),
  ("Evaluate", "However, the external cost is difficult to measure, so a tax could be set too high or too low."),
  ("Bargaining", "If property rights are clear and few parties are involved, the polluter and the victim might bargain without government intervention."),
  ("Regulation", "Regulation could give more precise control over emissions but may be costly to monitor and enforce."),
]) + CMD(EVAL, DISC, CONS, EXPLAIN) + '  <h2>Flashcards</h2><div id="fc1"></div>\n'
js = HEAD + S.j_((76, 113)) + '''
/* ---------- Watch: bargaining ---------- */
const BB = 280, HB = (v) => v * 1.4;
function barDraw(s) {
  let o = SV.line(60, BB, 740, BB) + SV.text(62, 24, "$", "sm");
  const grp = (x, dmg, k, lab) => {
    let g = "";
    if (k.a > 0) g += SV.rect(x, BB - HB(100) * k.a, 90, HB(100) * k.a, "f3", op(k.a)) + SV.text(x + 45, BB - HB(100) - 8, "$100", "lbl bd", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 45, BB + 18, "Factory gain", "sm", { "text-anchor": "middle", ...op(k.a) }) +
      SV.rect(x + 110, BB - HB(dmg) * k.a, 90, HB(dmg) * k.a, "f2", op(k.a)) + SV.text(x + 155, BB - HB(dmg) - 8, "$" + dmg, "lbl bd", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 155, BB + 18, "Resident damage", "sm", { "text-anchor": "middle", ...op(k.a) }) + SV.text(x + 100, BB + 42, lab, "lbl bd", { "text-anchor": "middle", ...op(k.a) });
    if (k.r > 0) g += SV.rect(x + 205, BB - HB(100), 14, HB(100) - HB(dmg), "f1", op(k.r)) + SV.text(x + 226, BB - HB(80) + 4, "payments between $" + dmg + " and $100", "sm bd t1", { ...halo, ...op(k.r) });
    return g;
  };
  o += grp(70, 60, { a: s.a, r: s.r }, "Case A: damage $60");
  o += grp(430, 150, { a: s.b, r: 0 }, "Case B: damage $150");
  return o;
}
Lib.stepper($("#stCo"), { w: 780, h: 340, label: "A factory and a resident bargaining over pollution when the damage is smaller or larger than the factory's gain", base: { a: 0, r: 0, b: 0 }, draw: barDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Case A.</b> The factory gains <b>$100</b> from producing. The pollution does <b>$60</b> of damage to a resident. Production creates a net social gain of $40.", s: { a: 1 } },
  { cap: "<b>The resident holds the right to clean air.</b> The factory must pay to pollute. It will pay up to $100 and the resident will accept anything above $60, so a deal at any amount in between leaves <b>both better off</b>. For example $80 gives each a gain of $20.", s: { a: 1, r: 1 } },
  { cap: "<b>Case B.</b> Now the damage is <b>$150</b>, more than the factory's gain of $100. The resident would refuse any payment under $150, which the factory will not pay, so there is <b>no deal and the factory stops</b>. Again the outcome is efficient: production costs more than it is worth.", s: { a: 1, r: 1, b: 1 } },
  { cap: "<b>The catch.</b> This needs clear property rights, few people involved and low transaction costs. For pollution that affects thousands of people, negotiating is impractical, which is why governments often step in with taxes or regulation.", s: { a: 1, r: 1, b: 1 } },
] });

/* ---------- Lab 3: bargaining ---------- */
function lab8() {
  if (!$("#dmg") || !$("#gn")) return;
  const d = +$("#dmg").value, g = +$("#gn").value, deal = g > d;
  $("#y1").textContent = "$" + g; $("#y2").textContent = "$" + d; $("#y3").textContent = deal ? "$" + d + " to $" + g : "none"; $("#y4").textContent = deal ? "Yes" : "No";
  $("#yv").textContent = deal ? `The factory gains $${g} and the damage is $${d}, so there is room for a deal: any payment from $${d} to $${g} leaves both better off. Production goes ahead and the outcome is efficient (net gain $${g - d}).`
    : `The damage ($${d}) is at least the factory's gain ($${g}), so no payment satisfies both sides. The factory stops. This is also efficient, because production costs society more than it is worth.`;
  const H = (v) => 1.2 * v, base = 190;
  let o = SV.line(30, base, 400, base);
  [[60, g, "f3", "Factory gain"], [220, d, "f2", "Resident damage"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 210, l, "sm", { "text-anchor": "middle" }); });
  if (deal) o += SV.rect(165, base - H(g), 50, H(g) - H(d), "f1") + SV.text(190, base - H(g) - 24, "deal range", "sm bd t1", { "text-anchor": "middle" });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g13"), { id: "gn", label: "Factory's gain from producing ($): ", min: 50, max: 150, step: 10, value: 100, fmt: (v) => v, onInput: lab8 });
Lib.slider($("#g14"), { id: "dmg", label: "Damage to the resident ($): ", min: 0, max: 150, step: 10, value: 60, fmt: (v) => v, onInput: lab8 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which type of policy is each one?",
  buckets: [{ label: "Tax or subsidy" }, { label: "Regulation or ban" }, { label: "Information or persuasion" }, { label: "Property rights and bargaining" }, { label: "Tradable permits" }],
  items: [
    { text: "A per-flight tax on air travel", b: 0 }, { text: "A subsidy for electric cars", b: 0 }, { text: "A congestion charge", b: 0 },
    { text: "A limit on night flights", b: 1 }, { text: "Emission standards for factories", b: 1 }, { text: "A ban on smoking in public places", b: 1 },
    { text: "Negative advertising about flying", b: 2 }, { text: "Health warnings on cigarette packs", b: 2 },
    { text: "A resident and a factory agreeing a payment", b: 3 }, { text: "Giving a community ownership of a river", b: 3 },
    { text: "A cap on emissions with permits firms can trade", b: 4 },
  ], done: "Name the type, then weigh its costs and limits.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Internalise", "Make the decision-maker face the full social cost or benefit"],
  ["Tax equal to the external cost", "Shifts MPC up to MSC so output moves to the social optimum"],
  ["Subsidy equal to the external benefit", "Moves output up to the social optimum"],
  ["Property rights", "Legal ownership that lets people exclude others and be paid for use"],
  ["Transaction costs", "The costs of negotiating and enforcing an agreement"],
  ["Regulation", "Legal limits or bans on harmful activity"],
  ["Government failure", "Intervention that leaves resources less efficiently used"],
], done: "Seven words for policy on externalities." });
Lib.order($("#o1"), { prompt: "Put the analysis of a tax on air travel in order.", items: [
  "Airlines and passengers ignore the external cost of emissions and noise",
  "MSC is above MPC and the market overproduces flights at Qm",
  "A tax equal to the external cost per flight shifts MPC up to MSC",
  "The price rises and the number of flights falls to the social optimum Qs",
  "The welfare loss is removed and the externality is internalised",
  "Evaluate: the external cost is hard to measure, demand may be inelastic, and there may be effects on jobs and tourism",
], done: "A reliable structure for a 20 mark policy answer." });
Lib.calc($("#c1"), { qs: [
  { q: "The marginal external cost is $15 a unit. What per-unit tax would internalise it ($)?", a: 15, sol: "A tax equal to the marginal external cost: <b>$15</b>." },
  { q: "Demand is P = 100 − Q and MPC = 20 + 0.5Q. A tax of $15 shifts supply to 35 + 0.5Q. What is the new output (units, 1 decimal place)?", a: 43.3, tol: 0.1, sol: "100 − Q = 35 + 0.5Q gives Q = <b>43.3</b>, the social optimum." },
  { q: "What is the government's tax revenue ($, nearest whole number)?", a: 650, tol: 1, sol: "15 × 43.3 = <b>$650</b>." },
  { q: "The tax is set too high at $30. What is the output (units, 1 decimal place)?", a: 33.3, tol: 0.1, sol: "100 − Q = 50 + 0.5Q gives Q = <b>33.3</b>, below the social optimum of 43.3." },
  { q: "A positive externality of $15 and a subsidy of $15 raise output to 63.3 units. What is the subsidy cost ($, nearest whole number)?", a: 950, tol: 1, sol: "15 × 63.3 = <b>$950</b>." },
  { q: "A factory gains $100 from producing and the damage is $60. What is the largest net gain available to be shared between them ($)?", a: 40, sol: "100 − 60 = <b>$40</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A tax set equal to the marginal external cost will:", opts: ["raise output above the optimum", "internalise the externality", "remove all costs", "have no effect on price"], a: 1, why: "It makes the producer face the full social cost." },
  { q: "Which makes bargaining without government more likely to work?", opts: ["Thousands of people affected", "Clear property rights and few parties", "High transaction costs", "No identifiable polluter"], a: 1, why: "Few parties, clear rights and low transaction costs make a deal easy." },
  { q: "A tax is above the external cost. Output will be:", opts: ["above the social optimum", "at the social optimum", "below the social optimum", "unchanged"], a: 2, why: "It overcorrects and creates a new welfare loss." },
  { q: "Which is a weakness of a tax on pollution?", opts: ["It raises revenue", "The external cost is hard to measure so the tax may be wrong", "It changes prices", "It affects incentives"], a: 1, why: "Setting the right level needs information the government may not have." },
  { q: "Which policy gives the most precise control over emissions?", opts: ["Information campaign", "Regulation or a ban", "A small tax", "Nothing"], a: 1, why: "A legal limit sets the quantity directly, though enforcement costs money." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Internalise an externality", "Make the decision-maker bear the full social cost or gain the full social benefit."],
  ["Tax for a negative externality", "A per-unit tax equal to the marginal external cost shifts MPC up to MSC."],
  ["Subsidy for a positive externality", "A per-unit subsidy equal to the marginal external benefit moves output to the social optimum."],
  ["Regulation", "Legal limits, standards or bans."],
  ["Tradable permits", "A cap on pollution with permits that can be traded."],
  ["Property rights", "Legal ownership that lets owners control and charge for use."],
  ["Bargaining", "Parties agree a payment instead of relying on the government."],
  ["Transaction costs", "The costs of negotiating and enforcing an agreement."],
  ["Information failure (policy)", "The external cost cannot be measured accurately, so a tax may be wrong."],
  ["Government failure", "Intervention that makes the allocation of resources worse or no better."],
] });
''' + MCQ((232,), '''  { q: "[May/June 2025 · 31 · Q8] Good X is a popular product that creates a negative externality when it is consumed. The government wants to reduce the consumption of good X significantly. Under which circumstances is the government most likely to meet its aim?", opts: ["subsidy, price elasticity of demand more than 1", "subsidy, price elasticity of demand less than 1", "indirect tax, price elasticity of demand more than 1", "indirect tax, price elasticity of demand less than 1"], a: 2, why: "A tax raises price. Elastic demand (more than 1) means quantity falls by a larger percentage, so consumption falls significantly." },
  { q: "[May/June 2025 · 34 · Q10] Which policy by a government would increase the negative externalities that result from cigarette smoking?", opts: ["a ban on cigarette advertising", "a ban on cigarette smoking in public places", "a ban on substitutes for cigarettes", "a ban on the sale of cigarettes"], a: 2, why: "Banning substitutes keeps smokers buying cigarettes. A, B and D all aim to reduce smoking." },
  { q: "[May/June 2025 · 31 · Q10] To reduce traffic congestion, a government built a new highway. Some citizens responded by switching from public transport to private cars, which made car journeys take even longer. What can be concluded about government failure?", opts: ["It occurred because the government's opportunity costs were not considered.", "It occurred because the wishes of the majority of citizens were ignored.", "It occurred because the result was unintended.", "It occurred from over-reliance on the market system."], a: 2, why: "The extra traffic was an unintended consequence of the policy." },
  { q: "[Oct/Nov 2022 · 31 · Q15] Too many flights cause unnecessary damage to the environment. Which measure is most likely to result in the socially optimal number of flights?", opts: ["a complete ban on flights removing all private and external costs", "greater deregulation of the global airline industry", "publishing information to highlight the negative effects of flying on the environment", "the payment of a subsidy per passenger equal to the difference between the private and social benefit"], a: 2, why: "Information raises awareness of the external cost and moves choices towards the social optimum. A ban removes all flights, deregulation may increase them, and a subsidy raises flying." },
  { q: "[May/June 2025 · 32 · Q11] What is not an outcome of the existence of private property rights?", opts: ["They encourage private owners to conserve property when its value is expected to rise.", "They give private owners the incentive to manage their property carefully.", "They make private owners accountable for damage to others from property misuse.", "They prevent private owners gaining from using resources to benefit others."], a: 3, why: "Property rights let owners gain from using resources, including by benefiting others, so D is not an outcome." },
  { q: "[May/June 2025 · 34 · Q3] Why does the lack of property rights cause an inefficient allocation of resources?", opts: ["Scarce resources are depleted because the owner has sold them too cheaply.", "Scarce resources are depleted because they had zero cost to the users.", "Scarce resources are under-allocated to the provision of demerit goods.", "Scarce resources are under-allocated to the provision of merit goods."], a: 1, why: "If no one owns a resource, users pay nothing and it may be overused." },
''')
write("ex3", page(EY.format(3), "Policies for Externalities: Taxes, Subsidies, Regulation and Bargaining",
  "How a government can internalise an externality with a tax or subsidy, other policies such as regulation, permits and information, and when property rights and bargaining could work instead. Animated bargaining, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips_html), js,
  "Policies for Externalities", "policies-for-externalities")

# ---------------------------------------------------------------- 33.4
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b>Cost-benefit analysis (CBA)</b> counts all the private and external costs and benefits of a project, gives them money values and compares them. Because costs and benefits arrive at different times, future amounts are <b>discounted</b> to <b>present value</b>: <b>PV = future value ÷ (1 + r)<sup>t</sup></b>. The project is worth doing if the <b>net present value (NPV)</b>, the discounted benefits minus the discounted costs, is positive. CBA is useful but hard in practice, because external effects are hard to value and the answer depends on the discount rate.</p></div>
''' + S.b((60, 71)).replace("4 · Cost-benefit analysis (CBA)", "1 · Cost-benefit analysis (CBA)") + '''
  <h2>2 · Discounting step by step</h2>
  <p>A project costs $600 now and gives $120 a year of private benefit for ten years, with $36 a year of external cost. At a discount rate of 5%:</p>
  <ul>
    <li>$120 in year 1 is worth 120 ÷ 1.05 = $114.3 now; $120 in year 10 is worth 120 ÷ 1.05<sup>10</sup> = <b>$73.7</b> now. Later money counts for less.</li>
    <li>The present value of ten years of $120 is about <b>$927</b>, so <b>private NPV</b> = 927 − 600 = <b>+$327</b>.</li>
    <li>Net of external cost, the yearly benefit is $84, with present value about $649, so <b>social NPV</b> = 649 − 600 = <b>+$49</b>: still worth doing, but much less so.</li>
  </ul>
  <h2>3 · Decision rules</h2>
  <ul>
    <li><b>Single project:</b> go ahead if NPV is greater than zero.</li>
    <li><b>Several projects with a limited budget:</b> rank by NPV, or by the ratio of discounted benefits to discounted costs.</li>
    <li><b>The discount rate matters.</b> A higher rate shrinks distant benefits more, which favours projects with quick payoffs and can turn a positive NPV negative. Use the Watch and Explore tabs to see the sign flip.</li>
  </ul>
  <h2>4 · Difficulties in practice</h2>
  <ul>
    <li><b>Valuing intangibles:</b> noise, a view, national pride, a life saved. Any figure is open to argument.</li>
    <li><b>Forecasting:</b> costs often overrun and future benefits are uncertain.</li>
    <li><b>Choosing the discount rate</b> can decide the result.</li>
    <li><b>Distribution:</b> a positive net benefit hides who gains and who loses.</li>
    <li><b>Judgement:</b> a project with a positive NPV may still not go ahead if money is limited or other projects have a better return.</li>
  </ul>
'''
watch = '''
  <h2>1 · Cost-benefit analysis over ten years</h2>
  <p>A project costs $600 now. It gives $120 of private benefit a year and causes $36 a year of external cost. The discount rate is 5%.</p><div id="stC"></div>
  <h2>2 · The discount rate can change the decision</h2>
  <p>The same project, the social NPV at different discount rates. Press Play, or click the steps.</p><div id="stR"></div>
'''
explore = S.b((113, 118)).replace("Lab 3 · Is", "Lab 1 · Is") + '''
  <h2>Lab 2 · Present value</h2>
  <p>What is a future payment worth today? Set the amount, the number of years and the discount rate.</p>
  <div class="card"><div class="grid2"><div><div id="g15"></div><div id="g16"></div><div id="g17"></div>
    <div class="readout"><div><small>Present value</small><strong id="z1"></strong></div><div><small>Value lost to discounting</small><strong id="z2"></strong></div></div>
    <div class="verdict" id="zv"></div></div>
    <div><svg id="labM" viewBox="0 0 420 270" role="img" aria-label="Curve of present value falling with the number of years"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Easy or hard to value in money?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the CBA steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = NOTE + S.b((156, 156)) + '''  <div class="rw"><h3>A new railway line</h3><p>A rail project has large construction costs and benefits that arrive over decades: time saved, fewer car journeys, more jobs near stations, but also noise and land use. CBA adds these up and discounts the future ones.</p><div class="use"><b>Exam use:</b> a project with long-term benefits. A high discount rate may make it look less attractive.</div></div>
  <div class="rw"><h3>Hosting a major sports event</h3><p>A stadium for a major event has high private and external costs, and benefits that are hard to value, such as national pride and the use of the stadium afterwards.</p><div class="use"><b>Exam use:</b> a Paper 3 question asked why CBA of a stadium is difficult: valuing national pride is hard.</div></div>
  <div class="rw"><h3>A bridge to an island</h3><p>A bridge cuts travel time and may raise incomes on the island, but ferry workers may lose their jobs and carbon emissions may rise.</p><div class="use"><b>Exam use:</b> a Paper 3 question asked what could be included in a CBA of a bridge: all of these, both costs and benefits.</div></div>
'''
exam = '''
  <h2>Past paper questions on cost-benefit analysis</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the written questions on CBA, a practice question with a model answer and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 25 marks</td><td>1</td><td>Oct/Nov 2022 (41)</td></tr>
    <tr><td>Essay part, 12 marks</td><td>1</td><td>Oct/Nov 2022 (43)</td></tr>
    <tr><td>Data response part, 4 marks</td><td>1</td><td>Feb/March 2020 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>6 shown below</td><td>2020 to 2024</td></tr>
  </table></div>
  <h2>A · Written questions</h2>
''' + S.b((214, 217), (235, 235)) + '''
  <details class="eq"><summary>Data response part on CBA</summary><div class="body"><ul>
    <li><b>Feb/March 2020 · 42 · Q1(b) [4]:</b> explain two merits of using cost-benefit analysis before a major public sector investment.</li></ul></div></details>
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">12 marks</span> Explain what is meant by discounting in cost-benefit analysis and why it matters when deciding whether to build a new hospital.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define CBA and present value. Show the formula or an example. Apply to a hospital with costs now and benefits for many years. Evaluate the effect of the discount rate and the difficulty of valuing health benefits.</div>
''' + key() + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">Cost-benefit analysis compares all the private and external costs and benefits of a project in money terms. Discounting converts future costs and benefits to present value, using present value = future value ÷ (1 + r)<sup>t</sup>, because money received later is worth less than money received now.</span></p>
    <p><span class="mk a" data-t="A">A hospital has a large cost when it is built, but its benefits, such as better health, fewer working days lost and jobs, may arrive over many decades.</span> <span class="mk n" data-t="N">Without discounting, distant benefits would count as much as present costs. With a discount rate of 5%, a benefit of $100 in 20 years has a present value of about $38, so later benefits count for much less. If the net present value of the discounted benefits minus the costs is positive, the project is worth doing.</span></p>
    <p><span class="mk e" data-t="E">The choice of discount rate could change the decision: a higher rate would reduce the value of long-term health benefits and could make the NPV negative. Valuing health, wildlife and traffic effects in money is also difficult. Overall, CBA is likely to be a useful guide but not the only factor, because the result depends on assumptions that are open to challenge.</span></p></div>
  </div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips_html = tips([
  ("For CBA, say all costs and benefits, money values and discounting.", "Then give the difficulties."),
  ("Write the formula:", "PV = future value ÷ (1 + r)<sup>t</sup>. Say that NPV above zero means go ahead."),
  ("Include the external effects.", "A private NPV can be positive and the social NPV negative once pollution or congestion is counted."),
  ("Test the discount rate.", "A higher rate cuts long-term benefits more, which can reverse the decision."),
  ("Give distribution as an evaluation point:", "a positive net benefit does not show who gains and who loses."),
  ("Apply to the case.", "A hospital, airport or road has particular costs and benefits. Name them."),
], [
  ("Define", "Cost-benefit analysis is a method of comparing the total discounted social costs and benefits of a project to decide whether it is worthwhile."),
  ("Discounting", "Future benefits are discounted because money received later is worth less than money received now."),
  ("Evaluate", "However, the choice of discount rate could change whether the net present value is positive."),
  ("Valuation", "External costs such as noise and loss of countryside are difficult to value in money, so the result may be open to challenge."),
]) + CMD(EXPLAIN, EVAL, ("Consider why", "Give reasons and judge how strong they are.")) + '  <h2>Flashcards</h2><div id="fc1"></div>\n'
js = HEAD + S.j_((51, 74)) + S.j_((115, 129)) + '''
/* ---------- Watch 2: discount rate ---------- */
const AF = (r) => { let a = 0; for (let t = 1; t <= 10; t++) a += 1 / (1 + r) ** t; return a; };
function rateDraw(s) {
  const base = 190, H = (v) => v * 0.8, bw = 90;
  let o = SV.line(60, base, 740, base) + SV.text(62, 24, "Social NPV ($)", "sm");
  [[0.02, 90], [0.05, 230], [0.08, 370], [0.1, 510]].forEach(([r, x], i) => {
    const k = s["b" + i] || 0; if (k <= 0) return;
    const v = 84 * AF(r) - 600, up = v >= 0, h = H(Math.abs(v)) * k;
    o += SV.rect(x, up ? base - h : base, bw, h, up ? "f3" : "f2", op(k)) + SV.text(x + bw / 2, up ? base - h - 8 : base + h + 16, (up ? "+" : "−") + Lib.fmtN(Math.abs(v), 0), "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + bw / 2, 296, "r = " + Math.round(r * 100) + "%", "lbl bd", { "text-anchor": "middle", ...op(k) });
  });
  return o;
}
Lib.stepper($("#stR"), { w: 780, h: 320, label: "Social net present value of the same project at four discount rates", base: { b0: 0, b1: 0, b2: 0, b3: 0 }, draw: rateDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The project.</b> Cost $600 now, benefits $120 a year for ten years, external cost $36 a year. The only thing that changes below is the <b>discount rate</b>.", s: {} },
  { cap: "<b>At 2%</b> the future counts for a lot. Social NPV is about <b>+$155</b>: go ahead.", s: { b0: 1 } },
  { cap: "<b>At 5%</b> social NPV falls to about <b>+$49</b>. Still positive, but only just.", s: { b0: 1, b1: 1 } },
  { cap: "<b>At 8%</b> distant benefits shrink further and social NPV turns <b>negative, about −$36</b>. The project should not go ahead.", s: { b0: 1, b1: 1, b2: 1 } },
  { cap: "<b>At 10%</b> the NPV is about <b>−$84</b>. The same project, the same costs and benefits, but the decision flips. This is why the choice of discount rate is a key criticism of CBA.", s: { b0: 1, b1: 1, b2: 1, b3: 1 } },
] });

/* ---------- Lab 2: present value ---------- */
function labPV() {
  if (!$("#pva") || !$("#pvt") || !$("#pvr")) return;
  const a = +$("#pva").value, t = +$("#pvt").value, r = +$("#pvr").value / 100, pv = a / (1 + r) ** t;
  $("#z1").textContent = "$" + Lib.fmtN(pv, 0); $("#z2").textContent = Math.round((1 - pv / a) * 100) + "%";
  $("#zv").textContent = t === 0 || r === 0 ? "With no waiting or a zero rate, there is no discounting: the present value equals the amount."
    : `$${a} received in ${t} years is worth $${Lib.fmtN(pv, 0)} today at ${Math.round(r * 100)}%. Waiting costs ${Math.round((1 - pv / a) * 100)}% of the value. The longer the wait and the higher the rate, the smaller the present value.`;
  const x = (v) => 50 + v * 11.5, y = (v) => 235 - 200 * v / 1000;
  let o = SV.line(50, 235, 395, 235) + SV.line(50, 235, 50, 20) + SV.text(392, 258, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Present value ($)", "sm");
  const pts = []; for (let k = 0; k <= 30; k++) pts.push([x(k), y(a / (1 + r) ** k)]);
  o += SV.path(ptsPath(pts), "c1") + SV.line(x(t), y(pv), x(t), 235, "gr") + SV.line(50, y(pv), x(t), y(pv), "gr") + SV.circle(x(t), y(pv), 6, "dot1") + SV.text(x(t) + 8, y(pv) - 8, "$" + Lib.fmtN(pv, 0), "lbl bd", { ...halo });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g15"), { id: "pva", label: "Future amount ($): ", min: 200, max: 1000, step: 100, value: 1000, fmt: (v) => v, onInput: labPV });
Lib.slider($("#g16"), { id: "pvt", label: "Years until it is received: ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labPV });
Lib.slider($("#g17"), { id: "pvr", label: "Discount rate: ", min: 0, max: 12, step: 1, value: 5, fmt: (v) => v + "%", onInput: labPV });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "In a CBA of a new airport, which items are easy to value in money and which are hard?",
  buckets: [{ label: "Easier to value" }, { label: "Hard to value" }],
  items: [
    { text: "Construction cost of the terminal", b: 0 }, { text: "Landing fees and ticket revenue", b: 0 }, { text: "Wages of airport staff", b: 0 }, { text: "Cost of buying the land", b: 0 },
    { text: "Noise for people living nearby", b: 1 }, { text: "Loss of countryside and wildlife", b: 1 }, { text: "Time saved by passengers", b: 1 }, { text: "Effect on local climate and health", b: 1 },
  ], done: "Prices exist for market items. External effects need estimates, which is the main weakness of CBA.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Cost-benefit analysis", "Counting all private and external costs and benefits of a project in money terms"],
  ["Discounting", "Converting future amounts to present value"],
  ["Present value", "What a future amount is worth today"],
  ["Net present value", "Discounted benefits minus discounted costs"],
  ["Discount rate", "The rate used to reduce the value of future amounts"],
  ["Social NPV", "NPV after including external costs and benefits"],
  ["Opportunity cost of funds", "What else the money could have achieved"],
], done: "Seven words for CBA." });
Lib.order($("#o1"), { prompt: "Put the steps of a cost-benefit analysis in order.", items: [
  "Identify the private costs and benefits of the project",
  "Identify the external costs and benefits",
  "Give each a money value, using estimates where needed",
  "Discount future amounts to present values",
  "Calculate the net present value",
  "Decide, and evaluate the difficulties and the effect of the discount rate",
], done: "A reliable structure for a CBA answer." });
Lib.calc($("#c1"), { qs: [
  { q: "A benefit of $110 arrives in one year. The discount rate is 10%. What is its present value ($)?", a: 100, sol: "110 ÷ 1.10 = <b>$100</b>." },
  { q: "A payment of $1,000 arrives in two years. The discount rate is 10%. What is its present value ($, nearest whole number)?", a: 826, tol: 1, sol: "1,000 ÷ 1.21 = <b>$826</b>." },
  { q: "A project costs $500 now and has a present value of benefits of $540. What is the NPV ($)?", a: 40, sol: "540 − 500 = <b>+$40</b>: go ahead." },
  { q: "The same project has external costs with a present value of $70. What is the social NPV ($)?", a: -30, sol: "40 − 70 = <b>−$30</b>: not worthwhile once external costs are counted." },
  { q: "A project has private cost 400, private benefit 440, social cost 450 and social benefit 480. What is the net external cost ($ million)?", a: 10, hint: "External cost = social cost − private cost. External benefit = social benefit − private benefit.", sol: "External cost 50, external benefit 40, so net external cost is <b>$10 million</b>." },
  { q: "Present value of benefits is $800 and of costs is $600. What is the ratio of discounted benefits to costs (1 decimal place)?", a: 1.3, tol: 0.05, sol: "800 ÷ 600 = <b>1.3</b>. Above 1 means NPV is positive." },
] });
Lib.quiz($("#qz1"), { qs: [
''' + S.j_((198, 198)) + '''  { q: "Why are future benefits discounted?", opts: ["Because they are certain", "Because money received later is worth less than money now", "Because costs always come first", "Because external costs are small"], a: 1, why: "A dollar now can be used or invested, so a dollar later has a lower present value." },
  { q: "A higher discount rate will usually:", opts: ["raise the value of benefits many years away", "reduce the value of benefits many years away", "have no effect on NPV", "remove external costs"], a: 1, why: "Distant amounts are divided by a larger number." },
  { q: "A project has a positive private NPV but a negative social NPV. What does this suggest?", opts: ["It is worth doing for everyone", "External costs outweigh the private gain", "The discount rate is zero", "Costs are underestimated"], a: 1, why: "Counting external costs turns the net benefit negative." },
  { q: "Which is a limitation of CBA?", opts: ["It ignores externalities", "It cannot compare projects", "External effects are hard to value in money", "It shows who gains and loses"], a: 2, why: "Valuing noise, health or a view involves estimates and judgement." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Cost-benefit analysis", "A method of valuing all private and external costs and benefits of a project over time."],
  ["Discounting", "Converting future amounts to present value."],
  ["Present value", "Future value ÷ (1 + r)^t."],
  ["Net present value", "Present value of benefits minus present value of costs. Go ahead if positive."],
  ["Social NPV", "NPV including external costs and benefits."],
  ["Private NPV", "NPV counting only the costs and benefits to the owner."],
  ["Discount rate", "The rate used to reduce the value of future amounts."],
  ["Intangibles", "Effects with no market price, such as noise or a view."],
  ["Distribution", "Who gains and who loses, which CBA totals can hide."],
  ["Benefit-cost ratio", "Discounted benefits divided by discounted costs."],
] });
''' + MCQ((), '''  { q: "[Feb/March 2023 · 32 · Q9] The result of a cost-benefit analysis of a proposed government road-building project is that there will be a positive net social benefit of $50 million. Why might the government not proceed with the project?", opts: ["The project would not be profitable for a private firm.", "The project would cause negative externalities.", "There is limited capital available for government projects.", "There would be more who lost than gained."], a: 2, why: "A positive NPV does not guarantee funding: the government may have limited capital and better uses for it." },
  { q: "[Oct/Nov 2020 · 31 · Q1] What is the main aim of cost-benefit analysis?", opts: ["to allow firms to maximise their private benefit and minimise the external cost", "to equate total social benefit to the total social cost of a project", "to find the correct level of direct tax to internalise the external cost of a project", "to find the highest positive difference between total benefit and total cost"], a: 3, why: "CBA looks for the net benefit (benefit minus cost) to society. B describes zero net benefit." },
  { q: "[Oct/Nov 2022 · 32 · Q3] What could be included in a cost-benefit analysis of a project to build a road bridge connecting an island community to the mainland? (a fall in employment for ferry services, an increase in carbon emissions, a reduction in travel time for work, an increase in incomes for the community)", opts: ["yes, no, no, yes", "yes, yes, no, no", "yes, yes, yes, yes", "no, no, yes, yes"], a: 2, why: "CBA counts all costs and benefits, so all four effects are included." },
  { q: "[Oct/Nov 2023 · 33 · Q9] Which conditions are most likely to reduce the accuracy of cost-benefit analysis in decision making?", opts: ["a high proportion of external costs and benefits, and a high share of total costs and benefits in the future", "a high proportion of external costs and benefits, and a low share in the future", "a low proportion of external costs and benefits, and a high share in the future", "a low proportion of external costs and benefits, and a low share in the future"], a: 0, why: "External effects are hard to value and distant amounts are uncertain and sensitive to the discount rate, so both together reduce accuracy." },
  { q: "[May/June 2023 · 32 · Q12] A government hopes to build an athletics stadium to hold the World Games. The stadium would have high private and external costs, but it would increase national pride. Why would it be difficult to use cost-benefit analysis to decide whether to build the stadium?", opts: ["The materials needed to build the stadium will need to be imported.", "The external costs of clearing land for building will outweigh the private costs.", "The stadium will not be used much for athletics after the World Games.", "The valuation of national pride will be complex to assess."], a: 3, why: "National pride has no market price, so valuing it is hard." },
  { q: "[Oct/Nov 2024 · 32 · Q11] What is not a valid comment economists may make regarding the need to subsidise a green energy market that uses solar and wind power?", opts: ["It is cheaper to use the plentiful supply of coal.", "Markets will become more efficient.", "The value of the positive externalities cannot be estimated.", "The value of the negative externalities cannot be estimated."], a: 1, why: "Claiming that markets will become more efficient is not a valid comment on the need for the subsidy. A, C and D are valid points about the cost of coal and the difficulty of measuring externalities." },
''')
write("ex4", page(EY.format(4), "Cost-Benefit Analysis",
  "Counting all the private and external costs and benefits of a project, discounting future amounts to present value, using net present value as the decision rule, and why the discount rate and valuation make CBA hard. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips_html), js,
  "Cost-Benefit Analysis", "cost-benefit-analysis")
