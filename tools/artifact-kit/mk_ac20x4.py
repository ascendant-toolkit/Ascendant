"""20.2.2 extra resource: exception handling when using files. Run: python3 tools/artifact-kit/mk_ac20x4.py"""
from ac20f import *

OLDQ = old_questions("mk_ac2022.py")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Files are the most common place for an exception, because the program depends on something outside itself: the file may not exist, may be unreadable, or may contain data in the wrong form. In Paper 4, a question that says <b>use exception handling</b> awards a mark or two for a <code>try</code> block round the file work and an <code>except</code> block with an <b>appropriate message</b>. The whole of the <b>open, read or write, and close</b> goes inside the <code>try</code>, so a problem at any stage is caught. A named <code>except IOError</code> catches file problems only, so a bad line such as <code>abc</code> (a <code>ValueError</code>) needs a bare <code>except</code> or a second block. A <code>finally</code> block can close the file whatever happened.</p></div>

  <h2>1 · What can go wrong with a file</h2>
  <div class="tw"><table class="t">
    <tr><th>Problem</th><th>Cause</th><th>Python exception</th></tr>
    <tr><td>The file does not exist</td><td>User error: wrong name or folder</td><td><code>FileNotFoundError</code> (an <code>IOError</code>)</td></tr>
    <tr><td>The file cannot be read or written</td><td>Hardware or system failure: damaged, locked, disk full</td><td><code>OSError</code> / <code>IOError</code></td></tr>
    <tr><td>A line is not a number</td><td>Data error: <code>abc</code>, or a blank line, given to <code>int()</code></td><td><code>ValueError</code></td></tr>
  </table></div>

  <h2>2 · Reading a file into an array</h2>
  <p>The file <code>Data.txt</code> holds whole numbers, one per line. The array is filled inside the try.</p>
  ''' + both('''DataArray = []
try:
    DataFile = open("Data.txt", "r")
    for Line in DataFile:
        DataArray.append(int(Line))
    DataFile.close()
except IOError:
    print("Could not find file")''', '''Index <- 0
TRY
   OPENFILE "Data.txt" FOR READ
   WHILE NOT EOF("Data.txt")
      READFILE "Data.txt", Line
      DataArray[Index] <- STR_TO_NUM(Line)
      Index <- Index + 1
   ENDWHILE
   CLOSEFILE "Data.txt"
EXCEPT
   OUTPUT "Could not find file"
ENDTRY''') + '''

  <h2>3 · Where the try goes</h2>
  <div class="tw"><table class="t">
    <tr><th>Placement</th><th>Result</th></tr>
    <tr><td><code>try</code> round the whole open, loop and close</td><td>A problem at any stage is caught. This is the mark-scheme pattern</td></tr>
    <tr><td><code>try</code> round only the <code>open</code></td><td>A bad line while reading is not caught, so the program can still halt</td></tr>
    <tr><td>No <code>try</code> at all</td><td>The program halts with a system message and the exception-handling marks are lost</td></tr>
  </table></div>

  <h2>4 · Writing a file</h2>
  ''' + both('''try:
    File = open("Tree.txt", "w")
    File.write("-1,20,1\\n")
    File.close()
except IOError:
    print("Cannot write to file")''', '''TRY
   OPENFILE "Tree.txt" FOR WRITE
   WRITEFILE "Tree.txt", "-1,20,1"
   CLOSEFILE "Tree.txt"
EXCEPT
   OUTPUT "Cannot write to file"
ENDTRY''') + '''

  <h2>5 · Catching a bad line as well</h2>
  <p>With <code>except IOError</code>, a line containing <code>abc</code> raises a <code>ValueError</code>, which does not match, so the program halts. Catch it too:</p>
  <div class="code">''' + pc('''try:
    DataFile = open("Data.txt", "r")
    for Line in DataFile:
        DataArray.append(int(Line))
    DataFile.close()
