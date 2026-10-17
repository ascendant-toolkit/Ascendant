"""AS syllabus 3.2.3 and 3.2.6 Direct provision of goods and services; provision of information. Run: python3 tools/artifact-kit/mk_as33.py"""
from asx import *
EY = EYAS("3.2.3 and 3.2.6")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Direct provision</b> means the government itself produces and supplies a good or service, usually <b>free or below cost at the point of use</b> and paid for through <b>taxation</b>; examples are state schools, public hospitals, defence, police and flood defences. Governments use it for <b>public goods</b> (which the market will not supply), for <b>merit goods</b> (to make sure everyone can use them) and for <b>equity</b>, but it has an <b>opportunity cost</b>, may be <b>inefficient</b> without competition, and a free service can cause <b>over-use and queues</b>. <b class="kw">Provision of information</b> tackles <b>information failure</b> directly, through campaigns, warnings, labels and education, to <b>raise demand for merit goods and cut demand for demerit goods</b>. It is cheap and respects choice, but it works slowly, may be ignored, and is rarely enough on its own.</p></div>

  <h2>1 · Direct provision (3.2.3)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Why governments do it</th><th>Problems with it</th></tr>
    <tr><td><b>Public goods</b> such as defence and street lighting would not be supplied by the market (free riders)</td><td><b>Opportunity cost</b>: funded by taxes, so less for other uses or higher taxes</td></tr>
    <tr><td><b>Merit goods</b> such as education and health care are under-consumed if left to the market</td><td><b>Free at the point of use</b> means demand rises, so queues and waiting lists</td></tr>
    <tr><td><b>Equity</b>: everyone can use essential services regardless of income</td><td><b>Inefficiency</b>: no profit motive or competition, so higher costs or lower quality</td></tr>
    <tr><td>Can supply where private firms cannot make a profit</td><td>Government may <b>misjudge</b> what consumers want; <b>no price signal</b> to show preferences</td></tr>
  </table></div>
  <ul>
    <li>Direct provision is <b>not only for public goods</b>: health care and education are <b>private goods</b> (rival and excludable) provided by the state.</li>
    <li>It means the <b>price mechanism is not used</b> for those goods: they are allocated by need, waiting lists or administrative rules.</li>
  </ul>

  <h2>2 · Provision of information (3.2.6)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Merit goods:</b> campaigns on the benefits of vaccination or education raise awareness, so demand shifts to the <b>right</b>.</li>
    <li><b>Demerit goods:</b> health warnings, plain packaging, calorie labels and advertising bans make people appreciate the harm, so demand shifts to the <b>left</b>.</li>
    <li><b>Advantages:</b> tackles the cause of the problem (information failure), keeps freedom of choice, usually cheaper than tax or direct provision, and has no black-market risk.</li>
    <li><b>Disadvantages:</b> results are <b>slow</b> and hard to measure; people may <b>ignore</b> or misunderstand it; advertising by firms may counter it; addicts may not respond; it does not help if cost is the barrier.</li>
  </ul>

  <h2>3 · Forms of direct provision</h2>
  <div class="tw"><table class="t">
    <tr><th>Form</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Fully free at the point of use</b></td><td>Government produces and pays for the service; users pay nothing directly</td><td>State schools, many public health services, street lighting</td></tr>
    <tr><td><b>Subsidised provision</b></td><td>Government provides at a price below cost; users pay part</td><td>Public transport, subsidised school meals</td></tr>
    <tr><td><b>State-funded, privately delivered</b></td><td>Government pays but private firms supply</td><td>Contracted waste collection, some health services</td></tr>
    <tr><td><b>Compulsory provision</b></td><td>Use is required by law</td><td>Compulsory schooling to a set age</td></tr>
  </table></div>
  <ul>
    <li><b>Public goods:</b> must be provided collectively because private firms cannot charge. <b>Merit goods:</b> could be sold by the market, but are provided directly to make sure everyone can use them.</li>
    <li><b>Financed by taxation:</b> everyone contributes, whether or not they use the service. The question of <b>how much</b> to provide is difficult because there is no price to show what people value.</li>
  </ul>

  <h2>4 · Worked example: free provision and excess demand</h2>
  <p>Suppose demand for a health service is P = 90 − Q (price per visit) and the government can afford to supply 40 visits.</p>
  <div class="tw"><table class="t">
    <tr><th>Item</th><th>Working</th><th>Result</th></tr>
    <tr><td>Price charged</td><td>Free</td><td>$0</td></tr>
    <tr><td>Quantity demanded at $0</td><td>0 = 90 − Q</td><td>90 visits</td></tr>
    <tr><td>Quantity supplied</td><td>Capacity</td><td>40 visits</td></tr>
    <tr><td>Excess demand</td><td>90 − 40</td><td>50 visits: waiting lists or rationing by queue</td></tr>
    <tr><td>Price that would clear the market</td><td>P = 90 − 40</td><td>$50</td></tr>
  </table></div>
  <ul>
    <li>Free provision removes the <b>price signal</b>, so goods must be rationed by <b>waiting lists, queues or rules</b> rather than price.</li>
    <li>This is not necessarily a failure: it can be justified on equity grounds. But it explains why free services can face <b>over-use and long waits</b>, and why governments consider charges, targeting or information.</li>
  </ul>

  <h2>5 · Forms of information provision</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples</th><th>Aim</th></tr>
    <tr><td><b>Public campaigns</b></td><td>Anti-smoking and vaccination adverts, healthy eating campaigns</td><td>Raise awareness of the benefits or harm</td></tr>
    <tr><td><b>Compulsory labelling and warnings</b></td><td>Health warnings, calorie and nutrition labels, plain packaging</td><td>Make the true cost visible at the point of purchase</td></tr>
    <tr><td><b>Education</b></td><td>School programmes on health, money and safety</td><td>Long-run change in attitudes</td></tr>
    <tr><td><b>Advertising rules</b></td><td>Bans or limits on advertising demerit goods</td><td>Reduce misleading or persuasive information</td></tr>
    <tr><td><b>Disclosure and ratings</b></td><td>Energy ratings, hygiene scores, safety ratings</td><td>Help consumers compare products</td></tr>
  </table></div>
  <ul>
    <li>Information shifts the <b>demand</b> curve: right for merit goods, left for demerit goods. It is aimed at the <b>cause</b> of the market failure, imperfect information.</li>
    <li><b>Why it may fail:</b> habits and addiction, powerful advertising by firms, the benefits being long term, and people who simply do not respond.</li>
  </ul>

  <h2>6 · Choosing between policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Best when</th><th>Main weakness</th></tr>
    <tr><td><b>Direct provision</b></td><td>The good is public, or many cannot pay for an essential service</td><td>Costly; waiting lists; possible inefficiency</td></tr>
    <tr><td><b>Information</b></td><td>The problem is lack of knowledge and the harm or benefit is clear</td><td>Slow and uncertain</td></tr>
    <tr><td><b>Subsidy</b></td><td>Price is the barrier to consuming a merit good</td><td>Cost; leakage to people who would buy anyway</td></tr>
    <tr><td><b>Tax, ban or minimum price</b></td><td>The aim is to cut consumption of a demerit good</td><td>Regressive effects; black markets; elasticity</td></tr>
  </table></div>
  <ul>
    <li>A <b>combination</b> is often best: information to change attitudes, plus a price measure or provision to change what people can afford.</li>
  </ul>
  <div class="warn"><b class="h">Do not write this</b>Direct provision is only for public goods (it is also used for merit goods such as education and health care, which are private goods). Do not say that free goods are free to society: the opportunity cost is paid through taxation.</div>
  <div class="tip"><b class="h">Exam tip</b>Link each policy to the <b>cause</b> of the market failure. Information fixes <b>information failure</b>; direct provision fixes <b>non-provision</b> of public goods and <b>under-provision</b> of merit goods. Evaluate with <b>cost</b>, <b>time</b> and <b>effectiveness</b>.</div>
