"""AS syllabus 4.4.4-4.4.5 Causes and consequences of economic growth. Run: python3 tools/artifact-kit/mk_as47.py"""
from asx import *
EY = EYAS("4.4.4 to 4.4.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Economic growth has <b>demand-side</b> causes, a rise in <b>aggregate demand</b> (consumption, investment, government spending or net exports) that uses up spare capacity, and <b>supply-side</b> causes, an increase in <b>productive capacity</b> from more or better <b>labour</b>, <b>capital</b>, <b>technology</b>, <b>enterprise</b> and <b>infrastructure</b>, which shifts <b>LRAS</b> right and allows <b>sustained</b> growth. The <b>consequences</b> can be good: <b>higher living standards, lower unemployment, higher tax revenue</b> to fund public services, and more resources for investment and development. They can also be bad: <b>inflation</b> if demand outruns capacity, a <b>current account deficit</b> as imports rise, <b>environmental damage and resource depletion</b>, widening <b>inequality</b>, and congestion. Whether the consequences are positive depends on the <b>source</b> and <b>speed</b> of the growth and on <b>who gains</b>.</p></div>

  <h2>1 · Causes of economic growth (4.4.4)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Causes</th><th>Effect on the diagram</th></tr>
    <tr><td><b>Demand-side (short run)</b></td><td>Lower interest rates, tax cuts, rising confidence, higher government spending, export growth, a weaker currency</td><td>AD shifts right; real output rises, most when there is spare capacity</td></tr>
    <tr><td><b>Supply-side (long run)</b></td><td>More workers (population, immigration, participation); better education and training; <b>net investment</b> in capital; <b>technology</b> and R&amp;D; <b>enterprise</b>; <b>infrastructure</b>; new resources; <b>mobility</b> of factors</td><td>LRAS (and SRAS) shift right; potential output rises; the PPC moves outward</td></tr>
  </table></div>
  <ul>
    <li><b>Sustained growth</b> needs supply-side improvements. Demand-led growth in an economy at full capacity just raises prices.</li>
    <li><b>Measuring the impact</b> of each cause is difficult: the <b>informal economy</b> hides output, causes interact, and time lags are long.</li>
    <li><b>Internal causes</b> (investment, education, technology) and <b>external causes</b> (export demand, commodity prices, foreign investment, world growth) both matter.</li>
  </ul>

  <h2>2 · Consequences of economic growth (4.4.5)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Possible benefits</th><th>Possible costs</th></tr>
    <tr><td><b>Higher living standards</b> (income per head, consumption)</td><td><b>Inflation</b> if AD grows faster than capacity</td></tr>
    <tr><td><b>Lower unemployment</b> as more workers are needed</td><td><b>Current account deficit</b>: rising incomes suck in imports</td></tr>
    <tr><td><b>Higher tax revenue</b>, so more for health, education, welfare and a lower budget deficit</td><td><b>Environmental damage</b>, pollution, resource depletion and climate change</td></tr>
    <tr><td><b>More investment</b> and development; reduced absolute poverty</td><td><b>Inequality</b> may widen; structural unemployment as industries change</td></tr>
    <tr><td>Greater consumer choice; firms' profits rise</td><td>Congestion, longer working hours, loss of leisure; unsustainable boom and bust</td></tr>
  </table></div>
  <ul>
    <li><b>Evaluation:</b> growth is usually beneficial if it is <b>supply-led</b>, <b>sustainable</b> and its gains are <b>widely shared</b>; it is more harmful if it is demand-led near full capacity, based on depleting resources, or raises inequality.</li>
    <li>Compare <b>actual</b> growth (using spare capacity) with <b>potential</b> growth (more capacity), and look at <b>GDP per head</b> and the distribution of income.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For 'always positive' questions, give <b>both</b> sides and then say <b>when</b> growth is more or less beneficial: depending on its source, the economy's spare capacity and who benefits. Do not just list.</div>
'''

watch = '''
  <h2>1 · Demand-led and supply-led growth</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · The virtuous circle of growth</h2>
  <div id="stV"></div>
'''

explore = '''
  <h2>Lab 1 · Sources of growth</h2>
  <p>Growth in potential output depends on more labour, more capital and better productivity or technology. Change each source and see the total.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Contribution: labour</small><strong id="r1"></strong></div><div><small>Contribution: capital</small><strong id="r2"></strong></div><div><small>Growth in potential output</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bars of the contributions of labour, capital and technology to growth"></svg></div></div></div>

  <h2>Lab 2 · Is the growth beneficial?</h2>
  <p>Set the rate of growth, the economy's spare capacity and how much of the growth comes from higher productive capacity.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Inflation pressure</small><strong id="t1"></strong></div><div><small>Current account effect</small><strong id="t2"></strong></div><div><small>Overall</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="Bars showing demand-led growth against spare capacity"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Cause or consequence?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the virtuous circle in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Investing in education and technology", "A country spends heavily on schools and research. Workers become more skilled and firms adopt better methods, so potential output rises. This is supply-side growth, which can last without causing inflation.", "supply-side causes and LRAS shifting right.") +
rw("A consumer boom", "Low interest rates and confidence lead households to borrow and spend. If the economy has spare capacity, output and jobs rise. If it does not, prices rise and the extra spending sucks in imports.", "demand-led growth and its costs.") +
rw("Rapid industrial growth", "A fast-growing economy raises incomes and cuts poverty, but factories and traffic raise air pollution and use up natural resources. The benefits are real, but so are the environmental costs.", "positive and negative consequences.") +
rw("Growth in a few sectors", "If growth is concentrated in mining or finance, a small group may gain most. Average income rises, but inequality widens and workers in declining industries may become unemployed.", "growth and the distribution of income.")
)