except (IOError, ValueError):         # or a bare:  except:
    print("Problem reading the file")''') + '''</div>

  <h2>6 · Closing the file with finally</h2>
  <p>If an exception is raised part-way through reading, the line that closes the file is skipped. A <code>finally</code> block always runs, so it can close the file whatever happened. Python needs to check the file was opened first.</p>
  ''' + both('''DataFile = None
try:
    DataFile = open("Data.txt", "r")
    Line = DataFile.readline()
except IOError:
    print("Problem with the file")
finally:
    if DataFile is not None:
        DataFile.close()''', '''TRY
   OPENFILE "Data.txt" FOR READ
   READFILE "Data.txt", Line
EXCEPT
   OUTPUT "Problem with the file"
FINALLY
   CLOSEFILE "Data.txt"
ENDTRY''') + '''

  <h2>7 · What Paper 4 awards marks for</h2>
  <div class="tw"><table class="t">
    <tr><th>Mark point</th><th>In the code</th></tr>
    <tr><td>The <code>try</code> structure round the file work</td><td><code>try:</code> before <code>open</code>, with the loop and the close inside</td></tr>
    <tr><td>An <code>except</code> block</td><td><code>except IOError:</code> or <code>except:</code></td></tr>
    <tr><td>An appropriate message</td><td><code>print("File not found")</code></td></tr>
    <tr><td>The file work itself</td><td>Open for the right mode, loop, convert each line, store, close</td></tr>
  </table></div>

  <h2>8 · Common ways to lose marks</h2>
  <ul>
    <li>A <code>try</code> round only the <code>open</code>, leaving the reading unprotected.</li>
    <li>An <code>except</code> with no message.</li>
    <li>Closing the file outside the structure, so it is skipped when an exception is raised.</li>
    <li>Using <code>except IOError</code> and expecting it to catch <code>int(Line)</code> failing.</li>
    <li>Forgetting <code>int()</code>, so the array holds strings.</li>
    <li>Leaving out the exception handling when the question says to use it.</li>
  </ul>
'''

watch = '''
  <h2>1 · The file does not exist</h2><p>Press Play, or click the steps. Both versions of the code are highlighted together.</p><div id="stA"></div>
  <h2>2 · A bad line in the file</h2><p>The file exists, but its third line is <code>abc</code>. The handler is <code>except IOError</code>.</p><div id="stB"></div>
  <h2>3 · Where the try goes</h2><div id="stC"></div>
