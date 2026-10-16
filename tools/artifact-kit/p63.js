const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
/* ---------- 1. expert system ---------- */
function esChart(s) {
  const k = Math.round(s.k), on = (a) => (a ? ACC : MUT);
  let o = panel(15, 55, 175, 120, "Interface", on(k === 1 || k === 4), 1) + panel(280, 70, 180, 110, "Inference engine", on(k === 2 || k === 3)) + panel(550, 15, 195, 100, "Knowledge base", on(k === 3)) + panel(550, 140, 195, 100, "Rule base", on(k === 2));
  o += sm(102, 110, "User answers:") + sm(102, 132, k >= 1 ? "lights dim" : "") + sm(102, 150, k >= 1 ? "engine clicks" : "");
  o += sm(370, 130, k >= 2 ? "match rule to facts" : "applies the rules") + sm(370, 152, k >= 3 ? "to the knowledge base" : "");
  o += sm(647, 62, "Flat battery: lights dim") + sm(647, 80, "Low power: starter clicks") + sm(647, 98, "Starter fault: no click");
  o += sm(647, 188, "IF lights dim AND engine clicks") + sm(647, 206, "THEN fault ← flat battery");
  o += arr(190, 115, 280, 115, on(k === 1 || k === 2)) + arr(460, 100, 550, 70, on(k === 3)) + arr(460, 150, 550, 185, on(k === 2));
  if (k === 4) o += arr(280, 165, 190, 165, GOOD);
  o += note(380, 270, ["The four parts of an expert system", "The user answers questions through the interface", "The inference engine takes the answers and finds a rule that matches", "It searches the knowledge base using that rule", "Conclusion shown: probably a flat battery"][k], k === 4 ? "t3" : "t1");
  if (k === 4) o += chip(40, 195, 140, "Flat battery (85%)", GOOD);
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 285, label: "How an expert system diagnoses a car that will not start", base: { k: 0 }, tween: 1, dwell: 3800, draw: esChart, steps: [
  { cap: "A car expert system has four parts: the <b>interface</b>, the <b>inference engine</b>, the <b>knowledge base</b> (facts) and the <b>rule base</b> (IF-THEN rules).", s: { k: 0 } },
  { cap: "The <b>user</b> answers the system's questions through the interface: \"The lights are dim\" and \"the engine clicks\".", s: { k: 1 } },
  { cap: "The <b>inference engine</b> uses the <b>rule base</b>: IF lights dim AND engine clicks THEN flat battery.", s: { k: 2 } },
  { cap: "It checks the rule against the facts in the <b>knowledge base</b>.", s: { k: 3 } },
  { cap: "The conclusion, <b>probably a flat battery</b>, is returned through the interface to the user.", s: { k: 4 } },
] });

