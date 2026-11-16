"""20.2.2 extra resource: try, except, else and finally in Python. Run: python3 tools/artifact-kit/mk_ac20x3.py"""
from ac20f import *

OLDQ = old_questions("mk_ac2022.py")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <code>try</code> block holds the statements that might cause an exception. If one does, the rest of the block is <b>skipped</b> and Python looks for an <code>except</code> block that matches the exception, runs it, and then carries on with the statement after the whole structure. If nothing goes wrong the <code>except</code> blocks are skipped. You can name the exception (<code>except ValueError:</code>), give several <code>except</code> blocks for different exceptions, or use a bare <code>except:</code> that catches any. An <code>else</code> block runs only when there was <b>no</b> exception, and a <code>finally</code> block runs <b>whether or not</b> there was one, which makes it the place to tidy up. The exam pseudocode form is <code>TRY ... EXCEPT ... FINALLY ... ENDTRY</code>.</p></div>

  <h2>1 · The basic structure</h2>
  ''' + both('''try:
    Number = int(input("Enter a number: "))
    Result = 100 / Number
    print(Result)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")''', '''TRY
   INPUT Number
   Result <- 100 / Number
   OUTPUT Result
EXCEPT
   OUTPUT "Cannot divide by zero"
FINALLY
   OUTPUT "Done"
ENDTRY''') + '''
  <p>Exam pseudocode has one <code>EXCEPT</code> block for every kind of exception. The named exceptions and <code>else</code> below are Python only.</p>

  <h2>2 · What runs, in order</h2>
  <div class="tw"><table class="t">
    <tr><th>Block</th><th>When it runs</th></tr>
    <tr><td><code>try</code></td><td>Always starts. Stops at the first statement that raises an exception; the rest of the block is skipped</td></tr>
    <tr><td><code>except</code></td><td>Only if an exception was raised <b>and</b> it matches. The first matching block runs; the others are skipped</td></tr>
    <tr><td><code>else</code></td><td>Only if the try block finished with <b>no</b> exception</td></tr>
    <tr><td><code>finally</code></td><td>Always, last, whether or not there was an exception</td></tr>
  </table></div>

  <h2>3 · Naming the exception</h2>
  <p>Different problems often need different responses, so there can be several <code>except</code> blocks.</p>
  <div class="code">''' + pc('''try:
    Number = int(input("Enter a number: "))
    Result = 100 / Number
except ValueError:                    # the text was not a whole number
    print("Not a whole number")
except ZeroDivisionError:             # the number was 0
    print("Cannot divide by zero")
else:                                 # no exception at all
    print("Result is", Result)''') + '''</div>
  <div class="tw"><table class="t">
    <tr><th>Form</th><th>Catches</th></tr>
    <tr><td><code>except ValueError:</code></td><td>Only that exception. Anything else still halts the program</td></tr>
    <tr><td><code>except (ValueError, TypeError):</code></td><td>Either of those two</td></tr>
    <tr><td><code>except IOError:</code></td><td>Problems opening or reading a file (<code>FileNotFoundError</code> is one)</td></tr>
    <tr><td><code>except:</code></td><td>Every exception. Accepted in the exam; less precise</td></tr>
  </table></div>
  <div class="code">''' + pc('''try:
    Age = int(input("Enter your age: "))
except ValueError as Problem:
    print("Problem:", Problem)        # Problem holds the reason Python gave''') + '''</div>

  <h2>4 · finally: tidying up</h2>
  <p>With input 0 the output is <code>Cannot divide by zero</code> then <code>Done</code>. With input 4 it is <code>25.0</code> then <code>Done</code>. The <code>finally</code> block runs both times. It even runs when an exception is <b>not</b> caught by any <code>except</code>: Python runs it, then halts.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li><code>try</code> with no <code>except</code> (or <code>finally</code>). It is a syntax error.</li>
    <li>An <code>except</code> block that does nothing, or has no message.</li>
    <li>Putting statements that can fail <b>outside</b> the <code>try</code>.</li>
    <li>Naming the wrong exception, such as <code>except IOError</code> for a <code>ValueError</code>. It does not match, so the program halts.</li>
    <li>Writing the colon or the indentation wrongly: every block ends with <code>:</code> and its lines are indented.</li>
    <li>Thinking <code>else</code> and <code>finally</code> are the same. <code>else</code> only runs if there was no exception.</li>
  </ul>
