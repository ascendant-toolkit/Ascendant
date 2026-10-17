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
  const B = [["Private sector", "Firms and households in markets: prices allocate most goods", 30, "f1"], ["Public sector", "Government provides public and merit goods, regulates, taxes", 270, "f2"], ["Mixed economy", "Both together: how mixed varies by country", 510, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 100, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 44, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); const w = d.split(": "); w.forEach((p, i) => { o += SV.text(x + 110, 70 + i * 20, i === 0 ? p + ":" : p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 124" role="img" aria-label="A mixed economy has a private sector and a public sector">${o}</svg>`;
})();
function specDraw(x) {
  let o = SV.line(60, 70, 700, 70, "c4", { "stroke-width": 4 }) + SV.text(60, 40, "Market economy", "lbl bd") + SV.text(700, 40, "Planned economy", "lbl bd", { "text-anchor": "end" }) + SV.text(380, 40, "Mixed economies", "lbl bd", { "text-anchor": "middle" });
  o += SV.text(60, 108, "little government role", "sm") + SV.text(700, 108, "state decides almost everything", "sm", { "text-anchor": "end" });
  const px = 60 + (x / 100) * 640; o += SV.circle(px, 70, 10, "dot3") + SV.text(px, 58, Math.round(x) + "", "lbl bd", { "text-anchor": "middle" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 130" role="img" aria-label="The spectrum from market to planned economy">${specDraw(45)}</svg>`;
chainStep("#stA", "Why the market alone is not enough", ["A pure market has no government role", "Public goods are not supplied (free riders)", "Merit goods are under-consumed; demerit goods over-consumed", "Essentials may be unaffordable to those with low incomes", "Governments intervene: the economy becomes mixed"], [
  "<b>Pure market:</b> the price mechanism alone.", "<b>No revenue</b> for firms providing public goods.", "<b>Imperfect information</b> and limited incomes.", "<b>Inequality:</b> output goes to those who can pay.", "<b>The mixed economy</b> adds provision, regulation and taxes."]);
chainStep("#stB", "Government failure", ["The government intervenes to correct a market failure", "It lacks full information about the right quantity or price", "Taxes, subsidies or price controls distort prices", "Waste, shortages or surpluses, or reduced incentives follow", "The result may be a worse allocation: government failure"], [
  "<b>Good intention:</b> fix market failure.", "<b>Information problem</b> for officials.", "<b>Price distortion.</b>", "<b>Unintended consequences.</b>", "<b>Evaluation point:</b> intervention does not always improve outcomes."]);
chainStep("#stC", "Merit goods from both sectors", ["Education and healthcare are merit goods: under-consumed in a free market", "The government provides or subsidises them so everyone has access", "Public funds are limited, so state provision may not meet all demand", "Private firms provide extra capacity and choice for those who can pay", "Both sectors supply: a mixed system for merit goods"], [
  "<b>Merit goods:</b> better than people realise.", "<b>Government role:</b> access for all.", "<b>The state cannot afford everything.</b>", "<b>The private sector</b> fills gaps.", "<b>Result:</b> a mixture of public and private supply."]);

function labS() {
  if (!["gs", "so", "rg"].every((i) => $("#" + i))) return;
  const gs = +$("#gs").value, so = +$("#so").value, rg = +$("#rg").value, idx = (gs / 70) * 40 + (so / 100) * 35 + (rg / 100) * 25;
  const name = idx < 15 ? "Close to a market economy" : idx < 35 ? "Mixed, market-led" : idx < 55 ? "Mixed, government-led" : idx < 80 ? "Heavily state-led" : "Close to a planned economy";
  $("#r1").textContent = Lib.fmtN(idx, 0); $("#r2").textContent = name; $("#r3").textContent = idx < 35 ? "Efficiency and choice" : idx < 55 ? "Balance of efficiency and equity" : "Equity and provision for all";
  $("#rv").textContent = `Government spending of ${gs}% of GDP, state ownership of ${so}% of industry and regulation at ${rg}% give a government role index of ${Lib.fmtN(idx, 0)}: ${name.toLowerCase()}. ${idx < 35 ? "Prices allocate most resources; the risk is market failure and inequality." : idx < 80 ? "The market and government share the work; the risks are government failure, high taxes and reduced incentives." : "Planners allocate most resources; the risks are the lack of price signals, shortages and weak incentives."}`;
  $("#labA").innerHTML = specDraw(idx);
}
Lib.slider($("#g1"), { id: "gs", label: "Government spending, % of GDP ", min: 10, max: 70, step: 5, value: 40, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "so", label: "Share of industry owned by the state, % ", min: 0, max: 100, step: 10, value: 20, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "rg", label: "Level of regulation and price controls, % ", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + "%", onInput: labS });
labS();

chooser("h", [
  ["Providing public goods", "Free riders: the market does not supply them", "Fund and provide them from taxes", "Wrong quantity chosen because people do not reveal their valuation", 5],
  ["Providing or subsidising merit goods", "Under-consumption through imperfect information and low incomes", "Free provision, subsidies, information campaigns", "Waste, excess demand, high opportunity cost", 5],
  ["Taxing or banning demerit goods", "Over-consumption because harm is underestimated", "Taxes, bans, warnings, minimum prices", "Black markets; the tax may fall on the poor", 4],
  ["Price controls on essentials", "Prices too high for low-income households or unstable farm incomes", "Maximum or minimum prices", "Shortages or surpluses", 3],
  ["Regulating monopolies", "Market power: high prices and low output", "Competition law and price regulation", "Regulators lack information; may be captured by firms", 3],
  ["Redistributing income", "Inequality: output goes to those who can pay", "Progressive taxes and benefits", "Reduced incentives to work; cost", 3]
], (it) => `${it[0]}: the market failure is ${it[1].toLowerCase()}. The government acts through ${it[2].toLowerCase()}. A possible government failure: ${it[3].toLowerCase()}.`, "Strength of the case for intervention");
Lib.classify($("#cl1"), { prompt: "Is it a government role or a market outcome?", buckets: [{"label": "Government role in a mixed economy"}, {"label": "Market outcome"}], items: [{"text": "Providing street lighting from taxes", "b": 0}, {"text": "Firms producing what is profitable", "b": 1}, {"text": "Banning smoking in public places", "b": 0}, {"text": "Price rising when demand rises", "b": 1}, {"text": "Subsidising healthcare", "b": 0}, {"text": "Consumers choosing between brands", "b": 1}, {"text": "Regulating monopolies", "b": 0}, {"text": "Firms entering a profitable market", "b": 1}], done: "The government provides public goods, corrects failure and regulates; the market allocates through prices and profit." });
Lib.classify($("#cl2"), { prompt: "Which type of good is it?", buckets: [{"label": "Public good"}, {"label": "Merit good"}, {"label": "Demerit good"}], items: [{"text": "Street lighting", "b": 0}, {"text": "Education", "b": 1}, {"text": "Tobacco", "b": 2}, {"text": "National defence", "b": 0}, {"text": "Vaccinations", "b": 1}, {"text": "Harmful drugs", "b": 2}, {"text": "Flood defences", "b": 0}, {"text": "Healthcare", "b": 1}], done: "Public goods are non-excludable and non-rival; merit goods are under-consumed; demerit goods are over-consumed." });
Lib.order($("#o1"), { prompt: "Put the move from a pure market towards a mixed economy in order.", items: ["A pure market fails to supply public goods", "Merit goods are under-consumed and demerit goods over-consumed", "The government provides, taxes and regulates", "The economy becomes mixed", "Government failure may then need to be addressed"], done: "Market failure leads to intervention and a mixed economy." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Mixed economy", "Price mechanism plus government intervention"], ["Public sector", "The part of the economy owned or run by government"], ["Private sector", "The part owned by households and firms"], ["Nationalisation", "Transfer of a firm to state ownership"], ["Government failure", "Intervention that makes the allocation worse"], ["Spectrum", "The range between pure market and pure planned economies"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Government spending is $400bn and GDP is $1000bn. What share of GDP is government spending (%)?", "a": 40, "unit": "%", "tol": 0.1, "hint": "400 ÷ 1000.", "sol": "<b>40%</b>."},
  {"q": "A government raises $120bn in tax and spends $150bn. What is the budget deficit ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "150 − 120.", "sol": "<b>$30bn</b>."},
  {"q": "State firms produce $200bn of a $800bn GDP. What share is produced by the state (%)?", "a": 25, "unit": "%", "tol": 0.1, "hint": "200 ÷ 800.", "sol": "<b>25%</b>."},
  {"q": "Spending on healthcare is $80bn and GDP is $1600bn. What share of GDP is this (%)?", "a": 5, "unit": "%", "tol": 0.1, "hint": "80 ÷ 1600.", "sol": "<b>5%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A mixed economy combines:", opts: ["The price mechanism and government intervention", "Planning and no prices", "Only private firms", "Only state firms"], a: 0, why: "Both methods of allocation." },
  { q: "Which is provided in a mixed economy but not in a pure market?", opts: ["Public goods", "Private goods", "Luxury goods", "Substitutes"], a: 0, why: "Free riders stop market supply." },
  { q: "A disadvantage of a mixed economy is:", opts: ["Government failure", "Wide consumer choice", "Efficient competition", "Public goods are provided"], a: 0, why: "Intervention can fail." },
  { q: "Merit goods in a mixed economy are often supplied by:", opts: ["Both public and private sectors", "Only the state", "Only the market", "Only charities"], a: 0, why: "State plus private provision." },
  { q: "How mixed an economy is depends on:", opts: ["Government spending, state ownership and regulation", "Only the exchange rate", "Only population", "Only tax rates"], a: 0, why: "The size of the government role." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Mixed economy", "Markets plus government."],
  ["Spectrum", "How mixed is the economy?"],
  ["Public goods", "Government provides."],
  ["Merit goods", "State and private supply."],
  ["Demerit goods", "Taxes, bans, warnings."],
  ["Advantages", "Efficiency plus equity."],
  ["Disadvantages", "Government failure, distortion."],
  ["Nationalisation", "State ownership of a firm."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources? (Feb/March 2024 · 12 · Q4, reworded)", opts: ["Demerit goods will be over supplied", "Merit goods will be under supplied", "Private goods will not be supplied", "Public goods will not be supplied"], a: 3, why: "Public goods would not be provided at all in a pure market, which is the most serious failure." },
  { q: "What is produced in a mixed economy but not in a free market economy? (May/June 2024 · 12 · Q2, reworded)", opts: ["Demerit goods", "Free goods", "Private goods", "Public goods"], a: 3, why: "Governments provide public goods in a mixed economy; a free market would not supply them." },
  { q: "Which goods would be expected to be produced in a mixed economy? (May/June 2025 · 13 · Q5, reworded)", opts: ["private goods, public goods and goods with external benefits", "private goods and public goods only", "private goods and goods with external benefits only", "goods with external benefits only"], a: 0, why: "A mixed economy produces private goods through markets, and public goods and goods with external benefits (merit goods) through government provision or support." },
  { q: "Under which conditions are free market forces most likely to allocate resources efficiently in an economy? (the number of demerit, merit and public goods needed by consumers) (May/June 2025 · 14 · Q3, reworded)", opts: ["a few of each type", "many demerit, many merit and a few public goods", "no demerit goods, many merit goods and no public goods", "no demerit goods, no merit goods and no public goods"], a: 3, why: "Markets work best when there is no market failure, so no demerit, merit or public goods are needed." },
] });
