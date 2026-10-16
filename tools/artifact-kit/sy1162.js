const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

/* ---------- Ladder of integration ---------- */
function ladDraw(s) {
  const step = (i, t, sub, k) => { if (k <= 0) return ""; const x = 60 + i * 165, y = 230 - i * 50; return SV.rect(x, y, 150, 280 - y, "f1", op(0.25 + 0.15 * i)) + SV.text(x + 75, y + 24, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) + sub.split("|").map((l, j) => SV.text(x + 75, y + 46 + j * 16, l, "sm", { "text-anchor": "middle", ...op(k) })).join(""); };
  let o = SV.line(40, 280, 730, 280); o += step(0, "Free trade area", "No internal tariffs|Own external tariffs", s.a) + step(1, "Customs union", "+ common external|tariff", s.b) + step(2, "Monetary union", "+ single currency|+ central bank", s.c) + step(3, "Full economic union", "+ common policies|+ free factor movement", s.d);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Four steps of economic integration from a free trade area to a full economic union">${ladDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stL"), { w: 760, h: 300, label: "Ladder of economic integration", base: { a: 0, b: 0, c: 0, d: 0 }, draw: ladDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Free trade area.</b> Members abolish tariffs and quotas on trade between themselves. Each keeps its own tariffs on non-members.", s: { a: 1 } },
  { cap: "<b>Customs union.</b> Members also agree one common external tariff on outsiders, so goods can enter any member on the same terms.", s: { a: 1, b: 1 } },
  { cap: "<b>Monetary union.</b> Members share a currency and a central bank, so there is no exchange rate risk but no independent monetary policy.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Full economic union.</b> Members coordinate fiscal and other economic policies, with free movement of labour and capital and common regulations.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Trade creation and diversion diagram ---------- */
const dP = (q) => (120 - q) / 8, sP = (q) => (q + 10) / 10, qD = (p) => 120 - 8 * p, qS = (p) => Math.max(0, 10 * p - 10);
function tcModel(t, pp) { const pw = 3, p0 = pw + t, p1 = Math.min(pp, p0), qd0 = qD(p0), qs0 = qS(p0), qd1 = qD(p1), qs1 = qS(p1), prod = 0.5 * (p0 - p1) * (qs0 - qs1), cons = 0.5 * (p0 - p1) * (qd1 - qd0), tc = prod + cons, td = pp > pw && p1 === pp ? (pp - pw) * (qd0 - qs0) : 0; return { pw, p0, p1, qd0, qs0, qd1, qs1, prod, cons, tc, td, net: tc - td, same: p1 >= p0 }; }
function tcSvg(t, pp, st, X, Y, w) {
  const m = tcModel(t, pp); let o = SV.line(X(0), Y(0), X(135), Y(0)) + SV.line(X(0), Y(0), X(0), Y(9.2)) + SV.text(X(135), Y(0) + 24, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(X(0) + 6, Y(9.2) - 4, "Price ($)", "sm");
  o += SV.line(X(0), Y(15), X(120), Y(0), "c1") + tag(X(54), Y(8.1), "D", "t1", 1, "start") + SV.line(X(0), Y(1), X(135), Y(14.5), "c3") + tag(X(78), Y(8.8) - 6, "S", "t3", 1, "end");
  o += SV.line(X(0), Y(m.pw), X(135), Y(m.pw), "c2 dash") + tag(X(133), Y(m.pw) + 16, "world price " + m.pw, "t2", 1, "end") + SV.line(X(0), Y(m.p0), X(135), Y(m.p0), "c4 dash") + tag(X(133), Y(m.p0) - 6, "with tariff " + Lib.fmtN(m.p0, 1), "t4", 1, "end");
  if (st >= 1) o += SV.line(X(0), Y(pp), X(135), Y(pp), "c1 dash") + tag(X(2), Y(pp) - 6, "partner price " + Lib.fmtN(pp, 1), "t1", st >= 1 ? 1 : 0);
  if (st >= 2 && !m.same) o += SV.poly([[X(m.qs1), Y(m.p1)], [X(m.qs0), Y(m.p0)], [X(m.qs0), Y(m.p1)]], "f3", { opacity: 0.55 }) + SV.poly([[X(m.qd0), Y(m.p0)], [X(m.qd1), Y(m.p1)], [X(m.qd0), Y(m.p1)]], "f3", { opacity: 0.55 }) + tag(X((m.qs0 + m.qs1) / 2), Y(m.p1) + 20, "production gain", "t3", 1, "end") + tag(X(m.qd0 + 4), Y(m.p1) + 20, "consumption gain", "t3", 1, "start");
  if (st >= 3 && !m.same && m.td > 0) o += SV.rect(X(m.qs0), Y(m.p1), X(m.qd0) - X(m.qs0), Y(m.pw) - Y(m.p1), "f2", { opacity: 0.6 }) + tag(X((m.qs0 + m.qd0) / 2), (Y(m.p1) + Y(m.pw)) / 2 + 4, "trade diversion", "t2", 1, "middle");
  return o;
}
const TX = (q) => 70 + q * 5, TYY = (p) => 300 - p * 29;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Domestic market with a tariff, a partner price below the tariff-inclusive price, trade creation triangles and the trade diversion rectangle">${tcSvg(3, 4.2, 3, TX, TYY)}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 345, label: "A customs union: trade creation triangles and the trade diversion rectangle", base: { st: 0 }, draw: (s) => tcSvg(3, 4.2, Math.round(s.st), TX, TYY), tween: 600, dwell: 6200, steps: [
  { cap: "<b>Before.</b> The country imports at the world price of $3 plus a tariff of $3, so the domestic price is $6. Domestic firms supply 50 units, consumers buy 72, and 22 units are imported from the cheapest world supplier.", s: { st: 0 } },
  { cap: "<b>Joining the union.</b> A partner can supply tariff-free at $4.20, which is cheaper than $6 but dearer than the world price of $3. The domestic price falls to $4.20.", s: { st: 1 } },
  { cap: "<b>Trade creation.</b> Dear domestic output (50 down to 32) is replaced by cheaper imports (production gain), and consumers buy more (72 up to 86) at the lower price (consumption gain). The two shaded triangles are the gain.", s: { st: 2 } },
  { cap: "<b>Trade diversion.</b> The 22 units once bought at $3 from the world are now bought from the partner at $4.20. The rectangle ($1.20 × 22) is a loss. Net effect here: gain of 29.2 minus loss of 26.4, a small net gain.", s: { st: 3 } },
] });

