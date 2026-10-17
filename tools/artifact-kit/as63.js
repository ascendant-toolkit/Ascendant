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

/* ---------- tariff diagram ---------- */
const TX = (q) => 70 + q * 6.4, TY = (p) => 270 - p * 2.4, PW = 40;
function tarDraw(t, k) {
  const pt = PW + t, qd0 = (100 - PW) / 0.8, qs0 = (PW - 20) / 0.8, qd1 = (100 - pt) / 0.8, qs1 = (pt - 20) / 0.8; let o = axes(70, 270, 720, 25, "Quantity", "Price");
  o += SV.line(TX(0), TY(100), TX(100), TY(20), "c2", { "stroke-width": 3 }) + tag(TX(100) + 4, TY(20), "Domestic demand", "c2") + SV.line(TX(0), TY(20), TX(100), TY(100), "c1", { "stroke-width": 3 }) + tag(TX(100) + 4, TY(100), "Domestic supply", "c1");
  o += SV.line(70, TY(PW), 720, TY(PW), "dash") + tag(724, TY(PW) + 14, "World price $40", "c4", 1, "end");
  if (t > 0 && k > 0) {
    o += SV.line(70, TY(pt), 720, TY(pt), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, TY(pt) - 6, "World price + tariff $" + pt, "c3", k, "end");
    const pl = (pts, c, v) => SV.poly(pts.map(([q, p]) => [TX(q), TY(p)]), c, op(v));
    o += pl([[qs0, PW], [qs1, pt], [0, pt], [0, PW]].slice(0, 0).concat([[0, PW], [qs0, PW], [qs1, pt], [0, pt]]), "f2", 0.5 * k);
    o += pl([[qs1, PW], [qd1, PW], [qd1, pt], [qs1, pt]], "f1", 0.6 * k);
    o += pl([[qd1, PW], [qd0, PW], [qd1, pt]], "f3", 0.6 * k) + pl([[qs0, PW], [qs1, PW], [qs1, pt]], "f3", 0.6 * k);
    o += SV.text(TX((qs1 + qd1) / 2), TY((pt + PW) / 2) + 4, "Tariff revenue", "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(TX(qs1 / 2), TY((pt + PW) / 2) + 4, "Producer gain", "sm", { "text-anchor": "middle", ...op(k) });
    o += SV.circle(TX(qd1), TY(pt), 5, "dot3", op(k)) + SV.circle(TX(qs1), TY(pt), 5, "dot2", op(k)) + SV.circle(TX(qd0), TY(PW), 4, "dot1", op(0.6)) + SV.circle(TX(qs0), TY(PW), 4, "dot1", op(0.6));
    o += SV.line(TX(qs1), TY(pt) - 14, TX(qd1), TY(pt) - 14, "c4", { "stroke-width": 2, ...op(k) }) + SV.text(TX((qs1 + qd1) / 2), TY(pt) - 20, "Imports " + Lib.fmtN(qd1 - qs1, 1), "sm", { "text-anchor": "middle", ...op(k) });
  } else o += SV.line(TX(qs0), TY(PW) - 14, TX(qd0), TY(PW) - 14, "c4", { "stroke-width": 2 }) + SV.text(TX((qs0 + qd0) / 2), TY(PW) - 20, "Imports " + Lib.fmtN(qd0 - qs0, 0), "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tariff raises the domestic price, reduces imports and creates tariff revenue and a welfare loss">${tarDraw(10, 1)}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 300, label: "A $10 tariff on imports with a world price of $40", base: { t: 0, k: 0 }, draw: (s) => tarDraw(s.t, s.k), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Free trade.</b> At the world price of $40 consumers buy 75 units, domestic firms supply 25 and the other 50 are imported.", s: { t: 0, k: 0 } },
  { cap: "<b>A $10 tariff</b> raises the price in the country to $50. Domestic firms supply more (37.5) and consumers buy less (62.5), so imports fall to 25.", s: { t: 10, k: 1 } },
  { cap: "<b>Winners and losers.</b> Producers gain (green area), the government collects tariff revenue ($10 × 25 = $250), and consumers lose surplus. The two small triangles are the <b>welfare loss</b>: $62.5 + $62.5 = $125.", s: { t: 10, k: 1 } },
] });

