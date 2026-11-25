"""A Level CS chapter 14 resources: the four TCP/IP layers in real situations (ac141r1) and the 14.1.4 protocols compared (ac141r2).
Run: python3 tools/artifact-kit/mk_ac141res.py"""
from ak20 import *
import mk_ac141 as P   # reuses PRE (shared JS helpers); importing also rebuilds pages 14.1.1 to 14.1.3, which is harmless
import mk_ac1414 as Q   # real protocol questions for resource 2

SUB = P.SUB
mcq = P.mcq
PRE = P.PRE

# ======================================================================= resource 1: the four layers in the real world
learn_r1 = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Every time you load a page, send a message or join a call, the data goes <b>down</b> the four TCP/IP layers on your device, across the network and <b>up</b> the same four layers on the other device. The <b>Application</b> layer is the program you use and the protocol it speaks, the <b>Transport</b> layer cuts the data into numbered packets and makes sure they all arrive, the <b>Internet</b> layer puts the IP addresses on and routes each packet, and the <b>Link</b> layer sends the frames over Wi-Fi, a cable or mobile data to the next device. The layers are not separate machines: they are separate jobs, done by software on your device, by routers on the way, and by the network hardware. This page follows real situations through the layers so you can see each job happen. The exam questions are covered in 14.1.2 and 14.1.3.</p></div>

  <h2>1 · The postal system as a four-layer stack</h2>
  <div class="tw"><table class="t">
    <tr><th>Layer</th><th>In the post</th><th>On the network</th></tr>
    <tr><td><b>Application</b></td><td>You write a letter in a language the reader understands and decide what to say</td><td>A browser or email client creates a message in a protocol such as HTTP or SMTP</td></tr>
    <tr><td><b>Transport</b></td><td>The letter is too big for one envelope, so it is split into numbered parcels so the reader can put them back in order and spot a missing one</td><td>The message is split into packets with sequence numbers; lost ones are sent again</td></tr>
    <tr><td><b>Internet</b></td><td>Each parcel is labelled with the full postal address of the sender and the receiver, and sorting offices decide the route</td><td>Source and destination IP addresses are added; routers choose the route</td></tr>
    <tr><td><b>Link</b></td><td>A van carries the parcel to the next depot, then another van to the next; each van knows only its own stretch of road</td><td>Frames carry the packet across one network segment at a time, using MAC addresses for the next hop</td></tr>
  </table></div>

  <h2>2 · Who does each job</h2>
  <div class="tw"><table class="t">
    <tr><th>Layer</th><th>Where you will find it</th></tr>
    <tr><td><b>Application</b></td><td>The program: Chrome, Outlook, a video call app, an FTP client</td></tr>
    <tr><td><b>Transport</b></td><td>The network software in the operating system of the two end devices (the source host and the destination host)</td></tr>
    <tr><td><b>Internet</b></td><td>The operating system on the two end devices, and every <b>router</b> on the way</td></tr>
    <tr><td><b>Link</b></td><td>The network card or Wi-Fi chip and its driver, the cable or radio link, and each device that passes frames on, such as a switch or a router</td></tr>
  </table></div>

  <h2>3 · Six everyday situations</h2>
  <div class="tw"><table class="t">
    <tr><th>Situation</th><th>Application</th><th>Transport</th><th>Internet</th><th>Link</th></tr>
    <tr><td><b>Loading a web page</b></td><td>HTTP(S) request from the browser</td><td>Numbered packets, lost ones re-sent</td><td>IP addresses of laptop and web server</td><td>Wi-Fi frame to the home router</td></tr>
    <tr><td><b>Sending an email</b></td><td>SMTP from the email client</td><td>Numbered packets, all must arrive</td><td>IP addresses of the PC and the mail server</td><td>Ethernet frame to the office router</td></tr>
    <tr><td><b>Video call</b></td><td>Call app sends audio and video</td><td>Small packets; a late one is skipped rather than re-sent</td><td>IP addresses of both callers</td><td>Wi-Fi frames</td></tr>
    <tr><td><b>Uploading homework by FTP</b></td><td>FTP</td><td>Numbered packets, all must arrive</td><td>IP addresses of the PC and the FTP server</td><td>Ethernet frames</td></tr>
    <tr><td><b>Streaming a film</b></td><td>HTTPS requests for the next piece of video</td><td>Packets in order, lost ones re-sent</td><td>IP addresses of phone and streaming server</td><td>Mobile data frames</td></tr>
    <tr><td><b>Downloading with BitTorrent</b></td><td>BitTorrent asks a peer for piece #17</td><td>Numbered packets</td><td>IP addresses of the two peers</td><td>Wi-Fi frames</td></tr>
  </table></div>
  <div class="tip"><b class="h">Beyond the syllabus</b>Transport protocols include <b>TCP</b>, which re-sends lost packets, and <b>UDP</b>, which does not and is faster. Video calls and games often use UDP because an old frame is no use by the time it is re-sent. The exam asks only about the functions of the layer, not TCP against UDP.</div>

  <h2>4 · What to take from the examples</h2>
  <ul>
    <li>The layers do the <b>same four jobs</b> in every situation. Only the Application protocol and the Link technology change.</li>
    <li>The <b>IP addresses stay the same</b> from your device to the server; the <b>MAC addresses change at every hop</b>.</li>
    <li>When something goes wrong, the symptom usually points to <b>one layer</b>, which is why layering makes faults easier to find.</li>
  </ul>
'''

watch_r1 = '''
  <h2>1 · Follow a message through the layers</h2>
  <p>Choose a situation, then press Play or click the numbered steps.</p>
  <div class="card"><div id="scB" class="btnrow"></div></div>
  <div id="scS"></div>
  <h2>2 · The same journey as a postal delivery</h2>
  <div id="stP"></div>
'''

explore_r1 = '''
  <h2>Lab 1 · The headers for your situation</h2>
  <p>Choose a situation to see what each layer adds, from the message at the top to the frame at the bottom.</p>
  <div class="card"><div id="hB" class="btnrow"></div><div id="hO"></div></div>

  <h2>Lab 2 · Which layer is the problem?</h2>
  <p>Choose a symptom. The symptom usually points to one layer.</p>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>

  <h2>Lab 3 · What each device handles</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
