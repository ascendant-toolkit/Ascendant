"""A Level CS syllabus 17.1.1: encryption, symmetric and asymmetric key cryptography. Run: python3 tools/artifact-kit/mk_ac1711.py"""
from ak16 import *

# toy RSA used in the labs (the classic textbook numbers)
N_, E_, D_ = 3233, 17, 2753
assert pow(pow(65, E_, N_), D_, N_) == 65 and pow(65, E_, N_) == 2790
assert pow(pow(1234, D_, N_), E_, N_) == 1234


def caesar(s, k):
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s.upper())


assert caesar("HELLO", 3) == "KHOOR" and caesar("KHOOR", -3) == "HELLO"

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Encryption</b> turns <b>plain text</b> into <b>cipher text</b> that is meaningless to anyone who intercepts it, using an encryption <b>algorithm</b> and a <b>key</b>; decryption reverses it. With <b>symmetric key cryptography</b> the sender and receiver use the <b>same secret key</b> to encrypt and decrypt, which is quick but the key has to be shared safely (the <b>key distribution problem</b>). With <b>asymmetric key cryptography</b> there is a <b>matched pair of keys</b>: a <b>public key</b> that anyone can have and a <b>private key</b> kept secret, and what one key encrypts only the other can decrypt. To send a <b>private message</b> you encrypt with the <b>receiver's public key</b> and only their private key can decrypt it; to send a <b>verified message</b> you encrypt with your <b>private key</b> and anyone can use your public key to prove it came from you.</p></div>

  <h2>1 · Words to know</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Plain text</b></td><td>The original, readable data before encryption.</td></tr>
    <tr><td><b>Cipher text</b></td><td>The text produced from plain text by an encryption algorithm.</td></tr>
    <tr><td><b>Encryption</b></td><td>Scrambling data so it is meaningless if intercepted.</td></tr>
    <tr><td><b>Key</b></td><td>A value used by the algorithm to encrypt or decrypt.</td></tr>
    <tr><td><b>Public key</b></td><td>One key of a matched pair; it can be obtained and used by anyone to send encrypted messages (or to decrypt a sender's digital signature).</td></tr>
    <tr><td><b>Private key</b></td><td>The other key of the pair: secret, never transmitted, and used to decrypt data that was encrypted with its matching public key.</td></tr>
  </table></div>
  <p>Why use key cryptography: to ensure the message is <b>authentic</b> (came from a trusted source), that <b>only the intended receiver</b> can understand it, and that it has <b>not been altered</b> in transit; and for <b>non-repudiation</b> (neither side can deny the transmission).</p>

  <h2>2 · Symmetric key cryptography</h2>
  <p>One key is used for both encryption and decryption. A simple example is a Caesar cipher with a shift of 3: HELLO becomes KHOOR, and shifting back by 3 decrypts it. (Real algorithms are far stronger but work the same way.)</p>
  <ul>
    <li><b>Benefit</b>: a simple process that can be carried out quickly; keys are usually shorter (128 or 256 bits).</li>
    <li><b>Drawback</b>: the key must be shared with the receiver first. Sending it over the network risks it being intercepted: the <b>key distribution problem</b>. If it is compromised, all messages are.</li>
  </ul>

  <h2>3 · Asymmetric key cryptography</h2>
  <p>Each user (or organisation) has a <b>matched pair of keys</b> made by an algorithm. One key encrypts and the <b>other key</b> decrypts. The public key can be shared openly; the private key never leaves its owner. This solves the key distribution problem, because no secret ever has to be sent.</p>
  <ul>
    <li><b>Benefit</b>: better security; keys do not need to be exchanged secretly; it allows <b>verification of the sender</b>.</li>
    <li><b>Drawback</b>: much more complex and so slower; the keys must be much longer (for example 2048 bits against 128 or 256) to give the same security.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Symmetric</th><th>Asymmetric</th></tr>
    <tr><td><b>Keys</b></td><td>One shared key</td><td>A pair: public and private</td></tr>
    <tr><td><b>Encrypt / decrypt</b></td><td>Same key does both</td><td>One key encrypts, the other decrypts</td></tr>
    <tr><td><b>Key sharing</b></td><td>The key must be shared (distribution problem)</td><td>Only the public key is shared; the private key stays secret</td></tr>
    <tr><td><b>Speed</b></td><td>Fast, simple</td><td>Slower, more complex</td></tr>
    <tr><td><b>Key length</b></td><td>Shorter (128 or 256 bits)</td><td>Longer (2048 bits)</td></tr>
    <tr><td><b>Verifies the sender?</b></td><td>No</td><td>Yes</td></tr>
  </table></div>

  <h2>4 · Sending a private message</h2>
  <ol>
    <li>The receiver's computer uses an algorithm to generate a <b>matched pair of keys</b>.</li>
    <li>The receiver <b>makes the public key available</b> (sends it, or publishes it on a website).</li>
    <li>The sender <b>encrypts the plain text with the receiver's public key</b> to give cipher text, and sends it.</li>
    <li>The receiver <b>decrypts the cipher text with their private key</b>. Only that key can do it.</li>
  </ol>

  <h2>5 · Sending a verified message to the public</h2>
  <ol>
    <li>The organisation generates a matched pair of keys and makes its <b>public key</b> available (for example on its website).</li>
    <li>It <b>encrypts the message with its private key</b> and sends it to the group.</li>
    <li>Anyone receiving it can <b>decrypt it with the organisation's public key</b>.</li>
    <li>It could only have been produced with the private key, so the sender is <b>verified</b> (non-repudiation). Anyone can read the message, so it is not private.</li>
  </ol>
  <div class="tip"><b class="h">Remember</b>Private message: <b>encrypt with the receiver's public key</b>. Verified message: <b>encrypt with your own private key</b>. In both cases the other key of the pair decrypts.</div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Encrypting a private message with your own public key. Use the receiver's public key.</li>
    <li>Saying the private key is sent to the receiver. It is never transmitted.</li>
    <li>Describing symmetric encryption as having "two keys" or asymmetric as "one key".</li>
    <li>Forgetting the order of the steps: keys generated, public key made available, message encrypted, sent, decrypted.</li>
    <li>Writing "the key is hidden" without saying which key and who holds it.</li>
  </ul>
'''

watch = '''
  <h2>1 · Symmetric: one shared key</h2>
  <p>Press Play. Sender and receiver use the same key.</p>
  <div id="stA"></div>
  <h2>2 · Asymmetric: a private message</h2>
  <div id="stB"></div>
  <h2>3 · Asymmetric: a verified message</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Caesar cipher (a symmetric example)</h2>
  <p>Type a message and choose the shared key (the shift). Decrypting uses the same key.</p>
  <div class="card"><input id="cI" type="text" value="HELLO" style="width:100%;font:inherit;padding:8px"><div id="cS"></div><div class="verdict" id="cV"></div></div>

  <h2>Lab 2 · A toy key pair</h2>
  <p>Public key (n = 3233, e = 17); private key (n = 3233, d = 2753). The numbers are tiny so you can follow them; real keys are 2048 bits or more.</p>
  <div class="card"><div id="rS"></div><div id="rO"></div></div>

  <h2>Lab 3 · Which key?</h2>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kO"></div></div>
'''

practise = '''
  <h2>1 · Symmetric or asymmetric?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which key?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of sending a private message in order</h2><div id="o1" class="card"></div>
  <h2>5 · Working out</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The padlock in your browser", "When you log in to a website your browser and the server set up encryption so your password cannot be read on the way. Asymmetric keys start the exchange; a faster symmetric key carries the data.", "both types of cryptography are used together.") +
rw("Messaging apps with end-to-end encryption", "Each person has a key pair. Your phone encrypts a message with the other person's public key, so only their private key, which never leaves their phone, can read it.", "encrypt with the receiver's public key.") +
rw("Wi-Fi passwords", "Everyone on a home network shares one passphrase. That is symmetric: the same key must be given to every device, which is the key distribution problem in a small way.", "symmetric keys have to be shared.") +
rw("Software updates that prove who made them", "The publisher signs the update with its private key. Your computer checks it with the publisher's public key, so it knows the update is genuine.", "encrypt with the private key to verify the sender.") +
rw("A safe with a letterbox", "Anyone can post a letter in through the slot (the public key), but only the owner has the key to open the safe (the private key).", "the public key encrypts; only the private key decrypts.")
)