'''

watch = '''
  <h2>1 · A free service and queues</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stF"></div>
  <h2>2 · Information shifts demand</h2>
  <div id="stI"></div>
'''

explore = '''
  <h2>Lab 1 · Free at the point of use</h2>
  <p>A hospital has fixed capacity. Change the price charged to patients and the capacity, and see waiting lists and the cost to taxpayers (each treatment costs $30).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Treatments wanted</small><strong id="r1"></strong></div><div><small>Waiting list</small><strong id="r2"></strong></div><div><small>Cost to taxpayers</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand, fixed capacity and the price charged, showing the waiting list"></svg></div></div></div>

  <h2>Lab 2 · An information campaign</h2>
  <p>A campaign about a demerit good. Set how many consumers see it and how much it changes their minds, and see the effect on demand and the market.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Demand shift</small><strong id="t1"></strong></div><div><small>New price</small><strong id="t2"></strong></div><div><small>New quantity</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 760 300" role="img" aria-label="Supply and demand with demand shifted left by the campaign"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which policy fits?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the problem of free provision in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A national health service", "Treatment is paid for through taxes and is free when used. Everyone can get care regardless of income, but demand exceeds capacity, so waiting lists form, and the system has a large opportunity cost.", "direct provision of a merit good, queues and opportunity cost.") +
