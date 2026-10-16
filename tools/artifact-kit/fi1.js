// uses: econ
/* ---------- 1. stepper: diminishing returns ---------- */
const TP = [10, 30, 60, 84, 100, 110, 114, 114], MPd = [10, 20, 30, 24, 16, 10, 4, 0], APd = TP.map((v, i) => v / (i + 1));
Lib.stepper($("#stA"), {
  w: 760, h: 400, label: "Total, marginal and average product as workers are added to a fixed factory", base: { n: 0, pk: 0, cut: 0 },
  draw: (s) => {
    const Yt = (v) => 340 - (v * 300) / 120, Ym = (v) => 340 - (v * 300) / 32, Xb = (i) => 60 + (i - 1) * 38, Xl = (i) => 430 + (i - 1) * 40;
    let o = SV.line(60, 40, 60, 340) + SV.line(60, 340, 366, 340) + SV.line(420, 40, 420, 340) + SV.line(420, 340, 724, 340);
    o += SV.text(64, 34, "Total product (TP)", "lbl bd", { "text-anchor": "start" }) + SV.text(424, 34, "MP and AP per worker", "lbl bd", { "text-anchor": "start" });
    o += SV.text(366, 384, "Workers", "sm", { "text-anchor": "end" }) + SV.text(724, 384, "Workers", "sm", { "text-anchor": "end" });
    for (let i = 1; i <= 8; i++) {
      const f = clamp01(s.n - (i - 1));
      o += SV.text(Xb(i) + 14, 358, i, "sm", { "text-anchor": "middle" }) + SV.text(Xl(i), 358, i, "sm", { "text-anchor": "middle" });
      if (f > 0) o += SV.rect(Xb(i), Yt(TP[i - 1] * f), 28, (TP[i - 1] * f * 300) / 120, "f1", { opacity: 0.6 });
      if (f > 0.95) o += SV.text(Xb(i) + 14, Yt(TP[i - 1]) - 6, TP[i - 1], "sm", { "text-anchor": "middle" });
      if (f > 0) o += SV.circle(Xl(i), Ym(MPd[i - 1]), 5, "dot2", { opacity: f }) + SV.circle(Xl(i), Ym(APd[i - 1]), 5, "dot1", { opacity: f });
      if (i < 8) {
        const g = clamp01(s.n - i);
        if (g > 0) {
          const e = (a) => Xl(i) + (Xl(i + 1) - Xl(i)) * g, mm = MPd[i - 1] + (MPd[i] - MPd[i - 1]) * g, aa = APd[i - 1] + (APd[i] - APd[i - 1]) * g;
          o += SV.line(Xl(i), Ym(MPd[i - 1]), e(), Ym(mm), "c2") + SV.line(Xl(i), Ym(APd[i - 1]), e(), Ym(aa), "c1");
        }
      }
    }
    o += SV.text(716, Ym(0.8), "MP", "lbl bd t2", { "text-anchor": "end", opacity: clamp01(s.n - 6) }) + SV.text(716, Ym(14.8), "AP", "lbl bd t1", { "text-anchor": "end", opacity: clamp01(s.n - 6) });
    if (s.pk) o += SV.line(Xl(3), 40, Xl(3), 340, "gr", { opacity: s.pk }) + SV.text(Xl(3) + 6, 56, "MP peaks here", "sm", { "text-anchor": "start", opacity: s.pk });
    if (s.cut) o += SV.circle((Xl(4) + Xl(5)) / 2, Ym(20.5), 9, "dot4", { opacity: s.cut * 0.5 }) + SV.line((Xl(4) + Xl(5)) / 2, Ym(20.5) + 9, (Xl(4) + Xl(5)) / 2, Ym(7), "gr", { opacity: s.cut }) + SV.text((Xl(4) + Xl(5)) / 2, Ym(5), "MP cuts AP at AP's maximum", "lbl bd t4", { "text-anchor": "middle", opacity: s.cut });
    return o;
  },
  steps: [
    { cap: "A factory has fixed capital. Workers are the variable factor. We add one worker at a time and track <b>TP</b> (total output), <b>MP</b> (extra output from the last worker) and <b>AP</b> (TP ÷ workers).", s: { n: 0, pk: 0, cut: 0 } },
    { cap: "<b>1 worker:</b> TP = 10. MP = 10 (the first worker's whole output) and AP = 10.", s: { n: 1, pk: 0, cut: 0 } },
    { cap: "<b>Workers 2 and 3:</b> division of labour and better use of the machines. TP rises to 60. MP <b>rises</b> to 30, and AP rises behind it to 20.", s: { n: 3, pk: 1, cut: 0 } },
    { cap: "<b>4th worker:</b> TP = 84, but MP falls to 24. This is the <b>law of diminishing returns</b>: each worker has less fixed capital to share. TP still rises, and AP still rises (to 21) because MP is above AP.", s: { n: 4, pk: 1, cut: 0 } },
    { cap: "<b>5th worker:</b> MP = 16, now <b>below</b> AP, so AP falls to 20. MP always cuts AP at AP's maximum.", s: { n: 5, pk: 1, cut: 1 } },
    { cap: "<b>Workers 6 to 8:</b> MP keeps falling. TP rises more and more slowly and stops at 114 when the 8th worker adds nothing (MP = 0). <b>TP is at its maximum where MP = 0.</b>", s: { n: 8, pk: 1, cut: 1 } },
  ],
});

