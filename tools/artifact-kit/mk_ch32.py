"""Builds the three ch32 part pages (ef1..ef3) from slices of ef.* plus new content. Run: python3 tools/artifact-kit/mk_ch32.py"""
from splitter import *
mktips = tips
S = Src("ef")
HEAD = S.j_((1, 7))
EY = "A Level Economics · 9708 · Syllabus 7.3 · Part {} of 3"
TAILNOTE = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'

# ------------------------------------------------------------------ 32.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Resources are scarce, so economists ask whether they are used efficiently, and there are several kinds of efficiency. <b>Productive efficiency</b> means output at the lowest possible average cost (the minimum of the AC curve, or on the production possibility curve). <b>Dynamic efficiency</b> means costs that fall over time through investment and innovation, while <b>X-inefficiency</b> means costs above the minimum because there is no pressure to control them. <b>Pareto efficiency</b> is the strictest test: no one can be made better off without making someone else worse off.</p></div>
''' + S.b((25, 34)) + '''
  <h2>2 · Measuring X-inefficiency</h2>
  <p>A firm's lowest possible average cost is $10 but it actually produces at $12. Its X-inefficiency is $2 a unit, or 20% above the minimum. A firm with competitors has an incentive to close the gap, because rivals with lower costs could undercut it. A sole supplier protected by barriers to entry has less pressure, so costs may drift up.</p>
  <h2>3 · Pareto improvements</h2>
  <p>A <b>Pareto improvement</b> is a change that makes at least one person better off and nobody worse off. When no such change remains, the economy is Pareto efficient. A move from inside the production possibility curve to a point on it can be a Pareto improvement, because more of both goods is possible. Most real policies make some people worse off, so they are not strict Pareto improvements, although the gainers might compensate the losers.</p>
  <div class="tip"><b class="h">Pareto and equity</b>A Pareto efficient outcome can be very unequal. Efficiency says nothing about fairness, which is why equity is covered separately (syllabus 8.2).</div>
'''
watch = '''
  <h2>1 · One firm: perfect competition and monopoly</h2>
  <p>Same costs (TC = 600 + 20Q + 0.25Q²). How efficient is each market structure? Press Play, or click the steps.</p><div id="stB"></div>
  <h2>2 · Pareto improvements on the production possibility curve</h2>
  <p>Moving from a point inside the curve to one on it: who gains?</p><div id="stC"></div>
'''
explore = S.b((94, 106)).replace("Lab 2 ·", "Lab 1 ·").replace("Lab 3 ·", "Lab 2 ·") + '''
  <h2>Lab 3 · Is it a Pareto improvement?</h2>
  <p>A policy changes the satisfaction of two people, A and B. Set the changes and check whether it passes the Pareto test.</p>
  <div class="card"><div class="grid2"><div><div id="g7"></div><div id="g8"></div>
    <div class="readout"><div><small>Change for A</small><strong id="p1"></strong></div><div><small>Change for B</small><strong id="p2"></strong></div><div><small>Total</small><strong id="p3"></strong></div><div><small>Pareto improvement?</small><strong id="p4"></strong></div></div>
    <div class="verdict" id="pv"></div></div>
    <div><svg id="labS" viewBox="0 0 420 260" role="img" aria-label="Bars showing the change in satisfaction for persons A and B"></svg></div></div></div>
