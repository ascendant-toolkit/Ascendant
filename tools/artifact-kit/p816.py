"""8.1.6 Procedures, functions, parameters, local and global variables."""
from p814k import *

PC_PS = ["PROCEDURE Greet(Name : STRING, Times : INTEGER)", "    DECLARE Count : INTEGER", "    FOR Count ← 1 TO Times", '        OUTPUT "Hi ", Name', "    NEXT Count", "ENDPROCEDURE", "", 'CALL Greet("Mai", 2)', 'CALL Greet("Sam", 1)']
PC_PY = ["def greet(name, times):", "    for count in range(1, times + 1):", '        print("Hi", name)', "", 'greet("Mai", 2)', 'greet("Sam", 1)']
FN_PS = ["FUNCTION Area(Length : INTEGER, Width : INTEGER) RETURNS INTEGER", "    RETURN Length * Width", "ENDFUNCTION", "", "Room ← Area(5, 3)", "OUTPUT Room", "OUTPUT Area(2, 4) + 10"]
FN_PY = ["def area(length, width):", "    return length * width", "", "room = area(5, 3)", "print(room)", "print(area(2, 4) + 10)"]
SC_PS = ["DECLARE Total : INTEGER", "", "PROCEDURE AddBonus", "    DECLARE Bonus : INTEGER", "    Bonus ← 5", "    Total ← Total + Bonus", "ENDPROCEDURE", "", "Total ← 20", "CALL AddBonus", "OUTPUT Total"]
SC_PY = ["def add_bonus():", "    global total", "    bonus = 5", "    total = total + bonus", "", "total = 20", "add_bonus()", "print(total)"]
SH_PS = ["DECLARE Score : INTEGER", "", "PROCEDURE Test", "    DECLARE Score : INTEGER", "    Score ← 99", "    OUTPUT Score", "ENDPROCEDURE", "", "Score ← 10", "CALL Test", "OUTPUT Score"]
SH_PY = ["def test():", "    score = 99", "    print(score)", "", "score = 10", "test()", "print(score)"]


def anim_proc():
    r = R([])
    r.f("The procedure is <b>defined</b> first. Nothing runs yet: a definition only says what the name <b>Greet</b> means.", [0, 5], [0], title="Main program")
    for line_ps, line_py, name, times, nxt in [(7, 4, "Mai", 2, "the next line"), (8, 5, "Sam", 1, "the end of the program")]:
        r.v = {}
        r.f(f'<b>CALL Greet("{name}", {times})</b>. The two <b>arguments</b> are passed in.', [line_ps], [line_py], title="Main program")
        r.v = {"Name": name, "Times": times, "Count": None}
        r.f(f'Control jumps into the procedure. The <b>parameters</b> take the values: Name is "{name}", Times is {times}.', [0], [0], hl=["Name", "Times"], title="Inside Greet")
        for c in range(1, times + 1):
            r.v["Count"] = c; r.out.append("Hi " + name)
            r.f(f"Loop {c} of {times}: <b>OUTPUT \"Hi {name}\"</b>.", [2, 3], [1, 2], hl=["Count"], title="Inside Greet")
        r.v = {}
        r.f(f"<b>ENDPROCEDURE</b>: control goes back to {nxt}. Name, Times and Count no longer exist.", [5], [line_py], title="Main program")
    return r.js()


def anim_fn():
    r = R(["Room"])
    r.f("<b>Area</b> is a function: it will <b>return</b> an integer.", [0, 2], [0], title="Main program")
    r.f("<b>Room ← Area(5, 3)</b>. The call is part of an assignment, so the result has somewhere to go.", [4], [3], title="Main program")
    r.v = {"Length": 5, "Width": 3}; r.f("Inside Area: Length is 5, Width is 3.", [0], [0], hl=["Length", "Width"], title="Inside Area")
    r.f("<b>RETURN Length * Width</b> sends 15 back to where the function was called.", [1], [1], title="Inside Area", note="returns 15", nc="t3")
    r.v = {"Room": 15}; r.f("The returned value <b>replaces the call</b>, so Room ← 15.", [4], [3], hl=["Room"], title="Main program")
    r.out.append("15"); r.f("<b>OUTPUT Room</b>.", [5], [4], title="Main program")
    r.v = {"Length": 2, "Width": 4}; r.f("<b>OUTPUT Area(2, 4) + 10</b> calls the function again, with new values.", [6, 1], [5, 1], hl=["Length", "Width"], title="Inside Area", note="returns 8", nc="t3")
    r.v = {"Room": 15}; r.out.append("18"); r.f("The call becomes 8, so the expression is 8 + 10 = <b>18</b>. Room is unchanged.", [6], [5], title="Main program", note="8 + 10 = 18", nc="t4")
    return r.js()