'''

watch = '''
  <h2>1 · Input 0: an exception</h2><p>Press Play, or click the steps. Both versions of the code are highlighted together.</p><div id="stA"></div>
  <h2>2 · Input 4: no exception</h2><div id="stB"></div>
  <h2>3 · Several except blocks, and else</h2><div id="stC"></div>
'''

PS = ['TRY', '   INPUT Number', '   Result <- 100 / Number', '   OUTPUT Result', 'EXCEPT', '   OUTPUT "Cannot divide by zero"', 'FINALLY', '   OUTPUT "Done"', 'ENDTRY']
PY = ['try:', '    Number = int(input("Enter a number: "))', '    Result = 100 / Number', '    print(Result)', 'except ZeroDivisionError:', '    print("Cannot divide by zero")', 'finally:', '    print("Done")']
ot = lambda *l: [(330, 10 + 24 * i, s, c) for i, (s, c) in enumerate(l)]
G, B = "lbl bd t3", "lbl bd t2"
stA = stp("stA", "try, except and finally with input 0", [
    dict(c="The try block starts. The user types <b>0</b>.", p=0, y=0, v=[("Number", ""), ("Result", "")], f=[]),
    dict(c="The input is read: <code>Number</code> is 0.", p=1, y=1, v=[("Number", "0"), ("Result", "")], f=[]),
    dict(c="<code>100 / Number</code> raises <b>ZeroDivisionError</b>. The rest of the try block is skipped: <code>Result</code> is never set and the print is not run.", p=2, y=2, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("ZeroDivisionError", B))),
    dict(c="Python looks for an except that matches and finds <code>except ZeroDivisionError</code>.", p=4, y=4, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("ZeroDivisionError", B))),
    dict(c="The response runs.", p=5, y=5, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("Cannot divide by zero", G))),
    dict(c="<b>finally</b> runs next, as it always does.", p=6, y=6, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("Cannot divide by zero", G))),
    dict(c="<code>Done</code> is output. The program then carries on after the structure.", p=7, y=7, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("Cannot divide by zero", G), ("Done", G)))],
    PS, PY, lh=22, vw=150, fh=70, dwell=3000)

stB = stp("stB", "try, except and finally with input 4", [
    dict(c="The try block starts. This time the user types <b>4</b>.", p=0, y=0, v=[("Number", ""), ("Result", "")], f=[]),
    dict(c="<code>Number</code> is 4.", p=1, y=1, v=[("Number", "4"), ("Result", "")], f=[]),
    dict(c="<code>100 / 4</code> works: <code>Result</code> is 25.0.", p=2, y=2, v=[("Number", "4"), ("Result", "25.0")], f=[]),
    dict(c="The result is output.", p=3, y=3, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("25.0", G))),
    dict(c="No exception was raised, so the <b>except block is skipped</b>.", p=4, y=4, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("25.0", G), ("except skipped", "sm"))),
    dict(c="<b>finally</b> still runs.", p=6, y=6, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("25.0", G), ("except skipped", "sm"))),
    dict(c="<code>Done</code> is output. <code>finally</code> runs with or without an exception.", p=7, y=7, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("25.0", G), ("Done", G)))],
    PS, PY, lh=22, vw=150, fh=70, dwell=3000)

PS3 = ['TRY', '   INPUT Number', '   Result <- 100 / Number', 'EXCEPT', '   OUTPUT "Problem with the number"', 'ENDTRY', '// one EXCEPT covers every exception', '// named exceptions and else are Python']
PY3 = ['try:', '    Number = int(input("Enter a number: "))', '    Result = 100 / Number', 'except ValueError:', '    print("Not a whole number")', 'except ZeroDivisionError:', '    print("Cannot divide by zero")', 'else:', '    print("Result is", Result)']
stC = stp("stC", "Which except block runs?", [
    dict(c="Two different exceptions can be raised in the try block, so there are two except blocks, and an else block for when nothing goes wrong.", p=-1, y=-1, v=[("Number", ""), ("Result", "")], f=[]),
    dict(c="The user types <b>abc</b>. <code>int(\"abc\")</code> raises <b>ValueError</b>. The rest of the try block is skipped.", p=1, y=1, v=[("Number", "abc"), ("Result", "")], f=[], t=ot(("ValueError", B))),
    dict(c="<code>except ValueError</code> matches, so it runs. The other except and the else are skipped.", p=4, y=4, v=[("Number", "abc"), ("Result", "")], f=[], t=ot(("Not a whole number", G))),
    dict(c="Now the user types <b>0</b>. <code>int(\"0\")</code> works, then <code>100 / 0</code> raises <b>ZeroDivisionError</b>.", p=2, y=2, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("ZeroDivisionError", B))),
    dict(c="Python checks the blocks in order. <code>except ValueError</code> does not match; <code>except ZeroDivisionError</code> does.", p=3, y=5, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("ZeroDivisionError", B))),
    dict(c="The matching response runs.", p=4, y=6, v=[("Number", "0"), ("Result", "")], f=[], t=ot(("Cannot divide by zero", G))),
    dict(c="Finally the user types <b>4</b>. Both statements work: <code>Result</code> is 25.0.", p=2, y=2, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("no exception", "sm"))),
    dict(c="No exception, so no except block runs. The <b>else</b> block runs instead.", p=-1, y=8, v=[("Number", "4"), ("Result", "25.0")], f=[], t=ot(("Result is 25.0", G)))],
    PS3, PY3, lh=22, vw=150, fh=70, dwell=3200)

explore = '''
  <h2>Lab 1 · Which blocks run?</h2>
  <p>The program has try, two except blocks, else and finally. Choose what the user types and see which blocks run, in order.</p>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div><div class="verdict" id="wV"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