'''

practise_r1 = '''
  <h2>1 · Which layer is involved?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which layer is at fault?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put a web page request in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the real thing to its layer</h2><div id="m1" class="card"></div>
  <h2>5 · Counting packets and hops</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real_r1 = RWNOTE + (
rw("Your home router", "It receives a Wi-Fi frame from your laptop, takes the packet out, reads the destination IP address and sends it on to your internet provider in a new frame. Each router on the route does the same.", "routers work at the Internet layer, and the Link layer builds a new frame for every hop.") +
rw("A smart doorbell", "The doorbell's video goes to a company's server. Its program is the Application layer, its Wi-Fi chip does the Link layer, and the packets use IP addresses like any other traffic. A small gadget needs all four layers too.", "every networked device implements the same stack, however simple it is.") +
rw("Online banking", "The bank's website uses HTTPS. The Application layer is where the secure web protocol lives; the layers below carry the encrypted data without needing to read it.", "the Application layer defines the protocol and can secure the communication, and the layers below do not change.") +
rw("School Wi-Fi", "Hundreds of students share one wireless network. The Link layer decides who sends when and addresses each frame to a device. The same packets then continue across the school's wired network to the internet.", "the Link layer moves frames within the local network segment.") +
rw("A slow download", "If packets are lost, the Transport layer asks for them again, which makes the download take longer even though the browser and the website are working perfectly.", "re-sending of lost packets is a Transport layer job.")
)

review_r1 = req("4 marks", "Explain", "Maya opens a school website on her laptop. Explain what the Transport layer and the Internet layer each do to the data that her browser sends.", "Two points for each layer.",
  "<p>Transport (max 2): " + mks(["It breaks the data into packets.", "It adds a sequence number to the header of each packet so that they can be put back in order (and lost packets re-sent)."]) + " Internet (max 2): " + mks(["It adds a header with the source (her laptop) and destination (the web server) IP addresses.", "It routes the packets by the best route."]) + "</p>", None) + req("2 marks", "Explain", "A home router receives a frame over Wi-Fi and sends the packet to the internet provider. Explain why the router builds a new frame.", "Think about MAC addresses.",
  "<p>" + mks(["The Link layer frame only carries the packet across one local network segment, from one device to the next.", "The MAC addresses are for the next hop, so a new frame with new MAC addresses is needed at each hop; the IP addresses stay the same."]) + "</p>", None) + req("3 marks", "Describe", "A video starts to freeze while streaming because packets are being lost. Describe what the Transport layer could do about it.", "Sequence numbers show what is missing.",
  "<p>" + mks(["It notices from the sequence numbers that a packet is missing.", "It asks for that packet to be sent again.", "It puts the packets in order before passing the data up to the Application layer."]) + "</p>", None) + req("2 marks", "Identify", "A user's laptop shows that it is not connected to any Wi-Fi network. Name the layer most likely to be involved and give a reason.", "No connection means no physical medium.",
  "<p>" + mks(["The Link layer.", "It is the layer that gives access to the physical medium and sends and receives the frames."]) + "</p>", None) + req("3 marks", "Describe", "Describe how the TCP/IP layers are used when an email is sent from one person to another. Do not describe the functions of the individual layers.", "Direction of travel, interfaces and headers, not the jobs.",
  "<p>" + mks(["The message is created at the top (Application) layer of the sender and passes down through the layers.", "Each layer only passes data to the adjacent layer, adding data to the header on the way down.", "It is sent over the network and passes up the layers on the receiving device, with headers removed, until the email program receives it."]) + "</p>", None)

exam_r1 = exam20("Part 1 is real 9618 questions on the four TCP/IP layers (Paper 3), 2022 to 2026. Part 2 is a set of review questions that apply the layers to real situations; they are not in exam format.", P.where3, P.past3, review_r1)

tips_r1 = tips_html([
  ("Use the situation.", "In a scenario question, name the layer and say what it does for that situation, for example 'the Transport layer numbers the packets of the web page'."),
  ("One symptom, one layer.", "Not connected: Link. Wrong or clashing address, no route: Internet. Missing or out-of-order packets: Transport. Error from the website or mail server: Application."),
  ("IP stays, MAC changes.", "A very common mix-up in 'describe a journey' answers."),
  ("Routers are Internet layer devices.", "They also use the Link layer on each side to receive and send frames."),
  ("Same stack everywhere.", "Phones, doorbells, servers and routers all follow the same four layers."),
], [
  ("what the layers do in a real situation", "The Application layer creates the message, the Transport layer numbers the packets, the Internet layer adds the IP addresses and the Link layer sends the frames to the next device."),
  ("which layer is at fault", "A device that cannot connect points to the Link layer; clashing IP addresses point to the Internet layer; missing packets point to the Transport layer."),
], [("Identify", "Name the layer."), ("Explain", "Say what it does, in this situation, and why."), ("Describe", "Say what happens in several points.")]) + FC