'''

PS = ['TRY', '   OPENFILE "Data.txt" FOR READ', '   WHILE NOT EOF("Data.txt")', '      READFILE "Data.txt", Line', '      DataArray[Index] <- STR_TO_NUM(Line)', '      Index <- Index + 1', '   ENDWHILE', '   CLOSEFILE "Data.txt"', 'EXCEPT', '   OUTPUT "Could not find file"', 'ENDTRY']
PY = ['try:', '    DataFile = open("Data.txt", "r")', '    for Line in DataFile:', '        DataArray.append(int(Line))', '    DataFile.close()', 'except IOError:', '    print("Could not find file")']
ot = lambda *l: [(330, 10 + 24 * i, s, c) for i, (s, c) in enumerate(l)]
G, B = "lbl bd t3", "lbl bd t2"
stA = stp("stA", "Opening a file that does not exist", [
    dict(c="The program is about to read <code>Data.txt</code>, but the user's folder has no file with that name.", p=-1, y=-1, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200)]),
    dict(c="The try block starts.", p=0, y=0, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200)]),
    dict(c="The open fails: there is no file called <code>Data.txt</code>. A <b>FileNotFoundError</b> is raised.", p=1, y=1, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200, no=[0, 1])], t=[(330, 10, "FileNotFoundError", B)]),
    dict(c="The loop and the close are <b>skipped</b>: they are inside the try block, after the failing statement.", p=-1, y=-1, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200)], t=[(330, 10, "FileNotFoundError", B), (330, 34, "loop and close skipped", "sm")]),
    dict(c="<code>except IOError</code> matches (FileNotFoundError is an IOError), so the response runs.", p=8, y=5, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200)], t=[(330, 10, "FileNotFoundError", B)]),
    dict(c="The user sees a meaningful message and the program carries on, instead of halting.", p=9, y=6, v=[("Line", ""), ("DataArray", "[]")], f=[F(20, 0, "Folder", ["Notes.txt", "Scores.txt"], w=200)], t=ot(("Could not find file", G), ("the program carries on", "sm")))],
    PS, PY, lh=22, vw=190, fh=70, dwell=3200)

rows = ["12", "7", "abc"]
fc = lambda hl=None, ok=None, no=None, ptr=None: [F(20, 0, "Data.txt", rows, w=200, hl=hl, ok=ok, no=no, ptr=ptr, ptrLabel="next read")]
stB = stp("stB", "A bad line with except IOError", [
    dict(c="<code>Data.txt</code> exists. Its lines are 12, 7 and <b>abc</b>. The handler is <code>except IOError</code>.", p=-1, y=-1, v=[("Line", ""), ("DataArray", "[]")], f=fc()),
    dict(c="The file opens without a problem.", p=1, y=1, v=[("Line", ""), ("DataArray", "[]")], f=fc(ptr=0)),
    dict(c="Line 1 is read and <code>int(\"12\")</code> works. 12 is stored.", p=4, y=3, v=[("Line", "12"), ("DataArray", "[12]")], f=fc(hl=0, ptr=1)),
    dict(c="Line 2: 7 is stored.", p=4, y=3, v=[("Line", "7"), ("DataArray", "[12, 7]")], f=fc(hl=1, ok=[0], ptr=2)),
    dict(c="Line 3: <code>int(\"abc\")</code> cannot be converted. A <b>ValueError</b> is raised.", p=4, y=3, v=[("Line", "abc"), ("DataArray", "[12, 7]")], f=fc(no=[2], ok=[0, 1]), t=[(330, 10, "ValueError", B)]),
    dict(c="Python looks for a matching except. <code>except IOError</code> does <b>not</b> match a ValueError.", p=8, y=5, v=[("Line", "abc"), ("DataArray", "[12, 7]")], f=fc(no=[2], ok=[0, 1]), t=[(330, 10, "ValueError: no match", B)]),
    dict(c="Nothing handles it, so the program <b>halts</b>, with the file still open. A bare <code>except:</code> or <code>except (IOError, ValueError):</code> would have caught it.", p=-1, y=-1, v=[("Line", "abc"), ("DataArray", "[12, 7]")], f=fc(no=[2], ok=[0, 1]), t=[(330, 10, "Program halted", B)])],
    PS, PY, lh=22, vw=190, fh=100, dwell=3400)

BAD = ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "except IOError:", "    print(\"No file\")", "for Line in DataFile:", "    DataArray.append(int(Line))"]
GOOD = ["try:", "    DataFile = open(\"Data.txt\", \"r\")", "    for Line in DataFile:", "        DataArray.append(int(Line))", "    DataFile.close()", "except:", "    print(\"Problem with the file\")"]
stC = stp("stC", "Where the try goes", [
    dict(c="Two versions of the same file read. The left one puts the <code>try</code> round the <code>open</code> only.", f=[F(20, 20, "Try round open only", BAD, w=350), F(390, 20, "Try round open, loop and close", GOOD, w=350)]),
    dict(c="On the left, if the file is missing the <code>open</code> fails and is caught. Good so far.", f=[F(20, 20, "Try round open only", BAD, w=350, ok=[1, 2, 3]), F(390, 20, "Try round open, loop and close", GOOD, w=350)]),
    dict(c="But if a line is <code>abc</code>, the failing <code>int()</code> is <b>outside</b> the try. Nothing catches it, so the program halts.", f=[F(20, 20, "Try round open only", BAD, w=350, no=[5]), F(390, 20, "Try round open, loop and close", GOOD, w=350)]),
    dict(c="On the right the loop and the close are inside the try, so a failure at <b>any</b> stage reaches the except block.", f=[F(20, 20, "Try round open only", BAD, w=350), F(390, 20, "Try round open, loop and close", GOOD, w=350, ok=[1, 2, 3, 4, 5, 6])])],
    fh=215, dwell=3600)

explore = '''
  <h2>Lab 1 · Read the file</h2>
  <p>Choose the file and the handler. The program reads the numbers into an array.</p>
  <div class="card"><div id="fB" class="btnrow"></div><div id="hB" class="btnrow"></div><div id="fO"></div><div class="verdict" id="fV"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

