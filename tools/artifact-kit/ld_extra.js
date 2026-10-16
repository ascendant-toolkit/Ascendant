
/* ---------- 40.1 additions ---------- */
const HALO = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const MPP = [20, 18, 15, 12, 9, 7, 5, 3];
$("#pic1").innerHTML = `<svg viewBox="0 0 760 390" role="img" aria-label="Marginal revenue product curve and the wage showing the number of workers hired">${hireChart({ a: 20, old: 0, wl: 1, pt: 1, zones: 1 })}</svg>`;

/* from MPP to MRP: bars */
function mrpDraw(s) {
  const m = s.m, X = (i) => 90 + i * 80, Y = (v) => 320 - v * 4.6, W = 20; let o = SV.line(70, 320, 740, 320) + SV.line(70, 320, 70, 30);
  o += SV.text(76, 24, m < 1.5 ? "Marginal physical product (units per day)" : "Marginal revenue product ($ per day)", "sm");
  const n = MPP.filter((v) => v * m >= W).length;
  MPP.forEach((v, i) => {
    const h = v * m, hired = s.hr > 0.5 && h >= W;
    o += SV.rect(X(i), Y(h), 52, 320 - Y(h), s.hr > 0.5 ? (hired ? "f3" : "f2") : "f1") + SV.text(X(i) + 26, Y(h) - 6, Math.round(h), "lbl bd", { "text-anchor": "middle", style: HALO }) + SV.text(X(i) + 26, 340, "worker " + (i + 1), "sm", { "text-anchor": "middle" });
  });
  if (s.wl > 0) o += SV.line(70, Y(W), 740, Y(W), "c2", { "stroke-dasharray": "6 5", ...op(s.wl) }) + SV.text(736, Y(W) - 8, "wage $20", "lbl bd t2", { "text-anchor": "end", style: HALO, ...op(s.wl) });
  if (s.hr > 0.5) o += SV.text(X(n - 1) + 52, 50, `hire ${n} workers (MRP ≥ wage)`, "lbl bd t3", { "text-anchor": "end", style: HALO });
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 360, label: "Marginal physical product multiplied by marginal revenue gives marginal revenue product, compared with the wage", base: { m: 1, wl: 0, hr: 0 }, draw: mrpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Marginal physical product.</b> The first worker adds 20 units of output a day, the second 18, and so on. Output per extra worker falls because of <b>diminishing marginal returns</b>.", s: { m: 1 } },
  { cap: "<b>Multiply by marginal revenue.</b> Each unit sells for $2, so MRP = MPP × $2. The first worker adds $40 of revenue, the eighth only $6. The bars are now in dollars.", s: { m: 2 } },
  { cap: "<b>Compare with the wage.</b> The wage is $20 a day. Green bars (MRP of $20 or more) add more to revenue than to cost: <b>hire 4 workers</b>. The 5th worker adds only $18, so the firm stops.", s: { m: 2, wl: 1, hr: 1 } },
  { cap: "<b>The product price rises to $3.</b> MRP = MPP × $3, every bar grows and the demand for labour shifts right. At the same $20 wage the firm now hires <b>6 workers</b>. This is derived demand at work.", s: { m: 3, wl: 1, hr: 1 } },
] });

