"""AS CS 12.2.1: structure charts. Run: python3 tools/artifact-kit/mk_as1221.py"""
from ascs import *
from ak12 import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

# the charts used on this page
C_LOAN = sc_html({"U": ("UpdateLoan()", 260, 30), "E": ("LoanExtend()", 130, 150), "R": ("LoanReturn()", 400, 150), "K": ("CheckReserve()", 130, 270)},
  [("U", "E", ["sel"], [("down", "data", "LoanID", 0.35, -1), ("down", "data", "BookID", 0.62, -1), ("up", "flag", "", 0.5, 1)]),
   ("U", "R", [], [("down", "data", "LoanID", 0.32, -1), ("down", "data", "BookID", 0.58, -1), ("up", "data", "Fine", 0.45, 1)]),
   ("E", "K", [], [("down", "data", "BookID", 0.5, -1), ("up", "flag", "", 0.5, 1)])], 520, 310, "Structure chart for the library modules")
C_HEAD = sc_html({"A": ("Head", 260, 30), "B": ("Mod_W", 80, 150), "C": ("Mod_X", 260, 150), "D": ("Mod_V", 440, 150), "E": ("Mod_Z", 340, 270), "F": ("Mod_Y", 500, 270)},
  [("A", "B", ["it"], [("down", "data", "P4", 0.5, -1)]),
   ("A", "C", [], [("down", "data", "T4", 0.35, -1), ("both", "data", "P3", 0.65, 1)]),
   ("A", "D", [], [("down", "data", "S2", 0.4, 1), ("up", "flag", "", 0.65, -1)]),
   ("D", "E", [], [("down", "data", "F3", 0.4, -1), ("up", "data", "", 0.6, 1)]),
   ("D", "F", [], [("down", "data", "W3", 0.35, -1), ("down", "data", "Z8", 0.65, 1)])], 560, 310, "Structure chart for Head")
C_SEC = sc_html({"S": ("Section_1()", 260, 30), "A": ("Sub1_A", 90, 150), "B": ("Sub1_B", 260, 150), "C": ("Sub1_C", 430, 150)},
  [("S", "A", ["sel"], [("down", "data", "XT", 0.35, -1), ("down", "data", "PB", 0.65, 1)]),
   ("S", "B", [], [("down", "data", "RA", 0.4, -1), ("up", "flag", "", 0.6, 1)]),
   ("S", "C", [], [("down", "data", "SB", 0.35, -1), ("both", "data", "SA", 0.65, 1)])], 520, 190, "Structure chart for Section_1")
C_CONV = sc_html({"C": ("Convert", 260, 30), "A": ("Analyse", 90, 150), "U": ("Update", 260, 150), "S": ("Sort", 430, 150)},
  [("C", "A", ["it"], [("down", "data", "Count", 0.5, -1)]),
   ("C", "U", [], [("down", "data", "Key", 0.35, -1), ("up", "data", "T1", 0.6, 1)]),
   ("C", "S", [], [("both", "flag", "P2", 0.5, 1)])], 520, 190, "Structure chart for Convert")
