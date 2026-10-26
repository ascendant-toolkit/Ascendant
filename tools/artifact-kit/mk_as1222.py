"""AS CS 12.2.2: state-transition diagrams. Run: python3 tools/artifact-kit/mk_as1222.py"""
from ascs import *
from ak12 import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

def sim(i, svg): return f'<div class="card"><div id="sim{i}" class="stdsim">{svg}</div><div class="btnrow" id="simb{i}"></div><div id="simo{i}"></div></div>'

D_PUMP = std_html({"X": (40, 120, "d"), "S1": (130, 120, "s"), "S2": (400, 80, "s"), "S3": (270, 210, "f")},
  [("X", "S1", "", None, (0, 0)), ("S1", "S2", "Low level detected | Activate pump", (265, 30), (265, 24)), ("S2", "S2", "Low level detected", "loop", (500, 36)),
   ("S2", "S3", "Normal level detected | Deactivate pump", (430, 200), (480, 215)), ("S1", "S3", "Normal level detected", (140, 210), (95, 205))], 620, 250, "State-transition diagram for a pump")
D_BTN = std_html({"START": (30, 100, "d"), "S1": (120, 100, "s"), "S3": (420, 80, "s"), "S2": (230, 230, "s"), "S4": (430, 240, "s")},
  [("START", "S1", "", None, (0, 0)), ("S1", "S3", "Button-Y", (270, 25), (270, 32)), ("S3", "S3", "Button-Z | Output-C", "loop", (520, 30)),
   ("S3", "S4", "Button-Y", (520, 170), (540, 170)), ("S4", "S2", "Button-Z | Output-B", (330, 300), (330, 312)), ("S2", "S4", "Button-Y | Output-A", (330, 190), (330, 188)),
   ("S1", "S2", "Button-X", (90, 220), (55, 205)), ("S2", "S1", "Button-Z", (190, 130), (215, 122))], 640, 330, "State-transition diagram with buttons")
D_HEAT = std_html({"S": (30, 120, "d"), "Heaters Off": (120, 120, "s"), "Heaters On": (380, 120, "s")},
  [("S", "Heaters Off", "", None, (0, 0)), ("Heaters Off", "Heaters On", "Temp < 10", (250, 50), (250, 42)), ("Heaters On", "Heaters Off", "Temp > 20", (250, 200), (250, 218)),
   ("Heaters Off", "Heaters Off", "Temp >= 10", "loop", (120, 40)), ("Heaters On", "Heaters On", "Temp <= 20", "loop", (380, 40))], 500, 235, "State-transition diagram for heating")
D_PUMP2 = std_html({"X": (40, 120, "d"), "S1": (130, 120, "s"), "S2": (400, 80, "s"), "S3": (270, 210, "f")},
  [("X", "S1", "", None, (0, 0)), ("S1", "S2", "Low level detected | Activate pump", (265, 30), (265, 24)), ("S2", "S2", "Low level detected", "loop", (500, 36)),
   ("S2", "S3", "Normal level detected | Deactivate pump", (430, 200), (480, 215)), ("S1", "S3", "Normal level detected", (140, 210), (95, 205))], 620, 250, "State-transition diagram for a pump")
D_BTN2 = std_html({"START": (30, 100, "d"), "S1": (120, 100, "s"), "S3": (420, 80, "s"), "S2": (230, 230, "s"), "S4": (430, 240, "s")},
  [("START", "S1", "", None, (0, 0)), ("S1", "S3", "Button-Y", (270, 25), (270, 32)), ("S3", "S3", "Button-Z | Output-C", "loop", (520, 30)),
   ("S3", "S4", "Button-Y", (520, 170), (540, 170)), ("S4", "S2", "Button-Z | Output-B", (330, 300), (330, 312)), ("S2", "S4", "Button-Y | Output-A", (330, 190), (330, 188)),
   ("S1", "S2", "Button-X", (90, 220), (55, 205)), ("S2", "S1", "Button-Z", (190, 130), (215, 122))], 640, 330, "State-transition diagram with buttons")
