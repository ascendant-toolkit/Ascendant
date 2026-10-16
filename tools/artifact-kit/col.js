/* ---------- model: demand P = 20 - Q (MR = 20 - 2Q), constant MC = 4, two firms ----------
   competition: Q = 16, P = 4.  Cartel: MR = MC at Q = 8, P = 12, joint profit 64 (32 each). */
const op = (v) => ({ style: `opacity:${Math.max(0, Math.min(1, v))}` });
const opf = (v, k = 1) => ({ style: `opacity:${Math.max(0, Math.min(1, v)) * 0.28 * k}` });
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:5px";
const fr = (x0, xs, y0, ys) => ({ X: (q) => x0 + q * xs, Y: (p) => y0 - p * ys, x0, y0 });
const BIG = fr(70, 34, 340, 14.5), SMALL = fr(52, 22, 320, 13);
const Dm = (q) => 20 - q, MRm = (q) => 20 - 2 * q, MCc = 4;

function marketDraw(F, W, s) {
  const { X, Y } = F;
  let o = SV.line(F.x0, Y(22), F.x0, Y(0)) + SV.line(F.x0, Y(0), W, Y(0)) + SV.text(F.x0 + 6, Y(22) - 2, "Price / cost ($)", "sm") + SV.text(W - 2, Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" });
  const qm = s.qm ?? 8;
  if ((s.prof ?? 0) > 0) {
    const pm = Dm(qm);
    if ((s.split ?? 0) > 0.5) {
      o += SV.rect(X(0), Y(pm), X(qm / 2) - X(0), Y(MCc) - Y(pm), "f3", opf(s.prof, 1.2)) + SV.rect(X(qm / 2), Y(pm), X(qm) - X(qm / 2), Y(MCc) - Y(pm), "f1", opf(s.prof, 1.4));
      o += SV.text(X(qm / 4), Y(pm) + 20, "Firm A", "lbl bd t3", { "text-anchor": "middle", ...op(s.split) }) + SV.text(X(3 * qm / 4), Y(pm) + 20, "Firm B", "lbl bd t1", { "text-anchor": "middle", ...op(s.split) });
    } else o += SV.rect(X(0), Y(pm), X(qm) - X(0), Y(MCc) - Y(pm), "f3", opf(s.prof, 1.2));
    o += SV.text(X(0.4), Y(MCc) - 10, "joint profit $" + fmtN((pm - MCc) * qm, 0), "lbl bd t3", { style: `${halo};opacity:${Math.max(0, Math.min(1, s.prof))}` });
  }
  if ((s.dwl ?? 0) > 0) o += SV.poly([[X(qm), Y(Dm(qm))], [X(qm), Y(MCc)], [X(16), Y(MCc)]], "f2", opf(s.dwl, 1.6)) + SV.text(X(qm) + 14, Y(5.4), "deadweight loss $" + fmtN(0.5 * (16 - qm) * (16 - qm), 0), "lbl bd t2", { style: `${halo};opacity:${Math.max(0, Math.min(1, s.dwl))}` });
  o += SV.line(X(0), Y(20), X(20), Y(0), "c1", op(s.d ?? 1)) + SV.text(X(20) - 4, Y(0) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d ?? 1) });
  if ((s.mc ?? 0) > 0) o += SV.line(X(0), Y(MCc), X(20), Y(MCc), "c2", op(s.mc)) + SV.text(X(20) - 4, Y(MCc) - 7, "MC = $4", "lbl bd t2", { "text-anchor": "end", ...op(s.mc) });
  if ((s.mr ?? 0) > 0) o += SV.line(X(0), Y(20), X(10), Y(0), "c3 dash", op(s.mr)) + SV.text(X(10) + 6, Y(0) - 8, "MR", "lbl bd t3", op(s.mr));
  if ((s.comp ?? 0) > 0) o += SV.line(X(16), Y(MCc), X(16), Y(0), "gr", op(s.comp)) + SV.circle(X(16), Y(MCc), 7, "dot2", op(s.comp)) + SV.text(X(16), Y(0) + 18, "16", "sm bd", { "text-anchor": "middle", ...op(s.comp) }) + SV.text(X(16) - 10, Y(MCc) + 26, "competition: Q = 16, P = $4", "lbl bd t2", { "text-anchor": "end", style: `${halo};opacity:${Math.max(0, Math.min(1, s.comp))}` });
  if ((s.car ?? 0) > 0) {
    const pm = Dm(qm);
    o += SV.line(X(qm), Y(0), X(qm), Y(pm), "gr", op(s.car)) + SV.circle(X(qm), Y(MCc), 6, "dot3", op(s.car)) + SV.text(X(qm), Y(0) + 18, fmtN(qm, 1).replace(".0", ""), "sm bd", { "text-anchor": "middle", ...op(s.car) });
  }
  if ((s.pr ?? 0) > 0) {
    const pm = Dm(qm);
    o += SV.line(F.x0, Y(pm), X(qm), Y(pm), "gr", op(s.pr)) + SV.circle(X(qm), Y(pm), 7, "dot1", op(s.pr)) + SV.text(F.x0 - 6, Y(pm) + 4, "$" + fmtN(pm, 0), "sm bd", { "text-anchor": "end", ...op(s.pr) }) + SV.text(X(qm) + 12, Y(pm) - 10, "cartel: Q = " + fmtN(qm, 0) + ", P = $" + fmtN(pm, 0), "lbl bd t1", { style: `${halo};opacity:${Math.max(0, Math.min(1, s.pr))}` });
  }
  return o;
}
const ALLM = { d: 1, mc: 1, mr: 1, comp: 1, car: 1, pr: 1, prof: 1, dwl: 1, split: 0 };
$("#pic1").innerHTML = `<svg viewBox="0 0 780 380" role="img" aria-label="Market diagram showing competitive output and price, and the higher cartel price with joint profit and deadweight loss">${marketDraw(BIG, 780, ALLM)}</svg>`;

