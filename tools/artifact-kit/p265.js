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

const GV = ["The government taxes cigarettes (inelastic demand)", "The price rises", "Quantity demanded falls only slightly", "Tax revenue is high but consumption barely falls", "The tax raises revenue more than it reduces smoking"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "Taxing an inelastic good", base: { n: 0 }, draw: mkChain(GV, "--bad"), steps: chainSteps(["The government <b>taxes cigarettes</b> (inelastic demand).", "The <b>price rises</b>.", "Quantity demanded falls only <b>slightly</b>.", "<b>Tax revenue is high</b> but consumption barely falls.", "The tax <b>raises revenue</b> more than it reduces smoking."]) });
const FM = ["A firm sells an elastic good", "It cuts its price", "Quantity sold rises by a bigger %", "Revenue rises", "Cutting price is a sensible strategy (if costs allow)"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "A firm's pricing", base: { n: 0 }, draw: mkChain(FM, "--good"), steps: chainSteps(["A firm sells an <b>elastic</b> good.", "It <b>cuts its price</b>.", "Quantity sold rises by a <b>bigger %</b>.", "<b>Revenue rises</b>.", "Cutting price can work (if costs allow)."]) });
const WK = ["Workers' union demands a pay rise", "Firm's costs rise; it raises the product price", "Demand for the product is elastic: sales fall a lot", "Firm needs fewer workers", "Jobs may be lost"];
Lib.stepper($("#stW"), { w: 760, h: 380, label: "Workers and PED", base: { n: 0 }, draw: mkChain(WK, "--warn"), steps: chainSteps(["A union demands a <b>pay rise</b>.", "The firm's <b>costs rise</b>; it raises the price.", "If demand is <b>elastic</b>, sales fall a lot.", "The firm needs <b>fewer workers</b>.", "<b>Jobs may be lost</b>."]) });

