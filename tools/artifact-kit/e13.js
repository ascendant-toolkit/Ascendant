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

function ecoChart(s) {
  let o = SV.line(60, 280, 700, 280) + SV.text(60, 26, "Supply and price of a good", "sm");
  [["Sunlight", "Free good", "$0", 210, "--good"], ["Tap water in a drought", "Becomes scarce", "price rises", 130, "--warn"], ["Bottled water", "Economic good", "has a price", 90, "--accent"]].forEach(([n, t, p, h, c], i) => {
    const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 200; o += `<g opacity="${op}">` + SV.rect(x, 280 - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, 280 - h - 8, t, "sm bd", { "text-anchor": "middle" }) + SV.text(x + 60, 300, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 60, 320, p, "sm", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 340, label: "From free to economic goods", base: { n: 0 }, draw: ecoChart, steps: [
  { cap: "Sunlight is <b>not scarce</b> and uses no resources: a <b>free good</b> with no price.", s: { n: 1 } },
  { cap: "In a drought, tap water becomes <b>scarce</b>: it takes resources to supply, so it gets a price.", s: { n: 2 } },
  { cap: "Bottled water uses resources (bottles, transport, labour): an <b>economic good</b> with a price and an opportunity cost.", s: { n: 3 } },
] });
const OC = ["Resources are scarce", "Using them to make an economic good means they cannot be used for something else", "So making the good has an opportunity cost", "A free good uses no scarce resources", "So a free good has no opportunity cost"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "Opportunity cost and the two kinds of goods", base: { n: 0 }, draw: mkChain(OC, "--accent"), steps: chainSteps(["Resources are <b>scarce</b>.", "Using them to make an <b>economic good</b> means they cannot be used for something else.", "So making the good has an <b>opportunity cost</b>.", "A <b>free good</b> uses no scarce resources.", "So a free good has <b>no opportunity cost</b>."]) });

const GG = [
  { n: "Sunlight", t: "Free good", e: "Unlimited supply; no resources used." },
  { n: "Air in an open field", t: "Free good", e: "Unlimited supply; no price." },
  { n: "Rain", t: "Free good", e: "Not scarce; no resources used." },
  { n: "Bottled water", t: "Economic good", e: "Uses resources; has a price." },
  { n: "A mobile phone", t: "Economic good", e: "Scarce; uses resources." },
  { n: "A free school meal", t: "Economic good", e: "Costs resources even if free to the pupil." },
  { n: "Clean air in a polluted city", t: "Can become an economic good", e: "Cleaning air takes resources." },
];
button_table("ggBtns", "ggOut", GG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const sup = +$("#sa").value, dem = +$("#sb").value, sc = dem > sup, gap = Math.max(0, dem - sup);
  $("#sa1").textContent = sc ? "Economic good" : "Free good"; $("#sa2").textContent = gap; $("#sa3").textContent = sc ? "Yes" : "No";
  $("#sav").textContent = sc ? `At a price of zero, demand of ${dem} exceeds supply of ${sup} by ${gap}. The good is scarce, so resources are needed, it gets a price and it has an opportunity cost: an economic good.` : `At a price of zero, supply of ${sup} meets all demand of ${dem}. The good is not scarce, needs no scarce resources and has no price: a free good.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Supply", sup, "--good"], ["Demand", dem, "--bad"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * 1.8; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labS").innerHTML = o + SV.text(60, 24, "Quantity available at a price of zero", "sm");
}
Lib.slider($("#g1"), { id: "sa", label: "Supply available at zero price", min: 10, max: 150, step: 10, value: 100, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Demand at zero price", min: 10, max: 150, step: 10, value: 60, fmt: (v) => v, onInput: labS });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>economic good</b> or a <b>free good</b>?", buckets: [{ label: "Economic good" }, { label: "Free good" }], items: [
  { text: "Sunlight", b: 1 }, { text: "Air in the countryside", b: 1 }, { text: "Rain", b: 1 },
  { text: "A car", b: 0 }, { text: "Healthcare", b: 0 }, { text: "Bottled water", b: 0 }, { text: "A school lunch paid for by taxes", b: 0 },
], done: "Economic goods are scarce and have a price." });
Lib.classify($("#cl2"), { prompt: "Does each describe an <b>economic good</b> or a <b>free good</b>?", buckets: [{ label: "Economic good" }, { label: "Free good" }], items: [
  { text: "Has an opportunity cost", b: 0 }, { text: "Uses scarce resources", b: 0 }, { text: "Has a price", b: 0 },
  { text: "No opportunity cost", b: 1 }, { text: "Not scarce", b: 1 }, { text: "No price", b: 1 },
], done: "Know the differences." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Economic good", "A scarce good that uses resources and has a price"],
  ["Free good", "A good that is not scarce and has no opportunity cost"],
  ["Opportunity cost", "The next best alternative given up"],
  ["Scarcity", "Limited resources compared with unlimited wants"],
  ["Price", "What a buyer pays for an economic good"],
  ["Free of charge", "Not paid for by the user but still uses resources"],
], done: "Free goods are not the same as free-of-charge goods." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why an economic good has an opportunity cost</b>.", items: [
  "Resources are scarce",
  "Making the good uses scarce resources",
  "Those resources could have made something else",
  "The next best alternative is given up",
  "So the good has an opportunity cost",
], done: "Scarcity leads to opportunity cost." });
Lib.calc($("#c1"), { qs: [
  { q: "A farmer uses 10 hectares for wheat worth $5,000. The next best use is rice worth $4,000. What is the opportunity cost of using it for wheat ($)?", a: 4000, sol: "The next best alternative: <b>$4,000</b>." },
  { q: "A bottle of water costs $2 to produce and 100 are produced. What is the total cost ($)?", a: 200, sol: "2 × 100 = <b>$200</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is an example of a free good?", opts: ["Bottled water", "Sunlight", "A car", "Healthcare"], a: 1, why: "Not scarce, no price." },
  { q: "Economic goods:", opts: ["Are not scarce", "Have no opportunity cost", "Are scarce and have an opportunity cost", "Have no price"], a: 2, why: "They use scarce resources." },
  { q: "A free good has:", opts: ["A price", "No opportunity cost", "A high cost", "Scarce supply"], a: 1, why: "No scarce resources used." },
  { q: "A school meal paid for by taxes is:", opts: ["A free good", "An economic good", "Not scarce", "Priceless"], a: 1, why: "It uses resources." },
  { q: "Why is the basic economic problem not solved by free goods?", opts: ["They are too scarce", "They are only a small part of wants", "They cost money", "They are banned"], a: 1, why: "Most goods are economic goods." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Economic good", "A good that is scarce, uses resources, has a price and an opportunity cost."],
  ["Free good", "A good that is not scarce, so it has no price and no opportunity cost."],
  ["Scarcity", "Limited resources compared with unlimited wants."],
  ["Opportunity cost", "The next best alternative given up."],
  ["Price", "What must be paid for an economic good."],
  ["Free of charge", "Not paid for by the user, but it still uses resources."],
  ["Resources", "Land, labour, capital and enterprise."],
  ["Supply", "The quantity firms are willing to produce at each price."],
  ["Demand", "The quantity buyers are willing to buy at each price."],
] });
labS(); 