js_r1 = PRE + r'''
const SC = [
  { n: "Loading a web page", d: ["HTTPS request: GET /timetable", "Numbered packets #1, #2, #3…", "192.168.1.20 → 203.0.113.10", "Wi-Fi frame: laptop → router"],
    c: ["Maya opens her school's website on her laptop.", "<b>Application:</b> the browser creates an HTTPS request for the timetable page.", "<b>Transport:</b> the reply will be sent as numbered packets; the request is wrapped with a sequence number and port.", "<b>Internet:</b> adds her laptop's IP address (192.168.1.20) and the school server's (203.0.113.10).", "<b>Link:</b> makes a Wi-Fi frame addressed to the home router, the next hop.", "The frames cross the network. Each router makes a new frame for its next hop; the IP addresses stay the same.", "<b>Link</b> on the school server receives the frame.", "<b>Internet:</b> checks the destination IP address is its own and passes the packet up.", "<b>Transport:</b> puts the packets in order using the sequence numbers and asks for any that are missing.", "<b>Application:</b> the web server receives the request and sends back the page, which travels the same four layers in reverse."] },
  { n: "Sending an email", d: ["SMTP: the message text", "Numbered packets, all must arrive", "10.0.0.8 → 198.51.100.25", "Ethernet frame: PC → router"],
    c: ["A teacher sends an email from an office PC.", "<b>Application:</b> the email client uses SMTP to hand the message to the mail server.", "<b>Transport:</b> splits the message into numbered packets and makes sure they all arrive.", "<b>Internet:</b> adds the IP addresses of the PC and the mail server.", "<b>Link:</b> puts each packet in an Ethernet frame to the office router.", "The frames cross the network to the mail server.", "<b>Link:</b> the mail server's network card receives the frames.", "<b>Internet:</b> confirms the destination IP address and passes the packets up.", "<b>Transport:</b> reorders the packets and requests any that are missing.", "<b>Application:</b> the mail server receives the complete message and stores it for the recipient."] },
  { n: "Video call", d: ["Audio and video data", "Small packets; late ones skipped", "192.168.1.20 → 203.0.113.55", "Wi-Fi frames → router"],
    c: ["Two friends start a video call.", "<b>Application:</b> the call app captures audio and video and prepares it for sending.", "<b>Transport:</b> sends small numbered packets quickly. For a live call a late packet is skipped rather than re-sent.", "<b>Internet:</b> adds the IP addresses of both callers.", "<b>Link:</b> sends Wi-Fi frames to the home router.", "The frames cross the network; each router makes a new frame for its next hop.", "<b>Link:</b> the other caller's device receives the frames.", "<b>Internet:</b> confirms the address and passes the packets up.", "<b>Transport:</b> uses the sequence numbers to play packets in order.", "<b>Application:</b> the call app shows the video and plays the sound."] },
  { n: "Uploading homework (FTP)", d: ["FTP: store homework.zip", "Numbered packets, all must arrive", "10.0.0.8 → 192.0.2.40", "Ethernet frame: PC → router"],
    c: ["A student uploads a file to their school's FTP server.", "<b>Application:</b> the FTP client sends the file using the FTP protocol.", "<b>Transport:</b> splits the file into numbered packets and makes sure every one arrives.", "<b>Internet:</b> adds the IP addresses of the PC and the FTP server.", "<b>Link:</b> puts the packets in Ethernet frames for the router.", "The frames cross the network.", "<b>Link:</b> the FTP server's network card receives the frames.", "<b>Internet:</b> passes the packets up after checking the address.", "<b>Transport:</b> reorders the packets and requests any missing ones.", "<b>Application:</b> the FTP server saves the complete file."] },
  { n: "Streaming a film", d: ["HTTPS: next video chunk", "Ordered packets, lost ones re-sent", "203.0.113.80 → 100.64.0.9", "Mobile data frames → phone"],
    c: ["A phone on mobile data streams a film.", "<b>Application:</b> the streaming app asks for the next piece of video over HTTPS.", "<b>Transport:</b> the server's reply is split into numbered packets and lost ones are re-sent.", "<b>Internet:</b> adds the IP addresses of the streaming server and the phone.", "<b>Link:</b> mobile network frames carry the data to the phone.", "The frames cross the internet and the mobile network.", "<b>Link:</b> the phone's radio receives the frames.", "<b>Internet:</b> checks the address and passes the packets up.", "<b>Transport:</b> puts the packets in order and asks for any missing.", "<b>Application:</b> the app buffers the video and plays it."] },
  { n: "BitTorrent download", d: ["BitTorrent: request piece #17", "Numbered packets", "192.168.1.20 → 203.0.113.99", "Wi-Fi frames → router"],
    c: ["A student downloads a large file from other users with BitTorrent.", "<b>Application:</b> the BitTorrent client asks a peer for piece number 17 of the file.", "<b>Transport:</b> splits the request and reply into numbered packets.", "<b>Internet:</b> adds the IP addresses of the two peers (no central web server is involved).", "<b>Link:</b> Wi-Fi frames to the home router.", "The frames cross the internet to the other peer.", "<b>Link:</b> the peer's network card receives the frames.", "<b>Internet:</b> passes the packets up.", "<b>Transport:</b> reorders the packets of the piece.", "<b>Application:</b> the peer's client sends back the piece, and the download client checks and keeps it."] }];
const LN = ["Application", "Transport", "Internet", "Link"], LC = ["f1", "f2", "f3", "f4"];

(function () {
  let cur = 0;
  const make = () => {
    const sc = SC[cur];
    const draw = (s) => {
      const k = Math.round(s.i); let o = SV.text(120, 20, "Sender", "lbl bd", { "text-anchor": "middle" }) + SV.text(640, 20, "Receiver", "lbl bd", { "text-anchor": "middle" });
      const stack = (x, side) => LN.map((n, i) => {
        const active = side === "s" ? k === i + 1 : k === 9 - i, shown = side === "s" ? k >= i + 1 : k >= 9 - i;
        return SV.rect(x, 32 + i * 62, 240, 54, active ? "cell-warn" : LC[i], { rx: 8, ...op(active ? 1 : shown ? 0.85 : 0.4) }) + SV.text(x + 12, 52 + i * 62, n, "lbl bd") + (shown ? SV.text(x + 12, 72 + i * 62, sc.d[i].length > 38 ? sc.d[i].slice(0, 36) + "…" : sc.d[i], "sm", {}) : "");
      }).join("");
      o += stack(0, "s") + stack(520, "r");
      o += SV.line(250, 160, 510, 160, "dash", op(k === 5 ? 1 : 0.3)) + SV.text(380, 152, k === 5 ? "frames cross the network" : "network and routers", "sm", { "text-anchor": "middle" });
      return o;
    };
    Lib.stepper($("#scS"), { w: 760, h: 292, label: sc.n + " through the four layers", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: sc.c.map((cap, i) => ({ cap, s: { i } })) });
  };
  $("#scB").innerHTML = SC.map((s, i) => `<button class="b" data-i="${i}">${s.n}</button>`).join("");
  const sel = () => $$("#scB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
  $$("#scB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; sel(); make(); }));
  sel(); make();
})();

(function () {
  const steps = [
    ["Application", "Write the letter", "You write a letter the reader can understand. This is the message and the language (protocol) it uses."],
    ["Transport", "Split into numbered parcels", "The letter is cut into parcels numbered 1 of 4, 2 of 4 and so on, so the reader can reassemble them and spot a missing one."],
    ["Internet", "Label with the full address", "Every parcel gets the full sender and receiver address. Sorting offices read it and choose the route."],
    ["Link", "Van to the next depot", "A van carries the parcels one stretch of the journey. At the next depot another van takes over."],
    ["Link", "New van, same address", "The van and depot change at every stage but the sender and receiver address on the parcel never does."],
    ["Link", "Arrives at the reader", "The last van delivers the parcels."],
    ["Transport", "Reassemble", "The reader puts the parcels in order using the numbers. If parcel 3 is missing, they ask for it again."],
    ["Application", "Read the letter", "The reader gets the complete letter, exactly as written."]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    LN.forEach((n, i) => (o += SV.rect(20, 20 + i * 52, 150, 42, steps[k][0] === n ? "cell-warn" : LC[i], { rx: 8, ...op(steps[k][0] === n ? 1 : 0.5) }) + SV.text(95, 47 + i * 52, n, "lbl bd", { "text-anchor": "middle" })));
    o += SV.rect(200, 20, 540, 194, "cell", { rx: 10 }) + SV.text(220, 56, steps[k][1], "lbl bd", { style: "font-size:19px" });
    const words = steps[k][2].split(" "); let line = "", y = 90;
    words.forEach((w) => { if ((line + w).length > 62) { o += SV.text(220, y, line, "lbl", {}); y += 26; line = ""; } line += w + " "; });
    o += SV.text(220, y, line, "lbl", {});
    return o;
  };
  Lib.stepper($("#stP"), { w: 760, h: 234, label: "A letter through the post as the four layers", base: { i: 0 }, draw, tween: 1, dwell: 3200, steps: steps.map((s, i) => ({ cap: "<b>" + s[0] + " layer:</b> " + s[1] + ".", s: { i } })) });
})();

(function () {
  let cur = 0;
  const hdr = [["Message", "Application", "The data the program wants to send"], ["Transport header", "Transport", "Sequence number and port, so the packets can be put in order"], ["Internet header", "Internet", "Source and destination IP address, so the packet can be routed"], ["Link header", "Link", "MAC addresses of this hop, to make a frame"]];
  const paint = () => {
    $$("#hB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const sc = SC[cur];
    $("#hO").innerHTML = '<div class="tw"><table class="t"><tr><th>Layer</th><th>What it contributes</th><th>In this situation</th></tr>' + hdr.map((h, i) => `<tr><td><b>${LN[i]}</b></td><td>${h[2]}</td><td>${sc.d[i]}</td></tr>`).join("") + "</table></div>";
  };
  $("#hB").innerHTML = SC.map((s, i) => `<button class="b" data-i="${i}">${s.n}</button>`).join("");
  $$("#hB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); })); paint();
})();

btnTable("fB", "fO", [
  ["Wi-Fi signal lost", "Link", "The device cannot send or receive frames on the physical medium", "No page loads at all"],
  ["404 Not Found", "Application", "The HTTP reply came back, so the network worked; the page does not exist", "A message from the website"],
  ["Two devices with the same IP address", "Internet", "Packets cannot be delivered reliably to a duplicated address", "One device keeps losing its connection"],
  ["Download arrives with chunks missing, then repeats them", "Transport", "Lost packets are noticed by sequence number and re-sent", "A slow download"],
  ["A router has no route to a network", "Internet", "Routing is the Internet layer's job", "Packets never reach that network"],
  ["Mail server rejects a message", "Application", "SMTP, the Application layer protocol, refused the message", "A bounce-back email"],
  ["Ethernet cable unplugged", "Link", "The physical connection has gone", "No connection"]
], ["Symptom", "Layer most likely involved", "Why", "What the user sees"]);

btnTable("dB", "dO", [
  ["Web browser", "Application", "Creates the HTTP request and shows the page"],
  ["Operating system", "Transport and Internet", "Its network software splits data into packets and adds IP addresses"],
  ["Home router", "Internet (and Link)", "Reads the IP address, routes the packet, builds a new frame for the next hop"],
  ["Network switch", "Link", "Passes frames within a local network using MAC addresses"],
  ["Wi-Fi chip or network card", "Link", "Sends and receives the frames over the physical medium"],
  ["Cable or radio link", "Physical medium used by the Link layer", "Carries the signal; it does not look at the data"]
], ["Device", "Layer(s) it works at", "What it does with the data"]);
''' + CLASSIFY("cl1", "Which layer is involved?", ["Application", "Transport", "Internet", "Link"],
  [("Chrome sends an HTTP request", 0), ("A packet's sequence number is checked", 1), ("A router reads the destination IP address", 2), ("The Wi-Fi chip sends a frame", 3), ("An email client uses SMTP", 0), ("A lost packet is requested again", 1), ("A new frame is made for the next hop", 3), ("Choosing the best route", 2)],
  "Programs and protocols: Application. Numbers and re-sending: Transport. IP and routing: Internet. Frames, MAC and the medium: Link.") + CLASSIFY("cl2", "Which layer is the likely cause?", ["Application", "Transport", "Internet", "Link"],
  [("The Wi-Fi is switched off", 3), ("The website returns 404 Not Found", 0), ("Two devices share one IP address", 2), ("Packets are missing and are re-sent, slowing a download", 1), ("The Ethernet cable is unplugged", 3), ("A router has no route to the destination", 2), ("The mail server refuses an email", 0), ("A file arrives with pieces out of order", 1)],
  "The symptom points to one layer: Link, Application, Internet or Transport.") + ORDER(
  "Put a web page request in order as it is sent.",
  ["The browser creates an HTTP request", "The message is split into numbered packets", "IP addresses are added to each packet", "Each packet is put into a frame and sent over Wi-Fi"],
  "Application, Transport, Internet, Link.") + MATCH([
  ["Chrome", "Application layer"], ["Sequence number", "Transport layer"], ["203.0.113.10 (an IP address)", "Internet layer"], ["Wi-Fi chip", "Link layer"], ["Router (routing)", "Internet layer"], ["Frame", "Link layer"]]) + CALC([
  {"q": "A 3 MB photo (3 000 000 bytes) is split into packets of 1500 bytes. How many packets?", "a": 2000, "unit": "", "tol": 0.01, "hint": "3 000 000 ÷ 1500.", "sol": "<b>2000</b>."},
  {"q": "A video call sends 50 packets every second. How many packets in a 2-minute call?", "a": 6000, "unit": "", "tol": 0.01, "hint": "50 × 120.", "sol": "<b>6000</b>."},
  {"q": "A packet crosses 4 routers between a laptop and a server. How many separate frames are made for the journey?", "a": 5, "unit": "", "tol": 0.01, "hint": "Laptop to router 1, then 1 to 2, 2 to 3, 3 to 4, 4 to server.", "sol": "<b>5</b>."},
  {"q": "A message is split into 12 packets and 3 are lost and re-sent. How many packet transmissions in total?", "a": 15, "unit": "", "tol": 0.01, "hint": "12 + 3.", "sol": "<b>15</b>."},
  {"q": "In the 4-router journey above, how many times does the destination IP address change?", "a": 0, "unit": "", "tol": 0.01, "hint": "It stays the same from end to end.", "sol": "<b>0</b>. It never changes."}]) + mcq([
  ("A router mainly works at which layer?", ["Application", "Transport", "Internet", "Link"], 2, "It reads IP addresses and routes packets."),
  ("Your laptop has no Wi-Fi signal. Which layer is most likely involved?", ["Application", "Transport", "Internet", "Link"], 3, "The Link layer gives access to the medium."),
  ("What changes at every hop?", ["The destination IP address", "The MAC addresses of the frame", "The sequence numbers", "The web page"], 1, "MAC addresses are for the next hop."),
  ("In the postal analogy, numbering the parcels is like...", ["the Application layer", "the Transport layer", "the Internet layer", "the Link layer"], 1, "Sequence numbers are the Transport layer."),
  ("A video call app is part of which layer?", ["Application", "Transport", "Internet", "Link"], 0, "The program is the Application layer."),
  ("Which statement is true?", ["Only computers use the stack", "Phones, routers and doorbells all use the same layers", "Only the Link layer is needed for the internet", "Each layer talks to every other layer"], 1, "Every networked device uses the stack.")]) + CARDS([
  ("Application", "The program and the protocol it speaks."), ("Transport", "Numbered packets, re-sending, reordering."), ("Internet", "IP addresses and routing."), ("Link", "Frames and the physical medium, hop by hop."),
  ("IP address", "Stays the same for the whole journey."), ("MAC address", "Changes at every hop."), ("Router", "Reads the IP address and routes; makes new frames."), ("Fault finding", "A symptom usually points to one layer.")])

