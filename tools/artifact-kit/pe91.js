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

const tickSet = (gx, gy, x0, y0, xm, ym, sx, sy) => { let o = ""; for (let v = 0; v <= xm + 0.001; v += sx) { if (v > 0) o += SV.line(gx(v), y0, gx(v), gy(ym), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(gx(v), y0, gx(v), y0 + 5, "", {}) + SV.text(gx(v), y0 + 18, v, "sm", { "text-anchor": "middle" }); }
  for (let v = sy; v <= ym + 0.001; v += sy) { o += SV.line(x0, gy(v), gx(xm), gy(v), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }) + SV.line(x0 - 5, gy(v), x0, gy(v), "", {}) + SV.text(x0 - 9, gy(v) + 4, v, "sm", { "text-anchor": "end" }); } return o; };

/* ---------- Keynesian cross, used for both questions ---------- */
function cross(el, cfg) {
  const E0 = 70, MXV = cfg.mx, SC = cfg.sc, TOP = 36, F0 = TOP + MXV * SC, px = (v) => E0 + SC * v, py = (v) => F0 - SC * v, SL = 0.6, a1 = cfg.a1, a2 = cfg.a2, YF = 500;
  const y1 = a1 / (1 - SL), y2 = a2 / (1 - SL), top = a1 + SL * YF, lo = Math.min(YF, top), hi = Math.max(YF, top);
  let o = tickSet(px, py, E0, F0, MXV, MXV, 100, 100) + axes(E0, F0, px(MXV) + 8, TOP - 14, "", "Aggregate expenditure, AE") + SV.text(px(MXV / 2), F0 + 52, "National income, Y", "sm", { "text-anchor": "middle" });
  o += SV.line(px(0), py(0), px(MXV), py(MXV), "c3") + tag(px(MXV) + 6, py(MXV) - 8, "45° line", "t3");
  o += SV.line(px(0), py(a1), px(MXV), py(a1 + SL * MXV), "c1") + tag(px(MXV) + 6, py(a1 + SL * MXV) + 6, "AE1", "t1");
  o += SV.line(px(0), py(a2), px(MXV), py(a2 + SL * MXV), "c2") + tag(px(MXV) + 6, py(a2 + SL * MXV) + 6, "AE2", "t2");
  o += SV.line(px(YF), F0, px(YF), py(hi), "c3 dash") + tag(px(YF), F0 + 34, "YF = 500", "t3", 1, "middle");
  o += SV.line(px(YF), py(lo), px(YF), py(hi), "c2", { "stroke-width": 8 }) + tag(px(YF) - 14, py(hi) - 16, cfg.gapTxt, "t2", 1, "end");
  o += SV.circle(px(y1), py(y1), 6, "dot1") + tag(px(y1) - 10, py(y1) - 14, "Y1 = " + y1, "t1", 1, "end") + SV.circle(px(y2), py(y2), 6, "dot2") + tag(px(y2) + 14, py(y2) + 36, "Y2 = " + y2, "t2");
  $(el).innerHTML = `<svg viewBox="0 0 600 ${F0 + 66}" role="img" aria-label="${cfg.label}">${o}</svg>`;
}
cross("#dg1", { a1: 260, a2: 200, mx: 700, sc: 0.5, gapTxt: "inflationary gap = 60", label: "45 degree diagram showing an inflationary gap of 60 closed by a downward shift of AE" });
cross("#dg3", { a1: 160, a2: 200, mx: 600, sc: 0.58, gapTxt: "deflationary gap = 40", label: "45 degree diagram showing a deflationary gap of 40 closed by an upward shift of AE" });

