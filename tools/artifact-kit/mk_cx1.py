"""IGCSE CS exam technique 1: command words and mark allocation. Run: python3 tools/artifact-kit/mk_cx1.py"""
from csk import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Every question in Paper 1 and Paper 2 has a <b>command word</b> and a <b>mark</b>, and together they say how much to write and what kind of sentence earns credit. A <b>state</b> or <b>identify</b> question wants a short fact, a <b>describe</b> question wants the features, and an <b>explain</b> question wants a reason, so it earns marks only when it says <b>why</b> or <b>how</b>. The examiner reports for every recent series ask for the same three habits: use <b>technical terms</b>, use the <b>context</b> in the question, and answer the <b>command word</b>. Mark schemes mostly award one mark per point, often in <b>pairs</b> of a point and the reason that goes with it, so a 4-mark explain question needs two points with a reason each. A wrong extra statement does not lose a mark (the generic marking principles say marks are not deducted for errors), but a sentence that repeats the question or lists without saying how it helps earns nothing.</p></div>

  <h2>1 · The command words in the syllabus</h2>
  <p>The syllabus lists these words and says the way each is used relates to the subject context. The right-hand column is what to write.</p>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What the syllabus means by it</th><th>What to write</th></tr>
    <tr><td><b>Identify</b></td><td>Name, select or recognise</td><td>The name only: tick the box, circle it, or write one word. Extra explanation earns no extra mark.</td></tr>
    <tr><td><b>State</b></td><td>Express in clear terms</td><td>One clear statement for each mark, with no reasoning.</td></tr>
    <tr><td><b>Give</b></td><td>Produce an answer from a source or from memory</td><td>A recalled fact or an example, kept short.</td></tr>
    <tr><td><b>Define</b></td><td>Give the precise meaning</td><td>The exact meaning using the technical term. "An address for a website" is too vague; "a text-based address" is the detail the mark scheme looks for.</td></tr>
    <tr><td><b>Outline</b></td><td>Set out the main points</td><td>Usually a name and a short expansion, for example the type of check and how it works.</td></tr>
    <tr><td><b>Describe</b></td><td>State the points of a topic: its characteristics and main features</td><td>What it is made of or what happens, in parts or in order. It says <i>what</i>, not <i>why</i>.</td></tr>
    <tr><td><b>Explain</b></td><td>Set out purposes or reasons; make relationships clear; say why and/or how, with support</td><td>A point plus its reason or effect, joined with <i>so</i>, <i>because</i> or <i>which means</i>.</td></tr>
    <tr><td><b>Compare</b></td><td>Comment on similarities and/or differences</td><td>Both items in every point. "Hexadecimal uses letters" is half a comparison.</td></tr>
    <tr><td><b>Suggest</b></td><td>Apply knowledge to a situation with a range of valid answers; put forward considerations</td><td>A sensible choice that fits the scenario, with a reason. Several answers are accepted, but a generic one is not.</td></tr>
    <tr><td><b>Calculate, Show (that), Demonstrate</b></td><td>Work out from facts; give structured evidence leading to a result; show how</td><td>Working in the form asked, such as binary addition with the carries shown, then the answer.</td></tr>
  </table></div>

  <h2>2 · The mark tells you how many points</h2>
  <p>These are the wordings that appear in the published mark schemes, with what each means for your answer.</p>
  <div class="tw"><table class="t">
    <tr><th>Mark scheme wording</th><th>What it means for you</th><th>Where it appeared</th></tr>
    <tr><td><b>Any two from…</b> (2 marks)</td><td>Two separate valid points. A third point earns nothing extra.</td><td>Two input devices for a smart phone (Oct/Nov 2024, paper 11)</td></tr>
    <tr><td><b>One mark for identifying, one for a matching description</b></td><td>Pairs. Name it, then say what it does.</td><td>One more function of an operating system (Oct/Nov 2024, paper 11)</td></tr>
    <tr><td><b>One mark for naming the check, one for an expansion</b></td><td>Name plus how it works.</td><td>Outline one verification check (Oct/Nov 2024, paper 22)</td></tr>
    <tr><td><b>One mark for each method, one for a further description (max six)</b></td><td>Three methods earn six only if each has its description.</td><td>Three methods for designing a solution (Oct/Nov 2024, paper 21)</td></tr>
    <tr><td><b>Six from, with a maximum of 4 for stating features</b></td><td>Names alone are capped. The last two marks need what each feature does.</td><td>Features of an IDE (Oct/Nov 2024, paper 11)</td></tr>
    <tr><td><b>Any four from</b>, bullets in point-then-reason chains</td><td>Make a point, then develop it with a reason. The bullet that starts with "…" continues the point above it.</td><td>Benefits of cloud storage (Oct/Nov 2024, paper 12)</td></tr>
    <tr><td><b>One mark for working, one for the answer</b></td><td>Show the method even when you are sure of the answer.</td><td>Binary addition and conversions (Oct/Nov 2024)</td></tr>
    <tr><td><b>One mark for each correct part of the diagram</b></td><td>Labelled parts and arrows each earn a mark; a neat but unlabelled box earns little.</td><td>Decode stage, DNS lookup, blockchain (Oct/Nov 2024)</td></tr>
  </table></div>

  <h2>3 · The three habits the examiner reports keep asking for</h2>
  <div class="tw"><table class="t">
    <tr><th>Habit</th><th>What the reports say</th><th>What to do</th></tr>
    <tr><td><b>Use technical terms</b></td><td>The Oct/Nov 2024 reports ask for "a greater use of technical terminology". One example given: "faster to email" is vague.</td><td>Say <i>transmitted in less time</i>, <i>uses less bandwidth</i>, <i>fits the file size limit</i>.</td></tr>
    <tr><td><b>Use the context</b></td><td>Answers that ignore the scenario score lower. Examples in the reports: a mouse suggested as an input device for a smart phone, a printer as an output device. The March 2025 report says a question about machine learning in a search engine needs more than a general description of machine learning.</td><td>Put the device, user or system from the question into the answer.</td></tr>
    <tr><td><b>Answer the command word</b></td><td>Several series say "explain" needs more detail than "state" or "identify", and an explain answer usually says how something is done, not just what is done.</td><td>Circle the command word before you read the rest of the question.</td></tr>
  </table></div>

  <h2>4 · One topic, three command words</h2>
  <p>Take parallel data transmission. The same fact is written three ways, depending on what the question asks.</p>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>A full-mark style answer</th></tr>
    <tr><td><b>State</b> what parallel transmission does [1]</td><td>It sends several bits at the same time.</td></tr>
    <tr><td><b>Describe</b> parallel full-duplex transmission [3]</td><td>Several bits are sent at the same time, each along its own wire. Data can travel in both directions at the same time.</td></tr>
    <tr><td><b>Explain why</b> a company used parallel full-duplex between computers in one room [4]</td><td>Several bits are sent at once along several wires, so data arrives quickly. The computers are in one room, so the data does not travel far and the bits stay in step. Data goes both ways at once, so users can send to each other with no delay.</td></tr>
  </table></div>
  <p>The examiner report for Oct/Nov 2024 (paper 11) notes that some candidates described how data is transmitted instead of explaining why the company would choose that method. A description of the method scores few marks when the question is "why".</p>

  <h2>5 · Differences, advantages and drawbacks</h2>
  <ul>
    <li><b>Both sides in every difference.</b> The report for paper 12 says some candidates gave one difference split across two answer lines, and that "hexadecimal uses letters" alone is not enough because it never mentions binary.</li>
    <li><b>An advantage is not a difference.</b> The report for paper 13 says some candidates wrote that Unicode uses more bits than ASCII without saying what the advantage is. The advantage is that more characters, symbols and languages can be represented. The drawback is that each character needs more storage.</li>
    <li><b>Say which way something changes.</b> The report for the March 2024 series says "the clock speed increases the performance" does not state whether the clock speed went up or down. Write "a higher clock speed means more instructions are carried out each second".</li>
  </ul>

  <h2>6 · Answer the question that was asked</h2>
  <p>Each row is a real pattern from the Oct/Nov 2024 examiner reports: the question asked, and what many candidates wrote instead.</p>
  <div class="tw"><table class="t">
    <tr><th>The question asked</th><th>What many wrote instead</th><th>What earns the mark</th></tr>
    <tr><td>The role of ROM in a smartwatch</td><td>A description of primary storage</td><td>Stores the start-up instructions, such as the bootstrap or firmware, in non-volatile storage</td></tr>
    <tr><td>A benefit of compression for storing a file</td><td>A benefit for transmitting it</td><td>Takes up less storage space</td></tr>
    <tr><td>Why lossy compression is not suitable for a report</td><td>What lossy compression is</td><td>Data is permanently removed and could be important, and lossy is not suitable for text</td></tr>
    <tr><td>The role of the microprocessor in an automated system</td><td>How the whole system works</td><td>Receives sensor data, analyses it, sends signals to trigger actions</td></tr>
    <tr><td>How a check digit detects an error in a barcode</td><td>How a barcode scanner works</td><td>Recalculated after scanning with the same algorithm; a different value means an error</td></tr>
    <tr><td>How features of an IDE help the programmer</td><td>A list of features</td><td>Each feature plus what it allows the programmer to do</td></tr>
    <tr><td>Why the email data is encrypted</td><td>"It stops the data being stolen"</td><td>It makes the data meaningless to anyone who steals it</td></tr>
  </table></div>

  <h2>7 · Writing a 4-mark explanation</h2>
  <ol>
    <li><b>Read</b> the command word and the marks. 4 marks for an explanation usually means two points, each with its reason.</li>
    <li><b>Underline</b> the key term and the scenario: "cloud storage", "smartwatch app".</li>
    <li><b>Write a point</b> that uses a technical term, then a link word, then the effect: <i>so</i>, <i>which means</i>, <i>because</i>, <i>this allows</i>.</li>
    <li><b>Apply the "so what?" test.</b> After each sentence ask "so what?" and keep writing until the answer is a consequence for the user, the device or the data.</li>
    <li><b>Check</b> that each pair uses a technical term and fits the context in the question.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th>Link word</th><th>Use it for</th><th>Example</th></tr>
    <tr><td>so</td><td>Result</td><td>"It has no moving parts, so the data is less likely to be lost if the phone is dropped."</td></tr>
    <tr><td>which means</td><td>Consequence for the user</td><td>"The provider maintains the servers, which means the user does not need to buy or look after hardware."</td></tr>
    <tr><td>because</td><td>Reason</td><td>"Serial is more reliable over a long distance because the bits arrive in order."</td></tr>
    <tr><td>this allows</td><td>Purpose</td><td>"An IDE has a run-time environment, which allows the programmer to run the program and see the output."</td></tr>
  </table></div>

  <h2>8 · Common ways to lose marks</h2>
  <ul>
    <li><b>Repeating the question</b> in the answer ("the values do not match so an error has occurred") without saying <i>why</i> a mismatch means an error.</li>
    <li><b>Listing without saying how it helps</b>, in any question that says explain.</li>
    <li><b>Generic answers</b> that could be about any device, when the question names a smart phone, a smartwatch, a plough or a robot vacuum.</li>
    <li><b>One-sided comparisons</b>: only one item mentioned.</li>
    <li><b>Brand names</b>: the paper states that no marks are awarded for brand names of software or hardware.</li>
    <li><b>Answers on extra pages</b> without saying clearly which question they belong to, as the reports remind candidates.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Before writing, circle the command word and write the number of marks next to it. After writing, put a tick beside each separate point. If you have fewer ticks than marks, find the missing point or the missing reason.</div>
