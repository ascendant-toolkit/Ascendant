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

/* ---------- 45 degree diagram ---------- */
const GX0 = 80, GY0 = 340;
function gapDraw(cfg, s) {
  const mx = cfg.max, sc = 290 / mx, gx = (v) => GX0 + sc * v, gy = (v) => GY0 - sc * v;
  const A = cfg.A0 + (s.sh || 0) * cfg.dA, sl = cfg.s, Y = A / (1 - sl), AEF = A + sl * cfg.YF, gap = AEF - cfg.YF;
  let o = axes(GX0, GY0, GX0 + 330, GY0 - 305, "National income, Y", "Aggregate expenditure");
  o += SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) + 4, gy(mx) + 4, "45° line", "t3", 1);
  o += SV.line(gx(0), gy(A), gx(mx), gy(A + sl * mx), s.sh > 0.01 ? "c2" : "c1", { "stroke-width": 3 }) + tag(gx(mx) + 4, gy(A + sl * mx) + 4, "AE", s.sh > 0.01 ? "t2" : "t1", 1);
  if (s.yf > 0) o += SV.line(gx(cfg.YF), GY0, gx(cfg.YF), gy(mx), "c3 dash", op(s.yf)) + tag(gx(cfg.YF), GY0 + 22, "Yₚ", "t3", s.yf, "middle");
  if (s.eq > 0) o += SV.line(gx(Y), GY0, gx(Y), gy(Y), "c1 dash", op(s.eq)) + SV.circle(gx(Y), gy(Y), 6, "dot1", op(s.eq)) + tag(gx(Y), GY0 + 22, "Y", "t1", s.eq, "middle");
  if (s.gap > 0 && Math.abs(gap) > 0.5) { const c = gap < 0 ? "t2" : "t4"; o += SV.line(gx(cfg.YF), gy(cfg.YF), gx(cfg.YF), gy(AEF), "c2", { "stroke-width": 6, ...op(s.gap) }) + tag(gx(cfg.YF) + 10, (gy(cfg.YF) + gy(AEF)) / 2 + 5, gap < 0 ? "deflationary gap" : "inflationary gap", c, s.gap); }
  return o;
}
const DCFG = { max: 600, A0: 120, dA: 80, s: 0.6, YF: 500 }, ICFG = { max: 600, A0: 200, dA: -40, s: 0.6, YF: 400 };
$("#pic1").innerHTML = `<svg viewBox="0 0 760 400" role="img" aria-label="Keynesian 45 degree diagram: aggregate expenditure line crossing the 45 degree line at equilibrium income below full employment">${gapDraw(DCFG, { sh: 0, yf: 1, eq: 1, gap: 1 })}</svg>`;
function gapStepper(el, cfg, label, steps, base) { Lib.stepper(el, { w: 760, h: 400, label, base, draw: (s) => gapDraw(cfg, s), tween: 1100, dwell: 5600, steps }); }
gapStepper($("#stD"), DCFG, "AE line below full employment, deflationary gap closed by a rise in government spending", [
  { cap: "<b>The 45° line.</b> Every point has expenditure equal to income. Output settles only where AE meets this line.", s: { sh: 0 } },
  { cap: "<b>The AE line</b> starts at autonomous spending of 120 and slopes up with slope 0.6, because some of each extra dollar of income is spent on domestic output.", s: { sh: 0, eq: 0 } },
  { cap: "<b>Equilibrium.</b> The AE line meets the 45° line at Y = 120 ÷ (1 − 0.6) = <b>300</b>. At lower income AE is greater than output, so firms produce more. At higher income AE is less than output, so they cut back.", s: { sh: 0, eq: 1 } },
  { cap: "<b>Full employment</b> is at 500. The economy is 200 short of it.", s: { sh: 0, eq: 1, yf: 1 } },
  { cap: "<b>The deflationary gap.</b> At 500 AE is only 120 + 0.6 × 500 = 420, so AE is <b>80 short</b> of output. This vertical distance is the deflationary gap.", s: { sh: 0, eq: 1, yf: 1, gap: 1 } },
  { cap: "<b>Government spending rises by 80.</b> Autonomous spending is now 200 and the AE line shifts up. The multiplier is 1 ÷ 0.4 = 2.5, so income rises by 80 × 2.5 = <b>200</b>.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
  { cap: "<b>The gap is closed.</b> The new AE line cuts the 45° line at 500, the full employment level. The injection is the gap, 80, not the income shortfall of 200: the multiplier does the rest.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
], { sh: 0, eq: 0, yf: 0, gap: 0 });
gapStepper($("#stI"), ICFG, "AE line above full employment, inflationary gap closed by a cut in government spending", [
  { cap: "<b>Start.</b> Autonomous spending is 200 and the slope of AE is 0.6, so equilibrium is at 200 ÷ 0.4 = <b>500</b>.", s: { sh: 0, eq: 1 } },
  { cap: "<b>Full employment is only 400.</b> The economy cannot produce 500 in real terms, so extra demand cannot create extra output.", s: { sh: 0, eq: 1, yf: 1 } },
  { cap: "<b>The inflationary gap.</b> At 400 AE is 200 + 0.6 × 400 = 440, so AE is <b>40 above</b> output. This excess demand pulls up the price level.", s: { sh: 0, eq: 1, yf: 1, gap: 1 } },
  { cap: "<b>Government spending is cut by 40</b> (or taxes are raised enough to cut spending by 40). The AE line shifts down. Income falls by 40 × 2.5 = <b>100</b>.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
  { cap: "<b>The gap is closed.</b> The new AE line cuts the 45° line at 400. Inflationary pressure falls, though the cut could also reduce growth and jobs if it goes too far.", s: { sh: 1, eq: 1, yf: 1, gap: 0 } },
], { sh: 0, eq: 0, yf: 0, gap: 0 });

/* ---------- Lab 1 ---------- */
function labGap() {
  if (!$("#sa") || !$("#sc") || !$("#st") || !$("#sm") || !$("#sf")) return;
  const A = +$("#sa").value, c = +$("#sc").value / 100, t = +$("#st").value / 100, m = +$("#sm").value / 100, YF = +$("#sf").value;
  const sl = c * (1 - t) - m, k = 1 / (1 - sl), Y = A * k, AEF = A + sl * YF, gap = AEF - YF, need = (YF - Y) / k;
  $("#r1").textContent = Lib.fmtN(sl, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = (need >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(need), 0) + "bn";
  const kind = Math.abs(gap) < 0.5 ? "none" : gap < 0 ? "def" : "inf";
  $("#rv").textContent = kind === "none" ? "Equilibrium is at full employment, so there is no gap." : kind === "def" ?
    `Equilibrium income of $${Lib.fmtN(Y, 0)}bn is below full employment of $${YF}bn. There is a deflationary gap of $${Lib.fmtN(-gap, 0)}bn. Autonomous spending would have to rise by $${Lib.fmtN(need, 0)}bn, which the multiplier of ${Lib.fmtN(k, 2)} turns into a rise in income of $${Lib.fmtN(YF - Y, 0)}bn.` :
    `Equilibrium income of $${Lib.fmtN(Y, 0)}bn is above full employment of $${YF}bn. There is an inflationary gap of $${Lib.fmtN(gap, 0)}bn. Autonomous spending would have to fall by $${Lib.fmtN(-need, 0)}bn, cutting income by $${Lib.fmtN(Y - YF, 0)}bn through the multiplier.`;
  const mx = Math.max(Y, YF) * 1.2, sc = 290 / mx, gx = (v) => 70 + sc * v, gy = (v) => 330 - sc * v;
  let o = axes(70, 330, 400, 25, "National income", "Expenditure") + SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) - 4, gy(mx) + 14, "45°", "t3", 1, "end") + SV.line(gx(0), gy(A), gx(mx), gy(A + sl * mx), "c1", { "stroke-width": 3 }) + tag(gx(mx) - 4, gy(A + sl * mx) - 6, "AE", "t1", 1, "end");
  o += SV.line(gx(YF), 330, gx(YF), gy(YF), "c3 dash") + tag(gx(YF), 350, "Yₚ " + YF, "t3", 1, "middle") + SV.line(gx(Y), 330, gx(Y), gy(Y), "c1 dash") + SV.circle(gx(Y), gy(Y), 6, "dot1") + tag(gx(Y), 368, "Y " + Lib.fmtN(Y, 0), "t1", 1, "middle");
  if (kind !== "none") o += SV.line(gx(YF), gy(YF), gx(YF), gy(AEF), "c2", { "stroke-width": 6 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sa", label: "Autonomous spending ($bn) ", min: 50, max: 200, step: 10, value: 120, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g2"), { id: "sc", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g3"), { id: "st", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g4"), { id: "sm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g5"), { id: "sf", label: "Full employment income ($bn) ", min: 200, max: 800, step: 20, value: 500, fmt: (v) => v, onInput: labGap });
labGap();
btnTable("lbBtns", "lbOut", [
  ["Unemployment 11%, prices falling, firms have spare machines", "Deflationary gap", "AE at full employment is too low. Keynesian policy: more G, lower taxes, lower interest rates."],
  ["Labour shortages, inflation rising, imports surging", "Inflationary gap", "AE at full employment is too high. Policy: cut G, raise taxes or raise interest rates."],
  ["Output at potential, inflation on target, low unemployment", "No gap", "Equilibrium is at the full employment level of income."],
  ["A rise in the exchange rate cuts exports and raises imports in a boom", "Reduces an inflationary gap", "Net exports fall, so AE shifts down."],
  ["Business confidence collapses and investment falls", "Creates or widens a deflationary gap", "Autonomous investment falls, so AE shifts down and income falls by a multiple."]
], ["Situation", "What it is", "Why and policy"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which gap does each description fit?", buckets: [{"label": "Deflationary gap"}, {"label": "Inflationary gap"}], items: [{"text": "Spare capacity and rising unemployment", "b": 0}, {"text": "Excess demand pulling up prices", "b": 1}, {"text": "AE at full employment is less than full employment output", "b": 0}, {"text": "The AE line is above the 45° line at Yₚ", "b": 1}, {"text": "Keynesian solution is to cut government spending", "b": 1}, {"text": "Keynesian solution is to borrow and spend more", "b": 0}, {"text": "Japan's long period of low growth and weak prices", "b": 0}, {"text": "A boom with labour shortages and rising wages", "b": 1}], done: "Deflationary means too little expenditure; inflationary means too much." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Aggregate expenditure", "Planned spending at each level of national income (C + I + G + X − M)"], ["45° line", "Every point where expenditure equals income"], ["Full employment level of income", "The output when all resources are in use"], ["Deflationary gap", "AE at full employment falls short of full employment output"], ["Inflationary gap", "AE at full employment exceeds full employment output"], ["Autonomous spending", "Spending that does not vary with income; it shifts the AE line"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the closing of a deflationary gap in order, starting with the first event.", items: ["The government increases its spending and borrows to pay for it", "Aggregate expenditure shifts upwards", "Firms produce more and hire more workers", "Households with more income spend more again", "National income rises by a multiple until it reaches full employment"], done: "The multiplier makes the final change in income larger than the original rise in spending." });
Lib.calc($("#c1"), { qs: [
  {"q": "Equilibrium national income is $600bn, full employment income is $800bn and the multiplier is 4. By how much must autonomous spending change to reach full employment? Give the answer in $bn.", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Gap in income ÷ multiplier.", "sol": "(800 − 600) ÷ 4 = <b>$50bn</b> (an increase)."},
  {"q": "In a closed economy with no government, mpc = 0.75. Equilibrium income is $1,200bn and full employment income is $1,000bn. By how much must autonomous spending change? Use a minus sign for a fall.", "a": -50, "unit": "$bn", "tol": 0.01, "hint": "k = 1 ÷ (1 − 0.75) = 4. Income must fall by 200.", "sol": "k = 4. Change in AD = (1,000 − 1,200) ÷ 4 = <b>−$50bn</b> (an inflationary gap)."},
  {"q": "An open economy with a government has mps = 0.1, mrt = 0.1 and mpm = 0.2. Full employment income is $540bn and income is $465bn. By how much must government spending rise to reach full employment? Give the answer in $bn.", "a": 30, "unit": "$bn", "tol": 0.01, "hint": "k = 1 ÷ (mps + mrt + mpm). Income gap is 75.", "sol": "k = 1 ÷ 0.4 = 2.5. Change in G = 75 ÷ 2.5 = <b>$30bn</b>."},
  {"q": "The AE line is AE = 100 + 0.5Y. Calculate equilibrium income.", "a": 200, "unit": "$bn", "tol": 0.01, "hint": "Set Y = 100 + 0.5Y.", "sol": "0.5Y = 100, so Y = <b>200</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The AE line cuts the 45° line at a level of income above the full employment level. What exists?", opts: ["A deflationary gap", "An inflationary gap", "A budget surplus", "A trade deficit only"], a: 1, why: "AE at full employment exceeds output, which is an inflationary gap." },
  { q: "Which is the Keynesian solution to a deflationary gap?", opts: ["Cut government spending", "Raise income tax", "Raise government spending, financed by borrowing", "Raise interest rates"], a: 2, why: "More autonomous spending shifts AE up and the multiplier lifts income." },
  { q: "What does a movement along the AE line show?", opts: ["A change in autonomous spending", "A change in income, with autonomous spending unchanged", "A change in the multiplier", "A change in the price level"], a: 1, why: "A change in income moves the economy along the AE line; autonomous spending shifts the line." },
  { q: "The multiplier is 5 and a deflationary gap in income is $100bn. How much does AD have to rise?", opts: ["$5bn", "$20bn", "$100bn", "$500bn"], a: 1, why: "Required change in AD = 100 ÷ 5 = $20bn." },
  { q: "Why may a deflationary gap persist, according to Keynesians?", opts: ["Wages and prices adjust immediately", "Low confidence and sticky wages keep expenditure low", "The multiplier is zero", "The economy is always at full employment"], a: 1, why: "If wages and prices are slow to fall and confidence is weak, equilibrium can stay below full employment." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Aggregate expenditure", "Total planned spending at each level of income: C + I + G + (X − M)."],
  ["Equilibrium national income", "The income where AE equals output: the AE line crosses the 45° line."],
  ["Full employment level of income", "Potential output, when all resources are in use."],
  ["Deflationary gap", "AE at full employment is below full employment output; spare capacity and unemployment."],
  ["Inflationary gap", "AE at full employment is above full employment output; the excess demand pulls up the price level."],
  ["Autonomous spending", "Spending that does not depend on income; a change shifts the AE line."],
  ["Required change in AD", "(Y at full employment − equilibrium Y) ÷ multiplier."],
  ["Keynesian view", "The economy can settle below full employment, so government demand management is needed."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a closed economy with no government there is an equilibrium level of national income of $1000 billion. Households always spend 80% of the income they receive. Full employment occurs when national income is $1200 billion. By how much must aggregate demand initially change to close the deflationary gap? (Oct/Nov 2021 · 33 · Q26, reworded)", opts: ["−$200 billion", "−$40 billion", "+$40 billion", "+$200 billion"], a: 2, why: "Multiplier = 1 ÷ (1 − 0.8) = 5. Income must rise by $200bn, so AD must rise by 200 ÷ 5 = $40bn." },
  { q: "Which would be most likely to close an inflationary gap? (Practice, not a past paper question)", opts: ["A rise in government spending", "A cut in income tax", "A rise in the rate of interest", "An increase in the money supply"], a: 2, why: "A higher interest rate lowers consumption and investment, so AE falls. The other options raise AE." },
  { q: "An economy is in equilibrium where national income is below the full employment level. Which is most likely? (Practice, not a past paper question)", opts: ["Inflationary pressure and labour shortages", "A deflationary gap and unemployment", "A government budget surplus only", "Aggregate expenditure above output"], a: 1, why: "Equilibrium below full employment means AE at full employment is too low: a deflationary gap, with spare capacity and unemployment." },
] });
