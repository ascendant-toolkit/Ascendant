"""IGCSE CS exam technique 4: the 15-mark scenario question. Run: python3 tools/artifact-kit/mk_cx4.py"""
from csk import *

SCEN = ["A cycling club has 60 riders who each ride a 5-kilometre time trial. The riders' names are stored in the one-dimensional (1D) array RiderName[]. Each rider's time, in seconds, is stored in the 1D array RiderTime[]. A rider's data is at the same index in both arrays.",
        "The club gives rosettes to the riders with the three fastest times and a badge to every rider who finishes in under 900 seconds."]

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>The last question of Paper 2 is a <b>15-mark unseen scenario</b> in which you write a program, and the syllabus says to spend about <b>30 minutes</b> on it. It is marked in two bands: <b>AO2 out of 9</b> for the programming techniques and the data structures you choose, and <b>AO3 out of 6</b> for comments, identifiers, logical order and accuracy, so a program that does everything the scenario asks, with the structures it names and clear comments, can earn all 15. Each series gives a list of requirements and the names of the arrays and variables to use, and the mark scheme is a <b>checklist of those requirements</b>, so the strongest answers follow the scenario line by line. The examiner reports repeat the same advice every year: read to the end, use the given arrays as they are described, do not waste time declaring what you are told is already declared, comment every part, and put a message with every input and output. The band you reach depends on how much of the checklist your program meets, so <b>plan the requirements first and write the program in that order</b>.</p></div>

  <h2>1 · The facts</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td><b>Marks and time</b></td><td>15 marks, about 30 minutes (syllabus guidance); the last question of Paper 2</td></tr>
    <tr><td><b>Language</b></td><td>Pseudocode, or Python, Visual Basic or Java. Other languages earn no marks.</td></tr>
    <tr><td><b>Content</b></td><td>Methods and concepts from Topics 7 to 10; the scenario is new each series</td></tr>
    <tr><td><b>Marking</b></td><td>AO2 maximum 9 marks and AO3 maximum 6 marks, each in bands</td></tr>
    <tr><td><b>Standard instructions</b></td><td>"You must use pseudocode or program code and add comments to explain how your code works." "You do not need to declare any arrays or variables." "All inputs and outputs must contain suitable messages."</td></tr>
  </table></div>

  <h2>2 · What a scenario gives you</h2>
  <div class="tw"><table class="t">
    <tr><th>Part of the scenario</th><th>What it tells you</th><th>What to do with it</th></tr>
    <tr><td><b>The context</b></td><td>The situation: a club, a house, a theatre, a league</td><td>Use it in your messages and comments</td></tr>
    <tr><td><b>Data structures with names</b></td><td>For example 1D arrays MemberName[] and MemberTime[], a 2D array Dimensions[], a variable Number</td><td>Use exactly those names, in the way described. Do not invent others for the same data.</td></tr>
    <tr><td><b>Facts about the data</b></td><td>"At the same index in both arrays", 60 riders, at least 3 rooms</td><td>These set loop limits and validation ranges</td></tr>
    <tr><td><b>Bulleted requirements</b></td><td>What the program must do</td><td>Turn each bullet into one line of a checklist</td></tr>
    <tr><td><b>The closing instructions</b></td><td>Pseudocode or code, comments, no declaring, messages</td><td>Follow all of them; they are marked</td></tr>
  </table></div>
  <p>The mark scheme for each scenario lists the data structures and the requirements with the technique each needs. For Oct/Nov 2024 paper 21 (a running club) the three requirements were: <b>R1</b> input and verify the times (input and iteration); <b>R2</b> sort both arrays into ascending order of time and output the top three (nested iteration, sorting, selection, output); <b>R3</b> store the names of the members who get a certificate and output the number (iteration, selection, counting, output).</p>

  <h2>3 · How it is marked: the published bands</h2>
  <p>The mark scheme gives a band descriptor for each assessment objective. The wording below is a close paraphrase of the descriptors in the Oct/Nov 2024 and 2023 mark schemes.</p>
  <h3>AO2: applying knowledge, out of 9</h3>
  <div class="tw"><table class="t">
    <tr><th>Band</th><th>Programming techniques</th><th>Data structures</th></tr>
    <tr><td><b>7 to 9</b></td><td>The range of techniques is appropriate to the problem. All criteria stated for the scenario are covered by an appropriate technique (check against the list of techniques needed).</td><td>The structures chosen are appropriate and store <b>all</b> the data the scenario requires.</td></tr>
    <tr><td><b>4 to 6</b></td><td>Some techniques are appropriate. More than one technique is applied to the scenario.</td><td>Some of the structures chosen are appropriate and store <b>some</b> of the data required. More than one structure is used.</td></tr>
    <tr><td><b>1 to 3</b></td><td>At least one programming technique is used: any use of selection, iteration, counting, totalling, input and output.</td><td>Some data is stored, but not appropriately: any use of variables, arrays or other structures such as Python lists.</td></tr>
    <tr><td><b>0</b></td><td colspan="2">No creditable response.</td></tr>
  </table></div>
  <h3>AO3: solutions and judgements, out of 6</h3>
  <div class="tw"><table class="t">
    <tr><th>Band</th><th>Comments and names</th><th>Logic and accuracy</th><th>Requirements</th></tr>
    <tr><td><b>5 to 6</b></td><td>The program is fully commented. Suitable identifiers, meaningful to their purpose, are used throughout. All the data structures have meaningful names.</td><td>In a logical order. Accurate: it performs all the tasks in the scenario. Minor syntax errors are ignored.</td><td>Meets all the requirements.</td></tr>
    <tr><td><b>3 to 4</b></td><td>Some relevant comments. The majority of identifiers are appropriately named; most structures have meaningful names.</td><td>Parts may be illogical or inaccurate. Lines of code with some errors still perform tasks logically. Minor syntax errors are ignored.</td><td>Meets most of the requirements.</td></tr>
    <tr><td><b>1 to 2</b></td><td>No relevant comments. Some identifiers are appropriate; some structures have meaningful names.</td><td>The solution is illogical, or inaccurate in many places, with few lines performing a task.</td><td>Attempts at least one requirement.</td></tr>
    <tr><td><b>0</b></td><td colspan="3">No creditable response.</td></tr>
  </table></div>

  <h2>4 · How to reach each band</h2>
  <p>The descriptors are about what your program contains. This table turns them into what to check in your own answer.</p>
  <div class="tw"><table class="t">
    <tr><th>Band</th><th>What your program looks like</th><th>What is usually missing to reach the next band</th></tr>
    <tr><td><b>AO2 1 to 3</b></td><td>An INPUT, an IF or a loop and an OUTPUT. Values may sit in single variables, and the arrays in the scenario are not used.</td><td>Apply more than one technique to the scenario, and use the structures the scenario names: a loop over the arrays, not one value.</td></tr>
    <tr><td><b>AO2 4 to 6</b></td><td>The given arrays are used with loops and selection. Several requirements are attempted. For example the times are read into RiderTime[] and the badge count is correct.</td><td>One or more requirements missing or incomplete: no verification, a sort that does one pass, names not carried with times, names not stored in the second array. Every requirement must be covered and all data stored.</td></tr>
    <tr><td><b>AO2 7 to 9</b></td><td>Every requirement is met by an appropriate technique: verification loop, nested iteration for the sort, selection, counting, storing in the given array, and output.</td><td>(Top band.) Check each bullet against the program.</td></tr>
    <tr><td><b>AO3 1 to 2</b></td><td>No comments. A few sensible names. The program does one small part of the scenario.</td><td>Add comments, name things well and complete more requirements.</td></tr>
    <tr><td><b>AO3 3 to 4</b></td><td>Some comments. Most names are meaningful. The program does most of the work, with parts that are wrong.</td><td>Comment every part, use meaningful names everywhere including the loop counters, fix the inaccurate parts and finish every requirement.</td></tr>
    <tr><td><b>AO3 5 to 6</b></td><td>Comments for each part. Meaningful names throughout. Logical order. Every requirement works.</td><td>(Top band.)</td></tr>
  </table></div>
  <p>The two bands move together, because a program that meets all the requirements with the right structures usually shows the habits that AO3 rewards. The lab in the Explore tab turns this table into a checklist for estimating where an answer sits. It is a teaching model, not an official mark.</p>

  <h2>5 · The 30-minute plan</h2>
  <div id="pic1" class="card"></div>
  <ol>
    <li><b>Read (3 minutes).</b> Read to the end. Underline the array and variable names, the numbers (60 riders, under 900 seconds) and the closing instructions.</li>
    <li><b>Checklist (2 minutes).</b> Write one line in the margin for each bullet, with the technique: input twice (loop, comparison), sort both arrays (nested loops), top three (output), store names (selection, counting, second array), output the count.</li>
    <li><b>Write (20 minutes).</b> One requirement at a time, in order, with a comment above each part and a message with each input and output.</li>
    <li><b>Check (5 minutes).</b> Tick each bullet against the code. Look for initialisation, loop limits, whether both arrays move together, and whether every output has a message.</li>
  </ol>

  <h2>6 · The techniques that scenarios keep asking for</h2>
  <h3>Validate a number in a loop</h3>
