"""Syllabus 9.3.4 The natural rate of unemployment (chapter 43). Run: python3 tools/artifact-kit/mk_sy934.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.3.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">natural rate of unemployment</b> is the rate of unemployment when the labour market is in equilibrium: it consists of <b>frictional, structural and seasonal</b> unemployment, and it is also the rate consistent with <b>stable inflation</b> (the NAIRU). It is <b>determined</b> by how well the labour market works: labour mobility, information, skills, benefits, union power, the minimum wage and the pace of structural change. The <b>policy implication</b> for monetarists and new classical economists is that demand-side policy cannot cut unemployment below the natural rate for long without accelerating inflation, so lowering the rate needs <b>supply-side</b> policy. Keynesians reply that the natural rate is not fixed and that hysteresis means demand matters too.</p></div>

  <h2>1 · Definition</h2>
  <ul>
    <li><b>Natural rate of unemployment (NRU):</b> the rate of unemployment that exists when the labour market is in equilibrium and the economy is at its long-run potential output. It includes frictional, structural and seasonal unemployment and excludes cyclical and real wage (disequilibrium) unemployment.</li>
    <li><b>NAIRU</b> (non-accelerating inflation rate of unemployment): the rate of unemployment at which inflation neither speeds up nor slows down. In practice it is used as another name for the natural rate.</li>
    <li>It is <b>not zero and not fixed</b>: it differs between countries and changes over time.</li>
  </ul>
  <div class="formula">natural rate = frictional + structural + seasonal unemployment (as a % of the labour force)</div>
  <div id="pic1" class="card"></div>

  <h2>2 · Determinants of the natural rate</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Raises the natural rate when…</th><th>Lowers it when…</th></tr>
    <tr><td><b>Unemployment benefits</b></td><td>High, long-lasting, easy to claim (higher replacement ratio): less urgency to take a job</td><td>Lower, time-limited, linked to job search</td></tr>
    <tr><td><b>Trade union power and minimum wage</b></td><td>Wages above equilibrium, insiders protected from outsiders</td><td>Weaker unions, lower wage floors</td></tr>
    <tr><td><b>Labour mobility</b></td><td>Workers cannot or will not move region or occupation</td><td>Easy to move: housing, transport, transferable skills</td></tr>
    <tr><td><b>Information</b></td><td>Poor information about vacancies lengthens the search</td><td>Job centres, online job platforms</td></tr>
    <tr><td><b>Education and training</b></td><td>Skills mismatch after industries decline</td><td>Retraining, apprenticeships, flexible skills</td></tr>
    <tr><td><b>Pace of structural change</b></td><td>Rapid technological change and trade shifts destroy jobs in some sectors</td><td>Stable industrial structure</td></tr>
    <tr><td><b>Hiring and firing costs, regulation</b></td><td>High costs make firms reluctant to hire</td><td>Flexible hiring rules</td></tr>
    <tr><td><b>Taxes on work and the poverty trap</b></td><td>High effective marginal rates on moving into work</td><td>Lower taxes and benefit withdrawal rates</td></tr>
    <tr><td><b>Hysteresis</b></td><td>Long recessions leave the unemployed with outdated skills</td><td>Quick recoveries, early help for the long-term unemployed</td></tr>
  </table></div>

  <h2>3 · Policy implications</h2>
  <div class="grid2">
    <div class="card"><h3>Monetarist and new classical view</h3><ul>
      <li>The natural rate is set by <b>supply-side</b> features of the labour market.</li>
      <li>A demand stimulus that pushes unemployment <b>below</b> the natural rate can only work while people <b>mistake</b> higher prices for higher real wages. Once expectations adjust, unemployment returns and inflation is <b>higher</b> (the long-run Phillips curve is vertical at the natural rate).</li>
      <li>To cut the natural rate, use supply-side policy: better information, retraining, weaker union power, lower benefits, labour market reform. This shifts LRAS right.</li>
    </ul></div>
    <div class="card"><h3>Keynesian view</h3><ul>
      <li>The natural rate is <b>not fixed</b>: it can be raised by long recessions (hysteresis), so demand management matters.</li>
      <li>Cyclical unemployment can be cut by demand policy without inflation when there is spare capacity.</li>
      <li>Supply-side policy takes years, costs money and may be unfair.</li>
    </ul></div>
  </div>
  <div class="tip"><b class="h">Evaluating the monetarist argument</b>It depends on how fast expectations adjust, on whether the economy is really at the natural rate (there may be spare capacity, with a negative output gap), on how accurately the natural rate can be estimated, and on whether supply-side reforms work and are acceptable. Estimates of the NAIRU are uncertain and often revised.</div>
'''

watch = '''
  <h2>1 · Expectations and the long-run Phillips curve</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · Supply-side policy lowers the natural rate</h2>
  <div id="stN"></div>
'''

explore = '''
  <h2>Lab 1 · What sets the natural rate?</h2>
  <p>A stylised model: move the four factors and see how the natural rate changes. The numbers are illustrative, not estimates.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Frictional</small><strong id="r1"></strong></div><div><small>Structural</small><strong id="r2"></strong></div><div><small>Natural rate</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bar of frictional, seasonal and structural unemployment forming the natural rate"></svg></div></div></div>

  <h2>Lab 2 · What if a government targets unemployment below the natural rate?</h2>
  <p>The natural rate is 5% and inflation starts at 2%. Choose a target for unemployment and see what happens to inflation if expectations adjust each year.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div>
    <div class="readout"><div><small>Target</small><strong id="t1"></strong></div><div><small>Inflation in year 6</small><strong id="t2"></strong></div><div><small>Unemployment kept low?</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Line chart of inflation rising each year when unemployment is held below the natural rate"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Does it raise or lower the natural rate?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the monetarist argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The 1970s stagflation", "Governments in several countries used demand policy to push unemployment down, but high inflation followed. By the end of the decade both inflation and unemployment were high, which led many economists to accept that the natural rate sets a limit on what demand policy can achieve.", "the main evidence behind the natural rate idea. Say that supply shocks (oil prices) also contributed, which weakens a simple monetarist reading.") +
rw("European labour market reforms", "Germany's reforms in the early 2000s cut the length of unemployment benefits, reorganised job centres and made part-time work easier. Unemployment fell from about 11% to under 5% over the next decade.", "supply-side policy that may have lowered the natural rate. Evaluate: other factors such as wage restraint and global demand also mattered, and low-paid jobs grew.") +
rw("The US after 2009 and hysteresis", "Unemployment peaked at 10% in 2009. For years many economists argued that a lot of it was becoming structural, but a long recovery brought unemployment below 4% by 2019 without a surge in inflation.", "an example showing the natural rate is not fixed and is hard to estimate. Use it to challenge a confident claim about where the NAIRU is.") +
rw("Job platforms and information", "Online job boards and matching services cut the time it takes to find a vacancy. Faster matching reduces the average length of a frictional spell.", "improving information as a way to cut the natural rate. Say it works on frictional unemployment, not on a skills mismatch.")
)

mc_exam = [
  ("The natural rate of unemployment is 5%. What will happen if the government keeps trying to hold unemployment at 3% using expansionary monetary policy? (Feb/March 2021 · 32 · Q29, reworded)", ["An accelerating rate of inflation", "A falling rate of inflation", "A high but constant rate of inflation", "A negative rate of inflation"], 0, "Below the natural rate, expectations adjust and inflation keeps accelerating."),
  ("An economy is at its natural rate of unemployment. When would extra government spending aimed at cutting unemployment most conflict with low inflation? (May/June 2025 · 31 · Q23, reworded)", ["If inflationary expectations are unchanged", "If inflationary expectations fall", "If labour productivity rises", "If labour supply rises"], 0, "At the natural rate, extra demand mainly raises prices, and it is worst when expectations do not adjust."),
  ("Why might country X have a higher natural rate of unemployment than country Y? (Feb/March 2024 · 32 · Q18, reworded)", ["A higher level of trade unionisation in X", "More training and education in X", "Greater incentives to find work in X", "More job vacancy information in X"], 0, "Strong unions push wages above equilibrium and protect insiders, raising the natural rate."),
  ("What is least likely to increase the natural rate of unemployment? (May/June 2025 · 34 · Q17, reworded)", ["Less information about vacancies", "Weaker trade union power", "Higher unemployment benefits", "Higher immigration"], 1, "Weaker unions reduce wage pressure. The other options all lengthen search or raise the supply of job seekers relative to vacancies."),
  ("Which increase is most likely to reduce the natural rate of unemployment? (Oct/Nov 2024 · 31 · Q18, reworded)", ["The level of unemployment benefit", "The militancy of trade unions", "The national minimum wage", "Participation on training courses"], 3, "Training reduces skills mismatch and so structural unemployment."),
  ("When is the natural rate of unemployment most likely to fall? (Oct/Nov 2024 · 32 · Q17, reworded)", ["When education levels decline", "When income tax rates rise", "When labour mobility increases", "When state unemployment benefits rise"], 2, "Greater mobility matches workers to vacancies faster."),
  ("Which policy is most likely to reduce the natural rate of unemployment? (Oct/Nov 2020 · 33 · Q30, reworded)", ["More government spending on goods and services", "More spending on training schemes to fix skill shortages", "A longer period of eligibility for welfare benefits", "A higher minimum wage"], 1, "Training addresses the structural part of the natural rate. The other options raise demand or raise the wage floor."),
  ("What is most likely to result from a fall in the natural rate of unemployment? (May/June 2024 · 31 · Q17, reworded)", ["A fall in government spending on goods and services", "A fall in payments to the unemployed", "A fall in trade union membership", "A fall in interest rates"], 1, "Fewer people unemployed in equilibrium means lower benefit payments.")
]

exam = exam_page("the natural rate of unemployment",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The natural rate appears in Paper 4 mostly in long essays that compare Keynesian and monetarist views, and in Paper 3 multiple choice. Reworded questions are below, with a practice question on determinants, and eight Paper 3 multiple choice questions.",
  [("Essay, 25 marks", "2", "Feb/March 2022 (42) Q6; May/June 2022 (41) Q7"), ("Essay part, 13 marks", "1", "Oct/Nov 2020 (41) Q7(b)"), ("Practice question", "1", "Determinants of the natural rate"), ("Multiple choice (Paper 3)", "8 shown below", "2021 to 2025")],
  [
  eq("Based on Feb/March 2022 · 9708/42 · Q6", "25 marks", "'Government policies that rely on increasing budget deficits to solve unemployment will not succeed because they do not affect the natural rate of unemployment.' Discuss the extent to which you agree.",
     ["A budget deficit as Keynesian demand management that targets cyclical unemployment, with a multiplier effect on AD, output and jobs.",
      "The natural rate is unemployment that remains when the labour market is in equilibrium: frictional and structural. Demand policy does not address these, so the statement has some force.",
      "Supply-side policies (union reform, lower taxes, retraining, subsidies to growth industries) are more suitable for the natural rate.",
      "Evaluation: budget deficits may still fail even for cyclical unemployment (higher interest rates and crowding out, inflation if money is printed, leakages); hysteresis means cyclical unemployment can become structural, so demand policy may affect the natural rate after all."],
     "Explain the Keynesian route. Define the natural rate. Show deficits do not reach it. Evaluate with crowding out, hysteresis and the case for supply-side policy."),
  eq("Based on May/June 2022 · 9708/41 and 43 · Q7", "25 marks", "Keynesians say bigger budget deficits will cure unemployment. Monetarists say supply-side policies are more effective. Consider which view is more likely to be correct.",
     ["Explain a budget deficit and why unemployment is a problem (waste of scarce resources).",
      "Keynesian case: a deficit raises AD, and with the multiplier output, income and jobs rise, especially with a negative output gap.",
      "Monetarist case: borrowing raises interest rates and crowds out investment, printed money causes inflation, and demand policy cannot help structural or frictional unemployment. Supply-side examples: deregulation, privatisation, lower corporation tax, labour market reform.",
      "Evaluation: which view holds depends on the type of unemployment, the state of the economy and time horizon. A good answer concludes that the best policy matches the cause."],
     "Define deficit and the problem. Keynesian case. Monetarist case. Match policy to cause of unemployment and give a reasoned verdict."),
  eq("Based on Oct/Nov 2020 · 9708/41 · Q7(b)", "13 marks", "'Government intervention through supply-side policies will have little effect on unemployment, whereas freer-market supply-side policies will cut unemployment significantly.' Discuss.",
     ["Distinguish interventionist supply-side policies (education and training, subsidies, infrastructure, job centres) from market-based ones (deregulation, privatisation, lower taxes and benefits, weaker unions), with at least two examples of each.",
      "Discuss how much each group would reduce unemployment, and for which types: interventionist policies suit structural and frictional unemployment; market-based policies work on incentives and wage flexibility.",
      "Level 4 needs analysis of both groups and a reasoned conclusion on the statement."],
     "Two groups, two examples each. Effects on unemployment. Weigh them and conclude."),
  eq("Practice (not a past paper question)", "8 marks", "Explain two factors that determine the natural rate of unemployment and how a government could reduce it.",
     ["Two determinants explained with a chain: for example unemployment benefits (replacement ratio) and labour mobility, or union power and skills.",
      "A policy for each: reform benefits or job search conditions, improve housing or transport, retraining, information.",
      "A reason why the policy works on the natural rate rather than cyclical unemployment: it shifts LRAS and lowers frictional or structural unemployment.",
      "Evaluation: time lags, cost, fairness."],
     "Two factors, each with cause and policy. One evaluative remark.",
     [[("k", "The natural rate of unemployment is the rate when the labour market is in equilibrium, made up of frictional and structural unemployment."), ("n", "One determinant is the level of unemployment benefit. If benefits are high and available for a long time, the unemployed may be less willing to accept the first job on offer, so the average search time is longer and frictional unemployment is higher.")],
      [("a", "A government could shorten the period for which benefits are paid or link them to evidence of job search, which would give more incentive to take work and lower the natural rate."), ("n", "A second determinant is the skills and mobility of workers. When an industry declines, workers with outdated skills or who live far from vacancies stay unemployed, which raises structural unemployment. Training and housing or transport support would improve matching and shift the LRAS to the right.")],
      [("e", "However, these supply-side policies take time and cost money, and cutting benefits could increase hardship and inequality, so their effect on the natural rate may be slow and politically difficult.")]])
  ],
  )

tips = tips_html(
  [("Define the natural rate with its parts.", "Frictional, structural and seasonal unemployment when the labour market is in equilibrium."),
   ("Say NAIRU means stable inflation.", "At the natural rate inflation is neither accelerating nor decelerating."),
   ("Link determinants to a mechanism.", "Benefits change the incentive to search, union power raises wages, mobility and training change matching, information shortens search."),
   ("Use the vertical long-run Phillips curve.", "Demand policy can push unemployment below the natural rate only temporarily, and inflation ends up higher."),
   ("Match policy to type.", "Demand policy for cyclical unemployment. Supply-side policy for the natural rate."),
   ("Evaluate the monetarist view.", "Expectations may adjust slowly, the economy may have spare capacity, the natural rate is hard to estimate, and hysteresis blurs the line."),
   ("Be careful with the word 'cause'.", "Say 'could raise' or 'may lower'. Estimates of the natural rate are uncertain.")],
  [("Define", "The natural rate of unemployment is the rate when the labour market is in equilibrium, consisting of frictional, structural and seasonal unemployment."),
   ("Determinant", "A rise in unemployment benefits could lengthen the average job search, which raises frictional unemployment and the natural rate."),
   ("Implication", "Demand-side policy cannot reduce unemployment below the natural rate for long without accelerating inflation."),
   ("Supply-side", "Retraining could reduce structural unemployment, shifting the LRAS to the right and lowering the natural rate."),
   ("Evaluate", "However, the natural rate is difficult to estimate and may be raised by hysteresis, so demand management may still matter.")],
  [CW["define"], CW["explain"], CW["assess"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Stacked bar showing the natural rate made of frictional, structural and seasonal unemployment, and the cyclical part on top">${(() => { let o = SV.line(70, 280, 700, 280); const parts = [["Frictional", 1.5, "f1", "t1"], ["Structural", 2.5, "f4", "t4"], ["Seasonal", 0.5, "f3", "t3"], ["Cyclical (disequilibrium)", 3, "f2", "t2"]]; let x = 70; parts.forEach(([l, v, c, t], i) => { const w = v * 90; o += SV.rect(x, 130, w, 70, c, { opacity: i === 3 ? 0.5 : 0.9 }) + SV.text(x + w / 2, 170, v + "%", "lbl bd", { "text-anchor": "middle" }); o += tag(x + w / 2, 125 - (i % 2) * 18, l, t, 1, "middle"); x += w; }); o += SV.line(70 + 4.5 * 90, 110, 70 + 4.5 * 90, 220, "c1 dash") + tag(70 + 4.5 * 90, 240, "natural rate = 4.5%", "t1", 1, "middle") + tag(70 + 7.5 * 90 - 4, 240, "actual unemployment = 7.5%", "t2", 1, "end") + tag(70, 40, "Actual unemployment = natural rate + cyclical unemployment", "t1"); return o; })()}</svg>`;

/* ---------- Watch 1: Phillips curves ---------- */
const PX = (u) => 70 + u * 52, PY = (p) => 300 - p * 26;
const srEnd = (p0, us) => Math.min(8, us + (p0 - 0.2) / 1.5);
function phDraw(s) {
  const sr = (u, p0, us) => p0 + 1.5 * (us - u);
  let o = axes(70, 300, 740, 30, "Unemployment rate (%)", "Inflation (%)");
  [0, 2, 4, 6, 8, 10].forEach((v) => (o += SV.text(PX(v), 318, v, "sm", { "text-anchor": "middle" })));
  o += SV.line(PX(s.us), PY(0), PX(s.us), PY(10.5), "c3", { "stroke-width": 3 }) + tag(PX(s.us) + 6, 44, "LRPC at the natural rate", "t3");
  if (s.old > 0) { const e = srEnd(2, 5), ps = sr(0.5, 2, 5), pe = sr(e, 2, 5); o += SV.line(PX(0.5), PY(ps), PX(e), PY(pe), "c2 dash", op(s.old)) + tag(PX(e) + 6, PY(pe) - 4, "SRPC₁", "t2", s.old); }
  const e2 = srEnd(s.p0, s.us), a = sr(0.5, s.p0, s.us), b = sr(e2, s.p0, s.us);
  o += SV.line(PX(0.5), PY(a), PX(e2), PY(b), "c2") + tag(PX(e2) + 6, PY(b) - 4, "SRPC", "t2");
  o += SV.circle(PX(s.u), PY(s.p), 8, "dot4") + tag(PX(s.u) + 12, PY(s.p) - 12, s.l, "t4");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 345, label: "Short-run Phillips curve shifting up when expectations adjust, and the vertical long-run Phillips curve at the natural rate", base: { us: 5, p0: 2, old: 0, u: 5, p: 2, l: "A" }, draw: phDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>At the natural rate.</b> Unemployment is 5% and inflation is 2%, which people expect. This is point A on the short-run Phillips curve (SRPC). The vertical long-run curve (LRPC) is at the natural rate.", s: {} },
  { cap: "<b>A demand stimulus.</b> The government expands demand to push unemployment to 3%. Prices rise faster than expected and wages lag, so real wages fall for a while and firms hire more. The economy moves <b>up the SRPC</b> to B: lower unemployment, 5% inflation.", s: { u: 3, p: 5, l: "B" } },
  { cap: "<b>Expectations adjust.</b> Workers see that prices are rising 5% a year and demand higher wages. The SRPC <b>shifts up</b>. Unemployment returns to the natural rate of 5%, but now inflation is 5%: C. The gain in jobs has gone and the cost in inflation remains.", s: { p0: 5, old: 1, u: 5, p: 5, l: "C" } },
  { cap: "<b>Trying again.</b> If the government keeps aiming at 3% unemployment, inflation must keep rising: 8% at D, and then more. Unemployment can only be held below the natural rate if inflation <b>accelerates</b>.", s: { p0: 5, old: 1, u: 3, p: 8, l: "D" } },
] });

/* ---------- Watch 2: supply-side lowers the natural rate ---------- */
function nrDraw(s) {
  const sr = (u, p0, us) => p0 + 1.5 * (us - u);
  let o = axes(70, 300, 740, 30, "Unemployment rate (%)", "Inflation (%)");
  [0, 2, 4, 6, 8, 10].forEach((v) => (o += SV.text(PX(v), 318, v, "sm", { "text-anchor": "middle" })));
  o += SV.line(PX(5), PY(0), PX(5), PY(10.5), "c3 dash", op(0.6)) + tag(PX(5) + 6, 60, "LRPC₁ (5%)", "t3");
  o += SV.line(PX(0.5), PY(sr(0.5, 2, 5)), PX(srEnd(2, 5)), PY(sr(srEnd(2, 5), 2, 5)), "c2 dash", op(0.5));
  const us = s.us; o += SV.line(PX(us), PY(0), PX(us), PY(10.5), "c3", { "stroke-width": 3 }) + tag(PX(us) - 6, 44, s.us < 5 ? "LRPC₂ (3.5%)" : "", "t3", 1, "end");
  o += SV.line(PX(0.5), PY(sr(0.5, 2, us)), PX(srEnd(2, us)), PY(sr(srEnd(2, us), 2, us)), "c2") + SV.circle(PX(us), PY(2), 8, "dot4") + tag(PX(us) + 12, PY(2) - 12, s.l, "t4");
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 345, label: "Supply side policy shifting the long-run Phillips curve left, lowering the natural rate", base: { us: 5, l: "natural rate 5%, inflation 2%" }, draw: nrDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The starting point.</b> The natural rate is 5% and inflation is 2%.", s: {} },
  { cap: "<b>Supply-side reform.</b> Better job information, retraining, easier mobility and a benefit system with stronger work incentives cut frictional and structural unemployment. The LRPC and SRPC both shift <b>left</b>.", s: { us: 3.5, l: "natural rate 3.5%, inflation 2%" } },
  { cap: "<b>The result.</b> The economy has permanently <b>lower unemployment at the same inflation</b>. Unlike a demand stimulus there is no inflation cost, but the reform takes time and may carry costs of its own (cost, fairness).", s: { us: 3.5, l: "natural rate 3.5%, inflation 2%" } },
] });

/* ---------- Lab 1: determinants ---------- */
function labNat() {
  if (!$("#bn") || !$("#un") || !$("#mb") || !$("#tr")) return;
  const b = +$("#bn").value, u = +$("#un").value, m = +$("#mb").value, t = +$("#tr").value;
  const fr = Math.max(0.5, 1 + 0.025 * b - 0.012 * m), st = Math.max(0.5, 1.5 + 0.02 * u - 0.018 * t - 0.008 * m + 0.01 * b), se = 0.5, nat = fr + st + se;
  $("#r1").textContent = Lib.fmtN(fr, 1) + "%"; $("#r2").textContent = Lib.fmtN(st, 1) + "%"; $("#r3").textContent = Lib.fmtN(nat, 1) + "%";
  $("#rv").textContent = `Frictional ${Lib.fmtN(fr, 1)}% + structural ${Lib.fmtN(st, 1)}% + seasonal 0.5% = natural rate ${Lib.fmtN(nat, 1)}%. ` + (b > 60 ? "Generous benefits lengthen job search. " : "") + (u > 60 ? "Strong union power pushes wages above equilibrium. " : "") + (m < 40 ? "Low mobility slows matching. " : "") + (t < 40 ? "Weak training leaves a skills mismatch. " : "") + (b <= 60 && u <= 60 && m >= 40 && t >= 40 ? "This labour market works fairly well, so the natural rate is low." : "");
  const k = 36, base = 250, parts = [[fr, "f1"], [st, "f4"], [se, "f3"]]; let y = base, o = SV.line(60, base, 380, base);
  parts.forEach(([v, c], i) => { const h = v * k; y -= h; o += SV.rect(150, y, 120, h, c) + SV.text(210, y + h / 2 + 5, ["Frictional", "Structural", "Seasonal"][i] + " " + Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" }); });
  o += tag(210, y - 10, "natural rate " + Lib.fmtN(nat, 1) + "%", "t1", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "bn", label: "Benefit generosity (0 to 100) ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labNat });
Lib.slider($("#g2"), { id: "un", label: "Union power (0 to 100) ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labNat });
Lib.slider($("#g3"), { id: "mb", label: "Labour mobility (0 to 100) ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labNat });
Lib.slider($("#g4"), { id: "tr", label: "Training and job information (0 to 100) ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labNat });
labNat();

/* ---------- Lab 2: target below the natural rate ---------- */
function labTarget() {
  if (!$("#tg")) return;
  const tg = +$("#tg").value / 10, nru = 5, infl = [2]; for (let y = 1; y <= 6; y++) infl.push(tg < nru ? infl[y - 1] + 1.5 * (nru - tg) : 2);
  $("#t1").textContent = Lib.fmtN(tg, 1) + "%"; $("#t2").textContent = Lib.fmtN(infl[6], 1) + "%"; $("#t3").textContent = tg < nru ? "Only with rising inflation" : "Yes, at stable inflation";
  $("#tv").textContent = tg < nru ? `Holding unemployment ${Lib.fmtN(nru - tg, 1)} points below the natural rate pushes inflation up by about ${Lib.fmtN(1.5 * (nru - tg), 1)} points a year as expectations adjust. After six years inflation reaches ${Lib.fmtN(infl[6], 1)}%.` : "A target at or above the natural rate is consistent with stable inflation of about 2%.";
  const X = (y) => 50 + y * 52, Y = (v) => 260 - v * 8;
  let o = SV.line(50, 260, 400, 260) + SV.line(50, 260, 50, 20) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Inflation (%)", "sm");
  [0, 5, 10, 15, 20, 25].forEach((v) => { o += SV.text(44, Y(v) + 4, v, "sm", { "text-anchor": "end" }); });
  o += SV.path(Lib.ptsPath(infl.map((v, i) => [X(i), Y(Math.min(v, 28))])), tg < nru ? "c2" : "c3") + tag(396, Y(Math.min(infl[6], 28)) - 8, Lib.fmtN(infl[6], 1) + "%", tg < nru ? "t2" : "t3", 1, "end");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "tg", label: "Unemployment target (x10 %) ", min: 20, max: 80, step: 5, value: 30, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labTarget });
labTarget();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Would the change raise or lower the natural rate of unemployment?", ["Raises it", "Lowers it"],
  [("Unemployment benefits become more generous and last longer", 0), ("Free retraining for workers in declining industries", 1), ("A national job-vacancy website is launched", 1), ("Trade unions win a large rise in wages above the market rate", 0), ("Housing becomes cheaper in areas with vacancies", 1), ("A long recession leaves many workers with outdated skills", 0), ("Hiring and firing rules become much stricter", 0), ("Support for workers to move to new regions", 1)],
  "Anything that improves matching of workers to jobs lowers the natural rate.") + MATCH([
  ["Natural rate", "Unemployment when the labour market is in equilibrium"],
  ["NAIRU", "Unemployment rate at which inflation does not accelerate"],
  ["LRPC", "Vertical long-run Phillips curve at the natural rate"],
  ["Replacement ratio", "Benefit income as a share of previous earnings"],
  ["Structural unemployment", "Mismatch of skills or location with the jobs available"],
  ["Frictional unemployment", "Time spent searching between jobs"]]) + ORDER(
  "Put the monetarist argument about demand stimulus in order.",
  ["The government expands demand to cut unemployment below the natural rate", "Prices rise faster than workers expected and real wages fall", "Firms hire more and unemployment falls temporarily", "Workers revise their expectations and demand higher wages", "Unemployment returns to the natural rate with higher inflation"],
  "Without a change in the natural rate, demand policy only buys a temporary fall in unemployment.") + CALC([
  {"q": "In an economy frictional unemployment is 1.5%, structural 2.5% and seasonal 0.5% of the labour force. Calculate the natural rate of unemployment (%).", "a": 4.5, "unit": "%", "tol": 0.05, "hint": "Add the three types.", "sol": "1.5 + 2.5 + 0.5 = <b>4.5%</b>."},
  {"q": "Actual unemployment is 7.5% and the natural rate is 4.5%. What percentage of the labour force is cyclically unemployed?", "a": 3, "unit": "%", "tol": 0.05, "hint": "Actual minus natural.", "sol": "7.5 − 4.5 = <b>3%</b>."},
  {"q": "Expected inflation is 3%. Each percentage point of unemployment below the natural rate (5%) adds 1.5 points to inflation. Calculate inflation if unemployment is held at 3.5%.", "a": 5.25, "unit": "%", "tol": 0.05, "hint": "Gap = 1.5 points. Add 1.5 × 1.5 to 3.", "sol": "3 + 1.5 × 1.5 = <b>5.25%</b>."},
  {"q": "The replacement ratio is the benefit received divided by previous earnings. A worker earned $2,000 a month and receives $1,300 in benefits. Calculate the replacement ratio (%).", "a": 65, "unit": "%", "tol": 0.05, "hint": "1300 ÷ 2000.", "sol": "1300 ÷ 2000 × 100 = <b>65%</b>."}]) + MCQ([
  ("What does the natural rate of unemployment include?", ["Cyclical unemployment only", "Frictional, structural and seasonal unemployment", "Real wage unemployment only", "All unemployment"], 1, "It is the unemployment that remains when the labour market is in equilibrium."),
  ("According to monetarists, what is the long-run effect of a demand stimulus that cuts unemployment below the natural rate?", ["Permanently lower unemployment", "Higher inflation with unemployment back at the natural rate", "Lower inflation", "No effect on prices"], 1, "Expectations adjust, so the gain in jobs disappears and inflation is higher."),
  ("Which policy would most directly lower the natural rate?", ["A cut in interest rates", "Retraining for workers in declining industries", "Higher government spending on defence", "A rise in the minimum wage"], 1, "Retraining lowers structural unemployment."),
  ("Which statement is a Keynesian criticism of the natural rate theory?", ["The natural rate is fixed forever", "Hysteresis means the natural rate can be raised by recessions", "Demand has no effect on unemployment", "Inflation never changes"], 1, "Long recessions can leave the unemployed with outdated skills and raise the equilibrium rate."),
  ("The natural rate is also known as the:", ["NAIRU", "GDP gap", "Participation rate", "Poverty line"], 0, "NAIRU is the non-accelerating inflation rate of unemployment, used as another name for the natural rate.")
], "qz1") + CARDS([
  ("Natural rate of unemployment", "Unemployment at labour market equilibrium: frictional, structural, seasonal."),
  ("NAIRU", "Rate of unemployment at which inflation neither accelerates nor decelerates."),
  ("Long-run Phillips curve", "Vertical at the natural rate."),
  ("Replacement ratio", "Benefits as a share of previous earnings."),
  ("Expectations", "Beliefs about future inflation that affect wage bargaining."),
  ("Supply-side policy", "Policy that raises capacity and lowers the natural rate."),
  ("Hysteresis", "A recession can raise the natural rate through lost skills."),
  ("Insider-outsider", "Employed insiders keep wages high at the expense of unemployed outsiders.")]) + MCQ(mc_exam)

build("sy934", "natural-rate-of-unemployment", "The Natural Rate of Unemployment", EY,
  "9.3.4: the natural rate and NAIRU, what determines it, and what it means for demand-side and supply-side policy. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
