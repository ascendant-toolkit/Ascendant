"""AS syllabus 4.5.4 Consequences of unemployment. Run: python3 tools/artifact-kit/mk_as49.py"""
from asx import *
EY = EYAS("4.5.4")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Unemployment has <b>costs for the unemployed themselves</b> (lost income, falling skills, poorer health and confidence), <b>for firms</b> (weaker demand for their products), <b>for the government</b> (lower tax revenue and higher spending on benefits, which have an opportunity cost) and <b>for the economy</b>, which produces <b>less than it could</b>: output is <b>inside the production possibility curve</b> and below potential output. Long-term unemployment is the most damaging because skills decay and people may become permanently detached from work, and it can worsen <b>inequality, poverty and social problems</b> such as crime. There can be <b>some benefits</b>: firms find it easier and cheaper to hire, and wage and inflation pressures are lower, but these are small compared with the costs. A <b>falling</b> unemployment rate has benefits (more income and output, tax revenue) and risks (<b>inflation</b>, skill shortages and a worse current account).</p></div>

  <h2>1 · Costs of unemployment (4.5.4)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Who</th><th>Consequences</th></tr>
    <tr><td><b>Unemployed individuals</b></td><td>Lower income and living standards; <b>skills decay</b> (more so if long-term); loss of confidence; poorer physical and mental health</td></tr>
    <tr><td><b>Firms</b></td><td><b>Lower demand</b> for goods and services as incomes fall; but easier recruitment and lower wage pressure</td></tr>
    <tr><td><b>Government</b></td><td><b>Less tax revenue</b> (income tax, VAT) and <b>more spending on benefits</b>, so the budget deficit rises; <b>opportunity cost</b> of that money</td></tr>
    <tr><td><b>The economy</b></td><td><b>Wasted resources</b>: output below potential (inside the PPC); lower AD; lower living standards; possibly lower long-run growth (loss of skills)</td></tr>
    <tr><td><b>Society</b></td><td>Greater <b>inequality and poverty</b>, crime, family stress and regional decline where unemployment is concentrated</td></tr>
  </table></div>
  <ul>
    <li><b>Long-term unemployment</b> (over a year) is most damaging: skills fall out of date and employers may avoid hiring long-term jobless people.</li>
    <li><b>Youth and regional unemployment</b> cause particular problems: young people lose early work experience, and a whole area can decline.</li>
    <li><b>Benefits of low unemployment but risks:</b> more output, income and tax revenue, but at very low unemployment <b>wages and inflation</b> rise, there may be <b>skill shortages</b>, and higher incomes can <b>raise imports</b>.</li>
  </ul>

  <h2>2 · The government budget (4.5.4)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>Each unemployed person <b>pays less tax</b> and <b>receives benefits</b>, so rising unemployment worsens the budget twice over (lower revenue, higher spending). These are called <b>automatic stabilisers</b> because they cushion falling demand.</li>
    <li>The <b>opportunity cost</b> of paying for unemployment is the education, health or infrastructure that could have been funded instead.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Organise answers by <b>group affected</b> (individual, firm, government, economy) and pair each consequence with a reason. In evaluation, compare short-term with long-term unemployment and note the <b>costs of low unemployment</b>.</div>
'''

watch = '''
  <h2>1 · Unemployment wastes output</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · The effect on the government's budget</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · The cost of unemployment</h2>
  <p>Estimate the lost output, lost tax and extra benefits for a number of unemployed workers.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Lost output</small><strong id="r1"></strong></div><div><small>Lost tax</small><strong id="r2"></strong></div><div><small>Extra benefits</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of lost output, lost tax revenue and extra benefit spending"></svg></div></div></div>

  <h2>Lab 2 · Who is affected?</h2>
  <p>Choose a group to see how unemployment affects it.</p>
  <div class="card"><div class="grid2"><div><div id="wB" class="btnrow"></div>
    <div class="readout"><div><small>Group</small><strong id="t1"></strong></div><div><small>Main effect</small><strong id="t2"></strong></div><div><small>Offsetting benefit</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A label for the group affected by unemployment"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Cost or benefit?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects on the budget in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("After a factory closes", "A town loses its main employer. Households spend less in local shops, which cut staff in turn. The council collects less tax and pays more in benefits, and young people leave the area.", "multiplied effects on firms and the government.") +