'''
practise = S.b((118, 119)) + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = TAILNOTE + S.b((142, 142), (145, 145)) + '''  <div class="rw"><h3>A fall in unemployment</h3><p>When people who want to work are idle, the economy is inside its production possibility curve. Helping them into jobs can make them better off at no cost to anyone else, which is close to a Pareto improvement.</p><div class="use"><b>Exam use:</b> a move from inside the PPC to the PPC.</div></div>
'''
exam = '''
  <h2>Past paper questions on types of efficiency</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essay parts on efficiency, dynamic efficiency and Pareto optimality, a data response part, and Paper 3 multiple choice questions. The June 2020 papers were not sat. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay parts, 12 or 13 marks</td><td>4</td><td>May/June 2021 (42); Feb/March 2022 (42); Oct/Nov 2020 (43); Oct/Nov 2022 (43)</td></tr>
    <tr><td>Data response part, 5 marks</td><td>1</td><td>May/June 2021 (41, 43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2021 to 2024</td></tr>
  </table></div>
  <h2>A · 12 and 13 mark questions</h2>
''' + KEYL + S.b((207, 211), (225, 228), (230, 233), (235, 238), (247, 247)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (258, 259), '''    <li><b>Say how each type differs:</b> productive efficiency is about cost, allocative about what is produced, dynamic about change over time, and Pareto about any possible reallocation.</li>
''', (272,)) + cmd(CW["explain"], CW["consider"], CW["discuss"]) + FC
js = HEAD + S.j_((31, 75)) + S.j_((92, 123)) + '''
/* ---------- Lab 3: Pareto test ---------- */
function labPar() {
  if (!$("#da") || !$("#db")) return;
  const a = +$("#da").value, b = +$("#db").value, t = a + b, imp = a >= 0 && b >= 0 && (a > 0 || b > 0);
  $("#p1").textContent = (a > 0 ? "+" : a < 0 ? "−" : "") + Math.abs(a); $("#p2").textContent = (b > 0 ? "+" : b < 0 ? "−" : "") + Math.abs(b); $("#p3").textContent = (t > 0 ? "+" : t < 0 ? "−" : "") + Math.abs(t); $("#p4").textContent = imp ? "Yes" : a === 0 && b === 0 ? "No change" : "No";
  $("#pv").textContent = a === 0 && b === 0 ? "Nothing changes, so the allocation is unchanged."
    : imp ? "Nobody is worse off and at least one person is better off: this is a Pareto improvement."
    : t > 0 ? "One person loses, so it is not a Pareto improvement, even though the total gain is positive. If the winner compensated the loser and still gained, it might count as a potential Pareto improvement."
    : "One person loses and the total is not positive: society is no better off.";
  const H = (v) => 7 * v, base = 130;
  let o = SV.line(30, base, 400, base);
  [[80, a, "Person A"], [240, b, "Person B"]].forEach(([x, v, l]) => { const up = v >= 0; o += SV.rect(x, up ? base - H(v) : base, 90, Math.abs(H(v)), up ? "f3" : "f2") + SV.text(x + 45, up ? base - H(v) - 8 : base + Math.abs(H(v)) + 16, (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labS").innerHTML = o;
}
Lib.slider($("#g7"), { id: "da", label: "Change in A's satisfaction: ", min: -10, max: 10, step: 1, value: 4, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labPar });
Lib.slider($("#g8"), { id: "db", label: "Change in B's satisfaction: ", min: -10, max: 10, step: 1, value: -2, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labPar });

/* ---------- Practise ---------- */
''' + S.j_((140, 150)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Productive efficiency", "Output at the lowest possible average cost"],
  ["Dynamic efficiency", "Falling costs over time from investment and innovation"],
  ["X-inefficiency", "Costs above the minimum because of weak competitive pressure"],
  ["Pareto efficiency", "No reallocation can make someone better off without making someone worse off"],
  ["Pareto improvement", "A change that makes someone better off and no one worse off"],
  ["Static efficiency", "Efficiency at one point in time"],
  ["Production possibility curve", "The maximum combinations of two goods an economy can produce"],
], done: "Seven words for the types of efficiency." });
''' + calc(S, (185, 187), '''  { q: "A firm's lowest possible average cost is $8 but it produces at $10. By what percentage is it above the minimum?", a: 25, sol: "(10 − 8) ÷ 8 × 100 = <b>25%</b>." },
  { q: "Unit cost is $100 and falls 5% a year through investment. What is it after 2 years ($, 2 decimal places)?", a: 90.25, tol: 0.01, sol: "100 × 0.95 × 0.95 = <b>$90.25</b>." },
''') + qz(S, (191, 192, 195), '''  { q: "A policy gives person A +5 and person B −2. This is:", opts: ["a Pareto improvement", "not a Pareto improvement, because B loses", "always desirable", "always inefficient"], a: 1, why: "A Pareto improvement requires that nobody loses." },
''') + cards(S, (198, 199, 200, 201, 202, 203, 204)) + mcq(S, (217, 218, 219, 222, 224, 225, 227))
write("ef1", page(EY.format(1), "Types of Efficiency: Productive, Dynamic, X-Inefficiency and Pareto",
  "Productive, dynamic and Pareto efficiency and X-inefficiency: what each means, how it is measured and how the production possibility curve shows Pareto improvements. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Types of Efficiency: Productive, Dynamic, X-Inefficiency and Pareto", "types-of-efficiency")

# ------------------------------------------------------------------ 32.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b>Allocative efficiency</b> means resources go to the goods consumers want most, which happens where <b>price equals marginal cost</b> (or, with externalities, <b>MSB = MSC</b>). At that output <b>total surplus</b> (consumer surplus plus producer surplus) is as large as possible, and any other output creates a <b>welfare loss</b>. Perfect competition is the benchmark: in the long run it produces at P = MC and at the minimum of average cost. A monopoly sets MR = MC, charges a price above MC and produces less than the efficient output, so it is allocatively inefficient, though it may gain from economies of scale and invest more.</p></div>
''' + S.b((36, 42)).replace("2 · The picture", "1 · The picture") + '''
  <h2>2 · Efficiency in different market structures</h2>
''' + S.b((45, 52)) + '''
  <h2>3 · Monopoly in numbers</h2>
  <p>Demand is P = 100 − Q and marginal cost is 20 + 0.5Q. The efficient output is where P = MC: <b>53.3 units</b> at $46.7. A monopolist sets MR = MC: 100 − 2Q = 20 + 0.5Q, so <b>Q = 32</b> at a price of <b>$68</b>. Output is 21 units lower and price is higher, and the triangle between demand and marginal cost over those units is the welfare loss.</p>
  <div class="tip"><b class="h">Do not say monopoly is always bad</b>A monopoly can use economies of scale to keep average cost low, may reinvest supernormal profit (dynamic efficiency) and may be contestable. Regulation or competition policy can reduce the price. Weigh these in evaluation.</div>
'''
watch = '''
  <h2>1 · Allocative efficiency and the welfare loss</h2>
  <p>Demand P = 100 − Q, marginal cost = 20 + 0.5Q. Press Play, or click the steps.</p><div id="stA"></div>
'''
explore = S.b((87, 92)) + '''
  <h2>Lab 2 · Surplus at different prices</h2>
  <p>Set the price. Only the smaller of the quantity demanded and supplied is traded, so a price away from the equilibrium cuts total surplus. Demand is P = 100 − Q and supply is P = 20 + 0.5Q.</p>
  <div class="card"><div class="grid2"><div><div id="g9"></div>
    <div class="readout"><div><small>Quantity traded</small><strong id="k1"></strong></div><div><small>Consumer surplus</small><strong id="k2"></strong></div><div><small>Producer surplus</small><strong id="k3"></strong></div><div><small>Total surplus</small><strong id="k4"></strong></div></div>
    <div class="verdict" id="kv"></div></div>
    <div><svg id="labT" viewBox="0 0 420 300" role="img" aria-label="Supply and demand at a chosen price with consumer and producer surplus shaded"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Put the monopoly argument in order</h2><div id="o1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = TAILNOTE + S.b((141, 141)) + '''  <div class="rw"><h3>A farmers' market and a corner shop monopoly</h3><p>In a market with many sellers of similar produce, price is pushed towards the cost of supply. A single shop on a remote island can charge more, because buyers have few alternatives.</p><div class="use"><b>Exam use:</b> competition keeps price near marginal cost, while a monopoly can charge more and sell less.</div></div>
  <div class="rw"><h3>Competition authorities and mergers</h3><p>When two large firms propose to merge, regulators ask whether the merged firm could raise prices. They weigh a possible rise in price against cost savings from a larger scale.</p><div class="use"><b>Exam use:</b> evaluating monopoly: allocative inefficiency against economies of scale.</div></div>
'''
exam = '''
  <h2>Past paper questions on allocative efficiency</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays on perfect competition, monopoly and allocative efficiency, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>2</td><td>May/June 2024 (41, 43); May/June 2023 (41, 43)</td></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>Feb/March 2021 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>3 shown below</td><td>2022 to 2025</td></tr>
  </table></div>
  <h2>A · Essays</h2>
''' + KEYL + S.b((164, 176), (183, 186), (215, 223)) + '''
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (260, 261, 262), '', (271, 273)) + cmd(CW["explain"], CW["evaluate"], CW["consider"]) + FC
js = HEAD + S.j_((8, 30), (76, 91)) + '''
/* ---------- Lab 2: surplus at a price ---------- */
function labSur() {
  if (!$("#pr")) return;
  const p = +$("#pr").value, qd = 100 - p, qs = Math.max(0, 2 * (p - 20)), q = Math.min(qd, qs), cs = 100 * q - q * q / 2 - p * q, ps = p * q - 20 * q - q * q / 4, ts = cs + ps, mx = TSF(QS);
  $("#k1").textContent = Lib.fmtN(q, 1); $("#k2").textContent = Lib.fmtN(cs, 0); $("#k3").textContent = Lib.fmtN(ps, 0); $("#k4").textContent = Lib.fmtN(ts, 0) + " (" + Math.round(ts / mx * 100) + "% of max)";
  $("#kv").textContent = Math.abs(p - PS) < 0.8 ? "At the equilibrium price the quantity traded is 53.3 and total surplus is at its maximum of about " + Lib.fmtN(mx, 0) + ": allocative efficiency."
    : p < PS ? `At $${p} consumers want ${Lib.fmtN(qd, 1)} but firms supply only ${Lib.fmtN(qs, 1)}, so only ${Lib.fmtN(q, 1)} are traded. Total surplus falls to ${Math.round(ts / mx * 100)}% of the maximum: units worth more than they cost are not made.`
    : `At $${p} firms supply ${Lib.fmtN(qs, 1)} but consumers buy only ${Lib.fmtN(qd, 1)}, so only ${Lib.fmtN(q, 1)} are traded. Total surplus falls to ${Math.round(ts / mx * 100)}% of the maximum.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "$", "sm");
  o += SV.poly([[x(0), y(100)], [x(q), y(100 - q)], [x(q), y(p)], [x(0), y(p)]], "f1", { opacity: 0.55 }) + SV.poly([[x(0), y(p)], [x(q), y(p)], [x(q), y(20 + 0.5 * q)], [x(0), y(20)]], "f4", { opacity: 0.55 });
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(70), "c2") + SV.line(40, y(p), 400, y(p), "gr", { "stroke-width": 2.5 }) + SV.text(x(100) - 4, y(0) - 6, "D", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(70) + 16, "S = MC", "sm bd t2", { "text-anchor": "end" });
  o += SV.text(x(q / 4) + 4, y((100 + p) / 2) + 4, "CS", "lbl bd t1", { "text-anchor": "middle" }) + SV.text(x(q / 4) + 4, y((20 + p) / 2) + 4, "PS", "lbl bd t3", { "text-anchor": "middle" });
  $("#labT").innerHTML = o;
}
Lib.slider($("#g9"), { id: "pr", label: "Price ($): ", min: 30, max: 90, step: 1, value: 60, fmt: (v) => v, onInput: labSur });

/* ---------- Practise ---------- */
''' + S.j_((172, 179)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Allocative efficiency", "Resources go to the goods consumers want most: P = MC"],
  ["Consumer surplus", "What consumers would pay minus what they do pay"],
  ["Producer surplus", "What producers receive minus the cost of supplying"],
  ["Total surplus", "Consumer surplus plus producer surplus"],
  ["Welfare loss", "The loss of total surplus when output is not the efficient output"],
  ["Monopoly", "A single seller that can set price above marginal cost"],
  ["Economies of scale", "Average cost falls as output rises"],
], done: "Seven words for allocative efficiency." });
''' + calc(S, (181, 182, 183, 184), '''  { q: "Demand is P = 100 − Q and MC = 20 + 0.5Q. What is the allocatively efficient output (units, 1 decimal place)?", a: 53.3, tol: 0.1, sol: "100 − Q = 20 + 0.5Q gives Q = <b>53.3</b>." },
  { q: "A monopolist in that market sets MR = MC, with MR = 100 − 2Q. What output does it produce (units)?", a: 32, sol: "100 − 2Q = 20 + 0.5Q gives 2.5Q = 80, so Q = <b>32</b>." },
''') + qz(S, (190,), '''  { q: "Total surplus is greatest where:", opts: ["price equals marginal cost", "profit is greatest", "demand is inelastic", "average cost is rising"], a: 0, why: "At P = MC every unit worth more than it costs is produced." },
  { q: "Compared with perfect competition, a monopoly produces:", opts: ["more output at a lower price", "less output at a higher price", "the same output", "more output at a higher price"], a: 1, why: "It restricts output to raise price." },
''') + cards(S, (205, 206, 199)) + mcq(S, (221, 223, 226))
write("ef2", page(EY.format(2), "Allocative Efficiency, Welfare Loss and Market Structures",
  "Allocative efficiency at P = MC, consumer and producer surplus, the welfare loss from monopoly and how efficiency differs across market structures. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Allocative Efficiency, Welfare Loss and Market Structures", "allocative-efficiency-welfare-loss")

# ------------------------------------------------------------------ 32.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b>Market failure</b> happens when the free market fails to allocate resources efficiently, so society's welfare is lower than it could be. The main causes are <b>externalities</b>, <b>public goods</b> (non-rival and non-excludable, so free riders mean the market will not supply them), <b>merit and demerit goods</b> (under- or over-consumed because people misjudge the benefit or harm), <b>information failure</b> (one side knows more) and <b>monopoly power</b>. Governments can respond with taxes, subsidies, regulation, provision and information, but <b>government failure</b> means intervention can leave resources no better allocated. Good answers name the cause, the type of inefficiency, the policy and its limits.</p></div>
''' + S.b((54, 64)).replace("4 · Market failure", "1 · Causes of market failure") + S.b((66, 67)).replace("5 · Government", "2 · Government") + '''
  <h2>3 · Matching the response to the cause</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Typical response</th><th>Limit of the response</th></tr>
    <tr><td>Negative externality</td><td>Tax, permits, regulation</td><td>The external cost is hard to measure</td></tr>
    <tr><td>Positive externality or merit good</td><td>Subsidy, provision, information</td><td>Costs taxpayers; may be wasted</td></tr>
    <tr><td>Public good</td><td>Provision by the state, paid for by taxes</td><td>The amount to provide is hard to judge</td></tr>
    <tr><td>Information failure</td><td>Labels, regulation, campaigns</td><td>Effect may be small; costs of enforcement</td></tr>
    <tr><td>Monopoly power</td><td>Competition policy, price caps</td><td>Regulators lack information on costs</td></tr>
  </table></div>
  <p>The policies are covered in more detail in syllabus 7.4 and 8.1.</p>
'''
watch = '''
  <h2>1 · The free-rider problem</h2>
  <p>A lighthouse costs $100 to build. Ten ships would each gain $15 from it, but no ship can be stopped from using the light. Press Play, or click the steps.</p><div id="stF"></div>
'''
explore = S.b((108, 113)).replace("Lab 4 ·", "Lab 1 ·") + '''
  <h2>Lab 2 · Information failure: the used car market</h2>
  <p>Buyers cannot tell good cars from bad ones. A good car is worth $10,000 to a buyer and a bad one $5,000. Sellers of good cars will accept no less than $8,000. Set the share of good cars and see what buyers are willing to offer. These numbers are illustrative.</p>
  <div class="card"><div class="grid2"><div><div id="g10"></div>
    <div class="readout"><div><small>Average value to buyers</small><strong id="h1"></strong></div><div><small>Good sellers' minimum</small><strong id="h2"></strong></div><div><small>Good cars for sale?</small><strong id="h3"></strong></div></div>
    <div class="verdict" id="hv"></div></div>
    <div><svg id="labU" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the average price buyers will offer with the minimum good-car sellers accept"></svg></div></div></div>
'''
practise = S.b((121, 122)).replace("2 · Which", "1 · Which") + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = TAILNOTE + S.b((140, 140), (143, 144))
exam = '''
  <h2>Past paper questions on market failure</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essay questions on the causes of market failure and government intervention, and Paper 3 multiple choice questions. The June 2020 papers were not sat. The detailed policy and externality questions are in syllabus 7.4 and 8.1. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 25 marks</td><td>4</td><td>May/June 2020 (41, 43, not sat); Oct/Nov 2020 (41); Oct/Nov 2021 (41, 42)</td></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2024 (42)</td></tr>
    <tr><td>Essay parts, 12 or 13 marks</td><td>3</td><td>May/June 2021 (42); May/June 2022 (41, 43); Oct/Nov 2020 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>3 shown below</td><td>2020 to 2022</td></tr>
  </table></div>
  <h2>A · 20 and 25 mark essays</h2>
''' + KEYL + S.b((178, 181), (188, 192), (194, 197), (199, 202), (204, 204)) + '''
  <h2>B · 12 and 13 mark questions</h2>
''' + S.b((213, 213), (240, 243), (245, 245)) + '''
''' + MCQTAIL.format("C · Multiple choice questions (Paper 3)")
tips = mktips(S, (263, 264, 265), '', (274, 275)) + cmd(CW["explain"], CW["discuss"], CW["evaluate"]) + FC
js = HEAD + '''
/* ---------- Watch: free rider ---------- */
const FH = (v) => 1.3 * v, FB = 270;
function frDraw(s) {
  let o = SV.line(60, FB, 740, FB) + SV.text(62, 24, "$", "sm");
  if (s.u > 0) { for (let i = 0; i < 10; i++) o += SV.rect(80 + i * 36, FB - FH(15) * s.u, 26, FH(15) * s.u, "f1", { opacity: (s.f > 0.5 ? 0.3 : 0.85) * s.u }); o += SV.text(250, FB + 22, "10 users, $15 each", "sm bd", { "text-anchor": "middle", ...op(s.u) }); }
  if (s.f > 0) o += SV.text(250, FB - FH(15) - 14, "each hopes someone else pays", "lbl bd t2", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px", ...op(s.f) });
  if (s.t > 0) o += SV.rect(480, FB - FH(150) * s.t, 80, FH(150) * s.t, "f3", op(s.t)) + SV.text(520, FB - FH(150) - 8, "benefit $150", "lbl bd t3", { "text-anchor": "middle", ...op(s.t) }) + SV.text(520, FB + 22, "total benefit", "sm bd", { "text-anchor": "middle", ...op(s.t) });
  if (s.c > 0) o += SV.rect(600, FB - FH(100) * s.c, 80, FH(100) * s.c, "f2", op(s.c)) + SV.text(640, FB - FH(100) - 8, "cost $100", "lbl bd t2", { "text-anchor": "middle", ...op(s.c) }) + SV.text(640, FB + 22, "cost to build", "sm bd", { "text-anchor": "middle", ...op(s.c) });
  if (s.s > 0) o += SV.text(400, 50, "State provides, tax $10 each: net social benefit +$50", "lbl bd t3", { "text-anchor": "middle", ...op(s.s) });
  return o;
}
Lib.stepper($("#stF"), { w: 780, h: 310, label: "A public good with ten users who each value it at $15, a cost of $100 and the free-rider problem", base: { u: 0, f: 0, t: 0, c: 0, s: 0 }, draw: frDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The good.</b> A lighthouse would give each of ten ships a benefit worth <b>$15</b>. It is <b>non-excludable</b> (no ship can be stopped from using the light) and <b>non-rival</b> (one ship's use does not reduce another's).", s: { u: 1 } },
  { cap: "<b>Worth building.</b> The total benefit is 10 × $15 = <b>$150</b> and the cost is <b>$100</b>, so society gains $50 if it is built.", s: { u: 1, t: 1, c: 1 } },
  { cap: "<b>The free-rider problem.</b> Each ship gets the light whether it pays or not, so each hopes the others will pay. No one pays, a private firm cannot earn revenue, and the lighthouse is <b>not built</b>. The market fails to supply a good that is worth more than it costs.", s: { u: 1, t: 1, c: 1, f: 1 } },
  { cap: "<b>State provision.</b> The government builds it and funds it with taxation, here $10 from each of the ten users. Everyone pays, the free-rider problem is overcome and society gains $50. The difficulty in practice is knowing how much to spend.", s: { u: 1, t: 1, c: 1, f: 1, s: 1 } },
] });
''' + S.j_((124, 138)) + '''
/* ---------- Lab 2: used cars ---------- */
function labCar() {
  if (!$("#gc")) return;
  const g = +$("#gc").value / 100, avg = g * 10000 + (1 - g) * 5000, ok = avg >= 8000;
  $("#h1").textContent = "$" + Lib.fmtN(avg, 0); $("#h2").textContent = "$8,000"; $("#h3").textContent = ok ? "Yes" : "No";
  $("#hv").textContent = ok ? `With ${Math.round(g * 100)}% good cars, buyers will pay an average of $${Lib.fmtN(avg, 0)}, enough for owners of good cars (who want $8,000) to sell. Both types of car are traded.`
    : `With ${Math.round(g * 100)}% good cars, buyers will pay only $${Lib.fmtN(avg, 0)} on average, less than the $8,000 owners of good cars want. They withdraw, the average quality of cars for sale falls, and offers fall further. Information failure can make a market shrink or disappear.`;
  const H = (v) => v / 50, base = 200;
  let o = SV.line(30, base, 400, base);
  [[70, avg, ok ? "f3" : "f2", "Buyers' average offer"], [230, 8000, "f4", "Good sellers' minimum"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 222, l, "sm", { "text-anchor": "middle" }); });
  $("#labU").innerHTML = o;
}
Lib.slider($("#g10"), { id: "gc", label: "Share of good cars for sale: ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labCar });

/* ---------- Practise ---------- */
''' + S.j_((151, 161)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Public good", "Non-rival and non-excludable, so the market will not supply it"],
  ["Free rider", "Someone who benefits without paying"],
  ["Merit good", "Under-consumed because people underestimate the benefit"],
  ["Demerit good", "Over-consumed because people underestimate the harm"],
  ["Asymmetric information", "One party knows more than the other"],
  ["Market failure", "The free market does not allocate resources efficiently"],
  ["Government failure", "Intervention that leaves resources less efficiently used"],
], done: "Seven words for the causes of market failure." });
''' + calc(S, (186,), '''  { q: "A street light costs $400. Twenty residents each gain $30 from it. What is the net social benefit ($)?", a: 200, sol: "20 × 30 = 600 benefit; 600 − 400 = <b>$200</b>. It should be built, but a private firm cannot charge for it." },
  { q: "The state funds that street light by taxing each of the 20 residents equally. How much does each pay ($)?", a: 20, sol: "400 ÷ 20 = <b>$20</b>, less than each resident's benefit of $30." },
  { q: "Good cars are worth $12,000 to buyers and bad cars $4,000. Half the cars for sale are good. What is the average value buyers will pay ($)?", a: 8000, sol: "0.5 × 12,000 + 0.5 × 4,000 = <b>$8,000</b>." },
''') + qz(S, (193, 194), '''  { q: "The free-rider problem occurs because:", opts: ["goods are rival", "people can use a non-excludable good without paying", "prices are too high", "firms have monopoly power"], a: 1, why: "If no one can be stopped from using it, no one has an incentive to pay." },
  { q: "Asymmetric information means:", opts: ["buyers and sellers have equal information", "one side of the market knows more than the other", "prices are fixed", "goods are non-rival"], a: 1, why: "A seller who knows more than the buyer can distort the market." },
''') + cards(S, (207, 208, 209, 210, 211, 212)) + mcq(S, (220, 228, 229))
write("ef3", page(EY.format(3), "Causes of Market Failure and the Case for Intervention",
  "Externalities, public goods, merit and demerit goods, information failure and monopoly power: what each is, why the market fails, and what a government can do. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Causes of Market Failure and the Case for Intervention", "causes-of-market-failure")
