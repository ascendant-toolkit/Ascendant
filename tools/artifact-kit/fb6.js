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
const D = (b) => [-b, 50 + 50 * b], S = (d, shift = 0) => [d, 50 - 50 * d + shift];
const fmtSteep = (v) => (v < 0.8 ? "flat (elastic)" : v > 1.4 ? "steep (inelastic)" : "medium");
const money = (v, d = 1) => Lib.fmtN(v, d);
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
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Fiscal policy shifting aggregate demand", base: { sh: 0 }, draw: adChart, steps: [
  { cap: "The economy starts at <b>Y</b> (real GDP) and <b>P</b> (price level) where AD meets AS. <b>AD = C + I + G + (X − M)</b>. Government spending (G) is part of AD, and taxes change how much households (C) and firms (I) have to spend.", s: { sh: 0 } },
  { cap: "<b>Expansionary fiscal policy</b>: the government raises spending and/or cuts taxes. AD shifts <b>right</b> to AD₁. Real GDP rises (<b>economic growth</b>), firms need more workers (<b>employment is likely to rise</b>) and the price level edges up.", s: { sh: 15 } },
  { cap: "<b>Evaluate:</b> push too hard when the economy is close to full capacity and AS is steep. The rise in output is small and most of the effect is a <b>higher price level</b>: inflation. It also leaves a bigger budget deficit.", s: { sh: 40 } },
  { cap: "<b>Contractionary fiscal policy</b>: cut spending and/or raise taxes. AD shifts <b>left</b> to AD₂. Price pressure eases, which helps against inflation, and spending on imports falls, but output and jobs are likely to fall too.", s: { sh: -15 } },
] });


const FCH = ["Government raises spending and/or cuts taxes", "AD shifts to the right", "Output ↑ (growth) and jobs ↑ (unemployment ↓)", "Price level ↑: risk of demand-pull inflation", "Imports ↑ with higher incomes: current account may worsen", "Budget deficit widens: more borrowing and debt"];
function fchain(s) {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  FCH.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap), col = i < 3 ? "--good" : "--bad";
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" });
    if (i < FCH.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 400, label: "Gains and costs of expansionary fiscal policy", base: { n: 0 }, draw: fchain, steps: [
  { cap: "The government uses <b>expansionary fiscal policy</b>: more spending and/or lower taxes.", s: { n: 1 } },
  { cap: "<b>AD shifts right.</b>", s: { n: 2 } },
  { cap: "<b>Gains:</b> real GDP rises and firms need more workers. Growth and employment aims move closer.", s: { n: 3 } },
  { cap: "<b>Costs:</b> as demand rises the price level may rise, especially close to full capacity: demand-pull inflation.", s: { n: 4 } },
  { cap: "Higher incomes also draw in more <b>imports</b>, so the current account may worsen.", s: { n: 5 } },
  { cap: "And the government has to <b>borrow</b> more, so the budget deficit and national debt grow. This is why aims <b>conflict</b>.", s: { n: 6 } },
] });

function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const b = +$("#sa").value, dG = +$("#sb").value, [y0, p0] = solveAD(b), [y1, p1, c1] = solveAD(b + dG), c0 = 90 + 0.8 * b;
  $("#sa1").textContent = (y1 - y0 >= 0 ? "+" : "−") + money(Math.abs(y1 - y0), 1); $("#sa2").textContent = (p1 - p0 >= 0 ? "+" : "−") + money(Math.abs(p1 - p0), 1);
  $("#sa3").textContent = y0 < 40 ? "Deep slump" : y0 < 52 ? "Spare capacity" : y0 < 62 ? "Near full capacity" : "Overheating";
  $("#sav").textContent = Math.abs(dG) < 1 ? "No policy change: nothing moves." : y1 - y0 > 2 * Math.abs(p1 - p0) ? "There is spare capacity, so most of the effect shows up in output and jobs, with only a small change in prices." : "Close to full capacity, a large part of the effect shows up in the price level: more inflation for each unit of extra output.";
  const xs = (y) => QX(y), ypos = (p) => PY(p);
  let o = axes("Price level", "Real GDP") + SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(c0, "c1", "AD", { t: "t1", attrs: { opacity: Math.abs(dG) >= 1 ? 0.4 : 1 } });
  if (Math.abs(dG) >= 1) o += adLine(c1, dG > 0 ? "c2" : "c4", dG > 0 ? "AD₁" : "AD₂", { t: dG > 0 ? "t2" : "t4" });
  o += hline(p0, "gr", y0) + vline(y0, p0) + SV.circle(xs(y0), ypos(p0), 6, "dot1", { opacity: 0.5 }) + ylab(p0, "P", "sm bd") + xlab(y0, "Y", "sm bd");
  if (Math.abs(dG) >= 1) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(xs(y1), ypos(p1), 6, dG > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  $("#labS").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sa", label: "Where the economy starts", min: -30, max: 35, step: 5, value: -10, fmt: (v) => (v < -15 ? "slump" : v < 15 ? "spare capacity" : "near full capacity"), onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Change in government spending (AD shift)", min: -20, max: 20, step: 1, value: 10, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labS });
