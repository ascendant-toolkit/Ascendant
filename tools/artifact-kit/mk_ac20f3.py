"""20.2.1 extra resource: adding a record to a random file. Run: python3 tools/artifact-kit/mk_ac20f3.py"""
from ac20f import *

OLDQ = old_questions()

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>random file</b> is a file of equal-sized records, each at a numbered <b>location</b>, and the program can jump straight to any location with <code>SEEK</code>. To add a record, a <b>hash function</b> turns its key into a location (here <code>Key MOD 7</code>), the program uses <code>SEEK</code> to move there, and <code>PUTRECORD</code> writes the record. If another record is already at that location, that is a <b>collision</b>, so the program checks the <b>next location</b> (wrapping round at the end) until it finds an empty one. If it comes back to where it started, the file is <b>full</b>. An empty location holds a record whose key is <code>0</code>, which is how the program recognises it.</p></div>

  <h2>1 · The file and its locations</h2>
  <p>This page uses a file <code>Accounts.dat</code> with 7 locations, numbered 0 to 6. Each record is a <code>TAccount</code>. The file is created with every location holding a blank record, so there is something at every location to read. (<code>PutRecord</code> is defined in the next section.)</p>
  ''' + both('''import struct

class TAccount:
    def __init__(self, AccountNumber=0, Name=""):
        self.AccountNumber = AccountNumber
        self.Name = Name

File = open("Accounts.dat", "wb")
for Location in range(7):
    PutRecord(File, TAccount())      # blank record
File.close()''', '''TYPE TAccount
   DECLARE AccountNumber : INTEGER
   DECLARE Name : STRING
ENDTYPE

DECLARE Blank : TAccount
Blank.AccountNumber <- 0
Blank.Name <- ""
OPENFILE "Accounts.dat" FOR RANDOM
FOR Location <- 0 TO 6
   SEEK "Accounts.dat", Location
   PUTRECORD "Accounts.dat", Blank
NEXT Location
CLOSEFILE "Accounts.dat"''') + '''

  <h2>2 · SEEK, GETRECORD and PUTRECORD in Python</h2>
  <p>Python has no commands with these names, so this page builds them from <code>seek()</code>, <code>read()</code> and <code>write()</code>. Every record is stored as exactly the same number of bytes, so location <i>n</i> starts at byte <code>n × RecSize</code>.</p>
  <div class="code">''' + pc('''import struct
Layout = "<i20s"                      # a 4-byte integer then 20 bytes of text
RecSize = struct.calcsize(Layout)     # 24 bytes per record

def PutRecord(File, Rec):
    File.write(struct.pack(Layout, Rec.AccountNumber, Rec.Name.encode()))

def GetRecord(File):
    Num, Name = struct.unpack(Layout, File.read(RecSize))
    return TAccount(Num, Name.decode().rstrip("\\x00"))

def Hash(Key):
    return Key % 7''') + '''</div>
  <div class="tw"><table class="t">
    <tr><th>Pseudocode</th><th>Python</th></tr>
    <tr><td><code>OPENFILE "Accounts.dat" FOR RANDOM</code></td><td><code>File = open("Accounts.dat", "r+b")</code></td></tr>
    <tr><td><code>SEEK "Accounts.dat", Location</code></td><td><code>File.seek(Location * RecSize)</code></td></tr>
    <tr><td><code>GETRECORD "Accounts.dat", Current</code></td><td><code>Current = GetRecord(File)</code></td></tr>
    <tr><td><code>PUTRECORD "Accounts.dat", NewAccount</code></td><td><code>PutRecord(File, NewAccount)</code></td></tr>
    <tr><td><code>CLOSEFILE "Accounts.dat"</code></td><td><code>File.close()</code></td></tr>
  </table></div>
  <p class="note">Random files have been examined as pseudocode in Paper 3. They have not been asked as Python code in Paper 4, so this Python is here to show the same logic running, not because the exam will ask for it.</p>

  <h2>3 · The hash function</h2>
  <p>It must give the same location every time for the same key, and a valid location (0 to 6). <code>MOD</code> does both: the remainder after dividing by 7 is always 0 to 6.</p>
  ''' + both('''def Hash(Key):
    return Key % 7

