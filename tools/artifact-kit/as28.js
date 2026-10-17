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

const pedAt = (p) => ({ q: 100 - p, ped: p / (100 - p), tr: p * (100 - p) });
function demDraw(p, k = 1) {
  const d = pedAt(p); let o = axes(70, 270, 720, 25, "Quantity", "Price") + SV.line(SDX(0), SDY(100), SDX(100), SDY(0), "c2", { "stroke-width": 3 }) + tag(SDX(100) + 4, SDY(0) - 4, "Demand", "c2");
  o += SV.rect(SDX(0), SDY(p), SDX(d.q) - SDX(0), SDY(0) - SDY(p), "f1", op(0.5 * k)) + SV.text(SDX(d.q / 2), SDY(p / 2) + 4, "Total revenue " + Lib.fmtN(d.tr, 0), "sm", { "text-anchor": "middle", ...op(k) });
  o += SV.circle(SDX(d.q), SDY(p), 6, "dot3", op(k)) + SV.text(SDX(d.q) + 10, SDY(p) - 8, "P = " + p + ", PED " + Lib.fmtN(d.ped, 2), "sm", op(k));
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand curve with PED elastic at high prices and inelastic at low prices">${demDraw(80)}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "PED and revenue along a straight-line demand curve", base: { p: 80 }, draw: (s) => demDraw(s.p), tween: 900, dwell: 5600, steps: [
  { cap: "<b>At a high price of 80</b>, quantity is 20 and PED is 4: <b>elastic</b>. Revenue is 1600.", s: { p: 80 } },
  { cap: "<b>At 50</b>, quantity is 50 and PED is 1: <b>unitary</b>. Revenue is at its maximum of 2500.", s: { p: 50 } },
  { cap: "<b>At a low price of 20</b>, quantity is 80 and PED is 0.25: <b>inelastic</b>. Revenue falls back to 1600.", s: { p: 20 } },
] });
chainStep("#stB", "A price cut when demand is elastic", ["The firm cuts its price by 10%", "Quantity demanded rises by more than 10% (PED above 1)", "The rise in quantity outweighs the lower price", "Total revenue rises", "If demand were inelastic, revenue would fall instead"], [
  "<b>A price cut</b> of 10%.", "<b>Elastic demand:</b> quantity rises by, say, 20%.", "<b>Revenue = price × quantity:</b> 0.90 × 1.20 = 1.08.", "<b>Revenue rises</b> by about 8%.", "<b>With inelastic demand</b> (say quantity +5%) revenue would be 0.90 × 1.05 = 0.945, a fall."]);

