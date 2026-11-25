"""A Level CS syllabus 14.1.1 to 14.1.3: why protocols are essential, the protocol stack, the four TCP/IP layers.
14.1.4 (application layer protocols) is mk_ac1414.py. Past paper and review questions and some animations are sliced from the old
single page kept in mk_ac141_src.py. Run: python3 tools/artifact-kit/mk_ac141.py"""
import re
from ak20 import *
import mk_ac141_src as O

SUB = CBK("Chapter 14 · Communication and internet technologies, section 14.1 Protocols")
PRE = O.js[:O.js.index("(function () {")]          # shared JS helpers + LAYERS
_ST = [m.start() for m in re.finditer(r"^\(function \(\) \{", O.js, re.M)]
_END = [O.js.index("/* Lab 1 */"), O.js.index("/* Lab 2 */"), O.js.index("btnTable("), O.js.index("Lib.classify(")]
STA, STB, STC = (O.js[_ST[i]:_ST[i + 1]] for i in range(3))     # message down/up, headers, adjacent layers
LAB_PACKET = O.js[_END[0]:_END[1]]
LAB_JOB = O.js[_END[1]:_END[2]]
LAB_COMPARE = O.js[_END[2]:_END[3]]

_PB = [b for b in re.split(r'(?=  <details class="eq">)', O.past)]
_PB = [re.sub(r"\s*<h3>.*?</h3>\s*", "\n", b, flags=re.S) for b in _PB]   # drop the old section headings
_RB = re.split(r'(?=  <details class="eq">)', O.review)   # index 0 is empty; indices match the old page
_WH = O.where


def pick(blocks, idx):
    return "".join(blocks[i] for i in idx)


def where(idx):
    return [_WH[i] for i in idx]


def mcq(items, el="qz1"):
    return MCQ(items, el)


FOOT = " · "

# ======================================================================= 14.1.1
learn1 = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>protocol</b> is a <b>standard set of rules</b> for communication between devices: it fixes the format of the data, how devices are addressed, the order of the messages and what to do when something goes wrong. Protocols are <b>essential</b> because they let devices from <b>different manufacturers and platforms</b> communicate, and they make communication <b>independent of the hardware and software</b> in use. If two devices followed different rules, the data would arrive but would <b>not be understood</b>. A protocol is a set of rules, not a program, although software is what carries the rules out. The next page shows how protocols are organised into a stack of layers.</p></div>

  <h2>1 · What a protocol is</h2>
  <ul>
    <li>A protocol is an <b>agreed set of rules</b> that two or more devices follow when they communicate.</li>
    <li>It is a <b>standard</b>: published and shared, so anyone can build a device that follows it.</li>
    <li>It is <b>not</b> a piece of hardware and not a single program. Software on each device <b>implements</b> the rules.</li>
  </ul>

  <h2>2 · What a protocol sets</h2>
  <div class="tw"><table class="t">
    <tr><th>Rule</th><th>What it decides</th><th>Everyday example</th><th>If devices disagree</th></tr>
    <tr><td><b>Data format</b></td><td>How the bits are arranged and what they mean</td><td>A web page is sent as text in a set layout</td><td>The receiver reads nonsense</td></tr>
    <tr><td><b>Addressing</b></td><td>How a sender names the receiver</td><td>An IP address on every packet</td><td>The data goes to the wrong place or nowhere</td></tr>
    <tr><td><b>Order of messages</b></td><td>Who sends first and what the reply must be</td><td>A request, then a response</td><td>Both wait, or both talk at once</td></tr>
    <tr><td><b>Speed and timing</b></td><td>How fast to send and how long to wait</td><td>Slow down if the receiver is busy</td><td>Data is lost because the receiver cannot keep up</td></tr>
    <tr><td><b>Error handling</b></td><td>How to spot a problem and recover</td><td>Ask for a lost packet to be sent again</td><td>Damaged data is accepted as correct</td></tr>
  </table></div>

  <h2>3 · Why a protocol is essential</h2>
  <ol>
    <li>It sets a <b>standard</b> for communication, so both ends know what to expect.</li>
    <li>It lets devices from <b>different manufacturers and platforms</b> communicate: a Windows laptop and an Android phone can use the same website.</li>
    <li>It makes communication <b>independent of the hardware and software</b> used.</li>
    <li>Without it, devices using different rules <b>could not communicate</b>: the receiver would not understand the data.</li>
  </ol>
  <div class="tip"><b class="h">Exam wording</b>"A protocol is a standard set of rules that allows communication between devices. It lets devices on different platforms or from different manufacturers communicate, because they follow the same rules."</div>

  <h2>4 · Protocols you already trust</h2>
  <div class="tw"><table class="t">
    <tr><th>Human example</th><th>The shared rules</th><th>What goes wrong without them</th></tr>
    <tr><td>Speaking a language</td><td>Vocabulary and grammar</td><td>Words are heard but not understood</td></tr>
    <tr><td>A postal address</td><td>Name, street, town, postcode in an agreed order</td><td>The letter is lost or delivered wrongly</td></tr>
    <tr><td>Driving on the road</td><td>Which side, traffic lights, signs</td><td>Crashes and gridlock</td></tr>
    <tr><td>A plug and socket</td><td>Shape, voltage and pin layout</td><td>The appliance does not fit or is damaged</td></tr>
  </table></div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing that a protocol "makes data faster" or "makes it secure". It makes communication <b>possible and consistent</b>; some protocols add security, but that is not why protocols are essential.</li>
    <li>Saying "so devices can communicate" and stopping. Add <b>why</b>: they follow the same standard rules, so different manufacturers and platforms can understand each other.</li>
    <li>Calling a protocol a program or a piece of hardware. It is a <b>set of rules</b>.</li>
    <li>Describing one named protocol when the question asks why protocols in general are needed.</li>
  </ul>
'''

watch1 = '''
  <h2>1 · Two devices, different rules</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · A protocol fixes the order of messages</h2>
  <div id="stB"></div>
  <h2>3 · One standard instead of many translators</h2>
  <div id="stC"></div>
'''

explore1 = '''
  <h2>Lab 1 · Will these two devices understand each other?</h2>
  <p>Set the rules each device follows, then send the message. Devices only communicate if <b>every</b> rule matches.</p>
  <div class="card"><div id="lab1"></div></div>

  <h2>Lab 2 · How many translators without a standard?</h2>
  <p>If every pair of makers had to agree its own rules, the number of separate arrangements grows quickly.</p>
  <div class="card"><div id="lab2s"></div><div id="lab2o"></div></div>

  <h2>Lab 3 · What a protocol defines</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise1 = '''
  <h2>1 · Does a protocol set this?</h2><div id="cl1" class="card"></div>
  <h2>2 · Good reason or wrong reason?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put a simple exchange in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Pairs and standards</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real1 = RWNOTE + (
rw("The airport", "Pilots and air traffic controllers all over the world use English phrases from an agreed list. A pilot from one country and a controller from another understand each other because they follow the same rules, not because they share a native language.", "a protocol is a standard that lets people or devices from different backgrounds communicate.") +
rw("USB-C chargers", "A phone, tablet and laptop from different companies can use the same charger and cable because the connector shape, voltages and signalling follow one standard.", "devices from different manufacturers work together when they follow the same standard.") +
rw("Any phone, any website", "An iPhone, an Android phone and a games console all load the same web page. The website does not know or care which device it is talking to, because both ends follow the same protocols.", "communication is independent of the hardware and software in use.") +
rw("Bluetooth headphones", "Headphones from one company pair with a phone from another. If each maker invented a private way of pairing, you could only buy a matching set.", "without a shared protocol, devices from different makers could not communicate.") +
rw("A letter with the wrong address layout", "A letter with the postcode first and no street name may be rejected by sorting machines that expect the usual order. The letter exists but the machine cannot interpret it.", "data that does not follow the agreed format is not understood by the receiver.")
)

where1 = where([0, 1, 2])
past1 = '''  <p class="note">"Why is a protocol essential?" is a regular two-mark question in Paper 3: it appears in O/N 2022, M/J 2024 and O/N 2025. The wording of the mark scheme barely changes, so learn the two points and the reason behind them.</p>

  <h3>Why a protocol is used</h3>
