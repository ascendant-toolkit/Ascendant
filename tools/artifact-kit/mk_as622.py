"""AS CS 6.2.2: data verification (visual check, double entry, parity, checksum). Run: python3 tools/artifact-kit/mk_as622.py"""
from ascs import *

def parity_bit(bits7, even=True):
    ones = bits7.count("1"); return str((ones % 2) if even else (1 - ones % 2))
assert parity_bit("0101110") == "0"           # w25 12 Q6(c)(i)
BLOCK = ["10110111", "01110000", "00010110", "01110100"]  # as printed in w25 12 Q6(c)(ii), parity bit is the last column
BLOCK = ["10110111", "01110000", "00011011", "01110100"]
PB = "10100000"
rows_bad = [i for i, r in enumerate(BLOCK) if r.count("1") % 2]
cols_bad = [j for j in range(8) if (sum(int(r[j]) for r in BLOCK) + int(PB[j])) % 2]
assert rows_bad == [1] and cols_bad == [4]    # the altered bit is row 2, column 5
def parity_fn(bs):
    return bs + ("1" if bs.count("1") % 2 else "0")
assert parity_fn("0010010110") == "00100101100" and parity_fn("101010") == "1010101"

def grid(rows, pb=None, mark=None, even=True):
    h = '<div class="tw"><table class="t mono"><tr><th></th>' + "".join(f"<th>{8 - i}</th>" for i in range(8)) + "</tr>"
    for i, r in enumerate(rows):
        h += f"<tr><td>byte {i + 1}</td>" + "".join(f'<td{" style=\"background:var(--accent-soft);font-weight:700\"" if mark == (i, j) else ""}>{c}</td>' for j, c in enumerate(r)) + "</tr>"
    if pb: h += "<tr><td>parity byte</td>" + "".join(f"<td>{c}</td>" for c in pb) + "</tr>"
    return h + "</table></div>"

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Data verification</b> checks that data entered or transferred is <b>the same as the original</b>; it does not check that the original was right. During <b>data entry</b> two methods are used: a <b>visual check</b> (a person compares the entered data with the original) and <b>double entry</b> (the data is entered twice and the computer compares them). During <b>data transfer</b> the methods are the <b>parity byte check</b>, the <b>parity block check</b> and the <b>checksum</b>. A parity bit is added so that the number of 1s in each byte is odd or even as agreed (7 bits of data plus one parity bit); the receiver recounts and an unexpected parity means an error. A <b>parity block check</b> adds parity in both directions so the position of a single wrong bit can be found; a <b>checksum</b> is calculated from the data, sent with it, recalculated by the receiver and compared.</p></div>

  <h2>1 · Verification during data entry</h2>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>How it works</th></tr>
    <tr><td><b>Visual check</b></td><td>The data entered is compared with the original by a person (for example reading the screen against the paper form, or printing a copy and comparing it)</td></tr>
    <tr><td><b>Double entry</b></td><td>The data is entered twice (by the same or by different people) and the computer compares the two entries; if they differ there is an error</td></tr>
  </table></div>

  <h2>2 · Verification during data transfer</h2>
  <h3>Parity byte check</h3>
  <p>Sender and receiver agree on <b>odd</b> or <b>even</b> parity. The data is split into groups (7 bits), the 1s in each group are counted and a <b>parity bit</b> is appended so the whole byte has an even (or odd) number of 1s. The receiver counts the 1s: if a byte with an odd number of 1s arrives when even parity is used, there is an error. Example, even parity: 0101110 has four 1s, so the parity bit is 0, giving 0101110<b>0</b>. 101010 has three 1s, so with even parity the parity bit is 1 (giving 1010101).</p>
  <h3>Parity block check</h3>
  <p>Bytes are grouped in a grid. Parity is calculated for each <b>row</b> (the parity bit) and for each <b>column</b> (the bits of the extra <b>parity byte</b>, sent with the data). When received, the rows and columns are recounted; the row with the wrong parity and the column with the wrong parity <b>locate the single bit that is wrong</b>, so it can be corrected.</p>
  <h3>Checksum</h3>
  <p>A calculation is made from the data and the result (the checksum) is transmitted with the data. The receiver repeats the calculation on the data received and compares it with the checksum received. If the two are different there is an error; if they match no error has been detected.</p>

  <h2>3 · Verification against validation</h2>
  <p><b>Verification</b> checks the data is the same as the original (or as sent). <b>Validation</b> checks the data is reasonable and in the right format. Neither proves the original data is accurate.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing that verification "checks the data is correct". It checks that it matches the original or the data sent.</li>
    <li>Describing double entry as "typing it again". The computer compares the two entries.</li>
    <li>Describing the checksum without the steps: calculate, send with the data, recalculate, compare.</li>
    <li>Counting the parity bit in the wrong way: with even parity the total number of 1s including the parity bit must be even.</li>
    <li>Saying a parity check can correct an error. A parity byte check only detects; a parity block check can locate a single wrong bit.</li>
  </ul>