mc_exam = [
  mcq("s24_12", 18, "Which change affecting an economy's labour force will cause an increase in economic growth in the short run?", ["an increase in students entering university", "an increase in the birth rate", "an increase in the immigration of skilled labour", "an increase in the school leaving age"], 2, "Skilled immigrants can start work at once, raising output in the short run. The other changes take years."),
  mcq("s23_12", 30, "Economic growth leads to increased levels of income and consumption per capita for the adult population. Which circumstances are needed for this to happen in an economy?", ["a change in technology that maintains the same level of output", "an increase in economic efficiency through higher productivity of factor inputs", "a policy of progressive taxation to reduce inequalities", "a rise in the size of the working population due to immigration"], 1, "Higher productivity raises output per head. A larger population need not raise income per head."),
  mcq("s23_13", 24, "Which government action is least likely to prevent a fall in economic growth?", ["additional controls on commercial banks' lending", "relaxation of rules for immigration of adult population", "removal of trade barriers on import of raw materials", "training and education of workforce"], 0, "Tighter controls on lending reduce credit and spending, so they are least likely to support growth."),
  mcq("s24_12", 20, "What is true about a government's macroeconomic objectives?", ["Economic growth ensures a more even distribution of income", "Increasing output ensures that more workers are employed", "Choosing between macroeconomic objectives requires a normative decision", "A stable rate of inflation means zero inflation is required"], 2, "Choosing between objectives (such as growth against inflation) involves value judgements.")
]

