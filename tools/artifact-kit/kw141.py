"""14.1 key words, push and pull protocols, and MIME. Added to the six 14.1 pages by their builders.

add(key, tabs..., js) returns the same tuple with the extra sections in place.
"""
import json
import re

from ak20 import pc, req, mks


def terms(rows):
    return ('  <div class="tw"><table class="t">\n    <tr><th>Key word</th><th>Meaning</th></tr>\n'
            + "".join(f"    <tr><td><b>{w}</b></td><td>{m}</td></tr>\n" for w, m in rows) + "  </table></div>\n")


def words(core, extra):
    h = '<p>These are the words to use in your answers.</p>\n' + terms(core)
    if extra:
        h += ('  <p><b>Wider words.</b> These are not named in the 14.1 syllabus wording. They help you understand the topic and read around it.</p>\n' + terms(extra))
    return h


STACK = ([("Protocol", "A set of rules for communication between devices"), ("Protocol suite", "A group of protocols designed to work together, such as TCP/IP"),
          ("Protocol stack", "The suite viewed as layers, each with its own job"), ("Layer", "One level of the stack; it only communicates with the layers next to it"),
          ("Interface", "The agreed way two adjacent layers pass data to each other"), ("Header", "Control information a layer adds in front of the data"),
          ("Host", "A device at one end of the communication")],
         [("Encapsulation (networking)", "Each layer wraps the data from the layer above with its own header on the way down. This is a different meaning from encapsulation in OOP"),
          ("Decapsulation", "Each layer removes its own header on the way up"), ("Trailer", "Control information added after the data, such as the error check at the end of a frame"),
          ("Peer layers", "The same layer on the two hosts, which each use the other's header")])

LAYERS = ([("Segment / packet", "A block of data with a header. The Transport layer's blocks are often called segments"), ("Sequence number", "Lets the destination put the pieces back in order and spot a missing one"),
           ("Port number", "Identifies which application on the host the data is for"), ("Flow control", "Managing how fast data is sent so the receiver is not overwhelmed"),
           ("Retransmission", "Sending lost or damaged data again"), ("Datagram", "The Internet layer's packet, carrying source and destination IP addresses"),
           ("IP address", "Identifies the network and host"), ("Router", "Forwards packets between networks using the destination IP address"),
           ("Routing table", "A router's stored list of where to send packets next"), ("Hop", "One step from a device to the next on the route"),
           ("Frame", "The Link layer's unit, built for one local network segment"), ("MAC address", "The hardware address of a network interface, used for the next hop")],
          [("TCP", "Transmission Control Protocol: a Transport protocol that sets up a connection and re-sends lost data"), ("UDP", "User Datagram Protocol: a Transport protocol with no connection and no re-sending, so it is quicker"),
           ("Handshake", "The opening exchange that sets up a connection before data is sent"), ("Acknowledgement", "A message from the receiver saying data has arrived"),
           ("Timeout", "If no acknowledgement arrives in time, the data is sent again"), ("Socket", "An IP address and port number together: one end of a connection"),
           ("Congestion", "Too much traffic on part of a network, which delays or loses packets"), ("TTL / hop limit", "A count in the packet that falls at each router, so a lost packet cannot circle for ever"),
           ("ARP", "Address Resolution Protocol: finds the MAC address that belongs to an IP address on the local network"), ("NIC", "Network interface card: the hardware that sends and receives frames")])

