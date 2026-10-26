"""A Level CS syllabus 13.3.1: floating-point format and conversion. Run: python3 tools/artifact-kit/mk_ac1331.py"""
from ak20 import *
from fpq import *
from fractions import Fraction as F


def sysd(mb, eb):
    return f"Numbers are stored in a computer system using binary floating-point representation with {mb} bits for the mantissa, {eb} bits for the exponent, and two's complement form for both."


def enc_marks(marks, neg):
    if marks == 2:
        return ["correct mantissa", "correct exponent"]
    if marks == 3:
        return (["number converted to binary", "the binary point moved: the exponent worked out", "correct mantissa and exponent"] if not neg else
                ["number converted to binary", "the negative form worked out (two's complement) and the exponent", "correct mantissa and exponent"])
    if marks == 4:
        return (["number converted to binary", "binary point moved: the exponent worked out", "correct mantissa", "correct exponent"] if not neg else
                ["the positive number converted to binary", "negative mantissa found: bits flipped and 1 added", "correct mantissa", "correct exponent"])
    return ["correct answer"]


def dec_marks(marks):
    return (["exponent converted to denary", "the exponent applied to the mantissa (binary point moved)", "correct denary answer"] if marks == 3 else ["the exponent applied to the mantissa", "correct denary answer"])


def encq(src, marks, x, mb, eb, label="denary", prefix="", note=None):
    """a 'write the normalised floating-point representation' question with computed working"""
    x = F(x)
    shown = label if label != "denary" else None
    L, m, e, exact = enc_working(x, mb, eb)
    neg = x < 0
    txt = f"{sysd(mb, eb)} " + (f"Calculate the normalised floating-point representation of {fmt_frac(x)} in this system. Show your working." if shown is None else f"Write the normalised floating-point representation of the binary number {shown} in this system. Show your working.")
    ans = "<p>" + mks(enc_marks(marks, neg)) + "</p>" + qcode("\n".join(l for l in L if l) + f"\n\nMantissa  {m}\nExponent  {e}")
    if not exact:
        ans += "<p><span class=\"mk a\">The number needs more bits than the mantissa has, so the least significant bits are lost and precision is reduced.</span></p>"
    return peq(src, f"{marks} marks", "Calculate", txt,
               "Convert to binary, move the binary point so the mantissa is 0.1... (or 1.0... for a negative), then write the mantissa and the exponent in two's complement." if not neg else
               "Work out the positive number first, then take the two's complement of the mantissa. The exponent does not change.",
               ans, note)