'''

watch = '''
  <h2>1 · Double entry</h2>
  <div id="stA"></div>
  <h2>2 · An even parity bit</h2>
  <div id="stB"></div>
  <h2>3 · A parity block finds the wrong bit</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Parity bit</h2>
  <p>Click the seven data bits. The eighth bit is set so the byte has an even number of 1s.</p>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div><div class="btnrow"><button id="pEv" class="on">even parity</button><button id="pOd">odd parity</button></div></div>
  <h2>Lab 2 · Parity block</h2>
  <p>Click a bit to flip it as if it were damaged in transit. The marked row and column show where the error is.</p>
  <div class="card"><div id="bG"></div><div id="bV" class="verdict"></div></div>
  <h2>Lab 3 · Verification method</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

_pr, _prjs = PR(["Entry or transfer?", "Verification or validation?", "Match the method to its description", "Put the checksum steps in order", "Working out", "Multiple choice"],
  ("Used during data entry or data transfer?", ["Data entry", "Data transfer"], [("Visual check", 0), ("Parity byte check", 1), ("Double entry", 0), ("Checksum", 1), ("Comparing the screen with the paper form", 0), ("Parity block check", 1)], "Entry: visual, double entry. Transfer: parity, checksum."),
  ("Verification or validation?", ["Verification", "Validation"], [("Double entry", 0), ("Range check", 1), ("Visual check", 0), ("Presence check", 1), ("Checksum", 0), ("Format check", 1)], "Verification: the same as the original."),
  [["Visual check", "A person compares the entered data with the original"], ["Double entry", "The data is entered twice and compared by the computer"], ["Parity byte check", "A bit is added so each byte has an agreed number of 1s"], ["Parity block check", "Row and column parity locate a wrong bit"], ["Checksum", "A value calculated from the data and sent with it"]],
  ("Put the checksum steps in order.", ["A value is calculated from the data before transmission", "The value is transmitted with the data", "The receiver recalculates the value from the data received", "The two values are compared", "A difference means an error has occurred"], "Calculate, send, recalculate, compare, difference."),
  [{"q": "Even parity: the 7 data bits 1011001 have four 1s. What is the parity bit?", "a": 0, "unit": "", "tol": 0.01, "hint": "Four is already even.", "sol": "<b>0</b>."}, {"q": "Odd parity: the 7 data bits 1011001. What is the parity bit?", "a": 1, "unit": "", "tol": 0.01, "hint": "Four 1s; add a 1 to make five.", "sol": "<b>1</b>."}, {"q": "A byte with even parity arrives as 01101110 (five 1s). How many 1s should it have (even)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Even number: 4 or 6; the error is one bit wrong. Answer 4 or 6: give the lower.", "sol": "<b>4</b> (or 6): it has 5, so there is an error."}, {"q": "A parity block has 4 data bytes and a parity byte. How many bits are sent in total (8 bits each)?", "a": 40, "unit": "", "tol": 0.01, "hint": "5 × 8.", "sol": "<b>40</b>."}, {"q": "A checksum is the sum of the bytes mod 256. The bytes are 100, 200 and 50. What is the checksum?", "a": 94, "unit": "", "tol": 0.01, "hint": "350 mod 256.", "sol": "<b>94</b>."}],
  [("Double entry:", ["Data entered twice and compared", "Typed once", "A range check", "Compression"], 0, "Twice."), ("A parity bit makes the number of 1s:", ["Odd or even as agreed", "Always zero", "Always one", "Prime"], 0, "Odd or even."), ("Parity block can:", ["Locate a single wrong bit", "Correct all errors", "Encrypt", "Compress"], 0, "Locate."), ("A checksum is compared:", ["After transmission", "Never", "Before typing", "Only by hand"], 0, "After."), ("Verification checks data is:", ["The same as the original", "Sensible", "Encrypted", "Short"], 0, "Same as the original."), ("Visual check is used during:", ["Data entry", "Data transfer", "Encryption", "Back-up"], 0, "Entry.")],
  [("Verification", "Same as the original."), ("Visual check", "Person compares with the original."), ("Double entry", "Two entries compared by the computer."), ("Parity bit", "Makes the 1s odd or even."), ("Parity block", "Rows and columns find the bit."), ("Checksum", "Calculated, sent, recalculated, compared."), ("Entry", "Visual, double entry."), ("Transfer", "Parity, checksum.")])

