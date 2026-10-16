"""Syllabus 9.3.6 Mobility of labour (chapter 43). Run: python3 tools/artifact-kit/mk_sy936.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.3.6"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Mobility of labour</b> is how easily workers can move between places (<b>geographical</b> mobility) and between jobs or occupations (<b>occupational</b> mobility). Geographical mobility depends mostly on housing, transport, family ties and the cost and risk of moving; occupational mobility depends mostly on skills, education and training, qualifications and information. Low mobility causes <b>structural and regional unemployment</b> alongside <b>labour shortages</b>, keeps <b>wage differentials</b> wide and raises the natural rate. Governments can raise mobility with retraining, housing, transport and information policies.</p></div>

  <h2>1 · Two forms of mobility</h2>
  <div class="grid2">
    <div class="card"><h3>Geographical mobility</h3><p>The ability and willingness of workers to <b>move to a different area or country</b> to take a job.</p><p><b>Example:</b> a worker moving from a high-unemployment region to a city with vacancies.</p></div>
    <div class="card"><h3>Occupational mobility</h3><p>The ability and willingness of workers to <b>change from one type of job or industry to another</b>.</p><p><b>Example:</b> a car-factory worker retraining as an electrician.</p></div>
  </div>
  <div id="pic1" class="card"></div>

  <h2>2 · Factors affecting mobility</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Reduces mobility when…</th><th>Increases mobility when…</th></tr>
    <tr><td colspan="3"><b>Geographical</b></td></tr>
    <tr><td>Housing</td><td>Houses are dear or scarce in areas with jobs, rented housing is short, social housing is tied to location</td><td>Affordable, flexible housing; relocation help</td></tr>
    <tr><td>Transport and infrastructure</td><td>Poor roads and public transport, high commuting costs</td><td>Good transport links, remote working</td></tr>
    <tr><td>Family and social ties</td><td>Family, schools and community keep people in place</td><td>Younger, single workers with fewer ties</td></tr>
    <tr><td>Information and cost</td><td>Little information about jobs elsewhere; moving is costly and risky</td><td>Job-search websites, relocation grants</td></tr>
    <tr><td>Wage and benefit gaps</td><td>Small regional wage gap; benefits that do not depend on moving</td><td>Large gap in pay between regions</td></tr>
    <tr><td>Immigration rules, language and culture</td><td>Visa limits, language barriers, non-recognised qualifications</td><td>Free movement of labour, common language</td></tr>
    <tr><td colspan="3"><b>Occupational</b></td></tr>
    <tr><td>Education and training</td><td>Skills are specific to one job; limited access to retraining</td><td>General education, transferable skills, retraining schemes</td></tr>
    <tr><td>Qualifications and licensing</td><td>Professional licences, union entry rules (closed shops)</td><td>Easier recognition of experience, modular qualifications</td></tr>
    <tr><td>Age</td><td>Older workers close to retirement have less incentive to retrain</td><td>Younger workers with a long working life ahead</td></tr>
    <tr><td>Information</td><td>Workers do not know which sectors are hiring or what skills are needed</td><td>Careers advice, job-centre services</td></tr>
    <tr><td>Discrimination and benefits</td><td>Employers discriminate by age or background; benefits discourage retraining</td><td>Anti-discrimination law, benefits linked to training</td></tr>
  </table></div>

  <h2>3 · Consequences of low mobility</h2>
  <ul>
    <li><b>Structural and regional unemployment</b> alongside <b>vacancies</b>: unemployment and job vacancies can both rise at the same time because the unemployed do not have the skills or location the vacancies need.</li>
    <li><b>Higher natural rate</b> of unemployment and a more rigid labour market.</li>
    <li><b>Wage differentials persist</b> between regions and occupations because workers cannot move to where pay is highest. A less elastic supply of labour to an occupation gives a larger wage response to a rise in demand.</li>
    <li><b>Misallocation of labour:</b> workers stay in declining sectors while growing sectors have shortages, which holds back growth.</li>
    <li><b>Regional inequality:</b> depressed areas lose businesses and tax base.</li>
  </ul>
  <div class="tip"><b class="h">Is more mobility always better?</b>More mobility can lower unemployment and raise output, but geographical mobility can empty rural areas (brain drain, ageing populations) and put pressure on housing and services where people arrive. Greater occupational mobility needs spending on training and may not be enough if demand for labour is weak.</div>

  <h2>4 · Policies to improve mobility</h2>
  <ul>
    <li><b>Retraining and education:</b> training subsidies, apprenticeships and recognised qualifications raise occupational mobility.</li>
    <li><b>Housing:</b> build more affordable housing in high-demand areas, give relocation grants and make renting easier.</li>
    <li><b>Transport and broadband:</b> shorter commutes and remote working widen the area a worker can reach.</li>
    <li><b>Information:</b> job centres, online vacancy platforms and careers guidance.</li>
    <li><b>Remove barriers:</b> easier recognition of qualifications, fewer licensing and union restrictions, immigration rules that match skills.</li>
  </ul>
'''

watch = '''
  <h2>1 · Two regions and the cost of moving</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · Bridging the skills gap</h2>
  <div id="stO"></div>
'''

explore = '''
  <h2>Lab 1 · Should the worker move?</h2>
  <p>A worker is unemployed in region A and is offered a job in region B. Set the pay, the cost of moving and the extra cost of living. See whether the move pays off.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Extra net pay a year</small><strong id="r1"></strong></div><div><small>Years to repay moving cost</small><strong id="r2"></strong></div><div><small>Net gain over the period</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars comparing the benefit of higher pay with the costs of moving and higher housing costs"></svg></div></div></div>

  <h2>Lab 2 · Which barrier and which policy?</h2>
  <p>Pick a barrier to mobility and see which type it affects and what could help.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Geographical or occupational?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of low mobility in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Coal towns and housing", "Miners who lost their jobs often owned cheap homes in towns with few other jobs. Selling up and moving to a city meant giving up a house that was worth little and renting somewhere far dearer. Many stayed unemployed.", "geographical immobility caused by housing and family ties. Link to structural unemployment and regional policy.") +
rw("Retraining in the energy transition", "Programmes in Germany and the US have retrained oil, gas and coal workers as installers of solar panels and wind turbines. Welders, electricians and engineers often have skills that transfer.", "occupational mobility through retraining. Evaluate on cost, time, the quality of new jobs and whether pay matches the old jobs.") +
rw("Free movement of labour in the EU", "After EU enlargement in 2004, large numbers of workers from Poland and other eastern states moved to the UK, Ireland and Germany where wages were higher. Home countries lost workers; receiving countries filled vacancies.", "geographical mobility across borders with benefits (higher output and tax receipts) and costs (brain drain, pressure on services). A common theme in Paper 4 data questions.") +
rw("Remote working", "After 2020 many firms allowed staff to work from home. Workers could take jobs in distant cities without moving, which raised effective geographical mobility for some roles.", "technology that cuts mobility barriers. Limit: it helps only some occupations, and may reduce demand for city-centre services.")
)

mc_exam = [
  ("What is likely to improve the occupational mobility of labour? (Feb/March 2025 · 32 · Q18, reworded)", ["A cut in income tax that raises aggregate demand", "A cut in unemployment benefit", "An increase in retraining schemes for the unemployed", "More advertising of vacancies across the economy"], 2, "Retraining gives workers the skills to move between occupations. Advertising helps information more than skills."),
  ("What is a factor affecting the occupational mobility of labour? (May/June 2025 · 31 · Q18, reworded)", ["Education and training", "Immigration controls", "The price of housing", "Transport infrastructure"], 0, "Education and training decide which jobs a worker can do. Housing and transport affect geographical mobility."),
  ("Which government policy is most likely to improve occupational mobility? (Oct/Nov 2023 · 32 · Q16, reworded)", ["Lower income tax rates", "More spending on education and training", "More spending on infrastructure", "Subsidies to firms that employ school leavers"], 1, "Education and training build skills that let workers change occupation."),
  ("In country X, unemployment is rising at the same time as the number of job vacancies. What is the most likely reason? (Oct/Nov 2024 · 31 · Q17, reworded)", ["Economic growth is falling", "Economic growth is rising", "Geographical mobility of labour is rising", "Occupational immobility of labour is rising"], 3, "If the unemployed lack the skills for the vacancies, both can rise together: structural unemployment."),
  ("When is the natural rate of unemployment most likely to fall? (Oct/Nov 2024 · 32 · Q17, reworded)", ["When education levels fall", "When income tax rises", "When labour mobility increases", "When unemployment benefits rise"], 2, "More mobile workers fill vacancies faster, which reduces frictional and structural unemployment."),
  ("Which statement about unemployment is correct? (Oct/Nov 2022 · 31 · Q21, reworded)", ["Cyclical unemployment is caused by occupational immobility", "Frictional unemployment is caused by lack of information on jobs", "Structural unemployment is caused by deficient aggregate demand", "Voluntary unemployment is caused by seasonal variation in demand"], 1, "Poor information about vacancies lengthens the search period. Occupational immobility causes structural unemployment, not cyclical."),
  ("Many workers in developed countries work from home after a pandemic, leading to closures of city-centre cafes and retailers. If this continues, what is most likely? (Oct/Nov 2023 · 33 · Q18, reworded)", ["Frictional unemployment will decrease", "Geographical mobility of labour will increase", "Structural unemployment will increase", "Voluntary unemployment will increase"], 2, "Jobs in city-centre services disappear and the former workers need new skills or locations: structural unemployment."),
  ("A firm faces a shortage of labour and starts its own training scheme for school leavers. What is the most likely effect on the firm? (Oct/Nov 2023 · 31 · Q13, reworded)", ["A fall in the number of workers employed", "A fall in the productivity of the workforce", "A rise in the geographical mobility of its labour", "A shift of the supply curve of labour to the firm to the right"], 3, "Training creates more workers with the right skills, shifting the supply of labour to the firm to the right.")
]

exam = exam_page("labour mobility, migration and the labour market",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Mobility is not usually tested as a stand-alone essay. It appears in data-response parts on migration and structural change, and in multiple choice. Reworded questions are below, with a practice question on barriers to mobility and eight Paper 3 multiple choice questions.",
  [("Data response parts, 4 to 8 marks", "4", "Oct/Nov 2021 (43) 1(b), (d); May/June 2024 (42) 1(c); Oct/Nov 2024 (42) 1(b), (d)"), ("Practice question", "1", "Barriers to mobility"), ("Multiple choice (Paper 3)", "8 shown below", "2023 to 2025")],
  [
  eq("Based on May/June 2024 · 9708/42 · Q1(c)", "6 marks", "Electric vehicles replace petrol cars and many skilled mechanical engineers who work on petrol engines live in one region of a country. With the help of a diagram, analyse the likely effect on the labour market for these workers in that region.",
     ["Identify the unemployment as structural, linked to occupational immobility (1).",
      "Demand for these workers falls: on a labour market diagram demand shifts left from D to D1, so the wage falls from W to W1 and employment falls from L to L1 (diagram marks: shift, fall in wage and employment, labelled axes).",
      "Credit the need for retraining and the point that the concentration of the workers in one region makes geographical mobility and local job creation important."],
     "Name the type of unemployment. Diagram of D shifting left. Wage and employment fall. One line on retraining."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q1(b)", "4 marks", "Large numbers of workers from poorer eastern countries move to other countries in the same trading bloc. What does this suggest about the state of their own economies compared with the countries they move to?",
     ["Wages and living standards at home are lower (1 to 2).",
      "Unemployment, underemployment or weaker job prospects in their home economies (1 to 2).",
      "The receiving country has higher wages, vacancies and growth, so it pulls workers in.",
      "Credit mention of push and pull factors and that migration is geographical mobility across borders."],
     "Push factors at home. Pull factors abroad. One sentence on what this says about the two economies."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q1(d)", "8 marks", "Using the information in an article about labour migration, assess whether increasing numbers of migrant workers are an advantage or a disadvantage to the receiving country.",
     ["Advantages: fills vacancies and skill shortages, raises potential output (LRAS shifts right), migrants spend and pay taxes (higher AD and revenue), supports public finances, often younger workers, new businesses.",
      "Disadvantages: possible downward pressure on wages in low-skill jobs if migrants are substitutes for existing workers, pressure on housing, schools and healthcare, remittances sent abroad, possible fall in unemployment benefits spending in the home country but not the receiving one.",
      "A reasoned conclusion that depends on the skills of migrants and the state of the economy."],
     "Two advantages. Two disadvantages. Judge using labour market conditions."),
  eq("Based on Oct/Nov 2024 · 9708/42 · Q1(d)", "8 marks", "Migration into a high-income economy was restricted for several years and then returns to its earlier level. Evaluate the likely effect on the economy's macroeconomic performance.",
     ["More labour raises aggregate supply, which may keep prices stable, and migrants spend their income, raising AD with a strong multiplier because they often have a high MPC.",
      "New businesses and jobs may be created. GDP rises, so growth is likely to improve.",
      "Against: remittances sent abroad lower net exports and the current account, there may be pressure on wages for competing workers (the crowding out argument) and on public services.",
      "Credit a diagram of AD and AS shifting right. Conclude on balance."],
     "AS up, AD up, growth. Then remittances and wage effects. Weigh and conclude."),
  eq("Practice (not a past paper question)", "8 marks", "Explain two barriers to the mobility of labour and how a government could reduce each.",
     ["Two barriers explained with a link to unemployment: for example high housing costs in areas with vacancies (geographical) and lack of transferable skills (occupational).",
      "A policy for each: affordable housing and relocation grants; retraining and recognised qualifications.",
      "Say how each policy raises mobility and lowers structural unemployment.",
      "Evaluation: cost, time lags and whether the new jobs match the training."],
     "Two barriers. A policy for each. One evaluation point.",
     [[("k", "Mobility of labour is the ease with which workers can move between areas or between jobs. One barrier to geographical mobility is the high cost of housing in areas where vacancies exist."), ("n", "A worker who lives in a region with few jobs may be unable to afford to rent or buy a home in a city with vacancies, so they stay unemployed even though firms elsewhere have shortages. This is structural, regional unemployment and it raises the natural rate.")],
      [("a", "A government could build more affordable housing in high-demand areas, give grants to cover relocation costs or support social housing that is not tied to a place, so that more workers can afford to move.")],
      [("n", "A second barrier is a lack of transferable skills, which limits occupational mobility. A coal miner whose mine has closed may not have the qualifications to work in other industries. Subsidised retraining and nationally recognised qualifications would let workers move into growing sectors, which reduces structural unemployment and fills vacancies."), ("e", "However, housing takes years to build and retraining is costly, and the retrained workers still need enough vacancies to be hired, so the effect on unemployment may be slow and depends on demand for labour.")]])
  ],
  )

tips = tips_html(
  [("Name the form of mobility.", "Geographical is moving place. Occupational is changing job or sector. Use the right factors for each."),
   ("Housing and transport for geographical; skills and training for occupational.", "Most mixed-up answers swap these."),
   ("Link immobility to unemployment.", "Immobility causes structural and regional unemployment and keeps vacancies unfilled."),
   ("Use a labour market diagram where you can.", "A fall in demand for a declining industry's workers shifts D left and lowers wage and employment."),
   ("Mention both sides of migration.", "Output, tax revenue and filling vacancies against pressure on wages, services and housing."),
   ("Evaluate policies on time and cost.", "Retraining and housing take years, and training only helps if there are suitable vacancies."),
   ("Use 'could'.", "The effect of migration on wages depends on whether migrants are substitutes or complements for existing workers.")],
  [("Define", "Geographical mobility of labour is the ability and willingness of workers to move to another area to take a job."),
   ("Barrier", "High housing costs in areas with vacancies could prevent unemployed workers from moving."),
   ("Consequence", "Occupational immobility could lead to structural unemployment, because workers lack the skills that vacancies need."),
   ("Policy", "Subsidised retraining could improve occupational mobility, which may shift the labour supply to growing industries."),
   ("Evaluate", "However, retraining takes time, and the unemployed may still not find work if demand for labour is weak.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture: mobility as barriers ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A worker in a region of high unemployment facing barriers of housing, transport and family ties before reaching a region with vacancies, and a skills gap between a declining and a growing occupation">${(() => { let o = SV.rect(40, 70, 190, 110, "f2") + tag(135, 100, "Region A", "t2", 1, "middle") + SV.text(135, 128, "unemployment 12%", "lbl", { "text-anchor": "middle" }) + SV.text(135, 150, "few vacancies", "lbl", { "text-anchor": "middle" }); o += SV.rect(530, 70, 190, 110, "f3") + tag(625, 100, "Region B", "t3", 1, "middle") + SV.text(625, 128, "unemployment 3%", "lbl", { "text-anchor": "middle" }) + SV.text(625, 150, "vacancies unfilled", "lbl", { "text-anchor": "middle" }); o += arrow(235, 125, 525, 125, "r", "c1", 1) + tag(380, 112, "geographical mobility", "t1", 1, "middle"); ["housing", "transport", "family", "moving cost"].forEach((l, i) => { const x = 280 + i * 62; o += SV.rect(x, 140, 4, 40, "f4") + SV.text(x + 2, 198, l, "sm", { "text-anchor": "middle" }); }); o += SV.rect(60, 232, 150, 44, "f2") + SV.text(135, 259, "Declining occupation", "lbl bd", { "text-anchor": "middle" }) + SV.rect(550, 232, 150, 44, "f3") + SV.text(625, 259, "Growing occupation", "lbl bd", { "text-anchor": "middle" }) + arrow(215, 254, 545, 254, "r", "c3", 1) + tag(380, 228, "occupational mobility: skills, training, qualifications", "t3", 1, "middle"); return o; })()}</svg>`;

/* ---------- Watch 1: regions ---------- */
function regDraw(s) {
  const m = s.m, ua = 12 - 5 * m, ub = 3 + 1.5 * m, wa = 80 + 10 * m, wb = 120 - 10 * m;
  let o = tag(70, 28, "Unemployment rate (%)", "t1") + tag(420, 28, "Average wage ($ thousand)", "t1");
  const Y = (v, k) => 280 - v * k;
  [[ua, "Region A", 70], [ub, "Region B", 190]].forEach(([v, l, x]) => { o += SV.rect(x, Y(v, 14), 90, 280 - Y(v, 14), l === "Region A" ? "f2" : "f3") + tag(x + 45, Y(v, 14) - 8, Lib.fmtN(v, 1) + "%", l === "Region A" ? "t2" : "t3", 1, "middle") + SV.text(x + 45, 300, l, "sm bd", { "text-anchor": "middle" }); });
  [[wa, "Region A", 420], [wb, "Region B", 540]].forEach(([v, l, x]) => { o += SV.rect(x, Y(v, 2), 90, 280 - Y(v, 2), l === "Region A" ? "f2" : "f3") + tag(x + 45, Y(v, 2) - 8, "$" + Lib.fmtN(v, 0) + "k", l === "Region A" ? "t2" : "t3", 1, "middle") + SV.text(x + 45, 300, l, "sm bd", { "text-anchor": "middle" }); });
  o += SV.line(60, 280, 330, 280) + SV.line(410, 280, 680, 280);
  if (s.b > 0) o += tag(380, 70, "barriers: housing, transport, family ties", "t4", s.b, "middle");
  if (s.a > 0) o += arrow(300, 140, 360, 140, "r", "c1", s.a) + tag(330, 132, "workers move", "t1", s.a, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 330, label: "Unemployment and wages in two regions as labour mobility increases", base: { m: 0, b: 0, a: 0 }, draw: regDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Immobile labour.</b> Region A has unemployment of 12% and wages of $80k. Region B has 3% unemployment, vacancies and wages of $120k. If workers could move freely, labour would flow from A to B.", s: { m: 0 } },
  { cap: "<b>Barriers.</b> Housing in B is dear, public transport is poor, families and schools tie workers to A, and moving is costly. Few people move, so the gaps stay open: <b>regional structural unemployment</b>.", s: { m: 0, b: 1 } },
  { cap: "<b>Policy to raise mobility.</b> Affordable housing, relocation grants, better transport and job information reduce the barriers. Some workers move from A to B.", s: { m: 0.5, b: 0.5, a: 1 } },
  { cap: "<b>Greater mobility.</b> Unemployment in A falls, wages in A rise a little, and B fills its vacancies, though B's wages fall slightly as labour supply grows. The gaps narrow and the economy produces more.", s: { m: 1, b: 0, a: 1 } },
] });

/* ---------- Watch 2: skills gap ---------- */
function skDraw(s) {
  let o = SV.rect(60, 100, 200, 120, "f2") + tag(160, 130, "Declining job", "t2", 1, "middle") + SV.text(160, 160, "e.g. coal mining", "lbl", { "text-anchor": "middle" }) + SV.text(160, 182, "skills: heavy machinery,", "sm", { "text-anchor": "middle" }) + SV.text(160, 198, "safety, teamwork", "sm", { "text-anchor": "middle" });
  o += SV.rect(500, 100, 200, 120, "f3") + tag(600, 130, "Growing job", "t3", 1, "middle") + SV.text(600, 160, "e.g. solar installer", "lbl", { "text-anchor": "middle" }) + SV.text(600, 182, "needs: electrical skills,", "sm", { "text-anchor": "middle" }) + SV.text(600, 198, "certification, roof safety", "sm", { "text-anchor": "middle" });
  const gx = 270 + (1 - s.g) * 0, w = 220 * s.g; o += SV.rect(270, 150, 220, 22, "f4", op(0.35)) + SV.rect(270, 150, 220 - w, 22, "f4", op(0.9)) + SV.rect(270 + 220 - w, 150, w, 22, "f3", op(0.9)) + tag(380, 140, s.g < 0.99 ? "skills gap" : "gap closed", s.g < 0.99 ? "t4" : "t3", 1, "middle");
  if (s.t > 0) o += tag(380, 200, s.l, "t1", s.t, "middle");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 300, label: "Skills gap between a declining occupation and a growing occupation closing with training", base: { g: 0, t: 0, l: "" }, draw: skDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>A mismatch.</b> A mine closes while installers of solar panels are in short supply. The miners are unemployed and the installers' jobs are vacant, because the skills do not match: <b>occupational immobility</b>.", s: { g: 0 } },
  { cap: "<b>Transferable skills.</b> Some skills carry over (working with machinery, safety, teamwork), which narrows the gap a little. Workers with transferable skills move more easily.", s: { g: 0.3, t: 1, l: "transferable skills" } },
  { cap: "<b>Retraining.</b> Subsidised courses in electrical skills and certification close most of the gap. This costs money and takes months.", s: { g: 0.8, t: 1, l: "retraining and certification" } },
  { cap: "<b>The move.</b> Workers are hired as installers. Structural unemployment falls and vacancies are filled, but it only works if enough vacancies exist and the pay is attractive.", s: { g: 1, t: 1, l: "workers hired" } },
] });

/* ---------- Lab 1: move or stay ---------- */
function labMove() {
  if (!$("#mw") || !$("#mc") || !$("#mh") || !$("#my")) return;
  const w = +$("#mw").value, c = +$("#mc").value, h = +$("#mh").value, y = +$("#my").value, net = w - h, pay = c > 0 && net > 0 ? c / net : Infinity, total = net * y - c;
  $("#r1").textContent = "$" + Lib.fmtN(net, 0); $("#r2").textContent = isFinite(pay) ? Lib.fmtN(pay, 1) + " years" : "Never"; $("#r3").textContent = (total >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(total), 0);
  $("#rv").textContent = net <= 0 ? "Higher housing and living costs wipe out the pay rise, so a rational worker would not move. This is geographical immobility caused by costs." : total > 0 ? `The extra net pay of $${net} a year repays the $${c} cost of moving in ${Lib.fmtN(pay, 1)} years and leaves a net gain of $${Lib.fmtN(total, 0)} over ${y} years: the worker is likely to move.` : `It would take ${Lib.fmtN(pay, 1)} years to repay the cost of moving, longer than the ${y} years the worker expects to stay, so the move does not pay.`;
  const mx = Math.max(net * y, c, 1) * 1.1, Y = (v) => 250 - v / mx * 200;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, Y(Math.max(net, 0) * y), 90, 250 - Y(Math.max(net, 0) * y), "f3") + SV.rect(240, Y(c), 90, 250 - Y(c), "f2") + tag(135, Y(Math.max(net, 0) * y) - 6, "$" + Lib.fmtN(Math.max(net, 0) * y, 0), "t3", 1, "middle") + tag(285, Y(c) - 6, "$" + c, "t2", 1, "middle") + SV.text(135, 270, "Extra net pay over " + y + " yrs", "sm bd", { "text-anchor": "middle" }) + SV.text(285, 270, "Cost of moving", "sm bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mw", label: "Extra annual pay in region B ($) ", min: 0, max: 12000, step: 500, value: 6000, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g2"), { id: "mh", label: "Extra housing and living costs a year ($) ", min: 0, max: 12000, step: 500, value: 3000, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g3"), { id: "mc", label: "One-off cost of moving ($) ", min: 0, max: 15000, step: 500, value: 4500, fmt: (v) => v, onInput: labMove });
Lib.slider($("#g4"), { id: "my", label: "Years the worker expects to stay ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labMove });
labMove();
btnTable("lbBtns", "lbOut", [
  ["High house prices where the jobs are", "Geographical", "Workers cannot afford to move to jobs", "Affordable housing, relocation grants, rent support"],
  ["Poor public transport", "Geographical", "Commuting to vacancies is slow or costly", "Transport investment, remote working, commuter subsidies"],
  ["Family and school ties", "Geographical", "Workers unwilling to leave the area", "Remote work, support for relocating families"],
  ["Skills specific to one industry", "Occupational", "Workers cannot do the vacant jobs", "Retraining, apprenticeships, general education"],
  ["Professional licences and union entry rules", "Occupational", "Hard to enter new occupations", "Recognise experience and foreign qualifications"],
  ["Lack of information about vacancies", "Both", "Workers do not know where jobs are", "Job centres, online vacancy platforms, careers advice"],
  ["Older age and short working life left", "Occupational", "Little incentive to retrain", "Training subsidies for older workers, anti-age-discrimination laws"]
], ["Barrier", "Type affected", "Effect", "Possible policy"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the factor mainly affect geographical or occupational mobility?", ["Geographical mobility", "Occupational mobility"],
  [("High rents in the city with the vacancies", 0), ("A skills certificate for a growing industry", 1), ("Poor rail links between regions", 0), ("Professional licensing rules", 1), ("Family and school ties", 0), ("Transferable skills from general education", 1), ("Visa and immigration rules", 0), ("A government retraining subsidy", 1)],
  "Geographical is where you work; occupational is what you do.") + MATCH([
  ["Geographical mobility", "Ability to move area or country for work"],
  ["Occupational mobility", "Ability to change job or industry"],
  ["Structural unemployment", "Mismatch of skills or location with vacancies"],
  ["Transferable skills", "Skills useful in many jobs"],
  ["Remittances", "Money sent home by migrant workers"],
  ["Brain drain", "Emigration of skilled workers from a country"]]) + ORDER(
  "Put the effects of low mobility in order.",
  ["An industry declines and jobs are lost in one region", "Workers cannot move or retrain because of high housing costs and specific skills", "Unemployment stays high in that region while vacancies exist elsewhere", "The natural rate of unemployment is higher", "Output is lower than it could be"],
  "Low mobility turns a local shock into lasting structural unemployment.") + CALC([
  {"q": "A worker would earn $6,000 a year more in another city but pay $3,000 more in housing costs. Calculate the extra net income a year ($).", "a": 3000, "unit": "$", "tol": 0.5, "hint": "Subtract the extra cost.", "sol": "6,000 − 3,000 = <b>$3,000</b>."},
  {"q": "Moving costs the worker $4,500 once. Using the extra net income above, calculate how many years it takes to repay the cost.", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "Cost ÷ extra net income.", "sol": "4,500 ÷ 3,000 = <b>1.5 years</b>."},
  {"q": "Region A has 80,000 unemployed and 5,000 vacancies. Calculate the number of unemployed people per vacancy.", "a": 16, "tol": 0.05, "hint": "Unemployed ÷ vacancies.", "sol": "80,000 ÷ 5,000 = <b>16</b>."},
  {"q": "A retraining programme costs $8,000 per worker and 400 workers take part. Calculate the total cost ($ million).", "a": 3.2, "unit": "$m", "tol": 0.05, "hint": "8,000 × 400 = 3,200,000.", "sol": "8,000 × 400 = $3.2 million."}]) + MCQ([
  ("Which is a barrier to geographical mobility?", ["Retraining schemes", "High house prices in areas with vacancies", "General education", "Online job boards"], 1, "If housing is unaffordable where the jobs are, workers cannot move."),
  ("Which is a barrier to occupational mobility?", ["Skills specific to one industry", "Cheap public transport", "Low rents", "Relocation grants"], 0, "Specific skills prevent a move to a different type of job."),
  ("Unemployment and vacancies both rise in a country. What is the most likely explanation?", ["Demand-deficient unemployment", "A mismatch of skills or location", "A rise in the minimum wage only", "A fall in the labour force"], 1, "The unemployed lack the skills or location the vacancies need: structural unemployment."),
  ("A government subsidises retraining. Which effect on the labour market is most likely?", ["Occupational mobility rises", "Geographical mobility must fall", "The natural rate rises", "Demand for labour falls"], 0, "Retraining gives workers the skills to move into other occupations."),
  ("Which is a possible cost of large-scale emigration for the home country?", ["A brain drain", "Lower remittances", "A fall in wages abroad", "A larger labour force"], 0, "Skilled workers who leave reduce the home country's productive capacity.")
], "qz1") + CARDS([
  ("Geographical mobility", "Ease of moving area or country for work."),
  ("Occupational mobility", "Ease of changing job or industry."),
  ("Structural unemployment", "Mismatch of skills or location with the jobs available."),
  ("Transferable skills", "Skills that can be used in many jobs."),
  ("Brain drain", "Skilled workers emigrating."),
  ("Remittances", "Money migrants send home."),
  ("Relocation grant", "Payment to help a worker move for a job."),
  ("Job centre", "Service that matches unemployed workers with vacancies.")]) + MCQ(mc_exam)

build("sy936", "mobility-of-labour", "Mobility of Labour", EY,
  "9.3.6: geographical and occupational mobility, the factors that affect them, the consequences of low mobility and policies to improve it. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