def decq(src, marks, m, e, note=None):
    L, v = dec_working(m, e)
    txt = f"{sysd(len(m), len(e))} Calculate the denary value of the given normalised binary floating-point number. Show your working." + qcode(f"Mantissa  {m}\nExponent  {e}")
    ans = "<p>" + mks(dec_marks(marks)) + "</p>" + qcode("\n".join(L) + f"\n\nDenary value  {fmt_frac(v)}")
    return peq(src, f"{marks} marks", "Calculate", txt,
               "Find the exponent first, then move the binary point that many places right (or left if the exponent is negative), then add up the place values. A mantissa that starts with 1 is negative, so its first bit counts as a negative place value.",
               ans, note)


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A computer stores a real number in <b>floating-point</b> form as a <b>mantissa</b> (the digits) and an <b>exponent</b> (the power of 2 that scales them), both in <b>two's complement</b>, so the value is <b>mantissa × 2<sup>exponent</sup></b>. The mantissa has an implied binary point after its first bit, so it is a value from −1 up to (but not including) +1, and the exponent says how many places to move the point right (positive) or left (negative). To convert a floating-point number to denary you read the exponent, move the binary point, and add up the place values, remembering the first bit of a negative mantissa has a negative place value. To convert a number to floating-point you convert it to binary, move the point to get a normalised mantissa, find the exponent, and for a negative number take the two's complement of the mantissa. The next page covers normalisation, accuracy and errors.</p></div>

  <h2>1 · The format</h2>
  <p>A floating-point number is stored in two parts, with a fixed number of bits for each, for example 10 bits for the mantissa and 6 for the exponent (16 bits in total):</p>
  <div class="tw"><table class="t mono">
    <tr><th colspan="10">Mantissa (10 bits)</th><th colspan="6">Exponent (6 bits)</th></tr>
    <tr><td>1</td><td>.0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>
  </table></div>
  <ul>
    <li>The <b>mantissa</b> is a two's complement fraction. The binary point sits <b>after the first bit</b>: <code>1.011000111</code>. The first bit has a place value of −1; the rest are ½, ¼, ⅛...</li>
    <li>The <b>exponent</b> is a two's complement <b>integer</b>: <code>000111</code> is 7, <code>100001</code> is −31.</li>
    <li><b>Value = mantissa × 2<sup>exponent</sup></b>. Multiplying by 2<sup>7</sup> moves the binary point 7 places to the right.</li>
    <li>A <b>positive</b> mantissa starts 0 and a <b>negative</b> one starts 1.</li>
  </ul>
  <div class="tip"><b class="h">Two's complement reminder</b>The first bit has a negative place value. In 8 bits, 10011011 is −128 + 16 + 8 + 2 + 1 = −101. To negate a number, <b>invert every bit and add 1</b>. So −(01100101) = 10011010 + 1 = 10011011.</div>

  <h2>2 · Floating-point to denary</h2>
  <ol>
    <li><b>Exponent:</b> convert the exponent from two's complement to denary.</li>
    <li><b>Move the point:</b> write the mantissa with its point after the first bit, then move the point right by the exponent (left if the exponent is negative), adding zeros if you run out of bits.</li>
    <li><b>Evaluate:</b> add up the place values. For a negative number the first (left-most) bit is negative: −2<sup>n</sup>.</li>
  </ol>
  <div class="tw"><table class="t mono">
    <tr><th>Step</th><th>Mantissa 1011000111, exponent 000111</th></tr>
    <tr><td>Exponent</td><td>000111 = 7</td></tr>
    <tr><td>Mantissa with its point</td><td>1.011000111</td></tr>
    <tr><td>Move the point 7 places right</td><td>10110001.11</td></tr>
    <tr><td>Place values</td><td>−128 + 32 + 16 + 1 + 0.5 + 0.25</td></tr>
    <tr><td>Value</td><td><b>−78.25</b></td></tr>
  </table></div>
  <p>A positive example: mantissa <code>0100111100</code>, exponent <code>001001</code> = 9. The mantissa is 0.100111100; moving the point 9 places gives 100111100, which is 256 + 32 + 16 + 8 + 4 = <b>316</b>. With a <b>negative exponent</b> the point moves left: exponent −2 turns 0.101 into 0.00101.</p>

  <h2>3 · Denary to floating-point</h2>
  <ol>
    <li><b>Convert</b> the number (ignore the sign) to binary, including any fraction.</li>
    <li><b>Normalise:</b> move the binary point so the number is written 0.1... × 2<sup>n</sup>. The number of places moved is the exponent (positive if the point moved left, negative if it moved right).</li>
    <li><b>Write the mantissa:</b> a 0 for the sign, then the digits, padding with zeros on the right to fill the mantissa.</li>
    <li><b>Negative numbers:</b> take the two's complement of the mantissa (invert and add 1). The exponent stays the same.</li>
    <li><b>Write the exponent</b> in two's complement using the bits available.</li>
  </ol>
  <div class="tw"><table class="t mono">
    <tr><th>Step</th><th>−7.25 in a 10-bit mantissa, 6-bit exponent</th></tr>
    <tr><td>Binary</td><td>7.25 = 111.01</td></tr>
    <tr><td>Normalise</td><td>0.11101 × 2<sup>3</sup>, so the exponent is 3</td></tr>
    <tr><td>Positive mantissa</td><td>0111010000</td></tr>
    <tr><td>Negative: invert, add 1</td><td>1000101111 + 1 = 1000110000</td></tr>
    <tr><td>Exponent 3 in 6 bits</td><td>000011</td></tr>
    <tr><td>Answer</td><td><b>1000110000  000011</b></td></tr>
  </table></div>
  <div class="tip"><b class="h">Check yourself</b>Convert your answer back to denary. 1.000110000 × 2<sup>3</sup> = 1000.110000 = −8 + 0.5 + 0.25 = −7.25. A normalised <b>negative</b> mantissa always starts <b>10</b>; a normalised <b>positive</b> one starts <b>01</b>.</div>
  <p>If the number has more significant bits than the mantissa can hold, the <b>extra bits on the right are lost</b> (truncated). The stored value is then only an approximation (see the next page).</p>
  <div class="code">''' + pc('''from fractions import Fraction

def to_float(x, mbits, ebits):
    """normalised two's complement mantissa and exponent for x"""
    mag, e = abs(Fraction(x)), 0
    while mag >= 1: mag, e = mag / 2, e + 1
    while mag < Fraction(1, 2): mag, e = mag * 2, e - 1
    m = int(mag * 2 ** (mbits - 1))                  # truncate extra bits
    if x < 0: m = (1 << mbits) - m                   # two's complement
    return format(m, f"0{mbits}b"), format(e % (1 << ebits), f"0{ebits}b")

print(to_float(-7.25, 10, 6))                        # ('1000110000', '000011')''') + '''</div>

  <h2>4 · Setting out your answer</h2>
  <ul>
    <li>Show the conversion to binary, the movement of the binary point (the exponent), and the final mantissa and exponent. The mark scheme awards marks for the working.</li>
    <li>Write the answer in the table the question gives: mantissa on the left, exponent on the right.</li>
    <li>Count the bits: a 10-bit mantissa has exactly 10 digits and a 6-bit exponent exactly 6.</li>
  </ul>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Treating the mantissa as a whole number. The point is after the first bit.</li>
    <li>Getting the exponent's direction wrong: moving the point <b>right</b> makes a <b>positive</b> exponent when converting to denary; moving it <b>left</b> to normalise a large number also makes a <b>positive</b> exponent.</li>
    <li>For a negative number, forgetting to take the two's complement of the whole mantissa, or changing the exponent.</li>
    <li>Not giving the first bit of a negative mantissa a negative place value when evaluating.</li>
    <li>Writing a mantissa or exponent with the wrong number of bits.</li>
    <li>Not saying the number is truncated (precision lost) when it does not fit in the mantissa.</li>
  </ul>