''' + code(["REPEAT", "    OUTPUT \"Enter the number of rooms (3 to 20)\"", "    INPUT Number", "    IF Number < 3 OR Number > 20", "      THEN", "        OUTPUT \"The number must be between 3 and 20, please try again\"", "    ENDIF", "UNTIL Number >= 3 AND Number <= 20"]) + '''
  <p>The May/June 2023 report notes that some candidates validated with a single IF statement, which allows only one attempt at entering a correct value. A loop allows as many as needed.</p>
  <h3>Enter a value twice and compare (verification)</h3>
''' + code(["REPEAT", "    OUTPUT \"Enter the time\"", "    INPUT FirstEntry", "    OUTPUT \"Enter the time again\"", "    INPUT SecondEntry", "    IF FirstEntry <> SecondEntry", "      THEN", "        OUTPUT \"The times do not match, please try again\"", "    ENDIF", "UNTIL FirstEntry = SecondEntry"]) + '''
  <h3>Sort two arrays together</h3>
  <p>When two arrays hold related data at the same index, every swap must move both. The Oct/Nov 2024 report notes some candidates used only one loop, and some used the min/max method once instead of the three times needed. Use the bubble sort from the previous review and swap the names as well as the times.</p>
  <h3>Store the items that meet a rule in another array</h3>
''' + code(["BadgeCount ← 0", "FOR Index ← 1 TO 60", "    IF RiderTime[Index] < 900", "      THEN", "        BadgeCount ← BadgeCount + 1", "        BadgeName[BadgeCount] ← RiderName[Index]", "    ENDIF", "NEXT Index"]) + '''
  <p>The second array has its own counter. Using <i>Index</i> there would leave gaps in the array. The report for the club scenario says candidates identified the right members but did not store their names in the array given.</p>
  <h3>Nested loops for a 2D array</h3>
''' + code(["FOR Row ← 1 TO 7", "    FOR Reading ← 1 TO 4", "        OUTPUT \"Enter the temperature for day \", Row, \" reading \", Reading", "        INPUT Temperature[Row, Reading]", "    NEXT Reading", "NEXT Row"]) + '''
  <h3>Round, total, find the largest, find the smallest</h3>
