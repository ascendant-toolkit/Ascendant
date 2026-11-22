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

const GRID = { style: "stroke:var(--line);stroke-width:1;opacity:.6" };
/* ---------- the J and W diagram ---------- */
const JL = 70, JSC = 0.7, JTOP = 36, JYMAX = 350, JYMIN = -100, JXMAX = 800, JY0 = JTOP + JYMAX * JSC, JBOT = JY0 - JYMIN * JSC;
const jx = (v) => JL + JSC * v, jy = (v) => JY0 - JSC * v;
function jwFrame() {
  let o = "";
  for (let v = 100; v <= JXMAX; v += 100) o += SV.line(jx(v), jy(JYMAX), jx(v), JBOT, "", GRID);
  for (let v = 0; v <= JXMAX; v += 100) o += SV.line(jx(v), JBOT, jx(v), JBOT + 5, "", {}) + SV.text(jx(v), JBOT + 19, v, "sm", { "text-anchor": "middle" });
  for (let v = JYMIN; v <= JYMAX; v += 50) o += SV.line(JL, jy(v), jx(JXMAX), jy(v), "", GRID) + SV.line(JL - 5, jy(v), JL, jy(v), "", {}) + SV.text(JL - 9, jy(v) + 4, v, "sm", { "text-anchor": "end" });
  return o + SV.line(JL, JBOT, JL, JTOP - 12) + SV.line(JL, jy(0), jx(JXMAX) + 10, jy(0)) + SV.text(JL + 8, JTOP - 18, "Injections and withdrawals, J and W ($bn)", "sm") + SV.text(jx(JXMAX / 2), JBOT + 62, "National income, Y ($bn)", "sm", { "text-anchor": "middle" });
}
function jwDraw(s) {
  const vj = s.vj, vw = s.vw, J = 200 + 50 * s.dJ, wi = -50 + 20 * s.wsh, ws = 0.5 + 0.1 * s.wrot, Y = (J - wi) / ws, Y0 = 500, W = (y) => wi + ws * y;
  const yEnd = (i, sl) => Math.min(JXMAX, (JYMAX - i) / sl);
  let o = jwFrame();
  const wLine = (i, sl, cls, extra) => { const e = yEnd(i, sl); return SV.line(jx(0), jy(i), jx(e), jy(i + sl * e), cls, extra || {}); };
  const wMoved = Math.abs(s.wsh) + Math.abs(s.wrot) > 0.01, jMoved = Math.abs(s.dJ) > 0.01;
  if (wMoved) o += wLine(-50, 0.5, "c2 dash", { "stroke-width": 2.5, opacity: 0.55 * vw }) + tag(jx(yEnd(-50, 0.5)) + 6, jy(-50 + 0.5 * yEnd(-50, 0.5)) + 4, "W", "t2", 1);
  o += wLine(wi, ws, wMoved ? "c4" : "c2", { "stroke-width": 3.5, ...op(vw) }) + tag(jx(yEnd(wi, ws)) + 6, jy(wi + ws * yEnd(wi, ws)) + 4, wMoved ? "W1" : "W", wMoved ? "t4" : "t2", vw);
  if (jMoved) o += SV.line(jx(0), jy(200), jx(JXMAX), jy(200), "c1 dash", { "stroke-width": 2.5, opacity: 0.55 * vj }) + tag(jx(JXMAX) + 6, jy(200) + 4, "J", "t1", 1);
  o += SV.line(jx(0), jy(J), jx(JXMAX), jy(J), jMoved ? "c3" : "c1", { "stroke-width": 3.5, ...op(vj) }) + tag(jx(JXMAX) + 6, jy(J) + 4, jMoved ? "J1" : "J", jMoved ? "t3" : "t1", vj);
  if (s.int > 0) o += SV.circle(jx(0), jy(wi), 6, "dot2", op(s.int)) + tag(jx(0) + 12, jy(wi) + 24, "−50: autonomous dissaving", "t2", s.int) + tag(jx(100), jy(0) - 10, "W = 0 at Y = 100", "t2", s.int, "middle");
  const mv = Math.abs(Y - Y0) > 1;
  if (s.eq > 0) {
    if (mv) o += SV.line(jx(Y0), jy(200), jx(Y0), JBOT, "c1 dash", { opacity: 0.4 * s.eq }) + SV.circle(jx(Y0), jy(200), 5, "dot1", { opacity: 0.45 * s.eq }) + tag(jx(Y0) + (Y > Y0 ? -4 : 4), JBOT + 34, "Y = 500", "t1", 0.6 * s.eq, Y > Y0 ? "end" : "start");
    o += SV.line(jx(Y), jy(J), jx(Y), JBOT, "c1 dash", op(s.eq)) + SV.circle(jx(Y), jy(J), 7, "dot1", op(s.eq)) + tag(jx(Y) + (mv && Y > Y0 ? 4 : mv ? -4 : 0), JBOT + 34, (mv ? "Y1 = " : "Y = ") + Lib.fmtN(Y, 0), "t1", s.eq, mv ? (Y > Y0 ? "start" : "end") : "middle");
  }
  if (s.yv > 0) { const w = W(s.yv), up = J > w, c = up ? "t3" : "t2", dir = up ? 1 : -1;
    o += SV.line(jx(s.yv), jy(w), jx(s.yv), jy(J), "c2", { "stroke-width": 7, ...op(s.a) }) + SV.circle(jx(s.yv), jy(w), 5, "dot2", op(s.a)) + SV.circle(jx(s.yv), jy(J), 5, "dot1", op(s.a));
    o += SV.line(jx(s.yv), jy(0) - 14, jx(s.yv + dir * 130), jy(0) - 14, "c2", op(s.a)) + SV.arrowHead(jx(s.yv + dir * 130), jy(0) - 14, up ? "r" : "l", "dot2");
    if (s.t) o += tag(jx(s.yv) + (up ? 12 : -12), jy((w + J) / 2) + 4, s.t, c, s.a, up ? "start" : "end"); }
  if (s.dy > 0) { const a = Math.min(Y0, Y), b = Math.max(Y0, Y);
    o += SV.line(jx(a), jy(0) + 24, jx(b), jy(0) + 24, "c3", { "stroke-width": 3, ...op(s.dy) }) + SV.line(jx(a), jy(0) + 18, jx(a), jy(0) + 30, "c3", op(s.dy)) + SV.line(jx(b), jy(0) + 18, jx(b), jy(0) + 30, "c3", op(s.dy)) + tag((jx(a) + jx(b)) / 2, jy(0) + 46, s.dyt, "t3", s.dy, "middle");
    if (s.dJt) o += SV.line(jx(740), jy(200), jx(740), jy(J), "c3", { "stroke-width": 5, ...op(s.dy) }) + tag(jx(740) - 8, (jy(200) + jy(J)) / 2 + 4, s.dJt, "t3", s.dy, "end"); }
  if (s.yf > 0) { const YF = s.yfv, w = W(YF), gap = w - J, c = gap > 0 ? "t2" : "t4";
    o += SV.line(jx(YF), jy(JYMAX), jx(YF), JBOT, "c4 dash", op(s.yf)) + tag(jx(YF), JBOT + 50, "YF = " + Lib.fmtN(YF, 0), "t4", s.yf, "middle");
    if (Math.abs(gap) > 0.5 && s.gp > 0) o += SV.line(jx(YF), jy(w), jx(YF), jy(J), "c2", { "stroke-width": 8, ...op(s.gp) }) + tag(jx(YF) + (gap > 0 ? 12 : -12), jy((w + J) / 2) + 4, (gap > 0 ? "deflationary gap = " : "inflationary gap = ") + Lib.fmtN(Math.abs(gap), 0), "t2", s.gp, gap > 0 ? "start" : "end"); }
  return o;
}
const D0 = { vj: 1, vw: 1, dJ: 0, wsh: 0, wrot: 0, int: 0, eq: 0, yv: 0, a: 0, t: "", dy: 0, dyt: "", dJt: "", yf: 0, yfv: 600, gp: 0 };
const st = (o) => Object.assign({}, D0, o);
$("#pic1").innerHTML = `<svg viewBox="0 0 720 ${JBOT + 84}" role="img" aria-label="Injections and withdrawals diagram: a horizontal J line, an upward sloping W line starting below the axis, and two equilibrium incomes">${jwDraw(st({ dJ: 1, int: 1, eq: 1, dy: 1, dyt: "ΔY = 100", dJt: "ΔJ = 50" }))}</svg>`;
const stp = (id, label, steps) => Lib.stepper($(id), { w: 720, h: JBOT + 84, label, base: D0, draw: jwDraw, tween: 1000, dwell: 6200, steps });

