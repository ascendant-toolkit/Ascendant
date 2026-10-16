/* IGCSE Economics Chapter 26: Fiscal policy, evaluation technique */
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const money = (v, d = 1) => Lib.fmtN(v, d);
const fade = (v) => clamp(v, 0, 1);

/* ---------- 1. shape of an 8-mark answer ---------- */
const BLOCKS = [
  { t: "Side 1: why it might work", d: "A developed reason: chain of cause and effect, with economic terms.", tag: "Analysis", cls: "n", y: 24, h: 84 },
  { t: "Side 2: why it might not", d: "A different developed reason, with its own chain.", tag: "Analysis", cls: "n", y: 124, h: 84 },
  { t: "Conclusion", d: "Which side is stronger, and why? Say what it depends on.", tag: "Judgement", cls: "e", y: 224, h: 84 },
];
function shapeChart(s) {
  let o = "";
  BLOCKS.forEach((b, k) => {
    const a = fade(s.a - k), col = `var(--${b.cls})`;
    o += `<g opacity="${(0.12 + 0.88 * a).toFixed(2)}">` + SV.rect(20, b.y, 560, b.h, "", { rx: 10, style: `fill:var(--surface);stroke:${col};stroke-width:3` }) +
      SV.rect(20, b.y, 8, b.h, "", { rx: 4, style: `fill:${col}` }) +
      SV.text(44, b.y + 26, b.t, "lbl bd", { style: `font-size:16px;fill:${col}` }) + SV.text(44, b.y + 48, b.d, "sm", { style: "font-size:12.5px" }) + "</g>";
    o += `<g opacity="${a.toFixed(2)}">` + SV.rect(600, b.y + b.h / 2 - 16, 140, 32, "", { rx: 16, style: `fill:${col};opacity:.18` }) + SV.text(670, b.y + b.h / 2 + 5, b.tag, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) + "</g>";
  });
  const lv = fade(s.l);
  o += `<g opacity="${lv.toFixed(2)}">` + SV.rect(600, 24, 140, 284, "", { rx: 10, style: "fill:none;stroke:var(--muted);stroke-width:1.5;stroke-dasharray:5 4" }) + "</g>";
  o += `<g opacity="${lv.toFixed(2)}">` + SV.text(670, 336, "Level 3 (6–8 marks)", "lbl bd t1", { "text-anchor": "middle" }) + "</g>";
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 350, label: "The three parts of an 8-mark Discuss answer", base: { a: 0, l: 0 }, draw: shapeChart, steps: [
  { cap: "An 8-mark <b>Discuss</b> question is marked by <b>levels</b>. To reach the top you need three things. A one-line definition at the start is fine, but it earns little by itself.", s: { a: 0, l: 0 } },
  { cap: "<b>Side 1.</b> A reason the policy <i>might</i> work, run as a chain: tax cut → higher after-tax profit → more investment → more output and jobs.", s: { a: 1, l: 0 } },
  { cap: "<b>Side 2.</b> A <i>different</i> reason it might not work, with its own chain: less tax revenue → less spending on public services. Not just the reverse of side 1.", s: { a: 2, l: 0 } },
  { cap: "<b>Conclusion.</b> Say which side is stronger and give a reason, for example \"more likely if firms are confident, because they would then use the extra profit to invest\".", s: { a: 3, l: 0 } },
  { cap: "That is a Level 3 answer: both sides developed, economic terms used, and a justified conclusion. Plan for about two minutes and write for about ten.", s: { a: 3, l: 1 } },
] });

