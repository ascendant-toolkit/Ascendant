"""Syllabus 10.2.5 Inflation and unemployment: the Phillips curve. Run: python3 tools/artifact-kit/mk_sy1025.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 10.2.5"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">traditional Phillips curve</b> shows an inverse relationship between unemployment and inflation (or wage growth): lower unemployment goes with higher inflation, so a government faces a <b>trade-off</b>. In the 1970s <b>stagflation</b> (high inflation with high unemployment) broke the pattern. The <b class="kw">expectations-augmented Phillips curve</b> explains why: each <b>short-run curve</b> depends on expected inflation, so it shifts when expectations change, and the <b class="kw">long-run Phillips curve</b> is <b>vertical at the natural rate</b> of unemployment. Demand policy can reduce unemployment below the natural rate only temporarily, at the price of accelerating inflation.</p></div>

  <h2>1 · The traditional Phillips curve</h2>
  <ul>
    <li><b>Origin:</b> A.W. Phillips (1958) found an inverse link between wage inflation and unemployment in UK data from 1861 to 1957. Later economists replaced wage inflation with <b>price inflation</b>.</li>
    <li><b>Why:</b> low unemployment means a tight labour market, so workers gain bargaining power and wages rise; firms pass higher costs on, and demand for goods is strong (demand-pull). High unemployment weakens both.</li>
    <li><b>Shape:</b> downward sloping and convex: reducing unemployment further costs more inflation.</li>
    <li><b>Policy menu:</b> a government could choose a point on the curve, such as lower unemployment with higher inflation, or the reverse.</li>
  </ul>
  <div id="pic1" class="card"></div>
  <p><b>Axes:</b> inflation rate (%) on the vertical axis, unemployment rate (%) on the horizontal axis.</p>

  <h2>2 · The breakdown in the 1970s</h2>
  <p>After the 1973 oil price shock many countries had <b>both high inflation and high unemployment</b>: <b>stagflation</b>. The curve seemed to have shifted outwards. Two explanations: <b>supply shocks</b> (cost-push) shift the curve up, and <b>expectations</b> of inflation raised wage demands whatever the level of unemployment.</p>

  <h2>3 · The expectations-augmented Phillips curve</h2>
  <div class="formula">inflation = expected inflation + a × (natural rate − unemployment)</div>
  <ul>
    <li><b>Short-run Phillips curve (SRPC):</b> drawn for a given level of <b>expected inflation</b>. Moving up it, the economy has lower unemployment and higher inflation. Workers wrongly expect lower inflation than actually happens, so their real wage falls and firms hire.</li>
    <li><b>Shift of the SRPC:</b> when expected inflation rises, workers bargain for higher wages and the SRPC <b>shifts up</b>. Unemployment returns to the natural rate but with higher inflation.</li>
    <li><b>Long-run Phillips curve (LRPC):</b> a <b>vertical line at the natural rate of unemployment</b>, because in the long run expectations adjust and there is no trade-off.</li>
    <li><b>Accelerationist view:</b> to keep unemployment below the natural rate the government must keep raising demand, so inflation <b>accelerates</b>.</li>
    <li><b>Disinflation:</b> to cut inflation the economy has to move down the SRPC (unemployment above the natural rate) until expectations fall. The <b>sacrifice ratio</b> measures the cost.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Event</th><th>On the diagram</th></tr>
    <tr><td>AD rises, with unemployment falling and inflation rising</td><td>Move <b>up along</b> the SRPC</td></tr>
    <tr><td>Expected inflation rises</td><td>SRPC <b>shifts up</b></td></tr>
    <tr><td>Supply shock (oil price rise)</td><td>SRPC <b>shifts up</b> (stagflation)</td></tr>
    <tr><td>Supply-side policy lowers the natural rate</td><td>LRPC and SRPC <b>shift left</b></td></tr>
    <tr><td>Credible anti-inflation policy lowers expected inflation</td><td>SRPC <b>shifts down</b></td></tr>
  </table></div>

  <h2>4 · Evaluation</h2>
  <ul>
    <li>The natural rate is hard to estimate and changes over time (see 9.3.4).</li>
    <li><b>Hysteresis:</b> long spells of unemployment can raise the natural rate, so the LRPC is not truly fixed.</li>
    <li>Since the 1990s the curve has often looked <b>flat</b>: low and stable inflation over a wide range of unemployment, perhaps because expectations are anchored by central bank targets and globalisation holds down prices.</li>
    <li><b>Rational expectations:</b> if workers anticipate policy, even the short-run trade-off may vanish, so credible policy is crucial.</li>
    <li>Keynesians accept a short-run trade-off but think the long run is not vertical when there is spare capacity.</li>
  </ul>
'''

watch = '''
  <h2>1 · The traditional Phillips curve and the policy menu</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stT"></div>
  <h2>2 · Stagflation and disinflation with expectations</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · The expectations-augmented Phillips curve</h2>
  <p>Set expected inflation, the natural rate and how sensitive inflation is to unemployment. Choose an unemployment rate and read off inflation.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Inflation</small><strong id="r1"></strong></div><div><small>Gap from natural rate</small><strong id="r2"></strong></div><div><small>Long-run inflation</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Short-run and long-run Phillips curves with a chosen point"></svg></div></div></div>

  <h2>Lab 2 · The cost of disinflation</h2>
  <p>Inflation is too high. To cut it, unemployment must stay above the natural rate until expectations adjust. The sacrifice ratio is the number of point-years of extra unemployment per point of inflation removed.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Total excess unemployment</small><strong id="t1"></strong></div><div><small>Years needed</small><strong id="t2"></strong></div><div><small>Lost output (Okun, % of a year)</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Inflation falling over the years while unemployment stays above the natural rate"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Movement along or shift of the curve?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the accelerationist argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The 1970s stagflation", "After the oil price rises of 1973 and 1979 many economies had inflation of 10% or more at the same time as unemployment rising to record post-war levels. Governments that stimulated demand to reduce unemployment saw inflation take off.", "the standard evidence for stagflation and expectations. Say that both supply shocks and expectations were involved.") +
rw("The Volcker disinflation in the US", "In 1979 to 1982 the US Federal Reserve raised interest rates sharply to bring down inflation of over 10%. Unemployment rose to around 10% before inflation fell to below 4%.", "an example of the cost of disinflation: moving down the short-run curve until expectations fall. Use it for the sacrifice ratio.") +
rw("A flat Phillips curve after 2010", "After the financial crisis unemployment fell from 10% to under 4% in the US in the 2010s, but inflation stayed close to 2%. Economists asked whether the curve had flattened because inflation expectations were anchored.", "evidence against a strong short-run trade-off. Use it in evaluation and add that the 2021 to 2022 inflation surge revived the debate.") +
rw("Labour market reform and the natural rate", "Reforms to benefits, job-matching services and wage bargaining in several European countries are credited with lowering the unemployment rate at which inflation stays stable, shifting the long-run curve left.", "supply-side policy shifting the LRPC. Link to 9.3.4.")
)

mc_exam = [
  ("Why is it likely that a curve showing the relationship between unemployment and inflation only applies in the short run? (Oct/Nov 2024 · 33 · Q21, reworded)", ["Any attempt to reduce unemployment will increase inflation", "Increased inflation actually increases unemployment", "Increased inflation leads to expectations of further inflation", "Increased inflation reduces real wages, which increases the demand for labour"], 2, "In the long run workers expect higher inflation and bargain for higher wages, so the trade-off disappears."),
  ("An economy uses expansionary monetary policy to boost employment, and the consumer price index rises at an accelerating rate. Which curve could represent this? (Oct/Nov 2022 · 31 · Q28, reworded)", ["Kuznets curve", "Laffer curve", "Lorenz curve", "Phillips curve"], 3, "A Phillips curve shows the link between inflation and unemployment."),
  ("What are the labels on the axes of a Phillips curve diagram? (Oct/Nov 2022 · 32 · Q30, reworded)", ["Vertical: inflation rate, horizontal: unemployment level", "Vertical: inflation rate, horizontal: unemployment rate", "Vertical: price level, horizontal: unemployment level", "Vertical: price level, horizontal: unemployment rate"], 1, "The Phillips curve plots the rate of inflation against the rate of unemployment."),
  ("What is measured on the vertical axis of the Phillips curve? (Oct/Nov 2023 · 33 · Q22, reworded)", ["The rate of change of real wages", "The rate of change of take-home pay", "The rate of inflation", "The rate of interest"], 2, "The traditional curve has inflation (or wage inflation) on the vertical axis."),
  ("A table gives year, unemployment rate and inflation rate: year 1 (7.6, 2.6), year 2 (6.2, 1.6), year 3 (5.8, 1.8), year 4 (5.9, 2.0), year 5 (5.8, 2.0). Which change between consecutive years agrees with the Phillips curve? (May/June 2025 · 34 · Q23, reworded)", ["Year 1 to year 2", "Year 2 to year 3", "Year 3 to year 4", "Year 4 to year 5"], 1, "From year 2 to year 3 unemployment fell and inflation rose: the inverse relationship."),
  ("Unemployment and inflation (2010, 2014): Australia 5.2, 6.1 and 2.7, 1.6; Canada 8.0, 6.9 and 2.2, 1.9; Japan 5.1, 3.6 and −0.3, 2.5; US 9.6, 6.2 and 1.7, 0.6. Which countries had a typical Phillips curve? (Oct/Nov 2023 · 31 · Q26, reworded)", ["Australia and Japan", "Australia only", "Japan only", "Canada and the United States"], 0, "A typical Phillips curve shows unemployment and inflation moving in opposite directions: Australia (up, down) and Japan (down, up)."),
  ("Inflation and unemployment in 2008 and 2011: Canada 2.38, 2.89 and 6.15, 7.47; France 3.16, 2.29 and 7.81, 9.68; Germany 2.75, 2.48 and 7.60, 5.98; Japan 1.37, −0.28 and 3.99, 4.55. Which experienced a trade-off between inflation and unemployment? (Oct/Nov 2023 · 32 · Q21, reworded)", ["Canada and Germany", "Canada only", "France and Japan", "France only"], 2, "In France and Japan inflation fell while unemployment rose. In Canada both rose and in Germany both fell."),
  ("An economy is at its natural rate. When will an increase in government spending to reduce unemployment most conflict with low inflation? (May/June 2025 · 31 · Q23, reworded)", ["If inflationary expectations are unchanged", "If inflationary expectations fall", "If labour productivity rises", "If labour supply rises"], 0, "If workers do not expect the extra inflation, they accept the lower real wage for a time; once expectations adjust, inflation rises with no lasting fall in unemployment.")
]

exam = exam_page("the Phillips curve and the link between inflation and unemployment",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The Phillips curve is tested in 20 mark Paper 4 essays (usually with fiscal policy) and in many Paper 3 data questions. Reworded questions are below, with two practice questions and eight Paper 3 multiple choice questions.",
  [("Essay, 20 marks", "2", "May/June 2025 (41, 43) Q4; Oct/Nov 2024 (41) Q4"), ("Practice questions", "2", "Traditional versus expectations-augmented; why the curve shifts"), ("Multiple choice (Paper 3)", "8 shown below", "2022 to 2025")],
  [
  eq("Based on May/June 2025 · 9708/41 and 43 · Q4", "20 marks", "A country is experiencing stagflation: high inflation at the same time as a negative output gap. With the help of a diagram, evaluate how effective fiscal policy would be in solving this problem.",
     ["<b>Knowledge and analysis (14):</b> define inflation and why it is a problem; define a negative output gap; AD and AS diagram showing stagflation (SRAS shifting left, so price level rises and output falls below potential). Explain fiscal policy, and how it could close the output gap (raise AD) or reduce inflation (cut AD). Maximum 8 marks without a relevant diagram.",
      "Show why the two aims conflict: expansionary fiscal policy closes the gap but raises prices; contractionary policy cuts inflation but widens the gap.",
      "<b>Evaluation (6):</b> fiscal policy aims at demand, but stagflation is caused by supply, so supply-side policy or exchange rate policy may be better; time lags; debt and crowding out; expectations may make inflation persist; a judgement on which problem to prioritise."],
     "Draw AD and AS with SRAS shift left. Show the conflict for fiscal policy. Evaluate: wrong tool for a supply shock, lags, expectations. Conclude on a mix of policies."),
  eq("Based on Oct/Nov 2024 · 9708/41 · Q4", "20 marks", "In periods of rising and persistent inflation, consumers and workers change their expectations of the future rate of inflation. Evaluate, with the help of a diagram or diagrams, the consequences of these changed expectations for fiscal policy.",
     ["<b>Knowledge and analysis (14):</b> define inflation and the non-accelerating inflation rate of unemployment; expectations based on past inflation; AD and AS diagram to show inflation; the Phillips curve trade-off between wage growth or inflation and employment; the wage-price spiral; how fiscal policy affects unemployment and inflation; the effect of changing expectations. Maximum Level 2 without a diagram.",
      "<b>Evaluation (6):</b> with changing expectations, the fall in unemployment from a fiscal stimulus is temporary, because workers negotiate higher wages to offset past inflation (the SRPC shifts up); policy may have to be tighter, and credibility matters; fiscal policy is better used with supply-side measures; other factors."],
     "Define expectations. Diagram: SRPC shifting up. Fiscal stimulus gives a temporary gain. Evaluate with credibility and the supply side."),
  eq("Practice (not a past paper question)", "12 marks", "Explain the difference between the traditional Phillips curve and the expectations-augmented Phillips curve.",
     ["Traditional: an inverse relationship between unemployment and inflation (or wage growth), stable over time, giving a trade-off the government could exploit.",
      "Expectations-augmented: each short-run curve depends on expected inflation, so it shifts when expectations change; the long-run curve is vertical at the natural rate.",
      "Link to the 1970s: stagflation as evidence; implication that demand policy only has temporary effects and supply-side policy is needed to lower the natural rate.",
      "Evaluation: the natural rate is uncertain, hysteresis, a flat curve in recent decades."],
     "Traditional first, with the trade-off. Then expectations and the vertical long-run curve. Then policy implication and a limit.",
     [[("k", "The traditional Phillips curve shows an inverse relationship between the rate of unemployment and the rate of inflation, so that lower unemployment is associated with higher inflation. It suggested a stable trade-off from which a government could choose a combination, for example accepting 4% inflation in return for lower unemployment."), ("n", "The expectations-augmented Phillips curve says that this trade-off holds only in the short run, for a given level of expected inflation. If the government pushes unemployment below the natural rate, inflation rises above what workers expected, so real wages fall and firms hire more. Once workers see prices rising faster they demand higher wages and the short-run curve shifts up, and unemployment returns to the natural rate with higher inflation.")],
      [("n", "The long-run Phillips curve is therefore vertical at the natural rate of unemployment, and to keep unemployment below that rate inflation would have to keep accelerating. This explains stagflation in the 1970s, when supply shocks and rising expectations shifted the curve up, and it implies that only supply-side policies that lower the natural rate can reduce unemployment permanently."), ("e", "However, the natural rate is difficult to estimate, hysteresis can raise it after a recession, and since the 1990s the curve has often looked flat because expectations are anchored by central bank targets, so the relationship is less reliable than the theory suggests.")]]),
  eq("Practice (not a past paper question)", "8 marks", "Explain why the short-run Phillips curve might shift upwards.",
     ["Higher expected inflation: workers bargain for higher wages to keep real wages, so the same unemployment rate goes with more inflation.",
      "A supply shock (higher oil prices or import costs) raises costs and prices whatever the level of unemployment (cost-push).",
      "A rise in the natural rate (for example after hysteresis) shifts the curve to the right.",
      "Evaluation: whether expectations are adaptive or forward-looking determines the speed of the shift."],
     "Expectations. Supply shock. Natural rate. One evaluative remark.",
     [[("k", "The short-run Phillips curve shows the trade-off between inflation and unemployment for a given level of expected inflation."), ("n", "It shifts upwards if expected inflation rises. Workers who expect prices to rise faster bargain for bigger pay rises, firms pass the costs on, and so at every level of unemployment inflation is higher. It also shifts up after a supply shock such as a sharp rise in oil prices, because firms' costs rise and they raise prices whether or not unemployment changes, which is how stagflation can arise.")],
      [("a", "A rise in the natural rate of unemployment, for example because long-term unemployment has led workers to lose skills, would shift the curve to the right."), ("e", "However, how quickly the curve shifts depends on whether expectations adapt slowly to past inflation or respond immediately to announced policy, so credibility of the central bank may reduce the shift.")]])
  ],
  )

tips = tips_html(
  [("Label the axes correctly.", "Inflation rate on the vertical axis and unemployment rate on the horizontal axis."),
   ("Say 'short run' and 'long run'.", "The trade-off holds in the short run. The long-run curve is vertical at the natural rate."),
   ("Movement or shift?", "A change in unemployment along the curve is a movement. A change in expected inflation or a supply shock is a shift."),
   ("Name stagflation.", "High inflation and high unemployment together. Cause: supply shock and expectations."),
   ("Always use a diagram in a 20 mark question.", "Without one the answer is capped at Level 2."),
   ("Link to policy.", "Demand policy: temporary. Supply-side policy: lowers the natural rate. Credible central bank: lowers expectations."),
   ("Evaluate with data.", "The natural rate is uncertain, and the curve has looked flat since the 1990s.")],
  [("Trade-off", "The traditional Phillips curve suggests that a government can reduce unemployment only by accepting higher inflation."),
   ("Expectations", "When workers expect higher inflation they demand higher wages, so the short-run Phillips curve shifts upwards."),
   ("Long run", "The long-run Phillips curve is vertical at the natural rate of unemployment, so there is no long-run trade-off."),
   ("Stagflation", "A supply shock could shift the curve up, giving higher inflation at the same level of unemployment."),
   ("Evaluate", "However, the natural rate is hard to measure, so the position of the long-run curve is uncertain.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["evaluate"]]) + FC

js = '''
/* ---------- Traditional Phillips curve ---------- */
const PX = (u) => 70 + u * 62, PY = (p) => 310 - p * 22;
const pc = (u, shift = 0) => 0.5 + 10 / (u - 1) + shift;
function curvePts(shift) { const pts = []; for (let u = 2; u <= 10.001; u += 0.2) { const p = pc(u, shift); if (p <= 13 && p >= 0) pts.push([PX(u), PY(p)]); } return pts; }
function tradDraw(s) {
  let o = axes(70, 310, 740, 30, "Unemployment rate (%)", "Inflation rate (%)"); [2, 4, 6, 8, 10].forEach((u) => (o += SV.text(PX(u), 326, u, "sm", { "text-anchor": "middle" })));
  [0, 4, 8, 12].forEach((p) => (o += SV.text(64, PY(p) + 4, p, "sm", { "text-anchor": "end" })));
  const hist = [[2.5, 8.0], [3.0, 5.3], [3.6, 4.2], [4.2, 3.7], [5.0, 3.1], [6.0, 2.5], [7.0, 2.1], [8.5, 1.8], [2.2, 9.5], [3.3, 4.8], [4.6, 3.3], [5.8, 2.7]];
  if (s.h > 0) hist.forEach((p) => (o += SV.circle(PX(p[0]), PY(p[1]), 4, "dot1", op(s.h))));
  o += SV.path(Lib.ptsPath(curvePts(0)), "c1", op(1 - 0.5 * s.k)); o += tag(PX(9.6), PY(pc(9.6)) - 8, "PC", "t1", 1 - 0.5 * s.k, "end");
  if (s.m > 0) [[3, "A"], [5, "B"], [8, "C"]].forEach(([u, l]) => (o += SV.circle(PX(u), PY(pc(u)), 7, "dot4", op(s.m)) + tag(PX(u) + 10, PY(pc(u)) - 8, l, "t4", s.m)));
  if (s.k > 0) { o += SV.path(Lib.ptsPath(curvePts(4)), "c2", op(s.k)) + tag(PX(9.6), PY(pc(9.6, 4)) - 8, "PC after the shift", "t2", s.k, "end") + SV.circle(PX(6), PY(pc(6, 4)), 8, "dot2", op(s.k)) + tag(PX(6) + 12, PY(pc(6, 4)) - 6, "stagflation", "t2", s.k); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 350" role="img" aria-label="Traditional Phillips curve sloping down with inflation on the vertical axis and unemployment on the horizontal axis">${tradDraw({ h: 1, k: 0, m: 0 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 350, label: "Observations on a downward sloping Phillips curve, a policy menu and a shift after supply shocks", base: { h: 0, m: 0, k: 0 }, draw: tradDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The curve.</b> Inflation is plotted against unemployment. A downward sloping curve means that lower unemployment goes with higher inflation: the Phillips curve.", s: {} },
  { cap: "<b>The evidence.</b> Observations from 1861 to the 1960s fall close to the curve. The relationship looked stable.", s: { h: 1 } },
  { cap: "<b>The policy menu.</b> A government could choose: A (low unemployment, high inflation), B (a middle position) or C (low inflation, high unemployment). There is a trade-off between objectives.", s: { h: 1, m: 1 } },
  { cap: "<b>The breakdown.</b> In the 1970s oil price shocks and rising expectations moved the whole curve up. At 6% unemployment inflation was now much higher than before: <b>stagflation</b>.", s: { h: 0.2, m: 0, k: 1 } },
] });

/* ---------- Expectations-augmented ---------- */
function expDraw(s) {
  const ua = 5, line = (p0, sh) => { const pts = []; for (let u = 1; u <= 9.001; u += 0.25) { const p = p0 + sh + 0.5 * (ua - u); if (p >= 0 && p <= 10.5) pts.push([PX(u), PY(p)]); } return pts; };
  let o = axes(70, 310, 740, 30, "Unemployment rate (%)", "Inflation rate (%)"); [1, 3, 5, 7, 9].forEach((u) => (o += SV.text(PX(u), 326, u, "sm", { "text-anchor": "middle" })));
  [0, 2, 4, 6, 8, 10].forEach((p) => (o += SV.text(64, PY(p) + 4, p, "sm", { "text-anchor": "end" })));
  o += SV.line(PX(ua), PY(0), PX(ua), PY(10.5), "c3", { "stroke-width": 3 }) + tag(PX(ua) + 6, 44, "LRPC at the natural rate", "t3");
  o += SV.path(Lib.ptsPath(line(2, 0)), "c2 dash", op(0.5)) + SV.path(Lib.ptsPath(line(s.p0, s.sh)), "c2");
  const p = s.p0 + s.sh + 0.5 * (ua - s.u);
  o += SV.circle(PX(s.u), PY(p), 8, "dot4") + tag(PX(s.u) + 12, PY(p) - 12, s.l, "t4");
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 345, label: "Stagflation from a supply shock, tight policy to cut inflation, then expectations adjusting", base: { p0: 2, sh: 0, u: 5, l: "start: 5% unemployment, 2% inflation" }, draw: expDraw, tween: 1100, dwell: 6000, steps: [
  { cap: "<b>Equilibrium.</b> Unemployment is at the natural rate of 5% and inflation is 2%, as expected. The short-run curve (dashed) passes through this point.", s: {} },
  { cap: "<b>A supply shock.</b> Oil prices jump. Costs rise and output falls, so the short-run curve shifts <b>up</b> and unemployment rises to 6.5%. Inflation rises to about 4.3%: <b>stagflation</b>.", s: { sh: 3, u: 6.5, l: "stagflation: 6.5% unemployment, 4.3% inflation" } },
  { cap: "<b>Tight policy.</b> The central bank raises interest rates to cut inflation. The economy moves <b>down</b> the short-run curve: unemployment rises to 8% and inflation falls to 3.5%. This is the cost of disinflation.", s: { sh: 3, u: 8, l: "tight policy: 8% unemployment, 3.5% inflation" } },
  { cap: "<b>Expectations fall.</b> The shock has passed and, as workers see lower inflation, expected inflation falls. The short-run curve shifts down and inflation at 8% unemployment is only 0.5%.", s: { sh: 0, u: 8, l: "expectations fall: 8% unemployment, 0.5% inflation" } },
  { cap: "<b>Recovery.</b> Demand is eased back and unemployment returns to the natural rate of 5% with inflation of 2%, but only after years of high unemployment. A credible central bank can shorten this period.", s: { sh: 0, u: 5, l: "back to the natural rate and 2% inflation" } },
] });

/* ---------- Lab 1 ---------- */
function labPC() {
  if (!$("#pe") || !$("#pn") || !$("#pa") || !$("#pu")) return;
  const pe = +$("#pe").value / 10, nru = +$("#pn").value / 10, a = +$("#pa").value / 10, u = +$("#pu").value / 10, p = pe + a * (nru - u);
  $("#r1").textContent = Lib.fmtN(p, 1) + "%"; $("#r2").textContent = (u - nru >= 0 ? "+" : "") + Lib.fmtN(u - nru, 1) + " pts"; $("#r3").textContent = Lib.fmtN(pe, 1) + "% (at the natural rate)";
  $("#rv").textContent = Math.abs(u - nru) < 0.05 ? "Unemployment is at the natural rate, so inflation equals expected inflation." : u < nru ? `Unemployment ${Lib.fmtN(nru - u, 1)} points below the natural rate pushes inflation to ${Lib.fmtN(p, 1)}%, ${Lib.fmtN(p - pe, 1)} points above expectations. If this is kept up, expectations rise and the short-run curve shifts up: inflation accelerates.` : `Unemployment ${Lib.fmtN(u - nru, 1)} points above the natural rate pulls inflation to ${Lib.fmtN(p, 1)}%, below expectations. If this lasts, expectations fall and the curve shifts down (disinflation).`;
  const X = (v) => 40 + v * 33, Y = (v) => 270 - v * 20, sh = (v) => pe + a * (nru - v);
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Unemployment (%)", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Inflation (%)", "sm");
  o += SV.line(X(nru), Y(0), X(nru), Y(12), "c3", { "stroke-width": 3 }) + tag(X(nru) + 4, 34, "LRPC", "t3");
  const pts = []; for (let v = 1; v <= 10.001; v += 0.25) { const q = sh(v); if (q >= 0 && q <= 12) pts.push([X(v), Y(q)]); } o += SV.path(Lib.ptsPath(pts), "c2");
  o += SV.circle(X(u), Y(Math.max(0, Math.min(12, p))), 7, "dot4") + SV.circle(X(nru), Y(pe), 5, "dot1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pe", label: "Expected inflation (%) ", min: 0, max: 80, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPC });
Lib.slider($("#g2"), { id: "pn", label: "Natural rate of unemployment (%) ", min: 30, max: 80, step: 5, value: 50, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPC });
Lib.slider($("#g3"), { id: "pa", label: "Sensitivity of inflation to unemployment ", min: 2, max: 10, step: 1, value: 5, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPC });
Lib.slider($("#g4"), { id: "pu", label: "Unemployment (%) ", min: 20, max: 90, step: 5, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labPC });
labPC();

/* ---------- Lab 2 ---------- */
function labSac() {
  if (!$("#sc") || !$("#sr") || !$("#su")) return;
  const cut = +$("#sc").value, sr = +$("#sr").value / 10, ex = +$("#su").value / 10, total = cut * sr, yrs = total / ex, lost = total * 2;
  $("#t1").textContent = Lib.fmtN(total, 1) + " point-years"; $("#t2").textContent = Lib.fmtN(yrs, 1) + " years"; $("#t3").textContent = Lib.fmtN(lost, 0) + "% of one year's GDP";
  $("#tv").textContent = `Cutting inflation by ${cut} points with a sacrifice ratio of ${Lib.fmtN(sr, 1)} needs ${Lib.fmtN(total, 1)} point-years of unemployment above the natural rate. Holding unemployment ${Lib.fmtN(ex, 1)} points above the natural rate it takes about ${Lib.fmtN(yrs, 1)} years. With Okun's law (2% of output per point), the lost output is about ${Lib.fmtN(lost, 0)}% of a year's GDP. A credible central bank may lower the sacrifice ratio.`;
  const n = Math.max(2, Math.min(12, Math.ceil(yrs))), X = (t) => 50 + t * 330 / n, Y = (v) => 260 - v * 18; let o = SV.line(40, 260, 400, 260) + SV.line(40, 260, 40, 30) + SV.text(400, 282, "Years", "sm", { "text-anchor": "end" }); const pts = []; for (let t = 0; t <= n; t++) pts.push([X(t), Y(Math.max(2, 2 + cut - cut * t / yrs))]);
  o += SV.path(Lib.ptsPath(pts), "c2") + SV.line(40, Y(2), 400, Y(2), "c3 dash") + tag(396, Y(2) - 6, "target 2%", "t3", 1, "end") + tag(60, Y(2 + cut) - 8, "inflation " + (2 + cut) + "%", "t2");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "sc", label: "Inflation to remove (points) ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labSac });
Lib.slider($("#g6"), { id: "sr", label: "Sacrifice ratio ", min: 10, max: 50, step: 5, value: 25, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labSac });
Lib.slider($("#g7"), { id: "su", label: "Unemployment above the natural rate (points) ", min: 5, max: 40, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labSac });
labSac();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens on the diagram?", ["Movement along the SRPC", "Shift of the SRPC up", "Shift of the SRPC down", "Shift of the LRPC left"],
  [("Demand stimulus lowers unemployment and raises inflation", 0), ("Expected inflation rises", 1), ("A credible central bank lowers inflation expectations", 2), ("Retraining lowers the natural rate", 3), ("An oil price rise raises costs", 1), ("Tight policy raises unemployment and cuts inflation", 0), ("Better job-matching services cut frictional unemployment", 3), ("Wage demands fall as inflation is expected to be lower", 2)],
  "Along the curve: demand changes. Shifts: expectations or supply. LRPC shifts: the natural rate changes.") + MATCH([
  ["Traditional Phillips curve", "An inverse relationship between unemployment and inflation"],
  ["Stagflation", "High inflation together with high unemployment"],
  ["Expectations-augmented Phillips curve", "A short-run curve that shifts when expected inflation changes"],
  ["Long-run Phillips curve", "A vertical line at the natural rate of unemployment"],
  ["Accelerationist hypothesis", "Unemployment below the natural rate needs ever-rising inflation"],
  ["Sacrifice ratio", "Point-years of extra unemployment per point of inflation removed"]]) + ORDER(
  "Put the monetarist argument about holding unemployment below the natural rate in order.",
  ["The government stimulates demand to cut unemployment below the natural rate", "Inflation rises above workers' expectations and real wages fall", "Firms hire and unemployment falls temporarily", "Workers raise expectations and wage demands", "Unemployment returns to the natural rate with higher inflation"],
  "The gain is temporary and the cost is higher inflation.") + CALC([
  {"q": "Expected inflation is 3%, the natural rate is 5% and each point of unemployment below the natural rate adds 0.5 points to inflation. Calculate inflation if unemployment is 3%.", "a": 4, "unit": "%", "tol": 0.05, "hint": "3 + 0.5 × 2.", "sol": "3 + 0.5 × 2 = <b>4%</b>."},
  {"q": "In the previous question, workers now expect inflation of 4%. Calculate inflation if unemployment is held at 3%.", "a": 5, "unit": "%", "tol": 0.05, "hint": "4 + 0.5 × 2.", "sol": "4 + 1 = <b>5%</b>: inflation has accelerated."},
  {"q": "A government wants to cut inflation by 4 points. The sacrifice ratio is 2.5 point-years of unemployment above the natural rate per point of inflation removed. Calculate the total point-years of extra unemployment.", "a": 10, "tol": 0.05, "hint": "4 × 2.5.", "sol": "4 × 2.5 = <b>10 point-years</b>."},
  {"q": "Unemployment rises from 5% to 7% and inflation falls from 4% to 2.5%. Calculate the change in inflation per percentage point rise in unemployment (use a minus sign).", "a": -0.75, "tol": 0.01, "hint": "Change in inflation ÷ change in unemployment.", "sol": "−1.5 ÷ 2 = <b>−0.75</b>."}]) + MCQ([
  ("What does the long-run Phillips curve show?", ["A trade-off between inflation and unemployment", "Unemployment at the natural rate whatever the rate of inflation", "Rising inflation as unemployment rises", "A fixed inflation rate"], 1, "In the long run there is no trade-off: the curve is vertical at the natural rate."),
  ("A rise in expected inflation causes:", ["A movement down the SRPC", "A shift up of the SRPC", "A shift left of the LRPC", "No change"], 1, "Workers bargain for higher wages whatever the unemployment rate, shifting the SRPC up."),
  ("Stagflation is best described as:", ["Low inflation and low unemployment", "High inflation and high unemployment", "Falling prices and rising output", "Rising output and low inflation"], 1, "Stagflation combines high inflation with stagnant output and high unemployment."),
  ("Which policy shifts the long-run Phillips curve to the left?", ["A cut in interest rates", "Retraining and better job information", "An increase in government spending", "A rise in the minimum wage"], 1, "Supply-side policies lower the natural rate of unemployment."),
  ("What cost does disinflation have in the expectations-augmented model?", ["Unemployment above the natural rate for some time", "Permanently higher inflation", "A permanently lower natural rate", "No cost"], 0, "To lower expectations the economy must move down the SRPC.")
], "qz1") + CARDS([
  ("Phillips curve", "Inverse relationship between inflation and unemployment."),
  ("Stagflation", "High inflation with high unemployment."),
  ("SRPC", "Short-run Phillips curve, for a given level of expected inflation."),
  ("LRPC", "Long-run Phillips curve, vertical at the natural rate."),
  ("Accelerationist", "Below-natural unemployment means accelerating inflation."),
  ("Adaptive expectations", "Expected inflation based on past inflation."),
  ("Sacrifice ratio", "Cost in point-years of unemployment of cutting inflation by one point."),
  ("NAIRU", "Unemployment at which inflation is stable.")]) + MCQ(mc_exam)

build("sy1025", "phillips-curve", "Inflation and Unemployment: the Phillips Curve", EY,
  "10.2.5: the traditional Phillips curve, stagflation, the expectations-augmented short-run and long-run Phillips curves, and the policy implications. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
