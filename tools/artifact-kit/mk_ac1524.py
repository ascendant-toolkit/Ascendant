"""A Level CS syllabus 15.2.4: Karnaugh maps. Run: python3 tools/artifact-kit/mk_ac1524.py"""
from ak15 import *

A4, A3 = list("ABCD"), list("ABC")


def kq(mins, names):
    """The empty map printed on the paper."""
    return kmap(mins, names, blank=True)


def terms(expr_list):
    return " + ".join(expr_list)


# every answer below is checked against the groups printed in the mark schemes
for m, n, e in [([9, 11, 12, 13, 14, 15], A4, ["A.B", "A.D"]), ([4, 5, 8, 9, 12, 13], A4, ["B.~C", "A.~C"]), ([0, 1, 4, 5, 12, 13], A4, ["~A.~C", "B.~C"]), ([0, 1, 2, 3, 6, 7], A4, ["~A.~B", "~A.C"]),
                ([0, 1, 4, 5, 6, 7], A3, ["A", "~B"]), ([1, 3, 9, 11, 13, 15], A4, ["~B.D", "A.D"]), ([0, 5, 7, 8, 13, 15], A4, ["B.D", "~B.~C.~D"]), ([2, 3, 4, 10, 11, 12], A4, ["~B.C", "B.~C.~D"]),
                ([1, 4, 5, 6, 7, 9, 12, 13, 14, 15], A4, ["B", "~C.D"]), ([3, 5, 7, 11, 12, 13, 14, 15], A4, ["A.B", "B.D", "C.D"]), ([2, 3, 5, 6], A3, ["~A.B", "B.~C", "A.~B.C"]), ([1, 3, 5, 6], A3, ["~A.C", "~B.C", "A.B.~C"]),
                ([1, 5, 7, 10, 11, 13, 14, 15], A4, ["~A.~C.D", "B.D", "A.C"]), ([4, 5, 6, 7, 12, 14], A4, ["~A.B", "B.~D"])]:
    chk(m, n, e)

EX1 = [3, 5, 7, 11, 12, 13, 14, 15]
EX3 = [2, 3, 5, 6]

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>Karnaugh map</b> (K-map) is a grid that shows a truth table so that <b>neighbouring cells differ in exactly one input</b>, which makes simplification a matter of drawing loops instead of using Boolean algebra. The rows and columns are labelled in <b>Gray code</b> (00, 01, 11, 10), not in binary order. You <b>loop groups of 1s</b> in sizes 1, 2, 4, 8 or 16, as large as possible, and the loops may wrap round the edges. Each loop becomes one AND term made of the inputs that <b>do not change</b> inside the loop, and the terms are joined with OR to give the <b>simplified sum-of-products</b>. A K-map is guaranteed to give an optimal sum-of-products, which is why the exam uses it.</p></div>

  <h2>1 · The layout</h2>
  <p>With four inputs the columns are A B and the rows are C D. The number in each cell is the row number of the truth table (A is the most significant bit), so cell 11 is row 1011.</p>
  ''' + kmap(list(range(16)), A4, layout=True) + '''
  <p>With three inputs the paper puts <b>A down the side</b> and <b>B C across the top</b>:</p>
  ''' + kmap(list(range(8)), A3, layout=True) + '''
  <p>Gray code matters: going from 01 to 11 changes only A, and going from 11 to 10 changes only B, so any two cells side by side differ in one input. The last column (10) is also next to the first (00) because 10 and 00 differ in one bit, so the edges <b>wrap round</b>.</p>

  <h2>2 · Filling in the map</h2>
  <ul>
    <li><b>From a truth table</b>: for each row put the output value in the cell with that row's inputs. Row 1011 goes in column A B = 10 and row C D = 11.</li>
    <li><b>From a sum-of-products</b>: each full product term (every input present) is one cell, so write 1 in the cell it names and 0 everywhere else. ''' + bx("A.~B.C") + ''' is A = 1, B = 0, C = 1.</li>
    <li>Write the 0s as well: the mark scheme says "0s must be present".</li>
  </ul>

  <h2>3 · Looping the 1s</h2>
  <ol>
    <li>Every 1 must be in at least one loop.</li>
    <li>A loop is a rectangle of <b>1, 2, 4, 8 or 16</b> cells (a power of two), containing only 1s, with sides of the grid next to each other.</li>
    <li>Make each loop <b>as large as possible</b>, and use <b>as few loops</b> as possible. Loops may overlap.</li>
    <li>Loops may <b>wrap</b> round the left and right edges, round the top and bottom edges, and the four corners together make a loop of four.</li>
    <li>No diagonals.</li>
  </ol>
  <h3>Reading a loop</h3>
  <p>Look at the labels along the loop's rows and columns. An input that is <b>always 1</b> across the loop goes into the term as it is. An input that is <b>always 0</b> goes in with a bar. An input that <b>changes</b> is left out. A loop of 2 drops one input, a loop of 4 drops two, a loop of 8 drops three.</p>
  <p>Example (M/J 2026, Paper 31): the map below has 1s in rows 3, 5, 7, 11, 12, 13, 14 and 15.</p>
  ''' + kgroups(EX1, A4) + '''
  <p>The bottom row CD = 11 (loop of 4) is always C = 1, D = 1, so it gives <b>C.D</b>. The AB = 11 column (loop of 4) gives <b>A.B</b>. The block in the middle where B = 1 and D = 1 (loop of 4) gives <b>B.D</b>. Together: ''' + bx("X = A.B + B.D + C.D") + '''. Do not carry out any further simplification unless asked.</p>
  <p>A 3-input example (O/N 2025, Paper 31): the 1s are in cells 2, 3, 5 and 6.</p>
  ''' + kgroups(EX3, A3) + '''
  <p>The top row loop of two (A = 0, B = 1) gives ''' + bx("~A.B") + '''; the right-hand column loop of two (B = 1, C = 0) gives ''' + bx("B.~C") + '''; the cell A = 1, B = 0, C = 1 cannot be joined to anything, so it is a loop of one with all three inputs: ''' + bx("A.~B.C") + '''.</p>

  <h2>4 · Taking it further with algebra</h2>
  <p>Some questions then ask for the answer in its <b>simplest form</b> using Boolean algebra. Take out a common factor: ''' + bx("A.B + A.D = A.(B + D)") + ''' and ''' + bx("~A.B + B.~D = B.(~A + ~D)") + '''.</p>

  <h2>5 · Why use a K-map?</h2>
  <p>The mark scheme gives: solving logic expressions with a K-map is easier because you do not need to use Boolean algebra; it is guaranteed to give an optimal solution; it converts a complex logic problem into a simpler one. "It makes it easier" on its own does not score.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Writing the columns in binary order (00, 01, 10, 11) instead of Gray code (00, 01, 11, 10).</li>
    <li>Looping a group that is not a power of two, such as three cells.</li>
    <li>Leaving a loop smaller than it could be: a loop of 2 inside a possible loop of 4 gives a longer term.</li>
    <li>Forgetting wrap-around: the left and right columns, and the top and bottom rows, are neighbours.</li>
    <li>Putting the changing input into the term. Only the inputs that are constant inside the loop belong.</li>
    <li>Leaving out the 0s when completing the map.</li>
  </ul>
