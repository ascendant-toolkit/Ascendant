"""AS syllabus 1.6.3-1.6.4 Merit goods, demerit goods and the market failure they create. Run: python3 tools/artifact-kit/mk_as19.py"""
from asx import *
EY = EYAS("1.6.3 to 1.6.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b class="kw">merit good</b> is a good that is <b>under-consumed</b> in a free market because consumers <b>do not fully understand its benefits</b> (<b>information failure</b>), so the benefit to the consumer is worth <b>more</b> than the consumer realises; examples are education, vaccinations and health check-ups. A <b class="kw">demerit good</b> is <b>over-consumed</b> because consumers <b>underestimate the harm</b> it does to themselves (and often others), such as tobacco, alcohol and sugary drinks. In both cases the <b>market failure</b> is that the free market output is <b>not the socially best one</b>, so resources are not allocated efficiently. Merit and demerit goods are still <b>private goods</b> (rival and excludable); the issue is how people value them, not whether they can be provided.</p></div>

  <h2>1 · Merit goods (1.6.3)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>Consumers <b>underestimate</b> the benefit they get, so <b>demand is too low</b> (private benefit is understated) and the market <b>under-provides</b> and people <b>under-consume</b> them.</li>
    <li>There are often <b>positive externalities</b> too (an educated workforce benefits everyone), so the social benefit is higher still.</li>
    <li>They are <b>private goods</b>, not public goods: <b>rival</b> and <b>excludable</b>. They are often provided by the government (education, health care) but this is a policy choice, not part of the definition.</li>
    <li>Cause: <b>information failure</b> (consumers do not know or fully understand the benefits), sometimes also a low income that stops them paying.</li>
  </ul>

  <h2>2 · Demerit goods (1.6.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>Consumers <b>underestimate the harm</b> (or the cost of consumption), so <b>demand is too high</b> (private benefit is overstated) and the good is <b>over-produced and over-consumed</b>.</li>
    <li>There may be <b>negative externalities</b> (passive smoking, drink-driving) which widen the gap between private and social cost.</li>
    <li>Examples: cigarettes, alcohol, illegal drugs, sugary drinks, gambling. They are private goods: rival and excludable.</li>
    <li>A product can be <b>both</b> a private good and a demerit good (a plastic bottle: rival and excludable, but over-consumed because of the harm to the environment that users do not weigh).</li>
  </ul>

  <h2>3 · What can be done?</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Merit good</th><th>Demerit good</th></tr>
    <tr><td><b>Indirect tax / subsidy</b></td><td><b>Subsidy</b> lowers cost, raises output and consumption</td><td><b>Indirect tax</b> raises cost, reduces output and consumption</td></tr>
    <tr><td><b>Price controls</b></td><td>Maximum price below the equilibrium (to make it cheaper)</td><td>Minimum price above the equilibrium (to make it dearer)</td></tr>
    <tr><td><b>Direct provision</b></td><td>State schools, public hospitals, free vaccination</td><td>Not common</td></tr>
    <tr><td><b>Regulation / ban</b></td><td>Compulsory schooling, compulsory vaccination</td><td>Age limits, advertising bans, banning a drug</td></tr>
    <tr><td><b>Information / education</b></td><td>Campaigns about the benefits</td><td>Health warnings, anti-smoking campaigns</td></tr>
  </table></div>
  <ul>
    <li><b>Evaluate:</b> tax and subsidy rely on knowing the <b>size of the failure</b>; demand for demerit goods is often <b>inelastic</b> (addiction), so a tax raises revenue but cuts consumption little; <b>minimum prices</b> can create <b>black markets</b>; <b>bans</b> are hard to enforce; <b>information</b> works slowly and may be ignored; <b>direct provision</b> costs taxpayers and has an <b>opportunity cost</b>.</li>
    <li>The best choice is probably a <b>combination</b> of policies, depending on the good.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Always say <b>why</b> (information failure) and say <b>which way</b> the market fails (merit: under-consumed; demerit: over-consumed). Merit goods are <b>private goods</b>, so use rivalry and excludability if asked.</div>
'''

watch = '''
  <h2>1 · Merit good: the market under-provides</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · Demerit good: a tax moves it back</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · How far does the market fall short?</h2>
  <p>A merit good, say vaccination. Consumers understand only part of its benefit. Move the sliders to see consumption in the free market and what the best level would be.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Free market quantity</small><strong id="r1"></strong></div><div><small>Best quantity</small><strong id="r2"></strong></div><div><small>Shortfall</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Demand, social benefit and supply for a merit good with free market and best quantities"></svg></div></div></div>

  <h2>Lab 2 · A tax on a demerit good</h2>
  <p>Cigarette-style demerit good. Set the tax and how price inelastic demand is (addiction), and see the fall in consumption and the tax revenue.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Quantity after tax</small><strong id="t1"></strong></div><div><small>Fall in consumption</small><strong id="t2"></strong></div><div><small>Tax revenue</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Supply and demand for a demerit good before and after an indirect tax"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Merit, demerit or neither?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the demerit good tax argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Vaccination", "Many parents undervalue the full benefit of vaccination, both to the child and to others. Governments therefore provide it free, make it compulsory for school entry or run information campaigns. It is a private good that is under-consumed, so a merit good.", "information failure, positive externalities and direct provision.") +
rw("Tobacco tax", "Cigarettes carry heavy taxes and health warnings. Smokers underestimate the harm and demand is price inelastic, so the tax raises large revenue but reduces smoking by a smaller amount. Governments often add plain packaging and advertising bans.", "taxation of a demerit good, price inelasticity and the use of combined policies.") +
rw("Sugar tax", "A tax on sugar-sweetened drinks charged to producers raises their cost, so some cut the sugar content and prices rise. Consumption of the highest sugar drinks falls, which is one way a tax can improve the allocation of resources.", "an indirect tax shifting the supply curve to correct over-consumption.") +
rw("Minimum alcohol prices", "A minimum price per unit of alcohol aims to cut consumption of the cheapest, strongest drinks. If demand is inelastic, spending on alcohol rises and producers gain. It may also push some drinkers towards illegal or cross-border sales.", "minimum prices above the equilibrium and their unintended effects.")
)

