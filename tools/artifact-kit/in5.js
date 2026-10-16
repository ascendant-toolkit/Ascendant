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

Lib.stepper($("#stD"), { w: 760, h: 400, label: "Contractionary policy against demand-pull inflation", base: { sh: 14, a: 0 }, draw: adasChart, steps: [
  { cap: "Excess demand has pushed AD to the <b>right</b>. The price level is rising: <b>demand-pull inflation</b>.", s: { sh: 30, a: 0 } },
  { cap: "The central bank <b>raises interest rates</b> and the government cuts spending or raises taxes. <b>AD shifts back to the left</b>.", s: { sh: 14, a: 0 } },
  { cap: "The price level stops rising (or rises more slowly): inflation falls. <b>Evaluate:</b> output also falls, so <b>unemployment may rise</b>. That is the cost of controlling demand-pull inflation.", s: { sh: 0, a: 0 } },
] });
const IR = ["Central bank raises the interest rate", "Borrowing costs more and saving pays more", "Consumption and investment fall", "The currency may rise, so imports are cheaper", "AD shifts left and costs fall", "Inflation falls, but output and jobs are at risk"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "How higher interest rates reduce inflation", base: { n: 0 }, draw: mkChain(IR, "--accent"), steps: chainSteps(["The central bank <b>raises interest rates</b>.", "Borrowing costs more and <b>saving pays more</b>.", "<b>Consumption and investment fall</b>.", "The <b>currency may rise</b>, making imports and raw materials cheaper.", "<b>AD shifts left</b> and costs fall.", "<b>Inflation falls</b>. Evaluate: growth slows, unemployment may rise, and borrowers suffer."]) });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy against cost-push inflation", base: { sh: 0, a: -12 }, draw: adasChart, steps: [
  { cap: "Rising costs have shifted AS <b>left</b>: output has fallen and prices have risen: <b>cost-push inflation</b>.", s: { sh: 0, a: -12 } },
  { cap: "The government invests in <b>training, infrastructure and competition</b>. Productivity rises and firms' costs fall.", s: { sh: 0, a: 0 } },
  { cap: "AS shifts <b>right</b>: output rises and the price level falls. <b>Evaluate:</b> it works slowly and costs money, but it does not cost jobs.", s: { sh: 0, a: 12 } },
] });

/* Lab 1: policy simulator */
function labP() {
  if (!$("#pa") || !$("#pb")) return;
  const pol = +$("#pa").value, sup = +$("#pb").value, sh0 = 24, [y0, p0] = solve2(sh0, 0), [y, p] = solve2(sh0 - pol, sup);
  $("#pa1").textContent = (p - p0 >= 0 ? "+" : "−") + money(Math.abs(p - p0), 1); $("#pa2").textContent = (y - y0 >= 0 ? "+" : "−") + money(Math.abs(y - y0), 1); $("#pa3").textContent = money(p, 1);
  $("#pav").textContent = pol === 0 && sup === 0 ? "The economy starts overheated: AD has shifted +24 and the price level is high. Choose a policy." : pol > 0 && sup === 0 ? `Contractionary policy cuts AD by ${pol}: the price level falls by ${money(p0 - p, 1)}, but output falls by ${money(y0 - y, 1)}, so jobs may be lost.` : pol === 0 ? `Supply-side policy raises AS by ${sup}: the price level changes by ${p - p0 >= 0 ? "+" : "−"}${money(Math.abs(p - p0), 1)} and output rises by ${money(y - y0, 1)}. It does not cost output, but it takes years.` : `A mix: the price level falls by ${money(p0 - p, 1)} and output changes by ${y - y0 >= 0 ? "+" : "−"}${money(Math.abs(y - y0), 1)}.`;
  let o = axes("Price level", "Real GDP") + SV.path(ptsPath([[QX(sup), PY(30)], [QX(60 + sup), PY(54)], [QX(87.7 + sup), PY(115)]]), "c3") + SV.text(QX(87.7 + sup) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90 + 0.8 * sh0, "c1", "AD", { t: "t1", attrs: { opacity: pol ? 0.4 : 1 } }); if (pol) o += adLine(90 + 0.8 * (sh0 - pol), "c4", "AD₁", { t: "t4" });
  o += hline(p0, "gr", y0) + vline(y0, p0) + SV.circle(QX(y0), PY(p0), 6, "dot1", { opacity: 0.5 }) + ylab(p0, "P", "sm bd") + xlab(y0, "Y", "sm bd");
  if (pol || sup) o += hline(p, "gr", y) + vline(y, p) + SV.circle(QX(y), PY(p), 6, "dot2") + ylab(p, "P₁", "sm bd") + xlab(y, "Y₁", "sm bd");
  $("#labP").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Contractionary demand-side policy (AD shift left)", min: 0, max: 30, step: 2, value: 12, fmt: (v) => "−" + v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Supply-side policy (AS shift right)", min: 0, max: 24, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labP });