'''

watch = watch_html("One topic, three command words", "Turning a vague answer into marks") + '''
  <h2>3 · Adding the context</h2>
  <div id="stC"></div>
'''

explore = chooser_html("h", "Lab 1 · What each command word asks for", "Choose a command word to see what it wants, how to start the sentence, and the trap to avoid.", ["What it wants", "Sentence starter", "Trap"]) + '''
  <h2>Lab 2 · Mark this answer</h2>
  <p>Question: <b>Explain two benefits to the user of a smartwatch app storing its data in the cloud. [4]</b> Choose an answer to see the marks it would earn against the mark scheme points, and why. These are our estimates from the published points; examiners decide the real mark.</p>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>

  <h2>Lab 3 · Add the context</h2>
  <p>Choose a scenario. The generic answer is what many candidates write; the second is the same idea tied to the scenario.</p>
  <div class="card"><div id="xB" class="btnrow"></div><div id="xO"></div></div>

  <h2>Lab 4 · Marks, points and time</h2>
  <p>Choose how many marks the question carries and the kind of question. Paper 1 and Paper 2 each give 75 marks in 105 minutes, which is 1.4 minutes per mark.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2" class="btnrow"></div>
    <div class="readout"><div><small>Separate points to make</small><strong id="r1"></strong></div><div><small>Minutes to spend (1.4 per mark)</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="Bars showing the number of points and the minutes"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Fact, description or explanation?</h2><div id="cl1" class="card"></div>
  <h2>2 · One side or both sides?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for an explain question in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the command word to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '<p class="note">These come from the Principal Examiner Reports for Cambridge IGCSE Computer Science, which describe what candidates actually wrote. The wording is ours.</p>\n' + (
rw("A list of features, not an explanation", "Oct/Nov 2024, paper 11: asked how the features of an IDE help a programmer, many candidates only listed features. Few went on to describe how each feature helps. The mark scheme caps the stating of features at four of the six marks.", "any 'explain how' question with a list of items: name the feature, then say what it lets the user do.") +
rw("A mouse in a smart phone", "Oct/Nov 2024, papers 11 and 12: some candidates gave a mouse or keyboard as input devices, and a printer as an output device, for a smart phone or smartwatch. The accepted answers are devices built into the product: touchscreen, microphone, camera, screen, speaker.", "'suggest' and 'give' questions set in a scenario: choose items that really fit the device.") +
rw("Vague about the URL", "Oct/Nov 2024, paper 12: many candidates described a URL as 'an address for the website'. The mark scheme asks for a text-based address for a website or web page.", "define questions: include the technical detail that makes the definition exact.") +
rw("Describing machine learning instead of using it", "Oct/Nov 2024, papers 12 and 13: asked how a robot vacuum and a plough could use machine learning or AI, many candidates only described what AI is. The mark scheme rewards gathering data, adapting the machine's own process, and an example such as obstacles or the route.", "'how could X use Y' questions: say what data X gathers, what it changes and what the benefit is.") +
rw("Encryption does not stop theft", "Oct/Nov 2024, paper 13: some candidates believed encryption stops data being stolen. It makes stolen data meaningless to the thief, which is what the mark scheme accepts.", "avoid statements that are almost true: 'prevents' versus 'makes meaningless'.") +
rw("Storage versus transmission", "Oct/Nov 2024, paper 12: asked for a benefit of compressing a file for storage, some candidates gave a benefit for transmission. Both are true benefits of compression, but only one answers the question.", "read the last words of the question: for storage, for transmission, for the user, for the programmer.")
)