lab = r'''
(function () {
  const files = [["File with 12, 7, 30", [12, 7, 30], false], ["File missing", null, true], ["File with 12, 7, abc", [12, 7, "abc"], false]];
  const hs = ["No handling", "except IOError", "except (bare)"];
  let f = 0, h = 1;
  const paint = () => {
    $$("#fB button").forEach((b, i) => b.classList.toggle("pri", i === f)); $$("#hB button").forEach((b, i) => b.classList.toggle("pri", i === h));
    const d = files[f][1]; let out = [], arr = [], msg = "";
    const caught = (kind) => h === 2 || (h === 1 && kind === "io");
    if (d === null) { if (caught("io")) { out.push('"Could not find file"'); msg = "FileNotFoundError is an IOError, so the handler catches it and the program carries on."; } else { out.push("Program halted: FileNotFoundError"); msg = "Nothing handles the exception, so the program halts."; } }
    else {
      for (const v of d) { if (typeof v === "string") { if (caught("value")) { out.push('"Problem reading the file"'); msg = "The ValueError was caught, and the program carries on with the numbers read so far."; } else { out.push("Program halted: ValueError"); msg = h === 1 ? "except IOError does not match a ValueError, so the program halts." : "Nothing handles the exception, so the program halts."; } break; } arr.push(v); }
      if (!out.length) msg = "No exception was raised, so the handler is not used.";
    }
    $("#fO").innerHTML = lineHTML(["DataArray = " + (d === null ? "[]" : "[" + arr.join(", ") + "]"), ...out.map((o) => "Output: " + o)]);
    $("#fV").textContent = msg;
  };
  $("#fB").innerHTML = files.map((x, i) => `<button class="b" data-i="${i}">${x[0]}</button>`).join(""); $("#hB").innerHTML = hs.map((x, i) => `<button class="b" data-i="${i}">${x}</button>`).join("");
  $$("#fB button").forEach((b) => (b.onclick = () => { f = +b.dataset.i; paint(); })); $$("#hB button").forEach((b) => (b.onclick = () => { h = +b.dataset.i; paint(); })); paint();
})();
btnTable("mB", "mO", [
  ["Try only round open", "try:\n    F = open(\"Data.txt\")\nexcept IOError: ...\nfor L in F: ...", "A bad line or failed read is outside the try, so the program can still halt", "Put the loop and close inside the try"],
  ["No message", "except IOError:\n    pass", "The user is told nothing and the message mark is lost", "print(\"Could not find file\")"],
  ["Close outside", "try: ... \nexcept: ...\nF.close()", "If the open failed, F does not exist and close() raises an error", "Close inside the try, or in a finally that checks the file opened"],
  ["Wrong exception", "except IOError:  # for int(Line)", "A ValueError does not match IOError", "except: or except (IOError, ValueError):"],
  ["No conversion", "DataArray.append(Line)", "The array holds strings, not integers", "DataArray.append(int(Line))"],
  ["Wrong mode", "open(\"Data.txt\", \"w\")  # to read", "Opening to write erases the file instead of reading it", "open(\"Data.txt\", \"r\")"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Where does each part of a file read go?", ["Inside the try", "In the except block", "Outside the structure"],
    [("Opening the file", 0), ("The loop that reads each line", 0), ("int(Line) to convert", 0), ("Closing the file after reading", 0), ("The message Could not find file", 1), ("DataArray = [] before the try", 2), ("The program carrying on afterwards", 2), ("print(\"Problem with the file\")", 1)],
    "The file work goes inside the try, the message goes in the except, and set-up lines sit before the structure.") + ORDER(
    "Put the steps in order for reading a file with exception handling.",
    ["Start the try block", "Open the file for reading", "Read each line and convert it", "Close the file", "If anything fails, the except block runs", "Output an appropriate message"],
    "Try, open, read and convert, close; on failure, except and message.") + MATCH([
    ["FileNotFoundError", "Raised when the file to be opened does not exist"], ["IOError", "A file input or output problem; the usual except for file work"], ["ValueError", "Raised when int(Line) is given text that is not a number"], ["finally", "Runs whatever happened, so it can close the file"], ["Bare except", "Catches every exception, including a bad line"], ["Appropriate message", "A mark point: tell the user what went wrong"]]) + CALC([
    {"q": "A file has 25 lines. The 10th is abc and the handler is a bare except. How many numbers are in the array when the handler runs?", "a": 9, "unit": "", "tol": 0.01, "hint": "Lines 1 to 9 were converted.", "sol": "<b>9</b>."},
    {"q": "The file is missing. How many lines are read before the except block runs?", "a": 0, "unit": "", "tol": 0.01, "hint": "The open fails, so nothing is read.", "sol": "<b>0</b>."},
    {"q": "A file of 100 numbers has a blank line as line 60 and the handler is a bare except. int(\"\") fails. How many numbers are stored?", "a": 59, "unit": "", "tol": 0.01, "hint": "Lines 1 to 59.", "sol": "<b>59</b>."},
    {"q": "The handler is except IOError and line 5 is abc. How many numbers are stored when the program halts?", "a": 4, "unit": "", "tol": 0.01, "hint": "Lines 1 to 4.", "sol": "<b>4</b>."},
    {"q": "A file of 50 numbers is read with no problems. How many times does the except block run?", "a": 0, "unit": "", "tol": 0.01, "hint": "No exception is raised.", "sol": "<b>0</b>."}]) + MCQ([
    ("Where should the file open, loop and close be placed?", ["Before the try", "Inside the try block", "Inside the except block", "After the program"], 1, "A problem at any stage is then caught."),
    ("What does except IOError NOT catch?", ["A missing file", "A damaged file", "int(\"abc\") failing", "A disk error"], 2, "That is a ValueError."),
    ("What is an appropriate message?", ["Nothing", "A statement telling the user what went wrong", "The array", "The file name only"], 1, "For example Could not find file."),
    ("Why might a file be left open after an exception?", ["Python never closes files", "The close line was skipped when the exception happened", "Files close themselves", "except closes files"], 1, "A finally block closes it either way."),
    ("A question says use exception handling. What is lost if you do not?", ["Nothing", "The marks for try and except", "The marks for the loop", "The marks for the open"], 1, "It is a mark point."),
    ("Which mode opens a file to read?", ["\"w\"", "\"a\"", "\"r\"", "\"x\""], 2, "r is read.")], "qz1") + CARDS([
    ("try round the file work", "Open, loop and close all go inside the try."), ("except IOError", "Catches file problems, including a missing file."), ("Bare except", "Catches everything, including a bad line."), ("Message", "Tell the user what went wrong."),
    ("finally", "Close the file whatever happened."), ("int(Line)", "Lines are strings: convert them."), ("FileNotFoundError", "The file does not exist."), ("ValueError", "int() was given text that is not a number.")])

real = RWNOTE + (
    rw("A save game that cannot be found", "When a player presses Load and the save file has been deleted, the game says it cannot find the save and returns to the menu instead of closing.", "file not found caught, with a message.") +
    rw("A spreadsheet import with a bad row", "A column of numbers has a text entry in row 40. The import stops at that row, reports it, and keeps the 39 rows already read.", "a ValueError during reading needs handling as well as the open.") +
    rw("A log written to a full disk", "A write fails when there is no space. The program reports the failure and carries on instead of crashing.", "hardware or system failure while writing.") +
    rw("A database connection", "Whether the query worked or not, the connection is closed afterwards so it does not stay open.", "finally closes the resource whatever happened.") +
    rw("A school mark file", "A teacher's program reads marks from a file. If the file is missing it asks for another file name rather than stopping.", "except with a recovery action."))

review = (
    req("4 marks", "Write", "The text file <code>Scores.txt</code> stores 50 integers, one on each line. Write Python to read them into the list <code>Scores</code>. Use exception handling.", "Try round open, loop and close; except with a message.", pc('''Scores = []
