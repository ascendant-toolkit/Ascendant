// uses: econ

const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
/* ---------- Watch 1: AR, MR and TR ---------- */
const RLX = (q) => 70 + q * 15, RLY = (p) => 150 - p * 5, RRX = (q) => 450 + q * 14, RRY = (v) => 270 - v * 2;
function revDraw(s) {
  let o = SV.line(70, 150, 380, 150) + SV.line(70, 40, 70, 260) + SV.text(380, 186, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Price, AR, MR ($)", "sm");
  [0, 10, 20].forEach((q) => { o += SV.text(RLX(q), 164, q, "sm", { "text-anchor": "middle" }); });
  o += SV.line(450, 270, 740, 270) + SV.line(450, 40, 450, 276) + SV.text(740, 294, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(456, 34, "Total revenue ($)", "sm");
  if (s.ar > 0) o += SV.line(RLX(0), RLY(20), RLX(20), RLY(0), "c1", op(s.ar)) + SV.text(RLX(19), RLY(0) - 8, "AR = D", "lbl bd t1", { "text-anchor": "end", ...op(s.ar) });
  if (s.mr > 0) o += SV.line(RLX(0), RLY(20), RLX(20), RLY(-20), "c2", op(s.mr)) + SV.text(RLX(18.5), RLY(-17) + 14, "MR", "lbl bd t2", { "text-anchor": "end", ...op(s.mr) });
  if (s.tr > 0) { const pts = []; for (let q = 0; q <= 20 * s.tr + 0.01; q += 0.5) pts.push([RRX(q), RRY(q * (20 - q))]); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c3"); }
  if (s.mk > 0) o += SV.line(RLX(10), RLY(0), RLX(10), 260, "gr", op(s.mk)) + SV.circle(RLX(10), RLY(0), 6, "dot2", op(s.mk)) + SV.line(RRX(10), RRY(100), RRX(10), 270, "gr", op(s.mk)) + SV.circle(RRX(10), RRY(100), 6, "dot3", op(s.mk)) + SV.text(RRX(10) + 10, RRY(100) - 8, "TR = $100 (maximum)", "lbl bd t3", { style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px", ...op(s.mk) }) + SV.text(RLX(10) - 8, RLY(0) + 36, "MR = 0 at Q = 10", "lbl bd t2", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px", ...op(s.mk) });
  return o;
}
Lib.stepper($("#stR2"), { w: 780, h: 310, label: "Average revenue, marginal revenue and total revenue for a price maker", base: { ar: 0, mr: 0, tr: 0, mk: 0 }, draw: revDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Average revenue.</b> The firm can only sell more by cutting its price, so average revenue (price) falls as quantity rises: <b>AR = D = 20 − Q</b>.", s: { ar: 1 } },
  { cap: "<b>Marginal revenue.</b> To sell one more unit the firm cuts the price on <b>all</b> units, so the extra revenue is less than the price. MR = 20 − 2Q lies below AR and is twice as steep. It reaches zero at Q = 10 and then goes negative.", s: { ar: 1, mr: 1 } },
  { cap: "<b>Total revenue.</b> TR = price × quantity. It rises while MR is positive, then falls once MR is negative.", s: { ar: 1, mr: 1, tr: 1 } },
  { cap: "<b>MR = 0 where TR is at its maximum</b> ($100 at Q = 10). At that point price elasticity of demand is 1. A firm that wants maximum revenue stops here; a profit-maximiser stops earlier, where MR = MC.", s: { ar: 1, mr: 1, tr: 1, mk: 1 } },
] });

/* ---------- Watch 2: profit types ---------- */
const PB = 270, PH = (v) => v / 30;
function profDraw(s) {
  const r = s.r, tc = 5200, ok = r > tc + 1, eq = Math.abs(r - tc) <= 1;
  let o = SV.line(60, PB, 740, PB) + SV.text(62, 24, "$", "sm");
  o += SV.rect(160, PB - PH(tc), 110, PH(tc), "f2") + SV.text(215, PB - PH(tc) - 8, "$5,200", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(215, PB + 20, "Total cost", "sm bd", { "text-anchor": "middle" }) + SV.text(215, PB + 38, "(includes normal profit)", "sm", { "text-anchor": "middle" });
  o += SV.rect(420, PB - PH(r), 110, PH(r), ok ? "f3" : eq ? "f4" : "f1") + SV.text(475, PB - PH(r) - 8, "$" + Math.round(r / 10) * 10, "lbl bd", { "text-anchor": "middle" }) + SV.text(475, PB + 20, "Total revenue", "sm bd", { "text-anchor": "middle" }) + SV.text(475, PB + 38, "(price × 500)", "sm", { "text-anchor": "middle" });
  o += SV.text(640, PB - 100, ok ? "supernormal profit" : eq ? "normal profit only" : "subnormal profit", "lbl bd " + (ok ? "t3" : eq ? "t4" : "t2"), { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stP2"), { w: 780, h: 320, label: "Total revenue against total cost, showing supernormal, normal and subnormal profit", base: { r: 5200 }, draw: profDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Total cost is $5,200</b>, including <b>normal profit</b>: the minimum return that keeps the entrepreneur in the industry. If total revenue equals total cost, the firm earns normal profit and is content to stay.", s: { r: 5200 } },
  { cap: "<b>Price $12.</b> Total revenue = 12 × 500 = $6,000, which is $800 more than total cost. That extra $800 is <b>supernormal profit</b>: it may attract new firms unless there are barriers to entry.", s: { r: 6000 } },
  { cap: "<b>Price $10.40.</b> Total revenue = $5,200 equals total cost: only <b>normal profit</b>. There is no incentive to enter or leave.", s: { r: 5200 } },
  { cap: "<b>Price $9.</b> Total revenue = $4,500, which is $700 below total cost. The firm earns <b>subnormal profit</b>, less than the minimum needed. In the long run it may leave the industry.", s: { r: 4500 } },
] });
/* ---------- Lab 3: AR, MR and TR ---------- */
Lib.slider($("#sl4"), { id: "a4", label: "Quantity sold (Q)", min: 1, max: 19, step: 0.5, value: 5, fmt: (v) => v.toFixed(1), onInput: (q) => {
  const P = 20 - q, tr = P * q, mr = 20 - 2 * q, ped = P / q;
  $("#r1").textContent = "$" + Lib.fmtN(P, 1); $("#r2").textContent = "$" + Lib.fmtN(tr, 1); $("#r3").textContent = (mr < 0 ? "−$" : "$") + Lib.fmtN(Math.abs(mr), 1); $("#r4").textContent = Lib.fmtN(ped, 2);
  $("#v3").textContent = Math.abs(q - 10) < 0.01 ? "MR = 0, PED = 1 and TR is at its maximum ($100)." : q < 10 ? "MR is positive and demand is elastic (PED > 1): selling more raises TR." : "MR is negative and demand is inelastic (PED < 1): selling more lowers TR.";
  const F = frame(480, 360, 50, 460, 20, 320, 20, -20, 20);
  let s = axes(F, "Quantity (Q)", "Price, AR, MR ($)", 0);
  s += SV.rect(F.X(0), F.Y(P), F.X(q) - F.X(0), F.Y(0) - F.Y(P), "f1");
  s += SV.line(F.X(0), F.Y(20), F.X(20), F.Y(0), "c1") + SV.text(F.X(19.5), F.Y(1) + 18, "AR = D", "lbl bd t1", { "text-anchor": "end" });
  s += SV.line(F.X(0), F.Y(20), F.X(20), F.Y(-20), "c2") + SV.text(F.X(19.5), F.Y(-18), "MR", "lbl bd t2", { "text-anchor": "end" });
  s += SV.line(F.X(q), F.Y(Math.min(P, mr)), F.X(q), F.Y(0), "gr") + SV.circle(F.X(q), F.Y(P), 6, "dot1") + SV.circle(F.X(q), F.Y(mr), 6, "dot2");
  s += SV.text(F.X(q / 2), (F.Y(P) + F.Y(0)) / 2 + 4, "TR = " + Lib.fmtN(tr, 0), "lbl bd t1", { "text-anchor": "middle" });
  $("#lab3").innerHTML = s;
} });

/* ---------- Lab 4: profit types for a price taker ---------- */
Lib.slider($("#sl5"), { id: "a5", label: "Market price (P = MR = AR)", min: 3, max: 24, step: 0.2, value: 16, fmt: (v) => "$" + v.toFixed(1), onInput: (P) => {
  const F = frame(480, 360, 50, 460, 20, 320, 5.5, 0, 40), shut = P < 6, q = shut ? 0 : 2 + Math.sqrt((P - 3) / 3);
  let s = axes(F, "Output (Q)", "Cost / revenue per unit ($)") + costSet(F, 20, { a: 0 }) + SV.line(F.l, F.Y(P), F.r, F.Y(P), "c4") + SV.text(F.r - 4, F.Y(P) - 8, "P = AR = MR", "lbl bd t4", { "text-anchor": "end" });
  if (shut) {
    $("#p1").textContent = "0"; $("#p2").textContent = "–"; $("#p3").textContent = "–"; $("#p4").textContent = "–$20";
    $("#v4").textContent = "Price is below the lowest AVC ($6). The firm cannot even cover its variable costs, so it is likely to shut down in the short run and lose only its fixed costs.";
  } else {
    const atc = ATC(q), u = P - atc, tp = u * q;
    $("#p1").textContent = Lib.fmtN(q, 2); $("#p2").textContent = "$" + Lib.fmtN(atc, 2); $("#p3").textContent = (u < 0 ? "−$" : "$") + Lib.fmtN(Math.abs(u), 2); $("#p4").textContent = (tp < 0 ? "−$" : "$") + Lib.fmtN(Math.abs(tp), 1);
    s += SV.rect(F.X(0), Math.min(F.Y(P), F.Y(atc)), F.X(q) - F.X(0), Math.abs(F.Y(P) - F.Y(atc)), u >= 0 ? "f3" : "f2") + SV.circle(F.X(q), F.Y(P), 6, "dot4");
    $("#v4").textContent = Math.abs(u) < 0.15 ? "P is about equal to ATC: the firm earns normal profit. TR covers all costs, including the entrepreneur's opportunity cost." : u > 0 ? "P is above ATC: supernormal profit. This is a signal that could attract new firms into the industry." : "P is below ATC but above AVC: subnormal profit. The firm covers its variable costs, so it may stay in the short run, but it is likely to leave in the long run.";
  }
  $("#lab4").innerHTML = s;
} });

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Total revenue", "Price × quantity sold"],
  ["Average revenue", "Total revenue ÷ quantity, equal to the price"],
  ["Marginal revenue", "The extra revenue from selling one more unit"],
  ["Price taker", "A firm facing a horizontal demand curve that must accept the market price"],
  ["Normal profit", "The minimum return needed to keep the firm in the industry, included in total cost"],
  ["Supernormal profit", "Profit above normal profit: TR greater than TC"],
  ["Subnormal profit", "Profit below normal profit: TR less than TC"],
], done: "Seven terms for revenue and profit." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm sells 300 units at $12 each. What is its total revenue?", a: 3600, unit: "$", hint: "TR = P × Q.", sol: "TR = 12 × 300 = $3,600." },
  { q: "TR is $5,000 and TC (including normal profit) is $4,200. How much supernormal profit does the firm earn?", a: 800, unit: "$", hint: "Supernormal profit = TR − TC.", sol: "$5,000 − $4,200 = $800." },
  { q: "Demand is P = 20 − Q. What is marginal revenue at Q = 6 (MR = 20 − 2Q)?", a: 8, sol: "20 − 2 × 6 = <b>$8</b>." },
  { q: "At what output is total revenue greatest for P = 20 − Q?", a: 10, sol: "MR = 20 − 2Q = 0 gives Q = <b>10</b>." },
  { q: "A firm sells 400 units at $9.50 each and total cost (including normal profit) is $3,600. What is its supernormal profit ($)?", a: 200, sol: "TR = 3,800; 3,800 − 3,600 = <b>$200</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement about a firm earning normal profit is correct?", opts: ["Total revenue is below total cost", "Total revenue equals total cost, which includes normal profit", "The firm is making an accounting loss", "The firm will leave the industry"], a: 1, why: "Normal profit is the opportunity cost of enterprise and is already included in total cost, so TR = TC." },
  { q: "A price maker's marginal revenue is zero when", opts: ["price equals average cost", "PED = 1 and total revenue is at its maximum", "demand is perfectly elastic", "the firm earns normal profit"], a: 1, why: "MR = 0 where AR is at the midpoint of a straight-line demand curve: PED = 1, and TR is at its maximum." },
  { q: "Total revenue is $4,500 and total cost, including normal profit, is $5,200. The firm earns:", opts: ["supernormal profit", "normal profit", "subnormal profit", "zero total revenue"], a: 2, why: "Revenue is less than total cost, which already includes normal profit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Marginal revenue", "The extra revenue from selling one more unit."],
  ["Price taker", "A firm that faces a horizontal demand curve and must accept the market price."],
  ["Normal profit", "The minimum return needed to keep the entrepreneur in the industry, included in total cost."],
  ["Supernormal profit", "Profit above normal profit, when TR is greater than TC."],
  ["Subnormal profit", "Profit below normal profit, when TR is less than TC."],
] });

