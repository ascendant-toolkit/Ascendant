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

$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A depreciation shifts AD to the right and may shift SRAS to the left">${adasPlot({ a: 20, s: -20, g: 1, n: 1, lras: false })}</svg>`;
function dpDraw(s) { return adasPlot({ a: s.a, s: s.s, g: 1, n: s.n, lras: false }); }
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A depreciation shifts AD right and may shift SRAS left", base: { a: 0, s: 0, n: 0 }, draw: dpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> AD and SRAS meet at output 50 and price level 50.", s: { a: 0, s: 0, n: 0 } },
  { cap: "<b>The currency depreciates.</b> Exports are cheaper, imports dearer, net exports rise and <b>AD shifts right</b>. Output rises to 60 and the price level to 58 (demand-pull).", s: { a: 20, s: 0, n: 1 } },
  { cap: "<b>Imported inputs cost more.</b> If the economy depends on imports, <b>SRAS shifts left</b> as well, adding cost-push pressure.", s: { a: 20, s: -20, n: 1 } },
  { cap: "<b>Net effect:</b> the price level rises to 66 and output stays at 50: the cost-push effect has offset the output gain.", s: { a: 20, s: -20, n: 1 } },
] });
chainStep("#stB", "The chain of effects of an appreciation", ["The exchange rate rises", "Imports are cheaper; exports are dearer abroad", "Net exports fall and AD shifts left", "Output and employment may fall", "Import costs fall, so inflation may be lower"], [
  "<b>An appreciation</b> raises the value of the currency.", "<b>Relative prices change:</b> import prices fall and export prices rise in foreign currency.", "<b>Net exports fall</b> if demand is elastic enough, shifting AD left.", "<b>Lower AD</b> could reduce output and jobs, especially in export industries.", "<b>Cheaper imports</b> lower costs, so SRAS may shift right and inflation falls."]);

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const sum = +$("#g1v").value / 10, imp = +$("#g2v").value, a = Math.max(-15, 30 * (sum - 1)), s = -imp, e = sdEq(a, s);
  $("#r1").textContent = (a >= 0 ? "+" : "") + Lib.fmtN(a, 1); $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = Lib.fmtN(e.p, 1);
  $("#rv").textContent = (sum > 1 ? `The sum of the elasticities is ${Lib.fmtN(sum, 1)}, above one, so net exports rise and AD shifts right. ` : sum < 1 ? `The sum of the elasticities is ${Lib.fmtN(sum, 1)}, below one, so the trade balance may worsen and AD shifts left. ` : "The sum of the elasticities is one, so net exports are unchanged. ") + (imp > 0 ? `Dearer imported inputs shift SRAS left by ${imp}. ` : "No reliance on imported inputs, so SRAS is unchanged. ") + `Output is ${Lib.fmtN(e.q, 1)} and the price level ${Lib.fmtN(e.p, 1)}.`;
  $("#labA").innerHTML = adasPlot({ a, s, g: 1, n: 1, lras: false });
}
Lib.slider($("#g1"), { id: "g1v", label: "Sum of price elasticities (PEDx + PEDm) × 10 ", min: 4, max: 20, step: 2, value: 14, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Reliance on imported inputs (SRAS shift left) ", min: 0, max: 20, step: 5, value: 5, fmt: (v) => v, onInput: labA });
labA();

chooser("h", [
  ["Exports rise (depreciation)", "Up", "Demand for exports is elastic", "Short run slow; long run larger", 4],
  ["Imports fall (depreciation)", "Down in volume, up in price", "Few close domestic substitutes weakens this", "Short run slow; long run larger", 3],
  ["Cost-push inflation (depreciation)", "Up", "Reliance on imported inputs", "Short run, fast", 4],
  ["AD rises (depreciation)", "Up", "PEDx + PEDm above one and spare capacity", "Medium run", 4],
  ["Trade balance worsens first (J-curve)", "Down, then up", "Contracts and habits delay adjustment", "Months to a few years", 3],
  ["Lower inflation (appreciation)", "Down", "Imports are a large share of spending", "Short run", 3],
  ["Exporters lose orders (appreciation)", "Down", "Demand for exports is elastic", "Short to medium run", 4]
], (it) => `${it[0]}: the direction is ${it[1].toLowerCase()}. It mainly depends on this condition: ${it[2].toLowerCase()}. Time frame: ${it[3].toLowerCase()}.`, "Likely size of the effect");
Lib.classify($("#cl1"), { prompt: "Is the effect more likely after a depreciation or after an appreciation?", buckets: [{"label": "Depreciation"}, {"label": "Appreciation"}], items: [{"text": "Exports become cheaper abroad", "b": 0}, {"text": "Imported raw materials become cheaper", "b": 1}, {"text": "Cost-push inflation pressure rises", "b": 0}, {"text": "Net exports and AD may fall", "b": 1}, {"text": "The terms of trade deteriorate", "b": 0}, {"text": "Manufacturers selling abroad lose orders", "b": 1}, {"text": "A current account deficit may narrow", "b": 0}, {"text": "Downward pressure on the price level", "b": 1}], done: "A depreciation helps exports and raises import prices; an appreciation does the reverse." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Marshall-Lerner condition", "The sum of the price elasticities of exports and imports exceeds one"], ["J-curve", "The trade balance worsens before it improves after a depreciation"], ["Net exports", "Exports minus imports"], ["Cost-push inflation", "Inflation caused by rising costs of production"], ["Terms of trade", "The ratio of export prices to import prices"], ["Expenditure switching", "Moving spending from imports to domestic goods"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a depreciation on output in order.", items: ["The exchange rate falls", "Exports become cheaper and imports dearer", "Net exports rise", "AD shifts right", "Real output and employment may rise"], done: "Relative prices change, net exports rise, AD and output rise." });
Lib.calc($("#c1"), { qs: [
  {"q": "PED of exports is 0.8 and PED of imports is 0.5. What is the sum?", "a": 1.3, "unit": "", "tol": 0.01, "hint": "0.8 + 0.5.", "sol": "<b>1.3</b>, above one, so the Marshall-Lerner condition is met."},
  {"q": "The terms of trade index was 100 and the price of exports falls 8% with import prices unchanged. What is the new index?", "a": 92, "unit": "", "tol": 0.1, "hint": "100 × 0.92.", "sol": "<b>92</b>."},
  {"q": "Exports are $120bn, imports $150bn. After a depreciation, exports rise by 10% and imports fall by 5% in value. What is the new trade balance ($bn)?", "a": -10.5, "unit": "$bn", "tol": 0.1, "hint": "132 − 142.5.", "sol": "Exports $132bn, imports $142.5bn, so <b>-$10.5bn</b>."},
  {"q": "A firm imports inputs costing $1000 and the currency depreciates by 10% against the supplier's currency (so inputs cost 10% more). What is the new cost ($)?", "a": 1100, "unit": "$", "tol": 0.5, "hint": "1000 × 1.10.", "sol": "<b>$1100</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A depreciation makes imports:", opts: ["Dearer in domestic currency", "Cheaper", "Unchanged", "Free"], a: 0, why: "Each unit of foreign currency costs more." },
  { q: "The Marshall-Lerner condition is that:", opts: ["PEDx + PEDm is above 1", "PEDx is above 1 only", "PEDm is below 1", "Elasticities are zero"], a: 0, why: "Then net exports improve." },
  { q: "An appreciation is likely to:", opts: ["Lower import prices", "Raise import prices", "Lift exports", "Raise inflation"], a: 0, why: "Imports cost less in domestic currency." },
  { q: "Cost-push inflation after a depreciation is more likely if:", opts: ["The economy relies on imported inputs", "It has many natural resources", "Imports are small", "There is spare capacity"], a: 0, why: "Imported inputs cost more." },
  { q: "A depreciation will usually cause the terms of trade to:", opts: ["Deteriorate", "Improve", "Stay the same", "Double"], a: 0, why: "Export prices fall relative to import prices." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Depreciation", "Cheaper exports, dearer imports."],
  ["Appreciation", "Dearer exports, cheaper imports."],
  ["Marshall-Lerner", "PEDx + PEDm above 1."],
  ["J-curve", "Worse first, then better."],
  ["AD effect", "Net exports up, AD right."],
  ["AS effect", "Import costs up, SRAS left."],
  ["Spare capacity", "Output rises; else prices rise."],
  ["Judge", "Elasticity, time, inputs."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An economy has an unemployment rate of 8%, an increase of 2% from the previous year. At the same time, the current account deficit rose from 3% of GDP to 4% of GDP. What would be most likely to reduce both unemployment and the current account deficit? (Feb/March 2024 · 12 · Q21, reworded)", opts: ["decrease government spending", "depreciation of the currency", "increase indirect taxation", "increase interest rates"], a: 1, why: "A depreciation could raise exports and reduce imports, boosting AD, output and employment while narrowing the deficit." },
  { q: "A government decides to allow the country's currency to depreciate to remove the deficit on its current account of the balance of payments. What is the most likely reason why this would not work? (Feb/March 2024 · 12 · Q25, reworded)", opts: ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], a: 3, why: "High trade barriers could limit the rise in exports." },
  { q: "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation) (May/June 2021 · 12 · Q27, reworded)", opts: ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], a: 3, why: "A worse current account tends to lower the exchange rate, which raises import costs and cost-push inflation." },
  { q: "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency? (May/June 2021 · 13 · Q25, reworded)", opts: ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], a: 1, why: "If the sum of the elasticities is below one, the Marshall-Lerner condition fails." },
  { q: "The table gives combinations of the price elasticity of demand for exports and for imports. Following a devaluation, under which combination would the current account worsen? (exports, imports) (May/June 2022 · 12 · Q24, reworded)", opts: ["0.3 and 0.3", "0.2 and 0.9", "0.6 and 0.5", "1.2 and 1.2"], a: 0, why: "The sum is 0.6, which is below one, so the trade balance worsens." },
  { q: "Why might a government wish to increase the value of its foreign exchange rate when the sum of the price elasticity of demand for imports and exports is greater than 1? (May/June 2021 · 11 · Q22, reworded)", opts: ["to attract more tourists into the country", "to improve the current account of the balance of payments in the long run", "to increase inflation if the country is in recession", "to make imported raw materials cheaper"], a: 3, why: "A higher exchange rate lowers import prices, including raw materials." },
  { q: "A government devalues its fixed exchange rate. What is most likely to be its aim? (May/June 2021 · 12 · Q20, reworded)", opts: ["to improve the terms of trade", "to increase the level of aggregate demand", "to reduce a current account surplus", "to reduce demand-pull inflation"], a: 1, why: "A devaluation aims to raise net exports and so AD." },
] });