mc_exam = [
  mcq("m22_12", 16, "The National Library Board of Singapore is a public sector organisation that finances and manages the state libraries. What is the most likely reason for this?", ["Libraries are public goods", "Libraries are merit goods", "The cost of providing library services would be greater in the private sector", "The opportunity cost to the public sector of providing library services is zero"], 1, "Libraries are private goods that are under-consumed unless the state provides them, so they are merit goods. They are rival and excludable, and the state has an opportunity cost."),
  mcq("m24_12", 13, "What explains the underconsumption of merit goods?", ["Their value is not fully understood by consumers", "They are unproductive goods and services", "They can only be provided by the government", "They are only provided by the private sector"], 0, "Merit goods are under-consumed because consumers do not fully understand their benefits (information failure)."),
  mcq("s21_11", 16, "A government provided additional free hospital care to its citizens. What happened as a result?", ["The supply of merit goods reduced", "The supply of merit goods increased", "The supply of private goods reduced", "The supply of public goods increased"], 1, "Hospital care is a merit good, so more free provision increases the supply of merit goods. It is a private good, not a public good."),
  mcq("s22_14", 15, "What would be a valid objection to the government provision of goods and services?", ["There will be an increase in consumer sovereignty", "Only the private sector can provide merit goods", "Tax rates and tax income are likely to fall", "Investment in the private sector might be reduced"], 3, "Government provision can crowd out private investment. The state can provide merit goods, and provision raises, not lowers, the need for taxes."),
  mcq("s24_13", 12, "A government introduces an effective minimum price for a product but makes no other intervention in the market. This policy suggests that the government's objective is", ["to discourage consumption of a demerit good", "to increase the consumption of a merit good", "to reduce the price of a private good", "to support the incomes of producers"], 0, "A minimum price above the equilibrium raises price and reduces quantity demanded, so it fits a demerit good."),
  mcq("s25_13", 13, "A flood-control dam is an example of a good provided directly by a government. Which statement relating to the direct provision of a flood-control dam is not correct?", ["It allows the government to tackle the failure to provide public goods", "It forces the government to incur an opportunity cost", "It involves the supply of a merit good", "It is an example of government allocation of resources"], 2, "A flood-control dam is non-rival and non-excludable, so it is a public good, not a merit good."),
  mcq("w22_13", 17, "If an industry is currently state-owned and state-run, what does not represent a reason for it being privatised?", ["Decisions will no longer be taken with political considerations in mind", "The benefits of merit goods will be taken into account in decision-making", "Its owners would have more incentive to make it operate profitably", "There will be greater incentives for managers to introduce modern technology"], 1, "A private owner is motivated by profit, so wider merit good benefits are less likely to be taken into account."),
  mcq("w21_12", 16, "Why might a government nationalise a private firm?", ["to gain greater efficiency due to more competition", "to increase merit good provision", "to increase choice for the consumer", "to raise more tax revenue"], 1, "Nationalisation can increase provision of merit goods that private firms under-supply. It reduces competition and choice."),
  mcq("w23_11", 14, "A government introduces charges for vehicles using the roads in its capital city. Which characteristic must the roads have for this to be successful in reducing congestion?", ["The roads must be excludable", "The roads must be merit goods", "The roads must be non-rivalrous", "The roads must be public goods"], 0, "A charge only works if non-payers can be excluded."),
  mcq("w20_13", 14, "A government regards alcoholic drinks as a demerit good and introduces a minimum price above the equilibrium in an attempt to protect consumers. Demand for alcoholic drinks is price inelastic. What is the most likely outcome?", ["a fall in the revenue of alcoholic drink producers", "a fall in the quantity of alcoholic drink sales", "a long-run shortage of alcoholic drinks", "an increase in specific tax revenue from the sale of alcoholic drinks"], 1, "A price above the equilibrium reduces quantity demanded, though only a little when demand is inelastic. Revenue rises, not falls.")
]

