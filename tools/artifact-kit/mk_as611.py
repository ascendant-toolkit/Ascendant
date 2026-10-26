"""AS CS 6.1.1: data security, privacy and integrity, and the security measures. Run: python3 tools/artifact-kit/mk_as611.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Data security</b> is protecting data from loss, corruption and unauthorised access. <b>Data privacy</b> means data can only be accessed by or disclosed to authorised people. <b>Data integrity</b> means the data is accurate, complete, consistent and up to date. Security and privacy are protected by <b>user accounts and passwords</b>, <b>access rights</b>, <b>biometrics</b>, <b>firewalls</b>, <b>anti-malware</b>, <b>encryption</b>, <b>digital signatures</b> and <b>back-ups</b>; integrity is protected by <b>validation</b> and <b>verification</b> (and back-ups). A good answer always says <b>how</b> the measure works, not only its name. Do not mix security measures (firewall, password) with integrity measures (double entry, presence check): matching them is a regular question.</p></div>

  <h2>1 · Security, privacy and integrity</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Why it matters</th></tr>
    <tr><td><b>Data security</b></td><td>Protecting data from loss, corruption, being amended or deleted, and from unauthorised access</td><td>Data needs protecting from someone amending, deleting or taking it; the computer system needs protecting from someone installing malware or damaging it; and data must be recoverable</td></tr>
    <tr><td><b>Data privacy</b></td><td>Ensuring data can only be accessed by or disclosed to authorised persons</td><td>Personal data about staff and students must not be seen by people who should not see it</td></tr>
    <tr><td><b>Data integrity</b></td><td>The accuracy, completeness and consistency of data (and that it is up to date), during and after processing</td><td>Wrong data gives wrong decisions</td></tr>
  </table></div>
  <p><b>Security against privacy:</b> security protects the data against loss or damage; privacy protects it against unauthorised access. <b>Security against integrity:</b> security protects data from loss or corruption; integrity is the accuracy and consistency of the data.</p>

  <h2>2 · Security measures</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>How it works</th></tr>
    <tr><td><b>User account and strong password</b></td><td>The user must log in to prove their identity; a strong password is long and mixes upper and lower case letters, digits and symbols, and is not related to the user</td></tr>
    <tr><td><b>Biometrics / two-factor authentication</b></td><td>Uses a feature of the individual (fingerprint, face) that is unique and almost impossible to duplicate; two-factor needs a second form of verification, such as an authenticator app code</td></tr>
    <tr><td><b>Access rights (permissions)</b></td><td>Each user can only open, edit or delete the files they have been given permission for</td></tr>
    <tr><td><b>Firewall</b></td><td>Monitors incoming and outgoing packets, checks them against a set of rules (allow or deny list of addresses, ports), blocks those that do not meet the rules and lets the others through</td></tr>
    <tr><td><b>Anti-virus / anti-malware</b></td><td>Scans files, downloads and devices, compares against a database of known malware, and quarantines, deletes or alerts the user if a match is found; its definitions must be kept up to date</td></tr>
    <tr><td><b>Encryption</b></td><td>Converts the data (plain text) into cipher text using a key, so that if it is intercepted it cannot be understood without the decryption key</td></tr>
    <tr><td><b>Digital signature</b></td><td>Proves the sender (authenticity) and that the data has not been changed (see section 3)</td></tr>
    <tr><td><b>Back-up</b></td><td>Regular copies so lost or corrupted data can be recovered</td></tr>
  </table></div>

  <h2>3 · Digital signatures</h2>
  <ol>
    <li>The sender puts the message through a <b>hashing algorithm</b> to produce a <b>digest</b>.</li>
    <li>The digest is <b>encrypted with the sender's private key</b>: this is the digital signature.</li>
    <li>The message and the signature are sent to the receiver.</li>
    <li>The receiver <b>decrypts</b> the signature with the sender's <b>public key</b> to reproduce the digest. This proves who sent it, because only the sender's private key could produce a signature the matching public key can decrypt.</li>
    <li>The receiver applies the same hashing algorithm to the message received and <b>compares</b> the two digests. If they are the same the message has <b>not changed</b>.</li>
  </ol>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying security "stops hackers" and privacy "stops hackers". Security protects from loss and corruption; privacy is about unauthorised access.</li>
    <li>Naming a measure without how it works, such as "use a firewall". Say it checks packets against rules and blocks those that do not meet them.</li>
    <li>Saying encryption "stops hackers from getting the data". It does not stop interception: the intercepted data cannot be understood without the key.</li>
    <li>Listing a validation or verification check as a security measure. They protect integrity.</li>
    <li>Describing a digital signature as an image of a signature. It is an encrypted digest.</li>
  </ul>
'''

watch = '''
  <h2>1 · A firewall decides which packets pass</h2>
  <div id="stA"></div>
  <h2>2 · Encryption</h2>
  <div id="stB"></div>
  <h2>3 · A digital signature</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Password strength</h2>
  <p>The number of possible passwords is the size of the character set to the power of the length.</p>
  <div class="card"><div id="pS1"></div><div id="pS2"></div><div id="pV" class="verdict"></div></div>
  <h2>Lab 2 · Caesar cipher</h2>
  <div class="card"><div id="eS"></div><div id="eV" class="verdict"></div></div>
  <h2>Lab 3 · Security or integrity?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

_pr, _prjs = PR(["Security, privacy or integrity?", "Security measure or integrity measure?", "Match the measure to how it works", "Put the digital signature steps in order", "Working out", "Multiple choice"],
  ("Security, privacy or integrity?", ["Security", "Privacy", "Integrity"], [("Protecting data from loss or corruption", 0), ("Only authorised people can see the data", 1), ("The data is accurate and consistent", 2), ("Making sure data can be recovered", 0), ("Preventing disclosure to unauthorised people", 1), ("The data is up to date and complete", 2)], "Security: loss. Privacy: access. Integrity: accuracy."),
  ("Is it a security measure or an integrity measure?", ["Data security", "Data integrity"], [("Firewall", 0), ("Double entry", 1), ("Access rights", 0), ("Presence check", 1), ("Password", 0), ("Visual check", 1)], "Firewall, access rights and passwords protect security; checks protect integrity."),
  [["Firewall", "Checks packets against rules and blocks those that fail"], ["Encryption", "Scrambles data with a key so it cannot be understood if intercepted"], ["Anti-malware", "Scans files against a database of known malware"], ["Access rights", "Limits which files each user can open or change"], ["Back-up", "Regular copies so lost data can be recovered"]],
  ("Put the digital signature steps in order.", ["The sender hashes the message to produce a digest", "The digest is encrypted with the sender's private key", "The message and signature are sent", "The receiver decrypts the signature with the sender's public key", "The receiver hashes the message and compares the digests"], "Hash, encrypt, send, decrypt, compare."),
  [{"q": "A password uses 26 lower-case letters and is 4 characters long. How many possible passwords?", "a": 456976, "unit": "", "tol": 0.5, "hint": "26^4.", "sol": "<b>456976</b>."}, {"q": "Using 62 characters (upper, lower, digits) and 6 characters, how many millions of passwords (nearest million)?", "a": 56800, "unit": "million", "tol": 100, "hint": "62^6 ÷ 10^6 ≈ 56 800.", "sol": "about <b>56 800</b> million."}, {"q": "A Caesar cipher shifts each letter by 3. What does D become? (Give its number: A=1, B=2 ...)", "a": 7, "unit": "", "tol": 0.01, "hint": "D is 4; 4 + 3.", "sol": "<b>7</b> (G)."}, {"q": "A firewall allows 3 ports and blocks the other 65 533. How many ports in total?", "a": 65536, "unit": "", "tol": 0.5, "hint": "3 + 65 533.", "sol": "<b>65536</b>."}, {"q": "A back-up is taken every night. The data is lost at 3 pm on Thursday; the last back-up was Wednesday night. How many hours of work could be lost if work started at 9 am?", "a": 6, "unit": "h", "tol": 0.01, "hint": "9 am to 3 pm.", "sol": "<b>6</b> hours."}],
  [("Data privacy means:", ["Only authorised people can access it", "It is accurate", "It is backed up", "It is compressed"], 0, "Authorised access."), ("Data integrity is:", ["Accuracy and consistency", "Encryption", "A firewall", "Copying"], 0, "Accuracy."), ("Encryption produces:", ["Cipher text", "A digest only", "A password", "A virus"], 0, "Cipher text."), ("A digital signature uses the sender's:", ["Private key", "Public key to sign", "Password", "IP address"], 0, "Private key encrypts the digest."), ("A firewall:", ["Checks packets against rules", "Creates back-ups", "Fixes typing errors", "Compresses files"], 0, "Rules."), ("Which protects integrity?", ["Validation", "Firewall", "Password", "Encryption"], 0, "Validation.")],
  [("Security", "Protect from loss, corruption, unauthorised access."), ("Privacy", "Only authorised people can see the data."), ("Integrity", "Accurate, complete, consistent, up to date."), ("Firewall", "Rules on packets; blocks those that fail."), ("Anti-malware", "Scans against known malware."), ("Encryption", "Cipher text; needs the key."), ("Digital signature", "Hash, encrypt digest with private key."), ("Back-up", "Recover lost data.")])

real = RWNOTE + (
rw("Your phone's face unlock", "A feature unique to you replaces a password: this is biometric authentication.", "biometrics.") +
rw("The padlock in a web address", "Data between your browser and the site is encrypted, so someone intercepting it sees only cipher text.", "encryption in transit.") +
rw("School data access", "A teacher can edit grades for their own class but a student cannot: the OS applies access rights.", "access rights.") +
rw("A signed software update", "Your computer checks the digital signature of an update, so it knows who published it and that nobody has changed it on the way.", "digital signature.") +
rw("A back-up after ransomware", "A school restores yesterday's copy of its files instead of paying: that is why back-ups protect security.", "back-up.")
)

where = [
  ("O/N 2021", "11, 13", "2(a)", "2", "The difference between data security and data integrity"),
  ("O/N 2021", "12", "1", "2", "Match measures to data security or data integrity"),
  ("M/J 2022", "11", "3(a)", "1", "The difference between the security and privacy of data"),
  ("O/N 2022", "11", "2", "4", "Match security features to their descriptions"),
  ("M/J 2022", "12", "4(a), (c)", "2 + 2", "Why data and the computer system must be secure; what encryption is and why it is used"),
  ("O/N 2022", "12", "6(a)", "2 + 3", "How a digital signature ensures authenticity; how a firewall protects data"),
  ("M/J 2022", "13", "5(a)", "1 + 2", "Why data needs to be kept secure; two security methods"),
  ("O/N 2023", "12", "5(a), (b)", "1 + 1", "The meanings of privacy and integrity"),
  ("M/J 2024", "12", "3(a)", "3 + 3", "A security measure against hackers; one for data in transmission"),
  ("M/J 2025", "11", "7", "3 + 5 + 3", "Restricting interception; how a digital signature shows data is unchanged; checksum"),
  ("M/J 2026", "12", "2(c)", "3 + 3", "Describe a virus and a hacker and a method to restrict each")]

past = '''  <p class="note">Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The matching question about security against integrity measures is asked in different forms nearly every year.</p>
''' + peq(SRC("w21", "11/13", "Q2(a)"), "2 marks", "Explain",
  "Explain the difference between data security and data integrity.", "Security: protect from loss or corruption. Integrity: consistency and accuracy.",
  "<p>" + mks(["Security is protecting data from loss or corruption", "Integrity is ensuring the consistency or accuracy of the data"]) + "</p>", None) + peq(SRC("w21", "12", "Q1"), "2 marks", "Match",
  "Draw one line from each measure to indicate whether it keeps data secure or protects the integrity of data. Measures: firewall, double entry, presence check, access rights, password.", "Three security, two integrity.",
  "<p>" + mks(["Data security: firewall, access rights, password", "Data integrity: double entry, presence check"]) + "</p>", "Putting a firewall or password under integrity. They keep data secure.") + peq(SRC("s22", "11", "Q3(a)"), "1 mark", "State",
  "State the difference between the security of data and the privacy of data.", "Loss against unauthorised access.",
  "<p>" + mks(["Security prevents loss of data, while privacy prevents unauthorised access"]) + "</p>", None) + peq(SRC("w22", "11", "Q2"), "4 marks", "Match",
  "Draw one line from each security feature to its most appropriate description. Features: firewall, pharming, anti-virus software, encryption (and digital signature). Descriptions: converts data to an alternative form; redirects a user to a fake website; verifies the authenticity of data; scans files on the hard drive for malicious software; accepts or rejects incoming and outgoing packets based on criteria.", "Pharming is a threat, not a measure.",
  "<p>" + mks(["Firewall: accepts or rejects incoming and outgoing packets based on criteria", "Pharming: redirects a user to a false website", "Anti-virus software: scans files on the hard drive for malicious software", "Encryption: converts data to an alternative form"]) + " (and digital signature: verifies the authenticity of data)</p>", None) + peq(SRC("s22", "12", "Q4(a)(c)"), "2 + 2 marks", "Explain / Describe",
  "(a) Explain why the school needs to keep both its data and its computer system secure from unauthorised access. (c) Data is encrypted when it is transmitted. Describe what is meant by encryption and explain why it is used.", "Data: someone amending, deleting or taking it. System: malware or damage. Cipher text and key.",
  "<p><b>(a)</b> " + mks(["Data needs protecting from someone amending, deleting or taking it", "The computer system needs protecting to stop people, for example, installing malware or damaging the system"]) + "</p><p><b>(c)</b> " + mks(["Data is turned into cipher text (encoded)", "It is used so that it cannot be understood if intercepted without the decryption key"], "a") + "</p>", None) + peq(SRC("w22", "12", "Q6(a)"), "2 + 3 marks", "Explain / Describe",
  "(i) Explain how a digital signature ensures the email is authentic. (ii) Describe how a firewall protects the data on the computer.", "Hash, digest, private key, public key. Monitors packets, rules, blocks.",
  "<p><b>(i)</b> Any two: " + mks(["The email message is put through a hashing algorithm to produce a digest", "The digest is encrypted with the sender's private key to create the digital signature", "The signature can only be decrypted with the matching sender's public key"]) + "</p><p><b>(ii)</b> " + mks(["Monitors incoming and outgoing packets or traffic", "Checks against an allow or deny list of IP addresses, or a set of rules for acceptable data or ports", "Blocks transmissions that do not meet the criteria and allows those that do"], "a") + "</p>", None) + peq(SRC("s22", "13", "Q5(a)"), "1 + 2 marks", "State / Give",
  "(i) State why data needs to be kept secure. (ii) Backup software is one way. Give two other ways the data stored in a computer can be kept secure.", "Loss, corruption, unauthorised access. Firewall, anti-malware, password, encryption, access rights.",
  "<p><b>(i)</b> " + mks(["To stop the data being lost, corrupted or amended", "To make sure it can be recovered", "To prevent unauthorised access"]) + "</p><p><b>(ii)</b> " + mks(["Install and run a firewall", "Up-to-date anti-virus or anti-malware", "A (strong) username and password", "Encryption", "Access rights"], "a") + " (any two)</p>", None) + peq(SRC("w23", "12", "Q5(a)(b)"), "1 + 1 marks", "State",
  "(a) State the meaning of privacy of data. (b) State the meaning of integrity of data.", "Authorised access only. Accuracy, completeness, consistency.",
  "<p><b>(a)</b> " + mks(["Ensuring data can only be accessed by or disclosed to authorised persons"]) + "</p><p><b>(b)</b> " + mks(["Ensuring the accuracy, completeness or consistency of data (during and after processing), or that it is up to date"], "a") + "</p>", None) + peq(SRC("s24", "12", "Q3(a)"), "3 + 3 marks", "Identify / Describe",
  "An assessment board stores digitised exam papers on a server. (i) Authentication methods help to protect the server against hackers. Identify one other security measure that helps to protect the server from hackers and describe how it works. (ii) Identify one security measure that helps to protect the data when it is being transmitted and describe how it works.", "Firewall or proxy; encryption.",
  "<p><b>(i)</b> One mark for the measure and two for the description: " + mks(["Firewall: checks incoming connections against criteria and blocks data from entering specific ports or data that does not meet the allow list or meets the deny list", "Proxy server: prevents devices accessing the web server directly, intercepts requests, forwards them using its own IP address, and screens returning data before sending it to the user"]) + "</p><p><b>(ii)</b> " + mks(["Encryption: encodes or scrambles data so if it is intercepted it cannot be understood; an algorithm or key is required to decode it"], "a") + "</p>", None) + peq(SRC("s25", "11", "Q7(a)(b)"), "3 + 5 marks", "Identify / Explain",
  "A banker transfers confidential data across the internet. (a) Identify and describe one method of restricting the risks posed by an unauthorised person intercepting the data. (b) The data includes a digital signature. Explain how a digital signature can make sure the data has not been changed during transmission.", "Encryption. Hash, digest, private key, compare.",
  "<p><b>(a)</b> " + mks(["Method: encryption", "Data is encoded or scrambled using a key to create cipher text", "If intercepted it cannot be understood without being decrypted using a key"]) + "</p><p><b>(b)</b> Any five: " + mks(["The sender hashes the document", "to produce a digest", "The sender encrypts the digest to create the digital signature", "The message and the signature are sent to the receiver", "The receiver decrypts the signature to reproduce the digest", "The receiver uses the same hashing algorithm on the document received to produce a second digest", "The receiver compares this digest with the one from the digital signature", "If they are the same the document has not changed"], "a") + "</p>", "Describing a digital signature as an image or as encrypting the whole message.")

review = req("2 marks", "State", "State two differences between data privacy and data integrity.", "Access, accuracy.", "<p>" + mks(["Privacy: only authorised people can access the data", "Integrity: the data is accurate, complete and consistent"]) + "</p>", None) + req("3 marks", "Describe", "Describe how a firewall protects a school network.", "Packets, rules, block.", "<p>" + mks(["It monitors incoming and outgoing packets", "It checks them against a set of rules", "It blocks those that do not meet the rules"]) + "</p>", None) + req("3 marks", "Explain", "Explain how encryption protects data that is intercepted on the internet.", "Cipher text, key.", "<p>" + mks(["The data is converted to cipher text using a key", "An interceptor sees only cipher text", "It cannot be understood without the decryption key"]) + "</p>", None) + req("2 marks", "Describe", "Describe how two-factor authentication improves security.", "Second form of verification.", "<p>" + mks(["A second form of verification is needed after the password, such as an authenticator code or biometrics", "so a stolen password alone is not enough to log in"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a company keeps back-ups even though it has a firewall.", "Recovery.", "<p>" + mks(["A firewall cannot prevent all loss or corruption (for example hardware failure or malware)", "back-ups allow the data to be recovered"]) + "</p>", None)

tips = tips_html([
  ("Security: loss. Privacy: access.", "Integrity: accuracy."),
  ("Name it and say how it works.", "Firewall: rules on packets."),
  ("Encryption: cipher text.", "Useless without the key."),
  ("Digital signature: hash, private key.", "Receiver compares two digests."),
  ("Checks protect integrity.", "Not security."),
  ("Back-up for recovery.", "It does not prevent loss."),
], [("data privacy", "Only authorised people can access the data."), ("data integrity", "The accuracy, completeness and consistency of data."), ("cipher text", "Data after encryption."), ("a digest", "The output of a hashing algorithm.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Match", "Link each measure to its description.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const pk = [["port 80 (web)", 1], ["port 4444 (unknown)", 0], ["port 443 (secure web)", 1]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Internet", "lbl bd") + SV.rect(210, 30, 40, 120, "f3", { rx: 6 }) + SV.text(230, 95, "firewall", "sm", { "text-anchor": "middle", style: "transform-origin:230px 95px;transform:rotate(-90deg)" }) + SV.text(380, 20, "Computer", "lbl bd");
    pk.forEach(([n, ok], i) => { if (i <= k) o += SV.rect(30, 40 + i * 36, 160, 28, ok ? "f1" : "f2", { rx: 4 }) + SV.text(40, 59 + i * 36, n, "lbl", { style: "font-size:12px" }); if (i < k || (i === k && false)) {} }); pk.forEach(([n, ok], i) => { if (ok && i <= k) o += SV.rect(290, 40 + i * 36, 160, 28, "f1", { rx: 4 }) + SV.text(300, 59 + i * 36, n, "lbl", { style: "font-size:12px" }) + SV.path(`M250,${54 + i * 36} H290`, "ax"); if (!ok && i <= k) o += SV.text(260, 59 + i * 36, "✗", "lbl bd", { style: "fill:var(--bad)" }); });
    o += SV.text(20, 170, ["", "web traffic matches the allow rule: it passes", "an unknown port is not allowed: blocked", "secure web traffic matches the rules: it passes"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 190, label: "Firewall", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The firewall monitors incoming and outgoing packets.", "Port 80 matches the rules: <b>allowed</b>.", "Port 4444 is not allowed: <b>blocked</b>.", "Port 443 matches the rules: <b>allowed</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "plain text", true) + B(160, "encrypt (key)", k >= 1) + B(310, "cipher text", k >= 2) + B(460, "decrypt (key)", k >= 3) + SV.path("M130,62 H160", "ax") + SV.path("M280,62 H310", "ax") + SV.path("M430,62 H460", "ax");
    o += SV.text(300, 125, ["HELLO", "", "KHOOR (interceptor sees this)", "HELLO again, only with the key"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 150, label: "Encryption", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The message is plain text.", "It is encrypted using a key.", "Cipher text is sent: if intercepted it cannot be understood.", "The receiver decrypts it with the key."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, on) => SV.rect(x, y, w, 36, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + w / 2, y + 23, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, 20, 100, "message", true) + B(150, 20, 100, "hash → digest", k >= 1) + B(290, 20, 150, "encrypt: private key", k >= 2) + B(10, 90, 150, "decrypt: public key", k >= 3) + B(200, 90, 150, "hash message again", k >= 4) + B(390, 90, 100, "same digest?", k >= 5);
    if (k >= 1) o += SV.path("M110,38 H150", "ax"); if (k >= 2) o += SV.path("M250,38 H290", "ax"); if (k >= 4) o += SV.path("M160,108 H200", "ax"); if (k >= 5) o += SV.path("M350,108 H390", "ax"); o += SV.text(20, 160, k >= 5 ? "If the digests match, the message is authentic and unchanged" : "", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 175, label: "Digital signature", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The sender has a message.", "It is hashed to produce a <b>digest</b>.", "The digest is encrypted with the sender's <b>private key</b> (the signature).", "The receiver decrypts the signature with the sender's <b>public key</b>.", "The receiver hashes the received message.", "The two digests are <b>compared</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let len = 8, set = 62; const sets = { 10: "digits only", 26: "lower-case letters", 52: "upper and lower case", 62: "upper, lower and digits", 94: "all keyboard characters" };
  const paint = () => { const n = Math.pow(set, len); const f = (x) => x >= 1e15 ? (x / 1e15).toFixed(1) + " quadrillion" : x >= 1e12 ? (x / 1e12).toFixed(1) + " trillion" : x >= 1e9 ? (x / 1e9).toFixed(1) + " billion" : x >= 1e6 ? (x / 1e6).toFixed(1) + " million" : x.toLocaleString(); $("#pV").innerHTML = `A <b>${len}</b>-character password from a set of <b>${set}</b> characters (${sets[set]}) has <b>${f(n)}</b> possible combinations. Longer passwords and a bigger set of characters make guessing far harder.`; };
  Lib.slider($("#pS1"), { id: "p1", label: "Length ", min: 4, max: 16, value: len, fmt: (x) => x, onInput: (v) => { len = v; paint(); } });
  const sl = $("#pS2"); [10, 26, 52, 62, 94].forEach((k) => { const b = document.createElement("button"); b.textContent = k + " chars"; b.onclick = () => { set = k; sl.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); paint(); }; if (k === set) b.className = "on"; sl.appendChild(b); }); paint();
})();
(function () {
  let shift = 3; const msg = "SECURITY"; const paint = () => { const enc = msg.split("").map((c) => String.fromCharCode(((c.charCodeAt(0) - 65 + shift) % 26) + 65)).join(""); $("#eV").innerHTML = `Plain text <b>${msg}</b>, key (shift) <b>${shift}</b> → cipher text <b>${enc}</b>. Without the key the cipher text is hard to understand; with it, shifting back gives <b>${msg}</b>. (A Caesar cipher is easy to break: real encryption uses very long keys.)`; };
  Lib.slider($("#eS"), { id: "e1", label: "Key (shift) ", min: 1, max: 25, value: shift, fmt: (x) => x, onInput: (v) => { shift = v; paint(); } }); paint();
})();
btnTable("mB", "mO", [
  ["Firewall", "Data security", "Blocks packets that fail the rules"],
  ["Password", "Data security", "Proves identity"],
  ["Double entry", "Data integrity", "Checks data is the same as the original"],
  ["Presence check", "Data integrity", "Validation"],
  ["Access rights", "Data security", "Limits what each user can do"],
  ["Back-up", "Data security", "Recovery of lost data"]
], ["Measure", "Protects", "Why"]);
''' + _prjs

finish("as-6-1-1-security-privacy-integrity", "as611", "Data Security, Privacy and Integrity",
  "Data security, privacy and integrity defined, and the security measures: passwords, biometrics, firewalls, anti-malware, encryption, digital signatures and back-ups, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "6.1.1", "6 · Security, privacy and data integrity", "section 6.1 Data security", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on data security, privacy and integrity and the security measures (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