items = [("w24_11", "6(e)", 6), ("w24_13", "7", 4), ("w24_11", "7(a)(ii)", 2), ("w24_12", "3(a)(ii)", 2), ("w24_13", "2(d)", 3), ("w24_13", "2(c)", 3), ("w24_13", "2(f)(ii)", 2),
         ("w24_13", "2(g)", 3), ("w24_12", "8(c)", 3), ("w24_13", "5(d)", 4), ("w24_11", "4(b)(i)", 4), ("w24_12", "4(d)(ii)", 4), ("w24_12", "4(c)", 2), ("w24_12", "5(a)", 4)]

exam = cs_exam("command words",
  "Fourteen questions from the Oct/Nov 2024 papers, chosen because the examiner reports name each as one where candidates answered a different question from the one asked. Circle the command word, count the marks, plan the points, then check against the mark scheme.",
  crows(items), [
  ceq(CP("w24_11", "6(e)"), "[6]", "A programmer uses an integrated development environment (IDE) to write the assembly language program for an embedded device. Explain how the features of an IDE help the programmer.",
    ["Six marks: up to four for naming features, so at least two must come from saying what a feature does", "Code editor: lets the programmer enter and change the program", "Run-time environment: lets the program be run so the output can be seen", "Error diagnostics: show the programmer where the errors are", "Auto-completion: offers suggestions for commands", "Auto-correction: fixes a command with a small spelling error", "Pretty-print: changes the colour of key words so they are easy to spot"],
    "<p>Choose three features and write each as a pair: the name, then 'which allows the programmer to…'. Three pairs make six marks. Six names with no purpose cap at four.</p>",
    [[("k", "An IDE has error diagnostics,"), ("a", "which show the programmer the line where each error is, so faults in the program for the device can be found and fixed quickly.")], [("k", "It has a run-time environment,"), ("a", "which lets the programmer run the program and see its output without leaving the IDE.")], [("k", "It has a code editor,"), ("a", "which lets the programmer type and change the assembly program in one place.")]]),
  ceq(CP("w24_13", "7"), "[4]", "Explain the purpose of an integrated development environment (IDE).",
    ["Any four from: it is software used to write, develop and edit code", "It is used to test and debug the code", "It has features, with a suitable example such as auto-completion", "It can translate the code into machine code or a low-level language"],
    "<p>'Purpose' means what it is for, not a list of features. State the job (write and edit code), then the other jobs (test, debug, translate), and add a feature as the example.</p>",
    [[("k", "An IDE is a piece of software used to write and edit code in one place."), ("a", "It is also used to test the program and find faults, with features such as auto-completion that suggest commands as the programmer types.")], [("k", "It can translate the code into machine code,"), ("a", "so the programmer can run and test the program without a separate tool.")]]),
  ceq(CP("w24_11", "7(a)(ii)"), "[2]", "Identify one function of an operating system other than handling interrupts, and describe what it does.",
    ["One mark for the function, one for a matching description", "Memory management: deciding what is stored where in memory", "Managing peripherals and drivers: managing communication with connected input and output devices", "Multitasking: switching between tasks that are running", "Platform for running applications: lets application software communicate with the hardware", "System security: for example a username and password", "User accounts: allowing several accounts on one computer"],
    "<p>A pair: name, then what it does. The report says many candidates named a function but did not describe its purpose.</p>"),
  ceq(CP("w24_12", "3(a)(ii)"), "[2]", "Give two differences between binary and hexadecimal.",
    ["Binary is base 2, whereas hexadecimal is base 16", "Binary uses only 0 and 1, whereas hexadecimal uses 0 to 9 and A to F", "Each difference must refer to both number systems"],
    "<p>Write each difference as 'binary… whereas hexadecimal…'. A sentence about hexadecimal only does not earn the mark.</p>"),
  ceq(CP("w24_13", "2(d)"), "[3]", "An email program can use Unicode instead of ASCII. Give two advantages and one drawback of using Unicode.",
    ["Advantages, any two: it can represent more characters; it can represent emojis and symbols; it can represent more languages", "Drawback: each character needs more storage space", "'It uses more bits' is a difference, not an advantage or a drawback"],
    "<p>For each answer ask what the extra bits give you (more characters) and what they cost (more storage).</p>"),
  ceq(CP("w24_13", "2(c)"), "[3]", "A report that contains text and pictures is to be compressed before it is emailed. Explain why lossy compression is not suitable.",
    ["Data is permanently removed, and that could be important data", "Lossy compression is not suitable for text files, as it would damage or corrupt the file", "The pictures in the report would lose quality"],
    "<p>The question is why it is <i>not</i> suitable. Do not define lossy compression. Link to what is in this file: text and pictures.</p>"),
  ceq(CP("w24_13", "2(f)(ii)"), "[2]", "A checksum is calculated from the email data before and after it is sent. Explain why different values show that an error has occurred.",
    ["The checksum is calculated from the data", "It is calculated using the same algorithm each time", "So if the values are different, the data must be different"],
    "<p>The report says many candidates repeated the question. Explain <i>why</i>: same data and same algorithm give the same value.</p>"),
  ceq(CP("w24_13", "2(g)"), "[3]", "(i) Give one reason why the email data is encrypted. (ii) Give two differences between symmetric and asymmetric encryption.",
    ["(i) One from: to keep it secure; the data is sensitive or confidential; to make it meaningless", "(ii) Two from: symmetric uses one key, asymmetric uses two (public and private)", "Symmetric can send its key with the data, asymmetric does not", "Symmetric decrypts with the same key, asymmetric with a different key", "Symmetric is less secure than asymmetric"],
    "<p>Part (i): 'makes it meaningless' is safe; 'stops it being stolen' is the misconception. Part (ii): refer to both types in each difference.</p>"),
  ceq(CP("w24_12", "8(c)"), "[3]", "A robot vacuum cleaner is controlled by a microprocessor. Explain how the robot vacuum could make use of machine learning.",
    ["Any three from: it could gather data while vacuuming, and adapt its own processes", "For example, learning where obstacles are, where dirtier areas are, the shape of a room or the most efficient route", "So it knows which areas to avoid or concentrate on, or which cleaning tool to use"],
    "<p>Three links: data gathered, what it changes, what the benefit is. Do not describe machine learning in general.</p>",
    [[("k", "The vacuum could gather data about the room while it cleans,"), ("a", "such as where furniture is and which areas are dirtier."), ("k", "It could use this data to adapt its own route,"), ("a", "so it avoids obstacles and spends longer on the dirty areas.")]]),
  ceq(CP("w24_13", "5(d)"), "[4]", "A farmer uses an automated plough that is controlled by a microprocessor. Explain how the plough could make use of artificial intelligence.",
    ["Any four from: it could use machine learning and gather data while ploughing", "It could adapt its own process so it makes fewer mistakes", "For example, the dimensions or landscape of the field, or where obstacles are", "It could create a map of the field and develop the most efficient route", "So it knows what to avoid in future"],
    "<p>Same pattern as the robot vacuum: what it gathers, what it adapts, what improves. Use the field, obstacles and route.</p>",
    [[("k", "The plough could use machine learning,"), ("a", "gathering data about the shape of the field and where obstacles such as rocks are while it ploughs."), ("k", "It could build a map of the field"), ("a", "and use it to find the most efficient route, so it makes fewer mistakes and knows what to avoid next time.")]]),
  ceq(CP("w24_11", "4(b)(i)"), "[4]", "Computers in one room of a company send data to each other using parallel full-duplex transmission. Explain why the company chose this method.",
    ["Any four from: it sends several bits at the same time, using several wires, so the transmission is fast", "The devices are in one room, so the data does not travel a long distance", "It sends data in both directions at the same time, so users can send to each other with no delay"],
    "<p>The question is 'why chosen', so every sentence should be a reason that suits one room. A description of how parallel works scores little.</p>"),
  ceq(CP("w24_12", "4(d)(ii)"), "[4]", "A smartwatch app stores user data in the cloud. Explain the benefits to the user of using cloud storage.",
    ["Any four from: no need to maintain the hardware, because the third party maintains the hardware and data security", "Storage can be increased or decreased on demand, so there is no worry about running out", "It saves the cost of buying hardware", "The watch needs less storage, so it can stay small and cost less", "The data can be accessed from other devices, so it is still available if the watch breaks or is lost"],
    "<p>Two benefits, each with its consequence. Do not repeat what cloud storage is; the report says many candidates did.</p>",
    [[("k", "The data can be reached from other devices,"), ("a", "so if the watch breaks or is lost the user's data is still available.")], [("k", "The provider can add storage on demand,"), ("a", "so the user will not run out of space for their health data.")]]),
  ceq(CP("w24_12", "4(c)"), "[2]", "A smartwatch contains ROM. Explain the role of the ROM in the watch.",
    ["Any two from: it stores the BIOS, the bootstrap or the firmware", "It helps start up the watch, because it stores the start-up instructions", "It provides non-volatile storage, so data is kept permanently", "It stores data or instructions that should not change"],
    "<p>'Role in the watch' is the job it does here: start-up instructions kept when the power is off. A definition of primary storage does not answer it.</p>"),
  ceq(CP("w24_12", "5(a)"), "[4]", "A barcode scanning system uses a check digit to check for errors in the data it inputs. Explain how the system operates to check for errors.",
    ["Any four from: a check digit is calculated from the barcode data, using an algorithm such as modulo 11", "It is added to the barcode", "After scanning, the check digit is recalculated using the same algorithm", "If the check digits do not match an error has occurred; if they match, no error occurred"],
    "<p>Give the check digit steps in order: calculate, add, recalculate, compare. The report says many candidates described how a barcode scanner works instead.</p>"),
])

