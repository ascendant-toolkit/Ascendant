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

Lib.stepper($("#stP"), { w: 760, h: 380, label: "Under, on and beyond the PPC", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1");
  if (s.n >= 1) o += ppcDot(80 * Math.cos(0.7), 90 * Math.sin(0.7), "A (on)", "dot3");
  if (s.n >= 2) o += ppcDot(32, 35, "B (inside)", "dot2");
  if (s.n >= 3) o += ppcDot(72, 78, "C (outside)", "dot4") + SV.text(PX(72) + 12, PY2(78) + 22, "unattainable now", "sm");
  return o;
}, steps: [
  { cap: "The PPC marks the limit of what the economy can produce.", s: { n: 0 } },
  { cap: "Point <b>A</b> is <b>on</b> the PPC: all resources fully and efficiently used.", s: { n: 1 } },
  { cap: "Point <b>B</b> is <b>inside</b> the PPC: resources are unemployed or wasted. The economy could produce more.", s: { n: 2 } },
  { cap: "Point <b>C</b> is <b>outside</b>: it cannot be reached with existing resources and technology.", s: { n: 3 } },
] });
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Recovery from a recession", base: { n: 0 }, draw: (s) => {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1") + ppcDot(32, 35, "B", "dot2");
  if (s.n >= 1) o += SV.line(PX(32), PY2(35), PX(32), PY2(90 * Math.sqrt(1 - (32 / 80) ** 2)), "c3");
  if (s.n >= 2) o += ppcDot(32, 90 * Math.sqrt(1 - (32 / 80) ** 2), "D", "dot3");
  if (s.n >= 3) o += SV.line(PX(32), PY2(35), PX(80 * Math.sqrt(1 - (35 / 90) ** 2)), PY2(35), "c3") + ppcDot(80 * Math.sqrt(1 - (35 / 90) ** 2), 35, "E", "dot3");
  return o;
}, steps: [
  { cap: "In a recession the economy is at <b>B</b>, inside the PPC, with unemployed resources.", s: { n: 0 } },
  { cap: "If unemployed resources are put to use, output can rise to the curve.", s: { n: 1 } },
  { cap: "Moving to <b>D</b> produces <b>more capital goods</b> with the same consumer goods: no opportunity cost.", s: { n: 2 } },
  { cap: "Or to <b>E</b>: more consumer goods with the same capital goods. Any point between D and E gives more of both.", s: { n: 3 } },
] });

