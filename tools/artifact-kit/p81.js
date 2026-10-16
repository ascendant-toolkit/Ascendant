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
const WPS = ["Number ← 20", "WHILE Number > 9 DO", "    Number ← Number - 9", "ENDWHILE", "OUTPUT Number"];
const WPY = ["number = 20", "while number > 9:", "    number = number - 9", "print(number)"];
const RPS = ["REPEAT", "    OUTPUT \"Enter the password\"", "    INPUT Password", "UNTIL Password = \"Secret\"", "OUTPUT \"Access granted\""];
const RPY = ["while True:", "    print(\"Enter the password\")", "    password = input()", "    if password == \"Secret\":", "        break", "print(\"Access granted\")"];

/* ---------- 1/2. loops ---------- */
function lv(title, vars, o) {
  let s = SV.text(14, 26, title, "lbl bd", { "text-anchor": "start" }); if (o.right) s += SV.text(626, 26, o.right, "lbl bd t4", { "text-anchor": "end" });
  vars.forEach(([n, v], i) => { const x = 40 + i * 190; s += SV.rect(x, 60, 170, 70, "", { rx: 10, style: `fill:var(--soft);stroke:${o.hi === i ? "var(--accent)" : "var(--line)"};stroke-width:${o.hi === i ? 4 : 2}` }) + sm(x + 85, 82, n) + SV.text(x + 85, 116, String(v), "lbl bd", { "text-anchor": "middle", style: "font-size:24px;font-family:var(--mono)" }); });
  if (o.cond) s += SV.rect(40, 150, 560, 46, "", { rx: 10, style: `fill:${o.ok === true ? "var(--good-soft)" : o.ok === false ? "var(--bad-soft)" : "var(--surface)"};stroke:var(--line);stroke-width:2` }) + SV.text(320, 180, o.cond, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:14px" });
  if (o.note) s += SV.text(320, 225, o.note, "lbl bd " + (o.nc || ""), { "text-anchor": "middle" });
  return s;
}
function wFrames() {
  const F = [], f = (cap, ps, py, vars, o) => F.push({ cap, ps, py, svg: lv("WHILE loop", vars, o) });
  f("<b>Number ← 20</b>.", [0], [0], [["Number", 20]], { hi: 0 });
  f("The condition is tested <b>first</b>: is 20 &gt; 9? <b>TRUE</b>, so the loop body runs.", [1], [1], [["Number", 20]], { cond: "20 > 9 ?  TRUE", ok: true, right: "Passes: 0" });
  f("<b>Number ← 20 − 9 = 11</b>.", [2], [2], [["Number", 11]], { hi: 0, right: "Passes: 1" });
  f("Back to the top: is 11 &gt; 9? <b>TRUE</b>, so it runs again.", [1], [1], [["Number", 11]], { cond: "11 > 9 ?  TRUE", ok: true, right: "Passes: 1" });
  f("<b>Number ← 11 − 9 = 2</b>.", [2], [2], [["Number", 2]], { hi: 0, right: "Passes: 2" });
  f("Is 2 &gt; 9? <b>FALSE</b>. The loop stops without running the body again.", [1, 3], [1], [["Number", 2]], { cond: "2 > 9 ?  FALSE", ok: false, right: "Passes: 2" });
  f("<b>OUTPUT Number</b> shows 2. If Number had started at 5, the body would never have run.", [4], [3], [["Number", 2]], { note: "Output: 2", nc: "t3" });
  return F;
}
Lib.algo($("#aW"), { w: 640, h: 240, label: "WHILE loop animation", pseudo: WPS, py: WPY, dwell: 2200, frames: wFrames() });
function rFrames() {
  const F = [], f = (cap, ps, py, vars, o) => F.push({ cap, ps, py, svg: lv("REPEAT loop", vars, o) });
  f("<b>REPEAT</b> starts. There is no test yet: the body runs <b>first</b>.", [0], [0], [["Password", "–"]], {});
  f("Prompt: <b>Enter the password</b>.", [1], [1], [["Password", "–"]], { note: "Enter the password", nc: "t1" });
  f("The user types <b>abc</b>. INPUT Password.", [2], [2], [["Password", '"abc"']], { hi: 0 });
  f("<b>UNTIL</b> Password = \"Secret\" is tested <b>after</b> the body: <b>FALSE</b>, so the loop repeats.", [3], [3, 4], [["Password", '"abc"']], { cond: '"abc" = "Secret" ?  FALSE', ok: false, right: "Passes: 1" });
  f("The body runs again: prompt, then INPUT. The user types <b>Secret</b>.", [1, 2], [1, 2], [["Password", '"Secret"']], { hi: 0, right: "Passes: 2" });
  f("UNTIL \"Secret\" = \"Secret\" is <b>TRUE</b>, so the loop ends.", [3], [3, 4], [["Password", '"Secret"']], { cond: '"Secret" = "Secret" ?  TRUE', ok: true, right: "Passes: 2" });
  f("<b>OUTPUT</b> Access granted. The loop ran at least once, always.", [4], [5], [["Password", '"Secret"']], { note: "Access granted", nc: "t3" });
  return F;
}
Lib.algo($("#aR"), { w: 640, h: 240, label: "REPEAT loop animation", pseudo: RPS, py: RPY, dwell: 2400, frames: rFrames() });

/* ---------- 3. function call ---------- */
function fnChart(s) {
  const k = Math.round(s.k); let o = panel(15, 25, 330, 220, "Main program", MUT) + panel(405, 25, 340, 220, "FUNCTION SumSquare(Number1, Number2)", k >= 1 && k <= 3 ? ACC : MUT);
  o += SV.text(180, 85, 'OUTPUT "Sum of squares = ", ', "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:12px" }) + SV.text(180, 115, k >= 4 ? "500" : "SumSquare(10, 20)", "lbl bd", { "text-anchor": "middle", style: `font-family:var(--mono);font-size:16px;fill:${k === 0 || k === 4 ? ACC : "var(--ink)"}` });
  if (k >= 4) o += SV.text(180, 160, "Sum of squares = 500", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  if (k >= 1) o += SV.text(575, 80, "Number1 = 10", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + SV.text(575, 105, "Number2 = 20", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  if (k >= 2) o += SV.text(575, 150, "10 * 10 + 20 * 20", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + SV.text(575, 175, "= 100 + 400 = 500", "lbl bd t1", { "text-anchor": "middle", style: "font-family:var(--mono)" });
  if (k === 3) o += SV.text(575, 215, "RETURN 500", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
  if (k === 1) o += arr(345, 120, 405, 120, ACC); if (k === 3 || k === 4) o += arr(405, 200, 345, 200, GOOD);
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 265, label: "Calling a function with parameters", base: { k: 0 }, tween: 1, dwell: 3600, draw: fnChart, steps: [
  { cap: "The main program reaches an expression containing the <b>function call</b> SumSquare(10, 20). The output cannot be completed until the function gives back a value.", s: { k: 0 } },
  { cap: "Control passes to the function. The values 10 and 20 are passed in as the <b>parameters</b> Number1 and Number2.", s: { k: 1 } },
  { cap: "The function runs its statements: 10 × 10 + 20 × 20 = 500.", s: { k: 2 } },
  { cap: "<b>RETURN 500</b> sends the value back to the point where the function was called.", s: { k: 3 } },
  { cap: "The returned value <b>replaces the call</b> in the expression, so the program outputs <b>Sum of squares = 500</b>. A procedure would not return a value.", s: { k: 4 } },
] });

/* ---------- 4. scope ---------- */
function scChart(s) {
  const k = Math.round(s.k); let o = panel(15, 25, 340, 205, "Program (global scope)", ACC) + SV.text(185, 78, "Total = " + (k >= 4 ? 25 : 0), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + sm(185, 98, "global variable: usable anywhere");
  o += SV.text(185, 135, k >= 1 ? "CALL AddBonus(25)" : "", "lbl", { "text-anchor": "middle", style: `font-family:var(--mono);fill:${k === 1 ? ACC : "var(--ink)"}` });
  if (k >= 2 && k <= 3) o += panel(420, 25, 330, 205, "PROCEDURE AddBonus(Bonus)", GOOD) + SV.text(585, 85, "Bonus = 25  (parameter)", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" }) + SV.text(585, 115, "Temp = 25  (local)", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" }) + SV.text(585, 150, k === 3 ? "Total ← Total + Temp" : "Temp ← Bonus", "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
  if (k >= 4) o += panel(420, 25, 330, 205, "Procedure has finished", MUT, 0.4) + sm(585, 110, "Temp and Bonus no longer exist") + sm(585, 130, "(local variables are gone)");
  if (k >= 2 && k <= 3) o += arr(355, 130, 420, 130, ACC);
  o += note(380, 255, ["The global variable Total can be used anywhere", "The procedure is called with 25", "Local variables Bonus and Temp are created", "The procedure can use Total (global) and Temp (local)", "Total has changed; the locals have disappeared"][k], "t1");
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 270, label: "Local and global variables", base: { k: 0 }, tween: 1, dwell: 3600, draw: scChart, steps: [
  { cap: "<b>Total</b> is a <b>global</b> variable. Any part of the program can read or change it.", s: { k: 0 } },
  { cap: "The program calls the procedure AddBonus with the value 25.", s: { k: 1 } },
  { cap: "Inside the procedure, the parameter <b>Bonus</b> and the <b>local</b> variable <b>Temp</b> are created. They exist <b>only here</b>.", s: { k: 2 } },
  { cap: "The procedure can use both its local variable and the global variable <b>Total</b>.", s: { k: 3 } },
  { cap: "When the procedure ends, its <b>local variables are gone</b>. The main program cannot use Temp, but the global Total keeps its new value.", s: { k: 4 } },
] });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdDecl"), { pseudo: ["DECLARE Counter : INTEGER", "DECLARE Price : REAL", "DECLARE GameOver : BOOLEAN", "CONSTANT HourlyRate ← 6.50", "Counter ← 0", "Counter ← Counter + 1", "TotalToPay ← NumberOfHours * HourlyRate"], py: ["counter = 0", "price = 0.0", "game_over = False", "HOURLY_RATE = 6.50", "counter = 0", "counter = counter + 1", "total_to_pay = number_of_hours * HOURLY_RATE"] });
Lib.codePanel($("#cdCase"), { pseudo: ["INPUT Move", "CASE OF Move", "    'W' : Position ← Position - 10", "    'E' : Position ← Position + 10", "    'A' : Position ← Position - 1", "    'D' : Position ← Position + 1", '    OTHERWISE OUTPUT "Beep"', "ENDCASE"], py: ["move = input()", 'if move == "W":', "    position = position - 10", 'elif move == "E":', "    position = position + 10", 'elif move == "A":', "    position = position - 1", 'elif move == "D":', "    position = position + 1", "else:", '    print("Beep")'] });
Lib.codePanel($("#cdFor"), { pseudo: ["FOR Count ← 1 TO 5", "    OUTPUT Count", "NEXT Count"], py: ["for count in range(1, 6):", "    print(count)"] });
Lib.codePanel($("#cdWhile"), { pseudo: ["WHILE Number > 9 DO", "    Number ← Number - 9", "ENDWHILE"], py: ["while number > 9:", "    number = number - 9"] });
Lib.codePanel($("#cdRep"), { pseudo: ["REPEAT", "    INPUT Password", 'UNTIL Password = "Secret"'], py: ["while True:", "    password = input()", '    if password == "Secret":', "        break"] });
Lib.codePanel($("#cdStr"), { pseudo: ['Word ← "Happy Days"', "OUTPUT LENGTH(Word)", "OUTPUT UCASE(Word)", "OUTPUT SUBSTRING(Word, 1, 5)"], py: ['word = "Happy Days"', "print(len(word))", "print(word.upper())", "print(word[0:5])"] });
Lib.codePanel($("#cdNest"), { pseudo: ["FOR Row ← 1 TO 3", "    FOR Column ← 1 TO 4", "        IF Row = Column", "          THEN", '            OUTPUT "X"', "        ENDIF", "    NEXT Column", "NEXT Row"], py: ["for row in range(1, 4):", "    for column in range(1, 5):", "        if row == column:", '            print("X")'] });
Lib.codePanel($("#cdProc"), { pseudo: ["PROCEDURE Line(Size : INTEGER)", "    DECLARE Length : INTEGER", "    FOR Length ← 1 TO Size", "        OUTPUT '-'", "    NEXT Length", "ENDPROCEDURE", "CALL Line(60)"], py: ["def line(size):", "    for length in range(size):", '        print("-", end="")', "", "line(60)"] });
Lib.codePanel($("#cdFunc"), { pseudo: ["FUNCTION SumSquare(Number1 : INTEGER, Number2 : INTEGER) RETURNS INTEGER", "    RETURN Number1 * Number1 + Number2 * Number2", "ENDFUNCTION", 'OUTPUT "Sum of squares = ", SumSquare(10, 20)'], py: ["def sum_square(number1, number2):", "    return number1 * number1 + number2 * number2", "", 'print("Sum of squares =", sum_square(10, 20))'] });
Lib.codePanel($("#cdScope"), { pseudo: ["DECLARE Total : INTEGER          // global", "Total ← 0", "PROCEDURE AddBonus(Bonus : INTEGER)", "    DECLARE Temp : INTEGER      // local", "    Temp ← Bonus", "    Total ← Total + Temp", "ENDPROCEDURE", "CALL AddBonus(25)"], py: ["total = 0                  # global", "def add_bonus(bonus):", "    global total", "    temp = bonus               # local", "    total = total + temp", "", "add_bonus(25)"] });

/* ---------- Lab 1 ---------- */
chooser($("#sn"), $("#sv"), ["INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN"], [
  ["42", "INTEGER"], ["3.14", "REAL"], ["'A'", "CHAR"], ['"Hello"', "STRING"], ["TRUE", "BOOLEAN"], ['"2025"', "STRING"], ["−7", "INTEGER"], ["0.0", "REAL"], ['"A"', "STRING"], ["FALSE", "BOOLEAN"],
]);

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  function upd() {
    if (!a || !b) return; const x = a.get(), y = b.get() || 1;
    const R = [["A + B", x + y], ["A − B", x - y], ["A * B", x * y], ["A / B", fmtN(x / y, 3)], ["A ^ 2", x ** 2], ["DIV(A, B)", Math.floor(x / y)], ["MOD(A, B)", ((x % y) + y) % y], ["ROUND(A / B, 1)", fmtN(Math.round((x / y) * 10) / 10, 1)], ["A = B", String(x === y).toUpperCase()], ["A > B", String(x > y).toUpperCase()], ["A <> B", String(x !== y).toUpperCase()], ["(A > 5) AND (B > 5)", String(x > 5 && y > 5).toUpperCase()], ["(A > 5) OR (B > 5)", String(x > 5 || y > 5).toUpperCase()], ["NOT (A > B)", String(!(x > y)).toUpperCase()]];
    $("#ot").innerHTML = `<tr><th>Expression</th><th>Result</th></tr>` + R.map((r) => `<tr><td>${r[0]}</td><td><b>${r[1]}</b></td></tr>`).join("");
  }
  a = Lib.slider($("#o1"), { id: "oa", label: "A", min: 0, max: 50, value: 17, onInput: upd }); b = Lib.slider($("#o2"), { id: "ob", label: "B", min: 1, max: 20, value: 5, onInput: upd }); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let st, ln; const inp = $("#sx");
  function upd() {
    if (!st || !ln) return; const s = inp.value, base = +($("[name=bs]:checked").value), n = s.length, start = Math.min(st.get(), Math.max(base, n - 1 + base)), len = ln.get(), a = start - base, sub = s.substr(a, len);
    let g = ""; const w = Math.min(36, 600 / Math.max(n, 1));
    [...s].forEach((c, i) => { const x = 20 + i * (w + 4), on = i >= a && i < a + len; g += SV.rect(x, 20, w, 40, "", { rx: 6, style: `fill:${on ? "var(--accent-soft)" : "var(--soft)"};stroke:${on ? "var(--accent)" : "var(--line)"};stroke-width:${on ? 3 : 1.5}` }) + SV.text(x + w / 2, 47, c === " " ? "␣" : c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px" }) + SV.text(x + w / 2, 80, i + base, "sm", { "text-anchor": "middle" }); });
    $("#ss").innerHTML = g;
    $("#st").innerHTML = `<tr><th>Expression</th><th>Result</th></tr><tr><td>LENGTH(Word)</td><td>${n}</td></tr><tr><td>UCASE(Word)</td><td>"${esc(s.toUpperCase())}"</td></tr><tr><td>LCASE(Word)</td><td>"${esc(s.toLowerCase())}"</td></tr><tr><td>SUBSTRING(Word, ${start}, ${len})</td><td>"${esc(sub)}"</td></tr>`;
  }
  st = Lib.slider($("#s1"), { id: "ssl", label: "Start position", min: 0, max: 19, value: 1, onInput: upd }); ln = Lib.slider($("#s2"), { id: "sll", label: "Length", min: 1, max: 20, value: 5, onInput: upd });
  inp.addEventListener("input", upd); $$("[name=bs]").forEach((r) => r.addEventListener("change", upd)); upd();
})();

/* ---------- Lab 4 ---------- */
(() => {
  let r, c;
  function upd() {
    if (!r || !c) return; const R = r.get(), C = c.get();
    Lib.codePanel($("#nc"), { pseudo: [`FOR Row ← 1 TO ${R}`, `    FOR Column ← 1 TO ${C}`, '        OUTPUT "*"', "    NEXT Column", "    OUTPUT NewLine", "NEXT Row"], py: [`for row in range(1, ${R + 1}):`, `    for column in range(1, ${C + 1}):`, '        print("*", end="")', "    print()"] });
    $("#na").textContent = R; $("#nb").textContent = R * C; $("#ng").innerHTML = Array.from({ length: R }, () => "*".repeat(C)).join("<br>");
  }
  r = Lib.slider($("#n1"), { id: "nr", label: "Rows", min: 1, max: 8, value: 3, onInput: upd }); c = Lib.slider($("#n2"), { id: "nc2", label: "Columns", min: 1, max: 12, value: 5, onInput: upd }); upd();
})();

/* ---------- Lab 5 ---------- */
chooser($("#sn2"), $("#sv2"), ["FOR loop", "WHILE loop", "REPEAT loop"], [
  ["Print the 12 times table", "FOR loop"], ["Keep asking for a password until it is correct", "REPEAT loop"], ["Add up marks while the user has not typed −1", "WHILE loop"], ["Process every element of an array of 30 values", "FOR loop"],
  ["Subtract 9 from a number while it is greater than 9 (it may already be small)", "WHILE loop"], ["Show a menu at least once, then again until the user quits", "REPEAT loop"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sequence, selection or iteration?", buckets: [{ label: "Sequence" }, { label: "Selection" }, { label: "Iteration" }], items: [
  { text: "Statements run one after another in order", b: 0 },
  { text: "INPUT, then a calculation, then OUTPUT", b: 0 },
  { text: "IF ... THEN ... ELSE", b: 1 },
  { text: "CASE OF ... ENDCASE", b: 1 },
  { text: "Choosing which code to run depending on a condition", b: 1 },
  { text: "FOR ... NEXT", b: 2 },
  { text: "WHILE ... ENDWHILE", b: 2 },
  { text: "REPEAT ... UNTIL", b: 2 },
], done: "In order, choose, repeat." });

Lib.classify($("#cl2"), { prompt: "Procedure or function?", buckets: [{ label: "Procedure" }, { label: "Function" }], items: [
  { text: "Returns a single value", b: 1 },
  { text: "Contains a RETURN statement", b: 1 },
  { text: "Called as part of an expression", b: 1 },
  { text: "Definition includes RETURNS and a data type", b: 1 },
  { text: "Called with CALL", b: 0 },
  { text: "Does a task but gives nothing back", b: 0 },
  { text: "Defined with PROCEDURE ... ENDPROCEDURE", b: 0 },
], done: "A function gives a value back; a procedure does not." });

Lib.classify($("#cl3"), { prompt: "Local or global variable?", buckets: [{ label: "Local" }, { label: "Global" }], items: [
  { text: "Can be used anywhere in the program", b: 1 },
  { text: "Declared at the start of the main program", b: 1 },
  { text: "Exists for the whole time the program runs", b: 1 },
  { text: "Declared inside a procedure", b: 0 },
  { text: "Only usable inside the routine that declares it", b: 0 },
  { text: "Disappears when the routine ends", b: 0 },
], done: "Scope: the routine or the whole program." });

Lib.match($("#m1"), { prompt: "Match each expression to its result.", pairs: [
  ["DIV(17, 5)", "3"],
  ["MOD(17, 5)", "2"],
  ["2 ^ 5", "32"],
  ["LENGTH(\"Computer\")", "8"],
  ["UCASE(\"cat\")", "\"CAT\""],
  ["SUBSTRING(\"Computer\", 1, 3)", "\"Com\""],
  ["ROUND(3.14159, 2)", "3.14"],
  ["NOT TRUE", "FALSE"]
] });

Lib.order($("#o1"), { prompt: "Put these lines in order to keep asking for a number from 1 to 10 until a valid one is entered.", items: [
  "REPEAT",
  "    OUTPUT \"Enter a number from 1 to 10\"",
  "    INPUT Number",
  "UNTIL Number >= 1 AND Number <= 10",
  "OUTPUT \"Thank you\""
], done: "REPEAT, prompt, input, test at the end, then continue." });

Lib.calc($("#c1"), { qs: [
  { q: "What is DIV(23, 4)?", a: 5, sol: "23 ÷ 4 = 5 remainder 3. DIV gives 5." },
  { q: "What is MOD(23, 4)?", a: 3, sol: "The remainder is 3." },
  { q: "What is 3 ^ 4?", a: 81, sol: "3 × 3 × 3 × 3 = 81." },
  { q: "What is ROUND(7.846, 1)?", a: 7.8, sol: "7.846 to one decimal place is 7.8." },
  { q: "How many times does FOR Count ← 3 TO 12 run its loop body?", a: 10, sol: "Count takes the values 3, 4, ..., 12: 10 times." },
  { q: "Number ← 40. WHILE Number > 9: Number ← Number − 9. What is Number at the end?", a: 4, sol: "40 → 31 → 22 → 13 → 4. At 4 the condition fails." },
  { q: "How many times does the body run? Count ← 5. REPEAT Count ← Count + 1 UNTIL Count > 3", a: 1, sol: "The body always runs once. After it, Count is 6, and 6 > 3 is TRUE, so it stops." },
  { q: "What is LENGTH(\"Hello World\")?", a: 11, sol: "Hello (5) + space (1) + World (5) = 11." },
  { q: "What is SUBSTRING(\"Computer\", 4, 3)? (first position is 1)", t: ["PUT"], ph: "3 letters", sol: "Characters 4, 5 and 6 of Computer (C-o-m-p-u-t-e-r) are p, u, t: put.", hint: "Count along from position 1." },
  { q: "What is UCASE(\"Pi3\")?", t: ["PI3"], ph: "text", sol: "Upper case: PI3." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which data type stores TRUE or FALSE?", opts: ["BOOLEAN", "CHAR", "STRING", "REAL"], a: 0, why: "BOOLEAN." },
  { q: "Which loop always runs at least once?", opts: ["REPEAT", "WHILE", "FOR from 5 to 1", "None"], a: 0, why: "REPEAT tests its condition at the end." },
  { q: "Which loop is best when you know the number of repeats?", opts: ["FOR", "WHILE", "REPEAT", "CASE"], a: 0, why: "A FOR loop is count-controlled." },
  { q: "What does a function do that a procedure does not?", opts: ["Returns a value", "Has parameters", "Has a name", "Uses a loop"], a: 0, why: "It returns a value." },
  { q: "What is a parameter?", opts: ["A value passed to a procedure or function", "A kind of loop", "A comment", "A constant"], a: 0, why: "Parameters carry values in when a routine is called." },
  { q: "Where can a local variable be used?", opts: ["Only in the routine where it is declared", "Anywhere", "Only in loops", "Only in IF statements"], a: 0, why: "Its scope is the routine." },
  { q: "What does MOD return?", opts: ["The remainder", "The quotient", "The product", "The sign"], a: 0, why: "The remainder after division." },
  { q: "Which makes a program more maintainable?", opts: ["Meaningful identifiers and comments", "Single-letter names", "No indentation", "No procedures"], a: 0, why: "Clear names and comments make code readable." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Variable", "A named storage location whose value can change while the program runs."],
  ["Constant", "A named value that does not change while the program runs."],
  ["INTEGER", "A whole number."],
  ["REAL", "A number with a fractional part."],
  ["CHAR", "A single character."],
  ["STRING", "A sequence of zero or more characters."],
  ["BOOLEAN", "TRUE or FALSE."],
  ["Sequence", "Statements run one after another in order."],
  ["Selection", "Choosing which statements to run: IF or CASE."],
  ["Iteration", "Repeating statements: FOR, WHILE or REPEAT."],
  ["Count-controlled loop", "A FOR loop that repeats a set number of times."],
  ["Pre-condition loop", "A WHILE loop: the condition is tested before each pass."],
  ["Post-condition loop", "A REPEAT loop: the condition is tested after each pass, so it runs at least once."],
  ["Procedure", "A named block of code that performs a task and does not return a value."],
  ["Function", "A named block of code that returns a single value."],
  ["Parameter", "A value passed into a procedure or function."],
  ["Local variable", "A variable that can only be used inside the routine that declares it."],
  ["Global variable", "A variable that can be used anywhere in the program."],
  ["Library routine", "A ready-made routine such as MOD, DIV, ROUND or RANDOM."]
] });
