/* ---------- data: income shares of five equal groups (poorest to richest) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const BASE = [5, 9, 14, 22, 50], AFTER = [8, 12, 16, 23, 41], halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const cumOf = (s) => { const t = s.reduce((a, b) => a + b, 0); let c = 0; return [0, ...s.map((v) => (c += (v / t) * 100))]; };
const ginOf = (s) => { const y = cumOf([...s].sort((a, b) => a - b)); let sum = 0; for (let i = 1; i < y.length; i++) sum += y[i - 1] / 100 + y[i] / 100; return 1 - 0.2 * sum; };
const FL = { x0: 60, y0: 300, w: 300, h: 250 }, LX = (p) => FL.x0 + (p / 100) * FL.w, LY = (v) => FL.y0 - (v / 100) * FL.h;
const lorAxes = () => SV.line(FL.x0, FL.y0, FL.x0 + FL.w + 8, FL.y0) + SV.line(FL.x0, FL.y0, FL.x0, FL.y0 - FL.h - 8) + SV.text(FL.x0 + FL.w + 8, FL.y0 + 36, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(FL.x0 + 6, FL.y0 - FL.h - 14, "Cumulative % of income", "sm");
function lorenzPath(cum, n) {
  const pts = [], f = Math.floor(n), fr = n - f;
  for (let i = 0; i <= Math.min(f, 5); i++) pts.push([LX(i * 20), LY(cum[i])]);
  if (f < 5 && fr > 0) pts.push([LX(f * 20 + fr * 20), LY(cum[f] + (cum[f + 1] - cum[f]) * fr)]);
  return pts;
}

/* ---------- Learn picture and Watch 1 ---------- */
const cB = cumOf(BASE), cA = cumOf(AFTER);
function lorDraw(s) {
  let o = lorAxes();
  for (let v = 0; v <= 100; v += 20) o += SV.text(FL.x0 - 6, LY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.text(LX(v), FL.y0 + 14, v, "sm", { "text-anchor": "middle" });
  if (s.sh > 0) { const poly = [[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)])]; o += SV.poly([[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)]).slice(1), [LX(100), LY(100)]], "f2", op(s.sh)) + SV.poly([[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)]).slice(1), [LX(100), LY(0)]], "f1", op(s.sh)) + SV.text(LX(70), LY(75), "A", "lbl bd t2", { "text-anchor": "middle", ...op(s.sh) }) + SV.text(LX(78), LY(25), "B", "lbl bd t1", { "text-anchor": "middle", ...op(s.sh) }); }
  if (s.eq > 0) o += SV.line(LX(0), LY(0), LX(100), LY(100), "gr", { "stroke-width": 2.5, ...op(s.eq) }) + SV.text(LX(46), LY(60), "line of equality", "sm bd", { ...halo, ...op(s.eq) });
  const pts = lorenzPath(cB, s.n); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  for (let i = 1; i <= 5; i++) if (s.n >= i) o += SV.circle(LX(i * 20), LY(cB[i]), 5, "dot1") + (i < 5 ? SV.text(LX(i * 20) + 8, LY(cB[i]) + 14, Lib.fmtN(cB[i], 0) + "%", "sm bd t1", { ...halo }) : "");
  if (s.aft > 0) { const p2 = lorenzPath(cA, 5); o += SV.path(Lib.ptsPath(p2), "c3", { "stroke-dasharray": "6 4", ...op(s.aft) }) + SV.text(LX(1), LY(86), "- - -  after tax and benefits", "lbl bd t3", { ...halo, ...op(s.aft) }); }
  if (s.sh > 0.5) o += SV.text(LX(2), LY(100) + 20, "Gini = A ÷ (A + B) ≈ " + Lib.fmtN(ginOf(BASE), 2) + (s.aft > 0.5 ? "  →  " + Lib.fmtN(ginOf(AFTER), 2) + " after" : ""), "lbl bd", { ...halo });
  // bars of quintile shares
  const bx = (i) => 450 + i * 58, bh = (v) => (v / 50) * 200;
  o += SV.text(450, 40, "Income share of each group (%)", "lbl bd") + SV.line(440, 300, 750, 300);
  ["poorest", "2nd", "3rd", "4th", "richest"].forEach((l, i) => { o += SV.text(bx(i) + 20, 316, l, "sm", { "text-anchor": "middle" }); if (s.n > i) o += SV.rect(bx(i), 300 - bh(BASE[i]), 18, bh(BASE[i]), "f1", op(Math.min(1, s.n - i))) + SV.text(bx(i) + 9, 300 - bh(BASE[i]) - 6, BASE[i], "sm bd t1", { "text-anchor": "middle", ...op(Math.min(1, s.n - i)) }); if (s.aft > 0) o += SV.rect(bx(i) + 20, 300 - bh(AFTER[i]), 18, bh(AFTER[i]), "f3", op(s.aft)) + SV.text(bx(i) + 29, 300 - bh(AFTER[i]) - 6, AFTER[i], "sm bd t3", { "text-anchor": "middle", ...op(s.aft) }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 345" role="img" aria-label="Lorenz curve below the line of equality with areas A and B, and income shares of five groups">${lorDraw({ n: 5, eq: 1, sh: 1, aft: 0 })}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 345, label: "Building a Lorenz curve from five income groups and calculating the Gini coefficient", base: { n: 0, eq: 0, sh: 0, aft: 0 }, draw: lorDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The line of equality.</b> If every group had the same income, the poorest 20% would get 20%, the poorest 40% would get 40%, and so on: a straight diagonal.", s: { eq: 1 } },
  { cap: "<b>Plot the data.</b> The poorest 20% of households receive <b>5%</b> of income. Adding the next group, the poorest 40% receive 5 + 9 = <b>14%</b>. The poorest 60% receive <b>28%</b>, the poorest 80% receive <b>50%</b>. The richest 20% receive the other 50%.", s: { eq: 1, n: 4 } },
  { cap: "<b>The Lorenz curve</b> joins the points up to (100, 100). It bows below the line of equality because the poor get a smaller share than their share of the population.", s: { eq: 1, n: 5 } },
  { cap: `<b>The Gini coefficient.</b> Area <b>A</b> is between the line of equality and the curve. Area <b>B</b> is under the curve. Gini = A ÷ (A + B) = <b>${Lib.fmtN(ginOf(BASE), 2)}</b>. A bigger bow means a larger A, so a higher Gini.`, s: { eq: 1, n: 5, sh: 1 } },
  { cap: `<b>After tax and benefits.</b> Progressive taxes and transfers raise the poorest 20% from 5% to 8% and cut the richest 20% from 50% to 41%. The Lorenz curve (dashed) moves towards the line of equality and the Gini falls to <b>${Lib.fmtN(ginOf(AFTER), 2)}</b>.`, s: { eq: 1, n: 5, sh: 1, aft: 1 } },
] });

