"""A Level CS syllabus 1.1.2: negative integers, binary addition and subtraction, overflow. Run: python3 tools/artifact-kit/mk_ac112.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An 8-bit pattern can mean an unsigned number (0 to 255) or, using <b>two's complement</b>, a number from −128 to +127, where the left-most bit is worth −128. To make a number negative you <b>flip every bit and add 1</b>. Computers <b>add</b> by the same column rules you use in denary, and they <b>subtract</b> by adding the two's complement of the second number, then ignoring any carry out of the left. When the true answer needs more bits than are available the result is wrong, which is called <b>overflow</b>. Exam marks are for the working (carries, flips, the added 1) and then the answer, so write them down.</p></div>

  <h2>1 · Representing negative integers</h2>
  <p>A fixed number of bits is used, so the first job is to know what the pattern means. The syllabus asks for <b>one's complement</b> and <b>two's complement</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>Representation</th><th>How negative numbers are made</th><th>8-bit range</th><th>Notes</th></tr>
    <tr><td><b>Unsigned binary</b></td><td>No negatives</td><td>0 to 255</td><td>Column values 128, 64, 32 ... 1</td></tr>
    <tr><td><b>One's complement</b></td><td>Flip every bit of the positive value</td><td>−127 to +127</td><td>Two patterns for zero: 0000 0000 and 1111 1111</td></tr>
    <tr><td><b>Two's complement</b></td><td>Flip every bit, then add 1</td><td>−128 to +127</td><td>One zero. The left-most column is worth −128.</td></tr>
  </table></div>
  <p>For <i>n</i> bits, two's complement holds −2<sup><i>n</i>−1</sup> to 2<sup><i>n</i>−1</sup> − 1. With 10 bits that is −512 to +511.</p>

  <h3>Making a number negative</h3>
  <ol>
    <li>Write the positive value in the full number of bits: 30 = 0001 1110.</li>
    <li>Flip every bit: 1110 0001. (This is the <b>one's complement</b>.)</li>
    <li>Add 1: 1110 0010. This is <b>−30</b> in 8-bit two's complement.</li>
  </ol>
  <p>A shortcut: copy bits from the right up to and including the first 1, then flip the rest. 0001 1110 → 1110 0010.</p>
  <h3>Reading a two's complement number</h3>
  <p>If the left-most bit is 0 the number is positive: read it as normal. If it is 1, work with column values where the first column is <b>−128</b>. For 1110 0010: −128 + 64 + 32 + 2 = <b>−30</b>. For 1110 0111: −128 + 64 + 32 + 4 + 2 + 1 = <b>−25</b>. For 0110 1011: 64 + 32 + 8 + 2 + 1 = <b>107</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>Denary</th><th>8-bit two's complement</th><th>Check</th></tr>
    <tr><td>+127 (largest)</td><td>0111 1111</td><td>64 + 32 + 16 + 8 + 4 + 2 + 1</td></tr>
    <tr><td>+1</td><td>0000 0001</td><td>1</td></tr>
    <tr><td>0</td><td>0000 0000</td><td></td></tr>
    <tr><td>−1</td><td>1111 1111</td><td>−128 + 127</td></tr>
    <tr><td>−30</td><td>1110 0010</td><td>−128 + 64 + 32 + 2</td></tr>
    <tr><td>−128 (smallest)</td><td>1000 0000</td><td>−128</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>For "smallest and largest two's complement number in <i>n</i> bits" write the patterns: smallest is a 1 followed by zeros (1000 0000), largest is a 0 followed by ones (0111 1111). Give the denary value as well if you have time.</div>

  <h2>2 · Binary addition</h2>
  <div class="tw"><table class="t mono">
    <tr><th>Column sum</th><th>Write</th><th>Carry</th></tr>
    <tr><td>0 + 0 = 0</td><td>0</td><td>0</td></tr>
    <tr><td>0 + 1 = 1</td><td>1</td><td>0</td></tr>
    <tr><td>1 + 1 = 10</td><td>0</td><td>1</td></tr>
    <tr><td>1 + 1 + 1 (with a carry) = 11</td><td>1</td><td>1</td></tr>
  </table></div>
  <p>Work from the right, writing the carry above the next column. 1011 0000 + 0001 1011: the right-most columns give 1 and 1, then 0 + 1, and so on, and the answer is <b>1100 1011</b> (176 + 27 = 203). Adding three numbers works the same way, but a column can produce a carry of 2, so take the carries one column at a time.</p>

  <h2>3 · Overflow</h2>
  <p><b>Overflow</b> happens when the result of a calculation is too large to be stored in the number of bits available. The extra bit is lost, so the stored result is wrong.</p>
  <ul>
    <li><b>Unsigned numbers:</b> a carry out of the left-most column means the sum was more than 255. 1100 0000 + 0100 0000 = 1 0000 0000 needs nine bits, so the 8-bit result is 0000 0000.</li>
    <li><b>Two's complement numbers:</b> overflow occurs when two positives give a negative result, or two negatives give a positive one, because the answer is outside −128 to +127. 0110 0100 (100) + 0011 0010 (50) = 1001 0110, which reads as −106.</li>
    <li><b>Three numbers:</b> 1001 1110 + 0110 0001 + 0001 1001 is 158 + 97 + 25 = 280, which needs nine bits. The 8-bit result is 0001 1000 (24), and you write "overflow".</li>
  </ul>
  <p>The mark scheme definition is short: <i>the result is larger than can be stored in the number of bits available</i>.</p>

  <h2>4 · Binary subtraction</h2>
  <p>There are two accepted methods, and you can use either.</p>
  <h3>Method 1: add the two's complement</h3>
  <ol>
    <li>Write the number being subtracted in full width: 30 = 0001 1110.</li>
    <li>Make it negative: flip and add 1 to get 1110 0010.</li>
    <li>Add it to the first number: 0110 1011 + 1110 0010 = (1) 0100 1101.</li>
    <li>Ignore the carry out of the left-most column. The answer is <b>0100 1101</b> (107 − 30 = 77).</li>
  </ol>
  <h3>Method 2: direct subtraction with borrowing</h3>
  <p>Subtract column by column from the right, borrowing from the next column when the top bit is smaller than the bottom bit. Show the borrows. The mark scheme for a recent subtraction accepted direct subtraction if the borrows or carries were visible.</p>
  <div class="tip"><b class="h">Exam tip</b>Do not convert to denary and back. The mark schemes say there are no marks for converting the numbers to denary, subtracting, and converting the answer back to binary.</div>
  <p>The same circuit adds and subtracts, which is why two's complement is used: a processor needs only an adder and a way to flip bits and add 1.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Flipping the bits but forgetting to add 1, which gives the one's complement.</li>
    <li>Treating the left-most bit as +128 when the question says two's complement.</li>
    <li>Leaving out the carries, so the working mark is lost.</li>
    <li>Counting the ninth bit as part of an 8-bit answer instead of discarding it and saying overflow occurred.</li>
    <li>Using too few bits: the negative of 30 in 12 bits starts 1111, not 1110.</li>
  </ul>
'''

watch = '''
  <h2>1 · Adding two bytes: 1011 0000 + 0001 1011</h2>
  <p>Press Play, or click the numbered steps. The carry is written above the next column.</p>
  <div id="stA"></div>
  <h2>2 · Making −30 in two's complement</h2>
  <div id="stB"></div>
  <h2>3 · Subtracting by adding: 0110 1011 − 0001 1110</h2>
  <div id="stC"></div>
  <h2>4 · Overflow: 1100 0000 + 0100 0000</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · How many bits?</h2>
  <p>Drag the number of bits and compare what each representation can hold.</p>
  <div class="card"><div class="grid2"><div><div id="nb"></div>
    <div class="readout"><div><small>Unsigned range</small><strong id="n1"></strong></div><div><small>One's complement range</small><strong id="n2"></strong></div><div><small>Two's complement range</small><strong id="n3"></strong></div></div>
    <div class="verdict" id="nv"></div></div>
    <div><svg id="nS" viewBox="0 0 420 200" role="img" aria-label="Ranges on a number line"></svg></div></div></div>

  <h2>Lab 2 · Denary to 8-bit two's complement</h2>
  <p>Drag from −128 to +127. The left-most column is worth −128, and the total is added up for you.</p>
  <div class="card"><div id="tcs"></div><svg id="tcS" viewBox="0 0 760 150" role="img" aria-label="Eight bits with column values"></svg>
    <div class="readout"><div><small>8-bit pattern</small><strong id="tc1"></strong></div><div><small>Sum of columns</small><strong id="tc2"></strong></div></div></div>

  <h2>Lab 3 · Add two bytes and test for overflow</h2>
  <p>Choose two values from 0 to 255. See the 8-bit result, whether an unsigned overflow occurred, and what the answer means if the bytes are read as two's complement.</p>
  <div class="card"><div id="aA"></div><div id="aB"></div>
    <div class="readout"><div><small>A (binary)</small><strong id="a1"></strong></div><div><small>B (binary)</small><strong id="a2"></strong></div><div><small>8-bit result</small><strong id="a3"></strong></div><div><small>True total</small><strong id="a4"></strong></div></div>
    <div class="verdict" id="av"></div><div class="verdict" id="av2"></div></div>

  <h2>Lab 4 · Subtract by adding</h2>
  <p>Choose A and B (0 to 127). The page makes −B and adds it to A, then drops the carry.</p>
  <div class="card"><div id="sA"></div><div id="sB"></div>
    <div class="readout"><div><small>A</small><strong id="s1"></strong></div><div><small>B</small><strong id="s2"></strong></div><div><small>−B (two's complement)</small><strong id="s3"></strong></div><div><small>A + (−B), carry dropped</small><strong id="s4"></strong></div></div>
    <div class="verdict" id="sv"></div></div>
'''

practise = '''
  <h2>1 · Will this unsigned 8-bit addition overflow?</h2><div id="cl1" class="card"></div>
  <h2>2 · Positive, negative or too big for 8 bits?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the subtraction steps in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The counter that ran out", "A large aircraft's control software once kept time in a counter that grew every hundredth of a second in a 32-bit signed number. After about 248 days of continuous power it would have overflowed, and the fix was to restart the systems before then and update the software.", "give a consequence of overflow: the stored value wraps to a wrong, often negative, value.") +
rw("A rocket and a number that did not fit", "In 1996 a rocket's guidance software converted a large number into a 16-bit signed integer that was too small to hold it. The overflow caused an error and the launch failed shortly after take-off.", "overflow is an error condition because the result is too large for the bits available.") +
rw("The view counter", "A video site once had a view count stored as a 32-bit signed integer, with a largest value of 2 147 483 647. A video passed that total, and the site changed the field to a 64-bit number.", "n bits signed holds up to 2^(n−1) − 1, so a larger count needs more bits.") +
rw("One circuit for add and subtract", "A processor's arithmetic logic unit only needs an adder. To subtract, it flips the bits of the second number, adds 1, and adds. This is why two's complement is used instead of storing a separate sign.", "explain why two's complement is useful: the same hardware adds and subtracts, and there is only one zero.") +
rw("Odometers", "A mechanical or digital counter that reaches its largest value rolls over to zero. An unsigned 8-bit counter does the same: 255 plus 1 gives 0, with a carry that is lost.", "unsigned overflow: a carry out of the left-most column that is not stored.")
)

items = [("s23_11", "3(d)(iv)", 2), ("s23_11", "3(d)(v)", 2), ("s25_12", "2(b)", 3), ("s26_11", "1(b)-(c)", 3), ("w22_11", "1(a)(iii)", 1), ("w22_11", "1(b)", 2),
         ("w21_11", "1(b)", 3), ("s24_11", "7", 3), ("s24_13", "1(c)", 1), ("s21_11", "1(c)(ii)-(iii)", 6), ("w23_12", "3(b)(i)", 1)]

exam = aexam("negative integers, binary addition and subtraction, and overflow",
  "Eleven questions from the 2021 to 2026 Paper 1 papers. The working marks are earned by showing carries, flips and the added 1. The numbers here are changed from the originals, so the answers are our own.",
  items, [
  ceq(AP("s23_11", "3(d)(iv)"), "[2]", "Give the smallest and the largest two's complement binary integer that can be represented using 10 bits.",
      ["Smallest: 10 0000 0000 (−512).", "Largest: 01 1111 1111 (511)."],
      "<p>Smallest is a 1 followed by nine 0s. Largest is a 0 followed by nine 1s. The range for n bits is −2<sup>n−1</sup> to 2<sup>n−1</sup> − 1.</p>",
      [[("k", "Smallest: 1000000000, which is −512. Largest: 0111111111, which is 511.")]]) +
  ceq(AP("s23_11", "3(d)(v)"), "[2]", "Add these two binary integers using binary addition. Show your working. 0110 1101 and 0011 0111.",
      ["One mark for the working: carries shown.", "One mark for the answer 1010 0100."],
      "<p>Write the carries above each column. 109 + 55 = 164, which is 1010 0100, and there is no carry out of the left-most column.</p>",
      [[("k", "Carries 1 1 1 1 1 1 across the columns; the result is 1010 0100 (109 + 55 = 164).")]]) +
  ceq(AP("s25_12", "2(b)"), "[3]", "(i) Convert the two's complement binary integer 1101 0100 into denary. (ii) Write the 8-bit two's complement form of denary −35.",
      ["−44 using −128 + 64 + 16 + 4.", "−35: 0010 0011, flipped 1101 1100, plus 1 gives 1101 1101."],
      "<p>Left column is −128, so add the other set columns to it. For −35, write 35 in eight bits, flip, add 1.</p>",
      [[("k", "−128 + 64 + 16 + 4 = −44. 35 = 0010 0011, flip 1101 1100, add 1 = 1101 1101.")]]) +
  ceq(AP("s26_11", "1(b)-(c)"), "[3]", "(i) Convert the 8-bit two's complement integer 0101 1100 into denary. (ii) Show how denary 25 is subtracted from 0101 1100 using binary subtraction. Show your working.",
      ["92 (64 + 16 + 8 + 4).", "Working: −25 as 1110 0111 added to 0101 1100, or direct subtraction with borrows shown.", "Answer: 0100 0011 (67)."],
      "<p>Method 1: 25 = 0001 1001, flip 1110 0110, add 1 = 1110 0111. Add: 0101 1100 + 1110 0111 = (1) 0100 0011. Drop the carry. Do not convert to denary and back.</p>",
      [[("k", "0101 1100 = 64 + 16 + 8 + 4 = 92. 25 = 0001 1001, flip 1110 0110, add 1 = 1110 0111. 0101 1100 + 1110 0111 = (1) 0100 0011, so the answer is 0100 0011 after the carry is dropped.")]]) +
  ceq(AP("w22_11", "1(a)(iii)"), "[1]", "Convert the 8-bit two's complement binary integer 1100 1101 into denary.",
      ["−51."],
      "<p>−128 + 64 + 8 + 4 + 1.</p>",
      [[("k", "−128 + 64 + 8 + 4 + 1 = −51.")]]) +
  ceq(AP("w22_11", "1(b)"), "[2]", "Perform the binary subtraction. Show your working. 1011 0100 − 0110 0111.",
      ["One mark for working (borrows, or the two's complement of 0110 0111 added).", "One mark for the answer 0100 1101."],
      "<p>180 − 103 = 77 = 0100 1101. By two's complement: 0110 0111 becomes 1001 1001, and 1011 0100 + 1001 1001 = (1) 0100 1101.</p>",
      [[("k", "0110 0111 flipped is 1001 1000, plus 1 is 1001 1001. 1011 0100 + 1001 1001 = (1) 0100 1101. The carry is ignored, so the answer is 0100 1101.")]]) +
  ceq(AP("w21_11", "1(b)"), "[3]", "(i) Perform the binary addition. Show your working. 1001 0110 + 0110 1111. (ii) State how an overflow can occur when adding two binary integers.",
      ["One mark for the working and one for the answer 0000 0101 with the ninth bit lost.", "Overflow: the result is a larger number than can be stored in the given number of bits, for example greater than 255 for 8 bits."],
      "<p>150 + 111 = 261, which needs nine bits. The 8-bit result is 0000 0101, and overflow has occurred.</p>",
      [[("k", "1001 0110 + 0110 1111 = 1 0000 0101, so the 8-bit result is 0000 0101 and the carry out of the left is lost. Overflow occurs when the result is a larger number than can be stored in the number of bits available.")]]) +
  ceq(AP("s24_11", "7"), "[3]", "Complete the binary addition. Show your working. 1100 0110 + 0100 0011 + 0010 1001.",
      ["Working shown with the carries.", "Correct 8-bit answer 0011 0010.", "Overflow clearly indicated."],
      "<p>198 + 67 + 41 = 306, which is more than 255. 306 − 256 = 50 = 0011 0010. Write the word overflow next to the answer.</p>",
      [[("k", "The 8-bit result is 0011 0010 with the carries shown in each column. The true total is 306, which needs nine bits, so overflow has occurred.")]]) +
  ceq(AP("s24_13", "1(c)"), "[1]", "State what is meant by an overflow in binary addition.",
      ["The answer is too long to be stored in the same number of bits as the numbers being added, or is larger than the largest number the bits can hold."],
      "<p>One precise sentence is enough.</p>",
      [[("k", "The result of the addition needs more bits than are available, so the extra bit is lost and the stored answer is wrong.")]]) +
  ceq(AP("s21_11", "1(c)(ii)-(iii)"), "[6]", "(i) Add denary 20 to the binary number 0101 0101 and give the answer in binary. Perform the addition in binary and show your working. (ii) Subtract denary 12 from the two's complement number 0011 0101. Give the answer in binary and show your working.",
      ["20 converted to 0001 0100, then a method of addition shown, then the answer 0110 1001.", "−12 formed as 1111 0100 (0000 1100 flipped 1111 0011, plus 1), added to 0011 0101, then the answer 0010 1001."],
      "<p>Three marks each. (i) 85 + 20 = 105. (ii) 53 − 12 = 41. In (ii), 0011 0101 + 1111 0100 = (1) 0010 1001, and the carry is dropped.</p>",
      [[("k", "20 = 0001 0100. 0101 0101 + 0001 0100 = 0110 1001. 12 = 0000 1100, flip 1111 0011, add 1 = 1111 0100. 0011 0101 + 1111 0100 = (1) 0010 1001, so the answer is 0010 1001.")]]) +
  ceq(AP("w23_12", "3(b)(i)"), "[1]", "Convert denary −150 into a 12-bit two's complement binary integer.",
      ["1111 0110 1010."],
      "<p>150 = 0000 1001 0110. Flip: 1111 0110 1001. Add 1: 1111 0110 1010. The pattern must be twelve bits and start with 1.</p>",
      [[("k", "150 = 0000 1001 0110. Flip to 1111 0110 1001 and add 1 to get 1111 0110 1010.")]])
])

tips = tips_html([
  ("Write the full width first.", "Put the positive number in 8 or 12 bits before you flip. Short patterns give wrong negatives."),
  ("Flip, then add 1.", "Flipping alone is the one's complement. The mark is for the added 1."),
  ("Show the carries.", "Write each carry above its column. It is the working mark."),
  ("Ignore the carry out when subtracting.", "In two's complement subtraction the ninth bit is discarded and the answer is the other eight bits."),
  ("Say overflow in words.", "When the true answer does not fit, write the 8-bit result and the word overflow."),
  ("Do not go through denary.", "Mark schemes give no marks for converting to denary, calculating, and converting back."),
], [
  ("what overflow is", "The result is larger than can be stored in the number of bits available, so the extra bit is lost."),
  ("why two's complement is used", "The same adder can add and subtract, and there is only one representation of zero."),
  ("how to find the negative", "Write the positive number in the full width, flip every bit, then add 1."),
  ("the range of n bits", "Two's complement can store −2^(n−1) to 2^(n−1) − 1; for 8 bits that is −128 to 127."),
], [("Convert", "Change to the representation asked for, with the working shown."), ("Perform", "Carry out the addition or subtraction and show the carries or borrows."), ("State", "A short, precise sentence."), ("Show", "Give the method as well as the result.")]) + FC

js = AKJS + r'''
/* column adder: rows a, b, result with carries; k columns done */
function addSteps(el, a, b, label, sub) {
  const n = a.length, res = [], car = Array(n + 1).fill(0), why = [];
  let c = 0;
  for (let j = n - 1; j >= 0; j--) { const s = +a[j] + +b[j] + c, w = s % 2, co = s >> 1; res[j] = w; car[j] = co; why[n - 1 - j] = `Column ${n - j}: ${a[j]} + ${b[j]}${c ? " + carry 1" : ""} = ${s.toString(2)}. Write <b>${w}</b>${co ? ", carry <b>1</b> to the next column" : ", no carry"}.`; c = co; }
  const out = c, total = parseInt(a, 2) + parseInt(b, 2);
  const draw = (s) => {
    const X0 = 60, W = 64, G = 16; let o = "";
    o += SV.text(24, 134, "+", "lbl bd", { "text-anchor": "middle", style: "font-size:26px" }) + SV.line(40, 160, 730, 160, "ax");
    o += boxRow(a.split("").map((t) => ({ t, c: "f1" })), X0, 62, W, 44, G, { fs: 20 });
    o += boxRow(b.split("").map((t) => ({ t, c: "f1" })), X0, 112, W, 44, G, { fs: 20 });
    for (let j = 0; j < n; j++) {
      const k = n - 1 - j, v = clamp01(s.k - k), x = X0 + j * (W + G);
      if (v > 0) o += boxRow([{ t: res[j], c: "f2", v }], x, 168, W, 44, 0, { fs: 20 });
      if (v > 0 && car[j] && j > 0) o += SV.text(X0 + (j - 1) * (W + G) + W / 2, 52, "1", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px", ...op(v) });
    }
    if (s.k > 0 && s.k < n + 0.5) { const j = n - Math.max(1, Math.min(n, Math.ceil(s.k))), x = X0 + j * (W + G); o += SV.rect(x - 6, 56, W + 12, 160, "f3", { rx: 10, style: "fill:none;stroke:var(--accent);stroke-width:2.5px" }); }
    if (s.k >= n && out) o += SV.text(X0 - 30, 196, "1", "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:22px" }) + SV.text(X0 - 30, 218, "lost", "sm", { "text-anchor": "middle" });
    o += SV.text(40, 40, "carries", "sm");
    return o;
  };
  const steps = [{ cap: `Write the two numbers in columns, one above the other. Start at the <b>right-most</b> column and write any carry above the next column. ${sub || ""}`, s: { k: 0 } }];
  for (let k = 0; k < n; k++) steps.push({ cap: why[k], s: { k: k + 1 } });
  steps.push({ cap: out ? `The result is <b>${res.join("")}</b> after dropping the ninth bit. The true total is ${total}, which is more than ${2 ** n - 1}, so <b>overflow</b> has occurred.` : `Result: <b>${res.join("")}</b> = ${total}. No carry out of the left-most column, so no overflow.`, s: { k: n + 1 } });
  Lib.stepper($(el), { w: 760, h: 236, label, base: { k: 0 }, draw, tween: 500, dwell: 3400, steps });
}
addSteps("#stA", "10110000", "00011011", "Adding 10110000 and 00011011 column by column", "Here 176 + 27 = 203.");
addSteps("#stC", "01101011", "11100010", "Adding 01101011 and the two's complement of 30", "This is 107 − 30, done by adding −30 (1110 0010).");
addSteps("#stD", "11000000", "01000000", "Overflow when adding 11000000 and 01000000", "192 + 64 = 256.");

(function () {
  const n = 30, p = bin(n), f = p.split("").map((x) => (x === "1" ? "0" : "1")).join(""), r = bin((~n + 1) & 255);
  const draw = (s) => {
    const row = (str, y, c, v, lab) => (v > 0 ? SV.text(20, y + 28, lab, "sm", op(v)) + boxRow(str.split("").map((t) => ({ t, c, v })), 80, y, 64, 44, 16, { fs: 20 }) : "");
    let o = row(p, 20, "f1", 1, "30");
    o += row(f, 86, "f3", clamp01(s.a), "flip");
    o += row(r, 152, "f2", clamp01(s.b), "+ 1");
    if (s.c > 0) o += SV.text(380, 226, "= −30 in 8-bit two's complement", "lbl bd t3", { "text-anchor": "middle", ...op(clamp01(s.c)) });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 244, label: "Making -30 in two's complement", base: { a: 0, b: 0, c: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "Write the positive number in the full width: 30 = <b>" + p + "</b>.", s: {} },
    { cap: "Flip every bit (1 becomes 0, 0 becomes 1): <b>" + f + "</b>. This is the one's complement.", s: { a: 1 } },
    { cap: "Add 1: " + f + " + 1 = <b>" + r + "</b>.", s: { a: 1, b: 1 } },
    { cap: "Check by adding the column values with −128: −128 + 64 + 32 + 2 = −30.", s: { a: 1, b: 1, c: 1 } }] });
})();

/* Lab 1 */
Lib.slider($("#nb"), { id: "nbs", label: "Number of bits ", min: 2, max: 16, value: 8, fmt: (x) => x, onInput: (n) => {
  const u = 2 ** n - 1, t = 2 ** (n - 1);
  $("#n1").textContent = "0 to " + u.toLocaleString("en-GB"); $("#n2").textContent = -(t - 1) + " to " + (t - 1); $("#n3").textContent = -t + " to " + (t - 1);
  $("#nv").textContent = `${n} bits give ${(2 ** n).toLocaleString("en-GB")} different patterns. Two's complement splits them: ${t.toLocaleString("en-GB")} negative, zero, and ${(t - 1).toLocaleString("en-GB")} positive.`;
  $("#nS").innerHTML = SV.text(30, 36, "unsigned", "sm") + SV.rect(30, 44, 360, 24, "f1", { rx: 6, ...op(0.6) }) + SV.text(30, 88, "0", "sm") + SV.text(390, 88, u.toLocaleString("en-GB"), "sm", { "text-anchor": "end" })
    + SV.text(30, 124, "two's complement", "sm") + SV.rect(30, 132, 360, 24, "f2", { rx: 6, ...op(0.6) }) + SV.line(210, 128, 210, 162, "ax") + SV.text(30, 176, -t, "sm") + SV.text(210, 176, "0", "sm", { "text-anchor": "middle" }) + SV.text(390, 176, t - 1, "sm", { "text-anchor": "end" });
} });

/* Lab 2 */
Lib.slider($("#tcs"), { id: "tcv", label: "Denary value ", min: -128, max: 127, value: -30, fmt: (x) => x, onInput: (v) => {
  const s = bin(v & 255), pv = [-128, 64, 32, 16, 8, 4, 2, 1];
  $("#tc1").textContent = grp4(s); $("#tc2").textContent = pv.map((p, i) => (s[i] === "1" ? p : 0)).filter((x) => x).join(" + ").replace(/\+ -/g, "- ") || "0";
  $("#tcS").innerHTML = boxRow(s.split("").map((t, i) => ({ t, c: t === "1" ? (i === 0 ? "f3" : "f2") : "f1", top: pv[i] })), 60, 40, 64, 52, 16) + SV.text(380, 130, "= " + v, "lbl bd t3", { "text-anchor": "middle", style: "font-size:20px" });
} });

/* Lab 3 */
(function () {
  let A = 200, B = 100;
  const paint = () => {
    const sA = bin(A), sB = bin(B), t = A + B, r = bin(t & 255), sa = A > 127 ? A - 256 : A, sb = B > 127 ? B - 256 : B, rs = (t & 255) > 127 ? (t & 255) - 256 : t & 255;
    $("#a1").textContent = grp4(sA); $("#a2").textContent = grp4(sB); $("#a3").textContent = grp4(r); $("#a4").textContent = t;
    $("#av").textContent = t > 255 ? `Unsigned: ${A} + ${B} = ${t}, which is more than 255, so there is a carry out and an overflow. The stored result is ${t & 255}.` : `Unsigned: ${A} + ${B} = ${t}, which fits in 8 bits. No overflow.`;
    const ov = sa + sb !== rs;
    $("#av2").textContent = `Two's complement: ${sa} + ${sb} = ${sa + sb}. ${ov ? "That is outside −128 to 127, so it overflows and the 8 bits read as " + rs + "." : "That is inside −128 to 127, so the 8 bits read correctly as " + rs + "."}`;
  };
  Lib.slider($("#aA"), { id: "asA", label: "A ", min: 0, max: 255, value: A, fmt: (x) => x, onInput: (v) => { A = v; paint(); } });
  Lib.slider($("#aB"), { id: "asB", label: "B ", min: 0, max: 255, value: B, fmt: (x) => x, onInput: (v) => { B = v; paint(); } });
})();

/* Lab 4 */
(function () {
  let A = 107, B = 30;
  const paint = () => {
    const nb = (-B) & 255, t = A + nb, r = t & 255, rs = r > 127 ? r - 256 : r;
    $("#s1").textContent = grp4(bin(A)); $("#s2").textContent = grp4(bin(B)); $("#s3").textContent = grp4(bin(nb)); $("#s4").textContent = grp4(bin(r));
    $("#sv").textContent = `${A} − ${B} = ${A - B}. The 8-bit sum is ${bin(t >= 256 ? t - 256 : t)} with ${t >= 256 ? "a carry that is dropped" : "no carry"}, which reads as ${rs}${A < B ? " (negative because B is larger)" : ""}.`;
  };
  Lib.slider($("#sA"), { id: "ssA", label: "A ", min: 0, max: 127, value: A, fmt: (x) => x, onInput: (v) => { A = v; paint(); } });
  Lib.slider($("#sB"), { id: "ssB", label: "B ", min: 0, max: 127, value: B, fmt: (x) => x, onInput: (v) => { B = v; paint(); } });
})();
''' + CLASSIFY("cl1", "Does the unsigned 8-bit addition overflow?", ["No overflow", "Overflow"],
  [("1010 1010 + 0101 0101 (170 + 85)", 0), ("1100 0000 + 0100 0000 (192 + 64)", 1), ("0111 1111 + 0000 0001 (127 + 1)", 0), ("1111 0000 + 0001 1111 (240 + 31)", 1), ("0011 0011 + 0101 0101 (51 + 85)", 0), ("1000 0000 + 1000 0000 (128 + 128)", 1)],
  "Overflow when the total is more than 255, which needs a ninth bit.") + CLASSIFY("cl2", "Read each 8-bit two's complement pattern. Is it positive or negative?", ["Positive or zero", "Negative"],
  [("0000 0000", 0), ("0111 1111", 0), ("1000 0000", 1), ("1111 1111", 1), ("0100 1101", 0), ("1110 0010", 1), ("1011 0100", 1), ("0001 1110", 0)],
  "In two's complement the left-most bit tells you the sign: 1 means negative.") + ORDER(
  "Put the steps for 0110 1011 − 0001 1110 using two's complement in order.",
  ["Write the number to subtract in full: 0001 1110", "Flip every bit: 1110 0001", "Add 1 to make −30: 1110 0010", "Add 0110 1011 + 1110 0010", "Ignore the carry out and write 0100 1101"],
  "Negate the second number, add, then drop the carry.") + MATCH([
  ["One's complement", "Flip every bit"], ["Two's complement", "Flip every bit, then add 1"], ["Overflow", "Result too large for the bits available"], ["Left-most bit (two's complement)", "Worth −128 in an 8-bit number"], ["Carry out", "A ninth bit produced when the sum is more than 255"]]) + CALC([
  {"q": "Convert the 8-bit two's complement number 1111 0001 into denary.", "a": -15, "unit": "", "tol": 0.01, "hint": "−128 + 64 + 32 + 16 + 1.", "sol": "<b>−15</b>."},
  {"q": "What is the largest number a 6-bit two's complement integer can hold?", "a": 31, "unit": "", "tol": 0.01, "hint": "2^5 − 1.", "sol": "<b>31</b>."},
  {"q": "What is the smallest number a 6-bit two's complement integer can hold?", "a": -32, "unit": "", "tol": 0.01, "hint": "−2^5.", "sol": "<b>−32</b>."},
  {"q": "Write denary −5 as an 8-bit two's complement integer (no spaces).", "t": ["11111011"], "unit": "", "hint": "5 = 00000101, flip 11111010, add 1.", "sol": "<b>1111 1011</b>."},
  {"q": "Add 0011 0110 and 0100 1001 in binary. Give the 8-bit answer (no spaces).", "t": ["01111111"], "unit": "", "hint": "54 + 73 = 127.", "sol": "<b>0111 1111</b>."},
  {"q": "How many different values can 12 bits represent?", "a": 4096, "unit": "", "tol": 0.01, "hint": "2^12.", "sol": "<b>4096</b>."},
  {"q": "A counter stores unsigned 8-bit values. It holds 250 and 10 is added. What does it hold afterwards?", "a": 4, "unit": "", "tol": 0.01, "hint": "260 − 256.", "sol": "<b>4</b>, and overflow has occurred."},
  {"q": "The one's complement of 0010 1101 is 1101 0010. What is the two's complement, as a denary value?", "a": -45, "unit": "", "tol": 0.01, "hint": "0010 1101 is 45, so its two's complement is −45.", "sol": "<b>−45</b> (1101 0011)."}]) + MCQ([
  ("How is the two's complement of a binary number found?", ["Flip every bit", "Add 1 to the number", "Flip every bit and add 1", "Move every bit one place left"], 2, "Flip, then add 1."),
  ("What is the range of an 8-bit two's complement integer?", ["0 to 255", "−127 to +127", "−128 to +127", "−256 to +255"], 2, "The left-most column is −128 and the rest add to 127."),
  ("What is the 8-bit two's complement pattern for −1?", ["1000 0001", "1111 1110", "1111 1111", "0000 0001"], 2, "1 = 0000 0001, flip 1111 1110, add 1 = 1111 1111."),
  ("1111 1111 + 0000 0001 is calculated using 8 bits. What happens?", ["The answer is 256", "A carry out is lost and the result is 0000 0000", "The answer is 1111 1111", "No error occurs and the result is 1 0000 0000"], 1, "The ninth bit does not fit, so the stored value is 0000 0000."),
  ("Why do computers use two's complement for negative numbers?", ["It uses fewer bits than other methods", "The same adder circuit can add and subtract", "It avoids all overflow", "It makes negative numbers look like denary"], 1, "Subtraction becomes addition of the negative."),
  ("When subtracting by adding the two's complement, what do you do with the carry out of the left-most column?", ["Add it back at the right", "Ignore it", "Write it as the sign bit", "Subtract it"], 1, "The carry is discarded; the remaining bits are the answer.")], "qz1") + CARDS([
  ("One's complement", "Flip every bit. Two zeros. 8-bit range −127 to +127."), ("Two's complement", "Flip every bit, then add 1. One zero. 8-bit range −128 to +127."), ("Sign bit", "Left-most bit. 1 means negative in two's complement."),
  ("Overflow", "Result too large for the bits available."), ("Carry out", "Ninth bit from adding two bytes. Lost in an 8-bit store."), ("Subtract", "Add the two's complement of the second number. Ignore the carry out."),
  ("Smallest 8-bit", "1000 0000 = −128."), ("Largest 8-bit", "0111 1111 = +127.")])

build("ac112", "ac-1-1-2-negative-numbers-binary-arithmetic", "Negative Integers, Binary Addition and Subtraction, and Overflow", EYA("1.1.2"),
  "One's and two's complement, adding and subtracting binary integers with the carries shown, how overflow happens, and eleven questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.1 Data representation"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