/* ---------- Lab 1: hire the next worker, with productivity ---------- */
function lab1() {
  if (!$("#la1") || !$("#la2") || !$("#la7")) return;
  const p = +$("#la1").value, w = +$("#la2").value, boost = 1 + +$("#la7").value / 100, mrp = MPP.map((m) => m * boost * p);
  let n = 0; while (n < mrp.length && mrp[n] >= w) n++;
  $("#r1").textContent = n; $("#r2").textContent = n ? "$" + Lib.fmtN(mrp[n - 1], 1) : "-"; $("#r3").textContent = n ? "$" + Lib.fmtN(mrp[n - 1] - w, 1) : "-";
  $("#rv").textContent = n === 0 ? `Even the first worker's MRP ($${Lib.fmtN(mrp[0], 1)}) is below the wage, so the firm hires nobody.`
    : n === MPP.length ? `Every worker's MRP is at least the wage, so the firm hires all ${n}. A lower product price or a higher wage would stop it sooner.`
    : `The firm hires ${n} workers. Worker ${n + 1} would add only $${Lib.fmtN(mrp[n], 1)}, less than the $${w} wage, so hiring stops where MRP falls below the wage.`;
  const X0 = 40, bw = 36, gap = 8, top = Math.max(120, mrp[0] * 1.05), Yc = (v) => 230 - v * (200 / top);
  let o = SV.line(X0, 230, 410, 230) + SV.line(X0, 230, X0, 20) + SV.text(X0 + 4, 16, "MRP and wage ($ per day)", "sm");
  mrp.forEach((v, i) => { const x = X0 + 8 + i * (bw + gap), h = Math.min(v, top); o += SV.rect(x, Yc(h), bw, 230 - Yc(h), i < n ? "f3" : "f2") + SV.text(x + bw / 2, Yc(h) - 5, Lib.fmtN(v, 0), "sm bd", { "text-anchor": "middle", style: HALO }) + SV.text(x + bw / 2, 248, i + 1, "sm", { "text-anchor": "middle" }); });
  o += SV.text(X0 + 190, 266, "Worker number", "sm", { "text-anchor": "middle" });
  const wy = Yc(Math.min(w, top)); o += SV.line(X0, wy, 410, wy, "c2 dash") + SV.text(406, wy - 6, "Wage $" + w, "lbl bd t2", { "text-anchor": "end", style: HALO });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la1", label: "Price of the product ($): ", min: 1, max: 6, step: 0.5, value: 2, fmt: (v) => v.toFixed(1), onInput: lab1 });
Lib.slider($("#g2"), { id: "la2", label: "Wage per day ($): ", min: 5, max: 100, step: 1, value: 20, fmt: (v) => v, onInput: lab1 });
Lib.slider($("#g7"), { id: "la7", label: "Rise in worker productivity: ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => "+" + v + "%", onInput: lab1 });

/* ---------- Lab 2: elasticity along the demand curve ---------- */
function lab2() {
  if (!$("#ew")) return;
  const W = +$("#ew").value, L = 200 - 10 * W, e = -(10 * W) / L, bill = W * L;
  $("#e1").textContent = Lib.fmtN(L, 0) + "k"; $("#e2").textContent = Lib.fmtN(e, 2); $("#e3").textContent = "$" + Lib.fmtN(bill, 0) + "k";
  $("#ev").textContent = Math.abs(e) > 1.02 ? `Elastic (${Lib.fmtN(e, 2)}): a rise in the wage cuts employment by a larger percentage, so the wage bill falls. A minimum wage or union wage here would cost many jobs.`
    : Math.abs(e) < 0.98 ? `Inelastic (${Lib.fmtN(e, 2)}): a wage rise cuts employment by a smaller percentage, so the wage bill rises. Job losses are small.`
    : "Unit elastic (−1): the wage bill is at its maximum here.";
  const X = (v) => 40 + v * 1.8, Y = (v) => 240 - v * 11;
  let o = SV.line(40, 240, 400, 240) + SV.line(40, 240, 40, 20) + SV.text(396, 262, "Workers (thousand)", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Wage ($)", "sm");
  o += SV.rect(40, Y(W), X(L) - 40, 240 - Y(W), "f1") + SV.line(X(0), Y(20), X(200), Y(0), "c1") + SV.line(40, Y(W), X(L), Y(W), "gr") + SV.line(X(L), Y(W), X(L), 240, "gr") + SV.circle(X(L), Y(W), 6, "dot1");
  o += SV.text(X(L) / 2 + 20, Y(W) + 20, "wage bill = W × L", "sm bd t1", { "text-anchor": "middle", style: HALO });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "ew", label: "Wage ($): ", min: 2, max: 18, step: 1, value: 14, fmt: (v) => v, onInput: lab2 });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Drag each event into the right bucket for the labour market it affects.",
  buckets: [{ label: "Shifts demand for labour" }, { label: "Movement along the demand curve" }],
  items: [
    { text: "Demand for the firm's product rises", b: 0 }, { text: "Training raises the productivity of workers", b: 0 },
    { text: "Machines used instead of workers become cheaper", b: 0 }, { text: "A new technology raises output per worker", b: 0 },
    { text: "The wage rises and the firm hires fewer workers", b: 1 }, { text: "The wage falls and the firm hires more workers", b: 1 },
  ], done: "Wage changes move along the curve; everything else shifts it.",
});
Lib.classify($("#cl2"), {
  prompt: "Does each factor make the demand for labour more elastic or less elastic?",
  buckets: [{ label: "More elastic" }, { label: "Less elastic" }],
  items: [
    { text: "Labour is a large share of total cost", b: 0 }, { text: "Machines are a good, easy substitute", b: 0 }, { text: "The demand for the product is elastic", b: 0 }, { text: "A long time period", b: 0 },
    { text: "Labour is a small share of total cost", b: 1 }, { text: "No close substitutes for these skills", b: 1 }, { text: "The demand for the product is inelastic", b: 1 }, { text: "A short time period", b: 1 },
  ], done: "A small share of costs, no substitutes, inelastic product demand and the short run all make demand less elastic.",
});
Lib.order($("#o1"), { prompt: "Put the explanation of how a firm decides how many workers to hire in order.", items: [
  "Find the marginal physical product (MPP) of each extra worker",
  "Multiply by marginal revenue to find the marginal revenue product (MRP)",
  "MRP falls as more workers are hired, because of diminishing marginal returns",
  "Compare MRP with the marginal cost of labour (the wage)",
  "Hire while MRP is greater than the wage",
  "Stop where MRP = wage: this gives the profit-maximising employment",
], done: "This is the standard MRP argument." });
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Derived demand", "Demand that comes from the demand for the product the factor helps to make"],
  ["Marginal physical product", "The extra output from employing one more worker"],
  ["Marginal revenue product", "The extra revenue from employing one more worker"],
  ["Diminishing marginal returns", "Each extra worker adds less output than the one before"],
  ["Wage taker", "A firm that cannot influence the market wage"],
  ["Elasticity of demand for labour", "How responsive the quantity of labour demanded is to the wage"],
  ["Substitute for labour", "An input, such as a machine, that can do the same job"],
  ["Productivity", "Output per worker"],
], done: "Eight words, the core of this part." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm sells its product at $4 a unit. The 5th worker adds 7 units of output. Calculate the MRP of the 5th worker ($).", a: 28, sol: "MRP = MPP × MR = 7 × $4 = <b>$28</b>." },
  { q: "The wage is $24 a day and the next worker has an MRP of $30. By how much would employing this worker change profit ($)?", a: 6, sol: "Extra revenue $30 − extra cost $24 = <b>+$6</b>. The firm should hire." },
  { q: "Using the table (MPP 20, 18, 15, 12, 9, 7, 5, 3), product price $2 and a wage of $20 a day, how many workers does the firm hire?", a: 4, hint: "MRP = 2 × MPP. Count workers with MRP of at least $20.", sol: "MRP: 40, 36, 30, 24, 18, … so 4 workers have MRP ≥ 20: hire <b>4</b>." },
  { q: "The product price rises to $3. Using the same table and wage of $20, how many workers are hired now?", a: 6, sol: "MRP: 60, 54, 45, 36, 27, 21, 15, 9. Six workers have MRP ≥ 20: hire <b>6</b>." },
  { q: "A wage rise of 10% reduces the quantity of labour demanded by 15%. Calculate the wage elasticity of demand for labour (include the sign).", a: -1.5, tol: 0.01, ph: "e.g. -0.5", sol: "−15% ÷ 10% = <b>−1.5</b>: elastic." },
  { q: "Demand for labour is L = 200 − 10W (L in thousands). What is the wage bill when W = $10 ($ thousand)?", a: 1000, sol: "L = 100, so wage bill = 10 × 100 = <b>1,000</b>." },
  { q: "At W = $14, L = 60. Using elasticity = −(10 × W) ÷ L, what is the elasticity?", a: -2.33, tol: 0.02, sol: "−(10 × 14) ÷ 60 = <b>−2.33</b>: elastic." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Marginal revenue product is equal to:", opts: ["MPP × MR", "MPP × wage", "Total revenue ÷ workers", "MR ÷ MPP"], a: 0, why: "MRP is the extra output from one more worker multiplied by the revenue from each extra unit." },
  { q: "A profit-maximising firm in a competitive labour market hires until:", opts: ["Total revenue is maximised", "MRP equals the wage", "MPP is zero", "MRP is zero"], a: 1, why: "Each worker adds MRP to revenue and the wage to cost, so hiring stops where they are equal." },
  { q: "The MRP curve slopes downward because of:", opts: ["Rising wages", "Diminishing marginal returns", "Falling product demand", "Economies of scale"], a: 1, why: "Each extra worker adds less output, so MPP and MRP fall." },
  { q: "The demand for labour is more likely to be elastic when:", opts: ["Labour is a small share of costs", "Good substitutes for labour are available", "Demand for the product is inelastic", "The time period is short"], a: 1, why: "If machines or other inputs are easy to switch to, a wage rise leads to a larger fall in jobs." },
  { q: "Which would shift the demand for labour to the right?", opts: ["A fall in the price of the product", "A rise in labour productivity", "A rise in net migration", "A fall in the wage"], a: 1, why: "Higher productivity raises MPP and so MRP. Migration shifts supply; a lower wage is a movement along the curve." },
  { q: "In a perfectly competitive labour market the supply of labour to one firm is:", opts: ["upward sloping", "horizontal at the market wage", "vertical", "backward bending"], a: 1, why: "The firm is a wage taker and can hire as many as it likes at the market wage." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Derived demand", "Demand for a factor that comes from the demand for the product it makes."],
  ["Marginal physical product (MPP)", "The extra output from employing one more worker."],
  ["Marginal revenue product (MRP)", "The extra revenue from employing one more worker: MPP × MR."],
  ["Diminishing marginal returns", "Adding more of a variable factor to fixed capital eventually gives smaller extra output."],
  ["Hiring rule", "Hire until MRP equals the marginal cost of labour."],
  ["Wage taker", "A firm that has to pay the market wage and cannot influence it."],
  ["Demand curve for labour", "The firm's MRP curve."],
  ["Shift in demand for labour", "Caused by product demand, productivity, price of substitutes or complements."],
  ["Movement along demand for labour", "Caused only by a change in the wage."],
  ["Wage elasticity of demand for labour", "% change in quantity of labour demanded ÷ % change in the wage."],
  ["Determinants of elasticity", "Share of labour in costs, substitutes, elasticity of product demand, time."],
  ["Assumption of MRP theory", "Profit-maximising firms, identical workers and perfect information in a competitive market."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2025 · 32 · Q13] How is marginal revenue product calculated?", opts: ["marginal physical product × marginal revenue", "marginal physical product ÷ price", "total physical product × marginal cost", "total physical product ÷ marginal cost"], a: 0, why: "MRP = MPP × MR." },
  { q: "[May/June 2020 (not sat) · 31 · Q17] A firm is operating in a perfectly competitive market. Why does the marginal revenue product of a factor of production employed by the firm fall as more of the factor is employed?", opts: ["Its average revenue falls.", "Its marginal physical product falls.", "Its marginal revenue falls.", "The supply price of the factor rises."], a: 1, why: "In a perfectly competitive product market MR is constant, so MRP falls because MPP falls (diminishing returns)." },
  { q: "[May/June 2023 · 31 · Q15] Economics textbooks state that labour is a derived demand for a firm in imperfect competition. How is the demand curve for labour derived?", opts: ["by multiplying the average physical product by the average revenue", "by multiplying the average physical product by the marginal revenue", "by multiplying the marginal physical product by the marginal cost", "by multiplying the marginal physical product by the marginal revenue"], a: 3, why: "MRP = MPP × MR." },
  { q: "[May/June 2024 · 32 · Q14] When will a profit-maximising firm employ the optimum number of workers?", opts: ["when the average revenue product of labour equals the average cost of hiring workers", "when the marginal revenue product of labour equals the average cost of hiring workers", "when the marginal revenue product of labour equals the marginal cost of hiring workers", "when the marginal revenue product of labour equals the trade union supplied cost of workers"], a: 2, why: "Hire until MRP = MCL." },
  { q: "[Feb/March 2024 · 32 · Q14] What would shift the marginal revenue product curve for workers producing electric vehicles to the right?", opts: ["a decrease in the price of petrol vehicles", "a decrease in the productivity of electric vehicles workers", "an increase in the price of electric vehicles", "an increase in the wage rate of electric vehicles workers"], a: 2, why: "A higher product price raises MR and so MRP. A wage change is a movement along the curve." },
  { q: "[May/June 2024 · 31 · Q14] What will cause an outward shift in the demand for labour curve?", opts: ["a decrease in the top rate of income tax", "an increase in the demand for the final product", "an increase in subsidies to firms", "an increase in the size of the working population"], a: 1, why: "Derived demand: higher demand for the final product raises the demand for labour. A larger working population shifts supply." },
  { q: "[Oct/Nov 2024 · 32 · Q13] A diagram shows a firm's marginal revenue product of labour curve shifting to the left, from MRP1 to MRP2. What could cause this?", opts: ["a fall in the wage rate", "a fall in the price of the final product", "a rise in the wage rate", "a rise in the price of the final product"], a: 1, why: "A fall in the product price lowers MR and so MRP. Wage changes are movements along the curve." },
  { q: "[Feb/March 2021 · 32 · Q17] What would be most likely to cause the demand for labour in an industry to be inelastic?", opts: ["Labour costs are a small percentage of total cost.", "The demand for the final product has a price elasticity of demand that is greater than one.", "The workforce belongs to a strong trade union.", "There is a large pool of readily available labour."], a: 0, why: "If labour is a small share of costs, a wage rise changes total cost little, so firms cut few jobs." },
] });
