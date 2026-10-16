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

const QA = [16, 18, 20, 22, 24], QB = [4, 8, 14, 24, 50], QN = ["Poorest 20%", "Next 20%", "Middle 20%", "Next 20%", "Richest 20%"];
function quintChart(s) {
  const base = 320, k = 5; let o = SV.line(60, base, 710, base) + SV.text(60, 30, "Average income per head in each fifth of the population ($ thousand)", "sm");
  s.q.forEach((v, i) => { const x = 90 + i * 120, h = v * k; o += SV.rect(x, base - h, 90, h, "", { style: `fill:var(${i === 0 ? "--bad" : i === 4 ? "--accent" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 45, base - h - 8, "$" + money(v, 0) + "k", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, QN[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  if (s.t) o += SV.text(380, 58, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stQ"), { w: 760, h: 400, label: "Same average income, different distribution", base: { q: QA, t: "" }, draw: quintChart, steps: [
  { cap: "<b>Country A</b>: income per head is spread fairly evenly. The average is <b>$20,000</b> and the poorest fifth earns <b>$16,000</b>.", s: { q: QA, t: "Country A: average $20k" } },
  { cap: "<b>Country B</b> has the <b>same average income of $20,000</b>, but the richest fifth gets $50,000 each and the poorest fifth only <b>$4,000</b>.", s: { q: QB, t: "Country B: average still $20k" } },
  { cap: "GDP per head is the same, but <b>living standards for most people are very different</b>. An average hides the distribution.", s: { q: QB, t: "Average hides inequality" } },
] });
const LOW = ["Low income, so little saving and investment", "Little capital, technology and education", "Low productivity", "Low output and low incomes", "Poor health and schooling: less skills and ability to work", "Low living standards persist: a poverty trap"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Why poor countries can stay poor", base: { n: 0 }, draw: mkChain(LOW, "--bad"), steps: chainSteps(["<b>Low income</b> means little saving and little tax revenue.", "So there is <b>little investment</b> in capital, technology and education.", "Workers have <b>low productivity</b>.", "<b>Output and incomes stay low</b>.", "Poor health and schooling make it even harder to raise productivity.", "<b>Living standards stay low</b>: a poverty trap. Policies and aid are needed to break the cycle."]) });
const FAR = ["Small plots, little capital and technology", "Low yields: low productivity", "Low and unstable crop prices; weather risk", "Low, seasonal and uncertain income", "Little spent on education, healthcare, nutrition", "Low living standards for farm families"];
Lib.stepper($("#stF"), { w: 760, h: 400, label: "Low-income farmers", base: { n: 0 }, draw: mkChain(FAR, "--warn"), steps: chainSteps(["<b>Small plots</b>, little capital and old methods.", "<b>Low yields</b>: low productivity.", "Crop prices are <b>low and unstable</b>, and weather brings risk.", "Income is <b>low, seasonal and uncertain</b>.", "Little can be spent on <b>education, healthcare and nutrition</b>.", "<b>Living standards are low</b>. Evaluate: roads, markets, irrigation and training can help."]) });

/* Lab 1: distribution simulator */
function labQ() {
  if (!$("#qa") || !$("#qb")) return;
  const u = +$("#qa").value / 100, r = +$("#qb").value / 100;
  const pre = QA.map((a, i) => a * (1 - u) + QB[i] * u), tot = pre.reduce((a, b) => a + b, 0), shares = pre.map((v) => v / tot);
  const post = shares.map((sh) => sh * (1 - r) + 0.2 * r), inc = post.map((sh) => sh * 100);
  $("#qa1").textContent = "$20k"; $("#qa2").textContent = "$" + money(inc[0], 1) + "k"; $("#qa3").textContent = money(post[4] * 100, 0) + "%"; $("#qa4").textContent = money(post[4] / post[0], 1) + " times";
  $("#qav").textContent = `Average income stays at $20,000, but the poorest fifth gets $${money(inc[0], 1)}k and the richest fifth $${money(inc[4], 1)}k: the richest fifth earns ${money(post[4] / post[0], 1)} times as much. ${r > 0 ? "Progressive taxes and benefits (redistribution) have narrowed the gap." : "Move the second slider to see how taxes and benefits narrow the gap."}`;
  $("#labQ").innerHTML = quintChart({ q: inc, t: "" });
}
Lib.slider($("#g1"), { id: "qa", label: "How unequal the pre-tax distribution is (0 = Country A, 100 = Country B)", min: 0, max: 100, step: 5, value: 100, fmt: (v) => v + "%", onInput: labQ });
Lib.slider($("#g2"), { id: "qb", label: "Redistribution through progressive taxes and benefits", min: 0, max: 80, step: 10, value: 0, fmt: (v) => v + "%", onInput: labQ });
const FX = [
  { n: "Productivity and technology", t: "Between countries", e: "High-productivity economies produce more per worker, so incomes are higher.", x: "Germany compared with a subsistence farming economy" },
  { n: "Education and health", t: "Between and within", e: "Skilled, healthy workers earn more; people without schooling are more likely to be poor.", x: "Higher wages for graduates" },
  { n: "Conflict and instability", t: "Between countries", e: "War destroys capital and deters investment, lowering living standards.", x: "Countries emerging from civil war" },
  { n: "Natural resources", t: "Between countries", e: "Oil and minerals can raise national income, if the gains are shared and not wasted.", x: "Guyana's oil discovery (past paper)" },
  { n: "Urban and rural location", t: "Within a country", e: "Cities have higher wages and services; rural areas lag.", x: "Rural farmers compared with city workers" },
  { n: "Ownership of wealth", t: "Within a country", e: "Owners of property and firms earn rents and profits on top of wages.", x: "Landowners and shareholders" },
  { n: "Taxes and benefits", t: "Within a country", e: "Progressive taxes and benefits reduce inequality; regressive taxes increase it.", x: "Welfare states have lower inequality" },
  { n: "Gender and discrimination", t: "Within a country", e: "Unequal pay and access to education and jobs lower incomes of some groups.", x: "Gender pay gaps" },
];
button_table("fxBtns", "fxOut", FX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Applies</th><th>How it affects living standards</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each factor explain differences <b>between countries</b> or <b>within a country</b>?", buckets: [{ label: "Between countries" }, { label: "Within a country" }], items: [
  { text: "Differences in national productivity and technology", b: 0 }, { text: "War and political instability in one country", b: 0 }, { text: "Oil and mineral resources", b: 0 }, { text: "A landlocked location with high transport costs", b: 0 },
  { text: "Higher wages in cities than in the countryside", b: 1 }, { text: "Unequal pay between men and women", b: 1 }, { text: "Some people own property and shares", b: 1 }, { text: "Progressive taxes and benefits narrowing the gap", b: 1 },
], done: "Know both: international differences and distribution inside a country." });
Lib.classify($("#cl2"), { prompt: "Does each <b>raise</b> or <b>lower</b> inequality within a country?", buckets: [{ label: "Raises inequality" }, { label: "Reduces inequality" }], items: [
  { text: "Regressive taxes", b: 0 }, { text: "Wide gaps in education access", b: 0 }, { text: "Ownership of wealth concentrated in few hands", b: 0 }, { text: "Discrimination in hiring", b: 0 },
  { text: "Progressive income tax", b: 1 }, { text: "More generous state benefits", b: 1 }, { text: "Free education and healthcare", b: 1 }, { text: "A national minimum wage", b: 1 },
], done: "Policies that move income from rich to poor reduce inequality." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Income distribution", "How a country's income is shared among its people"],
  ["Quintile", "One fifth (20%) of the population ranked by income"],
  ["Inequality", "A gap in income or wealth between richer and poorer people"],
  ["Urban area", "A city or town"],
  ["Rural area", "A countryside area, often with farming"],
  ["Poverty trap", "A cycle where low income keeps people poor"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why low-income farmers have low living standards</b>.", items: [
  "Small plots and little capital",
  "Low yields and productivity",
  "Low and unstable crop prices and weather risk",
  "Low, seasonal and uncertain income",
  "Little spending on education, healthcare and nutrition",
  "Low living standards",
], done: "A complete 6-mark chain." });
Lib.calc($("#c1"), { qs: [
  { q: "The richest 20% earn $60,000 each and the poorest 20% earn $5,000 each. How many times more do the richest earn?", a: 12, sol: "60,000 ÷ 5,000 = <b>12 times</b>." },
  { q: "The richest 20% of households receive 50% of national income. How much do the other 80% receive (%)?", a: 50, sol: "100 − 50 = <b>50%</b>." },
  { q: "City incomes average $30,000 and rural incomes average $12,000. By what percentage are city incomes higher than rural incomes?", a: 150, sol: "(30,000 − 12,000) ÷ 12,000 × 100 = <b>150%</b>." },
  { q: "A country with a population of 50 million has GDP of $500bn. What is GDP per head ($)?", a: 10000, sol: "500,000m ÷ 50m = <b>$10,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which would most likely increase living standards between countries over time?", opts: ["Falling productivity", "Investment in education and capital", "Civil war", "Falling investment"], a: 1, why: "Better capital and skills raise output." },
  { q: "Which is a likely cause of income inequality within a country?", opts: ["Free education for all", "Wide gaps in skills and wages", "Progressive taxation", "A national minimum wage"], a: 1, why: "Differences in skills lead to pay gaps." },
  { q: "Why may low-income farmers have low living standards?", opts: ["High and stable crop prices", "Low productivity and uncertain incomes", "Easy access to healthcare", "Many machines"], a: 1, why: "Low and unstable incomes." },
  { q: "Average income is the same in two countries. Which statement is correct?", opts: ["Living standards must be the same", "Living standards could differ because distribution differs", "The poor are equally well off", "HDI must be the same"], a: 1, why: "An average hides inequality." },
  { q: "Which is a disadvantage of living in a city?", opts: ["Higher wages", "More jobs", "Higher housing costs and pollution", "Better schools"], a: 2, why: "Cities have costs as well as benefits." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Income distribution", "How a country's income is shared among its people."],
  ["Inequality", "A gap between the incomes or wealth of richer and poorer people."],
  ["Quintile", "One fifth of the population, ranked by income."],
  ["Productivity", "Output per worker."],
  ["Poverty trap", "A cycle in which low income keeps people poor."],
  ["Urban", "Relating to cities and towns."],
  ["Rural", "Relating to the countryside."],
  ["Redistribution", "Moving income from richer to poorer people, for example by progressive taxes and benefits."],
  ["Tertiary sector", "The service industries, such as banking, tourism and retail."],
] });
labQ(); 