/* Lab 1: tax revenue */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const tax = +$("#ta").value, ped = +$("#tb").value / 10, p0 = 10, q0 = 100, p1 = p0 + tax, q1 = q0 * (1 - ped * (tax / p0)), rev = tax * q1, drop = q0 - q1;
  $("#ta1").textContent = money(Math.max(0, q1), 0); $("#ta2").textContent = "$" + money(Math.max(0, rev), 0); $("#ta3").textContent = money((drop / q0) * 100, 0) + "%";
  $("#tav").textContent = `A $${tax} tax raises the price from $10 to $${p1} (+${money((tax / p0) * 100, 0)}%). With PED ${money(ped, 1)} (${pedLabel(ped)}), quantity falls from 100 to ${money(Math.max(0, q1), 0)} (${money((drop / q0) * 100, 0)}% fall). Tax revenue is $${tax} × ${money(Math.max(0, q1), 0)} = $${money(Math.max(0, rev), 0)}. ${ped < 1 ? "Inelastic: high revenue, small fall in consumption." : "Elastic: large fall in consumption, lower revenue."}`;
  const base = 290; let o = SV.line(60, base, 700, base);
  [["Quantity before", 100, "--accent"], ["Quantity after", Math.max(0, q1), "--warn"], ["Tax revenue", Math.max(0, rev) / 5, "--good"]].forEach(([n, v, c], i) => { const x = 110 + i * 190, h = v * 2; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, i === 2 ? "$" + money(Math.max(0, rev), 0) : money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labT").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ta", label: "Tax per unit (price starts at $10)", min: 1, max: 5, step: 1, value: 2, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g2"), { id: "tb", label: "PED (size, ×0.1)", min: 2, max: 25, step: 1, value: 4, fmt: (v) => money(v / 10, 1), onInput: labT });
const DM = [
  { n: "Consumers", d: "Know which goods they can avoid buying when prices rise." },
  { n: "Workers", d: "Pay claims are more affordable when product demand is inelastic." },
  { n: "Firms", d: "Choose price rises or cuts to raise revenue." },
  { n: "Government", d: "Taxes on inelastic goods raise revenue; on elastic goods cut consumption." },
];
button_table("dmBtns", "dmOut", DM, 0, (p) => `<div class="tw"><table class="t"><tr><th>How PED helps</th></tr><tr><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> uses PED this way?", buckets: [{ label: "Firm" }, { label: "Government" }, { label: "Worker/union" }, { label: "Consumer" }], items: [
  { text: "Cutting prices on an elastic good to raise revenue", b: 0 }, { text: "Charging more for an inelastic good", b: 0 },
  { text: "Taxing cigarettes to raise revenue", b: 1 }, { text: "Choosing which goods to tax", b: 1 },
  { text: "Asking for higher pay when demand for the product is inelastic", b: 2 },
  { text: "Switching away from a dearer elastic good", b: 3 },
], done: "PED guides decisions." });
Lib.classify($("#cl2"), { prompt: "Is each tax <b>good at raising revenue</b> or <b>good at cutting consumption</b>?", buckets: [{ label: "Raises revenue" }, { label: "Cuts consumption" }], items: [
  { text: "A tax on an inelastic good", b: 0 }, { text: "A tax on cigarettes", b: 0 }, { text: "A tax on an elastic good", b: 1 }, { text: "A tax on a luxury with many substitutes", b: 1 },
], done: "Inelastic: revenue. Elastic: consumption." });
Lib.match($("#m1"), { prompt: "Match the situation to the implication.", pairs: [
  ["Inelastic demand, firm raises price", "Revenue rises"],
  ["Elastic demand, firm cuts price", "Revenue rises"],
  ["Tax on inelastic good", "High revenue, small fall in consumption"],
  ["Tax on elastic good", "Large fall in consumption"],
  ["Inelastic product demand", "Union pay claims cost fewer jobs"],
  ["Price discrimination", "Charge more where demand is inelastic"],
], done: "Link PED to decisions." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a tax on cigarettes raises a lot of revenue</b>.", items: [
  "The government taxes cigarettes",
  "The price rises",
  "Demand is inelastic so quantity falls only a little",
  "Many units are still sold",
  "Tax revenue is high",
], done: "Inelastic goods are good revenue-raisers." });
Lib.calc($("#c1"), { qs: [
  { q: "A $2 tax is placed on each unit. 80 units are still sold. What is the tax revenue ($)?", a: 160, sol: "2 × 80 = <b>$160</b>." },
  { q: "PED is 0.4 and a tax raises the price by 25%. By what percentage does quantity demanded fall?", a: 10, sol: "0.4 × 25 = <b>10%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Governments tax goods with inelastic demand because:", opts: ["Revenue stays high", "Consumption falls a lot", "They are luxuries", "Prices fall"], a: 0, why: "Quantity falls little." },
  { q: "A firm with inelastic demand that wants more revenue should:", opts: ["Cut price", "Raise price", "Do nothing", "Stop selling"], a: 1, why: "Revenue rises with price." },
  { q: "Workers can seek pay rises more safely when product demand is:", opts: ["Elastic", "Inelastic", "Zero", "Falling"], a: 1, why: "Higher prices will not cut sales much." },
  { q: "A tax is most effective at cutting consumption when demand is:", opts: ["Inelastic", "Elastic", "Zero", "Unitary only"], a: 1, why: "Quantity responds." },
  { q: "Which good is the best source of tax revenue?", opts: ["A brand of chocolate", "Cigarettes", "Holidays", "Restaurant meals"], a: 1, why: "Inelastic demand." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Indirect tax", "A tax on goods and services."],
  ["Price discrimination", "Charging different prices to different groups for the same good."],
  ["Pay claim", "A request by workers for higher wages."],
  ["Tax revenue", "Money raised by taxes."],
  ["Consumption", "The quantity of a good consumed."],
  ["Strategy", "A plan to achieve an aim."],
  ["Promotion", "A temporary price cut or offer."],
  ["Short-run", "A period too short to adjust."],
  ["Reliability", "How far PED estimates can be trusted."],
] });
labT(); 
