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

function mncChart(s) {
  let o = ""; const box = (x, t1, t2, c) => SV.rect(x, 70, 240, 150, "", { rx: 12, style: `fill:var(${c});fill-opacity:0.15;stroke:var(${c});stroke-width:2.5` }) + SV.text(x + 120, 105, t1, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 120, 130, t2, "sm", { "text-anchor": "middle" });
  o += box(40, "Home country", "Head office, research", "--accent") + box(480, "Host country", "Factories, shops, workers", "--good");
  const arr = (y, label, dir, op) => `<g opacity="${op}">` + SV.line(284, y, 476, y, "ax", { style: "stroke-width:3" }) + SV.arrowHead(dir === "r" ? 478 : 282, y, dir, "dot1") + SV.text(380, y - 8, label, "sm bd", { "text-anchor": "middle" }) + "</g>";
  o += arr(110, "Investment, technology", "r", clamp(s.n, 0, 1)) + arr(150, "Profits", "l", clamp(s.n - 1, 0, 1)) + arr(190, "Goods and services (exports)", "l", clamp(s.n - 2, 0, 1));
  o += `<g opacity="${clamp(s.n - 3, 0, 1)}">` + SV.text(600, 250, "Jobs, wages, skills, taxes", "lbl bd t3", { "text-anchor": "middle" }) + "</g>" + `<g opacity="${clamp(s.n - 4, 0, 1)}">` + SV.text(160, 250, "Profits, lower prices, head-office jobs", "lbl bd t3", { "text-anchor": "middle" }) + "</g>";
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 300, label: "How an MNC links two countries", base: { n: 0 }, draw: mncChart, steps: [
  { cap: "An MNC has its <b>head office in its home country</b> and factories or shops in <b>host countries</b>.", s: { n: 0.2 } },
  { cap: "It sends <b>investment and technology</b> to the host country (foreign direct investment).", s: { n: 1 } },
  { cap: "<b>Profits</b> flow back to the home country, which is a cost to the host.", s: { n: 2 } },
  { cap: "Goods and services made in the host country may be <b>exported</b> to the home country and elsewhere.", s: { n: 3 } },
  { cap: "The <b>host country</b> gains jobs, wages, skills and tax revenue.", s: { n: 4 } },
  { cap: "The <b>home country</b> gains profits, lower prices and head-office jobs, but may lose production jobs.", s: { n: 5 } },
] });
const HB = ["An MNC sets up a factory in a host country", "It hires local workers and pays wages", "Workers gain skills; the MNC buys from local suppliers", "Output, exports and tax revenue rise", "Incomes rise: spending increases and poverty may fall", "Evaluation: profits leave, wages may be low, local firms may close"];
Lib.stepper($("#stH"), { w: 760, h: 400, label: "How an MNC could reduce poverty in a host country", base: { n: 0 }, draw: mkChain(HB, "--good"), steps: chainSteps(["An MNC <b>sets up a factory</b> in a host country.", "It <b>hires local workers</b> and pays wages.", "Workers gain <b>skills</b>; the MNC buys from <b>local suppliers</b>.", "<b>Output, exports and tax revenue</b> rise.", "<b>Incomes rise</b>, spending increases and <b>poverty may fall</b>.", "<b>Evaluate:</b> profits leave, wages may be low and local firms may close."]) });
const HC = ["Costs rise in the host country (wages, taxes)", "The MNC moves production to another country", "The factory closes and workers lose their jobs", "Local suppliers lose orders", "Unemployment and poverty rise in the area", "Evaluation: the host country is dependent on 'footloose' firms"];
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Why an MNC may leave a host country", base: { n: 0 }, draw: mkChain(HC, "--bad"), steps: chainSteps(["<b>Costs rise</b> in the host country: wages, taxes, rents.", "The MNC <b>moves production</b> to another country.", "The factory <b>closes</b> and workers lose their jobs.", "<b>Local suppliers</b> lose orders.", "<b>Unemployment and poverty</b> rise in the area.", "<b>Evaluate:</b> dependence on 'footloose' MNCs is a risk for host countries."]) });