C_MAIN = sc_html({"M": ("Main", 270, 30), "A": ("Sub_A", 130, 130), "B": ("Sub_B", 420, 130), "A1": ("Sub_Part1A", 50, 240), "A2": ("Sub_Part2A", 190, 240), "A3": ("Sub_Part3A", 330, 240), "B1": ("Sub_Part1B", 420, 240), "B2": ("Sub_Part2B", 540, 240)},
  [("M", "A", ["sel"], [("down", "data", "M", 0.35, -1), ("both", "data", "P", 0.65, 1)]),
   ("M", "B", [], [("up", "flag", "", 0.5, 1)]),
   ("A", "A1", ["it"], [("down", "data", "R", 0.5, -1)]),
   ("A", "A2", [], [("down", "data", "T", 0.35, 1), ("up", "flag", "", 0.65, -1)]),
   ("A", "A3", [], [("down", "data", "V", 0.3, 1), ("down", "flag", "W", 0.58, 1), ("both", "data", "U", 0.82, -1)])], 600, 290, "Structure chart with Main, Sub_A and Sub_B")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>structure chart</b> shows how a program is divided into <b>modules</b> (procedures and functions) and how they relate: which module calls which, and what <b>parameters</b> pass between them. It is drawn as a hierarchy: the top module calls the modules below it. Arrows beside the lines show the parameters passed <b>down</b> to a module and the values passed <b>up</b> (returned) to the module that called it. A <b>diamond</b> shows <b>selection</b> (one of the lower modules is called) and a <b>curved arrow</b> shows <b>repetition</b> (the lower modules are called repeatedly, in order, left to right). Structure charts are produced in the design stage, from the problem broken down by <b>decomposition</b>.</p></div>

  <h2>1 · The notation</h2>
  ''' + tbl(["Symbol", "Meaning"], [["Rectangle", "A module (procedure or function) with its name"], ["Line from a module to the one below", "The upper module calls the lower module"], ["Arrow pointing down with an open circle", "A data parameter passed to the lower module"], ["Arrow pointing up", "A value returned to the calling module: the lower module is a <b>function</b>"], ["Arrow with a filled circle", "A flag (a Boolean value)"], ["Arrow with a head at both ends", "A value passed in and passed back: a <b>BYREF</b> parameter"], ["Diamond on the calling module", "<b>Selection</b>: one of the lower modules is called, chosen when the program runs"], ["Curved arrow under the calling module", "<b>Repetition</b>: the lower modules are called repeatedly in order, left to right"]]) + '''
  <p>A module with no upward arrow is a <b>procedure</b>; a module with an upward arrow is a <b>function</b> and its header ends with <span class="mono">RETURNS</span> and a type.</p>

  <h2>2 · Reading a chart to write headers</h2>
  ''' + C_CONV + '''
  <p>Analyse has one parameter coming down (Count): <span class="mono">PROCEDURE Analyse(Count : INTEGER)</span>. Update has Key coming down and T1 coming back, so it is a function: <span class="mono">FUNCTION Update(Key : STRING) RETURNS INTEGER</span>. Sort has a two-headed arrow: <span class="mono">PROCEDURE Sort(BYREF P2 : BOOLEAN)</span>. The curved arrow on Convert means it repeatedly calls Analyse, then Update, then Sort.</p>

  <h2>3 · Drawing a chart from headers</h2>
  <ol>
    <li>Put the top (calling) module at the top and the modules it calls below it, in the order they are called.</li>
    <li>Join each pair with a line.</li>
    <li>For each parameter in a header, add a down arrow with an open circle (open circle for data, filled for a Boolean flag).</li>
    <li>For a FUNCTION add an up arrow for the returned type. For BYREF add an arrow with two heads.</li>
    <li>Add a diamond if one of the modules is called, or the curved arrow if they are called repeatedly.</li>
  </ol>

  <h2>4 · Why use a structure chart and decomposition</h2>
  <ul>
    <li>Breaking a complex problem into sub-problems (<b>decomposition</b>) makes it easier to understand and solve.</li>
    <li>Smaller modules are easier to program, test and maintain.</li>
    <li>Different modules can be given to different teams or programmers with different expertise and solved separately.</li>
    <li>A structure chart shows the relationships and hierarchy, the parameters passed between modules, and whether each module is a function or a procedure.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Arrows in the wrong direction: down is a parameter passed to the lower module; up is a value returned.</li>
    <li>Forgetting the up arrow for a function, or adding one for a procedure.</li>
    <li>Showing selection when the question says the modules are called repeatedly (and the other way round).</li>
    <li>Leaving out the data types in a header, or BYREF on a two-headed arrow.</li>
  </ul>
'''

watch = '''
  <h2>1 · Building a structure chart</h2>
  <div id="stA"></div>
  <h2>2 · Selection and repetition</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Header to arrows</h2>
  <p>Choose a header and see how it appears on the chart.</p>
  <div class="card"><div id="hdB" class="btnrow"></div><div id="hdV"></div></div>
  <h2>Lab 2 · What does the symbol mean?</h2>
  <div class="card"><div id="syB" class="btnrow"></div><div id="syO"></div></div>