def anim_scope():
    r = R(["Total"])
    r.f("<b>Total</b> is declared outside any routine, so it is <b>global</b>.", [0], [], title="Main program")
    r.v["Total"] = 20; r.f("<b>Total ← 20</b>.", [8], [5], hl=["Total"], title="Main program")
    r.f("<b>CALL AddBonus</b>.", [9], [6], title="Main program")
    r.v["Bonus"] = None; r.f("A <b>local</b> variable, Bonus, is created inside the procedure. Python needs <code>global total</code> to change a global.", [3], [1], hl=["Bonus"], title="Inside AddBonus")
    r.v["Bonus"] = 5; r.f("<b>Bonus ← 5</b>.", [4], [2], hl=["Bonus"], title="Inside AddBonus")
    r.v["Total"] = 25; r.f("<b>Total ← Total + Bonus</b>. The procedure can use the global Total: 20 + 5 = 25.", [5], [3], hl=["Total"], title="Inside AddBonus")
    del r.v["Bonus"]; r.f("The procedure ends. <b>Bonus is destroyed</b>. Total keeps its new value.", [6], [6], title="Main program")
    r.out.append("25"); r.f("<b>OUTPUT Total</b>: 25. Trying to OUTPUT Bonus here would be an error.", [10], [7], title="Main program")
    return r.js()


def anim_shadow():
    r = R(["global Score"])
    r.v["global Score"] = 10; r.f("The global <b>Score</b> is set to 10.", [8], [4], hl=["global Score"], title="Main program")
    r.f("<b>CALL Test</b>.", [9], [5], title="Main program")
    r.v["local Score"] = None; r.f("Test declares its <b>own</b> Score. Same name, but a <b>separate</b> variable.", [3], [1], hl=["local Score"], title="Inside Test")
    r.v["local Score"] = 99; r.f("<b>Score ← 99</b> changes only the local one.", [4], [1], hl=["local Score"], title="Inside Test")
    r.out.append("99"); r.f("<b>OUTPUT Score</b> inside Test uses the local one: 99.", [5], [2], hl=["local Score"], title="Inside Test")
    del r.v["local Score"]; r.f("Test ends and its local Score disappears.", [6], [5], title="Main program")
    r.out.append("10"); r.f("<b>OUTPUT Score</b> in the main program: still <b>10</b>.", [10], [6], hl=["global Score"], title="Main program")
    return r.js()