/* Watch 1 */
Lib.stepper($("#stA"), { w: 780, h: 380, label: "From competition to a cartel on a market diagram", base: { d: 0, mc: 0, mr: 0, comp: 0, car: 0, pr: 0, prof: 0, dwl: 0, split: 0 }, draw: (s) => marketDraw(BIG, 780, s), tween: 900, dwell: 5600, steps: [
  { cap: "<b>The market.</b> Demand is P = 20 − Q and each unit costs $4 to make (MC = $4). Two firms share the market.", s: { d: 1, mc: 1 } },
  { cap: "<b>Competition.</b> If the firms compete, price is driven down to marginal cost: <b>16 units at $4</b>. Profit is close to zero and consumers get the most for their money.", s: { d: 1, mc: 1, comp: 1 } },
  { cap: "<b>What a monopolist would do.</b> If the two firms acted as one, they would work out the marginal revenue from the whole market. MR = 20 − 2Q falls twice as fast as demand.", s: { d: 1, mc: 1, comp: 1, mr: 1 } },
  { cap: "<b>Profit-maximising output.</b> The joint profit is largest where MR = MC: 20 − 2Q = 4, so total output should be <b>8 units</b>, half the competitive output.", s: { d: 1, mc: 1, comp: 1, mr: 1, car: 1 } },
  { cap: "<b>The price.</b> At 8 units consumers are willing to pay <b>$12</b>. The price rises from $4 to $12, and the shaded box is the <b>joint profit: (12 − 4) x 8 = $64</b>.", s: { d: 1, mc: 1, comp: 1, mr: 1, car: 1, pr: 1, prof: 1 } },
  { cap: "<b>The cost to society.</b> Units between 8 and 16 are worth more to consumers than they cost to make, but are no longer produced. This is the <b>deadweight loss</b> ($32 here).", s: { d: 1, mc: 1, comp: 1, mr: 1, car: 1, pr: 1, prof: 1, dwl: 1 } },
  { cap: "<b>The agreement.</b> To hold the price at $12 the firms agree <b>output quotas</b>: 4 units each, so each earns $32. This is a formal cartel. The next animation shows why it is hard to keep.", s: { d: 1, mc: 1, comp: 1, mr: 1, car: 1, pr: 1, prof: 1, dwl: 1, split: 1 } },
] });

