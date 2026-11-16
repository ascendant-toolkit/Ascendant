"""20.2.2 extra resource: why and when to use exception handling. Run: python3 tools/artifact-kit/mk_ac20x2.py"""
from ac20f import *

OLDQ = old_questions("mk_ac2022.py")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Exception handling</b> is a process that responds to an unwanted or unexpected event while a program is running, so the program does not stop unexpectedly. There are three reasons to use it: to <b>trap runtime errors</b>, to <b>prevent the program halting</b>, and to <b>show a meaningful message</b> (or recover) instead of a system error. Use it where the problem comes from <b>outside the program's control</b> and cannot be ruled out in advance, such as opening a file, reading a file, or converting what a user typed. For a value that has to be in a range, or a choice from a known set, an ordinary <b>IF check</b> (validation) is the right tool. The two work together: validation checks the data is sensible, and exception handling catches what is still able to go wrong.</p></div>

  <h2>1 · Why use it: the three reasons</h2>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>What it means</th><th>Without it</th></tr>
    <tr><td>Trap runtime errors</td><td>The error is caught at the moment it happens</td><td>The error goes uncaught</td></tr>
    <tr><td>Stop the program halting</td><td>The program carries on after the problem</td><td>It stops at that line and later statements never run</td></tr>
    <tr><td>Meaningful message or recovery</td><td>The user is told what to do, or asked again</td><td>A system error message that means nothing to the user</td></tr>
  </table></div>

  <h2>2 · The same input, handled</h2>
  <p>The user types <b>ten</b> instead of 10. The conversion cannot be done, but the program responds and carries on.</p>
  ''' + both('''try:
    Age = int(input("Enter your age: "))
    print("Next year you will be", Age + 1)
except ValueError:
    print("Please enter a whole number")
print("Finished")''', '''TRY
   INPUT Age
   OUTPUT "Next year you will be ", Age + 1
EXCEPT
   OUTPUT "Please enter a whole number"
ENDTRY
OUTPUT "Finished"''') + '''

  <h2>3 · When to use it, and when to use an IF</h2>
  <div class="tw"><table class="t">
    <tr><th>Use exception handling for</th><th>Use an ordinary IF check for</th></tr>
    <tr><td>Opening, reading and writing files</td><td>A value that must be in a range, such as <code>IF Age &lt; 0 THEN</code></td></tr>
    <tr><td>Converting typed input: <code>int(input())</code></td><td>A list index you can test: <code>IF Index &lt; len(List)</code></td></tr>
    <tr><td>Network, printer or disk problems</td><td>A menu choice from a known set</td></tr>
    <tr><td>Anything that depends on something outside the program</td><td>Logic errors in your own algorithm, which are fixed in the code, not caught</td></tr>
  </table></div>

  <h2>4 · Using both: ask until the input is valid</h2>
  <p><code>int()</code> can fail, so it goes inside a <code>try</code>. Whether the age is sensible is a range check, so it is an <code>IF</code>.</p>
  ''' + both('''Valid = False
while not Valid:
    try:
        Age = int(input("Enter your age: "))
        if Age < 0 or Age > 120:
            print("Age must be between 0 and 120")
        else:
            Valid = True
    except ValueError:
        print("Please enter a whole number")''', '''Valid <- FALSE
WHILE NOT Valid
   TRY
      INPUT Age
      IF Age < 0 OR Age > 120 THEN
         OUTPUT "Age must be between 0 and 120"
      ELSE
         Valid <- TRUE
      ENDIF
   EXCEPT
      OUTPUT "Please enter a whole number"
   ENDTRY
