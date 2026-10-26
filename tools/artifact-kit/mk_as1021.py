"""AS CS 10.2.1: 1D and 2D arrays: declaring, processing, totals and maximum. Run: python3 tools/artifact-kit/mk_as1021.py"""
from ak9 import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def jn(x, y): return ("proc", "", x, y, (4, 4))

F_MIN = flow({
  "S": ("term", "START", 170, 16), "A": ("proc", "Min ← Data[1]\nMinIndex ← 1", 170, 58, (150, 36)), "B": ("proc", "Index ← 2", 170, 102, (120, 28)),
  "D1": ("dec", "Index <= 30 ?", 170, 160, (150, 56)), "O": ("io", "OUTPUT MinIndex", 430, 160, (150, 30)), "E": ("term", "END", 430, 212),
  "D2": ("dec", "Data[Index] < Min ?", 170, 252, (180, 56)), "P": ("proc", "Min ← Data[Index]\nMinIndex ← Index", 430, 252, (160, 36)), "I": ("proc", "Index ← Index + 1", 170, 330, (140, 30))},
  [("S", "b", "A", "t", [], None, None), ("A", "b", "B", "t", [], None, None), ("B", "b", "D1", "t", [], None, None), ("D1", "r", "O", "l", [], "NO", (250, 152)), ("O", "b", "E", "t", [], None, None),
   ("D1", "b", "D2", "t", [], "YES", (176, 204)), ("D2", "r", "P", "l", [], "YES", (262, 244)), ("P", "b", "I", "r", [(430, 330)], None, None), ("D2", "b", "I", "t", [], "NO", (176, 304)), ("I", "l", "D1", "l", [(40, 330), (40, 160)], None, None)], w=540, h=355, cap="find the index of the smallest value")
F_NB = flow({
  "S": ("term", "START", 170, 16), "A": ("proc", "Count ← 0", 170, 56, (120, 28)), "B": ("proc", "Index ← 1", 170, 96, (120, 28)), "D1": ("dec", "Index <= 30 ?", 170, 152, (150, 56)),
  "O": ("io", "OUTPUT Count", 430, 152, (140, 30)), "E": ("term", "END", 430, 204), "D2": ("dec", "Data[Index] <> \"\" ?", 170, 232, (180, 56)), "W": ("io", "OUTPUT Data[Index]", 170, 295, (150, 28)),
  "C": ("proc", "Count ← Count + 1", 170, 337, (150, 28)), "I": ("proc", "Index ← Index + 1", 170, 385, (140, 28))},
  [("S", "b", "A", "t", [], None, None), ("A", "b", "B", "t", [], None, None), ("B", "b", "D1", "t", [], None, None), ("D1", "r", "O", "l", [], "NO", (250, 144)), ("O", "b", "E", "t", [], None, None), ("D1", "b", "D2", "t", [], "YES", (176, 192)),
   ("D2", "b", "W", "t", [], "YES", (176, 268)), ("W", "b", "C", "t", [], None, None), ("C", "b", "I", "t", [], None, None), ("D2", "r", "I", "r", [(340, 232), (340, 385)], "NO", (262, 224)), ("I", "l", "D1", "l", [(40, 385), (40, 152)], None, None)], w=540, h=410, cap="output non-blank elements and a count")
F_99 = flow({
  "S": ("term", "START", 170, 16), "A": ("proc", "Index ← 1", 170, 54, (120, 28)), "J": jn(170, 80), "N": ("io", "INPUT Num", 170, 106, (130, 28)), "D1": ("dec", "Num = 99.9 ?", 170, 164, (140, 54)),
  "E1": ("term", "END", 430, 164), "P": ("proc", "Data[Index] ← Num", 170, 228, (150, 28)), "Q": ("proc", "Index ← Index + 1", 170, 270, (150, 28)), "D2": ("dec", "Index > 20 ?", 170, 330, (140, 54)), "E2": ("term", "END", 430, 330)},
  [("S", "b", "A", "t", [], None, None), ("A", "b", "J", "t", [], None, None), ("J", "b", "N", "t", [], None, None), ("N", "b", "D1", "t", [], None, None), ("D1", "r", "E1", "l", [], "YES", (252, 156)), ("D1", "b", "P", "t", [], "NO", (176, 197)),
   ("P", "b", "Q", "t", [], None, None), ("Q", "b", "D2", "t", [], None, None), ("D2", "r", "E2", "l", [], "YES", (252, 322)), ("D2", "l", "J", "l", [(40, 330), (40, 80)], "NO", (46, 322))], w=540, h=360, cap="store values until 99.9 or the array is full")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>array</b> stores many values of the <b>same data type</b> under one identifier; each element is reached by an <b>index</b>. A 1D array is declared with its bounds and type, <span class="mono">DECLARE Data : ARRAY [1:30] OF REAL</span>; a 2D array has two bounds, <span class="mono">DECLARE Version1 : ARRAY [0:2, 1:15] OF CHAR</span> (floor, room). Before an array can be declared you must know its <b>data type</b> (and its size). Arrays are processed with a <b>loop</b> whose counter is the index: to <b>total</b> or <b>count</b>, initialise before the loop; to find the <b>largest or smallest</b>, start with the first element and replace it when a better one is found; to <b>search</b>, compare each element and stop when found. The benefits of an array over separate variables are that the algorithm is simpler and easier to write, understand and test, you can use a loop to iterate through the values, and many values are stored under a single identifier.</p></div>

  <h2>1 · Declaring and using arrays</h2>
  ''' + pc('''
