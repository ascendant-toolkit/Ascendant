"""AS CS 11.3: structured programming. Run: python3 tools/artifact-kit/mk_as113.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t mono"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Structured programming</b> breaks a program into named, self-contained <b>subroutines</b> (also called <b>modules</b>): a <b>procedure</b> does a task, and a <b>function</b> does a task and <b>returns a value</b>. Data is passed in through <b>parameters</b>; the values supplied when the subroutine is called are the <b>arguments</b>. A <b>local</b> variable exists only inside its subroutine, while a <b>global</b> variable can be used anywhere. Subroutines mean a repeated or separate task is written once, tested on its own and reused, so the program is shorter and easier to understand, test and maintain. A program is also easier to read when it uses <b>meaningful names, indentation and white space, capitalised keywords and comments</b>.</p></div>

  <h2>1 · Procedures and functions</h2>
  ''' + pc('''
PROCEDURE ShowTotal(Name : STRING, Total : REAL)
   OUTPUT Name, " owes ", Total
ENDPROCEDURE

FUNCTION IsAdult(Age : INTEGER) RETURNS BOOLEAN
   IF Age >= 18 THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION

CALL ShowTotal("Mr Khan", 15.75)        // a procedure is called with CALL
IF IsAdult(MyAge) THEN                   // a function is called inside an expression
   OUTPUT "Adult"
ENDIF''') + '''
  <div class="tw"><table class="t">
    <tr><th></th><th>Procedure</th><th>Function</th></tr>
    <tr><td><b>Returns a value?</b></td><td>No</td><td>Yes: RETURNS a type and uses RETURN</td></tr>
    <tr><td><b>Called</b></td><td>As a statement: CALL Name(...)</td><td>Inside an expression or assignment</td></tr>
    <tr><td><b>Header</b></td><td>PROCEDURE Name(Param : TYPE)</td><td>FUNCTION Name(Param : TYPE) RETURNS TYPE</td></tr>
  </table></div>
  <p>Use a function when the subroutine produces a single result (a check, a calculation). Use a procedure when it performs an action (output, write to a file, change several values).</p>

  <h2>2 · Parameters</h2>
  <ul>
    <li>In the header the names are <b>parameters</b>, each with a data type: <span class="mono">PROCEDURE MyProc(Count : INTEGER, Message : STRING)</span>. Parameters pass values into the subroutine; this makes it reusable with different data.</li>
    <li><b>By value (BYVAL, the default)</b>: the subroutine gets a copy, so changing it does not change the caller's variable.</li>
    <li><b>By reference (BYREF)</b>: the subroutine works on the caller's variable itself, so a change is seen by the caller. It is how a procedure can send back more than one value: <span class="mono">PROCEDURE Mod_X(T4 : INTEGER, BYREF P3 : REAL)</span>.</li>
    <li>The arguments in the call must match the parameters in number, order and type.</li>
  </ul>

  <h2>3 · Local and global variables</h2>
  <ul>
    <li><b>Local:</b> declared inside the subroutine; it exists only while it runs, cannot be changed by other subroutines, and its name can be reused elsewhere. This is the better choice.</li>
    <li><b>Global:</b> declared outside any subroutine; any part of the program can use or change it, so it is harder to test and a fault can appear in any subroutine that touches it. A global is sometimes used for data shared by many parts (a list of settings).</li>
    <li>A fault with a global variable is exposed by testing different paths, for example data that does and does not cause the assignment to happen.</li>
  </ul>

  <h2>4 · Why use subroutines (and library routines)?</h2>
  <ul>
    <li>A task repeated or reused in several places is written once.</li>
    <li>Each subroutine does one specific job: the program is simpler, and each part is easier to test, debug and maintain.</li>
    <li>Different programmers can write different subroutines at the same time.</li>
    <li><b>Library routines</b> are ready-made subroutines: they are tried and tested, do things you may not be able to program yourself (encryption), and save development time.</li>
  </ul>

  <h2>5 · Writing readable programs</h2>
  <p>Meaningful identifier names, indentation and blank lines (white space), capital letters for keywords, and comments that explain why. These make the code easier to read, understand, debug and maintain.</p>

  <h2>6 · Reading code in the exam</h2>
  <p>Questions give a numbered listing and ask for: a line with an <b>initialisation</b> (a variable set before a loop, such as OutString ← ""), the start of a <b>repeating block</b> (the FOR or WHILE line), a <b>logic operation</b> (AND, OR, NOT), the <b>number of parameters</b> a function takes (MID takes three), the type of loop, and what could be simplified. NOT((c &lt; 'a') OR (c &gt; 'z')) simplifies to (c &gt;= 'a') AND (c &lt;= 'z').</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing "function" for a module that does not return a value, or the other way round.</li>
    <li>Saying a parameter and an argument are the same without the context: parameters are in the header, arguments in the call.</li>
    <li>Forgetting RETURNS and the type in a function header, or the RETURN statement itself.</li>
    <li>Using a global variable when a parameter or a local variable would do.</li>
  </ul>
'''

watch = '''
  <h2>1 · Calling a function</h2>
  <div id="stA"></div>
  <h2>2 · By value and by reference</h2>
  <div id="stB"></div>
  <h2>3 · Local and global scope</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · By value or by reference?</h2>
  <p>A procedure doubles its parameter. Run it with each passing method.</p>
  <div class="card"><div class="btnrow"><label>X <input id="pm_x" type="number" value="5" style="width:70px"></label><button id="pm_val">PROCEDURE Double(BYVAL N)</button><button id="pm_ref">PROCEDURE Double(BYREF N)</button></div><div id="pmV"></div></div>
  <h2>Lab 2 · Where can the variable be used?</h2>
  <div class="card"><div id="scB" class="btnrow"></div><div id="scO"></div></div>
  <h2>Lab 3 · Procedure or function?</h2>
  <div class="card"><div id="pfB" class="btnrow"></div><div id="pfO"></div></div>
'''

_pr, _prjs = PR(["Procedure or function?", "Local or global?", "Match the term", "Put the function call steps in order", "Working out", "Multiple choice"],
  ("Is this a procedure or a function?", ["Procedure", "Function"], [("Returns TRUE if a number is prime", 1), ("Outputs a report to the screen", 0), ("Returns the average of three marks", 1), ("Writes a new line to a file", 0), ("FUNCTION ... RETURNS INTEGER", 1), ("Called with CALL", 0)], "A function returns a value."),
  ("Local or global?", ["Local", "Global"], [("Exists only while the subroutine runs", 0), ("Can be changed from any subroutine", 1), ("Declared outside any subroutine", 1), ("Its name can be reused in another subroutine", 0), ("A fault in it may be anywhere in the program", 1), ("The better choice for most variables", 0)], "Local is safe; global is shared."),
  [["Parameter", "A name and type in the subroutine header"], ["Argument", "The value supplied when it is called"], ["BYREF", "Changes the caller's variable"], ["BYVAL", "Works on a copy"], ["RETURN", "Sends a value back from a function"]],
  ("Put the steps of a function call IsAdult(17) in order.", ["The program reaches IsAdult(17) in an expression", "The value 17 is passed to the parameter Age", "The function body runs: 17 >= 18 is false", "RETURN FALSE sends a value back", "The call is replaced by FALSE in the expression"], "Call, pass, run, return, replace."),
  [{"q": "MID(InString, Counter, 1) is called with how many parameters?", "a": 3, "unit": "", "tol": 0.01, "hint": "String, start, length.", "sol": "<b>3</b>."}, {"q": "A procedure has the header PROCEDURE P(A : INTEGER, BYREF B : REAL, C : STRING). How many parameters does it take?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count A, B, C.", "sol": "<b>3</b>."}, {"q": "A procedure doubles BYVAL N. X = 5 before the call. What is X after?", "a": 5, "unit": "", "tol": 0.01, "hint": "A copy was changed.", "sol": "<b>5</b>."}, {"q": "The same procedure with BYREF N. What is X after?", "a": 10, "unit": "", "tol": 0.01, "hint": "The original is changed.", "sol": "<b>10</b>."}, {"q": "A program has 4 subroutines. Two are functions. How many are procedures?", "a": 2, "unit": "", "tol": 0.01, "hint": "4 − 2.", "sol": "<b>2</b>."}],
  [("A function differs from a procedure because it:", ["Returns a value", "Has no parameters", "Cannot be called", "Has no header"], 0, "Returns."), ("In PROCEDURE MyProc(Count : INTEGER), Count is a:", ["Parameter", "Argument", "Constant", "Library"], 0, "In the header."), ("BYREF means the subroutine:", ["Changes the caller's variable", "Works on a copy", "Cannot use the value", "Returns a string"], 0, "Reference."), ("A local variable:", ["Exists only in its subroutine", "Exists everywhere", "Cannot be changed", "Is a constant"], 0, "Local."), ("A benefit of a library routine:", ["It is tried and tested", "It is always slower", "It cannot be reused", "It has no parameters"], 0, "Tested."), ("A feature of readable code:", ["Meaningful identifiers and indentation", "Single-letter names only", "No blank lines", "No comments"], 0, "Readability.")],
  [("Procedure", "Does a task; no value returned."), ("Function", "Returns a value."), ("Parameter", "In the header."), ("Argument", "In the call."), ("BYVAL", "A copy."), ("BYREF", "The original."), ("Local", "Only inside the subroutine."), ("Global", "Anywhere in the program.")])

real = RWNOTE + (
rw("A spreadsheet function", "SUM(A1:A9) is a function: you give it values (parameters) and it returns a result.", "function and parameters.") +
rw("Games", "A game has subroutines such as DrawScreen(), MovePlayer() and CheckCollision(); each can be tested on its own.", "subroutines.") +
rw("A team project", "Different programmers write different subroutines, and a library routine does the encryption that nobody wanted to write from scratch.", "teamwork and library routines.") +
rw("Settings", "A global variable such as Volume can be read by every part of an app; any part can also change it, which is why bugs with globals are hard to find.", "global variables.")
)

where = [
  ("M/J 2021", "22", "5(b)", "4 + 2", "Read a function listing: initialisation, loop start, logic and the number of MID parameters; simplify a condition"),
  ("O/N 2021", "22", "4", "5 + 3 + 2 + 1", "Read a procedure: line numbers, loop type, functions, parameters; readability; a better loop"),
  ("O/N 2022", "21", "1(a)", "3", "Benefits of library routines"),
  ("O/N 2022", "22", "1(a)", "2 + 2", "Reasons for a subroutine; the term for identifiers in a header"),
  ("O/N 2023", "22", "6(b)", "3", "Type of module, header and file mode for CheckFiles()")]

past = '''  <p class="note">Questions on subroutines ask you to read a header, name the type of module, state why subroutines are used, or read a numbered listing. The structure chart questions that use module headers are on the program design pages (section 12.2).</p>
''' + peq(SRC("w22", "22", "Q1(a)"), "2 + 2 marks", "State / Give",
  "An algorithm has a part that would be appropriate to implement as a subroutine (a procedure or a function). (i) State two reasons why the programmer may use a subroutine. (ii) A procedure header is PROCEDURE MyProc(Count : INTEGER, Message : STRING). Give the correct term for the identifiers Count and Message and explain their use.", "Reuse; simpler, easier to test. Parameters pass values in.",
  "<p><b>(i)</b> Any two: " + mks(["A task is repeated or reused in several places", "A part of the algorithm performs a specific task", "It reduces the complexity of the program (or a subroutine is already available)", "Testing, debugging and maintenance are easier"], "b") + "</p><p><b>(ii)</b> " + mks(["Term: parameters", "Use: to pass values (arguments) to the procedure"], "a") + "</p>", "Saying \"variables\" for Count and Message: the term is parameters.") + peq(SRC("w22", "21", "Q1(a)"), "3 marks", "State",
  "An algorithm includes a number of complex calculations. A programmer decides to use library routines to provide part of the solution. State three possible benefits of using library routines in the development of the program.", "Tested, hard to write, quick.",
  "<p>" + mks(["They are tried and tested, so free from errors", "They perform a function that you may not be able to program yourself (for example encryption)", "They are readily available and speed up development time"]) + "</p>", None) + peq(SRC("s21", "22", "Q5(b)"), "4 + 2 marks", "Complete / Write",
  "01 FUNCTION StringClean(InString : STRING) RETURNS STRING; 03 DECLARE NextChar : CHAR; 04 DECLARE OutString : STRING; 05 DECLARE Counter : INTEGER; 07 OutString ← \"\"; 09 FOR Counter ← 1 TO LENGTH(InString); 10 NextChar ← MID(InString, Counter, 1); 11 NextChar ← LCASE(NextChar); 12 IF NOT((NextChar < 'a') OR (NextChar > 'z')) THEN; 13 OutString ← OutString & NextChar; 14 ENDIF; 15 NEXT Counter; 17 RETURN OutString; 19 ENDFUNCTION. (i) Give a line number containing an initialisation statement, the start of a repeating block, a logic operation, and the number of parameters of MID(). (ii) Write a simplified version of the statement in line 12.", "07; 09; 12; MID takes three. NOT(a OR b) = NOT a AND NOT b.",
  "<p><b>(i)</b> One mark per row:" + tbl(["Question", "Answer"], [["A line number containing an initialisation statement", "07"], ["A line number containing the start of a repeating block", "09 or 10"], ["A line number containing a logic operation", "12"], ["The number of parameters of function MID()", "3"]], "t") + "</p><p><b>(ii)</b> " + mks(["IF ... AND ...", "Both conditions correct"], "b") + "</p>" + pc("IF (NextChar >= 'a') AND (NextChar <= 'z') THEN"), "Leaving the NOT in place or changing OR to AND without reversing both comparisons.") + peq(SRC("w21", "22", "Q4"), "5 + 3 + 2 + 1 marks", "Complete / Identify / State",
  "10 PROCEDURE Check(InString : STRING); 11 DECLARE Odds, Evens, Index : INTEGER; 13 Odds ← 0; 14 Evens ← 0; 15 Index ← 1; 17 WHILE Index <= LENGTH(InString); 18 IF STR_TO_NUM(MID(InString, Index, 1)) MOD 2 <> 0 THEN; 19 Odds ← Odds + 1; 20 ELSE; 21 Evens ← Evens + 1; 22 ENDIF; 23 Index ← Index + 1; 24 ENDWHILE; 26 CALL Result(Odds, Evens); 27 ENDPROCEDURE. (a) Complete the table: a line number containing a variable being incremented; the type of loop structure; the number of functions used; the number of parameters passed to STR_TO_NUM(); the name of a procedure other than Check(). (b) Identify three features that make the pseudocode easier to read. (c)(i) The loop is not the most appropriate: state a more appropriate loop and justify it. (ii) With that loop two lines are changed and two removed: write the line numbers of the two lines removed.", "Counted loop; FOR replaces the manual index.",
  "<p><b>(a)</b> One mark each:" + tbl(["Question", "Answer"], [["A line number containing a variable being incremented", "19, 21 or 23"], ["The type of loop structure", "Pre-condition (WHILE)"], ["The number of functions used", "3 (LENGTH, STR_TO_NUM, MID)"], ["The number of parameters passed to STR_TO_NUM()", "1"], ["The name of a procedure other than Check()", "Result"]], "t") + "</p><p><b>(b)</b> " + mks(["Meaningful variable names", "Indentation and white space (blank lines)", "Capitalisation of keywords"]) + "</p><p><b>(c)(i)</b> " + mks(["Structure: a count-controlled loop (FOR)", "Justification: the number of iterations is known (the length of InString)"], "a") + "</p><p><b>(ii)</b> " + mks(["15 and 23 (the initialisation and the increment of Index)"], "a") + "</p>", "Naming the loop but not justifying it from the code: the number of repeats is the length of the string, which is known before the loop starts.") + peq(SRC("w23", "22", "Q6(b)"), "3 marks", "Identify / Write / State",
  "A module CheckFiles() takes a file name as its parameter and returns the number of files found. (i) Identify the type of module. (ii) Write the module header. (iii) State the file mode it uses on the files.", "It returns a value: function. RETURNS INTEGER. It only reads.",
  "<p>" + mks(["(i) Function", "(ii) FUNCTION CheckFiles(NameRoot : STRING) RETURNS INTEGER", "(iii) Read"]) + "</p>", "Writing PROCEDURE: a module that returns a value is a function.")

review = req("3 marks", "State", "State the difference between a procedure and a function.", "Returns.", "<p>" + mks(["A function returns a value; a procedure does not", "A function is used in an expression or assignment", "A procedure is called with CALL"]) + "</p>", None) + req("3 marks", "Write", "Write the header and body of a function Double() that takes an INTEGER and returns it multiplied by two.", "FUNCTION ... RETURNS ... RETURN.", "<p>" + mks(["Header with parameter and type", "RETURNS INTEGER", "RETURN N * 2 and ENDFUNCTION"]) + "</p>" + pc("FUNCTION Double(N : INTEGER) RETURNS INTEGER\n   RETURN N * 2\nENDFUNCTION"), None) + req("2 marks", "Explain", "Explain the difference between BYVAL and BYREF parameters.", "Copy or original.", "<p>" + mks(["BYVAL passes a copy, so the caller's variable is unchanged", "BYREF passes the variable itself, so a change is seen by the caller"]) + "</p>", None) + req("2 marks", "State", "State two reasons why local variables are better than global variables.", "Safe, reusable.", "<p>" + mks(["They cannot be changed accidentally by other subroutines", "Their names can be reused, and the subroutine can be tested on its own"]) + "</p>", None) + req("3 marks", "Identify", "Identify three ways of making pseudocode easier to read.", "Names, indentation, keywords.", "<p>" + mks(["Meaningful identifier names", "Indentation and white space", "Capitalised keywords (or comments)"]) + "</p>", None)

tips = tips_html([
  ("Function = returns.", "Write RETURNS and the type, and a RETURN statement."),
  ("Parameter or argument.", "Header or call."),
  ("BYREF changes the original.", "BYVAL works on a copy."),
  ("Prefer local.", "Pass values in with parameters."),
  ("Read the listing.", "Initialise before the loop; the loop line starts the repeating block."),
  ("Library routines.", "Tested, hard to write, quick to use."),
], [("a subroutine", "A named block of code: a procedure or a function."), ("a parameter", "A name in the header that receives a value."), ("an argument", "The value passed in a call."), ("scope", "Where in the program a variable can be used.")],
  [("State", "A short answer."), ("Identify", "Name it from the code."), ("Write", "Write the header or the code."), ("Explain", "Give the reason.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["IF IsAdult(17) THEN", "Age ← 17  (argument 17 into parameter Age)", "17 >= 18 is FALSE", "RETURN FALSE", "IF FALSE THEN"]; let o = ""; L.forEach((t, i) => o += SV.rect(10, 8 + i * 26, 320, 22, i === k ? "f3" : "cell", { rx: 4 }) + SV.text(18, 24 + i * 26, t, "lbl bd", { style: "font-size:12px;font-family:monospace" })); return o; };
  Lib.stepper($("#stA"), { w: 340, h: 145, label: "Function call", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The function is called inside the IF.", "The argument 17 is passed to the parameter.", "The body runs.", "A value is returned.", "The call is replaced by the returned value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 10, 120, 34, "cell", { rx: 6 }) + SV.text(20, 32, "X = " + (k >= 3 ? "10" : "5"), "lbl bd", { style: "font-size:14px;font-family:monospace" }); if (k >= 1) o += SV.rect(190, 10, 120, 34, "f3", { rx: 6 }) + SV.text(200, 32, "N = " + (k >= 2 ? "10" : "5"), "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(10, 74, ["Before the call", "BYREF: N is X itself (BYVAL: a copy)", "N ← N * 2 inside the procedure", "X is now 10 (BYVAL: still 5)"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 92, label: "BYREF", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["X holds 5.", "CALL Double(X) with BYREF.", "The procedure doubles N.", "The change is seen by the caller."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 6, 320, 28, k === 0 ? "f3" : "cell", { rx: 5 }) + SV.text(18, 24, "GLOBAL  Volume = 7   (visible everywhere)", "lbl bd", { style: "font-size:12px" }); o += SV.rect(10, 44, 150, 62, k === 1 ? "f3" : "cell", { rx: 5 }) + SV.text(18, 62, "PROCEDURE A", "lbl bd", { style: "font-size:12px" }) + SV.text(18, 80, "local Temp = 1", "lbl", { style: "font-size:12px;font-family:monospace" }) + SV.text(18, 96, "can use Volume", "lbl", { style: "font-size:11px" }); o += SV.rect(180, 44, 150, 62, k === 2 ? "f3" : "cell", { rx: 5 }) + SV.text(188, 62, "PROCEDURE B", "lbl bd", { style: "font-size:12px" }) + SV.text(188, 80, "local Temp = 99", "lbl", { style: "font-size:12px;font-family:monospace" }) + SV.text(188, 96, "its own Temp", "lbl", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 340, h: 118, label: "Scope", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A global variable can be used by every subroutine.", "A's local Temp exists only inside A.", "B has a separate Temp: no clash, and B cannot see A's."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#pm_x"); const go = (ref) => { const x = Math.round(+inp.value || 0); const n = x * 2; $("#pmV").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Passing</th><th>X before</th><th>N after Double</th><th>X after</th></tr><tr><td>${ref ? "BYREF" : "BYVAL"}</td><td>${x}</td><td>${n}</td><td><b>${ref ? n : x}</b></td></tr></table></div><div class="verdict">${ref ? "BYREF: N is the caller's variable, so X changed." : "BYVAL: N is a copy, so X is unchanged."}</div>`; };
  $("#pm_val").onclick = () => go(false); $("#pm_ref").onclick = () => go(true); go(false);
})();
btnTable("scB", "scO", [
  ["A variable declared inside PROCEDURE A", "Only in A", "local: exists while A runs"],
  ["A variable declared before all procedures", "Anywhere", "global"],
  ["A parameter in a header", "Only in that subroutine", "it behaves like a local variable"],
  ["Two procedures each declare Temp", "Each has its own Temp", "locals do not clash"]
], ["Variable", "Where it can be used", "Why"]);
btnTable("pfB", "pfO", [
  ["IsPrime(N) returns TRUE or FALSE", "Function", "returns a value"],
  ["ShowMenu() prints options", "Procedure", "an action, no value"],
  ["Average(A, B, C) gives the mean", "Function", "returns a value"],
  ["SaveScores() writes the scores to a file", "Procedure", "an action"],
  ["CheckFiles(NameRoot) returns the number found", "Function", "RETURNS INTEGER"]
], ["Subroutine", "Type", "Why"]);
''' + _prjs

finish("as-11-3-structured-programming", "as113", "Structured Programming",
  "Procedures and functions, parameters, by value and by reference, local and global variables, library routines and readable code, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "11.3", "11 · Programming", "section 11.3 Structured programming", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on subroutines (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
