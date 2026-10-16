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

/* ---------- Savings gap ---------- */
const GY = (v) => 300 - v * 8.5;
function gapDraw(s) {
  let o = axes(70, 300, 730, 30, "", "% of GDP"); [0, 10, 20, 30].forEach((v) => (o += SV.text(64, GY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const bx = (x, v, y0, c, l, k) => (k > 0 ? SV.rect(x, GY(y0 + v * k), 100, v * k * 8.5, c, op(0.75)) + tag(x + 50, GY(y0 + v * k) - 6, l + " " + Lib.fmtN(v, 0) + "%", "t1", 1, "middle") : "");
  o += SV.rect(120, GY(25), 100, 25 * 8.5, "f2", op(0.2)) + SV.line(120, GY(25), 220, GY(25), "c2 dash") + tag(170, GY(25) - 6, "needed: 25%", "t2", s.a, "middle");
  o += bx(300, 12, 0, "f1", "Saving", s.a);
  if (s.b > 0) o += bx(300, 13, 12, "f3", "Aid", s.b);
  if (s.c > 0) o += tag(560, 80, "Growth = investment ÷ capital-output ratio (4)", "t4", s.c, "middle") + tag(560, 106, "Without aid: 12 ÷ 4 = 3% a year", "t1", s.c, "middle") + tag(560, 132, "With aid: 25 ÷ 4 = 6.25% a year", "t3", s.c, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Investment needed of 25 percent of GDP, domestic saving of 12 percent and an aid-funded gap of 13 percent">${gapDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 345, label: "A savings gap filled by aid and the effect on growth", base: { a: 0, b: 0, c: 0 }, draw: gapDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The target.</b> To grow at about 6% a year with a capital-output ratio of 4, the economy needs to invest about 25% of GDP.", s: { a: 1 } },
  { cap: "<b>Domestic saving</b> is only 12% of GDP, because incomes are low and little is left over after meeting basic needs.", s: { a: 1 } },
  { cap: "<b>Aid fills the gap.</b> An aid inflow worth 13% of GDP, used for investment, brings total funds up to 25%.", s: { a: 1, b: 1 } },
  { cap: "<b>Growth.</b> Investment of 25% ÷ capital-output ratio 4 gives growth of about 6.25% a year, compared with 3% without aid, provided the aid is invested well.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Routes of aid ---------- */
function routeDraw(s) {
  const box = (x, y, w, t, c, k) => (k > 0 ? SV.rect(x, y, w, 48, c, op(0.5 * k)) + SV.text(x + w / 2, y + 30, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "");
  let o = box(40, 130, 150, "Donor government", "f1", 1) + box(570, 130, 150, "Recipient country", "f3", 1);
  const ar = (x1, y1, x2, y2, k, t, ty) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, "r", "dot1") + tag((x1 + x2) / 2, ty, t, "t1", k, "middle") : "");
  o += ar(190, 154, 570, 154, s.a, "Bilateral aid (grants, loans, technical help)", 144);
  if (s.b > 0) o += box(290, 40, 180, "World Bank / UN agencies", "f2", s.b) + ar(190, 140, 290, 70, s.b, "", 90) + ar(470, 70, 570, 140, s.b, "Multilateral aid", 80);
  if (s.c > 0) o += box(290, 240, 180, "NGOs and charities", "f2", s.c) + ar(190, 170, 290, 262, s.c, "Donations and grants", 230) + ar(470, 262, 570, 172, s.c, "Emergency and local projects", 244);
  if (s.d > 0) o += tag(380, 118, "TIED: must buy from the donor", "t2", s.d, "middle") + SV.rect(575, 190, 140, 34, "f2", op(0.4 * s.d)) + tag(645, 212, "Higher project costs", "t2", s.d, "middle");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 310" role="img" aria-label="Aid flowing from a donor government to a recipient directly, via multilateral agencies and via NGOs">${routeDraw({ a: 1, b: 1, c: 1, d: 0 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 310, label: "Aid routes: bilateral, multilateral and through NGOs, and the effect of tying", base: { a: 0, b: 0, c: 0, d: 0 }, draw: routeDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>Bilateral aid</b> goes directly from one government to another as grants, soft loans or technical assistance.", s: { a: 1 } },
  { cap: "<b>Multilateral aid</b> is pooled through organisations such as the World Bank and UN agencies, which decide how to spend it.", s: { a: 1, b: 1 } },
  { cap: "<b>NGOs and charities</b> channel private donations and some government funds into emergency relief and local projects. Private charity is not counted as official aid.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Tying.</b> If bilateral aid must be spent on the donor's goods, the recipient loses the chance to buy more cheaply elsewhere, so the same money does less.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!$("#sv") || !$("#ai") || !$("#ko")) return;
  const sv = +$("#sv").value, ai = +$("#ai").value, k = +$("#ko").value / 10, inv = sv + ai, g0 = sv / k, g1 = inv / k;
  $("#r1").textContent = Lib.fmtN(inv, 0) + "% of GDP"; $("#r2").textContent = Lib.fmtN(g0, 1) + "%"; $("#r3").textContent = Lib.fmtN(g1, 1) + "%";
  $("#rv").textContent = ai === 0 ? `With no aid, investment equals saving (${sv}% of GDP) and growth is ${sv} ÷ ${Lib.fmtN(k, 1)} = ${Lib.fmtN(g0, 1)}% a year.` : `Aid of ${ai}% of GDP lifts investment from ${sv}% to ${inv}% of GDP. With a capital-output ratio of ${Lib.fmtN(k, 1)}, growth rises from ${Lib.fmtN(g0, 1)}% to ${Lib.fmtN(g1, 1)}% a year. This assumes all the aid is invested productively, which is the key limit of the model.`;
  const Y = (v) => 270 - v * 6; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "% of GDP, % a year", "sm");
  [["Saving", sv, "f1"], ["Aid", ai, "f3"], ["Growth, no aid", g0, "f1"], ["Growth, aid", g1, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85; o += SV.rect(x, Y(Math.min(v, 40)), 60, 270 - Y(Math.min(v, 40)), c) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(Math.min(v, 40)) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sv", label: "Domestic saving, % of GDP ", min: 5, max: 25, step: 1, value: 12, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "ai", label: "Aid invested, % of GDP ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g3"), { id: "ko", label: "Capital-output ratio ", min: 20, max: 60, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labA });
labA();

/* ---------- Lab 2 ---------- */
function labE() {
  if (!$("#tp") || !$("#lk")) return;
  const p = +$("#tp").value / 100, l = +$("#lk").value / 100, eff = 100 * (1 - l) / (1 + p);
  $("#t1").textContent = "+" + Lib.fmtN(p * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(l * 100, 0) + "%"; $("#t3").textContent = "$" + Lib.fmtN(eff, 1) + "m";
  $("#tv").textContent = `Of $100m of aid, ${Lib.fmtN(l * 100, 0)}% leaks away, leaving $${Lib.fmtN(100 * (1 - l), 0)}m. If the tied goods cost ${Lib.fmtN(p * 100, 0)}% more than on the open market, that $${Lib.fmtN(100 * (1 - l), 0)}m buys only what $${Lib.fmtN(eff, 1)}m would buy: an effective value of ${Lib.fmtN(eff, 1)}% of the nominal figure.`;
  const Y = (v) => 270 - v * 2.3; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["Given", 100, "f1"], ["After leakage", 100 * (1 - l), "f2"], ["Effective value", eff, "f3"]].forEach(([lab, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c) + SV.text(x + 40, 290, lab, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "tp", label: "Extra cost of tied goods, % ", min: 0, max: 40, step: 1, value: 25, fmt: (v) => v + "%", onInput: labE });
Lib.slider($("#g5"), { id: "lk", label: "Leakage through waste or corruption, % ", min: 0, max: 40, step: 1, value: 10, fmt: (v) => v + "%", onInput: labE });
labE();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which type of aid is it?", buckets: [{"label": "Grant or soft loan"}, {"label": "Technical assistance"}, {"label": "Emergency or food aid"}, {"label": "Tied aid"}], items: [{"text": "A gift of $50m for rural schools with no repayment", "b": 0}, {"text": "Experts sent to help a ministry reform tax collection", "b": 1}, {"text": "Food and tents sent after a flood", "b": 2}, {"text": "A loan that must be spent on the donor's engineering firms", "b": 3}, {"text": "A 40-year loan at 0.5% interest", "b": 0}, {"text": "Teaching teams train local nurses", "b": 1}, {"text": "Medical supplies flown in after an earthquake", "b": 2}, {"text": "A grant that can be used only to buy the donor's drugs", "b": 3}], done: "Grants and soft loans are financial; technical help is expertise; emergency aid meets urgent needs; tied aid is limited to donor goods." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Bilateral aid", "Aid from one government directly to another"], ["Multilateral aid", "Aid pooled and channelled through international bodies"], ["Tied aid", "Aid that must be spent on the donor's goods and services"], ["Official development assistance", "Government aid to promote development on concessional terms"], ["Savings gap", "Shortage of domestic saving to fund the investment needed for growth"], ["Foreign exchange gap", "Shortage of foreign currency to pay for imports of capital goods"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain from aid to growth in order.", items: ["Aid is received and invested in infrastructure and schools", "The savings and foreign exchange gaps narrow", "Investment and human capital rise", "Productive capacity (potential output) rises", "Growth and living standards may improve"], done: "Aid helps growth only if it is invested productively." });
Lib.calc($("#c1"), { qs: [
  {"q": "A donor gives $24bn of aid and its GNI is $3,600bn. Calculate aid as a percentage of GNI (2 decimal places).", "a": 0.67, "unit": "%", "tol": 0.01, "hint": "24 ÷ 3,600 × 100.", "sol": "<b>0.67%</b>, close to but below the UN target of 0.7%."},
  {"q": "Saving is 15% of GDP and the capital-output ratio is 3. Calculate the growth rate with no aid (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "15 ÷ 3.", "sol": "<b>5%</b>."},
  {"q": "Aid worth 6% of GDP is invested as well. Using the same figures, calculate the new growth rate (%).", "a": 7, "unit": "%", "tol": 0.05, "hint": "(15 + 6) ÷ 3.", "sol": "21 ÷ 3 = <b>7%</b>."},
  {"q": "A $100m tied aid package costs 25% more than the same goods on the open market and 10% is lost to waste. Calculate the effective value ($m).", "a": 72, "unit": "$m", "tol": 0.5, "hint": "100 × 0.9 ÷ 1.25.", "sol": "90 ÷ 1.25 = <b>$72m</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Tied aid is aid that:", opts: ["Must be spent on goods from the donor", "Has to be repaid in a year", "Is given to a company", "Is only for emergencies"], a: 0, why: "The recipient has less freedom to choose cheaper suppliers." },
  { q: "Which is a possible benefit of aid?", opts: ["Funding for infrastructure, health and education", "Guaranteed zero debt", "Lower birth rates in every case", "A fall in the exchange rate"], a: 0, why: "Productive spending can raise potential output." },
  { q: "A disadvantage of food aid is that it may:", opts: ["Lower local food prices and hurt local farmers", "Raise the price of capital goods", "Increase interest rates", "Reduce imports of oil"], a: 0, why: "Local producers face competition from free supplies." },
  { q: "The UN target for aid from high-income countries is:", opts: ["0.7% of GNI", "7% of GNI", "0.07% of GNI", "20% of exports"], a: 0, why: "The 0.7% of GNI target has been met by few countries." },
  { q: "Which is least likely to be official foreign aid?", opts: ["A donation by a charity after a flood", "A government grant for schools", "A soft loan from the World Bank", "Technical assistance from a government agency"], a: 0, why: "Official aid comes from governments and agencies." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Bilateral aid", "Government to government."],
  ["Multilateral aid", "Through the World Bank or UN."],
  ["Tied aid", "Spent on donor's goods."],
  ["Grant", "A gift; no repayment."],
  ["Soft loan", "Low interest, long term."],
  ["Savings gap", "Too little saving to fund investment."],
  ["Foreign exchange gap", "Too little foreign currency for imports."],
  ["0.7% target", "UN aid target as share of GNI."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Money given by the US government to certain African countries to fight HIV/AIDS requires their governments to buy expensive US drugs rather than cheaper ones from South Africa, India or Brazil. What is this an example of? (Oct/Nov 2021 · 31 · Q28, reworded)", opts: ["Bilateral aid", "Debt relief", "Multilateral aid", "Tied aid"], a: 3, why: "Tied aid must be spent on the donor's own goods, which can raise costs for the recipient." },
  { q: "Some conditions for providing foreign aid to low-income countries are restrictive. Which kind of aid fits this description? (Oct/Nov 2024 · 31 · Q28, reworded)", opts: ["Food aid after natural disasters such as drought", "Grants tied to buying donor country goods", "Loans repaid over a long period at a low rate of interest", "Technical assistance using highly skilled workers"], a: 1, why: "Tying the grant to purchases from the donor limits how the recipient can spend it." },
  { q: "A developing country receiving foreign financial aid is most likely to grow in the long run if it uses the money to: (Oct/Nov 2020 · 33 · Q18, reworded)", opts: ["Boost welfare benefits for the poorest households", "Pay for imports of capital goods", "Reduce environmental pollution", "Reduce income tax for all households"], a: 1, why: "Capital goods raise productive capacity, which raises long-run growth. The others are worthwhile but raise consumption or reduce external costs rather than capacity." },
  { q: "Why is disaster relief money sent by non-governmental organisations to a South American country not classified as official foreign aid? (Oct/Nov 2022 · 32 · Q20, reworded)", opts: ["It does not finance a long-term investment programme", "It does not incur interest", "It is not supplied by a government", "Only countries in Asia and Africa count as developing"], a: 2, why: "Official aid is government or agency aid. Private charity is outside it." },
  { q: "The table shows GNI and foreign aid spending in 2016: Belgium $468.9bn and $2.10bn; Germany $3,612.1bn and $23.84bn; Sweden $532.7bn and $5.38bn; South Korea $1,403.6bn and $2.10bn. What can be concluded? (Oct/Nov 2020 · 32 · Q19, reworded)", opts: ["Countries with higher GNI always spend more on aid", "Germany spends the most on aid in the world", "South Korea and Belgium give an equal share of GNI", "Sweden gave the highest share of GNI"], a: 3, why: "Aid as a share of GNI: Sweden about 1.0%, Germany 0.66%, Belgium 0.45%, South Korea 0.15%." },
  { q: "Some economists argue there is little evidence of the value of aid in improving development. Which situation supports this claim? (Feb/March 2025 · 32 · Q30, reworded)", opts: ["Greater capacity to benefit from communications technology", "Investment in infrastructure creating transport links and ports", "Over-reliance on technical assistance impairing local initiative and innovation", "Education and training projects improving the supply side"], a: 2, why: "Dependence on outside experts is a way that aid can undermine local capacity. The others are benefits." },
  { q: "Middle Eastern countries want to help low-income countries to grow. Which policy would be least likely to achieve this? (Feb/March 2023 · 32 · Q19, reworded)", opts: ["Writing off debts to ease foreign exchange shortages", "Financing clean water capital projects through aid", "Hiring mainly labour from low-income countries to build infrastructure in the Middle East", "Cutting fuel exports to low-income countries to reduce pollution"], a: 3, why: "Cutting the fuel supply would raise energy costs and slow growth. The other three raise capacity or income." },
  { q: "Which items are classified as foreign aid? Foreign direct investment, official development assistance, portfolio investment flows. (May/June 2022 · 31 · Q27, reworded)", opts: ["Foreign direct investment only", "Official development assistance only", "Official development assistance and portfolio investment", "Foreign direct investment and portfolio investment"], a: 1, why: "Only official development assistance is aid. Investment flows are commercial." },
] });