D_HEAT2 = std_html({"S": (30, 120, "d"), "Heaters Off": (120, 120, "s"), "Heaters On": (380, 120, "s")},
  [("S", "Heaters Off", "", None, (0, 0)), ("Heaters Off", "Heaters On", "Temp < 10", (250, 50), (250, 42)), ("Heaters On", "Heaters Off", "Temp > 20", (250, 200), (250, 218)),
   ("Heaters Off", "Heaters Off", "Temp >= 10", "loop", (120, 40)), ("Heaters On", "Heaters On", "Temp <= 20", "loop", (380, 40))], 500, 235, "State-transition diagram for heating")
D_FULL = std_html({"START": (30, 130, "d"), "S1": (130, 130, "s"), "S2": (340, 100, "s"), "S3": (530, 130, "s"), "S4": (270, 250, "s")},
  [("START", "S1", "", None, (0, 0)), ("S1", "S2", "Input-A | Output-X", (235, 35), (235, 28)), ("S2", "S2", "Input-A", "loopd", (400, 185)), ("S2", "S3", "Input-B | Output-W", (435, 45), (440, 38)),
   ("S3", "S3", "Input-B", "loop", (590, 50)), ("S3", "S4", "Input-A | Output-W", (460, 275), (470, 292)), ("S4", "S1", "Input-A", (190, 215), (215, 190)), ("S1", "S4", "Input-B", (70, 240), (50, 218))], 640, 310, "State-transition diagram with four states")
D_TAB = std_html({"START": (30, 100, "d"), "S1": (120, 100, "s"), "S2": (300, 100, "s"), "S5": (480, 100, "s"), "S3": (120, 240, "s"), "S4": (120, 340, "s")},
  [("START", "S1", "", None, (0, 0)), ("S1", "S2", "A1 | X1", (210, 60), (210, 52)), ("S2", "S1", "A3", (210, 140), (210, 156)), ("S2", "S5", "A2 | X4", (390, 60), (390, 52)), ("S5", "S2", "A4 | X2", (390, 140), (390, 156)),
   ("S5", "S5", "A1 | X1", "loop", (540, 40)), ("S1", "S3", "A9 | X9", None, (180, 175)), ("S5", "S3", "A3", (330, 320), (345, 290)), ("S3", "S4", "A9 | X9", None, (180, 295))], 620, 385, "State-transition diagram completed from a table")