/* ---------- Watch 2: tax systems ---------- */
const INC = [10, 30, 60, 100], TAX = { prog: [0, 4, 14, 30], prop: [2, 6, 12, 20], reg: [1.0, 2.7, 4.8, 6.0] };
function taxBars(s) {
  const H = (r) => (r / 35) * 220; let o = SV.line(60, 300, 740, 300) + SV.line(60, 300, 60, 50) + SV.text(66, 44, "Average tax rate (% of income)", "sm");
  INC.forEach((y, i) => {
    const gx = 100 + i * 160; o += SV.text(gx + 55, 322, "income $" + y + "k", "sm", { "text-anchor": "middle" });
    [["prog", "f1", "t1", s.p], ["prop", "f3", "t3", s.q], ["reg", "f2", "t2", s.r]].forEach(([k, c, t, v], j) => {
      if (v <= 0) return; const r = (TAX[k][i] / y) * 100, x = gx + j * 36;
      o += SV.rect(x, 300 - H(r), 30, H(r), c, op(v)) + SV.text(x + 15, 300 - H(r) - 6, Lib.fmtN(r, 0) + "%", "sm bd " + t, { "text-anchor": "middle", ...op(v) });
    });
  });
  if (s.p > 0) o += SV.text(80, 70, "progressive", "lbl bd t1", op(s.p)); if (s.q > 0) o += SV.text(80, 92, "proportional", "lbl bd t3", op(s.q)); if (s.r > 0) o += SV.text(80, 114, "regressive", "lbl bd t2", op(s.r));
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 345, label: "Average tax rate by income for progressive, proportional and regressive tax systems", base: { p: 0, q: 0, r: 0 }, draw: taxBars, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A progressive income tax.</b> No tax on the first $10k, 20% on income from $10k to $40k, 40% above $40k. Average rates <b>rise</b> with income: 0%, 13%, 23%, 30%. Richer households pay a larger <b>share</b>. The marginal rate (20% then 40%) is above the average rate.", s: { p: 1 } },
  { cap: "<b>A proportional tax.</b> A flat 20% of income. The average rate is the <b>same</b> at every income level.", s: { p: 1, q: 1 } },
  { cap: "<b>A regressive tax.</b> A 10% sales tax, where poorer households spend all their income and richer households save part. The tax takes 10%, 9%, 8% and 6% of income: the average rate <b>falls</b> as income rises.", s: { p: 1, q: 1, r: 1 } },
] });

