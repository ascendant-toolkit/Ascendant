const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl) {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, "Strength of the case: " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

const exLab = { x: "Quantity of currency", y: "Exchange rate", D1: "D", D2: "D1", S1: "S", S2: "S1", P1: "R", Q1: "Q", P2: "R1", Q2: "Q1" };
function exDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }, exLab); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in demand for a currency lowers the exchange rate">${exDraw({ d: -20, s: 0, n: 1 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A fall in demand for the currency lowers the exchange rate", base: { d: 0, s: 0, n: 0 }, draw: exDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The demand for and supply of the currency meet at an exchange rate of 50.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Demand falls</b>, for example because foreigners buy fewer of the country's exports. The demand curve shifts left.", s: { d: -20, s: 0, n: 1 } },
  { cap: "<b>The exchange rate falls</b> to 42: a <b>depreciation</b>. Exports now look cheaper abroad and imports dearer at home.", s: { d: -20, s: 0, n: 1 } },
  { cap: "<b>Alternatively, supply rises</b> (more imports or higher interest rates abroad). The supply curve shifts right and the rate also falls to 42.", s: { d: 0, s: 20, n: 1 } },
] });

function pegDraw(s) {
  const d = s.d, qd = d + 50, qs = 50, e = sdEq(d, 0);
  let o = sdPlot({ d: d, s: 0, g: 0, n: 1 }, exLab) + SV.line(70, SDY(50), 720, SDY(50), "c3", { "stroke-width": 2.5, ...op(s.k) }) + tag(724, SDY(50) - 6, "Fixed rate", "c3", s.k, "end");
  if (s.k > 0 && d < -0.5) o += SV.line(SDX(qd), SDY(50) + 16, SDX(qs), SDY(50) + 16, "c4", { "stroke-width": 3, ...op(s.k) }) + SV.text(SDX((qd + qs) / 2), SDY(50) + 32, "Excess supply: bank buys " + Lib.fmtN(qs - qd, 0), "sm", { "text-anchor": "middle", ...op(s.k) });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A central bank defends a fixed exchange rate", base: { d: 0, k: 0 }, draw: pegDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The rate is fixed at 50</b>, which is the market rate at the start.", s: { d: 0, k: 1 } },
  { cap: "<b>Demand for the currency falls</b>, for example after a rise in the current account deficit. At the fixed rate the supply of the currency exceeds demand.", s: { d: -20, k: 1 } },
  { cap: "<b>The central bank buys the surplus currency</b> using its foreign currency reserves (20 units here), and may raise interest rates, until demand matches supply at 50.", s: { d: -20, k: 1 } },
  { cap: "<b>The limit:</b> reserves are finite. If they run low, the country may have to devalue or accept higher interest rates.", s: { d: -20, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const d = +$("#g1v").value, s = +$("#g2v").value, e = sdEq(d, s);
  $("#r1").textContent = Lib.fmtN(e.p, 1); $("#r2").textContent = Lib.fmtN(e.q, 1);
  const ch = e.p - 50;
  $("#rv").textContent = Math.abs(ch) < 0.5 ? "The exchange rate is roughly unchanged at 50." : (ch < 0 ? "Depreciation" : "Appreciation") + `: the rate moves from 50 to ${Lib.fmtN(e.p, 1)}. ` + (d < -0.5 ? "Demand for the currency has fallen (e.g. fewer exports or lower interest rates). " : d > 0.5 ? "Demand for the currency has risen (e.g. more exports or higher interest rates). " : "") + (s > 0.5 ? "Supply has risen (e.g. more imports or higher foreign interest rates)." : s < -0.5 ? "Supply has fallen (e.g. fewer imports)." : "");
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 }, exLab);
}
Lib.slider($("#g1"), { id: "g1v", label: "Shift in demand for the currency ", min: -30, max: 30, step: 5, value: -20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Shift in supply of the currency ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labA });
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#g3v")) return;
  const d = +$("#g3v").value, e = sdEq(d, 0), ex = -d;
  $("#t1").textContent = ex > 0 ? Lib.fmtN(ex, 0) + " units" : "None"; $("#t2").textContent = Lib.fmtN(e.p, 1);
  $("#tv").textContent = ex > 0 ? `With demand down by ${ex}, the market rate would fall to ${Lib.fmtN(e.p, 1)}. To hold the rate at 50 the central bank must buy ${ex} units of its own currency using reserves, and may raise interest rates. The larger the shift, the faster reserves fall.` : "Demand has not changed, so the fixed rate matches the market rate and no intervention is needed.";
  $("#labB").innerHTML = pegDraw({ d, k: 1 });
}
Lib.slider($("#g3"), { id: "g3v", label: "Fall in demand for the currency ", min: -30, max: 0, step: 5, value: -20, fmt: (v) => v, onInput: labB });
labB();
Lib.classify($("#cl1"), { prompt: "Does it affect the demand for or the supply of the currency?", buckets: [{"label": "Demand for the currency"}, {"label": "Supply of the currency"}], items: [{"text": "Foreigners buy more of the country's exports", "b": 0}, {"text": "Residents buy more imports", "b": 1}, {"text": "A higher interest rate attracts foreign savings", "b": 0}, {"text": "Residents invest in firms abroad", "b": 1}, {"text": "Inward foreign direct investment rises", "b": 0}, {"text": "Savers move funds abroad for higher interest", "b": 1}, {"text": "Speculators expect the currency to rise", "b": 0}, {"text": "Tourists from this country spend more overseas", "b": 1}], done: "Demand comes from foreign buyers who need the currency; supply comes from residents who sell the currency to buy foreign currency." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Appreciation", "A rise in the value of a floating currency"], ["Depreciation", "A fall in the value of a floating currency"], ["Devaluation", "An official fall in a fixed exchange rate"], ["Trade-weighted rate", "An average of rates weighted by trade with each partner"], ["Hot money", "Short-term funds that move for higher interest"], ["Reserves", "Foreign currency held by the central bank"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps in a depreciation in order.", items: ["Foreign demand for exports falls", "Demand for the currency falls", "The demand curve shifts left", "The exchange rate falls", "Exports become cheaper abroad"], done: "Demand falls, the curve shifts and the rate falls." });
Lib.calc($("#c1"), { qs: [
  {"q": "£1 = $1.25. A UK good costs £200. What is its price in $?", "a": 250, "unit": "$", "tol": 0.5, "hint": "200 × 1.25.", "sol": "<b>$250</b>."},
  {"q": "The pound depreciates to £1 = $1.10. What is the $ price of the £200 good?", "a": 220, "unit": "$", "tol": 0.5, "hint": "200 × 1.10.", "sol": "<b>$220</b>."},
  {"q": "What is the % change in the exchange rate from $1.25 to $1.10?", "a": -12, "unit": "%", "tol": 0.1, "hint": "(1.10 − 1.25) ÷ 1.25.", "sol": "<b>-12%</b>."},
  {"q": "At £1 = $1.10, a US good costs $330. What is its price in £?", "a": 300, "unit": "£", "tol": 0.5, "hint": "330 ÷ 1.10.", "sol": "<b>£300</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The exchange rate is:", opts: ["The price of one currency in terms of another", "The interest rate", "The inflation rate", "A tax on imports"], a: 0, why: "The price of a currency." },
  { q: "A rise in demand for a currency causes:", opts: ["An appreciation", "A depreciation", "A devaluation", "No change"], a: 0, why: "Higher demand raises its value." },
  { q: "A fixed rate is defended by:", opts: ["Buying or selling the currency and changing interest rates", "Tariffs only", "Lowering taxes", "Letting demand and supply decide"], a: 0, why: "Intervention with reserves and interest rates." },
  { q: "Higher inflation than trading partners is likely to:", opts: ["Lower the exchange rate", "Raise the exchange rate", "Fix the exchange rate", "Not matter"], a: 0, why: "Exports lose competitiveness." },
  { q: "A devaluation is:", opts: ["An official fall in a fixed rate", "A market fall in a floating rate", "A rise in the rate", "A tax"], a: 0, why: "Set by the authorities." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Exchange rate", "Price of a currency."],
  ["Appreciation", "Floating rate rises."],
  ["Depreciation", "Floating rate falls."],
  ["Demand for currency", "Exports, investment, interest rates."],
  ["Supply of currency", "Imports, investing abroad."],
  ["Fixed rate", "Set and defended."],
  ["Intervention", "Reserves and interest rates."],
  ["Hot money", "Moves for interest rates."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "When is a country's exchange rate most likely to fall? (Feb/March 2025 · 12 · Q27, reworded)", opts: ["When its current account surplus exceeds that of its trading partners.", "When its inflation rate exceeds that of its trading partners.", "When its interest rate exceeds that of its trading partners.", "When its unemployment rate exceeds that of its trading partners."], a: 1, why: "Higher relative inflation reduces competitiveness, lowering demand for the currency and raising supply." },
  { q: "What does a trade-weighted exchange rate attempt to take account of? (May/June 2022 · 12 · Q20, reworded)", opts: ["a country's terms of trade", "international trade as a proportion of a country's national income", "the relative value of international trade done with a country's trading partners", "the size of a country's current account surplus or deficit"], a: 2, why: "It weights each exchange rate by the amount of trade with that partner." },
  { q: "A country operates a fixed exchange rate system. What will put pressure on the country to devalue its currency? (May/June 2022 · 12 · Q23, reworded)", opts: ["a decrease in the country's inflation rate relative to the inflation rates of other countries", "a decrease in the tariffs on its products imposed by other countries", "an increase in its current account balance of payments deficit with other countries", "an increase in the country's interest rate relative to the interest rates of other countries"], a: 2, why: "A bigger deficit raises supply of the currency relative to demand, putting downward pressure on the rate." },
  { q: "The central bank of an economy decides to raise interest rates in order to attract capital inflows and improve the financial account of the balance of payments. When is the central bank's decision least likely to be effective? (May/June 2022 · 11 · Q27, reworded)", opts: ["when the currency of the economy is expected to lose its value", "when the economy is politically and economically stable", "when the interest rate of the economy is higher than that of other countries", "when the reserves of foreign currencies held by the central bank are high and rising"], a: 0, why: "If the currency is expected to fall, investors may not move funds in even at higher rates." },
  { q: "A country with a fixed exchange rate experiences a balance of payments surplus. Which policy measure will enable it to maintain its exchange rate? (Feb/March 2020 · 12 · Q30, reworded)", opts: ["decreasing government borrowing", "decreasing government spending", "decreasing the interest rate", "decreasing the money supply"], a: 2, why: "Lower interest rates reduce demand for the currency, offsetting the upward pressure." },
] });
