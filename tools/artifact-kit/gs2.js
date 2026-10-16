/* ---------- LRAC geometry: AC(q) = 6 + 0.0008 (q - 100)^2, minimum efficient scale at q = 100 ---------- */
const MES = 100, AMIN = 6;
const AC = (q) => AMIN + 0.0008 * (q - MES) ** 2;
const CX = (q) => 70 + q * 3.1, CY = (c) => 320 - c * 17;
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
function cAxes() {
  return SV.line(70, 320, 700, 320) + SV.line(70, 320, 70, 40) + SV.text(700, 348, "Output (units per month)", "sm", { "text-anchor": "end" }) + SV.text(76, 40, "Long-run average cost ($)", "sm");
}
function curve(frac) {
  const pts = [];
  for (let q = 0; q <= 200 * frac + 0.01; q += 4) pts.push([CX(q), CY(AC(q))]);
  return pts.length > 1 ? SV.path(Lib.ptsPath(pts), "c1") : "";
}

/* ---------- Learn: static picture ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 370" role="img" aria-label="U-shaped long-run average cost curve showing economies of scale, the minimum efficient scale and diseconomies of scale">${cAxes()}
  ${SV.poly([[CX(0), 40], [CX(98), 40], [CX(98), 320], [CX(0), 320]], "f3")}${SV.poly([[CX(102), 40], [CX(200), 40], [CX(200), 320], [CX(102), 320]], "f2")}
  ${curve(1)}${SV.text(CX(200) - 4, CY(AC(200)) - 8, "LRAC", "lbl bd t1", { "text-anchor": "end" })}
  ${SV.line(CX(100), CY(6), CX(100), 320, "gr")}${SV.line(70, CY(6), CX(100), CY(6), "gr")}${SV.circle(CX(100), CY(6), 6, "dot3")}
  ${SV.text(CX(100), 342, "MES", "lbl bd", { "text-anchor": "middle" })}${SV.text(62, CY(6) + 4, "lowest cost", "sm", { "text-anchor": "end" })}
  ${SV.text(CX(45), 90, "ECONOMIES OF SCALE", "lbl bd t3", { "text-anchor": "middle" })}${SV.text(CX(45), 110, "LRAC falls as output rises", "sm", { "text-anchor": "middle" })}
  ${SV.text(CX(150), 90, "DISECONOMIES OF SCALE", "lbl bd t2", { "text-anchor": "middle" })}${SV.text(CX(150), 110, "LRAC rises as output rises", "sm", { "text-anchor": "middle" })}
  </svg>`;

/* ---------- Watch 1: build the LRAC curve ---------- */
function buildLRAC(s) {
  let o = cAxes();
  if (s.e > 0) o += SV.poly([[CX(0), 40], [CX(98), 40], [CX(98), 320], [CX(0), 320]], "f3", op(s.e)) + SV.text(CX(45), 90, "ECONOMIES OF SCALE", "lbl bd t3", { "text-anchor": "middle", ...op(s.e) });
  if (s.d > 0) o += SV.poly([[CX(102), 40], [CX(200), 40], [CX(200), 320], [CX(102), 320]], "f2", op(s.d)) + SV.text(CX(150), 90, "DISECONOMIES OF SCALE", "lbl bd t2", { "text-anchor": "middle", ...op(s.d) });
  o += curve(s.cv);
  if (s.m > 0) o += SV.line(CX(100), CY(6), CX(100), 320, "gr", op(s.m)) + SV.line(70, CY(6), CX(100), CY(6), "gr", op(s.m)) + SV.circle(CX(100), CY(6), 6, "dot3", op(s.m)) + SV.text(CX(100), 342, "MES", "lbl bd", { "text-anchor": "middle", ...op(s.m) }) + SV.text(CX(100) + 12, CY(6) + 34, "Minimum efficient scale: lowest LRAC", "lbl bd t3", op(s.m));
  if (s.x > 0) {
    const a = AC(30), b = AC(100);
    o += SV.circle(CX(30), CY(a), 6, "dot2", op(s.x)) + SV.text(CX(30) + 10, CY(a) - 8, "small firm: $" + Lib.fmtN(a, 2), "lbl bd t2", op(s.x));
    o += SV.line(CX(30), CY(a), CX(30), CY(b), "c2", { "stroke-width": 3, ...op(s.x) }) + SV.text(CX(30) + 10, CY(b) + 34, "extra cost per unit: $" + Lib.fmtN(a - b, 2), "sm bd t2", op(s.x));
  }
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 380, label: "Building the long-run average cost curve with economies of scale, the minimum efficient scale and diseconomies of scale", base: { cv: 0, e: 0, d: 0, m: 0, x: 0 }, draw: buildLRAC, tween: 1100, dwell: 5200, steps: [
  { cap: "<b>Start small.</b> A firm with low output has a high average cost per unit. The fixed costs are spread over only a few units.", s: { cv: 0.12 } },
  { cap: "<b>Economies of scale.</b> As output grows, LRAC <b>falls</b>: bulk buying, specialist workers and machines, cheaper loans, and fixed costs spread over more units.", s: { cv: 0.5, e: 1 } },
  { cap: "<b>Minimum efficient scale (MES).</b> At about 100 units LRAC reaches its <b>lowest point</b>. This is the smallest output at which the firm has used up all the economies of scale.", s: { cv: 0.5, e: 1, m: 1 } },
  { cap: "<b>Diseconomies of scale.</b> Beyond MES, LRAC <b>rises</b>: communication gets harder, coordination is slow, workers feel less motivated and layers of management add cost.", s: { cv: 1, e: 1, m: 1, d: 1 } },
  { cap: "<b>Why it matters for survival.</b> A firm making only 30 units has a unit cost well above the MES firm. It needs a <b>niche, higher prices or support</b> to survive. If the MES is small compared with the market, many firms reach low cost, so small firms are common.", s: { cv: 1, e: 1, m: 1, d: 1, x: 1 } },
] });

