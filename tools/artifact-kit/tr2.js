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

function acChart(s) {
  const X = (q) => 80 + q * 3, Y = (v) => 340 - (v - 20) * 1.3, ac = (q) => 30 + 4000 / (q + 10);
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 700, 340) + SV.text(86, 48, "Average cost ($)", "sm") + SV.text(700, 362, "Output of the domestic industry", "sm", { "text-anchor": "end" });
  const pts = []; for (let q = 15; q <= 200; q += 5) pts.push([X(q), Y(ac(q))]); o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 }) + SV.text(X(30) + 10, Y(ac(30)) - 12, "Average cost", "lbl bd t1");
  o += SV.line(80, Y(60), 700, Y(60), "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.text(696, Y(60) - 8, "World price $60", "lbl bd t2", { "text-anchor": "end" });
  if (s.p > 0.02) o += `<g opacity="${s.p}">` + SV.line(80, Y(105), 700, Y(105), "dash", { style: "stroke:var(--good);stroke-width:2.5" }) + SV.text(696, Y(105) - 8, "Protected price $105", "lbl bd t3", { "text-anchor": "end" }) + "</g>";
  const q = s.q; o += SV.circle(X(q), Y(ac(q)), 8, ac(q) > 60 ? "dot2" : "dot3") + SV.line(X(q), Y(ac(q)), X(q), 340, "gr") + SV.text(X(q), 358, "Output " + Math.round(q), "sm bd", { "text-anchor": "middle" });
  o += SV.text(X(q) + 12, Y(ac(q)) - 12, "AC $" + Math.round(ac(q)), "lbl bd " + (ac(q) > 60 ? "t2" : "t3"), { style: halo });
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 400, label: "The infant industry argument", base: { q: 20, p: 0 }, draw: acChart, steps: [
  { cap: "A <b>new industry</b> produces only a small amount (20 units), so its <b>average cost is high ($143)</b>, far above the <b>world price of $60</b>. Foreign firms are larger and cheaper: it cannot compete and would be driven out.", s: { q: 20, p: 0 } },
  { cap: "The government <b>protects</b> it with a tariff or subsidy. The protected price is <b>$105</b>, so the industry can sell and survive, and it grows.", s: { q: 60, p: 1 } },
  { cap: "As output grows, <b>average cost falls</b> (economies of scale and learning).", s: { q: 110, p: 1 } },
  { cap: "At about 150 units, average cost is <b>below the world price</b>. The industry can now compete, and the protection can be <b>removed</b>. <b>Evaluate:</b> protection must be temporary, and some infant industries never become competitive.", s: { q: 160, p: 0 } },
] });
const DM = ["A foreign firm sells in a country below its cost of production", "Domestic firms cannot match the low price", "Domestic firms lose sales and close", "The foreign firm gains market power", "It then raises prices: consumers lose in the long run", "Anti-dumping tariffs aim to stop this"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Dumping", base: { n: 0 }, draw: mkChain(DM, "--bad"), steps: chainSteps(["A foreign firm sells in a country <b>below its cost of production</b>.", "Domestic firms <b>cannot match</b> the low price.", "They <b>lose sales and close</b>.", "The foreign firm gains <b>market power</b>.", "It then <b>raises prices</b>: consumers lose in the long run.", "<b>Anti-dumping tariffs</b> aim to stop this and keep competition fair. Evaluate: dumping is hard to prove and may lead to retaliation."]) });
const CA = ["A country has a current account deficit: imports exceed exports", "The government raises tariffs or quotas on imports", "Imports become dearer and fall; some demand switches to domestic goods", "The deficit narrows", "But other countries may retaliate, so exports fall", "And firms using imports face higher costs: the net effect is uncertain"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Using tariffs to reduce a current account deficit", base: { n: 0 }, draw: mkChain(CA, "--accent"), steps: chainSteps(["The country has a <b>current account deficit</b>: imports exceed exports.", "The government raises <b>tariffs or quotas</b> on imports.", "Imports become <b>dearer and fall</b>; some demand switches to domestic goods.", "The <b>deficit narrows</b>.", "But other countries may <b>retaliate</b>, so exports fall.", "And firms using imports face <b>higher costs</b>. <b>Evaluate:</b> the net effect is uncertain and depends on elasticity."]) });

/* Lab 1: tariff and the current account */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc")) return;
  const t = +$("#ca").value / 100, e = +$("#cb").value, r = +$("#cc").value / 100, imp = 100 * Math.pow(1 + t, -e), exp = 90 * Math.pow(1 + r * t, -1.2), def = imp - exp, rev = t * imp;
  $("#ca1").textContent = "$" + money(imp, 0) + "bn"; $("#ca2").textContent = "$" + money(exp, 0) + "bn"; $("#ca3").textContent = (def >= 0 ? "Deficit $" : "Surplus $") + money(Math.abs(def), 0) + "bn";
  $("#cav").textContent = `Imports fall from $100bn to $${money(imp, 0)}bn (import demand elasticity ${e}). ${r > 0 ? `Foreign countries retaliate with tariffs of ${Math.round(r * t * 100)}%, so exports fall from $90bn to $${money(exp, 0)}bn.` : "No retaliation: exports stay at $90bn."} The deficit goes from $10bn to $${money(def, 0)}bn. Tariff revenue is $${money(rev, 1)}bn. ${def > 10 ? "The deficit has got worse: retaliation and low elasticity can make the policy backfire." : def < 10 ? "The deficit has narrowed." : ""}`;
  const base = 290, k = 2.2; let o = SV.line(60, base, 700, base);
  [["Imports", imp, "--bad"], ["Exports", exp, "--good"], ["Deficit", Math.max(0, def), "--warn"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = v * k; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, "$" + money(v, 0) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 24, "Baseline: imports $100bn, exports $90bn, deficit $10bn", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Tariff on imports", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Price elasticity of demand for imports", min: 0.2, max: 2, step: 0.2, value: 1, fmt: (v) => v.toFixed(1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : ""), onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Foreign retaliation (share of our tariff matched)", min: 0, max: 100, step: 25, value: 0, fmt: (v) => v + "%", onInput: labC });
const RS = [
  { n: "Infant industry", w: "A new, small industry has high costs and cannot yet compete.", h: "Protection gives time to grow and gain economies of scale.", c: "May never become efficient; consumers pay more." },
  { n: "Declining (sunset) industry", w: "An old industry is losing out to cheaper imports.", h: "Protects jobs and gives time to retrain workers and adjust.", c: "Delays change; consumers pay more; resources tied up." },
  { n: "Strategic industry", w: "Food, energy and defence are vital for security.", h: "Keeps domestic supply and avoids dependence.", c: "Higher costs; hard to define 'strategic'." },
  { n: "Avoiding dumping", w: "Foreign firms sell below cost to win market share.", h: "Anti-dumping duties keep competition fair.", c: "Hard to prove; retaliation." },
  { n: "Current account deficit", w: "Imports exceed exports.", h: "Cutting imports narrows the deficit.", c: "Elasticity and retaliation can make it fail." },
  { n: "Raising tax revenue", w: "The government needs revenue.", h: "Tariffs are easy to collect.", c: "Revenue falls if imports fall; higher prices." },
  { n: "Demerit goods", w: "Tobacco, alcohol, drugs and weapons are harmful.", h: "Restricting imports reduces consumption and protects health.", c: "Smuggling; black markets." },
  { n: "Environmental sustainability", w: "Some imports are produced unsustainably.", h: "Restrictions protect forests, wildlife and the climate.", c: "May be disguised protection; hard to monitor." },
];
button_table("rsBtns", "rsOut", RS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Situation</th><th>How restriction helps</th><th>Problem</th></tr><tr><td>${p.w}</td><td>${p.h}</td><td>${p.c}</td></tr></table></div>`);
const SC = [
  { n: "A new electric car firm cannot match large foreign makers", a: "Infant industry", w: "Small, new, high costs: needs time to grow." },
  { n: "A coal industry is closing as demand falls", a: "Declining (sunset) industry", w: "Protection slows job losses." },
  { n: "A country wants to avoid relying on imported food", a: "Strategic industry", w: "Self-sufficiency and security." },
  { n: "A foreign steel firm sells below its production cost", a: "Avoiding dumping", w: "Selling below cost." },
  { n: "A very low-income country with few taxes imposes import duties", a: "Raising tax revenue", w: "Tariffs are easy to collect." },
  { n: "A government bans imports of ivory and illegally logged timber", a: "Environmental sustainability", w: "Protecting forests and wildlife." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Reason for restriction</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>reason for trade restrictions</b> fits each situation?", buckets: [{ label: "Infant industry" }, { label: "Declining industry" }, { label: "Strategic industry" }, { label: "Dumping" }], items: [
  { text: "A new computer maker with high costs", b: 0 }, { text: "A start-up car battery firm needing time to grow", b: 0 },
  { text: "A shipyard losing jobs to cheaper foreign yards", b: 1 }, { text: "An old textile industry in decline", b: 1 },
  { text: "A country's food and energy supply", b: 2 }, { text: "Defence equipment manufacturing", b: 2 },
  { text: "Foreign firms selling below cost to win market share", b: 3 }, { text: "Cheap steel flooding the market at a price below cost", b: 3 },
], done: "Know all eight reasons." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>benefit</b> or a <b>problem</b> of using tariffs to reduce a current account deficit?", buckets: [{ label: "Benefit" }, { label: "Problem" }], items: [
  { text: "Imports fall", b: 0 }, { text: "Demand for domestic goods rises", b: 0 }, { text: "The deficit narrows", b: 0 },
  { text: "Other countries may retaliate and cut our exports", b: 1 }, { text: "Firms using imported inputs face higher costs", b: 1 }, { text: "Consumers pay higher prices", b: 1 }, { text: "Fails if demand for imports is inelastic", b: 1 },
], done: "The net effect is uncertain." });
Lib.match($("#m1"), { prompt: "Match the reason to what the government wants.", pairs: [
  ["Infant industry protection", "Give a new industry time to grow and gain economies of scale"],
  ["Sunset industry protection", "Slow job losses and give time to adjust"],
  ["Strategic industry protection", "Secure food, energy and defence supplies"],
  ["Anti-dumping duties", "Stop foreign firms selling below cost"],
  ["Tariffs on imports", "Raise tax revenue or cut imports"],
  ["Import bans on demerit goods", "Protect health and safety"],
], done: "Link the reason to the aim." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why dumping may harm domestic firms</b>.", items: [
  "A foreign firm sells below cost in the domestic market",
  "Domestic firms lose sales",
  "Some domestic firms close and workers lose jobs",
  "The foreign firm has less competition",
  "It raises prices later",
], done: "A dumping chain." });
Lib.calc($("#c1"), { qs: [
  { q: "A foreign firm's cost of producing a good is $20 but it sells it abroad for $14. By what percentage is the price below cost?", a: 30, sol: "6 ÷ 20 × 100 = <b>30%</b>." },
  { q: "A country imports $200bn and exports $180bn. A tariff cuts imports by 10%, with no other change. What is the new deficit ($bn)?", a: 0, sol: "Imports = $180bn, so the deficit = 180 − 180 = <b>$0bn</b>." },
  { q: "Imports fall from 100 units to 70 units after a tariff. At $5 a unit, tariff revenue is $1 per unit. How much revenue ($)?", a: 70, sol: "70 × 1 = <b>$70</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Why might a government protect an infant industry?", opts: ["It is declining", "It needs time to grow and gain economies of scale", "It is very efficient", "It sells at a high price"], a: 1, why: "New firms have high costs." },
  { q: "What is dumping?", opts: ["Selling goods abroad below cost", "Buying too many imports", "Banning imports", "Taxing exports"], a: 0, why: "A price below cost." },
  { q: "Which is a reason for restricting imports of demerit goods?", opts: ["To protect health", "To raise prices", "To reduce exports", "To increase imports"], a: 0, why: "Reduce harmful consumption." },
  { q: "A tariff may fail to reduce a current account deficit if:", opts: ["Demand for imports is inelastic", "Demand for imports is elastic", "No country retaliates", "Imports are cheap"], a: 0, why: "Imports will not fall much." },
  { q: "Why might a government protect a strategic industry?", opts: ["For national security and self-sufficiency", "To raise prices", "To cut exports", "To reduce competition abroad"], a: 0, why: "Food, energy and defence." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Infant (sunrise) industry", "A new industry that is not yet able to compete with established foreign firms."],
  ["Declining (sunset) industry", "An industry in long-term decline that may be protected to slow job losses."],
  ["Strategic industry", "An industry essential for national security, such as defence, energy and food."],
  ["Dumping", "Selling goods abroad at a price below the cost of production."],
  ["Current account deficit", "When the value of imports (and outflows) exceeds exports (and inflows)."],
  ["Demerit good", "A good that is harmful to consumers, such as tobacco."],
  ["Environmental sustainability", "Meeting today's needs without damaging future generations' ability to meet theirs."],
  ["Retaliation", "A response by another country, such as raising its own tariffs."],
  ["Self-sufficiency", "Producing enough of a good at home not to depend on imports."],
] });
labC(); 