where = [
  ("M/J 2022", "31, 33", "8(a)", "2 + 2", "Two reasons for key cryptography; two methods of key cryptography"),
  ("O/N 2022", "31, 33", "6(a), (b)", "2 + 2", "What a private key is; the process of asymmetric encryption"),
  ("O/N 2022", "32", "6(a)", "2", "Two differences between symmetric and asymmetric encryption"),
  ("M/J 2023", "32", "5(b)", "3", "Differences between symmetric and asymmetric cryptography"),
  ("M/J 2023", "31, 33", "9(a)", "2", "Purpose of asymmetric key cryptography"),
  ("O/N 2024", "32", "4", "4", "How one person uses asymmetric encryption to send a document securely"),
  ("O/N 2025", "32", "7", "1 + 4", "Another type of cryptography; how an organisation uses two keys to receive a secure transmission"),
  ("M/J 2026", "31", "8", "1 + 1 + 4", "Define cipher text and public key; send a private message using asymmetric keys"),
  ("M/J 2026", "32", "8", "3 + 4", "Differences between symmetric and asymmetric; send a verified message to a group")]

past = '''  <p class="note">Encryption has been examined in Paper 3 in almost every series from 2022 to 2026. The questions are about symmetric and asymmetric keys and the order of the steps when sending a private or a verified message. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s22", "31/33", "Q8(a)"), "2 + 2 marks", "Give",
  "A message is to be sent securely. Software uses a key to encrypt the message before it is sent. (a)(i) Give two reasons for using key cryptography. (ii) Give two methods of key cryptography that can be used.",
  "Authentic, private, unaltered, non-repudiation. Methods: symmetric and asymmetric.",
  "<p><b>(i)</b> Any two: " + mks(["To ensure the message is authentic: it came from a trusted source", "To ensure that only the intended receiver is able to understand the message", "To ensure the message has not been altered during transmission", "Non-repudiation: neither the sender nor the receiver can deny the transmission occurred"]) + "</p><p><b>(ii)</b> " + mks(["Symmetric", "Asymmetric"], "a") + "</p>", None) + peq(SRC("w22", "31/33", "Q6(a)(b)"), "2 + 2 marks", "State / Describe",
  "A message is encrypted using a private key and sent to an individual using asymmetric encryption. (a) State what is meant by a private key. (b) Describe the process of asymmetric encryption.",
  "(a) secret; has a matching public key. (b) encrypt with one key, decrypt with the matching key.",
  "<p><b>(a)</b> Any two: " + mks(["A private key is the unpublished, secret key that is never transmitted anywhere", "It has a matching public key", "It is used to decrypt data that was encrypted with its matching public key"]) + "</p><p><b>(b)</b> " + mks(["The message to be sent is encrypted using the recipient's public key (or the sender's private key)", "The message is decrypted using the recipient's private key (or the sender's public key)"]) + "</p>", None) + peq(SRC("w22", "32", "Q6(a)"), "2 marks", "State",
  "State two differences between symmetric and asymmetric encryption.",
  "Number of keys; who has which key.",
  "<p>" + mks(["Symmetric encryption uses a single key and asymmetric encryption uses a pair of keys", "The symmetric key is used by all, whereas only one of the asymmetric keys is available to everyone; the other needs to be kept secret"]) + "</p>", "Giving a difference with only one side: 'symmetric is faster'. Say what asymmetric does instead.") + peq(SRC("s23", "32", "Q5(b)"), "3 marks", "Explain",
  "Explain the differences between symmetric and asymmetric cryptography when encrypting and decrypting data.",
  "Keys, sharing, speed, length.",
  "<p>Any three: " + mks(["Symmetric cryptography uses a single key to encrypt and decrypt; asymmetric uses two", "The symmetric key is shared, whereas with asymmetric only the public key is shared and the private key is not", "so the risk of compromise is higher with symmetric, and asymmetric is more secure", "Symmetric is a simple process that is quick; asymmetric is much more complex, so slower", "Symmetric keys are usually shorter than asymmetric ones (128 or 256 bits against 2048 bits)"]) + "</p>", None) + peq(SRC("s23", "31/33", "Q9(a)"), "2 marks", "Describe",
  "Encryption is used to alter data into a form that makes it meaningless if intercepted. Describe the purpose of asymmetric key cryptography.",
  "Better security with a pair of keys.",
  "<p>Any two: " + mks(["To provide better security", "by using two different keys, a public key and a private key", "One of the keys is used to encrypt the message", "and the matching key is used to decrypt it"]) + "</p>", None) + peq(SRC("s24", "32", "Q4"), "4 marks", "Explain",
  "Sheila has a customer called Fred. Fred wants to send Sheila a confidential document as part of a transaction. Explain how Fred uses asymmetric encryption to send his document securely.",
  "Sheila's keys; her public key to Fred; Fred encrypts; Sheila decrypts with her private key.",
  "<p>Any four: " + mks(["Sheila's computer uses an algorithm to generate a matching pair of keys, a private key and a public key", "Sheila's computer sends Sheila's public key to Fred's computer, or Fred's computer acquires it", "Fred's computer encrypts the document (plain text) using Sheila's public key to create cipher text", "Fred's computer sends the cipher text to Sheila's computer", "The cipher text can only be decrypted using Sheila's private key: Sheila's computer decrypts it with her private key"]) + "</p>", "Having Fred encrypt with his own private key or with Sheila's private key. A private message is encrypted with the receiver's public key.") + peq(SRC("w25", "32", "Q7"), "1 + 4 marks", "Identify / Explain",
  "(a) Asymmetric encryption is a type of cryptography. Identify one other type of cryptography. (b) An organisation holds two asymmetric encryption keys, which they intend to use to receive secure transmissions. Explain how the organisation makes use of the two keys to receive a secure transmission.",
  "Symmetric or quantum. The organisation's public key is shared; the private key decrypts.",
  "<p><b>(a)</b> One: " + mks(["Symmetric cryptography", "Quantum cryptography"]) + "</p><p><b>(b)</b> " + mks(["The two keys held are a private key and a public key", "The organisation makes the public key available to anyone who wishes to send them secure transmissions; the sender obtains it", "The sender uses the organisation's public key to encrypt the message (plain text) into cipher text", "The organisation uses its private key to decrypt the message"]) + "</p>", None) + peq(SRC("s26", "31", "Q8"), "1 + 1 + 4 marks", "Define / Outline",
  "(a) Define the following asymmetric key encryption terms: (i) cipher text; (ii) public key. (b) Outline the process that would allow an individual to use asymmetric key encryption to send a private message to an organisation.",
  "(b) the organisation's keys, public key to the individual, encrypt, send, decrypt with the private key.",
  "<p><b>(a)(i)</b> " + mks(["Text encrypted from plain text using an encryption algorithm"]) + "<br><b>(ii)</b> " + mks(["A key that can be obtained and used by anyone to send encrypted messages; it is part of a matched pair"], "a") + "</p><p><b>(b)</b> " + mks(["The organisation generates a matched pair of encryption keys", "The organisation makes its public key available to the individual", "The individual uses the public key to encrypt their message", "and sends it to the organisation", "The organisation decrypts the message using their private key"]) + "</p><p>The sequence of steps is important.</p>", None) + peq(SRC("s26", "32", "Q8"), "3 + 4 marks", "Describe / Outline",
  "(a) Describe the differences between symmetric key and asymmetric key cryptography. (b) Outline the process that would allow a business to use encryption keys to send a verified message to a group of people.",
  "(a) both types needed for each mark. (b) the business encrypts with its private key.",
  "<p><b>(a)</b> Any three (both key types for each mark): " + mks(["Symmetric uses only one key but asymmetric uses two; the public and private keys are a mathematically linked pair", "Asymmetric uses one key to encrypt and the other to decrypt, whereas symmetric uses the same key for both", "Symmetric suffers from the key distribution problem, which the matched pair of keys for asymmetric has resolved", "Asymmetric keys must be much larger than symmetric keys for the same level of security", "Asymmetric allows verification of the sender, which symmetric does not"]) + "</p><p><b>(b)</b> " + mks(["The organisation generates a matched pair of encryption keys", "It makes its public key available to the group of people, for example via its website", "It encrypts its message using its private key", "and sends it to the group", "Anyone receiving the message can decrypt it using the organisation's public key", "Therefore verifying the sender (non-repudiation)"]) + "</p>", "Encrypting the verified message with the group's public keys. A verified message uses the sender's private key.")

review = req("3 marks", "Explain", "Explain the key distribution problem of symmetric encryption.", "How does the receiver get the key?", "<p>" + mks(["Both sides need the same secret key", "To give it to the receiver it must be sent or handed over", "If it is intercepted, anyone can decrypt all the messages"]) + "</p>", None) + req("2 marks", "State", "State which key Amy uses to encrypt a private message to Ben, and which key Ben uses to decrypt it.", "Receiver's keys.", "<p>" + mks(["Amy uses Ben's public key", "Ben decrypts with his private key"]) + "</p>", None) + req("2 marks", "State", "A company encrypts an announcement with its private key. State what anyone can do with the company's public key and what that proves.", "Verified message.", "<p>" + mks(["Decrypt the announcement", "It must have been encrypted with the company's private key, so it came from the company"]) + "</p>", None) + req("2 marks", "Describe", "Give one benefit and one drawback of asymmetric encryption compared with symmetric.", "Security against speed.", "<p>" + mks(["Benefit: no secret key has to be shared, or it can verify the sender", "Drawback: it is more complex and slower, and needs longer keys"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between plain text and cipher text.", "Before and after.", "<p>" + mks(["Plain text is the original readable data", "Cipher text is the result of putting it through the encryption algorithm"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on symmetric and asymmetric key cryptography (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Private message: receiver's public key.", "Only the receiver's private key can decrypt it."),
  ("Verified message: your private key.", "Anyone can check it with your public key."),
  ("The private key is never sent.", "It stays with its owner."),
  ("Symmetric: one key.", "Fast and simple, but the key must be shared."),
  ("Asymmetric: a pair.", "More secure, slower, longer keys."),
  ("Order of steps matters.", "Generate keys, share public key, encrypt, send, decrypt."),
], [
  ("plain text", "The original readable data."),
  ("cipher text", "Data after encryption."),
  ("a public key", "Obtainable by anyone; part of a matched pair."),
  ("a private key", "Secret key that decrypts data encrypted with its public key."),
], [("State", "Give a short answer."), ("Describe", "Say what happens, in several points."), ("Explain", "Give the steps and reasons."), ("Outline", "The main steps in order.")]) + FC

js = AKJS + AK20JS + r'''
function msgDraw(o) { // o: {left, right, mid, midNote, keyL, keyR, keyNote}
  let s = SV.rect(20, 40, 140, 70, "cell", { rx: 10 }) + SV.text(90, 66, o.left[0], "lbl bd", { "text-anchor": "middle" }) + SV.text(90, 92, o.left[1], "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
  s += SV.rect(480, 40, 140, 70, "cell", { rx: 10 }) + SV.text(550, 66, o.right[0], "lbl bd", { "text-anchor": "middle" }) + SV.text(550, 92, o.right[1], "lbl", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
  s += SV.path("M160,75 H480", "ax", { style: "stroke-dasharray:6 5" }); if (o.mid) s += SV.rect(250, 55, 140, 40, "f2", { rx: 6 }) + SV.text(320, 80, o.mid, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:14px" });
  if (o.keyL) s += SV.text(10, 140, o.keyL, "sm", { "text-anchor": "start", style: "fill:var(--accent);font-size:12px" }); if (o.keyR) s += SV.text(630, 140, o.keyR, "sm", { "text-anchor": "end", style: "fill:var(--accent);font-size:12px" }); if (o.note) s += SV.text(320, 170, o.note, "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return s; }
(function () {
  const S = [{ left: ["Sender", "HELLO"], right: ["Receiver", ""], note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyL: "key: shift 3", keyR: "key: shift 3", note: "both hold the same secret key (shared first)" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], mid: "KHOOR", keyL: "encrypt with the key", keyR: "", note: "cipher text travels; an eavesdropper sees only KHOOR" }, { left: ["Sender", ""], right: ["Receiver", "HELLO"], mid: "", keyL: "", keyR: "decrypt with the same key", note: "the same key reverses it" }];
  Lib.stepper($("#stA"), { w: 640, h: 190, label: "Symmetric", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "The sender wants to send HELLO privately.", s: { i: 0 } }, { cap: "<b>Symmetric</b>: both sides need the <b>same key</b>. Getting it to the receiver safely is the key distribution problem.", s: { i: 1 } }, { cap: "The sender encrypts the plain text with the key: the cipher text <b>KHOOR</b> is sent.", s: { i: 2 } }, { cap: "The receiver decrypts with the same key and gets HELLO.", s: { i: 3 } }] });
})();
(function () {
  const S = [{ left: ["Sender", "HELLO"], right: ["Receiver", ""], note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyR: "makes a key pair: public + private", note: "" }, { left: ["Sender", "HELLO"], right: ["Receiver", ""], keyL: "has the receiver's PUBLIC key", keyR: "keeps the PRIVATE key secret", note: "the public key can be sent to anyone" }, { left: ["Sender", ""], right: ["Receiver", ""], mid: "x9#Qk2", keyL: "encrypt with receiver's PUBLIC key", keyR: "", note: "" }, { left: ["Sender", ""], right: ["Receiver", "HELLO"], mid: "", keyL: "", keyR: "decrypt with own PRIVATE key", note: "only the private key can decrypt it" }];
  Lib.stepper($("#stB"), { w: 640, h: 190, label: "Private message", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "The sender wants to send a <b>private message</b> to the receiver.", s: { i: 0 } }, { cap: "The receiver generates a <b>matched pair of keys</b>.", s: { i: 1 } }, { cap: "The receiver makes the <b>public key</b> available. The <b>private key</b> is never sent.", s: { i: 2 } }, { cap: "The sender encrypts with the <b>receiver's public key</b> and sends the cipher text.", s: { i: 3 } }, { cap: "The receiver decrypts with the <b>private key</b>. Nobody else can.", s: { i: 4 } }] });
})();
(function () {
  const S = [{ left: ["Organisation", "NOTICE"], right: ["Anyone", ""], note: "" }, { left: ["Organisation", "NOTICE"], right: ["Anyone", ""], keyL: "key pair; public key published", keyR: "has the organisation's PUBLIC key", note: "" }, { left: ["Organisation", ""], right: ["Anyone", ""], mid: "q4%Rz8", keyL: "encrypt with its PRIVATE key", keyR: "", note: "" }, { left: ["Organisation", ""], right: ["Anyone", "NOTICE"], mid: "", keyL: "", keyR: "decrypt with the PUBLIC key", note: "it must have come from the organisation: verified" }];
  Lib.stepper($("#stC"), { w: 640, h: 190, label: "Verified message", base: { i: 0 }, draw: (s) => msgDraw(S[Math.round(s.i)]), tween: 120, dwell: 2800, steps: [{ cap: "An organisation wants to send a <b>verified</b> message to the public.", s: { i: 0 } }, { cap: "It generates a key pair and makes its <b>public key</b> available, for example on its website.", s: { i: 1 } }, { cap: "It encrypts the message with its <b>private key</b> and sends it to everyone.", s: { i: 2 } }, { cap: "Anyone can decrypt with the <b>public key</b>. Only the owner of the private key could have made it, so the sender is verified.", s: { i: 3 } }] });
})();