APPS = ([("HTTP / HTTPS", "Transfers hypertext documents (web pages); HTTPS is the secure form"), ("FTP", "Sends and receives files over a network"),
         ("SMTP", "Sends email towards its destination"), ("POP3", "Receives email by downloading it, normally removing it from the server"),
         ("IMAP", "Receives email while keeping it on the server, so devices stay in sync"), ("Push protocol", "The sending side starts the transfer when it has something to send"),
         ("Pull protocol", "The receiving client asks the server for data"), ("Mail server", "A computer that sends on, receives and stores email"),
         ("Mailbox", "The space on a mail server holding one user's messages"), ("Peer-to-peer", "Computers of equal status share directly, with no central server holding the file"),
         ("Torrent file", "A small descriptor file with metadata about the shared file and its tracker"), ("Tracker", "Holds data about the computers in the swarm"),
         ("Swarm", "All the peers sharing one file"), ("Seed", "A peer with the whole file that is uploading it"), ("Piece", "One equal-sized part of the file")],
        [("MIME", "Multipurpose Internet Mail Extensions: the standard that lets email carry attachments, images, sound and other character sets"),
         ("Polling", "A client checking a server again and again at set intervals"), ("Email client / user agent", "The program you read and write email with"),
         ("Mail transfer agent", "The server software that passes email between mail servers"), ("Request and response", "An HTTP client asks; the server replies"),
         ("Stateless", "HTTP treats each request on its own and does not remember earlier ones"), ("Status code", "The number in an HTTP response, such as 200 (OK) or 404 (not found)"),
         ("URL", "The address of a resource, such as a web page"), ("Anonymous FTP", "Access to an FTP server without a personal account"),
         ("Leecher", "A peer still downloading the file; also used for one who downloads and shares little"), ("Lurker (free rider)", "A user who downloads files but adds nothing for others"),
         ("Choking", "A peer temporarily refusing to upload to another, to share its bandwidth fairly")])

# ---------------------------------------------------------------- push, pull and MIME
PULL = '''<h2>0 · Push protocols and pull protocols</h2>
  <p>The difference is <b>which side starts the transfer</b>.</p>
  <div class="tw"><table class="t">
    <tr><th></th><th>Push</th><th>Pull</th></tr>
    <tr><td>Who starts</td><td>The sender, as soon as it has something to send</td><td>The receiving client, when it asks the server</td></tr>
    <tr><td>Email example</td><td><b>SMTP</b>: client to mail server, and server to server</td><td><b>POP3</b> and <b>IMAP</b>: your client collects from your mail server</td></tr>
    <tr><td>Why it is used</td><td>Mail servers are always on, so mail can be delivered at once</td><td>Your phone or laptop may be off or offline, so the server holds the mail until it asks</td></tr>
  </table></div>
  <h3>How a pull client keeps checking</h3>
  <p>The mail server does not need to know where your device is. Your <b>email client checks the server again and again</b>, for example every 5 minutes. This is called <b>polling</b>.</p>
  <ol>
    <li>A timer in the email client runs out, or the user presses refresh.</li>
    <li>The client <b>connects</b> to the mail server and logs in with the user name and password.</li>
    <li>The client <b>asks</b> what is in the mailbox.</li>
    <li>If there is new mail, the client retrieves it. <b>POP3</b> downloads it and normally deletes the server copy; <b>IMAP</b> synchronises and leaves it there.</li>
    <li>The client disconnects (or, with IMAP, may stay connected), waits, and checks again.</li>
  </ol>
  <p>A message that arrives just after a check waits on the server until the next one. A short interval means less delay but more checks, most of which find nothing. Many IMAP clients can also stay connected and be told of new mail by the server, using an extension called IDLE.</p>
'''

