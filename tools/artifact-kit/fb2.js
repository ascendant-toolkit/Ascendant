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
const D = (b) => [-b, 50 + 50 * b], S = (d, shift = 0) => [d, 50 - 50 * d + shift];
const fmtSteep = (v) => (v < 0.8 ? "flat (elastic)" : v > 1.4 ? "steep (inelastic)" : "medium");
const money = (v, d = 1) => Lib.fmtN(v, d);
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
/* ---------- 2. multiplier ---------- */
const MPC0 = 0.8;
function multChart(s) {
  const inj = s.inj ?? 20, mpc = s.mpc ?? MPC0, base = 330, k = 205 / inj, n = s.n;
  let o = SV.line(30, base, 740, base), tot = 0;
  for (let i = 0; i < 8; i++) {
    const v = clamp(n - i, 0, 1), a = inj * Math.pow(mpc, i);
    if (v <= 0) continue;
    const h = a * k * v, x = 40 + i * 85;
    tot += a * v;
    o += SV.rect(x, base - h, 64, h, "", { style: "fill:var(" + (i ? "--accent" : "--warn") + ")", opacity: 0.85 });
    if (v > 0.6) o += SV.text(x + 32, base - h - 8, "$" + money(a, a % 1 === 0 ? 0 : 1) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 32, base + 20, i ? "Round " + (i + 1) : "Injection", "sm", { "text-anchor": "middle" });
  }
  if (n > 7.5) o += SV.text(730, base - 8, "…", "lbl bd", { "text-anchor": "end", style: "font-size:24px" });
  o += SV.text(40, 40, "Extra income created so far: $" + money(tot, 1) + "m", "lbl bd", { style: "font-size:17px" });
  if (s.fin > 0.5) o += SV.text(40, 70, "Final rise = $" + money(inj, 0) + "m ÷ (1 − " + mpc + ") = $" + money(inj / (1 - mpc), 0) + "m: " + money(1 / (1 - mpc), 1) + " times the original", "lbl bd t3", { style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "The multiplier effect", base: { n: 0, fin: 0 }, draw: multChart, steps: [
  { cap: "The government spends an extra <b>$20m</b> (for example building a road). That money becomes income for construction firms and workers.", s: { n: 1, fin: 0 } },
  { cap: "Those who receive the $20m spend <b>$16m</b> of it (80%) and save $4m. The $16m is now income for shops, suppliers and their workers.", s: { n: 2, fin: 0 } },
  { cap: "They in turn spend 80% of $16m, about <b>$12.8m</b>. Each round is smaller because some is <b>saved</b> (and some leaks out to imports and tax) each time.", s: { n: 3, fin: 0 } },
  { cap: "The rounds keep going: $10.2m, $8.2m, $6.6m, $5.2m, $4.2m… The rises get smaller but they add up.", s: { n: 8, fin: 0 } },
  { cap: "The total rise in income, spending and output is <b>$100m</b>, five times the original $20m. That bigger-than-initial effect is the <b>multiplier effect</b>. The more people spend of extra income, the bigger it is.", s: { n: 8, fin: 1 } },
] });


/* education spending: AD rises now, AS later */
function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = a >= 1;
  const pts = (x) => [[QX(x), PY(30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Spending on education: short-run and long-run effects", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>. The government decides to spend more on <b>education</b>.", s: { sh: 0, a: 0 } },
  { cap: "In the <b>short run</b> the spending is part of <b>G</b>. Builders and teachers are paid and spend their pay, so <b>AD shifts right</b> to AD₁. Real GDP and jobs rise, and the price level edges up.", s: { sh: 22, a: 0 } },
  { cap: "In the <b>long run</b> the workforce is better skilled and more productive. The economy can produce more at each price level, so <b>AS shifts right</b> to AS₁. Output is higher and the price level lower than AD alone would give.", s: { sh: 22, a: 14 } },
  { cap: "<b>Evaluate:</b> the supply effect takes years, the money has an <b>opportunity cost</b> (it could have been spent elsewhere) and it only works if the education is of good quality and leads to jobs.", s: { sh: 22, a: 14 } },
] });

