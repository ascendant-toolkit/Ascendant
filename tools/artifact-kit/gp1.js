/* ---------- model: demand P = 100 - Q, supply P = 20 + Q (equilibrium Q = 40, P = 60) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 7.5, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const marketLines = (s) => (s.d > 0 ? SV.line(X(0), Y(100), X(90), Y(10), "c1", op(s.d)) + SV.text(X(90) - 4, Y(10) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) : "") +
  (s.s > 0 ? SV.line(X(0), Y(20), X(80), Y(100), "c2", op(s.s)) + SV.text(X(80) - 4, Y(100) + 16, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) }) : "");
const eqMark = (s) => s.eq > 0 ? SV.line(X(40), Y(60), X(40), 330, "gr", op(s.eq)) + SV.line(70, Y(60), X(40), Y(60), "gr", op(s.eq)) + SV.circle(X(40), Y(60), 6, "dot3", op(s.eq)) + SV.text(66, Y(60) + 4, "60", "sm bd", { "text-anchor": "end", ...op(s.eq) }) + SV.text(X(40), 350, "40", "lbl bd", { "text-anchor": "middle", ...op(s.eq) }) : "";

/* maximum price (Learn picture and Watch 1) */
function ceilingDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.c > 0) o += SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40", "lbl bd t4", { "text-anchor": "end", ...op(s.c) });
  if (s.q > 0) o += SV.line(X(20), Y(40), X(20), 330, "gr", op(s.q)) + SV.line(X(60), Y(40), X(60), 330, "gr", op(s.q)) + SV.circle(X(20), Y(40), 6, "dot2", op(s.q)) + SV.circle(X(60), Y(40), 6, "dot1", op(s.q)) + SV.text(X(20), 350, "Qs = 20", "lbl bd", { "text-anchor": "middle", ...op(s.q) }) + SV.text(X(60), 350, "Qd = 60", "lbl bd", { "text-anchor": "middle", ...op(s.q) });
  if (s.sh > 0) o += SV.rect(X(20), Y(40) - 7, X(60) - X(20), 14, "f2", op(s.sh)) + SV.text((X(20) + X(60)) / 2, Y(40) - 16, "Shortage = 40", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.sh) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 370" role="img" aria-label="Supply and demand with a maximum price at 40 causing a shortage, and a minimum price at 80 causing a surplus">${axes()}${marketLines({ d: 1, s: 1 })}${eqMark({ eq: 1 })}
  ${SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3 })}${SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40: shortage 40", "lbl bd t4", { "text-anchor": "end", ...halo })}
  ${SV.line(70, Y(80), X(90), Y(80), "c3", { "stroke-width": 3 })}${SV.text(X(90) - 4, Y(80) - 8, "Minimum price $80: surplus 40", "lbl bd t3", { "text-anchor": "end", ...halo })}
  ${SV.rect(X(20), Y(40) - 6, X(60) - X(20), 12, "f2")}${SV.rect(X(20), Y(80) - 6, X(60) - X(20), 12, "f3")}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 370, label: "A maximum price below the equilibrium price causing a shortage", base: { d: 0, s: 0, eq: 0, c: 0, q: 0, sh: 0 }, draw: ceilingDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Demand meets supply at <b>$60</b> and <b>40 units</b>. There is no shortage or surplus.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The government sets a maximum price of $40</b>, below the equilibrium price, to make the good more affordable. The line is a legal limit.", s: { d: 1, s: 1, eq: 1, c: 1 } },
  { cap: "<b>Quantities at $40.</b> Consumers now want <b>60</b> units (Qd). But at that price firms are only willing to supply <b>20</b> (Qs).", s: { d: 1, s: 1, eq: 1, c: 1, q: 1 } },
  { cap: "<b>A shortage of 40.</b> Only 20 units are traded. Goods must be rationed by queues, favouritism or a <b>black market</b>, and suppliers may cut quality or leave the market. Consumers who get the good gain, others lose out.", s: { d: 1, s: 1, eq: 1, c: 1, q: 1, sh: 1 } },
] });