/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
  { id: "pr6", title: "6 · Average and marginal revenue", ctx: "Sketch a downward-sloping AR curve with its MR curve below it, marking the point where MR = 0.", ask: "Explain the relationship between MR = 0, PED = 1 and total revenue at that point. Apply it: for a real product, would cutting the price raise or lower total revenue right now, and what would you need to know to answer?" },
  { id: "pr7", title: "7 · Normal, subnormal and supernormal profit", ctx: "No chart needed: write TR and TC for three imagined scenarios, one earning normal profit, one supernormal and one subnormal.", ask: "Explain, using your own numbers, why normal profit is included in total costs rather than sitting on top of them. Apply it: describe a real or plausible business earning subnormal profit and say what you would expect to happen to it over the next few years." },
];
PROMPTS.forEach((p) => {
  const card = document.createElement("div");
  card.className = "prompt-card";
  card.innerHTML = `<h3>${p.title}</h3><p class="ctx">${p.ctx}</p><div class="draw-box">sketch your diagram here (on paper or in your notebook)</div><label for="${p.id}">Explain and apply</label><textarea id="${p.id}" placeholder="${p.ask.replace(/"/g, "&quot;")}"></textarea>`;
  $("#promptList").appendChild(card);
  const ta = $("#" + p.id);
  try { const saved = localStorage.getItem("firm-focus-" + p.id); if (saved) ta.value = saved; } catch (e) {}
  ta.addEventListener("input", () => { try { localStorage.setItem("firm-focus-" + p.id, ta.value); } catch (e) {} });
});
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2020 (not sat) · 32 · Q8] At which level of output will a firm achieve the aim of sales maximisation?", opts: ["where AC = AR", "where AC = MC", "where MC = AR", "where MR = zero"], a: 0, why: "Sales maximisation subject to a minimum profit is at AR = AC, where only normal profit is earned. MR = 0 is revenue maximisation." },
  { q: "[Feb/March 2025 · 32 · Q7] A profit-maximising monopoly makes an abnormal profit and decides to reinvest some of this profit to improve its capital stock. What are the most likely outcomes from this change? (allocative, dynamic, productive efficiency)", opts: ["improves, improves, improves", "unchanged, improves, improves", "improves, unchanged, unchanged", "unchanged, unchanged, improves"], a: 1, why: "Investing improves capital and lowers costs over time (dynamic and productive efficiency), but price is still above marginal cost, so allocative efficiency is unchanged." },
  { q: "[Feb/March 2023 · 32 · Q6] What is achieved in monopolistic competition in the long run? (allocative efficiency, supernormal profit)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 0, why: "Entry removes supernormal profit in the long run, but price stays above marginal cost, so there is no allocative efficiency." },
] });