/* ---------- Lab 1: where on the LRAC? ---------- */
function lab1() {
  if (!$("#q1")) return;
  const q = +$("#q1").value, ac = AC(q), over = Math.round((ac / AMIN - 1) * 100);
  const zone = q < 96 ? "Economies of scale" : q <= 104 ? "At MES" : "Diseconomies";
  $("#r1").textContent = "$" + Lib.fmtN(ac, 2); $("#r2").textContent = over + "%"; $("#r3").textContent = zone;
  $("#rv").textContent = q < 96 ? `At ${q} units the firm is below the minimum efficient scale. Growing would cut average cost, so there is a reason to expand.`
    : q <= 104 ? "The firm is at (or very near) the lowest possible cost. Growing further would not cut cost any more."
    : `At ${q} units the firm has grown beyond MES. Average cost has started to rise because of diseconomies of scale, so more growth could raise cost per unit.`;
  const X = (v) => 50 + v * 1.75, Y = (c) => 250 - c * 14;
  const pts = []; for (let v = 0; v <= 200; v += 4) pts.push([X(v), Y(AC(v))]);
  $("#labA").innerHTML = SV.line(50, 250, 410, 250) + SV.line(50, 250, 50, 20) + SV.text(406, 272, "Output", "sm", { "text-anchor": "end" }) + SV.text(56, 24, "LRAC ($)", "sm") +
    SV.path(Lib.ptsPath(pts), "c1") + SV.line(X(q), Y(ac), X(q), 250, "gr") + SV.line(50, Y(ac), X(q), Y(ac), "gr") + SV.circle(X(q), Y(ac), 7, q < 96 ? "dot3" : q <= 104 ? "dot1" : "dot2") +
    SV.text(X(100), 268, "MES", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "q1", label: "Firm's output (units): ", min: 10, max: 200, step: 5, value: 40, fmt: (v) => v, onInput: lab1 });