D_CAM = std_html({"START": (30, 110, "d"), "standby mode": (110, 110, "s"), "detect mode": (320, 110, "s"), "active mode": (530, 110, "s"), "sequence complete": (430, 250, "s")},
  [("START", "standby mode", "", None, (0, 0)), ("standby mode", "detect mode", "turn on", (215, 60), (215, 52)), ("detect mode", "standby mode", "turn off", (215, 160), (215, 176)), ("detect mode", "active mode", "movement detected", (425, 60), (425, 52)),
   ("active mode", "sequence complete", "20 seconds elapsed", None, (545, 190)), ("sequence complete", "detect mode", "time saved", None, (340, 190)), ("active mode", "standby mode", "turn off", (320, 320), (180, 320))], 640, 340, "State-transition diagram for a camera system")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>state-transition diagram</b> shows how a system moves between <b>states</b> when something happens. Each <b>state</b> is a circle, the <b>start</b> is a filled dot with an arrow, and a <b>final (halting) state</b> is drawn as a double circle. An arrow between states is a <b>transition</b>, labelled with the <b>input</b> or event that causes it and, after a bar, any <b>output</b>: <span class="mono">Low level detected | Activate pump</span>. An arrow that leaves a state and returns to it is a <b>loop</b> (the input does not change the state). The same information can be written as a <b>state-transition table</b> with columns for current state, input, output and next state.</p></div>

  <h2>1 · The notation</h2>
  ''' + D_PUMP + '''
  <ul>
    <li><b>X</b> (the dot and arrow into S1) is the <b>start</b>: the label that replaces X is "Start".</li>
    <li><b>S1</b> to <b>S2</b>: input "Low level detected", output "Activate pump". <b>S1</b> to <b>S3</b>: input "Normal level detected", no output.</li>
    <li><b>S2</b> loops on "Low level detected" (no output) and moves to <b>S3</b> on "Normal level detected" with the output "Deactivate pump".</li>
    <li><b>S3</b> is the <b>final</b> (halting) state: it has the double circle and no transitions out.</li>
  </ul>
  <p>Counting: three transitions result in a different state (S1 to S2, S1 to S3, S2 to S3); two have an associated output. If the current state is S1 and "Low level detected" happens four times, the first moves to S2 and produces one output; the other three loop on S2 and produce nothing: <b>1 output, current state S2</b>.</p>

  <h2>2 · Reading a diagram as a table</h2>
  ''' + D_FULL + '''
  <p>Start in S1. Follow each input: the table is built one row at a time, using the next state of the previous row as the current state.</p>
  ''' + tbl(["Input", "Output", "Next state", "Why"], [["", "", "S1", "the start"], ["Input-A", "Output-X", "S2", "S1, Input-A | Output-X"], ["Input-A", "none", "S2", "S2 loops on Input-A"], ["Input-B", "Output-W", "S3", "S2, Input-B | Output-W"], ["Input-A", "Output-W", "S4", "S3, Input-A | Output-W"]]) + '''
  <p>Write <b>none</b> when there is no output. The different inputs are the distinct labels before each bar (here two: Input-A and Input-B), and the distinct outputs are those after a bar (X and W).</p>

  <h2>3 · Drawing a diagram from a table</h2>
  ''' + tbl(["Current state", "Input", "Output", "Next state"], [["S1", "A1", "X1", "S2"], ["S2", "A3", "none", "S1"], ["S2", "A2", "X4", "S5"], ["S5", "A1", "X1", "S5"], ["S5", "A4", "X2", "S2"], ["S5", "A3", "none", "S3"], ["S1", "A9", "X9", "S3"], ["S3", "A9", "X9", "S4"]]) + D_TAB + '''
  <ol>
    <li>Draw one circle for every state in the table, and mark the start.</li>
    <li>For each row draw an arrow from the current state to the next state, labelled input | output (only the input if the output is "none").</li>
    <li>A row where the current state equals the next state is a <b>loop</b>.</li>
    <li>Tick off the rows as you draw them: eight rows, eight arrows.</li>
  </ol>

  <h2>4 · Using a diagram to design</h2>
  <p>A state-transition diagram documents an algorithm in the design stage: the states, the events that cause the change, and the outputs. Identify the states of the system (standby mode, on mode, alarm sounding) and the events (movement detected, wrong password entered repeatedly, battery too low).</p>
  ''' + D_CAM + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing an output for a transition that has none (use "none"), or taking the output from the wrong arrow.</li>
    <li>Using the wrong current state: each row starts in the previous row's next state.</li>
    <li>Counting loops as changes of state, or leaving them out of a diagram you draw.</li>
    <li>Drawing an arrow in the wrong direction: it starts at the current state and ends at the next state.</li>
  </ul>
'''

watch = '''
  <h2>1 · Following the inputs</h2>
  <div id="stA"></div>
  <h2>2 · A loop and a halting state</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · The pump</h2>
  <p>Press an input. The current state is highlighted; outputs are listed below.</p>
''' + sim(1, D_PUMP2) + '''
  <h2>Lab 2 · The buttons</h2>
''' + sim(2, D_BTN2) + '''
  <h2>Lab 3 · The heater</h2>
''' + sim(3, D_HEAT2) + '''
  <h2>Lab 4 · Table row to arrow</h2>
  <div class="card"><div id="trB" class="btnrow"></div><div id="trO"></div></div>
'''