learn = '''
  <h2>8.1.6 Procedures and functions</h2>
  <p>A <span class="kw">procedure</span> or <span class="kw">function</span> is a <b>named block of code</b> that does one job. You write it once, then <b>call</b> it by name whenever you need it. Together they are often called <span class="kw">subroutines</span>. They are defined at the start of the program.</p>

  <h3>Procedures</h3>
  <p>A <span class="kw">procedure</span> carries out a task. It is called with <span class="ln2">CALL</span>, and the call is a complete statement on its own.</p>
  <div id="cdP0" class="code"></div>

  <h3>Parameters</h3>
  <p>A <span class="kw">parameter</span> is a variable in the routine's heading that receives a value when the routine is called. The actual value you pass in is called an <span class="kw">argument</span>. Parameters let one routine work with different data. At IGCSE a routine can have <b>up to three</b>.</p>
  <div id="cdPc" class="code"></div>
  <div class="tip"><b class="h">Order matters</b>Arguments are matched to parameters <b>by position</b>. <code>CALL Greet("Mai", 2)</code> gives Name "Mai" and Times 2. Swapping them is an error.</div>

  <h3>Functions</h3>
  <p>A <span class="kw">function</span> works like a procedure but <b>returns one value</b> to the place it was called. The heading states the data type with <span class="ln2">RETURNS</span>, and <span class="ln2">RETURN</span> sends the value back. A function is called <b>inside an expression</b> (assigned, output or compared) and <b>never</b> with CALL.</p>
  <div id="cdFn" class="code"></div>

  <div class="tw"><table class="t">
    <tr><th></th><th>Procedure</th><th>Function</th></tr>
    <tr><td>Heading</td><td>PROCEDURE Name(...)</td><td>FUNCTION Name(...) RETURNS type</td></tr>
    <tr><td>Ends with</td><td>ENDPROCEDURE</td><td>ENDFUNCTION</td></tr>
    <tr><td>Returns a value</td><td>No</td><td>Yes, with RETURN</td></tr>
    <tr><td>Called</td><td>CALL Name(...)</td><td>inside an expression, no CALL</td></tr>
    <tr><td>Python</td><td>def, no return value</td><td>def with return</td></tr>
  </table></div>

  <h3>Local and global variables</h3>
  <p>The <span class="kw">scope</span> of a variable is the part of the program where it can be used. A <span class="kw">global variable</span> is declared outside all routines and can be used <b>anywhere</b>. A <span class="kw">local variable</span> is declared inside a routine, can only be used <b>there</b>, and exists only while that routine is running. Parameters behave like local variables.</p>
  <div id="cdSc" class="code"></div>
  <div class="tip"><b class="h">Prefer local</b>Local variables cannot be changed by accident from elsewhere, the same name can safely be reused in different routines, and their memory is freed when the routine ends.</div>
  <div class="warn"><b class="h">Python and globals</b>A variable assigned inside a Python <code>def</code> is local. To change a global one you must write <code>global total</code> first.</div>

  <h3>Why use subroutines?</h3>
  <p>Code is written once and <b>reused</b>. The program is shorter and split into manageable parts. Each part can be written and <b>tested on its own</b>, often by different people, and a fix is made in one place only.</p>
'''

watch = '''  <h2>1 · Calling a procedure with parameters</h2><div id="aP"></div>
  <h2>2 · A function returns a value</h2><div id="aF"></div>
  <h2>3 · Local and global variables</h2><div id="aS"></div>
  <h2>4 · Two variables with the same name</h2><div id="aH"></div>
'''