rw("Long-term unemployment", "Someone out of work for several years finds their skills out of date, and employers become reluctant to hire them. This lowers their lifetime income and the economy's potential output.", "skill decay and long-term damage.") +
rw("Youth unemployment", "A person who cannot find a first job misses early experience and training. The effect can reduce their earnings for decades and, across many people, limits future growth.", "long-run costs of unemployment.") +
rw("Very low unemployment", "When almost everyone has a job, employers struggle to find workers and bid up wages. Costs and prices rise, and rising incomes may suck in imports. Low unemployment is good, but not without risk.", "the possible costs of falling unemployment.")
)

mc_exam = [
  mcq("s24_13", 18, "What is a cost of negative economic growth?", ["deteriorating balance of payments", "higher inflation", "higher unemployment", "increased pollution"], 2, "A falling real GDP means firms need fewer workers, so unemployment rises."),
  mcq("s24_11", 18, "A major trading nation, country X, is in equilibrium at the full employment level of real output. There is then a recession in its main international markets. What are the most likely consequences of this change for country X? (rate of inflation, unemployment)", ["decrease, decrease", "decrease, increase", "unchanged, decrease", "unchanged, increase"], 1, "Falling export demand shifts AD left, lowering the price level and output, so unemployment rises."),
  mcq("s20_11", 1, "The transition of centrally planned economies to market economies was accompanied by a significant change in the composition of output. What was an immediate consequence of this transition?", ["a build-up of unsold stocks of goods", "an increase in exports of goods", "an increase in unemployment", "decreasing prices of goods and services"], 2, "Closing inefficient state industries created structural unemployment.")
]

exam = exam_page("the consequences of unemployment",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The consequences of unemployment appear mostly in short data-response parts (2 to 6 marks) and occasionally in Paper 1. Reworded past questions are below, with three Paper 1 multiple choice questions.",
  [("Data response, 2 to 6 marks", "3", "May/June 2025 (22) Q1(b); May/June 2025 (24) Q1(e); Feb/March 2024 (22) Q1(d)"), ("Multiple choice (Paper 1)", "3 shown below", "2020 to 2024")],
  [
  eq(P("s25_22", "1(b)"), "2 marks", "Identify one possible impact on firms and one possible impact on the government of a very high rate of unemployment.",
     ["Firms may find it easier or cheaper to recruit labour, may pay lower wages, or may suffer weaker demand for their products (1).", "The government may have reduced tax revenue or higher welfare payments (1). Maximum 1 mark for each of firms and government."],
     "Firms: weaker demand or cheaper labour. Government: less tax, more benefits.",
     [[("k", "High unemployment lowers incomes and spending, so firms may suffer weaker demand for their products. The government collects less income tax and VAT and pays out more in unemployment benefits.")]]),
  eq(P("s25_24", "1(e)"), "6 marks", "Assess the possible consequences of a falling rate of unemployment for an economy such as Malaysia's.",
     ["Analysis (up to 3): possible positive consequences, such as higher overall income levels and living standards, more government tax revenue and less spending on welfare, which could be spent on infrastructure, education and health, more output and export opportunities, and more investment by firms.",
      "Analysis (up to 3): possible negative consequences, such as demand-pull inflation if AS cannot keep up, cost-push inflation as wages rise and resources become scarce, a decline in labour productivity, and higher demand for imports leading to a current account deficit.",
      "Maximum 4 for analysis; the remaining marks are for a judgement. Generic suggestions are accepted."],
     "Positives: incomes, tax revenue, less welfare, output. Negatives: demand-pull and cost-push inflation, imports. Judge.",
     [[("n", "A falling unemployment rate raises incomes and living standards, and means more people paying tax and fewer claiming benefits, so the government has more to spend on infrastructure, education and health. More employment also means more output. But if AD rises faster than supply, the extra demand may cause demand-pull inflation, shortages of workers can push up wages and costs, and higher incomes could raise imports and widen the current account deficit.")], [("e", "Overall the consequences are mostly positive, because lower unemployment raises output and incomes, but if unemployment falls to very low levels the costs of inflation and a worse trade balance become more significant, so the benefits are not unlimited.")]]),
  eq(P("m24_22", "1(d)"), "6 marks", "A country increases investment in artificial intelligence (AI) in its industries. Assess the possible impact on unemployment.",
     ["Analysis (up to 3): possible increases in unemployment, as AI replaces workers in some jobs (technological and structural unemployment), especially for low-skilled workers who lack the skills to move.",
      "Analysis (up to 3): possible reductions in unemployment, as AI raises productivity and growth, creates new industries and jobs, and lowers costs, which raises demand and output.",
      "A judgement on the overall impact, depending on retraining, time period and the pace of change."],
     "Jobs lost: technological and structural unemployment. Jobs created: new industries, higher growth. Judge: depends on retraining and timing.",
     [[("n", "AI can replace workers in routine tasks, so some people lose their jobs, which is technological unemployment. If their skills do not match new jobs, the unemployment is structural and may last. On the other hand, AI raises productivity and lowers costs, which can raise output and demand, and creates jobs in new industries such as software and maintenance.")], [("e", "In the short run AI is likely to raise unemployment for workers in affected industries. In the long run the effect depends on how quickly workers retrain and whether economic growth creates enough new jobs, so the overall impact may be small or even positive.")]])
  ],
  )

