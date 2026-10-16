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
Lib.classify($("#cl1"), { prompt: "Which type of unemployment is it?", buckets: [{"label": "Frictional"}, {"label": "Structural"}, {"label": "Cyclical"}, {"label": "Seasonal"}], items: [{"text": "A graduate searching for a job that fits their skills", "b": 0}, {"text": "A textile worker whose factory moved abroad", "b": 1}, {"text": "A shop assistant laid off in a recession", "b": 2}, {"text": "A fruit picker out of work in winter", "b": 3}, {"text": "A bank clerk replaced by online banking software", "b": 1}, {"text": "A builder between two projects", "b": 0}, {"text": "A hotel worker laid off when exports and tourism fall sharply", "b": 2}, {"text": "A beach lifeguard unemployed outside summer", "b": 3}], done: "Think about why the job was lost and how long it will last." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Full employment", "Everyone willing and able to work at the going wage can find a job"], ["Labour force", "People who are employed or actively seeking work"], ["Hysteresis", "Unemployment that stays high after its cause has gone"], ["Real wage unemployment", "Caused by a wage held above equilibrium"], ["Demand-deficient unemployment", "Caused by a fall in aggregate demand"], ["Voluntary unemployment", "Choosing not to accept jobs at the going wage"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the hysteresis chain in order.", items: ["A recession causes mass layoffs", "Many workers stay unemployed for a long time", "Their skills and contacts fade and employers see them as less employable", "Demand recovers but vacancies cannot be filled from the unemployed", "The natural rate of unemployment is higher than before"], done: "Long-term unemployment turns a cyclical problem into a structural one." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country has 18 million employed, 1.2 million unemployed and 9 million economically inactive. Calculate the unemployment rate (to one decimal place).", "a": 6.3, "unit": "%", "tol": 0.1, "hint": "Labour force = employed + unemployed.", "sol": "Labour force = 19.2m. Rate = 1.2 ÷ 19.2 × 100 = <b>6.3%</b>."},
  {"q": "The working-age population is 30 million; 19 million are employed. Calculate the employment rate (to one decimal place).", "a": 63.3, "unit": "%", "tol": 0.1, "hint": "Employed ÷ working-age population.", "sol": "19 ÷ 30 × 100 = <b>63.3%</b>."},
  {"q": "In a labour market, demand is L = 100 − 10W and supply is L = −20 + 10W. A minimum wage of 7 is set. Calculate the number of unemployed workers.", "a": 20, "tol": 0.01, "hint": "Find labour demanded and supplied at W = 7.", "sol": "Demand = 100 − 70 = 30. Supply = −20 + 70 = 50. Unemployed = <b>20</b>."},
  {"q": "The labour force is 25 million and the unemployment rate is 8%. Next year 500,000 of the unemployed find jobs and the labour force stays the same. Calculate the new unemployment rate (%).", "a": 6, "unit": "%", "tol": 0.05, "hint": "Unemployed now = 2m.", "sol": "Unemployed = 2m − 0.5m = 1.5m. 1.5 ÷ 25 × 100 = <b>6%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is true at full employment?", opts: ["There is no unemployment of any kind", "Everyone willing and able to work at the going wage has a job", "The government budget is balanced", "Inflation is zero"], a: 1, why: "Full employment allows for frictional and structural unemployment." },
  { q: "A minimum wage set above the equilibrium wage is most likely to cause:", opts: ["Demand-deficient unemployment", "Real wage unemployment", "Frictional unemployment", "Seasonal unemployment"], a: 1, why: "A wage above equilibrium means labour supplied exceeds labour demanded: real wage unemployment." },
  { q: "Which is an example of equilibrium unemployment?", opts: ["Unemployment in a deep recession", "Unemployment caused by a wage floor", "Workers between jobs searching for vacancies", "Unemployment from a collapse in exports"], a: 2, why: "Frictional unemployment exists even when the labour market clears." },
  { q: "What is a cause of hysteresis?", opts: ["A rise in aggregate demand", "Loss of skills during long spells of unemployment", "A fall in the minimum wage", "A rise in labour mobility"], a: 1, why: "Skills decay, stigma and discouragement make long-term unemployment persistent." },
  { q: "Who is in the labour force?", opts: ["Full-time students", "Retired people", "People actively seeking work", "People who have given up looking for work"], a: 2, why: "The labour force is the employed plus those actively seeking work." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Full employment", "Everyone willing and able to work at the going wage can find a job."],
  ["Labour force", "Employed plus unemployed (actively seeking work)."],
  ["Equilibrium unemployment", "Exists even when the labour market is in balance: frictional, structural, seasonal."],
  ["Disequilibrium unemployment", "Labour market out of balance: real wage and demand-deficient."],
  ["Voluntary unemployment", "Not accepting jobs at the going wage."],
  ["Involuntary unemployment", "Willing to work at the going wage but cannot find a job."],
  ["Real wage unemployment", "Wage held above the equilibrium by a minimum wage or union power."],
  ["Hysteresis", "Unemployment stays high after the cause has gone."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is a definition of hysteresis unemployment? (May/June 2025 · 31 · Q16, reworded)", opts: ["Workers who are briefly unemployed while moving between jobs", "Workers who lose jobs in a recession but find work when the economy recovers", "Workers who stay unemployed for a long time and lose job skills and work experience", "Workers who lose jobs when firms close and new firms use new technology"], a: 2, why: "Hysteresis is long-lasting unemployment caused by loss of skills and work experience, which stops it falling back after a recession." },
  { q: "A government cuts interest rates to reduce unemployment but finds this has little effect because of hysteresis. What causes the hysteresis? (May/June 2025 · 32 · Q20, reworded)", opts: ["More capital investment", "Fewer people save", "The skills of unemployed workers become outdated", "The money supply rises"], a: 2, why: "Out-of-date skills mean the unemployed cannot fill vacancies even when demand recovers." },
  { q: "Which type of unemployment is associated with a deficiency in aggregate demand? (May/June 2022 · 31 · Q21, reworded)", opts: ["Cyclical", "Frictional", "Structural", "Voluntary"], a: 0, why: "Cyclical or demand-deficient unemployment arises when AD is too low." },
  { q: "Which term describes short-term unemployment when people are changing jobs? (Feb/March 2022 · 32 · Q22, reworded)", opts: ["Cyclical", "Frictional", "Seasonal", "Voluntary"], a: 1, why: "Frictional unemployment is the time spent searching between jobs." },
  { q: "Which statement about unemployment is correct? (Oct/Nov 2022 · 31 · Q21, reworded)", opts: ["Cyclical unemployment is caused by occupational immobility", "Frictional unemployment is caused by a lack of information on jobs", "Structural unemployment is caused by a deficiency in aggregate demand", "Voluntary unemployment is caused by seasonal variations in demand"], a: 1, why: "Poor information about vacancies lengthens the search period. The other statements swap the causes." },
  { q: "'If you pay people not to work, and tax them when they do, don't be surprised if you get unemployment.' What type is this? (May/June 2022 · 32 · Q22, reworded)", opts: ["Cyclical", "Frictional", "Structural", "Voluntary"], a: 3, why: "Benefit and tax incentives make people choose not to take work: voluntary unemployment." },
  { q: "Which citizen is not structurally unemployed? (May/June 2023 · 31 · Q19, reworded)", opts: ["A coal miner whose power stations are closing and is unwilling to retrain", "A cafe worker who lost the job when town-centre trade fell after a pandemic", "A worker who cannot move with a firm that relocated", "A skilled person who is taking time to choose among job offers"], a: 3, why: "Choosing between offers is frictional search. The others involve a lasting mismatch of skills, location or demand." },
  { q: "The table shows a country's population data: total population 2,000,000; labour force 1,200,000; employed 900,000; unemployed 300,000. What is the unemployment rate? (Oct/Nov 2024 · 31 · Q20, reworded)", opts: ["25%", "33%", "60%", "75%"], a: 0, why: "Unemployment rate = unemployed ÷ labour force = 300,000 ÷ 1,200,000 = 25%." },
] });
