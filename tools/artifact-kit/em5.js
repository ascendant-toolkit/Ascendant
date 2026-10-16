const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

Lib.stepper($("#stD"), { w: 760, h: 400, label: "Demand-side policy and cyclical unemployment", base: { sh: -16, a: 0 }, draw: adasChart, steps: [
  { cap: "After a recession AD has shifted <b>left</b> and cyclical unemployment is high.", s: { sh: -16, a: 0 } },
  { cap: "The government and central bank use <b>expansionary policy</b>: lower interest rates, more spending, lower taxes. <b>AD shifts back to the right</b>.", s: { sh: 0, a: 0 } },
  { cap: "Real GDP rises. Firms need more workers, so <b>cyclical unemployment falls</b>.", s: { sh: 14, a: 0 } },
  { cap: "<b>Evaluate:</b> push too far and AD runs into capacity limits: <b>inflation</b>. It does little for structural unemployment, where workers' skills do not match vacancies.", s: { sh: 40, a: 0 } },
] });
const STP = ["The government funds retraining and relocation help", "Workers gain new skills and can move to where jobs are", "The mismatch between workers and vacancies narrows", "Firms can fill vacancies: employment rises", "Structural unemployment falls", "Evaluation: slow, costly, and the skills must match the jobs"];
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Supply-side policy and structural unemployment", base: { n: 0 }, draw: mkChain(STP, "--good"), steps: chainSteps(["The government funds <b>retraining and relocation help</b>.", "Workers gain <b>new skills</b> and can move to where the jobs are.", "The <b>mismatch</b> between workers and vacancies narrows.", "Firms can <b>fill vacancies</b>: employment rises.", "<b>Structural unemployment</b> falls.", "<b>Evaluate:</b> it takes years, costs money, and only works if the skills taught match what firms want."]) });