exam = exam_page("merit goods, demerit goods and market failure",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Merit and demerit goods appear in 8 mark Paper 2 parts most series, often paired with a 12 mark policy evaluation, and as Paper 1 questions every year. Reworded past questions are below, with ten Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "May/June 2022 (21) Q2(a); May/June 2021 (22) Q2(a)"), ("Essay parts, 12 marks", "1", "May/June 2020 (22) Q4(b)"), ("Data response, 4 marks", "1", "May/June 2020 (23) Q1(a)"), ("Multiple choice (Paper 1)", "10 shown below", "2020 to 2025")],
  [
  eq(P("s22_21", "2(a)"), "8 marks", "Explain, using examples, why merit goods are classified as private goods rather than public goods.",
     ["Knowledge (up to 2): of private goods (1) and of public goods (1).",
      "Application (up to 6): examples to explain why merit goods are private goods (up to 3) and why they are not public goods (up to 3)."],
     "Private: rival and excludable. Public: non-rival and non-excludable. Apply both to education and health care.",
     [[("k", "A private good is rival, because when one person consumes it another cannot, and excludable, because those who do not pay can be kept out. A public good is non-rival and non-excludable.")], [("n", "Education and health care are merit goods. A hospital bed or a school place used by one person cannot be used by another, so they are rival, and a person who has not enrolled or registered can be excluded, so they are excludable. They are not public goods, such as street lighting or defence, which are available to everyone at once and cannot be withheld. Merit goods are often provided by the government, but this does not make them public.")]]),
  eq(P("s21_22", "2(a)"), "8 marks", "State what is meant by a demerit good and, with the help of a diagram, explain how a tax on producers can improve the allocation of resources in the market for sugar-sweetened drinks.",
     ["Knowledge (up to 2): a demerit good is one whose cost of consumption is underestimated, or is worse for the consumer than they realise, because of information failure (1), and is over-consumed (1).",
      "Application (up to 3): a correctly labelled diagram showing a left shift of supply (1), a fall in quantity (1) and a rise in price (1).",
      "Analysis (up to 3): the tax increases the cost of production (1), which raises the price and reduces consumption (1), so the problem of over-consumption is reduced and the allocation of resources improves (1)."],
     "Demerit: harm underestimated, over-consumed. Diagram: supply shifts left, price up, quantity down. Explain the improvement.",
     [[("k", "A demerit good, such as a sugary drink, is a good whose harm consumers underestimate because of information failure, so it is over-consumed in a free market.")], [("n", "A tax on producers raises their costs, so the supply curve shifts to the left. The equilibrium price rises and the quantity falls. Because consumption was too high, a smaller quantity is closer to the best level for society, so resources are used more efficiently and the market failure is reduced.")]]),
  eq(P("s20_23", "1(a)"), "4 marks", "Explain why a plastic bottle can be classified as both a private good and a demerit good.",
     ["Private good: excludability (1) and rivalry (1).", "Demerit good: over-consumption (1) as a result of information failure (1)."],
     "Private: rival and excludable. Demerit: over-consumed through information failure.",
     [[("k", "A plastic bottle is a private good because it is excludable, since a seller can refuse it to someone who will not pay, and rival, since one person using it stops another using it."), ("n", "It can be a demerit good because it is over-consumed: users do not fully understand the harm that plastic waste does to the environment, which is information failure, so too many are used.")]]),
  eq(P("s20_22", "4(b)"), "12 marks", "Consider the problem of the provision of merit goods in a market economy and assess whether direct provision of such goods is the most effective way to deal with this problem.",
     ["Analysis (up to 8): the under-production and under-consumption of merit goods based on information failure (up to 4); a comparison of direct provision with at least one alternative, such as a subsidy or a public education campaign (up to 4).",
      "Evaluation (up to 4): evaluative comment and a reasoned conclusion on the most effective policy."],
     "Problem: information failure, under-consumption. Direct provision vs subsidy vs campaign. Judge.",
     [[("n", "Merit goods such as education are under-consumed in a free market because consumers do not fully understand the long-term benefit, so private demand is too low. Direct provision by the state, such as free schools, ensures everyone can use them, but costs taxpayers and has an opportunity cost. A subsidy lowers the price and encourages consumption, but depends on estimating the right level. An information campaign may raise understanding, but works slowly.")], [("e", "Direct provision is probably the most reliable way of reaching everyone, especially where income is low, but it is costly and may reduce quality. A mix of provision, subsidy and information is likely to be most effective, depending on the good and the size of the information failure.")]])
  ],
  )