/* ---------- 2. where the chain breaks: a cut in income tax ---------- */
const NODES = ["Cut in income tax", "Disposable income rises", "Consumption rises", "AD shifts right", "Output and jobs rise"];
const BREAKS = ["Size: a small cut may be too small to notice", "Saved, not spent: households may expect higher taxes later", "Spent on imports: the multiplier is smaller", "No spare capacity: demand mainly raises prices", "Time lags and a bigger deficit: effects arrive late and cost more"];
function chainChart(s) {
  const w = 134, gap = 22, x0 = 8, y = 56, h = 62;
  let o = "";
  NODES.forEach((n, i) => {
    const x = x0 + i * (w + gap), lit = fade(s.p - i), words = n.split(" "), half = Math.ceil(words.length / 2), l1 = words.slice(0, half).join(" "), l2 = words.slice(half).join(" ");
    o += SV.rect(x, y, w, h, "", { rx: 10, style: `fill:${lit > 0.5 ? "var(--accent-soft)" : "var(--surface)"};stroke:${lit > 0.5 ? "var(--accent)" : "var(--line)"};stroke-width:${lit > 0.5 ? 3 : 2}` });
    o += SV.text(x + w / 2, y + 28, l1, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(x + w / 2, y + 46, l2, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    if (i < 4) {
      const ax = x + w + 2, a2 = x + w + gap - 2, on = fade(s.p - i - 0.5);
      o += SV.line(ax, y + h / 2, a2 - 5, y + h / 2, "ax", { style: `stroke:${on > 0.5 ? "var(--accent)" : "var(--line)"};stroke-width:3` }) + SV.arrowHead(a2, y + h / 2, "r", on > 0.5 ? "dot1" : "arr");
    }
    const b = fade(s.b - i), by = 150;
    if (b > 0.05) {
      const lines = [], max = 19;
      let cur = "";
      BREAKS[i].split(" ").forEach((wd) => { if ((cur + " " + wd).trim().length > max) { lines.push(cur.trim()); cur = wd; } else cur += " " + wd; });
      lines.push(cur.trim());
      o += `<g opacity="${b.toFixed(2)}">` + SV.line(x + w / 2, y + h + 4, x + w / 2, by - 6, "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.circle(x + w / 2, y + h + 4, 5, "dot2");
      o += SV.rect(x, by, w, 22 + lines.length * 17, "", { rx: 8, style: "fill:var(--bad-soft);stroke:var(--bad);stroke-width:2" });
      lines.forEach((l, k) => { o += SV.text(x + 8, by + 20 + k * 17, l, "sm", { style: "font-size:12px;fill:var(--ink)" }); });
      o += "</g>";
    }
  });
  if (s.p > 4.5 && s.b < 0.5) o += SV.text(380, 28, "The chain works on paper", "lbl bd t1", { "text-anchor": "middle", style: "font-size:16px" });
  if (s.b > 4.5) o += SV.text(380, 28, "Each red box is a reason for side 2", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 238, label: "Chain of reasoning for a tax cut with break points", base: { p: 0, b: 0 }, draw: chainChart, steps: [
  { cap: "The analysis is a <b>chain</b>. Each box leads to the next, and each link is a mark for analysis. We start with the policy.", s: { p: 0.99, b: 0 } },
  { cap: "A cut in income tax raises <b>disposable income</b>, so households could <b>consume</b> more.", s: { p: 2.5, b: 0 } },
  { cap: "Higher consumption shifts <b>AD to the right</b> and real GDP and employment could rise. That is a full Level 3 chain.", s: { p: 5, b: 0 } },
  { cap: "Now think about <b>side 2</b>: every link can break. The cut may be too small, or the money <b>saved</b> instead of spent.", s: { p: 5, b: 2 } },
  { cap: "Some of the extra income may go on <b>imports</b>, and if there is no <b>spare capacity</b> the extra AD mainly raises prices.", s: { p: 5, b: 4 } },
  { cap: "Last, <b>time lags</b> and the larger <b>deficit</b>. Pick the one or two breaks that fit the question and write them as a developed argument: \"however … because …\".", s: { p: 5, b: 5 } },
] });

/* ---------- 3. elasticity and indirect tax ---------- */
const QX = (q) => 80 + 6 * q, PY = (p) => 350 - 2.7 * p;
function clip(m, c) { // P = mQ + c inside Q 0..100, P 0..120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function ln(m, c, cls, label, t, attrs) {
  const [q1, p1, q2, p2] = clip(m, c);
  if (q2 <= q1) return "";
  return SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, attrs) + SV.text(QX(q2) + 6, PY(p2) + 4, label, "lbl bd " + t, attrs && attrs.opacity !== undefined ? { opacity: attrs.opacity } : undefined);
}
function taxChart(s) {
  const b = s.b, t = s.t, dq = -t / (b + 0.6), p1 = 50 + (b * t) / (b + 0.6), q1 = 50 + dq;
  let o = SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) + SV.text(QX(0) - 8, PY(120) + 2, "Price", "sm", { "text-anchor": "end" }) + SV.text(QX(104), PY(0) + 22, "Quantity", "sm", { "text-anchor": "end" });
  o += ln(-b, 50 + 50 * b, "c1", "D", "t1") + ln(0.6, 20, "c3", "S", "t3", { opacity: t > 1 ? 0.4 : 1 });
  o += SV.line(QX(0), PY(50), QX(50), PY(50), "gr") + SV.line(QX(50), PY(50), QX(50), PY(0), "gr") + SV.circle(QX(50), PY(50), 5, "dot3", { opacity: t > 1 ? 0.5 : 1 });
  o += SV.text(QX(0) - 8, PY(50) + 4, "P", "sm bd", { "text-anchor": "end" }) + SV.text(QX(50), PY(0) + 18, "Q", "sm bd", { "text-anchor": "middle" });
  if (t > 1) {
    o += ln(0.6, 20 + t, "c2", "S₁", "t2");
    o += SV.line(QX(0), PY(p1), QX(q1), PY(p1), "gr") + SV.line(QX(q1), PY(p1), QX(q1), PY(0), "gr") + SV.circle(QX(q1), PY(p1), 6, "dot2");
    o += SV.text(QX(0) - 8, PY(p1) + 4, "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(QX(q1), PY(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
    const share = ((p1 - 50) / t) * 100, fall = ((50 - q1) / 50) * 100;
    o += SV.text(QX(70), PY(15), "Consumers pay " + Math.round(share) + "% of the tax", "lbl bd t2", { style: "font-size:14px" });
    o += SV.text(QX(70), PY(7), "Quantity falls " + Math.round(fall) + "%", "lbl bd t1", { style: "font-size:14px" });
  }
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 410, label: "An indirect tax shifting supply, with steep and flat demand", base: { b: 1.4, t: 0 }, draw: taxChart, steps: [
  { cap: "A market for a demerit good: demand <b>D</b> and supply <b>S</b> meet at price <b>P</b> and quantity <b>Q</b>. Producing and consuming it creates external costs, so the government considers an <b>indirect tax</b>.", s: { b: 1.4, t: 0 } },
  { cap: "The tax raises firms' costs, so supply shifts <b>left</b> to S₁ by the amount of the tax. Quantity falls to Q₁ and price rises to P₁. With medium elasticity the tax is shared between buyers and sellers.", s: { b: 1.4, t: 24 } },
  { cap: "<b>Inelastic demand</b> (steep D), such as an addictive good. Buyers pay almost all of the tax and quantity barely falls. The tax raises revenue but <b>does little to cut consumption</b>: the external cost may remain.", s: { b: 3.2, t: 24 } },
  { cap: "<b>Elastic demand</b> (flat D), where substitutes exist. Buyers react a lot, quantity falls sharply and producers bear more of the tax. Now the tax <b>does reduce the external cost</b>.", s: { b: 0.4, t: 24 } },
  { cap: "<b>Conclusion link:</b> \"This depends on price elasticity of demand.\" Say which type of good the question is about, and whether the tax is likely to change behaviour or mainly raise revenue.", s: { b: 1.4, t: 24 } },
] });

/* ---------- 4. sentence ladder ---------- */
const LADDER = [
  { tag: "Statement", cls: "k", tx: ["A cut in income tax helps the economy."], note: "One mark of knowledge at best." },
  { tag: "Reason", cls: "k", tx: ["…because households have more disposable income."], note: "A reason, but no chain yet." },
  { tag: "Chain", cls: "n", tx: ["…so they are likely to spend more, AD could shift right", "and real GDP and employment may rise."], note: "Analysis: a developed cause and effect chain." },
  { tag: "Side 2", cls: "e", tx: ["However, households might save the extra income instead of spending it."], note: "The other side starts, but it is only stated." },
  { tag: "Developed", cls: "e", tx: ["If confidence is low they may save it, so consumption rises by less and", "AD, output and jobs may hardly change."], note: "The second side now has a reason and an effect." },
  { tag: "Conclusion", cls: "e", tx: ["Overall, a tax cut is more likely to help when households are confident,", "because they would spend rather than save the extra income."], note: "Picks a side and gives a reason." },
];
function ladderChart(s) {
  let o = "";
  LADDER.forEach((r, k) => {
    const a = fade(s.i - k), y = 14 + k * 62, col = `var(--${r.cls})`;
    o += `<g opacity="${(0.1 + 0.9 * a).toFixed(2)}">` + SV.rect(14, y, 732, 54, "", { rx: 9, style: `fill:var(--surface);stroke:${col};stroke-width:${a > 0.9 && Math.round(s.i) === k ? 3.5 : 1.8}` });
    o += SV.rect(14, y, 112, 54, "", { rx: 9, style: `fill:${col};opacity:.2` }) + SV.text(70, y + 33, r.tag, "lbl bd", { "text-anchor": "middle", style: `fill:${col};font-size:14px` });
    r.tx.forEach((t, j) => { o += SV.text(138, y + (r.tx.length === 1 ? 33 : 23 + j * 18), t, "lbl", { style: "font-size:13.5px" }); });
    o += "</g>";
  });
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 392, label: "A sentence climbing from statement to conclusion", base: { i: 0 }, draw: ladderChart, steps: LADDER.map((r, k) => ({ cap: `<b>${r.tag}.</b> ${r.note}`, s: { i: k } })) });

