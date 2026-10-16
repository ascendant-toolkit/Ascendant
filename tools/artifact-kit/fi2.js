// uses: econ
/* ---------- 3. stepper: SRAC curves and the LRAC envelope ---------- */
const L = (q) => 0.25 * (q - 5) * (q - 5) + 5, centres = [2, 3.5, 5, 6.5, 8];
const sracF = (c) => (q) => L(c) + 0.5 * (c - 5) * (q - c) + 0.6 * (q - c) * (q - c);
Lib.stepper($("#stC"), {
  w: 760, h: 400, label: "Short-run average cost curves for different plant sizes and the long-run average cost envelope", base: { s0: 0, s1: 0, s2: 0, s3: 0, s4: 0, e: 0, z: 0 },
  draw: (s) => {
    const F = frame(760, 400, 70, 730, 20, 350, 10, 0, 14);
    let o = axes(F, "Output (Q)", "Cost per unit ($)");
    centres.forEach((c, k) => { const a = (s["s" + k] || 0) * (1 - 0.65 * s.e); if (a > 0) { const f = sracF(c); o += SV.path(curve(f, Math.max(0.2, c - 2.2), Math.min(9.8, c + 2.2), F), "c1", { opacity: a }) + SV.text(F.X(c), F.Y(f(c)) + 20, "SRAC" + (k + 1), "sm", { "text-anchor": "middle", opacity: a }); } });
    if (s.e) o += SV.path(curve(L, 0.2, 9.8, F), "c2", { opacity: s.e }) + SV.text(F.X(9.6), F.Y(L(9.6)) - 10, "LRAC", "lbl bd t2", { "text-anchor": "end", opacity: s.e });
    if (s.z) o += SV.circle(F.X(5), F.Y(5), 8, "dot4", { opacity: s.z }) + SV.line(F.X(5), F.Y(5), F.X(5), F.Y(0), "gr", { opacity: s.z }) + SV.text(F.X(5), F.Y(0) - 10, "MES", "lbl bd t4", { "text-anchor": "middle", opacity: s.z })
      + SV.text(F.X(2.2), F.Y(13), "Economies of scale", "lbl bd t3", { "text-anchor": "middle", opacity: s.z }) + SV.text(F.X(7.8), F.Y(13), "Diseconomies of scale", "lbl bd t2", { "text-anchor": "middle", opacity: s.z });
    return o;
  },
  steps: [
    { cap: "In the long run the firm can choose its plant size. Each <b>SRAC</b> curve shows average cost for <b>one</b> plant size, with that plant fixed.", s: { s0: 1 } },
    { cap: "A bigger plant gives a different SRAC curve, centred on a higher output. The firm picks whichever plant gives the <b>lowest cost per unit</b> for the output it wants.", s: { s0: 1, s1: 1, s2: 1 } },
    { cap: "With a whole family of plant sizes available, the choices overlap like scallops.", s: { s0: 1, s1: 1, s2: 1, s3: 1, s4: 1 } },
    { cap: "The <b>LRAC curve</b> is the envelope: the lowest cost per unit available at each output once any plant can be chosen. It touches each SRAC at one point only.", s: { s0: 1, s1: 1, s2: 1, s3: 1, s4: 1, e: 1 } },
    { cap: "LRAC falls while the firm gets <b>economies of scale</b>, bottoms out at the <b>minimum efficient scale (MES)</b>, then rises with <b>diseconomies of scale</b>.", s: { s0: 1, s1: 1, s2: 1, s3: 1, s4: 1, e: 1, z: 1 } },
  ],
});