lab = r'''
(function () {
  const ins = ["4", "0", "abc"];
  const code = ["try:", "    Number = int(input(...))", "    Result = 100 / Number", "except ValueError:", "    print(\"Not a whole number\")", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "else:", "    print(\"Result is\", Result)", "finally:", "    print(\"Done\")"];
  const run = (t) => {
    const n = parseInt(t, 10), rows = [["try", "runs"]], out = [];
    if (isNaN(n)) { rows[0][1] = "stops at int(): ValueError raised"; rows.push(["except ValueError", "RUNS"], ["except ZeroDivisionError", "skipped"], ["else", "skipped"]); out.push("Not a whole number"); }
    else if (n === 0) { rows[0][1] = "stops at 100 / Number: ZeroDivisionError raised"; rows.push(["except ValueError", "skipped (no match)"], ["except ZeroDivisionError", "RUNS"], ["else", "skipped"]); out.push("Cannot divide by zero"); }
    else { rows[0][1] = "finishes normally"; rows.push(["except ValueError", "skipped"], ["except ZeroDivisionError", "skipped"], ["else", "RUNS"]); out.push("Result is " + (Number.isInteger(100 / n) ? (100 / n).toFixed(1) : 100 / n)); }
    rows.push(["finally", "RUNS (always)"]); out.push("Done"); return { rows, out };
  };
  const paint = (i) => {
    $$("#wB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = run(ins[i]);
    $("#wO").innerHTML = '<div class="grid2"><div>' + lineHTML(code) + '</div><div><div class="tw"><table class="t"><tr><th>Block</th><th>What happens</th></tr>' + r.rows.map((x) => `<tr><td><code>${x[0]}</code></td><td>${x[1]}</td></tr>`).join("") + "</table></div></div></div>";
    $("#wV").textContent = "Output: " + r.out.join(", then ");
  };
  $("#wB").innerHTML = ins.map((x) => `<button class="b">Type ${x}</button>`).join("");
  $$("#wB button").forEach((b, i) => (b.onclick = () => paint(i))); paint(1);
})();
btnTable("mB", "mO", [
  ["try with no except", "try:\n    X = int(input())", "A try must be followed by except or finally: this is a syntax error", "Add except ValueError: with a response"],
  ["Empty except", "except ValueError:\n    pass", "The user is told nothing, and the exam mark needs a message or action", "print(\"Please enter a whole number\")"],
  ["Risky line outside try", "X = int(input())\ntry:\n    print(100 / X)", "The int() can still fail and halt the program", "Put int(input()) inside the try"],
  ["Wrong exception", "try: X = int(\"abc\")\nexcept IOError: ...", "IOError does not match a ValueError, so the program halts", "except ValueError: (or a bare except:)"],
  ["else instead of finally", "else:\n    File.close()", "else only runs when nothing went wrong, so the file stays open after an exception", "Use finally: for tidying up"],
  ["Missing colon or indent", "except ValueError\nprint(\"Oops\")", "Each except needs a colon and an indented block", "except ValueError:\n    print(\"Oops\")"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Which block does each statement describe?", ["try", "except", "else", "finally"],
    [("Holds the statements that might raise the exception", 0), ("Runs only if an exception was raised and it matches", 1), ("Runs only if there was no exception", 2), ("Runs whether or not an exception happened", 3), ("The place to tidy up, such as closing a file", 3), ("Contains the message shown to the user", 1), ("Skipped if the try block raises an exception", 2), ("Is left part-way when an exception is raised", 0)],
    "try: risky. except: response. else: no exception. finally: always.") + ORDER(
    "Put the steps in order for a try block that raises an exception which is caught, with a finally block.",
    ["The try block starts", "A statement in the try block raises an exception", "The rest of the try block is skipped", "The matching except block runs", "The finally block runs", "The program carries on after the structure"],
    "Try, raise, skip, except, finally, carry on.") + MATCH([
    ["try", "The block of statements that might cause an exception"], ["except", "The block that responds to the exception"], ["else", "Runs only if no exception was raised"], ["finally", "Runs whether or not an exception was raised"], ["ValueError", "Raised when int(\"abc\") cannot convert the text"], ["ZeroDivisionError", "Raised when a number is divided by zero"]]) + CALC([
    {"q": "The program on this page is run with input 4 (result 25.0, with finally). How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "The result and Done.", "sol": "<b>2</b>."},
    {"q": "Same program, input 0. How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "The message and Done.", "sol": "<b>2</b>."},
    {"q": "Program: try: print(\"A\"); print(int(\"x\")); print(\"B\") except ValueError: print(\"C\") finally: print(\"D\"). How many lines are printed?", "a": 3, "unit": "", "tol": 0.01, "hint": "A, C and D. B is skipped.", "sol": "<b>3</b> (A, C, D)."},
    {"q": "The try block raises a ValueError but the only except is for ZeroDivisionError. A finally block prints one line. How many lines does the program print before the error message?", "a": 1, "unit": "", "tol": 0.01, "hint": "finally still runs, then the program halts.", "sol": "<b>1</b> (the finally line)."},
    {"q": "A try has three except blocks, and an exception matches the second. How many except blocks run?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first match runs.", "sol": "<b>1</b>."}]) + MCQ([
    ("What happens to the rest of a try block after an exception is raised?", ["It runs", "It is skipped", "It runs twice", "It moves to finally"], 1, "Control jumps to the matching except."),
    ("Which block runs only if no exception happens?", ["except", "finally", "else", "try"], 2, "else is the no-exception block."),
    ("Which block always runs?", ["except", "finally", "else", "none of them"], 1, "finally runs whether or not there was an exception."),
    ("What does a bare except: catch?", ["Only ValueError", "Only file errors", "Any exception", "No exceptions"], 2, "A bare except catches everything."),
    ("try with no except or finally is...", ["Fine", "A syntax error", "A logic error", "Only a warning"], 1, "A try needs a handler."),
    ("In exam pseudocode, which keyword ends the structure?", ["END", "ENDTRY", "ENDEXCEPT", "STOP"], 1, "TRY ... EXCEPT ... FINALLY ... ENDTRY.")], "qz1") + CARDS([
    ("try", "The statements that might raise an exception."), ("except", "The response. Naming the exception is best."), ("else", "Runs only when there was no exception. Python only."), ("finally", "Always runs. For tidying up."),
    ("Bare except", "Catches every exception. Accepted in the exam."), ("except ... as E", "E holds the reason Python gave."), ("Order", "First matching except runs; the rest are skipped."), ("ENDTRY", "Ends the exam pseudocode structure.")])

real = RWNOTE + (
    rw("A form with two kinds of bad input", "A calculator page gives one message for text that is not a number and a different one for a division by zero, because the two need different advice.", "several except blocks for different exceptions.") +
    rw("A report that always closes its file", "A program writes a report and must release the file whatever happens, so the closing is in finally, not at the end of the try block.", "finally: runs with or without an exception.") +
    rw("A save that confirms only when it worked", "A message 'Saved' is shown only if no problem happened, and an error message otherwise.", "else: for the no-exception path.") +
    rw("A catch-all in a launcher", "A launcher wraps starting each program in try and a general except, so one failing program never closes the launcher.", "a bare except catching everything.") +
    rw("A hospital system closing a connection", "Whether a record was read or the read failed, the database connection is closed at the end so it is not left open.", "finally for cleanup."))

review = (
    req("3 marks", "Write", "Write Python that divides 100 by <code>Number</code> and outputs <code>Cannot divide by zero</code> if <code>Number</code> is 0.", "Risky statement in try, response in except.", pc('''try:
    print(100 / Number)
