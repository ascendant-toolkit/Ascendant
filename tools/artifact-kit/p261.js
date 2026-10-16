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

Lib.stepper($("#stE"), { w: 760, h: 380, label: "Elastic vs inelastic", base: { n: 0 }, draw: (s) => {
  let o = axes();
  if (s.n >= 0) o += pedCurve(3, "c2", "Elastic D", "t2") + SV.circle(X(50), Y(50), 6, "dot1");
  if (s.n >= 1) o += pedCurve(1, "c1", "Inelastic D", "t1");
  return o;
}, steps: [
  { cap: "A <b>flat</b> (elastic) demand curve: a small price change makes quantity demanded change a lot.", s: { n: 0 } },
  { cap: "A <b>steep</b> (inelastic) demand curve: a big price change changes quantity demanded only a little.", s: { n: 1 } },
] });
const RS = ["The price of a good rises by 10%", "Quantity demanded changes", "If quantity falls by more than 10%: elastic", "If quantity falls by less than 10%: inelastic", "PED measures this response"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Responsiveness", base: { n: 0 }, draw: mkChain(RS, "--accent"), steps: chainSteps(["The <b>price</b> of a good rises by 10%.", "<b>Quantity demanded</b> changes.", "If quantity falls by <b>more</b> than 10%: <b>elastic</b>.", "If quantity falls by <b>less</b> than 10%: <b>inelastic</b>.", "<b>PED</b> measures this response."]) });

/* Lab 1 */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const dp = +$("#ra").value, dq = +$("#rb").value, ped = dp === 0 ? 0 : dq / dp, lab = pedLabel(Math.abs(ped));
  $("#ra1").textContent = (dq >= 0 ? "+" : "") + dq + "%"; $("#ra2").textContent = money(Math.abs(ped), 2); $("#ra3").textContent = lab.charAt(0).toUpperCase() + lab.slice(1);
  $("#rav").textContent = `A ${dp}% price rise cuts quantity demanded by ${Math.abs(dq)}%. The percentage change in quantity (${Math.abs(dq)}) is ${Math.abs(dq) > dp ? "bigger" : Math.abs(dq) < dp ? "smaller" : "equal"} than the percentage change in price (${dp}), so demand is ${lab}.`;
  const q1 = 50 * (1 - Math.abs(dq) / 100), p1 = 50 * (1 + dp / 100), k = (p1 - 50) / (q1 - 50), qa = Math.max(0, 50 + (95 - 50) / k), qb = Math.min(108, 50 + (5 - 50) / k), pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50);
  $("#labR").innerHTML = axes() + SV.line(X(qa), Y(pa), X(qb), Y(pb), "c1") + dsDrop(50, 50) + SV.circle(X(50), Y(50), 6, "dot1") + dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ra", label: "Price rise", min: 5, max: 40, step: 5, value: 10, fmt: (v) => "+" + v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Change in quantity demanded", min: -80, max: -2, step: 2, value: -20, fmt: (v) => v + "%", onInput: labR });
const EL = [
  { n: "Petrol", t: "Inelastic", w: "Necessity for drivers; few substitutes in the short run." },
  { n: "Salt", t: "Inelastic", w: "Cheap; no close substitute; tiny part of spending." },
  { n: "Branded chocolate", t: "Elastic", w: "Many substitute brands; a luxury." },
  { n: "Package holidays", t: "Elastic", w: "Many alternatives; large part of income." },
  { n: "Life-saving medicine", t: "Inelastic", w: "Essential; no substitute." },
];
button_table("elBtns", "elOut", EL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Demand is</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is demand for each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "A luxury holiday", b: 0 }, { text: "A branded snack with many rivals", b: 0 }, { text: "A restaurant meal", b: 0 },
  { text: "Petrol", b: 1 }, { text: "Salt", b: 1 }, { text: "Insulin for diabetics", b: 1 },
], done: "Substitutes and necessity matter." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["PED", "Responsiveness of quantity demanded to a price change"],
  ["Elastic demand", "Quantity changes by a bigger % than price"],
  ["Inelastic demand", "Quantity changes by a smaller % than price"],
  ["Flat demand curve", "Elastic"],
  ["Steep demand curve", "Inelastic"],
  ["Responsiveness", "How much one variable reacts to another"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>what happens to quantity when price rises for an elastic good</b>.", items: [
  "The price rises by 10%",
  "Consumers switch to substitutes",
  "Quantity demanded falls by more than 10%",
  "Demand is elastic",
], done: "Elastic means a big response." });
Lib.calc($("#c1"), { qs: [
  { q: "A 10% rise in price causes a 20% fall in quantity demanded. Is the % change in quantity bigger? Enter the % change in quantity (positive number).", a: 20, sol: "<b>20%</b>: bigger than 10%, so demand is elastic." },
  { q: "Price rises 20% and quantity demanded falls 5%. What is the size of the % change in quantity?", a: 5, sol: "<b>5%</b>: smaller than 20%, so demand is inelastic." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "PED measures:", opts: ["How price responds to quantity", "How quantity demanded responds to price", "Income and demand", "Supply and price"], a: 1, why: "Responsiveness of Qd to price." },
  { q: "Demand is elastic if:", opts: ["Quantity changes by a smaller % than price", "Quantity changes by a bigger % than price", "Price does not change", "Quantity is zero"], a: 1, why: "A big response." },
  { q: "Which is likely to be inelastic?", opts: ["A branded chocolate", "Petrol", "A holiday", "A restaurant meal"], a: 1, why: "A necessity." },
  { q: "An elastic demand curve is:", opts: ["Steep", "Flat", "Vertical", "Absent"], a: 1, why: "Flatter." },
  { q: "Inelastic demand means consumers:", opts: ["Respond a lot to price", "Respond little to price", "Buy nothing", "Buy more when price rises"], a: 1, why: "Hardly respond." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Price elasticity of demand", "A measure of the responsiveness of quantity demanded to a change in price."],
  ["Elastic demand", "Quantity demanded changes by a bigger percentage than price."],
  ["Inelastic demand", "Quantity demanded changes by a smaller percentage than price."],
  ["Responsiveness", "How much one variable reacts to a change in another."],
  ["Substitute", "A good that can replace another."],
  ["Necessity", "A good people need and cannot easily do without."],
  ["Luxury", "A good people want but could do without."],
  ["Quantity demanded", "The amount bought at one price."],
  ["Percentage change", "Change divided by the original, times 100."],
] });
labR(); 