'''

_pr, _prjs = PR(["Procedure or function?", "Symbol meaning", "Match the symbol", "Put the drawing steps in order", "Working out", "Multiple choice"],
  ("Is the module a procedure or a function, from the chart?", ["Procedure", "Function"], [("Arrow down only", 0), ("Arrow down and an arrow up", 1), ("Only an arrow up", 1), ("No arrows at all", 0), ("A two-headed arrow only", 0), ("Header ends with RETURNS BOOLEAN", 1)], "An upward arrow means a returned value."),
  ("What does the symbol show?", ["Selection", "Repetition", "BYREF parameter"], [("A diamond on the calling module", 0), ("A curved arrow under the calling module", 1), ("An arrow with a head at both ends", 2), ("One of the lower modules is called", 0), ("Lower modules are called repeatedly in order", 1), ("A value passed in and changed", 2)], "Diamond: choose. Curve: repeat. Two heads: in and out."),
  [["Rectangle", "A module"], ["Down arrow", "A parameter passed in"], ["Up arrow", "A value returned"], ["Diamond", "Selection"], ["Curved arrow", "Repetition"]],
  ("Put the steps for drawing a structure chart in order.", ["Put the calling module at the top", "Put the called modules below, in order", "Join each pair with a line", "Add the parameter arrows with circles", "Add the diamond or curved arrow"], "Boxes, lines, arrows, symbols."),
  [{"q": "A calling module has 3 lower modules. How many lines join it to them?", "a": 3, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>3</b>."}, {"q": "PROCEDURE Mod_Y(W3 : REAL, Z8 : INTEGER) needs how many down arrows?", "a": 2, "unit": "", "tol": 0.01, "hint": "One per parameter.", "sol": "<b>2</b>."}, {"q": "FUNCTION Mod_V(S2 : INTEGER) RETURNS BOOLEAN needs how many arrows in total?", "a": 2, "unit": "", "tol": 0.01, "hint": "One down, one up.", "sol": "<b>2</b>."}, {"q": "PROCEDURE Mod_X(T4 : INTEGER, BYREF P3 : REAL): how many arrows?", "a": 2, "unit": "", "tol": 0.01, "hint": "T4 down, P3 two-headed.", "sol": "<b>2</b>."}, {"q": "A chart has 6 modules. How many lines join them in the hierarchy?", "a": 5, "unit": "", "tol": 0.01, "hint": "Every module except the top has one line above it.", "sol": "<b>5</b>."}],
  [("An arrow pointing up beside a line shows:", ["A value returned to the caller", "A parameter passed down", "Selection", "Repetition"], 0, "Returned."), ("A diamond on a module means:", ["One of the lower modules is called", "All are called repeatedly", "It is a function", "It is a library"], 0, "Selection."), ("A curved arrow under a module means:", ["Repetition of the lower modules in order", "Selection", "A function", "A return"], 0, "Repetition."), ("A two-headed arrow shows:", ["A BYREF parameter", "A function return", "Selection", "A library"], 0, "In and out."), ("A structure chart is produced in:", ["The design stage", "The testing stage", "The analysis stage", "Maintenance"], 0, "Design."), ("A benefit of decomposition:", ["Modules can be given to different teams", "Programs run faster", "No testing is needed", "No parameters are needed"], 0, "Teams.")],
  [("Module", "A procedure or function."), ("Parameter", "A value passed to a module."), ("Diamond", "Selection."), ("Curved arrow", "Repetition."), ("Up arrow", "Returned value: a function."), ("Two-headed arrow", "BYREF."), ("Filled circle", "A Boolean flag."), ("Decomposition", "Breaking a problem into sub-problems.")])

real = RWNOTE + (
rw("A game's design document", "Before coding, the team draws the modules: Main calls LoadLevel, then repeatedly calls ReadInput, UpdateWorld and DrawScreen.", "repetition on a structure chart.") +
rw("A cash machine", "One module reads the card, then a choice of Withdraw, Balance or Deposit is called depending on what the user presses.", "selection.") +
rw("A construction plan", "A big building is broken into sections that different teams build at once, as modules are given to different programmers.", "decomposition.") +
rw("A function in a spreadsheet", "A formula takes values in and returns one value, like an up arrow on a function module.", "functions.")
)

where = [
  ("M/J 2021", "21", "2(a)(b)", "5 + 2", "Draw a structure chart for four library modules; write a module header"),
  ("M/J 2022", "22", "3", "3 + 3 + 3", "Complete a structure chart from five module headers; identify the modules; benefits of decomposition"),
  ("M/J 2023", "22", "3", "2 + 5", "The purpose of a structure chart; draw a chart with selection"),
  ("O/N 2023", "23", "7", "2 + 3 + 2", "The meaning of the curved arrow; define a record type; write a procedure header"),
  ("M/J 2025", "23", "6", "1 + 5 + 3", "Function and procedure; headers from a chart; the diamond and curved arrow"),
  ("O/N 2025", "22", "7", "2 + 4", "The meaning of the curved arrow; module headers from a chart")]

past = '''  <p class="note">Structure chart diagrams are redrawn here from the descriptions and the mark schemes. The answer diagrams follow the notation in the mark schemes; accept any clear equivalent in the exam.</p>
''' + peq(SRC("s21", "21", "Q2(a)(b)"), "5 + 2 marks", "Draw / Write",
  "Four modules form part of a library program. UpdateLoan() calls either LoanExtend() or LoanReturn() and is called with parameters LoanID and BookID. LoanExtend() is called with parameters LoanID and BookID, calls CheckReserve(), and returns TRUE if the loan has been extended, otherwise FALSE. CheckReserve() is called with BookID and returns TRUE if the book has been reserved for another library user, otherwise FALSE. LoanReturn() is called with parameters LoanID and BookID and returns a REAL (the fine to be paid for an overdue loan). (a) Draw a structure chart to show the relationship between the four modules and the parameters passed between them. (b) LoanReturn() is amended: it is called with LoanID and BookID (STRING) and Fine (REAL), and assigns a new value to Fine. Write the pseudocode header.", "Selection diamond on UpdateLoan only. Parameters down; returned values up.",
  "<p><b>(a)</b> " + mks(["All four boxes correctly labelled and positioned", "A selection diamond (only on UpdateLoan, and no iteration arrows)", "Parameters to and from LoanExtend()", "Parameters to and from CheckReserve()", "Parameters to and from LoanReturn()"]) + "</p>" + C_LOAN + "<p><b>(b)</b> " + mks(["PROCEDURE LoanReturn(LoanID, BookID : STRING, ...", "... BYREF Fine : REAL)"], "a") + "</p>" + pc("PROCEDURE LoanReturn(LoanID, BookID : STRING, BYREF Fine : REAL)"), "Drawing a diamond on every line, or adding a curved arrow: UpdateLoan calls one or the other, not both in turn.") + peq(SRC("s22", "22", "Q3(a)(b)"), "3 + 3 + 3 marks", "Complete / Describe",
  "The module headers for five modules are: FUNCTION Mod_V(S2 : INTEGER) RETURNS BOOLEAN; PROCEDURE Mod_W(P4 : INTEGER); PROCEDURE Mod_X(T4 : INTEGER, BYREF P3 : REAL); PROCEDURE Mod_Y(W3 : REAL, Z8 : INTEGER); FUNCTION Mod_Z(F3 : REAL) RETURNS INTEGER. An additional module Head() repeatedly calls three of the modules in sequence. A structure chart has been partially completed (boxes A to F). (i) Complete the structure chart. (ii) Complete a table giving the module name for each label A to F. (b) Describe three benefits of decomposition.", "Head calls W, X, V in turn (repeatedly). V calls Z and Y.",
  "<p><b>(a)(i)</b> One mark per annotation added (the curved arrow, the missing arrows to and from the modules):</p>" + C_HEAD + "<p><b>(ii)</b> " + tbl(["Label", "Module name"], [["A", "Head"], ["B", "Mod_W"], ["C", "Mod_X"], ["D", "Mod_V"], ["E", "Mod_Z"], ["F", "Mod_Y"]]) + "Two rows correct: one mark; four rows: two marks; all six: three marks.</p><p><b>(b)</b> " + mks(["Breaking a complex problem down makes it easier to understand or solve", "Smaller problems are easier to program, test and maintain", "Sub-problems can be given to different teams or programmers with different expertise, or solved separately"]) + "</p>", "Labelling the module with the most parameters as the top of the chart. The module that \"repeatedly calls three of the modules\" is Head.") + peq(SRC("s22", "23", "Q3"), "2 + 5 marks", "Describe / Draw",
  "Four modules: PROCEDURE Sub1_A(XT : INTEGER, PB : STRING); FUNCTION Sub1_B(RA : INTEGER) RETURNS BOOLEAN; PROCEDURE Sub1_C(SB : INTEGER, BYREF SA : STRING); PROCEDURE Section_1(). (a) A structure chart is produced during development. Describe its purpose. (b) Section_1() calls one of the other three modules; the module called is selected when the program runs. Draw the structure chart.", "Hierarchy and parameters. Diamond for selection.",
  "<p><b>(a)</b> " + mks(["To show the module relationships or hierarchy, selection and repetition, or how a problem is broken down", "To show the parameters passed between the modules, or whether a module is a function or a procedure"], "a") + "</p><p><b>(b)</b> " + mks(["Four boxes linked as shown and correctly labelled (the order of the lower three is not important)", "Parameters to Sub1_A", "Parameter to Sub1_B and the return value", "Parameters to Sub1_C", "A selection diamond"]) + "</p>" + C_SEC, None) + peq(SRC("w25", "22", "Q7"), "2 + 4 marks", "Explain / Write",
  "A structure chart shows Convert at the top calling Analyse, Update and Sort, with a curved arrow under Convert. Count goes down to Analyse; Key goes down to Update and T1 comes back up; P2 is shown with an arrow head at both ends on the line to Sort. (a) Explain the meaning of the curved arrow. (b) Count is the number of elements in an array; T1 is the number of modified elements; Key is a STRING; P2 is a Boolean flag. Write the module headers for Analyse, Update and Sort.", "Repetition. Procedure, function, BYREF.",
  "<p>" + C_CONV + "</p><p><b>(a)</b> " + mks(["Reference to repetition", "Convert repeatedly calls Analyse, then Update, then Sort, in that order"], "a") + "</p><p><b>(b)</b> One mark per underlined part:</p>" + pc("PROCEDURE Analyse(Count : INTEGER)\nFUNCTION Update(Key : STRING) RETURNS INTEGER\nPROCEDURE Sort(BYREF P2 : BOOLEAN)"), "Writing PROCEDURE Update: T1 comes back up, so Update returns a value and is a function.") + peq(SRC("s25", "23", "Q6"), "1 + 5 + 3 marks", "Explain / Write",
  "A chart shows Main (diamond) calling Sub_A and Sub_B; Sub_A (curved arrow) calling Sub_Part1A, Sub_Part2A and Sub_Part3A; and Sub_B calling Sub_Part1B and Sub_Part2B. Parameters: R and V are INTEGER, T is REAL, U is STRING, W is BOOLEAN. R goes down to Sub_Part1A; T goes down and a Boolean flag comes up from Sub_Part2A; V and W (flag) go down and U has two heads at Sub_Part3A. (a) Explain one difference between functions and procedures. (b) Write the module headers for Sub_Part1A, Sub_Part2A and Sub_Part3A. (c) Explain the two symbols: the diamond and the curved arrow.", "A function returns a value. Two-headed is BYREF.",
  "<p>" + C_MAIN + "</p><p><b>(a)</b> " + mks(["A function returns a (single) value and a procedure does not", "A procedure can pass parameters by reference"], "a") + " (max 1)</p><p><b>(b)</b> " + mks(["PROCEDURE Sub_Part1A(R : INTEGER)", "FUNCTION Sub_Part2A(T : REAL) RETURNS BOOLEAN", "PROCEDURE Sub_Part3A(V : INTEGER, W : BOOLEAN, BYREF U : STRING)"]) + " (the second and third are worth two marks each, the first one)</p>" + pc("PROCEDURE Sub_Part1A(R : INTEGER)\nFUNCTION Sub_Part2A(T : REAL) RETURNS BOOLEAN\nPROCEDURE Sub_Part3A(V : INTEGER, W : BOOLEAN, BYREF U : STRING)") + "<p><b>(c)</b> " + mks(["The diamond shows selection: Main calls either Sub_A or Sub_B (which is decided at run time)", "The curved arrow shows repetition or iteration: Sub_A repeatedly calls Sub_Part1A followed by Sub_Part2A then Sub_Part3A", "Correct use of all module names in both parts"]) + "</p>", None) + peq(SRC("w23", "23", "Q7"), "2 + 3 + 2 marks", "Explain / Write",
  "A chart shows Module-A() at the top with a curved arrow, calling Sub-Y1(), Sub-Y2() and Sub-9() in that order; Sub-9() is a function. A Boolean is returned by Sub-9() to Module-A(); the original parameter RA is an integer and RB is a string. (a) Explain the meaning of the curved arrow. (b)(i) Write pseudocode to define a record type MyType with three fields for the values passed between the two modules. (ii) Sub-9() is changed to a procedure called with a single parameter of type MyType: write the header.", "Iteration. Record with RA, RB, RC. One BYREF parameter.",
  "<p><b>(a)</b> " + mks(["Iteration (looping)", "Module-A repeatedly calls Sub-Y1, then Sub-Y2, then Sub-9 (all four modules named in sequence)"], "a") + "</p><p><b>(b)(i)</b> " + mks(["TYPE MyType ... ENDTYPE", "RA as INTEGER and RB as STRING", "RC as BOOLEAN"]) + "</p>" + pc("TYPE MyType\n   DECLARE RA : INTEGER\n   DECLARE RB : STRING\n   DECLARE RC : BOOLEAN\nENDTYPE") + "<p><b>(ii)</b> " + mks(["BYREF", "the rest of the statement"], "b") + "</p>" + pc("PROCEDURE Sub-9(BYREF Param : MyType)"), "Making the new procedure BYVAL: it must send back the Boolean, so the record is passed by reference.")

review = req("4 marks", "Write", "Write the module headers: Show takes a STRING Name and an INTEGER Age and returns nothing; IsValid takes an INTEGER Number and returns a BOOLEAN.", "Procedure and function.", "<p>" + mks(["PROCEDURE Show(Name : STRING, Age : INTEGER)", "FUNCTION IsValid(Number : INTEGER) RETURNS BOOLEAN"], "a") + " (two marks each)</p>", None) + req("3 marks", "Describe", "Describe how selection and repetition are shown on a structure chart.", "Diamond and curve.", "<p>" + mks(["Selection: a diamond on the calling module; one of the lower modules is called", "Repetition: a curved arrow under the calling module", "The lower modules are called repeatedly, in order from left to right"]) + "</p>", None) + req("3 marks", "State", "State three things a structure chart shows.", "Hierarchy, parameters, type.", "<p>" + mks(["The modules and the hierarchy (which module calls which)", "The parameters passed between modules", "Whether a module is a function or a procedure"]) + "</p>", None) + req("3 marks", "Draw", "A module Menu() calls either Add() or Remove(). Add takes a STRING Item. Remove takes a STRING Item and returns a Boolean. Draw the structure chart.", "Diamond, down arrows, up arrow.", "<p>" + mks(["Three boxes, Menu above Add and Remove", "A diamond on Menu", "Item down to both modules, and a Boolean flag up from Remove"]) + "</p>", None) + req("3 marks", "Describe", "Describe three benefits of breaking a problem into modules.", "Easier, teams, testing.", "<p>" + mks(["Easier to understand and solve", "Easier to program, test and maintain", "Modules can be given to different programmers or teams"]) + "</p>", None)

tips = tips_html([
  ("Down passes in, up returns.", "An up arrow means a function."),
  ("Two heads: BYREF.", "In and out."),
  ("Diamond or curve.", "Diamond: choose one. Curve: repeat all in order."),
  ("Name every module.", "In the explanations and on the chart."),
  ("Types in headers.", "Add the data type for every parameter."),
  ("Left to right.", "The order of the lower modules is the order they are called."),
], [("a module", "A named block of code: a procedure or a function."), ("decomposition", "Breaking a problem into sub-problems."), ("a parameter", "A value passed into a module."), ("selection", "A choice between modules.")],
  [("Draw", "Draw the chart."), ("Write", "Write the headers."), ("Explain", "Give the meaning."), ("Describe", "Give the features or steps.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const B = (x, y, t, on) => SV.rect(x, y, 90, 26, on ? "f3" : "cell", { rx: 3 }) + SV.text(x + 45, y + 17, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); o += B(140, 6, "Head()", k === 0); if (k >= 1) { ["Mod_W", "Mod_X", "Mod_V"].forEach((t, i) => o += SV.line(185, 32, 40 + i * 140 + 45 - (i === 1 ? 0 : 0), 80, "w") + B(10 + i * 140, 80, t, k === 1)); } if (k >= 2) o += SV.text(14, 140, "arrows show the parameters", "lbl bd t3", { style: "font-size:11px" }); if (k >= 3) o += SV.text(14, 156, "curved arrow: Head repeats the calls", "lbl bd t2", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stA"), { w: 430, h: 170, label: "Chart", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The top module.", "The modules it calls, in order.", "Add the parameter arrows.", "Add selection or repetition."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(110, 6, 90, 26, "cell", { rx: 3 }) + SV.text(155, 23, "Menu()", "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); ["Add()", "Remove()", "Show()"].forEach((t, i) => { const hit = k === 1 ? i === 1 : k === 2 ? true : false; o += SV.line(155, 32, 45 + i * 110, 84, "w") + SV.rect(i * 110, 84, 90, 26, hit ? "f3" : "cell", { rx: 3 }) + SV.text(45 + i * 110, 101, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); o += SV.text(10, 136, k === 0 ? "Menu() calls one of three modules, or all three" : k === 1 ? "Diamond: this run calls only Remove()" : "Curved arrow: all three, in order, repeatedly", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 148, label: "Selection and repetition", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Menu() has three lower modules.", "Selection: only one is called.", "Repetition: all are called, in order, again and again."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const H = [["PROCEDURE Show(Name : STRING, Age : INTEGER)", "Two arrows down (Name, Age); none up."], ["FUNCTION IsValid(Number : INTEGER) RETURNS BOOLEAN", "One arrow down (Number); one arrow up with a filled circle (Boolean)."], ["PROCEDURE Sort(BYREF P2 : BOOLEAN)", "One arrow with a head at both ends and a filled circle."], ["FUNCTION Update(Key : STRING) RETURNS INTEGER", "Key down; an integer up."]];
  const bar = $("#hdB"); H.forEach((h) => { const b = document.createElement("button"); b.className = "mono"; b.textContent = h[0].split("(")[0]; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = "mono" + (x === b ? " on" : "")); $("#hdV").innerHTML = `<div class="verdict mono">${h[0]}</div><p>${h[1]}</p>`; }; bar.appendChild(b); });
})();
btnTable("syB", "syO", [
  ["Diamond on a calling module", "Selection", "one lower module is called"],
  ["Curved arrow under a calling module", "Repetition", "the lower modules are called repeatedly, left to right"],
  ["Arrow up from a module", "A returned value", "the lower module is a function"],
  ["Arrow with two heads", "BYREF", "the value is passed in and changed"],
  ["Filled circle on an arrow", "A flag", "a Boolean value"]
], ["Symbol", "Meaning", "Detail"]);
''' + _prjs

finish("as-12-2-1-structure-charts", "as1221", "Structure Charts",
  "Structure charts: modules, parameters, functions and procedures, selection and repetition, module headers from a chart and decomposition, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "12.2.1", "12 · Software development", "section 12.2 Program design", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on structure charts (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