/* Watch 2: the cheating dilemma */
const PAY = [[[32, 32], [28, 35]], [[35, 28], [30, 30]]];
Lib.stepper($("#stB"), {
  w: 760, h: 400, label: "Payoff matrix for two cartel members choosing to keep the quota or cheat", base: { a1: 0, a2: 0, b1: 0, b2: 0, n: 0 },
  draw: (s) => {
    const x0 = 210, y0 = 90, w = 250, h = 120, names = ["keep quota (4)", "cheat (5)"];
    let o = SV.text(x0 + w, 40, "Firm B", "lbl bd", { "text-anchor": "middle" }) + SV.text(40, y0 + h, "Firm A", "lbl bd", { "text-anchor": "middle", transform: `rotate(-90 40 ${y0 + h})` });
    for (let k = 0; k < 2; k++) o += SV.text(x0 + w * k + w / 2, y0 - 14, names[k], "lbl", { "text-anchor": "middle" }) + SV.text(x0 - 12, y0 + h * k + h / 2 + 5, names[k], "lbl", { "text-anchor": "end" });
    for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++) {
      const cx = x0 + w * j, cy = y0 + h * i, nash = i === 1 && j === 1;
      o += SV.rect(cx, cy, w, h, nash && s.n ? "f2" : "cell", { rx: 10, style: nash && s.n ? "" : "fill:var(--soft);stroke:var(--line);stroke-width:2;opacity:1" });
      o += SV.text(cx + w / 2 - 50, cy + h / 2 + 8, PAY[i][j][0], "lbl bd t1", { "text-anchor": "middle", style: "font-size:30px" }) + SV.text(cx + w / 2 + 50, cy + h / 2 + 8, PAY[i][j][1], "lbl bd t2", { "text-anchor": "middle", style: "font-size:30px" });
      o += SV.text(cx + w / 2 - 50, cy + 24, "A", "sm", { "text-anchor": "middle" }) + SV.text(cx + w / 2 + 50, cy + 24, "B", "sm", { "text-anchor": "middle" });
    }
    const ring = (i, j, who, op_) => op_ ? SV.circle(x0 + w * j + w / 2 + (who ? 50 : -50), y0 + h * i + h / 2 - 2, 30, "dot4", { style: "fill:none;stroke:var(--warn);stroke-width:4", opacity: op_ }) : "";
    o += ring(1, 0, 0, s.a1) + ring(1, 1, 0, s.a2) + ring(0, 1, 1, s.b1) + ring(1, 1, 1, s.b2);
    o += SV.text(x0 + w, y0 + 2 * h + 36, "Profit in $: Firm A in blue, Firm B in red. Circles mark the best response.", "sm", { "text-anchor": "middle" });
    if (s.n) o += SV.text(x0 + w, y0 + 2 * h + 62, "Both cheat: $30 each, $60 in total. Keeping the quota would give $32 each, $64 in total.", "lbl bd t2", { "text-anchor": "middle", opacity: s.n });
    return o;
  },
  steps: [
    { cap: "<b>The agreement.</b> Each firm may keep its quota of 4 units (profit $32 each) or secretly cheat by producing 5. The matrix shows each firm's profit for every combination.", s: {} },
    { cap: "<b>If B keeps the quota</b>, A compares $32 (keep) with $35 (cheat: price falls only to $11 and A sells 5). A is better off cheating.", s: { a1: 1 } },
    { cap: "<b>If B cheats</b>, A compares $28 (keep: price falls to $11 but A sells only 4) with $30 (cheat). A is better off cheating again. <b>Cheating is a dominant strategy.</b>", s: { a1: 1, a2: 1 } },
    { cap: "B faces exactly the same choice, so B cheats as well, whatever A does.", s: { a1: 1, a2: 1, b1: 1, b2: 1 } },
    { cap: "<b>The cartel breaks down.</b> Both firms cheat and each earns $30, less than the $32 each from keeping the quota. Total output of 10 pushes the price down to $10. In practice, members try to prevent this through monitoring, penalties and repeated dealing.", s: { a1: 1, a2: 1, b1: 1, b2: 1, n: 1 } },
  ],
});

