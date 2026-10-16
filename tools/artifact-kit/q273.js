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

const SP = ["A firm has spare capacity and stocks", "Demand and price rise", "The firm uses idle machines and sells stocks", "Output rises quickly by a large %", "Supply is elastic"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Spare capacity and stocks", base: { n: 0 }, draw: mkChain(SP, "--good"), steps: chainSteps(["A firm has <b>spare capacity and stocks</b>.", "Demand and <b>price rise</b>.", "The firm uses <b>idle machines</b> and sells stocks.", "Output rises quickly by a <b>large %</b>.", "Supply is <b>elastic</b>."]) });
const FC = ["A farm's land and machinery are fixed", "Price of wheat rises", "Farmers cannot grow more until the next season", "Output rises only slightly", "Supply is inelastic in the short run"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "Fixed capacity", base: { n: 0 }, draw: mkChain(FC, "--bad"), steps: chainSteps(["A farm's <b>land and machinery are fixed</b>.", "The <b>price of wheat</b> rises.", "Farmers <b>cannot grow more</b> until the next season.", "Output rises only <b>slightly</b>.", "Supply is <b>inelastic</b> in the short run."]) });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Time and elasticity", base: { k: 1 }, draw: (s) => axes() + pesCurve(s.k, "c2", s.k === 1 ? "Short-run S" : "Long-run S", "t2"), steps: [
  { cap: "In the <b>short run</b> firms are stuck with existing capacity: supply is <b>inelastic</b> (steep).", s: { k: 1 } },
  { cap: "In the <b>long run</b> firms can expand capacity: supply is <b>more elastic</b> (flatter).", s: { k: 3 } },
] });

/* Lab 1 */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc") || !$("#dd")) return;
  const t = +$("#da").value, c = +$("#db").value, s = +$("#dc").value, m = +$("#dd").value, score = t + c + s + m, pes = 0.1 + score * 0.14, lab = pesLabel(pes);
  $("#da1").textContent = money(pes, 2); $("#da2").textContent = lab.charAt(0).toUpperCase() + lab.slice(1); $("#da3").textContent = score + " / 20";
  $("#dav").textContent = `Time to adjust ${t}, spare capacity ${c}, stocks ${s} and factor mobility ${m} give a score of ${score}/20 and PES of about ${money(pes, 2)}: ${lab}. More time, more spare capacity, more stocks and more mobile resources make supply more elastic (illustrative model).`;
  const k = pes < 0.99 ? 1 : pes > 1.01 ? 3 : 2;
  $("#labD").innerHTML = axes() + pesCurve(k, "c2", "S") + SV.circle(X(50), Y(50), 6, "dot1");
}
Lib.slider($("#g1"), { id: "da", label: "Time to adjust (1 short, 5 long)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "Spare capacity (1 none, 5 lots)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Stocks of finished goods (1 none, 5 lots)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g4"), { id: "dd", label: "Mobility of resources (1 low, 5 high)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
const GD = [
  { n: "Fresh fruit (short run)", d: "Inelastic", w: "Perishable; limited by the growing season." },
  { n: "Housing", d: "Inelastic", w: "Takes years to build; land limited." },
  { n: "Mass-produced clothes", d: "Elastic", w: "Spare capacity and stocks; quick production." },
  { n: "Wheat (long run)", d: "More elastic", w: "Farmers can plant more acres over several seasons." },
  { n: "Online services", d: "Elastic", w: "Additional supply costs little." },
];
button_table("gdBtns", "gdOut", GD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Supply is</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each make supply more <b>elastic</b> or more <b>inelastic</b>?", buckets: [{ label: "More elastic" }, { label: "More inelastic" }], items: [
  { text: "Spare capacity", b: 0 }, { text: "Large stocks of goods", b: 0 }, { text: "A long time period", b: 0 }, { text: "Mobile, flexible resources", b: 0 },
  { text: "Firms at full capacity", b: 1 }, { text: "Perishable goods", b: 1 }, { text: "A short time period", b: 1 }, { text: "Specialised resources", b: 1 },
], done: "Time, capacity, stocks, mobility." });
Lib.classify($("#cl2"), { prompt: "Is supply of each likely to be <b>elastic</b> or <b>inelastic</b> in the short run?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "Factory-made shirts", b: 0 }, { text: "Online software", b: 0 },
  { text: "Housing", b: 1 }, { text: "A crop between harvests", b: 1 }, { text: "Fresh fish", b: 1 },
], done: "Apply the determinants." });
Lib.match($("#m1"), { prompt: "Match the determinant to its effect.", pairs: [
  ["Spare capacity", "More elastic"],
  ["Large stocks", "More elastic"],
  ["Long time period", "More elastic"],
  ["Perishable goods", "More inelastic"],
  ["Specialised factors", "More inelastic"],
  ["Full capacity", "More inelastic"],
], done: "Learn the determinants." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why housing supply is inelastic</b>.", items: [
  "House prices rise",
  "Builders want to build more",
  "Planning and construction take years and land is limited",
  "Output rises only slightly in the short run",
  "Supply is inelastic",
], done: "Time and land limits." });
Lib.calc($("#c1"), { qs: [
  { q: "A good has a PES of 2. Price rises 5%. By what percentage does quantity supplied rise?", a: 10, sol: "2 × 5 = <b>10%</b>." },
  { q: "A firm at 90% capacity can raise output by at most 11% (to full capacity). Price rises 20%. What is the maximum PES (1 decimal place)?", a: 0.6, sol: "11 ÷ 20 ≈ <b>0.6</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which makes supply more elastic?", opts: ["Full capacity", "Spare capacity", "Perishable goods", "A short time period"], a: 1, why: "Easy to produce more." },
  { q: "Supply of fresh strawberries is inelastic in the short run because:", opts: ["They are stored", "They take time to grow and spoil quickly", "Costs are zero", "Demand is high"], a: 1, why: "Growing season and perishability." },
  { q: "In the long run supply tends to be:", opts: ["More inelastic", "More elastic", "Unchanged", "Zero"], a: 1, why: "Time to expand capacity." },
  { q: "Which good has the most elastic supply?", opts: ["Housing", "Fresh fruit", "Factory-made clothes", "A rare painting"], a: 2, why: "Spare capacity and stocks." },
  { q: "Stocks of finished goods make supply:", opts: ["More inelastic", "More elastic", "Zero", "Fixed"], a: 1, why: "Can be sold quickly." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Determinants of PES", "Factors that decide how elastic or inelastic supply is."],
  ["Spare capacity", "Unused productive capacity."],
  ["Stocks", "Goods held in storage."],
  ["Mobility of factors", "How easily resources move between uses."],
  ["Perishable good", "A good that spoils quickly."],
  ["Time period", "Supply is more elastic in the long run."],
  ["Short run", "A period too short to change capacity."],
  ["Long run", "A period long enough to adjust."],
  ["Production time", "How long it takes to make more."],
] });
labD(); 
