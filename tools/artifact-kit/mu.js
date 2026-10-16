/* ---------- shared chart helpers ---------- */
/* Steppers: L (thousand workers) 0-200 on x, wage ($ per hour) 0-28 on y */
const SX = (L) => 80 + L * 3.1, SY = (w) => 330 - w * 10.5;
function sAxes(extra) {
  return SV.line(80, 330, 710, 330) + SV.line(80, 330, 80, 30) + SV.text(710, 368, "Quantity of labour (thousand workers)", "sm", { "text-anchor": "end" }) + SV.text(86, 34, "Wage ($ per hour)", "sm") + (extra || "");
}
function sLine(a, b, L0, L1, cls, o) { return SV.line(SX(L0), SY(a + b * L0), SX(L1), SY(a + b * L1), cls, o); }
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });


/* ---------- 40.4: monopsony and trade unions ---------- */
const HALO = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const Lu = (w) => (w <= 8 ? 60 : Math.min((20 - w) * 10, (w - 2) * 10));        // employment with a union wage w against the monopsony
function monoDraw(s) {
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
  if (s.comp > 0) o += SV.circle(SX(90), SY(11), 7, "dot3", op(s.comp)) + SV.line(SX(90), SY(11), SX(90), SY(0), "gr", op(s.comp)) + SV.text(SX(90), SY(0) + 20, "90", "lbl bd t3", { "text-anchor": "middle", ...op(s.comp) }) + SV.text(SX(90) + 14, SY(11) - 14, "Competitive: 90, $11", "lbl bd t3", op(s.comp));
  if (s.u > 0) {
    const w = s.uw, L = Lu(w);
    o += SV.line(SX(0), SY(w), SX(Math.max(L, (w - 2) * 10)), SY(w), "c3 dash", op(s.u)) + SV.circle(SX(L), SY(w), 7, "dot3", op(s.u)) + SV.line(SX(L), SY(w), SX(L), SY(0), "gr", op(s.u));
    o += SV.text(SX(0) - 6, SY(w) + 4, Lib.fmtN(w, 0), "lbl bd t3", { "text-anchor": "end", ...op(s.u) }) + SV.text(SX(L), SY(0) + 20, Lib.fmtN(L, 0), "lbl bd t3", { "text-anchor": "middle", ...op(s.u) });
    o += SV.text(SX(L) - 10, SY(w) + 44, `Union wage $${Lib.fmtN(w, 0)}: employment ${Lib.fmtN(L, 0)}`, "lbl bd t3", { "text-anchor": "end", style: HALO, ...op(s.u) });
    if ((w - 2) * 10 > L + 0.5) o += SV.rect(SX(L), SY(w), SX((w - 2) * 10) - SX(L), 8, "f2", op(s.u)) + SV.text(SX((L + (w - 2) * 10) / 2), SY(w) - 12, "unemployment " + Lib.fmtN((w - 2) * 10 - L, 0), "sm bd t2", { "text-anchor": "middle", style: HALO, ...op(s.u) });
  }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 390" role="img" aria-label="Monopsony diagram with MRP, ACL and MCL showing the monopsony and competitive outcomes">${monoDraw({ mcl: 1, mono: 1, gap: 1, comp: 1, u: 0, uw: 8 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 370, label: "Monopsony labour market diagram with marginal cost of labour", base: { mcl: 0, mono: 0, gap: 0, comp: 0, u: 0, uw: 8 }, draw: monoDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "The monopsonist's <b>MRP</b> is its demand for labour. As the only buyer it faces the whole market supply curve, which is the <b>average cost of labour (ACL)</b>: the wage it must pay at each level of employment.", s: {} },
  { cap: "To hire one more worker it must raise the wage, and it pays that higher wage to <b>all</b> its workers. So the <b>marginal cost of labour (MCL)</b> lies above the ACL and is steeper.", s: { mcl: 1 } },
  { cap: "It hires where <b>MCL = MRP</b>: <b>60</b> thousand workers. This is the profit-maximising quantity.", s: { mcl: 1, mono: 1 } },
  { cap: "The wage is read <b>down to the ACL (supply) curve</b>: just <b>$8</b>. Workers produce $14 of revenue at the margin but are paid $8: the wage is <b>below MRP</b>.", s: { mcl: 1, mono: 1, gap: 1 } },
  { cap: "In a competitive market ACL would meet MRP at <b>90 thousand workers and $11</b>. So the monopsony pays a <b>lower wage</b> and employs <b>fewer workers</b>.", s: { mcl: 1, mono: 1, gap: 1, comp: 1 } },
] });
Lib.stepper($("#stU"), { w: 760, h: 370, label: "A trade union bargaining a wage with a monopsony employer", base: { mcl: 1, mono: 0.5, gap: 0, comp: 1, u: 0, uw: 8 }, draw: monoDraw, tween: 1000, dwell: 5400, steps: [
  { cap: "<b>The starting point.</b> The monopsony pays <b>$8</b> and employs <b>60 thousand</b> (faint). The competitive wage would be $11 with 90 thousand workers.", s: { mono: 1, comp: 1 } },
  { cap: "<b>The union bargains a wage of $10.</b> The firm can no longer pay less than $10, so extra workers cost only $10 each (the MCL is flat at the union wage). It now hires up to where MRP = $10: <b>80 thousand</b>. <b>Wage and employment both rise.</b>", s: { mono: 0.4, comp: 1, u: 1, uw: 10 } },
  { cap: "<b>A union wage of $11</b> (the competitive wage) takes employment to <b>90 thousand</b>: the outcome of a competitive market. This is the most the union can win <b>without</b> costing jobs.", s: { mono: 0.4, comp: 1, u: 1, uw: 11 } },
  { cap: "<b>A union wage of $13</b> is above the competitive wage. Firms now want only <b>70 thousand</b> (MRP falls below $13 after that) while <b>110 thousand</b> want to work: employment falls and there is <b>unemployment of 40 thousand</b>. The bargain turns from a gain to a loss for some workers.", s: { mono: 0.4, comp: 1, u: 1, uw: 13 } },
] });