Hash(24)    # 3
Hash(16)    # 2''', '''FUNCTION Hash(Key : INTEGER) RETURNS INTEGER
   RETURN Key MOD 7
ENDFUNCTION

Hash(24)    // 3
Hash(16)    // 2''') + '''

  <h2>4 · Storing a record at its hashed location</h2>
  <p>When the question does not mention collisions, this is the whole answer: calculate the location, SEEK, PUTRECORD.</p>
  ''' + both('''File = open("Accounts.dat", "r+b")
Location = Hash(NewAccount.AccountNumber)
File.seek(Location * RecSize)
PutRecord(File, NewAccount)
File.close()''', '''OPENFILE "Accounts.dat" FOR RANDOM
Location <- Hash(NewAccount.AccountNumber)
SEEK "Accounts.dat", Location
PUTRECORD "Accounts.dat", NewAccount
CLOSEFILE "Accounts.dat"''') + '''
  <div class="tip"><b class="h">The danger</b>PUTRECORD writes over whatever is at that location. If another account is already there, it is lost. That is why a safe version reads the location first.</div>

  <h2>5 · Collisions: the next free location</h2>
  <p>Two keys can hash to the same location: 24 and 10 both give 3. Read the location first. If it is empty (<code>AccountNumber = 0</code>) store the record. If not, move to the next location, wrapping from 6 back to 0 with <code>MOD 7</code>. This method is called <b>linear probing</b>. <code>Start</code> remembers where the search began, so if the program gets all the way round the file is full.</p>
  ''' + both('''File = open("Accounts.dat", "r+b")
Stored = False
Location = Hash(NewAccount.AccountNumber)
Start = Location
while True:
    File.seek(Location * RecSize)
    Current = GetRecord(File)
    if Current.AccountNumber == 0:
        File.seek(Location * RecSize)
        PutRecord(File, NewAccount)
        Stored = True
    else:
        Location = (Location + 1) % 7
    if Stored or Location == Start:
        break
File.close()
if not Stored:
    print("File full")''', '''OPENFILE "Accounts.dat" FOR RANDOM
Stored <- FALSE
Location <- Hash(NewAccount.AccountNumber)
Start <- Location
REPEAT
   SEEK "Accounts.dat", Location
   GETRECORD "Accounts.dat", Current
   IF Current.AccountNumber = 0 THEN
      PUTRECORD "Accounts.dat", NewAccount
      Stored <- TRUE
   ELSE
      Location <- (Location + 1) MOD 7
   ENDIF
UNTIL Stored OR Location = Start
IF NOT Stored THEN
   OUTPUT "File full"
ENDIF
CLOSEFILE "Accounts.dat"''') + '''
  <div class="tip"><b class="h">Why the second seek in Python?</b>In Python, reading a record moves the file position on to the next location, so the program seeks back before it writes. The exam mark scheme (M/J 2025, Paper 33, Question 11) writes with PUTRECORD straight after GETRECORD with no second SEEK, so in exam pseudocode the pointer stays at the location that was sought.</div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Leaving out <code>SEEK</code>. <code>PUTRECORD</code> writes wherever the pointer already is.</li>
    <li>Using <code>READFILE</code> or <code>WRITEFILE</code> on a random file. Random files use <code>GETRECORD</code> and <code>PUTRECORD</code>.</li>
    <li>Opening <code>FOR APPEND</code> or <code>FOR WRITE</code> instead of <code>FOR RANDOM</code>.</li>
    <li>Storing straight at the hashed location without checking whether it is already used.</li>
    <li>Adding 1 to the location without <code>MOD</code>, so it runs off the end of the file.</li>
    <li>Not stopping when the file is full, so the loop never ends.</li>
    <li>Not closing the file.</li>
  </ul>
'''

watch = '''
  <h2>1 · Storing a record at its hashed location</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · A collision, line by line</h2><p>Account 24 hashes to location 3, which is already taken. Watch the pointer move on until it finds an empty location.</p><div id="stB"></div>
  <h2>3 · When the file is full</h2><div id="stC"></div>
