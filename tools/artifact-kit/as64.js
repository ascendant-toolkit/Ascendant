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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl) {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, "Strength of the case: " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

chainStep("#stA", "How infant industry protection is meant to work", ["A new industry cannot compete with established foreign firms", "A tariff or quota protects it from import competition", "It grows and gains economies of scale", "Costs fall and it becomes efficient", "Protection is removed and the industry competes alone"], [
  "<b>The problem:</b> a new industry has high unit costs because it is small.", "<b>Temporary protection</b> raises the price of imports, so domestic sales can grow.", "<b>Growth</b> lets the firm spread its fixed costs and gain economies of scale.", "<b>Falling unit costs</b> may allow it to match foreign prices.", "<b>In theory</b> the protection ends and the industry competes without help."]);
chainStep("#stB", "How protection may reduce welfare", ["The government protects an industry for a long time", "Less competition reduces the pressure to cut costs", "The industry may remain inefficient (X-inefficiency)", "Consumers pay higher prices and have less choice", "Trading partners may retaliate against exports"], [
  "<b>Long protection</b> may become hard to remove because the industry lobbies to keep it.", "<b>Less competition</b> reduces the incentive to innovate.", "<b>Costs stay high</b>, so the industry may never become competitive.", "<b>Higher prices</b> reduce real incomes and living standards.", "<b>Retaliation</b> can hurt exporters, and the country may end up worse off overall."]);

chooser("g", [
  ["Infant industry", "Temporary support lets a new industry reach scale", "May never become efficient; hard to remove", "Time limit and a realistic path to lower costs", 4],
  ["Declining industry", "Gives workers and capital time to move", "Delays change and wastes resources", "Support should be short and linked to retraining", 3],
  ["Strategic industry", "Secures supply of defence or food", "Almost any industry may be called strategic", "A genuine security risk and no alternative suppliers", 4],
  ["Anti-dumping", "Stops sales below cost that drive out rivals", "Hard to prove; consumers lose cheap goods", "Clear evidence of below-cost selling", 3],
  ["Current account deficit", "Fewer imports may narrow the deficit", "Retaliation; inelastic demand; does not fix the cause", "Elastic demand for imports and no retaliation", 2],
  ["Government revenue", "Tariffs can raise tax income", "A high tariff reduces imports and so revenue", "Limited alternative sources of tax", 2]
], (it) => `${it[0]}: the best case is that ${it[1].toLowerCase()}. The limit is that ${it[2].toLowerCase()}. It is strongest when ${it[3].toLowerCase()}.`);

chooser("h", [
  ["Young manufacturing industry in a developing economy", "Protection (temporary and targeted)", "Cannot reach scale against established foreign firms", "A clear plan for removal, and whether costs actually fall", 4],
  ["Large efficient exporter", "Free trade", "Gains from specialisation are large and retaliation would hurt exports", "A sudden surge of dumped imports", 4],
  ["Food supply in a small island economy", "Some protection (strategic)", "Security of supply matters in a crisis", "Whether imports can be stored or diversified", 3],
  ["Long-declining coal industry", "Short-term protection, then free trade", "Gives workers time to retrain", "Whether the support lasts for decades", 3],
  ["Country with a large current account deficit", "Depends on causes", "Protection may not fix weak competitiveness", "Elasticity of demand for imports and retaliation", 2]
], (it) => `In "${it[0].toLowerCase()}", the stronger side may be: ${it[1].toLowerCase()}. The main reason: ${it[2].toLowerCase()}. This could change with: ${it[3].toLowerCase()}.`);
Lib.classify($("#cl1"), { prompt: "Is this an argument for or against protectionism?", buckets: [{"label": "For protectionism"}, {"label": "Against protectionism"}], items: [{"text": "It gives a new industry time to reach economies of scale", "b": 0}, {"text": "It reduces specialisation and world output", "b": 1}, {"text": "It stops foreign firms selling below cost", "b": 0}, {"text": "It raises prices and reduces choice for consumers", "b": 1}, {"text": "It protects industries vital for security", "b": 0}, {"text": "It may provoke retaliation from trading partners", "b": 1}, {"text": "It gives workers in a declining industry time to retrain", "b": 0}, {"text": "It protects inefficient firms from competition", "b": 1}], done: "The arguments for protect particular industries or aims; the arguments against stress efficiency, prices and retaliation." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Infant industry", "A new industry that may need temporary protection to grow"], ["Sunset industry", "An industry in long-term decline"], ["Strategic industry", "An industry important for national security"], ["Dumping", "Selling abroad at a price below cost"], ["Retaliation", "A trading partner's response with its own trade barriers"], ["X-inefficiency", "Lack of cost-cutting pressure when firms are protected from competition"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in the infant industry argument in order.", items: ["A new industry has high costs because it is small", "A tariff protects it from foreign competition", "Its sales grow and it gains economies of scale", "Unit costs fall", "Protection is removed and it competes on its own"], done: "Temporary protection should allow growth, scale and lower costs." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country exports $600m and imports $800m of goods. What is the trade deficit ($m)?", "a": 200, "unit": "$m", "tol": 0.5, "hint": "800 - 600.", "sol": "<b>$200m</b>."},
  {"q": "A tariff cuts imports by 15% from $800m (exports unchanged at $600m). What is the new trade deficit ($m)?", "a": 80, "unit": "$m", "tol": 0.5, "hint": "Imports = 0.85 × 800 = 680.", "sol": "Imports $680m, so the deficit is <b>$80m</b>."},
  {"q": "A 20% tariff is charged on $500m of imports. What is the tariff revenue ($m)?", "a": 100, "unit": "$m", "tol": 0.5, "hint": "0.2 × 500.", "sol": "<b>$100m</b>."},
  {"q": "A foreign firm sells 1000 units at $60 against a cost of $80. How much below cost is the firm selling in total ($)?", "a": 20000, "unit": "$", "tol": 1, "hint": "(80 - 60) × 1000.", "sol": "<b>$20 000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An infant industry is:", opts: ["A new industry that may need temporary protection", "A declining industry", "A foreign industry", "A government-owned industry"], a: 0, why: "Young and small." },
  { q: "Dumping means:", opts: ["Selling below cost in another country", "Selling at high prices", "Banning imports", "Taxing exports"], a: 0, why: "A below-cost export." },
  { q: "An argument against protectionism is:", opts: ["It may raise prices for consumers", "It protects infant industries", "It guards strategic industries", "It stops dumping"], a: 0, why: "Higher prices and less choice." },
  { q: "Protecting a sunset industry mainly aims to:", opts: ["Give workers time to adjust", "Raise exports", "Cut taxes", "Increase competition"], a: 0, why: "Slows the decline." },
  { q: "A risk of protectionism is:", opts: ["Retaliation by trading partners", "Lower tariffs abroad", "More competition", "Lower costs for protected firms"], a: 0, why: "Trading partners may respond." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Infant industry", "New; needs time."],
  ["Sunset industry", "Declining; slow the fall."],
  ["Strategic industry", "Security."],
  ["Dumping", "Below-cost exports."],
  ["For protection", "Targeted and temporary."],
  ["Against protection", "Prices, efficiency, retaliation."],
  ["X-inefficiency", "No pressure to cut costs."],
  ["Judgement", "Depends on the context."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement is not a valid reason why a country may impose protectionist measures? (May/June 2025 · 12 · Q26, reworded)", opts: ["to allow a newly developed domestic industry to grow to a viable size", "to enable a country to retain control of an industry it regards as being of strategic importance", "to give consumers a wider choice of goods and services", "to give time for workers in a declining domestic industry to find alternative employment"], a: 2, why: "Protection restricts imports, so it narrows rather than widens consumer choice." },
  { q: "Which argument in favour of protectionism is not generally regarded as economically valid? (May/June 2025 · 13 · Q26, reworded)", opts: ["Once the protected industry becomes established, it will produce efficiently.", "It prevents heavily subsidised imports from competing unfairly against domestic goods.", "It provides time for the protected industry's workers to be retrained for other work.", "It increases the standard of living of the population in general."], a: 3, why: "Protection usually raises prices, so it is not generally accepted that it raises living standards across the population." },
  { q: "What is not an aim of protectionism? (May/June 2021 · 13 · Q20, reworded)", opts: ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], a: 1, why: "Protectionism aims to cut imports and protect industries, not to raise export prices." },
  { q: "In which economic context is the term 'protectionism' usually applied? (Oct/Nov 2020 · 12 · Q20, reworded)", opts: ["the protection of consumers against excessive prices", "the protection of employees against exploitation by multinational companies", "the protection of local producers against foreign competitors", "the protection of the foreign exchange rate against currency speculators"], a: 2, why: "Protectionism shields local producers from foreign competition." },
  { q: "What is not an example of protectionism? (Oct/Nov 2024 · 12 · Q28, reworded)", opts: ["the European Union (EU) requiring goods imported into member states to meet safety standards", "the Pakistan government increasing the rate of goods and services tax (GST) on some exported goods from 2% to 5%", "the Nigeria government banning the import of packaged sugar", "the US imposing a 35% tariff on tyres imported from China"], a: 1, why: "A tax on exports does not protect domestic producers from import competition." },
  { q: "Two statements describing forms of protectionism a government can use are listed. Statement 1: there is a total ban on imports. Statement 2: all imported goods have to be of a specified standard. Which combination correctly describes these two statements? (statement 1, statement 2) (Oct/Nov 2024 · 13 · Q28, reworded)", opts: ["administrative barrier, import quota", "administrative barrier, embargo", "embargo, administrative barrier", "embargo, import quota"], a: 2, why: "A total ban is an embargo; a required standard is an administrative barrier." },
] });
