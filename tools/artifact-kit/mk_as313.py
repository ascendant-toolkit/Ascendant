"""AS CS 3.1.3: RAM, ROM, SRAM, DRAM, PROM, EPROM, EEPROM. Run: python3 tools/artifact-kit/mk_as313.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>RAM</b> is volatile primary memory that holds the programs, data and part of the operating system currently in use; <b>ROM</b> is non-volatile primary memory that holds the start-up (boot) instructions or BIOS. RAM comes in two forms: <b>SRAM</b> (static: flip-flops, no refresh needed, faster, more expensive, lower density, used for cache) and <b>DRAM</b> (dynamic: one transistor and a capacitor per bit, must be refreshed constantly, slower, cheaper, higher density, used for main memory). ROM comes in three programmable forms: <b>PROM</b> (written once), <b>EPROM</b> (erased with ultraviolet light, after removing the chip, all at once) and <b>EEPROM</b> (erased electrically, in place, byte by byte). The exam asks for definitions, differences and justifications of which type suits a device.</p></div>

  <h2>1 · RAM and ROM</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>RAM</th><th>ROM</th></tr>
    <tr><td>Full name</td><td>Random Access Memory</td><td>Read Only Memory</td></tr>
    <tr><td>Volatile?</td><td>Yes: contents lost when power is off</td><td>No: contents kept without power</td></tr>
    <tr><td>Read/write</td><td>Read and write</td><td>Normally read only</td></tr>
    <tr><td>Holds</td><td>Currently running software, data, part of the OS</td><td>Start-up (boot-up) instructions, BIOS, firmware</td></tr>
  </table></div>

  <h2>2 · SRAM and DRAM</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>SRAM (static)</th><th>DRAM (dynamic)</th></tr>
    <tr><td>Cell</td><td>Transistors arranged as <b>flip-flops (latches)</b></td><td>One <b>transistor and a capacitor</b></td></tr>
    <tr><td>Refreshing</td><td>Not needed</td><td>Capacitor charge leaks, so it must be <b>refreshed constantly</b></td></tr>
    <tr><td>Access time</td><td>Faster</td><td>Slower</td></tr>
    <tr><td>Cost per bit</td><td>Higher</td><td>Lower</td></tr>
    <tr><td>Capacity per chip (bit density)</td><td>Lower</td><td>Higher</td></tr>
    <tr><td>Typical use</td><td>Cache memory</td><td>Main memory, buffers (such as a printer's 1 GB)</td></tr>
  </table></div>

  <h2>3 · PROM, EPROM and EEPROM</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>PROM</th><th>EPROM</th><th>EEPROM</th></tr>
    <tr><td>Programmed</td><td>Once only, after manufacture</td><td>Can be rewritten many times</td><td>Can be rewritten many times</td></tr>
    <tr><td>Erased by</td><td>Cannot be erased</td><td><b>Ultraviolet light</b></td><td><b>Electrical signal (voltage)</b></td></tr>
    <tr><td>Where</td><td>Not applicable</td><td>Must be <b>removed from the circuit board</b></td><td>Erased <b>in situ</b>, still in the device</td></tr>
    <tr><td>What is erased</td><td>Not applicable</td><td>The <b>whole chip</b></td><td>Can erase <b>parts</b> (a byte)</td></tr>
  </table></div>
  <p>EEPROM suits firmware that may need updating, for example in a VR headset: it can be changed many times, without removing the chip and without technical expertise, so the headset can take advantage of new features.</p>

  <h2>4 · Choosing a memory</h2>
  <ul>
    <li>Needs speed (cache): SRAM. Needs lots of memory cheaply (main memory, buffer): DRAM.</li>
    <li>Fixed instructions that never change: ROM or PROM. Firmware that may be updated: EEPROM.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying DRAM is "faster" or "more expensive". It is slower and cheaper.</li>
    <li>Saying SRAM needs refreshing. It does not, which is why it is faster.</li>
    <li>Saying EEPROM is "electronic" and EPROM is not. Both are electronic: the difference is how they are erased.</li>
    <li>Giving only the difference without a contrast: say what each type does.</li>
  </ul>
'''

watch = '''
  <h2>1 · Reading a DRAM cell and refreshing it</h2>
  <div id="stA"></div>
  <h2>2 · Erasing EPROM and EEPROM</h2>
  <div id="stB"></div>
  <h2>3 · What happens at start-up</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · DRAM refresh</h2>
  <p>A DRAM capacitor leaks. Change the refresh interval to see when the stored 1 is lost.</p>
  <div class="card"><div id="rS1"></div><div id="rG"></div><div id="rV" class="verdict"></div></div>
  <h2>Lab 2 · SRAM or DRAM?</h2>
  <div class="card"><div id="sB" class="btnrow"></div><div id="sO"></div></div>
  <h2>Lab 3 · Which ROM?</h2>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>
'''

_pr, _prjs = PR(["SRAM or DRAM?", "PROM, EPROM or EEPROM?", "Match the term to its meaning", "Put the DRAM refresh steps in order", "Working out", "Multiple choice"],
  ("SRAM or DRAM?", ["SRAM", "DRAM"], [("Flip-flops", 0), ("Transistor and capacitor", 1), ("No refresh needed", 0), ("Higher bit density per chip", 1), ("Used for cache", 0), ("Cheaper per bit", 1)], "SRAM: fast and costly. DRAM: cheap and dense."),
  ("Which statement describes EPROM and which EEPROM?", ["EPROM", "EEPROM"], [("Erased with ultraviolet light", 0), ("Erased electrically in situ", 1), ("Must be removed from the circuit board", 0), ("Can erase just a byte", 1), ("Whole chip is erased", 0), ("Firmware in a VR headset", 1)], "UV and removal against electrical and in place."),
  [["Volatile", "Contents are lost when power is switched off"], ["Refresh", "Rewriting a DRAM capacitor's charge"], ["Flip-flop", "SRAM cell"], ["BIOS", "Start-up instructions in ROM"], ["PROM", "Can be programmed only once"]],
  ("Put the DRAM refresh steps in order.", ["A capacitor is charged to store a 1", "The charge slowly leaks away", "A refresh circuit reads the value before the charge is lost", "The value is rewritten to the capacitor", "The cycle repeats constantly"], "Charge, leak, read, rewrite, repeat."),
  [{"q": "A DRAM cell has 1 transistor and 1 capacitor. How many transistors are in 8 cells (one byte)?", "a": 8, "unit": "", "tol": 0.01, "hint": "1 per cell.", "sol": "<b>8</b>."}, {"q": "A DRAM chip must be refreshed every 64 ms. How many refreshes per second?", "a": 15.625, "unit": "", "tol": 0.01, "hint": "1000 ÷ 64.", "sol": "<b>15.625</b>."}, {"q": "A 1 GB DRAM buffer holds 1024 MB. How many 8 MB print jobs fit?", "a": 128, "unit": "", "tol": 0.01, "hint": "1024 ÷ 8.", "sol": "<b>128</b>."}, {"q": "A ROM holds 4 KiB. How many bytes?", "a": 4096, "unit": "bytes", "tol": 0.5, "hint": "4 × 1024.", "sol": "<b>4096</b>."}, {"q": "A PROM can be programmed 1 time and an EEPROM thousands of times. How many times more flexible is 1000 programmes than 1?", "a": 1000, "unit": "times", "tol": 0.5, "hint": "1000 ÷ 1.", "sol": "<b>1000</b>."}],
  [("Which memory is volatile?", ["RAM", "ROM", "PROM", "EPROM"], 0, "RAM."), ("Which uses a capacitor?", ["DRAM", "SRAM", "ROM", "PROM"], 0, "DRAM."), ("Which needs UV light to erase?", ["EPROM", "EEPROM", "DRAM", "SRAM"], 0, "EPROM."), ("Which is used for cache?", ["SRAM", "DRAM", "PROM", "EPROM"], 0, "SRAM."), ("Which can be erased in situ?", ["EEPROM", "EPROM", "PROM", "ROM"], 0, "EEPROM."), ("DRAM compared with SRAM:", ["Cheaper and denser", "Faster", "No refresh", "Flip-flops"], 0, "Cheaper, denser.")],
  [("RAM", "Volatile; running programs and data."), ("ROM", "Non-volatile; boot instructions."), ("SRAM", "Flip-flops; fast; no refresh; cache."), ("DRAM", "Transistor and capacitor; refresh; cheaper."), ("PROM", "Programmed once."), ("EPROM", "UV erase; removed; whole chip."), ("EEPROM", "Electrical; in situ; partial."), ("Volatile", "Lost when power is off.")])

real = RWNOTE + (
rw("Your CPU's cache", "The small, very fast memory next to the processor is SRAM. It is too expensive for gigabytes, so main memory is cheaper DRAM.", "SRAM for speed, DRAM for size.") +
rw("A phone's updates", "The device firmware is stored in a rewritable memory so the maker can update it without opening the case: the same idea as EEPROM.", "in-place updates.") +
rw("A new PC starting up", "Before the operating system loads, a small program in ROM tests the hardware and finds the OS on the storage.", "boot instructions in ROM.") +
rw("A printer's buffer", "Many printers have 1 GB of DRAM to hold print jobs: it is cheap and dense, and extra speed is not needed.", "DRAM is cheaper and denser.") +
rw("Old game cartridges", "Games stored in ROM could not be changed; once the data was set, it could only be read.", "read only.")
)

where = [
  ("M/J 2022", "11", "2(a)(i)", "5", "Complete a description of RAM, ROM, SRAM and DRAM"),
  ("M/J 2022", "11", "2(a)(ii)", "4", "Explain the difference between PROM, EPROM and EEPROM"),
  ("M/J 2023", "11", "4(a)(ii)", "2", "Two advantages of DRAM instead of SRAM"),
  ("O/N 2023", "13", "7(a), (b)", "2 + 2", "Why SRAM is used in a laptop; two reasons for EEPROM in a VR headset"),
  ("O/N 2023", "11", "7(c)", "2", "Two advantages of DRAM instead of SRAM in a 3D printer"),
  ("O/N 2024", "12", "2(b), (c)", "1 + 2", "A benefit of DRAM instead of SRAM; two differences between EPROM and EEPROM"),
  ("O/N 2024", "13", "2(a)", "2", "Two differences between DRAM and SRAM")]

past = '''  <p class="note">Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The comparison of DRAM and SRAM and of EPROM and EEPROM appears almost every series, so learn the two tables in the Learn tab word for word.</p>
''' + peq(SRC("s22", "11", "Q2(a)(ii)"), "4 marks", "Explain",
  "Explain the difference between Programmable ROM (PROM), Erasable Programmable ROM (EPROM) and Electrically Erasable Programmable ROM (EEPROM).", "Once, UV and removal, electrical and in place, whole or partial.",
  "<p>Any three, 1 mark each (max 3): " + mks(["PROM can be set once; EPROM and EEPROM can be overwritten multiple times", "EPROM needs to be removed from the device; EEPROM can be erased in situ", "EPROM is erased using UV light; EEPROM is erased using voltage", "EPROM must be entirely erased before rewriting; EEPROM does not have to be entirely erased"]) + "</p>", "Only describing what each name stands for. The question asks for the difference between them.") + peq(SRC("w23", "13", "Q7(a)(b)"), "2 + 2 marks", "Explain / Identify",
  "(a) Explain why Static RAM is used in the laptop instead of Dynamic RAM. (b) Identify two reasons for using EEPROM in a virtual reality headset.", "SRAM faster as no refresh. EEPROM rewritable without erasing everything.",
  "<p><b>(a)</b> Any two: " + mks(["Static RAM has a faster access time", "because it does not need to be refreshed", "used for the CPU's cache for improvement of cache speed"]) + "</p><p><b>(b)</b> Any two: " + mks(["EEPROM allows frequent read/write/erase operations", "which means the firmware in the headset can be changed easily", "without fully erasing the contents of the firmware first"], "a") + "</p>", None) + peq(SRC("s23", "11", "Q4(a)(ii)"), "2 marks", "Identify",
  "The central computer has Dynamic RAM (DRAM). Identify two advantages of using DRAM instead of Static RAM (SRAM).", "Cost and density.",
  "<p>" + mks(["DRAM has a lower cost per unit (cheaper)", "DRAM has a higher bit density, so more data can be stored per chip"]) + "</p>", None) + peq(SRC("w23", "11", "Q7(c)"), "2 marks", "State",
  "A 3D printer contains 1 GB of Dynamic RAM (DRAM) to store print data. State two advantages of the printer having DRAM instead of Static RAM (SRAM).", "Cost, speed not needed, density.",
  "<p>Any two: " + mks(["DRAM has a lower cost per unit", "A fast access speed is not needed", "Higher bit density, so more data can be stored per chip"]) + "</p>", None) + peq(SRC("w24", "12", "Q2(b)(c)"), "1 + 2 marks", "Identify / Give",
  "(b) An embedded system has DRAM. Identify one benefit of using DRAM instead of SRAM in an embedded system. (c) Give two differences between EPROM and EEPROM.", "Cheaper or denser; UV against electrical, removal, whole or part.",
  "<p><b>(b)</b> One: " + mks(["DRAM is less expensive to manufacture or purchase than SRAM", "DRAM has a higher bit density per chip"]) + "</p><p><b>(c)</b> Any two: " + mks(["EPROM uses ultraviolet light to erase data; EEPROM uses an electrical signal", "EPROM has to be removed from the circuit board when changing the data; EEPROM stays in the circuit", "EPROM erases all the data; EEPROM can erase parts of the data"], "a") + "</p>", None) + peq(SRC("w24", "13", "Q2(a)"), "2 marks", "Identify",
  "A memory buffer uses Dynamic RAM (DRAM). Identify two differences between DRAM and Static RAM (SRAM).", "Refresh, capacity, speed.",
  "<p>Any two: " + mks(["DRAM requires constant refreshing; SRAM does not", "DRAM generally has greater capacities per chip; SRAM has lower", "DRAM has slower access times than SRAM"]) + "</p>", None)

review = req("2 marks", "Distinguish", "Distinguish between RAM and ROM.", "Volatile; contents.", "<p>" + mks(["RAM is volatile and holds the data and programs currently in use", "ROM is non-volatile and holds the boot-up instructions"]) + "</p>", None) + req("3 marks", "Explain", "Explain why a game console uses SRAM for its cache and DRAM for its main memory.", "Speed and cost/density.", "<p>" + mks(["SRAM is faster because it needs no refresh, so it suits the small cache", "DRAM is cheaper per bit", "and denser, so a large main memory is affordable"]) + "</p>", None) + req("2 marks", "Describe", "Describe how a DRAM cell stores a bit.", "Capacitor.", "<p>" + mks(["A capacitor is charged or not charged to represent 1 or 0, controlled by a transistor", "The charge leaks, so it must be refreshed constantly"]) + "</p>", None) + req("2 marks", "Explain", "A router's firmware is stored in EEPROM. Explain why.", "Updates.", "<p>" + mks(["The firmware can be updated many times", "electrically without removing the chip from the router"]) + "</p>", None) + req("1 mark", "State", "State what PROM stands for and one limitation.", "Once.", "<p>" + mks(["Programmable ROM: it can only be programmed once"]) + "</p>", None)

tips = tips_html([
  ("SRAM: flip-flops, fast.", "No refresh, costly, lower density."),
  ("DRAM: capacitor, refresh.", "Cheaper, denser, slower."),
  ("EPROM: UV, removed, whole chip.", "EEPROM: electrical, in situ, partial."),
  ("PROM: once only.", "Do not call it rewritable."),
  ("RAM: running. ROM: start-up.", "Say which is volatile."),
  ("Write a pair.", "'DRAM is cheaper' needs 'SRAM is dearer' to be a difference."),
], [("volatile", "Loses its contents when the power is switched off."), ("refresh", "Rewriting a DRAM capacitor's charge before it leaks."), ("in situ", "Without removing the chip from the device."), ("firmware", "Permanent instructions stored in ROM or EEPROM.")],
  [("Identify", "Name the point."), ("Explain", "Reasons as well."), ("Give", "State the differences."), ("Complete", "Fill in missing words.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lvl = [0, 1, 0.5, 0.15, 1][k]; let o = SV.rect(60, 40, 90, 24, "f3", { rx: 4 }) + SV.text(105, 57, "transistor", "sm", { "text-anchor": "middle" }) + SV.rect(200, 30, 50, 90, "cell", { rx: 4 }) + SV.rect(200, 120 - 90 * lvl, 50, 90 * lvl, "f1", { rx: 4 }) + SV.text(225, 140, "capacitor", "sm", { "text-anchor": "middle" }) + SV.path("M150,52 H200", "ax");
    o += SV.text(340, 60, k === 0 ? "empty cell" : k === 1 ? "charged: stores a 1" : k === 2 ? "charge leaking..." : k === 3 ? "almost lost!" : "refreshed: back to 1", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 170, label: "DRAM cell", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "A DRAM cell is a transistor and a capacitor.", s: { i: 0 } }, { cap: "The capacitor is charged to store a 1.", s: { i: 1 } }, { cap: "The charge leaks away over time.", s: { i: 2 } }, { cap: "If nothing happens the 1 is lost.", s: { i: 3 } }, { cap: "A refresh circuit rewrites it before it is lost. It repeats constantly.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(150, 20, "EPROM", "lbl bd", { "text-anchor": "middle" }) + SV.text(450, 20, "EEPROM", "lbl bd", { "text-anchor": "middle" }) + SV.rect(80, 40, 140, 60, k >= 2 ? "cell" : "f3", { rx: 6 }) + SV.rect(380, 40, 140, 60, k >= 3 ? "f2" : "f3", { rx: 6 });
    if (k >= 1) o += SV.text(150, 125, "removed from the board", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.text(150, 145, "UV light erases the whole chip", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); if (k >= 3) o += SV.text(450, 125, "stays in the circuit", "sm", { "text-anchor": "middle" }) + SV.text(450, 145, "voltage erases just a byte", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 165, label: "Erasing", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "Both can be programmed and reprogrammed.", s: { i: 0 } }, { cap: "<b>EPROM</b> must be taken out of the device.", s: { i: 1 } }, { cap: "UV light erases <b>everything</b> on the chip.", s: { i: 2 } }, { cap: "<b>EEPROM</b> is erased electrically <b>in situ</b>, and parts can be erased.", s: { i: 3 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 50, 100, 46, k >= 1 ? "f3" : "cell", { rx: 8 }) + SV.text(70, 78, "ROM boot", "lbl bd", { "text-anchor": "middle" }) + SV.rect(250, 50, 100, 46, k >= 2 ? "f3" : "cell", { rx: 8 }) + SV.text(300, 78, "Storage", "lbl bd", { "text-anchor": "middle" }) + SV.rect(480, 50, 100, 46, k >= 3 ? "f3" : "cell", { rx: 8 }) + SV.text(530, 78, "RAM", "lbl bd", { "text-anchor": "middle" });
    if (k >= 2) o += SV.path("M120,73 H250", "ax"); if (k >= 3) o += SV.path("M350,73 H480", "ax"); o += SV.text(300, 140, ["power on", "ROM runs the start-up program", "it finds the operating system", "the OS is copied into RAM and runs", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 600, h: 160, label: "Start-up", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: [{ cap: "The computer is switched on. RAM is empty.", s: { i: 0 } }, { cap: "The processor runs the <b>start-up instructions in ROM</b>.", s: { i: 1 } }, { cap: "They locate the operating system on secondary storage.", s: { i: 2 } }, { cap: "The OS is copied into <b>RAM</b> and takes over.", s: { i: 3 } }] });
})();

(function () {
  let iv = 40; const leak = 64; const paint = () => { let d = ""; for (let t = 0; t <= 200; t++) { const tt = t % iv; const q = Math.max(0, 1 - tt / leak); d += (t ? "L" : "M") + (30 + t * 1.8) + "," + (130 - q * 100) + " "; } const lost = iv > leak;
    $("#rG").innerHTML = `<svg viewBox="0 0 420 160" style="width:420px;max-width:100%;display:block"><path d="M30,20 V130 H400" class="ax"/><path d="${d}" fill="none" stroke="${lost ? "var(--bad)" : "var(--accent)"}" stroke-width="2.5"/><text x="400" y="152" class="sm" text-anchor="end" style="font-size:11px">time</text><text x="34" y="16" class="sm" style="font-size:11px">charge</text></svg>`;
    $("#rV").innerHTML = lost ? `Refreshing every <b>${iv} ms</b> is too slow: the charge leaks away (in ${leak} ms) before it is rewritten, so the <b>1 is lost</b>.` : `Refreshing every <b>${iv} ms</b> rewrites the charge before it is lost, so the data is kept. This constant refreshing is why DRAM is slower than SRAM.`; };
  Lib.slider($("#rS1"), { id: "r1", label: "Refresh interval (ms) ", min: 10, max: 120, value: iv, fmt: (x) => x, onInput: (v) => { iv = v; paint(); } }); paint();
})();
btnTable("sB", "sO", [
  ["CPU cache", "SRAM", "Fastest; no refresh; expensive"],
  ["Main memory of a PC", "DRAM", "Cheap and dense"],
  ["Printer buffer of 1 GB", "DRAM", "Speed not critical; lots of capacity"],
  ["Needs refreshing constantly", "DRAM", "Capacitor leaks"],
  ["Uses flip-flops", "SRAM", "Stays set until changed"]
], ["Use or feature", "Type", "Why"]);
btnTable("rB", "rO", [
  ["Router firmware that is updated by the maker", "EEPROM", "Rewritable in situ"],
  ["Data written at the factory and never changed", "PROM or ROM", "Once only is enough"],
  ["Chip taken out and put under UV light to erase", "EPROM", "UV and removed"],
  ["Erase one byte only", "EEPROM", "Partial erase"],
  ["BIOS that is fixed", "ROM", "Boot instructions"]
], ["Description", "Type", "Why"]);
''' + _prjs

finish("as-3-1-3-ram-rom-sram-dram-eeprom", "as313", "RAM, ROM, SRAM, DRAM and EEPROM",
  "RAM and ROM, SRAM and DRAM, and PROM, EPROM and EEPROM compared, with animations, a DRAM refresh lab and the real Paper 1 questions from 2021 to 2026.",
  "3.1.3", "3 · Hardware", "section 3.1 Computers and their components", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on RAM, ROM and their types (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