tips = tips_html(
  [("Organise by group affected.", "Individual, firm, government, economy, society."),
   ("Pair each effect with a reason.", "Lower income, so less spending."),
   ("Use the PPC.", "Unemployment means output inside the curve."),
   ("Mention government finances twice.", "Less tax revenue and more benefits."),
   ("Long-term is worst.", "Skills decay."),
   ("Give the costs of low unemployment too.", "Inflation, shortages, imports."),
   ("Judge short run versus long run.", "Retraining matters.")],
  [("Opportunity cost", "Benefit payments have an opportunity cost in other government spending."),
   ("Output", "Unemployment means the economy produces less than it could."),
   ("Tax revenue", "Higher unemployment lowers government tax revenue."),
   ("Long-term", "Long-term unemployment causes skills to decay."),
   ("Assess", "The consequences depend on the type and duration of unemployment.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- PPC and unemployment ---------- */
function ppDraw(s) {
  const X = (q) => 80 + q * 6, Y = (p) => 270 - p * 2.4; let o = axes(80, 270, 700, 30, "Capital goods", "Consumer goods"), d = "";
  for (let a = 0; a <= 90; a += 5) { const r = a * Math.PI / 180, x = 85 * Math.cos(r), y = 95 * Math.sin(r); d += (a ? " L" : "M") + X(x) + "," + Y(y); }
  o += SV.path(d, "c2", { fill: "none", "stroke-width": 3.5 }) + tag(X(75), Y(18), "PPC", "c2");
  const f = 1 - 0.3 * s.u, px = 60 * f, py = 66 * f; o += SV.circle(X(px), Y(py), 8, "dot3") + SV.text(X(px) + 14, Y(py) + 4, s.u > 0.5 ? "Actual output (unemployment)" : "Full employment", "lbl bd", { ...halo });
  if (s.u > 0.5) { const qx = 60, qy = 66; o += SV.line(X(px), Y(py), X(qx) - 4, Y(qy) + 4, "dash") + SV.circle(X(qx), Y(qy), 6, "dot1", op(0.6)) + SV.text(X(qx) + 10, Y(qy) - 8, "Potential", "sm"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Output inside the production possibility curve because of unemployment">${ppDraw({ u: 1 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Unemployment and the production possibility curve", base: { u: 0 }, draw: ppDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Full employment.</b> The economy uses all its resources and produces on the PPC.", s: { u: 0 } },
  { cap: "<b>Unemployment.</b> Workers and capital are idle, so the economy produces at a point <b>inside</b> the PPC: less of both goods than it could.", s: { u: 1 } },
  { cap: "<b>Recovery.</b> When the unemployed find work, output moves back towards the PPC, raising living standards.", s: { u: 0 } },
] });

function bgDraw(s) {
  const Y = (v) => 250 - v * 2; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const tax = 100 - 12 * s.u, ben = 30 + 18 * s.u;
  o += SV.rect(150, Y(tax), 120, 250 - Y(tax), "f2", op(0.65)) + SV.text(210, 270, "Tax revenue", "sm", { "text-anchor": "middle" }) + SV.text(210, Y(tax) - 6, Lib.fmtN(tax, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(330, Y(ben), 120, 250 - Y(ben), "f3", op(0.65)) + SV.text(390, 270, "Benefit spending", "sm", { "text-anchor": "middle" }) + SV.text(390, Y(ben) - 6, Lib.fmtN(ben, 0), "lbl bd", { "text-anchor": "middle" });
  o += SV.rect(510, Y(Math.max(0, ben - tax + 70)), 120, 250 - Y(Math.max(0, ben - tax + 70)), "f1", op(0.65)) + SV.text(570, 270, "Pressure on budget", "sm", { "text-anchor": "middle" }) + SV.text(570, Y(Math.max(0, ben - tax + 70)) - 6, Lib.fmtN(ben - tax + 70, 0), "lbl bd", { "text-anchor": "middle" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Tax revenue falls and benefit spending rises as unemployment rises">${bgDraw({ u: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 290, label: "Tax revenue and benefit spending as unemployment rises", base: { u: 0 }, draw: bgDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Low unemployment.</b> Tax revenue is high and benefit spending low.", s: { u: 0 } },
  { cap: "<b>Unemployment rises.</b> Fewer people pay income tax and VAT, so revenue falls, and more people claim benefits, so spending rises.", s: { u: 1 } },
  { cap: "<b>A recession deepens.</b> The gap between spending and revenue widens: a larger budget deficit, with an opportunity cost for other services.", s: { u: 2 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  if (!["un", "wg", "tx", "bn"].every((i) => $("#" + i))) return;
  const u = +$("#un").value, w = +$("#wg").value, t = +$("#tx").value / 100, b = +$("#bn").value, out = u * w / 1000, tax = out * t, ben = u * b / 1000;
  $("#r1").textContent = "$" + Lib.fmtN(out, 1) + "bn"; $("#r2").textContent = "$" + Lib.fmtN(tax, 1) + "bn"; $("#r3").textContent = "$" + Lib.fmtN(ben, 1) + "bn";
  $("#rv").textContent = `${u} thousand unemployed workers who could earn $${Lib.fmtN(w, 0)} each would produce about $${Lib.fmtN(out, 1)}bn a year. The government loses $${Lib.fmtN(tax, 1)}bn in tax and pays $${Lib.fmtN(ben, 1)}bn in benefits: a swing of $${Lib.fmtN(tax + ben, 1)}bn against the budget, which could have funded other services (the opportunity cost).`;
  const Y = (v) => 250 - v * 14; let o = SV.line(40, 250, 400, 250);
  [["Lost output", out, "f1"], ["Lost tax", tax, "f3"], ["Extra benefits", ben, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Math.max(30, Y(v)), 80, 250 - Math.max(30, Y(v)), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Math.max(30, Y(v)) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "un", label: "Number of unemployed, thousands ", min: 100, max: 1000, step: 50, value: 500, fmt: (v) => v, onInput: labC });
Lib.slider($("#g2"), { id: "wg", label: "Output each could produce, $ per year ", min: 20000, max: 60000, step: 5000, value: 40000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labC });
Lib.slider($("#g3"), { id: "tx", label: "Average tax rate on that income, % ", min: 10, max: 40, step: 5, value: 25, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "bn", label: "Benefit paid per unemployed person, $ per year ", min: 5000, max: 20000, step: 1000, value: 9000, fmt: (v) => "$" + Lib.fmtN(v, 0), onInput: labC });
labC();

/* ---------- Lab 2 ---------- */
const GR = [["Unemployed individuals", "Lower income, skill decay, poorer health", "More leisure time (small)", "Income falls, so living standards and spending fall. The longer the spell, the more skills and confidence decay."], ["Firms", "Weaker demand for products", "Easier and cheaper recruitment", "Falling incomes cut spending, so firms sell less, but they may hire at lower wages."], ["The government", "Lower tax revenue and more benefits", "Less wage pressure and lower inflation", "The budget deficit rises, and the money has an opportunity cost in schools or hospitals."], ["The economy", "Output below potential, inside the PPC", "Lower inflation pressure", "Wasted resources reduce living standards and may reduce long-run growth if skills are lost."], ["Society", "Poverty, inequality and social problems", "None significant", "Concentrated unemployment can lead to crime, family stress and regional decline."]];
function showG(i) {
  const [g, m, o, why] = GR[i]; $$("#wB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = g; $("#t2").textContent = m; $("#t3").textContent = o; $("#tv").textContent = why;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, g, "lbl bd", { "text-anchor": "middle", style: "font-size:20px" });
}
$("#wB").innerHTML = GR.map((g, i) => `<button class="b" data-i="${i}">${g[0]}</button>`).join("");
$$("#wB button").forEach((b) => (b.onclick = () => showG(+b.dataset.i)));
showG(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Cost or possible benefit of unemployment?", ["Cost", "Possible benefit"],
  [("Lower income for the unemployed", 0), ("Easier recruitment for firms", 1), ("Lower government tax revenue", 0), ("Less pressure on wages and inflation", 1), ("Output below potential", 0), ("Skills decay over time", 0), ("Higher spending on benefits", 0), ("Lower wage costs for employers", 1)],
  "Costs fall on individuals, the government and the economy. Firms may gain easier recruitment and less wage pressure.") + MATCH([
  ["Opportunity cost", "Other spending given up to pay benefits"],
  ["Long-term unemployment", "Out of work for a year or more, with skills decaying"],
  ["Automatic stabiliser", "Benefits and taxes that cushion falling demand"],
  ["Inside the PPC", "Output below potential because resources are idle"],
  ["Hysteresis (skill decay)", "Long spells of unemployment reduce employability"],
  ["Youth unemployment", "Young people miss early work experience"]]) + ORDER(
  "Put the effects of rising unemployment on the budget in order.",
  ["More people lose their jobs", "Income tax and VAT revenue fall", "Spending on unemployment benefits rises", "The budget deficit widens", "Other spending may have to be cut or taxes raised"],
  "Lower revenue plus higher spending widens the deficit.") + CALC([
  {"q": "800,000 unemployed workers could each produce $30,000 a year. What output is lost ($bn)?", "a": 24, "unit": "$bn", "tol": 0.1, "hint": "800,000 × 30,000.", "sol": "<b>$24bn</b>."},
  {"q": "The average tax rate on that income is 20%. How much tax is lost ($bn)?", "a": 4.8, "unit": "$bn", "tol": 0.05, "hint": "0.2 × 24.", "sol": "<b>$4.8bn</b>."},
  {"q": "Benefits of $8,000 a year are paid to each of the 800,000. What is the total ($bn)?", "a": 6.4, "unit": "$bn", "tol": 0.05, "hint": "800,000 × 8,000.", "sol": "<b>$6.4bn</b>."},
  {"q": "What is the total effect on the budget (lost tax plus benefits) ($bn)?", "a": 11.2, "unit": "$bn", "tol": 0.05, "hint": "4.8 + 6.4.", "sol": "<b>$11.2bn</b>."}]) + MCQ([
  ("A cost of unemployment to the government is:", ["Lower tax revenue and higher benefits", "Higher tax revenue", "Lower welfare spending", "A budget surplus"], 0, "Both sides of the budget worsen."),
  ("Unemployment means the economy produces:", ["Inside its PPC", "On its PPC", "Beyond its PPC", "At a fixed point"], 0, "Resources idle."),
  ("The most damaging type of unemployment is often:", ["Long-term", "Frictional", "Seasonal for a week", "Voluntary"], 0, "Skills decay."),
  ("A possible benefit of unemployment for firms is:", ["Easier recruitment", "Higher demand", "Higher tax revenue", "Lower inflation target"], 0, "More workers available."),
  ("Very low unemployment can cause:", ["Wage and inflation pressure", "Deflation", "Lower AD", "A budget surplus always"], 0, "Labour shortages.")
], "qz1") + CARDS([
  ("Individual", "Lower income, skill decay."),
  ("Firms", "Weaker demand."),
  ("Government", "Less tax, more benefits."),
  ("Economy", "Inside the PPC."),
  ("Society", "Inequality, crime."),
  ("Long-term", "Most damaging."),
  ("Low unemployment", "Inflation risk."),
  ("Opportunity cost", "Spending forgone.")]) + MCQ(mc_exam)

build("as49", "as-consequences-of-unemployment", "Consequences of Unemployment", EY,
  "4.5.4: the economic and social costs of unemployment for individuals, firms, the government and the economy, and the possible benefits. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
