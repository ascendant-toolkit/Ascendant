"""AS syllabus 4.5.1-4.5.3 Unemployment: meaning, measurement, causes and types. Run: python3 tools/artifact-kit/mk_as48.py"""
from asx import *
EY = EYAS("4.5.1 to 4.5.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Unemployment</b> means people who are <b>able, available and actively seeking work but cannot find a job</b>; the <b class="kw">unemployment rate</b> is the number unemployed as a percentage of the <b>labour force</b> (the employed plus the unemployed). It is measured by the <b>labour force survey</b> (a sample survey of who is seeking work) and the <b>claimant count</b> (people claiming unemployment benefit), and both have difficulties, such as <b>discouraged workers, hidden unemployment, informal work</b> and people who claim benefits without searching. The main types are <b>frictional</b> (between jobs), <b>structural</b> (mismatch of skills or location after industries decline), <b>cyclical</b> (lack of demand in a recession), <b>seasonal</b> (jobs that depend on the time of year) and <b>technological</b> (machines replace workers). Each has different causes and needs different policies.</p></div>

  <h2>1 · Meaning and measurement (4.5.1 to 4.5.2)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Unemployment rate</b> = (number unemployed ÷ labour force) × 100. The <b>labour force</b> = employed + unemployed (not the whole population, and not those who have stopped looking).</li>
    <li><b>Labour force survey (ILO method):</b> a sample of households is asked whether people are without a job, have looked for work recently and are available to start. It is <b>internationally comparable</b> but costly, depends on the sample and on honest answers.</li>
    <li><b>Claimant count:</b> those registered and claiming unemployment benefit. It is <b>cheap and quick</b> but misses people not eligible or not claiming, and may include people who are working illegally or not really seeking work.</li>
    <li><b>Difficulties:</b> <b>discouraged workers</b> who have given up looking are not counted; <b>underemployment</b> (part-time workers wanting full-time work) and <b>disguised unemployment</b> (people in jobs with little real work) are hidden; the <b>informal economy</b> hides workers; regional and seasonal differences are averaged out; definitions differ between countries.</li>
  </ul>

  <h2>2 · Types and causes (4.5.3)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Cause</th><th>Example</th><th>Typical remedy</th></tr>
    <tr><td><b>Frictional</b></td><td>Time taken to search and match between jobs; imperfect information</td><td>A graduate looking for a first job; Asha rejects an offer to seek better pay</td><td>Better job information, job centres, shorter benefit periods</td></tr>
    <tr><td><b>Structural</b></td><td>Decline of an industry; skills and location mismatch; immobility of labour</td><td>Mine closures; manufacturing's share of GDP falls</td><td>Retraining, relocation help, regional policy</td></tr>
    <tr><td><b>Cyclical</b> (demand-deficient)</td><td>Fall in AD during a recession</td><td>Job losses after a financial crisis</td><td>Expansionary fiscal or monetary policy</td></tr>
    <tr><td><b>Seasonal</b></td><td>Demand varies with the time of year</td><td>Agriculture, tourism, ski resorts</td><td>Diversify local economy, off-season jobs</td></tr>
    <tr><td><b>Technological</b></td><td>Machines or automation replace workers</td><td>Robots in car factories</td><td>Retraining, investment in new industries</td></tr>
  </table></div>
  <ul>
    <li><b>Cyclical</b> unemployment is linked to the <b>business cycle</b> and falls when AD recovers. <b>Structural and technological</b> unemployment can persist for years and may be long term.</li>
    <li><b>Other contributing factors:</b> inflexible wages or minimum wages above equilibrium, generous benefits (voluntary unemployment), geographical and occupational immobility.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not mix up <b>types</b> with <b>methods of measurement</b>. For types, give the <b>cause</b> and an example for each. For measurement, give <b>two methods</b> and a <b>difficulty</b> of each.</div>
'''

watch = '''
  <h2>1 · From population to the unemployment rate</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stU"></div>
  <h2>2 · Cyclical unemployment in a recession</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Work out the unemployment rate</h2>
  <p>Change the number employed, unemployed and discouraged (millions) and see how each affects the rate.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Labour force</small><strong id="r1"></strong></div><div><small>Unemployment rate</small><strong id="r2"></strong></div><div><small>If discouraged were counted</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of employed, unemployed and discouraged workers"></svg></div></div></div>

  <h2>Lab 2 · What type of unemployment is it?</h2>
  <p>Choose a situation to see the type, the cause and a suitable policy.</p>
  <div class="card"><div class="grid2"><div><div id="sB" class="btnrow"></div>
    <div class="readout"><div><small>Type</small><strong id="t1"></strong></div><div><small>Likely duration</small><strong id="t2"></strong></div><div><small>Suitable policy</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="A label showing the type of unemployment"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which type of unemployment?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put structural unemployment in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A factory closes", "A car plant shuts and 3,000 workers lose their jobs. Local firms do not need their specialised skills, and few other employers are nearby. This is structural unemployment, which can last a long time unless workers retrain or move.", "structural unemployment.") +
rw("A recession", "Spending falls across the economy, so firms cut output and staff in many industries at once. This is cyclical unemployment, and it tends to fall as demand recovers.", "cyclical (demand-deficient) unemployment.") +
rw("Harvest and holiday jobs", "Fruit pickers are needed in autumn but not in winter, and hotels in a ski resort hire in the season. When the season ends many lose work: seasonal unemployment.", "seasonal unemployment.") +
rw("Discouraged workers", "After months of searching, a worker stops looking. They are not counted as unemployed in the labour force survey, so the published rate understates the true level of joblessness.", "difficulties in measuring unemployment.")
)

