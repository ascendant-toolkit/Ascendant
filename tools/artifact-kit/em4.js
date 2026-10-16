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

function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, "PPC", "lbl bd t1");
  const k = s.in, f = 1 - 0.3 * (1 - k), px = ox + X * 0.7071 * f, py = oy - Y * 0.7071 * f;
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, k > 0.5 ? "dot1" : "dot2");
  if (s.t) o += SV.text(px + 14, py + 24, s.t, "lbl bd t2", { style: halo });
  return o;
}

Lib.stepper($("#stP"), { w: 760, h: 400, label: "Unemployment and the PPC", base: { s: 1, in: 0, t: "" }, draw: ppcChart, steps: [
  { cap: "With <b>full employment</b> the economy produces <b>on its PPC</b>: all resources are used.", s: { s: 1, in: 1, t: "Full employment" } },
  { cap: "When workers lose their jobs, resources lie idle. The economy produces <b>inside the PPC</b>: lower output of everything.", s: { s: 1, in: 0, t: "Unemployment" } },
  { cap: "This is why unemployment is a <b>waste of resources</b>: the economy could produce more with the same factors. Bringing the unemployed back to work moves it back to the PPC.", s: { s: 1, in: 1, t: "Back to full employment" } },
] });
const UCH = ["Unemployment rises: workers lose their jobs", "Household incomes and spending fall", "Firms' sales and profits fall", "Government tax revenue falls and benefit spending rises", "The budget deficit widens: more borrowing", "Lower output: the economy produces below its potential"];
Lib.stepper($("#stU"), { w: 760, h: 400, label: "How unemployment spreads through the economy", base: { n: 0 }, draw: mkChain(UCH, "--bad"), steps: chainSteps(["<b>Individuals:</b> workers lose their jobs and their income.", "<b>Consumers:</b> lower incomes mean lower spending.", "<b>Firms:</b> sales and profits fall, so they may cut more jobs.", "<b>Government:</b> tax revenue falls and benefit spending rises.", "<b>Budget:</b> the deficit widens and the government has to borrow more.", "<b>Economy:</b> output falls below potential and living standards fall."]) });