/* ---------- imports under tools ---------- */
function toolDraw(s) {
  const Y = (v) => 250 - v * 3.2; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Imports (units)", "sm");
  const T = [["Free trade", 50, "f1"], ["Tariff $10", 25, "f3"], ["Quota of 25", 25, "f2"], ["Red tape", 38, "f1"], ["Embargo", 0, "f3"]];
  T.forEach(([n, v, c], i) => { const k = Math.max(0, Math.min(1, s.k - i)); if (k > 0) o += SV.rect(90 + i * 120, Y(v * k + 0), 80, Math.max(2, 250 - Y(v)), c, op(0.65 * k)) + SV.text(130 + i * 120, 268, n, "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(130 + i * 120, Y(v) - 6, v, "lbl bd", { "text-anchor": "middle", ...op(k) }); });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Imports under free trade, a tariff, a quota, red tape and an embargo">${toolDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 290, label: "Imports under different tools of protection", base: { k: 0 }, draw: toolDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Free trade:</b> 50 units are imported.", s: { k: 1 } },
  { cap: "<b>A tariff</b> raises the price and imports fall to 25. The government collects revenue.", s: { k: 2 } },
  { cap: "<b>A quota</b> limits imports to 25 directly. The price gap goes to importers.", s: { k: 3 } },
  { cap: "<b>Red tape</b> adds cost and delay, reducing imports a little (to 38) without any visible tax.", s: { k: 4 } },
  { cap: "<b>An embargo</b> bans trade: imports fall to zero.", s: { k: 5 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#tf")) return;
  const t = +$("#tf").value, pt = PW + t, qd1 = (100 - pt) / 0.8, qs1 = (pt - 20) / 0.8, qd0 = (100 - PW) / 0.8, qs0 = (PW - 20) / 0.8, imp = qd1 - qs1, rev = t * imp, dwl = 0.5 * (qs1 - qs0) * t + 0.5 * (qd0 - qd1) * t;
  $("#r1").textContent = "$" + pt + ", " + Lib.fmtN(imp, 1); $("#r2").textContent = "$" + Lib.fmtN(rev, 0); $("#r3").textContent = "$" + Lib.fmtN(dwl, 1);
  $("#rv").textContent = t === 0 ? "No tariff: free trade at the world price of $40 with 50 units imported." : `A $${t} tariff raises the domestic price to $${pt}. Imports fall from 50 to ${Lib.fmtN(imp, 1)}, domestic output rises from 25 to ${Lib.fmtN(qs1, 1)} and consumption falls from 75 to ${Lib.fmtN(qd1, 1)}. The government collects $${Lib.fmtN(rev, 0)}. The welfare loss is $${Lib.fmtN(dwl, 1)}.${imp <= 0.5 ? " At this tariff imports are almost eliminated: a prohibitive tariff." : ""}`;
  $("#labA").innerHTML = tarDraw(t, 1);
}
Lib.slider($("#g1"), { id: "tf", label: "Tariff per unit, $ ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
const TL = [["Tariff", "Government (revenue), domestic producers", "Consumers, foreign exporters", "Retaliation and higher input costs"], ["Import quota", "Domestic producers, importers with licences", "Consumers, the government (no revenue)", "Quota rent and possible corruption"], ["Export subsidy", "Exporters and their workers", "Taxpayers, foreign rivals", "Retaliation; high cost"], ["Embargo", "Domestic producers of substitutes", "Consumers and exporters", "Retaliation; political aims, not economic"], ["Red tape", "Domestic producers", "Consumers and importers", "Hard to measure and justify; may be challenged"]];
function showT(i) {
  const [n, g, l, m] = TL[i]; $$("#tB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = g; $("#t2").textContent = l; $("#t3").textContent = m; $("#tv").textContent = `${n}: it protects domestic producers by reducing import competition (or lowering export prices). The gainers are ${g.toLowerCase()}, the losers ${l.toLowerCase()}, and the main limit is ${m.toLowerCase()}.`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, "f3", { rx: 12, ...op(0.45) }) + SV.text(210, 105, n, "lbl bd", { "text-anchor": "middle", style: "font-size:22px" });
}
$("#tB").innerHTML = TL.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
$$("#tB button").forEach((b) => (b.onclick = () => showT(+b.dataset.i)));
showT(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it a form of protectionism?", buckets: [{"label": "Protectionism"}, {"label": "Not protectionism"}], items: [{"text": "A tariff on imported steel", "b": 0}, {"text": "A subsidy on imported goods", "b": 1}, {"text": "An import quota", "b": 0}, {"text": "A general sales tax on all goods", "b": 1}, {"text": "An export subsidy", "b": 0}, {"text": "A voluntary export restraint", "b": 0}, {"text": "An embargo", "b": 0}, {"text": "Removing import duties", "b": 1}], done: "Protectionism restricts imports or supports exporters. Import subsidies and general taxes do not." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Tariff", "A tax on imports"], ["Quota", "A limit on the quantity of imports"], ["Embargo", "A ban on trade"], ["Export subsidy", "A payment to exporters per unit sold abroad"], ["Red tape", "Excessive administrative burdens on trade"], ["Protectionism", "Policy to protect domestic firms from foreign competition"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a tariff in order.", items: ["The government imposes a tariff on imports", "The price of imports rises", "Imports fall and domestic firms sell more", "Domestic output and employment rise", "Consumers pay more and a welfare loss results"], done: "Tariff raises price, shifts demand to domestic goods, costs consumers." });
Lib.calc($("#c1"), { qs: [
  {"q": "World price $40, tariff $10 and imports after the tariff 25 units. What is tariff revenue ($)?", "a": 250, "unit": "$", "tol": 1, "hint": "10 × 25.", "sol": "<b>$250</b>."},
  {"q": "A tariff of 25% is placed on a $200 import. How much is the tariff ($)?", "a": 50, "unit": "$", "tol": 0.5, "hint": "0.25 × 200.", "sol": "<b>$50</b>."},
  {"q": "The price paid in the country is therefore ($)?", "a": 250, "unit": "$", "tol": 0.5, "hint": "200 + 50.", "sol": "<b>$250</b>."},
  {"q": "Imports fall from 50 to 25 units after the tariff. What is the % fall?", "a": 50, "unit": "%", "tol": 0.5, "hint": "25 ÷ 50.", "sol": "<b>50%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A tariff is:", opts: ["A tax on imports", "A limit on imports", "A ban", "A subsidy"], a: 0, why: "Raises the price of imports." },
  { q: "An import quota:", opts: ["Limits the quantity of imports", "Taxes imports", "Subsidises exports", "Bans all trade"], a: 0, why: "A physical limit." },
  { q: "A tariff will usually:", opts: ["Raise the domestic price", "Lower the domestic price", "Raise imports", "Lower tariff revenue"], a: 0, why: "Imports become dearer." },
  { q: "Protectionism may provoke:", opts: ["Retaliation", "More free trade", "Lower prices", "Lower tariffs"], a: 0, why: "Trading partners respond." },
  { q: "A tariff is more effective if demand for imports is:", opts: ["Elastic", "Inelastic", "Perfectly inelastic", "Zero"], a: 0, why: "Imports fall by more." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Protectionism", "Protect domestic firms."],
  ["Tariff", "Tax on imports."],
  ["Quota", "Limit on imports."],
  ["Export subsidy", "Pay exporters."],
  ["Embargo", "Trade ban."],
  ["Red tape", "Excessive rules."],
  ["Tariff effect", "Price up, imports down."],
  ["Limits", "Retaliation, elasticity, costs."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A government removes its quota on imported laptops. Assuming a normal demand curve and upward-sloping supply curve for laptops, what are the likely effects on domestic laptop manufacturers? (price received, income received) (Feb/March 2022 · 12 · Q20, reworded)", opts: ["price decreases, income decreases", "price increases, income increases", "price decreases, income uncertain", "price increases, income uncertain"], a: 0, why: "More imports lower the price and reduce domestic output, so income falls." },
  { q: "What is not a form of protectionism? (Feb/March 2022 · 12 · Q26, reworded)", opts: ["embargoes", "increase in sales tax (VAT)", "subsidies on goods for export", "voluntary export restraints"], a: 1, why: "A general sales tax does not target imports. The others restrict imports or support exporters." },
  { q: "What is not an example of protectionism? (May/June 2020 · 11 · Q24, reworded)", opts: ["export subsidies", "import subsidies", "quotas", "tariffs"], a: 1, why: "Subsidising imports would encourage imports." },
  { q: "A small country imports tractors. The government decides to impose a quota on imported tractors. What is likely to be the effect on the price of imported tractors and on domestic output of tractors? (price of imported tractors, domestic output) (May/June 2021 · 11 · Q26, reworded)", opts: ["fall, fall", "increase, no change", "no change, fall", "no change, increase"], a: 3, why: "A quota restricts supply, so the price paid rises and domestic producers expand. The answer given in the paper is that import prices do not change (world price) and domestic output increases, since the country is small and the quota limits quantity." },
  { q: "What is not an aim of protectionism? (May/June 2021 · 13 · Q20, reworded)", opts: ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], a: 1, why: "Protectionism aims to cut imports and protect industries, not to raise the price of exports." },
  { q: "Which statement about trade protection is correct? (May/June 2021 · 13 · Q26, reworded)", opts: ["A tariff results in a greater decrease in demand for an import the lower is its price elasticity of demand", "Embargoes are only an effective trade barrier when the demand for imports is price-elastic", "Export subsidies to domestic firms will prevent the dumping of foreign products in the domestic market", "Quotas are less effective than tariffs for raising government revenue"], a: 3, why: "A quota raises no tax revenue unless licences are sold, while a tariff does." },
  { q: "A small country imposes no tariffs and has a perfectly elastic supply of smartphones from the rest of the world. Which statement is correct after the imposition of a tariff? (May/June 2022 · 12 · Q25, reworded)", opts: ["The domestic demand for smartphones will rise", "The domestic price of smartphones will rise", "The government will lose tax revenue", "The supply of imports will increase"], a: 1, why: "The tariff raises the price paid in the country by the amount of the tariff." },
  { q: "In a recent year, Japanese car manufacturers agreed to limit exports of cars to the USA. Which form of protectionism is this? (May/June 2022 · 12 · Q26, reworded)", opts: ["an embargo", "an export subsidy", "a quota", "voluntary export restraint"], a: 3, why: "An exporters' agreement to limit sales is a voluntary export restraint." },
  { q: "Which statement correctly describes how an import quota works? (May/June 2022 · 14 · Q20, reworded)", opts: ["It is a ban on the import of demerit goods", "It imposes strict product regulations on imports", "It is a unit tax that raises the price of imported goods", "It limits the quantity of certain imported goods"], a: 3, why: "A quota limits the quantity of imports." },
  { q: "In 2018 the United States government introduced tariffs on a wide range of imports from China. Which type of policy was the US government adopting? (May/June 2020 · 12 · Q29, reworded)", opts: ["expenditure-reducing", "expenditure-switching", "monetary", "supply-side"], a: 1, why: "Tariffs switch spending from imports to domestically produced goods." },
] });
