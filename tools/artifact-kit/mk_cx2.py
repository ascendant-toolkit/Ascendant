"""IGCSE CS exam technique 2: Paper 1 Computer Systems. Run: python3 tools/artifact-kit/mk_cx2.py"""
from csk import *

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>Paper 1 is a <b>75-mark written paper in 1 hour 45 minutes</b> on Topics 1 to 6, made of short and structured questions that you answer on the question paper, with <b>no calculator</b>. About 60% of the marks are for knowledge (AO1) and about 20% each for applying it to a scenario (AO2) and for reasoned judgements (AO3), so most marks reward <b>precise technical facts</b>, and the rest reward <b>applying them to the device in the question</b>. The paper mixes one-mark recall with number work where you must <b>show the working</b>, diagrams where each labelled part earns a mark, and explain questions set in a scenario. The examiner reports keep naming the same causes of lost marks: vague wording, ignoring the context, and mixing up stages or devices. At 1.4 minutes a mark you have time to plan every answer, so aim to <b>earn every mark on the short questions</b> and then use the time on the 4-mark and 6-mark answers.</p></div>

  <h2>1 · The facts</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td><b>Paper</b></td><td>Paper 1 Computer Systems (variants 11 to 13 in the main series)</td></tr>
    <tr><td><b>Time and marks</b></td><td>1 hour 45 minutes (105 minutes), 75 marks, so 1.4 minutes per mark</td></tr>
    <tr><td><b>Content</b></td><td>Topics 1 to 6: data representation, data transmission, hardware, software, the internet and its uses, automated and emerging technologies</td></tr>
    <tr><td><b>Question types</b></td><td>Short answer and structured; all questions are compulsory</td></tr>
    <tr><td><b>Answering</b></td><td>On the question paper, in the space provided. If you use an extra page, say clearly which question it answers.</td></tr>
    <tr><td><b>Equipment</b></td><td>Black or dark blue pen; HB pencil for diagrams; no calculator</td></tr>
    <tr><td><b>Assessment objectives</b></td><td>Approximately AO1 knowledge 60%, AO2 application 20%, AO3 judgement 20% of the paper</td></tr>
    <tr><td><b>Brand names</b></td><td>No marks for brand names of software or hardware</td></tr>
  </table></div>

  <h2>2 · Where the 75 marks sit</h2>
  <p>This is Oct/Nov 2024 paper 11, with the marks added up from the published mark scheme. Other papers differ in the order but not in the mix.</p>
  <div class="tw"><table class="t">
    <tr><th>Q</th><th>Topic</th><th>Marks</th><th>What the marks reward</th></tr>
    <tr><td>1</td><td>Data representation: file size units, compression</td><td>6</td><td>Recall of units and types of compression, three benefits</td></tr>
    <tr><td>2</td><td>Hardware: smart phone input, output and storage</td><td>10</td><td>Devices that fit a phone; justify solid state storage</td></tr>
    <tr><td>3</td><td>Data representation: character sets, conversions, shift, addition</td><td>11</td><td>Accurate number work with working</td></tr>
    <tr><td>4</td><td>Data transmission: packets, parallel full-duplex</td><td>11</td><td>Describe the packet; explain why a method suits the scenario</td></tr>
    <tr><td>5</td><td>Hardware: fetch-decode-execute, registers, buses, clock speed</td><td>11</td><td>What happens at each stage; effect of a faster clock</td></tr>
    <tr><td>6</td><td>Software: embedded systems, translators, assembly, IDE</td><td>10</td><td>Six marks for how an IDE helps</td></tr>
    <tr><td>7</td><td>Software: operating system, firmware</td><td>4</td><td>Function and description</td></tr>
    <tr><td>8</td><td>Internet: blockchain diagram</td><td>4</td><td>Labelled diagram</td></tr>
    <tr><td>9</td><td>Emerging technology: AI components, machine learning</td><td>8</td><td>Complete a paragraph; name the ability</td></tr>
  </table></div>
  <p>The marks come in very different sizes. Questions worth one or two marks are quick to earn if the fact is exact, and the answers worth four, six or seven marks (the packet, parallel transmission, solid state storage, the IDE, blockchain) are where explaining and applying decide the total, so give them the time.</p>

  <h2>3 · Using the 105 minutes</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Marks</th><th>Time at 1.4 min a mark</th><th>What that buys</th></tr>
    <tr><td>1</td><td>1.4 minutes</td><td>Read, answer, move on</td></tr>
    <tr><td>2</td><td>2.8 minutes</td><td>Two points, or a name and a description</td></tr>
    <tr><td>4</td><td>5.6 minutes</td><td>Two points with reasons, or a labelled diagram</td></tr>
    <tr><td>6</td><td>8.4 minutes</td><td>Three pairs of feature and purpose, with time to check</td></tr>
  </table></div>
  <p>This is a guide, not a rule in the mark scheme. A sensible plan: about 85 minutes to work through the paper in order, answering everything, then about 15 to 20 minutes to return to anything you skipped and to check number work and diagrams. Leave a blank only until you come back to it.</p>

  <h2>4 · Question shapes and how to attack them</h2>
  <div class="tw"><table class="t">
    <tr><th>Shape</th><th>Example</th><th>How to attack it</th></tr>
    <tr><td><b>Tick or circle</b></td><td>Which is not a unit of file size? Circle three buses.</td><td>Read every option. For "circle three", you must circle exactly three. The reports say the common wrong answers were "central" and "execute" for buses.</td></tr>
    <tr><td><b>Complete the paragraph</b></td><td>Choose terms from a list; each may be used more than once</td><td>Read the whole paragraph first. Use only words from the list. A term can be reused when the question says so.</td></tr>
    <tr><td><b>Number work</b></td><td>Convert, add, shift, work out a file size</td><td>Show the working in the form asked. One mark is usually for working and one for the answer.</td></tr>
    <tr><td><b>Give or state a list</b></td><td>Give two registers used in the fetch stage</td><td>Exactly the number asked; accept the first two that you are sure of.</td></tr>
    <tr><td><b>Describe a process</b></td><td>What happens at the decode stage?</td><td>Steps in order, with the register or bus named in each.</td></tr>
    <tr><td><b>Draw and annotate</b></td><td>DNS lookup, blockchain, decode stage</td><td>Boxes, arrows and a label on every arrow. Each correct part is a mark.</td></tr>
    <tr><td><b>Explain in a scenario</b></td><td>Why is serial simplex suitable for this stock system?</td><td>Reason plus context. Use the command-word habits from the first review in this section.</td></tr>
    <tr><td><b>Suggest and justify</b></td><td>Choose a storage device for a smart phone and justify it</td><td>Name it (1), then reasons with consequences.</td></tr>
  </table></div>

  <h2>5 · Show the working</h2>
  <p>Paper 1 has no calculator, and many number questions award separate marks for working. The syllabus says calculations use 1024, not 1000, and that answers must be in the units asked for.</p>
  <div class="tw"><table class="t">
    <tr><th>Skill</th><th>What earns the working mark</th><th>What goes wrong</th></tr>
    <tr><td><b>Binary addition</b></td><td>The carries shown, then each nibble correct, and for overflow: a 9th bit or a statement that the result is too big for 8 bits</td><td>The reports say candidates who converted to denary, added and converted back did not show binary addition and lost the working mark</td></tr>
    <tr><td><b>Denary to binary</b></td><td>Working such as 128 + 32 + 8 + 4 + 2 + 1</td><td>Writing the answer with nothing else</td></tr>
    <tr><td><b>Binary or denary to hexadecimal</b></td><td>Split into nibbles, convert each</td><td>Reading the whole byte as one number</td></tr>
    <tr><td><b>Logical shift</b></td><td>Each bit moves; the end bit is lost; a 0 is added at the other end. Left shift multiplies, right shift divides</td><td>"The value is increased" or "changed" is too vague for the effect</td></tr>
    <tr><td><b>Two's complement</b></td><td>"Flip and add" working, then the sign</td><td>Reading a two's complement pattern as an ordinary positive number</td></tr>
    <tr><td><b>File size</b></td><td>Bits = (image) pixels × colour depth, or (sound) sample rate × resolution × seconds; ÷ 8 for bytes; ÷ 1024 for each larger unit</td><td>Dividing by 1000, or stopping at bits when the question asks for KiB</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>The mark scheme for a three-mark conversion question commonly splits into two marks for stages of working and one for the answer. A correct answer with no working may still earn full marks, but a wrong answer with working keeps marks. Always write the working.</div>

  <h2>6 · Diagrams: what each correct part earns</h2>
  <div class="tw"><table class="t">
    <tr><th>Diagram</th><th>Parts that each earn a mark</th></tr>
    <tr><td><b>Decode stage of the FDE cycle</b> (4)</td><td>The instruction goes from the MDR to the CIR/control unit; it travels along the data bus; the CIR is part of the control unit; the instruction is split into opcode and operand; the control unit decodes it using the instruction set</td></tr>
    <tr><td><b>Retrieving a web page</b> (5)</td><td>URL sent from the browser to the DNS; DNS finds the matching IP address (passing it to the next DNS if it cannot); IP address returned to the browser; request sent from the browser to the web server; web page sent back; browser renders the HTML</td></tr>
    <tr><td><b>Blockchain in a transaction</b> (4)</td><td>A digital ledger is used; the payment details are sent from the device to the ledger; the transaction is stored in a block with details such as a digital signature and time stamp; each block has a unique hash; the full block is added to the chain held on every device</td></tr>
  </table></div>
  <p>The reports say few candidates drew the decode stage correctly; many drew the fetch or the execute stage. Some candidates also showed the request for the web page going from the DNS to the web server, when the browser sends it after receiving the IP address.</p>

  <h2>7 · Misconceptions the examiners have flagged</h2>
  <div class="tw"><table class="t">
    <tr><th>Wrong idea</th><th>What is correct</th></tr>
    <tr><td>Secondary storage is only used when primary storage is full</td><td>It stores data and programs permanently, so they are still there each time the device is switched on</td></tr>
    <tr><td>The accumulator carries out calculations</td><td>It stores the interim result of a calculation; the ALU does the calculation</td></tr>
    <tr><td>Encryption stops data being stolen</td><td>It makes stolen data meaningless to the person who has it</td></tr>
    <tr><td>JPEG is a type of compression</td><td>JPEG is a file format. The two types are lossy and lossless</td></tr>
    <tr><td>Hexadecimal is for the benefit of the computer</td><td>It is a shorter representation of binary that is easier for people to read and write</td></tr>
    <tr><td>A hard disk drive is the best storage for a phone</td><td>Solid state suits it: small, light, no moving parts, fast, cool, quiet, low power</td></tr>
    <tr><td>The DNS sends the request for the page to the web server</td><td>The DNS returns the IP address to the browser, which sends the request</td></tr>
    <tr><td>Decode and execute are the same</td><td>Decode: the control unit splits the instruction into opcode and operand using the instruction set. Execute: the instruction is carried out</td></tr>
  </table></div>

  <h2>8 · Choosing a device and justifying it</h2>
  <p>Questions that set a device, such as a smart phone, a smartwatch or an automated plough, reward choices that fit it. For storage in a smart phone the mark scheme gives one mark for naming solid state, then three marks for reasons, each with its consequence:</p>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>Consequence for the phone</th></tr>
    <tr><td>Small and thin</td><td>It fits easily inside the phone</td></tr>
    <tr><td>Light</td><td>It does not make the phone heavy to carry</td></tr>
    <tr><td>No moving parts</td><td>Durable: the data is less likely to be lost if the phone is dropped</td></tr>
    <tr><td>Fast read and write</td><td>Files and software load quickly</td></tr>
    <tr><td>Runs cool and quiet</td><td>The phone does not get hot to hold, and does not spoil music or video with noise</td></tr>
    <tr><td>Low power</td><td>It does not drain the battery</td></tr>
  </table></div>

  <h2>9 · Common ways to lose marks</h2>
  <ul>
    <li><b>Confusing the stages</b> of the fetch-decode-execute cycle, or naming a stage instead of a register or bus.</li>
    <li><b>No working</b> on number questions, or converting to denary when binary addition was asked for.</li>
    <li><b>Vague wording</b>: "faster", "better", "more secure", with no technical term.</li>
    <li><b>Generic devices</b> in a scenario.</li>
    <li><b>Describing when asked to explain</b>, or listing when asked for a description of how it helps.</li>
    <li><b>Skipping the diagram</b>: each labelled part is a mark and a diagram can be built from memory with arrows and labels.</li>
    <li><b>Not reading "use only terms from the list"</b>.</li>
  </ul>
