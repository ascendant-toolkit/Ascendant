"""AS CS 4.3: bit manipulation (shifts and masks). Run: python3 tools/artifact-kit/mk_as43.py"""
from ak42 import *

def R(before, ins, exp, mem=None):
    got = acc_after(before, ins, mem)
    assert got.replace(" ", "") == exp.replace(" ", ""), f"{before} {ins}: {got} != {exp}"
    return (sp(before.replace(" ", "")), ins, sp(exp.replace(" ", "")))

# ---- every result is calculated by the emulator and checked against the mark scheme
m_w21 = {100: 0b01010101, 101: 0b11110000, 102: 0b00001111, 103: 0, 104: 0b11111111}
T_w21 = result_table([R("01010101", "XOR 101", "10100101", m_w21), R("11110000", "AND 104", "11110000", m_w21), R("00001111", "LSL #4", "11110000", m_w21), R("11111111", "OR 102", "11111111", m_w21)])
T_s22 = result_table([R("01101101", "AND #2", "00000000"), R("01101101", "OR #8", "01101101"), R("01101101", "LSL #4", "11010000")])
m_s24a = {30: 0b01110101, 31: 255, 32: 0, 33: 0b11001100, 34: 0b10101010}
T_s24a = result_table([R("10011010", "AND 31", "10011010", m_s24a), R("10011010", "XOR B01001111", "11010101"), R("10011010", "OR #30", "10011110")])
m_s24b = {25: 0b11000110, 26: 0b11100001, 27: 0b10000001, 28: 0b11001101, 29: 0b00001111}
T_s24b = result_table([R("01000110", "XOR 29", "01001001", m_s24b), R("01000110", "AND #29", "00000100"), R("01000110", "OR B11111111", "11111111")])
m_s24c = {100: 0b00001101, 101: 0b10111110, 102: 0b11110011, 103: 0b00110111, 104: 0}
T_s24c = result_table([R("11111111", "LSL #2", "11111100", m_s24c), R("11111111", "XOR 100", "11110010", m_s24c), R("11111111", "AND 103", "00110111", m_s24c)])
T_w23 = result_table([R("01001111", "AND B10100101", "00000101"), R("00010111", "LSR #3", "00000010"), R("11110111", "XOR B00100101", "11010010")])
A24 = 0b10011010
assert format((A24 << 2) & 255, "08b") == "01101000"
assert format(((A24 + 5) & 255) & 30, "08b") == "00011110"
assert format(((A24 | 0b11110010) + 1) & 255, "08b") == "11111011"
T_w24 = '<div class="tw"><table class="t mono"><tr><th>Set</th><th>Instructions</th><th>ACC after</th></tr><tr><td>1</td><td>LSL #2</td><td><b>0110 1000</b></td></tr><tr><td>2</td><td>ADD #5, AND #30</td><td><b>0001 1110</b></td></tr><tr><td>3</td><td>OR B11110010, INC ACC</td><td><b>1111 1011</b></td></tr></table></div>'
m_w25 = {100: 0b00000011, 101: 0b10101110, 102: 0b11001100, 103: 255, 104: 0b11001100}
T_w25 = result_table([R("00001111", "AND 101", "00001110", m_w25), R("00000000", "OR #100", "01100100"), R("00000001", "XOR &F1", "11110000")])
T_w25b = result_table([R("11100011", "XOR &12", "11110001"), R("11100011", "AND #63", "00100011"), R("11100011", "OR 100", "11110011", {100: 0b00110011})])
T_s25 = result_table([R("01010101", "XOR &FE", "10101011"), R("01101011", "LSR #5", "00000011")])
R("00011110", "LSL #2", "01111000")
T_s26 = result_table([R("00110101", "LSR #3", "00000110")])
R("00110101", "AND B00000000", "00000000")
R("01100101", "OR #255", "11111111"); R("01100101", "XOR #255", "10011010"); R("01100101", "XOR #154", "11111111")
R("01111110", "LSL #3", "11110000")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Bit manipulation</b> changes individual bits of the accumulator with <b>shifts</b> and <b>bit masks</b>. A <b>logical shift</b> moves every bit left (LSL) or right (LSR) by n places and fills the gap with zeros, which multiplies (left) or divides (right) an unsigned number by powers of 2. The <b>bitwise AND, OR and XOR</b> instructions combine the ACC with a mask (the operand) one bit at a time: <b>AND</b> clears bits (and tests them), <b>OR</b> sets bits, <b>XOR</b> flips bits. The operand may be an immediate value (<span class="mono">#n</span> denary, <span class="mono">Bn</span> binary, <span class="mono">&amp;n</span> hexadecimal) or the contents of an address. Exam questions give the ACC contents and an instruction and ask for the new contents, or ask for the instruction that makes a given change.</p></div>

  <h2>1 · Shifts</h2>
  <div class="tw"><table class="t">
    <tr><th>Instruction</th><th>Effect</th><th>Example</th></tr>
    <tr><td class="mono">LSL #n</td><td>Logical shift left n places; zeros enter on the right; bits shifted off the left are lost</td><td class="mono">0001 1110 LSL #2 = 0111 1000</td></tr>
    <tr><td class="mono">LSR #n</td><td>Logical shift right n places; zeros enter on the left</td><td class="mono">0001 0111 LSR #3 = 0000 0010</td></tr>
  </table></div>
  <p>A shift left by n multiplies an unsigned value by 2<sup>n</sup> (if no bits are lost); a shift right by n divides by 2<sup>n</sup> and discards the remainder. LSL #4 on 0110 1101 gives 1101 0000: the leading 0110 is lost. The 2026 instruction set also lists <b>arithmetic</b> shifts (ASL, ASR: the sign bit is preserved on a right shift) and <b>cyclic</b> shifts (CSL, CSR: bits pushed off one end re-enter at the other); logical shifts are the ones asked for in the calculations in 2021 to 2025.</p>

  <h2>2 · Bit masks</h2>
  <div class="tw"><table class="t">
    <tr><th>Instruction</th><th>Rule for each bit</th><th>Use</th></tr>
    <tr><td class="mono">AND mask</td><td>1 only if both bits are 1</td><td><b>Clear</b> bits (mask 0 clears; mask 1 keeps), or <b>test</b> a bit</td></tr>
    <tr><td class="mono">OR mask</td><td>0 only if both bits are 0</td><td><b>Set</b> bits to 1 (mask 1 sets; mask 0 keeps)</td></tr>
    <tr><td class="mono">XOR mask</td><td>1 if the bits differ</td><td><b>Flip</b> bits (mask 1 flips; mask 0 keeps), or compare</td></tr>
  </table></div>
  <p>Worked: ACC = 0110 0101. To set every bit to 1: <span class="mono">OR #255</span> (or XOR #154, which flips just the 0 bits). To flip every bit: <span class="mono">XOR #255</span>, giving 1001 1010. To set the least significant bit to 1 and leave the rest unchanged: <span class="mono">OR #1</span> (OR B00000001). To clear the data in an 8-bit register: <span class="mono">AND B00000000</span>. To test whether a number is odd: <span class="mono">AND #1</span>, then compare the result with 1: it is true when the least significant bit is 1.</p>

  <h2>3 · Reading the operand</h2>
  <p><span class="mono">#29</span> is denary 29 (0001 1101), <span class="mono">B01001111</span> is binary and <span class="mono">&amp;12</span> is hexadecimal 12 = 0001 0010. An operand that is an address (for example <span class="mono">AND 31</span>) means the contents of address 31 are the mask. Convert the operand to 8 bits before you combine it with the ACC, and write the answer in 8 bits.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Not converting #n or &amp;n to binary first.</li>
    <li>Using the address as the mask instead of the contents of the address.</li>
    <li>Writing fewer or more than 8 bits after a shift.</li>
    <li>Using AND to set bits or OR to clear them. Remember: AND clears, OR sets, XOR flips.</li>
    <li>Saying "bit manipulation tests odd numbers" without naming the instruction, or without the comparison with 1.</li>
  </ul>
'''

watch = '''
  <h2>1 · A logical shift left</h2>
  <div id="stA"></div>
  <h2>2 · AND clears bits</h2>
  <div id="stB"></div>
  <h2>3 · XOR flips bits</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Bit calculator</h2>
  <p>Click bits of the ACC to toggle them, choose an instruction and an operand.</p>
  <div class="card"><div id="bA" class="btnrow"></div><div id="bI" class="btnrow"></div><div id="bS"></div><div id="bV" class="verdict"></div></div>
  <h2>Lab 2 · Which instruction?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
  <h2>Lab 3 · Shifts and powers of two</h2>
  <div class="card"><div id="sS"></div><div id="sV" class="verdict"></div></div>
'''

_pr, _prjs = PR(["AND, OR or XOR?", "Left or right shift?", "Match the task to the instruction", "Put the odd-number test in order", "Working out", "Multiple choice"],
  ("Which instruction does the task need?", ["AND", "OR", "XOR"], [("Clear some bits to 0", 0), ("Set some bits to 1", 1), ("Flip some bits", 2), ("Test whether the last bit is 1", 0), ("Set the least significant bit and leave the rest", 1), ("Invert every bit with mask 11111111", 2)], "AND clears and tests, OR sets, XOR flips."),
  ("Left shift or right shift?", ["LSL", "LSR"], [("Multiplies an unsigned number by 2^n", 0), ("Divides an unsigned number by 2^n", 1), ("Zeros enter on the right", 0), ("Zeros enter on the left", 1), ("Bits can be lost from the left end", 0), ("Bits can be lost from the right end", 1)], "LSL multiplies; LSR divides."),
  [["AND B00000000", "Clears the ACC to zero"], ["OR #1", "Sets the least significant bit"], ["XOR #255", "Flips every bit"], ["AND #1", "Isolates the least significant bit"], ["LSL #1", "Doubles an unsigned number"]],
  ("Put the odd-number test in order.", ["Take the number in the ACC", "Mask it with AND #1", "The result is 1 if the least significant bit is 1", "Compare the ACC with 1", "If equal, the number is odd"], "Number, mask, bit, compare, odd."),
  [{"q": "ACC = 0001 0111 (23). What denary value after LSL #2?", "a": 92, "unit": "", "tol": 0.01, "hint": "23 × 4.", "sol": "<b>92</b>."}, {"q": "ACC = 0010 1000 (40). What denary value after LSR #3?", "a": 5, "unit": "", "tol": 0.01, "hint": "40 ÷ 8.", "sol": "<b>5</b>."}, {"q": "How many bits are lost when 0110 1101 is shifted left by 4?", "a": 4, "unit": "", "tol": 0.01, "hint": "The leading four.", "sol": "<b>4</b>."}, {"q": "ACC = 1001 1010 after AND #30 (0001 1110): what denary value?", "a": 26, "unit": "", "tol": 0.01, "hint": "0001 1010.", "sol": "<b>26</b>."}, {"q": "What is &F1 in denary?", "a": 241, "unit": "", "tol": 0.01, "hint": "15 × 16 + 1.", "sol": "<b>241</b>."}],
  [("Which instruction clears bits?", ["AND", "OR", "XOR", "LSL"], 0, "AND with 0."), ("Which sets bits?", ["OR", "AND", "LSR", "CMP"], 0, "OR with 1."), ("LSL #1 on an unsigned number:", ["Doubles it", "Halves it", "Adds 1", "Clears it"], 0, "×2."), ("XOR with 1 does what to a bit?", ["Flips it", "Clears it", "Sets it", "Keeps it"], 0, "Flips."), ("AND #1 isolates:", ["The least significant bit", "The most significant bit", "The whole byte", "The carry"], 0, "LSB."), ("The operand &12 is:", ["Hexadecimal", "Binary", "Denary", "An address"], 0, "& = hex.")],
  [("LSL / LSR", "Logical shifts; zeros enter."), ("AND", "Clear or test bits."), ("OR", "Set bits."), ("XOR", "Flip bits."), ("#n / Bn / &n", "Denary / binary / hex operand."), ("Clear a register", "AND B00000000."), ("Odd test", "AND #1, compare with 1."), ("8 bits", "Always write all eight.")])

real = RWNOTE + (
rw("Pixel colours", "Image programs pull the red, green and blue values out of a packed number with AND masks and shifts, thousands of times per image.", "AND masks and LSR.") +
rw("Permissions on a file", "A set of on/off options is stored in one number; OR sets an option, AND with the opposite mask clears it, XOR toggles it.", "setting, clearing and flipping flags.") +
rw("Fast multiplying", "Shifting left by 1 doubles a number much faster than a full multiplication, so compilers use it.", "LSL = × 2.") +
rw("Checking odd or even", "A program tests the lowest bit with a mask to see whether a number is odd without dividing.", "AND #1.") +
rw("Simple encryption", "XOR a message with a key to scramble it; XOR again with the same key to get the message back.", "XOR flips bits and is reversible.")
)

where = [
  ("O/N 2021", "11, 13", "6(b)", "4", "ACC after XOR, AND, LSR and OR instructions"),
  ("O/N 2021", "12", "8(b)(i)", "4", "ACC after XOR, AND, LSL and OR instructions"),
  ("M/J 2022", "11", "6(c)", "3", "ACC after AND #2, OR #8 and LSL #4"),
  ("M/J 2022", "12", "3(a), (b), (d)", "2 + 2 + 1", "Write the instruction for a given change; a three-place logical shift"),
  ("O/N 2022", "13", "3(c)", "3", "Match instructions to their results on 00111101"),
  ("O/N 2023", "11", "8(c)", "3", "ACC after AND, LSR and XOR"),
  ("M/J 2024", "11", "4(b)", "3", "ACC after three programs"),
  ("M/J 2024", "12", "5(b)", "3", "ACC after three programs"),
  ("M/J 2024", "13", "3(b)", "3", "ACC after LSL #2, XOR and AND"),
  ("O/N 2024", "12", "8(b)", "3 + 3", "ACC after three sets; test whether the number in the ACC is odd"),
  ("O/N 2024", "13", "7(b)", "3", "Clear the data in an 8-bit register"),
  ("M/J 2025", "11", "8(b)", "1 + 1 + 1", "Set the least significant bit; XOR &FE; LSR #5"),
  ("O/N 2025", "11", "4", "1 + 1 + 1 + 1", "A binary shift; XOR &12; AND #63; OR 100"),
  ("O/N 2025", "13", "6(a)", "4", "ACC after AND, LDM, XOR and CMP"),
  ("M/J 2026", "11", "3(b)", "1 + 1", "Set the ACC to &0; LSR #3")]

past = '''  <p class="note">Bit manipulation calculations are in Paper 1 every series. Each answer here was worked out step by step by a program and matches the published mark scheme. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. Write all eight bits.</p>
''' + peq(SRC("w21", "12", "Q8(b)(i)"), "4 marks", "Complete",
  "Memory: 100: 01010101, 101: 11110000, 102: 00001111, 103: 00000000, 104: 11111111. Complete the table of the new contents of the ACC for the instructions XOR 101 (ACC = 01010101), AND 104 (ACC = 11110000), LSL #4 (ACC = 00001111), OR 102 (ACC = 11111111).", "Use the contents of the address as the mask.",
  "<p>" + mks(["1010 0101", "1111 0000", "1111 0000", "1111 1111"]) + "</p>" + T_w21, "Using the address 101 as the number. The mask is the contents of address 101.") + peq(SRC("s22", "11", "Q6(c)"), "3 marks", "Complete",
  "The ACC holds 0110 1101. Complete the register to show the result after (i) AND #2, (ii) OR #8, (iii) LSL #4.", "#2 is 0000 0010; #8 is 0000 1000.",
  "<p>" + mks(["(i) 0000 0000", "(ii) 0110 1101", "(iii) 1101 0000"]) + "</p>" + T_s22, "Forgetting that OR #8 changes nothing here: bit 3 is already 1.") + peq(SRC("s22", "12", "Q3(a)(b)(d)"), "2 + 2 + 1 marks", "Write / Show",
  "The ACC holds 0110 0101. (a) Write the bit manipulation instruction that would change it to 1111 1111. (b) Write the instruction that would change it to 1001 1010. (d) Show the result of a three-place logical shift to the left on 0111 1110.", "OR #255; XOR #255; LSL #3.",
  "<p><b>(a)</b> " + mks(["OR #255 (or OR #154, or XOR #154): the opcode and the matching operand"]) + "</p><p><b>(b)</b> " + mks(["XOR #255: the opcode and the matching operand"], "a") + "</p><p><b>(d)</b> " + mks(["1111 0000"], "b") + "</p>", "Writing a binary answer or a shift for (a). The mask for (b) must flip every bit.") + peq(SRC("w22", "13", "Q3(c)"), "3 marks", "Match",
  "The binary value 00111101 is stored in address 200. Each instruction is performed on the data in 200. Draw one line from each instruction to its result: XOR B11110000; OR B01010101; AND B11111111. Results: 01111101, 00111101, 11111111, 11000010, 11001101.", "Work each one bit by bit.",
  "<p>" + mks(["XOR B11110000 gives 11001101", "OR B01010101 gives 01111101", "AND B11111111 gives 00111101"]) + "</p>", None) + peq(SRC("w23", "11", "Q8(c)"), "3 marks", "Show",
  "Show the contents of the ACC after: (i) AND B10100101 when the ACC holds 0100 1111; (ii) LSR #3 when the ACC holds 0001 0111; (iii) XOR B00100101 when the ACC holds 1111 0111.", "AND keeps only bits where both are 1.",
  "<p>" + mks(["(i) 0000 0101", "(ii) 0000 0010", "(iii) 1101 0010"]) + "</p>" + T_w23, None) + peq(SRC("s24", "11", "Q4(b)"), "3 marks", "Complete",
  "Memory: 30: 01110101, 31: 11111111, 32: 00000000, 33: 11001100, 34: 10101010. The ACC holds 10011010 before each program. Write the ACC after: (1) AND 31; (2) XOR B01001111; (3) OR #30.", "AND with 11111111 changes nothing.",
  "<p>" + mks(["1: 1001 1010", "2: 1101 0101", "3: 1001 1110"]) + "</p>" + T_s24a, None) + peq(SRC("s24", "12", "Q5(b)"), "3 marks", "Complete",
  "Memory: 25: 11000110, 26: 11100001, 27: 10000001, 28: 11001101, 29: 00001111. The ACC holds 01000110 before each program. Write the ACC after: (1) XOR 29; (2) AND #29; (3) OR B11111111.", "#29 is 0001 1101.",
  "<p>" + mks(["1: 0100 1001", "2: 0000 0100", "3: 1111 1111"]) + "</p>" + T_s24b, None) + peq(SRC("s24", "13", "Q3(b)"), "3 marks", "Complete",
  "Memory: 100: 00001101, 101: 10111110, 102: 11110011, 103: 00110111, 104: 00000000. The ACC holds 11111111 before each instruction. Write the ACC after: (1) LSL #2; (2) XOR 100; (3) AND 103.", "XOR with all 1s flips the bits of the mask.",
  "<p>" + mks(["1: 1111 1100", "2: 1111 0010", "3: 0011 0111"]) + "</p>" + T_s24c, None) + peq(SRC("w24", "12", "Q8(b)"), "3 + 3 marks", "Complete / Explain",
  "The ACC holds 10011010 before each set of instructions: (1) LSL #2; (2) ADD #5, AND #30; (3) OR B11110010, INC ACC. (i) Complete the ACC after each set. (ii) Explain how bit manipulation can be used to test whether the binary number in the ACC is odd, and write the instruction.", "Set 2: add 5 first (1001 1111), then mask. AND #1 and compare with 1.",
  "<p><b>(i)</b> " + mks(["1: 0110 1000 after LSL #2 (the published answer shows the result of the first instruction: 0110 1000)", "2: 0001 1110 after AND #30, then 1111 1010 after OR B11110010", "3: 1111 1011 after INC ACC"]) + "</p><p><b>(ii)</b> " + mks(["An odd binary number has a 1 in the least significant bit", "A bit manipulation operation (a mask) isolates the LSB and clears the others", "Compare the result with denary 1; it is true if the number is odd"], "a") + " <b>Instruction:</b> " + mks(["AND B00000001 (or AND #1, or AND &01)"], "b") + "</p>", "Writing a mask that does not isolate the least significant bit.") + peq(SRC("w24", "13", "Q7(b)"), "3 marks", "Explain / Write",
  "Explain how bit manipulation can be used to clear the data in an 8-bit register. Write the bit manipulation instruction that will be used.", "AND with all zeros.",
  "<p>" + mks(["A bit manipulation operation is required to set all the bits to zero", "Compare the result with 0; it is true if the register is cleared"]) + " <b>Instruction:</b> " + mks(["AND B00000000 (or AND #0, or AND &00)"], "a") + "</p>", None) + peq(SRC("s25", "11", "Q8(b)"), "1 + 1 + 1 marks", "Write",
  "(i) Write the instruction that sets the least significant bit to 1 in an 8-bit register, leaving all the other bits unchanged, for any 8-bit number. (ii) The ACC holds 0101 0101: write the result of XOR &FE. (iii) The ACC holds 0110 1011: write the result of LSR #5.", "OR with 0000 0001. &FE is 1111 1110.",
  "<p>" + mks(["(i) OR B00000001 (or OR #1, or OR &1)", "(ii) 1010 1011", "(iii) 0000 0011"]) + "</p>" + T_s25, "Using AND for (i). AND cannot set a bit.") + peq(SRC("w25", "11", "Q4"), "1 + 1 + 1 + 1 marks", "Write",
  "(a) The ACC holds 0001 1110. Write an instruction that uses a binary shift to change it to 0111 1000. The ACC holds 1110 0011 for (b) XOR &12, (c) AND #63, (d) OR 100 where address 100 holds 00110011. Write the ACC after each.", "LSL #2. &12 = 0001 0010; #63 = 0011 1111.",
  "<p>" + mks(["(a) LSL #2", "(b) 1111 0001", "(c) 0010 0011", "(d) 1111 0011"]) + "</p>" + T_w25b, None) + peq(SRC("w25", "13", "Q6(a)"), "4 marks", "Complete",
  "Memory: 100: 0000 0011, 101: 1010 1110, 102: 1100 1100, 103: 1111 1111, 104: 1100 1100. Write the ACC after each instruction: (ACC 0000 1111) AND 101; (ACC 0000 0000) LDM #100; (ACC 0000 0001) XOR &F1; (ACC 0001 0001) CMP 101.", "LDM #100 loads denary 100; CMP changes nothing.",
  "<p>" + mks(["0000 1110", "0110 0100", "1111 0000", "0001 0001 (CMP does not change the ACC)"]) + "</p>" + T_w25, "Changing the ACC after CMP. It only compares.") + peq(SRC("s26", "11", "Q3(b)"), "2 + 1 marks", "Write",
  "(i) Write the bit manipulation instruction that will set the ACC to &0. (ii) The ACC holds 0011 0101: write the result after LSR #3.", "AND with zero; shift right three.",
  "<p>" + mks(["(i) AND with 0: AND B00000000, AND &0 or AND #0 (the instruction, then the operand; no load command)", "(ii) 0000 0110"]) + "</p>" + T_s26, None)

review = req("2 marks", "State", "State the instruction that flips every bit of the ACC.", "XOR with all ones.", "<p>" + mks(["XOR", "#255 (or B11111111 or &FF)"]) + "</p>", None) + req("3 marks", "Complete", "The ACC holds 1100 1010. Write the result of (i) AND #15; (ii) OR #15; (iii) LSR #2.", "#15 = 0000 1111.", "<p>" + mks(["(i) 0000 1010", "(ii) 1100 1111", "(iii) 0011 0010"]) + "</p>" + result_table([R("11001010", "AND #15", "00001010"), R("11001010", "OR #15", "11001111"), R("11001010", "LSR #2", "00110010")]), None) + req("2 marks", "Explain", "Explain how a program can use an instruction to test whether bit 7 of the ACC is set.", "AND with a mask.", "<p>" + mks(["AND the ACC with B10000000 so every other bit is cleared", "The result is non-zero (128) only if bit 7 was 1"]) + "</p>", None) + req("2 marks", "Explain", "Explain the effect of LSL #3 on an unsigned number, and when this fails.", "× 8; bits lost.", "<p>" + mks(["It multiplies the number by 2^3 = 8", "It fails if any of the top three bits were 1: they are lost"]) + "</p>", None) + req("2 marks", "Write", "Write an instruction that sets bits 0 and 1 of the ACC to 1 and leaves the rest unchanged.", "OR with 0000 0011.", "<p>" + mks(["OR", "#3 (or B00000011)"]) + "</p>", None)

tips = tips_html([
  ("AND clears, OR sets, XOR flips.", "Say the mask value too."),
  ("Convert the operand to 8 bits.", "#n, Bn and &n are all numbers."),
  ("An address operand: use its contents.", "Not the address itself."),
  ("Write all eight bits.", "In groups of four."),
  ("Odd test: AND #1, compare with 1.", "Both parts."),
  ("LSL ×2, LSR ÷2.", "Bits can fall off the end."),
], [("a bit mask", "A value combined with the ACC to clear, set or test bits."), ("a logical shift", "Moves bits left or right and fills with zeros."), ("the least significant bit", "The rightmost bit; 1 for an odd number."), ("XOR", "1 only if the two bits differ.")],
  [("Complete", "Fill in the ACC contents."), ("Write", "Give the instruction."), ("Explain", "Reasons as well."), ("Match", "Link the instruction to its result.")]) + FC

js = AKJS + AK20JS + r'''
const BM = { AND: (a, m) => a & m, OR: (a, m) => a | m, XOR: (a, m) => a ^ m, LSL: (a, n) => (a << n) & 255, LSR: (a, n) => a >> n, CSL: (a, n) => ((a << n) | (a >> (8 - n))) & 255, CSR: (a, n) => ((a >> n) | (a << (8 - n))) & 255 };
const b8 = (n) => ("00000000" + (n & 255).toString(2)).slice(-8), g4 = (s) => s.slice(0, 4) + " " + s.slice(4);
(function () {
  const draw = (s) => { const k = Math.round(s.i); const a = "00011110"; const r = [a, "00111100", "01111000", "01111000"]; let o = ""; for (let i = 0; i < 8; i++) { const bit = r[Math.min(k, 2)][i]; o += SV.rect(30 + i * 40, 30, 34, 34, bit === "1" ? "f1" : "cell", { rx: 6 }) + SV.text(47 + i * 40, 53, bit, "lbl bd", { "text-anchor": "middle" }); }
    o += SV.text(30, 100, ["ACC = 0001 1110", "LSL #1: every bit moves one place left", "LSL #2: two places left; zeros enter on the right", "0001 1110 LSL #2 = 0111 1000 (30 × 4 = 120)"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 380, h: 120, label: "Shift left", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The ACC holds 0001 1110 (30).", s: { i: 0 } }, { cap: "<b>LSL #1</b>: each bit moves one place left, a 0 enters on the right.", s: { i: 1 } }, { cap: "<b>LSL #2</b>: two places.", s: { i: 2 } }, { cap: "The result is 0111 1000 = 120, which is 30 × 2<sup>2</sup>.", s: { i: 3 } }] });
})();
(function () {
  const A = "10011010", M = "00011110", R = "00011010";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const row = (y, t, str, on) => { o += SV.text(10, y + 22, t, "sm"); for (let i = 0; i < 8; i++) o += SV.rect(80 + i * 40, y, 34, 30, str[i] === "1" ? (on ? "f1" : "f3") : "cell", { rx: 5 }) + SV.text(97 + i * 40, y + 21, str[i], "lbl bd", { "text-anchor": "middle" }); };
    row(10, "ACC", A, false); row(50, "mask", M, false); if (k >= 1) row(90, "AND", k >= 3 ? R : R.slice(0, k * 3) + "?".repeat(8 - k * 3), true); return o; };
  Lib.stepper($("#stB"), { w: 420, h: 135, label: "AND", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "ACC = 1001 1010 and the mask is 0001 1110 (#30).", s: { i: 0 } }, { cap: "AND is 1 only when both bits are 1. A 0 in the mask <b>clears</b> that bit.", s: { i: 1 } }, { cap: "The top bits of the mask are 0, so they are cleared.", s: { i: 2 } }, { cap: "Result: 0001 1010.", s: { i: 3 } }] });
})();
(function () {
  const A = "01100101", M = "11111111", R = "10011010";
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const row = (y, t, str) => { o += SV.text(10, y + 22, t, "sm"); for (let i = 0; i < 8; i++) o += SV.rect(80 + i * 40, y, 34, 30, str[i] === "1" ? "f1" : "cell", { rx: 5 }) + SV.text(97 + i * 40, y + 21, str[i], "lbl bd", { "text-anchor": "middle" }); };
    row(10, "ACC", A); row(50, "mask", M); if (k >= 1) row(90, "XOR", k >= 2 ? R : "????????"); o += SV.text(80, 140, ["", "XOR is 1 when the bits differ", "A mask of all 1s flips every bit: XOR #255", ""][Math.min(k, 3)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 150, label: "XOR", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "ACC = 0110 0101 and the mask is 1111 1111.", s: { i: 0 } }, { cap: "XOR gives 1 when the bits <b>differ</b>.", s: { i: 1 } }, { cap: "With a mask of all 1s every bit is <b>flipped</b>: 1001 1010.", s: { i: 2 } }] });
})();

