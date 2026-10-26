/* ---------- model: demand P = 100 - Q, supply P = 20 + Q (equilibrium Q = 40, P = 60) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const X = (q) => 70 + q * 7.5, Y = (p) => 330 - p * 3;
const axes = () => SV.line(70, 330, 750, 330) + SV.line(70, 330, 70, 20) + SV.text(750, 358, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price ($)", "sm");
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const marketLines = (s) => (s.d > 0 ? SV.line(X(0), Y(100), X(90), Y(10), "c1", op(s.d)) + SV.text(X(90) - 4, Y(10) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) : "") +
  (s.s > 0 ? SV.line(X(0), Y(20), X(80), Y(100), "c2", op(s.s)) + SV.text(X(80) - 4, Y(100) + 16, "S", "lbl bd t2", { "text-anchor": "end", ...op(s.s) }) : "");
const eqMark = (s) => s.eq > 0 ? SV.line(X(40), Y(60), X(40), 330, "gr", op(s.eq)) + SV.line(70, Y(60), X(40), Y(60), "gr", op(s.eq)) + SV.circle(X(40), Y(60), 6, "dot3", op(s.eq)) + SV.text(66, Y(60) + 4, "60", "sm bd", { "text-anchor": "end", ...op(s.eq) }) + SV.text(X(40), 350, "40", "lbl bd", { "text-anchor": "middle", ...op(s.eq) }) : "";


/* ---------- natural monopoly: MC 20, fixed cost 800, D: P = 100 - Q ---------- */
const NX = (q) => 70 + q * 6.8, NY = (p) => 330 - p * 3, AC = (q) => 20 + 800 / q;
function nmBase(s) {
  const acPts = []; for (let q = 10; q <= 100; q += 2) acPts.push([NX(q), NY(AC(q))]);
  return axes() + SV.line(NX(0), NY(100), NX(100), NY(0), "c1", op(s.d)) + SV.line(NX(0), NY(100), NX(50), NY(0), "c3", op(s.d)) + SV.line(NX(0), NY(20), NX(100), NY(20), "c2", op(s.d)) + SV.path(ptsPath(acPts), "c4", op(s.d)) +
    SV.text(NX(100) - 4, NY(0) - 8, "D", "lbl bd t1", { "text-anchor": "end", ...op(s.d) }) + SV.text(NX(50) + 6, NY(0) - 8, "MR", "lbl bd t3", op(s.d)) + SV.text(NX(100) - 4, NY(28) - 8, "AC", "lbl bd t4", { "text-anchor": "end", ...op(s.d) }) + SV.text(NX(100) - 4, NY(20) + 18, "MC", "lbl bd t2", { "text-anchor": "end", ...op(s.d) });
}
const nmPoint = (q, p, pl, ql, o, c) => SV.line(NX(q), NY(p), NX(q), 330, "gr", op(o)) + SV.line(70, NY(p), NX(q), NY(p), "gr", op(o)) + SV.circle(NX(q), NY(p), 6, c, op(o)) + SV.text(66, NY(p) + 4, pl, "sm bd", { "text-anchor": "end", ...op(o) }) + SV.text(NX(q), 350, ql, "lbl bd", { "text-anchor": "middle", ...op(o) });
function nmDraw(s) {
  let o = nmBase(s);
  if (s.u > 0) o += SV.rect(70, NY(60), NX(40) - 70, NY(40) - NY(60), "f3", op(s.u)) + nmPoint(40, 60, "60", "40", s.u, "dot3") + SV.text(NX(20), NY(50) + 4, "profit 800", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.u) });
  if (s.c1 > 0) o += SV.rect(70, NY(30), NX(80) - 70, NY(20) - NY(30), "f2", op(s.c1)) + nmPoint(80, 20, "20", "80", s.c1, "dot2") + SV.text(NX(40), NY(25) + 4, "loss 800", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.c1) });
  if (s.c2 > 0) o += nmPoint(68.3, 31.7, "31.7", "68", s.c2, "dot1") + SV.text(NX(34), NY(31.7) - 10, "cap = AC: normal profit", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.c2) });
  return o;
}
Lib.stepper($("#stN"), { w: 780, h: 370, label: "A natural monopoly with a price cap at marginal cost and at average cost", base: { d: 0, u: 0, c1: 0, c2: 0 }, draw: nmDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A natural monopoly.</b> A big fixed cost ($800) means average cost (AC) keeps falling as output rises, so one firm is cheapest. Marginal cost (MC) is $20 and demand is P = 100 − Q.", s: { d: 1 } },
  { cap: "<b>Left alone.</b> The monopolist produces where MR = MC: <b>40 units at $60</b>, above average cost of $40. The shaded box is a supernormal profit of $20 × 40 = <b>$800</b>. Price is well above marginal cost, so output is too low.", s: { d: 1, u: 1 } },
  { cap: "<b>Cap at marginal cost ($20).</b> Output rises to <b>80</b> and price equals MC: allocative efficiency. But AC at 80 is $30, so the firm loses $10 a unit, <b>$800</b> in all. It may need a subsidy or leave.", s: { d: 1, c1: 1 } },
  { cap: "<b>Cap at average cost ($31.70).</b> Where D meets AC output is about <b>68</b>. The firm earns only normal profit, so it stays in business, and consumers get more output at a lower price. Regulators rarely know the true AC curve, though.", s: { d: 1, c2: 1 } },
] });

