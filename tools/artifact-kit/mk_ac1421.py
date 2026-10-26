"""A Level CS syllabus 14.2.1: circuit switching. Run: python3 tools/artifact-kit/mk_ac1421.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Circuit switching</b> sends data over a <b>dedicated circuit</b> that is set up between the two ends <b>before</b> any data is sent and kept for the <b>whole</b> of the communication. The whole bandwidth of that path is reserved, so the data flows as a <b>continuous stream</b> along the <b>same route</b> and arrives in the order it was sent. This makes it suitable for <b>real-time</b> communication such as voice calls, but the circuit cannot be used by anyone else while it is open, even when nothing is being sent, and if the route fails the call ends. The three phases are <b>set up</b>, <b>transmit</b>, <b>release</b>. The exam asks you to describe it, give benefits and drawbacks, and say where it is appropriate; comparing it with packet switching is on the next page.</p></div>

  <h2>1 · How circuit switching works</h2>
  <ol>
    <li><b>Set up (establish) the circuit.</b> A dedicated path is found through the network, through switches, from the sender to the receiver. This happens <b>before</b> transmission starts and takes some time.</li>
    <li><b>Transmit.</b> Data travels in a <b>continuous stream</b> along the <b>same route</b>, using the <b>whole bandwidth</b> of the circuit. Transmission is usually bidirectional (both ends can send).</li>
    <li><b>Release.</b> At the end the circuit is closed (released) and the resources can be used for another communication.</li>
  </ol>
  <p>The classic example is a traditional <b>telephone call</b>: when you dial, a circuit is set up through the exchanges and kept for the whole call.</p>

  <h2>2 · Characteristics</h2>
  <ul>
    <li>A <b>dedicated circuit / channel</b> is required.</li>
    <li>The circuit is established <b>before</b> the transmission begins and lasts for <b>the whole transmission</b>.</li>
    <li>Data travels in a <b>continuous stream</b> along the <b>same route</b>; it arrives <b>in order</b> and does not need reassembling.</li>
    <li>The data rate is <b>fixed</b> and the whole bandwidth is available.</li>
  </ul>

  <h2>3 · Benefits and drawbacks</h2>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>The <b>whole bandwidth</b> is available: a steady, high data rate</td><td>The circuit <b>cannot be used by anyone else</b> while it is open, even if it is idle (bandwidth wasted)</td></tr>
    <tr><td>Data arrives in the <b>same order</b> it was sent: no reordering or reassembling delay</td><td><b>Time to set up</b> the circuit before sending can begin</td></tr>
    <tr><td>Suitable for <b>real-time</b> transmission and long continuous communication</td><td><b>No alternative route</b> if there is a fault: the transmission ends</td></tr>
    <tr><td>Data is unlikely to be lost, since it all follows the same path; no waiting at switches</td><td>Less secure: all the data follows one route and can be intercepted. Not flexible and difficult to scale</td></tr>
  </table></div>

  <h2>4 · Where it is appropriate</h2>
  <div class="tw"><table class="t">
    <tr><th>Use</th><th>Why circuit switching suits it</th></tr>
    <tr><td>Standard voice communication (a phone call)</td><td>A dedicated path is needed for the whole call, with the data arriving in real time and in order</td></tr>
    <tr><td>Live video or streaming</td><td>A steady data rate with no delay for reordering</td></tr>
    <tr><td>Private data networks</td><td>The whole bandwidth is reserved and the connection is predictable</td></tr>
  </table></div>
  <div class="tip"><b class="h">Wording for "where and why"</b>"Circuit switching is used where a dedicated path needs to be sustained throughout the communication, or where the whole bandwidth or real-time communication is required, for example voice calls."</div>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Describing circuit switching as "a circuit with wires". It is a <b>dedicated path set up before the data is sent and kept for the whole transmission</b>.</li>
    <li>Giving a benefit and a drawback that are the same point stated twice (for example "dedicated" for both).</li>
    <li>Forgetting that a drawback is the <b>unused bandwidth</b> that cannot be shared.</li>
    <li>Saying the data is split into packets. That is packet switching.</li>
    <li>Writing "it is faster" without saying why: no packets to reorder and the whole bandwidth is reserved.</li>
  </ul>
'''

watch = '''
  <h2>1 · The three phases of a call</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · A busy circuit cannot be shared</h2>
  <div id="stB"></div>
  <h2>3 · A fault ends the call</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Make calls through a small network</h2>
  <p>The network has three separate circuits between the two cities. Each call needs a whole circuit. Start calls and see what happens when all are busy.</p>
  <div class="card"><div id="cS"></div><div class="btnrow"><button class="b pri" id="cN">Start a call</button><button class="b" id="cE">End the longest call</button><button class="b" id="cR">Reset</button></div><div class="verdict" id="cV"></div></div>

  <h2>Lab 2 · Is the circuit being used?</h2>
  <p>A call lasts 10 minutes. Slide to set how long the people are actually talking. The circuit is reserved all 10 minutes.</p>
  <div class="card"><div id="uS"></div><div class="readout"><div><small>Reserved</small><strong id="u1"></strong></div><div><small>Used</small><strong id="u2"></strong></div><div><small>Wasted</small><strong id="u3"></strong></div></div></div>

  <h2>Lab 3 · Benefits and drawbacks</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Circuit switching: true or false?</h2><div id="cl1" class="card"></div>
  <h2>2 · Benefit or drawback?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the phases in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A traditional phone call", "When you dial, a path is set up between the two phones and reserved until you hang up, even during silences.", "circuit switching: a dedicated circuit for the whole communication.") +
rw("A live video link in a broadcast studio", "A dedicated, steady connection delivers the pictures with no waiting for packets to be reordered, which a live broadcast cannot tolerate.", "suitable for real-time transmission with a fixed data rate.") +
rw("A private line between two offices", "A company leases a dedicated connection so the whole bandwidth is always available and the traffic follows a known route.", "dedicated bandwidth: predictable, but not shared.") +
rw("A busy signal", "In the old phone network, if every circuit between two exchanges was in use you got an engaged tone. No other call could use a circuit that was open.", "a drawback: the circuit cannot be shared while it is in use.") +
rw("A call that drops", "If a cable on the route is cut, the call ends, because there is no other route and the circuit has to be set up again.", "no alternative route if there is a fault.")
)

where = [
  ("M/J 2023", "31, 33", "5(a), 5(b)", "2 + 4", "Where circuit switching is appropriate; two benefits and two drawbacks"),
  ("O/N 2024", "31, 33", "3", "3 + 2", "Describe circuit switching; one benefit and one drawback"),
  ("M/J 2025", "32", "4", "4", "Two benefits and two drawbacks of circuit switching")]

past = '''  <p class="note">Circuit switching appears in Paper 3 as a short describe, benefits and drawbacks question. Questions that compare it with packet switching are on the next page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Describing circuit switching</h3>
''' + peq(SRC("w24", "31, 33", "Q3"), "3 + 2 marks", "Describe / State",
  "(a) Describe circuit switching as a method of data transmission. (b) State one benefit and one drawback of circuit switching as a method of data transmission.",
  "(a) dedicated, set up first, kept to the end, one route. (b) a benefit and a drawback, different points.",
  "<p><b>(a)</b> Any three: " + mks(["A dedicated circuit / channel is required", "The circuit is established before the transmission begins", "The circuit lasts for the whole of the transmission and is closed at the end", "Data travels in a continuous stream along the same route", "Transmission is usually bidirectional"]) + "</p><p><b>(b)</b> Benefit (one): " + mks(["No need for data to be reassembled: it arrives in the order it was sent", "Suitable for real-time transmission / a fast data transfer rate", "The whole of the bandwidth is available"], "a") + " Drawback (one): " + mks(["No other transmission can use the circuit while it is in use, so bandwidth can be wasted", "Not secure: all data travels along the same route and can be intercepted", "If there is a problem with the route the transmission ends", "Can take time to set up before transmission starts"], "a") + "</p>", None) + peq(SRC("s23", "31, 33", "Q5(a), (b)"), "2 + 4 marks", "State / Give",
  "(a) State, with a reason, where it would be appropriate to use circuit switching. (b) Give two benefits and two drawbacks of circuit switching.",
  "(a) a use and why: a dedicated path, the whole bandwidth, real time. (b) two of each, in different words.",
  "<p><b>(a)</b> " + mks(["Where a dedicated path needs to be sustained throughout the call, where the whole bandwidth is required, or where real-time communication is used", "A typical application: standard voice communication, video streaming or private data networks"]) + "</p><p><b>(b)</b> Benefits (max 2): " + mks(["The whole of the bandwidth is available", "A dedicated channel increases the quality of transmission", "Data is transmitted at a fixed rate with no waiting time at switches", "Suitable for long continuous communication / better for real time", "Data arrives in the same order and cannot get lost"], "a") + " Drawbacks (max 2): " + mks(["A dedicated connection makes it impossible to transmit other data even if the channel is free", "Not very flexible", "No alternative route in case of failure", "The time to establish the physical link can be too long", "The bandwidth cannot be shared"], "a") + "</p>", "Giving 'it is fast' for a benefit without a reason such as no reordering or the whole bandwidth.") + peq(SRC("s25", "32", "Q4"), "4 marks", "State",
  "Circuit switching may be used as a method of data transmission. State two benefits and two drawbacks of circuit switching.",
  "Two benefits and two drawbacks, each a separate point.",
  "<p>Benefits (max 2): " + mks(["Suitable for long continuous transmission: once connected it is available until the end", "No time lost resending or rearranging packets because packets are not lost or out of order", "A steady, high rate of transmission because the whole bandwidth is available", "Data loss is unlikely because all data follows the same path"]) + " Drawbacks (max 2): " + mks(["Delays because the dedicated connection must be established before transmission can begin", "The dedicated connection cannot be used to transmit any other data", "Resources may be under-used: the bandwidth cannot be shared and may be wasted", "No alternative routes if there is a failure or fault on the line", "Reduced security because of the single path"], "a") + "</p>", None)

review = req("3 marks", "Describe", "Describe how a circuit is used when two people have a phone conversation using circuit switching.", "Set up, use, release.",
  "<p>" + mks(["A dedicated circuit is set up between the two phones before the conversation starts.", "The voice travels as a continuous stream along the same route, in order, using the whole bandwidth.", "The circuit is released when the call ends."]) + "</p>", None) + req("2 marks", "Explain", "Explain why circuit switching wastes bandwidth.", "What happens in a silence?",
  "<p>" + mks(["The circuit is reserved for the whole call and cannot be used by anyone else.", "During pauses nothing is sent, but the unused bandwidth cannot be shared."]) + "</p>", None) + req("2 marks", "State", "State two reasons why circuit switching is suitable for a live video call.", "Delay and order.",
  "<p>" + mks(["The data arrives in the order it was sent, so there is no delay for reassembling.", "The whole bandwidth is reserved, giving a steady data rate."]) + "</p>", None) + req("3 marks", "Give", "Give three drawbacks of circuit switching.", "Setting up, sharing, faults.",
  "<p>" + mks(["It takes time to set up the circuit before sending can begin.", "The circuit cannot be shared, even when it is idle.", "If the route fails the transmission ends: there is no alternative route."]) + "</p>", None) + req("2 marks", "Identify", "A caller hears an engaged tone because all the circuits between two exchanges are in use. Explain how this shows a feature of circuit switching.", "Dedicated, not shared.",
  "<p>" + mks(["Each call needs a whole dedicated circuit.", "While every circuit is in use, no other call can use any of them, so a new call is blocked."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on circuit switching (Paper 3), 2023 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Three words: dedicated, before, whole.", "A dedicated circuit, set up before the data is sent, lasting the whole transmission."),
  ("Same route, same order.", "That is why no reassembly is needed."),
  ("Benefit with a reason.", "Whole bandwidth and no reordering, so a steady real-time stream."),
  ("Drawback with a reason.", "Cannot be shared when idle, set-up time, no alternative route."),
  ("Give an example.", "A telephone call, live video, a private data network."),
  ("Do not mention packets.", "Circuit switching sends a continuous stream."),
], [
  ("what circuit switching is", "Data is sent over a dedicated circuit that is set up before transmission and kept for the whole of it."),
  ("a benefit", "The whole bandwidth is available and data arrives in order, so it suits real-time transmission."),
  ("a drawback", "The circuit cannot be used by anyone else while it is open, even when it is idle."),
  ("where it is used", "Standard voice communication, where a dedicated path is needed throughout."),
], [("State", "Give the fact or use."), ("Describe", "Say how it works, in several points."), ("Give", "Name the benefits or drawbacks."), ("Explain", "Give the reason.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const nodes = [[60, 100, "Caller"], [220, 60, "Switch 1"], [380, 140, "Switch 2"], [540, 60, "Switch 3"], [700, 100, "Receiver"]];
    for (let i = 0; i < 4; i++) o += SV.line(nodes[i][0], nodes[i][1], nodes[i + 1][0], nodes[i + 1][1], k >= 1 && k <= 3 ? "c1" : "dash", { "stroke-width": k >= 1 && k <= 3 ? 5 : 2, ...op(k >= 1 && k <= 3 ? 1 : 0.5) });
    nodes.forEach((n, i) => (o += SV.rect(n[0] - 46, n[1] - 18, 92, 36, i === 0 || i === 4 ? "f2" : "f3", { rx: 8 }) + SV.text(n[0], n[1] + 5, n[2], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })));
    if (k === 1) o += SV.text(30, 200, "1 Set up: a dedicated path is reserved BEFORE any data is sent", "lbl bd t3", { style: "font-size:14px" });
    if (k === 2) o += SV.text(30, 200, "2 Transmit: continuous stream, same route, whole bandwidth, in order", "lbl bd t3", { style: "font-size:14px" });
    if (k === 3) { for (let i = 0; i < 4; i++) o += SV.circle((nodes[i][0] + nodes[i + 1][0]) / 2, (nodes[i][1] + nodes[i + 1][1]) / 2, 7, "dot2"); o += SV.text(30, 200, "data flows along the reserved path", "lbl bd", { style: "font-size:14px" }); }
    if (k === 4) o += SV.text(30, 200, "3 Release: the circuit is closed and can be used by someone else", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "Phases of circuit switching", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "A caller wants to speak to a receiver through three switches.", s: { i: 0 } },
    { cap: "<b>Set up</b>: before any data is sent, a dedicated circuit is established through the switches and reserved.", s: { i: 1 } },
    { cap: "<b>Transmit</b>: the voice travels as a <b>continuous stream</b> along the same route, using the whole bandwidth, and arrives in order.", s: { i: 2 } },
    { cap: "Data flows the whole time the circuit is open, even if the two people are silent.", s: { i: 3 } },
    { cap: "<b>Release</b>: when the call ends the circuit is closed.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(280, 70, 200, 70, "f3", { rx: 8 }) + SV.text(380, 100, "circuit in use by", "lbl", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(380, 125, "call 1", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
    o += SV.rect(30, 80, 170, 50, "f2", { rx: 8 }) + SV.text(115, 111, "Call 1", "lbl bd", { "text-anchor": "middle" }) + SV.line(200, 105, 280, 105, "c1", { "stroke-width": 5 });
    o += SV.rect(30, 150, 170, 50, k >= 1 ? "cell-no" : "cell", { rx: 8 }) + SV.text(115, 181, "Call 2", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M 200 175 C 240 175 250 140 280 130", "c3", { fill: "none", "stroke-width": 3, "stroke-dasharray": "6 4" }) + SV.text(500, 170, "blocked: the circuit is busy", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 2) o += SV.text(500, 110, "even though call 1 is silent", "lbl", { style: "font-size:14px" }) + SV.text(500, 195, "bandwidth cannot be shared", "sm");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "A dedicated circuit cannot be shared", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Call 1 has a dedicated circuit.", s: { i: 0 } },
    { cap: "A second call tries to use the same circuit and is <b>blocked</b>: the circuit is reserved for call 1.", s: { i: 1 } },
    { cap: "Even if call 1 goes quiet, the bandwidth <b>cannot be shared</b>: it is wasted.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const nodes = [[60, 100], [220, 60], [380, 140], [540, 60], [700, 100]];
    for (let i = 0; i < 4; i++) o += SV.line(nodes[i][0], nodes[i][1], nodes[i + 1][0], nodes[i + 1][1], i === 1 && k >= 1 ? "dash" : "c1", { "stroke-width": i === 1 && k >= 1 ? 2 : 5, ...op(i === 1 && k >= 1 ? 0.5 : 1) });
    nodes.forEach((n) => (o += SV.circle(n[0], n[1], 14, "dot1")));
    if (k >= 1) o += SV.text(300, 80, "✗ cable fault", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
    if (k >= 2) o += SV.text(30, 200, "no other route is reserved: the transmission ends and the circuit must be set up again", "lbl bd t2", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "A fault on the route", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The circuit follows one route all the way.", s: { i: 0 } },
    { cap: "A fault occurs on one link of that route.", s: { i: 1 } },
    { cap: "There is <b>no alternative route</b>: the transmission ends. The circuit has to be set up again.", s: { i: 2 } }] });
})();

/* Lab 1 */
(function () {
  let calls, n;
  const reset = () => { calls = []; n = 0; paint("Three circuits are free."); };
  const paint = (msg) => {
    $("#cS").innerHTML = '<div class="tw"><table class="t"><tr><th>Circuit 1</th><th>Circuit 2</th><th>Circuit 3</th></tr><tr>' + [0, 1, 2].map((i) => `<td style="${calls[i] ? "background:var(--warn-soft);font-weight:700" : ""}">${calls[i] ? "Call " + calls[i] + " (using the whole circuit)" : "free"}</td>`).join("") + "</tr></table></div>";
    $("#cV").textContent = msg;
  };
  $("#cN").onclick = () => { n++; if (calls.length >= 3) { paint("Call " + n + " is BLOCKED: all three circuits are busy. Dedicated circuits cannot be shared."); return; } calls.push(n); paint("Call " + n + " gets its own dedicated circuit."); };
  $("#cE").onclick = () => { if (!calls.length) return; const c = calls.shift(); paint("Call " + c + " ends and releases its circuit."); };
  $("#cR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let talk = 4;
  const paint = () => { $("#u1").textContent = "10 min"; $("#u2").textContent = talk + " min"; $("#u3").textContent = 10 - talk + " min (" + (100 - talk * 10) + "%)"; };
  Lib.slider($("#uS"), { id: "uss", label: "Minutes of actual talking ", min: 0, max: 10, value: talk, fmt: (x) => x + " min", onInput: (v) => { talk = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["Whole bandwidth", "Benefit", "The whole bandwidth of the circuit is available: a steady, high data rate", "Real-time communication"],
  ["Data arrives in order", "Benefit", "Everything follows the same route, so no reordering or reassembly is needed", "No delay to put data back in order"],
  ["Cannot be shared", "Drawback", "The circuit is reserved even when idle, and no other transmission can use it", "Wasted bandwidth"],
  ["Set-up time", "Drawback", "The circuit has to be established before sending starts", "A delay before the call connects"],
  ["No alternative route", "Drawback", "If the route fails, the transmission ends", "A call drops if a cable is cut"]
], ["Feature", "Benefit or drawback", "What it means", "Example"]);
''' + CLASSIFY("cl1", "Is this true of circuit switching?", ["True of circuit switching", "Not circuit switching"],
  [("A dedicated circuit is set up before sending", 0), ("Data is split into packets sent by different routes", 1), ("All data follows the same route", 0), ("Packets can arrive out of order", 1), ("The whole bandwidth is reserved", 0), ("Data arrives in the order it was sent", 0)],
  "Dedicated, same route, in order: circuit switching. Packets and different routes: packet switching.") + CLASSIFY("cl2", "Is it a benefit or a drawback of circuit switching?", ["Benefit", "Drawback"],
  [("The whole bandwidth is available", 0), ("The circuit cannot be used by others when idle", 1), ("Data arrives in order", 0), ("It takes time to set up", 1), ("Suitable for real-time transmission", 0), ("No alternative route if a fault occurs", 1)],
  "Benefits: bandwidth, order, real time. Drawbacks: not shared, set-up, no alternative route.") + ORDER(
  "Put the phases of circuit switching in order.",
  ["A dedicated circuit is established between the two ends", "Data is transmitted as a continuous stream along the same route", "The communication ends", "The circuit is released for others to use"],
  "Establish, transmit, end, release.") + MATCH([
  ["Circuit switching", "A dedicated path reserved for the whole communication"], ["Dedicated circuit", "A path used by one communication only"], ["Continuous stream", "Data sent steadily along one route"], ["Real-time", "Data must arrive as it is sent, with no delay"], ["Release", "Closing the circuit at the end"]]) + CALC([
  {"q": "A network has 4 circuits and each call takes one whole circuit. How many calls can be in progress at once?", "a": 4, "unit": "", "tol": 0.01, "hint": "One call per circuit.", "sol": "<b>4</b>."},
  {"q": "5 calls are started on a network with 4 circuits. How many are blocked?", "a": 1, "unit": "", "tol": 0.01, "hint": "5 − 4.", "sol": "<b>1</b>."},
  {"q": "A call lasts 20 minutes and the people talk for 12 minutes. For how many minutes is the circuit idle but still reserved?", "a": 8, "unit": "min", "tol": 0.01, "hint": "20 − 12.", "sol": "<b>8</b> minutes."},
  {"q": "A circuit takes 2 seconds to set up and the data takes 8 seconds to send. What is the total time?", "a": 10, "unit": "s", "tol": 0.01, "hint": "Set-up plus transfer.", "sol": "<b>10</b> seconds."}]) + MCQ([
  ("When is the circuit set up?", ["After the data is sent", "Before any data is sent", "Packet by packet", "Never"], 1, "Before transmission starts."),
  ("Which is a benefit of circuit switching?", ["Bandwidth can be shared", "Data arrives in order", "No set-up time", "Alternative routes"], 1, "All data follows the same route."),
  ("Which is a drawback?", ["The data is reordered", "The circuit cannot be used by others while open", "Packets are lost", "It needs headers"], 1, "It cannot be shared."),
  ("Which is a suitable use?", ["Sending email", "A voice call", "Downloading a web page in pieces", "Sending a large file by many routes"], 1, "A call needs a dedicated path."),
  ("What happens if the route fails?", ["The data takes another route", "The transmission ends", "Packets are resent", "Nothing"], 1, "There is no alternative route.")], "qz1") + CARDS([
  ("Circuit switching", "Dedicated circuit set up before sending, kept for the whole transmission."), ("Route", "The same route for all the data."), ("Bandwidth", "The whole bandwidth is reserved."), ("Benefit", "Steady rate, in order, real time."),
  ("Drawback", "Cannot be shared; set-up time; no alternative route."), ("Use", "Voice calls, live video, private networks."), ("Order", "Data arrives in the order sent."), ("Not", "Not split into packets.")])

build("ac1421", "ac-14-2-1-circuit-switching", "Circuit Switching", EYA("14.2.1"),
  "How a dedicated circuit is set up, used and released, its benefits and drawbacks and where it is used; animations, a call simulator and the real 9618 circuit switching questions.",
  dict(sub=CBK("Chapter 14 · Communication and internet technologies, section 14.2 Circuit switching, packet switching"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
