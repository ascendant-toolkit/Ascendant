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

/* ---------- MNC network ---------- */
function mncDraw(s) {
  const box = (x, y, w, h, t, c, k) => (k > 0 ? SV.rect(x, y, w, h, c, op(0.5 * k)) + SV.text(x + w / 2, y + h / 2 + 5, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "");
  const ar = (x1, y1, x2, y2, d, t, k, ty, tx) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, d, "dot1") + tag(tx, ty, t, "t1", k, "middle") : "");
  let o = box(40, 120, 190, 70, "Home HQ (parent company)", "f1", 1) + box(530, 120, 190, 70, "Host subsidiary (factory)", "f3", 1);
  o += ar(230, 140, 530, 140, "r", "FDI: capital, technology, managers", s.a, 130, 380);
  if (s.b > 0) o += box(540, 40, 170, 40, "Jobs, training, wages", "f3", s.b) + ar(625, 120, 625, 82, "u", "", s.b, 100, 625);
  if (s.b > 0) o += box(540, 230, 170, 40, "Exports and tax revenue", "f3", s.b) + ar(625, 190, 625, 228, "d", "", s.b, 210, 625);
  if (s.c > 0) o += ar(530, 175, 230, 175, "l", "Profits repatriated; transfer pricing", s.c, 200, 380);
  if (s.d > 0) o += box(260, 230, 210, 44, "Environmental and local-firm costs", "f2", s.d) + ar(530, 190, 470, 245, "l", "", s.d, 210, 500);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A multinational's home headquarters sending FDI to a host country subsidiary, which returns profits">${mncDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "An MNC investing abroad: FDI flows out, benefits and costs flow in the host, and profits flow home", base: { a: 0, b: 0, c: 0, d: 0 }, draw: mncDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>FDI.</b> The parent company in its home country builds or buys a subsidiary in the host country, sending capital, technology and managers.", s: { a: 1 } },
  { cap: "<b>Benefits for the host.</b> The subsidiary creates jobs, trains workers, pays wages and taxes and may export.", s: { a: 1, b: 1 } },
  { cap: "<b>Profits flow home.</b> The parent receives profits and dividends (repatriation), and may use transfer pricing to book profits in low-tax locations. This reduces the net gain for the host.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Other costs.</b> The host may suffer environmental damage and pressure on local firms. The balance depends on the sector and the rules the host sets.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- FDI and the balance of payments over time ---------- */
const BP = [["Year 1", 60, -20], ["Year 3", 25, -8], ["Year 6", 5, 4], ["Year 10", 0, 10]], BY = (v) => 170 - v * 1.7;
function bpDraw(s) {
  let o = axes(70, 170, 730, 20, "", "$m") + SV.line(70, BY(0), 730, BY(0), "ax"); [-20, 0, 20, 40, 60].forEach((v) => (o += SV.text(64, BY(v) + 4, v, "sm", { "text-anchor": "end" })));
  BP.forEach(([l, fa, ca], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 120 + i * 150; o += SV.rect(x, BY(fa * k), 50, Math.abs(fa * k) * 1.7, "f3", op(0.8)) + SV.rect(x + 56, ca >= 0 ? BY(ca * k) : BY(0), 50, Math.abs(ca * k) * 1.7, ca >= 0 ? "f1" : "f2", op(0.8)) + tag(x + 78, 296, l, "sm", k, "middle") + tag(x + 25, BY(fa * k) - 6, "+" + fa, "t3", k, "middle") + tag(x + 81, ca >= 0 ? BY(ca * k) - 6 : BY(0) + Math.abs(ca * k) * 1.7 + 14, (ca >= 0 ? "+" : "") + ca, ca >= 0 ? "t1" : "t2", k, "middle"); });
  o += SV.rect(520, 312, 10, 10, "f3", op(0.8)) + SV.text(536, 321, "Financial account (FDI inflow)", "sm") + SV.rect(520, 330, 10, 10, "f1", op(0.8)) + SV.text(536, 339, "Current account", "sm");
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 345, label: "FDI and the balance of payments over time: a financial account inflow, a current account deficit that later improves", base: { n: 0 }, draw: bpDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>Year 1.</b> The FDI inflow ($60m) improves the financial account. The new factory imports machinery and materials, so the current account worsens ($20m).", s: { n: 1 } },
  { cap: "<b>Year 3.</b> Less new investment arrives and the factory begins to export, so the current account deficit narrows.", s: { n: 2 } },
  { cap: "<b>Year 6.</b> Exports from the factory now exceed its imports, but profit payments abroad appear in the current account, so the surplus is small.", s: { n: 3 } },
  { cap: "<b>Year 10.</b> Exports are established: a current account surplus. The capital inflow has stopped, and profit repatriation is a continuing outflow.", s: { n: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#mc") || !$("#tx") || !$("#mm") || !$("#rp")) return;
  const c = +$("#mc").value / 100, t = +$("#tx").value / 100, m = +$("#mm").value / 100, rp = +$("#rp").value / 100, k = 1 / (1 - c * (1 - t) + m), gdp = 120 * k, gni = gdp * (1 - rp);
  $("#r1").textContent = Lib.fmtN(k, 2); $("#r2").textContent = "$" + Lib.fmtN(gdp, 0) + "m"; $("#r3").textContent = "$" + Lib.fmtN(gni, 0) + "m";
  $("#rv").textContent = `Multiplier = 1 ÷ (1 − ${c.toFixed(2)} × (1 − ${t.toFixed(2)}) + ${m.toFixed(2)}) = ${Lib.fmtN(k, 2)}. FDI of $120m raises GDP by $${Lib.fmtN(gdp, 0)}m. If ${Lib.fmtN(rp * 100, 0)}% of the extra income is profit sent abroad, national income (GNI) rises by only $${Lib.fmtN(gni, 0)}m.`;
  const Y = (v) => 270 - v * 0.9; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["FDI", 120, "f1"], ["Rise in GDP", gdp, "f3"], ["Rise in GNI", gni, "f2"]].forEach(([l, v, cl], i) => { const x = 60 + i * 115, yy = Y(Math.min(v, 280)); o += SV.rect(x, yy, 80, 270 - yy, cl) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, yy - 6, "$" + Lib.fmtN(v, 0) + "m", "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "mc", label: "Marginal propensity to consume, % ", min: 50, max: 90, step: 5, value: 80, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g2"), { id: "tx", label: "Tax rate, % ", min: 0, max: 40, step: 5, value: 25, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g3"), { id: "mm", label: "Marginal propensity to import, % ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: labF });
Lib.slider($("#g3b"), { id: "rp", label: "Share of extra income sent abroad as profit, % ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v + "%", onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labX() {
  if (!$("#sf")) return;
  const s = +$("#sf").value, th = 0.3 * (100 - s), tv = 0.1 * s, loss = 30 - th;
  $("#t1").textContent = "$" + Lib.fmtN(th, 1) + "m"; $("#t2").textContent = "$" + Lib.fmtN(tv, 1) + "m"; $("#t3").textContent = "$" + Lib.fmtN(loss, 1) + "m";
  $("#tv").textContent = s === 0 ? "No profit is shifted: $100m is taxed in the host at 30%, giving $30m of revenue." : `Shifting $${s}m of profit to the haven means $${100 - s}m is taxed in the host at 30% ($${Lib.fmtN(th, 1)}m) and $${s}m at 10% in the haven ($${Lib.fmtN(tv, 1)}m). The group's total tax falls from $30m to $${Lib.fmtN(th + tv, 1)}m and the host loses $${Lib.fmtN(loss, 1)}m of tax revenue that it could have spent on public services.`;
  const Y = (v) => 270 - v * 8; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Tax paid ($m)", "sm");
  [["Host", th, "f2"], ["Haven", tv, "f1"], ["Host's loss", loss, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "sf", label: "Profit shifted to the haven, $m ", min: 0, max: 100, step: 5, value: 40, fmt: (v) => v, onInput: labX });
labX();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it mainly a benefit or a cost for the host country?", buckets: [{"label": "Benefit"}, {"label": "Cost"}], items: [{"text": "Training for local workers", "b": 0}, {"text": "Profits sent back to the home country", "b": 1}, {"text": "New jobs in a factory", "b": 0}, {"text": "Pollution from a mine", "b": 1}, {"text": "Transfer of new technology", "b": 0}, {"text": "Local firms driven out by a large competitor", "b": 1}, {"text": "Extra tax revenue for the government", "b": 0}, {"text": "Transfer pricing used to cut tax", "b": 1}], done: "Benefits: jobs, skills, technology, tax. Costs: repatriation, pollution, competition and transfer pricing." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Multinational company", "A firm that operates in two or more countries"], ["Foreign direct investment", "Investment in real assets or control of a firm in another country"], ["Portfolio investment", "Buying shares or bonds without control; easily sold"], ["Profit repatriation", "Sending profits back to the home country"], ["Transfer pricing", "Setting prices between subsidiaries to shift profits to low-tax places"], ["Greenfield FDI", "Building a new plant abroad"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effect of new FDI on income in order.", items: ["A multinational builds a factory in a host country", "Investment spending and demand for local labour rise", "Workers and suppliers earn income and spend part of it", "Income rises by a multiple of the original investment", "Part of the profit is sent abroad, limiting the rise in national income"], done: "The multiplier works through rounds of spending, with leakages." });
Lib.calc($("#c1"), { qs: [
  {"q": "The MPC is 0.8, the tax rate is 25% and the marginal propensity to import is 0.2. Calculate the multiplier (2 decimal places).", "a": 1.67, "unit": "", "tol": 0.02, "hint": "1 ÷ (1 − 0.8 × 0.75 + 0.2).", "sol": "1 ÷ (1 − 0.6 + 0.2) = 1 ÷ 0.6 = <b>1.67</b>."},
  {"q": "FDI of $120m is made with a multiplier of 1.67. Calculate the rise in GDP ($m).", "a": 200, "unit": "$m", "tol": 1, "hint": "120 × 1.67.", "sol": "<b>$200m</b>."},
  {"q": "30% of the extra $200m of income is sent abroad as profit. Calculate the rise in GNI ($m).", "a": 140, "unit": "$m", "tol": 1, "hint": "200 × 0.7.", "sol": "<b>$140m</b>."},
  {"q": "A subsidiary earns $100m. The host taxes at 30% and the haven at 10%. If $40m of profit is shifted to the haven, by how much does the host's tax revenue fall ($m)?", "a": 12, "unit": "$m", "tol": 0.5, "hint": "30% of 40.", "sol": "Host tax falls by 0.3 × 40 = <b>$12m</b> (the group pays $4m in the haven, saving $8m overall)."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A multinational company is a firm that:", opts: ["Operates in more than one country", "Sells only to its home market", "Is owned by the government", "Has no overseas staff"], a: 0, why: "It has production or operations in two or more countries." },
  { q: "FDI differs from portfolio investment because FDI:", opts: ["Is investment in real assets or a controlling stake", "Can be sold instantly", "Involves only government bonds", "Is always short term"], a: 0, why: "Portfolio investment is in shares and bonds without control." },
  { q: "Transfer pricing is a problem for host countries because it:", opts: ["Reduces tax revenue", "Raises wages", "Raises exports", "Increases competition"], a: 0, why: "Profits are shown in low-tax countries." },
  { q: "A benefit of FDI to a host country is:", opts: ["Transfer of technology and skills", "Outflow of profits", "Loss of local firms", "A larger national debt"], a: 0, why: "Technology and skills may raise productivity." },
  { q: "Which is most likely to attract FDI?", opts: ["Good infrastructure and political stability", "High tariffs", "Poor roads", "Unpredictable laws"], a: 0, why: "Reliable conditions lower risk and costs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["MNC", "A firm operating in more than one country."],
  ["FDI", "Investment in real assets abroad."],
  ["Portfolio investment", "Shares and bonds; volatile."],
  ["Profit repatriation", "Profits sent to the home country."],
  ["Transfer pricing", "Shifting profit through internal prices."],
  ["Greenfield / brownfield", "New plant / buying an existing firm."],
  ["Benefits for host", "Jobs, technology, tax, exports."],
  ["Costs for host", "Repatriation, pollution, local firms hurt."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A government wants to attract foreign direct investment to develop its economy. What is most likely to encourage this? (Feb/March 2022 · 32 · Q20, reworded)", opts: ["Improved health and safety standards for workers", "Increased import quotas", "Increased spending on infrastructure", "Introducing a minimum wage"], a: 2, why: "Roads, power and ports lower firms' costs, so FDI is attracted. A minimum wage raises costs and quotas restrict trade." },
  { q: "In what circumstances will low wages and low-cost land not attract foreign investment in manufacturing in a low-income country? (Oct/Nov 2023 · 33 · Q30, reworded)", opts: ["If the country creates an independent central bank", "If the country privatises state firms", "If the country lacks well-developed infrastructure", "If the country allows repatriation of profits"], a: 2, why: "Without reliable transport and power, low wages are not enough to make production profitable." },
  { q: "What is the most likely consequence of an increase in the number of multinational companies? (May/June 2024 · 31 · Q27, reworded)", opts: ["Fewer advances in technology", "Less foreign direct investment", "More exports", "More unemployment"], a: 2, why: "MNCs trade globally and set up export production, so international trade tends to rise." },
  { q: "An MNC buys a manufacturing firm in a developing country that sells to local consumers. The MNC then exports machinery and raw materials to it. What is the most likely effect on the developing country's balance of payments? (May/June 2024 · 32 · Q28, reworded)", opts: ["Current account improves; financial account improves", "Current account improves; financial account worsens", "Current account worsens; financial account improves", "Current account worsens; financial account worsens"], a: 2, why: "The imported machinery and materials worsen the current account, and the purchase is a capital inflow, which improves the financial account." },
  { q: "FDI brings better training and higher productivity, but profits are sent back to the investor's home country. What is the effect on aggregate demand and aggregate supply in the host country? (Oct/Nov 2020 · 33 · Q21, reworded)", opts: ["AD shifts left; AS shifts left", "AD shifts right; AS shifts left", "AD shifts left; AS shifts right", "AD shifts right; AS shifts right"], a: 2, why: "Better skills shift AS right. The profit outflow reduces spending in the host country's circular flow, so AD shifts left." },
  { q: "Country X has low inflation, a stable currency and unemployed resources. It attracts $25bn of FDI. What is most likely to be a positive benefit? (Oct/Nov 2022 · 32 · Q28, reworded)", opts: ["Aggregate demand rises through the investment multiplier", "It must use its reserves to eliminate any trade deficit", "The balance of payments is affected by the outflow of profits", "Inflation rises if capacity is raised"], a: 0, why: "With spare resources, the extra investment raises output and employment by a multiple of the original amount. The other three are costs." },
  { q: "What is most likely to result from foreign direct investment in a developing economy? (Oct/Nov 2024 · 33 · Q28, reworded)", opts: ["An improved trade balance", "A rise in net investment income", "A fall in government tax revenue", "A fall in wage levels"], a: 0, why: "FDI that builds export capacity or replaces imports can improve the trade balance. Profit outflows reduce net investment income, and tax revenue and wages are more likely to rise." },
  { q: "Company X makes batteries for electric cars and invests in a new factory in country N. Under which conditions is this most likely to improve N's current account? Share of raw materials supplied by N, and income elasticity of demand for electric cars outside N. (Oct/Nov 2024 · 32 · Q28, reworded)", opts: ["10%, 0.5", "10%, 1.5", "90%, 0.5", "90%, 1.5"], a: 3, why: "Buying most materials locally reduces imports, and high income elasticity abroad means export sales rise strongly as incomes grow." },
  { q: "A multinational firm wants to minimise costs and maximise profits. What would least assist it? (Oct/Nov 2021 · 31 · Q9, reworded)", opts: ["Near-monopoly status to control output and prices", "Locating its home base in a low corporation tax country", "Operating in a cartel with production quotas", "Owning subsidiaries in several countries to gain economies of scale"], a: 2, why: "A cartel needs agreement between rival firms, and tends to break down; it does not follow from being multinational. The other three help directly." },
] });
