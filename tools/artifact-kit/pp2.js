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

const PYR = {
  young: { n: "Young population (like Haiti or Niger)", b: [33, 27, 20, 14, 6] },
  mid: { n: "Middle-aged population (like Chile)", b: [20, 24, 24, 22, 10] },
  old: { n: "Ageing population (like Japan)", b: [12, 14, 16, 30, 28] },
};
const BANDS = ["0-14", "15-29", "30-44", "45-64", "65+"];
function pyrChart(b) {
  const cx = 380, k = 9, bh = 46; let o = SV.line(cx, 20, cx, 290) + SV.text(cx - 6, 14, "Male", "sm", { "text-anchor": "end" }) + SV.text(cx + 6, 14, "Female", "sm");
  b.forEach((v, i) => { const y = 250 - i * (bh + 6), w = (v / 2) * k; o += SV.rect(cx - w, y, w, bh, "", { style: `fill:var(${i === 0 || i === 4 ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.rect(cx, y, w, bh, "", { style: `fill:var(${i === 0 || i === 4 ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(cx - w - 8, y + bh / 2 + 4, v + "%", "sm bd", { "text-anchor": "end" }) + SV.text(cx + 330, y + bh / 2 + 4, BANDS[i], "sm"); });
  return o + SV.text(cx + 330, 300, "Age", "sm") + SV.text(60, 326, "Amber bars: dependants (0-14 and 65+). Blue: working age.", "sm");
}

function optChart(s) {
  const T = s.T, Ls = 40 * T, Ym = 20 * T, f = (L) => Math.max(0, Ym * (1 - Math.pow((L - Ls) / (Ls + 20), 2))), X = (L) => 80 + L * 6, Y = (v) => 330 - v * 6.2;
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 48, "Output per head", "sm") + SV.text(710, 362, "Population size", "sm", { "text-anchor": "end" });
  const pts = []; for (let L = 4; L <= 100; L += 2) pts.push([X(L), Y(f(L))]);
  o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 }) + SV.line(X(Ls), Y(Ym), X(Ls), 340, "dash", { style: "stroke:var(--good);stroke-width:2" }) + SV.text(X(Ls), 358, "Optimum", "sm bd", { "text-anchor": "middle" });
  o += SV.circle(X(s.L), Y(f(s.L)), 8, Math.abs(s.L - Ls) < 4 ? "dot3" : "dot2");
  const st = Math.abs(s.L - Ls) < 5 ? "Optimum population" : s.L < Ls ? "Underpopulated" : "Overpopulated";
  o += SV.text(X(s.L), Y(f(s.L)) - 18, st, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 400, label: "Under-population, optimum and over-population", base: { L: 15, T: 1 }, draw: optChart, steps: [
  { cap: "The country is <b>underpopulated</b>: there are too few people to use its land and resources. Output per head is low and <b>more people would raise it</b>.", s: { L: 15, T: 1 } },
  { cap: "As population grows to the <b>optimum</b>, workers specialise, markets grow and output per head <b>reaches its maximum</b>.", s: { L: 40, T: 1 } },
  { cap: "Beyond the optimum the country is <b>overpopulated</b>: too many people share the same land and capital. Output per head <b>falls</b>.", s: { L: 75, T: 1 } },
  { cap: "New <b>technology, capital and education</b> raise the optimum. The same population is now closer to the optimum, with higher output per head: the optimum is <b>not fixed</b>.", s: { L: 75, T: 1.8 } },
] });
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (Math.abs(s.s - 1) > 0.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * Math.cos(0.9) + 6, oy - Y0 * Math.sin(0.9) - 8, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, Math.abs(s.s - 1) > 0.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const px = ox + X * 0.7071, py = oy - Y * 0.7071; o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : s.s < 0.98 ? "dot4" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Population change and the PPC", base: { s: 1 }, draw: ppcChart, steps: [
  { cap: "The PPC shows the most the economy can produce with its <b>labour</b>, capital and land.", s: { s: 1 } },
  { cap: "<b>An increase in the labour force</b> (from higher births or immigration) means more can be produced: the PPC shifts <b>outwards</b> to PPC₁. Total output could rise.", s: { s: 1.2 } },
  { cap: "<b>A fall in the population</b> (emigration, a falling birth rate) reduces the labour force: the PPC shifts <b>inwards</b> to PPC₁. The economy can produce less in total.", s: { s: 0.8 } },
  { cap: "<b>Evaluate:</b> total output may fall but output <b>per head</b> may rise if the country was overpopulated. It depends on whether the people leaving are skilled workers.", s: { s: 0.8 } },
] });
function dsChart(s) {
  const d = s.d; let o = axes("Price", "Quantity") + curve(-1, 110, "c1", "D", { t: "t1", attrs: { opacity: d > 1 ? 0.4 : 1 } }) + curve(1, 10, "c3", "S", { t: "t3" });
  if (d > 1) o += curve(-1, 110 + d, "c2", "D₁", { t: "t2" });
  const q0 = 50, p0 = 60, q1 = (100 + d) / 2, p1 = 60 + d / 2;
  o += hline(p0, "gr", q0) + vline(q0, p0) + SV.circle(QX(q0), PY(p0), 6, "dot1", { opacity: d > 1 ? 0.5 : 1 }) + ylab(p0, "P") + xlab(q0, "Q");
  if (d > 1) o += hline(p1, "gr", q1) + vline(q1, p1) + SV.circle(QX(q1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(q1, "Q₁", "sm bd");
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "A bigger population and the market for clothing", base: { d: 0 }, draw: dsChart, steps: [
  { cap: "The market for <b>clothing</b> is in equilibrium at price <b>P</b> and quantity <b>Q</b>.", s: { d: 0 } },
  { cap: "The <b>population increases</b> (more births or immigration). More people want clothes at each price, so <b>demand shifts right</b> to D₁.", s: { d: 24 } },
  { cap: "The new equilibrium has a <b>higher price (P₁)</b> and <b>higher quantity (Q₁)</b>. Firms in the market could earn more revenue and expand. (The same applies to housing, food and toys.)", s: { d: 24 } },
] });
const ACH = ["The share of the population aged 65+ rises", "The dependency ratio rises: fewer workers per pensioner", "Pension and healthcare spending rise; tax revenue grows more slowly", "The government raises taxes, borrows more or cuts other spending", "A smaller labour force may slow growth and productivity", "Evaluation: later retirement, immigration and technology can ease the strain"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Effects of an ageing population", base: { n: 0 }, draw: mkChain(ACH, "--warn"), steps: chainSteps(["The <b>share aged 65+ rises</b>.", "The <b>dependency ratio rises</b>: fewer workers support each pensioner.", "<b>Pension and healthcare spending rise</b>; tax revenue grows more slowly.", "The government <b>raises taxes, borrows more or cuts other spending</b>.", "A smaller labour force may <b>slow growth and productivity</b>.", "<b>Evaluate:</b> later retirement, immigration, higher productivity and automation can ease the strain."]) });

/* Lab 1: optimum population */
function labO() {
  if (!$("#oa") || !$("#ob")) return;
  const L = +$("#oa").value, T = +$("#ob").value / 100, Ls = 40 * T, Ym = 20 * T, f = Math.max(0, Ym * (1 - Math.pow((L - Ls) / (Ls + 20), 2)));
  $("#oa1").textContent = "$" + money(f, 1) + "k"; $("#oa2").textContent = Math.round(Ls) + "m"; $("#oa3").textContent = Math.abs(L - Ls) < 5 ? "Optimum" : L < Ls ? "Under" : "Over";
  $("#oav").textContent = Math.abs(L - Ls) < 5 ? `At ${L}m people, output per head is close to its maximum of $${money(Ym, 1)}k.` : L < Ls ? `With ${L}m people the country is underpopulated: more people would raise output per head towards $${money(Ym, 1)}k at ${Math.round(Ls)}m.` : `With ${L}m people the country is overpopulated: output per head is only $${money(f, 1)}k. Fewer people (or better technology) would help.`;
  $("#labO").innerHTML = optChart({ L, T });
}
Lib.slider($("#g1"), { id: "oa", label: "Population (millions)", min: 10, max: 100, step: 5, value: 20, fmt: (v) => v + "m", onInput: labO });
Lib.slider($("#g2"), { id: "ob", label: "Technology and capital (100 = today)", min: 100, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labO });
/* Lab 2: dependency */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const y = +$("#da").value, o = +$("#db").value, w = 100 - y - o, dep = (y + o) / w, per = w / o;
  $("#da1").textContent = w + "%"; $("#da2").textContent = money(dep, 2); $("#da3").textContent = money(per, 1);
  $("#dav").textContent = `${y}% are children and ${o}% are 65 or over, so ${w}% are of working age. There are ${money(dep, 2)} dependants for each worker, and ${money(per, 1)} workers for each person aged 65+. ${o > 22 ? "A high share of old people means high pension and healthcare costs." : y > 30 ? "A high share of children means high spending on schools, but a large future workforce." : ""}`;
  const base = 290; let g = SV.line(60, base, 700, base);
  [["Aged 0-14", y, "--warn"], ["Working age", w, "--accent"], ["Aged 65+", o, "--bad"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = v * 3.2; g += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = g;
}
Lib.slider($("#g3"), { id: "da", label: "Share of the population aged 0 to 14", min: 10, max: 45, step: 1, value: 20, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "db", label: "Share of the population aged 65 and over", min: 3, max: 35, step: 1, value: 15, fmt: (v) => v + "%", onInput: labD });
const EF = [
  { n: "A rapidly growing population", b: "Bigger labour force and market; more future workers.", c: "Pressure on food, housing and services; more dependants; possible overpopulation and lower output per head." },
  { n: "A falling population", b: "Less pressure on resources and the environment.", c: "Fewer workers and customers; ageing; lower tax revenue and growth." },
  { n: "A young population", b: "Large future workforce; adaptable; lower pension costs.", c: "High dependency now; need schools and jobs." },
  { n: "An ageing population", b: "Experienced workers; demand for healthcare and leisure.", c: "Pensions and healthcare costs; labour shortages; slower growth." },
  { n: "Large-scale immigration", b: "More workers and skills; more tax revenue; younger population.", c: "Pressure on housing and services; wages may fall for some; brain drain from the home country." },
  { n: "Large-scale emigration", b: "Remittances sent home; less unemployment.", c: "Loss of skilled workers; labour shortages; ageing population." },
];
button_table("efBtns", "efOut", EF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible benefits</th><th>Possible costs</th></tr><tr><td>${p.b}</td><td>${p.c}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a possible <b>benefit</b> or <b>cost</b> of a <b>rapidly growing</b> population?", buckets: [{ label: "Benefit" }, { label: "Cost" }], items: [
  { text: "Larger labour force", b: 0 }, { text: "Bigger market for firms", b: 0 }, { text: "More tax revenue", b: 0 }, { text: "Economies of scale", b: 0 },
  { text: "Pressure on food and water", b: 1 }, { text: "More spending on schools and hospitals", b: 1 }, { text: "Unemployment and lower wages", b: 1 }, { text: "Output per head may fall (overpopulation)", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Does each describe <b>underpopulation</b> or <b>overpopulation</b>?", buckets: [{ label: "Underpopulation" }, { label: "Overpopulation" }], items: [
  { text: "Too few workers to use the land and resources", b: 0 }, { text: "More people would raise output per head", b: 0 }, { text: "Unused natural resources", b: 0 }, { text: "Labour shortages", b: 0 },
  { text: "Too many people for the available resources", b: 1 }, { text: "Output per head falls as population rises", b: 1 }, { text: "Overcrowding and pressure on housing", b: 1 }, { text: "Fewer people would raise living standards", b: 1 },
], done: "The optimum maximises output per head." });
Lib.classify($("#cl3"), { prompt: "Is each effect more likely with an <b>ageing</b> or a <b>young</b> population?", buckets: [{ label: "Ageing population" }, { label: "Young population" }], items: [
  { text: "Rising pension and healthcare costs", b: 0 }, { text: "Labour shortages in the future", b: 0 }, { text: "Less spending on durable goods and more on healthcare", b: 0 },
  { text: "Large spending on schools", b: 1 }, { text: "A large future workforce", b: 1 }, { text: "High demand for jobs", b: 1 },
], done: "Both structures have costs and benefits." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Optimum population", "The population that gives the highest output per head"],
  ["Overpopulation", "Too many people for the resources and capital available"],
  ["Underpopulation", "Too few people to use resources fully"],
  ["Dependency ratio", "Dependants (young and old) compared with those of working age"],
  ["Ageing population", "A rising share of the population aged 65 and over"],
  ["Labour force", "People who are employed or looking for work"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an ageing population could slow economic growth</b>.", items: [
  "The share of older people rises",
  "The labour force grows more slowly or shrinks",
  "Fewer workers produce less output",
  "Tax revenue grows slowly and spending on pensions and healthcare rises",
  "Less money is available for investment",
  "Economic growth may slow",
], done: "A full analysis chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A country has 10 million people aged 0-14, 30 million aged 15-64 and 10 million aged 65+. What is the dependency ratio?", a: 0.67, tol: 0.01, sol: "(10 + 10) ÷ 30 = <b>0.67</b>." },
  { q: "GDP is $300bn and the population is 10 million. What is GDP per head ($)?", a: 30000, sol: "$300,000m ÷ 10m = <b>$30,000</b>." },
  { q: "The population rises to 12 million while GDP rises to $330bn. Does GDP per head rise or fall? Give the new GDP per head ($).", a: 27500, sol: "330,000 ÷ 12 = <b>$27,500</b>: GDP per head falls." },
  { q: "There are 4 workers for each person aged 65+. In 20 years there will be 2 workers for each. By what percentage does the ratio fall?", a: 50, sol: "(4 − 2) ÷ 4 × 100 = <b>50%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the optimum population?", opts: ["The largest possible population", "The population that gives the highest output per head", "The population with no unemployment", "The population of working age"], a: 1, why: "It maximises output per head." },
  { q: "Overpopulation is most likely to cause:", opts: ["A rise in output per head", "A fall in output per head", "Labour shortages", "A rise in wages"], a: 1, why: "Too many people for the resources." },
  { q: "An ageing population is most likely to cause:", opts: ["Falling pension costs", "Higher healthcare and pension costs", "A larger labour force", "Lower dependency"], a: 1, why: "More older people need support." },
  { q: "Which could increase the optimum population?", opts: ["New technology and capital", "Depletion of resources", "Pollution", "War"], a: 0, why: "A country can support more people at high income." },
  { q: "A rise in the population is most likely to shift the demand for housing:", opts: ["Left", "Right", "Not at all", "Down"], a: 1, why: "More people want homes." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Optimum population", "The population size that gives the highest output per head."],
  ["Overpopulation", "Too many people for the resources and capital available, so output per head falls."],
  ["Underpopulation", "Too few people to use resources fully."],
  ["Dependency ratio", "The number of dependants (aged 0-14 and 65+) divided by the number of working-age people."],
  ["Ageing population", "A rising share of the population aged 65 and over."],
  ["Young population", "A large share of the population aged under 15."],
  ["Labour force", "People who are employed or looking for work."],
  ["Economies of scale", "Lower average costs from larger output."],
  ["Remittances", "Money sent home by migrants working abroad."],
  ["Brain drain", "The emigration of skilled and educated workers."],
] });
labO(); labD();