/* ---------- 2. stepper: short-run cost curves ---------- */
Lib.stepper($("#stB"), {
  w: 760, h: 400, label: "Average fixed, average variable, average total and marginal cost curves", base: { a: 0, v: 0, m: 0, t: 0, d1: 0, d2: 0 },
  draw: (s) => {
    const F = frame(760, 400, 70, 730, 20, 350, 5.5, 0, 40);
    let o = axes(F, "Output (Q)", "Cost per unit ($)");
    o += costSet(F, 20, { a: s.a, v: s.v, t: s.t, m: s.m });
    if (s.d1) o += SV.circle(F.X(3), F.Y(6), 7, "dot4", { opacity: s.d1 }) + SV.line(F.X(3), F.Y(6), F.X(3), F.Y(0), "gr", { opacity: s.d1 }) + SV.text(F.X(3) - 10, F.Y(6) + 26, "MC = AVC at AVC's minimum", "lbl bd t4", { "text-anchor": "end", opacity: s.d1 });
    if (s.d2) o += SV.circle(F.X(3.71), F.Y(11.8), 8, "dot4", { opacity: s.d2 }) + SV.line(F.X(3.71), F.Y(11.8), F.X(3.71), F.Y(0), "gr", { opacity: s.d2 }) + SV.text(F.X(3.71) + 12, F.Y(11.8) - 14, "Optimum output: MC = ATC", "lbl bd t4", { "text-anchor": "start", opacity: s.d2 });
    return o;
  },
  steps: [
    { cap: "A firm has <b>fixed costs of $20</b> and variable costs that depend on output. Costs per unit are shown on the vertical axis.", s: {} },
    { cap: "<b>AFC = FC ÷ Q.</b> The same $20 is spread over more and more units, so AFC falls all the way. It never turns up.", s: { a: 1 } },
    { cap: "<b>AVC = VC ÷ Q.</b> It falls at first, then rises as diminishing returns bite. U-shaped.", s: { a: 1, v: 1 } },
    { cap: "<b>MC</b> is the cost of one more unit. It also falls then rises, but it <b>cuts AVC at AVC's lowest point</b>: while MC is below AVC the average is pulled down, once MC is above it the average is pulled up.", s: { a: 1, v: 1, m: 1, d1: 1 } },
    { cap: "<b>ATC = AFC + AVC.</b> It is U-shaped too, and MC cuts it at its lowest point. That is the <b>optimum output</b>: the lowest cost per unit the firm can reach in the short run.", s: { a: 1, v: 1, m: 1, t: 1, d1: 1, d2: 1 } },
  ],
});