'''

watch = '''
  <h2>1 · The decode stage, step by step</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stA"></div>
  <h2>2 · Binary addition with the carries</h2>
  <div id="stB"></div>
  <h2>3 · A file size, with the working</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Binary addition with working</h2>
  <p>Choose a pair of 8-bit numbers to see the carries, the answer and whether it overflows.</p>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aO"></div></div>

  <h2>Lab 2 · Two's complement</h2>
  <p>Choose an 8-bit pattern. A pattern that starts with 1 is negative, so flip the bits and add 1 to find the size.</p>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>

  <h2>Lab 3 · File size working</h2>
  <p>Choose a file. The working goes in the order the mark scheme rewards: bits, bytes, then the unit asked for. The last line shows the answer you would get by dividing by 1000, which is the common error.</p>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>

  <h2>Lab 4 · Where the marks sit</h2>
  <p>Choose a question from Oct/Nov 2024 paper 11 to see its topic, its marks and the time that many marks deserve at 1.4 minutes a mark.</p>
  <div class="card"><div id="qB" class="btnrow"></div><div id="qO"></div></div>
'''

practise = '''
  <h2>1 · Does the device fit?</h2><div id="cl1" class="card"></div>
  <h2>2 · Misconception or correct?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the web page retrieval in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the register or part to its job</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '<p class="note">These come from the Principal Examiner Reports for Cambridge IGCSE Computer Science, which describe what candidates actually wrote. The wording is ours.</p>\n' + (
rw("Drawing fetch or execute instead of decode", "Oct/Nov 2024, papers 11 and 13: asked what happens at the decode stage, many candidates described or drew the execute stage, and some the fetch stage. The mark scheme looks for the instruction going from the MDR to the CIR, the split into opcode and operand, and the control unit decoding with the instruction set.", "FDE questions: write the name of the stage at the top of your answer and check every point belongs to it.") +
rw("Converting to denary to add", "Oct/Nov 2024, papers 11 and 13: asked to add two binary values, some candidates converted both to denary, added, and converted back. The report says they did not show the working as binary addition, which is where a mark is given.", "'add in binary' questions: write the numbers one above the other with a carries row.") +
rw("Reading two's complement as plain binary", "Oct/Nov 2024, paper 13: some candidates converted a two's complement value as though it were an ordinary positive binary number. The mark scheme gives a mark for working such as flip and add and a mark for the negative denary answer.", "if a question mentions two's complement, check the left-hand bit first.") +
rw("The wrong direction for the request", "Oct/Nov 2024, paper 12: some candidates drew the request for the web page going from the DNS to the web server. The DNS returns the IP address to the browser, and the browser then sends the request.", "diagram questions: put an arrow and a label on every step, and check the direction.") +
rw("The accumulator does not calculate", "Oct/Nov 2024, paper 12: a common misconception was that the accumulator carries out calculations. It stores the interim result of a calculation.", "CPU questions: link each register to what it stores, not to a process it does not perform.") +
rw("A hard disk drive in a phone", "Oct/Nov 2024, paper 11: the most common wrong answer for the most suitable storage in a smart phone was a hard disk drive. Solid state was accepted, with reasons such as small size, no moving parts and low power.", "'most suitable' questions: pick the item that fits the device, then say why.")
)

