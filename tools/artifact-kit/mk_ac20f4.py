"""20.2.1 extra resource: finding a record in a random file. Run: python3 tools/artifact-kit/mk_ac20f4.py"""
from ac20f import *

OLDQ = old_questions()

HELP = pc('''import struct
class TAccount:
    def __init__(self, AccountNumber=0, Name=""):
        self.AccountNumber = AccountNumber
        self.Name = Name

Layout = "<i20s"
RecSize = struct.calcsize(Layout)     # 24 bytes per record

def GetRecord(File):
    Num, Name = struct.unpack(Layout, File.read(RecSize))
    return TAccount(Num, Name.decode().rstrip("\\x00"))

def Hash(Key):
    return Key % 7''')

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A random file lets a program <b>go straight to a record</b> instead of reading the ones before it. To find a record by its <b>key</b>, the program calculates the location with the same hash function that stored it, uses <code>SEEK</code> to move there, and <code>GETRECORD</code> to read it. It then <b>compares the key</b> of the record it read with the key it wants: if they match, the record is found. If the location holds a different record the wanted one may have been moved on by a collision, so the program checks the <b>next locations</b>, and gives up at an <b>empty location</b> or after every location has been tried. To find a record by a field that is <b>not the key</b>, such as a name, the hash cannot help, so every location is read in turn until the value is found.</p></div>

  <h2>1 · The file used on this page</h2>
  <p>The same file as the previous page: 7 locations, <code>Hash(Key) = Key MOD 7</code>, collisions handled by trying the next location, an empty location holding account number 0. Account 24 hashes to 3, but 3, 4 and 5 were taken when it was added, so it was stored at location 6.</p>
  <div class="tw"><table class="t mono">
    <tr><th>Location</th><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr>
    <tr><th>Record</th><td>14 Hall</td><td>22 Ito</td><td>(empty)</td><td>10 Ray</td><td>18 Cho</td><td>5 Dev</td><td>24 Eli</td></tr>
  </table></div>
  <p>The Python on this page uses these helpers, built on the previous page:</p>
  <div class="code">''' + HELP + '''</div>

  <h2>2 · Direct access: one SEEK, one GETRECORD</h2>
  <p>When the question does not mention collisions, finding a record is four steps: calculate the location, SEEK, GETRECORD, use the record. This is how the exam questions on random files are written.</p>
  ''' + both('''File = open("Accounts.dat", "rb")
Location = Hash(SearchKey)
File.seek(Location * RecSize)
Current = GetRecord(File)
if Current.AccountNumber == SearchKey:
    print(Current.AccountNumber, Current.Name)
else:
    print("Not found")
File.close()''', '''OPENFILE "Accounts.dat" FOR RANDOM
Location <- Hash(SearchKey)
SEEK "Accounts.dat", Location
GETRECORD "Accounts.dat", Current
IF Current.AccountNumber = SearchKey THEN
   OUTPUT Current.AccountNumber, Current.Name
ELSE
   OUTPUT "Not found"
ENDIF
CLOSEFILE "Accounts.dat"''') + '''
  <p>The comparison matters. Searching for 17 gives location 3, but location 3 holds account 10. Without the <code>IF</code> the program would output the wrong customer.</p>

  <h2>3 · The record may have been moved: follow the chain</h2>
  <p>Searching for 24 starts at location 3 and finds account 10, so it is not there. It looks at 4, then 5, then 6 and finds 24. The search follows the same steps the insert took. It stops when the key is found, when it reaches an <b>empty location</b> (a record with this key would have been stored there, so it is not in the file), or when it has looked at every location.</p>
  ''' + both('''File = open("Accounts.dat", "rb")
Location = Hash(SearchKey)
Count = 0
Found = False
while True:
    File.seek(Location * RecSize)
    Rec = GetRecord(File)
    if Rec.AccountNumber == SearchKey:
        Found = True
    else:
        Location = (Location + 1) % 7
        Count = Count + 1
    if Found or Rec.AccountNumber == 0 or Count == 7:
        break