''' + code(["TotalArea ← 0", "Largest ← 0", "Smallest ← 100000", "FOR Index ← 1 TO Number", "    TotalArea ← TotalArea + Area[Index]", "    IF Area[Index] > Largest", "      THEN", "        Largest ← Area[Index]", "    ENDIF", "    IF Area[Index] < Smallest", "      THEN", "        Smallest ← Area[Index]", "    ENDIF", "NEXT Index", "AverageArea ← ROUND(TotalArea / Number, 2)"]) + '''
  <p>The Oct/Nov 2024 report for the rooms scenario says variables that need initialising must be initialised: a smallest value starting at 0 would never be replaced, and a total used before it is set gives the wrong answer.</p>

  <h2>7 · One scenario, three answers, three bands</h2>
  <p>This scenario is our own, built on the pattern of a real running club question. Below are three different answers to it and the band each would be given against the published descriptors. These are our own illustrations, not examiner scripts, and an examiner decides the real mark.</p>
  <div class="card"><p><b>Scenario.</b> ''' + SCEN[0] + ' ' + SCEN[1] + '''</p>
  <p>Write a program that: allows each rider's time to be input twice and checks that the two inputs match; sorts <i>RiderTime[]</i> and <i>RiderName[]</i> into ascending order of time; outputs the names and times of the three fastest riders, labelled First, Second and Third; stores the names of all riders who earn a badge in the array <i>BadgeName[]</i>; and outputs the number of badges needed. Use pseudocode or program code and add comments. You do not need to declare any arrays or variables. All inputs and outputs must have suitable messages. [15]</p></div>

  <h3>Answer A: AO2 about 2 of 9, AO3 about 1 of 6</h3>
''' + code(["INPUT Time", "IF Time < 900", "  THEN", "    OUTPUT \"Badge\"", "ENDIF", "OUTPUT Time"]) + '''
  <p>It uses input, selection and output, so some technique is present (AO2 band 1 to 3). It stores one value in a variable and not the arrays in the scenario. There is no loop, so only one rider is handled. No comments (AO3 band 1 to 2). It attempts one requirement: the badge test.</p>

  <h3>Answer B: AO2 about 5 of 9, AO3 about 2 to 3 of 6</h3>
''' + code(["// input the times", "FOR Index ← 1 TO 60", "    OUTPUT \"Enter the time for \", RiderName[Index]", "    INPUT RiderTime[Index]", "NEXT Index", "// sort the times", "FOR Index ← 1 TO 59", "    IF RiderTime[Index] > RiderTime[Index + 1]", "      THEN", "        Temp ← RiderTime[Index]", "        RiderTime[Index] ← RiderTime[Index + 1]", "        RiderTime[Index + 1] ← Temp", "    ENDIF", "NEXT Index", "OUTPUT \"First \", RiderName[1], RiderTime[1]", "OUTPUT \"Second \", RiderName[2], RiderTime[2]", "OUTPUT \"Third \", RiderName[3], RiderTime[3]", "Count ← 0", "FOR Index ← 1 TO 60", "    IF RiderTime[Index] < 900", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]) + '''
  <p>It uses the given arrays with loops, selection and counting: more than one technique applied to the scenario, and some of the data stored in the structures given (AO2 band 4 to 6). It is not in the top band because requirements are missing or wrong: the times are entered once, not twice with a comparison; the sort makes one pass; the names do not move with the times, so a rider can be given another rider's time; and the badge names are not stored in <i>BadgeName[]</i>. It has some comments and mostly sensible names, but parts are inaccurate and fewer than most of the requirements are fully met, so AO3 sits on the border between band 1 to 2 and band 3 to 4. The last output has no message.</p>

  <h3>Answer C: AO2 about 9 of 9, AO3 about 6 of 6</h3>
''' + code(["// input each rider's time twice and check that the inputs match", "FOR Index ← 1 TO 60", "    REPEAT", "        OUTPUT \"Enter the time in seconds for \", RiderName[Index]", "        INPUT FirstEntry", "        OUTPUT \"Enter the time again to confirm\"", "        INPUT SecondEntry", "        IF FirstEntry <> SecondEntry", "          THEN", "            OUTPUT \"The two times do not match, please try again\"", "        ENDIF", "    UNTIL FirstEntry = SecondEntry", "    RiderTime[Index] ← FirstEntry", "NEXT Index", "// bubble sort into ascending order of time, swapping name and time together", "Last ← 60", "REPEAT", "    Swapped ← FALSE", "    FOR Index ← 1 TO Last - 1", "        IF RiderTime[Index] > RiderTime[Index + 1]", "          THEN", "            TempTime ← RiderTime[Index]", "            RiderTime[Index] ← RiderTime[Index + 1]", "            RiderTime[Index + 1] ← TempTime", "            TempName ← RiderName[Index]", "            RiderName[Index] ← RiderName[Index + 1]", "            RiderName[Index + 1] ← TempName", "            Swapped ← TRUE", "        ENDIF", "    NEXT Index", "    Last ← Last - 1", "UNTIL Swapped = FALSE OR Last = 1", "// output the three fastest riders", "OUTPUT \"First: \", RiderName[1], \" with a time of \", RiderTime[1], \" seconds\"", "OUTPUT \"Second: \", RiderName[2], \" with a time of \", RiderTime[2], \" seconds\"", "OUTPUT \"Third: \", RiderName[3], \" with a time of \", RiderTime[3], \" seconds\"", "// store the names of the riders who earn a badge and count them", "BadgeCount ← 0", "FOR Index ← 1 TO 60", "    IF RiderTime[Index] < 900", "      THEN", "        BadgeCount ← BadgeCount + 1", "        BadgeName[BadgeCount] ← RiderName[Index]", "    ENDIF", "NEXT Index", "OUTPUT \"Number of badges needed: \", BadgeCount"]) + '''
  <p>Every bullet has a matching block: a verification loop with the two inputs compared, a bubble sort with nested iteration that moves both arrays, the top three output with labels, the names stored in <i>BadgeName[]</i> with their own counter, and the count output. All the data the scenario requires is stored in the structures it names (AO2 band 7 to 9). Every part has a comment, the names say what they hold, the order is logical and the program does everything asked (AO3 band 5 to 6). It does not declare the arrays, because the scenario says that is unnecessary.</p>

  <h2>8 · Common ways to lose marks</h2>
  <div class="tw"><table class="t">
    <tr><th>What many candidates did</th><th>Where the reports say it</th></tr>
    <tr><td>Input data for one member, not all 200, or ignored the given arrays</td><td>Oct/Nov 2024, paper 21</td></tr>
    <tr><td>Used the arrays without an index or without a loop</td><td>Oct/Nov 2024, paper 21</td></tr>
    <tr><td>Sorted with a single loop, or used the min/max method once instead of three times</td><td>Oct/Nov 2024, paper 21</td></tr>
    <tr><td>Identified the right members but did not store the names in the array given</td><td>Oct/Nov 2024, paper 21</td></tr>
    <tr><td>Declared arrays and variables when the question said it was not needed, spending time that could go on requirements</td><td>Oct/Nov 2024, paper 22; May/June 2024, paper 22</td></tr>
    <tr><td>Forgot to initialise a maximum, a minimum or a total</td><td>Oct/Nov 2024, paper 22</td></tr>
    <tr><td>Found the index of the best team but not the highest points, and wrote nothing for a tie</td><td>May/June 2024, paper 21</td></tr>
    <tr><td>Did not use a nested loop or the 2D array; stated only the seats booked, not whether seats were available</td><td>Oct/Nov 2023, paper 21</td></tr>
    <tr><td>Calculated the averages and the Fahrenheit conversion but did not round</td><td>May/June 2023, paper 21</td></tr>
    <tr><td>Used a program language not in the syllabus</td><td>May/June 2023, paper 21</td></tr>
  </table></div>
