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

function wfDraw(items, s) {
  const max = Math.max(...items.map((it) => it[3] || 0)) * 1.15, Y = (v) => 250 - (v / max) * 190, w = 600 / items.length; let o = SV.line(50, 250, 740, 250);
  items.forEach((it, i) => {
    const [lab, val, kind, top, bot] = it, x = 70 + i * (w + 8), v = Math.max(0, Math.min(1, s.k - i));
    if (v <= 0) return;
    o += SV.rect(x, Y(top), w - 20, Math.max(2, Y(bot) - Y(top)), kind === "t" ? "f1" : val < 0 ? "f3" : "f2", op(0.65 * v)) + SV.text(x + (w - 20) / 2, Y(top) - 8, (kind === "d" && val > 0 ? "+" : "") + Lib.fmtN(val, 0), "lbl bd", { "text-anchor": "middle", ...op(v) }) + SV.text(x + (w - 20) / 2, 270, lab, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return o;
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

const itemsB = [["GDP at market prices", 120, "t", 120, 0], ["Taxes on products", -15, "d", 120, 105], ["Subsidies on products", 5, "d", 110, 105], ["GDP at basic prices", 110, "t", 110, 0]];
function bDraw(s) { return wfDraw(itemsB, s); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="GDP at market prices of 120, less taxes on products of 15, plus subsidies of 5, gives GDP at basic prices of 110">${bDraw({ k: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 290, label: "GDP from market prices to basic prices", base: { k: 0 }, draw: bDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Market prices</b> are what buyers pay, including sales taxes: $120bn.", s: { k: 1 } },
  { cap: "<b>Subtract taxes on products</b> ($15bn). Producers do not receive this money.", s: { k: 2 } },
  { cap: "<b>Add subsidies on products</b> ($5bn). Producers do receive this money.", s: { k: 3 } },
  { cap: "<b>GDP at basic prices = 120 − 15 + 5 = $110bn</b>, the amount producers actually receive.", s: { k: 4 } },
] });
const itemsG = [["Gross domestic product", 120, "t", 120, 0], ["Capital consumption", -10, "d", 120, 110], ["Net domestic product", 110, "t", 110, 0], ["Net primary income", -5, "d", 110, 105], ["NNI", 105, "t", 105, 0]];
function gDraw(s) { return wfDraw(itemsG, s); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Gross domestic product of 120 less capital consumption of 10 gives net domestic product of 110; adjusting for net primary income of minus 5 gives NNI of 105">${gDraw({ k: 5 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 290, label: "From gross to net", base: { k: 0 }, draw: gDraw, tween: 800, dwell: 5000, steps: [
  { cap: "<b>Gross domestic product</b> counts all output, including output needed to replace worn-out capital: $120bn.", s: { k: 1 } },
  { cap: "<b>Capital consumption</b> of $10bn is the value of capital used up.", s: { k: 2 } },
  { cap: "<b>Net domestic product = $110bn.</b> This is output available to consume or to add to the capital stock.", s: { k: 3 } },
  { cap: "<b>Net primary income from abroad</b> of −$5bn moves from a domestic to a national measure.", s: { k: 4 } },
  { cap: "<b>NNI = $105bn.</b> Both adjustments applied: net and national.", s: { k: 5 } },
] });

function labP() {
  if (!["gd", "tx", "sb"].every((i) => $("#" + i))) return;
  const gdp = +$("#gd").value, tx = +$("#tx").value, sb = +$("#sb").value, basic = gdp - tx + sb, ts = tx - sb;
  $("#r1").textContent = (ts >= 0 ? "" : "−") + "$" + Math.abs(ts) + "bn"; $("#r2").textContent = "$" + basic + "bn"; $("#r3").textContent = Lib.fmtN((basic / gdp) * 100, 1) + "%";
  $("#rv").textContent = `GDP at basic prices = ${gdp} − ${tx} + ${sb} = ${basic}. ${ts > 0 ? "Taxes on products exceed subsidies, so basic prices are below market prices." : ts < 0 ? "Subsidies exceed taxes, so basic prices are above market prices." : "Taxes equal subsidies, so the two are equal."}`;
  const Y = (v) => 240 - v * 1.2; let o = SV.line(40, 240, 400, 240);
  [["Market", gdp, "f1"], ["Basic", basic, "f2"]].forEach(([l, v, c], i) => (o += SV.rect(90 + i * 140, Y(v), 90, 240 - Y(v), c, op(0.65)) + SV.text(135 + i * 140, 258, l, "sm", { "text-anchor": "middle" }) + SV.text(135 + i * 140, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gd", label: "GDP at market prices, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "tx", label: "Taxes on products, $bn ", min: 0, max: 40, step: 1, value: 15, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "sb", label: "Subsidies on products, $bn ", min: 0, max: 30, step: 1, value: 5, fmt: (v) => v, onInput: labP });
labP();
function labG() {
  if (!["gg", "cc"].every((i) => $("#" + i))) return;
  const g = +$("#gg").value, c = +$("#cc").value, n = g - c;
  $("#t1").textContent = "$" + n + "bn"; $("#t2").textContent = Lib.fmtN((c / g) * 100, 1) + "%";
  $("#tv").textContent = `Net domestic product = ${g} − ${c} = ${n}. Capital consumption is ${Lib.fmtN((c / g) * 100, 1)}% of GDP. ${c / g > 0.15 ? "A large share of output is only replacing worn-out capital, leaving less for consumption and growth." : "A small share of output is needed to replace capital."}`;
  const Y = (v) => 190 - v * 0.9; let o = SV.line(40, 190, 400, 190);
  [["Gross", g, "f1"], ["Depreciation", c, "f3"], ["Net", n, "f2"]].forEach(([l, v, k], i) => (o += SV.rect(60 + i * 110, Y(v), 80, 190 - Y(v), k, op(0.65)) + SV.text(100 + i * 110, 208, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(v) - 6, "$" + v, "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gg", label: "Gross domestic product, $bn ", min: 80, max: 200, step: 5, value: 120, fmt: (v) => v, onInput: labG });
Lib.slider($("#g5"), { id: "cc", label: "Capital consumption, $bn ", min: 0, max: 40, step: 1, value: 10, fmt: (v) => v, onInput: labG });
labG();
Lib.classify($("#cl1"), { prompt: "Is it included at market prices or at basic prices?", buckets: [{"label": "Market prices only"}, {"label": "Basic prices only"}], items: [{"text": "Sales tax paid by the buyer", "b": 0}, {"text": "A subsidy paid to the producer", "b": 1}, {"text": "VAT collected on a purchase", "b": 0}, {"text": "Government payment per tonne of grain produced", "b": 1}, {"text": "The price printed on the shop label", "b": 0}, {"text": "The amount the producer actually receives for the good", "b": 1}], done: "Market prices include taxes on products; basic prices include subsidies." });
Lib.classify($("#cl2"), { prompt: "Is it a gross or a net measure?", buckets: [{"label": "Gross"}, {"label": "Net"}], items: [{"text": "GDP", "b": 0}, {"text": "NNI", "b": 1}, {"text": "GNI", "b": 0}, {"text": "Net domestic product", "b": 1}, {"text": "A figure before deducting depreciation", "b": 0}, {"text": "A figure after deducting capital consumption", "b": 1}], done: "Gross is before depreciation; net is after." });
Lib.order($("#o1"), { prompt: "Put the steps from GDP at market prices to NNI in order.", items: ["Start with GDP at market prices", "Adjust for net primary income from abroad to reach GNI", "Subtract capital consumption", "This gives NNI at market prices"], done: "GDP + net primary income − capital consumption = NNI." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Market prices", "Prices buyers pay, including product taxes"], ["Basic prices", "Market prices minus taxes plus subsidies"], ["Gross", "Before deducting capital consumption"], ["Net", "After deducting capital consumption"], ["Taxes on products", "Sales taxes such as VAT"], ["Subsidies on products", "Payments to producers per unit produced"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "GDP at market prices is $200bn, taxes on products $25bn and subsidies $10bn. What is GDP at basic prices ($bn)?", "a": 185, "unit": "$bn", "tol": 0.5, "hint": "200 − 25 + 10.", "sol": "<b>$185bn</b>."},
  {"q": "A good costs $120 in the shop including $20 of sales tax. There is no subsidy. What is the basic price ($)?", "a": 100, "unit": "$", "tol": 0.5, "hint": "120 − 20.", "sol": "<b>$100</b>."},
  {"q": "GDP at basic prices is $450bn, taxes on products $60bn and subsidies $20bn. What is GDP at market prices ($bn)?", "a": 490, "unit": "$bn", "tol": 0.5, "hint": "450 + 60 − 20.", "sol": "<b>$490bn</b>."},
  {"q": "GDP is $300bn and capital consumption is $36bn. What is net domestic product ($bn)?", "a": 264, "unit": "$bn", "tol": 0.5, "hint": "300 − 36.", "sol": "<b>$264bn</b>."},
  {"q": "What percentage of GDP is capital consumption?", "a": 12, "unit": "%", "tol": 0.1, "hint": "36 ÷ 300.", "sol": "<b>12%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Basic prices equal:", opts: ["Market prices − taxes on products + subsidies", "Market prices + taxes", "Market prices − subsidies", "Market prices + depreciation"], a: 0, why: "What producers receive." },
  { q: "Market prices include:", opts: ["Taxes on products", "Subsidies only", "Depreciation", "Net primary income"], a: 0, why: "What buyers pay." },
  { q: "A net figure is:", opts: ["After deducting capital consumption", "Before deducting capital consumption", "Adjusted for inflation", "Adjusted for population"], a: 0, why: "Gross minus depreciation." },
  { q: "Net national income is lower than gross national income because of:", opts: ["Capital consumption", "Taxes", "Subsidies", "Exports"], a: 0, why: "Depreciation." },
  { q: "If subsidies exceed taxes on products, basic prices are:", opts: ["Above market prices", "Below market prices", "Equal to market prices", "Zero"], a: 0, why: "More is added than subtracted." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market prices", "What the buyer pays."],
  ["Basic prices", "Market − taxes + subsidies."],
  ["Gross", "Before depreciation."],
  ["Net", "After depreciation."],
  ["NDP", "GDP − depreciation."],
  ["NNI", "GNI − depreciation."],
  ["Taxes on products", "VAT and similar."],
  ["Why basic?", "Removes the effect of product taxes."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A country's net national income (NNI) is less than its gross national income (GNI). What does this mean? (May/June 2024 · 11 · Q16, reworded)", opts: ["incomes earned overseas were less than incomes sent overseas", "inflation has been accounted for in NNI but not in GNI", "the country's exports decreased", "there has been a net depreciation in the value of the country's fixed capital assets"], a: 3, why: "NNI is GNI minus capital consumption, so NNI is lower when capital has depreciated." },
] });
