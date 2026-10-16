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
/* ---------- 5. fiscal policy on AD / AS ---------- */
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


/* tax cut vs spending rise */
function tsChart(s) {
  const base = 320, k = 8.5, rows = [["Spending rise $10bn", s.g, "--n"], ["Tax cut $10bn", s.t, "--accent"]];
  let o = SV.line(60, base, 700, base) + SV.text(60, 30, "First-round rise in AD ($bn)", "sm");
  rows.forEach(([n, v, col], i) => {
    const x = 160 + i * 260, h = v * k;
    o += SV.rect(x, base - h, 140, h, "", { style: `fill:var(${col})`, opacity: 0.85 }) + SV.text(x + 70, base - h - 8, v ? "$" + money(v, 0) + "bn" : "", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 70, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  if (s.note) o += SV.text(380, 60, s.note, "lbl bd t3", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 400, label: "A spending rise compared with a tax cut", base: { g: 0, t: 0, note: "" }, draw: tsChart, steps: [
  { cap: "The government has $10bn to use. First option: <b>raise its own spending</b> by $10bn.", s: { g: 0, t: 0, note: "" } },
  { cap: "All $10bn is <b>spent</b> on goods, services and workers, so AD rises by the full <b>$10bn</b> in the first round.", s: { g: 10, t: 0, note: "" } },
  { cap: "Second option: <b>cut taxes</b> by $10bn. Households keep the money, but they <b>save part</b> and spend part on imports.", s: { g: 10, t: 7, note: "" } },
  { cap: "In this example about <b>$7bn</b> is spent in the first round. A tax cut is slower and weaker at first, but gives people the choice and is easier to reverse.", s: { g: 10, t: 7, note: "Spending: bigger first effect" } },
] });
/* Lab 4: fiscal policy simulator. Shift in AD = change in G minus 0.7 x change in taxes (some of a tax change is saved). */
function labF() {
  if (!$("#fa") || !$("#fb")) return;
  const dG = +$("#fa").value, dT = +$("#fb").value, sh = dG - 0.7 * dT, [y, p] = solveAD(sh), bud = dT - dG;
  $("#fa1").textContent = money(y, 1) + (y > 50.5 ? " ▲" : y < 49.5 ? " ▼" : ""); $("#fa2").textContent = money(p, 1) + (p > 50.5 ? " ▲" : p < 49.5 ? " ▼" : "");
  $("#fa3").textContent = (bud >= 0 ? "+" : "−") + "$" + money(Math.abs(bud), 0) + "bn"; $("#fa4").textContent = sh > 1 ? "Expansionary" : sh < -1 ? "Contractionary" : "Neutral";
  let v;
  if (Math.abs(sh) < 1) v = "Spending and tax changes roughly cancel out, so aggregate demand hardly moves.";
  else if (sh > 0) v = `Aggregate demand shifts right. Real GDP rises by ${money(y - 50, 1)} and the price level by ${money(p - 50, 1)}. ${y > 61 ? "The economy is near full capacity, so a large share of the extra demand shows up as higher prices." : "Output rises by more than prices, so growth and employment are likely to benefit."} The initial effect on the budget is ${bud < 0 ? "a larger deficit" : "a smaller deficit"}.`;
  else v = `Aggregate demand shifts left. Real GDP falls by ${money(50 - y, 1)} and the price level by ${money(50 - p, 1)}. Inflationary pressure eases but jobs are at risk. The initial effect on the budget is ${bud > 0 ? "a smaller deficit" : "a larger deficit"}.`;
  $("#fv").textContent = v;
  $("#labF").innerHTML = adChart({ sh });
}
Lib.slider($("#g7"), { id: "fa", label: "Change in government spending", min: -20, max: 20, step: 1, value: 10, fmt: (v) => (v > 0 ? "+$" : v < 0 ? "−$" : "$") + Math.abs(v) + "bn", onInput: labF });
Lib.slider($("#g8"), { id: "fb", label: "Change in taxes (positive = tax rise)", min: -20, max: 20, step: 1, value: 0, fmt: (v) => (v > 0 ? "+$" : v < 0 ? "−$" : "$") + Math.abs(v) + "bn", onInput: labF });


const LV = [
  { n: "Cut income tax", s: "Expansionary", w: "Workers' disposable income rises, so consumption could rise.", g: "Workers and households; may encourage work.", c: "Part is saved. The deficit could widen and higher earners gain most in cash terms." },
  { n: "Raise income tax", s: "Contractionary", w: "Disposable income falls, so consumption could fall.", g: "Government: more revenue. Could help redistribute income if progressive.", c: "May discourage effort; AD and growth could slow." },
  { n: "Cut corporation tax", s: "Expansionary", w: "Firms keep more profit, which could raise investment and attract foreign firms.", g: "Firms and shareholders.", c: "Effect depends on firms' confidence; revenue may fall." },
  { n: "Cut VAT", s: "Expansionary", w: "Prices fall, so spending could rise; helps low-income households most.", g: "Consumers, especially the poor.", c: "Revenue falls; firms may not pass on the whole cut." },
  { n: "Raise spending on infrastructure", s: "Expansionary", w: "Direct rise in G with a multiplier effect; may also raise AS.", g: "Construction firms, workers, later all firms.", c: "Slow to start, large cost, borrowing needed." },
  { n: "Raise benefits", s: "Expansionary", w: "Low-income households spend most of it, so AD could rise fast.", g: "People on low incomes.", c: "Costly; may reduce the incentive to work if too generous." },
  { n: "Cut government spending", s: "Contractionary", w: "G falls, so AD falls; the deficit may narrow.", g: "Taxpayers (lower deficit, lower future taxes).", c: "Jobs and services may be lost; growth could slow." },
];
function showLV(i) {
  const p = LV[i];
  $("#lvBtns").innerHTML = LV.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#lvBtns .b").forEach((b) => (b.onclick = () => showLV(+b.dataset.j)));
  $("#lvOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Stance</th><th>How it works</th><th>Who gains</th><th>The catch</th></tr><tr><td><b>${p.s}</b></td><td>${p.w}</td><td>${p.g}</td><td>${p.c}</td></tr></table></div>`;
}
showLV(0);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a change in <b>taxes</b> or a change in <b>government spending</b>?", buckets: [{ label: "Change in taxes" }, { label: "Change in government spending" }], items: [
  { text: "Raise the rate of income tax", b: 0 }, { text: "Cut corporation tax", b: 0 }, { text: "Raise VAT", b: 0 }, { text: "Increase the tax-free allowance", b: 0 },
  { text: "Build a new motorway", b: 1 }, { text: "Increase old age pensions", b: 1 }, { text: "Cut public sector pay", b: 1 }, { text: "Increase spending on schools", b: 1 },
], done: "Syllabus 4.2.5: changes in taxes and changes in government spending." });
Lib.classify($("#cl2"), { prompt: "Which would be <b>expansionary</b> and which <b>contractionary</b> fiscal policy?", buckets: [{ label: "Expansionary" }, { label: "Contractionary" }], items: [
  { text: "Cut income tax rates", b: 0 }, { text: "Raise spending on roads and rail", b: 0 }, { text: "Raise the tax-free allowance", b: 0 }, { text: "Increase benefits for the unemployed", b: 0 },
  { text: "Cut government spending on education", b: 1 }, { text: "Raise VAT", b: 1 }, { text: "Raise corporation tax", b: 1 }, { text: "Freeze public sector pay and cut projects", b: 1 },
], done: "Expansionary raises AD; contractionary reduces it." });
Lib.order($("#o1"), { prompt: "Put the chain for <b>expansionary fiscal policy</b> in order.", items: [
  "The government cuts income tax rates",
  "Households' disposable income rises",
  "Consumption rises (and investment may follow)",
  "Aggregate demand shifts to the right",
  "Real GDP rises and firms take on more workers",
  "The price level may rise and the budget deficit may widen",
], done: "A full analysis chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A government cuts taxes by $20bn. Households save 30% of the tax cut. How much of the cut is spent ($bn)?", a: 14, sol: "70% of 20 = <b>$14bn</b>." },
  { q: "A government raises spending by $10bn and the multiplier is 3. What is the total rise in income ($bn)?", a: 30, sol: "3 × 10 = <b>$30bn</b>." },
  { q: "A worker earns $40,000, the tax-free allowance is $10,000 and the tax rate above it is 20%. The government raises the allowance to $12,000. How much less tax does she pay ($)?", a: 400, hint: "Only the extra allowance escapes tax.", sol: "Extra tax-free income = $2,000. 20% × 2,000 = <b>$400</b> less." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a likely effect of expansionary fiscal policy?", opts: ["AD shifts left", "Real GDP and employment are likely to rise", "The budget moves towards surplus", "The price level is certain to fall"], a: 1, why: "Higher spending or lower taxes raise AD, which tends to raise output and employment." },
  { q: "Why might a $10bn tax cut raise AD by less than $10bn of extra spending?", opts: ["Taxes are always saved", "Part of the tax cut may be saved or spent on imports", "Spending cannot raise AD", "Tax cuts reduce G"], a: 1, why: "Only the amount spent on domestic goods in the first round adds to AD." },
  { q: "Which measure is contractionary fiscal policy?", opts: ["Cut in corporation tax", "Increase in benefits", "Increase in VAT with lower spending", "Cut in income tax"], a: 2, why: "Both reduce AD." },
  { q: "A government wants to help low-income households quickly. Which measure is most likely to raise their spending most?", opts: ["Cut corporation tax", "Raise benefits", "Cut capital gains tax", "Cut inheritance tax"], a: 1, why: "Low-income households spend most of any extra income." },
  { q: "A cut in corporation tax is most likely to:", opts: ["Raise firms' costs", "Increase firms' after-tax profit and may encourage investment", "Reduce AD directly", "Raise imports"], a: 1, why: "Higher after-tax profit may be used to invest." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Fiscal policy", "Government spending and taxation decisions to influence AD"],
  ["Fiscal policy", "Decisions on government spending and taxation designed to influence aggregate demand."],
  ["Expansionary fiscal policy", "Rises in government spending and/or cuts in taxation designed to increase AD."],
  ["Contractionary fiscal policy", "Cuts in government spending and/or rises in taxation designed to reduce AD."],
  ["Income tax", "A tax on income from employment and investments, above a tax allowance."],
  ["Corporation tax", "A tax on the profits of firms."],
  ["Excise duty", "An indirect tax on certain goods such as alcohol, petrol and tobacco."],
  ["Tax allowance", "An amount of income that can be earned free of tax."],
  ["Multiplier effect", "Final change in AD is larger than the initial change"],
  ["Multiplier effect", "The final impact on aggregate demand is greater than the initial change."],
  ["Capital spending", "Government spending on assets such as roads, schools and hospitals."],
  ["Current spending", "Government spending on day-to-day items such as wages and services."],
  ["Subsidy", "Payment by the government to producers to lower their costs."],
] });
labF(); showLV(0);
