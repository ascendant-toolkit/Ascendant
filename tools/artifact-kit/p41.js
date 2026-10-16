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

Lib.stepper($("#stP"), { w: 760, h: 380, label: "Building a PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes();
  if (s.n >= 1) o += SV.text(PX(0) - 8, PY2(90), "90", "sm", { "text-anchor": "end" }) + SV.text(PX(80), PY2(0) + 40, "80", "sm", { "text-anchor": "middle" }) + ppcDot(0, 90, "", "dot1") + ppcDot(80, 0, "", "dot1");
  if (s.n >= 2) o += SV.path(ppcPath(80, 90), "c1");
  if (s.n >= 2) o += SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  if (s.n >= 3) { const x = 80 * Math.cos(0.7), y = 90 * Math.sin(0.7); o += ppcDrop(x, y) + ppcDot(x, y, "A", "dot2"); }
  return o;
}, steps: [
  { cap: "Put capital goods on the vertical axis and consumer goods on the horizontal axis.", s: { n: 0 } },
  { cap: "If all resources make <b>capital goods</b> the economy makes 90 and no consumer goods. If all make <b>consumer goods</b> it makes 80 and no capital goods.", s: { n: 1 } },
  { cap: "Join the two ends with a curve bowed outwards: the <b>PPC</b>. Every point on it uses resources fully and efficiently.", s: { n: 2 } },
  { cap: "Point <b>A</b> on the curve is one combination of both goods the economy can produce.", s: { n: 3 } },
] });
const OC = ["Resources are scarce", "Choose to make more consumer goods", "Resources move from capital goods production", "Less capital goods are produced", "Opportunity cost = the capital goods given up"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "Opportunity cost on the PPC", base: { n: 0 }, draw: mkChain(OC, "--accent"), steps: chainSteps(["<b>Resources are scarce</b>.", "The economy chooses to make <b>more consumer goods</b>.", "<b>Resources move</b> from capital goods production.", "<b>Less capital goods</b> are produced.", "The opportunity cost is the <b>capital goods given up</b>."]) });

/* Lab 1: draw your own PPC */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc")) return;
  const a = +$("#pa").value, b = +$("#pb").value, share = +$("#pc").value / 100, t = (1 - share) * Math.PI / 2 * 0.99, x = a * Math.cos(Math.PI / 2 * share), y = b * Math.sin(Math.PI / 2 * share);
  const cx = a * Math.sin(Math.PI / 2 * (1 - share)), cy = b * Math.cos(Math.PI / 2 * (1 - share));
  const px = a * Math.cos(Math.PI / 2 * share), py = b * Math.sin(Math.PI / 2 * share);
  $("#pa1").textContent = money(px, 0); $("#pa2").textContent = money(py, 0); $("#pa3").textContent = Math.round(share * 100) + "%";
  $("#pav").textContent = `With ${Math.round(share * 100)}% of resources on capital goods the economy makes ${money(py, 0)} capital goods and ${money(px, 0)} consumer goods. Moving more resources to capital goods raises capital output but lowers consumer goods: that is the trade-off.`;
  $("#labP").innerHTML = ppcAxes() + SV.path(ppcPath(a, b), "c1") + ppcDrop(px, py) + ppcDot(px, py, "", "dot2") + SV.text(PX(a) , PY2(0) + 40, a, "sm", { "text-anchor": "middle" }) + SV.text(PX(0) - 8, PY2(b), b, "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "pa", label: "Maximum consumer goods (all resources on them)", min: 40, max: 100, step: 10, value: 80, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Maximum capital goods (all resources on them)", min: 40, max: 100, step: 10, value: 90, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Share of resources on capital goods", min: 5, max: 95, step: 5, value: 50, fmt: (v) => v + "%", onInput: labP });
const RD = [
  { n: "Both axes", d: "Label the two goods. Always label both axes." },
  { n: "Intercepts", d: "The maximum of one good if none of the other is produced." },
  { n: "Curve shape", d: "Bowed out: resources are not equally suited to both goods, so opportunity cost rises." },
  { n: "Point on the curve", d: "Full and efficient use of all resources." },
  { n: "Slope", d: "The trade-off between the two goods: the opportunity cost." },
];
button_table("rdBtns", "rdOut", RD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Meaning</th></tr><tr><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each statement <b>true</b> or <b>false</b> for a PPC?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "It shows the maximum combinations of two goods", b: 0 }, { text: "Every point on it uses resources fully", b: 0 }, { text: "It shows scarcity and opportunity cost", b: 0 }, { text: "It is usually drawn bowed outwards", b: 0 },
  { text: "It shows what consumers want to buy", b: 1 }, { text: "It shows unlimited production", b: 1 }, { text: "It can slope upwards", b: 1 },
], done: "A PPC shows what is possible, not what is wanted." });
Lib.match($("#m1"), { prompt: "Match the PPC term to its meaning.", pairs: [
  ["PPC", "Maximum combinations of two goods with existing resources"],
  ["Intercept", "Maximum of one good if none of the other is made"],
  ["Opportunity cost", "What is given up to produce more of the other good"],
  ["Bowed-out curve", "Opportunity cost rises as more of a good is made"],
  ["Straight-line PPC", "Constant opportunity cost"],
  ["Point on the curve", "Full and efficient use of resources"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>drawing a PPC</b>.", items: [
  "Label the axes with the two goods",
  "Mark the maximum of each good on its axis",
  "Join the points with a curve bowed outwards",
  "Label the curve PPC",
  "Mark and label a point on the curve",
], done: "Always label." });
Lib.calc($("#c1"), { qs: [
  { q: "On a PPC, an economy can make 90 capital goods or 80 consumer goods (not both). It produces 40 consumer goods and 78 capital goods. How many consumer goods are given up compared with the maximum?", a: 40, sol: "80 − 40 = <b>40</b>." },
  { q: "The PPC for good X and good Y: 100 X and 0 Y at one end, 60 X and 30 Y at another. What is the opportunity cost of moving to the second point in units of X?", a: 40, sol: "100 − 60 = <b>40 X</b> given up for 30 Y." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A PPC shows:", opts: ["Maximum combinations of two goods", "The demand curve", "Prices", "Unemployment"], a: 0, why: "What the economy can produce." },
  { q: "A point on the PPC represents:", opts: ["Wasted resources", "Full and efficient use of resources", "Unattainable output", "Inflation"], a: 1, why: "Maximum output." },
  { q: "A PPC is bowed outwards because:", opts: ["Resources are equally good at both", "Resources are not equally good at making both goods", "Prices rise", "Wants are unlimited"], a: 1, why: "Resources differ." },
  { q: "A PPC illustrates:", opts: ["Scarcity, choice and opportunity cost", "Inflation", "Demand and supply", "Trade"], a: 0, why: "The economic problem." },
  { q: "The end of the curve on the vertical axis shows:", opts: ["Zero of both goods", "Maximum of the vertical good with none of the other", "A free good", "Unemployment"], a: 1, why: "All resources on one good." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Production possibility curve", "A curve showing the maximum combinations of two goods an economy can produce with existing resources."],
  ["Consumer goods", "Goods bought by households to satisfy wants."],
  ["Capital goods", "Goods used to produce other goods and services."],
  ["Intercept", "The point where the curve meets an axis."],
  ["Concave", "Curved outwards, away from the origin."],
  ["Opportunity cost", "The next best alternative given up."],
  ["Efficiency", "Producing with no waste of resources."],
  ["Full employment of resources", "All available resources in use."],
  ["Trade-off", "Giving up one thing to get another."],
] });
labP(); 
