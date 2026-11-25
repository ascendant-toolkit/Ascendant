"""Real past paper questions for the section 19 pages and the 20.1.2 sub-topic pages.

Questions are reworded from 9618 Papers 3 and 4 (2021 to June 2026); mark points are summarised from the mark schemes.
    python3 tools/artifact-kit/pp19.py          injects the section 19 pages and rebuilds them
    python3 tools/artifact-kit/mk_ac20r1.py     (to r7) picks up the 20.1.2 sub-topic questions
"""
import contextlib, io, re, subprocess, sys
from pathlib import Path

import ak18, ak20
from ak20 import SRC, mks, peq, pc
from pp19_code import C

KIT = Path(__file__).parent
ROOT = KIT.parents[1]


def qcode(text):
    return ak20.qcode(text.replace("<-", "←"))


def py(*keys):
    return pc("".join(C[k] for k in keys))


def code(src, marks, ask, question, tip, points, keys, warn=None):
    """Paper 4 entry: Python answer followed by the marking points."""
    ans = py(*keys) + "<p><b>Marks are given for:</b> " + mks(points) + "</p>"
    return ask, peq(src, marks, "Write", question, tip, ans, warn)


def q(src, marks, command, ask, question, tip, answer, warn=None):
    return ask, peq(src, marks, command, question, tip, answer, warn)


def p(*points, lead=""):
    return "<p>" + lead + mks(list(points)) + "</p>"


# ================================================================ searching
S_s22 = q(SRC("s22", "32", "Q8"), "13 marks", "Complete / State / Describe / Compare", "Linear search pseudocode; binary search condition, method and Big O",
    "A binary search or a linear search can look for a value in an array. (a) Complete the linear search pseudocode. [4] (b) State the necessary condition for a binary search, describe how to perform one, and explain how its performance varies with the number of values. [1 + 4 + 1] (c) Compare the two algorithms using Big O notation for time complexity. [3]"
    + qcode('''DECLARE MyList : ARRAY[0:9] OF INTEGER
DECLARE MaxIndex : INTEGER
DECLARE Index : INTEGER
DECLARE Found : BOOLEAN
DECLARE ValueToFind : ....(1)....
INPUT ValueToFind
Found <- FALSE
Index <- 0
MaxIndex <- ....(2)....
REPEAT
  IF MyList[Index] = ValueToFind THEN
    Found <- TRUE
  ENDIF
  Index <- ....(3)....
UNTIL Found OR Index > MaxIndex
IF Found THEN
  OUTPUT "Value found at position ", Index
ELSE
  OUTPUT ....(4)....
ENDIF'''),
    "The array is declared 0:9, so work out the last index before filling blank (2).",
    p("(1) INTEGER", "(2) 9 or LENGTH(MyList) - 1", "(3) Index + 1", "(4) \"Value not found\" or similar", lead="(a) ")
    + p("The list must be sorted / ordered", lead="(b) condition: ")
    + p("Find the middle item", "Check the value of the middle item", "If it equals the item searched for, it is found", "If not, discard the half of the list that cannot contain the item", "Repeat until the item is found", "or only one item is left and it is not the one wanted", lead="(b) method, any four: ")
    + p("As the number of items increases, the time to search increases", lead="(b) performance: ")
    + p("Linear search is O(n), binary search is O(log n)", "Linear search time rises linearly with the number of items; binary search time rises logarithmically", "so the time rises less rapidly for a binary search", lead="(c) "),
    "Describing a binary search without saying the discarded half is thrown away and the process repeats.")

S_w22 = q(SRC("w22", "31, 33", "Q12"), "9 marks", "Complete / State / Describe", "Binary search pseudocode; Big O for linear and binary search",
    "The array Names[0:99] is in alphabetical order. (a) Complete the binary search pseudocode. [6] (b)(i) State the Big O time complexity of a linear search. [1] (ii) Describe the meaning of O(log n) as it applies to a binary search. [2]"
    + qcode('''Lower <- 0
....(1)....
Mid <- 0
Exit <- FALSE
OUTPUT "Enter the name to be found "
INPUT Target
REPEAT
  IF ....(2).... THEN
    OUTPUT Target, " does not exist"
    Exit <- TRUE
  ENDIF
  Mid <- Lower + (Upper - Lower + 1) DIV 2
  IF Names[Mid] < Target THEN
    Lower <- ....(3)....
  ENDIF
  IF Names[Mid] > Target THEN
    ....(4)....
  ENDIF
  IF ....(5).... THEN
    OUTPUT Target, " was found at location ", Mid
    Exit <- TRUE
  ENDIF
....(6)....'''),
    "REPEAT needs an UNTIL, and every blank is one of: set the bounds, test for failure, move a bound, test for success.",
    p("(1) Upper <- 99", "(2) Upper < Lower", "(3) Mid + 1", "(4) Upper <- Mid - 1", "(5) Names[Mid] = Target", "(6) UNTIL Exit", lead="(a) ")
    + p("O(n)", lead="(b)(i) ")
    + p("It is a logarithmic time complexity", "the time rises linearly as the number of items rises exponentially", lead="(b)(ii) "),
    "Writing Lower ← Mid. Without the + 1 the search can loop for ever.")

BS_NAMES = '''DECLARE Names : ARRAY[1:100000] OF STRING
TopOfList <- 1
EndOfList <- 100000
INPUT ToFind
....(1)....
NotInList <- FALSE
WHILE ....(2).... AND ....
  CurrentItem <- (TopOfList + EndOfList) DIV 2
  IF ....(3).... THEN
    Found <- TRUE
  ELSE
    IF TopOfList >= EndOfList THEN
      ....(4)....
    ELSE
      IF ToFind > Names[CurrentItem] THEN
        ....(5)....
      ELSE
        EndOfList <- CurrentItem - 1
      ENDIF
    ENDIF
  ENDIF
ENDWHILE'''

S_s24a = q(SRC("s24", "31, 33", "Q10"), "8 marks", "State / Complete / Describe", "Binary search condition, pseudocode and performance",
    "(a) State a condition that must be true for an array to be searchable by a binary search. [1] (b) Complete the binary search pseudocode. [5] (c) Describe the performance of a binary search in relation to the number of data items, referring to Big O notation. [2]" + qcode(BS_NAMES),
    "Two flags control the loop. Both must be set before it starts.",
    p("The elements are sorted (ascending or descending order)", lead="(a) ")
    + p("(1) Found <- FALSE", "(2) Found = FALSE AND NotInList = FALSE", "(3) ToFind = Names[CurrentItem]", "(4) NotInList <- TRUE", "(5) TopOfList <- CurrentItem + 1", lead="(b) ")
    + p("Big O for a binary search is O(log n)", "the time increases logarithmically as the number of items increases linearly", lead="(c) "),
    "Saying only that it is fast. Link the time to the number of items.")

S_s24b = q(SRC("s24", "32", "Q8"), "8 marks", "Complete / Compare", "Linear search pseudocode; compare linear and binary search",
    "(a) Complete the linear search pseudocode. [4] (b) Compare the methods used by the linear and binary search algorithms to find an item in an array, referring to Big O notation. [4]"
    + qcode('''DECLARE Widgets : ARRAY[1:50000] OF STRING
TopOfList <- 1
EndOfList <- 50000
INPUT ToFind
....(1)....
NotInList <- FALSE
Count <- TopOfList
WHILE ....(2).... AND ....
  IF ....(3).... THEN
    Found <- TRUE
  ENDIF
  Count <- Count + 1
  IF ....(4).... THEN
    NotInList <- TRUE
  ENDIF
ENDWHILE
IF Found = TRUE THEN
  OUTPUT "Item found at position ", Count - 1, " in array"
ELSE
  OUTPUT "Item not in array"
ENDIF'''),
    "Count has already moved on when you test for the end of the list.",
    p("(1) Found <- FALSE", "(2) Found = FALSE AND NotInList = FALSE", "(3) ToFind = Widgets[Count]", "(4) Found = FALSE AND Count > EndOfList", lead="(a) ")
    + p("A linear search checks each element in turn", "until the item or the end of the array is reached", "A binary search finds the middle and decides which half holds the item", "discarding the other half repeatedly", "A binary search needs sorted data", "it usually needs far fewer comparisons", lead="(b) up to three from: ")
    + p("binary search is O(log n)", "linear search is O(n)", lead="and up to two from: "),
    "Leaving out Big O notation when the question asks for it.")

