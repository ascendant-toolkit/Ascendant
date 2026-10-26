"""AS CS 5.2.1: language translators: assembler, compiler, interpreter. Run: python3 tools/artifact-kit/mk_as521.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>language translator</b> converts a program written in one language into machine code that the processor can run. An <b>assembler</b> translates assembly language into machine code. A <b>compiler</b> translates the <b>whole</b> high-level program in one go, reporting all errors together, and if there are none it produces an <b>executable file</b> (object code) that runs without the source code. An <b>interpreter</b> translates and runs the program <b>one line at a time</b>, stopping at the first error so the programmer can correct it immediately and carry on. Interpreters are better during <b>development</b> (easier to debug, can test unfinished programs); compilers are better for the <b>finished</b> program (fast to run, source code stays private). Some languages are <b>partially compiled and partially interpreted</b>: the source is compiled to an intermediate code and interpreted at run time.</p></div>

  <h2>1 · Compiler and interpreter compared</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Compiler</th><th>Interpreter</th></tr>
    <tr><td>Translates</td><td>All the code at the same time, then the program is run</td><td>One line at a time, then runs that line</td></tr>
    <tr><td>Output</td><td>An executable (object code) file that can run without the source code</td><td>No executable file: the source code is needed every time the program runs</td></tr>
    <tr><td>Errors</td><td>Checks all the code first and reports all errors together; the program does not run if there are errors; one error can cause false extra errors</td><td>Stops at the first error and displays it; the error can be corrected immediately (in real time) and translation continues from that line</td></tr>
    <tr><td>Best for</td><td>The finished program (it runs faster, and the source code is not distributed)</td><td>Development: debugging line by line, testing unfinished code or small sections</td></tr>
  </table></div>

  <h2>2 · Drawbacks of a compiler during development</h2>
  <ul>
    <li>Large amounts of source code take time to compile; it can be slower to produce the object code than an interpreter.</li>
    <li>The code must be <b>recompiled</b> whenever it is changed.</li>
    <li>The program cannot run if there are any errors, and errors cannot be corrected in real time.</li>
    <li>One error can cause false reporting of other errors.</li>
    <li>Sections of code or unfinished code cannot easily be tested.</li>
  </ul>

  <h2>3 · Advantages of an interpreter</h2>
  <ul>
    <li>Easier to debug: it translates line by line and stops when an error is found, reporting one error at a time.</li>
    <li>The error can be corrected in real time and the program restarts from the same point.</li>
    <li>The effect of changes can be seen immediately, and a partially completed program can be translated and tested.</li>
  </ul>

  <h2>4 · Partially compiled and partially interpreted languages</h2>
  <p>Some languages compile the source into an <b>intermediate code</b> that is then interpreted when the program runs. Reasons: the compiled program can be <b>used on different platforms</b> because it is interpreted at run time; the machine code is <b>optimised for the CPU</b> at run time; and the source code does not need recompiling for each machine, so it is efficient to run.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying a compiler "translates line by line". That is the interpreter.</li>
    <li>Writing that an assembler translates "high-level language". It translates assembly language into machine code.</li>
    <li>Saying interpreted programs "run faster". Compiled programs usually run faster.</li>
    <li>Describing the advantage of an interpreter with no development context, such as "it is easier". Say it stops at the first error so it can be corrected in real time.</li>
    <li>Forgetting that the compiler produces an executable file that runs without the source code.</li>
  </ul>
'''

watch = '''
  <h2>1 · A compiler translates everything first</h2>
  <div id="stA"></div>
  <h2>2 · An interpreter works line by line</h2>
  <div id="stB"></div>
  <h2>3 · Partially compiled, partially interpreted</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Compile or interpret?</h2>
  <p>A five-line program has errors in lines 2 and 4. See what each translator reports.</p>
  <div class="card"><div class="btnrow"><button id="tl_c">Compiler</button><button id="tl_i">Interpreter</button><button id="tl_f">Fix line 2</button><button id="tl_r">Reset</button></div><div id="tlP"></div><div id="tlV" class="verdict"></div></div>
  <h2>Lab 2 · Which translator?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
  <h2>Lab 3 · Compile once, run often</h2>
  <div class="card"><div id="rS"></div><div id="rV" class="verdict"></div></div>
'''

_pr, _prjs = PR(["Compiler or interpreter?", "Which translator is needed?", "Match the translator to its job", "Put the compiler steps in order", "Working out", "Multiple choice"],
  ("Compiler or interpreter?", ["Compiler", "Interpreter"], [("Translates all the code at the same time", 0), ("Translates one line then runs it", 1), ("Produces an executable file", 0), ("Stops at the first error", 1), ("Reports all errors together", 0), ("Needs the source code every time the program runs", 1)], "Compiler: whole program, executable. Interpreter: line by line."),
  ("Which translator does the situation need?", ["Compiler", "Interpreter", "Assembler"], [("Translate assembly code into machine code", 2), ("A finished program to be sold without its source code", 0), ("Testing a half-finished program one section at a time", 1), ("Correcting errors in real time while developing", 1), ("A program that must run quickly on many machines", 0), ("Converting mnemonics such as LDD and ADD into binary", 2)], "Assembler: assembly. Interpreter: development. Compiler: finished."),
  [["Compiler", "Translates the whole program and makes an executable"], ["Interpreter", "Translates and runs one line at a time"], ["Assembler", "Translates assembly language into machine code"], ["Executable file", "Machine code that runs without the source code"], ["Source code", "The program as the programmer wrote it"]],
  ("Put the compiler stages in order.", ["The whole source code is read", "All the code is checked for errors", "Any errors are reported together", "If no errors, an executable file is produced", "The executable runs without the source code"], "Read, check, report, produce, run."),
  [{"q": "A program of 600 lines has an error on line 150. An interpreter runs line by line. How many lines does it execute before it stops (lines 1 to 149)?", "a": 149, "unit": "", "tol": 0.01, "hint": "Up to the line before the error.", "sol": "<b>149</b>."}, {"q": "A compile takes 40 s. You change the code 12 times and recompile each time. Total compile time in minutes?", "a": 8, "unit": "min", "tol": 0.01, "hint": "12 × 40 s = 480 s.", "sol": "<b>8</b> min."}, {"q": "A program of 600 lines has no errors. How many lines does the compiler translate before it produces the executable?", "a": 600, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>600</b>."}, {"q": "A compiler lists 5 errors, but 3 are false errors caused by one real error. How many real errors?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."}, {"q": "A program of 100 lines contains errors at line 20 and line 60. How many errors does an interpreter report on the first run?", "a": 1, "unit": "", "tol": 0.01, "hint": "It stops at the first.", "sol": "<b>1</b>."}],
  [("A compiler produces:", ["An executable file", "No output", "Only error messages", "Assembly code"], 0, "Executable."), ("An interpreter:", ["Translates line by line", "Translates all at once", "Makes an exe", "Is used only for assembly"], 0, "Line by line."), ("An assembler translates:", ["Assembly language", "Python", "A website", "Machine code into text"], 0, "Assembly."), ("During development an interpreter is useful because:", ["It stops at the first error and can be fixed immediately", "It makes the exe fast", "It hides the source code", "It needs no source code"], 0, "Real-time correction."), ("A drawback of a compiler:", ["Must recompile after every change", "Can run partial code", "Reports one error only", "Is line by line"], 0, "Recompile."), ("Partial compilation helps programs:", ["Run on different platforms", "Avoid any translator", "Use no CPU", "Skip testing"], 0, "Different platforms.")],
  [("Translator", "Converts a program into machine code."), ("Assembler", "Assembly language to machine code."), ("Compiler", "Whole program; all errors; executable."), ("Interpreter", "Line by line; stops at first error."), ("Executable", "Runs without the source code."), ("Development", "Interpreter: debug line by line."), ("Finished program", "Compiler: runs faster, source hidden."), ("Partial compile", "Intermediate code interpreted; platform independent.")])

real = RWNOTE + (
rw("An app downloaded from a store", "The app is compiled: you get an executable and cannot see or run the source code.", "compiled programs run without the source.") +
rw("Learning to program in a notebook", "Python runs each line as you type, so you can run half a program and fix a mistake immediately.", "interpreter, good for development.") +
rw("A website's JavaScript", "The browser interprets the code line by line on your machine, so the same page works on any device.", "interpreted at run time.") +
rw("Java programs", "Java is compiled to an intermediate code that a runtime then runs on any platform: partially compiled and partially interpreted.", "platform independence.") +
rw("Writing assembly for a tiny chip", "An assembler turns each mnemonic into one machine instruction for that chip.", "assembler.")
)

where = [
  ("O/N 2021", "11, 13", "4(d)", "4", "Complete the descriptions of compilers, interpreters and assemblers"),
  ("O/N 2022", "12", "1(b)", "2 + 2", "Two drawbacks of a compiler during development; why programs may be partially compiled and partially interpreted"),
  ("O/N 2023", "11", "6(a), (b)", "4 + 1", "The advantages of an interpreter compared with a compiler; why some languages are partially compiled"),
  ("M/J 2023", "12", "7(b)", "3", "An interpreter or a compiler while writing the program, with justification"),
  ("M/J 2025", "13", "3(a)", "4", "Complete the description of compilers and interpreters"),
  ("O/N 2025", "13", "8(a)", "2", "Two disadvantages of a compiler compared with an interpreter"),
  ("M/J 2026", "12", "7(b)(ii)", "2", "Why a language is partially compiled and partially interpreted")]

past = '''  <p class="note">The compiler against interpreter comparison is the most repeated question in this section: the same list of points is used every series. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "11/13", "Q4(d)"), "4 marks", "Complete",
  "Francis's team use language translators. Complete the descriptions by writing the missing words. ... are usually used when a high-level language program is complete. They translate all the code at the same time and then run the program. They produce ... files that can be run without the source code. ... translate one line of a high-level language program at a time, and then run that line. They are most useful while developing the programs because errors can be corrected and then the program continues from that line. Assemblers are used to translate assembly code into ... .", "Compilers, executable, interpreters, machine code.",
  "<p>" + mks(["Compilers", "executable (.exe or object code)", "Interpreters", "binary or machine code"]) + "</p>", None) + peq(SRC("w22", "12", "Q1(b)"), "2 + 2 marks", "State / Explain",
  "(i) State two drawbacks of using a compiler compared to an interpreter during program development. (ii) Explain why high-level language programs might be partially compiled and partially interpreted.", "Large code takes time; recompile; will not run with errors; cannot correct in real time. Platforms; optimised for the CPU.",
  "<p><b>(i)</b> Any two: " + mks(["Larger amounts of source code take time to compile", "It is slower to produce the object code than an interpreter", "The code cannot be changed without recompilation", "The program will not run if there are any errors", "Errors cannot be corrected in real time", "One error may result in other false errors being reported", "Specific sections or unfinished code cannot easily be tested"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Partially compiled programs can be used on different platforms as they are interpreted when run", "The code is optimised for the CPU as machine code is generated at run time"], "a") + "</p>", None) + peq(SRC("w23", "11", "Q6(a)(b)"), "4 + 1 marks", "Describe / State",
  "A programmer uses both a compiler and an interpreter to translate a program. (a) Describe the advantages of using the interpreter compared to the compiler. (b) State one reason why some high-level languages are partially compiled and partially interpreted.", "Easier to debug, line by line, real time, partial programs.",
  "<p><b>(a)</b> Any four: " + mks(["It is easier to debug the program", "because it translates line by line and stops when an error is found, whereas the compiler translates all the program at the same time", "only reporting one error at a time", "which allows the error to be corrected in real time, whereas with a compiler the program needs to be corrected and recompiled", "the program can restart at the same point where the error occurred", "The effect of any changes can be seen immediately", "A partially completed program can be translated and tested on its own; a compiler cannot translate a partial program"]) + "</p><p><b>(b)</b> One: " + mks(["Partially compiled programs can be used on different platforms as they are interpreted when run", "The code is optimised for the CPU as machine code is generated at run time", "The source code does not need recompiling so it is more efficient to run"], "a") + "</p>", None) + peq(SRC("s23", "12", "Q7(b)"), "3 marks", "Identify / Justify",
  "The development team needs to use a translator whilst writing the program. Identify whether an interpreter or a compiler would be more appropriate at this stage of the program development. Justify your choice.", "No mark for the choice. Interpreter: real-time changes, test incomplete code.",
  "<p>No mark for the choice. Interpreter, any three: " + mks(["Allows the developer to make real-time changes so the program can be debugged at each stage", "The effect of any changes can be seen immediately", "The developer can test when the program is incomplete, so small parts can be tested without having to test the rest", "To avoid dependent errors"]) + "</p><p>Compiler, any three (also accepted): " + mks(["The developer can debug multiple errors simultaneously", "It produces an executable file so the developer can test the program multiple times without recompiling"], "a") + "</p>", None) + peq(SRC("s25", "13", "Q3(a)"), "4 marks", "Complete",
  "A compiler checks all the code before attempting to translate. If any errors are found, they are all reported at the same time and the program does not translate or run. If there are no errors, the compiler produces ... which can run without access to the ... . An interpreter translates one line of code and then runs it. If the line has an error, the interpreter ... and displays the error. The programmer can correct the error ... and then the interpreter continues translating from that point.", "Executable, source code, stops, immediately.",
  "<p>" + mks(["an executable file (.exe)", "source or program code", "stops", "immediately or in real time"]) + "</p>", None) + peq(SRC("w25", "13", "Q8(a)"), "2 marks", "State",
  "State two disadvantages of using a compiler compared to an interpreter during program development.", "Compile time, recompile, errors.",
  "<p>Any two: " + mks(["Large amounts of source code take time to compile", "It can be slower to produce the object code than an interpreter", "The code must be recompiled when it is changed", "The program cannot run if there are errors", "It is not possible to correct errors in real time", "One error can cause false reporting of multiple further errors", "Sections of code or unfinished code cannot easily be tested"]) + "</p>", None) + peq(SRC("s26", "12", "Q7(b)(ii)"), "2 marks", "Explain",
  "Explain why a high-level language program might be partially compiled and partially interpreted.", "Platforms; CPU optimisation; no recompiling.",
  "<p>Any two: " + mks(["Partially compiled programs can be used on different platforms as they are interpreted when run", "The code is optimised for the CPU as machine code is generated at run time", "It is more efficient to run as the source code does not need recompiling"]) + "</p>", "Stating the fact without the 'why'. Each point needs a reason.")

review = req("2 marks", "State", "State two differences between a compiler and an interpreter.", "Whole program or line.", "<p>" + mks(["A compiler translates all the code at once; an interpreter translates one line at a time", "A compiler produces an executable file; an interpreter does not"]) + "</p>", None) + req("3 marks", "Explain", "Explain why a company ships its finished product as a compiled executable.", "Speed, source hidden.", "<p>" + mks(["The executable runs without the source code", "so the source code is kept private", "and compiled programs usually run faster"]) + "</p>", None) + req("2 marks", "Explain", "Explain why an interpreter is helpful for a student writing their first program.", "Stops at first error.", "<p>" + mks(["It stops at the first error and displays it", "so the error can be corrected immediately and the program continues"]) + "</p>", None) + req("1 mark", "State", "State what an assembler does.", "Assembly to machine code.", "<p>" + mks(["Translates assembly language into machine code (binary)"]) + "</p>", None) + req("2 marks", "Describe", "Describe what is meant by a program that is partially compiled and partially interpreted.", "Intermediate code.", "<p>" + mks(["The source code is compiled to an intermediate code", "which is then interpreted when the program runs"]) + "</p>", None)

tips = tips_html([
  ("Compiler: whole program.", "Executable file; all errors together."),
  ("Interpreter: one line.", "Stops at the first error."),
  ("Say 'real time'.", "Errors corrected immediately."),
  ("Assembler: assembly to machine code.", "Never high-level."),
  ("Pair each point with its reason.", "Different platforms because it is interpreted."),
  ("Development: interpreter. Finished: compiler.", "Say which stage."),
], [("a compiler", "Translates the whole program into an executable."), ("an interpreter", "Translates and runs one line at a time."), ("an assembler", "Translates assembly language into machine code."), ("source code", "The program as written by the programmer.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Complete", "Fill in the missing words.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "Source code", true) + B(190, "Compiler", k >= 1) + B(360, k >= 3 ? "Executable" : "Errors?", k >= 2) + SV.path("M130,62 H190", "ax") + SV.path("M300,62 H360", "ax");
    o += SV.text(240, 125, ["", "the compiler reads ALL the code", "it reports all errors together (none here)", "an executable file runs without the source code"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 150, label: "Compiler", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [0, 1, 2, 3].map((i) => ({ cap: ["The programmer finishes writing the source code.", "The <b>compiler</b> checks all of it at the same time.", "All errors are reported together; if none, translation continues.", "The result is an <b>executable file</b>."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 5; i++) o += SV.rect(30, 20 + i * 28, 240, 24, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 4 }) + SV.text(40, 37 + i * 28, "line " + (i + 1), "lbl") + (i === 2 ? SV.text(180, 37 + i * 28, "error!", "lbl bd") : "");
    o += SV.text(300, 80, k < 2 ? "line " + (k + 1) + " translated and run" : k === 2 ? "error: the interpreter STOPS" : "fixed: continues from line 3", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 170, label: "Interpreter", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Line 1 is translated and run.", "Line 2 is translated and run.", "Line 3 has an error: the interpreter <b>stops</b> and displays it.", "The programmer corrects it immediately; the interpreter continues from there.", "Lines 4 and 5 run."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "Source code", true) + B(160, "Compiler", k >= 1) + B(310, "Intermediate code", k >= 2) + B(460, "Run by interpreter", k >= 3) + SV.path("M130,62 H160", "ax") + SV.path("M280,62 H310", "ax") + SV.path("M430,62 H460", "ax");
    o += SV.text(300, 125, ["", "the compiler produces intermediate code", "it can be copied to any platform", "interpreted at run time: optimised for that CPU"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 150, label: "Partial compilation", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [0, 1, 2, 3].map((i) => ({ cap: ["The source is compiled first...", "...to an intermediate code, not machine code.", "The same intermediate code works on different platforms.", "It is interpreted when run, and optimised for the CPU in use."][i], s: { i } })) });
})();

(function () {
  const prog = ["x ← 10", "y ← 5 +", "OUTPUT x", "z ← x / 0 ?", "OUTPUT y"], bad = [1, 3]; let fixed = false, msg = "";
  const paint = () => { $("#tlP").innerHTML = '<div class="tw"><table class="t mono">' + prog.map((l, i) => `<tr><td>${i + 1}</td><td>${l}</td><td>${bad.includes(i) && !(fixed && i === 1) ? "← error" : ""}</td></tr>`).join("") + "</table></div>"; $("#tlV").innerHTML = msg || "Choose a translator."; };
  const errs = () => bad.filter((i) => !(fixed && i === 1));
  $("#tl_c").onclick = () => { const e = errs(); msg = e.length ? `<b>Compiler</b> reports <b>all ${e.length} error(s)</b> (line ${e.map((i) => i + 1).join(" and line ")}). No executable file is produced and nothing runs.` : "<b>Compiler</b>: no errors, so an executable file is produced."; paint(); };
  $("#tl_i").onclick = () => { const e = errs(); msg = e.length ? `<b>Interpreter</b> runs line 1${e[0] > 1 ? " to " + e[0] : ""} then <b>stops at line ${e[0] + 1}</b> and reports that one error. Fix it and it continues.` : "<b>Interpreter</b>: all lines run."; paint(); };
  $("#tl_f").onclick = () => { fixed = true; msg = "Line 2 is fixed. Run the translators again: only line 4 is still wrong."; paint(); };
  $("#tl_r").onclick = () => { fixed = false; msg = ""; paint(); }; paint();
})();
btnTable("wB", "wO", [
  ["A finished app to be sold without its source code", "Compiler", "Executable file; source stays private"],
  ["Learning to program: fix each line as you go", "Interpreter", "Stops at the first error"],
  ["Testing half a program", "Interpreter", "Unfinished code can run"],
  ["Mnemonics such as LDD and ADD", "Assembler", "Assembly to machine code"],
  ["The same code on Windows and Mac", "Partially compiled", "Intermediate code interpreted on each platform"]
], ["Situation", "Translator", "Why"]);
(function () {
  let runs = 20; const paint = () => { const ct = 30, ir = 5; $("#rV").innerHTML = `Compile once (<b>${ct} s</b>) then each run takes about 1 s: <b>${ct + runs} s</b> for ${runs} runs. An interpreter translates each time: about 2 s per run, <b>${runs * 2} s</b>. ` + (ct + runs < runs * 2 ? "For many runs the compiled program wins." : "For a few runs the interpreter is quicker overall because there is no compile wait."); };
  Lib.slider($("#rS"), { id: "r1", label: "Number of runs ", min: 1, max: 60, value: runs, fmt: (x) => x, onInput: (v) => { runs = v; paint(); } }); paint();
})();
''' + _prjs

finish("as-5-2-1-language-translators", "as521", "Language Translators",
  "The assembler, the compiler and the interpreter compared, why partial compilation is used, and which translator suits development or a finished program, with animations, a compile-or-interpret lab and the real Paper 1 questions from 2021 to 2026.",
  "5.2.1", "5 · System software", "section 5.2 Language translators", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on language translators (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
