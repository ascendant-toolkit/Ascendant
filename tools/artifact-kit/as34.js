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

function pcDraw(s) {
  const p = s.p, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8); let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, ...op(s.v) }) + tag(724, SDY(p) - 6, p < 50 ? "Max price" : "Min price", "c4", s.v, "end");
  if (s.v > 0.2 && Math.abs(qd - qs) > 1) o += SV.rect(SDX(Math.min(qd, qs)), SDY(p) - 8, Math.abs(SDX(qd) - SDX(qs)), 16, p < 50 ? "f3" : "f2", op(0.7 * s.v)) + SV.circle(SDX(qd), SDY(p), 6, "dot2", op(s.v)) + SV.circle(SDX(qs), SDY(p), 6, "dot1", op(s.v)) + tag(SDX(Math.max(qd, qs)) + 10, SDY(p) + 22, (p < 50 ? "shortage " : "surplus ") + Lib.fmtN(Math.abs(qd - qs), 0), p < 50 ? "c3" : "c2", s.v);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${pcDraw({ p: 35, v: 1 })}</svg>`;
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A minimum price above equilibrium creates a surplus">${pcDraw({ p: 65, v: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A maximum price of $35", base: { p: 35, v: 0 }, draw: pcDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market clears at $50 and 50 units. Housing, bread and fuel are common targets for price caps.", s: { p: 35, v: 0 } },
  { cap: "<b>A maximum price of $35</b> is below equilibrium. At $35 buyers want 69 units but firms supply only 31: a <b>shortage</b> of 38.", s: { p: 35, v: 1 } },
  { cap: "<b>Only 31 units are traded.</b> They must be rationed by queues, waiting lists or contacts, and a <b>black market</b> may form where buyers pay more than $35.", s: { p: 35, v: 1 } },
] });
Lib.stepper($("#stN"), { w: 760, h: 300, label: "A minimum price of $65", base: { p: 65, v: 0 }, draw: pcDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market clears at $50 and 50 units.", s: { p: 65, v: 0 } },
  { cap: "<b>A minimum price of $65</b> is above equilibrium. At $65 firms supply 69 units but buyers want only 31: a <b>surplus</b> of 38.", s: { p: 65, v: 1 } },
  { cap: "<b>Only 31 units are bought.</b> The government may buy the surplus (a cost to taxpayers) or it may go to waste. Consumers pay more and lose consumer surplus.", s: { p: 65, v: 1 } },
] });

/* ---------- Lab 1 ---------- */
let kd = "max";
function labP() {
  if (!$("#pc")) return;
  const p = +$("#pc").value, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8), eff = kd === "max" ? p < 50 : p > 50, gap = Math.abs(qd - qs);
  $$("#kind button").forEach((b) => b.classList.toggle("pri", b.dataset.k === kd));
  $("#r1").textContent = Lib.fmtN(eff ? qd : 50, 0); $("#r2").textContent = Lib.fmtN(eff ? qs : 50, 0); $("#r3").textContent = !eff ? "No effect" : kd === "max" ? "Shortage " + Lib.fmtN(gap, 0) : "Surplus " + Lib.fmtN(gap, 0);
  $("#rv").textContent = !eff ? `A ${kd === "max" ? "maximum" : "minimum"} price of $${p} is ${kd === "max" ? "at or above" : "at or below"} the equilibrium of $50, so it has no effect: the market still clears at $50 and 50 units.` : kd === "max" ? `At $${p} buyers want ${Lib.fmtN(qd, 0)} units but firms supply ${Lib.fmtN(qs, 0)}, so there is a shortage of ${Lib.fmtN(gap, 0)}. Only ${Lib.fmtN(qs, 0)} are traded and they must be rationed; a black market is likely.` : `At $${p} firms supply ${Lib.fmtN(qs, 0)} units but buyers want ${Lib.fmtN(qd, 0)}, so there is a surplus of ${Lib.fmtN(gap, 0)}. Only ${Lib.fmtN(qd, 0)} are traded. If the government buys the surplus it spends $${Lib.fmtN(p * gap, 0)}.`;
  $("#labA").innerHTML = pcDraw({ p: eff ? p : 50, v: eff ? 1 : 0 }) + (eff ? "" : SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, "stroke-dasharray": "6 4" }) + tag(724, SDY(p) - 6, kd === "max" ? "Max price" : "Min price", "c4", 1, "end"));
}
$("#kind").innerHTML = `<button class="b" data-k="max">Maximum price</button><button class="b" data-k="min">Minimum price</button>`;
$$("#kind button").forEach((b) => (b.onclick = () => { kd = b.dataset.k; const el = $("#pc"); el.value = kd === "max" ? 35 : 65; el.dispatchEvent(new Event("input", { bubbles: true })); }));
Lib.slider($("#g1"), { id: "pc", label: "Controlled price, $ ", min: 20, max: 80, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#cap") || !$("#sn")) return;
  const p = +$("#cap").value, n = +$("#sn").value / 10, qs = 50 + (p - 50) / n, qd = 50 + (50 - p) / 0.8, pb = 50 + 0.8 * (50 - qs), X = (q) => 70 + q * 6, Y = (v) => 270 - v * 2.2;
  $("#t1").textContent = Lib.fmtN(qd - qs, 0); $("#t2").textContent = "$" + p; $("#t3").textContent = "$" + Lib.fmtN(pb, 0);
  $("#tv").textContent = `With a legal maximum of $${p} firms supply only ${Lib.fmtN(qs, 0)} units and buyers want ${Lib.fmtN(qd, 0)}, a shortage of ${Lib.fmtN(qd - qs, 0)}. Buyers would pay up to $${Lib.fmtN(pb, 0)} for the last unit supplied, so a black market could charge about $${Lib.fmtN(pb - p, 0)} above the legal price. ${n >= 0.8 ? "Supply is inelastic, so the shortage is smaller but the black-market premium is large." : "Supply is elastic, so firms cut output a lot and the shortage is bigger."}`;
  let o = SV.line(70, 270, 700, 270) + SV.line(70, 270, 70, 30) + SV.line(X(0), Y(50 + 50 * 0.8), X(100), Y(50 - 50 * 0.8), "c2", { "stroke-width": 3 }) + SV.line(X(0), Y(Math.max(0, 50 - 50 * n)), X(100), Y(50 + 50 * n), "c1", { "stroke-width": 3 });
  o += SV.line(70, Y(p), X(qd), Y(p), "c4", { "stroke-width": 2.5 }) + SV.line(X(qs), Y(p), X(qs), Y(pb), "dash") + SV.line(70, Y(pb), X(qs), Y(pb), "dash") + SV.circle(X(qs), Y(pb), 6, "dot3") + SV.circle(X(qs), Y(p), 5, "dot1") + SV.circle(X(qd), Y(p), 5, "dot2");
  o += SV.text(62, Y(p) + 4, "$" + p, "sm", { "text-anchor": "end" }) + SV.text(62, Y(pb) + 4, "$" + Lib.fmtN(pb, 0), "sm", { "text-anchor": "end" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "cap", label: "Legal maximum price, $ ", min: 20, max: 45, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "sn", label: "Steepness of supply (3 = elastic, 10 = inelastic) ", min: 3, max: 10, step: 1, value: 8, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What is the effect?", buckets: [{"label": "Shortage"}, {"label": "Surplus"}, {"label": "No effect"}], items: [{"text": "Maximum price of $35, equilibrium $50", "b": 0}, {"text": "Minimum price of $65, equilibrium $50", "b": 1}, {"text": "Maximum price of $60, equilibrium $50", "b": 2}, {"text": "Minimum price of $40, equilibrium $50", "b": 2}, {"text": "Rent controlled below the market rent", "b": 0}, {"text": "Guaranteed price for wheat above the market price", "b": 1}, {"text": "Price cap on bread set at the market price", "b": 2}, {"text": "Minimum price per unit of alcohol above the market price", "b": 1}], done: "A maximum below equilibrium creates a shortage; a minimum above equilibrium creates a surplus; on the wrong side, no effect." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Maximum price", "A legal limit on how high a price can go"], ["Minimum price", "A legal limit on how low a price can go"], ["Black market", "Illegal trade at a price above the legal maximum"], ["Rationing", "Sharing out a shortage without using price"], ["Excess supply", "Quantity supplied exceeds quantity demanded"], ["Effective control", "Set on the side of equilibrium where it binds"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a maximum price in order.", items: ["The government sets a maximum price below equilibrium", "Quantity demanded rises and quantity supplied falls", "A shortage develops", "Goods must be rationed and a black market may appear", "Some consumers gain and others cannot buy"], done: "Cap, shortage, rationing, black market." });
Lib.calc($("#c1"), { qs: [
  {"q": "Equilibrium price is $50. A maximum price of $35 gives Qd = 69 and Qs = 31. What is the shortage (units)?", "a": 38, "unit": "units", "tol": 0.5, "hint": "69 − 31.", "sol": "<b>38</b>."},
  {"q": "With a minimum price of $65, Qs = 69 and Qd = 31. What is the surplus?", "a": 38, "unit": "units", "tol": 0.5, "hint": "69 − 31.", "sol": "<b>38</b>."},
  {"q": "The government buys the surplus of 38 units at the minimum price of $65. What does it cost ($)?", "a": 2470, "unit": "$", "tol": 1, "hint": "65 × 38.", "sol": "<b>$2,470</b>."},
  {"q": "A cap of $35 is set. Quantity traded is the quantity supplied (31). What is consumers' spending at the legal price ($)?", "a": 1085, "unit": "$", "tol": 1, "hint": "35 × 31.", "sol": "<b>$1,085</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An effective maximum price is set:", opts: ["Below the equilibrium price", "Above the equilibrium price", "At the equilibrium price", "At the cost of production"], a: 0, why: "Below equilibrium." },
  { q: "An effective minimum price creates:", opts: ["A surplus", "A shortage", "A black market", "No change"], a: 0, why: "Qs > Qd." },
  { q: "A likely consequence of a maximum price is:", opts: ["A black market", "Excess supply", "Falling demand", "Lower quantity demanded"], a: 0, why: "Shortage encourages illegal trade." },
  { q: "Minimum prices on demerit goods aim to:", opts: ["Reduce consumption", "Raise consumption", "Lower the price", "Shift supply right"], a: 0, why: "Higher price cuts demand." },
  { q: "A price control set at the equilibrium:", opts: ["Has no effect", "Creates a shortage", "Creates a surplus", "Raises quantity"], a: 0, why: "Nothing binds." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Maximum price", "Below equilibrium: shortage."],
  ["Minimum price", "Above equilibrium: surplus."],
  ["Quantity traded", "The smaller side."],
  ["Rationing", "Queues and waiting lists."],
  ["Black market", "Illegal sales above cap."],
  ["Surplus", "Government may buy it."],
  ["Winners", "Consumers who still get the good."],
  ["Evaluate", "Elasticity, alternatives."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A government imposes a maximum rent in order to make rented housing more affordable. What is likely to be a long-run consequence if the maximum is set below the current free market level? (Feb/March 2020 · 12 · Q15, reworded)", opts: ["a shortage of applicants for rented housing", "a shortage of rented housing", "an increase in supply to satisfy the increased demand for rented housing", "an increase in the number of houses being rented"], a: 1, why: "A rent limit below the market level discourages landlords from supplying, so there is a shortage of housing." },
  { q: "What are the effects of a government imposing a maximum price below the equilibrium price on demand and supply? (Feb/March 2022 · 12 · Q15, reworded)", opts: ["demand falls, supply falls", "demand falls, supply rises", "demand rises, supply falls", "demand rises, supply rises"], a: 2, why: "The lower price extends quantity demanded and contracts quantity supplied." },
  { q: "Which row shows the effect of a maximum price above equilibrium, a maximum price below equilibrium and a minimum price above equilibrium? (May/June 2022 · 11 · Q14, reworded)", opts: ["excess demand, no effect, no effect", "excess supply, no effect, no effect", "no effect, excess demand, excess supply", "no effect, excess supply, excess demand"], a: 2, why: "A maximum above equilibrium has no effect, one below creates excess demand, and a minimum above equilibrium creates excess supply." },
  { q: "The demand and supply functions for a product are quantity demanded = 1500 + 50P and quantity supplied = 300P − 2000, where P is price. With government regulation, the current price in the market is $15. What can be concluded about the form of price regulation and the balance of demand and supply? (May/June 2022 · 12 · Q15, reworded)", opts: ["effective maximum price, excess demand", "effective maximum price, excess supply", "effective minimum price, excess demand", "effective minimum price, excess supply"], a: 3, why: "Equilibrium is at P = $14. At $15 quantity demanded is 2,250 and supplied 2,500, so there is excess supply, which means an effective minimum price." },
  { q: "A government imposes a maximum price on medical face masks, below the market equilibrium. What is the most likely effect of this? (May/June 2022 · 13 · Q17, reworded)", opts: ["Some consumers will be unable to buy face masks at the maximum price", "Firms will produce more masks to meet the excess demand at the maximum price", "Poorer consumers will be able to obtain all the masks they need at the maximum price", "The market will clear at the maximum price"], a: 0, why: "A shortage means some consumers cannot buy at the capped price." },
  { q: "After a series of poor harvests, a government imposes an effective maximum price on cereals. What would be a consequence of this policy? (Feb/March 2021 · 12 · Q14, reworded)", opts: ["Both rich and poor people would satisfy their demands equally", "Illegal buying and selling through a black market would be prevented", "Rationing would be necessary to ensure a fair distribution of cereals", "The market would fail to clear leaving a surplus of cereals"], a: 2, why: "A shortage means rationing is needed. A black market becomes more likely." },
  { q: "Which statement about maximum and minimum prices is correct? (May/June 2025 · 13 · Q12, reworded)", opts: ["With an effective maximum price for a product, a shortage will develop", "With an effective maximum price for a product, the market price will rise", "With an effective minimum price for a product, rationing will be necessary", "With an effective minimum price for a product, the market price will fall"], a: 0, why: "A maximum price below equilibrium creates excess demand, a shortage." },
] });