S_s26a = q(SRC("s26", "32", "Q10(a)"), "3 marks", "Describe", "Effect of more data items on linear and binary search",
    "Describe how increasing the number of data items to be searched affects the time efficiency of a linear search and a binary search. Refer to Big O notation.",
    "One sentence about each search, plus its notation.",
    p("Linear search time increases linearly as the number of items increases", "Linear search worst case is O(n)", "Binary search time increases logarithmically as the number of items increases", "Binary search worst case is O(log n)", lead="Any three: "))

S_s26b = q(SRC("s26", "33", "Q10"), "9 marks", "Complete / Write / Describe", "Variable table and pseudocode for a binary search function; Big O",
    "A global 1D array PartName[1:1000000] OF STRING is sorted in ascending order. The function PartSearch takes the item to find as a parameter and returns its location, or -1. (a)(i) Define the variables Left, Right, Mid and Target in a table. [2] (ii) Complete the function using all four. [5] (b) Describe how the time efficiency changes as the number of items increases, referring to Big O. [2]",
    "Target arrives as the parameter. The array is global.",
    p("Left INTEGER: lowest index in the search area; Right INTEGER: highest index", "Mid INTEGER: middle index; Target STRING: the item to be found", lead="(a)(i) ")
    + qcode('''FUNCTION PartSearch(Target : STRING) RETURNS INTEGER
  Left <- 1
  Right <- 1000000
  WHILE Left <= Right
    Mid <- (Left + Right) DIV 2
    IF PartName[Mid] = Target THEN
      RETURN Mid
    ELSE
      IF PartName[Mid] < Target THEN
        Left <- Mid + 1
      ELSE
        Right <- Mid - 1
      ENDIF
    ENDIF
  ENDWHILE
  RETURN -1
ENDFUNCTION''')
    + p("function header", "Left and Right initialised", "loop with a correct exit condition", "Mid calculated", "test for the item", "correct bound moved when not found", "location returned, or -1", lead="(a)(ii) any five: ")
    + p("time increases logarithmically as the number of items increases", "worst case O(log n)", lead="(b) "),
    "Returning -1 inside the loop, which ends the search after one comparison.")

S_s21 = code(SRC("s21", "41, 42, 43", "Q2(b)(i)"), "6 marks", "linearSearch() returning True or False",
    "The global 1D array arrayData holds ten integers. Write the function linearSearch() that takes an integer parameter, performs a linear search and returns True if it is found and False if not.",
    "Return True as soon as you find it. Return False only after the loop has finished.",
    ["function with the correct name", "integer search value as parameter", "loop through all ten elements", "compare each element with the search value", "return True if found", "return False if not found"], ["linear_s21"],
    "Putting <code>return False</code> in an else inside the loop.")

S_w22p4 = code(SRC("w22", "41, 43", "Q1(c)"), "7 marks", "FindValues(): validated input and count of matches",
    "DataArray holds 100 integers from 1 to 100. Write the function FindValues() that asks for a whole number between 1 and 100 and returns the number of times it appears in the array.",
    "This is a linear search that cannot stop early, because every match counts.",
    ["input of the value", "cast to integer", "validated between 1 and 100", "loop through all 100 elements", "compare each element", "counter starts at 0 and goes up on a match", "total returned"], ["find_w22"])

S_s26p4 = code(SRC("s26", "43", "Q1(e)"), "5 marks", "FindWords(): count a word in an array of strings",
    "DataArray holds 15 lower-case strings. Write the procedure FindWords() that takes a string as input, converts it to lower case and outputs the number of times it is stored. Do not use a built-in counting function.",
    "Convert the input before you compare it.",
    ["procedure that inputs a string and converts it to lower case", "loop through all elements", "compare each with the input", "count the matches", "output the final count"], ["find_s26"])

S_s22p4 = code(SRC("s22", "42", "Q2(c)(i)"), "8 marks", "Recursive binary search on the first row of a 2D array",
    "The paper gives pseudocode with six gaps for BinarySearch(SearchArray, Lower, Upper, SearchValue), which uses recursion to search row 0 of a 2D array and returns the index, or -1. Write the function.",
    "Recursive calls must be returned, or the answer is lost on the way back.",
    ["each of the six completed statements", "function header with the four parameters and recursive calls", "rest of the function accurate, including integer division"], ["bs2d_s22"],
    "The paper prints (Lower + (Upper - 1)) DIV 2. Use (Lower + Upper) DIV 2 in your own programs; the printed form can go wrong when Lower is above 0.")

S_s24p4a = code(SRC("s24", "41, 43", "Q1(e)(i)"), "6 marks", "Iterative binary search function",
    "The global array DataStored holds NumberItems sorted integers. Write the iterative function BinarySearch() that takes DataToFind and returns its index, or -1.",
    "The last valid index is NumberItems - 1.",
    ["header with the parameter", "middle value calculated inside the loop", "return the middle index if it matches", "move the upper bound to mid - 1", "move the lower bound to mid + 1", "suitable loop that returns -1 when not found"], ["bs_s24_41"])

S_s24p4b = code(SRC("s24", "42", "Q3(d)(i)"), "6 marks", "Recursive binary search with four parameters",
    "Write the recursive function BinarySearch() that takes IntegerArray, First, Last and ToFind, and returns the index of ToFind or -1.",
    "Write the base case first: First has passed Last.",
    ["recursive function with four parameters", "base case First > Last returning -1", "integer middle index", "return Middle if it matches", "recursive call with Last = Middle - 1", "recursive call with First = Middle + 1"], ["bs_s24_42"])

S_s25p4 = code(SRC("s25", "43", "Q2(e)"), "6 marks", "Binary search function Search()",
    "Write the function Search() that takes DataArray and ItemToFind, performs a binary search and returns the index, or -1. No built-in searching functions.",
    "Use integer division for the middle index.",
    ["header with both parameters", "loop while Low <= High, returning -1 afterwards", "middle index calculated and accessed", "compared with the item", "return the middle index if equal", "Low or High moved correctly"], ["bs_s25"])

S_w25p4 = code(SRC("w25", "42", "Q2(e)"), "6 marks", "RecursiveBinarySearch()",
    "Write the recursive function RecursiveBinarySearch() with four parameters: an integer array, its lower bound, its upper bound and the value to find. It returns the index, or -1.",
    "Every path through the function needs a return.",
    ["function with four parameters, written recursively", "middle value calculated", "return the index if equal", "recursive call with upper = middle - 1", "recursive call with lower = middle + 1", "return -1 when not found"], ["bs_w25"])

SEARCH = [("Paper 3", [S_s22, S_w22, S_s24a, S_s24b, S_s26a, S_s26b]),
          ("Paper 4", [S_s21, S_s22p4, S_w22p4, S_s24p4a, S_s24p4b, S_s25p4, S_w25p4, S_s26p4])]

# ================================================================ sorting
F_s21 = q(SRC("s21", "31, 32, 33", "Q8(a)"), "2 marks", "State", "Two factors that affect a sort's performance",
    "State two factors that may affect the performance of a sorting algorithm.", "Think about the data, then the algorithm.",
    p("The initial order of the data", "The number of data items to be sorted", "The efficiency of the sorting algorithm", lead="Any two: "))

