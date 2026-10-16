const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;

/* ---------- Watch 1: consumption function ---------- */
const CXs = (y) => 70 + y * 0.85, CYs = (v) => 330 - v * 0.42;
function consDraw(s) {
  let o = SV.line(70, 330, 760, 330) + SV.line(70, 330, 70, 30) + SV.text(760, 370, "Disposable income Y", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Consumption C", "sm");
  [0, 200, 400, 600, 800].forEach((y) => { o += SV.text(CXs(y), 346, y, "sm", { "text-anchor": "middle" }); });
  if (s.l > 0) o += SV.line(CXs(0), CYs(0), CXs(700), CYs(700), "gr", { "stroke-dasharray": "5 5", ...op(s.l) }) + SV.text(CXs(700) - 4, CYs(700) + 18, "C = Y", "sm bd", { "text-anchor": "end", ...halo, ...op(s.l) });
  if (s.c > 0) o += SV.line(CXs(0), CYs(100), CXs(800), CYs(700), "c1", op(s.c)) + SV.text(CXs(800) - 4, CYs(700) - 10, "C = 100 + 0.75Y", "lbl bd t1", { "text-anchor": "end", ...halo, ...op(s.c) });
  if (s.a > 0) o += SV.circle(CXs(0), CYs(100), 6, "dot3", op(s.a)) + SV.text(CXs(0) + 12, CYs(100) - 8, "autonomous consumption = 100", "lbl bd t3", { ...halo, ...op(s.a) });
  if (s.b > 0) o += SV.line(CXs(400), CYs(400), CXs(400), 330, "gr", op(s.b)) + SV.circle(CXs(400), CYs(400), 7, "dot2", op(s.b)) + SV.text(CXs(400), 372, "Y = 400: C = Y, saving = 0", "lbl bd t2", { "text-anchor": "middle", ...op(s.b) });
  if (s.m > 0) o += SV.line(CXs(600), CYs(550), CXs(800), CYs(550), "c4", { "stroke-width": 3, ...op(s.m) }) + SV.line(CXs(800), CYs(550), CXs(800), CYs(700), "c4", { "stroke-width": 3, ...op(s.m) }) + SV.text(CXs(700), CYs(550) + 18, "ΔY = 200", "sm bd t4", { "text-anchor": "middle", ...halo, ...op(s.m) }) + SV.text(CXs(800) + 6, CYs(625), "ΔC = 150", "sm bd t4", { ...halo, ...op(s.m) });
  return o;
}
Lib.stepper($("#stC"), { w: 780, h: 385, label: "Consumption function C equals 100 plus 0.75 Y with the 45 degree line", base: { l: 0, c: 0, a: 0, b: 0, m: 0 }, draw: consDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The 45° line.</b> Points on C = Y show consumption equal to income, so saving is zero.", s: { l: 1 } },
  { cap: "<b>The consumption function.</b> C = 100 + 0.75Y slopes up: more income, more consumption, but less than one-for-one.", s: { l: 1, c: 1 } },
  { cap: "<b>Autonomous consumption.</b> The intercept (100) is spending that does not depend on income: it is funded by savings or borrowing at low incomes.", s: { l: 1, c: 1, a: 1 } },
  { cap: "<b>Break-even income.</b> Where the function crosses the 45° line (Y = 400) households spend all their income. Below it they dissave; above it they save.", s: { l: 1, c: 1, a: 1, b: 1 } },
  { cap: "<b>The MPC.</b> The slope is the marginal propensity to consume: when income rises by 200 consumption rises by 150, so <b>MPC = 150 ÷ 200 = 0.75</b>, and MPS = 0.25.", s: { l: 1, c: 1, a: 0.4, b: 0.4, m: 1 } },
] });