try:
    File = open("Scores.txt", "r")
    for Line in File:
        Scores.append(int(Line))
    File.close()
except IOError:
    print("Could not read the file")'''), "Putting the try only round the open.") +
    req("3 marks", "Write", "Write Python that writes each name in the list <code>Names</code> on its own line to <code>Names.txt</code>. Use exception handling.", "Open to write, loop with a new line, close, all in the try.", pc('''try:
    File = open("Names.txt", "w")
    for Name in Names:
        File.write(Name + "\\n")
    File.close()
except IOError:
    print("Could not write to the file")'''), "Forgetting the new line so all the names run together.") +
    req("2 marks", "Explain", "Explain why the loop and the close are inside the try block and not only the open.", "What else can fail?", mks(["A problem can occur while reading or converting a line, not just when opening", "so the whole file work is protected and the program does not halt"])) +
    req("2 marks", "Explain", "A file read uses <code>except IOError</code>. One line holds <code>abc</code> and is converted with <code>int()</code>. Explain what happens.", "Which exception?", mks(["int() raises a ValueError, which is not an IOError", "so the except block does not run and the program halts"])) +
    req("3 marks", "Write", "Write exam pseudocode that opens <code>Data.txt</code> to read, reads one line, outputs a message if there is a problem, and always closes the file.", "TRY, EXCEPT, FINALLY, ENDTRY.", pc('''TRY
   OPENFILE "Data.txt" FOR READ
   READFILE "Data.txt", Line