F_s26 = q(SRC("s26", "31", "Q10(b), (c)"), "3 + 1 marks", "Describe / State", "Factors affecting insertion sort time; its Big O",
    "(b) Describe the factors, other than changing the algorithm, that affect the time efficiency of the insertion sort. [3] (c) State the Big O notation for its worst-case time complexity. [1]",
    "Name each factor and say which way it moves the time.",
    p("The number of elements in the array", "fewer elements to sort means better time efficiency", "The initial order of the data", "a partially sorted array is sorted more quickly", lead="(b) any three: ")
    + p("O(n<sup>2</sup>)", lead="(c) "), "Missing the brackets: O(n<sup>2</sup>) must be written exactly.")

B_s21 = code(SRC("s21", "41, 42, 43", "Q2(c)"), "6 marks", "Bubble sort into descending order",
    "The paper gives bubble sort pseudocode with five gaps that sorts into descending order. Write the procedure bubbleSort() to sort the ten values in arrayData into descending order.",
    "Descending order: swap when the left value is smaller.",
    ["correct end of the outer loop", "correct end of the inner loop", "swap when the element is less than the next one", "use of index y + 1", "correct use of temp", "rest matching the pseudocode"], ["bub_s21"],
    "Running the inner loop to the last index, so that y + 1 goes past the end.")

B_s22 = code(SRC("s22", "42", "Q2(b)(i)"), "5 marks", "Bubble sort on each row of a 2D array",
    "ArrayData is a 10 by 10 array of random integers. Using the given pseudocode, add a bubble sort that puts each row (the second dimension) into ascending order. No built-in sorting functions.",
    "Three loops: rows, passes, comparisons.",
    ["loop through the rows", "loop for the passes", "inner loop through the row", "comparison of neighbours", "correct swap"], ["bub_s22"])

B_w22 = code(SRC("w22", "41, 43", "Q1(e)"), "4 marks", "BubbleSort() on 100 integers, then output",
    "Write the procedure BubbleSort() to bubble sort the 100 values in DataArray into ascending order and output the sorted array.",
    "Each pass puts one more value in its final place, so the inner loop can get shorter.",
    ["procedure with an outer loop", "inner loop that stays inside the array", "comparison and swap of neighbours", "output of the sorted array"], ["bub_w22"])

B_s24 = code(SRC("s24", "41, 43", "Q1(d)(i)"), "4 marks", "BubbleSort() on a partly filled array",
    "Write the procedure BubbleSort() to sort the NumberItems values in the global array DataStored into ascending order.",
    "Only sort the elements that are in use.",
    ["procedure looping through the elements", "working inner loop", "comparison of elements", "swapping of elements"], ["bub_s24"])

B_w24a = code(SRC("w24", "41, 43", "Q1(d)(i)"), "3 marks", "Bubble() using a CompareStrings() function",
    "CompareStrings() returns 1 if its first parameter comes first alphabetically and 2 if the second does. Write the function Bubble() that takes an array of strings, bubble sorts it into ascending order using CompareStrings() and returns it.",
    "A result of 2 means the pair is in the wrong order.",
    ["function taking the array and returning it", "strings compared with CompareStrings() and swapped when needed", "correct bubble sort"], ["bub_w24_41"])

B_w24b = code(SRC("w24", "42", "Q3(d)"), "4 marks", "SortScores(): sort by level, then by score",
    "HighScores is a 2D array of strings: player ID, level, score. Write the function SortScores() that uses a bubble sort to order it by level (highest first), then by score (highest first) within a level, and returns it.",
    "The values are strings, so convert them before comparing. Swap the whole record.",
    ["function taking and returning the array", "compare levels and swap every item in the record", "compare scores when levels are equal", "correct loops so the data ends in order"], ["bub_w24_42"],
    "Comparing the strings directly, which puts \"9\" above \"10\".")

B_w25 = code(SRC("w25", "42", "Q2(c)"), "5 marks", "BubbleSort() for an array of any length",
    "Write the function BubbleSort() that takes an integer array, bubble sorts it into ascending order and returns it. It must work for any length. No built-in sorting.",
    "Use the length of the parameter, never a fixed number.",
    ["function taking the array and returning it sorted", "outer loop", "inner loop", "compare and swap into ascending order", "works for any length"], ["bub_w25"])

B_s26 = code(SRC("s26", "43", "Q1(f)(i)"), "5 marks", "Efficient bubble sort by string length",
    "Write the procedure SortLength() that uses a bubble sort to order the 15 strings in DataArray by length, ascending. It must stop as soon as the array is in order. No built-in sorting or order checking.",
    "A swap flag: if a whole pass makes no swap, stop.",
    ["procedure with an outer loop", "inner loop", "stops when the data is in order", "compares lengths", "swaps correctly"], ["bub_s26"])

I_s21 = q(SRC("s21", "31, 32, 33", "Q8(b)"), "6 marks", "Write", "Rewrite a two-array bubble sort as an insertion sort",
    "Scores for 249 students are in Score[1:249] and their names in the matching rows of Name[1:249, 1:2]. A bubble sort orders them into descending order of score. Write pseudocode that does the same task using an insertion sort.",
    "Hold all three items for the student being inserted, and move all three together.",
    qcode('''YearSize <- 249
FOR Student <- 2 TO YearSize
  Temp1 <- Score[Student]
  Temp2 <- Name[Student, 1]
  Temp3 <- Name[Student, 2]
  Counter <- Student
  WHILE Counter > 1 AND Score[Counter - 1] < Temp1
    Score[Counter] <- Score[Counter - 1]
    Name[Counter, 1] <- Name[Counter - 1, 1]
    Name[Counter, 2] <- Name[Counter - 1, 2]
    Counter <- Counter - 1
  ENDWHILE
  Score[Counter] <- Temp1
  Name[Counter, 1] <- Temp2
  Name[Counter, 2] <- Temp3
NEXT Student''')
    + p("FOR loop through the year group", "temporary storage of the score", "temporary storage of the names", "WHILE loop with a correct exit condition", "all three items moved up", "counter updated", "all three items inserted at the end", lead="Any six: "),
    "Sorting ascending. The question keeps descending order, so move items that are smaller.")

I_s25p3 = q(SRC("s25", "33", "Q12(b)"), "4 marks", "Write", "Insertion sort pseudocode for 1000 integers",
    "A 1D array DataArray holds up to 1000 integers. Write pseudocode for an insertion sort into ascending order using Index (outer counter), Position (insertion position) and Value (value to insert). The first line given is FOR Index ← 2 TO 1000.",
    "Store the value before you start moving elements over it.",
    qcode('''FOR Index <- 2 TO 1000
  Value <- DataArray[Index]
  Position <- Index
  WHILE Position > 1 AND DataArray[Position - 1] > Value
    DataArray[Position] <- DataArray[Position - 1]
    Position <- Position - 1
  ENDWHILE
  DataArray[Position] <- Value
NEXT Index''')
    + p("element stored before the inner loop", "appropriate inner loop", "check that the current content is greater than Value", "data moved to the next element", "Position updated", "element reinserted after the inner loop", lead="Any four: "))

