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

const QS = ["Scarce resources must be allocated", "WHAT to produce: which goods and services, and how many", "HOW to produce: which methods, technology and resource mix", "WHO to produce for: who gets the output", "Each answer has an opportunity cost"];
Lib.stepper($("#stQ"), { w: 760, h: 380, label: "The three questions", base: { n: 0 }, draw: mkChain(QS, "--accent"), steps: chainSteps(["Because of scarcity, resources must be <b>allocated</b>.", "<b>What</b> to produce: which goods and services, and how many.", "<b>How</b> to produce: which methods, technology and resource mix.", "<b>Who</b> to produce for: who gets the output.", "Each answer has an <b>opportunity cost</b>."]) });
const MK = ["Consumers spend more on a product", "Its price and profit rise", "Firms switch resources into making it", "Resources move out of less profitable goods", "The market has answered WHAT to produce"];
Lib.stepper($("#stM"), { w: 760, h: 380, label: "How the market answers what to produce", base: { n: 0 }, draw: mkChain(MK, "--good"), steps: chainSteps(["<b>Consumers spend more</b> on a product.", "Its <b>price and profit rise</b>.", "Firms <b>switch resources</b> into making it.", "Resources <b>move out</b> of less profitable goods.", "The market has answered <b>what to produce</b>."]) });

/* Lab 1: sort decisions */
const DQ = [
  { n: "A farmer chooses wheat rather than rice", q: "What to produce", e: "A choice of output." },
  { n: "A factory installs robots instead of hiring workers", q: "How to produce", e: "A choice of production method." },
  { n: "A government gives free school meals to poor children", q: "Who to produce for", e: "A decision on who receives output." },
  { n: "A car firm makes electric rather than petrol cars", q: "What to produce", e: "A choice of output." },
  { n: "A firm uses solar rather than coal power", q: "How to produce", e: "A choice of method and resources." },
  { n: "A shop stocks luxury goods for high-income customers", q: "Who to produce for", e: "A decision on the target market." },
];
button_table("dqBtns", "dqOut", DQ, 0, (p) => `<div class="tw"><table class="t"><tr><th>Basic question</th><th>Why</th></tr><tr><td><b>${p.q}</b></td><td>${p.e}</td></tr></table></div>`);
function labW() {
  if (!$("#wa")) return;
  const l = +$("#wa").value, k = 100 - l, cost = l * 8 + k * 14, out = l * 6 + k * 12;
  $("#wa1").textContent = "$" + cost; $("#wa2").textContent = out; $("#wa3").textContent = "$" + money(cost / out, 2);
  $("#wav").textContent = `${l}% labour and ${k}% capital: cost $${cost}, output ${out}, cost per unit $${money(cost / out, 2)}. Choosing HOW to produce is a trade-off between labour-intensive and capital-intensive methods (illustrative figures).`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Labour share", l, "--warn"], ["Capital share", k, "--accent"]].forEach(([n, v, cl], i) => { const x = 160 + i * 250, h = v * 2.2; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${cl})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Share of production using labour", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labW });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>basic economic question</b> is each decision?", buckets: [{ label: "What to produce" }, { label: "How to produce" }, { label: "Who to produce for" }], items: [
  { text: "Wheat or rice?", b: 0 }, { text: "More hospitals or more roads?", b: 0 },
  { text: "Robots or workers?", b: 1 }, { text: "Which technology and location to use", b: 1 },
  { text: "Goods for the rich or for the poor?", b: 2 }, { text: "Export or home market?", b: 2 },
], done: "What, how, who." });
Lib.classify($("#cl2"), { prompt: "Who answers the questions in each system?", buckets: [{ label: "The market" }, { label: "The government" }, { label: "Both" }], items: [
  { text: "Consumers' spending and firms' profit", b: 0 }, { text: "Prices act as signals", b: 0 },
  { text: "Planners set output targets", b: 1 }, { text: "State-owned firms follow instructions", b: 1 },
  { text: "Private firms and public services together", b: 2 }, { text: "A mixed economy", b: 2 },
], done: "Market, planned or mixed." });
Lib.match($("#m1"), { prompt: "Match the question to the example.", pairs: [
  ["What to produce", "Solar panels or coal"],
  ["How to produce", "Machines or hand tools"],
  ["Who to produce for", "Luxury goods or basic goods"],
  ["Resource allocation", "Dividing scarce resources between uses"],
  ["Market economy", "Prices and profits decide"],
  ["Planned economy", "The government decides"],
], done: "Link each question to an example." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the market decides what to produce</b>.", items: [
  "Consumers demand more of a good",
  "Its price and profit rise",
  "Firms move resources into producing it",
  "Output of the good rises",
  "Resources move away from goods in less demand",
], done: "A market chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm can use 60 workers at $100 each a day, or 10 machines at $500 each a day. How much cheaper per day is the machine method ($)?", a: 1000, sol: "Workers: 60 × 100 = $6,000. Machines: 10 × 500 = $5,000. Difference <b>$1,000</b>." },
  { q: "A country has 50% of its resources in farming and 30% in manufacturing. What percentage is left for services?", a: 20, sol: "100 − 50 − 30 = <b>20%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a 'how to produce' decision?", opts: ["Making cars or bikes", "Using robots or workers", "Selling to rich or poor", "Wheat or rice"], a: 1, why: "Choice of method." },
  { q: "Deciding to make more healthcare and less military equipment answers:", opts: ["How to produce", "What to produce", "Who to produce for", "None"], a: 1, why: "A choice of output." },
  { q: "Who to produce for is about:", opts: ["Methods", "How output is distributed", "Quantity of output", "Prices only"], a: 1, why: "Distribution." },
  { q: "The three questions arise because of:", opts: ["Inflation", "Scarcity", "Unemployment", "Trade"], a: 1, why: "Limited resources." },
  { q: "In a market economy the questions are answered mainly by:", opts: ["Planners", "Consumers and firms through prices", "Courts", "Banks only"], a: 1, why: "The price mechanism." },
] });

Lib.cards($("#fc1"), { cards: [
  ["What to produce", "The decision on which goods and services to make and how many."],
  ["How to produce", "The decision on the methods and resources used."],
  ["Who to produce for", "The decision on who receives the output."],
  ["Resource allocation", "Dividing scarce resources between competing uses."],
  ["Market economy", "An economy where prices and profits decide."],
  ["Planned economy", "An economy where the government decides."],
  ["Mixed economy", "An economy with both private and public decision-making."],
  ["Labour-intensive", "Production that uses relatively more labour than capital."],
  ["Capital-intensive", "Production that uses relatively more capital than labour."],
] });
labW(); 