/* Lab 2: which policy for which cause */
const TYPES = ["Demand-pull", "Cost-push: wages", "Cost-push: imports (weak currency)"], POLS = ["Raise interest rates", "Cut spending or raise taxes", "Supply-side policy (training, competition)", "Let the exchange rate rise", "Wage and price controls"];
const RATE = [[3, 1, 1], [3, 1, 0], [1, 3, 2], [1, 1, 3], [1, 2, 1]];
const NOTE = [["Cuts spending and AD, tackling excess demand.", "Reduces spending but does not lower wage costs; may cause unemployment.", "A higher rate can raise the exchange rate, which lowers import prices: some help."], ["Directly reduces demand-pull pressure.", "May reduce pressure on wages if unemployment rises, but a blunt tool.", "Does not address imported costs."], ["Raising capacity eases demand-pull pressure only slowly.", "Productivity gains offset wage rises: lowers unit labour costs.", "Competition and domestic substitutes reduce reliance on imports."], ["Lower import prices help a little but also reduce exports.", "Little effect on wages.", "Directly lowers the cost of imported inputs and goods."], ["Cannot easily control spending.", "Limits wage growth directly, but hard to enforce and may cause disputes.", "Cannot control world prices."]];
const RL = ["Little effect", "Some help", "Moderate help", "Very effective"];
let selT = 0, selP = 0;
function showMatrix() {
  $("#mxT").innerHTML = TYPES.map((t, j) => `<button class="b${j === selT ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $("#mxP").innerHTML = POLS.map((t, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${t}</button>`).join("");
  $$("#mxT .b").forEach((b) => (b.onclick = () => { selT = +b.dataset.j; showMatrix(); }));
  $$("#mxP .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; showMatrix(); }));
  const r = RATE[selP][selT];
  $("#mxOut").innerHTML = `<div class="verdict"><b>${POLS[selP]}</b> against <b>${TYPES[selT].toLowerCase()}</b> inflation: <b>${RL[r]}</b>. ${NOTE[selP][selT]}</div>`;
}
showMatrix();

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>monetary</b>, <b>fiscal</b> or <b>supply-side</b> way to control inflation?", buckets: [{ label: "Monetary" }, { label: "Fiscal" }, { label: "Supply-side" }], items: [
  { text: "Raise the interest rate", b: 0 }, { text: "Reduce the money supply", b: 0 }, { text: "Let the currency rise", b: 0 },
  { text: "Raise income tax", b: 1 }, { text: "Cut government spending", b: 1 },
  { text: "Train workers to raise productivity", b: 2 }, { text: "Increase competition between firms", b: 2 }, { text: "Improve infrastructure to cut firms' costs", b: 2 },
], done: "Match the type of policy to how it works." });
Lib.classify($("#cl2"), { prompt: "Which type of inflation does each policy mainly address?", buckets: [{ label: "Demand-pull" }, { label: "Cost-push" }], items: [
  { text: "Higher interest rates", b: 0 }, { text: "Higher taxes", b: 0 }, { text: "Cutting government spending", b: 0 },
  { text: "Training that raises productivity", b: 1 }, { text: "A stronger currency lowering import costs", b: 1 }, { text: "Deregulation lowering firms' costs", b: 1 },
], done: "Demand-pull: cut demand. Cost-push: cut costs." });
Lib.match($("#m1"), { prompt: "Match the policy to its main weakness.", pairs: [
  ["Raise interest rates", "Raises unemployment and hurts borrowers"],
  ["Cut government spending", "Reduces services and jobs"],
  ["Raise income tax", "Politically unpopular; may reduce work incentives"],
  ["Let the currency rise", "Makes exports dearer"],
  ["Supply-side policy", "Slow and costly"],
  ["Wage and price controls", "Hard to enforce and distorts markets"],
], done: "Every policy needs an evaluation point." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in income tax could reduce demand-pull inflation</b>.", items: [
  "The government raises income tax",
  "Households' disposable income falls",
  "Consumption falls",
  "Aggregate demand shifts left",
  "Demand-pull pressure on prices eases",
], done: "A fiscal policy chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Inflation is 8% and the central bank wants 2%. By how many percentage points does it need to fall?", a: 6, sol: "8 − 2 = <b>6 percentage points</b>." },
  { q: "The CPI is 105 and the inflation target is 2%. What CPI would match 2% next year?", a: 107.1, tol: 0.1, sol: "105 × 1.02 = <b>107.1</b>." },
  { q: "A tax rise cuts consumption by $12bn and the multiplier is 1.5. By how much does AD fall ($bn)?", a: 18, sol: "12 × 1.5 = <b>$18bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which policy is most likely to reduce demand-pull inflation?", opts: ["Cutting interest rates", "Raising interest rates", "Increasing government spending", "Cutting taxes"], a: 1, why: "Higher rates reduce spending." },
  { q: "Which policy would best reduce cost-push inflation caused by low productivity?", opts: ["Raising interest rates", "Supply-side policy such as training", "Cutting benefits", "Raising taxes"], a: 1, why: "Higher productivity lowers costs." },
  { q: "A disadvantage of raising interest rates to control inflation is:", opts: ["Lower unemployment", "Slower growth and possible higher unemployment", "Higher spending", "Lower saving"], a: 1, why: "AD falls, so output may fall." },
  { q: "A central bank could avoid deflation by:", opts: ["Raising interest rates", "Cutting interest rates and increasing the money supply", "Cutting government spending", "Raising the exchange rate"], a: 1, why: "Expansionary monetary policy." },
  { q: "A higher exchange rate may reduce inflation because:", opts: ["Imports become cheaper", "Exports rise", "Wages fall", "Spending rises"], a: 0, why: "Import costs fall." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Contractionary policy", "Policy that reduces aggregate demand, such as higher interest rates or higher taxes."],
  ["Inflation target", "A rate of inflation that the central bank aims to achieve, often 2%."],
  ["Monetary policy", "Interest rates, money supply and exchange rate used to influence AD and inflation."],
  ["Fiscal policy", "Government spending and taxation used to influence AD."],
  ["Supply-side policy", "Measures to raise productive capacity and lower costs."],
  ["Price controls", "Government limits on how much prices can rise."],
  ["Central bank independence", "When a central bank sets interest rates without political interference."],
  ["Quantitative easing", "A central bank buying bonds to increase the money supply."],
  ["Time lag", "The delay between a policy change and its effect."],
] });
labP(); showMatrix();