DECLARE RNum : ARRAY [1:100] OF INTEGER
DECLARE Data : ARRAY [1:120] OF REAL
DECLARE Version1 : ARRAY [0:2, 1:15] OF CHAR

RNum[5] ← 42
Version1[0, 3] ← 'A'          // floor 0, room 3
OUTPUT Data[Index]''') + '''
  <p>Bounds are inclusive: [1:100] has 100 elements and [0:2, 1:15] has 3 × 15 = 45. Use the loop counter as the index: <span class="mono">FOR Index ← 1 TO 100</span>. For a 2D array, use <b>one loop for the first index</b> and <b>another for the second</b> if the whole array is needed.</p>

  <h2>2 · Standard array algorithms</h2>
  <div class="tw"><table class="t">
    <tr><th>Task</th><th>Steps</th></tr>
    <tr><td><b>Total</b></td><td>Total ← 0; loop: Total ← Total + Data[Index]; output after the loop</td></tr>
    <tr><td><b>Count the values in a range</b></td><td>Count ← 0; loop: IF value >= low AND value <= high THEN Count ← Count + 1</td></tr>
    <tr><td><b>Largest value</b></td><td>Max ← Data[1]; loop from 2: IF Data[Index] &gt; Max THEN Max ← Data[Index]; output Max</td></tr>
    <tr><td><b>Index of the smallest</b></td><td>Min ← Data[1]; MinIndex ← 1; loop: IF Data[Index] &lt; Min THEN Min ← Data[Index]; MinIndex ← Index</td></tr>
    <tr><td><b>Odd and even positions</b></td><td>IF Index MOD 2 = 0 THEN even total ELSE odd total</td></tr>
    <tr><td><b>Averages of every three values</b></td><td>FOR IxA ← 1 TO 598 STEP 3: sum three consecutive values, divide by 3, INT, store at IxB, add 1 to IxB</td></tr>
    <tr><td><b>Random values</b></td><td>RNum[Index] ← INT(RAND(200)) + 1 gives 1 to 200</td></tr>
  </table></div>
  ''' + F_MIN + '''
  <p>Unique random values: initialise the array to a rogue value, and for each element generate a number, check it against the values already stored, generate another if it is found, otherwise store it.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Declaring the array without its type, or with the wrong bounds (an array of 120 elements is [1:120]).</li>
    <li>Using a loop that goes one too far (an index of 101 in a 100-element array) or one too short.</li>
    <li>Initialising the total, count or maximum inside the loop.</li>
    <li>Comparing the loop counter instead of the element: <span class="mono">IF Index &gt; Max</span> instead of <span class="mono">IF Data[Index] &gt; Max</span>.</li>
    <li>Outputting the count or total inside the loop when the question asks for a final value.</li>
  </ul>
'''

watch = '''
  <h2>1 · Finding the largest value</h2>
  <div id="stA"></div>
  <h2>2 · A 2D array: floor and room</h2>
  <div id="stB"></div>
  <h2>3 · Averages of three consecutive values</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Largest and smallest</h2>
  <p>Click Step to run the loop over ten values. Edit the values by pressing Shuffle.</p>
  <div class="card"><div class="btnrow"><button id="mx_step">Step</button><button id="mx_shuf">Shuffle</button><button id="mx_reset">Reset</button></div><div id="mxV"></div></div>
  <h2>Lab 2 · Hotel rooms (2D array)</h2>
  <div class="card"><div id="hF"></div><div id="hG"></div><div id="hV" class="verdict"></div></div>
  <h2>Lab 3 · Which algorithm?</h2>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aO"></div></div>