rw("Flood defences", "A private firm cannot charge each household for a sea wall, because no one can be excluded and one household's protection does not reduce another's. Governments build them with tax money.", "direct provision of a public good.") +
rw("Cigarette health warnings", "Large pictorial warnings tell smokers about the harm. Awareness rises and some smokers cut down, but heavy smokers who are addicted may not respond, so warnings usually accompany taxes.", "information provision for a demerit good and its limits.") +
rw("Vaccination campaigns", "Adverts and local clinics explain the benefits of vaccination. Demand shifts to the right as people understand them better, and the campaign costs far less than providing every dose without explanation.", "information as a way of raising consumption of merit goods.") +
rw("A national health service", "Many governments fund health care from taxes so that everyone can use it regardless of income. Waiting lists appear when demand at a zero price exceeds capacity, which is how the service is rationed.", "direct provision of a merit good, excess demand and rationing without price.") +
rw("Calorie labels in restaurants", "Some governments require chains to show calorie information on menus. Diners may choose lower-calorie options, but those who do not respond to the information may not change what they order.", "information as a policy for a demerit good, and its limits.")
)

mc_exam = [
  mcq("m20_12", 16, "What would be categorised as direct government provision of goods and services?", ["a government grant to a firm to provide healthcare services", "a government regulation on the amount of sugar in soft drinks", "a government subsidy to a firm that operates a regional train service", "a government takeover of a local bus service"], 3, "Direct provision means the government itself supplies the service, as when it takes over a bus service."),
  mcq("s20_13", 18, "What is an example of direct provision by a government?", ["The government introduces a subsidy on renewable fuels to help the environment", "The government introduces a unit tax on cigarettes to discourage consumption", "The government sets a maximum rent on housing to protect tenants", "The government takes over a private library to improve local services"], 3, "Taking over a library to run it is direct provision. The other options are a subsidy, a tax and a price control."),
  mcq("m25_12", 12, "A government may use a range of methods to intervene in a market to affect both demand and supply. What is a method which will shift the demand curve for a good?", ["an indirect tax", "a subsidy", "direct provision", "provision of information"], 3, "Information changes tastes and awareness, so it shifts demand. Taxes and subsidies shift supply."),
  mcq("w20_11", 16, "The demand and supply curves show healthcare in a private market. What would happen if the government provides the same amount of healthcare free of charge?", ["Healthcare will become a public good", "Healthcare will no longer have external benefits", "There will be over-consumption of healthcare", "There will need to be rationing"], 3, "At a zero price quantity demanded exceeds the fixed amount provided, so rationing by other means is needed. It stays a private good."),
  mcq("s22_14", 15, "What would be a valid objection to the government provision of goods and services?", ["There will be an increase in consumer sovereignty", "Only the private sector can provide merit goods", "Tax rates and tax income are likely to fall", "Investment in the private sector might be reduced"], 3, "State provision can crowd out private investment. It does not increase consumer sovereignty or reduce tax needs.")
]