I_s26p3 = q(SRC("s26", "31", "Q10(a)"), "5 marks", "Write", "Insertion sort on two parallel arrays",
    "MemberID[0:499] holds unique ID numbers and Names[0:499] the matching names. Using Count, Temp1, Temp2 and Insert, write pseudocode for an insertion sort into ascending order of ID that keeps each name with its ID.",
    "The array starts at 0, so the outer loop starts at 1.",
    qcode('''FOR Count <- 1 TO 499
  Temp1 <- MemberID[Count]
  Temp2 <- Names[Count]
  Insert <- Count - 1
  WHILE Insert >= 0 AND MemberID[Insert] > Temp1
    MemberID[Insert + 1] <- MemberID[Insert]
    Names[Insert + 1] <- Names[Insert]
    Insert <- Insert - 1
  ENDWHILE
  MemberID[Insert + 1] <- Temp1
  Names[Insert + 1] <- Temp2
NEXT Count''')
    + p("outer loop from the second element to the end", "both temporary variables set", "Insert initialised", "correct inner loop condition", "elements of both arrays moved", "Insert decreased", "temporary values placed in both arrays", lead="Any five: "),
    "Writing a bubble sort. It earns nothing here.")

I_w22 = code(SRC("w22", "42", "Q1(e)"), "5 marks", "InsertionSort() of jobs by priority",
    "The global 2D array Jobs[0:99, 0:1] holds a job number and priority in each row, and NumberOfJobs counts the rows in use. Write the procedure InsertionSort() to sort the jobs into ascending order of priority.",
    "Compare the priority column, but move both columns.",
    ["procedure header", "outer loop through the jobs", "inner loop", "comparison of priority", "elements moved up and inserted correctly"], ["ins_w22"])

I_s24 = code(SRC("s24", "42", "Q3(b)(i), (c)(i)"), "4 + 4 marks", "Recursive and iterative insertion sort",
    "The paper gives pseudocode for a recursive function RecursiveInsertion(IntegerArray, NumberElements). (b)(i) Write it in program code. (c)(i) Write IterativeInsertion() to do the same job using iteration.",
    "The recursive call sorts the first n - 1 items. The rest of the function inserts item n.",
    ["(b) header with two parameters and a recursive call", "correct base case and return", "correct while loop", "structure all correct", "(c) iterative header returning the array", "outer loop while elements remain", "inner loop", "accurate selection"], ["ins_s24"])

I_s25p4 = code(SRC("s25", "43", "Q2(b)"), "5 marks", "InsertionSort() function returning the array",
    "Write the function InsertionSort() that takes an integer array, sorts it into ascending order with an insertion sort and returns it. No built-in sorting.",
    "Shift larger values right, then drop the held value into the gap.",
    ["header taking and returning the array", "loop through each element", "element taken out and compared with the sorted part", "elements moved", "element inserted in the correct position"], ["ins_s25"])

I_s26p4 = code(SRC("s26", "42", "Q1(c)(i)"), "5 marks", "InsertionSort() for strings of any array length",
    "Write the function InsertionSort() that takes an array of strings, sorts it into ascending alphabetical order with an insertion sort and returns it. It must work for any length.",
    "Python compares strings alphabetically with &lt; and &gt;.",
    ["header taking the string array", "loop through each element", "insertion sort method", "suitable string comparison", "correctly sorted array returned"], ["ins_s26"])

BUBBLE = [B_s21, B_s22, B_w22, B_s24, B_w24a, B_w24b, B_w25, B_s26]
INS = [I_s21, I_s25p3, I_s26p3, I_w22, I_s24, I_s25p4, I_s26p4]
SORT = [("Factors and efficiency (Paper 3)", [F_s21, F_s26]), ("Bubble sort (Paper 4)", BUBBLE), ("Insertion sort (Papers 3 and 4)", INS)]
INSERT = [("Paper 3", [I_s21, I_s25p3, I_s26p3, F_s21, F_s26]), ("Paper 4", [I_w22, I_s24, I_s25p4, I_s26p4])]


# ================================================================ binary trees
def _tree(values, key=lambda v: v):
    nodes = {}
    for v in values:
        nodes[v] = [None, None]
        cur = values[0]
        while v != cur:
            side = 0 if key(v) < key(cur) else 1
            if nodes[cur][side] is None:
                nodes[cur][side] = v
                break
            cur = nodes[cur][side]
    return values[0], nodes


def tree_svg(root, nodes, null=None):
    """null=None draws the tree as circles; otherwise as linked-list nodes with that null pointer."""
    order, depth = [], {}

    def walk(n, d):
        if n is None:
            return
        walk(nodes[n][0], d + 1)
        order.append(n)
        depth[n] = d
        walk(nodes[n][1], d + 1)
    walk(root, 0)
    boxed = null is not None
    step, bw = (64, 110) if boxed else (62, 64)
    xy = {n: (i * step + bw / 2 + 4, depth[n] * 70 + 26) for i, n in enumerate(order)}
    w, h = (len(order) - 1) * step + bw + 8, max(depth.values()) * 70 + 52
    line = lambda a, b: f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="currentColor" stroke-width="1.5"/>'
    text = lambda x, y, s: f'<text x="{x:.0f}" y="{y + 5:.0f}" text-anchor="middle" font-size="14" fill="currentColor">{s}</text>'
    out = []
    for n in order:
        x, y = xy[n]
        for side, child in enumerate(nodes[n]):
            if child is not None:
                cx, cy = xy[child]
                start = (x + (side * 2 - 1) * 40, y) if boxed else (x, y + 18)
                out.append(line(start, (cx, cy - (15 if boxed else 18))) + f'<circle cx="{cx:.0f}" cy="{cy - (15 if boxed else 18):.0f}" r="3" fill="currentColor"/>')
    for n in order:
        x, y = xy[n]
        if boxed:
            for bx, bww in ((-55, 28), (-27, 54), (27, 28)):
                out.append(f'<rect x="{x + bx:.0f}" y="{y - 15:.0f}" width="{bww}" height="30" fill="none" stroke="currentColor" stroke-width="1.5"/>')
            out.append(text(x, y, n))
            for side, child in enumerate(nodes[n]):
                if child is None:
                    out.append(text(x + (side * 2 - 1) * 41, y, null))
        else:
            out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="29" ry="18" fill="none" stroke="currentColor" stroke-width="1.5"/>' + text(x, y, n))
    if boxed:
        # boxes in neighbouring columns sit on different levels, so they never overlap
        assert all(abs(xy[a][0] - xy[b][0]) >= bw + 4 or depth[a] != depth[b] for a in order for b in order if a != b)
    kind = "linked list of nodes" if boxed else "binary tree"
    return (f'<div style="overflow-x:auto"><svg viewBox="0 0 {w:.0f} {h}" style="display:block;width:100%;min-width:{min(w, 520):.0f}px;max-width:{w:.0f}px;height:auto" role="img" aria-label="Diagram of the {kind}">'
            + "".join(out) + "</svg></div>")


def draw(src, marks, ask, intro, given, added, null, shown_note):
    full = _tree(given + added)
    return q(src, marks, "Complete", ask,
             intro + f" {null} is the null pointer. " + shown_note + tree_svg(*_tree(given)),
             "Compare with each node from the root down: smaller goes left, larger goes right. Fill every empty pointer with the null value.",
             "<p>The completed linked list (the root pointer points to the first node):</p>" + tree_svg(*full, null=str(null))
             + p("new nodes added with the correct data", "all of them connected by arrows from the correct pointer boxes", "correct null pointers throughout", "nothing extra written in any pointer box", lead="Marks: "),
             "Writing a null value in a pointer box that has an arrow.")


