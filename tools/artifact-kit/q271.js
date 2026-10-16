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

/* Supply curves through (50, 50). kind: 0 perfectly inelastic, 1 inelastic, 2 unitary, 3 elastic, 4 perfectly elastic */
function pesCurve(kind, cls, lab, t) {
  let o = "", lx = 0, ly = 0;
  if (kind === 0) { o = SV.line(X(50), Y(0), X(50), Y(105), cls || "c2"); lx = 50; ly = 100; }
  else if (kind === 4) { o = SV.line(X(0), Y(50), X(110), Y(50), cls || "c2"); lx = 112; ly = 50; }
  else { const k = kind === 1 ? 3 : kind === 2 ? 1 : 0.35; let qa = Math.max(0, 50 - 48 / k), qb = Math.min(108, 50 + 48 / k); const pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50); o = SV.line(X(qa), Y(pa), X(qb), Y(pb), cls || "c2"); lx = qb + 1; ly = pb; }
  return o + SV.text(X(lx) + 6, Y(ly), lab || "S", "lbl bd " + (t || "t2"));
}
function pesLabel(v) { if (v === 0) return "perfectly inelastic"; if (v === Infinity) return "perfectly elastic"; return v < 0.99 ? "inelastic" : v > 1.01 ? "elastic" : "unitary"; }

Lib.stepper($("#stE"), { w: 760, h: 380, label: "Elastic vs inelastic supply", base: { n: 0 }, draw: (s) => {
  let o = axes() + pesCurve(3, "c2", "Elastic S", "t2") + SV.circle(X(50), Y(50), 6, "dot1");
  if (s.n >= 1) o += pesCurve(1, "c1", "Inelastic S", "t1");
  return o;
}, steps: [
  { cap: "A <b>flat</b> (elastic) supply curve: a small price change makes quantity supplied change a lot.", s: { n: 0 } },
  { cap: "A <b>steep</b> (inelastic) supply curve: quantity supplied hardly changes even when the price changes a lot.", s: { n: 1 } },
] });
const RS = ["Demand rises, so price rises 10%", "Producers want to supply more", "If they can raise output by more than 10% quickly: elastic", "If they can raise output by less than 10%: inelastic", "PES measures this response"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Responsiveness of supply", base: { n: 0 }, draw: mkChain(RS, "--accent"), steps: chainSteps(["Demand rises, so the <b>price rises</b> 10%.", "Producers want to <b>supply more</b>.", "If they can raise output by <b>more</b> than 10% quickly: <b>elastic</b>.", "If they can raise output by <b>less</b> than 10%: <b>inelastic</b>.", "<b>PES</b> measures this response."]) });

/* Lab 1 */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const dp = +$("#ra").value, dq = +$("#rb").value, pes = dq / dp, lab = pesLabel(pes);
  $("#ra1").textContent = "+" + dq + "%"; $("#ra2").textContent = money(pes, 2); $("#ra3").textContent = lab.charAt(0).toUpperCase() + lab.slice(1);
  $("#rav").textContent = `A ${dp}% price rise increases quantity supplied by ${dq}%. The change in quantity (${dq}%) is ${dq > dp ? "bigger" : dq < dp ? "smaller" : "equal"} than the change in price (${dp}%), so supply is ${lab}.`;
  const q1 = 50 * (1 + dq / 100), p1 = 50 * (1 + dp / 100), k = (p1 - 50) / (q1 - 50), qa = Math.max(0, 50 + (5 - 50) / k), qb = Math.min(108, 50 + (95 - 50) / k), pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50);
  $("#labR").innerHTML = axes() + SV.line(X(qa), Y(pa), X(qb), Y(pb), "c2") + dsDrop(50, 50) + SV.circle(X(50), Y(50), 6, "dot1") + dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ra", label: "Price rise", min: 5, max: 40, step: 5, value: 10, fmt: (v) => "+" + v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Increase in quantity supplied", min: 2, max: 80, step: 2, value: 20, fmt: (v) => "+" + v + "%", onInput: labR });
const EL = [
  { n: "Factory-made T-shirts", t: "Elastic", w: "Easy to increase output; spare capacity; stocks." },
  { n: "Fresh strawberries in a season", t: "Inelastic", w: "Crops take months to grow; harvest is limited." },
  { n: "Housing", t: "Inelastic", w: "Building takes years; land is limited." },
  { n: "Fine art by a dead artist", t: "Perfectly inelastic", w: "Fixed supply." },
  { n: "Online software", t: "Elastic", w: "Copies cost almost nothing to supply." },
];
button_table("elBtns", "elOut", EL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Supply is</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is supply of each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "Mass-produced plastic toys", b: 0 }, { text: "Online software", b: 0 }, { text: "A haircut", b: 0 },
  { text: "Housing in a city", b: 1 }, { text: "A farm crop between harvests", b: 1 }, { text: "Rare paintings", b: 1 },
], done: "Think about how quickly output can rise." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["PES", "Responsiveness of quantity supplied to a price change"],
  ["Elastic supply", "Quantity supplied changes by a bigger % than price"],
  ["Inelastic supply", "Quantity supplied changes by a smaller % than price"],
  ["Spare capacity", "Unused ability to produce more"],
  ["Stocks", "Goods held in storage ready to sell"],
  ["Flat supply curve", "Elastic"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why supply of strawberries is inelastic in the short run</b>.", items: [
  "The price of strawberries rises",
  "Farmers want to produce more",
  "Plants take months to grow",
  "Output can rise by only a small %",
  "Supply is inelastic",
], done: "Time limits supply." });
Lib.calc($("#c1"), { qs: [
  { q: "A 10% rise in price leads to a 5% rise in quantity supplied. What is the % change in quantity?", a: 5, sol: "<b>5%</b>: smaller than 10%, so supply is inelastic." },
  { q: "A 5% rise in price raises quantity supplied by 15%. What is the % change in quantity?", a: 15, sol: "<b>15%</b>: bigger than 5%, so supply is elastic." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "PES measures:", opts: ["How price responds to quantity", "How quantity supplied responds to price", "Income and supply", "Demand and price"], a: 1, why: "Responsiveness of Qs to price." },
  { q: "Supply is elastic if:", opts: ["Quantity changes by a smaller % than price", "Quantity changes by a bigger % than price", "Price does not change", "Quantity is fixed"], a: 1, why: "A big response." },
  { q: "Which is likely to have inelastic supply?", opts: ["Online software", "Mass-produced goods", "Housing", "A haircut"], a: 2, why: "Takes years to build." },
  { q: "An elastic supply curve is:", opts: ["Steep", "Flat", "Vertical", "Absent"], a: 1, why: "Flatter." },
  { q: "PES is normally:", opts: ["Negative", "Positive", "Zero", "Infinite"], a: 1, why: "Supply slopes upwards." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Price elasticity of supply", "A measure of the responsiveness of quantity supplied to a change in price."],
  ["Elastic supply", "Quantity supplied changes by a bigger percentage than price."],
  ["Inelastic supply", "Quantity supplied changes by a smaller percentage than price."],
  ["Spare capacity", "Unused ability to produce more."],
  ["Stocks", "Goods held in storage."],
  ["Responsiveness", "How much one variable reacts to another."],
  ["Output", "The quantity produced."],
  ["Short run", "A period too short to change capacity."],
  ["Long run", "A period long enough to change capacity."],
] });
labR(); 