'''

watch = '''
  <h2>1 · Reading a floating-point number</h2>
  <p>Press Play, or click the steps. Mantissa 1011000111 and exponent 000111.</p>
  <div id="stA"></div>
  <h2>2 · Converting −7.25 to floating-point</h2>
  <div id="stB"></div>
  <h2>3 · The exponent moves the binary point</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Floating-point to denary: flip the bits</h2>
  <p>Click a bit to flip it. The value is worked out from the mantissa and exponent.</p>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fM" class="btnrow"></div><div id="fE" class="btnrow"></div><div id="fW"></div><div class="readout"><div><small>Exponent</small><strong id="f1"></strong></div><div><small>Mantissa</small><strong id="f2"></strong></div><div><small>Value</small><strong id="f3"></strong></div></div></div>

  <h2>Lab 2 · Denary to floating-point</h2>
  <p>Type a number (it may be negative or have a fractional part) and choose the allocation of bits. The working is shown as in the exam.</p>
  <div class="card"><div id="gB" class="btnrow"></div><p><input id="gN" type="text" value="-7.25" style="width:12em;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Number"> <button class="b pri" id="gR">Convert</button></p><div id="gW"></div><div class="verdict" id="gV"></div></div>

  <h2>Lab 3 · The format</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Mantissa or exponent?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which way does the point move?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for converting a denary number in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Conversions</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Why computers use floating point", "A scientific calculation may involve both the size of an atom and the distance to a star. Floating point stores a number as digits and a scale factor so the same number of bits can cover both huge and tiny values.", "floating point trades some precision for a very wide range.") +
rw("A weather model", "Temperatures, pressures and distances are real numbers with fractional parts. The model stores them in floating point and a small rounding at each step can add up over many steps.", "floating-point numbers are often approximations of the true value.") +
rw("Graphics and games", "Positions and colours of millions of points are real numbers. Graphics hardware is built to do floating-point arithmetic very fast.", "mantissa and exponent let one format store many magnitudes.") +
rw("Money in a banking program", "Money is often stored as a whole number of pence rather than a floating-point number, because some decimals such as 0.1 cannot be stored exactly in binary.", "not every decimal fraction can be stored exactly in binary floating point.") +
rw("Scientific notation", "Writing 6.02 × 10<sup>23</sup> is the same idea in denary: a number (the mantissa) and a power of ten (the exponent). Floating point uses powers of 2.", "value = mantissa × 2<sup>exponent</sup>.")
)

where = [
  ("M/J 2021", "31, 32, 33", "1(a), 1(b)", "3 + 3", "Denary to floating-point (−7.25); floating-point to denary"),
  ("O/N 2021", "31, 32", "1(a)(i)", "2", "Normalised floating-point form of a binary number"),
  ("O/N 2022", "31, 33", "1(a), 1(b)", "3 + 3", "+202 and −202 in an 8-bit mantissa, 8-bit exponent"),
  ("O/N 2022", "32", "1(b)", "3", "Floating-point to denary"),
  ("M/J 2023", "31, 33", "1(a)", "4", "113.75 in two different systems"),
  ("M/J 2023", "32", "1(a)", "2", "A binary number to floating-point"),
  ("O/N 2023", "31, 33", "1(a)", "3", "+65.25 to floating-point"),
  ("O/N 2023", "32", "1(a)", "3", "−96.75 to floating-point"),
  ("M/J 2024", "31, 33", "1(a), 1(b)", "3 + 3", "Floating-point to denary; −102.75 to floating-point"),
  ("M/J 2024", "32", "1(b)", "3", "+54.8125 to floating-point"),
  ("O/N 2024", "31, 33", "1(a), 1(b)", "3 + 3", "+201.125 to floating-point; floating-point to denary"),
  ("O/N 2024", "32", "4(a), 4(b)", "2 + 4", "Floating-point to denary; −49.1875 to floating-point"),
  ("M/J 2025", "31", "2(a), 2(b)", "2 + 4", "A small binary number and −25.3125 to floating-point"),
  ("M/J 2025", "32", "2(a), 2(b)", "3 + 3", "+124.4375 to floating-point; floating-point to denary"),
  ("M/J 2025", "33", "2(b)", "4", "−3.59375 to floating-point"),
  ("O/N 2025", "31", "2(a), 2(b)", "2 + 4", "A small binary number and −76.1875 to floating-point"),
  ("O/N 2025", "32", "2(a), 2(b)", "3 + 3", "Floating-point to denary; +26.6875 to floating-point"),
  ("M/J 2026", "31", "3(a), 3(b)", "3 + 3", "−10.8125 to floating-point; floating-point to denary"),
  ("M/J 2026", "32", "3(a)", "3", "Floating-point to denary"),
  ("M/J 2026", "33", "5(a)", "4", "−18.5625 to floating-point")]