/* spending scorecard */
const SP = [
  { n: "Healthcare", why: "Merit good: a healthier workforce, fairer access to treatment.", ad: "Pays staff and suppliers, so AD could rise quickly.", lr: "Fewer days lost to illness: productivity may rise.", cost: "Large and rising cost, especially as populations age." },
  { n: "Education", why: "Merit good: skills for jobs, equal opportunity.", ad: "Pays teachers and builders: AD could rise.", lr: "A more skilled workforce raises AS and long-run growth.", cost: "Benefits take years to appear; quality matters." },
  { n: "Pensions and benefits", why: "Equity: income for the old, the sick and the unemployed.", ad: "Recipients spend most of it, so AD could rise, and benefits rise automatically in a slump.", lr: "Little direct effect on AS.", cost: "Can be costly; may reduce the incentive to work if too generous." },
  { n: "Infrastructure", why: "Roads, rail and broadband that private firms may not build.", ad: "Construction jobs and orders raise AD.", lr: "Lower costs and faster transport can raise AS.", cost: "Large projects, long delays, and money borrowed to build them has to be repaid." },
  { n: "Defence and law and order", why: "Public goods that markets will not supply.", ad: "Pays soldiers, police and suppliers.", lr: "Security helps firms and investors.", cost: "High opportunity cost: the money could go to other areas." },
];
function showSP(i) {
  const p = SP[i];
  $("#spBtns").innerHTML = SP.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#spBtns .b").forEach((b) => (b.onclick = () => showSP(+b.dataset.j)));
  $("#spOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Why spend</th><th>Short run: effect on AD</th><th>Long run</th><th>Cost or limit</th></tr><tr><td>${p.why}</td><td>${p.ad}</td><td>${p.lr}</td><td>${p.cost}</td></tr></table></div>`;
}
showSP(0);
/* Lab 2: multiplier */
function labM() {
  if (!$("#ma") || !$("#mb")) return;
  const inj = +$("#ma").value, mpc = +$("#mb").value, k = 1 / (1 - mpc), tot = inj * k;
  $("#ma1").textContent = money(k, 2); $("#ma2").textContent = "$" + money(tot, 0) + "m"; $("#ma3").textContent = "$" + money(tot - inj, 0) + "m";
  $("#mav").textContent = `For every $1 of extra income people spend $${money(mpc, 2)} and save or lose the rest, so the total rise is ${money(k, 2)} times the injection. Raise the share spent and the multiplier grows.`;
  $("#labM").innerHTML = multChart({ n: 8, fin: 1, inj, mpc });
}
Lib.slider($("#g4"), { id: "ma", label: "Extra government spending", min: 5, max: 50, step: 5, value: 20, fmt: (v) => "$" + v + "m", onInput: labM });
Lib.slider($("#g5"), { id: "mb", label: "Share of extra income spent", min: 0.1, max: 0.9, step: 0.05, value: 0.8, fmt: (v) => Math.round(v * 100) + "%", onInput: labM });


/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>reason for government spending</b> fits each example?", buckets: [{ label: "Influence economic activity" }, { label: "Reduce market failure" }, { label: "Promote equity" }, { label: "Pay debt interest" }], items: [
  { text: "A stimulus package of road building during a recession", b: 0 }, { text: "Cutting spending when the economy is overheating", b: 0 },
  { text: "Providing street lighting and national defence", b: 1 }, { text: "Free vaccination (a merit good)", b: 1 },
  { text: "Pensions for older people", b: 2 }, { text: "Housing support for low-income families", b: 2 },
  { text: "Interest on money borrowed in earlier years", b: 3 }, { text: "Repaying part of the national debt", b: 3 },
], done: "Match the reason to the aim behind the spending." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Multiplier effect", "Final change in AD is larger than the initial change"],
  ["Injection", "Money added to the flow of income, such as government spending"],
  ["Leakage", "Money taken out of the flow, such as saving, taxes and imports"],
  ["Merit good", "A good that is under-provided by the market and may be provided by the government"],
  ["Public good", "A good that private firms will not supply because people cannot be excluded"],
  ["Transfer payment", "Benefits paid by the government with no good or service in return"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the steps of the <b>multiplier</b> in order.", items: [
  "The government raises its spending by $20m",
  "Firms and workers receive $20m of extra income",
  "They spend part of it (say $16m) and save the rest",
  "That spending becomes income for other people, who spend part of it again",
  "The rounds continue, each smaller than the last",
  "Total rise in spending, income and output is larger than the original $20m",
], done: "That is the multiplier effect." });
Lib.order($("#o2"), { prompt: "Put the long-run effect of <b>spending on education</b> in order.", items: [
  "The government raises spending on schools and training",
  "More young people gain skills and qualifications",
  "Workers become more productive",
  "Firms can produce more at each price level: AS shifts right",
  "Output rises and the price level may be lower than otherwise",
  "Future tax revenue could rise as incomes grow",
], done: "A supply-side chain from spending." });
Lib.calc($("#c1"), { qs: [
  { q: "Government spending rises by $40m. People spend 75% of any extra income. Using multiplier = 1 ÷ (1 − share spent), calculate the total rise in income ($m).", a: 160, hint: "Multiplier = 1 ÷ 0.25.", sol: "Multiplier = 1 ÷ (1 − 0.75) = 4. Total rise = 4 × 40 = <b>$160m</b>." },
  { q: "Government spending rises by $50m. People spend 80% of any extra income. Calculate the total rise in income ($m).", a: 250, hint: "Multiplier = 1 ÷ 0.2.", sol: "Multiplier = 1 ÷ (1 − 0.8) = 5. Total rise = 5 × 50 = <b>$250m</b>." },
  { q: "The multiplier is 4. The government injects $30m. What is the final rise in income ($m)?", a: 120, sol: "4 × 30 = <b>$120m</b>." },
  { q: "People spend 50% of any extra income. What is the multiplier?", a: 2, sol: "1 ÷ (1 − 0.5) = <b>2</b>." },
  { q: "A government spends $15bn on healthcare out of total spending of $75bn. What percentage is spent on healthcare?", a: 20, sol: "15 ÷ 75 × 100 = <b>20%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a reason for government spending?", opts: ["To pay interest on the national debt", "To discourage demerit goods", "To protect domestic firms by taxing imports", "To raise the costs of polluters"], a: 0, why: "The other three are aims of taxation, not spending." },
  { q: "Which is an example of a public good the government may provide?", opts: ["Cinema tickets", "National defence", "A restaurant meal", "Mobile phone"], a: 1, why: "Defence is non-excludable, so private firms will not supply it." },
  { q: "What is the multiplier effect?", opts: ["A fall in AD after a tax rise", "The final change in AD being larger than the initial injection", "Spending financed only by tax", "A rise in the deficit"], a: 1, why: "Each round of spending creates income for someone else." },
  { q: "Which would make the multiplier smaller?", opts: ["People spend a larger share of extra income", "People save a larger share of extra income", "Government spending rises", "Firms hire more workers"], a: 1, why: "More leakages mean a smaller multiplier." },
  { q: "Government spending on education is most likely to raise AS in the long run because:", opts: ["Teachers spend their wages", "Workers become more skilled and productive", "It raises the budget deficit", "It reduces imports"], a: 1, why: "Productivity rises, so the economy can produce more." },
  { q: "Which spending is mainly to promote equity?", opts: ["Unemployment benefit", "Road building", "Defence", "Debt interest"], a: 0, why: "Benefits redistribute income to people on low incomes." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Government spending", "Money spent by the government on goods, services, benefits and debt interest. Also called G in AD."],
  ["Multiplier effect", "The final impact on aggregate demand is greater than the initial change."],
  ["Public good", "A good provided for everyone, which private firms will not supply as non-payers cannot be excluded."],
  ["Merit good", "A good that people may not value enough, so it is under-provided by the market, such as education and healthcare."],
  ["Transfer payment", "A payment, such as a pension or benefit, made by the government with nothing received in return."],
  ["Injection", "Money added to the circular flow, such as government spending."],
  ["Leakage", "Money taken out of the circular flow: savings, taxes and imports."],
  ["Opportunity cost", "The next best alternative given up when a choice is made."],
  ["Infrastructure", "The roads, rail, energy and broadband networks the economy relies on."],
] });
labM(); showSP(0);