stp("#stB", "Building the injections and withdrawals diagram: J, W with a negative intercept, and equilibrium", [
  { cap: "<b>The axes.</b> National income on the horizontal axis, injections and withdrawals (J and W) on the vertical. The vertical axis runs below zero because W can be negative.", s: st({ vj: 0, vw: 0 }) },
  { cap: "<b>Injections J = I + G + X = 100 + 70 + 30 = 200.</b> A horizontal line: injections do not depend on domestic income.", s: st({ vj: 1, vw: 0 }) },
  { cap: "<b>Withdrawals W = S + T + M = −50 + 0.5Y.</b> It slopes up because saving, tax and imports rise with income. The slope is the MPW: 0.1 + 0.25 + 0.15 = 0.5.", s: st({ vj: 1, vw: 1 }) },
  { cap: "<b>The negative intercept.</b> At zero income there is no tax and no imports, but households dissave 50 (spend from past savings). So W is −50 where it meets the vertical axis, and crosses the horizontal axis at Y = 100.", s: st({ int: 1 }) },
  { cap: "<b>Equilibrium.</b> J = W where 200 = −50 + 0.5Y, so Y = <b>500</b>. At that income S = 0, T = 125 and M = 75, which total 200.", s: st({ int: 1, eq: 1 }) },
]);
stp("#stE", "Below equilibrium injections exceed withdrawals so income rises; above it withdrawals exceed injections so income falls", [
  { cap: "<b>Equilibrium at 500.</b> J = W = 200.", s: st({ eq: 1 }) },
  { cap: "<b>Income of 300.</b> J = 200 but W = −50 + 150 = 100, a <b>net injection of 100</b>. More is going into the circular flow than leaves it.", s: st({ eq: 1, yv: 300, a: 1, t: "J > W: net injection of 100" }) },
  { cap: "<b>Income rises.</b> Firms sell more than planned, so output and incomes rise. As income rises W rises with it, so the net injection shrinks, until W = J at 500.", s: st({ eq: 1, yv: 300, a: 1, t: "income rises" }) },
  { cap: "<b>Income of 700.</b> W = −50 + 350 = 300, which is <b>100 more than J</b>: a net withdrawal. Spending falls short of output.", s: st({ eq: 1, yv: 700, a: 1, t: "W > J: net withdrawal of 100" }) },
  { cap: "<b>Income falls</b> back to 500. From either side the economy moves to the point where J = W, so the equilibrium is stable.", s: st({ eq: 1, yv: 700, a: 1, t: "income falls" }) },
]);
stp("#stM", "A rise in injections of 50 shifts J up to J1 and income rises by 100", [
  { cap: "<b>Start at equilibrium, Y = 500.</b> J = 200, W = −50 + 0.5Y.", s: st({ eq: 1 }) },
  { cap: "<b>Government spending rises by 50.</b> J shifts up to J1 = 250. The old J is shown dashed.", s: st({ dJ: 1, eq: 0.01 }) },
  { cap: "<b>A net injection of 50.</b> At Y = 500, J1 = 250 but W is still 200. Injections exceed withdrawals, so income begins to rise.", s: st({ dJ: 1, eq: 0.01, yv: 500, a: 1, t: "net injection of 50" }) },
  { cap: "<b>W catches up.</b> For each 1 of extra income, W rises by only 0.5, so it needs income to rise by 50 ÷ 0.5 = 100 before W reaches J1. The new equilibrium is Y1 = 600.", s: st({ dJ: 1, eq: 1 }) },
  { cap: "<b>The multiplier.</b> The vertical shift of J is 50, the horizontal change in income is 100. ΔY = ΔJ × 1 ÷ MPW = 50 × 2 = 100.", s: st({ dJ: 1, eq: 1, dy: 1, dyt: "ΔY = 100 = 50 × 2", dJt: "ΔJ = 50" }) },
]);
stp("#stW", "A rise in autonomous saving shifts W up; a rise in the tax rate makes W steeper", [
  { cap: "<b>Start.</b> W = −50 + 0.5Y and J = 200, so Y = 500.", s: st({ eq: 1 }) },
  { cap: "<b>A shift of W.</b> Households become more cautious and autonomous dissaving falls from 50 to 30, so W shifts <b>up by 20</b> (W1 = −30 + 0.5Y). The slope is unchanged.", s: st({ wsh: 1, eq: 0.01 }) },
  { cap: "<b>Equilibrium falls.</b> Y = (200 + 30) ÷ 0.5 = <b>460</b>, a fall of 40, which is 20 × 2 (the same multiplier).", s: st({ wsh: 1, eq: 1 }) },
  { cap: "<b>A rotation of W.</b> The marginal rate of income tax rises from 0.25 to 0.35, so the MPW is 0.6. W becomes <b>steeper</b>, pivoting around its intercept at −50.", s: st({ wrot: 1, eq: 0.01 }) },
  { cap: "<b>Equilibrium falls and the multiplier falls.</b> Y = 250 ÷ 0.6 ≈ <b>417</b>. The multiplier is now 1 ÷ 0.6 ≈ 1.67 instead of 2.", s: st({ wrot: 1, eq: 1 }) },
]);
stp("#stG", "Full employment: W above J at YF is a deflationary gap and J above W is an inflationary gap", [
  { cap: "<b>Equilibrium is 500</b> with J = 200.", s: st({ eq: 1 }) },
  { cap: "<b>Full employment is at 600.</b> The economy is 100 below it.", s: st({ eq: 1, yf: 1, yfv: 600 }) },
  { cap: "<b>Compare J and W at YF.</b> W = −50 + 0.5 × 600 = 250, which is <b>50 above J</b>. Withdrawals exceed injections at full employment: a <b>deflationary gap of 50</b>, the vertical distance between W and J.", s: st({ eq: 1, yf: 1, yfv: 600, gp: 1 }) },
  { cap: "<b>Close it.</b> Raise injections by 50 (more G, lower interest rates for investment). J1 = 250 meets W at 600, so the gap disappears. Income rises by 50 × 2 = 100.", s: st({ dJ: 1, eq: 1, yf: 1, yfv: 600, gp: 1 }) },
  { cap: "<b>An inflationary gap.</b> If full employment were 400, W would be 150 at YF, which is <b>50 below J</b>. Injections exceed withdrawals at full employment, so the excess demand pulls up prices.", s: st({ eq: 1, yf: 1, yfv: 400, gp: 1 }) },
  { cap: "<b>Close it.</b> Cut injections by 50 (less G, higher interest rates). J falls to 150, meeting W at 400, and income falls by 100.", s: st({ dJ: -1, eq: 1, yf: 1, yfv: 400, gp: 1 }) },
]);

