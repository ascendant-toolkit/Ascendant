"""A Level CS syllabus 13.3.2: normalisation, accuracy and range, overflow and underflow, rounding errors. Run: python3 tools/artifact-kit/mk_ac1332.py"""
from ak20 import *
from fpq import *
from fractions import Fraction as F


def rng_rows():
    rows = []
    for mb, eb in [(8, 8), (10, 6), (11, 5), (12, 4)]:
        ee = 2 ** (eb - 1)
        big = (1 - F(1, 2 ** (mb - 1))) * F(2) ** (ee - 1)
        rows.append(f"<tr><td>{mb} bits</td><td>{eb} bits</td><td>(1 − 2<sup>−{mb - 1}</sup>) × 2<sup>{ee - 1}</sup>{' = ' + fmt_frac(big) if big < 10 ** 7 else ''}</td><td>2<sup>−{ee + 1}</sup></td></tr>")
    return "".join(rows)


m1, e1, _ = encode(F(1, 10), 12, 4)
st01 = decode(m1, e1)
m2, e2, _ = encode(F(652, 10), 12, 4)
st652 = decode(m2, e2)

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A floating-point number is <b>normalised</b> when its mantissa starts <b>01</b> (positive) or <b>10</b> (negative), so there are no wasted leading bits; this gives the <b>most precision</b> for the bits available, a <b>single representation</b> for each number, and the widest range. To normalise, shift the mantissa left until the first two bits differ and subtract the number of shifts from the exponent. With a fixed total number of bits, more bits for the mantissa give more <b>precision</b> and fewer for the exponent give a smaller <b>range</b>, and the reverse. A result too large to store causes <b>overflow</b>, one too small (closer to zero than the smallest number) causes <b>underflow</b>. Many numbers, such as 0.1, cannot be stored exactly in binary, so the stored value is an approximation and <b>rounding errors</b> appear.</p></div>

  <h2>1 · Normalisation</h2>
  <p>In two's complement the first bit is the sign. A mantissa is <b>normalised</b> if its first <b>two bits are different</b>:</p>
  <div class="tw"><table class="t mono">
    <tr><th>Mantissa</th><th>Normalised?</th><th>Reason</th></tr>
    <tr><td>0111010000</td><td>Yes</td><td>starts 01: positive, 0.1...</td></tr>
    <tr><td>1000110000</td><td>Yes</td><td>starts 10: negative</td></tr>
    <tr><td>0001111000</td><td>No</td><td>starts 00: the leading zeros are wasted</td></tr>
    <tr><td>1110000000</td><td>No</td><td>starts 11: the leading ones are wasted</td></tr>
  </table></div>
  <p>A normalised positive mantissa has a value from 0.5 up to just below 1, and a normalised negative mantissa from −1 up to just below −0.5.</p>
  <h3>How to normalise</h3>
  <ol>
    <li><b>Shift the mantissa left</b> until its first two bits are different, adding zeros on the right.</li>
    <li>Each shift left makes the number twice as big, so <b>subtract 1 from the exponent</b> for every shift (to keep the same value).</li>
    <li>Write the new mantissa and exponent. Check: the value is unchanged.</li>
  </ol>
  <div class="tw"><table class="t mono">
    <tr><th>Step</th><th>Mantissa</th><th>Exponent</th></tr>
    <tr><td>Given (starts 00, not normalised)</td><td>0000000111</td><td>100111 (−25)</td></tr>
    <tr><td>Shift left 6 places: starts 01</td><td>0111000000</td><td>100111 − 6 = 100001 (−31)</td></tr>
  </table></div>
  <div class="tip"><b class="h">Why normalise?</b>(1) To store the <b>maximum range of numbers</b> in the minimum number of bits. (2) It minimises the number of <b>leading zeros or ones</b>, so the <b>most significant bits</b> are kept: the number has the greatest possible <b>precision</b>. (3) It avoids a number having <b>multiple representations</b>.</div>

  <h2>2 · Range and precision: how the bits are shared</h2>
  <p>The total number of bits is fixed (for example 16). Every bit given to the mantissa is taken from the exponent.</p>
  <div class="tw"><table class="t">
    <tr><th>Change</th><th>Effect on precision (accuracy)</th><th>Effect on range</th></tr>
    <tr><td><b>More bits for the mantissa</b>, fewer for the exponent</td><td>Increases: more significant digits can be stored</td><td>Decreases: the exponent is smaller, so the largest and smallest numbers are less extreme</td></tr>
    <tr><td><b>Fewer bits for the mantissa</b>, more for the exponent</td><td>Decreases</td><td>Increases: larger and smaller numbers can be stored</td></tr>
  </table></div>
  <p>The range and the accuracy trade off: when the range increases the accuracy decreases, and the other way round. For a mantissa of <i>m</i> bits and an exponent of <i>e</i> bits (normalised, two's complement), with <i>E</i> = 2<sup><i>e</i>−1</sup>:</p>
  <ul>
    <li><b>Largest positive:</b> mantissa 0111...1 and the largest exponent: (1 − 2<sup>−(<i>m</i>−1)</sup>) × 2<sup><i>E</i>−1</sup></li>
    <li><b>Smallest positive:</b> mantissa 0100...0 (0.5) and the most negative exponent: 0.5 × 2<sup>−<i>E</i></sup> = 2<sup>−<i>E</i>−1</sup></li>
    <li><b>Largest negative number (most negative):</b> mantissa 1000...0 (−1) with the largest exponent.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Mantissa</th><th>Exponent</th><th>Largest positive number</th><th>Smallest positive number</th></tr>
    ''' + rng_rows() + '''
  </table></div>
  <p>For 12 bits and 4 bits the largest positive number is 127.9375 (exponent 7). Giving 10 bits to the mantissa and 6 to the exponent <b>increases the range</b> (up to 2<sup>31</sup>) but <b>reduces the precision</b> of each number.</p>

  <h2>3 · Overflow and underflow</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Overflow</th><th>Underflow</th></tr>
    <tr><td>What happens</td><td>The result of a calculation is <b>too large</b> to be stored: the exponent needed is bigger than the system can hold</td><td>The result is <b>too small</b>: closer to zero than the smallest number the system can represent</td></tr>
    <tr><td>Example</td><td>Multiplying two very large numbers; adding 91.5 and 123.25 in a system whose largest value is 127.9375 (the answer, 214.75, needs an exponent of 8)</td><td>Dividing a very small number by a large one repeatedly</td></tr>
    <tr><td>Consequence</td><td>The most significant bits are lost, so the answer is wrong, or the program stops with an error</td><td>The result is stored as zero (or loses all accuracy), so later calculations are wrong</td></tr>
  </table></div>

  <h2>4 · Approximations and rounding errors</h2>
  <p>A binary fraction can only be built from halves, quarters, eighths and so on. A decimal fraction such as 0.1 or 0.2 is a <b>recurring</b> binary fraction (0.000110011...), and a finite mantissa has to cut it off, so the stored number is only the nearest value it can hold. The difference is a <b>rounding error</b>.</p>
  <div class="tw"><table class="t mono">
    <tr><th>Number</th><th>Stored in 12 + 4 bits</th><th>Error</th></tr>
    <tr><td>0.1</td><td>''' + fmt_frac(st01) + '''</td><td>−0.0000244...</td></tr>
    <tr><td>65.2</td><td>''' + fmt_frac(st652) + '''</td><td>−0.0125</td></tr>
    <tr><td>0.25</td><td>0.25</td><td>none: 1/4 is a power of two</td></tr>
  </table></div>
  <div class="code">''' + pc('''print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.2 == 0.3)       # False