/* ---------- 2. machine learning ---------- */
const PX = (x) => 60 + x * 40, PY = (y) => 260 - y * 24;
const SPAM0 = [[6, 7], [7, 6], [8, 8], [6.5, 5.5]], NOT0 = [[2, 2], [3, 1], [1.5, 3], [2.5, 2.5]], SPAM1 = [[4.7, 5.5], [5, 4.6], [9, 7]], NOT1 = [[3.5, 4], [4, 3], [1, 1.5]];
const cen = (P) => [P.reduce((a, p) => a + p[0], 0) / P.length, P.reduce((a, p) => a + p[1], 0) / P.length];
function bnd(S, N) { const a = cen(S), b = cen(N); return { mx: (a[0] + b[0]) / 2, my: (a[1] + b[1]) / 2, ang: Math.atan2(a[1] - b[1], a[0] - b[0]) }; }
const B0 = bnd(SPAM0, NOT0), B1 = bnd(SPAM0.concat(SPAM1), NOT0.concat(NOT1));
function mlChart(s) {
  const k = Math.round(s.k);
  let o = SV.rect(60, 20, 400, 240, "", { style: "fill:var(--soft);stroke:var(--line);stroke-width:2" }) + sm(260, 285, "number of links") + SV.text(18, 140, "capital words", "sm", {});
  const dots = (P, col) => P.map((p) => SV.circle(PX(p[0]), PY(p[1]), 8, "", { style: `fill:${col}` })).join("");
  if (k >= 1) o += dots(SPAM0, "var(--bad)") + dots(NOT0, "var(--accent)");
  if (k >= 4) o += dots(SPAM1, "var(--bad)") + dots(NOT1, "var(--accent)");
  if (k >= 2) { const nx = Math.cos(s.ang), ny = Math.sin(s.ang), tx = -ny, ty = nx, cx = PX(s.mx), cy = PY(s.my); o += SV.line(cx - tx * 300, cy + ty * 300, cx + tx * 300, cy - ty * 300, "", { style: "stroke:var(--ink);stroke-width:3;stroke-dasharray:8 6", "clip-path": "url(#cp)" }); }
  o = `<defs><clipPath id="cp"><rect x="60" y="20" width="400" height="240"/></clipPath></defs>` + o;
  if (k >= 3) o += SV.text(PX(5.5), PY(5.2) + 8, "?", "lbl bd", { "text-anchor": "middle", style: "font-size:26px;fill:var(--ink)" });
  o += SV.circle(500, 50, 8, "", { style: "fill:var(--bad)" }) + SV.text(516, 55, "spam", "lbl", { "text-anchor": "start" }) + SV.circle(500, 80, 8, "", { style: "fill:var(--accent)" }) + SV.text(516, 85, "not spam", "lbl", { "text-anchor": "start" });
  o += SV.text(480, 140, ["", "Labelled examples", "The program has found a boundary", "New email ? falls on the spam side", "More examples: the boundary adapts"][k], "lbl bd t1", { "text-anchor": "start" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 295, label: "A machine learning spam filter", base: { k: 0, mx: B0.mx, my: B0.my, ang: B0.ang }, tween: 1000, dwell: 3800, draw: mlChart, steps: [
  { cap: "No rules have been written. The program will <b>learn from examples</b>.", s: { k: 0, mx: B0.mx, my: B0.my, ang: B0.ang } },
  { cap: "It is given <b>training data</b>: emails labelled spam (red) or not spam (blue), described by the number of links and capital words.", s: { k: 1, mx: B0.mx, my: B0.my, ang: B0.ang } },
  { cap: "It works out the <b>pattern</b>: a boundary between the two groups. Nobody wrote this rule.", s: { k: 2, mx: B0.mx, my: B0.my, ang: B0.ang } },
  { cap: "A <b>new email</b> arrives. It falls on the spam side, so it is classified as spam.", s: { k: 3, mx: B0.mx, my: B0.my, ang: B0.ang } },
  { cap: "As more labelled emails (and user corrections) arrive, the program <b>adapts its data</b> and the boundary moves, so it becomes more accurate.", s: { k: 4, mx: B1.mx, my: B1.my, ang: B1.ang } },
] });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdRule"), { pseudo: ["IF Lights = \"dim\" AND Engine = \"clicking\"", "  THEN", "    Fault ← \"flat battery\"", "ENDIF", "IF Lights = \"bright\" AND Engine = \"silent\"", "  THEN", "    Fault ← \"starter motor\"", "ENDIF"], py: ["if lights == \"dim\" and engine == \"clicking\":", "    fault = \"flat battery\"", "if lights == \"bright\" and engine == \"silent\":", "    fault = \"starter motor\""] });

