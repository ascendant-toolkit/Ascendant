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

function ftChart(s) {
  const pw = s.pw, qs = pw - 10, qd = 110 - pw; let o = axes("Price", "Quantity");
  o += curve(-1, 110, "c1", "Demand", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Domestic supply", { t: "t3", dx: -125, dy: 16 });
  o += hline(60, "gr", 50) + vline(50, 60) + SV.circle(QX(50), PY(60), 6, "dot1", { opacity: s.f > 0.5 ? 0.5 : 1 }) + ylab(60, "P") + xlab(50, "Q");
  if (s.f > 0.02) { o += `<g opacity="${s.f}">` + SV.line(QX(0), PY(pw), QX(100), PY(pw), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(pw) - 8, "World price $" + Math.round(pw), "lbl bd t2", { "text-anchor": "end" }) + SV.line(QX(qs), PY(pw), QX(qs), PY(0), "gr") + SV.line(QX(qd), PY(pw), QX(qd), PY(0), "gr") + SV.circle(QX(qs), PY(pw), 6, "dot2") + SV.circle(QX(qd), PY(pw), 6, "dot2") + SV.text(QX(qs), PY(0) + 18, "Qs " + Math.round(qs), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(qd), PY(0) + 18, "Qd " + Math.round(qd), "sm bd", { "text-anchor": "middle" }); if (qd > qs) o += SV.text(QX((qs + qd) / 2), PY(pw) + 22, "Imports: " + Math.round(qd - qs), "lbl bd t2", { "text-anchor": "middle", style: halo }); else if (qs > qd) o += SV.text(QX((qs + qd) / 2), PY(pw) - 14, "Exports: " + Math.round(qs - qd), "lbl bd t2", { "text-anchor": "middle", style: halo }); o += "</g>"; }
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 400, label: "Free trade in a market", base: { pw: 40, f: 0 }, draw: ftChart, steps: [
  { cap: "Without trade, the domestic market for a good has equilibrium price <b>$60</b> and quantity <b>50</b>.", s: { pw: 40, f: 0 } },
  { cap: "The country opens to <b>free trade</b>. The <b>world price is $40</b>, lower than the domestic price, so imports enter at $40.", s: { pw: 40, f: 1 } },
  { cap: "<b>Consumers gain:</b> the price falls to $40 and they buy <b>70</b> instead of 50. <b>Domestic producers lose:</b> they supply only <b>30</b>. <b>Imports of 40</b> fill the gap.", s: { pw: 40, f: 1 } },
  { cap: "<b>Evaluate:</b> consumers and importers gain, but domestic firms may close and workers lose jobs. Overall the gains to consumers could outweigh the losses, but not for those who lose jobs.", s: { pw: 40, f: 1 } },
] });
const EX = ["Free trade opens large export markets", "Exporters sell more: higher revenue and profit", "They expand output and gain economies of scale", "Jobs and incomes rise in export industries", "Imported inputs are cheaper and better", "Higher competitiveness and growth for the economy"];
Lib.stepper($("#stE"), { w: 760, h: 400, label: "How free trade could raise growth", base: { n: 0 }, draw: mkChain(EX, "--good"), steps: chainSteps(["Free trade opens <b>large export markets</b>.", "Exporters <b>sell more</b>: higher revenue and profit.", "They expand output and gain <b>economies of scale</b>.", "<b>Jobs and incomes rise</b> in export industries.", "<b>Imported inputs</b> are cheaper and better, lowering costs.", "The economy becomes more <b>competitive</b> and grows faster."]) });
const JL = ["Free trade lets cheaper imports in", "Domestic firms in that industry lose sales", "They cut output, close or lay off workers", "Unemployment rises, especially in some regions", "Workers' skills do not match new jobs: structural unemployment", "The government may need to spend on retraining and benefits"];
Lib.stepper($("#stJ"), { w: 760, h: 400, label: "How free trade can cost jobs", base: { n: 0 }, draw: mkChain(JL, "--bad"), steps: chainSteps(["Free trade lets <b>cheaper imports</b> in.", "Domestic firms in that industry <b>lose sales</b>.", "They <b>cut output, close or lay off workers</b>.", "<b>Unemployment rises</b>, especially in some regions.", "Workers' skills do not match new jobs: <b>structural unemployment</b>.", "The government may need to fund <b>retraining and benefits</b>. Evaluate: the gains to consumers and exporters may outweigh this over time."]) });