/* ================= LABS ================= */
function labA() {
  if (!$("#la") || !$("#lb") || !$("#lc")) return;
  const leak = +$("#la").value, spare = +$("#lb").value, inj = +$("#lc").value, mult = 1 / leak, ad = inj * mult, out = (ad * spare) / 100, pr = ad - out;
  $("#la1").textContent = money(mult, 2); $("#la2").textContent = "$" + money(ad, 0) + "bn"; $("#la3").textContent = "$" + money(out, 0) + "bn"; $("#la4").textContent = "$" + money(pr, 0) + "bn";
  const parts = [];
  parts.push(spare >= 70 ? "With plenty of spare capacity most of the extra demand is likely to raise real output and jobs." : spare <= 30 ? "With little spare capacity most of the extra demand could simply raise prices, so the gain in real output may be small." : "With some spare capacity the extra demand is likely to be split between more output and higher prices.");
  parts.push(leak >= 0.55 ? "A large share leaks into saving, taxes and imports, so the multiplier is small and the effect is weak." : leak <= 0.3 ? "Little leaks out, so the multiplier is large and each $1 of spending is likely to go further." : "The multiplier is moderate.");
  parts.push(`Meanwhile the $${inj}bn has an opportunity cost: it must be paid for by borrowing (a bigger deficit) or by higher taxes.`);
  $("#lav").textContent = parts.join(" ");
  const k = 4.2, x0 = 150, bars = [["Spending", inj, "var(--accent)"], ["Total rise in AD", ad, "var(--n)"], ["Real output", out, "var(--good)"], ["Higher prices", pr, "var(--bad)"]];
  let o = "";
  bars.forEach((b, i) => {
    const y = 28 + i * 72;
    o += SV.text(x0 - 12, y + 28, b[0], "lbl bd", { "text-anchor": "end" }) + SV.rect(x0, y, Math.max(2, b[1] * k), 44, "", { rx: 6, style: `fill:${b[2]};opacity:.85` }) + SV.text(x0 + Math.max(2, b[1] * k) + 10, y + 29, "$" + money(b[1], 0) + "bn", "lbl bd", { style: "font-size:15px" });
  });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "la", label: "Leakages: share of extra income saved, taxed or spent on imports", min: 0.2, max: 0.7, step: 0.05, value: 0.4, fmt: (v) => Math.round(v * 100) + "%", onInput: labA });