_pr, _prjs = PR(["Read the diagram", "Table or diagram?", "Match the part", "Put the trace in order", "Working out", "Multiple choice"],
  ("In the pump diagram, which is it?", ["Start", "Final state", "Output", "Loop"], [("The dot with an arrow into S1", 0), ("S3, drawn as a double circle", 1), ("Activate pump", 2), ("Low level detected on S2 returning to S2", 3), ("Deactivate pump", 2), ("The state with no transitions out", 1)], "Dot start; double circle final; after the bar an output."),
  ("Which belongs in a state-transition table?", ["Table column", "Not a column"], [("Current state", 0), ("Input", 0), ("Output", 0), ("Next state", 0), ("The author's name", 1), ("The number of marks", 1)], "Current state, input, output, next state."),
  [["State", "A circle"], ["Transition", "An arrow between states"], ["Start", "A filled dot and an arrow"], ["Final state", "A double circle"], ["Output", "After the bar on the label"]],
  ("Put the steps of tracing Input-A, Input-A, Input-B from S1 in order (using the four-state diagram).", ["Start in S1", "Input-A: output X, move to S2", "Input-A: no output, loop on S2", "Input-B: output W, move to S3", "End in S3"], "Follow each arrow."),
  [{"q": "In the pump diagram, how many transitions result in a different state?", "a": 3, "unit": "", "tol": 0.01, "hint": "S1 to S2, S1 to S3, S2 to S3.", "sol": "<b>3</b>."}, {"q": "In the pump diagram, how many transitions have an associated output?", "a": 2, "unit": "", "tol": 0.01, "hint": "Activate pump and Deactivate pump.", "sol": "<b>2</b>."}, {"q": "In the pump diagram from S1, four Low level detected inputs occur. How many outputs?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first leaves S1.", "sol": "<b>1</b> (and the state is S2)."}, {"q": "The button diagram uses Button-X, Button-Y and Button-Z. How many different inputs?", "a": 3, "unit": "", "tol": 0.01, "hint": "Count the distinct labels.", "sol": "<b>3</b>."}, {"q": "A table has 9 rows. How many arrows does the diagram have?", "a": 9, "unit": "", "tol": 0.01, "hint": "One per row, including loops.", "sol": "<b>9</b>."}],
  [("A loop on a state means:", ["The input does not change the state", "The system stops", "An error", "The start"], 0, "Same state."), ("A final state is drawn as:", ["A double circle", "A diamond", "A dot", "A rectangle"], 0, "Double circle."), ("The label after the bar is the:", ["Output", "Input", "State", "Start"], 0, "Output."), ("The X on the start arrow should be labelled:", ["Start", "S0", "Input", "Halt"], 0, "Start."), ("In a trace table the current state of a row is:", ["The next state of the previous row", "Always S1", "The input", "The output"], 0, "Chain."), ("A state-transition diagram is produced in:", ["The design stage", "Coding", "Testing", "Maintenance"], 0, "Design.")],
  [("State", "A circle in the diagram."), ("Transition", "An arrow between states."), ("Input | Output", "The label on an arrow."), ("Loop", "An arrow from a state to itself."), ("Start", "A dot and an arrow."), ("Final state", "A double circle."), ("Table row", "Current state, input, output, next state."), ("none", "Write it when there is no output.")])

real = RWNOTE + (
rw("A traffic light", "The states are red, red-amber, green and amber; a timer is the event that moves from one to the next.", "states and events.") +
rw("A vending machine", "It waits for coins, then a choice, then dispenses; pressing cancel returns the coins and goes back to waiting.", "transitions with outputs.") +
rw("A door alarm", "Standby, armed and alarm sounding are states; entering the password, opening a door or waiting are the events.", "design with states.") +
rw("Games and characters", "A character is idle, walking, jumping or falling, and the buttons and the ground are the inputs that change its state.", "state machines.")
)

where = [
  ("M/J 2021", "22", "2(a)", "4 + 2", "Count transitions, outputs, the label for X and the final state; the output and state after four inputs"),
  ("M/J 2022", "21", "2", "3 + 4", "The number of different inputs and outputs; complete a table of inputs, outputs and next states"),
  ("O/N 2021", "21", "4(b)", "3", "Complete a state-transition diagram for a heating system"),
  ("O/N 2022", "22", "2(b)", "4", "Complete a table of inputs, outputs and next states"),
  ("O/N 2023", "21", "7", "5", "Complete a state-transition diagram from a table"),
  ("O/N 2025", "21", "7(a)", "5", "Complete a state-transition diagram from a table"),
  ("O/N 2025", "23", "7(a)", "5", "Complete a state-transition diagram from a table"),
  ("M/J 2025", "22", "5(a)", "4", "Complete a state-transition diagram for a camera system"),
  ("M/J 2026", "22", "1(b)", "2 + 3", "Identify states and events for an alarm system")]

