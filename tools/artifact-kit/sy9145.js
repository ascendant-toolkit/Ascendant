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

/* ---------- the 45 degree diagram ---------- */
const E0 = 80, F0 = 345, SC = 0.43, MX = 700, px = (v) => E0 + SC * v, py = (v) => F0 - SC * v, SL = 0.6;
const tickSet = (gx, gy, x0, y0, xm, ym, step, grid) => { let o = ""; for (let v = 0; v <= xm + 0.001; v += step) { if (grid && v > 0) o += SV.line(gx(v), y0, gx(v), gy(ym), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(gx(v), y0, gx(v), y0 + 5, "", {}) + SV.text(gx(v), y0 + 18, v, "sm", { "text-anchor": "middle" }); }
  for (let v = step; v <= ym + 0.001; v += step) { if (grid) o += SV.line(x0, gy(v), gx(xm), gy(v), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(x0 - 5, gy(v), x0, gy(v), "", {}) + SV.text(x0 - 9, gy(v) + 4, v, "sm", { "text-anchor": "end" }); } return o; };
const niceStep = (mx) => [10, 20, 50, 100, 200, 500, 1000].find((s) => s >= mx / 6) || 1000;
function d45(s) {
  const dI = (s.dI || 0) * 20, aAE = 100 + (s.I ? 50 : 0) + (s.G ? 50 : 0) + dI, top = s.G ? 200 : s.I ? 150 : 100;
  let o = tickSet(px, py, E0, F0, 700, 700, 100, true) + axes(E0, F0, E0 + 315, F0 - 318, "", "Aggregate expenditure, AE") + SV.text(px(350), F0 + 40, "National income, Y", "sm", { "text-anchor": "middle" });
  if (s.l45 > 0) o += SV.line(px(0), py(0), px(MX), py(MX), "c3", op(s.l45)) + tag(px(MX) + 6, py(MX) + 4, "45° line", "t3", s.l45) + tag(px(MX) + 6, py(MX) + 20, "(AE = Y)", "t3", s.l45);
  const ln = (a, c, lab, dash, dy) => SV.line(px(0), py(a), px(MX), py(a + SL * MX), c + (dash ? " dash" : ""), op(1)) + tag(px(MX) + 6, py(a + SL * MX) + (dy || 4), lab, c === "c1" ? "t1" : c === "c2" ? "t2" : "t4", 1);
  if (s.C > 0) o += SV.line(px(0), py(100), px(MX), py(100 + SL * MX), "c4", op(s.C)) + tag(px(MX) + 6, py(100 + SL * MX) + 4, "C", "t4", s.C);
  if (s.I > 0) o += SV.line(px(0), py(150), px(MX), py(150 + SL * MX), "c1", op(s.I)) + tag(px(MX) + 6, py(150 + SL * MX) + 4, "C + I", "t1", s.I);
  if (s.G > 0) o += SV.line(px(0), py(200), px(MX), py(200 + SL * MX), "c1", { ...op(s.G), ...(dI > 0 ? { "stroke-dasharray": "6 5" } : {}) }) + tag(px(MX) + 6, py(200 + SL * MX) + 4, "C + I + G", "t1", s.G);
  if (dI > 0) o += SV.line(px(0), py(aAE), px(MX), py(aAE + SL * MX), "c2") + tag(px(MX) + 6, py(aAE + SL * MX) - 10, "C + I + G (I up 20)", "t2", 1);
  if (s.be > 0) o += SV.line(px(250), F0, px(250), py(250), "c4 dash", op(s.be)) + SV.circle(px(250), py(250), 5, "dot4", op(s.be)) + SV.line(E0, py(250), px(250), py(250), "c4 dash", op(s.be)) + tag(px(250) - 8, py(250) - 12, "break-even: C = Y = 250", "t4", s.be, "end");
  const Y0 = top === 200 ? 500 : 0;
  if (s.eq > 0) o += SV.line(px(Y0), F0, px(Y0), py(Y0), "c1 dash", op(s.eq)) + SV.circle(px(Y0), py(Y0), 6, "dot1", op(s.eq)) + SV.line(E0, py(Y0), px(Y0), py(Y0), "c1 dash", op(s.eq)) + tag(px(Y0) - 10, py(Y0) - 12, "equilibrium: Y = AE = 500", "t1", s.eq, "end");
  if (s.y > 0) { const Y = s.yv, a = 200 + SL * Y, c = Y < 500 ? "t2" : "t4";
    o += SV.line(px(Y), py(Y), px(Y), py(a), "c2", { "stroke-width": 6, ...op(s.y) }) + SV.circle(px(Y), py(Y), 5, "dot3", op(s.y)) + SV.circle(px(Y), py(a), 5, "dot1", op(s.y));
    o += SV.line(px(Y), F0 - 8, px(Y + (Y < 500 ? 150 : -150)), F0 - 8, "c2", op(s.y)) + SV.arrowHead(px(Y + (Y < 500 ? 150 : -150)), F0 - 8, Y < 500 ? "r" : "l", "dot2");
    if (s.t) o += tag(px(Y) + (Y < 500 ? -10 : 10), py(Math.max(Y, a)) - 14, s.t, c, s.y, Y < 500 ? "end" : "start"); }
  if (s.st > 0) { const Ys = [500, 520, 532, 539.2, 543.52]; let d = "";
    for (let k = 0; k < Math.min(4, s.st); k++) { const a = Ys[k], b = Ys[k + 1]; d += SV.line(px(a), py(a), px(a), py(b), "c2", { "stroke-width": 2 }) + SV.line(px(a), py(b), px(b), py(b), "c2", { "stroke-width": 2 }); }
    o += d; }
  if (s.sv > 0) { const a = 500, cc = 400;
    o += SV.line(px(a) - 10, py(cc), px(a) - 10, py(a), "c3", { "stroke-width": 6, ...op(s.sv) }) + tag(px(a) - 18, py(450) + 4, "S = 100", "t3", s.sv, "end");
    o += SV.line(px(a) + 10, py(cc), px(a) + 10, py(a), "c1", { "stroke-width": 6, ...op(s.sv) }) + tag(px(a) + 18, py(450) + 4, "I + G = 100", "t1", s.sv); }
  return o;
}
const D0 = { l45: 0, C: 0, I: 0, G: 0, be: 0, eq: 0, y: 0, yv: 300, t: "", dI: 0, st: 0, sv: 0 };
const st = (o) => Object.assign({}, D0, o);
$("#pic1").innerHTML = `<svg viewBox="0 0 760 400" role="img" aria-label="Axes of the Keynesian diagram with the 45 degree line, the aggregate expenditure line and equilibrium">${d45(st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }))}</svg>`;
const stp = (id, label, steps) => Lib.stepper($(id), { w: 760, h: 400, label, base: D0, draw: d45, tween: 900, dwell: 6200, steps });

stp("#stB", "Building the 45 degree diagram: the 45 degree line, then C, C plus I, C plus I plus G and equilibrium", [
  { cap: "<b>The axes.</b> National income on the horizontal axis, aggregate expenditure on the vertical, both on the <b>same scale</b>.", s: st({}) },
  { cap: "<b>The 45° line.</b> With equal scales, every point on it has expenditure equal to income. It marks the only places where spending matches output.", s: st({ l45: 1 }) },
  { cap: "<b>Consumption: C = 100 + 0.6Y.</b> It starts at 100 (autonomous consumption) and slopes up with the MPC of 0.6, so it is flatter than the 45° line.", s: st({ l45: 1, C: 1 }) },
  { cap: "<b>Break-even.</b> C meets the 45° line at Y = 250. Below it households spend more than they earn. Above it the vertical gap between the lines is saving.", s: st({ l45: 1, C: 1, be: 1 }) },
  { cap: "<b>Add investment of 50.</b> It is autonomous, so the line shifts up in parallel to C + I.", s: st({ l45: 1, C: 1, I: 1 }) },
  { cap: "<b>Add government spending of 50.</b> Another parallel shift: C + I + G = 200 + 0.6Y. This is the aggregate expenditure line.", s: st({ l45: 1, C: 1, I: 1, G: 1 }) },
  { cap: "<b>Equilibrium.</b> AE crosses the 45° line at Y = 200 ÷ (1 − 0.6) = <b>500</b>. Only here does planned expenditure equal output.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
]);
stp("#stE", "Below equilibrium aggregate expenditure exceeds output so income rises, and above it income falls", [
  { cap: "<b>Equilibrium is 500.</b> At 500 planned spending is 200 + 0.6 × 500 = 500: it matches output.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Income of 300.</b> AE is 200 + 0.6 × 300 = 380, which is <b>80 more than output</b>. Shops sell more than expected, so stocks fall.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 300, t: "AE > output: stocks fall" }) },
  { cap: "<b>Firms respond</b> by raising output and hiring. Income rises, which is a movement along the AE line towards 500, and the gap gets smaller as it goes.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 300, t: "output rises" }) },
  { cap: "<b>Income of 700.</b> AE is 200 + 0.6 × 700 = 620, which is <b>80 less than output</b>. Unsold stocks pile up.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 700, t: "AE < output: stocks rise" }) },
  { cap: "<b>Firms cut production</b> and income falls back towards 500. From either side the economy moves to the point where the lines cross, so the equilibrium is stable.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, y: 1, yv: 700, t: "output falls" }) },
]);
stp("#stM", "A rise in investment of 20 shifts the aggregate expenditure line up and income rises by 50 through rounds of spending", [
  { cap: "<b>Start at equilibrium, Y = 500.</b>", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Investment rises by 20.</b> Autonomous spending is now 220, so the whole AE line shifts <b>up by 20</b> (the red line).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1 }) },
  { cap: "<b>Round 1.</b> At Y = 500, AE is now 520, so firms produce 520. The 20 of extra output is 20 of extra income.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 1 }) },
  { cap: "<b>Round 2.</b> People spend 60% of that extra 20, which is 12. AE at 520 is 532, so output rises to 532.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 2 }) },
  { cap: "<b>Rounds 3 and 4.</b> Each step is 60% of the one before: 7.2, then 4.3. The staircase between the AE line and the 45° line gets smaller and smaller.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, dI: 1, st: 4 }) },
  { cap: "<b>The new equilibrium is 550.</b> The vertical shift was 20, but income rose by 50 = 20 × 2.5, because the multiplier is 1 ÷ (1 − 0.6). The horizontal change is larger than the vertical shift.", s: st({ l45: 1, C: 1, I: 1, G: 1, dI: 1, st: 4 }) },
]);
stp("#stS", "At equilibrium the gap between C and the 45 degree line equals the gap between C and aggregate expenditure", [
  { cap: "<b>At equilibrium (500)</b> consumption is 100 + 0.6 × 500 = 400.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1 }) },
  { cap: "<b>Saving is income minus consumption</b>: 500 − 400 = <b>100</b>. On the diagram it is the vertical gap between the 45° line and the C line (green).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 0.01 }) },
  { cap: "<b>Investment plus government spending</b> is 50 + 50 = <b>100</b>. It is the vertical gap between the C line and the AE line (blue).", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 1 }) },
  { cap: "<b>The same height.</b> At equilibrium AE lies on the 45° line, so the two gaps are equal: S = I + G. With taxes and trade, leakages S + T + M equal injections I + G + X. The 45° diagram and the circular flow give the same equilibrium.", s: st({ l45: 1, C: 1, I: 1, G: 1, eq: 1, sv: 1 }) },
]);

/* ---------- Lab 1 ---------- */
function lab45() {
  if (!$("#la") || !$("#lc") || !$("#li") || !$("#lg") || !$("#lx") || !$("#lt") || !$("#lm")) return;
  const a = +$("#la").value, c = +$("#lc").value / 100, I = +$("#li").value, G = +$("#lg").value, X = +$("#lx").value, t = +$("#lt").value / 100, m = +$("#lm").value / 100;
  const sl = c * (1 - t) - m, k = 1 / (1 - sl), A = a + I + G + X, Y = A * k;
  const S = -a + (1 - c) * (1 - t) * Y, T = t * Y, M = m * Y, lk = S + T + M, inj = I + G + X;
  $("#r1").textContent = Lib.fmtN(sl, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = "$" + Lib.fmtN(lk, 0) + "bn"; $("#r5").textContent = "$" + Lib.fmtN(inj, 0) + "bn";
  $("#rv").textContent = `AE = ${Lib.fmtN(A, 0)} + ${Lib.fmtN(sl, 2)}Y crosses the 45° line at Y = ${Lib.fmtN(A, 0)} × ${Lib.fmtN(k, 2)} = $${Lib.fmtN(Y, 0)}bn. At that income leakages (${Lib.fmtN(lk, 0)}) equal injections (${Lib.fmtN(inj, 0)}).`;
  const mx = Math.max(Y * 1.3, 100), sc = 300 / mx, gx = (v) => 70 + sc * v, gy = (v) => 340 - sc * v, ln = (b) => [gx(0), gy(b), gx(mx), gy(b + sl * mx)];
  const lines = [[a, "c4", "C", "t4"], [a + I, "c1", "C+I", "t1"], [a + I + G, "c1", "C+I+G", "t1"], [A, "c2", "AE", "t2"]];
  const stp2 = niceStep(mx);
  let o = tickSet(gx, gy, 70, 340, mx, mx, stp2, true) + axes(70, 340, 410, 25, "", "Expenditure, AE") + SV.text(gx(mx / 2), 378, "Income, Y", "sm", { "text-anchor": "middle" }) + SV.line(gx(0), gy(0), gx(mx), gy(mx), "c3") + tag(gx(mx) - 2, gy(mx) + 16, "45°", "t3", 1, "end");
  let prev = -1;
  lines.forEach(([b, cl, lab, tc], i) => { if (i > 0 && Math.abs(b - prev) < 0.01) return; prev = b; const [x1, y1, x2, y2] = ln(b); o += SV.line(x1, y1, x2, y2, cl, i === 3 ? { "stroke-width": 4 } : {}) + (i === 3 ? tag(x2 + 4, y2 + 4, lab, tc, 1) : tag(x2 - 4, y2 - 6, lab, tc, 1, "end")); });
  o += SV.line(gx(Y), 340, gx(Y), gy(Y), "c1 dash") + SV.circle(gx(Y), gy(Y), 6, "dot1") + tag(gx(Y) - 10, gy(Y) - 12, "Y = " + Lib.fmtN(Y, 0), "t1", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la", label: "Autonomous consumption a ($bn) ", min: 20, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g2"), { id: "lc", label: "MPC (%) ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g3"), { id: "li", label: "Investment I ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g4"), { id: "lg", label: "Government spending G ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g5"), { id: "lx", label: "Exports X ($bn) ", min: 0, max: 150, step: 10, value: 50, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g6"), { id: "lt", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 10, fmt: (v) => v, onInput: lab45 });
Lib.slider($("#g7"), { id: "lm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: lab45 });
lab45();
btnTable("lbBtns", "lbOut", [
  ["Vertical distance from the horizontal axis up to the C line at income Y", "Consumption at Y", "Read the height of the C line."],
  ["Vertical distance between the 45° line and the C line", "Saving at Y", "S = Y − C. At break-even the distance is zero."],
  ["Vertical distance between the C line and the AE line", "I + G + net exports at Y", "The other components of AE added to consumption."],
  ["Vertical distance between the 45° line and the AE line at income below equilibrium", "Unplanned fall in stocks (AE exceeds output)", "A signal for firms to raise production."],
  ["Vertical distance between the 45° line and the AE line at full employment income", "The inflationary or deflationary gap", "The injection or cut in AD needed to reach full employment."],
  ["Horizontal distance between the old and the new equilibrium", "The change in national income", "Equals the vertical shift of AE times the multiplier."],
  ["Vertical distance between the old and the new AE line", "The change in autonomous spending", "Equals the change in income divided by the multiplier."]
], ["Distance on the diagram", "What it represents", "Note"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does each change cause a movement along the AE line or a shift of the AE line?", buckets: [{"label": "Movement along the AE line"}, {"label": "Shift of the AE line"}], items: [{"text": "Income rises because firms hire more workers", "b": 0}, {"text": "A fall in the interest rate raises investment", "b": 1}, {"text": "The government cuts its spending", "b": 1}, {"text": "A rise in foreign income raises exports", "b": 1}, {"text": "Consumption rises because income has risen", "b": 0}, {"text": "Business confidence falls", "b": 1}, {"text": "Income falls from 700 towards 500 as stocks pile up", "b": 0}, {"text": "A rise in house prices makes households feel wealthier", "b": 1}], done: "Autonomous spending shifts the line. A change in income moves you along it." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["45° line", "All the points where aggregate expenditure equals national income"], ["Aggregate expenditure", "Total planned spending: C + I + G + (X − M)"], ["Break-even income", "The income at which consumption equals income and saving is zero"], ["Autonomous spending", "Spending that does not depend on income; it sets the intercept"], ["Slope of the AE line", "The share of extra income spent on domestic output"], ["Equilibrium national income", "The income where the AE line cuts the 45° line"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "An economy is at an income below equilibrium. Put the adjustment in order.", items: ["Planned expenditure is greater than output", "Stocks fall unexpectedly", "Firms raise output and employ more workers", "Income rises along the AE line", "The economy reaches the income where AE equals output"], done: "The gap between AE and output gets smaller each round until the lines cross." });
Lib.calc($("#c1"), { qs: [
  {"q": "C = 100 + 0.6Y, I = 50 and G = 50. Calculate equilibrium national income.", "a": 500, "unit": "$bn", "tol": 0.01, "hint": "Y = 200 + 0.6Y.", "sol": "0.4Y = 200, so Y = <b>500</b>."},
  {"q": "C = 100 + 0.6Y. At what income does saving equal zero (break-even)?", "a": 250, "unit": "$bn", "tol": 0.01, "hint": "Set Y = 100 + 0.6Y.", "sol": "0.4Y = 100, so Y = <b>250</b>."},
  {"q": "With C = 100 + 0.6Y, what is saving when income is 500?", "a": 100, "unit": "$bn", "tol": 0.01, "hint": "S = Y − C.", "sol": "C = 400, so S = 500 − 400 = <b>100</b>."},
  {"q": "AE = 200 + 0.6Y. What is aggregate expenditure at an income of 300?", "a": 380, "unit": "$bn", "tol": 0.01, "hint": "200 + 0.6 × 300.", "sol": "200 + 180 = <b>380</b>, which is 80 more than output."},
  {"q": "Autonomous spending rises by 20 and the slope of the AE line is 0.6. By how much does equilibrium income rise?", "a": 50, "unit": "$bn", "tol": 0.01, "hint": "Multiplier = 1 ÷ (1 − 0.6).", "sol": "k = 2.5, so the rise is 20 × 2.5 = <b>50</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does every point on the 45° line show?", opts: ["Saving equals investment", "Aggregate expenditure equals national income", "Full employment", "Zero inflation"], a: 1, why: "With equal scales, expenditure equals income at every point." },
  { q: "Why must the AE line be flatter than the 45° line?", opts: ["Because investment is autonomous", "Because the MPC is less than 1 and leakages take part of each extra dollar", "Because government spending is fixed", "Because the multiplier is greater than 1"], a: 1, why: "Only part of each extra dollar of income is spent on domestic output, so the slope is below 1." },
  { q: "A rise in autonomous consumption does what on the 45° diagram?", opts: ["Moves the economy along the AE line", "Shifts the AE line upwards", "Rotates the 45° line", "Shifts the 45° line downwards"], a: 1, why: "Autonomous spending sets the intercept, so a rise shifts the line up." },
  { q: "At an income above equilibrium, what happens to stocks?", opts: ["They fall unexpectedly", "They rise unexpectedly", "They stay the same", "They are not affected"], a: 1, why: "AE is below output, so unsold goods build up and firms cut production." },
  { q: "At equilibrium in a closed economy with no government, which is true?", opts: ["S = I", "S > I", "S < I", "S = 0"], a: 0, why: "C + I = Y means that I = Y − C = S." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Keynesian 45° diagram", "Expenditure (vertical) against income (horizontal); equilibrium where AE cuts the 45° line."],
  ["45° line", "Points where AE = Y; the only places where output is fully sold."],
  ["AE line", "Planned spending at each income: C + I + G + (X − M). Starts at autonomous spending."],
  ["Slope of AE", "c(1 − t) − m: the share of extra income spent on domestic output."],
  ["Break-even income", "Where C = Y and saving is zero."],
  ["Stable equilibrium", "Below it stocks fall and output rises; above it stocks rise and output falls."],
  ["Shift versus movement", "Autonomous spending shifts the line; income moves you along it."],
  ["Leakages = injections", "S + T + M = I + G + X at equilibrium; the same point as AE = Y."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a closed economy the aggregate expenditure line (C + I + G) cuts the 45° line at a level of income below the full employment level. What measures the deflationary gap? (Based on May/June 2023 · 33 · Q20)", opts: ["The horizontal distance between equilibrium income and full employment income", "The vertical distance between the C + I + G line and the 45° line at full employment income", "The vertical distance between the C line and the C + I line", "The vertical distance between the C line and the 45° line at equilibrium income"], a: 1, why: "The deflationary gap is the vertical distance between the 45° line and the AE line (C + I + G) at the full employment level of income." },
  { q: "A closed economy has an AD line that cuts the 45° line at income N, and full employment income YF is above N. Which distance measures the deflationary gap? (Based on Oct/Nov 2023 · 31 · Q18)", opts: ["The horizontal distance from N to YF", "The vertical distance between the 45° line and the AD line at YF", "The vertical distance between the AD line and the consumption line at YF", "The height of the AD line at the vertical axis"], a: 1, why: "Measure the gap vertically at full employment, between the 45° line and AD. The horizontal distance is the change in income needed." },
  { q: "Which is true at the equilibrium level of national income on the 45° diagram? (Practice, not a past paper question)", opts: ["Planned expenditure is greater than output", "Planned expenditure equals output and there is no unplanned change in stocks", "Output is always at the full employment level", "Saving is zero"], a: 1, why: "At equilibrium AE = Y, so firms sell what they produce and stocks do not change unexpectedly." },
] });
