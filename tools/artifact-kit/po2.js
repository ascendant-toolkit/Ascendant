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

function lifeChart(s) {
  const base = 320, X = (a) => 80 + a * 7.2, Y = (v) => base - v * 2.4, inc = (a) => (a < 18 ? 10 : a < 25 ? 10 + (35 * (a - 18)) / 7 : a < 60 ? 45 + 55 * Math.sin(((a - 25) / 35) * Math.PI) : Math.max(15, 45 - (a - 60) * 0.9));
  let o = SV.line(80, base, 710, base) + SV.line(80, base, 80, 40) + SV.text(86, 48, "Household income", "sm") + SV.text(710, base + 28, "Age", "sm", { "text-anchor": "end" });
  o += SV.line(80, Y(35), 710, Y(35), "dash", { style: "stroke:var(--bad);stroke-width:2" }) + SV.text(86, Y(35) - 6, "Poverty line", "sm bd", { style: "fill:var(--bad)" });
  [0, 20, 40, 60, 80].forEach((a) => (o += SV.text(X(a), base + 16, a, "sm", { "text-anchor": "middle" })));
  const pts = []; for (let a = 0; a <= 85; a += 1) if (a <= s.a) pts.push([X(a), Y(inc(a))]);
  if (pts.length > 1) o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 });
  if (s.a >= 0) o += SV.circle(X(s.a), Y(inc(s.a)), 7, inc(s.a) < 35 ? "dot2" : "dot1");
  if (s.t) o += SV.text(X(s.a), Y(inc(s.a)) - 18, s.t, "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Poverty risk over the life cycle", base: { a: 0, t: "" }, draw: lifeChart, steps: [
  { cap: "<b>Childhood:</b> children cannot earn, and the household has more mouths to feed. Large families face a higher risk of poverty.", s: { a: 8, t: "Children" } },
  { cap: "<b>Young adults</b> start work. Wages are low at first, then rise with skills and experience.", s: { a: 30, t: "Early career" } },
  { cap: "<b>Middle age:</b> incomes peak. The risk of poverty is lowest, unless there is unemployment, illness or low pay.", s: { a: 45, t: "Peak earnings" } },
  { cap: "<b>Old age:</b> people retire or cannot work. Without a pension or savings, income falls <b>below the poverty line</b>.", s: { a: 80, t: "Old age" } },
] });
const ENV = ["A drought or flood hits farmland or fishing grounds", "Crops fail or the catch falls", "Farm or fishing income falls sharply", "Households sell assets or borrow at high interest", "They cannot afford enough food, schooling or healthcare", "Poverty deepens and the next shock is harder to survive"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Environmental shocks and poverty", base: { n: 0 }, draw: mkChain(ENV, "--warn"), steps: chainSteps(["A <b>drought, flood or storm</b> hits farmland or fishing grounds.", "<b>Crops fail</b> or the <b>catch falls</b> (also from overfishing and climate change).", "<b>Income falls sharply</b> for farmers and fishermen.", "Households <b>sell assets or borrow</b> at high interest rates.", "They <b>cannot afford food, schooling or healthcare</b>.", "<b>Poverty deepens</b>, and the next shock is even harder to survive."]) });
const TRAP = ["Low income: cannot afford good food, healthcare or school fees", "Poor health and little education", "Low productivity: only low-paid or insecure work", "Income stays low", "Children inherit the same disadvantages", "Poverty is passed on: the poverty trap"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "The poverty trap", base: { n: 0 }, draw: mkChain(TRAP, "--bad"), steps: chainSteps(["<b>Low income:</b> the family cannot afford good food, healthcare or school fees.", "Children have <b>poor health and little education</b>.", "As adults they have <b>low productivity</b> and low-paid or insecure work.", "<b>Income stays low</b>.", "<b>Their children</b> inherit the same disadvantages.", "<b>Poverty is passed on</b>: the poverty trap. Policy has to break the cycle."]) });