/* Lab 1: place a point */
function labL() {
  if (!$("#la") || !$("#lb")) return;
  const x = +$("#la").value, y = +$("#lb").value, r = onPPC(x, y, 80, 90), st = r > 1.02 ? "Outside: unattainable" : r < 0.98 ? "Inside: inefficient" : "On: efficient";
  $("#la1").textContent = st.split(":")[0]; $("#la2").textContent = r < 0.98 ? "Yes" : "No"; $("#la3").textContent = r > 1.02 ? "Yes" : "No";
  $("#lav").textContent = `${x} consumer goods and ${y} capital goods: ${st.toLowerCase()}. ${r < 0.98 ? "Resources are unemployed or wasted: the economy could move up or out to the curve and produce more of one or both goods." : r > 1.02 ? "This is more than the economy can produce now; it needs economic growth to reach it." : "All resources are fully and efficiently used."}`;
  $("#labL").innerHTML = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC", "lbl bd t1") + ppcDrop(x, y) + ppcDot(x, y, "", r > 1.02 ? "dot4" : r < 0.98 ? "dot2" : "dot3");
}
Lib.slider($("#g1"), { id: "la", label: "Consumer goods produced", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Capital goods produced", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labL });
const WH = [
  { n: "A recession with high unemployment", p: "Inside the PPC", e: "Resources are unemployed." },
  { n: "Full employment and efficient production", p: "On the PPC", e: "Maximum output." },
  { n: "A target output beyond current capacity", p: "Outside the PPC", e: "Unattainable without growth." },
  { n: "A war destroys factories", p: "PPC shifts inwards; point may be inside", e: "Fewer resources." },
  { n: "Workers' skills do not match the jobs available", p: "Inside the PPC", e: "Resources are under-used." },
  { n: "Pollution closes farmland", p: "Inside or PPC shifts inwards", e: "Resources lost or wasted." },
];
button_table("whBtns", "whOut", WH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Position</th><th>Why</th></tr><tr><td><b>${p.p}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Where is each point compared with the PPC?", buckets: [{ label: "On the PPC" }, { label: "Inside the PPC" }, { label: "Outside the PPC" }], items: [
  { text: "Full employment of all resources", b: 0 }, { text: "Maximum efficient output", b: 0 },
  { text: "High unemployment in a recession", b: 1 }, { text: "Resources wasted by poor management", b: 1 },
  { text: "Unattainable with current resources", b: 2 }, { text: "Needs economic growth to reach", b: 2 },
], done: "On = efficient; inside = wasteful; outside = unattainable." });
Lib.classify($("#cl2"), { prompt: "Does each cause the economy to be <b>inside</b> its PPC or to <b>move to</b> it?", buckets: [{ label: "Moves inside" }, { label: "Moves to the PPC" }], items: [
  { text: "A rise in unemployment", b: 0 }, { text: "Factories left idle in a recession", b: 0 }, { text: "Skills mismatch", b: 0 },
  { text: "Unemployed workers find jobs", b: 1 }, { text: "Idle factories restart", b: 1 }, { text: "Better management", b: 1 },
], done: "Using resources moves the economy towards the curve." });
Lib.match($("#m1"), { prompt: "Match the position to its meaning.", pairs: [
  ["On the PPC", "Full and efficient use"],
  ["Inside the PPC", "Unemployed or wasted resources"],
  ["Outside the PPC", "Unattainable at present"],
  ["Recession", "The economy is inside its PPC"],
  ["Recovery", "Moving towards the PPC"],
  ["Economic growth", "A shift outwards of the PPC"],
], done: "Know what each position means." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an economy recovers from a recession</b>.", items: [
  "The economy is inside its PPC with unemployed resources",
  "Demand recovers and firms hire",
  "Unemployed resources are used",
  "Output of one or both goods rises",
  "The economy returns to the PPC",
], done: "Recovery uses idle resources." });
Lib.calc($("#c1"), { qs: [
  { q: "A point on an economy's PPC is 60 consumer goods and 70 capital goods. The economy actually produces 60 consumer goods and 40 capital goods. How many more capital goods could it produce with no loss of consumer goods?", a: 30, sol: "70 − 40 = <b>30</b>." },
  { q: "Output is 60% of capacity. Capacity is 200 units. How many units are produced?", a: 120, sol: "60% × 200 = <b>120</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A point inside the PPC shows:", opts: ["Full employment", "Unemployed or wasted resources", "Unattainable output", "Economic growth"], a: 1, why: "Inefficiency." },
  { q: "A point outside the PPC is:", opts: ["Efficient", "Unattainable now", "Inefficient", "A recession"], a: 1, why: "Beyond current resources." },
  { q: "Moving from inside the PPC to the curve has:", opts: ["A high opportunity cost", "No opportunity cost", "Fewer goods", "No benefit"], a: 1, why: "Unused resources are put to work." },
  { q: "Which could cause a point inside the PPC?", opts: ["High unemployment", "New technology", "More workers", "Better education"], a: 0, why: "Resources are idle." },
  { q: "To reach a point outside the PPC an economy needs:", opts: ["Unemployment", "Economic growth", "A recession", "Lower taxes only"], a: 1, why: "More or better resources." },
] });

Lib.cards($("#fc1"), { cards: [
  ["On the PPC", "Full and efficient use of resources."],
  ["Inside the PPC", "Under-used or wasted resources."],
  ["Outside the PPC", "Unattainable with current resources and technology."],
  ["Efficiency", "Using resources without waste."],
  ["Unemployment", "People who want to work but cannot find a job."],
  ["Recession", "A fall in real GDP for two consecutive quarters."],
  ["Recovery", "A rise in output after a recession."],
  ["Productive capacity", "The maximum output an economy can produce."],
  ["Full employment", "All available resources in use."],
] });
labL(); 
