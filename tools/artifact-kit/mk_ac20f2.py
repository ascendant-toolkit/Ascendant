"""20.2.1 extra resource: adding a record to a sequential file. Run: python3 tools/artifact-kit/mk_ac20f2.py"""
from ac20f import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>sequential file</b> keeps its records in order of a <b>key field</b>, so a new record cannot simply be added to the end: it has to go in its <b>key position</b>. A text file cannot have a line pushed in the middle, so the program makes a <b>new version</b> of the file. It reads the old file one record at a time and copies each to a <b>new file</b>, and when it reaches the first record whose key is <b>larger</b> than the new key it writes the new record first. If no record is larger, the new record is written <b>after the loop</b>, at the end. Finally the old file is deleted and the new file renamed to take its place.</p></div>

  <h2>1 · Why not just append?</h2>
  <p>Appending 130 to a file that holds 101, 115, 142, 160 gives 101, 115, 142, 160, 130. The file is no longer in key order, so it is no longer sequential: a search that stops when it passes the key would now give wrong answers. The record has to be placed <b>between 115 and 142</b>.</p>

  <h2>2 · The record format used on this page</h2>
  <p>Each record is one line, as on the previous page. The key is the <b>first three characters</b>: every StudentID has exactly 3 digits, so the key can be cut out with <code>LEFT(Line, 3)</code> in pseudocode, or <code>Line.split(",")[0]</code> in Python.</p>
  <div class="code">''' + pc('''101,Ana,58
115,Bo,66
142,Cy,71
160,Di,49''') + '''</div>

  <h2>3 · The algorithm</h2>
  <p>The new record is <code>NewLine</code> and its key is <code>NewKey</code>. <code>Placed</code> remembers whether the new record has been written yet, so it is written only once.</p>
  ''' + both('''import os
NewKey = 130
NewLine = "130,Dev,64\\n"
Placed = False

Old = open("Students.txt", "r")
New = open("NewStudents.txt", "w")
for Line in Old:
    Key = int(Line.split(",")[0])
    if not Placed and Key > NewKey:
        New.write(NewLine)
        Placed = True
    New.write(Line)
if not Placed:
    New.write(NewLine)
Old.close()
New.close()
os.replace("NewStudents.txt", "Students.txt")''', '''NewKey <- 130
NewLine <- "130,Dev,64"
Placed <- FALSE

OPENFILE "Students.txt" FOR READ
OPENFILE "NewStudents.txt" FOR WRITE
WHILE NOT EOF("Students.txt")
   READFILE "Students.txt", Line
   Key <- STR_TO_NUM(LEFT(Line, 3))
   IF NOT Placed AND Key > NewKey THEN
      WRITEFILE "NewStudents.txt", NewLine
      Placed <- TRUE
   ENDIF
   WRITEFILE "NewStudents.txt", Line
ENDWHILE
IF NOT Placed THEN
   WRITEFILE "NewStudents.txt", NewLine
ENDIF
CLOSEFILE "Students.txt"
CLOSEFILE "NewStudents.txt"
// delete Students.txt, then rename NewStudents.txt to Students.txt''') + '''
  <div class="tip"><b class="h">Two files are open at once</b>The old file is opened <code>FOR READ</code> and the new file <code>FOR WRITE</code>. Both must be closed before the old one is replaced. Python's <code>os.replace()</code> does the delete and rename in one step.</div>

  <h2>4 · What each part does</h2>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Job</th></tr>
    <tr><td><code>Key &gt; NewKey</code></td><td>True at the first record that should come <b>after</b> the new one. Records with a smaller key are copied untouched</td></tr>
    <tr><td><code>Placed</code></td><td>Stops the new record being written again at every later record</td></tr>
    <tr><td><code>New.write(Line)</code></td><td>Copies the record just read. It runs every time round the loop, after any insertion</td></tr>
    <tr><td><code>IF NOT Placed</code> after the loop</td><td>Catches the case where the new key is larger than every key in the file</td></tr>
    <tr><td>Replace the file</td><td>The new version becomes the file the program uses from now on</td></tr>
  </table></div>

  <h2>5 · The three cases</h2>
  <div class="tw"><table class="t">
    <tr><th>New key</th><th>Where it is written</th><th>Which line does it</th></tr>
    <tr><td>Smaller than the first key (100)</td><td>Before the first record</td><td>The <code>IF</code> inside the loop, on the very first record</td></tr>
    <tr><td>Between two keys (130)</td><td>Between them</td><td>The <code>IF</code> inside the loop, at the first larger key</td></tr>
    <tr><td>Larger than every key (200)</td><td>After the last record</td><td>The <code>IF NOT Placed</code> after the loop</td></tr>
  </table></div>

  <h2>6 · The same pattern changes and deletes records</h2>
  <p>Copy every record to a new file, but <b>leave out</b> the record to delete, or <b>write a changed version</b> of it instead. For a small file, an alternative is to read the records into an array, insert the new record in the right position, and write the whole array back with <code>FOR WRITE</code>.</p>

  <h2>7 · Common ways to lose marks</h2>
  <ul>
    <li>Appending the record. That breaks the key order.</li>
    <li>Opening the same file for reading and writing at once. The update is done through a second file.</li>
    <li>Writing the new record every time the key is larger. <code>Placed</code> must stop it after the first.</li>
    <li>Forgetting the check after the loop, so a record with the largest key is lost.</li>
    <li>Leaving out the copy of the record just read, so existing records disappear.</li>
    <li>Forgetting to close both files before replacing the old one.</li>
  </ul>
