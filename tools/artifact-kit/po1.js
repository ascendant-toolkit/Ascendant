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

const BASE = [1, 2, 3, 5, 7, 9, 12, 15, 20, 26];
function lineChart(s) {
  const base = 320, k = 6, inc = BASE.map((b) => b * s.g), sorted = inc.slice().sort((a, b) => a - b), med = (sorted[4] + sorted[5]) / 2, rel = 0.5 * med, abs = 3;
  let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Income per person ($ a day) in ten households", "sm");
  inc.forEach((v, i) => { const x = 80 + i * 62, h = Math.min(v * k, 215), a = v < abs, r = v < rel; o += SV.rect(x, base - h, 44, h, "", { style: `fill:var(${a ? "--bad" : r ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(x + 22, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:11px" }); });
  const ya = base - abs * k, yr = base - rel * k;
  o += SV.line(60, ya, 710, ya, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.line(70, 78, 100, 78, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.text(106, 82, "Absolute poverty line: $3 a day", "sm bd");
  if (s.r > 0.02) o += `<g opacity="${s.r}">` + SV.line(60, yr, 710, yr, "dash", { style: "stroke:var(--warn);stroke-width:2.5" }) + SV.line(70, 98, 100, 98, "dash", { style: "stroke:var(--warn);stroke-width:2.5" }) + SV.text(106, 102, "Relative poverty line: 50% of median = $" + money(rel, 1), "sm bd") + "</g>";
  const na = inc.filter((v) => v < abs).length, nr = inc.filter((v) => v < rel).length;
  o += SV.text(380, 52, "In absolute poverty: " + na + " of 10" + (s.r > 0.5 ? " · In relative poverty: " + nr + " of 10" : ""), "lbl bd t2", { "text-anchor": "middle", style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 400, label: "Absolute and relative poverty lines", base: { g: 1, r: 0 }, draw: lineChart, steps: [
  { cap: "Ten households. The <b>absolute poverty line</b> is $3 a day: income needed for basic necessities. <b>Two</b> households (red) fall below it.", s: { g: 1, r: 0 } },
  { cap: "The <b>relative poverty line</b> is 50% of the <b>median</b> income, here $4 a day. <b>Three</b> households are below it: relative poverty includes people who can afford basics but not a normal life.", s: { g: 1, r: 1 } },
  { cap: "The economy grows and <b>everyone's income doubles</b>. Absolute poverty falls to <b>one</b> household, but the relative line doubles too (the median rose), so <b>three households are still in relative poverty</b>.", s: { g: 2, r: 1 } },
  { cap: "If income triples, <b>no one</b> is in absolute poverty. But the poorest are still far below the median: <b>relative poverty remains</b> unless inequality falls.", s: { g: 3, r: 1 } },
] });
function twoChart(s) {
  const base = 320, k = 4.6; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Share of the population in poverty (%)", "sm");
  [["Low-income country", [45, 55], "Low-income"], ["High-income country", [1, 15], "High-income"]].forEach(([n, v], i) => { const x = 130 + i * 300; o += `<g opacity="${i === 0 ? 1 : s.b}">` + SV.rect(x, base - v[0] * k, 80, v[0] * k, "", { style: "fill:var(--bad)", opacity: 0.85 }) + SV.text(x + 40, base - v[0] * k - 8, v[0] + "%", "lbl bd", { "text-anchor": "middle" }) + SV.rect(x + 90, base - v[1] * k, 80, v[1] * k, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 130, base - v[1] * k - 8, v[1] + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 85, base + 22, n, "lbl bd", { "text-anchor": "middle" }) + "</g>"; });
  o += SV.rect(520, 50, 14, 14, "", { style: "fill:var(--bad)" }) + SV.text(540, 62, "Absolute", "sm") + SV.rect(520, 72, 14, 14, "", { style: "fill:var(--warn)" }) + SV.text(540, 84, "Relative", "sm");
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Two types of poverty in two countries", base: { b: 0 }, draw: twoChart, steps: [
  { cap: "In a <b>low-income country</b> a large share of people (illustrative 45%) are in <b>absolute poverty</b>, and an even larger share (55%) in relative poverty.", s: { b: 0 } },
  { cap: "In a <b>high-income country</b> almost nobody is in absolute poverty (1%), but <b>15%</b> are still in <b>relative poverty</b>: their income is far below the average.", s: { b: 1 } },
  { cap: "Absolute poverty is mainly a problem of <b>low-income countries</b>; relative poverty <b>exists in every country</b>. Figures here are illustrative.", s: { b: 1 } },
] });

/* Lab 1 */
function labL() {
  if (!$("#la") || !$("#lb") || !$("#lc") || !$("#ld")) return;
  const g = +$("#la").value, u = +$("#lb").value / 100, abs = +$("#lc").value, pct = +$("#ld").value / 100;
  const inc = BASE.map((b) => (10 * (1 - u) + b * u) * g), sorted = inc.slice().sort((a, b) => a - b), med = (sorted[4] + sorted[5]) / 2, rel = pct * med;
  const na = inc.filter((v) => v < abs).length, nr = inc.filter((v) => v < rel).length;
  $("#la1").textContent = na + " of 10"; $("#la2").textContent = nr + " of 10"; $("#la3").textContent = "$" + money(med, 1);
  $("#lav").textContent = `With the absolute line at $${abs}, ${na} household${na === 1 ? " is" : "s are"} in absolute poverty. The relative line is ${Math.round(pct * 100)}% of the median ($${money(med, 1)}) = $${money(rel, 1)}, so ${nr} ${nr === 1 ? "is" : "are"} in relative poverty. ${g > 1 && nr > 0 ? "Growth raised everyone's income, but the relative line rose too." : ""} ${u === 0 ? "With no inequality, nobody falls below 50% of the median." : ""}`;
  const base = 290, k = 5; let o = SV.line(60, base, 710, base);
  inc.forEach((v, i) => { const x = 80 + i * 62, h = Math.min(v * k, 250), a = v < abs, r = v < rel; o += SV.rect(x, base - h, 44, h, "", { style: `fill:var(${a ? "--bad" : r ? "--warn" : "--accent"})`, opacity: 0.85 }) + SV.text(x + 22, base - h - 6, money(v, 0), "sm bd", { "text-anchor": "middle", style: "font-size:11px" }); });
  o += SV.line(60, base - abs * k, 710, base - abs * k, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.line(60, base - rel * k, 710, base - rel * k, "dash", { style: "stroke:var(--warn);stroke-width:2.5" });
  $("#labL").innerHTML = o + SV.text(60, 24, "Daily income per person: red = absolute poverty, amber = relative only", "sm");
}
Lib.slider($("#g1"), { id: "la", label: "Economic growth (multiplies everyone's income)", min: 1, max: 4, step: 0.25, value: 1, fmt: (v) => "×" + v, onInput: labL });
Lib.slider($("#g2"), { id: "lb", label: "Inequality (0 = everyone equal, 100 = unequal)", min: 0, max: 100, step: 10, value: 100, fmt: (v) => v + "%", onInput: labL });
Lib.slider($("#g3"), { id: "lc", label: "Absolute poverty line ($ a day)", min: 1, max: 8, step: 0.5, value: 3, fmt: (v) => "$" + v, onInput: labL });
Lib.slider($("#g4"), { id: "ld", label: "Relative poverty line (% of median income)", min: 30, max: 70, step: 5, value: 50, fmt: (v) => v + "%", onInput: labL });
const CASES = [
  { n: "A family cannot afford enough food or safe water", a: "Absolute poverty", w: "Basic necessities are out of reach." },
  { n: "A family eats well but cannot afford a computer or school trips that most children have", a: "Relative poverty", w: "Income is too low to take part in normal social life." },
  { n: "Income is below the World Bank's international poverty line", a: "Absolute poverty", w: "A fixed line based on basic needs." },
  { n: "Income is below 60% of the country's median income", a: "Relative poverty", w: "Measured against the rest of society." },
  { n: "A homeless person in a rich country", a: "Absolute poverty", w: "Cannot afford shelter, a basic necessity, even in a rich country." },
  { n: "Real incomes double, but the gap between rich and poor widens", a: "Absolute poverty falls; relative poverty may not", w: "The relative line moves up with the median." },
];
button_table("csBtns", "csOut", CASES, 0, (p) => `<div class="tw"><table class="t"><tr><th>Which type?</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>absolute</b> or <b>relative</b> poverty?", buckets: [{ label: "Absolute poverty" }, { label: "Relative poverty" }], items: [
  { text: "Cannot afford enough food", b: 0 }, { text: "No access to clean water or shelter", b: 0 }, { text: "Income below the World Bank international poverty line", b: 0 }, { text: "A refugee with no home or income", b: 0 },
  { text: "Income below half of the average", b: 1 }, { text: "Cannot afford what most people in society take for granted", b: 1 }, { text: "Exists even in rich countries with high average income", b: 1 }, { text: "Depends on the gap between rich and poor", b: 1 },
], done: "Absolute: fixed line, basic needs. Relative: compared with others." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Absolute poverty", "Being unable to afford the basic necessities of life"],
  ["Relative poverty", "Having income too low to take part in the normal life of society"],
  ["Poverty line", "The income level below which people are counted as poor"],
  ["Poverty rate", "The percentage of the population below the poverty line"],
  ["Median income", "The middle income when everyone is ranked from lowest to highest"],
  ["Basic necessities", "Food, clean water, shelter, clothing and healthcare"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "Guyana has a population of 0.8 million and 12% live in poverty. How many people live in poverty (thousands)?", a: 96, hint: "800,000 × 0.12.", sol: "12% × 800,000 = <b>96,000</b>, so 96 thousand." },
  { q: "A country has 40 million people and 6 million live below the poverty line. What is the poverty rate (%)?", a: 15, sol: "6 ÷ 40 × 100 = <b>15%</b>." },
  { q: "The median income is $30 a day. The relative poverty line is 60% of the median. What is the line ($)?", a: 18, sol: "0.6 × 30 = <b>$18</b>." },
  { q: "The poverty rate falls from 20% to 15% in a population of 60 million. How many fewer people are in poverty (millions)?", a: 3, sol: "5% × 60m = <b>3 million</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is absolute poverty?", opts: ["Having less than the average income", "Being unable to afford basic necessities", "Having less than others in society", "Being unemployed"], a: 1, why: "It is about basic needs." },
  { q: "Which statement about relative poverty is correct?", opts: ["It only exists in poor countries", "It is measured against the incomes of others in a country", "It is a fixed income level", "It disappears when growth occurs"], a: 1, why: "It depends on how much others earn." },
  { q: "Economic growth is most likely to reduce:", opts: ["Absolute poverty, if the poor gain", "Relative poverty in all cases", "Inequality in all cases", "Population"], a: 0, why: "Higher incomes lift people over a fixed line." },
  { q: "Relative poverty can rise even when all incomes rise if:", opts: ["Everyone's income rises equally", "The rich gain more than the poor", "Prices fall", "The poor gain more than the rich"], a: 1, why: "The gap widens." },
  { q: "Who is most likely to be in absolute poverty in a rich country?", opts: ["A homeless person", "A student with a part-time job", "A middle manager", "A retired professor"], a: 0, why: "Cannot afford shelter." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Absolute poverty", "Being unable to afford the basic necessities of life."],
  ["Relative poverty", "Having an income too low to take part in the normal activities of society."],
  ["Poverty line", "The income level below which a person is counted as poor."],
  ["Poverty rate", "The percentage of the population living below the poverty line."],
  ["Median income", "The middle income when all incomes are ranked from lowest to highest."],
  ["Basic necessities", "The things people need to live: food, water, shelter, clothing and healthcare."],
  ["International poverty line", "A standard income level, set by the World Bank, for measuring absolute poverty across countries."],
  ["Inequality", "An uneven distribution of income or wealth."],
  ["Poverty trap", "A cycle where low income keeps people poor."],
] });
labL(); 