mc_exam = [
  mcq("m24_12", 18, "To calculate the unemployment rate, the number unemployed is related to which of the following?", ["the total adult population aged 18–65", "the number of unemployed who are seeking work", "the total number in full-time employment", "the total population in the labour force"], 3, "The rate is the number unemployed as a percentage of the labour force."),
  mcq("s24_11", 17, "Asha is currently unemployed. She has been offered a job but has decided to decline the offer and search for a better paid job. Which type of unemployment is this?", ["cyclical", "frictional", "seasonal", "structural"], 1, "Time spent searching between jobs is frictional unemployment."),
  mcq("s25_11", 18, "An economy's manufacturing share of real GDP fell from 30% in 1990 to 12% in 2023. Which type of unemployment would have resulted from this?", ["cyclical", "frictional", "structural", "voluntary"], 2, "The decline of a whole industry creates structural unemployment."),
  mcq("s23_12", 22, "The table shows the types of unemployment and their possible solutions: technological (introduce minimum wage legislation), cyclical (raise government spending), frictional (increase advertising of job vacancies), structural (retrain workers). Which combination is not correct?", ["technological: introduce minimum wage legislation", "cyclical: raise government spending", "frictional: increase advertising of job vacancies", "structural: retrain workers"], 0, "A minimum wage does not solve technological unemployment. Retraining and new investment do."),
  mcq("s24_11", 22, "What is most likely to decrease if a government uses expansionary fiscal policy?", ["a balance of payments deficit", "cyclical unemployment", "the level of wages", "the rate of inflation"], 1, "Higher AD creates jobs, reducing cyclical unemployment. It may worsen the balance of payments and raise inflation."),
  mcq("s24_13", 18, "What is a cost of negative economic growth?", ["deteriorating balance of payments", "higher inflation", "higher unemployment", "increased pollution"], 2, "A falling real GDP means falling output and rising unemployment.")
]