/* Lab 1 */
function labF() {
  if (!$("#fa")) return;
  const pw = +$("#fa").value, qs = Math.max(0, pw - 10), qd = Math.max(0, 110 - pw), net = qd - qs;
  $("#fa1").textContent = "$" + pw; $("#fa2").textContent = Math.round(qs); $("#fa3").textContent = net > 0 ? "Imports " + Math.round(net) : net < 0 ? "Exports " + Math.round(-net) : "None";
  $("#fav").textContent = pw < 60 ? `The world price ($${pw}) is below the domestic price of $60. Consumers pay less and buy ${Math.round(qd)}, domestic producers supply only ${Math.round(qs)}, and ${Math.round(net)} is imported. Consumers gain; producers lose.` : pw > 60 ? `The world price ($${pw}) is above the domestic price of $60. Producers can sell abroad at the higher price and supply ${Math.round(qs)}, but consumers buy only ${Math.round(qd)} at the higher price. The country exports ${Math.round(-net)}. Producers gain; consumers lose.` : "The world price equals the domestic price: no trade.";
  $("#labF").innerHTML = ftChart({ pw, f: 1 });
}
Lib.slider($("#g1"), { id: "fa", label: "World price of the good", min: 20, max: 90, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labF });
const WL = [
  { n: "Consumers", g: "Lower prices, more choice and quality.", l: "Fewer local varieties if firms close; may lose income if their own jobs go." },
  { n: "Exporters", g: "Access to larger markets, more sales, scale economies.", l: "More competition in foreign markets." },
  { n: "Domestic firms facing imports", g: "Cheaper inputs and pressure to become efficient.", l: "Lost sales; some close, especially infant industries." },
  { n: "Workers in export industries", g: "More jobs and higher wages.", l: "Fewer protections in some cases." },
  { n: "Workers in import-competing industries", g: "None directly.", l: "Job losses and structural unemployment." },
  { n: "The government", g: "Growth raises tax revenue.", l: "Loses tariff revenue; pays for retraining and benefits." },
  { n: "Poorer countries", g: "Market access, technology, investment.", l: "Hard to compete with larger rich-country firms; risk of dependency." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);
const MV = [
  { n: "Remove tariffs", w: "Imports become cheaper; domestic firms face more competition.", e: "Consumers gain; import-competing firms lose; the government loses revenue." },
  { n: "Raise or remove quotas", w: "More imports allowed; supply rises; prices fall.", e: "Consumers gain; domestic producers lose sales." },
  { n: "End embargoes (bans)", w: "Trade restarts with the banned country.", e: "Wider market and choice; may remove political pressure." },
  { n: "Remove subsidies", w: "Firms no longer artificially cheap; fairer competition.", e: "Taxpayers gain; some subsidised firms lose." },
  { n: "Cut red tape and join trade agreements", w: "Easier, cheaper cross-border trade; other countries may open their markets too.", e: "Exporters gain access to larger markets." },
];
button_table("mvBtns", "mvOut", MV, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it does</th><th>Who is affected</th></tr><tr><td>${p.w}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of free trade?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Lower prices for consumers", b: 0 }, { text: "Larger markets for exporters", b: 0 }, { text: "Access to cheaper raw materials", b: 0 }, { text: "More competition raises efficiency", b: 0 },
  { text: "Domestic firms may close", b: 1 }, { text: "Structural unemployment in some industries", b: 1 }, { text: "Dependence on other countries", b: 1 }, { text: "Loss of tariff revenue", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Who is likely to <b>gain</b> and who to <b>lose</b> from a move to free trade?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "Consumers buying cheaper imports", b: 0 }, { text: "Exporters selling in new markets", b: 0 }, { text: "Firms using imported raw materials", b: 0 },
  { text: "Workers in an industry hit by imports", b: 1 }, { text: "Infant industries without protection", b: 1 }, { text: "A government that relied on tariff revenue", b: 1 },
], done: "Winners and losers." });
Lib.classify($("#cl3"), { prompt: "Does each action <b>move a country towards free trade</b>?", buckets: [{ label: "Towards free trade" }, { label: "Towards protection" }], items: [
  { text: "Cut import tariffs", b: 0 }, { text: "Increase an import quota", b: 0 }, { text: "Join a free trade agreement", b: 0 }, { text: "Remove an embargo", b: 0 },
  { text: "Raise tariffs", b: 1 }, { text: "Ban imports", b: 1 }, { text: "Subsidise domestic producers", b: 1 }, { text: "Cut an import quota", b: 1 },
], done: "Free trade removes restrictions." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Free trade", "Trade between countries without restrictions such as tariffs or quotas"],
  ["Tariff", "A tax on imports"],
  ["Import quota", "A limit on the quantity of a good that can be imported"],
  ["Embargo", "A ban on trade with a country"],
  ["Dumping", "Selling goods abroad at a price below cost"],
  ["Infant industry", "A new industry that cannot yet compete with established foreign firms"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how free trade could reduce prices for consumers</b>.", items: [
  "Trade restrictions are removed",
  "Cheaper foreign goods enter the market",
  "Domestic firms face more competition",
  "Firms cut prices and costs to compete",
  "Consumers pay lower prices and have more choice",
], done: "A competition chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Domestic demand at a world price of $40 is 70 and domestic supply is 30. How many units are imported?", a: 40, sol: "70 − 30 = <b>40</b>." },
  { q: "A good costs $60 at home and $40 in world markets. By what percentage is the world price lower than the home price (1 d.p.)?", a: 33.3, tol: 0.1, sol: "(60 − 40) ÷ 60 × 100 = <b>33.3%</b>." },
  { q: "A country exports $90bn and imports $100bn. What is the trade balance ($bn)? Use a minus sign for a deficit.", a: -10, sol: "90 − 100 = <b>−$10bn</b>, a trade deficit." },
  { q: "Imports of $5bn face a 10% tariff. How much tariff revenue does the government lose ($bn) if the tariff is removed, assuming imports stay the same?", a: 0.5, sol: "10% × 5 = <b>$0.5bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is free trade?", opts: ["Trade with high tariffs", "Trade between countries without restrictions", "Trade only within a country", "Trade without money"], a: 1, why: "No tariffs, quotas or other restrictions." },
  { q: "Which is a benefit of free trade?", opts: ["Higher prices", "Lower prices and greater choice", "Fewer exports", "Less competition"], a: 1, why: "Competition and imports help consumers." },
  { q: "Which is a disadvantage of free trade?", opts: ["Larger markets", "Domestic firms may be unable to compete with imports", "More choice", "Specialisation"], a: 1, why: "Some firms and jobs are lost." },
  { q: "Which would move a country towards free trade?", opts: ["Raising tariffs", "Banning imports", "Removing quotas", "Subsidising exports"], a: 2, why: "Quotas are a restriction." },
  { q: "Who is most likely to lose from free trade?", opts: ["Consumers", "Exporters", "Workers in industries that compete with imports", "Firms buying cheaper inputs"], a: 2, why: "Import-competing industries face competition." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Free trade", "Trade between countries without restrictions such as tariffs, quotas, subsidies or embargoes."],
  ["Tariff", "A tax on imports."],
  ["Quota", "A limit on the quantity of a good that can be imported."],
  ["Embargo", "A ban on trade with a particular country."],
  ["Subsidy", "A payment by the government to producers to lower their costs."],
  ["Protection", "Measures to protect domestic producers from foreign competition."],
  ["Dumping", "Selling goods abroad at a price below the cost of production."],
  ["Infant industry", "A new industry that is not yet able to compete with established foreign firms."],
  ["Trade agreement", "A deal between countries to reduce trade barriers."],
  ["Competitiveness", "How cheaply and well a country's firms can produce compared with rivals."],
] });
labF(); 
