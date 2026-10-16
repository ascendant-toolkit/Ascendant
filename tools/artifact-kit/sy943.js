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

/* ---------- Scale picture ---------- */
function scaleSvg(M, V, P, T, note) {
  const L = M * V, R = P * T, mx = Math.max(L, R, 1) * 1.15, Y = (v) => 270 - v / mx * 220; let o = SV.line(40, 270, 720, 270);
  o += SV.rect(110, Y(L), 220, 270 - Y(L), "f1") + tag(220, Y(L) - 8, "MV = " + Lib.fmtN(L, 0), "t1", 1, "middle") + SV.text(220, 290, "M × V (spending)", "sm bd", { "text-anchor": "middle" });
  o += SV.rect(430, Y(R), 220, 270 - Y(R), "f4") + tag(540, Y(R) - 8, "PT = " + Lib.fmtN(R, 0), "t4", 1, "middle") + SV.text(540, 290, "P × T (value of transactions)", "sm bd", { "text-anchor": "middle" });
  o += tag(220, 190, "M = " + M + ", V = " + Lib.fmtN(V, 1), "t1", 1, "middle") + tag(540, 190, "P = " + Lib.fmtN(P, 2) + ", T = " + Lib.fmtN(T, 0), "t4", 1, "middle");
  if (note) o += tag(380, 30, note, "t3", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 310" role="img" aria-label="Bars showing that money supply times velocity equals price level times transactions">${scaleSvg(1000, 4, 2, 2000, "Both sides measure total spending: 4,000")}</svg>`;
function eqDraw(s) { const M = 1000 * (1 + 0.1 * s.m), V = 4 * (1 + s.v), T = 2000 * (1 + s.t), P = M * V / T; return scaleSvg(M, V, P, T, s.l); }
Lib.stepper($("#stE"), { w: 760, h: 310, label: "The equation MV = PT as two bars of equal height changing as M rises, V changes or T changes", base: { m: 0, v: 0, t: 0, l: "" }, draw: eqDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The identity.</b> M = 1,000, V = 4 so total spending MV is 4,000. With T = 2,000 transactions, P = 2. Both sides measure the same thing.", s: { l: "Base case: P = 2" } },
  { cap: "<b>M rises 10%</b> with V and T unchanged. Spending is 4,400 and P rises to 2.2: a 10% rise. This is the quantity theory's prediction.", s: { m: 1, l: "M up 10%: P up 10%" } },
  { cap: "<b>Velocity falls.</b> If people hold on to money (V falls 10%), the extra money is offset and P stays near 2. The prediction fails if V is not stable.", s: { m: 1, v: -0.1, l: "V down 10%: P back to about 2" } },
  { cap: "<b>Transactions rise.</b> With spare capacity T could rise 10%, so the extra spending buys more output. P is back at 2 with higher output. The prediction fails if T is not fixed.", s: { m: 1, t: 0.1, l: "T up 10%: P back to 2" } },
] });

/* ---------- Watch 2: two cases ---------- */
const GXX = (t) => 90 + t * 62, GYY = (v) => 300 - v * 2.2;
function twoDraw(s) {
  let o = SV.line(70, 300, 700, 300) + SV.line(70, 300, 70, 40) + SV.text(700, 320, "Years", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Index (year 0 = 100)", "sm");
  const N = Math.round(s.n), mk = (f) => Lib.ptsPath(Array.from({ length: N + 1 }, (_, t) => [GXX(t), GYY(f(t) - 80)]));
  const money = (t) => 100 * Math.pow(1.12, t), pr1 = (t) => 100 * Math.pow(s.k > 0 ? 1.12 : 1.02, t), out1 = (t) => 100 * Math.pow(s.k > 0 ? 1.0 : 1.05, t);
  if (N >= 1) { o += SV.path(mk(money), "c1") + SV.path(mk(pr1), "c2") + SV.path(mk(out1), "c3"); o += tag(GXX(N) + 6, GYY(money(N) - 80) - 6, "money supply", "t1") + tag(GXX(N) + 6, GYY(pr1(N) - 80) + 14, "prices", "t2") + tag(GXX(N) + 6, GYY(out1(N) - 80) + 28, "real output", "t3"); }
  o += tag(380, 56, s.l, "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "Money supply growing 12 percent a year with prices rising in one case and output rising in the other", base: { n: 0, k: 0, l: "" }, draw: twoDraw, tween: 1000, dwell: 6000, steps: [
  { cap: "<b>The same money growth.</b> In both economies the money supply grows 12% a year.", s: { n: 1, k: 0, l: "Case A: spare capacity" } },
  { cap: "<b>Case A: spare capacity.</b> The economy has idle resources. Extra spending raises <b>real output</b> by about 5% a year and prices by only 2%: velocity or output absorbs the money. This supports the Keynesian view.", s: { n: 8, k: 0, l: "Case A: spare capacity" } },
  { cap: "<b>Case B: full employment.</b> Output cannot rise. Money growth of 12% shows up almost wholly as <b>inflation of 12%</b>, as the quantity theory predicts.", s: { n: 8, k: 1, l: "Case B: at full employment" } },
] });

/* ---------- Lab 1 ---------- */
function labQT() {
  if (!$("#qm") || !$("#qv") || !$("#qt")) return;
  const M = +$("#qm").value, V = +$("#qv").value / 10, T = +$("#qt").value, P = M * V / T, chg = (P / 2 - 1) * 100;
  $("#r1").textContent = Lib.fmtN(P, 2); $("#r2").textContent = (chg >= 0 ? "+" : "") + Lib.fmtN(chg, 1) + "%"; $("#r3").textContent = Lib.fmtN(M * V, 0);
  $("#rv").textContent = Math.abs(chg) < 0.5 ? "The three variables roughly offset: the price level is about unchanged." : chg > 0 ? `MV = ${Lib.fmtN(M * V, 0)} against T = ${T}, so P = ${Lib.fmtN(P, 2)}, a rise of ${Lib.fmtN(chg, 1)}%. Spending has grown faster than transactions.` : `MV = ${Lib.fmtN(M * V, 0)} against T = ${T}, so P = ${Lib.fmtN(P, 2)}, a fall of ${Lib.fmtN(-chg, 1)}%. Transactions have grown faster than spending (deflation).`;
  $("#labA").innerHTML = scaleSvg(M, V, P, T, "");
}
Lib.slider($("#g1"), { id: "qm", label: "Money supply M ", min: 600, max: 1600, step: 50, value: 1000, fmt: (v) => v, onInput: labQT });
Lib.slider($("#g2"), { id: "qv", label: "Velocity V ", min: 20, max: 80, step: 2, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labQT });
Lib.slider($("#g3"), { id: "qt", label: "Transactions T ", min: 1400, max: 2800, step: 100, value: 2000, fmt: (v) => v, onInput: labQT });
labQT();

/* ---------- Lab 2 ---------- */
function labSC() {
  if (!$("#sp")) return;
  const g = 10, share = +$("#sp").value / 100, dT = g * share, dP = (1 + g / 100) / (1 + dT / 100) * 100 - 100;
  $("#t1").textContent = "+" + Lib.fmtN(dT, 1) + "%"; $("#t2").textContent = "+" + Lib.fmtN(dP, 1) + "%"; $("#t3").textContent = share < 0.2 ? "Monetarist" : share > 0.6 ? "Keynesian" : "Mixed";
  $("#tv").textContent = `A 10% rise in the money supply with ${Math.round(share * 100)}% of it met by extra output raises output by ${Lib.fmtN(dT, 1)}% and prices by ${Lib.fmtN(dP, 1)}% (velocity held constant). With full employment (0% met by output) all of the rise goes to prices; with large spare capacity most goes to output.`;
  let o = SV.line(40, 250, 400, 250); [["Output", dT, "f3", "t3"], ["Prices", dP, "f2", "t2"]].forEach(([l, v, c, t], i) => { const x = 90 + i * 150, h = v / 11 * 200; o += SV.rect(x, 250 - h, 90, Math.max(h, 2), c) + tag(x + 45, 250 - h - 8, "+" + Lib.fmtN(v, 1) + "%", t, 1, "middle") + SV.text(x + 45, 270, l, "sm bd", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "sp", label: "Share of extra spending met by extra output (%) ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v, onInput: labSC });
labSC();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "According to the quantity theory (V and T constant), what happens to the price level?", buckets: [{"label": "Rises"}, {"label": "Falls"}, {"label": "Stays the same"}], items: [{"text": "The money supply rises 8% and output is unchanged", "b": 0}, {"text": "The money supply is unchanged and transactions rise 5%", "b": 1}, {"text": "The money supply and transactions both rise 4%", "b": 2}, {"text": "The money supply falls 6% and output is unchanged", "b": 1}, {"text": "The money supply rises 5% and transactions rise 5%", "b": 2}, {"text": "The money supply rises 15% and transactions rise 3%", "b": 0}], done: "With V constant: %ΔP ≈ %ΔM − %ΔT." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["MV = PT", "Total spending equals the value of transactions: an identity"], ["Velocity of circulation", "How many times a unit of money is spent in a period"], ["Monetarism", "The view that money supply growth drives inflation"], ["Endogenous money", "Money supply that responds to demand for credit"], ["Fisher equation", "The form of the theory with T as transactions or real output"], ["Money supply rule", "A rule to keep the growth of money in line with output"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the monetarist argument in order.", items: ["The central bank allows the money supply to grow faster than output", "There is more money chasing the same quantity of goods", "With V and T constant total spending rises while output cannot", "Prices rise", "Inflation can be controlled only by slowing money growth"], done: "Inflation is a monetary phenomenon in the monetarist view." });
Lib.calc($("#c1"), { qs: [
  {"q": "M = 500, V = 4 and T = 1,000. Calculate the price level P.", "a": 2, "tol": 0.01, "hint": "P = MV ÷ T.", "sol": "500 × 4 ÷ 1000 = <b>2</b>."},
  {"q": "M rises to 600 with V = 4 and T = 1,000. Calculate the percentage change in the price level from the previous question.", "a": 20, "unit": "%", "tol": 0.05, "hint": "New P = 600 × 4 ÷ 1000 = 2.4.", "sol": "P rises from 2 to 2.4: <b>20%</b>."},
  {"q": "The money supply grows 7% a year, velocity is constant and real output grows 2% a year. Using the approximation, what is the inflation rate (%)?", "a": 5, "unit": "%", "tol": 0.05, "hint": "%ΔP ≈ %ΔM − %ΔT.", "sol": "7 − 2 = <b>5%</b>."},
  {"q": "Nominal GDP is $2,400bn and the money supply is $600bn. Calculate the income velocity of circulation.", "a": 4, "tol": 0.01, "hint": "V = nominal GDP ÷ M.", "sol": "2400 ÷ 600 = <b>4</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The quantity theory of money states that:", opts: ["A rise in the money supply raises output", "A rise in the money supply raises the price level when V and T are constant", "Velocity always rises", "Prices are unrelated to money"], a: 1, why: "With V and T fixed, MV = PT implies that a rise in M raises P." },
  { q: "Which would raise the velocity of circulation?", opts: ["Wages paid monthly instead of weekly", "More use of credit cards", "A fall in interest rates", "Greater uncertainty and hoarding of cash"], a: 1, why: "Card use lets people hold smaller balances so money circulates faster." },
  { q: "What would a Keynesian say about the effect of extra money in a recession?", opts: ["Prices will rise one-for-one", "Output may rise because there is spare capacity", "Velocity is stable", "Nothing will happen to demand"], a: 1, why: "With spare capacity T can rise, so the quantity theory prediction fails." },
  { q: "Which is a criticism of the quantity theory?", opts: ["V is not stable", "It uses equations", "It mentions prices", "It is too simple to state"], a: 0, why: "V changes with technology, interest rates and confidence." },
  { q: "Which period is most associated with money growth causing hyperinflation?", opts: ["Weimar Germany in 1923", "The UK in 1990", "Japan in 2000", "The US in 2019"], a: 0, why: "Rapid printing of money led to extreme price rises." },
] });
Lib.cards($("#fc1"), { cards: [
  ["MV = PT", "Money supply × velocity = price level × transactions."],
  ["Velocity of circulation", "Times a unit of money is spent in a period."],
  ["Quantity theory", "With V and T stable, M changes P."],
  ["Monetarism", "Inflation is caused by excessive money supply growth."],
  ["Endogenous money", "The supply of money responds to demand."],
  ["Hyperinflation", "Extremely rapid, accelerating inflation."],
  ["Money supply rule", "Fixed target for money growth."],
  ["Fisher", "Developed the equation of exchange."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In MV = PT, V is the income velocity of circulation. Which change would tend to reduce V? (Feb/March 2025 · 32 · Q17, reworded)", opts: ["A move to monthly rather than weekly salary payments", "A rise in interest rates", "More use of cash machines to reduce money balances held", "A fall in the use of credit cards by individuals"], a: 0, why: "Less frequent payments mean people hold larger balances for longer, so money circulates more slowly." },
  { q: "The quantity theory is sometimes written MV = PT. Which statement is not correct? (May/June 2025 · 34 · Q19, reworded)", opts: ["M is the total value of notes and coins in circulation only", "P measures the average price level", "T stands for the quantity of real transactions in the period", "V is the average number of times money changes hands in a period"], a: 0, why: "M is the whole money supply, including bank deposits, not only notes and coins." },
  { q: "Which components of the quantity theory are considered constant and which variable by monetarists? (Oct/Nov 2022 · 33 · Q23, reworded)", opts: ["Money supply constant, velocity variable, price level constant, transactions variable", "Velocity and transactions constant; money supply and price level variable", "Money supply variable, velocity constant, price level variable, transactions constant", "All variable"], a: 1, why: "Monetarists assume V and T are constant, so M changes lead to changes in P." },
  { q: "What is an important assumption of monetarism? (Oct/Nov 2020 · 32 · Q25, reworded)", opts: ["Fiscal policy is more effective than monetary policy in reducing inflation", "Long-term unemployment results from deficient demand", "The interest elasticity of investment is low", "The velocity of circulation is stable"], a: 3, why: "A stable velocity is what makes money growth predict inflation." },
  { q: "Which statement does not correctly characterise the monetarist view? (Oct/Nov 2022 · 31 · Q25, reworded)", opts: ["Inflation is always caused by increases in the money supply in the long run", "The LRAS curve is vertical", "The velocity of circulation of money is highly unstable", "Policy should follow set rules"], a: 2, why: "Monetarists believe velocity is stable or predictable." },
  { q: "What belief do Keynesians and monetarists share? (May/June 2020 · 31 · Q27, reworded)", opts: ["Expectations adapt quickly", "Fiscal policy is the most effective policy", "There is a need for individual choice expressed through the market", "Velocity of circulation is stable"], a: 2, why: "Both accept a role for markets and individual choice, though they disagree about the rest." },
  { q: "What do monetarists believe? (Oct/Nov 2022 · 32 · Q25, reworded)", opts: ["Economies are naturally unstable", "Policy makers should follow set rules targeting the money supply", "The AS curve has a slight slope", "Wages are sticky downwards"], a: 1, why: "Monetarists favour rules for the money supply rather than discretion." },
] });