/* Lab 1: shocks */
function labK() {
  if (!$("#ka") || !$("#kb") || !$("#kc") || !$("#kd")) return;
  const job = +$("#ka").value / 100, wage = +$("#kb").value / 100, med = +$("#kc").value, crop = +$("#kd").value / 100;
  const base = 420, inc = base * (1 - job) * (1 - wage) * (1 - crop), needs = 300 + med, gap = inc - needs;
  $("#ka1").textContent = "$" + Math.round(inc); $("#ka2").textContent = "$" + needs; $("#ka3").textContent = (gap >= 0 ? "+$" : "−$") + Math.abs(Math.round(gap));
  $("#kav").textContent = gap >= 0 ? `Income of $${Math.round(inc)} covers basic needs of $${needs}, with $${Math.round(gap)} spare. This household is not in absolute poverty.` : `Income of $${Math.round(inc)} is $${Math.abs(Math.round(gap))} short of basic needs of $${needs}: the household cannot afford the basic necessities: absolute poverty. Combined shocks (job loss, low pay, illness, crop failure) hit hardest.`;
  const b = 300; let o = SV.line(80, b, 700, b);
  [["Weekly income", inc, "--accent"], ["Basic needs", needs, "--warn"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * 0.55; o += SV.rect(x, b - h, 150, h, "", { style: `fill:var(${gap >= 0 || i === 1 ? c : "--bad"})`, opacity: 0.85 }) + SV.text(x + 75, b - h - 8, "$" + Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, b + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labK").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ka", label: "Unemployment: share of working time lost", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g2"), { id: "kb", label: "Low wages: cut in the hourly wage", min: 0, max: 50, step: 5, value: 0, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g3"), { id: "kc", label: "Illness: extra medical costs a week", min: 0, max: 200, step: 20, value: 0, fmt: (v) => "$" + v, onInput: labK });
Lib.slider($("#g4"), { id: "kd", label: "Environmental shock: share of farm income lost", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labK });
const CAU = [
  { n: "Unemployment", m: "No wage; small or no benefits; skills fade; harder to re-enter work.", w: "Workers in declining industries; young people; people in recessions.", p: "Job creation, retraining, unemployment benefit." },
  { n: "Low wages", m: "Pay too low to afford necessities, especially with a large family.", w: "Unskilled, part-time and informal workers; small farmers.", p: "National minimum wage, education and training, growth." },
  { n: "Illness", m: "Cannot work; medical costs; carers lose earnings; lower productivity.", w: "People without healthcare; in areas with disease and poor sanitation.", p: "Free or subsidised healthcare, clean water, sickness benefits." },
  { n: "Age", m: "Children cannot earn; the old may have no pension or savings.", w: "Large families; pensioners without state pensions.", p: "State pensions, child benefits, family support." },
  { n: "Environmental factors", m: "Drought, floods, soil erosion, overfishing and climate change destroy crops, fish stocks and homes.", w: "Farmers, fishermen, people in disaster-prone areas.", p: "Irrigation, insurance, disaster relief, sustainable fishing rules." },
  { n: "Low education", m: "Low skills mean low wages and unemployment. Poor families may not afford schooling.", w: "Children of poor families; girls in some countries.", p: "Free education, school meals, grants." },
];
button_table("cuBtns", "cuOut", CAU, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it causes poverty</th><th>Who is at risk</th><th>Possible response</th></tr><tr><td>${p.m}</td><td>${p.w}</td><td>${p.p}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>cause of poverty</b> is each?", buckets: [{ label: "Unemployment" }, { label: "Low wages" }, { label: "Illness" }, { label: "Age" }, { label: "Environmental" }], items: [
  { text: "A factory closes and workers have no income", b: 0 }, { text: "Pay in a job is too low for basic needs", b: 1 }, { text: "A parent cannot work because of disease", b: 2 },
  { text: "A pensioner with no state pension", b: 3 }, { text: "A drought destroys the harvest", b: 4 }, { text: "Fish stocks collapse after overfishing and warming seas", b: 4 },
  { text: "Medical bills use up the family's savings", b: 2 }, { text: "A large family of young children with one earner", b: 3 },
], done: "Five causes in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Does each make poverty <b>more likely</b> or <b>less likely</b>?", buckets: [{ label: "More likely" }, { label: "Less likely" }], items: [
  { text: "Unemployment rises", b: 0 }, { text: "Illness with no health insurance", b: 0 }, { text: "Floods destroy farmland", b: 0 }, { text: "No state pension", b: 0 },
  { text: "A good education and skills", b: 1 }, { text: "Free healthcare", b: 1 }, { text: "A job paying above the poverty line", b: 1 }, { text: "A pension in old age", b: 1 },
], done: "Know both the causes and the protections." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Poverty trap", "A cycle where low income keeps people poor across generations"],
  ["Structural unemployment", "Unemployment from a mismatch of skills and jobs"],
  ["Informal economy", "Unregulated work with low and insecure pay"],
  ["Subsistence farming", "Growing food mainly for the family's own use"],
  ["Climate change", "Long-term change in weather patterns that can harm farming and fishing"],
  ["Dependency ratio", "Number of dependants (young and old) compared with workers"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why children of poor families tend to receive less education</b>.", items: [
  "The family has a low income",
  "It cannot afford fees, books, uniforms or transport",
  "Children may work or care for others instead of attending school",
  "Children leave school with few skills",
  "They find only low-paid work or unemployment",
  "They remain poor and cannot afford to educate their own children",
], done: "The poverty trap across generations." });
Lib.calc($("#c1"), { qs: [
  { q: "A worker earns $400 a week. She loses 40% of her working hours. What is her new weekly income ($)?", a: 240, sol: "400 × 0.6 = <b>$240</b>." },
  { q: "Basic needs cost $300 a week. Her income falls to $240. How big is the shortfall ($)?", a: 60, sol: "300 − 240 = <b>$60</b>." },
  { q: "A fisherman's catch falls from 50 kg a day to 30 kg a day. By what percentage has it fallen?", a: 40, sol: "20 ÷ 50 × 100 = <b>40%</b>." },
  { q: "In a village of 2,000 people, 30% are children and 10% are elderly. How many are of working age?", a: 1200, sol: "100% − 40% = 60%. 60% × 2,000 = <b>1,200</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of poverty?", opts: ["Unemployment", "High wages", "Free healthcare", "A state pension"], a: 0, why: "No wage means no money for necessities." },
  { q: "Why might old people be at risk of poverty?", opts: ["They earn peak incomes", "They may have no pension or savings and cannot work", "They pay high income tax", "They are always employed"], a: 1, why: "Incomes fall in old age." },
  { q: "How can illness cause poverty?", opts: ["It increases wages", "It stops people working and raises medical costs", "It raises school attendance", "It lowers prices"], a: 1, why: "Lost income and costs." },
  { q: "Which environmental factor could cause poverty among farmers?", opts: ["Drought", "A good harvest", "Higher crop prices", "Irrigation"], a: 0, why: "Crops fail and incomes fall." },
  { q: "A poverty trap is when:", opts: ["Poor people stay poor over generations", "Rich people lose money", "Prices fall", "Wages rise quickly"], a: 0, why: "Low income, low education and low income again." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Unemployment", "Being without a job while willing, able and looking for work."],
  ["Low wages", "Pay too low to afford basic necessities."],
  ["Illness", "Poor health that prevents work and raises costs."],
  ["Dependants", "People who rely on others' income, such as children and the elderly."],
  ["Environmental factors", "Natural conditions such as drought, floods and climate change that affect income."],
  ["Poverty trap", "A cycle in which low income keeps people poor over generations."],
  ["Informal economy", "The part of the economy not regulated, protected or taxed by the government."],
  ["Subsistence farming", "Farming mainly to feed the farmer's own family."],
  ["Migration", "People moving to another place to find work or safety."],
] });
labK(); 