/* Lab 1: which policy for which type */
const TYPES = ["Frictional", "Structural", "Cyclical", "Seasonal"], POLS = ["Expansionary fiscal or monetary policy", "Training and retraining", "Job information and matching", "Cutting benefits (labour market reform)", "Regional policy and help to move"];
const RATE = [[1, 1, 3, 0], [1, 3, 1, 1], [3, 2, 1, 1], [2, 2, 0, 1], [1, 3, 1, 1]];
const NOTE = [["Cheaper borrowing and more spending raise demand for workers, but this does not teach skills or stop people changing jobs.", "Better skills are not the cause of unemployment in a slump; demand is.", "Raises AD, so firms hire again: the standard cure for cyclical unemployment.", "Seasonal jobs depend on the calendar, not total demand."], ["A little help, if the person lacks skills, but they are mainly between jobs.", "Directly tackles the skills mismatch: the best tool.", "Skills are not the main problem in a slump.", "Some value if workers retrain for work in the off-season."], ["Faster matching is exactly what reduces time between jobs.", "Helps workers find the vacancies that suit their skills.", "Vacancies are not available, so information does not create jobs.", "Helps people find temporary work in the off-season."], ["Lower benefits speed up job search.", "May push people into any job but does not fix a skills mismatch.", "Cutting benefits could reduce demand and make a recession worse.", "Some effect, but does not change the seasonal pattern."], ["Helps a little by moving jobs and workers closer.", "Brings jobs to depressed regions or helps workers move: tackles geographical immobility.", "Little help in a general downturn.", "May help diversify the local economy."]];
const RL = ["Little effect", "Some help", "Moderate help", "Very effective"];
let selT = 1, selP = 1;
function showMatrix() {
  $("#mxT").innerHTML = TYPES.map((t, j) => `<button class="b${j === selT ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $("#mxP").innerHTML = POLS.map((t, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $$("#mxT .b").forEach((b) => (b.onclick = () => { selT = +b.dataset.j; showMatrix(); }));
  $$("#mxP .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; showMatrix(); }));
  const r = RATE[selP][selT];
  $("#mxOut").innerHTML = `<div class="verdict"><b>${POLS[selP]}</b> for <b>${TYPES[selT].toLowerCase()}</b> unemployment: <b>${RL[r]}</b>. ${NOTE[selP][selT]}</div>`;
}
showMatrix();
const PP = [
  { n: "Expansionary fiscal policy", w: "Raises AD through G and tax cuts.", sp: "Medium", c: "Deficit; inflation near capacity; weak against structural unemployment." },
  { n: "Cut interest rates", w: "Cheaper borrowing raises C and I.", sp: "Months to a year", c: "Weak if confidence is low; may raise inflation." },
  { n: "Education and training", w: "Skills and mobility rise, filling vacancies.", sp: "Slow (years)", c: "Costly; skills must match jobs." },
  { n: "Cut unemployment benefit", w: "Raises the incentive to look for work.", sp: "Medium", c: "Hurts the poor; may cut demand; may not create jobs." },
  { n: "Minimum wage", w: "Raises incomes of low-paid workers.", sp: "Immediate", c: "May raise unemployment if set too high, especially for young and unskilled." },
  { n: "Tariffs", w: "Protect domestic jobs from imports.", sp: "Fast", c: "Higher prices, retaliation, fewer exports; other jobs may be lost." },
  { n: "Regional subsidies", w: "Encourage firms to open in depressed areas.", sp: "Medium", c: "Costly; firms may leave when subsidy ends." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it works</th><th>Speed</th><th>The catch</th></tr><tr><td>${p.w}</td><td>${p.sp}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of unemployment</b> would each policy mainly help?", buckets: [{ label: "Cyclical" }, { label: "Structural" }, { label: "Frictional" }, { label: "Seasonal" }], items: [
  { text: "Cut interest rates and raise government spending", b: 0 }, { text: "Cut taxes in a recession", b: 0 },
  { text: "Retraining programmes for ex-miners", b: 1 }, { text: "Relocation grants to move to where jobs are", b: 1 },
  { text: "An online job-matching service", b: 2 }, { text: "Better information about vacancies", b: 2 },
  { text: "Diversifying a resort's economy into summer activities", b: 3 }, { text: "Training seasonal workers for off-season jobs", b: 3 },
], done: "Match the policy to the type." });
Lib.classify($("#cl2"), { prompt: "Is each policy <b>demand-side</b> or <b>supply-side</b>?", buckets: [{ label: "Demand-side" }, { label: "Supply-side" }], items: [
  { text: "Raise government spending", b: 0 }, { text: "Cut interest rates", b: 0 }, { text: "Cut income tax to raise spending", b: 0 }, { text: "Increase the money supply", b: 0 },
  { text: "Fund apprenticeships", b: 1 }, { text: "Cut unemployment benefit to raise incentives", b: 1 }, { text: "Deregulate markets so new firms can enter", b: 1 }, { text: "Build infrastructure to lower firms' costs", b: 1 },
], done: "Demand-side shifts AD; supply-side raises capacity and matching." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Expansionary fiscal policy", "Bigger deficit; inflation near full capacity"],
  ["Cutting interest rates", "May not work if confidence is low"],
  ["Education and training", "Takes years and skills may not match jobs"],
  ["Cutting unemployment benefit", "May hurt the poor and reduce demand"],
  ["Minimum wage", "May cause unemployment among low-skilled workers"],
  ["Tariffs", "Retaliation and higher prices"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a cut in interest rates could reduce cyclical unemployment</b>.", items: [
  "The central bank cuts the interest rate",
  "Borrowing is cheaper and saving less attractive",
  "Consumption and investment rise",
  "Aggregate demand shifts right",
  "Firms produce more and hire more workers",
  "Cyclical unemployment falls",
], done: "A demand-side chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A government spends $6bn on a jobs programme and the multiplier is 2. By how much does income rise ($bn)?", a: 12, sol: "2 × 6 = <b>$12bn</b>." },
  { q: "Training moves 40% of 50,000 structurally unemployed workers into jobs. How many find work?", a: 20000, sol: "40% × 50,000 = <b>20,000</b>." },
  { q: "The unemployment rate falls from 9% to 7% in a labour force of 25 million. How many fewer people are unemployed (millions)?", a: 0.5, sol: "2% × 25m = <b>0.5 million</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is most likely to reduce cyclical unemployment?", opts: ["Retraining programmes", "Expansionary fiscal and monetary policy", "Job-matching websites", "Cuts to unemployment benefit"], a: 1, why: "It raises AD and so the demand for labour." },
  { q: "Which policy is most likely to reduce structural unemployment?", opts: ["Cutting interest rates", "Education and retraining", "Raising VAT", "Higher import tariffs"], a: 1, why: "It tackles the skills mismatch." },
  { q: "A possible disadvantage of expansionary fiscal policy to reduce unemployment is:", opts: ["Lower inflation", "A larger budget deficit and possible inflation", "Fewer jobs", "Lower AD"], a: 1, why: "Spending may raise prices and the deficit." },
  { q: "A minimum wage set above the equilibrium wage may:", opts: ["Reduce unemployment", "Increase employers' demand for workers", "Increase unemployment among low-skilled workers", "Reduce prices"], a: 2, why: "Firms may hire fewer workers." },
  { q: "Which policy would best reduce frictional unemployment?", opts: ["Better job information", "Higher government spending", "Higher interest rates", "Tariffs"], a: 0, why: "Faster matching reduces time between jobs." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand-side policy", "Fiscal and monetary policy that changes aggregate demand."],
  ["Supply-side policy", "Measures to raise productive capacity and improve how labour markets work."],
  ["Retraining", "Teaching workers new skills so they can move to different jobs."],
  ["Regional policy", "Policies to create jobs and investment in depressed regions."],
  ["Labour market reform", "Changes to make labour markets more flexible, such as easier hiring and lower benefits."],
  ["Minimum wage", "The lowest wage employers can legally pay."],
  ["Tariff", "A tax on imports."],
  ["Job centre", "A service that helps unemployed people find work."],
  ["Diversification", "Developing different industries so an area is less dependent on one."],
] });
showMatrix();
