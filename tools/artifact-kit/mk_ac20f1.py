"""20.2.1 extra resource: storing records in a serial or sequential file. Run: python3 tools/artifact-kit/mk_ac20f1.py"""
from ac20f import *

OLD = old_questions()

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>record</b> is a group of related <b>fields</b> (a student's ID, name and mark), and a <b>file</b> keeps many records after the program has ended. In a text file each record is stored as <b>one line</b>, made by joining the fields into a string with a separator such as a comma. A <b>serial file</b> stores the records in the order they arrive, so a new record is <b>appended to the end</b> with <code>FOR APPEND</code>. A <b>sequential file</b> stores them in order of a <b>key field</b>, so the records must be sorted by the key before they are written. Either file is read back from the start, one record after another, until <code>EOF</code>.</p></div>

  <h2>1 · A record in a program</h2>
  <p>Before a record can be stored it has to exist in the program. A record type groups the fields; one variable of that type holds one record.</p>
  ''' + both('''class TStudent:
    def __init__(self, StudentID, Name, Mark):
        self.StudentID = StudentID
        self.Name = Name
        self.Mark = Mark

S = TStudent(104, "Aria", 72)''', '''TYPE TStudent
   DECLARE StudentID : INTEGER
   DECLARE Name : STRING
   DECLARE Mark : INTEGER
ENDTYPE

DECLARE S : TStudent
S.StudentID <- 104
S.Name <- "Aria"
S.Mark <- 72''') + '''

  <h2>2 · Turning a record into one line of text</h2>
  <p>A text file can only hold strings. Convert each number to a string (<code>str()</code> in Python, <code>NUM_TO_STR()</code> in pseudocode) and join the fields with a comma. The comma is the <b>separator</b>: it is what lets the fields be cut apart again when the line is read back.</p>
  ''' + both('''Line = str(S.StudentID) + "," + S.Name + "," + str(S.Mark)
# Line is now "104,Aria,72"''', '''Line <- NUM_TO_STR(S.StudentID) & "," & S.Name & "," & NUM_TO_STR(S.Mark)
// Line is now "104,Aria,72"''') + '''
  <div class="tip"><b class="h">Keep the format fixed</b>Every record must use the same fields, in the same order, with the same separator. If a name could contain a comma, choose a different separator, otherwise the line cannot be cut apart correctly.</div>

  <h2>3 · Storing a record in a serial file</h2>
  <p>Open the file for <b>append</b>, write the line, close the file. Append keeps every record already in the file and adds the new one after the last. If the file does not exist yet, append creates it.</p>
  ''' + both('''File = open("Students.txt", "a")
File.write(Line + "\\n")
File.close()''', '''OPENFILE "Students.txt" FOR APPEND
WRITEFILE "Students.txt", Line
CLOSEFILE "Students.txt"''') + '''
  <p><code>write()</code> does not add a new line by itself, so the <code>"\\n"</code> ends the record. Without it the next record would run on to the same line.</p>

  <h2>4 · Storing records in a sequential file</h2>
  <p>The line format is exactly the same. What changes is the <b>order</b>: the records are sorted on the key field (<code>StudentID</code>) first, then written from the start of a new file, so each key is larger than the one before. Opening with <code>FOR WRITE</code> is right here because the whole file is being created.</p>
  ''' + both('''Students.sort(key=lambda Student: Student.StudentID)
File = open("Students.txt", "w")
for Student in Students:
    File.write(str(Student.StudentID) + "," + Student.Name + "," + str(Student.Mark) + "\\n")
File.close()''', '''// sort Students[1:Count] into StudentID order (for example a bubble sort)
OPENFILE "Students.txt" FOR WRITE
FOR Index <- 1 TO Count
   Line <- NUM_TO_STR(Students[Index].StudentID) & "," & Students[Index].Name & "," & NUM_TO_STR(Students[Index].Mark)
   WRITEFILE "Students.txt", Line
NEXT Index
CLOSEFILE "Students.txt"''') + '''
  <p>Adding one record to a file that is already in key order is a different job, because the new record has to go in the right place. That is on the next page, <b>Adding a Record to a Sequential File</b>.</p>

  <h2>5 · Serial against sequential</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Serial</th><th>Sequential</th></tr>
    <tr><td>Order of records</td><td>The order they were added (chronological)</td><td>Order of a key field</td></tr>
    <tr><td>Storing a record</td><td>Append to the end</td><td>Sort on the key, then write in order (or insert in the right place)</td></tr>
    <tr><td>Open mode used</td><td><code>APPEND</code></td><td><code>WRITE</code> for a new file</td></tr>
    <tr><td>Reading</td><td>From the start, record by record, until <code>EOF</code></td><td>Same, and the search can stop once a key larger than the one wanted is reached</td></tr>
    <tr><td>Typical use</td><td>Transaction logs, data logging, temporary files</td><td>Payroll, bills, batch processing</td></tr>
  </table></div>

  <h2>6 · Reading the stored records back</h2>
  <p>Both kinds are read the same way: open for read, repeat until the end of the file, close. Each line is cut into fields and converted back to the right data types.</p>
  ''' + both('''File = open("Students.txt", "r")
for Line in File:
    Parts = Line.strip().split(",")
    S = TStudent(int(Parts[0]), Parts[1], int(Parts[2]))
File.close()''', '''OPENFILE "Students.txt" FOR READ
WHILE NOT EOF("Students.txt")
   READFILE "Students.txt", Line
   S.StudentID <- STR_TO_NUM(LEFT(Line, 3))   // IDs are always 3 digits
   // Name and Mark are cut out of Line with MID in the same way
ENDWHILE
CLOSEFILE "Students.txt"''') + '''
  <p><code>strip()</code> removes the new line at the end of each line, and <code>int()</code> turns the text back into a number.</p>

  <h2>7 · Common ways to lose marks</h2>
  <ul>
    <li>Using <code>FOR WRITE</code> to add one record. It deletes every record already in the file. Use <code>FOR APPEND</code>.</li>
    <li>Forgetting <code>NUM_TO_STR</code> or <code>str()</code> when joining a number to a string.</li>
    <li>Forgetting the separator or the new line, so the fields run together.</li>
    <li>Describing a serial file as "in order". Serial means the order added, not sorted.</li>
    <li>Not closing the file.</li>
  </ul>
'''

watch = '''
  <h2>1 · Appending a record to a serial file</h2><p>Press Play, or click the steps. Both versions of the code are highlighted together.</p><div id="stA"></div>
  <h2>2 · Serial order against sequential order</h2><div id="stB"></div>
  <h2>3 · Reading the records back</h2><div id="stC"></div>
'''

PSA = ['Line <- NUM_TO_STR(S.StudentID) & ","', 'Line <- Line & S.Name & ","', 'Line <- Line & NUM_TO_STR(S.Mark)', 'OPENFILE "Students.txt" FOR APPEND', 'WRITEFILE "Students.txt", Line', 'CLOSEFILE "Students.txt"']
PYA = ['Line = str(S.StudentID) + ","', 'Line = Line + S.Name + ","', 'Line = Line + str(S.Mark)', 'File = open("Students.txt", "a")', 'File.write(Line + "\\n")', 'File.close()']
base = ["118,Ben,55", "102,Cho,81"]
sv = lambda l: [("S.StudentID", "104"), ("S.Name", "Aria"), ("S.Mark", "72"), ("Line", l)]
stA = stp("stA", "Appending to a serial file", [
    dict(c="The record <code>S</code> holds 104, Aria and 72. <code>Students.txt</code> already holds two records, in the order they were added.", p=-1, y=-1, v=sv(""), f=[F(20, 0, "Students.txt", base)]),
    dict(c="The first field is converted to a string and the separator added.", p=0, y=0, v=sv("104,"), f=[F(20, 0, "Students.txt", base)]),
    dict(c="The name and a second separator are joined on.", p=1, y=1, v=sv("104,Aria,"), f=[F(20, 0, "Students.txt", base)]),
    dict(c="The mark is converted and joined on. <code>Line</code> now holds the whole record as text.", p=2, y=2, v=sv("104,Aria,72"), f=[F(20, 0, "Students.txt", base)]),
    dict(c="<code>FOR APPEND</code> opens the file and puts the pointer at the <b>end</b>. The old records are kept.", p=3, y=3, v=sv("104,Aria,72"), f=[F(20, 0, "Students.txt", base, ptr=2, ptrLabel="next write goes here")]),
    dict(c="The line is written at the pointer, as a new last line.", p=4, y=4, v=sv("104,Aria,72"), f=[F(20, 0, "Students.txt", base + ["104,Aria,72"], nw=2)]),
    dict(c="The file is closed so the data is saved. The records are in the order they arrived (118, 102, 104). That is a serial file: no sorting was done.", p=5, y=5, v=sv("104,Aria,72"), f=[F(20, 0, "Students.txt", base + ["104,Aria,72"], ok=[2])])],
    PSA, PYA, lh=22, vw=150, fh=105)

R4 = ["130,Dev,64", "104,Aria,72", "160,Eli,90", "118,Ben,55"]
S4 = ["104,Aria,72", "118,Ben,55", "130,Dev,64", "160,Eli,90"]
stB = stp("stB", "Serial and sequential order", [
    dict(c="Four records arrive, in this order: 130, 104, 160, 118.", f=[F(20, 20, "Order of arrival", R4)], t=[(260, 40, "Both files are built from these four records.", "sm")]),
    dict(c="<b>Serial:</b> each record is appended as it arrives. The file holds them in arrival order.", f=[F(20, 20, "Order of arrival", R4), F(260, 20, "Serial file", R4, nw=3)]),
    dict(c="<b>Sequential:</b> the records are first sorted on the key field, <code>StudentID</code>, in memory.", f=[F(20, 20, "Order of arrival", R4), F(260, 20, "Serial file", R4), F(500, 20, "Sorted on StudentID", S4, hl=0)]),
    dict(c="The sorted records are written from the start of a new file. Each key is larger than the one before.", f=[F(20, 20, "Order of arrival", R4), F(260, 20, "Serial file", R4), F(500, 20, "Sequential file", S4, ok=[0, 1, 2, 3])]),
    dict(c="Reading from the top: the serial file gives 130 first. The sequential file gives 104 first and the keys then rise: 104, 118, 130, 160.", f=[F(260, 20, "Serial file", R4, hl=0), F(500, 20, "Sequential file", S4, hl=0)])],
    fh=150, dwell=3600)

PSC = ['OPENFILE "Students.txt" FOR READ', 'WHILE NOT EOF("Students.txt")', '   READFILE "Students.txt", Line', '   Key <- STR_TO_NUM(LEFT(Line, 3))', '   OUTPUT Key', 'ENDWHILE', 'CLOSEFILE "Students.txt"']
PYC = ['File = open("Students.txt", "r")', 'for Line in File:', '    Key = int(Line.split(",")[0])', '    print(Key)', 'File.close()']
rows3 = ["118,Ben,55", "102,Cho,81", "104,Aria,72"]
stepsC = [dict(c="The file is opened for reading. The pointer is at the first line.", p=0, y=0, v=[("Line", ""), ("Key", "")], f=[F(20, 0, "Students.txt", rows3, ptr=0, ptrLabel="next read")])]
out = []
for i, r in enumerate(rows3):
    stepsC.append(dict(c=f"Not at the end of the file, so the loop runs. <code>READFILE</code> reads line {i + 1} into <code>Line</code> and moves the pointer on.", p=2, y=1, v=[("Line", r), ("Key", "")], f=[F(20, 0, "Students.txt", rows3, hl=i, ptr=i + 1, ptrLabel="next read")], t=[(380, 14, "Output so far: " + (", ".join(out) or "none"), "sm")]))
    out.append(r[:3])
    stepsC.append(dict(c=f"The first three characters are converted to a number and output: <b>{r[:3]}</b>.", p=4, y=3, v=[("Line", r), ("Key", r[:3])], f=[F(20, 0, "Students.txt", rows3, hl=i, ptr=i + 1, ptrLabel="next read")], t=[(380, 14, "Output so far: " + ", ".join(out), "sm")]))
stepsC.append(dict(c="<code>EOF</code> is now true, so the loop ends. Records come back in the order they are stored.", p=1, y=1, v=[("Line", ""), ("Key", "")], f=[F(20, 0, "Students.txt", rows3, eof=True)], t=[(380, 14, "Output: " + ", ".join(out), "sm")]))
stepsC.append(dict(c="The file is closed.", p=6, y=4, v=[("Line", ""), ("Key", "")], f=[F(20, 0, "Students.txt", rows3)], t=[(380, 14, "Output: " + ", ".join(out), "sm")]))
stC = stp("stC", "Reading records until the end of the file", stepsC, PSC, PYC, lh=22, fh=125, dwell=2800)

explore = '''
  <h2>Lab 1 · Turn a record into a line</h2>
  <p>Change the fields. The statements and the line stored in the file update as you type.</p>
  <div class="card"><div class="btnrow"><label>StudentID <input id="lI" size="5" value="104"></label> <label>Name <input id="lN" size="10" value="Aria"></label> <label>Mark <input id="lM" size="4" value="72"></label></div><div id="lO"></div><div class="verdict" id="lV"></div></div>

  <h2>Lab 2 · Serial or sequential?</h2>
  <p>Add records one at a time and see where each one is stored. Try a key that is smaller than the ones already there.</p>
  <div class="card"><div class="btnrow"><label>New StudentID <input id="aK" size="5" value="140"></label> <button class="b pri" id="aB">Add record</button> <button class="b" id="aR">Reset</button></div><div class="grid2"><div id="aS"></div><div id="aQ"></div></div><div class="verdict" id="aV"></div></div>
'''

lab = r'''
(function () {
  const g = (id) => $("#" + id).value;
  const paint = () => {
    const id = g("lI").trim(), nm = g("lN"), mk = g("lM").trim(), line = id + "," + nm + "," + mk;
    $("#lO").innerHTML = lineHTML([
      'Line = str(' + id + ') + "," + "' + nm + '" + "," + str(' + mk + ')', 'Line <- NUM_TO_STR(' + id + ') & "," & "' + nm + '" & "," & NUM_TO_STR(' + mk + ')', "", "Written to the file:  " + line, line.length + " characters, plus the new line"]);
    const w = [];
    if (nm.includes(",")) w.push("The name contains a comma, so the line now has " + line.split(",").length + " parts instead of 3. Reading it back would cut it in the wrong place.");
    if (!/^\d{3}$/.test(id)) w.push("StudentID is not 3 digits, so LEFT(Line, 3) would not pick out the key correctly.");
    if (!/^-?\d+$/.test(mk)) w.push("Mark is not a whole number, so int() would fail when the line is read back.");
    $("#lV").textContent = w.length ? w.join(" ") : "Three fields, two commas: this line can be cut back into its fields.";
  };
  ["lI", "lN", "lM"].forEach((i) => ($("#" + i).oninput = paint)); paint();
})();

(function () {
  const start = [118, 102];
  let ser, seq;
  const reset = () => { ser = start.slice(); seq = start.slice().sort((a, b) => a - b); paint("Starting files: 118 and 102."); };
  const tbl = (t, rows, mark) => '<div class="tw"><table class="t mono"><tr><th>' + t + "</th></tr>" + rows.map((r, i) => `<tr><td${i === mark ? ' style="background:var(--ok-soft);font-weight:700"' : ""}>${r}</td></tr>`).join("") + "</table></div>";
  const paint = (msg, ms, mq) => { $("#aS").innerHTML = tbl("Serial file (order added)", ser, ms); $("#aQ").innerHTML = tbl("Sequential file (key order)", seq, mq); $("#aV").textContent = msg; };
  $("#aB").onclick = () => {
    const k = parseInt($("#aK").value, 10); if (isNaN(k)) { $("#aV").textContent = "Enter a whole number."; return; }
    ser.push(k); let p = 0; while (p < seq.length && seq[p] < k) p++; seq.splice(p, 0, k);
    const after = seq.length - 1 - p;
    paint("Serial: " + k + " was appended to the end, nothing else moved. Sequential: " + k + " belongs at position " + (p + 1) + ", so " + (after ? after + " record" + (after > 1 ? "s" : "") + " after it must move down (the file is rewritten)." : "it goes at the end, so nothing needs to move."), ser.length - 1, p);
  };
  $("#aR").onclick = reset; reset();
})();
''' + CLASSIFY("cl1", "Which kind of file does each statement describe?", ["Serial", "Sequential", "Both"],
    [("Records are in the order they were added", 0), ("Records are in order of a key field", 1), ("A new record is written with FOR APPEND", 0), ("Records are sorted on the key before they are written", 1), ("Each record is stored as one line of text", 2), ("It is read from the start until EOF", 2), ("Suits a log of transactions", 0), ("Suits a payroll run that processes staff in key order", 1)],
    "Serial is chronological, sequential is by key. Both are text files read from the start.") + ORDER(
    "Put the steps for storing one record in a serial file in order.",
    ["Put the values into a record variable", "Convert each number to a string", "Join the fields into one line with commas", "Open the file FOR APPEND", "WRITEFILE the line", "CLOSEFILE"],
    "Build the record, build the line, open for append, write, close.") + MATCH([
    ["Record", "A group of related fields, such as ID, name and mark"], ["Field", "One item of data inside a record"], ["Key field", "The field that identifies a record and decides the order in a sequential file"], ["Separator", "The character, such as a comma, that divides the fields in a line"], ["Serial file", "Records stored in the order they were added"], ["Sequential file", "Records stored in key field order"]]) + CALC([
    {"q": "A record is stored as the line 104,Aria,72. How many characters are in the line, not counting the new line?", "a": 11, "unit": "", "tol": 0.01, "hint": "3 + 1 + 4 + 1 + 2.", "sol": "<b>11</b>."},
    {"q": "A serial file holds 40 records. One more is added with FOR APPEND. How many records does it hold?", "a": 41, "unit": "", "tol": 0.01, "hint": "Append keeps the old ones.", "sol": "<b>41</b>."},
    {"q": "The same file (40 records) is opened FOR WRITE by mistake and one record is written. How many records does it hold afterwards?", "a": 1, "unit": "", "tol": 0.01, "hint": "WRITE replaces the old contents.", "sol": "<b>1</b>."},
    {"q": "Records with keys 130, 104, 160 and 118 are sorted and written to a sequential file. What is the key of the third record in the file?", "a": 130, "unit": "", "tol": 0.01, "hint": "Sorted order: 104, 118, 130, 160.", "sol": "<b>130</b>."},
    {"q": "A file holds 250 records, one per line. A loop reads until EOF. How many times does READFILE run?", "a": 250, "unit": "", "tol": 0.01, "hint": "One read for each line.", "sol": "<b>250</b>."}]) + MCQ([
    ("Which open mode adds a record to a serial file without losing the existing ones?", ["READ", "WRITE", "APPEND", "RANDOM"], 2, "APPEND adds at the end and keeps the old records."),
    ("In a serial file the records are stored...", ["In key order", "In the order they were added", "At a calculated address", "In random order of size"], 1, "Serial means chronological."),
    ("Why is a separator needed when a record is stored as a line?", ["To make the file smaller", "So the fields can be cut apart when read back", "To sort the record", "To close the file"], 1, "Without it the fields run together."),
    ("What must be done to a number before it is joined to a string in a line?", ["Rounded", "Converted to a string", "Sorted", "Deleted"], 1, "str() in Python, NUM_TO_STR() in pseudocode."),
    ("Which is needed to build a sequential file from unsorted records?", ["Sort them on the key first", "Open the file FOR RANDOM", "Use SEEK", "Append them in any order"], 0, "Sequential files are in key order."),
    ("What does write() NOT do for you in Python?", ["Write text", "Add the new line at the end of the record", "Use the open file", "Send text to the file"], 1, "Add \"\\n\" yourself.")], "qz1") + CARDS([
    ("Record", "A group of related fields."), ("Field", "One item inside a record."), ("Serial file", "Records in the order added. Append new ones."), ("Sequential file", "Records in key order. Sort before writing."),
    ("FOR APPEND", "Open and add to the end."), ("FOR WRITE", "Open and replace everything."), ("Separator", "A comma between fields in the line."), ("EOF", "True when nothing more can be read.")])

real = RWNOTE + (
    rw("A shop's till log", "Every sale is added as a new line at the end of the day's file as it happens. Nothing is sorted, so recording is quick and no earlier sale is touched.", "serial file: records in the order they happened, added with APPEND.") +
    rw("A payroll file", "Staff records are held in order of employee number. A program reads the file from the top once a month and produces payslips in that order.", "sequential file: sorted on the key field, processed from start to end.") +
    rw("Data logging from a sensor", "A weather station writes a temperature line every minute. The file simply grows, and an analysis program reads it from the start later.", "serial file used for data logging.") +
    rw("A temporary transaction file", "During the day orders are collected in a file in the order they arrive. Overnight they are sorted and merged into the main file, which is kept in order of customer number.", "serial for collecting, sequential for the master file."))

review = (
    req("2 marks", "Describe", "Describe how records are stored in a serial file.", "Two points: the order, and where a new record goes.", mks(["Records are stored one after the other in the order they were added", "A new record is appended to the end of the file"])) +
    req("2 marks", "Explain", "Why is a record stored as a single line with commas between the fields?", "A text file holds strings; link to reading it back.", mks(["A text file can only hold text, so the fields are joined into one string", "the commas let the line be split back into separate fields when it is read"])) +
    req("4 marks", "Write", "Write pseudocode to store the record <code>S</code> (type <code>TStudent</code>) at the end of the serial file <code>Students.txt</code>.", "Build the line, then open, write, close.", pc('''Line <- NUM_TO_STR(S.StudentID) & "," & S.Name & "," & NUM_TO_STR(S.Mark)
OPENFILE "Students.txt" FOR APPEND
WRITEFILE "Students.txt", Line
CLOSEFILE "Students.txt"'''), "Opening FOR WRITE, which erases the earlier records.") +
    req("5 marks", "Write", "Write Python to store all the records in the list <code>Students</code> in a sequential file, in order of <code>StudentID</code>.", "Sort first. FOR WRITE is right because the file is being created.", pc('''Students.sort(key=lambda Student: Student.StudentID)
File = open("Students.txt", "w")
for Student in Students:
    File.write(str(Student.StudentID) + "," + Student.Name + "," + str(Student.Mark) + "\\n")
File.close()'''), "Writing the records without sorting them, which gives a serial file.") +
    req("3 marks", "Explain", "A school stores exam entries in a serial file and also in a sequential file. Explain one difference between adding a new entry to each.", "Where the record goes.", mks(["Serial: the new entry is appended to the end of the file", "Sequential: the entry must go in the position given by its key field", "so records after it have to be moved (the file rewritten)"]), "Saying the sequential file is 'sorted' without saying what that means for adding."))

where = [("O/N 2024", "32", "2(a), (b)", "2 + 1", "Describe serial file organisation; state a use"),
         ("O/N 2023", "31, 33", "4(b)", "2", "Outline sequential access for serial and sequential files"),
         ("O/N 2025", "42", "3(d)", "5", "Write the contents of an array to a new text file, one comma-separated line per record (Python)")]
past = peq(SRC("w24", "32", "Q2(a), (b)"), "2 + 1 marks", "Describe / State",
    "(a) Describe serial file organisation as a method of storing data records in a file. (b) State one example of a use for serial file organisation.",
    "Order, then where new records go. A use must be a real use, not another description.",
    "<p>(a) " + mks(["Records are stored one after the other as they are collected (chronological order)", "New records are appended to the end of the file"]) + "</p><p>(b) One of: " + mks(["creating unsorted or temporary transaction files", "creating data logging files"], "a") + "</p>",
    "Writing that the records are 'in order'. Serial is the order they arrived, not an order on a key.") + peq(SRC("w23", "31, 33", "Q4(b)"), "2 marks", "Outline",
    "Outline the process of sequential access for serial and sequential files.",
    "Start, check one after another, stop.",
    "<p>" + mks(["Start at the beginning of the file", "check the records one after another (linearly)", "until the record is found, or the end of the file is reached (or the records have been processed)"]) + " (maximum 2)</p>",
    "Describing a jump straight to a record. That is direct access, which random files use.") + OLD["O/N 2025 · 9618/42 · Q3(d)"]
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Serial and sequential files are asked as written descriptions in Paper 3. Paper 4 asks you to write records to a text file as Python, as in the last question."

tipsl = [("Name the order.", "Serial: the order added. Sequential: the order of a key field. Never swap them."), ("Say where a new record goes.", "Serial: the end of the file. Sequential: in its key position."), ("APPEND adds, WRITE replaces.", "Using WRITE to add a record loses the rest of the file."), ("One record, one line.", "Join the fields with a separator and end with a new line."), ("Convert numbers.", "str() or NUM_TO_STR() before joining; int() or STR_TO_NUM() after reading."), ("Always close.", "CLOSEFILE once the writing or reading is finished.")]
sents = [("Describe a serial file", "Records are stored in the order they were added, and new records are appended to the end of the file."), ("Describe a sequential file", "Records are stored in order of a key field, so a new record must be placed in its key position."), ("Describe reading either", "Start at the beginning and check each record in turn until the record is found or the end of the file is reached.")]
words = [("Describe", "Give the main features in connected points."), ("State", "Give a short fact or example."), ("Write", "Produce pseudocode or Python that opens, writes and closes."), ("Explain", "Give a reason as well as the fact.")]

finishf("ac20f1", "ac-20-2-1-storing-records-serial-sequential", "Storing Records in a Serial or Sequential File",
        "Turning a record into a line, appending to a serial file, sorting before writing a sequential file, and reading the records back; pseudocode and Python side by side, with step-by-step animations.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words)
