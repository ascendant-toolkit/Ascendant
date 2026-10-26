"""A Level CS syllabus 16.1.4: virtual memory, paging, segmentation, page replacement and disk thrashing. Run: python3 tools/artifact-kit/mk_ac1614.py"""
from ak16 import *


def fault_trace(refs, nframes, policy):
    """Page-replacement trace: (page, frames after, fault?) per reference."""
    fr, out, last = [], [], {}
    for i, p in enumerate(refs):
        f = p not in fr
        if f:
            if len(fr) == nframes:
                v = fr[0] if policy == "FIFO" else min(fr, key=lambda x: last[x])
                fr.remove(v)
            fr.append(p)
        last[p] = i
        out.append((p, list(fr), f))
    return out


REFS = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
fifo = fault_trace(REFS, 3, "FIFO")
lru = fault_trace(REFS, 3, "LRU")
assert sum(f for *_, f in fifo) == 9 and sum(f for *_, f in lru) == 10


def trace_table(tr):
    h = '<div class="tw"><table class="t mono"><tr><th>Page</th>' + "".join(f"<td>{p}</td>" for p, _, _ in tr) + "</tr>"
    for r in range(3):
        h += f"<tr><th>frame {r + 1}</th>" + "".join(f"<td>{fr[r] if r < len(fr) else ''}</td>" for _, fr, _ in tr) + "</tr>"
    h += "<tr><th>fault</th>" + "".join(f"<td>{'F' if f else ''}</td>" for *_, f in tr) + "</tr></table></div>"
    return h


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Virtual memory</b> uses part of secondary storage (the disk) to extend main memory (RAM), so the CPU appears to be able to use more memory than is physically installed; only the data in use needs to be in RAM and the rest is swapped in and out as necessary. It is managed by <b>paging</b>, which divides memory into <b>fixed-size</b> blocks (pages in the logical address space, frames in physical memory), or by <b>segmentation</b>, which divides it into <b>variable-size</b> logical segments such as code, data and stack. A page or segment <b>table</b> maps the logical address the program uses onto a physical address in RAM. When RAM is full a page has to be <b>replaced</b>: the OS chooses one to move out to disk to make room. If too much swapping takes place the computer suffers <b>disk thrashing</b>: more time is spent moving pages than running programs.</p></div>

  <h2>1 · Why virtual memory is needed</h2>
  <ul>
    <li>RAM is limited, and running many processes at once could need more memory than is installed.</li>
    <li>Programs and data that are not needed immediately can be <b>moved from RAM to virtual memory</b> on the disk, which makes efficient use of RAM and the processor.</li>
    <li>Virtual memory is created <b>temporarily</b> when it is needed, using space on the disk.</li>
    <li>It is slower than RAM, because the disk is much slower.</li>
  </ul>

  <h2>2 · Paging</h2>
  <p>In <b>paging</b> the memory is divided into blocks of the <b>same fixed size</b>. The program's (logical) address space is divided into <b>pages</b>; physical memory into <b>frames</b> of the same size. Any page can go in any free frame, so the frames used by a program need not be next to each other.</p>
  <ul>
    <li>A <b>page table</b> records, for each page, the frame it is in (or that it is not in memory).</li>
    <li>A logical address is a <b>page number</b> and an <b>offset</b> within that page. The OS uses the page table to find the frame, then adds the offset: physical address = frame number × page size + offset.</li>
    <li>Only the pages in use need to be in RAM. If the CPU needs a page that is not in RAM there is a <b>page fault</b>: the OS reads the page from the disk into a free frame (or into a frame freed by replacing another page).</li>
    <li>The OS divides memory into pages (not the programmer).</li>
  </ul>
  <p>Example. Page size 1024 bytes. Logical address 3000 is in page 3000 ÷ 1024 = 2 (remainder 952): page 2, offset 952. If the page table says page 2 is in frame 7, the physical address is 7 × 1024 + 952 = 8120.</p>

  <h2>3 · Segmentation</h2>
  <p>In <b>segmentation</b> the logical address space is divided into <b>segments of varying size</b>, usually the logical parts of a program such as the main code, a procedure, the data or the stack. The size of each segment is decided by the program or the compiler, not by the OS.</p>
  <ul>
    <li>Each segment has a <b>name or number</b> and a <b>size</b>. Segments are numbered, and the number is used as an index in a <b>segment map table</b> that maps logical addresses to physical addresses.</li>
    <li>A logical address is a <b>segment number and an offset</b>. The offset must be within the size of the segment.</li>
    <li>During execution, segments from virtual memory are loaded into physical memory.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th></th><th>Paging</th><th>Segmentation</th></tr>
    <tr><td><b>Size of block</b></td><td>Fixed-size pages and frames</td><td>Variable-size segments</td></tr>
    <tr><td><b>Who decides the division</b></td><td>The operating system</td><td>The programmer or compiler (logical units)</td></tr>
    <tr><td><b>Address</b></td><td>Page number + offset</td><td>Segment number + offset</td></tr>
    <tr><td><b>Table</b></td><td>Page table</td><td>Segment map table</td></tr>
    <tr><td><b>Access time</b></td><td>Generally faster</td><td>Slower</td></tr>
  </table></div>

  <h2>4 · Replacing pages</h2>
  <p>When a page fault occurs and no frame is free, the OS must pick a page to remove (a <b>victim</b>). If that page has been changed since it was loaded, it is written back to the disk first. The syllabus does not name the algorithm; two common ones are <b>first in first out</b> (replace the page that has been in memory longest) and <b>least recently used</b> (replace the page not used for the longest time). A good choice keeps the pages that are about to be needed in RAM.</p>
  <p>Reference string 1 2 3 4 1 2 5 1 2 3 4 5 with 3 frames. F marks a page fault.</p>
  <h3>First in first out: 9 faults</h3>
  ''' + trace_table(fifo) + '''
  <h3>Least recently used: 10 faults</h3>
  ''' + trace_table(lru) + '''
  <p>Neither is always better: here FIFO happens to give fewer faults. You will not be asked to run an algorithm in the exam, but you should be able to explain what page replacement does.</p>

  <h2>5 · Disk thrashing</h2>
  <p><b>Disk thrashing</b> can occur when virtual memory is being used and <b>main memory is full</b>. More and more pages have to be swapped between RAM and the disk, so there is a very high rate of disk accesses and the read/write head moves constantly. Moving the head takes a long time, so eventually <b>more time is spent swapping pages than processing data</b> (the thrash point), and programs may freeze or fail to run.</p>
  <p>It can be reduced by installing <b>more RAM</b> or by running <b>fewer programs</b> at once.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Saying virtual memory is "the same as RAM" or "a type of RAM". It is disk space used as an extension of memory.</li>
    <li>Giving the difference between paging and segmentation without both sides: pages are fixed size, segments are variable size.</li>
    <li>Describing segmentation without the segment number, the offset and the segment map table.</li>
    <li>Explaining thrashing as "the disk wearing out". It is excessive swapping, so more time is spent on swapping than on processing.</li>
    <li>Forgetting the cause of thrashing: main memory is full while virtual memory is in use.</li>
  </ul>