'''

watch = '''
  <h2>1 · Plan the scenario in five minutes</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Sorting two arrays together</h2>
  <div id="stB"></div>
  <h2>3 · From a requirement to marks</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Break a scenario into a checklist</h2>
  <p>Choose a scenario to see its data structures, its requirements with the technique each needs, and what the reports say candidates missed.</p>
  <div class="card"><div id="scB" class="btnrow"></div><div id="scO"></div></div>

  <h2>Lab 2 · Estimate the band</h2>
  <p>Describe a program by ticking what it contains. The estimate follows the published band descriptors in a simple way. It is a teaching model, not an official mark.</p>
  <div class="card"><div class="grid2"><div>
    <h3 style="margin-top:0">Techniques and data (AO2)</h3><div id="a2"></div>
    <h3>Comments, names and accuracy (AO3)</h3><div id="a3"></div></div>
    <div><div class="readout"><div><small>AO2 band (out of 9)</small><strong id="b2"></strong></div><div><small>AO3 band (out of 6)</small><strong id="b3"></strong></div><div><small>Estimated total</small><strong id="bt"></strong></div></div>
    <div class="verdict" id="bv"></div></div></div></div>

  <h2>Lab 3 · The 30 minutes</h2>
  <p>Choose how long to read and plan, and how long to check, and see how many minutes are left to write each requirement.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Minutes for writing</small><strong id="r1"></strong></div><div><small>Minutes per requirement</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="A bar divided into read, write and check"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which AO2 band does each feature belong to?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which AO3 band does each feature belong to?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the 30-minute plan in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the instruction to what it means</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '<p class="note">These come from the Principal Examiner Reports for Cambridge IGCSE Computer Science, which describe what candidates actually wrote. The wording is ours.</p>\n' + (
rw("Data for one member, not all", "Oct/Nov 2024, paper 21 (a running club): most candidates attempted the input requirement but did not use the arrays in the question. Most entered the data for one member, not the 200 stated, and many did not use an index or a loop to input all the times.", "read the numbers in the scenario and make the loop limits match them.") +
rw("Declaring what was already declared", "Oct/Nov 2024, paper 22 (house rooms): many candidates spent time declaring arrays and variables when the question said it was not necessary. Marks are given for covering the requirements, so the time is better spent there.", "read the closing instructions before writing anything.") +
rw("The maximum that never changed", "Oct/Nov 2024, paper 22: finding the largest and smallest room needs a maximum and a minimum that are initialised sensibly, and totals must be set before they are used. Initialisation still has to be shown.", "start the smallest at a large number or at the first item.") +
rw("The top team but not the points", "May/June 2024, paper 21 (a league): some candidates found only the index of the team with the highest points, not the points themselves, and most wrote nothing for a tie for first place.", "ask what the requirement says to output, and what could go wrong with the data.") +
rw("Only the seats booked", "Oct/Nov 2023, paper 21 (theatre seats): requirement 1 was not attempted well because candidates did not use a nested loop or the 2D array, and requirement 3 was met by only a few because the output only stated the seats booked, not whether any were available.", "use the array structure as described and output what the requirement asks.") +
rw("A single attempt at validating", "May/June 2023, paper 21 (weekly temperatures): a few candidates used an IF statement for validation, which allows one attempt. A loop within the loops was the strongest approach. Many calculated and converted correctly but did not round.", "validation needs a loop; read each requirement for rounding.") +
rw("What the strongest answers did", "Every series, the reports say the strongest candidates matched the requirements closely, used the data structures as the scenario described them, commented each part, and gave a message for every input and output.", "the closing instructions in the scenario are marking instructions.")
)