'''

watch = '''
  <h2>1 · Why appending breaks the order</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Inserting 130 into the file, line by line</h2><p>Both versions of the code are highlighted together. Watch the pointer in the old file and the new file filling up.</p><div id="stB"></div>
  <h2>3 · A key smaller than every record (100)</h2><div id="stC"></div>
  <h2>4 · A key larger than every record (200)</h2><div id="stD"></div>
'''

OLD_ROWS = ["101,Ana,58", "115,Bo,66", "142,Cy,71", "160,Di,49"]
NEWLINE = "130,Dev,64"
stA = stp("stA", "Appending breaks the key order", [
    dict(c="The sequential file holds four records in key order: 101, 115, 142, 160.", f=[F(20, 20, "Students.txt", OLD_ROWS, ok=[0, 1, 2, 3])]),
    dict(c="A new record with key 130 arrives. If it is appended it goes after 160.", f=[F(20, 20, "Students.txt", OLD_ROWS + [NEWLINE], no=[4])], t=[(300, 62, "130 comes after 160: out of order", "lbl bd t2")]),
    dict(c="The file is no longer in key order. A search that stops when it passes the key would give the wrong answer.", f=[F(20, 20, "Students.txt", OLD_ROWS + [NEWLINE], no=[4])], t=[(300, 62, "A search for 130 stops at 142 and says it is missing", "lbl bd t2")]),
    dict(c="It belongs between 115 and 142. A text file cannot have a line pushed into the middle, so the whole file is copied into a new one with 130 in the right place.", f=[F(20, 20, "Students.txt", OLD_ROWS, ok=[0, 1, 2, 3]), F(300, 20, "NewStudents.txt", ["101,Ana,58", "115,Bo,66", NEWLINE, "142,Cy,71", "160,Di,49"], nw=2)])],
    fh=170, dwell=3600)

PS = ['Placed <- FALSE', 'OPENFILE "Students.txt" FOR READ', 'OPENFILE "NewStudents.txt" FOR WRITE', 'WHILE NOT EOF("Students.txt")', '   READFILE "Students.txt", Line', '   Key <- STR_TO_NUM(LEFT(Line, 3))', '   IF NOT Placed AND Key > NewKey THEN', '      WRITEFILE "NewStudents.txt", NewLine', '      Placed <- TRUE', '   ENDIF', '   WRITEFILE "NewStudents.txt", Line', 'ENDWHILE', 'IF NOT Placed THEN', '   WRITEFILE "NewStudents.txt", NewLine', 'ENDIF', 'CLOSEFILE "Students.txt"', 'CLOSEFILE "NewStudents.txt"', '// delete the old file, rename the new one']
PY = ['Placed = False', 'Old = open("Students.txt", "r")', 'New = open("NewStudents.txt", "w")', 'for Line in Old:', '    Key = int(Line.split(",")[0])', '    if not Placed and Key > NewKey:', '        New.write(NewLine)', '        Placed = True', '    New.write(Line)', 'if not Placed:', '    New.write(NewLine)', 'Old.close()', 'New.close()', 'os.replace("NewStudents.txt", "Students.txt")']


def trace(newkey, newline, old):
    """Simulate the insert and return one step per line that matters."""
    steps, new, placed, key, line = [], [], False, "", ""
    v = lambda: [("NewKey", str(newkey)), ("Placed", "TRUE" if placed else "FALSE"), ("Key", str(key)), ("Line", line)]
    cols = lambda i=None, ptr=None, nw=None, eof=False: [F(20, 0, "Students.txt (old)", old, hl=i, ptr=ptr, ptrLabel="next read", eof=eof), F(390, 0, "NewStudents.txt (new)", new, nw=nw)]
    steps.append(dict(c=f"The new record has key <b>{newkey}</b>. <code>Placed</code> starts FALSE because it has not been written yet.", p=0, y=0, v=v(), f=cols(ptr=0)))
    steps.append(dict(c="The old file is opened to read and the new file to write. The new file is empty.", p=2, y=2, v=v(), f=cols(ptr=0)))
    for i, r in enumerate(old):
        line, key = r, int(r[:3])
        test = (not placed) and key > newkey
        why = (f"<code>Placed</code> is already TRUE, so the IF is skipped." if placed else (f"{key} &gt; {newkey} is <b>true</b>: this is the first larger key." if test else f"{key} &gt; {newkey} is false, so the IF is skipped."))
        steps.append(dict(c=f"<code>READFILE</code> reads {key} and <code>Key</code> is set. " + why, p=6, y=5, v=v(), f=cols(i=i, ptr=i + 1)))
        if test:
            new.append(newline); placed = True
            steps.append(dict(c=f"The new record is written <b>first</b>, then <code>Placed</code> becomes TRUE. Nothing has been lost: record {key} is still to be copied.", p=7, y=6, v=v(), f=cols(i=i, ptr=i + 1, nw=len(new) - 1)))
        new.append(r)
        steps.append(dict(c=f"The record just read ({key}) is copied to the new file.", p=10, y=8, v=v(), f=cols(i=i, ptr=i + 1, nw=len(new) - 1)))
    line = ""
    steps.append(dict(c="<code>EOF</code> is true, so the loop ends.", p=11, y=3, v=v(), f=cols(ptr=None, eof=True)))
    if placed:
        steps.append(dict(c="<code>Placed</code> is TRUE, so nothing more is written. The new record was placed inside the loop.", p=12, y=9, v=v(), f=cols()))
    else:
        new.append(newline); placed = True
        steps.append(dict(c=f"<code>Placed</code> is still FALSE: no key was larger than {newkey}. The new record is written <b>at the end</b>.", p=13, y=10, v=v(), f=cols(nw=len(new) - 1)))
    steps.append(dict(c="Both files are closed.", p=15, y=11, v=v(), f=cols()))
    steps.append(dict(c="The old file is deleted and the new one renamed. The file is in key order again, with one more record.", p=17, y=13, v=v(), f=[F(20, 0, "Students.txt (now)", new, ok=list(range(len(new))))]))
    return steps


stB = stp("stB", "Inserting 130", trace(130, NEWLINE, OLD_ROWS), PS, PY, lh=20, vw=150, fh=190, dwell=3000)

stC = stp("stC", "Smaller than every key", [
    dict(c="The new record has key <b>100</b>. The first record read is 101, and 101 &gt; 100.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, hl=0, ptr=1, ptrLabel="read"), F(390, 20, "NewStudents.txt (new)", [])]),
    dict(c="The IF is true on the very first record, so the new record is written <b>before anything else</b>. <code>Placed</code> becomes TRUE.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, hl=0, ptr=1, ptrLabel="read"), F(390, 20, "NewStudents.txt (new)", ["100,Zed,50"], nw=0)]),
    dict(c="Record 101 and every other record are then copied in turn. The IF is never true again.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, ok=[0, 1, 2, 3]), F(390, 20, "NewStudents.txt (new)", ["100,Zed,50"] + OLD_ROWS, nw=0)]),
    dict(c="The new file replaces the old one. 100 is now the first record.", f=[F(20, 20, "Students.txt (now)", ["100,Zed,50"] + OLD_ROWS, ok=[0, 1, 2, 3, 4])])],
    fh=175, dwell=3400)

stD = stp("stD", "Larger than every key", [
    dict(c="The new record has key <b>200</b>. No record in the file has a key larger than 200.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, ptr=0, ptrLabel="read"), F(390, 20, "NewStudents.txt (new)", [])]),
    dict(c="Each record fails <code>Key &gt; NewKey</code>, so each is just copied. After the loop <code>Placed</code> is still FALSE.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, ok=[0, 1, 2, 3], eof=True), F(390, 20, "NewStudents.txt (new)", OLD_ROWS)]),
    dict(c="<code>IF NOT Placed</code> is true, so the new record is written <b>after the loop</b>, at the end. Without this check the record would be lost.", f=[F(20, 20, "Students.txt (old)", OLD_ROWS, ok=[0, 1, 2, 3]), F(390, 20, "NewStudents.txt (new)", OLD_ROWS + ["200,Max,77"], nw=4)]),
    dict(c="The new file replaces the old one. 200 is now the last record.", f=[F(20, 20, "Students.txt (now)", OLD_ROWS + ["200,Max,77"], ok=[0, 1, 2, 3, 4])])],
    fh=175, dwell=3400)

explore = '''
  <h2>Lab 1 · Insert a record</h2>
  <p>The file starts with keys 101, 115, 142 and 160. Enter a 3-digit key and press Insert. The table shows what the loop does with each record. The file keeps your changes until you reset it.</p>
  <div class="card"><div class="btnrow"><label>New key <input id="iK" size="5" value="130"></label> <button class="b pri" id="iB">Insert</button> <button class="b" id="iR">Reset file</button></div><div id="iT"></div><div id="iN"></div><div class="verdict" id="iV"></div></div>

  <h2>Lab 2 · Searching: serial against sequential</h2>
  <p>Both files hold the keys 101, 115, 142 and 160. The serial file is in arrival order; the sequential file is in key order. Enter a key to find. Count the records read.</p>
  <div class="card"><div class="btnrow"><label>Key to find <input id="sK" size="5" value="120"></label> <button class="b pri" id="sB">Search</button></div><div class="grid2"><div id="sS"></div><div id="sQ"></div></div><div class="verdict" id="sV"></div></div>