except ZeroDivisionError:
    print("Cannot divide by zero")'''), "Leaving the print outside the try.") +
    req("2 marks", "State", "State the difference between an <code>else</code> block and a <code>finally</code> block.", "When each runs.", mks(["else runs only if no exception was raised", "finally runs whether or not an exception was raised"])) +
    req("3 marks", "Trace", "State the output when the code below is run and the user types <code>abc</code>." + qcode('''try:
    N = int(input())
    print("A")
except ValueError:
    print("B")
finally:
    print("C")'''), "int() fails before A is printed.", mks(["B", "C", "A is not output"]) + "<p>Output: B then C.</p>", "Including A. The try block stops at the failing line.") +
    req("2 marks", "Explain", "Why is naming the exception in the except block better than using a bare except?", "Think of exceptions you did not expect.", mks(["Only the expected exception is caught, so a different problem is not hidden", "each exception can be given its own, more accurate message"])) +
    req("2 marks", "Explain", "A programmer closes a file in an else block. Explain the problem and give a better place.", "What if an exception happens?", mks(["else only runs when no exception happened, so the file stays open after an exception", "closing it in a finally block means it is closed either way"])))

where = [("O/N 2022", "41, 43", "1(b)", "6", "ReadFile(): read 100 integers from IntegerData.txt with exception handling"),
         ("M/J 2023", "41, 43", "1(a)(ii)", "1 + 4", "Read 25 integers from Data.txt into an array with exception handling")]
past = "".join(OLDQ[k] for k in ["O/N 2022 · 9618/41, 43 · Q1(b)", "M/J 2023 · 9618/41, 43 · Q1(a)"])
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The try and except structure is a mark inside the Paper 4 file questions. The mark schemes use except IOError or a bare except, with a message. else and finally have not been required, but finally is part of the exam pseudocode."

tipsl = [("try needs except.", "A try with no except or finally is a syntax error."), ("Risky lines go inside.", "Everything that can fail belongs in the try block."), ("Always a message.", "An except with no action earns nothing."), ("Match the exception.", "ValueError for bad text, IOError for files. Or use a bare except."), ("else is the no-exception block.", "finally runs whatever happens."), ("Colons and indents.", "Each block ends with : and is indented.")]
sents = [("Describe try and except", "The statements that might cause an exception are in the try block, and if one occurs the except block responds to it."), ("Describe finally", "A finally block runs whether or not an exception occurred, so it is used to tidy up."), ("Describe the effect", "The rest of the try block is skipped and the program carries on after the structure.")]
words = [("Write", "Produce Python with try, except and a message."), ("State", "Give a fact or the output."), ("Explain", "A reason as well as the fact."), ("Trace", "Follow the code line by line and give the output.")]

finishf("ac20x3", "ac-20-2-2-try-except-python", "try, except, else and finally in Python",
        "How a try block, except blocks, else and finally run and in what order, with named exceptions and the exam pseudocode form; pseudocode and Python side by side, with line-by-line animations.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words, sub_num="20.2.2")
