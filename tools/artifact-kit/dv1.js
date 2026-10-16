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

function secChart(s) {
  const cols = [["Primary", "--warn"], ["Secondary", "--n"], ["Tertiary", "--accent"]], data = [["Low-income country", [45, 20, 35]], ["Middle-income country", [15, 35, 50]], ["High-income country", [3, 22, 75]]], base = 300, bw = 130, h = 240;
  let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Share of output by sector (%)", "sm");
  data.forEach(([n, v], i) => {
    const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 210; let y = base, g = `<g opacity="${op}">`;
    v.forEach((p, j) => { const hh = (p / 100) * h; y -= hh; g += SV.rect(x, y, bw, hh, "", { style: `fill:var(${cols[j][1]});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }); if (hh > 16) g += SV.text(x + bw / 2, y + hh / 2 + 5, cols[j][0].slice(0, 3) + ". " + p + "%", "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:13px" }); });
    o += g + SV.text(x + bw / 2, base + 22, n, "sm bd", { "text-anchor": "middle" }) + "</g>";
  });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "The sectors as a country develops", base: { n: 0 }, draw: secChart, steps: [
  { cap: "In a <b>low-income country</b> the <b>primary sector</b> (farming, mining, fishing) is large: here 45% of output. Value added is low, prices are unstable and productivity is low.", s: { n: 1 } },
  { cap: "In a <b>middle-income country</b> industry grows: the <b>secondary sector</b> (manufacturing, construction) expands as workers move out of farming. Incomes rise.", s: { n: 2 } },
  { cap: "In a <b>high-income country</b> the <b>tertiary sector</b> (services) dominates, with 75% of output, and the primary sector is small. Services such as finance, tourism and healthcare add high value. Figures are illustrative.", s: { n: 3 } },
] });
const VIC = ["Low income: little saving or tax revenue", "Little investment in capital, education and healthcare", "Low productivity and a large, low-value primary sector", "Output and income stay low", "Population grows quickly and resources are spread thinly", "The country stays poor: a vicious circle"];
Lib.stepper($("#stV"), { w: 760, h: 400, label: "The vicious circle of low development", base: { n: 0 }, draw: mkChain(VIC, "--bad"), steps: chainSteps(["<b>Low income</b> means little saving and little tax revenue.", "There is <b>little investment</b> in capital, education and healthcare.", "<b>Productivity is low</b> and the economy relies on low-value primary products.", "<b>Output and income stay low</b>.", "Fast <b>population growth</b> spreads resources thinly.", "<b>The country stays poor</b>: a vicious circle. Aid, FDI, better policy and education can break it."]) });
const VIR = ["Higher income allows more saving and tax revenue", "More investment in capital, schools and hospitals", "Workers are more skilled and healthier; capital is better", "Productivity rises and the economy moves to higher-value sectors", "Output and income rise further", "Development continues: a virtuous circle"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "The virtuous circle of development", base: { n: 0 }, draw: mkChain(VIR, "--good"), steps: chainSteps(["<b>Higher income</b> allows more saving and more tax revenue.", "There is <b>more investment</b> in capital, schools and hospitals.", "Workers are <b>more skilled and healthier</b>; capital is better.", "<b>Productivity rises</b> and the economy moves to <b>higher-value sectors</b>.", "<b>Output and income rise</b> further.", "<b>Development continues</b>: a virtuous circle. Evaluate: it needs stability, good institutions and shared gains."]) });

/* Lab 1: country profiles */
const PRO = [
  { n: "Low-income country", inc: 800, prod: 3, pg: 3.0, sec: [45, 20, 35], si: [12, 14], ed: 4, le: 60, res: "Few, or exported unprocessed" },
  { n: "Middle-income country", inc: 6000, prod: 15, pg: 1.2, sec: [15, 35, 50], si: [28, 26], ed: 9, le: 74, res: "Used to build industry" },
  { n: "High-income country", inc: 45000, prod: 60, pg: 0.3, sec: [3, 22, 75], si: [25, 22], ed: 13, le: 82, res: "Imports many, adds high value" },
];
let selP = 1;
function labC() {
  const p = PRO[selP]; $("#cpBtns").innerHTML = PRO.map((q, j) => `<button class="b${j === selP ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#cpBtns .b").forEach((b) => (b.onclick = () => { selP = +b.dataset.j; labC(); }));
  $("#cpOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Income per head</th><th>Output per worker</th><th>Population growth</th><th>Primary / secondary / tertiary</th><th>Saving / investment (% GDP)</th><th>Years of schooling</th><th>Life expectancy</th><th>Natural resources</th></tr><tr><td>$${p.inc.toLocaleString("en-US")}</td><td>$${p.prod}k</td><td>${p.pg}%</td><td>${p.sec.join(" / ")}%</td><td>${p.si[0]}% / ${p.si[1]}%</td><td>${p.ed}</td><td>${p.le}</td><td>${p.res}</td></tr></table></div><p class="note">Illustrative figures to show typical patterns, not data for a particular country.</p>`;
  const mx = Math.max(...PRO.map((q) => q.inc)), base = 250; let o = SV.line(60, base, 700, base) + SV.text(60, 20, "Income per head ($, illustrative)", "sm");
  PRO.forEach((q, j) => { const x = 130 + j * 190, h = (Math.log(q.inc) - Math.log(300)) / (Math.log(mx) - Math.log(300)) * 200 + 8; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${j === selP ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, "$" + q.inc.toLocaleString("en-US"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, q.n.replace(" country", ""), "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
/* Lab 2: development simulator */
function labG() {
  if (!$("#ga") || !$("#gb") || !$("#gc")) return;
  const inv = +$("#ga").value, ed = +$("#gb").value, pg = +$("#gc").value, g = 0.1 * inv + 0.2 * (ed - 2) - pg, start = 2000;
  const v = []; for (let t = 0; t <= 30; t += 5) v.push(start * Math.pow(1 + g / 100, t));
  $("#ga1").textContent = (g >= 0 ? "+" : "") + money(g, 1) + "%"; $("#ga2").textContent = "$" + Math.round(v[6]).toLocaleString("en-US"); $("#ga3").textContent = money(v[6] / start, 1) + " times";
  $("#gav").textContent = `With investment of ${inv}% of GDP, ${ed} years of schooling and population growth of ${pg}%, income per head grows about ${money(g, 1)}% a year, from $2,000 to $${Math.round(v[6]).toLocaleString("en-US")} in 30 years. ${g < 1 ? "Growth in income per head is slow: the country struggles to catch up." : "Faster growth lets the country narrow the gap."} (A simple illustrative model.)`;
  const base = 290, mx = Math.max(...v), k = 220 / mx; let o = SV.line(60, base, 700, base);
  v.forEach((val, i) => { const x = 90 + i * 90, h = Math.max(4, val * k); o += SV.rect(x, base - h, 60, h, "", { style: `fill:var(${g >= 1 ? "--good" : "--warn"})`, opacity: 0.85 }) + SV.text(x + 30, base - h - 8, "$" + Math.round(val / 100) / 10 + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 30, base + 20, i ? "Year " + i * 5 : "Now", "sm", { "text-anchor": "middle" }); });
  $("#labG").innerHTML = o + SV.text(60, 24, "Income per head ($)", "sm");
}
Lib.slider($("#g1"), { id: "ga", label: "Saving and investment (% of GDP)", min: 5, max: 35, step: 1, value: 22, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "gb", label: "Average years of schooling", min: 2, max: 14, step: 1, value: 8, fmt: (v) => v + " years", onInput: labG });
Lib.slider($("#g3"), { id: "gc", label: "Population growth", min: 0, max: 4, step: 0.5, value: 2, fmt: (v) => v + "%", onInput: labG });
const DF = [
  { n: "Income", c: "Low income limits what people can spend on food, education and healthcare, and how much they can save.", e: "Two countries with GDP per head of $800 and $45,000." },
  { n: "Productivity", c: "More capital, better technology and skills raise output per worker and wages.", e: "A modern factory worker compared with a farmer using hand tools." },
  { n: "Population growth", c: "Fast growth increases dependants and pressure on resources, which can lower GDP per head.", e: "Many low-income countries have growth above 2% a year." },
  { n: "Sector sizes", c: "A large primary sector means low value added and unstable incomes; services add more value.", e: "Agriculture is a large share of output in many low-income economies." },
  { n: "Saving and investment", c: "Low saving means little to invest in capital, so growth in capacity is slow.", e: "East Asian economies invested heavily and grew fast." },
  { n: "Education", c: "More schooling raises skills, productivity, wages and job opportunities.", e: "Higher years of schooling in higher-income countries." },
  { n: "Healthcare", c: "Healthier workers lose fewer days to illness and live longer.", e: "Life expectancy of 60 compared with 82." },
  { n: "Natural resources", c: "Resources can raise income, but exporting them raw gives low value added; dependence on one resource is risky.", e: "Oil exporters can still have low HDI." },
];
button_table("dfBtns", "dfOut", DF, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it causes differences in development</th><th>Example</th></tr><tr><td>${p.c}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>sector</b> is each?", buckets: [{ label: "Primary" }, { label: "Secondary" }, { label: "Tertiary" }], items: [
  { text: "Farming", b: 0 }, { text: "Mining", b: 0 }, { text: "Fishing", b: 0 }, { text: "Oil extraction", b: 0 },
  { text: "Car manufacturing", b: 1 }, { text: "Construction", b: 1 }, { text: "Food processing", b: 1 },
  { text: "Banking", b: 2 }, { text: "Tourism", b: 2 }, { text: "Education", b: 2 }, { text: "Retail", b: 2 },
], done: "Primary: extract. Secondary: make. Tertiary: serve." });
Lib.classify($("#cl2"), { prompt: "Is each more typical of a <b>low-income</b> or a <b>high-income</b> country?", buckets: [{ label: "Low-income country" }, { label: "High-income country" }], items: [
  { text: "Large primary sector", b: 0 }, { text: "Low life expectancy", b: 0 }, { text: "High population growth", b: 0 }, { text: "Low saving and investment", b: 0 },
  { text: "Large tertiary sector", b: 1 }, { text: "High average years of schooling", b: 1 }, { text: "High productivity", b: 1 }, { text: "Ageing population", b: 1 },
], done: "Typical patterns, with exceptions." });
Lib.classify($("#cl3"), { prompt: "Is each <b>economic growth</b> or <b>economic development</b>?", buckets: [{ label: "Economic growth" }, { label: "Economic development" }], items: [
  { text: "A rise in real GDP", b: 0 }, { text: "An increase in output over time", b: 0 },
  { text: "A rise in life expectancy and schooling", b: 1 }, { text: "An improvement in the HDI", b: 1 }, { text: "Better living standards and quality of life", b: 1 },
], done: "Growth is about output; development is about living standards." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Economic development", "An improvement in living standards and quality of life"],
  ["Primary sector", "Extracts or grows natural resources"],
  ["Secondary sector", "Manufactures goods and builds"],
  ["Tertiary sector", "Provides services"],
  ["Value added", "The extra value created at each stage of production"],
  ["Foreign direct investment", "Investment in a country by foreign firms"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how low investment keeps a country poor</b>.", items: [
  "Low income means little saving",
  "Little investment in capital, education and healthcare",
  "Low productivity",
  "Low output and income",
  "Little saving again: the cycle repeats",
], done: "The vicious circle of poverty." });
Lib.calc($("#c1"), { qs: [
  { q: "A country's output is $20bn from primary, $30bn from secondary and $50bn from tertiary. What percentage of output is tertiary?", a: 50, sol: "50 ÷ 100 × 100 = <b>50%</b>." },
  { q: "In Jordan 2 million people are in the labour force and 0.3 million work in the secondary sector. What percentage of the labour force is this?", a: 15, sol: "0.3 ÷ 2 × 100 = <b>15%</b>." },
  { q: "GDP is $60bn and the population is 20 million. What is GDP per head ($)?", a: 3000, sol: "60,000m ÷ 20m = <b>$3,000</b>." },
  { q: "A country saves 8% of a GDP of $50bn. How much is saved ($bn)?", a: 4, sol: "8% × 50 = <b>$4bn</b>." },
  { q: "Output per worker is $4,000 in country A and $40,000 in country B. How many times higher is productivity in B?", a: 10, sol: "40,000 ÷ 4,000 = <b>10 times</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is economic development?", opts: ["A rise in real GDP only", "An improvement in living standards and quality of life", "A rise in population", "An increase in exports"], a: 1, why: "It is wider than growth." },
  { q: "Which sector includes farming and mining?", opts: ["Primary", "Secondary", "Tertiary", "Quaternary"], a: 0, why: "Extraction of natural resources." },
  { q: "A large primary sector is most often linked to:", opts: ["High incomes", "Lower incomes and low value added", "High productivity", "A large services sector"], a: 1, why: "Raw materials add little value." },
  { q: "Which is likely to raise development in the long run?", opts: ["Less education", "More investment in capital and education", "Higher population growth only", "Fewer hospitals"], a: 1, why: "Higher productivity and quality of labour." },
  { q: "A vicious circle of poverty means:", opts: ["Low income leads to low investment and so low income", "High income leads to high investment", "Prices fall", "Exports rise"], a: 0, why: "Poverty reinforces itself." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Economic development", "An improvement in the standard of living and quality of life of the people of a country."],
  ["Economic growth", "A rise in real GDP over time."],
  ["Primary sector", "The sector that extracts or grows natural resources, such as farming, mining and fishing."],
  ["Secondary sector", "The sector that manufactures goods and builds, such as car making and construction."],
  ["Tertiary sector", "The sector that provides services, such as banking, tourism and education."],
  ["Value added", "The extra value created at each stage of production."],
  ["Productivity", "Output per worker."],
  ["Saving", "Income not spent now."],
  ["Investment", "Spending on capital goods such as machinery and buildings."],
  ["Foreign direct investment (FDI)", "Investment in a country by foreign firms, such as multinationals."],
  ["Vicious circle of poverty", "A cycle in which low income leads to low saving and investment, keeping income low."],
  ["Natural resources", "Raw materials found in nature, such as oil, minerals and fertile land."],
] });
labC(); labG();