'''

SL = [(14, "Hall"), (22, "Ito"), None, (10, "Ray"), (18, "Cho"), (5, "Dev"), None]
rowt = lambda sl: [f"{s[0]} {s[1]}" if s else "(empty)" for s in sl]

stA = stp("stA", "Storing 16 at its hashed location", [
    dict(c="A new account arrives: number 16, name Fay. The file has 7 locations, two of them empty.", f=[F(20, 20, "Accounts.dat", rowt(SL), addr=True, lh=26)], t=[(330, 50, "NewAccount = 16 Fay", "lbl bd")]),
    dict(c="The hash function turns the key into a location: 16 MOD 7 = <b>2</b>.", f=[F(20, 20, "Accounts.dat", rowt(SL), addr=True, lh=26, hl=2)], t=[(330, 50, "NewAccount = 16 Fay", "lbl bd"), (330, 80, "Location = 16 MOD 7 = 2", "lbl bd t3")]),
    dict(c="<code>SEEK \"Accounts.dat\", 2</code> moves the file pointer to location 2.", f=[F(20, 20, "Accounts.dat", rowt(SL), addr=True, lh=26, hl=2, ptr=2, ptrLabel="pointer")], t=[(330, 50, "NewAccount = 16 Fay", "lbl bd"), (330, 80, "Location = 16 MOD 7 = 2", "lbl bd t3")]),
    dict(c="<code>GETRECORD</code> reads location 2 into <code>Current</code>. Its account number is 0, so the location is empty and safe to use.", f=[F(20, 20, "Accounts.dat", rowt(SL), addr=True, lh=26, hl=2, ptr=2, ptrLabel="pointer")], t=[(330, 50, "Current.AccountNumber = 0", "lbl bd t3"), (330, 80, "empty: store here", "sm")]),
    dict(c="<code>PUTRECORD</code> writes the new record at the pointer. No other location was touched.", f=[F(20, 20, "Accounts.dat", rowt(SL[:2] + [(16, "Fay")] + SL[3:]), addr=True, lh=26, nw=2)], t=[(330, 50, "Stored", "lbl bd t3")])],
    fh=235, dwell=3400)

PS = ['OPENFILE "Accounts.dat" FOR RANDOM', 'Stored <- FALSE', 'Location <- Hash(NewAccount.AccountNumber)', 'Start <- Location', 'REPEAT', '   SEEK "Accounts.dat", Location', '   GETRECORD "Accounts.dat", Current', '   IF Current.AccountNumber = 0 THEN', '      PUTRECORD "Accounts.dat", NewAccount', '      Stored <- TRUE', '   ELSE', '      Location <- (Location + 1) MOD 7', '   ENDIF', 'UNTIL Stored OR Location = Start', 'CLOSEFILE "Accounts.dat"']
PY = ['File = open("Accounts.dat", "r+b")', 'Stored = False', 'Location = Hash(NewAccount.AccountNumber)', 'Start = Location', 'while True:', '    File.seek(Location * RecSize)', '    Current = GetRecord(File)', '    if Current.AccountNumber == 0:', '        File.seek(Location * RecSize)', '        PutRecord(File, NewAccount)', '        Stored = True', '    else:', '        Location = (Location + 1) % 7', '    if Stored or Location == Start:', '        break', 'File.close()']


def trace_add(key, name, sl):
    sl = list(sl); steps = []
    st = dict(L="", S="", C="", T="FALSE")
    v = lambda: [("Location", st["L"]), ("Start", st["S"]), ("Current.AccountNumber", st["C"]), ("Stored", st["T"])]
    cols = lambda **kw: [F(20, 0, "Accounts.dat", rowt(sl), addr=True, lh=26, **kw)]
    info = lambda extra=None: [(330, 20, f"NewAccount = {key} {name}", "lbl bd")] + ([(330, 50, extra, "sm")] if extra else [])
    steps.append(dict(c="The file is opened for random access. Empty locations hold account number 0.", p=0, y=0, v=v(), f=cols(), t=info()))
    steps.append(dict(c="<code>Stored</code> starts FALSE: the record has not been written yet.", p=1, y=1, v=v(), f=cols(), t=info()))
    loc = key % 7; st["L"] = str(loc)
    steps.append(dict(c=f"The hash function gives the first location to try: {key} MOD 7 = <b>{loc}</b>.", p=2, y=2, v=v(), f=cols(hl=loc), t=info()))
    st["S"] = str(loc)
    steps.append(dict(c=f"<code>Start</code> remembers {loc}. If the loop ever comes back to it, every location has been tried.", p=3, y=3, v=v(), f=cols(hl=loc), t=info()))
    while True:
        cur = sl[loc]; st["C"] = str(cur[0]) if cur else "0"
        steps.append(dict(c=f"<code>SEEK</code> moves to location {loc} and <code>GETRECORD</code> reads it. " + (f"Account <b>{cur[0]}</b> ({cur[1]}) is stored here." if cur else "It is empty (account number 0)."), p=6, y=6, v=v(), f=cols(hl=loc, ptr=loc, ptrLabel="pointer"), t=info()))
        if cur:
            nxt = (loc + 1) % 7; st["L"] = str(nxt)
            steps.append(dict(c=f"{cur[0]} is not 0, so the location is taken. <b>Collision.</b> <code>Location</code> becomes ({loc} + 1) MOD 7 = {nxt}. <code>UNTIL</code> is false, so the loop repeats.", p=11, y=12, v=v(), f=cols(no=[loc]), t=info()))
            loc = nxt
        else:
            sl[loc] = (key, name)
            steps.append(dict(c=f"The location is empty, so <code>PUTRECORD</code> writes the new record here.", p=8, y=9, v=v(), f=cols(nw=loc), t=info()))
            st["T"] = "TRUE"
            steps.append(dict(c="<code>Stored</code> becomes TRUE.", p=9, y=10, v=v(), f=cols(nw=loc), t=info()))
            steps.append(dict(c="<code>UNTIL Stored OR Location = Start</code> is true, so the loop ends.", p=13, y=13, v=v(), f=cols(ok=[loc]), t=info()))
            break
    steps.append(dict(c=f"The file is closed. Account {key} ended up at location {loc}, not at its hashed location 3, because of the collisions on the way.", p=14, y=15, v=v(), f=cols(ok=[loc]), t=info()))
    return steps


stB = stp("stB", "Adding 24 with collisions", trace_add(24, "Eli", SL), PS, PY, lh=20, vw=170, fh=215, dwell=3000)

FULL = [(14, "Hall"), (22, "Ito"), (16, "Fay"), (10, "Ray"), (18, "Cho"), (5, "Dev"), (24, "Eli")]
stC = stp("stC", "A full file", [
    dict(c="Every location now holds a record. A new account arrives: 8 Gus. 8 MOD 7 = 1, so <code>Start</code> is 1.", f=[F(20, 20, "Accounts.dat", rowt(FULL), addr=True, lh=26, hl=1)], t=[(330, 30, "NewAccount = 8 Gus", "lbl bd"), (330, 60, "Location = Start = 1", "sm")]),
    dict(c="Location 1 is taken, so the program moves to 2. Then 3, 4, 5 and 6, which are all taken too.", f=[F(20, 20, "Accounts.dat", rowt(FULL), addr=True, lh=26, no=[1, 2, 3, 4, 5, 6])], t=[(330, 30, "NewAccount = 8 Gus", "lbl bd"), (330, 60, "Location goes 1, 2, 3, 4, 5, 6", "sm")]),
    dict(c="From 6, <code>(Location + 1) MOD 7</code> wraps round to <b>0</b>. The program has not run off the end of the file. Location 0 is taken as well.", f=[F(20, 20, "Accounts.dat", rowt(FULL), addr=True, lh=26, no=[0, 1, 2, 3, 4, 5, 6])], t=[(330, 30, "NewAccount = 8 Gus", "lbl bd"), (330, 60, "(6 + 1) MOD 7 = 0", "sm")]),
    dict(c="<code>Location</code> becomes 1 again, which equals <code>Start</code>. <code>UNTIL Stored OR Location = Start</code> is true while <code>Stored</code> is FALSE.", f=[F(20, 20, "Accounts.dat", rowt(FULL), addr=True, lh=26, hl=1)], t=[(330, 30, "Location = 1 = Start", "lbl bd t2"), (330, 60, "Stored = FALSE", "lbl bd t2")]),
    dict(c="<code>IF NOT Stored</code> is true, so the program outputs <b>File full</b>. The new record is not stored and no existing record was overwritten.", f=[F(20, 20, "Accounts.dat", rowt(FULL), addr=True, lh=26)], t=[(330, 30, "OUTPUT \"File full\"", "lbl bd t2")])],
    fh=235, dwell=3600)

explore = '''
  <h2>Lab 1 · Add a record</h2>
  <p>The file has 7 locations and the hash is Key MOD 7. Enter an account number and press Add. The table shows every location the program looks at. Fill the file until it is full.</p>
  <div class="card"><div class="btnrow"><label>Account number <input id="aK" size="5" value="24"></label> <button class="b pri" id="aB">Add</button> <button class="b" id="aR">Reset file</button></div><div id="aT"></div><div id="aF"></div><div class="verdict" id="aV"></div></div>

  <h2>Lab 2 · Hash calculator</h2>
  <p>Choose the number of locations and edit the keys. Keys that land on the same location are marked as collisions. The three keys in the box are the ones from the M/J 2023 exam question.</p>
  <div class="card"><div class="btnrow" id="hM"></div><div class="btnrow"><label>Keys <input id="hK" size="34" value="3003, 1029, 7630, 14, 22, 29"></label></div><div id="hO"></div><div class="verdict" id="hV"></div></div>
