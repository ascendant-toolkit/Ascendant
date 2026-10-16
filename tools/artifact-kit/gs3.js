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


/* ---------- Watch: takeover and the consumer ---------- */
const TB = 270, TH = (v) => v * 20;
function takeDraw(s) {
  let o = SV.line(60, TB, 740, TB) + SV.text(62, 24, "$ per unit", "sm");
  const bar = (x, v, c, l, k, t) => k > 0 ? SV.rect(x, TB - TH(v), 64, TH(v), c, { opacity: k }) + SV.text(x + 32, TB - TH(v) - 6, t, "lbl bd", { "text-anchor": "middle", opacity: k }) + SV.text(x + 32, TB + 18, l, "sm", { "text-anchor": "middle", opacity: k }) : "";
  o += bar(90, 10, "f1", "Price", s.a, "$10.00") + bar(170, 8, "f2", "Cost", s.a, "$8.00") + (s.a > 0 ? SV.text(165, TB + 42, "Before", "lbl bd", { "text-anchor": "middle" }) : "");
  o += bar(310, 7.2, "f3", "Cost", s.b, "$7.20") + bar(390, 9.6, "f1", "Price", s.c, "$9.60") + (s.b > 0 ? SV.text(385, TB + 42, "After: saving passed on", "lbl bd", { "text-anchor": "middle" }) : "");
  o += bar(560, 7.2, "f3", "Cost", s.d, "$7.20") + bar(640, 10.6, "f4", "Price", s.d, "$10.60") + (s.d > 0 ? SV.text(635, TB + 42, "After: market power", "lbl bd", { "text-anchor": "middle" }) : "");
  return o;
}
Lib.stepper($("#stT"), { w: 780, h: 320, label: "Price and unit cost before a takeover, after it with savings passed on and after it with greater market power", base: { a: 0, b: 0, c: 0, d: 0 }, draw: takeDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Before the takeover.</b> The firm sells at <b>$10</b> and unit cost is <b>$8</b>, so profit is $2 a unit.", s: { a: 1 } },
  { cap: "<b>Economies of scale.</b> A larger firm cuts unit cost by 10% to <b>$7.20</b>, a saving of $0.80 a unit.", s: { a: 1, b: 1 } },
  { cap: "<b>Competition passes on half.</b> If rivals keep competition strong, the firm passes half of the saving to consumers: price falls to <b>$9.60</b> and profit rises to $2.40. Consumers <b>and</b> the firm gain.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Market power instead.</b> If the takeover removes a rival and the firm can raise price by 10% while still passing on half the saving, price is <b>$10.60</b>. Costs fall but consumers pay more: the gain goes to the firm, which is why authorities may block some deals.", s: { a: 1, b: 0.4, c: 0.4, d: 1 } },
] });
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
Lib.order($("#o1"), { prompt: "Put the explanation of how a takeover could lead to lower prices in the best order.", items: [
  "A firm takes over a rival in the same industry (horizontal integration)",
  "Output is combined, so the firm produces on a larger scale",
  "Economies of scale such as bulk buying lower the average cost per unit",
  "Competition from other firms still forces the firm to pass the saving on",
  "The price charged to consumers could fall",
  "Evaluate: if competition falls instead, the firm may keep the saving or raise prices",
], done: "This is the chain of reasoning behind a strong 20-mark answer." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Market power", "The ability of a firm to influence price"],
  ["Concentration ratio", "The combined market share of the largest few firms"],
  ["Competition authority", "A body that reviews mergers and can block them"],
  ["Niche market", "A small specialist part of a market"],
  ["Economies of scale", "A fall in LRAC as output rises"],
  ["Contestable market", "A market where rivals can enter easily"],
  ["Public interest", "The overall benefit to consumers and society"],
], done: "Seven words for the effects of mergers." });
Lib.calc($("#c1"), { qs: [
  { q: "Two firms have market shares of 18% and 12%. They merge. What is the combined market share (%)?", a: 30, sol: "18 + 12 = <b>30%</b>." },
  { q: "The four largest firms have shares of 30%, 25%, 15% and 10%. What is the four-firm concentration ratio (%)?", a: 80, sol: "30 + 25 + 15 + 10 = <b>80%</b>." },
  { q: "A takeover cuts a firm's unit cost from $8 to $7. The firm passes on half of the saving and prices were $10. What is the new price ($)?", a: 9.5, sol: "Saving = $1. Half passed on = $0.50. New price = 10 − 0.50 = <b>$9.50</b>." },
  { q: "A takeover cuts unit cost from $8 to $7.20 and the price was $10. The firm passes on half of the saving. What is the new price ($)?", a: 9.6, tol: 0.01, sol: "Saving 0.80; half is 0.40; 10 − 0.40 = <b>$9.60</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is most likely to be a benefit of a merger for consumers?", opts: ["Fewer firms to choose from", "Economies of scale passed on in lower prices", "Greater X-inefficiency", "Higher barriers to entry"], a: 1, why: "Lower costs from scale could lead to lower prices if competition forces the saving to be passed on." },
  { q: "Which makes the survival of small firms more likely?", opts: ["A large minimum efficient scale", "Customers valuing personalised service", "Large rivals' price cuts", "Banks refusing loans"], a: 1, why: "Customers who value service may pay a higher price. The others harm small firms." },
  { q: "A takeover removes a rival and the merged firm raises price. Consumers are:", opts: ["better off", "worse off", "unaffected", "certain to gain from economies of scale"], a: 1, why: "A higher price with fewer rivals reduces consumer welfare, even if costs fall." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Concentration ratio", "The combined market share of the largest few firms."],
  ["Niche market", "A small specialist part of a market, often served by small firms."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q8] What would be likely to help a small firm to survive and what might be a threat to its survival? (help / threat)", opts: ["contestability of the market / expensive new technology", "customers valuing personal service / new government regulations on its business", "low barriers to entering its industry / managerial diseconomies of scale", "selling a homogeneous product / new firms entering the market"], a: 1, why: "Personal service is a classic strength of small firms; new regulations can hit them hard. Low entry barriers would be a threat, and managerial diseconomies are a large-firm problem." },
  { q: "[Oct/Nov 2020 · 31 · Q12] Which is not a reason for the existence of small firms in a market dominated by large companies?", opts: ["Small firms can concentrate on providing specialist services.", "Small firms enjoy greater economies of scale.", "Small firms enter the market with new innovative ideas.", "Small firms have good knowledge of local markets."], a: 1, why: "Large firms usually enjoy the larger economies of scale. The other three are real reasons small firms survive." },
  { q: "[May/June 2022 · 31 · Q12] What would encourage an increase in the number of small firms?", opts: ["increasing government regulation of conditions in the workplace", "more risk-averse (cautious) lending policies by banks", "stronger government laws against the growth of monopoly", "tougher penalties in the case of personal bankruptcy"], a: 2, why: "Limiting the growth of monopolies leaves more room for small firms. A raises costs; B and D make starting up harder." },
  { q: "[May/June 2022 · 32 · Q9] What would be most likely to allow the survival of small firms in an economy?", opts: ["an increase in the cost of borrowing from commercial banks", "an increase in personal services as a share of GDP", "an increase in the rate of change of information technology", "an increase in the ratio of capital to labour employed in an economy"], a: 1, why: "Personal services are often supplied by small firms, so a larger share of GDP in services helps them. A makes borrowing harder; D favours large, capital-heavy firms." },
  { q: "[Feb/March 2022 · 32 · Q11] In many developed economies, large and small firms often exist side by side in the same industry. What is most likely to explain the survival of the small firms?", opts: ["They each offer a much wider range of products.", "They have a higher minimum efficient scale.", "They pay much higher wages to their staff.", "They provide a more personal level of consumer service."], a: 3, why: "Personal service gives small firms something big firms may not match. A higher MES would make survival harder." },
  { q: "[May/June 2024 · 32 · Q8] What is likely to make it more difficult for a small firm to survive?", opts: ["increased preference on the part of consumers for distinctive non-standardised products", "reductions in the rate of interest charged by commercial banks", "the absence of effective barriers to the entry of potential competitors", "the existence of decreasing returns to scale"], a: 2, why: "Without barriers to entry, new competitors can easily appear. A and B would help small firms." },
] });
