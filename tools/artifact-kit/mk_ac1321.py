"""A Level CS syllabus 13.2.1: file organisation (serial, sequential, random) and file access (sequential, direct). Run: python3 tools/artifact-kit/mk_ac1321.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>File <b>organisation</b> is how the records are arranged in a file: <b>serial</b> files hold records in the order they were added, <b>sequential</b> files hold them in order of a <b>key field</b>, and <b>random</b> files place each record at a location worked out from its key. File <b>access</b> is how a program finds a record: <b>sequential access</b> reads the records one after another from the start, and <b>direct access</b> jumps straight to a record without reading the others. Serial and sequential files are normally accessed sequentially; random files are accessed directly, and a sequential file can be accessed directly if it has an index. You choose a method by thinking about how the file is used: adding, searching, updating and processing in bulk. The pseudocode commands that do this are on the chapter 20 file processing page.</p></div>

  <h2>1 · The three organisations</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Serial</th><th>Sequential</th><th>Random</th></tr>
    <tr><td>Order of records</td><td>The order they were added (chronological), with no ordering on a key</td><td>In order of a <b>key field</b></td><td>No particular order; each record is at an address calculated from its key</td></tr>
    <tr><td>Adding a record</td><td>Append to the end</td><td>Insert in the right place: write a new version of the file</td><td>Store at the calculated location (or the next free one if it is taken)</td></tr>
    <tr><td>Finding a record</td><td>Read from the start until found or the end</td><td>Read from the start until found or until the key has been passed</td><td>Calculate the location and go there</td></tr>
    <tr><td>Updating a record</td><td>Rewrite the file</td><td>Create a new version of the file</td><td>Update directly in place</td></tr>
    <tr><td>Typical uses</td><td>Logs, temporary transaction files, backups, batch processing, bills and payroll</td><td>Master files processed in batches, ordered payroll or bill files</td><td>Databases, booking systems, operating system file management</td></tr>
  </table></div>
  <ul>
    <li>In <b>both serial and sequential</b> files the records are stored one after the other and have to be accessed one after the other.</li>
    <li>In a <b>sequential</b> file the position depends on the key. In a <b>serial</b> file it depends only on <i>when</i> the record was added.</li>
    <li>A <b>random</b> file can have empty locations, and its key is turned into a location by a <b>hashing algorithm</b> (next page).</li>
  </ul>

  <h2>2 · The two methods of access</h2>
  <h3>Sequential access</h3>
  <p>Start at the <b>beginning</b> of the file and check each record in turn (linearly) until the record is found, the end of the file is reached, or (in a sequential file) the key of the current record is greater than the key you are looking for.</p>
  <div class="tw"><table class="t">
    <tr><th>Organisation</th><th>How sequential access finds record K</th></tr>
    <tr><td>Serial</td><td>Check every record from the start until K is found or all have been checked. It cannot stop early, because the file is not in key order</td></tr>
    <tr><td>Sequential</td><td>Check records in key order until K is found, or the key of the current record is <b>larger</b> than K, which means K is not in the file</td></tr>
  </table></div>
  <h3>Direct access</h3>
  <p>A record is found <b>without reading the other records</b>, using its key field to work out where it is.</p>
  <div class="tw"><table class="t">
    <tr><th>Organisation</th><th>How direct access finds record K</th></tr>
    <tr><td>Sequential</td><td>An <b>index</b> of all the key fields is kept. The index is searched for the key, and gives the address in the file of the record, which is then read directly</td></tr>
    <tr><td>Random</td><td>A <b>hashing algorithm</b> is applied to the key to calculate the address; the record is read from there. If it is not there, a collision method (such as a linear search from that point) is used</td></tr>
  </table></div>
  <div class="tip"><b class="h">Which method?</b>A record referenced by a unique <b>address</b> on a disk-type medium: <b>direct</b> access. A bank storing its records in ascending order of account number and processing them all: <b>sequential</b> access.</div>

  <h2>3 · Choosing an organisation</h2>
  <div class="tw"><table class="t">
    <tr><th>If the program mostly...</th><th>Use</th><th>Because</th></tr>
    <tr><td>Adds records as they arrive and processes everything later (logs, backups, a payroll run)</td><td>Serial</td><td>Appending is fast and no ordering is needed</td></tr>
    <tr><td>Processes every record in key order in a batch</td><td>Sequential</td><td>Ordered records suit report and merge jobs, and a search can stop early</td></tr>
    <tr><td>Looks up one record at a time, quickly, in a very large file (bookings, accounts)</td><td>Random</td><td>Direct access avoids reading the other records</td></tr>
  </table></div>

  <h2>4 · In code</h2>
  <p>Text files (serial and sequential) are read with <code>READFILE</code> in a loop until <code>EOF</code>. Random files use <code>SEEK</code> and <code>GETRECORD</code> or <code>PUTRECORD</code>.</p>
  <div class="code">''' + pc('''# sequential access to a sequential (key-ordered) text file
def Find(Key):
    File = open("Accounts.txt", "r")
    for Line in File:
        Record = int(Line.strip())
        if Record == Key:
            File.close()
            return True              # found
        if Record > Key:
            break                    # passed the key: not in the file
    File.close()
    return False''') + '''</div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Describing a serial file as "in order". It is in the order the records were <b>added</b> (chronological); a sequential file is in key order.</li>
    <li>Saying random means "stored anywhere at random". A random file uses the key to calculate where a record goes.</li>
    <li>Forgetting that sequential access starts at the <b>beginning</b> of the file.</li>
    <li>For a sequential file, not saying the search can stop when the key has been exceeded.</li>
    <li>For direct access on a sequential file, leaving out the <b>index</b>; on a random file, leaving out the <b>hashing algorithm</b>.</li>
    <li>Writing a definition of the organisation when the question asks for an example of where it is used (the mark scheme says not to allow that).</li>
  </ul>
'''

watch = '''
  <h2>1 · A serial file: records in the order they arrive</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · A sequential file: the search can stop early</h2>
  <div id="stB"></div>
  <h2>3 · A random file: calculate where to go</h2>
  <div id="stC"></div>
  <h2>4 · Direct access to a sequential file with an index</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · How many records are read?</h2>
  <p>A file holds 12 account records with the keys shown. Choose the organisation and the key to find, and see how many records are read.</p>
  <div class="card"><div id="oB" class="btnrow"></div><div id="oK" class="btnrow"></div><div id="oF"></div>
    <div class="readout"><div><small>Records read</small><strong id="o1"></strong></div><div><small>Result</small><strong id="o2"></strong></div></div><div class="verdict" id="oV"></div></div>

  <h2>Lab 2 · Which organisation and which access?</h2>
  <p>Choose the best answer for each situation.</p>
  <div class="card"><div id="qB" class="btnrow"></div><div id="qO"></div></div>

  <h2>Lab 3 · Compare the organisations</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Serial, sequential or random?</h2><div id="cl1" class="card"></div>
  <h2>2 · Sequential access or direct access?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of a sequential search in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Count the records read</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A data-logging file", "A weather station adds a reading every minute to a file. The readings are stored in the order they were taken and processed at the end of the day, so a serial file fits.", "serial: chronological order, new records appended to the end.") +
rw("A payroll run", "Every employee's pay is calculated once a month by reading the employee file from start to finish, in order of employee number. A sequential file is processed in a batch.", "sequential: ordered by a key; accessed one after another.") +
rw("An airline booking system", "Seat records are fetched and updated in a moment by flight and seat number, among millions of records. The key is turned into a location, and the record is read directly.", "random organisation with direct access using a hashing algorithm.") +
rw("A bank's overnight batch", "Account records stored in ascending order of account number are matched against the day's transactions, which are in the same order, in one pass.", "sequential access suits batch processing of an ordered file.") +
rw("A backup", "A backup copies every file from the start to the end in one go, without needing any ordering or fast lookup.", "serial files are good for simple storage that is read in full.")
)

where = [
  ("O/N 2021", "31, 32", "5", "4 + 1 + 1", "Compare sequential and serial organisation; choose the access method for two situations"),
  ("M/J 2023", "32", "2(a)", "3", "Describe how records are organised and accessed in a sequential file"),
  ("O/N 2023", "31, 33", "4", "4 + 2", "Describe sequential and random organisation; outline sequential access"),
  ("M/J 2024", "31, 33", "4", "2 + 3", "Describe sequential access; explain it on serial and sequential files"),
  ("M/J 2024", "32", "7", "2 + 2 + 3", "Outline direct access; explain it for sequential and random files"),
  ("O/N 2024", "32", "2", "2 + 1", "Describe serial organisation; give a use"),
  ("M/J 2026", "31", "2", "1 + 2 + 3", "Random file organisation: a use, how records are organised, how a record is found"),
  ("M/J 2026", "32", "4", "1 + 2 + 3", "Sequential file organisation: a use, how records are organised, how a record is found"),
  ("M/J 2026", "33", "3", "1 + 2 + 3", "Serial file organisation: a use, how records are organised, how a record is found")]

past = '''  <p class="note">File organisation and access appear in Paper 3 in most series; each question asks you to describe or compare. The pseudocode questions that use these files are on the chapter 20 page on file processing. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Serial and sequential organisation</h3>
''' + peq(SRC("w21", "31, 32", "Q5"), "4 + 1 + 1 marks", "Compare / State",
  "(a) Compare sequential and serial methods of file organisation. (b) State the most suitable method of file access when a record is referenced by a unique address on a disk-type storage medium. (c) State the most suitable method of file access when a bank stores its data records in ascending order of account number.",
  "(a) say what is the same (stored one after another) and what differs (chronological or key order, and how a new record is added).",
  "<p><b>(a)</b> Four marks: " + mks(["In both, records are stored one after the other", "and need to be accessed one after the other", "Serial files are stored in chronological order, sequential files with the records ordered on the key field", "In serial files new records are appended; in sequential files they are inserted in the correct position"]) + "</p><p><b>(b)</b> " + mks(["Direct (access)"], "a") + " <b>(c)</b> " + mks(["Sequential (access)"], "a") + "</p>",
  "Giving only differences. A comparison also needs the similarity: both store records one after another.") + peq(SRC("w24", "32", "Q2"), "2 + 1 marks", "Describe / State",
  "(a) Describe serial file organisation as a method of storing data records in a file. (b) State one example of a use for serial file organisation.",
  "(a) added in order, appended to the end. (b) a use, not a definition.",
  "<p><b>(a)</b> " + mks(["Records are stored one after the other as they are collected / in chronological order", "New records are appended to the end of the file"]) + " <b>(b)</b> " + mks(["Creating an unsorted or temporary transaction file / a data logging file / batch processing / backup"], "a") + "</p>",
  "Giving a use that is really a description, such as 'records are stored one after another'.") + peq(SRC("s26", "33", "Q3"), "1 + 2 + 3 marks", "State / Describe / Outline",
  "(a) State one example of where serial file organisation could be used. (b) Describe how records are organised in serial files. (c) Outline the process that is used to find a record in a serial file.",
  "(c) sequential access: each record in turn, to the end of the file or until found.",
  "<p><b>(a)</b> " + mks(["Batch processing, a transaction file for a batch, storing bills or payroll, a backup, or any case where data is added chronologically"]) + "</p><p><b>(b)</b> " + mks(["Records are stored one after the other", "in chronological order", "new records are appended to the end"], "a") + " (maximum 2)</p><p><b>(c)</b> Up to three: " + mks(["sequential file access is used", "each record is searched one after the other", "until the end of the file is reached", "or until the record is found"]) + "</p>", None) + peq(SRC("s26", "32", "Q4"), "1 + 2 + 3 marks", "State / Describe / Outline",
  "(a) State one example of where sequential file organisation could be used. (b) Describe how records are organised in sequential files. (c) Outline the process of sequential file access to find a record in a sequential file.",
  "(b) in a given order based on a key field, not 'one after another' on its own. (c) one by one using the key, stopping when found or when the key has been exceeded.",
  "<p><b>(a)</b> " + mks(["Batch processing, log files, generating bills or payroll, a backup, or data stored in a specified order"]) + "</p><p><b>(b)</b> " + mks(["Records are stored in a file one after the other / linearly", "in a given order", "usually based on a key field / unique identifier"], "a") + " (maximum 2)</p><p><b>(c)</b> Up to three: " + mks(["each record is searched one after the other, from the physical start of the file", "using the record key", "until the record is found", "or until the value of the key being searched has been exceeded / the end of the file is reached"]) + "</p>",
  "Describing sequential as chronological. Chronological order is serial; sequential is key order.") + peq(SRC("s23", "32", "Q2(a)"), "3 marks", "Describe",
  "Describe how records are organised and accessed in a sequential file.",
  "Ordered by a key, accessed one after the other from the start.",
  "<p>Up to three: " + mks(["records are stored in a particular order", "the order is determined by the value in a key field", "records are accessed one after the other / found by searching from the beginning of the file, record by record", "until the required record is found or the key field value is exceeded"]) + "</p>", None) + '''
  <h3>Random organisation and access methods</h3>
''' + peq(SRC("w23", "31, 33", "Q4"), "4 + 2 marks", "Describe / Outline",
  "(a) Describe sequential and random methods of file organisation. (b) Outline the process of sequential access for serial and sequential files.",
  "(a) two points each: ordered by key and a new version of the file, against calculated location and direct update.",
  "<p><b>(a)</b> Sequential (max 2): " + mks(["Records in the file are ordered", "based on the key field", "a new version of the file has to be created to update it"]) + " Random (max 2): " + mks(["Records are in no particular order within the file", "there is a relationship between the key of the record and its location, so a hashing algorithm is used to find the location", "updates can be carried out directly"], "a") + "</p><p><b>(b)</b> Two marks: " + mks(["start at the beginning of the file", "check the records linearly", "until the desired record is found, or all are processed / the end of file"]) + "</p>", None) + peq(SRC("s24", "31, 33", "Q4"), "2 + 3 marks", "Describe / Explain",
  "(a) Describe the sequential method of file access. (b) Explain how the sequential method of file access is applied to files with serial organisation and to files with sequential organisation.",
  "(b) the difference: serial has no key order so every record is checked; sequential can stop once the key is passed.",
  "<p><b>(a)</b> " + mks(["Records are searched one after the other", "from the physical start of the file until the record is found or the end of the file"]) + "</p><p><b>(b)</b> Up to three: " + mks(["Serial files: records are in chronological order", "so every record is checked until the record is found or all have been checked", "Sequential files: records are in order of a key field", "so every record is checked until the record is found or the key of the current record is greater than the target key"], "a") + "</p>", None) + peq(SRC("s24", "32", "Q7"), "2 + 2 + 3 marks", "Outline / Explain",
  "(a) Outline what is meant by direct access as a method of file access. (b) Explain how direct access is used to locate a specific record in (i) sequential files and (ii) random files.",
  "(i) an index. (ii) a hashing algorithm and what to do if the record is not at the expected location.",
  "<p><b>(a)</b> " + mks(["Direct access allows a record to be found without other records being read", "records are found using the key field of the target record / its location found by hashing"]) + "</p><p><b>(b)(i)</b> " + mks(["An index of all key fields is kept", "the index is searched for the address of the file location where the target record is stored"], "a") + " <b>(ii)</b> " + mks(["A hashing algorithm is used on the key field", "to calculate the address where the target record is expected to be", "a method such as linear probing or searching an overflow area if it is not at the expected location"], "a") + "</p>", None) + peq(SRC("s26", "31", "Q2"), "1 + 2 + 3 marks", "State / Describe / Outline",
  "(a) Random file organisation can be used with a database management system. State one other example of where random file organisation could be used. (b) Describe how records are organised in random files. (c) Outline the process that would be used to find a record in a random file.",
  "(a) not DBMS. (c) direct access, a hash function, collision handling.",
  "<p><b>(a)</b> " + mks(["For example a booking system, an operating system's file management, a video game, an encryption or compression utility"]) + "</p><p><b>(b)</b> " + mks(["Records are stored in no particular order / any available position", "a record key is used to determine the location, generated using a hash function on the key field", "new records are added in an empty location"], "a") + " (maximum 2)</p><p><b>(c)</b> Up to three: " + mks(["direct file access is used", "a hashing function is used on the key field to find the location", "if the record is found at the hashed location it is retrieved", "if not, a collision resolution method is used, such as a linear search from that point"]) + "</p>", None)

review = req("2 marks", "Distinguish", "Distinguish between a serial file and a sequential file.", "Order of the records.",
  "<p>" + mks(["A serial file stores records in the order they were added (chronological), with new records appended to the end.", "A sequential file stores records in order of a key field, with new records inserted in the correct position."]) + "</p>", None) + req("3 marks", "Explain", "Explain why a random file is better than a serial file for a booking system with millions of records.", "How a record is found.",
  "<p>" + mks(["In a serial file records must be read one after the other from the start until the one wanted is found.", "In a random file a hashing algorithm turns the key into the address of the record.", "The record is read directly without reading the others, so access is much faster."]) + "</p>", None) + req("2 marks", "State", "A sequential file holds the keys 5, 12, 20, 33, 47, 60. A program searches it for 25. State the keys read and why the search stops.", "Stop when the current key exceeds the target.",
  "<p>" + mks(["5, 12, 20 and 33 are read", "the search stops at 33 because it is greater than 25, so 25 is not in the file"]) + "</p>", "Reading to the end of the file. A sequential file lets the search stop once the key is passed.") + req("2 marks", "Outline", "Outline how a new record is added to a sequential file.", "Why can it not simply be appended?",
  "<p>" + mks(["The file cannot just be appended to, because the records must stay in key order.", "A new version of the file is created, with the new record written in the correct position."]) + "</p>", None) + req("3 marks", "Choose", "For each situation, name the file organisation and access method: (a) a log of every sensor reading, processed at the end of the day; (b) a flight booking record fetched by booking reference.", "Serial or random; sequential or direct.",
  "<p>" + mks(["(a) serial organisation", "with sequential access (read from the start to the end)", "(b) random organisation with direct access"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on file organisation and access methods (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Serial is chronological; sequential is key order.", "Keep these apart. Both are read one record after another."),
  ("Start at the beginning.", "Sequential access always begins at the start of the file."),
  ("Mention the stopping condition.", "Found, end of file, or (sequential) key exceeded."),
  ("Direct access needs a tool.", "An index for a sequential file; a hashing algorithm for a random file."),
  ("An example is not a definition.", "When the question asks where it is used, name a use such as batch processing or a booking system."),
  ("Match the method to the use.", "Whole-file batch: sequential access. One record quickly: direct access."),
], [
  ("what a serial file is", "Records are stored one after the other in the order they were added, with new records appended to the end."),
  ("what a sequential file is", "Records are stored in order of a key field, and a new version of the file is needed to insert one."),
  ("what a random file is", "Each record is stored at a location calculated from its key using a hashing algorithm."),
  ("what direct access is", "A record is found without reading the others, using its key to work out where it is."),
], [("State", "A short fact or example."), ("Describe", "Say how it is organised or works, in several points."), ("Outline", "Give the main steps without detail."), ("Compare", "Give similarities and differences.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const recs = [4090, 1203, 7731, 2650, 5112];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "File (records in the order they arrive)", "sm");
    recs.forEach((r, i) => { o += SV.rect(30 + i * 138, 34, 124, 50, i < Math.min(k, 5) ? "f3" : "cell", { rx: 8, ...op(i < k ? 1 : 0.35) }) + SV.text(92 + i * 138, 66, String(r), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px", ...op(i < k ? 1 : 0.35) }); });
    if (k >= 1 && k <= 5) o += SV.text(30, 110, "newest record is appended to the end: " + recs[k - 1], "lbl bd", { style: "font-size:14px" });
    if (k >= 6) { o += SV.text(30, 110, "Search for 2650: read 4090, 1203, 7731, then 2650", "lbl bd", { style: "font-size:14px" }); [0, 1, 2, 3].forEach((i) => (o += SV.rect(30 + i * 138, 130, 124, 8, i === 3 ? "cell-ok" : "cell-warn", { rx: 3 }))); o += SV.text(30, 166, "4 records read: no order to use, so it could not stop early", "sm"); }
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 190, label: "A serial file", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [
    { cap: "A <b>serial</b> file is empty. Records are written as they arrive.", s: { i: 0 } },
    { cap: "The first record, 4090, is appended.", s: { i: 1 } },
    { cap: "1203 is appended after it. Each new record goes at the <b>end</b>, whatever its key.", s: { i: 2 } },
    { cap: "7731 is appended.", s: { i: 3 } },
    { cap: "2650 is appended.", s: { i: 4 } },
    { cap: "5112 is appended. The records are in <b>chronological</b> order, not key order.", s: { i: 5 } },
    { cap: "To find 2650 the program reads from the start, one record after another. With no key order it cannot predict where 2650 is.", s: { i: 6 } }] });
})();

(function () {
  const recs = [1203, 2650, 4090, 5112, 7731];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "File (records in key order)", "sm");
    recs.forEach((r, i) => { o += SV.rect(30 + i * 138, 34, 124, 50, k >= 1 && i === Math.min(k, 3) - 1 ? "cell-warn" : "f3", { rx: 8 }) + SV.text(92 + i * 138, 66, String(r), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" }); });
    if (k >= 1) o += SV.text(30, 112, "Search for 3000", "lbl bd", { style: "font-size:15px" });
    if (k >= 1) o += SV.text(30, 140, "1203 < 3000: carry on" + (k >= 2 ? "     2650 < 3000: carry on" : ""), "lbl", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.text(30, 168, "4090 > 3000: the key has been passed, so 3000 is not in the file", "lbl bd t2", { style: "font-size:14px" }) + SV.text(30, 196, "stop: 3 records read (the end of the file was never reached)", "sm");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "A sequential file search that stops early", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "In a <b>sequential</b> file the records are in order of the key field.", s: { i: 0 } },
    { cap: "Search for 3000: start at the beginning. 1203 is smaller than 3000, so carry on.", s: { i: 1 } },
    { cap: "2650 is smaller too, so carry on.", s: { i: 2 } },
    { cap: "4090 is <b>greater</b> than 3000. Because the file is in key order, 3000 cannot be further on, so the search stops.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "Key: 4719", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 1) o += SV.text(30, 62, "Hash(4719) = 4719 MOD 11 = 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 92, "go straight to location 6", "lbl bd t3", { style: "font-size:15px" });
    for (let i = 0; i < 11; i++) o += memCell(430, 14 + i * 21, i, i === 6 && k >= 3 ? "4719 Hall" : i === 2 ? "1202 Ito" : i === 9 ? "7745 Ray" : "", i === 6 && k >= 2 ? "cell-warn" : "f3", 1, 280, 19);
    if (k >= 3) o += SV.text(30, 124, "record read: 1 record accessed", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Direct access to a random file", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A <b>random</b> file has locations 0 to 10. Records are not in key order; each is at an address worked out from its key.", s: { i: 0 } },
    { cap: "To find key 4719, apply the <b>hashing algorithm</b> to the key: 4719 MOD 11 = 6.", s: { i: 1 } },
    { cap: "Go <b>directly</b> to location 6.", s: { i: 2 } },
    { cap: "The record is there. Only one record was read, however large the file.", s: { i: 3 } }] });
})();

(function () {
  const idx = [[1203, 0], [2650, 1], [4090, 2], [5112, 3], [7731, 4]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Index (keys and addresses)", "sm") + SV.text(360, 24, "Sequential file", "sm");
    idx.forEach((r, i) => { o += SV.rect(30, 34 + i * 38, 260, 32, k === 2 && r[0] === 5112 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, 56 + i * 38, r[0] + "  →  address " + r[1], "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    [1203, 2650, 4090, 5112, 7731].forEach((r, i) => { o += SV.rect(360, 34 + i * 38, 200, 32, k === 3 && r === 5112 ? "cell-ok" : "f3", { rx: 6 }) + SV.text(374, 56 + i * 38, "address " + i + ":  " + r, "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    if (k >= 1) o += SV.text(590, 70, "Find 5112", "lbl bd", { style: "font-size:16px" });
    if (k >= 2) o += SV.text(590, 100, "index gives address 3", "lbl", { style: "font-size:14px" });
    if (k >= 3) o += SV.text(590, 130, "read address 3: found", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "A sequential file with an index", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A sequential file can also be accessed <b>directly</b> if an <b>index</b> of all the key fields is kept with the address of each record.", s: { i: 0 } },
    { cap: "To find 5112, search the index (it is small and in key order).", s: { i: 1 } },
    { cap: "The index gives the address where 5112 is stored: address 3.", s: { i: 2 } },
    { cap: "Read that address directly. The records before it in the file were never read.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const keys = [4090, 1203, 7731, 2650, 5112, 8844, 3377, 6021, 9150, 1998, 7010, 2301]; let org = 0, target = 2650;
  const orgs = ["Serial", "Sequential", "Random (direct)"];
  const sorted = keys.slice().sort((a, b) => a - b);
  const ex = [2650, 9150, 3000, 1203];
  const run = () => {
    if (org === 0) { const i = keys.indexOf(target); return i >= 0 ? { n: i + 1, ok: true, why: "Records are read from the start until the key is found." } : { n: keys.length, ok: false, why: "Not in the file: every record had to be read, because a serial file has no order to stop on." }; }
    if (org === 1) { let n = 0; for (const k of sorted) { n++; if (k === target) return { n, ok: true, why: "Records are read in key order from the start until the key is found." }; if (k > target) return { n, ok: false, why: "The key was passed (" + k + " > " + target + "), so the search stopped without reading the rest." }; } return { n, ok: false, why: "End of file reached." }; }
    const i = keys.indexOf(target); return { n: 1, ok: i >= 0, why: "Hash the key, SEEK straight to the location, read one record" + (i >= 0 ? "." : ": the location is empty or holds another key, so the record is not in the file.") };
  };
  const paint = () => {
    $$("#oB button").forEach((b, i) => b.classList.toggle("pri", i === org)); $$("#oK button").forEach((b, i) => b.classList.toggle("pri", ex[i] === target));
    const L = org === 1 ? sorted : keys, r = run();
    $("#oF").innerHTML = '<div class="tw"><table class="t mono"><tr>' + L.map((k, i) => `<td style="${i < r.n && org !== 2 ? "background:var(--warn-soft);font-weight:700" : ""}">${k}</td>`).join("") + "</tr></table></div>";
    $("#o1").textContent = r.n; $("#o2").textContent = r.ok ? "found" : "not found"; $("#oV").textContent = r.why;
  };
  $("#oB").innerHTML = orgs.map((o, i) => `<button class="b" data-i="${i}">${o}</button>`).join("");
  $("#oK").innerHTML = ex.map((k) => `<button class="b">Find ${k}</button>`).join("");
  $$("#oB button").forEach((b) => (b.onclick = () => { org = +b.dataset.i; paint(); })); $$("#oK button").forEach((b, i) => (b.onclick = () => { target = ex[i]; paint(); }));
  paint();
})();

/* Lab 2 */
(function () {
  const q = [
    ["A log of every sensor reading, processed once at the end of the day", "Serial organisation, sequential access", ["Serial organisation, sequential access", "Random organisation, direct access", "Sequential organisation, direct access"], "Readings arrive in time order and everything is read in one pass."],
    ["An airline booking system fetching one seat record among millions", "Random organisation, direct access", ["Serial organisation, sequential access", "Random organisation, direct access", "Sequential organisation, sequential access"], "One record quickly: calculate its location and go there."],
    ["A bank processing every account in account-number order each night", "Sequential organisation, sequential access", ["Random organisation, direct access", "Sequential organisation, sequential access", "Serial organisation, direct access"], "Ordered records processed in a batch."],
    ["A large ordered customer file where individual customers are looked up often", "Sequential organisation, direct access with an index", ["Serial organisation, sequential access", "Sequential organisation, direct access with an index", "Random organisation, sequential access"], "An index lets an ordered file be accessed directly."]
  ]; let cur = 0, pick = null;
  const paint = () => {
    $$("#qB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#qO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow">` + Q[2].map((o, i) => `<button class="b${pick === o ? " pri" : ""}" data-o="${i}">${o}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose an answer." : pick === Q[1] ? "Correct. " + Q[3] : "Not the best choice. " + Q[3]) + "</div>";
    $$("#qO button").forEach((b) => (b.onclick = () => { pick = Q[2][+b.dataset.o]; paint(); }));
  };
  $("#qB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#qB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Serial", "Records in the order added (chronological)", "Append to the end", "Read from the start to the end; cannot stop early", "Logs, backups, batch files, temporary transaction files"],
  ["Sequential", "Records in order of a key field", "Create a new version of the file with the record inserted", "Read in key order; stop when found or the key is passed", "Ordered master files, payroll, bills, batch processing"],
  ["Random", "At an address calculated from the key using a hashing algorithm", "Store at the calculated location (handle collisions)", "Direct access: calculate the location and go there", "Databases, booking systems, operating system file management"]
], ["Organisation", "How records are stored", "Adding a record", "Finding a record", "Typical uses"]);
''' + CLASSIFY("cl1", "Which file organisation does each statement describe?", ["Serial", "Sequential", "Random"],
  [("Records are in the order they were added", 0), ("Records are ordered on a key field", 1), ("The location is calculated from the key using a hash function", 2), ("New records are appended to the end", 0), ("A new version of the file is created to insert a record", 1), ("Records can be updated directly in place", 2), ("Suits a data log", 0), ("Suits a booking system", 2)],
  "Serial: chronological. Sequential: key order. Random: calculated location.") + CLASSIFY("cl2", "Which access method is it?", ["Sequential access", "Direct access"],
  [("Start at the beginning and check each record in turn", 0), ("Use an index to find the address of a record", 1), ("Apply a hashing algorithm to the key to find the address", 1), ("Stop when the key of the current record is greater than the target", 0), ("A record is found without reading the others", 1), ("Check every record until the end of the file", 0)],
  "Sequential: one after another from the start. Direct: straight to the record.") + ORDER(
  "Put the steps of a sequential search of a key-ordered file in order.",
  ["Open the file and start at the first record", "Read the next record", "If its key equals the target, the record is found", "If its key is greater than the target, stop: it is not in the file", "Otherwise go back and read the next record"],
  "Start, read, compare, stop or repeat.") + MATCH([
  ["Serial file", "Records stored in the order they were added"], ["Sequential file", "Records stored in order of a key field"], ["Random file", "Records stored at a location calculated from the key"], ["Direct access", "Finding a record without reading the others"], ["Index", "A list of keys with the address of each record"]]) + CALC([
  {"q": "A serial file holds 1000 records. The record wanted is the 640th. How many records are read to find it?", "a": 640, "unit": "", "tol": 0.01, "hint": "Read from the start.", "sol": "<b>640</b>."},
  {"q": "A serial file holds 1000 records and the key is not in the file. How many records are read to find that out?", "a": 1000, "unit": "", "tol": 0.01, "hint": "No order to stop on.", "sol": "<b>1000</b>."},
  {"q": "A sequential file has the keys 10, 20, 30, 40, 50, 60. How many records are read when searching for 35?", "a": 4, "unit": "", "tol": 0.01, "hint": "10, 20, 30, then 40 is greater than 35.", "sol": "<b>4</b>."},
  {"q": "A sequential file has the keys 10, 20, 30, 40, 50, 60. How many records are read when searching for 60?", "a": 6, "unit": "", "tol": 0.01, "hint": "The last one.", "sol": "<b>6</b>."},
  {"q": "A random file uses Hash(Key) = Key MOD 7. At which location is key 52?", "a": 3, "unit": "", "tol": 0.01, "hint": "7 × 7 = 49, remainder 3.", "sol": "<b>3</b>."},
  {"q": "How many records are read after the hash to retrieve a record in a random file with no collision?", "a": 1, "unit": "", "tol": 0.01, "hint": "Direct access.", "sol": "<b>1</b>."}]) + MCQ([
  ("Which organisation stores records in the order they were added?", ["Sequential", "Serial", "Random", "Indexed"], 1, "Serial files are chronological."),
  ("Which organisation orders records on a key field?", ["Serial", "Sequential", "Random", "Direct"], 1, "Sequential files use a key."),
  ("What is needed for direct access to a sequential file?", ["A hash function", "An index", "A second file", "Nothing"], 1, "An index of keys and addresses."),
  ("What is needed for direct access to a random file?", ["An index", "A hashing algorithm", "Sorting", "Compression"], 1, "The hash gives the address."),
  ("A sequential search of a key-ordered file stops early when...", ["the file is empty", "the current key is greater than the target", "the first record is read", "it can never stop early"], 1, "The key has been passed."),
  ("Which method suits a bank processing all accounts in account-number order?", ["Direct access", "Sequential access", "Hashing", "Random access"], 1, "Batch processing of an ordered file.")], "qz1") + CARDS([
  ("Serial", "Records in the order added. Append to the end."), ("Sequential", "Records in key order. New version of the file to insert."), ("Random", "Location calculated from the key with a hash."), ("Sequential access", "From the start, one after another."),
  ("Direct access", "Straight to the record without reading the others."), ("Index", "Keys with addresses: direct access to a sequential file."), ("Stop early", "Sequential file: key exceeded."), ("Examples", "Serial log, sequential payroll, random bookings.")])

build("ac1321", "ac-13-2-1-file-organisation-access", "File Organisation and Access", EYA("13.2.1"),
  "Serial, sequential and random file organisation, sequential and direct access, how a record is found in each, choosing a method for a problem; animations, a search simulator and the real 9618 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.2 File organisation and access"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