items = [("w24_11", "3(d)", 3), ("w24_13", "1(e)", 2), ("w24_12", "3(d)", 3), ("s24_12", "2(d)", 3), ("w24_12", "2(c)", 3), ("w24_11", "4(a)", 4), ("w24_12", "5(b)", 6),
         ("w24_11", "5(b)", 3), ("w24_11", "5(e)", 2), ("w24_13", "3(b)", 4), ("w24_12", "7(d)", 5), ("w24_11", "8", 4), ("w24_11", "2(c)", 6), ("w24_13", "5(b)", 3)]

exam = cs_exam("Paper 1 technique",
  "Fourteen Paper 1 questions covering the shapes in this review: number work with working, file sizes, describing a process, three diagrams, justifying a choice and explaining in a scenario. The figures and contexts are changed, and the answers have been recalculated; the mark scheme points are the ones the papers used.",
  crows(items), [
  ceq(CP("w24_11", "3(d)"), "[3]", "Add these two 8-bit binary integers and show your working as binary addition: 01010100 and 01110100.",
    ["One mark for working that shows binary addition, for example the carries", "One mark for each correct nibble: the answer is 11001000 (denary 84 + 116 = 200)", "The report says candidates who converted to denary, added and converted back did not show binary addition"],
    "<p>Write the numbers one above the other, add a carries row, and work from the right: 0+0, 0+0, 1+1 (0 carry 1), 0+0+1, 1+1 (0 carry 1), 0+1+1 (0 carry 1), 1+1+1 (1 carry 1), 0+0+1.</p>"),
  ceq(CP("w24_13", "1(e)"), "[2]", "The 8-bit two's complement binary integer 10011100 is stored. Convert it to a denary number and show your working.",
    ["One mark for correct working, for example flip the bits and add 1", "One mark for the correct denary number: 10011100 flips to 01100011, adding 1 gives 01100100 = 100, so the answer is −100", "The left-hand bit is 1, so the number is negative"],
    "<p>Check the left-hand bit. It is 1, so flip and add. Do not read 10011100 as 156.</p>"),
  ceq(CP("w24_12", "3(d)"), "[3]", "A logical left shift of one place is performed on the binary integer 00110101. (i) Describe the shift. (ii) State the effect on the value.",
    ["(i) Two from: each bit moves one place to the left; the most significant bit is lost; a 0 is added as the new least significant bit", "(ii) The value is multiplied by 2: 00110101 (53) becomes 01101010 (106)", "The report says answers such as 'it increases' were too vague"],
    "<p>Use the words moved, lost and added. For the effect, give the operation: multiplied by 2.</p>"),
  ceq(CP("s24_12", "2(d)"), "[3]", "A 24-bit colour image is 256 pixels wide and 128 pixels high. Calculate the file size in kibibytes (KiB). Show your working.",
    ["Up to two marks for stages of working, for example 256 × 128 = 32 768 pixels, then × 24 bits = 786 432 bits", "÷ 8 gives 98 304 bytes; ÷ 1024 gives the answer", "One mark for the correct answer: 96 KiB"],
    "<p>Pixels, then bits, then bytes, then KiB. Divide by 1024 for the last step, not 1000.</p>"),
  ceq(CP("w24_12", "2(c)"), "[3]", "A 16 second sound clip is recorded at a sample rate of 8192 Hz with a resolution of 16 bits. Calculate the file size in kibibytes (KiB). Show your working.",
    ["Up to two marks for stages of working: 8192 × 16 × 16 = 2 097 152 bits", "÷ 8 gives 262 144 bytes", "÷ 1024 gives the answer, one mark: 256 KiB"],
    "<p>Sample rate × resolution × seconds gives bits. Then ÷ 8, then ÷ 1024.</p>"),
  ceq(CP("w24_11", "4(a)"), "[4]", "An email is split into data packets. Describe the structure of a data packet.",
    ["Any four from: the packet has three sections", "A packet header, which contains data such as the destination address", "A payload, which contains the main data of the email", "A trailer, which contains data such as the error detection method"],
    "<p>The report says some candidates listed what goes in the header instead of describing the structure. Name the three sections, then say what each holds.</p>"),
  ceq(CP("w24_12", "5(b)"), "[6]", "A barcode scanner sends stock data to a stock control system using serial simplex transmission. (i) Explain how data is sent using serial simplex. (ii) Explain why serial simplex is appropriate here.",
    ["(i) Three: bits are sent one at a time; down a single wire; in one direction only", "(ii) Any three from: the stock system may be a long distance away, and serial is more reliable over distance", "The data does not need to arrive quickly, and only small amounts are sent, so the speed of parallel is not needed", "Bits arrive in order, so the data cannot be skewed, and there are fewer errors or less interference", "No reply is needed, so half- or full-duplex is not necessary"],
    "<p>Part (i) is how; part (ii) is why. Put the stock system and the one-way data into the reasons.</p>"),
  ceq(CP("w24_11", "5(b)"), "[3]", "Describe what happens at the decode stage of the fetch-decode-execute cycle.",
    ["Any three from: the control unit or CIR receives the instruction from the MDR, using the data bus", "The instruction is split into opcode and operand", "The control unit decodes the instruction using the instruction set"],
    "<p>The report says many candidates described the execute stage. Start with 'The instruction goes from the MDR to the CIR', and stay at the decode stage.</p>"),
  ceq(CP("w24_11", "5(e)"), "[2]", "A user changes their dual core CPU with a clock speed of 2.0 GHz to a dual core CPU with a clock speed of 3.0 GHz. Explain the effect on the performance of the CPU.",
    ["It can now carry out more instructions, or more fetch-decode-execute cycles, each second", "So the performance of the CPU increases"],
    "<p>The report says few gave a technically correct reason. Say what changes (more instructions per second) and the result (performance rises). Name the direction.</p>"),
  ceq(CP("w24_13", "3(b)"), "[4]", "Draw a labelled diagram to show what happens at the decode stage of the fetch-decode-execute cycle.",
    ["The instruction or data is sent from the MDR to the CIR or control unit, using the data bus", "The CIR is shown as part of the control unit", "The instruction is separated into operand and opcode", "The control unit decodes the instruction using the instruction set"],
    "<p>Draw MDR → (data bus) → CIR inside the CU, then a box that splits into opcode and operand, with the instruction set labelled. Each labelled part is a mark.</p>"),
  ceq(CP("w24_12", "7(d)"), "[5]", "Draw and annotate a diagram to show how a web page is found and retrieved when a user enters a URL into a browser.",
    ["The URL is sent from the browser to the DNS", "The DNS finds the matching IP address, passing the URL to the next DNS if it is not found", "The IP address is returned to the browser", "The request for the page is sent from the browser to the web server", "The web page or HTML files are sent back to the browser, which renders the HTML"],
    "<p>Three boxes (browser, DNS, web server) and arrows labelled in order. The report says some candidates sent the request from the DNS to the server.</p>"),
  ceq(CP("w24_11", "8"), "[4]", "Draw and annotate a diagram to show how blockchain is used when a customer pays for goods online.",
    ["A digital ledger is used and the customer's device sends the payment data to it, encrypted", "The payment is recorded, with details such as digital signature, time and date", "The transaction is stored in a block, and a block can hold several transactions", "Each block has a block hash or unique identifier", "When the block is full it is added to the blockchain held on every device"],
    "<p>The report says very few candidates drew this correctly. Label the device, the ledger, a block with its hash, and the chain on every device.</p>"),
  ceq(CP("w24_11", "2(c)"), "[6]", "A smart phone has primary and secondary storage. (i) Explain the purpose of the secondary storage. (ii) Name the most suitable type of secondary storage for the phone and justify your choice.",
    ["(i) Two from: to store data and files permanently, so they do not have to be entered or installed each time the phone is switched on", "To let software be downloaded and installed, or to store the user's files, or to create virtual memory", "(ii) One mark for solid state, then three from: small, so it fits in the phone; light; no moving parts, so durable if dropped", "Fast read and write, so files load quickly; runs cool; quiet; low power, so it does not drain the battery"],
    "<p>The report says some thought secondary storage was only used when primary storage is full. For (ii) the common wrong answer was a hard disk drive. Name solid state, then give reasons with consequences.</p>"),
  ceq(CP("w24_13", "5(b)"), "[3]", "An automated irrigation system uses a microprocessor. Describe the role of the microprocessor in the system.",
    ["It receives data from the sensors", "It analyses the data, for example by checking whether it is within or outside a range", "It sends signals to trigger actions based on the data"],
    "<p>Only the role of the microprocessor is asked for. The report says some candidates described the whole system.</p>"),
])

