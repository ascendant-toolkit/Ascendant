const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

const X = (q) => 90 + q * 4.6, Y = (p) => 310 - p * 2.7;
function axes() { return SV.line(X(0), Y(0), X(0), Y(108)) + SV.line(X(0), Y(0), X(135), Y(0)) + SV.text(X(0) + 8, 14, "Price ($)", "sm") + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }); }
function dCurve(d, cls, lab, t) { const a = d >= 0 ? [d, 100] : [0, 100 + d], b = [100 + d, 0]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c1") + SV.text(X(b[0]) + 6, Y(b[1]) - 8, lab || "D", "lbl bd " + (t || "t1")); }
function sCurve(s, cls, lab, t) { const a = s >= 0 ? [s, 0] : [0, -s], b = [100 + s, 100]; return SV.line(X(a[0]), Y(a[1]), X(b[0]), Y(b[1]), cls || "c2") + SV.text(X(b[0]) + 6, Y(b[1]) + 4, lab || "S", "lbl bd " + (t || "t2")); }
function eq(d, s) { const q = (100 + d + s) / 2, p = q - s; return [q, p]; }
function dsDrop(q, p) { return SV.line(X(0), Y(p), X(q), Y(p), "gr") + SV.line(X(q), Y(p), X(q), Y(0), "gr"); }
function qD(p, d) { return Math.max(0, 100 + d - p); }
function qS(p, s) { return Math.max(0, p + s); }

function ctrl(kind, amt) {
  // kind: 0 none, 1 max price, 2 min price, 3 indirect tax, 4 subsidy
  let o = axes(), [q0, p0] = eq(0, 0);
  if (kind === 3) { o += dCurve(0, "c1", "D") + sCurve(0, "c3", "S", "t3") + sCurve(-amt, "c4", "S₁ (with tax)", "t4"); const [q, p] = eq(0, -amt); o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1") + dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.line(X(q), Y(p), X(q), Y(p - amt), "c3") + SV.text(X(q) - 8, Y(p - amt / 2), "tax $" + amt, "sm bd t4", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }); return o; }
  if (kind === 4) { o += dCurve(0, "c1", "D") + sCurve(0, "c3", "S", "t3") + sCurve(amt, "c2", "S₁ (with subsidy)", "t2"); const [q, p] = eq(0, amt); o += dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1") + dsDrop(q, p) + SV.circle(X(q), Y(p), 7, "dot2") + SV.text(X(0) - 8, Y(p), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p0), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q0), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }); return o; }
  o += dCurve(0, "c1", "D") + sCurve(0, "c2", "S") + dsDrop(q0, p0) + SV.circle(X(q0), Y(p0), 5, "dot1");
  if (kind === 1 || kind === 2) { const pc = p0 + (kind === 1 ? -amt : amt), qd = qD(pc, 0), qs = qS(pc, 0); o += SV.line(X(0), Y(pc), X(Math.max(qd, qs) + 8), Y(pc), "c4") + SV.circle(X(qd), Y(pc), 6, "dot3") + SV.circle(X(qs), Y(pc), 6, "dot4") + SV.text(X(0) - 8, Y(pc), (kind === 1 ? "Max $" : "Min $") + Math.round(pc), "sm bd t4", { "text-anchor": "end" }) + SV.text(X((qd + qs) / 2), Y(pc) - 12, kind === 1 ? "Shortage " + Math.round(qd - qs) : "Surplus " + Math.round(qs - qd), "lbl bd t4", { "text-anchor": "middle" }) + SV.text(X(qd), Y(0) + 18, "Qd", "sm bd", { "text-anchor": "middle" }) + SV.text(X(qs), Y(0) + 18, "Qs", "sm bd", { "text-anchor": "middle" }); }
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 380, label: "Maximum price", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "The government sets a <b>maximum price</b> below equilibrium (to keep rents affordable). At this price quantity demanded exceeds quantity supplied: a <b>shortage</b>.", s: { k: 1, a: 20 } },
  { cap: "Shortages lead to queues, rationing and possibly a <b>black market</b>, and suppliers may cut supply further.", s: { k: 1, a: 20 } },
] });
Lib.stepper($("#stN"), { w: 760, h: 380, label: "Minimum price", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "The government sets a <b>minimum price</b> above equilibrium (to protect farmers' incomes). Quantity supplied exceeds quantity demanded: a <b>surplus</b>.", s: { k: 2, a: 20 } },
  { cap: "The surplus must be bought, stored or destroyed: a <b>cost</b> to taxpayers, and consumers pay a higher price.", s: { k: 2, a: 20 } },
] });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Indirect tax", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "An <b>indirect tax</b> raises producers' costs: supply shifts <b>left</b> to S₁.", s: { k: 3, a: 20 } },
  { cap: "The price <b>rises</b> to P₁ and the quantity <b>falls</b> to Q₁. The government raises tax revenue and consumption of the taxed good falls.", s: { k: 3, a: 20 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Subsidy", base: { k: 0, a: 20 }, draw: (s) => ctrl(s.k, s.a), steps: [
  { cap: "Market equilibrium at price P and quantity Q.", s: { k: 0, a: 20 } },
  { cap: "A <b>subsidy</b> lowers producers' costs: supply shifts <b>right</b> to S₁.", s: { k: 4, a: 20 } },
  { cap: "The price <b>falls</b> to P₁ and the quantity <b>rises</b> to Q₁. Consumers buy more of the subsidised good; the cost falls on taxpayers.", s: { k: 4, a: 20 } },
] });