/* Lab 1: cost to the government */
function labU() {
  if (!$("#ua") || !$("#ub") || !$("#uc")) return;
  const u = +$("#ua").value, b = +$("#ub").value, t = +$("#uc").value, tax = (u * t) / 1e6, ben = (u * b) / 1e6, tot = tax + ben;
  $("#ua1").textContent = "$" + money(tax, 2) + "bn"; $("#ua2").textContent = "$" + money(ben, 2) + "bn"; $("#ua3").textContent = "$" + money(tot, 2) + "bn";
  $("#uav").textContent = u === 0 ? "No rise in unemployment." : `If ${u.toLocaleString("en-US")} thousand more people are unemployed, the government loses about $${money(tax, 2)}bn in tax and pays about $${money(ben, 2)}bn in benefits: the budget gets worse by $${money(tot, 2)}bn. This money has an opportunity cost: it could have paid for schools or hospitals.`;
  const base = 300, k = 60 / Math.max(1, Math.max(tot, 1)) * 4; let o = SV.line(60, base, 700, base);
  [["Lost tax revenue", tax, "--accent"], ["Extra benefits", ben, "--warn"], ["Total effect on deficit", tot, "--bad"]].forEach(([n, v, c], i) => { const x = 110 + i * 190, h = Math.min(250, v * 40); o += SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, "$" + money(v, 2) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labU").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ua", label: "Rise in the number unemployed (thousands)", min: 0, max: 1000, step: 50, value: 500, fmt: (v) => v + "k", onInput: labU });
Lib.slider($("#g2"), { id: "ub", label: "Benefit paid to each unemployed person ($ a year)", min: 2000, max: 10000, step: 500, value: 6000, fmt: (v) => "$" + v, onInput: labU });
Lib.slider($("#g3"), { id: "uc", label: "Tax each worker used to pay ($ a year)", min: 2000, max: 15000, step: 500, value: 9000, fmt: (v) => "$" + v, onInput: labU });
const UG = [
  { n: "The individual", s: "Lower income, debt, stress and health problems; skills fade the longer the spell.", l: "Long-term unemployment can mean permanent loss of earnings and confidence.", x: "Explain two consequences of unemployment" },
  { n: "Firms", s: "Lower consumer spending cuts sales and profits; some firms close.", l: "Wasted potential workers; but firms may find hiring easier and wage costs lower.", x: "Explain two consequences to firms of unemployment" },
  { n: "The government", s: "Tax revenue falls, benefit spending rises: bigger deficit.", l: "Higher borrowing and debt; opportunity cost for other spending.", x: "Analyse how unemployment may affect the government's budget" },
  { n: "The economy", s: "Output falls below potential; lower real GDP and living standards.", l: "Wasted resources, more inequality and poverty, social costs; may lower inflation.", x: "Analyse why a government may have lower unemployment as its main aim" },
];
button_table("ugBtns", "ugOut", UG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Short-run effect</th><th>Longer-run effect</th><th>Exam link</th></tr><tr><td>${p.s}</td><td>${p.l}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Who mainly bears each <b>consequence of unemployment</b>?", buckets: [{ label: "Individual" }, { label: "Firms" }, { label: "Government" }, { label: "Economy" }], items: [
  { text: "Lower income and stress", b: 0 }, { text: "Skills fade over time", b: 0 },
  { text: "Falling sales as customers spend less", b: 1 }, { text: "Lower profits and some closures", b: 1 },
  { text: "Lower tax revenue and higher benefit spending", b: 2 }, { text: "Larger budget deficit", b: 2 },
  { text: "Output below the PPC: wasted resources", b: 3 }, { text: "Lower real GDP and living standards", b: 3 },
], done: "Individual, firms, government, economy: the four groups in the syllabus." });
Lib.classify($("#cl2"), { prompt: "Is each effect of rising unemployment likely to <b>raise</b> or <b>lower</b> the government's budget balance?", buckets: [{ label: "Moves budget towards deficit" }, { label: "Moves budget towards surplus" }], items: [
  { text: "Less income tax from people who lost jobs", b: 0 }, { text: "More unemployment benefit paid", b: 0 }, { text: "Less sales tax as spending falls", b: 0 }, { text: "Lower corporation tax as profits fall", b: 0 },
  { text: "Government cuts benefits", b: 1 }, { text: "Government raises taxes", b: 1 },
], done: "Unemployment tends to widen the deficit." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Opportunity cost", "The next best alternative given up"],
  ["Automatic stabilisers", "Taxes and benefits that change with the cycle and cushion falls in demand"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Long-term unemployment", "Being without a job for a long period, often a year or more"],
  ["Poverty", "A lack of income to meet basic needs"],
  ["Potential output", "Output when resources are fully used"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how unemployment could widen the budget deficit</b>.", items: [
  "Firms lay off workers",
  "Workers lose their earnings",
  "Income tax and sales tax revenue fall",
  "More people claim unemployment benefit",
  "Government spending rises while revenue falls",
  "The budget deficit widens",
], done: "A full 4-mark chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A worker paid $10,000 a year in tax. She loses her job and claims $5,000 in benefit. By how much does the government's position worsen ($)?", a: 15000, sol: "10,000 + 5,000 = <b>$15,000</b>." },
  { q: "If 400,000 workers each lose $9,000 in tax payments, how much tax revenue is lost ($bn)?", a: 3.6, hint: "400,000 × 9,000 = 3,600,000,000.", sol: "400,000 × 9,000 = $3.6bn = <b>$3.6bn</b>." },
  { q: "Unemployment benefit is $6,000 per person. 500,000 more people claim it. What is the extra cost ($bn)?", a: 3, sol: "500,000 × 6,000 = <b>$3bn</b>." },
  { q: "Output is $800bn at full employment and $760bn with unemployment. What percentage of output is lost?", a: 5, sol: "40 ÷ 800 × 100 = <b>5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a likely effect of rising unemployment on the government's budget?", opts: ["Higher tax revenue", "A smaller deficit", "A larger deficit", "No effect"], a: 2, why: "Tax falls and benefit spending rises." },
  { q: "Unemployment means an economy is producing:", opts: ["On its PPC", "Outside its PPC", "Inside its PPC", "At full employment"], a: 2, why: "Resources are not fully used." },
  { q: "Which is a consequence of unemployment for an individual?", opts: ["Higher income", "Loss of skills over time", "Lower stress", "More tax paid"], a: 1, why: "Skills fade the longer someone is out of work." },
  { q: "Rising unemployment could reduce inflation because:", opts: ["Total demand falls", "Output rises", "Taxes fall", "Imports rise"], a: 0, why: "Lower spending reduces demand-pull pressure." },
  { q: "A firm may suffer from unemployment because:", opts: ["Customers have less to spend", "Workers become more skilled", "Taxes fall", "Imports fall"], a: 0, why: "Lower incomes mean lower sales." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Opportunity cost", "The next best alternative given up when a choice is made."],
  ["Automatic stabilisers", "Taxes and benefits that change with the economic cycle and cushion falls in demand."],
  ["Budget deficit", "Government spending is higher than revenue."],
  ["Poverty", "A lack of income to meet basic needs."],
  ["Long-term unemployment", "Being without a job for a long period."],
  ["Living standards", "The quality and quantity of goods and services people can obtain."],
  ["Potential output", "Output when resources are fully and efficiently used."],
  ["Social costs of unemployment", "Costs to society such as crime, ill health and family problems."],
] });
labU();