tips = tips_html(
  [("Show the working.", "Binary addition with carries, flip and add, bits then bytes then KiB."),
   ("Use 1024, not 1000.", "For every file size unit."),
   ("Name the stage.", "Decode, not fetch or execute."),
   ("Arrows and labels.", "Every part of a diagram is a mark."),
   ("Fit the device.", "Phone: touchscreen, SSD. Not a mouse or an HDD."),
   ("Say which way it changes.", "More instructions per second, not 'faster'."),
   ("Read 'use only terms from the list'.", "And note if terms can be reused.")],
  [("Binary addition", "I wrote the carries above each column and added from the right."),
   ("Logical shift", "Each bit moves one place left, the left-hand bit is lost, a 0 is added, so the value is multiplied by 2."),
   ("Two's complement", "The left-hand bit is 1, so I flipped the bits, added 1 and made the result negative."),
   ("Justifying a device", "Solid state has no moving parts, so the data is less likely to be lost if the phone is dropped."),
   ("File size", "Bits divided by 8 gives bytes, and bytes divided by 1024 gives KiB.")],
  [("Identify", "Name or select."), ("State", "A clear statement."), ("Describe", "Features or steps, in order."), ("Explain", "Reasons: why and how."), ("Calculate", "Work out, with working."), ("Draw", "A labelled diagram: each part is a mark.")]) + FC