'''

_pr, _prjs = PR(["Which array task?", "Initialise before or inside the loop?", "Match the term to its meaning", "Put the totalling steps in order", "Working out", "Multiple choice"],
  ("Which array algorithm does it describe?", ["Total", "Count in a range", "Largest value", "Index of smallest"], [("Add each element to a running sum", 0), ("Add 1 when an element is between 66 and 173", 1), ("Keep the biggest value seen so far", 2), ("Store the position of the minimum", 3), ("Total ← Total + Data[Index]", 0), ("IF Data[Index] > Max THEN Max ← Data[Index]", 2)], "Match the loop body."),
  ("Should this be set before the loop or inside the loop?", ["Before the loop", "Inside the loop"], [("Count ← 0", 0), ("Reading the element Data[Index]", 1), ("Total ← 0", 0), ("Adding Data[Index] to Total", 1), ("Max ← Data[1]", 0), ("Comparing the element with Max", 1)], "Set starting values first."),
  [["Array", "Many values of the same type under one identifier"], ["Index", "The position of an element"], ["Bounds", "The lowest and highest index"], ["2D array", "Two indexes, for example floor and room"], ["Element", "One value in an array"]],
  ("Put the steps for the largest value in order.", ["Set Max to the first element", "Loop through the remaining elements", "Compare each element with Max", "If it is greater, replace Max", "Output Max after the loop"], "Start, loop, compare, replace, output."),
  [{"q": "DECLARE Data : ARRAY [1:120] OF REAL. How many elements?", "a": 120, "unit": "", "tol": 0.01, "hint": "120 − 1 + 1.", "sol": "<b>120</b>."}, {"q": "DECLARE Version1 : ARRAY [0:2, 1:15] OF CHAR. How many elements?", "a": 45, "unit": "", "tol": 0.01, "hint": "3 × 15.", "sol": "<b>45</b>."}, {"q": "Values: 4, 9, 2, 7. What is the total?", "a": 22, "unit": "", "tol": 0.01, "hint": "4 + 9 + 2 + 7.", "sol": "<b>22</b>."}, {"q": "In the same values, what is the index (from 1) of the smallest?", "a": 3, "unit": "", "tol": 0.01, "hint": "The value 2.", "sol": "<b>3</b>."}, {"q": "Array1 has 600 elements; averages of three consecutive values go in Array2. How many elements are used in Array2?", "a": 200, "unit": "", "tol": 0.01, "hint": "600 ÷ 3.", "sol": "<b>200</b>."}],
  [("An array holds:", ["Values of the same type", "Mixed types", "One value", "Only text"], 0, "Same type."), ("ARRAY [0:99] has:", ["100 elements", "99 elements", "101 elements", "1 element"], 0, "0 to 99."), ("To total an array you:", ["Initialise Total before the loop", "Set Total inside the loop", "Never initialise", "Loop twice"], 0, "Before the loop."), ("A 2D array needs:", ["Two indexes", "Two types", "No loop", "A record"], 0, "Two indexes."), ("An array beats separate variables because:", ["A loop can go through the values", "It uses less memory always", "It is faster always", "It needs no type"], 0, "Iterate with a loop."), ("INT(RAND(200)) + 1 gives:", ["1 to 200", "0 to 199", "1 to 199", "0 to 200"], 0, "1 to 200.")],
  [("Array", "Same type, one name, index."), ("Declare", "ARRAY [lower:upper] OF type."), ("2D array", "[0:2, 1:15]"), ("Total", "Initialise, add in a loop."), ("Largest", "Start with the first; replace."), ("Count", "Initialise; add 1 on a match."), ("Loop counter", "Used as the index."), ("Benefit", "Simpler, loop, one identifier.")])

real = RWNOTE + (
rw("Daily temperatures", "A list of 365 readings in an array lets a loop find the hottest day or the average without 365 separate variables.", "arrays and loops.") +
rw("Hotel booking grid", "Floors and rooms form a 2D grid where each cell says available or booked.", "2D array.") +
rw("A leaderboard", "Finding the top score is the 'largest value' algorithm run over the array of scores.", "largest value.") +
rw("Sensor averages", "A sensor takes three readings at a time; the program averages each group of three to smooth the data.", "averaging consecutive values.") +
rw("Spreadsheet columns", "A column of numbers is like a 1D array: totals, counts and maximums use the same loops.", "array algorithms.")
)

where = [
  ("M/J 2021", "22", "5", "6 + 3 + 4 + 2", "Declare an array of random numbers and count a range; make the values unique; analyse StringClean"),
  ("O/N 2022", "21", "3", "5", "Describe the steps to find and output the largest value in a 200-element array"),
  ("O/N 2022", "21", "5", "5", "Write the procedure Summarise() that averages three consecutive values"),
  ("O/N 2022", "23", "4(a)", "1", "The one piece of information needed before an array can be declared"),
  ("O/N 2023", "23", "2", "5 + 2 + 2", "Flowchart for the index of the smallest value; benefits of an array; declare a REAL array"),
  ("M/J 2024", "21", "4", "6", "Write the function Check() totalling odd and even index elements"),
  ("O/N 2025", "21", "2", "5", "Complete a flowchart to output the non-blank elements and a count"),
  ("O/N 2025", "21", "4", "6 + 2 + 1", "Complete Store(); benefits of a file instead of an array"),
  ("O/N 2025", "22", "2", "5", "Complete a flowchart to store values until 99.9 or the array is full"),
  ("O/N 2025", "23", "4", "6", "Complete Store() to extract three-digit numbers from a string into an array"),
  ("M/J 2026", "21", "9", "2 + 6 + 3 + 7", "Declare a 2D array for hotel rooms; the enquiry program; a record version")]

past = '''  <p class="note">Array algorithms are the core of Paper 2: a fresh scenario every series with the same marking points (declare, loop, test, update, output). Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "22", "Q5"), "6 + 3 + 4 + 2 marks", "Write / Describe",
  "(a) A student writes a program to declare a 1D array RNum of 100 INTEGER elements, assign each element a random value in the range 1 to 200 inclusive and count and output how many numbers were between 66 and 173 inclusive. (i) Write pseudocode. (ii) Describe the changes needed so each element contains a unique value. (b) The function StringClean(InString) loops through the string with NextChar ← LCASE(MID(InString, Counter, 1)) and the test IF NOT((NextChar < 'a') OR (NextChar > 'z')) THEN OutString ← OutString & NextChar. Write a simplified version of that statement.", "ARRAY [1:100]; RAND; AND for the range. Rogue value, check against stored.",
  "<p><b>(a)(i)</b> " + mks(["Array declaration", "Loop for 100 iterations", "Array element index syntax on the left of the assignment in the loop", "RAND() used to generate a value in range and assign it to the element", "Check if in range and increment Count in the loop", "Output Count after the loop"]) + "</p>" + pc('''
DECLARE RNum : ARRAY[1:100] OF INTEGER
DECLARE Index, Count : INTEGER
Count ← 0
FOR Index ← 1 TO 100
   RNum[Index] ← INT(RAND(200)) + 1
   IF RNum[Index] >= 66 AND RNum[Index] <= 173 THEN
      Count ← Count + 1
   ENDIF
NEXT Index
OUTPUT Count''') + "<p><b>(ii)</b> Any three: " + mks(["Initialise the array to a rogue value to show an element is unassigned", "Add a conditional loop to generate and store a random number in the correct range", "check the stored number against the values already in the array", "if it is found generate another, otherwise add it to the array and exit the loop"], "a") + "</p><p><b>(b)(ii)</b> " + mks(["IF (NextChar >= 'a') AND (NextChar <= 'z') THEN (IF ... AND ... with both conditions)"], "b") + "</p>", "Using INT(RAND(200)) alone: it gives 0 to 199, so 1 must be added.") + peq(SRC("w22", "21", "Q3"), "5 marks", "Describe",
  "A 1D array Data of 200 INTEGER elements has unique values. An algorithm searches for the largest value and outputs it. Describe the steps. Do not include pseudocode statements.", "Max variable, first element, loop of 200, compare, output.",
  "<p>Any five: " + mks(["Declare a variable (an integer) Max", "Assign the value of the first (or any) element to Max", "Set up a loop to repeat 200 times, from the start to the end of the array", "Use the loop counter as the array index", "If the value of the current element is greater than Max", "then assign that value to Max", "After the loop, output Max"]) + "</p>", None) + peq(SRC("w22", "21", "Q5"), "5 marks", "Write",
  "Array1 (600 INTEGER) holds sensor samples taken three at a time; Array2 has 200 elements. A procedure Summarise() calculates the average of three consecutive values from Array1 and writes the result to Array2, repeating for all values (for example 10, 20, 15 gives 15). Write pseudocode for Summarise().", "STEP 3 loop; sum, divide by 3, INT; second index.",
  "<p>" + mks(["Procedure heading and ending and declaration of both indexes", "Loop to process all elements from Array1", "Sum three consecutive values and divide by 3 in the loop", "Convert the result to an integer", "Assign the value to the correct element of Array2", "Increment the Array2 index"]) + "</p>" + pc('''
PROCEDURE Summarise()
   DECLARE Value : REAL
   DECLARE IxA, IxB : INTEGER
   IxB ← 1
   FOR IxA ← 1 TO 598 STEP 3
      Value ← Array1[IxA] + Array1[IxA + 1] + Array1[IxA + 2]
      Value ← Value / 3
      Array2[IxB] ← INT(Value)
      IxB ← IxB + 1
   NEXT IxA
ENDPROCEDURE'''), "Looping to 600 with a step of 3: the last group would run past the end of the array.") + peq(SRC("w22", "23", "Q4(a)"), "1 mark", "State",
  "A program contains a 1D array DataItem with 100 elements. State the one additional piece of information required before the array can be declared.", "The type of data to be stored.",
  "<p>" + mks(["The data type (of the items to be stored)"]) + "</p>", None) + peq(SRC("w23", "23", "Q2"), "5 + 2 + 2 marks", "Draw / Explain / Write",
  "Data is a 1D array of 30 integers, all values unique. (a) Draw a flowchart for an algorithm that outputs the index of the element with the smallest value. (b) Explain the benefits of using an array instead of separate variables. (c) The array must now hold 120 elements and each value may include a decimal place. Write a pseudocode statement to declare it.", "Min and MinIndex; loop; compare; update both; output.",
  "<p><b>(a)</b> " + mks(["Initialise Min to the first value and MinIndex to 1", "Loop through 29 more values (or 30 in total)", "Compare the element from Data[] with Min", "Set the new Min and save MinIndex when the element is smaller, in the loop", "Output MinIndex"]) + "</p>" + F_MIN + "<p><b>(b)</b> " + mks(["It simplifies the algorithm: easier to write, understand, test and debug", "It is possible to iterate through the values with a loop, and many values are stored under one identifier"], "a") + "</p><p><b>(c)</b> " + mks(["DECLARE Data : ARRAY[1:120] OF REAL (the bounds and the REAL type)"], "b") + "</p>", None) + peq(SRC("s24", "21", "Q4"), "6 marks", "Write",
  "A global 1D array Data has 100 INTEGER elements. A function Check() will total the element values in odd index locations (1, 3 ... 99) and in even index locations (2, 4 ... 100), and return one of the strings 'Odd', 'Even' or 'Same' to indicate which total is the greater, or whether they are the same. Write pseudocode for Check().", "Index MOD 2; two totals; compare after the loop.",
  "<p>" + mks(["Function heading, ending and return type", "Declare Odd, Even and Index as integers", "Initialise Odd and Even", "Loop for 100 iterations", "Sum the odd and even element values in the loop", "Compare Odd and Even after the loop and return the appropriate string"]) + "</p>" + pc('''
FUNCTION Check() RETURNS STRING
   DECLARE Odd, Even, Index : INTEGER
   Odd ← 0
   Even ← 0
   FOR Index ← 1 TO 100
      IF Index MOD 2 = 0 THEN
         Even ← Even + Data[Index]
      ELSE
         Odd ← Odd + Data[Index]
      ENDIF
   NEXT Index
   IF Odd > Even THEN
      RETURN "Odd"
   ELSE
      IF Even > Odd THEN
         RETURN "Even"
      ELSE
         RETURN "Same"
      ENDIF
   ENDIF
ENDFUNCTION'''), "Returning inside the loop. The comparison must be made after the loop.") + peq(SRC("w25", "21", "Q2"), "5 marks", "Complete",
  "Data is a global 1D array of 30 STRING elements. An algorithm will output all non-blank elements (not an empty string) and the final total of the number of elements output. Complete the program flowchart.", "Index and Count; loop 30; test for non-empty; output; count; final output.",
  "<p>" + mks(["Initialisation of the variables used as the array index and the count", "Loop through exactly 30 elements", "Test for an empty (or non-empty) string in the current element", "Increment the count if appropriate in the loop", "Both required outputs under the correct conditions"]) + "</p>" + F_NB, None) + peq(SRC("w25", "21", "Q4"), "6 + 2 + 1 marks", "Complete / Give / State",
  "A global 1D array Number has 20 REAL elements. A procedure Store() inputs up to 20 real values one at a time. Step 1: store the first value in the first element. Step 2: check each later value; if it is larger than the previous value input, assign it to the next element, otherwise go to step 4. Step 3: repeat from step 2 unless the array is full. Step 4: output the count of values stored with a message. (a) Complete the pseudocode for Store(). (b) The sequence may be longer than 20 and the values must be available to another program, so a text file replaces the array. (i) Give two benefits of using a text file instead of an array. (ii) State a change needed before each value is written to the file.", "Two tests in a WHILE; LastNum; index. File: any size, available to other programs; convert to a string.",
  "<p><b>(a)</b> " + mks(["Declare local variables: Index as integer, ThisNum and LastNum as real", "Input a value and assign it to the first element", "An attempt at a conditional loop including both tests", "A completely correct conditional loop with both tests", "Assign the input value to the current element if it is greater than the previous one, and input the next value, in the loop", "A final output giving the count stored, with a message, after the loop"]) + "</p>" + pc('''
PROCEDURE Store()
   DECLARE ThisNum, LastNum : REAL
   DECLARE Index : INTEGER
   INPUT ThisNum
   LastNum ← ThisNum
   Number[1] ← ThisNum
   INPUT ThisNum
   Index ← 2
   WHILE Index < 21 AND ThisNum > LastNum
      Number[Index] ← ThisNum
      LastNum ← ThisNum
      Index ← Index + 1
      IF Index < 21 THEN
         INPUT ThisNum
      ENDIF
   ENDWHILE
   OUTPUT Index - 1, " values were stored in the array"
ENDPROCEDURE''') + "<p><b>(b)</b> " + mks(["(i) The file can hold more than 20 values (it is not limited by a fixed size), and it can be accessed by another program as data (it is saved permanently)", "(ii) Each value must be converted to a string before it is written to the file"], "a") + "</p>", None) + peq(SRC("w25", "22", "Q2"), "5 marks", "Complete",
  "Data is a global 1D array of 20 REAL elements. An algorithm inputs a sequence of real values, one at a time, assigns each to consecutive elements starting at index 1, and ends when 99.9 is input or all 20 elements have been assigned (99.9 must not be stored). Complete the program flowchart.", "Index; input in a loop; test 99.9; test full; store and increment.",
  "<p>" + mks(["Initialisation of the array index", "Input the number in a loop", "Test for the termination value 99.9 and correct ending", "Test for the array full (or a maximum of 20 iterations) and correct ending", "Assign the number to the array element and increment the index"]) + "</p>" + F_99, None) + peq(SRC("w25", "23", "Q4"), "6 marks", "Complete",
  "A global 1D array Data has 20 INTEGER elements. A global string NumString holds three-digit numbers separated by commas, for example \"101,456,219,754,328\" (at least four numbers; the total is unknown). A procedure Store() extracts one three-digit number at a time, converts it to an integer and assigns it to the next element starting at index 1, ending when all numbers have been stored or the array is full. Complete the pseudocode for Store().", "MID(NumString, StartPos, 3); step 4; two conditions.",
  "<p>" + mks(["Declare all the local variables used", "A conditional loop while the end of the string is not reached", "and the array is not full", "Attempted use of MID() (or LEFT and RIGHT)", "Correct extraction of the next three-digit substring in the loop", "Convert it to an integer and assign it to the array element in the loop", "Increment the array index by 1 and the start position by 4"]) + " (max 6)</p>" + pc('''
PROCEDURE Store()
   DECLARE Index, StartPos, ThisNum : INTEGER
   DECLARE ThisString : STRING
   Index ← 1
   StartPos ← 1
   WHILE StartPos < LENGTH(NumString) AND Index < 21
      ThisString ← MID(NumString, StartPos, 3)
      ThisNum ← STR_TO_NUM(ThisString)
      Data[Index] ← ThisNum
      Index ← Index + 1
      StartPos ← StartPos + 4
   ENDWHILE
ENDPROCEDURE'''), None) + peq(SRC("s26", "21", "Q9(a)(b)"), "2 + 6 marks", "Write",
  "A hotel has three floors numbered 0 to 2 with 15 rooms (numbered 1 to 15) on each floor. The availability data is stored in a 2D array Version1: the first index is the floor, the second the room; each cell stores 'A' (available) or 'B' (booked). (a) Write the declaration for Version1. (b) An enquiry program inputs a floor number, outputs all room numbers available on that floor and outputs the number of rooms available.", "ARRAY [0:2, 1:15] OF CHAR; loop 15 rooms; test 'A'; count.",
  "<p><b>(a)</b> " + mks(["DECLARE Version1 : ARRAY [0:2, 1:15]", "OF CHAR"]) + "</p><p><b>(b)</b> " + mks(["Declaration of all integer variables", "Input of the floor number (with a prompt)", "A loop for 15 iterations", "Test the array element to see if the room is available ('A')", "Initialise and increment Count and output the room number", "Output the final count line with the message outside the loop"], "a") + "</p>" + pc('''
DECLARE RoomNumber, FloorNumber, Count : INTEGER
Count ← 0
OUTPUT "Floor number: "
INPUT FloorNumber
FOR RoomNumber ← 1 TO 15
   IF Version1[FloorNumber, RoomNumber] = 'A' THEN
      OUTPUT RoomNumber
      Count ← Count + 1
   ENDIF
NEXT RoomNumber
OUTPUT NUM_TO_STR(Count) & " room(s) available"'''), None)

