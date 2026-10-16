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

const FLOW = ["Trade: goods and services cross borders", "Investment: firms build factories and offices abroad (FDI)", "People: workers, students and tourists move between countries", "Ideas and technology spread quickly", "Money: capital moves between countries' financial markets", "Culture and brands become global"];
Lib.stepper($("#stF"), { w: 760, h: 400, label: "What globalisation involves", base: { n: 0 }, draw: mkChain(FLOW, "--accent"), steps: chainSteps(["<b>Trade:</b> goods and services cross borders in growing amounts.", "<b>Investment:</b> firms build factories and offices abroad (<b>FDI</b>).", "<b>People:</b> workers, students and tourists move between countries.", "<b>Ideas and technology</b> spread quickly, for example through the internet.", "<b>Money</b> moves between countries' financial markets.", "<b>Culture and brands</b> become global. Together these link the world's economies."]) });
function scChart(s) {
  const nodes = [["Design", "USA"], ["Chips", "South Korea"], ["Screen", "Japan"], ["Assembly", "China"], ["Sold", "Worldwide"]]; let o = "";
  nodes.forEach(([a, b], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 20 + i * 146, y = 130; let g = `<g opacity="${op}">` + SV.rect(x, y, 120, 90, "", { rx: 10, style: "fill:var(--accent);fill-opacity:0.15;stroke:var(--accent);stroke-width:2" }) + SV.text(x + 60, y + 38, a, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 60, y + 64, b, "sm bd", { "text-anchor": "middle", style: "font-size:14px" }); if (i < 4) g += SV.line(x + 122, y + 45, x + 142, y + 45, "ax", { style: "stroke-width:2.5" }) + SV.arrowHead(x + 144, y + 45, "r", "dot1"); o += g + "</g>"; });
  if (s.n >= 5) o += SV.text(380, 300, "One product, five stages, many countries", "lbl bd t3", { "text-anchor": "middle", style: "font-size:18px" });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 360, label: "A global supply chain", base: { n: 0 }, draw: scChart, steps: [
  { cap: "A smartphone is <b>designed</b> in one country (here the USA).", s: { n: 1 } },
  { cap: "Its <b>chips</b> are made in South Korea, where firms have the skills and technology.", s: { n: 2 } },
  { cap: "The <b>screen</b> comes from Japan.", s: { n: 3 } },
  { cap: "It is <b>assembled</b> in China, where there are many skilled workers and large factories.", s: { n: 4 } },
  { cap: "It is <b>sold worldwide</b>. Each stage is done where it is cheapest or best: this is <b>globalisation</b> in action (and also specialisation). It also means a problem in one country can disrupt the whole chain.", s: { n: 5 } },
] });
function trChart(s) {
  const d = [["1970", 26], ["1990", 39], ["2008", 61], ["2020", 52]], base = 310, k = 4.2; let o = SV.line(60, base, 710, base) + SV.text(60, 28, "World trade as a share of world GDP (%, rounded)", "sm");
  d.forEach(([y, v], i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 110 + i * 150, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 50, base - h - 8, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, y, "sm", { "text-anchor": "middle" }) + "</g>"; });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Trade has grown faster than output", base: { n: 0 }, draw: trChart, steps: [
  { cap: "In about <b>1970</b> trade (exports plus imports) was roughly a quarter of world GDP.", s: { n: 1 } },
  { cap: "By <b>1990</b> it had risen to around 39%, helped by lower tariffs and cheaper transport.", s: { n: 2 } },
  { cap: "By <b>2008</b> it peaked at around 60%: the height of globalisation, with global supply chains and big MNCs.", s: { n: 3 } },
  { cap: "In <b>2020</b> it fell back (pandemic, trade tensions) to roughly half of world GDP. Globalisation can slow or even go into reverse. Figures are approximate.", s: { n: 4 } },
] });