past = '''  <p class="note">Floating-point conversion is the most frequently tested topic in this chapter: nearly every Paper 3 from May/June 2021 to May/June 2026 has one or two conversions. Every mantissa, exponent and denary value below was calculated and checked against the mark scheme. The theory questions on normalisation, precision and errors are on the next page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Denary or binary to floating-point</h3>
''' + encq(SRC("s21", "31, 32, 33", "Q1(a)"), 3, F(-29, 4), 10, 6) + encq(SRC("w22", "31, 33", "Q1(a)"), 3, 202, 8, 8) + encq(SRC("w22", "31, 33", "Q1(b)"), 3, -202, 8, 8) + encq(SRC("w23", "31, 33", "Q1(a)"), 3, F(261, 4), 12, 4) + encq(SRC("w23", "32", "Q1(a)"), 3, F(-387, 4), 10, 6) + encq(SRC("s24", "31, 33", "Q1(b)"), 3, F(-411, 4), 10, 6) + encq(SRC("s24", "32", "Q1(b)"), 3, F(877, 16), 12, 4) + encq(SRC("w24", "32", "Q4(b)"), 4, F(-787, 16), 12, 4) + encq(SRC("s25", "31", "Q2(b)"), 4, F(-405, 16), 10, 6) + encq(SRC("s25", "32", "Q2(a)"), 3, F(1991, 16), 12, 4) + encq(SRC("s25", "33", "Q2(b)"), 4, F(-115, 32), 8, 8) + encq(SRC("w25", "31", "Q2(b)"), 4, F(-1219, 16), 12, 4) + encq(SRC("w25", "32", "Q2(b)"), 3, F(427, 16), 10, 6) + encq(SRC("s26", "31", "Q3(a)"), 3, F(-173, 16), 10, 6) + encq(SRC("s26", "33", "Q5(a)"), 4, F(-297, 16), 12, 4) + '''
  <h3>Denary conversion with a given number of bits that is too small</h3>
''' + encq(SRC("w24", "31, 33", "Q1(a)"), 3, F(1609, 8), 10, 6, note="A number that needs more bits than the mantissa has is truncated. The mark scheme also gives a mark for stating that precision is lost.") + peq(SRC("s23", "31, 33", "Q1(a)"), "4 marks", "Calculate",
  "Numbers are stored in two different computer systems using floating-point representation. System 1 uses 10 bits for the mantissa and 6 bits for the exponent. System 2 uses 8 bits for the mantissa and 8 bits for the exponent. Both use two's complement for the mantissa and the exponent. Calculate the normalised floating-point representation of 113.75 and show how it would be represented in each of these two systems. Show your working.",
  "One working out, two different mantissa lengths. System 2 has fewer bits for the mantissa.",
  "<p>" + mks(["113.75 converted to binary: 1110001.11", "normalised 0.11100011 1 × 2^7, so the exponent is 7", "System 1: mantissa 0111000111, exponent 000111", "System 2: mantissa 01110001 (the extra bits are lost), exponent 00000111"]) + "</p>" + qcode('''113.75 = 1110001.11
       = 0.111000111 × 2^7

System 1 (10, 6):  Mantissa 0111000111   Exponent 000111
System 2 (8, 8):   Mantissa 01110001     Exponent 00000111'''),
  "Using 6 bits for the exponent in System 2. System 2 has an 8-bit exponent.") + peq(SRC("w21", "31, 32", "Q1(a)(i)"), "2 marks", "Write",
  "Numbers are stored in a computer using floating-point representation with 12 bits for the mantissa, 4 bits for the exponent, and two's complement form for both. Write the normalised floating-point representation of the following unsigned binary number using this system: 1011100.011001",
  "The number is already binary. Move the point to the front and fit the digits into 12 bits.",
  "<p>" + mks(["correct mantissa", "correct exponent"]) + "</p>" + qcode('''1011100.011001 = 0.1011100011001 × 2^7

Mantissa  010111000110     (12 bits: the last two digits do not fit)
Exponent  0111'''), "Putting the 13 digits into the mantissa. The mantissa has only 12 bits, including the sign bit, so the last digits are lost.") + peq(SRC("s23", "32", "Q1(a)"), "2 marks", "Write",
  "Numbers are stored with 10 bits for the mantissa, 6 bits for the exponent, two's complement for both. Write the normalised floating-point representation of the binary number 0101010.111 in this system.",
  "Remove the leading zero first: the number is 101010.111.",
  "<p>" + mks(["mantissa 0101010111", "exponent 000110"]) + "</p>" + qcode('''0101010.111 = 101010.111 = 0.101010111 × 2^6

Mantissa  0101010111
Exponent  000110'''), None) + peq(SRC("s25", "31", "Q2(a)"), "2 marks", "Write",
  "Numbers are stored with 10 bits for the mantissa, 6 bits for the exponent, two's complement for both. Write the normalised floating-point representation of the binary number 0.00000011010111 in this system.",
  "This is a very small number, so the exponent will be negative: count how many places the point moves right.",
  "<p>" + mks(["mantissa 0110101110", "exponent 111010 (−6)"]) + "</p>" + qcode('''0.00000011010111 = 0.11010111 × 2^(-6)       (the point moves 6 places right)

Mantissa  0110101110
Exponent  111010         (−6 in 6-bit two's complement)'''), "Giving a positive exponent. The point moved right, so the exponent is negative.") + peq(SRC("w25", "31", "Q2(a)"), "2 marks", "Write",
  "Numbers are stored with 12 bits for the mantissa, 4 bits for the exponent, two's complement for both. Write the normalised floating-point representation of the binary number 0.00000001110101101 in this system.",
  "Another small number: the point moves right 7 places.",
  "<p>" + mks(["mantissa 011101011010", "exponent 1001 (−7)"]) + "</p>" + qcode('''0.00000001110101101 = 0.1110101101 × 2^(-7)

Mantissa  011101011010
Exponent  1001         (−7 in 4-bit two's complement)'''), None) + '''
  <h3>Floating-point to denary</h3>
''' + decq(SRC("s21", "31, 32, 33", "Q1(b)"), 3, "1011000111", "000111") + decq(SRC("w22", "32", "Q1(b)"), 3, "10110010011", "01001") + decq(SRC("s24", "31, 33", "Q1(a)"), 3, "0100111100", "001001") + decq(SRC("w24", "31, 33", "Q1(b)"), 3, "1010110011", "000101") + decq(SRC("w24", "32", "Q4(a)"), 2, "010001110111", "0111") + decq(SRC("s25", "32", "Q2(b)"), 3, "101000101011", "0110") + decq(SRC("w25", "32", "Q2(a)"), 3, "0111100101", "001011") + decq(SRC("s26", "31", "Q3(b)"), 3, "1010000111", "000111") + decq(SRC("s26", "32", "Q3(a)"), 3, "101101000110", "0110")