/* ---------- AD/AS with Keynesian AS: more than one shift of AD ---------- */
(function () {
  const E0 = 70, TOP = 36, SX = 0.6, SY = 1.3, F0 = TOP + 250 * SY, px = (v) => E0 + SX * v, py = (v) => F0 - SY * v, YF = 500, P0 = 100, YMAX = 600;
  const ad = (sh) => (Y) => 200 - 0.25 * (Y - sh);
  let o = tickSet(px, py, E0, F0, YMAX, 250, 100, 50) + axes(E0, F0, px(YMAX) + 10, TOP - 14, "", "Price level") + SV.text(px(300), F0 + 52, "Real GDP ($bn)", "sm", { "text-anchor": "middle" });
  o += SV.path(`M${px(0)} ${py(P0)} L${px(YF)} ${py(P0)} L${px(YF)} ${py(250)}`, "c4") + tag(px(YF) + 6, py(238), "AS", "t4");
  const line = (sh, cls, lab, tc) => { const pts = []; for (let Y = 0; Y <= YMAX; Y += 10) { const p = ad(sh)(Y); if (p >= 40 && p <= 250) pts.push([px(Y), py(p)]); } const lp = sh === 0 ? 175 : sh === 40 ? 200 : 225, lx = px((200 - lp) / 0.25 + sh); return SV.path(Lib.ptsPath(pts), cls) + tag(lx + 6, py(lp) - 8, lab, tc); };
  o += line(0, "c1", "AD1", "t1") + line(40, "c3", "AD2", "t3") + line(100, "c2", "AD3", "t2");
  o += SV.line(px(400), py(P0), px(400), F0, "c1 dash") + SV.circle(px(400), py(P0), 6, "dot1") + tag(px(400) - 4, F0 + 34, "Y1 = 400", "t1", 1, "end");
  o += SV.circle(px(440), py(P0), 5, "dot3") + SV.line(px(440), py(P0), px(440), F0, "c3 dash");
  o += SV.line(px(500), py(P0), px(500), F0, "c2 dash") + SV.circle(px(500), py(P0), 6, "dot2") + tag(px(500) + 4, F0 + 34, "YF = 500", "t2", 1, "start");
  o += tag(px(10), py(P0) - 10, "negative output gap = 100", "t2");
  o += SV.line(px(400), py(P0) + 14, px(440), py(P0) + 14, "c3", { "stroke-width": 3 }) + SV.line(px(440), py(P0) + 14, px(500), py(P0) + 14, "c2", { "stroke-width": 3 });
  o += tag(px(YF) + 26, py(215), "AD1 to AD2: G, 40", "t3") + tag(px(YF) + 26, py(190), "AD2 to AD3: multiplier, 60", "t2");
  $("#dg2").innerHTML = `<svg viewBox="0 0 640 ${F0 + 66}" role="img" aria-label="AD and AS diagram with Keynesian AS showing AD shifting three times from output 400 to output 500">${o}</svg>`;
})();

/* ---------- self check ---------- */
function checker(el, items, res) {
  const box = $(el); if (!box) return;
  box.innerHTML = items.map((t, i) => `<label><input type="checkbox" data-i="${i}"> <span>${t}</span></label>`).join("") + '<div class="res"></div>';
  const upd = () => { const n = $$("input:checked", box).length; box.querySelector(".res").textContent = res(n, items.length); };
  $$("input", box).forEach((c) => (c.onchange = upd)); upd();
}
checker("#ck1", [
  "I defined an inflationary gap (AE at full employment above potential output) and monetary policy",
  "I drew and labelled a diagram showing the gap and used it in the text",
  "I explained a full chain for a rise in interest rates (at least four links) to a lower AE and income",
  "I explained a second type of monetary policy (money supply, credit)",
  "I included a real example or figure",
  "I explained fiscal policy as an alternative, with a limit",
  "I explained supply-side policy as an alternative, with a limit",
  "I evaluated each policy (elasticity of spending, lags, causes of inflation)",
  "I answered 'how far' with a degree and said what it depends on"
], (n, t) => n <= 3 ? "Level 1 to 2 (up to about 6 marks): you need more than one tool, a diagram and a comparison." : n <= 5 ? "Level 3 (about 7 to 8): add the missing tools, alternatives and a conclusion on relative effectiveness." : n <= 7 ? "Level 4, lower to middle (about 9 to 11): explain the evaluation and make the conclusion compare the options." : "Level 4, upper (about 11 to 13): check that the chains are developed and the conclusion depends on size and cause of the gap.");
checker("#ck2", [
  "I defined negative output gap and full employment",
  "I defined expansionary fiscal policy and said G is an injection and a component of AD",
  "I gave the multiplier formula and the open-economy version (MPS + MRT + MPM)",
  "I calculated the spending needed (gap ÷ multiplier) with numbers",
  "I explained multiple rounds of spending and induced consumption and investment",
  "I drew an AD/AS diagram with more than one shift (or explained why the rise is more than the spending)",
  "I applied it to a type of government spending (roads, schools) or a real figure",
  "I evaluated at least three points, each explained (lever, because, so what)",
  "I included both undershoot and overshoot as the multiplier is uncertain",
  "I wrote a conclusion that answers the statement, says when it holds and ranks the factors"
], (n, t) => n <= 3 ? "Level 1 (about 1 to 5 of 14, E1 at best): learn the concepts and the formula and add numbers." : n <= 5 ? "Level 2 (about 6 to 10 of 14, E1): add the rounds, the diagram and application, and explain each evaluation point." : n <= 8 ? "Level 3 for the 14 and E1 to E2 (about 11 to 14, 3 to 5): make sure every evaluation point is explained and ends with 'so what'." : "Level 3 and E2 (about 13 to 14 of 14 and 5 to 6 of 6): check the conclusion answers the statement directly.");