/* Lab 1 */
const KN = ["No policy", "Maximum price", "Minimum price", "Indirect tax", "Subsidy"];
function labI() {
  if (!$("#ia") || !$("#ib")) return;
  const k = +$("#ia").value, a = +$("#ib").value, [q0, p0] = eq(0, 0); let r = ["$" + p0, q0, "None"], t = "Equilibrium: price $" + p0 + ", quantity " + q0 + ".";
  if (k === 1) { const pc = p0 - a, qd = qD(pc, 0), qs = qS(pc, 0); r = ["$" + pc, qs + " supplied", "Shortage " + (qd - qs)]; t = "A maximum price of $" + pc + " (below $" + p0 + ") means " + qd + " demanded but only " + qs + " supplied: a shortage of " + (qd - qs) + ". It helps buyers who can find the good, but leads to queues and black markets."; }
  if (k === 2) { const pc = p0 + a, qd = qD(pc, 0), qs = qS(pc, 0); r = ["$" + pc, qd + " demanded", "Surplus " + (qs - qd)]; t = "A minimum price of $" + pc + " (above $" + p0 + ") means " + qs + " supplied but only " + qd + " demanded: a surplus of " + (qs - qd) + ". Producers earn more per unit but consumers pay more and the surplus has to be dealt with."; }
  if (k === 3) { const [q, p] = eq(0, -a); r = ["$" + p.toFixed(0), q.toFixed(0), "$" + (a * q).toFixed(0)]; t = "A $" + a + " tax per unit shifts supply left: price rises from $" + p0 + " to $" + p.toFixed(0) + " and quantity falls from " + q0 + " to " + q.toFixed(0) + ". Tax revenue is $" + a + " × " + q.toFixed(0) + " = $" + (a * q).toFixed(0) + "."; }
  if (k === 4) { const [q, p] = eq(0, a); r = ["$" + p.toFixed(0), q.toFixed(0), "$" + (a * q).toFixed(0)]; t = "A $" + a + " subsidy per unit shifts supply right: price falls from $" + p0 + " to $" + p.toFixed(0) + " and quantity rises from " + q0 + " to " + q.toFixed(0) + ". The subsidy costs the government $" + a + " × " + q.toFixed(0) + " = $" + (a * q).toFixed(0) + "."; }
  $("#ia1").textContent = r[0]; $("#ia2").textContent = r[1]; $("#ia3").textContent = r[2]; $("#iav").textContent = t;
  $("#labI").innerHTML = ctrl(k, a);
}
Lib.slider($("#g1"), { id: "ia", label: "Policy (0 none, 1 max price, 2 min price, 3 tax, 4 subsidy)", min: 0, max: 4, step: 1, value: 3, fmt: (v) => KN[v], onInput: labI });
Lib.slider($("#g2"), { id: "ib", label: "Size of the policy ($)", min: 5, max: 30, step: 5, value: 20, fmt: (v) => "$" + v, onInput: labI });
const OT = [
  { n: "Regulation", a: "Laws and rules", b: "Controls pollution and monopoly; costs of compliance." },
  { n: "Privatisation", a: "Selling state firms", b: "May raise efficiency; risk of private monopoly and job losses." },
  { n: "Nationalisation", a: "State takeover of firms", b: "Protects essential services; possible inefficiency and taxpayer cost." },
  { n: "Direct provision", a: "The state supplies the good", b: "Ensures public and merit goods for all; high tax cost." },
  { n: "Quotas", a: "Limits on quantity extracted or produced", b: "Protects resources; raises prices; illegal extraction." },
];
button_table("otBtns", "otOut", OT, 0, (p) => `<div class="tw"><table class="t"><tr><th>Meaning</th><th>Advantages and disadvantages</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What is the <b>effect</b> of each policy?", buckets: [{ label: "Shortage" }, { label: "Surplus" }, { label: "Price up, quantity down" }, { label: "Price down, quantity up" }], items: [
  { text: "Maximum price below equilibrium", b: 0 }, { text: "Minimum price above equilibrium", b: 1 }, { text: "Indirect tax", b: 2 }, { text: "Subsidy", b: 3 },
  { text: "Rent control", b: 0 }, { text: "A guaranteed price for wheat above the market price", b: 1 }, { text: "A tax on cigarettes", b: 2 }, { text: "A subsidy for solar panels", b: 3 },
], done: "Know the effects." });
Lib.classify($("#cl2"), { prompt: "Which <b>policy</b> fits each aim?", buckets: [{ label: "Tax or quota" }, { label: "Subsidy or direct provision" }, { label: "Regulation" }], items: [
  { text: "Reduce consumption of a demerit good", b: 0 }, { text: "Protect fish stocks", b: 0 }, { text: "Increase use of a merit good", b: 1 }, { text: "Provide street lighting", b: 1 }, { text: "Limit pollution from factories", b: 2 }, { text: "Stop a monopoly abusing consumers", b: 2 },
], done: "Match policy to failure." });
Lib.match($("#m1"), { prompt: "Match the policy to its definition.", pairs: [
  ["Maximum price", "A legal limit on how high a price may go"],
  ["Minimum price", "A legal limit on how low a price may go"],
  ["Indirect tax", "A tax on goods and services"],
  ["Subsidy", "A government payment to lower producers' costs"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Nationalisation", "The government takes over a private firm"],
  ["Regulation", "Laws and rules firms must follow"],
  ["Quota", "A legal limit on quantity"],
], done: "Definitions score marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a subsidy increases consumption of a merit good</b>.", items: [
  "The government pays a subsidy to producers",
  "Producers' costs fall: supply shifts right",
  "The price falls",
  "Quantity demanded rises",
  "More of the merit good is consumed",
], done: "A supply increase." });
Lib.calc($("#c1"), { qs: [
  { q: "A tax of $20 a unit is placed on 40 units sold. What is the tax revenue ($)?", a: 800, sol: "20 × 40 = <b>$800</b>." },
  { q: "A subsidy of $5 a unit is paid on 600 units. What does it cost the government ($)?", a: 3000, sol: "5 × 600 = <b>$3,000</b>." },
  { q: "At a maximum price, quantity demanded is 70 and quantity supplied is 30. What is the shortage?", a: 40, sol: "70 − 30 = <b>40</b>." },
  { q: "At a minimum price, quantity supplied is 80 and quantity demanded is 45. What is the surplus?", a: 35, sol: "80 − 45 = <b>35</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A maximum price set below equilibrium causes:", opts: ["A surplus", "A shortage", "Equilibrium", "A tax"], a: 1, why: "Qd > Qs." },
  { q: "A minimum price set above equilibrium causes:", opts: ["A shortage", "A surplus", "Lower prices", "No change"], a: 1, why: "Qs > Qd." },
  { q: "An indirect tax shifts:", opts: ["Demand right", "Supply left", "Supply right", "Demand left"], a: 1, why: "Costs rise." },
  { q: "Which is privatisation?", opts: ["Selling a state firm to private owners", "A government taking over a firm", "A tax", "A quota"], a: 0, why: "State to private." },
  { q: "A disadvantage of subsidies is:", opts: ["Lower prices", "Cost to taxpayers", "More output", "Wider choice"], a: 1, why: "Opportunity cost." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Maximum price", "A legal limit on how high a price may be."],
  ["Minimum price", "A legal limit on how low a price may be."],
  ["Indirect tax", "A tax on goods and services."],
  ["Subsidy", "A government payment to lower producers' costs."],
  ["Regulation", "Laws and rules that firms must follow."],
  ["Privatisation", "Selling state-owned firms to the private sector."],
  ["Nationalisation", "The government taking over private firms."],
  ["Direct provision", "The government supplying goods and services itself."],
  ["Quota", "A legal limit on the quantity produced or extracted."],
] });
labI(); 