/* Watch 3: price leadership */
const LEAD = [[1, 1], [2, 2], [2, 2], [3, 3]];  /* time each firm switches: leader, B, C, D */
const SW = [1, 2, 2, 3], NM = ["Leader", "Firm B", "Firm C", "Firm D"], CL = ["c1", "c2", "c3", "c4"], TX = ["t1", "t2", "t3", "t4"];
function plDraw(s) {
  const X = (t) => 100 + t * 150, Y = (p) => 330 - (p - 9) * 80;
  let o = SV.line(100, Y(12), 100, Y(9)) + SV.line(100, Y(9), 720, Y(9)) + SV.text(106, Y(12) - 4, "Price ($)", "sm") + SV.text(720, Y(9) + 26, "Time (months)", "sm", { "text-anchor": "end" });
  for (let t = 0; t <= 4; t++) o += SV.text(X(t), Y(9) + 18, t, "sm bd", { "text-anchor": "middle" });
  for (let p = 9; p <= 12; p++) o += SV.text(94, Y(p) + 4, "$" + p, "sm bd", { "text-anchor": "end" }) + SV.line(100, Y(p), 720, Y(p), "gr");
  const T = s.t;
  SW.forEach((sw, k) => {
    const dy = (k - 1.5) * 3.5, pts = [];
    for (let t = 0; t <= T + 1e-9; t += 0.05) pts.push([X(t), Y(t >= sw ? 11 : 10) + dy]);
    if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), CL[k], { "stroke-width": 3 });
    o += SV.text(X(T) + 8, Y(T >= sw ? 11 : 10) + (k - 1.5) * 14 + 4, NM[k], "sm bd " + TX[k]);
  });
  if (s.m > 0) o += SV.text(410, 60, "No meeting. No agreement. Prices rise together.", "lbl bd t2", { "text-anchor": "middle", ...op(s.m) });
  return o;
}
Lib.stepper($("#stC"), { w: 780, h: 400, label: "Four firms following a price leader over time", base: { t: 0, m: 0 }, draw: plDraw, tween: 1400, dwell: 5600, steps: [
  { cap: "<b>The starting position.</b> Four firms in a market all charge $10. The first firm, the leader, is the largest (or the one rivals watch most closely).", s: { t: 0 } },
  { cap: "<b>The leader moves.</b> After its costs rise, the leader raises its price to $11. The other firms notice but do not respond yet.", s: { t: 1.2 } },
  { cap: "<b>Followers join.</b> Firms B and C raise their prices to $11 as well. They fear a price gap would either cost them sales (if they stay high alone) or start a price war (if they cut).", s: { t: 2.4 } },
  { cap: "<b>The last follower.</b> Firm D matches the new price. All firms charge $11, with <b>no meeting, no agreement</b>. This is tacit collusion: price leadership.", s: { t: 4, m: 1 } },
  { cap: "<b>Why it is hard to prove.</b> A cost increase for the whole industry could also explain why all the prices rose together. Regulators need extra evidence, such as signalling or exchange of information, before treating it as collusion.", s: { t: 4, m: 1 } },
] });

/* ---------- Lab 1 ---------- */
Lib.slider($("#g1"), { id: "tq", label: "Total output of the two firms: ", min: 2, max: 16, step: 0.5, value: 8, fmt: (v) => fmtN(v, 1) + " units", onInput: lab1 });
function lab1() {
  const q = $("#tq").value * 1, p = Dm(q), pr = (p - MCc) * q, dwl = 0.5 * (16 - q) * (16 - q);
  $("#r1").textContent = "$" + fmtN(p, 2); $("#r2").textContent = fmtN(pr, 2); $("#r3").textContent = fmtN(pr / 2, 2); $("#r4").textContent = fmtN(dwl, 2);
  $("#rv").innerHTML = Math.abs(q - 8) < 0.01 ? "<b>Joint profit is at its maximum, $64.</b> MR = MC at 8 units. The firms are acting exactly like a monopolist, and each earns $32. Consumers pay $12."
    : q < 8 ? `<b>The cartel is restricting output too much.</b> Cutting below 8 units raises the price to $${fmtN(p, 2)} but sells so few units that joint profit falls to $${fmtN(pr, 2)}.`
      : q >= 16 ? "<b>This is the competitive outcome.</b> Price equals MC, profit is zero and there is no deadweight loss."
        : `<b>Output is above the profit-maximising level.</b> Marginal revenue is below marginal cost for units beyond 8, so extra output lowers joint profit ($${fmtN(pr, 2)}). Consumers gain from the lower price of $${fmtN(p, 2)}.`;
  const F = SMALL, { X, Y } = F;
  let o = marketDraw(F, 520, { d: 1, mc: 1, mr: 1, prof: 1, dwl: q < 16 ? 1 : 0, qm: q, car: 1, pr: 1, comp: 0 });
  $("#labA").innerHTML = o;
}
lab1();

