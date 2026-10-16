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

/* PED curves through (50, 50). kind: 0 inelastic perfectly, 1 inelastic, 2 unitary, 3 elastic, 4 perfectly elastic */
function pedCurve(kind, cls, lab, t) {
  let o = "", lx = 0, ly = 0;
  if (kind === 0) { o = SV.line(X(50), Y(0), X(50), Y(105), cls || "c1"); lx = 50; ly = 100; }
  else if (kind === 4) { o = SV.line(X(0), Y(50), X(110), Y(50), cls || "c1"); lx = 112; ly = 50; }
  else if (kind === 2) { let d = ""; for (let q = 25; q <= 105; q += 2) d += (d ? "L" : "M") + X(q).toFixed(1) + " " + Y(2500 / q).toFixed(1); o = SV.path(d, cls || "c1"); lx = 100; ly = 25; }
  else { const k = kind === 1 ? 3 : 0.35, qa = Math.max(0, 50 - 48 / k), qb = Math.min(108, 50 + 48 / k), pa = 50 - k * (qa - 50), pb = 50 - k * (qb - 50); o = SV.line(X(qa), Y(pa), X(qb), Y(pb), cls || "c1"); lx = qb + 1; ly = pb; }
  return o + SV.text(X(lx) + 6, Y(ly), lab || "D", "lbl bd " + (t || "t1"));
}
function pedLabel(v) { if (v === 0) return "perfectly inelastic"; if (v === Infinity) return "perfectly elastic"; const a = Math.abs(v); return a < 0.99 ? "inelastic" : a > 1.01 ? "elastic" : "unitary"; }

function revChart(p0, q0, p1, q1) {
  let o = axes();
  o += SV.rect(X(0), Y(p0), X(q0) - X(0), Y(0) - Y(p0), "", { style: "fill:var(--accent)", opacity: 0.22 });
  o += SV.rect(X(0), Y(p1), X(q1) - X(0), Y(0) - Y(p1), "", { style: "fill:var(--warn)", opacity: 0.25 });
  o += SV.line(X(0), Y(p0), X(q0), Y(p0), "gr") + SV.line(X(q0), Y(p0), X(q0), Y(0), "gr") + SV.line(X(0), Y(p1), X(q1), Y(p1), "gr") + SV.line(X(q1), Y(p1), X(q1), Y(0), "gr");
  o += SV.circle(X(q0), Y(p0), 6, "dot1") + SV.circle(X(q1), Y(p1), 6, "dot2") + SV.text(X(0) - 8, Y(p0), "P₀", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(q0), Y(0) + 18, "Q₀", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(X(60), Y(104), "Blue: old revenue  ·  Orange: new revenue", "sm");
}
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Price rise, inelastic demand", base: { n: 0 }, draw: (s) => s.n === 0 ? revChart(40, 60, 40, 60) : revChart(40, 60, 60, 52), steps: [
  { cap: "Price $40, quantity 60: revenue = 40 × 60 = <b>2,400</b>.", s: { n: 0 } },
  { cap: "Price rises to $60 and quantity falls only to 52: revenue = 60 × 52 = <b>3,120</b>. Revenue <b>rises</b>: demand is inelastic.", s: { n: 1 } },
] });
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Price rise, elastic demand", base: { n: 0 }, draw: (s) => s.n === 0 ? revChart(40, 60, 40, 60) : revChart(40, 60, 60, 30), steps: [
  { cap: "Price $40, quantity 60: revenue = <b>2,400</b>.", s: { n: 0 } },
  { cap: "Price rises to $60 and quantity falls to 30: revenue = 60 × 30 = <b>1,800</b>. Revenue <b>falls</b>: demand is elastic.", s: { n: 1 } },
] });
const RL = ["A firm raises its price", "Demand is elastic: quantity falls by a bigger %", "Revenue falls", "Demand is inelastic: quantity falls by a smaller %", "Revenue rises"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "The rule", base: { n: 0 }, draw: mkChain(RL, "--accent"), steps: chainSteps(["A firm <b>raises its price</b>.", "If demand is <b>elastic</b>, quantity falls by a bigger %.", "<b>Revenue falls</b>.", "If demand is <b>inelastic</b>, quantity falls by a smaller %.", "<b>Revenue rises</b>."]) });

