"""Syllabus 9.3.1-9.3.3 Full employment, equilibrium and disequilibrium unemployment, voluntary and involuntary (chapter 43). Run: python3 tools/artifact-kit/mk_sy931.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.3.1 to 9.3.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Full employment</b> means everyone who is willing and able to work at the going wage can find a job; it does <b>not</b> mean zero unemployment, because some frictional and structural unemployment always remains. <b class="kw">Equilibrium unemployment</b> exists even when the labour market is in balance (frictional, structural, seasonal). <b class="kw">Disequilibrium unemployment</b> exists because the labour market is <b>not</b> in balance: wages are above the equilibrium level (<b>real wage</b> or classical unemployment) or demand for goods is too low (<b>demand-deficient</b> or cyclical unemployment). <b class="kw">Hysteresis</b> is when a rise in unemployment feeds on itself and stays high after its cause has gone, because workers lose skills and contacts.</p></div>

  <h2>1 · Measuring employment and unemployment</h2>
  <div class="grid2">
    <div class="card"><h3>Labour force</h3><p>Everyone of working age who is <b>employed or actively seeking work</b>. People who are retired, in full-time education, caring at home or have given up looking are <b>economically inactive</b> and are not in the labour force.</p><div class="formula">labour force = employed + unemployed</div></div>
    <div class="card"><h3>Rates</h3><div class="formula">unemployment rate = unemployed ÷ labour force × 100</div><div class="formula">employment rate = employed ÷ working-age population × 100</div></div>
  </div>

  <h2>2 · Full employment (9.3.1)</h2>
  <ul>
    <li>Everyone willing and able to work at the <b>current wage</b> can find a job; the labour market is in equilibrium (labour demand equals supply).</li>
    <li>There is still <b>frictional</b> unemployment (people between jobs), <b>structural</b> unemployment (skills or location mismatch) and <b>seasonal</b> unemployment. Some economists put full employment at about 3% to 5% unemployment; the figure depends on the country and the period.</li>
    <li>Full employment is closely linked to <b>potential output</b>: when the economy is at full employment, output is at the LRAS.</li>
  </ul>
  <div id="pic1" class="card"></div>

  <h2>3 · Equilibrium and disequilibrium unemployment (9.3.2)</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Equilibrium unemployment</th><th>Disequilibrium unemployment</th></tr>
    <tr><td><b>Labour market</b></td><td>In balance: demand equals supply at the going wage</td><td>Not in balance: more people willing to work than jobs on offer</td></tr>
    <tr><td><b>Types</b></td><td>Frictional, structural, seasonal, voluntary (the natural rate)</td><td>Real wage (classical) and demand-deficient (cyclical, Keynesian)</td></tr>
    <tr><td><b>Cause</b></td><td>Search time, skills mismatch, seasonal patterns, benefits that discourage work</td><td>Wages above equilibrium (minimum wage, union power), or low aggregate demand and sticky wages</td></tr>
    <tr><td><b>Duration</b></td><td>Persists even when the economy is at full capacity</td><td>Falls if wages adjust or demand recovers</td></tr>
  </table></div>
  <div class="grid2">
    <div class="card"><h3>Real wage (classical) unemployment</h3><p>The wage is held <b>above</b> the equilibrium by a minimum wage or union bargaining. Firms demand less labour than workers supply, so there is <b>excess supply of labour</b>. Classical economists say the answer is to let wages fall or remove the floor.</p></div>
    <div class="card"><h3>Demand-deficient (cyclical) unemployment</h3><p>A fall in aggregate demand (recession) reduces demand for goods, so firms cut output and jobs. Keynesians say wages are <b>sticky downwards</b>, so unemployment can persist until demand recovers. The answer is to raise AD.</p></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>Frictional</h3><p>Short-term unemployment while people <b>search</b> for a new job or enter the labour market. Poor information about vacancies lengthens it. It exists even in a healthy economy.</p></div>
    <div class="card"><h3>Structural</h3><p>A long-term <b>mismatch</b> between the skills or location of workers and the jobs available, caused by technology, changes in demand, foreign competition or the decline of an industry. It can be regional or technological.</p></div>
  </div>
  <p><b>Seasonal</b> unemployment follows the time of year (tourism, farming, construction).</p>

  <h2>4 · Voluntary and involuntary unemployment (9.3.3)</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Voluntary</th><th>Involuntary</th></tr>
    <tr><td><b>Meaning</b></td><td>People choose not to take jobs at the going wage: reservation wage too high, benefits too generous, long job search</td><td>People are willing and able to work at the going wage but cannot find a job</td></tr>
    <tr><td><b>On the diagram</b></td><td>People off the supply curve at that wage</td><td>The gap between labour supplied and labour demanded at that wage</td></tr>
    <tr><td><b>Types</b></td><td>Part of frictional unemployment, benefit-related and poverty-trap cases</td><td>Cyclical, real wage and most structural unemployment</td></tr>
    <tr><td><b>Policy</b></td><td>Change incentives (benefits, taxes) and information</td><td>Raise demand, retrain, change wages</td></tr>
  </table></div>

  <h3>Hysteresis</h3>
  <p>After a recession, unemployment may not fall back to its previous level. <b>Hysteresis</b> means the equilibrium rate is <b>raised</b> by the experience of unemployment:</p>
  <ul>
    <li>Long-term unemployed workers lose <b>skills</b> and work habits.</li>
    <li>Employers see long spells as a signal of low quality (<b>stigma</b>).</li>
    <li>Workers become discouraged and stop searching, or become <b>outsiders</b> to the wage bargain (insider-outsider).</li>
    <li>Industries close and capital is scrapped, so jobs do not come back where workers live.</li>
  </ul>
  <div class="tip"><b class="h">Why it matters</b>Hysteresis turns <b>cyclical</b> unemployment into <b>structural</b> unemployment and raises the <b>natural rate</b>. It is why governments try to prevent long recessions and help the long-term unemployed early with training.</div>
'''

watch = '''
  <h2>1 · Labour market: full employment, then two ways to get unemployment</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · Hysteresis: unemployment that does not come back</h2>
  <div id="stH"></div>
'''

explore = '''
  <h2>Lab 1 · The labour market</h2>
  <p>Move the demand for labour and set a wage floor. See employment, how many are unemployed and the unemployment rate. The wage floor is a minimum wage or union wage. When wages are sticky after a fall in demand, set the floor at the old wage.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Wage paid</small><strong id="r1"></strong></div><div><small>Employed</small><strong id="r2"></strong></div><div><small>Unemployment rate</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Labour market diagram with demand, supply and a wage floor showing unemployment"></svg></div></div></div>

  <h2>Lab 2 · What type of unemployment?</h2>
  <p>Pick a person's story to see the type, whether it is equilibrium or disequilibrium, voluntary or involuntary, and the best response.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Which type of unemployment?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the hysteresis chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Coal mining closures", "When mines close because power stations switch to gas and renewables, miners often have skills that no local employer needs and live in towns with few other jobs. Many stay unemployed for years.", "structural unemployment, regional immobility and hysteresis. Link to retraining and regional investment as the policy response.") +
rw("Youth unemployment in southern Europe after 2010", "After the financial crisis and the euro-zone recession, youth unemployment in Spain and Greece reached 50% or more. Many young people spent years without work, losing skills and experience.", "demand-deficient unemployment that risked becoming hysteresis. Use it to say why a long recession costs more than lost output.") +
rw("Summer jobs on the coast", "A seaside town employs many hotel and cafe staff between May and September, and many of them are out of work in winter. Employers hire again every year.", "seasonal unemployment, which is predictable and part of the equilibrium rate. It is hard to cut with demand policy.") +
rw("A graduate searching for the right job", "A new graduate turns down jobs they see as below their skills while waiting for a better offer, supported by savings and family. Some weeks later they take a job in their field.", "frictional and voluntary unemployment. Better job information and shorter search time reduce it.")
)

mc_exam = [
  ("What is a definition of hysteresis unemployment? (May/June 2025 · 31 · Q16, reworded)", ["Workers who are briefly unemployed while moving between jobs", "Workers who lose jobs in a recession but find work when the economy recovers", "Workers who stay unemployed for a long time and lose job skills and work experience", "Workers who lose jobs when firms close and new firms use new technology"], 2, "Hysteresis is long-lasting unemployment caused by loss of skills and work experience, which stops it falling back after a recession."),
  ("A government cuts interest rates to reduce unemployment but finds this has little effect because of hysteresis. What causes the hysteresis? (May/June 2025 · 32 · Q20, reworded)", ["More capital investment", "Fewer people save", "The skills of unemployed workers become outdated", "The money supply rises"], 2, "Out-of-date skills mean the unemployed cannot fill vacancies even when demand recovers."),
  ("Which type of unemployment is associated with a deficiency in aggregate demand? (May/June 2022 · 31 · Q21, reworded)", ["Cyclical", "Frictional", "Structural", "Voluntary"], 0, "Cyclical or demand-deficient unemployment arises when AD is too low."),
  ("Which term describes short-term unemployment when people are changing jobs? (Feb/March 2022 · 32 · Q22, reworded)", ["Cyclical", "Frictional", "Seasonal", "Voluntary"], 1, "Frictional unemployment is the time spent searching between jobs."),
  ("Which statement about unemployment is correct? (Oct/Nov 2022 · 31 · Q21, reworded)", ["Cyclical unemployment is caused by occupational immobility", "Frictional unemployment is caused by a lack of information on jobs", "Structural unemployment is caused by a deficiency in aggregate demand", "Voluntary unemployment is caused by seasonal variations in demand"], 1, "Poor information about vacancies lengthens the search period. The other statements swap the causes."),
  ("'If you pay people not to work, and tax them when they do, don't be surprised if you get unemployment.' What type is this? (May/June 2022 · 32 · Q22, reworded)", ["Cyclical", "Frictional", "Structural", "Voluntary"], 3, "Benefit and tax incentives make people choose not to take work: voluntary unemployment."),
  ("Which citizen is not structurally unemployed? (May/June 2023 · 31 · Q19, reworded)", ["A coal miner whose power stations are closing and is unwilling to retrain", "A cafe worker who lost the job when town-centre trade fell after a pandemic", "A worker who cannot move with a firm that relocated", "A skilled person who is taking time to choose among job offers"], 3, "Choosing between offers is frictional search. The others involve a lasting mismatch of skills, location or demand."),
  ("The table shows a country's population data: total population 2,000,000; labour force 1,200,000; employed 900,000; unemployed 300,000. What is the unemployment rate? (Oct/Nov 2024 · 31 · Q20, reworded)", ["25%", "33%", "60%", "75%"], 0, "Unemployment rate = unemployed ÷ labour force = 300,000 ÷ 1,200,000 = 25%.")
]

exam = exam_page("employment, full employment and types of unemployment",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The types and causes of unemployment appear regularly in Paper 4 as 12 mark questions, usually followed by a 13 mark question on policy (see the 9.3.7 page). Reworded questions are below, with a practice question on hysteresis and eight Paper 3 multiple choice questions.",
  [("Essay part, 12 marks", "4", "Oct/Nov 2020 (42, 43); May/June 2021 (42); Oct/Nov 2021 (42)"), ("Data response parts, 3 to 6 marks", "2", "May/June 2025 (41, 43) 1(a); Oct/Nov 2022 (42) 1(b)"), ("Practice question", "1", "Hysteresis"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2025 · 9708/41 and 43 · Q1(a)", "3 marks", "Explain what is meant by structural unemployment and whether it is the same as the natural rate of unemployment.",
     ["Structural unemployment: a mismatch between the skills or location of the unemployed and the jobs on offer, so people looking for work cannot find a suitable job (2 marks).",
      "It is not the same as the natural rate. The natural rate includes structural <b>and</b> frictional (and seasonal) unemployment, so structural is only part of it (1 mark)."],
     "Define in two sentences with a cause, then one sentence on the difference."),
  eq("Based on Oct/Nov 2021 · 9708/42 · Q6(a)", "12 marks", "Explain the difference between frictional unemployment and real wage (classical) unemployment.",
     ["Frictional: temporary, while workers leave or lose a job and search for another; the labour market is in equilibrium. Explain the role of poor information and search time.",
      "Real wage: caused by a wage held above the equilibrium by union power or a minimum wage; firms demand less labour than workers supply. Show on a labour market diagram: wage floor, quantity demanded below quantity supplied.",
      "Level 4 (9 to 12) needs both explained and the difference made clear: equilibrium versus disequilibrium, short-term versus persistent, and the policy implication for each."],
     "Define each. Diagram for real wage. Then a direct comparison on cause, duration and cure."),
  eq("Based on Oct/Nov 2020 · 9708/43 · Q6(a)", "12 marks", "Explain the causes of demand-deficient (cyclical) unemployment and consider which cause is the most important.",
     ["Define demand-deficient unemployment: output and jobs fall because aggregate demand is too low, shown on AD and AS or a Keynesian cross.",
      "Causes: fall in consumer confidence and spending, fall in investment, fall in exports (a global slowdown or a stronger currency), tighter fiscal or monetary policy, a credit crunch.",
      "For Level 4 explain at least two causes and discuss their relative importance with a conclusion, for example that a fall in exports also affects the exchange rate and other aims."],
     "Define and draw a fall in AD. Two causes with chains of reasoning. Rank them and conclude."),
  eq("Based on Oct/Nov 2022 · 9708/42 · Q1(b)", "2 + 4 marks", "A country's sugar plantations close because foreign producers can sell sugar more cheaply. (i) Identify the type of unemployment this causes. (ii) Explain how this type of unemployment could be reduced.",
     ["<b>(i)</b> Structural unemployment (1), because the industry cannot compete with foreign producers, which changes the pattern of demand for labour (1).",
      "<b>(ii)</b> Supply-side policies (1), for example retraining and education for the workers (1), with up to two more marks for developing the example. Credit subsidies or incentives for new industries in the region."],
     "Name the type and give the reason. Policy: one supply-side measure, developed."),
  eq("Based on Oct/Nov 2020 · 9708/42 · Q5(a)", "12 marks", "Analyse the causes of unemployment and explain which cause could be most significant in your country.",
     ["Explain causes with some precision: frictional, structural, seasonal, cyclical (demand-deficient) and real wage unemployment, ideally with a diagram for at least one.",
      "Choose one as the most significant for your own country and justify it with evidence about the economy: the main industries, growth, the minimum wage, skills and migration.",
      "Level 4 needs analysis and a reasoned choice, not a list."],
     "Four causes in a short paragraph each. Then pick one with country-specific evidence and a reason for ranking it first."),
  eq("Practice (not a past paper question)", "8 marks", "Explain what is meant by hysteresis and why it might raise the natural rate of unemployment.",
     ["Definition: unemployment that stays high after the cause (such as a recession) has gone, because unemployment itself changes the labour market.",
      "At least two mechanisms: skills decay, stigma in hiring, discouragement and withdrawal from the labour force, loss of contacts, firms closing.",
      "Link to the natural rate: cyclical becomes structural, so the equilibrium rate rises and the same demand policy produces more inflation and less fall in unemployment.",
      "Evaluation: early training and temporary job subsidies can prevent it."],
     "Define. Two mechanisms. Link to the natural rate. One policy.",
     [[("k", "Hysteresis means that a rise in unemployment, for example in a recession, does not fully reverse when the cause disappears, because the experience of unemployment itself reduces the chances of re-employment."), ("n", "Workers who are out of work for a long time lose skills and work habits, so employers find them less employable. Some employers may treat a long spell of unemployment as a sign of low quality, and some workers become discouraged and stop searching. When demand recovers, vacancies appear but many of the unemployed do not fit them, so cyclical unemployment has become structural.")],
      [("n", "This raises the natural rate of unemployment, because there are more workers in the economy who cannot easily be matched to jobs even when demand is high. A rise in demand may therefore push up wages and prices sooner, rather than reduce unemployment."), ("e", "However, hysteresis can be reduced by early intervention, for example retraining programmes and temporary wage subsidies for the long-term unemployed, so the effect depends on policy and on how long the recession lasts.")]])
  ],
  )

tips = tips_html(
  [("Full employment is not zero unemployment.", "It means everyone willing and able to work at the going wage can find a job. Frictional and structural unemployment remain."),
   ("Use the rate formulas.", "Unemployment rate = unemployed ÷ labour force. Know who is in the labour force and who is inactive."),
   ("Equilibrium versus disequilibrium.", "Say whether the labour market is in balance. Real wage and demand-deficient unemployment are disequilibrium."),
   ("Draw the labour market.", "A wage floor above equilibrium shows real wage unemployment as the gap between supply and demand."),
   ("Match type to cause to cure.", "Frictional: information. Structural: retraining and mobility. Cyclical: raise AD. Real wage: weaken the floor. Seasonal: diversify."),
   ("Explain hysteresis with a mechanism.", "Skills decay, stigma and discouragement are the usual ones."),
   ("Voluntary does not mean 'their own fault'.", "It means they choose not to accept jobs at the going wage, often because of benefits, search time or a high reservation wage.")],
  [("Full employment", "Full employment means everyone who is willing and able to work at the going wage can find a job, although some frictional and structural unemployment remains."),
   ("Real wage", "Real wage unemployment occurs when a minimum wage or union power holds the wage above the equilibrium, so labour supplied exceeds labour demanded."),
   ("Cyclical", "Demand-deficient unemployment arises when a fall in aggregate demand leads firms to cut output and jobs."),
   ("Structural", "Structural unemployment occurs because the skills or location of workers do not match the jobs available."),
   ("Hysteresis", "Hysteresis could raise the natural rate, because long spells of unemployment lead workers to lose skills.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["consider"]]) + FC

js = '''
/* ---------- Labour market diagram ---------- */
const LX = (l) => 70 + l * 6, LY = (w) => 320 - w * 26;
function lmDraw(s) {
  const d = s.d, dem = (l) => (100 + d - l) / 10, sup = (l) => (l + 20) / 10, Ws = (120 + d) / 20;
  let o = axes(70, 320, 700, 30, "Number of workers", "Wage");
  o += SV.line(LX(0), LY(dem(0)), LX(100), LY(dem(100)), "c1") + tag(LX(100) - 4, LY(dem(100)) - 8, "Demand (D)", "t1", 1, "end");
  o += SV.line(LX(0), LY(sup(0)), LX(100), LY(sup(100)), "c2") + tag(LX(60) , LY(sup(60)) - 40, "Supply (S)", "t2", 1, "end");
  const W = Math.max(s.wf, Ws), Ld = 100 + d - 10 * W, Ls = -20 + 10 * W;
  if (s.eq > 0) o += SV.circle(LX(100 + d - 10 * Ws), LY(Ws), 7, "dot4", op(s.eq)) + SV.line(LX(100 + d - 10 * Ws), LY(Ws), LX(100 + d - 10 * Ws), 320, "gr", op(s.eq)) + SV.line(70, LY(Ws), LX(100 + d - 10 * Ws), LY(Ws), "gr", op(s.eq)) + tag(LX(100 + d - 10 * Ws) + 10, LY(Ws) + 22, "equilibrium", "t4", s.eq);
  if (s.wf > 0 && W > Ws + 0.01) o += SV.line(70, LY(W), 640, LY(W), "c4", { "stroke-width": 3, ...op(s.fl) }) + tag(644, LY(W) + 4, "wage W", "t4", s.fl);
  if (s.un > 0 && Ls > Ld + 0.5) o += SV.line(LX(Ld), LY(W), LX(Ls), LY(W), "c2", { "stroke-width": 7, ...op(s.un) }) + SV.circle(LX(Ld), LY(W), 5, "dot1", op(s.un)) + SV.circle(LX(Ls), LY(W), 5, "dot2", op(s.un)) + tag(LX((Ld + Ls) / 2), LY(W) - 12, "involuntary unemployment", "t2", s.un, "middle") + tag(LX(Ld), LY(W) + 20, "employed", "t1", s.un, "middle");
  if (s.vl > 0) o += tag(LX(100 + d - 10 * Ws) + 70, LY(Ws) + 50, "to the right of S: not willing at this wage (voluntary)", "t3", s.vl, "start");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="Labour market equilibrium and the natural rate of unemployment as labour force, employed and frictional and structural unemployment">${(() => { let o = ""; const bars = [["Working-age population", 100, "f1"], ["Labour force", 72, "f3"], ["Employed (full employment)", 68, "f4"]]; bars.forEach(([l, v, c], i) => { const y = 40 + i * 70; o += SV.rect(70, y, v * 6, 42, c) + tag(76, y + 26, l + " (" + v + ")", "t1"); }); o += SV.rect(70 + 68 * 6, 180, 4 * 6, 42, "f2") + tag(70 + 68 * 6 + 12, 242, "frictional, structural and seasonal unemployment remain at full employment (about 4 of 72 = 5.6%)", "t2", 1, "end"); o += tag(70, 300, "Not in the labour force: students, retirees, carers, discouraged workers (28)", "t3"); return o; })()}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 360, label: "Labour market equilibrium with full employment, a wage floor above equilibrium, and a fall in demand with sticky wages", base: { d: 0, wf: 0, eq: 1, fl: 0, un: 0, vl: 0 }, draw: lmDraw, tween: 1000, dwell: 6000, steps: [
  { cap: "<b>Equilibrium.</b> Demand for labour (D) and supply (S) meet at a wage of 6. At that wage everyone willing and able to work has a job: <b>full employment</b>.", s: {} },
  { cap: "<b>Voluntary non-participation.</b> People who would only work at a higher wage are not in the labour force at this wage. They are <b>voluntarily</b> out of work and are not counted among the involuntarily unemployed.", s: { vl: 1 } },
  { cap: "<b>Real wage unemployment.</b> A minimum wage or union agreement raises the wage to 6.5. More people want jobs (Ls) than firms want to hire (Ld). The gap is <b>involuntary unemployment</b>, a disequilibrium.", s: { wf: 6.5, fl: 1, un: 1, eq: 1 } },
  { cap: "<b>Demand-deficient unemployment.</b> Now demand for labour falls (a recession cuts demand for goods). If the wage stays at 6 because wages are sticky downwards, firms employ fewer workers than before and the gap is unemployment.", s: { d: -20, wf: 6, fl: 1, un: 1, eq: 1 } },
  { cap: "<b>The two answers.</b> Classical economists say wages should fall to the new equilibrium. Keynesians say wages do not adjust quickly, so demand has to be raised to move D back to the right.", s: { d: -20, wf: 6, fl: 1, un: 1, eq: 1 } },
] });

/* ---------- Hysteresis path ---------- */
const HP = [[0, 5], [2, 5], [3, 8], [4, 10], [6, 9], [8, 8.1], [10, 7.4], [12, 7], [20, 7]];
const HX = (t) => 70 + t * 33, HY = (u) => 300 - u * 22;
function hyDraw(s) {
  let o = axes(70, 300, 740, 40, "Years", "Unemployment rate (%)");
  [0, 5, 10].forEach((u) => (o += SV.text(64, HY(u) + 4, u, "sm", { "text-anchor": "end" })));
  o += SV.line(70, HY(5), 730, HY(5), "c3 dash") + tag(732, HY(5) - 6, "original natural rate 5%", "t3", 1, "end");
  const pts = []; for (let t = 0; t <= s.p + 1e-9; t += 0.1) { let k = 0; while (k < HP.length - 2 && t > HP[k + 1][0]) k++; const [t0, u0] = HP[k], [t1, u1] = HP[k + 1], u = u0 + (u1 - u0) * (t - t0) / (t1 - t0); pts.push([HX(t), HY(u)]); }
  o += SV.path(Lib.ptsPath(pts), "c2");
  if (s.n > 0) o += SV.line(HX(12), HY(7), 730, HY(7), "c4 dash", op(s.n)) + tag(732, HY(7) - 6, "new natural rate 7%", "t4", s.n, "end");
  if (s.l) o += tag(HX(s.p) + 10, 62, s.l, "t2");
  return o;
}
Lib.stepper($("#stH"), { w: 760, h: 330, label: "Unemployment rises in a recession and does not return to its previous level", base: { p: 0.5, n: 0, l: "" }, draw: hyDraw, tween: 1300, dwell: 5600, steps: [
  { cap: "<b>Before the recession.</b> Unemployment is at the natural rate of 5%.", s: { p: 1.5 } },
  { cap: "<b>The recession.</b> Falling demand pushes <b>cyclical</b> unemployment up to 10%.", s: { p: 4, l: "recession" } },
  { cap: "<b>Recovery begins.</b> Demand returns and unemployment falls, but slowly. Many of the long-term unemployed have lost skills and cannot take the new vacancies.", s: { p: 8, l: "recovery" } },
  { cap: "<b>Hysteresis.</b> Unemployment levels off at <b>7%</b>, not 5%. The experience of unemployment has raised the natural rate: cyclical unemployment has become structural.", s: { p: 14, n: 1, l: "hysteresis" } },
] });

/* ---------- Lab 1: labour market ---------- */
function labLab() {
  if (!$("#dd") || !$("#wf")) return;
  const d = +$("#dd").value, wf = +$("#wf").value / 10, Ws = (120 + d) / 20, W = Math.max(wf, Ws), Ld = 100 + d - 10 * W, Ls = -20 + 10 * W, un = Math.max(0, Ls - Ld), rate = un / Ls * 100;
  $("#r1").textContent = Lib.fmtN(W, 1); $("#r2").textContent = Lib.fmtN(Ld, 0); $("#r3").textContent = Lib.fmtN(rate, 0) + "%";
  $("#rv").textContent = un < 0.5 ? `The wage is at the equilibrium of ${Lib.fmtN(Ws, 1)}: ${Lib.fmtN(Ld, 0)} workers are employed and everyone who wants to work at that wage has a job (full employment).` : `The wage floor of ${Lib.fmtN(W, 1)} is above the equilibrium of ${Lib.fmtN(Ws, 1)}. Firms hire ${Lib.fmtN(Ld, 0)} but ${Lib.fmtN(Ls, 0)} want to work: ${Lib.fmtN(un, 0)} workers (${Lib.fmtN(rate, 0)}% of the labour force) are involuntarily unemployed.`;
  const X = (l) => 40 + l * 3.4, Y = (w) => 270 - w * 21;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 290, "Workers", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Wage", "sm");
  o += SV.line(X(0), Y((100 + d) / 10), X(100), Y(d / 10), "c1") + SV.line(X(0), Y(2), X(100), Y(12), "c2");
  o += SV.line(40, Y(W), 380, Y(W), "c4", op(0.7)) + SV.circle(X(Ld), Y(W), 6, "dot1") + SV.circle(X(Ls), Y(W), 6, "dot2");
  if (un > 0.5) o += SV.line(X(Ld), Y(W), X(Ls), Y(W), "c2", { "stroke-width": 7 }) + tag((X(Ld) + X(Ls)) / 2, Y(W) - 12, "unemployed " + Lib.fmtN(un, 0), "t2", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dd", label: "Change in demand for labour ", min: -30, max: 20, step: 5, value: 0, fmt: (v) => v, onInput: labLab });
Lib.slider($("#g2"), { id: "wf", label: "Wage floor (x10) ", min: 0, max: 90, step: 1, value: 0, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labLab });
labLab();
btnTable("lbBtns", "lbOut", [
  ["Amira is between jobs and searching", "Frictional", "Equilibrium", "Voluntary (search)", "Better job information, shorter search"],
  ["A factory closes as robots replace workers", "Structural (technological)", "Equilibrium (part of natural rate)", "Involuntary", "Retraining, subsidies for new industries"],
  ["Orders collapse in a recession and a shop cuts staff", "Cyclical (demand-deficient)", "Disequilibrium", "Involuntary", "Raise AD: fiscal and monetary stimulus"],
  ["A union wage deal prices some workers out of jobs", "Real wage (classical)", "Disequilibrium", "Involuntary", "Reduce union power or the floor, raise productivity"],
  ["A ski instructor is out of work every summer", "Seasonal", "Equilibrium", "Mostly involuntary but predictable", "Diversify local work, train for off-season jobs"],
  ["A worker refuses jobs because benefits pay almost as much", "Voluntary (benefit-related)", "Equilibrium", "Voluntary", "Reform benefits, lower the tax on low earners"],
  ["After a long recession many workers have outdated skills", "Hysteresis", "Equilibrium (raised natural rate)", "Involuntary", "Early retraining, job subsidies"]
], ["Case", "Type", "Equilibrium or disequilibrium", "Voluntary or involuntary", "Response"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of unemployment is it?", ["Frictional", "Structural", "Cyclical", "Seasonal"],
  [("A graduate searching for a job that fits their skills", 0), ("A textile worker whose factory moved abroad", 1), ("A shop assistant laid off in a recession", 2), ("A fruit picker out of work in winter", 3), ("A bank clerk replaced by online banking software", 1), ("A builder between two projects", 0), ("A hotel worker laid off when exports and tourism fall sharply", 2), ("A beach lifeguard unemployed outside summer", 3)],
  "Think about why the job was lost and how long it will last.") + MATCH([
  ["Full employment", "Everyone willing and able to work at the going wage can find a job"],
  ["Labour force", "People who are employed or actively seeking work"],
  ["Hysteresis", "Unemployment that stays high after its cause has gone"],
  ["Real wage unemployment", "Caused by a wage held above equilibrium"],
  ["Demand-deficient unemployment", "Caused by a fall in aggregate demand"],
  ["Voluntary unemployment", "Choosing not to accept jobs at the going wage"]]) + ORDER(
  "Put the hysteresis chain in order.",
  ["A recession causes mass layoffs", "Many workers stay unemployed for a long time", "Their skills and contacts fade and employers see them as less employable", "Demand recovers but vacancies cannot be filled from the unemployed", "The natural rate of unemployment is higher than before"],
  "Long-term unemployment turns a cyclical problem into a structural one.") + CALC([
  {"q": "A country has 18 million employed, 1.2 million unemployed and 9 million economically inactive. Calculate the unemployment rate (to one decimal place).", "a": 6.3, "unit": "%", "tol": 0.1, "hint": "Labour force = employed + unemployed.", "sol": "Labour force = 19.2m. Rate = 1.2 ÷ 19.2 × 100 = <b>6.3%</b>."},
  {"q": "The working-age population is 30 million; 19 million are employed. Calculate the employment rate (to one decimal place).", "a": 63.3, "unit": "%", "tol": 0.1, "hint": "Employed ÷ working-age population.", "sol": "19 ÷ 30 × 100 = <b>63.3%</b>."},
  {"q": "In a labour market, demand is L = 100 − 10W and supply is L = −20 + 10W. A minimum wage of 7 is set. Calculate the number of unemployed workers.", "a": 20, "tol": 0.01, "hint": "Find labour demanded and supplied at W = 7.", "sol": "Demand = 100 − 70 = 30. Supply = −20 + 70 = 50. Unemployed = <b>20</b>."},
  {"q": "The labour force is 25 million and the unemployment rate is 8%. Next year 500,000 of the unemployed find jobs and the labour force stays the same. Calculate the new unemployment rate (%).", "a": 6, "unit": "%", "tol": 0.05, "hint": "Unemployed now = 2m.", "sol": "Unemployed = 2m − 0.5m = 1.5m. 1.5 ÷ 25 × 100 = <b>6%</b>."}]) + MCQ([
  ("Which is true at full employment?", ["There is no unemployment of any kind", "Everyone willing and able to work at the going wage has a job", "The government budget is balanced", "Inflation is zero"], 1, "Full employment allows for frictional and structural unemployment."),
  ("A minimum wage set above the equilibrium wage is most likely to cause:", ["Demand-deficient unemployment", "Real wage unemployment", "Frictional unemployment", "Seasonal unemployment"], 1, "A wage above equilibrium means labour supplied exceeds labour demanded: real wage unemployment."),
  ("Which is an example of equilibrium unemployment?", ["Unemployment in a deep recession", "Unemployment caused by a wage floor", "Workers between jobs searching for vacancies", "Unemployment from a collapse in exports"], 2, "Frictional unemployment exists even when the labour market clears."),
  ("What is a cause of hysteresis?", ["A rise in aggregate demand", "Loss of skills during long spells of unemployment", "A fall in the minimum wage", "A rise in labour mobility"], 1, "Skills decay, stigma and discouragement make long-term unemployment persistent."),
  ("Who is in the labour force?", ["Full-time students", "Retired people", "People actively seeking work", "People who have given up looking for work"], 2, "The labour force is the employed plus those actively seeking work.")
], "qz1") + CARDS([
  ("Full employment", "Everyone willing and able to work at the going wage can find a job."),
  ("Labour force", "Employed plus unemployed (actively seeking work)."),
  ("Equilibrium unemployment", "Exists even when the labour market is in balance: frictional, structural, seasonal."),
  ("Disequilibrium unemployment", "Labour market out of balance: real wage and demand-deficient."),
  ("Voluntary unemployment", "Not accepting jobs at the going wage."),
  ("Involuntary unemployment", "Willing to work at the going wage but cannot find a job."),
  ("Real wage unemployment", "Wage held above the equilibrium by a minimum wage or union power."),
  ("Hysteresis", "Unemployment stays high after the cause has gone.")]) + MCQ(mc_exam)

build("sy931", "full-employment-types-of-unemployment", "Full Employment and Types of Unemployment", EY,
  "9.3.1 to 9.3.3: full employment, equilibrium and disequilibrium unemployment including hysteresis, and voluntary and involuntary unemployment. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