ENDWHILE''') + '''

  <h2>5 · Why checking first is not always enough</h2>
  <p>A program can test that a file exists with an <code>IF</code> and still fail: the file may be deleted, locked or damaged between the check and the <code>open</code>, or the read may fail part-way through. A <code>try</code> block responds whenever the problem happens.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Giving only an example. "Reasons" needs the reasons: trap errors, stop the halt, meaningful message.</li>
    <li>Describing validation (an <code>IF</code>) as exception handling.</li>
    <li>Saying exception handling "fixes" a bug. It responds to an unexpected event; a logic error still has to be fixed in the code.</li>
    <li>Writing a <code>try</code> block with no message or action in the <code>except</code>.</li>
  </ul>
'''

watch = '''
  <h2>1 · Bad input, handled</h2><p>Press Play, or click the steps. The user types <b>ten</b>.</p><div id="stA"></div>
  <h2>2 · A check is not enough</h2><div id="stB"></div>
  <h2>3 · Exception handling or an IF?</h2><div id="stC"></div>
'''

PS = ['TRY', '   INPUT Age', '   OUTPUT "Next year you will be ", Age + 1', 'EXCEPT', '   OUTPUT "Please enter a whole number"', 'ENDTRY', 'OUTPUT "Finished"']
PY = ['try:', '    Age = int(input("Enter your age: "))', '    print("Next year you will be", Age + 1)', 'except ValueError:', '    print("Please enter a whole number")', 'print("Finished")']
o = lambda *l: [(330, 10 + 24 * i, s, "lbl bd t3" if s != "ValueError raised" else "lbl bd t2") for i, s in enumerate(l)]
stA = stp("stA", "try and except with a bad input", [
    dict(c="The risky statements are inside a <b>try</b> block. The user is going to type <b>ten</b>.", p=0, y=0, v=[("Age", "")], f=[]),
    dict(c="The input is read and Python tries to convert <code>ten</code> to a whole number.", p=1, y=1, v=[("Age", "")], f=[], t=o("ValueError raised")),
    dict(c="The conversion fails, so an exception is raised. The rest of the try block is <b>skipped</b>: the next-year line does not run.", p=2, y=2, v=[("Age", "")], f=[], t=[(330, 10, "ValueError raised", "lbl bd t2"), (330, 34, "line skipped", "sm")]),
    dict(c="The <b>except</b> block matches the exception and takes over.", p=3, y=3, v=[("Age", "")], f=[], t=[(330, 10, "ValueError handled", "lbl bd t2")]),
    dict(c="The user sees a meaningful message, not a system error.", p=4, y=4, v=[("Age", "")], f=[], t=[(330, 10, "Please enter a whole number", "lbl bd t3")]),
    dict(c="The program <b>carries on</b> after the try statement. It did not halt unexpectedly.", p=6, y=5, v=[("Age", "")], f=[], t=[(330, 10, "Please enter a whole number", "lbl bd t3"), (330, 34, "Finished", "lbl bd t3")])],
    PS, PY, lh=24, vw=150, fh=70, dwell=3200)

stB = stp("stB", "Why an IF check can fail", [
    dict(c="A program checks that <code>Data.txt</code> exists before it opens it.", f=[F(20, 20, "Folder", ["Data.txt", "Notes.txt"], w=200, hl=0)], t=[(300, 40, "IF file exists THEN ...", "lbl bd")]),
    dict(c="The check passes: the file is there.", f=[F(20, 20, "Folder", ["Data.txt", "Notes.txt"], w=200, ok=[0])], t=[(300, 40, "IF file exists  ->  TRUE", "lbl bd t3")]),
    dict(c="Before the program reaches <code>open</code>, the file is deleted by the user or another program.", f=[F(20, 20, "Folder", ["Notes.txt"], w=200)], t=[(300, 40, "Data.txt has been deleted", "lbl bd t2")]),
    dict(c="<code>open(\"Data.txt\")</code> fails and the program halts, even though the check passed.", f=[F(20, 20, "Folder", ["Notes.txt"], w=200)], t=[(300, 40, "FileNotFoundError: halted", "lbl bd t2")]),
    dict(c="A <b>try</b> block round the open responds whenever it happens, whatever happened before. The program reports the problem and carries on.", f=[F(20, 20, "Folder", ["Notes.txt"], w=200)], t=[(300, 40, "except: \"File not found\"", "lbl bd t3"), (300, 66, "the program carries on", "sm")])],
    fh=100, dwell=3400)

sc = [("Age must be between 0 and 120", "IF check", "A range check on a value the program already has."), ("Open the file the user names", "Exception handling", "The file may not exist: outside the program's control."), ("Convert typed text to a number", "Exception handling", "The user may type anything."), ("Menu choice must be 1, 2 or 3", "IF check", "A known set of values you can test directly."), ("Disk fills up while saving", "Exception handling", "Hardware: the program cannot rule it out.")]
stC = stp("stC", "Choosing the right tool", [dict(c=f"<b>{a}</b>: use an <b>{b.lower() if b == 'IF check' else b.lower()}</b>. {d}", f=[F(20, 20, "Situation", [a], w=360), F(20, 70, "Use", [b], w=360, ok=[0])]) for a, b, d in sc], fh=125, dwell=3200)

explore = '''
  <h2>Lab 1 · Exception handling or an IF?</h2>
  <p>Choose a situation to see which tool fits and why.</p>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>

  <h2>Lab 2 · Run the program</h2>
  <p>The program asks for an age and prints next year's age. Choose what the user types, then turn exception handling on or off. Try -5 as well.</p>
  <div class="card"><div id="rB" class="btnrow"></div><div class="btnrow"><button class="b" id="rT">Exception handling: off</button></div><div id="rO"></div><div class="verdict" id="rV"></div></div>