/* ---------- default effect ---------- */
function defDraw(s) {
  let o = SV.line(60, 250, 740, 250) + SV.text(62, 24, "Share of people who are donors", "sm");
  const H = (v) => 2.2 * v;
  if (s.a > 0) o += SV.rect(180, 250 - H(30) * s.a, 130, H(30) * s.a, "f2", op(s.a)) + SV.text(245, 250 - H(30) * s.a - 8, "30%", "lbl bd", { "text-anchor": "middle", ...op(s.a) });
  if (s.b > 0) o += SV.rect(440, 250 - H(80) * s.b, 130, H(80) * s.b, "f3", op(s.b)) + SV.text(505, 250 - H(80) * s.b - 8, "80%", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  o += SV.text(245, 274, "Opt-in", "lbl bd", { "text-anchor": "middle", ...op(s.a) }) + SV.text(505, 274, "Opt-out", "lbl bd", { "text-anchor": "middle", ...op(s.b) });
  return o;
}
Lib.stepper($("#stD2"), { w: 780, h: 300, label: "Share of donors under opt-in and opt-out systems in an illustrative model", base: { a: 0, b: 0 }, draw: defDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The set-up.</b> Suppose 60% of people would donate if they made an active choice, and half of all people simply accept whatever the default is. (Illustrative numbers.)", s: { a: 0, b: 0 } },
  { cap: "<b>Opt-in.</b> The default is not to donate. Only those who actively choose and want to donate sign up: 50% × 60% = <b>30%</b>.", s: { a: 1, b: 0 } },
  { cap: "<b>Opt-out.</b> The default is to donate. The 50% who accept the default are donors, and half of the active choosers (60% of 50% = 30%) also donate: <b>80%</b>.", s: { a: 1, b: 1 } },
  { cap: "<b>Same freedom, different outcome.</b> Everyone can still choose, nothing is banned and no price changes, but the default moves the donor rate by 50 percentage points. That is what a <b>nudge</b> does.", s: { a: 1, b: 1 } },
] });

