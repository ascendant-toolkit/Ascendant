"""AS CS 10.4: abstract data types. Run: python3 tools/artifact-kit/mk_as104.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t mono"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>abstract data type (ADT)</b> is a collection of data together with the operations allowed on it, described without saying how it is stored. A <b>stack</b> is last in, first out (LIFO): PUSH adds to the top and POP removes from the top, using a <b>top of stack pointer</b>. A <b>queue</b> is first in, first out (FIFO): items are added at the <b>end</b> (rear) and removed from the <b>front</b>, each with its own pointer; a <b>circular</b> queue wraps round so empty locations are reused. A <b>linked list</b> stores each item in a <b>node</b> with a <b>pointer</b> to the next node, a <b>start pointer</b> to the first node, a <b>null pointer</b> at the end and a <b>free list</b> of unused nodes. All three are built from <b>arrays</b> (or records) and variables for the pointers.</p></div>

  <h2>1 · Stack (LIFO)</h2>
  <ul>
    <li>PUSH: check the stack is not full, store the value where the pointer says, move the pointer; POP: check the stack is not empty, take the value, move the pointer back.</li>
    <li>The value on the stack for the longest time is at the <b>bottom</b>; the next value out is at the <b>top</b>.</li>
    <li>A stack can grow upwards (index 1, 2, 3 ...) or down through memory (207, 206 ...). Read the question to see which way, and whether the pointer is at the last value added or the next free place.</li>
    <li>Uses: Back button history, undo, returning from procedure calls, evaluating expressions.</li>
  </ul>
  ''' + pc('''
// stack in ThisStack[1:60], SP = next free index, OnStack = items held
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
   IF OnStack = 60 THEN
      RETURN FALSE            // stack is full
   ENDIF
   ThisStack[SP] ← ThisValue
   SP ← SP + 1
   OnStack ← OnStack + 1
   RETURN TRUE
ENDFUNCTION''') + '''
  <p>Initially SP is 1 and OnStack is 0. The array elements need no initial values: an element cannot be popped until a value has been pushed (which overwrites it).</p>

  <h2>2 · Queue (FIFO)</h2>
  <ul>
    <li>Front pointer: the next item to be removed. End pointer: the last item added.</li>
    <li><b>Add:</b> check the queue is not full; move the end pointer on by 1 (back to 0 after the last location); store the item at the end pointer.</li>
    <li><b>Remove:</b> check the queue is not empty; copy the item at the front pointer; move the front pointer on by 1 (wrapping round).</li>
    <li>If the front and end pointers are equal there is <b>one</b> item in the queue.</li>
    <li>Number of items in a circular queue: end − front + 1, and if that is not above zero add the number of locations.</li>
  </ul>
  ''' + pc('''
// adding to a circular queue held in an array of 8 (0 to 7)
IF Items = 8 THEN
   OUTPUT "Queue full"
ELSE
   EndPtr ← EndPtr + 1
   IF EndPtr > 7 THEN
      EndPtr ← 0            // wrap round
   ENDIF
   Queue[EndPtr] ← NewItem
   Items ← Items + 1
ENDIF''') + '''

  <h2>3 · Linked list</h2>
  <ul>
    <li>A <b>node</b> holds a data item and a <b>pointer</b> to the next node. The <b>start pointer</b> points to the first node; the last node has a <b>null pointer</b> (written Ø).</li>
    <li>Items are accessed in order by following the pointers. The order of the data is set by the pointers, so an item is added or deleted by changing pointers only; no data is moved (an array would have to shift items to keep the order).</li>
    <li>Disadvantages: extra memory for the pointers, and more complex to set up and program.</li>
    <li><b>Free list:</b> the unused nodes are linked together too. After initialisation the start pointer is null, the free list pointer points to the first node and <b>all</b> the nodes are on the free list.</li>
    <li><b>Implementation:</b> two 1D arrays (one for data, one for pointers, the same index being one node) and two integer variables (start pointer, free list pointer); or one array of records with a data field and a pointer field. A value outside the array indices (such as 0) is the null pointer.</li>
    <li><b>Insert:</b> take the first node from the free list (move the free pointer on), store the data in it, set its pointer to the node that should follow it, and set the pointer of the node before it to point to the new node. <b>Delete:</b> change the previous node's pointer to skip the deleted node and add that node to the free list.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Stack</th><th>Queue</th><th>Linked list</th></tr>
    <tr><td><b>Order</b></td><td>LIFO</td><td>FIFO</td><td>Follow the pointers</td></tr>
    <tr><td><b>Pointers</b></td><td>Top of stack</td><td>Front and end</td><td>Start, free list, one per node</td></tr>
    <tr><td><b>Add</b></td><td>Push on top</td><td>At the end</td><td>Anywhere by changing pointers</td></tr>
    <tr><td><b>Remove</b></td><td>Pop from top</td><td>From the front</td><td>Anywhere by changing pointers</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Not checking for a full stack/queue before adding, or an empty one before removing.</li>
    <li>Forgetting wrap-around in a circular queue.</li>
    <li>Moving the pointer in the wrong direction (stack grows down in memory in some questions).</li>
    <li>In a linked list, drawing arrows but leaving out the start pointer, the null pointer or the free list.</li>
    <li>Saying "it is faster" for a linked list: the advantage is that only the pointers change.</li>
  </ul>
'''

watch = '''
  <h2>1 · Push and pop</h2>
  <div id="stA"></div>
  <h2>2 · A circular queue</h2>
  <div id="stB"></div>
  <h2>3 · Inserting into a linked list</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Stack</h2>
  <p>Memory locations 200 to 207. The pointer shows the last value added. Push letters and pop them.</p>
  <div class="card"><div class="btnrow"><button id="sk_push">PUSH next letter</button><button id="sk_pop">POP</button><button id="sk_reset">Reset</button></div><div id="skV"></div></div>
  <h2>Lab 2 · Circular queue of 8</h2>
  <div class="card"><div class="btnrow"><button id="qu_add">Add item</button><button id="qu_rem">Remove item</button><button id="qu_reset">Reset</button></div><div id="quV"></div></div>
  <h2>Lab 3 · Linked list in two arrays</h2>
  <p>Insert words in alphabetical order, or delete one. Watch the pointer array and the free list: no data moves.</p>
  <div class="card"><div class="btnrow" id="llB"></div><div class="btnrow"><button id="ll_del">Delete the last word added</button><button id="ll_reset">Reset</button></div><div id="llV"></div></div>
'''

_pr, _prjs = PR(["Which ADT?", "Pointer words", "Match the term", "Put the add-to-queue steps in order", "Working out", "Multiple choice"],
  ("Which ADT is described?", ["Stack", "Queue", "Linked list"], [("Last in, first out", 0), ("First in, first out", 1), ("Each node has a pointer to the next node", 2), ("Browser Back button history", 0), ("Print jobs waiting for a printer", 1), ("Items can be inserted by changing pointers only", 2)], "LIFO stack; FIFO queue; pointers linked list."),
  ("Which pointer or term?", ["Start pointer", "Null pointer", "Free list pointer"], [("Points to the first node in the list", 0), ("Marks the end of the list (Ø)", 1), ("Points to the first unused node", 2), ("The value 0 when array indices are 1 to 8", 1), ("After initialisation it points to the first node", 2), ("Is null when the list is empty", 0)], "Start first; null end; free unused."),
  [["PUSH", "Add to the top of a stack"], ["POP", "Remove from the top of a stack"], ["Front pointer", "Next item to be removed from a queue"], ["End pointer", "Last item added to a queue"], ["Node", "A data item with a pointer"]],
  ("Put the steps for adding to a circular queue in order.", ["Check the queue is not full", "Increment the end pointer", "If past the last location, set it to the first (wrap round)", "Store the item at the end pointer", "Increment the count of items"], "Check, move, wrap, store, count."),
  [{"q": "Stack at 200 to 207; TOS points to 203. Three POPs are done. Which location does TOS point to afterwards? (The stack grows downwards in memory, so a POP raises the address.)", "a": 206, "unit": "", "tol": 0.01, "hint": "203 + 3.", "sol": "<b>206</b>."}, {"q": "A queue of 10 locations has the front pointer at 5 and the end pointer at 1 (wrapped). How many items?", "a": 7, "unit": "", "tol": 0.01, "hint": "5 to 9 is 5; 0 to 1 is 2.", "sol": "<b>7</b>."}, {"q": "A stack array holds 60 values. After 25 pushes and 9 pops, how many values are on the stack?", "a": 16, "unit": "", "tol": 0.01, "hint": "25 − 9.", "sol": "<b>16</b>."}, {"q": "A stack grows up from index 1. SP points to the next free place. After 12 pushes, what is SP?", "a": 13, "unit": "", "tol": 0.01, "hint": "1 + 12.", "sol": "<b>13</b>."}, {"q": "A linked list has 8 nodes. After initialisation, how many nodes are on the free list?", "a": 8, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>8</b>."}],
  [("The next item out of a stack is:", ["The last one pushed", "The first one pushed", "A random one", "The largest"], 0, "LIFO."), ("A queue works on:", ["FIFO", "LIFO", "Random order", "Alphabetical order"], 0, "FIFO."), ("In a circular queue, the end pointer after the last location goes to:", ["The first location", "The front pointer", "Null", "Zero items"], 0, "Wraps."), ("In a linked list the last node holds:", ["A null pointer", "The start pointer", "The free list", "No data"], 0, "Null."), ("A disadvantage of a linked list compared with an array is:", ["It stores extra pointers", "Insertion needs data to move", "It cannot hold strings", "It is always full"], 0, "Pointers need memory."), ("Front and end pointers are equal. The queue holds:", ["One item", "No items", "A full queue", "Two items"], 0, "One.")],
  [("Stack", "LIFO. PUSH, POP, top of stack."), ("Queue", "FIFO. Front and end pointers."), ("Circular", "Wraps round to reuse locations."), ("Node", "Data and a pointer."), ("Start pointer", "First node."), ("Null pointer", "End of list (Ø)."), ("Free list", "The unused nodes."), ("Full / empty", "Check before add / remove.")])

real = RWNOTE + (
rw("A browser's Back and Forward buttons", "Two stacks hold the pages you have left: Back pops the most recent page, and the page you are leaving is pushed onto the Forward stack.", "stack.") +
rw("Undo in a document", "Each change is pushed on a stack; Undo pops the most recent change.", "stack.") +
rw("A printer queue", "Print jobs are added at the end and the printer takes the job at the front, so the first to arrive is printed first.", "queue.") +
rw("A keyboard buffer", "Key presses wait in a circular buffer until the program reads them in the order they were typed.", "circular queue.") +
rw("A music playlist", "Each track holds a pointer to the next one, so a track can be inserted anywhere without moving the others.", "linked list.")
)

where = [
  ("M/J 2021", "22", "3", "6", "Identify a linked list, its start and null pointers; draw it after sorting"),
  ("O/N 2021", "21", "3", "13", "Add/remove in a circular queue; state when pointers are equal; the add algorithm"),
  ("M/J 2022", "21", "4", "6", "A stack in locations 200 to 207: longest-held value, pointer after POPs, state after operations"),
  ("O/N 2022", "21", "4", "10", "Ordered linked list after adds and deletes; advantages and disadvantages over an array; implementation"),
  ("M/J 2023", "22", "3", "10", "Add two items to a circular queue; count items; FileToQueue() algorithm"),
  ("O/N 2023", "22", "3", "9", "A linked list in two arrays; the steps to insert a node using the free list"),
  ("M/J 2024", "21", "3", "8", "Linked list after initialisation; the variable and array design"),
  ("O/N 2024", "22", "3", "7", "Initial values for SP and OnStack; Push() function"),
  ("M/J 2026", "22", "4", "9", "Two stacks for a browser's Back/Forward buttons")]

STK = [("'F'", "TopOfStack")]
past = '''  <p class="note">The ADT question appears in most Paper 2 papers: a diagram to complete, a short explanation, and sometimes an algorithm. The diagrams below are re-drawn as tables; check the original paper for the printed layout.</p>
''' + peq(SRC("s21", "22", "Q3"), "6 marks", "Identify / Give / Complete",
  "A diagram shows Dolphin, Cat, Fish and Elk as nodes, each with an arrow to the next, a pointer labelled A pointing at Dolphin and a null item labelled B after Elk. (a) Identify this type of ADT. (b) Give the technical term for A. (c) Give the technical term for B and explain the meaning of its value. (d) Complete the diagram to show the ADT after the data has been sorted in alphabetical order.", "Linked list; start pointer; null pointer; reorder the arrows.",
  "<p><b>(a)</b> " + mks(["Linked list"], "a") + " <b>(b)</b> " + mks(["Start pointer"], "a") + " <b>(c)</b> " + mks(["Name: Null pointer", "Meaning: there are no further nodes in the list"], "b") + "</p><p><b>(d)</b> " + mks(["Start pointer pointing to the Cat node", "Remaining arrows: Cat → Dolphin → Elk → Fish"], "b") + "</p>", "Moving the data. In a linked list the nodes stay where they are; only the pointers are changed.") + peq(SRC("w21", "21", "Q3"), "5 + 5 + 3 marks", "Describe / Complete",
  "A queue ADT holds up to eight items in locations 0 to 7. The front of queue pointer points to the next item to be removed, the end of queue pointer to the last item added, and the queue is circular. The queue holds Frog (0), Cat (1), Fish (2), Elk (3) with front at 0 and end at 3. (a)(i) Describe how \"Octopus\" is added. (ii) Describe how the next item is removed and stored in AnimalName. (iii) Describe the state of the queue when the front and end pointers have the same value. (b)(i) Add Wasp, Bee and Mouse, then remove two items; show the queue. (ii) Another queue holds Frog, Cat, Fish, Elk (front, 3), Wasp, Bee, Mouse (end, 6), Ant (7); remove one item, then add Dolphin and Shark. (c) The queue is in a 1D array. Describe the algorithm to modify the end of queue pointer when adding, detecting any error conditions.", "End pointer moves on, store at it. Take the front, move front. One item. Wrap round.",
  "<p><b>(a)(i)</b> " + mks(["The end of queue pointer moves on to location 4 (incremented by 1)", "\"Octopus\" is stored in the location the end pointer refers to (location 4)"], "a") + "</p><p><b>(ii)</b> " + mks(["\"Frog\" (the value at the front pointer, location 0) is assigned to AnimalName", "The front pointer moves to location 1 (\"Cat\") (incremented by 1)"], "a") + "</p><p><b>(iii)</b> " + mks(["There is only one data item in the queue"], "a") + "</p>" +
  "<p><b>(b)(i)</b> Three marks: both pointers and the three new values." + tbl(["Location", "Value", "Pointer"], [["0", "Frog", ""], ["1", "Cat", ""], ["2", "Fish", "Front of queue pointer"], ["3", "Elk", ""], ["4", "Wasp", ""], ["5", "Bee", ""], ["6", "Mouse", "End of queue pointer"], ["7", "", ""]]) + "</p>" +
  "<p><b>(ii)</b> One mark for both pointers and one for all the data values as shown." + tbl(["Location", "Value", "Pointer"], [["0", "Shark", "End of queue pointer"], ["1", "(Cat)", ""], ["2", "(Fish)", ""], ["3", "(Elk)", ""], ["4", "Wasp", "Front of queue pointer"], ["5", "Bee", ""], ["6", "Mouse", ""], ["7", "Dolphin", ""]]) + "<span class=\"note\">Brackets show old values that are no longer part of the queue.</span></p>" +
  "<p><b>(c)</b> " + mks(["If incremented, the end pointer would equal the front pointer: the queue is full (error condition)", "Otherwise increment the end of queue pointer", "Manage wrap-around: if it goes past the last element of the array, set it to the first"]) + "</p>", "Writing a stack answer (LIFO) when the data structure is a queue.") + peq(SRC("s22", "21", "Q4"), "6 marks", "Complete",
  "A stack uses memory locations 200 to 207; TopOfStack points to the last value added. In the first stack, TopOfStack is at 203 with F (203), C (204), D (205), E (206), H (207). (a) State the value on the stack for the longest time, and the location TopOfStack points to after three POP operations. (b) A second stack has TopOfStack at 202 with W (202), Y (203), X (204), Z (205), N (206), P (207). The operations POP, POP, PUSH 'A', PUSH 'B', POP, PUSH 'C', PUSH 'D' are performed. Show the state of the stack.", "Bottom is the oldest. The stack grows down memory, so POP moves the pointer up.",
  "<p><b>(a)</b> " + mks(["'H'", "206"], "b") + "</p><p><b>(b)</b> " + mks(["TopOfStack pointing to 'D'", "Value 'D' in 201", "Values 'C' and 'A' in 202 and 203", "Values 'X' to 'P' unchanged (204 to 207)"], "b") + tbl(["Location", "Value", "Pointer"], [["200", "", ""], ["201", "'D'", "TopOfStack"], ["202", "'C'", ""], ["203", "'A'", ""], ["204", "'X'", ""], ["205", "'Z'", ""], ["206", "'N'", ""], ["207", "'P'", ""]]) + "<span class=\"note\">Working: POP removes W, Y (TopOfStack → 204); PUSH A → 203; PUSH B → 202; POP removes B (→ 203); PUSH C → 202; PUSH D → 201.</span></p>", "Moving the pointer up when pushing. Here the stack grows towards location 200, so a PUSH lowers the address.") + peq(SRC("w22", "21", "Q4"), "4 + 2 + 2 + 4 marks", "Complete / Explain",
  "An ordered linked list holds 'C', 'J', 'L' (single characters, accessed alphabetically). (a)(i) Nodes 'A' and 'K' are added and nodes 'J' and 'L' are deleted; the data must still be accessed in alphabetical order. Complete the diagram. (ii) Explain the advantages of making these changes with a linked list instead of a 1D array holding the characters. (iii) Explain the disadvantages. (b) Explain how the linked list can be implemented in a program.", "A → C → K → Ø. Only pointers change. Needs pointer storage. Two arrays or an array of records.",
  "<p><b>(a)(i)</b> " + mks(["'A' and 'K' stored in new or existing nodes", "Start pointer points to node A", "Node A points to node C, and node C points to node K", "Node K contains a null pointer"]) + " Result: Start → A → C → K → Ø.</p><p><b>(ii)</b> " + mks(["The pointers determine the order of the data, so only pointers need to change when data changes", "It is easier to add and delete data and keep the correct sequence (in an array items would have to be moved)"], "a") + "</p><p><b>(iii)</b> " + mks(["Pointers must be stored as well as the data", "It is more complex to set up and implement"], "a") + "</p><p><b>(b)</b> Any four: " + mks(["Declare two 1D arrays", "One for the data and one for the pointers", "Elements with the same index represent one node", "Declare an integer variable for the start pointer and explain its use", "Define a null pointer value and explain its use", "Declare an integer for the free list pointer and explain its use", "Routines to add, delete and search"], "b") + " Alternatively declare a record type with a data field and a pointer field, and one array of that record type.</p>", None) + peq(SRC("s23", "22", "Q3"), "4 + 1 + 5 marks", "Describe",
  "A queue of up to 10 items (locations 0 to 9, circular) holds Red (5, front), Green (6), Blue (7), Pink (8, end). (a)(i) Describe how Orange and Yellow are added. (ii) A second queue has front pointer at location 5 and end pointer at location 1, all locations used at least once: state the number of items. (b) A function AddToQueue() takes a string and returns TRUE if it was added. A procedure FileToQueue() adds each line of a file; it ends when all lines have been added or the queue is full. Describe its algorithm without pseudocode.", "Check not full; EoQ to 9, store; wrap to 0, store. 5 to 9 and 0 to 1.",
  "<p><b>(a)(i)</b> Any four: " + mks(["Check that the queue is not full", "The end pointer moves to location 9", "Orange is stored in the location the end pointer refers to", "The end pointer moves to location 0", "Yellow is stored in the location the end pointer refers to"], "b") + "</p><p><b>(ii)</b> " + mks(["7"], "a") + " (locations 5 to 9 and 0 to 1).</p><p><b>(b)</b> " + mks(["Open the file in read mode", "Loop until the end of the file, reading all the lines", "The loop also ends when the return value from AddToQueue() is FALSE (queue full)", "Read a line from the file in the loop", "Pass the string to AddToQueue()"]) + "</p>", None) + peq(SRC("w23", "22", "Q3"), "5 + 4 marks", "Complete",
  "A linked list has start pointer Ptr1 and free list pointer Ptr2. The list is D40 → D32 → D11 → D100 → Ø; the free list is F1 → F2 → F3 → F4 → Ø. It is implemented with two variables and two 1D arrays (Data and Pointer, indices 1 to 8). Given: Free_List_Pointer = 5, index 1 holds D32 with pointer 2, index 4 holds D40, index 6 holds F2 with pointer 7. (a) Complete the diagram to show the list as arrays. (b) A node D6 is inserted between D32 and D11. Complete the four steps.", "Index 4 is D40, so Start_Pointer = 4. F1 is at 5. Take F1 off the free list.",
  "<p><b>(a)</b> One mark for Start_Pointer and one mark for each group of rows (2; 3 and 4; 5; 7 and 8). The null pointer may be shown as 0 or Ø." + tbl(["Index", "Data array", "Pointer array"], [["1", "D32", "2"], ["2", "D11", "3"], ["3", "D100", "0 (null)"], ["4", "D40", "1"], ["5", "F1", "6"], ["6", "F2", "7"], ["7", "F3", "8"], ["8", "F4", "0 (null)"]]) + "Start_Pointer = 4, Free_List_Pointer = 5.</p><p><b>(b)</b> " + mks(["Assign the data item D6 to F1", "Set the pointer of this node to point to D11", "Set Ptr2 to point to F2", "Set the pointer of D32 to point to D6"]) + "</p>", "Starting the list at index 1. The start pointer is the index of the first item in order, here 4 (D40).") + peq(SRC("s24", "21", "Q3"), "3 + 5 marks", "Describe / Complete",
  "A linked list has start pointer PS and free list pointer PF. (a) Describe the linked list immediately after initialisation, before any data items are added. (b) The list is to store alphanumeric user IDs using two variables and two 1D arrays, each element holding a single data type (not a record). Complete the statements describing the design.", "Start null, free points to the first node, all nodes on the free list. Integers; String array; Integer array.",
  "<p><b>(a)</b> " + mks(["The start pointer PS contains a null pointer", "The free list pointer PF points to the first element on the free list", "All the nodes are on the free list"]) + "</p><p><b>(b)</b> " + mks(["The two variables will be of type Integer (max 2 marks for the variables)", "They are used as pointers (indexes) to the arrays", "Their values indicate the first element in each list", "The first 1D array is of type String and stores the data items (the user IDs)", "The second 1D array is of type Integer and stores the pointers to the next item"]) + "</p>", None) + peq(SRC("w24", "22", "Q3"), "1 + 2 + 4 marks", "Give / Explain / Complete",
  "A stack holds up to 60 numeric values in DECLARE ThisStack : ARRAY[1:60] OF REAL. SP points to the next available location (an index), OnStack is the number of values held, and the stack grows upwards from index 1. (a)(i) Give the initial values for the two variables. (ii) Explain why the array elements need not be initialised before use. (b) Complete the function Push(ThisValue : REAL) RETURNS BOOLEAN: it returns TRUE if the value was added, otherwise FALSE.", "SP 1, OnStack 0. Check full first, then store, SP + 1, OnStack + 1.",
  "<p><b>(a)(i)</b> " + mks(["SP = 1 and OnStack = 0"], "a") + "</p><p><b>(ii)</b> " + mks(["Unused values cannot be popped off the stack", "until a value has first been pushed, which overwrites the previous value"], "a") + "</p><p><b>(b)</b> One mark per gap:</p>" + pc('''
FUNCTION Push(ThisValue : REAL) RETURNS BOOLEAN
   DECLARE ReturnValue : BOOLEAN
   IF OnStack = 60 THEN
      RETURN FALSE
   ENDIF
   ThisStack[SP] ← ThisValue
   SP ← SP + 1
   OnStack ← OnStack + 1
   RETURN TRUE
ENDFUNCTION'''), "Testing the pointer SP <= 60 after adding. Test whether the stack is full before storing, or you write outside the array.") + peq(SRC("s26", "22", "Q4(a)"), "6 marks", "Complete",
  "A browser uses two stacks. Back button: push the displayed address onto the forward stack, pop the back stack, load the popped address. Forward button: push the displayed address onto the back stack, pop the forward stack, load it. The back stack (bottom to top) is www.ccc.my, www.aaa.home, www.zzz.corp; the forward stack (bottom to top) is www.222.me, www.999.corp, www.111.home, www.333.corp; the page displayed is www.bbb.home. Group 1 is one back click, group 2 one forward click, group 3 three forward clicks. Show both stacks and the displayed page after each group.", "Push the current page onto the other stack, pop this stack.",
  "<p>" + mks(["After group 1: back stack with TOS at www.aaa.home, TOS on the forward stack", "After group 1: forward stack www.bbb.home on top, and the current page www.zzz.corp", "After group 2: both stacks and TOS, current page www.bbb.home", "After group 3: back stack as shown, TOS at www.111.home", "After group 3: forward stack with www.222.me only, TOS there", "After group 3: current page www.999.corp"]) + "</p>" + tbl(["After", "Back stack (bottom to top)", "Forward stack (bottom to top)", "Displayed"], [["Start", "ccc.my, aaa.home, zzz.corp", "222.me, 999.corp, 111.home, 333.corp", "bbb.home"], ["Group 1", "ccc.my, aaa.home", "222.me, 999.corp, 111.home, 333.corp, bbb.home", "zzz.corp"], ["Group 2", "ccc.my, aaa.home, zzz.corp", "222.me, 999.corp, 111.home, 333.corp", "bbb.home"], ["Group 3", "ccc.my, aaa.home, zzz.corp, bbb.home, 333.corp, 111.home", "222.me", "999.corp"]], "t") , "Not pushing the page being displayed onto the other stack before popping.")

review = req("3 marks", "Describe", "Describe how an item is removed from a circular queue held in an array.", "Check, copy front, move front.", "<p>" + mks(["Check the queue is not empty", "Copy the item at the front pointer", "Increment the front pointer, wrapping to the first location if it passes the end"]) + "</p>", None) + req("3 marks", "State", "A stack's array has 5 locations. State what must be checked before PUSH and before POP.", "Full and empty.", "<p>" + mks(["Before PUSH: whether the stack is full", "Before POP: whether the stack is empty", "Otherwise an overflow or underflow error occurs"]) + "</p>", None) + req("2 marks", "State", "State the contents of a stack after PUSH 4, PUSH 7, POP, PUSH 9, PUSH 2, POP.", "Work through.", "<p>" + mks(["4 and 9 remain", "with 9 on top"]) + "</p>", None) + req("3 marks", "Explain", "Explain why a linked list may be better than an array for a list that is kept in order and changed often.", "Pointers only.", "<p>" + mks(["Insertion or deletion only changes pointers", "In an array all the items after the insertion point must be moved", "so the order is kept without moving data"]) + "</p>", None) + req("4 marks", "Describe", "Describe how the first node on the free list is used when a new item is added to a linked list.", "Take node, store, link in, free pointer moves.", "<p>" + mks(["The data is stored in the node the free list pointer points to", "The free list pointer moves to the next node on the free list", "The pointer of the new node is set to the node that follows it", "The pointer of the previous node (or the start pointer) is set to the new node"]) + "</p>", None)

tips = tips_html([
  ("Name the end of each structure.", "Top of stack; front and end of queue; start, null and free pointers."),
  ("Check full and empty.", "Before adding or removing."),
  ("Read how the stack grows.", "Up or down memory; pointer at last value or next free."),
  ("Wrap round.", "Circular queue pointers return to the first location."),
  ("Only pointers change.", "Linked list inserts and deletes move no data."),
  ("Show every pointer.", "A linked list diagram needs start and null."),
], [("an ADT", "A data collection and its operations, described without saying how it is stored."), ("LIFO", "Last in, first out: a stack."), ("FIFO", "First in, first out: a queue."), ("a null pointer", "A pointer to nowhere that marks the end of a list.")],
  [("Identify", "Name it."), ("Describe", "Steps or features."), ("Complete", "Fill the diagram or code."), ("Explain", "Reason with the structure.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const seq = [[], ["A"], ["A", "B"], ["A", "B", "C"], ["A", "B"], ["A"]]; const st = seq[k]; let o = ""; for (let i = 0; i < 5; i++) { const v = st[i]; o += SV.rect(30, 12 + (4 - i) * 26, 90, 24, v ? "f3" : "cell", { rx: 4 }) + SV.text(36, 29 + (4 - i) * 26, i + 1, "sm") + SV.text(75, 29 + (4 - i) * 26, v || "", "lbl bd", { "text-anchor": "middle" }); } if (st.length) o += SV.text(135, 29 + (5 - st.length) * 26, "← top of stack", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 330, h: 150, label: "Stack", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The stack is empty.", "PUSH A.", "PUSH B.", "PUSH C.", "POP removes C: the last in is the first out.", "POP removes B."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const S = [{ q: [], f: 0, e: -1 }, { q: [[0, "Ann"]], f: 0, e: 0 }, { q: [[0, "Ann"], [1, "Bo"]], f: 0, e: 1 }, { q: [[0, "Ann"], [1, "Bo"], [2, "Cy"]], f: 0, e: 2 }, { q: [[1, "Bo"], [2, "Cy"]], f: 1, e: 2 }, { q: [[1, "Bo"], [2, "Cy"], [3, "Di"]], f: 1, e: 3 }];
  const draw = (s) => { const k = Math.round(s.i); const st = S[k]; let o = ""; for (let i = 0; i < 4; i++) { const it = st.q.find((x) => x[0] === i); o += SV.rect(30, 12 + i * 26, 90, 24, it ? "f3" : "cell", { rx: 4 }) + SV.text(36, 29 + i * 26, i, "sm") + SV.text(75, 29 + i * 26, it ? it[1] : "", "lbl bd", { "text-anchor": "middle" }); } if (st.q.length) { o += SV.text(135, 29 + st.f * 26, "← front", "lbl bd t3", { style: "font-size:12px" }); o += SV.text(135, 45 + st.e * 26, "← end", "lbl bd t2", { style: "font-size:12px" }); } return o; };
  Lib.stepper($("#stB"), { w: 330, h: 125, label: "Queue", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["An empty queue.", "Add Ann.", "Add Bo.", "Add Cy.", "Remove: Ann leaves first (FIFO) and the front moves on.", "Add Di at the end."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = [["D40", "→ D32"], ["D32", "→ D11"], ["D11", "→ D100"], ["D100", "→ Ø"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const L = k < 2 ? ["D40", "D32", "D11", "D100"] : k < 3 ? ["D40", "D32", "D11", "D100"] : ["D40", "D32", "D6", "D11", "D100"]; if (k >= 3) {} L.forEach((d, i) => { o += SV.rect(20 + i * 80, 30, 60, 28, d === "D6" ? "f3" : "cell", { rx: 5 }) + SV.text(50 + i * 80, 49, d, "lbl bd", { "text-anchor": "middle" }) + (i < L.length - 1 ? SV.text(82 + i * 80, 48, "→", "lbl") : SV.text(82 + i * 80, 48, "Ø", "lbl")); }); o += SV.text(20, 16, "Ptr1 (start)", "sm"); o += SV.text(20, 90, "Free list: " + (k < 3 ? "F1 → F2 → F3 → F4 → Ø" : "F2 → F3 → F4 → Ø  (F1 now holds D6)"), "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 105, label: "Insert", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["Insert D6 between D32 and D11.", "Take the first free node (F1) and store D6 in it.", "Set its pointer to D11, then Ptr2 moves to F2.", "Set the pointer of D32 to D6: the list is in order, no data moved."].map((c, i) => ({ cap: c, s: { i: i === 0 ? 0 : i === 1 ? 1 : i === 2 ? 2 : 3 } })) });
})();

(function () {
  let st, nxt; const abc = "PQRSTUVWXYZ".split(""); const reset = () => { st = []; nxt = 0; paint("Empty stack. TopOfStack is not pointing at anything."); };
  const paint = (m) => { let h = '<div class="tw"><table class="t mono"><tr><th>location</th><th>value</th><th>pointer</th></tr>'; for (let a = 200; a <= 207; a++) { const idx = 207 - a; const v = st[idx]; h += `<tr><td>${a}</td><td>${v ? "'" + v + "'" : ""}</td><td>${idx === st.length - 1 && v ? "TopOfStack" : ""}</td></tr>`; } $("#skV").innerHTML = h + `</table></div><div class="verdict">${m}</div>`; };
  $("#sk_push").onclick = () => { if (st.length === 8) return paint("Stack full: PUSH refused (overflow)."); const c = abc[nxt++ % abc.length]; st.push(c); paint(`PUSH '${c}': stored at ${208 - st.length}. The stack grows towards 200.`); };
  $("#sk_pop").onclick = () => { if (!st.length) return paint("Stack empty: POP refused (underflow)."); const c = st.pop(); paint(`POP returns '${c}', the last value added. TopOfStack moves back up.`); }; $("#sk_reset").onclick = reset; reset();
})();
(function () {
  let q, f, e, n, c; const reset = () => { q = Array(8).fill(""); f = 0; e = -1; n = 0; c = 0; paint("Empty queue."); };
  const paint = (m) => { let h = '<div class="tw"><table class="t mono"><tr><th>loc</th><th>value</th><th>pointer</th></tr>'; for (let i = 0; i < 8; i++) { const live = n > 0 && ((f <= e) ? i >= f && i <= e : i >= f || i <= e); h += `<tr><td>${i}</td><td style="${live ? "" : "opacity:.4"}">${q[i]}</td><td>${n && i === f ? "front " : ""}${n && i === e ? "end" : ""}</td></tr>`; } $("#quV").innerHTML = h + `</table></div><div class="verdict">${m} Items: <b>${n}</b>.</div>`; };
  $("#qu_add").onclick = () => { if (n === 8) return paint("Queue full: add refused."); e = (e + 1) % 8; q[e] = "item" + (++c); n++; paint(`End pointer moves to ${e}${e === 0 && c > 1 ? " (wrapped round)" : ""} and stores ${q[e]}.`); };
  $("#qu_rem").onclick = () => { if (!n) return paint("Queue empty: remove refused."); const v = q[f]; f = (f + 1) % 8; n--; paint(`Removed ${v} from the front. Front moves to ${f}. The old value stays in the array but is no longer in the queue (faded).`); }; $("#qu_reset").onclick = reset; reset();
})();
(function () {
  let D, P, S, F, hist; const N = 8; const reset = () => { D = Array(N + 1).fill(""); P = Array(N + 1).fill(0); for (let i = 1; i < N; i++) P[i] = i + 1; P[N] = 0; S = 0; F = 1; hist = []; paint("All 8 nodes are on the free list; the start pointer is null (0)."); };
  const paint = (m) => { let h = `<p class="mono">Start_Pointer = ${S || "0 (null)"} &nbsp; Free_List_Pointer = ${F || "0 (null: list full)"}</p><div class="tw"><table class="t mono"><tr><th>index</th><th>Data</th><th>Pointer</th></tr>`; for (let i = 1; i <= N; i++) h += `<tr><td>${i}</td><td>${D[i]}</td><td>${P[i] || "0"}</td></tr>`; const chain = []; for (let p = S; p; p = P[p]) chain.push(D[p]); $("#llV").innerHTML = h + `</table></div><div class="verdict">List in order: <b>${chain.length ? chain.join(" → ") + " → Ø" : "empty"}</b>. ${m}</div>`; };
  const bar = $("#llB"); ["mango", "apple", "pear", "fig", "kiwi", "banana"].forEach((w) => { const b = document.createElement("button"); b.textContent = "Insert " + w; b.onclick = () => { if (!F) return paint("No free node left."); const nn = F; F = P[nn]; D[nn] = w; let prev = 0, p = S; while (p && D[p] < w) { prev = p; p = P[p]; } P[nn] = p; if (prev) P[prev] = nn; else S = nn; hist.push(w); paint(`Took node ${nn} from the free list, stored "${w}" and changed pointers only. No data moved.`); }; bar.appendChild(b); });
  $("#ll_del").onclick = () => { if (!hist.length) return paint("Nothing to delete."); const w = hist.pop(); let prev = 0, p = S; while (p && D[p] !== w) { prev = p; p = P[p]; } if (!p) return paint(""); if (prev) P[prev] = P[p]; else S = P[p]; D[p] = ""; P[p] = F; F = p; paint(`Deleted "${w}": the previous pointer skips node ${p}, which joins the free list.`); }; $("#ll_reset").onclick = reset; reset();
})();
''' + _prjs

finish("as-10-4-abstract-data-types", "as104", "Abstract Data Types",
  "Stacks, queues and linked lists: push and pop, circular queues, pointers, free lists and array implementation, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "10.4", "10 · Data types and structures", "section 10.4 Abstract data types", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on abstract data types (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
