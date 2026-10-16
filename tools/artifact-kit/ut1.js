/* ---------- data: pizza (single good) and X, Y (two goods, income $24, Py = $2) ---------- */
const TUp = [0, 20, 36, 48, 56, 60, 60, 56, 48];            // total utility of n slices
const MUp = (n) => TUp[n] - TUp[n - 1];
const MUX = [24, 20, 16, 12, 8, 4], MUY = [15, 12, 9, 6, 3, 1], INC = 24, PY = 2;
const cum = (a) => { let t = [0]; a.forEach((v) => t.push(t[t.length - 1] + v)); return t; };
const CX = cum(MUX), CY = cum(MUY);
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
function best(px) {
  let b = { x: 0, y: 0, tu: -1, spend: 0 };
  for (let x = 0; x <= 6; x++) for (let y = 0; y <= 6; y++) {
    const sp = px * x + PY * y; if (sp > INC) continue;
    const tu = CX[x] + CY[y];
    if (tu > b.tu || (tu === b.tu && sp > b.spend)) b = { x, y, tu, spend: sp };
  }
  return b;
}
const PRICES = [8, 6, 4, 3, 2, 1];

/* ---------- Learn: static TU and MU picture ---------- */
function utPanels(n) {
  const X1 = (k) => 60 + k * 38, Y1 = (v) => 330 - v * 4.2, X2 = (k) => 430 + k * 38, Y2 = (v) => 230 - v * 6.5, N = Math.max(0, Math.min(8, n)), f = Math.floor(N), fr = N - f;
  let o = SV.line(60, 330, 380, 330) + SV.line(60, 330, 60, 70) + SV.text(380, 367, "Slices", "sm", { "text-anchor": "end" }) + SV.text(60, 40, "Total utility", "lbl bd t1");
  o += SV.line(430, 230, 750, 230) + SV.line(430, 100, 430, 300) + SV.text(750, 367, "Slices", "sm", { "text-anchor": "end" }) + SV.text(430, 40, "Marginal utility", "lbl bd t4");
  for (let k = 1; k <= 8; k++) o += SV.text(X1(k), 348, k, "sm", { "text-anchor": "middle" }) + SV.text(X2(k), 330, k, "sm", { "text-anchor": "middle" });
  const pts = [[X1(0), Y1(0)]];
  for (let k = 1; k <= f; k++) pts.push([X1(k), Y1(TUp[k])]);
  if (f < 8 && fr > 0) pts.push([X1(f + fr), Y1(TUp[f] + (TUp[f + 1] - TUp[f]) * fr)]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  for (let k = 1; k <= f; k++) o += SV.circle(X1(k), Y1(TUp[k]), 5, "dot1");
  for (let k = 1; k <= 8; k++) {
    const v = k <= f ? 1 : k === f + 1 ? fr : 0; if (v <= 0) continue;
    const m = MUp(k), top = Math.min(Y2(m), 230), h = Math.abs(Y2(m) - 230);
    o += SV.rect(X2(k) - 15, top, 30, h, m >= 0 ? "f4" : "f2", op(v)) + SV.text(X2(k), m >= 0 ? top - 6 : top + h + 16, m, "lbl bd", { "text-anchor": "middle", ...op(v) });
  }
  if (N >= 5.9) o += SV.text(380, 58, "TU maximum when MU = 0", "lbl bd t3", { "text-anchor": "end" });
  if (N >= 7) o += SV.text(X1(7.6), Y1(48) + 36, "TU falls", "lbl bd t2", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 370" role="img" aria-label="Total utility rising then falling and marginal utility falling through zero to negative for slices of pizza">${utPanels(8)}</svg>`;

/* ---------- Watch 1: TU and MU ---------- */
Lib.stepper($("#stA"), { w: 760, h: 370, label: "Building total and marginal utility curves for slices of pizza", base: { n: 0 }, draw: (s) => utPanels(s.n), tween: 1200, dwell: 5200, steps: [
  { cap: "<b>The first slice</b> gives 20 utils. Total utility is 20 and marginal utility is 20.", s: { n: 1 } },
  { cap: "<b>Slices 2 and 3.</b> Total utility rises (36, 48) but marginal utility <b>falls</b> (16, 12). This is the <b>law of diminishing marginal utility</b>.", s: { n: 3 } },
  { cap: "<b>Slices 4 and 5.</b> TU still rises, <b>more slowly</b> (56, 60). MU is small (8, then 4) but still positive.", s: { n: 5 } },
  { cap: "<b>Slice 6.</b> MU = <b>0</b>. Total utility is at its <b>maximum</b> (60). A rational consumer who paid nothing might stop here.", s: { n: 6 } },
  { cap: "<b>Slices 7 and 8.</b> MU is <b>negative</b> (−4, −8) and total utility <b>falls</b>. Too much pizza makes things worse.", s: { n: 8 } },
] });

/* ---------- Lab 1: pizza ---------- */
function lab1() {
  if (!$("#n1")) return;
  const n = +$("#n1").value, tu = TUp[n], mu = n === 0 ? 0 : MUp(n), au = n === 0 ? 0 : tu / n;
  $("#r1").textContent = tu; $("#r2").textContent = n === 0 ? "–" : mu; $("#r3").textContent = n === 0 ? "–" : Lib.fmtN(au, 1);
  $("#rv").textContent = n === 0 ? "No slices yet. Total utility is zero."
    : mu > 0 ? `MU is positive (${mu}), so total utility is still rising. MU is smaller than for the last slice because of diminishing marginal utility.`
    : mu === 0 ? "MU = 0. Total utility is at its maximum. One more slice adds nothing."
    : `MU is negative (${mu}). Total utility is falling: this slice makes the person worse off.`;
  const X = (k) => 40 + k * 42, Y = (v) => 150 - v * 4;
  let o = SV.line(40, 150, 400, 150) + SV.text(396, 168, "Slices", "sm", { "text-anchor": "end" });
  for (let k = 1; k <= 8; k++) { const m = MUp(k), on = k <= n; o += SV.rect(X(k) - 14, Math.min(Y(m), 150), 28, Math.abs(Y(m) - 150), m >= 0 ? "f4" : "f2", op(on ? 1 : 0.2)) + SV.text(X(k), 266, k, "sm", { "text-anchor": "middle" }); }
  o += SV.text(44, 24, "Bars: marginal utility. Line: total utility (lower).", "sm");
  const base = 262; const ptsT = []; for (let k = 0; k <= n; k++) ptsT.push([X(k), base - TUp[k] * 0.5]);
  if (ptsT.length > 1) o += SV.path(Lib.ptsPath(ptsT), "c1"); if (n > 0) o += SV.circle(X(n), base - TUp[n] * 0.5, 6, "dot1");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "n1", label: "Slices eaten: ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: lab1 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each statement in the right bucket.",
  buckets: [{ label: "MU positive: TU rises" }, { label: "MU = 0: TU maximum" }, { label: "MU negative: TU falls" }],
  items: [
    { text: "The 2nd slice adds 16 utils", b: 0 }, { text: "The first sip of water after a run", b: 0 }, { text: "TU rises, but at a decreasing rate", b: 0 },
    { text: "The 6th slice adds nothing", b: 1 }, { text: "The consumer would not pay for another unit", b: 1 }, { text: "The point where TU stops rising", b: 1 },
    { text: "The 7th slice makes the person feel ill", b: 2 }, { text: "TU is falling as more is consumed", b: 2 },
  ], done: "Positive MU: TU rises. Zero MU: TU peaks. Negative MU: TU falls.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Utility", "The satisfaction a consumer gets from consuming a good"],
  ["Total utility", "All the satisfaction from a given quantity"],
  ["Marginal utility", "The extra satisfaction from one more unit"],
  ["Diminishing marginal utility", "Each extra unit adds less satisfaction than the one before"],
  ["Util", "An imaginary unit used to measure utility"],
  ["Paradox of value", "Water is cheap and diamonds dear because price follows marginal, not total, utility"],
], done: "Six words for the building blocks." });
Lib.calc($("#c1"), { qs: [
  { q: "Total utility is 36 for 2 units and 48 for 3 units. What is the marginal utility of the 3rd unit?", a: 12, sol: "48 − 36 = <b>12</b>." },
  { q: "The marginal utilities of 4 successive units are 20, 16, 12 and 8. What is the total utility of 4 units?", a: 56, sol: "20 + 16 + 12 + 8 = <b>56</b>." },
  { q: "Total utility from 5 units is 60. What is the average utility?", a: 12, sol: "60 ÷ 5 = <b>12</b>." },
  { q: "The marginal utilities of the 1st, 2nd and 3rd slices are 20, 16 and 12. What is the total utility of 3 slices?", a: 48, sol: "20 + 16 + 12 = <b>48</b>." },
  { q: "Total utility is 60 at 5 slices and 60 at 6 slices. What is the marginal utility of the 6th slice?", a: 0, sol: "60 − 60 = <b>0</b>: total utility is at its maximum." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "When marginal utility is zero, total utility is:", opts: ["at its maximum", "at its minimum", "negative", "rising at an increasing rate"], a: 0, why: "Another unit adds nothing, so total utility has stopped rising." },
  { q: "The law of diminishing marginal utility says that as a consumer consumes more of a good:", opts: ["total utility falls at once", "each extra unit adds less utility than the last", "price must fall", "marginal utility rises"], a: 1, why: "MU falls as consumption rises. Total utility can still rise while MU is positive." },
  { q: "Marginal utility is negative. Total utility is:", opts: ["rising", "falling", "at its maximum", "zero"], a: 1, why: "A negative MU means the extra unit reduces total satisfaction." },
  { q: "Water is cheap but diamonds are dear because:", opts: ["water has no utility", "price depends on marginal utility, which is low for plentiful water", "diamonds have higher total utility", "demand for water is zero"], a: 1, why: "The MU of one more unit of a plentiful good is low." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Utility", "The satisfaction a consumer gets from consuming a good or service."],
  ["Total utility (TU)", "The total satisfaction from consuming a given quantity of a good."],
  ["Marginal utility (MU)", "The additional satisfaction from consuming one more unit."],
  ["Diminishing marginal utility", "The extra satisfaction from each additional unit falls as consumption rises."],
  ["When MU is zero", "Total utility is at its maximum."],
  ["When MU is negative", "Total utility is falling."],
  ["Util", "An imaginary unit used to measure utility."],
  ["Paradox of value", "Water is cheap and diamonds dear because price depends on marginal, not total, utility."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 31 · Q4] What is the central principle of marginal utility theory?", opts: ["As more is consumed of a normal good, the additional satisfaction gained increases.", "Consumers are in equilibrium when the marginal utility gained from good X equals the price of good Y.", "Consumers are in equilibrium when the ratio of the marginal utility of goods X and Y are equal to the ratio of their prices.", "Consumers are in equilibrium when the total utility gained from good X is the same as gained from good Y."], a: 2, why: "MUx ÷ MUy = Px ÷ Py, the same as MUx ÷ Px = MUy ÷ Py." },
  { q: "[May/June 2024 · 31 · Q1] Which statement about the concept of utility is correct?", opts: ["Diminishing marginal utility means that producers become less efficient the more they produce.", "If marginal utility is above average utility, average utility must be rising.", "The equi-marginal principle says that a consumer gets equal total satisfaction from each item purchased.", "Total utility continually rises as the level of consumption rises."], a: 1, why: "Like any marginal and average pair, if the marginal is above the average, the average rises. A confuses utility with productivity, C mixes up total satisfaction with MU per dollar, D ignores negative MU." },
  { q: "[Oct/Nov 2023 · 31 · Q1] Economists normally assume that the marginal utility from consuming additional goods is positive and diminishing. What is the effect on total satisfaction of consuming extra units of the good?", opts: ["Total satisfaction falls at a decreasing rate.", "Total satisfaction falls at an increasing rate.", "Total satisfaction rises at a decreasing rate.", "Total satisfaction rises at an increasing rate."], a: 2, why: "Positive MU means TU rises; diminishing MU means it rises more slowly." },
  { q: "[May/June 2021 · 31 · Q5] Which act of purchase or consumption is most likely to illustrate the law of diminishing marginal utility?", opts: ["the final course of an 'eat all you can' banquet to end an evening out", "the last coin to complete an enthusiast's coin collection", "the second of the two rolls of wallpaper needed to decorate a room", "the tenth driving lesson needed to enable a learner to pass the driving test"], a: 0, why: "The last course at a banquet adds little to the diner's satisfaction. B, C and D are cases where the last unit completes a set or a need." },
  { q: "[May/June 2024 · 32 · Q1] A table shows total utility from bottles of water: 1 bottle 30, 2 bottles 40, 3 bottles 48, 4 bottles 54, 5 bottles 58. What can be concluded?", opts: ["Marginal utility increases as consumption increases.", "The consumer cannot switch expenditure to another product to increase total utility.", "The marginal utility of the 3rd unit is 8.", "The marginal utility of the 5th unit is 2."], a: 2, why: "MU of the 3rd unit = 48 − 40 = 8. MU of the 5th is 58 − 54 = 4, and MU falls as consumption rises." },
] });