/* ---------- Watch 2: accelerator ---------- */
const AY = [100, 110, 125, 135, 140, 140];
function accDraw(s) {
  let o = SV.line(60, 150, 740, 150) + SV.text(62, 24, "National income", "sm") + SV.line(60, 340, 740, 340) + SV.text(62, 196, "Investment = 2 × change in income", "sm");
  AY.forEach((y, i) => {
    const k = Math.max(0, Math.min(1, s.n - i)), x = 90 + i * 108; if (k <= 0) return;
    o += SV.rect(x, 150 - y * 0.8 * k, 56, y * 0.8 * k, "f1", op(k)) + SV.text(x + 28, 150 - y * 0.8 * k - 6, y, "sm bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 28, 168, "year " + (i + 1), "sm", { "text-anchor": "middle", ...op(k) });
    if (i > 0) { const inv = 2 * (y - AY[i - 1]); o += SV.rect(x, 340 - inv * 3 * k, 56, inv * 3 * k, inv >= (i > 1 ? 2 * (AY[i - 1] - AY[i - 2]) : 0) ? "f3" : "f2", op(k)) + SV.text(x + 28, 340 - inv * 3 * k - 6, inv, "sm bd", { "text-anchor": "middle", ...op(k) }); }
  });
  if (s.f > 0) o += SV.text(560, 232, "income still rising, investment falls", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.f) });
  return o;
}
Lib.stepper($("#stA"), { w: 780, h: 365, label: "National income growing by smaller amounts and the investment that follows from the accelerator", base: { n: 0, f: 0 }, draw: accDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Year 1.</b> National income is 100 and there is no change yet, so no net investment is needed.", s: { n: 1 } },
  { cap: "<b>Year 2.</b> Income rises by 10 to 110. With an accelerator of 2, firms need 20 of extra capital: <b>investment = 20</b>.", s: { n: 2 } },
  { cap: "<b>Year 3.</b> Income rises by 15 to 125, a faster rise, so <b>investment rises to 30</b>.", s: { n: 3 } },
  { cap: "<b>Year 4.</b> Income rises by only 10 to 135. Investment falls to <b>20</b> even though income is still rising.", s: { n: 4, f: 1 } },
  { cap: "<b>Years 5 and 6.</b> Growth slows to 5 and then 0, so investment falls to 10 and then 0. A slowdown in growth can cut investment (an injection) sharply.", s: { n: 6, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labCons() {
  if (!$("#ca") || !$("#cc") || !$("#cy")) return;
  const a = +$("#ca").value, c = +$("#cc").value, y = +$("#cy").value, C = a + c * y, S = y - C, F = { x: (v) => 40 + v * 0.42, y: (v) => 270 - v * 0.34 };
  $("#c1r").textContent = "$" + Lib.fmtN(C, 0); $("#c2r").textContent = (S < 0 ? "−$" : "$") + Lib.fmtN(Math.abs(S), 0); $("#c3r").textContent = y ? Lib.fmtN(C / y, 2) : "–"; $("#c4r").textContent = Lib.fmtN(c, 2);
  $("#cv").textContent = S < -0.5 ? `At income $${y} consumption ($${Lib.fmtN(C, 0)}) is above income, so households dissave $${Lib.fmtN(-S, 0)} (APC is above 1).` : S > 0.5 ? `At income $${y} households consume $${Lib.fmtN(C, 0)} and save $${Lib.fmtN(S, 0)}. The APC (${Lib.fmtN(C / y, 2)}) is below 1, while the MPC stays at ${Lib.fmtN(c, 2)}.` : `At income $${y} consumption equals income: break-even, saving is zero.`;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Income Y", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "C", "sm");
  o += SV.line(F.x(0), F.y(0), F.x(800), F.y(800), "gr", { "stroke-dasharray": "5 5" }) + SV.line(F.x(0), F.y(a), F.x(800), F.y(a + c * 800), "c1") + SV.line(F.x(y), F.y(C), F.x(y), 270, "gr") + SV.circle(F.x(y), F.y(C), 6, "dot1") + SV.text(F.x(800) - 4, F.y(800) + 16, "C = Y", "sm bd", { "text-anchor": "end" }) + SV.text(F.x(y), 288, y, "sm bd", { "text-anchor": "middle" });
  $("#labN").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ca", label: "Autonomous consumption a ($): ", min: 0, max: 200, step: 20, value: 100, fmt: (v) => v, onInput: labCons });
Lib.slider($("#g2"), { id: "cc", label: "Marginal propensity to consume c: ", min: 0.5, max: 0.95, step: 0.05, value: 0.75, fmt: (v) => Lib.fmtN(v, 2), onInput: labCons });
Lib.slider($("#g3"), { id: "cy", label: "Disposable income Y ($): ", min: 0, max: 800, step: 50, value: 400, fmt: (v) => v, onInput: labCons });

/* ---------- Lab 2 ---------- */
function labAcc() {
  if (!$("#v2") || !$("#v3") || !$("#v4") || !$("#vv")) return;
  const g = [+$("#v2").value / 100, +$("#v3").value / 100, +$("#v4").value / 100], v = +$("#vv").value, y = [100]; g.forEach((r) => y.push(y[y.length - 1] * (1 + r)));
  const inv = [1, 2, 3].map((i) => v * (y[i] - y[i - 1]));
  $("#a1").textContent = "$" + Lib.fmtN(inv[0], 1); $("#a2").textContent = "$" + Lib.fmtN(inv[1], 1); $("#a3").textContent = "$" + Lib.fmtN(inv[2], 1);
  const fall = inv[2] < inv[1] - 0.05 && y[3] > y[2], fall2 = inv[1] < inv[0] - 0.05 && y[2] > y[1];
  $("#av").textContent = fall || fall2 ? `Income is still rising, but investment falls (${Lib.fmtN(inv[fall2 && !fall ? 0 : 1], 1)} to ${Lib.fmtN(inv[fall2 && !fall ? 1 : 2], 1)}) because the increase in income is smaller than the year before: the accelerator.` : "Investment follows the change in income. Lower the growth rate in a later year to see investment fall while income is still rising.";
  const base = 240;
  let o = SV.line(30, base, 400, base);
  y.forEach((val, i) => { const x = 50 + i * 85; o += SV.rect(x, base - val * 0.8, 28, val * 0.8, "f1") + SV.text(x + 14, base - val * 0.8 - 6, Lib.fmtN(val, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(x + 14, base + 14, "Y" + (i + 1), "sm", { "text-anchor": "middle" }); if (i > 0) { const h = Math.max(0, inv[i - 1]) * 2; o += SV.rect(x + 32, base - h, 28, h, "f3") + SV.text(x + 46, base - h - 6, Lib.fmtN(inv[i - 1], 0), "sm bd t3", { "text-anchor": "middle" }); } });
  o += SV.text(210, 268, "blue: national income · green: investment", "sm", { "text-anchor": "middle" });
  $("#labO").innerHTML = o;
}
Lib.slider($("#g4"), { id: "v2", label: "Growth in year 2: ", min: -2, max: 20, step: 1, value: 10, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g5"), { id: "v3", label: "Growth in year 3: ", min: -2, max: 20, step: 1, value: 14, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g6"), { id: "v4", label: "Growth in year 4: ", min: -2, max: 20, step: 1, value: 8, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g7"), { id: "vv", label: "Accelerator v (capital-output ratio): ", min: 1, max: 4, step: 0.5, value: 2, fmt: (v) => Lib.fmtN(v, 1), onInput: labAcc });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does each change move households along the consumption function or shift it?",
  buckets: [{ label: "Movement along the function" }, { label: "Shift of the function" }],
  items: [
    { text: "A rise in disposable income from a pay rise", b: 0 }, { text: "A fall in disposable income after a tax rise", b: 0 },
    { text: "A rise in house prices (wealth)", b: 1 }, { text: "Households become more confident about jobs", b: 1 }, { text: "Credit becomes easier to get", b: 1 }, { text: "A fall in interest rates that discourages saving", b: 1 }, { text: "Fear of a recession raises saving at every income", b: 1 },
  ], done: "Income changes move you along the function; everything else shifts it.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Consumption function", "The relationship between consumption and disposable income: C = a + cY"],
  ["Autonomous consumption", "Spending that does not depend on current income"],
  ["Marginal propensity to consume", "The share of an extra dollar of income that is spent"],
  ["Average propensity to consume", "Consumption divided by income"],
  ["Wealth effect", "A change in consumption caused by a change in the value of assets"],
  ["Accelerator principle", "Investment depends on the rate of change of national income"],
  ["Capital-output ratio", "The amount of capital needed to produce a unit of output (the accelerator)"],
], done: "Seven words for consumption and investment." });
Lib.order($("#o1"), { prompt: "Put the accelerator chain in order.", items: [
  "Demand and national income grow",
  "Firms need more capital to meet the extra output",
  "Investment rises by the accelerator times the change in income",
  "National income continues to rise, but by less",
  "The change in income falls, so the extra capital needed falls",
  "Investment falls, reducing aggregate demand even though income is still rising",
], done: "The key point is the rate of change of income." });
Lib.calc($("#c1"), { qs: [
  { q: "Consumption is C = 100 + 0.75Y. What is consumption when income is $600?", a: 550, sol: "100 + 0.75 × 600 = <b>$550</b>." },
  { q: "What is saving at income $600 ($)?", a: 50, sol: "600 − 550 = <b>$50</b>." },
  { q: "What is the average propensity to consume at income $600 (2 decimal places)?", a: 0.92, tol: 0.01, sol: "550 ÷ 600 = <b>0.92</b>." },
  { q: "Income rises from $1,000 to $1,200 and consumption rises from $800 to $900. What is the MPC?", a: 0.5, tol: 0.01, sol: "100 ÷ 200 = <b>0.5</b>." },
  { q: "The MPC is 0.8. What is the MPS?", a: 0.2, tol: 0.01, sol: "1 − 0.8 = <b>0.2</b>." },
  { q: "The accelerator is 3. National income rises by $20m. What is the investment ($m)?", a: 60, sol: "3 × 20 = <b>$60m</b>." },
  { q: "Income rises by $20m in one year and by $15m the next. With an accelerator of 3, by how much does investment fall ($m)?", a: 15, sol: "Investment falls from 60 to 45: a fall of <b>$15m</b>, although income is still rising." },
  { q: "A consumer's income is $1,000 and she spends 80% of it. What is her average propensity to consume?", a: 0.8, tol: 0.01, sol: "800 ÷ 1,000 = <b>0.8</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The marginal propensity to consume is:", opts: ["total consumption ÷ total income", "the change in consumption ÷ the change in income", "income − saving", "saving ÷ income"], a: 1, why: "It is about extra income, not total income." },
  { q: "An increase in house prices is most likely to:", opts: ["move households along the consumption function", "shift the consumption function upwards", "reduce the MPC to zero", "have no effect"], a: 1, why: "A wealth effect raises consumption at every income." },
  { q: "According to the accelerator principle, investment will fall when:", opts: ["income falls only", "the rate of growth of income falls", "income rises at a constant rate", "interest rates fall"], a: 1, why: "Investment depends on the rate of change of income." },
  { q: "If MPC = 0.9, then MPS =", opts: ["0.1", "0.9", "1.9", "0.09"], a: 0, why: "MPC + MPS = 1." },
  { q: "A rise in saving that is not matched by a rise in investment will probably:", opts: ["raise national income", "lower national income", "not affect national income", "raise the multiplier"], a: 1, why: "Withdrawals exceed injections, so income falls." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Consumption function", "C = a + cY: consumption depends on disposable income."],
  ["Autonomous consumption", "Spending that does not depend on current income (the intercept a)."],
  ["MPC", "Change in consumption ÷ change in income."],
  ["APC", "Consumption ÷ income."],
  ["MPS", "Change in saving ÷ change in income; MPC + MPS = 1."],
  ["Wealth effect", "A rise in asset values raises consumption."],
  ["Accelerator principle", "Investment depends on the rate of change of national income."],
  ["Investment determinants", "Interest rates, expected profit, confidence, spare capacity and technology."],
  ["Paradox of thrift", "If everyone saves more, income may fall and total saving may not rise."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: '[Feb/March 2023 · 32 · Q21] What does the accelerator principle state?', opts: ['Consumption is a function of the rate of change of income.', 'Income is a function of the rate of change of investment.', 'Investment is a function of the rate of change of income.', 'Investment is a function of the rate of interest.'], a: 2, why: 'The accelerator links investment to the rate of change of income.' },
  { q: '[May/June 2020 (not sat) · 31 · Q24] What does the accelerator principle explain?', opts: ['how changes in consumption lead to changes in income', 'how changes in income lead to changes in consumption', 'how changes in income lead to changes in investment', 'how changes in investment lead to changes in income'], a: 2, why: 'The accelerator explains how changes in income lead to changes in investment. Option D is the multiplier.' },
  { q: '[Feb/March 2025 · 32 · Q15] What does the accelerator principle explain?', opts: ['how changes in consumption lead to changes in income', 'how changes in income lead to changes in consumption', 'how changes in income lead to changes in investment', 'how changes in investment lead to changes in income'], a: 2, why: 'Income changes lead to changes in investment through the accelerator.' },
  { q: '[Oct/Nov 2020 · 31 · Q24] According to the accelerator theory, what would cause investment in an economy to be lower than in the previous year?', opts: ['a lower marginal propensity to consume than in the previous year', 'a lower marginal propensity to save than in the previous year', 'a smaller fall in national income than occurred in the previous year', 'a smaller rise in national income than occurred in the previous year'], a: 3, why: 'A smaller rise in income means a smaller change in income, so investment falls.' },
  { q: '[Oct/Nov 2023 · 33 · Q21] What, according to the accelerator principle, will cause the level of investment to fall?', opts: ['a decrease in confidence', 'a decrease in the rate of growth of national income', 'an increase in the price of capital equipment', 'an increase in the rate of interest'], a: 1, why: 'The accelerator principle is about the rate of growth of national income. The other options are real influences, but not part of the accelerator.' },
  { q: '[Oct/Nov 2023 · 31 · Q22] What is the basic assumption underlying the accelerator theory?', opts: ['Investment depends on the level of business confidence.', 'Investment depends on the level of savings.', 'Investment depends on the rate of change in national income.', 'Investment depends on the rate of change of interest rates.'], a: 2, why: 'Investment depends on the rate of change of national income.' },
  { q: '[Oct/Nov 2024 · 31 · Q19] A consumer has an income of $1000 per week and spends 80% of this. After income rises to $1200 per week, consumption increases to $900 per week. Which statement is correct?', opts: ['The average propensity to consume does not change.', 'The initial average propensity to consume is 5.', 'The marginal propensity to consume is 0.5.', 'The marginal propensity to consume is 2.'], a: 2, why: 'The MPC is the change in consumption (900 − 800 = 100) divided by the change in income (200) = 0.5. The APC falls from 0.8 to 0.75.' },
] });
