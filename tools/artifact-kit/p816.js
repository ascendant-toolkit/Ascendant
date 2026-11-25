const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const fv = (v) => (v === null || v === undefined ? "?" : v === true ? "TRUE" : v === false ? "FALSE" : typeof v === "string" ? '"' + v + '"' : v);
/* One animation frame: variable boxes, optional character cells or input queue, a condition result, and the output so far. */
function trSvg(f, o) {
  const W = 640; let s = SV.text(14, 24, f.title || o.title || "", "lbl bd", { "text-anchor": "start" });
  if (f.right) s += SV.text(W - 14, 24, f.right, "lbl bd t4", { "text-anchor": "end" });
  const vs = f.vars || [], n = vs.length;
  if (n) {
    const gap = 10, w = Math.min(150, Math.floor((W - 28 - (n - 1) * gap) / n)), tot = n * w + (n - 1) * gap, x0 = (W - tot) / 2;
    vs.forEach(([k, v], i) => {
      const x = x0 + i * (w + gap), hi = (f.hl || []).includes(k), t = String(fv(v));
      s += SV.rect(x, 38, w, 58, "", { rx: 10, style: `fill:var(--surface);stroke:${hi ? ACC : MUT};stroke-width:${hi ? 4 : 2}` });
      s += SV.text(x + w / 2, 56, k, "sm", { "text-anchor": "middle" });
      s += SV.text(x + w / 2, 84, t, "lbl bd", { "text-anchor": "middle", style: `font-size:${t.length > 9 ? 13 : t.length > 6 ? 16 : 20}px;font-family:var(--mono)` });
    });
  }
  if (f.cells) {
    const a = f.cells, m = a.length, g = 5, w = Math.min(44, Math.floor((W - 28 - (m - 1) * g) / m)), tot = m * w + (m - 1) * g, x0 = (W - tot) / 2;
    s += Lib.cells(a, { x0, y: 112, w, h: 38, gap: g, cls: f.cc || {}, idx: false });
    a.forEach((_, i) => (s += SV.text(x0 + i * (w + g) + w / 2, 166, i + 1, "sm", { "text-anchor": "middle" })));
  } else if (f.inp) {
    const t = f.inp.length ? "Waiting to be typed in:   " + f.inp.map(fv).join("    ") : "Nothing left to input";
    s += SV.rect(14, 114, W - 28, 36, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
    s += SV.text(W / 2, 138, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
  }
  if (f.cond) s += SV.text(W / 2, 196, `${f.cond[0]}   is   ${f.cond[1] ? "TRUE" : "FALSE"}`, "lbl bd " + (f.cond[1] ? "t3" : "t2"), { "text-anchor": "middle", style: "font-family:var(--mono)" });
  else if (f.note) s += SV.text(W / 2, 196, f.note, "lbl bd " + (f.nc || ""), { "text-anchor": "middle" });
  let ot = (f.out || []).join("   "); if (ot.length > 62) ot = "…" + ot.slice(-61);
  s += SV.rect(14, 212, W - 28, 44, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
  s += SV.text(26, 229, "Output", "sm", { "text-anchor": "start" });
  s += SV.text(26, 249, ot, "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:15px" });
  return s;
}
function tr(el, o) {
  Lib.algo(el, { w: 640, h: 270, label: o.label, pseudo: o.pseudo, py: o.py, dwell: o.dwell || 2000, frames: o.frames.map((f) => ({ cap: f.cap, ps: f.ps, py: f.py, svg: trSvg(f, o) })) });
}
const nums = (v, k = 20) => v.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x)).slice(0, k);

