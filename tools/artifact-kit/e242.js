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

Lib.stepper($("#stE"), { w: 760, h: 380, label: "Finding equilibrium", base: { n: 0 }, draw: (s) => {
  let o = axes() + dCurve(0, "c1", "D") + sCurve(0, "c2", "S");
  if (s.n >= 1) o += SV.circle(X(50), Y(50), 8, "dot2");
  if (s.n >= 2) o += dsDrop(50, 50) + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (s.n >= 3) o += SV.text(X(52), Y(50) - 14, "Equilibrium", "lbl bd t2");
  return o;
}, steps: [
  { cap: "Demand D slopes down; supply S slopes up.", s: { n: 0 } },
  { cap: "They <b>intersect</b>: where quantity demanded equals quantity supplied.", s: { n: 1 } },
  { cap: "Read across for the <b>equilibrium price P</b> and down for the <b>equilibrium quantity Q</b>.", s: { n: 2 } },
  { cap: "At P the market <b>clears</b>: no shortage and no surplus.", s: { n: 3 } },
] });
const SC = ["Demand and supply are not equal at the current price", "Buyers or sellers cannot trade as they wish", "The price moves", "Quantities adjust", "The market settles where demand equals supply"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Why the market settles", base: { n: 0 }, draw: mkChain(SC, "--accent"), steps: chainSteps(["Demand and supply are <b>not equal</b> at the current price.", "Buyers or sellers <b>cannot trade as they wish</b>.", "The <b>price moves</b>.", "<b>Quantities adjust</b>.", "The market settles where <b>demand equals supply</b>."]) });

/* Lab 1: schedule and equilibrium */
function labE() {
  if (!$("#ea") || !$("#eb")) return;
  const d = +$("#ea").value, s = +$("#eb").value, [q, p] = eq(d, s);
  $("#ea1").textContent = "$" + money(p, 0); $("#ea2").textContent = money(q, 0); $("#ea3").textContent = "$" + money(p * q, 0);
  $("#eav").textContent = `With demand shifted by ${d} and supply by ${s}, equilibrium is at a price of $${money(p, 0)} and a quantity of ${money(q, 0)}. At this price quantity demanded (${money(qD(p, d), 0)}) equals quantity supplied (${money(qS(p, s), 0)}). Total spending (revenue) is $${money(p * q, 0)}.`;
  $("#labE").innerHTML = axes() + dCurve(d, "c1", "D") + sCurve(s, "c2", "S") + dsDrop(q, p) + SV.circle(X(q), Y(p), 8, "dot2") + SV.text(X(0) - 8, Y(p), "$" + money(p, 0), "sm bd", { "text-anchor": "end" }) + SV.text(X(q), Y(0) + 18, money(q, 0), "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ea", label: "Shift in demand (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labE });
Lib.slider($("#g2"), { id: "eb", label: "Shift in supply (right +, left −)", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labE });
const SCH = [[10, 20, 80], [8, 40, 60], [6, 50, 50], [4, 70, 30], [2, 90, 10]];
function labT() {
  const el = $("#schOut"); if (!el) return;
  const p = +($("#tp") ? $("#tp").value : 6), r = SCH.find((x) => x[0] === p) || SCH[2], diff = r[1] - r[2];
  $("#tp1").textContent = r[1]; $("#tp2").textContent = r[2]; $("#tp3").textContent = diff === 0 ? "Equilibrium" : diff > 0 ? "Shortage " + diff : "Surplus " + (-diff);
  el.innerHTML = `<div class="tw"><table class="t"><tr><th>Price</th><th>Qd</th><th>Qs</th><th>Result</th></tr>${SCH.map((x) => `<tr${x[0] === p ? ' class="hl"' : ""}><td>$${x[0]}</td><td>${x[1]}</td><td>${x[2]}</td><td>${x[1] === x[2] ? "<b>Equilibrium</b>" : x[1] > x[2] ? "Shortage " + (x[1] - x[2]) : "Surplus " + (x[2] - x[1])}</td></tr>`).join("")}</table></div>`;
}
Lib.slider($("#g3"), { id: "tp", label: "Price from the schedule", min: 2, max: 10, step: 2, value: 6, fmt: (v) => "$" + v, onInput: labT });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "At each price shown in the schedule above, is it a <b>shortage</b>, <b>surplus</b> or <b>equilibrium</b>?", buckets: [{ label: "Surplus" }, { label: "Equilibrium" }, { label: "Shortage" }], items: [
  { text: "$10 (Qd 20, Qs 80)", b: 0 }, { text: "$8 (Qd 40, Qs 60)", b: 0 },
  { text: "$6 (Qd 50, Qs 50)", b: 1 },
  { text: "$4 (Qd 70, Qs 30)", b: 2 }, { text: "$2 (Qd 90, Qs 10)", b: 2 },
], done: "Compare Qd and Qs." });
Lib.classify($("#cl2"), { prompt: "Is each statement about equilibrium <b>true</b> or <b>false</b>?", buckets: [{ label: "True" }, { label: "False" }], items: [
  { text: "At equilibrium, quantity demanded equals quantity supplied", b: 0 }, { text: "Equilibrium is where D and S intersect", b: 0 }, { text: "At equilibrium there is no shortage or surplus", b: 0 },
  { text: "Equilibrium is always fair", b: 1 }, { text: "Equilibrium cannot change", b: 1 }, { text: "At equilibrium there is always a shortage", b: 1 },
], done: "Equilibrium means the market clears." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market equilibrium", "Quantity demanded equals quantity supplied"],
  ["Equilibrium price", "The price at which demand equals supply"],
  ["Equilibrium quantity", "The quantity traded at the equilibrium price"],
  ["Market clearing", "No shortage or surplus"],
  ["Intersection of D and S", "The equilibrium point"],
  ["Schedule", "A table of prices and quantities"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a market moves to equilibrium from a surplus</b>.", items: [
  "The price is above equilibrium",
  "Quantity supplied exceeds quantity demanded",
  "Sellers cut prices to clear stock",
  "Quantity demanded rises; quantity supplied falls",
  "The market reaches equilibrium",
], done: "A surplus pushes price down." });
Lib.calc($("#c1"), { qs: [
  { q: "At a price of $6, quantity demanded is 50 and quantity supplied is 50. What is the equilibrium quantity?", a: 50, sol: "<b>50</b>: where they are equal." },
  { q: "The equilibrium price is $6 and the equilibrium quantity is 50. What is total revenue ($)?", a: 300, sol: "6 × 50 = <b>$300</b>." },
  { q: "At $4, Qd is 70 and Qs is 30. What is the shortage?", a: 40, sol: "70 − 30 = <b>40</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Market equilibrium is where:", opts: ["Demand exceeds supply", "Quantity demanded equals quantity supplied", "Supply exceeds demand", "Prices are zero"], a: 1, why: "The market clears." },
  { q: "On a diagram, equilibrium is found at:", opts: ["The y-axis", "The intersection of D and S", "The x-axis", "The top of D"], a: 1, why: "Where the curves cross." },
  { q: "At the equilibrium price there is:", opts: ["A shortage", "A surplus", "No shortage or surplus", "Unemployment"], a: 2, why: "Cleared." },
  { q: "The equilibrium price in the schedule above is:", opts: ["$10", "$8", "$6", "$2"], a: 2, why: "Qd = Qs = 50." },
  { q: "Equilibrium means:", opts: ["The outcome is fair", "Supply equals demand", "Prices never change", "No one wants to trade"], a: 1, why: "No tendency to change." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Market equilibrium", "Where quantity demanded equals quantity supplied."],
  ["Equilibrium price", "The price at which the market clears."],
  ["Equilibrium quantity", "The quantity traded at equilibrium."],
  ["Market clearing", "No shortage or surplus remains."],
  ["Demand schedule", "A table of quantities demanded at each price."],
  ["Supply schedule", "A table of quantities supplied at each price."],
  ["Intersection", "The point where two curves cross."],
  ["Quantity demanded", "Amount buyers want at a price."],
  ["Quantity supplied", "Amount sellers offer at a price."],
] });
labE(); labT(); 