''' + pick(_PB, [1, 2, 3])

review1 = req("2 marks", "State", "State two things that a protocol sets for communication between two computers.", "Think of the rules table: format, addressing, order, timing, errors.",
  "<p>Any two: " + mks(["The format of the data", "How devices are addressed", "The order of the messages", "The speed / timing of transmission", "How errors are detected and handled"]) + "</p>", None) + req("3 marks", "Explain", "A laptop from one manufacturer is connected to a printer from another. Explain why they can work together.", "Use the word standard and say what it allows.",
  "<p>" + mks(["Both follow the same protocol / standard set of rules.", "So each device understands the data and commands that the other sends.", "The protocol makes communication independent of the manufacturer, hardware and software."]) + "</p>", None) + req("2 marks", "Describe", "Describe what could happen if two devices used different protocols to communicate.", "Think about what the receiver does with the data.",
  "<p>" + mks(["The data would not be understood / interpreted correctly by the receiving device.", "The devices would be unable to communicate (or the data would be lost or misread)."]) + "</p>", None) + req("2 marks", "Explain", "Ten manufacturers each make devices that must connect to all of the others. Explain why one shared protocol is better than each pair of makers agreeing its own rules.", "Count the pairs: 10 × 9 ÷ 2.",
  "<p>" + mks(["Without a standard there would be 45 separate sets of rules; with one protocol each maker builds to a single standard.", "That is simpler, cheaper and means any new device works with all the others."]) + "</p>", None)

exam1 = exam20("Part 1 is the real 9618 questions on why protocols are used (Paper 3), 2022 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where1, past1, review1)

tips1 = tips_html([
  ("Give two points.", "A standard set of rules, and what it allows (devices from different manufacturers or platforms can communicate)."),
  ("Say 'standard'.", "It is the word the mark scheme looks for."),
  ("Say what happens without one.", "The devices would not be able to communicate because the data would not be understood."),
  ("Do not call it a program.", "A protocol is a set of rules. Software carries them out."),
  ("Do not say it makes things faster or secure.", "Those are not the reason protocols are essential."),
], [
  ("why protocols are essential", "They set a standard so that devices from different manufacturers and platforms can communicate."),
  ("what happens without one", "The devices would use different rules, so the receiver would not understand the data."),
  ("independence", "A protocol makes communication independent of the hardware and software in use."),
], [("State", "Give the point only."), ("Outline", "Give the main points briefly."), ("Describe", "Say what it does or what happens."), ("Explain", "Give the reason as well.")]) + FC

js1 = PRE + r'''
(function () {
  const dev = (x, y, name, rule, k, bad) => SV.rect(x, y, 170, 70, bad ? "cell-no" : k ? "cell-ok" : "f1", { rx: 10, ...op(0.8) }) + SV.text(x + 85, y + 28, name, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 85, y + 52, rule, "sm", { "text-anchor": "middle" });
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const same = k >= 4, sent = k >= 1;
    o += dev(30, 40, "Device A", same ? "Rules: protocol X" : "Rules: made-up set 1", same, false) + dev(560, 40, "Device B", same ? "Rules: protocol X" : "Rules: made-up set 2", same, k === 2 || k === 3);
    if (sent) o += SV.line(200, 75, 560, 75, "ax", { "stroke-width": 2.5 }) + SV.arrowHead(560, 75, "r", "dot1");
    if (k === 1 || k === 4 || k === 5) o += SV.text(380, 62, "HELLO", "lbl bd", { "text-anchor": "middle" });
    if (k === 2 || k === 3) o += SV.text(380, 62, "01001000 01000101 …", "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" });
    if (k === 3) o += SV.text(645, 150, "?@#% ¿", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(645, 175, "not understood", "sm", { "text-anchor": "middle" });
    if (k === 5) o += SV.text(645, 150, "HELLO", "lbl bd t3", { "text-anchor": "middle" }) + SV.text(645, 175, "understood", "sm", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "Two devices with different rules and then the same rules", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Two devices from different manufacturers. Each has its own idea of how data should look.", s: { i: 0 } },
    { cap: "Device A sends the word HELLO using <b>its</b> rules.", s: { i: 1 } },
    { cap: "The bits arrive intact, but Device B follows <b>different rules</b> for reading them.", s: { i: 2 } },
    { cap: "Device B cannot interpret the data. The message is <b>not understood</b>, so the devices cannot communicate.", s: { i: 3 } },
    { cap: "Now both devices follow the <b>same protocol</b>.", s: { i: 4 } },
    { cap: "Device B reads the data exactly as Device A meant it. The protocol is a <b>standard</b> that makes communication possible.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["Client", "Server"]];
  const msgs = ["Request: 'send me the page'", "Acknowledge: 'request received'", "Data: the page, in the agreed format", "Check: 'did it arrive undamaged?'", "Close: 'finished'"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(110, 22, "Client", "lbl bd", { "text-anchor": "middle" }) + SV.text(650, 22, "Server", "lbl bd", { "text-anchor": "middle" });
    o += SV.line(110, 34, 110, 250, "ax", { "stroke-dasharray": "5 4" }) + SV.line(650, 34, 650, 250, "ax", { "stroke-dasharray": "5 4" });
    msgs.forEach((m, i) => {
      if (i >= k) return; const y = 62 + i * 42;
      const toRight = [true, false, false, true, true][i];
      o += (toRight ? arrow(110, y, 650, y, "r", "c1", 1) : arrow(650, y, 110, y, "l", "c3", 1)) + SV.text(380, y - 8, m, "sm", { "text-anchor": "middle", ...halo });
    });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 270, label: "Order of messages in a simple exchange", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [
    { cap: "Before any message, the protocol has decided <b>who speaks first</b> and what the reply must look like.", s: { i: 0 } },
    { cap: "The client sends a <b>request</b> in the agreed format.", s: { i: 1 } },
    { cap: "The server <b>acknowledges</b> it, as the protocol says it must.", s: { i: 2 } },
    { cap: "The server sends the <b>data</b> in the format both ends expect.", s: { i: 3 } },
    { cap: "The client <b>checks</b> the data and reports any problem, so errors are handled in a set way.", s: { i: 4 } },
    { cap: "Either end can <b>close</b> the exchange. Every step followed a rule that both devices already knew.", s: { i: 5 } }] });
})();

(function () {
  const P = [[380, 30], [570, 90], [500, 195], [260, 195], [190, 90]], names = ["A", "B", "C", "D", "E"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    if (k <= 1) { for (let a = 0; a < 5; a++) for (let b = a + 1; b < 5; b++) o += SV.line(P[a][0], P[a][1] + 18, P[b][0], P[b][1] + 18, "c2", { "stroke-width": 2, ...op(0.55) }); }
    if (k >= 2) { P.forEach((p) => (o += SV.line(p[0], p[1] + 18, 380, 125, "c3", { "stroke-width": 2.5 }))); o += SV.rect(325, 103, 110, 44, "cell-ok", { rx: 10 }) + SV.text(380, 131, "Protocol", "lbl bd", { "text-anchor": "middle" }); }
    P.forEach((p, i) => (o += SV.circle(p[0], p[1] + 18, 20, "dot1", op(0.9)) + SV.text(p[0], p[1] + 25, names[i], "lbl bd", { "text-anchor": "middle", style: "fill:#fff" })));
    o += SV.text(30, 268, k === 0 ? "5 makers, no standard" : k === 1 ? "10 separate arrangements needed (5 × 4 ÷ 2)" : "5 makers, one shared protocol: each builds to 1 standard", "lbl bd", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 280, label: "Many private arrangements against one shared standard", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "Five manufacturers, each with its own way of communicating.", s: { i: 0 } },
    { cap: "For all five to work together, every pair needs its own arrangement: <b>10</b> links, and every new maker adds more.", s: { i: 1 } },
    { cap: "With one <b>shared protocol</b>, each maker follows the same rules once and every device can talk to every other.", s: { i: 2 } }] });
})();