/* ---------- Lab ---------- */
function labT() {
  if (!$("#tf") || !$("#pp")) return;
  const t = +$("#tf").value / 10, pp = +$("#pp").value / 10, m = tcModel(t, pp);
  $("#r1").textContent = m.same ? "none" : Lib.fmtN(m.tc, 1); $("#r2").textContent = m.same ? "none" : Lib.fmtN(m.td, 1); $("#r3").textContent = m.same ? "0" : (m.net >= 0 ? "+" : "") + Lib.fmtN(m.net, 1);
  $("#rv").textContent = m.same ? `The partner's price ($${pp.toFixed(1)}) is no lower than the tariff-inclusive price ($${m.p0.toFixed(1)}), so the country keeps buying at the world price plus the tariff and the union makes no difference to this good.` : `The price falls from $${m.p0.toFixed(1)} to $${m.p1.toFixed(1)}. Trade creation (production effect ${Lib.fmtN(m.prod, 1)} plus consumption effect ${Lib.fmtN(m.cons, 1)}) is ${Lib.fmtN(m.tc, 1)}. Trade diversion is the extra $${(pp - m.pw).toFixed(1)} paid on the ${Lib.fmtN(m.qd0 - m.qs0, 0)} units formerly imported from the world: ${Lib.fmtN(m.td, 1)}. Net effect: ${m.net >= 0 ? "a gain" : "a loss"} of ${Lib.fmtN(Math.abs(m.net), 1)}. ${m.net >= 0 ? "The union is better for the country when the partner is nearly as cheap as the rest of the world." : "The union is worse when the partner is much dearer than the world and the external tariff is high."}`;
  const X = (q) => 40 + q * 2.6, Y = (p) => 295 - p * 29; $("#labA").innerHTML = tcSvg(t, pp, 3, X, Y, 1);
}
Lib.slider($("#g1"), { id: "tf", label: "Tariff, $ ", min: 10, max: 40, step: 1, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
Lib.slider($("#g2"), { id: "pp", label: "Partner's price, $ ", min: 31, max: 70, step: 1, value: 42, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labM() {
  if (!$("#yr")) return;
  const y = +$("#yr").value, gap = (Math.pow(1.03, y) - 1) * 100, adj = (1 - 1 / Math.pow(1.03, y)) * 100;
  $("#t1").textContent = "+" + Lib.fmtN(gap, 1) + "%"; $("#t2").textContent = gap > 10 ? "Badly weakened" : gap > 4 ? "Weakened" : "Slightly weaker"; $("#t3").textContent = "−" + Lib.fmtN(adj, 1) + "%";
  $("#tv").textContent = `After ${y} years of costs rising 3% a year faster than in the stronger member, the weaker member's costs are ${Lib.fmtN(gap, 1)}% higher relative to its partner. With one currency it cannot devalue, so to restore competitiveness its wages and prices must fall by about ${Lib.fmtN(adj, 1)}% relative to the partner's: an 'internal devaluation', which usually means unemployment and spending cuts.`;
  const X = (t) => 50 + t * 11, Y = (v) => 270 - (v - 100) * 4.2; let o = SV.line(50, 270, 400, 270) + SV.line(50, 270, 50, 20) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(56, 16, "Relative cost level (start = 100)", "sm") + SV.line(50, Y(100), 400, Y(100), "c3 dash");
  const pts = []; for (let t = 0; t <= y; t += 0.5) pts.push([X(t), Y(100 * Math.pow(1.03, t))]); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2");
  $("#labB").innerHTML = o + tag(X(y) - 4, Y(100 * Math.pow(1.03, y)) - 8, Lib.fmtN(100 * Math.pow(1.03, y), 0), "t2", 1, "end");
}
Lib.slider($("#g3"), { id: "yr", label: "Years in the union ", min: 1, max: 25, step: 1, value: 10, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which stage of integration is it?", buckets: [{"label": "Free trade area"}, {"label": "Customs union"}, {"label": "Monetary union"}], items: [{"text": "Members remove tariffs between themselves but set their own tariffs on non-members", "b": 0}, {"text": "Members adopt a common external tariff", "b": 1}, {"text": "Members use one currency and one central bank", "b": 2}, {"text": "Rules of origin are needed to stop trade deflection", "b": 0}, {"text": "No exchange rate risk between members", "b": 2}, {"text": "Members negotiate trade deals as a single bloc", "b": 1}, {"text": "A member can still sign its own trade agreements with outsiders", "b": 0}, {"text": "A weaker member can no longer devalue", "b": 2}], done: "Free trade area: no internal tariffs. Customs union: plus common external tariff. Monetary union: plus single currency." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Free trade area", "Members abolish tariffs and quotas between themselves"], ["Customs union", "A free trade area plus a common external tariff"], ["Monetary union", "Members share a single currency and central bank"], ["Trade creation", "Dearer domestic output replaced by cheaper imports from a partner"], ["Trade diversion", "Imports switched from a cheaper outsider to a dearer partner"], ["Common external tariff", "One tariff all members charge on goods from outside the union"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the integration stages in order, least integrated first.", items: ["Free trade area", "Customs union", "Monetary union", "Full economic union"], done: "Each stage adds a new level of integration." });
Lib.calc($("#c1"), { qs: [
  {"q": "The world price is $3 and the tariff is $3. A partner offers $4.20 tariff-free. By how much does the domestic price fall ($)?", "a": 1.8, "unit": "$", "tol": 0.01, "hint": "6 − 4.20.", "sol": "<b>$1.80</b>."},
  {"q": "Before joining, the country imported 22 units at the world price of $3. The partner price is $4.20. Calculate the trade diversion loss ($).", "a": 26.4, "unit": "$", "tol": 0.1, "hint": "(4.20 − 3.00) × 22.", "sol": "1.20 × 22 = <b>$26.4</b>."},
  {"q": "The production effect is 16.2 and the consumption effect is 13.0. Calculate total trade creation (1 decimal place).", "a": 29.2, "unit": "", "tol": 0.1, "hint": "Add them.", "sol": "<b>29.2</b>."},
  {"q": "A member's costs rise 3% a year faster than its partner's for 10 years. By about what percentage are its costs relatively higher (%, 1 decimal place)?", "a": 34.4, "unit": "%", "tol": 0.3, "hint": "1.03^10 − 1.", "sol": "1.03^10 = 1.344, so about <b>34.4%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A customs union differs from a free trade area because it has:", opts: ["A common external tariff", "No tariffs between members", "A single currency", "No non-tariff barriers"], a: 0, why: "Members apply the same tariff to outsiders." },
  { q: "Trade diversion occurs when:", opts: ["Imports switch from a lower-cost outsider to a higher-cost partner", "Domestic output is replaced by cheaper partner imports", "Exports fall to zero", "A currency is devalued"], a: 0, why: "The common external tariff makes outside goods dearer." },
  { q: "Trade creation is a:", opts: ["Gain, as cheaper imports replace dearer domestic output", "Loss, as dearer imports replace cheaper ones", "Cost of tariffs", "Change in the exchange rate"], a: 0, why: "Production and consumption efficiency improve." },
  { q: "A disadvantage of a monetary union for a weaker member is that it:", opts: ["Cannot devalue its currency", "Pays more tariffs", "Loses all its exports", "Has too much monetary independence"], a: 0, why: "It has no exchange rate adjustment." },
  { q: "The net effect of joining a customs union is more likely to be positive if:", opts: ["The partner's price is close to the world price", "The external tariff is very high", "The partner is much less efficient", "Demand is perfectly inelastic"], a: 0, why: "Trade diversion is smaller when the partner is nearly as efficient as outsiders." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Free trade area", "No internal tariffs; own external tariffs."],
  ["Customs union", "FTA + common external tariff."],
  ["Monetary union", "Single currency and central bank."],
  ["Full economic union", "Common economic policies as well."],
  ["Trade creation", "Cheaper partner replaces dearer domestic output."],
  ["Trade diversion", "Dearer partner replaces cheaper outsider."],
  ["Net effect", "Creation minus diversion."],
  ["Cost of monetary union", "No devaluation or independent interest rate."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country imposes a tariff on steel imports. What is the likely impact on its economy? (May/June 2025 · 31 · Q25, reworded)", opts: ["Its steel exports become more price competitive", "Productive inefficiency in its steel industry", "An improvement in its terms of trade", "A fall in producer surplus for its steel producers"], a: 1, why: "Protection from foreign competition can reduce the incentive to cut costs. Domestic producers gain surplus, not lose it." },
  { q: "The US introduced tariffs on many imports from China in 2018. Which policy type was this? (Oct/Nov 2024 · 32 · Q25, reworded)", opts: ["Expenditure-reducing", "Expenditure-switching", "Expansionary monetary", "Contractionary monetary"], a: 1, why: "Tariffs switch spending from imports to domestic goods." },
  { q: "What is a failure of government microeconomic intervention? (Feb/March 2024 · 32 · Q13, reworded)", opts: ["An indirect tax equal to external costs is imposed on cigarettes and demand falls", "Limits are placed on a union's restrictions that increase labour mobility", "Price controls on bread are removed", "Tariffs on imports raise the Gini coefficient"], a: 3, why: "A policy that worsens an objective, such as higher inequality, is a government failure. The other three work as intended." },
  { q: "Which is an example of an expenditure-switching policy? (Feb/March 2023 · 32 · Q29, reworded)", opts: ["Higher income tax rates", "Higher interest rates", "Higher tariff rates", "A larger money supply"], a: 2, why: "Tariffs change the mix of spending from imports to domestic goods. The others reduce total spending." },
  { q: "What is most likely to be an appropriate action to reduce both a current account surplus and inflation? (Oct/Nov 2021 · 32 · Q30, reworded)", opts: ["Lower the rate of interest", "Devalue the currency", "Increase direct taxes", "Remove tariffs on imports"], a: 3, why: "Removing tariffs lowers import prices, which cuts inflation and raises imports, reducing the surplus." },
] });
