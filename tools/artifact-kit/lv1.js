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

function gdpChart(s) {
  const base = 330, k = 0.36; let o = SV.line(60, base, 710, base);
  const bars = [["Real GDP ($bn)", s.g, "--accent", 1, "$"], ["Population (m)", s.p, "--warn", 1, ""], ["Real GDP per head ($)", (s.g * 1000) / s.p, "--good", s.o, "$"]];
  bars.forEach(([n, v, c, op, pre], i) => { if (op <= 0.02) return; const sc = i === 2 ? 0.0028 : i === 0 ? 0.4 : 4; const x = 110 + i * 200, h = v * sc; o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, pre + Math.round(v).toLocaleString("en-US"), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Real GDP per head", base: { g: 600, p: 20, o: 0, t: "" }, draw: gdpChart, steps: [
  { cap: "A country has <b>real GDP of $600bn</b> and a <b>population of 20 million</b>.", s: { g: 600, p: 20, o: 0, t: "" } },
  { cap: "<b>Real GDP per head</b> = $600bn ÷ 20 million = <b>$30,000</b>. This is the average income per person.", s: { g: 600, p: 20, o: 1, t: "$30,000 per person" } },
  { cap: "Real GDP grows 4% to <b>$624bn</b>, but population grows 6% to <b>21.2 million</b>. Output rose, but real GDP per head <b>falls</b> to about <b>$29,400</b>: the average person is a little worse off.", s: { g: 624, p: 21.2, o: 1, t: "Output up, but per head down" } },
] });
function hdiChart(s) {
  const base = 320, k = 240; let o = SV.line(60, base, 710, base) + SV.line(60, base, 60, 60) + SV.text(66, 60, "Index (0 to 1)", "sm");
  const bars = [["Health", 0.85, "--good", s.a], ["Education", 0.70, "--n", s.b], ["Income", 0.75, "--warn", s.c]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0.02) return; const x = 100 + i * 140, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  const hdi = Math.cbrt(0.85 * 0.7 * 0.75);
  if (s.d > 0.02) { const h = hdi * k; o += `<g opacity="${s.d}">` + SV.rect(540, base - h, 130, h, "", { style: "fill:var(--accent)", opacity: 0.9 }) + SV.text(605, base - h - 8, "HDI " + money(hdi, 2), "lbl bd t3", { "text-anchor": "middle" }) + SV.text(605, base + 20, "Combined", "sm", { "text-anchor": "middle" }) + "</g>"; }
  return o;
}
Lib.stepper($("#stH"), { w: 760, h: 400, label: "How the HDI is built", base: { a: 0, b: 0, c: 0, d: 0 }, draw: hdiChart, steps: [
  { cap: "<b>Health:</b> life expectancy at birth is turned into an index from 0 to 1. Here the country scores <b>0.85</b>.", s: { a: 1, b: 0, c: 0, d: 0 } },
  { cap: "<b>Education:</b> mean and expected years of schooling give an index of <b>0.70</b>.", s: { a: 1, b: 1, c: 0, d: 0 } },
  { cap: "<b>Income:</b> GNI per head (adjusted for price differences) gives an index of <b>0.75</b>.", s: { a: 1, b: 1, c: 1, d: 0 } },
  { cap: "The three are combined into one <b>HDI of about 0.76</b>: <b>high</b> human development. A country can raise its HDI by improving health or education, even if income is unchanged.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
function twoChart(s) {
  const base = 320, k = 0.0085; let o = SV.line(60, base, 710, base);
  const c = [["Country A", 20000, 0.8], ["Country B", 20000, 0.7]];
  c.forEach(([n, g, h], i) => { const x = 130 + i * 300, op = i === 0 ? 1 : s.b; if (op <= 0.02) return; o += `<g opacity="${op}">` + SV.rect(x, base - g * k * 0.9, 90, g * k * 0.9, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 45, base - g * k * 0.9 - 8, "$20,000", "lbl bd", { "text-anchor": "middle" }) + SV.rect(x + 100, base - h * 200, 90, h * 200, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 145, base - h * 200 - 8, "HDI " + h.toFixed(2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 95, base + 22, n, "lbl bd", { "text-anchor": "middle" }) + "</g>"; });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 400, label: "Why add health and education to income?", base: { b: 0, t: "" }, draw: twoChart, steps: [
  { cap: "<b>Country A</b> has GDP per head of $20,000 and an HDI of <b>0.80</b>: people are healthy and well educated.", s: { b: 0, t: "" } },
  { cap: "<b>Country B</b> has the <b>same GDP per head</b> but an HDI of only <b>0.70</b>.", s: { b: 1, t: "Same income, different HDI" } },
  { cap: "B's income is spent differently: lower life expectancy and fewer years of schooling. <b>GDP per head alone would hide this</b>. That is the advantage of the HDI.", s: { b: 1, t: "GDP per head hides the difference" } },
] });

/* Lab 1: HDI calculator */
function labH() {
  if (!$("#ha") || !$("#hb") || !$("#hc") || !$("#hd")) return;
  const le = +$("#ha").value, my = +$("#hb").value, ey = +$("#hc").value, gni = +$("#hd").value;
  const I = (v, a, b) => clamp((v - a) / (b - a), 0, 1), li = I(le, 20, 85), ei = (I(my, 0, 15) + I(ey, 0, 18)) / 2, ii = clamp((Math.log(gni) - Math.log(100)) / (Math.log(75000) - Math.log(100)), 0, 1), hdi = Math.cbrt(li * ei * ii);
  $("#ha1").textContent = money(li, 2); $("#ha2").textContent = money(ei, 2); $("#ha3").textContent = money(ii, 2); $("#ha4").textContent = money(hdi, 3);
  const cat = hdi >= 0.8 ? "very high" : hdi >= 0.7 ? "high" : hdi >= 0.55 ? "medium" : "low";
  $("#hav").textContent = `HDI = about ${money(hdi, 3)}: ${cat} human development. Try raising life expectancy or schooling while keeping income fixed: HDI rises. Income is on a log scale, so doubling a low income helps the HDI much more than doubling a high one.`;
  const base = 300; let o = SV.line(60, base, 700, base);
  [["Health", li, "--good"], ["Education", ei, "--n"], ["Income", ii, "--warn"], ["HDI", hdi, "--accent"]].forEach(([n, v, c], i) => { const x = 100 + i * 150, h = v * 240; o += SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 2), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labH").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ha", label: "Life expectancy at birth", min: 40, max: 85, step: 1, value: 72, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g2"), { id: "hb", label: "Mean years of schooling (adults)", min: 1, max: 15, step: 0.5, value: 9, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g3"), { id: "hc", label: "Expected years of schooling (children)", min: 4, max: 18, step: 0.5, value: 13, fmt: (v) => v + " years", onInput: labH });
Lib.slider($("#g4"), { id: "hd", label: "GNI per head ($, adjusted)", min: 500, max: 75000, step: 500, value: 15000, fmt: (v) => "$" + v.toLocaleString("en-US"), onInput: labH });
/* Lab 2: scatter */
const CT = [["Niger", 600, 61, 0.39], ["Ethiopia", 1000, 66, 0.49], ["Nigeria", 2200, 53, 0.54], ["India", 2500, 68, 0.64], ["Eswatini", 4000, 58, 0.61], ["Vietnam", 4000, 74, 0.73], ["Brazil", 8700, 73, 0.76], ["China", 12600, 78, 0.78], ["Japan", 34000, 85, 0.92], ["United Kingdom", 46000, 81, 0.93], ["Singapore", 80000, 83, 0.94]];
let selC = 8;
function labS() {
  const X = (g) => 70 + ((Math.log(g) - Math.log(400)) / (Math.log(100000) - Math.log(400))) * 600, Y = (v) => 300 - ((v - 45) / (90 - 45)) * 250;
  let o = SV.line(70, 300, 690, 300) + SV.line(70, 300, 70, 40) + SV.text(690, 330, "GDP per head (log scale)", "sm", { "text-anchor": "end" }) + SV.text(76, 44, "Life expectancy (years)", "sm");
  [50, 60, 70, 80, 90].forEach((v) => (o += SV.line(70, Y(v), 690, Y(v), "gr") + SV.text(62, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  CT.forEach(([n, g, l], i) => { o += SV.circle(X(g), Y(l), i === selC ? 9 : 6, i === selC ? "dot2" : "dot1", { opacity: i === selC ? 1 : 0.7 }); if (i === selC) o += SV.text(X(g) + 12, Y(l) - 8, n, "lbl bd t2", { style: halo }); });
  $("#labS").innerHTML = o;
  const c = CT[selC];
  $("#hsBtns").innerHTML = CT.map((q, j) => `<button class="b${j === selC ? " pri" : ""}" data-j="${j}">${q[0]}</button>`).join("");
  $$("#hsBtns .b").forEach((b) => (b.onclick = () => { selC = +b.dataset.j; labS(); }));
  $("#hsOut").innerHTML = `<div class="tw"><table class="t"><tr><th>GDP per head</th><th>Life expectancy</th><th>HDI</th></tr><tr><td>$${c[1].toLocaleString("en-US")}</td><td>${c[2]} years</td><td>${c[3].toFixed(2)}</td></tr></table></div>`;
}
const IND = [
  { n: "Real GDP per head", m: "Average income per person, adjusted for inflation.", s: "Simple, regular, comparable over time and countries.", w: "Average hides inequality; misses informal economy, health, education, environment." },
  { n: "HDI", m: "Combines health, education and income into one index.", s: "Broader than income; easy to compare.", w: "Hides inequality; leaves out environment, freedom and quality." },
  { n: "Life expectancy", m: "Average years a newborn can expect to live.", s: "Reflects health, nutrition and sanitation.", w: "An average; says little about quality of life." },
  { n: "Literacy rate", m: "Share of adults who can read and write.", s: "Simple measure of education.", w: "Says nothing about quality of education." },
  { n: "Infant mortality", m: "Deaths of babies per 1,000 births.", s: "Sensitive to healthcare, nutrition and poverty.", w: "Only one aspect of health." },
  { n: "Access to clean water", m: "Share of people with safe drinking water.", s: "Basic need linked to health.", w: "Ignores quantity and other needs." },
];
button_table("inBtns", "inOut", IND, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it measures</th><th>Strength</th><th>Weakness</th></tr><tr><td>${p.m}</td><td>${p.s}</td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>HDI component</b> does each measure belong to?", buckets: [{ label: "Health" }, { label: "Education" }, { label: "Income" }], items: [
  { text: "Life expectancy at birth", b: 0 }, { text: "Mean years of schooling", b: 1 }, { text: "Expected years of schooling", b: 1 },
  { text: "Gross national income per head", b: 2 }, { text: "Average income, adjusted for price differences", b: 2 }, { text: "How long people can expect to live", b: 0 },
], done: "Three components: health, education, income." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>disadvantage of GDP per head</b>, a <b>disadvantage of HDI</b> or <b>both</b>?", buckets: [{ label: "GDP per head only" }, { label: "HDI only" }, { label: "Both" }], items: [
  { text: "Does not measure health or education", b: 0 }, { text: "Counts harmful output such as pollution clean-up", b: 0 },
  { text: "Education measure ignores quality of schooling", b: 1 }, { text: "Equal weighting of three parts may be arbitrary", b: 1 },
  { text: "Hides income inequality", b: 2 }, { text: "Ignores the environment", b: 2 }, { text: "Leaves out freedom and crime", b: 2 },
], done: "Both hide inequality and the environment; HDI at least covers health and education." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Living standards", "The quality and quantity of goods and services people can obtain"],
  ["Real GDP per head", "Real GDP divided by population"],
  ["Human Development Index", "A composite index of health, education and income between 0 and 1"],
  ["Life expectancy", "The average number of years a newborn is expected to live"],
  ["Composite index", "An index that combines several measures into one number"],
  ["Informal economy", "Activity that is not regulated, recorded or taxed"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP is $800bn and the population is 20 million. Calculate real GDP per head ($).", a: 40000, hint: "$800bn = 800,000m.", sol: "$800bn ÷ 20m = <b>$40,000</b>." },
  { q: "Real GDP rises 3% a year and population rises 1% a year. Roughly, what is the growth of real GDP per head (%)?", a: 2, sol: "3 − 1 = <b>about 2%</b>." },
  { q: "An HDI is 0.64 in Year 1 and 0.70 in Year 5. By how much has it risen?", a: 0.06, tol: 0.001, sol: "0.70 − 0.64 = <b>0.06</b>." },
  { q: "A country's life expectancy index is 0.8, education index 0.6 and income index 0.5. What is the average of the three (to 2 d.p.)? (The HDI uses a similar but slightly different method.)", a: 0.63, tol: 0.01, sol: "(0.8 + 0.6 + 0.5) ÷ 3 = <b>0.63</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does real GDP per head show?", opts: ["Total output", "Average income per person, adjusted for inflation", "Population growth", "Unemployment"], a: 1, why: "Real GDP divided by population." },
  { q: "Which is a component of the HDI?", opts: ["Inflation", "Life expectancy", "Unemployment", "The exchange rate"], a: 1, why: "Health, education and income." },
  { q: "Which is a limitation of real GDP per head?", opts: ["It is adjusted for inflation", "It hides inequality", "It is divided by population", "It is easy to compare"], a: 1, why: "It is an average." },
  { q: "A country has a falling GDP per head but a rising HDI. This could be because:", opts: ["Education and healthcare are improving", "Income is rising fast", "The HDI ignores education", "Population is falling"], a: 0, why: "Health and education offset falling income." },
  { q: "Which statement about the HDI is correct?", opts: ["It only measures income", "It is a value between 0 and 1", "It includes the environment", "It includes unemployment"], a: 1, why: "A composite index from 0 to 1." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Living standards", "The quality and quantity of goods and services people can obtain."],
  ["Real GDP per head", "Real GDP divided by population: the average income per person adjusted for inflation."],
  ["Human Development Index (HDI)", "A composite index of life expectancy, years of schooling and income per head, between 0 and 1."],
  ["Composite index", "An index that combines several measures into one value."],
  ["Life expectancy", "The average number of years a newborn is expected to live."],
  ["Mean years of schooling", "The average number of years of education adults have completed."],
  ["Expected years of schooling", "The number of years of schooling a child entering school can expect to receive."],
  ["GNI per head", "Gross national income divided by population."],
  ["Informal economy", "Activity that is not regulated, recorded or taxed."],
  ["Infant mortality", "The number of deaths of babies under one year per 1,000 live births."],
] });
labH(); labS();