explore = '''  <h2>Lab 1 · The function machine</h2>
  <p>Choose the arguments and see them go into the parameters, and the value come back.</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div id="fcode"></div><div class="readout"><div><small>Parameters</small><strong id="fp" style="font-size:1rem"></strong></div><div><small>Returned value</small><strong id="fr"></strong></div></div><div class="verdict" id="fv" aria-live="polite"></div></div>

  <h2>Lab 2 · One procedure, many results</h2>
  <p>The same procedure draws different shapes because its three parameters change.</p>
  <div class="card"><div id="s3"></div><div id="s4"></div><label>Symbol <select id="sym"><option>*</option><option>#</option><option>=</option><option>+</option></select></label><div id="dcode"></div><div class="out" id="dout" style="min-height:60px;white-space:pre;font-family:var(--mono)"></div></div>

  <h2>Lab 3 · What can be seen here?</h2>
  <p>Move to a place in the program and see which variables are in scope.</p>
  <div class="card"><div id="s5"></div><div id="vcode"></div><div class="verdict" id="vv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Procedure or function?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Match the term</h2>
  <div id="m1" class="card"></div>
  <h2>3 · Build a function</h2>
  <div id="o1" class="card"></div>
  <h2>4 · What is returned or output?</h2>
  <div id="c1"></div>
  <h2>5 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A cash machine menu", "Showing the balance, printing a receipt and ejecting the card are each separate routines called from the main program.", "procedures: each carries out a task and can be reused from several menu options.")
        + rw("A currency converter", "Give it an amount and an exchange rate and it hands back the converted amount.", "a function with two parameters that returns a real value.")
        + rw("A game with many levels", "One routine draws an enemy at any position. It is called hundreds of times with different coordinates.", "parameters let one routine work with different data, so code is not repeated.")
        + rw("A large team project", "Programmers each write routines using their own local variables, then combine them.", "local variables avoid clashes between names; routines can be tested separately."))

ex = [
    eq(1, "State", 2, "State two differences between a <b>procedure</b> and a <b>function</b>.", "Think about returning and calling.",
       mk(1, "A function returns a value, a procedure does not") + " " + mk(2, "A function is called as part of an expression, a procedure is called with CALL"),
       "Saying only functions can have parameters. Both can."),
    eq(2, "State", 2, "Explain what is meant by a <b>parameter</b>.", "Where does its value come from?",
       mk(1, "A variable in the heading of a procedure / function") + " " + mk(2, "that receives a value passed in when the routine is called"),
       "Saying it is the value the function returns."),
    eq(3, "Write", 4, "Write a procedure Stars that takes an integer parameter Number and outputs \"*\" that many times. Then call it to output 8 stars.", "Heading, loop, end, call.",
       mk(1, "PROCEDURE Stars(Number : INTEGER) ... ENDPROCEDURE") + " " + mk(2, "loop from 1 TO Number") + " " + mk(3, 'OUTPUT "*" inside the loop') + " " + mk(4, "CALL Stars(8)")
       + ac(["PROCEDURE Stars(Number : INTEGER)", "    DECLARE Count : INTEGER", "    FOR Count ← 1 TO Number", '        OUTPUT "*"', "    NEXT Count", "ENDPROCEDURE", "", "CALL Stars(8)"]),
       "Asking the user to INPUT Number inside the procedure. Its value arrives through the parameter."),
    eq(4, "Write", 4, "Write a function Larger that takes two integers and returns the larger one.", "A function needs RETURNS and RETURN.",
       mk(1, "FUNCTION heading with two integer parameters") + " " + mk(2, "RETURNS INTEGER") + " " + mk(3, "IF comparing the two parameters") + " " + mk(4, "RETURN the correct value in each branch, then ENDFUNCTION")
       + ac(["FUNCTION Larger(A : INTEGER, B : INTEGER) RETURNS INTEGER", "    IF A > B", "      THEN", "        RETURN A", "      ELSE", "        RETURN B", "    ENDIF", "ENDFUNCTION"]),
       "Using OUTPUT instead of RETURN, so nothing is sent back."),
    eq(5, "State", 3, "State the output of this program.", "Work out each call, then the expression.",
       mk(1, "Double(4) returns 8") + " " + mk(2, "Double(8) returns 16") + " " + mk(3, "Output: 16"),
       "Stopping after the first call. The inner call is worked out first, then its result is passed in again.",
       pre=qc(["FUNCTION Double(N : INTEGER) RETURNS INTEGER", "    RETURN N * 2", "ENDFUNCTION", "", "OUTPUT Double(Double(4))"])),
    eq(6, "Explain", 4, "Explain the difference between a <b>local</b> and a <b>global</b> variable.", "Where is it declared, and where can it be used?",
       mk(1, "A global variable is declared outside any procedure / function (in the main program)") + " " + mk(2, "and can be used anywhere in the program") + " " + mk(3, "A local variable is declared inside a procedure / function") + " " + mk(4, "and can only be used within that routine"),
       "Writing that local variables are \"smaller\" or \"temporary files\". Describe <b>scope</b>."),
    eq(7, "State", 2, "State the two values output by this program, in order.", "Which Number does each OUTPUT use?",
       mk(1, "7 (the local Number)") + " " + mk(2, "3 (the global Number is unchanged)"),
       "Outputting 7 twice. The local variable does not change the global one.",
       pre=qc(["DECLARE Number : INTEGER", "", "PROCEDURE Show", "    DECLARE Number : INTEGER", "    Number ← 7", "    OUTPUT Number", "ENDPROCEDURE", "", "Number ← 3", "CALL Show", "OUTPUT Number"])),
    eq(8, "Identify", 3, "Identify three errors in this pseudocode.", "Check the heading, the value sent back and the call.",
       mk(1, "RETURNS and the data type are missing from the heading") + " " + mk(2, "OUTPUT used where RETURN is needed") + " " + mk(3, "CALL must not be used to call a function (use it in an expression, e.g. OUTPUT Half(10))"),
       "Reporting spelling or indentation instead of errors in the logic of a function.",
       pre=qc(["FUNCTION Half(N : INTEGER)", "    OUTPUT N / 2", "ENDFUNCTION", "", "CALL Half(10)"])),
    eq(9, "Write", 7, "Write a function Grade that takes a mark and returns \"Pass\" if it is 50 or more, otherwise \"Fail\". Then write code that inputs 20 marks, uses the function for each, outputs the result and finally outputs how many passed.", "Define the function first, then the main program.",
       mk(1, "FUNCTION Grade(Mark : INTEGER) RETURNS STRING") + " " + mk(2, 'IF Mark >= 50 RETURN "Pass" ELSE RETURN "Fail"') + " " + mk(3, "Passes ← 0 before the loop") + " " + mk(4, "loop 20 times with INPUT inside") + " " + mk(5, "function called in an expression and result output") + " " + mk(6, 'add 1 to Passes when the result is "Pass"') + " " + mk(7, "OUTPUT Passes after the loop")
       + ac(["FUNCTION Grade(Mark : INTEGER) RETURNS STRING", "    IF Mark >= 50", "      THEN", '        RETURN "Pass"', "      ELSE", '        RETURN "Fail"', "    ENDIF", "ENDFUNCTION", "", "Passes ← 0", "FOR Count ← 1 TO 20", "    INPUT Mark", "    Result ← Grade(Mark)", "    OUTPUT Result", '    IF Result = "Pass"', "      THEN", "        Passes ← Passes + 1", "    ENDIF", "NEXT Count", "OUTPUT Passes"]),
       "Writing CALL Grade(Mark)."),
    eq(10, "Explain", 3, "Explain three benefits of using procedures and functions in a program.", "Reuse, testing, readability.",
       mk(1, "Code can be reused without writing it again, so the program is shorter") + " " + mk(2, "Each routine can be written and tested separately (or by different programmers)") + " " + mk(3, "The program is easier to read and maintain, because a change is made in one place"),
       "Claiming they always make the program run faster."),
]

tipshtml = tips([
    "<b>Function = returns a value.</b> Procedure = does a job.",
    "<b>CALL for procedures only.</b> Use a function inside an expression.",
    "<b>Every function needs RETURNS (heading) and RETURN (body).</b>",
    "<b>Give each parameter a data type</b> in the heading, and pass arguments in the same order.",
    "<b>Do not INPUT a parameter.</b> Its value is already there.",
    "<b>RETURN sends a value back. OUTPUT shows it on screen.</b> They are not the same.",
    "<b>Local: inside one routine. Global: everywhere.</b>",
])

page("8.1.6 · Procedures and functions", "Procedures and Functions", "Named blocks of code, parameters, returned values, and local and global variables.",
     "A <span class=\"kw\">procedure</span> or <span class=\"kw\">function</span> lets you <b>write code once and use it many times</b>. <b>Parameters</b> carry values in; a function <b>returns</b> a value out.",
     learn, watch, explore, practise, real, "".join(ex), tipshtml, "p816")

js = []
consts = ", ".join(f"{n} = {json.dumps(v, ensure_ascii=False)}" for n, v in [("PC_PS", PC_PS), ("PC_PY", PC_PY), ("FN_PS", FN_PS), ("FN_PY", FN_PY), ("SC_PS", SC_PS), ("SC_PY", SC_PY), ("SH_PS", SH_PS), ("SH_PY", SH_PY)])
js.append(f'''
const {consts};
tr($("#aP"), {{ label: "Procedure call", pseudo: PC_PS, py: PC_PY, frames: {anim_proc()} }});
tr($("#aF"), {{ label: "Function call", pseudo: FN_PS, py: FN_PY, frames: {anim_fn()} }});
tr($("#aS"), {{ label: "Local and global", pseudo: SC_PS, py: SC_PY, frames: {anim_scope()} }});
tr($("#aH"), {{ label: "Same name, two variables", pseudo: SH_PS, py: SH_PY, frames: {anim_shadow()} }});
Lib.codePanel($("#cdP0"), {{ pseudo: ["PROCEDURE ShowLine", '    OUTPUT "----------"', "ENDPROCEDURE", "", "CALL ShowLine", 'OUTPUT "Menu"', "CALL ShowLine"], py: ["def show_line():", '    print("----------")', "", "show_line()", 'print("Menu")', "show_line()"] }});
Lib.codePanel($("#cdPc"), {{ pseudo: PC_PS, py: PC_PY }});
Lib.codePanel($("#cdFn"), {{ pseudo: FN_PS, py: FN_PY }});
Lib.codePanel($("#cdSc"), {{ pseudo: SC_PS, py: SC_PY }});
''')

js.append(r'''
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
''')
write_js("p816", js)
