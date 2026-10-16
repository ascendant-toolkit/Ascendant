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

/* business cycle: GDP wiggling around a rising trend */
const gdpT = (t) => 100 + 0.6 * t + 22 * Math.sin((2 * Math.PI * t) / 50);
const CX = (t) => 60 + t * 6.4, CYv = (g) => 330 - (g - 60) * 2.2;
function cycleChart(s) {
  const t = s.t; let o = SV.line(60, 340, 60, 30) + SV.line(60, 340, 710, 340) + SV.text(66, 40, "Real GDP", "sm") + SV.text(710, 362, "Time", "sm", { "text-anchor": "end" });
  o += SV.line(CX(0), CYv(100), CX(100), CYv(160), "dash", { style: "stroke:var(--muted);stroke-width:2" }) + SV.text(CX(100) - 4, CYv(160) - 8, "Trend (long-run growth)", "sm bd", { "text-anchor": "end" });
  const pts = []; for (let i = 0; i <= 100; i += 2) pts.push([CX(i), CYv(gdpT(i))]);
  o += SV.path(ptsPath(pts), "c3", { opacity: 0.45 });
  const done = []; for (let i = 0; i <= t; i += 1) done.push([CX(i), CYv(gdpT(i))]); done.push([CX(t), CYv(gdpT(t))]);
  if (done.length > 1) o += SV.path(ptsPath(done), "c1");
  o += SV.circle(CX(t), CYv(gdpT(t)), 8, "dot2");
  if (s.lbl) o += SV.text(CX(t), CYv(gdpT(t)) - 18, s.lbl, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}

function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (s.s > 1.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * 0.7071 + 10, oy - Y0 * 0.7071 + 22, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, s.s > 1.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const k = s.in || 0, px = ox + (X * 0.7071) * (1 - 0.25 * (1 - k)), py = oy - (Y * 0.7071) * (1 - 0.25 * (1 - k));
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Actual and potential growth on a PPC", base: { s: 1, in: 0 }, draw: ppcChart, steps: [
  { cap: "The economy is <b>inside its PPC</b>: some resources are unused (unemployed workers, idle factories). Output is below its potential.", s: { s: 1, in: 0 } },
  { cap: "<b>Actual growth:</b> spending rises and unused resources are put to work. The economy moves <b>towards the PPC</b>, and real GDP rises.", s: { s: 1, in: 1 } },
  { cap: "<b>Potential growth:</b> more or better resources and technology shift the PPC <b>outwards</b>. The economy can now produce more than before: <b>productive capacity</b> has grown.", s: { s: 1.2, in: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 400, label: "The business cycle", base: { t: 0, lbl: "" }, draw: cycleChart, steps: [
  { cap: "Real GDP tends to rise over time along a <b>long-run trend</b>, but not smoothly.", s: { t: 0, lbl: "Start" } },
  { cap: "In a <b>boom</b> output grows fast and unemployment is low. Demand may outstrip supply and prices rise.", s: { t: 12, lbl: "Boom" } },
  { cap: "Growth <b>slows</b>, then output <b>falls</b>. When real GDP falls for at least two quarters in a row, the economy is in <b>recession</b>.", s: { t: 28, lbl: "Recession" } },
  { cap: "At the <b>trough</b>, output is at its lowest. Unemployment is high and confidence is low.", s: { t: 37, lbl: "Trough" } },
  { cap: "<b>Recovery:</b> output starts to rise again, jobs return, and the economy heads back to trend and the next boom.", s: { t: 50, lbl: "Recovery" } },
] });

/* Lab 1: compound growth */
function labG() {
  if (!$("#ga") || !$("#gb")) return;
  const r = +$("#ga").value, n = +$("#gb").value, gdp = [100]; for (let i = 1; i <= n; i++) gdp.push(gdp[i - 1] * (1 + r / 100));
  $("#ga1").textContent = money(gdp[n], 1); $("#ga2").textContent = "+" + money(gdp[n] - 100, 1); $("#ga3").textContent = r > 0 ? money(70 / r, 0) + " years" : "never";
  $("#gav").textContent = `At ${r}% a year real GDP rises from 100 to ${money(gdp[n], 1)} after ${n} years. Small differences in the growth rate add up: compare 2% with 6%. A rough rule: GDP doubles in about 70 ÷ growth rate years.`;
  const base = 320, mx = Math.max(...gdp), k = 250 / Math.max(mx, 120), w = Math.min(28, 640 / (n + 1)), gap = w * 0.2;
  let o = SV.line(40, base, 740, base);
  gdp.forEach((v, i) => { const x = 50 + i * (w + gap); o += SV.rect(x, base - v * k, w, v * k, "", { style: "fill:var(--accent)", opacity: 0.8 }); if (n <= 12 || i % 2 === 0) o += SV.text(x + w / 2, base - v * k - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:10px" }); });
  $("#labG").innerHTML = o + SV.text(40, 24, "Real GDP index (start = 100)", "sm") + SV.text(740, base + 22, "Years", "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "ga", label: "Growth rate each year", min: 0, max: 10, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "gb", label: "Number of years", min: 1, max: 20, step: 1, value: 10, fmt: (v) => v + " years", onInput: labG });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>actual growth</b> (using spare resources) or <b>potential growth</b> (more productive capacity)?", buckets: [{ label: "Actual growth" }, { label: "Potential growth" }], items: [
  { text: "Unemployed workers get jobs after a rise in spending", b: 0 }, { text: "An economy moves from inside the PPC towards it", b: 0 }, { text: "AD shifts right and spare capacity is used", b: 0 }, { text: "Firms restart idle factories", b: 0 },
  { text: "The PPC shifts outwards", b: 1 }, { text: "AS shifts right", b: 1 }, { text: "New technology raises productivity", b: 1 }, { text: "More investment in machinery raises capacity", b: 1 },
], done: "Actual growth uses spare resources; potential growth raises the limit." });
Lib.classify($("#cl2"), { prompt: "Which <b>phase of the business cycle</b> does each describe?", buckets: [{ label: "Boom" }, { label: "Recession" }, { label: "Recovery" }], items: [
  { text: "Output is growing fast and unemployment is very low", b: 0 }, { text: "Demand outstrips supply and prices are rising", b: 0 },
  { text: "Real GDP falls for two quarters in a row", b: 1 }, { text: "Firms lay off workers and profits fall", b: 1 },
  { text: "Output starts to rise again after a trough", b: 2 }, { text: "Confidence returns and firms start to hire again", b: 2 },
], done: "The cycle: boom, slowdown, recession, recovery." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Economic growth", "An increase in real GDP (output) over time"],
  ["Productive capacity", "The most an economy can produce with its resources"],
  ["Business cycle", "The pattern of booms and recessions around a long-run trend"],
  ["Recession", "A fall in real GDP for at least two quarters in a row"],
  ["Boom", "A period of fast growth, high demand and low unemployment"],
  ["Potential output", "Output when resources are fully and efficiently used"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP was $2,000bn in 2022 and $2,100bn in 2023. What is the growth rate (%)?", a: 5, hint: "Change divided by the original, times 100.", sol: "(2,100 − 2,000) ÷ 2,000 × 100 = <b>5%</b>." },
  { q: "Real GDP was $8,750bn in 2016 and $9,362.5bn in 2017. Calculate the growth rate in 2017 (%). (India, past paper)", a: 7, sol: "(9,362.5 − 8,750) ÷ 8,750 × 100 = <b>7%</b>." },
  { q: "Real GDP is $400bn and grows at 5% a year. What is it after one year ($bn)?", a: 420, sol: "400 × 1.05 = <b>$420bn</b>." },
  { q: "An economy grows by 2% a year. Roughly how many years will it take for real GDP to double (70 ÷ rate)?", a: 35, sol: "70 ÷ 2 = <b>35 years</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is economic growth?", opts: ["A rise in the price level", "An increase in real GDP over time", "A fall in unemployment", "A rise in the exchange rate"], a: 1, why: "Growth is a rise in real output." },
  { q: "An outward shift of the PPC shows:", opts: ["Recession", "Potential (long-run) growth", "Unemployment", "Inflation"], a: 1, why: "The economy can now produce more." },
  { q: "A recession is usually defined as:", opts: ["A fall in prices", "A fall in real GDP for two successive quarters", "A fall in unemployment", "A rise in interest rates"], a: 1, why: "Two quarters of falling real GDP." },
  { q: "Which phase of the business cycle usually has the lowest unemployment?", opts: ["Recession", "Trough", "Boom", "Recovery"], a: 2, why: "Firms are hiring to meet high demand." },
  { q: "Which is most likely to raise an economy's productive capacity?", opts: ["A temporary tax cut", "Investment in new technology", "A fall in interest rates", "A rise in prices"], a: 1, why: "Technology raises output per worker." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Economic growth", "An increase in real GDP over time."],
  ["Actual growth", "A rise in real GDP as spare resources are used."],
  ["Potential growth", "A rise in productive capacity, shown by an outward shift of the PPC or AS shifting right."],
  ["Productive capacity", "The most an economy can produce with its resources."],
  ["Business cycle", "The pattern of booms and recessions around a long-run trend."],
  ["Recession", "A fall in real GDP for at least two quarters in a row."],
  ["Boom", "A period of fast growth and high demand."],
  ["Recovery", "Output rising again after a recession."],
  ["Trend growth", "The long-run average rate of growth of real GDP."],
] });
labG();