past = '''  <p class="note">State-transition questions appear in nearly every series: read a diagram, build a table, or draw a diagram from a table. The diagrams are redrawn from the papers' printed versions and mark schemes; check the original for the layout.</p>
''' + peq(SRC("s21", "22", "Q2(a)"), "4 + 2 marks", "Complete / Give",
  "A state-transition diagram shows a start arrow labelled X into S1; S1 goes to S2 on \"Low level detected | Activate pump\"; S2 loops on \"Low level detected\"; S2 goes to S3 on \"Normal level detected | Deactivate pump\"; S1 goes to S3 on \"Normal level detected\"; S3 is a double circle. (i) Complete the table: the number of transitions that result in a different state; the number of transitions with associated outputs; the label that should replace X; the final or halting state. (ii) The current state is S1 and Low level detected occurs four times. Give the number of outputs and the current state.", "Count the arrows between different states; outputs after a bar.",
  "<p>" + D_PUMP + "</p><p><b>(i)</b> One mark per row:" + tbl(["Question", "Answer"], [["The number of transitions that result in a different state", "3"], ["The number of transitions with associated outputs", "2"], ["The label that should replace X", "Start"], ["The final or halting state", "S3"]]) + "</p><p><b>(ii)</b> " + mks(["Number of outputs: 1", "Current state: S2"], "a") + "</p>", "Counting the loop on S2 as a transition that changes the state.") + peq(SRC("s22", "21", "Q2"), "3 + 4 marks", "Complete",
  "A state-transition diagram has a START arrow into S1; S1 goes to S3 on Button-Y; S1 goes to S2 on Button-X; S2 goes to S1 on Button-Z; S2 goes to S4 on Button-Y | Output-A; S3 loops on Button-Z | Output-C; S3 goes to S4 on Button-Y; S4 goes to S2 on Button-Z | Output-B. (a) Complete the table: the number of different inputs; the number of different outputs; the single input value that could result in S4. (b) The initial state is S1: complete a table to show the inputs, outputs and next states for the input sequence Button-Y, Button-Y, Button-Z, Button-Z.", "Inputs: X, Y, Z. Outputs: A, B, C. Follow each arrow in turn.",
  "<p>" + D_BTN + "</p><p><b>(a)</b> One mark per row:" + tbl(["Question", "Answer"], [["The number of different inputs", "3"], ["The number of different outputs", "3"], ["The single input value that could result in S4", "Button-Y"]]) + "</p><p><b>(b)</b> One mark per row (accept other valid answers):" + tbl(["Input", "Output", "Next state"], [["Button-Y", "none", "S3"], ["Button-Y", "none", "S4"], ["Button-Z", "Output-B", "S2"], ["Button-Z", "none", "S1"]]) + "</p>", "Starting each row in S1 instead of the next state of the row above.") + peq(SRC("w21", "21", "Q4(b)"), "3 marks", "Complete",
  "A program module controls the heaters in a sports hall: if the temperature is below 10, switch the heaters on; if the temperature is above 20, switch the heaters off. Complete the state-transition diagram: a Start arrow into the state Heaters Off, and the two states Heaters Off and Heaters On drawn with their transitions unlabelled.", "Off to On: below 10. On to Off: above 20. The loops are the opposite conditions.",
  "<p>" + D_HEAT + "</p>" + mks(["Temp < 10 (Heaters Off to Heaters On)", "Temp > 20 (Heaters On to Heaters Off)", "Labels on both loops (non-contradictory values: Temp >= 10 and Temp <= 20)"]), "Leaving out the loops: while the temperature is between the limits the heaters stay in the same state.") + peq(SRC("w22", "22", "Q2(b)"), "4 marks", "Complete",
  "A state-transition diagram has START into S1; S1 to S2 on Input-A | Output-X; S2 loops on Input-A; S2 to S3 on Input-B | Output-W; S3 loops on Input-B; S3 to S4 on Input-A | Output-W; S4 to S1 on Input-A; S1 to S4 on Input-B. Complete the table of inputs, outputs and next state (the first row, next state S1, is given).", "Follow each arrow in turn; none where there is no output.",
  "<p>" + D_FULL + "</p><p>One mark per row (rows 2 to 5):" + tbl(["Input", "Output", "Next state"], [["", "", "S1"], ["Input-A", "Output-X", "S2"], ["Input-A", "none", "S2"], ["Input-B", "Output-W", "S3"], ["Input-A", "Output-W", "S4"]]) + "</p>", None) + peq(SRC("w23", "21", "Q7"), "5 marks", "Complete",
  "The table shows the inputs, outputs and states of an algorithm: S1 A1 X1 S2; S2 A3 none S1; S2 A2 X4 S5; S5 A1 X1 S5; S5 A4 X2 S2; S5 A3 none S3; S1 A9 X9 S3; S3 A9 X9 S4. Complete the state-transition diagram (S1 with the start arrow and the transition A1 | X1 and the label A3 are given).", "Eight rows, eight arrows; S5 loops.",
  "<p>" + D_TAB + "</p>" + mks(["S2 labelled", "S3, S4 and S5 added", "A line from S1 to S3", "All three lines between S2 and S5 (including S5 to S5)", "A line from S5 to S3 and from S3 to S4"]), "Forgetting the loop: a row whose next state equals the current state is an arrow back to the same circle.") + peq(SRC("w25", "21", "Q7(a)"), "5 marks", "Complete",
  "The table shows the inputs, outputs and states: S1 A2 X2 S3; S1 A1 X1 S2; S2 A4 X4 S5; S3 A1 (no output) S3; S3 A3 X3 S2; S3 A2 X4 S4; S4 A1 X1 S4; S4 A3 (no output) S2; S4 A4 X4 S5. Complete the diagram (S1 with the start arrow and A2 | X2 are given).", "Nine rows, nine arrows; S3 and S4 loop.",
  "<p>" + mks(["Label A1 | X1 added on the line from S1 to S2", "States S3, S4 and S5 labelled", "A line from S2 to S5 with the label A4 | X4", "Lines from S3 with the correct labels, including the loop label", "Lines from S4 with the correct labels, including the loop"]) + "</p><p>The nine arrows: S1 to S3 (A2 | X2); S1 to S2 (A1 | X1); S2 to S5 (A4 | X4); S3 loop (A1); S3 to S2 (A3 | X3); S3 to S4 (A2 | X4); S4 loop (A1 | X1); S4 to S2 (A3); S4 to S5 (A4 | X4).</p>", None) + peq(SRC("w25", "23", "Q7(a)"), "5 marks", "Complete",
  "The table shows: S1 A1 (no output) S2; S2 A2 X4 S3; S3 A1 X1 S3; S3 A2 X1 S3; S3 A3 X3 S4; S3 A4 (no output) S2; S4 A3 X4 S5; S4 A4 X4 S5; S4 A1 (no output) S2. Complete the diagram (S1 with the start arrow is given).", "Two loops on S3; two arrows from S4 to S5.",
  "<p>The nine arrows: S1 to S2 (A1); S2 to S3 (A2 | X4); S3 loops (A1 | X1 and A2 | X1); S3 to S4 (A3 | X3); S3 to S2 (A4); S4 to S5 (A3 | X4 and A4 | X4); S4 to S2 (A1). Mark by the same scheme: states labelled, then the transitions from each state with their labels, including the loops.</p>", "Drawing one loop on S3 with a single label: there are two inputs (A1 and A2) that keep S3 as the current state.") + peq(SRC("s25", "22", "Q5(a)"), "4 marks", "Complete",
  "An automated camera system takes pictures of animals. It starts in standby mode. The table gives: standby mode, turn on, detect mode; detect mode, turn off, standby mode; detect mode, movement detected, active mode; active mode, 20 seconds elapsed, sequence complete; active mode, turn off, standby mode; sequence complete, time saved, detect mode. Complete the state-transition diagram (standby mode is shown with the start arrow).", "Three new states; six arrows with directions and labels.",
  "<p>" + D_CAM + "</p>" + mks(["The three new states drawn and labelled", "Two of the events drawn with labels connecting the correct states and with the correct direction", "Four of the events drawn correctly", "All and only six events drawn with labels connecting the correct states and the correct direction"]), "Reversing an arrow: \"time saved\" goes from sequence complete to detect mode.") + peq(SRC("s26", "22", "Q1(b)"), "2 + 3 marks", "Identify",
  "A state-transition diagram is created in the design of the module that controls an alarm system once it has been installed. Two states are already identified: the alarm is in standby mode, and the alarm is on. (i) Identify two other states that should be part of the diagram. (ii) Two events that change the state are entering the password when in standby mode and entering the password when on. Identify three other events that would cause a change of state.", "States: what the alarm could be doing. Events: sensors and time.",
  "<p><b>(i)</b> Any two: " + mks(["Sensor activated, or movement (intruder) detected mode", "Alarm sounding, or alarm activated", "Error mode, power loss detected, or battery too low", "Tamper detected, or lockdown mode", "Disarm, maintenance, password change or service mode"], "a") + "</p><p><b>(ii)</b> Any three: " + mks(["Movement or pressure detected", "Window opened or broken", "A door opened", "A wrong password entered repeatedly", "A password entered to enter or leave maintenance mode, or to silence the alarm", "Tampering with or damage to the alarm", "A time delay after the alarm is triggered or before it is activated", "The battery charge becomes too low", "The panic button pressed"], "b") + "</p>", None)