MIME = '''<h2>0 · MIME: sending photos and files by email</h2>
  <p>SMTP was designed to carry <b>plain 7-bit ASCII text</b>. A photo, a PDF or a sound file is binary data, and many languages need characters outside ASCII. <b>MIME (Multipurpose Internet Mail Extensions)</b> solves this by describing each part of a message and turning it into text that can travel safely. MIME is not a transfer protocol: SMTP still sends the message, and POP3 or IMAP still retrieves it.</p>
  <ol>
    <li><b>Compose.</b> You type a message and attach a photo.</li>
    <li><b>Describe.</b> The email client adds headers: <code>MIME-Version</code>, and a <code>Content-Type</code> for each part, such as <code>text/plain</code> or <code>image/jpeg</code>. A message with several parts is <code>multipart/mixed</code>, with a <b>boundary</b> string marking where each part starts.</li>
    <li><b>Encode.</b> Binary parts are converted into text, usually with <b>Base64</b>. The <code>Content-Transfer-Encoding</code> header records the method.</li>
    <li><b>Send.</b> <b>SMTP</b> carries the whole message, which is now all text, to the recipient's mail server.</li>
    <li><b>Retrieve.</b> The recipient's client pulls it with <b>POP3</b> or <b>IMAP</b>.</li>
    <li><b>Decode.</b> The client reads the headers, splits the message at the boundaries, decodes each part back to the original bytes and opens it with a suitable program.</li>
  </ol>
  <pre class="plain">From: teacher@example.com
To: student@example.com
Subject: Trip photo
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="PART"

--PART
Content-Type: text/plain; charset="utf-8"

Here is the photo.

--PART
Content-Type: image/jpeg
Content-Disposition: attachment; filename="trip.jpg"
Content-Transfer-Encoding: base64

/9j/4AAQSkZJRgABAQAAAQABAAD...
--PART--</pre>
  <h3>Base64 in one example</h3>
  <p>Base64 takes 3 bytes (24 bits), cuts them into 4 groups of 6 bits and writes each group as one of 64 safe characters. The data therefore grows by about a third.</p>
  <div class="tw"><table class="t mono">
    <tr><th>Characters</th><td>M</td><td>a</td><td>n</td><td></td></tr>
    <tr><th>8-bit bytes</th><td>01001101</td><td>01100001</td><td>01101110</td><td></td></tr>
    <tr><th>6-bit groups</th><td>010011</td><td>010110</td><td>000101</td><td>101110</td></tr>
    <tr><th>Values</th><td>19</td><td>22</td><td>5</td><td>46</td></tr>
    <tr><th>Base64</th><td>T</td><td>W</td><td>F</td><td>u</td></tr>
  </table></div>
''' + pc('''import base64
from email.message import EmailMessage

print(base64.b64encode(b"Man"))        # b'TWFu'

msg = EmailMessage()
msg["From"] = "teacher@example.com"
msg["To"] = "student@example.com"
msg["Subject"] = "Trip photo"
msg.set_content("Here is the photo.")
photo = open("trip.jpg", "rb").read()  # binary data
msg.add_attachment(photo, maintype="image", subtype="jpeg", filename="trip.jpg")
print(msg)                             # headers, boundaries and Base64 text''') + '''
  <div class="tip"><b class="h">For the exam</b>MIME is not named in the 9618 syllabus wording for 14.1. Learn the six protocols first, and use MIME to explain how attachments can travel over SMTP.</div>
'''

WATCH_PULL = '<h2>0 · A client polling for new mail</h2>\n  <p>Press Play, or click the steps.</p>\n  <div id="stPoll"></div>\n'
WATCH_MIME = '<h2>0 · A photo travelling by email with MIME</h2>\n  <div id="stMime"></div>\n'
LAB_POLL = ('<h2>Lab 0 · How often should the client check?</h2>\n  <p>Move the sliders to see how long a new email waits on the server and how many checks the client makes.</p>\n'
            '  <div class="card"><div id="poI"></div><div id="poA"></div><div class="verdict" id="poV"></div></div>\n')

