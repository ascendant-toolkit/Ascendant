"""A Level CS syllabus 1.1.1: binary prefixes, number bases, BCD and hexadecimal. Run: python3 tools/artifact-kit/mk_ac111.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Computers store everything in <b>binary</b>, and the syllabus expects you to move between <b>binary, denary and hexadecimal</b> and to describe <b>Binary Coded Decimal (BCD)</b>. Sizes use two sets of prefixes: <b>kilo, mega, giga, tera</b> are powers of 10 and <b>kibi, mebi, gibi, tebi</b> are powers of 2, so a kibibyte is 1024 bytes and a kilobyte is 1000. <b>Hexadecimal</b> is a shorthand for binary because one hex digit stands for exactly four bits. <b>BCD</b> stores each denary digit in its own four bits, which makes it easy to display and exact for money. Most marks in this topic are for a conversion with the working shown, a one-line difference, or a justified use of BCD or hex.</p></div>

  <h2>1 · Binary and decimal prefixes</h2>
  <p>A <b>decimal prefix</b> steps up by 1000 (10<sup>3</sup>) each time. A <b>binary prefix</b> steps up by 1024 (2<sup>10</sup>) each time, because memory addresses are binary and 1024 is the power of 2 closest to 1000.</p>
  <div class="tw"><table class="t">
    <tr><th>Decimal prefix</th><th>Bytes</th><th>Binary prefix</th><th>Bytes</th><th>Gap</th></tr>
    <tr><td><b>kilobyte</b> (kB)</td><td>1000 = 10<sup>3</sup></td><td><b>kibibyte</b> (KiB)</td><td>1024 = 2<sup>10</sup></td><td>2.4%</td></tr>
    <tr><td><b>megabyte</b> (MB)</td><td>1 000 000 = 10<sup>6</sup></td><td><b>mebibyte</b> (MiB)</td><td>1 048 576 = 2<sup>20</sup></td><td>4.9%</td></tr>
    <tr><td><b>gigabyte</b> (GB)</td><td>10<sup>9</sup></td><td><b>gibibyte</b> (GiB)</td><td>1 073 741 824 = 2<sup>30</sup></td><td>7.4%</td></tr>
    <tr><td><b>terabyte</b> (TB)</td><td>10<sup>12</sup></td><td><b>tebibyte</b> (TiB)</td><td>2<sup>40</sup></td><td>10.0%</td></tr>
  </table></div>
  <ul>
    <li><b>The pairs to know:</b> kibi and kilo, mebi and mega, gibi and giga, tebi and tera. The syllabus names exactly these four pairs.</li>
    <li><b>Moving between units</b> within one family multiplies or divides by the step: 3 kibibytes = 3 × 1024 = 3072 bytes, and 2 terabytes = 2 × 1000 = 2000 gigabytes. Do not mix families in one calculation.</li>
    <li><b>Why the gap matters:</b> storage makers advertise in decimal units while operating systems often report in binary units, so a 1 TB drive appears as about 931 GiB.</li>
    <li><b>Bits and bytes:</b> 1 byte = 8 bits, so a file of 1 kibibyte holds 8192 bits.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>A "difference between a kibibyte and a kilobyte" needs both values or both families: "kibibyte = 1024 bytes, kilobyte = 1000 bytes" or "kibi is a binary prefix, kilo is a denary prefix". Saying only "a kibibyte is bigger" is not enough.</div>

  <h2>2 · Number systems and place value</h2>
  <p>A number system is defined by its <b>base</b>: the number of different digits it uses. Each column is worth the base raised to a power.</p>
  <div class="tw"><table class="t">
    <tr><th>System</th><th>Base</th><th>Digits</th><th>Column values (right to left)</th></tr>
    <tr><td><b>Denary</b></td><td>10</td><td>0 to 9</td><td>1, 10, 100, 1000</td></tr>
    <tr><td><b>Binary</b></td><td>2</td><td>0 and 1</td><td>1, 2, 4, 8, 16, 32, 64, 128</td></tr>
    <tr><td><b>Hexadecimal</b></td><td>16</td><td>0 to 9 then A to F (A=10, B=11, C=12, D=13, E=14, F=15)</td><td>1, 16, 256, 4096</td></tr>
  </table></div>

  <h3>Binary to denary</h3>
  <p>Write the column values above the bits and add the values under each 1. For 10110110: 128 + 32 + 16 + 4 + 2 = <b>182</b>.</p>
  <h3>Denary to binary</h3>
  <p>Work down the column values, writing 1 if the value fits into what is left and subtracting it, otherwise 0. For 241: 128 fits (113 left), 64 fits (49), 32 fits (17), 16 fits (1), 8, 4 and 2 do not, 1 fits. That gives <b>11110001</b>. The Watch tab animates this.</p>
  <h3>Binary to hexadecimal and back</h3>
  <p>Split the binary number into groups of four bits from the right, then convert each group to one hex digit. 1111 0010 becomes F and 2, so 11110010 = <b>F2</b>. To go back, write each hex digit as four bits.</p>
  <h3>Denary to hexadecimal</h3>
  <p>Either convert to binary first and then group the bits, or divide by 16: 241 ÷ 16 = 15 remainder 1, so 241 = F1 (15 is F). For a number over 255 the binary route is safer: 558 = 0010 0010 1110 = <b>22E</b>.</p>
  <h3>Hexadecimal to denary</h3>
  <p>Multiply each digit by its column value and add. F0 = 15 × 16 + 0 = <b>240</b>. A04 = 10 × 256 + 0 × 16 + 4 = <b>2564</b>. C0F = 12 × 256 + 0 + 15 = <b>3087</b>.</p>
  <div class="tw"><table class="t">
    <tr><th>Denary</th><th>Binary (8 bits)</th><th>Hex</th><th>Check</th></tr>
    <tr><td>241</td><td>1111 0001</td><td>F1</td><td>15 × 16 + 1</td></tr>
    <tr><td>182</td><td>1011 0110</td><td>B6</td><td>11 × 16 + 6</td></tr>
    <tr><td>64</td><td>0100 0000</td><td>40</td><td>4 × 16</td></tr>
    <tr><td>255</td><td>1111 1111</td><td>FF</td><td>15 × 16 + 15</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>"Show your working" is worth a mark on its own in many conversions. Write the column values or the nibbles, even when you can see the answer. Give 12-bit answers all twelve bits when the question names 12 bits.</div>

  <h2>3 · Binary Coded Decimal (BCD)</h2>
  <p>In BCD each <b>denary digit</b> is stored as its own 4-bit group. The number is not converted to a single binary value.</p>
  <div class="tw"><table class="t">
    <tr><th>Denary</th><th>BCD</th><th>Plain binary</th></tr>
    <tr><td>964</td><td>1001 0110 0100</td><td>11 1100 0100</td></tr>
    <tr><td>87</td><td>1000 0111</td><td>101 0111</td></tr>
    <tr><td>27</td><td>0010 0111</td><td>1 1011</td></tr>
  </table></div>
  <ul>
    <li><b>Encoding:</b> take each digit, write it as four bits, and keep the digits in the same order. 964 is 9 (1001), 6 (0110), 4 (0100).</li>
    <li><b>Decoding:</b> split into groups of four from the left or right and read each group as a digit. 1000 0110 0101 = 8, 6, 5 = <b>865</b>.</li>
    <li><b>Only 0000 to 1001 are valid.</b> The patterns 1010 to 1111 are never a BCD digit, so a nibble such as 1100 means the value is not BCD.</li>
    <li><b>Same bits, different value:</b> 0010 0111 is 39 as an unsigned binary integer but 27 as BCD. The question tells you which to use.</li>
    <li><b>Cost:</b> BCD uses more bits than plain binary for the same value (4 bits per digit), so it wastes some storage and arithmetic is more awkward.</li>
  </ul>

  <h2>4 · Where BCD and hexadecimal are used</h2>
  <div class="tw"><table class="t">
    <tr><th>Used for</th><th>Why that representation</th></tr>
    <tr><td><b>BCD</b> · financial and banking calculations</td><td>Money uses decimal digits and exactly two decimal places. Many decimal fractions cannot be stored exactly in plain binary, so rounding errors build up. BCD keeps each digit exact.</td></tr>
    <tr><td><b>BCD</b> · calculators, digital clocks, seven-segment displays</td><td>A display shows one digit at a time, so each digit is already in its own group and conversion to the display is simple.</td></tr>
    <tr><td><b>BCD</b> · date and time in the PC's BIOS clock</td><td>Hours, minutes and days are read and shown as separate decimal digits, so conversion with denary is easier.</td></tr>
    <tr><td><b>BCD</b> · barcode systems</td><td>Each digit of a code is separate, and denary-to-BCD conversion is accurate and quick.</td></tr>
    <tr><td><b>Hex</b> · colour codes such as #FC238A</td><td>Three pairs of hex digits give the red, green and blue values (0 to 255), which is far shorter than 24 binary digits.</td></tr>
    <tr><td><b>Hex</b> · memory addresses, machine code and memory dumps</td><td>One hex digit is four bits, so addresses are short and easy to read and copy without mistakes.</td></tr>
    <tr><td><b>Hex</b> · MAC addresses, IPv6 addresses, error codes</td><td>Long binary values are shown in a compact form that a person can check.</td></tr>
  </table></div>
  <p>Hexadecimal does <b>not</b> make the computer work faster or take less memory: the computer still stores binary. It is for people, because it is shorter, easier to read and has fewer transcription errors than a long string of 1s and 0s.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Treating BCD as plain binary: converting 87 to 1010111 instead of 1000 0111.</li>
    <li>Mixing prefixes: using 1000 for a kibibyte or 1024 for a megabyte.</li>
    <li>Reading hex letters as ordinary numbers, for example taking F as 6 instead of 15.</li>
    <li>Dropping leading zeros in a BCD or fixed-width answer, so the groups no longer line up.</li>
    <li>Justifying BCD with "it is faster". The accepted reasons are exact decimal digits, no accumulating errors, and easy conversion to a display.</li>
  </ul>
'''

watch = '''
  <h2>1 · Denary to binary: 241</h2>
  <p>Press Play, or click the numbered steps. Each column asks whether its value fits into what is left.</p>
  <div id="stA"></div>
  <h2>2 · Binary to hexadecimal: 11110010</h2>
  <div id="stB"></div>
  <h2>3 · Denary to BCD: 964</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · How big is the prefix gap?</h2>
  <p>Choose a unit. The decimal and binary versions start to drift apart as the units grow, which is why a drive sold as 1 TB shows fewer gibibytes.</p>
  <div class="card"><div class="grid2"><div><div id="pB" class="btnrow"></div>
    <div class="readout"><div><small>Decimal prefix (bytes)</small><strong id="p1"></strong></div><div><small>Binary prefix (bytes)</small><strong id="p2"></strong></div><div><small>Binary is larger by</small><strong id="p3"></strong></div></div>
    <div class="verdict" id="pv"></div></div>
    <div><svg id="pS" viewBox="0 0 420 200" role="img" aria-label="Bars comparing a decimal prefix and a binary prefix"></svg></div></div></div>

  <h2>Lab 2 · Toggle the bits</h2>
  <p>Click a bit to flip it. See the same value as denary, hexadecimal, and (if each nibble is 0 to 9) as BCD.</p>
  <div class="card"><div id="tg" class="btnrow"></div>
    <div class="readout"><div><small>Unsigned denary</small><strong id="t1"></strong></div><div><small>Hexadecimal</small><strong id="t2"></strong></div><div><small>Read as BCD</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div>
    <svg id="tS" viewBox="0 0 760 130" role="img" aria-label="Eight bits with their column values"></svg></div>

  <h2>Lab 3 · Mix a colour in hex</h2>
  <p>A colour code is three hex pairs: red, green, blue. Each pair is a byte from 0 to 255.</p>
  <div class="card"><div class="grid2"><div><div id="cr"></div><div id="cg"></div><div id="cb"></div>
    <div class="readout"><div><small>Colour code</small><strong id="k1"></strong></div><div><small>Red, green, blue (denary)</small><strong id="k2"></strong></div></div></div>
    <div><svg id="kS" viewBox="0 0 420 200" role="img" aria-label="Colour swatch"></svg></div></div></div>

  <h2>Lab 4 · BCD or plain binary: how many bits?</h2>
  <p>Drag to choose a denary number. BCD needs four bits for every digit; plain binary needs only as many bits as the value requires.</p>
  <div class="card"><div class="grid2"><div><div id="bs"></div>
    <div class="readout"><div><small>BCD</small><strong id="b1"></strong></div><div><small>BCD bits</small><strong id="b2"></strong></div><div><small>Plain binary bits</small><strong id="b3"></strong></div></div>
    <div class="verdict" id="bv"></div></div>
    <div><svg id="bS" viewBox="0 0 420 200" role="img" aria-label="Bars comparing bits needed"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Binary prefix or decimal prefix?</h2><div id="cl1" class="card"></div>
  <h2>2 · BCD or hexadecimal?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for denary to hexadecimal in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The missing gigabytes", "A 1 TB drive holds 1 000 000 000 000 bytes. A computer that reports sizes in binary units divides by 2<sup>40</sup> and shows about 0.91 TiB, or roughly 931 GiB. Nothing is missing: the two sides use different prefixes.", "a 'why does the drive show less space' question: decimal prefix on the label, binary prefix in the reporting.") +
rw("Web colours", "A colour such as #FC238A is red FC (252), green 23 (35) and blue 8A (138). Three bytes give 16.7 million colours, and the six hex digits are much easier to type and compare than twenty-four bits.", "hex questions set in a graphics context: convert each pair separately.") +
rw("Network addresses", "A MAC address is 48 bits shown as twelve hex digits, such as 3C:22:FB:7A:10:E5. IPv6 addresses use hex too. Engineers read and copy them far more reliably than binary.", "justify hex: shorter, four bits per digit, fewer transcription errors.") +
rw("Why the till does not use plain binary for pence", "Decimal fractions such as 0.10 cannot be stored exactly in plain binary, so repeated additions drift. Financial software uses decimal digit encodings such as BCD so each penny is held exactly.", "BCD application and justification: exact decimal digits, no accumulating rounding error.") +
rw("Seven-segment displays", "A digital clock or calculator shows one digit at a time. Holding each digit in its own four bits means the display circuit can decode the digit directly, with no division by ten needed.", "second BCD justification: easier conversion between stored value and the display.")
)

items = [("s24_13", "1(a)", 4), ("s23_11", "3(d)(i)", 1), ("s26_11", "1(d)", 2), ("s23_11", "3(d)(ii)-(iii)", 2), ("w23_12", "3(b)(ii)-(iii)", 2), ("w23_12", "3(c)", 2),
         ("s25_12", "2(a)", 2), ("s26_11", "1(a)(i)", 4), ("w21_11", "1(c)", 1), ("w22_11", "1(a)(i)-(ii)", 2), ("s22_13", "1(b)", 5)]

exam = aexam("binary prefixes, number bases, BCD and hexadecimal",
  "Eleven questions from the 2021 to 2026 Paper 1 papers. Conversions are worth a mark for working and a mark for the answer, so show the groups or column values. The figures here are changed from the originals, so the answers are our own.",
  items, [
  ceq(AP("s24_13", "1(a)"), "[4]", "Complete the description. A kibibyte has a ........ prefix. Five kibibytes is the same as ........ bytes. A gigabyte has a ........ prefix. Three terabytes is the same as ........ gigabytes.",
      ["One mark for each blank: binary, 5120, denary (decimal), 3000."],
      "<p>Kibi is the binary family (steps of 1024) and giga is the decimal family (steps of 1000). Multiply within one family only: 5 × 1024, then 3 × 1000.</p>",
      [[("k", "A kibibyte has a binary prefix. Five kibibytes is the same as 5 × 1024 = 5120 bytes. A gigabyte has a decimal prefix. Three terabytes is the same as 3 × 1000 = 3000 gigabytes.")]]) +
  ceq(AP("s23_11", "3(d)(i)"), "[1]", "State the difference between a kibibyte and a kilobyte.",
      ["Kibibyte is 1024 bytes and kilobyte is 1000 bytes, or kibibyte is a binary prefix and kilobyte a denary prefix."],
      "<p>Give both sides in one sentence.</p>",
      [[("k", "A kibibyte is 1024 bytes whereas a kilobyte is 1000 bytes.")]]) +
  ceq(AP("s26_11", "1(d)"), "[2]", "Identify two differences between binary prefixes and decimal prefixes.",
      ["Binary prefixes are based on powers of 2 and decimal prefixes on powers of 10.", "A matching pair of values, such as a kibibyte is 1024 bytes and a kilobyte is 1000 bytes. The two values must come from the matching pair."],
      "<p>One structural difference, one worked example. Compare mebibyte with megabyte or kibibyte with kilobyte, not kibibyte with megabyte.</p>",
      [[("k", "Binary prefixes step up in powers of 2 (1024) whereas decimal prefixes step up in powers of 10 (1000). A mebibyte is 1 048 576 bytes whereas a megabyte is 1 000 000 bytes.")]]) +
  ceq(AP("s23_11", "3(d)(ii)-(iii)"), "[2]", "(i) Convert the denary number 735 into Binary Coded Decimal (BCD). (ii) Convert the positive binary integer 10110110 into hexadecimal.",
      ["BCD: 0111 0011 0101 (one group of four for each digit).", "Hexadecimal: B6 (1011 is B, 0110 is 6)."],
      "<p>BCD works digit by digit: 7, 3, 5. Hex works nibble by nibble from the right.</p>",
      [[("k", "735: 7 = 0111, 3 = 0011, 5 = 0101, so BCD is 0111 0011 0101. 10110110: 1011 = B and 0110 = 6, so the hexadecimal is B6.")]]) +
  ceq(AP("w23_12", "3(b)(ii)-(iii)"), "[2]", "(i) Convert the Binary Coded Decimal (BCD) value 1001 0111 0001 into denary. (ii) Convert the unsigned binary integer 000110111001 into denary.",
      ["971, from 9, 7 and 1.", "441: 256 + 128 + 32 + 16 + 8 + 1, or hex 1B9 = 256 + 176 + 9."],
      "<p>Same kind of bit pattern, two different rules. Group by four for BCD; use column values for unsigned binary.</p>",
      [[("k", "BCD: 1001 = 9, 0111 = 7, 0001 = 1, so the denary value is 971. Unsigned binary: 256 + 128 + 32 + 16 + 8 + 1 = 441.")]]) +
  ceq(AP("w23_12", "3(c)"), "[2]", "Identify one practical application of BCD and justify why BCD is used in this application.",
      ["One mark for a valid application: financial or banking calculations, electronic displays such as calculators and clocks, BIOS date and time storage, barcode systems.", "One mark for the matching reason. For money: exact decimal digits, two decimal places, no accumulating rounding errors. For displays: each digit is shown separately, and conversion with denary is easier."],
      "<p>The reason must match the application chosen. 'It is more accurate' alone is too vague.</p>",
      [[("k", "Application: a calculator display. "), ("a", "Justification: the display shows one digit at a time, and each denary digit is already stored in its own four bits, so converting the stored value to the display is straightforward.")]]) +
  ceq(AP("s25_12", "2(a)"), "[2]", "Convert the denary integer 934 into 12-bit binary and into hexadecimal.",
      ["Binary: 0011 1010 0110.", "Hexadecimal: 3A6."],
      "<p>Build the 12-bit binary first, then read it in groups of four: 0011 = 3, 1010 = A, 0110 = 6. 934 = 512 + 256 + 128 + 32 + 4 + 2.</p>",
      [[("k", "Binary 0011 1010 0110 (512 + 256 + 128 + 32 + 4 + 2 = 934). Hexadecimal: 0011 = 3, 1010 = A, 0110 = 6, so 3A6.")]]) +
  ceq(AP("s26_11", "1(a)(i)"), "[4]", "Complete the table for three Unicode characters: (1) denary 300, give binary and hexadecimal; (2) hexadecimal 2B9, give denary and binary; (3) binary 0001 1111 0100, give hexadecimal and denary; (4) state the largest denary value that three hexadecimal digits can hold.",
      ["300 = 0001 0010 1100 = 12C.", "2B9 = 697 = 0010 1011 1001.", "0001 1111 0100 = 1F4 = 500.", "FFF = 4095."],
      "<p>Each row is one conversion done in two directions. For (4) the largest three-digit hex value is FFF: 15 × 256 + 15 × 16 + 15 = 4095.</p>",
      [[("k", "300 = 256 + 32 + 8 + 4, so binary 0001 0010 1100 and hexadecimal 12C. 2B9 = 2 × 256 + 11 × 16 + 9 = 697 and binary 0010 1011 1001. 0001 1111 0100 = 1F4 = 256 + 240 + 4 = 500. FFF = 4095.")]]) +
  ceq(AP("w21_11", "1(c)"), "[1]", "Convert the hexadecimal value B7 into denary.",
      ["183."],
      "<p>B is 11: 11 × 16 + 7.</p>",
      [[("k", "B7 = 11 × 16 + 7 = 176 + 7 = 183.")]]) +
  ceq(AP("w22_11", "1(a)(i)-(ii)"), "[2]", "The 8-bit pattern 0101 0011 is stored in a register. (i) Convert it into denary as an unsigned binary integer. (ii) Convert it into denary as a BCD value.",
      ["Unsigned binary: 83 (64 + 16 + 2 + 1).", "BCD: 53 (0101 = 5, 0011 = 3)."],
      "<p>The same bits give two answers. Check which rule the question names before you convert.</p>",
      [[("k", "As unsigned binary: 64 + 16 + 2 + 1 = 83. As BCD: 0101 is 5 and 0011 is 3, so the value is 53.")]]) +
  ceq(AP("s22_13", "1(b)"), "[5]", "State each value. (i) Hexadecimal 2C in denary. (ii) The largest denary number an unsigned 8-bit binary integer can hold. (iii) Denary 59 in BCD. (iv) Denary 200 in hexadecimal. (v) Denary 19 as an 8-bit binary integer.",
      ["44.", "255.", "0101 1001.", "C8.", "0001 0011."],
      "<p>Five quick conversions, one mark each: 2 × 16 + 12; all eight bits set; digits 5 and 9; 200 = 12 × 16 + 8; 16 + 2 + 1.</p>",
      [[("k", "2C = 32 + 12 = 44. Largest unsigned 8-bit is 255. 59 in BCD is 0101 1001. 200 = 12 × 16 + 8, so C8. 19 = 16 + 2 + 1 = 0001 0011.")]])
])

tips = tips_html([
  ("Show the groups.", "Write the column values or the nibbles beside the answer. Working earns a mark even when the answer slips."),
  ("Match the prefix family.", "Compare kibi with kilo, mebi with mega, gibi with giga and tebi with tera. Never mix 1000 and 1024 in one step."),
  ("Check which rule the question names.", "The same eight bits can be unsigned binary, BCD or two's complement. Each gives a different denary value."),
  ("Use the full width.", "A 12-bit answer needs twelve bits with leading zeros; a BCD answer needs a full nibble for every digit."),
  ("Justify, do not just name.", "For BCD or hex, write the use and then the reason: 'financial calculations, because decimal digits are stored exactly'."),
  ("Hex is for people.", "The computer stores binary. Hex is shorter and easier to read and copy, with fewer errors."),
], [
  ("a difference between binary and decimal prefixes", "Binary prefixes such as kibi are based on powers of 2 (1024) whereas decimal prefixes such as kilo are based on powers of 10 (1000)."),
  ("why hex is used", "One hex digit represents four bits, so a long binary value is shown in a shorter form that is easier to read and less likely to be copied wrongly."),
  ("why BCD suits money", "Each denary digit is stored exactly, so there are no rounding errors from converting decimal fractions to binary."),
  ("an invalid BCD value", "The pattern 1100 is not valid BCD because a BCD digit can only be 0000 to 1001."),
], [("State / Give", "One fact or value. No reasoning needed."), ("Convert", "Change the value to the base asked for, showing the groups or column values."), ("Identify", "Pick the correct term, application or value."), ("Justify", "Give a reason that fits the example you chose."), ("Describe", "Say what it is made of or how it works.")]) + FC

js = AKJS + r'''
function bitsSteps(el, n, label) {
  const pv = [128, 64, 32, 16, 8, 4, 2, 1]; let rem = n; const rows = pv.map((p) => { const b = rem >= p ? 1 : 0, before = rem; rem -= b * p; return { p, b, before, after: rem }; });
  const draw = (s) => {
    let o = SV.text(380, 28, n + " in denary", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    rows.forEach((r, i) => {
      const x = 60 + i * 80, v = clamp01(s.k - i);
      o += SV.text(x + 34, 66, r.p, "sm", { "text-anchor": "middle" });
      if (v > 0) {
        o += boxRow([{ t: r.b, c: r.b ? "f2" : "f3", v }], x, 76, 68, 52, 0);
        o += SV.text(x + 34, 152, r.b ? "fits" : "no", "sm", { "text-anchor": "middle", ...op(v) }) + SV.text(x + 34, 172, "left " + r.after, "sm", { "text-anchor": "middle", ...op(v) });
      } else o += boxRow([{ t: "", v: 1 }], x, 76, 68, 52, 0);
    });
    const done = clamp01(s.k - 7.5);
    if (done > 0) o += SV.text(380, 214, bin(n), "lbl bd t3", { "text-anchor": "middle", style: "font-size:26px;font-family:var(--mono)", ...op(done) }) + SV.text(380, 240, "= " + n + " in binary", "sm", { "text-anchor": "middle", ...op(done) });
    return o;
  };
  const steps = [{ cap: "Write the column values 128, 64, 32 ... 1 above eight empty bits. Work from the left. For each column ask: does this value fit into what is left of " + n + "?", s: { k: 0 } }];
  rows.forEach((r, i) => steps.push({ cap: `<b>${r.p}:</b> ${r.b ? `${r.before} is at least ${r.p}, so write <b>1</b> and subtract. ${r.after} left.` : `${r.before} is less than ${r.p}, so write <b>0</b>. Still ${r.after} left.`}`, s: { k: i + 1 } }));
  steps.push({ cap: `Read the bits: <b>${bin(n)}</b>. Check by adding the columns with a 1: ${rows.filter((r) => r.b).map((r) => r.p).join(" + ")} = ${n}.`, s: { k: 8 } });
  Lib.stepper($(el), { w: 760, h: 256, label, base: { k: 0 }, draw, tween: 600, dwell: 3600, steps });
}
bitsSteps("#stA", 241, "Converting 241 to binary one column at a time");

(function () {
  const v = "11110010", hi = "1111", lo = "0010";
  const draw = (s) => {
    const items = v.split("").map((t, i) => ({ t, c: i < 4 ? "f1" : "f2", top: [128, 64, 32, 16, 8, 4, 2, 1][i] }));
    let o = boxRow(items, 60 + 0, 50, 64, 52, 16);
    const g = clamp01(s.g);
    o += SV.line(60, 124, 60 + 4 * 80 - 16, 124, "c1", { "stroke-width": 3, ...op(g) }) + SV.line(60 + 4 * 80, 124, 60 + 8 * 80 - 16, 124, "c2", { "stroke-width": 3, ...op(g) });
    o += SV.text(60 + 2 * 80 - 8, 146, "1111", "lbl bd t1", { "text-anchor": "middle", style: "font-family:var(--mono)", ...op(g) }) + SV.text(60 + 6 * 80 - 8, 146, "0010", "lbl bd t2", { "text-anchor": "middle", style: "font-family:var(--mono)", ...op(g) });
    o += SV.text(60 + 2 * 80 - 8, 176, "8+4+2+1 = 15", "sm", { "text-anchor": "middle", ...op(clamp01(s.h)) }) + SV.text(60 + 6 * 80 - 8, 176, "2", "sm", { "text-anchor": "middle", ...op(clamp01(s.h)) });
    o += boxRow([{ t: "F", c: "f1", v: clamp01(s.f1) }], 60 + 2 * 80 - 40, 190, 64, 52, 0, { fs: 26 }) + boxRow([{ t: "2", c: "f2", v: clamp01(s.f2) }], 60 + 6 * 80 - 40, 190, 64, 52, 0, { fs: 26 });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 262, label: "Converting 11110010 to hexadecimal", base: { g: 0, h: 0, f1: 0, f2: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "Start with the 8-bit value <b>11110010</b>. One hex digit stands for exactly four bits, so two hex digits will do.", s: {} },
    { cap: "Split into groups of four bits from the right: <b>1111</b> and <b>0010</b>. If the length is not a multiple of four, add leading zeros on the left.", s: { g: 1 } },
    { cap: "Work out each group. 1111 is 8 + 4 + 2 + 1 = <b>15</b>, which is the hex digit <b>F</b>. 0010 is <b>2</b>.", s: { g: 1, h: 1, f1: 1, f2: 1 } },
    { cap: "Write the digits in order: <b>F2</b>. To go back, write each hex digit as four bits again.", s: { g: 1, h: 1, f1: 1, f2: 1 } }] });
})();

(function () {
  const digs = [9, 6, 4];
  const draw = (s) => {
    let o = "";
    digs.forEach((d, i) => {
      const x = 90 + i * 200, a = clamp01(s.k - i * 1);
      o += boxRow([{ t: d, c: "f1", v: clamp01(s.d) }], x + 51, 36, 70, 52, 0, { fs: 28 });
      if (a > 0) {
        o += SV.line(x + 86, 94, x + 86, 120, "dash", op(a));
        o += boxRow(bin(d, 4).split("").map((t) => ({ t, c: "f2", v: a })), x, 126, 40, 46, 4, { fs: 20 });
      }
    });
    const f = clamp01(s.f);
    if (f > 0) o += SV.text(380, 226, "1001 0110 0100", "lbl bd t3", { "text-anchor": "middle", style: "font-size:26px;font-family:var(--mono)", ...op(f) });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Converting 964 into BCD", base: { d: 0, k: 0, f: 0 }, draw, tween: 600, dwell: 4200, steps: [
    { cap: "BCD treats each denary digit separately. 964 has three digits: <b>9</b>, <b>6</b> and <b>4</b>.", s: { d: 1 } },
    { cap: "Convert the first digit, 9, into four bits: 8 + 1 = <b>1001</b>.", s: { d: 1, k: 1 } },
    { cap: "Next digit, 6: 4 + 2 = <b>0110</b>. Always use all four bits, with leading zeros.", s: { d: 1, k: 2 } },
    { cap: "Last digit, 4: <b>0100</b>.", s: { d: 1, k: 3 } },
    { cap: "Join the groups in order: <b>1001 0110 0100</b>. Plain binary for 964 is 1111000100, so BCD needs 12 bits against 10 and the groups are different.", s: { d: 1, k: 3, f: 1 } }] });
})();

/* Lab 1 */
(function () {
  const rows = [["kilo and kibi", 1, "kB", "KiB"], ["mega and mebi", 2, "MB", "MiB"], ["giga and gibi", 3, "GB", "GiB"], ["tera and tebi", 4, "TB", "TiB"]];
  const show = (i) => {
    const r = rows[i], dec = 10 ** (3 * r[1]), b = 2 ** (10 * r[1]), gap = (b / dec - 1) * 100;
    $$("#pB button").forEach((x, k) => x.classList.toggle("pri", k === i));
    $("#p1").textContent = dec.toLocaleString("en-GB"); $("#p2").textContent = b.toLocaleString("en-GB"); $("#p3").textContent = Lib.fmtN(gap, 1) + "%";
    $("#pv").textContent = r[1] === 4 ? "A drive sold as 1 TB holds 10^12 bytes, which is only " + Lib.fmtN(dec / b, 3) + " TiB, about " + Lib.fmtN(dec / 2 ** 30, 0) + " GiB." : "1 " + r[3] + " = " + b.toLocaleString("en-GB") + " bytes, 1 " + r[2] + " = " + dec.toLocaleString("en-GB") + " bytes.";
    const w = 320, wb = w * (b / dec) / 1.11;
    $("#pS").innerHTML = SV.text(30, 40, "1 " + r[2] + " (decimal)", "lbl bd") + SV.rect(30, 50, w / 1.11, 28, "f3", { rx: 6, ...op(0.7) }) + SV.text(30, 112, "1 " + r[3] + " (binary)", "lbl bd") + SV.rect(30, 122, wb, 28, "f1", { rx: 6, ...op(0.7) }) + SV.text(30, 178, "Binary is " + Lib.fmtN(gap, 1) + "% larger", "sm");
  };
  $("#pB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#pB button").forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
})();

/* Lab 2 */
(function () {
  let bits = [1, 1, 1, 1, 0, 0, 1, 0];
  const pv = [128, 64, 32, 16, 8, 4, 2, 1];
  const paint = () => {
    const n = bits.reduce((a, b, i) => a + b * pv[i], 0), s = bits.join("");
    $("#t1").textContent = n; $("#t2").textContent = hx(n);
    const hi = parseInt(s.slice(0, 4), 2), lo = parseInt(s.slice(4), 2), ok = hi <= 9 && lo <= 9;
    $("#t3").textContent = ok ? "" + hi + lo : "not BCD";
    $("#tv").textContent = ok ? `As BCD the nibbles ${s.slice(0, 4)} and ${s.slice(4)} are the digits ${hi} and ${lo}, so BCD gives ${hi}${lo} but unsigned binary gives ${n}.` : `A nibble above 1001 (${hi > 9 ? s.slice(0, 4) : s.slice(4)}) is not a valid BCD digit, so this pattern cannot be BCD.`;
    $$("#tg button").forEach((b, i) => { b.textContent = bits[i]; b.classList.toggle("pri", !!bits[i]); });
    $("#tS").innerHTML = boxRow(bits.map((t, i) => ({ t, c: t ? "f2" : "f3", top: pv[i] })), 60, 24, 64, 48, 16) + SV.text(60 + 2 * 80 - 8, 108, hx(hi, 1), "lbl bd t1", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(60 + 6 * 80 - 8, 108, hx(lo, 1), "lbl bd t2", { "text-anchor": "middle", style: "font-size:20px" });
  };
  $("#tg").innerHTML = bits.map((b, i) => `<button class="b" data-i="${i}" aria-label="Bit ${pv[i]}"></button>`).join("");
  $$("#tg button").forEach((b) => (b.onclick = () => { bits[+b.dataset.i] ^= 1; paint(); })); paint();
})();

/* Lab 3 */
(function () {
  const v = { r: 252, g: 35, b: 138 };
  const paint = () => {
    $("#k1").textContent = "#" + hx(v.r) + hx(v.g) + hx(v.b); $("#k2").textContent = `${v.r}, ${v.g}, ${v.b}`;
    $("#kS").innerHTML = SV.rect(30, 20, 360, 110, "f3", { rx: 12, style: `fill:rgb(${v.r},${v.g},${v.b});opacity:1` }) + SV.text(210, 160, "R " + hx(v.r) + " = " + bin(v.r), "sm", { "text-anchor": "middle" }) + SV.text(210, 180, "G " + hx(v.g) + " = " + bin(v.g) + "   B " + hx(v.b) + " = " + bin(v.b), "sm", { "text-anchor": "middle" });
  };
  [["cr", "Red", "r"], ["cg", "Green", "g"], ["cb", "Blue", "b"]].forEach(([id, l, k]) => Lib.slider($("#" + id), { id: "s" + id, label: l + " ", min: 0, max: 255, value: v[k], fmt: (x) => x + " (" + hx(x) + ")", onInput: (x) => { v[k] = x; paint(); } }));
  paint();
})();

/* Lab 4 */
(function () {
  Lib.slider($("#bs"), { id: "bsl", label: "Denary number ", min: 0, max: 9999, value: 964, fmt: (x) => x, onInput: (n) => {
    const d = String(n).split(""), bcd = d.map((x) => bin(+x, 4)).join(" "), bb = Math.max(1, n.toString(2).length), cb = d.length * 4;
    $("#b1").textContent = bcd; $("#b2").textContent = cb; $("#b3").textContent = bb;
    $("#bv").textContent = cb > bb ? `BCD needs ${cb - bb} more bit${cb - bb === 1 ? "" : "s"} than plain binary here, but each digit stays separate.` : "Same number of bits here.";
    const mx = 40;
    $("#bS").innerHTML = SV.text(30, 40, "BCD: " + cb + " bits", "lbl bd") + SV.rect(30, 50, cb / mx * 360, 26, "f1", { rx: 6, ...op(0.7) }) + SV.text(30, 112, "Plain binary: " + bb + " bits", "lbl bd") + SV.rect(30, 122, bb / mx * 360, 26, "f2", { rx: 6, ...op(0.7) });
  } });
})();
''' + CLASSIFY("cl1", "Is each prefix binary or decimal?", ["Binary prefix", "Decimal prefix"],
  [("kibi", 0), ("kilo", 1), ("mebi", 0), ("mega", 1), ("gibi", 0), ("giga", 1), ("tebi", 0), ("tera", 1)], "Kibi, mebi, gibi and tebi are the binary prefixes; they are written with an 'i'.") + CLASSIFY("cl2", "Which representation suits each use?", ["BCD", "Hexadecimal"],
  [("A bank adds up pence", 0), ("A web page colour code", 1), ("A calculator shows digits", 0), ("A MAC address", 1), ("Date and time held in the BIOS clock", 0), ("A memory address in a debugger", 1), ("A digital clock display", 0), ("An error code on a screen", 1)],
  "BCD keeps each denary digit separate. Hexadecimal is a compact way of showing binary for people.") + ORDER(
  "Put the steps for converting denary 558 into hexadecimal in order.",
  ["Write 558 as binary using the column values", "Pad the binary to 12 bits: 0010 0010 1110", "Split into groups of four bits from the right", "Convert each group to a hex digit", "Write the digits in order: 22E"],
  "Binary first, group in fours, then convert each nibble.") + MATCH([
  ["Nibble", "Four bits"], ["Kibibyte", "1024 bytes"], ["Kilobyte", "1000 bytes"], ["BCD", "Each denary digit stored in its own four bits"], ["Hexadecimal", "Base 16, digits 0 to 9 and A to F"], ["Binary", "Base 2, digits 0 and 1"]]) + CALC([
  {"q": "Convert the binary number 11010110 into denary.", "a": 214, "unit": "", "tol": 0.01, "hint": "128 + 64 + 16 + 4 + 2.", "sol": "<b>214</b>."},
  {"q": "Convert the hexadecimal value 3F into denary.", "a": 63, "unit": "", "tol": 0.01, "hint": "3 × 16 + 15.", "sol": "<b>63</b>."},
  {"q": "How many bytes are there in 6 kibibytes?", "a": 6144, "unit": "bytes", "tol": 0.01, "hint": "6 × 1024.", "sol": "<b>6144</b> bytes."},
  {"q": "A drive is sold as 2 terabytes. How many gigabytes is that in decimal units?", "a": 2000, "unit": "GB", "tol": 0.01, "hint": "Terabyte is a decimal prefix: 1 TB = 1000 GB.", "sol": "<b>2000</b> GB."},
  {"q": "Convert denary 200 into hexadecimal.", "t": ["C8"], "unit": "", "hint": "200 = 12 × 16 + 8, and 12 is C.", "sol": "<b>C8</b>."},
  {"q": "How many bits are in 3 kibibytes?", "a": 24576, "unit": "bits", "tol": 0.01, "hint": "3 × 1024 × 8.", "sol": "<b>24576</b> bits."},
  {"q": "Write denary 48 in BCD (eight bits, no spaces).", "t": ["01001000"], "unit": "", "hint": "4 = 0100, 8 = 1000.", "sol": "<b>0100 1000</b>."},
  {"q": "The BCD value 0110 0010 is stored. What denary number is it?", "a": 62, "unit": "", "tol": 0.01, "hint": "0110 = 6 and 0010 = 2.", "sol": "<b>62</b>."}]) + MCQ([
  ("Which of these is a binary prefix?", ["kilo", "mebi", "giga", "tera"], 1, "Mebi is the binary prefix paired with mega."),
  ("How many bytes are in one kibibyte?", ["1000", "1024", "1 000 000", "1 048 576"], 1, "A kibibyte is 2^10 = 1024 bytes."),
  ("What is denary 59 in BCD?", ["0011 1011", "0101 1001", "1001 0101", "0101 1010"], 1, "Digits 5 and 9: 0101 and 1001."),
  ("Why do people use hexadecimal to show binary values?", ["The computer can only process hex", "It uses less memory in the computer", "One hex digit stands for four bits, so values are shorter and easier to read", "It runs programs faster"], 2, "Hex is a human-friendly shorthand; the computer still stores binary."),
  ("Which use best suits BCD?", ["A colour code on a web page", "A memory address in a debugger", "Financial calculations", "A MAC address"], 2, "BCD stores decimal digits exactly, so there are no rounding errors in money."),
  ("Which 4-bit pattern cannot be a BCD digit?", ["1001", "0111", "1010", "0000"], 2, "BCD digits run from 0000 (0) to 1001 (9).")], "qz1") + CARDS([
  ("Kibibyte", "1024 bytes. Binary prefix."), ("Kilobyte", "1000 bytes. Decimal prefix."), ("Pairs", "Kibi/kilo, mebi/mega, gibi/giga, tebi/tera."), ("Nibble", "Four bits. One hex digit."),
  ("Hexadecimal", "Base 16. Digits 0-9 and A-F. A = 10, F = 15."), ("BCD", "Each denary digit in its own four bits."), ("Valid BCD digits", "0000 to 1001 only."), ("BCD use", "Money, calculators, clocks, BIOS time, barcodes.")])

build("ac111", "ac-1-1-1-number-bases-bcd-hex", "Binary Prefixes, Number Bases, BCD and Hexadecimal", EYA("1.1.1"),
  "Binary and decimal prefixes, converting between binary, denary and hexadecimal, Binary Coded Decimal, where BCD and hex are used, and eleven questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.1 Data representation"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