const PC_PS = ["PROCEDURE Greet(Name : STRING, Times : INTEGER)", "    DECLARE Count : INTEGER", "    FOR Count ← 1 TO Times", "        OUTPUT \"Hi \", Name", "    NEXT Count", "ENDPROCEDURE", "", "CALL Greet(\"Mai\", 2)", "CALL Greet(\"Sam\", 1)"], PC_PY = ["def greet(name, times):", "    for count in range(1, times + 1):", "        print(\"Hi\", name)", "", "greet(\"Mai\", 2)", "greet(\"Sam\", 1)"], FN_PS = ["FUNCTION Area(Length : INTEGER, Width : INTEGER) RETURNS INTEGER", "    RETURN Length * Width", "ENDFUNCTION", "", "Room ← Area(5, 3)", "OUTPUT Room", "OUTPUT Area(2, 4) + 10"], FN_PY = ["def area(length, width):", "    return length * width", "", "room = area(5, 3)", "print(room)", "print(area(2, 4) + 10)"], SC_PS = ["DECLARE Total : INTEGER", "", "PROCEDURE AddBonus", "    DECLARE Bonus : INTEGER", "    Bonus ← 5", "    Total ← Total + Bonus", "ENDPROCEDURE", "", "Total ← 20", "CALL AddBonus", "OUTPUT Total"], SC_PY = ["def add_bonus():", "    global total", "    bonus = 5", "    total = total + bonus", "", "total = 20", "add_bonus()", "print(total)"], SH_PS = ["DECLARE Score : INTEGER", "", "PROCEDURE Test", "    DECLARE Score : INTEGER", "    Score ← 99", "    OUTPUT Score", "ENDPROCEDURE", "", "Score ← 10", "CALL Test", "OUTPUT Score"], SH_PY = ["def test():", "    score = 99", "    print(score)", "", "score = 10", "test()", "print(score)"];
tr($("#aP"), { label: "Procedure call", pseudo: PC_PS, py: PC_PY, frames: [{"cap": "The procedure is <b>defined</b> first. Nothing runs yet: a definition only says what the name <b>Greet</b> means.", "ps": [0, 5], "py": [0], "vars": [], "hl": [], "out": [], "title": "Main program"}, {"cap": "<b>CALL Greet(\"Mai\", 2)</b>. The two <b>arguments</b> are passed in.", "ps": [7], "py": [4], "vars": [], "hl": [], "out": [], "title": "Main program"}, {"cap": "Control jumps into the procedure. The <b>parameters</b> take the values: Name is \"Mai\", Times is 2.", "ps": [0], "py": [0], "vars": [["Name", "Mai"], ["Times", 2], ["Count", null]], "hl": ["Name", "Times"], "out": [], "title": "Inside Greet"}, {"cap": "Loop 1 of 2: <b>OUTPUT \"Hi Mai\"</b>.", "ps": [2, 3], "py": [1, 2], "vars": [["Name", "Mai"], ["Times", 2], ["Count", 1]], "hl": ["Count"], "out": ["Hi Mai"], "title": "Inside Greet"}, {"cap": "Loop 2 of 2: <b>OUTPUT \"Hi Mai\"</b>.", "ps": [2, 3], "py": [1, 2], "vars": [["Name", "Mai"], ["Times", 2], ["Count", 2]], "hl": ["Count"], "out": ["Hi Mai", "Hi Mai"], "title": "Inside Greet"}, {"cap": "<b>ENDPROCEDURE</b>: control goes back to the next line. Name, Times and Count no longer exist.", "ps": [5], "py": [4], "vars": [], "hl": [], "out": ["Hi Mai", "Hi Mai"], "title": "Main program"}, {"cap": "<b>CALL Greet(\"Sam\", 1)</b>. The two <b>arguments</b> are passed in.", "ps": [8], "py": [5], "vars": [], "hl": [], "out": ["Hi Mai", "Hi Mai"], "title": "Main program"}, {"cap": "Control jumps into the procedure. The <b>parameters</b> take the values: Name is \"Sam\", Times is 1.", "ps": [0], "py": [0], "vars": [["Name", "Sam"], ["Times", 1], ["Count", null]], "hl": ["Name", "Times"], "out": ["Hi Mai", "Hi Mai"], "title": "Inside Greet"}, {"cap": "Loop 1 of 1: <b>OUTPUT \"Hi Sam\"</b>.", "ps": [2, 3], "py": [1, 2], "vars": [["Name", "Sam"], ["Times", 1], ["Count", 1]], "hl": ["Count"], "out": ["Hi Mai", "Hi Mai", "Hi Sam"], "title": "Inside Greet"}, {"cap": "<b>ENDPROCEDURE</b>: control goes back to the end of the program. Name, Times and Count no longer exist.", "ps": [5], "py": [5], "vars": [], "hl": [], "out": ["Hi Mai", "Hi Mai", "Hi Sam"], "title": "Main program"}] });
tr($("#aF"), { label: "Function call", pseudo: FN_PS, py: FN_PY, frames: [{"cap": "<b>Area</b> is a function: it will <b>return</b> an integer.", "ps": [0, 2], "py": [0], "vars": [["Room", null]], "hl": [], "out": [], "title": "Main program"}, {"cap": "<b>Room ← Area(5, 3)</b>. The call is part of an assignment, so the result has somewhere to go.", "ps": [4], "py": [3], "vars": [["Room", null]], "hl": [], "out": [], "title": "Main program"}, {"cap": "Inside Area: Length is 5, Width is 3.", "ps": [0], "py": [0], "vars": [["Length", 5], ["Width", 3]], "hl": ["Length", "Width"], "out": [], "title": "Inside Area"}, {"cap": "<b>RETURN Length * Width</b> sends 15 back to where the function was called.", "ps": [1], "py": [1], "vars": [["Length", 5], ["Width", 3]], "hl": [], "out": [], "title": "Inside Area", "note": "returns 15", "nc": "t3"}, {"cap": "The returned value <b>replaces the call</b>, so Room ← 15.", "ps": [4], "py": [3], "vars": [["Room", 15]], "hl": ["Room"], "out": [], "title": "Main program"}, {"cap": "<b>OUTPUT Room</b>.", "ps": [5], "py": [4], "vars": [["Room", 15]], "hl": [], "out": ["15"], "title": "Main program"}, {"cap": "<b>OUTPUT Area(2, 4) + 10</b> calls the function again, with new values.", "ps": [6, 1], "py": [5, 1], "vars": [["Length", 2], ["Width", 4]], "hl": ["Length", "Width"], "out": ["15"], "title": "Inside Area", "note": "returns 8", "nc": "t3"}, {"cap": "The call becomes 8, so the expression is 8 + 10 = <b>18</b>. Room is unchanged.", "ps": [6], "py": [5], "vars": [["Room", 15]], "hl": [], "out": ["15", "18"], "title": "Main program", "note": "8 + 10 = 18", "nc": "t4"}] });
tr($("#aS"), { label: "Local and global", pseudo: SC_PS, py: SC_PY, frames: [{"cap": "<b>Total</b> is declared outside any routine, so it is <b>global</b>.", "ps": [0], "py": [], "vars": [["Total", null]], "hl": [], "out": [], "title": "Main program"}, {"cap": "<b>Total ← 20</b>.", "ps": [8], "py": [5], "vars": [["Total", 20]], "hl": ["Total"], "out": [], "title": "Main program"}, {"cap": "<b>CALL AddBonus</b>.", "ps": [9], "py": [6], "vars": [["Total", 20]], "hl": [], "out": [], "title": "Main program"}, {"cap": "A <b>local</b> variable, Bonus, is created inside the procedure. Python needs <code>global total</code> to change a global.", "ps": [3], "py": [1], "vars": [["Total", 20], ["Bonus", null]], "hl": ["Bonus"], "out": [], "title": "Inside AddBonus"}, {"cap": "<b>Bonus ← 5</b>.", "ps": [4], "py": [2], "vars": [["Total", 20], ["Bonus", 5]], "hl": ["Bonus"], "out": [], "title": "Inside AddBonus"}, {"cap": "<b>Total ← Total + Bonus</b>. The procedure can use the global Total: 20 + 5 = 25.", "ps": [5], "py": [3], "vars": [["Total", 25], ["Bonus", 5]], "hl": ["Total"], "out": [], "title": "Inside AddBonus"}, {"cap": "The procedure ends. <b>Bonus is destroyed</b>. Total keeps its new value.", "ps": [6], "py": [6], "vars": [["Total", 25]], "hl": [], "out": [], "title": "Main program"}, {"cap": "<b>OUTPUT Total</b>: 25. Trying to OUTPUT Bonus here would be an error.", "ps": [10], "py": [7], "vars": [["Total", 25]], "hl": [], "out": ["25"], "title": "Main program"}] });
tr($("#aH"), { label: "Same name, two variables", pseudo: SH_PS, py: SH_PY, frames: [{"cap": "The global <b>Score</b> is set to 10.", "ps": [8], "py": [4], "vars": [["global Score", 10]], "hl": ["global Score"], "out": [], "title": "Main program"}, {"cap": "<b>CALL Test</b>.", "ps": [9], "py": [5], "vars": [["global Score", 10]], "hl": [], "out": [], "title": "Main program"}, {"cap": "Test declares its <b>own</b> Score. Same name, but a <b>separate</b> variable.", "ps": [3], "py": [1], "vars": [["global Score", 10], ["local Score", null]], "hl": ["local Score"], "out": [], "title": "Inside Test"}, {"cap": "<b>Score ← 99</b> changes only the local one.", "ps": [4], "py": [1], "vars": [["global Score", 10], ["local Score", 99]], "hl": ["local Score"], "out": [], "title": "Inside Test"}, {"cap": "<b>OUTPUT Score</b> inside Test uses the local one: 99.", "ps": [5], "py": [2], "vars": [["global Score", 10], ["local Score", 99]], "hl": ["local Score"], "out": ["99"], "title": "Inside Test"}, {"cap": "Test ends and its local Score disappears.", "ps": [6], "py": [5], "vars": [["global Score", 10]], "hl": [], "out": ["99"], "title": "Main program"}, {"cap": "<b>OUTPUT Score</b> in the main program: still <b>10</b>.", "ps": [10], "py": [6], "vars": [["global Score", 10]], "hl": ["global Score"], "out": ["99", "10"], "title": "Main program"}] });
Lib.codePanel($("#cdP0"), { pseudo: ["PROCEDURE ShowLine", '    OUTPUT "----------"', "ENDPROCEDURE", "", "CALL ShowLine", 'OUTPUT "Menu"', "CALL ShowLine"], py: ["def show_line():", '    print("----------")', "", "show_line()", 'print("Menu")', "show_line()"] });
Lib.codePanel($("#cdPc"), { pseudo: PC_PS, py: PC_PY });
Lib.codePanel($("#cdFn"), { pseudo: FN_PS, py: FN_PY });
Lib.codePanel($("#cdSc"), { pseudo: SC_PS, py: SC_PY });