exam = cs_exam("the 15-mark scenario",
  "Six scenario questions in the style of the last question of Paper 2. They are our own scenarios, built on the real pattern. For each, write your plan, write the program, then compare it with the checklist, which uses the real mark scheme requirements where one is published and the examiner report where it is not.",
  [("Scenario questions (Paper 2)", "6 shown below", "Oct/Nov 2024 (21) Q11, Oct/Nov 2024 (22) Q12, Oct/Nov 2023 (21) Q10, May/June 2024 (21) Q10, May/June 2023 (21) Q11, Feb/March 2025 (22) Q10")], [
  ceq(CP("w24_21", "11"), "[15]", SCEN[0] + " " + SCEN[1] + " Write a program that allows each time to be input twice and checks that the inputs match; sorts both arrays into ascending order of time; outputs the three fastest riders as First, Second and Third; stores the names of riders who earn a badge in BadgeName[]; outputs the number of badges needed. Use comments and give every input and output a message. You do not need to declare any arrays or variables.",
    ["AO2 maximum 9, AO3 maximum 6. Data structures required, named as given: RiderName[], RiderTime[], BadgeName[]", "R1 input and verify the times (input, iteration)", "R2 sort both arrays in ascending order of time and output the top three (nested iteration, sorting, selection, output)", "R3 store the names of the riders who get a badge and output the number (iteration, selection, counting, output)", "AO2 top band: every requirement covered by an appropriate technique and all the data stored in appropriate structures", "AO3 top band: fully commented, meaningful identifiers, logical order, accurate, all requirements"],
    "<p>Checklist: loop of 60; two inputs and a comparison in a REPEAT; bubble sort moving both arrays; three labelled outputs; BadgeName[] with its own counter; a message with the count. The full model answer is in the Learn tab.</p>"),
  ceq(CP("w24_22", "12"), "[15]", "A garden centre stores the names of up to 12 flower beds in the 1D array BedName[] and the length, width and area of each bed in the 2D array BedSize[]. The variable NumberOfBeds holds the number of beds, which must be at least 2 and no more than 12. Write a program that: inputs and validates the number of beds; inputs each bed's name, length and width in metres; calculates and stores the area, rounded to 2 decimal places; calculates the total area and the average area, rounded to 2 decimal places; finds the largest and smallest beds by area; outputs every bed's name, dimensions and area; and outputs the names of the largest and smallest beds, the total area and the average. Use comments and messages. You do not need to declare any arrays or variables.",
    ["Structures: a 1D array for the names, a 2D array for the dimensions and area, and a variable for the number", "R1 input and store the number of beds, the names and the dimensions, with validation of the number (input with prompts, nested iteration, variables, 1D and 2D arrays, validation)", "R2 calculate and store the areas, the total and the average, rounded; find the smallest and largest (calculation, totalling, rounding, maximum and minimum, iteration)", "R3 output the results, including the contents of the arrays and the calculated data (iteration, output)", "The report: variables for the maximum and minimum and the total need initialising; declaring arrays was not required"],
    "<p>Checklist: validate NumberOfBeds in a REPEAT loop; FOR loop to input; ROUND(Length * Width, 2); total with TotalArea ← 0; Largest and Smallest set before the loop; output loop; final outputs with messages.</p>"),
  ceq(CP("w23_21", "10"), "[15]", "A cinema hall has 8 rows of 15 seats. The 2D Boolean array Seat[1:8, 1:15] holds FALSE for a seat that is free and TRUE for a seat that is booked. A customer can book from 1 to 5 seats at a time, and seats are given in order from those free. Write a program that: counts and outputs the number of free seats; inputs and validates the number of seats the customer wants; checks whether enough free seats are left and outputs suitable messages; and books the seats if there are enough. You do not need to declare any arrays or variables.",
    ["Structures: a 2D array for the seats (Boolean) and variables for the counters and the number wanted", "R1 find the number of seats available and output it (searching, nested iteration, output)", "R2 input and validate the number of seats (input, iteration, selection)", "R3 check whether seats are available (selection, assignment, output with appropriate messages)", "The report: many did not use a nested loop or the 2D array; the output often stated only the seats booked, not whether any were available"],
    "<p>Checklist: nested FOR loops over Row and Column counting FALSE values; REPEAT loop validating 1 to 5; IF free seats >= wanted; a loop that sets the next free seats to TRUE; separate messages for 'not enough seats' and for a booking made.</p>"),
  ceq(CP("s24_21", "10"), "[15]", "A hockey league has 8 teams. The array TeamName[] holds the names. For each team the program must input the number of games played, wins, draws and losses, and check that wins + draws + losses equals the games played. A win scores 3 points, a draw 1 and a loss 0. Write a program that stores the data, calculates each team's points in the array Points[], finds the highest number of points, and outputs the name of every team with the highest number of points. Use comments and messages.",
    ["Based on the report for May/June 2024 paper 21: the best responses validated the games played against the wins, draws and losses", "Calculation of points for each team (iteration, arithmetic)", "Find the highest points, and not only the index of the team", "Output the team or teams with the highest points: a second loop that outputs every team whose points equal the highest, to cover a tie"],
    "<p>Checklist: loop over 8 teams with a validation loop; Points[Index] ← Wins * 3 + Draws; Highest set from the first team; a second loop for the output, using IF Points[Index] = Highest.</p>"),
  ceq(CP("s23_21", "11"), "[15]", "A weather station records four temperature readings in degrees Celsius on each of 7 days. They are stored in the 2D array Temperature[1:7, 1:4]. Write a program that inputs all the readings with validation (between −20 and 45), calculates the average for each day and for the whole week, and outputs each average in degrees Fahrenheit rounded to 1 decimal place (Fahrenheit = Celsius × 9 / 5 + 32). Use comments and messages.",
    ["Based on the report for May/June 2023 paper 21: requirement 1 was well attempted by most candidates with a nested loop and the 2D array stated", "A few validated with a loop within the loops; a few validated with an IF that allowed one attempt only", "Requirements 2 and 3 were fairly well attempted, but many calculated the averages and converted correctly and did not round the answer", "Round with ROUND(…, 1) at the point of output"],
    "<p>Checklist: nested FOR loops with a REPEAT validation inside; a day total and average for each day; a week total and average; conversion to Fahrenheit; ROUND to 1 decimal place; messages.</p>"),
  ceq(CP("m25_22", "10"), "[15]", "A sports club stores its members' codes in the 1D array MemberCode[] and their first and last names in the 2D array MemberName[]. The variable NewCode holds a new code. Write a program that shows a menu with three options: 1 add a new member; 2 display all members' names and codes; 3 end the program. To add a member, input the new code, the first name and the last name, and check that the code has exactly 6 characters and has not been used before. Use comments and messages. You do not need to declare any arrays or variables.",
    ["Based on the report for Feb/March 2025: the scenario required a menu with three options, a check that the code had six characters and had not been used before, a list of all members and an option to end", "Stronger responses closely matched the requirements and used all the data structures as described: a 1D array for the codes, a 2D array for the names, a variable for the new code", "Use LENGTH for the length check; a loop through the existing codes for the uniqueness check; a REPEAT loop for the menu"],
    "<p>Checklist: REPEAT … UNTIL Choice = 3 around a CASE or IF structure; a validation loop with LENGTH(NewCode) = 6; a search loop for a duplicate; storage of first and last names in the 2D array; an output loop; messages for each option.</p>"),
])