exam = exam_page("direct provision and provision of information",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Direct provision and information are tested as 8 and 12 mark Paper 2 parts most years, and in several Paper 1 questions. Reworded past questions are below, with five Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2023 (21) Q3(a); Oct/Nov 2020 (21) Q2(a)"), ("Essay parts, 12 marks", "1", "Feb/March 2024 (22) Q2(b)"), ("Data response, 6 marks", "1", "May/June 2023 (23) Q1(e)"), ("Multiple choice (Paper 1)", "5 shown below", "2020 to 2025")],
  [
  eq(P("w23_21", "3(a)"), "8 marks", "Explain why a government might decide to increase its direct provision of essential goods and services and consider whether such a policy is always likely to be successful.",
     ["Knowledge (up to 3): an understanding of the role of the state in providing essential goods and services, such as merit goods (1); these could include education and health care (1); they could be financed out of money received from taxation (1).",
      "Analysis (up to 3): up to 2 marks for explaining each essential good or service that a government might decide to provide (2 for well explained, 1 for limited explanation). Maximum 3.",
      "Evaluation (up to 2): a valid judgement on whether an increase in direct provision will always be likely to be successful."],
     "Define direct provision, name essential goods such as health and education, funded by tax. Evaluate: opportunity cost, queues, inefficiency.",
     [[("k", "Direct provision is when the government itself supplies goods and services, such as education and health care. They are merit goods, financed from taxation, and the government may increase provision to make sure everyone can use them, whatever their income.")], [("n", "Education raises skills and productivity, with benefits for the whole economy, but low-income households may under-consume it if they have to pay. Health care keeps the workforce healthy and has external benefits. If left to the market, both would be under-provided, so the state steps in.")], [("e", "However, more provision will not always succeed. It has an opportunity cost, because the money could be spent elsewhere or taxes raised, free services can lead to over-use and waiting lists, and state providers can be inefficient. Success depends on how well the extra funding is targeted.")]]),
  eq(P("w20_21", "2(a)"), "8 marks", "Explain, with the help of examples, how imperfect information among consumers affects their consumption of merit goods and demerit goods.",
     ["Knowledge (up to 2): knowledge of imperfect information in relation to a merit good and a demerit good, with suitable examples (such as education or health care and alcohol or tobacco).",
      "Application (up to 6): imperfect information and the under-consumption (and under-production) of a merit good because consumers do not fully appreciate its value (up to 3); imperfect information and the over-consumption of a demerit good because consumers do not appreciate the harm (up to 3)."],
     "Merit: benefits not fully appreciated, under-consumed. Demerit: harm underestimated, over-consumed. Use examples for each.",
     [[("k", "A merit good, such as education or health care, is a private good that has benefits for the individual and society. A demerit good, such as alcohol or tobacco, is a private good that is damaging to the individual.")], [("n", "With imperfect information, consumers may not appreciate the full value of a merit good, so they under-consume it: for example, some do not see the long-term gain from preventive health care. The market then under-produces it too. For a demerit good, consumers may not understand the damage caused, so they consume more than if they knew, and the market over-produces. Both mean the free market output is not the best for society.")]]),
  eq(P("m24_22", "2(b)"), "12 marks", "Assess whether the improved provision of information is likely to be the best method to reduce the consumption of demerit goods.",
     ["Analysis (up to 8): how information (labels, warnings, campaigns) corrects information failure and shifts demand to the left; a comparison with at least one alternative, such as an indirect tax, a minimum price, regulation or a ban, with the advantages and disadvantages of each. Indicative content may include elasticity, time lags and cost.",
      "Evaluation (up to 4): a judgement on whether information is likely to be the best method, supported by reasons, with a conclusion."],
     "Information: targets the cause, slow, may be ignored. Alternatives: tax (inelastic demand), minimum price (black markets), ban (enforcement). Judge.",
     [[("n", "Demerit goods are over-consumed because consumers underestimate the harm. Better information tackles this directly: warnings and campaigns could shift demand to the left without raising prices, respect consumer choice and cost less than other methods. But information works slowly, may be ignored by addicted users and can be countered by advertising. An indirect tax raises the price, but with inelastic demand consumption may fall only a little. A minimum price or a ban could cut consumption but risk black markets and are hard to enforce.")], [("e", "Information is unlikely to be the best method on its own, particularly for addictive goods, but it deals with the cause of the problem. A mix of information and a tax is likely to be the most effective, and the best choice depends on the good and on elasticity.")]]),
  eq(P("s23_23", "1(e)"), "6 marks", "With the help of a diagram, assess how the market for sugary foods might be affected by a ban on online advertising.",
     ["Analysis (up to 5): a ban on advertising reduces awareness and lowers demand, shifting the demand curve to the left, with a labelled diagram showing a fall in price and quantity; explanation of the effect on producers and revenue; consideration of what limits the effect, such as other forms of promotion, brand loyalty or addiction.",
      "Judgement (1): a valid conclusion about the likely overall effect."],
     "Diagram: demand shifts left, price and quantity fall. Limits: other promotion, taste, price elasticity.",
     [[("n", "Advertising raises demand for sugary foods. A ban on online advertising would reduce awareness and temptation, so demand would shift to the left. On a supply and demand diagram the equilibrium price and quantity would both fall, so producers lose revenue and may cut production. But companies may switch to other forms of advertising, and many consumers have strong taste preferences.")], [("e", "The overall effect is likely to be a small fall in consumption, because the ban affects only one channel, so it would probably work best alongside other policies such as taxes and labelling.")]])
  ],
  )