print(abs((0.1 + 0.2) - 0.3) < 1e-9)   # True: compare with a tolerance, not ==''') + '''</div>
  <ul>
    <li>Rounding errors <b>build up</b> when many calculations are done on approximate numbers.</li>
    <li>More mantissa bits give a closer approximation but never remove the problem.</li>
    <li>Programs compare real numbers using a small tolerance, and store money as a whole number of pence.</li>
  </ul>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Calling a mantissa normalised because it starts with 0. It must start <b>01</b> or <b>10</b>.</li>
    <li>Changing the exponent in the wrong direction when normalising: each shift left <b>reduces</b> the exponent by 1.</li>
    <li>Saying more mantissa bits give a bigger range. They give more <b>precision</b>; more exponent bits give the bigger <b>range</b>.</li>
    <li>Mixing up overflow (too large) and underflow (too small, near zero).</li>
    <li>Explaining an approximation without saying why: the fractional part cannot be written exactly as a sum of powers of ½ in the available bits, so bits are lost or rounded.</li>
    <li>Not giving the <b>consequence</b> when asked: loss of precision, a wrong answer, or the value stored as zero.</li>
  </ul>
'''

watch = '''
  <h2>1 · Normalising a mantissa</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · Sharing 16 bits: precision against range</h2>
  <div id="stB"></div>
  <h2>3 · Overflow and underflow on the number line</h2>
  <div id="stC"></div>
  <h2>4 · Why 0.1 is only an approximation</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Normalise a floating-point number</h2>
  <p>Choose a number that is not normalised and press Shift left until it is. Watch the exponent drop by one each time.</p>
  <div class="card"><div id="nB" class="btnrow"></div><div id="nS"></div><div class="btnrow"><button class="b pri" id="nL">Shift mantissa left</button><button class="b" id="nR">Reset</button></div><div class="verdict" id="nV"></div></div>

  <h2>Lab 2 · Share 16 bits between mantissa and exponent</h2>
  <p>Move the slider. The mantissa takes the bits you give it; the exponent gets the rest. Watch what happens to the range and to the precision.</p>
  <div class="card"><div id="sS"></div><div class="readout"><div><small>Largest positive</small><strong id="s1" style="font-size:1rem"></strong></div><div><small>Smallest positive</small><strong id="s2" style="font-size:1rem"></strong></div><div><small>Gap near 1 (precision)</small><strong id="s3" style="font-size:1rem"></strong></div></div><div class="verdict" id="sV"></div></div>

  <h2>Lab 3 · What is actually stored?</h2>
  <p>Type a decimal number and choose the allocation of bits. The stored value and the error are shown.</p>
  <div class="card"><div id="rB" class="btnrow"></div><div class="btnrow" id="rE"></div><p><input id="rN" type="text" value="0.1" style="width:12em;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Number"> <button class="b pri" id="rR">Store it</button></p><div id="rO"></div><div class="verdict" id="rV"></div></div>
'''

practise = '''
  <h2>1 · Is the mantissa normalised?</h2><div id="cl1" class="card"></div>
  <h2>2 · More mantissa bits or more exponent bits?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for normalising in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Normalising and ranges</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Spreadsheet totals that are off by a tiny amount", "A sum of prices can show 0.30000000000000004 instead of 0.3. The computer holds 0.1 and 0.2 as approximations, so adding them gives an answer that is very slightly wrong.", "rounding errors come from binary approximations.") +