File.close()
if Found:
    print(Rec.AccountNumber, Rec.Name)
else:
    print("Not found")''', '''OPENFILE "Accounts.dat" FOR RANDOM
Location <- Hash(SearchKey)
Count <- 0
Found <- FALSE
REPEAT
   SEEK "Accounts.dat", Location
   GETRECORD "Accounts.dat", Rec
   IF Rec.AccountNumber = SearchKey THEN
      Found <- TRUE
   ELSE
      Location <- (Location + 1) MOD 7
      Count <- Count + 1
   ENDIF
UNTIL Found OR Rec.AccountNumber = 0 OR Count = 7
CLOSEFILE "Accounts.dat"
IF Found THEN
   OUTPUT Rec.AccountNumber, Rec.Name
ELSE
   OUTPUT "Not found"
ENDIF''') + '''
  <div class="tw"><table class="t">
    <tr><th>The loop ends because</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><code>Found</code> is TRUE</td><td>The key matches the record read</td><td>24: found at location 6 after 4 reads</td></tr>
    <tr><td>The record read is empty</td><td>The key would have been stored here if it were in the file</td><td>9: location 2 is empty, 1 read</td></tr>
    <tr><td><code>Count = 7</code></td><td>Every location has been read and none matched</td><td>A key that is not stored, in a file with no empty location</td></tr>
  </table></div>

  <h2>4 · Finding a record by a field that is not the key</h2>
  <p>The hash function turns an <b>account number</b> into a location. It cannot turn a <b>name</b> into one, because the records were not placed by name. So the program starts at location 0 and reads every location until the name matches or the file ends. A flag stops the loop as soon as the record is found.</p>
  ''' + both('''File = open("Accounts.dat", "rb")
Location = 0
Found = False
while not Found and Location < 7:
    File.seek(Location * RecSize)
    Rec = GetRecord(File)
    if Rec.Name == SearchName:
        Found = True
    else:
        Location = Location + 1
File.close()
if Found:
    print(Rec.AccountNumber, Rec.Name)
else:
    print("Customer does not exist.")''', '''OPENFILE "Accounts.dat" FOR RANDOM
Location <- 0
Found <- FALSE
WHILE NOT Found AND Location <= 6
   SEEK "Accounts.dat", Location
   GETRECORD "Accounts.dat", Rec
   IF Rec.Name = SearchName THEN
      Found <- TRUE
   ELSE
      Location <- Location + 1
   ENDIF
ENDWHILE
CLOSEFILE "Accounts.dat"
IF Found THEN
   OUTPUT Rec.AccountNumber, Rec.Name
ELSE
   OUTPUT "Customer does not exist."
ENDIF''') + '''

  <h2>5 · How many records are read?</h2>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>Records read to find one record</th></tr>
    <tr><td>Random file, search by key, no collision</td><td><b>1</b></td></tr>
    <tr><td>Random file, search by key, collisions</td><td>1 plus the number of locations moved on (4 for account 24)</td></tr>
    <tr><td>Random file, search by another field</td><td>Up to every location in the file</td></tr>
    <tr><td>Serial or sequential file</td><td>From the start of the file, record by record, until found (a sequential file can stop once the key has been passed)</td></tr>
  </table></div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Leaving out <code>SEEK</code>, so GETRECORD reads wherever the pointer was.</li>
    <li>Not comparing the key of the record read with the key wanted.</li>
    <li>Using <code>READFILE</code> on a random file. Random files use <code>GETRECORD</code>.</li>
    <li>Using the hash to search for a name. The hash is for the key field only.</li>
    <li>A loop that never ends because it does not stop at an empty location, at the end of the file or when the record is found.</li>
    <li>Forgetting the message when the record is not found.</li>
    <li>Not closing the file.</li>
  </ul>