'''

watch = '''
  <h2>1 · Filling a K-map from a truth table</h2>
  <div id="stA"></div>
  <h2>2 · Drawing the loops and reading the terms</h2>
  <div id="stB"></div>
  <h2>3 · A loop that wraps round the edge</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build your own K-map</h2>
  <p>Choose 3 or 4 inputs and click cells to flip them between 0 and 1. The loops and the simplified sum-of-products update.</p>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kM"></div><div class="verdict" id="kV"></div></div>
  <h2>Lab 2 · Real past paper maps</h2>
  <p>Pick a question. The map, loops and simplified expression for it appear.</p>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pM"></div><div class="verdict" id="pV"></div></div>
  <h2>Lab 3 · Grouping size and the term</h2>
  <p>Move the slider to choose a loop size. See how many inputs each size drops.</p>
  <div class="card"><div id="gS"></div><div id="gO"></div></div>
'''

practise = '''
  <h2>1 · Is this a valid loop?</h2><div id="cl1" class="card"></div>
  <h2>2 · Read the term from the loop</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the loop to its term</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps for using a K-map in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Designing a chip with fewer gates", "Chip designers simplify the control logic. A K-map turns the truth table of a small circuit into the smallest set of AND and OR terms, so fewer gates are used.", "a simplified sum-of-products needs fewer gates.") +
rw("A seven-segment display", "Each segment of a digit display lights for certain values of four input bits. A K-map for each segment gives the simplest wiring from the 4-bit number to the segment.", "four inputs, a 4 by 4 K-map.") +
rw("Traffic light and lift controllers", "The logic that decides when to change lights or open a door has many inputs. Simplifying with K-maps reduces cost and removes unneeded conditions.", "fewer terms, fewer wires, fewer faults.") +
rw("Don't-care conditions", "Some input combinations never happen. Designers can loop those cells with the 1s to get larger groups and simpler logic. (The exam does not ask this.)", "larger loops give simpler terms.") +
rw("Checking an answer", "If you are not sure your loops are right, write the truth table for your simplified expression and compare it with the original.", "the two truth tables must match.")
)

where = [
  ("O/N 2021", "31, 32", "7(b)", "2 + 2 + 2 + 1", "K-map from a truth table, loops, simplified sum-of-products, simplest form"),
  ("O/N 2022", "31, 33", "7", "2 + 2 + 3", "K-map from a sum-of-products, loops, simplified and simplest form"),
  ("M/J 2023", "31, 33", "7", "2 + 2 + 2 + 1", "K-map from a sum-of-products, loops, simplified and simplest form"),
  ("M/J 2023", "32", "9(b)-(e)", "2 + 2 + 2 + 1", "K-map from a truth table, loops, simplified and simplest form"),
  ("M/J 2024", "31", "6(c)", "2 + 2 + 1", "Three-input K-map from a sum-of-products, loops, simplified"),
  ("M/J 2024", "32, 33", "6(c)", "2 + 2 + 1", "Three-input K-map for a different expression each; same format"),
  ("O/N 2024", "31, 33", "7(b)-(d)", "2 + 2 + 2 + 1", "K-map from a truth table, loops, simplified and simplest form"),
  ("O/N 2024", "32", "6(b)-(d)", "2 + 2 + 2", "K-map from a truth table, loops, simplified sum-of-products"),
  ("M/J 2025", "31, 33", "5(b), 3(b)", "2 + 2 + 2", "K-map from a truth table (a different table in each paper), loops, simplified"),
  ("O/N 2025", "31, 32", "6(b)", "2 + 2 + 2", "Three-input K-map from a sum-of-products, loops, simplified"),
  ("O/N 2025", "33", "6(a)", "3 + 2", "Given K-map: loops, simplified sum-of-products"),
  ("M/J 2026", "31", "6(b), (c)", "1 + 3 + 2", "Benefit of a K-map; loops and simplified sum-of-products from a given map"),
  ("M/J 2026", "32", "7(a)", "2 + 2 + 1", "K-map from a truth table, loops, simplified"),
  ("M/J 2026", "33", "6(a)", "2 + 2 + 1", "Given K-map: loops, simplified, simplest form by algebra")]

TT21, TT23, TT25, TT24 = [9, 11, 12, 13, 14, 15], [0, 1, 2, 3, 6, 7], [0, 5, 7, 8, 13, 15], [1, 3, 9, 11, 13, 15]


def expr(mins, names, order=None):
    return " + ".join(term("".join(map(str, bits(m, len(names)))), names) for m in (order or sorted(mins)))