rw("A game physics engine", "If an object's speed is multiplied by 0.99 many times it may shrink until it is too small to store and becomes zero. That is underflow, and the object stops.", "underflow: a result closer to zero than the smallest number.") +
rw("A scientific simulation", "A model of a galaxy multiplies huge masses and distances. If the result is bigger than the largest number the format can hold, the program reports an overflow error or gives a wrong answer.", "overflow: a result too large to store.") +
rw("Choosing 32-bit or 64-bit floats", "A 64-bit float has more bits for both parts, giving far more precision and range than a 32-bit float, but uses twice the memory.", "the allocation of bits sets the precision and the range.") +
rw("Storing money", "Banks store pounds and pence as a whole number of pence, because 0.10 cannot be held exactly as a binary fraction and tiny errors would add up over millions of transactions.", "avoid floating point where exact values matter.")
)

where = [
  ("M/J 2021", "31, 32, 33", "1(c), 1(d)", "3 + 3 + 2", "Normalise a mantissa; explain why 513 cannot be stored; alter the storage"),
  ("O/N 2021", "31, 32", "1(a)(ii), 1(b)", "2 + 3", "Consequence of too few mantissa bits; why numbers are normalised"),
  ("O/N 2022", "31, 33", "1(c)", "1 + 2", "Why a number is not normalised; normalise it"),
  ("O/N 2022", "32", "1(a), 1(c)", "1 + 2", "Largest positive number; when underflow occurs"),
  ("M/J 2023", "31, 33", "1(b)", "2", "The problem representing 113.75 in the 8-bit mantissa system"),
  ("M/J 2023", "32", "1(b)", "3", "Why a normalised number cannot be represented accurately"),
  ("O/N 2023", "31, 33", "1(b)", "2", "The problem storing +65.20"),
  ("O/N 2023", "32", "1(b)", "3", "Why a binary representation is only an approximation"),
  ("M/J 2024", "32", "1(a)", "2", "The effect of changing the allocation of bits"),
  ("M/J 2025", "33", "2(a)", "2", "Largest normalised positive number and its denary value"),
  ("O/N 2025", "33", "2(a), 2(b)", "3 + 3", "Effect of a 10-bit mantissa; an example of overflow and its consequences"),
  ("M/J 2026", "32", "3(b)", "2", "An example of underflow and its consequences"),
  ("M/J 2026", "33", "5(b)", "3", "The problem adding 91.5 and 123.25 in the system")]