tips = tips_html(
  [("Circle the command word.", "Write the marks beside it."),
   ("One point per mark.", "Two points with reasons for 4 marks."),
   ("Use the scenario.", "Name the device, user or system."),
   ("Both sides in a comparison.", "'whereas' joins them."),
   ("Say why or how.", "So, because, which means, this allows."),
   ("Use the technical term.", "Less storage space, less bandwidth, non-volatile."),
   ("Do not repeat the question.", "Add the reason it leaves out.")],
  [("Explaining a benefit", "It reduces the storage space needed, which means the watch can stay small."),
   ("Comparing", "Binary uses only 0 and 1, whereas hexadecimal also uses A to F."),
   ("Linking to a scenario", "In the robot vacuum, the data gathered could be where obstacles are."),
   ("Explaining why an error is found", "The same algorithm is used on the same data, so a different value means the data has changed."),
   ("Naming and describing", "An IDE has error diagnostics, which show where the errors are in the program.")],
  [("Identify", "Name, select or recognise. A word or a tick."), ("State", "Express in clear terms. One statement per mark."), ("Describe", "State the points and main features. What, not why."), ("Explain", "Give reasons: why and how, with a link word."), ("Outline", "Set out the main points. Name plus a short expansion."), ("Compare", "Similarities and differences, with both items in each point."), ("Suggest", "A proposal that fits the scenario, with a reason.")]) + FC

