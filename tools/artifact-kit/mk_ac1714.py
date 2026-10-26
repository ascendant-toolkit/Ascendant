"""A Level CS syllabus 17.1.4: digital certificates and digital signatures. Run: python3 tools/artifact-kit/mk_ac1714.py"""
from ak16 import *

N_, E_, D_ = 3233, 17, 2753


def toyhash(s):
    return sum(ord(c) * (i + 1) for i, c in enumerate(s)) % 3000


sig = pow(toyhash("PAY 50"), D_, N_)
assert pow(sig, E_, N_) == toyhash("PAY 50")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>digital certificate</b> is an electronic document, issued by a trusted <b>Certificate Authority (CA)</b>, that proves the identity of a website, individual or organisation and contains their <b>public key</b>. To get one, you ask a CA, send your details and public key, the CA <b>verifies your identity</b> and then <b>issues a certificate</b> containing your public key. A <b>digital signature</b> shows that a message really came from its sender and has not been changed: the sender <b>hashes</b> the message to make a <b>message digest</b> and <b>encrypts the digest with their private key</b>. The receiver uses the sender's <b>public key</b>, which the digital certificate supplies and vouches for, to decrypt the signature, hashes the message they received, and <b>compares the two digests</b>: if they match, the message is genuine and unaltered.</p></div>

  <h2>1 · Digital certificates</h2>
  <p>A digital certificate is an <b>electronic (online) document</b> used to <b>authenticate or prove the identity</b> of a website, individual or organisation. It is typically <b>issued by a CA</b>. Items commonly found inside it:</p>
  <ul>
    <li>the name of the certificate holder (subject);</li>
    <li>the holder's <b>public key</b>;</li>
    <li>a serial number and a version number;</li>
    <li>the start and expiry dates (validity);</li>
    <li>the certificate issuer (the CA) and the CA's <b>digital signature</b>.</li>
  </ul>

  <h2>2 · How a certificate is acquired</h2>
  <ol>
    <li>The organisation <b>generates a public and private key pair</b> (for example with a key-generation tool, on its own computer).</li>
    <li>It <b>requests a digital certificate</b> from a <b>Certificate Authority</b>.</li>
    <li>It gathers the information the CA needs, including <b>information to prove its identity</b> and its <b>public key</b>, and sends it to the CA (protected: signed with its own private key and encrypted with the CA's public key).</li>
    <li>The CA <b>verifies the organisation's identity</b>.</li>
    <li>If the checks are passed, the CA <b>generates and issues the certificate</b>, which includes the organisation's public key (signed with the CA's private key, so others can trust it).</li>
  </ol>

  <h2>3 · Digital signatures</h2>
  <p>A digital signature <b>validates the authenticity</b> of an electronic message and shows it has <b>not been altered</b>. It uses a <b>hashing algorithm</b>, which turns a message of any length into a short fixed-size <b>message digest</b>; the same message always gives the same digest, and changing even one character gives a different one.</p>
  <h3>Producing the signature (sender)</h3>
  <ol>
    <li>The message is <b>hashed</b> with the agreed hashing algorithm...</li>
    <li>...to produce a <b>message digest</b>.</li>
    <li>The digest is <b>encrypted with the sender's private key</b>. This is the <b>digital signature</b>. The message and signature are then sent (and may themselves be encrypted with the receiver's public key to keep the message private).</li>
  </ol>
  <h3>Checking the signature (receiver)</h3>
  <ol>
    <li>If the message and signature were encrypted for the receiver, they are decrypted with the <b>receiver's private key</b>.</li>
    <li>The digital signature is <b>decrypted with the sender's public key</b> to recover the message digest that was sent.</li>
    <li>The message received is <b>hashed with the same hashing algorithm</b> to make a digest of the message as received.</li>
    <li>The <b>two digests are compared</b>. If they are the same, the message has not been altered (and came from the sender). If they differ, the message has been altered.</li>
  </ol>

  <h2>4 · Why a certificate is needed for a digital signature</h2>
  <ul>
    <li>The certificate <b>provides the sender's public key</b>, which is needed to check the signature.</li>
    <li>It <b>validates that the public key belongs to the person or organisation</b> it claims to, and so validates the private key used to create the signature.</li>
    <li>It makes a digital signature <b>virtually impossible to spoof</b>, and gives evidence of who signed and that the document was not altered.</li>
    <li>It gives <b>non-repudiation</b>: the sender cannot deny sending it.</li>
  </ul>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Saying the signature is a scanned picture of a handwritten signature. It is an encrypted message digest.</li>
    <li>Encrypting the whole message with the private key instead of the digest, or hashing with the public key.</li>
    <li>Leaving out the comparison of the two digests, or saying what it shows.</li>
    <li>Writing that the receiver uses their own private key to check the signature. The signature is checked with the sender's public key.</li>
    <li>Describing a certificate as a key. It is a document that contains a public key and proves identity.</li>
  </ul>