/* Lab 1 */
function labV() {
  if (!$("#va") || !$("#vb")) return;
  const dp = +$("#va").value, ped = +$("#vb").value / 10, p0 = 40, q0 = 60, p1 = p0 * (1 + dp / 100), q1 = q0 * (1 - ped * dp / 100), r0 = p0 * q0, r1 = p1 * q1, ch = r1 - r0;
  $("#va1").textContent = "$" + money(r0, 0); $("#va2").textContent = "$" + money(r1, 0); $("#va3").textContent = (ch >= 0 ? "+" : "−") + "$" + money(Math.abs(ch), 0);
  $("#vav").textContent = `PED ${money(ped, 1)} (${pedLabel(ped)}). A ${dp >= 0 ? "rise" : "fall"} of ${Math.abs(dp)}% changes price from $${p0} to $${money(p1, 0)} and quantity from ${q0} to ${money(q1, 0)}. Revenue goes from $${money(r0, 0)} to $${money(r1, 0)}: ${ch > 1 ? "it rises" : ch < -1 ? "it falls" : "it is unchanged"}. ${ped < 1 ? "Inelastic: price and revenue move together." : ped > 1 ? "Elastic: price and revenue move in opposite directions." : "Unitary: no change in revenue."}`;
  $("#labV").innerHTML = revChart(p0, q0, Math.min(100, p1), Math.max(2, q1));
}
Lib.slider($("#g1"), { id: "va", label: "Price change", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labV });
Lib.slider($("#g2"), { id: "vb", label: "PED (size, ×0.1)", min: 2, max: 30, step: 1, value: 5, fmt: (v) => money(v / 10, 1), onInput: labV });
const SC = [
  { n: "Elastic demand, price rises", r: "Revenue falls", w: "Quantity falls by a bigger % than price rises." },
  { n: "Elastic demand, price falls", r: "Revenue rises", w: "Quantity rises by a bigger % than price falls." },
  { n: "Inelastic demand, price rises", r: "Revenue rises", w: "Quantity falls by a smaller % than price rises." },
  { n: "Inelastic demand, price falls", r: "Revenue falls", w: "Quantity rises by a smaller % than price falls." },
  { n: "Unitary demand, any price change", r: "Revenue unchanged", w: "Equal % changes cancel." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Revenue</th><th>Why</th></tr><tr><td><b>${p.r}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>revenue</b>?", buckets: [{ label: "Revenue rises" }, { label: "Revenue falls" }, { label: "Revenue unchanged" }], items: [
  { text: "Price rises, demand inelastic", b: 0 }, { text: "Price falls, demand elastic", b: 0 },
  { text: "Price rises, demand elastic", b: 1 }, { text: "Price falls, demand inelastic", b: 1 },
  { text: "Price changes, demand unitary", b: 2 },
], done: "Elastic: price and revenue move in opposite directions." });
Lib.classify($("#cl2"), { prompt: "Should the firm <b>raise</b> or <b>cut</b> its price to increase revenue?", buckets: [{ label: "Raise price" }, { label: "Cut price" }], items: [
  { text: "Demand is inelastic", b: 0 }, { text: "PED is 0.4", b: 0 }, { text: "Demand is elastic", b: 1 }, { text: "PED is 2.5", b: 1 },
], done: "Use the rule (educational, not advice)." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Total revenue", "Price × quantity sold"],
  ["Consumer expenditure", "What consumers spend; equals firms' revenue"],
  ["Inelastic demand", "Price rise increases revenue"],
  ["Elastic demand", "Price rise decreases revenue"],
  ["Unitary demand", "Revenue unchanged by price changes"],
  ["Area of rectangle", "Revenue on a diagram"],
], done: "Learn the link." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price rise reduces revenue when demand is elastic</b>.", items: [
  "The firm raises its price",
  "Consumers switch to substitutes",
  "Quantity demanded falls by a bigger percentage than the price rise",
  "Revenue (price × quantity) falls",
], done: "Elastic demand punishes price rises." });
Lib.calc($("#c1"), { qs: [
  { q: "Price $10 with 100 sold; price rises to $12 with 90 sold. By how much does revenue change ($)?", a: 80, sol: "1,080 − 1,000 = <b>+$80</b>." },
  { q: "Price $10 with 100 sold; price rises to $12 with 60 sold. What is the new revenue ($)?", a: 720, sol: "12 × 60 = <b>$720</b>." },
  { q: "PED is 0.5. A firm raises its price by 10%. By what percentage does revenue change (approximately, enter a whole number)?", a: 4, sol: "Quantity falls 5%; revenue ≈ 1.10 × 0.95 = 1.045: about <b>+4%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "If demand is inelastic and a firm raises price, revenue:", opts: ["Rises", "Falls", "Is unchanged", "Is zero"], a: 0, why: "Quantity falls by a smaller %." },
  { q: "If demand is elastic and a firm raises price, revenue:", opts: ["Rises", "Falls", "Is unchanged", "Doubles"], a: 1, why: "Quantity falls by a bigger %." },
  { q: "Consumer expenditure equals:", opts: ["Firms' costs", "Firms' revenue", "Firms' profit", "Taxes"], a: 1, why: "Spending = revenue." },
  { q: "If PED = 1 and the price rises, revenue:", opts: ["Rises", "Falls", "Is unchanged", "Is zero"], a: 2, why: "Equal % changes." },
  { q: "Revenue is shown on a diagram as:", opts: ["A point", "A line", "The area of the rectangle P × Q", "The slope"], a: 2, why: "Price × quantity." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Total revenue", "Price multiplied by quantity sold."],
  ["Consumer expenditure", "The amount spent by consumers on a good."],
  ["Elastic demand", "Price rise reduces revenue."],
  ["Inelastic demand", "Price rise increases revenue."],
  ["Unitary demand", "Revenue does not change when price changes."],
  ["Area of rectangle", "How revenue is shown on a diagram."],
  ["Percentage change", "Used in PED."],
  ["Price rise", "Increase in price."],
  ["Price fall", "Decrease in price."],
] });
labV(); 