exam = exam_page("the causes and consequences of economic growth",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Growth is one of the most common Paper 2 topics: an 8 mark part on causes and a 12 mark assessment of whether growth is always beneficial in most series, plus short data-response parts. Reworded past questions are below, with four Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "2", "May/June 2025 (23) Q4(a); Oct/Nov 2024 (21) Q4(a)"), ("Essay parts, 12 marks", "4", "Feb/March 2023 (22) Q4(b); Feb/March 2024 (22) Q5(b); May/June 2025 (23) Q4(b); May/June 2023 (22) Q5(b)"), ("Data response, 4 to 6 marks", "3", "Oct/Nov 2023 (21) Q1(b) and (e); Oct/Nov 2023 (23) Q1(c)"), ("Multiple choice (Paper 1)", "4 shown below", "2020 to 2025")],
  [
  eq(P("s25_23", "4(a)"), "8 marks", "Explain two causes of economic growth and consider the extent to which their impact can be measured.",
     ["Knowledge (up to 3): economic growth is the increase in the real value of goods and services produced in an economy over time (1); an explanation of two causes, such as an increase in AD (higher real wages, direct tax cuts, lower interest rates) or increases in LRAS (increased investment, increased productivity) (1 + 1).",
      "Analysis (up to 3): an explanation of how each cause increases economic growth (1 + 1), for example reductions in income tax raise disposable income, AD and growth, though if job insecurity is high the increase may be less; or alternatively that the ability to measure the impact is affected by the size of the hidden or informal economy (1).",
      "Evaluation (up to 2): the extent to which the causes can be measured, such as the size of the informal economy, with a justified conclusion (1)."],
     "Define growth. Two causes, each explained: one demand-side (lower interest rates), one supply-side (investment). Measurement: informal economy, lags.",
     [[("k", "Economic growth is an increase in the real value of goods and services produced in an economy over time. Lower interest rates are one cause, because they make borrowing cheaper and so raise consumption and investment, shifting AD to the right. Increased investment in machinery and technology is another, because it raises productivity and shifts LRAS to the right.")], [("n", "Lower interest rates raise AD, so real GDP rises if there is spare capacity. Investment raises productive capacity, so potential output grows. Each increases real GDP, but the extent can be hard to measure: causes work together, there are time lags, and output in the informal economy is not recorded.")], [("e", "The impact of each cause can be estimated, for example from changes in investment and in GDP, but it cannot be measured exactly because of the hidden economy and because of other influences. So the measurement is approximate.")]]),
  eq(P("w24_21", "4(a)"), "8 marks", "Explain two possible causes of economic growth and consider whether the consequences of economic growth for an economy will always be positive.",
     ["Knowledge (up to 3): what is meant by economic growth (1) and two causes, such as an increase in the number of workers, better education and training, research and development, technology, investment in capital stock, mobility of factors or new export markets (up to 2).",
      "Analysis (up to 3): the possible positive and negative consequences of growth, such as a higher standard of living and lower unemployment, but also inflation, a worse current account, environmental damage and inequality.",
      "Evaluation (up to 2): a judgement on whether the consequences will always be positive, with a conclusion."],
     "Growth defined. Two causes. Consequences: higher living standards, jobs, but inflation, imports, environment, inequality. Judge: not always.",
     [[("k", "Economic growth is an increase in real GDP over time. It could be caused by investment in capital stock, which raises productive capacity, and by improved education and training, which raises the quality of labour.")], [("n", "Growth raises living standards, may cut unemployment, and raises tax revenue for health and education. But if AD grows faster than capacity there may be inflation, higher incomes may raise imports and worsen the current account, and higher output may damage the environment.")], [("e", "The consequences are not always positive. Growth driven by investment and productivity is more likely to be sustainable and beneficial, while rapid demand-led growth is more likely to be inflationary, and the gains may not be shared equally.")]]),
  eq(P("m23_22", "4(b)"), "12 marks", "Assess whether the consequences of economic growth for an economy are always positive.",
     ["Analysis (up to 8): the positive consequences, such as higher living standards, lower unemployment, higher tax revenue and more resources for public services (up to 4); the negative consequences, such as inflation, a current account deficit, environmental damage and inequality (up to 4).",
      "Evaluation (up to 4): a judgement on whether the consequences are always positive, depending on the type of growth, the economy's spare capacity and who benefits, with a conclusion."],
     "Positives: living standards, jobs, tax revenue. Negatives: inflation, imports, environment, inequality. Judge: depends on source, capacity and distribution.",
     [[("n", "Economic growth raises real incomes and living standards, creates jobs and raises tax revenue, which the government can spend on health and education. But growth that comes from rising AD in an economy with little spare capacity pushes up prices, higher incomes raise spending on imports and may widen the current account deficit, and more output can mean pollution and depletion of resources. The benefits may also go mostly to higher earners, so inequality could rise.")], [("e", "Growth is not always positive. It is most beneficial when it comes from higher productive capacity, is sustainable and is widely shared. It is more likely to cause problems when it is driven by demand in a fully employed economy or by activities that damage the environment.")]])
  ],
  )