(function () {
  const inp = $("#cI"); let k = 3;
  const enc = (s, k) => [...s.toUpperCase()].map((c) => (/[A-Z]/.test(c) ? String.fromCharCode(((c.charCodeAt(0) - 65 + k + 26) % 26) + 65) : c)).join("");
  const paint = () => { const c = enc(inp.value, k); $("#cV").innerHTML = `Plain text <b class="bx">${inp.value.toUpperCase()}</b> → cipher text <b class="bx">${c}</b> (key: shift ${k}). Decrypting <b class="bx">${c}</b> with the same key gives <b class="bx">${enc(c, -k)}</b>. Anyone who learns the key can read every message.`; };
  Lib.slider($("#cS"), { id: "cs", label: "Shared key (shift) ", min: 1, max: 25, value: k, fmt: (x) => x, onInput: (v) => { k = v; paint(); } }); inp.oninput = paint; paint();
})();
(function () {
  const N = 3233, E = 17, D = 2753; let m = 65;
  const pw = (b, e) => { let r = 1n, x = BigInt(b) % BigInt(N), p = BigInt(e); while (p > 0n) { if (p & 1n) r = (r * x) % BigInt(N); x = (x * x) % BigInt(N); p >>= 1n; } return Number(r); };
  const paint = () => { const c = pw(m, E), back = pw(c, D), sig = pw(m, D), ver = pw(sig, E);
    $("#rO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Calculation</th><th>Result</th></tr>' + `<tr><td>Message (plain text)</td><td></td><td>${m}</td></tr><tr><td>Encrypt with the <b>public</b> key</td><td>${m}^${E} mod ${N}</td><td><b>${c}</b></td></tr><tr><td>Decrypt with the <b>private</b> key</td><td>${c}^${D} mod ${N}</td><td><b>${back}</b></td></tr></table></div>` + `<div class="verdict">Private message: only the holder of d = ${D} can turn ${c} back into ${back}. Verified message: encrypting ${m} with the <b>private</b> key gives ${sig}; anyone can use the public key to get ${ver} back, which proves it came from the key's owner.</div>`; };
  Lib.slider($("#rS"), { id: "rs", label: "Message number ", min: 2, max: 3000, value: m, fmt: (x) => x, onInput: (v) => { m = v; paint(); } }); paint();
})();
btnTable("kB", "kO", [
  ["Send a private message to Ben", "Ben's public key", "Ben's private key", "Only Ben can read it"],
  ["Send a verified message to the public", "Your private key", "Your public key (anyone)", "Proves it came from you; anyone can read it"],
  ["Symmetric encryption", "The shared secret key", "The same shared secret key", "Both sides need the key first"],
  ["Receive a private message", "(the sender uses your public key)", "Your private key", "Never share the private key"]
], ["Situation", "Encrypt with", "Decrypt with", "Result"]);
''' + CLASSIFY("cl1", "Symmetric or asymmetric?", ["Symmetric", "Asymmetric"],
  [("One key encrypts and decrypts", 0), ("A matched pair of keys", 1), ("Has the key distribution problem", 0), ("Slower and needs longer keys", 1), ("Allows the sender to be verified", 1), ("Quick and simple", 0)],
  "Symmetric: one shared key. Asymmetric: public and private pair.") + CLASSIFY("cl2", "Which key is used?", ["Receiver's public key", "Receiver's private key", "Sender's private key"],
  [("Encrypting a private message to the receiver", 0), ("The receiver decrypting a private message", 1), ("Encrypting a verified message", 2), ("Keeping the message secret from everyone else", 0), ("Never sent to anyone", 1), ("Proving who sent the message", 2)],
  "Private message: receiver's public key in, receiver's private key out.") + MATCH([
  ["Plain text", "The original readable data"], ["Cipher text", "The result of encrypting plain text"], ["Public key", "A key anyone can have"], ["Private key", "A key kept secret by its owner"], ["Key distribution problem", "A symmetric key has to be shared safely"]]) + ORDER(
  "Put the steps of sending a private message in order.",
  ["The receiver generates a matched pair of keys", "The receiver makes the public key available to the sender", "The sender encrypts the message with the public key", "The sender sends the cipher text", "The receiver decrypts it with the private key"],
  "Generate, publish, encrypt, send, decrypt.") + CALC([
  {"q": "How many keys are used in symmetric encryption between two people?", "a": 1, "unit": "", "tol": 0.01, "hint": "One shared key.", "sol": "<b>1</b>."},
  {"q": "How many keys does one user have in asymmetric encryption?", "a": 2, "unit": "", "tol": 0.01, "hint": "Public and private.", "sol": "<b>2</b>."},
  {"q": "A Caesar cipher with shift 3 encrypts the letter A. Which position in the alphabet (A = 1) is the cipher letter?", "a": 4, "unit": "", "tol": 0.01, "hint": "A to D.", "sol": "<b>4</b> (D)."},
  {"q": "Toy keys n = 3233, e = 17: what is 2790 decrypted with d = 2753? (use the lab)", "a": 65, "unit": "", "tol": 0.01, "hint": "Message 65 encrypts to 2790.", "sol": "<b>65</b>."},
  {"q": "A symmetric key is 128 bits and an asymmetric key is 2048 bits. How many times longer is the asymmetric key?", "a": 16, "unit": "", "tol": 0.01, "hint": "2048 ÷ 128.", "sol": "<b>16</b>."}]) + MCQ([
  ("Which key encrypts a private message to Sam?", ["Sam's private key", "Sam's public key", "Your private key", "Your public key"], 1, "The receiver's public key."),
  ("The private key is:", ["Sent with the message", "Kept secret by its owner", "Published on a website", "Shared with everyone"], 1, "Never transmitted."),
  ("Which is a drawback of symmetric encryption?", ["Slow", "The key has to be shared safely", "Two keys", "Long keys"], 1, "The key distribution problem."),
  ("A verified message is encrypted with:", ["The receiver's public key", "The sender's private key", "The receiver's private key", "No key"], 1, "The sender's private key."),
  ("Cipher text is:", ["Readable data", "Encrypted data", "A key", "A certificate"], 1, "Encrypted data."),
  ("Asymmetric encryption can:", ["Verify the sender", "Only be used by banks", "Not use keys", "Only decrypt"], 0, "It allows verification.")], "qz1") + CARDS([
  ("Plain text", "Original readable data."), ("Cipher text", "Encrypted data."), ("Symmetric", "One shared key; fast; key distribution problem."), ("Asymmetric", "Public and private pair; slower; longer keys."),
  ("Private message", "Encrypt with the receiver's public key."), ("Verified message", "Encrypt with your private key."), ("Private key", "Secret; never transmitted."), ("Public key", "Available to anyone.")])

build("ac1711", "ac-17-1-1-symmetric-asymmetric-encryption", "Symmetric and Asymmetric Encryption", EYA("17.1.1"),
  "Plain text and cipher text, symmetric and asymmetric key cryptography, and sending private and verified messages with public and private keys; animations, a toy key-pair lab and the real Paper 3 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 17 · Security, section 17.1 Encryption, encryption protocols and digital certificates"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