/* minimum price (Watch 2) */
function floorDraw(s) {
  let o = axes() + marketLines(s) + eqMark(s);
  if (s.c > 0) o += SV.line(70, Y(80), X(90), Y(80), "c3", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(80) - 8, "Minimum price $80", "lbl bd t3", { "text-anchor": "end", ...op(s.c) });
  if (s.q > 0) o += SV.line(X(20), Y(80), X(20), 330, "gr", op(s.q)) + SV.line(X(60), Y(80), X(60), 330, "gr", op(s.q)) + SV.circle(X(20), Y(80), 6, "dot1", op(s.q)) + SV.circle(X(60), Y(80), 6, "dot2", op(s.q)) + SV.text(X(20), 350, "Qd = 20", "lbl bd", { "text-anchor": "middle", ...op(s.q) }) + SV.text(X(60), 350, "Qs = 60", "lbl bd", { "text-anchor": "middle", ...op(s.q) });
  if (s.sh > 0) o += SV.rect(X(20), Y(80) - 7, X(60) - X(20), 14, "f3", op(s.sh)) + SV.text((X(20) + X(60)) / 2, Y(80) - 16, "Surplus = 40", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.sh) });
  return o;
}
Lib.stepper($("#stB"), { w: 780, h: 370, label: "A minimum price above the equilibrium price causing a surplus", base: { d: 0, s: 0, eq: 0, c: 0, q: 0, sh: 0 }, draw: floorDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Equilibrium at $60 and 40 units.", s: { d: 1, s: 1, eq: 1 } },
  { cap: "<b>The government sets a minimum price of $80</b>, above the equilibrium price. For example to raise farmers' incomes, or to cut consumption of a demerit good such as cheap alcohol.", s: { d: 1, s: 1, eq: 1, c: 1 } },
  { cap: "<b>Quantities at $80.</b> Consumers buy only <b>20</b> (Qd). Firms want to supply <b>60</b> (Qs).", s: { d: 1, s: 1, eq: 1, c: 1, q: 1 } },
  { cap: "<b>A surplus of 40.</b> Producers are left with unsold stock. The government may have to buy and store it, or it goes to waste. Consumers pay more and buy less; producers who sell gain.", s: { d: 1, s: 1, eq: 1, c: 1, q: 1, sh: 1 } },
] });

