const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}

function spChart(s) {
  const base = 320, k = 2.6; let o = SV.line(60, base, 710, base) + SV.text(60, 28, "Total output of the two countries together", "sm");
  const grp = (x, label, parts, tot, op) => { let y = base, g = `<g opacity="${op}">`; parts.forEach(([n, v, c]) => { const h = v * k; y -= h; g += SV.rect(x, y, 90, h, "", { style: `fill:var(${c});stroke:var(--surface);stroke-width:2`, opacity: 0.85 }); if (h > 16) g += SV.text(x + 45, y + h / 2 + 5, n + " " + v, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:12px" }); }); return g + SV.text(x + 45, base - tot * k - 8, tot, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 45, base + 20, label, "sm", { "text-anchor": "middle" }) + "</g>"; };
  o += grp(90, "Wheat before", [["A", 50, "--accent"], ["B", 30, "--warn"]], 80, s.b) + grp(200, "Wheat after", [["A", 100, "--accent"]], 100, s.a) + grp(380, "Cars before", [["A", 25, "--accent"], ["B", 30, "--warn"]], 55, s.b) + grp(490, "Cars after", [["B", 60, "--warn"]], 60, s.a);
  if (s.t) o += SV.text(380, 54, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Specialisation raises total output", base: { b: 0, a: 0, t: "" }, draw: spChart, steps: [
  { cap: "Country <b>A</b> can make 100 tonnes of wheat <b>or</b> 50 cars. Country <b>B</b> can make 60 tonnes of wheat <b>or</b> 60 cars. <b>Before specialising</b> each splits its resources evenly.", s: { b: 1, a: 0, t: "" } },
  { cap: "Together they make <b>80 tonnes of wheat and 55 cars</b>.", s: { b: 1, a: 0, t: "Before: 80 wheat, 55 cars" } },
  { cap: "A gives up 1 car for 2 tonnes of wheat; B gives up only 1 tonne for 1 car. A has the <b>lower opportunity cost of wheat</b>, B of cars. So <b>A specialises in wheat</b> and <b>B in cars</b>.", s: { b: 1, a: 1, t: "After specialising" } },
  { cap: "Now they make <b>100 tonnes of wheat and 60 cars</b>: more of <b>both</b>. By trading, each can consume more than before. That is the gain from specialisation and trade.", s: { b: 1, a: 1, t: "After: 100 wheat, 60 cars" } },
] });
const SB = ["Workers and firms focus on one product", "They gain skills and use machinery more fully", "Productivity rises and average costs fall (economies of scale)", "Prices are lower and quality higher: more competitive", "More is exported: higher revenue, profit and jobs", "Higher income and growth for the country"];
Lib.stepper($("#stB"), { w: 760, h: 400, label: "How specialisation benefits a country", base: { n: 0 }, draw: mkChain(SB, "--good"), steps: chainSteps(["Workers and firms <b>focus on one product</b>.", "They gain <b>skills</b> and use machinery more fully.", "<b>Productivity rises</b> and average costs fall, with economies of scale.", "<b>Prices are lower</b> and quality is higher, so exports are more competitive.", "<b>More is exported</b>: higher revenue, profit and jobs.", "Higher <b>income and growth</b> for the country."]) });
function riskChart(s) {
  const price = [100, 100, 60, 70, 95, 100], yrs = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6"], X = (i) => 100 + i * 112, Y = (v) => 330 - (v - 40) * 3.5;
  const earn = (sh) => price.map((p) => 100 * (1 - sh) + sh * p);
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 710, 340) + SV.text(86, 48, "Export earnings (index)", "sm");
  [50, 75, 100].forEach((v) => (o += SV.line(80, Y(v), 710, Y(v), "gr") + SV.text(72, Y(v) + 4, v, "sm", { "text-anchor": "end" })));
  yrs.forEach((y, i) => (o += SV.text(X(i), 358, y, "sm", { "text-anchor": "middle" })));
  [[0.2, "c1", "Diversified (20% from main product)", "dot1"], [0.9, "c2", "Specialised (90% from one product)", "dot2"]].forEach(([sh, cl, lbl, dt], j) => { const e = earn(sh), pts = []; for (let i = 0; i <= Math.min(5, Math.floor(s.n)); i++) pts.push([X(i), Y(e[i])]); if (pts.length > 1) o += SV.path(ptsPath(pts), cl, { "stroke-width": 3 }); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, dt))); if (s.n >= 1) o += SV.text(660, j ? 84 : 62, lbl, "lbl bd " + (j ? "t2" : "t1"), { "text-anchor": "end", style: "font-size:13px" }); });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "The risk of depending on one product", base: { n: 0 }, draw: riskChart, steps: [
  { cap: "Two countries. One <b>specialises</b>: 90% of its export earnings come from a single product. The other is <b>diversified</b>: only 20% comes from its main product.", s: { n: 1 } },
  { cap: "Prices of the main product are steady for two years: both earn the same.", s: { n: 2 } },
  { cap: "Then the <b>world price of the main product falls 40%</b>. The diversified country's earnings fall only a little; the specialised country's earnings <b>fall by about a third</b>, with a risk of job losses and a government budget crisis.", s: { n: 3 } },
  { cap: "Prices recover slowly. <b>Evaluate:</b> specialisation raises income when prices are good, but exposes the country to price swings and shocks. Diversifying reduces the risk.", s: { n: 6 } },
] });