past = '''  <p class="note">K-maps are examined in Paper 3 in every series from May/June 2021 to May/June 2026, almost always after a truth table or sum-of-products. The 3-input layout used since 2024 has A down the side. The questions below are reworded from the papers; maps are redrawn. Where a mark scheme gives a loop picture, the loops here are the same groups. Check the original paper and mark scheme for the exact wording.</p>

  <h3>From a truth table</h3>
''' + peq(SRC("w21", "31/32", "Q7(b)"), "2 + 2 + 2 + 1 marks", "Complete / Draw / Write",
  "Here is the truth table for Z (rows with Z = 1 are 1001, 1011, 1100, 1101, 1110 and 1111)." + tt_from_mins(A4, "Z", TT21) + "(b)(i) Complete the Karnaugh map (K-map) for the given truth table. (ii) Draw loop(s) around appropriate group(s) of 1s in the K-map to produce an optimal sum-of-products. (iii) Write the Boolean expression from your answer to (ii) as a simplified sum-of-products. (iv) Write the simplified Boolean expression for your answer to (iii)." + kq(TT21, A4),
  "Gray code 00 01 11 10. Ring the AB = 11 column (four 1s) and the block AB = 1x, D = 1.",
  "<p><b>(i)</b> " + mks(["Every two correct rows or columns, up to two marks"]) + "</p>" + kmap(TT21, A4) + "<p><b>(ii)</b> " + mks(["One mark for each correct loop (max 2)"]) + "</p>" + kgroups(TT21, A4) + "<p><b>(iii)</b> Z = " + bx("A.B + A.D") + " " + mks(["A.B", "A.D"]) + "<br><b>(iv)</b> Z = " + bx("A.(B + D)") + " " + mks(["common factor A taken out"], "a") + "</p>", "Looping the 1s in column 11 and the 1s in column 10 separately, giving more terms. The loop A.D covers cells in two columns, 11 and 10.") + peq(SRC("s23", "32", "Q9(b)-(e)"), "2 + 2 + 2 + 1 marks", "Complete / Draw / Write",
  "A truth table with Z = 1 for the rows 0000, 0001, 0010, 0011, 0110 and 0111 represents a logic circuit." + tt_from_mins(A4, "Z", TT23) + "(b) Complete the K-map for the given truth table. (c) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (d) Write the Boolean logic expression from your answer to part (c) as a simplified sum-of-products. (e) Use Boolean algebra to give your answer to part (d) in its simplest form." + kq(TT23, A4),
  "Two loops of four. Take ~A out at the end.",
  "<p><b>(b)</b> " + mks(["Two marks if no errors; one mark if one error"]) + "</p>" + kmap(TT23, A4) + "<p><b>(c)</b> " + mks(["One correct loop", "A second correct loop"]) + "</p>" + kgroups(TT23, A4) + "<p><b>(d)</b> Z = " + bx("~A.~B + ~A.C") + " " + mks(["~A.~B", "~A.C"]) + "<br><b>(e)</b> Z = " + bx("~A.(~B + C)") + " " + mks(["common factor ~A taken out"], "a") + "</p>", "Missing the loop that makes ~A.C: cells 0011, 0010, 0111 and 0110 form a block of four, with C = 1 and A = 0, and a loop of two would give a longer term.") + peq(SRC("w24", "31/33", "Q7(b)-(d)"), "2 + 2 + 2 + 1 marks", "Complete / Draw / Write",
  "The truth table for a logic circuit has T = 1 for rows 0001, 0011, 1001, 1011, 1101 and 1111." + tt_from_mins(A4, "T", TT24) + "(b) Complete the K-map. (c) Draw loop(s) to produce an optimal sum-of-products. (d)(i) Write the Boolean logic expression from your answer to (c) as the simplified sum-of-products. (ii) Use Boolean algebra to write your answer to (d)(i) in its simplest form." + kq(TT24, A4),
  "D = 1 in every row with T = 1. One loop wraps across the 00 and 10 columns.",
  "<p><b>(b)</b> " + mks(["Two marks if no errors; one mark for one error"]) + "</p>" + kmap(TT24, A4) + "<p><b>(c)</b> " + mks(["Loop of four for ~B.D (columns 00 and 10, which wrap round)", "Loop of four for A.D (columns 11 and 10)"]) + "</p>" + kgroups(TT24, A4) + "<p><b>(d)(i)</b> T = " + bx("~B.D + A.D") + "<br><b>(ii)</b> T = " + bx("D.(~B + A)") + " " + mks(["common factor D taken out"], "a") + "</p>", "Not noticing that columns 00 and 10 are neighbours. The loop for ~B.D needs the wrap-around.") + peq(SRC("s25", "31", "Q5(b)"), "2 + 2 + 2 marks", "Complete / Draw / Write",
  "This truth table represents a logic circuit (Z = 1 in rows 0000, 0101, 0111, 1000, 1101 and 1111)." + tt_from_mins(A4, "Z", TT25) + "(b)(i) Complete the K-map for the given truth table. (ii) Draw loop(s) around appropriate group(s) to produce an optimal sum-of-products. (iii) Write the Boolean logic expression from your answer to (b)(ii) as the simplified sum-of-products." + kq(TT25, A4),
  "A block of four in the middle and a pair that wraps round the edge.",
  "<p><b>(i)</b> " + mks(["Two marks if no errors; one if one error"]) + "</p>" + kmap(TT25, A4) + "<p><b>(ii)</b> " + mks(["One mark per correct loop (max 2)"]) + "</p>" + kgroups(TT25, A4) + "<p><b>(iii)</b> Z = " + bx("B.D + ~B.~C.~D") + " " + mks(["B.D", "~B.~C.~D"]) + "</p>", "Leaving the 1s in cells 0000 and 1000 as two separate loops of one. They are neighbours across the wrap, so they make a loop of two.") + peq(SRC("s25", "33", "Q3(b)"), "2 + 2 + 2 marks", "Complete / Draw / Write",
  "This truth table represents a logic circuit (Z = 1 in rows 0010, 0011, 0100, 1010, 1011 and 1100)." + tt_from_mins(A4, "Z", [2, 3, 4, 10, 11, 12]) + "(b)(i) Complete the K-map. (ii) Draw loop(s) to produce an optimal sum-of-products. (iii) Write the Boolean logic expression as the simplified sum-of-products." + kq([2, 3, 4, 10, 11, 12], A4),
  "The pair 0100 and 1100 are neighbours.",
  "<p><b>(i)</b> " + mks(["Two marks if no errors; one if one error"]) + "</p>" + kmap([2, 3, 4, 10, 11, 12], A4) + "<p><b>(ii)</b> " + mks(["One mark per correct loop"]) + "</p>" + kgroups([2, 3, 4, 10, 11, 12], A4) + "<p><b>(iii)</b> Z = " + bx("~B.C + B.~C.~D") + "</p>", None) + peq(SRC("s26", "32", "Q7(a)"), "2 + 2 + 1 marks", "Complete / Draw / Write",
  "This truth table represents a logic circuit (Z = 1 in rows 0001, 0100 to 0111, 1001 and 1100 to 1111)." + tt_from_mins(A4, "Z", [1, 4, 5, 6, 7, 9, 12, 13, 14, 15]) + "(a)(i) Complete the K-map. (ii) Draw loop(s) to produce an optimal sum-of-products. (iii) Write the Boolean expression from your answer to 7(a)(ii) as a simplified sum-of-products." + kq([1, 4, 5, 6, 7, 9, 12, 13, 14, 15], A4),
  "The two middle columns (AB = 01 and 11) are all 1s: a loop of eight.",
  "<p><b>(i)</b> " + mks(["Two marks if no errors present (the 0s must be present); one mark if one error"]) + "</p>" + kmap([1, 4, 5, 6, 7, 9, 12, 13, 14, 15], A4) + "<p><b>(ii)</b> " + mks(["Loop of eight: the columns AB = 01 and 11", "Loop of four: the row CD = 01, wrapping the columns 00 and 10"]) + "</p>" + kgroups([1, 4, 5, 6, 7, 9, 12, 13, 14, 15], A4) + "<p><b>(iii)</b> Z = " + bx("B + ~C.D") + " " + mks(["B (loop of eight drops A, C and D)"]) + "</p>", "Writing four terms for the two middle columns. A loop of eight gives one term with three inputs dropped: B.") + '''
  <h3>From a sum-of-products</h3>
''' + peq(SRC("w22", "31/33", "Q7"), "2 + 2 + 3 marks", "Complete / Draw / Write",
  "(a) Complete the K-map for the Boolean expression Z = " + bx(expr([4, 5, 12, 13, 8, 9], A4, [4, 5, 12, 13, 8, 9])) + ". (b) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (c) Write the Boolean expression from your answer to (b) as a simplified sum-of-products. Use Boolean algebra to give your answer in its simplest form." + kq([4, 5, 12, 13, 8, 9], A4),
  "Six terms: cells 4, 5, 12, 13, 8, 9. All have C = 0.",
  "<p><b>(a)</b> " + mks(["Two marks if no errors; one mark if one error"]) + "</p>" + kmap([4, 5, 8, 9, 12, 13], A4) + "<p><b>(b)</b> " + mks(["One mark for each correct loop (two loops of four that overlap)"]) + "</p>" + kgroups([4, 5, 8, 9, 12, 13], A4) + "<p><b>(c)</b> Simplified: Z = " + bx("B.~C + A.~C") + "<br>Simplest form: Z = " + bx("~C.(A + B)") + " " + mks(["B.~C", "A.~C", "common factor ~C"], "a") + "</p>", "Ringing all six 1s as one group. Six is not a power of two. Use two overlapping groups of four.") + peq(SRC("s23", "31/33", "Q7"), "2 + 2 + 2 + 1 marks", "Complete / Draw / Write",
  "(a) Complete the K-map for the Boolean expression Z = " + bx(expr([0, 1, 4, 5, 12, 13], A4, [0, 1, 4, 5, 12, 13])) + ". (b) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (c) Write the Boolean logic expression from your answer to (b) as a simplified sum-of-products. (d) Use Boolean algebra to give your answer to (c) in its simplest form." + kq([0, 1, 4, 5, 12, 13], A4),
  "All six terms have C = 0 and D either value, so the loops are across the CD = 00 and 01 rows.",
  "<p><b>(a)</b> " + mks(["Two marks if no errors; one mark if one error"]) + "</p>" + kmap([0, 1, 4, 5, 12, 13], A4) + "<p><b>(b)</b> " + mks(["One mark for each correct loop (max 2)"]) + "</p>" + kgroups([0, 1, 4, 5, 12, 13], A4) + "<p><b>(c)</b> Z = " + bx("~A.~C + B.~C") + "<br><b>(d)</b> Z = " + bx("~C.(~A + B)") + " " + mks(["~A.~C", "B.~C"]) + " " + mks(["~C.(~A + B)"], "a") + "</p>", None) + peq(SRC("w25", "31", "Q6(b)"), "2 + 2 + 2 marks", "Complete / Draw / Write",
  "(i) Complete the K-map for the Boolean expression " + bx(expr([3, 2, 5, 6], A3, [3, 2, 5, 6])) + ". (ii) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (iii) Write the Boolean expression from your answer to part b(ii) as a simplified sum-of-products. Do not carry out any further simplification." + kq([2, 3, 5, 6], A3),
  "A is down the side, B C across the top in Gray code.",
  "<p><b>(i)</b> " + mks(["Two marks if no errors; one mark if one error"]) + "</p>" + kmap([2, 3, 5, 6], A3) + "<p><b>(ii)</b> " + mks(["One mark for each correct loop (max 2)"]) + "</p>" + kgroups([2, 3, 5, 6], A3) + "<p><b>(iii)</b> " + bx("~A.B + B.~C + A.~B.C") + " " + mks(["One correct term with a + sign", "All the terms and operators correct with none extra"]) + "</p>", "Putting the columns in order 00, 01, 10, 11. In Gray code the third column is 11 and the fourth is 10.") + peq(SRC("w25", "32", "Q6(b)"), "2 + 2 + 2 marks", "Complete / Draw / Write",
  "(i) Complete the K-map for the Boolean expression " + bx(expr([1, 3, 5, 6], A3, [1, 3, 5, 6])) + ". (ii) Draw loop(s) to produce an optimal sum-of-products. (iii) Write the Boolean expression from your answer to part b(ii) as a simplified sum-of-products. Do not carry out any further simplification." + kq([1, 3, 5, 6], A3),
  "Two loops of two share the cell 001. The cell 110 stands alone.",
  "<p><b>(i)</b> " + mks(["Two marks if no errors; one mark if one error"]) + "</p>" + kmap([1, 3, 5, 6], A3) + "<p><b>(ii)</b> " + mks(["One mark for each correct loop (max 2)"]) + "</p>" + kgroups([1, 3, 5, 6], A3) + "<p><b>(iii)</b> " + bx("~A.C + ~B.C + A.B.~C") + " " + mks(["One correct term with a + sign", "All the terms and operators correct with none extra"]) + "</p>", "Ringing the cell 110 together with 010 that is a 0 on the map. A loop can contain only 1s.") + peq(SRC("s24", "31", "Q6(c)"), "2 + 2 + 1 marks", "Complete / Draw / Write",
  "(c)(i) Complete the K-map for the Boolean expression " + bx(expr([0, 1, 4, 5, 6, 7], A3, [0, 1, 4, 5, 6, 7])) + ". (ii) Draw loop(s) around appropriate group(s) to produce an optimal sum-of-products. (iii) Write the Boolean expression from your answer to part (c)(ii) as a simplified sum-of-products." + kq([0, 1, 4, 5, 6, 7], A3),
  "The A = 1 row is all 1s: a loop of four.",
  "<p><b>(i)</b> " + mks(["Two marks if all correct; one mark if one error"]) + "</p>" + kmap([0, 1, 4, 5, 6, 7], A3) + "<p><b>(ii)</b> " + mks(["One mark for each correct loop (max 2)"]) + "</p>" + kgroups([0, 1, 4, 5, 6, 7], A3) + "<p><b>(iii)</b> Z = " + bx("A + ~B") + " " + mks(["A + ~B"]) + "</p>", "Writing A.B + A.~B + ... The bottom row is a loop of four, which drops B and C to give just A.") + '''
  <h3>Given a K-map</h3>
''' + peq(SRC("s26", "31", "Q6(b)(c)"), "1 + 3 + 2 marks", "Describe / Draw / Write",
  "(b) Describe one benefit of using a Karnaugh map (K-map) for solving logic problems. (c) The K-map represents a logic circuit with four inputs. (i) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (ii) Write the Boolean expression from your answer to 6(c)(i) as a simplified sum-of-products. Do not carry out any further simplification." + kmap(EX1, A4),
  "Three loops of four. Any two overlapping loops are allowed.",
  "<p><b>(b)</b> " + mks(["It makes solving logic expressions easier because you do not need Boolean algebra, or it is guaranteed to give an optimal solution, or it converts complex logic problems into simpler ones"]) + "</p><p><b>(c)(i)</b> " + mks(["Loop for C.D (the CD = 11 row)", "Loop for A.B (the AB = 11 column)", "Loop for B.D"]) + "</p>" + kgroups(EX1, A4) + "<p><b>(ii)</b> " + bx("A.B + B.D + C.D") + " " + mks(["One correct term", "All three terms joined by + with nothing extra"]) + "</p>", "Saying only 'it makes it easier'. That does not score on its own: give a reason, such as no Boolean algebra needed or guaranteed optimal.") + peq(SRC("w25", "33", "Q6(a)"), "3 + 2 marks", "Draw / Write",
  "(a) The K-map represents a logic circuit with four inputs. (i) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (ii) Write the Boolean expression from your answer to a(i) as a simplified sum-of-products." + kmap([1, 5, 7, 10, 11, 13, 14, 15], A4),
  "Three groups of four. Two of them overlap in the cell 1111.",
  "<p><b>(i)</b> " + mks(["Loop for ~A.~C.D (cells 0001 and 0101: a pair)", "Loop of four for B.D", "Loop of four for A.C"]) + "</p>" + kgroups([1, 5, 7, 10, 11, 13, 14, 15], A4) + "<p><b>(ii)</b> " + bx("~A.~C.D + B.D + A.C") + " " + mks(["One correct term with a + sign", "All three terms correct with nothing extra"]) + "</p>", None) + peq(SRC("s26", "33", "Q6(a)"), "2 + 2 + 1 marks", "Draw / Write",
  "(a) The K-map represents a logic circuit with four inputs. (i) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products. (ii) Write the Boolean expression from your answer to 6(a)(i) as a simplified sum-of-products. Do not carry out any further simplification. (iii) Write the Boolean expression from your answer to 6(a)(ii) in its simplest form by using Boolean algebra to simplify it." + kmap([4, 5, 6, 7, 12, 14], A4),
  "One loop of four is a whole column. The other wraps top to bottom.",
  "<p><b>(i)</b> " + mks(["Loop of four: the AB = 01 column", "Loop of four: B = 1, D = 0, wrapping the top and bottom rows"]) + "</p>" + kgroups([4, 5, 6, 7, 12, 14], A4) + "<p><b>(ii)</b> " + bx("~A.B + B.~D") + " " + mks(["One correct Boolean term", "Both terms joined by + with no others"]) + "<br><b>(iii)</b> " + bx("B.(~A + ~D)") + " " + mks(["common factor B taken out"], "a") + "</p>", "Missing the wrap-around loop: cells 0100 and 1100 (top row) and 0110 and 1110 (bottom row) are neighbours across the top and bottom edges.")