(function () {
  const fmt = ["ASCII (8 bit)", "Unicode (16 bit)"], spd = ["9600 bit/s", "115200 bit/s"], err = ["Parity check", "No checking"];
  const st = { A: [0, 0, 0], B: [0, 0, 0] };
  const sel = (who, idx, opts) => `<label>${who === "A" ? "Device A" : "Device B"}: <select data-w="${who}" data-i="${idx}">${opts.map((o, j) => `<option value="${j}"${st[who][idx] === j ? " selected" : ""}>${o}</option>`).join("")}</select></label>`;
  const paint = () => {
    const bad = [0, 1, 2].filter((i) => st.A[i] !== st.B[i]), ok = bad.length === 0;
    const rules = [["Data format", fmt], ["Speed", spd], ["Error handling", err]];
    $("#lab1").innerHTML = rules.map((r, i) => `<div style="margin-bottom:8px"><b>${r[0]}</b><br>${sel("A", i, r[1])} &nbsp; ${sel("B", i, r[1])}</div>`).join("") +
      `<div class="verdict ${ok ? "ok" : "no"}">${ok ? "Every rule matches. Device B reads: HELLO. The devices communicate." : "Rules that do not match: " + bad.map((i) => rules[i][0]).join(", ") + ". Device B reads: ?@#% ¿  The data arrives but is not understood."}</div>`;
    $$("#lab1 select").forEach((s) => (s.onchange = () => { st[s.dataset.w][+s.dataset.i] = +s.value; paint(); }));
  };
  paint();
})();

(function () {
  Lib.slider($("#lab2s"), { id: "nm", label: "Number of manufacturers: ", min: 2, max: 30, value: 5, onInput: (n) => {
    const pairs = n * (n - 1) / 2;
    $("#lab2o").innerHTML = `<div class="tw"><table class="t"><tr><th>Without a standard</th><th>With one shared protocol</th></tr><tr><td><b>${pairs}</b> separate arrangements (${n} × ${n - 1} ÷ 2)</td><td><b>${n}</b> makers each follow <b>1</b> standard</td></tr></table></div><div class="verdict">A shared protocol saves ${pairs - n > 0 ? pairs - n : 0} arrangements at ${n} manufacturers.</div>`;
  } });
})();

