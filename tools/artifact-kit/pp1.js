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

function natChart(s) {
  const x0 = 330, k = 16; let o = "";
  const row = (i, label, v, c, op) => { const y = 40 + i * 62, w = Math.abs(v) * k; return `<g opacity="${op}">` + SV.text(24, y + 24, label, "lbl bd", { "text-anchor": "start" }) + SV.rect(v >= 0 ? x0 : x0 + v * k, y, w, 38, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(v >= 0 ? x0 + w + 8 : x0 + v * k - 8, y + 25, (v >= 0 ? "" : "−") + Math.abs(v), "lbl bd", { "text-anchor": v >= 0 ? "start" : "end" }) + "</g>"; };
  o += SV.line(x0, 30, x0, 300);
  o += row(0, "Births per 1,000", 20, "--good", clamp(s.n, 0, 1)) + row(1, "Deaths per 1,000", -8, "--bad", clamp(s.n - 1, 0, 1)) + row(2, "Natural increase", 12, "--accent", clamp(s.n - 2, 0, 1)) + row(3, "Net migration", 2, "--warn", clamp(s.n - 3, 0, 1));
  o += `<g opacity="${clamp(s.n - 4, 0, 1)}">` + SV.text(380, 340, "Population change = 12 + 2 = 14 per 1,000 = 1.4% a year", "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" }) + "</g>";
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 380, label: "Natural increase and net migration", base: { n: 0 }, draw: natChart, steps: [
  { cap: "The <b>birth rate</b> is 20 live births per 1,000 people a year.", s: { n: 1 } },
  { cap: "The <b>death rate</b> is 8 deaths per 1,000 people a year.", s: { n: 2 } },
  { cap: "<b>Natural increase</b> = births − deaths = 20 − 8 = <b>12 per 1,000</b> (1.2%).", s: { n: 3 } },
  { cap: "<b>Net migration</b> = immigrants − emigrants = <b>+2 per 1,000</b>: more people moved in than left.", s: { n: 4 } },
  { cap: "The population grows by <b>14 per 1,000</b>, or <b>1.4%</b> a year. A negative figure for either part could make the population fall.", s: { n: 5 } },
] });
const dth = (t) => (t < 12 ? 36 : t < 45 ? 36 - 27 * (0.5 - 0.5 * Math.cos(((t - 12) / 33) * Math.PI)) : 9);
const brt = (t) => (t < 30 ? 38 : t < 85 ? 38 - 27 * (0.5 - 0.5 * Math.cos(((t - 30) / 55) * Math.PI)) : 11);
function dtmChart(s) {
  const X = (t) => 80 + t * 6.2, Y = (v) => 330 - v * 7; let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 34, "Rate per 1,000", "sm") + SV.text(710, 362, "Time as a country develops", "sm", { "text-anchor": "end" });
  const pts = [], pb = [], pd = []; for (let t = 0; t <= s.t; t += 1) { pb.push([X(t), Y(brt(t))]); pd.push([X(t), Y(dth(t))]); }
  if (pb.length > 1) { o += SV.poly(pb.concat(pd.slice().reverse()), "f1", { style: "fill:var(--accent);fill-opacity:0.18" }); o += SV.path(ptsPath(pb), "c2", { "stroke-width": 3 }) + SV.path(ptsPath(pd), "c4", { "stroke-width": 3 }); }
  if (pb.length > 1) o += SV.text(X(s.t) - 14, Y(brt(s.t)) - 18, "Birth rate", "lbl bd t2", { "text-anchor": "end" }) + SV.text(X(s.t) - 4, Y(dth(s.t)) + 20, "Death rate", "lbl bd t4", { "text-anchor": "end" });
  if (s.lbl) o += SV.text(X(s.t), 80, s.lbl, "lbl bd t3", { "text-anchor": s.t > 80 ? "end" : "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 400, label: "How birth and death rates change as a country develops", base: { t: 0, lbl: "" }, draw: dtmChart, steps: [
  { cap: "<b>Stage 1:</b> both rates are high. Many babies are born but many die (poor healthcare and food). The population grows slowly.", s: { t: 10, lbl: "Stage 1" } },
  { cap: "<b>Stage 2:</b> better healthcare, food and sanitation make the <b>death rate fall</b> quickly, but the birth rate stays high: <b>fast population growth</b> (the shaded gap).", s: { t: 32, lbl: "Stage 2" } },
  { cap: "<b>Stage 3:</b> as incomes and education rise, women have jobs, contraception is used and fewer babies die: the <b>birth rate falls</b>. The gap narrows.", s: { t: 65, lbl: "Stage 3" } },
  { cap: "<b>Stage 4:</b> both rates are low. Population growth is slow, and the population ages. Some countries now have birth rates below death rates. This is a simplified model: real countries vary.", s: { t: 100, lbl: "Stage 4" } },
] });
const AGE = ["Healthcare and nutrition improve: the death rate falls", "People live longer: life expectancy rises", "Meanwhile the birth rate falls (costs, careers, contraception)", "Fewer young people and more old people", "The share of the population aged 65+ rises: an ageing population"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Why populations age", base: { n: 0 }, draw: mkChain(AGE, "--warn"), steps: chainSteps(["<b>Healthcare and nutrition improve</b>: the death rate falls.", "<b>Life expectancy rises</b>: people live longer.", "Meanwhile the <b>birth rate falls</b>: fewer babies are born.", "There are <b>fewer young</b> and <b>more old</b> people.", "<b>An ageing population:</b> the share aged 65+ rises. Emigration of the young can add to this."]) });

/* Lab 1: population calculator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc") || !$("#pd") || !$("#pe")) return;
  const P0 = +$("#pa").value, b = +$("#pb").value, d = +$("#pc").value, im = +$("#pd").value, em = +$("#pe").value, nat = b - d, net = im - em, g = (nat + net) / 10;
  $("#pa1").textContent = (nat >= 0 ? "+" : "") + nat + " per 1,000"; $("#pa2").textContent = (net >= 0 ? "+" : "") + net + " per 1,000"; $("#pa3").textContent = (g >= 0 ? "+" : "") + money(g, 1) + "%";
  const pop = [P0]; for (let i = 1; i <= 6; i++) pop.push(pop[i - 1] * Math.pow(1 + g / 100, 5));
  $("#pav").textContent = `Natural increase = ${b} − ${d} = ${nat} per 1,000. Net migration = ${im} − ${em} = ${net}. Total change = ${nat + net} per 1,000 = ${money(g, 1)}% a year, so the population goes from ${P0}m to about ${money(pop[6], 1)}m in 30 years. ${g < 0 ? "The population is falling." : ""}`;
  const base = 290, mx = Math.max(...pop), mn = Math.min(...pop), lo = Math.min(P0 * 0.5, mn * 0.9), k = 230 / Math.max(1, mx - lo); let o = SV.line(60, base, 700, base);
  pop.forEach((v, i) => { const x = 90 + i * 90, h = (v - lo) * k + 10; o += SV.rect(x, base - h, 60, h, "", { style: `fill:var(${g >= 0 ? "--accent" : "--bad"})`, opacity: 0.85 }) + SV.text(x + 30, base - h - 8, money(v, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 30, base + 20, i ? "Year " + i * 5 : "Now", "sm", { "text-anchor": "middle" }); });
  $("#labP").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Population today (millions)", min: 10, max: 100, step: 5, value: 50, fmt: (v) => v + "m", onInput: labP });
Lib.slider($("#g2"), { id: "pb", label: "Birth rate (per 1,000)", min: 8, max: 45, step: 1, value: 20, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "pc", label: "Death rate (per 1,000)", min: 4, max: 25, step: 1, value: 8, fmt: (v) => v, onInput: labP });
Lib.slider($("#g4"), { id: "pd", label: "Immigration (per 1,000)", min: 0, max: 15, step: 1, value: 3, fmt: (v) => v, onInput: labP });
Lib.slider($("#g5"), { id: "pe", label: "Emigration (per 1,000)", min: 0, max: 15, step: 1, value: 1, fmt: (v) => v, onInput: labP });
/* Lab 2: age structure */
let selA = "young";
function labA() {
  const t = PYR[selA]; $("#paBtns").innerHTML = Object.keys(PYR).map((k) => `<button class="b${k === selA ? " pri" : ""}" data-k="${k}">${PYR[k].n}</button>`).join("");
  $$("#paBtns .b").forEach((b) => (b.onclick = () => { selA = b.dataset.k; labA(); }));
  const y = t.b[0], o = t.b[4], w = 100 - y - o, dep = (y + o) / w;
  $("#paOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Aged 0-14</th><th>Working age (15-64)</th><th>Aged 65+</th><th>Dependency ratio</th></tr><tr><td>${y}%</td><td>${w}%</td><td>${o}%</td><td>${money(dep, 2)} dependants per worker</td></tr></table></div><p class="note">Illustrative shares. A young structure has many children to support; an ageing one has many pensioners.</p>`;
  $("#labA").innerHTML = pyrChart(t.b);
}
const PP = [
  { n: "Low wages and unemployment at home", t: "Push", e: "People leave to find work and higher pay abroad." },
  { n: "War or persecution", t: "Push", e: "People flee for safety (refugees)." },
  { n: "Natural disaster or drought", t: "Push", e: "Farms and homes destroyed; people move to survive." },
  { n: "Higher wages abroad", t: "Pull", e: "Migrants gain more income, and can send money home." },
  { n: "Better healthcare and education abroad", t: "Pull", e: "Migrants and their children can access better services." },
  { n: "Family already living abroad", t: "Pull", e: "Support with housing, jobs and settling in." },
  { n: "Political stability and rights", t: "Pull", e: "Safe, predictable conditions to live and work." },
];
button_table("ppBtns", "ppOut", PP, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>How it affects migration</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each factor <b>raise</b> or <b>lower</b> the birth rate?", buckets: [{ label: "Raises birth rate" }, { label: "Lowers birth rate" }], items: [
  { text: "High infant mortality", b: 0 }, { text: "Children are needed to work the farm and support parents", b: 0 }, { text: "Little access to contraception", b: 0 }, { text: "Large share of women of child-bearing age", b: 0 },
  { text: "More women in higher education and work", b: 1 }, { text: "State pensions reduce the need for children", b: 1 }, { text: "Higher cost of raising children", b: 1 }, { text: "Wide use of contraception", b: 1 },
], done: "Think about cost, education, income and need for children." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>push</b> factor or a <b>pull</b> factor for migration?", buckets: [{ label: "Push" }, { label: "Pull" }], items: [
  { text: "High unemployment at home", b: 0 }, { text: "War in the home country", b: 0 }, { text: "Drought destroys crops", b: 0 }, { text: "Very low wages", b: 0 },
  { text: "Higher wages in another country", b: 1 }, { text: "Better schools and hospitals abroad", b: 1 }, { text: "Relatives already living there", b: 1 }, { text: "A safe, stable society", b: 1 },
], done: "Push: reasons to leave. Pull: reasons to go." });
Lib.classify($("#cl3"), { prompt: "Does each lead to an <b>ageing population</b>?", buckets: [{ label: "Leads to ageing" }, { label: "Does not" }], items: [
  { text: "Fall in the death rate and higher life expectancy", b: 0 }, { text: "Fall in the birth rate", b: 0 }, { text: "Emigration of young adults", b: 0 }, { text: "Better healthcare for older people", b: 0 },
  { text: "A rise in the birth rate", b: 1 }, { text: "Large immigration of young workers", b: 1 }, { text: "A rise in infant deaths", b: 1 }, { text: "More young families moving in", b: 1 },
], done: "Fewer young, longer lives, or young people leaving." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Birth rate", "Live births per 1,000 of the population in a year"],
  ["Death rate", "Deaths per 1,000 of the population in a year"],
  ["Immigration", "People moving into a country to live"],
  ["Emigration", "People leaving a country to live in another"],
  ["Net migration", "Immigration minus emigration"],
  ["Life expectancy", "The average number of years a newborn is expected to live"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "A country has a birth rate of 24 and a death rate of 9 per 1,000. What is its natural increase (per 1,000)?", a: 15, sol: "24 − 9 = <b>15 per 1,000</b>." },
  { q: "Immigration is 4 per 1,000 and emigration is 7 per 1,000. What is net migration (per 1,000)?", a: -3, sol: "4 − 7 = <b>−3 per 1,000</b>: more people leave than arrive." },
  { q: "Natural increase is 15 per 1,000 and net migration is −3 per 1,000. What is the population growth rate (%)?", a: 1.2, tol: 0.01, sol: "(15 − 3) ÷ 10 = <b>1.2%</b>." },
  { q: "A country has 40 million people and a birth rate of 15 per 1,000. How many babies are born in a year (thousands)?", a: 600, hint: "40 million = 40,000 thousand.", sol: "40,000 × 15 = <b>600 thousand</b> (0.6 million)." },
  { q: "A country's population is 8.5 million of which 2.2 million are foreign nationals. What percentage are foreign nationals (1 d.p.)?", a: 25.9, tol: 0.1, sol: "2.2 ÷ 8.5 × 100 = <b>25.9%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the birth rate?", opts: ["Total number of babies born", "Live births per 1,000 of the population in a year", "Babies born per family", "Births per 100 people"], a: 1, why: "A rate per 1,000." },
  { q: "Net migration is:", opts: ["Immigration + emigration", "Immigration − emigration", "Births − deaths", "Population ÷ area"], a: 1, why: "Arrivals minus departures." },
  { q: "Which could cause a fall in the death rate?", opts: ["Better healthcare", "A war", "A famine", "A new epidemic"], a: 0, why: "Fewer deaths from illness." },
  { q: "Which is a pull factor for migration?", opts: ["War", "Unemployment at home", "Higher wages abroad", "Drought"], a: 2, why: "A reason to move to a country." },
  { q: "Which could cause a fall in the birth rate?", opts: ["Fewer women in education", "Higher cost of raising children", "Higher infant mortality", "No contraception"], a: 1, why: "Costs discourage large families." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Birth rate", "The number of live births per 1,000 of the population in a year."],
  ["Death rate", "The number of deaths per 1,000 of the population in a year."],
  ["Natural increase", "The birth rate minus the death rate."],
  ["Immigration", "People moving into a country to live."],
  ["Emigration", "People leaving a country to live in another country."],
  ["Net migration", "Immigration minus emigration."],
  ["Life expectancy", "The average number of years a newborn is expected to live."],
  ["Ageing population", "A rising share of the population aged 65 and over."],
  ["Dependency ratio", "The number of dependants (young and old) compared with the working-age population."],
  ["Push and pull factors", "Reasons for leaving a place (push) and reasons for moving to another (pull)."],
  ["Internal migration", "People moving from one part of a country to another."],
  ["Brain drain", "The emigration of skilled and educated workers."],
] });
labP(); labA();