T_w24a = q(SRC("w24", "31, 33", "Q11(a)"), "4 marks", "Complete", "Draw a binary tree of colours as a linked list",
    "The ordered binary tree below is to be stored as a linked list of nodes, each with a left pointer, data and right pointer. -1 is the null pointer. Complete the linked list for the whole tree."
    + tree_svg("Red", {"Red": ["Green", "Yellow"], "Green": ["Blue", "Orange"], "Yellow": ["Violet", None], "Blue": [None, None], "Orange": ["Indigo", None], "Violet": [None, None], "Indigo": [None, None]}),
    "Copy the shape of the tree exactly, then add -1 wherever a node has no child.",
    tree_svg("Red", {"Red": ["Green", "Yellow"], "Green": ["Blue", "Orange"], "Yellow": ["Violet", None], "Blue": [None, None], "Orange": ["Indigo", None], "Violet": [None, None], "Indigo": [None, None]}, null="-1")
    + p("four additional nodes with correct data", "correct null pointers and no extra ones", "arrows joining parents to children", "all nodes in the correct order", lead="Marks: "),
    "Putting Violet to the right of Yellow. It is on the left.")

_w24b = {25: [4, 36], 4: [1, 16], 36: [None, 64], 1: [None, None], 16: [9, None], 64: [49, None], 9: [None, None], 49: [None, None]}
T_w24b = q(SRC("w24", "32", "Q11(a)"), "4 marks", "Complete", "Draw a binary tree of integers as a linked list",
    "The ordered binary tree below is to be stored as a linked list of nodes. -1 is the null pointer. Complete the linked list." + tree_svg(25, _w24b),
    "Arrows must leave from the left or right pointer box, never the data box.",
    tree_svg(25, _w24b, null="-1") + p("five additional nodes with correct data", "correct null pointers", "arrows from the correct pointer boxes", "all nodes in the correct order", lead="Marks: "))

T_s25a = draw(SRC("s25", "31", "Q4(a)"), "4 marks", "Add 6, 15, 41 and 66 to a binary tree",
    "A linked list of nodes stores ordered integers, organised as a binary tree. Complete it after adding 6, 15, 41 and 66, including null pointers.",
    [36, 12, 40, 3], [6, 15, 41, 66], -1, "The tree before adding them:")
T_s25b = draw(SRC("s25", "32", "Q11(a)"), "4 marks", "Add four strings to a binary tree",
    "A linked list of nodes stores ordered strings, organised as a binary tree. Complete it after adding Aa, Mm, Ss and Xx, including null pointers.",
    ["Pp", "Gg", "Rr", "Kk"], ["Aa", "Mm", "Ss", "Xx"], 0, "The tree before adding them:")

A_w21 = code(SRC("w21", "41, 42", "Q3(b)"), "8 marks", "AddNode() for a tree held in a 2D array",
    "ArrayNodes holds 20 nodes as [left pointer, data, right pointer]; -1 is null. The paper gives pseudocode with six gaps for AddNode(ArrayNodes, RootPointer, FreeNode), which inputs an integer and adds it to the tree. Write the procedure.",
    "Python cannot pass integers by reference, so return the changed pointers.",
    ["each completed statement (up to six)", "header that passes by reference, returns the three values, or uses global", "rest of the procedure matching the pseudocode"], ["add_w21"])

A_w22 = code(SRC("w22", "41, 43", "Q3(c)"), "5 marks", "Recursive SearchValue() on a tree",
    "ArrayNodes is a global 2D array of [left pointer, data, right pointer]; -1 is null. The paper gives pseudocode with four gaps for the recursive function SearchValue(Root, ValueToFind), which returns the index of the value or -1. Write the function.",
    "Smaller values are to the left, so go left when the node's data is greater than the target.",
    ["each completed statement (four)", "rest of the function correct"], ["search_w22"])

A_s24 = ("InsertNode() for an object-based tree in an array", peq(SRC("s24", "42", "Q2(b)(ii)"), "6 marks", "Write",
    "TreeClass has a private array Tree[0:19] of Node objects, FirstNode and NumberNodes. Write the method InsertNode(NewNode). If the tree is empty it stores the node at index NumberNodes and sets FirstNode to 0. Otherwise it stores the node, follows the pointers from FirstNode to the correct position and sets the parent's left or right pointer. NumberNodes goes up each time.",
    "Remember the previous node: you update its pointer after you fall off the tree.",
    pc(C["tree_s24"].split("    def OutputTree")[0]) + "<p><b>Marks are given for:</b> "
    + mks(["method taking a Node", "empty tree handled", "node stored at index NumberNodes", "root data compared", "left or right chosen", "repeated until the position is found", "parent pointer and NumberNodes updated"]) + "</p>",
    "Comparing the Node objects themselves instead of their data."))

A_s25 = code(SRC("s25", "41", "Q3(c)(iii)"), "6 marks", "Insert() for a tree of linked node objects",
    "A Tree object holds FirstNode, the root Node. Each Node has data and left and right Node attributes (null if empty). Write the method Insert() that takes a node and places it: left if its data is less than the current node's, right if greater or equal, until an empty position is found.",
    "The pointers are objects here, so test against None rather than -1.",
    ["method taking a node", "go left if smaller", "store it if the left is null", "go right if greater or equal", "store it if the right is null", "repeat until placed"], ["tree_s25"])

A_s26 = code(SRC("s26", "43", "Q3(b)"), "7 marks", "AddNode() with a full-tree check",
    "BinaryTree is a global array of 100 nodes [left, data, right]; TreeRootPointer starts at -1 and FirstFreeNodePointer at 0. Write the procedure AddNode() that takes an integer, outputs \"The tree is full\" if there is no space, and otherwise adds it in the correct position.",
    "Check for a full tree first, then an empty tree, then walk down.",
    ["header taking the integer and increasing the free pointer", "empty tree handled and root updated", "full tree message", "data and null pointers stored", "compare from the root", "follow left if less", "follow right if greater", "repeat to a leaf", "update the parent pointer"], ["add_s26"])

A_w25 = code(SRC("w25", "42", "Q3(b)"), "7 marks", "AddNode() for a 50-node tree",
    "TreeArray holds up to 50 nodes [left, data, right], with global RootPointer (-1) and FreeNode (0). Write the procedure AddNode() that takes an integer, stores it in the next free node and updates the parent's pointer, or outputs \"The tree is full\".",
    "FreeNode must go up only when a node has been added.",
    ["header and data stored at FreeNode", "full tree check and message", "empty tree sets RootPointer", "compare with the root", "go left if less", "go right if greater", "loop until placed", "parent pointer updated", "FreeNode increased"], ["add_w25"])

R_w21 = code(SRC("w21", "41, 42", "Q3(e)(i)"), "7 marks", "Recursive in-order traversal",
    "An in-order traversal visits the left node, outputs the root, then visits the right node. Write the recursive procedure InOrder() for the tree held in ArrayNodes, where -1 is null.",
    "Test each pointer before you make the call.",
    ["InOrder with a parameter for the current node", "check the left pointer for -1", "recursive call on the left", "output the data", "check the right pointer", "recursive call on the right", "order left, root, right"], ["in_w21"])

R_w22 = code(SRC("w22", "41, 43", "Q3(d)"), "7 marks", "Recursive post-order traversal",
    "A post-order traversal visits the left node, visits the right node, then outputs the root. Write the procedure PostOrder() that takes the root node as a parameter.",
    "The output line comes after both calls.",
    ["header with one parameter and a recursive call", "check the left pointer", "recursive call on the left", "check the right pointer", "recursive call on the right", "output the node's data", "all in the correct order"], ["post_w22"])

R_s25 = code(SRC("s25", "41", "Q3(d)"), "5 marks", "OutputInOrder() on node objects",
    "Write the recursive procedure OutputInOrder() that takes a Node object and outputs the tree's data in ascending order: left subtree, current node, right subtree. A missing child is null.",
    "Use the get methods: the attributes are private.",
    ["recursive procedure taking a node", "left checked for null and called", "node's data output", "right checked for null and called", "correct order"], ["out_s25"])

