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
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, "P1", "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, "P2", "Q2", g * n);
  return o;
}

const dEnd = (m) => Math.min(100, 50 + 45 / m);
/* ---------- shared panel drawing ---------- */
function panel(x0, m, L, k, name) {
  const X = (q) => x0 + q * 2.7, Y = (p) => 250 - p * 1.65, dint = 50 + 50 * m, Dp = (q) => 50 + m * (50 - q);
  const q1 = (40 + 50 * m - 0.8 * L) / (m + 0.8), p1 = Dp(q1);
  let o = SV.line(x0, 250, x0 + 300, 250) + SV.line(x0, 250, x0, 60) + SV.text(x0 + 6, 56, "Price", "sm") + SV.text(x0 + 300, 270, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(x0 + 150, 40, name, "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(0), Y(dint), X(dEnd(m)), Y(Dp(dEnd(m))), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3 });
  o += SV.poly([[X(0), Y(dint)], [X(0), Y(50)], [X(50), Y(50)]], "f3", op(0.4)) + SV.circle(X(50), Y(50), 5, "dot1");
  const cs0 = 0.5 * 50 * (dint - 50), cs1 = 0.5 * q1 * (dint - p1);
  if (k > 0) {
    o += SV.line(X(0), Y(10 + 0.8 * L), X(100 - L), Y(90), "c3", { "stroke-width": 3, ...op(k) });
    o += SV.poly([[X(0), Y(dint)], [X(0), Y(p1)], [X(q1), Y(p1)]], "f3", op(0.4 * k)) + SV.poly([[X(0), Y(p1)], [X(0), Y(50)], [X(50), Y(50)], [X(q1), Y(p1)]], "f2", op(0.7 * k));
    o += SV.circle(X(q1), Y(p1), 6, "dot3", op(k)) + SV.text(x0 + 150, 292, "CS " + Lib.fmtN(cs0, 0) + " to " + Lib.fmtN(cs1, 0) + " (loss " + Lib.fmtN(cs0 - cs1, 0) + ")", "lbl bd", { "text-anchor": "middle", ...op(k) });
  } else o += SV.text(x0 + 150, 292, "CS " + Lib.fmtN(cs0, 0), "lbl bd", { "text-anchor": "middle" });
  return o;
}
function twoDraw(s) { return panel(40, 0.4, 15, s.k, "Elastic demand (flat)") + panel(420, 1.2, 15, s.k, "Inelastic demand (steep)"); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Supply shifts left on an elastic and an inelastic demand curve and consumer surplus falls by more on the inelastic one">${twoDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 300, label: "The same leftward shift of supply with elastic and inelastic demand", base: { k: 0 }, draw: twoDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> Two markets with the same supply curve and the same equilibrium ($50, 50 units). Demand is flat (elastic) in one and steep (inelastic) in the other. Consumer surplus is the shaded triangle: 500 and 1,500.", s: { k: 0 } },
  { cap: "<b>An indirect tax (or cost rise) shifts supply to the left</b> by the same amount in both markets. The shaded loss of consumer surplus is shown in green, with the remaining surplus in blue.", s: { k: 1 } },
  { cap: "<b>Elastic demand:</b> price up only a little ($54) and quantity down to 40; consumer surplus falls 180. <b>Inelastic demand:</b> price up more ($57) and quantity down to 44; consumer surplus falls about 338. The steeper demand curve suffers the bigger loss.", s: { k: 1 } },
] });