# ======================================================================= resource 2: the application protocols compared
learn_r2 = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The six protocols in 14.1.4 are easy to mix up, so this page puts them side by side and gives you questions to ask that separate them. First, is it <b>email</b>? If it is, <b>SMTP sends</b>, while <b>POP3 and IMAP receive</b>: POP3 downloads the message to one device and normally removes it from the server, IMAP leaves it on the server so every device stays in sync. If it is not email, <b>HTTP(S)</b> transfers web pages, <b>FTP</b> transfers files to and from a server, and <b>BitTorrent</b> shares a file <b>peer to peer</b> in pieces with no central server holding it. All six belong to the <b>Application layer</b>. Use the decision path and the confusions table below, then test yourself.</p></div>

  <h2>1 · The six side by side</h2>
  <div class="tw"><table class="t">
    <tr><th>Protocol</th><th>Stands for</th><th>Used to</th><th>Model</th><th>Everyday example</th></tr>
    <tr><td><b>HTTP / HTTPS</b></td><td>Hypertext Transfer Protocol (S = secure)</td><td>Transfer web pages (hypertext documents) between a server and a browser</td><td>Client and server</td><td>Opening a website</td></tr>
    <tr><td><b>FTP</b></td><td>File Transfer Protocol</td><td>Send and receive files over a network</td><td>Client and server</td><td>Uploading a website's files to hosting</td></tr>
    <tr><td><b>SMTP</b></td><td>Simple Mail Transfer Protocol</td><td><b>Send</b> email to a mail server and between mail servers</td><td>Push</td><td>Pressing Send in an email client</td></tr>
    <tr><td><b>POP3</b></td><td>Post Office Protocol, version 3</td><td><b>Receive</b> email by downloading it from the server</td><td>Pull</td><td>An old desktop email program collecting mail</td></tr>
    <tr><td><b>IMAP</b></td><td>Internet Message Access Protocol</td><td><b>Receive</b> email, leaving it on the server, in sync across devices</td><td>Pull</td><td>Reading the same inbox on a phone and a laptop</td></tr>
    <tr><td><b>BitTorrent</b></td><td>(a name, not an abbreviation)</td><td>Share a large file peer to peer, in pieces</td><td>Peer to peer</td><td>Downloading a large file from many other users</td></tr>
  </table></div>

  <h2>2 · A decision path</h2>
  <ol>
    <li><b>Is it email?</b> If yes: is it <b>sending</b>? Use <b>SMTP</b>. Is it <b>receiving</b>? Does the mail need to stay on the server, and be read from several devices? <b>IMAP</b>. Is it downloaded to one device and removed from the server? <b>POP3</b>.</li>
    <li><b>Is it a web page in a browser?</b> <b>HTTP(S)</b>.</li>
    <li><b>Is it a file moved to or from a server?</b> <b>FTP</b>.</li>
    <li><b>Is it a large file shared among many users with no central server holding it?</b> <b>BitTorrent</b>.</li>
  </ol>

  <h2>3 · The confusions, one at a time</h2>
  <div class="tw"><table class="t">
    <tr><th>Often confused</th><th>The difference</th></tr>
    <tr><td><b>SMTP and POP3 / IMAP</b></td><td>SMTP is for <b>sending</b> and pushes mail towards its destination. POP3 and IMAP are for <b>receiving</b> and pull mail from the server</td></tr>
    <tr><td><b>POP3 and IMAP</b></td><td>POP3 downloads to the device and by default removes the message from the server; IMAP leaves it on the server and keeps all devices in sync</td></tr>
    <tr><td><b>HTTP and FTP</b></td><td>HTTP transfers <b>web pages</b> for a browser to display; FTP transfers <b>files</b> between devices, in either direction</td></tr>
    <tr><td><b>FTP and BitTorrent</b></td><td>FTP gets a file from <b>one server</b>; BitTorrent gets pieces from <b>many peers</b> with no central server holding the file</td></tr>
    <tr><td><b>HTTP and HTTPS</b></td><td>Same job; the S means the communication is secured (encrypted)</td></tr>
  </table></div>

  <h2>4 · BitTorrent words</h2>
  <ul>
    <li>A <b>peer</b> is a user sharing and downloading pieces; the <b>swarm</b> is all the peers sharing one file.</li>
    <li>A <b>seed</b> has the whole file and shares it. A <b>tracker</b> holds data about the peers in the swarm.</li>
    <li>The file is split into <b>pieces</b>; each peer collects pieces from several others and passes on the ones it has.</li>
  </ul>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Naming <b>SMTP</b> for receiving email, or <b>POP3</b> for sending it.</li>
    <li>Writing that IMAP "downloads" the email. It leaves the message on the server.</li>
    <li>Describing BitTorrent as "downloading from a server". There is no central server holding the file.</li>
    <li>Saying HTTP is "for the internet". Be specific: it transfers web pages (hypertext documents).</li>
    <li>Describing which layer the protocols belong to wrongly. All six are Application layer protocols.</li>
  </ul>