'''

lab = r'''
(function () {
  const start = [101, 115, 142, 160];
  let keys = start.slice();
  const nameOf = (k) => k + ",N" + (k % 100) + "," + (50 + (k % 40));
  const paint = (rows, newFile, msg) => {
    $("#iT").innerHTML = rows ? '<div class="tw"><table class="t mono"><tr><th>Record read</th><th>Key &gt; NewKey and not Placed?</th><th>What is written</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>" : "";
    $("#iN").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Students.txt now</th></tr>' + (newFile || keys).map((k) => `<tr><td>${nameOf(k)}</td></tr>`).join("") + "</table></div>";
    $("#iV").textContent = msg;
  };
  $("#iB").onclick = () => {
    const nk = parseInt($("#iK").value, 10);
    if (isNaN(nk) || nk < 100 || nk > 999) { paint(null, null, "Enter a 3-digit whole number (100 to 999)."); return; }
    const rows = [], out = []; let placed = false;
    keys.forEach((k) => {
      const t = !placed && k > nk;
      if (t) { out.push(nk); placed = true; }
      out.push(k);
      rows.push([nameOf(k), (placed && !t) ? "no: already Placed" : (t ? k + " &gt; " + nk + ": yes" : k + " &gt; " + nk + ": no"), t ? "new record " + nk + ", then " + k : k]);
    });
    if (!placed) { out.push(nk); rows.push(["(end of file)", "-", "IF NOT Placed: new record " + nk]); }
    const dup = keys.includes(nk);
    const reads = keys.length, writes = out.length;
    keys = out;
    paint(rows, null, `${reads} records read, ${writes} written. ` + (dup ? "That key was already in the file, so it now appears twice; a real program would check for a duplicate first." : "The file is still in key order."));
  };
  $("#iR").onclick = () => { keys = start.slice(); paint(null, null, "File reset."); };
  paint(null, null, "Press Insert.");
})();