review = req("3 marks", "Complete", "A logic circuit has inputs A, B and C. The output is 1 for the inputs 000, 001, 010 and 011 and 0 otherwise. Draw the K-map (A down the side, BC across the top), loop the 1s and write the simplified expression.", "Gray code order for BC.",
  "<p>" + mks(["Map with 1s in the A = 0 row, and 0s in the A = 1 row", "One loop of four for the whole A = 0 row", "Expression: ~A"]) + "</p>" + kgroups([0, 1, 2, 3], A3), None) + req("4 marks", "Draw", "Four inputs A, B, C and D. The 1s are in the four corner cells. Draw the K-map, loop the 1s and write the simplified expression.", "The corners are neighbours across both edges.",
  "<p>" + mks(["Ones in cells 0000, 0010, 1000 and 1010", "One loop of four that wraps round the corners", "Constant inputs: B = 0 and D = 0", "Expression: ~B.~D"]) + "</p>" + kgroups([0, 2, 8, 10], A4), None) + req("2 marks", "Explain", "Explain why the K-map labels use the order 00, 01, 11, 10 instead of 00, 01, 10, 11.", "Think about neighbouring cells.",
  "<p>" + mks(["It is Gray code: only one input changes between neighbouring cells, including from the last column back to the first", "So adjacent 1s can be grouped, and the group has terms in which one input has been eliminated"]) + "</p>", None) + req("3 marks", "State", "State the rules for forming a loop on a K-map.", "Size, shape and contents.",
  "<p>" + mks(["The loop contains only 1s", "Its size is a power of two: 1, 2, 4, 8 or 16, and it is a rectangle with no diagonals", "Loops should be as large as possible; they may overlap and may wrap round the edges"]) + "</p>", None) + req("3 marks", "Describe", "A loop of four covers the cells with A = 1 and B = 1, for every value of C and D. State its term and the number of inputs it drops.", "Which inputs are constant?",
  "<p>" + mks(["A is always 1 and B is always 1, so the term contains both", "C and D change inside the loop, so they are left out", "Term A.B: two inputs dropped"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on Karnaugh maps (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Gray code order.", "Label columns and rows 00, 01, 11, 10."),
  ("Write the 0s.", "The mark scheme says 0s must be present."),
  ("Loop only 1s, in powers of two.", "1, 2, 4, 8 or 16. Large loops, few loops."),
  ("Check the edges.", "Left and right edges, top and bottom, and the four corners wrap round."),
  ("Constant inputs go in the term.", "Always 1: plain. Always 0: barred. Changing: left out."),
  ("Do not simplify further unless asked.", "'Do not carry out any further simplification'."),
], [
  ("a K-map", "A grid of the truth table in Gray code order so that neighbouring 1s can be looped to simplify a sum-of-products."),
  ("Gray code", "An order of binary numbers in which neighbours differ in one bit."),
  ("a loop of four", "Drops two inputs, so its term has two fewer inputs."),
  ("the benefit of a K-map", "Easier than Boolean algebra and guaranteed to give an optimal solution."),
], [("Complete", "Fill in every cell, including 0s."), ("Draw", "Loop the groups of 1s on the map."), ("Write", "Give the sum-of-products from your loops."), ("Describe", "Give a benefit with a reason.")]) + FC

PRE = [
  ("M/J 2026 P31 6(c)", A4, EX1), ("M/J 2026 P32 7(a)", A4, [1, 4, 5, 6, 7, 9, 12, 13, 14, 15]), ("M/J 2026 P33 6(a)", A4, [4, 5, 6, 7, 12, 14]), ("O/N 2025 P33 6(a)", A4, [1, 5, 7, 10, 11, 13, 14, 15]),
  ("O/N 2025 P31 6(b)", A3, [2, 3, 5, 6]), ("O/N 2025 P32 6(b)", A3, [1, 3, 5, 6]), ("M/J 2025 P31 5(b)", A4, TT25), ("O/N 2024 P31/33 7", A4, TT24), ("M/J 2023 P32 9", A4, TT23), ("O/N 2021 P31/32 7(b)", A4, TT21)]

js = AKJS + AK20JS + AK15JS + "const PRE = " + json.dumps([[n, "".join(nm), m] for n, nm, m in PRE]) + ";\n" + r'''
/* K-map drawn as SVG: o.shown = set of cells whose value is shown, o.groups = [{cells, k}] */
function kmDraw(names, mins, o) {
  const nv = names.length, cols = GRAYS, rows = nv === 4 ? GRAYS : ["0", "1"], X0 = (o.ox || 0) + 96, Y0 = (o.oy || 0) + 40, cw = 70, ch = 52; let s = "";
  const idx = (c, r) => parseInt(nv === 3 ? r + c : c + r, 2), cell = (m) => { for (let ri = 0; ri < rows.length; ri++) for (let ci = 0; ci < 4; ci++) if (idx(cols[ci], rows[ri]) === m) return [ci, ri]; };
  s += SV.text(X0 - 8, Y0 - 24, nv === 4 ? "CD \\ AB" : "A \\ BC", "sm", { "text-anchor": "end" });
  cols.forEach((c, i) => (s += SV.text(X0 + i * cw + cw / 2, Y0 - 10, c, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" })));
  rows.forEach((r, i) => (s += SV.text(X0 - 14, Y0 + i * ch + ch / 2 + 5, r, "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono)" })));
  rows.forEach((r, ri) => cols.forEach((c, ci) => { const m = idx(c, r), shown = !o.shown || o.shown.has(m); s += SV.rect(X0 + ci * cw, Y0 + ri * ch, cw, ch, "cell", { rx: 2 }) + (shown ? SV.text(X0 + ci * cw + cw / 2, Y0 + ri * ch + ch / 2 + 7, mins.includes(m) ? "1" : "0", "lbl bd", { "text-anchor": "middle", style: "font-size:22px;font-family:var(--mono)" }) : "") + SV.text(X0 + ci * cw + cw - 5, Y0 + ri * ch + ch - 5, String(m), "sm", { "text-anchor": "end", style: "font-size:9px" }); }));
  (o.groups || []).forEach((g, k) => g.cells.forEach((m) => { const [ci, ri] = cell(m); s += SV.rect(X0 + ci * cw + 3 + 3 * g.k, Y0 + ri * ch + 3 + 3 * g.k, cw - 6 - 6 * g.k, ch - 6 - 6 * g.k, "ax", { rx: 8, fill: "none", style: "stroke:" + KCOL[g.k % 6] + ";stroke-width:3" }); }));
  return s;
}
/* 1: truth table to map */
(function () {
  const names = ["A", "B", "C", "D"], mins = [0, 5, 7, 8, 13, 15], order = [0, 5, 7, 8, 13, 15];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 20, "A B C D   Z", "lbl bd", { style: "font-family:var(--mono)" });
    for (let m = 0; m < 16; m++) { const one = mins.includes(m), at = order.indexOf(m), cur = one && at === k - 1, done = one && at < k - 1; o += SV.rect(8, 28 + m * 22, 150, 20, cur ? "cell-warn" : done ? "cell-ok" : "cell", { rx: 3 }) + SV.text(14, 43 + m * 22, bitsOf(m, 4).join(" ") + "   " + (one ? 1 : 0), "lbl", { style: "font-family:var(--mono);font-size:12px" }); }
    const mm = mins.filter((m) => order.indexOf(m) < k);
    return o + kmDraw(names, mm, { ox: 170, oy: 0, shown: k === 0 ? new Set() : k === 6 ? undefined : new Set(mm) }); };
  const caps = ["Each row of the truth table has a cell on the map. Columns are A B and rows are C D, both in Gray code order.", "Row 0000 (Z = 1) goes in column AB = 00, row CD = 00.", "Row 0101 (Z = 1): AB = 01, CD = 01.", "Row 0111: AB = 01, CD = 11.", "Row 1000: AB = 10, CD = 00. This cell is at the far right of the map.", "Row 1101: AB = 11, CD = 01.", "Row 1111: AB = 11, CD = 11. All six 1s are placed; every other cell is 0."];
  Lib.stepper($("#stA"), { w: 560, h: 400, label: "Truth table to K-map", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: caps.map((c, i) => ({ cap: c, s: { i } })) });
})();
/* 2: loops on the map */
(function () {
  const names = ["A", "B", "C", "D"], mins = [3, 5, 7, 11, 12, 13, 14, 15];
  const gs = [{ cells: [3, 7, 15, 11], k: 0, t: "C.D" }, { cells: [12, 13, 15, 14], k: 1, t: "A.B" }, { cells: [5, 7, 13, 15], k: 2, t: "B.D" }];
  const draw = (s) => { const k = Math.round(s.i); let o = kmDraw(names, mins, { ox: 40, oy: 0, groups: gs.slice(0, k) });
    gs.slice(0, k).forEach((g, i) => (o += SV.text(430, 60 + i * 30, "loop " + (i + 1) + ": " + g.t.replace(/~/g, "¬"), "lbl bd", { style: "fill:" + KCOL[i] + ";font-family:var(--mono)" })));
    if (k === 3) o += SV.text(430, 160, "X = A.B + B.D + C.D", "lbl bd t3", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stB"), { w: 640, h: 300, label: "Loops", base: { i: 0 }, draw, tween: 150, dwell: 3000, steps: [{ cap: "The 1s of the map from M/J 2026 Paper 31. Look for the biggest groups.", s: { i: 0 } }, { cap: "Loop 1: the CD = 11 row is a group of four. C = 1 and D = 1 all along, A and B change: the term is <b>C.D</b>.", s: { i: 1 } }, { cap: "Loop 2: the AB = 11 column is a group of four. A = 1, B = 1, C and D change: <b>A.B</b>.", s: { i: 2 } }, { cap: "Loop 3: the block B = 1, D = 1 (cells 5, 7, 13, 15) overlaps the others: <b>B.D</b>. Every 1 is now looped. X = A.B + B.D + C.D.", s: { i: 3 } }] });
})();
/* 3: wrap-around */
(function () {
  const names = ["A", "B", "C", "D"], mins = [4, 5, 6, 7, 12, 14];
  const gs = [{ cells: [4, 5, 7, 6], k: 0 }, { cells: [4, 6, 12, 14], k: 1 }];
  const draw = (s) => { const k = Math.round(s.i); let o = kmDraw(names, mins, { ox: 40, oy: 0, groups: gs.slice(0, k) });
    if (k >= 1) o += SV.text(430, 60, "¬A.B  (column AB = 01)", "lbl bd", { style: "fill:" + KCOL[0] + ";font-family:var(--mono)" }); if (k >= 2) o += SV.text(430, 90, "B.¬D  (rows 00 and 10 wrap)", "lbl bd", { style: "fill:" + KCOL[1] + ";font-family:var(--mono)" }); if (k >= 3) o += SV.text(430, 130, "¬A.B + B.¬D = B.(¬A + ¬D)", "lbl bd t3", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stC"), { w: 700, h: 300, label: "Wrap-around", base: { i: 0 }, draw, tween: 150, dwell: 3000, steps: [{ cap: "A K-map for M/J 2026 Paper 33. The 1s in cells 4, 5, 6, 7, 12 and 14.", s: { i: 0 } }, { cap: "The whole AB = 01 column is a group of four: A = 0 and B = 1 throughout, so <b>¬A.B</b>.", s: { i: 1 } }, { cap: "Cells 4, 6, 12 and 14 form a group of four <b>that wraps</b>: the top row (CD = 00) and the bottom row (CD = 10) are neighbours. B = 1 and D = 0 throughout: <b>B.¬D</b>.", s: { i: 2 } }, { cap: "Then algebra: take out B. The simplest form is <b>B.(¬A + ¬D)</b>.", s: { i: 3 } }] });
})();

/* lab 1 */
(function () {
  let nv = 4, mins = [3, 5, 7, 11, 12, 13, 14, 15]; const b = $("#kB");
  const names = () => ["A", "B", "C", "D"].slice(0, nv);
  const paint = () => { $("#kM").innerHTML = kgroupsJS(mins, names()); $("#kM").querySelectorAll("td[data-m]").forEach((td) => (td.onclick = () => { const m = +td.dataset.m; mins = mins.includes(m) ? mins.filter((x) => x !== m) : mins.concat(m); paint(); }));
    $("#kV").innerHTML = "Simplified sum-of-products: <b>" + obJS(simpJS(mins, names())) + "</b><br>Full sum-of-products has " + mins.length + " term" + (mins.length === 1 ? "" : "s") + "."; };
  [[3, "3 inputs"], [4, "4 inputs"]].forEach(([n, t]) => { const x = document.createElement("button"); x.textContent = t; x.onclick = () => { nv = n; mins = mins.filter((m) => m < 1 << n); b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; paint(); }; b.appendChild(x); });
  const cl = document.createElement("button"); cl.textContent = "Clear"; cl.onclick = () => { mins = []; paint(); }; b.appendChild(cl); b.children[1].className = "on"; paint();
})();
/* lab 2 */
(function () {
  const b = $("#pB");
  const show = (i) => { const [n, nm, m] = PRE[i], names = nm.split(""); $("#pM").innerHTML = "<p><b>" + n + "</b></p>" + kgroupsJS(m, names); $("#pV").innerHTML = "Simplified sum-of-products: <b>" + obJS(simpJS(m, names)) + "</b>"; };
  PRE.forEach((p, i) => { const x = document.createElement("button"); x.textContent = p[0]; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
/* lab 3 */
(function () {
  let k = 2;
  const info = [["1 cell", "no inputs dropped", "a full product term, e.g. A.~B.C.D"], ["2 cells", "1 input dropped", "a term of 3 inputs"], ["4 cells", "2 inputs dropped", "a term of 2 inputs"], ["8 cells", "3 inputs dropped", "a term of 1 input"], ["16 cells", "4 inputs dropped", "the constant 1"]];
  const paint = () => { const [a, b, c] = info[k]; $("#gO").innerHTML = '<div class="verdict">A loop of <b>' + a + "</b> in a 4-input map: <b>" + b + "</b>, so the term is " + c + ". Each doubling of the loop removes one more input.</div>"; };
  Lib.slider($("#gS"), { id: "gss", label: "Loop size (power of 2): ", min: 0, max: 4, value: k, fmt: (x) => Math.pow(2, x), onInput: (v) => { k = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Is the group a valid K-map loop?", ["Valid", "Not valid"],
  [("Two 1s side by side", 0), ("Three 1s in a row", 1), ("A 2 by 2 block of 1s", 0), ("Two 1s joined diagonally", 1), ("Left-hand and right-hand 1s in the same row (wrapping)", 0), ("A block containing a 0", 1), ("All eight 1s of two adjacent columns", 0)],
  "A loop is a rectangle of 1s with 1, 2, 4, 8 or 16 cells.") + CLASSIFY("cl2", "How many inputs does the loop drop on a 4-input map?", ["One", "Two", "Three"],
  [("A loop of two cells", 0), ("A loop of four cells", 1), ("A loop of eight cells", 2), ("The four corner cells", 1), ("A full row of four", 1), ("Two full columns", 2)],
  "2 cells: one input; 4 cells: two; 8 cells: three.") + MATCH([
  ["Gray code", "The label order 00, 01, 11, 10"], ["A loop of four", "Drops two inputs"], ["Wrap-around", "Left and right edges are neighbours, and top and bottom"], ["Simplified sum-of-products", "One AND term per loop, joined by OR"], ["Optimal", "Fewest and largest loops"]]) + ORDER(
  "Put the steps for using a K-map in order.",
  ["Write the output of each row in its cell, with the 0s as well", "Loop groups of 1s: the largest powers of two, wrapping round the edges", "For each loop keep the inputs that do not change", "Join the terms with OR", "Use Boolean algebra only if asked for the simplest form"],
  "Fill, loop, read, join, factor.") + CALC([
  {"q": "How many cells does a K-map for four inputs have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2 to the power 4.", "sol": "<b>16</b>."},
  {"q": "A loop of eight cells on a four-input map: how many inputs are in its term?", "a": 1, "unit": "", "tol": 0.01, "hint": "Three are dropped.", "sol": "<b>1</b>."},
  {"q": "A loop of four cells on a four-input map: how many inputs are in its term?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two are dropped.", "sol": "<b>2</b>."},
  {"q": "How many cells does a three-input K-map have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 cubed.", "sol": "<b>8</b>."},
  {"q": "The four corner cells of a four-input map are looped. How many inputs are in the term?", "a": 2, "unit": "", "tol": 0.01, "hint": "~B.~D.", "sol": "<b>2</b>."}]) + MCQ([
  ("What is the correct column order for a K-map?", ["00 01 10 11", "00 01 11 10", "00 10 01 11", "01 00 10 11"], 1, "Gray code."),
  ("Which loop size is NOT allowed?", ["2", "4", "6", "8"], 2, "Powers of two only."),
  ("A loop's term contains the inputs that:", ["change inside the loop", "do not change inside the loop", "are all 0", "are all 1"], 1, "The constant ones."),
  ("A benefit of a K-map is that it:", ["Is faster to draw than a truth table", "Is guaranteed to give an optimal solution", "Uses fewer inputs", "Always gives a single term"], 1, "Guaranteed optimal."),
  ("Can loops overlap?", ["No", "Yes", "Only in 3-input maps", "Only with 8 cells"], 1, "Overlapping is allowed."),
  ("Cells 0000 and 1000 on a 4-input map are:", ["Not neighbours", "Neighbours (the edges wrap)", "Neighbours only diagonally", "The same cell"], 1, "Edges wrap round.")], "qz1") + CARDS([
  ("K-map", "Grid of a truth table in Gray code order."), ("Gray code", "00, 01, 11, 10."), ("Loop", "Rectangle of 1, 2, 4, 8 or 16 cells containing only 1s."), ("Wrap", "Left and right, top and bottom and the corners."),
  ("Reading a loop", "Keep inputs that do not change: 1 plain, 0 barred."), ("Loop of 2", "Drops one input."), ("Loop of 4", "Drops two inputs."), ("Benefit", "No Boolean algebra; guaranteed optimal solution.")])

build("ac1524", "ac-15-2-4-karnaugh-maps", "Karnaugh Maps", EYA("15.2.4"),
  "Karnaugh maps for three and four inputs: Gray code layout, looping the 1s, wrap-around, reading the terms and simplifying; animations, a K-map builder and the real Paper 3 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.2 Boolean algebra and logic circuits"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