'''

watch_r2 = '''
  <h2>1 · Sending then receiving: push and pull</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stM"></div>
  <h2>2 · POP3 against IMAP with three devices</h2>
  <div id="stI"></div>
  <h2>3 · One server against a swarm</h2>
  <div id="stS"></div>
'''

explore_r2 = '''
  <h2>Lab 1 · Which protocol?</h2>
  <p>Answer the questions to reach a protocol.</p>
  <div class="card"><div id="tree"></div></div>

  <h2>Lab 2 · Compare any two</h2>
  <p>Pick two protocols and see where they are the same and where they differ.</p>
  <div class="card"><div id="cmp"></div></div>

  <h2>Lab 3 · POP3 or IMAP: what happens to your mailbox?</h2>
  <div class="card"><div id="pi"></div></div>
'''

practise_r2 = '''
  <h2>1 · Which protocol?</h2><div id="cl1" class="card"></div>
  <h2>2 · Sending or receiving?</h2><div id="cl2" class="card"></div>
  <h2>3 · Client and server, or peer to peer?</h2><div id="cl3" class="card"></div>
  <h2>4 · Put an email's journey in order</h2><div id="o1" class="card"></div>
  <h2>5 · Match the protocol to its job</h2><div id="m1" class="card"></div>
  <h2>6 · Pieces, devices and messages</h2><div id="c1"></div>
  <h2>7 · Multiple choice</h2><div id="qz1"></div>
