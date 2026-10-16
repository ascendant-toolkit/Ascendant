const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;

/* ---------- Watch 1: rounds ---------- */
const RC = 0.6, RB = 270, RH = (v) => v * 2.0;
function roundsDraw(s) {
  let o = SV.line(60, RB, 740, RB) + SV.text(62, 24, "New spending in each round ($m)", "sm");
  let v = 100, cum = 0;
  for (let i = 0; i < 8; i++) {
    const k = Math.max(0, Math.min(1, s.n - i)); cum += v;
    if (k > 0) o += SV.rect(90 + i * 80, RB - RH(v) * k, 56, RH(v) * k, "f1", op(k)) + SV.text(118 + i * 80, RB - RH(v) * k - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle", ...op(k) }) + SV.text(118 + i * 80, RB + 18, "round " + (i + 1), "sm", { "text-anchor": "middle", ...op(k) });
    v *= RC;
  }
  if (s.t > 0) o += SV.text(400, 70, "total approaches $250m = 100 × 1 ÷ (1 − 0.6)", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.t) });
  return o;
}
Lib.stepper($("#stR"), { w: 780, h: 310, label: "Rounds of spending after an injection of 100 million with a marginal propensity to consume of 0.6", base: { n: 0, t: 0 }, draw: roundsDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Round 1.</b> The injection of <b>$100m</b> is paid out as income to firms and workers.", s: { n: 1 } },
  { cap: "<b>Round 2.</b> They spend 60% of it (MPC = 0.6): <b>$60m</b> becomes income for other firms and workers. The rest leaks out as saving, taxes or imports.", s: { n: 2 } },
  { cap: "<b>Round 3.</b> $60m × 0.6 = <b>$36m</b> is spent again. Each round is 0.6 times the one before.", s: { n: 3 } },
  { cap: "<b>Later rounds</b> keep shrinking: $21.6m, $13m, $7.8m, $4.7m, $2.8m…", s: { n: 8 } },
  { cap: "<b>The total.</b> The rounds add up to <b>$250m</b>: the multiplier is 1 ÷ (1 − 0.6) = <b>2.5</b>, so national income rises by 2.5 times the injection.", s: { n: 8, t: 1 } },
] });

