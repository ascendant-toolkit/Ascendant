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

const incEq = (m, n, t) => { const q = 50 - t / (m + n), pc = 50 + m * (t / (m + n)); return { q, pc, pp: pc - t, sc: m / (m + n) }; };
function incPlot(x0, w, m, n, t, k, name, o = {}) {
  const X = (q) => x0 + q * (w / 110), Y = (p) => 250 - p * 1.7, e = incEq(m, n, t), ax = Math.abs(t) > 0.05, dEnd = Math.min(100, 50 + 45 / m);
  let s = SV.line(x0, 250, x0 + w, 250) + SV.line(x0, 250, x0, 50) + SV.text(x0 + 6, 46, "Price", "sm") + SV.text(x0 + w, 270, "Quantity", "sm", { "text-anchor": "end" });
  if (name) s += SV.text(x0 + w / 2, 30, name, "lbl bd", { "text-anchor": "middle" });
  s += SV.line(X(0), Y(50 + 50 * m), X(dEnd), Y(50 + m * (50 - dEnd)), "c2", { "stroke-width": 3 }) + tag(X(dEnd) + 4, Y(50 + m * (50 - dEnd)) + 4, "D", "c2");
  s += SV.line(X(0), Y(50 - 50 * n), X(100), Y(50 + 50 * n), "c1", { "stroke-width": 3, ...op(ax && k > 0 ? 0.4 : 1) }) + tag(X(100) + 4, Y(50 + 50 * n), "S", "c1", ax && k > 0 ? 0.4 : 1);
  s += SV.circle(X(50), Y(50), 5, "dot1", op(ax && k > 0 ? 0.6 : 1)) + SV.line(x0, Y(50), X(50), Y(50), "dash", op(0.6)) + SV.line(X(50), Y(50), X(50), 250, "dash", op(0.6)) + SV.text(x0 - 6, Y(50) + 4, "50", "sm", { "text-anchor": "end" });
  if (ax && k > 0) {
    s += SV.line(X(0), Y(50 - 50 * n + t), X(100), Y(50 + 50 * n + t), "c3", { "stroke-width": 3, ...op(k) }) + tag(X(100) + 4, Y(50 + 50 * n + t), t > 0 ? "S + tax" : "S + subsidy", "c3", k);
    const mid = 50;
    s += SV.rect(X(0), Math.min(Y(e.pc), Y(mid)), X(e.q) - X(0), Math.abs(Y(mid) - Y(e.pc)), "f3", op(0.45 * k)) + SV.rect(X(0), Math.min(Y(e.pp), Y(mid)), X(e.q) - X(0), Math.abs(Y(e.pp) - Y(mid)), "f2", op(0.45 * k));
    s += SV.circle(X(e.q), Y(e.pc), 6, "dot3", op(k)) + SV.circle(X(e.q), Y(e.pp), 5, "dot2", op(k)) + SV.line(x0, Y(e.pc), X(e.q), Y(e.pc), "dash", op(k)) + SV.line(x0, Y(e.pp), X(e.q), Y(e.pp), "dash", op(k)) + SV.line(X(e.q), Y(e.pc), X(e.q), 250, "dash", op(k));
    s += SV.text(x0 - 6, Y(e.pc) + 4, Lib.fmtN(e.pc, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(x0 - 6, Y(e.pp) + 4, Lib.fmtN(e.pp, 1), "sm", { "text-anchor": "end", ...op(k) }) + SV.text(X(e.q), 268, Lib.fmtN(e.q, 1), "sm", { "text-anchor": "middle", ...op(k) });
  }
  return s;
}

$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="An indirect tax shifts supply up, raising the price consumers pay and lowering the price producers keep">${incPlot(70, 640, 0.8, 0.8, 10, 1, "")}</svg>`;
function t1Draw(s) { return incPlot(70, 640, 0.8, 0.8, 10, s.k, "") + (s.v > 0 ? SV.text(380, 292, "Tax revenue = $10 × " + Lib.fmtN(incEq(0.8, 0.8, 10).q, 1) + " = $" + Lib.fmtN(10 * incEq(0.8, 0.8, 10).q, 0), "lbl bd", { "text-anchor": "middle", ...op(s.v) }) : ""); }
Lib.stepper($("#stT"), { w: 760, h: 300, label: "An indirect tax of $10 per unit", base: { k: 0, v: 0 }, draw: t1Draw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before the tax.</b> The market is in equilibrium at $50 and 50 units.", s: { k: 0, v: 0 } },
  { cap: "<b>The tax raises each firm's cost by $10.</b> The supply curve shifts up (left) by $10: the vertical gap is the tax.", s: { k: 1, v: 0 } },
  { cap: "<b>The new equilibrium.</b> Consumers now pay $55 (up $5). Producers receive $55 − $10 = $45 (down $5). Quantity falls to 43.75. Each side bears half the tax here.", s: { k: 1, v: 0 } },
  { cap: "<b>Tax revenue</b> is the tax per unit times the quantity sold after the tax. The blue box is the consumers' share, the green box the producers' share.", s: { k: 1, v: 1 } },
] });

function incTwo(s) { return incPlot(30, 330, 1.2, 0.6, 10, s.k, "Inelastic demand (steep)") + incPlot(400, 330, 0.4, 0.6, 10, s.k, "Elastic demand (flat)") + (s.k > 0.5 ? SV.text(195, 288, "Consumers bear " + Lib.fmtN(incEq(1.2, 0.6, 10).sc * 100, 0) + "%", "lbl bd", { "text-anchor": "middle", ...op(s.k) }) + SV.text(565, 288, "Consumers bear " + Lib.fmtN(incEq(0.4, 0.6, 10).sc * 100, 0) + "%", "lbl bd", { "text-anchor": "middle", ...op(s.k) }) : ""); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same tax on a market with inelastic demand and on one with elastic demand">${incTwo({ k: 1 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 300, label: "The same tax with inelastic and with elastic demand", base: { k: 0 }, draw: incTwo, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Two markets</b> with the same supply curve and equilibrium. Demand is steep (inelastic) on the left and flat (elastic) on the right.", s: { k: 0 } },
  { cap: "<b>The same $10 tax.</b> With <b>inelastic</b> demand, consumers keep buying, so the price rises by about two thirds of the tax and the quantity falls little. With <b>elastic</b> demand the price rises only by about 40% of the tax and the quantity falls more.", s: { k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labT() {
  if (!$("#tx") || !$("#dm") || !$("#sn")) return;
  const t = +$("#tx").value, m = +$("#dm").value / 10, n = +$("#sn").value / 10, e = incEq(m, n, t), rev = t * e.q;
  $("#r1").textContent = "$" + Lib.fmtN(e.pc, 1) + " (+" + Lib.fmtN(e.pc - 50, 1) + ")"; $("#r2").textContent = "$" + Lib.fmtN(e.pp, 1) + " (" + Lib.fmtN(e.pp - 50, 1) + ")"; $("#r3").textContent = "$" + Lib.fmtN(rev, 0);
  $("#rv").textContent = t === 0 ? "No tax, so nothing changes." : `Of the $${t} tax, consumers bear $${Lib.fmtN(e.pc - 50, 1)} (${Lib.fmtN(e.sc * 100, 0)}%) and producers $${Lib.fmtN(50 - e.pp, 1)} (${Lib.fmtN((1 - e.sc) * 100, 0)}%). Quantity falls from 50 to ${Lib.fmtN(e.q, 1)} and the government raises $${Lib.fmtN(rev, 0)}. ${m > n ? "Demand is steeper than supply (more inelastic), so consumers bear more." : m < n ? "Supply is steeper than demand (more inelastic), so producers bear more." : "Demand and supply are equally steep, so the burden is shared equally."}`;
  $("#labA").innerHTML = incPlot(70, 640, m, n, t, 1, "");
}
Lib.slider($("#g1"), { id: "tx", label: "Tax per unit, $ ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g2"), { id: "dm", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 8, fmt: (v) => v, onInput: labT });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = flat and elastic, 10 = steep and inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Lab 2 ---------- */
function labV() {
  if (!$("#st")) return;
  const t = +$("#st").value, r = t / 50 * 100, X = (q) => 70 + q * 6, Y = (p) => 270 - p * 2.2; let o = SV.line(70, 270, 700, 270) + SV.line(70, 270, 70, 40);
  o += SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3, ...op(0.45) }) + SV.line(X(0), Y(10 + t), X(100), Y(90 + t), "c3", { "stroke-width": 3 }) + SV.line(X(0), Y(10 * (1 + r / 100)), X(100), Y(90 * (1 + r / 100)), "c2", { "stroke-width": 3, "stroke-dasharray": "6 4" });
  o += tag(X(100) + 4, Y(90), "S", "c1", 0.6) + tag(X(100) + 4, Y(90 + t) - 4, "S + specific", "c3") + tag(X(100) + 4, Y(90 * (1 + r / 100)) + 14, "S + ad valorem", "c2");
  $("#t1").textContent = "$" + t; $("#t2").textContent = Lib.fmtN(r, 0) + "%"; $("#t3").textContent = "Specific $" + t + " vs ad valorem $" + Lib.fmtN(80 * r / 100, 1);
  $("#tv").textContent = `A specific tax of $${t} is the same at every price, so the supply curve moves up in parallel. An ad valorem tax of ${Lib.fmtN(r, 0)}% raises the same amount at $50 but takes $${Lib.fmtN(80 * r / 100, 1)} at $80, so the new curve pivots and gets further from the old one as price rises.`;
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "st", label: "Specific tax, $ (equal to an ad valorem tax at a price of $50) ", min: 2, max: 20, step: 2, value: 10, fmt: (v) => "$" + v, onInput: labV });
labV();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Who bears more of the tax?", buckets: [{"label": "Consumers"}, {"label": "Producers"}], items: [{"text": "Demand is inelastic and supply is elastic", "b": 0}, {"text": "Demand is elastic and supply is inelastic", "b": 1}, {"text": "Cigarettes (addictive, few substitutes)", "b": 0}, {"text": "A luxury good with many substitutes", "b": 1}, {"text": "Demand is perfectly inelastic", "b": 0}, {"text": "Supply is perfectly inelastic", "b": 1}, {"text": "Petrol in the short run", "b": 0}, {"text": "A product facing close competitors", "b": 1}], done: "The side with the less elastic curve bears the larger share of the tax." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Indirect tax", "A tax on spending that raises firms' costs"], ["Specific tax", "A fixed amount per unit"], ["Ad valorem tax", "A percentage of the price"], ["Incidence", "How the burden of a tax is shared"], ["Tax revenue", "Tax per unit × quantity sold after the tax"], ["Regressive tax", "Takes a larger share of low incomes"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of an indirect tax in order.", items: ["The government imposes a tax per unit", "The supply curve shifts to the left", "The price paid by consumers rises", "The quantity traded falls", "The government collects tax revenue and the burden is shared by elasticity"], done: "Tax, supply shifts, price up, quantity down, revenue." });
Lib.calc($("#c1"), { qs: [
  {"q": "A tax of $3 per unit raises the price from $40 to $42. How much of the tax per unit is paid by consumers?", "a": 2, "unit": "$", "tol": 0.05, "hint": "New price minus old price.", "sol": "<b>$2</b> per unit."},
  {"q": "In the same example, how much per unit is borne by producers?", "a": 1, "unit": "$", "tol": 0.05, "hint": "3 − 2.", "sol": "<b>$1</b> per unit."},
  {"q": "Quantity falls from 100 to 90 units. What is the tax revenue ($)?", "a": 270, "unit": "$", "tol": 1, "hint": "3 × 90.", "sol": "<b>$270</b>."},
  {"q": "What percentage of the tax is borne by consumers?", "a": 66.7, "unit": "%", "tol": 0.5, "hint": "2 ÷ 3.", "sol": "<b>66.7%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A specific tax is:", opts: ["A fixed amount per unit", "A percentage of the price", "A tax on income", "A tax on profits only"], a: 0, why: "Per unit." },
  { q: "An indirect tax shifts the supply curve:", opts: ["To the left", "To the right", "Not at all", "To a vertical line"], a: 0, why: "Costs rise." },
  { q: "Consumers bear most of a tax when demand is:", opts: ["Inelastic", "Elastic", "Unit elastic only", "Perfectly elastic"], a: 0, why: "They have few alternatives." },
  { q: "The price consumers pay after a tax rises by:", opts: ["Less than the tax, unless demand is perfectly inelastic", "More than the tax", "Exactly the tax always", "Nothing"], a: 0, why: "The burden is shared." },
  { q: "Tax revenue equals:", opts: ["Tax per unit × quantity after the tax", "Tax per unit × quantity before the tax", "Price × quantity", "Consumer surplus"], a: 0, why: "Use the new quantity." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Indirect tax", "Tax on spending; shifts supply left."],
  ["Specific", "Fixed sum per unit."],
  ["Ad valorem", "Percentage of price."],
  ["Incidence", "Who bears the tax."],
  ["Inelastic demand", "Consumers bear more."],
  ["Revenue", "Tax × new quantity."],
  ["Demerit goods", "Taxed to cut consumption."],
  ["Regressive", "Hits low incomes harder."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which type of tax is the 15% sales tax levied in South Africa? (Feb/March 2020 · 12 · Q17, reworded)", opts: ["ad valorem direct", "ad valorem indirect", "specific direct", "specific indirect"], a: 1, why: "A percentage of the price is ad valorem, and a sales tax on spending is indirect." },
  { q: "A specific tax is imposed on a product for which the elasticity of supply is zero. Which statement is correct? (May/June 2020 · 11 · Q14, reworded)", opts: ["The burden of this tax will fall entirely on consumers", "The burden of this tax will fall entirely on suppliers", "The burden of this tax will fall mainly on consumers", "The burden of this tax will fall mainly on suppliers"], a: 1, why: "If supply is perfectly inelastic, the price cannot rise, so producers bear all of the tax." },
  { q: "The supply curve of a product passes through the origin. The government imposes a specific indirect tax of $5 on the product. How will the price elasticity of supply of the product change? (May/June 2020 · 12 · Q12, reworded)", opts: ["from elastic to inelastic", "from inelastic to elastic", "from inelastic to unitary", "from unitary to elastic"], a: 3, why: "A curve through the origin has unit elasticity. A parallel shift up by $5 gives a positive price intercept, so supply becomes elastic." },
  { q: "The table shows sources of government revenue: sale of government assets 100, tax on self employed 1000, carbon tax on goods produced 100, corporate taxes 500, capital gains tax 100, goods and services tax 1000, air passenger tax 100 ($ billions). What is the total amount of tax revenue raised by indirect taxes? (May/June 2021 · 12 · Q17, reworded)", opts: ["$1,200 billion", "$1,300 billion", "$1,400 billion", "$1,600 billion"], a: 0, why: "Indirect taxes are the carbon tax, goods and services tax and air passenger tax: 100 + 1000 + 100." },
  { q: "An indirect tax is imposed on a product in a competitive market. Under which circumstances would the value of the consumer surplus be most likely to remain unchanged? (May/June 2020 · 11 · Q9, reworded)", opts: ["New substitutes are developed for the product and production costs rise", "Some producers merge so there is less competition in the market", "The product is an inferior good, consumer incomes increase and production costs rise", "The product is a normal good, consumer incomes increase and production costs fall"], a: 3, why: "Higher demand raises consumer surplus, while a tax lowers it, so the effects can offset. Falling costs raise supply as well." },
] });