tips = tips_html(
  [("Say what direct provision is.", "The state supplies the good or service itself, paid for by tax."),
   ("It is not only for public goods.", "Health and education are private goods provided by the state."),
   ("Always mention opportunity cost.", "Tax money has other uses."),
   ("Free means queues.", "At a zero price demand exceeds capacity."),
   ("Information targets the cause.", "Information failure, so it shifts demand."),
   ("Say which way demand shifts.", "Right for merit goods, left for demerit goods."),
   ("Evaluate with time and cost.", "Information is slow and may be ignored.")],
  [("Direct provision", "Direct provision is when the government supplies goods and services itself, funded by taxation."),
   ("Information", "Provision of information aims to correct information failure."),
   ("Merit good", "Information could raise consumption of a merit good."),
   ("Opportunity cost", "Direct provision has an opportunity cost for the government."),
   ("Assess", "Information is likely to be most effective alongside other policies.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + '''
/* ---------- free provision ---------- */
function fpDraw(s) {
  const cap = 50, p = s.p, qd = Math.max(0, (90 - p) / 0.8); let o = axes(70, 270, 720, 25, "Treatments", "Price charged");
  o += SV.line(SDX(0), SDY(90), SDX(100), SDY(10), "c2", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(10) - 4, "Demand", "c2") + SV.line(SDX(cap), SDY(0), SDX(cap), SDY(100), "c1", { "stroke-width": 3 }) + tag(SDX(cap) + 6, SDY(98), "Capacity (supply)", "c1");
  o += SV.line(70, SDY(p), SDX(Math.max(qd, cap)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(cap), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  if (qd - cap > 1) o += SV.rect(SDX(cap), SDY(p) - 8, SDX(qd) - SDX(cap), 16, "f3", op(0.7)) + tag(SDX(qd) + 8, SDY(p) - 12, "waiting list " + Lib.fmtN(qd - cap, 0), "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="At a price of zero, demand exceeds fixed capacity so there is a waiting list">${fpDraw({ p: 0 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "A service with fixed capacity, priced and then free", base: { p: 50 }, draw: fpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>With a market price of $50</b> demand equals the capacity of 50 treatments. The service clears with no waiting list.", s: { p: 50 } },
  { cap: "<b>The price is cut to $25.</b> Quantity demanded rises to 81 but capacity is fixed at 50, so a waiting list of 31 appears.", s: { p: 25 } },
  { cap: "<b>Free at the point of use ($0).</b> Quantity demanded rises to 112, over twice capacity. With no price to ration, <b>waiting lists</b> or other rules decide who is treated, and taxpayers meet the cost.", s: { p: 0 } },
] });

/* ---------- information ---------- */
function infDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Information about a demerit good shifts demand to the left, lowering price and quantity">${infDraw({ d: -20, n: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "Information shifts the demand curve", base: { d: 0, n: 0 }, draw: infDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A demerit good.</b> Consumers underestimate the harm, so demand is higher than it would be with full information.", s: { d: 0, n: 0 } },
  { cap: "<b>Health warnings and a campaign</b> raise awareness of the harm. Demand shifts to the <b>left</b>: price and quantity fall.", s: { d: -20, n: 1 } },
  { cap: "<b>For a merit good</b> (such as vaccination) information has the opposite effect: demand shifts to the <b>right</b> and consumption rises.", s: { d: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#pr") || !$("#cp")) return;
  const p = +$("#pr").value, cap = +$("#cp").value, qd = (90 - p) / 0.8, wl = Math.max(0, qd - cap), served = Math.min(qd, cap), cost = 30 * served - p * served;
  $("#r1").textContent = Lib.fmtN(qd, 0); $("#r2").textContent = Lib.fmtN(wl, 0); $("#r3").textContent = "$" + Lib.fmtN(cost, 0);
  $("#rv").textContent = wl > 0 ? `At $${p} patients want ${Lib.fmtN(qd, 0)} treatments but capacity is ${cap}, so ${Lib.fmtN(wl, 0)} wait. Taxpayers pay $${Lib.fmtN(cost, 0)} (cost of $30 each minus the $${p} charge). Free provision removes the price rationing, so queues ration instead.` : `At $${p} demand (${Lib.fmtN(qd, 0)}) is within capacity (${cap}), so everyone is treated. Taxpayers pay $${Lib.fmtN(cost, 0)}${p >= 30 ? ", or nothing if the charge covers the cost" : ""}.`;
  const dEnd = cap; let o = axes(70, 270, 720, 25, "Treatments", "Price charged");
  o += SV.line(SDX(0), SDY(90), SDX(100), SDY(10), "c2", { "stroke-width": 3 }) + SV.line(SDX(cap), SDY(0), SDX(cap), SDY(100), "c1", { "stroke-width": 3 }) + SV.line(70, SDY(p), SDX(Math.max(qd, cap)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.text(62, SDY(p) + 4, "$" + p, "sm", { "text-anchor": "end" });
  if (wl > 0.5) o += SV.rect(SDX(cap), SDY(p) - 8, SDX(qd) - SDX(cap), 16, "f3", op(0.7));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pr", label: "Price charged to patients, $ ", min: 0, max: 50, step: 5, value: 0, fmt: (v) => "$" + v, onInput: labF });
Lib.slider($("#g2"), { id: "cp", label: "Capacity of the service, treatments ", min: 30, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#rc") || !$("#st")) return;
  const reach = +$("#rc").value / 100, str = +$("#st").value / 100, d = -30 * reach * str, e = sdEq(d, 0), e0 = sdEq(0, 0), dq = (e.q - e0.q) / e0.q * 100;
  $("#t1").textContent = d === 0 ? "None" : "Left " + Lib.fmtN(-d, 1); $("#t2").textContent = "$" + Lib.fmtN(e.p, 1); $("#t3").textContent = Lib.fmtN(e.q, 1);
  $("#tv").textContent = d === 0 ? "The campaign reaches no one or changes no minds, so demand stays put." : `${Lib.fmtN(reach * 100, 0)}% of consumers see the campaign and it changes ${Lib.fmtN(str * 100, 0)}% of their minds, shifting demand left by ${Lib.fmtN(-d, 1)}. Price falls to $${Lib.fmtN(e.p, 1)} and quantity by ${Lib.fmtN(-dq, 1)}%. Information is cheap, but the effect is small unless many people notice it and respond.`;
  $("#labB").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g3"), { id: "rc", label: "Share of consumers reached, % ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "st", label: "Share who change their minds, % ", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + "%", onInput: labC });
labC();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Direct provision or information?", ["Direct provision", "Provision of information"],
  [("State schools funded by taxes", 0), ("Health warnings on cigarette packs", 1), ("A public hospital", 0), ("An anti-smoking advert campaign", 1), ("A government-run flood barrier", 0), ("Calorie labels on menus", 1), ("State-run police service", 0), ("Education about healthy eating", 1)],
  "Direct provision: the state supplies the good. Information: the state informs consumers so they choose differently.") + MATCH([
  ["Direct provision", "The government supplies a good or service itself"],
  ["Information failure", "Consumers lack or misjudge relevant information"],
  ["Waiting list", "Rationing when a free service has fixed capacity"],
  ["Opportunity cost", "Other spending given up to fund provision"],
  ["Health warning", "Information that shifts demand for a demerit good left"],
  ["Crowding out", "State provision reducing private investment"]]) + ORDER(
  "Put the problem with free provision in order.",
  ["The government provides a service free at the point of use", "The price falls to zero", "Quantity demanded rises above capacity", "A waiting list forms", "Taxpayers meet the cost, which has an opportunity cost"],
  "Free provision removes price rationing, so queues ration instead.") + CALC([
  {"q": "A clinic treats 80 patients at a cost of $40 each, charging $10 per visit. What is the cost to taxpayers ($)?", "a": 2400, "unit": "$", "tol": 1, "hint": "(40 − 10) × 80.", "sol": "<b>$2,400</b>."},
  {"q": "At a price of $0, demand is Qd = 112 and capacity is 50. What is the waiting list?", "a": 62, "unit": "", "tol": 0.5, "hint": "112 − 50.", "sol": "<b>62</b>."},
  {"q": "A campaign reduces demand for a demerit good from 200 to 170 units. What is the percentage fall?", "a": 15, "unit": "%", "tol": 0.3, "hint": "30 ÷ 200.", "sol": "<b>15%</b>."},
  {"q": "A government spends $3m on a campaign that cuts consumption by 50 000 units. What is the cost per unit reduction ($)?", "a": 60, "unit": "$", "tol": 0.5, "hint": "3,000,000 ÷ 50,000.", "sol": "<b>$60</b>."}]) + MCQ([
  ("Direct provision means:", ["The government supplies the good itself", "The government taxes a good", "The government sets a price limit", "A firm subsidises output"], 0, "State supplies."),
  ("Provision of information is most likely to correct:", ["Information failure", "A public good", "Income inequality", "Monopoly power"], 0, "Cause of the problem."),
  ("A free service with fixed capacity will tend to create:", ["Waiting lists", "Surpluses", "Lower costs", "Higher prices"], 0, "Demand exceeds capacity."),
  ("Information about a demerit good shifts demand:", ["To the left", "To the right", "Not at all", "Vertically"], 0, "Harm is better understood."),
  ("A valid disadvantage of direct provision is:", ["Opportunity cost", "Lower tax need", "More consumer sovereignty", "More competition"], 0, "Uses tax money.")
], "qz1") + CARDS([
  ("Direct provision", "State supplies it."),
  ("Public goods", "Provided because markets will not."),
  ("Merit goods", "Provided to ensure access."),
  ("Free service", "Queues and waiting lists."),
  ("Information", "Corrects information failure."),
  ("Merit: demand", "Shifts right."),
  ("Demerit: demand", "Shifts left."),
  ("Limits", "Slow, cost, may be ignored.")]) + MCQ(mc_exam)

build("as33", "as-direct-provision-information", "Direct Provision and Provision of Information", EY,
  "3.2.3 and 3.2.6: when governments supply goods directly, the problems of free provision, and how information can correct information failure. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
