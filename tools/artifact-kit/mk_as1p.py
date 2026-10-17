"""AS syllabus 1.4.3 The planned economy. Run: python3 tools/artifact-kit/mk_as1p.py"""
from as6k import *
EY = EYAS("1.4.3")

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>In a <b class="kw">planned (command) economy</b> the government, through a <b class="kw">central planning authority</b>, decides <b>what</b> to produce, <b>how</b> to produce it and <b>for whom</b>, and the factors of production and most firms are <b>owned by the state</b>. Planners set <b>output targets</b>, allocate resources between industries and often set prices and wages, usually aiming to provide <b>essentials for everyone</b> and a more <b>equal</b> distribution of output. The system can provide <b>public and merit goods</b>, avoid duplication and direct resources to long-term goals. But without <b>price signals</b> planners lack the information to match output to preferences, so there are <b>shortages and surpluses</b>, and weak <b>incentives</b> for workers and managers lead to low efficiency, little innovation and limited consumer choice. Few economies are fully planned; some have moved towards markets, and the effects of such a <b>transition</b> include both gains in efficiency and costs such as unemployment and inequality.</p></div>

  <h2>1 · Features of a planned economy</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>State ownership</b> of land, capital and most firms; there is little private enterprise.</li>
    <li><b>Central planning:</b> a government authority sets output targets for industries and firms, often in multi-year plans.</li>
    <li><b>Allocation by instruction, not price:</b> inputs are directed to firms, and prices and wages may be set by the state.</li>
    <li><b>Aims:</b> equity (a fairer distribution), full employment, provision of essentials, and rapid development of chosen industries.</li>
  </ul>

  <h2>2 · How a planned economy answers the three questions</h2>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>Planned economy</th><th>Market economy (for comparison)</th></tr>
    <tr><td><b>What to produce?</b></td><td>Planners' targets and priorities</td><td>What consumers will pay for</td></tr>
    <tr><td><b>How to produce?</b></td><td>Methods decided or approved by the state</td><td>Lowest-cost methods chosen by firms</td></tr>
    <tr><td><b>For whom?</b></td><td>Allocated by the state, in principle by need or according to plan</td><td>Those with income and ability to pay</td></tr>
  </table></div>

  <h2>3 · Strengths of a planned economy</h2>
  <ul>
    <li><b>Public and merit goods</b> such as health and education are provided to everyone, regardless of income.</li>
    <li><b>Greater equality</b> in the distribution of income and goods.</li>
    <li><b>Long-term planning:</b> resources can be directed to large, long-term projects that markets might neglect.</li>
    <li><b>Reduced unemployment</b> in principle, since the state can direct people to jobs.</li>
    <li><b>No wasteful competition or duplication</b> in some industries; no monopoly profits for private owners.</li>
  </ul>

  <h2>4 · Weaknesses of a planned economy</h2>
  <ul>
    <li><b>Information problem:</b> without prices to signal scarcity and preferences, planners cannot know how much of each good to produce, so there are <b>shortages</b> (queues) of some goods and <b>surpluses</b> of others.</li>
    <li><b>Weak incentives:</b> no profit motive and little reward for effort, so managers and workers have little reason to be efficient or to innovate.</li>
    <li><b>Limited consumer choice</b> and often poor quality, since consumers cannot signal what they want.</li>
    <li><b>Bureaucracy and slow decisions:</b> a large administration is costly and slow to respond.</li>
    <li><b>Possible lack of economic freedom</b> and black markets where goods are scarce.</li>
  </ul>
  <div id="pic2" class="card"></div>

  <h2>5 · Changing the system</h2>
  <ul>
    <li><b>Transition from planned to market</b> (as in the former Soviet bloc and in China's reforms): prices are freed, firms are privatised, competition and private enterprise grow.</li>
    <li><b>Possible benefits:</b> more efficiency, innovation and choice; higher growth in the long run.</li>
    <li><b>Possible costs:</b> rising prices, structural unemployment as state firms close, widening inequality, and under-provision of public and merit goods.</li>
    <li>Whether the change is beneficial depends on <b>how quickly</b> it is done, how well institutions work and who gains and loses. Many economies move towards a <b>mixed</b> system.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not write that a planned economy has "no" markets. Say who makes the <b>main</b> decisions and what the consequences are. The key weakness is the <b>lack of price signals</b>, which leads to shortages and surpluses, and the lack of an incentive.</div>
'''

watch = '''
  <h2>1 · The planners' information problem</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Why incentives matter</h2>
  <div id="stB"></div>
  <h2>3 · The costs and benefits of moving to a market</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Set the output target</h2>
  <p>Consumers' demand is P = 90 − 0.8Q and the cost of supply is P = 10 + 0.8Q, so the market-clearing output is 50 at a price of 50. The planners fix the output and the price. Move the target to see shortages and surpluses.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Quantity consumers want at that price</small><strong id="r1"></strong></div><div><small>Planned output</small><strong id="r2"></strong></div><div><small>Shortage or surplus</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="Demand and supply with a planned output and fixed price, showing the shortage or surplus"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Strength or weakness?", "Choose a feature of a planned economy to see whether it is a strength or a weakness and why.", ["Strength or weakness", "Why", "Market comparison"])

practise = '''
  <h2>1 · Planned, market or mixed?</h2><div id="cl1" class="card"></div>
  <h2>2 · Strength or weakness of a planned economy?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the effects of planners' errors in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Central planning and queues", "In the former Soviet Union, state planners set output targets and prices. Goods such as bread were cheap, but some goods were always in short supply and others were unwanted. Queues and black markets were common.", "shortages and surpluses without price signals.") +
rw("Output targets and quality", "When a factory is judged on the quantity it produces, managers may care less about quality or about what consumers want. Goods may be made but not used.", "weak incentives and targets.") +
rw("Moving towards a market", "China and several former Soviet bloc countries freed prices, allowed private firms and opened to trade. Output and incomes grew, but state firms closed, causing unemployment, and inequality widened.", "the benefits and costs of transition.") +
rw("Free provision of essentials", "A planned system may offer housing, health and education to everyone at low or zero prices. This reduces inequality, but supply can be limited and quality may suffer without funding or incentives.", "the strength of equity, and its limits.") +
rw("North Korea and Cuba", "These are often cited as examples of economies where the state plays an extremely large role in allocating resources. Even they are not purely planned, because informal markets exist.", "no real economy is purely planned.")
)

mc_exam = [
  mcq("w22_12", 2, "In a planned economy, what will determine the allocation of scarce resources?", ["A mixture of private and central decision making", "The decisions of central government", "The forces of demand and supply", "The revenue generated from direct and indirect taxes"], 1, "In a planned economy the state decides, not the market."),
  mcq("s22_12", 2, "What is the main characteristic of a planned economy?", ["All goods and services are produced by privately-owned firms", "All goods and services are produced by state-owned firms", "Private firms produce private goods and state firms produce public goods", "The price mechanism allocates scarce resources through buyers and sellers"], 1, "State ownership and state decision making are the main characteristics. Option C describes a mixed economy and D a market economy."),
  mcq("w23_11", 4, "What is least likely to increase as a result of a transition from a planned economy to a free market economy?", ["Prices of goods and services", "Privately owned resources", "Provision of merit goods", "Structural unemployment"], 2, "A free market tends to under-provide merit goods; prices, private ownership and structural unemployment are likely to rise.")
]

exam = exam_page("the planned economy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The planned economy appears in 8 and 12 mark questions on the economic problem, on switching to a mixed economy and on transition, and in Paper 1 most years. Reworded past questions are below, with three Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "Oct/Nov 2021 (23) Q2(a)"), ("Essay parts, 12 marks", "2", "May/June 2024 (21) Q2(b); Oct/Nov 2021 (21) Q2(b)"), ("Multiple choice (Paper 1)", "3 shown below", "2022 to 2023")],
  [
  eq(P("w21_23", "2(a)"), "8 marks", "Explain how the fundamental economic problem is addressed in a planned economy and in a market economy.",
     ["Knowledge (up to 2): the fundamental economic problem is scarce resources (1) but unlimited wants (1).",
      "Application to a planned economy (up to 3): central planning and government allocation of resources, perhaps with an emphasis on welfare.",
      "Application to a market economy (up to 3): the price mechanism, with rationing, signalling and the interaction of demand and supply."],
     "Scarcity. Planned: government decides what, how and for whom. Market: price mechanism and profit.",
     [[("k", "The fundamental economic problem is that resources are scarce but wants are unlimited, so choices must be made about what, how and for whom to produce.")], [("n", "In a planned economy the government decides. A central authority sets output targets, directs resources to chosen industries and decides how output is shared, often aiming for a fairer distribution.")], [("n", "In a market economy the price mechanism decides. Prices ration scarce goods to those willing and able to pay, signal consumer preferences to firms and give firms an incentive to supply what is profitable, so demand and supply allocate resources.")]]),
  eq(P("s24_21", "2(b)"), "12 marks", "Assess whether a planned economic system should always switch to a mixed economy.",
     ["Analysis (up to 8): advantages and disadvantages of a planned system, including its emphasis on welfare and the provision of public and merit goods, but the lack of competition may mean inefficient allocation.",
      "Advantages and disadvantages of a mixed economy: it may contain the best of both systems, but this depends on how mixed it is; the ease of the switch can also be assessed.",
      "Balanced analysis reaches the top level; one-sided answers are limited. Evaluation (up to 4): a valid conclusion."],
     "Planned: pros and cons. Mixed: pros and cons. Judge: depends on the starting point and the speed of the switch.",
     [[("k", "A planned economy has strengths: the state can provide public and merit goods for everyone, aim for equity and direct resources to long-term goals. Its weaknesses are the lack of price signals and competition, which can cause shortages, inefficiency and limited choice."), ("n", "A mixed economy keeps the efficiency and choice of markets, while the government provides public goods and corrects market failure. Its disadvantages are possible government failure, and that the outcome depends on how the balance is set.")], [("e", "A switch is probably beneficial if the planned economy suffers from inefficiency and shortages, but it may bring unemployment and inequality in the short run, and the benefit depends on how quickly it is done. So a planned economy should not always switch, but a move towards mixed is likely to help where the planning system is failing.")]]),
  eq(P("w21_21", "2(b)"), "12 marks", "Discuss whether the advantages of a transition from a planned economy to a market economy always outweigh the disadvantages.",
     ["Analysis (up to 8): advantages of a market economy: the price mechanism, prices as signals of consumer preferences, private ownership and decision-making with little government intervention, competition leading to efficiency.",
      "Disadvantages: some products under-provided and under-consumed (merit goods), some over-provided (demerit goods), some not provided at all (public goods), and further consequences of the transition.",
      "Evaluation (up to 4): judgement on whether the advantages always outweigh the disadvantages; reserve 1 mark for a conclusion."],
     "Advantages (prices, competition). Disadvantages (market failure, unemployment, inequality). Judge: depends on speed and institutions.",
     [[("k", "A transition to a market economy introduces a price mechanism that signals what consumers want. Private ownership and competition give firms an incentive to be efficient and to innovate, and resources can move quickly to where they are most valued.")], [("n", "But a market economy may under-provide merit goods, over-provide demerit goods and fail to provide public goods. In the transition, state firms may close and cause structural unemployment, prices may rise and inequality may widen.")], [("e", "The advantages do not always outweigh the disadvantages. Gains in efficiency may take years, while the costs fall quickly on workers and the poor. A gradual change with strong institutions and a government that still provides public and merit goods is likely to give the best result.")]])
  ],
  )

tips = tips_html(
  [("Say who decides.", "The government or a central planning authority."),
   ("Name the key weakness.", "No price signals: shortages and surpluses."),
   ("Mention incentives.", "No profit motive, so little innovation."),
   ("Give the strengths.", "Equity, public and merit goods, long-term planning."),
   ("Avoid 'no markets'.", "Informal markets exist."),
   ("Cover transition.", "Efficiency gains versus unemployment and inequality."),
   ("Judge.", "Depends on the speed and the institutions.")],
  [("Planned economy", "In a planned economy the state decides how resources are allocated."),
   ("Central planning", "Central planning is the setting of output targets by a government authority."),
   ("Shortage", "A shortage arises when demand exceeds supply at the set price."),
   ("State ownership", "State ownership means the government owns the factors of production."),
   ("Transition", "Transition is the move from a planned to a market economy.")],
  [CW["define"], CW["explain"], CW["assess"], CW["discuss"]]) + FC

js = SDJS + CHAINJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["State ownership", "Government owns resources and most firms", 20, "f1"], ["Central planning", "Targets and prices set from the centre", 270, "f2"], ["Allocation by plan", "Resources directed, not bought", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="State ownership, central planning and allocation by plan are features of a planned economy">${o}</svg>`;
})();
$("#pic2").innerHTML = (() => {
  const B = [["No price signals", "Planners lack information", 20, "f3"], ["Weak incentives", "Little reward for efficiency", 270, "f3"], ["Result", "Shortages, surpluses, little choice", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="No price signals and weak incentives lead to shortages and surpluses">${o}</svg>`;
})();
const plLab = { x: "Quantity", y: "Price", D1: "Demand", S1: "Cost of supply", P1: "P*", Q1: "Q*" };
function plDraw(q, p, k = 1) {
  const qd = (90 - p) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, plLab);
  o += SV.line(70, SDY(p), 720, SDY(p), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(p) - 6, "Planned price " + p, "c3", k, "end");
  o += SV.line(SDX(q), 270, SDX(q), SDY(100) + 20, "c4", { "stroke-width": 2.5, "stroke-dasharray": "6 4", ...op(k) }) + SV.text(SDX(q), 286, "Planned output " + q, "sm", { "text-anchor": "middle", ...op(k) });
  const gap = qd - q; if (Math.abs(gap) > 0.5) o += SV.line(SDX(Math.min(qd, q)), SDY(p) + 16, SDX(Math.max(qd, q)), SDY(p) + 16, "c4", { "stroke-width": 3, ...op(k) }) + SV.text(SDX((qd + q) / 2), SDY(p) + 34, (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 0), "sm", { "text-anchor": "middle", ...op(k) });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The planners' information problem", base: { q: 50, p: 50, k: 0 }, draw: (s) => plDraw(s.q, s.p, s.k), tween: 900, dwell: 5600, steps: [
  { cap: "<b>The market-clearing outcome</b> would be a price of 50 and an output of 50. Planners do not know this.", s: { q: 50, p: 50, k: 0 } },
  { cap: "<b>Planners guess:</b> they set the price at 30 (to keep it affordable) and an output of 30.", s: { q: 30, p: 30, k: 1 } },
  { cap: "<b>At 30, consumers want 75</b> but only 30 are produced: a <b>shortage</b> of 45. Queues and black markets appear.", s: { q: 30, p: 30, k: 1 } },
  { cap: "<b>If planners over-estimate</b> and produce 70 at a price of 60, consumers want only 37.5: a <b>surplus</b> of 32.5 is wasted.", s: { q: 70, p: 60, k: 1 } },
] });
chainStep("#stB", "Why incentives matter", ["Managers and workers are paid whatever the output", "There is no profit or reward for being efficient", "Little effort to cut costs or improve quality", "Low productivity and little innovation", "Output is poorer and consumers have limited choice"], [
  "<b>State ownership</b> removes the profit motive.", "<b>No reward</b> for good performance.", "<b>Quality and cost</b> suffer.", "<b>Innovation</b> is slow.", "<b>The result:</b> shortages and low-quality goods."]);
chainStep("#stC", "The costs and benefits of moving to a market", ["Prices are freed and state firms are privatised", "Competition and private enterprise grow", "Efficiency, choice and innovation improve", "But inefficient state firms close and unemployment rises", "Prices rise and inequality widens; some merit goods are under-provided"], [
  "<b>The transition</b> begins.", "<b>Incentives</b> change.", "<b>Possible long-run gains.</b>", "<b>A short-run cost</b> for workers.", "<b>Other costs:</b> a role for government remains."]);

function labP() {
  if (!["tq", "tp"].every((i) => $("#" + i))) return;
  const q = +$("#tq").value, p = +$("#tp").value, qd = (90 - p) / 0.8, gap = qd - q;
  $("#r1").textContent = Lib.fmtN(qd, 1); $("#r2").textContent = q; $("#r3").textContent = Math.abs(gap) < 0.5 ? "None" : (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 1);
  $("#rv").textContent = Math.abs(gap) < 0.5 ? `At a price of ${p} consumers want ${Lib.fmtN(qd, 1)}, exactly the planned output: the plan happens to clear the market.` : gap > 0 ? `At a price of ${p} consumers want ${Lib.fmtN(qd, 1)} but only ${q} are produced: a shortage of ${Lib.fmtN(gap, 1)}, with queues, rationing and black markets.` : `At a price of ${p} consumers want only ${qd} but ${q} are produced: a surplus of ${Lib.fmtN(-gap, 1)} that is wasted. Planners have no price signal to tell them.`;
  $("#labA").innerHTML = plDraw(q, p, 1);
}
Lib.slider($("#g1"), { id: "tq", label: "Planned output ", min: 10, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "tp", label: "Planned price ", min: 20, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labP });
labP();

chooser("h", [
  ["Free provision of essentials", "Strength", "Everyone can access health and education", "Markets provide them only to those who can pay", 4],
  ["Long-term planning of big projects", "Strength", "Resources can be directed to long-term goals", "Markets may neglect projects with distant payoffs", 3],
  ["Greater equality of outcomes", "Strength", "Output is shared more evenly", "Markets reward ability to pay", 4],
  ["No price signals", "Weakness", "Planners cannot match output to preferences, causing shortages and surpluses", "Prices signal scarcity automatically", 5],
  ["Weak incentives", "Weakness", "No profit, so little reward for efficiency or innovation", "Profit motive encourages efficiency", 5],
  ["Limited consumer choice", "Weakness", "Planners decide what is produced", "Consumer spending decides what is produced", 4],
  ["Bureaucracy", "Weakness", "A large administration is costly and slow", "Decentralised decisions respond quickly", 3]
], (it) => `${it[0]}: a ${it[1].toLowerCase()} of planning. ${it[2]}. By contrast, in a market: ${it[3].toLowerCase()}.`, "Importance");
''' + CLASSIFY("cl1", "Which economic system does it best describe?", ["Planned", "Market"],
  [("Output targets are set by a central authority", 0), ("Prices are set by demand and supply", 1), ("Most firms are owned by the state", 0), ("Firms aim to make a profit", 1), ("Resources are directed by an economic plan", 0), ("Consumer spending decides what is produced", 1)],
  "In a planned economy the state decides and owns most resources; in a market economy price and private firms decide.") + CLASSIFY("cl2", "Strength or weakness of a planned economy?", ["Strength", "Weakness"],
  [("Essentials are provided to everyone", 0), ("Shortages and surpluses arise", 1), ("Resources can be directed to long-term projects", 0), ("Little incentive to innovate", 1), ("Greater equality in distribution", 0), ("Limited consumer choice", 1)],
  "Strengths: equity, provision of essentials, long-term planning. Weaknesses: no price signals, weak incentives, limited choice.") + ORDER(
  "Put the effects of a planners' error in order.",
  ["Planners set an output target without price signals", "The target does not match consumers' demand", "Shortages or surpluses arise", "Queues, black markets or wasted output follow"],
  "No price signal, so mismatches.") + MATCH([
  ["Planned economy", "The state decides what, how and for whom"],
  ["Central planning", "Output targets set by a government authority"],
  ["State ownership", "Government owns the factors of production"],
  ["Shortage", "Demand exceeds supply at the set price"],
  ["Surplus", "Supply exceeds demand at the set price"],
  ["Transition", "The move from a planned to a market economy"]]) + CALC([
  {"q": "Demand is Q = (90 − P) ÷ 0.8. The planned price is 30. What quantity do consumers want?", "a": 75, "unit": "", "tol": 0.5, "hint": "(90 − 30) ÷ 0.8.", "sol": "<b>75</b>."},
  {"q": "Planned output at that price is 30. What is the shortage?", "a": 45, "unit": "", "tol": 0.5, "hint": "75 − 30.", "sol": "<b>45 units</b>."},
  {"q": "The planned price is 60 and planned output 70. What is the surplus? (Demand at 60 is 37.5.)", "a": 32.5, "unit": "", "tol": 0.5, "hint": "70 − 37.5.", "sol": "<b>32.5 units</b>."},
  {"q": "A plan targets output growth of 5% a year from 200. What is output after one year?", "a": 210, "unit": "", "tol": 0.5, "hint": "200 × 1.05.", "sol": "<b>210</b>."}]) + MCQ([
  ("In a planned economy resources are allocated by:", ["The state", "Demand and supply", "Consumer choice only", "Private firms"], 0, "Central planning."),
  ("A weakness of a planned economy is:", ["No price signals", "Competition", "Consumer sovereignty", "Profit incentives"], 0, "Planners lack information."),
  ("A strength of a planned economy is:", ["Provision of essentials to all", "Wide consumer choice", "Strong profit incentive", "Rapid response to taste changes"], 0, "Equity and welfare."),
  ("A possible cost of transition to a market is:", ["Structural unemployment", "Lower prices", "Less choice", "More state ownership"], 0, "State firms close."),
  ("Shortages in a planned economy arise because:", ["Planners lack price signals", "Prices rise too fast", "Firms compete too much", "Consumers are too rich"], 0, "No information about demand.")
], "qz1") + CARDS([
  ("Planned economy", "State decides and owns."),
  ("Central planning", "Output targets from the centre."),
  ("Strengths", "Equity, essentials, long-term goals."),
  ("Weaknesses", "No signals, weak incentives, little choice."),
  ("Shortage", "Demand above supply."),
  ("Surplus", "Supply above demand."),
  ("Transition", "Planned to market."),
  ("Reality", "No pure planned economy.")]) + MCQ(mc_exam)

build("as1p", "as-planned-economy", "The Planned Economy", EY,
  "1.4.3: how a planned economy allocates resources, its strengths and weaknesses, and the effects of moving to a market economy. Animated diagrams, labs, drills and past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