past = '''  <p class="note">Normalisation, accuracy, overflow, underflow and rounding errors are the second half of the floating-point questions in Paper 3, often as the second part of a conversion question. The conversions are on the previous page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Normalising and why</h3>
''' + peq(SRC("s21", "31, 32, 33", "Q1(c)"), "3 marks", "Normalise",
  "Real numbers are stored using 10 bits for the mantissa and 6 bits for the exponent, in two's complement. The given binary floating-point number is not normalised. Normalise it. Show your working. Mantissa 0000000111, exponent 100111." ,
  "Shift the mantissa left until it starts 01, and reduce the exponent by the number of shifts.",
  "<p>" + mks(["working: the mantissa is moved 6 places left (6 shifts) so the exponent is reduced by 6", "correct mantissa 0111000000", "correct exponent 100001"]) + "</p>" + qcode('''Mantissa 0000000111   starts 00: not normalised
Shift left 6 places:  0111000000   (starts 01)
Exponent 100111 = −25;  −25 − 6 = −31 = 100001

Mantissa  0111000000
Exponent  100001'''),
  "Adding 6 to the exponent. Shifting the mantissa left makes it look larger, so the exponent must be made smaller to keep the value.") + peq(SRC("w22", "31, 33", "Q1(c)"), "1 + 2 marks", "State / Normalise",
  "Real numbers use 8 bits for the mantissa and 8 bits for the exponent, in two's complement. A binary number is stored with mantissa 00011110 and exponent 00011000. (i) State why the number is not normalised. (ii) Write the normalised floating-point representation of the number.",
  "(i) look at the first two bits. (ii) shift and adjust the exponent.",
  "<p><b>(i)</b> " + mks(["The mantissa does not begin 01 or 10 (it begins 00): the first two digits are the same"]) + "</p><p><b>(ii)</b> " + mks(["correct mantissa 01111000", "correct exponent 00010110"], "a") + "</p>" + qcode('''00011110 → shift left 2 places → 01111000
Exponent 00011000 = 24;  24 − 2 = 22 = 00010110

Mantissa  01111000
Exponent  00010110'''), None) + peq(SRC("w21", "31, 32", "Q1(b)"), "3 marks", "Explain",
  "Explain the reason why binary numbers are stored in normalised form.",
  "Range in the fewest bits; leading zeros or ones; precision; one representation.",
  "<p>Any three: " + mks(["To store the maximum range of numbers in the minimum number of bytes / bits", "Normalisation minimises the number of leading zeros / ones represented", "so the number of significant bits is maximised, giving the greatest precision / accuracy for the given number of bits", "it enables very large or very small numbers to be stored with accuracy", "it avoids the possibility of many numbers having multiple representations"]) + "</p>", None) + '''
  <h3>Range, accuracy and the allocation of bits</h3>
''' + peq(SRC("s24", "32", "Q1(a)"), "2 marks", "Describe",
  "Describe the effect of changing the allocation of bits used for the mantissa and for the exponent in a floating-point number with a fixed total number of bits.",
  "Mantissa bits: precision. Exponent bits: range. And the trade-off.",
  "<p>Any two: " + mks(["More bits for the mantissa increase the precision / accuracy of the number; fewer reduce it", "Fewer bits for the exponent reduce the range of numbers that can be represented; more increase it", "When the range increases the accuracy decreases, and when the range decreases the accuracy increases"]) + "</p>",
  "Writing that more bits make the number 'bigger'. Say which part: the mantissa affects precision, the exponent affects range.") + peq(SRC("w25", "33", "Q2(a)"), "3 marks", "Outline",
  "Numbers are stored using 12 bits for the mantissa, 4 bits for the exponent, in two's complement, 2 bytes in total. Outline the effect of changing the number of bits used to store the mantissa to 10 bits in this system.",
  "The total stays 16, so the exponent gets 6.",
  "<p>" + mks(["The precision of the number stored in the mantissa is reduced", "the number of bits available for the exponent increases to 6", "so the range of numbers that can be stored increases"]) + "</p>", None) + peq(SRC("s21", "31, 32, 33", "Q1(d)"), "3 + 2 marks", "Explain / Describe",
  "Real numbers are stored with 10 bits for the mantissa, 6 for the exponent. The denary number 513 cannot be stored accurately as a normalised floating-point number in this system. (i) Explain the reason for this. (ii) Describe an alteration to the way floating-point numbers are stored to enable this number to be stored accurately using the same total number of bits.",
  "513 in binary is 1000000001 (10 digits): the positive mantissa needs 11 bits.",
  "<p><b>(i)</b> " + mks(["It requires 11 bits (more than 10) in the mantissa to store 513 accurately; the largest whole number a 10-bit mantissa can hold is 511", "513 in binary is 1000000001, which normalised is 0.1000000001 × 2<sup>10</sup>", "so the least significant digit is lost / the result is an overflow of the mantissa"]) + "</p><p><b>(ii)</b> " + mks(["The number of bits for the mantissa must be increased", "to 11 or 12 bits for the mantissa and 5 or 4 bits for the exponent"], "a") + "</p>", None) + peq(SRC("w22", "32", "Q1(a)"), "1 mark", "Write",
  "Normalised floating-point numbers are stored using two's complement for both the mantissa and the exponent, with 11 bits for the mantissa and 5 bits for the exponent. Write the largest positive two's complement binary number that can be stored in this system.",
  "A positive mantissa with every other bit 1, and the largest positive exponent.",
  "<p>" + mks(["mantissa 01111111111, exponent 01111"]) + "</p>" + qcode('''Mantissa  01111111111    (0.1111111111 = 1 − 2^-10)
Exponent  01111          (+15)'''), "Using 11111 for the exponent. A leading 1 would make it negative: the largest positive exponent is 01111.") + peq(SRC("s25", "33", "Q2(a)"), "2 marks", "Give",
  "Numbers are stored using 8 bits for the mantissa and 8 bits for the exponent, in two's complement. Give the largest normalised positive two's complement binary number that can be stored in this system and state its denary equivalent. The denary answer should be expressed in terms of powers of 2.",
  "Mantissa 01111111 and the largest exponent 01111111 (127).",
  "<p>" + mks(["Mantissa 01111111 and exponent 01111111", "Denary: (1 − 2<sup>−7</sup>) × 2<sup>127</sup> = 2<sup>127</sup> − 2<sup>120</sup>"]) + "</p>" + qcode('''Mantissa  01111111      = 0.1111111 = 1 - 2^-7
Exponent  01111111      = 127
Value = (1 - 2^-7) x 2^127  =  2^127 - 2^120'''), None) + '''
  <h3>Overflow, underflow and approximations</h3>
''' + peq(SRC("w22", "32", "Q1(c)"), "2 marks", "State",
  "State when underflow occurs in a binary floating-point system.",
  "A result too small, following an operation.",
  "<p>" + mks(["Following an arithmetic or logical operation", "the result is too small to be precisely represented in the available system (smaller than the smallest number that can be stored)"]) + "</p>", None) + peq(SRC("s26", "32", "Q3(b)"), "2 marks", "Describe",
  "Describe one example of a situation that could cause underflow to occur and the consequences of this underflow.",
  "A calculation on a normalised number, the result below the lowest value, and what is stored.",
  "<p>" + mks(["When a calculation is performed on a normalised floating-point number (any specific example is allowed)", "so that the result is less than the lowest possible value that can be stored, the exponent being too small for the number of bits, so the result becomes zero"]) + "</p>", None) + peq(SRC("w25", "33", "Q2(b)"), "3 marks", "Describe",
  "Describe one example of a situation that could cause an overflow to occur and the consequences of such an overflow.",
  "A calculation, a result out of range, and what is lost.",
  "<p>" + mks(["A process involving a calculation, such as multiplying two large numbers, could take place", "the result might be outside the range of values possible to store in the given system", "leading to the most significant bits of the mantissa or exponent being lost, which is an overflow"]) + "</p>", None) + peq(SRC("s26", "33", "Q5(b)"), "3 marks", "Explain",
  "Numbers are stored using 12 bits for the mantissa and 4 bits for the exponent, in two's complement. Explain the problem that would occur if the two binary floating-point numbers representing the denary numbers 91.5 and 123.25 were added together and the result stored in the given system.",
  "Add them, then compare with the largest number that can be stored.",
  "<p>Up to three: " + mks(["The sum would be 214.75", "which exceeds the largest number that can be stored in this system with an exponent of 7 (127.9375)", "an exponent of 8 would be required to increase the range beyond 128", "overflow would occur"]) + "</p>" + qcode('''91.5 + 123.25 = 214.75
Largest number with a 4-bit exponent:  (1 − 2^-11) × 2^7 = 127.9375
214.75 > 127.9375  →  OVERFLOW'''), None) + peq(SRC("s23", "31, 33", "Q1(b)"), "2 marks", "Explain",
  "System 1 uses 10 bits for the mantissa and 6 bits for the exponent. System 2 uses 8 bits for the mantissa and 8 for the exponent. 113.75 is stored in both. Explain the problem that occurred when representing the number in System 2.",
  "How many bits does the mantissa need?",
  "<p>" + mks(["The mantissa in System 2 does not have enough bits to store the whole binary number (10 bits are required, only 8 are available)", "so precision is lost / the number is truncated"]) + "</p>" + qcode('''113.75 = 0.111000111 × 2^7   needs 10 bits of mantissa
System 2 has 8: stored as 01110001 → 0.1110001 × 2^7 = 112.5'''), None) + peq(SRC("s23", "32", "Q1(b)"), "3 marks", "Describe",
  "Numbers are stored with 10 bits for the mantissa and 6 for the exponent. Describe the reason why the normalised form of the binary number 0101011.111001 cannot be represented accurately using this system.",
  "Count the digits in the normalised mantissa.",
  "<p>" + mks(["The mantissa of the number would need to be 0.101011111001 (13 bits)", "but it can only store 10 bits", "so the 3 least significant digits would be truncated, causing a loss of precision"]) + "</p>", None) + peq(SRC("w23", "31, 33", "Q1(b)"), "2 marks", "Explain",
  "Numbers are stored with 12 bits for the mantissa and 4 bits for the exponent. Explain the problem that will occur in storing the normalised floating-point representation of +65.20 in this system.",
  "Can 0.20 be written exactly as a sum of halves, quarters, eighths...?",
  "<p>" + mks(["The decimal fraction 0.20 cannot be represented exactly in binary (the closest values are 0.1875 and 0.25)", "so there will be a loss of precision due to a rounding error / truncation"]) + "</p>" + qcode('''65.2 = 1000001.001100110011...   (the fraction recurs)
12-bit mantissa keeps 1000001.0011  →  stored value 65.1875'''), None) + peq(SRC("w23", "32", "Q1(b)"), "3 marks", "Explain",
  "Explain why a binary representation is sometimes only an approximation to the real number it represents.",
  "Fractions, fixed length, powers of 2.",
  "<p>Any three: " + mks(["Real numbers can have a fractional part (such as 1/3 or 0.4)", "The fixed length of the storage means very large or very small numbers cannot be stored, and not every fraction can be stored with enough precision", "Binary represents numbers using powers of 2, so only fractions such as 1/2, 1/4, 1/8, 1/16 can be stored exactly", "The fractional part is stored as close as possible within the constraints (so it is an approximation)"]) + "</p>", None) + peq(SRC("w21", "31, 32", "Q1(a)(ii)"), "2 marks", "State",
  "Numbers are stored with 12 bits for the mantissa, 4 bits for the exponent. The unsigned binary number 1011100.011001 (13 binary digits) is stored in this system. State the consequence of storing it as a floating-point number in this system, and justify your answer.",
  "One mark for the consequence, one for why.",
  "<p>" + mks(["Consequence: the precision / accuracy of the number would be reduced", "Justification: the least significant bits of the original number have been truncated / lost, because the number needs 13 (or 14 with the sign) bits but the mantissa can only store 12"]) + "</p>", None)

