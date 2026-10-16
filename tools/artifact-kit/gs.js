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

/* ---------- Watch 2: types of integration ---------- */
function box(x, y, w, h, label, o = {}) {
  return SV.rect(x, y, w, h, "ax", { rx: 10, fill: "none", ...(o.op !== undefined ? op(o.op) : {}) }) + SV.text(x + w / 2, y + h / 2 + 5, label, "lbl bd", { "text-anchor": "middle", ...(o.op !== undefined ? op(o.op) : {}) });
}
function arrow(x1, y1, x2, y2, c, o) {
  const ang = Math.atan2(y2 - y1, x2 - x1), hx = x2, hy = y2, k = 11, p = 6;
  const ux = Math.cos(ang), uy = Math.sin(ang);
  return SV.line(x1, y1, x2 - ux * k, y2 - uy * k, c, o) + `<polygon points="${hx},${hy} ${hx - ux * k - uy * p},${hy - uy * k + ux * p} ${hx - ux * k + uy * p},${hy - uy * k - ux * p}" class="${c === "ax" ? "arr" : c.replace("c", "t")}"${at(o)}/>`;
}
const IB = { farm: [20, 150], mill: [170, 150], bak: [320, 150], shop: [470, 150], cust: [620, 150], rival: [320, 280], toy: [560, 280], branch: [320, 20] }, IW = 110, IH = 60;
function integ(s) {
  let o = "";
  const fill = (k, cl, v) => v > 0 ? SV.rect(IB[k][0], IB[k][1], IW, IH, cl, { rx: 10, ...op(v) }) : "";
  o += fill("rival", "f1", s.h) + fill("mill", "f4", s.b) + fill("shop", "f3", s.f) + fill("toy", "f2", s.c) + fill("branch", "f1", s.o);
  o += SV.rect(IB.bak[0], IB.bak[1], IW, IH, "f1", { rx: 10, opacity: 0.55 });
  o += box(...IB.farm, IW, IH, "Farm") + box(...IB.mill, IW, IH, "Flour mill") + box(...IB.bak, IW, IH, "Bakery X") + box(...IB.shop, IW, IH, "Shops") + box(...IB.cust, IW, IH, "Customers");
  o += box(IB.rival[0], IB.rival[1], IW, IH, "Rival bakery", { op: 0.35 + 0.65 * s.h }) + box(IB.toy[0], IB.toy[1], IW, IH, "Toy maker", { op: 0.35 + 0.65 * s.c }) + box(IB.branch[0], IB.branch[1], IW, IH, "New branch", { op: Math.max(0, s.o) });
  [["farm", "mill"], ["mill", "bak"], ["bak", "shop"], ["shop", "cust"]].forEach(([a, b]) => { o += arrow(IB[a][0] + IW + 2, 180, IB[b][0] - 2, 180, "ax"); });
  o += SV.text(380, 130, "supply chain flows left to right", "sm", { "text-anchor": "middle" });
  if (s.h > 0) o += arrow(375, 213, 375, 278, "c1", op(s.h)) + SV.text(385, 250, "HORIZONTAL: same stage", "lbl bd t1", op(s.h));
  if (s.b > 0) o += arrow(318, 168, 284, 168, "c4", op(s.b)) + SV.text(225, 252, "BACKWARD: buys its supplier", "lbl bd t4", { "text-anchor": "middle", ...op(s.b) }) + SV.text(225, 270, "(earlier in the chain)", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.f > 0) o += arrow(432, 168, 468, 168, "c3", op(s.f)) + SV.text(525, 252, "FORWARD: buys its seller", "lbl bd t3", { "text-anchor": "middle", ...op(s.f) }) + SV.text(525, 270, "(later in the chain)", "sm", { "text-anchor": "middle", ...op(s.f) });
  if (s.c > 0) o += arrow(430, 205, 568, 284, "c2", op(s.c)) + SV.text(620, 360, "CONGLOMERATE: unrelated industry", "lbl bd t2", { "text-anchor": "middle", ...op(s.c) });
  if (s.o > 0) o += arrow(375, 148, 375, 84, "c1", op(s.o)) + SV.text(495, 55, "ORGANIC: built from own profit", "lbl bd t1", op(s.o));
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 380, label: "A supply chain with a bakery in the middle, showing horizontal, backward, forward and conglomerate integration and organic growth", base: { h: 0, b: 0, f: 0, c: 0, o: 0 }, draw: integ, tween: 800, dwell: 5200, steps: [
  { cap: "<b>The supply chain.</b> A farm grows wheat, a mill makes flour, <b>Bakery X</b> makes bread, shops sell it. Other bakeries compete with X.", s: {} },
  { cap: "<b>Horizontal integration.</b> X takes over a <b>rival bakery</b>: same industry, same stage. Possible gains: economies of scale and less competition. Possible harm: market power.", s: { h: 1 } },
  { cap: "<b>Backward vertical integration.</b> X buys the <b>mill that supplies it</b>. It secures supply and may cut a supplier mark-up.", s: { b: 1 } },
  { cap: "<b>Forward vertical integration.</b> X buys the <b>shops that sell its bread</b>. It secures outlets and keeps the retail margin.", s: { f: 1 } },
  { cap: "<b>Conglomerate integration.</b> X buys a <b>toy maker</b>. Unrelated industry, so risk is spread: a fall in demand for bread does not hit toys.", s: { c: 1 } },
  { cap: "<b>Organic growth.</b> No other firm is bought. X uses <b>its own profit</b> to open a new branch. Slower, but X keeps control and its culture.", s: { o: 1 } },
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

/* ---------- Lab 3: can the small firm survive ---------- */
function lab3() {
  if (!$("#sf1") || !$("#sf2")) return;
  const f = +$("#sf1").value / 100, prem = +$("#sf2").value, cost = AMIN + 4 * (1 - f) ** 2, pen = Math.round((cost / AMIN - 1) * 100), price = AMIN * (1 + prem / 100), ok = prem >= pen;
  $("#t1").textContent = "+" + pen + "%"; $("#t2").textContent = "+" + prem + "%"; $("#t3").textContent = ok ? "Survives" : "Squeezed";
  $("#tv").textContent = ok ? `The small firm's unit cost is ${pen}% above the big firm's. Customers pay ${prem}% more for its service or product, which covers the gap. It can earn at least normal profit.`
    : `The small firm's unit cost is ${pen}% higher than the big firm's but customers only pay ${prem}% more. The firm makes a loss on each unit. It needs a bigger premium, a bigger scale, or lower costs.`;
  const Y = (v) => 210 - v * 20, bw = 70;
  const bars = [[40, 6, "f1", "Big firm cost", "$6.00"], [150, cost, "f2", "Small firm cost", "$" + Lib.fmtN(cost, 2)], [260, price, ok ? "f3" : "f4", "Small firm price", "$" + Lib.fmtN(price, 2)]];
  let o = SV.line(30, 210, 400, 210) + SV.text(32, 24, "$ per unit", "sm");
  bars.forEach(([x, v, c, l, t]) => { o += SV.rect(x, Y(v), bw, 210 - Y(v), c) + SV.text(x + bw / 2, Y(v) - 6, t, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 228, l, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o;
}
Lib.slider($("#g3"), { id: "sf1", label: "Small firm's output as a % of MES: ", min: 10, max: 100, step: 5, value: 30, fmt: (v) => v + "%", onInput: lab3 });
Lib.slider($("#g4"), { id: "sf2", label: "Extra price customers will pay for service or niche: ", min: 0, max: 60, step: 1, value: 20, fmt: (v) => v + "%", onInput: lab3 });

/* ---------- Lab 4: takeover and the consumer ---------- */
function lab4() {
  if (!$("#tk1") || !$("#tk2") || !$("#tk3")) return;
  const s = +$("#tk1").value, pass = +$("#tk2").value, rise = +$("#tk3").value;
  const saving = 8 * s / 100, c1 = 8 - saving, p1 = 10 * (1 + rise / 100) - (pass / 100) * saving, pr = p1 - c1;
  $("#u1").textContent = "$" + Lib.fmtN(c1, 2); $("#u2").textContent = "$" + Lib.fmtN(p1, 2); $("#u3").textContent = "$" + Lib.fmtN(pr, 2);
  const d = p1 - 10;
  $("#uv").textContent = d < -0.005 ? `Price falls by $${Lib.fmtN(-d, 2)}. Consumers gain, and the firm's profit per unit rises from $2.00 to $${Lib.fmtN(pr, 2)}.`
    : d > 0.005 ? `Price rises by $${Lib.fmtN(d, 2)}. Market power outweighs the cost saving, so consumers are worse off while the firm's profit per unit is $${Lib.fmtN(pr, 2)}.`
    : `Price is unchanged. The firm keeps the whole saving as extra profit ($${Lib.fmtN(pr, 2)} a unit).`;
  const Y = (v) => 220 - v * 16, bw = 60;
  const bars = [[30, 10, "f1", "Price before", "$10.00"], [110, 8, "f2", "Cost before", "$8.00"], [220, p1, "f1", "Price after", "$" + Lib.fmtN(p1, 2)], [300, c1, "f3", "Cost after", "$" + Lib.fmtN(c1, 2)]];
  let o = SV.line(20, 220, 400, 220) + SV.text(24, 24, "$ per unit", "sm");
  bars.forEach(([x, v, c, l, t]) => { o += SV.rect(x, Y(v), bw, 220 - Y(v), c) + SV.text(x + bw / 2, Y(v) - 6, t, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g5"), { id: "tk1", label: "Cost saving from economies of scale: ", min: 0, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: lab4 });
Lib.slider($("#g6"), { id: "tk2", label: "Share of the saving passed on to consumers: ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v + "%", onInput: lab4 });
Lib.slider($("#g7"), { id: "tk3", label: "Price rise caused by greater market power: ", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v + "%", onInput: lab4 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Put each takeover or merger in the right bucket.",
  buckets: [{ label: "Horizontal" }, { label: "Backward vertical" }, { label: "Forward vertical" }, { label: "Conglomerate" }],
  items: [
    { text: "A supermarket chain buys a rival supermarket chain", b: 0 }, { text: "Two banks merge", b: 0 },
    { text: "A bakery buys a flour mill", b: 1 }, { text: "A steel maker buys an iron-ore mine", b: 1 }, { text: "A phone maker buys a company that designs its chips", b: 1 },
    { text: "A car maker buys a chain of showrooms", b: 2 }, { text: "A brewery buys pubs", b: 2 }, { text: "A film studio buys a cinema chain", b: 2 },
    { text: "A mobile phone company buys a chocolate maker", b: 3 }, { text: "A tobacco company buys a snack-food company", b: 3 },
  ], done: "Test: who supplies whom? The supplier is backward, the seller is forward, the same stage is horizontal, and unrelated is conglomerate.",
});
Lib.classify($("#cl2"), {
  prompt: "Does each item help a small firm survive, or threaten it?",
  buckets: [{ label: "Helps survival" }, { label: "Threat" }],
  items: [
    { text: "Customers value personal service", b: 0 }, { text: "A niche market that big firms ignore", b: 0 }, { text: "Minimum efficient scale is small compared with the market", b: 0 },
    { text: "Quick decisions and flexibility", b: 0 }, { text: "Government grants and cheaper loans for start-ups", b: 0 }, { text: "Local knowledge and loyal customers", b: 0 },
    { text: "Large rivals with economies of scale cut prices", b: 1 }, { text: "Banks refuse to lend or charge high interest", b: 1 }, { text: "Low barriers to entry bring new rivals", b: 1 },
    { text: "New regulation with a fixed compliance cost", b: 1 }, { text: "Customers move to cheap standard products", b: 1 },
  ], done: "Many small firms win on something other than cost.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Organic growth", "Growth from the firm's own resources and investment"],
  ["Merger", "Two firms agree to join and form one new company"],
  ["Takeover", "One firm buys another, usually by buying its shares"],
  ["Demerger", "A firm splits into separate businesses"],
  ["Diversification", "Moving into different products or markets to spread risk"],
  ["Minimum efficient scale", "The smallest output at which LRAC is at its lowest"],
  ["Diseconomies of scale", "LRAC rises as the firm gets too big"],
  ["Concentration ratio", "The share of the market held by the largest few firms"],
], done: "These eight terms cover most of the chapter." });
Lib.order($("#o1"), { prompt: "Put the explanation of how a takeover could lead to lower prices in the best order.", items: [
  "A firm takes over a rival in the same industry (horizontal integration)",
  "Output is combined, so the firm produces on a larger scale",
  "Economies of scale such as bulk buying lower the average cost per unit",
  "Competition from other firms still forces the firm to pass the saving on",
  "The price charged to consumers could fall",
  "Evaluate: if competition falls instead, the firm may keep the saving or raise prices",
], done: "This is the chain of reasoning behind a strong 20-mark answer." });
Lib.calc($("#c1"), { qs: [
  { q: "Two firms have market shares of 18% and 12%. They merge. What is the combined market share (%)?", a: 30, sol: "18 + 12 = <b>30%</b>." },
  { q: "The four largest firms have shares of 30%, 25%, 15% and 10%. What is the four-firm concentration ratio (%)?", a: 80, sol: "30 + 25 + 15 + 10 = <b>80%</b>." },
  { q: "Before a takeover a firm makes 40,000 units at a total cost of $120,000. After it makes 100,000 units at a total cost of $270,000. By what percentage does average cost fall?", a: 10, hint: "Average cost = total cost ÷ output, before and after.", sol: "Before: 120,000 ÷ 40,000 = $3.00. After: 270,000 ÷ 100,000 = $2.70. Fall = 0.30 ÷ 3.00 × 100 = <b>10%</b>." },
  { q: "A company has 10 million shares priced at $5. A bidder offers a 40% premium. What is the total value of the bid ($ million)?", a: 70, sol: "Offer per share = 5 × 1.4 = $7. Total = 10 million × $7 = <b>$70 million</b>." },
  { q: "A firm's sales rise from $20 million to $23 million through organic growth. What is the growth rate (%)?", a: 15, sol: "(23 − 20) ÷ 20 × 100 = <b>15%</b>." },
  { q: "The minimum efficient scale is 5% of the market. Roughly how many firms can reach MES?", a: 20, sol: "100 ÷ 5 = <b>20</b>. With so many firms, the market is likely to be competitive and small firms can survive." },
  { q: "A takeover cuts a firm's unit cost from $8 to $7. The firm passes on half of the saving and prices were $10. What is the new price ($)?", a: 9.5, sol: "Saving = $1. Half passed on = $0.50. New price = 10 − 0.50 = <b>$9.50</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is organic growth?", opts: ["A firm buys a rival", "A firm merges with a supplier", "A firm opens new outlets using its own retained profit", "A firm is taken over"], a: 2, why: "Organic (internal) growth uses the firm's own resources. The others are external growth." },
  { q: "A clothing retailer buys a textile factory that supplies its cloth. This is:", opts: ["horizontal integration", "backward vertical integration", "forward vertical integration", "conglomerate integration"], a: 1, why: "The factory is earlier in the chain: it supplies the retailer." },
  { q: "Which is most likely to be a benefit of a merger for consumers?", opts: ["Fewer firms to choose from", "Economies of scale passed on in lower prices", "Greater X-inefficiency", "Higher barriers to entry"], a: 1, why: "Lower costs from scale could lead to lower prices if competition forces the saving to be passed on." },
  { q: "Beyond the minimum efficient scale, a firm is most likely to experience:", opts: ["falling LRAC", "diseconomies of scale", "perfect competition", "constant returns forever"], a: 1, why: "Past MES, LRAC rises because of communication and coordination problems." },
  { q: "Which makes the survival of small firms more likely?", opts: ["A large minimum efficient scale", "Customers valuing personalised service", "Large rivals' price cuts", "Banks refusing loans"], a: 1, why: "Customers who value service may pay a higher price. The others harm small firms." },
  { q: "A demerger is:", opts: ["Two firms joining", "A takeover paid for in shares", "A firm splitting into separate businesses", "A firm closing down"], a: 2, why: "A demerger undoes a merger, for example when the parts work better apart." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Organic (internal) growth", "Growth using the firm's own resources: retained profit, investment, new products or outlets."],
  ["External growth", "Growth by joining with another firm: a merger or a takeover."],
  ["Merger", "Two firms agree to join and form one new company."],
  ["Takeover (acquisition)", "One firm buys another, usually by buying its shares."],
  ["Horizontal integration", "Joining with a firm in the same industry at the same stage of production."],
  ["Backward vertical integration", "Buying a firm earlier in the supply chain, such as a supplier."],
  ["Forward vertical integration", "Buying a firm later in the supply chain, such as a distributor or retailer."],
  ["Conglomerate integration", "Joining with a firm in an unrelated industry. Also called diversification."],
  ["Diversification", "Spreading into different products or markets to reduce risk."],
  ["Demerger", "A firm splits into separate businesses."],
  ["Minimum efficient scale", "The smallest output at which long-run average cost is at its lowest."],
  ["Economies of scale", "A fall in long-run average cost as output rises."],
  ["Diseconomies of scale", "A rise in long-run average cost as output rises beyond MES."],
  ["Concentration ratio", "The combined market share of the largest few firms."],
  ["Niche market", "A small specialist part of a market, often served by small firms."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q7] Why might a firm adopt a policy of diversification?", opts: ["to achieve cost economies of scale", "to agree common prices with rivals", "to ensure greater ability to spread investment risks", "to increase productivity of labour"], a: 2, why: "Diversification means operating in several markets, so a fall in one is less damaging. B is collusion." },
  { q: "[May/June 2021 · 31 · Q8] What would be likely to help a small firm to survive and what might be a threat to its survival? (help / threat)", opts: ["contestability of the market / expensive new technology", "customers valuing personal service / new government regulations on its business", "low barriers to entering its industry / managerial diseconomies of scale", "selling a homogeneous product / new firms entering the market"], a: 1, why: "Personal service is a classic strength of small firms; new regulations can hit them hard. Low entry barriers would be a threat, and managerial diseconomies are a large-firm problem." },
  { q: "[Oct/Nov 2020 · 31 · Q12] Which is not a reason for the existence of small firms in a market dominated by large companies?", opts: ["Small firms can concentrate on providing specialist services.", "Small firms enjoy greater economies of scale.", "Small firms enter the market with new innovative ideas.", "Small firms have good knowledge of local markets."], a: 1, why: "Large firms usually enjoy the larger economies of scale. The other three are real reasons small firms survive." },
  { q: "[May/June 2022 · 31 · Q12] What would encourage an increase in the number of small firms?", opts: ["increasing government regulation of conditions in the workplace", "more risk-averse (cautious) lending policies by banks", "stronger government laws against the growth of monopoly", "tougher penalties in the case of personal bankruptcy"], a: 2, why: "Limiting the growth of monopolies leaves more room for small firms. A raises costs; B and D make starting up harder." },
  { q: "[May/June 2022 · 32 · Q9] What would be most likely to allow the survival of small firms in an economy?", opts: ["an increase in the cost of borrowing from commercial banks", "an increase in personal services as a share of GDP", "an increase in the rate of change of information technology", "an increase in the ratio of capital to labour employed in an economy"], a: 1, why: "Personal services are often supplied by small firms, so a larger share of GDP in services helps them. A makes borrowing harder; D favours large, capital-heavy firms." },
  { q: "[Feb/March 2022 · 32 · Q11] In many developed economies, large and small firms often exist side by side in the same industry. What is most likely to explain the survival of the small firms?", opts: ["They each offer a much wider range of products.", "They have a higher minimum efficient scale.", "They pay much higher wages to their staff.", "They provide a more personal level of consumer service."], a: 3, why: "Personal service gives small firms something big firms may not match. A higher MES would make survival harder." },
  { q: "[May/June 2024 · 32 · Q8] What is likely to make it more difficult for a small firm to survive?", opts: ["increased preference on the part of consumers for distinctive non-standardised products", "reductions in the rate of interest charged by commercial banks", "the absence of effective barriers to the entry of potential competitors", "the existence of decreasing returns to scale"], a: 2, why: "Without barriers to entry, new competitors can easily appear. A and B would help small firms." },
  { q: "[May/June 2024 · 32 · Q10] What is an example of backward vertical integration?", opts: ["a bakery buying a wheat farm", "a car manufacturer buying a car showroom", "a vineyard buying an apple orchard", "two rival supermarkets joining together"], a: 0, why: "The wheat farm supplies the bakery (earlier in the chain). B is forward, C is unrelated, D is horizontal." },
  { q: "[Oct/Nov 2021 · 31 · Q6] Firm X, which currently specialises in producing cars, takes over firm Y, which owns a number of car retail outlets. How may this be described?", opts: ["horizontal integration", "the formation of a cartel", "vertical integration backwards", "vertical integration forwards"], a: 3, why: "The retailer is later in the chain, selling X's cars: forward integration." },
  { q: "[May/June 2020 · 31 · Q9] An electronics firm began as a semiconductor firm making memory chips. It used continuous research and investment to become an industry leader and applied its research to enter televisions and mobile phones. What has taken place?", opts: ["external growth and diversification", "external growth and sales revenue maximisation", "internal growth and diversification", "internal growth and sales revenue maximisation"], a: 2, why: "No firm was bought, so growth is internal (organic). Entering other markets is diversification." },
  { q: "[Oct/Nov 2022 · 33 · Q8] The manufacture of some sports equipment is dominated by very large firms but there are also smaller firms in the industry. What enables a small firm to exist in such an industry?", opts: ["high concentration ratio that reduces competition", "high start-up costs that occur in a contestable market", "decreasing average cost as a large firm expands", "a requirement for personalised equipment"], a: 3, why: "A niche for personalised products lets small firms survive. B and C describe conditions that favour big firms." },
  { q: "[Feb/March 2024 · 32 · Q9] Company R manufactures steel, S produces ships, T operates oil tankers, V operates cruise liners. Which statement is correct?", opts: ["If R takes over S, this is an example of forwards vertical integration.", "If S takes over V, this is an example of backwards vertical integration.", "If T takes over S, this is an example of diversification.", "If V takes over S, this is an example of horizontal integration."], a: 0, why: "S buys R's steel, so S is later in the chain: forward. S taking over V is forward (V buys ships); T taking over S is backward; V taking over S is backward too." },
  { q: "[Oct/Nov 2024 · 31 · Q10] Firms X and Y merge in a horizontal integration. What must be true about the industry and the stage of production in which X and Y operate? (industry / stage)", opts: ["different / different", "different / same", "same / different", "same / same"], a: 3, why: "Horizontal integration joins firms in the same industry at the same stage of production." },
] });
