"""AS syllabus 5.4 Supply-side policy. Run: python3 tools/artifact-kit/mk_as55.py"""
from asx import *
EY = EYAS("5.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Supply-side policy</b> consists of government measures designed to <b>increase aggregate supply</b>, mainly by shifting the <b>long-run aggregate supply (LRAS)</b> curve to the right so the economy can produce more at full employment. Its objectives are to increase <b>productivity</b> and <b>productive capacity</b>, which supports economic growth, lower unemployment and lower inflation. <b>Tools</b> include spending on <b>education and training</b>, <b>infrastructure</b>, support for <b>technology and research</b>, tax incentives for work and investment, <b>deregulation</b>, <b>privatisation</b> and reducing labour market rigidities. The effects are mostly <b>long term</b>, uncertain and costly: in the short run extra government spending also raises AD, and policies can take years to raise productivity.</p></div>

  <h2>1 · Meaning and objectives (5.4.1 to 5.4.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li>Supply-side policies aim to shift the <b>LRAS curve to the right</b>, raising potential output. They are also called <b>aggregate supply policies</b>.</li>
    <li><b>Objectives:</b> raise <b>productivity</b> (output per worker); increase <b>productive capacity</b> (more and better factors of production); increase competition and efficiency; reduce structural unemployment.</li>
    <li><b>Benefits if successful:</b> higher real output, lower unemployment, <b>lower price level</b> (or lower inflation), better international competitiveness and a stronger current account.</li>
  </ul>

  <h2>2 · Tools (5.4.3)</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples</th><th>How it raises supply</th></tr>
    <tr><td><b>Investment in human capital</b></td><td>Education, training and apprenticeships, health care</td><td>More skilled, productive, healthy workers; fewer skill mismatches</td></tr>
    <tr><td><b>Infrastructure and technology</b></td><td>Roads, ports, broadband, research grants, tax relief for R&amp;D</td><td>Lower firms' costs, raise productivity, speed innovation</td></tr>
    <tr><td><b>Incentives</b></td><td>Lower income tax, reduced corporation tax, lower benefits for the long-term unemployed</td><td>Encourage work, enterprise and investment</td></tr>
    <tr><td><b>Market reforms</b></td><td>Deregulation, privatisation, cutting red tape, free trade zones, flexible labour markets</td><td>Increase competition and efficiency, lower costs</td></tr>
  </table></div>

  <h2>3 · AD/AS analysis and evaluation (5.4.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Effect on the diagram:</b> LRAS (and SRAS) shift right: <b>real output rises, the price level falls</b>, employment rises. If AD also rises, the price level may stay stable while output grows.</li>
    <li><b>Short run:</b> spending on education or roads is also <b>government spending</b>, so it raises <b>AD</b> first, which may raise prices before supply improves.</li>
    <li><b>Limits:</b> <b>time lags</b> (years before training raises productivity); <b>high cost</b> and opportunity cost; <b>uncertain results</b> (training may not match skills needed); incentive policies may widen inequality; deregulation can harm consumers or the environment; privatised firms may exploit market power.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Link each tool to a shift of <b>LRAS</b> and explain <b>how</b> it raises productivity or capacity. Always separate <b>short-run</b> AD effects from <b>long-run</b> supply effects, and evaluate with time lags, cost and uncertainty.</div>
'''

watch = '''
  <h2>1 · Supply-side policy shifts LRAS</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stL"></div>
  <h2>2 · Short run and long run</h2>
  <div id="stS"></div>
'''

explore = '''
  <h2>Lab 1 · Build a supply-side package</h2>
  <p>Increase spending on each tool. The long-run effect shifts LRAS to the right, with diminishing returns and a cost.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>LRAS shift</small><strong id="r1"></strong></div><div><small>Potential output</small><strong id="r2"></strong></div><div><small>Total cost</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD, SRAS and LRAS with LRAS shifted by the supply-side package"></svg></div></div></div>

  <h2>Lab 2 · Which policy, and what is the catch?</h2>
  <p>Choose a supply-side policy to see how it works and its main drawback.</p>
  <div class="card"><div class="grid2"><div><div id="pB" class="btnrow"></div>
    <div class="readout"><div><small>Type</small><strong id="t1"></strong></div><div><small>Raises supply by</small><strong id="t2"></strong></div><div><small>Main drawback</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A label for the chosen supply-side policy"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Is it a supply-side policy?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the long-run effect of training in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Apprenticeships and training", "A government funds training programmes so workers gain skills that employers need. Productivity rises and structural unemployment falls, shifting LRAS right, but the benefits take years to appear.", "human capital as a supply-side tool.") +
rw("Broadband and transport links", "New rail and fibre networks lower firms' costs and open new markets. Capital spending adds to AD at once and to productive capacity over the long run.", "infrastructure raising AS.") +
rw("Cutting red tape", "Simplifying the rules for starting a business makes it quicker and cheaper to set up firms, encouraging enterprise and competition. But less regulation might reduce consumer protection or environmental standards.", "deregulation and its drawbacks.") +
rw("Privatisation", "Selling a state-owned industry to private owners gives managers a profit motive and exposes the industry to competition, which may cut costs. It can also create a private monopoly that raises prices.", "market-based supply-side policy and its risks.")
)

mc_exam = [
  mcq("m24_12", 23, "What can be considered an expansionary supply-side policy?", ["an increase in government expenditure on training", "an increase in sales tax", "an increase in the rate of interest", "an increase of the exchange rate"], 0, "Training raises productivity and capacity, shifting aggregate supply right."),
  mcq("s25_11", 24, "What is not an example of an expansionary supply-side policy?", ["a reduction in government spending on training", "an increase in support for technological improvement", "a reduction in payments to the unemployed", "an increase in privatisation of industry"], 0, "Cutting training would reduce skills. The others aim to raise supply."),
  mcq("m25_12", 21, "A government cuts income tax. Why might this be seen as an example of a supply-side policy?", ["Real incomes are increased", "The costs of businesses are reduced", "The opportunity cost of unemployment has increased", "The standard of living has improved"], 2, "Lower income tax raises the reward for working, so the opportunity cost of not working rises, encouraging people into work."),
  mcq("s20_13", 14, "What is most likely to occur when the government privatises public sector organisations?", ["Consumer choice will increase", "Employment will increase in the short run", "Innovation will be discouraged", "The production of public goods will increase"], 0, "Privatisation usually increases competition and choice."),
  mcq("s21_13", 28, "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target? (main aim, policy measure)", ["economic growth, deregulation", "full employment, increasing the money supply", "income equality, more progressive taxation", "stable prices, decreasing interest rates"], 0, "Deregulation is a supply-side measure aimed at growth. The others are demand-side or distribution policies."),
  mcq("s25_12", 4, "A country increases its spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect of these changes on human capital and physical capital?", ["human capital decreases, physical capital decreases", "human capital decreases, physical capital increases", "human capital increases, physical capital decreases", "human capital increases, physical capital increases"], 2, "Education and training raise human capital. Taxes on imported machinery make capital goods dearer, so physical capital is likely to fall.")
]

exam = exam_page("supply-side policy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Supply-side policy is a 12 mark Paper 2 discussion in most series (long-run growth, unemployment, inflation) and an 8 mark AD/AS explanation, with short data-response parts. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "Oct/Nov 2020 (23) Q4(a); May/June 2025 (24) Q4(a)"), ("Essay parts, 12 marks", "5", "Oct/Nov 2020 (23) Q4(b); May/June 2024 (22) Q4(b); Oct/Nov 2023 (23) Q4(b); Oct/Nov 2024 (22) Q4(b); Feb/March 2025 (22) Q5(b)"), ("Data response, 6 marks", "1", "May/June 2024 (21) Q1(e)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2025")],
  [
  eq(P("w20_23", "4(a)"), "8 marks", "A government embarks on a supply-side policy involving substantial additional funding for new road schemes and for new training schemes designed to raise labour productivity. Use an AD/AS diagram to explain the effects of this funding on the level of output in the economy.",
     ["Knowledge (up to 2): an accurate AD/AS diagram showing national output in equilibrium (2).",
      "Application (up to 6): a clear understanding of aggregate demand (1), with the diagram showing that the AD curve shifts right because of the increase in government spending (1) and that this increases national output (1); a clear understanding of aggregate supply (1), with the diagram showing that the AS curve shifts right because of the increase in productivity (1) and that this increases national output (1)."],
     "AD/AS diagram. Short run: spending shifts AD right, output up. Long run: productivity shifts AS right, output up again.",
     [[("k", "On an AD/AS diagram with the price level and real output on the axes, the initial equilibrium is where AD meets SRAS.")], [("n", "Funding for roads and training is government spending, a component of AD, so AD shifts to the right and national output rises in the short run. Over the longer term, the training raises labour productivity and the roads lower firms' costs, so AS shifts to the right as well, raising national output further and holding down the price level.")]]),
  eq(P("w20_23", "4(b)"), "12 marks", "Discuss the extent to which a supply-side policy involving new road schemes and new training schemes will increase the rate of inflation in the economy.",
     ["Analysis (up to 8): the short-run effect: spending raises AD, which may raise prices if there is no spare capacity (up to 4); the long-run effect: higher productivity and capacity raise AS, which reduces inflationary pressure (up to 4).",
      "Evaluation (up to 4): a judgement on the extent to which the policy increases inflation, depending on spare capacity, time lags and the size of the AS effect, with a conclusion."],
     "Short run: AD up, inflation risk if at capacity. Long run: AS up, price level falls. Judge: depends on spare capacity and time lags.",
     [[("n", "In the short run, spending on roads and training is injected into the economy as government spending and raises AD. If the economy has no spare capacity, the rise in AD mainly raises the price level, so inflation could increase. Over time, better roads and a more productive workforce lower costs and raise capacity, so AS shifts right, which reduces inflationary pressure and may lower the price level.")], [("e", "The policy is more likely to raise inflation in the short run, particularly in an economy near full capacity, but the long-run effect is likely to reduce it. Overall the extent of any inflation depends on spare capacity and on how quickly supply improves.")]]),
  eq(P("s24_22", "4(b)"), "12 marks", "Assess whether supply-side policy is the most effective way to achieve long-run economic growth.",
     ["Analysis (up to 8): how supply-side policies, such as education, training, infrastructure and technology, raise productive capacity and shift LRAS right, giving sustainable growth (up to 4); the limits of supply-side policy (cost, time lags, uncertainty) and alternatives such as expansionary fiscal or monetary policy and their limits (up to 4).",
      "Evaluation (up to 4): a judgement on whether supply-side policy is the most effective way to achieve long-run growth, with a conclusion."],
     "Supply-side: LRAS shifts right, sustainable. Limits: lags, cost. Demand-side: raises growth only if spare capacity. Judge: best for long-run growth, with demand support.",
     [[("n", "Supply-side policies raise productivity and productive capacity, shifting LRAS to the right, so output can grow without inflation. Education, training and infrastructure all do this. They take years to work, cost money and may not be well targeted, so they are uncertain. Expansionary fiscal and monetary policy raise AD and can raise output in the short run, but without spare capacity they only raise prices, so they cannot achieve long-run growth by themselves.")], [("e", "Supply-side policy is the most effective way to achieve long-run growth, because only increases in capacity can sustain higher output. But it needs sufficient demand to use the extra capacity, so a combination of policies is likely to work best.")]]),
  eq(P("m25_22", "5(b)"), "12 marks", "Assess the extent to which supply-side policy is the best method to reduce the rate of inflation.",
     ["Analysis (up to 8): how supply-side policy reduces inflation by shifting AS to the right, lowering costs and the price level (up to 4); at least one alternative, such as contractionary monetary or fiscal policy, analysed, with the limits of each (up to 4).",
      "Evaluation (up to 4): a judgement depending on the cause of inflation, time lags and the costs of each policy, with a conclusion."],
     "Supply-side: lowers costs, price level falls, long run. Alternatives: monetary, fiscal: quicker but cut output. Judge by cause of inflation and time horizon.",
     [[("n", "Supply-side policies such as training and investment in technology raise productivity, lower unit costs and shift AS to the right, which reduces the price level without cutting output. They are particularly suited to cost-push inflation. However, they take years to work and are costly. Contractionary monetary policy, through higher interest rates, reduces AD more quickly but cuts output and employment, and fiscal policy has similar effects.")], [("e", "Supply-side policy is likely to be the best long-run method, because it reduces inflation while raising output, but it is too slow to deal with high inflation in the short run, when monetary policy is usually needed. The best choice depends on the cause of inflation and the time available.")]])
  ],
  )

tips = tips_html(
  [("Define it.", "Policies to increase aggregate supply, shifting LRAS right."),
   ("Name tools and explain each.", "Education, infrastructure, technology, deregulation, incentives."),
   ("Draw LRAS shifting right.", "Output up, price level down."),
   ("Separate short run from long run.", "Spending raises AD first; supply improves later."),
   ("Mention time lags and cost.", "Years to work; opportunity cost."),
   ("Say which problems it suits.", "Structural unemployment, cost-push inflation."),
   ("Judge with a mix of policies.", "Supply needs demand to be used.")],
  [("Supply-side policy", "Supply-side policy is designed to increase aggregate supply and shift LRAS to the right."),
   ("Productivity", "Supply-side policy aims to raise productivity and productive capacity."),
   ("Human capital", "Education and training raise human capital."),
   ("Time lags", "The effects of supply-side policy often take years to appear."),
   ("Evaluation", "It depends on spare capacity, cost and how well the policy is targeted.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
function slDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="LRAS and SRAS shifting right, raising output and lowering the price level">${slDraw({ a: 0, s: 15, l: 15, n: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifts right first, then supply shifts right">${slDraw({ a: 10, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "A supply-side policy shifts LRAS and SRAS to the right", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD and SRAS meet at output 50 and price level 50. Potential output (LRAS) is 75.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Supply-side policy.</b> Better training, infrastructure and technology raise productivity and capacity. SRAS and LRAS shift <b>right</b>.", s: { a: 0, s: 15, l: 15, n: 1 } },
  { cap: "<b>The result:</b> real output rises, the price level falls and employment rises. Potential output has increased: long-run economic growth.", s: { a: 0, s: 15, l: 15, n: 1 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 300, label: "The short-run demand effect and the long-run supply effect", base: { a: 0, s: 0, l: 0, n: 0 }, draw: slDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is in equilibrium.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Short run.</b> The government spends on roads and training. This is government spending, so <b>AD shifts right</b> first: output rises but so may the price level.", s: { a: 10, s: 0, l: 0, n: 1 } },
  { cap: "<b>Long run.</b> As workers become more productive and transport improves, <b>SRAS and LRAS shift right</b>. Output rises further and the price level is held down.", s: { a: 10, s: 15, l: 15, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!["tr", "in", "rd", "dr"].every((i) => $("#" + i))) return;
  const [t, f, r, d] = ["tr", "in", "rd", "dr"].map((k) => +$("#" + k).value), raw = 0.5 * t + 0.4 * f + 0.5 * r + 0.3 * d, sh = Math.min(25, raw), cost = t + f + r + d * 0.5;
  $("#r1").textContent = Lib.fmtN(sh, 1) + " units right"; $("#r2").textContent = Lib.fmtN(75 + sh, 1); $("#r3").textContent = "$" + Lib.fmtN(cost, 0) + "bn";
  $("#rv").textContent = sh < 0.5 ? "No spending on the tools, so LRAS stays at 75." : `Spending of $${Lib.fmtN(cost, 0)}bn shifts LRAS right by ${Lib.fmtN(sh, 1)} to ${Lib.fmtN(75 + sh, 1)}. The effect takes years and has diminishing returns (it is capped at 25). In the short run the spending also raises AD, so inflation could rise before capacity grows.`;
  $("#labA").innerHTML = adasPlot({ a: 0, s: sh * 0.6, l: sh, g: 1, n: 1 });
}
[["g1", "tr", "Education and training, $bn ", 10], ["g2", "in", "Infrastructure, $bn ", 10], ["g3", "rd", "Technology and R&D support, $bn ", 5], ["g4", "dr", "Deregulation and reforms (effort), index ", 10]].forEach(([el, id, lab, v]) => Lib.slider($("#" + el), { id, label: lab, min: 0, max: 30, step: 5, value: v, fmt: (z) => z, onInput: labP }));
labP();

/* ---------- Lab 2 ---------- */
const PL = [["Education and training", "Human capital", "More skilled, productive workers", "Takes years; may not match skills needed"], ["Infrastructure spending", "Capital and technology", "Lower costs; better access to markets", "High cost; long delay; raises the deficit"], ["Lower income tax", "Incentive", "More work effort and enterprise", "May widen inequality; reduces revenue"], ["Deregulation", "Market reform", "Easier entry, more competition and efficiency", "Weaker consumer or environmental protection"], ["Privatisation", "Market reform", "Profit motive and competition cut costs", "Possible private monopoly power"], ["Cutting benefits for the long-term unemployed", "Incentive", "Encourages people to seek work", "Hardship; may not create jobs"]];
function showP(i) {
  const [n, t, h, d] = PL[i]; $$("#pB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = t; $("#t2").textContent = h; $("#t3").textContent = d; $("#tv").textContent = `${n}: it raises supply through "${h.toLowerCase()}", shifting LRAS right over time. The main drawback is that it ${d.toLowerCase()}.`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f2", { rx: 12, ...op(0.45) }) + SV.text(210, 105, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(210, 170, "Type: " + t, "sm", { "text-anchor": "middle" });
}
$("#pB").innerHTML = PL.map((p, i) => `<button class="b" data-i="${i}">${p[0]}</button>`).join("");
$$("#pB button").forEach((b) => (b.onclick = () => showP(+b.dataset.i)));
showP(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Supply-side policy or not?", ["Supply-side", "Demand-side"],
  [("Funding apprenticeships", 0), ("Cutting interest rates", 1), ("Building new ports", 0), ("A cut in VAT to boost spending", 1), ("Tax relief for R&D", 0), ("Deregulating industries", 0), ("Higher government spending on benefits", 1), ("Privatising state industries", 0)],
  "Supply-side policies raise capacity and productivity; demand-side policies change spending.") + MATCH([
  ["Supply-side policy", "Measures to increase aggregate supply"],
  ["LRAS", "Potential output; shifted by supply-side policy"],
  ["Human capital", "Skills and knowledge of the workforce"],
  ["Deregulation", "Removing rules to increase competition and efficiency"],
  ["Privatisation", "Transferring state industries to private ownership"],
  ["Time lag", "Delay before supply improvements appear"]]) + ORDER(
  "Put the long-run effect of training in order.",
  ["The government funds training", "Workers' skills and productivity rise", "Unit costs fall and capacity rises", "LRAS shifts to the right", "Real output rises and the price level falls"],
  "Training raises productivity, shifting LRAS right.") + CALC([
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "A training programme costs $30m and raises output per worker by $200 for 100,000 workers. What is the extra output ($m)?", "a": 20, "unit": "$m", "tol": 0.1, "hint": "200 × 100,000.", "sol": "<b>$20m</b> a year."},
  {"q": "How many years does it take for the extra output to cover the cost?", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5 years</b>."},
  {"q": "A firm's labour costs are 50% of its costs. Productivity rises 10%, so labour cost per unit falls 9.1%. By roughly how much do total unit costs fall (%)?", "a": 4.5, "unit": "%", "tol": 0.2, "hint": "0.5 × 9.1.", "sol": "<b>4.5%</b>."}]) + MCQ([
  ("A supply-side policy aims to:", ["Increase aggregate supply", "Reduce aggregate supply", "Raise interest rates", "Cut government spending only"], 0, "Raise capacity."),
  ("Which is a supply-side policy?", ["Spending on education and training", "A cut in interest rates", "A rise in VAT", "A rise in the money supply"], 0, "Human capital."),
  ("Supply-side policy shifts:", ["LRAS to the right", "AD to the right only", "LRAS to the left", "SRAS to the left"], 0, "More capacity."),
  ("A limit of supply-side policy is:", ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], 0, "Time lags."),
  ("Privatisation may:", ["Increase efficiency through competition", "Lower the quality always", "Raise unemployment always", "Reduce supply"], 0, "Profit motive.")
], "qz1") + CARDS([
  ("Supply-side", "Raise AS and LRAS."),
  ("Tools", "Education, infrastructure, tech, incentives, reforms."),
  ("Effect", "Output up, price level down."),
  ("Short run", "Spending raises AD."),
  ("Long run", "LRAS shifts right."),
  ("Limits", "Lags, cost, uncertainty."),
  ("Suits", "Structural unemployment, cost-push."),
  ("Evaluate", "Mix of policies.")]) + MCQ(mc_exam)

build("as55", "as-supply-side-policy", "Supply-Side Policy", EY,
  "5.4: the meaning, objectives and tools of supply-side policy, and its effect on LRAS in AD/AS analysis. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