Lib.slider($("#g2"), { id: "lb", label: "Spare capacity in the economy", min: 0, max: 100, step: 5, value: 70, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g3"), { id: "lc", label: "Rise in government spending", min: 5, max: 50, step: 5, value: 20, fmt: (v) => "$" + v + "bn", onInput: labA });

function labB() {
  if (!$("#ld") || !$("#le")) return;
  const ed = +$("#ld").value, tx = +$("#le").value, share = 1 / (ed + 1), rise = tx * share, fall = Math.min(100, ed * rise), q1 = 100 - fall, rev = ((100 * tx) / 100) * q1;
  $("#lb1").textContent = money(rise, 1) + "%"; $("#lb2").textContent = money(fall, 1) + "%"; $("#lb3").textContent = money(rev, 0); $("#lb4").textContent = Math.round(share * 100) + "%";
  const p1 = fall < 10 ? `Quantity falls by only ${money(fall, 0)}%: the tax raises plenty of revenue but changes behaviour very little, so the external cost may remain.` : fall < 30 ? `Quantity falls by ${money(fall, 0)}%: a useful reduction, though a large part of the external cost may remain.` : `Quantity falls by ${money(fall, 0)}%: the tax is likely to reduce the external cost noticeably.`;
  $("#lbv").textContent = p1 + ` Consumers bear about ${Math.round(share * 100)}% of the tax${share > 0.6 ? ", so poorer households may be hit hard (regressive)." : "."}`;
  const k = 2.6, base = 270, o = SV.line(100, base, 700, base) +
    SV.rect(180, base - 100 * k, 150, 100 * k, "", { rx: 6, style: "fill:var(--accent);opacity:.85" }) + SV.rect(430, base - q1 * k, 150, q1 * k, "", { rx: 6, style: "fill:var(--bad);opacity:.85" }) +
    SV.text(255, base + 22, "Quantity before tax: 100", "lbl bd", { "text-anchor": "middle" }) + SV.text(505, base + 22, "After tax: " + money(q1, 0), "lbl bd", { "text-anchor": "middle" }) +
    SV.text(255, base - 100 * k + 28, "100", "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:18px" }) + SV.text(505, base - q1 * k + 28, money(q1, 0), "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:18px" });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "ld", label: "Price elasticity of demand (ignoring the minus sign)", min: 0.2, max: 3, step: 0.1, value: 0.5, fmt: (v) => money(v, 1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : " unit elastic"), onInput: labB });