/* Lab 1: location */
const CAND = [["Country X", [9, 3, 4, 8, 4, 3], "Low wages and low taxes, but poor skills and infrastructure"], ["Country Y", [5, 7, 7, 6, 7, 7], "Balanced: reasonable costs, skills, market and stability"], ["Country Z", [2, 9, 9, 3, 9, 9], "High costs and taxes, but skilled, rich market and stable"]];
const CRIT = ["Low wages", "Skilled workers", "Market size", "Low taxes", "Stability", "Infrastructure"];
function labM() {
  const ids = ["ma", "mb", "mc", "md", "me", "mf"]; if (!ids.every((i) => $("#" + i))) return;
  const w = ids.map((i) => +$("#" + i).value), tot = w.reduce((a, b) => a + b, 0) || 1, sc = CAND.map(([n, v]) => v.reduce((a, x, i) => a + x * w[i], 0) / tot), best = sc.indexOf(Math.max(...sc));
  $("#ma1").textContent = money(sc[0], 1); $("#ma2").textContent = money(sc[1], 1); $("#ma3").textContent = money(sc[2], 1);
  $("#mav").textContent = `Weighted scores: X ${money(sc[0], 1)}, Y ${money(sc[1], 1)}, Z ${money(sc[2], 1)} out of 10. On these priorities ${CAND[best][0]} is the most attractive location (${CAND[best][2].toLowerCase()}). An MNC cutting costs would weigh wages and taxes; one seeking a market would weigh market size and skills.`;
  const base = 290; let o = SV.line(60, base, 700, base);
  CAND.forEach(([n], i) => { const x = 130 + i * 190, h = sc[i] * 22; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${i === best ? "--good" : "--muted"})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(sc[i], 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labM").innerHTML = o + SV.text(60, 24, "Weighted attractiveness to the MNC (out of 10)", "sm");
}
[["ma", "g1", "Importance of low wages", 8], ["mb", "g2", "Importance of skilled workers", 4], ["mc", "g3", "Importance of market size", 4], ["md", "g4", "Importance of low taxes", 6], ["me", "g5", "Importance of stability", 5], ["mf", "g6", "Importance of infrastructure", 5]].forEach(([id, g, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 10, step: 1, value: v, fmt: (x) => x, onInput: labM }));
const HH = [
  { n: "Host country: gains", t: "Jobs and wages; investment; technology and skills; tax revenue; exports; more choice and lower prices.", e: "Foreign car plants creating thousands of jobs." },
  { n: "Host country: costs", t: "Profits sent abroad; local firms driven out; low pay and poor conditions; pollution; footloose firms may leave.", e: "Garment factories criticised for conditions." },
  { n: "Home country: gains", t: "Profits and tax revenue; lower prices; head office and research jobs; larger markets.", e: "Profits from overseas operations returning to the headquarters country." },
  { n: "Home country: costs", t: "Production jobs lost at home; investment goes abroad; tax avoidance.", e: "Factory closures after production moves abroad." },
];
button_table("hhBtns", "hhOut", HH, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effects</th><th>Example</th></tr><tr><td>${p.t}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>benefit</b> or a <b>cost</b> of an MNC for the <b>host</b> country?", buckets: [{ label: "Benefit" }, { label: "Cost" }], items: [
  { text: "Creates jobs and wages", b: 0 }, { text: "Brings new technology and skills", b: 0 }, { text: "Pays corporation tax", b: 0 }, { text: "Raises exports", b: 0 },
  { text: "Profits are sent abroad", b: 1 }, { text: "Local firms cannot compete", b: 1 }, { text: "Pollution and resource depletion", b: 1 }, { text: "May leave when costs rise", b: 1 },
], done: "Always give both sides for the host country." });
Lib.classify($("#cl2"), { prompt: "Is each effect most relevant to the <b>host</b> country or the <b>home</b> country of an MNC?", buckets: [{ label: "Host country" }, { label: "Home country" }], items: [
  { text: "Jobs created in new factories", b: 0 }, { text: "Local suppliers gain orders", b: 0 }, { text: "Local firms driven out of business", b: 0 },
  { text: "Profits returned to shareholders", b: 1 }, { text: "Production jobs lost when factories move abroad", b: 1 }, { text: "Head-office jobs grow", b: 1 },
], done: "Do not confuse host and home countries." });
Lib.classify($("#cl3"), { prompt: "Would each make a country <b>more</b> or <b>less</b> attractive to an MNC?", buckets: [{ label: "More attractive" }, { label: "Less attractive" }], items: [
  { text: "Low corporation tax", b: 0 }, { text: "Skilled, educated workers", b: 0 }, { text: "Large and growing market", b: 0 }, { text: "Good roads, ports and internet", b: 0 },
  { text: "Political instability", b: 1 }, { text: "Corruption and poor law enforcement", b: 1 }, { text: "Poor infrastructure", b: 1 }, { text: "Very small market and few skills", b: 1 },
], done: "Costs, market, skills, infrastructure, stability." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Multinational company", "A firm that operates in more than one country"],
  ["Home country", "The country where an MNC has its head office"],
  ["Host country", "A country where an MNC has factories or shops"],
  ["Foreign direct investment", "Investment by a firm in another country"],
  ["Tax haven", "A country with very low or no taxes on firms"],
  ["Footloose firm", "A firm that can easily move production elsewhere"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how an MNC could help a host country grow</b>.", items: [
  "The MNC invests in a factory in the host country",
  "It hires local workers and trains them",
  "Output and exports rise",
  "Government tax revenue and incomes rise",
  "Spending and living standards increase",
], done: "A benefit chain." });
Lib.calc($("#c1"), { qs: [
  { q: "An MNC employs 5,000 workers in a host country at an average wage of $6,000 a year. What is the total wage bill ($m)?", a: 30, sol: "5,000 × 6,000 = <b>$30m</b>." },
  { q: "An MNC's profit in a host country is $50m and it pays 20% corporation tax. How much tax does the host government receive ($m)?", a: 10, sol: "20% × 50 = <b>$10m</b>." },
  { q: "The MNC sends 70% of its $50m profit to the home country. How much is sent ($m)?", a: 35, sol: "70% × 50 = <b>$35m</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a multinational company?", opts: ["A firm that only sells at home", "A firm that operates in more than one country", "A government firm", "A small firm"], a: 1, why: "Operates across borders." },
  { q: "A benefit of an MNC to a host country is:", opts: ["Profits sent abroad", "Jobs and investment", "Local firms closing", "Pollution"], a: 1, why: "Creating employment." },
  { q: "A disadvantage of an MNC to a host country is:", opts: ["Technology transfer", "Higher tax revenue", "Local firms may be driven out", "More exports"], a: 2, why: "Competition from large firms." },
  { q: "Which would attract an MNC to a country?", opts: ["High taxes and instability", "Skilled workers and a large market", "Poor infrastructure", "Corruption"], a: 1, why: "Skills and demand." },
  { q: "A benefit to the home country of an MNC is:", opts: ["Production jobs lost", "Profits returned and tax revenue", "Investment abroad only", "Local pollution"], a: 1, why: "Profits flow back." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Multinational company (MNC)", "A firm that operates in more than one country."],
  ["Home country", "The country where an MNC has its head office."],
  ["Host country", "A country in which an MNC operates factories, shops or offices."],
  ["Foreign direct investment (FDI)", "Investment by a firm in capital in another country."],
  ["Technology transfer", "The spread of technology and skills from an MNC to the host country."],
  ["Tax haven", "A country with low or no taxes that attracts firms."],
  ["Footloose", "Able to move production easily to other places."],
  ["Profit repatriation", "Sending profits back to the home country."],
  ["Infrastructure", "The roads, ports, energy and communications networks an economy uses."],
] });
labM(); 