'''

real_r2 = RWNOTE + (
rw("A school reports portal", "Parents open a link and see their child's report in a browser. The page and the login form travel by HTTPS, which keeps the details secure.", "HTTP(S) transfers web pages; the S means secure.") +
rw("Uploading a website", "A designer uses an FTP program to send the website's files to the hosting company's server, and later downloads them again to make changes.", "FTP sends and receives files over a network, in either direction.") +
rw("A phone and a laptop, one inbox", "An email read on the phone is shown as read on the laptop. Both are using IMAP to look at the same copy on the mail server.", "IMAP leaves the mail on the server and keeps every device in sync.") +
rw("An old desktop mail program", "A program set to use POP3 collects the mail onto the computer and removes it from the server. Another device would not see those messages.", "POP3 downloads the message and normally removes it from the server.") +
rw("Sharing a large file", "A game developer shares a large file via BitTorrent so thousands of users download pieces from each other, which stops one server from being overloaded.", "BitTorrent is peer to peer: no central server holds the file; users share pieces.")
)

review_r2 = req("1 mark", "Identify", "Name the protocol used by an email client to send a message to a mail server.", "Sending: SMTP.", "<p>" + mks(["SMTP (Simple Mail Transfer Protocol)"]) + "</p>", None) + req("3 marks", "Describe", "A user reads the same email on a phone, a tablet and a laptop. Name the protocol and describe how it makes this possible.", "Name it, then say where the message lives.",
  "<p>" + mks(["IMAP"]) + " " + mks(["The email is kept on the mail server and not removed from it.", "Each device shows the server's copy, so all stay in sync."]) + "</p>", None) + req("2 marks", "Distinguish", "Explain one difference between POP3 and IMAP.", "Where is the message afterwards?",
  "<p>" + mks(["POP3 downloads the message to the device and normally removes it from the server.", "IMAP leaves it on the server and keeps all the user's devices in sync."]) + "</p>", None) + req("3 marks", "Describe", "Describe how BitTorrent allows a large file to be shared among many users.", "Pieces, peers, no central server.",
  "<p>" + mks(["The file is split into pieces.", "Users (peers) download pieces from several other peers at once and share the pieces they have, forming a swarm.", "No central server holds the file; a tracker holds data about the peers."]) + "</p>", None) + req("2 marks", "Explain", "A web designer needs to upload 200 files to a web host. Name the most suitable protocol and give one reason.", "Which protocol is for files?",
  "<p>" + mks(["FTP", "It is designed for sending and receiving files over a network, so many files can be transferred to the server."]) + "</p>", None) + req("2 marks", "Identify", "State the layer of the TCP/IP suite to which all six protocols HTTP, FTP, SMTP, POP3, IMAP and BitTorrent belong.", "The one the user's programs use.", "<p>" + mks(["The Application layer"]) + "</p>", None)

exam_r2 = exam20("Part 1 is real 9618 questions on the Application layer protocols (Paper 3), 2022 to 2025. Part 2 is a set of review questions that separate the six protocols; they are not in exam format.", Q.where, Q.past.replace("The TCP/IP layers themselves are on the previous page. ", ""), review_r2)

tips_r2 = tips_html([
  ("Sending or receiving?", "SMTP sends. POP3 and IMAP receive. Say which in your answer."),
  ("Where does the mail end up?", "POP3: on the device, removed from the server. IMAP: stays on the server, every device in sync."),
  ("Is there a central server?", "HTTP and FTP: yes, a server. BitTorrent: no, peers share pieces."),
  ("Be specific about HTTP.", "It transfers web pages (hypertext documents). The S means secure."),
  ("All six are Application layer protocols.", "They are what programs use to exchange data."),
], [
  ("what HTTP is used for", "HTTP is used to transfer web pages from a web server to a browser."),
  ("what POP3 does", "POP3 downloads email from the mail server to the device, normally removing it from the server."),
  ("what IMAP does", "IMAP lets the user read email on any device, leaving it on the server so all devices stay in sync."),
  ("what BitTorrent does", "BitTorrent shares a file peer to peer: the file is split into pieces that peers download from each other."),
], [("Name / Identify", "Give the protocol."), ("State", "Give the purpose briefly."), ("Describe", "Say what it does, in several points."), ("Distinguish", "Say how two things differ.")]) + FC

js_r2 = PRE + "const PROT = [];\n" + r'''
PROT.push(...[
  ["HTTP(S)", "Web pages", "Client and server", "A web page", "Pull (the browser asks)", "Stays on the server", "Opening a website"],
  ["FTP", "Files", "Client and server", "Files, in either direction", "Client uploads or downloads", "Stays on the server unless deleted", "Uploading a website's files"],
  ["SMTP", "Sending email", "Client to server, server to server", "An outgoing email", "Push", "Delivered onward to the recipient's server", "Pressing Send"],
  ["POP3", "Receiving email", "Client and server", "Mail downloaded to the device", "Pull", "Normally removed from the server", "A desktop mail program"],
  ["IMAP", "Receiving email", "Client and server", "Mail viewed on any device", "Pull", "Stays on the server", "A phone and laptop in sync"],
  ["BitTorrent", "Peer-to-peer file sharing", "Peers, no central server", "Pieces of a file", "Pieces from many peers", "Each peer keeps and shares its pieces", "Downloading a large file"]]);
const PH = ["Protocol", "Used for", "Model", "Carries", "Push or pull", "Where the data ends up", "Example"];

(function () {
  const A = [["Email client", 20], ["Sender's server", 215], ["Recipient's server", 410], ["Recipient's client", 610]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    A.forEach((a, i) => (o += SV.rect(a[1], 50, 130, 50, i === 0 || i === 3 ? "f1" : "f3", { rx: 8, ...op(0.8) }) + SV.text(a[1] + 65, 80, a[0], "sm bd", { "text-anchor": "middle" })));
    const seg = (i, lbl, cls, a, b, v) => { const x1 = A[a][1] + 130, x2 = A[b][1]; return k >= v ? (x2 > x1 ? arrow(x1, 75, x2, 75, "r", cls, 1) : arrow(A[a][1], 75, A[b][1] + 110, 75, "l", cls, 1)) + SV.text((x1 + x2) / 2, 66, lbl, "sm bd", { "text-anchor": "middle", ...halo }) : ""; };
    o += seg(0, "SMTP", "c1", 0, 1, 1) + seg(1, "SMTP", "c1", 1, 2, 2);
    if (k >= 3) o += SV.rect(410, 110, 130, 34, "cell-ok", { rx: 6 }) + SV.text(475, 133, "mailbox", "sm", { "text-anchor": "middle" });
    if (k >= 4) o += arrow(610, 150, 540, 150, "l", "c3", 1) + SV.text(575, 168, "asks for mail", "sm", { "text-anchor": "middle" });
    if (k >= 5) o += arrow(540, 128, 610, 128, "r", "c3", 1) + SV.text(575, 120, "POP3 / IMAP", "sm bd", { "text-anchor": "middle", ...halo });
    o += SV.text(30, 200, k <= 2 ? "SMTP pushes the message towards its destination" : k >= 4 ? "POP3 and IMAP pull the message from the server" : "The message waits in the recipient's mailbox", "lbl bd", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stM"), { w: 760, h: 215, label: "SMTP sends, POP3 and IMAP receive", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "A user has written an email and presses Send.", s: { i: 0 } },
    { cap: "The email client uses <b>SMTP</b> to push the message to the sender's mail server.", s: { i: 1 } },
    { cap: "That server uses <b>SMTP</b> to push it on to the recipient's mail server.", s: { i: 2 } },
    { cap: "The message sits in the recipient's <b>mailbox</b> on their mail server.", s: { i: 3 } },
    { cap: "Later the recipient's client <b>asks</b> the server for new mail. This is a <b>pull</b>.", s: { i: 4 } },
    { cap: "<b>POP3</b> or <b>IMAP</b> delivers the message to the client.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const dev = (x, y, n, got, gone) => SV.rect(x, y, 76, 40, got ? "cell-ok" : "cell", { rx: 8 }) + SV.text(x + 38, y + 25, n + (got ? " ✓" : ""), "sm bd", { "text-anchor": "middle" });
    const side = (x, title, mode) => {
      let t = SV.text(x + 120, 20, title, "lbl bd", { "text-anchor": "middle" });
      t += SV.rect(x + 45, 40, 150, 46, k >= 1 && !(mode === "pop" && k >= 2) ? "cell-warn" : "cell", { rx: 8 }) + SV.text(x + 120, 68, k >= 1 && !(mode === "pop" && k >= 2) ? "Server: 1 message" : "Server: empty", "sm bd", { "text-anchor": "middle" });
      const have = (i) => mode === "imap" ? k >= 2 : k >= 2 && i === 0;
      ["Phone", "Tablet", "Laptop"].forEach((n, i) => (t += SV.line(x + 120, 86, x + 43 + i * 80, 130, "ax", op(k >= 2 ? 0.9 : 0.25)) + dev(x + 5 + i * 80, 130, n, have(i))));
      return t;
    };
    return side(20, "POP3", "pop") + side(400, "IMAP", "imap");
  };
  Lib.stepper($("#stI"), { w: 760, h: 190, label: "POP3 and IMAP with three devices", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "The user has three devices and no new mail.", s: { i: 0 } },
    { cap: "A message arrives on the mail server.", s: { i: 1 } },
    { cap: "<b>POP3</b>: the first device that checks downloads the message and, by default, it is <b>removed from the server</b>, so only that device has it. <b>IMAP</b>: the message <b>stays on the server</b> and all three devices show it.", s: { i: 2 } }] });
})();