/* ---------- Lab 1 ---------- */
const nice = (mx) => [10, 20, 25, 50, 100, 200, 250, 500, 1000].find((s) => s >= mx / 6) || 1000;
function labJW() {
  if (!["#li", "#lg", "#lx", "#la", "#lps", "#ltx", "#lm", "#lf"].every((id) => $(id))) return;
  const I = +$("#li").value, G = +$("#lg").value, X = +$("#lx").value, a = +$("#la").value, mps = +$("#lps").value / 100, mrt = +$("#ltx").value / 100, mpm = +$("#lm").value / 100, YF = +$("#lf").value;
  const J = I + G + X, w = mps + mrt + mpm, Y = (J + a) / w, k = 1 / w, S = -a + mps * Y, T = mrt * Y, M = mpm * Y, WF = -a + w * YF, gap = WF - J;
  $("#r1").textContent = Lib.fmtN(w, 2); $("#r2").textContent = Lib.fmtN(k, 2); $("#r3").textContent = "$" + Lib.fmtN(Y, 0) + "bn";
  $("#r4").textContent = "$" + Lib.fmtN(S + T + M, 0) + "bn"; $("#r5").textContent = "$" + Lib.fmtN(J, 0) + "bn";
  $("#rv").textContent = `W = ${a ? "−" + a + " + " : ""}${Lib.fmtN(w, 2)}Y meets J = ${J} at Y = $${Lib.fmtN(Y, 0)}bn. At that income S = ${Lib.fmtN(S, 0)}, T = ${Lib.fmtN(T, 0)} and M = ${Lib.fmtN(M, 0)}. ` + (Math.abs(gap) < 0.5 ? "Equilibrium is at full employment." : gap > 0 ? `At full employment W is above J by ${Lib.fmtN(gap, 0)}: a deflationary gap. Injections would have to rise by ${Lib.fmtN(gap, 0)}, which the multiplier turns into an income rise of ${Lib.fmtN(gap * k, 0)}.` : `At full employment J is above W by ${Lib.fmtN(-gap, 0)}: an inflationary gap. Injections would have to fall by ${Lib.fmtN(-gap, 0)}.`);
  const xm = Math.max(Y * 1.25, YF * 1.15, 100), ymax = Math.max(J * 1.35, 60), ymin = -a - 10, sx = 340 / xm, sy = 270 / (ymax - ymin), gx = (v) => 70 + sx * v, gy = (v) => 20 + sy * (ymax - v), yb = gy(ymin), xs = nice(xm), ys = nice(ymax - ymin);
  let o = "";
  for (let v = xs; v <= xm; v += xs) o += SV.line(gx(v), yb, gx(v), gy(ymax), "", GRID);
  for (let v = 0; v <= xm; v += xs) o += SV.line(gx(v), yb, gx(v), yb + 5, "", {}) + SV.text(gx(v), yb + 18, v, "sm", { "text-anchor": "middle" });
  for (let v = Math.ceil(ymin / ys) * ys; v <= ymax; v += ys) o += SV.line(70, gy(v), gx(xm), gy(v), "", GRID) + SV.line(65, gy(v), 70, gy(v), "", {}) + SV.text(61, gy(v) + 4, v, "sm", { "text-anchor": "end" });
  o += SV.line(70, yb, 70, gy(ymax) - 8) + SV.line(70, gy(0), gx(xm) + 8, gy(0)) + SV.text(76, 16, "J and W ($bn)", "sm") + SV.text(gx(xm / 2), yb + 64, "National income ($bn)", "sm", { "text-anchor": "middle" });
  const yEndW = Math.min(xm, (ymax + a) / w);
  o += SV.line(gx(0), gy(-a), gx(yEndW), gy(-a + w * yEndW), "c2", { "stroke-width": 3.5 }) + tag(gx(yEndW) + 4, gy(-a + w * yEndW) + 4, "W", "t2", 1) + SV.line(gx(0), gy(J), gx(xm), gy(J), "c1", { "stroke-width": 3.5 }) + tag(gx(xm) + 4, gy(J) + 4, "J", "t1", 1);
  o += SV.line(gx(Y), gy(J), gx(Y), yb, "c1 dash") + SV.circle(gx(Y), gy(J), 6, "dot1") + tag(gx(Y), yb + 32, "Y = " + Lib.fmtN(Y, 0), "t1", 1, "middle");
  o += SV.line(gx(YF), yb, gx(YF), gy(ymax), "c4 dash") + tag(gx(YF), yb + 46, "YF = " + YF, "t4", 1, "middle");
  if (Math.abs(gap) > 0.5) o += SV.line(gx(YF), gy(WF), gx(YF), gy(J), "c2", { "stroke-width": 7 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "li", label: "Investment I ($bn) ", min: 0, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g2"), { id: "lg", label: "Government spending G ($bn) ", min: 0, max: 200, step: 10, value: 70, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g3"), { id: "lx", label: "Exports X ($bn) ", min: 0, max: 200, step: 10, value: 30, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g4"), { id: "la", label: "Autonomous dissaving a ($bn) ", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g5"), { id: "lps", label: "Marginal propensity to save (%) ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g6"), { id: "ltx", label: "Marginal rate of tax (%) ", min: 0, max: 40, step: 5, value: 25, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g7"), { id: "lm", label: "Marginal propensity to import (%) ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: labJW });
Lib.slider($("#g8"), { id: "lf", label: "Full employment income ($bn) ", min: 200, max: 1000, step: 50, value: 600, fmt: (v) => v, onInput: labJW });
labJW();
btnTable("lbBtns", "lbOut", [
  ["Vertical distance between J and W at an income below equilibrium", "A net injection", "J > W, so income rises towards equilibrium."],
  ["Vertical distance between W and J at an income above equilibrium", "A net withdrawal", "W > J, so income falls towards equilibrium."],
  ["Vertical shift of J to J1", "The change in injections, ΔJ", "From a change in I, G or X."],
  ["Horizontal distance between Y and Y1", "The change in national income, ΔY", "ΔY = ΔJ × multiplier = ΔJ ÷ MPW."],
  ["Where W cuts the vertical axis (below zero)", "Autonomous dissaving", "The a in S = −a + sY, since T and M are zero at zero income."],
  ["Where W cuts the horizontal axis", "Income at which withdrawals are zero", "Here dissaving exactly offsets taxes and imports."],
  ["Vertical distance between W and J at full employment income", "The inflationary or deflationary gap", "W above J is deflationary. J above W is inflationary. The size is the injection needed."]
], ["Distance on the diagram", "What it represents", "Note"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens on the J and W diagram in each case?", buckets: [{"label": "J shifts"}, {"label": "W shifts"}, {"label": "W rotates (slope changes)"}, {"label": "Movement along a line"}], items: [{"text": "The government raises spending on infrastructure", "b": 0}, {"text": "Exports fall after a recession abroad", "b": 0}, {"text": "Households raise their autonomous saving", "b": 1}, {"text": "The marginal rate of income tax rises", "b": 2}, {"text": "Income rises because J has risen", "b": 3}, {"text": "Tariffs lower the marginal propensity to import", "b": 2}, {"text": "Firms invest more because interest rates have fallen", "b": 0}, {"text": "Households draw less on past savings when income is zero", "b": 1}], done: "Autonomous items shift a line. A change in a marginal propensity rotates W. A change in income moves you along a line." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Injections (J)", "I + G + X: spending added to the circular flow"], ["Withdrawals (W)", "S + T + M: income taken out of the circular flow"], ["Net injection", "Injections minus withdrawals at an income below equilibrium"], ["Autonomous dissaving", "Spending from past savings at zero income; the negative intercept of W"], ["Marginal propensity to withdraw", "MPS + MRT + MPM; the slope of W"], ["Multiplier", "1 ÷ MPW; the number of times a change in J is multiplied into a change in income"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the adjustment to a rise in injections in order, starting with the first event.", items: ["Injections rise, so J shifts up to J1", "At the old income, J1 exceeds W: a net injection", "Firms sell more than planned and raise output and employment", "Income rises and withdrawals rise with it along the W line", "W equals J1 at a higher income and the economy is in equilibrium again"], done: "Income rises until withdrawals have caught up with the new injections. The change is a multiple of the rise in J." });
Lib.calc($("#c1"), { qs: [
  {"q": "MPS = 0.1, MRT = 0.25 and MPM = 0.15. What is the multiplier?", "a": 2, "tol": 0.01, "hint": "1 ÷ MPW.", "sol": "MPW = 0.5, so k = <b>2</b>."},
  {"q": "W = −50 + 0.5Y and J = 200. What is equilibrium income ($bn)?", "a": 500, "tol": 0.01, "hint": "Set −50 + 0.5Y = 200.", "sol": "0.5Y = 250, so Y = <b>500</b>."},
  {"q": "J rises from 200 to 250 and W = −50 + 0.5Y. What is the new equilibrium income ($bn)?", "a": 600, "tol": 0.01, "hint": "−50 + 0.5Y = 250.", "sol": "0.5Y = 300, so Y = <b>600</b>."},
  {"q": "At an income of 300, W = −50 + 0.5Y and J = 200. What is the net injection ($bn)?", "a": 100, "tol": 0.01, "hint": "J − W.", "sol": "W = 100, so the net injection is 200 − 100 = <b>100</b>."},
  {"q": "Full employment income is 600, W = −50 + 0.5Y and J = 200. What is the deflationary gap, the vertical distance between W and J at 600 ($bn)?", "a": 50, "tol": 0.01, "hint": "W at 600 minus J.", "sol": "W = 250, so the gap is 250 − 200 = <b>50</b>."},
  {"q": "In a closed economy MPS = 0.1 and MRT = 0.1. By how much does income rise ($m) if injections rise by $100m?", "a": 500, "tol": 0.01, "hint": "k = 1 ÷ 0.2.", "sol": "k = 5, so the rise is 5 × 100 = <b>$500m</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does a horizontal J line assume?", opts: ["Injections rise with income", "Injections do not depend on domestic income", "Injections equal withdrawals at every income", "There is no government"], a: 1, why: "J is flat because I, G and X are assumed to be set by factors other than domestic income." },
  { q: "Why does W slope upwards?", opts: ["Because saving, taxes and imports all rise with income", "Because injections rise with income", "Because prices rise", "Because the multiplier is greater than one"], a: 0, why: "Each of S, T and M increases as income rises." },
  { q: "At an income below equilibrium, which is true?", opts: ["W > J and income rises", "J > W and income rises", "J > W and income falls", "J = W"], a: 1, why: "A net injection raises output and income." },
  { q: "A flatter W line means:", opts: ["A smaller multiplier", "A larger multiplier", "No change in the multiplier", "No equilibrium"], a: 1, why: "The multiplier is 1 ÷ MPW, and a flatter line is a smaller MPW." },
  { q: "Which is shown by the negative intercept of W?", opts: ["Autonomous dissaving", "Autonomous investment", "The marginal rate of tax", "Net exports"], a: 0, why: "At zero income taxes and imports are zero, so the negative withdrawal is dissaving." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Injections J", "I + G + X; spending added to the circular flow; shown as a horizontal line."],
  ["Withdrawals W", "S + T + M; income taken out of the circular flow; slopes up."],
  ["Equilibrium", "J = W; no net injection or withdrawal."],
  ["Net injection", "J minus W at an income below equilibrium; income rises."],
  ["MPW", "MPS + MRT + MPM; the slope of W."],
  ["Multiplier", "1 ÷ MPW; ΔY = ΔJ × k."],
  ["Shift vs rotation of W", "Autonomous items shift it; a change in a marginal propensity rotates it."],
  ["Gap at YF", "W − J > 0 is deflationary; J − W > 0 is inflationary."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a closed economy, the marginal propensity to save is 0.1 and the marginal propensity to pay taxes is also 0.1. These values are constant. What is the increase in national income if there is an injection of $100 million? (Based on May/June 2021 · 32 · Q24)", opts: ["$1000 million", "$500 million", "$100 million", "$80 million"], a: 1, why: "MPW = 0.1 + 0.1 = 0.2, so the multiplier is 1 ÷ 0.2 = 5. Income rises by 5 × $100m = $500m." },
  { q: "Which does not change the level of withdrawals from the circular flow of income? (Based on May/June 2022 · 32 · Q25)", opts: ["Households having more of their income taken in tax after a rise in the rate of income tax", "Households spending more on imported cars after a currency appreciation", "Households taking money from their savings to spend on a celebration", "Households transferring money from an account in one bank to an account in another bank"], a: 3, why: "Moving money between banks is not a withdrawal. The others change taxes, imports or saving." },
  { q: "What could be used to offset a leakage from the circular flow of income? (Based on May/June 2022 · 32 · Q27)", opts: ["A reduction in domestic consumption", "A reduction in government expenditure", "An increase in the rate of interest", "An increase in investment"], a: 3, why: "An injection offsets a leakage. Investment is an injection. The other options reduce spending." },
  { q: "What might decrease if a closed economy with a government sector decides to allow international trade? (Based on Oct/Nov 2023 · 31 · Q17)", opts: ["Components of aggregate expenditure", "The number of injections into the circular flow", "The number of leakages from the circular flow", "The value of the economy's multiplier"], a: 3, why: "Trade adds exports (an injection) and imports (a leakage). The extra leakage lowers the multiplier." },
  { q: "An economy has falling incomes and rising unemployment. The central bank cuts the interest rate. When is this most likely to succeed? (Based on Oct/Nov 2024 · 33 · Q23)", opts: ["When spending by consumers is income elastic", "When spending by firms on capital goods is interest rate elastic", "When the leakage on additional national income is high", "When overseas demand for exports is price inelastic"], a: 1, why: "If investment responds strongly to interest rates, J shifts up by more. A high leakage lowers the multiplier, so it makes the policy less effective." },
] });