Lib.slider($("#g5"), { id: "le", label: "Size of the tax as a % of the original price", min: 5, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: labB });

/* Level checker */
(function () {
  const items = [
    ["for", "I give at least one reason it might work and develop it as a chain (A leads to B leads to C)."],
    ["against", "I give at least one different reason it might not work and develop it as a chain."],
    ["terms", "I use at least two economic terms correctly (AD, multiplier, deficit, elastic, progressive, opportunity cost…)."],
    ["judge", "My conclusion says which side is stronger and gives a reason."],
    ["ctx", "I use the context or a real example (cigarettes, a housing shortage, a recession)."],
    ["hedge", "I use hedged words (could, may, likely) rather than \"will\" and \"always\"."],
  ];
  const el = $("#chk");
  el.innerHTML = items.map(([k, t]) => `<label style="display:flex;gap:10px;align-items:flex-start;margin:7px 0;cursor:pointer"><input type="checkbox" data-k="${k}" style="margin-top:5px;accent-color:var(--accent);width:18px;height:18px"><span>${t}</span></label>`).join("") + `<div class="verdict" id="chkv" aria-live="polite"></div><div id="chkm" class="note"></div>`;
  const upd = () => {
    const on = {}; $$("input", el).forEach((i) => (on[i.dataset.k] = i.checked));
    const n = Object.values(on).filter(Boolean).length;
    let lvl;
    if (on.for && on.against && on.terms && on.judge) lvl = "Level 3 (6–8 marks)" + (on.ctx && on.hedge ? ": likely 7–8" : ": likely 6–7");
    else if ((on.for || on.against) && on.terms) lvl = "Level 2 (3–5 marks)";
    else if (n > 0) lvl = "Level 1 (1–2 marks)";
    else lvl = "Tick what your answer contains";
    $("#chkv").textContent = lvl;
    const miss = items.filter(([k]) => !on[k]).map(([, t]) => t);
    $("#chkm").textContent = n && miss.length ? "To move up, add: " + miss[0].replace(/^I /, "") : n ? "Nothing missing. Check the timing: about ten minutes." : "";
  };
  $$("input", el).forEach((i) => i.addEventListener("change", upd)); upd();
})();

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each sentence <b>developing a reason</b> (how it works) or part of a <b>conclusion</b> (weighing the sides and giving a reason)?", buckets: [{ label: "Developing a reason" }, { label: "Conclusion" }], items: [
  { text: "A cut in income tax raises households' disposable income.", b: 0 },
  { text: "Higher spending raises AD, so output and employment could rise.", b: 0 },
  { text: "An excise duty raises firms' costs, so supply shifts left and the price rises.", b: 0 },
  { text: "Households might save the extra income, so consumption rises by less.", b: 0 },
  { text: "The multiplier means the final rise in AD may be larger than the initial spending.", b: 0 },
  { text: "Overall, the tax is more likely to work for goods with elastic demand, because quantity would fall by more.", b: 1 },
  { text: "On balance, extra spending is more likely to help if there is spare capacity, because output could rise without prices rising.", b: 1 },
  { text: "A tax cut is more likely to help if households are confident, because they would spend the extra income.", b: 1 },
  { text: "Overall, spending on education is likelier to benefit the economy than a tax cut, since the skills gained could raise output for years.", b: 1 },
], done: "Reasons build the chain; the conclusion weighs the sides and says why." });
Lib.classify($("#cl2"), { prompt: "Sort these points for <i>Discuss whether or not lower taxes on firms will be beneficial for an economy</i>.", buckets: [{ label: "Why it might be beneficial" }, { label: "Why it might not be" }], items: [
  { text: "Higher after-tax profits give firms the ability to invest", b: 0 },
  { text: "More investment may raise output and demand for workers", b: 0 },
  { text: "Lower rates may attract foreign firms", b: 0 },
  { text: "Investment in new technology may raise productivity", b: 0 },
  { text: "The government receives less revenue to spend on services", b: 1 },
  { text: "Firms may keep the extra profit instead of investing it", b: 1 },
  { text: "More output may create external costs such as pollution", b: 1 },
  { text: "Foreign firms could replace local firms", b: 1 },
], done: "Both sides are available from the same policy: each side needs a chain." });
Lib.match($("#m1"), { prompt: "Match the sentence to what it points out.", pairs: [
  ["Time lag", "Spending on schools may take years to raise productivity."],
  ["Spare capacity", "Without unused resources, extra demand could mainly raise prices."],
  ["Elasticity", "Smokers may keep buying after a tax rise, so quantity may fall little."],
  ["Multiplier", "Much of the extra income may be spent on imported goods."],
  ["Opportunity cost", "The same money could have paid for healthcare."],
  ["Size", "A very small cut in tax may be saved rather than spent."],
], done: "These are the things your second side or conclusion could depend on." });
Lib.order($("#o1"), { prompt: "Put the sentences of one analysis-plus-evaluation paragraph in order.", items: [
  "Government spending on housing could benefit the economy because it adds directly to aggregate demand.",
  "Builders would need more workers, so employment may rise.",
  "Their extra income may be spent again, creating a multiplier effect.",
  "Real GDP could therefore rise by more than the original spending.",
  "However, this is more likely if the economy has spare capacity.",
  "If it does not, the extra demand could mainly raise prices and the gain may be smaller.",
], done: "Claim, step, step, result, however, because." });
Lib.order($("#o2"), { prompt: "Put the parts of an 8-mark answer in order.", items: [
  "Opening line: define the policy in one sentence",
  "Side 1: a reason it might work, as a chain",
  "Side 2: a different reason it might not work, as a chain",
  "Conclusion: which side is stronger and why",
], done: "That is the shape of a Level 3 answer." });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which sentence best <b>develops side 2</b> after: \"A tax cut raises consumption\"?", opts: ["A tax cut is a fall in the tax rate.", "Consumption is spending by households.", "However, households may save the extra income if they expect taxes to rise.", "A tax cut is made by the government."], a: 2, why: "It gives a reason (expecting higher taxes) and an effect (saving), so the outcome might differ." },
  { q: "Which is the <b>best conclusion</b> for \"Discuss whether or not a government should increase spending on healthcare\"?", opts: ["Healthcare is good so the government should spend more.", "There are advantages and disadvantages.", "Overall, extra spending is more likely to benefit the economy if it targets preventive care and the economy has spare capacity, because the productivity gain could outweigh the opportunity cost.", "I think it depends."], a: 2, why: "It picks a side and gives a reason. The others state a view or say \"depends\" without saying on what." },
  { q: "A student writes: \"Indirect taxes reduce consumption of demerit goods. However, they might not.\" What is missing?", opts: ["A definition of demerit goods", "A reason why they might not, such as inelastic demand", "A diagram", "Another side"], a: 1, why: "\"They might not\" is a bare assertion. Say <i>why</i>: addictive goods have inelastic demand, so quantity may fall little." },
  { q: "Which is a <b>time lag</b> point?", opts: ["The government might borrow more.", "Spending on training may take years to raise skills and output.", "A tax might be avoided.", "Demand may be inelastic."], a: 1, why: "Time lags are about when the effect appears, not whether it appears." },
  { q: "Which statement is only <b>knowledge</b> (no reasoning)?", opts: ["This depends on how the revenue is spent.", "A larger multiplier would make the effect bigger.", "The government might not have enough money, so it may borrow.", "Government spending is part of AD."], a: 3, why: "That is a fact. The others give a condition or a reason." },
  { q: "Which pair is the <b>weakest</b> use of two sides?", opts: ["Tax cuts raise consumption; tax cuts do not raise consumption.", "Tax cuts raise consumption; lower revenue reduces public spending.", "Tax cuts help firms invest; firms may keep the profit.", "Spending raises AD; spending has an opportunity cost."], a: 0, why: "Side 2 is just the reverse of side 1 with no new argument. Mark schemes say that a simple reversal earns little." },
] });