EXCEPT
   OUTPUT "Problem with the file"
FINALLY
   CLOSEFILE "Data.txt"
ENDTRY'''), "Putting CLOSEFILE inside the try, where it is skipped by an exception."))

where = [("M/J 2023", "41, 43", "1(a)(ii)", "1 + 4", "Read 25 integers from Data.txt into an array with exception handling"),
         ("O/N 2025", "42", "3(c)", "4", "Read 50 integers from TreeData.txt into a binary tree, with exception handling"),
         ("M/J 2026", "42", "2(b)", "7 + 1", "LoadAvatars(): read objects from AvatarFile.txt with exception handling")]
past = "".join(OLDQ[k] for k in ["M/J 2023 · 9618/41, 43 · Q1(a)", "O/N 2025 · 9618/42 · Q3(c)", "M/J 2026 · 9618/42 · Q2(b)"])
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. In Paper 4 the exception handling is a mark point inside a file question, and appears in most papers; further examples are on the main 20.2.2 page. Paper 3 asks about exceptions in words, not as file code."

tipsl = [("Whole file work inside.", "Open, loop and close all go inside the try."), ("Add a message.", "An except with no message or action loses the mark."), ("Match the exception.", "IOError for files, ValueError for int(). Or use a bare except."), ("Convert each line.", "int(Line) before storing numbers."), ("Close properly.", "Inside the try, or in finally."), ("Read the question.", "If it says use exception handling, it is a mark point.")]
sents = [("Write the structure", "try: open the file, loop through the lines, convert and store each one, close the file. except: output a message."), ("Say why a file needs it", "The file might not exist or might be unreadable, which the program cannot control."), ("Say what a bad line does", "int() raises a ValueError, so the handler must catch it as well as file errors.")]
words = [("Write program code", "Produce Python that opens, reads or writes, closes, with try and except."), ("Explain", "A reason as well as the fact."), ("State", "A fact or the exception name."), ("Complete", "Fill in the missing lines of the given code.")]

finishf("ac20x4", "ac-20-2-2-exception-handling-files", "Exception Handling When Using Files",
        "What can go wrong with a file, where the try block goes, catching a bad line as well as a missing file, and closing with finally; pseudocode and Python side by side, with line-by-line animations.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words, sub_num="20.2.2")