tips = tips_html(
  [("Read to the end first.", "Names, numbers and the closing instructions."),
   ("Turn each bullet into a checklist line.", "One technique for each."),
   ("Use the names given.", "In the way they are described."),
   ("Do not declare what is declared.", "Initialise what needs initialising."),
   ("Comment each part.", "And a message with every input and output."),
   ("Both arrays move together.", "Swap names as well as times."),
   ("Check against the list.", "Tick every bullet in the last five minutes.")],
  [("A comment", "// input each time twice and check that the two inputs match"),
   ("A message", "OUTPUT \"Enter the time in seconds for \", RiderName[Index]"),
   ("A validation loop", "REPEAT … UNTIL the value is in the range"),
   ("Storing items", "BadgeName[BadgeCount] ← RiderName[Index]"),
   ("Rounding", "AverageArea ← ROUND(TotalArea / Number, 2)")],
  [("Write", "Write the program as asked, in pseudocode or program code."), ("Comment", "Explain the purpose of each part in the code."), ("Validate", "Reject unsuitable input and ask again."), ("Verify", "Enter twice and compare."), ("Initialise", "Give a variable its starting value before the loop.")]) + FC

js = CHAINJS + PICKJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Read", "3 min", "Names, numbers, instructions", 20, "f1", 100], ["Plan", "2 min", "One checklist line per bullet", 130, "f3", 120], ["Write", "20 min", "Requirement by requirement, with comments", 260, "f2", 330], ["Check", "5 min", "Tick every bullet", 600, "f1", 140]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d.length > Math.floor(w / 6.2) ? d.slice(0, Math.floor(w / 6.2)) + "…" : d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Plan for the 30 minutes of the scenario question">${o}</svg>`;
})();
chainStep("#stA", "Planning the scenario", ["Read to the end: note RiderName[], RiderTime[], BadgeName[], 60 riders, 900 seconds", "Write one checklist line per bullet: twice and match; sort both; top three; store names; count", "Choose the technique for each line: loop, nested loops, selection, counter and second array", "Write in the order of the list, a comment above each part, a message on every input and output"], [
  "<b>Read:</b> the names and numbers you will use.", "<b>Checklist:</b> this is the mark scheme in your own words.", "<b>Techniques:</b> the mark scheme lists these beside each requirement.", "<b>Write:</b> the order of the list is the order of the program."]);
chainStep("#stC", "One requirement turned into marks", ["Requirement: store the names of riders who earn a badge in BadgeName[]", "Technique: a loop with selection and a counter that has its own index in the second array", "Code: IF RiderTime[Index] < 900 THEN BadgeCount ← BadgeCount + 1, BadgeName[BadgeCount] ← RiderName[Index]", "Marks: an appropriate technique and data stored in the structure (AO2); a comment and sensible names (AO3)"], [
  "<b>Requirement:</b> taken straight from a bullet.", "<b>Technique:</b> iteration, selection, counting.", "<b>Code:</b> the counter is separate from Index.", "<b>Marks:</b> AO2 for technique and data, AO3 for clarity and a requirement met."]);

/* ---- parallel arrays sort animation ---- */
const PF = [
  { n: ["Ana", "Ben", "Cal"], t: [95, 80, 88], hl: [], note: "Each rider's name and time sit at the same index." },
  { n: ["Ana", "Ben", "Cal"], t: [80, 95, 88], hl: [0, 1], bad: true, note: "Only the times were swapped. Ana now has 80 and Ben has 95: the pairing is broken." },
  { n: ["Ben", "Ana", "Cal"], t: [80, 95, 88], hl: [0, 1], note: "Swap the names too. Ben 80, Ana 95: the pairs are kept." },
  { n: ["Ben", "Cal", "Ana"], t: [80, 88, 95], hl: [1, 2], note: "Compare 95 and 88: swap both arrays again." },
  { n: ["Ben", "Cal", "Ana"], t: [80, 88, 95], hl: [], done: true, note: "Sorted. Index 1 holds the fastest rider, so RiderName[1] and RiderTime[1] give First." }
];
function pfDraw(s) {
  const f = PF[Math.max(0, Math.min(PF.length - 1, Math.round(s.i)))]; let o = SV.text(40, 40, "RiderName[]", "sm bd") + SV.text(40, 130, "RiderTime[]", "sm bd");
  [0, 1, 2].forEach((i) => {
    const x = 60 + i * 150, hl = f.hl.includes(i), c = hl ? (f.bad ? "f3" : "f1") : "f2";
    o += SV.rect(x, 52, 120, 44, c, { rx: 8, ...op(0.55) }) + SV.text(x + 60, 80, f.n[i], "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    o += SV.rect(x, 142, 120, 44, c, { rx: 8, ...op(0.55) }) + SV.text(x + 60, 170, f.t[i], "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" });
    o += SV.text(x + 60, 112, "index " + (i + 1), "sm", { "text-anchor": "middle" });
  });
  return o;
}
Lib.stepper($("#stB"), { w: 560, h: 210, label: "Sorting two parallel arrays together", base: { i: 0 }, draw: pfDraw, tween: 300, dwell: 4800, steps: PF.map((f, i) => ({ cap: "<b>" + (i === 1 ? "Wrong" : i === 4 ? "Done" : i === 0 ? "Start" : "Right") + ":</b> " + f.note, s: { i } })) });

/* ---- scenario decomposer ---- */
pick("sc", [
  { label: "Running club (Oct/Nov 2024, 21)", s: "1D arrays MemberName[], MemberTime[], MemberCertificate[], Position[]; variables such as ClubSize, TempTime, TempName, Swap, Count", r: [["R1", "Input and verify each member's time", "input, iteration"], ["R2", "Sort both arrays into ascending order of time and output the top three", "nested iteration, sorting, selection, output"], ["R3", "Store the names of members who get a certificate and output the number", "iteration, selection, counting, output"]], m: "One member only, not 200; the arrays not used or no index; a sort with one loop; the min/max method used once not three times; names not stored in the array given" },
  { label: "House rooms (Oct/Nov 2024, 22)", s: "1D array Rooms[], 2D array Dimensions[], variable Number", r: [["R1", "Input and store the number of rooms (validated), the names and the dimensions", "input with prompts, nested iteration, 1D and 2D arrays, validation"], ["R2", "Calculate and store the areas, total and average (rounded); find the smallest and largest", "calculation, totalling, rounding, maximum and minimum, iteration"], ["R3", "Output the results including the contents of the arrays", "iteration, output"]], m: "Declaring arrays and variables without need; maximum, minimum and totals not initialised" },
  { label: "Theatre seats (Oct/Nov 2023, 21)", s: "2D array Evening[1:10, 1:20]; variables Counter, SeatCounter, NumSeats, Row, Column", r: [["R1", "Find the number of seats available for each performance and output it", "searching, nested iteration, output"], ["R2", "Input and validate the number of seats", "input, iteration, selection"], ["R3", "Check whether seats are available and book them", "selection, assignment, output with appropriate messages"]], m: "No nested loop and not using the 2D array; output states only the seats booked, not whether seats were available" }
], (it) => `<p><small>Data structures named</small><br>${it.s}</p><div class="tw"><table class="t"><tr><th></th><th>Requirement</th><th>Technique the mark scheme lists</th></tr>${it.r.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td></tr>`).join("")}</table></div><div class="verdict"><b>What the reports say was missed:</b> ${it.m}.</div>`);

