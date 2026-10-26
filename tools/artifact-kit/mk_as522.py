"""AS CS 5.2.2: Integrated Development Environments. Run: python3 tools/artifact-kit/mk_as522.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>Integrated Development Environment (IDE)</b> brings together the tools a programmer needs to write, translate, test and debug a program in one application. Its features fall into two groups. <b>Presentation and writing features</b> make the code easier to read and write: <b>colour coding</b> (syntax highlighting), <b>prettyprint</b> (automatic formatting), <b>auto-indentation</b>, <b>expand and collapse code blocks</b>, <b>auto-complete</b> and <b>context-sensitive prompts</b>, <b>auto-correct</b> and <b>dynamic syntax checks</b>. <b>Debugging features</b> help to find logic and run-time errors: <b>single stepping</b>, <b>breakpoints</b>, and the <b>report window</b> (variable watch window). A good answer names the feature and says what it does, linked to the situation.</p></div>

  <h2>1 · Presentation and writing features</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>What it does</th></tr>
    <tr><td><b>Colour coding</b> (syntax highlighting)</td><td>Shows keywords, variables, strings and comments in different colours so the structure is easy to see</td></tr>
    <tr><td><b>Prettyprint</b> (auto-formatting)</td><td>Automatically lays out the code in a standard style</td></tr>
    <tr><td><b>Auto-indentation</b></td><td>Indents code as the user types so the structure is clear and it is more readable</td></tr>
    <tr><td><b>Expand and collapse code blocks</b></td><td>Sections of code that belong to the same block can be expanded to see the content or collapsed so the overall structure is seen</td></tr>
    <tr><td><b>Auto-complete / context-sensitive prompts</b></td><td>As the code is being written, the options to complete the statement are shown or completed automatically</td></tr>
    <tr><td><b>Auto-correct</b></td><td>Fixes common mistakes as the code is typed</td></tr>
    <tr><td><b>Dynamic syntax checks</b></td><td>Highlights or underlines statements that do not meet the rules of the language as the code is entered</td></tr>
  </table></div>

  <h2>2 · Debugging features</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>What it does</th><th>How the programmer uses it</th></tr>
    <tr><td><b>Single stepping</b></td><td>Executes one line of the program and then stops</td><td>Runs the code one line at a time and checks the variable contents and program flow</td></tr>
    <tr><td><b>Breakpoint</b></td><td>Stops the program running at a set line</td><td>Runs the code up to a set line, then checks the status (values of variables) or tests a sub-section</td></tr>
    <tr><td><b>Report window / variable watch window</b></td><td>Shows the contents of variables and data structures</td><td>Views how and when the data changes as each line runs</td></tr>
  </table></div>
  <p>A <b>trace table</b> is the same idea on paper: it records the value of each variable after every line, and the watch window does it automatically.</p>

  <h2>3 · Choosing the feature</h2>
  <ul>
    <li>The program must <b>stop at a particular line</b> to check a value: a breakpoint (the technical term for the position at which the program stops).</li>
    <li>To <b>see the effect of each statement</b>: single stepping.</li>
    <li>To <b>see how a variable changes</b> over time: the report (watch) window.</li>
    <li>To make the code <b>easier to read</b>: prettyprint, colour coding, auto-indentation, expand/collapse.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Naming a debugging feature when the question asks for a presentation feature (or the other way round).</li>
    <li>Describing "debugging" as "check for errors". Say how: one line at a time, stop at a line, view variables.</li>
    <li>Describing single stepping and a breakpoint in the same way. Stepping runs one line then stops; a breakpoint stops at a set line.</li>
    <li>Describing colour coding as "making the code look nice". Say it shows keywords and structure so the code is easier to read.</li>
    <li>Describing the feature without saying how the student uses it when the question asks how they can use it.</li>
  </ul>
'''

watch = '''
  <h2>1 · Single stepping and the watch window</h2>
  <div id="stA"></div>
  <h2>2 · A breakpoint</h2>
  <div id="stB"></div>
  <h2>3 · Dynamic syntax check and auto-complete</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · A debugger</h2>
  <p>Click a line number to toggle a breakpoint, then Run to breakpoint, or Step one line at a time. The report window shows the variables.</p>
  <div class="card"><div class="btnrow"><button id="db_step">Step</button><button id="db_run">Run to breakpoint</button><button id="db_reset">Reset</button></div><div id="dbP"></div><div id="dbW"></div><div id="dbV" class="verdict"></div></div>
  <h2>Lab 2 · Which IDE feature?</h2>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>
  <h2>Lab 3 · Presentation or debugging?</h2>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div></div>
'''

_pr, _prjs = PR(["Presentation or debugging feature?", "Single stepping or breakpoint?", "Match the feature to its description", "Put the debugging steps in order", "Working out", "Multiple choice"],
  ("Presentation feature or debugging feature?", ["Presentation", "Debugging"], [("Prettyprint", 0), ("Single stepping", 1), ("Expand and collapse code blocks", 0), ("Breakpoints", 1), ("Auto-indentation", 0), ("Report (variable watch) window", 1)], "Presentation: how the code looks. Debugging: finding errors."),
  ("Single stepping or breakpoint?", ["Single stepping", "Breakpoint"], [("Executes one line and then stops", 0), ("Stops the code at a set line", 1), ("Used to check a value at a particular statement", 1), ("Used to see the effect of every statement", 0), ("The technical term for the position at which the program stops", 1), ("The program waits for the next click after each line", 0)], "Stepping: one line. Breakpoint: a chosen line."),
  [["Context-sensitive prompt", "Displays predictions of the code being entered"], ["Dynamic syntax check", "Underlines or highlights statements that break the rules of the language"], ["Breakpoint", "Stops the code executing at a set line"], ["Single stepping", "Executes one line of the program and then stops"], ["Report window", "Outputs the contents of variables and data structures"]],
  ("Put the debugging steps in order.", ["Set a breakpoint at the line before the suspected error", "Run the program: it stops at the breakpoint", "Check the variables in the report window", "Single step through the next lines", "Spot where a variable first holds a wrong value"], "Breakpoint, run, check, step, spot."),
  [{"q": "A program has 120 lines and a breakpoint on line 80. How many lines run before it stops (lines 1 to 79)?", "a": 79, "unit": "", "tol": 0.01, "hint": "Up to the line before.", "sol": "<b>79</b>."}, {"q": "A loop runs 8 times with 3 lines in the body. How many single steps to run the loop body completely?", "a": 24, "unit": "", "tol": 0.01, "hint": "8 × 3.", "sol": "<b>24</b>."}, {"q": "total starts at 0 and adds 4 each loop. What is total after 5 loops?", "a": 20, "unit": "", "tol": 0.01, "hint": "5 × 4.", "sol": "<b>20</b>."}, {"q": "How many presentation features are in the Learn tab table (colour coding, prettyprint, auto-indentation, expand/collapse, auto-complete, auto-correct, dynamic syntax checks)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count the rows.", "sol": "<b>7</b>."}, {"q": "A student sets 2 breakpoints. The program stops at both in turn. How many times must they press Run to reach the end of the program (after the last breakpoint)?", "a": 3, "unit": "", "tol": 0.01, "hint": "To the 1st, the 2nd, then the end.", "sol": "<b>3</b>."}],
  [("A breakpoint:", ["Stops the program at a set line", "Runs one line", "Formats code", "Compiles"], 0, "Stops at a set line."), ("Single stepping:", ["Runs one line then stops", "Runs to the end", "Highlights errors", "Indents code"], 0, "One line."), ("Prettyprint is a:", ["Presentation feature", "Debugging feature", "Translator", "Utility"], 0, "Presentation."), ("The report window shows:", ["The contents of variables", "The source code colours", "The compiler output only", "The file size"], 0, "Variables."), ("Dynamic syntax checking:", ["Highlights errors as you type", "Runs the program", "Compresses code", "Creates a back-up"], 0, "As you type."), ("An IDE is:", ["An application with tools to write and test programs", "A type of RAM", "An assembler only", "A file format"], 0, "Tools together.")],
  [("IDE", "Tools to write, translate, test and debug."), ("Presentation", "Colour, prettyprint, indentation, collapse."), ("Context-sensitive prompt", "Shows predictions as you type."), ("Dynamic syntax check", "Underlines errors as you type."), ("Single stepping", "One line then stop."), ("Breakpoint", "Stops at a set line."), ("Report window", "Shows variable values."), ("Debugging", "Finding and fixing errors.")])

real = RWNOTE + (
rw("A red squiggle under code", "The editor checks the syntax as you type, so you fix a missing bracket before you run anything.", "dynamic syntax check.") +
rw("Finding why a total is wrong", "Set a breakpoint, run to it, then step one line at a time and watch the total change until it goes wrong.", "breakpoint, single stepping, watch window.") +
rw("Reading someone else's code", "Colour coding and collapsing the functions you do not need makes a long program much easier to follow.", "presentation features.") +
rw("Typing a function name", "The editor suggests the rest of the name and its parameters, so you make fewer typing mistakes.", "auto-complete and context-sensitive prompts.") +
rw("A team agreeing a style", "Prettyprint formats everyone's code the same way, so it is easy to read each other's work.", "prettyprint.")
)

where = [
  ("M/J 2021", "11, 13", "4(b)(ii)", "3", "Three IDE features that support writing the program"),
  ("M/J 2022", "11", "5(a)", "4", "Match four IDE features to their descriptions"),
  ("M/J 2022", "22", "1(a)", "1", "The technical term for the position at which the program stops (Paper 2)"),
  ("O/N 2023", "11", "6(c)", "2 + 2", "Two presentation features and two debugging features"),
  ("O/N 2023", "13", "5(a)", "4", "Describe context-sensitive prompts and single stepping"),
  ("M/J 2023", "12", "7(c)", "4", "Describe breakpoints, dynamic syntax checks, context-sensitive prompts and single stepping"),
  ("O/N 2024", "11", "4(d)", "2 + 2", "Another presentation feature and another debugging feature"),
  ("O/N 2024", "12", "4(a)", "4", "How the programmers can use the debugging features"),
  ("O/N 2025", "11", "5(c)", "2", "Two presentation features"),
  ("M/J 2026", "12", "7(b)(i)", "4", "How the student can use the debugging tools")]

past = '''  <p class="note">The IDE features come up almost every series, as a list of features to name, to describe or to match. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The "how can the programmer use" version needs the feature and how it is used.</p>
''' + peq(SRC("w21", "11/13", "Q4(b)(ii)"), "3 marks", "Identify",
  "A typical IDE provides debugging tools to support testing. Identify three other tools or features found in a typical IDE to support the writing of the program.", "Presentation and writing features.",
  "<p>" + mks(["Colour coding or prettyprint", "Auto-complete", "Auto-correct", "Context-sensitive prompts", "Expand and collapse code blocks"]) + " (any three)</p>", None) + peq(SRC("s22", "11", "Q5(a)"), "4 marks", "Match",
  "Draw one line from each IDE feature to its correct description. Features: context-sensitive prompt, dynamic syntax check, breakpoint, single stepping, report window. Descriptions: executes one line of the program and then stops; underlines or highlights statements that do not meet the rules of the language; outputs the contents of variables and data structures; stops the code executing at a set line; displays predictions of the code being entered.", "One mark for 1 correct line, 2 for 2 lines, 3 for 3 or 4 lines, 4 for all five.",
  "<p>" + mks(["Context-sensitive prompt: displays predictions of the code being entered", "Dynamic syntax check: underlines or highlights statements that do not meet the rules of the language", "Breakpoint: stops the code executing at a set line", "Single stepping: executes one line of the program and then stops", "Report window: outputs the contents of variables and data structures"]) + "</p>", "Swapping single stepping and breakpoint. One stops after every line; the other at a chosen line.") + peq(SRC("s22", "22", "Q1(a)"), "1 mark", "Give",
  "A programmer is testing a program using an IDE. The programmer wants the program to stop when it reaches a specific instruction or program statement in order to check the value assigned to a variable. Give the technical term for the position at which the program stops.", "Breakpoint.",
  "<p>" + mks(["Breakpoint"]) + " (correct answer only)</p>", None) + peq(SRC("w23", "11", "Q6(c)"), "2 + 2 marks", "Identify",
  "(i) Identify two features that support the visual presentation of the code in a typical IDE. (ii) Identify two features that support the debugging of the code in a typical IDE.", "Prettyprint, collapse, indentation. Single stepping, breakpoints, report window.",
  "<p><b>(i)</b> " + mks(["Prettyprint", "Expand or collapse code blocks", "Auto indentation or formatting"]) + " (any two)</p><p><b>(ii)</b> " + mks(["Single stepping", "Breakpoints", "Report window", "Variable expressions"], "a") + " (any two)</p>", None) + peq(SRC("w23", "13", "Q5(a)"), "4 marks", "Describe",
  "A programmer uses an IDE to develop a program that monitors air quality. Describe the following features of a typical IDE: context-sensitive prompts; single stepping.", "Options shown as the code is written. One line at a time.",
  "<p>" + mks(["Context-sensitive prompts: as the code is being written", "the options to complete the statement are shown", "Single stepping: allows the programmer to execute the program one line at a time", "so that the effects of each statement can be seen"]) + "</p>", None) + peq(SRC("s23", "12", "Q7(c)"), "4 marks", "Describe",
  "Complete the table by describing the typical features found in an IDE: breakpoints; dynamic syntax checks; context-sensitive prompts; single stepping.", "One description each.",
  "<p>" + mks(["Breakpoints: stop the code at a specific line to check the current progress or values", "Dynamic syntax checks: highlight, underline or colour syntax errors as the code is entered", "Context-sensitive prompts: suggest the code to add, or automatically complete statements", "Single stepping: run the code one line at a time so the values can be checked"]) + "</p>", None) + peq(SRC("w24", "11", "Q4(d)"), "2 + 2 marks", "Identify / Describe",
  "(i) One presentation feature found in a typical IDE is prettyprint. Identify and describe one other presentation feature. (ii) One debugging feature is single stepping. Identify and describe one other debugging feature.", "Expand/collapse or auto-indentation. Breakpoints or report window.",
  "<p><b>(i)</b> " + mks(["Expand or collapse code blocks: sections of source code that are part of the same block can be expanded to see the content or collapsed to see the overall code", "Auto-indentation or auto-formatting: automatically indents or formats code as the user types so the structure is clear and readable"]) + " (name and description)</p><p><b>(ii)</b> " + mks(["Breakpoints: stop the code running on a set line to view the current status, variable contents or program flow", "Report window or variable watch window: shows the values in variables and data structures and how they change when each line is run"], "a") + " (name and description)</p>", None) + peq(SRC("w24", "12", "Q4(a)"), "4 marks", "Describe",
  "A program is written by a team using an IDE. Describe how the programmers can use the debugging features of a typical IDE during the development of the program.", "Single stepping, breakpoints, watch window, each with use.",
  "<p>Any four: " + mks(["Single stepping: run the program one line at a time", "and check the variable contents or program flow, or show the effect of each line of code", "Set breakpoints: run the code up to a set line", "and then check the status", "Variable or report watch window: view how the data changes as the program is running"]) + "</p>", "Describing what a feature is without how the programmers use it during development.") + peq(SRC("w25", "11", "Q5(c)"), "2 marks", "Identify",
  "Identify two presentation features found in a typical IDE.", "Prettyprint, collapse, auto-indent.",
  "<p>" + mks(["Prettyprint", "Expanding and collapsing code blocks", "Automatic or smart indentation or formatting"]) + " (any two)</p>", None) + peq(SRC("s26", "12", "Q7(b)(i)"), "4 marks", "Explain",
  "The student uses an IDE. Explain how the student can use the debugging tools to find errors in their program.", "Stepping, breakpoints, watch window, each with how they are used.",
  "<p>Mark in pairs, max 4: " + mks(["(Single) stepping: the student runs one line of code at a time and looks at the output, results or flow before moving on", "Breakpoints: inserted in the code to stop the code at a specific point so the student can check the flow or values, or test sub-sections of the code", "(Variable) watch window: the student can view how and when the variables change during execution"]) + "</p>", "Naming the tools with no use. Two marks maximum for names only.")

review = req("2 marks", "Describe", "Describe how a student can use a breakpoint to find why a variable has the wrong value.", "Stop at a line; check.", "<p>" + mks(["Set a breakpoint on the line where the value is first used", "Run the program to the breakpoint and check the value of the variable in the watch window"]) + "</p>", None) + req("2 marks", "Identify", "Identify two features that help a programmer see the structure of a long program.", "Colour, collapse.", "<p>" + mks(["Expand and collapse code blocks", "Colour coding, prettyprint or auto-indentation"]) + "</p>", None) + req("2 marks", "Explain", "Explain the difference between single stepping and a breakpoint.", "One line against a chosen line.", "<p>" + mks(["Single stepping runs one line and then stops each time", "A breakpoint stops the program at a chosen line, and the code in between runs normally"]) + "</p>", None) + req("2 marks", "Describe", "Describe what a dynamic syntax check does.", "As the code is typed.", "<p>" + mks(["It checks the code as it is entered", "and highlights or underlines statements that break the rules of the language"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a report window is useful when testing a loop.", "See values change.", "<p>" + mks(["It shows the values of the variables", "and how they change on each pass of the loop"]) + "</p>", None)

tips = tips_html([
  ("Name it, then what it does.", "Two marks for each feature."),
  ("Presentation or debugging?", "Check which the question wants."),
  ("Stepping: one line.", "Breakpoint: a set line."),
  ("Report window: variables.", "Shows how they change."),
  ("'How can the programmer use it?'", "Say what the programmer does with it."),
  ("Dynamic: as you type.", "Syntax checks and prompts."),
], [("an IDE", "An application bringing together tools for writing and testing programs."), ("prettyprint", "Automatic formatting of code."), ("a breakpoint", "A set line at which the program stops."), ("single stepping", "Running one line at a time.")],
  [("Identify", "Name the feature."), ("Describe", "What it does."), ("Explain", "How it is used."), ("Match", "Link each feature to its description.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const lines = ["total ← 0", "FOR n ← 1 TO 3", "  total ← total + n", "NEXT n", "OUTPUT total"]; const draw = (s) => { const k = Math.round(s.i); const st = [[0, "-"], [1, "n=1"], [2, "total=1"], [1, "n=2"], [2, "total=3"]][k]; let o = ""; lines.forEach((l, i) => { o += SV.rect(20, 14 + i * 28, 260, 24, i === st[0] ? "f3" : "cell", { rx: 4 }) + SV.text(30, 31 + i * 28, (i + 1) + "  " + l, "lbl"); });
    o += SV.rect(320, 14, 200, 80, "cell", { rx: 6 }) + SV.text(330, 34, "watch window", "sm") + SV.text(330, 58, "total = " + [0, 0, 1, 1, 3][k], "lbl bd") + SV.text(330, 80, "n = " + ["?", 1, 1, 2, 2][k], "lbl bd"); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 165, label: "Single stepping", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Single stepping: line 1 runs, total = 0.", "Line 2: n becomes 1.", "Line 3: total = 0 + 1 = 1.", "Back to the loop: n = 2.", "Line 3 again: total = 1 + 2 = 3."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const lines = ["a ← 5", "b ← 0", "FOR i ← 1 TO 4", "  b ← b + a", "NEXT i", "OUTPUT b"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; lines.forEach((l, i) => { o += SV.circle(26, 26 + i * 28, 7, i === 3 ? "f2" : "cell") + SV.rect(44, 14 + i * 28, 240, 24, k >= 1 && i === 3 ? "f3" : "cell", { rx: 4 }) + SV.text(54, 31 + i * 28, (i + 1) + "  " + l, "lbl"); });
    o += SV.text(310, 40, ["breakpoint set on line 4", "lines 1-3 run normally", "it stops: check b and i"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 180, label: "Breakpoint", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Set a <b>breakpoint</b> on line 4.", "Run: lines 1 to 3 execute normally.", "The program <b>stops at the breakpoint</b>; the programmer checks the variables."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 20, 330, 30, k === 3 ? "f1" : "cell", { rx: 4 }) + SV.text(30, 40, ["IF a > 5 THEN", "IF a > 5 THE", "pri", "print("][k], "lbl") + (k === 1 ? SV.path("M30,44 H110", "ax", { style: "stroke:var(--bad);stroke-width:3" }) + SV.text(370, 40, "syntax error underlined", "lbl bd t3", { style: "font-size:12px" }) : "") + (k === 2 ? SV.rect(30, 52, 180, 56, "f3", { rx: 4 }) + SV.text(40, 72, "print", "lbl") + SV.text(40, 92, "printf", "lbl") + SV.text(40, 108, "", "sm") : "");
    o += SV.text(20, 135, ["", "Dynamic syntax check: the error is highlighted as you type", "Context-sensitive prompt: options are shown", "Auto-complete finishes the statement"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 150, label: "Typing", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A statement is typed.", "A <b>dynamic syntax check</b> underlines the mistake straight away.", "A <b>context-sensitive prompt</b> predicts what is being entered.", "<b>Auto-complete</b> finishes it."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const lines = ["total ← 0", "FOR n ← 1 TO 3", "  total ← total + n", "NEXT n", "OUTPUT total"];
  // pre-computed execution: [line index, total, n, output]
  const run = [[0, 0, "?", ""], [1, 0, 1, ""], [2, 1, 1, ""], [3, 1, 1, ""], [1, 1, 2, ""], [2, 3, 2, ""], [3, 3, 2, ""], [1, 3, 3, ""], [2, 6, 3, ""], [3, 6, 3, ""], [4, 6, 3, "6"]]; let k = -1, bp = new Set();
  const paint = () => { const cur = k >= 0 ? run[k] : null;
    $("#dbP").innerHTML = '<div class="tw"><table class="t mono">' + lines.map((l, i) => `<tr style="${cur && cur[0] === i ? "background:var(--accent-soft);font-weight:700" : ""}"><td><button data-ln="${i}" style="min-width:34px">${bp.has(i) ? "●" : (i + 1)}</button></td><td>${l}</td></tr>`).join("") + "</table></div>";
    $("#dbP").querySelectorAll("button").forEach((b) => b.onclick = () => { const i = +b.dataset.ln; bp.has(i) ? bp.delete(i) : bp.add(i); paint(); });
    $("#dbW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>total</th><th>n</th><th>output</th></tr><tr>' + (cur ? `<td>${cur[1]}</td><td>${cur[2]}</td><td>${cur[3]}</td>` : "<td>·</td><td>·</td><td>·</td>") + "</tr></table></div>";
    $("#dbV").innerHTML = k < 0 ? "Press Step or Run to breakpoint." : k >= run.length - 1 ? "The program has finished and printed 6." : `Stopped on line ${cur[0] + 1}. The report window shows total = ${cur[1]} and n = ${cur[2]}.`; };
  $("#db_step").onclick = () => { if (k < run.length - 1) { k++; paint(); } };
  $("#db_run").onclick = () => { do { k++; } while (k < run.length - 1 && !bp.has(run[k][0])); if (k >= run.length) k = run.length - 1; paint(); };
  $("#db_reset").onclick = () => { k = -1; paint(); }; bp.add(2); paint();
})();
btnTable("fB", "fO", [
  ["Run the program one line at a time", "Single stepping", "Debugging"],
  ["Stop at line 40 to look at a variable", "Breakpoint", "Debugging"],
  ["Show the values of variables as they change", "Report (watch) window", "Debugging"],
  ["Underline a mistake as you type", "Dynamic syntax check", "Presentation / writing"],
  ["Suggest the rest of a statement", "Context-sensitive prompt", "Presentation / writing"],
  ["Hide the body of a long function", "Collapse code block", "Presentation"]
], ["Need", "Feature", "Type"]);
btnTable("pB", "pO", [
  ["Prettyprint", "Presentation", "Formats the code"],
  ["Breakpoint", "Debugging", "Stops at a set line"],
  ["Colour coding", "Presentation", "Shows keywords and structure"],
  ["Single stepping", "Debugging", "One line at a time"],
  ["Auto-indentation", "Presentation", "Shows the structure"],
  ["Variable watch window", "Debugging", "Shows values change"]
], ["Feature", "Type", "Why"]);
''' + _prjs

finish("as-5-2-2-ide-features", "as522", "IDE Features: Presentation and Debugging",
  "The presentation and debugging features of an Integrated Development Environment, with a debugger simulator, labs and the real Paper 1 questions from 2021 to 2026.",
  "5.2.2", "5 · System software", "section 5.2 Language translators", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on IDE features (Papers 1 and 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