btnTable("eB", "eO", [
  ["Data format", "How the bits are arranged and what they mean", "Text in a set layout; the same character codes", "The receiver reads nonsense"],
  ["Addressing", "How the sender names the receiver", "An address on every packet", "Data goes to the wrong place"],
  ["Order of messages", "Who sends first, what the reply is", "Request then response", "Both ends wait or both talk at once"],
  ["Speed and timing", "How fast to send, how long to wait", "Slow down if the receiver is busy", "Data is lost because the receiver cannot keep up"],
  ["Error handling", "How to spot and recover from a problem", "Ask for lost data to be sent again", "Damaged data is accepted"]
], ["Rule", "What it decides", "Example", "If devices disagree"]);
''' + CLASSIFY("cl1", "Does a protocol set this?", ["Set by a protocol", "Not set by a protocol"],
  [("The format of the data", 0), ("The order of the messages", 0), ("The colour of the monitor", 1), ("What to do if data is lost", 0), ("How fast the user types", 1), ("The brand of the computer", 1), ("How devices are addressed", 0), ("The size of the hard drive", 1)],
  "A protocol sets the rules of the communication: format, order, addressing, timing and errors.") + CLASSIFY("cl2", "Good reason or wrong reason for using protocols?", ["Correct reason", "Wrong reason"],
  [("So devices from different manufacturers can communicate", 0), ("So communication is independent of the hardware and software", 0), ("To make the files smaller", 1), ("Without one, devices might not understand each other's data", 0), ("To make every connection faster", 1), ("To set a standard set of rules", 0), ("To stop all hackers", 1)],
  "Protocols are about a standard that makes communication possible. They do not compress data or guarantee speed or security.") + ORDER(
  "Put this simple exchange in the order the protocol requires.",
  ["The client sends a request", "The server acknowledges the request", "The server sends the data", "The client checks the data for errors", "The exchange is closed"],
  "Request, acknowledge, data, check, close.") + MATCH([
  ["Protocol", "A standard set of rules for communication"], ["Standard", "An agreed, shared specification anyone can follow"], ["Platform", "The hardware and operating system a device runs on"], ["Manufacturer", "The company that makes a device"], ["Compatible", "Able to work together because the same rules are followed"]]) + CALC([
  {"q": "4 manufacturers each need to connect to all of the others without a standard. How many separate arrangements?", "a": 6, "unit": "", "tol": 0.01, "hint": "4 × 3 ÷ 2.", "sol": "<b>6</b>."},
  {"q": "10 manufacturers, no standard. How many separate arrangements?", "a": 45, "unit": "", "tol": 0.01, "hint": "10 × 9 ÷ 2.", "sol": "<b>45</b>."},
  {"q": "20 manufacturers, no standard. How many separate arrangements?", "a": 190, "unit": "", "tol": 0.01, "hint": "20 × 19 ÷ 2.", "sol": "<b>190</b>."},
  {"q": "10 manufacturers all follow one shared protocol. How many standards does each maker build to?", "a": 1, "unit": "", "tol": 0.01, "hint": "The same one.", "sol": "<b>1</b>."},
  {"q": "A device must follow 3 rules (format, speed, error handling) and the other device matches on 2 of them. How many rules do not match?", "a": 1, "unit": "", "tol": 0.01, "hint": "3 − 2.", "sol": "<b>1</b>. One mismatch is enough to stop the data being understood."}]) + mcq([
  ("What is a protocol?", ["A type of cable", "A standard set of rules for communication", "A program that stores data", "A kind of network card"], 1, "A set of rules."),
  ("Why is a protocol essential?", ["It makes data smaller", "It lets devices from different manufacturers communicate", "It stops viruses", "It makes the screen brighter"], 1, "A shared standard makes communication possible."),
  ("Two devices follow different protocols. What is most likely?", ["Faster transfer", "The data is not understood", "The data is automatically fixed", "Nothing changes"], 1, "The receiver cannot interpret the data."),
  ("Which is NOT normally set by a protocol?", ["Data format", "Order of messages", "Error handling", "The colour of the case"], 3, "Case colour is not communication."),
  ("A protocol makes communication independent of...", ["the data", "the hardware and software in use", "the receiver", "the sender"], 1, "Hardware and software independence."),
  ("A protocol is best described as...", ["a program", "a piece of hardware", "a set of rules", "an operating system"], 2, "Rules.")]) + CARDS([
  ("Protocol", "A standard set of rules for communication between devices."), ("Standard", "An agreed specification anyone can follow."), ("Why essential", "Devices from different manufacturers and platforms can communicate."), ("Independence", "Communication does not depend on the hardware and software used."),
  ("Without one", "The data would not be understood."), ("Sets", "Format, addressing, order of messages, timing, error handling."), ("Not a program", "Software implements the rules; the protocol is the rules."), ("Interoperable", "Able to work with devices from other makers.")])

# ======================================================================= 14.1.2
learn2 = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A protocol suite is built as a <b>stack of layers</b>, and each layer has its <b>own functionality</b>. A layer can only accept input from the <b>next higher</b> or the <b>next lower</b> layer, and the <b>interface</b> between adjacent layers is the only interaction between layers. <b>User interaction</b> happens at the top of the stack and <b>direct access to the hardware</b> happens at the bottom. When a message is sent it passes <b>down</b> the stack on the sender, with each layer adding data to the <b>header</b>, and <b>up</b> the stack on the receiver, where each layer removes its header. Layering makes the system easier to build, test and improve, because one layer can change without the others having to change.</p></div>

  <h2>1 · The stack idea</h2>
  <ul>
    <li>Protocol implementation can be viewed as a <b>stack</b>: layers one on top of another.</li>
    <li>Each layer has its <b>own job</b>. The whole job of communicating is divided into smaller jobs.</li>
    <li>The layers are put in order. The layer at the top is nearest the <b>user</b>, the layer at the bottom is nearest the <b>hardware</b>.</li>
  </ul>

  <h2>2 · The rules of the stack</h2>
  <div class="tw"><table class="t">
    <tr><th>Rule</th><th>What it means</th></tr>
    <tr><td><b>Own functionality</b></td><td>Each layer does one specific job and no other</td></tr>
    <tr><td><b>Adjacent layers only</b></td><td>A layer accepts input only from the layer above or the layer below. It never skips a layer</td></tr>
    <tr><td><b>Interface</b></td><td>The point where two adjacent layers meet. It is the only interaction between those layers</td></tr>
    <tr><td><b>Installed software</b></td><td>The interactions between layers are carried out by software installed on the device</td></tr>
    <tr><td><b>Top and bottom</b></td><td>User interaction takes place at the top. Direct access to the hardware takes place at the bottom</td></tr>
    <tr><td><b>Headers</b></td><td>Data is added to the header as packets and frames pass down the layers, and removed as they pass up</td></tr>
  </table></div>

  <h2>3 · Down the stack, across, up the stack</h2>
  <ol>
    <li>The message starts in a program at the <b>top</b> layer of the <b>sending</b> device.</li>
    <li>It passes <b>down</b>, one layer at a time. Each layer treats what it receives as its data and <b>adds its own header</b> in front.</li>
    <li>At the bottom the data is sent over the physical medium, through any routers, to the receiving device.</li>
    <li>On the <b>receiving</b> device it passes <b>up</b>, one layer at a time. Each layer <b>reads and removes</b> its own header, then hands the rest to the layer above.</li>
    <li>The program at the top receives the original message.</li>
  </ol>
  <div class="code">''' + pc('''# data gains a header at each layer on the way down (encapsulation)
message  = "GET /index.html"                          # top layer: the message
segment  = {"seq": 1, "port": 80, "data": message}    # next layer adds a header
packet   = {"src": "192.168.1.5", "dst": "93.184.216.34", "data": segment}
frame    = {"mac_src": "AA:01", "mac_dst": "BB:02", "data": packet}
# the receiver removes the headers in the opposite order, bottom layer first''') + '''</div>

  <h2>4 · Why use layers</h2>
  <ul>
    <li>Each layer can be <b>designed, tested and improved on its own</b>.</li>
    <li>A layer can be <b>replaced</b> (a new Wi-Fi standard, say) without changing the other layers.</li>
    <li><b>Different teams or manufacturers</b> can work on different layers, as long as the interfaces stay the same.</li>
    <li>It is <b>easier to find faults</b>: you can tell which layer is not doing its job.</li>
  </ul>
  <div class="tip"><b class="h">Which stack?</b>The TCP/IP suite is the stack the exam uses. It has four layers: Application, Transport, Internet and Link. This page is about how any stack works; the next page covers what each of those four layers does.</div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Writing that a layer talks to <b>every</b> other layer. Only <b>adjacent</b> layers interact.</li>
    <li>Describing what each layer does when the question says <i>not</i> to (for example "describe how the suite is applied when a message is sent"). Describe the stack, the direction down then up, and the interface.</li>
    <li>Getting the top and bottom the wrong way round. The <b>user</b> is at the top; the <b>hardware</b> is at the bottom.</li>
    <li>Forgetting the header. Say that data is <b>added to the header</b> on the way down and removed on the way up.</li>
  </ul>
'''

watch2 = '''
  <h2>1 · A message goes down the stack, across, and up</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · Headers are added at each layer</h2>
  <div id="stB"></div>
  <h2>3 · Only adjacent layers talk to each other</h2>
  <div id="stC"></div>
'''

explore2 = '''
  <h2>Lab 1 · Build the packet</h2>
  <p>Choose a layer to see what it adds on the way down. The data grows a header at each layer.</p>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div><div class="verdict" id="pV"></div></div>

  <h2>Lab 2 · Can these two layers talk directly?</h2>
  <p>Pick two layers of the stack. Only adjacent layers can exchange data.</p>
  <div class="card"><div id="adj"></div></div>

  <h2>Lab 3 · Change one layer, leave the rest</h2>
  <p>Choose how the device connects. Only the bottom layer changes, which is why layering makes upgrades easy.</p>
  <div class="card"><div id="swB" class="btnrow"></div><div id="swO"></div></div>
'''

practise2 = '''
  <h2>1 · Down the stack or up the stack?</h2><div id="cl1" class="card"></div>
  <h2>2 · Protocol facts or stack facts?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the layers in order, top to bottom</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Counting layers and headers</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real2 = RWNOTE + (
rw("Upgrading Wi-Fi", "Moving from Wi-Fi 5 to Wi-Fi 6 changes the bottom layer only. The browser, the web page and the IP addresses are unchanged, because the layers are separate.", "layers can be improved independently, and only adjacent layers interact.") +
rw("Changing from Wi-Fi to mobile data", "A phone moves out of Wi-Fi range and switches to mobile data. Apps keep working, because only the bottom layer has changed; the layers above are the same.", "a layer can be replaced without changing the others.") +
rw("The post office", "You write a letter (top). The post office puts it in a bag with a sorting code (middle). A van takes the bag to the next depot (bottom). The writer never drives the van, and the driver never reads the letter: each does their own job at their own level.", "each layer has its own functionality and talks only to its neighbours.") +
rw("An operating system", "The network part of Windows, macOS, Android and Linux is installed software that implements the stack. Programs call it, and it calls the network card's driver.", "the interactions between layers are carried out by installed software.") +
rw("Finding a fault", "If a web page will not load but other devices on the same Wi-Fi work, an engineer can check the layers in turn: is the Wi-Fi connected, does the device have an IP address, does the browser's request get a reply?", "layering makes faults easier to isolate.")
)

where2 = where([5, 7, 10, 13])
past2 = '''  <p class="note">Questions about the stack as a whole (not about one particular layer) ask for the same points each time: layers, adjacent only, interface, headers, direction, and user at the top and hardware at the bottom.</p>

  <h3>How the layers interact</h3>
''' + pick(_PB, [5, 6]) + '''
  <h3>Completing a paragraph about the stack</h3>