/* ---------- Lab 1 ---------- */
(() => {
  const FACTS = [["flat", "The tyre is flat"], ["chain", "The chain has come off"], ["brake", "The brake blocks rub on the wheel"], ["gear", "The gears are stiff"]];
  const RULES = [["R1", "IF flat THEN pump up or repair the tyre", (f) => f.flat], ["R2", "IF chain THEN refit the chain", (f) => f.chain], ["R3", "IF brake AND NOT flat THEN adjust the brakes", (f) => f.brake && !f.flat], ["R4", "IF gear AND NOT chain THEN oil the chain and gears", (f) => f.gear && !f.chain]];
  const el = $("#ef"), rl = $("#er"), ev = $("#ev");
  el.innerHTML = FACTS.map((f) => `<label><input type="checkbox" data-f="${f[0]}"> ${f[1]}</label>`).join("");
  function upd() {
    const f = {}; $$("input", el).forEach((i) => (f[i.dataset.f] = i.checked)); const fired = RULES.filter((r) => r[2](f));
    rl.innerHTML = RULES.map((r) => `<div style="padding:5px 8px;margin:3px 0;border-radius:8px;border:1.5px solid ${fired.includes(r) ? "var(--good)" : "var(--line)"};background:${fired.includes(r) ? "var(--good-soft)" : "var(--surface)"}"><b>${r[0]}</b> ${r[1]}</div>`).join("");
    ev.innerHTML = fired.length ? `<b>Inference engine:</b> ${fired.length} rule${fired.length > 1 ? "s" : ""} matched the facts. Conclusion: ${fired.map((r) => r[1].split("THEN ")[1]).join("; ")}.` : Object.values(f).some(Boolean) ? "No rule matches these facts." : "Tick the facts you know. The inference engine will look for rules that match.";
  }
  $$("input", el).forEach((i) => i.addEventListener("change", upd)); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const svg = $("#ml"); let S = [], N = [], T = null, mode = "S";
  const X = (x) => 20 + x * 40, Y = (y) => 270 - y * 25;
  const pred = (p) => { if (!S.length || !N.length) return null; const a = cen(S), b = cen(N), ds = Math.hypot(p[0] - a[0], p[1] - a[1]), dn = Math.hypot(p[0] - b[0], p[1] - b[1]); return ds < dn ? "S" : "N"; };
  function draw() {
    let s = SV.rect(20, 20, 400, 250, "", { style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
    if (S.length && N.length) { const a = cen(S), b = cen(N), mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, ang = Math.atan2(a[1] - b[1], a[0] - b[0]), tx = -Math.sin(ang), ty = Math.cos(ang);
      s += `<defs><clipPath id="cp2"><rect x="20" y="20" width="400" height="250"/></clipPath></defs>` + SV.line(X(mx) - tx * 600, Y(my) + ty * 600, X(mx) + tx * 600, Y(my) - ty * 600, "", { style: "stroke:var(--ink);stroke-width:3;stroke-dasharray:8 6", "clip-path": "url(#cp2)" }); }
    S.forEach((p) => (s += SV.circle(X(p[0]), Y(p[1]), 7, "", { style: "fill:var(--bad)" }))); N.forEach((p) => (s += SV.circle(X(p[0]), Y(p[1]), 7, "", { style: "fill:var(--accent)" })));
    if (T) { const r = pred(T); s += SV.text(X(T[0]), Y(T[1]) + 9, "?", "lbl bd", { "text-anchor": "middle", style: "font-size:28px;fill:var(--ink)" }); }
    svg.innerHTML = s;
    $("#mc").textContent = S.length + N.length;
    let ok = 0; S.forEach((p) => pred(p) === "S" && ok++); N.forEach((p) => pred(p) === "N" && ok++);
    $("#ma").textContent = S.length && N.length ? Math.round((ok / (S.length + N.length)) * 100) + " %" : "–";
    const r = T ? pred(T) : null; $("#mt").textContent = !T ? "–" : r ? (r === "S" ? "Spam" : "Not spam") : "need both classes";
    $("#mv").innerHTML = !S.length || !N.length ? "Add at least one example of each class. The program works out the average of each group and draws a boundary between them." : `The program has <b>learned</b> from ${S.length + N.length} examples. Add more examples and watch the boundary move: this is the program <b>adapting its data</b>.`;
  }
  svg.addEventListener("click", (e) => { const r = svg.getBoundingClientRect(), sc = 440 / r.width, px = (e.clientX - r.left) * sc, py = (e.clientY - r.top) * sc; if (px < 20 || px > 420 || py < 20 || py > 270) return; const p = [(px - 20) / 40, (270 - py) / 25]; (mode === "S" ? S : N).push(p); draw(); });
  $("#cS").onclick = () => { mode = "S"; $("#cS").classList.add("pri"); $("#cN").classList.remove("pri"); }; $("#cN").onclick = () => { mode = "N"; $("#cN").classList.add("pri"); $("#cS").classList.remove("pri"); };
  const rnd = (a, b) => a + Math.random() * (b - a);
  $("#cR").onclick = () => { for (let i = 0; i < 5; i++) { S.push([rnd(5, 9.5), rnd(4.5, 9)]); N.push([rnd(0.5, 5), rnd(0.5, 5.5)]); } draw(); };
  $("#cT").onclick = () => { T = [rnd(1, 9), rnd(1, 9)]; draw(); }; $("#cC").onclick = () => { S = []; N = []; T = null; draw(); };
  draw();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does each statement describe an expert system or machine learning?", buckets: [{ label: "Expert system" }, { label: "Machine learning" }], items: [
  { text: "Has a knowledge base", b: 0 },
  { text: "Has a rule base of IF-THEN rules", b: 0 },
  { text: "Has an inference engine", b: 0 },
  { text: "Rules are written by human experts", b: 0 },
  { text: "Finds patterns from training data", b: 1 },
  { text: "Automatically adapts its own processes or data", b: 1 },
  { text: "Improves as it receives more examples", b: 1 },
  { text: "A spam filter that learns from corrections", b: 1 },
], done: "Rules written by people against patterns found from data." });

Lib.match($("#m1"), { prompt: "Match each part of an expert system to its purpose.", pairs: [
  ["Knowledge base", "Stores facts about the subject"],
  ["Rule base", "A set of IF-THEN rules"],
  ["Inference engine", "Applies the rules to the knowledge base to reach a conclusion"],
  ["Interface", "Lets the user enter information and see the result"]
] });

Lib.order($("#o1"), { prompt: "Put these steps of an expert system in order.", items: [
  "The user answers questions through the interface",
  "The inference engine takes the answers",
  "It uses the rule base to search the knowledge base",
  "A conclusion is reached",
  "The result is shown to the user"
], done: "Answers, engine, rules and knowledge, conclusion, output." });

Lib.order($("#o2"), { prompt: "Put the steps of machine learning in order.", items: [
  "A large set of labelled examples is collected",
  "The program finds patterns in the data",
  "The program is used on new data",
  "Mistakes and new data are fed back",
  "The program adapts and becomes more accurate"
], done: "Examples, patterns, use, feedback, adapt." });

Lib.calc($("#c1"), { qs: [
  { q: "A spam filter correctly classifies 17 of 20 test emails. What percentage is that?", a: 85, sol: "17 ÷ 20 × 100 = 85%." },
  { q: "An expert system has 24 rules. 6 are matched by a user's facts. What fraction (as a percentage) of the rules matched?", a: 25, sol: "6 ÷ 24 = 0.25 = 25%." },
  { q: "A machine learning program is trained on 1500 spam and 2500 non-spam emails. How many examples is that in total?", a: 4000, sol: "1500 + 2500 = 4000." },
  { q: "How many components does an expert system have?", a: 4, sol: "Knowledge base, rule base, inference engine, interface." },
  { q: "A rule base has 5 rules and each rule uses 2 facts from the knowledge base. How many fact checks if every rule is tested once?", a: 10, sol: "5 × 2 = 10." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "What does the inference engine do?", opts: ["Applies rules to the knowledge base", "Stores facts", "Prints results", "Draws the screen"], a: 0, why: "It applies the rules to the knowledge base to reach a conclusion." },
  { q: "What is stored in the rule base?", opts: ["IF-THEN rules", "Photos", "User names", "Passwords"], a: 0, why: "Rules for using the facts." },
  { q: "What is machine learning?", opts: ["A program that adapts its own processes or data", "A machine that learns at school", "A fast processor", "A type of robot"], a: 0, why: "It automatically adapts using data." },
  { q: "Which is a characteristic of AI?", opts: ["Data and rules, reasoning, and learning", "Only storage", "Only printing", "Only sensors"], a: 0, why: "AI collects data and rules, reasons, and can learn." },
  { q: "Which is a disadvantage of expert systems?", opts: ["They are expensive to build", "They work 24 hours a day", "They are consistent", "They hold expert knowledge"], a: 0, why: "They take a lot of effort and money to create." },
  { q: "A spam filter that improves from user corrections is an example of…", opts: ["Machine learning", "An expert system", "A router", "An actuator"], a: 0, why: "It adapts using data." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Artificial intelligence (AI)", "A branch of computer science dealing with the simulation of intelligent behaviours by computers."],
  ["Expert system", "An AI system that imitates a human expert using a knowledge base, rule base, inference engine and interface."],
  ["Knowledge base", "Part of an expert system that stores facts about the subject."],
  ["Rule base", "Part of an expert system that holds IF-THEN rules."],
  ["Inference engine", "Part of an expert system that applies the rules to the knowledge base to reach a conclusion."],
  ["Interface", "The part of an expert system the user uses to enter information and see results."],
  ["Machine learning", "When a program automatically adapts its own processes and/or data, learning from examples."],
  ["Training data", "Examples used to teach a machine learning program."]
] });