/* ---- band estimator ---- */
const A2L = [["io", "Uses input and output"], ["loop", "Uses a loop to handle every item"], ["sel", "Uses selection to decide"], ["ct", "Uses counting or totalling"], ["ns", "Sorts or searches with nested iteration (if the scenario needs it)"], ["ver", "Verifies or validates input in a loop (if the scenario needs it)"], ["arr", "Uses the arrays or variables the scenario names"], ["all", "Stores all the data the scenario asks for"], ["cov", "Meets every requirement with an appropriate technique"]];
$("#a2").innerHTML = A2L.map(([k, t]) => `<label style="display:block;margin:5px 0"><input type="checkbox" data-k="${k}"> ${t}</label>`).join("");
$("#a3").innerHTML = `<label style="display:block;margin:5px 0">Comments <select id="cm"><option value="0">none</option><option value="1">some</option><option value="2">every part</option></select></label>
<label style="display:block;margin:5px 0">Identifiers <select id="id"><option value="0">few meaningful</option><option value="1">some</option><option value="2">most</option><option value="3">all, including data structures</option></select></label>
<label style="display:block;margin:5px 0">Requirements met <select id="rq"><option value="0">none</option><option value="1">at least one</option><option value="2">most</option><option value="3">all</option></select></label>
<label style="display:block;margin:5px 0"><input type="checkbox" id="lg"> In a logical order</label><label style="display:block;margin:5px 0"><input type="checkbox" id="ac"> Accurate: it works</label>`;
function band() {
  const t = {}; $$("#a2 input").forEach((c) => (t[c.dataset.k] = c.checked));
  const tech = ["loop", "sel", "ct", "ns", "ver"].filter((k) => t[k]).length, any = Object.values(t).some(Boolean);
  const a2 = !any ? [0, "0"] : t.all && t.cov && t.arr ? [8, "7 to 9"] : tech >= 2 && t.arr ? [5, "4 to 6"] : [2, "1 to 3"];
  const cm = +$("#cm").value, idv = +$("#id").value, rq = +$("#rq").value, lg = $("#lg").checked, ac = $("#ac").checked;
  const a3 = cm === 2 && idv === 3 && rq === 3 && lg && ac ? [6, "5 to 6"] : cm >= 1 && idv >= 2 && rq >= 2 ? [4, "3 to 4"] : (rq >= 1 || cm >= 1 || idv >= 1) ? [1, "1 to 2"] : [0, "0"];
  $("#b2").textContent = a2[1]; $("#b3").textContent = a3[1]; $("#bt").textContent = (a2[0] + a3[0]) + " approx.";
  const nextA = a2[1] === "7 to 9" ? "AO2 is in the top band." : a2[1] === "4 to 6" ? "To reach AO2 7 to 9, cover every requirement and store all the data in the structures the scenario names." : a2[1] === "1 to 3" ? "To reach AO2 4 to 6, apply at least two techniques to the scenario and use the arrays it names." : "Write something: any input, selection, loop or output earns credit.";
  const nextB = a3[1] === "5 to 6" ? "AO3 is in the top band." : a3[1] === "3 to 4" ? "To reach AO3 5 to 6, comment every part, use meaningful names throughout, put it in a logical order and make it work." : a3[1] === "1 to 2" ? "To reach AO3 3 to 4, add comments, name most things well and meet most of the requirements." : "Attempt at least one requirement.";
  $("#bv").textContent = nextA + " " + nextB;
}
$$("#a2 input, #a3 input, #a3 select").forEach((e) => e.addEventListener("input", band)); band();

