"""AS CS syllabus 2.1.4: the internet and the WWW, bit streaming, internet hardware. Run: python3 tools/artifact-kit/mk_as214.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>internet</b> is the worldwide network of networks: the physical infrastructure of cables, routers and servers that carries data. The <b>World Wide Web (WWW)</b> is one service that runs on the internet: a collection of web pages and resources found with URLs and viewed in a browser; email, file transfer and streaming also use the internet. <b>Bit streaming</b> sends audio or video as a continuous flow of bits that is played as it arrives, using a <b>buffer</b> on the receiving device and <b>compression</b> to cut the bandwidth needed; it is <b>real-time</b> when live (a video call) and <b>on-demand</b> when a stored file is played whenever you choose. The speed of the connection (the <b>bit rate</b> or broadband speed) decides whether it plays smoothly or keeps stopping to buffer. The internet is reached with hardware such as <b>modems</b>, the <b>PSTN</b>, <b>dedicated lines</b>, the <b>cell phone network</b> and <b>routers</b>.</p></div>

  <h2>1 · The internet and the World Wide Web</h2>
  <div class="tw"><table class="t">
    <tr><th>Internet</th><th>World Wide Web (WWW)</th></tr>
    <tr><td>A global <b>network of networks</b>: the hardware and infrastructure that connects computers</td><td>A <b>service</b> that uses the internet: web pages and resources linked together</td></tr>
    <tr><td>Carries many services: web, email, file transfer, streaming, voice calls</td><td>Accessed with a <b>web browser</b>, using <b>URLs</b> and HTTP or HTTPS</td></tr>
    <tr><td>Can exist without the web</td><td>Cannot exist without the internet</td></tr>
  </table></div>
  <p>Using webmail (an email account accessed through a website) uses <b>both</b>: the <b>internet</b>, because data is sent across the infrastructure, and the <b>WWW</b>, because you reach the account through a website stored on a web server.</p>

  <h2>2 · Bit streaming</h2>
  <p>Streaming sends a <b>continuous series of bits</b>. The receiver does not wait for the whole file: it starts playing while the rest is still arriving.</p>
  <ol>
    <li>The video or audio is <b>compressed</b> and uploaded to a <b>media server</b>.</li>
    <li>The server sends the data to the user as a <b>stream of bits</b>.</li>
    <li>On the user's device the data goes into a <b>buffer</b>, which stores data from the server until the device is ready to play it, and smooths out differences between the speed of arrival and the speed of playback.</li>
    <li>The player takes the bits from the buffer and displays them.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th></th><th>Real-time streaming</th><th>On-demand streaming</th></tr>
    <tr><td><b>Source</b></td><td>Live events, captured and sent as they happen (video conferences, live concerts)</td><td>Pre-recorded files stored on a media server</td></tr>
    <tr><td><b>Playback</b></td><td>Immediately, as it happens; the viewer cannot choose the time and usually cannot rewind</td><td>When the user chooses; can pause, rewind and skip</td></tr>
    <tr><td><b>Needs</b></td><td>Enough bandwidth all the time and heavy compression so people are not behind in the conversation</td><td>A buffer that fills ahead of the viewing point</td></tr>
  </table></div>
  <h3>Why compress?</h3>
  <p>Video is data-intensive, so the file size has to be reduced to <b>reduce the bandwidth</b> used and the <b>buffering</b>. That lets people with lower bandwidth take part. For real-time streaming <b>lossy</b> compression is more appropriate: it shrinks the file much more than lossless, so less bandwidth and less buffering are needed, and the data removed (fine detail, or a reduced resolution or sample rate) is not noticed.</p>
  <h3>Bit rate and broadband speed</h3>
  <p>The <b>bit rate</b> is the number of bits per second the video needs. If the connection (broadband speed) delivers bits more slowly than the player uses them, the buffer empties and playback <b>pauses to buffer</b>. A higher quality video needs a higher bit rate, so it needs a faster connection.</p>

  <h2>3 · Hardware that supports the internet</h2>
  <ul>
    <li><b>Modem</b> (modulator-demodulator): converts <b>digital data into analogue</b> signals for transmission over telephone lines, and analogue back into digital at the other end.</li>
    <li><b>PSTN</b> (Public Switched Telephone Network): the worldwide telephone network, made of many different types of communication line. Data may be converted into another form (analogue signals), can travel in both directions at the same time (duplex), and passes through different <b>switching centres</b> and ISPs.</li>
    <li><b>Dedicated lines</b>: a direct, private connection, such as a leased line, giving faster, more reliable transmission than shared links.</li>
    <li><b>Cell phone network</b>: wireless access through towers (see 2.1.2).</li>
    <li><b>Routers</b>: receive packets, read the destination IP address and forward them towards their destination using a routing table.</li>
  </ul>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Using "internet" and "web" as if they were the same. The web is a service that runs on the internet.</li>
    <li>Describing streaming as "downloading a video". The data is played as it arrives, via a buffer.</li>
    <li>Leaving out what the buffer does: it stores data from the server until the device can process it.</li>
    <li>Saying lossy compression is used "because it is better". Say it reduces file size more, so less bandwidth and buffering.</li>
    <li>Writing that a modem "connects to the internet". It converts digital to analogue and back.</li>
  </ul>
'''

watch = '''
  <h2>1 · Internet and WWW</h2>
  <div id="stA"></div>
  <h2>2 · Bit streaming through a buffer</h2>
  <p>Press Play.</p>
  <div id="stB"></div>
  <h2>3 · A modem and the telephone network</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Will the video buffer?</h2>
  <p>Choose the video's bit rate and the speed of the connection. The graph shows how full the buffer is over 30 seconds.</p>
  <div class="card"><div id="vS"></div><div id="vR"></div><div id="vG"></div><div class="verdict" id="vV"></div></div>
  <h2>Lab 2 · Internet, WWW or both?</h2>
  <div class="card"><div id="iB" class="btnrow"></div><div id="iO"></div></div>
  <h2>Lab 3 · Real-time or on-demand?</h2>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>
'''

_pr, _prjs = PR(["Internet or WWW?", "Real-time or on-demand?", "Match the term to its meaning", "Put the streaming steps in order", "Working out", "Multiple choice"],
  ("Does it describe the internet or the World Wide Web?", ["Internet", "World Wide Web"], [("A global network of networks", 0), ("Web pages found with URLs in a browser", 1), ("The physical infrastructure of cables and routers", 0), ("A service that runs on the internet", 1), ("Also carries email and file transfer", 0), ("Uses HTTP or HTTPS", 1)], "Internet: infrastructure. Web: a service on it."),
  ("Is it real-time or on-demand streaming?", ["Real-time", "On-demand"], [("A live video conference", 0), ("A film you choose to watch tonight", 1), ("Can be paused and rewound", 1), ("Sent as it happens, not stored", 0), ("Played from a file on a media server", 1), ("Viewers must see it at the same moment", 0)], "Real-time is live; on-demand is stored."),
  [["Bit streaming", "A continuous flow of bits played as it arrives"], ["Buffer", "Stores data until the device can process it"], ["Modem", "Converts digital to analogue and back"], ["PSTN", "The public telephone network with many line types and switching centres"], ["Dedicated line", "A direct private connection"]],
  ("Put the steps of bit streaming in order.", ["The video is compressed", "It is uploaded to a media server", "The server sends it to the user as a stream of bits", "It is stored in a buffer on the user's device", "The player plays it from the buffer"], "Compress, upload, stream, buffer, play."),
  [{"q": "A video needs 5 Mbps. The connection gives 8 Mbps. Does it need to pause to buffer? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "8 is more than 5.", "sol": "<b>0</b>."}, {"q": "The same video on a 3 Mbps connection. How many Mbps short is it?", "a": 2, "unit": "Mbps", "tol": 0.01, "hint": "5 − 3.", "sol": "<b>2</b> Mbps."}, {"q": "A film file is 600 MB. At 8 MB per second how many seconds does it take to download completely?", "a": 75, "unit": "s", "tol": 0.5, "hint": "600 ÷ 8.", "sol": "<b>75</b> s."}, {"q": "A video of 24 Mbps is compressed to a third of its size. What is the new bit rate in Mbps?", "a": 8, "unit": "Mbps", "tol": 0.01, "hint": "24 ÷ 3.", "sol": "<b>8</b> Mbps."}, {"q": "How many services are named as using the internet in the table (web, email, file transfer, streaming, voice calls)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>5</b>."}],
  [("The WWW is:", ["The whole internet", "A service that uses the internet", "A cable", "A router"], 1, "A service."), ("What does a buffer do in streaming?", ["Stores data until the device can process it", "Compresses data", "Encrypts data", "Prints data"], 0, "Stores data."), ("Which compression suits real-time streaming?", ["Lossy", "Lossless only", "None", "Encryption"], 0, "Lossy, for the bandwidth."), ("A modem converts:", ["Digital to analogue and back", "Text to images", "Light to sound", "Files to paper"], 0, "Digital and analogue."), ("Webmail uses:", ["Only the internet", "Only the web", "Both the internet and the WWW", "Neither"], 2, "Both."), ("A dedicated line is:", ["A direct private connection", "A shared public link", "A radio wave", "A browser"], 0, "A direct private connection.")],
  [("Internet", "Global network of networks."), ("WWW", "Web pages on the internet; browser, URL."), ("Bit streaming", "Continuous bits, played as they arrive."), ("Buffer", "Holds data until it can be played."), ("Real-time", "Live; played immediately."), ("On-demand", "Stored; played when chosen."), ("Modem", "Digital to analogue and back."), ("PSTN", "Telephone network; switching centres; duplex.")])

real = RWNOTE + (
rw("Watching a film on a streaming service", "The film is stored on a media server. Your device buffers a few seconds ahead so it can keep playing, and if your Wi-Fi slows down the picture pauses to buffer.", "on-demand streaming with a buffer.") +
rw("A live football match online", "Cameras capture it, it is compressed, and sent to viewers as it happens. You cannot skip ahead of real time.", "real-time bit streaming.") +
rw("Sending an email from a website", "You open a web page (the WWW) to write the email, and the message crosses the internet to the other person.", "webmail uses both the web and the internet.") +
rw("Old dial-up internet", "A modem turned computer data into sounds that could travel over the telephone line, and back again at the other end.", "a modem converts digital to analogue and back.") +
rw("A business with a leased line", "A company pays for a direct private link to its ISP so its connection is faster and more reliable than a shared one.", "dedicated lines give direct, private connections.")
)

where = [
  ("M/J 2021", "11, 13", "4(d)", "3", "Whether webmail uses the internet, the WWW or both"),
  ("O/N 2023", "12", "6(a)", "3", "Most appropriate compression for streaming a live concert, with justification"),
  ("M/J 2024", "12", "3(c)", "2 + 2", "The role of routers and of the PSTN in transmitting data through the internet"),
  ("O/N 2024", "13", "9(c)", "4", "How bit streaming is used in a real-time video conference"),
  ("M/J 2025", "11", "2", "4 + 4 + 3 + 2", "Real-time bit streaming; why compress; lossy or lossless; the use of modems and dedicated lines")]

past = '''  <p class="note">Streaming, the web and internet hardware appear in Paper 1 about once a year. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q4(d)"), "3 marks", "Explain",
  "Melinda sends emails from her webmail account (an email account accessed through a website). Explain whether Melinda is using the internet, or the World Wide Web (WWW), or both.",
  "One mark for identifying both, two for the reasons.",
  "<p>" + mks(["She is using both"]) + " " + mks(["Internet: because she is sending data on the infrastructure", "WWW: because she is accessing a website, stored on a web server operated by the webmail provider, that is part of the WWW"], "a") + "</p>", "Choosing only one. Webmail is a website (the WWW) and the message travels across the internet.") + peq(SRC("s25", "11", "Q2"), "4 + 4 + 3 + 2 marks", "Explain / Identify / Complete",
  "Programmers take part in live video conferences using real-time bit streaming. The video is compressed before it is transmitted. (a) Explain how data is transferred using real-time bit streaming. (b)(i) Explain the reasons why a video is compressed before it is transmitted using real-time bit streaming. (ii) Identify whether the lossy or lossless compression method is more appropriate for real-time bit streaming. Justify your answer. (c) The video conference is accessed over the internet. State how modems and dedicated lines are used when data is transmitted over the internet.",
  "(a) Continuous bits, media server, buffer. (b) Reduce bandwidth and buffering.",
  "<p><b>(a)</b> Any four: " + mks(["The video is transmitted continuously", "as a series of bits", "The video is uploaded to a media server", "The users download from the media server", "On download, the media server sends the data to a buffer on the user's device", "The buffer is used when there is a difference in speed between transmission and receipt", "The buffer stores data from the server until the recipient can receive it", "The recipient views the bit stream from the buffer"]) + "</p><p><b>(b)(i)</b> Any four: " + mks(["Video is data-intensive", "so the file size needs reducing", "in order to reduce the amount of bandwidth used", "and reduce buffering", "This means people are not behind in the conversation", "and people with lower bandwidth can still take part"], "a") + "</p><p><b>(ii)</b> No mark for the choice (lossy); up to three: " + mks(["Reduces file size more than lossless", "so significantly less bandwidth is needed", "so buffering is reduced even more", "Data can be removed which cannot be seen", "reducing quality without impacting the experience"], "n") + "</p><p><b>(c)</b> " + mks(["Modems: convert digital data into analogue for transmission down phone lines, and analogue into digital after transmission", "Dedicated lines: provide a direct or private connection, which therefore gives faster transmission"]) + "</p>", "Saying a buffer 'speeds up' the video. It stores data until the device can process it, evening out differences in speed.") + peq(SRC("w24", "13", "Q9(c)"), "4 marks", "Explain",
  "The computer on the LAN is used for real-time video conferences, where people connected to the internet communicate in real time using video and audio. Explain how bit streaming is used in a real-time video conference.",
  "Compressed, continuous bits, media server, buffer.",
  "<p>Any four: " + mks(["Data is compressed before transmitting", "The video and audio are transmitted continuously as a series of bits", "The video is uploaded to a media server", "On download, the media server sends the data to a buffer", "The buffer stores data from the server until the receiving device can process it", "The receiving device receives the bit stream from the buffer"]) + "</p>", None) + peq(SRC("s24", "12", "Q3(c)"), "2 + 2 marks", "Describe",
  "Data transmitted on the internet passes through multiple different systems. (i) Describe the role of routers in the transmission of data through the internet. (ii) Describe the role of the PSTN (Public Switched Telephone Network) in the transmission of data through the internet.",
  "(ii) many types of line; conversion; duplex; switching centres.",
  "<p><b>(i)</b> Any two: " + mks(["Receives packets from the internet", "Analyses the destination IP address of each packet", "Forwards the packet towards its destination using the routing table", "Maintains or updates the routing table", "Finds the most efficient route to the destination"]) + "</p><p><b>(ii)</b> Any two: " + mks(["The PSTN consists of many different types of communication line", "so the digital data may need to be converted into a different form or an analogue signal", "Data is transmitted in both directions at the same time (duplex transmission)", "The communication passes through different switching centres or ISPs"], "a") + "</p>", None) + peq(SRC("w23", "12", "Q6(a)"), "3 marks", "Justify",
  "A real-time video of a music concert needs to be streamed to subscribers. Tick one box to identify the most appropriate type of compression (lossy or lossless) and justify your answer.",
  "No mark for the tick: marks for the justification. Lossy is the usual choice.",
  "<p>Lossy ticked, up to three: " + mks(["Loss of quality will not be noticed", "It needs to be viewed in real time, so less bandwidth is needed if the file size is smaller", "Smaller file sizes reduce buffering so the video plays more smoothly", "Viewers may watch on different devices, so may not need high-quality resolution"]) + " (Lossless is also accepted with a justification such as: viewers do not want any loss of quality, or streaming to high-bandwidth devices.)</p>", None)

review = req("2 marks", "Distinguish", "Distinguish between the internet and the World Wide Web.", "Infrastructure and service.", "<p>" + mks(["The internet is the global network of networks, the infrastructure", "The WWW is a service that runs on it: web pages and resources accessed with a browser and URLs"]) + "</p>", None) + req("3 marks", "Explain", "A film keeps stopping to buffer. Explain why and one way to improve it.", "Bit rate against connection speed.", "<p>" + mks(["The connection delivers bits more slowly than the player uses them", "so the buffer empties and playback pauses", "A faster connection, or a lower-quality (lower bit rate or more compressed) video, would fix it"]) + "</p>", None) + req("2 marks", "Describe", "Describe the purpose of the buffer in bit streaming.", "Between arrival and playback.", "<p>" + mks(["It stores data from the server until the device can play it", "It smooths out differences between the speed of transmission and the speed of playback"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between real-time and on-demand bit streaming.", "Live or stored.", "<p>" + mks(["Real-time: a live event captured and sent as it happens, played immediately", "On-demand: a stored file on a media server played when the user chooses, with pause and rewind"]) + "</p>", None) + req("2 marks", "State", "State what a modem does and why it is needed to use a telephone line.", "Digital and analogue.", "<p>" + mks(["It converts digital data into analogue signals (and back at the other end)", "because telephone lines carry analogue signals"]) + "</p>", None)

tips = tips_html([
  ("Internet = infrastructure. WWW = a service.", "Webmail uses both."),
  ("Streaming: continuous bits, a buffer.", "Played as it arrives."),
  ("Buffer: stores until the device can process it.", "It evens out speed differences."),
  ("Compression: less bandwidth, less buffering.", "Lossy suits real-time."),
  ("Modem: digital to analogue and back.", "PSTN: many line types, switching centres."),
  ("Dedicated line.", "A direct private connection, faster."),
], [("the internet", "A global network of networks."), ("the WWW", "A collection of web pages accessed over the internet."), ("a buffer", "Memory that holds data until it can be used."), ("a modem", "Converts digital to analogue and back.")],
  [("Explain", "Give the process and the reasons."), ("Identify", "Name it."), ("Describe", "Say what it does."), ("Justify", "Reason for the choice.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.circle(300, 110, 100, "ax", { fill: "none", style: "stroke:var(--accent);stroke-width:3" }) + SV.text(300, 24, "The internet (infrastructure)", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.circle(300, 120, 56, "f1", {}) + SV.text(300, 125, "WWW", "lbl bd", { "text-anchor": "middle" }) + SV.text(300, 143, "web pages, browser", "sm", { "text-anchor": "middle" });
    if (k >= 2) [["email", 180, 105], ["file transfer", 180, 150], ["streaming", 420, 105], ["voice calls", 420, 150]].forEach(([t, x, y]) => (o += SV.rect(x - 52, y - 14, 104, 28, "cell", { rx: 6 }) + SV.text(x, y + 5, t, "lbl", { "text-anchor": "middle", style: "font-size:12px" })));
    if (k >= 3) o += SV.text(300, 238, "webmail uses the WWW (a website) and the internet (the data crosses it)", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 250, label: "Internet and WWW", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The <b>internet</b> is the global network of networks: the infrastructure.", s: { i: 0 } }, { cap: "The <b>World Wide Web</b> is one service that runs on it: web pages and resources.", s: { i: 1 } }, { cap: "Other services also use the internet: email, file transfer, streaming and voice calls.", s: { i: 2 } }, { cap: "Webmail is both: a website (WWW) and data crossing the internet.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 130, 70, "f3", { rx: 10 }) + SV.text(85, 70, "Media server", "lbl bd", { "text-anchor": "middle" }) + SV.text(85, 92, "(compressed video)", "sm", { "text-anchor": "middle" }) + SV.rect(240, 55, 140, 40, "cell", { rx: 6 }) + SV.text(310, 80, "buffer", "lbl bd", { "text-anchor": "middle" }) + SV.rect(470, 40, 110, 70, "cell", { rx: 10 }) + SV.text(525, 80, "Player", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M150,75 H240", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(195, 62, "bits", "sm", { "text-anchor": "middle" }); if (k >= 2) { for (let i = 0; i < 5; i++) o += SV.rect(250 + i * 25, 66, 20, 18, "f1", {}); } if (k >= 3) o += SV.path("M380,75 H470", "ax", { style: "stroke:var(--good);stroke-width:3" }) + SV.text(425, 62, "plays", "sm", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(300, 150, "arrival slower than playback: buffer empties and the video pauses", "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 170, label: "Streaming", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The video is compressed and stored (or uploaded live) on a <b>media server</b>.", s: { i: 0 } }, { cap: "The server sends a <b>continuous stream of bits</b>.", s: { i: 1 } }, { cap: "The bits go into a <b>buffer</b> on the receiving device, which holds them until the device can process them.", s: { i: 2 } }, { cap: "The player takes data from the buffer and plays it while more arrives.", s: { i: 3 } }, { cap: "If the connection is too slow, the buffer empties and playback <b>pauses to buffer</b>.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 120, 60, "cell", { rx: 8 }) + SV.text(80, 85, "Computer", "lbl bd", { "text-anchor": "middle" }) + SV.rect(190, 50, 100, 60, "f3", { rx: 8 }) + SV.text(240, 85, "Modem", "lbl bd", { "text-anchor": "middle" }) + SV.rect(340, 40, 140, 80, "f1", { rx: 10 }) + SV.text(410, 70, "PSTN", "lbl bd", { "text-anchor": "middle" }) + SV.text(410, 92, "switching centres", "sm", { "text-anchor": "middle" }) + SV.rect(520, 50, 70, 60, "cell", { rx: 8 }) + SV.text(555, 85, "ISP", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.text(80, 140, "digital data", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(240, 140, "→ analogue signal", "sm", { "text-anchor": "middle" }); if (k >= 3) o += SV.path("M290,80 H340", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.path("M480,80 H520", "ax", { style: "stroke:var(--accent);stroke-width:3" }) + SV.text(410, 140, "many types of line; both directions at once", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 165, label: "Modem and PSTN", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "A computer wants to send data over a telephone line.", s: { i: 0 } }, { cap: "The data is <b>digital</b>.", s: { i: 1 } }, { cap: "The <b>modem</b> converts it into an <b>analogue</b> signal for the phone line (and back at the other end).", s: { i: 2 } }, { cap: "The signal crosses the <b>PSTN</b>: many types of line, different switching centres, data in both directions at once, to the ISP.", s: { i: 3 } }] });
})();

(function () {
  let rate = 5, speed = 4;
  const paint = () => { const T = 30, pts = []; let buf = 3; for (let t = 0; t <= T; t++) { pts.push(buf); buf = Math.max(0, Math.min(10, buf + (speed - rate) / Math.max(rate, 1))); } let o = '<path d="M40,20 V150 H400" class="ax"/>'; let d = ""; pts.forEach((p, i) => (d += (i ? "L" : "M") + (40 + i * 12) + "," + (150 - p * 12) + " ")); o += `<path d="${d}" fill="none" stroke="${speed >= rate ? "var(--good)" : "var(--bad)"}" stroke-width="3"/>`;
    o += '<text x="46" y="16" class="sm" style="font-size:11px">buffer level (seconds of video)</text><text x="400" y="166" class="sm" text-anchor="end" style="font-size:11px">time (30 s)</text>';
    $("#vG").innerHTML = `<svg viewBox="0 0 420 175" style="width:420px;max-width:100%;display:block">${o}</svg>`; const stalls = pts.filter((p) => p <= 0.01).length;
    $("#vV").innerHTML = speed >= rate ? `The connection (<b>${speed} Mbps</b>) is at least the video's bit rate (<b>${rate} Mbps</b>): the buffer stays full and the video plays smoothly.` : `The connection (<b>${speed} Mbps</b>) is slower than the video's bit rate (<b>${rate} Mbps</b>): the buffer drains${stalls ? " and the video <b>pauses to buffer</b>" : ""}. Use a faster connection, or compress the video more.`; };
  Lib.slider($("#vR"), { id: "vr", label: "Video bit rate (Mbps) ", min: 1, max: 20, value: rate, fmt: (x) => x, onInput: (v) => { rate = v; paint(); } });
  Lib.slider($("#vS"), { id: "vs", label: "Connection speed (Mbps) ", min: 1, max: 20, value: speed, fmt: (x) => x, onInput: (v) => { speed = v; paint(); } }); paint();
})();
btnTable("iB", "iO", [
  ["Browsing a company's web pages", "Both", "A website (WWW) delivered across the internet"],
  ["Sending email from a mail program", "Internet", "Data crosses the internet; no web page needed"],
  ["Using webmail in a browser", "Both", "A website (WWW) and data across the internet"],
  ["Transferring a file with FTP", "Internet", "A service on the internet, not a web page"],
  ["Reading a wiki article", "Both", "A web page found by URL, carried by the internet"],
  ["A video call", "Internet", "Streams over the internet, not web pages"]
], ["Activity", "Uses", "Why"]);
btnTable("rB", "rO", [
  ["A live football match", "Real-time", "Sent as it happens; cannot be paused"],
  ["Watching last week's lesson recording", "On-demand", "Stored on a media server; pause and rewind"],
  ["A team video meeting", "Real-time", "Heavy compression so nobody is behind"],
  ["A film on a streaming service", "On-demand", "Buffer fills ahead of the viewing point"],
  ["A live concert broadcast", "Real-time", "Lossy compression to use less bandwidth"],
  ["Catch-up TV", "On-demand", "A stored file chosen by the viewer"]
], ["Situation", "Type", "Reason"]);
''' + _prjs

finish("as-2-1-4-internet-www-bit-streaming", "as214", "The Internet, the WWW and Bit Streaming",
  "The difference between the internet and the World Wide Web, real-time and on-demand bit streaming with buffers and compression, bit rate and broadband speed, and modems, the PSTN and dedicated lines; animations, a buffering lab and the real Paper 1 questions from 2021 to 2025.",
  "2.1.4", "2 · Communication", "section 2.1 Networks including the internet", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on the internet, the WWW and bit streaming (Paper 1), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