review = req("3 marks", "Calculate", "A system uses 8 bits for the mantissa and 4 bits for the exponent, both in two's complement. Calculate the denary value of mantissa 01100000 and exponent 0011.", "Exponent 3; move the point 3 places.",
  "<p>" + mks(["exponent 0011 = 3", "mantissa 0.1100000 with its point moved 3 places right: 110.0000", "value 4 + 2 = 6"]) + "</p>" + qcode('''Exponent 0011 = 3
Mantissa 0.1100000
Move the point 3 places right: 110.0000
Value = 4 + 2 = 6'''), "Moving the point the wrong way, or by the wrong number of places.") + req("3 marks", "Calculate", "Calculate the 8-bit mantissa and 4-bit exponent (two's complement) for the denary number 5.5.", "Convert to binary, normalise, write the bits.",
  "<p>" + mks(["5.5 = 101.1", "0.1011 × 2^3, exponent 0011", "mantissa 01011000"]) + "</p>" + qcode('''5.5 = 101.1 = 0.1011 × 2^3
Mantissa  01011000
Exponent  0011'''), None) + req("4 marks", "Calculate", "Using an 8-bit mantissa and a 4-bit exponent, both in two's complement, write −5.5 in floating-point form.", "Use the positive mantissa for 5.5 and negate it.",
  "<p>" + mks(["5.5 = 101.1, mantissa 01011000", "invert the bits: 10100111", "add 1: 10101000", "exponent 0011"]) + "</p>" + qcode('''+5.5   mantissa 01011000   exponent 0011
invert 10100111, add 1  →  10101000
−5.5   mantissa 10101000   exponent 0011'''), "Changing the exponent for a negative number. Only the mantissa is negated.") + req("3 marks", "Calculate", "A 10-bit mantissa and 6-bit exponent (two's complement). Calculate the denary value of mantissa 0110000000 and exponent 111110.", "A negative exponent moves the point left.",
  "<p>" + mks(["exponent 111110 = −2", "mantissa 0.110000000 moved 2 places left", "value 0.1875"]) + "</p>" + qcode('''Exponent 111110 = -2
Mantissa 0.11 × 2^(-2) = 0.0011
Value = 1/8 + 1/16 = 0.1875'''), None) + req("2 marks", "State", "State how many bits in total are needed for a mantissa of 12 bits and an exponent of 4 bits, and the number of bytes this is.", "Add the two parts.",
  "<p>" + mks(["16 bits", "2 bytes"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 floating-point conversion questions from every Paper 3 between May/June 2021 and May/June 2026, with the working worked out. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Write the working.", "Binary conversion, the movement of the point, the exponent, then the answer. The marks are for the working."),
  ("Mantissa starts 0 or 1.", "0 positive, 1 negative. The point is after that first bit."),
  ("Exponent sign.", "Point moves right to evaluate: positive exponent. A small number needs a negative exponent."),
  ("Negatives: negate the mantissa only.", "Invert, add 1. The exponent is the same as for the positive number."),
  ("Fit the bits.", "Count the digits in each field. Extra digits on the right are lost."),
  ("Check by converting back.", "It takes a minute and catches most slips."),
], [
  ("how floating point is stored", "A mantissa and an exponent, both in two's complement; the value is the mantissa multiplied by 2 to the power of the exponent."),
  ("how to read the exponent", "Convert it from two's complement, then move the binary point that many places."),
  ("what the working shows", "The conversion to binary, the normalising of the point and the exponent, and the two's complement of a negative mantissa."),
  ("when precision is lost", "When the number needs more bits than the mantissa has, so the least significant bits are lost."),
], [("Calculate", "Work it out and show the working, then write the answer."), ("Write", "Give the mantissa and exponent in the table, with the right number of bits."), ("Show your working", "Each step earns marks: the binary, the point, the exponent.")]) + FC

js = AKJS + AK20JS + r'''
const val2 = (s) => { const n = parseInt(s, 2); return s[0] === "1" ? n - 2 ** s.length : n; };
const decodeFp = (m, e) => (val2(m) / 2 ** (m.length - 1)) * 2 ** val2(e);
function encodeFp(x, mb, eb) {
  if (x === 0) return { m: "0".repeat(mb), e: "0".repeat(eb), exact: true };
  const mag = Math.abs(x); let e = 0, m = mag;
  while (m >= 1) { m /= 2; e++; } while (m < 0.5) { m *= 2; e--; }
  const scaled = m * 2 ** (mb - 1), pos = Math.floor(scaled), exact = scaled === pos;
  let mi = x > 0 ? pos : 2 ** mb - pos;
  const tw = (n, b) => (n < 0 ? n + 2 ** b : n).toString(2).padStart(b, "0");
  return { m: tw(mi, mb), e: tw(e, eb), exact, ev: e, mag };
}

(function () {
  const M = "1011000111", E = "000111";
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const boxes = (str, x0, cls) => str.split("").map((c, i) => SV.rect(x0 + i * 34, 30, 30, 36, cls, { rx: 4 }) + SV.text(x0 + i * 34 + 15, 55, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" })).join("");
    o += SV.text(30, 22, "Mantissa", "sm") + SV.text(430, 22, "Exponent", "sm") + boxes(M, 30, "f3") + boxes(E, 430, "f2");
    if (k >= 1) o += SV.text(430, 96, "exponent 000111 = 7", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 96, "mantissa 1.011000111", "lbl bd", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(30, 114, "(point after the first bit)", "lbl", { style: "font-family:var(--mono);font-size:12.5px" });
    if (k >= 3) o += SV.text(30, 132, "move the point 7 places right:   10110001.11", "lbl bd t3", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 4) o += SV.text(30, 168, "−128 + 32 + 16 + 1 + 0.5 + 0.25", "lbl", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 5) o += SV.text(30, 204, "value = −78.25", "lbl bd t3", { style: "font-family:var(--mono);font-size:22px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "Converting floating-point to denary", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "The 16 bits are a 10-bit <b>mantissa</b> and a 6-bit <b>exponent</b>, both in two's complement.", s: { i: 0 } },
    { cap: "Convert the exponent: <code>000111</code> is <b>7</b>.", s: { i: 1 } },
    { cap: "The mantissa has its point after the first bit: <code>1.011000111</code>. It starts with 1, so the number is negative.", s: { i: 2 } },
    { cap: "Multiply by 2<sup>7</sup>: move the point <b>7 places right</b>. <code>1.011000111</code> becomes <code>10110001.11</code>.", s: { i: 3 } },
    { cap: "Add the place values. The first bit is a <b>negative</b> place value: −128 + 32 + 16 + 1 + 0.5 + 0.25.", s: { i: 4 } },
    { cap: "The value is <b>−78.25</b>.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["7.25 in binary", "111.01"], ["Normalise: move the point 3 places left", "0.11101 × 2^3,  exponent = 3"], ["Positive mantissa (10 bits)", "0111010000"], ["Negative: invert the bits", "1000101111"], ["Add 1", "1000110000"], ["Exponent 3 in 6 bits", "000011"], ["Answer", "1000110000   000011"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Convert −7.25: 10-bit mantissa, 6-bit exponent", "lbl bd");
    rows.forEach((r, i) => { const v = i < k ? 1 : 0; if (!v) return; o += SV.rect(30, 38 + i * 34, 700, 30, i === rows.length - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(44, 59 + i * 34, r[0], "lbl", { style: "font-size:14px" }) + SV.text(330, 59 + i * 34, r[1], "lbl bd", { style: "font-family:var(--mono);font-size:15px" }); });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 285, label: "Denary to floating-point", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "Convert <b>−7.25</b> to floating-point. First ignore the sign.", s: { i: 0 } },
    { cap: "7.25 in binary: 7 is 111 and 0.25 is .01, so <b>111.01</b>.", s: { i: 1 } },
    { cap: "Normalise to 0.1...: move the point 3 places left. That is <b>× 2³</b>, so the exponent is 3.", s: { i: 2 } },
    { cap: "The positive mantissa has a 0 sign bit and the digits, padded with zeros to 10 bits.", s: { i: 3 } },
    { cap: "The number is negative, so take the <b>two's complement</b> of the mantissa. Invert every bit...", s: { i: 4 } },
    { cap: "...then add 1. The mantissa is now 1000110000. It starts with <b>10</b>, as a normalised negative mantissa does.", s: { i: 5 } },
    { cap: "The exponent does not change: 3 in 6-bit two's complement is 000011.", s: { i: 6 } },
    { cap: "The answer, mantissa then exponent: <b>1000110000 000011</b>.", s: { i: 7 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const vals = ["0.1011", "1.011", "10.11", "101.1", "1011."], dec = ["0.6875", "1.375", "2.75", "5.5", "11"];
    let o = SV.text(30, 26, "mantissa 0.1011 (0.6875)", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    o += SV.text(30, 76, "× 2^" + k, "lbl bd", { style: "font-family:var(--mono);font-size:22px" });
    o += SV.text(30, 130, "move the point " + k + " place" + (k === 1 ? "" : "s") + " right", "lbl", { style: "font-size:15px" });
    o += SV.text(30, 180, vals[k] + "  =  " + dec[k], "lbl bd t3", { style: "font-family:var(--mono);font-size:26px" });
    for (let i = 0; i <= 4; i++) o += SV.rect(430 + i * 62, 40, 54, 50, i === k ? "cell-ok" : "cell", { rx: 6 }) + SV.text(457 + i * 62, 70, "2^" + i, "lbl", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "The exponent as a shift of the binary point", base: { i: 0 }, draw, tween: 200, dwell: 2200, steps: [0, 1, 2, 3, 4].map((i) => ({ cap: i === 0 ? "A mantissa of 0.1011 is 0.5 + 0.125 + 0.0625 = <b>0.6875</b>. With exponent 0 the value is unchanged." : `Exponent ${i}: multiply by 2<sup>${i}</sup>, which moves the binary point <b>${i}</b> place${i > 1 ? "s" : ""} to the right. The value is ${["", "1.375", "2.75", "5.5", "11"][i]}. Each increase of 1 in the exponent doubles the value.`, s: { i } })) });
})();

/* Lab 1 */
(function () {
  const alloc = [[10, 6], [12, 4], [8, 8]]; let cur = 0, m = "1011000111", e = "000111";
  const paint = () => {
    $$("#fB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const bits = (str, id, w) => { $("#" + id).innerHTML = '<span style="align-self:center;margin-right:6px">' + (id === "fM" ? "Mantissa" : "Exponent") + "</span>" + str.split("").map((c, i) => `<button class="b${c === "1" ? " pri" : ""}" data-i="${i}" style="min-width:2.2em;font-family:var(--mono)">${c}</button>`).join(""); $$("#" + id + " button").forEach((b) => (b.onclick = () => { const i = +b.dataset.i, arr = (id === "fM" ? m : e).split(""); arr[i] = arr[i] === "1" ? "0" : "1"; if (id === "fM") m = arr.join(""); else e = arr.join(""); paint(); })); };
    bits(m, "fM"); bits(e, "fE");
    const ev = val2(e), v = decodeFp(m, e), pt = 1 + ev;
    $("#f1").textContent = ev; $("#f2").textContent = m[0] + "." + m.slice(1); $("#f3").textContent = String(+v.toPrecision(12));
    let ipb, fpb; if (pt >= m.length) { ipb = m + "0".repeat(pt - m.length); fpb = ""; } else if (pt <= 0) { ipb = "0"; fpb = "0".repeat(-pt) + m; } else { ipb = m.slice(0, pt); fpb = m.slice(pt); }
    $("#fW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Working</th></tr><tr><td>Exponent</td><td>' + e + " = " + ev + "</td></tr><tr><td>Mantissa</td><td>" + m[0] + "." + m.slice(1) + (m[0] === "1" ? " (negative)" : " (positive)") + "</td></tr><tr><td>Move the point " + Math.abs(ev) + (ev >= 0 ? " places right" : " places left") + "</td><td>" + ipb + (fpb ? "." + fpb : "") + "</td></tr><tr><td>Normalised?</td><td>" + (m[0] !== m[1] ? "yes (starts " + m[0] + m[1] + ")" : "no: the mantissa starts " + m[0] + m[1]) + "</td></tr></table></div>";
  };
  $("#fB").innerHTML = alloc.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#fB button").forEach((b, i) => (b.onclick = () => { cur = i; m = ["1011000111", "010111000110", "01110001"][i]; e = ["000111", "0111", "00000111"][i]; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  const alloc = [[10, 6], [12, 4], [8, 8]]; let cur = 0;
  const run = () => {
    $$("#gB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const x = parseFloat($("#gN").value), [mb, eb] = alloc[cur];
    if (isNaN(x)) { $("#gW").innerHTML = ""; $("#gV").textContent = "Enter a number."; return; }
    const r = encodeFp(x, mb, eb), back = decodeFp(r.m, r.e), mag = Math.abs(x);
    const maxE = 2 ** (eb - 1) - 1, over = r.ev !== undefined && (r.ev > maxE || r.ev < -(maxE + 1));
    const bin = (() => { let ip = Math.floor(mag), fr = mag - ip, s = ip.toString(2), f = ""; for (let i = 0; i < 20 && fr > 0; i++) { fr *= 2; f += fr >= 1 ? "1" : "0"; fr -= Math.floor(fr); } return s + (f ? "." + f : ""); })();
    $("#gW").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Working</th></tr><tr><td>Binary of ' + mag + "</td><td>" + bin + "</td></tr><tr><td>Exponent</td><td>" + (r.ev === undefined ? "0" : r.ev) + " → " + r.e + "</td></tr><tr><td>Mantissa</td><td>" + r.m + (x < 0 ? " (two's complement of the positive mantissa)" : "") + "</td></tr><tr><td>Answer</td><td><b>" + r.m + "  " + r.e + "</b></td></tr><tr><td>Converted back</td><td>" + +back.toPrecision(12) + "</td></tr></table></div>";
    $("#gV").textContent = over ? "The exponent does not fit in " + eb + " bits: this number is outside the range of this system (overflow or underflow)." : r.exact ? "Stored exactly." : "The number needs more bits than the " + mb + "-bit mantissa has, so the last bits are lost: the stored value is " + +back.toPrecision(12) + ", an approximation.";
  };
  $("#gB").innerHTML = alloc.map((a) => `<button class="b">${a[0]} + ${a[1]} bits</button>`).join("");
  $$("#gB button").forEach((b, i) => (b.onclick = () => { cur = i; run(); })); $("#gR").onclick = run; $("#gN").addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  run();
})();

btnTable("eB", "eO", [
  ["Mantissa", "A two's complement fraction with the binary point after the first bit; holds the digits of the number", "Normalised: starts 01 (positive) or 10 (negative)", "More mantissa bits: more precision"],
  ["Exponent", "A two's complement integer: the power of 2 the mantissa is multiplied by", "Positive moves the point right; negative moves it left", "More exponent bits: larger range"],
  ["Value", "mantissa × 2^exponent", "Example: 0.1011 × 2^3 = 5.5", "Check by converting back"]
], ["Part", "What it is", "Detail", "Effect of more bits"]);
''' + CLASSIFY("cl1", "Does each statement describe the mantissa or the exponent?", ["Mantissa", "Exponent"],
  [("Holds the digits of the number", 0), ("Says how many places to move the binary point", 1), ("Has the binary point after its first bit", 0), ("A two's complement integer", 1), ("More bits here increase precision", 0), ("More bits here increase the range", 1)],
  "Mantissa: the digits and precision. Exponent: the scale and range.") + CLASSIFY("cl2", "Which way does the binary point move (and what is the exponent's sign)?", ["Right (positive exponent)", "Left (negative exponent)"],
  [("Converting 0.101 × 2^4 to denary", 0), ("Normalising 0.000111 (a small number)", 0), ("Converting 0.101 × 2^(-2) to denary", 1), ("Writing 111.01 as 0.11101 × 2^3: the point moves left, exponent +3", 0), ("A very small number: the normalised exponent", 1), ("A large number such as 202 when normalised", 0)],
  "Evaluating with a positive exponent moves the point right. A very small number needs a negative exponent.") + ORDER(
  "Put the steps for converting −7.25 to floating-point in order.",
  ["Convert 7.25 to binary: 111.01", "Normalise: 0.11101 × 2^3, so the exponent is 3", "Write the positive mantissa: 0111010000", "Invert the bits and add 1: 1000110000", "Write the exponent 3 in two's complement: 000011"],
  "Binary, normalise, mantissa, negate, exponent.") + MATCH([
  ["Mantissa", "The digits of the number, a two's complement fraction"], ["Exponent", "The power of 2 that scales the mantissa"], ["Floating point", "A real number stored as a mantissa and an exponent"], ["Two's complement", "Representation where the first bit has a negative place value"], ["Normalised", "The mantissa starts 01 or 10"]]) + CALC([
  {"q": "Exponent 000111 in 6-bit two's complement. What is its denary value?", "a": 7, "unit": "", "tol": 0.01, "hint": "4 + 2 + 1.", "sol": "<b>7</b>."},
  {"q": "Exponent 111110 in 6-bit two's complement. What is its denary value?", "a": -2, "unit": "", "tol": 0.01, "hint": "−32 + 16 + 8 + 4 + 2.", "sol": "<b>−2</b>."},
  {"q": "Mantissa 0.1 (binary) with exponent 3. What is the value?", "a": 4, "unit": "", "tol": 0.01, "hint": "0.5 × 8.", "sol": "<b>4</b>."},
  {"q": "Mantissa 0.11 (binary) with exponent 2. What is the value?", "a": 3, "unit": "", "tol": 0.01, "hint": "0.75 × 4.", "sol": "<b>3</b>."},
  {"q": "Mantissa 0100111100 with exponent 001001. What is the denary value?", "a": 316, "unit": "", "tol": 0.01, "hint": "Move the point 9 places: 100111100.", "sol": "<b>316</b>."},
  {"q": "Mantissa 1011000111 with exponent 000111. What is the denary value?", "a": -78.25, "unit": "", "tol": 0.01, "hint": "10110001.11 = −128 + 32 + 16 + 1 + 0.5 + 0.25.", "sol": "<b>−78.25</b>."},
  {"q": "In 8-bit two's complement, what is the denary value of 10011011?", "a": -101, "unit": "", "tol": 0.01, "hint": "−128 + 16 + 8 + 2 + 1.", "sol": "<b>−101</b>."},
  {"q": "A floating-point system has 12 bits for the mantissa and 4 for the exponent. How many bytes does one number use?", "a": 2, "unit": "bytes", "tol": 0.01, "hint": "16 bits.", "sol": "<b>2</b> bytes."}]) + MCQ([
  ("Where is the binary point in a floating-point mantissa?", ["At the far right", "After the first bit", "In the middle of the exponent", "It has no point"], 1, "The mantissa is a fraction with the point after the first bit."),
  ("A mantissa starting with 1 is...", ["positive", "negative", "zero", "not normalised"], 1, "In two's complement a leading 1 means negative."),
  ("To negate a mantissa you...", ["add 1 to the exponent", "invert the bits and add 1", "remove the first bit", "double it"], 1, "Two's complement."),
  ("What does a positive exponent do?", ["Moves the point right", "Moves the point left", "Makes the number negative", "Nothing"], 0, "It multiplies by a power of 2."),
  ("How is a negative number converted to floating point?", ["Negate the mantissa and the exponent", "Convert the positive number, then take the two's complement of the mantissa only", "Subtract from 1", "Use a sign bit in the exponent"], 1, "The exponent is the same as for the positive number."),
  ("0.11101 × 2³ equals...", ["7.25", "3.625", "7", "14.5"], 0, "111.01 = 7.25.")], "qz1") + CARDS([
  ("Floating point", "Mantissa × 2^exponent, both in two's complement."), ("Mantissa", "Fraction with the point after the first bit; holds the digits."), ("Exponent", "Integer power of 2. Positive moves the point right."), ("Denary to float", "Binary, normalise, mantissa, negate if negative, exponent."),
  ("Float to denary", "Exponent, move the point, add place values."), ("Negative mantissa", "Invert bits, add 1. Exponent unchanged."), ("Normalised", "Mantissa starts 01 or 10."), ("Truncation", "Bits that do not fit are lost: precision reduced.")])

build("ac1331", "ac-13-3-1-floating-point-conversion", "Floating-point Numbers: Format and Conversion", EYA("13.3.1"),
  "The floating-point format with a two's complement mantissa and exponent, converting to and from denary with the working the exam awards marks for; animations, labs and every Paper 3 conversion question from 2021 to 2026.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.3 Floating-point numbers, representation and manipulation"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