real = RWNOTE + (
rw("Typing a password twice", "A sign-up form makes you type your new password twice and refuses if they differ: double entry.", "verification at data entry.") +
rw("Downloading a file", "Many download pages give a checksum; your computer recalculates it on the downloaded file and compares to be sure it arrived unchanged.", "checksum.") +
rw("Memory and network errors", "A parity bit on each byte catches a single flipped bit caused by noise on a line.", "parity byte check.") +
rw("A teacher reading marks back", "After typing marks from a paper register, the teacher reads the screen against the paper: a visual check.", "visual check.") +
rw("Barcode scanning", "A second scan of the same barcode and comparison guards against misreads.", "comparing to the original.")
)

where = [
  ("O/N 2021", "11, 13", "2(b)(ii)", "2", "How data verification helps to protect integrity, with an example"),
  ("O/N 2022", "12", "4(a), (b)", "1 + 3", "Verification against validation; how a checksum is used"),
  ("M/J 2022", "13", "5(b)(i)", "2", "A method of verification when transferring paper data to the computer"),
  ("M/J 2024", "11", "5(b)", "5", "Complete the description of parity byte and parity block checks"),
  ("M/J 2024", "13", "7(f)(i)", "4", "Two methods of data verification during transfer"),
  ("M/J 2025", "11", "7(c)", "3", "How data can be verified using a checksum"),
  ("M/J 2025", "23", "5", "8", "Write the module Parity() (Paper 2)"),
  ("O/N 2025", "12", "1", "2", "Match verification methods to data transfer or data entry"),
  ("O/N 2025", "12", "6(c)", "1 + 1", "Complete a parity bit; locate the altered bit in a parity block"),
  ("M/J 2026", "12", "2(a)", "4", "Two methods of data verification during data entry"),
  ("M/J 2026", "13", "1", "5", "Complete the description of verification and validation methods")]