function labA() {
  if (!$("#g1v")) return;
  const p = +$("#g1v").value, d = pedAt(p);
  $("#r1").textContent = d.q; $("#r2").textContent = Lib.fmtN(d.ped, 2); $("#r3").textContent = Lib.fmtN(d.tr, 0);
  $("#rv").textContent = Math.abs(d.ped - 1) < 0.02 ? "PED is 1: unitary. Revenue is at its maximum; a small price change leaves it roughly unchanged." : d.ped > 1 ? `PED is ${Lib.fmtN(d.ped, 2)}: elastic. A price cut may raise revenue, and a price rise may reduce it.` : `PED is ${Lib.fmtN(d.ped, 2)}: inelastic. A price rise may raise revenue, and a price cut may reduce it.`;
  $("#labA").innerHTML = demDraw(p);
}
Lib.slider($("#g1"), { id: "g1v", label: "Price ", min: 10, max: 90, step: 5, value: 70, fmt: (v) => v, onInput: labA });
labA();
function labB() {
  if (!["g2v", "g3v"].every((i) => $("#" + i))) return;
  const ped = +$("#g2v").value / 10, pc = +$("#g3v").value, qc = -ped * pc, tr = ((1 + pc / 100) * (1 + qc / 100) - 1) * 100;
  $("#t1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#t2").textContent = (tr >= 0 ? "+" : "") + Lib.fmtN(tr, 1) + "%";
  const bar = (y, lab, v, c) => SV.text(20, y + 15, lab, "sm") + SV.rect(150, y, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, y + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labB").innerHTML = bar(20, "Price", pc, "f3") + bar(70, "Quantity", qc, "f1") + bar(120, "Revenue", tr, "f2");
  $("#tv").textContent = `With PED of ${Lib.fmtN(ped, 1)} (${ped > 1 ? "elastic" : ped < 1 ? "inelastic" : "unitary"}) a ${pc >= 0 ? "rise" : "fall"} of ${Math.abs(pc)}% in price changes quantity by ${Lib.fmtN(qc, 1)}% and total revenue by ${Lib.fmtN(tr, 1)}%.`;
}
Lib.slider($("#g2"), { id: "g2v", label: "PED (size) × 10 ", min: 2, max: 30, step: 2, value: 14, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labB });
Lib.slider($("#g3"), { id: "g3v", label: "Change in price, % ", min: -20, max: 20, step: 5, value: -10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labB });
labB();
Lib.classify($("#cl1"), { prompt: "Is demand more likely to be elastic or inelastic?", buckets: [{"label": "Elastic"}, {"label": "Inelastic"}], items: [{"text": "A single brand with many close rivals", "b": 0}, {"text": "Petrol for daily commuting, in the short run", "b": 1}, {"text": "A luxury holiday", "b": 0}, {"text": "An addictive product such as cigarettes", "b": 1}, {"text": "A good that takes a large share of income", "b": 0}, {"text": "Table salt", "b": 1}, {"text": "A product measured over several years", "b": 0}, {"text": "Life-saving medicine", "b": 1}], done: "Many substitutes, luxuries, large income share and a long period make demand more elastic; necessities, habits and small spending make it more inelastic." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["PED", "% change in quantity demanded ÷ % change in price"], ["Elastic demand", "Quantity changes by a greater percentage than price"], ["Inelastic demand", "Quantity changes by a smaller percentage than price"], ["Unitary demand", "Revenue stays the same when price changes"], ["Total revenue", "Price × quantity"], ["Perfectly inelastic", "Quantity does not change when price changes"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a price cut with elastic demand in order.", items: ["The firm cuts its price", "Quantity demanded rises by a larger percentage", "The rise in quantity outweighs the fall in price", "Total revenue rises"], done: "Elastic demand: quantity rises more than price falls, so revenue rises." });
Lib.calc($("#c1"), { qs: [
  {"q": "Price rises by 10% and quantity demanded falls by 25%. What is the PED (size)?", "a": 2.5, "unit": "", "tol": 0.05, "hint": "25 ÷ 10.", "sol": "<b>2.5</b>, elastic."},
  {"q": "PED is -0.4 and price rises by 15%. By what % does quantity demanded change?", "a": -6, "unit": "%", "tol": 0.1, "hint": "-0.4 × 15.", "sol": "<b>-6%</b>."},
  {"q": "Price falls from $20 to $18 and quantity rises from 100 to 130. What is the PED (size)?", "a": 3, "unit": "", "tol": 0.05, "hint": "% change in Q = 30%; % change in P = 10%.", "sol": "<b>3</b>, elastic."},
  {"q": "Using the same figures, by how much does total revenue change ($)?", "a": 340, "unit": "$", "tol": 0.5, "hint": "(18 × 130) − (20 × 100).", "sol": "2340 − 2000 = <b>$340</b> increase."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Elastic demand means:", opts: ["PED size above 1", "PED size below 1", "PED is zero", "Price is fixed"], a: 0, why: "Quantity changes by more than price." },
  { q: "With inelastic demand a price rise:", opts: ["Raises revenue", "Lowers revenue", "Leaves revenue unchanged", "Cuts quantity to zero"], a: 0, why: "Quantity falls less than price rises." },
  { q: "A cause of more elastic demand is:", opts: ["Many close substitutes", "A necessity", "Addiction", "A small share of income"], a: 0, why: "Consumers can switch." },
  { q: "PED = ", opts: ["% change in Q demanded ÷ % change in price", "Change in price ÷ change in Q", "Price × quantity", "% change in income ÷ % change in Q"], a: 0, why: "The PED formula." },
  { q: "Demand is usually more elastic:", opts: ["In the long run", "In the short run", "For necessities", "For addictive goods"], a: 0, why: "People find substitutes over time." },
] });
Lib.cards($("#fc1"), { cards: [
  ["PED formula", "%ΔQd ÷ %ΔP."],
  ["Elastic", "Size above 1."],
  ["Inelastic", "Size below 1."],
  ["Unitary", "Size equals 1."],
  ["Elastic, price cut", "Revenue rises."],
  ["Inelastic, price rise", "Revenue rises."],
  ["Determinants", "Substitutes, necessity, income share, habit, time."],
  ["Along a straight line", "Elastic high, unitary mid, inelastic low."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In which circumstance will the total expenditure by consumers on a good increase when its price increases? (Feb/March 2020 · 12 · Q5, reworded)", opts: ["Demand for the good is income elastic.", "Demand for the good is price inelastic.", "The price of a complementary good also increases.", "The price of substitute goods also increases."], a: 1, why: "With inelastic demand quantity falls by a smaller percentage than price rises, so expenditure rises." },
  { q: "A decrease in the quantity demanded of a product results in a proportionate decrease in sales revenues. What is true about its price elasticity of demand? (Feb/March 2025 · 12 · Q11, reworded)", opts: ["It is between zero and one.", "It is infinite.", "It is unitary.", "It is zero."], a: 1, why: "Revenue falls in proportion to quantity only if price is unchanged, which is the case when demand is perfectly elastic at that price." },
  { q: "The economics department of a university calculates that the price elasticity of demand for the products of a local firm is between -1.1 and -1.3. Which decision could be justified by the research? (May/June 2020 · 11 · Q13, reworded)", opts: ["Increase prices to increase profit.", "Invest in more capital to increase output.", "Reduce advertising to reduce costs.", "Reduce prices to increase revenue."], a: 3, why: "Demand is elastic, so a price cut raises total revenue." },
  { q: "A manufacturer progressively reduces the price of his product. The table shows the outcome: at prices of $10, $9 and $8, total revenue is $750 (000s) each time. What is the price elasticity of demand for the product? (May/June 2020 · 12 · Q6, reworded)", opts: ["perfectly inelastic", "relatively inelastic", "perfectly elastic", "unitary"], a: 3, why: "Revenue does not change when price changes, so demand is unitary." },
  { q: "Why is the price elasticity of demand for a particular brand of coffee likely to be higher than the price elasticity of demand for coffee in general? (May/June 2021 · 11 · Q8, reworded)", opts: ["Coffee in general takes up a higher proportion of consumers' income.", "Consumers may be very loyal to a particular brand of coffee.", "There are more substitutes for a particular brand of coffee than for coffee in general.", "Total demand for coffee is higher than for any one brand."], a: 2, why: "Other brands are close substitutes for a single brand." },
  { q: "The price elasticity of demand for a firm's product is equal to one for all price changes. What would be the result of this? (May/June 2021 · 12 · Q6, reworded)", opts: ["A percentage increase in price will cause demand to fall by a larger percentage.", "A percentage increase in price will cause demand to increase by the same percentage.", "Quantity demanded will always be the same whatever the price.", "The firm's revenue will always be the same whatever the price."], a: 3, why: "With unitary elasticity, price and quantity change by the same percentage in opposite directions, so revenue is constant." },
  { q: "What would be the most likely reason for a firm's decision to calculate the price elasticity of demand for its product? (May/June 2022 · 12 · Q9, reworded)", opts: ["to provide retail statistics for the government", "to predict the change in its total revenue after it raises prices", "to calculate the firm's competitive position", "to enable the firm to complete consumer satisfaction surveys"], a: 1, why: "PED shows how revenue may respond to a price change." },
  { q: "The price elasticity of demand for a high-quality smartphone is elastic. The price of the smartphone decreases. What is the impact on the quantity demanded and total revenue? (quantity demanded, total revenue) (May/June 2022 · 14 · Q11, reworded)", opts: ["rises by a greater percentage than the price fall, falls", "rises by a greater percentage than the price fall, rises", "rises by a smaller percentage than the price fall, falls", "rises by a smaller percentage than the price fall, rises"], a: 1, why: "With elastic demand, quantity rises by a greater percentage than price falls, so revenue rises." },
  { q: "When is the price elasticity of demand for a product most likely to be price elastic? (May/June 2023 · 13 · Q5, reworded)", opts: ["A large percentage of income is spent on the product.", "It is measured in the short run.", "It is a necessity product.", "There are few substitutes available."], a: 0, why: "A large share of income makes consumers more responsive to price." },
  { q: "When the price of a firm's product falls by 5%, its total revenue also falls by 5%. What describes the product's price elasticity of demand? (May/June 2023 · 13 · Q10, reworded)", opts: ["elastic", "infinite", "unitary", "zero"], a: 3, why: "Quantity is unchanged, so demand is perfectly inelastic (zero)." },
] });