/* ---------- Lab 1: price cap ---------- */
function labN() {
  if (!$("#cap")) return;
  const c = +$("#cap").value, free = c >= 60, p = free ? 60 : c, q = free ? 40 : 100 - c, prof = (p - 20) * q - 800;
  $("#n1").textContent = "$" + p; $("#n2").textContent = q; $("#n3").textContent = (prof >= 0 ? "$" : "−$") + Math.abs(Math.round(prof)); $("#n4").textContent = p === 20 ? "Allocative" : "Not allocative";
  $("#nv").textContent = free ? "The cap is at or above the price the monopolist would charge ($60), so it is not binding: output stays at 40 and profit at $800."
    : c === 20 ? "Price equals marginal cost: output is at the allocatively efficient level of 80. But average cost is $30, so the firm loses $800 and may need a subsidy."
    : prof >= 0 ? `Price falls to $${c} and output rises to ${q}. The firm still earns a profit of $${Math.round(prof)}, so it stays in business, and consumers gain. A lower cap would give them more.`
    : `At $${c} the price is below average cost ($${Lib.fmtN(AC(q), 1)}), so the firm loses $${Math.abs(Math.round(prof))}. In the long run it may leave or need a subsidy. Output is higher, but the service may not be sustainable.`;
  const x = (v) => 40 + v * 3.6, y = (v) => 270 - v * 2.4, acp = []; for (let k = 10; k <= 100; k += 2) acp.push([x(k), y(AC(k))]);
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "Price ($)", "sm");
  o += SV.rect(40, Math.min(y(p), y(AC(q))), x(q) - 40, Math.abs(y(p) - y(AC(q))), prof >= 0 ? "f3" : "f2");
  o += SV.line(x(0), y(100), x(100), y(0), "c1") + SV.line(x(0), y(20), x(100), y(20), "c2") + SV.path(ptsPath(acp), "c4") + SV.line(40, y(p), 400, y(p), free ? "gr" : "c3", { "stroke-width": 3 }) + SV.circle(x(q), y(p), 6, "dot1") + SV.text(x(100) - 4, y(0) - 6, "D", "sm bd t1", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(20) + 16, "MC", "sm bd t2", { "text-anchor": "end" }) + SV.text(x(100) - 4, y(28) - 6, "AC", "sm bd t4", { "text-anchor": "end" });
  $("#labG").innerHTML = o;
}
Lib.slider($("#g8"), { id: "cap", label: "Price cap ($): ", min: 20, max: 70, step: 1, value: 40, fmt: (v) => v, onInput: labN });

