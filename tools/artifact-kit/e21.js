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

const FC = ["Land supplies raw materials", "Labour works on them", "Capital (machines) makes the work more productive", "Enterprise organises the other three and takes the risk", "Goods and services are produced", "Owners earn rent, wages, interest and profit"];
Lib.stepper($("#stF"), { w: 760, h: 420, label: "Four factors make a product", base: { n: 0 }, draw: mkChain(FC, "--accent"), steps: chainSteps(["<b>Land</b> supplies raw materials such as timber.", "<b>Labour</b> works on them.", "<b>Capital</b> (machines and tools) makes the work more productive.", "<b>Enterprise</b> organises the other three and takes the risk.", "<b>Goods and services</b> are produced and sold.", "Owners of the factors earn <b>rent, wages, interest and profit</b>."]) });
function bakeChart(s) {
  const items = [["Land", "Flour from wheat fields", "--good"], ["Labour", "Bakers", "--accent"], ["Capital", "Ovens, mixers", "--warn"], ["Enterprise", "Owner who risks money", "--bad"]]; let o = SV.text(60, 26, "A bakery", "sm");
  items.forEach(([n, d, c], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 60 + i * 170; o += `<g opacity="${op}">` + SV.rect(x, 60, 150, 90, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, 100, n, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:16px" }) + SV.text(x + 75, 125, d, "sm", { "text-anchor": "middle", style: "fill:#fff;font-size:11px" }) + SV.text(x + 75, 190, ["Rent", "Wages", "Interest", "Profit"][i], "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, 210, "is the reward", "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 240, label: "A bakery's factors and rewards", base: { n: 0 }, draw: bakeChart, steps: [
  { cap: "<b>Land:</b> the wheat fields that supply flour. Reward: <b>rent</b>.", s: { n: 1 } },
  { cap: "<b>Labour:</b> bakers. Reward: <b>wages</b>.", s: { n: 2 } },
  { cap: "<b>Capital:</b> ovens and mixers. Reward: <b>interest</b>.", s: { n: 3 } },
  { cap: "<b>Enterprise:</b> the owner who organises and risks money. Reward: <b>profit</b>.", s: { n: 4 } },
] });

/* Lab 1: income shares */
function labR() {
  if (!$("#ra") || !$("#rb") || !$("#rc") || !$("#rd")) return;
  const v = [+$("#ra").value, +$("#rb").value, +$("#rc").value, +$("#rd").value], tot = v.reduce((a, b) => a + b, 0), nm = ["Rent (land)", "Wages (labour)", "Interest (capital)", "Profit (enterprise)"], cl = ["--good", "--accent", "--warn", "--bad"];
  $("#ra1").textContent = "$" + tot; $("#ra2").textContent = money(tot ? (v[1] / tot) * 100 : 0, 0) + "%"; $("#ra3").textContent = nm[v.indexOf(Math.max(...v))].split(" ")[0];
  $("#rav").textContent = `A firm sells $${tot} of output and shares it between the factors: rent $${v[0]}, wages $${v[1]}, interest $${v[2]}, profit $${v[3]}. Wages take ${money(tot ? (v[1] / tot) * 100 : 0, 0)}% of the total. The more a firm pays one factor, the less is left for the others (scarcity again).`;
  const base = 280, k = 200 / Math.max(...v, 1); let o = SV.line(60, base, 700, base);
  v.forEach((x, i) => { const px = 100 + i * 150, h = x * k; o += SV.rect(px, base - h, 110, h, "", { style: `fill:var(${cl[i]})`, opacity: 0.85 }) + SV.text(px + 55, base - h - 8, "$" + x, "lbl bd", { "text-anchor": "middle" }) + SV.text(px + 55, base + 20, nm[i], "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labR").innerHTML = o;
}
[["g1", "ra", "Rent paid to landowners", 10], ["g2", "rb", "Wages paid to workers", 50], ["g3", "rc", "Interest paid on capital", 15], ["g4", "rd", "Profit kept by the entrepreneur", 25]].forEach(([g, id, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 100, step: 5, value: v, fmt: (x) => "$" + x, onInput: labR }));
const FF = [
  { n: "A farm field", f: "Land", r: "Rent" }, { n: "A teacher", f: "Labour", r: "Wages" }, { n: "A delivery lorry", f: "Capital", r: "Interest" },
  { n: "A person who starts a café and risks savings", f: "Enterprise", r: "Profit" }, { n: "An oil well", f: "Land", r: "Rent" }, { n: "A computer in an office", f: "Capital", r: "Interest" },
];
button_table("ffBtns", "ffOut", FF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Factor</th><th>Reward</th></tr><tr><td><b>${p.f}</b></td><td>${p.r}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>factor of production</b> is each?", buckets: [{ label: "Land" }, { label: "Labour" }, { label: "Capital" }, { label: "Enterprise" }], items: [
  { text: "A copper mine", b: 0 }, { text: "A forest", b: 0 },
  { text: "A nurse", b: 1 }, { text: "A builder", b: 1 },
  { text: "A factory machine", b: 2 }, { text: "A tractor", b: 2 },
  { text: "An entrepreneur starting a business", b: 3 }, { text: "Taking the risk of a new product", b: 3 },
], done: "Land, labour, capital, enterprise." });
Lib.match($("#m1"), { prompt: "Match each factor to its reward.", pairs: [
  ["Land", "Rent"], ["Labour", "Wages"], ["Capital", "Interest"], ["Enterprise", "Profit"],
  ["Financial capital", "Money used to buy machinery"], ["Physical capital", "Machines used to make goods"],
], done: "Learn all four pairs." });
Lib.classify($("#cl2"), { prompt: "Which <b>reward</b> goes to the owner of each?", buckets: [{ label: "Rent" }, { label: "Wages" }, { label: "Interest" }, { label: "Profit" }], items: [
  { text: "A landowner leasing a field", b: 0 }, { text: "A worker's monthly pay", b: 1 }, { text: "A firm's machines (capital)", b: 2 }, { text: "The risk-taking owner of a business", b: 3 },
  { text: "A farm leased to a farmer", b: 0 }, { text: "A salary", b: 1 },
], done: "Reward follows the factor." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how factors of production earn incomes</b>.", items: [
  "Firms combine land, labour, capital and enterprise",
  "Goods and services are produced and sold",
  "Revenue is earned by the firm",
  "The firm pays rent, wages and interest",
  "The entrepreneur keeps the profit",
], done: "Revenue is shared between the factors." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm earns $500,000 revenue and pays $100,000 wages, $50,000 rent and $30,000 interest. Ignoring other costs, what is profit ($)?", a: 320000, sol: "500,000 − 100,000 − 50,000 − 30,000 = <b>$320,000</b>." },
  { q: "Wages are $60,000 of a firm's $200,000 costs. What percentage is this?", a: 30, sol: "60 ÷ 200 × 100 = <b>30%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the reward to capital?", opts: ["Rent", "Wages", "Interest", "Profit"], a: 2, why: "Capital earns interest." },
  { q: "What is the reward to enterprise?", opts: ["Rent", "Wages", "Interest", "Profit"], a: 3, why: "A reward for risk-taking." },
  { q: "Which is an example of land?", opts: ["A factory", "Oil reserves", "A worker", "Money"], a: 1, why: "A natural resource." },
  { q: "Which is an example of capital?", opts: ["A forest", "A tractor", "A manager's effort", "Fish in the sea"], a: 1, why: "Man-made, used to produce." },
  { q: "Labour is rewarded with:", opts: ["Rent", "Wages", "Interest", "Profit"], a: 1, why: "Wages." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Factors of production", "The resources used to produce goods and services: land, labour, capital and enterprise."],
  ["Land", "All natural resources."],
  ["Labour", "The physical and mental effort of people in production."],
  ["Capital", "Man-made goods used to produce other goods and services."],
  ["Enterprise", "Organising the factors of production and taking risks."],
  ["Rent", "The reward for land."],
  ["Wages", "The reward for labour."],
  ["Interest", "The reward for capital."],
  ["Profit", "The reward for enterprise."],
] });
labR(); 