/* Lab 1: allocation */
function labA() {
  if (!$("#aa") || !$("#ab")) return;
  const a = +$("#aa").value / 100, b = +$("#ab").value / 100, wheat = 100 * (1 - a) + 60 * (1 - b), cars = 50 * a + 60 * b, base = 80, baseC = 55;
  $("#aa1").textContent = money(wheat, 0) + " t"; $("#aa2").textContent = money(cars, 0); $("#aa3").textContent = wheat >= 100 && cars >= 60 ? "Best" : wheat >= 80 && cars >= 55 ? "Better than even split" : "Worse or equal";
  $("#aav").textContent = `A puts ${Math.round(a * 100)}% of its resources into cars and B puts ${Math.round(b * 100)}%. Total output is ${money(wheat, 0)} tonnes of wheat and ${money(cars, 0)} cars. ${wheat >= 100 && cars >= 60 ? "This is full specialisation by comparative cost: A makes wheat, B makes cars: more of both than the even split (80 wheat, 55 cars)." : a > 0.99 ? "A is making cars, but A is worse at cars than B. Try swapping." : "Try putting A at 0% cars and B at 100% cars."}`;
  const base0 = 290, k = 2.2; let o = SV.line(60, base0, 700, base0);
  [["Wheat (tonnes)", wheat, "--accent", 100], ["Cars", cars, "--warn", 60]].forEach(([n, v, c, best], i) => { const x = 140 + i * 280; o += SV.rect(x, base0 - v * k, 130, v * k, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.rect(x, base0 - best * k, 130, best * k, "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4" }) + SV.text(x + 65, base0 - v * k - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base0 + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o + SV.text(60, 24, "Dashed outline: output with full specialisation", "sm");
}
Lib.slider($("#g1"), { id: "aa", label: "Share of A's resources used for cars", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "ab", label: "Share of B's resources used for cars", min: 0, max: 100, step: 10, value: 50, fmt: (v) => v + "%", onInput: labA });
/* Lab 2: dependency */
function labD() {
  if (!$("#da") || !$("#db")) return;
  const sh = +$("#da").value / 100, fall = +$("#db").value / 100, loss = sh * fall;
  $("#da1").textContent = "−" + money(loss * 100, 1) + "%"; $("#da2").textContent = "$" + money(100 * (1 - loss), 0) + "bn"; $("#da3").textContent = loss > 0.2 ? "Severe" : loss > 0.08 ? "Moderate" : "Small";
  $("#dav").textContent = `If ${Math.round(sh * 100)}% of export earnings come from one product and its price falls ${Math.round(fall * 100)}%, total export earnings fall by ${Math.round(sh * 100)}% × ${Math.round(fall * 100)}% = ${money(loss * 100, 1)}%. The more a country depends on one product, the more a price fall hurts. A diversified economy is much safer.`;
  const base = 290; let o = SV.line(80, base, 700, base);
  [["Before", 100, "--accent"], ["After the price fall", 100 * (1 - loss), loss > 0.2 ? "--bad" : "--warn"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * 2.2; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + money(v, 0) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labD").innerHTML = o;
}
Lib.slider($("#g3"), { id: "da", label: "Share of export earnings from the main product", min: 10, max: 90, step: 10, value: 70, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "db", label: "Fall in the world price of that product", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v + "%", onInput: labD });
const BS = [
  { n: "Natural resources and climate", e: "Land, minerals and weather suit some products and not others.", x: "Saudi Arabia (oil), Brazil (coffee), Kenya (cut flowers)" },
  { n: "Low-cost, plentiful labour", e: "Labour-intensive goods can be made cheaply.", x: "Bangladesh and Vietnam (clothing, footwear)" },
  { n: "Skilled labour and education", e: "A skilled workforce makes complex goods and services.", x: "India (IT services), Switzerland (watches, finance)" },
  { n: "Capital and technology", e: "Machinery and infrastructure raise productivity.", x: "Germany (machinery), South Korea (electronics)" },
  { n: "Economies of scale", e: "Large markets and output lower average costs.", x: "China (large-scale manufacturing)" },
  { n: "Government policy and investment", e: "Spending on education and infrastructure, or tax incentives, build new strengths.", x: "Singapore (finance and logistics)" },
];
button_table("bsBtns", "bsOut", BS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Why it leads to specialisation</th><th>Example</th></tr><tr><td>${p.e}</td><td>${p.x}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each an <b>advantage</b> or a <b>disadvantage</b> of specialisation?", buckets: [{ label: "Advantage" }, { label: "Disadvantage" }], items: [
  { text: "Workers gain skills and productivity", b: 0 }, { text: "Lower average costs from economies of scale", b: 0 }, { text: "Higher output and quality", b: 0 }, { text: "Export earnings create jobs and income", b: 0 },
  { text: "Over-dependence on a few products", b: 1 }, { text: "A fall in world price causes a sharp fall in income", b: 1 }, { text: "Dependence on imports for other goods", b: 1 }, { text: "Structural unemployment if the main industry declines", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "What is the likely <b>basis for specialisation</b> in each case?", buckets: [{ label: "Natural resources or climate" }, { label: "Cheap or skilled labour" }, { label: "Capital and technology" }], items: [
  { text: "A country with large oil reserves exports oil", b: 0 }, { text: "A tropical country grows coffee and bananas", b: 0 },
  { text: "A country with many low-paid workers makes clothing", b: 1 }, { text: "A country with highly trained programmers sells IT services", b: 1 },
  { text: "A country with advanced factories makes machinery and cars", b: 2 }, { text: "A country with modern infrastructure and technology exports electronics", b: 2 },
], done: "Resources, labour, capital." });
Lib.classify($("#cl3"), { prompt: "Is each a reason a country may <b>change</b> its specialisation?", buckets: [{ label: "Yes, a reason to change" }, { label: "Not a reason" }], items: [
  { text: "Its main resource is running out", b: 0 }, { text: "Education and technology improve", b: 0 }, { text: "Wages rise, so labour-intensive goods cost more", b: 0 }, { text: "World demand for its product falls", b: 0 },
  { text: "It keeps the same costs and demand for decades", b: 1 }, { text: "Nothing changes in the world market", b: 1 },
], done: "Costs, resources, technology, demand." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Specialisation by country", "A country concentrating on producing a limited range of goods and services"],
  ["Opportunity cost", "The next best alternative given up"],
  ["Economies of scale", "Lower average costs as output rises"],
  ["Diversification", "Producing a wider range of goods to reduce risk"],
  ["Export", "A good or service sold to another country"],
  ["Import", "A good or service bought from another country"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why specialisation is risky</b>.", items: [
  "A country depends on one product for most of its exports",
  "The world price of that product falls",
  "Export earnings fall sharply",
  "Firms cut output and workers lose jobs",
  "Government tax revenue falls and the economy suffers",
], done: "Over-dependence." });
Lib.calc($("#c1"), { qs: [
  { q: "Country A can make 40 shirts or 20 phones. How many shirts does it give up for each phone?", a: 2, hint: "Compare the two choices.", sol: "40 ÷ 20 = <b>2 shirts</b>." },
  { q: "Country B can make 30 shirts or 30 phones. How many shirts does it give up for each phone?", a: 1, sol: "30 ÷ 30 = <b>1 shirt</b>. B has the lower opportunity cost of phones, so B should make phones." },
  { q: "Oil is 80% of a country's export earnings of $50bn. The oil price falls 25%. By how much do total export earnings fall ($bn)?", a: 10, sol: "80% × 50 = $40bn from oil. 25% × 40 = <b>$10bn</b>." },
  { q: "A country exports $60bn of goods, of which $45bn is one product. What percentage of exports is that product?", a: 75, sol: "45 ÷ 60 × 100 = <b>75%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is specialisation by country?", opts: ["A country producing everything it needs", "A country concentrating on producing a limited range of goods and services", "A country banning imports", "A country with no exports"], a: 1, why: "Concentrating on what it does best." },
  { q: "Which is an advantage of specialisation?", opts: ["Over-dependence on one product", "Lower costs through skills and economies of scale", "Higher import dependence", "More risk from price falls"], a: 1, why: "Productivity and costs improve." },
  { q: "Which is a disadvantage of specialisation?", opts: ["Higher productivity", "Dependence on a few products", "Lower costs", "Higher output"], a: 1, why: "A price fall can hit income hard." },
  { q: "A country should specialise in goods with the:", opts: ["Highest opportunity cost", "Lowest opportunity cost", "Highest tariffs", "Lowest quality"], a: 1, why: "Lowest opportunity cost: it gives up least." },
  { q: "Which could make a country change its specialisation?", opts: ["New technology and education", "Unchanged costs", "No change in demand", "Fixed resources"], a: 0, why: "The pattern of what it can do best changes." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Specialisation by country", "A country concentrating its resources on producing a limited range of goods and services."],
  ["Opportunity cost", "The next best alternative given up when a choice is made."],
  ["Economies of scale", "Lower average costs from producing on a larger scale."],
  ["Diversification", "Producing a wider range of goods and services to reduce risk."],
  ["Exports", "Goods and services sold to other countries."],
  ["Imports", "Goods and services bought from other countries."],
  ["Over-dependence", "Relying too much on one product or one market."],
  ["Resource allocation", "How a country uses its scarce resources among competing uses."],
  ["Structural unemployment", "Unemployment caused by the decline of an industry and a mismatch of skills."],
] });
labA(); labD();