'''

watch = '''
  <h2>1 · Producing a digital signature</h2>
  <p>Press Play. The message is hashed, and only the digest is signed.</p>
  <div id="stA"></div>
  <h2>2 · Checking the signature</h2>
  <div id="stB"></div>
  <h2>3 · Getting a certificate</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Sign and verify</h2>
  <p>Toy numbers: public key (n = 3233, e = 17), private key (n = 3233, d = 2753). The hash is a simple toy one. Edit the message after signing to see verification fail.</p>
  <div class="card"><div class="verdict">Signed message: <b>PAY 50</b></div><input id="gI" type="text" value="PAY 50" style="width:100%;font:inherit;padding:8px"><div id="gO"></div></div>

  <h2>Lab 2 · What is in a certificate?</h2>
  <div class="card"><div id="cB" class="btnrow"></div><div id="cO"></div></div>
'''

practise = '''
  <h2>1 · Certificate or signature?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which key is used?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of checking a signature in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The padlock on a website", "Click it and you can see the site's certificate: who it was issued to, who issued it (the CA) and when it expires. Your browser checks it before trusting the site.", "a digital certificate proves the identity of a website.") +
rw("Signed software", "Apps and updates carry a digital signature. Your device checks it with the publisher's public key and refuses software that has been tampered with.", "the digest of the received file must match.") +
rw("Signing a PDF contract", "A digital signature on a contract shows who signed it and that nothing has been changed since. If one word is edited, verification fails.", "authenticity and integrity.") +
rw("An ID card", "A certificate is like a passport: a trusted authority checks who you are and issues a document that others accept without having to check you themselves.", "the CA verifies identity and issues the certificate.") +
rw("A wax seal on a letter", "The seal shows the sender (only they have the stamp) and that the letter has not been opened. A digital signature does the same for a message.", "non-repudiation and integrity.")
)

where = [
  ("O/N 2022", "31, 33", "6(c)", "4", "How a digital signature is used to verify a message when it is received"),
  ("O/N 2022", "32", "6(b)", "4", "How an organisation acquires its digital certificate"),
  ("M/J 2022", "32", "7", "3 + 3 + 4", "How a certificate is obtained; how a signature is produced; how it is checked on receipt"),
  ("O/N 2024", "31, 33", "7", "3 + 2", "What a digital certificate is; its role in creating a digital signature"),
  ("O/N 2025", "31", "5", "2 + 3", "Two items in a certificate; why a certificate is required to validate a signature"),
  ("O/N 2025", "33", "9", "4", "The process followed to acquire a digital certificate")]

