
/* ---------- 40.5: the minimum wage ---------- */
const HALO = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
$("#pic1").innerHTML = `<svg viewBox="0 0 760 390" role="img" aria-label="Competitive labour market with a minimum wage above equilibrium causing unemployment">${cmChart({ d: 1, s: 1, e: 0.5, m: 1, q: 1, u: 1 })}</svg>`;

/* ---------- Lab 3: do low-paid workers gain overall? ---------- */
function lab4() {
  if (!$("#mr") || !$("#ed")) return;
  const rise = +$("#mr").value / 100, ed = +$("#ed").value, de = -ed * rise, bill = (1 + rise) * (1 + de) - 1;
  $("#w1").textContent = (de * 100).toFixed(1) + "%"; $("#w2").textContent = (bill >= 0 ? "+" : "") + (bill * 100).toFixed(1) + "%"; $("#w3").textContent = bill > 0.0005 ? "Pay up" : bill < -0.0005 ? "Pay down" : "No change";
  $("#wv").textContent = rise === 0 ? "No change in the minimum wage."
    : ed < 1 ? `Demand for labour is inelastic (${ed.toFixed(1)}): employment falls by ${Math.abs(de * 100).toFixed(1)}%, a smaller percentage than the wage rise, so total pay for low-paid workers rises by ${(bill * 100).toFixed(1)}% even though some jobs are lost.`
    : ed === 1 ? "Unit elastic: the fall in jobs roughly cancels the rise in the wage, so the wage bill barely changes."
    : `Demand for labour is elastic (${ed.toFixed(1)}): employment falls by a larger percentage than the wage rises, so total pay for low-paid workers ${bill < 0 ? "falls" : "changes little"}. Some workers gain, but as a group they lose.`;
  const H = (v) => 90 * (Math.abs(v) / 0.5), bw = 90, base = 130;
  let o = SV.line(30, base, 400, base);
  [[60, de, "Employment"], [230, bill, "Wage bill"]].forEach(([x, v, l]) => { o += SV.rect(x, v >= 0 ? base - H(v) : base, bw, H(v), v >= 0 ? "f3" : "f2") + SV.text(x + bw / 2, v >= 0 ? base - H(v) - 8 : base + H(v) + 16, (v >= 0 ? "+" : "−") + Math.abs(v * 100).toFixed(1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, 242, l, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g7"), { id: "mr", label: "Rise in the minimum wage: ", min: 0, max: 50, step: 5, value: 20, fmt: (v) => "+" + v + "%", onInput: lab4 });
Lib.slider($("#g8"), { id: "ed", label: "Elasticity of demand for labour (size): ", min: 0, max: 2, step: 0.1, value: 0.5, fmt: (v) => v.toFixed(1), onInput: lab4 });
lab2(); lab3();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Who is likely to gain, lose, or be affected in different ways by a binding minimum wage in a competitive market?",
  buckets: [{ label: "Likely to gain" }, { label: "Likely to lose" }, { label: "Depends" }],
  items: [
    { text: "Low-paid workers who keep their jobs", b: 0 }, { text: "Workers whose hours are protected by a higher hourly wage", b: 0 },
    { text: "Workers who lose their jobs", b: 1 }, { text: "People looking for work who cannot find a job", b: 1 }, { text: "Employers' profit margins", b: 1 },
    { text: "Consumers (prices may rise)", b: 2 }, { text: "The government's budget", b: 2 }, { text: "Workers in a monopsony", b: 2 }, { text: "Firms whose workers become more productive", b: 2 },
  ], done: "There are winners and losers, and the answer depends on the market and the level of the minimum.",
});
Lib.classify($("#cl2"), {
  prompt: "Which market does each statement describe?",
  buckets: [{ label: "Competitive labour market" }, { label: "Monopsony" }, { label: "Both" }],
  items: [
    { text: "A binding minimum wage cuts employment", b: 0 }, { text: "A minimum wage in a range can raise employment", b: 1 },
    { text: "The wage before the minimum is below MRP", b: 1 }, { text: "The wage is set where demand equals supply", b: 0 },
    { text: "MCL becomes flat at the minimum wage until supply runs out", b: 1 },
    { text: "A minimum wage below the market wage has no effect", b: 2 }, { text: "Higher pay may raise productivity", b: 2 },
  ], done: "Only above the competitive wage does a minimum wage cost jobs in both cases.",
});
Lib.order($("#o1"), { prompt: "Put the analysis of a minimum wage in a competitive labour market in order.", items: [
  "Draw demand (MRP) and supply of labour and find the equilibrium wage and employment",
  "Draw the minimum wage above the equilibrium wage so that it is binding",
  "At the minimum wage the quantity demanded of labour falls",
  "At the minimum wage the quantity supplied of labour rises",
  "Supply exceeds demand, so there is unemployment",
  "Evaluate: elasticity of demand, size of the minimum, productivity effects, who gains and loses",
], done: "A reliable exam routine." });
Lib.match($("#mt1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Minimum wage", "A legal floor on the hourly wage"],
  ["Binding minimum wage", "A minimum set above the market wage, so it changes the outcome"],
  ["Equilibrium wage", "The wage where the quantity of labour demanded equals the quantity supplied"],
  ["Unemployment from a minimum wage", "Quantity of labour supplied minus quantity demanded at the minimum"],
  ["Monopsony wage", "The wage a single buyer of labour pays, below the competitive wage"],
  ["Wage bill", "Wage multiplied by the number of workers employed"],
  ["Elasticity of demand for labour", "How responsive employment is to a change in the wage"],
  ["Substitutability of capital", "How easily machines can replace workers"],
], done: "Eight terms for the minimum wage." });
Lib.calc($("#c1"), { qs: [
  { q: "Demand for labour: L = 200 − 10W. Supply: L = 10W − 40 (L in thousands, W in $). A minimum wage of $14 is set. How many thousand workers are unemployed?", a: 40, hint: "Find L demanded and L supplied at W = 14.", sol: "Demand: 200 − 140 = 60. Supply: 140 − 40 = 100. Unemployment = 100 − 60 = <b>40 thousand</b>." },
  { q: "In that market the equilibrium is $12 and 80 thousand. Employment falls from 80 to 60 thousand at the $14 minimum. What is the percentage fall in employment (%)?", a: 25, sol: "(80 − 60) ÷ 80 × 100 = <b>25%</b>." },
  { q: "The wage rises from $12 to $14. What is the percentage rise in the wage (%, 1 decimal place)?", a: 16.7, tol: 0.1, sol: "(14 − 12) ÷ 12 × 100 = <b>16.7%</b>." },
  { q: "Calculate the elasticity of demand for labour between the two points (include the sign).", a: -1.5, tol: 0.02, sol: "−25% ÷ 16.7% = <b>−1.5</b>: elastic, so the wage bill falls." },
  { q: "What is the change in the wage bill (wage × employment), in $ thousand per hour?", a: -120, hint: "Before: 12 × 80. After: 14 × 60.", sol: "Before 960, after 840: change = <b>−120</b>." },
  { q: "A monopsony has MRP = 20 − 0.1L and supply W = 2 + 0.1L (L in thousands). It pays $8 and employs 60 thousand. A minimum wage of $10 is set. How many thousand are employed?", a: 80, hint: "Supply at $10 is (10 − 2) × 10. MRP = 10 gives 100. Take the smaller.", sol: "Supply at $10 = 80, MRP gives 100. Employment is the smaller, <b>80 thousand</b>: employment rises from 60." },
  { q: "In the same monopsony a minimum wage of $7 is set. How many thousand are employed?", a: 60, sol: "$7 is below the monopsony wage of $8, so it has no effect: employment stays at <b>60 thousand</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A minimum wage set above equilibrium in a competitive labour market is likely to cause:", opts: ["Excess demand for labour", "Unemployment", "Higher employment", "A fall in labour supply"], a: 1, why: "The quantity of labour supplied rises and the quantity demanded falls." },
  { q: "Which minimum wage could raise both the wage and employment?", opts: ["Below the monopsony wage", "Between the monopsony wage and the competitive wage", "Above the competitive wage", "Any minimum wage"], a: 1, why: "In that range the firm is forced to pay more but still wants to hire up to the point where supply runs out." },
  { q: "A minimum wage set below the equilibrium wage in a competitive market will:", opts: ["cause unemployment", "have no effect", "raise wages", "cause a shortage of labour"], a: 1, why: "It is not binding, so the market wage stays above it." },
  { q: "Job losses from a minimum wage are likely to be smaller when:", opts: ["Demand for labour is elastic", "Machines are cheap substitutes", "Demand for labour is inelastic", "The minimum rise is very large"], a: 2, why: "If demand is inelastic, employment falls by a smaller percentage than the wage rises." },
  { q: "Which is an argument for a minimum wage?", opts: ["It may raise productivity and reduce poverty", "It always raises employment", "It lowers firms' costs", "It reduces the supply of labour"], a: 0, why: "Higher pay may raise effort and reduce turnover, and raises the pay of low-paid workers who stay in work." },
  { q: "A minimum wage may not target the poorest households because:", opts: ["The poorest all earn the minimum wage", "Many low-paid workers live in households with other income, and the poorest may have no job", "It is always too low", "It raises benefits"], a: 1, why: "Targeting is imperfect: it helps workers, not the unemployed." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Minimum wage", "A legal floor on the hourly wage employers may pay."],
  ["Binding (effective) minimum wage", "One set above the market wage so that it changes the outcome."],
  ["Competitive labour market effect", "A binding minimum cuts quantity demanded, raises quantity supplied: unemployment."],
  ["Monopsony effect", "A minimum between the monopsony and competitive wages raises wage and employment."],
  ["Unemployment from the minimum", "Quantity of labour supplied minus quantity demanded at the minimum wage."],
  ["Insiders and outsiders", "Workers who keep their jobs at the higher wage versus those who lose out."],
  ["Wage bill", "Wage multiplied by employment."],
  ["Elasticity and the minimum wage", "The less elastic the demand for labour, the smaller the job loss."],
  ["Productivity effect", "Higher pay may raise effort and cut turnover, shifting MRP right."],
  ["Substitutability of capital", "The easier machines replace labour, the greater the job losses."],
  ["Targeting", "A minimum wage helps workers, not the unemployed, and not only the poor."],
  ["Alternatives", "Tax credits, training subsidies, anti-discrimination law."],
] });

/* ---------- Past paper MCQ (text) ---------- */
Lib.quiz($("#qz2"), { qs: [
  { q: "[Oct/Nov 2024 · 32 · Q12] In which situation is the introduction of a minimum wage most likely to raise employment opportunities as well as wages?", opts: ["Firms face intense competition both at home and abroad.", "Labour costs are a high proportion of the total cost of the firm.", "The minimum wage is not high enough to lower the profits of the firms.", "The minimum wage introduced in monopsony is less than the marginal revenue productivity (MRP) of the last worker employed."], a: 3, why: "In a monopsony a minimum wage below the MRP of the last worker raises both the wage and employment. A and B make job losses more likely, and C describes a minimum that is probably not binding." },
  { q: "[May/June 2025 · 34 · Q11] What determines the amount by which employment is reduced if a minimum wage is set 5% above the equilibrium market wage?", opts: ["the average revenue product curve", "the marginal revenue product curve", "the mobility of labour", "the wage rate in other industries"], a: 1, why: "The MRP curve is the demand for labour, and its elasticity (slope) decides how many jobs are lost when the wage rises." },
] });
