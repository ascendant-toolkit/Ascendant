"""AS CS 4.1.2: CPU performance factors and ports (USB, HDMI, VGA). Run: python3 tools/artifact-kit/mk_as412.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The performance of a computer depends on several factors: <b>clock speed</b> (more fetch-execute cycles per second), <b>number of cores</b> (more instructions in parallel, but with overheads), <b>cache memory</b> (fast memory close to the CPU holding frequently used instructions and data), <b>amount of RAM</b> (more running programs held without using slower secondary storage) and <b>bus width</b> (a wider data bus moves more data at once; a wider address bus addresses more memory). Each exam answer needs the factor <b>and</b> its effect. <b>Ports</b> connect peripherals: <b>USB</b> is a universal serial bus that detects devices automatically and loads a driver, <b>HDMI</b> carries digital video and audio on one cable and <b>VGA</b> carries analogue video only. Multiple cores do not always double the speed.</p></div>

  <h2>1 · Performance factors</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Effect on performance</th></tr>
    <tr><td><b>Clock speed</b></td><td>A higher clock speed means more fetch-execute cycles per second (for example 4 GHz is 4 billion timing signals a second instead of 2.1 billion)</td></tr>
    <tr><td><b>Number of cores</b></td><td>Each core can carry out a process at the same time, so more instructions are performed in parallel</td></tr>
    <tr><td><b>Cache memory</b></td><td>Fast access memory close to the CPU that stores frequently used instructions and data, so they can be accessed faster than from RAM and the CPU waits less</td></tr>
    <tr><td><b>RAM</b></td><td>More RAM means more running programs and data can be held without using virtual memory or fetching from slower secondary storage: less delay</td></tr>
    <tr><td><b>Bus width</b></td><td>A wider <b>data bus</b> transfers more data at the same time; a wider <b>address bus</b> allows more memory locations to be addressed directly</td></tr>
    <tr><td>Secondary storage type</td><td>A solid state drive has faster access than a magnetic hard disk</td></tr>
  </table></div>

  <h2>2 · Why two cores are not twice as fast</h2>
  <ul>
    <li>Multiple cores add <b>overheads</b>: the cores must communicate and share data, which adds latency.</li>
    <li>Not all software is designed to use several cores, so some of the cores sit <b>idle</b>.</li>
    <li>Memory access speed may not keep up with the cores, causing delays.</li>
    <li>Possible deadlock, where one core waits for another that is waiting for the first, and more heat is generated.</li>
    <li>The two computers may differ in other ways too (RAM, GPU).</li>
  </ul>

  <h2>3 · Ports</h2>
  <div class="tw"><table class="t">
    <tr><th>Port</th><th>Transfers</th><th>Key points</th></tr>
    <tr><td><b>USB</b> (Universal Serial Bus)</td><td>Data, one bit at a time (serial); also power</td><td>Universal standard; fast transfer; detects devices automatically; USB 3 is full duplex, earlier versions half duplex; can be synchronous or asynchronous</td></tr>
    <tr><td><b>HDMI</b> (High Definition Multimedia Interface)</td><td>Digital video and audio together</td><td>High bandwidth; one cable; uncompressed digital signals; no loss from converting to analogue and back; less prone to interference; supports high resolutions</td></tr>
    <tr><td><b>VGA</b> (Video Graphics Array)</td><td>Analogue video only</td><td>Needs a separate sound cable; digital signal converted to analogue and back; more prone to interference; lower resolution</td></tr>
  </table></div>
  <p><b>How USB connects automatically:</b> plugging in the device causes a voltage change; the computer detects it; the device sends its code (identification) to the computer; the OS finds that code in its list of devices and loads the correct device driver.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Naming a factor with no effect, such as "more cores". Say that more instructions can be performed at the same time.</li>
    <li>Saying more cores doubles the speed. The question usually asks why it does not always.</li>
    <li>Saying a wider bus makes the bus "faster". It transfers more data at once, or addresses more memory.</li>
    <li>Describing USB as "universal" with no mention of automatic detection and the device driver.</li>
    <li>Saying HDMI is "better quality" with no reason (digital, single cable for audio and video, high bandwidth).</li>
  </ul>
'''

watch = '''
  <h2>1 · More fetch-execute cycles per second</h2>
  <div id="stA"></div>
  <h2>2 · Cache against RAM</h2>
  <div id="stB"></div>
  <h2>3 · A USB device connects automatically</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Cores and the work that can be shared</h2>
  <p>The more of a program that can run in parallel, the more extra cores help.</p>
  <div class="card"><div id="cS1"></div><div id="cS2"></div><div id="cG"></div><div id="cV" class="verdict"></div></div>
  <h2>Lab 2 · Cache hit rate</h2>
  <div class="card"><div id="hS"></div><div id="hV" class="verdict"></div></div>
  <h2>Lab 3 · Which port?</h2>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div></div>
'''

_pr, _prjs = PR(["Which factor?", "Why is the performance not doubled?", "Match the factor to its effect", "Put the USB connection steps in order", "Working out", "Multiple choice"],
  ("Which performance factor does the effect describe?", ["Clock speed", "Cores", "Cache", "RAM", "Bus width"], [("More fetch-execute cycles per second", 0), ("More instructions at the same time", 1), ("Frequently used data held close to the CPU", 2), ("Fewer fetches from secondary storage", 3), ("More data moved each time", 4), ("Fewer waits for data from main memory", 2)], "Match the effect."),
  ("Why might two cores not give twice the speed?", ["A real reason", "Not a reason"], [("The cores must communicate with each other", 0), ("Software may not use both cores", 0), ("The cores always run at half speed", 1), ("Memory may not keep up with the cores", 0), ("Each core has a different clock", 1), ("There is extra overhead sharing the work", 0)], "Overhead, idle cores, memory."),
  [["Clock speed", "Number of fetch-execute cycles per second"], ["Cache", "Fast memory close to the CPU"], ["Data bus width", "How much data is transferred at once"], ["Address bus width", "How many memory locations can be addressed"], ["Cores", "Number of processing units working in parallel"]],
  ("Put the USB automatic connection steps in order.", ["The device is plugged in", "A voltage change occurs", "The computer detects the voltage change", "The device's code is sent to the computer", "The OS finds the code and loads the device driver"], "Plug, voltage, detect, code, driver."),
  [{"q": "A CPU is upgraded from 2.1 GHz to 4.2 GHz. How many times more timing signals per second?", "a": 2, "unit": "times", "tol": 0.01, "hint": "4.2 ÷ 2.1.", "sol": "<b>2</b> times."}, {"q": "A 3 GHz CPU needs 4 clock ticks for one fetch-execute cycle. How many cycles per second, in millions?", "a": 750, "unit": "million", "tol": 0.5, "hint": "3000 ÷ 4.", "sol": "<b>750</b> million."}, {"q": "A monitor is 2560 × 1600 pixels. How many pixels in millions (1 d.p.)?", "a": 4.1, "unit": "million", "tol": 0.05, "hint": "2560 × 1600 = 4 096 000.", "sol": "<b>4.1</b> million."}, {"q": "A data bus is 64 bits wide. How many bytes can be transferred at once?", "a": 8, "unit": "bytes", "tol": 0.01, "hint": "64 ÷ 8.", "sol": "<b>8</b> bytes."}, {"q": "A cache hit takes 2 ns and a miss 100 ns. With a 90% hit rate, what is the average access time in ns (1 d.p.)?", "a": 11.8, "unit": "ns", "tol": 0.05, "hint": "0.9 × 2 + 0.1 × 100.", "sol": "<b>11.8</b> ns."}],
  [("A wider data bus:", ["Transfers more data at the same time", "Addresses more memory", "Raises the clock speed", "Adds cores"], 0, "More data at once."), ("Cache stores:", ["Frequently used instructions and data", "The OS", "The BIOS", "Backups"], 0, "Frequently used."), ("HDMI differs from VGA because it:", ["Carries digital video and audio together", "Is analogue only", "Needs a separate sound cable", "Is slower"], 0, "Digital, audio and video."), ("More RAM reduces:", ["Use of slower secondary storage", "The clock speed", "The number of buses", "The ALU size"], 0, "Fewer fetches from disk."), ("USB loads a:", ["Device driver", "Compiler", "Utility", "Firewall"], 0, "Driver."), ("Doubling cores does not double speed because:", ["Of overheads and software limits", "The clock halves", "The bus is shorter", "Cache is bigger"], 0, "Overheads.")],
  [("Clock speed", "Fetch-execute cycles per second."), ("Cores", "Instructions in parallel; overheads."), ("Cache", "Fast memory for frequently used data."), ("RAM", "More running programs, less disk use."), ("Data bus", "Wider: more data at once."), ("Address bus", "Wider: more locations."), ("USB", "Serial; auto-detected; driver."), ("HDMI", "Digital video and audio, one cable.")])

real = RWNOTE + (
rw("Buying a gaming PC", "More cores help if the game is written to use them; a faster clock helps almost every program; more RAM stops the game loading data from the drive.", "match the factor to the work.") +
rw("A video call that stutters", "If the processor is waiting for data from slow memory or storage, a bigger cache or more RAM reduces the delay.", "less waiting for data.") +
rw("Plugging in a memory stick", "It appears on screen within seconds with no software to install: the OS recognises the device and loads its driver.", "automatic detection.") +
rw("A laptop to a TV", "One HDMI cable carries both picture and sound at high resolution. An old VGA lead would need a separate audio cable.", "HDMI carries audio and video.") +
rw("Why a 32-bit computer stops at 4 GB", "Its address bus can only address 2^32 locations. A wider address bus is needed for more memory.", "address bus width.")
)

where = [
  ("M/J 2022", "11", "6(b)", "2", "One factor affecting performance and its impact"),
  ("O/N 2022", "13", "4(c)", "2", "A hardware upgrade and why it improves performance"),
  ("M/J 2023", "12", "5(b), (c)", "4 + 1 + 1", "Two hardware upgrades; how data is transmitted through USB; another port for a monitor"),
  ("O/N 2023", "11", "5(c)", "1 + 5", "Increasing the clock speed; why two cores are not twice as fast"),
  ("O/N 2023", "13", "7(d)", "3", "A port for a VR headset with justification"),
  ("O/N 2024", "11", "3(b)", "2 + 3", "A feature affecting performance; a port that gives an automatic connection and how"),
  ("O/N 2024", "12", "3(b)", "4", "The benefits of HDMI instead of VGA"),
  ("M/J 2025", "11", "6(a)(ii), (iii)", "3 + 2", "How RAM and bus width affect performance"),
  ("M/J 2025", "13", "2(b), (c)", "2 + 2", "The benefit of cache memory; how HDMI provides a connection"),
  ("O/N 2025", "11", "6(b)", "2", "Drawbacks of increasing the number of cores")]

past = '''  <p class="note">Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The "factor and effect" question is asked most series with a different factor each time.</p>
''' + peq(SRC("s22", "11", "Q6(b)"), "2 marks", "Identify / State",
  "Identify one factor that can affect the performance of the computer system and state how it impacts the performance.", "Factor plus effect: clock speed, cores, bus width, cache.",
  "<p>One mark for the factor and one for the impact: " + mks(["Clock speed: a higher clock speed means more fetch-execute cycles per second", "Number of cores: more instructions can be carried out simultaneously", "Bus width: allows the transfer of more data each time, or more memory locations to be directly accessed", "Cache: a higher capacity can store more frequently used instructions for fast access"]) + "</p>", "Naming only the factor. The impact is the second mark.") + peq(SRC("w22", "13", "Q4(c)"), "2 marks", "Identify / Explain",
  "Upgrading secondary storage to solid state typically improves the performance of computer systems. Identify one other upgrade to the hardware and explain why it improves the performance of a computer system.", "RAM, cache, clock speed or cores, with the reason.",
  "<p>One mark for the upgrade and one for the explanation: " + mks(["Increase the quantity of RAM, allowing more applications to reside in memory at the same time and saving disk access times", "Increase the size of cache memory, so that the CPU can continue working without waiting for data", "Increase clock speed, so that more instructions are performed in a time period", "Increase the number of processors or cores, so that more instructions are performed in parallel"]) + "</p>", None) + peq(SRC("s23", "12", "Q5(b)(c)"), "4 + 1 + 1 marks", "Describe / Identify",
  "A student has purchased a new laptop. (b) Describe two ways the hardware can be upgraded to improve performance and explain how each does so. (c)(i) A printer is connected to a USB port. Describe how data is transmitted through a USB port. (ii) Identify one other type of port that can be used to connect the monitor.", "Cores, RAM, cache, clock speed. One bit at a time. HDMI or DisplayPort.",
  "<p><b>(b)</b> One mark for each description and one for the explanation (max 4): " + mks(["Increase the number of cores: each core can carry out a process at the same time, so more instructions are performed in parallel", "Increase RAM capacity: allows more applications to reside in memory at the same time, saving disk access times", "Increase cache memory: more data stored in fast access memory so less time is spent accessing RAM", "Increase clock speed: more fetch-decode-execute cycles each second"]) + "</p><p><b>(c)(i)</b> " + mks(["One bit is transferred at a time; it can be synchronous or asynchronous; USB 3 is full duplex and earlier versions half duplex"], "a") + " (any one) <b>(ii)</b> " + mks(["HDMI or DisplayPort"], "a") + "</p>", None) + peq(SRC("w23", "11", "Q5(c)"), "1 + 5 marks", "Describe / Explain",
  "A computer has a single 2.1 GHz CPU. (i) Describe how increasing the clock speed to 4 GHz can increase the performance. (ii) A second computer has a CPU with two 2.1 GHz cores. Explain why it does not always run twice as fast as the computer with one 2.1 GHz CPU.", "Almost twice as many cycles. Overheads, idle cores, memory, other differences.",
  "<p><b>(i)</b> " + mks(["The CPU can now perform nearly twice as many fetch-execute cycles per second: 4 billion instead of 2.1 billion"]) + "</p><p><b>(ii)</b> Any five: " + mks(["Multiple cores introduce additional overheads", "because of the need for communication between cores", "Software may not be designed for multiple cores", "so one of the cores will be left idle", "Memory access speed may not match the speed of the cores", "so causing delay", "The computers may have more differences than just the cores", "for example more RAM, or a GPU"], "a") + "</p>", "Writing that two cores 'double the speed' or that the cores are 'slower'. Give overheads, idle cores or memory delays.") + peq(SRC("w23", "13", "Q7(d)"), "3 marks", "Identify / Justify",
  "A virtual reality headset is connected to a laptop. Identify one port that could be used to connect the headset to the laptop. Justify your choice.", "USB: fast, universal. HDMI: audio and video, one cable.",
  "<p>One mark for the port and two for the matching justification: " + mks(["USB: has fast data transfer speeds", "USB: is a universal or popular standard cable"]) + " or " + mks(["HDMI: allows video and audio to be transferred on the same cable", "HDMI: convenient as there is no need for two cables"], "a") + "</p>", None) + peq(SRC("w24", "11", "Q3(b)"), "2 + 3 marks", "Identify / Explain",
  "(i) Identify one other feature of a processor (not the number of cores) that can affect performance and state why. (ii) A solid state drive is automatically recognised when it is plugged into a port. Identify an appropriate type of port and explain how this port provides an automatic connection.", "Clock speed or bus width, with the reason. USB: voltage change, code, driver.",
  "<p><b>(i)</b> " + mks(["Clock speed: more fetch-execute cycles are executed per second", "Bus width: more data is transferred at the same time"]) + "</p><p><b>(ii)</b> One mark for USB and two for the explanation: " + mks(["A voltage change occurs when the drive is plugged in and the computer detects it", "The code of the device is transferred to the computer, the OS finds it in the list of devices and loads the appropriate device driver"], "a") + "</p>", None) + peq(SRC("w24", "12", "Q3(b)"), "4 marks", "Explain",
  "A monitor has a screen resolution of 2560 × 1600 pixels and built-in speakers. The computer has a VGA port and an HDMI port. Explain the benefits of connecting the monitor using the HDMI port instead of the VGA port.", "Faster, supports the resolution, audio and video on one cable, digital, less interference.",
  "<p>Any four: " + mks(["HDMI has faster transfer rates than VGA", "needed due to the high resolution (large number of pixels) of the monitor", "HDMI supports video and audio transfer to the built-in speakers", "so no separate sound cable is needed unlike VGA", "HDMI is a digital interface so no data is lost in conversion to analogue and back", "HDMI is less prone to error, crosstalk or interference"]) + "</p>", None) + peq(SRC("s25", "11", "Q6(a)(ii)(iii)"), "3 + 2 marks", "Explain",
  "Computer 1 has a quad-core 2.2 GHz processor, 16-bit architecture and 1 GB RAM; Computer 2 has a dual-core 3.8 GHz processor, 32-bit architecture and 2 GB RAM. (ii) Explain how different amounts of RAM affect the performance of a computer. (iii) Explain how different bus widths affect the performance.", "More RAM: no virtual memory, less fetching from secondary storage. Wider bus: more data or more addresses.",
  "<p><b>(ii)</b> Any three: " + mks(["More RAM means more currently running data and instructions can be stored", "without needing to use virtual memory", "without having to fetch the data from secondary storage first", "which has a slower access time", "Less latency waiting for instructions or data"]) + "</p><p><b>(iii)</b> Any two: " + mks(["A wider data bus means more data can be transferred between components at a time", "so there is less delay when fetching data for a running process", "A wider address bus means larger memory addresses can be used", "allowing more memory locations to be accessed directly"], "a") + "</p>", None) + peq(SRC("s25", "13", "Q2(b)(c)"), "2 + 2 marks", "Describe / Explain",
  "(b) Describe one benefit of the computer using cache memory. (c) Explain how HDMI provides connection to peripheral devices.", "Fast memory near the CPU; HDMI audio and video, high bandwidth, digital.",
  "<p><b>(b)</b> " + mks(["Using cache memory improves performance because it is fast access memory close to the CPU", "which stores frequently used instructions or data so they can be accessed faster than from RAM"]) + "</p><p><b>(c)</b> Any two: " + mks(["HDMI transfers both audio and video using a single cable", "HDMI has a high bandwidth", "Data is transmitted as a stream of uncompressed digital signals", "HDMI uses Transition-Minimized Differential Signalling (TMDS)"], "a") + "</p>", None) + peq(SRC("w25", "11", "Q6(b)"), "2 marks", "Describe",
  "Increasing the number of cores in a processor can affect the performance of a computer. Describe the drawbacks of increasing the number of cores.", "Latency, deadlock, software, heat.",
  "<p>Any two: " + mks(["Latency may be increased because the cores must communicate with one another", "There is a potential for dead-lock situations where one core waits for information from other cores that are waiting for the first", "Not all software is designed to use multiple cores, so some of the additional cores would be idle", "Increased heat generation which could cause damage to other components"]) + "</p>", None)

review = req("2 marks", "Explain", "Explain why a larger cache can make a computer run programs faster.", "Frequently used data.", "<p>" + mks(["Cache stores frequently used instructions and data close to the CPU", "so the CPU waits less for data from slower RAM"]) + "</p>", None) + req("3 marks", "Explain", "A user adds more RAM to an old laptop. Explain how this improves its performance when many programs are open.", "Virtual memory, disk.", "<p>" + mks(["More programs and data are held in RAM", "so virtual memory on the drive is used less", "and less time is spent fetching from slower secondary storage"]) + "</p>", None) + req("2 marks", "Identify", "Identify two differences between HDMI and VGA.", "Digital against analogue; audio.", "<p>" + mks(["HDMI is digital; VGA is analogue", "HDMI carries audio and video on one cable; VGA carries video only"]) + "</p>", None) + req("3 marks", "Describe", "Describe how a computer recognises a USB device.", "Voltage change; code; driver.", "<p>" + mks(["A voltage change is detected when the device is plugged in", "The device sends its code to the computer", "The OS finds the code in its list and loads the device driver"]) + "</p>", None) + req("2 marks", "Explain", "A 64-bit CPU has a wider data bus than a 32-bit CPU. Explain the effect on performance.", "More data at once.", "<p>" + mks(["More data can be transferred at the same time", "so there is less delay fetching data for running programs"]) + "</p>", None)

tips = tips_html([
  ("Factor plus effect.", "Two marks, one for each."),
  ("Cache: frequently used, close to the CPU.", "The CPU waits less."),
  ("Cores: parallel, with overheads.", "Idle cores, communication, software."),
  ("Data bus width: more data at once.", "Address bus width: more locations."),
  ("USB: voltage, code, driver.", "Say 'device driver'."),
  ("HDMI: digital, audio and video.", "One cable, high bandwidth."),
], [("clock speed", "Number of timing signals each second."), ("a core", "A processing unit within the CPU."), ("cache", "Fast memory that holds frequently used data."), ("a device driver", "Software that lets the OS control a device.")],
  [("Identify", "Name the point."), ("Explain", "Reasons as well."), ("Describe", "Several points."), ("Justify", "Give a reason for your choice.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const hz = [2.1, 4.2][k]; let o = SV.rect(20, 40, 160, 50, "cell", { rx: 8 }) + SV.text(100, 70, hz + " GHz", "lbl bd", { "text-anchor": "middle" });
    for (let i = 0; i < 20; i++) o += SV.rect(220 + i * 15, 54, 4, 22, i < (k ? 20 : 10) ? "f1" : "cell", { rx: 1 }); o += SV.text(220, 110, (k ? "about 4 billion" : "about 2 billion") + " timing signals a second", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 130, label: "Clock speed", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "At 2.1 GHz the CPU runs about 2.1 billion fetch-execute steps a second.", s: { i: 0 } }, { cap: "At 4.2 GHz it runs nearly <b>twice as many</b> cycles per second.", s: { i: 1 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 100, 46, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 50, 68, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "CPU", true) + B(190, "Cache", k >= 1) + B(360, "RAM", k >= 2) + SV.path("M120,63 H190", "ax") + SV.path("M290,63 H360", "ax");
    o += SV.text(240, 130, ["", "cache: very fast, holds frequently used data", "slower RAM: used if the cache misses", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 150, label: "Cache", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [{ cap: "The CPU needs data.", s: { i: 0 } }, { cap: "It looks in the <b>cache</b> first: fast, close to the CPU.", s: { i: 1 } }, { cap: "If it is not there, it must be fetched from <b>RAM</b>, which takes longer.", s: { i: 2 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 46, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 68, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, "USB device", k >= 0) + B(220, "Computer / OS", k >= 2) + SV.path("M130,63 H220", "ax", { style: k >= 1 ? "stroke:var(--accent);stroke-width:3" : "" }); o += SV.text(240, 130, ["plug in", "voltage change", "computer detects the voltage change", "the device's code is sent to the OS", "the OS finds the code in its list and loads the device driver"][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 150, label: "USB", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The device is plugged in.", s: { i: 0 } }, { cap: "A <b>voltage change</b> occurs.", s: { i: 1 } }, { cap: "The computer <b>detects</b> the change.", s: { i: 2 } }, { cap: "The device's <b>code</b> is transferred to the computer.", s: { i: 3 } }, { cap: "The OS finds the code in its list of devices and loads the <b>device driver</b>.", s: { i: 4 } }] });
})();

(function () {
  let cores = 4, par = 70; const paint = () => { const f = par / 100; const sp = 1 / ((1 - f) + f / cores);
    let h = ""; for (let c = 1; c <= 16; c++) { const s = 1 / ((1 - f) + f / c); h += `<rect x="${30 + c * 22}" y="${130 - s * 7}" width="16" height="${s * 7}" fill="${c === cores ? "var(--accent)" : "var(--muted)"}" opacity="${c === cores ? 1 : 0.35}"/>`; }
    $("#cG").innerHTML = `<svg viewBox="0 0 420 150" style="width:420px;max-width:100%;display:block"><path d="M30,10 V130 H400" class="ax"/>${h}<text x="400" y="146" class="sm" text-anchor="end" style="font-size:11px">number of cores (1 to 16)</text><text x="34" y="14" class="sm" style="font-size:11px">speed-up</text></svg>`;
    $("#cV").innerHTML = `With <b>${cores}</b> cores and <b>${par}%</b> of the program able to run in parallel, the program runs about <b>${sp.toFixed(1)}</b> times faster, not ${cores} times. The part that cannot be shared (${100 - par}%) and the overheads limit the gain.`; };
  Lib.slider($("#cS1"), { id: "c1", label: "Cores ", min: 1, max: 16, value: cores, fmt: (x) => x, onInput: (v) => { cores = v; paint(); } });
  Lib.slider($("#cS2"), { id: "c2", label: "% of the program that can run in parallel ", min: 0, max: 100, value: par, fmt: (x) => x + "%", onInput: (v) => { par = v; paint(); } }); paint();
})();
(function () {
  let h = 90; const paint = () => { const avg = (h / 100) * 2 + (1 - h / 100) * 100; $("#hV").innerHTML = `A cache hit takes <b>2 ns</b> and a miss (fetch from RAM) takes <b>100 ns</b>. With a <b>${h}%</b> hit rate the average access time is <b>${avg.toFixed(1)} ns</b>. A larger cache holds more frequently used data, so the hit rate rises and the CPU waits less.`; };
  Lib.slider($("#hS"), { id: "h1", label: "Cache hit rate ", min: 0, max: 100, value: h, fmt: (x) => x + "%", onInput: (v) => { h = v; paint(); } }); paint();
})();
btnTable("pB", "pO", [
  ["Fast data to a storage drive, auto-detected", "USB", "Voltage change, code, driver"],
  ["Laptop to a modern monitor with built-in speakers, one cable", "HDMI", "Digital audio and video together"],
  ["Older projector that needs a separate sound cable", "VGA", "Analogue video only"],
  ["A VR headset needing fast data and video", "USB or HDMI", "Fast transfer; audio and video on one cable"],
  ["Needs no conversion from digital to analogue", "HDMI", "Fully digital"]
], ["Need", "Port", "Why"]);
''' + _prjs

finish("as-4-1-2-performance-ports", "as412", "CPU Performance and Ports",
  "Clock speed, cores, cache, RAM and bus width and their effect on performance, why more cores do not always double the speed, and the USB, HDMI and VGA ports, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "4.1.2", "4 · Processor fundamentals", "section 4.1 Central Processing Unit architecture", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on performance factors and ports (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