exam = exam_page("unemployment: measurement and causes",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Unemployment is an 8 mark Paper 2 part in most years, usually on the causes or the measurement, and appears in short data-response parts and in Paper 1. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "3", "Oct/Nov 2024 (22) Q4(a); May/June 2024 (21) Q5(a); Oct/Nov 2023 (23) Q4(a)"), ("Data response, 2 to 4 marks", "3", "May/June 2023 (21) Q1(b) and (c); Oct/Nov 2023 (22) Q1(d)"), ("Multiple choice (Paper 1)", "6 shown below", "2020 to 2025")],
  [
  eq(P("w24_22", "4(a)"), "8 marks", "Explain two methods of measuring unemployment and consider the extent of the possible difficulties in obtaining an accurate measurement of unemployment.",
     ["Knowledge (up to 3): identification of two methods of measuring unemployment (1), plus a brief explanation of each (1 each). The two most used are the claimant count, based on those claiming benefits, and the labour force survey, based on a survey of people actively seeking a job. Answers on types of unemployment rather than methods are not rewarded.",
      "Analysis (up to 3): the difficulties in obtaining an accurate measurement with both methods, for example the claimant count may omit people who are not eligible for or do not claim benefits, and the survey depends on sample size and honest answers; discouraged workers and the informal economy.",
      "Evaluation (up to 2): a judgement on the extent of the difficulties and which method is more accurate, with a conclusion."],
     "Two methods: claimant count, labour force survey. Difficulties of each: omissions, discouraged workers, informal work. Judge how serious.",
     [[("k", "The claimant count measures unemployment by counting people who claim unemployment benefit. The labour force survey asks a sample of households whether people are without a job, looking for work and available to start, and then scales up the results.")], [("n", "The claimant count can understate unemployment because some people are not eligible for benefits or do not claim, while it can overstate it if people claim without looking for work. The survey relies on the sample being representative and on honest replies, and neither method counts discouraged workers who have given up looking, or people in the informal economy.")], [("e", "Both methods give a rough guide rather than an exact figure, and the survey is probably more accurate because it follows an international definition and does not depend on benefit rules. The problem of hidden unemployment means that any measure understates the true level of jobless people.")]]),
  eq(P("s24_21", "5(a)"), "8 marks", "Explain three causes of unemployment and consider which cause is likely to be most damaging to a high-income economy.",
     ["Knowledge (up to 3): a clear and accurate explanation of three causes from frictional, structural, cyclical (demand deficient), seasonal or technological (1 each).",
      "Analysis (up to 3): each cause is analysed and judgements are made about how damaging it might be to a high-income economy: frictional depends on information provision; structural may be permanent and hard to solve; cyclical depends on the economic cycle; seasonal depends on alternative sources of employment; technological depends on occupational or geographical immobility.",
      "Evaluation (up to 2): an assessment of how damaging each cause is in comparison with the others (1), leading to a justified conclusion as to which is most damaging (1)."],
     "Three causes explained. How damaging for a high-income economy? Judge: structural is likely to be most damaging because it can be long term.",
     [[("k", "Frictional unemployment arises when workers are between jobs and searching, perhaps because they lack information about vacancies. Structural unemployment arises when industries decline and workers' skills no longer match available jobs. Cyclical unemployment arises when AD falls in a recession and firms cut output and jobs.")], [("n", "In a high-income economy frictional unemployment is short and mostly harmless, and cyclical unemployment falls when the economy recovers. Structural unemployment, such as the closure of heavy industry, can be long term because workers may need retraining or to move.")], [("e", "Structural unemployment is probably the most damaging, since it can persist for years, wastes skills and concentrates in particular regions, while the others are more temporary. A deep recession could still cause very high cyclical unemployment.")]]),
  eq(P("w23_23", "4(a)"), "8 marks", "With reference to a country that is known to you, explain the main causes of unemployment and consider which of these causes is most significant.",
     ["Knowledge (up to 3): a definition of unemployment (1) and an understanding of at least two types of unemployment (1 each).",
      "Analysis (up to 3): an analysis of the causes of those two types of unemployment and their significance, applied to a named country. If only one type is analysed, a maximum of 2; if no country is named, a maximum of 1.",
      "Evaluation (up to 2): an evaluation of which cause is most significant in the named country, leading to a justified conclusion (1)."],
     "Define unemployment. Two types and their causes, applied to a named country. Judge which is most significant there.",
     [[("k", "Unemployment means people who are willing and able to work and are looking for work but cannot find a job. Two types are structural unemployment, caused by changes in the pattern of industry, and cyclical unemployment, caused by a fall in aggregate demand.")], [("n", "In the UK the decline of coal mining and heavy manufacturing in the north left workers with skills that were no longer needed, which created structural unemployment. In the financial crisis of 2008 a fall in AD led firms across the economy to cut jobs, creating cyclical unemployment.")], [("e", "In the UK, structural unemployment has probably been the most significant cause of long-term unemployment in particular regions, while cyclical unemployment rises and falls with the economy. Which is most significant depends on the period examined.")]]),
  eq(P("s23_21", "1(c)"), "4 marks", "Consider the extent to which difficulties may arise in the measurement of unemployment in a developing country with a large rural and informal sector.",
     ["Up to 2 marks for each valid difficulty explained, such as inactive workers who might look for work if their situation changed, discouraged workers who have had no success, disguised unemployment, unreported employment in the informal economy, the efficiency of record collection, the scale of the survey and the difficulty of measurement in rural areas.",
      "Up to 3 marks overall for difficulties, with 1 mark for a valid judgement on the extent."],
     "Two difficulties explained (discouraged workers, informal work, rural areas). Then judge how far they distort the figure.",
     [[("n", "Many unemployed people may have stopped looking, so they are not counted as unemployed, and others work in the informal economy and may be recorded as unemployed or missed entirely. Rural areas are hard to survey, so figures may be unreliable."), ("e", "These difficulties are likely to make the measured rate inaccurate, so figures should be treated as a rough guide, although trends over time may still be useful if the method stays the same.")]])
  ],
  )