review = req("3 marks", "Complete", "A turnstile has states Locked and Unlocked. Putting in a coin unlocks it; pushing through locks it. Pushing a locked turnstile and putting a coin into an unlocked one do nothing. Draw the state-transition diagram, starting Locked.", "Two states, four arrows (two loops).", "<p>" + mks(["Two states with the start arrow into Locked", "Coin: Locked to Unlocked; Push: Unlocked to Locked", "Loops: Push on Locked and Coin on Unlocked"]) + "</p>", None) + req("3 marks", "Complete", "From S1: input A goes to S2 with output X; input B on S2 loops with no output; input A on S2 goes to S3 with output Y. Complete the table for inputs A, B, A.", "Follow the arrows.", "<p>" + tbl(["Input", "Output", "Next state"], [["", "", "S1"], ["A", "X", "S2"], ["B", "none", "S2"], ["A", "Y", "S3"]]) + mks(["First row correct", "Second row correct", "Third row correct"]) + "</p>", None) + req("2 marks", "State", "State what a double circle and a dot with an arrow show.", "Final, start.", "<p>" + mks(["A double circle is the final (halting) state", "A dot with an arrow shows the start"]) + "</p>", None) + req("2 marks", "Explain", "Explain what a loop on a state means.", "Same state.", "<p>" + mks(["The input or event does not change the state", "The system stays in the same state (and may produce an output)"]) + "</p>", None) + req("2 marks", "State", "State the four columns of a state-transition table.", "State, input, output, next state.", "<p>" + mks(["Current state and input", "Output and next state"]) + "</p>", None)