review = req("5 marks", "Write", "A global array Marks has 30 INTEGER elements. Write pseudocode that outputs the average mark, as a REAL.", "Total, divide by 30.", "<p>" + mks(["Declare Total (integer or real), Index and Average", "Initialise Total before the loop", "Loop through 30 elements adding Marks[Index]", "Divide the total by 30", "Output the average after the loop"]) + "</p>" + pc("DECLARE Total, Index : INTEGER\nDECLARE Average : REAL\nTotal ← 0\nFOR Index ← 1 TO 30\n   Total ← Total + Marks[Index]\nNEXT Index\nAverage ← Total / 30\nOUTPUT Average"), None) + req("4 marks", "Write", "Write pseudocode to count how many elements of Marks are 50 or more and output the count.", "Count with IF.", "<p>" + mks(["Initialise Count", "Loop through 30 elements", "IF Marks[Index] >= 50 THEN Count ← Count + 1", "Output Count after the loop"]) + "</p>", None) + req("2 marks", "Write", "Write the declaration of a 2D array Grid with 8 rows (1 to 8) and 8 columns (1 to 8) of CHAR.", "Two bounds.", "<p>" + mks(["DECLARE Grid : ARRAY [1:8, 1:8]", "OF CHAR"]) + "</p>", None) + req("3 marks", "Explain", "Explain why storing 50 test marks in an array is better than in 50 separate variables.", "Loop, one name, simpler.", "<p>" + mks(["One identifier holds all the values", "A loop can process every value", "The algorithm is shorter and easier to write and test"]) + "</p>", None) + req("3 marks", "Describe", "Describe (no pseudocode) how to find the largest value in an array.", "Max, loop, compare.", "<p>" + mks(["Set Max to the first element", "Loop through the rest comparing each with Max and replacing Max if greater", "Output Max after the loop"]) + "</p>", None)

