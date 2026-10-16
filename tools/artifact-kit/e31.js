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

const OP = ["Resources are scarce", "A choice must be made between alternatives", "One option is chosen", "The next best alternative is given up", "That is the opportunity cost"];
Lib.stepper($("#stO"), { w: 760, h: 380, label: "From scarcity to opportunity cost", base: { n: 0 }, draw: mkChain(OP, "--accent"), steps: chainSteps(["Resources are <b>scarce</b>.", "A <b>choice</b> must be made between alternatives.", "<b>One option</b> is chosen.", "The <b>next best alternative</b> is given up.", "That is the <b>opportunity cost</b>."]) });
function rankChart(s) {
  const opts = [["Concert", 1], ["Trainers", 2], ["Meal out", 3]]; let o = SV.text(60, 26, "You have $50 and can do one thing", "sm");
  opts.forEach(([n, r], i) => { const x = 80 + i * 210, chosen = s.n >= 1 && r === 1, oc = s.n >= 2 && r === 2, lost = s.n >= 3 && r === 3; const c = chosen ? "--good" : oc ? "--bad" : "--accent", op = lost ? 0.35 : 0.85; o += SV.rect(x, 60, 180, 110, "", { style: `fill:var(${c})`, opacity: op }) + SV.text(x + 90, 105, n, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:16px" }) + SV.text(x + 90, 130, "Rank " + r, "sm", { "text-anchor": "middle", style: "fill:#fff" }) + (chosen ? SV.text(x + 90, 200, "CHOSEN", "lbl bd t3", { "text-anchor": "middle" }) : "") + (oc ? SV.text(x + 90, 200, "OPPORTUNITY COST", "lbl bd t2", { "text-anchor": "middle", style: "font-size:12px" }) : "") + (lost ? SV.text(x + 90, 200, "also given up, but not the cost", "sm", { "text-anchor": "middle", style: "font-size:11px" }) : ""); });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 240, label: "Ranking the alternatives", base: { n: 0 }, draw: rankChart, steps: [
  { cap: "You rank three options for your $50: concert, trainers, meal out.", s: { n: 0 } },
  { cap: "You choose the <b>concert</b> (your first choice).", s: { n: 1 } },
  { cap: "The <b>opportunity cost</b> is your second choice only: the <b>trainers</b>.", s: { n: 2 } },
  { cap: "The meal out is also not bought, but it is <b>not</b> the opportunity cost: only the next best alternative counts.", s: { n: 3 } },
] });

/* Lab 1: choose */
const OPTS = [["Concert tickets", 7], ["New trainers", 8], ["Meal out", 5], ["Save the money", 4]];
function labO() {
  if (!$("#oa")) return;
  const i = +$("#oa").value, chosen = OPTS[i], rest = OPTS.filter((_, j) => j !== i).sort((a, b) => b[1] - a[1]), nb = rest[0];
  $("#oa1").textContent = chosen[0]; $("#oa2").textContent = nb[0]; $("#oa3").textContent = nb[1] + " / 10";
  $("#oav").textContent = `You choose ${chosen[0]} (value ${chosen[1]}/10 to you). The alternatives ranked by value are ${rest.map((r) => r[0] + " " + r[1]).join(", ")}. The opportunity cost is the best of them: ${nb[0]}. Choose a different option and the opportunity cost can change.`;
  const base = 280; let o = SV.line(60, base, 700, base);
  OPTS.forEach(([n, v], j) => { const x = 90 + j * 150, h = v * 22, c = j === i ? "--good" : n === nb[0] ? "--bad" : "--accent"; o += SV.rect(x, base - h, 110, h, "", { style: `fill:var(${c})`, opacity: j === i || n === nb[0] ? 0.9 : 0.4 }) + SV.text(x + 55, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 55, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labO").innerHTML = o + SV.text(60, 24, "Green: chosen. Red: opportunity cost.", "sm");
}
Lib.slider($("#g1"), { id: "oa", label: "Choose an option (0 to 3)", min: 0, max: 3, step: 1, value: 0, fmt: (v) => OPTS[v][0], onInput: labO });
const OE = [
  { n: "A student studies instead of working a part-time job", c: "The wages from the job" },
  { n: "A government builds a road", c: "The hospital or school that could have been built" },
  { n: "A farmer grows wheat on a field", c: "The next best crop (e.g. barley)" },
  { n: "A firm buys a new machine", c: "The next best use of the money (e.g. advertising)" },
  { n: "A person takes a two-year apprenticeship", c: "The wages from a full-time job over the two years" },
  { n: "A country makes more weapons", c: "The consumer goods given up" },
];
button_table("oeBtns", "oeOut", OE, 0, (p) => `<div class="tw"><table class="t"><tr><th>Opportunity cost</th></tr><tr><td><b>${p.c}</b></td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> faces each opportunity cost?", buckets: [{ label: "Consumer" }, { label: "Worker" }, { label: "Firm" }, { label: "Government" }], items: [
  { text: "The trainers given up to buy a game", b: 0 }, { text: "The meal out given up for concert tickets", b: 0 },
  { text: "Wages lost while doing an apprenticeship", b: 1 }, { text: "Leisure given up for overtime", b: 1 },
  { text: "Advertising given up for new machinery", b: 2 }, { text: "The next best crop on a farm", b: 2 },
  { text: "Schools given up to build roads", b: 3 }, { text: "Hospitals given up to fund defence", b: 3 },
], done: "Everyone gives up the next best alternative." });
Lib.classify($("#cl2"), { prompt: "Does each have an <b>opportunity cost</b>?", buckets: [{ label: "Has an opportunity cost" }, { label: "No opportunity cost" }], items: [
  { text: "Building a hospital", b: 0 }, { text: "Buying a phone", b: 0 }, { text: "Studying for a degree", b: 0 }, { text: "Using a field for wheat", b: 0 },
  { text: "Enjoying sunshine", b: 1 }, { text: "Breathing fresh air in the open", b: 1 }, { text: "Rain falling on a garden", b: 1 },
], done: "Only free goods have no opportunity cost." });
Lib.match($("#m1"), { prompt: "Match the choice to its opportunity cost.", pairs: [
  ["Going to university", "Wages from a job"],
  ["Building a road", "A hospital"],
  ["Growing apples", "The next best crop"],
  ["Producing consumer goods", "Capital goods given up"],
  ["Using leisure time to cycle", "Studying or earning"],
  ["A free good", "No opportunity cost"],
], done: "Learn these examples." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>working out an opportunity cost</b>.", items: [
  "List the alternatives",
  "Rank them from best to worst",
  "Choose the best",
  "The second best is given up",
  "That second best is the opportunity cost",
], done: "The next best alternative." });
Lib.calc($("#c1"), { qs: [
  { q: "You have $20 and can buy a book ($20), a cinema ticket ($20) or two snacks ($20). You choose the cinema and your next best is the book. What is the opportunity cost?", a: 1, sol: "<b>One book</b>: the next best alternative." },
  { q: "A farmer can grow 40 tonnes of wheat or 30 tonnes of barley on a field. If wheat is grown, how many tonnes of barley are given up?", a: 30, sol: "<b>30 tonnes</b> of barley." },
  { q: "An apprenticeship lasts 2 years. A full-time job would pay $15,000 a year. What wages are given up ($)?", a: 30000, sol: "2 × 15,000 = <b>$30,000</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Opportunity cost is:", opts: ["The money price", "The next best alternative given up", "All alternatives given up", "The first choice"], a: 1, why: "Only the next best." },
  { q: "What is the opportunity cost of building a road?", opts: ["The cost of materials only", "Another project that could have been funded", "Nothing", "The road itself"], a: 1, why: "Resources used elsewhere." },
  { q: "Which has no opportunity cost?", opts: ["A free good", "A car", "Healthcare", "A house"], a: 0, why: "Free goods." },
  { q: "A worker doing a 2-year apprenticeship gives up:", opts: ["Nothing", "Wages from a job", "Leisure only", "All jobs"], a: 1, why: "Lost earnings." },
  { q: "Opportunity cost exists because:", opts: ["Wants are limited", "Resources are scarce", "Money exists", "Taxes exist"], a: 1, why: "Scarcity forces choice." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Opportunity cost", "The next best alternative given up when a choice is made."],
  ["Choice", "Selecting between alternatives."],
  ["Scarcity", "Limited resources compared with unlimited wants."],
  ["Trade-off", "Giving up one thing to get another."],
  ["Alternative", "Another option that could have been chosen."],
  ["Free good", "A good with no opportunity cost because it is not scarce."],
  ["Economic good", "A scarce good that uses resources."],
  ["Apprenticeship", "Paid work with training, usually lasting a few years."],
  ["Resource allocation", "How scarce resources are shared between uses."],
] });
labO(); 