'''

watch = '''
  <h2>1 · Direct access to a record</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · A record moved by a collision, line by line</h2><p>Account 24 hashes to location 3 but was stored at 6. Watch the search follow the chain.</p><div id="stB"></div>
  <h2>3 · A record that is not in the file</h2><div id="stC"></div>
  <h2>4 · Searching by name: every location is read</h2><div id="stD"></div>
'''

FILEB = [(14, "Hall"), (22, "Ito"), None, (10, "Ray"), (18, "Cho"), (5, "Dev"), (24, "Eli")]
rowt = lambda sl: [f"{s[0]} {s[1]}" if s else "(empty)" for s in sl]
R = rowt(FILEB)
info = lambda *lines: [(330, 20 + 30 * i, s, c) for i, (s, c) in enumerate(lines)]

stA = stp("stA", "Finding account 18 directly", [
    dict(c="A customer gives account number <b>18</b>. The file has 7 locations.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26)], t=info(("SearchKey = 18", "lbl bd"))),
    dict(c="The hash function gives the location: 18 MOD 7 = <b>4</b>.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, hl=4)], t=info(("SearchKey = 18", "lbl bd"), ("Location = 18 MOD 7 = 4", "lbl bd t3"))),
    dict(c="<code>SEEK \"Accounts.dat\", 4</code> jumps straight to location 4. Locations 0 to 3 are not read.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, hl=4, ptr=4, ptrLabel="pointer")], t=info(("SearchKey = 18", "lbl bd"), ("Location = 4", "lbl bd t3"))),
    dict(c="<code>GETRECORD</code> reads the record at the pointer: 18 Cho. Its account number equals <code>SearchKey</code>, so it is the record wanted.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, ok=[4], ptr=4, ptrLabel="pointer")], t=info(("SearchKey = 18", "lbl bd"), ("Rec = 18 Cho", "lbl bd t3"), ("Found after 1 record read", "sm"))),
    dict(c="A serial file would have had to read from the start until it reached account 18. Here one record was read.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, ok=[4])], t=info(("1 record read", "lbl bd t3"), ("no other record was touched", "sm")))],
    fh=235, dwell=3400)

PS = ['OPENFILE "Accounts.dat" FOR RANDOM', 'Location <- Hash(SearchKey)', 'Count <- 0', 'Found <- FALSE', 'REPEAT', '   SEEK "Accounts.dat", Location', '   GETRECORD "Accounts.dat", Rec', '   IF Rec.AccountNumber = SearchKey THEN', '      Found <- TRUE', '   ELSE', '      Location <- (Location + 1) MOD 7', '      Count <- Count + 1', '   ENDIF', 'UNTIL Found OR Rec.AccountNumber = 0 OR Count = 7', 'CLOSEFILE "Accounts.dat"']
PY = ['File = open("Accounts.dat", "rb")', 'Location = Hash(SearchKey)', 'Count = 0', 'Found = False', 'while True:', '    File.seek(Location * RecSize)', '    Rec = GetRecord(File)', '    if Rec.AccountNumber == SearchKey:', '        Found = True', '    else:', '        Location = (Location + 1) % 7', '        Count = Count + 1', '    if Found or Rec.AccountNumber == 0 or Count == 7:', '        break', 'File.close()']


def trace_find(key, sl):
    steps = []; st = dict(L="", N="", R="", F="")
    v = lambda: [("Location", st["L"]), ("Count", st["N"]), ("Rec.AccountNumber", st["R"]), ("Found", st["F"])]
    cols = lambda **kw: [F(20, 0, "Accounts.dat", rowt(sl), addr=True, lh=26, **kw)]
    inf = lambda extra=None: [(330, 20, f"SearchKey = {key}", "lbl bd")] + ([(330, 50, extra, "sm")] if extra else [])
    steps.append(dict(c="The file is opened for random access.", p=0, y=0, v=v(), f=cols(), t=inf()))
    loc = key % 7; st["L"] = str(loc)
    steps.append(dict(c=f"The first location to try is the hash of the key: {key} MOD 7 = <b>{loc}</b>.", p=1, y=1, v=v(), f=cols(hl=loc), t=inf()))
    st["N"] = "0"; st["F"] = "FALSE"
    steps.append(dict(c="<code>Count</code> will count the locations checked, so the search cannot go round forever. <code>Found</code> starts FALSE.", p=3, y=3, v=v(), f=cols(hl=loc), t=inf()))
    count, reads = 0, 0
    while True:
        cur = sl[loc]; reads += 1; st["R"] = str(cur[0]) if cur else "0"
        who = f"account <b>{cur[0]}</b> ({cur[1]})" if cur else "an empty record (account number 0)"
        steps.append(dict(c=f"<code>SEEK</code> to location {loc}, then <code>GETRECORD</code>: it holds {who}.", p=6, y=6, v=v(), f=cols(hl=loc, ptr=loc, ptrLabel="pointer"), t=inf(f"records read: {reads}")))
        if cur and cur[0] == key:
            st["F"] = "TRUE"
            steps.append(dict(c=f"{cur[0]} equals {key}, so <code>Found</code> becomes TRUE.", p=8, y=8, v=v(), f=cols(ok=[loc]), t=inf(f"records read: {reads}")))
            steps.append(dict(c=f"<code>UNTIL Found ...</code> is true, so the loop ends. Account {key} was found after <b>{reads}</b> records were read.", p=13, y=12, v=v(), f=cols(ok=[loc]), t=inf(f"records read: {reads}")))
            break
        if not cur:
            steps.append(dict(c=f"Not the record wanted. The location is empty, so a record with key {key} would have been stored here: it is not in the file. <code>UNTIL</code> is true.", p=13, y=12, v=v(), f=cols(no=[loc]), t=inf(f"records read: {reads}")))
            break
        nxt = (loc + 1) % 7; count += 1; st["L"] = str(nxt); st["N"] = str(count)
        steps.append(dict(c=f"{cur[0]} is not {key}. <code>Location</code> becomes {nxt} and <code>Count</code> becomes {count}. <code>UNTIL</code> is false, so the loop repeats.", p=11, y=11, v=v(), f=cols(no=[loc]), t=inf(f"records read: {reads}")))
        loc = nxt
    steps.append(dict(c="The file is closed. The program outputs the record, or \"Not found\" if <code>Found</code> is FALSE.", p=14, y=14, v=v(), f=cols(ok=[loc]) if cur and cur[0] == key else cols(), t=inf(f"records read: {reads}")))
    return steps


stB = stp("stB", "Finding 24 after a collision", trace_find(24, FILEB), PS, PY, lh=20, vw=170, fh=215, dwell=3000)

stC = stp("stC", "A key that is not in the file", [
    dict(c="A customer gives account number <b>9</b>. 9 MOD 7 = <b>2</b>.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, hl=2)], t=info(("SearchKey = 9", "lbl bd"), ("Location = 9 MOD 7 = 2", "lbl bd t3"))),
    dict(c="<code>SEEK</code> and <code>GETRECORD</code> read location 2. It is <b>empty</b>.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, hl=2, ptr=2, ptrLabel="pointer")], t=info(("SearchKey = 9", "lbl bd"), ("Rec.AccountNumber = 0", "lbl bd t2"))),
    dict(c="If account 9 had been added, it would have been stored at location 2, or earlier in the chain. Location 2 is empty, so it is not in the file. The program outputs \"Not found\" after <b>1</b> read.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, no=[2])], t=info(("OUTPUT \"Not found\"", "lbl bd t2"), ("1 record read", "sm"))),
    dict(c="A key like 17 also hashes to 3 and has to follow the chain 3, 4, 5, 6, 0, 1 before reaching the empty location 2: 7 reads. The empty location is what stops the search.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, no=[3, 4, 5, 6, 0, 1], hl=2)], t=info(("SearchKey = 17", "lbl bd"), ("17 MOD 7 = 3", "sm"), ("chain: 3, 4, 5, 6, 0, 1, then 2", "sm")))],
    fh=235, dwell=3600)

order = [0, 1, 2, 3, 4]
stepsD = [dict(c="The customer is known by name only: <b>Cho</b>. The hash function works on account numbers, so it cannot give a location for a name. The search starts at location 0.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26)], t=info(("SearchName = Cho", "lbl bd")))]
for i in range(5):
    s = FILEB[i]
    steps_c = f"Location {i}: <code>GETRECORD</code> reads " + (f"{s[0]} {s[1]}. " + ("The name matches, so <code>Found</code> is TRUE and the loop stops." if s[1] == "Cho" else f"{s[1]} is not Cho, so <code>Location</code> becomes {i + 1}.") if s else "an empty record. Not Cho, so move on.")
    stepsD.append(dict(c=steps_c, f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, hl=i if s and s[1] != "Cho" else None, ok=[i] if s and s[1] == "Cho" else None, no=list(range(i)) if i else None, ptr=i, ptrLabel="pointer")], t=info(("SearchName = Cho", "lbl bd"), (f"records read: {i + 1}", "sm"))))
stepsD.append(dict(c="Cho was found after <b>5</b> reads. Searching by key would have taken 1. If the name were not in the file, all 7 locations would be read before the loop ended.", f=[F(20, 20, "Accounts.dat", R, addr=True, lh=26, ok=[4])], t=info(("5 reads by name", "lbl bd t2"), ("1 read by key", "lbl bd t3"))))
stD = stp("stD", "Searching by name", stepsD, fh=235, dwell=3000)

explore = '''
  <h2>Lab 1 · Find an account by key</h2>
  <p>The file holds the records in the table. Enter an account number, or use the quick buttons, and read the trail of locations the program looks at.</p>
  <div class="card"><div class="btnrow"><label>Account number <input id="fK" size="5" value="24"></label> <button class="b pri" id="fB">Find</button> <button class="b" data-k="18">Try 18</button> <button class="b" data-k="24">Try 24</button> <button class="b" data-k="9">Try 9</button> <button class="b" data-k="17">Try 17</button></div><div id="fF"></div><div id="fT"></div><div class="verdict" id="fV"></div></div>

  <h2>Lab 2 · By key or by name?</h2>
  <p>Pick a customer to find by name. The program reads from location 0 until the name matches. Compare the reads with a search by key.</p>
  <div class="card"><div class="btnrow" id="nB"></div><div id="nT"></div><div class="verdict" id="nV"></div></div>