tips = tips_html([
  ("Declare: bounds and type.", "ARRAY [1:120] OF REAL."),
  ("Initialise before the loop.", "Total, Count, Max."),
  ("The loop counter is the index.", "Data[Index], not Index."),
  ("2D arrays: two loops or two indexes.", "[floor, room]."),
  ("Output after the loop.", "A final count or total."),
  ("Three benefits.", "Simple, iterate, one identifier."),
], [("an array", "A set of values of one type under one identifier."), ("an index", "The position used to reach an element."), ("bounds", "The lowest and highest index."), ("a rogue value", "A value that cannot occur, used as a marker.")],
  [("Declare", "Write the array declaration."), ("Write", "Write the pseudocode."), ("Describe", "Steps in words."), ("Complete", "Finish the flowchart or code.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const vals = [7, 12, 3, 18, 9]; const draw = (s) => { const k = Math.round(s.i); let mx = vals[0]; for (let i = 1; i <= Math.min(k, 4); i++) if (vals[i] > mx) mx = vals[i]; let o = ""; vals.forEach((v, i) => o += SV.rect(20 + i * 76, 20, 68, 34, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(54 + i * 76, 43, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(54 + i * 76, 68, "[" + (i + 1) + "]", "sm", { "text-anchor": "middle" }));
    o += SV.text(20, 108, "Max = " + mx, "lbl bd t3"); return o; };
  Lib.stepper($("#stA"), { w: 420, h: 125, label: "Largest", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Max starts as the first element: 7.", "12 > 7: Max = 12.", "3 is not greater: Max stays 12.", "18 > 12: Max = 18.", "9 is not greater. Output 18."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const g = ["AAB", "BAA", "ABA"]; let o = SV.text(20, 14, "Version1[floor, room]", "sm"); g.forEach((r, f) => r.split("").forEach((c, m) => o += SV.rect(60 + m * 60, 22 + f * 34, 54, 28, c === "A" ? "f1" : "f2", { rx: 4 }) + SV.text(87 + m * 60, 41 + f * 34, c, "lbl bd", { "text-anchor": "middle" }))); for (let f = 0; f < 3; f++) o += SV.text(20, 41 + f * 34, "floor " + f, "sm"); for (let m = 0; m < 3; m++) o += SV.text(87 + m * 60, 130, "room " + (m + 1), "sm", { "text-anchor": "middle" });
    if (k >= 1) o += SV.rect(56, 18, 190, 36, "ax", { rx: 4, style: "fill:none;stroke:var(--accent);stroke-width:2" }); o += SV.text(280, 50, ["", "Version1[0, 3] is the 3rd room on floor 0", "loop through the rooms of one floor"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 145, label: "2D array", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Each cell holds A (available) or B (booked): three floors by rooms.", "The first index is the floor, the second the room.", "To list a floor, loop through its rooms."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const a = [10, 20, 15, 40, 41, 42]; const draw = (s) => { const k = Math.round(s.i); let o = ""; a.forEach((v, i) => o += SV.rect(20 + i * 70, 20, 62, 30, Math.floor(i / 3) === k - 1 ? "f1" : "cell", { rx: 4 }) + SV.text(51 + i * 70, 40, v, "lbl bd", { "text-anchor": "middle" })); const avg = k >= 1 ? Math.floor((a[0] + a[1] + a[2]) / 3) : null, avg2 = k >= 2 ? Math.floor((a[3] + a[4] + a[5]) / 3) : null;
    if (avg !== null) o += SV.rect(20, 80, 100, 30, "f3", { rx: 4 }) + SV.text(70, 100, "Array2[1] = " + avg, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); if (avg2 !== null) o += SV.rect(140, 80, 110, 30, "f3", { rx: 4 }) + SV.text(195, 100, "Array2[2] = " + avg2, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 130, label: "Averages", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Six sensor samples in Array1.", "(10 + 20 + 15) / 3 = 15 stored in Array2[1].", "(40 + 41 + 42) / 3 = 41 stored in Array2[2]. IxA moves on by 3."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let vals, k; const reset = () => { k = 0; paint(); }; const shuf = () => { vals = Array.from({ length: 10 }, () => 1 + Math.floor(Math.random() * 99)); k = 0; paint(); };
  const paint = () => { let mx = vals[0], mi = 1, mn = vals[0], ni = 1; for (let i = 1; i <= k; i++) { if (vals[i] > mx) { mx = vals[i]; mi = i + 1; } if (vals[i] < mn) { mn = vals[i]; ni = i + 1; } }
    let h = '<div class="tw"><table class="t mono"><tr><th>index</th>' + vals.map((_, i) => `<th>${i + 1}</th>`).join("") + "</tr><tr><td>Data</td>" + vals.map((v, i) => `<td style="${i === k ? "background:var(--accent-soft);font-weight:700" : i < k ? "opacity:.6" : ""}">${v}</td>`).join("") + "</tr></table></div>"; $("#mxV").innerHTML = h + `<div class="verdict">After checking element ${k + 1}: Max = <b>${mx}</b> (index ${mi}), Min = <b>${mn}</b> (index ${ni}).</div>`; };
  vals = [34, 78, 12, 90, 45, 23, 67, 5, 88, 51]; $("#mx_step").onclick = () => { if (k < vals.length - 1) { k++; paint(); } }; $("#mx_shuf").onclick = shuf; $("#mx_reset").onclick = reset; reset();
})();
(function () {
  const g = [["A", "B", "A", "A", "B"], ["B", "A", "A", "B", "A"], ["A", "A", "B", "A", "A"]]; let fl = 0; const bar = $("#hF");
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>floor ↓ room →</th>' + [1, 2, 3, 4, 5].map((r) => `<th>${r}</th>`).join("") + "</tr>"; g.forEach((r, f) => h += `<tr style="${f === fl ? "background:var(--accent-soft);font-weight:700" : ""}"><td>${f}</td>` + r.map((c) => `<td>${c}</td>`).join("") + "</tr>"); $("#hG").innerHTML = h + "</table></div>"; const av = []; g[fl].forEach((c, i) => { if (c === "A") av.push(i + 1); }); $("#hV").innerHTML = `Floor <b>${fl}</b>: available rooms ${av.join(", ")}. The loop <span class="mono">FOR RoomNumber ← 1 TO 5</span> tests <span class="mono">Version1[${fl}, RoomNumber] = 'A'</span> and counts <b>${av.length}</b>.`; };
  [0, 1, 2].forEach((f) => { const b = document.createElement("button"); b.textContent = "Floor " + f; b.onclick = () => { fl = f; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (f === 0) b.className = "on"; bar.appendChild(b); }); paint();
})();
btnTable("aB", "aO", [
  ["Add all the marks", "Total ← 0; Total ← Total + Marks[Index]", "Total"],
  ["How many marks are 50 or more", "Count ← 0; IF Marks[Index] >= 50 THEN Count ← Count + 1", "Count"],
  ["The highest mark", "Max ← Marks[1]; IF Marks[Index] > Max THEN Max ← Marks[Index]", "Largest"],
  ["Where the lowest mark is", "Min ← Marks[1]; MinIndex ← 1; update both when smaller", "Index of smallest"]
], ["Need", "Pseudocode", "Algorithm"]);
''' + _prjs

finish("as-10-2-1-arrays-processing", "as1021", "Arrays: Declaring and Processing",
  "Declaring 1D and 2D arrays, looping through them, totals, counts, largest and smallest values, averages, and flowcharts for array algorithms, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "10.2.1", "10 · Data types and structures", "section 10.2 Arrays", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on arrays (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
