/* ---------- shared chart helpers ---------- */
/* Steppers: L (thousand workers) 0-200 on x, wage ($ per hour) 0-28 on y */
const SX = (L) => 80 + L * 3.1, SY = (w) => 330 - w * 10.5;
function sAxes(extra) {
  return SV.line(80, 330, 710, 330) + SV.line(80, 330, 80, 30) + SV.text(710, 368, "Quantity of labour (thousand workers)", "sm", { "text-anchor": "end" }) + SV.text(86, 34, "Wage ($ per hour)", "sm") + (extra || "");
}
function sLine(a, b, L0, L1, cls, o) { return SV.line(SX(L0), SY(a + b * L0), SX(L1), SY(a + b * L1), cls, o); }
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });

/* ---------- 2 · minimum wage, competitive market ---------- */
function cmChart(s) {
  let o = sAxes();
  o += sLine(20, -0.1, 0, 200, "c1") + SV.text(SX(12), SY(18.8) - 12, "D = MRP", "lbl bd t1", op(s.d));
  if (s.s > 0) o += sLine(4, 0.1, 0, 200, "c2", op(s.s)) + SV.text(SX(200) - 4, SY(24) - 8, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) });
  if (s.e > 0) {
    o += SV.line(SX(80), SY(12), SX(80), SY(0), "gr", op(s.e)) + SV.line(SX(0), SY(12), SX(80), SY(12), "gr", op(s.e)) + SV.circle(SX(80), SY(12), 7, "dot3", op(s.e));
    o += SV.text(SX(80), SY(0) + 20, "80", "lbl bd", { "text-anchor": "middle", ...op(s.e) }) + SV.text(SX(0) - 6, SY(12) + 4, "12", "lbl bd", { "text-anchor": "end", ...op(s.e) });
    o += SV.text(SX(80) + 12, SY(12) + 22, "Equilibrium", "lbl bd t3", op(s.e));
  }
  if (s.m > 0) {
    o += SV.line(SX(0), SY(14), SX(200), SY(14), "c4 dash", op(s.m)) + SV.text(SX(0) - 6, SY(14) + 4, "14", "lbl bd t4", { "text-anchor": "end", ...op(s.m) }) + SV.text(SX(200) - 4, SY(14) - 8, "Minimum wage $14", "lbl bd t4", { "text-anchor": "end", ...op(s.m) });
  }
  if (s.q > 0) {
    o += SV.circle(SX(60), SY(14), 6, "dot1", op(s.q)) + SV.circle(SX(100), SY(14), 6, "dot2", op(s.q));
    o += SV.line(SX(60), SY(14), SX(60), SY(0), "gr", op(s.q)) + SV.line(SX(100), SY(14), SX(100), SY(0), "gr", op(s.q));
    o += SV.text(SX(60), SY(0) + 20, "60", "lbl bd t1", { "text-anchor": "middle", ...op(s.q) }) + SV.text(SX(100), SY(0) + 20, "100", "lbl bd t2", { "text-anchor": "middle", ...op(s.q) });
    o += SV.text(SX(60) - 10, SY(14) - 24, "Demanded", "sm", { "text-anchor": "end", ...op(s.q) }) + SV.text(SX(100) + 10, SY(14) - 24, "Supplied", "sm", op(s.q));
  }
  if (s.u > 0) {
    o += SV.rect(SX(60), SY(14), SX(100) - SX(60), 14, "f2", op(s.u)) + SV.text((SX(60) + SX(100)) / 2, SY(14) + 62, "Unemployment 40", "lbl bd t2", { "text-anchor": "middle", ...op(s.u) });
  }
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 370, label: "Labour market diagram with a minimum wage above the equilibrium wage", base: { d: 0, s: 0, e: 0, m: 0, q: 0, u: 0 }, draw: cmChart, tween: 1000, dwell: 5000, steps: [
  { cap: "The <b>demand for labour</b> (MRP) slopes down: firms hire more when labour is cheaper.", s: { d: 1 } },
  { cap: "The <b>supply of labour</b> slopes up: a higher wage attracts more workers into this occupation.", s: { d: 1, s: 1 } },
  { cap: "In a competitive market the wage settles where demand equals supply: <b>$12 an hour and 80 thousand workers</b>.", s: { d: 1, s: 1, e: 1 } },
  { cap: "The government sets a <b>minimum wage of $14</b>, above equilibrium, so it is <b>binding</b>. Firms cannot legally pay less.", s: { d: 1, s: 1, e: 0.5, m: 1 } },
  { cap: "At $14 firms demand only <b>60</b> thousand workers (MRP falls below the wage for the others), but <b>100</b> thousand want to work. Employment falls from 80 to 60.", s: { d: 1, s: 1, e: 0.5, m: 1, q: 1 } },
  { cap: "The gap is <b>unemployment of 40 thousand</b>. Those with jobs gain $2 an hour; those who lose or cannot find jobs lose. The size of the job loss depends on how <b>elastic</b> the demand for labour is.", s: { d: 1, s: 1, e: 0.5, m: 1, q: 1, u: 1 } },
] });
/* ---------- 3 · monopsony ---------- */
function monoChart(s) {
  let o = sAxes();
  o += sLine(20, -0.1, 0, 200, "c1") + SV.text(SX(200) - 4, SY(0) - 8, "MRP", "lbl bd t1", { "text-anchor": "end" });
  o += sLine(2, 0.1, 0, 180, "c2") + SV.text(SX(180) + 4, SY(20) + 4, "ACL = S", "lbl bd t2");
  if (s.mcl > 0) o += sLine(2, 0.2, 0, 90, "c4", op(s.mcl)) + SV.text(SX(90) + 4, SY(20) + 4, "MCL", "lbl bd t4", op(s.mcl));
  if (s.mono > 0) {
    o += SV.line(SX(60), SY(14), SX(60), SY(0), "gr", op(s.mono)) + SV.line(SX(0), SY(8), SX(60), SY(8), "gr", op(s.mono)) + SV.line(SX(0), SY(14), SX(60), SY(14), "gr", op(s.mono));
    o += SV.circle(SX(60), SY(14), 6, "dot4", op(s.mono)) + SV.circle(SX(60), SY(8), 7, "dot2", op(s.mono));
    o += SV.text(SX(60), SY(0) + 20, "60", "lbl bd", { "text-anchor": "middle", ...op(s.mono) }) + SV.text(SX(0) - 6, SY(8) + 4, "8", "lbl bd t2", { "text-anchor": "end", ...op(s.mono) }) + SV.text(SX(0) - 6, SY(14) + 4, "14", "lbl bd t4", { "text-anchor": "end", ...op(s.mono) });
    o += SV.text(SX(60) + 10, SY(14) - 10, "MCL = MRP", "lbl bd t4", op(s.mono));
  }
  if (s.gap > 0) o += SV.rect(SX(0), SY(14), SX(60) - SX(0), SY(8) - SY(14), "f2", op(s.gap)) + SV.text(SX(30), SY(11) + 4, "wage below MRP", "lbl bd t2", { "text-anchor": "middle", ...op(s.gap) });
  if (s.comp > 0) {
    o += SV.circle(SX(90), SY(11), 7, "dot3", op(s.comp)) + SV.line(SX(90), SY(11), SX(90), SY(0), "gr", op(s.comp));
    o += SV.text(SX(90), SY(0) + 20, "90", "lbl bd t3", { "text-anchor": "middle", ...op(s.comp) }) + SV.text(SX(90) + 14, SY(11) - 14, "Competitive: 90, $11", "lbl bd t3", op(s.comp));
  }
  if (s.mw > 0) {
    o += SV.line(SX(0), SY(10), SX(80), SY(10), "c3 dash", op(s.mw)) + SV.text(SX(0) - 6, SY(10) + 4, "10", "lbl bd t3", { "text-anchor": "end", ...op(s.mw) });
    o += SV.circle(SX(80), SY(10), 7, "dot3", op(s.mw)) + SV.line(SX(80), SY(10), SX(80), SY(0), "gr", op(s.mw));
    o += SV.text(SX(80), SY(0) + 20, "80", "lbl bd t3", { "text-anchor": "middle", ...op(s.mw) }) + SV.text(SX(80) - 10, SY(10) + 44, "Minimum wage $10: 80", "lbl bd t3", { "text-anchor": "end", ...op(s.mw) }) + SV.text(0, 0, "", "lbl bd t3", op(s.mw));
  }
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 370, label: "Monopsony labour market diagram with marginal cost of labour and a minimum wage", base: { mcl: 0, mono: 0, gap: 0, comp: 0, mw: 0 }, draw: monoChart, tween: 1000, dwell: 5200, steps: [
  { cap: "The monopsonist's <b>MRP</b> is its demand for labour. As the only buyer it faces the whole market supply curve, which is the <b>average cost of labour (ACL)</b>: the wage it must pay at each level of employment.", s: {} },
  { cap: "To hire one more worker it must raise the wage, and it pays that higher wage to <b>all</b> its workers. So the <b>marginal cost of labour (MCL)</b> lies above the ACL and is steeper.", s: { mcl: 1 } },
  { cap: "It hires where <b>MCL = MRP</b>: <b>60</b> thousand workers. This is the profit-maximising quantity.", s: { mcl: 1, mono: 1 } },
  { cap: "The wage is read <b>down to the ACL (supply) curve</b>: just <b>$8</b>. Workers produce $14 of revenue at the margin but are paid $8: the wage is <b>below MRP</b>.", s: { mcl: 1, mono: 1, gap: 1 } },
  { cap: "In a competitive market ACL would meet MRP at <b>90 thousand workers and $11</b>. So the monopsony pays a <b>lower wage</b> and employs <b>fewer workers</b>.", s: { mcl: 1, mono: 1, gap: 1, comp: 1 } },
  { cap: "A <b>minimum wage of $10</b> (between $8 and $11): the firm cannot pay less, so its MCL is flat at $10 until supply runs out. It hires where MRP meets that, <b>80 thousand</b> workers. Wage <b>and</b> employment rise. Above $11 the minimum would start to cost jobs.", s: { mcl: 0.4, mono: 0.35, gap: 0, comp: 1, mw: 1 } },
] });
/* ---------- Lab 2: competitive market + minimum wage ---------- */
let sl3, sl4, sl5;
function lab2() {
  if (!$("#lb1") || !$("#lb2") || !$("#lb3")) return;
  const a = 20 + +$("#lb1").value, b = 4 - +$("#lb2").value, mw = +$("#lb3").value;
  const Le = (a - b) / 0.2, We = a - 0.1 * Le;
  const bind = mw > We + 0.001, W = bind ? mw : We;
  const Ld = bind ? Math.max(0, (a - mw) * 10) : Le, Ls = bind ? Math.max(0, (mw - b) * 10) : Le, un = Ls - Ld;
  $("#s1").textContent = "$" + Lib.fmtN(W, 2); $("#s2").textContent = Lib.fmtN(Ld, 0) + "k"; $("#s3").textContent = Lib.fmtN(un, 0) + "k"; $("#s4").textContent = "$" + Lib.fmtN(W * Ld, 0) + "k/hr";
  $("#sv").textContent = mw === 0 ? `No minimum wage: the market clears at $${Lib.fmtN(We, 2)} and ${Lib.fmtN(Le, 0)} thousand workers.`
    : !bind ? `The minimum wage ($${mw}) is below the equilibrium wage ($${Lib.fmtN(We, 2)}), so it is not binding and changes nothing.`
    : `A binding minimum wage of $${mw}: ${Lib.fmtN(Le - Ld, 0)} thousand fewer jobs than at equilibrium, and ${Lib.fmtN(un, 0)} thousand people who want work cannot find it.`;
  const X = (L) => 50 + L * 1.75, Y = (w) => 260 - w * 8.2;
  let o = SV.line(50, 260, 410, 260) + SV.line(50, 260, 50, 20) + SV.text(406, 280, "Labour (thousand)", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Wage ($/hr)", "sm");
  const De = Math.min(200, a * 10);
  o += SV.line(X(0), Y(a), X(De), Y(a - 0.1 * De), "c1") + SV.text(X(De) - 4, Y(a - 0.1 * De) - 6, "D", "lbl bd t1", { "text-anchor": "end" });
  o += SV.line(X(0), Y(b), X(200), Y(b + 20), "c2") + SV.text(X(200) - 4, Y(b + 20) - 6, "S", "lbl bd t2", { "text-anchor": "end" });
  o += SV.circle(X(Le), Y(We), 5, "dot3", { opacity: bind ? 0.4 : 1 });
  if (mw > 0) {
    o += SV.line(X(0), Y(mw), X(200), Y(mw), "c4 dash");
    if (bind) {
      o += SV.rect(X(Ld), Y(mw), X(Ls) - X(Ld), 10, "f2") + SV.circle(X(Ld), Y(mw), 5, "dot1") + SV.circle(X(Ls), Y(mw), 5, "dot2");
      o += SV.line(X(Ld), Y(mw), X(Ld), 260, "gr") + SV.line(X(Ls), Y(mw), X(Ls), 260, "gr");
    }
  }
  $("#labB").innerHTML = o;
}
sl3 = Lib.slider($("#g3"), { id: "lb1", label: "Demand for labour (productivity / product price): ", min: -6, max: 8, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" + v : v), onInput: lab2 });
sl4 = Lib.slider($("#g4"), { id: "lb2", label: "Supply of labour (more workers to the right): ", min: -4, max: 4, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" + v : v), onInput: lab2 });
sl5 = Lib.slider($("#g5"), { id: "lb3", label: "Minimum wage ($ per hour, 0 = none): ", min: 0, max: 20, step: 0.5, value: 0, fmt: (v) => (v === 0 ? "none" : v.toFixed(1)), onInput: lab2 });
$("#pb1").onclick = () => sl3.set(4); $("#pb2").onclick = () => sl4.set(3); $("#pb3").onclick = () => { sl3.set(0); sl4.set(0); sl5.set(0); };
/* ---------- Lab 3: monopsony + minimum wage ---------- */
function lab3() {
  if (!$("#lc1")) return;
  const mw = +$("#lc1").value;
  let W, L, un = 0, note;
  if (mw <= 8) { W = 8; L = 60; note = `A minimum wage of $${mw.toFixed(1)} is below the monopsony wage of $8, so it has no effect.`; }
  else if (mw <= 11) { W = mw; L = (mw - 2) * 10; note = `Between the monopsony wage ($8) and the competitive wage ($11): the wage and employment both rise. The firm is forced to pay $${mw.toFixed(1)}, and it is still profitable to hire up to the point where supply runs out.`; }
  else { W = mw; L = (20 - mw) * 10; un = (mw - 2) * 10 - L; note = `Above the competitive wage ($11), MRP is below the minimum wage for the marginal worker, so employment falls and there is unemployment of ${Lib.fmtN(un, 0)} thousand. Beyond $11 the monopsony gain turns into a competitive-market loss.`; }
  const gap = 20 - 0.1 * L - W;
  $("#m1").textContent = "$" + Lib.fmtN(W, 2); $("#m2").textContent = Lib.fmtN(L, 0) + "k"; $("#m3").textContent = "$" + Lib.fmtN(Math.max(0, gap), 2); $("#m4").textContent = Lib.fmtN(un, 0) + "k";
  $("#mv").textContent = note;
  const X = (l) => 50 + l * 1.75, Y = (w) => 260 - w * 11.5;
  let o = SV.line(50, 260, 410, 260) + SV.line(50, 260, 50, 20) + SV.text(406, 280, "Labour (thousand)", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Wage ($/hr)", "sm");
  o += SV.line(X(0), Y(20), X(200), Y(0), "c1") + SV.text(X(200) - 2, Y(0) - 6, "MRP", "lbl bd t1", { "text-anchor": "end" });
  o += SV.line(X(0), Y(2), X(180), Y(20), "c2") + SV.text(X(180) + 3, Y(20) + 14, "S", "lbl bd t2");
  o += SV.line(X(0), Y(2), X(90), Y(20), "c4") + SV.text(X(90) + 4, Y(20) - 2, "MCL", "lbl bd t4");
  if (mw > 8) o += SV.line(X(0), Y(mw), X(Math.max(L, (mw - 2) * 10)), Y(mw), "c3 dash");
  if (gap > 0.05) o += SV.rect(X(L) - 4, Y(20 - 0.1 * L), 4, Y(W) - Y(20 - 0.1 * L), "f2");
  o += SV.line(X(L), Y(W), X(L), 260, "gr") + SV.circle(X(L), Y(W), 6, "dot3") + SV.circle(X(L), Y(20 - 0.1 * L), 4, "dot4");
  if (un > 0) o += SV.rect(X(L), Y(W), X((mw - 2) * 10) - X(L), 8, "f2");
  $("#labC").innerHTML = o;
}
Lib.slider($("#g6"), { id: "lc1", label: "Minimum wage ($ per hour): ", min: 4, max: 16, step: 0.5, value: 8, fmt: (v) => v.toFixed(1), onInput: lab3 });

/* ---------- 40.5: the minimum wage ---------- */
const HALO = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
$("#pic1").innerHTML = `<svg viewBox="0 0 760 390" role="img" aria-label="Competitive labour market with a minimum wage above equilibrium causing unemployment">${cmChart({ d: 1, s: 1, e: 0.5, m: 1, q: 1, u: 1 })}</svg>`;

/* ---------- Lab 3: do low-paid workers gain overall? ---------- */
function lab4() {
  if (!$("#mr") || !$("#ed")) return;
  const rise = +$("#mr").value / 100, ed = +$("#ed").value, de = -ed * rise, bill = (1 + rise) * (1 + de) - 1;
  $("#w1").textContent = (de * 100).toFixed(1) + "%"; $("#w2").textContent = (bill >= 0 ? "+" : "") + (bill * 100).toFixed(1) + "%"; $("#w3").textContent = bill > 0.0005 ? "Pay up" : bill < -0.0005 ? "Pay down" : "No change";
  $("#wv").textContent = rise === 0 ? "No change in the minimum wage."
    : ed < 1 ? `Demand for labour is inelastic (${ed.toFixed(1)}): employment falls by ${Math.abs(de * 100).toFixed(1)}%, a smaller percentage than the wage rise, so total pay for low-paid workers rises by ${(bill * 100).toFixed(1)}% even though some jobs are lost.`
    : ed === 1 ? "Unit elastic: the fall in jobs roughly cancels the rise in the wage, so the wage bill barely changes."
    : `Demand for labour is elastic (${ed.toFixed(1)}): employment falls by a larger percentage than the wage rises, so total pay for low-paid workers ${bill < 0 ? "falls" : "changes little"}. Some workers gain, but as a group they lose.`;
  const H = (v) => 90 * (Math.abs(v) / 0.5), bw = 90, base = 130;
  let o = SV.line(30, base, 400, base);
  [[60, de, "Employment"], [230, bill, "Wage bill"]].forEach(([x, v, l]) => { o += SV.rect(x, v >= 0 ? base - H(v) : base, bw, H(v), v >= 0 ? "f3" : "f2") + SV.text(x + bw / 2, v >= 0 ? base - H(v) - 8 : base + H(v) + 16, (v >= 0 ? "+" : "−") + Math.abs(v * 100).toFixed(1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 242, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g7"), { id: "mr", label: "Rise in the minimum wage: ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => "+" + v + "%", onInput: lab4 });
Lib.slider($("#g8"), { id: "ed", label: "Elasticity of demand for labour (size): ", min: 0, max: 2, step: 0.1, value: 0.5, fmt: (v) => v.toFixed(1), onInput: lab4 });
lab2(); lab3();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Who is likely to gain, lose, or be affected in different ways by a binding minimum wage in a competitive market?",
  buckets: [{ label: "Likely to gain" }, { label: "Likely to lose" }, { label: "Depends" }],
  items: [
    { text: "Low-paid workers who keep their jobs", b: 0 }, { text: "Workers whose hours are protected by a higher hourly wage", b: 0 },
    { text: "Workers who lose their jobs", b: 1 }, { text: "People looking for work who cannot find a job", b: 1 }, { text: "Employers' profit margins", b: 1 },
    { text: "Consumers (prices may rise)", b: 2 }, { text: "The government's budget", b: 2 }, { text: "Workers in a monopsony", b: 2 }, { text: "Firms whose workers become more productive", b: 2 },
  ], done: "There are winners and losers, and the answer depends on the market and the level of the minimum.",
});
Lib.classify($("#cl2"), {
  prompt: "Which market does each statement describe?",
  buckets: [{ label: "Competitive labour market" }, { label: "Monopsony" }, { label: "Both" }],
  items: [
    { text: "A binding minimum wage cuts employment", b: 0 }, { text: "A minimum wage in a range can raise employment", b: 1 },
    { text: "The wage before the minimum is below MRP", b: 1 }, { text: "The wage is set where demand equals supply", b: 0 },
    { text: "MCL becomes flat at the minimum wage until supply runs out", b: 1 },
    { text: "A minimum wage below the market wage has no effect", b: 2 }, { text: "Higher pay may raise productivity", b: 2 },
  ], done: "Only above the competitive wage does a minimum wage cost jobs in both cases.",
});
Lib.order($("#o1"), { prompt: "Put the analysis of a minimum wage in a competitive labour market in order.", items: [
  "Draw demand (MRP) and supply of labour and find the equilibrium wage and employment",
  "Draw the minimum wage above the equilibrium wage so that it is binding",
  "At the minimum wage the quantity demanded of labour falls",
  "At the minimum wage the quantity supplied of labour rises",
  "Supply exceeds demand, so there is unemployment",
  "Evaluate: elasticity of demand, size of the minimum, productivity effects, who gains and loses",
], done: "A reliable exam routine." });
Lib.match($("#mt1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Minimum wage", "A legal floor on the hourly wage"],
  ["Binding minimum wage", "A minimum set above the market wage, so it changes the outcome"],
  ["Equilibrium wage", "The wage where the quantity of labour demanded equals the quantity supplied"],
  ["Unemployment from a minimum wage", "Quantity of labour supplied minus quantity demanded at the minimum"],
  ["Monopsony wage", "The wage a single buyer of labour pays, below the competitive wage"],
  ["Wage bill", "Wage multiplied by the number of workers employed"],
  ["Elasticity of demand for labour", "How responsive employment is to a change in the wage"],
  ["Substitutability of capital", "How easily machines can replace workers"],
], done: "Eight terms for the minimum wage." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand for labour: L = 200 − 10W. Supply: L = 10W − 40 (L in thousands, W in $). A minimum wage of $14 is set. How many thousand workers are unemployed?", a: 40, hint: "Find L demanded and L supplied at W = 14.", sol: "Demand: 200 − 140 = 60. Supply: 140 − 40 = 100. Unemployment = 100 − 60 = <b>40 thousand</b>." },
  { q: "In that market the equilibrium is $12 and 80 thousand. Employment falls from 80 to 60 thousand at the $14 minimum. What is the percentage fall in employment (%)?", a: 25, sol: "(80 − 60) ÷ 80 × 100 = <b>25%</b>." },
  { q: "The wage rises from $12 to $14. What is the percentage rise in the wage (%, 1 decimal place)?", a: 16.7, tol: 0.1, sol: "(14 − 12) ÷ 12 × 100 = <b>16.7%</b>." },
  { q: "Calculate the elasticity of demand for labour between the two points (include the sign).", a: -1.5, tol: 0.02, sol: "−25% ÷ 16.7% = <b>−1.5</b>: elastic, so the wage bill falls." },
  { q: "What is the change in the wage bill (wage × employment), in $ thousand per hour?", a: -120, hint: "Before: 12 × 80. After: 14 × 60.", sol: "Before 960, after 840: change = <b>−120</b>." },
  { q: "A monopsony has MRP = 20 − 0.1L and supply W = 2 + 0.1L (L in thousands). It pays $8 and employs 60 thousand. A minimum wage of $10 is set. How many thousand are employed?", a: 80, hint: "Supply at $10 is (10 − 2) × 10. MRP = 10 gives 100. Take the smaller.", sol: "Supply at $10 = 80, MRP gives 100. Employment is the smaller, <b>80 thousand</b>: employment rises from 60." },
  { q: "In the same monopsony a minimum wage of $7 is set. How many thousand are employed?", a: 60, sol: "$7 is below the monopsony wage of $8, so it has no effect: employment stays at <b>60 thousand</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A minimum wage set above equilibrium in a competitive labour market is likely to cause:", opts: ["Excess demand for labour", "Unemployment", "Higher employment", "A fall in labour supply"], a: 1, why: "The quantity of labour supplied rises and the quantity demanded falls." },
  { q: "Which minimum wage could raise both the wage and employment?", opts: ["Below the monopsony wage", "Between the monopsony wage and the competitive wage", "Above the competitive wage", "Any minimum wage"], a: 1, why: "In that range the firm is forced to pay more but still wants to hire up to the point where supply runs out." },
  { q: "A minimum wage set below the equilibrium wage in a competitive market will:", opts: ["cause unemployment", "have no effect", "raise wages", "cause a shortage of labour"], a: 1, why: "It is not binding, so the market wage stays above it." },
  { q: "Job losses from a minimum wage are likely to be smaller when:", opts: ["Demand for labour is elastic", "Machines are cheap substitutes", "Demand for labour is inelastic", "The minimum rise is very large"], a: 2, why: "If demand is inelastic, employment falls by a smaller percentage than the wage rises." },
  { q: "Which is an argument for a minimum wage?", opts: ["It may raise productivity and reduce poverty", "It always raises employment", "It lowers firms' costs", "It reduces the supply of labour"], a: 0, why: "Higher pay may raise effort and reduce turnover, and raises the pay of low-paid workers who stay in work." },
  { q: "A minimum wage may not target the poorest households because:", opts: ["The poorest all earn the minimum wage", "Many low-paid workers live in households with other income, and the poorest may have no job", "It is always too low", "It raises benefits"], a: 1, why: "Targeting is imperfect: it helps workers, not the unemployed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Minimum wage", "A legal floor on the hourly wage employers may pay."],
  ["Binding (effective) minimum wage", "One set above the market wage so that it changes the outcome."],
  ["Competitive labour market effect", "A binding minimum cuts quantity demanded, raises quantity supplied: unemployment."],
  ["Monopsony effect", "A minimum between the monopsony and competitive wages raises wage and employment."],
  ["Unemployment from the minimum", "Quantity of labour supplied minus quantity demanded at the minimum wage."],
  ["Insiders and outsiders", "Workers who keep their jobs at the higher wage versus those who lose out."],
  ["Wage bill", "Wage multiplied by employment."],
  ["Elasticity and the minimum wage", "The less elastic the demand for labour, the smaller the job loss."],
  ["Productivity effect", "Higher pay may raise effort and cut turnover, shifting MRP right."],
  ["Substitutability of capital", "The easier machines replace labour, the greater the job losses."],
  ["Targeting", "A minimum wage helps workers, not the unemployed, and not only the poor."],
  ["Alternatives", "Tax credits, training subsidies, anti-discrimination law."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2024 · 32 · Q12] In which situation is the introduction of a minimum wage most likely to raise employment opportunities as well as wages?", opts: ["Firms face intense competition both at home and abroad.", "Labour costs are a high proportion of the total cost of the firm.", "The minimum wage is not high enough to lower the profits of the firms.", "The minimum wage introduced in monopsony is less than the marginal revenue productivity (MRP) of the last worker employed."], a: 3, why: "In a monopsony a minimum wage below the MRP of the last worker raises both the wage and employment. A and B make job losses more likely, and C describes a minimum that is probably not binding." },
  { q: "[May/June 2025 · 34 · Q11] What determines the amount by which employment is reduced if a minimum wage is set 5% above the equilibrium market wage?", opts: ["the average revenue product curve", "the marginal revenue product curve", "the mobility of labour", "the wage rate in other industries"], a: 1, why: "The MRP curve is the demand for labour, and its elasticity (slope) decides how many jobs are lost when the wage rises." },
] });