/* ---------- Lab 2: isoquant and isocost ---------- */
Lib.slider($("#sl3"), { id: "a3", label: "Wage per unit of labour", min: 4, max: 40, step: 1, value: 10, fmt: (v) => "$" + v, onInput: (w) => {
  const r = 10, Lq = Math.sqrt((100 * r) / w), K = Math.sqrt((100 * w) / r), C = w * Lq + r * K;
  $("#i1").textContent = Lib.fmtN(Lq, 1); $("#i2").textContent = Lib.fmtN(K, 1); $("#i3").textContent = "$" + Lib.fmtN(C, 0);
  $("#v2").textContent = w === r ? "Labour and capital cost the same, so the firm uses equal amounts of each." : w > r ? "Labour is dearer than capital, so the firm uses less labour and more capital." : "Labour is cheaper than capital, so the firm uses more labour and less capital.";
  const F = frame(480, 360, 50, 460, 20, 320, 30, 0, 30);
  let s = axes(F, "Labour (L)", "Capital (K)");
  const p = []; for (let x = 3.4; x <= 30; x += 0.2) p.push([F.X(x), F.Y(100 / x)]);
  s += SV.path(ptsPath(p), "c1") + SV.text(F.X(25), F.Y(100 / 25) - 10, "100 units", "lbl bd t1");
  const k0 = C / r, x0 = k0 > 30 ? ((k0 - 30) * r) / w : 0, y0 = k0 > 30 ? 30 : k0, x1 = Math.min(30, C / w), y1 = x1 < C / w ? k0 - (w / r) * x1 : 0;
  s += SV.line(F.X(x0), F.Y(y0), F.X(x1), F.Y(y1), "c2") + SV.circle(F.X(Lq), F.Y(K), 7, "dot2");
  s += SV.text(F.X(Lq) + 12, F.Y(K) - 10, `L = ${Lib.fmtN(Lq, 1)}, K = ${Lib.fmtN(K, 1)}`, "lbl bd t2", { "text-anchor": "start" });
  $("#lab2").innerHTML = s;
} });