'''

lab = r'''
(function () {
  const START = [[14, "Hall"], [22, "Ito"], null, [10, "Ray"], [18, "Cho"], [5, "Dev"], null];
  let sl = START.slice();
  const show = (trail, loc, msg) => {
    $("#aF").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th><th>Record</th></tr>' + sl.map((s, i) => `<tr${i === loc ? ' style="background:var(--ok-soft);font-weight:700"' : ""}><td>${i}</td><td>${s ? s[0] + " " + s[1] : "(empty)"}</td></tr>`).join("") + "</table></div>";
    $("#aT").innerHTML = trail ? '<div class="tw"><table class="t mono"><tr><th>Look at location</th><th>GETRECORD finds</th><th>Action</th></tr>' + trail.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>" : "";
    $("#aV").textContent = msg;
  };
  $("#aB").onclick = () => {
    const k = parseInt($("#aK").value, 10);
    if (isNaN(k) || k < 1) { show(null, -1, "Enter a whole number above 0."); return; }
    if (sl.some((s) => s && s[0] === k)) { show(null, -1, "Account " + k + " is already stored."); return; }
    const start = k % 7; let loc = start, trail = [], done = false, steps = 0;
    while (!done) {
      steps++;
      if (!sl[loc]) { sl[loc] = [k, "New"]; trail.push([loc, "0 (empty)", "PUTRECORD: stored"]); done = true; break; }
      const nxt = (loc + 1) % 7;
      trail.push([loc, sl[loc][0] + " " + sl[loc][1], "taken: try " + nxt]); loc = nxt;
      if (loc === start) break;
    }
    if (done) show(trail, loc, `Hash(${k}) = ${k} MOD 7 = ${start}. ` + (steps === 1 ? "No collision: stored at its own location with one GETRECORD." : `${steps - 1} collision${steps > 2 ? "s" : ""}, so the record went to location ${loc} after ${steps} GETRECORDs.`));
    else show(trail, -1, `Hash(${k}) = ${start}. Every location was checked and none was empty: the file is full, so the program outputs "File full".`);
  };
  $("#aR").onclick = () => { sl = START.slice(); show(null, -1, "File reset."); };
  show(null, -1, "Press Add.");
})();