/* ---------- Watch 3: poverty trap ---------- */
const TX = (e) => 70 + e * 30, TY = (v) => 330 - v * 18;
function trapDraw(s) {
  let o = SV.line(70, 330, 690, 330) + SV.line(70, 330, 70, 40) + SV.text(690, 366, "Earnings ($k)", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Net income ($k)", "sm");
  [0, 5, 10, 15, 20].forEach((e) => { o += SV.text(TX(e), 348, e, "sm", { "text-anchor": "middle" }); });
  [0, 4, 8, 12, 16].forEach((v) => { o += SV.text(62, TY(v) + 4, v, "sm", { "text-anchor": "end" }); });
  if (s.b > 0) o += SV.line(TX(0), TY(8), TX(20), TY(8), "gr", { "stroke-dasharray": "5 4", ...op(s.b) }) + SV.circle(TX(0), TY(8), 6, "dot1", op(s.b)) + SV.text(TX(0) + 12, TY(8) - 10, "benefit $8k with no earnings", "lbl bd t1", { ...halo, ...op(s.b) });
  if (s.t > 0) o += SV.line(TX(0), TY(8), TX(20), TY(8 + 0.8 * 20), "c1", { "stroke-dasharray": "6 4", ...op(s.t) }) + SV.text(TX(13) + 4, TY(8 + 0.8 * 13) - 8, "keeps benefit, pays 20% tax", "lbl bd t1", { ...halo, ...op(s.t) });
  if (s.w > 0) {
    const pts = []; for (let e = 0; e <= 20; e += 0.5) pts.push([TX(e), TY(0.8 * e + Math.max(0, 8 - 0.8 * e))]);
    o += SV.path(Lib.ptsPath(pts), "c2", { "stroke-width": 4, ...op(s.w) }) + SV.rect(TX(0), TY(8) - 7, TX(10) - TX(0), 14, "f2", op(s.w)) + SV.text(TX(5), TY(8) + 30, "POVERTY TRAP: earning more gains nothing", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.w) }) + SV.text(TX(17), TY(0.8 * 17) + 22, "benefit exhausted: net income rises again", "sm bd t2", { "text-anchor": "end", ...halo, ...op(s.w) });
  }
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 370, label: "Net income against earnings for a household whose means-tested benefit is withdrawn as earnings rise", base: { b: 0, t: 0, w: 0 }, draw: trapDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The benefit.</b> With no earnings, the household receives a means-tested benefit of $8k.", s: { b: 1 } },
  { cap: "<b>If the benefit were kept</b> and only the 20% income tax applied, each extra $1 earned would add 80 cents of net income. The dashed line slopes up steadily.", s: { b: 1, t: 1 } },
  { cap: "<b>But the benefit is withdrawn</b> at 80 cents for each $1 earned. Together with the 20% tax, the household loses <b>100%</b> of extra earnings (an effective marginal tax rate of 100%). Net income stays flat at $8k until the benefit runs out at $10k of earnings. This is the <b>poverty trap</b>: no incentive to work more.", s: { b: 1, t: 0.3, w: 1 } },
] });