/* ================= PAST QUESTIONS ================= */
const PQ = [
  { ref: "Paper 21 · Oct/Nov 2020 · Q2(d)", m: 8, q: "Discuss whether or not lower taxes on firms will be beneficial for an economy.", ch: "26.3, 26.4, 26.8", lev: "What firms do with the money, what the government loses",
    yes: "Higher after-tax profits raise firms' ability and incentive to invest; firms may expand output and take on more workers; investment may raise innovation and productivity.",
    no: "Firms may keep the profit instead of investing; the government gets less revenue to spend; foreign firms attracted by low taxes may replace local ones; capital may replace labour; more output may cause pollution." },
  { ref: "Paper 21 · May/June 2020 · Q5(d)", m: 8, q: "Discuss whether or not an increase in government spending will reduce unemployment.", ch: "26.2, 26.8", lev: "Spare capacity, what it is spent on",
    yes: "Higher AD encourages firms to hire; spending on education raises skills; spending on healthcare may make workers fitter and more employable; subsidies to firms encourage output and hiring.",
    no: "Benefits may encourage some people to leave jobs; if the economy is already at full employment it may just raise prices; education spending may build the wrong skills; firms may respond to higher demand by using more capital rather than labour." },
  { ref: "Paper 21 · Oct/Nov 2021 · Q5(d)", m: 8, q: "Discuss whether or not high government spending can help a government achieve its macroeconomic aims.", ch: "25.1, 26.2, 26.8", lev: "Conflict between aims, cost and borrowing",
    yes: "Higher AD may raise economic growth; infrastructure and education may increase demand for workers and skills; welfare spending may redistribute income.",
    no: "Extra demand could raise inflation; government spending may reduce private investment; reliance on subsidies may breed complacency; welfare may reduce the incentive to look for work; higher taxes may be a disincentive; a bigger deficit may reduce confidence." },
  { ref: "Paper 23 · Oct/Nov 2021 · Q2(d)", m: 8, q: "Discuss whether or not indirect taxation can reduce market failure.", ch: "14, 26.3, 26.4", lev: "Elasticity, size of tax, use of revenue",
    yes: "Demerit goods are over-consumed with external costs, so a tax discourages them; revenue can subsidise merit goods or fund public goods that the private sector would not provide.",
    no: "External costs are hard to measure; demerit goods may be over-taxed; demand for some is inelastic; indirect taxes may fall most on the poor; demand may move to imports where taxes are lower; revenue may not be spent on merit or public goods." },
  { ref: "Paper 22 · Feb/Mar 2022 · Q1(h)", m: 6, q: "Discuss whether or not higher indirect taxes can reduce the market failure caused by demerit goods.", ch: "14, 26.3", lev: "Elasticity, avoidance",
    yes: "Demerit goods are more harmful than consumers realise and are over-produced and over-consumed; a tax raises costs and price and cuts consumption towards where social cost equals social benefit; revenue can fund campaigns.",
    no: "Behaviour is hard to change, especially for addictive goods and high-income consumers; demand may be inelastic; firms may not pass the tax on, and illegal markets may grow; it is hard to find the right level of output." },
  { ref: "Paper 23 · May/June 2023 · Q2(d)", m: 8, q: "Discuss whether or not low tax rates benefit an economy.", ch: "26.3, 26.4, 26.6", lev: "Which tax (income, corporation, indirect), lost revenue",
    yes: "Low corporation tax encourages investment, productivity and demand for labour; low income tax encourages more people into the labour force and raises disposable income and spending.",
    no: "Less revenue means less spending on public goods and infrastructure, which could reduce investment and productivity; more production may add to pollution and environmental damage." },
  { ref: "Paper 21 · Oct/Nov 2023 · Q3(d)", m: 8, q: "Discuss whether or not a tax on a product can reduce external costs.", ch: "14, 26.3, 26.6", lev: "Elasticity, size of tax, avoidance",
    yes: "The tax raises price and cuts quantity demanded, more so if demand is elastic; it raises costs and reduces supply and profits; revenue can subsidise cleaner alternatives.",
    no: "The tax may be small compared with the final price; avoidance, evasion or illegal markets; if demand is inelastic (for example, addictive products) quantity may hardly change." },
  { ref: "Paper 22 · May/June 2024 · Q5(d)", m: 8, q: "Discuss whether or not an increase in government spending on housing would benefit an economy.", ch: "24, 26.2, 26.8", lev: "Opportunity cost, financing, spare capacity",
    yes: "Higher AD, output and employment; lower housing prices; fewer people without a home.",
    no: "Opportunity cost; may need higher taxes; the quality of the housing may be poor; the private sector may build better homes; external costs during construction." },
  { ref: "Paper 23 · May/June 2024 · Q4(d)", m: 8, q: "Discuss whether or not a government should increase its spending on healthcare.", ch: "14, 24, 26.2", lev: "Opportunity cost, efficiency, deficit",
    yes: "Healthcare is a merit good that may be under-consumed; poorer people may not afford it; a healthier population may be more productive; more jobs in healthcare; extra AD; possibly more tax revenue.",
    no: "The cost may cause a budget deficit or need higher taxes; opportunity cost such as education; the private sector may be more efficient; more spending does not guarantee better quality." },
  { ref: "Paper 23 · Oct/Nov 2024 · Q3(d)", m: 8, q: "Discuss whether or not a government should tax sports equipment.", ch: "26.3, 26.4, 26.5", lev: "Who pays, merit goods, jobs",
    yes: "Extra tax revenue; other leisure goods are taxed; sports equipment is not a necessity; richer people may spend more on it; elite sports people can afford higher prices.",
    no: "Higher prices may discourage people on low incomes from playing; sport may be a merit good that improves health and fitness; lower output could cost jobs in sport and leisure industries." },
];
(function () {
  const el = $("#pq");
  el.innerHTML = PQ.map((p, i) => `<details class="eq"><summary>${i + 1} <span class="cmd">Discuss</span> <span class="mark">${p.m} marks</span> ${esc(p.q)}</summary><div class="body">
    <p class="note">${p.ref} · coursebook sections ${p.ch}</p>
    <div class="tip"><b class="h">Plan first</b>Write two reasons for, two against, and one angle for each, in a few words. Then look below.</div>
    <div class="grid2"><div class="card" style="border-top:4px solid var(--good)"><h3>Why it might (examiners credited)</h3><p>${esc(p.yes)}</p></div>
    <div class="card" style="border-top:4px solid var(--bad)"><h3>Why it might not (examiners credited)</h3><p>${esc(p.no)}</p></div></div>
    <div class="verdict">Your conclusion could depend on: ${esc(p.lev)}.</div>
    <p class="note">Summarised from the published mark scheme. Check your own plan against it, then write the answer and use the Level checker on the Explore tab.</p>
  </div></details>`).join("");
})();