const SC = [
  { n: "Cut taxes", g: "▲ rises", u: "▼ falls", i: "▲ may rise", c: "▼ may worsen (more imports)", b: "▼ deficit widens", catch: "Some of the cut is saved; benefits higher earners most in cash." },
  { n: "Raise government spending", g: "▲ rises", u: "▼ falls", i: "▲ risk near full capacity", c: "▼ may worsen", b: "▼ deficit widens", catch: "Time lags; opportunity cost; borrowing." },
  { n: "Raise taxes", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", b: "▲ deficit narrows", catch: "May discourage effort and investment; slower growth reduces revenue." },
  { n: "Cut government spending", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", b: "▲ deficit narrows", catch: "Public services and jobs suffer; may take longer than hoped to cut the deficit." },
  { n: "Progressive taxes and higher benefits", g: "◆ little effect", u: "◆ little effect", i: "◆ little effect", c: "◆ little effect", b: "▼ may widen", catch: "Redistributes income, but a high tax may reduce effort." },
  { n: "Green spending and pollution taxes", g: "▲ long run", u: "◆ may create jobs", i: "▲ costs may rise", c: "◆ little effect", b: "◆ depends", catch: "Helps environmental sustainability; may conflict with short-run growth." },
];
function showSC(i) {
  const p = SC[i];
  $("#scBtns").innerHTML = SC.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#scBtns .b").forEach((b) => (b.onclick = () => showSC(+b.dataset.j)));
  $("#scOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Growth</th><th>Unemployment</th><th>Inflation</th><th>Current account</th><th>Budget</th></tr><tr><td>${p.g}</td><td>${p.u}</td><td>${p.i}</td><td>${p.c}</td><td>${p.b}</td></tr></table></div><div class="warn"><b class="h">The catch</b>${p.catch}</div>`;
}
showSC(0);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost</b> of expansionary fiscal policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP rises", b: 0 }, { text: "Unemployment may fall", b: 0 }, { text: "More tax revenue as incomes rise", b: 0 }, { text: "Benefits help people on low incomes", b: 0 },
  { text: "Demand-pull inflation near full capacity", b: 1 }, { text: "Bigger budget deficit", b: 1 }, { text: "Higher imports and a worse current account", b: 1 }, { text: "More borrowing and debt interest", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> does each measure mainly support?", buckets: [{ label: "Growth and jobs" }, { label: "Stable prices" }, { label: "Redistribution" }, { label: "Environment" }], items: [
  { text: "Cut income tax to raise spending in a slump", b: 0 }, { text: "Build roads and rail to create jobs", b: 0 },
  { text: "Raise taxes in an overheating economy", b: 1 }, { text: "Cut government spending to reduce demand-pull inflation", b: 1 },
  { text: "Higher tax on high earners and benefits for the poor", b: 2 }, { text: "Free healthcare for low-income households", b: 2 },
  { text: "A tax on carbon emissions", b: 3 }, { text: "Subsidies for renewable energy", b: 3 },
], done: "Name the aim, then follow the chain." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why expansionary fiscal policy could conflict with the balance of payments</b>.", items: [
  "The government cuts taxes or raises spending",
  "AD rises and real incomes grow",
  "Households and firms spend more, including on imports",
  "Imports rise by more than exports",
  "The current account moves towards deficit",
], done: "A conflict between growth and the balance of payments." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP is $500bn and it rises to $520bn. What is the percentage growth?", a: 4, sol: "20 ÷ 500 × 100 = <b>4%</b>." },
  { q: "A government has a deficit of $12bn. After a contractionary policy it falls to $9bn. By what percentage did the deficit fall?", a: 25, sol: "3 ÷ 12 × 100 = <b>25%</b>." },
  { q: "The price level rises from 100 to 103 after a boost to AD. What is the inflation rate (%)?", a: 3, sol: "3 ÷ 100 × 100 = <b>3%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A government cuts taxes when the economy is close to full capacity. The most likely result is:", opts: ["Large fall in prices", "Mostly higher prices rather than higher output", "A budget surplus", "Lower imports"], a: 1, why: "With little spare capacity, extra AD mostly raises prices." },
  { q: "Expansionary fiscal policy could create a conflict between:", opts: ["Full employment and stable prices", "Equal pay and education", "Free trade and tariffs", "Poverty and population"], a: 0, why: "More spending can reduce unemployment but raise demand-pull inflation." },
  { q: "Which is a limit on the effectiveness of fiscal policy?", opts: ["Time lags", "Higher AD", "More jobs", "Lower taxes"], a: 0, why: "It can take a long time before spending reaches the economy." },
  { q: "Which fiscal policy is most likely to improve the current account in the short run?", opts: ["Higher government spending", "Higher taxes and lower spending, which reduce spending on imports", "Lower VAT", "Higher benefits"], a: 1, why: "Falling incomes reduce import spending." },
  { q: "A progressive tax system and generous benefits mainly support which aim?", opts: ["Redistribution of income", "Balance of payments stability", "Low inflation", "Full employment"], a: 0, why: "They move income from richer to poorer households." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand-pull inflation", "A rise in the price level caused by AD growing faster than AS."],
  ["Spare capacity", "Unused resources: when output is below what the economy could produce."],
  ["Time lag", "The delay between a policy change and its effects."],
  ["Conflict of aims", "When achieving one macroeconomic aim makes another harder."],
  ["Budget deficit", "Government spending is higher than revenue."],
  ["Economic growth", "A rise in real GDP over time."],
  ["Current account", "The part of the balance of payments for trade in goods and services and income flows."],
  ["Redistribution of income", "Moving income from richer to poorer people, for example through taxes and benefits."],
] });
labS(); showSC(0);