/* ---------- Lab 2 ---------- */
let cn, cd, cdl;
function lab2() {
  const n = cn.get(), d = cd.get(), dl = cdl.get();
  const pim = 64 / n, Qo = 8 - 8 / n, qc = (16 - Qo) / 2, pic = (16 - Qo) * (16 - Qo) / 4;
  const Vc = pim / (1 - dl), Vx = pic / (1 - dl * (1 - d)), holds = Vc >= Vx;
  $("#c1").textContent = fmtN(pim, 2); $("#c2").textContent = fmtN(pic, 2); $("#c3").textContent = fmtN(Vc, 0); $("#c4").textContent = fmtN(Vx, 0);
  $("#cv").innerHTML = (holds ? `<b>The cartel is likely to hold.</b> Sticking to the quota is worth ${fmtN(Vc, 0)} against ${fmtN(Vx, 0)} for cheating, because the chance of being caught (${Math.round(d * 100)}%) and the value firms place on the future make the punishment worth fearing.` : `<b>The cartel is likely to collapse.</b> Cheating is worth ${fmtN(Vx, 0)} against ${fmtN(Vc, 0)} for sticking to the quota. Cheating gains ${fmtN((pic / pim - 1) * 100, 0)}% on one year's cartel profit, and the risk of being caught is too low to stop it.`) + (n > 2 ? ` With ${n} firms each member's share is small, so the gain from cheating is large compared with its cartel profit.` : "");
  const W = 520, H = 380, base = 320, mx = Math.max(Vc, Vx, 1), sc = 250 / mx;
  const bar = (x, v, cls, t, lab) => SV.rect(x, base - v * sc, 120, v * sc, cls) + SV.text(x + 60, base - v * sc - 8, fmtN(v, 0), "lbl bd " + t, { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, lab, "lbl bd", { "text-anchor": "middle" });
  $("#labB").innerHTML = SV.line(60, base, 480, base) + bar(110, Vc, "f3", "t3", "Stick to quota") + bar(290, Vx, "f2", "t2", "Cheat") + SV.text(260, 40, holds ? "Value of sticking is higher: cartel holds" : "Value of cheating is higher: cartel collapses", "lbl bd " + (holds ? "t3" : "t2"), { "text-anchor": "middle" });
}
cn = Lib.slider($("#g2"), { id: "cn", label: "Number of firms in the cartel: ", min: 2, max: 10, step: 1, value: 4, fmt: (v) => v, onInput: () => cdl && lab2() });
cd = Lib.slider($("#g3"), { id: "cd", label: "Chance that cheating is caught and punished: ", min: 0, max: 1, step: 0.05, value: 0.3, fmt: (v) => Math.round(v * 100) + "%", onInput: () => cdl && lab2() });
cdl = Lib.slider($("#g4"), { id: "cl", label: "How much firms value the future (0.5 to 0.95): ", min: 0.5, max: 0.95, step: 0.05, value: 0.9, fmt: (v) => fmtN(v, 2), onInput: () => cdl && lab2() });
lab2();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each example formal (overt) or tacit (informal) collusion?",
  buckets: [{ label: "Formal (overt)" }, { label: "Tacit (informal)" }],
  items: [
    { text: "A written agreement to fix a minimum price", b: 0 }, { text: "Firms agree output quotas at a meeting", b: 0 }, { text: "Firms divide the market by region by agreement", b: 0 }, { text: "Bidders agree in advance who will win a contract", b: 0 }, { text: "A cartel of producers sets a common price", b: 0 },
    { text: "Rivals raise prices soon after the biggest firm", b: 1 }, { text: "Firms charge a round-number price everyone expects", b: 1 }, { text: "A respected firm changes price first and others follow", b: 1 }, { text: "Firms match each other's published prices without any contact", b: 1 }, { text: "Prices move in step with no agreement", b: 1 },
  ], done: "The test is whether there is an explicit agreement.",
});
Lib.classify($("#cl2"), {
  prompt: "Does each condition make collusion more likely or less likely to work?",
  buckets: [{ label: "More likely" }, { label: "Less likely" }],
  items: [
    { text: "Few firms in the market", b: 0 }, { text: "High barriers to entry", b: 0 }, { text: "Similar costs and products", b: 0 }, { text: "Transparent, easily observed prices", b: 0 }, { text: "Stable demand", b: 0 }, { text: "Strong and well-enforced penalties for cheating by other members", b: 0 },
    { text: "Many firms in the market", b: 1 }, { text: "Easy entry for new firms", b: 1 }, { text: "Very different costs between firms", b: 1 }, { text: "Secret discounts are hard to detect", b: 1 }, { text: "Demand falling in a recession", b: 1 }, { text: "A strict competition authority with a leniency programme", b: 1 },
  ], done: "Collusion thrives where cheating is difficult and unprofitable.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Collusion", "Firms co-operating to limit competition and raise joint profit"],
  ["Cartel", "A formal agreement between firms to fix price or output"],
  ["Tacit collusion", "Co-ordinated behaviour without any explicit agreement"],
  ["Price leadership", "One firm sets the price and the others follow"],
  ["Output quota", "A limit on the amount each cartel member may produce"],
  ["Bid rigging", "Firms agree in advance who will win a contract"],
  ["Leniency programme", "Immunity or lower fines for the first firm to report a cartel"],
], done: "Seven terms to use in every collusion answer." });
Lib.order($("#o1"), { prompt: "Put the explanation of why a cartel may collapse in order.", items: [
  "Firms form a cartel and agree output quotas to keep the price high",
  "The higher price gives each member a joint profit above the competitive level",
  "A member sees that, if the others keep to their quotas, it could gain by secretly producing more",
  "Every member has the same incentive, so more of them cheat",
  "Total output rises and the price falls, so each member's profit falls",
  "The agreement collapses unless it can be monitored and enforced; evaluate the factors that affect this",
], done: "This chain works for any question on the stability of a cartel." });