tips = tips_html(
  [("Say why: information failure.", "Merit goods: consumers do not see the full benefit. Demerit goods: they underestimate the harm."),
   ("Say which way the market fails.", "Merit: under-consumed. Demerit: over-consumed."),
   ("They are private goods.", "Rival and excludable, even when the state provides them."),
   ("Match the policy to the failure.", "Subsidy and maximum price for merit goods. Tax and minimum price for demerit goods."),
   ("Evaluate with elasticity.", "Inelastic demand means a tax cuts consumption only a little."),
   ("Mention unintended effects.", "Black markets, enforcement costs, opportunity cost of provision."),
   ("Use a diagram.", "A left shift in supply for a tax, a right shift for a subsidy.")],
  [("Merit good", "A merit good is a good that is under-consumed because consumers do not fully understand its benefits."),
   ("Demerit good", "A demerit good is over-consumed because consumers underestimate the harm it does."),
   ("Information failure", "Information failure may lead to merit goods being under-consumed and demerit goods over-consumed."),
   ("Judge", "A tax might reduce consumption of a demerit good, but the effect depends on how inelastic demand is."),
   ("Mixed policies", "A combination of policies is likely to work best in many cases.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- merit: demand below social benefit ---------- */
function meritDraw(s) {
  let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Price ($)", "sm") + SV.text(700, 288, "Quantity", "sm", { "text-anchor": "end" });
  o += SV.line(60, 70, 640, 250, "c1") + SV.text(646, 256, "Supply", "lbl bd c1");
  o += SV.line(80, 210, 560, 70, "c2") + SV.text(562, 66, "Demand (private benefit)", "lbl bd c2");
  if (s.a > 0) o += SV.line(80, 150, 560, 30, "c3", op(s.a)) + SV.text(566, 30, "Marginal social benefit", "lbl bd c3", op(s.a));
  o += SV.circle(360, 157, 5, "dot2");
  if (s.b > 0) o += SV.line(360, 157, 360, 270, "dash", op(s.b)) + SV.text(360, 286, "Q market", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.c > 0) o += SV.line(440, 127, 440, 270, "dash", op(s.c)) + SV.text(440, 286, "Q best", "sm", { "text-anchor": "middle", ...op(s.c) }) + SV.line(362, 262, 428, 262, "c4", op(s.c)) + SV.arrowHead(440, 262, "r", "dot4") + SV.text(400, 252, "under-consumed", "sm", { "text-anchor": "middle", ...op(s.c) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A merit good: social benefit above private demand, so the market quantity is below the best quantity">${meritDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "Demand, social benefit and supply for a merit good", base: { a: 0, b: 0, c: 0 }, draw: meritDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Consumers value the good by what they understand of its benefit, so demand reflects only the <b>private benefit</b>. Supply and demand meet at the market quantity.", s: { b: 1 } },
  { cap: "<b>The true benefit.</b> The benefit to society is higher than consumers realise (information failure, positive externalities), so the <b>marginal social benefit</b> curve lies above demand.", s: { a: 1, b: 1 } },
  { cap: "<b>Under-consumption.</b> The best quantity is to the right of the market quantity. The market fails to provide enough, so the government may subsidise, regulate or provide the good.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- demerit tax ---------- */
function demDraw(s) {
  let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Price ($)", "sm") + SV.text(700, 288, "Quantity", "sm", { "text-anchor": "end" });
  o += SV.line(80, 230, 620, 60, "c2") + SV.text(626, 64, "Demand", "lbl bd c2");
  o += SV.line(80, 90, 620, 220, "c1") + SV.text(626, 224, "S", "lbl bd c1");
  const dy = -s.t * 45;
  if (s.t > 0) o += SV.line(80, 90 + dy, 620, 220 + dy, "c3", op(s.t)) + SV.text(626, 220 + dy, "S + tax", "lbl bd c3", op(s.t));
  o += SV.circle(380, 156, 5, "dot2") + SV.line(380, 156, 380, 270, "dash") + SV.text(380, 286, "Q1", "sm", { "text-anchor": "middle" });
  if (s.t > 0) o += SV.circle(332, 156 + dy + 30, 5, "dot3", op(s.t)) + SV.line(332, 186 + dy, 332, 270, "dash", op(s.t)) + SV.text(332, 286, "Q2", "sm", { "text-anchor": "middle", ...op(s.t) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tax shifts supply left on a demerit good so quantity falls from Q1 to Q2">${demDraw({ t: 1 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 300, label: "A tax on a demerit good shifts supply to the left", base: { t: 0 }, draw: demDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Over-consumption.</b> Because consumers underestimate the harm, the market quantity Q1 is higher than the best level for society.", s: { t: 0 } },
  { cap: "<b>The tax.</b> An indirect tax raises producers' costs, so supply shifts to the left. The price rises and the quantity falls to Q2, closer to the best level.", s: { t: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#aw") || !$("#sb")) return;
  const aw = +$("#aw").value / 100, sb = +$("#sb").value, qm = 100 * aw, qb = Math.min(160, qm + sb), gap = qb - qm;
  $("#r1").textContent = Lib.fmtN(qm, 0); $("#r2").textContent = Lib.fmtN(qb, 0); $("#r3").textContent = Lib.fmtN(gap, 0);
  $("#rv").textContent = gap <= 0.5 ? "Consumers understand the full benefit, so the free market output is the best one and there is no under-consumption." : `Consumers recognise only ${Lib.fmtN(aw * 100, 0)}% of the benefit, so the market supplies ${Lib.fmtN(qm, 0)} units but ${Lib.fmtN(qb, 0)} is best. This under-consumption of ${Lib.fmtN(gap, 0)} units is why governments subsidise, provide or promote merit goods.`;
  const X = (v) => 40 + v * 2.2; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30);
  o += SV.line(X(0), 250, X(160), 70, "c1") + SV.line(X(0), 80, X(160), 230, "c2");
  o += SV.line(X(qm), 270, X(qm), 150, "dash") + SV.line(X(qb), 270, X(qb), 150, "dash", { style: "stroke:var(--good)" }) + SV.text(X(qm), 288, "Market " + Lib.fmtN(qm, 0), "sm", { "text-anchor": "middle" }) + SV.text(X(qb), 288, "Best " + Lib.fmtN(qb, 0), "sm", { "text-anchor": "middle", style: "fill:var(--good)" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "aw", label: "Share of the benefit consumers understand, % ", min: 20, max: 100, step: 5, value: 50, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g2"), { id: "sb", label: "Extra output society would want, units ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#tx") || !$("#el")) return;
  const t = +$("#tx").value, el = +$("#el").value / 10, p0 = 10, q0 = 100, p1 = p0 + t, dq = -el * (t / p0) * q0, q1 = Math.max(0, q0 + dq), fall = q0 - q1, rev = q1 * t;
  $("#t1").textContent = Lib.fmtN(q1, 0); $("#t2").textContent = Lib.fmtN(fall, 0) + " units (" + Lib.fmtN(fall / q0 * 100, 0) + "%)"; $("#t3").textContent = "$" + Lib.fmtN(rev, 0);
  $("#tv").textContent = `A $${t} tax raises the price from $${p0} to $${p1} (all passed on, to keep it simple). With price elasticity of demand of ${Lib.fmtN(el, 1)}, quantity falls by ${Lib.fmtN(fall / q0 * 100, 0)}%, and the government collects $${Lib.fmtN(rev, 0)}. ${el < 1 ? "Demand is inelastic, so the tax reduces consumption by less than the price rise, but raises plenty of revenue." : "Demand is elastic, so consumption falls by more, so the tax is more effective at cutting use but raises less revenue."}`;
  const X = (v) => 40 + v * 3, Y = (v) => 270 - v * 10; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30);
  o += SV.line(X(0), Y(14), X(110), Y(2), "c2") + SV.line(X(0), Y(3), X(110), Y(15), "c1") + SV.line(X(0), Y(3 + t), X(110), Y(15 + t), "c3");
  o += SV.circle(X(q0), Y(p0), 5, "dot2") + SV.circle(X(q1), Y(p1), 5, "dot3") + SV.line(X(q1), Y(p1), X(q1), 270, "dash");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "tx", label: "Tax per unit, $ ", min: 0, max: 5, step: 1, value: 2, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g4"), { id: "el", label: "Price elasticity of demand (×10) ", min: 2, max: 20, step: 1, value: 5, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Merit good, demerit good or neither?", ["Merit good", "Demerit good", "Neither"],
  [("Vaccination", 0), ("Cigarettes", 1), ("A loaf of bread", 2), ("Education", 0), ("Sugary drinks", 1), ("Health check-ups", 0), ("A haircut", 2), ("Gambling", 1)],
  "Merit: under-consumed. Demerit: over-consumed. Both come from information failure.") + MATCH([
  ["Merit good", "Under-consumed because consumers undervalue the benefit"],
  ["Demerit good", "Over-consumed because consumers underestimate the harm"],
  ["Information failure", "Consumers lack or misjudge relevant information"],
  ["Subsidy", "Payment to producers that lowers price and raises consumption"],
  ["Indirect tax", "Raises cost of production and cuts consumption"],
  ["Minimum price", "Price floor above the equilibrium"]]) + ORDER(
  "Put the case for taxing a demerit good in order.",
  ["Consumers underestimate the harm of the good", "Demand is too high, so output and consumption are too high", "The government imposes an indirect tax", "Supply shifts left, the price rises and quantity falls", "Consumption is closer to the best level for society"],
  "Information failure leads to over-consumption, and a tax moves it back.") + CALC([
  {"q": "A good is sold at $10 and 100 units are sold. A tax of $2 is passed on to consumers and quantity falls to 90. What is the tax revenue ($)?", "a": 180, "unit": "$", "tol": 1, "hint": "Tax per unit × quantity after tax.", "sol": "2 × 90 = <b>$180</b>."},
  {"q": "In the same example, what is the percentage fall in quantity?", "a": 10, "unit": "%", "tol": 0.2, "hint": "(100 − 90) ÷ 100.", "sol": "<b>10%</b>."},
  {"q": "Price rises from $10 to $12. What is the price elasticity of demand (ignore the minus sign)?", "a": 0.5, "unit": "", "tol": 0.02, "hint": "% change in quantity ÷ % change in price: 10 ÷ 20.", "sol": "10% ÷ 20% = <b>0.5</b>, inelastic."},
  {"q": "A subsidy of $3 per unit lowers a merit good's price from $15 to $12. Quantity rises from 200 to 260. What is the new total subsidy cost ($)?", "a": 780, "unit": "$", "tol": 1, "hint": "3 × 260.", "sol": "3 × 260 = <b>$780</b>."}]) + MCQ([
  ("A merit good is best described as one that is:", ["Under-consumed because its benefits are not fully understood", "Over-consumed because its harm is underestimated", "Non-rival and non-excludable", "Always provided by the government"], 0, "Information failure leads to under-consumption."),
  ("A demerit good is one that is:", ["Over-consumed because the harm is underestimated", "Under-consumed because its benefits are not understood", "Not scarce", "Only found in the black market"], 0, "Demerit goods are over-consumed."),
  ("Merit goods are:", ["Private goods", "Public goods", "Free goods", "Always non-excludable"], 0, "Rival and excludable."),
  ("Which policy is most likely to reduce consumption of a demerit good?", ["An indirect tax", "A subsidy", "A maximum price below equilibrium", "A fall in advertising warnings"], 0, "A tax raises price and cuts quantity."),
  ("If demand for a demerit good is price inelastic, a tax is likely to:", ["Raise a lot of revenue but cut consumption only a little", "Cut consumption a lot and raise little revenue", "Have no effect on price", "Increase consumption"], 0, "Inelastic demand means quantity falls by less than the price rise.")
], "qz1") + CARDS([
  ("Merit good", "Under-consumed: benefits not fully seen."),
  ("Demerit good", "Over-consumed: harm underestimated."),
  ("Information failure", "Root cause of both."),
  ("Private good", "Merit and demerit goods are private goods."),
  ("Subsidy", "Merit good policy: lowers price."),
  ("Indirect tax", "Demerit good policy: raises price."),
  ("Minimum price", "Raises price above equilibrium."),
  ("Black market", "Unintended effect of bans and price floors.")]) + MCQ(mc_exam)

build("as19", "as-merit-demerit-goods", "Merit and Demerit Goods", EY,
  "1.6.3 to 1.6.4: merit goods, demerit goods, information failure, and policy responses (tax, subsidy, price controls, provision, regulation and information). Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
