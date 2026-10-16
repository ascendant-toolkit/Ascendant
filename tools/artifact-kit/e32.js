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

const CN = ["The price of a good rises", "Buying it means giving up more other goods", "The opportunity cost of the good rises", "Consumers buy less of it", "Quantity demanded falls"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Consumer decisions", base: { n: 0 }, draw: mkChain(CN, "--accent"), steps: chainSteps(["The <b>price of a good rises</b>.", "Buying it means giving up <b>more other goods</b>.", "The <b>opportunity cost</b> of the good rises.", "Consumers <b>buy less</b> of it.", "<b>Quantity demanded falls</b>."]) });
const GV = ["The government has a limited tax budget", "It could spend on a hospital or on a new school", "Building the hospital means no school (opportunity cost)", "It compares the benefits of each to society", "It chooses the option with greater benefit"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "Government decisions", base: { n: 0 }, draw: mkChain(GV, "--good"), steps: chainSteps(["The government has a <b>limited budget</b>.", "It could spend on a <b>hospital</b> or on a <b>new school</b>.", "Building the hospital means <b>no school</b>: the opportunity cost.", "It <b>compares the benefits</b> of each to society.", "It chooses the option with the <b>greater benefit</b>."]) });
const FM = ["A firm has $1m to invest", "Options: new machines, advertising, or staff pay rises", "It compares expected extra profit of each", "It chooses the best; the next best is the opportunity cost", "If costs or benefits change, the decision may change"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "Firm decisions", base: { n: 0 }, draw: mkChain(FM, "--warn"), steps: chainSteps(["A firm has <b>$1m to invest</b>.", "Options: <b>new machines</b>, <b>advertising</b>, or <b>staff pay rises</b>.", "It compares the <b>expected extra profit</b> of each.", "It chooses the best; the <b>next best is the opportunity cost</b>.", "If costs or benefits change, the <b>decision may change</b>."]) });

/* Lab 1: work or study */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const wage = +$("#wa").value, ben = +$("#wb").value, yrs = 3, cost = wage * yrs, gain = ben * 30 - cost, go = ben * 10 > wage * 1;
  $("#wa1").textContent = "$" + cost.toLocaleString(); $("#wa2").textContent = "$" + (ben * 30).toLocaleString(); $("#wa3").textContent = (gain >= 0 ? "+" : "−") + "$" + Math.abs(gain).toLocaleString();
  $("#wav").textContent = `Studying for 3 years gives up $${cost.toLocaleString()} of wages (the opportunity cost). If the degree raises pay by $${ben.toLocaleString()} a year for 30 years that is $${(ben * 30).toLocaleString()}. Net gain: ${gain >= 0 ? "+" : "−"}$${Math.abs(gain).toLocaleString()}. ${gain > 0 ? "Study looks worthwhile." : "The opportunity cost outweighs the benefit, so working may be better."} Higher wages raise the opportunity cost of study.`;
  const base = 280, k = 200 / Math.max(cost, ben * 30, 1); let o = SV.line(60, base, 700, base);
  [["Opportunity cost (wages lost)", cost, "--bad"], ["Benefit (extra pay later)", ben * 30, "--good"]].forEach(([n, v, c], i) => { const x = 140 + i * 280, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + v.toLocaleString(), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Yearly wage if you worked instead", min: 5000, max: 40000, step: 1000, value: 15000, fmt: (v) => "$" + v.toLocaleString(), onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Extra yearly pay from the qualification", min: 1000, max: 20000, step: 1000, value: 6000, fmt: (v) => "$" + v.toLocaleString(), onInput: labW });