past = '''  <p class="note">Parity is asked in a new form nearly every year: describe it, complete a byte, find a wrong bit, or write a Paper 2 function. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "11/13", "Q2(b)(ii)"), "2 marks", "Describe",
  "Describe how data verification helps to protect the integrity of the data. Give an example in your answer.", "Same as the original; double entry.",
  "<p>" + mks(["Verification checks that data is the same as the original", "Example: double entry"]) + "</p>", None) + peq(SRC("w22", "12", "Q4(a)(b)"), "1 + 3 marks", "State / Describe",
  "(a) State the difference between data verification and data validation. (b) A checksum can be used to detect errors during data transmission. Describe how a checksum is used.", "Same as the original against reasonable. Calculate, send, recalculate, compare.",
  "<p><b>(a)</b> " + mks(["Verification checks that input data is the same as the original; validation checks that the data is reasonable or sensible"]) + "</p><p><b>(b)</b> Any three: " + mks(["A checksum value is calculated from the data before transmission", "This calculated value is transmitted with the data", "The receiving computer recalculates the checksum from the received data", "If the checksum received and calculated match, no error has occurred; if they do not match an error has occurred"], "a") + "</p>", None) + peq(SRC("s22", "13", "Q5(b)(i)"), "2 marks", "Identify / Describe",
  "Identify and describe one method of data verification that can be used when transferring the data from paper to the computer.", "Visual check or double entry.",
  "<p>" + mks(["Visual check: manually compare the data entered with the original document", "Double entry: enter the data twice and the system compares them to see if they are the same"]) + " (name and description; either)</p>", None) + peq(SRC("s24", "11", "Q5(b)"), "5 marks", "Complete",
  "Parity check is one example of data verification. Computer A and Computer B agree on whether to use ... parity. Computer A divides the data into groups of ... . The number of 1s in each group is counted. If the agreed parity is ... and the group has an even number of 1s, a parity bit of 1 is appended, otherwise a parity bit of 0. In a parity ... check the bytes are grouped together in a grid; the number of 1s in each column is counted and a bit is assigned to each column. These parity bits are transmitted with the data as a parity ... .", "Odd or even; 7 bits; odd; block; byte.",
  "<p>" + mks(["odd or even", "7 bits", "odd", "block", "byte"]) + "</p>", None) + peq(SRC("s24", "13", "Q7(f)(i)"), "4 marks", "Identify",
  "Complete the table by identifying and describing two methods of data verification that can be used during data transfer.", "Parity byte, parity block, checksum.",
  "<p>One mark for each method and one for its description (max 4): " + mks(["Parity byte: an additional bit is added to make the number of 1s in the byte odd or even to match the parity; if a byte with an odd number of 1s is received when even parity is used, there is an error", "Parity block: parity is calculated horizontally and vertically; a parity byte is created from the vertical parity check and sent with the data; when received the position of an incorrect bit can be determined", "Checksum: a calculation is made from the data and the result transmitted with the data; the receiver repeats the calculation and compares; if different there is an error"]) + "</p>", None) + peq(SRC("s25", "11", "Q7(c)"), "3 marks", "Explain",
  "The data that is transferred can also be verified using a checksum. Explain how data can be verified using a checksum.", "Algorithm, send with data, receiver repeats, compare.",
  "<p>Any three: " + mks(["The data is put through an algorithm to create a checksum value", "The data and the checksum are sent to the receiver", "The receiver performs the same algorithm on the data", "If both checksums match the data is verified"]) + "</p>", None) + peq(SRC("s25", "23", "Q5"), "8 marks", "Write",
  "A module Parity() takes a string BitString representing a binary value. It concatenates '0' to the end if BitString contains an even number of 1s, or '1' if it contains an odd number, and returns the modified value. For example \"0010010110\" returns \"00100101100\" and \"101010\" returns \"1010101\". Write pseudocode for the module Parity().", "Count the 1s; MOD 2; append the character.",
  "<p>One answer:</p>" + code('''FUNCTION Parity(BitString : STRING) RETURNS STRING
   DECLARE Index, Count : INTEGER
   Count ← 0
   FOR Index ← 1 TO LENGTH(BitString)
      IF MID(BitString, Index, 1) = '1' THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   IF Count MOD 2 = 1 THEN
      BitString ← BitString & '1'
   ELSE
      BitString ← BitString & '0'
   ENDIF
   RETURN BitString