(function () {
  const ser = [142, 101, 160, 115], seq = [101, 115, 142, 160];
  const tbl = (t, rows, hit, stop) => '<div class="tw"><table class="t mono"><tr><th>' + t + "</th></tr>" + rows.map((r, i) => `<tr><td${i === hit ? ' style="background:var(--ok-soft);font-weight:700"' : (i === stop ? ' style="background:var(--warn-soft)"' : "")}>${r}${i === hit ? " found" : (i === stop ? " too big: stop" : "")}</td></tr>`).join("") + "</table></div>";
  $("#sB").onclick = () => {
    const k = parseInt($("#sK").value, 10); if (isNaN(k)) { $("#sV").textContent = "Enter a whole number."; return; }
    let a = ser.indexOf(k), ra = a >= 0 ? a + 1 : ser.length;
    let b = seq.indexOf(k), stop = -1, rb;
    if (b >= 0) rb = b + 1; else { stop = seq.findIndex((x) => x > k); rb = stop >= 0 ? stop + 1 : seq.length; }
    $("#sS").innerHTML = tbl("Serial: records read " + ra, ser.slice(0, ra), a, -1);
    $("#sQ").innerHTML = tbl("Sequential: records read " + rb, seq.slice(0, rb), b, stop);
    $("#sV").textContent = b >= 0 ? `Both find ${k}. The sequential file needed ${rb} read${rb > 1 ? "s" : ""}; the serial file needed ${ra}.` : `${k} is not in either file. The serial file has to read all ${ra} records to be sure; the sequential file stopped after ${rb} because the key was passed.`;
  };
  $("#sB").onclick();
})();
''' + CLASSIFY("cl1", "Does the statement describe a serial file or a sequential file?", ["Serial file", "Sequential file"],
    [("A new record is added by appending it", 0), ("A new record is added by copying to a new file with the record in its key position", 1), ("Two files are open during the update", 1), ("The old file is replaced by the new one afterwards", 1), ("A search can stop once it has passed the key", 1), ("A search that fails must read to the end of the file", 0), ("FOR APPEND is enough to store the record", 0)],
    "Serial: append, and search to the end. Sequential: rebuild in key order, and search can stop early.") + ORDER(
    "Put the steps for adding a record to a sequential file in order.",
    ["Open the old file for reading and a new file for writing", "Read a record from the old file", "If its key is larger than the new key, and the new record is not written yet, write the new record", "Write the record that was read", "Repeat until the end of the old file", "If the new record has still not been written, write it", "Close both files and replace the old file with the new one"],
    "Open both, read, place the new record at the first larger key, copy, repeat, catch the end case, close and replace.") + MATCH([
    ["Placed", "A flag that records whether the new record has been written yet"], ["NewStudents.txt", "The new version of the file that the records are copied into"], ["Key > NewKey", "True at the first record that belongs after the new one"], ["IF NOT Placed after the loop", "Writes the new record when its key is the largest"], ["os.replace", "Deletes the old file and gives its name to the new file"], ["Sequential file", "Records in order of a key field"]]) + CALC([
    {"q": "A sequential file has keys 101, 115, 142, 160. A record with key 130 is inserted. How many records does the new file hold?", "a": 5, "unit": "", "tol": 0.01, "hint": "All four old records plus the new one.", "sol": "<b>5</b>."},
    {"q": "Same file, inserting 130. How many records are written to the new file before the new record is written?", "a": 2, "unit": "", "tol": 0.01, "hint": "101 and 115 are smaller than 130.", "sol": "<b>2</b>."},
    {"q": "Same file, inserting 100. How many records are written before the new record?", "a": 0, "unit": "", "tol": 0.01, "hint": "101 is already larger than 100.", "sol": "<b>0</b>."},
    {"q": "Same file, inserting 200. How many records are written before the new record?", "a": 4, "unit": "", "tol": 0.01, "hint": "Every old record is copied first.", "sol": "<b>4</b>."},
    {"q": "A sequential file holds 1000 records. One is inserted using the copy method. How many times does READFILE run in total?", "a": 1000, "unit": "", "tol": 0.01, "hint": "Every old record is read once, whatever its position.", "sol": "<b>1000</b>."},
    {"q": "Same file (1000 records). How many WRITEFILE statements run in total?", "a": 1001, "unit": "", "tol": 0.01, "hint": "1000 copies plus the new record.", "sol": "<b>1001</b>."}]) + MCQ([
    ("Why is a new record not simply appended to a sequential file?", ["Appending is too slow", "It would break the key order", "The file would be deleted", "Append cannot be used on text files"], 1, "A sequential file must stay in key order."),
    ("Which statement stops the new record being written more than once?", ["EOF", "The Placed flag", "CLOSEFILE", "The new line"], 1, "Placed becomes TRUE after the first write."),
    ("What is needed after the loop if the new key is the largest?", ["Nothing", "IF NOT Placed, write the new record", "Another loop", "SEEK"], 1, "Otherwise the record would be lost."),
    ("How is the file updated?", ["By editing the middle of the old file", "By writing a new version and replacing the old file", "By using SEEK", "By appending then sorting in place"], 1, "Text files cannot have lines inserted, so a new version is made."),
    ("Which open modes are used for the old and new files?", ["READ and WRITE", "WRITE and READ", "APPEND and APPEND", "RANDOM and RANDOM"], 0, "Read the old, write the new."),
    ("What does the key comparison in the loop look for?", ["The last record", "The first record with a larger key than the new one", "A duplicate key", "An empty line"], 1, "That is where the new record belongs.")], "qz1") + CARDS([
    ("Sequential file", "Records in key order."), ("New version", "Records are copied to a new file with the new one inserted."), ("Placed", "Flag: has the new record been written yet?"), ("Key > NewKey", "Find the first record that goes after the new one."),
    ("IF NOT Placed (after loop)", "The new key was the largest: write it at the end."), ("Replace", "Delete the old file and rename the new file."), ("Two files", "READ the old, WRITE the new."), ("Amend or delete", "Same copy pattern: change the record or leave it out.")])

real = RWNOTE + (
    rw("A payroll master file", "Employees are kept in employee number order. When someone joins, the program copies the old file to a new one and writes the new employee at the right place, so the file is still in order for the next payroll run.", "sequential update by copying to a new file.") +
    rw("Overnight batch processing", "The day's changes are collected in a transaction file, sorted by key, and merged with the master file in a single pass from top to bottom to produce a new master file.", "sequential files suit batch processing: one pass, old file in, new file out.") +
    rw("A bank statement run", "At the end of the month every account is read in account order and a line is written for each to a new file. The old file is kept as a backup until the new one is checked.", "the old and new version both exist during the update.") +
    rw("Why a search can stop early", "A library file is in order of book number. A search for number 5120 can stop as soon as it reads 5121, because 5120 would have come before it.", "a sequential search stops when the key has been passed."))

review = (
    req("3 marks", "Explain", "Explain why a new record cannot be appended to a sequential file.", "Link the order to the key field.", mks(["A sequential file is stored in order of a key field", "appending would put the record at the end, out of key order", "so the record has to be placed in its key position (a new version of the file is made)"])) +
    req("2 marks", "Describe", "Describe how a program updates a sequential text file when a new record is added.", "Two files, copy, replace.", mks(["The old file is read record by record and each record is copied to a new file, with the new record written in its key position", "the old file is then replaced by the new file"])) +
    req("6 marks", "Write", "Write Python to insert the line <code>NewLine</code> with key <code>NewKey</code> into <code>Students.txt</code>, which is in key order.", "Open both, copy with a Placed flag, write after the loop if needed, close, replace.", pc('''import os