/* ---------- Practise ---------- */
Lib.classify($("#cl2"), {
  prompt: "Is each of these an internal or an external economy of scale?",
  buckets: [{ label: "Internal (the firm grows)" }, { label: "External (the industry grows)" }],
  items: [
    { text: "Buying raw materials in bulk at a discount", b: 0 }, { text: "Large firm borrows at a lower interest rate", b: 0 }, { text: "Hiring specialist managers", b: 0 }, { text: "Advertising spread over far more units", b: 0 },
    { text: "A local pool of skilled, industry-trained workers", b: 1 }, { text: "A cluster of nearby suppliers", b: 1 }, { text: "Shared port and road infrastructure built for the industry", b: 1 }, { text: "University research spillovers", b: 1 },
  ],
  done: "Internal economies are movements along the LRAC curve. External economies shift the whole curve down.",
});
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Isoquant", "All labour and capital combinations that give the same output"],
  ["Isocost line", "All combinations of factors that cost the same total amount"],
  ["Least-cost combination", "Where the isocost line just touches the isoquant"],
  ["Long-run average cost", "The lowest average cost at each output when all factors can change"],
  ["Minimum efficient scale", "The lowest output at which LRAC reaches its minimum"],
  ["Internal economies", "Falling LRAC from the growth of the firm itself"],
  ["External economies", "Lower costs for every firm from the growth of the whole industry"],
], done: "Seven terms for the long run." });
Lib.order($("#o1"), { prompt: "Put the explanation of how internal economies of scale lower average cost in order.", items: [
  "The firm increases its output in the long run",
  "It can buy materials in bulk and use specialised machinery and managers",
  "Total cost rises by less than the rise in output",
  "Average cost (total cost ÷ output) falls",
  "The firm moves down its long-run average cost curve towards MES",
  "Beyond MES diseconomies of scale may raise average cost again",
], done: "Internal economies are a movement along the LRAC curve." });
Lib.calc($("#c1"), { qs: [
  { q: "To produce 100 units, labour costs $10 a unit and capital $10 a unit, and the least-cost mix is 10 labour and 10 capital. What is the total cost ($)?", a: 200, sol: "10 × 10 + 10 × 10 = <b>$200</b>." },
  { q: "The wage rises to $40. The least-cost mix becomes 5 labour and 20 capital (capital still $10). What is the total cost ($)?", a: 400, sol: "40 × 5 + 10 × 20 = <b>$400</b>. The firm uses less of the dearer factor." },
  { q: "A firm's total cost is $2,000 at 100 units and $3,600 at 300 units. What is the long-run average cost at 300 units ($)?", a: 12, sol: "3,600 ÷ 300 = <b>$12</b>, down from $20 at 100 units: economies of scale." },
  { q: "Output doubles from 200 to 400 and total cost rises from $4,000 to $6,000. By what percentage does average cost fall (%)?", a: 25, sol: "Average cost falls from $20 to $15: (20 − 15) ÷ 20 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A cluster of suppliers growing near a car factory lowers every local firm's costs. This is", opts: ["an internal economy of scale", "an external economy of scale", "diminishing returns", "an internal diseconomy"], a: 1, why: "The saving comes from the industry or area growing, not from the firm's own size, so the whole LRAC curve shifts down." },
  { q: "A firm growing along its long-run average cost curve towards MES is likely to benefit from:", opts: ["diminishing returns", "internal economies of scale", "fixed costs", "external diseconomies"], a: 1, why: "Falling LRAC as the firm grows is the effect of internal economies of scale." },
  { q: "Which is a diseconomy of scale?", opts: ["Bulk-buying discounts", "Slower decisions in a very large firm", "Cheaper loans", "A local pool of skilled workers"], a: 1, why: "Management and communication problems raise average cost beyond MES." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Isoquant", "A line joining every combination of labour and capital that produces the same output."],
  ["Isocost line", "A line joining every combination of factors that costs the same total amount."],
  ["Long-run average cost (LRAC)", "The lowest average cost at each output when all factors, including plant size, can be varied."],
  ["Minimum efficient scale", "The lowest output at which LRAC reaches its minimum."],
  ["Internal economies of scale", "Falling LRAC caused by the growth of the firm itself."],
  ["External economies of scale", "Lower costs for every firm caused by the growth of the whole industry or location."],
] });

/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
  { id: "pr3", title: "3 · Isoquants and isocosts", ctx: "Sketch two isoquants (Q1 and Q2) with an isocost line tangent to Q1.", ask: "Explain what the tangency point represents, and why a firm would move away from any other point on the isoquant. Apply it: for a real industry, would you expect the least-cost combination to use more labour or more capital, and why?" },
  { id: "pr4", title: "4 · SRAC envelope and the LRAC curve", ctx: "Sketch several SRAC curves and the LRAC envelope that wraps around them, marking the minimum efficient scale.", ask: "Explain why the LRAC only touches each SRAC at one point. Apply it: name an industry with a high MES and one with a low MES, and say what that implies about how many firms compete in each." },
  { id: "pr5", title: "5 · Economies and diseconomies of scale", ctx: "No chart needed: list two examples each of internal and external economies of scale for a real company you know.", ask: "Explain the difference between an internal and an external economy of scale using your examples. Apply it: what might cause that company to run into diseconomies of scale if it kept growing?" },
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
  { q: "[Feb/March 2024 · 32 · Q4] The statement and the table provide information about a production function. The production function represents the amount of ...1... obtainable from each combination of ...2... and can be used to give information about ...3.... Which words correctly complete gaps 1, 2 and 3?", opts: ["demand, labour, returns to scale", "demand, labour, normal profit", "output, inputs, returns to scale", "output, inputs, supernormal profit"], a: 2, why: "A production function links inputs to the maximum output, and shows returns to scale when all inputs change." },
  { q: "[Feb/March 2020 · 32 · Q10] What is true about economies of scale but not diseconomies of scale?", opts: ["They occur because average revenue is increasing.", "They occur because of management policy changes.", "They occur in the short run.", "They occur with decreasing average cost."], a: 3, why: "Economies of scale are falling average cost as output rises; diseconomies are rising average cost." },
  { q: "[Feb/March 2024 · 32 · Q5] Two firms selling the same type of product find it more efficient to merge. Which combination describes how the merged firm's average costs of production and demand curve are expected to change?", opts: ["average costs fall, demand curve more elastic", "average costs fall, demand curve more inelastic", "average costs rise, demand curve more elastic", "average costs rise, demand curve more inelastic"], a: 1, why: "A larger firm may gain economies of scale so costs fall, and with fewer rivals the demand it faces becomes less elastic." },
] });