ENDFUNCTION'''.split("\n")) + "<p>" + mks(["Function heading, ending, STRING parameter and STRING return type", "Loop for the length of BitString", "Extract the current character in the loop", "Compare it to '1' or '0'", "Increment a count that was initialised", "Check if there is an even or odd number of 1s", "Append '1' or '0' as appropriate", "Return the amended BitString"]) + "</p>", "Appending the parity before the count is complete, or returning only the parity character.") + peq(SRC("w25", "12", "Q1"), "2 marks", "Match",
  "Draw one line from each verification method to indicate whether it is used during data transfer or data entry: parity byte check, checksum, visual check, parity block check.", "Transfer: parity and checksum. Entry: visual check.",
  "<p>" + mks(["Parity byte check, checksum and parity block check: data transfer (2 or 3 correct for 1 mark)", "Visual check: data entry (all four correct for 2 marks)"]) + "</p>", None) + peq(SRC("w25", "12", "Q6(c)"), "1 + 1 marks", "Complete / Circle",
  "A computer system uses even parity. The least significant (rightmost) bit of each byte is the parity bit. (i) Complete the byte 0101110_ by writing the missing parity bit. (ii) The computer also uses a parity block check with even parity. Computer B receives four bytes followed by a parity byte: 10110111, 01110000, 00011011, 01110100, parity byte 10100000. One of the four bytes has an error in one bit. Circle the bit that has been altered.", "Count the 1s in each byte and each column.",
  "<p><b>(i)</b> " + mks(["0 (the byte 01011100: the data has four 1s, which is already even)"]) + "</p><p><b>(ii)</b> " + mks(["The altered bit is in byte 2, fifth column from the left: byte 2 has an odd number of 1s (3), and only column 5 has the wrong parity"]) + "</p>" + grid(BLOCK, PB, mark=(1, 4)), "Looking at only the rows or only the columns. The error is where the wrong row and wrong column meet.") + peq(SRC("s26", "12", "Q2(a)"), "4 marks", "Describe",
  "Describe two methods of data verification that can be used during data entry.", "Visual check and double entry, each with a description.",
  "<p>One mark for each method and one for its description, twice: " + mks(["Visual check: the entered data is compared with the original by a person", "Double entry: enter the data twice and the computer automatically compares if they match"]) + "</p>", "Writing 'the data as intended' for the description. The comparison is with the original.") + peq(SRC("s26", "13", "Q1"), "5 marks", "Complete",
  "Complete the description of the methods of ensuring data integrity by writing the missing terms (visual check, checksum, existence check, format check, length check).", "Verification: visual check, checksum.",
  "<p>" + mks(["Visual check", "checksum", "Existence", "Format", "Length"]) + "</p>", None)

review = req("3 marks", "Describe", "Describe how double entry verifies the data for a new student record.", "Two entries.", "<p>" + mks(["The data is entered twice", "The computer compares the two entries", "If they differ an error is reported and the data must be re-entered"]) + "</p>", None) + req("2 marks", "Complete", "Even parity: write the parity bit for the 7 data bits 1100101.", "Count the 1s.", "<p>" + mks(["Four 1s, so the parity bit is 0", "The byte is 11001010"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a parity byte check cannot always detect an error.", "Two bits change.", "<p>" + mks(["If two bits in a byte change the number of 1s stays odd or even", "so the receiver does not detect the error"]) + "</p>", None) + req("3 marks", "Describe", "Describe how a checksum is used to detect errors in a downloaded file.", "Calculate and compare.", "<p>" + mks(["A value is calculated from the file by the sender and sent with it", "The receiver recalculates the value from the received file", "If the values differ there is an error"]) + "</p>", None) + req("2 marks", "State", "State two differences between a parity byte check and a parity block check.", "Direction, locate.", "<p>" + mks(["A parity byte check adds parity to each byte (rows) only; a block check uses rows and columns", "A block check can locate the wrong bit; a byte check can only detect an error in the byte"]) + "</p>", None)

tips = tips_html([
  ("Verification: same as the original.", "Not 'correct'."),
  ("Entry: visual check, double entry.", "Transfer: parity, checksum."),
  ("Parity: odd or even, 7 bits plus 1.", "Count the 1s including the parity bit."),
  ("Block: row and column.", "They cross at the wrong bit."),
  ("Checksum: four steps.", "Calculate, send, recalculate, compare."),
  ("Double entry: the computer compares.", "Say who compares."),
], [("verification", "Checking data is the same as the original."), ("a parity bit", "An extra bit making the number of 1s odd or even."), ("a checksum", "A value calculated from the data and sent with it."), ("double entry", "Entering the data twice and comparing.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Complete", "Fill in the gaps."), ("Write", "Give the pseudocode.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(30, 20, 200, 32, "cell", { rx: 6 }) + SV.text(40, 42, "entry 1: Smith", "lbl") + (k >= 1 ? SV.rect(30, 62, 200, 32, "cell", { rx: 6 }) + SV.text(40, 84, k >= 2 ? "entry 2: Smyth" : "entry 2: Smith", "lbl") : "") + (k >= 2 ? SV.rect(280, 40, 240, 36, "f2", { rx: 6 }) + SV.text(290, 63, "different: error, re-enter", "lbl bd") : "") + (k === 1 ? SV.rect(280, 40, 240, 36, "f1", { rx: 6 }) + SV.text(290, 63, "same: accepted", "lbl bd") : ""); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 120, label: "Double entry", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The name is entered once.", "It is entered a second time and the computer compares them: the same, so accepted.", "If the second entry differs the computer reports an error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const bits = "0101110"; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 7; i++) o += SV.rect(30 + i * 50, 30, 44, 36, bits[i] === "1" ? "f1" : "cell", { rx: 6 }) + SV.text(52 + i * 50, 54, bits[i], "lbl bd", { "text-anchor": "middle" }); o += SV.rect(380, 30, 44, 36, k >= 2 ? "f3" : "cell", { rx: 6 }) + SV.text(402, 54, k >= 2 ? "0" : "?", "lbl bd", { "text-anchor": "middle" }) + SV.text(380, 90, "parity bit", "sm");
    o += SV.text(30, 120, ["7 data bits: 0101110", "count the 1s: four", "four is even, so the parity bit is 0", "byte sent: 01011100; receiver counts: still even, accepted"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 460, h: 140, label: "Parity", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Seven data bits are to be sent with <b>even parity</b>.", "The sender counts the 1s.", "Four is already even, so the parity bit is 0.", "The receiver recounts: an odd count would mean an error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = ["10110111", "01110000", "00011011", "01110100"], pb = "10100000";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; rows.forEach((r, i) => { for (let j = 0; j < 8; j++) { const hot = (k >= 1 && i === 1) || (k >= 2 && j === 4); o += SV.rect(20 + j * 40, 14 + i * 28, 36, 24, k >= 3 && i === 1 && j === 4 ? "f2" : hot ? "f3" : "cell", { rx: 4 }) + SV.text(38 + j * 40, 31 + i * 28, r[j], "lbl", { "text-anchor": "middle" }); } }); for (let j = 0; j < 8; j++) o += SV.rect(20 + j * 40, 130, 36, 24, k >= 2 && j === 4 ? "f3" : "f1", { rx: 4 }) + SV.text(38 + j * 40, 147, pb[j], "lbl bd", { "text-anchor": "middle" });
    o += SV.text(350, 14, "", "sm"); return o; };
  Lib.stepper($("#stC"), { w: 360, h: 170, label: "Parity block", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Four bytes arrive with a parity byte (even parity, last column is each byte's parity bit).", "Row 2 has an odd number of 1s (three): the error is in this byte.", "Column 5 has the wrong parity: the error is in this bit position.", "The wrong bit is where row 2 and column 5 cross: a 0 that should be a 1."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let even = true; const bitsA = [0, 1, 0, 1, 1, 1, 0]; const bar = $("#pB");
  const paint = () => { bar.querySelectorAll("button").forEach((b, i) => { b.textContent = bitsA[i]; b.className = bitsA[i] ? "on" : ""; }); const ones = bitsA.reduce((a, b) => a + b, 0); const p = even ? ones % 2 : 1 - (ones % 2);
    $("#pO").innerHTML = `<div class="mono">${bitsA.join("")} <b>${p}</b></div><div class="verdict">${ones} ones in the data. For <b>${even ? "even" : "odd"}</b> parity the parity bit is <b>${p}</b>, so the whole byte ${bitsA.join("") + p} has ${ones + p} ones (${(ones + p) % 2 ? "odd" : "even"}).</div>`; };
  for (let i = 0; i < 7; i++) { const b = document.createElement("button"); b.onclick = () => { bitsA[i] ^= 1; paint(); }; bar.appendChild(b); }
  $("#pEv").onclick = () => { even = true; $("#pEv").className = "on"; $("#pOd").className = ""; paint(); }; $("#pOd").onclick = () => { even = false; $("#pOd").className = "on"; $("#pEv").className = ""; paint(); }; paint();
})();
(function () {
  const orig = ["1011011", "0111000", "0001101", "0111010"].map((r) => r.split("").map(Number)); const rowsP = orig.map((r) => r.reduce((a, b) => a + b, 0) % 2); const colsP = orig[0].map((_, j) => orig.reduce((a, r) => a + r[j], 0) % 2);
  let cur = orig.map((r) => r.slice());
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th></th>' + orig[0].map((_, j) => `<th>${j + 1}</th>`).join("") + "<th>parity</th></tr>"; const rbad = [], cbad = [];
    cur.forEach((r, i) => { if ((r.reduce((a, b) => a + b, 0) + rowsP[i]) % 2) rbad.push(i); }); orig[0].forEach((_, j) => { if ((cur.reduce((a, r) => a + r[j], 0) + colsP[j]) % 2) cbad.push(j); });
    cur.forEach((r, i) => { h += `<tr><td>byte ${i + 1}</td>` + r.map((c, j) => `<td><button data-r="${i}" data-c="${j}" style="min-width:34px;${rbad.includes(i) && cbad.includes(j) ? "background:var(--bad);color:#fff" : ""}">${c}</button></td>`).join("") + `<td>${rowsP[i]}</td></tr>`; });
    h += "<tr><td>parity byte</td>" + colsP.map((c) => `<td>${c}</td>`).join("") + "<td></td></tr></table></div>"; $("#bG").innerHTML = h;
    $("#bG").querySelectorAll("button").forEach((b) => b.onclick = () => { cur[+b.dataset.r][+b.dataset.c] ^= 1; paint(); });
    $("#bV").innerHTML = rbad.length === 0 && cbad.length === 0 ? "No error: every row and column has the agreed (even) parity. Click a bit to damage it." : rbad.length === 1 && cbad.length === 1 ? `Error located: byte <b>${rbad[0] + 1}</b>, bit <b>${cbad[0] + 1}</b> is wrong. It can be corrected by flipping it.` : "More than one bit is wrong: the errors are detected but cannot be located reliably."; };
  paint();
})();
btnTable("mB", "mO", [
  ["Reading the screen against the paper form", "Visual check", "Data entry"],
  ["Typing a new password twice", "Double entry", "Data entry"],
  ["An extra bit on each byte", "Parity byte check", "Data transfer"],
  ["Row and column parity to find a wrong bit", "Parity block check", "Data transfer"],
  ["A value calculated from the whole file", "Checksum", "Data transfer"]
], ["Description", "Method", "Used during"]);
''' + _prjs

finish("as-6-2-2-data-verification", "as622", "Data Verification",
  "Visual check, double entry, parity byte and block checks and the checksum, how each detects errors and where it is used, with animations, parity labs and the real Paper 1 and Paper 2 questions from 2021 to 2026.",
  "6.2.2", "6 · Security, privacy and data integrity", "section 6.2 Data integrity", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on data verification (Papers 1 and 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