'''

watch = '''
  <h2>1 · Paging: pages, frames and the page table</h2>
  <p>Press Play. The program's pages sit in different frames; the page table records where.</p>
  <div id="stA"></div>
  <h2>2 · Segmentation: variable-size segments</h2>
  <div id="stB"></div>
  <h2>3 · How thrashing develops</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Translate an address</h2>
  <p>The page size is 1024 bytes. Choose a logical address; see its page, offset and physical address.</p>
  <div class="card"><div id="aS"></div><div id="aO"></div></div>

  <h2>Lab 2 · Page replacement</h2>
  <p>The reference string is 1 2 3 4 1 2 5 1 2 3 4 5. Choose the number of frames and the replacement rule.</p>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rS"></div><div id="rO"></div></div>

  <h2>Lab 3 · How many programs before thrashing?</h2>
  <p>The computer has 12 frames of RAM. Each program needs 3 frames at a time.</p>
  <div class="card"><div id="tS"></div><div id="tO"></div><div class="verdict" id="tV"></div></div>
'''

practise = '''
  <h2>1 · Paging or segmentation?</h2><div id="cl1" class="card"></div>
  <h2>2 · True or false about virtual memory?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put what happens in a page fault in order</h2><div id="o1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A computer slows down when you open too many programs", "The OS moves pages out to the disk to make room. If you open even more, it spends its time moving pages back and forth: thrashing. Closing programs or adding RAM helps.", "disk thrashing: more time swapping than processing.") +
