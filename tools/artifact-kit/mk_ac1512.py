"""A Level CS syllabus 15.1.2: computer architectures (SISD, SIMD, MISD, MIMD) and massively parallel computers. Run: python3 tools/artifact-kit/mk_ac1512.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Computer architectures are classified by how many <b>instruction streams</b> and how many <b>data streams</b> they handle at once. <b>SISD</b> (single instruction, single data) is an ordinary sequential computer with one processor. <b>SIMD</b> (single instruction, multiple data) applies the <b>same</b> instruction to many data items at the same time, and <b>MISD</b> (multiple instruction, single data) applies <b>different</b> instructions to the <b>same</b> data stream. <b>MIMD</b> (multiple instruction, multiple data) has many processors, each running its own instructions on its own data, independently. A <b>massively parallel computer</b> links together a very large number of processors or separate computers, each working on its own part of one problem at the same time, and they communicate over a network by passing messages.</p></div>

  <h2>1 · The four categories</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Single data stream</th><th>Multiple data streams</th></tr>
    <tr><td><b>Single instruction stream</b></td><td><b>SISD</b>: one processor does one instruction at a time on one piece of data</td><td><b>SIMD</b>: the same instruction is performed on many data items at once</td></tr>
    <tr><td><b>Multiple instruction streams</b></td><td><b>MISD</b>: different instructions are performed on the same data</td><td><b>MIMD</b>: different instructions on different data, at the same time</td></tr>
  </table></div>

  <h3>SISD: Single Instruction, Single Data</h3>
  <ul>
    <li>Data is taken from a <b>single source</b> and a <b>single instruction</b> is performed on it at a time.</li>
    <li>It has <b>one processor</b>, a control unit and a memory unit, and executes instructions <b>sequentially</b>.</li>
    <li>The traditional (von Neumann) computer, such as a basic single-core processor.</li>
  </ul>
  <h3>SIMD: Single Instruction, Multiple Data</h3>
  <ul>
    <li>The <b>same operation</b> is performed on <b>multiple different data</b> streams simultaneously.</li>
    <li>A parallel computer with <b>multiple (array) processors</b> that execute the <b>same instruction</b> using <b>different</b> data sets.</li>
    <li>Example: changing the brightness of every pixel in an image; graphics processors.</li>
  </ul>
  <h3>MISD: Multiple Instruction, Single Data</h3>
  <ul>
    <li><b>Different operations</b> are performed on the <b>same</b> data stream.</li>
    <li>Each processor works on the <b>same data</b> independently, using different instructions. Parallel computers with <b>multiple processors</b>.</li>
    <li>Rare in practice. Example: several different checks on the same data in fault-tolerant systems.</li>
  </ul>
  <h3>MIMD: Multiple Instruction, Multiple Data</h3>
  <ul>
    <li>At any time any processor can execute <b>different instructions</b> on <b>different sets of data</b>.</li>
    <li>Contains <b>many processors</b> that operate <b>asynchronously and independently</b>.</li>
    <li>Example: a multi-core processor running several programs, a cluster of computers.</li>
  </ul>

  <h2>2 · Massively parallel computers</h2>
  <p>A <b>massively parallel</b> computer links together <b>very many</b> processors (thousands or more) or separate computers.</p>
  <ul>
    <li>A <b>large number of processors / computers connected together</b> to form a more powerful "single machine".</li>
    <li>They work <b>simultaneously on the same problem</b>, a set of <b>coordinated computations</b>, with <b>each processor responsible for its own part</b> of the problem.</li>
    <li>They need a <b>network infrastructure</b> (interconnected data pathways) and <b>communicate by sending messages</b> (a message interface), or through shared pools of memory.</li>
  </ul>
  <p>Used for problems that can be split into many independent parts: weather forecasting, simulations of molecules, searching enormous databases, training large AI models.</p>
  <div class="tw"><table class="t">
    <tr><th>Benefit</th><th>Limitation</th></tr>
    <tr><td>Very large problems are solved far faster because the work is shared</td><td>The problem must be split into parts that can run at the same time</td></tr>
    <tr><td>More processors can be added to increase power</td><td>Processors spend time communicating, which can slow things down; the network is costly and complex</td></tr>
  </table></div>

  <h2>3 · Common ways to lose marks</h2>
  <ul>
    <li>Expanding the acronym and nothing more. The question asks for the <b>features</b>: how many processors, what they do and to which data.</li>
    <li>Mixing up SIMD and MISD: in <b>SIMD</b> the <b>instruction</b> is the same and the data differ; in <b>MISD</b> the <b>data</b> is the same and the instructions differ.</li>
    <li>Describing MIMD without saying the processors work <b>independently / asynchronously</b>.</li>
    <li>Describing a massively parallel computer as "one very fast processor". It is <b>many</b> processors linked together, communicating by messages.</li>
    <li>Saying SISD is "slow". It is sequential: one instruction at a time on one data item.</li>
  </ul>
'''

watch = '''
  <h2>1 · The four architectures</h2>
  <p>Press Play, or click the steps. Boxes are processors; the left arrows are instructions, the right arrows are data.</p>
  <div id="stA"></div>
  <h2>2 · A massively parallel computer shares one problem</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Classify the architecture</h2>
  <p>Choose the number of instruction streams and data streams to see the architecture.</p>
  <div class="card"><div id="aI" class="btnrow"></div><div id="aD" class="btnrow"></div><div id="aO"></div></div>

  <h2>Lab 2 · How much faster with more processors?</h2>
  <p>A job of 1200 equal tasks is shared between processors working at the same time. Each task takes 1 second. Slide the number of processors; add a communication cost to see why speed-up is not perfect.</p>
  <div class="card"><div id="sP"></div><div id="sC"></div><div class="readout"><div><small>Time with one processor</small><strong id="s1"></strong></div><div><small>Time with this many</small><strong id="s2"></strong></div><div><small>Speed-up</small><strong id="s3"></strong></div></div></div>

  <h2>Lab 3 · The architectures compared</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Which architecture?</h2><div id="cl1" class="card"></div>
  <h2>2 · SIMD or MISD?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of solving a problem on a massively parallel computer in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Counting streams</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A graphics card (SIMD)", "To brighten an image the same instruction, add 20 to the brightness, is applied to millions of pixels at once. A graphics processor has many simple processors doing the same operation on different data.", "SIMD: the same instruction on many data items simultaneously.") +
rw("A multi-core phone (MIMD)", "While one core plays music another handles the screen and another the network. Each core runs different instructions on different data, independently.", "MIMD: many processors, different instructions, different data, asynchronously.") +
rw("A basic microcontroller (SISD)", "A very simple controller in a toy or alarm has one processor that runs one instruction at a time on one piece of data.", "SISD: one processor, sequential execution.") +
rw("A weather forecast on a supercomputer", "The atmosphere is divided into millions of boxes. Each of thousands of processors works out the weather for its own boxes at the same time and passes messages to its neighbours.", "massively parallel: many processors, each doing its part, communicating by messages.") +
rw("Error checking in a flight system (MISD)", "Several different programs check the same sensor data independently, and their answers are compared. This is a rare use of MISD.", "MISD: different instructions on the same data stream.")
)

where = [
  ("M/J 2022", "32", "5", "6", "Identify the three other architectures and describe each"),
  ("M/J 2023", "31, 33", "8", "3", "Outline the characteristics of massively parallel computers"),
  ("O/N 2023", "31, 33", "5", "4", "Describe the features of SISD and MIMD"),
  ("O/N 2023", "32", "10", "4", "Describe the features of SIMD and MISD"),
  ("M/J 2026", "33", "4", "3 + 2", "Characteristics of massively parallel computers; a difference and a similarity between SIMD and MISD")]

past = '''  <p class="note">Computer architectures are tested in Paper 3 in May/June 2022, May/June and Oct/Nov 2023 and May/June 2026. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>The four categories</h3>
''' + peq(SRC("s22", "32", "Q5"), "6 marks", "Identify / Describe",
  "There are four basic categories of computer architecture. Single Instruction Single Data (SISD) is one architecture. Identify the three other categories of computer architecture. Describe each category that you identify.",
  "SIMD, MISD and MIMD, each with a mark for the name and a mark for the description.",
  "<p>" + mks(["SIMD", "many / array processors execute the same instruction using different data sets"]) + " " + mks(["MISD", "many processors, using different instructions, use the same data set"], "a") + " " + mks(["MIMD", "many processors, using different instructions, use different data sets"]) + "</p>", "Describing SIMD as 'different instructions'. SIMD has one instruction applied to many data items.") + peq(SRC("w23", "31, 33", "Q5"), "4 marks", "Describe",
  "Describe the features of SISD and MIMD computer architectures.",
  "Two marks for each.",
  "<p>SISD (max 2): " + mks(["Single instruction, single data: data from a single source with a single instruction performed on it", "contains one processor, a control unit and a memory unit", "that executes instructions sequentially"]) + " MIMD (max 2): " + mks(["Multiple instruction, multiple data: at any time any processor can execute different instructions on different sets of data", "contains many processors", "that operate asynchronously / independently"], "a") + "</p>", None) + peq(SRC("w23", "32", "Q10"), "4 marks", "Describe",
  "Describe the features of the SIMD and MISD computer architectures.",
  "Two marks for each.",
  "<p>SIMD (max 2): " + mks(["Single instruction, multiple data: performs the same operation on multiple different data streams simultaneously", "the instructions can be performed sequentially, taking advantage of pipelining", "parallel computers with multiple processors"]) + " MISD (max 2): " + mks(["Multiple instruction, single data: performs different operations on the same data stream", "each processor works on the same data stream independently", "parallel computers with multiple processors"], "a") + "</p>", None) + peq(SRC("s26", "33", "Q4(b)"), "2 marks", "State",
  "State one difference and one similarity between the SIMD and MISD computer architectures.",
  "Both must be named in each answer. The difference: what is the same and what changes.",
  "<p>Difference (one): " + mks(["SIMD systems all execute the same instruction, whereas MISD systems perform different instructions", "SIMD systems work on many data streams simultaneously, whereas MISD systems all work on the same data source"]) + " Similarity (one): " + mks(["Both are parallel systems", "Both use multiple processors"], "a") + "</p>", "Writing only what SIMD does. A difference must mention both SIMD and MISD.") + '''
  <h3>Massively parallel computers</h3>
''' + peq(SRC("s23", "31, 33", "Q8"), "3 marks", "Outline",
  "Outline the characteristics of massively parallel computers.",
  "Many processors, working together on one problem, connected by a network and passing messages.",
  "<p>Any three: " + mks(["A large number of computer processors / separate computers connected together", "simultaneously performing a set of coordinated computations (collaborative processing)", "network infrastructure", "communicating by sending messages / using a message interface"]) + "</p>", None) + peq(SRC("s26", "33", "Q4(a)"), "3 marks", "Describe",
  "Describe the characteristics of massively parallel computers.",
  "Three of the five points.",
  "<p>Any three: " + mks(["The linking together of many (thousands of) processors / computers", "to form a more powerful 'single machine'", "All the processors work simultaneously on the same problem", "with each processor responsible for its own part of the problem", "communication is via interconnected data pathways / networks, or shared pools of memory"]) + "</p>", "Saying 'a very powerful single processor'. It is many processors linked together.")

review = req("2 marks", "Distinguish", "Distinguish between SISD and SIMD.", "How many data items are handled at once?",
  "<p>" + mks(["SISD has one processor that carries out one instruction at a time on one data item, sequentially.", "SIMD applies the same instruction to many data items at the same time, using several processors."]) + "</p>", None) + req("3 marks", "Explain", "Explain why a graphics processor suits SIMD.", "Think of pixels.",
  "<p>" + mks(["Operations such as changing brightness are the same for every pixel.", "The same instruction can be applied to many pixels (data items) at once.", "Many simple processors working at the same time finish the image much faster than one processor."]) + "</p>", None) + req("2 marks", "State", "State two features of a MIMD computer.", "Instructions, data, timing.",
  "<p>" + mks(["It has many processors, each able to execute different instructions on different data.", "The processors operate asynchronously / independently."]) + "</p>", None) + req("3 marks", "Describe", "Describe how a massively parallel computer might forecast the weather.", "Split the problem, work at once, share results.",
  "<p>" + mks(["The atmosphere is divided into many small areas and each processor is responsible for its own part.", "All the processors work simultaneously on their parts of the problem.", "They communicate by sending messages over the network, for example to share boundary values with neighbours."]) + "</p>", None) + req("2 marks", "State", "State two limitations of massively parallel computers.", "Splitting and communicating.",
  "<p>" + mks(["The problem has to be split into parts that can be done at the same time.", "Communication between processors takes time and the network is complex and expensive."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on SISD, SIMD, MISD, MIMD and massively parallel computers (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Say what is single and what is multiple.", "Instruction streams and data streams: S or M for each."),
  ("SIMD: same instruction, different data.", "MISD: different instructions, same data."),
  ("MIMD: independent.", "Many processors, different instructions and data, asynchronously."),
  ("SISD: one processor, sequential.", "One control unit, one memory unit."),
  ("Massively parallel: many, together, messages.", "Many processors linked by a network, each doing its part of one problem."),
  ("Do not only expand the acronym.", "Give the features."),
], [
  ("what SIMD is", "The same instruction is performed on many different data streams at the same time."),
  ("what MIMD is", "Many processors each run different instructions on different data, independently."),
  ("what massively parallel means", "Very many processors working simultaneously on parts of the same problem, communicating by messages."),
  ("a difference between SIMD and MISD", "SIMD runs one instruction on many data streams; MISD runs different instructions on one data stream."),
], [("Identify", "Name the architecture."), ("Describe", "Say what it does and how, in several points."), ("Outline", "Give the main characteristics."), ("State", "Give the difference or similarity, naming both.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const A = [
    ["SISD", 1, 1, "One processor carries out one instruction at a time on one data item."],
    ["SIMD", 1, 3, "One instruction is applied to several data items at once."],
    ["MISD", 3, 1, "Several processors apply different instructions to the same data."],
    ["MIMD", 3, 3, "Each processor runs its own instructions on its own data."]
  ];
  const draw = (s) => {
    const k = Math.round(s.i), [name, ni, nd] = A[k]; let o = SV.text(30, 26, name, "lbl bd", { style: "font-size:22px" });
    const np = Math.max(ni, nd) === 1 ? 1 : 3, cols = ["f1", "f2", "f3"];
    for (let p = 0; p < np; p++) {
      const y = 50 + p * 62, x = 330;
      o += SV.rect(x, y, 140, 48, cols[p], { rx: 8 }) + SV.text(x + 70, y + 29, "Processor " + (p + 1), "lbl bd", { "text-anchor": "middle", style: "font-size:13px" });
      const ins = ni === 1 ? "same instruction" : "instruction " + "ABC"[p], dat = nd === 1 ? "same data" : "data " + (p + 1);
      o += arrow(190, y + 24, 328, y + 24, "r", "c1", 1) + SV.text(30, y + 28, ins, "lbl", { style: "font-size:14px" }) + arrow(580, y + 24, 472, y + 24, "l", "c2", 1) + SV.text(590, y + 28, dat, "lbl", { style: "font-size:14px" });
    }
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 240, label: "The four architectures", base: { i: 0 }, draw, tween: 250, dwell: 3600, steps: A.map((a, i) => ({ cap: "<b>" + a[0] + "</b>: " + a[3], s: { i } })) });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    for (let r = 0; r < 3; r++) for (let c = 0; c < 6; c++) { const x = 40 + c * 78, y = 30 + r * 56; o += SV.rect(x, y, 66, 44, k >= 1 ? (k >= 2 ? "cell-ok" : "f3") : "cell", { rx: 6 }) + SV.text(x + 33, y + 27, "P" + (r * 6 + c + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" }); }
    if (k >= 1) o += SV.text(40, 215, "each processor gets its own part of the problem", "lbl bd", { style: "font-size:14px" });
    if (k >= 2) o += SV.text(40, 238, "all work at the same time; results shared as messages over the network", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 255, label: "A massively parallel computer", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "A massively parallel computer links together a very large number of processors (only 18 are drawn).", s: { i: 0 } },
    { cap: "A big problem is split into parts and <b>each processor is responsible for its own part</b>.", s: { i: 1 } },
    { cap: "They <b>work simultaneously</b> and communicate by <b>sending messages</b> across the network, combining their results.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let ni = 1, nd = 1;
  const names = { "1,1": ["SISD", "One processor, one instruction at a time, one data item. Sequential."], "1,3": ["SIMD", "The same instruction on many data items at once."], "3,1": ["MISD", "Different instructions on the same data stream."], "3,3": ["MIMD", "Different instructions on different data, independently."] };
  const paint = () => {
    $$("#aI button").forEach((b, i) => b.classList.toggle("pri", (i === 0 ? 1 : 3) === ni)); $$("#aD button").forEach((b, i) => b.classList.toggle("pri", (i === 0 ? 1 : 3) === nd));
    const n = names[ni + "," + nd]; $("#aO").innerHTML = `<div class="readout"><div><small>Architecture</small><strong>${n[0]}</strong></div></div><div class="verdict">${n[1]}</div>`;
  };
  $("#aI").innerHTML = '<span style="align-self:center;margin-right:6px">Instruction streams:</span><button class="b">Single</button><button class="b">Multiple</button>';
  $("#aD").innerHTML = '<span style="align-self:center;margin-right:6px">Data streams:</span><button class="b">Single</button><button class="b">Multiple</button>';
  $$("#aI button").forEach((b, i) => (b.onclick = () => { ni = i === 0 ? 1 : 3; paint(); })); $$("#aD button").forEach((b, i) => (b.onclick = () => { nd = i === 0 ? 1 : 3; paint(); })); paint();
})();

/* Lab 2 */
(function () {
  let p = 8, c = 0; const T = 1200;
  const paint = () => { const t = T / p + c * (p - 1) * 0.5; $("#s1").textContent = T + " s"; $("#s2").textContent = t.toFixed(1) + " s"; $("#s3").textContent = (T / t).toFixed(1) + "×"; };
  Lib.slider($("#sP"), { id: "sps", label: "Number of processors ", min: 1, max: 64, value: p, fmt: (x) => x, onInput: (v) => { p = v; paint(); } });
  Lib.slider($("#sC"), { id: "scs", label: "Communication cost per extra processor (seconds × 0.5) ", min: 0, max: 5, value: c, fmt: (x) => x, onInput: (v) => { c = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["SISD", "1 instruction stream, 1 data stream", "One processor, control unit and memory; sequential", "A basic single-core processor"],
  ["SIMD", "1 instruction stream, many data streams", "Same instruction on many data items at once; array processors", "Graphics processing"],
  ["MISD", "Many instruction streams, 1 data stream", "Different operations on the same data; rare", "Fault-tolerant checking"],
  ["MIMD", "Many instruction streams, many data streams", "Many processors working independently, asynchronously", "A multi-core PC, a cluster"],
  ["Massively parallel", "Very many processors working on one problem", "Network, message passing, each processor its own part", "Weather forecasting"]
], ["Type", "Streams", "Features", "Example"]);
''' + CLASSIFY("cl1", "Which architecture is described?", ["SISD", "SIMD", "MISD", "MIMD"],
  [("One processor, instructions executed sequentially", 0), ("The same instruction on many data items at once", 1), ("Different instructions on the same data stream", 2), ("Many processors, each with its own instructions and data", 3), ("Contains one processor, a control unit and a memory unit", 0), ("Array processors performing the same operation", 1), ("Processors operate asynchronously and independently", 3), ("Several processors work on a single data stream", 2)],
  "Single or multiple instructions; single or multiple data.") + CLASSIFY("cl2", "Is the statement true of SIMD or of MISD?", ["SIMD", "MISD"],
  [("All the processors execute the same instruction", 0), ("The processors perform different instructions", 1), ("Many data streams are processed at once", 0), ("All processors work on the same data", 1), ("Suits applying one operation to every pixel", 0), ("Used where different checks are made on one data stream", 1)],
  "SIMD: same instruction, many data. MISD: different instructions, same data.") + ORDER(
  "Put the steps of solving a problem on a massively parallel computer in order.",
  ["The problem is divided into many parts", "Each processor is given its own part", "All the processors work on their parts at the same time", "Processors exchange results by sending messages", "The results are combined into the answer"],
  "Divide, assign, work together, message, combine.") + MATCH([
  ["SISD", "Single instruction, single data"], ["SIMD", "Same instruction applied to multiple data streams"], ["MISD", "Different instructions on one data stream"], ["MIMD", "Different instructions on different data, independently"], ["Massively parallel", "Very many processors working together on one problem"]]) + CALC([
  {"q": "A SIMD processor applies one instruction to 8 data items at a time. How many instructions are needed to process 64 items?", "a": 8, "unit": "", "tol": 0.01, "hint": "64 ÷ 8.", "sol": "<b>8</b>."},
  {"q": "1200 equal tasks of 1 second are shared equally between 24 processors with no communication cost. How long does it take?", "a": 50, "unit": "s", "tol": 0.01, "hint": "1200 ÷ 24.", "sol": "<b>50</b> seconds."},
  {"q": "The same job on a single processor takes 1200 s. What is the speed-up with 24 processors (perfect sharing)?", "a": 24, "unit": "×", "tol": 0.01, "hint": "1200 ÷ 50.", "sol": "<b>24</b> times."},
  {"q": "How many data streams does a SISD computer have?", "a": 1, "unit": "", "tol": 0.01, "hint": "Single data.", "sol": "<b>1</b>."},
  {"q": "In MIMD, 4 processors each run their own program. How many instruction streams?", "a": 4, "unit": "", "tol": 0.01, "hint": "One each.", "sol": "<b>4</b>."}]) + MCQ([
  ("What does SIMD stand for?", ["Single Instruction, Multiple Data", "Several Instructions, Multiple Data", "Single Instruction, Many Devices", "Serial Instruction, Multiple Data"], 0, "Single Instruction, Multiple Data."),
  ("Which architecture has many processors working independently on different data?", ["SISD", "SIMD", "MISD", "MIMD"], 3, "MIMD."),
  ("In massively parallel computers, how do processors communicate?", ["By sending messages over a network", "They do not", "Through a single bus only", "By sharing one register"], 0, "A message interface over a network."),
  ("Which executes instructions sequentially?", ["SISD", "SIMD", "MISD", "MIMD"], 0, "SISD."),
  ("Which applies different instructions to the same data?", ["SISD", "SIMD", "MISD", "MIMD"], 2, "MISD.")], "qz1") + CARDS([
  ("SISD", "One processor; one instruction at a time on one data item."), ("SIMD", "Same instruction, multiple data items at once."), ("MISD", "Multiple instructions, same data."), ("MIMD", "Multiple instructions, multiple data, independent."),
  ("Massively parallel", "Many processors linked together, one problem, messages."), ("Asynchronous", "Not in step: each processor works independently."), ("Array processor", "Does the same operation on many data items."), ("Message passing", "How processors in a massively parallel computer communicate.")])

build("ac1512", "ac-15-1-2-computer-architectures", "Computer Architectures: SISD, SIMD, MISD, MIMD", EYA("15.1.2"),
  "The four categories of computer architecture, massively parallel computers, what is single and what is multiple; animations, a speed-up lab and the real Paper 3 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.1 Processors, parallel processing and virtual machines"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
