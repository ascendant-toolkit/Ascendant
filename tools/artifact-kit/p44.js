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

function shiftChart(s) {
  let o = ppcAxes() + SV.path(ppcPath(80, 90), "c1") + SV.text(PX(70), PY2(52), "PPC₁", "lbl bd t1");
  if (s.g[0] !== 0 || s.g[1] !== 0) { const a2 = 80 * (1 + s.g[0] / 100), b2 = 90 * (1 + s.g[1] / 100); o += SV.path(ppcPath(a2, b2), s.g[0] < 0 || s.g[1] < 0 ? "c4" : "c2") + SV.text(PX(a2 * 0.8) + 6, PY2(b2 * 0.65) - 6, "PPC₂", "lbl bd " + (s.g[0] < 0 || s.g[1] < 0 ? "t4" : "t2")); }
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Shifts of the PPC", base: { g: [0, 0] }, draw: shiftChart, steps: [
  { cap: "The economy's PPC today.", s: { g: [0, 0] } },
  { cap: "New technology and a better-trained workforce raise capacity for <b>both goods</b>: PPC shifts <b>outwards</b>. This is <b>economic growth</b>.", s: { g: [25, 25] } },
  { cap: "A war or natural disaster destroys resources: PPC shifts <b>inwards</b>.", s: { g: [-25, -25] } },
  { cap: "New farming technology raises capacity for <b>only one good</b>: a one-sided shift.", s: { g: [0, 30] } },
] });
const GR = ["Investment in capital and training today", "Capital and labour improve in quantity and quality", "Productive capacity rises", "The PPC shifts outwards", "Economic growth: more of both goods can be produced"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "From investment to growth", base: { n: 0 }, draw: mkChain(GR, "--good"), steps: chainSteps(["<b>Investment</b> in capital and training today.", "Capital and labour improve in <b>quantity and quality</b>.", "<b>Productive capacity</b> rises.", "The <b>PPC shifts outwards</b>.", "<b>Economic growth</b>: more of both goods can be produced."]) });

/* Lab 1 */
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const gx = +$("#sa").value, gy = +$("#sb").value, a2 = 80 * (1 + gx / 100), b2 = 90 * (1 + gy / 100);
  $("#sa1").textContent = money(a2, 0); $("#sa2").textContent = money(b2, 0); $("#sa3").textContent = gx === 0 && gy === 0 ? "No change" : gx >= 0 && gy >= 0 ? (gx === gy ? "Parallel outward" : "One-sided / uneven") : "Inward or mixed";
  $("#sav").textContent = `Maximum consumer goods ${money(a2, 0)} (was 80) and maximum capital goods ${money(b2, 0)} (was 90). ${gx > 0 && gy > 0 ? "Capacity rises for both goods: economic growth." : gx < 0 || gy < 0 ? "Capacity falls for at least one good: the economy has lost resources or technology." : "Capacity rises for one good only."}`;
  $("#labS").innerHTML = shiftChart({ g: [gx, gy] });
}
Lib.slider($("#g1"), { id: "sa", label: "Change in capacity for consumer goods", min: -30, max: 40, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Change in capacity for capital goods", min: -30, max: 40, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labS });
const CS = [
  { n: "New technology", d: "Outward shift", e: "Higher productivity." },
  { n: "Immigration of workers", d: "Outward shift", e: "More labour." },
  { n: "Education and training", d: "Outward shift", e: "Better-quality labour." },
  { n: "Discovery of oil", d: "Outward shift", e: "More land." },
  { n: "A major earthquake", d: "Inward shift", e: "Capital and lives lost." },
  { n: "War", d: "Inward shift", e: "Destroyed capacity." },
  { n: "Brain drain", d: "Inward shift", e: "Skills lost." },
  { n: "Unemployment falls", d: "Move to the PPC, not a shift", e: "Idle resources used." },
];
button_table("csBtns", "csOut", CS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the PPC</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Would each shift the PPC <b>outwards</b>, <b>inwards</b>, or just <b>move the economy to the PPC</b>?", buckets: [{ label: "Outwards" }, { label: "Inwards" }, { label: "Move to the PPC" }], items: [
  { text: "New technology", b: 0 }, { text: "More investment in factories", b: 0 }, { text: "Better education", b: 0 },
  { text: "A hurricane destroys factories", b: 1 }, { text: "Skilled workers emigrate", b: 1 },
  { text: "Unemployed workers find jobs", b: 2 }, { text: "Idle machines are used", b: 2 },
], done: "A shift needs a change in resources; a move to the PPC does not." });
Lib.classify($("#cl2"), { prompt: "Is each cause a change in the <b>quantity</b> or <b>quality</b> of resources?", buckets: [{ label: "Quantity" }, { label: "Quality" }], items: [
  { text: "Immigration", b: 0 }, { text: "Oil discovery", b: 0 }, { text: "New factories", b: 0 },
  { text: "Training", b: 1 }, { text: "Better technology", b: 1 }, { text: "Better health", b: 1 },
], done: "More or better resources shift the PPC." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect on the PPC.", pairs: [
  ["New technology", "Outward shift"],
  ["War", "Inward shift"],
  ["Falling unemployment", "Move to the PPC"],
  ["Immigration", "Outward shift (more labour)"],
  ["Depletion of resources", "Inward shift"],
  ["Farming technology only", "One-sided shift"],
], done: "Know the causes." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how education leads to economic growth</b>.", items: [
  "The government invests in education",
  "Workers become more skilled",
  "Productivity rises",
  "Productive capacity increases",
  "The PPC shifts outwards: economic growth",
], done: "Quality leads to growth." });
Lib.calc($("#c1"), { qs: [
  { q: "A country's maximum capital goods rise from 90 to 108 after a shift. What is the percentage increase?", a: 20, sol: "18 ÷ 90 × 100 = <b>20%</b>." },
  { q: "A country's potential output is 200 and grows by 4%. What is the new potential output?", a: 208, sol: "200 × 1.04 = <b>208</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An outward shift of the PPC shows:", opts: ["A recession", "Economic growth", "Unemployment", "Inflation"], a: 1, why: "Capacity rises." },
  { q: "Which could shift the PPC outwards?", opts: ["War", "New technology", "Brain drain", "A flood"], a: 1, why: "Raises productivity." },
  { q: "Which shifts the PPC inwards?", opts: ["Education", "A natural disaster", "Investment", "Immigration of workers"], a: 1, why: "Loss of resources." },
  { q: "A fall in unemployment is shown by:", opts: ["An outward shift", "An inward shift", "A move towards the PPC", "A new axis"], a: 2, why: "Idle resources used." },
  { q: "A shift of the PPC is caused by changes in:", opts: ["Prices", "Quantity or quality of resources", "Demand", "Taxes only"], a: 1, why: "Resources and technology." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Outward shift", "An increase in productive capacity: economic growth."],
  ["Inward shift", "A fall in productive capacity."],
  ["Economic growth", "An increase in an economy's productive capacity or real GDP."],
  ["Technology", "Knowledge and methods that raise productivity."],
  ["Investment", "Spending on capital goods."],
  ["Productive capacity", "The maximum output an economy can produce."],
  ["Brain drain", "Skilled workers emigrating."],
  ["Depletion", "Using up natural resources."],
  ["One-sided shift", "A shift where capacity rises for only one good."],
] });
labS(); 