(function () {
  const peers = [[400, 40], [560, 90], [560, 190], [400, 240], [240, 190], [240, 90]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    if (k <= 1) { o += SV.rect(30, 110, 110, 60, "f2", { rx: 10, ...op(0.8) }) + SV.text(85, 145, "Server", "lbl bd", { "text-anchor": "middle" }); [[290, 30], [290, 100], [290, 170], [290, 240]].forEach((c, i) => (o += SV.rect(c[0], c[1], 100, 36, "f1", { rx: 8, ...op(0.8) }) + SV.text(c[0] + 50, c[1] + 24, "Client " + (i + 1), "sm bd", { "text-anchor": "middle" }) + (k === 1 ? arrow(140, 140, c[0], c[1] + 18, "r", "c1", 1) : ""))); o += SV.text(430, 150, k === 1 ? "Everyone downloads from one server" : "One server holds the file", "lbl bd", { style: "font-size:14px" }); }
    else { peers.forEach((p, i) => peers.forEach((q, j) => { if (j > i && (k === 3 || (j - i) % 2 === 1)) o += SV.line(p[0] + 20, p[1] + 20, q[0] + 20, q[1] + 20, "c3", { "stroke-width": 1.8, ...op(0.6) }); })); peers.forEach((p, i) => (o += SV.circle(p[0] + 20, p[1] + 20, 24, i === 0 ? "dot4" : "dot1", op(0.9)) + SV.text(p[0] + 20, p[1] + 25, i === 0 ? "Seed" : "Peer", "sm bd", { "text-anchor": "middle", style: "fill:#fff" }))); o += SV.text(30, 130, k === 2 ? "A seed holds the whole file" : "Peers swap pieces", "lbl bd", { style: "font-size:14px" }); if (k === 3) o += SV.text(30, 156, "No central server holds the file", "sm"); }
    return o;
  };
  Lib.stepper($("#stS"), { w: 760, h: 285, label: "Client and server compared with a BitTorrent swarm", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "<b>HTTP and FTP</b> are client and server: a central server holds the file.", s: { i: 0 } },
    { cap: "Every client downloads from the same server, so that server carries the whole load.", s: { i: 1 } },
    { cap: "<b>BitTorrent</b>: the file is split into pieces. A <b>seed</b> has the whole file, and a <b>tracker</b> tells peers who else is in the swarm.", s: { i: 2 } },
    { cap: "Each <b>peer</b> downloads pieces from several others and passes on the pieces it has. There is <b>no central server</b> holding the file.", s: { i: 3 } }] });
})();

(function () {
  const T = {
    q0: { q: "Is it email?", y: "q1", n: "q2" }, q1: { q: "Is the message being sent?", y: "SMTP", n: "q3" }, q3: { q: "Must the message stay on the server so several devices see it?", y: "IMAP", n: "POP3" },
    q2: { q: "Is it a web page shown in a browser?", y: "HTTP(S)", n: "q4" }, q4: { q: "Is the file shared by many users with no central server holding it?", y: "BitTorrent", n: "FTP" } };
  const WHY = { "SMTP": "SMTP sends email and pushes it towards its destination.", "IMAP": "IMAP leaves mail on the server so every device stays in sync.", "POP3": "POP3 downloads mail to one device and normally removes it from the server.", "HTTP(S)": "HTTP(S) transfers web pages between a web server and a browser.", "BitTorrent": "BitTorrent shares pieces of a file peer to peer, with no central server holding it.", "FTP": "FTP sends and receives files between a client and a server." };
  let path = ["q0"];
  const paint = () => {
    const cur = path[path.length - 1], t = T[cur];
    $("#tree").innerHTML = t ? `<p><b>${t.q}</b></p><div class="btnrow"><button class="b" data-a="y">Yes</button><button class="b" data-a="n">No</button><button class="b" data-a="r">Start again</button></div>` : `<div class="verdict ok"><b>${cur}</b>: ${WHY[cur]}</div><div class="btnrow"><button class="b" data-a="r">Start again</button></div>`;
    $$("#tree button").forEach((b) => (b.onclick = () => { const a = b.dataset.a; if (a === "r") path = ["q0"]; else path.push(T[cur][a]); paint(); }));
  };
  paint();
})();

(function () {
  let a = 0, b = 1;
  const opt = (id, v) => `<select id="${id}">${PROT.map((p, i) => `<option value="${i}"${i === v ? " selected" : ""}>${p[0]}</option>`).join("")}</select>`;
  const paint = () => {
    $("#cmp").innerHTML = `<p>${opt("cA", a)} against ${opt("cB", b)}</p><div class="tw"><table class="t"><tr><th></th><th>${PROT[a][0]}</th><th>${PROT[b][0]}</th><th></th></tr>` + PH.slice(1).map((h, i) => `<tr><td><b>${h}</b></td><td>${PROT[a][i + 1]}</td><td>${PROT[b][i + 1]}</td><td>${PROT[a][i + 1] === PROT[b][i + 1] ? "same" : "differs"}</td></tr>`).join("") + "</table></div>";
    $("#cA").onchange = (e) => { a = +e.target.value; paint(); }; $("#cB").onchange = (e) => { b = +e.target.value; paint(); };
  };
  paint();
})();