/* ---------- Lab 1: short-run costs ---------- */
function lab1() {
  if (!$("#a1") || !$("#a2")) return;
  const q = +$("#a1").value, fc = +$("#a2").value, vc = q * AVC(q), tc = fc + vc;
  $("#k1").textContent = "$" + Lib.fmtN(tc, 1); $("#k2").textContent = "$" + Lib.fmtN(fc / q, 1); $("#k3").textContent = "$" + Lib.fmtN(AVC(q), 1); $("#k4").textContent = "$" + Lib.fmtN(ATC(q, fc), 1); $("#k5").textContent = "$" + Lib.fmtN(MC(q), 1);
  let best = 0.4, bv = 1e9; for (let x = 0.4; x <= 5.5; x += 0.01) if (ATC(x, fc) < bv) { bv = ATC(x, fc); best = x; }
  $("#v1").textContent = Math.abs(q - best) < 0.1 ? `This is the optimum output: MC meets ATC and ATC is at its lowest ($${Lib.fmtN(bv, 1)}).` : q < best ? "Left of the optimum: MC is below ATC, so ATC is still falling." : "Right of the optimum: MC is above ATC, so ATC is rising.";
  const F = frame(480, 360, 50, 460, 20, 320, 5.5, 0, 40);
  let s = axes(F, "Output (Q)", "Cost per unit ($)") + costSet(F, fc) + SV.line(F.X(q), F.Y(0), F.X(q), F.t, "gr") + SV.circle(F.X(q), F.Y(Math.min(40, ATC(q, fc))), 6, "dot1");
  $("#lab1").innerHTML = s;
}
Lib.slider($("#sl1"), { id: "a1", label: "Output (Q)", min: 0.5, max: 5.5, step: 0.1, value: 2, fmt: (v) => v.toFixed(1), onInput: lab1 });
Lib.slider($("#sl2"), { id: "a2", label: "Fixed cost (FC)", min: 0, max: 40, step: 2, value: 20, fmt: (v) => "$" + v, onInput: lab1 });
lab1();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Which of these are fixed costs and which are variable costs in the short run?",
  buckets: [{ label: "Fixed cost" }, { label: "Variable cost" }],
  items: [
    { text: "Rent on the factory", b: 0 }, { text: "Insurance on the building", b: 0 }, { text: "Salaries of permanent managers", b: 0 }, { text: "Repayments on a machinery loan", b: 0 },
    { text: "Raw materials", b: 1 }, { text: "Hourly wages of temporary workers", b: 1 }, { text: "Electricity used by machines", b: 1 }, { text: "Packaging", b: 1 },
  ],
  done: "Fixed costs do not change with output in the short run. Variable costs rise as output rises.",
});
Lib.order($("#o1"), { prompt: "Put the chain from diminishing returns to rising average cost in order.", items: [
  "A firm adds more workers to a fixed amount of capital.",
  "Each extra worker has less capital to share.",
  "Marginal product starts to fall.",
  "The cost of producing one more unit (MC) starts to rise.",
  "MC pulls AVC and then ATC upwards.",
] });
Lib.calc($("#c1"), { qs: [
  { q: "TP is 60 with 3 workers and 84 with 4 workers. What is the marginal product of the 4th worker?", a: 24, hint: "MP = change in TP ÷ change in workers.", sol: "MP = 84 − 60 = 24 units." },
  { q: "TP is 100 with 5 workers. What is the average product?", a: 20, hint: "AP = TP ÷ number of workers.", sol: "AP = 100 ÷ 5 = 20 units per worker." },
  { q: "A firm has fixed costs of $200 and variable costs of $600 at an output of 50 units. What is the average total cost?", a: 16, unit: "$", hint: "ATC = TC ÷ Q, and TC = FC + VC.", sol: "TC = 200 + 600 = $800. ATC = 800 ÷ 50 = $16." },
  { q: "Total cost rises from $300 to $312 when output rises from 20 to 21 units. What is the marginal cost?", a: 12, unit: "$", hint: "MC = change in TC ÷ change in Q.", sol: "MC = (312 − 300) ÷ (21 − 20) = $12." },
  { q: "AVC at 4 units of output is $11 and AFC is $12.50. What is ATC ($)?", a: 23.5, tol: 0.01, sol: "ATC = AFC + AVC = 12.50 + 11 = <b>$23.50</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The law of diminishing returns applies when", opts: ["all factors are increased in the same proportion", "one factor is varied and at least one is fixed", "a firm moves to a bigger plant", "firms enter an industry"], a: 1, why: "Diminishing returns is a short-run idea: one factor is fixed, so extra units of the variable factor add less and less." },
  { q: "Marginal cost cuts average total cost", opts: ["at ATC's maximum point", "at ATC's minimum point", "where AFC is zero", "at the origin"], a: 1, why: "MC pulls ATC down while below it and up when above it, so it cuts ATC at its lowest point." },
  { q: "Which cost falls continuously as output rises in the short run?", opts: ["Marginal cost", "Average variable cost", "Average fixed cost", "Average total cost"], a: 2, why: "Fixed cost is spread over more and more units." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Law of diminishing returns", "In the short run, as more of a variable factor is added to a fixed factor, the extra output from each additional unit eventually falls."],
  ["Marginal product", "The extra output from one more unit of a variable factor."],
  ["Average product", "Total product divided by the number of units of the variable factor."],
  ["Fixed costs", "Costs that do not change with output in the short run."],
  ["Marginal cost", "The extra cost of producing one more unit of output."],
  ["Optimum output", "The output where MC = ATC and average total cost is at its lowest in the short run."],
] });

/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
  { id: "pr1", title: "1 · Total, average and marginal product", ctx: "Sketch TP against number of workers, then AP and MP on a second set of axes below it.", ask: "Explain why MP rises then falls, and identify the point where MP = AP. Apply it: think of a small business (a restaurant kitchen, say). At what point would adding another worker start doing more harm than good?" },
  { id: "pr2", title: "2 · Short-run cost curves", ctx: "Sketch AFC, AVC, ATC and MC on one set of axes.", ask: "Explain why MC cuts AVC and ATC at their minimum points, and why AFC never has a U-shape. Apply it: for a firm you know, what counts as its fixed cost and what counts as its variable cost?" },
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
  { q: "[Feb/March 2021 · 32 · Q8] When output increases in the short run, which statement is correct?", opts: ["Average fixed cost first falls and then, beyond some point, rises.", "Average variable cost increases as soon as the law of diminishing marginal returns begins to operate.", "The minimum point of the average total cost curve occurs at a greater level of output than the minimum point of the average variable cost curve.", "When marginal cost reaches its minimum point, average variable cost must be greater than average fixed cost."], a: 2, why: "MC cuts AVC at its minimum and ATC at its minimum, and ATC includes falling AFC, so ATC reaches its lowest point at a higher output than AVC." },
  { q: "[Feb/March 2025 · 32 · Q1] Which cost will continually decrease as a firm's output increases in the short run?", opts: ["average cost", "average fixed cost", "average variable cost", "marginal cost"], a: 1, why: "Average fixed cost is fixed cost divided by output, so it falls as output rises." },
  { q: "[Feb/March 2020 · 32 · Q8] Why might a firm continue in production in the short run even though the price of its product has fallen below its average total costs of production?", opts: ["It anticipates a rise in variable costs.", "It expects the fall in price to be temporary.", "It has large fixed costs of production.", "It has no control over the price of its product."], a: 1, why: "In the short run a firm may carry on if price covers variable cost and it expects price to recover. Large fixed costs are paid anyway, but they do not explain staying open." },
  { q: "[May/June 2020 (not sat) · 31 · Q6] In the short run, a firm produces an extra unit of output. Which of the firm's production costs will change?", opts: ["fixed cost only", "fixed cost and variable cost", "variable cost only", "variable cost and total cost"], a: 3, why: "Fixed cost does not change with output, so variable cost and total cost both rise." },
  { q: "[May/June 2020 (not sat) · 32 · Q7] The table shows total costs for a firm producing chairs: output 0 gives $50, 1 gives $60, 2 gives $64, 3 gives $77, 4 gives $94, 5 gives $114. What is the average variable cost when output is 4 chairs?", opts: ["$11", "$17", "$44", "$23.50"], a: 0, why: "Fixed cost is $50 (the cost at zero output), so variable cost at 4 chairs is 94 − 50 = 44, and 44 ÷ 4 = $11." },
] });