review = req("3 marks", "Normalise", "A system has an 8-bit mantissa and a 6-bit exponent (two's complement). Normalise mantissa 00001100 with exponent 000101.", "Shift until it starts 01 and reduce the exponent by the number of shifts.",
  "<p>" + mks(["the mantissa starts 00, so it is not normalised", "shift 3 places left: 01100000", "exponent 5 − 3 = 2: 000010"]) + "</p>" + qcode('''00001100 → 3 shifts left → 01100000
Exponent 000101 = 5;  5 − 3 = 2 = 000010'''), "Increasing the exponent. Each left shift reduces it.") + req("2 marks", "State", "State two reasons why numbers are stored in normalised form.", "Think precision and range.",
  "<p>" + mks(["It gives the maximum precision for the number of bits, because there are no wasted leading zeros or ones.", "Each number has only one representation, and the range is maximised."]) + "</p>", None) + req("3 marks", "Explain", "A system uses 12 bits for the mantissa and 4 bits for the exponent. The designer changes it to 8 bits and 8 bits. Explain the effect on the range and on the accuracy of the numbers.", "Which part gets bigger?",
  "<p>" + mks(["The exponent has more bits, so the range of numbers that can be stored increases.", "The mantissa has fewer bits, so fewer significant digits are stored: the accuracy / precision decreases.", "Larger and smaller numbers can be represented but each is less precise."]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between overflow and underflow.", "Too large against too small.",
  "<p>" + mks(["Overflow: the result of a calculation is too large to be stored in the number of bits available.", "Underflow: the result is too small, closer to zero than the smallest number that can be stored."]) + "</p>", None) + req("3 marks", "Explain", "Explain why the result of adding 0.1 ten times in a program may not be exactly 1.", "0.1 in binary.",
  "<p>" + mks(["0.1 cannot be stored exactly in binary: it is a recurring binary fraction.", "The stored value is an approximation with a small rounding error.", "Adding it ten times adds the error ten times, so the total is slightly different from 1."]) + "</p>", None) + req("2 marks", "Calculate", "Using 12 bits for the mantissa and 4 for the exponent, the largest positive number is (1 − 2<sup>−11</sup>) × 2<sup>7</sup>. Write the mantissa and exponent for it.", "The largest positive mantissa has a 0 sign bit then all 1s.",
  "<p>" + mks(["mantissa 011111111111", "exponent 0111"]) + "</p>", None)

exam = exam20("Part 1 is the real 9618 questions on normalisation, range and precision, overflow, underflow and approximations (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Normalised means 01 or 10.", "If the first two bits match, shift left and lower the exponent for each shift."),
  ("Mantissa bits: precision. Exponent bits: range.", "A fixed total means gaining one costs the other."),
  ("Give the cause and the consequence.", "Overflow: too large, bits lost. Underflow: too small, stored as zero. Approximation: lost bits, rounding error."),
  ("Say why 0.1 is an approximation.", "It is not a sum of powers of ½, so it recurs in binary and has to be cut off."),
  ("Use numbers from the question.", "'The mantissa needs 13 bits but only 10 are available, so the last 3 are lost.'"),
  ("Quote the limit.", "In 12 + 4 bits the largest number is 127.9375, so 214.75 overflows."),
], [
  ("why numbers are normalised", "It maximises the precision for the available bits, uses the fewest bits for the range, and gives each number one representation."),
  ("what overflow is", "The result of a calculation is too large to store, so the most significant bits are lost."),
  ("what underflow is", "The result is closer to zero than the smallest number that can be stored, so it is stored as zero."),
  ("why a number is an approximation", "Its binary fraction needs more bits than the mantissa has, so the least significant bits are truncated and precision is lost."),
], [("State", "Give the fact in a short sentence."), ("Explain", "Give the cause and the effect, using the numbers in the question."), ("Describe", "Say what happens, with an example."), ("Normalise", "Show the shifts and the change to the exponent.")]) + FC

