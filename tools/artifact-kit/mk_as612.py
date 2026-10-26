"""AS CS 6.1.2: security threats and how to restrict them. Run: python3 tools/artifact-kit/mk_as612.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>threat</b> is something that can harm data or a computer system. <b>Malware</b> (malicious software) includes <b>viruses</b>, which replicate themselves and can corrupt, delete or fill storage, and <b>spyware</b>, which is installed without the user's knowledge, secretly records their actions (such as keystrokes) and sends them to a third party. <b>Phishing</b> uses an email pretending to be from an official body to persuade people to disclose private information or click a link to a fake site; <b>pharming</b> uses malicious code on the computer to redirect the user to a fake website automatically. A <b>hacker</b> is a person who gains unauthorised access to a computer system. Each threat is restricted by a matching measure: anti-malware, firewalls, strong passwords and multi-factor authentication, user training and care in what is downloaded.</p></div>

  <h2>1 · The threats</h2>
  <div class="tw"><table class="t">
    <tr><th>Threat</th><th>What it is</th><th>What it does</th></tr>
    <tr><td><b>Virus</b></td><td>Malicious software that replicates (copies) itself</td><td>Corrupts, deletes or changes files and data, or fills storage</td></tr>
    <tr><td><b>Spyware</b></td><td>Malware downloaded or installed without the user's knowledge</td><td>Secretly records the user's actions or keystrokes and sends the logs to a third party; runs in the background</td></tr>
    <tr><td><b>Phishing</b></td><td>An email (or message) that pretends to be from an official body, such as a bank</td><td>Persuades people to disclose private information such as bank details, or to click a link to an unofficial website: it needs the user to act</td></tr>
    <tr><td><b>Pharming</b></td><td>Malicious code or software installed on a computer</td><td>Redirects the user to a fake website to obtain personal data, automatically (no user action needed)</td></tr>
    <tr><td><b>Hacker</b></td><td>A person who gains unauthorised access to a computer system</td><td>Can delete, damage or steal data, or install malware</td></tr>
  </table></div>

  <h2>2 · Comparing threats</h2>
  <ul>
    <li><b>Spyware and virus, similarities:</b> both are malicious software; both are installed or run without the user's knowledge; both can be hidden in legitimate software and can try to avoid the firewall; both run in the background.</li>
    <li><b>Spyware and virus, differences:</b> a virus replicates itself and can damage data; spyware does not replicate, it only records data and sends it to a third party.</li>
    <li><b>Phishing and pharming, similarities:</b> both try to obtain financial or personal information; both falsely represent an official organisation (a bank); both make use of fake websites.</li>
    <li><b>Phishing and pharming, differences:</b> phishing uses an email to prompt the user to act; pharming is malicious code that redirects to a fake website automatically.</li>
  </ul>

  <h2>3 · Restricting the risk</h2>
  <div class="tw"><table class="t">
    <tr><th>Threat</th><th>Measure</th><th>How it works</th></tr>
    <tr><td>Virus, malware</td><td>Anti-virus or anti-malware</td><td>Scans files, downloads and devices and compares them with a database of known viruses; quarantines or deletes a match or alerts the user. Keep the definitions up to date</td></tr>
    <tr><td>Spyware</td><td>Anti-spyware, firewall, a virtual (on-screen) keyboard</td><td>Detects and removes the program; the firewall blocks it sending data out; an on-screen keyboard defeats a keystroke logger</td></tr>
    <tr><td>Hacker</td><td>Firewall, strong passwords, multi-factor authentication, access rights</td><td>The firewall monitors traffic and blocks transmissions that are not allowed; a strong password mixes character types and is long; multi-factor authentication needs a second form of verification</td></tr>
    <tr><td>Phishing</td><td>Training and careful checking</td><td>Do not click links in unexpected emails; check the sender and address; use a spam filter</td></tr>
    <tr><td>Pharming</td><td>Anti-malware, checking for the secure padlock and address</td><td>Remove the malicious code; verify the website</td></tr>
    <tr><td>Malware in general</td><td>Download only from reputable sources; keep back-ups; deny administrator rights to everyday users; avoid removable devices</td><td>Reputable sources are less likely to contain malware; a back-up restores data lost to malware; fewer rights means everyday users cannot install it</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Describing malware as "a virus that damages computers". Describe the specific behaviour, such as replicating or recording keystrokes.</li>
    <li>Giving a threat with no description, or a measure with no explanation of how it works.</li>
    <li>Repeating the same measure for two threats when the question says each measure must be different.</li>
    <li>Mixing phishing and pharming. Phishing needs the user to click; pharming redirects automatically.</li>
    <li>Describing a hacker as someone with "malicious intent". The key idea is unauthorised access.</li>
  </ul>
'''

watch = '''
  <h2>1 · A virus replicates</h2>
  <div id="stA"></div>
  <h2>2 · Spyware sends data out</h2>
  <div id="stB"></div>
  <h2>3 · Phishing against pharming</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Virus spread</h2>
  <p>A virus that replicates spreads quickly. Change how many copies each infected file makes.</p>
  <div class="card"><div id="vS1"></div><div id="vS2"></div><div id="vG"></div><div id="vV" class="verdict"></div></div>
  <h2>Lab 2 · Which threat?</h2>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>
  <h2>Lab 3 · Phishing email or genuine?</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

_pr, _prjs = PR(["Which threat?", "Phishing or pharming?", "Match the threat to its description", "Put the phishing attack in order", "Working out", "Multiple choice"],
  ("Which threat does it describe?", ["Virus", "Spyware", "Phishing", "Pharming", "Hacker"], [("Replicates itself and corrupts files", 0), ("Records keystrokes and sends them to a third party", 1), ("An email pretending to be a bank asking for details", 2), ("Redirects the user to a fake website automatically", 3), ("A person with unauthorised access to a system", 4), ("Installed without the user's knowledge, runs in the background", 1)], "Match each description."),
  ("Phishing or pharming?", ["Phishing", "Pharming"], [("Uses an email to prompt user action", 0), ("Malicious code redirects to a fake site", 1), ("Needs the user to click a link", 0), ("Happens automatically", 1), ("Asks you to reply with your bank details", 0), ("Installed on the computer", 1)], "Phishing: user acts. Pharming: automatic."),
  [["Virus", "Malicious software that replicates itself"], ["Spyware", "Secretly records user actions and sends them on"], ["Phishing", "An email that pretends to be from an official body"], ["Pharming", "Malicious code that redirects to a fake website"], ["Hacker", "Gains unauthorised access to a computer system"]],
  ("Put the phishing attack in order.", ["A fake email pretends to be from a bank", "It asks the user to click a link", "The link opens a fake website", "The user enters their bank details", "The details are sent to the criminal"], "Email, link, fake site, details, sent."),
  [{"q": "A virus infects 1 file and every infected file infects 2 new files per hour. How many infected files after 4 hours (including the original, cumulative)?", "a": 31, "unit": "", "tol": 0.01, "hint": "1 + 2 + 4 + 8 + 16.", "sol": "<b>31</b>."}, {"q": "Spyware records 50 keystrokes each minute. How many keystrokes in an hour?", "a": 3000, "unit": "", "tol": 0.01, "hint": "50 × 60.", "sol": "<b>3000</b>."}, {"q": "An anti-malware database has 2 million known viruses and adds 5000 a day. How many after 10 days?", "a": 2050000, "unit": "", "tol": 0.5, "hint": "2 000 000 + 50 000.", "sol": "<b>2 050 000</b>."}, {"q": "A school sends 800 emails; 2% are phishing. How many phishing emails?", "a": 16, "unit": "", "tol": 0.01, "hint": "2% of 800.", "sol": "<b>16</b>."}, {"q": "A password has 8 characters from 26 letters. How many possible passwords, in billions (1 d.p.)?", "a": 208.8, "unit": "billion", "tol": 0.2, "hint": "26^8 = 208 827 064 576.", "sol": "about <b>208.8</b> billion."}],
  [("A virus:", ["Replicates itself", "Only records keystrokes", "Is a person", "Is an email"], 0, "Replicates."), ("Spyware:", ["Sends recorded data to a third party", "Redirects to fake sites", "Blocks ports", "Creates back-ups"], 0, "Sends data out."), ("Pharming:", ["Redirects to a fake website automatically", "Needs a user click", "Is a measure", "Is a firewall"], 0, "Automatic redirect."), ("A hacker:", ["Gains unauthorised access", "Updates software", "Compresses files", "Formats a disk"], 0, "Unauthorised access."), ("Anti-malware:", ["Scans against known malware", "Redirects traffic", "Encrypts emails", "Slows the CPU"], 0, "Scans."), ("A back-up helps against malware by:", ["Restoring lost data", "Blocking packets", "Detecting phishing", "Hiding passwords"], 0, "Restoring data.")],
  [("Virus", "Replicates; corrupts or deletes data."), ("Spyware", "Records and sends to a third party."), ("Phishing", "Email; user acts; fake site."), ("Pharming", "Code redirects automatically."), ("Hacker", "Unauthorised access."), ("Anti-malware", "Scan, quarantine, update."), ("Firewall", "Blocks unwanted packets."), ("Strong password", "Long; mixed characters.")])

real = RWNOTE + (
rw("An email 'from your bank'", "It asks you to click a link and enter your login. The sender address and link are slightly wrong: this is phishing.", "phishing.") +
rw("A keystroke logger in a free program", "A free download secretly records everything you type, including passwords, and sends it to the attacker.", "spyware.") +
rw("Typing the right web address and still getting a fake page", "Malicious code on your computer sends you to a fake copy of the site: pharming.", "pharming.") +
rw("A school server breached", "Someone guessed a weak password and gained unauthorised access: a hacker.", "hacker; strong passwords and multi-factor authentication.") +
rw("A USB stick from a stranger", "Plugging it in can install malware, which is why removable devices are avoided.", "malware restriction.")
)

where = [
  ("O/N 2021", "11, 13", "2(c)", "3", "Two similarities and a difference between spyware and a virus"),
  ("M/J 2022", "11", "3(b)", "6", "Two threats to exam papers on a laptop, each with a security measure"),
  ("M/J 2022", "12", "4(b)", "6", "Two security threats, their descriptions and prevention"),
  ("O/N 2023", "12", "5(c)", "4", "Describe a phishing email and spyware"),
  ("O/N 2023", "13", "8(b), (c)", "2 + 3", "A difference and a similarity between pharming and phishing; how the risks of malware can be restricted"),
  ("O/N 2025", "11", "8(a)", "2", "What a virus and pharming are"),
  ("M/J 2026", "12", "2(c)", "3 + 3", "Describe a virus and a hacker and a method to restrict each")]

past = '''  <p class="note">Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The threats are always asked in the same triple: name the threat, describe it, give a different measure. Description and prevention are separate marks.</p>
''' + peq(SRC("w21", "11/13", "Q2(c)"), "3 marks", "Give",
  "Two malware threats are spyware and viruses. Give two similarities and one difference between spyware and a virus.", "Both malicious, both unknown to the user. Virus replicates, spyware records.",
  "<p>Similarities, any two: " + mks(["Both are pieces of malicious software", "Both are downloaded, installed or run without the user's knowledge", "Both can pretend to be, or be embedded in, legitimate software", "Both run in the background"]) + "</p><p>Difference, any one: " + mks(["A virus can damage computer data; spyware only records or accesses data", "A virus does not send data out of the computer; spyware sends recorded data to a third party", "A virus replicates itself; spyware does not"], "a") + "</p>", None) + peq(SRC("s22", "11", "Q3(b)"), "6 marks", "Identify / Describe",
  "A teacher is writing examination papers on a laptop connected to the internet. Identify and describe two threats to the data. Identify one security measure to protect against each threat. Each security measure must be different.", "Malware, hacker, spyware, each with a description and a different measure.",
  "<p>One mark for the threat, one for its description and one for the measure, twice: " + mks(["Malware: malicious software that replicates and can delete or damage the papers; install and run anti-malware", "Hacker: illegal access in order to delete or damage the papers; use a firewall or strong passwords", "Spyware: software installed without the teacher's knowledge which records keystrokes and sends the data to a third party; use a firewall, anti-spyware or a virtual keyboard"]) + "</p>", "Using 'firewall' for both threats. The measures must be different.") + peq(SRC("s22", "12", "Q4(b)"), "6 marks", "Complete",
  "Complete the table by identifying two security threats to the data on a computer. Describe each threat. Give a different prevention method for each threat.", "Virus: replicates and corrupts. Hacker: unauthorised access.",
  "<p>One mark for each threat, its description and its prevention (two threats): " + mks(["Virus: malicious software that replicates itself and can corrupt data; anti-virus, firewall or anti-malware", "Hacker: unauthorised access to the computer with malicious intent; firewall, strong or biometric passwords, or user permissions"]) + "</p>", None) + peq(SRC("w23", "12", "Q5(c)"), "4 marks", "Describe",
  "Describe the following threats to a computer system: phishing email; spyware.", "Pretends to be official, asks for information or a click. Secretly records and sends logs.",
  "<p>Phishing email (max 2): " + mks(["The email pretends to be from an official body", "persuading individuals to disclose private information, such as bank details", "or requesting authentication by redirecting to an unofficial website, or inviting a user to click a link"]) + "</p><p>Spyware (max 2): " + mks(["Malware downloaded without the user's knowledge", "which secretly records the user's actions or keystrokes on the computer", "and sends logs of the actions to a third party"], "a") + "</p>", None) + peq(SRC("w23", "13", "Q8(b)(c)"), "2 + 3 marks", "State / Explain",
  "(b) State one difference and one similarity between pharming and phishing. (c) Explain how the data security risks of malware can be restricted.", "Automatic redirect against email prompt; both seek personal information. Reputable sources, back-up, anti-malware, firewall, rights.",
  "<p><b>(b)</b> " + mks(["Difference: pharming is malicious code that redirects to a fake website, whereas phishing uses an email to prompt user action (or pharming is automatic, phishing needs user action)", "Similarity: both try to obtain financial or personal information; both falsely represent an official organisation; both make use of fake websites"]) + "</p><p><b>(c)</b> Any three: " + mks(["Download programs from reputable sources, as they are less likely to contain malware", "Back up computer systems so they can be restored after data loss from malware", "Install and run an anti-malware program so regular scans find and remove or quarantine malware, with definitions kept up to date", "Use a firewall to block unused ports so malware cannot enter", "Deny administrator privileges to everyday users so malware cannot be downloaded by them", "Avoid removable devices so malware cannot be installed from them"], "a") + "</p>", None) + peq(SRC("w25", "11", "Q8(a)"), "2 marks", "Explain",
  "Viruses and pharming are examples of malware. Explain what is meant by a virus and pharming.", "Replicates and alters files. Redirects to a fake site.",
  "<p>" + mks(["Virus: malicious program or software that replicates itself and deletes or alters files or data stored on a computer", "Pharming: malicious code installed on a computer which redirects the user to a fake website to obtain personal data"]) + "</p>", None) + peq(SRC("s26", "12", "Q2(c)"), "3 + 3 marks", "Describe",
  "Personal data needs to be kept secure whilst on the computer. (i) Describe what is meant by a virus, and identify and describe one method to restrict the risk. (ii) Describe what is meant by a hacker, and identify and describe one method to restrict the risk.", "Virus: replicates and fills storage or damages data; anti-malware scans. Hacker: unauthorised access; firewall, MFA, strong password.",
  "<p><b>(i)</b> " + mks(["Description: malicious software that replicates on the computer and can fill storage or delete, corrupt or change data", "Method: anti-virus or anti-malware software", "Description: scans files, downloads or devices and compares against a database of known viruses, and quarantines, deletes or alerts the user if a match is found"]) + "</p><p><b>(ii)</b> " + mks(["Description: a person who gains unauthorised access to a computer system", "Method: firewall, multi-factor authentication, strong passwords or encryption", "Description: for example the firewall monitors all data compares it to stored criteria and blocks transmissions that are not allowed; MFA requires a second form of verification such as biometrics or an authenticator app"], "a") + "</p>", "Writing 'a hacker has malicious intent'. The mark is for unauthorised access.")

review = req("3 marks", "Describe", "Describe how spyware could steal a student's online banking password.", "Keystrokes, send.", "<p>" + mks(["Spyware is installed without the student knowing", "It secretly records the keystrokes as they type", "and sends the log to a third party"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between phishing and pharming.", "Email and click against automatic redirect.", "<p>" + mks(["Phishing uses an email to persuade the user to disclose information or click a link", "Pharming uses malicious code to redirect to a fake website automatically"]) + "</p>", None) + req("2 marks", "Explain", "Explain two ways a school can reduce the risk of malware.", "Anti-malware; reputable sources; rights.", "<p>" + mks(["Install and run anti-malware software that scans for known malware", "Do not give administrator rights to everyday users so they cannot install malware"]) + "</p>", None) + req("2 marks", "Describe", "Describe what a hacker is.", "Unauthorised access.", "<p>" + mks(["A person who gains unauthorised access to a computer system", "who can then delete, damage or steal data"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a back-up does not stop a virus but is still useful.", "Recovery.", "<p>" + mks(["A back-up does not prevent infection", "but the data can be restored if the virus corrupts or deletes it"]) + "</p>", None)

tips = tips_html([
  ("Threat, description, measure.", "Three separate marks."),
  ("Different measure for each threat.", "Do not repeat 'firewall'."),
  ("Virus replicates.", "Spyware records and sends."),
  ("Phishing: the user acts.", "Pharming: automatic redirect."),
  ("Hacker: unauthorised access.", "Say it in those words."),
  ("Say how the measure works.", "Scan, compare, quarantine; check packets."),
], [("malware", "Malicious software such as a virus or spyware."), ("phishing", "A fake email that asks the user to disclose information or click."), ("pharming", "Code that redirects the user to a fake website."), ("a hacker", "A person who gains unauthorised access to a system.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Identify", "Name the threat or measure.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const n = [1, 2, 4, 8][k]; let o = ""; for (let i = 0; i < 8; i++) o += SV.rect(30 + i * 60, 40, 52, 40, i < n ? "f2" : "cell", { rx: 6 }) + SV.text(56 + i * 60, 65, i < n ? "infected" : "file", "sm", { "text-anchor": "middle" });
    o += SV.text(30, 120, [`${n} infected file`, `${n} infected files: each copied itself once`, `${n} infected files: it keeps replicating`, `${n} infected files: it fills storage and corrupts data`][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 140, label: "Virus", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["One file is infected by a virus.", "The virus <b>replicates</b> itself into other files.", "It copies itself again.", "It can fill storage and <b>corrupt or delete</b> data."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 120, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(10, "User types", true) + B(180, "Spyware (hidden)", k >= 1) + B(350, "Third party", k >= 3) + SV.path("M130,62 H180", "ax") + SV.path("M300,62 H350", "ax", { style: k >= 2 ? "stroke:var(--bad);stroke-width:3" : "" });
    o += SV.text(260, 125, ["", "installed without the user knowing; runs in the background", "it records keystrokes", "and sends the log to a third party"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 500, h: 145, label: "Spyware", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A user types a password.", "<b>Spyware</b> is running in the background.", "It <b>records</b> every keystroke.", "It <b>sends</b> the data to a third party."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Phishing", "lbl bd") + SV.text(300, 20, "Pharming", "lbl bd") + SV.rect(20, 30, 230, 34, "cell", { rx: 6 }) + SV.text(30, 52, k >= 1 ? "email: 'click here'" : "", "lbl", { style: "font-size:12px" }) + SV.rect(300, 30, 230, 34, "cell", { rx: 6 }) + SV.text(310, 52, k >= 2 ? "user types the real address" : "", "lbl", { style: "font-size:12px" });
    if (k >= 3) o += SV.rect(20, 80, 230, 34, "f2", { rx: 6 }) + SV.text(30, 102, "user clicks: fake website", "lbl", { style: "font-size:12px" }) + SV.rect(300, 80, 230, 34, "f2", { rx: 6 }) + SV.text(310, 102, "code redirects: fake website", "lbl", { style: "font-size:12px" });
    o += SV.text(20, 150, k >= 3 ? "Phishing needs the user to act; pharming redirects automatically." : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 560, h: 170, label: "Phishing and pharming", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Both aim to get personal data through a fake website.", "<b>Phishing</b> starts with an email that tells the user to click.", "<b>Pharming</b> starts with malicious code on the computer.", "Phishing needs <b>user action</b>; pharming is <b>automatic</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let copies = 2, hours = 5; const paint = () => { let a = 1, t = [1]; for (let h = 1; h <= hours; h++) { a *= copies; t.push(t[t.length - 1] + a); } const mx = Math.max(...t); let o = '<svg viewBox="0 0 420 150" style="width:420px;max-width:100%;display:block"><path d="M30,10 V130 H400" class="ax"/>'; t.forEach((v, i) => { const hgt = (Math.log(v + 1) / Math.log(mx + 1)) * 110; o += `<rect x="${40 + i * (350 / t.length)}" y="${130 - hgt}" width="${300 / t.length}" height="${hgt}" fill="var(--bad)" opacity=".7"/>`; }); $("#vG").innerHTML = o + `<text x="400" y="146" class="sm" text-anchor="end" style="font-size:11px">hours</text></svg>`;
    $("#vV").innerHTML = `If every infected file infects <b>${copies}</b> new file(s) each hour, after <b>${hours}</b> hours there are <b>${t[t.length - 1].toLocaleString()}</b> infected files. Replication makes a virus spread fast, which is why anti-malware needs to be running and up to date.`; };
  Lib.slider($("#vS1"), { id: "v1", label: "New infections per infected file per hour ", min: 1, max: 5, value: copies, fmt: (x) => x, onInput: (v) => { copies = v; paint(); } });
  Lib.slider($("#vS2"), { id: "v2", label: "Hours ", min: 1, max: 8, value: hours, fmt: (x) => x, onInput: (v) => { hours = v; paint(); } }); paint();
})();
btnTable("tB", "tO", [
  ["Records every key you press and sends it away", "Spyware", "Secretly records and sends to a third party"],
  ["Copies itself into other files and corrupts them", "Virus", "Replicates"],
  ["Email asking you to confirm your bank details by clicking a link", "Phishing", "Needs the user to act"],
  ["Types bank.com and lands on a copy of the site", "Pharming", "Redirected automatically"],
  ["Guesses a weak password and logs in as a teacher", "Hacker", "Unauthorised access"]
], ["Description", "Threat", "Key idea"]);
btnTable("eB", "eO", [
  ["'Your account is locked, click this link now', from a strange address", "Phishing", "Urgent, unexpected, suspicious sender"],
  ["Message from your school about a timetable, from the school domain, no link", "Genuine", "Expected and no request for details"],
  ["'You have won a prize: send your card number'", "Phishing", "Asks for private information"],
  ["Receipt for something you bought, address matches the shop", "Genuine", "Expected and matches"]
], ["Email", "Verdict", "Why"]);
''' + _prjs

finish("as-6-1-2-security-threats", "as612", "Security Threats: Malware, Phishing, Pharming, Hackers",
  "Viruses, spyware, phishing, pharming and hackers, how they differ and how each risk can be restricted, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "6.1.2", "6 · Security, privacy and data integrity", "section 6.1 Data security", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on security threats (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