(function () {
  let dev = 3;
  const paint = () => {
    $("#pi").innerHTML = `<div id="piS"></div><div class="tw"><table class="t"><tr><th></th><th>POP3 (default)</th><th>IMAP</th></tr><tr><td><b>Devices that can read a new message</b></td><td id="pa"></td><td id="pb"></td></tr><tr><td><b>Copies kept on the server</b></td><td>0</td><td>1</td></tr></table></div>`;
    Lib.slider($("#piS"), { id: "dv", label: "Number of devices: ", min: 1, max: 6, value: dev, onInput: (n) => { dev = n; $("#pa").textContent = "1 (the first to download it)"; $("#pb").textContent = n + " (all of them)"; } });
  };
  paint();
})();
''' + CLASSIFY("cl1", "Which protocol is described?", ["HTTP(S)", "FTP", "SMTP", "POP3", "IMAP", "BitTorrent"],
  [("Transfers web pages to a browser", 0), ("Sends files to a web host", 1), ("Sends an email", 2), ("Downloads mail to one device and removes it from the server", 3), ("Reads the same inbox on a phone and a laptop", 4), ("Shares a large file in pieces among many users", 5), ("Delivers mail between mail servers", 2), ("Uses a tracker and seeds", 5)],
  "Web pages: HTTP(S). Files: FTP. Sending mail: SMTP. Downloading: POP3. In sync: IMAP. Peer to peer: BitTorrent.") + CLASSIFY("cl2", "Is the protocol used for sending or for receiving email?", ["Sending email", "Receiving email"],
  [("SMTP", 0), ("POP3", 1), ("IMAP", 1), ("Pushes mail towards its destination", 0), ("Pulls mail from the mail server", 1), ("Passes mail from one mail server to another", 0)],
  "SMTP sends. POP3 and IMAP receive.") + CLASSIFY("cl3", "Client and server, or peer to peer?", ["Client and server", "Peer to peer"],
  [("HTTP", 0), ("FTP", 0), ("BitTorrent", 1), ("Pieces come from many other users", 1), ("A central server holds the file", 0), ("A swarm of peers", 1)],
  "HTTP and FTP use a server. BitTorrent shares pieces between peers.") + ORDER(
  "Put the journey of an email in order.",
  ["The sender's client pushes the message to its mail server with SMTP", "That mail server passes it to the recipient's mail server with SMTP", "The recipient's mail server stores it in their mailbox", "The recipient's client retrieves it with POP3 or IMAP"],
  "Client, server, server, mailbox, retrieve.") + MATCH([
  ["HTTP", "Transferring hypertext documents"], ["FTP", "Sending and receiving files"], ["SMTP", "Sending email"], ["POP3", "Downloading email from a server"], ["IMAP", "Reading email on any device, in sync"], ["BitTorrent", "Peer-to-peer file sharing"]]) + CALC([
  {"q": "A file is split into 40 equal pieces and a peer has 25. How many more pieces does it need?", "a": 15, "unit": "", "tol": 0.01, "hint": "40 − 25.", "sol": "<b>15</b>."},
  {"q": "A 900 MB file is shared in pieces of 3 MB. How many pieces?", "a": 300, "unit": "", "tol": 0.01, "hint": "900 ÷ 3.", "sol": "<b>300</b>."},
  {"q": "A user has 4 devices and uses IMAP. On how many devices can they read the same message?", "a": 4, "unit": "", "tol": 0.01, "hint": "All of them.", "sol": "<b>4</b>."},
  {"q": "A user has 4 devices and uses POP3 with default settings. On how many devices will a message be downloaded?", "a": 1, "unit": "", "tol": 0.01, "hint": "The first to download it.", "sol": "<b>1</b>."},
  {"q": "An email passes from a client to its server and then to the recipient's server using SMTP. How many SMTP transfers?", "a": 2, "unit": "", "tol": 0.01, "hint": "Client to server, server to server.", "sol": "<b>2</b>."}]) + mcq([
  ("Which protocol is used to send email?", ["POP3", "IMAP", "SMTP", "FTP"], 2, "SMTP."),
  ("Which protocol lets you read mail on any device and leaves it on the server?", ["IMAP", "SMTP", "HTTP", "FTP"], 0, "IMAP."),
  ("Which protocol normally removes mail from the server after downloading?", ["IMAP", "POP3", "SMTP", "HTTP"], 1, "POP3."),
  ("What does HTTP transfer?", ["Email", "Web pages", "Peer-to-peer files", "MAC addresses"], 1, "Hypertext documents."),
  ("Which protocol sends and receives files to and from a server?", ["FTP", "SMTP", "POP3", "HTTP"], 0, "FTP."),
  ("In BitTorrent there is...", ["a central server holding the file", "no central server holding the file", "only one source", "no peers"], 1, "Peer to peer."),
  ("To which layer of the TCP/IP suite do all six belong?", ["Application", "Transport", "Internet", "Link"], 0, "Application."),
  ("A peer with the complete file that keeps sharing it is called...", ["a tracker", "a seed", "a router", "a swarm"], 1, "A seed.")]) + CARDS([
  ("HTTP(S)", "Web pages; S = secure."), ("FTP", "Sending and receiving files."), ("SMTP", "Sending email (push)."), ("POP3", "Receiving email; downloaded, removed from the server."),
  ("IMAP", "Receiving email; stays on the server, any device in sync."), ("BitTorrent", "Peer to peer file sharing in pieces."), ("Seed", "A peer with the whole file that shares it."), ("Tracker", "Holds data about the peers in the swarm.")])


def go(bundle, slug, title, lead, tabset, js):
    build(bundle, slug, title, EYA("14.1") + " · Resource", lead, dict(sub=SUB, **tabs(*tabset)), js)


go("ac141r1", "ac-14-1-four-layers-in-the-real-world", "The Four Layers in the Real World",
   "Follow a web page, an email, a video call, an FTP upload, a film and a BitTorrent download through Application, Transport, Internet and Link, with a postal analogy, a fault finder and practice.",
   (learn_r1, watch_r1, explore_r1, practise_r1, real_r1, exam_r1, tips_r1), js_r1)
go("ac141r2", "ac-14-1-protocols-compared", "HTTP, FTP, SMTP, POP3, IMAP and BitTorrent Compared",
   "Tell the six application layer protocols apart: what each is for, push against pull, client and server against peer to peer, and POP3 against IMAP; a decision path, side-by-side comparison and practice.",
   (learn_r2, watch_r2, explore_r2, practise_r2, real_r2, exam_r2, tips_r2), js_r2)