JS_STEPS = r'''
(function () {
  const X = (m) => 90 + m * 40;
  const draw = (s) => {
    const k = Math.round(s.i);
    let o = SV.text(12, 49, "Client", "lbl bd") + SV.text(12, 169, "Server", "lbl bd") + SV.line(80, 45, 710, 45, "ax") + SV.line(80, 165, 710, 165, "ax");
    [[0, 1, "9:00", "No new mail"], [5, 2, "9:05", "No new mail"], [10, 4, "9:10", "Yes: 1 new"]].forEach(([m, at, t, reply]) => {
      if (k < at) return;
      o += SV.line(X(m), 52, X(m), 158, "c1") + SV.text(X(m), 28, t + " any mail?", "lbl", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(X(m) + 8, 110, reply, "lbl bd", { style: "font-size:13px" });
    });
    if (k >= 3) o += SV.rect(X(7) - 7, 158, 14, 14, "f3", { rx: 3 }) + SV.text(X(7), 195, "9:07 email arrives and waits", "lbl", { "text-anchor": "middle", style: "font-size:13px" });
    return o;
  };
  Lib.stepper($("#stPoll"), { w: 760, h: 210, label: "A client polling a mail server", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "The email client is set to check its mail server every 5 minutes.", s: { i: 0 } },
    { cap: "9:00. The client connects and asks for new mail. There is none.", s: { i: 1 } },
    { cap: "9:05. The client asks again. Still nothing.", s: { i: 2 } },
    { cap: "9:07. An email arrives at the server by SMTP. In a pull protocol the server holds it until the client asks.", s: { i: 3 } },
    { cap: "9:10. The next check finds the email and the client retrieves it with POP3 or IMAP. It waited 3 minutes.", s: { i: 4 } }] });
})();
'''
JS_MIME = r'''
(function () {
  const stages = [["Compose", "text + photo"], ["MIME", "headers, Base64"], ["SMTP", "send"], ["POP3 / IMAP", "retrieve"], ["MIME", "decode, open"]];
  const detail = [["Message: Here is the photo.", "Attachment: trip.jpg (binary)"], ["Content-Type: image/jpeg", "binary becomes text: /9j/4AAQ..."], ["The all-text message travels to", "the recipient's mail server"],
    ["The recipient's client pulls", "the message from the server"], ["Base64 text becomes bytes again", "and the photo opens"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    stages.forEach((t, i) => { const x = 8 + i * 150; o += SV.rect(x, 20, 136, 62, i === k ? "f3" : "cell", { rx: 8, ...op(i <= k ? 1 : 0.5) }) + SV.text(x + 68, 46, t[0], "lbl bd", { "text-anchor": "middle", style: "font-size:14px" }) + SV.text(x + 68, 68, t[1], "sm", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.rect(150, 112, 460, 72, "cell", { rx: 8 }) + detail[k].map((l, j) => SV.text(380, 142 + j * 24, l, "lbl", { "text-anchor": "middle", style: "font-size:14px" })).join("");
    return o;
  };
  Lib.stepper($("#stMime"), { w: 760, h: 200, label: "An email attachment with MIME", base: { i: 0 }, draw, tween: 250, dwell: 3400, steps: [
    { cap: "You write a message and attach a photo. The photo is binary data.", s: { i: 0 } },
    { cap: "The email client adds MIME headers and encodes the photo as Base64 text.", s: { i: 1 } },
    { cap: "<b>SMTP</b> pushes the message to the recipient's mail server.", s: { i: 2 } },
    { cap: "The recipient's client <b>pulls</b> it with POP3 or IMAP.", s: { i: 3 } },
    { cap: "The client reads the MIME headers, decodes the Base64 and opens the photo.", s: { i: 4 } }] });
})();
'''
JS_LAB = r'''
(function () {
  let every = 5, arrive = 7;
  const paint = () => {
    const next = Math.ceil(arrive / every) * every, wait = next - arrive;
    $("#poV").textContent = `The email arrives at minute ${arrive}. The next check is at minute ${next}, so it waits ${wait} minute${wait === 1 ? "" : "s"}. Checking every ${every} minute${every === 1 ? "" : "s"} makes ${Math.floor(1440 / every)} checks a day.`;
  };
  Lib.slider($("#poI"), { id: "poi", label: "Check the server every (minutes) ", min: 1, max: 30, value: every, onInput: (v) => { every = v; paint(); } });
  Lib.slider($("#poA"), { id: "poa", label: "Email arrives at minute ", min: 1, max: 60, value: arrive, onInput: (v) => { arrive = v; paint(); } });
})();
'''