function pl() {
  if (!$("#rd") || !$("#ck")) return;
  const rd = +$("#rd").value, ck = +$("#ck").value, wr = 30 - rd - ck;
  $("#r1").textContent = wr + " min"; $("#r2").textContent = Lib.fmtN(wr / 3, 1) + " min";
  $("#rv").textContent = `${rd} minutes reading and planning and ${ck} minutes checking leave ${wr} minutes to write, about ${Lib.fmtN(wr / 3, 1)} minutes for each of three requirements. ` + (wr / 3 < 6 ? "That is tight: the writing will have to be fast." : wr / 3 > 8 ? "Plenty of time: do not skip the check." : "A workable balance.");
  const W = 380, X = (v) => 20 + (v / 30) * W;
  $("#labA").innerHTML = SV.rect(X(0), 70, X(rd) - X(0), 50, "f1", op(0.5)) + SV.rect(X(rd), 70, X(rd + wr) - X(rd), 50, "f2", op(0.5)) + SV.rect(X(rd + wr), 70, X(30) - X(rd + wr), 50, "f3", op(0.5)) + SV.text(X(rd / 2), 100, rd, "sm", { "text-anchor": "middle" }) + SV.text(X(rd + wr / 2), 100, "Write: " + wr, "sm", { "text-anchor": "middle" }) + SV.text(X(rd + wr + ck / 2), 100, ck, "sm", { "text-anchor": "middle" }) + SV.text(210, 150, "30 minutes", "sm", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "rd", label: "Minutes reading and planning ", min: 2, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: pl });
Lib.slider($("#g2"), { id: "ck", label: "Minutes checking ", min: 2, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: pl });
pl();
''' + CLASSIFY("cl1", "Which AO2 band does each feature describe?", ["Band 1 to 3", "Band 4 to 6", "Band 7 to 9"],
  [("Uses input, selection and output only", 0), ("Stores a value in a variable but not in the arrays given", 0), ("More than one technique applied to the scenario", 1), ("Uses some of the given structures and stores some of the data", 1),
   ("Every requirement is met by an appropriate technique", 2), ("The structures chosen store all the data the scenario requires", 2)],
  "Low: some technique. Middle: several techniques, some data stored. Top: every requirement and all the data.") + CLASSIFY("cl2", "Which AO3 band does each feature describe?", ["Band 1 to 2", "Band 3 to 4", "Band 5 to 6"],
  [("No relevant comments", 0), ("Attempts at least one requirement", 0), ("Some relevant comments", 1), ("The majority of identifiers are appropriately named", 1), ("Meets most of the requirements", 1),
   ("Fully commented", 2), ("Meaningful names throughout, including all data structures", 2), ("In a logical order and accurate", 2), ("Meets all the requirements", 2)],
  "Comments, names, accuracy and requirements all move up together.") + ORDER(
  "Put the 30-minute plan in order.",
  ["Read the scenario to the end", "Write a checklist line for each requirement", "Write the program one requirement at a time, with comments", "Check each requirement against the code"],
  "Read, checklist, write, check.") + MATCH([
  ["You do not need to declare any arrays", "Use them without declaring them"], ["All inputs and outputs must contain suitable messages", "Put a prompt before each input and a message with each output"], ["Add comments to explain how your code works", "Comment each part of the solution"], ["Names are stored in the array MemberName[]", "Use that array, with that name"], ["Use pseudocode or program code", "Pseudocode, Python, Visual Basic or Java"]]) + CALC([
  {"q": "The scenario question is 15 marks with AO2 worth 9. What percentage of its marks is AO2?", "a": 60, "unit": "%", "tol": 0.5, "hint": "9 ÷ 15.", "sol": "<b>60%</b>."},
  {"q": "You spend 3 minutes reading, 2 minutes planning and 5 minutes checking in a 30-minute question. How many minutes are left for writing?", "a": 20, "unit": "min", "tol": 0.1, "hint": "30 − 10.", "sol": "<b>20 minutes</b>."},
  {"q": "A bubble sort on 60 riders needs at most how many passes?", "a": 59, "unit": "", "tol": 0.01, "hint": "n − 1.", "sol": "<b>59</b>."},
  {"q": "Five rooms have areas totalling 126.5 m². What is the average area, rounded to 2 decimal places?", "a": 25.3, "unit": "m²", "tol": 0.005, "hint": "126.5 ÷ 5.", "sol": "<b>25.30</b>."},
  {"q": "With 21 minutes for writing three requirements, how many minutes does each get?", "a": 7, "unit": "min", "tol": 0.05, "hint": "21 ÷ 3.", "sol": "<b>7 minutes</b>."}]) + MCQ([
  ("What does the syllabus suggest for the time on the 15-mark scenario question?", ["10 minutes", "20 minutes", "30 minutes", "45 minutes"], 2, "About 30 minutes."),
  ("The scenario says 'you do not need to declare any arrays or variables'. What should you do?", ["Declare them anyway", "Use them without declaring them, and initialise only what needs a starting value", "Not use them", "Ask the invigilator"], 1, "The reports say the time is better spent on the requirements."),
  ("Two arrays hold names and times for the same riders. When sorting by time, what must each swap do?", ["Move the times only", "Move the names and the times together", "Move the names only", "Delete one array"], 1, "Otherwise the pairs are broken."),
  ("Which gets AO3 credit?", ["Using a long program", "Comments and meaningful identifiers", "Using three languages", "A very short program"], 1, "AO3 rewards comments, names, logic and accuracy."),
  ("How should a second array of selected items be indexed?", ["With the same Index as the first array", "With its own counter", "With a random number", "Not at all"], 1, "Its own counter avoids gaps.")
], "qz1") + CARDS([
  ("Scenario question", "15 marks, about 30 minutes."), ("Marking", "AO2 out of 9, AO3 out of 6."), ("Plan", "Read, checklist, write, check."), ("Use the names", "Arrays and variables as described."),
  ("Do not declare", "If the question says it is not needed."), ("Initialise", "Totals, largest, smallest."), ("Comments", "Every part."), ("Messages", "Every input and output.")])

build("cx4", "ig-cs-scenario-question-technique", "The 15-Mark Scenario Question: How Each Band Is Reached", EYC,
  "How the last question of Paper 2 is marked, what the AO2 and AO3 bands look like in a real program, a 30-minute plan, the techniques scenarios keep asking for, and six practice scenarios.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
