const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.slice(1).map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

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
Lib.classify($("#cl1"), { prompt: "Would the change raise or lower the natural rate of unemployment?", buckets: [{"label": "Raises it"}, {"label": "Lowers it"}], items: [{"text": "Unemployment benefits become more generous and last longer", "b": 0}, {"text": "Free retraining for workers in declining industries", "b": 1}, {"text": "A national job-vacancy website is launched", "b": 1}, {"text": "Trade unions win a large rise in wages above the market rate", "b": 0}, {"text": "Housing becomes cheaper in areas with vacancies", "b": 1}, {"text": "A long recession leaves many workers with outdated skills", "b": 0}, {"text": "Hiring and firing rules become much stricter", "b": 0}, {"text": "Support for workers to move to new regions", "b": 1}], done: "Anything that improves matching of workers to jobs lowers the natural rate." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Natural rate", "Unemployment when the labour market is in equilibrium"], ["NAIRU", "Unemployment rate at which inflation does not accelerate"], ["LRPC", "Vertical long-run Phillips curve at the natural rate"], ["Replacement ratio", "Benefit income as a share of previous earnings"], ["Structural unemployment", "Mismatch of skills or location with the jobs available"], ["Frictional unemployment", "Time spent searching between jobs"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the monetarist argument about demand stimulus in order.", items: ["The government expands demand to cut unemployment below the natural rate", "Prices rise faster than workers expected and real wages fall", "Firms hire more and unemployment falls temporarily", "Workers revise their expectations and demand higher wages", "Unemployment returns to the natural rate with higher inflation"], done: "Without a change in the natural rate, demand policy only buys a temporary fall in unemployment." });
Lib.calc($("#c1"), { qs: [
  {"q": "In an economy frictional unemployment is 1.5%, structural 2.5% and seasonal 0.5% of the labour force. Calculate the natural rate of unemployment (%).", "a": 4.5, "unit": "%", "tol": 0.05, "hint": "Add the three types.", "sol": "1.5 + 2.5 + 0.5 = <b>4.5%</b>."},
  {"q": "Actual unemployment is 7.5% and the natural rate is 4.5%. What percentage of the labour force is cyclically unemployed?", "a": 3, "unit": "%", "tol": 0.05, "hint": "Actual minus natural.", "sol": "7.5 − 4.5 = <b>3%</b>."},
  {"q": "Expected inflation is 3%. Each percentage point of unemployment below the natural rate (5%) adds 1.5 points to inflation. Calculate inflation if unemployment is held at 3.5%.", "a": 5.25, "unit": "%", "tol": 0.05, "hint": "Gap = 1.5 points. Add 1.5 × 1.5 to 3.", "sol": "3 + 1.5 × 1.5 = <b>5.25%</b>."},
  {"q": "The replacement ratio is the benefit received divided by previous earnings. A worker earned $2,000 a month and receives $1,300 in benefits. Calculate the replacement ratio (%).", "a": 65, "unit": "%", "tol": 0.05, "hint": "1300 ÷ 2000.", "sol": "1300 ÷ 2000 × 100 = <b>65%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does the natural rate of unemployment include?", opts: ["Cyclical unemployment only", "Frictional, structural and seasonal unemployment", "Real wage unemployment only", "All unemployment"], a: 1, why: "It is the unemployment that remains when the labour market is in equilibrium." },
  { q: "According to monetarists, what is the long-run effect of a demand stimulus that cuts unemployment below the natural rate?", opts: ["Permanently lower unemployment", "Higher inflation with unemployment back at the natural rate", "Lower inflation", "No effect on prices"], a: 1, why: "Expectations adjust, so the gain in jobs disappears and inflation is higher." },
  { q: "Which policy would most directly lower the natural rate?", opts: ["A cut in interest rates", "Retraining for workers in declining industries", "Higher government spending on defence", "A rise in the minimum wage"], a: 1, why: "Retraining lowers structural unemployment." },
  { q: "Which statement is a Keynesian criticism of the natural rate theory?", opts: ["The natural rate is fixed forever", "Hysteresis means the natural rate can be raised by recessions", "Demand has no effect on unemployment", "Inflation never changes"], a: 1, why: "Long recessions can leave the unemployed with outdated skills and raise the equilibrium rate." },
  { q: "The natural rate is also known as the:", opts: ["NAIRU", "GDP gap", "Participation rate", "Poverty line"], a: 0, why: "NAIRU is the non-accelerating inflation rate of unemployment, used as another name for the natural rate." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Natural rate of unemployment", "Unemployment at labour market equilibrium: frictional, structural, seasonal."],
  ["NAIRU", "Rate of unemployment at which inflation neither accelerates nor decelerates."],
  ["Long-run Phillips curve", "Vertical at the natural rate."],
  ["Replacement ratio", "Benefits as a share of previous earnings."],
  ["Expectations", "Beliefs about future inflation that affect wage bargaining."],
  ["Supply-side policy", "Policy that raises capacity and lowers the natural rate."],
  ["Hysteresis", "A recession can raise the natural rate through lost skills."],
  ["Insider-outsider", "Employed insiders keep wages high at the expense of unemployed outsiders."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The natural rate of unemployment is 5%. What will happen if the government keeps trying to hold unemployment at 3% using expansionary monetary policy? (Feb/March 2021 · 32 · Q29, reworded)", opts: ["An accelerating rate of inflation", "A falling rate of inflation", "A high but constant rate of inflation", "A negative rate of inflation"], a: 0, why: "Below the natural rate, expectations adjust and inflation keeps accelerating." },
  { q: "An economy is at its natural rate of unemployment. When would extra government spending aimed at cutting unemployment most conflict with low inflation? (May/June 2025 · 31 · Q23, reworded)", opts: ["If inflationary expectations are unchanged", "If inflationary expectations fall", "If labour productivity rises", "If labour supply rises"], a: 0, why: "At the natural rate, extra demand mainly raises prices, and it is worst when expectations do not adjust." },
  { q: "Why might country X have a higher natural rate of unemployment than country Y? (Feb/March 2024 · 32 · Q18, reworded)", opts: ["A higher level of trade unionisation in X", "More training and education in X", "Greater incentives to find work in X", "More job vacancy information in X"], a: 0, why: "Strong unions push wages above equilibrium and protect insiders, raising the natural rate." },
  { q: "What is least likely to increase the natural rate of unemployment? (May/June 2025 · 34 · Q17, reworded)", opts: ["Less information about vacancies", "Weaker trade union power", "Higher unemployment benefits", "Higher immigration"], a: 1, why: "Weaker unions reduce wage pressure. The other options all lengthen search or raise the supply of job seekers relative to vacancies." },
  { q: "Which increase is most likely to reduce the natural rate of unemployment? (Oct/Nov 2024 · 31 · Q18, reworded)", opts: ["The level of unemployment benefit", "The militancy of trade unions", "The national minimum wage", "Participation on training courses"], a: 3, why: "Training reduces skills mismatch and so structural unemployment." },
  { q: "When is the natural rate of unemployment most likely to fall? (Oct/Nov 2024 · 32 · Q17, reworded)", opts: ["When education levels decline", "When income tax rates rise", "When labour mobility increases", "When state unemployment benefits rise"], a: 2, why: "Greater mobility matches workers to vacancies faster." },
  { q: "Which policy is most likely to reduce the natural rate of unemployment? (Oct/Nov 2020 · 33 · Q30, reworded)", opts: ["More government spending on goods and services", "More spending on training schemes to fix skill shortages", "A longer period of eligibility for welfare benefits", "A higher minimum wage"], a: 1, why: "Training addresses the structural part of the natural rate. The other options raise demand or raise the wage floor." },
  { q: "What is most likely to result from a fall in the natural rate of unemployment? (May/June 2024 · 31 · Q17, reworded)", opts: ["A fall in government spending on goods and services", "A fall in payments to the unemployed", "A fall in trade union membership", "A fall in interest rates"], a: 1, why: "Fewer people unemployed in equilibrium means lower benefit payments." },
] });
