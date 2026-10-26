"""A Level CS syllabus 13.2.2: hashing algorithms (random file storage, collisions). Run: python3 tools/artifact-kit/mk_ac1322.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>hashing algorithm</b> is a mathematical formula that is applied to a record's <b>key field</b> and calculates the <b>address</b> where the record is stored or should be found. The most common one is the <b>modulus</b>: divide the key by the number of locations and use the remainder. Because two different keys can give the same address, a <b>collision</b> can occur, and the system needs a <b>collision resolution</b> method, such as storing the record in the <b>next free location</b> (linear probing) or in an <b>overflow area</b>. To find a record the same hash is calculated, the location is read, and if the key there does not match the search continues in the same way. This is how random files give direct access to a record without reading the others.</p></div>

  <h2>1 · What a hashing algorithm does</h2>
  <div class="tw"><table class="t">
    <tr><th>Step</th><th>Storing a record</th><th>Finding a record</th></tr>
    <tr><td>1</td><td>Take the record's <b>key</b> (e.g. account number 3003)</td><td>Take the <b>key</b> being searched for</td></tr>
    <tr><td>2</td><td>Apply the hashing algorithm: 3003 MOD 5 = 3</td><td>Apply the <b>same</b> algorithm: 3003 MOD 5 = 3</td></tr>
    <tr><td>3</td><td>Write the record at location 3</td><td>Read location 3 and check the key matches</td></tr>
  </table></div>
  <p>The same key always gives the same address, so a record can be stored and found without searching. <b>MOD</b> gives the remainder after integer division: 3003 MOD 5 = 3, 1029 MOD 5 = 4, 7630 MOD 5 = 0.</p>
  <div class="code">''' + pc('''def Hash(Key, Size):
    return Key % Size            # the remainder: always from 0 to Size - 1

print(Hash(3003, 5))             # 3
print(Hash(1029, 5))             # 4
print(Hash(7630, 5))             # 0''') + '''</div>
  <p>A good hashing algorithm is <b>fast</b>, always gives the <b>same</b> address for the same key, and <b>spreads</b> keys evenly over all locations so there are few collisions. Using a table size that is a prime number helps.</p>

  <h2>2 · Collisions</h2>
  <p>A <b>collision</b> occurs when two different keys give the <b>same hash value</b>, so the location the algorithm identifies is <b>already in use</b>. Two records cannot occupy the same address.</p>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>When storing</th><th>When finding</th></tr>
    <tr><td><b>Linear probing</b> (closed hashing)</td><td>Start at the hashed location and go through the following locations, one after another, until the first free one, and store the record there</td><td>Start at the hashed location and search linearly onwards until the key matches. If an empty location is reached, the record is not in the file</td></tr>
    <tr><td><b>Overflow area</b> (open hashing)</td><td>Store the record in the next free space in a separate overflow area</td><td>If the key at the hashed location does not match, search the overflow area linearly until the matching key is found</td></tr>
    <tr><td><b>Chaining</b></td><td>Each location holds a reference to a collection (chain) of items; add the record to the chain</td><td>Search the chain at the hashed location</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam wording</b>When asked what happens on a collision, say: the calculated location is already used for another record; the file is searched linearly from that point (or the overflow area is searched) for the next free space and the record is stored there; when finding, the search carries on linearly until the matching key is found, and if it is not found the record is not in the file.</div>

  <h2>3 · Hashing and the random file</h2>
  <p>A random file is opened with <code>FOR RANDOM</code>. The hash gives the location to <code>SEEK</code>, and then <code>GETRECORD</code> or <code>PUTRECORD</code> reads or writes the record. The pseudocode questions that do this are on the chapter 20 file processing page.</p>
  <div class="code">''' + pc('''Location ← Hash(Customer.AccountNumber)
SEEK AccountFile, Location
GETRECORD AccountFile, Customer''') + '''</div>

  <h2>4 · Advantages and limits</h2>
  <ul>
    <li><b>Fast direct access</b>: one calculation and (usually) one read, however large the file.</li>
    <li>Records can be <b>updated directly</b> without rewriting the file.</li>
    <li>Some locations are <b>empty</b>, so space is wasted, and collisions make access slower as the file fills up.</li>
    <li>The records are <b>not in key order</b>, so a hash file is poor for reports that need an order.</li>
  </ul>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Saying a hash function "encrypts" the key. It calculates an address; it is not for secrecy.</li>
    <li>Calculating MOD wrongly: the remainder after integer division, so 1029 MOD 5 is 4, not 205.</li>
    <li>Describing a collision as an error in the file. It is two keys producing the same address.</li>
    <li>For a collision, only saying "use another location". Say how: next free space linearly, or an overflow area.</li>
    <li>Forgetting that finding a record also has to follow the same collision method.</li>
  </ul>
'''

watch = '''
  <h2>1 · Storing records with a hash</h2>
  <p>Press Play, or click the steps. The table has 5 locations and Hash(Key) = Key MOD 5.</p>
  <div id="stA"></div>
  <h2>2 · A collision and linear probing</h2>
  <div id="stB"></div>
  <h2>3 · Finding a record after a collision</h2>
  <div id="stC"></div>
  <h2>4 · An overflow area</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Hash table sandbox</h2>
  <p>Choose the table size and how a collision is resolved, then store keys one at a time and watch the table fill. Use Find to see how many locations are checked.</p>
  <div class="card"><div id="hZ" class="btnrow"></div><div id="hM" class="btnrow"></div>
    <p><input id="hK" type="number" value="1030" style="width:9em;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Key"> <button class="b pri" id="hS">Store key</button> <button class="b" id="hF">Find key</button> <button class="b" id="hR">Clear table</button></p>
    <div id="hT"></div><div class="verdict" id="hV"></div></div>

  <h2>Lab 2 · Calculate a hash value</h2>
  <div class="card"><div id="cK"></div><div id="cZ"></div><div class="readout"><div><small>Key MOD size</small><strong id="c1"></strong></div><div><small>Working</small><strong id="c2" style="font-size:1rem"></strong></div></div></div>

  <h2>Lab 3 · Collision methods compared</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Hashing facts</h2><div id="cl1" class="card"></div>
  <h2>2 · Storing or finding?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for storing a record with a collision in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculate the hash values</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A library catalogue", "Each book's ID is turned into a shelf location by a hash. Looking up a book means calculating the hash and going to that shelf, instead of searching every shelf.", "hashing gives direct access using the key field.") +
rw("A phone's contacts or a database index", "Many databases use hash tables so a record can be found from its key in about one step, however many records there are.", "random files and hash tables share the same idea.") +
rw("A hotel booking system", "Booking references are hashed to locations in a large file. If two bookings map to the same place, the second is stored in the next free location, and a search follows the same path.", "collisions are resolved by linear probing or an overflow area.") +
rw("Checking a downloaded file", "A different kind of hash, a checksum, is calculated over a whole file. If the result differs from the published one, the file has changed.", "same word, different purpose: this hash checks integrity, not an address.") +
rw("Passwords", "Websites store a hash of your password, not the password. When you log in the hash of what you type is compared with the stored one.", "another use of hashing: here it is a one-way function, unlike the address calculation in this topic.")
)

where = [
  ("M/J 2023", "31, 33", "3", "2 + 4", "Complete a table of hash values (modulus 3); describe what happens on a collision"),
  ("M/J 2023", "32", "2(b)", "2", "Complete a table of hash values (modulus 5)"),
  ("O/N 2023", "32", "3", "2 + 3", "Outline a collision; explain how it is dealt with when writing records"),
  ("O/N 2024", "31, 33", "5", "3 + 2", "Explain a hashing algorithm; outline two ways of overcoming a collision")]

past = '''  <p class="note">Hashing is tested in Paper 3 as a short theory question, in May/June and Oct/Nov 2023 and Oct/Nov 2024. The pseudocode questions that use a hash to read and write a random file (Oct/Nov 2023 Paper 31 and 33 Question 8 and others) are on the chapter 20 page on file processing, and the question that asks how direct access finds a record in a random file (May/June 2024 Paper 32 Question 7) is on the previous page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Calculating and defining</h3>
''' + peq(SRC("s23", "31, 33", "Q3"), "2 + 4 marks", "Complete / Describe",
  "A hashing algorithm is used to calculate storage locations for records in a random access file. It calculates hash values by using the function modulus 3. The function modulus gives the remainder after integer division. For example, 1030 modulus 3 = 1, so the record key 1030 gives a hash value of 1. (a) Complete the table to show the hash values for the keys 1050 and 1025. (b) Describe what happens, in relation to the storage or retrieval of a record in the file, when the calculated hash value is a duplicate of a previously calculated hash value for a different record key." + qcode('''Record key     Hash value
1030           1
1050           ...
1025           ...'''),
  "(a) divide and keep the remainder. (b) a collision, then how a record is stored and how it is found.",
  "<p><b>(a)</b> " + mks(["1050 MOD 3 = 0 (1050 = 3 × 350)", "1025 MOD 3 = 2 (1025 = 3 × 341 + 2)"]) + "</p>" + qcode('''Record key     Hash value
1030           1
1050           0
1025           2''') + "<p><b>(b)</b> Up to four marks: " + mks(["A collision occurs when the record key does not match the stored record key", "which means the determined storage location has already been used for another record", "When storing: search the file linearly to find the next available storage space (closed hash), or the overflow area linearly (open hash)", "When finding: search the overflow area linearly, or search linearly from where you are, until the matching record key is found; if it is not found the record is not in the file"], "a") + "</p>",
  "Giving a wrong remainder: 1050 is exactly divisible by 3, so the hash value is 0.") + peq(SRC("s23", "32", "Q2(b)"), "2 marks", "Complete",
  "A hashing algorithm is used to calculate storage locations for records in a random access file, using the function modulus 5. For example, 3003 modulus 5 = 3, so the record key 3003 gives a hash value of 3. Complete the table to show the hash values for the keys 1029 and 7630." + qcode('''Record key     Hash value
3003           3
1029           ...
7630           ...'''),
  "Remainder after dividing by 5: look at the last digit.",
  "<p>One mark for each correct hash value: " + mks(["1029 MOD 5 = 4", "7630 MOD 5 = 0"]) + "</p>" + qcode('''Record key     Hash value
3003           3
1029           4
7630           0'''),
  "Writing the quotient (205 or 1526) instead of the remainder.") + peq(SRC("w24", "31, 33", "Q5"), "3 + 2 marks", "Explain / Outline",
  "(a) Explain what is meant by a hashing algorithm in the context of file access. (b) The use of a hashing algorithm can result in the same storage location being identified for more than one record. Outline two methods of overcoming this issue.",
  "(a) a formula, applied to the key, giving the address. (b) next free space after the hashed location; an overflow area.",
  "<p><b>(a)</b> Up to three: " + mks(["A hashing algorithm is used in direct access methods on random and sequential files", "It is a mathematical formula", "used to perform a calculation applied to the key field of the record being searched or stored", "The result of the calculation gives the address where the record should be found or stored"]) + "</p><p><b>(b)</b> " + mks(["The record is stored in the next free memory space after the one identified by the hashing algorithm (linear progression)", "An overflow area is set up and the record is stored in the next free memory space in the overflow area"], "a") + "</p>",
  "Describing hashing as sorting the records. It calculates an address; it does not sort.") + peq(SRC("w23", "32", "Q3"), "2 + 3 marks", "Outline / Explain",
  "The location of a record in a random file is determined using a hashing algorithm. A collision may occur during the process of adding a record. (a) Outline what is meant by the term collision in this context. (b) Explain how a collision can be dealt with when writing records to a random file.",
  "(a) two keys, the same hash value, the location already in use. (b) any one method, with its steps.",
  "<p><b>(a)</b> " + mks(["A collision is when the key fields of two records give the same hash value", "so the location identified may already be in use: two records cannot occupy the same address"]) + "</p><p><b>(b)</b> Up to three, from one method: " + mks(["A process of collision resolution is used: start at the original hashed storage space", "go through the following spaces in a linear fashion", "and store the data item in the first available slot (or: search the overflow area in the same way; or: each space holds a reference to a chain of items, and the item is stored in the first available space in the chain)"], "a") + "</p>", None)

review = req("2 marks", "Calculate", "A random file uses Hash(Key) = Key MOD 11. Give the hash values for the keys 4719 and 5000.", "Divide by 11, keep the remainder.",
  "<p>" + mks(["4719 MOD 11 = 0 (11 × 429 = 4719 exactly)", "5000 MOD 11 = 6"]) + "</p>", "Using the quotient. Hash values are always remainders between 0 and 10.") + req("3 marks", "Describe", "Keys 1030 and 1050 are stored in a file using Hash(Key) = Key MOD 5. Both give 0. Describe what happens when 1050 is stored after 1030, and how 1050 is later found.", "Collision, next free space, linear search.",
  "<p>" + mks(["Location 0 is already used by 1030, so there is a collision.", "1050 is stored in the next free location after location 0 (linear probing).", "To find 1050 the hash is calculated, location 0 is read (key 1030, no match), and the search continues linearly until the key 1050 is found."]) + "</p>", None) + req("2 marks", "State", "State two properties of a good hashing algorithm.", "Think speed and spread.",
  "<p>" + mks(["It is quick to calculate and always gives the same value for the same key.", "It spreads the keys evenly over the locations so there are few collisions."]) + "</p>", None) + req("2 marks", "Explain", "Explain why records in a hash (random) file cannot easily be produced in key order.", "Where do the records sit?",
  "<p>" + mks(["Records are stored at addresses calculated from their keys, not in key order.", "Many locations are empty, so producing an ordered list needs a separate sort."]) + "</p>", None) + req("3 marks", "Compare", "Compare using the next free location with using an overflow area to resolve a collision.", "Where is the record stored; how is it found?",
  "<p>" + mks(["Next free location: the record goes in the following space in the main file, found by searching linearly on from the hashed location.", "Overflow area: the record goes in a separate area, found by searching that area when the hashed location holds a different key.", "Both need the same method used when storing and finding."]) + "</p>", None)

exam = exam20("Part 1 is the real 9618 questions on hashing algorithms and collisions (Paper 3), 2023 and 2024. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("MOD is the remainder.", "Divide, ignore the whole number, keep what is left over."),
  ("Same hash, same place.", "Storing and finding use the same algorithm and the same collision method."),
  ("Define a collision.", "Two different keys give the same hash value, so the location is already in use."),
  ("Give a method with its steps.", "Next free space, searching on linearly; or an overflow area searched linearly."),
  ("The hash gives an address, not an order.", "Records are not stored in key order."),
  ("Say 'key field'.", "The hashing algorithm is applied to the key field of the record."),
], [
  ("what a hashing algorithm is", "A formula applied to the key field of a record that calculates the address where it should be stored or found."),
  ("what a collision is", "Two different keys give the same hash value, so the location is already in use."),
  ("how to deal with a collision", "Store the record in the next free space found by searching linearly, or in an overflow area."),
  ("how a record is found after a collision", "Search linearly from the hashed location, or in the overflow area, until the matching key is found."),
], [("Complete", "Fill in the table with the remainders."), ("Outline", "Give the main points briefly."), ("Explain", "Give the points with reasons."), ("Describe", "Say what happens, step by step.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const keys = [3003, 1029, 7630], loc = [3, 4, 0];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Hash(Key) = Key MOD 5", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    for (let i = 0; i < 5; i++) { const idx = loc.indexOf(i); const filled = idx >= 0 && idx < k; o += memCell(430, 20 + i * 44, i, filled ? keys[idx] : "", filled && idx === k - 1 ? "cell-warn" : "f3", 1, 280, 38); }
    if (k >= 1) o += SV.text(30, 70, keys[k - 1] + " MOD 5 = " + loc[k - 1], "lbl", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(30, 100, "store at location " + loc[k - 1], "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 240, label: "Storing records using MOD 5", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "The table has locations 0 to 4. The algorithm divides the key by 5 and uses the <b>remainder</b>.", s: { i: 0 } },
    { cap: "Key 3003: 3003 MOD 5 = 3, so the record is stored at location 3.", s: { i: 1 } },
    { cap: "Key 1029: 1029 MOD 5 = 4, so location 4.", s: { i: 2 } },
    { cap: "Key 7630: 7630 MOD 5 = 0, so location 0. Each key goes straight to its own address.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Hash(Key) = Key MOD 5", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const cells = ["7630", "", "", "3003", "1029"]; if (k >= 1) cells[1] = k >= 3 ? "1055" : cells[1];
    for (let i = 0; i < 5; i++) o += memCell(430, 20 + i * 44, i, cells[i], (k === 2 && i === 0) || (k === 3 && i === 1) ? "cell-warn" : i === 1 && k >= 3 ? "cell-ok" : "f3", 1, 280, 38);
    if (k >= 1) o += SV.text(30, 70, "New key 1055: 1055 MOD 5 = 0", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 100, "location 0 holds 7630: COLLISION", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 3) o += SV.text(30, 130, "search on linearly: location 1 is free", "lbl", { style: "font-size:15px" }) + SV.text(30, 160, "store 1055 at location 1", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 240, label: "A collision resolved by linear probing", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Locations 0, 3 and 4 are already in use. A new record with key <b>1055</b> arrives.", s: { i: 0 } },
    { cap: "1055 MOD 5 = 0, the same hash value as the key 7630 that is already stored.", s: { i: 1 } },
    { cap: "Location 0 is occupied by a different key: a <b>collision</b>. Two records cannot share an address.", s: { i: 2 } },
    { cap: "<b>Linear probing</b>: look at the next location, 1. It is free, so 1055 is stored there.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Find key 1055", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const cells = ["7630", "1055", "", "3003", "1029"];
    for (let i = 0; i < 5; i++) o += memCell(430, 20 + i * 44, i, cells[i], (k >= 2 && k <= 3 && i === 0) || (k >= 3 && i === 1) ? (i === 1 && k >= 4 ? "cell-ok" : "cell-warn") : "f3", 1, 280, 38);
    if (k >= 1) o += SV.text(30, 66, "1055 MOD 5 = 0: go to location 0", "lbl", { style: "font-size:15px" });
    if (k >= 2) o += SV.text(30, 96, "key there is 7630, not 1055: no match", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 3) o += SV.text(30, 126, "carry on linearly: location 1", "lbl", { style: "font-size:15px" });
    if (k >= 4) o += SV.text(30, 156, "key 1055 matches: found after 2 reads", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Finding a record that collided", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "The same record is looked up later.", s: { i: 0 } },
    { cap: "Calculate the hash again: <b>1055 MOD 5 = 0</b>.", s: { i: 1 } },
    { cap: "The record at location 0 has the key 7630, which does not match. The record may have been moved by a collision.", s: { i: 2 } },
    { cap: "Follow the <b>same method</b> used when it was stored: search on linearly to location 1.", s: { i: 3 } },
    { cap: "The key matches, so the record is found. If an empty location had been reached first, the record would not be in the file.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Main file", "sm") + SV.text(450, 22, "Overflow area", "sm");
    const main = ["7630", "", "", "3003", "1029"];
    for (let i = 0; i < 5; i++) o += memCell(30, 30 + i * 40, i, main[i], k === 1 && i === 0 ? "cell-warn" : "f3", 1, 280, 34);
    const over = k >= 2 ? ["1055"] : []; if (k >= 3) over.push("2310");
    for (let i = 0; i < 3; i++) o += memCell(450, 30 + i * 40, "o" + i, over[i] || "", i < over.length ? "cell-ok" : "f3", 1, 260, 34);
    if (k >= 1) o += SV.text(450, 182, "keys 1055 and 2310 both hash to location 0", "sm");
    if (k >= 2) o += arrow(318, 50, 440, 50, "r", "c2", 1) ;
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "An overflow area", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Instead of searching on in the main file, a separate <b>overflow area</b> can hold the records that collide.", s: { i: 0 } },
    { cap: "Key 1055 hashes to 0, which is taken by 7630: a collision.", s: { i: 1 } },
    { cap: "1055 is stored in the next free space of the overflow area.", s: { i: 2 } },
    { cap: "Another collision with location 0 goes in the next overflow space. To find 1055 or 2310, check location 0 first, then search the overflow area linearly.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let size = 7, meth = 0, tab, over;
  const sizes = [5, 7, 11], meths = ["Linear probing", "Overflow area"];
  const reset = () => { tab = Array(size).fill(null); over = []; paint("Store some keys to see collisions."); };
  const paint = (msg) => {
    $$("#hZ button").forEach((b, i) => b.classList.toggle("pri", sizes[i] === size)); $$("#hM button").forEach((b, i) => b.classList.toggle("pri", i === meth));
    $("#hT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th>' + tab.map((_, i) => `<td>${i}</td>`).join("") + "</tr><tr><th>Key</th>" + tab.map((k) => `<td>${k === null ? "" : k}</td>`).join("") + "</tr></table></div>" + (meth === 1 ? '<div class="tw"><table class="t mono"><tr><th>Overflow area</th>' + (over.length ? over.map((k) => `<td>${k}</td>`).join("") : "<td>(empty)</td>") + "</tr></table></div>" : "");
    $("#hV").textContent = msg;
  };
  const store = (key) => {
    const h = key % size;
    if (tab.includes(key) || over.includes(key)) return "Key " + key + " is already stored.";
    if (tab[h] === null) { tab[h] = key; return key + " MOD " + size + " = " + h + ": location " + h + " is free, so it is stored there."; }
    if (meth === 1) { over.push(key); return key + " MOD " + size + " = " + h + ": location " + h + " holds " + tab[h] + ". COLLISION: stored in the overflow area."; }
    for (let i = 1; i < size; i++) { const j = (h + i) % size; if (tab[j] === null) { tab[j] = key; return key + " MOD " + size + " = " + h + ": location " + h + " holds " + tab[h] + ". COLLISION: next free location is " + j + ", so it is stored there."; } }
    return "The table is full.";
  };
  const find = (key) => {
    const h = key % size; let reads = 1;
    if (tab[h] === key) return key + " MOD " + size + " = " + h + ": found at location " + h + " after 1 read.";
    if (meth === 1) { const i = over.indexOf(key); if (i >= 0) return "Location " + h + " holds a different key, so the overflow area is searched: found at overflow position " + i + " after " + (1 + i + 1) + " reads."; return "Not at location " + h + " and not in the overflow area: the record is not in the file."; }
    for (let i = 1; i < size; i++) { const j = (h + i) % size; reads++; if (tab[j] === key) return key + " hashes to " + h + " but is at location " + j + ": found after " + reads + " reads."; if (tab[j] === null) return "An empty location was reached after " + reads + " reads: the record is not in the file."; }
    return "Not found.";
  };
  $("#hZ").innerHTML = sizes.map((s) => `<button class="b">Table size ${s}</button>`).join(""); $("#hM").innerHTML = meths.map((m) => `<button class="b">${m}</button>`).join("");
  $$("#hZ button").forEach((b, i) => (b.onclick = () => { size = sizes[i]; reset(); })); $$("#hM button").forEach((b, i) => (b.onclick = () => { meth = i; reset(); }));
  $("#hS").onclick = () => { const k = parseInt($("#hK").value, 10); if (isNaN(k)) return; paint(store(k)); };
  $("#hF").onclick = () => { const k = parseInt($("#hK").value, 10); if (isNaN(k)) return; paint(find(k)); };
  $("#hR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let key = 1029, size = 5;
  const paint = () => { const q = Math.floor(key / size); $("#c1").textContent = key % size; $("#c2").textContent = key + " = " + size + " × " + q + " + " + (key % size); };
  Lib.slider($("#cK"), { id: "cks", label: "Key ", min: 1000, max: 9999, value: key, fmt: (x) => x, onInput: (v) => { key = v; paint(); } });
  Lib.slider($("#cZ"), { id: "czs", label: "Table size (MOD) ", min: 2, max: 13, value: size, fmt: (x) => x, onInput: (v) => { size = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["Linear probing", "Go to the next location after the hashed one, and onwards, until a free one is found; store there", "Start at the hashed location and search linearly until the key matches; an empty location means not found", "No extra area needed; clusters can form and slow searches"],
  ["Overflow area", "Store the record in the next free space of a separate overflow area", "If the hashed location holds another key, search the overflow area linearly", "Main file stays tidy; the overflow area has to be searched in order"],
  ["Chaining", "Each location refers to a chain of items; add the record to that chain", "Search the chain at the hashed location", "A location can hold many items; chains need extra space for references"]
], ["Method", "Storing a record", "Finding a record", "Notes"]);
''' + CLASSIFY("cl1", "True or false for hashing?", ["Describes hashing", "Does not describe hashing"],
  [("A formula applied to the key field to give an address", 0), ("The same key always gives the same address", 0), ("Two keys can give the same hash value", 0), ("The records are stored in key order", 1), ("It is used to give direct access to a random file", 0), ("It encrypts the record so it cannot be read", 1)],
  "Hashing calculates an address from the key. It does not sort or encrypt.") + CLASSIFY("cl2", "Is the step part of storing a record or finding a record?", ["Storing", "Finding"],
  [("Calculate the hash of the key and go to that location", 0), ("Write the record at the first free location after a collision", 0), ("Compare the key at the location with the one searched for", 1), ("Search the overflow area until the key matches", 1), ("Search linearly for the next available space", 0), ("An empty location means the record is not in the file", 1)],
  "Storing looks for a free place. Finding looks for the matching key.") + ORDER(
  "Put the steps for storing a record when a collision occurs in order.",
  ["Apply the hashing algorithm to the key", "Go to the location calculated", "Find that the location is already used by another record (a collision)", "Search linearly for the next free location", "Store the record there"],
  "Hash, go, collision, search on, store.") + MATCH([
  ["Hashing algorithm", "A formula applied to the key to give an address"], ["Hash value", "The location calculated from a key"], ["Collision", "Two different keys giving the same hash value"], ["Linear probing", "Storing in the next free location after the hashed one"], ["Overflow area", "A separate area for records whose location is taken"]]) + CALC([
  {"q": "Hash(Key) = Key MOD 5. What is the hash value of 1029?", "a": 4, "unit": "", "tol": 0.01, "hint": "1029 = 5 × 205 + 4.", "sol": "<b>4</b>."},
  {"q": "Hash(Key) = Key MOD 3. What is the hash value of 1025?", "a": 2, "unit": "", "tol": 0.01, "hint": "1025 = 3 × 341 + 2.", "sol": "<b>2</b>."},
  {"q": "Hash(Key) = Key MOD 7. What is the hash value of 3003?", "a": 0, "unit": "", "tol": 0.01, "hint": "3003 = 7 × 429.", "sol": "<b>0</b>."},
  {"q": "Hash(Key) = Key MOD 10. What is the hash value of 7845?", "a": 5, "unit": "", "tol": 0.01, "hint": "The last digit.", "sol": "<b>5</b>."},
  {"q": "With MOD 5, keys 12 and 27 are stored. At which location is 27 stored if linear probing is used and location 2 is taken by 12?", "a": 3, "unit": "", "tol": 0.01, "hint": "27 MOD 5 = 2 (taken), so the next free location is 3.", "sol": "<b>3</b>."},
  {"q": "A table has 11 locations. What is the largest hash value that Key MOD 11 can give?", "a": 10, "unit": "", "tol": 0.01, "hint": "Remainders run 0 to 10.", "sol": "<b>10</b>."}]) + MCQ([
  ("What is a hashing algorithm?", ["A way to sort records", "A formula that calculates an address from the key field", "A kind of encryption", "A file type"], 1, "It gives the address where the record is stored or found."),
  ("What is a collision?", ["A corrupted record", "Two different keys giving the same hash value", "A full disk", "A deleted record"], 1, "The location is already in use."),
  ("Which is a way to deal with a collision?", ["Delete the record", "Store it in the next free location or an overflow area", "Change the key", "Sort the file"], 1, "Linear probing or an overflow area."),
  ("What does 3003 MOD 5 equal?", ["600", "3", "5", "0"], 1, "The remainder after dividing 3003 by 5."),
  ("How is a record found after a collision?", ["Search the whole file from the start", "Search on linearly from the hashed location (or the overflow area) until the key matches", "Calculate a new key", "It cannot be found"], 1, "Use the same method used to store it."),
  ("Hashing gives direct access to which file organisation?", ["Serial", "Random", "Text", "None"], 1, "Random files use a hash to find the address.")], "qz1") + CARDS([
  ("Hashing algorithm", "A formula applied to the key to calculate an address."), ("MOD", "Remainder after integer division. Gives 0 to size - 1."), ("Collision", "Two keys give the same hash value; the location is used."), ("Linear probing", "Store in the next free location; find by searching on linearly."),
  ("Overflow area", "Separate area for colliding records; search it linearly."), ("Chaining", "A location holds a chain of items."), ("Good hash", "Fast, consistent, spreads keys evenly."), ("Used for", "Direct access to random files.")])

build("ac1322", "ac-13-2-2-hashing", "Hashing Algorithms", EYA("13.2.2"),
  "What a hashing algorithm does, MOD hash values, collisions and how they are resolved when storing and finding records; animations, a hash table sandbox and the real 9618 hashing questions from 2023 and 2024.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.2 File organisation and access"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