/* ---------- Watch 2: leakages ---------- */
function kDraw(s) {
  const B = 270, H = (v) => v * 0.38;
  let o = SV.line(60, B, 740, B) + SV.text(62, 24, "Rise in income from a $100m injection ($m)", "sm");
  [[110, 500, "f3", "MPS 0.2", "k = 5", s.a], [330, 333.3, "f1", "+ taxes (MRT 0.1)", "k = 3.3", s.b], [550, 250, "f2", "+ imports (MPM 0.1)", "k = 2.5", s.c]].forEach(([x, v, c, l, k, f]) => {
    if (f <= 0) return;
    o += SV.rect(x, B - H(v) * f, 100, H(v) * f, c, op(f)) + SV.text(x + 50, B - H(v) * f - 20, "$" + Lib.fmtN(v, 0) + "m", "lbl bd", { "text-anchor": "middle", ...op(f) }) + SV.text(x + 50, B - H(v) * f - 4, k, "sm bd", { "text-anchor": "middle", ...op(f) }) + SV.text(x + 50, B + 18, l, "sm", { "text-anchor": "middle", ...op(f) });
  });
  return o;
}
Lib.stepper($("#stK"), { w: 780, h: 310, label: "Rise in income from an injection of 100 million as taxes and imports are added to the leakages", base: { a: 0, b: 0, c: 0 }, draw: kDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Saving only.</b> With MPS = 0.2 and no taxes or imports, MPW = 0.2, so k = 1 ÷ 0.2 = <b>5</b>. A $100m injection raises income by <b>$500m</b>.", s: { a: 1 } },
  { cap: "<b>Add taxes.</b> A marginal rate of taxation of 0.1 raises MPW to 0.3, so k = 1 ÷ 0.3 = <b>3.3</b>. Income rises by <b>$333m</b>.", s: { a: 1, b: 1 } },
  { cap: "<b>Add imports.</b> A marginal propensity to import of 0.1 raises MPW to 0.4, so k = 1 ÷ 0.4 = <b>2.5</b>. Income rises by only <b>$250m</b>: every leakage shrinks the multiplier.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labMul() {
  if (!$("#ms") || !$("#mt") || !$("#mi") || !$("#mj")) return;
  const s = +$("#ms").value, t = +$("#mt").value, m = +$("#mi").value, J = +$("#mj").value, w = s + t + m, k = 1 / w, dy = k * J;
  $("#k1").textContent = Lib.fmtN(w, 2); $("#k2").textContent = Lib.fmtN(k, 2); $("#k3").textContent = "$" + Lib.fmtN(dy, 0) + "m";
  $("#kv").textContent = `MPW = ${Lib.fmtN(s, 2)} + ${Lib.fmtN(t, 2)} + ${Lib.fmtN(m, 2)} = ${Lib.fmtN(w, 2)}, so the multiplier is 1 ÷ ${Lib.fmtN(w, 2)} = ${Lib.fmtN(k, 2)}. An injection of $${J}m raises national income by $${Lib.fmtN(dy, 0)}m. Lower any of the three leakages and the multiplier rises.`;
  const H = (v) => v / 8, base = 200;
  let o = SV.line(30, base, 400, base);
  [[80, J, "f3", "Injection"], [240, dy, "f1", "Rise in income"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + Lib.fmtN(v, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ms", label: "Marginal propensity to save: ", min: 0.05, max: 0.5, step: 0.05, value: 0.2, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g2"), { id: "mt", label: "Marginal rate of taxation: ", min: 0, max: 0.4, step: 0.05, value: 0.1, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g3"), { id: "mi", label: "Marginal propensity to import: ", min: 0, max: 0.4, step: 0.05, value: 0.1, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g4"), { id: "mj", label: "Injection ($m): ", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labMul });

/* ---------- Lab 2 ---------- */
function labRnd() {
  if (!$("#rc") || !$("#rj")) return;
  const c = +$("#rc").value, J = +$("#rj").value, k = 1 / (1 - c), fin = k * J; let v = J, cum = 0; const vals = [];
  for (let i = 0; i < 10; i++) { vals.push(v); cum += v; if (i === 4) var c5 = cum; v *= c; }
  $("#r1").textContent = Lib.fmtN(k, 2); $("#r2").textContent = "$" + Lib.fmtN(fin, 0) + "m"; $("#r3").textContent = Math.round((c5 / fin) * 100) + "%";
  $("#rv").textContent = `With MPC = ${Lib.fmtN(c, 2)} the multiplier is ${Lib.fmtN(k, 2)}. After five rounds ${Math.round((c5 / fin) * 100)}% of the final $${Lib.fmtN(fin, 0)}m has been reached. A higher MPC means the rounds shrink more slowly, so the total is bigger and takes longer to arrive.`;
  const H = (x) => 190 * x / J, base = 230;
  let o = SV.line(30, base, 400, base);
  vals.forEach((x, i) => { o += SV.rect(40 + i * 36, base - H(x), 26, H(x), "f1") + SV.text(53 + i * 36, base + 14, i + 1, "sm", { "text-anchor": "middle" }); });
  o += SV.text(210, 270, "round", "sm", { "text-anchor": "middle" });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g5"), { id: "rc", label: "Marginal propensity to consume: ", min: 0.3, max: 0.9, step: 0.05, value: 0.6, fmt: (v) => Lib.fmtN(v, 2), onInput: labRnd });
Lib.slider($("#g6"), { id: "rj", label: "Injection ($m): ", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labRnd });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does each change raise or lower the value of the multiplier?",
  buckets: [{ label: "Raises the multiplier" }, { label: "Lowers the multiplier" }],
  items: [
    { text: "A higher marginal propensity to consume", b: 0 }, { text: "A lower marginal propensity to save", b: 0 }, { text: "A cut in the marginal rate of taxation", b: 0 }, { text: "A fall in the marginal propensity to import", b: 0 },
    { text: "A higher marginal propensity to save", b: 1 }, { text: "A rise in the marginal rate of taxation", b: 1 }, { text: "A rise in the marginal propensity to import", b: 1 }, { text: "More households saving windfall income", b: 1 },
  ], done: "Anything that increases leakages lowers the multiplier; anything that reduces them raises it.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Multiplier", "The change in national income divided by the initial change in injections"],
  ["Marginal propensity to consume (MPC)", "The share of an extra dollar of income that is spent"],
  ["Marginal propensity to save (MPS)", "The share of an extra dollar of income that is saved"],
  ["Marginal rate of taxation (MRT)", "The share of an extra dollar of income paid in tax"],
  ["Marginal propensity to import (MPM)", "The share of an extra dollar of income spent on imports"],
  ["Marginal propensity to withdraw (MPW)", "MPS + MRT + MPM: the share of extra income that leaks out"],
  ["Crowding out", "Government borrowing that raises interest rates and cuts private investment"],
], done: "Seven words for the multiplier." });
Lib.order($("#o1"), { prompt: "Put the multiplier process in order.", items: [
  "Injections rise, for example government spending increases by $100m",
  "The $100m becomes income for firms and workers",
  "They spend a share of it (the MPC) on other firms' output",
  "That spending becomes income for others, who spend part of it again",
  "Each round is smaller because of leakages into saving, taxes and imports",
  "National income rises by a multiple of the original injection",
], done: "Always mention the leakages that make each round smaller." });
Lib.calc($("#c1"), { qs: [
  { q: "In a closed economy with no government the MPC is 0.8. What is the multiplier?", a: 5, sol: "1 ÷ (1 − 0.8) = <b>5</b>." },
  { q: "An injection of $40m is made with a multiplier of 5. By how much does national income rise ($m)?", a: 200, sol: "5 × 40 = <b>$200m</b>." },
  { q: "The MPC is 0.6 in a closed economy with no government and investment rises by $100m. What is the rise in national income ($m)?", a: 250, sol: "1 ÷ 0.4 = 2.5; 2.5 × 100 = <b>$250m</b>." },
  { q: "MPS = 0.2, MRT = 0.2 and MPM = 0.1. What is the multiplier?", a: 2, sol: "MPW = 0.5, so k = 1 ÷ 0.5 = <b>2</b>." },
  { q: "In a closed economy MPS = 0.1 and MRT = 0.1. What is the rise in national income from an injection of $100m ($m)?", a: 500, sol: "MPW = 0.2, k = 5, rise = <b>$500m</b>." },
  { q: "Investment rises by $20bn and national income rises by $100bn. What is the multiplier?", a: 5, sol: "100 ÷ 20 = <b>5</b>." },
  { q: "Using that multiplier in a closed economy with no government, what is the MPC?", a: 0.8, tol: 0.01, sol: "k = 1 ÷ (1 − MPC) = 5 gives 1 − MPC = 0.2, so MPC = <b>0.8</b>." },
  { q: "A consumer's income rises from $1,000 to $1,200 and consumption rises from $800 to $900. What is the MPC?", a: 0.5, tol: 0.01, sol: "100 ÷ 200 = <b>0.5</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The multiplier is greater when:", opts: ["the marginal propensity to save is high", "the marginal propensity to import is low", "the marginal rate of taxation is high", "withdrawals are large"], a: 1, why: "Lower leakages mean more of each round is re-spent." },
  { q: "If MPC = 0.75 in a closed economy with no government the multiplier is:", opts: ["0.75", "1.33", "4", "7.5"], a: 2, why: "1 ÷ (1 − 0.75) = 4." },
  { q: "The multiplier effect works best when:", opts: ["the economy is at full employment", "there is spare capacity", "prices are rising fast", "imports are very high"], a: 1, why: "Unemployed resources allow output to rise rather than prices." },
  { q: "A rise in the rate of income tax will most likely:", opts: ["raise the multiplier", "lower the multiplier", "have no effect on the multiplier", "make MPC rise"], a: 1, why: "A higher marginal rate of taxation increases the leakage." },
  { q: "A fall in injections will:", opts: ["raise income by a multiple", "reduce income by a multiple", "not affect income", "raise the multiplier"], a: 1, why: "The multiplier works in both directions." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Multiplier", "The ratio of the change in national income to the change in injections that caused it."],
  ["k = 1 ÷ (1 − MPC)", "The multiplier in a closed economy with no government."],
  ["k = 1 ÷ MPW", "The multiplier with all leakages: MPW = MPS + MRT + MPM."],
  ["MPC", "The share of extra income that is spent."],
  ["MPS", "The share of extra income that is saved."],
  ["MRT", "Marginal rate of taxation: the share of extra income paid in tax."],
  ["MPM", "Marginal propensity to import: the share of extra income spent on imports."],
  ["ΔY = k × ΔJ", "The change in national income equals the multiplier times the change in injections."],
  ["Crowding out", "Government borrowing that pushes up interest rates and reduces private investment."],
  ["Multiplier in reverse", "A fall in injections reduces income by a multiple."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: '[Feb/March 2022 · 32 · Q27] In a closed economy with no government sector, the multiplier shows the impact of a change in', opts: ['consumption on investment.', 'investment on national income.', 'national income on consumption.', 'national income on investment.'], a: 1, why: 'The multiplier shows how a change in investment (an injection) changes national income.' },
  { q: '[Feb/March 2021 · 32 · Q24] In a closed economy, the marginal propensity to save is 0.1 and the marginal propensity to pay taxes is also 0.1. These values are constant. What will be the increase in national income if there is an injection of $100 million into the circular flow?', opts: ['$1000 million', '$500 million', '$100 million', '$80 million'], a: 1, why: 'MPW = 0.1 + 0.1 = 0.2, so the multiplier is 5 and income rises by 5 × $100m = $500m.' },
  { q: '[Oct/Nov 2020 · 33 · Q23] What reduces the value of the multiplier?', opts: ['an increase in government investment expenditure', 'an increase in consumption', 'an increase in the rate of taxation', 'an increase in the volume of exports'], a: 2, why: 'A higher tax rate increases a leakage. A, B and D increase injections or spending, not the size of the multiplier.' },
  { q: '[Oct/Nov 2020 · 32 · Q26] According to Keynesian theory, how will an increase in autonomous spending affect the value of equilibrium income?', opts: ['Income will increase by an amount equal to the value of autonomous spending.', 'Income will increase by an amount greater than the value of autonomous spending.', 'Income will increase by an amount smaller than the value of autonomous spending.', 'Income will not increase as a result of autonomous spending.'], a: 1, why: 'The multiplier effect means income rises by more than the initial spending.' },
  { q: '[May/June 2021 · 31 · Q24] What describes the multiplier process, as it operates within a closed economy with no government sector?', opts: ['Changes in National Income determine the level of investment.', 'The level of consumption depends on the level of National Income.', 'The levels of consumption and investment together determine the level of National Income.', 'When investment changes, there will be a greater change in equilibrium National Income.'], a: 3, why: 'The multiplier is the greater change in income that follows a change in investment.' },
  { q: '[Oct/Nov 2021 · 32 · Q25] In a closed economy with no government sector the marginal propensity to consume is 0.6 at all levels of income. There is an increase in private sector investment of $100 million. What will be the increase in national income?', opts: ['$60 million', '$100 million', '$166 million', '$250 million'], a: 3, why: 'k = 1 ÷ (1 − 0.6) = 2.5, so the rise in income is 2.5 × $100m = $250m.' },
  { q: '[May/June 2023 · 32 · Q21] Which condition will produce the highest value of the national income multiplier in an open economy with a government sector?', opts: ['high average and marginal tax rates', 'high marginal propensity to save', 'low level of autonomous consumption', 'low marginal propensity to import'], a: 3, why: 'A low marginal propensity to import means less of each round leaks abroad. High tax and saving rates reduce the multiplier.' },
  { q: '[May/June 2024 · 32 · Q19] Country X has a marginal propensity to consume (MPC) of 0.7. Its marginal propensity to save (MPS), marginal rate of taxation (MRT) and marginal propensity to import (MPM) are each 0.1. What is likely to lead to the biggest increase in the national income multiplier?', opts: ['a 5% increase in the MPC together with a 5% fall in the MRT', 'a 5% increase in the MPM together with a 5% fall in the MRT', 'a 5% increase in the MPS together with a 5% fall in the MPM', 'a 5% increase in the MRT together with a 5% fall in the MPS'], a: 0, why: 'Raising the MPC and cutting a leakage both raise the multiplier. B, C and D each add a leakage as well as cutting one.' },
  { q: '[Oct/Nov 2023 · 32 · Q17] The table shows MPC 0.5, MPS 0.2, MRT 0.2 and MPM 0.1 for a four-sector economy. What is the size of the multiplier?', opts: ['1', '2', '5', '10'], a: 1, why: 'MPW = 0.2 + 0.2 + 0.1 = 0.5, so the multiplier is 1 ÷ 0.5 = 2.' },
  { q: '[Feb/March 2025 · 32 · Q24] In an economy with unemployed resources the marginal propensity to consume is 0.2. The government increases its budget deficit and finances it by selling bonds to the non-bank private sector. What is the likely consequence of this?', opts: ['The currency will depreciate, increasing exports and reducing the trade deficit.', 'The increase in real output will be limited as the value of the multiplier is low.', 'The money supply will fall, leading to a reduction in aggregate demand.', 'There will be a decrease in the rate of interest, causing demand-pull inflation.'], a: 1, why: 'With an MPC of 0.2 the multiplier is only 1.25, so the rise in real output is small.' },
  { q: '[Feb/March 2020 · 32 · Q21] In a closed economy with no government sector, when will an increase in investment spending generate the largest increase in equilibrium national income?', opts: ['when households have a high level of autonomous consumption', 'when households have a high level of compulsory saving', 'when households have a high marginal propensity to consume', 'when households have a high marginal propensity to save'], a: 2, why: 'A high MPC means a high multiplier.' },
  { q: '[Oct/Nov 2021 · 31 · Q24] In a closed economy with no government there is an initial equilibrium national income of $500 billion. Households spend a constant fraction of every $1 of income. When investment increases by $20 billion national income moves to $600 billion. What is the marginal propensity to consume?', opts: ['0.20', '0.80', '0.83', '1.00'], a: 1, why: 'The multiplier is 100 ÷ 20 = 5, so MPS = 0.2 and MPC = 0.8.' },
] });