/* union in a competitive labour market */
function unionDraw(s) {
  let o = sAxes();
  o += sLine(20, -0.1, 0, 200, "c1") + SV.text(SX(12), SY(18.8) - 12, "D = MRP", "lbl bd t1");
  o += sLine(4, 0.1, 0, 200, "c2") + SV.text(SX(200) - 4, SY(24) - 8, "S", "lbl bd t2", { "text-anchor": "end" });
  if (s.e > 0) o += SV.line(SX(80), SY(12), SX(80), SY(0), "gr", op(s.e)) + SV.line(SX(0), SY(12), SX(80), SY(12), "gr", op(s.e)) + SV.circle(SX(80), SY(12), 7, "dot3", op(s.e)) + SV.text(SX(80), SY(0) + 20, "80", "lbl bd", { "text-anchor": "middle", ...op(s.e) }) + SV.text(SX(0) - 6, SY(12) + 4, "12", "lbl bd", { "text-anchor": "end", ...op(s.e) }) + SV.text(SX(80) + 12, SY(12) + 22, "Equilibrium", "lbl bd t3", op(s.e));
  if (s.m > 0) o += SV.line(SX(0), SY(14), SX(200), SY(14), "c4 dash", op(s.m)) + SV.text(SX(0) - 6, SY(14) + 4, "14", "lbl bd t4", { "text-anchor": "end", ...op(s.m) }) + SV.text(SX(200) - 4, SY(14) - 8, "Union wage $14", "lbl bd t4", { "text-anchor": "end", ...op(s.m) });
  if (s.q > 0) o += SV.circle(SX(60), SY(14), 6, "dot1", op(s.q)) + SV.circle(SX(100), SY(14), 6, "dot2", op(s.q)) + SV.line(SX(60), SY(14), SX(60), SY(0), "gr", op(s.q)) + SV.line(SX(100), SY(14), SX(100), SY(0), "gr", op(s.q)) + SV.text(SX(60), SY(0) + 20, "60", "lbl bd t1", { "text-anchor": "middle", ...op(s.q) }) + SV.text(SX(100), SY(0) + 20, "100", "lbl bd t2", { "text-anchor": "middle", ...op(s.q) });
  if (s.u > 0) o += SV.rect(SX(60), SY(14), SX(100) - SX(60), 14, "f2", op(s.u)) + SV.text((SX(60) + SX(100)) / 2, SY(14) + 62, "Unemployment 40", "lbl bd t2", { "text-anchor": "middle", ...op(s.u) });
  if (s.d2 > 0) o += sLine(22, -0.1, 0, 200, "c3", op(s.d2)) + SV.text(SX(12), SY(20.8) - 12, "D2: MRP after productivity gain", "lbl bd t3", op(s.d2)) + SV.circle(SX(80), SY(14), 7, "dot3", op(s.d2)) + SV.line(SX(80), SY(14), SX(80), SY(0), "gr", op(s.d2));
  return o;
}
Lib.stepper($("#stV"), { w: 760, h: 370, label: "A trade union wage in a competitive labour market and the effect of rising productivity", base: { e: 0, m: 0, q: 0, u: 0, d2: 0 }, draw: unionDraw, tween: 1000, dwell: 5400, steps: [
  { cap: "In a competitive market the wage settles at <b>$12 and 80 thousand workers</b>.", s: { e: 1 } },
  { cap: "The union bargains a wage of <b>$14</b>, above equilibrium. This acts like a minimum wage.", s: { e: 0.5, m: 1 } },
  { cap: "At $14 firms want only <b>60</b> thousand workers but <b>100</b> thousand are willing to work: <b>unemployment of 40 thousand</b>. Members who keep their jobs (the insiders) gain $2 an hour; the outsiders lose.", s: { e: 0.5, m: 1, q: 1, u: 1 } },
  { cap: "<b>But the union may also raise productivity</b> (training, motivation, lower turnover). MPP and so MRP rise, and the demand for labour shifts right to D2. At $14 the firm now employs <b>80 thousand</b> again: the higher wage costs no jobs.", s: { e: 0.4, m: 1, q: 0.4, u: 0.3, d2: 1 } },
] });