tips = tips_html([
  ("Chain the rows.", "Next state of one row is the current state of the next."),
  ("Write none.", "When a transition has no output."),
  ("Loops count.", "Draw them and write their labels; they are not changes of state."),
  ("Start and final.", "Dot with an arrow; double circle."),
  ("One arrow per row.", "Tick the table off as you draw."),
  ("Arrow direction.", "From the current state to the next state."),
], [("a state", "A condition the system is in."), ("a transition", "A change from one state to another."), ("an input or event", "What causes a transition."), ("a halting state", "A final state with no way out.")],
  [("Complete", "Fill in the table or diagram."), ("Give", "State the answer."), ("Identify", "Name the states or events."), ("State", "A short answer.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const N = ["S1", "S2", "S3"]; const cur = [0, 1, 1, 2][k]; let o = ""; N.forEach((n, i) => o += SV.circle(50 + i * 110, 50, 24, i === cur ? "f3" : "cell") + SV.text(50 + i * 110, 54, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(14, 100, ["Start in S1.", "Input A | output X: move to S2.", "Input A again: a loop on S2, no output.", "Input B | output W: move to S3."][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 330, h: 112, label: "States", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The system starts in S1.", "The first input moves it to S2.", "The same input on S2 is a loop.", "Input B changes the state to S3."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.circle(70, 50, 24, k === 0 ? "f3" : "cell") + SV.text(70, 54, "S2", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.circle(220, 50, 24, k === 1 ? "f3" : "cell") + SV.circle(220, 50, 19, "cell") + SV.text(220, 54, "S3", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); o += SV.text(14, 104, ["Loop: the input leaves the system in S2.", "Final state: S3 is a double circle with no way out."][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 320, h: 118, label: "Loop and final state", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["A loop leaves the state unchanged.", "The final or halting state."].map((c, i) => ({ cap: c, s: { i } })) });
})();

const MACH = {
  1: { start: "S1", T: { S1: { "Low level detected": ["S2", "Activate pump"], "Normal level detected": ["S3", ""] }, S2: { "Low level detected": ["S2", ""], "Normal level detected": ["S3", "Deactivate pump"] }, S3: {} } },
  2: { start: "S1", T: { S1: { "Button-Y": ["S3", ""], "Button-X": ["S2", ""] }, S2: { "Button-Z": ["S1", ""], "Button-Y": ["S4", "Output-A"] }, S3: { "Button-Z": ["S3", "Output-C"], "Button-Y": ["S4", ""] }, S4: { "Button-Z": ["S2", "Output-B"] } } },
  3: { start: "Heaters Off", T: { "Heaters Off": { "Temp < 10": ["Heaters On", "switch on"], "Temp >= 10": ["Heaters Off", ""] }, "Heaters On": { "Temp > 20": ["Heaters Off", "switch off"], "Temp <= 20": ["Heaters On", ""] } } }
};
function mkSim(i, host, svg) {
  const M = MACH[i]; const box = $("#sim" + i); const out = $("#simo" + i); const bar = $("#simb" + i); let cur = M.start, log = [];
  const paint = (msg) => { box.querySelectorAll("circle[data-n]").forEach((c) => c.style.fill = c.getAttribute("data-n") === cur ? "var(--accent, #fcd34d)" : "var(--surface)"); const outs = log.filter((x) => x).length; out.innerHTML = `<div class="verdict">Current state: <b>${cur}</b>. ${msg || ""}</div><p>Inputs so far: ${log.length}. Outputs so far: <b>${outs}</b>.</p>`; };
  const inputs = [...new Set(Object.values(M.T).flatMap((o) => Object.keys(o)))];
  inputs.forEach((inp) => { const b = document.createElement("button"); b.textContent = inp; b.onclick = () => { const t = (M.T[cur] || {})[inp]; if (!t) return paint(`No transition for ${inp} from ${cur}: nothing happens.`); const was = cur; cur = t[0]; log.push(t[1]); paint(`${was} → ${cur}${t[1] ? ", output: " + t[1] : ", no output"}${was === cur ? " (a loop)" : ""}.`); }; bar.appendChild(b); });
  const r = document.createElement("button"); r.textContent = "Reset"; r.onclick = () => { cur = M.start; log = []; paint("Back to the start."); }; bar.appendChild(r); paint("Choose an input.");
}
[1, 2, 3].forEach((i) => mkSim(i));
btnTable("trB", "trO", [
  ["S1, A1, X1, S2", "Arrow S1 to S2 labelled A1 | X1", "a change of state with an output"],
  ["S2, A3, none, S1", "Arrow S2 to S1 labelled A3", "no output: only the input is written"],
  ["S5, A1, X1, S5", "A loop on S5 labelled A1 | X1", "current state equals next state"],
  ["S3, A9, X9, S4", "Arrow S3 to S4 labelled A9 | X9", "S3 is the current state, S4 the next"]
], ["Table row", "On the diagram", "Why"]);
''' + _prjs

finish("as-12-2-2-state-transition-diagrams", "as1222", "State-Transition Diagrams",
  "State-transition diagrams: states, inputs, outputs, loops and halting states, reading a diagram into a table and drawing one from a table, with animations, simulators and the real Paper 2 questions from 2021 to 2026.",
  "12.2.2", "12 · Software development", "section 12.2 Program design", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on state-transition diagrams (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