/* ================= FLASHCARDS ================= */
Lib.cards($("#fc1"), { cards: [
  ["Spare capacity", "Unused resources. If there is a lot, extra demand is likely to raise output; if there is little, it could mainly raise prices."],
  ["Time lag", "The delay between a policy and its effect. Spending on education may take years to raise productivity."],
  ["Multiplier leakage", "Income that is saved, taxed or spent on imports instead of being spent again at home. More leakage means a smaller multiplier."],
  ["Elastic demand (tax)", "Buyers react a lot to a price rise, so an indirect tax cuts quantity by a lot and producers bear more of the tax."],
  ["Inelastic demand (tax)", "Buyers react little, so quantity barely falls, consumers bear most of the tax and the external cost may remain."],
  ["Opportunity cost (policy)", "What the government gives up by choosing one use of funds, for example housing instead of healthcare."],
  ["Budget deficit (cost)", "Extra spending or lower taxes may widen the deficit, so the government might have to borrow or raise taxes later."],
  ["Disincentive effect", "Higher taxes may reduce people's incentive to work, save or invest, reducing the benefit of the tax."],
  ["Avoidance and evasion", "Ways of paying less tax, legally or illegally, which may reduce the revenue and the behavioural effect of a tax."],
  ["Regressive effect", "Indirect taxes may take a larger percentage from poorer households, so equity may suffer."],
  ["Short run and long run", "An effect that appears quickly (a tax cut raising spending) may differ from one that takes years (education raising productivity)."],
  ["Judgement", "A conclusion that weighs the sides, picks the likelier outcome and names the condition and the reason."],
] });
labA(); labB();
