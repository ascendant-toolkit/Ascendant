const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

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
Lib.classify($("#cl1"), { prompt: "What happens on the diagram?", buckets: [{"label": "Movement along the SRPC"}, {"label": "Shift of the SRPC up"}, {"label": "Shift of the SRPC down"}, {"label": "Shift of the LRPC left"}], items: [{"text": "Demand stimulus lowers unemployment and raises inflation", "b": 0}, {"text": "Expected inflation rises", "b": 1}, {"text": "A credible central bank lowers inflation expectations", "b": 2}, {"text": "Retraining lowers the natural rate", "b": 3}, {"text": "An oil price rise raises costs", "b": 1}, {"text": "Tight policy raises unemployment and cuts inflation", "b": 0}, {"text": "Better job-matching services cut frictional unemployment", "b": 3}, {"text": "Wage demands fall as inflation is expected to be lower", "b": 2}], done: "Along the curve: demand changes. Shifts: expectations or supply. LRPC shifts: the natural rate changes." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Traditional Phillips curve", "An inverse relationship between unemployment and inflation"], ["Stagflation", "High inflation together with high unemployment"], ["Expectations-augmented Phillips curve", "A short-run curve that shifts when expected inflation changes"], ["Long-run Phillips curve", "A vertical line at the natural rate of unemployment"], ["Accelerationist hypothesis", "Unemployment below the natural rate needs ever-rising inflation"], ["Sacrifice ratio", "Point-years of extra unemployment per point of inflation removed"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the monetarist argument about holding unemployment below the natural rate in order.", items: ["The government stimulates demand to cut unemployment below the natural rate", "Inflation rises above workers' expectations and real wages fall", "Firms hire and unemployment falls temporarily", "Workers raise expectations and wage demands", "Unemployment returns to the natural rate with higher inflation"], done: "The gain is temporary and the cost is higher inflation." });
Lib.calc($("#c1"), { qs: [
  {"q": "Expected inflation is 3%, the natural rate is 5% and each point of unemployment below the natural rate adds 0.5 points to inflation. Calculate inflation if unemployment is 3%.", "a": 4, "unit": "%", "tol": 0.05, "hint": "3 + 0.5 × 2.", "sol": "3 + 0.5 × 2 = <b>4%</b>."},
  {"q": "In the previous question, workers now expect inflation of 4%. Calculate inflation if unemployment is held at 3%.", "a": 5, "unit": "%", "tol": 0.05, "hint": "4 + 0.5 × 2.", "sol": "4 + 1 = <b>5%</b>: inflation has accelerated."},
  {"q": "A government wants to cut inflation by 4 points. The sacrifice ratio is 2.5 point-years of unemployment above the natural rate per point of inflation removed. Calculate the total point-years of extra unemployment.", "a": 10, "tol": 0.05, "hint": "4 × 2.5.", "sol": "4 × 2.5 = <b>10 point-years</b>."},
  {"q": "Unemployment rises from 5% to 7% and inflation falls from 4% to 2.5%. Calculate the change in inflation per percentage point rise in unemployment (use a minus sign).", "a": -0.75, "tol": 0.01, "hint": "Change in inflation ÷ change in unemployment.", "sol": "−1.5 ÷ 2 = <b>−0.75</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does the long-run Phillips curve show?", opts: ["A trade-off between inflation and unemployment", "Unemployment at the natural rate whatever the rate of inflation", "Rising inflation as unemployment rises", "A fixed inflation rate"], a: 1, why: "In the long run there is no trade-off: the curve is vertical at the natural rate." },
  { q: "A rise in expected inflation causes:", opts: ["A movement down the SRPC", "A shift up of the SRPC", "A shift left of the LRPC", "No change"], a: 1, why: "Workers bargain for higher wages whatever the unemployment rate, shifting the SRPC up." },
  { q: "Stagflation is best described as:", opts: ["Low inflation and low unemployment", "High inflation and high unemployment", "Falling prices and rising output", "Rising output and low inflation"], a: 1, why: "Stagflation combines high inflation with stagnant output and high unemployment." },
  { q: "Which policy shifts the long-run Phillips curve to the left?", opts: ["A cut in interest rates", "Retraining and better job information", "An increase in government spending", "A rise in the minimum wage"], a: 1, why: "Supply-side policies lower the natural rate of unemployment." },
  { q: "What cost does disinflation have in the expectations-augmented model?", opts: ["Unemployment above the natural rate for some time", "Permanently higher inflation", "A permanently lower natural rate", "No cost"], a: 0, why: "To lower expectations the economy must move down the SRPC." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Phillips curve", "Inverse relationship between inflation and unemployment."],
  ["Stagflation", "High inflation with high unemployment."],
  ["SRPC", "Short-run Phillips curve, for a given level of expected inflation."],
  ["LRPC", "Long-run Phillips curve, vertical at the natural rate."],
  ["Accelerationist", "Below-natural unemployment means accelerating inflation."],
  ["Adaptive expectations", "Expected inflation based on past inflation."],
  ["Sacrifice ratio", "Cost in point-years of unemployment of cutting inflation by one point."],
  ["NAIRU", "Unemployment at which inflation is stable."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Why is it likely that a curve showing the relationship between unemployment and inflation only applies in the short run? (Oct/Nov 2024 · 33 · Q21, reworded)", opts: ["Any attempt to reduce unemployment will increase inflation", "Increased inflation actually increases unemployment", "Increased inflation leads to expectations of further inflation", "Increased inflation reduces real wages, which increases the demand for labour"], a: 2, why: "In the long run workers expect higher inflation and bargain for higher wages, so the trade-off disappears." },
  { q: "An economy uses expansionary monetary policy to boost employment, and the consumer price index rises at an accelerating rate. Which curve could represent this? (Oct/Nov 2022 · 31 · Q28, reworded)", opts: ["Kuznets curve", "Laffer curve", "Lorenz curve", "Phillips curve"], a: 3, why: "A Phillips curve shows the link between inflation and unemployment." },
  { q: "What are the labels on the axes of a Phillips curve diagram? (Oct/Nov 2022 · 32 · Q30, reworded)", opts: ["Vertical: inflation rate, horizontal: unemployment level", "Vertical: inflation rate, horizontal: unemployment rate", "Vertical: price level, horizontal: unemployment level", "Vertical: price level, horizontal: unemployment rate"], a: 1, why: "The Phillips curve plots the rate of inflation against the rate of unemployment." },
  { q: "What is measured on the vertical axis of the Phillips curve? (Oct/Nov 2023 · 33 · Q22, reworded)", opts: ["The rate of change of real wages", "The rate of change of take-home pay", "The rate of inflation", "The rate of interest"], a: 2, why: "The traditional curve has inflation (or wage inflation) on the vertical axis." },
  { q: "A table gives year, unemployment rate and inflation rate: year 1 (7.6, 2.6), year 2 (6.2, 1.6), year 3 (5.8, 1.8), year 4 (5.9, 2.0), year 5 (5.8, 2.0). Which change between consecutive years agrees with the Phillips curve? (May/June 2025 · 34 · Q23, reworded)", opts: ["Year 1 to year 2", "Year 2 to year 3", "Year 3 to year 4", "Year 4 to year 5"], a: 1, why: "From year 2 to year 3 unemployment fell and inflation rose: the inverse relationship." },
  { q: "Unemployment and inflation (2010, 2014): Australia 5.2, 6.1 and 2.7, 1.6; Canada 8.0, 6.9 and 2.2, 1.9; Japan 5.1, 3.6 and −0.3, 2.5; US 9.6, 6.2 and 1.7, 0.6. Which countries had a typical Phillips curve? (Oct/Nov 2023 · 31 · Q26, reworded)", opts: ["Australia and Japan", "Australia only", "Japan only", "Canada and the United States"], a: 0, why: "A typical Phillips curve shows unemployment and inflation moving in opposite directions: Australia (up, down) and Japan (down, up)." },
  { q: "Inflation and unemployment in 2008 and 2011: Canada 2.38, 2.89 and 6.15, 7.47; France 3.16, 2.29 and 7.81, 9.68; Germany 2.75, 2.48 and 7.60, 5.98; Japan 1.37, −0.28 and 3.99, 4.55. Which experienced a trade-off between inflation and unemployment? (Oct/Nov 2023 · 32 · Q21, reworded)", opts: ["Canada and Germany", "Canada only", "France and Japan", "France only"], a: 2, why: "In France and Japan inflation fell while unemployment rose. In Canada both rose and in Germany both fell." },
  { q: "An economy is at its natural rate. When will an increase in government spending to reduce unemployment most conflict with low inflation? (May/June 2025 · 31 · Q23, reworded)", opts: ["If inflationary expectations are unchanged", "If inflationary expectations fall", "If labour productivity rises", "If labour supply rises"], a: 0, why: "If workers do not expect the extra inflation, they accept the lower real wage for a time; once expectations adjust, inflation rises with no lasting fall in unemployment." },
] });
