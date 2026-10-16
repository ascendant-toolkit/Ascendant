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

const QT = ["More investment in machinery and technology", "Capital stock rises and improves", "Workers are more productive", "Productive capacity rises", "The economy can produce more goods and services: growth"];
Lib.stepper($("#stQ"), { w: 760, h: 380, label: "Better capital raises capacity", base: { n: 0 }, draw: mkChain(QT, "--good"), steps: chainSteps(["More <b>investment</b> in machinery and technology.", "The <b>capital stock</b> rises and improves in quality.", "Workers are <b>more productive</b>.", "<b>Productive capacity</b> rises.", "The economy can produce more goods and services: <b>growth</b>."]) });
const LB = ["The government spends more on education and training", "Workers gain skills and better health", "The quality of labour improves", "Output per worker (productivity) rises", "Costs fall and output can rise"];
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Better labour", base: { n: 0 }, draw: mkChain(LB, "--accent"), steps: chainSteps(["The government spends more on <b>education and training</b>.", "Workers gain <b>skills and better health</b>.", "The <b>quality of labour</b> improves.", "<b>Output per worker</b> (productivity) rises.", "Costs fall and output can rise."]) });
const DP = ["Resources such as oil or fish are used up faster than they are replaced", "The quantity of land falls", "Output from that resource falls", "Incomes and jobs fall; the country may need to import"];
Lib.stepper($("#stD"), { w: 760, h: 340, label: "Depletion", base: { n: 0 }, draw: mkChain(DP, "--bad"), steps: chainSteps(["Resources such as oil or fish are used up <b>faster than they are replaced</b>.", "The <b>quantity</b> of the resource falls.", "<b>Output</b> from that resource falls.", "Incomes and jobs fall; the country may need to <b>import</b>."]) });

/* Lab 1: capacity */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc")) return;
  const q = +$("#ca").value / 100, ql = +$("#cb").value / 100, cap = +$("#cc").value / 100, base0 = 100, out = base0 * (1 + q) * (1 + ql) * (1 + cap), g = out - base0;
  $("#ca1").textContent = money(out, 0); $("#ca2").textContent = (g >= 0 ? "+" : "−") + money(Math.abs(g), 0) + "%"; $("#ca3").textContent = money((1 + ql) * (1 + cap) * 100 - 100, 0) + "%";
  $("#cav").textContent = `Labour quantity ${q >= 0 ? "+" : ""}${Math.round(q * 100)}%, labour quality ${Math.round(ql * 100)}% and capital ${Math.round(cap * 100)}%: potential output moves from 100 to ${money(out, 0)} (${money(g, 0)}%). Improving quality raises output per worker (productivity) even if the number of workers does not change.`;
  const base = 290, k = 1.6; let o = SV.line(60, base, 700, base);
  [["Before", base0, "--accent"], ["After", out, g >= 0 ? "--good" : "--bad"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 24, "Potential output (index, before = 100)", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Change in the number of workers", min: -20, max: 30, step: 5, value: 5, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Change in worker skills (quality)", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Change in capital stock and technology", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labC });
const CE = [
  { n: "Discovery of oil", f: "Land", t: "Quantity", d: "Increase" },
  { n: "Soil erosion", f: "Land", t: "Quality", d: "Decrease" },
  { n: "Immigration", f: "Labour", t: "Quantity", d: "Increase" },
  { n: "More education and training", f: "Labour", t: "Quality", d: "Increase" },
  { n: "Brain drain (skilled workers leave)", f: "Labour", t: "Quality", d: "Decrease" },
  { n: "Investment in new factories", f: "Capital", t: "Quantity", d: "Increase" },
  { n: "New technology", f: "Capital", t: "Quality", d: "Increase" },
  { n: "Government support for start-ups", f: "Enterprise", t: "Quantity", d: "Increase" },
];
button_table("ceBtns", "ceOut", CE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Factor</th><th>Quantity or quality</th><th>Direction</th></tr><tr><td><b>${p.f}</b></td><td>${p.t}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each change the <b>quantity</b> or the <b>quality</b> of a factor?", buckets: [{ label: "Quantity" }, { label: "Quality" }], items: [
  { text: "Immigration of workers", b: 0 }, { text: "New oil discovered", b: 0 }, { text: "Building new factories", b: 0 }, { text: "More people start businesses", b: 0 },
  { text: "Training that raises skills", b: 1 }, { text: "Better technology in machines", b: 1 }, { text: "Fertilisers improve the soil", b: 1 }, { text: "Better health among workers", b: 1 },
], done: "More units, or better units." });
Lib.classify($("#cl2"), { prompt: "Does each <b>increase</b> or <b>decrease</b> the factor?", buckets: [{ label: "Increase" }, { label: "Decrease" }], items: [
  { text: "Discovery of new minerals", b: 0 }, { text: "Investment in education", b: 0 }, { text: "New technology", b: 0 }, { text: "Immigration of skilled workers", b: 0 },
  { text: "Depletion of fish stocks", b: 1 }, { text: "Brain drain", b: 1 }, { text: "Machines wearing out (depreciation)", b: 1 }, { text: "A flood destroying farmland", b: 1 },
], done: "Know both directions." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect.", pairs: [
  ["Education and training", "Higher quality of labour"],
  ["Immigration", "Larger labour force"],
  ["Investment in machinery", "Larger capital stock"],
  ["Discovery of oil", "More land (natural resources)"],
  ["Brain drain", "Lower quality of labour"],
  ["Depreciation", "Capital wears out"],
], done: "Link each cause to its effect." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how education improves the economy</b>.", items: [
  "The government invests in education and training",
  "Workers gain skills",
  "Labour productivity rises",
  "Output rises and costs fall",
  "Economic growth increases",
], done: "Quality leads to growth." });
Lib.calc($("#c1"), { qs: [
  { q: "A labour force of 20 million grows by 5%. How many workers are there now (million)?", a: 21, sol: "20 × 1.05 = <b>21 million</b>." },
  { q: "Output is 200 units from 20 workers. What is output per worker?", a: 10, sol: "200 ÷ 20 = <b>10 units</b>." },
  { q: "After training, output rises to 240 units with the same 20 workers. By what percentage does productivity rise?", a: 20, sol: "(12 − 10) ÷ 10 × 100 = <b>20%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which would increase the quantity of labour?", opts: ["Training", "Immigration", "Better technology", "Higher wages for few"], a: 1, why: "More workers." },
  { q: "Which would improve the quality of labour?", opts: ["Education and training", "Emigration", "Depreciation", "Population growth"], a: 0, why: "More skilled." },
  { q: "Investment in new machinery changes:", opts: ["Quantity of capital", "Quantity of land", "Quality of enterprise only", "Nothing"], a: 0, why: "More capital." },
  { q: "A brain drain:", opts: ["Raises labour quality", "Lowers labour quality", "Raises quantity of land", "Has no effect"], a: 1, why: "Skilled workers leave." },
  { q: "A cause of growth in an economy's factors is:", opts: ["Depletion", "Technological advance", "Flooding", "Depreciation"], a: 1, why: "Raises quality of capital." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Quantity of factors", "How much of a factor is available."],
  ["Quality of factors", "How productive each unit of a factor is."],
  ["Productivity", "Output per worker or per unit of input."],
  ["Investment", "Spending on capital goods."],
  ["Depreciation", "The wearing out of capital over time."],
  ["Immigration", "People moving into a country to live and work."],
  ["Brain drain", "The emigration of skilled and educated workers."],
  ["Depletion", "Using up natural resources."],
  ["Productive capacity", "The maximum output an economy can produce."],
] });
labC(); 
