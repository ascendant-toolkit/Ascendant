"""A Level CS syllabus 15.1.3: virtual machines. Run: python3 tools/artifact-kit/mk_ac1513.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>virtual machine (VM)</b> is a software emulation of a computer system: a standalone environment, with all the components of a real computer, that runs on a physical <b>host</b> computer and behaves like a different machine. The host's <b>operating system</b> controls the real hardware, and a <b>hypervisor</b> (VM software) runs between the host and the <b>guest operating system</b>, creating the virtual machines and sharing the host's RAM, processor time and storage between them. Benefits include running <b>software for a different system</b>, trying software <b>safely</b> (a crash or virus is contained), and <b>saving the cost</b> of extra hardware. Limitations include <b>poorer performance</b> than a real machine, the <b>complexity</b> of setting up and maintaining it, and that some <b>hardware cannot be emulated</b>. The exam asks you to describe a VM, give benefits and limitations, and explain the roles of the host and guest operating systems.</p></div>

  <h2>1 · What a virtual machine is</h2>
  <ul>
    <li>The <b>emulation</b> of a computer system (hardware and/or software) using a <b>host computer</b>.</li>
    <li>It is a <b>standalone environment</b> running on a physical computer; it is not a physical machine, but it contains all the components of one (processor, memory, storage, devices), all simulated.</li>
    <li>A <b>guest operating system</b> runs inside the virtual machine. <b>Several</b> virtual machines, with different guest operating systems, can run on one host.</li>
    <li>The host provides the real resources (RAM, processor, storage) and shares them between the virtual machines.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Layer (from the bottom)</th><th>Role</th></tr>
    <tr><td><b>Physical hardware</b></td><td>The real processor, RAM and storage</td></tr>
    <tr><td><b>Host operating system</b></td><td>The normal operating system of the host computer. It has control of all the resources of the host and can access its physical hardware. It also provides a user interface to operate the VM software and runs the VM software</td></tr>
    <tr><td><b>Hypervisor / VM software</b></td><td>Runs between the host and guest operating systems; creates and runs the virtual machines and allocates host resources to them</td></tr>
    <tr><td><b>Virtual machine</b> (guest OS)</td><td>The <b>guest operating system</b> runs within the virtual machine, under the control of the host. It controls the virtual hardware during the emulation, reaches the real hardware through the VM and the host OS, and gives the emulated system its own user interface</td></tr>
    <tr><td><b>Applications</b></td><td>Programs running inside the guest</td></tr>
  </table></div>

  <h2>2 · Benefits</h2>
  <div class="tw"><table class="t">
    <tr><th>Benefit</th><th>Explanation</th></tr>
    <tr><td><b>Compatibility</b></td><td>Software or <b>legacy applications</b> that do not run on the host can run in a guest operating system that they do work on; <b>different instruction set architectures</b> can be emulated on one computer; software can be tried on different operating systems on the same hardware</td></tr>
    <tr><td><b>Protection</b></td><td>The guest operating system can <b>crash without affecting the host</b> or other VMs, so a new or suspicious program can be tested safely: if it has a virus it only infects the VM. Easier recovery</td></tr>
    <tr><td><b>Cost</b></td><td>No need to buy extra computers or hardware to test or run another system: several VMs run on the same hardware</td></tr>
    <tr><td><b>Flexibility</b></td><td>More than one operating system can <b>coexist on a single computer</b>; a new system can be tried before the hardware is bought</td></tr>
  </table></div>

  <h2>3 · Limitations</h2>
  <div class="tw"><table class="t">
    <tr><th>Limitation</th><th>Explanation</th></tr>
    <tr><td><b>Performance</b></td><td>A VM is <b>less efficient</b> than a real machine: there is extra code to run, it accesses hardware <b>indirectly</b> through the host, and the resources (RAM, processor time) are <b>shared</b>. Many VMs on a weak host slow each other down. Response times cannot be measured accurately on a VM</td></tr>
    <tr><td><b>Complexity / maintenance</b></td><td>Setting up and maintaining a VM is complex and can be expensive: both the host and the VM need to be maintained and updated</td></tr>
    <tr><td><b>Hardware / software issues</b></td><td><b>Some hardware cannot be emulated</b> (especially new hardware), or the host's hardware cannot be accessed directly. A VM depends on the features of the host and can be affected by its weaknesses</td></tr>
  </table></div>

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Saying a VM is "a computer in the cloud" or "a copy of a computer". It is an <b>emulation by software</b> on a host.</li>
    <li>Giving "it is slower" without a reason: extra code, indirect access to hardware, shared resources.</li>
    <li>Giving "it is cheaper" with no explanation. Say no extra hardware has to be bought.</li>
    <li>Mixing up the host and guest operating systems: the <b>host</b> controls the real hardware; the <b>guest</b> runs inside the VM.</li>
    <li>Stating a benefit and a limitation that are the same point twice.</li>
  </ul>
'''

watch = '''
  <h2>1 · The layers of a virtual machine</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · A crash stays inside the VM</h2>
  <div id="stB"></div>
  <h2>3 · The host's resources are shared</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Share a host between virtual machines</h2>
  <p>The host has 16 GB of RAM. Choose how many VMs to run, each allocated 4 GB. When the VMs ask for more than the host has, performance suffers.</p>
  <div class="card"><div id="vS"></div><div id="vT"></div><div class="readout"><div><small>RAM requested</small><strong id="v1"></strong></div><div><small>Host RAM</small><strong id="v2"></strong></div><div><small>Performance</small><strong id="v3"></strong></div></div><div class="verdict" id="vV"></div></div>

  <h2>Lab 2 · Is a virtual machine a good choice?</h2>
  <div class="card"><div id="qB" class="btnrow"></div><div id="qO"></div></div>

  <h2>Lab 3 · Host and guest</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Benefit or limitation?</h2><div id="cl1" class="card"></div>
  <h2>2 · Host or guest?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the layers in order, from the hardware up</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Sharing resources</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Running Windows software on a Mac", "A VM runs Windows as a guest on a Mac. A program that only works on Windows can be used without buying a second computer.", "benefit: runs software not compatible with the host, and saves the cost of extra hardware.") +
rw("Testing a suspicious download", "A security analyst opens a file inside a VM. If it contains malware, it can only infect the VM, which is then deleted. The host is untouched.", "benefit: the guest can crash or be infected without affecting the host.") +
rw("Cloud servers", "A cloud provider runs many customers' virtual servers on the same physical machines. Each customer sees a separate computer.", "several VMs share one host; the hypervisor allocates resources.") +
rw("Running an old game or old program", "Old software that needs an old operating system can run in a VM with that system as the guest, even though the host has a modern one.", "legacy applications run in a compatible guest operating system.") +
rw("A slow virtual desktop", "If ten virtual desktops share a host with too little RAM, each becomes slow, because they share the host's resources and every action goes through the VM software.", "limitation: reduced performance from shared resources and extra code.")
)

where = [
  ("M/J 2022", "31, 33", "6", "6", "Two benefits and one limitation of a virtual machine emulating a new computer system"),
  ("O/N 2022", "32", "5", "6", "Describe a virtual machine with two benefits and two drawbacks"),
  ("M/J 2024", "32", "9", "4 + 3", "Two benefits and two limitations; the roles of the host and guest operating systems"),
  ("M/J 2026", "31", "5", "4", "Two benefits and two limitations of a virtual machine"),
  ("M/J 2026", "32", "5", "4", "Explain what is meant by the term virtual machine")]

past = '''  <p class="note">Virtual machines are tested in Paper 3 in May/June 2022, Oct/Nov 2022, May/June 2024 and May/June 2026, nearly always as a benefits and limitations question. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>What a virtual machine is</h3>
''' + peq(SRC("s26", "32", "Q5"), "4 marks", "Explain",
  "Explain what is meant by the term virtual machine.",
  "A standalone environment, emulating a system, host resources, guest operating system, hypervisor.",
  "<p>Any four: " + mks(["A VM is a standalone environment running on a physical computer: it is not a physical machine", "It can emulate the hardware / software of another system", "VM software has all the components of a physical computer system", "The host machine provides all the physical resources, e.g. RAM", "and is controlled via a host operating system", "The hypervisor runs between the host and guest operating systems", "and creates and runs virtual machines / allocates resources from the host to the guest OS", "A guest OS runs within the VM; multiple guest operating systems can run on the same host"]) + "</p>", "Describing a VM as a physical computer, or as 'a copy of a computer'. It is a software environment.") + peq(SRC("w22", "32", "Q5"), "6 marks", "Describe",
  "Describe what is meant by a virtual machine. Include in your answer two benefits and two drawbacks of using a virtual machine.",
  "A description (2), two benefits (2), two drawbacks (2).",
  "<p>Description (max 2): " + mks(["The emulation of a computer system, hardware and/or software", "using a host computer system", "using guest operating system(s) for the emulation"]) + " Benefits (max 2): " + mks(["Multiple guest operating systems / VMs can be used on the same computer", "Different instruction set architectures can be emulated on a single computer", "A VM can crash without affecting the host", "Security: suspicious software with a virus will only infect the VM", "Cost savings: no extra hardware", "Can run legacy applications that are incompatible with the host"], "a") + " Drawbacks (max 2): " + mks(["Less efficient / poorer performance than real machines because of the extra load on the host computer", "The performance of the guest system cannot be adequately measured", "May be affected by any weaknesses of the host machine", "Costly or complex to maintain / implement / manage", "Cannot emulate some hardware"]) + "</p>", None) + '''
  <h3>Benefits and limitations</h3>
''' + peq(SRC("s22", "31, 33", "Q6"), "6 marks", "Describe",
  "A virtual machine is used to emulate a new computer system. Describe two benefits and one limitation of using a virtual machine for this purpose.",
  "Two marks for each described benefit and two for the limitation: a point and its reason.",
  "<p>Benefits (2 marks each, max 4): " + mks(["The new system can be tried on different virtual hardware, without needing to buy the hardware", "It is easier to recover if the software emulating the new computer causes a crash, as the VM protects other software", "Programs for the new system that are not compatible with the host can be emulated using the guest operating system", "More than one new system can be emulated, so multiple operating systems can coexist on one computer"]) + " Limitation (2 marks, max 2): " + mks(["A VM may not be able to emulate the new hardware, because that hardware may have been developed since the VM was written", "Extra code is executed, and resources such as RAM and processor time are shared, so performance is degraded", "Using a VM increases maintenance overheads, because both the host and the VM must be maintained"], "a") + "</p>", "Naming a benefit without the second mark, which is the reason. Each benefit needs a point and why.") + peq(SRC("s26", "31", "Q5"), "4 marks", "Outline",
  "A virtual machine may be used to emulate computer hardware using software. Outline two benefits and two limitations of using a virtual machine.",
  "Two benefits and two limitations, each in your own words, with a reason.",
  "<p>Benefits (max 2): " + mks(["It can provide an instruction set architecture different from the real computer, or allow multiple operating system environments on one computer; or run legacy software that is not compatible with the host using a compatible guest OS", "Cost saved by not having to buy additional hardware to test or use applications", "The guest OS can crash, or suspicious software can cause a problem, without affecting the host machine"]) + " Limitations (max 2): " + mks(["Degraded performance: a VM is less efficient than a real machine because it accesses hardware indirectly, through the host, and when several VMs run the host may lack the power for all of them", "A VM depends on the features of the host and may be affected by its weaknesses; not all hardware or software can be emulated", "Managing and maintaining a virtual machine can be complex and specialised"], "a") + "</p>", None) + peq(SRC("s24", "32", "Q9"), "4 + 3 marks", "Outline / Explain",
  "(a) Outline two benefits and two limitations of a virtual machine. (b) Explain the roles of the host operating system and the guest operating system as used in a computer system running a virtual machine.",
  "(b) the host: normal OS, controls the real resources, runs the VM software. The guest: runs within the VM.",
  "<p><b>(a)</b> Benefits (max 2): " + mks(["Compatibility: applications not compatible with the host can run in the VM, or old software can be emulated on a new system", "Protection: the guest operating system has no effect outside the VM, so testing will not crash the host", "Cost: no need to buy extra computers; several VMs run on the same hardware"]) + " Limitations (max 2): " + mks(["Performance: the guest will not perform as well as on its own compatible machine because of extra code and more RAM use; it depends on the host's capabilities", "Complexity: building an in-house VM can be expensive, time consuming and complex to maintain", "Some hardware or software cannot be emulated, or some host hardware cannot be accessed directly by the VM"], "a") + "</p><p><b>(b)</b> Host (max 2): " + mks(["The host OS is the normal operating system for the host computer", "It has control of all the resources of the host and can access its physical resources", "It provides a user interface to operate the VM software and runs the VM software"]) + " Guest (max 2): " + mks(["The guest OS runs within the virtual machine", "It controls the virtual hardware / software during the emulation, accessing the actual hardware through the VM and the host OS", "It provides a virtual user interface for the emulated system and runs under the control of the host OS"], "a") + "</p>", "Reversing the roles: the host controls the real hardware, the guest runs inside the virtual machine.")

review = req("2 marks", "Explain", "Explain why a virtual machine is slower than running the same program on a real computer.", "Extra layers and sharing.",
  "<p>" + mks(["Extra code (the VM software and guest OS) has to be run, and the hardware is accessed indirectly through the host.", "The resources, RAM and processor time, are shared with the host and other VMs."]) + "</p>", None) + req("3 marks", "Describe", "A company wants to test new software for a different operating system. Describe how a virtual machine helps.", "Compatibility, protection, cost.",
  "<p>" + mks(["A guest OS that the software works on is installed in a VM, so it can run on the existing computer.", "If the software crashes or has a fault, only the VM is affected, not the host.", "No extra computer has to be bought."]) + "</p>", None) + req("2 marks", "State", "State two resources that the host shares with its virtual machines.", "What a VM needs to run.",
  "<p>" + mks(["RAM / memory", "Processor time (also storage)"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between the host operating system and the guest operating system.", "Which controls the real hardware?",
  "<p>" + mks(["The host OS is the normal OS of the physical computer and controls all its resources.", "The guest OS runs inside the virtual machine, under the control of the host, and controls the virtual hardware."]) + "</p>", None) + req("3 marks", "Explain", "Explain why running ten virtual machines on a small host might not be a good idea.", "Shared RAM and processor time.",
  "<p>" + mks(["Each VM needs RAM and processor time from the host.", "A small host may not have enough for all ten, so they compete.", "Every VM runs slowly, so performance is degraded."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on virtual machines (Paper 3), 2022 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Benefit plus reason.", "'Protection: a crash or virus stays in the VM and cannot affect the host.'"),
  ("Limitation plus reason.", "'Slower: extra code and shared resources.'"),
  ("Know the layers.", "Hardware, host OS, hypervisor, virtual machine with guest OS."),
  ("Host and guest.", "Host controls the real resources; guest runs inside the VM."),
  ("Describe 'emulate'.", "A VM emulates a computer system in software."),
  ("Do not repeat a point.", "Give two different benefits and two different limitations."),
], [
  ("what a virtual machine is", "A software emulation of a computer system that runs on a host computer."),
  ("a benefit of a virtual machine", "Software that is not compatible with the host can run in a guest operating system, and a crash does not affect the host."),
  ("a limitation of a virtual machine", "Performance is poorer, because of the extra code and the shared host resources."),
  ("the role of the host operating system", "It controls the real resources of the host computer and runs the virtual machine software."),
], [("Describe", "Say what it is and how it works."), ("Outline", "Give the main benefits or limitations briefly."), ("Explain", "Give the reason for each."), ("State", "Give the resource or fact.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const layers = [["Physical hardware", "f1", "real processor, RAM, storage"], ["Host operating system", "f2", "controls the real resources; runs the VM software"], ["Hypervisor / VM software", "f3", "creates and runs the VMs; shares host resources"], ["Virtual machine: guest operating system", "f4", "runs inside the VM; emulated hardware"], ["Applications", "f1", "programs in the guest"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    layers.forEach((l, i) => { const y = 200 - i * 44, v = k >= i ? 1 : 0; if (!v) return; o += SV.rect(160, y, 440, 38, k === i ? "cell-warn" : l[1], { rx: 6, ...op(k === i ? 1 : 0.7) }) + SV.text(180, y + 24, l[0], "lbl bd", { style: "font-size:14px" }) + SV.text(620, y + 24, l[2], "sm", { style: "font-size:11px" }); });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 245, label: "The layers of a virtual machine", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "At the bottom is the <b>physical hardware</b>: the real processor, RAM and storage.", s: { i: 0 } },
    { cap: "The <b>host operating system</b> controls all the real resources and runs the virtual machine software.", s: { i: 1 } },
    { cap: "The <b>hypervisor</b> (VM software) runs between the host and guest operating systems, creating the VMs and allocating resources to them.", s: { i: 2 } },
    { cap: "Inside the VM runs the <b>guest operating system</b>, using virtual hardware that the VM software emulates.", s: { i: 3 } },
    { cap: "The guest runs its own applications. Several VMs can run at once, each with its own guest.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.rect(30, 20, 700, 190, "f1", { rx: 10, ...op(0.2) }) + SV.text(50, 44, "Host computer", "lbl bd");
    o += SV.rect(60, 60, 300, 130, k >= 1 ? "cell-no" : "f4", { rx: 8, ...op(0.6) }) + SV.text(80, 86, "Virtual machine A", "lbl bd", { style: "font-size:14px" }) + SV.text(80, 112, k >= 1 ? "guest OS crashes ✗" : "guest OS running", "lbl", { style: "font-size:13px" });
    o += SV.rect(400, 60, 300, 130, "f3", { rx: 8, ...op(0.6) }) + SV.text(420, 86, "Virtual machine B", "lbl bd", { style: "font-size:14px" }) + SV.text(420, 112, "still running normally", "lbl", { style: "font-size:13px" });
    if (k >= 2) o += SV.text(60, 238, "The host and VM B are unaffected. VM A can be restarted or deleted.", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 250, label: "Protection", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Two virtual machines run on one host.", s: { i: 0 } },
    { cap: "The guest operating system in VM A <b>crashes</b> (or a program in it contains a virus).", s: { i: 1 } },
    { cap: "The problem stays <b>inside</b> VM A. The host and the other VM are not affected: this is the protection a VM gives.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Host RAM: 16 GB", "lbl bd");
    o += SV.rect(30, 34, 700, 30, "cell", { rx: 6 });
    const vms = [4, 4, 4, 4]; let x = 30;
    vms.slice(0, Math.min(k + 1, 4)).forEach((g, i) => { o += SV.rect(x, 34, g / 16 * 700, 30, ["f1", "f2", "f3", "f4"][i], { rx: 6 }) + SV.text(x + 10, 54, "VM" + (i + 1) + " 4 GB", "lbl bd", { style: "font-size:12px" }); x += g / 16 * 700; });
    if (k >= 4) o += SV.rect(30 + 700, 34, 140, 30, "cell-no", { rx: 6 }) + SV.text(34 + 700, 54, "VM5 4 GB", "lbl bd", { style: "font-size:12px" });
    o += SV.text(30, 110, k < 4 ? (k + 1) * 4 + " GB requested of 16 GB: fine" : "20 GB requested of 16 GB: the host runs short; every VM slows", "lbl bd" + (k < 4 ? " t3" : " t2"), { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 130, label: "Sharing the host's RAM", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [0, 1, 2, 3, 4].map((i) => ({ cap: i < 4 ? (i + 1) + " VM" + (i ? "s" : "") + " running, each allocated 4 GB." : "A fifth VM is started. The host cannot give all of them what they ask for, so <b>performance drops</b>: the resources are shared.", s: { i } })) });
})();

/* Lab 1 */
(function () {
  let n = 3;
  const paint = () => {
    const req = n * 4; $("#v1").textContent = req + " GB"; $("#v2").textContent = "16 GB"; const perf = req <= 12 ? "good" : req <= 16 ? "ok (host nearly full)" : "poor (not enough RAM)"; $("#v3").textContent = perf;
    $("#vT").innerHTML = '<div class="tw"><table class="t mono"><tr>' + Array.from({ length: n }, (_, i) => `<th>VM${i + 1}</th>`).join("") + "</tr><tr>" + Array.from({ length: n }, () => "<td>4 GB</td>").join("") + "</tr></table></div>";
    $("#vV").textContent = req <= 16 ? "The host can give each VM its RAM. The VMs still run a little slower than real machines because of the extra code and indirect hardware access." : "The VMs ask for " + req + " GB but the host only has 16 GB. The host has to swap data in and out, so every VM slows down: shared resources limit performance.";
  };
  Lib.slider($("#vS"), { id: "vss", label: "Number of virtual machines ", min: 1, max: 6, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();

/* Lab 2 */
(function () {
  const q = [["A developer wants to test a program on three different operating systems using one laptop", "Good choice", "Several guest operating systems run on one host, with no extra hardware to buy."], ["A video game needs the very highest graphics performance", "Poor choice", "A VM accesses the hardware indirectly and shares the host's resources, so performance is lower than on a real machine."], ["An analyst opens a suspicious email attachment", "Good choice", "If it contains a virus it only infects the VM, which can be deleted."], ["A school needs software that only runs on an old operating system", "Good choice", "Run the old OS as a guest: legacy applications can run on a modern host."], ["A hardware engineer needs to test a new graphics card that is not yet supported by the VM software", "Poor choice", "Some hardware cannot be emulated or accessed directly by a VM."]];
  let cur = 0, pick = null;
  const paint = () => {
    $$("#qB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#qO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow"><button class="b${pick === "Good choice" ? " pri" : ""}">Good choice</button><button class="b${pick === "Poor choice" ? " pri" : ""}">Poor choice</button></div><div class="verdict">` + (pick === null ? "Choose an answer." : (pick === Q[1] ? "Correct. " : "Not quite. ") + Q[2]) + "</div>";
    $$("#qO .btnrow button").forEach((b) => (b.onclick = () => { pick = b.textContent; paint(); }));
  };
  $("#qB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#qB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Host operating system", "The normal OS of the physical computer", "Controls all the real resources; runs the VM software; provides the user interface to it", "Windows or macOS on the laptop"],
  ["Hypervisor", "VM software between host and guests", "Creates and runs VMs; allocates host resources to them", "VirtualBox, VMware"],
  ["Guest operating system", "The OS inside the virtual machine", "Controls the virtual hardware during emulation; runs under the host's control", "Linux running in a VM on Windows"],
  ["Virtual machine", "A software emulation of a computer system", "A standalone environment with all the components of a computer, simulated", "A test machine"]
], ["Term", "What it is", "Role", "Example"]);
''' + CLASSIFY("cl1", "Benefit or limitation of a virtual machine?", ["Benefit", "Limitation"],
  [("Software for another system can run in a compatible guest OS", 0), ("Performance is poorer than a real machine", 1), ("A crash or virus stays inside the VM", 0), ("Some hardware cannot be emulated", 1), ("No extra hardware has to be bought", 0), ("Setting up and maintaining it is complex", 1), ("The host's RAM and processor time are shared", 1), ("Several operating systems can coexist on one computer", 0)],
  "Benefits: compatibility, protection, cost. Limitations: performance, complexity, hardware.") + CLASSIFY("cl2", "Is it the host or the guest operating system?", ["Host OS", "Guest OS"],
  [("Controls all the real resources of the computer", 0), ("Runs inside the virtual machine", 1), ("Runs the VM software", 0), ("Controls the virtual hardware during emulation", 1), ("Accesses the physical resources directly", 0), ("Accesses real hardware through the VM and the host OS", 1)],
  "The host runs on the real hardware. The guest runs inside the VM.") + ORDER(
  "Put the layers in order, from the hardware up.",
  ["Physical hardware", "Host operating system", "Hypervisor / virtual machine software", "Guest operating system in the virtual machine", "Applications"],
  "Hardware, host OS, hypervisor, guest OS, applications.") + MATCH([
  ["Virtual machine", "A software emulation of a computer system"], ["Host", "The physical computer and its OS that run the VM"], ["Guest operating system", "The OS that runs inside the virtual machine"], ["Hypervisor", "Software that creates and runs virtual machines"], ["Emulate", "Behave like another system using software"]]) + CALC([
  {"q": "A host has 32 GB of RAM and each VM is allocated 6 GB. What is the largest number of VMs that fit?", "a": 5, "unit": "", "tol": 0.01, "hint": "32 ÷ 6 = 5.33.", "sol": "<b>5</b>."},
  {"q": "Four VMs are each given 8 GB on a host with 24 GB. How many GB more than the host has are requested?", "a": 8, "unit": "GB", "tol": 0.01, "hint": "32 − 24.", "sol": "<b>8</b> GB."},
  {"q": "How many operating systems are running if a Windows host runs two Linux VMs?", "a": 3, "unit": "", "tol": 0.01, "hint": "One host OS and two guests.", "sol": "<b>3</b>."},
  {"q": "One VM crashes out of three running on a host. How many are still running?", "a": 2, "unit": "", "tol": 0.01, "hint": "The others are unaffected.", "sol": "<b>2</b>."}]) + MCQ([
  ("What is a virtual machine?", ["A physical computer", "A software emulation of a computer system", "A type of network", "A kind of memory"], 1, "It emulates a system in software."),
  ("Where does the guest operating system run?", ["On the hardware directly", "Inside the virtual machine", "Only in ROM", "On the keyboard"], 1, "Inside the VM."),
  ("Which is a benefit of a VM?", ["Better performance than a real machine", "A crash does not affect the host", "No software is needed", "It needs no RAM"], 1, "Protection."),
  ("Which is a limitation?", ["It saves money", "It uses extra code and shared resources, so is slower", "It runs legacy software", "It is safe for testing"], 1, "Performance."),
  ("What creates and runs the virtual machines?", ["The hypervisor / VM software", "The keyboard", "The guest OS only", "The printer"], 0, "VM software.")], "qz1") + CARDS([
  ("Virtual machine", "Software emulation of a computer system on a host."), ("Host OS", "Normal OS of the host; controls real resources; runs the VM software."), ("Guest OS", "Runs inside the VM; controls the virtual hardware."), ("Hypervisor", "Creates and runs VMs, allocates host resources."),
  ("Benefits", "Compatibility, protection, cost, several OSs at once."), ("Limitations", "Performance, complexity, hardware cannot be emulated."), ("Legacy", "Old software runs in a compatible guest."), ("Shared", "RAM and processor time are shared with the host.")])

build("ac1513", "ac-15-1-3-virtual-machines", "Virtual Machines", EYA("15.1.3"),
  "What a virtual machine is, the host and guest operating systems and the hypervisor, benefits and limitations with reasons; animations, a resource-sharing lab and the real Paper 3 questions from 2022 to 2026.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.1 Processors, parallel processing and virtual machines"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
