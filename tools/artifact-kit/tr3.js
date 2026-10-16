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

Lib.stepper($("#stH"), { w: 760, h: 400, label: "Who gains and who loses from a tariff?", base: { pw: 40, t: 0 }, draw: tmChart, steps: [
  { cap: "Free trade: price <b>$40</b>, consumers buy 70, domestic firms supply 30, imports 40.", s: { pw: 40, t: 0 } },
  { cap: "A <b>$10 tariff</b> raises the price to <b>$50</b>. <b>Consumers lose</b>: they pay more and buy less (60).", s: { pw: 40, t: 10 } },
  { cap: "<b>Domestic producers gain</b>: they sell more (40) at a higher price. <b>The government gains</b> tariff revenue (the green box). <b>Foreign exporters lose</b>: imports fall from 40 to 20.", s: { pw: 40, t: 10 } },
  { cap: "<b>Evaluate:</b> the loss to consumers is larger than the gains to domestic producers and the government taken together, so the economy as a whole is likely to lose, though protected workers gain.", s: { pw: 40, t: 10 } },
] });
const TW = ["Country A raises tariffs on imports from Country B", "B's exporters lose sales and jobs", "B retaliates with tariffs on imports from A", "A's exporters lose sales; both countries' consumers pay more", "Firms' supply chains are disrupted and costs rise", "Trade and growth fall in both countries: a trade war"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "A trade war", base: { n: 0 }, draw: mkChain(TW, "--bad"), steps: chainSteps(["Country A <b>raises tariffs</b> on imports from Country B.", "B's <b>exporters lose sales</b> and jobs.", "B <b>retaliates</b> with tariffs on imports from A.", "A's exporters lose sales; <b>consumers in both countries pay more</b>.", "Firms' <b>supply chains are disrupted</b> and costs rise.", "<b>Trade and growth fall</b> in both countries: a trade war leaves everyone worse off."]) });
const PT = ["The home country imposes a tariff or quota", "Foreign exporters sell less in that market", "Foreign firms cut output and workers lose jobs", "Their export earnings and growth fall", "The foreign government may retaliate or seek new markets", "Trading partners' current accounts and incomes may worsen"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Effects on trading partners", base: { n: 0 }, draw: mkChain(PT, "--warn"), steps: chainSteps(["The home country imposes a <b>tariff or quota</b>.", "<b>Foreign exporters</b> sell less in that market.", "Foreign firms <b>cut output</b> and workers lose jobs.", "Their <b>export earnings and growth</b> fall.", "The foreign government may <b>retaliate</b> or seek new markets.", "Trading partners' <b>current accounts and incomes</b> may worsen."]) });

/* Lab 1: trade war */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const tA = +$("#wa").value, r = +$("#wb").value / 100, tB = r * tA, outA = 100 + 0.2 * tA - 0.3 * tB, outB = 100 + 0.2 * tB - 0.3 * tA, price = 0.5 * tA, wt = 100 - 0.5 * (tA + tB);
  $("#wa1").textContent = money(outA, 1); $("#wa2").textContent = money(outB, 1); $("#wa3").textContent = "+" + money(price, 1) + "%"; $("#wa4").textContent = money(wt, 0);
  $("#wav").textContent = tA === 0 ? "No tariff: free trade, output index 100 for both." : `A's tariff of ${tA}% protects some of its industries (+${money(0.2 * tA, 1)}), but ${r > 0 ? `B retaliates with ${money(tB, 0)}%, hitting A's exports (−${money(0.3 * tB, 1)}). Net output index for A: ${money(outA, 1)}.` : "B does not retaliate. A's output index rises slightly."} B's output index: ${money(outB, 1)}. World trade falls to ${money(wt, 0)}. Consumers in A pay about ${money(price, 1)}% more. ${r >= 1 && tA > 0 ? "With full retaliation both countries end up worse off than under free trade: a trade war." : ""}`;
  const base = 290, k = 2.4; let o = SV.line(60, base, 700, base);
  [["Output A", outA, "--accent"], ["Output B", outB, "--good"], ["World trade", wt, "--warn"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = (v - 50) * k * 1.5; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labW").innerHTML = o + SV.text(60, 24, "Index (free trade = 100). Illustrative model.", "sm");
}
Lib.slider($("#g1"), { id: "wa", label: "Country A's tariff", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Country B's retaliation (share of A's tariff matched)", min: 0, max: 100, step: 25, value: 100, fmt: (v) => v + "%", onInput: labW });
const WL = [
  { n: "Consumers in the home country", g: "None, unless a protected industry becomes efficient.", l: "Higher prices, less choice, lower quality if competition falls." },
  { n: "Protected domestic producers", g: "More sales and profit; jobs protected.", l: "May become inefficient and complacent." },
  { n: "Firms using imported inputs", g: "None.", l: "Higher costs; some lose competitiveness." },
  { n: "The home government", g: "Tariff revenue; may improve the current account.", l: "May have to pay subsidies; higher inflation; breaking trade agreements." },
  { n: "Foreign exporters", g: "None.", l: "Lost sales, jobs and earnings; may retaliate." },
  { n: "Foreign consumers", g: "May gain if other exports are cheaper (diverted).", l: "Higher prices if they retaliate." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);
const AD = [
  { n: "For the home country", a: "Protects jobs and infant, declining and strategic industries; may reduce the current account deficit; raises revenue.", d: "Higher prices; less choice; inefficiency; higher costs for firms using imports; risk of retaliation." },
  { n: "For trading partners", a: "None directly; may find new markets.", d: "Lost exports, jobs and growth; may widen their current account deficit; may retaliate." },
  { n: "For the world economy", a: "Can protect vulnerable industries while they adjust.", d: "Less trade and specialisation; slower growth; trade wars; less competition." },
];
button_table("adBtns", "adOut", AD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Advantages</th><th>Disadvantages</th></tr><tr><td>${p.a}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each effect of a tariff a <b>gain</b> or a <b>loss</b> for the <b>home country</b>?", buckets: [{ label: "Gain" }, { label: "Loss" }], items: [
  { text: "Domestic producers sell more", b: 0 }, { text: "The government collects revenue", b: 0 }, { text: "Jobs saved in protected industries", b: 0 }, { text: "Imports fall, helping the current account", b: 0 },
  { text: "Consumers pay higher prices", b: 1 }, { text: "Less choice for consumers", b: 1 }, { text: "Firms using imported inputs face higher costs", b: 1 }, { text: "Protected firms may become inefficient", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Who is affected? Is each effect on the <b>home country</b> or on <b>trading partners</b>?", buckets: [{ label: "Home country" }, { label: "Trading partners" }], items: [
  { text: "Consumers pay higher prices", b: 0 }, { text: "Domestic firms gain market share", b: 0 }, { text: "Tariff revenue for the government", b: 0 },
  { text: "Exporters lose sales and jobs", b: 1 }, { text: "Governments may retaliate with tariffs", b: 1 }, { text: "Export earnings fall", b: 1 },
], done: "Tariffs hurt trading partners' exporters." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Retaliation", "Responding to a trade restriction with one of your own"],
  ["Trade war", "Countries raising barriers against each other, harming trade"],
  ["Complacency", "Domestic firms becoming inefficient because of weak competition"],
  ["Consumer surplus", "The gain consumers get from paying less than they were willing to pay"],
  ["Trading partner", "A country that buys from and sells to your country"],
  ["Import-competing industry", "An industry that competes with imports"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a trade war reduces growth</b>.", items: [
  "One country raises tariffs",
  "Trading partners retaliate",
  "Trade between the countries falls",
  "Prices rise and supply chains are disrupted",
  "Firms cut output and investment: growth slows",
], done: "A trade war chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A tariff raises the price of imported shoes from $50 to $60. By what percentage has the price risen?", a: 20, sol: "10 ÷ 50 × 100 = <b>20%</b>." },
  { q: "A country's exports to a market fall from $80bn to $68bn after a tariff. By what percentage did they fall?", a: 15, sol: "12 ÷ 80 × 100 = <b>15%</b>." },
  { q: "Domestic production rises from 30 to 40 units after a tariff. By what percentage?", a: 33.3, tol: 0.1, sol: "10 ÷ 30 × 100 = <b>33.3%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Who is most likely to lose from a tariff on imports?", opts: ["Domestic producers", "The government", "Consumers", "Protected workers"], a: 2, why: "Consumers pay higher prices." },
  { q: "A likely effect of a tariff on trading partners is:", opts: ["Exports to that country rise", "Exports to that country fall", "No change", "Higher imports"], a: 1, why: "Foreign goods become dearer." },
  { q: "A trade war is:", opts: ["Countries lowering tariffs", "Countries raising barriers against each other", "A war over trade routes", "Free trade"], a: 1, why: "Retaliation spirals." },
  { q: "A disadvantage of restricting trade is:", opts: ["Protects jobs", "Raises revenue", "Higher prices for consumers", "Reduces imports"], a: 2, why: "Consumers lose." },
  { q: "A tariff is least likely to work if demand for imports is:", opts: ["Elastic", "Inelastic", "Unit elastic", "Falling"], a: 1, why: "Imports will not fall much." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Retaliation", "A response to a trade restriction with a similar restriction on the other country's goods."],
  ["Trade war", "A situation where countries impose trade restrictions on each other, harming trade."],
  ["Complacency", "A lack of effort to improve because of weak competition."],
  ["Trading partner", "A country with which another country regularly trades."],
  ["Consumer loss", "Higher prices and less choice for consumers caused by trade restrictions."],
  ["Import-competing industry", "An industry that competes directly with imports."],
  ["Smuggling", "Illegally bringing goods into a country to avoid tariffs or bans."],
  ["Efficiency", "Producing goods at the lowest cost possible."],
  ["Current account", "The part of the balance of payments for trade in goods and services and income flows."],
] });
labW(); 
