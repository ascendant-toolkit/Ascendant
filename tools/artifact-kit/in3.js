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

Lib.stepper($("#stD"), { w: 760, h: 400, label: "Demand-pull inflation", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Spending rises: lower interest rates, tax cuts, booming exports. <b>AD shifts right</b>. Output rises and the price level rises.", s: { sh: 14, a: 0 } },
  { cap: "If the economy is <b>close to full capacity</b>, AS is steep. The same rise in demand gives a small rise in output and a <b>big rise in prices</b>: <b>demand-pull inflation</b>.", s: { sh: 40, a: 0 } },
] });
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Cost-push inflation", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Costs rise: oil and raw material prices, wages above productivity, a weaker currency raising import costs. <b>AS shifts left</b> to AS₁.", s: { sh: 0, a: -12 } },
  { cap: "Output <b>falls</b> to Y₁ and the price level <b>rises</b> to P₁: <b>cost-push inflation</b>. Unemployment may rise as well.", s: { sh: 0, a: -12 } },
] });
const WSP = ["Prices rise, so workers' real wages fall", "Workers (and unions) demand higher wages", "Firms' costs rise: cost-push pressure", "Higher wages also raise spending: demand-pull pressure", "Firms raise prices again", "The cycle repeats: a wage-price spiral"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "The wage-price spiral", base: { n: 0 }, draw: mkChain(WSP, "--bad"), steps: chainSteps(["Prices rise, so workers' <b>real wages fall</b>.", "Workers and unions <b>demand higher wages</b>.", "<b>Firms' costs rise</b>: cost-push pressure.", "Higher pay also raises spending: <b>demand-pull pressure</b>.", "Firms <b>raise prices</b> again.", "The cycle <b>repeats</b>: a wage-price spiral. Expectations of inflation make it harder to stop."]) });

/* Lab 1 */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const sh = +$("#ta").value, a = -(+$("#tb").value), [y, p] = solve2(sh, a), dy = y - 50, dp = p - 50;
  $("#ta1").textContent = (dy >= 0 ? "+" : "−") + money(Math.abs(dy), 1); $("#ta2").textContent = (dp >= 0.05 ? "+" : dp <= -0.05 ? "−" : "") + money(Math.abs(dp), 1);
  $("#ta3").textContent = sh > 0 && a === 0 ? "Demand-pull" : sh === 0 && a < 0 ? "Cost-push" : sh > 0 && a < 0 ? "Both" : "None";
  $("#tav").textContent = sh === 0 && a === 0 ? "Move a slider." : a === 0 ? `AD shifts right: output +${money(dy, 1)} and prices +${money(dp, 1)}. Demand-pull inflation. The nearer to full capacity, the more of it is prices.` : sh === 0 ? `AS shifts left: output ${money(dy, 1)} and prices +${money(dp, 1)}. Cost-push inflation: prices rise while output falls.` : `Both: prices rise by ${money(dp, 1)}. Output changes by ${dy >= 0 ? "+" : ""}${money(dy, 1)}.`;
  $("#labT").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ta", label: "Rise in AD (demand-pull)", min: 0, max: 50, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labT });
