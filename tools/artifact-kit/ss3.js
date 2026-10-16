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

const SG = ["Government spends on training, infrastructure and incentives", "AS shifts right: productive capacity rises", "Real GDP rises: economic growth", "Structural unemployment falls as skills match vacancies", "Costs fall, so the price level falls or rises by less", "Exports become more competitive: current account may improve"];
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Gains of a successful supply-side policy", base: { n: 0 }, draw: mkChain(SG, "--good"), steps: chainSteps(["The government uses <b>supply-side measures</b>: training, infrastructure, incentives.", "<b>AS shifts right</b>: the economy can produce more at each price level.", "<b>Growth:</b> real GDP rises.", "<b>Jobs:</b> better skills and incentives mean <b>structural unemployment</b> may fall.", "<b>Prices:</b> lower costs and more output mean the price level falls or rises by less.", "<b>Balance of payments:</b> lower costs could make exports more competitive. <b>Evaluate:</b> all of this takes years, and some measures have costs."]) });
const SC = [
  { n: "Education and training", g: "▲ long run", u: "▼ structural falls", i: "▼ eases", c: "▲ may improve", b: "▲ revenue later, ▼ cost first", catch: "Slow and costly; skills must match jobs." },
  { n: "Infrastructure", g: "▲ long run", u: "▼ construction jobs, then others", i: "▼ lower costs", c: "▲ exports easier", b: "▼ large cost", catch: "Delays, cost and environmental damage." },
  { n: "Labour market reforms", g: "▲ may rise", u: "▼ may fall", i: "▼ lower wage costs", c: "▲ more competitive", b: "▲ less benefit spending", catch: "Insecurity and inequality; cuts in benefits reduce demand." },
  { n: "Lower direct taxes", g: "▲ incentives", u: "▼ may fall", i: "◆ little effect", c: "◆ little effect", b: "▼ revenue falls", catch: "High earners gain most; behaviour may not change." },
  { n: "Deregulation", g: "▲ competition", u: "▼ new firms, new jobs", i: "▼ competition cuts prices", c: "▲ may improve", b: "◆ small effect", catch: "Less protection for consumers, workers and the environment." },
  { n: "Privatisation", g: "▲ efficiency", u: "▲ job losses at first", i: "▼ may fall (or rise if monopoly)", c: "◆ little effect", b: "▲ sale revenue", catch: "Private monopoly; loss of public service; job losses." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Growth</th><th>Unemployment</th><th>Inflation</th><th>Current account</th><th>Budget</th></tr><tr><td>${p.g}</td><td>${p.u}</td><td>${p.i}</td><td>${p.c}</td><td>${p.b}</td></tr></table></div><div class="warn"><b class="h">The catch</b>${p.catch}</div>`);
const UT = [
  { n: "Structural", d: "Workers' skills do not match vacancies, often after an industry declines.", w: "Supply-side policy works well: training and mobility help match workers and jobs.", t: "Training, retraining, relocation help." },
  { n: "Frictional", d: "People are between jobs and searching.", w: "Supply-side policy helps: better job information, and lower benefits may speed job search.", t: "Job information, benefit conditions." },
  { n: "Cyclical (demand-deficient)", d: "Not enough demand in a recession.", w: "Supply-side policy alone may not help: there are no jobs because spending is low. Demand-side policy fits better.", t: "Fiscal and monetary policy." },
  { n: "Seasonal", d: "Work depends on the time of year, such as tourism or farming.", w: "Limited: the pattern of work is the cause, though training for other industries may help.", t: "Retraining; year-round industries." },
];
button_table("utBtns", "utOut", UT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it is</th><th>Will supply-side policy help?</th><th>Better tool</th></tr><tr><td>${p.d}</td><td>${p.w}</td><td>${p.t}</td></tr></table></div>`);
function labA() {
  if (!$("#ab") || !$("#aa")) return;
  const a = +$("#aa").value, sh = +$("#ab").value, [y, p] = solve2(sh, a);
  $("#ab1").textContent = (y - 50 >= 0 ? "+" : "−") + money(Math.abs(y - 50), 1); $("#ab2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#abv").textContent = a === 0 && sh === 0 ? "Move a slider." : a > sh ? "A bigger supply-side effect: output grows with lower or falling prices. But it took years to build." : sh > a ? "A bigger demand-side effect: output rises but with more inflationary pressure." : "Equal shifts: growth with a roughly stable price level.";
  $("#labA").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g3"), { id: "aa", label: "Supply-side policy (AS shift)", min: 0, max: 30, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labA });
Lib.slider($("#g4"), { id: "ab", label: "Demand-side policy (AD shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labA });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost or risk</b> of supply-side policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP could rise in the long run", b: 0 }, { text: "Structural unemployment could fall", b: 0 }, { text: "Firms' costs could fall, holding prices down", b: 0 }, { text: "Exports could become more competitive", b: 0 },
  { text: "It can take years to work", b: 1 }, { text: "Education and infrastructure are costly", b: 1 }, { text: "Cuts in benefits and taxes could widen inequality", b: 1 }, { text: "Privatisation could create a private monopoly", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> does each measure mainly support?", buckets: [{ label: "Growth" }, { label: "Lower unemployment" }, { label: "Stable prices" }, { label: "Balance of payments" }], items: [
  { text: "Infrastructure that raises long-run productive capacity", b: 0 }, { text: "Tax breaks for business investment", b: 0 },
  { text: "Retraining for workers in declining industries", b: 1 }, { text: "Help with job search", b: 1 },
  { text: "Deregulation that cuts firms' costs", b: 2 }, { text: "Competition that holds prices down", b: 2 },
  { text: "Lower costs make exports cheaper", b: 3 }, { text: "Home-produced goods replace imports", b: 3 },
], done: "Name the aim, then follow the chain." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how supply-side policy could reduce structural unemployment</b>.", items: [
  "The government funds retraining for workers in a declining industry",
  "Workers gain skills that employers need",
  "Workers can fill vacancies in growing industries",
  "The mismatch between workers and jobs narrows",
  "Structural unemployment falls",
], done: "A chain for a 6-mark analysis." });
Lib.calc($("#c1"), { qs: [
  { q: "Unemployment falls from 2.5 million to 2.0 million. The labour force is 25 million. What is the new unemployment rate (%)?", a: 8, sol: "2.0 ÷ 25 × 100 = <b>8%</b>." },
  { q: "Real GDP rises from $600bn to $624bn after supply-side reforms. What is the percentage growth?", a: 4, sol: "24 ÷ 600 × 100 = <b>4%</b>." },
  { q: "A government runs a deficit of $20bn. Growth raises tax revenue by $4bn and cuts benefit spending by $2bn. What is the new deficit ($bn)?", a: 14, sol: "20 − 4 − 2 = <b>$14bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the most likely effect of a successful supply-side policy on an economy?", opts: ["Falling real GDP", "A rise in productive capacity and potential output", "Higher inflation and unemployment", "A bigger budget deficit"], a: 1, why: "AS shifts right, raising potential output." },
  { q: "Which type of unemployment is most likely to fall because of education and training?", opts: ["Cyclical", "Structural", "Seasonal only", "None"], a: 1, why: "Training matches workers' skills to vacancies." },
  { q: "Supply-side policy is less likely to help when unemployment is caused by:", opts: ["A lack of skills", "A recession with low demand", "A decline in an industry", "Job search delays"], a: 1, why: "Low demand needs demand-side policy." },
  { q: "Which is a possible disadvantage of cutting unemployment benefit as a supply-side measure?", opts: ["It may reduce spending by the poor", "It always raises employment", "It raises the deficit", "It cuts productivity"], a: 0, why: "Lower benefits reduce incomes and may reduce AD." },
  { q: "A supply-side policy could reduce a budget deficit if it:", opts: ["Raises employment and tax revenue", "Lowers GDP", "Raises benefits", "Raises imports"], a: 0, why: "More jobs mean more tax and fewer benefits." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Structural unemployment", "Unemployment caused by a mismatch between workers' skills and the jobs available."],
  ["Frictional unemployment", "Unemployment of people between jobs and searching for work."],
  ["Cyclical unemployment", "Unemployment caused by lack of demand in a recession."],
  ["Cost-push inflation", "A rise in the price level caused by rising costs of production."],
  ["Potential output", "The level of output when resources are fully and efficiently used."],
  ["Time lag", "The delay between a policy change and its effects."],
  ["Unemployment trap", "When benefits are so close to wages that working pays little more."],
  ["Private monopoly", "A single privately owned firm dominating a market, which may raise prices."],
] });
 labA();
