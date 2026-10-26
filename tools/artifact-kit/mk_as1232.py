"""AS CS 12.3.2: program maintenance. Run: python3 tools/artifact-kit/mk_as1232.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Maintenance</b> is the last stage of the program development life cycle: changing a program after it has been released. <b>Corrective</b> maintenance fixes errors (bugs) found while the program is in use. <b>Adaptive</b> maintenance changes the program to cope with a change in its environment or requirements, such as new hardware, new technology, a changed library module or a change in the law. <b>Perfective</b> maintenance improves the program without changing what it does, for example to make it faster or easier to use. Good <b>documentation</b> (an identifier table, design documents and comments) made during design and coding makes all three types easier.</p></div>

  <h2>1 · The three types</h2>
  ''' + tbl(["Type", "Purpose", "Typical reasons"], [
    ["<b>Corrective</b>", "Fix faults", "The program does not operate as expected, contains a bug, or unexpected bugs are reported after it is installed (passwords are not hidden)"],
    ["<b>Adaptive</b>", "Change the program to fit a change outside it", "A change in the user requirements; new technology or new hardware; changes made to library modules used; a change in the law (legislation); a new version of a standard such as HTML"],
    ["<b>Perfective</b>", "Make the program better without changing what it does", "Improve the speed of response; make the program more efficient or easier to use; improve the user interface"]]) + '''
  <p>Use the question to decide: a fault reported by users is corrective; a new requirement, new hardware or a change in the law is adaptive; a change that improves speed or efficiency is perfective.</p>

  <h2>2 · Why documentation matters</h2>
  <ul>
    <li>A maintenance programmer may not be the person who wrote the program. They need to find what each part does.</li>
    <li>An <b>identifier table</b> records each variable with its name, data type, purpose and an example value or initial value.</li>
    <li>Design documents (structure charts, flowcharts, state-transition diagrams, pseudocode) and comments in the code show how the program works, so a change can be made without introducing new faults.</li>
    <li>Meaningful identifier names, indentation, white space and comments make the code easier to understand and to change.</li>
  </ul>

  <h2>3 · Where maintenance fits</h2>
  <p>After testing and release, maintenance can go on for many years. A change may mean going back through analysis, design, coding and testing: even a small change has to be tested again so that it has not caused a new fault elsewhere.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Calling a bug fix adaptive: fixing faults is corrective.</li>
    <li>Describing perfective maintenance as adding a new feature required by a change in the requirement (that is adaptive).</li>
    <li>Giving a reason without naming the type, or a type without a matching reason: the marks are dependent.</li>
    <li>Writing "easier to read" for documentation: say what is recorded (purpose of each variable) and who uses it (the maintenance programmer).</li>
  </ul>
'''

watch = '''
  <h2>1 · Three reasons to change a released program</h2>
  <div id="stA"></div>
  <h2>2 · Documentation helps the next programmer</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Which maintenance?</h2>
  <p>Click a change to see its type.</p>
  <div class="card"><div id="mnB" class="btnrow"></div><div id="mnO"></div></div>
  <h2>Lab 2 · Which type? Quick sort</h2>
  <div class="card"><div class="btnrow"><button id="qz_c">Corrective</button><button id="qz_a">Adaptive</button><button id="qz_p">Perfective</button><button id="qz_n">Next change</button></div><div id="qzV"></div></div>
'''

_pr, _prjs = PR(["Which type of maintenance?", "Fix, adapt or improve?", "Match the type to the reason", "Put the steps of a fix in order", "Working out", "Multiple choice"],
  ("Which type of maintenance?", ["Corrective", "Adaptive", "Perfective"], [("The program crashes when a field is empty and is fixed", 0), ("The program is changed to run on new hardware", 1), ("The speed of response is improved", 2), ("A change in the law means the program must store extra data", 1), ("Passwords are not hidden when typed, and this is fixed", 0), ("The interface is made easier to use", 2)], "Fix a fault: corrective. Environment changed: adaptive. Improve: perfective."),
  ("Is the change a fix, an adaptation or an improvement?", ["Fix", "Adapt", "Improve"], [("A bug is found after installation", 0), ("A library module the program uses changes", 1), ("The code is made to run faster", 2), ("A new HTML version is released", 1), ("The wrong total is corrected", 0), ("The screens are redesigned for easier use", 2)], "Bug: fix. Environment: adapt. Better: improve."),
  [["Corrective", "Fixes errors"], ["Adaptive", "Copes with a change in the environment or requirements"], ["Perfective", "Improves the program without changing what it does"], ["Identifier table", "Documents variables for maintenance"], ["Legislation change", "A reason for adaptive maintenance"]],
  ("Put the steps of a maintenance change in order.", ["A fault or a need for a change is reported", "The programmer reads the documentation", "The change is made in the code", "The program is tested again", "The updated program is released"], "Report, read, change, test, release."),
  [{"q": "How many types of maintenance are named on this page?", "a": 3, "unit": "", "tol": 0.01, "hint": "Corrective, adaptive, perfective.", "sol": "<b>3</b>."}, {"q": "A bug list has 12 faults. 5 are fixed. How many corrective changes remain?", "a": 7, "unit": "", "tol": 0.01, "hint": "12 − 5.", "sol": "<b>7</b>."}, {"q": "A response time falls from 800 ms to 200 ms. By what percentage is it reduced?", "a": 75, "unit": "%", "tol": 0.01, "hint": "(800 − 200) ÷ 800.", "sol": "<b>75%</b>. This is perfective maintenance."}, {"q": "An identifier table has 4 columns: name, type, purpose and example. How many columns record something other than the data type and name?", "a": 2, "unit": "", "tol": 0.01, "hint": "Purpose and example.", "sol": "<b>2</b>."}, {"q": "A program is on 3 platforms and a new platform is added. How many platforms must now be supported?", "a": 4, "unit": "", "tol": 0.01, "hint": "3 + 1: this is adaptive maintenance.", "sol": "<b>4</b>."}],
  [("Fixing a bug found after release is:", ["Corrective", "Adaptive", "Perfective", "Analysis"], 0, "Corrective."), ("Changing a program for new hardware is:", ["Adaptive", "Corrective", "Perfective", "Design"], 0, "Adaptive."), ("Making a program respond faster is:", ["Perfective", "Corrective", "Adaptive", "Testing"], 0, "Perfective."), ("A reason for adaptive maintenance:", ["A change in legislation", "A typing error", "A bug", "A faster response"], 0, "Law changed."), ("A suitable way of documenting variables:", ["An identifier table", "A beta test", "A stub", "A loop"], 0, "Identifier table."), ("Maintenance is in the life cycle:", ["After testing and release", "Before analysis", "Instead of design", "Only for new programs"], 0, "Last stage.")],
  [("Corrective", "Fix faults."), ("Adaptive", "Adapt to a change in the environment."), ("Perfective", "Improve without changing function."), ("Legislation", "A reason for adaptive."), ("Identifier table", "Documents variables."), ("Documentation", "Helps the maintenance programmer."), ("Retest", "After every change."), ("Maintenance", "The last life cycle stage.")])

real = RWNOTE + (
rw("Phone app updates", "Some updates fix bugs (corrective), some support a new phone or operating system (adaptive) and some make the app faster (perfective).", "all three types.") +
rw("Tax software every year", "When the tax rules change, the program has to be changed: adaptive maintenance in response to legislation.", "adaptive.") +
rw("A game patch after launch", "Players report that the score is wrong, and the developer fixes it, retests and releases a patch.", "corrective.") +
rw("A website redesign for speed", "The pages are rewritten so they load faster without changing what they do.", "perfective.")
)

where = [
  ("M/J 2022", "23", "2", "4", "Name two other types of maintenance, with a reason for each"),
  ("O/N 2022", "23", "1(d)", "2", "Two reasons adaptive maintenance may be required"),
  ("M/J 2023", "23", "5(b)", "1", "The type of maintenance applied to improve speed of response"),
  ("O/N 2023", "23", "1(d)", "2", "The type of maintenance when the hardware changes; another reason"),
  ("M/J 2024", "22", "1(c)", "2", "A way of documenting variables to simplify maintenance"),
  ("M/J 2025", "22", "1(b)", "3 + 1", "Three reasons for adaptive maintenance; one other type"),
  ("M/J 2026", "21", "3(b)", "1 (adaptive gap)", "Complete the summary of the development of a system"),
  ("M/J 2026", "23", "3(a)", "1 (corrective gap)", "Complete the summary of the development of a system")]

past = '''  <p class="note">Maintenance is a short question: name the type, give a matching reason. Know the three types, and two or three reasons for adaptive.</p>
''' + peq(SRC("s22", "23", "Q2"), "4 marks", "Name / Give",
  "A program has been written to implement a website browser and maintenance is now required. One type of maintenance is called perfective. Name two other types of maintenance that the program may require and give a reason for each.", "Corrective and adaptive, with a reason for each.",
  "<p>Dependent marks: one mark for the type and one for the matching reason.</p>" + tbl(["Type", "Reason"], [["Adaptive", "To accommodate a change in the requirement, technology or legislation (for example a new HTML version is available)"], ["Corrective", "The program does not operate as expected or contains a bug (for example passwords are not hidden)"]]), "Giving two reasons for the same type, or a reason with no type named.") + peq(SRC("w22", "23", "Q1(d)"), "2 marks", "Give",
  "Adaptive maintenance needs to be carried out on a website program. Give two reasons why adaptive maintenance may be required.", "A change outside the program.",
  "<p>Any two: " + mks(["A change to the website requirements", "New technologies are available to host the website, or changes are made to the library modules used", "A change in the relevant legislation"], "a") + "</p>", None) + peq(SRC("s23", "23", "Q5(b)"), "1 mark", "State",
  "Testing is completed and the program is made available to users. Some time later, changes are made to improve the speed of response of the program. State the type of maintenance that has been applied.", "It improves the program without changing what it does.",
  "<p>" + mks(["Perfective"], "a") + "</p>", None) + peq(SRC("w23", "23", "Q1(d)"), "2 marks", "Identify / Give",
  "The hardware that runs a program is changed and the program needs to be modified so that it works with the new hardware. Identify the type of maintenance that this represents and give one other reason why this type of maintenance may be needed.", "Adaptive. Requirements or the law.",
  "<p>" + mks(["Type: adaptive", "Reason: the user requirements change, or to accommodate legislative changes"], "a") + "</p>", None) + peq(SRC("s24", "22", "Q1(c)"), "2 marks", "State",
  "The variables in a program are chosen during the design stage of the program development life cycle. The choices are to be documented to simplify program maintenance. State a suitable way of documenting the variables and give one piece of information that should be recorded, in addition to the data type.", "An identifier table. Purpose.",
  "<p>" + mks(["An identifier table", "One piece of information: an explanation of what each variable is used for (its purpose), an example of the data values stored, or its initial value"], "a") + "</p>", None) + peq(SRC("s25", "22", "Q1(b)"), "3 + 1 marks", "Give / Identify",
  "A program to control the production line in a factory has been in use for a number of months and adaptive maintenance is required. (i) Give three reasons why adaptive maintenance may be required. (ii) Identify one other type of program maintenance.", "Changes in requirements, technology, library modules, the law.",
  "<p><b>(i)</b> Any three: " + mks(["A change to the production line requirements", "New technology or hardware is available to control the production line", "Changes made to the library modules used", "A change in the relevant legislation"], "a") + "</p><p><b>(ii)</b> " + mks(["Perfective", "or corrective"], "b") + "</p>", None) + peq(SRC("s26", "21", "Q3(b)"), "1 mark (of 6)", "Complete",
  "In the first week after the new software was rolled out to all five call centres, staff report that it still requires extra features which were not originally agreed. The software is withdrawn until ______ maintenance is completed.", "New requirements outside the original agreement.",
  "<p>" + mks(["Adaptive"], "a") + "</p>", "Writing corrective: nothing is broken, the requirements have changed.") + peq(SRC("s26", "23", "Q3(a)"), "1 mark (of 4)", "Complete",
  "A new system is installed in all shops. In the first week of its use, unexpected bugs are reported. ______ maintenance has to be carried out.", "Bugs are faults.",
  "<p>" + mks(["Corrective"], "a") + "</p>", None)

review = req("3 marks", "State", "State the type of maintenance: (a) a spelling mistake in the output is corrected; (b) the program is changed because the tax rate changes; (c) the code is rewritten to use less memory.", "Fix, adapt, improve.", "<p>" + mks(["Corrective", "Adaptive", "Perfective"]) + "</p>", None) + req("2 marks", "Explain", "Explain why an identifier table helps a maintenance programmer.", "Purpose of variables.", "<p>" + mks(["It records what each variable is used for and its type", "so the programmer can understand the code written by someone else and change it safely"]) + "</p>", None) + req("3 marks", "Give", "Give three reasons for adaptive maintenance.", "Environment changes.", "<p>" + mks(["A change in requirements", "New hardware or technology", "A change in the law or in a library module used"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a program must be retested after maintenance.", "New faults.", "<p>" + mks(["A change may have introduced new faults", "or stopped parts that worked from working"]) + "</p>", None) + req("2 marks", "Describe", "Describe perfective maintenance.", "Improve, same function.", "<p>" + mks(["Changes made to improve the program (speed, efficiency, ease of use)", "without changing what the program does"]) + "</p>", None)

tips = tips_html([
  ("Three types.", "Corrective fixes, adaptive adapts, perfective improves."),
  ("A reason for each.", "Marks depend on the type and the matching reason."),
  ("Adaptive reasons.", "Requirements, technology or hardware, library modules, law."),
  ("Perfective is not new.", "Same function, better speed or use."),
  ("Documentation.", "An identifier table with purpose, type, example."),
  ("Retest.", "Every change needs testing."),
], [("maintenance", "Changing a program after it has been released."), ("corrective", "Fixing errors."), ("adaptive", "Changing the program to suit a change in its environment."), ("perfective", "Improving the program without changing its function.")],
  [("State", "A short answer."), ("Identify", "Name the type."), ("Give", "A reason or an example."), ("Complete", "Fill in the gap.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const N = [["Corrective", "a bug is fixed"], ["Adaptive", "new hardware or law"], ["Perfective", "faster and easier"]]; let o = ""; N.forEach((n, i) => o += SV.rect(10 + i * 110, 14, 100, 30, i === k ? "f3" : "cell", { rx: 5 }) + SV.text(60 + i * 110, 34, n[0], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(10, 70, N[k][0] + ": " + N[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 350, h: 84, label: "Maintenance", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A fault is found: corrective.", "The world changes: adaptive.", "The program is improved: perfective."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 8, 310, 62, "cell", { rx: 6 }) + SV.text(20, 26, "Identifier table", "lbl bd", { style: "font-size:12px" }); if (k >= 1) o += SV.text(20, 44, "Total  REAL  sum of the marks", "lbl", { style: "font-size:11px;font-family:monospace" }); if (k >= 2) o += SV.text(20, 60, "Count  INTEGER  number of students", "lbl", { style: "font-size:11px;font-family:monospace" }); o += SV.text(10, 92, ["", "The purpose is recorded", "A new programmer can follow the code"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 102, label: "Documentation", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["An identifier table is made in design.", "Each variable has its type and purpose.", "Years later, the maintenance programmer reads it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("mnB", "mnO", [
  ["Users report a bug and it is fixed", "Corrective", "fixing a fault"],
  ["The program is changed for new hardware", "Adaptive", "the environment changed"],
  ["A change in the law means the program stores new data", "Adaptive", "legislation"],
  ["The speed of response is improved", "Perfective", "improvement, same function"],
  ["A library module used by the program changes", "Adaptive", "environment changed"]
], ["Change", "Type", "Why"]);
(function () {
  const Q = [["Passwords were not hidden on screen and this is fixed", 0], ["The program is changed to work with a new operating system", 1], ["The code is rewritten so results appear faster", 2], ["Unexpected bugs are reported in the first week", 0], ["The law changes what data may be stored", 1], ["The menus are redesigned to be easier to use", 2]]; let i = 0, score = 0, tries = 0, done = false;
  const paint = (m) => { $("#qzV").innerHTML = `<p><b>${Q[i][0]}</b></p><div class="verdict">${m || "Choose a type."} Score: ${score} / ${tries}</div>`; };
  const ans = (k) => { if (done) return; tries++; if (k === Q[i][1]) { score++; done = true; paint("Correct."); } else paint("Not that one: try again, or move to the next."); };
  $("#qz_c").onclick = () => ans(0); $("#qz_a").onclick = () => ans(1); $("#qz_p").onclick = () => ans(2); $("#qz_n").onclick = () => { i = (i + 1) % Q.length; done = false; paint(); }; paint();
})();
''' + _prjs

finish("as-12-3-2-program-maintenance", "as1232", "Program Maintenance",
  "Corrective, adaptive and perfective maintenance, reasons for each and documentation that helps maintenance, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "12.3.2", "12 · Software development", "section 12.3 Program testing and maintenance", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on program maintenance (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