'''

lab = r'''
const FILE = [[14, "Hall"], [22, "Ito"], null, [10, "Ray"], [18, "Cho"], [5, "Dev"], [24, "Eli"]];
(function () {
  const table = (loc) => '<div class="tw"><table class="t mono"><tr><th>Location</th>' + FILE.map((s, i) => `<td${i === loc ? ' style="background:var(--ok-soft);font-weight:700"' : ""}>${i}</td>`).join("") + "</tr><tr><th>Record</th>" + FILE.map((s) => `<td>${s ? s[0] + " " + s[1] : "(empty)"}</td>`).join("") + "</tr></table></div>";
  const find = () => {
    const k = parseInt($("#fK").value, 10);
    if (isNaN(k) || k < 1) { $("#fF").innerHTML = table(-1); $("#fT").innerHTML = ""; $("#fV").textContent = "Enter a whole number above 0."; return; }
    let loc = k % 7, count = 0, trail = [], found = -1;
    while (true) {
      const r = FILE[loc];
      if (r && r[0] === k) { trail.push([loc, r[0] + " " + r[1], "key matches: Found"]); found = loc; break; }
      if (!r) { trail.push([loc, "(empty)", "empty: not in the file"]); break; }
      trail.push([loc, r[0] + " " + r[1], "not " + k + ": try " + ((loc + 1) % 7)]); loc = (loc + 1) % 7; count++;
      if (count === 7) break;
    }
    $("#fF").innerHTML = table(found);
    $("#fT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>SEEK location</th><th>GETRECORD finds</th><th>Result</th></tr>' + trail.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>";
    $("#fV").textContent = `Hash(${k}) = ${k} MOD 7 = ${k % 7}. ` + (found >= 0 ? `Found at location ${found} after ${trail.length} record${trail.length > 1 ? "s" : ""} read.` : `Not found after ${trail.length} record${trail.length > 1 ? "s" : ""} read. ` + (count === 7 ? "Every location was tried." : "An empty location ended the search."));
  };
  $("#fB").onclick = find; $$("[data-k]").forEach((b) => (b.onclick = () => { $("#fK").value = b.dataset.k; find(); })); find();
})();

(function () {
  const names = ["Hall", "Ray", "Cho", "Eli", "Zed"];
  $("#nB").innerHTML = names.map((n, i) => `<button class="b" data-i="${i}">${n}</button>`).join("");
  const show = (i) => {
    $$("#nB button").forEach((b, k) => b.classList.toggle("pri", k === i));
    const n = names[i]; let loc = 0, rows = [], hit = -1;
    while (loc < 7) { const r = FILE[loc]; rows.push([loc, r ? r[0] + " " + r[1] : "(empty)", r && r[1] === n ? "name matches: Found" : "no match"]); if (r && r[1] === n) { hit = loc; break; } loc++; }
    $("#nT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location read</th><th>Record</th><th>Result</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("") + "</table></div>";
    const acc = hit >= 0 ? FILE[hit][0] : null;
    const viaKey = (a) => { let l = a % 7, c = 1; while (FILE[l][0] !== a) { l = (l + 1) % 7; c++; } return c; };
    $("#nV").textContent = hit >= 0 ? `${n} was found after ${rows.length} read${rows.length > 1 ? "s" : ""}. Knowing the account number (${acc}), the hash would have found it in ${viaKey(acc)} read${viaKey(acc) > 1 ? "s" : ""}.` : `${n} is not in the file. All 7 locations were read before the program could say so.`;
  };
  $$("#nB button").forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(2);
})();
''' + CLASSIFY("cl1", "Is the search done by key (using the hash) or by another field (reading every location)?", ["By key (hash)", "By another field (scan)"],
    [("Location <- Hash(SearchKey)", 0), ("Start at location 0 and read each location in turn", 1), ("Usually one GETRECORD", 0), ("May read every location in the file", 1), ("Compares Rec.Name with SearchName", 1), ("Compares Rec.AccountNumber with SearchKey", 0), ("Needs the same hash function that stored the record", 0), ("Stops when Found is TRUE or the last location has been read", 1)],
    "The hash only works on the key field. Any other field has to be searched for.") + ORDER(
    "Put the steps for finding a record by its key in a random file in order.",
    ["Open the file FOR RANDOM", "Calculate the location with the hash function", "SEEK to the location", "GETRECORD the record there", "Compare its key with the key wanted", "If it does not match and is not empty, move on to the next location", "CLOSEFILE and output the record or Not found"],
    "Open, hash, seek, read, compare, follow the chain, close and report.") + MATCH([
    ["Direct access", "Reaching a record without reading the ones before it"], ["Hash function", "Turns the key into the location to look at first"], ["Empty location", "Where a search by key can stop: the record is not in the file"], ["Count", "Counts locations checked so a full file cannot loop forever"], ["Found", "A flag that becomes TRUE when the key matches"], ["Scan", "Reading each location in turn when searching by a field that is not the key"]]) + CALC([
    {"q": "Account 18 is stored at its hashed location (18 MOD 7). How many records are read to find it?", "a": 1, "unit": "", "tol": 0.01, "hint": "SEEK goes straight there.", "sol": "<b>1</b>."},
    {"q": "Account 24 hashes to 3 and is stored at 6, because 3, 4 and 5 were taken. How many records are read to find it?", "a": 4, "unit": "", "tol": 0.01, "hint": "Locations 3, 4, 5 and 6.", "sol": "<b>4</b>."},
    {"q": "Account 9 hashes to location 2, which is empty. How many records are read before the program concludes it is not in the file?", "a": 1, "unit": "", "tol": 0.01, "hint": "An empty location ends the search.", "sol": "<b>1</b>."},
    {"q": "A name is not in the file, which has 7 locations. How many records are read in a search by name?", "a": 7, "unit": "", "tol": 0.01, "hint": "Every location is read.", "sol": "<b>7</b>."},
    {"q": "A serial file has 500 records and the one wanted is the 350th. How many records are read to reach it?", "a": 350, "unit": "", "tol": 0.01, "hint": "From the start, one at a time.", "sol": "<b>350</b>."},
    {"q": "In the Python version each record is 24 bytes. At which byte does File.seek go to read location 6?", "a": 144, "unit": "", "tol": 0.01, "hint": "6 × 24.", "sol": "<b>144</b>."}]) + MCQ([
    ("Which statement must come before GETRECORD when finding a record in a random file?", ["READFILE", "SEEK", "EOF", "OPENFILE FOR APPEND"], 1, "SEEK moves the pointer to the location."),
    ("Why compare the key of the record read with the key wanted?", ["To sort the file", "The location may hold a different record because of a collision", "To close the file", "To find the end of the file"], 1, "The record at the hashed location may belong to another key."),
    ("What does reaching an empty location tell a search by key?", ["The file is full", "The record is not in the file", "The record is at the next location", "The hash is wrong"], 1, "It would have been stored there or earlier."),
    ("A customer is searched for by name. Which method?", ["Hash the name", "Read each location from the start until the name matches", "SEEK 0 only", "Append the name"], 1, "The hash is built from the key field only."),
    ("Which is the usual number of records read to find a record by key with no collisions?", ["1", "Half the file", "All of the file", "The location number"], 0, "SEEK then one GETRECORD."),
    ("What is Count for in the search loop?", ["Counting matches", "Stopping the loop after every location has been tried", "Counting bytes", "Counting empty records"], 1, "If Count reaches the number of locations, the key is not in the file.")], "qz1") + CARDS([
    ("Direct access", "Go straight to a record with SEEK."), ("Search by key", "Hash, SEEK, GETRECORD, compare, follow the chain."), ("Stop conditions", "Found, an empty location, or every location tried."), ("Search by name", "Read from location 0 until it matches or the end is reached."),
    ("Rec.AccountNumber = 0", "An empty location."), ("Found flag", "Stops a WHILE loop when the record is found."), ("Not found", "Always output a message if the record was not found."), ("SEEK first", "SEEK before every GETRECORD.")])

real = RWNOTE + (
    rw("An ATM looking up an account", "When a card is inserted the account number is turned into a location and the record is fetched directly. The customer is not left waiting while millions of other records are read.", "direct access: hash the key, SEEK, GETRECORD.") +
    rw("A school office searching by surname", "The student file is organised by student ID, so searching by surname means the system has to read record after record until the name is found, which is slower than searching by ID.", "the hash cannot be used on a field that is not the key.") +
    rw("A stock check", "A warehouse program asks for a location and reads that one record. An empty record means the shelf is empty, and the program shows a message instead of an item.", "SEEK, GETRECORD, then test the record for empty.") +
    rw("A missing record", "A customer quotes an account number that was never opened. The program reaches an empty location and reports that the account does not exist, without reading the whole file.", "an empty location ends the search: the record is not stored."))

review = (
    req("3 marks", "Explain", "Explain how a record is found in a random file when its key is known.", "Hash, direct access, the record read.", mks(["A hash function is applied to the key to calculate the location of the record", "the file pointer is moved directly to that location (SEEK)", "the record is read from there (GETRECORD) without reading other records"])) +
    req("5 marks", "Complete", "Write pseudocode that outputs the record for <code>SearchKey</code> from <code>Accounts.dat</code>, or the message <code>Not found</code>. Assume there are no collisions.", "Open, hash, SEEK, GETRECORD, compare, output, close.", pc('''OPENFILE "Accounts.dat" FOR RANDOM
Location <- Hash(SearchKey)
SEEK "Accounts.dat", Location
GETRECORD "Accounts.dat", Rec
IF Rec.AccountNumber = SearchKey THEN
   OUTPUT Rec
ELSE
   OUTPUT "Not found"
ENDIF
CLOSEFILE "Accounts.dat"'''), "Outputting the record without checking that its key is the one asked for.") +
    req("3 marks", "Explain", "A search by account number reads the record at the hashed location but the account number is different. Explain what the program should do next.", "The record may have been moved by a collision.", mks(["The wanted record may have been stored in a later location because of a collision", "so the program checks the next location (wrapping round at the end)", "until the key is found, an empty location is reached, or every location has been checked"])) +
    req("6 marks", "Write", "Write Python that searches <code>Accounts.dat</code> for the customer called <code>SearchName</code> and prints the account number, or <code>Customer does not exist.</code>", "A name cannot be hashed. Read every location until it is found.", pc('''File = open("Accounts.dat", "rb")
Location = 0
Found = False
while not Found and Location < 7:
    File.seek(Location * RecSize)
    Rec = GetRecord(File)
    if Rec.Name == SearchName:
        Found = True
    else:
        Location = Location + 1
File.close()
if Found:
    print(Rec.AccountNumber)
else:
    print("Customer does not exist.")'''), "Using Hash(SearchName). The hash is calculated from the key field, not from a name.") +
    req("2 marks", "Explain", "Why is searching a random file by key usually faster than searching a serial file?", "Compare the number of records read.", mks(["The location is calculated from the key, so the program goes directly to it", "a serial file has to be read from the start, record by record, until the record is found"])))

where = [("O/N 2023", "31, 33", "8(a)", "5", "Complete the random file lookup of a customer using a hash function"),
         ("O/N 2023", "32", "12(b)", "7", "Complete a search of a random file for a customer by name"),
         ("M/J 2025", "31", "12", "5", "Complete a check of a location in StockList.dat"),
         ("M/J 2023", "32", "6(b)", "5", "Complete the pseudocode that reads every record of a random file"),
         ("M/J 2026", "32", "10(b)", "6", "Complete TempCheck() using SEEK and GETRECORD")]
past = "".join(OLDQ[k] for k in ["O/N 2023 · 9618/31, 33 · Q8(a)", "O/N 2023 · 9618/32 · Q12(b)", "M/J 2025 · 9618/31 · Q12", "M/J 2023 · 9618/32 · Q6(b)", "M/J 2026 · 9618/32 · Q10(b)"])
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Finding a record in a random file is a regular Paper 3 completion question. Paper 4 has not asked for random files as Python so far, so the Python on this page shows the same logic rather than a past question."

tipsl = [("SEEK before GETRECORD.", "Every time, for every location you read."), ("Open FOR RANDOM.", "Not READ or APPEND."), ("Compare the key.", "The record at the hashed location may belong to a different key."), ("Know when to stop.", "Record found, empty location, or every location tried. A flag or Count makes the loop end."), ("Hash is for the key only.", "To find a name, read every location from the start."), ("Say what happens if it is missing.", "Output a message such as \"Not found\".")]
sents = [("Describe direct access", "A record is found without reading the other records, by calculating its location from the key field."), ("Describe finding with a hash", "A hash function calculates the address from the key, SEEK moves to it and GETRECORD reads the record there."), ("Describe a missing record", "If the location is empty, or the key does not match after the other locations are checked, the record is not in the file.")]
words = [("Complete", "Fill in the missing lines of the given pseudocode."), ("Describe", "Give the main features in connected points."), ("Explain", "A reason as well as the fact."), ("Write", "Produce pseudocode or Python that searches the file and reports the result.")]

finishf("ac20f4", "ac-20-2-1-finding-in-random-file", "Finding a Record in a Random File",
        "Direct access with a hash, following a collision chain, knowing when a record is not in the file, and searching by a field that is not the key; pseudocode and Python side by side, with a line-by-line animation.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + stD + lab, where, past, note, words)