/* black market (Watch 3) */
function bmDraw(s) {
  let o = axes() + marketLines({ d: 1, s: 1 });
  o += SV.line(70, Y(40), X(90), Y(40), "c4", { "stroke-width": 3, ...op(s.c) }) + SV.text(X(90) - 4, Y(40) + 18, "Maximum price $40", "lbl bd t4", { "text-anchor": "end", ...op(s.c) });
  o += SV.line(X(20), Y(40), X(20), Y(80), "gr", op(s.u)) + SV.circle(X(20), Y(40), 6, "dot2", op(s.u)) + SV.circle(X(20), Y(80), 6, "dot1", op(s.u)) + SV.text(X(20), 350, "Qs = 20", "lbl bd", { "text-anchor": "middle", ...op(s.u) });
  o += SV.line(70, Y(80), X(20), Y(80), "c3", { "stroke-dasharray": "6 5", ...op(s.bm) }) + SV.text(66, Y(80) + 4, "80", "sm bd", { "text-anchor": "end", ...op(s.bm) }) + SV.text(X(20) + 14, Y(80) - 12, "Black market price up to $80", "lbl bd t3", { ...halo, ...op(s.bm) });
  return o;
}
Lib.stepper($("#stK"), { w: 780, h: 370, label: "A maximum price holding supply at 20 units while buyers would pay up to 80", base: { c: 0, u: 0, bm: 0 }, draw: bmDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The ceiling.</b> The government holds the price at <b>$40</b>, below the $60 equilibrium.", s: { c: 1 } },
  { cap: "<b>Supply is held down.</b> At $40 firms supply only <b>20</b> units. Read up the vertical line to the demand curve.", s: { c: 1, u: 1 } },
  { cap: "<b>Buyers would pay up to $80</b> for the 20th unit (the demand curve at 20). The legal price of $40 leaves a big gap that sellers can exploit: a <b>black market</b> may charge close to $80, so the ceiling can help some consumers but hurt others.", s: { c: 1, u: 1, bm: 1 } },
] });
/* ---------- Lab 1: price control ---------- */
function lab1() {
  if (!$("#pc")) return;
  const p = +$("#pc").value, qd = Math.max(0, 100 - p), qs = Math.max(0, p - 20), tr = Math.min(qd, qs), gap = qd - qs;
  $("#r1").textContent = qd; $("#r2").textContent = qs; $("#r3").textContent = gap === 0 ? "none" : gap > 0 ? "shortage " + gap : "surplus " + -gap; $("#r4").textContent = tr;
  $("#rv").textContent = p === 60 ? "The price equals the market price, so there is no shortage or surplus: the control has no effect."
    : p < 60 ? `A maximum price at $${p} is below the market price. Consumers want ${qd} but suppliers offer only ${qs}: a shortage of ${gap}. Only ${tr} units are traded, so some buyers go without or pay on a black market.`
    : `A minimum price at $${p} is above the market price. Consumers buy only ${qd} but suppliers offer ${qs}: a surplus of ${-gap}. Only ${tr} units are sold.`;
  const x = (v) => 40 + v * 3.9, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.line(x(0), y(100), x(90), y(10), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + SV.line(40, y(p), 400, y(p), p < 60 ? "c4" : p > 60 ? "c3" : "gr", { "stroke-width": 3 });
  if (gap !== 0) o += SV.rect(x(Math.min(qd, qs)), y(p) - 6, Math.abs(x(qd) - x(qs)), 12, gap > 0 ? "f2" : "f3");
  o += SV.circle(x(qd), y(p), 6, "dot1") + SV.circle(x(qs), y(p), 6, "dot2") + SV.text(x(qd), 288, "Qd", "sm bd t1", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t2", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pc", label: "Legal price ($): ", min: 20, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: buying the surplus ---------- */
function lab5() {
  if (!$("#mp")) return;
  const p = +$("#mp").value, qd = Math.max(0, 100 - p), qs = Math.max(0, p - 20), sur = p > 60 ? qs - qd : 0, cost = sur * p;
  $("#m1r").textContent = qd; $("#m2r").textContent = qs; $("#m3r").textContent = sur || "none"; $("#m4r").textContent = "$" + cost;
  $("#mv").textContent = p <= 60 ? `A minimum of $${p} is at or below the market price of $60, so it is not binding: no surplus and no cost.`
    : `At $${p} consumers buy ${qd} but firms supply ${qs}: a surplus of ${sur}. If the government buys it all, the cost is ${sur} x $${p} = $${cost}, paid by taxpayers. The higher the floor, the bigger the surplus and the bill.`;
  const x = (v) => 40 + v * 3.9, y = (v) => 270 - v * 2.4;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  if (sur > 0) o += SV.rect(x(qd), y(p), x(qs) - x(qd), 270 - y(p), "f3") + SV.text((x(qd) + x(qs)) / 2, y(p) + (270 - y(p)) / 2 + 4, "cost $" + cost, "lbl bd", { "text-anchor": "middle" });
  o += SV.line(x(0), y(100), x(90), y(10), "c1") + SV.line(x(0), y(20), x(80), y(100), "c2") + SV.line(40, y(p), 400, y(p), p > 60 ? "c3" : "gr", { "stroke-width": 3 });
  o += SV.circle(x(qd), y(p), 6, "dot1") + SV.circle(x(qs), y(p), 6, "dot2") + SV.text(x(qd), 288, "Qd", "sm bd t1", { "text-anchor": "middle" }) + SV.text(x(qs), 306, "Qs", "sm bd t2", { "text-anchor": "middle" });
  $("#labE").innerHTML = o;
}
Lib.slider($("#g6"), { id: "mp", label: "Minimum price ($): ", min: 40, max: 100, step: 5, value: 80, fmt: (v) => v, onInput: lab5 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "The market price is $60. What happens with each price control?",
  buckets: [{ label: "Shortage" }, { label: "Surplus" }, { label: "No effect" }],
  items: [
    { text: "Maximum price of $40", b: 0 }, { text: "Rent ceiling below the market rent", b: 0 }, { text: "Cap on bread prices below the market price", b: 0 },
    { text: "Minimum price of $80", b: 1 }, { text: "Guaranteed farm price above the market price", b: 1 }, { text: "Minimum price for alcohol above the market price", b: 1 },
    { text: "Maximum price of $80", b: 2 }, { text: "Minimum price of $50", b: 2 }, { text: "A ceiling above the price firms already charge", b: 2 },
  ], done: "Only a control on the wrong side of the market price is binding.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Maximum price", "A legal limit below the market price, causing a shortage"],
  ["Minimum price", "A legal floor above the market price, causing a surplus"],
  ["Binding", "A control set on the side of equilibrium where it changes the outcome"],
  ["Shortage", "Quantity demanded is greater than quantity supplied"],
  ["Surplus", "Quantity supplied is greater than quantity demanded"],
  ["Rationing", "Deciding who gets the good when there is not enough, by queue, waiting list or favour"],
  ["Black market", "Illegal trade at a price above the legal maximum"],
], done: "Seven words to use in every price control answer." });
Lib.order($("#o1"), { prompt: "Put the explanation of a maximum price in order.", items: [
  "The government sets a maximum price below the equilibrium price",
  "At the lower price the quantity demanded rises",
  "At the lower price the quantity supplied falls",
  "Quantity demanded is greater than quantity supplied: a shortage",
  "The good must be rationed, and black markets and lower quality may appear",
  "Evaluate: who gains (those who get the good), who loses, and alternatives such as subsidies",
], done: "This chain works for any price ceiling question, for example rent control." });

Lib.calc($("#c1"), { qs: [
  { q: "Demand is P = 100 − Q and supply is P = 20 + Q. A maximum price of $40 is set. What is the shortage (units)?", a: 40, hint: "Qd = 100 − P and Qs = P − 20.", sol: "Qd = 60, Qs = 20, shortage = <b>40</b>." },
  { q: "A minimum price of $80 is set in the same market. What is the surplus (units)?", a: 40, sol: "Qd = 20, Qs = 60, surplus = <b>40</b>." },
  { q: "Another market has Qd = 200 − 10P and Qs = 50 + 5P. A maximum price of $6 is set. What is the shortage (units)?", a: 60, hint: "Equilibrium is $10 and 100 units, so $6 is binding.", sol: "Qd = 200 − 60 = 140, Qs = 50 + 30 = 80. Shortage = <b>60</b>." },
  { q: "In that market a minimum price of $14 is set. What is the surplus (units)?", a: 60, sol: "Qd = 200 − 140 = 60, Qs = 50 + 70 = 120. Surplus = <b>60</b>." },
  { q: "The government buys the whole surplus at $14. What is the cost ($)?", a: 840, sol: "60 x 14 = <b>$840</b>." },
  { q: "With the $6 maximum only 80 units are supplied. At what price would consumers demand exactly 80 units, a guide to the black market price ($)?", a: 12, hint: "Solve 200 − 10P = 80.", sol: "10P = 120, so P = <b>$12</b>, double the legal price." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A maximum price set above the equilibrium price is likely to:", opts: ["cause a shortage", "cause a surplus", "have no effect", "raise supply"], a: 2, why: "It is not binding, because the market price is already below the limit." },
  { q: "A binding minimum price will most likely:", opts: ["leave a surplus", "cause a shortage", "lower the price", "raise quantity demanded"], a: 0, why: "At the higher price, quantity supplied exceeds quantity demanded." },
  { q: "Rent control is an example of:", opts: ["a minimum price", "a maximum price", "a subsidy", "a tradable permit"], a: 1, why: "It sets a legal limit on the rent a landlord may charge." },
  { q: "Who pays for a surplus bought by the government after a minimum price?", opts: ["Taxpayers", "Consumers only", "Producers only", "Nobody"], a: 0, why: "The purchase is funded from tax revenue." },
  { q: "A black market is most likely to appear when:", opts: ["a ceiling holds supply well below demand", "a floor is above equilibrium", "supply is perfectly elastic", "the government subsidises the good"], a: 0, why: "Buyers who cannot get the good at the legal price may pay more to illegal sellers." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Maximum price", "A legal limit below equilibrium: causes a shortage."],
  ["Minimum price", "A legal floor above equilibrium: causes a surplus."],
  ["Binding", "A control that is on the wrong side of the market price, so it changes the outcome."],
  ["Shortage", "Quantity demanded greater than quantity supplied."],
  ["Surplus", "Quantity supplied greater than quantity demanded."],
  ["Rationing", "How scarce goods are shared when price cannot do it: queues, waiting lists, favouritism."],
  ["Black market", "Illegal trade above the legal maximum price."],
  ["Guaranteed price", "A minimum price, usually for farm products, backed by government buying."],
  ["Cost of buying the surplus", "Surplus times the minimum price."],
  ["Alternatives to price controls", "Subsidies, cash benefits and increasing supply."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2023 · 32 · Q17] A government imposes a maximum price for electricity. Which statement justifying this measure might be considered valid on economic grounds?", opts: ["It will encourage electricity suppliers to invest in additional capacity.", "It will increase the incentive for consumers to conserve energy.", "It will prevent the monopolistic exploitation of consumers.", "It will prevent the rationing of electricity through power cuts."], a: 2, why: "A price cap can limit the price a monopoly supplier charges. A, B and D are the opposite of what a ceiling does." },
  { q: "[Oct/Nov 2023 · 33 · Q15] To control the cost of living, governments have sometimes imposed a maximum price on certain goods that is below the free market price. What is often an undesirable side effect of such a policy?", opts: ["accelerating general inflation", "an increase in profits above normal profits", "an increase in the stocks of unsold goods held by firms", "shortages of the good"], a: 3, why: "A price below equilibrium makes quantity demanded exceed quantity supplied. C describes the effect of a minimum price." },
  { q: "[May/June 2021 · 31 · Q30] A government is increasing the role of market forces in its economy. However, it imposed temporary maximum price controls. Why might a government, committed to reducing central planning, introduce price controls?", opts: ["to increase allocative efficiency", "to increase the incentive for producers to raise supply", "to reduce consumer demand", "to reduce expectations of inflation"], a: 3, why: "A temporary cap on prices may stop price rises being expected while markets are freed. A ceiling does not raise efficiency, supply or cut demand." },
] });
