"""A Level CS syllabus 17.1.2: quantum cryptography. Run: python3 tools/artifact-kit/mk_ac1712.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Quantum cryptography</b> uses the laws of <b>quantum physics</b>, the properties of <b>photons</b> (particles of light), instead of mathematical formulae to create and exchange encryption keys, aiming to give a <b>virtually unbreakable</b> system. Photons are sent down a <b>fibre-optic cable</b> with a polarisation that carries the bits of the key. Measuring a photon <b>changes its state</b>, so if someone <b>eavesdrops</b> the errors this causes can be detected and the key thrown away and another requested. Quantum states cannot be copied (the <b>no-cloning</b> theorem), so the key cannot be duplicated and kept for later. The drawbacks are the <b>cost</b>, the need for <b>dedicated fibre and specialist hardware</b>, a <b>limited range</b>, and that polarisation can be altered on the way, giving errors.</p></div>

  <h2>1 · Purpose</h2>
  <p>Ordinary encryption is protected by hard mathematics: the keys are safe only as long as nobody can work out the answer fast enough. Quantum cryptography is used to:</p>
  <ul>
    <li>provide a <b>virtually unbreakable</b> method of encryption, or send virtually un-hackable secure messages;</li>
    <li>do this using the <b>laws and principles of quantum mechanics</b> (properties of photons) rather than mathematical algorithms;</li>
    <li><b>detect eavesdropping</b>, because the properties of photons change when they are observed;</li>
    <li>protect the security of data sent over <b>fibre-optic cables</b>, and allow <b>longer keys</b> to be exchanged.</li>
  </ul>
  <p>Its job on this syllabus is the secure <b>exchange of keys</b>: when the keys have been exchanged securely, the message itself is sent.</p>

  <h2>2 · How it works (the idea)</h2>
  <ol>
    <li>The sender sends a stream of photons, each given one of several polarisations that stand for a 0 or a 1.</li>
    <li>The receiver measures each photon and records the bit.</li>
    <li>If an eavesdropper measures a photon on its way, they disturb its state, and the receiver gets some bits wrong.</li>
    <li>The two sides compare a sample of their bits over an ordinary channel. If more errors appear than the equipment would cause alone, an <b>eavesdropper is detected</b>, the key is discarded and a new one is requested.</li>
    <li>If the sample matches, the rest of the bits form a secret key, which is then used to encrypt the message.</li>
  </ol>

  <h2>3 · Benefits and drawbacks</h2>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>Security based on laws of physics rather than mathematical algorithms, so more secure; virtually unhackable</td><td>High cost of purchasing and maintaining the equipment: a dedicated fibre-optic line and specialist hardware</td></tr>
    <tr><td>Eavesdropping can be detected, so the receiver can request another key</td><td>Currently only works over relatively short distances</td></tr>
    <tr><td>Keys cannot be duplicated (no-cloning)</td><td>The technology is not yet readily available; error rates are relatively high</td></tr>
    <tr><td>Protects data sent over fibre-optic cables; longer keys can be used</td><td>Polarisation of the light may be changed while travelling down the fibre</td></tr>
    <tr><td>Suits the most valuable government and industrial secrets</td><td>Lacks features such as digital signatures; allows criminals to hide their communications</td></tr>
  </table></div>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Saying quantum cryptography is "uncrackable" with no reason. Say it uses the laws of physics and detects eavesdropping.</li>
    <li>Giving the drawback "it is expensive" only. Say what costs: dedicated fibre and specialist hardware.</li>
    <li>Writing that it protects data on wireless networks. It relies on fibre-optic cables.</li>
    <li>Confusing it with asymmetric encryption: quantum cryptography is a different, third type used to exchange keys safely.</li>
    <li>Giving two benefits that mean the same thing, such as "secure" and "hard to hack". Pick two different ideas.</li>
  </ul>
'''

watch = '''
  <h2>1 · Sending key bits with photons</h2>
  <p>Press Play. Without an eavesdropper every bit arrives correctly.</p>
  <div id="stA"></div>
  <h2>2 · An eavesdropper is detected</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Detecting an eavesdropper</h2>
  <p>Send photons from the sender to the receiver. Turn the eavesdropper on and see how many bits in the comparison sample disagree.</p>
  <div class="card"><div class="btnrow" id="eB"></div><div id="eS"></div><div id="eT"></div><div class="verdict" id="eV"></div></div>

  <h2>Lab 2 · Benefit or drawback?</h2>
  <div class="card"><div id="bB" class="btnrow"></div><div id="bO"></div></div>
'''

practise = '''
  <h2>1 · Benefit or drawback of quantum cryptography?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which type of cryptography?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of a quantum key exchange in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Banks and governments", "Organisations with very valuable secrets can use quantum key exchange between two sites linked by fibre. If anyone taps the cable, the errors reveal it.", "eavesdropping can be detected.") +
rw("Satellite experiments", "Because fibre only works over short distances, researchers have sent quantum keys by satellite to test longer links.", "range is a limit for fibre-based systems.") +
rw("Future-proofing", "Some computers of the future could break today's mathematical encryption. Quantum cryptography does not rely on that mathematics.", "security from physics, not algorithms.") +
rw("Opening a sealed envelope", "A paper letter in a wax-sealed envelope shows if someone has opened it. Measuring a photon changes it in the same way, so tampering shows.", "observing a quantum state disturbs it.") +
rw("Dedicated lines", "Quantum links need their own fibre and special hardware, which is why they are used by a few large organisations and not by ordinary home users.", "high cost and specialist hardware.")
)

where = [
  ("M/J 2022", "31, 33", "8(b)", "2 + 2", "Two benefits and two drawbacks of quantum cryptography"),
  ("M/J 2023", "31, 33", "9(b)", "2 + 2", "Two benefits and two drawbacks of quantum cryptography"),
  ("O/N 2023", "32", "5(a)", "2", "The purpose of quantum cryptography"),
  ("M/J 2026", "33", "8", "2 + 2 + 2", "The purpose of quantum cryptography; two benefits and two drawbacks")]

past = '''  <p class="note">Quantum cryptography has appeared in Paper 3 in 2022, 2023 and 2026, and is asked as a purpose, then two benefits and two drawbacks. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s22", "31/33", "Q8(b)"), "2 + 2 marks", "State",
  "When there is a secure exchange of key(s), the message is sent. The use of quantum cryptography is being considered for the secure exchange. (i) State two possible benefits of using quantum cryptography. (ii) State two possible drawbacks of using quantum cryptography.",
  "Eavesdropping detected; longer keys. Drawbacks: dedicated fibre and cost; range.",
  "<p><b>(i)</b> Any two: " + mks(["Any eavesdropping can be identified, as the state will be changed", "The integrity of the key once transferred can be guaranteed (it cannot be copied and decrypted at a later date)", "Longer, more secure keys can be exchanged"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Limited range", "Requires a dedicated fibre-optic line and specialist hardware", "The cost of the dedicated line and specialist hardware is expensive", "The polarisation of light may be altered whilst travelling down fibre-optic cables"], "a") + "</p>", None) + peq(SRC("s23", "31/33", "Q9(b)"), "2 + 2 marks", "Identify",
  "Encryption is used to alter data into a form that makes it meaningless if intercepted. Identify two benefits and two drawbacks of quantum cryptography.",
  "Two different benefits and two different drawbacks.",
  "<p><b>Benefits</b>, any two: " + mks(["Security based on the laws of physics rather than mathematical algorithms, so more secure", "Protects the security of data transmitted over fibre-optic cables", "Virtually unhackable", "Its performance is continuously improved, making it suitable for the most valuable government and industrial secrets", "Longer keys can be used", "Eavesdropping can be detected"]) + "</p><p><b>Drawbacks</b>, any two: " + mks(["Lacks many vital features such as digital signatures and certified mail", "High cost of purchasing and maintaining the equipment", "Currently only works over relatively short distances", "Error rates are relatively high as the technology is still being developed", "The polarisation of light can change during transmission", "Allows criminals and terrorists to hide their communications"], "a") + "</p>", "Giving 'it is secure' and 'it is unhackable' as two benefits. They are the same point.") + peq(SRC("w23", "32", "Q5(a)"), "2 marks", "Describe",
  "Encryption is used to scramble data to make it meaningless if intercepted. Describe the purpose of quantum cryptography.",
  "Virtually unbreakable, using physics, detects eavesdropping.",
  "<p>Any two: " + mks(["To produce a virtually unbreakable encryption system, or to send virtually un-hackable secure messages", "using the laws or principles of quantum mechanics, or the properties of photons", "To detect eavesdropping", "because the properties of photons change", "To protect the security of data transmitted over fibre-optic cables", "To enable the use of longer keys"]) + "</p>", None) + peq(SRC("s26", "33", "Q8"), "2 + 2 + 2 marks", "Describe / Outline",
  "(a) Describe the purpose of quantum cryptography. (b) Outline two benefits and two drawbacks of quantum cryptography.",
  "(a) more secure than current methods, using quantum physics rather than formulae.",
  "<p><b>(a)</b> Any two: " + mks(["To provide a more secure method of encryption than current methods, a virtually unbreakable method, or to detect eavesdropping", "using the laws of quantum physics rather than mathematical formulae to generate keys", "To provide encryption that can be guaranteed for a longer period than current methods"]) + "</p><p><b>(b) Benefits</b>, any two: " + mks(["Better security for internet communication", "Can detect eavesdropping, enabling the receiver to request another key", "Virtually unhackable due to rapidly changing quantum states", "Keys are non-duplicable (no-cloning theorem)"]) + "</p><p><b>Drawbacks</b>, any two: " + mks(["Currently can only be used over relatively short distances", "Very expensive to implement initially: installation, hardware, a dedicated line and specialist hardware", "The technology is not currently readily available", "Photon polarisation might be affected in the travelling medium", "Terrorists and criminals can use it to hide their activities from law enforcement"], "a") + "</p>", None)

review = req("2 marks", "Explain", "Explain how quantum cryptography can detect an eavesdropper.", "Measuring changes the photon.", "<p>" + mks(["Measuring a photon changes its quantum state", "So an eavesdropper causes errors in the key bits, which the two sides find when they compare a sample"]) + "</p>", None) + req("2 marks", "State", "State two reasons why quantum cryptography is not widely used.", "Cost and distance.", "<p>" + mks(["It needs dedicated fibre and specialist hardware, which is expensive", "It only works over relatively short distances"]) + "</p>", None) + req("2 marks", "Describe", "Describe what happens when an eavesdropper is detected during a quantum key exchange.", "What do the two sides do?", "<p>" + mks(["The key is thrown away because it may have been seen", "The receiver requests another key and the exchange is repeated"]) + "</p>", None) + req("2 marks", "Explain", "Explain why quantum cryptography is said to be based on physics and not mathematics.", "What protects the key?", "<p>" + mks(["The security comes from the properties of photons and quantum mechanics", "Not from a maths problem that a fast enough computer might solve"]) + "</p>", None) + req("1 mark", "Identify", "Identify the type of cable that quantum cryptography uses to send photons.", "Light.", "<p>" + mks(["Fibre-optic cable"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on quantum cryptography (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Purpose: unbreakable by physics.", "Uses the laws of quantum mechanics, not mathematical algorithms."),
  ("Eavesdropping detected.", "Photons change when measured."),
  ("Two different benefits.", "Detects eavesdropping, longer keys, no-cloning, protects fibre data."),
  ("Drawbacks need a reason.", "Dedicated fibre, specialist hardware, short range, polarisation altered."),
  ("It exchanges keys.", "The message is sent after the secure key exchange."),
  ("Fibre-optic cables.", "Photons travel along them."),
], [
  ("quantum cryptography", "Encryption that uses the properties of photons to exchange keys securely."),
  ("a photon", "A particle of light, used to carry the key bits."),
  ("no-cloning", "Quantum states cannot be copied."),
  ("polarisation", "The orientation of the light, used to represent a bit."),
], [("State", "Short answer."), ("Outline", "Give each benefit or drawback with a reason."), ("Describe", "Say what it is used for, in several points."), ("Identify", "Name them.")]) + FC

js = AKJS + AK20JS + r'''
function lcg(seed) { let s = seed; return () => ((s = (s * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff); }
(function () {
  const rnd = lcg(7), bits = Array.from({ length: 8 }, () => (rnd() < 0.5 ? 0 : 1)), flips = [0, 0, 1, 0, 0, 1, 0, 0].map(Number);
  const make = (el, eve) => { const recv = bits.map((b, i) => (eve ? b ^ flips[i] : b));
    const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "Sender", "lbl bd") + SV.text(20, 112, "Receiver", "lbl bd"); if (eve) o += SV.text(300, 22, "Eavesdropper measures each photon", "sm");
      bits.forEach((b, i) => { const x = 130 + i * 56, sent = i < k + 1 && k >= 0; o += SV.rect(x, 30, 46, 40, "f1", { rx: 6 }) + SV.text(x + 23, 57, String(b), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" }); if (i < k) { const bad = recv[i] !== b; o += SV.rect(x, 96, 46, 40, bad ? "cell-no" : "cell-ok", { rx: 6 }) + SV.text(x + 23, 123, String(recv[i]), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" }); } });
      if (k >= 8) { const err = recv.filter((r, i) => r !== bits[i]).length; o += SV.text(20, 168, eve ? "Compare: " + err + " bits differ, so an eavesdropper is detected. The key is discarded." : "Compare: all bits match. The key can be used.", "lbl bd " + (eve ? "t2" : "t3"), { style: "font-size:13.5px" }); } return o; };
    Lib.stepper(el, { w: 620, h: 186, label: eve ? "With eavesdropper" : "No eavesdropper", base: { i: 0 }, draw, tween: 100, dwell: 1500, steps: [0, 1, 2, 3, 4, 5, 6, 7, 8].map((i) => ({ cap: i === 0 ? (eve ? "The sender sends eight photons; an eavesdropper tries to measure them on the way." : "The sender sends eight photons down the fibre; the receiver measures each one.") : i === 8 ? (eve ? "Measuring photons disturbs them, so some arrive wrong. The two sides compare bits and find the differences." : "Every bit matches: nobody has disturbed the photons.") : "Photon " + i + " arrives" + (eve && recv[i - 1] !== bits[i - 1] ? " but its state was changed by the eavesdropper: <b>wrong bit</b>." : "."), s: { i } })) }); };
  make($("#stA"), false); make($("#stB"), true);
})();
(function () {
  let eve = false, n = 40; const b = $("#eB");
  const paint = () => { const rnd = lcg(11), sent = [], recv = []; for (let i = 0; i < n; i++) { const s = rnd() < 0.5 ? 0 : 1; sent.push(s); const wrong = eve && rnd() < 0.25; recv.push(wrong ? 1 - s : s); }
    const diff = sent.filter((s, i) => s !== recv[i]).length; $("#eT").innerHTML = '<div class="tw"><table class="t mono"><tr><td>sent</td><td>' + sent.join("") + "</td></tr><tr><td>received</td><td>" + recv.map((r, i) => (r !== sent[i] ? '<b style="color:var(--bad)">' + r + "</b>" : r)).join("") + "</td></tr></table></div>";
    $("#eV").innerHTML = eve ? `With an eavesdropper about a quarter of the bits are disturbed: <b>${diff}</b> of ${n} differ. The sides see the mismatch, <b>detect the eavesdropper</b>, discard the key and request another.` : `<b>${diff}</b> bits differ: nobody has measured the photons, so the key can be used.`; b.querySelectorAll("button").forEach((x) => (x.className = (x.dataset.k === "on") === eve ? "on" : "")); };
  [["off", "No eavesdropper"], ["on", "Eavesdropper listening"]].forEach(([k, t]) => { const x = document.createElement("button"); x.textContent = t; x.dataset.k = k; x.onclick = () => { eve = k === "on"; paint(); }; b.appendChild(x); });
  Lib.slider($("#eS"), { id: "es", label: "Photons sent ", min: 8, max: 80, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("bB", "bO", [
  ["Eavesdropping can be detected", "Benefit", "Measuring a photon changes it, so errors appear"],
  ["Needs dedicated fibre and specialist hardware", "Drawback", "Expensive to buy and maintain"],
  ["Based on the laws of physics", "Benefit", "Not reliant on a mathematical problem"],
  ["Works only over short distances", "Drawback", "A current limit of the technology"],
  ["Polarisation may be altered in the fibre", "Drawback", "Causes errors in the key"],
  ["Keys cannot be copied", "Benefit", "No-cloning theorem"]
], ["Point", "Benefit or drawback", "Reason"]);
''' + CLASSIFY("cl1", "Is it a benefit or a drawback?", ["Benefit", "Drawback"],
  [("Eavesdropping can be detected", 0), ("Needs a dedicated fibre-optic line", 1), ("Virtually unhackable", 0), ("Currently works over short distances only", 1), ("Longer keys can be exchanged", 0), ("Equipment is very expensive", 1), ("Criminals can hide their communications", 1)],
  "Benefits: detection, security, longer keys. Drawbacks: cost, range, hardware.") + CLASSIFY("cl2", "Which type of cryptography?", ["Symmetric", "Asymmetric", "Quantum"],
  [("Uses photons", 2), ("One shared key", 0), ("A public and a private key", 1), ("Detects eavesdropping by the change in a state", 2), ("Has the key distribution problem", 0), ("Can verify the sender with a key pair", 1)],
  "Quantum uses the properties of photons.") + MATCH([
  ["Quantum cryptography", "Uses laws of quantum physics to exchange keys securely"], ["Photon", "A particle of light carrying a bit"], ["Eavesdropping", "Listening to a communication without permission"], ["No-cloning", "A quantum state cannot be copied"], ["Fibre-optic cable", "The medium the photons travel through"]]) + ORDER(
  "Put the steps of a quantum key exchange in order.",
  ["The sender sends photons carrying the key bits", "The receiver measures them", "The two sides compare a sample of the bits", "If the bits match, no eavesdropper is present and the key is used", "The message is encrypted with the key and sent"],
  "Send, measure, compare, accept, encrypt.") + CALC([
  {"q": "A key exchange sends 40 photons. An eavesdropper disturbs about a quarter of them. About how many bits are wrong?", "a": 10, "unit": "", "tol": 0.5, "hint": "40 × 0.25.", "sol": "<b>10</b>."},
  {"q": "In the comparison, 0 of 20 sample bits differ. How many eavesdroppers are suggested?", "a": 0, "unit": "", "tol": 0.01, "hint": "No errors, no eavesdropper.", "sol": "<b>0</b>."},
  {"q": "How many benefits does a Paper 3 question usually ask for, and how many drawbacks? Add the numbers.", "a": 4, "unit": "", "tol": 0.01, "hint": "Two and two.", "sol": "<b>4</b>."},
  {"q": "What kind of cable carries the photons? Enter 1 for copper, 2 for fibre-optic.", "a": 2, "unit": "", "tol": 0.01, "hint": "Light needs fibre.", "sol": "<b>2</b>."},
  {"q": "A key has 256 bits and a quarter are discarded after comparing. How many bits remain?", "a": 192, "unit": "", "tol": 0.5, "hint": "256 × 3/4.", "sol": "<b>192</b>."}]) + MCQ([
  ("Quantum cryptography uses:", ["Prime numbers", "Photons", "Passwords", "Paper keys"], 1, "Photons."),
  ("How is an eavesdropper detected?", ["By a loud noise", "Errors appear because measuring photons changes them", "By a certificate", "They cannot be detected"], 1, "Disturbed states."),
  ("A drawback is:", ["It detects eavesdropping", "It needs a dedicated fibre line and specialist hardware", "It uses physics", "It uses long keys"], 1, "Cost and hardware."),
  ("Quantum cryptography is used mainly for:", ["Exchanging keys securely", "Printing", "Compressing files", "Browsing"], 0, "Secure key exchange."),
  ("Which is a benefit?", ["Short range", "Virtually unhackable", "High cost", "Needs dedicated line"], 1, "Virtually unhackable."),
  ("The no-cloning theorem means:", ["Keys can be copied", "A quantum state cannot be copied", "Photons are free", "Fibre is cheap"], 1, "Cannot be copied.")], "qz1") + CARDS([
  ("Purpose", "Virtually unbreakable key exchange using quantum physics."), ("Detects eavesdropping", "Photon states change when measured."), ("Benefit", "Security from physics; longer keys; no-cloning."), ("Drawback", "Cost, dedicated fibre, short range, polarisation altered."),
  ("Photon", "Particle of light that carries a bit."), ("Fibre-optic", "The cable photons travel in."), ("Key exchange", "Keys first, then the message."), ("Third type", "Not symmetric or asymmetric.")])

build("ac1712", "ac-17-1-2-quantum-cryptography", "Quantum Cryptography", EYA("17.1.2"),
  "The purpose of quantum cryptography, how eavesdropping is detected, and its benefits and drawbacks; animations, an eavesdropper lab and the real Paper 3 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 17 · Security, section 17.1 Encryption, encryption protocols and digital certificates"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
