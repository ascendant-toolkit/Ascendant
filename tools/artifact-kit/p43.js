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

const PX = (x) => 90 + x * 5.4, PY2 = (y) => 310 - y * 2.3;
function ppcPath(a, b) { let d = ""; for (let i = 0; i <= 40; i++) { const t = (i / 40) * Math.PI / 2, x = a * Math.cos(t), y = b * Math.sin(t); d += (i ? "L" : "M") + PX(x).toFixed(1) + " " + PY2(y).toFixed(1); } return d; }
function ppcAxes(xl, yl) { return SV.line(PX(0), PY2(0), PX(0), PY2(130)) + SV.line(PX(0), PY2(0), PX(118), PY2(0)) + SV.text(PX(0) + 8, 14, yl || "Capital goods", "sm") + SV.text(PX(118), PY2(0) + 24, xl || "Consumer goods", "sm", { "text-anchor": "end" }); }
function ppcDot(x, y, lab, cl, side) { return SV.circle(PX(x), PY2(y), 7, cl || "dot1") + SV.text(PX(x) + (side === "l" ? -12 : 12), PY2(y) + (side === "l" ? -6 : 4), lab, "lbl bd", { "text-anchor": side === "l" ? "end" : "start" }); }
function ppcDrop(x, y) { return SV.line(PX(0), PY2(y), PX(x), PY2(y), "gr") + SV.line(PX(x), PY2(y), PX(x), PY2(0), "gr"); }
function onPPC(x, y, a, b) { return (x / a) ** 2 + (y / b) ** 2; }

Lib.stepper($("#stM"), { w: 760, h: 380, label: "Moving along the PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  const pt = (t) => [80 * Math.cos(t), 90 * Math.sin(t)], a = pt(1.1), b = pt(0.7);
  o += ppcDot(a[0], a[1], "A", "dot1");
  if (s.n >= 1) o += ppcDrop(a[0], a[1]);
  if (s.n >= 2) o += ppcDot(b[0], b[1], "B", "dot2") + SV.line(PX(a[0]), PY2(a[1]), PX(b[0]), PY2(b[1]), "c3");
  if (s.n >= 3) o += ppcDrop(b[0], b[1]) + SV.text(PX(b[0]) - 6, PY2(a[1]) + 24, "gained: " + Math.round(b[0] - a[0]) + " consumer", "sm bd t3", { "text-anchor": "middle" }) + SV.text(PX(0) + 16, PY2((a[1] + b[1]) / 2), "lost: " + Math.round(a[1] - b[1]) + " capital", "sm bd t2");
  return o;
}, steps: [
  { cap: "The economy starts at <b>A</b> on its PPC.", s: { n: 0 } },
  { cap: "It decides to produce more consumer goods.", s: { n: 1 } },
  { cap: "It moves along the PPC to <b>B</b>: more consumer goods, but fewer capital goods.", s: { n: 2 } },
  { cap: "The capital goods given up are the <b>opportunity cost</b> of the extra consumer goods.", s: { n: 3 } },
] });
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Rising opportunity cost", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1");
  const ts = [1.4, 1.1, 0.8, 0.5, 0.2], ps = ts.map((t) => [80 * Math.cos(t), 90 * Math.sin(t)]);
  ps.forEach((p, i) => { if (i <= s.n) o += SV.circle(PX(p[0]), PY2(p[1]), 6, "dot1"); if (i > 0 && i <= s.n) { const q = ps[i - 1], lost = q[1] - p[1], gain = p[0] - q[0]; o += SV.line(PX(q[0]), PY2(q[1]), PX(p[0]), PY2(p[1]), "c3") + SV.text(PX((p[0] + q[0]) / 2) + 10, PY2((p[1] + q[1]) / 2) - 8, money(lost / gain, 1), "sm bd t2"); } });
  return o + SV.text(PX(55), PY2(95), "Labels: capital goods given up per extra consumer good", "sm");
}, steps: [
  { cap: "Start with almost all resources making capital goods.", s: { n: 0 } },
  { cap: "The first moves cost <b>few</b> capital goods per extra consumer good.", s: { n: 1 } },
  { cap: "The cost per extra consumer good rises.", s: { n: 2 } },
  { cap: "Higher still.", s: { n: 3 } },
  { cap: "Near the end, each extra consumer good costs <b>many</b> capital goods: <b>rising opportunity cost</b> gives the bowed-out shape.", s: { n: 4 } },
] });