REVIEW_APPS = req("3 marks", "Describe", "An email client uses a pull protocol. Describe how it finds out that a new email has arrived.", "Who starts, how often, and what happens to the message.",
    "<p>" + mks(["The email client connects to the mail server at set intervals (or when the user refreshes).", "It asks the server whether there are new messages in the mailbox.", "If there are, it retrieves them using POP3 or IMAP; until then they wait on the server."]) + "</p>",
    "Saying the server pushes each email to the user's device. With POP3 the client has to ask.") + req("4 marks", "Explain", "Explain how a photo can be sent by email using SMTP, which was designed for text.", "Describe, encode, send, decode.",
    "<p>" + mks(["MIME headers state the type of each part of the message.", "The binary photo is encoded as text, for example with Base64.", "SMTP sends the message, which now contains only text.", "The receiving client uses the headers to decode the text back into the photo."]) + "</p>",
    "Calling MIME the protocol that sends the email. SMTP sends it; MIME describes and encodes the content.")


def _match(pairs, el):
    return f'\nLib.match($("#{el}"), {json.dumps(dict(prompt="Match the key word to its meaning.", pairs=pairs, done="Use these words in your answers."))});\n'


_M = {
    "stack": [["Protocol suite", "Protocols designed to work together"], ["Interface", "How two adjacent layers pass data"], ["Header", "Control information added in front of data"],
              ["Encapsulation", "Wrapping data with a header on the way down"], ["Decapsulation", "Removing a header on the way up"], ["Host", "A device at one end of the communication"]],
    "layers": [["Port number", "Says which application the data is for"], ["Sequence number", "Lets the data be put back in order"], ["Datagram", "A packet carrying IP addresses"],
               ["Frame", "The unit sent over one local segment"], ["Routing table", "A router's list of where to send packets next"], ["Acknowledgement", "A message saying data has arrived"]],
    "apps": [["Push protocol", "The sender starts the transfer"], ["Pull protocol", "The receiving client asks for the data"], ["Polling", "Checking a server at set intervals"],
             ["MIME", "Lets email carry attachments"], ["Base64", "Writes binary data as safe text characters"], ["Tracker", "Holds data about the peers in a swarm"]],
}

# page -> key word tables, whether it gets the push/pull and MIME material, which match activity
_PAGES = {
    "stack": dict(words=[("Key words: the stack", STACK)], email=False, match="stack"),
    "layers": dict(words=[("Key words: the four layers", LAYERS)], email=False, match="layers"),
    "apps": dict(words=[("Key words: application protocols", APPS)], email=True, match="apps"),
    "journey": dict(words=[("Key words: the stack", STACK), ("Key words: the four layers", LAYERS)], email=False, match="layers"),
}


def _number(tab, blocks, prefix="", before=None):
    """Put the new blocks into a tab and renumber its numbered headings."""
    new = "".join("  " + b for b in blocks)
    if before:
        m = re.search(rf"  <h2>{prefix}\d+ · {before}", tab)
        tab = tab[:m.start()] + new + "\n" + tab[m.start():] if m else tab + new
    else:
        tab += new
    n = iter(range(1, 99))
    return re.sub(rf"<h2>{prefix}\d+ · ", lambda m: f"<h2>{prefix}{next(n)} · ", tab)


def add(key, learn, watch, explore, practise, review, js):
    cfg = _PAGES[key]
    blocks = []
    if cfg["email"]:
        blocks += [PULL, MIME]
        watch = _number(watch, [WATCH_PULL, WATCH_MIME])
        explore = _number(explore, [LAB_POLL], prefix="Lab ")
        review += REVIEW_APPS
        js += JS_STEPS + JS_MIME + JS_LAB
    blocks += [f"<h2>0 · {title}</h2>\n  " + words(*data) for title, data in cfg["words"]]
    learn = _number(learn, blocks, before="(?:Common ways|What to take)")
    practise = _number(practise, ['<h2>0 · Key words</h2><div id="m2" class="card"></div>\n'])
    js += _match(_M[cfg["match"]], "m2")
    return learn, watch, explore, practise, review, js