/* ---------- price fall ---------- */
function fallDraw(s) {
  const one = (x0, m, name) => {
    const X = (q) => x0 + q * 2.7, Y = (p) => 250 - p * 1.65, dint = 50 + 50 * m, q1 = 50 + 10 / m, gain = 10 * (50 + q1) / 2;
    let o = SV.line(x0, 250, x0 + 300, 250) + SV.line(x0, 250, x0, 60) + SV.text(x0 + 150, 40, name, "lbl bd", { "text-anchor": "middle" }) + SV.line(X(0), Y(dint), X(dEnd(m)), Y(50 + m * (50 - dEnd(m))), "c2", { "stroke-width": 3 });
    o += SV.line(X(0), Y(50), X(q1), Y(50), "dash") + SV.line(X(0), Y(40), X(q1), Y(40), "dash") + SV.poly([[X(0), Y(dint)], [X(0), Y(50)], [X(50), Y(50)]], "f3", op(0.35));
    if (s.k > 0) o += SV.poly([[X(0), Y(50)], [X(0), Y(40)], [X(q1), Y(40)], [X(50), Y(50)]], "f2", op(0.75 * s.k)) + SV.text(x0 + 150, 292, "Gain in CS: " + Lib.fmtN(gain, 0) + " (quantity " + Lib.fmtN(q1, 0) + ")", "lbl bd", { "text-anchor": "middle", ...op(s.k) });
    return o + SV.text(x0 - 6, Y(50) + 4, "50", "sm", { "text-anchor": "end" }) + SV.text(x0 - 6, Y(40) + 4, "40", "sm", { "text-anchor": "end" });
  };
  return one(40, 0.4, "Elastic demand") + one(420, 1.2, "Inelastic demand");
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="The same fall in price raises consumer surplus by more when demand is elastic">${fallDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stF"), { w: 760, h: 300, label: "The same price fall from $50 to $40 with elastic and inelastic demand", base: { k: 0 }, draw: fallDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Before.</b> The price is $50 in both markets. Demand is elastic on the left and inelastic on the right.", s: { k: 0 } },
  { cap: "<b>The price falls to $40.</b> The extra consumer surplus (green) is the gain for existing buyers plus the gain for new buyers. With elastic demand quantity rises to 75, so the gain is about 625. With inelastic demand quantity rises to about 58, so the gain is about 542.", s: { k: 1 } },
] });

/* ---------- Lab 1: events ---------- */
const EVN = [
  ["Demand rises", { d: 15, s: 0 }, "More demand raises the price and quantity, so consumers gain willingness to pay and producers sell more at a higher price."],
  ["Demand falls", { d: -15, s: 0 }, "Less demand lowers the price and quantity, so both surpluses fall."],
  ["Costs fall (supply rises)", { d: 0, s: 10 }, "Supply moves right, the price falls and quantity rises: consumer surplus up."],
  ["Indirect tax (supply falls)", { d: 0, s: -15 }, "Supply moves left, the price rises and quantity falls: consumer surplus down, and producers also lose volume."],
  ["Maximum price $35", { p: 35 }, "Below equilibrium: quantity traded is set by supply, so some buyers cannot buy and total surplus falls."],
  ["Minimum price $65", { p: 65 }, "Above equilibrium: quantity traded is set by demand, so consumer surplus falls and some producers cannot sell."],
];
const polyS = (pts, c, v) => SV.poly(pts.map(([q, p]) => [SDX(q), SDY(p)]), c, op(v));
function showEv(i) {
  const [nm, a, why] = EVN[i]; let cs, ps, o, qd = 0;
  $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  if (a.p !== undefined) {
    const p = a.p, up = p > 50, Q = up ? (90 - p) / 0.8 : (p - 10) / 0.8;
    cs = up ? 0.5 * Q * (90 - p) : 90 * Q - 0.4 * Q * Q - p * Q; ps = up ? p * Q - (10 * Q + 0.4 * Q * Q) : 0.5 * Q * (p - 10);
    const pts = up ? [[[0, 90], [0, p], [Q, p]], [[0, 10], [0, p], [Q, p], [Q, 10 + 0.8 * Q]]] : [[[0, 90], [0, p], [Q, p], [Q, 90 - 0.8 * Q]], [[0, 10], [0, p], [Q, p]]];
    o = sdPlot({ d: 0, s: 0, g: 0 }) + polyS(pts[0], "f3", 0.5) + polyS(pts[1], "f2", 0.5) + SV.line(70, SDY(p), SDX(Math.max(Q, 50)), SDY(p), "c4", { "stroke-width": 2.5 });
  } else {
    const e = sdEq(a.d, a.s), di = 90 + 0.8 * a.d, si = 10 - 0.8 * a.s; cs = 0.5 * e.q * (di - e.p); ps = 0.5 * e.q * (e.p - si);
    o = sdPlot({ d: a.d, s: a.s, g: 0, n: 1 }) + polyS([[0, di], [0, e.p], [e.q, e.p]], "f3", 0.5) + polyS([[0, si], [0, e.p], [e.q, e.p]], "f2", 0.5) + SV.circle(SDX(e.q), SDY(e.p), 5, "dot3");
  }
  $("#r1").textContent = Lib.fmtN(cs, 0) + (cs > 1005 ? " (up)" : cs < 995 ? " (down)" : ""); $("#r2").textContent = Lib.fmtN(ps, 0) + (ps > 1005 ? " (up)" : ps < 995 ? " (down)" : ""); $("#r3").textContent = a.p !== undefined ? Lib.fmtN(Math.max(0, 2000 - cs - ps), 0) : "None";
  $("#rv").textContent = nm + ". " + why + (a.p !== undefined ? " Starting surpluses are 1,000 each." : " Starting surpluses are 1,000 each; the market still trades at its new equilibrium, so there is no welfare loss.");
  $("#labA").innerHTML = o;
}
$("#evB").innerHTML = EVN.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showEv(+b.dataset.i)));
showEv(0);

