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

/* ---------- Openness over time ---------- */
const TY = [[1960, 24], [1970, 26], [1980, 36], [1990, 39], [2000, 47], [2008, 61], [2015, 56], [2020, 52]], TX = (y) => 90 + (y - 1960) / 60 * 600, TV = (v) => 300 - v * 3.6;
function opDraw(s) {
  let o = axes(70, 300, 730, 30, "Year", "World trade as % of world GDP (approx.)"); [0, 20, 40, 60].forEach((v) => (o += SV.text(64, TV(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.line(70, TV(v), 730, TV(v), "gr", op(0.3))));
  TY.forEach(([y]) => (o += SV.text(TX(y), 320, y, "sm", { "text-anchor": "middle" })));
  const n = Math.min(7, s.p * 7), pts = []; for (let i = 0; i <= Math.floor(n); i++) pts.push([TX(TY[i][0]), TV(TY[i][1])]); if (n % 1 > 0 && Math.floor(n) < 7) { const a = Math.floor(n), f = n - a; pts.push([TX(TY[a][0]) + (TX(TY[a + 1][0]) - TX(TY[a][0])) * f, TV(TY[a][1] + (TY[a + 1][1] - TY[a][1]) * f)]); }
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  const last = pts[pts.length - 1]; o += SV.circle(last[0], last[1], 6, "dot4");
  if (s.l > 0) o += tag(TX(1975), TV(26) + 30, "Containers, lower tariffs", "t1", s.l, "middle");
  if (s.l > 1) o += tag(TX(1993), TV(40) - 26, "China, ex-Soviet bloc open up", "t3", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += tag(TX(2008), TV(61) - 14, "2008 peak", "t4", Math.min(1, s.l - 2), "middle");
  if (s.l > 3) o += tag(TX(2017), TV(54) + 38, "Crisis, tariffs, pandemic", "t2", Math.min(1, s.l - 3), "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="World trade as a share of world GDP rising from about 24 percent in 1960 to about 60 percent in 2008 and slipping since">${opDraw({ p: 1, l: 4 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 340, label: "World trade as a share of world GDP, rising and then levelling off (approximate values)", base: { p: 0, l: 0 }, draw: opDraw, tween: 1800, dwell: 5800, steps: [
  { cap: "<b>1960 to 1980.</b> Trade grows as tariffs fall and shipping gets cheaper with containers, so trade rises from about a quarter to over a third of world output.", s: { p: 0.3, l: 1 } },
  { cap: "<b>1980 to 2008.</b> China, India and the former Soviet bloc open up, global supply chains spread and capital flows grow. Trade climbs to about 60% of world GDP.", s: { p: 0.85, l: 2 } },
  { cap: "<b>2008.</b> The peak of this wave of globalisation, just before the global financial crisis.", s: { p: 0.88, l: 3 } },
  { cap: "<b>After 2008.</b> The financial crisis, trade tensions and tariffs, and the pandemic slow the rise, and the share levels off or dips. (Approximate figures, for illustration.)", s: { p: 1, l: 4 } },
] });

/* ---------- Winners and losers ---------- */
const WG = [["Consumers", 6], ["Exporters", 4], ["Skilled workers", 3], ["Displaced workers", -5], ["Low-skill workers", -7]], WL = [["Export sectors", 5], ["Factory workers", 3], ["Local firms", -3], ["Small farmers", -4]];
function wlDraw(s) {
  let o = SV.line(60, 160, 730, 160); const bars = (set, x0, title, k, w) => { if (k <= 0) return ""; let r = SV.text(x0 + set.length * w / 2, 36, title, "lbl bd", { "text-anchor": "middle", ...op(k) }); set.forEach(([l, v], i) => { const x = x0 + i * w + 6, y = 160 - v * 12 * k; r += SV.rect(x, Math.min(y, 160), w - 14, Math.abs(y - 160), v > 0 ? "f3" : "f2", op(0.8)) + tag(x + (w - 14) / 2, v > 0 ? y - 6 : y + 16, (v > 0 ? "+" : "") + v, v > 0 ? "t3" : "t2", k, "middle") + SV.text(x + (w - 14) / 2, 278, l.split(" ").slice(0, 1).join(" "), "sm", { "text-anchor": "middle", ...op(k) }) + SV.text(x + (w - 14) / 2, 292, l.split(" ").slice(1).join(" "), "sm", { "text-anchor": "middle", ...op(k) }); }); return r; };
  o += bars(WG, 70, "High-income country (illustrative net effects)", s.a, 80) + bars(WL, 500, "Low-income country", s.b, 58);
  if (s.c > 0) o += tag(380, 314, "On average a gain, but the gains and losses fall on different people", "t4", s.c, "middle");
  return o;
}
Lib.stepper($("#stW"), { w: 760, h: 324, label: "Illustrative winners and losers from globalisation in a high-income and a low-income country", base: { a: 0, b: 0, c: 0 }, draw: wlDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>High-income country.</b> Consumers (cheaper goods), exporters and skilled workers gain. Workers in industries facing cheap imports lose jobs or wages, especially low-skilled manufacturing workers.", s: { a: 1 } },
  { cap: "<b>Low-income country.</b> Export sectors and factory workers gain jobs and income, but local firms and subsistence farmers may suffer from imports, and conditions in some factories are poor.", s: { a: 1, b: 1 } },
  { cap: "<b>Overall.</b> The net effect may be positive, but gains and losses go to different groups, so policies to retrain workers and spread the gains matter. (Values are illustrative.)", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labG() {
  if (!$("#pf") || !$("#jl")) return;
  const pf = +$("#pf").value / 100, jl = +$("#jl").value, gain = 1000 * pf, lose = jl * 0.04, net = gain - lose;
  $("#r1").textContent = "$" + Lib.fmtN(gain, 0) + "m"; $("#r2").textContent = "$" + Lib.fmtN(lose, 0) + "m"; $("#r3").textContent = (net >= 0 ? "+$" : "−$") + Lib.fmtN(Math.abs(net), 0) + "m";
  $("#rv").textContent = `A ${Lib.fmtN(pf * 100, 0)}% fall in import prices saves consumers $${Lib.fmtN(gain, 0)}m a year. ${jl} lost jobs cost workers ${jl} × $40,000 = $${Lib.fmtN(lose, 0)}m a year. ${net >= 0 ? "The net effect is positive, so the winners could in theory compensate the losers, but the benefits are spread thinly across many consumers while the costs fall heavily on a few workers and towns, which is why retraining and support matter." : "Here the loss to displaced workers outweighs the gain to consumers."}`;
  const Y = (v) => 270 - v * 0.5; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m a year", "sm");
  [["Consumers gain", gain, "f3"], ["Workers lose", lose, "f2"], ["Net", Math.max(0, net), net >= 0 ? "f1" : "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 480)); o += SV.rect(x, yy, 80, 270 - yy, c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, "$" + Lib.fmtN(v, 0) + "m", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pf", label: "Fall in import prices, % ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labG });
Lib.slider($("#g2"), { id: "jl", label: "Jobs lost in import-competing firms ", min: 0, max: 5000, step: 250, value: 1500, fmt: (v) => v.toLocaleString("en-US"), onInput: labG });
labG();

/* ---------- Lab 2 ---------- */
function labO() {
  if (!$("#xs") || !$("#ms") || !$("#fd")) return;
  const x = +$("#xs").value, m = +$("#ms").value, fd = +$("#fd").value, open_ = x + m, hit = x * fd / 100;
  $("#t1").textContent = open_ + "% of GDP"; $("#t2").textContent = "−" + Lib.fmtN(hit, 1) + "% of GDP"; $("#t3").textContent = open_ > 100 ? "Very high" : open_ > 60 ? "High" : "Moderate";
  $("#tv").textContent = `Exports are ${x}% of GDP and imports ${m}%, so openness is ${open_}% of GDP. If foreign demand falls ${fd}%, exports fall by ${fd}% of ${x}%, a direct hit of ${Lib.fmtN(hit, 1)}% of GDP (before multiplier effects). A more open economy gains from trade in good times but is more exposed to shocks abroad.`;
  const Y = (v) => 270 - v * 2; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "% of GDP", "sm");
  [["Exports", x, "f1"], ["Imports", m, "f2"], ["Direct hit", hit, "f3"]].forEach(([l, v, c], i) => { const px = 60 + i * 115, yy = Y(Math.min(v, 120)); o += SV.rect(px, yy, 80, 270 - yy, c) + SV.text(px + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(px + 40, yy - 6, Lib.fmtN(v, 1) + "%", "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "xs", label: "Exports, % of GDP ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labO });
Lib.slider($("#g4"), { id: "ms", label: "Imports, % of GDP ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labO });
Lib.slider($("#g5"), { id: "fd", label: "Fall in foreign demand, % ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labO });
labO();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it mainly a cause, a benefit or a cost of globalisation?", buckets: [{"label": "Cause"}, {"label": "Benefit"}, {"label": "Cost"}], items: [{"text": "Containerisation lowers shipping costs", "b": 0}, {"text": "Consumers pay lower prices for imported goods", "b": 1}, {"text": "Workers lose jobs when production moves to a low-wage country", "b": 2}, {"text": "Governments cut tariffs under trade agreements", "b": 0}, {"text": "Technology transfer from multinationals raises productivity", "b": 1}, {"text": "A financial crisis spreads across countries", "b": 2}, {"text": "The internet cuts the cost of global communication", "b": 0}, {"text": "Transfer of polluting production to countries with weak rules", "b": 2}], done: "Causes: cheaper transport and communication, liberalisation, MNCs. Benefits: prices, growth, technology. Costs: job losses, inequality, shocks, pollution." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Globalisation", "The growing integration of economies through trade, capital, labour and technology flows"], ["Global supply chain", "Production of a good spread across several countries"], ["Openness", "Trade (exports plus imports) as a share of GDP"], ["Trade liberalisation", "Reducing tariffs and other barriers to trade"], ["Protectionism", "Policies such as tariffs and quotas to limit imports"], ["Structural unemployment", "Unemployment from the decline of an industry"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain from cheaper transport to a global supply chain in order.", items: ["Shipping and communication costs fall", "Firms can sell and source goods in more countries", "Production moves to the lowest-cost locations", "Parts are made in different countries", "A global supply chain develops"], done: "Lower transport costs make worldwide specialisation profitable." });
Lib.calc($("#c1"), { qs: [
  {"q": "Exports are $400bn, imports are $350bn and GDP is $1,000bn. Calculate openness, (X + M) ÷ GDP, as a percentage (%).", "a": 75, "unit": "%", "tol": 0.5, "hint": "(400 + 350) ÷ 1,000.", "sol": "<b>75%</b>."},
  {"q": "Exports are 40% of GDP. Foreign demand falls by 10%. Calculate the direct fall in GDP (% of GDP).", "a": 4, "unit": "%", "tol": 0.05, "hint": "0.4 × 10.", "sol": "<b>4%</b> of GDP, before multiplier effects."},
  {"q": "Consumers spend $800m on imports and prices fall by 5%. Calculate the saving to consumers ($m).", "a": 40, "unit": "$m", "tol": 0.5, "hint": "800 × 0.05.", "sol": "<b>$40m</b>."},
  {"q": "A country's imports of manufactured goods rise and 2,000 workers each lose $30,000 a year. Calculate the total loss ($m a year).", "a": 60, "unit": "$m", "tol": 0.5, "hint": "2,000 × 30,000.", "sol": "<b>$60m</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a cause of globalisation?", opts: ["Falling transport and communication costs", "Higher tariffs", "Exchange controls", "Shorter supply chains"], a: 0, why: "Cheaper movement of goods and information integrates markets." },
  { q: "A possible cost of globalisation for high-income countries is:", opts: ["Structural unemployment in industries facing cheap imports", "Higher prices for all goods", "Lower access to technology", "Smaller markets"], a: 0, why: "Workers in import-competing sectors can lose jobs." },
  { q: "Openness is measured by:", opts: ["Exports plus imports as a share of GDP", "Exports minus imports", "The exchange rate", "The inflation rate"], a: 0, why: "It shows how much of the economy depends on trade." },
  { q: "Protectionism is a threat to globalisation because it:", opts: ["Restricts trade flows", "Lowers transport costs", "Raises FDI", "Opens markets"], a: 0, why: "Tariffs and quotas reduce trade." },
  { q: "An advantage of globalisation for consumers is:", opts: ["Lower prices and wider choice", "Fewer products", "Higher import tariffs", "Less competition"], a: 0, why: "Competition and specialisation lower prices." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Globalisation", "Growing integration of economies."],
  ["Causes", "Cheaper transport, liberalisation, MNCs."],
  ["Global supply chain", "Production across many countries."],
  ["Openness", "(Exports + imports) ÷ GDP."],
  ["Benefits", "Lower prices, growth, technology."],
  ["Costs", "Job losses, inequality, pollution, shocks."],
  ["Protectionism", "Barriers to limit imports."],
  ["Evaluation", "Gains are real but not shared equally."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is not a threat to globalisation? (May/June 2024 · 31 · Q23, reworded)", opts: ["Fear of losing jobs to immigrant workers", "Political tensions among major economies", "Stronger trade unions in industries that compete with imports", "Withdrawal of government support for inefficient industries"], a: 3, why: "Removing support for inefficient industries opens markets rather than restricting them. The other three encourage protectionism." },
  { q: "In 2021 a cargo ship carrying over 18,000 containers blocked the Suez Canal for seven days and delayed 350 ships, causing shortages around the world. Which consequence of globalisation does this best illustrate? (Oct/Nov 2023 · 32 · Q28, reworded)", opts: ["Cheaper products for consumers", "Greater choice of products", "Increased interdependence between countries", "Increased migration of labour"], a: 2, why: "A disruption in one place spread because supply chains link countries together." },
  { q: "What is a likely result of globalisation? (Oct/Nov 2024 · 32 · Q30, reworded)", opts: ["Absolute advantage replaces comparative advantage as the basis for trade", "Firms' supply chains are shortened", "Trade is less exposed to international shocks", "Higher standards of living"], a: 3, why: "Trade and growth raise real incomes, although not automatically for everyone. Supply chains lengthen and exposure to shocks increases." },
  { q: "What would increase structural unemployment in the manufacturing sector of the US? (Oct/Nov 2021 · 33 · Q21, reworded)", opts: ["Asian exporters of manufactured goods to the US lower their labour costs per unit of output", "Tariffs on Asian manufacturing imports rise", "The share of US manufacturing workers in unions falls", "The US dollar's real effective exchange rate against Asian currencies falls"], a: 0, why: "Cheaper imports reduce demand for US-made goods. Tariffs and a lower real exchange rate would protect US producers." },
  { q: "The US introduced tariffs on a wide range of imports from China in 2018. Which type of policy was this? (Oct/Nov 2024 · 32 · Q25, reworded)", opts: ["Expenditure-reducing", "Expenditure-switching", "Expansionary monetary", "Contractionary monetary"], a: 1, why: "Tariffs switch spending from imports to domestically produced goods." },
  { q: "A country imposes a tariff on steel imports. What is the likely effect on its economy? (May/June 2025 · 31 · Q25, reworded)", opts: ["Its steel exports become more price competitive", "Productive inefficiency in its steel industry", "An improvement in its terms of trade", "A fall in producer surplus for its steel producers"], a: 1, why: "Protection reduces competition, so domestic producers may have less incentive to cut costs." },
] });
