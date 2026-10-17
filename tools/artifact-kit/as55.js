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

const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}

const adLab = { x: "Real output (Y)", y: "Price level", D1: "AD1", D2: "AD2", S1: "SRAS1", S2: "SRAS2", P1: "P1", Q1: "Y1", P2: "P2", Q2: "Y2" };
function adasPlot(st, o = {}) {
  const l = st.l || 0, ln = o.lras !== false;
  let s = sdPlot({ d: st.a || 0, s: st.s || 0, g: st.g === undefined ? 1 : st.g, n: st.n === undefined ? 1 : st.n }, adLab);
  if (ln) s += SV.line(SDX(75 + l), SDY(0), SDX(75 + l), SDY(100), "c4", { "stroke-width": 3, "stroke-dasharray": "7 4" }) + tag(SDX(75 + l) + 6, SDY(98), "LRAS", "c4");
  return s;
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
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

$("#pic1").innerHTML = (() => {
  const B = [["Interventionist", "Government spends: education, training, infrastructure, research", 30, "f1"], ["Market-based", "Incentives and competition: tax cuts, deregulation, privatisation", 270, "f2"], ["Result", "Productivity and capacity rise: LRAS shifts right", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 110, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 52, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }); d.split(": ").forEach((p, i) => { o += SV.text(x + 110, 80 + i * 20, i === 0 ? p + ":" : p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 150" role="img" aria-label="Interventionist and market-based tools both raise productivity and capacity">${o}</svg>`;
})();
chainStep("#stA", "Government spending on training", ["The government funds training and apprenticeships", "Workers gain skills that employers need", "Labour productivity rises and structural unemployment falls", "Unit costs fall and potential output rises", "LRAS shifts to the right: long-run growth"], [
  "<b>Interventionist policy:</b> the state pays for training.", "<b>Human capital</b> improves: the quality of labour rises.", "<b>More output per worker</b> and a better match of skills and jobs.", "<b>Firms can produce more</b> at lower cost.", "<b>Potential output grows</b>, but only after years of delay."]);
chainStep("#stB", "Deregulation and competition", ["The government removes barriers to entry and red tape", "More firms can enter the market", "Competition increases", "Firms cut costs and innovate to survive", "Efficiency and capacity rise; prices may fall"], [
  "<b>Market-based policy</b> that reduces the role of rules.", "<b>Entry</b> becomes cheaper and easier.", "<b>Rivals</b> compete for customers.", "<b>Efficiency</b> rises under pressure.", "<b>The risk:</b> weaker consumer, worker or environmental protection."]);
chainStep("#stC", "A tax cut as a supply-side incentive", ["Income tax rates on earnings are cut", "The reward for working rises; the opportunity cost of leisure rises", "More people join the labour force and some work longer hours", "The quantity of labour supplied rises", "Potential output rises, if jobs are available"], [
  "<b>Supply-side aim:</b> incentives, not spending.", "<b>Incentive effect</b> on work effort.", "<b>Participation</b> and hours increase.", "<b>The labour supply</b> grows.", "<b>The limit:</b> people may simply spend the extra income (a demand effect), and jobs must exist."]);

function labT() {
  if (!["cs", "gn", "dl"].every((i) => $("#" + i))) return;
  const cost = +$("#cs").value, gain = +$("#gn").value, dl = +$("#dl").value; let cum = -cost, first = null, rows = [];
  for (let y = 1; y <= 10; y++) { if (y > dl) cum += gain; rows.push(cum); if (cum >= 0 && first === null) first = y; }
  $("#r1").textContent = Lib.fmtN(cost / gain, 1) + " years"; $("#r2").textContent = (cum >= 0 ? "+" : "−") + "$" + Lib.fmtN(Math.abs(cum), 0) + "m"; $("#r3").textContent = first === null ? "None in 10 years" : "Year " + first;
  $("#rv").textContent = `The programme costs $${cost}m now and raises output by $${gain}m a year, starting after a delay of ${dl} years. It takes ${Lib.fmtN(cost / gain, 1)} years of gains to repay the cost, so the first net gain is ${first === null ? "beyond year 10" : "in year " + first}. After 10 years the net result is ${cum >= 0 ? "+" : "−"}$${Lib.fmtN(Math.abs(cum), 0)}m. A longer delay or lower gain makes supply-side spending harder to justify.`;
  const mx = Math.max(cost, Math.abs(Math.min(...rows)), Math.max(...rows), 1), Y = (v) => 110 - (v / mx) * 85; let o = SV.line(30, Y(0), 400, Y(0));
  rows.forEach((v, i) => (o += SV.rect(40 + i * 35, v >= 0 ? Y(v) : Y(0), 26, Math.max(2, Math.abs(Y(v) - Y(0))), v >= 0 ? "f2" : "f3", op(0.7))));
  o += SV.text(30, 205, "Cumulative net gain by year (1 to 10)", "sm"); $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "cs", label: "Cost of the programme, $m ", min: 20, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labT });
Lib.slider($("#g2"), { id: "gn", label: "Yearly gain once it works, $m ", min: 5, max: 60, step: 5, value: 25, fmt: (v) => v, onInput: labT });
Lib.slider($("#g3"), { id: "dl", label: "Delay before gains start, years ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: labT });
labT();

chooser("h", [
  ["Education and training", "Interventionist; labour (quality)", "Raises skills and productivity", "Costly; years before payoff; skills may not match", 5],
  ["Infrastructure", "Interventionist; capital", "Lowers costs and opens markets", "High cost; long delay; raises the deficit", 4],
  ["Research and technology support", "Interventionist; capital and enterprise", "Faster innovation", "Uncertain returns", 3],
  ["Lower income tax", "Market-based; labour (quantity)", "Raises the reward for work", "Revenue falls; may widen inequality", 3],
  ["Deregulation", "Market-based; enterprise", "More competition and lower costs", "Weaker consumer or environmental protection", 4],
  ["Privatisation", "Market-based; capital and enterprise", "Profit motive and competition cut costs", "Possible private monopoly power", 4],
  ["Reduced benefits for the long-term unemployed", "Market-based; labour (quantity)", "Encourages people to look for work", "Hardship; may not create jobs", 2],
  ["Free trade zones", "Market-based; capital and enterprise", "Attract investment and cut bureaucracy", "May only move activity around", 3]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. It raises supply by ${it[2].toLowerCase()}. The main drawback is that it ${it[3].toLowerCase()}.`, "Long-run effect on capacity");
chooser("k", [
  ["Funding apprenticeships", "Supply-side", "Raise skills and productivity", "LRAS and SRAS", 5],
  ["Cutting the interest rate to boost spending", "Demand-side", "Raise total spending", "AD", 1],
  ["A tax cut to raise work incentives", "Supply-side", "Raise labour supply", "LRAS", 4],
  ["A tax cut to boost spending in a recession", "Demand-side", "Raise consumption", "AD", 1],
  ["Building new railways to cut firms' costs", "Supply-side (also boosts AD in the short run)", "Raise productive capacity", "LRAS (and AD at first)", 4],
  ["Raising benefits to support spending", "Demand-side", "Raise consumption", "AD", 1]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. Its aim is to ${it[2].toLowerCase()}, so the curve that shifts is ${it[3]}.`, "How supply-side the policy is (5 = fully)");
Lib.classify($("#cl1"), { prompt: "Market-based or interventionist?", buckets: [{"label": "Market-based"}, {"label": "Interventionist"}], items: [{"text": "Cutting income tax rates", "b": 0}, {"text": "Government funding for apprenticeships", "b": 1}, {"text": "Privatising a state-owned railway", "b": 0}, {"text": "Building a new port", "b": 1}, {"text": "Removing barriers to entry for new firms", "b": 0}, {"text": "Grants for research and development", "b": 1}, {"text": "Making it easier to hire and fire workers", "b": 0}, {"text": "Funding health services", "b": 1}], done: "Market-based measures change incentives and competition; interventionist measures involve the government spending to improve the supply side." });
Lib.classify($("#cl2"), { prompt: "Supply-side or demand-side?", buckets: [{"label": "Supply-side"}, {"label": "Demand-side"}], items: [{"text": "Funding apprenticeships", "b": 0}, {"text": "Cutting interest rates", "b": 1}, {"text": "Building new ports", "b": 0}, {"text": "A cut in VAT to boost spending", "b": 1}, {"text": "Tax relief for R&D", "b": 0}, {"text": "Deregulating industries", "b": 0}, {"text": "Higher government spending on benefits", "b": 1}, {"text": "Privatising state industries", "b": 0}], done: "Supply-side policies raise capacity and productivity; demand-side policies change spending." });
Lib.order($("#o1"), { prompt: "Put the long-run effect of training in order.", items: ["The government funds training", "Workers' skills and productivity rise", "Unit costs fall and capacity rises", "LRAS shifts to the right", "Real output rises and the price level falls"], done: "Training raises productivity, shifting LRAS right." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Supply-side policy", "Measures to increase aggregate supply"], ["Productivity", "Output per unit of input"], ["Human capital", "Skills and knowledge of the workforce"], ["Deregulation", "Removing rules to increase competition and efficiency"], ["Privatisation", "Transferring state industries to private ownership"], ["Productive capacity", "The maximum output the economy can produce"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Potential output is 800 and a supply-side package raises it by 5%. What is the new potential output?", "a": 840, "unit": "", "tol": 0.5, "hint": "800 × 1.05.", "sol": "<b>840</b>."},
  {"q": "A training programme costs $30m and raises output per worker by $200 for 100,000 workers. What is the extra output ($m)?", "a": 20, "unit": "$m", "tol": 0.1, "hint": "200 × 100,000.", "sol": "<b>$20m</b> a year."},
  {"q": "How many years does it take for the extra output to cover the cost?", "a": 1.5, "unit": "years", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5 years</b>."},
  {"q": "A worker produces 40 units a day and productivity rises 15%. How many units a day now?", "a": 46, "unit": "units", "tol": 0.1, "hint": "40 × 1.15.", "sol": "<b>46 units</b>."},
  {"q": "A firm's labour costs are 50% of its costs. Productivity rises 10%, so labour cost per unit falls 9.1%. By roughly how much do total unit costs fall (%)?", "a": 4.5, "unit": "%", "tol": 0.2, "hint": "0.5 × 9.1.", "sol": "<b>4.5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A supply-side policy aims to:", opts: ["Increase aggregate supply", "Reduce aggregate supply", "Raise interest rates", "Cut government spending only"], a: 0, why: "Raise capacity." },
  { q: "Which is a supply-side policy?", opts: ["Spending on education and training", "A cut in interest rates", "A rise in VAT", "A rise in the money supply"], a: 0, why: "Human capital." },
  { q: "Privatisation is:", opts: ["A market-based supply-side policy", "A demand-side policy", "An interventionist policy", "A tax"], a: 0, why: "It aims to raise efficiency." },
  { q: "A limit of supply-side policy is:", opts: ["It takes a long time to work", "It reduces productivity", "It always raises inflation", "It has no cost"], a: 0, why: "Time lags." },
  { q: "A tax cut is supply-side if its aim is to:", opts: ["Raise incentives to work and invest", "Boost spending in a recession", "Reduce the budget deficit", "Raise import demand"], a: 0, why: "Incentive effect." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Supply-side", "Raise AS and LRAS."],
  ["Interventionist", "Government spends: training, infrastructure."],
  ["Market-based", "Incentives and competition."],
  ["Productivity", "Output per unit of input."],
  ["Deregulation", "Remove rules, raise competition."],
  ["Privatisation", "Sell state firms."],
  ["Limits", "Cost, time lags, uncertainty."],
  ["Demand-side", "Changes spending, not capacity."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What can be considered an expansionary supply-side policy? (Feb/March 2024 · 12 · Q23, reworded)", opts: ["an increase in government expenditure on training", "an increase in sales tax", "an increase in the rate of interest", "an increase of the exchange rate"], a: 0, why: "Training raises productivity and capacity, shifting aggregate supply right." },
  { q: "What is not an example of an expansionary supply-side policy? (May/June 2025 · 11 · Q24, reworded)", opts: ["a reduction in government spending on training", "an increase in support for technological improvement", "a reduction in payments to the unemployed", "an increase in privatisation of industry"], a: 0, why: "Cutting training would reduce skills. The others aim to raise supply." },
  { q: "A government cuts income tax. Why might this be seen as an example of a supply-side policy? (Feb/March 2025 · 12 · Q21, reworded)", opts: ["Real incomes are increased", "The costs of businesses are reduced", "The opportunity cost of unemployment has increased", "The standard of living has improved"], a: 2, why: "Lower income tax raises the reward for working, so the opportunity cost of not working rises, encouraging people into work." },
  { q: "What is most likely to occur when the government privatises public sector organisations? (May/June 2020 · 13 · Q14, reworded)", opts: ["Consumer choice will increase", "Employment will increase in the short run", "Innovation will be discouraged", "The production of public goods will increase"], a: 0, why: "Privatisation usually increases competition and choice." },
  { q: "Which argument has often been used to justify the privatisation of state enterprises? (Feb/March 2020 · 12 · Q14, reworded)", opts: ["Private firms can produce the same outputs using fewer inputs.", "Private firms try to earn large profits.", "State enterprises are always monopolies which exploit consumers.", "State enterprises cannot operate without government subsidies."], a: 0, why: "The efficiency argument: the profit motive and competition reduce costs." },
  { q: "Which combination identifies a main aim of supply-side policy and a measure used to achieve this target? (main aim, policy measure) (May/June 2021 · 13 · Q28, reworded)", opts: ["economic growth, deregulation", "full employment, increasing the money supply", "income equality, more progressive taxation", "stable prices, decreasing interest rates"], a: 0, why: "Deregulation is a supply-side measure aimed at growth. The others are demand-side or distribution policies." },
  { q: "A country increases its spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect of these changes on human capital and physical capital? (May/June 2025 · 12 · Q4, reworded)", opts: ["human capital decreases, physical capital decreases", "human capital decreases, physical capital increases", "human capital increases, physical capital decreases", "human capital increases, physical capital increases"], a: 2, why: "Education and training raise human capital. Taxes on imported machinery make capital goods dearer, so physical capital is likely to fall." },
  { q: "What would supporters of a nationalised public transport service expect to be the most likely outcome from the privatisation of train and bus services? (May/June 2020 · 11 · Q16, reworded)", opts: ["fewer destinations served by trains and buses", "lower fares", "more frequent services to all destinations", "more people employed in public transport services"], a: 0, why: "Supporters of nationalisation would expect private firms to drop unprofitable routes." },
] });
