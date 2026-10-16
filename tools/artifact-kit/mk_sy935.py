"""Syllabus 9.3.5 Patterns and trends in employment and unemployment (chapter 43). Run: python3 tools/artifact-kit/mk_sy935.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.3.5"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Employment and unemployment data show <b>patterns</b> across groups (age, gender, region, education) and <b>trends</b> over time, such as rising unemployment in recessions and the long-run shift from agriculture and manufacturing to services. Unemployment usually moves <b>against output</b> but <b>lags behind it</b>. National figures hide big differences between groups and regions, and different measures (<b>survey-based</b> or <b>claimant count</b>) can give different answers. Reading the data well means knowing <b>who is counted</b>, using rates and numbers correctly and not mistaking correlation for cause.</p></div>

  <h2>1 · The main measures</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>What it shows</th><th>Limitation</th></tr>
    <tr><td><b>Unemployment rate</b> (labour force survey, ILO)</td><td>Unemployed ÷ labour force, where unemployed = without work, available to start and actively seeking work</td><td>Excludes discouraged workers and underemployment</td></tr>
    <tr><td><b>Claimant count</b></td><td>Number claiming unemployment benefits</td><td>Depends on benefit rules; leaves out those not eligible</td></tr>
    <tr><td><b>Employment rate</b></td><td>Employed ÷ working-age population</td><td>Does not show quality of jobs or hours worked</td></tr>
    <tr><td><b>Participation (activity) rate</b></td><td>Labour force ÷ working-age population</td><td>A fall may reflect study, retirement or discouragement</td></tr>
    <tr><td><b>Long-term unemployment</b></td><td>Share unemployed for 12 months or more</td><td>Signals hysteresis risk</td></tr>
    <tr><td><b>Underemployment</b></td><td>Part-time workers who want more hours, or workers in jobs below their skill</td><td>Hard to measure</td></tr>
  </table></div>
  <div class="tip"><b class="h">Hidden unemployment</b>Official rates can understate the true level. <b>Discouraged workers</b> have stopped looking, <b>underemployed</b> workers have too few hours or jobs below their skills, and <b>informal sector</b> workers in developing countries appear as employed even when earnings are very low. If unemployed people give up searching, the unemployment rate falls but nobody has found a job: check the employment rate and participation rate too.</div>

  <h2>2 · Patterns</h2>
  <ul>
    <li><b>By age:</b> youth unemployment is usually 2 to 3 times the average, because of limited experience and fewer contacts. Older workers have lower rates but longer spells.</li>
    <li><b>By gender:</b> participation rates differ, and in many countries women are more often in part-time or informal jobs.</li>
    <li><b>By region:</b> areas that depended on declining industries have higher rates; capital cities usually lower.</li>
    <li><b>By education:</b> workers with fewer qualifications face higher unemployment and lower pay.</li>
    <li><b>By country:</b> differences in labour markets, benefits and wage-setting give very different rates, for example persistently lower rates in Germany than in Spain in the 2010s.</li>
    <li><b>Developed and developing countries:</b> developing countries often show low measured unemployment but high underemployment and informal work.</li>
  </ul>
  <div id="pic1" class="card"></div>

  <h2>3 · Trends</h2>
  <ul>
    <li><b>The cycle:</b> unemployment rises in a recession and falls in a boom. It <b>lags</b> output, because firms keep workers at first and hire late in a recovery.</li>
    <li><b>Okun's law:</b> a rough rule that a fall in output of about 2% below trend goes with about 1 percentage point more unemployment. It varies between countries and periods.</li>
    <li><b>Structural change:</b> employment shifts from the <b>primary</b> sector to <b>manufacturing</b> and then <b>services</b> as economies develop. Automation changes the mix of jobs.</li>
    <li><b>Flexible work:</b> more part-time, temporary, self-employed and gig work, which blurs the line between employed and unemployed.</li>
    <li><b>Demographics:</b> ageing populations shrink the labour force and may lower unemployment.</li>
    <li><b>Long-term unemployment</b> tends to rise after deep recessions (hysteresis).</li>
  </ul>

  <h2>4 · Reading data in the exam</h2>
  <ul>
    <li><b>Percentage points or percent?</b> A rise from 4% to 6% is a 2 percentage point rise and a 50% rise.</li>
    <li><b>Rate or number?</b> A rate can fall while the number of unemployed rises if the labour force grows.</li>
    <li><b>Quote figures with units and dates</b> and compare like with like.</li>
    <li><b>Trend, then exception, then explanation.</b> Give the overall pattern, one specific figure, then a reason.</li>
    <li><b>Correlation is not causation.</b> Say that the data are consistent with a link, then bring in theory to explain it.</li>
  </ul>
'''

watch = '''
  <h2>1 · Output growth and unemployment over time</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · What the average hides</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Who counts as unemployed?</h2>
  <p>A country has 100 people of working age: 62 employed, 6 unemployed and 32 inactive. Move some of the unemployed out of the labour force (they stop looking) and see how the rates behave.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Unemployment rate</small><strong id="r1"></strong></div><div><small>Employment rate</small><strong id="r2"></strong></div><div><small>Participation rate</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bar showing employed, unemployed and inactive people in the working-age population"></svg></div></div></div>

  <h2>Lab 2 · Data detective</h2>
  <p>Pick a statement from a data release. See what it tells you and what to check before drawing a conclusion.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Counted as unemployed or not?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the recession in the data in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Youth unemployment in southern Europe", "After 2010, unemployment among under-25s in Spain and Greece was often more than double the national rate and reached about half of young people in the labour force at the peak. Many emigrated or stayed in education.", "an example of a pattern by age. Use it with hysteresis and the cost of lost skills, and note that falling youth unemployment can reflect emigration or education, not jobs.") +
rw("Germany's low unemployment", "Germany's measured unemployment fell to historic lows in the 2010s, helped by wage restraint, short-time work schemes, apprenticeships and growth in part-time and low-paid jobs.", "country differences. Evaluate: a low rate can hide underemployment and low pay, and comparisons depend on measurement.") +
rw("Informal work in developing economies", "In many low-income countries most workers are in informal jobs such as street trading or small-scale farming. They count as employed but may work few hours for low pay.", "why measured unemployment is a poor guide in developing economies. Mention underemployment.") +
rw("The pandemic and the participation rate", "In 2020 many economies lost millions of jobs, but unemployment rates rose less than expected in some countries because many people left the labour force and some were supported by furlough schemes.", "a reminder to check the employment and participation rates and not only the headline unemployment rate.")
)

mc_exam = [
  ("The table shows labour market data: employed 15m; unemployed 0.5m; not available for work 7m; working-age population 23m. What is the size of the labour force? (Oct/Nov 2021 · 32 · Q21, reworded)", ["15m", "15.5m", "22m", "22.5m"], 1, "Labour force = employed + unemployed = 15m + 0.5m = 15.5m."),
  ("Which groups are part of a country's labour force? (May/June 2023 · 31 · Q28, reworded)", ["Unemployed only", "Unemployed and self-employed, but not the economically inactive", "Unemployed and inactive", "Inactive and self-employed"], 1, "The labour force is those in work (including self-employed) plus those actively seeking work. The inactive are outside it."),
  ("The Netherlands has the highest share of part-time employees and an average working week of 32 hours. Greece has a smaller share of part-time employees and an average of 41 hours. What can be concluded? (Feb/March 2020 · 32 · Q26, reworded)", ["Greece has a higher percentage of its workforce in full-time employment than the Netherlands", "Part-time employees work longer on average in Greece", "Full-time employees work longer weeks in Greece", "There are more part-time employees in the Netherlands than in Greece"], 0, "A smaller part-time share means a larger full-time share. The other statements compare hours or numbers of people that the data do not give."),
  ("A report suggests that automation could threaten a third of existing jobs in the UK, mainly in manufacturing and retail. Which type of unemployment is this? (Feb/March 2020 · 32 · Q27, reworded)", ["Demand-deficient", "Frictional", "Seasonal", "Structural"], 3, "Technology changing the pattern of jobs causes structural unemployment."),
  ("The table shows monthly US inflation (2.2, 1.9, 1.6, 1.7, 1.9, 2.2 per cent) and unemployment (3.9, 3.8, 3.9, 3.9, 3.8, 3.7 per cent). What can be concluded? (May/June 2022 · 31 · Q30, reworded)", ["Falling inflation leads to lower unemployment", "Rising inflation leads to rising unemployment", "Inflation correlates exactly with unemployment", "Inflation has only a marginal effect on unemployment over this period"], 3, "Unemployment barely moved while inflation changed, so the data show only a small effect. They do not show cause."),
  ("Unemployment in a country rose from 3.5% to 4.8% over five years while inflation fell from 4.0% to 2.0%. Which statement about the Phillips curve is best supported? (Oct/Nov 2024 · 32 · Q23, reworded)", ["The data are entirely consistent with the Phillips curve idea", "The data prove the Phillips curve does not work", "No conclusion about the Phillips curve is possible", "The Phillips curve is correct, with time lags"], 0, "Higher unemployment with lower inflation fits the inverse relationship, although five observations cannot prove it."),
  ("Which combination is most likely to increase a country's budget deficit? (Feb/March 2023 · 32 · Q17, reworded)", ["Government spending falls, GDP rises, unemployment falls", "Government spending falls, GDP rises, unemployment unchanged", "Government spending rises, GDP falls, unemployment rises", "Government spending rises, GDP falls, unemployment unchanged"], 2, "A downturn cuts tax revenue and raises benefit spending, and higher spending adds to the deficit."),
  ("Two people lose their jobs. Mariana's factory closes because of cheaper imports. Alfonso, a shop assistant, is laid off because sales fall in a recession. How would an economist classify the two job losses? (Feb/March 2021 · 32 · Q21, reworded)", ["Frictional and seasonal", "Regional and frictional", "Structural and cyclical", "Technological and structural"], 2, "Competition from imports changing the pattern of demand is structural. A recession-led fall in sales is cyclical.")
]

exam = exam_page("patterns and trends in employment and unemployment",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Data-based parts on employment and unemployment appear in Paper 4 Question 1 and in longer questions on the costs of unemployment. Reworded questions are below, with eight Paper 3 multiple choice questions that need data skills.",
  [("Data response parts, 3 to 6 marks", "2", "Oct/Nov 2022 (41) 1(a), (c); Oct/Nov 2023 (43) 1(b)"), ("Essay part, 12 marks", "1", "Oct/Nov 2020 (41) Q7(a)"), ("Essay part, 13 marks", "2", "Oct/Nov 2021 (43) Q6(b); May/June 2021 (42) Q6(b)"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2024")],
  [
  eq("Based on Oct/Nov 2022 · 9708/41 · Q1(a)", "3 marks", "The table shows 2017 data: Country A had growth of 7.0% and unemployment of 5.9%. The EU average was growth of 2.4% and unemployment of 8.6%. Use the information to indicate how Country A's economy performed in 2017 compared with the EU as a whole.",
     ["Growth: Country A grew much faster than the EU average (7.0% against 2.4%), about three times as fast (1 to 2 marks).",
      "Unemployment: Country A's rate was lower (5.9% against 8.6%), a difference of 2.7 percentage points (1 to 2 marks).",
      "Credit a short link: strong growth is consistent with lower unemployment. Quote both figures with units."],
     "Growth sentence with both numbers, unemployment sentence with both numbers, one link."),
  eq("Based on Oct/Nov 2022 · 9708/41 · Q1(c)", "6 marks", "A country's workforce fell after a large number of workers moved abroad: 600,000 left out of a population of 21.2 million, and the population is now 19.4 million. There is now a labour shortage. Describe the changes in the workforce and consider whether they have been a benefit to the country.",
     ["Describe: emigration of 600,000 people (about 2.8% of the population in the year they left), population down by 1.8 million, a shortage of labour despite low unemployment.",
      "Benefits: lower unemployment, less pressure on public services and housing, remittances sent home, higher bargaining power and wages for those who stay.",
      "Costs: labour shortages limit output (lower potential growth), loss of skilled and young workers (a brain drain), smaller tax base, ageing population.",
      "A conclusion that weighs short-run gains against long-run costs."],
     "Describe in two sentences with figures. Two benefits. Two costs. A judgement."),
  eq("Based on Oct/Nov 2020 · 9708/41 · Q7(a)", "12 marks", "Explain the economic costs of unemployment and consider which is the most important.",
     ["Waste of scarce resources: output is below potential, so living standards are lower than they could be.",
      "Loss of tax revenue and higher spending on benefits, which widens the budget deficit.",
      "Costs for individuals and society: lower income, loss of skills (hysteresis), poverty, crime and health costs, inequality.",
      "Level 4 needs about three costs analysed, an assessment of each and a conclusion on which is most important (many answers say waste of resources, because the others follow from it)."],
     "Three costs, each with cause and effect, then rank them and justify."),
  eq("Based on Oct/Nov 2021 · 9708/43 · Q6(b)", "13 marks", "'Economic growth will always reduce unemployment, but this will usually create significant problems for other macroeconomic aims.' How far do you agree?",
     ["Growth raises demand for labour, so unemployment tends to fall. Use Okun's law and the lag between output and jobs. Say 'always' is too strong: jobless growth, productivity growth, automation, structural change and a rise in participation can all keep unemployment high.",
      "Conflicts with other aims: faster growth can raise inflation, cause a current account deficit as imports rise, widen inequality and harm the environment.",
      "Evaluation: the problems are not inevitable if growth comes from supply-side improvements, and the severity depends on spare capacity. Reach a judgement on both halves of the statement."],
     "Growth and jobs, with the word 'always' tested. Then the conflicts. Then spare capacity and a conclusion."),
  eq("Based on May/June 2021 · 9708/42 · Q6(b)", "13 marks", "Discuss whether reducing unemployment should be the main policy objective for the government of a developing country.",
     ["Why it matters: wasted resources, poverty, lost output, social problems, and in developing countries more workers in low-productivity informal work.",
      "Why not the main aim: measured unemployment may be low while underemployment is high; growth, development, inflation, debt and the balance of payments may matter more; policies for jobs may conflict with other aims.",
      "A reasoned conclusion that links the aim to the country's circumstances."],
     "Case for. Case against, including underemployment. Compare with other aims. Judge.")
  ],
  )

tips = tips_html(
  [("Quote figures with units and years.", "Say '5.9% in 2017 against 8.6% for the EU', not 'lower'."),
   ("Distinguish percentage points from percent.", "A rise from 4% to 6% is 2 percentage points, or 50%."),
   ("Check who is counted.", "The unemployment rate falls if people stop searching. Look at the employment rate and participation rate too."),
   ("Mention the lag.", "Unemployment usually rises after output falls and keeps falling after a recovery begins."),
   ("Break the average down.", "Age, region, gender and education can show very different rates from the national figure."),
   ("Do not say 'proves'.", "Data are consistent with a theory. Bring in the economic reason for the pattern."),
   ("For developing countries, talk about underemployment and the informal sector.", "Headline unemployment may be low even if many workers have very little work.")],
  [("Compare", "Unemployment was 5.9% in 2017, which is 2.7 percentage points lower than the EU average of 8.6%."),
   ("Lag", "Unemployment may continue to rise after output starts to recover, because firms are slow to hire."),
   ("Hidden", "The unemployment rate could understate the problem, because discouraged workers have left the labour force."),
   ("Pattern", "Youth unemployment is usually higher than the national average because young workers have less experience."),
   ("Data caution", "The data are consistent with a link between growth and falling unemployment, but they do not prove cause.")],
  [CW["define"], CW["explain"], CW["consider"], CW["discuss"]]) + FC

js = '''
/* ---------- Learn picture: unemployment by age ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Bar chart of unemployment rates by age group: youth 14 percent, prime age 5 percent, older workers 4 percent, with the national average of 6 percent">${(() => { const g = [["15 to 24", 14, "f2", "t2"], ["25 to 49", 5, "f1", "t1"], ["50 to 64", 4, "f3", "t3"]]; let o = SV.line(70, 290, 720, 290) + SV.line(70, 290, 70, 30) + tag(70, 22, "Illustrative unemployment rates by age (%)", "t1"); const Y = (v) => 290 - v * 16; g.forEach(([l, v, c, t], i) => { const x = 130 + i * 170; o += SV.rect(x, Y(v), 100, 290 - Y(v), c) + tag(x + 50, Y(v) - 8, v + "%", t, 1, "middle") + SV.text(x + 50, 312, l, "sm bd", { "text-anchor": "middle" }); }); o += SV.line(70, Y(6), 700, Y(6), "c4 dash") + tag(698, Y(6) - 6, "national average 6%", "t4", 1, "end"); return o; })()}</svg>`;

/* ---------- Watch 1: growth and unemployment ---------- */
const GR = [3, 2.5, -2, -0.5, 2, 3, 3.2, 2.8, 2.5, -5, 3, 3.5], UR = [5, 5, 8, 9, 8.2, 7.1, 6.2, 5.6, 5.3, 8.5, 7.6, 6.4];
const GX = (i) => 100 + i * 52, GYb = (g) => 160 - g * 12, GYu = (u) => 310 - u * 11;
function guDraw(s) {
  let o = SV.line(70, 160, 740, 160) + SV.text(66, 164, "0", "sm", { "text-anchor": "end" }) + tag(70, 28, "GDP growth (%, bars)", "t1") + tag(70, 208, "Unemployment rate (%, line)", "t2") + SV.line(70, 310, 740, 310, "gr");
  const n = Math.round(s.n);
  for (let i = 0; i < n && i < 12; i++) { const g = GR[i], y = g >= 0 ? GYb(g) : 160; o += SV.rect(GX(i) - 14, y, 28, Math.abs(g) * 12, g >= 0 ? "f1" : "f2") + SV.text(GX(i), 330, "Y" + (i + 1), "sm", { "text-anchor": "middle" }); }
  const pts = []; for (let i = 0; i < n && i < 12; i++) pts.push([GX(i), GYu(UR[i])]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2"); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2")));
  if (s.m1 > 0 && n >= 4) o += tag(GX(3) , GYu(9) - 12, "peak after the fall in output", "t2", s.m1, "middle");
  if (s.m2 > 0 && n >= 10) o += tag(GX(9) , GYu(8.5) - 12, "rises again", "t2", s.m2, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 345, label: "Bars for GDP growth and a line for unemployment over twelve years with two recessions", base: { n: 0, m1: 0, m2: 0 }, draw: guDraw, tween: 1200, dwell: 6000, steps: [
  { cap: "<b>A normal expansion.</b> In years 1 and 2 growth is solid at about 3% and unemployment is steady at 5%.", s: { n: 2 } },
  { cap: "<b>Recession.</b> Output falls in years 3 and 4 and unemployment jumps from 5% to 9%. Notice that unemployment keeps rising in year 4 even though the economy is shrinking by less: the <b>lag</b>.", s: { n: 4, m1: 1 } },
  { cap: "<b>Recovery.</b> Growth returns and unemployment falls, but slowly, over about four years. Firms hire late and some of the long-term unemployed have lost skills.", s: { n: 8, m1: 1 } },
  { cap: "<b>A second shock.</b> A deep one-year fall in output (year 10) raises unemployment sharply again, though the recovery that follows is quicker because many jobs were kept.", s: { n: 12, m1: 1, m2: 1 } },
] });

/* ---------- Watch 2: what the average hides ---------- */
const BX = (i) => 110 + i * 70;
function avgDraw(s) {
  const grp = [["All", 6, "f4"], ["15-24", 14, "f2"], ["25-49", 5, "f1"], ["50-64", 4, "f3"], ["City", 4, "f1"], ["Old industry", 11, "f2"]];
  let o = SV.line(70, 280, 740, 280) + SV.line(70, 280, 70, 30), Y = (v) => 280 - v * 14;
  grp.forEach(([l, v, c], i) => { const on = i === 0 || (i <= 3 && s.a > 0) || (i >= 4 && s.b > 0), op_ = i === 0 ? 1 : i <= 3 ? s.a : s.b; if (!on) return; o += SV.rect(BX(i) - 25, Y(v), 50, 280 - Y(v), c, op(op_)) + tag(BX(i), Y(v) - 8, v + "%", i === 0 ? "t4" : "t1", op_, "middle") + SV.text(BX(i), 300, l, "sm bd", { "text-anchor": "middle", ...op(op_) }); });
  o += SV.line(70, Y(6), 740, Y(6), "c4 dash") + tag(738, Y(6) - 6, "average 6%", "t4", 1, "end");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 330, label: "National unemployment rate of 6 percent broken down by age and region", base: { a: 0, b: 0 }, draw: avgDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The headline.</b> The national unemployment rate is <b>6%</b>. It sounds moderate, and it is a useful single number.", s: {} },
  { cap: "<b>By age.</b> Young workers face <b>14%</b>, prime-age workers 5% and older workers 4%. Youth have less experience and fewer contacts, and are the first to be let go.", s: { a: 1 } },
  { cap: "<b>By region.</b> A prosperous city is at 4% while a region that depended on a declining industry is at 11%. The average hides large differences, so policy must be targeted.", s: { a: 1, b: 1 } },
] });

/* ---------- Lab 1: who counts ---------- */
function labCount() {
  if (!$("#gu") || !$("#uh")) return;
  const g = +$("#gu").value, f = Math.min(+$("#uh").value, 6 - g);
  const emp = 62 + f, unemployed = 6 - g - f, inactive = 32 + g, labour = emp + unemployed;
  $("#r1").textContent = Lib.fmtN(unemployed / labour * 100, 1) + "%"; $("#r2").textContent = Lib.fmtN(emp, 0) + "%"; $("#r3").textContent = Lib.fmtN(labour, 0) + "%";
  $("#rv").textContent = g === 0 && f === 0 ? "Baseline: 62 employed, 6 unemployed and 32 inactive out of 100. Unemployment rate = 6 ÷ 68 = 8.8%." : g > 0 && f === 0 ? `${g} unemployed people stopped looking for work. The unemployment rate falls to ${Lib.fmtN(unemployed / labour * 100, 1)}% but employment is still 62 out of 100 and the participation rate has fallen to ${labour}%. No jobs were created, so the headline rate understates the problem.` : `${f} unemployed people found jobs, so employment rises to ${emp}% and the unemployment rate falls to ${Lib.fmtN(unemployed / labour * 100, 1)}%` + (g > 0 ? `, and ${g} others stopped looking, so the participation rate is ${labour}%.` : ".");
  let x = 50, o = SV.line(40, 250, 400, 250);
  [[emp, "f1", "Employed"], [unemployed, "f2", "Unemployed"], [inactive, "f3", "Inactive"]].forEach(([v, c, l]) => { const w = v * 3.2; o += SV.rect(x, 120, w, 70, c) + SV.text(x + w / 2, 160, v, "lbl bd", { "text-anchor": "middle" }); if (v > 4) o += SV.text(x + w / 2, 212, l, "sm bd", { "text-anchor": "middle" }); x += w; });
  o += tag(50, 100, "100 people of working age", "t1") + SV.line(50, 232, 50 + labour * 3.2, 232, "c4", { "stroke-width": 3 }) + tag(50, 250, "labour force: " + labour, "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gu", label: "Unemployed who stop looking ", min: 0, max: 6, step: 1, value: 0, fmt: (v) => v, onInput: labCount });
Lib.slider($("#g2"), { id: "uh", label: "Unemployed who find jobs ", min: 0, max: 6, step: 1, value: 0, fmt: (v) => v, onInput: labCount });
labCount();
btnTable("lbBtns", "lbOut", [
  ["The unemployment rate fell from 8% to 6%.", "Fewer unemployed as a share of the labour force.", "Check whether employment rose or people left the labour force (participation rate)."],
  ["Unemployment is 5% nationally but 12% for under-25s.", "A pattern by age: youth are hit harder.", "Ask why (experience, last in first out) and whether students are included."],
  ["Employment rose by 300,000 while unemployment rose too.", "The labour force grew (more people entered).", "Rates and numbers can move differently. Look at participation and population."],
  ["Unemployment has risen for three years while GDP is growing again.", "Unemployment lags behind output.", "Consider hysteresis, productivity growth and skills mismatch."],
  ["Measured unemployment is 4% but half the workforce is in informal work.", "Measured unemployment may understate under-use of labour.", "Look for underemployment and low pay, especially in developing countries."],
  ["The claimant count fell by 10% but survey unemployment fell by 3%.", "The two measures use different definitions.", "Benefit rules and eligibility can change the claimant count without changing real unemployment."]
], ["Statement", "What it tells you", "What to check"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is the person counted as unemployed in the survey measure?", ["Counted as unemployed", "Not counted as unemployed"],
  [("Without a job, available and applying for jobs", 0), ("A full-time student who is not looking for work", 1), ("A worker who gave up looking after a year", 1), ("A part-time worker who wants full-time hours", 1), ("A person who lost their job last week and is searching", 0), ("A retired person", 1), ("A graduate waiting to start a job next week, who has been searching for three months", 0), ("A parent caring for children who is not looking for work", 1)],
  "Unemployed means without work, available to start and actively seeking work.") + MATCH([
  ["Participation rate", "Labour force as a share of the working-age population"],
  ["Claimant count", "Number of people claiming unemployment benefits"],
  ["Underemployment", "Workers with too few hours or in jobs below their skills"],
  ["Okun's law", "A fall in output below trend is linked to more unemployment"],
  ["Long-term unemployment", "Out of work for 12 months or more"],
  ["Discouraged worker", "Someone who has stopped looking for work because they expect no success"]]) + ORDER(
  "Put the way a recession shows up in the data in order.",
  ["Real GDP falls", "Firms cut hours and freeze hiring", "Unemployment rises, with a lag", "The share of long-term unemployed rises", "After recovery begins unemployment falls slowly"],
  "Unemployment lags behind output at both turning points.") + CALC([
  {"q": "The working-age population is 40m, of whom 26m are employed, 2m are unemployed and the rest are inactive. Calculate the participation rate (%).", "a": 70, "unit": "%", "tol": 0.05, "hint": "Labour force = employed + unemployed = 28m.", "sol": "28 ÷ 40 × 100 = <b>70%</b>."},
  {"q": "Using the same data, calculate the unemployment rate (to one decimal place).", "a": 7.1, "unit": "%", "tol": 0.1, "hint": "Unemployed ÷ labour force.", "sol": "2 ÷ 28 × 100 = <b>7.1%</b>."},
  {"q": "Unemployment rises from 4% to 6%. By how many percentage points has it risen?", "a": 2, "unit": "points", "tol": 0.01, "hint": "Subtract.", "sol": "6 − 4 = <b>2 percentage points</b>. (It is a 50% rise.)"},
  {"q": "Using Okun's law (2% below trend output goes with 1 percentage point more unemployment), by how many percentage points would unemployment rise if output is 5% below trend?", "a": 2.5, "unit": "points", "tol": 0.05, "hint": "5 ÷ 2.", "sol": "5 ÷ 2 = <b>2.5 percentage points</b>."}]) + MCQ([
  ("The unemployment rate falls but the employment rate is unchanged. What is the most likely explanation?", ["More jobs have been created", "Some unemployed people have left the labour force", "The population has fallen", "Output has grown"], 1, "If nobody found a job but some stopped searching, the unemployment rate falls without any rise in employment."),
  ("What is the labour force?", ["Everyone of working age", "Employed plus unemployed", "Employed only", "Unemployed only"], 1, "The labour force is the employed plus those actively seeking work."),
  ("Which statement describes the lag between output and unemployment?", ["Unemployment rises before output falls", "Unemployment usually keeps rising after output starts to recover", "Unemployment and output move together without a delay", "Output always follows unemployment"], 1, "Firms keep workers at first and hire late in a recovery."),
  ("Which group usually has the highest unemployment rate?", ["Prime-age workers", "Older workers", "Young workers", "Highly qualified workers"], 2, "Young workers have less experience and fewer contacts."),
  ("Why might measured unemployment be low in a developing country?", ["Most people have well-paid secure jobs", "Many people work in the informal sector or are underemployed", "There are no benefits", "Growth is always rapid"], 1, "Informal and underemployed workers count as employed even though their work is limited.")
], "qz1") + CARDS([
  ("Unemployment rate", "Unemployed ÷ labour force × 100."),
  ("Employment rate", "Employed ÷ working-age population × 100."),
  ("Participation rate", "Labour force ÷ working-age population."),
  ("Claimant count", "Number claiming unemployment benefits."),
  ("Discouraged worker", "Stopped looking; not counted as unemployed."),
  ("Underemployment", "Too few hours or a job below skill level."),
  ("Okun's law", "About 2% below-trend output goes with 1 point more unemployment."),
  ("Long-term unemployment", "Out of work 12 months or more.")]) + MCQ(mc_exam)

build("sy935", "patterns-trends-unemployment", "Patterns and Trends in Employment and Unemployment", EY,
  "9.3.5: measures of employment and unemployment, patterns by group and region, trends over the cycle and how to read the data. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