/* Lab 1 */
function labO() {
  if (!$("#oa") || !$("#ob") || !$("#oc")) return;
  const x = +$("#oa").value, m = +$("#ob").value, g = +$("#oc").value, open = ((x + m) / g) * 100;
  $("#oa1").textContent = money(open, 0) + "%"; $("#oa2").textContent = (x - m >= 0 ? "+" : "−") + "$" + Math.abs(x - m) + "bn"; $("#oa3").textContent = open > 100 ? "Very open" : open > 50 ? "Open" : open > 30 ? "Moderately open" : "Less open";
  $("#oav").textContent = `Trade openness = (${x} + ${m}) ÷ ${g} × 100 = ${money(open, 0)}%. ${open > 100 ? "Trade is larger than GDP: typical of small countries that trade re-exports or rely on imports, such as Singapore." : open > 50 ? "A very open economy: events abroad matter a lot." : "A larger, more self-contained economy: a bigger home market means less reliance on trade."}`;
  const base = 290; let o = SV.line(60, base, 700, base);
  [["This economy", open, "--accent"], ["Typical small open economy", 150, "--muted"], ["Typical large economy", 25, "--muted"]].forEach(([n, v, c], i) => { const h = Math.min(v, 160) * 1.5, xx = 120 + i * 190; o += SV.rect(xx, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(xx + 60, base - h - 8, money(v, 0) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(xx + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labO").innerHTML = o + SV.text(60, 24, "Exports plus imports as % of GDP", "sm");
}
Lib.slider($("#g1"), { id: "oa", label: "Exports ($bn)", min: 10, max: 300, step: 10, value: 80, fmt: (v) => "$" + v, onInput: labO });
Lib.slider($("#g2"), { id: "ob", label: "Imports ($bn)", min: 10, max: 300, step: 10, value: 90, fmt: (v) => "$" + v, onInput: labO });
Lib.slider($("#g3"), { id: "oc", label: "GDP ($bn)", min: 100, max: 1000, step: 50, value: 400, fmt: (v) => "$" + v, onInput: labO });
const FT = [
  { n: "International trade", m: "Exports and imports grow.", e: "Shops full of goods from many countries.", x: "Gains: choice, lower prices. Risks: dependence." },
  { n: "Multinational companies", m: "Firms operate in several countries.", e: "Global brands in every city.", x: "Gains: jobs, investment. Risks: profits sent abroad." },
  { n: "Foreign direct investment", m: "Firms invest in factories, offices and shops abroad.", e: "A car plant built by a foreign firm.", x: "Gains: capital, technology. Risks: control by foreigners." },
  { n: "Migration", m: "People move to work, study or settle.", e: "Doctors from abroad working in hospitals.", x: "Gains: skills, remittances. Risks: brain drain." },
  { n: "Technology and communication", m: "Internet and mobile networks link people instantly.", e: "Video calls with overseas teams.", x: "Gains: lower costs. Risks: disruption of jobs." },
  { n: "Global culture", m: "Brands, music and ideas spread.", e: "Streaming shows watched worldwide.", x: "Gains: sharing. Risks: loss of local traditions." },
];
button_table("ftBtns", "ftOut", FT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it means</th><th>Example</th><th>Gains and risks</th></tr><tr><td>${p.m}</td><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>feature of globalisation</b> or <b>not</b>?", buckets: [{ label: "Feature of globalisation" }, { label: "Not" }], items: [
  { text: "Rapid growth in international trade", b: 0 }, { text: "Firms producing in many countries", b: 0 }, { text: "Workers migrating to other countries", b: 0 }, { text: "Ideas and technology spreading quickly", b: 0 },
  { text: "A country banning all imports", b: 1 }, { text: "Firms only selling in their home town", b: 1 }, { text: "Trade falling to zero", b: 1 },
], done: "Globalisation is increasing integration of economies." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Globalisation", "Increasing connection and integration of the world's economies"],
  ["Multinational company", "A firm that operates in more than one country"],
  ["Foreign direct investment", "Investment by a firm in factories or offices abroad"],
  ["Supply chain", "The stages of production, often in different countries"],
  ["Trade openness", "Exports plus imports as a share of GDP"],
  ["Migration", "People moving from one country to another"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the stages in order: <b>a product made through a global supply chain</b>.", items: [
  "A firm designs a product in its home country",
  "Components are made in countries with skills and low costs",
  "The parts are shipped to a country where the product is assembled",
  "The finished product is exported to markets around the world",
  "Consumers in many countries buy it",
], done: "Different stages, different countries." });
Lib.calc($("#c1"), { qs: [
  { q: "Exports are $60bn and imports are $70bn in an economy with GDP of $260bn. Calculate trade openness (%).", a: 50, sol: "(60 + 70) ÷ 260 × 100 = <b>50%</b>." },
  { q: "A country's exports rise from $80bn to $100bn. What is the percentage increase?", a: 25, sol: "20 ÷ 80 × 100 = <b>25%</b>." },
  { q: "GDP is $500bn. Exports and imports together are $750bn. What is trade openness (%)?", a: 150, sol: "750 ÷ 500 × 100 = <b>150%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is globalisation?", opts: ["A fall in world trade", "Increasing integration of the world's economies", "Protection of home industries", "Trade within one country"], a: 1, why: "Increasing integration." },
  { q: "Which is a feature of globalisation?", opts: ["Fewer MNCs", "More international trade", "Fewer migrants", "More tariffs"], a: 1, why: "Trade, FDI, migration, technology." },
  { q: "A global supply chain means:", opts: ["All production in one country", "Stages of production in different countries", "No exports", "Only primary products"], a: 1, why: "Different stages in different places." },
  { q: "Which measures how open an economy is?", opts: ["GDP per head", "(Exports + imports) ÷ GDP", "Inflation", "Population"], a: 1, why: "Trade openness." },
  { q: "Foreign direct investment is:", opts: ["Buying goods from abroad", "Firms investing in factories and offices abroad", "Government aid", "Tourism"], a: 1, why: "Capital invested abroad." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Globalisation", "The increasing connection and integration of the world's economies."],
  ["Multinational company (MNC)", "A firm that operates in more than one country."],
  ["Foreign direct investment (FDI)", "Investment by firms in factories, offices or shops in other countries."],
  ["Supply chain", "The stages of production of a good, which may be in different countries."],
  ["Trade openness", "Exports plus imports as a percentage of GDP."],
  ["Migration", "People moving from one country to another."],
  ["Remittances", "Money sent home by migrants working abroad."],
  ["Offshoring", "Moving production to another country."],
  ["Global brand", "A brand sold and known worldwide."],
] });
labO(); 