(function () {
  let m = 5; const M = [5, 7, 11];
  const paint = () => {
    $$("#hM button").forEach((b, i) => b.classList.toggle("pri", M[i] === m));
    const keys = $("#hK").value.split(",").map((s) => parseInt(s.trim(), 10)).filter((x) => !isNaN(x));
    const by = {}; keys.forEach((k) => { const h = k % m; (by[h] = by[h] || []).push(k); });
    $("#hO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Key</th><th>Key MOD ' + m + '</th><th></th></tr>' + keys.map((k) => { const h = k % m, c = by[h].length > 1; return `<tr${c ? ' style="background:var(--warn-soft)"' : ""}><td>${k}</td><td>${h}</td><td>${c ? "collision with " + by[h].filter((x) => x !== k).join(", ") : ""}</td></tr>`; }).join("") + "</table></div>";
    const n = Object.values(by).filter((a) => a.length > 1).length;
    $("#hV").textContent = n ? `${n} location${n > 1 ? "s are" : " is"} shared by more than one key. The second key to arrive at each would have to use the next free location.` : "Every key has its own location, so there are no collisions with this set of keys.";
  };
  $("#hM").innerHTML = M.map((x) => `<button class="b" data-m="${x}">MOD ${x}</button>`).join("");
  $$("#hM button").forEach((b) => (b.onclick = () => { m = +b.dataset.m; paint(); }));
  $("#hK").oninput = paint; paint();
})();
''' + CLASSIFY("cl1", "Which part of adding a record to a random file is this?", ["Hash function", "Collision handling", "File commands"],
    [("Location <- Key MOD 7", 0), ("Turns the key into a location", 0), ("Two keys give the same location", 1), ("Move to the next location, wrapping round", 1), ("Stop when the location is back at Start", 1), ("SEEK", 2), ("GETRECORD", 2), ("PUTRECORD", 2)],
    "Hash finds the first location. Collision handling finds a free one. SEEK, GETRECORD and PUTRECORD do the file work.") + ORDER(
    "Put the steps for adding a record to a random file in order.",
    ["Open the file FOR RANDOM", "Calculate the location with the hash function", "SEEK to the location", "GETRECORD to see what is there", "If it is empty, PUTRECORD the new record", "If it is taken, move to the next location and repeat", "CLOSEFILE"],
    "Open, hash, seek, read, store if empty or try the next, close.") + MATCH([
    ["Hash function", "Turns a key into a location"], ["Collision", "Two keys giving the same location"], ["Linear probing", "Trying the next location until a free one is found"], ["Empty location", "A record with AccountNumber 0"], ["MOD", "Wraps the location back to 0 after the last one"], ["SEEK", "Moves the pointer to a location before GETRECORD or PUTRECORD"]]) + CALC([
    {"q": "Hash(Key) = Key MOD 7. At which location is account 24 first tried?", "a": 3, "unit": "", "tol": 0.01, "hint": "7 × 3 = 21, so 24 − 21.", "sol": "<b>3</b>."},
    {"q": "Locations 3, 4 and 5 are taken and 6 is empty. Account 24 hashes to 3. How many GETRECORD statements run before it is stored?", "a": 4, "unit": "", "tol": 0.01, "hint": "One for each location looked at, including the empty one.", "sol": "<b>4</b> (locations 3, 4, 5, 6)."},
    {"q": "Hash is Key MOD 5. What is the hash value of 1029?", "a": 4, "unit": "", "tol": 0.01, "hint": "1029 = 5 × 205 + 4.", "sol": "<b>4</b>."},
    {"q": "Hash is Key MOD 5. What is the hash value of 7630?", "a": 0, "unit": "", "tol": 0.01, "hint": "7630 divides exactly by 5.", "sol": "<b>0</b>."},
    {"q": "A file has 7 locations and all are taken. How many locations are looked at before the program decides the file is full?", "a": 7, "unit": "", "tol": 0.01, "hint": "It goes all the way round, back to Start.", "sol": "<b>7</b>."},
    {"q": "In the Python version each record is 24 bytes. At which byte does File.seek go for location 5?", "a": 120, "unit": "", "tol": 0.01, "hint": "5 × 24.", "sol": "<b>120</b>."}]) + MCQ([
    ("Which file mode is used to store records at calculated locations?", ["FOR APPEND", "FOR WRITE", "FOR RANDOM", "FOR READ"], 2, "Random access needs FOR RANDOM."),
    ("What must come before PUTRECORD so the record goes in the right place?", ["READFILE", "EOF", "SEEK", "CLOSEFILE"], 2, "SEEK moves the pointer to the location."),
    ("What is a collision?", ["The file is full", "Two keys hash to the same location", "A record is deleted", "The file is closed"], 1, "The location is already used by a different record."),
    ("Why is MOD used when moving to the next location?", ["To make it faster", "To wrap round to 0 after the last location", "To sort the records", "To empty the location"], 1, "(Location + 1) MOD 7 never reaches 7."),
    ("How does the program know a location is empty?", ["EOF is true", "The record's key is 0", "The pointer is at 0", "GETRECORD returns an error"], 1, "Blank records have AccountNumber 0."),
    ("What does the loop compare Location with, to detect a full file?", ["MaxSize", "Start", "0", "The key"], 1, "Back at Start means every location has been tried.")], "qz1") + CARDS([
    ("Random file", "Equal-sized records at numbered locations. Jump with SEEK."), ("Hash function", "Key MOD 7 gives a location from 0 to 6."), ("Collision", "Two keys with the same hashed location."), ("Linear probing", "Try the next location, wrapping with MOD."),
    ("Empty location", "A blank record: AccountNumber 0."), ("Start", "Where the search began. Back at Start means the file is full."), ("SEEK then PUTRECORD", "Move first, then write at the pointer."), ("FOR RANDOM", "The open mode for random access.")])

real = RWNOTE + (
    rw("School lockers", "A locker is assigned as student ID MOD number of lockers. If that locker is already taken, the student is given the next free one, wrapping round to the start after the last. That is the same method as linear probing.", "hash for the first choice, next location on a collision.") +
    rw("A bank's account file", "Millions of records are stored at locations worked out from the account number. A new account is written straight to its location without reading any other record, which is why a random file is fast to add to.", "direct access: SEEK to the calculated location, then PUTRECORD.") +
    rw("A hotel booking system", "Each booking reference is turned into a location in the booking file. When two references give the same location the system looks at the following locations until it finds an empty one.", "collisions are handled by checking the next location.") +
    rw("A full file", "A small random file used as a cache has 500 slots. When all are taken the program has to report that it is full or throw an old record away; it must never overwrite a record by accident.", "the Start check stops the loop and the program reports the file is full."))

review = (
    req("2 marks", "State", "What is meant by a collision when a record is stored in a random file?", "Two keys, one location.", mks(["Two different records (keys) produce the same hash value", "so the location they should go in is already used"])) +
    req("3 marks", "Calculate", "The hash function is <code>Key MOD 7</code>. State the location for the keys 52, 31 and 15, and say which two collide.", "Divide by 7 and keep the remainder.", mks(["52 gives 3", "31 gives 3 and 15 gives 1", "52 and 31 collide at location 3"]) + "<p>52 = 7 × 7 + 3, 31 = 7 × 4 + 3, 15 = 7 × 2 + 1.</p>") +
    req("5 marks", "Complete", "Write pseudocode that stores <code>NewAccount</code> in <code>Accounts.dat</code> at the location given by <code>Hash()</code>. Assume there is no collision.", "Open for random, hash, SEEK, PUTRECORD, close.", pc('''OPENFILE "Accounts.dat" FOR RANDOM
Location <- Hash(NewAccount.AccountNumber)
SEEK "Accounts.dat", Location
PUTRECORD "Accounts.dat", NewAccount
CLOSEFILE "Accounts.dat"'''), "Leaving out SEEK, or opening FOR WRITE.") +
    req("6 marks", "Write", "Write Python that stores <code>NewAccount</code> in the next empty location from its hashed location, wrapping round and stopping if the file is full. Use <code>GetRecord</code> and <code>PutRecord</code>.", "Read each location in turn; an empty one has AccountNumber 0.", pc('''File = open("Accounts.dat", "r+b")
Stored = False
Location = Hash(NewAccount.AccountNumber)
Start = Location
while True:
    File.seek(Location * RecSize)
    Current = GetRecord(File)
    if Current.AccountNumber == 0:
        File.seek(Location * RecSize)
        PutRecord(File, NewAccount)
        Stored = True
    else:
        Location = (Location + 1) % 7
    if Stored or Location == Start:
        break
File.close()'''), "Forgetting the second seek, so the record is written at the next location instead of the empty one.") +
    req("2 marks", "Explain", "Why is the new location calculated with <code>(Location + 1) MOD 7</code> rather than <code>Location + 1</code>?", "What would happen at location 6.", mks(["Location 6 is the last location, and 6 + 1 = 7 is outside the file", "MOD 7 wraps the location back to 0 so the search continues from the start of the file"])))

where = [("M/J 2025", "33", "11", "5", "Complete the insertion of a new stock item into the next empty location of a random file"),
         ("M/J 2023", "32", "2(b)", "2", "Hash values using modulus 5"),
         ("M/J 2024", "32", "7(a), (b)(ii)", "2 + 2", "Direct access, and how a record is located in a random file"),
         ("O/N 2023", "31, 33", "4(a)", "4", "Describe sequential and random file organisation (random part: hashing, direct update)")]
past = OLDQ["M/J 2025 · 9618/33 · Q11"] + peq(SRC("s23", "32", "Q2(b)"), "2 marks", "Complete",
    "A hashing algorithm is used to calculate storage locations for records in a random access file. The algorithm calculates hash values using the function modulus 5, which gives the remainder after integer division. For example, 3003 modulus 5 = 3, so the record key 3003 gives a hash value of 3. Complete the table to show the remaining hash values.<table class=\"t\"><tr><th>Record key</th><th>Hash value</th></tr><tr><td>3003</td><td>3</td></tr><tr><td>1029</td><td></td></tr><tr><td>7630</td><td></td></tr></table>",
    "Divide by 5 and keep the remainder. A number ending in 0 or 5 divides exactly.",
    "<p>One mark for each correct value (maximum 2): 1029 gives " + mks(["4"]) + " and 7630 gives " + mks(["0"]) + ".</p>",
    "Giving the result of the division (205 or 1526) instead of the remainder.") + peq(SRC("s24", "32", "Q7(a), (b)(ii)"), "2 + 2 marks", "Outline / Explain",
    "(a) Outline what is meant by direct access as a method of file access. (b)(ii) Explain how direct access is used to locate a specific record in random files.",
    "(a) is about not reading other records. (b)(ii) is the hash, the calculated address and what happens if the record is not there.",
    "<p>(a) " + mks(["A record can be found in a file without other records being read", "using the key field of the target record (the location is found with a hashing algorithm)"]) + "</p><p>(b)(ii) " + mks(["A hashing algorithm is used on the key field of the record", "to calculate the address of the location where the target record is expected to be stored", "Another method is used if it is not at the expected location, for example linear probing or an overflow area"], "a") + " (maximum 2)</p>",
    "Writing only that the record is 'found quickly'. The marks are for the key, the hash and the calculated address.")
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Random files are asked in Paper 3 as completed pseudocode and as written descriptions. Handling collisions by checking the next location is accepted in the mark scheme as an example of a method for finding a record that is not at its expected location."

tipsl = [("Always SEEK first.", "SEEK to the location before every GETRECORD or PUTRECORD."), ("Open FOR RANDOM.", "APPEND and WRITE are for text files."), ("Hash first.", "Location comes from the key, not from a loop, unless there is a collision."), ("Check before you write.", "PUTRECORD overwrites. Read the location and test that it is empty."), ("Wrap round with MOD.", "(Location + 1) MOD 7 never leaves the file."), ("Say what empty means.", "A blank record, such as AccountNumber 0 or an empty string.")]
sents = [("Describe direct access", "A record is found without reading the other records, because its location is calculated from the key field."), ("Describe a hash function", "It takes the key field and calculates the address at which the record is stored."), ("Describe a collision", "Two different keys give the same location, so another method is used to place the second record.")]
words = [("Complete", "Fill in the missing lines of the given pseudocode."), ("Describe", "Give the main features in connected points."), ("Explain", "A reason as well as the fact."), ("State", "A short fact.")]

finishf("ac20f3", "ac-20-2-1-adding-to-random-file", "Adding a Record to a Random File",
        "Hashing a key to a location, SEEK and PUTRECORD, handling a collision with the next free location, and detecting a full file; pseudocode and Python side by side, with a line-by-line animation.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words)