js = AKJS + AK20JS + r'''
const val2 = (s) => { const n = parseInt(s, 2); return s[0] === "1" ? n - 2 ** s.length : n; };
const decodeFp = (m, e) => (val2(m) / 2 ** (m.length - 1)) * 2 ** val2(e);
function encodeFp(x, mb, eb) {
  if (x === 0) return { m: "0".repeat(mb), e: "0".repeat(eb), exact: true, ev: 0 };
  const mag = Math.abs(x); let e = 0, m = mag;
  while (m >= 1) { m /= 2; e++; } while (m < 0.5) { m *= 2; e--; }
  const scaled = m * 2 ** (mb - 1), pos = Math.floor(scaled), exact = scaled === pos, mi = x > 0 ? pos : 2 ** mb - pos;
  const tw = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");
  return { m: tw(mi, mb), e: tw(e, eb), exact, ev: e };
}
const tw2 = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const sh = [0, 1, 3, 6][k], m = ("0000000111" + "000000").slice(sh, sh + 10), e = tw2(val2("100111") - sh, 6);
    let o = SV.text(30, 22, "Mantissa", "sm") + SV.text(430, 22, "Exponent", "sm");
    m.split("").forEach((c, i) => (o += SV.rect(30 + i * 34, 30, 30, 36, i < 2 ? (m[0] !== m[1] ? "cell-ok" : "cell-no") : "f3", { rx: 4 }) + SV.text(45 + i * 34, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })));
    e.split("").forEach((c, i) => (o += SV.rect(430 + i * 34, 30, 30, 36, "f2", { rx: 4 }) + SV.text(445 + i * 34, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })));
    o += SV.text(30, 100, m[0] !== m[1] ? "starts " + m[0] + m[1] + ": NORMALISED" : "starts " + m[0] + m[1] + ": not normalised", "lbl bd " + (m[0] !== m[1] ? "t3" : "t2"), { style: "font-size:16px" });
    o += SV.text(430, 100, "exponent = " + val2(e), "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    if (sh) o += SV.text(30, 140, sh + " shift" + (sh > 1 ? "s" : "") + " left, so the exponent drops by " + sh + " (from −25)", "lbl", { style: "font-size:15px" });
    if (k === 3) o += SV.text(30, 178, "value unchanged: 0.0000000111 × 2^-25 = 0.111 × 2^-31", "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 205, label: "Shifting a mantissa until it is normalised", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Mantissa <code>0000000111</code>, exponent <code>100111</code> (−25). The mantissa starts 00, so the leading zeros are wasted: it is <b>not normalised</b>.", s: { i: 0 } },
    { cap: "Shift the mantissa <b>1 place left</b>. Each shift doubles the mantissa, so the exponent is reduced by 1 to keep the value the same.", s: { i: 1 } },
    { cap: "After 3 shifts it still starts 00. The exponent is −28.", s: { i: 2 } },
    { cap: "After <b>6</b> shifts the mantissa starts <b>01</b>: normalised. The exponent is −25 − 6 = −31 (<code>100001</code>).", s: { i: 3 } }] });
})();

(function () {
  const al = [[12, 4], [10, 6], [8, 8]];
  const draw = (s) => {
    const k = Math.round(s.i), [mb, eb] = al[k], E = 2 ** (eb - 1); let o = "";
    for (let i = 0; i < 16; i++) o += SV.rect(30 + i * 28, 30, 24, 34, i < mb ? "f3" : "f2", { rx: 4 }) + SV.text(42 + i * 28, 52, i < mb ? "M" : "E", "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
    o += SV.text(30, 90, mb + " bits mantissa (precision)", "lbl bd", { style: "font-size:14px" }) + SV.text(430, 90, eb + " bits exponent (range)", "lbl bd", { style: "font-size:14px" });
    o += SV.rect(30, 110, mb * 30, 20, "f3", { rx: 4, ...op(0.8) }) + SV.text(30, 150, "precision", "sm");
    o += SV.rect(30, 164, eb * 38, 20, "f2", { rx: 4, ...op(0.8) }) + SV.text(30, 204, "range", "sm");
    o += SV.text(430, 130, "largest ≈ 2^" + (E - 1), "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(430, 160, "smallest ≈ 2^-" + (E + 1), "lbl", { style: "font-family:var(--mono);font-size:15px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Sharing 16 bits", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "<b>12 + 4</b>: lots of precision, but the 4-bit exponent only reaches 2<sup>7</sup> = 128: a small range.", s: { i: 0 } },
    { cap: "<b>10 + 6</b>: two bits move from the mantissa to the exponent. The range becomes huge (up to 2<sup>31</sup>) but each number has fewer digits of precision.", s: { i: 1 } },
    { cap: "<b>8 + 8</b>: the exponent reaches 2<sup>127</sup>, but with only 7 digits after the sign bit the numbers are rough approximations. Precision and range trade off.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.line(40, 100, 720, 100, "ax");
    o += SV.rect(240, 70, 280, 60, "f3", { rx: 6, ...op(0.55) }) + SV.text(380, 124, "range that can be stored", "lbl bd", { "text-anchor": "middle" });
    o += SV.text(240, 150, "-largest", "sm", { "text-anchor": "middle" }) + SV.text(520, 150, "+largest", "sm", { "text-anchor": "middle" }) + SV.text(380, 150, "0", "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.circle(640, 100, 12, "dot2") + SV.text(640, 70, "214.75", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(640, 175, "OVERFLOW: beyond +127.9375", "lbl bd t2", { "text-anchor": "middle" });
    if (k >= 2) o += SV.circle(380, 100, 5, "dot1") + SV.text(380, 55, "1.0 × 10^-12 → 0", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(380, 200, "UNDERFLOW: closer to 0 than the smallest number", "lbl bd t2", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "Overflow and underflow", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A system can only store numbers within a range. In 12 + 4 bits the largest is 127.9375.", s: { i: 0 } },
    { cap: "<b>Overflow</b>: 91.5 + 123.25 = 214.75 is too large. It needs an exponent of 8, which does not fit. The most significant bits are lost.", s: { i: 1 } },
    { cap: "<b>Underflow</b>: a result very close to zero, smaller than the smallest storable number, is stored as zero.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "0.1 in binary", "lbl bd", { style: "font-size:16px" });
    o += SV.text(30, 64, "0.000110011001100110011...  (recurring)", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(30, 100, "normalised: 0.110011001100... × 2^-3", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 136, "12-bit mantissa keeps:   011001100110   (the rest is cut off)", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 3) o += SV.text(30, 172, "stored value = ''' + fmt_frac(st01) + r'''", "lbl bd t2", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(30, 200, "not 0.1: a rounding error of about −0.0000244", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "A rounding error", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "0.1 is easy in denary but in <b>binary</b> it recurs: 0.0001100110011... It cannot be written as a finite sum of ½, ¼, ⅛...", s: { i: 0 } },
    { cap: "Normalised, the mantissa digits are 1100110011... with exponent −3.", s: { i: 1 } },
    { cap: "A 12-bit mantissa can only keep the first digits: the rest is <b>truncated</b>.", s: { i: 2 } },
    { cap: "The stored value is a little less than 0.1. A <b>rounding error</b> appears, and it can build up over many calculations.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const pre = [["0000000111", "100111"], ["00011110", "00011000"], ["11110000", "000100"], ["00000001", "000011"]]; let cur = 0, m, e, n;
  const reset = () => { m = pre[cur][0]; e = pre[cur][1]; n = 0; paint(); };
  const paint = () => {
    $$("#nB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const norm = m[0] !== m[1];
    $("#nS").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Mantissa</th><th>Exponent</th><th>Value</th><th>Normalised?</th></tr><tr><td>' + m + "</td><td>" + e + " (" + val2(e) + ")</td><td>" + +decodeFp(m, e).toPrecision(12) + "</td><td>" + (norm ? "yes: starts " + m[0] + m[1] : "no: starts " + m[0] + m[1]) + "</td></tr></table></div>";
    $("#nV").textContent = norm ? "Normalised after " + n + " shift" + (n === 1 ? "" : "s") + ". The value is unchanged." : "Shift left; the exponent will drop by 1 each time. Shifts so far: " + n + ".";
  };
  $("#nB").innerHTML = pre.map((p, i) => `<button class="b" data-i="${i}">${p[0]} | ${p[1]}</button>`).join("");
  $$("#nB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; reset(); }));
  $("#nL").onclick = () => { if (m[0] !== m[1]) return; if (parseInt(m, 2) === 0 || /^(0+|1+)$/.test(m)) { $("#nV").textContent = "A mantissa of all 0s or all 1s cannot be normalised."; return; } m = m.slice(1) + "0"; e = tw2(val2(e) - 1, e.length); n++; paint(); };
  $("#nR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let mb = 10;
  const paint = () => {
    const eb = 16 - mb, E = 2 ** (eb - 1), big = (1 - 2 ** -(mb - 1)) * 2 ** (E - 1), small = 2 ** -(E + 1);
    $("#s1").textContent = big.toExponential(3) + "  (2^" + (E - 1) + ")"; $("#s2").textContent = small.toExponential(3) + "  (2^-" + (E + 1) + ")"; $("#s3").textContent = (2 ** -(mb - 1)).toExponential(2) + " (spacing 2^-" + (mb - 1) + ")";
    $("#sV").textContent = mb + " bits for the mantissa and " + eb + " for the exponent. " + (mb >= 11 ? "High precision, small range." : mb <= 8 ? "Large range, low precision." : "A balance of range and precision.");
  };
  Lib.slider($("#sS"), { id: "sss", label: "Bits for the mantissa (the rest go to the exponent) ", min: 6, max: 13, value: mb, fmt: (x) => x + " + " + (16 - x), onInput: (v) => { mb = v; paint(); } });
  paint();
})();

/* Lab 3 */
(function () {
  const al = [[12, 4], [10, 6], [8, 8]]; let cur = 0;
  const run = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const x = parseFloat($("#rN").value); if (isNaN(x)) { $("#rO").innerHTML = ""; $("#rV").textContent = "Enter a number."; return; }
    const [mb, eb] = al[cur], r = encodeFp(x, mb, eb), v = decodeFp(r.m, r.e), maxE = 2 ** (eb - 1);
    const outOfRange = r.ev > maxE - 1 || r.ev < -maxE;
    $("#rO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Mantissa</th><th>Exponent</th><th>Stored value</th><th>Error</th></tr><tr><td>' + r.m + "</td><td>" + r.e + "</td><td>" + +v.toPrecision(14) + "</td><td>" + +(v - x).toPrecision(4) + "</td></tr></table></div>";
    $("#rV").textContent = outOfRange ? "The exponent needed (" + r.ev + ") does not fit in " + eb + " bits: overflow or underflow." : r.exact ? "Stored exactly: the number is a sum of powers of 2 that fits in the mantissa." : "Not stored exactly: the stored value is the nearest the mantissa can hold, so there is a rounding error.";
  };
  $("#rB").innerHTML = al.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#rB button").forEach((b, i) => (b.onclick = () => { cur = i; run(); }));
  $("#rE").innerHTML = ["0.1", "0.25", "0.3", "65.2", "1000000"].map((v) => `<button class="b">${v}</button>`).join("");
  $$("#rE button").forEach((b) => (b.onclick = () => { $("#rN").value = b.textContent; run(); }));
  $("#rR").onclick = run; $("#rN").addEventListener("keydown", (ev) => { if (ev.key === "Enter") run(); });
  run();
})();
''' + CLASSIFY("cl1", "Is each mantissa normalised?", ["Normalised", "Not normalised"],
  [("0110100000", 0), ("1001100000", 0), ("0011010000", 1), ("1101100000", 1), ("01000000", 0), ("00000011", 1), ("10000000", 0), ("11100000", 1)],
  "Normalised: the first two bits differ (01 or 10).") + CLASSIFY("cl2", "Which change gives this effect?", ["More mantissa bits", "More exponent bits"],
  [("Greater precision", 0), ("A larger range of numbers", 1), ("More significant digits stored", 0), ("A larger largest number", 1), ("Smaller rounding errors", 0), ("A smaller smallest positive number", 1)],
  "Mantissa: precision. Exponent: range.") + ORDER(
  "Put the steps for normalising a mantissa in order.",
  ["Check the first two bits of the mantissa", "If they are the same, shift the mantissa left one place", "Reduce the exponent by 1", "Repeat until the first two bits differ", "Write the new mantissa and exponent"],
  "Check, shift, lower the exponent, repeat, write.") + MATCH([
  ["Normalised", "Mantissa starts 01 or 10"], ["Overflow", "A result too large to be stored"], ["Underflow", "A result closer to zero than the smallest storable number"], ["Rounding error", "The difference between a number and its stored approximation"], ["Truncated", "Least significant bits that do not fit are lost"]]) + CALC([
  {"q": "Mantissa 00011000 is shifted left until it is normalised. How many shifts are needed?", "a": 2, "unit": "", "tol": 0.01, "hint": "00011000 → 00110000 → 01100000.", "sol": "<b>2</b> shifts."},
  {"q": "The exponent is 5 before 3 shifts left are made to normalise. What is it after?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b>."},
  {"q": "The exponent is −25 and the mantissa needs 6 shifts. What is the new exponent?", "a": -31, "unit": "", "tol": 0.01, "hint": "−25 − 6.", "sol": "<b>−31</b>."},
  {"q": "What is the largest positive value with a 12-bit mantissa and a 4-bit exponent? (1 − 2^-11) × 2^7, to 4 decimal places.", "a": 127.9375, "unit": "", "tol": 0.001, "hint": "128 − 0.0625.", "sol": "<b>127.9375</b>."},
  {"q": "The largest value is 127.9375. Does 91.5 + 123.25 (= 214.75) overflow? Enter 1 for yes, 0 for no.", "a": 1, "unit": "", "tol": 0.01, "hint": "214.75 > 127.9375.", "sol": "<b>1</b>: yes."},
  {"q": "How many bits does a 10-bit mantissa system with a 6-bit exponent use in total?", "a": 16, "unit": "bits", "tol": 0.01, "hint": "10 + 6.", "sol": "<b>16</b> bits."}]) + MCQ([
  ("A normalised positive mantissa starts...", ["00", "01", "10", "11"], 1, "01: 0.1..."),
  ("Increasing the bits for the exponent...", ["increases precision", "increases range", "decreases range", "does nothing"], 1, "More exponent bits means a larger range (and, with a fixed total, less precision)."),
  ("What is overflow?", ["A result too small to store", "A result too large to store", "A file that is too big", "Memory running out"], 1, "The most significant bits are lost."),
  ("Why is 0.1 only an approximation in binary?", ["It is negative", "It is a recurring binary fraction cut off by the mantissa", "It is too large", "It is an integer"], 1, "A finite mantissa cannot hold a recurring fraction."),
  ("Why are numbers normalised?", ["To make them negative", "To maximise precision and give one representation", "To save the file", "To add a sign bit"], 1, "No wasted leading bits."),
  ("What happens to the exponent when the mantissa is shifted left once?", ["It increases by 1", "It decreases by 1", "It is unchanged", "It doubles"], 1, "To keep the value the same.")], "qz1") + CARDS([
  ("Normalised", "Mantissa starts 01 or 10: no wasted leading bits."), ("Normalising", "Shift mantissa left until first two bits differ; subtract the shifts from the exponent."), ("More mantissa bits", "More precision, smaller range."), ("More exponent bits", "Larger range, less precision."),
  ("Overflow", "Result too large to store."), ("Underflow", "Result too small: stored as zero."), ("Rounding error", "Stored value differs from the real number: binary cannot hold it exactly."), ("Fix", "Compare with a tolerance; store money as integers.")])

build("ac1332", "ac-13-3-2-floating-point-accuracy", "Floating-point Numbers: Normalisation, Range and Errors", EYA("13.3.2"),
  "Why and how numbers are normalised, how the allocation of bits affects range and precision, overflow, underflow and rounding errors; animations, labs and the real 9618 theory questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.3 Floating-point numbers, representation and manipulation"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