/* ---------- Lab 2 ---------- */
function labE() {
  if (!$("#sl") || !$("#cc")) return;
  const m = +$("#sl").value / 10, L = +$("#cc").value, dint = 50 + 50 * m, q1 = (40 + 50 * m - 0.8 * L) / (m + 0.8), p1 = 50 + m * (50 - q1), cs0 = 0.5 * 50 * (dint - 50), cs1 = 0.5 * q1 * (dint - p1), ped = 1 / m;
  $("#t1").textContent = Lib.fmtN(ped, 2); $("#t2").textContent = "$" + Lib.fmtN(p1, 1); $("#t3").textContent = Lib.fmtN(cs0, 0) + " to " + Lib.fmtN(cs1, 0);
  $("#tv").textContent = L === 0 ? "No cost rise, so nothing changes." : `Supply shifts left by ${L}. With PED ${Lib.fmtN(ped, 2)} (${ped > 1 ? "elastic" : ped < 1 ? "inelastic" : "unit"}) the price rises by $${Lib.fmtN(p1 - 50, 1)} to $${Lib.fmtN(p1, 1)} and quantity falls from 50 to ${Lib.fmtN(q1, 0)}. Consumer surplus falls by ${Lib.fmtN(cs0 - cs1, 0)}. ${ped < 1 ? "Steeper demand means a bigger price rise, so the loss is larger." : "Flatter demand means a smaller price rise but a larger quantity fall."}`;
  const X = (q) => 60 + q * 5.5, Y = (p) => 270 - p * 1.7; let o = SV.line(60, 270, 600, 270) + SV.line(60, 270, 60, 30);
  o += SV.line(X(0), Y(dint), X(dEnd(m)), Y(50 + m * (50 - dEnd(m))), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(10), X(100), Y(90), "c1", { "stroke-width": 3 }) + SV.line(X(0), Y(10 + 0.8 * L), X(100 - L), Y(90), "c3", { "stroke-width": 3 });
  o += SV.poly([[X(0), Y(dint)], [X(0), Y(p1)], [X(q1), Y(p1)]], "f3", op(0.4)) + SV.poly([[X(0), Y(p1)], [X(0), Y(50)], [X(50), Y(50)], [X(q1), Y(p1)]], "f2", op(0.7)) + SV.circle(X(50), Y(50), 5, "dot1") + SV.circle(X(q1), Y(p1), 6, "dot3");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sl", label: "Steepness of demand (3 = flat and elastic, 12 = steep and inelastic) ", min: 3, max: 12, step: 1, value: 4, fmt: (v) => v, onInput: labE });
Lib.slider($("#g2"), { id: "cc", label: "Size of the leftward shift of supply ", min: 0, max: 30, step: 5, value: 15, fmt: (v) => v, onInput: labE });
labE();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to consumer surplus?", buckets: [{"label": "Rises"}, {"label": "Falls"}, {"label": "Depends"}], items: [{"text": "A subsidy to producers lowers the price", "b": 0}, {"text": "An indirect tax on a good", "b": 1}, {"text": "Demand shifts right", "b": 0}, {"text": "An effective minimum price above equilibrium", "b": 1}, {"text": "Costs fall and supply shifts right", "b": 0}, {"text": "An import tariff raises the price", "b": 1}, {"text": "The price falls but quantity bought is fixed", "b": 0}, {"text": "A tax: size of the loss for steep vs flat demand", "b": 2}], done: "A lower price raises consumer surplus; a higher price lowers it. The size of the change depends on elasticity." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Welfare loss", "Lost total surplus when trades no longer happen"], ["Indirect tax", "Shifts supply left, lowers CS, raises government revenue"], ["Subsidy", "Shifts supply right, raises CS"], ["Minimum price", "Raises price above equilibrium, lowers CS"], ["Inelastic demand", "Steep demand: price changes a lot, quantity little"], ["Elastic demand", "Flat demand: quantity changes a lot, price little"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of a tax on surplus in order.", items: ["An indirect tax is imposed on the good", "Supply shifts to the left", "The price consumers pay rises and quantity falls", "Consumer surplus (and producer surplus) fall", "The size of the fall depends on elasticity"], done: "Tax, supply left, price up, surplus down, size depends on elasticity." });
Lib.calc($("#c1"), { qs: [
  {"q": "Demand: P = 100 − 2Q; original supply P = 10 + Q, equilibrium Q = 30, P = $40. Consumer surplus = ½ × 30 × 60. What is it?", "a": 900, "unit": "$", "tol": 1, "hint": "½ × 30 × 60.", "sol": "<b>$900</b>."},
  {"q": "A tax shifts supply to P = 25 + Q. What is the new equilibrium quantity?", "a": 25, "unit": "units", "tol": 0.5, "hint": "100 − 2Q = 25 + Q.", "sol": "75 = 3Q, so Q = <b>25</b>, P = $50."},
  {"q": "What is the new consumer surplus (½ × Q × (100 − P))?", "a": 625, "unit": "$", "tol": 1, "hint": "½ × 25 × 50.", "sol": "<b>$625</b>."},
  {"q": "By how much did consumer surplus fall ($)?", "a": 275, "unit": "$", "tol": 1, "hint": "900 − 625.", "sol": "<b>$275</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A fall in price will usually cause consumer surplus to:", opts: ["Rise", "Fall", "Stay the same", "Become zero"], a: 0, why: "Buyers pay less than before." },
  { q: "A tax shifts supply left. Consumer surplus falls most when demand is:", opts: ["Inelastic (steep)", "Elastic (flat)", "Perfectly elastic", "Unit elastic only"], a: 0, why: "A steeper demand curve means a larger price rise." },
  { q: "A price control that stops some mutually beneficial trades causes:", opts: ["A welfare loss", "A rise in total surplus", "More consumer surplus only", "No change"], a: 0, why: "Total surplus falls." },
  { q: "A subsidy to producers will usually:", opts: ["Raise consumer surplus", "Lower consumer surplus", "Raise the price", "Reduce quantity"], a: 0, why: "Price falls and quantity rises." },
  { q: "An effective maximum price:", opts: ["Reduces producer surplus", "Raises producer surplus", "Has no effect on surplus", "Always raises total surplus"], a: 0, why: "Producers receive a lower price and sell fewer units." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price up", "CS down, PS up."],
  ["Price down", "CS up, PS down."],
  ["Tax", "Supply left, CS down."],
  ["Subsidy", "Supply right, CS up."],
  ["Max price", "Shortage, PS down."],
  ["Min price", "Surplus, CS down."],
  ["Welfare loss", "Lost total surplus."],
  ["Elasticity", "Decides how big the change is."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The market for good X is in equilibrium. A government then introduces an effective minimum price on good X. What will decrease as a result of this minimum price? (May/June 2022 · 14 · Q17, reworded)", opts: ["the excess supply of the product", "the market price of the product", "the quantity of the product supplied", "the size of the consumer surplus"], a: 3, why: "A price above equilibrium raises the price and cuts quantity demanded, so consumer surplus falls. Excess supply and quantity supplied rise." },
  { q: "There are 10 000 tickets available to watch a sports final. The initial market equilibrium ticket price is $20. The government decides to fix an effective minimum price for the tickets. Under which conditions will the consumer surplus decrease the most as a result of the minimum price? (minimum price $18 or $22; price elasticity of demand −0.5 or −1.5) (May/June 2023 · 13 · Q14, reworded)", opts: ["$18 and −0.5", "$18 and −1.5", "$22 and −0.5", "$22 and −1.5"], a: 2, why: "A minimum price at $18 is below equilibrium and has no effect. At $22 the price paid rises, and with inelastic demand (−0.5) buyers keep buying most tickets at a much higher price, so the loss of consumer surplus is largest." },
  { q: "The equilibrium price of a product is $10. The government introduces an effective minimum price of $12 for the product. Under which condition will the value of the producer surplus increase the most? (May/June 2020 · 13 · Q8, reworded)", opts: ["price elasticity of demand is 0", "price elasticity of demand is between 0 and 1", "price elasticity of demand is 1", "price elasticity of demand is greater than 1"], a: 0, why: "If demand is perfectly inelastic, quantity sold does not fall, so producers gain the full higher price on every unit." },
  { q: "A country imports natural gas for which it has price-inelastic demand. What is the effect if that country imposes an import duty on the gas? (May/June 2024 · 13 · Q27, reworded)", opts: ["Consumers in the importing country will suffer a loss of consumer surplus", "The exporting country will gain export revenue", "The importing country's primary income will increase", "The price of natural gas will rise in other importing countries"], a: 0, why: "The duty raises the price paid. With inelastic demand consumers keep buying, so they pay more for the same quantity and lose consumer surplus." },
] });
