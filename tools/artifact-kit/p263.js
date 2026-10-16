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

const SU = ["A brand of chocolate has many close rivals", "The price of the brand rises", "Consumers switch to rival brands", "Quantity demanded falls by a large %", "Demand is elastic"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Many substitutes", base: { n: 0 }, draw: mkChain(SU, "--good"), steps: chainSteps(["A brand of chocolate has <b>many close rivals</b>.", "The <b>price rises</b>.", "Consumers <b>switch</b> to rival brands.", "Quantity demanded falls by a <b>large %</b>.", "Demand is <b>elastic</b>."]) });
const NE = ["Petrol is a necessity for drivers", "The price of petrol rises", "Drivers still need to travel", "Quantity demanded falls by a small %", "Demand is inelastic"];
Lib.stepper($("#stN"), { w: 760, h: 380, label: "A necessity", base: { n: 0 }, draw: mkChain(NE, "--bad"), steps: chainSteps(["Petrol is a <b>necessity</b> for drivers.", "The <b>price rises</b>.", "Drivers still <b>need to travel</b>.", "Quantity demanded falls by a <b>small %</b>.", "Demand is <b>inelastic</b>."]) });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Time and elasticity", base: { k: 1 }, draw: (s) => axes() + pedCurve(s.k, "c1", s.k === 1 ? "Short-run D" : "Long-run D", "t1"), steps: [
  { cap: "In the <b>short run</b> consumers have few options: demand is <b>inelastic</b> (steep).", s: { k: 1 } },
  { cap: "In the <b>long run</b> consumers find alternatives: demand is <b>more elastic</b> (flatter).", s: { k: 3 } },
] });

/* Lab 1: score a good */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc") || !$("#dd")) return;
  const s = +$("#da").value, n = +$("#db").value, i = +$("#dc").value, t = +$("#dd").value, score = s + (5 - n) + i + t, ped = 0.2 + score * 0.12, lab = pedLabel(ped);
  $("#da1").textContent = money(ped, 2); $("#da2").textContent = lab.charAt(0).toUpperCase() + lab.slice(1); $("#da3").textContent = score + " / 20";
  $("#dav").textContent = `With ${s} out of 5 for substitutes, a necessity score of ${n}, ${i} for share of income and ${t} for time to adjust, the elasticity score is ${score}/20 and PED is roughly ${money(ped, 2)}: ${lab}. More substitutes, a luxury, a bigger share of income and more time all push demand towards elastic (illustrative model).`;
  const k = ped < 0.99 ? 1 : ped > 1.01 ? 3 : 2;
  $("#labD").innerHTML = axes() + pedCurve(k, "c1", "D") + SV.circle(X(50), Y(50), 6, "dot1");
}
Lib.slider($("#g1"), { id: "da", label: "Availability of substitutes (1 few, 5 many)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "How much of a necessity (1 luxury, 5 necessity)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Share of income spent (1 tiny, 5 large)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g4"), { id: "dd", label: "Time to adjust (1 short, 5 long)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
const GD = [
  { n: "Petrol (short run)", d: "Inelastic", w: "Necessity, few substitutes, habitual." },
  { n: "Petrol (long run)", d: "More elastic", w: "People move closer to work or buy efficient cars." },
  { n: "A brand of trainers", d: "Elastic", w: "Many rival brands." },
  { n: "Salt", d: "Inelastic", w: "Cheap, no substitute, tiny share of income." },
  { n: "Cigarettes", d: "Inelastic", w: "Addictive." },
  { n: "A new car", d: "Elastic", w: "Large share of income; can delay." },
];
button_table("gdBtns", "gdOut", GD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Demand is</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each make demand <b>more elastic</b> or <b>more inelastic</b>?", buckets: [{ label: "More elastic" }, { label: "More inelastic" }], items: [
  { text: "Many close substitutes", b: 0 }, { text: "A luxury good", b: 0 }, { text: "A large share of income", b: 0 }, { text: "A long time to adjust", b: 0 },
  { text: "Few substitutes", b: 1 }, { text: "A necessity", b: 1 }, { text: "A tiny share of income", b: 1 }, { text: "Addiction", b: 1 },
], done: "Substitutes, necessity, income share, time, habit." });
Lib.classify($("#cl2"), { prompt: "Is demand for each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "A branded soft drink", b: 0 }, { text: "A foreign holiday", b: 0 }, { text: "A new car", b: 0 },
  { text: "Salt", b: 1 }, { text: "Tap water", b: 1 }, { text: "Cigarettes", b: 1 },
], done: "Apply the determinants." });
Lib.match($("#m1"), { prompt: "Match the determinant to its effect.", pairs: [
  ["Many substitutes", "More elastic"],
  ["A necessity", "More inelastic"],
  ["Large share of income", "More elastic"],
  ["Long time period", "More elastic"],
  ["Addiction", "More inelastic"],
  ["Narrow definition (a brand)", "More elastic"],
], done: "Learn the determinants." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why demand for petrol is inelastic in the short run</b>.", items: [
  "Petrol is a necessity for travel",
  "There are few substitutes in the short run",
  "The price of petrol rises",
  "Drivers cut consumption only slightly",
  "Demand is inelastic",
], done: "Necessity plus few substitutes." });
Lib.calc($("#c1"), { qs: [
  { q: "A good has a PED of 0.5. Price rises 20%. By what percentage does quantity demanded fall?", a: 10, sol: "0.5 × 20 = <b>10%</b>." },
  { q: "A good has a PED of 2. Price rises 5%. By what percentage does quantity demanded fall?", a: 10, sol: "2 × 5 = <b>10%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which makes demand more elastic?", opts: ["Few substitutes", "A necessity", "Many close substitutes", "Addiction"], a: 2, why: "Easy to switch." },
  { q: "Demand for salt is inelastic because:", opts: ["It is a luxury", "It is a tiny share of income with no substitute", "It has many substitutes", "It is expensive"], a: 1, why: "Cheap and essential." },
  { q: "In the long run demand tends to be:", opts: ["More inelastic", "More elastic", "Unchanged", "Zero"], a: 1, why: "Time to find alternatives." },
  { q: "Which good is most likely to have elastic demand?", opts: ["Salt", "Petrol", "A brand of chocolate", "Insulin"], a: 2, why: "Many rival brands." },
  { q: "Addictive goods tend to have:", opts: ["Elastic demand", "Inelastic demand", "Perfectly elastic demand", "No demand"], a: 1, why: "Habit." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Determinants of PED", "Factors that decide how elastic or inelastic demand is."],
  ["Substitutes", "Goods that can replace each other."],
  ["Necessity", "A good that people need."],
  ["Luxury", "A good that people want but can do without."],
  ["Proportion of income", "The share of income spent on a good."],
  ["Time period", "Demand is more elastic in the long run."],
  ["Addictive good", "A good people find hard to stop buying."],
  ["Short run", "A period too short to change habits or find alternatives."],
  ["Long run", "A period long enough to adjust."],
] });
labD(); 