/* ---------- Lab 2: how many firms fit at MES ---------- */
function lab2() {
  if (!$("#m2")) return;
  const mes = +$("#m2").value, n = Math.floor(100 / mes);
  const st = n >= 20 ? "Many firms (competitive or monopolistic competition)" : n >= 5 ? "Several firms (oligopoly, fairly many)" : n >= 3 ? "Few firms (oligopoly)" : n === 2 ? "Duopoly: two firms" : "One firm: natural monopoly";
  $("#s1").textContent = n; $("#s2").textContent = st.split(" (")[0];
  $("#sv").textContent = n >= 20 ? `MES is only ${mes}% of the market, so ${n} firms can all reach the lowest cost. Small firms can survive, and the market is likely to be competitive.`
    : n >= 3 ? `MES is ${mes}% of the market, so only about ${n} firms can reach the lowest cost. A firm much smaller than MES is likely to have higher cost, so small firms struggle unless they have a niche.`
    : n === 2 ? `MES is ${mes}% of the market. The market only has room for two firms at the lowest cost.` : `MES is ${mes}% of the market. One firm can serve the whole market at the lowest cost: a natural monopoly.`;
  const W = 340, x0 = 40, shown = Math.min(n, 50), w = (W * mes) / 100;
  let o = SV.text(x0, 40, "The whole market = 100%", "lbl bd") + SV.rect(x0, 60, W, 60, "ax", { fill: "none" });
  for (let i = 0; i < shown; i++) o += SV.rect(x0 + i * w, 60, w, 60, i % 2 ? "f1" : "f3", { stroke: "var(--surface)", "stroke-width": 1 });
  if (n > 50) o += SV.text(x0, 150, "(first 50 firms drawn)", "sm");
  o += SV.text(x0, 150, `Each block = one firm at minimum efficient scale (${mes}% of the market)`, "sm") + SV.text(x0, 180, `${n} firm${n > 1 ? "s" : ""} fit${n > 1 ? "" : "s"}`, "lbl bd t1");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "m2", label: "Minimum efficient scale as a % of the market: ", min: 2, max: 100, step: 1, value: 10, fmt: (v) => v + "%", onInput: lab2 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each cause an economy or a diseconomy of scale?",
  buckets: [{ label: "Economy of scale" }, { label: "Diseconomy of scale" }],
  items: [
    { text: "Bulk-buying discounts from suppliers", b: 0 }, { text: "Cheaper borrowing for a large firm", b: 0 }, { text: "Specialist managers become affordable", b: 0 }, { text: "Larger machines cut cost per unit", b: 0 }, { text: "Advertising costs spread over more units", b: 0 },
    { text: "Decisions slow down as layers of management grow", b: 1 }, { text: "Workers feel less motivated in a very large firm", b: 1 }, { text: "Communication between divisions becomes poor", b: 1 }, { text: "Difficulty coordinating many sites", b: 1 },
  ], done: "Economies lower unit cost as output grows; diseconomies raise it beyond MES.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Long-run average cost", "Cost per unit when all inputs can be changed"],
  ["Economies of scale", "A fall in LRAC as output rises"],
  ["Diseconomies of scale", "A rise in LRAC as output rises beyond MES"],
  ["Minimum efficient scale", "The smallest output at which LRAC is lowest"],
  ["Internal economies", "Savings that come from the size of the firm itself"],
  ["External economies", "Savings that come from the growth of the whole industry"],
  ["Barrier to entry", "Something that makes it hard for new firms to join a market"],
], done: "Seven words for costs and size." });
Lib.calc($("#c1"), { qs: [
  { q: "Before a takeover a firm makes 40,000 units at a total cost of $120,000. After it makes 100,000 units at a total cost of $270,000. By what percentage does average cost fall?", a: 10, hint: "Average cost = total cost ÷ output, before and after.", sol: "Before: 120,000 ÷ 40,000 = $3.00. After: 270,000 ÷ 100,000 = $2.70. Fall = 0.30 ÷ 3.00 × 100 = <b>10%</b>." },
  { q: "The minimum efficient scale is 5% of the market. Roughly how many firms can reach MES?", a: 20, sol: "100 ÷ 5 = <b>20</b>. With so many firms, the market is likely to be competitive and small firms can survive." },
  { q: "A firm produces 100 units at a total cost of $1,000, then 200 units at a total cost of $1,600. What is the average cost at 200 units ($)?", a: 8, sol: "1,600 ÷ 200 = <b>$8</b>, down from $10: economies of scale." },
  { q: "MES is 20% of the market. About how many firms can reach MES?", a: 5, sol: "100 ÷ 20 = <b>5</b> firms." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Beyond the minimum efficient scale, a firm is most likely to experience:", opts: ["falling LRAC", "diseconomies of scale", "perfect competition", "constant returns forever"], a: 1, why: "Past MES, LRAC rises because of communication and coordination problems." },
  { q: "Falling long-run average cost as output rises shows:", opts: ["diseconomies of scale", "economies of scale", "constant returns", "a barrier to entry"], a: 1, why: "Economies of scale are falls in LRAC as output rises." },
  { q: "Which is a technical economy of scale?", opts: ["A bulk discount on materials", "A larger, more efficient machine", "Cheaper loans", "Advertising spread over more output"], a: 1, why: "Technical economies come from the production process and equipment." },
  { q: "If the minimum efficient scale is a small share of the market:", opts: ["only a few firms can reach it", "many firms can reach it", "no firm can survive", "all firms are monopolies"], a: 1, why: "A small MES leaves room for many firms operating at the lowest cost." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Minimum efficient scale", "The smallest output at which long-run average cost is at its lowest."],
  ["Economies of scale", "A fall in long-run average cost as output rises."],
  ["Diseconomies of scale", "A rise in long-run average cost as output rises beyond MES."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2022 · 33 · Q8] The manufacture of some sports equipment is dominated by very large firms but there are also smaller firms in the industry. What enables a small firm to exist in such an industry?", opts: ["high concentration ratio that reduces competition", "high start-up costs that occur in a contestable market", "decreasing average cost as a large firm expands", "a requirement for personalised equipment"], a: 3, why: "A niche for personalised products lets small firms survive. B and C describe conditions that favour big firms." },
  { q: "[Feb/March 2020 · 32 · Q10] What is true about economies of scale but not diseconomies of scale?", opts: ["They occur because average revenue is increasing.", "They occur because of management policy changes.", "They occur in the short run.", "They occur with decreasing average cost."], a: 3, why: "Economies of scale are falling average cost as output rises; diseconomies are rising average cost." },
  { q: "[May/June 2023 · 31 · Q4] Which type of efficiency is shown by the shift from long-run average cost curve 1 (LRAC1) to long-run average cost curve 2 (LRAC2), where LRAC2 is below LRAC1?", opts: ["allocative", "dynamic", "Pareto", "productive"], a: 1, why: "A downward shift of the LRAC curve over time shows dynamic efficiency." },
  { q: "[May/June 2022 · 31 · Q8] Firms often remain small even when growth could result in technical economies of scale. What is not a likely reason for this?", opts: ["Demand for the product tends to change often and rapidly.", "Individual entrepreneurs wish to keep a tight personal control over their own firm.", "The entrepreneurs who establish the firms tend to be ambitious risk-takers.", "The market in which they operate is very specialised in nature, often selling unique products."], a: 2, why: "Ambitious risk-takers would be expected to grow their firms, so this is not a reason for staying small." },
] });