'''

lab = r'''
btnTable("dB", "dO", [
  ["Age 0 to 120", "IF check", "The value is known and can be tested against a range."],
  ["Open a named file", "Exception handling", "The file may not exist or may fail to read."],
  ["Convert typed text", "Exception handling", "The user may type text that is not a number."],
  ["Menu choice 1 to 3", "IF check", "The valid values are known, so test them directly."],
  ["Printer disconnected", "Exception handling", "Hardware failure outside the program's control."],
  ["Total is wrong", "Neither: fix the code", "A logic error runs without stopping, so nothing is raised to catch."]
], ["Situation", "Use", "Why"]);

(function () {
  const inputs = ["25", "ten", "-5"]; let cur = 0, on = false;
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur)); $("#rT").textContent = "Exception handling: " + (on ? "on" : "off");
    const t = inputs[cur], n = parseInt(t, 10), bad = isNaN(n); let L = ["Enter your age: " + t];
    if (!bad) { L.push("Next year you will be " + (n + 1)); L.push("Finished"); $("#rV").textContent = n < 0 ? "No exception was raised, but the output is nonsense. A negative age needs an IF check as well." : "The input is valid, so handling makes no difference."; }
    else if (on) { L.push("Please enter a whole number"); L.push("Finished"); $("#rV").textContent = "ValueError raised and handled: the program carries on."; }
    else { L.push("Traceback ... ValueError: invalid literal for int()"); L.push("(program halted: Finished never printed)"); $("#rV").textContent = "ValueError raised and not handled: the program halts."; }
    $("#rO").innerHTML = lineHTML(L);
  };
  $("#rB").innerHTML = inputs.map((x, i) => `<button class="b" data-i="${i}">Type ${x}</button>`).join("");
  $$("#rB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); $("#rT").onclick = () => { on = !on; paint(); }; paint();
})();
''' + CLASSIFY("cl1", "Exception handling or an ordinary IF check?", ["Exception handling", "IF check"],
    [("Opening a file the user names", 0), ("Making sure Age is between 0 and 120", 1), ("Converting typed text with int()", 0), ("Testing a menu choice is 1, 2 or 3", 1), ("Reading a file that might be damaged", 0), ("Checking a list index is less than the length", 1), ("A printer that might be unplugged", 0), ("Making sure a score is not negative", 1)],
    "Exception handling: things outside the program's control. IF: values you can test directly.") + ORDER(
    "Put the steps in order when a bad input meets try and except.",
    ["The program enters the try block", "A statement cannot be carried out", "An exception is raised", "The rest of the try block is skipped", "The matching except block runs", "The program carries on after the try statement"],
    "Try, failure, raise, skip, except, carry on.") + MATCH([
    ["Trap a runtime error", "Catch the error at the moment it happens"], ["Prevent halting", "The program carries on after the problem"], ["Meaningful message", "The user is told what went wrong in plain words"], ["Validation", "An IF check that a value is sensible"], ["Exception handling", "A response to an unexpected event while the program runs"], ["try block", "Holds the statements that might raise the exception"]]) + CALC([
    {"q": "try: print(\"A\"); print(1 / 0); print(\"B\")  except: print(\"C\"). How many lines are printed?", "a": 2, "unit": "", "tol": 0.01, "hint": "A is printed, then the exception, then C.", "sol": "<b>2</b> (A and C)."},
    {"q": "A try block has 5 statements. The second one raises an exception. How many statements of the try block are skipped?", "a": 3, "unit": "", "tol": 0.01, "hint": "Statements 3, 4 and 5.", "sol": "<b>3</b>."},
    {"q": "A loop asks for a number until it is valid. The user types ten, 4x, then 7. How many times does the except block run?", "a": 2, "unit": "", "tol": 0.01, "hint": "ten and 4x both fail.", "sol": "<b>2</b>."},
    {"q": "Of these four: age range, open a file, convert text to a number, menu choice 1 to 3, how many are best handled with exception handling?", "a": 2, "unit": "", "tol": 0.01, "hint": "Opening a file and converting text.", "sol": "<b>2</b>."},
    {"q": "How many reasons for using exception handling does this page give?", "a": 3, "unit": "", "tol": 0.01, "hint": "Trap, prevent halting, meaningful message.", "sol": "<b>3</b>."}]) + MCQ([
    ("What is a reason for using exception handling?", ["To make code run faster", "To prevent the program halting unexpectedly", "To remove logic errors", "To skip validation"], 1, "It stops an unexpected halt."),
    ("Which is best handled by an IF check?", ["Opening a file", "A value that must be between 1 and 10", "A lost network connection", "Converting text to a number"], 1, "A range is known and can be tested."),
    ("What does the except block normally contain?", ["The risky statements", "The response to the exception", "The input", "The loop"], 1, "It says what to do."),
    ("Why is checking a file exists first not always enough?", ["IF is slow", "It may be deleted or fail after the check", "IF cannot test files", "Files cannot be opened"], 1, "Things change between the check and the open."),
    ("What happens to the statements after the failing one in a try block?", ["They run", "They are skipped", "They run twice", "They run first"], 1, "Control jumps to except."),
    ("A negative age is typed and int() accepts it. Which tool catches this?", ["try and except", "An IF range check", "Neither", "finally"], 1, "No exception is raised; it is a validation matter.")], "qz1") + CARDS([
    ("Exception handling", "Responds to an unexpected event so the program does not halt."), ("Reason 1", "Trap runtime errors."), ("Reason 2", "Stop the program halting unexpectedly."), ("Reason 3", "Give a meaningful message or recover."),
    ("Use it for", "Files, typed conversions, hardware and network problems."), ("Use IF for", "Ranges, menus and known values."), ("Validation", "An IF check that data is sensible."), ("Not a bug fix", "A logic error is fixed in the code.")])

real = RWNOTE + (
    rw("A web form that asks for a quantity", "If a customer types ten instead of 10, the conversion would normally crash the page. The code catches the error and shows 'Please enter a whole number'.", "meaningful message instead of a system error.") +
    rw("A spreadsheet opening a missing file", "When a linked file has been moved the program says it cannot find the file and offers to browse for it, instead of closing.", "the program carries on after the problem.") +
    rw("A game saving to a full disk", "The save fails. The game reports it and keeps running, so the player does not lose progress held in memory.", "stops the program halting; protects the data.") +
    rw("A banking program with a range check", "An account balance that must not be negative is checked with an IF before it is saved. This is not an exception: the program already has the value and can test it.", "validation uses IF, not try.") +
    rw("An app that loses its connection", "A download stops when the Wi-Fi drops. The app catches the connection error, tells the user and lets them retry.", "failure outside the program's control, reported rather than crashing."))

review = (
    req("3 marks", "State", "State three reasons for including exception handling in a program.", "One mark each.", mks(["To trap runtime errors", "To prevent the program halting unexpectedly", "To give a meaningful error message instead of a system message"])) +
    req("2 marks", "Explain", "A program asks the user to type their age. Explain why <code>int(input())</code> should be inside a try block.", "What the user might type.", mks(["The user may type something that is not a whole number, so the conversion can raise an exception", "the except block can show a message and let the program carry on instead of halting"])) +
    req("4 marks", "Write", "Write Python that keeps asking for an age until a whole number from 0 to 120 is entered.", "int() in a try; the range in an IF.", pc('''Valid = False