/* ---------- practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which skill does each sentence show?", buckets: [{ label: "Knowledge" }, { label: "Application" }, { label: "Analysis" }, { label: "Evaluation" }], items: [
  { text: "A negative output gap exists when actual output is below potential output.", b: 0 },
  { text: "The Bank of England raised Bank Rate from 0.1% to 5.25% between late 2021 and August 2023.", b: 1 },
  { text: "A higher interest rate raises the cost of borrowing, so firms cancel investment and AE shifts down.", b: 2 },
  { text: "However, if firms are confident, investment may fall by less than expected and some of the gap remains.", b: 3 },
  { text: "The multiplier is the ratio of the final change in income to the initial change in an injection.", b: 0 },
  { text: "Workers on a new railway spend their wages in shops, which pay their own staff.", b: 1 },
  { text: "The multiplier is 1 ÷ 0.4 = 2.5, so $40bn of spending raises income by $100bn.", b: 2 },
  { text: "With a high MPM the multiplier falls to 1.25 and the government would need to spend $80bn.", b: 3 }],
  done: "Evaluation questions the claim and says what changes. Analysis explains the steps. Application uses the specific context or figures." });
Lib.order($("#o1"), { prompt: "Put the chain for question 2 in order, starting with the first event.", items: ["The government spends $40bn on infrastructure", "Construction firms and workers receive $40bn of extra income", "They spend part of it, which becomes income for others (rounds of spending)", "Induced consumption and investment add to later rounds", "National income rises by 40 × 2.5 = $100bn and output reaches full employment"], done: "The required injection is the gap ÷ the multiplier." });
Lib.calc($("#c1"), { qs: [
  { q: "MPS = 0.1, MRT = 0.2 and MPM = 0.1. What is the multiplier?", a: 2.5, tol: 0.01, sol: "MPW = 0.4, so k = 1 ÷ 0.4 = <b>2.5</b>." },
  { q: "The negative output gap is $100bn and the multiplier is 2.5. How much must the government spend ($bn)?", a: 40, tol: 0.01, sol: "100 ÷ 2.5 = <b>$40bn</b>." },
  { q: "MPS = 0.2, MRT = 0.2 and MPM = 0.4. What is the multiplier?", a: 1.25, tol: 0.01, sol: "MPW = 0.8, so k = 1 ÷ 0.8 = <b>1.25</b>." },
  { q: "Using that multiplier and a gap of $100bn, how much must the government spend ($bn)?", a: 80, tol: 0.01, sol: "100 ÷ 1.25 = <b>$80bn</b>." },
  { q: "AE1 = 260 + 0.6Y and full employment is 500. What is the inflationary gap (the vertical distance at 500)?", a: 60, tol: 0.01, sol: "AE at 500 is 260 + 300 = 560. The gap is 560 − 500 = <b>60</b>." },
  { q: "With a multiplier of 2.5, a fall in autonomous spending of 60 lowers income by how much ($bn)?", a: 150, tol: 0.01, sol: "60 × 2.5 = <b>$150bn</b>." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement about the Question 2 conclusion is best?", opts: ["The statement is always true because the multiplier is greater than one", "The statement is true in theory, but in practice it depends on the size of the multiplier, so spending may be too little or too much", "The statement is false because crowding out always cancels the multiplier", "The statement cannot be evaluated"], a: 1, why: "A top conclusion answers the statement, says when it holds, and ranks the factors." },
  { q: "Which is the strongest evaluation of an interest rate rise as a way to close an inflationary gap?", opts: ["It is expensive", "It depends on how sensitive spending is to interest rates and it works with a lag, so the gap could close first or remain", "It is used by many governments", "It always works"], a: 1, why: "It explains the lever, the reason and the effect on the outcome." },
  { q: "On an AD/AS diagram for Question 2, what should the examiner see?", opts: ["One shift of AD only", "More than one shift of AD, or one shift with an explanation that the rise is more than the spending", "AS shifting to the right", "A fall in the price level"], a: 1, why: "The mark scheme asks for this." },
  { q: "Why is the 20-mark question harder than the 13-mark one?", opts: ["It has more content", "Knowledge and analysis (14) and evaluation (6) are marked separately, so each skill needs more depth", "It needs no diagram", "It is only about evaluation"], a: 1, why: "The 20-mark scales reward depth in each skill separately." },
  { q: "An answer to Question 1 uses only fiscal policy. What is the likely result?", opts: ["Full marks", "A low level because the question asks about monetary policy", "Level 4", "No effect"], a: 1, why: "The scheme asks for at least two types of monetary policy." }] });
Lib.cards($("#fc1"), { cards: [
  ["Inflationary gap", "AE at the full employment level of income exceeds potential output; excess demand pulls up the price level."],
  ["Negative output gap", "Actual output below potential output; spare capacity and cyclical unemployment."],
  ["Multiplier (open economy)", "1 ÷ (MPS + MRT + MPM) = 1 ÷ MPW."],
  ["Injection needed", "Output gap ÷ multiplier."],
  ["Crowding out", "Government borrowing raises interest rates and reduces private investment, lowering the net multiplier."],
  ["Lever, because, so what", "The structure of an explained evaluation point."],
  ["Table A", "14 marks: knowledge, application and analysis (L1 1–5, L2 6–10, L3 11–14)."],
  ["Table B", "6 marks: evaluation (E1 1–3, E2 4–6)."]] });