Lib.calc($("#c5"), { qs: [
  { q: "With competition, price equals MC. What is total output (units)?", a: 16, hint: "Solve 20 − Q = 4.", sol: "Q = <b>16</b>." },
  { q: "What is the competitive price ($)?", a: 4, sol: "P = MC = <b>$4</b>." },
  { q: "A cartel acts like a monopolist and sets MR = MC. MR = 20 − 2Q. What is total output (units)?", a: 8, hint: "Solve 20 − 2Q = 4.", sol: "2Q = 16, so Q = <b>8</b>." },
  { q: "What price does the cartel charge ($)?", a: 12, hint: "Substitute Q = 8 into P = 20 − Q.", sol: "P = 20 − 8 = <b>$12</b>." },
  { q: "What is the cartel's joint profit ($)?", a: 64, hint: "(P − MC) x Q.", sol: "(12 − 4) x 8 = <b>$64</b>." },
  { q: "The two firms share the quota equally. What is each firm's profit ($)?", a: 32, sol: "64 / 2 = <b>$32</b> each (4 units each)." },
  { q: "Firm A cheats by producing 5 units while Firm B keeps to 4. What is the market price ($)?", a: 11, hint: "Total output is 9.", sol: "P = 20 − 9 = <b>$11</b>." },
  { q: "What is Firm A's profit from cheating ($)?", a: 35, hint: "(P − MC) x 5.", sol: "(11 − 4) x 5 = <b>$35</b>, more than the $32 for keeping the quota." },
  { q: "Both firms cheat and each produces 5. What is each firm's profit ($)?", a: 30, hint: "Total output is 10.", sol: "P = 10, profit = (10 − 4) x 5 = <b>$30</b> each: less than $32." },
  { q: "What is the deadweight loss of the cartel compared with competition ($)? (Triangle between D and MC from Q = 8 to Q = 16.)", a: 32, hint: "Half x base x height.", sol: "0.5 x (16 − 8) x (12 − 4) = <b>$32</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which of these is a form of tacit collusion?", opts: ["Firms agree output quotas", "Firms follow the price changes of a leading firm without any agreement", "Bid rigging", "A written price-fixing agreement"], a: 1, why: "Price leadership involves no explicit agreement, so it is tacit." },
  { q: "Why do colluding firms try to restrict output?", opts: ["To reduce marginal cost", "To raise price towards the monopoly level and earn higher joint profit", "To increase competition", "To increase allocative efficiency"], a: 1, why: "Restricting output pushes price up so the firms share a bigger joint profit." },
  { q: "A cartel member produces more than its quota while the others keep to theirs. What is most likely?", opts: ["Its profit falls to zero at once", "It may gain in the short run, but if all do the same the price falls", "The cartel's profit rises", "The price rises"], a: 1, why: "Cheating pays if others keep the agreement, but when everyone cheats output rises and price falls." },
  { q: "Which makes it harder to maintain a cartel?", opts: ["Few firms", "High barriers to entry", "Many firms with different costs", "Easily observed prices"], a: 2, why: "Many firms with different costs find it harder to agree and to monitor each other." },
  { q: "The observation that rival firms charge very similar prices:", opts: ["proves collusion", "could result from collusion, but could also result from competition or similar costs", "means there is perfect competition", "shows a cartel"], a: 1, why: "Parallel pricing alone is not proof of an agreement." },
  { q: "What is the purpose of a leniency programme?", opts: ["To increase the price of goods", "To encourage cartel members to report the cartel in return for immunity or lower fines", "To protect consumers from monopoly", "To help firms merge"], a: 1, why: "It creates distrust between members, as each fears another will report first." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Collusion", "Firms co-operating to limit competition and raise joint profit."],
  ["Formal (overt) collusion", "An explicit agreement between firms, such as a cartel."],
  ["Tacit (informal) collusion", "Firms co-ordinating without any explicit agreement, such as by following a price leader."],
  ["Cartel", "A formal agreement to fix price or output. Often unstable and illegal."],
  ["Output quota", "A limit on the amount each cartel member may produce."],
  ["Price fixing", "Firms agree the price, or a minimum price, to charge."],
  ["Market sharing", "Firms divide the market by region, customer or product."],
  ["Bid rigging", "Firms agree in advance who will win a contract; the others bid higher."],
  ["Price leadership", "One firm (dominant or barometric) sets price and the others follow."],
  ["Focal-point pricing", "Firms settle at an obvious price each expects the others to charge."],
  ["Price signalling", "Announcing intended price changes so rivals can respond."],
  ["Prisoner's dilemma", "Each member does better by cheating whatever the others do, so everyone cheats and all are worse off."],
  ["Leniency programme", "Immunity or lower fines for the first firm to report a cartel."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2021 · 32 · Q7] What is correct about cartels?", opts: ["They are a form of trade union restrictive practice.", "They are a type of industrial merger.", "They are often subject to government investigation.", "They establish a vertical link between firms."], a: 2, why: "Agreeing to fix price or output limits competition, so cartels are often investigated and are illegal in many countries." },
  { q: "[Feb/March 2025 · 32 · Q3] What is likely to prevent the development of an effective cartel in an industry?", opts: ["a high concentration ratio", "a limit-pricing policy", "high fixed costs", "low barriers to entry"], a: 3, why: "If new firms can enter easily, outsiders undercut the cartel and its high price cannot be held." },
  { q: "[May/June 2022 · 32 · Q10] What is a condition for operating a successful cartel?", opts: ["a large number of firms in the industry", "having a differentiated product", "low barriers of entry to the industry", "strictly enforced production quotas"], a: 3, why: "Members must keep to their output quotas, otherwise each gains by cheating." },
  { q: "[May/June 2020 (not sat) · 31 · Q11] When will a cartel find it most difficult to fix the market price of its product? (proportion of firms in the industry that are members, barriers to entry)", opts: ["high, high", "high, low", "low, high", "low, low"], a: 3, why: "A cartel with few of the industry's firms and easy entry cannot control the market price." },
  { q: "[May/June 2022 · 31 · Q7] Firms in a market decide to collude over the price that they charge for their products. What is not likely to be a feature of the market?", opts: ["Firms have similar cost structures.", "Products of the firms are close substitutes.", "There are high barriers to entry into the market.", "There is a large number of competing firms."], a: 3, why: "Collusion is easier with a few firms; a large number makes agreement and policing difficult." },
] });