while not Valid:
    try:
        Age = int(input("Enter your age: "))
        if Age < 0 or Age > 120:
            print("Age must be between 0 and 120")
        else:
            Valid = True
    except ValueError:
        print("Please enter a whole number")'''), "Using only try and except, so an age of -5 is accepted.") +
    req("2 marks", "Explain", "A programmer checks a file exists with an IF before opening it. Explain why exception handling may still be needed.", "What can change after the check.", mks(["The file could be deleted, locked or damaged after the check and before it is opened", "or fail part-way through reading, so the program could still halt"])) +
    req("2 marks", "Explain", "Explain why a range check on a score would use an IF, not exception handling.", "Is anything unexpected?", mks(["The value is already in the program and its valid range is known", "so it can be tested directly; no unexpected event occurs for an exception to catch"])))

where = [("M/J 2022", "32", "9", "4", "State the reasons for including exception handling, with an example"),
         ("O/N 2025", "31", "10", "3", "Explain exception handling with an example of a cause"),
         ("O/N 2025", "32", "10(a), 10(b)", "2 + 2", "Describe how termination due to an exception is avoided; identify two causes")]
past = "".join(OLDQ[k] for k in ["M/J 2022 · 9618/32 · Q9", "O/N 2025 · 9618/31 · Q10", "O/N 2025 · 9618/32 · Q10"])
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Why exception handling is used is a short Paper 3 theory question. Paper 4 expects it written round file work, which is on the last page of this section."

tipsl = [("Give the reasons.", "Trap errors, prevent halting, meaningful message. An example alone is not enough."), ("Say 'unexpected'.", "Exception handling responds to unexpected events while the program runs."), ("Use try for the outside world.", "Files, typed input, devices, networks."), ("Use IF for known values.", "Ranges and menus are validation."), ("Always add a response.", "An except block needs a message or action."), ("Name how to avoid termination.", "A try ... except block, or an error message.")]
sents = [("State the purpose", "Exception handling responds to unexpected events while a program runs, to prevent it stopping unexpectedly."), ("State the benefit", "It gives the user a meaningful message instead of a system error and lets the program carry on."), ("Say how to avoid termination", "Use a try ... except routine to catch the exception.")]
words = [("State", "Give each reason briefly: one mark each."), ("Explain", "A reason as well as the fact."), ("Describe", "Say how it works in connected points."), ("Write", "Produce Python with try, except and a message.")]

finishf("ac20x2", "ac-20-2-2-why-and-when-exception-handling", "Why and When to Use Exception Handling",
        "The three reasons, the situations where try and except is the right tool and where an IF is better, and why checking first is not always enough; pseudocode and Python side by side, with step-by-step animations.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words, sub_num="20.2.2")