const DM = [
  { n: "Consumer", d: "Which goods to buy", e: "Gives up other goods; a higher price raises the opportunity cost." },
  { n: "Worker", d: "Work, study or leisure", e: "Study loses wages; overtime loses leisure; higher wages raise the cost of leisure." },
  { n: "Firm", d: "Invest or advertise", e: "Funds used on one project cannot be used on another." },
  { n: "Government", d: "Health, education, defence", e: "More on one means less on another." },
];
button_table("dmBtns", "dmOut", DM, 0, (p) => `<div class="tw"><table class="t"><tr><th>Decision</th><th>Influence of opportunity cost</th></tr><tr><td>${p.d}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> makes each decision?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "Whether to buy a phone or save", b: 0 }, { text: "Whether to buy a cheaper brand", b: 0 },
  { text: "Whether to take unpaid training", b: 1 }, { text: "Whether to work overtime", b: 1 },
  { text: "Whether to invest in a new machine", b: 2 }, { text: "Which product to make", b: 2 },
  { text: "How to divide the budget between health and education", b: 3 }, { text: "Whether to build a bridge or a school", b: 3 },
], done: "All face opportunity cost." });
Lib.classify($("#cl2"), { prompt: "Would a rise in the opportunity cost make each choice <b>more</b> or <b>less</b> likely?", buckets: [{ label: "More likely" }, { label: "Less likely" }], items: [
  { text: "Higher wages: choosing to work rather than study", b: 0 }, { text: "Higher price of wheat: a farmer switches to wheat", b: 0 },
  { text: "Higher wages: a student staying in education", b: 1 }, { text: "Higher price of a good: consumers buying it", b: 1 },
  { text: "A pay cut: working extra hours", b: 1 }, { text: "Higher wages: choosing leisure over work", b: 1 },
], done: "A higher opportunity cost makes the choice less attractive." });
Lib.match($("#m1"), { prompt: "Match the decision to the opportunity cost involved.", pairs: [
  ["A worker takes unpaid training", "Wages lost"],
  ["A firm buys new technology", "Advertising or wage rises given up"],
  ["A government spends on healthcare", "Education or defence given up"],
  ["A consumer buys a holiday", "Other goods given up"],
  ["A farmer grows apples", "The next best crop"],
  ["A student studies", "Leisure or work time"],
], done: "Link each decision to what is given up." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>how a government uses opportunity cost</b>.", items: [
  "The government has a limited budget",
  "It lists projects it could fund",
  "It compares the benefits of each to society",
  "It chooses the project with the most benefit",
  "The other projects are the opportunity cost",
], done: "Weighing benefits against opportunity cost." });
Lib.calc($("#c1"), { qs: [
  { q: "A student could earn $18,000 a year or study for 4 years. What wages are given up ($)?", a: 72000, sol: "4 × 18,000 = <b>$72,000</b>." },
  { q: "A degree raises pay by $8,000 a year for 25 years. What is the total extra pay ($)?", a: 200000, sol: "8,000 × 25 = <b>$200,000</b>." },
  { q: "A government has $10bn. It spends $6bn on healthcare. How much is left for other uses ($bn)?", a: 4, sol: "10 − 6 = <b>$4bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in wages raises the opportunity cost of:", opts: ["Work", "Leisure", "Training being free", "Machines"], a: 1, why: "More pay given up for each hour of leisure." },
  { q: "A government that spends on defence has an opportunity cost of:", opts: ["Nothing", "Other public services", "Free goods", "Taxes"], a: 1, why: "Less for health, education, etc." },
  { q: "A firm's opportunity cost of investing in new technology is:", opts: ["The technology itself", "The next best use of the funds", "Nothing", "Profit"], a: 1, why: "What the money could have done." },
  { q: "When the price of a good rises, consumers may:", opts: ["Buy more", "Buy less as the opportunity cost rises", "Ignore it", "Buy free goods"], a: 1, why: "Higher opportunity cost." },
  { q: "Good decisions compare:", opts: ["Costs only", "Benefits with opportunity cost", "Only price", "Only time"], a: 1, why: "Weigh both." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Opportunity cost", "The next best alternative given up."],
  ["Benefit", "The gain from a decision."],
  ["Trade-off", "Giving up one thing for another."],
  ["Decision-maker", "A consumer, worker, producer or government making a choice."],
  ["Cost-benefit", "Comparing the benefits of a decision with its costs."],
  ["Leisure", "Time not spent working."],
  ["Investment", "Spending on capital goods."],
  ["Budget", "A plan of income and spending."],
  ["Satisfaction", "The benefit a consumer gets from a good."],
] });
labW(); 