/* Lab 1: opportunity cost calculator */
function labO() {
  if (!$("#oa")) return;
  const x = +$("#oa").value, y0 = 90, y = 90 * Math.sqrt(1 - (x / 80) ** 2), x1 = Math.min(80, x + 10), y1 = 90 * Math.sqrt(1 - (x1 / 80) ** 2), oc = x1 > x ? (y - y1) / (x1 - x) : 0;
  $("#oa1").textContent = money(y, 0); $("#oa2").textContent = money(y0 - y, 0); $("#oa3").textContent = money(oc, 2);
  $("#oav").textContent = `At ${x} consumer goods the economy can make ${money(y, 0)} capital goods, having given up ${money(y0 - y, 0)} compared with the maximum of 90. Making 10 more consumer goods would cost ${money(y - y1, 0)} more capital goods: ${money(oc, 2)} per extra unit. Move the slider right and the cost per unit rises.`;
  $("#labO").innerHTML = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + ppcDrop(x, y) + ppcDot(x, y, "", "dot2") + SV.circle(PX(x1), PY2(y1), 6, "dot4");
}
Lib.slider($("#g1"), { id: "oa", label: "Consumer goods produced", min: 0, max: 70, step: 5, value: 30, fmt: (v) => v, onInput: labO });
const MV = [
  { n: "More consumer goods", d: "Move down-right along the PPC", e: "Fewer capital goods produced." },
  { n: "More capital goods", d: "Move up-left along the PPC", e: "Fewer consumer goods produced." },
  { n: "Bowed-out PPC", d: "Opportunity cost rises", e: "Resources are not equally good at both." },
  { n: "Straight-line PPC", d: "Constant opportunity cost", e: "Resources equally good at both." },
  { n: "Investing today", d: "Fewer consumer goods now", e: "More capital goods; may shift the PPC later." },
];
button_table("mvBtns", "mvOut", MV, 0, (p) => `<div class="tw"><table class="t"><tr><th>What happens</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>movement along</b> a PPC or a <b>shift</b> of the PPC?", buckets: [{ label: "Movement along" }, { label: "Shift of the PPC" }], items: [
  { text: "Producing more consumer goods and fewer capital goods", b: 0 }, { text: "A government moves resources to healthcare from defence", b: 0 }, { text: "Choosing more capital goods this year", b: 0 },
  { text: "New technology raises capacity", b: 1 }, { text: "A war destroys factories", b: 1 }, { text: "Immigration raises the labour force", b: 1 },
], done: "Movement along means reallocating existing resources." });
Lib.match($("#m1"), { prompt: "Match the PPC shape to its meaning.", pairs: [
  ["Bowed outwards", "Rising opportunity cost"],
  ["Straight line", "Constant opportunity cost"],
  ["Moving along the PPC", "Reallocating resources between goods"],
  ["Gain of one good", "Loss of the other"],
  ["Opportunity cost", "Goods given up when resources are switched"],
  ["Mobility of resources", "How easily they switch between uses"],
], done: "Know the shapes." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why the opportunity cost rises along a bowed PPC</b>.", items: [
  "The economy makes more of one good",
  "Resources less suited to it must be switched",
  "Output per resource falls",
  "More of the other good is given up for each extra unit",
  "Opportunity cost rises",
], done: "The reason for the bowed shape." });
Lib.calc($("#c1"), { qs: [
  { q: "Moving from 20 consumer goods and 86 capital goods to 40 consumer goods and 76 capital goods, how many capital goods are given up?", a: 10, sol: "86 − 76 = <b>10</b>." },
  { q: "In the same move, what is the opportunity cost per extra consumer good (capital goods)?", a: 0.5, sol: "10 ÷ 20 = <b>0.5</b>." },
  { q: "Moving from 60 consumer goods and 60 capital goods to 80 consumer goods and 0 capital goods, what is the opportunity cost per extra consumer good (capital goods)?", a: 3, sol: "60 ÷ 20 = <b>3</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Moving along the PPC means:", opts: ["Using unemployed resources", "Reallocating resources between goods", "Economic growth", "A recession"], a: 1, why: "A choice." },
  { q: "The opportunity cost of more consumer goods is:", opts: ["The extra consumer goods", "The capital goods given up", "Nothing", "Unemployment"], a: 1, why: "What is lost." },
  { q: "A bowed-out PPC shows:", opts: ["Constant opportunity cost", "Rising opportunity cost", "Zero opportunity cost", "Unemployment"], a: 1, why: "Resources differ." },
  { q: "A straight-line PPC shows:", opts: ["Rising opportunity cost", "Constant opportunity cost", "Economic growth", "A free good"], a: 1, why: "Resources are equally suitable." },
  { q: "Choosing more capital goods now means:", opts: ["More consumer goods now", "Fewer consumer goods now", "No change", "A smaller PPC later"], a: 1, why: "A trade-off." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Movement along a PPC", "Reallocating resources from one good to another."],
  ["Opportunity cost", "The next best alternative given up."],
  ["Rising opportunity cost", "More of one good must be given up for each extra unit of the other."],
  ["Constant opportunity cost", "A fixed amount given up per extra unit, shown by a straight line."],
  ["Trade-off", "Giving up one thing for another."],
  ["Mobility of resources", "How easily resources can switch between uses."],
  ["Capital goods", "Goods used to produce other goods."],
  ["Consumer goods", "Goods used by households."],
  ["Consumption now vs the future", "More consumption now means fewer capital goods and slower growth."],
] });
labO(); 