Lib.slider($("#g2"), { id: "tb", label: "Rise in costs (AS shifts left)", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labT });
const CAUSE = [
  { n: "Higher consumer spending", t: "Demand-pull", e: "Lower interest rates, tax cuts or higher confidence raise C and so AD." },
  { n: "Higher government spending", t: "Demand-pull", e: "G is a part of AD; a large stimulus may overheat the economy." },
  { n: "Booming exports", t: "Demand-pull", e: "Strong overseas demand raises X and so AD." },
  { n: "Rise in the money supply", t: "Demand-pull", e: "More money and credit raise spending." },
  { n: "Wages rise faster than productivity", t: "Cost-push (and demand-pull)", e: "Labour costs per unit rise; higher pay can also raise spending." },
  { n: "Higher oil or raw material prices", t: "Cost-push", e: "Firms' costs rise across many industries, so prices rise." },
  { n: "Fall in the exchange rate", t: "Cost-push (imported inflation)", e: "Imported inputs and goods cost more in the home currency." },
  { n: "Higher indirect taxes", t: "Cost-push", e: "VAT and excise duties raise the price firms and consumers pay." },
];
button_table("ctBtns", "ctOut", CAUSE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type of inflation</th><th>How it works</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a cause of <b>demand-pull</b> or <b>cost-push</b> inflation?", buckets: [{ label: "Demand-pull" }, { label: "Cost-push" }], items: [
  { text: "Consumer confidence and spending surge", b: 0 }, { text: "Interest rates are cut", b: 0 }, { text: "A government stimulus package", b: 0 }, { text: "A boom in exports", b: 0 },
  { text: "A rise in oil prices", b: 1 }, { text: "Wages rise faster than productivity", b: 1 }, { text: "The currency falls, raising import costs", b: 1 }, { text: "Firms face higher raw material costs", b: 1 },
], done: "Demand-pull: AD shifts right. Cost-push: AS shifts left." });
Lib.classify($("#cl2"), { prompt: "Which <b>diagram shift and effect</b> fits each type?", buckets: [{ label: "AD shifts right" }, { label: "AS shifts left" }], items: [
  { text: "Demand-pull inflation", b: 0 }, { text: "Output rises and unemployment falls", b: 0 }, { text: "Tax cuts raise spending", b: 0 },
  { text: "Cost-push inflation", b: 1 }, { text: "Output falls and unemployment may rise", b: 1 }, { text: "Energy costs surge", b: 1 },
], done: "Link the type to the diagram." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Demand-pull inflation", "Inflation caused by total demand growing faster than supply"],
  ["Cost-push inflation", "Inflation caused by a rise in firms' costs of production"],
  ["Imported inflation", "Inflation caused by dearer imports, often after a currency falls"],
  ["Wage-price spiral", "Wages and prices pushing each other up"],
  ["Productivity", "Output per worker"],
  ["Full capacity", "When resources are fully used and output cannot rise more"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could cause inflation</b>.", items: [
  "The currency falls against other currencies",
  "Imported raw materials and goods cost more in the home currency",
  "Firms' costs of production rise",
  "AS shifts to the left",
  "Firms raise prices: cost-push inflation",
], done: "Imported inflation chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Wages rise 6% and productivity rises 2%. By roughly what percentage do labour costs per unit rise?", a: 4, sol: "6 − 2 = <b>about 4%</b>." },
  { q: "A raw material that makes up 30% of a firm's costs rises in price by 20%. By how much do the firm's total costs rise (%)?", a: 6, sol: "30% × 20% = <b>6%</b>." },
  { q: "Total spending rises 5% but output can only rise 2%. By roughly how much could the price level rise (%)?", a: 3, sol: "5 − 2 = <b>about 3%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of demand-pull inflation?", opts: ["A rise in oil prices", "A cut in interest rates leading to higher spending", "A rise in productivity", "A fall in wages"], a: 1, why: "Higher spending raises AD." },
  { q: "Which is a cause of cost-push inflation?", opts: ["Higher consumer confidence", "A rise in firms' raw material costs", "A rise in exports", "More government spending"], a: 1, why: "Higher costs shift AS left." },
  { q: "A fall in the exchange rate may cause inflation because:", opts: ["Imported inputs cost more", "Exports fall", "Wages fall", "Spending falls"], a: 0, why: "Imported inflation." },
  { q: "Demand-pull inflation is most likely when the economy is:", opts: ["In deep recession", "Close to full capacity", "Producing far below capacity", "In deflation"], a: 1, why: "Prices rise when output cannot." },
  { q: "Wages rising faster than productivity is most likely to cause:", opts: ["Cost-push inflation", "Deflation", "Lower prices", "Falling costs"], a: 0, why: "Unit labour costs rise." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand-pull inflation", "A rise in the price level caused by AD growing faster than AS."],
  ["Cost-push inflation", "A rise in the price level caused by a rise in firms' costs."],
  ["Imported inflation", "Inflation caused by rising import prices, often after a fall in the exchange rate."],
  ["Wage-price spiral", "A cycle where higher wages raise prices, which lead to higher wage demands."],
  ["Productivity", "Output per worker or per unit of input."],
  ["Full capacity", "When resources are fully used so output cannot rise more."],
  ["Unit labour costs", "Labour cost per unit of output."],
  ["Total demand", "Aggregate demand: C + I + G + (X − M)."],
  ["Supply shock", "A sudden change in costs or supply, such as an oil price rise."],
] });
labT();