past = '''  <p class="note">Digital certificates and signatures have been examined in Paper 3 in 2022, 2024 and 2025. The longer questions ask for the steps in order. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s24", "31/33", "Q7"), "3 + 2 marks", "Describe / Explain",
  "(a) Describe what is meant by a digital certificate. (b) Explain the role of a digital certificate in creating a digital signature.",
  "(a) electronic document; proves identity; issued by a CA; contains a public key.",
  "<p><b>(a)</b> Any three: " + mks(["A digital certificate is an electronic or online document", "used to authenticate or prove the identity of a website, or the online identity of an individual or organisation", "typically issued by a Certificate Authority (CA)", "For example, it contains information identifying a website owner or individual and a public key"]) + "</p><p><b>(b)</b> " + mks(["The digital certificate provides the public key", "that can be used to validate the private key associated with the organisation, website or digital signature"], "a") + "</p>", None) + peq(SRC("w25", "31", "Q5"), "2 + 3 marks", "Identify / Explain",
  "(a) Identify two items commonly found within a digital certificate. (b) Explain why a digital certificate is required to validate a digital signature.",
  "(a) name, public key, serial number, dates, issuer. (b) it provides the public key.",
  "<p><b>(a)</b> Any two: " + mks(["Name of the certificate holder (subject)", "Serial number", "Version number", "Expiration date, start date or validity", "The certificate holder's public key", "The certificate issuer, or the digital signature of the CA"]) + "</p><p><b>(b)</b> Any three: " + mks(["A digital certificate provides a public key", "which validates the private key used to create the digital signature", "It makes a digital signature virtually impossible to spoof, and provides evidence of the signer's identity and that the document was not altered", "Non-repudiation"], "a") + "</p>", None) + peq(SRC("w22", "32", "Q6(b)"), "4 marks", "Explain",
  "Explain the process by which an organisation may acquire its digital certificate.",
  "Request to a CA; details; verify; issue.",
  "<p>Any four: " + mks(["The organisation requests a certificate from a Certificate Authority (CA)", "The organisation may send its public key to the CA", "The organisation gathers all the information required by the CA, which includes information to prove its identity", "The CA verifies the organisation's identity", "The CA generates and issues the certificate, including the organisation's public key and other information"]) + "</p>", None) + peq(SRC("w25", "33", "Q9"), "4 marks", "Outline",
  "A company requires a digital certificate to ensure the authenticity of its online communications. Outline the process followed to acquire a digital certificate.",
  "Keys generated, request to a CA, information sent, CA verifies and issues.",
  "<p>Any four: " + mks(["The company generates a public and private key pair locally, using a web browser and an RSA key generator tool, which may be part of the CA's web page", "The company requests a digital certificate from a Certificate Authority (CA)", "The CA responds with its public key and digital certificate", "signed with its private key", "The company gathers authentication information, for example its public key", "and sends it to the CA signed with the company's private key and encrypted with the CA's public key", "The CA verifies the received information and generates and issues the digital certificate"]) + "</p>", None) + peq(SRC("w22", "31/33", "Q6(c)"), "4 marks", "Explain",
  "A message is encrypted using a private key and sent to an individual using asymmetric encryption. Explain how a digital signature is used to verify a message when it is received.",
  "Decrypt signature with the sender's public key; hash the message; compare the digests.",
  "<p>Any four: " + mks(["The message together with the digital signature is decrypted using the receiver's private key", "The digital signature received is decrypted with the sender's public key to recover the message digest sent", "The decrypted message received is hashed with the agreed hashing algorithm to reproduce the message digest of the message received", "The two message digests are compared", "If both digests are the same the message has not been altered; if they are different the message has been altered"]) + "</p>", "Forgetting to hash the received message. The comparison needs a second digest, made by the receiver.") + peq(SRC("s22", "32", "Q7"), "3 + 3 + 4 marks", "State / Explain",
  "A digital signature is used to validate the authenticity of an electronic message. In order to produce a digital signature, a digital certificate is required. (a) State how a digital certificate is obtained. (b)(i) Explain how a digital signature is produced before the message is sent. (ii) Explain how the digital signature can be checked on receipt to ensure that the message has not been altered during transmission.",
  "(b)(i) hash, digest, encrypt the digest with the sender's private key.",
  "<p><b>(a)</b> Any three: " + mks(["An enquiry is made to a Certificate Authority (CA)", "The enquirer's details are checked by the CA", "If the enquirer's details are verified by the CA, the public key is agreed", "The CA creates and issues a certificate that includes the enquirer's public key", "Data sent to or by the CA is encrypted with the CA's public or private key"]) + "</p><p><b>(b)(i)</b> " + mks(["The message is hashed (with the agreed hashing algorithm)", "to produce a message digest", "The message digest is then encrypted with the sender's private key to form the digital signature"], "a") + "</p><p><b>(ii)</b> Any four: " + mks(["The message together with the digital signature is decrypted using the receiver's private key", "The digital signature received is decrypted with the sender's public key to recover the message digest sent", "The decrypted message received is hashed with the agreed algorithm to reproduce a message digest of the message received", "The two message digests are compared", "If they are the same the message has not been altered; if different it has been altered"], "n") + "</p>", None)

review = req("3 marks", "Describe", "Describe how a message digest is made and what is signed.", "Hash first.", "<p>" + mks(["The message is put through a hashing algorithm", "which produces a fixed-size message digest", "The digest, not the whole message, is encrypted with the sender's private key to make the signature"]) + "</p>", None) + req("2 marks", "Explain", "Explain what the receiver concludes when the two digests are different.", "Altered?", "<p>" + mks(["The message has been altered since it was signed", "or it was not signed by the owner of that key, so it should not be trusted"]) + "</p>", None) + req("2 marks", "State", "State two items found in a digital certificate and who issues it.", "Subject, public key, dates.", "<p>" + mks(["Any two of: holder's name, public key, serial number, expiry date, issuer", "A Certificate Authority (CA)"]) + "</p>", None) + req("3 marks", "Explain", "Explain why the sender's public key is used, not the private key, to check a digital signature.", "Who has which key?", "<p>" + mks(["The signature was made with the sender's private key", "Only the matching public key can decrypt it", "The public key is available to everyone, including the receiver (from the sender's certificate)"]) + "</p>", None) + req("2 marks", "Identify", "Identify two things a digital signature proves about a message.", "Who and what.", "<p>" + mks(["It came from the sender (authenticity, non-repudiation)", "It has not been altered (integrity)"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on digital certificates and digital signatures (Paper 3), 2022 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Certificate = document with a public key.", "Issued by a CA after checking the identity."),
  ("Sign the digest.", "Hash the message, encrypt the digest with the sender's private key."),
  ("Check with the public key.", "Decrypt the signature, hash the message, compare."),
  ("Two digests compared.", "Same: unaltered. Different: altered."),
  ("Why a certificate?", "It provides and validates the public key; non-repudiation."),
  ("Order matters.", "Hash, digest, encrypt; then decrypt, hash, compare."),
], [
  ("a digital certificate", "An electronic document from a CA that proves identity and holds a public key."),
  ("a CA", "Certificate Authority: a trusted organisation that issues certificates."),
  ("a message digest", "The fixed-size result of hashing a message."),
  ("a digital signature", "The message digest encrypted with the sender's private key."),
], [("Describe", "Say what it is and what it does."), ("Explain", "Give the steps in order and the reasons."), ("Outline", "The main steps."), ("Identify", "Name them.")]) + FC

js = AKJS + AK20JS + r'''
function boxes(items, ox, y) { let o = ""; items.forEach(([t, cls, w], i) => { o += SV.rect(ox, y + i * 54, w || 190, 42, cls || "cell", { rx: 8 }) + SV.text(ox + (w || 190) / 2, y + i * 54 + 27, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); }); return o; }
(function () {
  const st = [["Message: PAY 50", "cell-ok"], ["Hash algorithm", "f4"], ["Message digest: 1158", "cell-ok"], ["Encrypt digest with sender's PRIVATE key", "f2"], ["Digital signature", "cell-ok"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; st.slice(0, k + 1).forEach(([t, c], i) => { o += SV.rect(30, 14 + i * 52, 300, 42, i === k ? "cell-warn" : c, { rx: 8 }) + SV.text(180, 41 + i * 52, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); if (i) o += SV.path("M180," + (14 + i * 52) + " V" + (6 + i * 52 + 8), "ax"); });
    if (k >= 4) o += SV.text(360, 250, "message + signature are sent", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 600, h: 280, label: "Producing a signature", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: [{ cap: "The sender has a message to sign.", s: { i: 0 } }, { cap: "The message is put through the agreed <b>hashing algorithm</b>...", s: { i: 1 } }, { cap: "...which produces a short <b>message digest</b>. Changing the message would change the digest.", s: { i: 2 } }, { cap: "The digest is <b>encrypted with the sender's private key</b>.", s: { i: 3 } }, { cap: "The result is the <b>digital signature</b>. It is sent with the message.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(30, 20, "received", "sm") + SV.rect(30, 28, 150, 40, "cell", { rx: 8 }) + SV.text(105, 54, "message", "lbl bd", { "text-anchor": "middle" }) + SV.rect(230, 28, 170, 40, "cell", { rx: 8 }) + SV.text(315, 54, "digital signature", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M315,68 V92", "ax") + SV.rect(215, 92, 200, 40, "f2", { rx: 8 }) + SV.text(315, 118, "decrypt with sender's PUBLIC key", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) + SV.path("M315,132 V150", "ax") + SV.rect(240, 150, 150, 36, "cell-ok", { rx: 8 }) + SV.text(315, 173, "digest A", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M105,68 V92", "ax") + SV.rect(30, 92, 150, 40, "f4", { rx: 8 }) + SV.text(105, 118, "hash it", "lbl", { "text-anchor": "middle" }) + SV.path("M105,132 V150", "ax") + SV.rect(30, 150, 150, 36, "cell-ok", { rx: 8 }) + SV.text(105, 173, "digest B", "lbl bd", { "text-anchor": "middle" });
    if (k >= 3) o += SV.text(210, 224, "compare digest A and digest B", "lbl bd", { "text-anchor": "middle" }); if (k >= 4) o += SV.text(210, 252, "same: not altered, from the sender  |  different: altered", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 440, h: 270, label: "Checking a signature", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "The receiver has the message and the digital signature.", s: { i: 0 } }, { cap: "The signature is decrypted with the sender's <b>public key</b> (from the certificate) to recover digest A.", s: { i: 1 } }, { cap: "The receiver hashes the message they received to make digest B.", s: { i: 2 } }, { cap: "The two digests are <b>compared</b>.", s: { i: 3 } }, { cap: "If they match the message has not been altered and the sender is verified; if not, it has been altered.", s: { i: 4 } }] });
})();
(function () {
  const L = ["Organisation generates a public and private key pair", "Organisation requests a certificate from a CA", "Organisation sends proof of identity and its public key", "CA verifies the organisation's identity", "CA issues the certificate (with the public key)"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((t, i) => (o += SV.rect(20, 12 + i * 46, 420, 38, i === k ? "cell-warn" : i < k ? "cell-ok" : "cell", { rx: 8 }) + SV.text(34, 36 + i * 46, t, "lbl", { style: "font-size:13px" }))); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 250, label: "Acquiring a certificate", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: L.map((t, i) => ({ cap: ["The organisation first makes its own key pair.", "It asks a trusted <b>Certificate Authority</b> for a certificate.", "It sends the information the CA needs to prove who it is, with its public key.", "The CA <b>checks</b> that the organisation is who it says it is.", "The CA <b>issues the certificate</b>, signed by the CA so others can trust it."][i], s: { i } })) });
})();

(function () {
  const N = 3233, E = 17, D = 2753; const h = (s) => [...s].reduce((a, c, i) => a + c.charCodeAt(0) * (i + 1), 0) % 3000;
  const pw = (b, e) => { let r = 1n, x = BigInt(b) % BigInt(N), p = BigInt(e); while (p > 0n) { if (p & 1n) r = (r * x) % BigInt(N); x = (x * x) % BigInt(N); p >>= 1n; } return Number(r); };
  const SIGNED = "PAY 50", sig = pw(h(SIGNED), D), inp = $("#gI");
  const paint = () => { const m = inp.value, d = pw(sig, E), hh = h(m), ok = d === hh;
    $("#gO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Step</th><th>Value</th></tr>' + `<tr><td>Signature sent with the message (digest ${h(SIGNED)} encrypted with the private key)</td><td>${sig}</td></tr><tr><td>Receiver decrypts it with the public key: digest A</td><td>${d}</td></tr><tr><td>Receiver hashes the message "${m.replace(/</g, "&lt;")}": digest B</td><td>${hh}</td></tr></table></div><div class="verdict">${ok ? "<b style=\"color:var(--good)\">Digests match</b>: the message is unaltered and was signed with the matching private key." : "<b style=\"color:var(--bad)\">Digests differ</b>: the message has been altered (or was not signed by this key)."}</div>`; };
  inp.oninput = paint; paint();
})();
btnTable("cB", "cO", [
  ["Subject (holder's name)", "The person, website or organisation the certificate is for", "Identifies who it belongs to"],
  ["Public key", "The holder's public key", "Used to encrypt messages to the holder or check their signature"],
  ["Issuer", "The Certificate Authority that issued it", "Who vouches for the holder"],
  ["Validity dates", "Start and expiry dates", "A certificate is only trusted while valid"],
  ["Serial and version number", "Unique number and format version", "Identify this certificate"],
  ["CA's digital signature", "Signature of the CA on the certificate", "Proves the certificate is genuine and unchanged"]
], ["Item", "What it is", "Why it matters"]);
''' + CLASSIFY("cl1", "Is it about a certificate or a signature?", ["Digital certificate", "Digital signature"],
  [("Issued by a Certificate Authority", 0), ("An encrypted message digest", 1), ("Contains the holder's public key", 0), ("Shows a message has not been altered", 1), ("Has an expiry date", 0), ("Made with the sender's private key", 1)],
  "Certificate: identity and public key. Signature: encrypted digest.") + CLASSIFY("cl2", "Which key is used?", ["Sender's private key", "Sender's public key", "Receiver's private key"],
  [("Encrypting the message digest to make the signature", 0), ("Decrypting the signature to recover the digest", 1), ("Decrypting a message that was encrypted for the receiver", 2), ("Provided to the receiver by the certificate", 1), ("Never sent to anybody", 0), ("Used to check who signed", 1)],
  "Sign with the private key; check with the public key.") + MATCH([
  ["Digital certificate", "Electronic document proving identity and holding a public key"], ["Certificate Authority", "Trusted organisation that issues certificates"], ["Message digest", "Fixed-size result of hashing a message"], ["Digital signature", "The message digest encrypted with the sender's private key"], ["Non-repudiation", "The sender cannot deny sending the message"]]) + ORDER(
  "Put the steps of checking a digital signature in order.",
  ["Decrypt the signature with the sender's public key to get digest A", "Hash the received message to get digest B", "Compare digest A and digest B", "Decide: same means unaltered, different means altered"],
  "Decrypt, hash, compare, decide.") + CALC([
  {"q": "How many digests are compared when a signature is checked?", "a": 2, "unit": "", "tol": 0.01, "hint": "A and B.", "sol": "<b>2</b>."},
  {"q": "The two digests are the same. Has the message been altered? Enter 0 for no, 1 for yes.", "a": 0, "unit": "", "tol": 0.01, "hint": "Same digests: not altered.", "sol": "<b>0</b>."},
  {"q": "How many items commonly in a certificate did the mark scheme list in the Learn tab (name, public key, serial number, version number, dates, issuer, CA signature)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>7</b>."},
  {"q": "How many keys does the signer use to make the signature?", "a": 1, "unit": "", "tol": 0.01, "hint": "Their private key.", "sol": "<b>1</b>."},
{"q": "A signature is made from a message digest. How many keys does the receiver need to check it (the sender's public key)?", "a": 1, "unit": "", "tol": 0.01, "hint": "One key.", "sol": "<b>1</b>."}]) + MCQ([
  ("A digital certificate is issued by:", ["The receiver", "A Certificate Authority", "The sender", "A printer"], 1, "A CA."),
  ("What is encrypted to make a digital signature?", ["The whole message", "The message digest", "The certificate", "The public key"], 1, "The digest."),
  ("The signature is checked with the:", ["Sender's public key", "Sender's private key", "Receiver's public key", "Nothing"], 0, "Sender's public key."),
  ("Different digests mean:", ["The message is unaltered", "The message has been altered", "The key is long", "Nothing"], 1, "Altered."),
  ("A certificate proves:", ["Identity", "Speed", "Colour", "Size"], 0, "Identity."),
  ("A hash function produces:", ["A key pair", "A fixed-size digest", "A certificate", "A network"], 1, "A digest.")], "qz1") + CARDS([
  ("Digital certificate", "Document from a CA proving identity; holds the public key."), ("CA", "Verifies identity and issues certificates."), ("Message digest", "Hash of the message."), ("Digital signature", "Digest encrypted with the sender's private key."),
  ("Checking", "Decrypt with public key, hash, compare digests."), ("Why a certificate", "Provides and validates the public key; non-repudiation."), ("Acquire", "Request, details and public key, CA verifies, issues."), ("Contents", "Name, public key, serial, dates, issuer, CA signature.")])

build("ac1714", "ac-17-1-4-digital-certificates-signatures", "Digital Certificates and Signatures", EYA("17.1.4"),
  "What a digital certificate is and how it is acquired, how a digital signature is produced and checked with a message digest, and why a certificate is needed; animations, a sign-and-verify lab and the real Paper 3 questions from 2022 to 2025.",
  dict(sub=CBK("Chapter 17 · Security, section 17.1 Encryption, encryption protocols and digital certificates"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