''' + pick(_PB, [13, 14])

review2 = pick(_RB, [0, 3, 4]) + req("4 marks", "Describe", "Describe what happens to a message as it passes up the protocol stack on the receiving device.", "Which direction, what each layer removes, who gets the message.",
  "<p>" + mks(["The message enters at the bottom layer from the physical medium.", "Each layer reads its own header and removes it.", "The remaining data is passed to the next higher (adjacent) layer.", "At the top layer the original message is passed to the program / user."]) + "</p>", None)

exam2 = exam20("Part 1 is real 9618 questions on how the protocol stack works (Paper 3), 2023 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where2, past2, review2)

tips2 = tips_html([
  ("Say 'adjacent'.", "A layer interacts only with the layer above and the layer below, through the interface between them."),
  ("Say 'down then up'.", "Sending goes top to bottom, receiving bottom to top."),
  ("Headers.", "Data is added to the header on the way down and removed on the way up."),
  ("Top and bottom.", "User interaction at the top, direct access to the hardware at the bottom."),
  ("Read what is excluded.", "If the question says not to describe the functions of the layers, describe how the stack is used instead."),
], [
  ("how the layers interact", "Each layer can only accept input from the next higher or next lower layer, and the interface between adjacent layers is the only interaction."),
  ("how a message travels", "It passes down the stack on the sender, with data added to the header at each layer, and up the stack on the receiver, where the headers are removed."),
  ("why layers", "Each layer can be developed and changed on its own without affecting the others."),
], [("State / Identify", "Give the name or fact only."), ("Outline", "Give the main points briefly."), ("Describe", "Say what it does, in several points."), ("Explain", "Give the reason as well.")]) + FC

js2 = PRE + STA + STB + STC + LAB_PACKET + r'''
(function () {
  const L = ["Application", "Transport", "Internet", "Link"];
  let a = null, b = null;
  const paint = () => {
    const pick = (who, sel) => `<div class="btnrow">` + L.map((l, i) => `<button class="b${sel === i ? " pri" : ""}" data-w="${who}" data-i="${i}">${l}</button>`).join("") + `</div>`;
    let v = "Choose a layer in each row.";
    if (a !== null && b !== null) v = a === b ? "That is the same layer. Pick two different layers." : Math.abs(a - b) === 1 ? L[a] + " and " + L[b] + " are <b>adjacent</b>: they can exchange data through their interface." : L[a] + " and " + L[b] + " are <b>not adjacent</b>. Data has to pass through " + (Math.abs(a - b) === 2 ? "the " + L[Math.min(a, b) + 1] + " layer" : "the layers between them") + " first.";
    $("#adj").innerHTML = "<p><b>First layer</b></p>" + pick("a", a) + "<p><b>Second layer</b></p>" + pick("b", b) + `<div class="verdict">${v}</div>`;
    $$("#adj button").forEach((x) => (x.onclick = () => { if (x.dataset.w === "a") a = +x.dataset.i; else b = +x.dataset.i; paint(); }));
  };
  paint();
})();

