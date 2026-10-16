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

/* business cycle: GDP wiggling around a rising trend */
const gdpT = (t) => 100 + 0.6 * t + 22 * Math.sin((2 * Math.PI * t) / 50);
const CX = (t) => 60 + t * 6.4, CYv = (g) => 330 - (g - 60) * 2.2;
function cycleChart(s) {
  const t = s.t; let o = SV.line(60, 340, 60, 30) + SV.line(60, 340, 710, 340) + SV.text(66, 40, "Real GDP", "sm") + SV.text(710, 362, "Time", "sm", { "text-anchor": "end" });
  o += SV.line(CX(0), CYv(100), CX(100), CYv(160), "dash", { style: "stroke:var(--muted);stroke-width:2" }) + SV.text(CX(100) - 4, CYv(160) - 8, "Trend (long-run growth)", "sm bd", { "text-anchor": "end" });
  const pts = []; for (let i = 0; i <= 100; i += 2) pts.push([CX(i), CYv(gdpT(i))]);
  o += SV.path(ptsPath(pts), "c3", { opacity: 0.45 });
  const done = []; for (let i = 0; i <= t; i += 1) done.push([CX(i), CYv(gdpT(i))]); done.push([CX(t), CYv(gdpT(t))]);
  if (done.length > 1) o += SV.path(ptsPath(done), "c1");
  o += SV.circle(CX(t), CYv(gdpT(t)), 8, "dot2");
  if (s.lbl) o += SV.text(CX(t), CYv(gdpT(t)) - 18, s.lbl, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}

Lib.stepper($("#stC"), { w: 760, h: 400, label: "Recession in the business cycle", base: { t: 20, lbl: "" }, draw: cycleChart, steps: [
  { cap: "The economy is growing, but near the top of a boom.", s: { t: 12, lbl: "Boom" } },
  { cap: "Spending slows and real GDP begins to <b>fall</b>. After two quarters of falling real GDP, it is a <b>recession</b>.", s: { t: 27, lbl: "Falling GDP" } },
  { cap: "Output keeps falling to a <b>trough</b>. Unemployment is high and tax revenue is low.", s: { t: 37, lbl: "Trough" } },
  { cap: "<b>Recovery</b> begins when real GDP rises again.", s: { t: 48, lbl: "Recovery" } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "A fall in total demand", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>.", s: { sh: 0, a: 0 } },
  { cap: "Confidence collapses, the interest rate rises, or exports fall. <b>AD shifts left</b>.", s: { sh: -16, a: 0 } },
  { cap: "Real GDP <b>falls</b> to Y₁, and the price level falls or rises more slowly. Firms cut output and workers.", s: { sh: -16, a: 0 } },
  { cap: "Or the economy loses resources: war, disaster or emigration. <b>AS shifts left</b>, and real GDP falls with prices rising: a more damaging recession.", s: { sh: 0, a: -12 } },
] });
const RCH = ["Total demand falls: consumers and firms cut spending", "Firms' sales and profits fall; investment is cut", "Firms lay off workers: unemployment rises", "Household incomes fall, so spending falls further", "Tax revenue falls and benefit spending rises: bigger deficit", "Output falls again: the recession may deepen"];
Lib.stepper($("#stR"), { w: 760, h: 400, label: "The recession spiral", base: { n: 0 }, draw: mkChain(RCH, "--bad"), steps: chainSteps(["<b>Demand falls</b>: consumers and firms cut spending.", "<b>Firms:</b> sales and profits fall, so they cut investment.", "<b>Workers:</b> firms lay off workers, so unemployment rises.", "<b>Consumers:</b> lower incomes mean even less spending.", "<b>Government:</b> tax revenue falls and benefit spending rises, so the deficit widens.", "<b>The spiral:</b> less spending cuts output again. Policy (lower rates, stimulus) is needed to break it."]) });

/* Lab 1: effects of a fall in GDP */
function labF() {
  if (!$("#fa")) return;
  const d = +$("#fa").value, un = 5 + 0.5 * d, rev = 100 * (1 - 1.5 * d / 100), ben = 20 * (1 + 3 * d / 100), bal = rev - (100 + ben - 20);
  $("#fa1").textContent = "−" + d + "%"; $("#fa2").textContent = money(un, 1) + "%"; $("#fa3").textContent = "$" + money(rev, 0) + "bn"; $("#fa4").textContent = (bal >= 0 ? "+" : "−") + "$" + money(Math.abs(bal), 1) + "bn";
  $("#fav").textContent = d === 0 ? "No fall in GDP. Move the slider." : `Real GDP falls ${d}%, so unemployment rises to about ${money(un, 1)}%. Tax revenue falls to $${money(rev, 0)}bn while benefit spending rises, so the budget balance moves to ${bal >= 0 ? "+" : "−"}$${money(Math.abs(bal), 1)}bn: automatic stabilisers widen the deficit.`;
  const base = 300, k = 2; let o = SV.line(80, base, 700, base);
  [["Tax revenue", rev, "--accent"], ["Benefit spending", ben, "--warn"], ["Unemployment %", un, "--bad"]].forEach(([n, v, c], i) => {
    const x = 120 + i * 190, kk = i === 2 ? 14 : 2, h = v * kk;
    o += SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, (i === 2 ? money(v, 1) + "%" : "$" + money(v, 0) + "bn"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labF").innerHTML = o;
}
Lib.slider($("#g1"), { id: "fa", label: "Fall in real GDP", min: 0, max: 10, step: 1, value: 4, fmt: (v) => "−" + v + "%", onInput: labF });
/* Lab 2: causes picker */
const RC = [
  { n: "Fall in consumer confidence", t: "Total demand", e: "Households fear unemployment and cut spending and borrowing: AD shifts left.", ex: "Financial crisis, rising unemployment news" },
  { n: "Higher interest rates", t: "Total demand", e: "Loans and mortgages cost more, so consumption and investment fall.", ex: "Central bank tightening to fight inflation" },
  { n: "Cut in government spending", t: "Total demand", e: "G falls and jobs in the public sector are lost: AD shifts left.", ex: "Austerity after a debt crisis" },
  { n: "Fall in exports", t: "Total demand", e: "A world slowdown reduces demand for the country's exports.", ex: "Global recession, loss of a major trading partner" },
  { n: "Emigration of workers", t: "Quantity of resources", e: "The labour force shrinks: AS shifts left.", ex: "Albania after 2013 (past paper)" },
  { n: "War or natural disaster", t: "Quantity of resources", e: "Factories, farms and infrastructure are destroyed: AS shifts left.", ex: "Earthquakes, floods, conflict" },
  { n: "Falling investment and skills", t: "Quality of resources", e: "Capital becomes outdated and skills decline: productivity and AS fall.", ex: "Long-term cuts in education and training" },
];
button_table("rcBtns", "rcOut", RC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type of cause</th><th>How it causes recession</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td><td>${p.ex}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each cause of recession a fall in <b>total demand</b>, in the <b>quantity of resources</b> or in the <b>quality of resources</b>?", buckets: [{ label: "Total demand" }, { label: "Quantity of resources" }, { label: "Quality of resources" }], items: [
  { text: "Consumer confidence collapses", b: 0 }, { text: "Interest rates rise sharply", b: 0 }, { text: "Government spending is cut", b: 0 },
  { text: "Workers emigrate in large numbers", b: 1 }, { text: "A war destroys factories", b: 1 }, { text: "A natural disaster destroys farmland", b: 1 },
  { text: "Education spending is cut for many years", b: 2 }, { text: "Investment falls so machinery becomes outdated", b: 2 },
], done: "Same three headings as growth, in reverse." });
Lib.classify($("#cl2"), { prompt: "Who is affected? Put each consequence of recession with the <b>group</b>.", buckets: [{ label: "Consumers" }, { label: "Workers" }, { label: "Firms" }, { label: "Government" }], items: [
  { text: "Lower incomes and lower confidence", b: 0 }, { text: "Fall into debt", b: 0 },
  { text: "Unemployment rises", b: 1 }, { text: "Pay is frozen or cut", b: 1 },
  { text: "Falling sales and profits", b: 2 }, { text: "Some firms close", b: 2 },
  { text: "Tax revenue falls", b: 3 }, { text: "Benefit spending rises", b: 3 },
], done: "Four groups: consumers, workers, firms, government." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Recession", "A fall in real GDP for two or more successive quarters"],
  ["Trough", "The lowest point of output in the cycle"],
  ["Automatic stabilisers", "Spending and taxes that move with the cycle and cushion falls in demand"],
  ["Unemployment", "People who are able and willing to work but cannot find a job"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Austerity", "Cuts in government spending and rises in taxes to reduce a deficit"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in the interest rate could cause a recession</b>.", items: [
  "The central bank raises the interest rate",
  "Borrowing costs more and saving is rewarded",
  "Consumption and investment fall",
  "Aggregate demand shifts left",
  "Real GDP falls: recession",
], done: "A causal chain for a 6-mark answer." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP falls from $400bn to $380bn. What is the percentage change?", a: -5, sol: "(380 − 400) ÷ 400 × 100 = <b>−5%</b>." },
  { q: "Tax revenue is $80bn. In a recession it falls by 10%. What is the new tax revenue ($bn)?", a: 72, sol: "80 × 0.9 = <b>$72bn</b>." },
  { q: "The unemployment rate rises from 6% to 9%. The labour force is 30 million. How many more people are unemployed (millions)?", a: 0.9, sol: "3% × 30m = <b>0.9 million</b>." },
  { q: "A government spends $100bn and raises $85bn. In a recession revenue falls to $80bn and spending rises to $108bn. How big is the new deficit ($bn)?", a: 28, sol: "108 − 80 = <b>$28bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A recession is usually defined as:", opts: ["A fall in prices", "Two or more successive quarters of falling real GDP", "A rise in unemployment", "A fall in the exchange rate"], a: 1, why: "Real GDP falls for two quarters." },
  { q: "Which is a likely cause of a recession?", opts: ["A rise in consumer confidence", "A rise in interest rates leading to lower spending", "A rise in exports", "More investment"], a: 1, why: "Higher rates cut consumption and investment." },
  { q: "Which is a likely consequence of a recession for the government?", opts: ["Higher tax revenue", "Lower benefit spending", "A wider budget deficit", "Fewer borrowing needs"], a: 2, why: "Tax revenue falls and benefits rise." },
  { q: "Which could cause a recession by reducing the quantity of resources?", opts: ["A rise in consumer spending", "Large-scale emigration of workers", "More training", "Lower interest rates"], a: 1, why: "Fewer workers reduce capacity." },
  { q: "Automatic stabilisers help in a recession because:", opts: ["Taxes rise and benefits fall", "Benefits rise and tax revenue falls, supporting spending", "The exchange rate falls", "Interest rates rise"], a: 1, why: "They cushion the fall in demand." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Recession", "A fall in real GDP for two or more successive quarters."],
  ["Trough", "The lowest point of output in the business cycle."],
  ["Recovery", "Output rising again after a recession."],
  ["Total demand", "Aggregate demand: C + I + G + (X − M)."],
  ["Consumer confidence", "How optimistic households are about the future, which affects spending and borrowing."],
  ["Emigration", "People leaving a country to live elsewhere."],
  ["Automatic stabilisers", "Government spending and taxes that cushion falls in demand without new decisions."],
  ["Austerity", "Cuts in government spending and rises in taxes to reduce a deficit."],
  ["Unemployment", "People able and willing to work who cannot find a job."],
] });
labF();
