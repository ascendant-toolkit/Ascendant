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

const trade = (o) => {
  const pw = o.pw ?? 40, t = o.t || 0, sub = o.sub || 0; let P = pw, mode = "free";
  if (o.emb && pw < 60) { P = 60; mode = "embargo"; }
  else if (o.q !== undefined && o.q !== null && (110 - pw) - (pw - 10) > o.q) { P = (120 - o.q) / 2; mode = "quota"; }
  else if (t > 0) { P = Math.min(pw + t, 60); mode = "tariff"; }
  const qs = P - 10 + (mode === "free" ? sub : 0), qd = 110 - P, imp = mode === "embargo" ? 0 : Math.max(0, qd - qs);
  return { P, qs, qd, imp, mode, rev: mode === "tariff" ? (P - pw) * imp : 0, cost: mode === "free" ? sub * qs : 0, rent: mode === "quota" ? (P - pw) * imp : 0 };
};
function tmChart(o) {
  const r = trade(o), pw = o.pw ?? 40; let s = axes("Price", "Quantity") + curve(-1, 110, "c1", "Demand", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Domestic supply", { t: "t3", dx: -125, dy: 16 });
  if (o.sub) s += curve(1, 10 - o.sub, "c2") + SV.text(QX(30), PY(30 - o.sub) + 30, "Supply + subsidy", "lbl bd t2");
  s += SV.line(QX(0), PY(pw), QX(100), PY(pw), "c4", { "stroke-width": 2.5 }) + SV.text(QX(100), PY(pw) + 18, "World price $" + Math.round(pw), "lbl bd t4", { "text-anchor": "end" });
  if (r.mode === "tariff" || r.mode === "quota" || r.mode === "embargo") {
    if (r.mode === "tariff" && r.imp > 0.5) s += SV.rect(QX(r.qs), PY(r.P), QX(r.qd) - QX(r.qs), PY(pw) - PY(r.P), "", { style: "fill:var(--good);fill-opacity:0.35" }) + SV.text(QX((r.qs + r.qd) / 2), PY((r.P + pw) / 2) + 4, "Revenue", "sm bd", { "text-anchor": "middle" });
    s += SV.line(QX(0), PY(r.P), QX(r.qd), PY(r.P), "gr", { style: "stroke-dasharray:5 4" }) + SV.text(QX(0) - 8, PY(r.P) + 4, "$" + money(r.P, 0), "sm bd", { "text-anchor": "end" });
  }
  s += SV.line(QX(r.qs), PY(Math.max(pw, r.P)), QX(r.qs), PY(0), "gr") + SV.line(QX(r.qd), PY(r.P), QX(r.qd), PY(0), "gr") + SV.circle(QX(r.qs), PY(r.P), 6, "dot2") + SV.circle(QX(r.qd), PY(r.P), 6, "dot2") + SV.text(QX(r.qs), PY(0) + 18, "Qs " + Math.round(r.qs), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(r.qd), PY(0) + 18, "Qd " + Math.round(r.qd), "sm bd", { "text-anchor": "middle" });
  if (r.imp > 0.5) s += SV.text(QX((r.qs + r.qd) / 2), PY(r.P) - 28, "Imports " + Math.round(r.imp), "lbl bd t2", { "text-anchor": "middle", style: halo });
  return s;
}

Lib.stepper($("#stT"), { w: 760, h: 400, label: "A tariff on imports", base: { pw: 40, t: 0 }, draw: tmChart, steps: [
  { cap: "With <b>free trade</b> the world price is $40. Domestic firms supply <b>30</b>, consumers buy <b>70</b> and <b>40</b> is imported.", s: { pw: 40, t: 0 } },
  { cap: "The government puts a <b>$10 tariff</b> on imports. Imported goods now cost <b>$50</b> in the shops.", s: { pw: 40, t: 10 } },
  { cap: "<b>Domestic output rises</b> to 40, <b>consumers buy less</b> (60) at the higher price, and <b>imports fall</b> to 20. The green box is <b>tariff revenue</b> ($10 × 20 = $200).", s: { pw: 40, t: 10 } },
  { cap: "<b>Evaluate:</b> domestic producers and the government gain. Consumers lose (higher price, less choice). Other countries may retaliate.", s: { pw: 40, t: 10 } },
] });
Lib.stepper($("#stQ"), { w: 760, h: 400, label: "An import quota", base: { pw: 40, q: 100 }, draw: tmChart, steps: [
  { cap: "With free trade, <b>40</b> units are imported at $40.", s: { pw: 40, q: 100 } },
  { cap: "The government sets an <b>import quota of 20 units</b>: no more than 20 can be imported.", s: { pw: 40, q: 20 } },
  { cap: "Supply falls, so the <b>price rises to $50</b>. Domestic firms supply 40 and consumers buy 60. The effect on price is like a tariff, but <b>there is no tax revenue</b>: the extra $10 goes to the importers who hold the licences.", s: { pw: 40, q: 20 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "A subsidy to domestic producers", base: { pw: 40, sub: 0 }, draw: tmChart, steps: [
  { cap: "The world price is $40. Domestic firms supply <b>30</b> and <b>40</b> is imported.", s: { pw: 40, sub: 0 } },
  { cap: "The government gives domestic producers a <b>$10 subsidy per unit</b>. Their costs fall: <b>supply shifts right</b>.", s: { pw: 40, sub: 10 } },
  { cap: "At the world price, domestic firms now supply <b>40</b> instead of 30, so <b>imports fall</b> to 30. Consumers still pay $40. The <b>cost to taxpayers is $10 × 40 = $400</b>.", s: { pw: 40, sub: 10 } },
] });
Lib.stepper($("#stE"), { w: 760, h: 400, label: "An embargo", base: { pw: 40, emb: 0 }, draw: (s) => tmChart({ pw: 40, emb: s.emb > 0.5 }), steps: [
  { cap: "With free trade the good is imported at <b>$40</b> and consumers buy <b>70</b>.", s: { emb: 0 } },
  { cap: "An <b>embargo bans imports</b> of the good. Only domestic firms can supply it.", s: { emb: 1 } },
  { cap: "The price rises to <b>$60</b>, consumers buy only <b>50</b> and all of it is domestic. Producers gain; consumers lose choice and pay more.", s: { emb: 1 } },
] });

/* Lab 1: tariff */
function labT() {
  if (!$("#ta")) return; const t = +$("#ta").value, r = trade({ pw: 40, t });
  $("#ta1").textContent = "$" + money(r.P, 0); $("#ta2").textContent = Math.round(r.imp); $("#ta3").textContent = "$" + money(r.rev, 0);
  $("#tav").textContent = t === 0 ? "No tariff: free trade at $40." : `A $${t} tariff raises the price to $${money(r.P, 0)}. Domestic output rises to ${Math.round(r.qs)}, consumers buy ${Math.round(r.qd)}, imports fall to ${Math.round(r.imp)} and the government collects $${money(r.rev, 0)}. ${r.P >= 60 ? "The tariff is so high that imports stop: it acts like an embargo." : ""}`;
  $("#labT").innerHTML = tmChart({ pw: 40, t });
}
Lib.slider($("#g1"), { id: "ta", label: "Tariff per unit", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labT });
function labQ() {
  if (!$("#qa")) return; const q = +$("#qa").value, r = trade({ pw: 40, q });
  $("#qa1").textContent = "$" + money(r.P, 0); $("#qa2").textContent = Math.round(r.imp); $("#qa3").textContent = "$" + money(r.rent, 0);
  $("#qav").textContent = q >= 40 ? "A quota of 40 or more does not limit imports: free trade imports are already 40." : `Limiting imports to ${q} raises the price to $${money(r.P, 0)}. Domestic firms supply ${Math.round(r.qs)} and consumers buy ${Math.round(r.qd)}. The extra $${money(r.P - 40, 0)} per unit on ${q} units ($${money(r.rent, 0)}) goes to importers, not the government.`;
  $("#labQ").innerHTML = tmChart({ pw: 40, q });
}
Lib.slider($("#g2"), { id: "qa", label: "Import quota (units)", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labQ });
function labS() {
  if (!$("#sa")) return; const sub = +$("#sa").value, r = trade({ pw: 40, sub });
  $("#sa1").textContent = Math.round(r.qs); $("#sa2").textContent = Math.round(r.imp); $("#sa3").textContent = "$" + money(r.cost, 0);
  $("#sav").textContent = sub === 0 ? "No subsidy." : `With a $${sub} subsidy domestic firms supply ${Math.round(r.qs)} at the $40 world price, so imports fall to ${Math.round(r.imp)}. Consumers still pay $40. The cost to taxpayers is $${money(r.cost, 0)}.`;
  $("#labS").innerHTML = tmChart({ pw: 40, sub });
}
Lib.slider($("#g3"), { id: "sa", label: "Subsidy per unit", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labS });
const MT = [
  { n: "Tariff", w: "A tax on imports: raises their price.", a: "Revenue for the government; protects domestic producers.", d: "Higher prices for consumers; retaliation; cost to firms using imported inputs." },
  { n: "Import quota", w: "A limit on the quantity imported.", a: "Guarantees a ceiling on imports; protects domestic producers.", d: "No tax revenue; higher prices; may encourage smuggling." },
  { n: "Subsidy", w: "Payment to domestic producers lowering their costs.", a: "Lower prices and more output; no price rise for consumers.", d: "Cost to taxpayers; inefficiency; may breach trade rules." },
  { n: "Embargo", w: "A ban on trade with a country or product.", a: "Total protection; can be a political tool.", d: "Higher prices, less choice, retaliation; trading partner's exports lost." },
  { n: "Other non-tariff barriers", w: "Regulations, standards, red tape, exchange controls.", a: "Protect consumers and industries; hard to challenge.", d: "Costly for foreign firms; may be hidden protection." },
];
button_table("mtBtns", "mtOut", MT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it is</th><th>Advantages</th><th>Disadvantages</th></tr><tr><td>${p.w}</td><td>${p.a}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>method of protection</b> is each?", buckets: [{ label: "Tariff" }, { label: "Import quota" }, { label: "Subsidy" }, { label: "Embargo" }], items: [
  { text: "A 15% tax on imported cars", b: 0 }, { text: "A customs duty on imported steel", b: 0 },
  { text: "No more than 10,000 tonnes of sugar may be imported", b: 1 }, { text: "A limit on imported textiles", b: 1 },
  { text: "Government pays domestic farmers $50 per tonne", b: 2 }, { text: "Grants to domestic car makers", b: 2 },
  { text: "A complete ban on imports from one country", b: 3 }, { text: "Trade with a country is prohibited", b: 3 },
], done: "Tax, limit, payment, ban." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>tariff barrier</b> or a <b>non-tariff barrier</b>?", buckets: [{ label: "Tariff barrier" }, { label: "Non-tariff barrier" }], items: [
  { text: "A tax on imports", b: 0 }, { text: "Customs duty", b: 0 },
  { text: "Quota", b: 1 }, { text: "Subsidy", b: 1 }, { text: "Embargo", b: 1 }, { text: "Complicated customs paperwork", b: 1 }, { text: "Safety and labelling rules aimed at imports", b: 1 },
], done: "Only a tariff is a tax on imports." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Tariff", "A tax on imports"],
  ["Import quota", "A limit on the quantity of imports"],
  ["Subsidy", "A payment by the government to producers to lower their costs"],
  ["Embargo", "A ban on trade with a country or product"],
  ["Protection", "Measures to protect domestic producers from foreign competition"],
  ["Customs duty", "Another word for a tariff"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a tariff protects domestic producers</b>.", items: [
  "The government puts a tax on imports",
  "Imported goods become more expensive",
  "Consumers buy fewer imports and more domestic goods",
  "Domestic firms sell more and may expand",
  "Employment in the industry may rise",
], done: "A tariff chain." });
Lib.calc($("#c1"), { qs: [
  { q: "The world price is $40 and a 25% tariff is applied. What is the price of the imported good ($)?", a: 50, sol: "40 × 1.25 = <b>$50</b>." },
  { q: "A tariff of $10 is paid on 20 imported units. How much revenue does the government collect ($)?", a: 200, sol: "10 × 20 = <b>$200</b>." },
  { q: "A government pays a subsidy of $8 per unit on 500 units. What does it cost ($)?", a: 4000, sol: "8 × 500 = <b>$4,000</b>." },
  { q: "A quota cuts imports from 40 to 20 units. By what percentage did imports fall?", a: 50, sol: "20 ÷ 40 × 100 = <b>50%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a tariff?", opts: ["A limit on imports", "A tax on imports", "A payment to producers", "A ban on trade"], a: 1, why: "A tariff is a tax on imports." },
  { q: "An import quota is:", opts: ["A tax on imports", "A limit on the quantity of imports", "A subsidy", "A free trade area"], a: 1, why: "A quantity limit." },
  { q: "A subsidy to domestic producers is most likely to:", opts: ["Raise their costs", "Lower their costs so they supply more", "Reduce output", "Raise import prices"], a: 1, why: "Supply shifts right." },
  { q: "Which is a non-tariff method of protection?", opts: ["Customs duty", "Import tariff", "Import quota", "VAT"], a: 2, why: "Quotas are non-tariff." },
  { q: "An embargo is:", opts: ["A tax on exports", "A ban on trade with a country or product", "A limit on imports", "A subsidy"], a: 1, why: "Total ban." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Protection", "Measures used to protect domestic producers from foreign competition."],
  ["Tariff", "A tax on imports (or exports) that raises their price."],
  ["Import quota", "A limit on the quantity of a good that can be imported."],
  ["Subsidy", "A payment by the government to producers to lower their costs."],
  ["Embargo", "A ban on trade with a particular country or in a particular product."],
  ["Tariff barrier", "A barrier to trade in the form of a tax."],
  ["Non-tariff barrier", "A barrier to trade that is not a tax, such as a quota or regulations."],
  ["Customs duty", "A tax on goods crossing a border."],
  ["Red tape", "Bureaucratic rules and paperwork that slow trade."],
] });
labT(); labQ(); labS(); 