/* ---------- Lab 2: defaults ---------- */
function labD() {
  if (!$("#inr") || !$("#sup")) return;
  const f = +$("#inr").value / 100, t = +$("#sup").value / 100, a = (1 - f) * t * 100, b = (f + (1 - f) * t) * 100;
  $("#d1").textContent = Math.round(a) + "%"; $("#d2").textContent = Math.round(b) + "%"; $("#d3").textContent = "+" + Math.round(b - a) + " points";
  $("#dv").textContent = f === 0 ? "If nobody follows the default, the system makes no difference: both give the same donor rate."
    : `With ${Math.round(f * 100)}% accepting the default and ${Math.round(t * 100)}% in favour, opt-in gives ${Math.round(a)}% donors and opt-out ${Math.round(b)}%. The more people go along with defaults, the bigger the effect of the nudge.`;
  const H = (v) => 1.8 * v;
  let o = SV.line(30, 220, 400, 220);
  [[70, a, "f2", "Opt-in"], [240, b, "f3", "Opt-out"]].forEach(([x, v, c, l]) => { o += SV.rect(x, 220 - H(v), 100, H(v), c) + SV.text(x + 50, 220 - H(v) - 8, Math.round(v) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 240, l, "sm", { "text-anchor": "middle" }); });
  $("#labH").innerHTML = o;
}
Lib.slider($("#g9"), { id: "inr", label: "People who just accept the default: ", min: 0, max: 80, step: 10, value: 50, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g10"), { id: "sup", label: "People who would donate if they chose: ", min: 40, max: 80, step: 10, value: 60, fmt: (v) => v + "%", onInput: labD });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "What type of policy is each one?",
  buckets: [{ label: "Regulation and legal limits" }, { label: "Provision and ownership" }, { label: "Information and nudges" }],
  items: [
    { text: "A ban on new petrol cars", b: 0 }, { text: "Emission standards for factories", b: 0 }, { text: "Competition law blocking a merger", b: 0 }, { text: "A price cap on a water company", b: 0 },
    { text: "Free vaccination provided by the state", b: 1 }, { text: "Nationalising the railways", b: 1 }, { text: "Selling a state-owned airline", b: 1 }, { text: "Street lighting provided by the council", b: 1 },
    { text: "Opt-out organ donation", b: 2 }, { text: "Health warnings on cigarette packs", b: 2 }, { text: "Fruit placed at eye level in canteens", b: 2 },
  ], done: "A nudge changes how choices are presented without forcing them; a ban is regulation and a tax is a price tool.",
});
Lib.classify($("#cl2"), {
  prompt: "Is each point an argument for or against privatisation?",
  buckets: [{ label: "For privatisation" }, { label: "Against privatisation" }],
  items: [
    { text: "Competition may cut costs and prices", b: 0 }, { text: "Shareholders scrutinise managers", b: 0 }, { text: "Access to private funds for investment", b: 0 }, { text: "The government stops funding losses and receives sale proceeds", b: 0 },
    { text: "A state monopoly may become a private monopoly", b: 1 }, { text: "Unprofitable but socially valuable services may be cut", b: 1 }, { text: "Natural monopolies cannot easily be made competitive", b: 1 }, { text: "A regulator will still be needed", b: 1 },
  ], done: "Weigh these by asking whether the industry can really become competitive.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Natural monopoly", "An industry where one firm is cheapest because of very high fixed costs"],
  ["Price cap", "A limit on the price a regulated firm may charge"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Nationalisation", "Taking private firms into state ownership"],
  ["Nudge", "A change in how choices are presented that influences behaviour without forcing it"],
  ["Regulatory capture", "When the regulator ends up serving the firms it regulates"],
  ["X-inefficiency", "Costs higher than necessary because of weak pressure to cut them"],
  ["Competition policy", "Laws on mergers and cartels to protect competition"],
], done: "Eight words for regulation, ownership and nudges." });
Lib.order($("#o1"), { prompt: "Put the explanation of price cap regulation of a natural monopoly in order.", items: [
  "A natural monopoly has high fixed costs, so one firm is cheapest",
  "Unregulated, it sets MR = MC, so price is high and output is low",
  "The regulator sets a maximum price below the monopoly price",
  "Output rises and price falls, moving towards allocative efficiency",
  "A cap at marginal cost may leave the firm making a loss; a cap at average cost allows normal profit",
  "Evaluate: the regulator may lack information about costs, and may be influenced by the firm",
], done: "A reliable structure for regulation of monopoly." });
Lib.calc($("#c1"), { qs: [
  { q: "A natural monopoly has MC = $20, a fixed cost of $800 and faces P = 100 − Q. It sets MR = MC, where MR = 100 − 2Q. What quantity does it produce?", a: 40, sol: "100 − 2Q = 20 gives Q = <b>40</b>, and P = $60." },
  { q: "What is its profit ($)?", a: 800, hint: "(P − MC) x Q − fixed cost.", sol: "(60 − 20) x 40 − 800 = <b>$800</b>." },
  { q: "A regulator caps the price at $20. What quantity is demanded?", a: 80, sol: "100 − 20 = <b>80</b>." },
  { q: "What is the firm's profit or loss at the $20 cap ($; use a negative for a loss)?", a: -800, sol: "(20 − 20) x 80 − 800 = <b>−$800</b>." },
  { q: "The cap is set at $36. What is the profit ($)?", a: 224, hint: "Q = 100 − 36 = 64.", sol: "(36 − 20) x 64 − 800 = 1024 − 800 = <b>$224</b>." },
  { q: "In an organ donation model 50% accept the default and 60% of the others would donate. What share are donors under opt-in (%)?", a: 30, sol: "50% x 60% = <b>30%</b>." },
  { q: "What share are donors under opt-out (%)?", a: 80, sol: "50% + 30% = <b>80%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an example of a nudge?", opts: ["A tax on sugary drinks", "A ban on smoking indoors", "An opt-out organ donation system", "A subsidy for fruit"], a: 2, why: "Changing the default influences choice without forcing it." },
  { q: "Privatising a natural monopoly may lead to:", opts: ["perfect competition at once", "a private monopoly that needs regulation", "no change in ownership", "zero profit"], a: 1, why: "Competition is unrealistic on a network, so a regulator is usually needed." },
  { q: "A price cap on a natural monopoly set at marginal cost is likely to:", opts: ["be allocatively efficient but cause a loss", "raise the price", "reduce output", "give supernormal profit"], a: 0, why: "P = MC is efficient, but average cost is above marginal cost, so the firm loses money." },
  { q: "X-inefficiency means:", opts: ["costs are higher than necessary", "output is too high", "prices are below cost", "there is perfect competition"], a: 0, why: "Weak pressure to control costs lets average cost rise above the minimum possible." },
  { q: "Public goods are best provided by the state because:", opts: ["firms can easily charge for them", "free riders make private supply unprofitable", "demand is always elastic", "they have no external benefits"], a: 1, why: "Non-excludability means people can use them without paying." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Production quota", "A legal limit on the quantity produced or sold; supply is fixed at the quota."],
  ["Prohibition", "An outright ban on producing, selling or using a good."],
  ["Licence", "Permission needed to produce or sell; the number of licences may be limited."],
  ["Deregulation", "Removing rules that restrict entry or competition, to encourage new firms."],
  ["Property rights", "Legal ownership or use of an asset, letting owners stop others imposing costs or charge them."],
  ["Regulation", "Legal rules such as bans, standards, price caps and competition law."],
  ["Competition policy", "Laws on mergers and cartels to protect competition."],
  ["Natural monopoly", "A market where one firm is cheapest because of very high fixed costs."],
  ["Price cap", "A maximum price set by a regulator for a monopoly."],
  ["State provision", "The government supplies the good, funded from taxation."],
  ["Nationalisation", "Taking private firms into state ownership."],
  ["Privatisation", "Selling state-owned firms to the private sector."],
  ["X-inefficiency", "Costs higher than necessary through lack of competitive pressure."],
  ["Nudge", "A change in the presentation of choices that influences behaviour without forcing it."],
  ["Regulatory capture", "When regulators serve the interests of the firms they regulate."],
  ["Cross-subsidisation", "Charging high prices to some consumers to fund low prices for others."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2022 · 31 · Q10] In which circumstance would direct provision of a product by the government be least likely?", opts: ["when fixed costs are very high", "when the demand for the product is very high but unit costs are low", "when the industry faces large natural barriers to entry", "when the minimum efficient scale of production is above the level of demand at current prices"], a: 1, why: "Direct provision is most likely where private firms would not enter (high fixed costs, natural barriers, small demand). High demand and low unit costs mean private firms would supply it." },
  { q: "[May/June 2022 · 31 · Q15] What is an example of 'nudge' theory when applied to encouraging healthy eating?", opts: ["advertising the benefits of healthy eating", "increasing tax on sugary foods", "introducing a subsidy for fruit growers", "supermarkets putting fruit near cash registers"], a: 3, why: "A nudge changes how choices are presented without forcing them. Advertising is information, a tax and subsidy are price tools." },
  { q: "[Feb/March 2022 · 32 · Q14] What would be an example of 'nudge' theory?", opts: ["a subsidy on fresh fruit to increase demand", "a unit tax on unhealthy food to reduce demand", "banning all unhealthy food to reduce demand", "putting fresh fruit at eye level in shops to increase demand"], a: 3, why: "Placing fruit at eye level changes the choice environment but leaves people free." },
  { q: "[May/June 2022 · 32 · Q14] What is not an example of the application of 'nudge' theory?", opts: ["A chain of coffee shops offers its customers a larger coffee if they bring their own reusable cup.", "A government imposes an indirect tax on the purchase of sugary snacks, to try to reduce childhood obesity.", "A government introduces an opt-out system for organ donation, to try to increase the number of organs donated.", "A restaurant chain introduces smaller-sized main courses on its menu, to try to reduce the amount of food wasted."], a: 1, why: "A tax changes the price (and the budget), so it is not a nudge." },
  { q: "[May/June 2023 · 31 · Q12] One reason for market failure is the existence of public goods. Which policy option is appropriate for addressing such a market failure?", opts: ["direct provision of the good by the government", "provision of detailed information to consumers", "subsidising firms that currently produce the good", "the adoption of maximum price controls"], a: 0, why: "The free-rider problem means the market will not supply public goods, so the state provides them." },
  { q: "[May/June 2023 · 31 · Q13] In 2020, the governor of California issued an order to ban the sale of new vehicles from 2035 that are powered by petrol or diesel fuel. Which type of government policy is this?", opts: ["a nudge", "a permit to pollute", "nationalisation", "regulation"], a: 3, why: "A legal ban is regulation." },
  { q: "[Feb/March 2020 · 32 · Q12] A government divides a nationalised rail service and sells it to five private companies. The largest dominates the four smaller companies. How will these changes affect the market structure for rail services?", opts: ["It will change from monopoly to monopolistic competition.", "It will create an oligopoly with the possibility of price leadership.", "It will encourage freedom of entry due to lower capital costs.", "It will guarantee ticket prices based on average costs."], a: 1, why: "Five firms with one dominant firm form an oligopoly in which the large firm may act as price leader." },
] });