/* ---------- Lab 1 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const l = a.get(), w = b.get();
    Lib.codePanel($("#fcode"), { pseudo: ["FUNCTION Area(Length : INTEGER, Width : INTEGER) RETURNS INTEGER", "    RETURN Length * Width", "ENDFUNCTION", "", `OUTPUT Area(${l}, ${w})`], py: ["def area(length, width):", "    return length * width", "", `print(area(${l}, ${w}))`] });
    $("#fp").textContent = `Length = ${l}, Width = ${w}`; $("#fr").textContent = l * w;
    $("#fv").innerHTML = `The call <b>Area(${l}, ${w})</b> is replaced by <b>${l * w}</b>, which is then output.`; };
  a = Lib.slider($("#s1"), { id: "al", label: "First argument ", min: 1, max: 20, value: 6, onInput: upd });
  b = Lib.slider($("#s2"), { id: "aw", label: "Second argument ", min: 1, max: 20, value: 4, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const w = a.get(), h = b.get(), c = $("#sym").value;
    Lib.codePanel($("#dcode"), { pseudo: ["PROCEDURE Block(Width : INTEGER, Height : INTEGER, Symbol : CHAR)", "    DECLARE Row : INTEGER", "    DECLARE Column : INTEGER", "    DECLARE Line : STRING", "    FOR Row ← 1 TO Height", '        Line ← ""', "        FOR Column ← 1 TO Width", "            Line ← Line & Symbol", "        NEXT Column", "        OUTPUT Line", "    NEXT Row", "ENDPROCEDURE", "", `CALL Block(${w}, ${h}, '${c}')`], py: ["def block(width, height, symbol):", "    for row in range(height):", '        line = ""', "        for column in range(width):", "            line = line + symbol", "        print(line)", "", `block(${w}, ${h}, "${c}")`] });
    $("#dout").textContent = Array(h).fill(c.repeat(w)).join("\n"); };
  a = Lib.slider($("#s3"), { id: "bw", label: "Width ", min: 1, max: 20, value: 8, onInput: upd });
  b = Lib.slider($("#s4"), { id: "bh", label: "Height ", min: 1, max: 6, value: 3, onInput: upd });
  $("#sym").onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const P = ["DECLARE Total : INTEGER", "", "PROCEDURE AddTax(Price : INTEGER)", "    DECLARE Tax : INTEGER", "    Tax ← Price DIV 10", "    Total ← Total + Price + Tax", "ENDPROCEDURE", "", "FUNCTION Half(Value : INTEGER) RETURNS REAL", "    DECLARE Answer : REAL", "    Answer ← Value / 2", "    RETURN Answer", "ENDFUNCTION", "", "Total ← 0", "CALL AddTax(50)", "OUTPUT Half(Total)"];
  const Q = ["def add_tax(price):", "    global total", "    tax = price // 10", "    total = total + price + tax", "", "def half(value):", "    answer = value / 2", "    return answer", "", "total = 0", "add_tax(50)", "print(half(total))"];
  let cp;
  const S = [{ n: "inside AddTax", ps: 5, py: 3, v: "<b>Total</b> (global), <b>Price</b> (parameter), <b>Tax</b> (local)", no: "Value and Answer" },
    { n: "inside Half", ps: 10, py: 6, v: "<b>Total</b> (global), <b>Value</b> (parameter), <b>Answer</b> (local)", no: "Price and Tax" },
    { n: "in the main program", ps: 16, py: 11, v: "<b>Total</b> (global) only", no: "Price, Tax, Value and Answer" }];
  cp = Lib.codePanel($("#vcode"), { pseudo: P, py: Q });
  Lib.slider($("#s5"), { id: "vp", label: "Place: ", min: 1, max: 3, value: 1, fmt: (v) => S[v - 1].n, onInput: (v) => { const s = S[v - 1]; cp.hl(s.ps, s.py); $("#vv").innerHTML = `In scope ${s.n}: ${s.v}.<br>Not in scope: ${s.no}.`; } });
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which would you write for each job?", buckets: [{ label: "Procedure" }, { label: "Function" }], items: [
  { text: "Display the main menu", b: 0 }, { text: "Print a line of 30 dashes", b: 0 }, { text: "Output a welcome message with the user's name", b: 0 },
  { text: "Work out VAT and send it back", b: 1 }, { text: "Give back TRUE if a number is even", b: 1 }, { text: "Calculate the average of three marks for use later", b: 1 }],
  done: "If the main program needs a value back, use a function." });
Lib.match($("#m1"), { prompt: "Drag each meaning to its term.", pairs: [["Parameter", "Variable in the heading that receives a value"], ["Argument", "The value passed in by the call"], ["RETURN", "Sends a value back from a function"], ["Local variable", "Can only be used inside its routine"], ["Global variable", "Can be used anywhere in the program"]] });
Lib.order($("#o1"), { prompt: "Build a function that returns the square of a number, then use it.", items: ["FUNCTION Square(N : INTEGER) RETURNS INTEGER", "DECLARE Answer : INTEGER", "Answer ← N * N", "RETURN Answer", "ENDFUNCTION", "OUTPUT Square(5)"], done: "Heading, declare, calculate, return, end, then call." });
Lib.calc($("#c1"), { qs: [
  { q: "Add(A, B) returns A + B. What is Add(7, 8)?", a: 15, sol: "7 + 8 = 15." },
  { q: "Take(A, B) returns A − B. What is Take(3, 10)?", a: -7, sol: "Order matters: A is 3 and B is 10, so 3 − 10 = −7." },
  { q: "Triple(N) returns N * 3. What is Triple(4) + Triple(2)?", a: 18, sol: "12 + 6 = 18." },
  { q: "Triple(N) returns N * 3. What is Triple(Triple(2))?", a: 18, sol: "Triple(2) = 6, then Triple(6) = 18." },
  { q: "Global X ← 5. A procedure adds 3 to the global X and is called twice. What is X?", a: 11, sol: "5 + 3 + 3 = 11." },
  { q: "Global X ← 5. A procedure declares a local X, sets it to 50 and ends. What is the global X?", a: 5, sol: "The local X is a separate variable." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which keyword calls a procedure?", opts: ["CALL", "RETURN", "FUNCTION", "RUN"], a: 0, why: "Procedures are called with CALL." },
  { q: "Which is a correct use of the function Cube?", opts: ["Result ← Cube(3)", "CALL Cube(3)", "Cube(3) ← Result", "RETURNS Cube(3)"], a: 0, why: "A function call is part of an expression." },
  { q: "What is the most parameters a routine will have at IGCSE?", opts: ["Three", "One", "Five", "Ten"], a: 0, why: "Up to three parameters." },
  { q: "A variable declared inside a function is...", opts: ["local", "global", "a constant", "a parameter of the main program"], a: 0, why: "It only exists inside that function." },
  { q: "What happens to a local variable when its routine ends?", opts: ["It no longer exists", "It becomes global", "It keeps its value for the main program", "It is output automatically"], a: 0, why: "It exists only while the routine runs." }] });
Lib.cards($("#fc1"), { cards: [
  ["Procedure", "A named block of code that does a task and is called with CALL."],
  ["Function", "A named block of code that returns a value."],
  ["Parameter", "A variable in a routine's heading that receives a value."],
  ["Argument", "The actual value passed to a routine when it is called."],
  ["Call", "To run a procedure or function by using its name."],
  ["RETURN", "The statement that sends a value back from a function."],
  ["Local variable", "Declared inside a routine and only usable there."],
  ["Global variable", "Declared outside all routines and usable anywhere."],
  ["Scope", "The part of a program where a variable can be used."]] });

