"""AS CS 10.2.2: searching, sorting and dry-run trace tables. Run: python3 tools/artifact-kit/mk_as1022.py"""
from ascs import *
import json

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def table(heads, rows):
    return '<div class="tw"><table class="t mono"><tr>' + "".join(f"<th>{h}</th>" for h in heads) + "</tr>" + "".join("<tr>" + "".join(f"<td>{'' if c is None else c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>"

# ---- traces computed by running the algorithms (each is checked against the published mark scheme)
def tr_binary(data, target):
    L, R = 1, len(data); rows = []; out = None
    while L <= R:
        M = (L + R) // 2; rows.append((L, R, M))
        if data[M - 1] == target: out = M; break
        if target > data[M - 1]: L = M + 1
        else: R = M - 1
    return rows, out
MYDATA = [2, 8, 9, 12, 13, 15, 18, 19, 20, 23, 25, 26, 39, 38, 40]
BR, BOUT = tr_binary(MYDATA, 15); assert BOUT == 6 and [r[2] for r in BR] == [8, 4, 6]
BIN = table(["LeftPointer", "RightPointer", "MidPointer"], [(1, 15, 8), (None, 7, 4), (5, None, 6)])

def tr_insertion(chars):
    ch = [None] + list(chars); rows = [("2", "", "", "", *chars)]; I = 2
    while I <= 4:
        key = ch[I]; J = I - 1; rows.append((I, key, J, ch[J], *ch[1:]))
        while J >= 1 and ch[J] > key:
            ch[J + 1] = ch[J]; J -= 1; rows.append(("", "", J if J else 0, ch[J] if J else "", *ch[1:]))
        ch[J + 1] = key; rows.append(("", "", "", "", *ch[1:])); I += 1
    return rows, "".join(ch[1:])
IR, IF = tr_insertion("DTHR"); assert IF == "DHRT"
INS = table(["I", "Key", "J", "Chars[J]", "[1]", "[2]", "[3]", "[4]"], [[("'" + c + "'" if len(str(c)) == 1 and str(c).isalpha() else c) for c in r] for r in IR])

def tr_mix22(mix, start):
    m = [None] + mix; idx = start; count = 0; rows = [("", "", "", *m[1:])]
    while True:
        v = m[idx]; m[idx] = m[idx] - 1; idx = v; count += 1; rows.append((idx, v, count, *m[1:]))
        if count == 5: break
    m[4] = count * idx; rows.append((idx, "", count, *m[1:])); return rows
MR22 = tr_mix22([1, 3, 4, 2], 3)
MIX22 = table(["Index", "Value", "Count", "Mix[1]", "Mix[2]", "Mix[3]", "Mix[4]"], MR22)

def tr_mix23(mix, start):
    m = [None] + mix; idx = start; tot = 0; rows = [("", "", "", *m[1:])]
    while tot < 20:
        v = m[idx]; tot += v
        m[idx] = m[idx] + (m[idx + 1] if idx < 4 else m[1]); idx = (v % 4) + 1; rows.append((idx, v, tot, *m[1:]))
    m[1] = tot * idx; rows.append((idx, "", tot, *m[1:])); return rows
MR23 = tr_mix23([4, 2, 3, 5], 2)
assert [r[2] for r in MR23[1:-1]] == [2, 5, 10, 15, 28] and MR23[-1][3] == 56
MIX23 = table(["Index", "Value", "Total", "Mix[1]", "Mix[2]", "Mix[3]", "Mix[4]"], MR23)

def tr_fmt(fmt):
    data = [None, "aaaaaa", "bbbbbb", "cccccc"]; result = "****"; rows = [("", "", "", "", "", *data[1:])]
    for cnt in range(1, len(fmt) + 1, 2):
        c = fmt[cnt - 1]; L = int(fmt[cnt]); idx = (cnt + 1) // 2
        if c == "X": result = data[idx].upper()
        elif c == "Y": result = data[idx].lower()
        elif c == "Z": result = "**" + data[idx]
        data[idx] = result[:L]; rows.append((cnt, c, L, idx, result, *data[1:]))
    return rows
FR = tr_fmt("X3Y2W4"); assert FR[-1][5:] == ("AAA", "bb", "bbbb")
FMT = table(["Count", "C", "L", "Index", "Result", "Data[1]", "Data[2]", "Data[3]"], FR)

def tr_num(num, start):
    n = [None] + num; idx = start; cnt = 0; rows = [("", "", "", *n[1:])]
    while cnt <= 20:
        cv = n[idx]
        if cv == 1: n[idx] += idx; idx += 1; cnt += 1
        elif cv == 2: n[idx] += idx; idx += 2; cnt += 2
        elif cv == 3: n[idx] *= 2; idx += 3; cnt -= 1
        elif cv == 4: cnt += 4
        else: cnt = 20
        idx = (idx % 4) + 1; rows.append((idx, cv, cnt, *n[1:]))
        if len(rows) > 40: break
    return rows
NR = tr_num([1, 2, 5, 3], 1)
NUM = table(["Index", "CaseVar", "Count", "Num[1]", "Num[2]", "Num[3]", "Num[4]"], NR)

def tr_s26():
    data = [None] * 7; num1 = 12; index = 1; rows = [(12, 1, "", *data[1:5])]
    for i in range(2, num1 // 2 + 1):
        if num1 % i == 0: data[index] = i; index += 1
        rows.append(("", index, i, *data[1:5]))
    return rows, index - 1
SR, SN = tr_s26(); assert SN == 4
S26 = table(["Num1", "Index", "i", "Data[1]", "Data[2]", "Data[3]", "Data[4]"], SR)

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>linear search</b> checks each element in turn until the target is found or the end is reached; a <b>binary search</b> works on a <b>sorted</b> array: compare with the <b>middle</b> element and discard the half that cannot contain the target (LeftPointer and RightPointer move, MidPointer ← (Left + Right) DIV 2). A <b>bubble sort</b> repeatedly compares neighbouring elements and swaps them if they are in the wrong order; an <b>insertion sort</b> takes each element (the key) and shifts larger elements right to insert it in the right place. A bubble sort is made <b>more efficient</b> by reducing the inner loop's boundary by one each pass (the largest value is then in place) and by stopping the outer loop when a pass makes <b>no swaps</b>. A <b>dry run</b> with a <b>trace table</b> records the value of each variable after each statement; in an exam you fill in the table row by row, starting from the initial values.</p></div>

  <h2>1 · Searching</h2>
  ''' + pc('''
// binary search: the array is sorted
LeftPointer ← 1
RightPointer ← 15
WHILE LeftPointer <= RightPointer
   MidPointer ← (LeftPointer + RightPointer) DIV 2
   IF MyData[MidPointer] = Target THEN
      OUTPUT "Found " & NUM_TO_STR(MidPointer)
      RETURN MidPointer
   ELSE
      IF Target > MyData[MidPointer] THEN
         LeftPointer ← MidPointer + 1
      ELSE
         RightPointer ← MidPointer - 1
      ENDIF
   ENDIF
ENDWHILE
OUTPUT "Not found"
RETURN -1''') + '''
  <p>Tracing MyTrace(15) on the sorted data 2, 8, 9, 12, 13, 15, 18, 19, ... gives the table below and the output <span class="mono">Found 6</span>, and Result is 6.</p>
  ''' + BIN + '''
  <p>A <b>linear search</b> needs no sorting and works on any array: loop through the elements, compare each with the target, stop when found (a flag in a WHILE or a REPEAT), and report 'not found' after the loop if it was never found.</p>

  <h2>2 · Sorting</h2>
  ''' + pc('''
// bubble sort A (ascending)
FOR LoopCounter ← 1 TO 999
   FOR Index ← 1 TO 999
      IF Numbers[Index] > Numbers[Index + 1] THEN
         Temp ← Numbers[Index]
         Numbers[Index] ← Numbers[Index + 1]
         Numbers[Index + 1] ← Temp
      ENDIF
   NEXT Index
NEXT LoopCounter''') + '''
  <ul>
    <li><b>Descending order:</b> change the &gt; in the comparison to &lt;.</li>
    <li><b>More efficient version (B):</b> the inner loop runs to <b>Boundary</b>, which falls by one each pass because the largest remaining value is now in place; the outer loop is a REPEAT that stops when NoSwaps is TRUE (a pass made no swaps). The outer loop runs the <b>minimum</b> number of times (once) when the array is <b>already sorted</b>.</li>
    <li><b>Swap procedure:</b> parameters must be passed <b>by reference</b>, otherwise the procedure changes copies and the array is unchanged: <span class="mono">PROCEDURE Swap(BYREF Num1, Num2 : INTEGER)</span>.</li>
  </ul>
  <p>Insertion sort of D, T, H, R: the key is taken in turn, larger elements to its left shift right and the key is inserted. Final order D H R T.</p>
  ''' + INS + '''

  <h2>3 · How to dry-run a procedure</h2>
  <ol>
    <li>Write down the starting values of every variable and array element in the first row.</li>
    <li>Execute one pass of the loop at a time, writing a new row after the statements that change values; copy unchanged values only if the table needs them.</li>
    <li>Check the loop condition every pass, using the new values; stop when it fails.</li>
    <li>Do any final assignment after the loop in a last row.</li>
  </ol>
  <p>Example: <span class="mono">Process(3)</span> with Mix = 1, 3, 4, 2; each pass sets Value ← Mix[Index], reduces Mix[Index] by 1, sets Index ← Value and adds 1 to Count; after five passes Mix[4] ← Count × Index.</p>
  ''' + MIX22 + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Doing two passes of a loop in one row of the trace table.</li>
    <li>Forgetting to carry unchanged values, or changing a value in the wrong row.</li>
    <li>Using BYVAL parameters in a Swap procedure.</li>
    <li>Describing the efficient bubble sort without both the shrinking inner loop and the early stop of the outer loop.</li>
    <li>Using binary search on an unsorted array.</li>
  </ul>
'''

watch = '''
  <h2>1 · Binary search halves the range</h2>
  <div id="stA"></div>
  <h2>2 · A bubble sort pass</h2>
  <div id="stB"></div>
  <h2>3 · An insertion sort step</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Binary search</h2>
  <p>Pick the target and press Step.</p>
  <div class="card"><div id="bT"></div><div class="btnrow"><button id="bs_step">Step</button><button id="bs_reset">Reset</button></div><div id="bsV"></div></div>
  <h2>Lab 2 · Bubble sort</h2>
  <div class="card"><div class="btnrow"><button id="bu_step">Compare next pair</button><button id="bu_pass">Run one pass</button><button id="bu_reset">Reset</button></div><div id="buV"></div></div>
  <h2>Lab 3 · Which search or sort?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
'''

_pr, _prjs = PR(["Search or sort?", "Bubble sort or insertion sort?", "Match the term to its meaning", "Put the binary search steps in order", "Working out", "Multiple choice"],
  ("Is it a search or a sort?", ["Search", "Sort"], [("Binary search", 0), ("Bubble sort", 1), ("Linear search", 0), ("Insertion sort", 1), ("Needs the data to be in order first", 0), ("Puts the data in order", 1)], "Search finds; sort orders."),
  ("Bubble sort or insertion sort?", ["Bubble sort", "Insertion sort"], [("Swaps neighbouring elements that are out of order", 0), ("Takes a key and shifts larger elements right", 1), ("Stops early when a pass makes no swaps", 0), ("Inserts the key into the sorted part", 1), ("Uses a Temp variable to swap", 0), ("Final list D H R T from D T H R by shifting", 1)], "Neighbour swaps against shifting."),
  [["Binary search", "Compare with the middle and discard half"], ["Linear search", "Check each element in turn"], ["Bubble sort", "Swap neighbouring elements that are out of order"], ["Dry run", "Executing an algorithm by hand with a trace table"], ["BYREF", "Parameter passed so the procedure changes the original"]],
  ("Put the binary search steps in order.", ["Set Left to 1 and Right to the last index", "Work out Mid ← (Left + Right) DIV 2", "If the middle element is the target, stop", "If the target is bigger, set Left to Mid + 1", "Otherwise set Right to Mid − 1 and repeat"], "Set, mid, found, right half, left half."),
  [{"q": "Left = 1, Right = 15. What is Mid ((Left + Right) DIV 2)?", "a": 8, "unit": "", "tol": 0.01, "hint": "16 DIV 2.", "sol": "<b>8</b>."}, {"q": "Left = 1, Right = 7. What is Mid?", "a": 4, "unit": "", "tol": 0.01, "hint": "8 DIV 2.", "sol": "<b>4</b>."}, {"q": "A bubble sort of 10 values needs at most how many comparisons in one pass?", "a": 9, "unit": "", "tol": 0.01, "hint": "Neighbouring pairs.", "sol": "<b>9</b>."}, {"q": "A binary search on 1000 sorted values needs at most about how many comparisons (log2 1000 rounded up)?", "a": 10, "unit": "", "tol": 0.01, "hint": "2^10 = 1024.", "sol": "<b>10</b>."}, {"q": "Process(3) with Count reaching 5 and Index 2 sets Mix[4] ← Count × Index. What is Mix[4]?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."}],
  [("A binary search needs data that is:", ["Sorted", "Random", "Text only", "Empty"], 0, "Sorted."), ("Mid is:", ["(Left + Right) DIV 2", "Left × Right", "Right − Left", "Left"], 0, "Average, integer."), ("BYREF means:", ["The original is changed", "A copy is changed", "Nothing happens", "The value is deleted"], 0, "Original changed."), ("A more efficient bubble sort stops when:", ["A pass has no swaps", "The array is empty", "Index = 1", "Never"], 0, "No swaps."), ("A trace table records:", ["Variable values as the algorithm runs", "Only the output", "The compiler", "Only arrays"], 0, "Values."), ("Linear search works on:", ["Any array", "Only sorted arrays", "Only numbers", "Only 2D arrays"], 0, "Any.")],
  [("Binary search", "Sorted data; Mid; discard half."), ("Linear search", "Each element in turn."), ("Bubble sort", "Compare neighbours; swap."), ("Insertion sort", "Shift larger; insert the key."), ("Efficient bubble", "Boundary − 1; stop if NoSwaps."), ("BYREF", "Swap needs reference parameters."), ("Dry run", "One row per pass."), ("Trace table", "Variables after each statement.")])

real = RWNOTE + (
rw("Looking up a name in a phone book", "You open near the middle, see whether the name comes before or after, and discard half the book each time: a binary search.", "binary search.") +
rw("Sorting playing cards in your hand", "You pick up each card and slide it into the right place among the cards you already hold: insertion sort.", "insertion sort.") +
rw("Searching an unsorted list", "A shopping list in random order must be checked item by item: linear search.", "linear search.") +
rw("Why sort at all", "Once data is sorted a binary search finds an item in a few steps, even in millions of records.", "sorting pays off.") +
rw("Debugging by hand", "Programmers write down variable values after each line to see where the logic goes wrong: a dry run.", "trace table.")
)

where = [
  ("M/J 2025", "21", "4", "2 + 6", "The most appropriate loop for an insertion sort; complete its trace table"),
  ("O/N 2023", "22", "5", "6", "Dry run Process(3) on a four-element array"),
  ("O/N 2023", "23", "5", "6", "Dry run Process(2) with a WHILE loop and Mix[1] at the end"),
  ("M/J 2024", "21", "5", "6 + 1 + 1", "Dry run Process(\"X3Y2W4\"); add an error handler to the CASE"),
  ("O/N 2024", "22", "5", "3 + 2 + 2", "Statements that could cause a run-time error; a construct that freezes the program; a CASE as an IF"),
  ("O/N 2025", "23", "5", "5 + 1 + 2", "Dry run Process(1) with a CASE; combine two clauses"),
  ("M/J 2026", "21", "8", "4 + 1 + 1", "Trace a binary search function; the output and the result"),
  ("M/J 2026", "22", "5", "1 + 4 + 1 + 2 + 2", "Descending order; why the second bubble sort is more efficient; the best case; a Swap procedure"),
  ("M/J 2026", "23", "7", "4 + 1 + 3 + 1", "Trace an algorithm that stores factors; the highest common factor")]

past = '''  <p class="note">Dry runs appear in every Paper 2 and take care rather than knowledge. Each trace table below was produced by running the algorithm, and the key totals agree with the mark schemes. The marks are per set of values (a zone of the table), so a single wrong row loses one mark only. Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s25", "21", "Q4"), "2 + 6 marks", "State / Complete",
  "An algorithm sorts Chars (ARRAY[1:4] OF CHAR, initially 'D', 'T', 'H', 'R') using I ← 2, WHILE I <= 4 (outer), Key ← Chars[I], J ← I − 1, an inner WHILE J >= 0 AND Chars[J] > Key that shifts Chars[J] to Chars[J + 1] and decrements J, then Chars[J + 1] ← Key and I ← I + 1. (a) The outer loop is not the most appropriate loop structure. State the most appropriate and justify it. (b) Complete the trace table by dry running the algorithm.", "A count-controlled loop (FOR): the number of iterations is known. Key and shifts.",
  "<p><b>(a)</b> " + mks(["A count-controlled (FOR) loop", "because the number of iterations required is known"]) + "</p><p><b>(b)</b> One mark per enclosure: the table shows each key, the shifted values and the final array D, H, R, T.</p>" + INS, "Treating J as zero at the end. The inner test J >= 0 would only matter if the key were the smallest value.") + peq(SRC("w23", "22", "Q5"), "6 marks", "Complete",
  "Mix[1] to Mix[4] are 1, 3, 4, 2. PROCEDURE Process(Start : INTEGER) sets Index ← Start and Count ← 0, then REPEAT Value ← Mix[Index]; Mix[Index] ← Mix[Index] − 1; Index ← Value; Count ← Count + 1 UNTIL Count = 5, then Mix[4] ← Count * Index. Complete the trace table by dry running CALL Process(3).", "Five passes; then the final assignment.",
  "<p>" + mks(["The initial row", "Each of the five iterations with the correct Index, Value, Count and array", "The final iteration and the Mix[4] assignment"]) + "</p>" + MIX22, "Updating Index before reading Value. Value is read from the old Index.") + peq(SRC("w23", "23", "Q5"), "6 marks", "Complete",
  "Mix[1] to Mix[4] are 4, 2, 3, 5. Process(Start) sets Index ← Start, Total ← 0, then WHILE Total < 20: Value ← Mix[Index]; Total ← Total + Value; IF Index < 4 THEN Mix[Index] ← Mix[Index] + Mix[Index + 1] ELSE Mix[Index] ← Mix[Index] + Mix[1]; Index ← (Value MOD 4) + 1; then Mix[1] ← Total * Index. Complete the trace table for CALL Process(2).", "Total 2, 5, 10, 15, 28; Mix[1] = 56.",
  "<p>" + mks(["Row 1 (initialisation)", "Iteration 1: Total 2", "Iteration 2: Total 5", "Iteration 3: Total 10", "Iteration 4: Total 15", "Iteration 5: Total 28 and the final Mix[1] = 56"]) + "</p>" + MIX23, None) + peq(SRC("s24", "21", "Q5"), "6 + 1 + 1 marks", "Complete / Write",
  "Data[1] to Data[3] are \"aaaaaa\", \"bbbbbb\", \"cccccc\". Process(Format) sets Result ← \"****\" then FOR Count ← 1 TO LENGTH(Format) STEP 2: C ← MID(Format, Count, 1); L ← STR_TO_NUM(MID(Format, Count + 1, 1)); Index ← (Count + 1) DIV 2; CASE OF C 'X': Result ← TO_UPPER(Data[Index]), 'Y': Result ← TO_LOWER(Data[Index]), 'Z': Result ← \"**\" & Data[Index]; Data[Index] ← LEFT(Result, L). (a) Complete the trace table for CALL Process(\"X3Y2W4\"). (b) A value of C other than 'X', 'Y' or 'Z' should call Error(C). (i) Write the single line of pseudocode. (ii) State where it goes.", "Three passes: X3, Y2, W4. W matches no clause, so Result is unchanged.",
  "<p><b>(a)</b> One mark per zone (three passes).</p>" + FMT + "<p><b>(b)(i)</b> " + mks(["OTHERWISE : CALL Error(C)"], "a") + " <b>(ii)</b> " + mks(["After the 'Z' clause in the CASE construct, before the ENDCASE"], "b") + "</p>", None) + peq(SRC("w24", "22", "Q5"), "3 + 2 + 2 marks", "Write / Explain",
  "A global 1D array Data has 100 INTEGER elements. FUNCTION Process(Number : INTEGER, Label : STRING) RETURNS STRING sets Count ← INT(100 / Number); Index ← Data[Number]; CASE OF (Index MOD 2) 0 : ReturnValue ← TO_UPPER(RIGHT(Label, Count)) 1 : ReturnValue ← \"****\"; and RETURN RetVal. (a) Three statements could generate a run-time error: write them and explain each. (b) One type of run-time error can make a program freeze. Identify the construct and explain why it occurs. (c) Write pseudocode with a single selection construct with the same functionality without CASE.", "Divide by zero; index out of range; RIGHT with a bad count; RetVal does not exist. A loop that never ends. IF ... ELSE.",
  "<p><b>(a)</b> Any three: " + mks(["Count ← INT(100 / Number): Number could be zero (divide by zero)", "Index ← Data[Number]: Number could be outside the range of the array indices", "ReturnValue ← TO_UPPER(RIGHT(Label, Count)): the number to extract may be too big, negative or out of range, or Label has too few characters", "RETURN RetVal: there is no variable named RetVal, so no value is returned"]) + "</p><p><b>(b)</b> " + mks(["A (pre- or post-) conditional loop", "The terminating condition is never satisfied"], "a") + "</p><p><b>(c)</b> " + mks(["IF ... THEN ... ELSE ... ENDIF", "Both correct assignments and the correct test"], "b") + "</p>" + pc('''
IF Index MOD 2 = 0 THEN
   ReturnValue ← TO_UPPER(RIGHT(Label, Count))
ELSE
   ReturnValue ← "****"
ENDIF'''), None) + peq(SRC("w25", "23", "Q5"), "5 + 1 + 2 marks", "Complete / Write",
  "Num[1] to Num[4] are 1, 2, 5, 3. Process(Start) sets Index ← Start and Count ← 0, then WHILE Count <= 20: CaseVar ← Num[Index]; CASE OF CaseVar 1: Num[Index] ← Num[Index] + Index, Index ← Index + 1, Count ← Count + 1; 2: Num[Index] ← Num[Index] + Index, Index ← Index + 2, Count ← Count + 2; 3: Num[Index] ← Num[Index] * 2, Index ← Index + 3, Count ← Count − 1; 4: Count ← Count + 4; OTHERWISE: Count ← 20; then Index ← (Index MOD 4) + 1. (a) Complete the trace table for CALL Process(1). (b) Which two clauses can be combined, and write the combined clause.", "Clauses one and two; use CaseVar for the index and count increments.",
  "<p><b>(a)</b> One mark for each of four sets of values; one for the later changes (Num[4] set to 6 when Index is 7; Num[1] set to 3 when Index is 3 for the second time).</p>" + NUM + "<p><b>(b)</b> " + mks(["Clauses 1 and 2"]) + " The combined clause:</p>" + pc('''
1 TO 2 : Num[Index] ← Num[Index] + Index
         Index ← Index + CaseVar
         Count ← Count + CaseVar''') + "<p>" + mks(["Use of the variable CaseVar rather than literal values", "A completely correct clause"], "a") + "</p>", None) + peq(SRC("s26", "21", "Q8"), "4 + 1 + 1 marks", "Complete / Give",
  "Global array MyData contains 2, 8, 9, 12, 13, 15, 18, 19, 20, 23, 25, 26, 39, 38, 40 (indexes 1 to 15). FUNCTION MyTrace(Target : INTEGER) RETURNS INTEGER is a binary search using LeftPointer ← 1, RightPointer ← 15 and MidPointer ← (LeftPointer + RightPointer) DIV 2, as shown in the Learn tab. (a) Complete the trace table for Result ← MyTrace(15). (b) Give the output. (c) Give the value assigned to Result.", "Mid 8, then 4, then 6: found.",
  "<p><b>(a)</b> " + mks(["First pass: Left 1, Right 15, Mid 8", "Second pass: Right 7, Mid 4", "Third pass: Left 5, Mid 6"]) + "</p>" + BIN + "<p><b>(b)</b> " + mks(["Found 6"], "a") + " <b>(c)</b> " + mks(["6"], "b") + "</p>", None) + peq(SRC("s26", "22", "Q5"), "1 + 4 + 1 + 2 + 2 marks", "Describe / Explain",
  "Algorithm A is a bubble sort of the array Numbers (1000 INTEGER elements) with an outer FOR LoopCounter ← 1 TO 999 and an inner FOR Index ← 1 TO 999. (a) Describe the change to sort into descending order. (b) Algorithm B uses Boundary ← 999, a REPEAT outer loop with NoSwaps ← TRUE, an inner loop FOR Index ← 1 TO Boundary, sets NoSwaps ← FALSE on a swap, reduces Boundary by 1 and ends UNTIL NoSwaps = TRUE. (i) Explain why B is more efficient, referring to both loops. (ii) State the situation that gives the minimum number of iterations of the outer loop. (c) A procedure Swap(Num1 : INTEGER, Num2 : INTEGER) replaces the swap block and is called Swap(Numbers[Index], Numbers[Index + 1]). (i) Explain why it will not work. (ii) Amend the procedure header and code so it works without global variables.", "Change > to <. Shrinking boundary and early stop. Already sorted. BYREF.",
  "<p><b>(a)</b> " + mks(["The greater-than operator in the comparison is changed to less-than: IF Numbers[Index] < Numbers[Index + 1] THEN"]) + "</p><p><b>(b)(i)</b> " + mks(["The inner loop iterates one fewer time each time the outer loop iterates", "because after each pass the last (largest remaining) element is in the correct place", "The outer loop stops if no swaps are made, as all numbers are sorted", "so fewer iterations are needed if the array is not initially sorted"], "a") + " <b>(ii)</b> " + mks(["When the array is already sorted (in ascending order)"], "b") + "</p><p><b>(c)(i)</b> " + mks(["The parameters are passed by value (BYVAL), not by reference", "so the swap inside the procedure does not change the values in the array"], "c") + "</p><p><b>(c)(ii)</b> " + mks(["The header with BYREF parameters", "The code of the swap using a local Temp"], "d") + "</p>" + pc('''
PROCEDURE Swap(BYREF Num1, Num2 : INTEGER)
   DECLARE Temp : INTEGER
   Temp ← Num1
   Num1 ← Num2
   Num2 ← Temp
ENDPROCEDURE'''), None) + peq(SRC("s26", "23", "Q7"), "4 + 1 + 3 + 1 marks", "Complete / State",
  "STAGE 1: Num1 ← 12; Index ← 1; FOR i ← 2 TO Num1 DIV 2: IF Num1 MOD i = 0 THEN Data[Index] ← i; Index ← Index + 1 ENDIF; NEXT i; Index ← Index − 1; OUTPUT Index, \" values were found\". (a)(i) Complete the trace table for STAGE 1. (ii) State how the numbers in Data are related. (b) STAGE 2 searches Data from Index back for the first value that divides Num2 (8) exactly. Num1 changes to 20. (i) Complete the STAGE 2 trace table. (ii) State what the algorithm finds.", "Data holds 2, 3, 4, 6: the factors of 12 (between 2 and 6).",
  "<p><b>(a)(i)</b> Mark by column:</p>" + S26 + "<p><b>(ii)</b> " + mks(["They are the factors (divisors) of Num1: all the numbers that divide exactly into it"]) + "</p><p><b>(b)(i)</b> With Num1 = 20, Data = 2, 4, 5, 10 and Index = 4; Num2 = 8: Index 4 (Match FALSE: 8 MOD 10 ≠ 0), Index 3 (FALSE: 8 MOD 5 ≠ 0), Index 2 (TRUE: 8 MOD 4 = 0). " + mks(["The Index, Match and Num2 values for each pass"], "a") + "</p><p><b>(ii)</b> " + mks(["The highest common factor (greatest common divisor) of Num1 and Num2: 4 is the highest number that divides exactly into both 8 and 20"], "b") + "</p>", None)

review = req("3 marks", "Complete", "Total ← 0; Index ← 1; WHILE Index <= 3: Total ← Total + Index * 2; Index ← Index + 1. Complete a trace table for Index, Total.", "Three passes.", "<p>" + mks(["Start: Total 0, Index 1", "After passes: Total 2, 6, 12", "Index values 2, 3, 4 and the loop ends"]) + "</p>" + table(["Total", "Index"], [(0, 1), (2, 2), (6, 3), (12, 4)]), None) + req("3 marks", "Trace", "Trace a binary search for 9 in the sorted array 2, 5, 9, 14, 20 (indexes 1 to 5). Give each Mid.", "Mid 3 first.", "<p>" + mks(["Left 1, Right 5, Mid 3", "MyData[3] = 9 = the target", "Found at index 3 on the first pass"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a bubble sort of a sorted array still makes a full pass in the basic version but stops early in the improved version.", "NoSwaps.", "<p>" + mks(["The basic version always runs all passes", "the improved version sets NoSwaps and stops after a pass with no swaps"]) + "</p>", None) + req("2 marks", "State", "State why a binary search cannot be used on an unsorted array.", "Discarding half.", "<p>" + mks(["It relies on the data being in order", "so that half the elements can be discarded after one comparison"]) + "</p>", None) + req("2 marks", "Write", "Write the pseudocode statement to swap Data[1] and Data[2] using Temp.", "Three assignments.", "<p>" + mks(["Temp ← Data[1] and Data[1] ← Data[2]", "Data[2] ← Temp"]) + "</p>", None)

tips = tips_html([
  ("One pass, one row.", "Carry unchanged values."),
  ("Read the old values first.", "Then update Index."),
  ("Binary search: sorted data.", "Mid ← (Left + Right) DIV 2."),
  ("Efficient bubble: two changes.", "Shrinking boundary; stop on no swaps."),
  ("BYREF for Swap.", "Otherwise the array is unchanged."),
  ("Check the loop condition each pass.", "Using the new values."),
], [("a dry run", "Executing an algorithm by hand."), ("a trace table", "A table of variable values after each statement."), ("a binary search", "A search that halves a sorted array each step."), ("BYREF", "A parameter passed by reference so the original changes.")],
  [("Complete", "Fill in the trace table."), ("Explain", "Reasons as well."), ("State", "Short answer."), ("Write", "Write pseudocode.")]) + FC

js = AKJS + AK20JS + "const MYD = " + json.dumps(MYDATA) + r''';
(function () {
  const draw = (s) => { const k = Math.round(s.i); const steps = [[1, 15, 8], [1, 7, 4], [5, 7, 6]]; const st = steps[Math.min(k, 2)]; let o = ""; MYD.forEach((v, i) => { const idx = i + 1, inr = idx >= st[0] && idx <= st[1]; o += SV.rect(10 + i * 38, 20, 34, 30, idx === st[2] ? "f3" : inr ? "f1" : "cell", { rx: 4, ...(inr ? {} : op(0.3)) }) + SV.text(27 + i * 38, 40, v, "lbl", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(27 + i * 38, 66, idx, "sm", { "text-anchor": "middle" }); });
    o += SV.text(10, 100, ["", "Mid = 8: 19 > 15 so Right = 7", "Mid = 4: 12 < 15 so Left = 5", "Mid = 6: 15 = target: Found 6"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 590, h: 115, label: "Binary search", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Search for 15 in sorted data, indexes 1 to 15; Mid = 8.", "19 is greater than 15: keep the left half.", "Mid = 4 holds 12: keep the right half of that.", "Mid = 6 holds 15: found."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const start = [5, 2, 4, 1]; const draw = (s) => { const k = Math.round(s.i); const a = start.slice(); const log = []; for (let i = 0; i < Math.min(k, 3); i++) if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; } let o = ""; a.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 34, k < 4 && (i === k || i === k + 1) ? "f3" : "cell", { rx: 5 }) + SV.text(51 + i * 70, 43, v, "lbl bd", { "text-anchor": "middle" })); o += SV.text(20, 88, k === 0 ? "pass starts: compare 5 and 2" : k < 4 ? "compare neighbours; swap if the left is larger" : "end of pass: the largest (5) is in place", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 340, h: 110, label: "Bubble sort pass", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["5, 2, 4, 1: compare the first pair.", "5 > 2: swap: 2, 5, 4, 1; compare 5 and 4.", "5 > 4: swap: 2, 4, 5, 1; compare 5 and 1.", "5 > 1: swap: 2, 4, 1, 5.", "The largest value 5 is in place after one pass."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["D", "T", "H", "R"], ["D", "T", "H", "R"], ["D", "H", "T", "R"], ["D", "H", "R", "T"]][Math.min(k, 3)]; let o = ""; rows.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 34, k === 1 && i === 2 ? "f3" : "cell", { rx: 5 }) + SV.text(51 + i * 70, 43, v, "lbl bd", { "text-anchor": "middle" })); o += SV.text(20, 88, ["D, T, H, R: D is already sorted", "key = H: T > H so T shifts right...", "...H is inserted before T: D H T R", "key = R: T shifts, R inserted: D H R T"][Math.min(k, 3)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 360, h: 110, label: "Insertion sort", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Start.", "Key H: shift T right.", "Insert H.", "Key R: shift T, insert R. Sorted."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let target = 15, L, R, rows, done; const reset = () => { L = 1; R = MYD.length; rows = []; done = false; paint(); };
  const step = () => { if (done || L > R) return; const M = Math.floor((L + R) / 2); rows.push([L, R, M, MYD[M - 1]]); if (MYD[M - 1] === target) done = M; else if (target > MYD[M - 1]) L = M + 1; else R = M - 1; paint(); };
  const paint = () => { $("#bsV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Left</th><th>Right</th><th>Mid</th><th>MyData[Mid]</th></tr>' + rows.map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("") + "</table></div>" + `<div class="verdict">${done ? `Found ${target} at index <b>${done}</b> after ${rows.length} comparison(s).` : L > R ? `<b>Not found</b> after ${rows.length} comparison(s).` : "Press Step to compare with the middle element."}</div>`; };
  Lib.slider($("#bT"), { id: "bt", label: "Target ", min: 1, max: 45, value: target, fmt: (x) => x, onInput: (v) => { target = v; reset(); } }); $("#bs_step").onclick = step; $("#bs_reset").onclick = reset; reset();
})();
(function () {
  let a, i, swaps, passes; const reset = () => { a = [9, 4, 7, 2, 8]; i = 0; swaps = 0; passes = 0; paint("Press the button to compare the first pair."); };
  const cmp = () => { if (i >= a.length - 1) { i = 0; passes++; paint("End of the pass: the largest remaining value is in place."); return; } let m = ""; if (a[i] > a[i + 1]) { [a[i], a[i + 1]] = [a[i + 1], a[i]]; swaps++; m = "swapped"; } else m = "no swap"; i++; paint(m); };
  const paint = (m) => { $("#buV").innerHTML = '<div class="tw"><table class="t mono"><tr>' + a.map((v, k) => `<td style="${k === i || k === i + 1 ? "background:var(--accent-soft);font-weight:700" : ""}">${v}</td>`).join("") + `</tr></table></div><div class="verdict">${m}. Swaps so far: <b>${swaps}</b>, passes: <b>${passes}</b>.</div>`; };
  $("#bu_step").onclick = cmp; $("#bu_pass").onclick = () => { for (let k = 0; k < a.length; k++) { if (i >= a.length - 1) break; cmp(); } }; $("#bu_reset").onclick = reset; reset();
})();
btnTable("wB", "wO", [
  ["Find a name in an unsorted list", "Linear search", "No order needed"],
  ["Find a name in a sorted list of a million", "Binary search", "Halve the range each step"],
  ["Compare neighbours and swap", "Bubble sort", "Largest value moves to the end"],
  ["Slide each item into place among the sorted ones", "Insertion sort", "Shift larger values right"],
  ["Swap two array elements in a procedure", "BYREF parameters", "Change the original"]
], ["Need", "Method", "Why"]);
''' + _prjs

finish("as-10-2-2-searching-sorting-tracing", "as1022", "Searching, Sorting and Dry Runs",
  "Linear and binary search, bubble and insertion sort with the efficient bubble sort and a BYREF swap, and how to complete trace tables, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "10.2.2", "10 · Data types and structures", "section 10.2 Arrays", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on searching, sorting and tracing (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