/* ---------- Lab 1: monopsonist's choice ---------- */
function lab1() {
  if (!$("#ma") || !$("#ms")) return;
  const a = +$("#ma").value, s = +$("#ms").value, Lm = (a - 2) / (0.1 + 2 * s), Wm = 2 + s * Lm, Mrp = a - 0.1 * Lm, Lc = (a - 2) / (0.1 + s), Wc = 2 + s * Lc;
  $("#p1").textContent = "$" + Lib.fmtN(Wm, 2); $("#p2").textContent = Lib.fmtN(Lm, 0) + "k"; $("#p3").textContent = "$" + Lib.fmtN(Wc, 1) + ", " + Lib.fmtN(Lc, 0) + "k"; $("#p4").textContent = "$" + Lib.fmtN(Mrp - Wm, 2);
  $("#pv").textContent = `The monopsony hires ${Lib.fmtN(Lm, 0)} thousand (where MCL = MRP) at a wage of $${Lib.fmtN(Wm, 2)}, which is $${Lib.fmtN(Mrp - Wm, 2)} below the MRP of the last worker. A competitive market would employ ${Lib.fmtN(Lc, 0)} thousand at $${Lib.fmtN(Wc, 1)}. ${s >= 0.15 ? "A steeper supply curve (less elastic) widens the gap between MCL and ACL, so the wage gap below MRP is bigger." : "A flatter supply curve (more elastic) means MCL is close to ACL, so monopsony power is weaker."}`;
  const X = (l) => 50 + l * 1.5, Y = (w) => 270 - w * 8.5, top = 28;
  let o = SV.line(50, 270, 400, 270) + SV.line(50, 270, 50, 20) + SV.text(396, 290, "Labour (thousand)", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Wage ($/hr)", "sm");
  const lm = Math.min(230, a / 0.1), ls = (top - 2) / s, lc = (top - 2) / (2 * s);
  o += SV.line(X(0), Y(a), X(lm), Y(Math.max(0, a - 0.1 * lm)), "c1") + SV.line(X(0), Y(2), X(Math.min(230, ls)), Y(Math.min(top, 2 + s * Math.min(230, ls))), "c2") + SV.line(X(0), Y(2), X(Math.min(230, lc)), Y(Math.min(top, 2 + 2 * s * Math.min(230, lc))), "c4");
  o += SV.text(X(lm) - 4, Y(Math.max(0, a - 0.1 * lm)) - 6, "MRP", "lbl bd t1", { "text-anchor": "end" }) + SV.text(X(Math.min(230, ls)) - 2, Y(Math.min(top, 2 + s * Math.min(230, ls))) + 14, "ACL", "lbl bd t2", { "text-anchor": "end" }) + SV.text(X(Math.min(230, lc)) + 3, Y(Math.min(top, 2 + 2 * s * Math.min(230, lc))) - 4, "MCL", "lbl bd t4");
  o += SV.line(X(Lm), Y(Mrp), X(Lm), 270, "gr") + SV.line(50, Y(Wm), X(Lm), Y(Wm), "gr") + SV.circle(X(Lm), Y(Mrp), 5, "dot4") + SV.circle(X(Lm), Y(Wm), 6, "dot2") + SV.circle(X(Lc), Y(Wc), 6, "dot3");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ma", label: "Strength of demand (MRP intercept $): ", min: 14, max: 26, step: 1, value: 20, fmt: (v) => v, onInput: lab1 });
Lib.slider($("#g2"), { id: "ms", label: "Steepness of supply (s in W = 2 + sL): ", min: 0.05, max: 0.2, step: 0.01, value: 0.1, fmt: (v) => v.toFixed(2), onInput: lab1 });

/* ---------- Lab 2: union with a monopsony ---------- */
function lab2() {
  if (!$("#uw")) return;
  const mw = +$("#uw").value; let W, L, un = 0, note;
  if (mw <= 8) { W = 8; L = 60; note = `A union wage of $${mw.toFixed(1)} is no better than the monopsony wage of $8, so nothing changes.`; }
  else if (mw <= 11) { W = mw; L = (mw - 2) * 10; note = `Between the monopsony wage ($8) and the competitive wage ($11): wage and employment both rise. The firm must pay $${mw.toFixed(1)} and still finds it profitable to hire up to the point where supply runs out.`; }
  else { W = mw; L = (20 - mw) * 10; un = (mw - 2) * 10 - L; note = `Above the competitive wage ($11), MRP is below the union wage for the marginal worker, so employment falls and there is unemployment of ${Lib.fmtN(un, 0)} thousand.`; }
  const gap = 20 - 0.1 * L - W;
  $("#q1").textContent = "$" + Lib.fmtN(W, 2); $("#q2").textContent = Lib.fmtN(L, 0) + "k"; $("#q3").textContent = "$" + Lib.fmtN(Math.max(0, gap), 2); $("#q4").textContent = Lib.fmtN(un, 0) + "k"; $("#qv").textContent = note;
  const X = (l) => 50 + l * 1.75, Y = (w) => 260 - w * 11.5;
  let o = SV.line(50, 260, 410, 260) + SV.line(50, 260, 50, 20) + SV.text(406, 280, "Labour (thousand)", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Wage ($/hr)", "sm");
  o += SV.line(X(0), Y(20), X(200), Y(0), "c1") + SV.text(X(200) - 2, Y(0) - 6, "MRP", "lbl bd t1", { "text-anchor": "end" }) + SV.line(X(0), Y(2), X(180), Y(20), "c2") + SV.text(X(180) + 3, Y(20) + 14, "S", "lbl bd t2") + SV.line(X(0), Y(2), X(90), Y(20), "c4") + SV.text(X(90) + 4, Y(20) - 2, "MCL", "lbl bd t4");
  if (mw > 8) o += SV.line(X(0), Y(mw), X(Math.max(L, (mw - 2) * 10)), Y(mw), "c3 dash");
  if (gap > 0.05) o += SV.rect(X(L) - 4, Y(20 - 0.1 * L), 4, Y(W) - Y(20 - 0.1 * L), "f2");
  o += SV.line(X(L), Y(W), X(L), 260, "gr") + SV.circle(X(L), Y(W), 6, "dot3") + SV.circle(X(L), Y(20 - 0.1 * L), 4, "dot4");
  if (un > 0) o += SV.rect(X(L), Y(W), X((mw - 2) * 10) - X(L), 8, "f2");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "uw", label: "Union wage ($ per hour): ", min: 4, max: 16, step: 0.5, value: 8, fmt: (v) => v.toFixed(1), onInput: lab2 });

/* ---------- Lab 3: union in a competitive market ---------- */
function lab3() {
  if (!$("#uc") || !$("#ug")) return;
  const uc = +$("#uc").value, g = +$("#ug").value, a = 20 + g, b = 4, Le = (a - b) / 0.2, We = (a + b) / 2, bind = uc > We + 0.001;
  const W = bind ? uc : We, Ld = bind ? Math.max(0, (a - uc) * 10) : Le, Ls = bind ? (uc - b) * 10 : Le, un = Ls - Ld;
  $("#u1").textContent = "$" + Lib.fmtN(W, 2); $("#u2").textContent = Lib.fmtN(Ld, 0) + "k"; $("#u3").textContent = Lib.fmtN(un, 0) + "k"; $("#u4").textContent = "$" + Lib.fmtN(W * Ld, 0) + "k/hr";
  $("#uv").textContent = uc === 0 ? `No union wage: the market clears at $${Lib.fmtN(We, 2)} and ${Lib.fmtN(Le, 0)} thousand workers.`
    : !bind ? `The union wage ($${uc}) is not above the equilibrium wage ($${Lib.fmtN(We, 2)}), so nothing changes.`
    : `A union wage of $${uc}: employment is ${Lib.fmtN(Ld, 0)} thousand (equilibrium would be ${Lib.fmtN(Le, 0)}) and ${Lib.fmtN(un, 0)} thousand people who want work cannot get it.${g > 0 ? " The productivity gain has shifted MRP to the right, cutting the job loss." : " Try raising productivity."}`;
  const X = (l) => 50 + l * 1.75, Y = (w) => 260 - w * 8.2;
  let o = SV.line(50, 260, 410, 260) + SV.line(50, 260, 50, 20) + SV.text(406, 280, "Labour (thousand)", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "Wage ($/hr)", "sm");
  const De = Math.min(200, a * 10);
  o += SV.line(X(0), Y(a), X(De), Y(a - 0.1 * De), "c1") + SV.text(X(De) - 4, Y(a - 0.1 * De) - 6, "D", "lbl bd t1", { "text-anchor": "end" }) + SV.line(X(0), Y(b), X(200), Y(b + 20), "c2") + SV.text(X(200) - 4, Y(b + 20) - 6, "S", "lbl bd t2", { "text-anchor": "end" });
  o += SV.circle(X(Le), Y(We), 5, "dot3", { opacity: bind ? 0.4 : 1 });
  if (uc > 0) { o += SV.line(X(0), Y(uc), X(200), Y(uc), "c4 dash"); if (bind) o += SV.rect(X(Ld), Y(uc), X(Ls) - X(Ld), 10, "f2") + SV.circle(X(Ld), Y(uc), 5, "dot1") + SV.circle(X(Ls), Y(uc), 5, "dot2") + SV.line(X(Ld), Y(uc), X(Ld), 260, "gr") + SV.line(X(Ls), Y(uc), X(Ls), 260, "gr"); }
  $("#labC").innerHTML = o;
}
Lib.slider($("#g4"), { id: "uc", label: "Union wage ($ per hour, 0 = none): ", min: 0, max: 20, step: 0.5, value: 14, fmt: (v) => (v === 0 ? "none" : v.toFixed(1)), onInput: lab3 });
Lib.slider($("#g5"), { id: "ug", label: "Productivity gain from union deal (MRP up by $): ", min: 0, max: 6, step: 1, value: 0, fmt: (v) => "+" + v, onInput: lab3 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which market structure does each statement describe?",
  buckets: [{ label: "Competitive labour market" }, { label: "Monopsony" }, { label: "Both" }],
  items: [
    { text: "The firm hires where wage = MRP", b: 0 }, { text: "The firm hires where MCL = MRP", b: 1 },
    { text: "The wage paid is below MRP", b: 1 }, { text: "MCL lies above the supply curve", b: 1 },
    { text: "The firm faces a horizontal supply of labour at the market wage", b: 0 },
    { text: "A union wage above equilibrium reduces employment", b: 0 }, { text: "A union wage in a range can raise employment", b: 1 },
    { text: "Demand for labour is derived from demand for the product", b: 2 }, { text: "MRP = MPP × MR", b: 2 },
  ], done: "Keep the two cases apart in an exam diagram.",
});
Lib.classify($("#cl2"), {
  prompt: "Does each factor raise or reduce a union's power to win higher pay?",
  buckets: [{ label: "Raises union power" }, { label: "Reduces union power" }],
  items: [
    { text: "Inelastic demand for the union's labour", b: 0 }, { text: "A high proportion of the workforce are members", b: 0 }, { text: "The firm is very profitable", b: 0 }, { text: "No close substitutes for the workers", b: 0 }, { text: "Inelastic demand for the firm's product", b: 0 },
    { text: "Machines can easily replace workers", b: 1 }, { text: "High unemployment gives the firm a pool of replacements", b: 1 }, { text: "Elastic demand for the firm's product", b: 1 }, { text: "Laws restrict strikes", b: 1 }, { text: "The firm can move production abroad", b: 1 },
  ], done: "Elasticity of demand for the labour is the central idea.",
});
Lib.order($("#o1"), { prompt: "Order the steps for analysing a monopsony on a diagram.", items: [
  "Draw the MRP curve (demand for labour) and the ACL curve (supply of labour)",
  "Draw the MCL curve above and steeper than the ACL curve",
  "Find where MCL = MRP: this is the profit-maximising employment",
  "Read down from that point to the horizontal axis to find the quantity of labour",
  "Read up from that quantity to the ACL curve to find the wage",
  "Compare with the competitive outcome where ACL meets MRP: wage and employment are lower",
], done: "A reliable exam routine." });
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Monopsony", "A market with a single buyer of labour"],
  ["Average cost of labour (ACL)", "The wage paid at each level of employment: the supply curve facing the firm"],
  ["Marginal cost of labour (MCL)", "The extra cost of employing one more worker"],
  ["Bilateral monopoly", "A single buyer of labour facing a single seller, such as one employer and one union"],
  ["Trade union", "An organisation of workers that bargains collectively over pay and conditions"],
  ["Insiders and outsiders", "Union members who keep their jobs versus those left out of work"],
  ["Collective bargaining", "Negotiation of pay and conditions by a union on behalf of its members"],
  ["Industrial action", "Strikes or other action taken by workers to support a pay claim"],
], done: "Eight terms for monopsony and unions." });
Lib.calc($("#c1"), { qs: [
  { q: "A monopsony has MRP = 20 − 0.1L and MCL = 2 + 0.2L (L in thousands). Find the profit-maximising employment (thousand).", a: 60, hint: "Set MCL = MRP and solve for L.", sol: "2 + 0.2L = 20 − 0.1L → 0.3L = 18 → L = <b>60</b>." },
  { q: "The supply curve (ACL) is W = 2 + 0.1L. At 60 thousand workers, what wage ($) does the monopsony pay?", a: 8, sol: "W = 2 + 0.1 × 60 = <b>$8</b>. MRP at 60 is $14, so the wage is $6 below MRP." },
  { q: "In a competitive market the same demand and supply meet where 20 − 0.1L = 2 + 0.1L. What is the competitive employment (thousand)?", a: 90, sol: "0.2L = 18 → L = <b>90</b>. The competitive wage is $11." },
  { q: "A union secures a wage of $10 from the monopsony above (MRP = 20 − 0.1L, supply W = 2 + 0.1L, L in thousands). How many thousand workers are employed?", a: 80, hint: "Employment is the smaller of: the quantity where MRP = $10, and the quantity supplied at $10.", sol: "MRP = 10 gives L = 100. Supply at $10 is (10 − 2) × 10 = 80. Employment is the smaller, <b>80</b>." },
  { q: "Demand W = 20 − 0.1L, supply W = 4 + 0.1L. A union wage of $14 is set. How many thousand are unemployed?", a: 40, hint: "Qd = (20 − 14) × 10, Qs = (14 − 4) × 10.", sol: "Qd = 60, Qs = 100, unemployment = <b>40</b>." },
  { q: "A union raises the wage from $12 to $14 and employment falls from 80 to 60 thousand. What is the percentage fall in employment (%)?", a: 25, sol: "(80 − 60) ÷ 80 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "For a monopsonist the MCL is above the supply curve because:", opts: ["Workers are more productive", "A higher wage to attract one more worker must be paid to all its workers", "Demand is falling", "Unions raise the wage"], a: 1, why: "Hiring one more worker raises the wage bill for everyone already employed." },
  { q: "Compared with a competitive market, a monopsony is likely to lead to:", opts: ["A higher wage and higher employment", "A lower wage and lower employment", "A lower wage and higher employment", "A higher wage and lower employment"], a: 1, why: "It hires where MCL = MRP, which is less than the competitive quantity, and pays the lower wage from the supply curve." },
  { q: "A union wage above equilibrium in a competitive labour market is likely to cause:", opts: ["Excess demand for labour", "Unemployment", "Higher employment", "A fall in labour supply"], a: 1, why: "Quantity supplied rises and quantity demanded falls." },
  { q: "Which union wage could raise both the wage and employment against a monopsony?", opts: ["Below the monopsony wage", "Between the monopsony wage and the competitive wage", "Above the competitive wage", "Any union wage"], a: 1, why: "In that range the firm is forced to pay more but still wants to hire up to the point where supply runs out." },
  { q: "A union is more likely to win higher pay without job losses when the demand for its labour is:", opts: ["very elastic", "inelastic", "falling", "perfectly elastic"], a: 1, why: "Few substitutes means firms cut few jobs when the wage rises." },
  { q: "A union deal that raises productivity could allow a higher wage without lost jobs because:", opts: ["MRP shifts to the right", "Supply shifts to the left", "MCL falls", "Demand for the product falls"], a: 0, why: "Higher MPP raises MRP, so the higher wage is justified." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Monopsony", "A market with a single buyer of labour, able to set the wage."],
  ["Average cost of labour (ACL)", "The wage paid at each level of employment: the supply curve facing a monopsony."],
  ["Marginal cost of labour (MCL)", "The extra cost of employing one more worker. Above ACL for a monopsony."],
  ["Monopsony outcome", "Hire where MCL = MRP, pay the wage on the ACL curve: lower wage and employment than competition."],
  ["Wage below MRP", "The monopsony pays workers less than the revenue they add at the margin."],
  ["Trade union", "An organisation of workers that bargains collectively over pay and conditions."],
  ["Collective bargaining", "Negotiation by a union on behalf of its members."],
  ["Bilateral monopoly", "A single buyer of labour facing a single seller, such as one employer and one union."],
  ["Insiders and outsiders", "Members who keep jobs at the higher wage versus those who lose out."],
  ["Union power", "Greater when demand for labour is inelastic, membership is high and the firm is profitable."],
  ["Productivity deal", "Higher pay in return for higher output, shifting MRP right so jobs are kept."],
  ["Industrial action", "Strikes or other action in support of a pay claim."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2022 · 32 · Q17] When is a trade union less likely to gain a large pay rise for its workers?", opts: ["It represents a large proportion of the workforce in the company.", "It represents a workforce that has an elastic demand for its labour.", "It represents a workforce that is increasing its labour productivity.", "It represents a workforce that works for a highly profitable monopoly firm."], a: 1, why: "If demand for the labour is elastic, a pay rise leads to large job losses, which weakens the union's position. A, C and D all strengthen it." },
  { q: "[Oct/Nov 2023 · 32 · Q10] Firm K operates in a competitive market. Firm L is a monopsony employer. Trade unions are introduced with the result that wages in each firm are increased. What is the likely effect on each firm? (firm K / firm L)", opts: ["employment will decrease / employment will decrease", "employment will decrease / employment will increase", "employment will increase / employment will decrease", "employment will increase / employment will increase"], a: 1, why: "In the competitive firm a wage above equilibrium cuts employment. In the monopsony a higher wage (up to the competitive level) can raise employment." },
  { q: "[May/June 2025 · 34 · Q12] What will increase the power of a trade union, allowing it to increase wages without reducing the employment of its members in a particular industry?", opts: ["The economy is experiencing a fall in the price of capital.", "The economy is experiencing rising employment.", "The price elasticity of demand for the industry's goods is equal to 1.", "The price elasticity of demand for the industry's goods is greater than 1."], a: 1, why: "When employment in the economy is rising, labour is in demand, so a wage rise is less likely to cost members' jobs. A cheaper price of capital makes substitution easier, and elastic product demand makes job losses larger." },
  { q: "[Oct/Nov 2022 · 31 · Q16] A government is worried about the increasing monopsony power of employers in the wage bargaining process. Which policy combination is most likely to improve the wages and employment prospects of workers? (trade union powers / immigration controls / national minimum wage)", opts: ["strengthen / relax / cut", "strengthen / strengthen / raise", "weaken / relax / cut", "weaken / strengthen / raise"], a: 1, why: "Stronger unions offset employer power, tighter immigration controls reduce the supply of labour and raise wages, and a higher minimum wage helps in a monopsony." },
] });