R_s26 = code(SRC("s26", "43", "Q3(e)(i)"), "7 marks", "InOrder() from the root pointer",
    "Write the recursive procedure InOrder() that takes the root pointer and outputs the data in the 2D array BinaryTree in ascending order. -1 is null.",
    "Ascending order from a binary search tree is always left, node, right.",
    ["recursive procedure with a parameter", "left pointer checked", "recursive call on the left", "data output", "right pointer checked", "recursive call on the right", "correct order"], ["in_s26"])

P_rec31 = q(SRC("s25", "31", "Q4(b), (c)"), "2 + 1 marks", "Describe / Identify", "Meaning of recursion; another ADT that uses recursive algorithms",
    "(b) Describe what is meant by recursion. [2] (c) A binary tree is an ADT that a designer can implement using recursive algorithms. Identify one other. [1]",
    "Two marks need the self-call and how it stops.",
    p("A function or procedure that calls itself", "until the terminating condition (base case) is reached, when no more calls are made", lead="(b) ") + p("Stack", lead="(c) "))

P_rec32 = q(SRC("s25", "32", "Q11(b)"), "2 marks", "Identify / Give", "Why recursion helps, with an example",
    "A binary tree can be used to implement recursion. Identify one feature of an algorithm that makes recursion beneficial, and give one example of an application that could use a recursive algorithm.",
    "One feature and one example.",
    p("The problem breaks down into smaller versions of itself", lead="Feature: ") + p("factorial, Fibonacci, compound interest, tree traversal or evaluating RPN", lead="Example: "))

BST = [("Drawing the tree (Paper 3)", [T_w24a, T_w24b, T_s25a, T_s25b]), ("Adding and searching (Paper 4)", [A_w21, A_w22, A_s24, A_s25, A_w25, A_s26]),
       ("Traversals (Paper 4)", [R_w21, R_w22, R_s25, R_s26])]
RECTREE = [("Traversals (Paper 4)", [R_w21, R_w22, R_s25, R_s26]), ("Recursive search (Paper 4)", [A_w22]), ("Theory (Paper 3)", [P_rec31, P_rec32])]