rw("A very large game on a computer with little RAM", "Only the parts of the game in use are kept in RAM; the rest wait on the disk and are paged in when needed. The game runs, but loading pauses are noticeable.", "virtual memory extends RAM.") +
rw("A library with a few reading desks", "The desks are RAM and the stacks are the disk. You keep only the books you are using on the desk and fetch others when needed. If you keep swapping books, you spend more time walking than reading.", "swapping and thrashing.") +
rw("Chapters and pages of a book", "Paging splits the book into equal pages whatever is on them. Segmentation splits it into chapters of different lengths because each chapter is a logical unit.", "fixed size against variable size.") +
rw("Fitting furniture into rooms", "Paging is like cutting everything into identical boxes so they fit anywhere; segmentation keeps each piece whole, so it needs a space big enough for it.", "frames can be anywhere; segments need contiguous blocks.")
)

where = [
  ("O/N 2022", "31, 33", "8(a), 8(b)", "3 + 1", "Explain virtual memory; one difference between paging and segmentation"),
  ("O/N 2023", "32", "5(a), 5(b)", "2 + 3", "Reasons the OS may need virtual memory; circumstances for disk thrashing"),
  ("O/N 2024", "31, 33", "8(a), 8(b)", "4 + 3", "Describe segmentation; explain disk thrashing"),
  ("M/J 2021", "31, 32, 33", "3(a)", "5", "Paging and virtual memory matched to descriptions (on the 16.1.1 page)")]