/* ---------- Lab 1: Lorenz and Gini ---------- */
function lab1() {
  if (!$("#ts") || !$("#rd")) return;
  const T = +$("#ts").value, r = +$("#rd").value / 100, f = (100 - T) / 50;
  const pre = [BASE[0] * f, BASE[1] * f, BASE[2] * f, BASE[3] * f, T], sh = pre.map((v) => (1 - r) * v + r * 20), c = cumOf(sh), g = ginOf(sh);
  $("#r1").textContent = Lib.fmtN(c[2], 0) + "%"; $("#r2").textContent = Lib.fmtN(sh[4], 0) + "%"; $("#r3").textContent = Lib.fmtN(g, 2);
  $("#rv").textContent = g > 0.5 ? "Very unequal: the richest 20% hold a large share, the curve bows far from the line of equality and the Gini is high."
    : g < 0.25 ? "Fairly equal: the curve is close to the line of equality and the Gini is low."
    : "A moderate level of inequality. Raise the top share to widen the gap, or add redistribution to bring the curve closer to the line.";
  const F = { x0: 50, y0: 290, w: 330, h: 250 }, X = (p) => F.x0 + (p / 100) * F.w, Y = (v) => F.y0 - (v / 100) * F.h;
  const pts = c.map((v, i) => [X(i * 20), Y(v)]);
  let o = SV.line(F.x0, F.y0, F.x0 + F.w + 8, F.y0) + SV.line(F.x0, F.y0, F.x0, F.y0 - F.h - 8) + SV.text(F.x0 + F.w + 8, F.y0 + 24, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(F.x0 + 6, F.y0 - F.h - 14, "Cumulative % of income", "sm");
  o += SV.poly([[X(0), Y(0)], ...pts.slice(1), [X(100), Y(100)]], "f2") + SV.line(X(0), Y(0), X(100), Y(100), "gr", { "stroke-width": 2 }) + SV.path(Lib.ptsPath(pts), "c1") + pts.slice(1, 5).map((p) => SV.circle(p[0], p[1], 5, "dot1")).join("");
  o += SV.text(X(70), Y(78), "A", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(X(80), Y(24), "B", "lbl bd t1", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ts", label: "Share of income going to the richest 20%: ", min: 30, max: 70, step: 1, value: 50, fmt: (v) => v + "%", onInput: lab1 });
Lib.slider($("#g2"), { id: "rd", label: "Redistribution through tax and benefits: ", min: 0, max: 60, step: 5, value: 0, fmt: (v) => v + "%", onInput: lab1 });

/* ---------- Lab 2: tax systems ---------- */
const SYS = ["progressive income tax", "proportional (flat) tax", "regressive sales tax"];
function lab2() {
  if (!$("#sy")) return;
  const k = +$("#sy").value, key = ["prog", "prop", "reg"][k - 1], tx = TAX[key];
  tx.forEach((v, i) => { $("#s" + (i + 1)).textContent = "$" + Lib.fmtN(v, 1) + "k (" + Lib.fmtN((v / INC[i]) * 100, 0) + "%)"; });
  $("#sv").textContent = k === 1 ? "Progressive: the average rate rises from 0% to 30% as income rises. Richer households pay a larger share, so it reduces inequality of disposable income."
    : k === 2 ? "Proportional: everyone pays 20% of income. The rich pay more dollars but the same share."
    : "Regressive: the sales tax takes 10% of spending, but richer households spend a smaller share of their income, so the average rate falls with income. It widens inequality of disposable income.";
  const H = (r) => (r / 35) * 200, cls = ["f1", "f3", "f2"][k - 1];
  let o = SV.line(40, 230, 400, 230) + SV.line(40, 230, 40, 20) + SV.text(46, 18, "Average tax rate (%)", "sm");
  INC.forEach((y, i) => { const r = (tx[i] / y) * 100, x = 60 + i * 85; o += SV.rect(x, 230 - H(r), 50, H(r), cls) + SV.text(x + 25, 230 - H(r) - 6, Lib.fmtN(r, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 25, 250, "$" + y + "k", "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "sy", label: "Tax system: ", min: 1, max: 3, step: 1, value: 1, fmt: (v) => SYS[v - 1], onInput: lab2 });

/* ---------- Lab 3: poverty trap ---------- */
function lab3() {
  if (!$("#wr") || !$("#it")) return;
  const w = +$("#wr").value / 100, t = +$("#it").value / 100, emtr = t + w, net = 1000 * (1 - emtr);
  $("#t1").textContent = Math.round(emtr * 100) + "%"; $("#t2").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 0);
  $("#tv").textContent = emtr >= 1 ? `Effective marginal tax rate ${Math.round(emtr * 100)}%: the worker ${emtr === 1 ? "gains nothing" : "is worse off"} from earning an extra $1,000. This is a poverty trap: there is no financial incentive to earn more.`
    : emtr > 0.7 ? `The worker keeps only $${Lib.fmtN(net, 0)} of an extra $1,000. The incentive to earn more is weak.`
    : `The worker keeps $${Lib.fmtN(net, 0)} of the extra $1,000. Lower withdrawal of benefits means a stronger incentive to work, but the benefit costs the government more to keep paying.`;
  const H = (v) => 150 * (Math.abs(v) / 1000), bw = 70, base = 190;
  let o = SV.line(30, base, 400, base);
  [[30, 1000, "f1", "Extra earnings"], [120, 1000 * t, "f2", "Income tax"], [210, 1000 * w, "f4", "Benefit lost"], [300, net, net >= 0 ? "f3" : "f2", "Extra net income"]].forEach(([x, v, c, l]) => { o += SV.rect(x, v >= 0 ? base - H(v) : base, bw, H(v), c) + SV.text(x + bw / 2, v >= 0 ? base - H(v) - 6 : base + H(v) + 14, (v < 0 ? "−" : "") + "$" + Lib.fmtN(Math.abs(v), 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 244, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "wr", label: "Benefit withdrawn per $1 of extra earnings: ", min: 0, max: 100, step: 5, value: 70, fmt: (v) => v + "%", onInput: lab3 });
Lib.slider($("#g5"), { id: "it", label: "Income tax rate: ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: lab3 });

/* ---------- Lab 4: redistribution ---------- */
function lab4() {
  if (!$("#rt")) return;
  const t = +$("#rt").value / 100, tx = t * 50, fin = [BASE[0] + tx / 2, BASE[1] + tx / 2, BASE[2], BASE[3], BASE[4] - tx], g = ginOf(fin);
  $("#u1").textContent = Lib.fmtN(fin[0], 1) + "%"; $("#u2").textContent = Lib.fmtN(fin[4], 1) + "%"; $("#u3").textContent = Lib.fmtN(g, 2);
  $("#uv").textContent = t === 0 ? `No redistribution: the Gini is ${Lib.fmtN(ginOf(BASE), 2)}.`
    : `The richest 20% pay ${Math.round(t * 100)}% of their income (${Lib.fmtN(tx, 1)} points of national income), and the revenue goes to the poorest 40%. The Gini falls from ${Lib.fmtN(ginOf(BASE), 2)} to ${Lib.fmtN(g, 2)}. A very high rate could reduce the incentive to earn and the revenue, which this simple model ignores.`;
  const H = (v) => (v / 55) * 170, bw = 28; let o = SV.line(30, 220, 400, 220) + SV.text(32, 20, "% of national income", "sm");
  ["poorest", "2nd", "3rd", "4th", "richest"].forEach((l, i) => { const x = 40 + i * 70; o += SV.rect(x, 220 - H(BASE[i]), bw, H(BASE[i]), "f1") + SV.text(x + bw / 2, 220 - H(BASE[i]) - 5, BASE[i], "sm bd t1", { "text-anchor": "middle" }) + SV.rect(x + bw + 2, 220 - H(fin[i]), bw, H(fin[i]), "f3") + SV.text(x + bw + 2 + bw / 2, 220 - H(fin[i]) - 5, Lib.fmtN(fin[i], 0), "sm bd t3", { "text-anchor": "middle" }) + SV.text(x + bw, 238, l, "sm", { "text-anchor": "middle" }); });
  o += SV.text(40, 258, "blue = before, green = after tax and benefits", "sm");
  $("#labD").innerHTML = o;
}
Lib.slider($("#g6"), { id: "rt", label: "Tax on the richest 20% (share of their income): ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each tax progressive, proportional or regressive (in its effect on the average tax rate)?",
  buckets: [{ label: "Progressive" }, { label: "Proportional" }, { label: "Regressive" }],
  items: [
    { text: "Income tax with higher rates on higher bands", b: 0 }, { text: "Inheritance tax with an exempt first amount", b: 0 }, { text: "A tax-free allowance on income", b: 0 }, { text: "A tax on high-value property", b: 0 },
    { text: "A flat 20% tax on all income", b: 1 }, { text: "A flat 15% tax on profits", b: 1 },
    { text: "A sales tax on food and clothing", b: 2 }, { text: "Tobacco duty", b: 2 }, { text: "A fixed $50 vehicle licence fee", b: 2 },
  ], done: "Look at what happens to the share of income paid as income rises.",
});
Lib.classify($("#cl2"), {
  prompt: "Which type of policy to reduce inequality is each one?",
  buckets: [{ label: "Fiscal policy (tax and benefits)" }, { label: "Supply-side policy" }, { label: "Labour market policy" }],
  items: [
    { text: "A more progressive income tax", b: 0 }, { text: "Means-tested child benefit", b: 0 }, { text: "An inheritance tax", b: 0 }, { text: "Free school meals paid for by the state", b: 0 },
    { text: "Subsidised training for the unemployed", b: 1 }, { text: "More investment in schools in poor regions", b: 1 }, { text: "Better transport links to deprived areas", b: 1 },
    { text: "A national minimum wage", b: 2 }, { text: "Laws against pay discrimination", b: 2 },
  ], done: "Fiscal policy works through tax and spending; supply-side raises skills and productive capacity; labour market policy changes pay and conditions.",
});
Lib.classify($("#cl3"), {
  prompt: "Is each item income (a flow) or wealth (a stock)?",
  buckets: [{ label: "Income" }, { label: "Wealth" }],
  items: [
    { text: "Monthly salary", b: 0 }, { text: "Interest received this year", b: 0 }, { text: "Dividends paid to a shareholder", b: 0 }, { text: "Unemployment benefit", b: 0 },
    { text: "A house", b: 1 }, { text: "Savings in a bank account", b: 1 }, { text: "Shares owned", b: 1 }, { text: "A pension fund", b: 1 },
  ], done: "Income is received over a period; wealth is a stock of assets at a point in time.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Equality", "An equal distribution of income, wealth or opportunity"],
  ["Equity", "Fairness or justice, a value judgement"],
  ["Lorenz curve", "Cumulative share of income plotted against cumulative share of the population"],
  ["Gini coefficient", "A measure of inequality from 0 (perfect equality) to 1 (perfect inequality)"],
  ["Absolute poverty", "Income too low to buy the basics needed to survive"],
  ["Relative poverty", "Income low compared with others in the same society"],
  ["Transfer payment", "A payment, such as a benefit, for which no good or service is produced"],
  ["Poverty trap", "Little or no gain from earning more because benefits are withdrawn and tax is paid"],
], done: "These eight words cover the chapter." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a Lorenz curve in order.", items: [
  "Rank households from poorest to richest and split them into equal groups",
  "Work out each group's share of total income",
  "Calculate cumulative population and cumulative income shares",
  "Draw the line of equality from (0, 0) to (100, 100)",
  "Plot the cumulative points and join them to form the Lorenz curve",
  "Compare the area between the curve and the line (A) with the area below the curve (B) to find the Gini",
], done: "A bigger bow means a higher Gini coefficient." });
Lib.calc($("#c1"), { qs: [
  { q: "Income shares of five equal groups are 5%, 9%, 14%, 22% and 50%. What share does the poorest 60% receive (%)?", a: 28, sol: "5 + 9 + 14 = <b>28%</b>." },
  { q: "On a Lorenz diagram area A is 0.1 and area B is 0.4. What is the Gini coefficient?", a: 0.2, sol: "A ÷ (A + B) = 0.1 ÷ 0.5 = <b>0.2</b>." },
  { q: "A household earning $30,000 pays $6,000 in tax. What is the average tax rate (%)?", a: 20, sol: "6,000 ÷ 30,000 × 100 = <b>20%</b>." },
  { q: "A tax is 0% on income up to $10,000 and 20% above that. How much tax does a person on $30,000 pay ($)?", a: 4000, sol: "20% × (30,000 − 10,000) = <b>$4,000</b>." },
  { q: "The same person's income rises from $30,000 to $40,000 and tax rises from $4,000 to $6,000. What is the marginal tax rate (%)?", a: 20, sol: "Extra tax 2,000 ÷ extra income 10,000 × 100 = <b>20%</b>." },
  { q: "Benefits are withdrawn at 70 cents per $1 earned and income tax is 30%. What share of an extra $100 earned does the worker keep ($)?", a: 0, hint: "Effective marginal tax rate = 70% + 30%.", sol: "Effective rate 100%, so the worker keeps <b>$0</b>: a poverty trap." },
  { q: "A country's Gini coefficient falls from 0.40 to 0.30. By what percentage did it fall (%)?", a: 25, sol: "(0.40 − 0.30) ÷ 0.40 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A Gini coefficient of 0 means:", opts: ["perfect inequality", "perfect equality", "high poverty", "no wealth"], a: 1, why: "At 0 everyone receives the same: the Lorenz curve is the line of equality." },
  { q: "A bigger bow of the Lorenz curve away from the line of equality shows:", opts: ["more equality", "more inequality", "lower poverty", "a lower Gini"], a: 1, why: "Area A is bigger, so the Gini is higher." },
  { q: "A tax whose average rate falls as income rises is:", opts: ["progressive", "proportional", "regressive", "direct"], a: 2, why: "Poorer people pay a bigger share of their income." },
  { q: "Which is most likely to reduce income inequality?", opts: ["A more regressive tax system", "A more progressive income tax with transfer payments", "Cuts in education spending", "Higher sales taxes on necessities"], a: 1, why: "Richer households pay more and poorer ones receive more." },
  { q: "Equity differs from equality because equity:", opts: ["is an equal distribution", "is about fairness, a value judgement", "can be measured by the Gini coefficient", "ignores incomes"], a: 1, why: "Equity is normative, equality is an outcome that can be measured." },
  { q: "A poverty trap exists when:", opts: ["a worker gains little from earning more because benefits are withdrawn", "income tax is zero", "everyone earns the same", "wealth is equally distributed"], a: 0, why: "A very high effective marginal tax rate removes the incentive to work more." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Economic equality", "An equal distribution of income, wealth and opportunities."],
  ["Equity", "Fairness or justice in the distribution of resources. A normative idea."],
  ["Income", "A flow received over a period: wages, profit, rent, interest, benefits."],
  ["Wealth", "A stock of assets at a point in time: property, savings, shares."],
  ["Lorenz curve", "Cumulative % of income against cumulative % of the population."],
  ["Line of equality", "The 45 degree line showing a perfectly equal distribution."],
  ["Gini coefficient", "Area A ÷ (A + B). From 0 (perfect equality) to 1 (perfect inequality)."],
  ["Absolute poverty", "Income below the level needed for basic survival (a poverty line)."],
  ["Relative poverty", "Income low compared with the average in the same society."],
  ["Progressive tax", "The average tax rate rises as income rises."],
  ["Regressive tax", "The average tax rate falls as income rises."],
  ["Proportional tax", "The average tax rate stays the same at all incomes."],
  ["Transfer payment", "A payment such as a benefit with no good or service produced in return."],
  ["Means-tested benefit", "A benefit paid only to people with income or wealth below a set level."],
  ["Poverty trap", "Little or no gain from earning more because benefits are withdrawn and tax is paid."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2022 · 32 · Q15] When is a policy of income redistribution from rich people to poor people most appropriate?", opts: ["when control of demand-pull inflation is the priority", "when equality is valued more highly than efficiency", "when monetary reward is the best incentive to risk-taking", "when the rich have higher marginal utility curves than the poor"], a: 1, why: "Redistribution trades some efficiency for equity, so it fits best where equality is valued more. D has the marginal utility argument the wrong way round: the rich have lower marginal utility of income." },
  { q: "[Feb/March 2020 · 32 · Q15] Which combination of policy changes is most likely to redistribute income from the richest households to the poorest households in an economy? (indirect taxes / means-tested benefits / benefits for everyone)", opts: ["decrease / increase / decrease", "decrease / increase / increase", "increase / decrease / increase", "increase / decrease / decrease"], a: 0, why: "Lower indirect taxes (often regressive), more targeted means-tested benefits and fewer universal benefits (which also go to the rich) move income towards the poorest." },
  { q: "[Feb/March 2023 · 32 · Q14] Which changes in direct and indirect tax are likely to increase the inequality in the distribution of income in a developed economy? (direct / indirect)", opts: ["fall / fall", "fall / rise", "rise / fall", "rise / remain constant"], a: 1, why: "Cutting progressive direct taxes while raising often-regressive indirect taxes shifts the burden onto lower incomes." },
  { q: "[Feb/March 2021 · 32 · Q16] In which circumstances is a poverty trap least likely to operate?", opts: ["A female worker is paid less than a male worker for doing the same job.", "A worker is paid the minimum wage and refuses a higher paid job because net income is lower after tax.", "A worker refuses higher paid work as it means more expensive travel and childcare costs.", "An unemployed worker refuses a job because earnings are less than unemployment benefit."], a: 0, why: "B, C and D are all cases where working more brings little or no gain. A is discrimination, not a poverty trap." },
  { q: "[May/June 2021 · 31 · Q15] The Gini coefficient of a country is 0.40. The poorest income earners pay no income tax. The government increases the tax rate on the highest income earners, which results in a more even distribution of income. What could be concluded from this?", opts: ["The Gini coefficient falls and the income tax system becomes more progressive.", "The Gini coefficient falls and the income tax system becomes more regressive.", "The Gini coefficient rises and the income tax system becomes more progressive.", "The Gini coefficient rises and the income tax system becomes more regressive."], a: 0, why: "A more even distribution means a lower Gini, and raising rates on the rich makes the tax more progressive." },
  { q: "[Feb/March 2025 · 32 · Q9] When does a more equal distribution of income occur?", opts: ["when a country's income tax system is made more progressive", "when someone is made better off without making someone else worse off", "when the best use is made of scarce resources", "when there is an increase in the Gini coefficient"], a: 0, why: "B is a Pareto improvement, C is efficiency, D is greater inequality." },
  { q: "[May/June 2020 (not sat) · 31 · Q16] The diagram shows two Lorenz curves. If the Lorenz curve shifts from L1 to L2 (further from the line of equality), what is least likely to have caused this?", opts: ["Capital gains tax has been reduced.", "Income tax has been made more progressive.", "Inheritance tax has been reduced.", "The tax-free allowance has been decreased for everyone."], a: 1, why: "A shift away from the line of equality means more inequality. A more progressive income tax reduces it, so it is the least likely cause." },
  { q: "[Feb/March 2023 · 32 · Q27] A diagram shows income inequality rising and then falling as income per capita increases. Which curve is shown?", opts: ["Kuznets curve", "Laffer curve", "Lorenz curve", "Phillips curve"], a: 0, why: "The Kuznets curve suggests inequality first rises then falls as a country develops." },
  { q: "[May/June 2020 (not sat) · 31 · Q20] Young workers find it especially difficult to get a job during a recession. A government introduces a transfer payment for those seeking work and provides information on vacancies. What should be a positive outcome for those seeking work?", opts: ["Firms no longer need to advertise jobs because there are few vacancies.", "No production of goods or services is required for a transfer payment.", "Obtaining information on jobs available makes the labour market more perfect.", "Students will leave their studies to join the workforce at an earlier age."], a: 2, why: "Better information moves the labour market towards perfect information, helping match workers to jobs. B is true of transfer payments but is not a benefit for the job seeker." },
] });