# ================================================================ abstract data types (theory and pointer questions)
def _table(head, rows):
    return ('<div class="tw"><table class="t"><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>")


_flowers = "Rose Marigold Foxglove Iris Daisy Dahlia Saxifrage Lupin Lily Hydrangea".split()
D_w21 = q(SRC("w21", "31, 32", "Q10(b), (c)"), "3 + 2 marks", "Explain / Identify", "Why a stack suits recursion; two other ADTs",
    "(b) Explain why a stack is a suitable ADT for implementing recursion. [3] (c) Identify two ADTs other than a stack. [2]", "Say what is stored, why last in, first out matters, and what that achieves.",
    p("A stack is a LIFO structure", "each recursive call is pushed and then popped as it ends", "so the calls unwind in the required order", lead="(b) ") + p("linked list", "queue or binary tree", lead="(c) "),
    "Naming data types such as array or record in (c).")
D_w22 = q(SRC("w22", "32", "Q11"), "10 marks", "Complete / Explain", "Delete from a linked list, search it and improve it",
    "A linked list stores flower names in alphabetical order in the arrays Flower and NextPointer; 0 ends the list and HeadPointer is 6." + _table(["Index", "Flower", "NextPointer"], [(i + 1, f, n) for i, (f, n) in enumerate(zip(_flowers, [7, 1, 10, 9, 3, 5, 0, 2, 8, 4]))])
    + "(a) Marigold, Dahlia, Saxifrage and Hydrangea are deleted. Give the new HeadPointer and NextPointer values. [3] (b) Complete the search pseudocode. [5] (c) Explain how the structure could be improved. [2]"
    + qcode('''Pointer <- ....(1)....
Found <- 0
INPUT FlowerName
WHILE ....(2)....
  IF Flower[Pointer] = FlowerName THEN
    Found <- Pointer
    Pointer <- 0
  ELSE
    Pointer <- ....(3)....
  ENDIF
ENDWHILE
IF ....(4).... THEN
  OUTPUT ....(5)...., " is found"
ELSE
  OUTPUT "The flower you wanted is not in the list"
ENDIF'''),
    "Write the remaining names in alphabetical order first, then point each one at the next.",
    "<p>(a) HeadPointer = 5</p>" + _table(["Name", "Index", "New NextPointer"], [("Daisy", 5, 3), ("Foxglove", 3, 4), ("Iris", 4, 9), ("Lily", 9, 8), ("Lupin", 8, 1), ("Rose", 1, 0)])
    + p("correct HeadPointer", "any three correct pointers", "all six correct", lead="(a) marks: ")
    + p("(1) HeadPointer", "(2) Pointer <> 0", "(3) NextPointer[Pointer]", "(4) Found <> 0", "(5) Flower[Found]", lead="(b) ")
    + p("add a free list pointer", "so that the unused space can be reused", lead="(c) "),
    "In (c), improving the search instead of the structure.")
D_s23 = q(SRC("s23", "31", "Q11"), "11 marks", "Write / Complete / Explain", "Declare a queue, complete Dequeue, build a queue from stacks",
    "A queue of up to 60 strings uses FrontPointer, RearPointer, Length and the 1D array Queue, with the constant MaxSize. (a) Write pseudocode to declare them. [3] (b) Complete the function Dequeue, which removes the front item, moves the pointer, reduces the length and wraps round past MaxSize. [4] (c) Explain how a new element can be added if the queue is implemented using two stacks. [4]",
    "Two LIFO stacks reverse the order twice, which gives FIFO.",
    qcode('''CONSTANT MaxSize = 60
DECLARE Queue : ARRAY[1:60] OF STRING
DECLARE FrontPointer : INTEGER
DECLARE RearPointer : INTEGER
DECLARE Length : INTEGER''') + p("constant defined", "array declared", "three integers declared", lead="(a) ")
    + qcode('''FUNCTION Dequeue RETURNS STRING
  DECLARE Item : STRING
  IF Length > 0 THEN
    Item <- Queue[FrontPointer]
    FrontPointer <- FrontPointer + 1
    Length <- Length - 1
    IF Length = 0 THEN
      CALL Initialise
    ELSE
      IF FrontPointer > MaxSize THEN
        FrontPointer <- 1
      ENDIF
    ENDIF
  ELSE
    OUTPUT "The print queue was empty - error"
    Item <- ""
  ENDIF
  RETURN Item
ENDFUNCTION''') + "<p>(b) one mark for each correctly completed line.</p>"
    + p("two stacks are needed so the second reverses the order", "stack 1 holds the queue with the newest at the bottom and stack 2 is empty", "pop everything from stack 1 onto stack 2, push the new element", "then pop everything from stack 2 back onto stack 1", lead="(c) "),
    "Saying \"use two stacks\" without explaining the reversal.")
D_w23a = q(SRC("w23", "32", "Q9(b)"), "2 marks", "Justify", "Linked list instead of an array for a stack",
    "Justify the use of a linked list instead of an array to implement a stack.", "Give one point about each structure.",
    p("A linked list is dynamic and not restricted in size", "it can grow or shrink by adding or removing nodes", "editing uses pointers rather than moving data", lead="Linked list: ") + p("An array is static, with a fixed size", "when it is full the stack cannot grow", lead="Array (one mark for each side, maximum 2): "))
D_w23b = q(SRC("w23", "31", "Q10(c)"), "2 marks", "Compare and contrast", "Queue and stack ADTs",
    "Compare and contrast the queue and stack abstract data types.", "Give a similarity and a difference.",
    p("A queue is FIFO and a stack is LIFO", "both can vary in size", "a stack adds and removes at the same end; a queue at opposite ends", "a stack has one moving pointer, a queue has two", lead="Any two: "))
D_s25 = q(SRC("s25", "33", "Q12(a)"), "1 mark", "Identify", "Two ADTs other than an array",
    "An array is an abstract data type (ADT). Identify two other ADTs.", "Both must be correct for the single mark.",
    p("any two of: stack, queue, linked list, binary tree, graph"))
ADT = [("Identify and compare", [D_s25, D_w21, D_w23b, D_w23a]), ("Queues and linked lists", [D_w22, D_s23])]


# ================================================================ banks from other pages
def _bank(module):
    keep = (ak18.build, ak20.build)
    ak18.build = ak20.build = lambda *a, **k: None   # import the question bank without rebuilding that page
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            m = __import__(module)
    finally:
        ak18.build, ak20.build = keep
    out = []
    for b in re.findall(r'  <details class="eq">.*?</details>\n?', m.past, re.S):
        ask = re.sub(r"<[^>]+>", " ", b.split('</span> ', 3)[-1].split("</summary>")[0])
        ask = " ".join(ask.split())
        out.append((ask[:90].rsplit(" ", 1)[0] + "…" if len(ask) > 90 else ask, b))
    return out


def graphs():
    return [("Graphs in artificial intelligence (Paper 3)", _bank("mk_ac1811")), ("Dijkstra's and A* algorithms (Paper 3)", _bank("mk_ac1812"))]


# ================================================================ 20.1.2 sub-topics
def oop(name):
    A, B = _bank("mk_ac2012"), _bank("mk_ac2013")   # theory and pseudocode (Paper 3); program code (Paper 4)

    def part(src, marks, ask, question, tip, points, keys, warn=None):
        return code(src, marks, ask, question, tip, points, keys, warn)

    emp = "A company stores employee data using OOP. Employee has private HourlyPay (REAL), EmployeeNumber (STRING), JobTitle (STRING) and PayYear2022 (ARRAY[0:51] OF REAL). "
    c41 = "A game uses OOP. Character has Name (STRING), XPosition and YPosition (INTEGER). "
    c42 = "A game uses OOP. Character has CharacterName (STRING), DateOfBirth (DATE), Intelligence (REAL) and Speed (INTEGER). "
    emp_con = part(SRC("s23", "42", "Q3(a)(i)"), "5 marks", "Employee class and constructor",
        emp + "Declare the class and its constructor, which takes the pay, number and job title and sets all 52 pay elements to 0.0.",
        "Declare every attribute inside the constructor, including the array.",
        ["class declaration", "four private attributes with the array of 52", "constructor with three parameters", "parameters assigned", "array filled with 0.0"], ["emp"])
    mgr_con = part(SRC("s23", "42", "Q3(b)(i)"), "4 marks", "Manager child class and constructor",
        emp + "The child class Manager adds BonusValue (REAL). Declare it with its constructor, which takes the bonus, pay, number and job title.",
        "Call the parent constructor first, then set the new attribute.",
        ["Manager inherits from Employee", "constructor with four parameters", "parent constructor called with three values", "BonusValue declared and assigned"], ["mgr"])
    c41_con = part(SRC("w23", "41, 43", "Q3(a)(i), (c)(i)"), "4 + 3 marks", "Character and BikeCharacter constructors",
        c41 + "(a)(i) Declare the class and its constructor. (c)(i) Declare BikeCharacter, which inherits from Character and passes all three values to the parent constructor.",
        "The child constructor needs only the call to super().",
        ["class with three attributes", "constructor with three parameters", "attributes assigned", "child class inherits", "child constructor with three parameters", "parent constructor called"], ["char41", "bike"])
    magic_con = part(SRC("w23", "42", "Q3(c)(i)"), "5 marks", "MagicCharacter child class and constructor",
        c42 + "Declare MagicCharacter, which inherits from Character and adds Element (STRING). Its constructor takes the element and the four parent values.",
        "Pass the parent only the four values it expects.",
        ["inherits from Character", "Element declared", "constructor with five parameters", "parent constructor called with four", "Element assigned"], ["magic"])
    emp_get = part(SRC("s23", "42", "Q3(a)(ii)-(iv)"), "2 + 3 + 2 marks", "Employee get method, SetPay() and GetTotalPay()",
        emp + "Write GetEmployeeNumber(); SetPay(), which takes a week number and hours and stores that week's pay; and GetTotalPay().",
        "Week 1 is stored at index 0.",
        ["get header with no parameters", "returns the employee number", "SetPay with two parameters", "pay = hours × hourly pay", "stored at the correct index", "total method returns a value", "all elements added"], ["emp_methods"])
    c41_get = ("Get methods and validated set methods", peq(SRC("w23", "41, 43", "Q3(a)(ii), (iii)"), "3 + 4 marks", "Write",
        c41 + "(ii) Write GetXPosition() and GetYPosition(). (iii) SetXPosition() and SetYPosition() add the parameter to the position and keep it between 0 and 10 000. Write them.",
        "These setters add to the value, then limit it.",
        pc(C["char41_methods"].split("    def Move")[0]) + "<p><b>Marks are given for:</b> " + mks(["get header with no parameter", "returns the correct value", "second get method", "set method with a parameter", "adds it to the attribute", "limits to 0 and 10 000", "second set method"]) + "</p>",
        "Replacing the position with the parameter instead of adding to it."))
    c42_get = ("Get methods and a set method", peq(SRC("w23", "42", "Q3(a)(ii), (iii)"), "3 + 2 marks", "Write",
        c42 + "(ii) Write GetIntelligence() and GetName(). (iii) Write SetIntelligence(), which assigns its parameter to the attribute.",
        "A getter returns; a setter assigns.",
        pc(C["char42_methods"].split("    def Learn")[0]) + "<p><b>Marks are given for:</b> " + mks(["get header with no parameter", "returns the attribute", "second get method", "set header with one parameter", "assigns it to the attribute"]) + "</p>",
        "Printing the value inside a get method instead of returning it."))
    node_get = part(SRC("s24", "42", "Q2(a)(ii), (iii)"), "3 + 3 marks", "Get and set methods for a Node class",
        "Node has LeftPointer, Data and RightPointer (INTEGER). Write the three get methods and the three set methods.",
        "One pattern, repeated: show it carefully the first time.",
        ["get method with no parameter", "returns the correct attribute", "other two correct", "set method with a parameter", "assigns it to the attribute", "other two correct"], ["getset_s24"])
    mgr_poly = part(SRC("s23", "42", "Q3(b)(ii)"), "3 marks", "Override SetPay() in Manager",
        emp + "Manager.SetPay() overrides the parent method: it increases the hours by the BonusValue percentage, then calls the parent's SetPay().",
        "Same method name and parameters as the parent.",
        ["SetPay with two parameters", "hours increased by the bonus percentage", "parent SetPay called with the week and new hours"], ["mgr_pay"])
    bike_poly = part(SRC("w23", "41, 43", "Q3(c)(ii)"), "2 marks", "Override Move() in BikeCharacter",
        c41 + "BikeCharacter.Move() overrides the parent method, changing the position by 20 instead of 10 for \"up\", \"down\", \"left\" or \"right\".",
        "Reuse the inherited set methods.",
        ["method with a parameter that overrides Move()", "positions changed by 20 correctly"], ["bike_move"])
    magic_poly = part(SRC("w23", "42", "Q3(c)(ii)"), "3 marks", "Override Learn() in MagicCharacter",
        c42 + "MagicCharacter.Learn() overrides the parent method: intelligence rises 20% for fire or water, 30% for earth and 10% otherwise.",
        "Private parent attributes are reached through the get and set methods.",
        ["overrides Learn() with no parameters", "element checked", "correct calculations stored"], ["magic_learn"])
    node_obj = ("Node class with a constructor", peq(SRC("s24", "42", "Q2(a)(i)"), "4 marks", "Write",
        "A binary tree is built with OOP. Declare the class Node with LeftPointer, Data and RightPointer (INTEGER). The constructor sets Data to its parameter and both pointers to -1.",
        "-1 is the null pointer.", py("node_s24") + "<p><b>Marks are given for:</b> " + mks(["class declaration", "three integer attributes", "constructor with one parameter", "Data assigned and pointers set to -1"]) + "</p>"))
    tree_obj = ("TreeClass: constructor, InsertNode() and OutputTree()", peq(SRC("s24", "42", "Q2(b)"), "4 + 6 + 4 marks", "Write",
        "TreeClass has an array Tree[0:19] of Node, FirstNode and NumberNodes. (i) Declare it with a constructor that sets FirstNode to -1, NumberNodes to 0 and each element to a Node holding -1. (ii) Write InsertNode(), which stores a node and links it to its parent. (iii) Write OutputTree(), which outputs each stored node's pointers and data, or \"No nodes\".",
        "Nodes are stored in the order they arrive; the pointers give the tree its shape.",
        py("tree_s24") + "<p><b>Marks are given for:</b> " + mks(["(i) class, attributes, constructor and 20 Node objects", "(ii) empty tree handled", "node stored at NumberNodes", "pointers followed until the position is found", "parent pointer and NumberNodes updated", "(iii) \"No nodes\" test", "loop over stored nodes", "get methods used for the output"]) + "</p>"))
    node25 = part(SRC("s25", "41", "Q3(a)"), "4 + 3 + 3 marks", "Node class whose pointers are objects",
        "A binary tree uses OOP. Node has NodeData (integer), LeftNode and RightNode (Node, null if empty). Declare the class and constructor, the three get methods and the two set methods.",
        "None is Python's null.",
        ["class and constructor with one parameter", "three attributes with correct types", "data assigned and nodes set to null", "three get methods", "two set methods taking a Node"], ["node_s25"])
    tree25 = part(SRC("s25", "41", "Q3(c)"), "2 + 1 + 6 marks", "Tree class with GetRootNode() and Insert()",
        "Tree has FirstNode, the root. Write its constructor, GetRootNode() and Insert(), which moves left for smaller data and right otherwise until it finds an empty position.",
        "Loop until the node has been stored, then return.",
        ["class and constructor taking a node", "get method returning the root", "Insert taking a node", "left checked and stored if null", "right checked and stored if null", "loops until placed"], ["tree_s25"])

    sets = {
        "ac20r1": [("Paper 3", [A[10], A[11], A[12]]), ("Paper 4", [B[3], emp_con, mgr_con, c41_con, magic_con, node_obj])],
        "ac20r2": [("Paper 3", [A[5], A[6], A[2]]), ("Paper 4: private attributes", [emp_con, B[3]])],
        "ac20r3": [("Paper 3", [A[5], A[6], A[7], A[8], A[11]]), ("Paper 4", [node_get, c41_get, c42_get, emp_get])],
        "ac20r4": [("Paper 3", [A[0], A[4], A[2], A[8]]), ("Paper 4", [B[1], mgr_con, c41_con, magic_con, B[4]])],
        "ac20r5": [("Paper 3", [A[4], A[3], A[6]]), ("Paper 4: overriding a parent method", [B[1], mgr_poly, bike_poly, magic_poly, B[4]])],
        "ac20r6": [("Paper 3", [A[8]]), ("Paper 4: classes that hold objects", [B[2], tree_obj])],
        "ac20r7": [("Paper 4: tree of nodes in an array", [node_obj, node_get, tree_obj]), ("Paper 4: tree of linked node objects", [node25, tree25, R_s25])],
    }
    return sets[name]


OOP_NOTES = {
    "ac20r2": "Encapsulation is examined as a definition or matching task in Paper 3. Paper 4 rewards it inside class declarations, where attributes must be private.",
    "ac20r6": "Containment (aggregation) has been asked about by name only once, in June 2026. The Paper 4 questions below use it without naming it: one class holds objects of another.",
}


# ================================================================ page output
def section(groups, note=""):
    """Summary table plus the questions, grouped under headings."""
    series = {"F/M": 0, "M/J": 1, "O/N": 2}
    rows, body, seen = [], "", set()
    for title, entries in groups:
        body += f"  <h3>{title}</h3>\n"
        for ask, html in entries:
            body += html
            ser, paper, qn = [x.strip() for x in re.search(r'class="src">(.*?)</span>', html)[1].replace("&middot;", "·").split("·")]
            marks = re.search(r'class="mark">(.*?)</span>', html)[1].replace(" marks", "").replace(" mark", "")
            row = (ser, paper.replace("9618/", ""), qn, marks, ask)
            if row[:3] not in seen:
                seen.add(row[:3])
                rows.append(row)
    rows.sort(key=lambda r: (r[0][-4:], series[r[0][:3]], r[1], r[2]))
    table = ('  <div class="tw"><table class="t">\n    <tr><th>Session</th><th>Paper</th><th>Question</th><th>Marks</th><th>What it asks</th></tr>\n'
             + "".join("    <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>\n" for r in rows) + "  </table></div>\n")
    lead = ('  <p class="note">' + (note + " " if note else "") + "Real 9618 questions from 2021 to June 2026, reworded and with mark points summarised. "
            "This is a selection: check the original paper and mark scheme for exact wording. Open each question for a reminder and an answer; each coloured phrase is a mark point.</p>\n")
    return lead + table + body


PAGES = {   # body file: (slug, question groups, note)
    "srch": ("searching-algorithms", lambda: SEARCH, ""),
    "srt": ("sorting-algorithms", lambda: SORT, ""),
    "isort": ("insertion-sort", lambda: INSERT, ""),
    "adt": ("abstract-data-types", lambda: ADT, "Paper 4 questions that code a stack, queue or linked list are on the Implementing ADTs page."),
    "gr": ("graphs", graphs, ""),
    "bst": ("binary-search-tree", lambda: BST, ""),
}
START, END = "<!-- PAST PAPERS (generated by pp19.py) -->\n", "<!-- /PAST PAPERS -->\n"


def inject(name, groups, note):
    f = KIT / f"{name}.body.html"
    s = f.read_text()
    if START in s:
        s = s[:s.index(START)] + "  <h2>Exam-style questions</h2>" + s[s.index(END) + len(END):]
    old = "  <h2>Exam-style questions</h2>"
    assert s.count(old) == 1, name
    new = START + "  <h2>1. Past paper questions</h2>\n" + section(groups, note) + "  <h2>2. Review questions</h2>\n  <p>Written for practice, not taken from past papers.</p>" + "\n" + END
    f.write_text(s.replace(old, new))


if __name__ == "__main__":
    for name, (slug, groups, note) in PAGES.items():
        inject(name, groups(), note)
        title = re.search(r"<title>(.*?)</title>", (ROOT / "artifacts_src" / slug / "index.html").read_text())[1]
        subprocess.run([sys.executable, str(KIT / "assemble.py"), name, title, slug], check=True)

    # the recursion tree page has its own builder
    f = KIT / "recuse" / "tree.html"
    s = f.read_text()
    new = (START + "  <h2>1. Past paper questions</h2>\n" + section(RECTREE, "Recursive tree traversal and search are set as program code in Paper 4.") + "  <h2>2. Review questions</h2>\n" + END)
    if START in s:   # re-run: replace the generated block
        a, b = s.index(START), s.index(END) + len(END)
    else:
        old = "  <h2>Review questions</h2>\n"
        a, b = s.index("  <h2>What 9618 has asked about trees and recursion</h2>"), s.index(old) + len(old)
    f.write_text(s[:a] + new + s[b:])
    subprocess.run([sys.executable, str(KIT / "mk_recuse.py"), "tree"], check=True)