js = CHAINJS + PICKJS + '''
$("#pic1").innerHTML = (() => {
  const B = [["Work in order", "about 85 min", "Answer every question; short ones first", 20, "f2", 400], ["Return and check", "15 to 20 min", "Skipped questions, number work, diagrams", 440, "f1", 180], ["Buffer", "to 105", "Extra pages labelled", 640, "f3", 100]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d.length > 34 ? d.slice(0, 34) + "…" : d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Suggested plan for the 105 minutes of Paper 1">${o}</svg>`;
})();
chainStep("#stA", "The decode stage", ["The instruction is held in the MDR after the fetch stage", "It is sent along the data bus to the CIR, which is part of the control unit", "The instruction is split into the opcode and the operand", "The control unit decodes it using the instruction set"], [
  "<b>Start:</b> fetch has finished; the instruction is in the MDR.", "<b>Transfer:</b> MDR to CIR along the data bus.", "<b>Split:</b> the opcode says what to do; the operand says what to do it to.", "<b>Decode:</b> the control unit uses the instruction set. Then execute begins."]);
chainStep("#stB", "Adding 01010100 and 01110100", ["Write the numbers one above the other and add a row for the carries", "Right to left: 0+0=0, 0+0=0, then 1+1=0 carry 1", "0+0+1=1, then 1+1=0 carry 1, then 0+1+1=0 carry 1", "1+1+1=1 carry 1, then 0+0+1=1: the answer is 11001000 (200)"], [
  "<b>Layout:</b> the carries row is where the working mark is earned.", "<b>First columns:</b> the first carry appears in the third column.", "<b>Middle columns:</b> carries keep moving left.", "<b>Check:</b> 84 + 116 = 200 and 11001000 is 200. No overflow, because there is no carry out of the last column."]);
chainStep("#stC", "A sound file: 10 s, 22 016 Hz, 8 bits", ["Bits = sample rate × resolution × seconds", "22 016 × 8 × 10 = 1 761 280 bits", "Bytes = bits ÷ 8 = 220 160 bytes", "KiB = bytes ÷ 1024 = 215 KiB"], [
  "<b>Formula:</b> write it first.", "<b>Substitute:</b> the first working mark.", "<b>Bytes:</b> divide by 8.", "<b>Unit asked:</b> divide by 1024 to get 215 KiB. One mark for the answer."]);

const bin = (n) => n.toString(2).padStart(8, "0");
pick("a", [[84, 116], [155, 100], [15, 15], [170, 85], [200, 100]].map(([x, y]) => ({ label: bin(x) + " + " + bin(y), x, y })), (it) => {
  const A = bin(it.x), B = bin(it.y); let c = 0, s = "", cr = "";
  for (let i = 7; i >= 0; i--) { const t = +A[i] + +B[i] + c; s = (t & 1) + s; cr = (c ? "1" : "·") + cr; c = t >> 1; }
  const sp = (t) => t.split("").join("  "), tot = it.x + it.y;
  return `<div class="formula" style="white-space:pre;overflow-x:auto">carries   ${sp(cr)}\\n          ${sp(A)}\\n        + ${sp(B)}\\n        ──────────────────────\\n    =   ${sp(s)}${c ? "  (carry out 1)" : ""}</div><p>${it.x} + ${it.y} = ${tot}. ${c ? "<b>Overflow:</b> the result is greater than 255, so it does not fit in 8 bits. The ninth bit is lost, and the error is called overflow." : "No carry out of the left-hand column, so there is no overflow."} The mark scheme gives a mark for the carries and a mark for each correct nibble.</p>`;
});

pick("t", [0b10011100, 0b11110001, 0b10000000, 0b01111111, 0b11111111].map((v) => ({ label: bin(v), v })), (it) => {
  const b = bin(it.v), neg = b[0] === "1", flip = b.split("").map((x) => (x === "1" ? "0" : "1")).join(""), mag = (parseInt(flip, 2) + 1) & 255 || 128;
  return neg
    ? `<div class="formula" style="white-space:pre;overflow-x:auto">pattern   ${b}   left-hand bit = 1: negative\\nflip      ${flip}\\nadd 1     ${bin((parseInt(flip, 2) + 1) & 255)}   = ${mag}\\nanswer    −${mag}</div><p>Trap: read as an ordinary unsigned number, ${b} would be ${it.v}. The mark scheme gives a mark for the flip-and-add working and a mark for the correct negative answer.</p>`
    : `<div class="formula" style="white-space:pre;overflow-x:auto">pattern   ${b}   left-hand bit = 0: positive\\nanswer    ${it.v}</div><p>A left-hand bit of 0 means the number is positive and is read as normal binary.</p>`;
});

const KB = (n) => (n % 1 ? n.toFixed(2) : n);
pick("f", [
  { label: "Image 256 × 128, 24-bit", kind: "image", w: 256, h: 128, d: 24 },
  { label: "Image 512 × 512, 16-bit", kind: "image", w: 512, h: 512, d: 16 },
  { label: "Sound 16 s, 8192 Hz, 16-bit", kind: "sound", r: 8192, d: 16, t: 16 },
  { label: "Sound 10 s, 22 016 Hz, 8-bit", kind: "sound", r: 22016, d: 8, t: 10 }
], (it) => {
  const bitsN = it.kind === "image" ? it.w * it.h * it.d : it.r * it.d * it.t, by = bitsN / 8, kib = by / 1024, wrong = by / 1000, f = (n) => n.toLocaleString("en-GB").replace(/,/g, " ");
  const l1 = it.kind === "image" ? `bits = width × height × colour depth = ${it.w} × ${it.h} × ${it.d} = ${f(bitsN)}` : `bits = sample rate × resolution × seconds = ${f(it.r)} × ${it.d} × ${it.t} = ${f(bitsN)}`;
  return `<div class="formula" style="white-space:pre-wrap">${l1}\\nbytes = bits ÷ 8 = ${f(by)}\\nKiB = bytes ÷ 1024 = ${KB(kib)}</div><p>Common error: dividing by 1000 gives ${KB(wrong)}, which is not ${KB(kib)}. The syllabus says calculations use 1024. Marks: up to two for the stages of working and one for the answer in the unit asked.</p>`;
});

const QS = [
  ["Q1", "Data representation: units and compression", 6, "A tick, two types of compression, three benefits"],
  ["Q2", "Hardware: smart phone devices and storage", 10, "Input, output, purpose of secondary storage, justify a choice"],
  ["Q3", "Data representation: conversions, shift, addition", 11, "Number work with working"],
  ["Q4", "Data transmission: packets and methods", 11, "Describe the packet; explain why a method is chosen"],
  ["Q5", "Hardware: fetch-decode-execute", 11, "Registers, decode stage, buses, clock speed"],
  ["Q6", "Software: embedded system, assembly, IDE", 10, "Six marks for how an IDE helps"],
  ["Q7", "Software: operating system and firmware", 4, "Function and description"],
  ["Q8", "Internet: blockchain", 4, "A labelled diagram"],
  ["Q9", "Emerging technology: AI", 8, "Complete a paragraph; name machine learning"]
].map(([label, topic, m, what]) => ({ label, topic, m, what }));
pick("q", QS, (it) => `<p><b>${it.topic}</b></p>${scoreBar(it.m, 11)}<p>${it.what}. At 1.4 minutes a mark this question deserves about <b>${Lib.fmtN(it.m * 1.4, 1)} minutes</b>. It is ${Lib.fmtN((it.m / 75) * 100, 0)}% of the paper.</p>`);
''' + CLASSIFY("cl1", "Does the device fit a smart phone or smartwatch?", ["Fits", "Does not fit"],
  [("Touchscreen", 0), ("Microphone", 0), ("Digital camera", 0), ("Screen", 0), ("Speaker", 0), ("Mouse", 1), ("Printer", 1), ("Full-size keyboard", 1), ("Plotter", 1)],
  "A device must be one that could feasibly be built into the product.") + CLASSIFY("cl2", "Is the statement correct or a misconception?", ["Correct", "Misconception"],
  [("Encryption makes stolen data meaningless to the thief", 0), ("Encryption stops data being stolen", 1), ("The accumulator stores the interim result of a calculation", 0), ("The accumulator carries out calculations", 1),
   ("Lossy and lossless are the two types of compression", 0), ("JPEG is a type of compression", 1), ("The browser sends the page request to the web server after the DNS returns the IP address", 0), ("The DNS sends the page request to the web server", 1),
   ("Secondary storage keeps data when the device is switched off", 0), ("Secondary storage is only used when primary storage is full", 1)],
  "Each wrong idea is one the examiners have recorded.") + ORDER(
  "Put the retrieval of a web page in order.",
  ["The user enters the URL in the web browser", "The browser sends the URL to the DNS", "The DNS finds the matching IP address", "The IP address is returned to the browser", "The browser sends a request to the web server", "The web server sends the web page back", "The browser renders the HTML"],
  "URL, DNS, IP address, request, page, render.") + MATCH([
  ["Program counter", "Stores the address of the next instruction to be fetched"], ["Accumulator", "Stores the interim result of a calculation"], ["Memory data register", "Holds the data or instruction just fetched from memory"],
  ["Control unit", "Decodes instructions and sends signals to manage the flow of data"], ["Instruction set", "A list of all the commands the processor can carry out"], ["Opcode", "The part of an instruction that says what to do"]]) + CALC([
  {"q": "Add 01010100 and 01110100. Give the answer in denary.", "a": 200, "unit": "", "tol": 0.01, "hint": "84 + 116.", "sol": "<b>200</b> (11001000)."},
  {"q": "A logical left shift of 2 places is performed on 00001111. Give the answer in denary.", "a": 60, "unit": "", "tol": 0.01, "hint": "00111100.", "sol": "<b>60</b>: 15 multiplied by 4."},
  {"q": "A 16-bit colour image is 512 pixels wide and 512 pixels high. What is its file size in KiB?", "a": 512, "unit": "KiB", "tol": 0.01, "hint": "512 × 512 × 16 ÷ 8 ÷ 1024.", "sol": "<b>512 KiB</b>."},
  {"q": "A sound file is 10 seconds at 22 016 Hz with 8-bit samples. What is its size in KiB?", "a": 215, "unit": "KiB", "tol": 0.5, "hint": "22 016 × 8 × 10 ÷ 8 ÷ 1024.", "sol": "<b>215 KiB</b>."},
  {"q": "The 8-bit two's complement pattern 11110001 is stored. What is its denary value?", "a": -15, "unit": "", "tol": 0.01, "hint": "Flip to 00001110, add 1.", "sol": "<b>−15</b>."}]) + MCQ([
  ("Which of these is a mistake candidates make about the accumulator?", ["It stores the interim result of a calculation", "It carries out calculations", "It is a register", "It is in the CPU"], 1, "The ALU calculates; the accumulator stores the result."),
  ("A question asks you to add two binary numbers. What gets the working mark?", ["Converting to denary", "Showing the carries in a binary addition", "Writing only the answer", "Drawing a circuit"], 1, "The working mark is for binary addition."),
  ("Which is the best storage device for a smart phone?", ["Hard disk drive", "Solid state", "Magnetic tape", "Optical disc"], 1, "Small, light, no moving parts, low power."),
  ("In the web page retrieval, what does the DNS return to the browser?", ["The web page", "The IP address", "The URL", "The HTML"], 1, "The DNS returns the IP address. The browser then sends the request."),
  ("What does the syllabus say to use when calculating file sizes?", ["1000", "1024", "1048", "Either"], 1, "Calculations must use 1024, not 1000.")
], "qz1") + CARDS([
  ("Paper 1", "75 marks, 105 minutes, no calculator."), ("1.4 minutes", "Per mark."), ("Binary addition", "Carries row; overflow above 255."), ("Two's complement", "Left bit 1: flip, add 1, negative."),
  ("File size", "Bits ÷ 8 ÷ 1024."), ("Decode", "MDR → CIR, opcode and operand, instruction set."), ("DNS", "URL → IP address → browser → request → page."), ("Phone storage", "Solid state: small, light, no moving parts.")])

build("cx2", "ig-cs-paper1-technique", "Paper 1 Computer Systems: Technique and Practice", EYC,
  "How Paper 1 is built and marked, a plan for the 105 minutes, how to show working in number questions, what each diagram part earns, the misconceptions examiners flag, and fourteen real questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