Placed = False
Old = open("Students.txt", "r")
New = open("NewStudents.txt", "w")
for Line in Old:
    if not Placed and int(Line.split(",")[0]) > NewKey:
        New.write(NewLine)
        Placed = True
    New.write(Line)
if not Placed:
    New.write(NewLine)
Old.close()
New.close()
os.replace("NewStudents.txt", "Students.txt")'''), "Writing NewLine inside the loop every time Key > NewKey. Without the Placed flag it is written again for every later record.") +
    req("3 marks", "State", "A new record has a key larger than every key already in the file. State where in the algorithm it is written and why.", "It never meets the IF inside the loop.", mks(["After the loop has finished", "because no record read had a larger key, so Placed is still FALSE", "so it is written at the end of the new file"])) +
    req("4 marks", "Complete", "In the pseudocode below, a record is <b>deleted</b> instead of added. Describe the one change to the loop.", "The loop copies every record except one.", mks(["Compare the key of the record read with the key to delete", "if they are equal, do not write the record to the new file", "otherwise write it as normal"]), "Trying to remove the line from the old file directly."))

OLDQ = old_questions()
where = [("O/N 2023", "31, 33", "4(a)", "4", "Describe sequential and random file organisation (a new version of the file is needed to update a sequential file)"),
         ("M/J 2023", "32", "2(a)", "3", "Describe how records are organised and accessed in a sequential file"),
         ("M/J 2026", "32", "4(a), (b), (c)", "1 + 2 + 3", "A use of a sequential file; how records are organised; how a record is found")]
past = peq(SRC("w23", "31, 33", "Q4(a)"), "4 marks", "Describe",
    "Describe sequential and random methods of file organisation. (2 marks for each.)",
    "Four points in total. For sequential: order, the key, and what updating means.",
    "<p>Sequential (max 2): " + mks(["Records in the file are ordered", "based on the key field", "A new version of the file has to be created to update the file"]) + "</p><p>Random (max 2): " + mks(["Records are stored in no particular order", "There is a relationship between the key and the record's location (a hashing algorithm is used)", "Updates can be carried out directly"], "a") + "</p>",
    "Saying a random file is 'not sorted' and stopping. The mark is for how the location is found.") + peq(SRC("s23", "32", "Q2(a)"), "3 marks", "Describe",
    "Describe how records are organised and accessed in a sequential file.",
    "Organised (order, key) and accessed (one after another, until found).",
    "<p>" + mks(["Records are stored in a particular order", "the order is determined by the value in a key field", "records are accessed one after the other (from the beginning, record by record)", "until the required record is found or the key field value is exceeded"]) + " (maximum 3)</p>",
    "Describing the records as stored 'in the order they were added'. That is a serial file.") + peq(SRC("s26", "32", "Q4(a), (b), (c)"), "1 + 2 + 3 marks", "State / Describe / Outline",
    "(a) State one example of where sequential file organisation could be used. (b) Describe how records are organised in sequential files. (c) Outline the process of sequential file access to find a record in a sequential file.",
    "(b) is about order and the key. (c) is a search from the start of the file that can stop early.",
    "<p>(a) One of: " + mks(["batch processing tasks", "generating bills or payroll", "recording log files", "backup"], "a") + "</p><p>(b) " + mks(["Records are stored one after the other (linearly)", "in a given order", "usually based on a key field / unique identifier"]) + " (maximum 2)</p><p>(c) " + mks(["Each record is searched one after the other from the physical start of the file", "using the record key", "until the record is found", "or until the key being searched for has been exceeded, or the end of the file is reached"]) + " (maximum 3)</p>",
    "Answering (b) with 'chronological order', which is serial. Describing an index in (c); an index belongs to indexed sequential files.")
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Sequential files are asked as written descriptions in Paper 3. Writing the update as code is not asked in the papers so far, so the algorithm on this page is the extension of the idea in the mark scheme (a new version of the file is created)."

tipsl = [("Never append.", "A new record goes in its key position, so the file is rebuilt."), ("Two files.", "READ the old, WRITE the new, then replace the old with the new."), ("Use a flag.", "Placed stops the new record being written more than once."), ("Cover the end case.", "IF NOT Placed after the loop handles the largest key."), ("Copy what you read.", "Every old record is written, after any insertion."), ("Say 'a new version of the file'.", "This phrase earns the mark in descriptions.")]
sents = [("Explain why it is rebuilt", "A sequential file is in key order, so the new record has to go in its key position, which means creating a new version of the file."), ("Describe the update", "The old file is read record by record and copied to a new file, and the new record is written at the first record with a larger key."), ("Describe a search", "Records are checked one after another from the start until the key is found or the key has been exceeded.")]
words = [("Describe", "Give the main features in connected points."), ("Explain", "Give a reason as well as the fact."), ("Write", "Produce Python or pseudocode that follows the steps."), ("State", "A short fact or example.")]

finishf("ac20f2", "ac-20-2-1-adding-to-sequential-file", "Adding a Record to a Sequential File",
        "Why a sequential file is rebuilt rather than appended to, and the copy-and-insert algorithm with its three cases; pseudocode and Python side by side, with a line-by-line animation.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + stD + lab, where, past, note, words)