past = '''  <p class="note">Virtual memory, paging, segmentation and thrashing have appeared in Paper 3 in Oct/Nov 2022, 2023 and 2024. Page replacement algorithms have not been asked. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w22", "31/33", "Q8"), "3 + 1 marks", "Explain / State",
  "Virtual memory, paging and segmentation are used in memory management. (a) Explain what is meant by virtual memory. (b) State one difference between paging and segmentation in the way memory is divided.",
  "(a) disk extends RAM, so the CPU appears to have more memory, swapped as necessary.",
  "<p><b>(a)</b> Any three: " + mks(["Disk or secondary storage is used to extend the RAM available", "so the CPU appears to be able to access more memory space than the available RAM", "Only the data in use needs to be in main memory, so data can be swapped between RAM and virtual memory as necessary", "Virtual memory is created temporarily"]) + "</p><p><b>(b)</b> One: " + mks(["Paging divides memory into fixed-size blocks; segmentation divides it into variable-size blocks", "The OS divides memory into pages; the compiler is responsible for calculating the segment sizes"], "a") + "</p>", "Writing that virtual memory is 'extra RAM'. It is space on the disk that is used as if it were RAM.") + peq(SRC("w23", "32", "Q5"), "2 + 3 marks", "Outline / Explain",
  "(a) Outline the reasons why an operating system may need to use virtual memory. (b) Explain the circumstances in which disk thrashing could occur.",
  "(a) RAM running low, many processes; (b) frequent swapping, heads moving, more time swapping than processing.",
  "<p><b>(a)</b> Any two: " + mks(["Virtual memory is used when RAM is running low", "such as when a computer is running many processes at once", "It may be used for efficient use of RAM and the processor", "such as when data or programs are not immediately needed, they can be moved from RAM to virtual memory"]) + "</p><p><b>(b)</b> Any three: " + mks(["Disk thrashing may occur when frequent transfers take place between main memory and secondary memory, or when virtual memory is being used", "As main memory fills up, more pages need to be swapped in and out of virtual memory", "This swapping leads to a very high rate of hard disk head movements", "Eventually more time is spent swapping the pages than processing the data"]) + "</p>", "Describing the effect (the computer is slow) without the circumstance (main memory is full and pages are swapped constantly).") + peq(SRC("w24", "31/33", "Q8"), "4 + 3 marks", "Describe / Explain",
  "(a) Describe the process of segmentation for memory management. (b) Explain what is meant by disk thrashing.",
  "(a) variable sizes, segment number and offset, segment map table.",
  "<p><b>(a)</b> Any four: " + mks(["In segmented memory the logical (virtual) address space is broken into varying-sized blocks called segments", "Each segment has a name and size", "During execution, segments from logical memory are loaded into physical memory", "The address is specified by the user and contains the segment name and an offset value", "Segments are numbered, and this number is used as an index in the segment map table", "The offset value determines the size of the segment", "A segment map table maps logical addresses to physical addresses"]) + "</p><p><b>(b)</b> Any three: " + mks(["Disk thrashing is a problem that may occur when virtual memory is being used", "As main memory fills up, more and more pages need to be swapped in and out of virtual memory", "This leads to a very high rate of hard disk access or head movement", "Moving the read/write head takes a relatively long time", "Eventually more time is spent swapping pages than processing data (the thrash point), which can cause the program to freeze or not run"]) + "</p>", "Describing segmentation as 'splitting memory into equal parts'. That is paging. Segments vary in size.")

review = req("3 marks", "Explain", "Explain how a page table is used to find the physical address for a logical address.", "Page number, frame, offset.", "<p>" + mks(["The logical address is split into a page number and an offset", "The page table is looked up with the page number to give the frame the page is in", "The physical address is the frame's start address plus the offset"]) + "</p>", None) + req("3 marks", "Calculate", "The page size is 1024 bytes. A program uses the logical address 2100. State the page number and offset. Page 2 is in frame 5. Give the physical address.", "Divide by 1024.", "<p>" + mks(["Page number 2 (2100 ÷ 1024 = 2 remainder 52)", "Offset 52", "Physical address 5 × 1024 + 52 = 5172"]) + "</p>", None) + req("2 marks", "Explain", "Explain what happens when a page fault occurs.", "The needed page is not in RAM.", "<p>" + mks(["The OS finds that the page needed is not in main memory", "It reads the page from the disk into a free frame, replacing another page if there is none free"]) + "</p>", None) + req("2 marks", "State", "State two ways of reducing disk thrashing.", "Memory and processes.", "<p>" + mks(["Add more RAM", "Run fewer programs at the same time"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a page and a segment.", "Size.", "<p>" + mks(["A page is a fixed-size block of the logical address space chosen by the OS", "A segment is a variable-size logical part of the program, such as code or data, with its size chosen by the programmer or compiler"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on virtual memory, paging, segmentation and disk thrashing (Paper 3), 2022 to 2024. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Virtual memory uses the disk.", "It extends RAM; the CPU appears to have more memory."),
  ("Paging: fixed. Segmentation: variable.", "Pages and frames are the same size; segments differ."),
  ("Segmentation answers.", "Segment number, offset, segment map table."),
  ("Page fault.", "The page is not in RAM: load it from the disk, replacing another if RAM is full."),
  ("Thrashing needs a cause.", "Main memory full, constant swapping, more time swapping than processing."),
  ("Fix thrashing.", "More RAM or fewer programs."),
], [
  ("virtual memory", "Disk space used to extend main memory."),
  ("a page", "A fixed-size block of the logical address space."),
  ("a segment", "A variable-size logical part of a program."),
  ("disk thrashing", "Excess swapping so more time is spent swapping than processing."),
], [("Explain", "Give the reasons as well."), ("Describe", "Say how it works, in several points."), ("Outline", "Give the main points."), ("State", "One short answer.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Program (logical)", "lbl bd") + SV.text(300, 20, "RAM (frames)", "lbl bd") + SV.text(510, 20, "Page table", "lbl bd");
    const frames = { 0: 2, 1: 0, 2: 3, 3: 1 }; // page -> frame
    [0, 1, 2, 3].forEach((p) => { o += SV.rect(20, 32 + p * 52, 130, 42, k === 3 && p === 3 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(85, 58 + p * 52, "page " + p, "lbl", { "text-anchor": "middle" }); });
    [0, 1, 2, 3].forEach((f) => { const p = Object.keys(frames).find((x) => frames[x] === f); const here = k >= 1 && p !== undefined && (+p !== 3 || k >= 4); o += SV.rect(300, 32 + f * 52, 130, 42, here ? "f" + (f + 1) : "cell", { rx: 6, ...op(here ? 1 : 0.5) }) + SV.rect(300, 32 + f * 52, 130, 42, "ax", { rx: 6, fill: "none", ...op(here ? 1 : 0.4) }) + SV.text(365, 58 + f * 52, here ? "page " + p : "frame " + f + " (free)", "lbl", { "text-anchor": "middle", ...op(here ? 1 : 0.6) }); });
    [0, 1, 2, 3].forEach((p) => { const inmem = p !== 3 || k >= 4; o += SV.rect(510, 32 + p * 52, 150, 42, k >= 2 ? "cell" : "cell", { rx: 6, ...op(k >= 2 ? 1 : 0.35) }) + (k >= 2 ? SV.text(585, 58 + p * 52, p + " → " + (inmem ? "frame " + frames[p] : "on disk"), "lbl", { "text-anchor": "middle" }) : ""); });
    if (k >= 1) [0, 1, 2].forEach((p) => (o += SV.path("M150," + (53 + p * 52) + " L300," + (53 + frames[p] * 52), "edge", { ...op(0.55) }))); if (k >= 4) o += SV.path("M150,209 L300,85", "edge", { style: "stroke:var(--accent);stroke-width:3.5" });
    return o; };
  Lib.stepper($("#stA"), { w: 700, h: 252, label: "Paging", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [
    { cap: "A program has four <b>pages</b> of the same size. RAM is divided into <b>frames</b> of the same size.", s: { i: 0 } },
    { cap: "Pages 0, 1 and 2 are loaded into frames. They do not have to be next to each other, and not every page has to be in RAM.", s: { i: 1 } },
    { cap: "The <b>page table</b> records which frame each page is in. Page 3 is still on the disk.", s: { i: 2 } },
    { cap: "The program needs page 3. It is not in RAM: a <b>page fault</b>. The OS must fetch it from the disk.", s: { i: 3 } },
    { cap: "The OS loads page 3 into a free frame and updates the page table. The program carries on.", s: { i: 4 } }] });
})();
(function () {
  const segs = [["Main code", 3], ["Procedure", 2], ["Data", 4], ["Stack", 1]]; const base = [0, 3, 5, 9], tw = 40;
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "Segments (logical, different sizes)", "lbl bd") + SV.text(380, 20, "RAM", "lbl bd") + SV.text(380, 168, "", "sm");
    let y = 30; segs.forEach(([n, h], i) => { o += SV.rect(20, y, 220, 14 * h + 8, i === 2 && k === 3 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(130, y + (14 * h + 8) / 2 + 5, i + ": " + n + " (size " + h + ")", "lbl", { "text-anchor": "middle" }); y += 14 * h + 16; });
    segs.forEach(([n, h], i) => { const on = k >= 1; o += SV.rect(380, 30 + base[i] * 18, 150, 18 * h - 2, on ? "f" + (i + 1) : "cell", { rx: 4, ...op(on ? 1 : 0.35) }) + (on ? SV.text(455, 30 + base[i] * 18 + (18 * h - 2) / 2 + 5, n, "lbl", { "text-anchor": "middle" }) : ""); });
    if (k >= 2) { o += SV.text(570, 36, "Segment map table", "lbl bd"); segs.forEach(([n, h], i) => (o += SV.text(570, 62 + i * 24, i + " → base " + base[i] + ", size " + h, "lbl", { style: "font-size:12.5px" }))); }
    if (k === 3) o += SV.text(380, 252, "address (2, 3): segment 2, offset 3 → base 5 + 3 = 8", "lbl bd t3", { style: "font-size:13px" });
    return o; };
  Lib.stepper($("#stB"), { w: 800, h: 280, label: "Segmentation", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [
    { cap: "The program is divided into logical <b>segments</b> of <b>different sizes</b>: code, a procedure, data, and the stack.", s: { i: 0 } },
    { cap: "Each segment is loaded into a block of RAM large enough to hold it.", s: { i: 1 } },
    { cap: "The <b>segment map table</b> records the start address (base) and size of each segment.", s: { i: 2 } },
    { cap: "A logical address is a <b>segment number and an offset</b>. (2, 3) means segment 2, offset 3: base 5 + offset 3 = physical 8. The offset must be less than the segment's size.", s: { i: 3 } }] });
})();
(function () {
  const pts = [[1, 30], [2, 55], [3, 80], [4, 95], [5, 80], [6, 45], [7, 18], [8, 8]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.path("M60,20 V190 H500", "ax") + SV.text(280, 214, "number of programs running", "sm", { "text-anchor": "middle" }) + SV.text(14, 14, "CPU doing useful work (%)", "sm");
    let d = ""; pts.slice(0, k).forEach(([n, u], i) => { const x = 60 + n * 52, y = 190 - u * 1.7; d += (i ? "L" : "M") + x + "," + y + " "; o += SV.circle(x, y, 5, k >= 6 && n >= 6 ? "dot2" : "dot3") + SV.text(x, 208, String(n), "sm", { "text-anchor": "middle", style: "display:none" }); });
    if (k > 1) o += SV.path(d, "c3"); if (k >= 5) o += SV.text(250, 38, "RAM is full: pages are swapped in and out", "lbl bd t4", { style: "font-size:13px" }); if (k >= 7) o += SV.text(380, 120, "thrashing", "lbl bd t2"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 230, label: "Thrashing", base: { i: 0 }, draw, tween: 120, dwell: 2200, steps: [{ cap: "One program: the CPU is often idle waiting for the disk.", s: { i: 1 } }, { cap: "More programs: the CPU is used more.", s: { i: 3 } }, { cap: "A peak: RAM holds just enough pages for every program.", s: { i: 4 } }, { cap: "Too many programs: RAM is full and pages are swapped in and out all the time.", s: { i: 5 } }, { cap: "More swapping means more disk head movement and long waits.", s: { i: 6 } }, { cap: "<b>Thrashing</b>: more time is spent swapping pages than processing data, so useful work falls to a few percent.", s: { i: 8 } }] });
})();

(function () {
  const PT = { 0: 5, 1: 2, 2: 7, 3: 1 }; let a = 3000; const PS = 1024;
  const paint = () => { const pg = Math.floor(a / PS), off = a % PS, fr = PT[pg]; $("#aO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Page</th><th>Frame</th></tr>' + Object.entries(PT).map(([p, f]) => `<tr${+p === pg ? ' style="background:var(--accent-soft);font-weight:700"' : ""}><td>${p}</td><td>${f}</td></tr>`).join("") + "</table></div>" + `<div class="verdict">Logical address <b>${a}</b>: page = ${a} ÷ ${PS} = <b>${pg}</b>, offset = <b>${off}</b>. ` + (fr === undefined ? "This page is not in the page table: page fault." : `Page ${pg} is in frame ${fr}: physical address = ${fr} × ${PS} + ${off} = <b>${fr * PS + off}</b>.`) + "</div>"; };
  Lib.slider($("#aS"), { id: "as", label: "Logical address ", min: 0, max: 4095, value: a, fmt: (x) => x, onInput: (v) => { a = v; paint(); } }); paint();
})();
(function () {
  const refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]; let nf = 3, pol = "FIFO"; const b = $("#rB");
  const run = () => { const fr = [], last = {}, out = []; refs.forEach((p, i) => { const f = !fr.includes(p); if (f) { if (fr.length === nf) { const v = pol === "FIFO" ? fr[0] : fr.reduce((m, x) => (last[x] < last[m] ? x : m)); fr.splice(fr.indexOf(v), 1); } fr.push(p); } last[p] = i; out.push([p, fr.slice(), f]); }); return out; };
  const paint = () => { const tr = run(); let h = '<div class="tw"><table class="t mono"><tr><th>Page</th>' + tr.map(([p]) => `<td>${p}</td>`).join("") + "</tr>"; for (let r = 0; r < nf; r++) h += `<tr><th>frame ${r + 1}</th>` + tr.map(([, f]) => `<td>${f[r] === undefined ? "" : f[r]}</td>`).join("") + "</tr>"; h += "<tr><th>fault</th>" + tr.map(([, , f]) => `<td>${f ? "F" : ""}</td>`).join("") + "</tr></table></div>";
    $("#rO").innerHTML = h + `<div class="verdict">${pol}, ${nf} frames: <b>${tr.filter((x) => x[2]).length}</b> page faults out of ${refs.length} references. ${nf >= 5 ? "With enough frames only the first use of each page faults." : ""}</div>`; b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === pol ? "on" : "")); };
  ["FIFO", "LRU"].forEach((k) => { const x = document.createElement("button"); x.textContent = k === "FIFO" ? "First in first out" : "Least recently used"; x.dataset.k = k; x.onclick = () => { pol = k; paint(); }; b.appendChild(x); });
  Lib.slider($("#rS"), { id: "rs", label: "Frames ", min: 2, max: 6, value: nf, fmt: (x) => x, onInput: (v) => { nf = v; paint(); } }); paint();
})();
(function () {
  let n = 3;
  const paint = () => { const need = 3 * n, ram = 12, fault = Math.max(0, (need - ram) / need), useful = Math.round(Math.min(1, 0.28 * n) * (1 - Math.min(0.96, 2.2 * fault)) * 100);
    $("#tO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Programs</th><th>Frames needed</th><th>RAM</th><th>Pages swapped a lot?</th><th>Useful CPU work</th></tr>' + `<tr><td>${n}</td><td>${need}</td><td>${ram}</td><td>${need > ram ? "yes" : "no"}</td><td>${useful}%</td></tr></table></div>`;
    $("#tV").innerHTML = need <= ram ? "All the pages the programs need fit in RAM, so there is little swapping." : "The programs need <b>" + need + "</b> frames but RAM has only 12. Pages are swapped between RAM and the disk all the time. " + (useful < 30 ? "This is <b>thrashing</b>: more time is spent swapping than processing." : "Performance is falling."); };
  Lib.slider($("#tS"), { id: "ts", label: "Programs running ", min: 1, max: 8, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Is it a feature of paging or segmentation?", ["Paging", "Segmentation"],
  [("Blocks are all the same size", 0), ("Blocks vary in size", 1), ("The OS divides memory into the blocks", 0), ("The compiler works out the sizes", 1), ("The address is a page number and an offset", 0), ("The address is a segment number and an offset", 1), ("Uses a page table", 0), ("Uses a segment map table", 1)],
  "Paging: fixed, OS. Segmentation: variable, logical units.") + CLASSIFY("cl2", "True or false about virtual memory?", ["True", "False"],
  [("It uses secondary storage to extend RAM", 0), ("It is faster than RAM", 1), ("The CPU appears to have more memory", 0), ("It is created temporarily when needed", 0), ("It is a type of RAM chip", 1), ("Data not in use can be moved to it", 0)],
  "Disk space, slower than RAM.") + MATCH([
  ["Page", "Fixed-size block of the logical address space"], ["Frame", "Fixed-size block of physical memory"], ["Page fault", "The page needed is not in RAM"], ["Segment", "Variable-size logical part of a program"], ["Thrashing", "More time swapping pages than processing"]]) + ORDER(
  "Put the steps of a page fault in order.",
  ["The CPU needs a page that is not in RAM", "The OS finds the page on the disk", "A free frame is found, or a page is replaced", "The page is loaded into the frame and the page table is updated", "The program carries on"],
  "Need, find, frame, load, continue.") + CALC([
  {"q": "The page size is 1024 bytes. Which page contains the logical address 5000?", "a": 4, "unit": "", "tol": 0.01, "hint": "5000 ÷ 1024 = 4.88.", "sol": "<b>4</b>."},
  {"q": "What is the offset of the logical address 5000 (page size 1024)?", "a": 904, "unit": "", "tol": 0.01, "hint": "5000 − 4 × 1024.", "sol": "5000 − 4096 = <b>904</b>."},
  {"q": "Page 4 is in frame 2. What is the physical address of logical address 5000?", "a": 2952, "unit": "", "tol": 0.01, "hint": "2 × 1024 + 904.", "sol": "2048 + 904 = <b>2952</b>."},
  {"q": "A segment starts at base 5 (in blocks) and the offset is 3. What is the physical block?", "a": 8, "unit": "", "tol": 0.01, "hint": "Base plus offset.", "sol": "<b>8</b>."},
  {"q": "A program has 6 pages. RAM can hold 4 of them. How many pages are on the disk?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 − 4.", "sol": "<b>2</b>."}]) + MCQ([
  ("Virtual memory uses:", ["Extra RAM chips", "Secondary storage", "Cache only", "ROM"], 1, "Disk space."),
  ("Pages are:", ["Variable-size blocks", "Fixed-size blocks of logical memory", "Files", "Folders"], 1, "Fixed-size blocks."),
  ("Which maps a segment number to a physical address?", ["Segment map table", "Page table", "Directory", "Stack"], 0, "The segment map table."),
  ("Disk thrashing happens when:", ["The disk is full", "Main memory is full and pages are swapped constantly", "The CPU is too fast", "The screen is off"], 1, "Constant swapping."),
  ("Who decides the segment sizes?", ["The user's keyboard", "The programmer or compiler", "The printer", "The monitor"], 1, "Logical units."),
  ("A page fault means:", ["The disk has failed", "The page is not in RAM", "The page is corrupt", "The CPU is hot"], 1, "The page is not in RAM.")], "qz1") + CARDS([
  ("Virtual memory", "Disk used to extend RAM; temporary."), ("Paging", "Fixed-size pages and frames; page table; page number + offset."), ("Segmentation", "Variable-size logical segments; segment map table."), ("Page fault", "Needed page not in RAM; load from disk."),
  ("Page replacement", "Choose a page to move out when RAM is full."), ("Thrashing", "Too much swapping: more time swapping than processing."), ("Fix thrashing", "More RAM or fewer programs."), ("Paging v segmentation", "Fixed v variable; OS v compiler.")])

build("ac1614", "ac-16-1-4-virtual-memory-paging-segmentation", "Virtual Memory, Paging and Segmentation", EYA("16.1.4"),
  "Virtual memory, paging with page tables, segmentation, page replacement and disk thrashing; animations, address-translation and page-replacement labs and the real Paper 3 questions from 2022 to 2024.",
  dict(sub=CBK("Chapter 16 · System software, section 16.1 Purposes of an operating system"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