js = CHAINJS + PICKJS + '''
chainStep("#stA", "One topic, three command words", ["State: parallel transmission sends several bits at the same time", "Describe: add how, each bit on its own wire, in one or both directions", "Explain why: add the reason, so data arrives quickly over a short distance", "Context: the computers are in one room, so the bits stay in step"], [
  "<b>State:</b> one clear fact earns one mark.", "<b>Describe:</b> the features of the method. Still only <i>what</i>.", "<b>Explain:</b> every sentence now has a reason: so, because.", "<b>Context:</b> the scenario decides which reasons count."]);
chainStep("#stB", "Turning a vague answer into marks", ["Vague: 'It is faster'", "Technical: 'The file is transmitted in less time'", "Reason: 'because there are fewer bits to send'", "Context: 'so the report fits under the size limit for the email'"], [
  "<b>Vague:</b> the report says this level of answer is not enough.", "<b>Technical:</b> name what is faster and use the term.", "<b>Reason:</b> say why it is quicker.", "<b>Context:</b> link to this file and this email."]);
chainStep("#stC", "Adding the context", ["Generic: 'Machine learning is when a computer learns from data'", "Linked to the device: 'The vacuum gathers data about the room as it cleans'", "What it does with it: 'and adapts its own route'", "Result: 'so it avoids obstacles and cleans dirtier areas for longer'"], [
  "<b>Generic:</b> true, but it earns no marks in a how-could-X-use-it question.", "<b>Device:</b> now it is about the robot vacuum.", "<b>Adapts:</b> the key idea the mark scheme looks for.", "<b>Benefit:</b> the consequence that completes the point."]);

chooser("h", [
  ["Identify", "A name only", "'The device is a router'", "Explaining when only a name is asked wastes time", 1],
  ["State", "One clear statement per mark", "'Lossless'; 'It is…'", "Adding reasons earns nothing extra", 1],
  ["Define", "The exact meaning with the technical term", "'A text-based address for…'", "Vague wording such as 'an address for a website'", 2],
  ["Outline", "Name plus a short expansion", "'A double entry check: the data is entered twice and compared'", "A name with no expansion earns half", 2],
  ["Describe", "Features or steps: what, not why", "'The packet has a header, a payload and a trailer'", "Listing the contents of a header instead of the structure", 3],
  ["Explain", "A point and its reason", "'…so the data arrives sooner'", "Describing how it works instead of why it is chosen", 5],
  ["Compare", "Both items in each point", "'Binary… whereas hexadecimal…'", "A sentence about one item only", 3],
  ["Suggest", "A fitting answer with a reason", "'A touchscreen, because the watch is small'", "A generic device that does not suit the scenario", 4]
], (it) => `${it[0]}: it wants ${it[1].toLowerCase()}. Start like this: ${it[2]}. Trap: ${it[3].toLowerCase()}.`, "Detail needed");

pick("m", [
  { label: "A", a: "The data is stored on the internet.", m: 0, why: "This repeats what cloud storage is. The report for this question says many candidates repeated the definition instead of giving a benefit." },
  { label: "B", a: "It is better and easier to use.", m: 0, why: "Vague words with no technical term and no reason. No mark scheme point matches." },
  { label: "C", a: "You can get your data on a phone or a laptop.", m: 1, why: "Matches the point that the data can be accessed from other devices, but the consequence is missing." },
  { label: "D", a: "You can get your data on a phone or a laptop, so if the watch breaks or is lost the data is still there.", m: 2, why: "The point plus its consequence: two marks for one benefit. A second benefit is needed for the other two." },
  { label: "E", a: "The watch needs less storage, which keeps it small. The data can also be reached from other devices.", m: 3, why: "The first benefit is a point with its consequence (two marks). The second is a point without a consequence (one mark)." },
  { label: "F", a: "You can get your data on a phone or a laptop, so if the watch breaks or is lost the data is still there. The provider can add more storage on demand, so the watch will not run out of space.", m: 4, why: "Two benefits, each with a consequence that fits the watch: four marks." }
], (it) => `<blockquote style="margin:10px 0">${it.a}</blockquote>${scoreBar(it.m, 4)}<div class="verdict">${it.why}</div>`);

pick("x", [
  { label: "Robot vacuum", g: "Machine learning means the computer learns from data.", b: "The vacuum collects data about the room while it cleans, such as where furniture is and which areas are dirtier. It uses the data to adapt its route, so it avoids obstacles and spends longer on the dirty areas.", w: "Gathers data, adapts its own process, gives an example and a benefit: the pattern in the mark scheme for this question." },
  { label: "Plough", g: "Artificial intelligence is when a machine acts like a human.", b: "The plough gathers data about the field as it works, such as its shape and where obstacles are. It builds a map and chooses the most efficient route, so it makes fewer mistakes the next time.", w: "Every sentence is about the plough and its field. The mark scheme lists a map, the route and fewer mistakes as creditable." },
  { label: "Smart phone", g: "A mouse and a printer.", b: "A touchscreen to enter text and a microphone for calls as input; a screen and a speaker to show and play content as output.", w: "A mouse and a printer are not built into a phone. The examiner report records this exact error." },
  { label: "Smartwatch ROM", g: "ROM is primary storage that cannot be changed.", b: "The ROM stores the start-up instructions, such as the firmware, so the watch can start. It is non-volatile, so the instructions are kept when the battery is flat.", w: "Describes the role in this watch. The generic answer defines ROM but does not say what it does here." }
], (it) => `<div class="grid2"><div><small>Generic answer</small><p style="margin:4px 0">${it.g}</p></div><div><small>Tied to the scenario</small><p style="margin:4px 0">${it.b}</p></div></div><div class="verdict">${it.w}</div>`);

let mode = 2;
function mt() {
  const m = +$("#mk").value, pts = mode === 2 ? Math.ceil(m / 2) : m, mins = m * 1.4;
  $("#r1").textContent = pts + (mode === 2 ? " with reasons" : "");
  $("#r2").textContent = Lib.fmtN(mins, 1) + " min";
  $("#rv").textContent = mode === 2 ? `${m} marks for an explanation: about ${pts} point${pts > 1 ? "s" : ""}, each with the reason that goes with it, in roughly ${Lib.fmtN(mins, 1)} minutes.` : mode === 1 ? `${m} marks for a description: about ${m} separate features or steps, kept short, in roughly ${Lib.fmtN(mins, 1)} minutes.` : `${m} marks for stating: ${m} separate short statements or answers, in roughly ${Lib.fmtN(mins, 1)} minutes.`;
  $("#labA").innerHTML = SV.rect(40, 40, (pts / 8) * 340, 36, "f1", op(0.6)) + SV.text(40, 32, "Points", "sm") + SV.rect(40, 120, Math.min(1, mins / 11.2) * 340, 36, "f2", op(0.6)) + SV.text(40, 112, "Minutes (out of 11.2 for 8 marks)", "sm");
}
$("#g2").innerHTML = [["State or identify", 0], ["Describe", 1], ["Explain", 2]].map(([t, v]) => `<button class="b${v === 2 ? " pri" : ""}" data-v="${v}">${t}</button>`).join("");
$$("#g2 button").forEach((b) => (b.onclick = () => { mode = +b.dataset.v; $$("#g2 button").forEach((x) => x.classList.toggle("pri", x === b)); mt(); }));
Lib.slider($("#g1"), { id: "mk", label: "Marks for the question ", min: 1, max: 8, step: 1, value: 4, fmt: (v) => v, onInput: mt });
mt();
''' + CLASSIFY("cl1", "Is each answer a fact, a description or an explanation?", ["State (a fact)", "Describe (features)", "Explain (a reason)"],
  [("Lossless", 0), ("A text-based address for a web page", 0), ("The packet has a header, a payload and a trailer", 1), ("Each bit travels along its own wire and several bits are sent together", 1),
   ("Serial is more reliable over a long distance because the bits arrive in order", 2), ("It has no moving parts, so the data is less likely to be lost if the phone is dropped", 2),
   ("A check digit is recalculated after scanning and compared with the original", 1), ("The checksum is worked out from the data, so a different value means the data has changed", 2)],
  "State gives a fact, describe gives features, explain gives the reason.") + CLASSIFY("cl2", "Does the answer mention both sides?", ["One side only", "Both sides"],
  [("Hexadecimal uses letters", 0), ("Binary uses only 0 and 1 whereas hexadecimal also uses A to F", 1), ("Symmetric encryption uses one key", 0), ("Symmetric uses one key whereas asymmetric uses a public and a private key", 1),
   ("Serial sends bits one at a time", 0), ("Serial sends one bit at a time whereas parallel sends several at once", 1)],
  "In a difference, both items must appear in the same answer.") + ORDER(
  "Put the steps for answering an explain question in order.",
  ["Read the command word and the number of marks", "Underline the key term and the scenario", "Plan a point and a reason for each pair of marks", "Write each point with a link word such as so or because", "Check each pair uses a technical term and fits the scenario"],
  "Read, underline, plan, write, check.") + MATCH([
  ["Identify", "Name, select or recognise"], ["State", "Express in clear terms"], ["Describe", "State the points and main features of a topic"], ["Explain", "Set out reasons: say why and how"], ["Outline", "Set out the main points"], ["Compare", "Comment on similarities and/or differences"]]) + CALC([
  {"q": "Each paper has 75 marks in 105 minutes. How many minutes per mark?", "a": 1.4, "unit": "min", "tol": 0.05, "hint": "105 ÷ 75.", "sol": "<b>1.4 minutes</b>."},
  {"q": "At 1.4 minutes per mark, how many minutes for a 6-mark explanation?", "a": 8.4, "unit": "min", "tol": 0.1, "hint": "6 × 1.4.", "sol": "<b>8.4 minutes</b>."},
  {"q": "A mark scheme gives one mark for each method and one for a further description (max six). How many methods give full marks?", "a": 3, "unit": "", "tol": 0.01, "hint": "Each method is worth 2.", "sol": "<b>3</b> methods, each with a description."},
  {"q": "A 6-mark question allows a maximum of 4 marks for stating features. What is the least number of marks that must come from saying what the features do?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b> marks."},
  {"q": "An explain question awards marks for pairs of point and reason. How many pairs give 4 marks?", "a": 2, "unit": "", "tol": 0.01, "hint": "Each pair is worth 2.", "sol": "<b>2</b> pairs."}]) + MCQ([
  ("Which command word asks you to say why or how?", ["State", "Identify", "Explain", "Give"], 2, "Explain means set out reasons: say why and how."),
  ("A question asks for two differences between binary and hexadecimal. Which answer earns a mark?", ["Hexadecimal uses letters", "Binary uses only 0 and 1 whereas hexadecimal also uses A to F", "Binary is a number system", "Hexadecimal is longer"], 1, "A difference must refer to both."),
  ("The mark scheme says 'six from, maximum 4 for stating features'. What does that mean?", ["Four features and nothing else earn full marks", "Features alone earn at most 4; the rest need what each does", "Four features must be wrong", "Only four lines may be written"], 1, "Naming alone is capped."),
  ("Why is a mouse a poor answer to 'suggest an input device for a smart phone'?", ["It is expensive", "It is not built into a smart phone", "It is an output device", "It needs a battery"], 1, "Answers must fit the scenario."),
  ("What does the generic marking principle say about wrong statements?", ["Each loses a mark", "Marks are not deducted for errors", "They cancel a correct point", "They cap the answer at half marks"], 1, "Marks are awarded positively; errors are not deducted.")
], "qz1") + CARDS([
  ("Identify", "Name, select, recognise."), ("State", "Clear statement, one per mark."), ("Describe", "Points and features: what."), ("Explain", "Reasons: why and how."),
  ("Compare", "Both items in each point."), ("Pairs", "Point plus reason or description."), ("Context", "Use the device or scenario."), ("Link words", "So, because, which means, this allows.")])

build("cx1", "ig-cs-command-words", "Command Words and Mark Allocation: Answering What Is Asked", EYC,
  "How the command word and the mark tell you what to write, how to turn a description into an explanation, why technical terms and context matter, and fourteen real questions with what the mark scheme wanted.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