tips = tips_html(
  [("Unemployment rate = unemployed ÷ labour force.", "Not ÷ population."),
   ("Two methods: survey and claimant count.", "Explain each, then a difficulty."),
   ("Do not confuse methods with types.", "Types are frictional, structural, cyclical, seasonal, technological."),
   ("Give a cause and an example for each type.", "Mine closures: structural. Recession: cyclical."),
   ("Mention hidden unemployment.", "Discouraged workers, underemployment, informal work."),
   ("Match the remedy to the type.", "Retraining for structural; demand for cyclical."),
   ("Judge which is most damaging.", "Structural can last years.")],
  [("Unemployment", "Unemployment is being available and looking for work without a job."),
   ("Labour force", "The labour force is the employed plus the unemployed."),
   ("Claimant count", "The claimant count measures people claiming unemployment benefit."),
   ("Structural", "Structural unemployment arises when skills do not match the jobs available."),
   ("Cyclical", "Cyclical unemployment is caused by a lack of aggregate demand.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- labour force bars ---------- */
function lfDraw(s) {
  const Y = (v) => 250 - v * 3; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Millions", "sm");
  const bar = (x, v, c, l, k) => k > 0 ? SV.rect(x, Y(v), 90, 250 - Y(v), c, op(0.65 * k)) + SV.text(x + 45, 270, l, "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 45, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "";
  o += bar(80, 80, "f1", "Population", s.a) + bar(200, 56, "f2", "Working age", s.b) + bar(320, 46, "f2", "Labour force", s.c);
  if (s.d > 0) o += SV.rect(440, Y(42), 90, 250 - Y(42), "f1", op(0.65 * s.d)) + SV.rect(440, Y(46), 90, Y(42) - Y(46), "f3", op(0.75 * s.d)) + SV.text(485, 270, "Employed 42 + unemployed 4", "sm", { "text-anchor": "middle", ...op(s.d) });
  if (s.e > 0) o += tag(380, 66, "Unemployment rate = 4 ÷ 46 × 100 = 8.7%", "c3", s.e, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Population, working age, labour force and the split between employed and unemployed">${lfDraw({ a: 1, b: 1, c: 1, d: 1, e: 1 })}</svg>`;
Lib.stepper($("#stU"), { w: 760, h: 290, label: "From population to the unemployment rate", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: lfDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Population</b> of 80 million.", s: { a: 1 } },
  { cap: "<b>Working age</b> population: 56 million. Children and the very old are excluded.", s: { a: 1, b: 1 } },
  { cap: "<b>The labour force</b> is those in work or actively seeking it: 46 million. Students, carers and those who have given up looking are outside it.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Employed</b> 42 million and <b>unemployed</b> 4 million make up the labour force.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The unemployment rate</b> is the unemployed as a percentage of the labour force: 4 ÷ 46 × 100 = 8.7%.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

function cuDraw(s) { return adasPlot({ a: s.a, s: 0, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in AD reduces real output below potential, creating cyclical unemployment">${cuDraw({ a: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A fall in AD creates cyclical unemployment", base: { a: 0, n: 0 }, draw: cuDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Real output is 50, with potential output at 75 (LRAS). Some spare capacity exists.", s: { a: 0, n: 0 } },
  { cap: "<b>A recession.</b> Consumers and firms cut spending, so AD shifts left. Real output falls (to about 40) and firms need fewer workers: <b>cyclical unemployment</b>.", s: { a: -20, n: 1 } },
  { cap: "<b>Recovery.</b> When AD recovers, output rises and cyclical unemployment falls. This is the key difference from structural unemployment, which stays even when demand recovers.", s: { a: 10, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labU() {
  if (!["em", "un", "dc"].every((i) => $("#" + i))) return;
  const e = +$("#em").value, u = +$("#un").value, d = +$("#dc").value, lf = e + u, r = u / lf * 100, r2 = (u + d) / (lf + d) * 100;
  $("#r1").textContent = lf + "m"; $("#r2").textContent = Lib.fmtN(r, 1) + "%"; $("#r3").textContent = Lib.fmtN(r2, 1) + "%";
  $("#rv").textContent = `Labour force = ${e} + ${u} = ${lf} million. Unemployment rate = ${u} ÷ ${lf} × 100 = ${Lib.fmtN(r, 1)}%. The ${d} million discouraged workers who have given up looking are not in the labour force; counting them as unemployed would raise the rate to ${Lib.fmtN(r2, 1)}%, so the official rate understates joblessness.`;
  const Y = (v) => 250 - v * 4; let o = SV.line(40, 250, 400, 250) + SV.line(40, 250, 40, 30);
  [["Employed", e, "f2"], ["Unemployed", u, "f3"], ["Discouraged", d, "f1"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(110 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "em", label: "Employed, millions ", min: 20, max: 60, step: 1, value: 42, fmt: (v) => v, onInput: labU });
Lib.slider($("#g2"), { id: "un", label: "Unemployed (seeking work), millions ", min: 0, max: 15, step: 1, value: 4, fmt: (v) => v, onInput: labU });
Lib.slider($("#g3"), { id: "dc", label: "Discouraged workers (stopped looking), millions ", min: 0, max: 10, step: 1, value: 2, fmt: (v) => v, onInput: labU });
labU();

/* ---------- Lab 2 ---------- */
const SIT = [["A graduate searching for a first job", "Frictional", "Short", "Better job information and matching", "Time is needed to search and match; the problem is information and search costs."], ["A coal mine closes in a town with few other employers", "Structural", "Long", "Retraining and help to relocate", "Skills no longer match the jobs available, and workers are occupationally and geographically immobile."], ["Spending falls in a recession and firms cut staff", "Cyclical", "While demand is weak", "Expansionary fiscal or monetary policy", "Demand-deficient: AD has fallen, so output and jobs fall across industries."], ["Fruit pickers lose work after harvest", "Seasonal", "Recurs each year", "Diversify local work, off-season jobs", "Demand for labour depends on the time of year."], ["Robots replace assembly-line workers", "Technological", "Long", "Retraining and investment in new industries", "New technology replaces labour, a form of structural change."], ["A worker rejects an offer to look for better pay", "Frictional", "Short", "Reduce search costs", "Voluntary search between jobs."]];
function showS(i) {
  const [n, t, d, p, why] = SIT[i]; $$("#sB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = t; $("#t2").textContent = d; $("#t3").textContent = p; $("#tv").textContent = `${n}: this is ${t.toLowerCase()} unemployment. ${why}`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, t + " unemployment", "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(210, 170, "Duration: " + d, "sm", { "text-anchor": "middle" });
}
$("#sB").innerHTML = SIT.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
$$("#sB button").forEach((b) => (b.onclick = () => showS(+b.dataset.i)));
showS(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What type of unemployment is it?", ["Frictional", "Structural", "Cyclical", "Seasonal"],
  [("A graduate searching for the right first job", 0), ("A steelworks closes and its skills are no longer needed", 1), ("Jobs are lost across the economy in a recession", 2), ("Hotel staff laid off after the holiday season", 3), ("A worker leaves a job to look for a better one", 0), ("Manufacturing declines as services grow", 1), ("A fall in AD causes firms to cut output", 2), ("Fruit pickers out of work in winter", 3)],
  "Frictional: searching. Structural: mismatch after industries decline. Cyclical: lack of demand. Seasonal: time of year.") + MATCH([
  ["Unemployment rate", "Unemployed as a percentage of the labour force"],
  ["Labour force", "Employed plus unemployed"],
  ["Claimant count", "People claiming unemployment benefit"],
  ["Labour force survey", "A sample survey of who is looking for work"],
  ["Discouraged worker", "Someone who has stopped looking for a job"],
  ["Technological unemployment", "Machines replace workers"]]) + ORDER(
  "Put the causes of structural unemployment in order.",
  ["An industry declines or closes", "Workers lose their jobs", "Their skills do not match the jobs available", "They are unable or unwilling to move or retrain quickly", "Unemployment persists for a long period"],
  "Decline plus mismatch plus immobility means long-term unemployment.") + CALC([
  {"q": "Employed 38 million, unemployed 2 million. What is the unemployment rate (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "2 ÷ 40.", "sol": "<b>5%</b>."},
  {"q": "The same economy has a working-age population of 52 million. What share of the working-age population is in the labour force (%)?", "a": 76.9, "unit": "%", "tol": 0.2, "hint": "40 ÷ 52.", "sol": "<b>76.9%</b>."},
  {"q": "A further 2 million discouraged workers are counted as unemployed (and as part of the labour force). What is the new rate (%)?", "a": 9.5, "unit": "%", "tol": 0.2, "hint": "4 ÷ 42.", "sol": "<b>9.5%</b>."},
  {"q": "Unemployment falls from 8% to 6% of a labour force of 50 million. How many fewer people are unemployed (millions)?", "a": 1, "unit": "million", "tol": 0.05, "hint": "2% of 50.", "sol": "<b>1 million</b>."}]) + MCQ([
  ("The unemployment rate is the unemployed as a percentage of:", ["The labour force", "The population", "The employed", "The working-age population"], 0, "The labour force."),
  ("Cyclical unemployment is caused by:", ["A lack of aggregate demand", "Skill mismatch", "The time of year", "Job search"], 0, "Demand-deficient."),
  ("Which method of measuring unemployment is based on a survey?", ["The labour force survey", "The claimant count", "The CPI", "GDP"], 0, "Sample of households."),
  ("A discouraged worker is:", ["Not counted as unemployed", "Counted as employed", "Always a claimant", "Part of seasonal unemployment"], 0, "They have stopped looking."),
  ("Which type tends to last longest?", ["Structural", "Frictional", "Seasonal", "Short-term cyclical"], 0, "Skills mismatch and immobility.")
], "qz1") + CARDS([
  ("Unemployment rate", "Unemployed ÷ labour force."),
  ("Labour force", "Employed + unemployed."),
  ("Survey", "Labour force survey."),
  ("Claimant count", "Counts benefit claimants."),
  ("Frictional", "Between jobs."),
  ("Structural", "Mismatch after decline."),
  ("Cyclical", "Lack of demand."),
  ("Seasonal / technological", "Time of year / machines.")]) + MCQ(mc_exam)

build("as48", "as-unemployment-measurement-types", "Unemployment: Measurement, Causes and Types", EY,
  "4.5.1 to 4.5.3: the meaning and measurement of unemployment, difficulties in measuring it, and the causes and types of unemployment. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