tips = tips_html(
  [("Split causes into demand and supply.", "AD shifts versus LRAS shifts."),
   ("Name two causes and explain each.", "Do not just list factors."),
   ("Actual versus potential growth.", "Using spare capacity versus raising capacity."),
   ("Give both sides of consequences.", "Benefits and costs."),
   ("Say when growth is beneficial.", "Supply-led, sustainable, shared."),
   ("Mention measurement.", "The informal economy, lags, interacting causes."),
   ("Use GDP per head and distribution.", "Who gains?")],
  [("Growth", "Economic growth is an increase in real GDP over time."),
   ("Demand-led", "Growth driven by AD may raise inflation if capacity is limited."),
   ("Supply-led", "Higher productive capacity shifts LRAS to the right."),
   ("Consequences", "Growth may raise living standards but harm the environment."),
   ("Assess", "The consequences are not always positive: it depends on the source of growth.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
function gcDraw(s) { return adasPlot({ a: s.a, s: s.s, l: s.l, g: 1, n: s.n }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="AD shifting right and LRAS and SRAS shifting right">${gcDraw({ a: 20, s: 15, l: 15, n: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 300, label: "Demand-led and supply-led growth", base: { a: 0, s: 0, l: 0, n: 0 }, draw: gcDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The economy is at output 50, below potential output of 75: there is spare capacity.", s: { a: 0, s: 0, l: 0, n: 0 } },
  { cap: "<b>Demand-led growth.</b> Lower interest rates shift AD to the right. Real output rises to about 60 and prices rise a little. Growth uses up spare capacity.", s: { a: 20, s: 0, l: 0, n: 1 } },
  { cap: "<b>Supply-led growth.</b> Investment and better education shift SRAS and LRAS to the right. Potential output rises to 90, so the economy can keep growing without inflation.", s: { a: 20, s: 15, l: 15, n: 1 } },
] });

function vcDraw(s) {
  const bx = (x, y, t, k, v) => SV.rect(x, y, 170, 52, k, { rx: 8, ...op(0.55 * v) }) + SV.text(x + 85, y + 31, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
  const ar = (x1, y1, x2, y2, d, v) => SV.line(x1, y1, x2, y2, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y2, d, "dot4");
  let o = bx(60, 40, "Economic growth", "f3", s.a) + ar(232, 66, 330, 66, "r", s.b) + bx(335, 40, "Higher incomes and tax revenue", "f1", s.b) + ar(505, 66, 560, 66, "r", s.c) + bx(565, 40, "Spending on education, health, roads", "f2", s.c);
  o += ar(650, 94, 650, 150, "d", s.d) + bx(565, 155, "Higher productive capacity", "f1", s.d) + ar(560, 181, 235, 181, "l", s.e) + bx(60, 155, "LRAS shifts right: more growth", "f3", s.e);
  if (s.f > 0) o += SV.text(380, 255, "Costs to weigh: inflation, imports, pollution, inequality", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)", ...op(s.f) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 280" role="img" aria-label="A virtuous circle from growth to higher incomes and tax revenue, public spending, capacity and more growth">${vcDraw({ a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 })}</svg>`;
Lib.stepper($("#stV"), { w: 760, h: 280, label: "The virtuous circle of economic growth", base: { a: 0, b: 0, c: 0, d: 0, e: 0, f: 0 }, draw: vcDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>Economic growth</b> raises real output.", s: { a: 1 } },
  { cap: "<b>Higher incomes and tax revenue.</b> People earn more, and the government collects more tax without raising rates.", s: { a: 1, b: 1 } },
  { cap: "<b>More public spending</b> on education, health care and infrastructure becomes affordable.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Productive capacity rises:</b> a healthier, more skilled workforce and better infrastructure.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>LRAS shifts right,</b> making further growth possible: a virtuous circle.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
  { cap: "<b>But there are costs to weigh:</b> inflation if demand outruns capacity, a worse current account, pollution and inequality. Growth is not always positive.", s: { a: 1, b: 1, c: 1, d: 1, e: 1, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labG() {
  if (!["lb", "cp", "tf"].every((i) => $("#" + i))) return;
  const l = +$("#lb").value, c = +$("#cp").value, t = +$("#tf").value, a = 0.6 * l, b = 0.4 * c, tot = a + b + t;
  $("#r1").textContent = Lib.fmtN(a, 1) + " pts"; $("#r2").textContent = Lib.fmtN(b, 1) + " pts"; $("#r3").textContent = Lib.fmtN(tot, 1) + "%";
  $("#rv").textContent = `Labour growth of ${l}% (weight 0.6) adds ${Lib.fmtN(a, 1)} points, capital growth of ${c}% (weight 0.4) adds ${Lib.fmtN(b, 1)}, and productivity or technology adds ${t}. Potential output grows ${Lib.fmtN(tot, 1)}% a year. ${t >= a + b ? "Most growth comes from productivity, which is the most sustainable source." : "Most growth comes from adding more labour and capital, which can be limited."}`;
  const Y = (v) => 250 - v * 28; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30) + SV.text(46, 26, "Growth (% points)", "sm"), y = 250;
  [["Labour", a, "f1"], ["Capital", b, "f2"], ["Technology", t, "f3"]].forEach(([n, v, k]) => { const h = v * 28; o += SV.rect(130, y - h, 140, h, k, op(0.65)) + (h > 14 ? SV.text(200, y - h / 2 + 5, n + " " + Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" }) : ""); y -= h; });
  o += SV.text(200, 270, "Total " + Lib.fmtN(tot, 1) + "%", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "lb", label: "Growth in the labour force, % ", min: 0, max: 4, step: 0.5, value: 1.5, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "cp", label: "Growth in the capital stock, % ", min: 0, max: 8, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g3"), { id: "tf", label: "Productivity and technology, % points ", min: 0, max: 4, step: 0.5, value: 1, fmt: (v) => v + "%", onInput: labG });
labG();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!["gg", "sp", "sh"].every((i) => $("#" + i))) return;
  const g = +$("#gg").value, sp = +$("#sp").value, sh = +$("#sh").value / 100, dem = g * (1 - sh), infl = Math.max(0, dem - sp / 2), ca = -0.45 * g;
  $("#t1").textContent = infl < 0.3 ? "Low" : infl < 2 ? "Moderate" : "High"; $("#t2").textContent = Lib.fmtN(ca, 1) + "% of GDP"; $("#t3").textContent = infl < 0.3 && sh > 0.4 ? "Mostly positive" : infl < 2 ? "Mixed" : "Risky";
  $("#tv").textContent = `${g}% growth, ${Lib.fmtN(sh * 100, 0)}% of it from higher capacity, so ${Lib.fmtN(dem, 1)} points are demand-led. With spare capacity of ${sp}% the economy can absorb about ${Lib.fmtN(sp / 2, 1)} points without much inflation, leaving inflation pressure of ${Lib.fmtN(infl, 1)}. Higher incomes also raise imports, which could worsen the current account by about ${Lib.fmtN(-ca, 1)}% of GDP. ${infl > 2 ? "The growth is likely to be inflationary and may not be sustainable." : "The growth looks reasonably sustainable."}`;
  let o = SV.line(40, 180, 400, 180); [["Total growth", g, "f1"], ["Demand-led", dem, "f3"], ["Absorbable", sp / 2, "f2"]].forEach(([n, v, k], i) => (o += SV.rect(70 + i * 110, 180 - v * 18, 80, v * 18, k, op(0.65)) + SV.text(110 + i * 110, 200, n, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, 174 - v * 18, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Real GDP growth, % ", min: 1, max: 9, step: 1, value: 5, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g5"), { id: "sp", label: "Spare capacity in the economy, % of GDP ", min: 0, max: 12, step: 1, value: 4, fmt: (v) => v + "%", onInput: labB });
Lib.slider($("#g6"), { id: "sh", label: "Share of growth from higher productive capacity, % ", min: 0, max: 100, step: 10, value: 30, fmt: (v) => v + "%", onInput: labB });
labB();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Benefit or cost of growth?", ["Possible benefit", "Possible cost"],
  [("Higher living standards", 0), ("Inflation when near full capacity", 1), ("Lower unemployment", 0), ("Pollution and resource depletion", 1), ("Higher tax revenue", 0), ("A bigger current account deficit", 1), ("More resources for health and education", 0), ("Widening inequality", 1)],
  "Growth can raise incomes and jobs but may bring inflation, imports, environmental damage and inequality.") + MATCH([
  ["Demand-led growth", "A rise in AD that uses up spare capacity"],
  ["Supply-led growth", "A rise in productive capacity: LRAS shifts right"],
  ["Net investment", "Spending on capital that adds to the capital stock"],
  ["Productivity", "Output per worker or per unit of input"],
  ["Informal economy", "Unrecorded output, which makes growth hard to measure"],
  ["Sustainable growth", "Growth that can continue without harming future output"]]) + ORDER(
  "Put the virtuous circle of growth in order.",
  ["Economic growth raises output", "Incomes and tax revenue rise", "The government spends more on education and infrastructure", "Productive capacity rises", "LRAS shifts right and growth continues"],
  "Growth, revenue, investment in capacity, more growth.") + CALC([
  {"q": "Labour grows 2% (weight 0.6), capital grows 5% (weight 0.4) and technology adds 1 point. What is growth in potential output (%)?", "a": 4.2, "unit": "%", "tol": 0.1, "hint": "1.2 + 2.0 + 1.", "sol": "<b>4.2%</b>."},
  {"q": "What share of that growth comes from technology (%)?", "a": 23.8, "unit": "%", "tol": 0.3, "hint": "1 ÷ 4.2.", "sol": "<b>23.8%</b>."},
  {"q": "Real GDP grows 5% and imports have an income elasticity of 1.5 with imports at 30% of GDP. By roughly what % of GDP do imports rise?", "a": 2.25, "unit": "%", "tol": 0.1, "hint": "7.5% × 0.3.", "sol": "Imports rise 7.5%, which is <b>2.25%</b> of GDP."},
  {"q": "Real GDP is $400bn. After growth of 3.5% it is: ($bn)", "a": 414, "unit": "$bn", "tol": 0.5, "hint": "400 × 1.035.", "sol": "<b>$414bn</b>."}]) + MCQ([
  ("Which is a supply-side cause of growth?", ["Investment in capital goods", "A cut in interest rates", "A rise in government spending", "A depreciation"], 0, "It raises capacity."),
  ("Demand-led growth is most likely to cause inflation when:", ["The economy is near full capacity", "There is much spare capacity", "AD is falling", "Unemployment is high"], 0, "Output cannot rise."),
  ("A possible consequence of growth is:", ["A rise in imports", "A fall in tax revenue", "A fall in living standards for all", "No change in demand"], 0, "Higher incomes raise import spending."),
  ("Growth is more sustainable when it comes from:", ["Higher productivity", "Borrowing to spend", "Running down natural resources", "Rising prices"], 0, "Higher capacity."),
  ("Growth is measured by the change in:", ["Real GDP", "Nominal GDP", "Prices", "Exports"], 0, "Real, not nominal.")
], "qz1") + CARDS([
  ("Demand-side", "AD shifts right."),
  ("Supply-side", "LRAS shifts right."),
  ("Benefits", "Living standards, jobs, tax revenue."),
  ("Costs", "Inflation, imports, environment, inequality."),
  ("Sustainable", "Productivity-led."),
  ("Measure", "Informal economy limits it."),
  ("Actual growth", "Uses spare capacity."),
  ("Judge", "Source, capacity, distribution.")]) + MCQ(mc_exam)

build("as47", "as-causes-consequences-of-growth", "Causes and Consequences of Economic Growth", EY,
  "4.4.4 to 4.4.5: demand-side and supply-side causes of economic growth, and its possible benefits and costs. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
