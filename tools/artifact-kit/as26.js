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

const poly = (pts, c, v) => SV.poly(pts.map(([q, p]) => [SDX(q), SDY(p)]), c, op(v));
function sfDraw(s) {
  let o = sdPlot({ d: 0, s: 0, g: 0 }) + SV.line(70, SDY(50), SDX(50), SDY(50), "dash") + SV.text(62, SDY(50) + 4, "P", "sm", { "text-anchor": "end" }) + SV.text(SDX(50), 286, "Q", "sm", { "text-anchor": "middle" });
  o += poly([[0, 90], [0, 50], [50, 50]], "f3", 0.5 * s.c) + poly([[0, 10], [0, 50], [50, 50]], "f2", 0.5 * s.p);
  if (s.c > 0.2) o += SV.text(SDX(14), SDY(60) + 4, "Consumer surplus", "lbl bd", { ...halo, ...op(s.c) });
  if (s.p > 0.2) o += SV.text(SDX(14), SDY(40) + 4, "Producer surplus", "lbl bd", { ...halo, ...op(s.p) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Consumer surplus is the triangle below the demand curve and above the price">${sfDraw({ c: 1, p: 0 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Producer surplus is the triangle above the supply curve and below the price">${sfDraw({ c: 0, p: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "Consumer and producer surplus on a supply and demand diagram", base: { c: 0, p: 0 }, draw: sfDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The market.</b> Demand shows what buyers are willing to pay; supply shows the lowest price sellers will accept. The equilibrium price is $50.", s: { c: 0, p: 0 } },
  { cap: "<b>Consumer surplus.</b> Buyers on the upper part of the demand curve would pay more than $50, so they gain the gap. The triangle below demand and above the price is <b>consumer surplus</b>.", s: { c: 1, p: 0 } },
  { cap: "<b>Producer surplus.</b> Sellers on the lower part of the supply curve would accept less than $50. The triangle above supply and below the price is <b>producer surplus</b>.", s: { c: 1, p: 1 } },
  { cap: "<b>Total surplus</b> is the two areas together. It is greatest at the equilibrium, where every unit worth more to buyers than it costs to produce is traded.", s: { c: 1, p: 1 } },
] });

/* ---------- individual buyers ---------- */
function bbDraw(s) {
  const W = [90, 80, 70, 60, 50], px = 60, y = (v) => 270 - v * 2.4; let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Willingness to pay ($)", "sm");
  W.forEach((w, i) => { const x = 90 + i * 120, buys = w >= px; o += SV.rect(x, y(w), 70, 270 - y(w), "f1", op(0.35 * s.a)); if (buys && s.c > 0) o += SV.rect(x, y(w), 70, y(px) - y(w), "f3", op(0.7 * s.c)) + SV.text(x + 35, (y(w) + y(px)) / 2 + 5, "$" + (w - px), "lbl bd", { "text-anchor": "middle", ...op(s.c) }); o += SV.text(x + 35, 286, "Buyer " + "ABCDE"[i], "sm", { "text-anchor": "middle", ...op(s.a) }) + SV.text(x + 35, y(w) - 6, "$" + w, "sm", { "text-anchor": "middle", ...op(s.a) }); });
  if (s.b > 0) o += SV.line(60, y(px), 700, y(px), "c4", { "stroke-width": 2.5, ...op(s.b) }) + tag(696, y(px) - 6, "Market price $60", "c4", s.b, "end");
  if (s.c > 0.5) o += tag(380, 50, "Consumer surplus = 30 + 20 + 10 + 0 = $60. Buyer E (willing to pay $50) does not buy.", "c3", s.c, "middle");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 300, label: "Five buyers, a market price of $60 and their surplus", base: { a: 0, b: 0, c: 0 }, draw: bbDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Willingness to pay.</b> Five buyers would pay at most $90, $80, $70, $60 and $50 for one unit.", s: { a: 1 } },
  { cap: "<b>A market price of $60.</b> Buyers A to D are willing to pay at least $60, so they buy. Buyer E would pay only $50, so does not.", s: { a: 1, b: 1 } },
  { cap: "<b>Surplus.</b> A gains $30, B $20, C $10 and D nothing (the marginal buyer): consumer surplus is <b>$60</b>.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, e = sdEq(d, s), di = 90 + 0.8 * d, si = 10 - 0.8 * s, cs = 0.5 * e.q * (di - e.p), ps = 0.5 * e.q * (e.p - si), base = 0.5 * 50 * 40;
  $("#r1").textContent = Lib.fmtN(cs, 0); $("#r2").textContent = Lib.fmtN(ps, 0); $("#r3").textContent = Lib.fmtN(cs + ps, 0);
  $("#rv").textContent = d === 0 && s === 0 ? "In the starting equilibrium (price $50, quantity 50) consumer and producer surplus are each 1,000 and the total is 2,000." : `At the new equilibrium (price $${Lib.fmtN(e.p, 0)}, quantity ${Lib.fmtN(e.q, 0)}) consumer surplus is ${Lib.fmtN(cs, 0)} (${cs > base ? "up" : "down"} from 1,000) and producer surplus is ${Lib.fmtN(ps, 0)} (${ps > base ? "up" : "down"} from 1,000). ${d > 0 ? "More demand raises both surpluses. " : ""}${s > 0 ? "More supply lowers the price, raising consumer surplus. " : ""}${d < 0 ? "Less demand lowers both surpluses. " : ""}${s < 0 ? "Less supply raises the price, lowering consumer surplus. " : ""}`;
  let o = sdPlot({ d, s, g: 0, n: 1 }) + poly([[0, di], [0, e.p], [e.q, e.p]], "f3", 0.5) + poly([[0, si], [0, e.p], [e.q, e.p]], "f2", 0.5) + SV.circle(SDX(e.q), SDY(e.p), 5, "dot3");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dd", label: "Demand shift (negative = left, positive = right) ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v, onInput: labS });
Lib.slider($("#g2"), { id: "ss", label: "Supply shift (negative = left, positive = right) ", min: -20, max: 10, step: 5, value: 0, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!$("#pf")) return;
  const p = +$("#pf").value, up = p > 50, Q = up ? (90 - p) / 0.8 : (p - 10) / 0.8, cs = up ? 0.5 * Q * (90 - p) : 90 * Q - 0.4 * Q * Q - p * Q, ps = up ? p * Q - (10 * Q + 0.4 * Q * Q) : 0.5 * Q * (p - 10), loss = 2000 - cs - ps;
  $("#t1").textContent = Lib.fmtN(cs, 0); $("#t2").textContent = Lib.fmtN(ps, 0); $("#t3").textContent = Lib.fmtN(Math.max(0, loss), 0);
  $("#tv").textContent = p === 50 ? "At the equilibrium price of $50, 50 units are traded and total surplus is at its maximum of 2,000." : `At $${p} only ${Lib.fmtN(Q, 0)} units are traded because ${up ? "buyers will not buy more at this high price" : "firms will not supply more at this low price"}. Consumer surplus is ${Lib.fmtN(cs, 0)} and producer surplus ${Lib.fmtN(ps, 0)}, so ${Lib.fmtN(loss, 0)} of total surplus is lost (the welfare loss).`;
  const pts = up ? [[[0, 90], [0, p], [Q, p]], [[0, 10], [0, p], [Q, p], [Q, 10 + 0.8 * Q]]] : [[[0, 90], [0, p], [Q, p], [Q, 90 - 0.8 * Q]], [[0, 10], [0, p], [Q, p]]];
  $("#labB").innerHTML = sdPlot({ d: 0, s: 0, g: 0 }) + poly(pts[0], "f3", 0.5) + poly(pts[1], "f2", 0.5) + SV.line(70, SDY(p), SDX(Math.max(Q, 50)), SDY(p), "c4", { "stroke-width": 2.5 }) + tag(SDX(Math.max(Q, 50)) + 6, SDY(p) + 4, "$" + p, "c4");
}
Lib.slider($("#g3"), { id: "pf", label: "Fixed price, $ ", min: 20, max: 80, step: 5, value: 50, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which surplus is it?", buckets: [{"label": "Consumer surplus"}, {"label": "Producer surplus"}, {"label": "Neither"}], items: [{"text": "A shopper would pay $80 but pays $50", "b": 0}, {"text": "A farmer would accept $3 but sells at $5", "b": 1}, {"text": "The total revenue of a firm", "b": 2}, {"text": "The area below demand and above the price", "b": 0}, {"text": "The area above supply and below the price", "b": 1}, {"text": "A firm's profit after all costs", "b": 2}, {"text": "Passengers who gain when airfares fall", "b": 0}, {"text": "Sellers who gain when the market price rises", "b": 1}], done: "Consumers gain below demand and above the price. Producers gain above supply and below the price. Revenue and profit are not surpluses." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Consumer surplus", "Willingness to pay minus price paid"], ["Producer surplus", "Price received minus the minimum acceptable price"], ["Total surplus", "Consumer plus producer surplus"], ["Welfare loss", "Total surplus lost when output is below the equilibrium"], ["Marginal buyer", "The last buyer, whose surplus is zero"], ["Equilibrium", "Where total surplus is greatest in a competitive market"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of drawing the surplus diagram in order.", items: ["Draw and label the axes, demand and supply", "Mark the equilibrium price and quantity", "Draw a horizontal line at the market price", "Shade the triangle below demand and above the price", "Shade the triangle above supply and below the price"], done: "Consumer surplus is above the price line; producer surplus is below it." });
Lib.calc($("#c1"), { qs: [
  {"q": "Demand: P = 100 − 2Q. Supply: P = 10 + Q. What is the equilibrium quantity?", "a": 30, "unit": "units", "tol": 0.5, "hint": "100 − 2Q = 10 + Q.", "sol": "90 = 3Q, so Q = <b>30</b> and P = $40."},
  {"q": "Using the same curves, what is the consumer surplus? (½ × Q × (100 − P))", "a": 900, "unit": "$", "tol": 1, "hint": "½ × 30 × 60.", "sol": "<b>$900</b>."},
  {"q": "What is the producer surplus? (½ × Q × (P − 10))", "a": 450, "unit": "$", "tol": 1, "hint": "½ × 30 × 30.", "sol": "<b>$450</b>."},
  {"q": "A buyer would pay up to $75 and pays $52. What is that buyer's consumer surplus?", "a": 23, "unit": "$", "tol": 0.5, "hint": "75 − 52.", "sol": "<b>$23</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Consumer surplus is the area:", opts: ["Below demand and above the price", "Above demand and below the price", "Below supply and above the price", "Under the supply curve"], a: 0, why: "Willingness to pay minus price." },
  { q: "A fall in price will usually:", opts: ["Raise consumer surplus", "Lower consumer surplus", "Raise producer surplus for the same quantity", "Not change either"], a: 0, why: "Buyers pay less than before." },
  { q: "Producer surplus is:", opts: ["Price received minus the minimum price producers would accept", "Total revenue", "Profit", "Price paid minus willingness to pay"], a: 0, why: "Above supply, below price." },
  { q: "Total surplus is greatest:", opts: ["At the equilibrium", "When price is fixed above equilibrium", "When price is fixed below equilibrium", "When the government sets price"], a: 0, why: "Allocative efficiency." },
  { q: "Which would reduce consumer surplus?", opts: ["A leftward shift of supply", "A rightward shift of supply", "A subsidy to producers", "A fall in costs"], a: 0, why: "Price rises and quantity falls." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Consumer surplus", "Willing to pay − price paid."],
  ["Producer surplus", "Price received − willing to accept."],
  ["CS area", "Below demand, above price."],
  ["PS area", "Above supply, below price."],
  ["Total surplus", "CS + PS."],
  ["Max at", "Equilibrium."],
  ["Price up", "CS down, PS up."],
  ["Elasticity", "Decides the size of the change."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is meant by consumer surplus? (May/June 2022 · 13 · Q11, reworded)", opts: ["It is the amount by which the price consumers are willing to pay exceeds the market price", "It is the difference between the price consumers are willing to pay and the price producers are willing to supply", "It is the discount firms offer to the consumers for buying goods in bulk", "It is the excess of quantity demanded of a product over its quantity supplied at a given price"], a: 0, why: "Consumer surplus is willingness to pay minus the price actually paid." },
  { q: "Which example of consumer behaviour would create consumer surplus? (Feb/March 2021 · 12 · Q8, reworded)", opts: ["when a consumer does not spend all of her income each month", "when a consumer pays less than they are willing to pay for a good", "when a consumer throws away vegetables because they bought too much", "when a good is purchased in order to resell it at a higher price"], a: 1, why: "Paying less than the maximum you would pay creates consumer surplus." },
  { q: "What could cause an increase in consumer surplus in the market for a good? (an increase in demand for the good, an increase in supply of the good) (Oct/Nov 2021 · 13 · Q5, reworded)", opts: ["no increase in demand, no increase in supply", "no increase in demand, an increase in supply", "an increase in demand, no increase in supply", "an increase in demand and an increase in supply"], a: 3, why: "A higher demand lifts the demand curve and so adds willingness to pay, and a rise in supply lowers the price, so both raise consumer surplus." },
  { q: "A private company achieves a producer surplus at the market equilibrium price. What might reduce the size of the private company's producer surplus? (May/June 2021 · 12 · Q11, reworded)", opts: ["Private companies choose to prioritise profits over customer needs", "Private companies start to pay dividends out of profits", "The government fixes the price of electricity below the market price", "The private company supply curve becomes more elastic"], a: 2, why: "A price below the market price lowers the price producers receive, so their surplus falls." },
  { q: "An economy with a long history of extensive barriers to trade decides to switch to totally free trade. What is most likely to increase in the short term? (May/June 2020 · 13 · Q26, reworded)", opts: ["consumer surplus", "government revenue", "inflationary pressure", "profits of all domestic companies"], a: 0, why: "Removing trade barriers lowers prices for consumers, so consumer surplus rises. Tariff revenue and some domestic profits fall." },
] });