(function () {
  let acc = 0b01100101, op = "AND", opd = 0b00001111;
  const bits = $("#bA"), ops = $("#bI");
  const paint = () => { bits.querySelectorAll("button").forEach((b, i) => { const v = (acc >> (7 - i)) & 1; b.textContent = v; b.className = v ? "on" : ""; });
    const sh = ["LSL", "LSR", "CSL", "CSR"].includes(op); const n = opd & 7; const res = BM[op](acc, sh ? n : opd);
    $("#bS").innerHTML = `<div class="mono">ACC &nbsp;&nbsp;${g4(b8(acc))}<br>${op} ${sh ? "#" + n : "B" + g4(b8(opd))}<br><b>result ${g4(b8(res))}</b> (denary ${res})</div>`;
    $("#bV").innerHTML = op === "AND" ? "AND keeps a bit only where the mask has a 1: it <b>clears</b> the others." : op === "OR" ? "OR sets a bit wherever the mask has a 1." : op === "XOR" ? "XOR flips the bits where the mask has a 1." : op === "LSL" ? "Logical shift left: zeros enter on the right; bits shifted off the left are lost." : op === "LSR" ? "Logical shift right: zeros enter on the left." : "Cyclic shift: bits pushed off one end come back on the other."; };
  for (let i = 0; i < 8; i++) { const b = document.createElement("button"); b.onclick = () => { acc ^= 1 << (7 - i); paint(); }; bits.appendChild(b); }
  ["AND", "OR", "XOR", "LSL", "LSR", "CSL", "CSR"].forEach((o) => { const b = document.createElement("button"); b.textContent = o; b.onclick = () => { op = o; ops.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (o === op) b.className = "on"; ops.appendChild(b); });
  Lib.slider($("#bS").parentNode.insertBefore(document.createElement("div"), $("#bS")), { id: "bo", label: "Operand (0 to 255; for shifts the low 3 bits) ", min: 0, max: 255, value: opd, fmt: (x) => x, onInput: (v) => { opd = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["Set the least significant bit and leave the rest", "OR #1", "OR sets bits"],
  ["Clear the register", "AND B00000000", "AND with 0 clears"],
  ["Flip every bit", "XOR #255", "XOR with 1 flips"],
  ["Test whether a number is odd", "AND #1 then compare with 1", "Isolate the LSB"],
  ["Multiply by 8", "LSL #3", "2^3"],
  ["Divide by 4", "LSR #2", "2^2"]
], ["Task", "Instruction", "Why"]);
(function () {
  let n = 12, k = 2; const paint = () => { $("#sV").innerHTML = `LSL #${k}: ${n} × 2<sup>${k}</sup> = <b>${n << k}</b>` + (((n << k) > 255) ? " (too big for 8 bits: the top bits are lost, so the 8-bit result is <b>" + ((n << k) & 255) + "</b>)" : "") + `.<br>LSR #${k}: ${n} ÷ 2<sup>${k}</sup> = <b>${n >> k}</b> (the remainder is discarded).`; };
  Lib.slider($("#sS").appendChild(document.createElement("div")), { id: "s1", label: "Number ", min: 0, max: 255, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } });
  Lib.slider($("#sS").appendChild(document.createElement("div")), { id: "s2", label: "Shift places ", min: 0, max: 7, value: k, fmt: (x) => x, onInput: (v) => { k = v; paint(); } }); paint();
})();
''' + _prjs

finish("as-4-3-bit-manipulation", "as43", "Bit Manipulation: Shifts and Masks",
  "Logical shifts and the AND, OR and XOR masks, clearing, setting, flipping and testing bits, with animations, a bit calculator and the real Paper 1 questions from 2021 to 2026.",
  "4.3", "4 · Processor fundamentals", "section 4.3 Bit manipulation", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on bit manipulation (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