(function () {
  const opts = [["Ethernet cable", "Ethernet frames"], ["Wi-Fi", "Wi-Fi frames"], ["Mobile data", "mobile network frames"]];
  const rows = [["Application", "Web browser using HTTP"], ["Transport", "Numbered packets"], ["Internet", "IP addresses"]];
  let cur = 0;
  const paint = () => {
    $$("#swB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#swO").innerHTML = '<div class="tw"><table class="t"><tr><th>Layer</th><th>What it uses</th><th>Changed?</th></tr>' + rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>No</td></tr>`).join("") + `<tr><td><b>Link</b></td><td style="background:var(--warn-soft)">${opts[cur][1]} over ${opts[cur][0].toLowerCase()}</td><td>${cur === 0 ? "No (starting point)" : "<b>Yes</b>"}</td></tr></table></div>`;
  };
  $("#swB").innerHTML = opts.map((o, i) => `<button class="b" data-i="${i}">${o[0]}</button>`).join("");
  $$("#swB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();
''' + CLASSIFY("cl1", "Does this happen on the way down (sending) or on the way up (receiving)?", ["Down the stack", "Up the stack"],
  [("A header is added", 0), ("A header is removed", 1), ("The data starts at the Application layer", 0), ("The data ends at the Application layer", 1), ("Data is passed to the next lower layer", 0), ("Data is passed to the next higher layer", 1), ("The Link layer sends the frames onto the network", 0), ("The Link layer receives the frames from the network", 1)],
  "Sending: down, headers added. Receiving: up, headers removed.") + CLASSIFY("cl2", "Is the statement about a protocol or about the stack?", ["About a protocol", "About the stack"],
  [("A standard set of rules for communication", 0), ("Layers that can only talk to adjacent layers", 1), ("Allows devices from different manufacturers to communicate", 0), ("Headers are added on the way down", 1), ("Makes communication independent of hardware and software", 0), ("User interaction at the top, hardware access at the bottom", 1)],
  "A protocol is the rules. The stack is the layered way of implementing them.") + ORDER(
  "Put the layers in order, from the top (nearest the user) to the bottom.",
  ["Application", "Transport", "Internet", "Link"],
  "Application, Transport, Internet, Link.") + MATCH([
  ["Stack", "Layers of protocols, each with its own function"], ["Layer", "One level of the stack with one specific job"], ["Interface", "The only point of interaction between adjacent layers"], ["Header", "Information added to the data by a layer"], ["Adjacent", "The layer directly above or directly below"]]) + CALC([
  {"q": "How many layers are in the TCP/IP protocol suite as used in the exam?", "a": 4, "unit": "", "tol": 0.01, "hint": "Application, Transport, Internet, Link.", "sol": "<b>4</b>."},
  {"q": "A message goes down the stack. How many headers have been added by the time it leaves the bottom layer (one for each layer below the top)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Transport, Internet and Link.", "sol": "<b>3</b>."},
  {"q": "How many layers can the second layer from the top exchange data with directly?", "a": 2, "unit": "", "tol": 0.01, "hint": "The adjacent layers above and below.", "sol": "<b>2</b>."},
  {"q": "How many layers can the top layer exchange data with directly?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the layer below it.", "sol": "<b>1</b>."},
  {"q": "A message passes down 4 layers, across the network and up 4 layers. How many layers does it pass through in total?", "a": 8, "unit": "", "tol": 0.01, "hint": "4 + 4.", "sol": "<b>8</b>."}]) + mcq([
  ("Where does user interaction take place in a protocol stack?", ["The bottom layer", "The top layer", "Every layer", "The middle layers only"], 1, "At the top."),
  ("Where does direct access to the hardware take place?", ["The top layer", "The bottom layer", "Every layer", "None"], 1, "At the bottom."),
  ("A layer can only interact with...", ["any other layer", "the adjacent layers", "the top layer", "the bottom layer"], 1, "Above and below."),
  ("What happens to the header as data passes down the stack?", ["It is removed", "Data is added to it", "It is encrypted", "Nothing"], 1, "Each layer adds to the header."),
  ("Why is a layered design useful?", ["It makes the data smaller", "A layer can be changed without changing the others", "It removes the need for hardware", "It makes the connection free"], 1, "Independence of the layers."),
  ("What carries out the interactions between layers?", ["Installed software", "A cable", "A router only", "The user"], 0, "Installed software.")]) + CARDS([
  ("Stack", "Layers of protocols, each with its own function."), ("Adjacent", "A layer interacts only with the layer above and below."), ("Interface", "The only interaction between adjacent layers."), ("Top layer", "User interaction."),
  ("Bottom layer", "Direct access to the hardware."), ("Sending", "Down the stack; data added to the header."), ("Receiving", "Up the stack; headers removed."), ("Why layers", "Each layer can change on its own.")])

# ======================================================================= 14.1.3
learn3 = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The TCP/IP protocol suite has <b>four layers</b>, from the top <b>Application, Transport, Internet and Link</b>. The <b>Application</b> layer gives programs their services and defines the protocols they use; the <b>Transport</b> layer breaks data into numbered packets and delivers it from the source host to the destination host; the <b>Internet</b> layer adds IP addresses and routes each packet; the <b>Link</b> layer formats frames with MAC addresses and sends them over the physical medium. Match every job to its layer: sequence numbers and re-sending are Transport, IP addresses and routing are Internet, frames and MAC addresses are Link. A packet keeps the same IP addresses for the whole journey, but the MAC addresses change at every hop. For a tour of all four layers in real situations, see the resource <i>The Four Layers in the Real World</i>.</p></div>

  <h2>1 · The four layers</h2>
  <div class="tw"><table class="t">
    <tr><th>Layer</th><th>Purpose and function</th><th>Protocols and examples</th></tr>
    <tr><td><b>Application</b> (top)</td><td>Provides services and an <b>interface to the user</b>: the programs that exchange data (web browser, email client, file transfer). Defines the protocols applications use to exchange data</td><td>HTTP(S), FTP, SMTP, POP3, IMAP, BitTorrent</td></tr>
    <tr><td><b>Transport</b></td><td>Delivery from the <b>source host to the destination host</b> (end to end). Breaks data into <b>packets</b>, adds a <b>sequence number</b> to the header, controls the <b>flow</b>, detects errors, requests <b>re-sending</b> of lost packets and reassembles the data at the destination</td><td>TCP, UDP</td></tr>
    <tr><td><b>Internet</b></td><td>Identifies the intended <b>network and host</b>. Adds a header with the <b>source and destination IP addresses</b>, forms datagrams, and <b>routes</b> each packet by the best route</td><td>IP</td></tr>
    <tr><td><b>Link</b> (bottom)</td><td>Transports data within the local network segment, <b>formats datagrams into frames</b>, maps <b>IP addresses to MAC addresses</b>, ensures the correct network protocols are followed, and sends and receives the frames over the physical medium</td><td>Ethernet, Wi-Fi</td></tr>
  </table></div>
  <div class="tip"><b class="h">Order to learn</b>From the user down: <b>A</b>pplication, <b>T</b>ransport, <b>I</b>nternet, <b>L</b>ink: "All Tests Include Logic". Some books call the Link layer the Network Access or Data Link layer; the exam uses Link.</div>

  <h2>2 · The Application layer</h2>
  <ul>
    <li>Provides <b>services and an interface</b> for the user's programs, such as login, file transfer and email.</li>
    <li><b>Defines the protocols</b> that applications use to exchange data (HTTP, FTP, SMTP, POP3, IMAP, BitTorrent: see 14.1.4).</li>
    <li>Can provide ways of <b>securing</b> communication, for example encryption and authentication.</li>
  </ul>

  <h2>3 · The Transport layer</h2>
  <ul>
    <li>Responsible for delivery from the <b>source host to the destination host</b>.</li>
    <li>Breaks the data into <b>packets</b> and adds a <b>sequence number</b> (and port number) to the packet header.</li>
    <li><b>Controls the flow</b> of packets, checks for errors and asks for lost or damaged packets to be <b>sent again</b>.</li>
    <li>At the destination it uses the sequence numbers to put the packets back in <b>order</b>.</li>
  </ul>

  <h2>4 · The Internet layer</h2>
  <ul>
    <li>Identifies the intended <b>network and host</b>.</li>
    <li>Adds a header containing the <b>source and destination IP addresses</b> and forms <b>datagrams</b> (packets) ready for delivery.</li>
    <li><b>Routes</b> each packet independently by the best available route. Routers work at this layer.</li>
  </ul>

  <h2>5 · The Link layer</h2>
  <ul>
    <li>Transports data within the <b>local network segment</b>, from one device to the next (the <b>next hop</b>).</li>
    <li><b>Formats the datagrams into frames</b>, mapping the IP address to a <b>MAC address</b>.</li>
    <li>Ensures the correct network protocols are followed and gives the upper layers <b>access to the physical medium</b> (cable, Wi-Fi).</li>
  </ul>

  <h2>6 · What changes on a journey</h2>
  <div class="tw"><table class="t">
    <tr><th>Address</th><th>Layer</th><th>Along the journey</th></tr>
    <tr><td><b>IP address</b> (source and destination)</td><td>Internet</td><td>Stays the same from start to end</td></tr>
    <tr><td><b>MAC address</b> (this hop)</td><td>Link</td><td>Changes at every hop, because each frame only travels one local segment</td></tr>
    <tr><td><b>Sequence number</b></td><td>Transport</td><td>Stays with its packet so the destination can reorder them</td></tr>
  </table></div>

  <h2>7 · Common ways to lose marks</h2>
  <ul>
    <li>Putting the layers in the wrong order. The Application layer is the top, the Link layer the bottom.</li>
    <li>Describing a layer by the function of another: <b>routing and IP addresses</b> are the <b>Internet</b> layer; <b>sequence numbers, error checking and re-sending</b> are the <b>Transport</b> layer.</li>
    <li>Calling the Link layer the "Network" or "Physical" layer.</li>
    <li>Writing "the Application layer is the application". It is the layer that provides services to applications and defines their protocols.</li>
    <li>Describing only one function. A 5-mark question wants up to three points for <i>each</i> layer.</li>
  </ul>
'''

watch3 = '''
  <h2>1 · The Transport layer: split, number, reorder</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stT"></div>
  <h2>2 · The Internet and Link layers: IP stays, MAC changes</h2>
  <div id="stH"></div>
  <h2>3 · The whole trip in one picture</h2>
  <div id="stA"></div>
'''

explore3 = '''
  <h2>Lab 1 · Which layer does the job?</h2>
  <p>Choose the layer for each job.</p>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>

  <h2>Lab 2 · The layers compared</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>

  <h2>Lab 3 · Rebuild the message</h2>
  <p>The Transport layer numbers each packet, so the destination can restore the order. Choose how many packets and shuffle them.</p>
  <div class="card"><div id="rb"></div></div>
'''

practise3 = '''
  <h2>1 · Which layer?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which address or number goes with which layer?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the layers in order, top to bottom</h2><div id="o1" class="card"></div>
  <h2>4 · Match each layer to its main job</h2><div id="m1" class="card"></div>
  <h2>5 · Packets and layers</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real3 = RWNOTE + (
rw("Loading a web page", "Your browser (Application layer) asks for a page with HTTP. The Transport layer splits the reply into numbered packets, the Internet layer addresses each one, and the Link layer sends it over Wi-Fi to your router.", "each layer does its own job as the message passes down.") +
rw("A lost packet", "If a packet in a download is lost, the Transport layer notices a sequence number is missing and asks for it again, without the browser having to do anything.", "the Transport layer handles sequencing, flow and error recovery.") +
rw("Finding the way", "A router reads the destination IP address, which was added by the Internet layer, to decide where to send each packet next.", "routing and IP addresses belong to the Internet layer.") +
rw("Your router's job at home", "Your home router receives a frame over Wi-Fi, takes out the packet, reads the IP address, and sends it on in a new frame to your internet provider. The MAC addresses change; the IP addresses do not.", "MAC addresses are for the next hop, IP addresses for the whole journey.") +
rw("Wi-Fi or Ethernet", "Plug an Ethernet cable into a laptop and the web carries on working. Only the Link layer (the way the frames are sent) has changed.", "the Link layer deals with the physical medium.")
)

where3 = where([3, 4, 6, 8, 9, 11, 12])
past3 = '''  <p class="note">The functions of the layers are examined in nearly every series. Learn the three or so points for each layer and which layer owns which job; a 5-mark question wants both layers, up to three marks each.</p>

  <h3>The functions of the layers</h3>
''' + pick(_PB, [7, 8, 9, 10]) + '''
  <h3>Order, matching and completing</h3>
''' + pick(_PB, [4, 11, 12])

review3 = pick(_RB, [2]) + req("2 marks", "Identify", "Name the layer that (a) adds the source and destination IP addresses; (b) formats the data into frames with MAC addresses.", "Internet adds the IP header. Link makes frames.",
  "<p>" + mks(["(a) Internet layer", "(b) Link layer"]) + "</p>", None) + req("3 marks", "Describe", "A packet travels from a laptop to a server through three routers. State what stays the same and what changes about its addresses.", "IP end to end, MAC at each hop.",
  "<p>" + mks(["The source and destination IP addresses stay the same for the whole journey.", "The MAC addresses change at each hop.", "Because the Link layer only moves the frame across one local network segment at a time."]) + "</p>", None) + req("2 marks", "State", "State what the Transport layer does with the sequence numbers when the packets arrive at the destination.", "Packets can arrive out of order.",
  "<p>" + mks(["It uses the sequence numbers to put the packets back into the correct order.", "It detects that a packet is missing and asks for it to be sent again."]) + "</p>", None)

exam3 = exam20("Part 1 is real 9618 questions on the four TCP/IP layers (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where3, past3, review3)

tips3 = tips_html([
  ("Learn the order.", "Application, Transport, Internet, Link: top to bottom."),
  ("Match the job to the layer.", "Sequence numbers, packets, re-sending: Transport. IP addresses, routing: Internet. Frames, MAC addresses, the cable or Wi-Fi: Link. User services and protocols: Application."),
  ("Three points per layer.", "A 5-mark 'describe two layers' question rewards up to three points for each."),
  ("IP against MAC.", "IP addresses stay the same for the journey; MAC addresses change at every hop."),
  ("Use the exam's name for the bottom layer.", "Link, not Network or Physical."),
], [
  ("what the Transport layer does", "It breaks data into numbered packets, controls the flow and ensures they arrive error free and in order."),
  ("what the Internet layer does", "It adds the source and destination IP addresses and routes each packet by the best route."),
  ("what the Link layer does", "It formats datagrams into frames with MAC addresses and sends them over the physical medium."),
  ("what the Application layer does", "It provides services and an interface to the user, and defines the protocols applications use."),
], [("State / Identify", "Give the name or fact only."), ("Outline", "Give the main points briefly."), ("Describe", "Say what it does, in several points."), ("Match", "Pair each item with the right description.")]) + FC

js3 = PRE + LAB_JOB + LAB_COMPARE + r'''
(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Sender", "lbl bd") + SV.text(560, 22, "Receiver", "lbl bd");
    const order = [1, 2, 3, 4], arrive = [3, 1, 4, 2];
    if (k >= 0) order.forEach((n, i) => { o += SV.rect(30 + i * 60, 34, 50, 38, "f2", { rx: 6, ...op(k >= 1 ? 0.9 : 0.5) }) + SV.text(55 + i * 60, 58, k >= 1 ? "#" + n : "", "lbl bd", { "text-anchor": "middle" }); });
    if (k === 0) o += SV.rect(30, 34, 230, 38, "f2", { rx: 6, ...op(0.7) }) + SV.text(145, 58, "message", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) arrive.forEach((n, i) => { const lost = n === 4 && k === 3; if (k >= 4 && n === 4 && k < 5) return; o += SV.rect(330 + i * 60, 120, 50, 38, lost ? "cell-no" : "f3", { rx: 6, ...op(lost ? 0.5 : 0.9) }) + SV.text(355 + i * 60, 144, lost ? "✗" : "#" + n, "lbl bd", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.line(270, 55, 320, 135, "dash", op(0.6));
    if (k >= 5) o = SV.text(30, 22, "Sender", "lbl bd") + SV.text(560, 22, "Receiver", "lbl bd") + order.map((n, i) => SV.rect(30 + i * 60, 34, 50, 38, "f2", { rx: 6, ...op(0.5) }) + SV.text(55 + i * 60, 58, "#" + n, "lbl bd", { "text-anchor": "middle" })).join("") + order.map((n, i) => SV.rect(330 + i * 60, 120, 50, 38, "cell-ok", { rx: 6 }) + SV.text(355 + i * 60, 144, "#" + n, "lbl bd", { "text-anchor": "middle" })).join("") + SV.text(330, 190, "Put in order using the sequence numbers", "sm");
    if (k === 3) o += SV.text(330, 190, "Packet #4 is lost on the way", "lbl bd t2", { style: "font-size:14px" });
    if (k === 4) o += SV.text(330, 190, "Receiver notices #4 is missing and asks for it again", "lbl bd t4", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stT"), { w: 760, h: 205, label: "Transport layer: packets, sequence numbers, re-sending", base: { i: 0 }, draw, tween: 250, dwell: 2700, steps: [
    { cap: "The Transport layer receives the message from the Application layer.", s: { i: 0 } },
    { cap: "It <b>breaks the message into packets</b> and adds a <b>sequence number</b> to each header.", s: { i: 1 } },
    { cap: "The packets are sent. They may take different routes and <b>arrive out of order</b>.", s: { i: 2 } },
    { cap: "One packet is <b>lost</b> on the way.", s: { i: 3 } },
    { cap: "The destination's Transport layer sees a gap in the sequence numbers and <b>asks for that packet to be sent again</b>.", s: { i: 4 } },
    { cap: "With every packet present, the sequence numbers let the layer <b>reassemble the message in the right order</b> and pass it up.", s: { i: 5 } }] });
})();

(function () {
  const N = [["Laptop", 40, "192.168.1.5"], ["Home router", 230, ""], ["ISP router", 420, ""], ["Web server", 610, "93.184.216.34"]];
  const MAC = [["AA:01", "BB:02"], ["BB:03", "CC:04"], ["CC:05", "DD:06"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    N.forEach((n, i) => { o += SV.rect(n[1], 60, 110, 46, i === 0 || i === 3 ? "f1" : "f3", { rx: 8, ...op(0.8) }) + SV.text(n[1] + 55, 88, n[0], "lbl bd", { "text-anchor": "middle" }); if (i < 3) o += SV.line(n[1] + 110, 83, N[i + 1][1], 83, "ax", { "stroke-width": 2 }); });
    o += SV.text(30, 30, "Internet layer (IP): source 192.168.1.5  →  destination 93.184.216.34, the same on every hop", "sm bd t1");
    if (k >= 1 && k <= 3) { const h = k - 1, x = N[h][1] + 110, w = N[h + 1][1] - x; o += SV.rect(x + 8, 128, w - 16, 54, "cell-warn", { rx: 8 }) + SV.text(x + w / 2, 150, "Link layer frame", "sm bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, 170, MAC[h][0] + " → " + MAC[h][1], "sm", { "text-anchor": "middle", style: "font-family:var(--mono)" }); o += SV.circle(x + w / 2, 83, 7, "dot4"); }
    if (k === 4) o += SV.text(380, 160, "Arrived: IP addresses unchanged, three different pairs of MAC addresses used", "lbl bd t3", { "text-anchor": "middle", style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stH"), { w: 760, h: 200, label: "IP addresses stay the same, MAC addresses change at each hop", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A laptop sends to a web server. The <b>Internet layer</b> puts both IP addresses in the header. They will not change.", s: { i: 0 } },
    { cap: "Hop 1: the <b>Link layer</b> frames the packet with the laptop's and the home router's <b>MAC addresses</b>.", s: { i: 1 } },
    { cap: "Hop 2: the home router removes the frame, reads the destination IP, and makes a <b>new frame</b> with new MAC addresses.", s: { i: 2 } },
    { cap: "Hop 3: the ISP router does the same, framing the packet for the web server.", s: { i: 3 } },
    { cap: "The IP addresses stayed the same for the whole journey; the MAC addresses changed at every hop.", s: { i: 4 } }] });
})();
''' + STA + r'''
(function () {
  let n = 4, order = [];
  const paint = () => {
    const shuffled = order.slice();
    $("#rb").innerHTML = `<div class="btnrow">${[3, 4, 5, 6].map((c) => `<button class="b${c === n ? " pri" : ""}" data-n="${c}">${c} packets</button>`).join("")}<button class="b" id="rbs">Shuffle arrival</button></div>` +
      `<p>Arrived in this order: <b>${shuffled.map((i) => "#" + (i + 1)).join("  ")}</b></p><p>After the Transport layer sorts them by sequence number: <b>${shuffled.slice().sort((a, b) => a - b).map((i) => "#" + (i + 1)).join("  ")}</b></p>`;
    $$("#rb button[data-n]").forEach((b) => (b.onclick = () => { n = +b.dataset.n; order = [...Array(n).keys()]; shuf(); }));
    $("#rbs").onclick = shuf;
  };
  const shuf = () => { order = [...Array(n).keys()]; for (let i = n - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; } paint(); };
  shuf();
})();
''' + CLASSIFY("cl1", "Which layer does each job belong to?", ["Application", "Transport", "Internet", "Link"],
  [("Provides an interface to the user's programs", 0), ("Adds a sequence number to each packet", 1), ("Adds the source and destination IP address", 2), ("Formats datagrams into frames", 3), ("Controls the flow of packets", 1), ("Routes each packet by the best route", 2), ("Maps IP addresses to MAC addresses", 3), ("Defines the protocols programs use to exchange data", 0)],
  "Application: user. Transport: packets and sequence. Internet: IP and routing. Link: frames and MAC.") + CLASSIFY("cl2", "Which layer does this belong to?", ["Transport", "Internet", "Link"],
  [("Sequence number", 0), ("Destination IP address", 1), ("Source MAC address", 2), ("Re-sending a lost packet", 0), ("Routing", 1), ("Wi-Fi or Ethernet", 2), ("Putting packets back in order", 0), ("A datagram", 1)],
  "Sequence and re-sending are Transport. IP and routing are Internet. MAC, frames and Wi-Fi are Link.") + ORDER(
  "Put the layers in order, from the top (nearest the user) to the bottom.",
  ["Application", "Transport", "Internet", "Link"],
  "Application, Transport, Internet, Link.") + MATCH([
  ["Application", "Services for the user's programs and the protocols they use"], ["Transport", "End-to-end delivery in numbered packets"], ["Internet", "IP addresses and routing"], ["Link", "Frames, MAC addresses and the physical medium"]]) + CALC([
  {"q": "A message of 4000 bytes is split into packets of 500 bytes. How many packets?", "a": 8, "unit": "", "tol": 0.01, "hint": "4000 ÷ 500.", "sol": "<b>8</b>."},
  {"q": "A file of 2 MB is split into packets of 1000 bytes (take 1 MB as 1 000 000 bytes). How many packets?", "a": 2000, "unit": "", "tol": 0.01, "hint": "2 000 000 ÷ 1000.", "sol": "<b>2000</b>."},
  {"q": "A packet passes through 3 routers between two hosts. How many separate frames (hops) are used?", "a": 4, "unit": "", "tol": 0.01, "hint": "Host to router 1, 1 to 2, 2 to 3, 3 to host.", "sol": "<b>4</b>."},
  {"q": "Packets 1 to 6 are sent and packet 4 is lost. How many packets must be sent again?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the missing one.", "sol": "<b>1</b>."},
  {"q": "How many layers have a header added or removed that the Application layer never sees (Transport, Internet and Link)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Everything below the top.", "sol": "<b>3</b>."}]) + mcq([
  ("Which layer breaks data into packets and adds sequence numbers?", ["Application", "Transport", "Internet", "Link"], 1, "Transport."),
  ("Which layer adds source and destination IP addresses?", ["Internet", "Link", "Application", "Transport"], 0, "Internet."),
  ("Which is the bottom layer of the TCP/IP stack?", ["Application", "Transport", "Internet", "Link"], 3, "Link."),
  ("Which layer maps IP addresses to MAC addresses?", ["Internet", "Link", "Application", "Transport"], 1, "Link."),
  ("Which layer routes packets by the best route?", ["Transport", "Link", "Internet", "Application"], 2, "Internet."),
  ("Which layer defines HTTP and SMTP?", ["Application", "Transport", "Internet", "Link"], 0, "Application.")]) + CARDS([
  ("Application", "User services; HTTP, FTP, SMTP, POP3, IMAP, BitTorrent."), ("Transport", "Packets, sequence numbers, flow control, error recovery."), ("Internet", "IP addresses and routing."), ("Link", "Frames, MAC addresses, the physical medium."),
  ("Datagram", "A packet with IP addresses in the header."), ("Frame", "A packet with MAC addresses, ready for the physical medium."), ("Hop", "One step from one device to the next."), ("Next hop", "The next device on the route, prepared by the Link layer.")])


def go(bundle, slug, title, num, lead, tabset, js):
    build(bundle, slug, title, EYA(num), lead, dict(sub=SUB, **tabs(*tabset)), js)


import kw141   # key words
learn2, watch2, explore2, practise2, review2, js2 = kw141.add("stack", learn2, watch2, explore2, practise2, review2, js2)
learn3, watch3, explore3, practise3, review3, js3 = kw141.add("layers", learn3, watch3, explore3, practise3, review3, js3)
exam2 = exam20("Part 1 is real 9618 questions on how the protocol stack works (Paper 3), 2023 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where2, past2, review2)
exam3 = exam20("Part 1 is real 9618 questions on the four TCP/IP layers (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where3, past3, review3)
go("ac1411", "ac-14-1-1-why-protocols-are-essential", "Why Protocols Are Essential", "14.1.1",
   "What a protocol is, what it sets, and why devices from different manufacturers and platforms need a shared standard; animations, labs and the real 9618 questions from 2022 to 2025.",
   (learn1, watch1, explore1, practise1, real1, exam1, tips1), js1)
go("ac1412", "ac-14-1-2-the-protocol-stack", "The Protocol Stack", "14.1.2",
   "How protocol implementation is viewed as a stack of layers: own functionality, adjacent layers, interfaces, headers, and the path down and up the stack; animations, labs and the real 9618 questions from 2023 to 2026.",
   (learn2, watch2, explore2, practise2, real2, exam2, tips2), js2)
go("ac1413", "ac-14-1-3-tcp-ip-four-layers", "The TCP/IP Protocol Suite: Four Layers", "14.1.3",
   "The Application, Transport, Internet and Link layers: what each does, which jobs belong to which layer, and how IP and MAC addresses behave on a journey; animations, labs and the real 9618 questions from 2022 to 2026.",
   (learn3, watch3, explore3, practise3, real3, exam3, tips3), js3)
