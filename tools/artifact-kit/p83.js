const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
const WPS = ["OPENFILE \"Scores.txt\" FOR WRITE", "FOR Count ← 1 TO 3", "    INPUT Score", "    WRITEFILE \"Scores.txt\", Score", "NEXT Count", "CLOSEFILE \"Scores.txt\""];
const WPY = ["file = open(\"Scores.txt\", \"w\")", "for count in range(3):", "    score = input()", "    file.write(score + \"\\n\")", "file.close()"];
const RPS = ["OPENFILE \"Scores.txt\" FOR READ", "Total ← 0", "FOR Count ← 1 TO 3", "    READFILE \"Scores.txt\", Score", "    Total ← Total + Score", "NEXT Count", "CLOSEFILE \"Scores.txt\"", "OUTPUT Total"];
const RPY = ["file = open(\"Scores.txt\", \"r\")", "total = 0", "for count in range(3):", "    score = int(file.readline())", "    total = total + score", "file.close()", "print(total)"];

/* ---------- file view ---------- */
function fl(lines, o) {
  let s = SV.text(14, 26, o.title, "lbl bd", { "text-anchor": "start" }); s += SV.rect(250, 50, 200, 170, "", { rx: 10, style: "fill:var(--surface);stroke:var(--line);stroke-width:3" }) + SV.text(350, 74, "Scores.txt", "lbl bd", { "text-anchor": "middle" });
  if (o.mode) s += chip(485, 50, 120, "mode: " + o.mode, o.mode === "WRITE" ? "var(--bad)" : o.mode === "READ" ? "var(--accent)" : "var(--muted)"); else s += chip(485, 50, 120, "file closed", "var(--muted)");
  lines.forEach((t, i) => { const y = 92 + i * 34, hi = o.ptr === i; s += SV.rect(268, y, 164, 28, "", { rx: 6, style: `fill:${hi ? "var(--accent-soft)" : "var(--soft)"};stroke:${hi ? "var(--accent)" : "var(--line)"};stroke-width:${hi ? 3 : 1.5};${o.dim ? "opacity:.35" : ""}` }) + SV.text(350, y + 20, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + SV.text(258, y + 20, i + 1, "sm", { "text-anchor": "end" }); });
  if (o.ptr !== undefined && o.ptr >= 0) s += SV.poly([[240, 92 + o.ptr * 34 + 14], [226, 92 + o.ptr * 34 + 6], [226, 92 + o.ptr * 34 + 22]], "t1");
  o.vars && o.vars.forEach(([n, v], i) => { s += SV.rect(20, 70 + i * 62, 170, 50, "", { rx: 8, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" }) + sm(105, 88 + i * 62, n) + SV.text(105, 110 + i * 62, String(v), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" }); });
  if (o.note) s += SV.text(320, 248, o.note, "lbl bd " + (o.nc || ""), { "text-anchor": "middle" }); return s;
}
function wFrames() {
  const F = [], IN = [72, 58, 91]; let L = ["40", "33"]; const f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: fl(L, { title: "Writing to a file", ...o }) });
  f("<b>Scores.txt</b> already holds two old scores. The file is closed.", [], [], { note: "Old data: 40, 33" });
  L = []; f("<b>OPENFILE FOR WRITE</b>: a <b>new file</b> is created. The old data is <b>lost</b>.", [0], [0], { mode: "WRITE", note: "Old scores erased", nc: "t2" });
  for (let i = 0; i < 3; i++) { f(`<b>INPUT Score</b>: the user types <b>${IN[i]}</b> (Count = ${i + 1}).`, [1, 2], [1, 2], { mode: "WRITE", vars: [["Score", IN[i]], ["Count", i + 1]] }); L = [...L, String(IN[i])]; f(`<b>WRITEFILE</b> puts ${IN[i]} into the file.`, [3], [3], { mode: "WRITE", ptr: i, vars: [["Score", IN[i]], ["Count", i + 1]] }); }
  f("<b>CLOSEFILE</b>: the file is closed, and the data is safely saved. It will still be there when the program is run again.", [5], [4], { note: "Saved: 72, 58, 91", nc: "t3" });
  return F;
}
Lib.algo($("#aW"), { w: 640, h: 270, label: "Writing to a file", pseudo: WPS, py: WPY, dwell: 2200, frames: wFrames() });
function rFrames() {
  const F = [], L = ["72", "58", "91"]; let tot = 0; const f = (cap, ps, py, o) => F.push({ cap, ps, py, svg: fl(L, { title: "Reading from a file", ...o }) });
  f("<b>OPENFILE FOR READ</b>: the file's data can now be read. The first READFILE will give line 1.", [0], [0], { mode: "READ" });
  f("<b>Total ← 0</b>.", [1], [1], { mode: "READ", vars: [["Total", 0]] });
  for (let i = 0; i < 3; i++) { const s = +L[i]; f(`<b>READFILE</b> (Count = ${i + 1}) reads the next line into Score: <b>${s}</b>.`, [3], [3], { mode: "READ", ptr: i, vars: [["Score", s], ["Total", tot]] }); const o = tot; tot += s; f(`<b>Total ← ${o} + ${s} = ${tot}</b>.`, [4], [4], { mode: "READ", ptr: i, vars: [["Score", s], ["Total", tot]] }); }
  f("<b>CLOSEFILE</b>: finished with the file.", [6], [5], { vars: [["Total", tot]] });
  f(`<b>OUTPUT Total</b>: ${tot}. The data came from the file, not from the keyboard.`, [7], [6], { vars: [["Total", tot]], note: "Output: " + tot, nc: "t3" });
  return F;
}
Lib.algo($("#aR"), { w: 640, h: 270, label: "Reading from a file", pseudo: RPS, py: RPY, dwell: 2000, frames: rFrames() });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdW"), { pseudo: ['OPENFILE "Names.txt" FOR WRITE', "FOR Count ← 1 TO 3", "    INPUT Name", '    WRITEFILE "Names.txt", Name', "NEXT Count", 'CLOSEFILE "Names.txt"'], py: ['file = open("Names.txt", "w")', "for count in range(3):", "    name = input()", '    file.write(name + "\\n")', "file.close()"] });
Lib.codePanel($("#cdR"), { pseudo: ['OPENFILE "Names.txt" FOR READ', "FOR Count ← 1 TO 3", '    READFILE "Names.txt", Name', "    OUTPUT Name", "NEXT Count", 'CLOSEFILE "Names.txt"'], py: ['file = open("Names.txt", "r")', "for count in range(3):", "    name = file.readline().strip()", "    print(name)", "file.close()"] });
Lib.codePanel($("#cdC"), { pseudo: ["DECLARE LineOfText : STRING", 'OPENFILE "FileA.txt" FOR READ', 'OPENFILE "FileB.txt" FOR WRITE', 'READFILE "FileA.txt", LineOfText', 'WRITEFILE "FileB.txt", LineOfText', 'CLOSEFILE "FileA.txt"', 'CLOSEFILE "FileB.txt"'], py: ['file_a = open("FileA.txt", "r")', 'file_b = open("FileB.txt", "w")', "line_of_text = file_a.readline()", "file_b.write(line_of_text)", "file_a.close()", "file_b.close()"] });

/* ---------- Lab 1 ---------- */
(() => {
  const ST = { disk: ["72", "58", "91"], mode: null, ptr: 0, score: "" }, el = $("#fd"), ss = $("#fs"), fm = $("#fm"), fv = $("#fv");
  const draw = () => { el.textContent = ST.disk.length ? ST.disk.map((l, i) => `${i + 1}  ${l}`).join("\n") : "(empty file)"; ss.innerHTML = `Mode: <b>${ST.mode || "closed"}</b>${ST.mode === "READ" ? ` · next line to read: <b>${ST.ptr + 1}</b>` : ""}`; fv.textContent = ST.score === "" ? "–" : ST.score; };
  const say = (t, bad) => (fm.innerHTML = (bad ? `<span class="flag">Error</span> ` : `<span class="okf">OK</span> `) + t);
  const act = { R() { if (ST.mode) return say("Close the file before opening it in another mode.", 1); ST.mode = "READ"; ST.ptr = 0; say("File opened for READ. The data is untouched."); },
    W() { if (ST.mode) return say("Close the file before opening it in another mode.", 1); ST.mode = "WRITE"; ST.disk = []; say("Opened for WRITE: a new file was created and the <b>old data was lost</b>."); },
    r() { if (!ST.mode) return say("The file is not open. Use OPENFILE first.", 1); if (ST.mode !== "READ") return say("You cannot READFILE: the file is open for WRITE.", 1); if (ST.ptr >= ST.disk.length) return say("There is no more data: you have reached the end of the file.", 1); ST.score = ST.disk[ST.ptr++]; say(`READFILE read line ${ST.ptr}: Score is now <b>${ST.score}</b>.`); },
    w() { if (!ST.mode) return say("The file is not open. Use OPENFILE first.", 1); if (ST.mode !== "WRITE") return say("You cannot WRITEFILE: the file is open for READ.", 1); const v = $("#fi").value.trim(); if (!v) return say("Type a value to write.", 1); ST.disk.push(v); say(`WRITEFILE added <b>${esc(v)}</b> to the file.`); },
    c() { if (!ST.mode) return say("The file is already closed.", 1); ST.mode = null; say("CLOSEFILE: the file is closed and saved."); },
    x() { ST.disk = ["72", "58", "91"]; ST.mode = null; ST.ptr = 0; ST.score = ""; say("The file has been reset to its original three scores."); } };
  $$("[data-f]").forEach((b) => (b.onclick = () => { act[b.dataset.f](); draw(); })); draw(); fm.textContent = "Press a button to begin.";
})();

/* ---------- Lab 2 ---------- */
chooser($("#sn"), $("#sv"), ["READ", "WRITE"], [
  ["Load the saved high scores when a game starts", "READ"], ["Save the new high score list at the end of the game", "WRITE"], ["Check whether a username exists in the users file", "READ"], ["Create a new empty log file for today", "WRITE"],
  ["Print every customer record from a file", "READ"], ["Replace the contents of the settings file with new settings", "WRITE"],
]);

/* ---------- Lab 3 ---------- */
chooser($("#sn2"), $("#sv2"), ["Not opened", "Not closed", "Wrong mode", "No error"], [
  ['<span class="ln2">READFILE "Data.txt", Item<br>OUTPUT Item</span>', "Not opened"],
  ['<span class="ln2">OPENFILE "Data.txt" FOR READ<br>READFILE "Data.txt", Item<br>OUTPUT Item</span>', "Not closed"],
  ['<span class="ln2">OPENFILE "Scores.txt" FOR WRITE<br>READFILE "Scores.txt", Score</span><br>The program should read saved scores', "Wrong mode"],
  ['<span class="ln2">OPENFILE "Log.txt" FOR WRITE<br>WRITEFILE "Log.txt", Message<br>CLOSEFILE "Log.txt"</span>', "No error"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each statement a reason for using a file or a problem with keeping data only in variables?", buckets: [{ label: "Reason for using a file" }, { label: "Problem with variables only" }], items: [
  { text: "Data is kept after the program ends", b: 0 },
  { text: "Data can be used again the next time", b: 0 },
  { text: "Data can be shared between programs", b: 0 },
  { text: "Large data can be read without typing", b: 0 },
  { text: "Variable values are lost when the program ends", b: 1 },
  { text: "The user must type the data in every time", b: 1 },
  { text: "Data stored in RAM is lost when the power is off", b: 1 },
], done: "Files keep data on secondary storage." });

Lib.classify($("#cl2"), { prompt: "Which mode does each statement need?", buckets: [{ label: "READ" }, { label: "WRITE" }], items: [
  { text: "Get the next line from the file", b: 0 },
  { text: "Load saved data at the start of a program", b: 0 },
  { text: "OPENFILE ... FOR READ", b: 0 },
  { text: "Old data in the file is lost", b: 1 },
  { text: "Save new data to the file", b: 1 },
  { text: "OPENFILE ... FOR WRITE", b: 1 },
], done: "Out of the file, or into it." });

Lib.match($("#m1"), { prompt: "Match each keyword to what it does.", pairs: [
  ["OPENFILE", "Opens a file in a stated mode"],
  ["READFILE", "Reads a data item or line from the file into a variable"],
  ["WRITEFILE", "Writes a value into the file"],
  ["CLOSEFILE", "Closes the file when it is no longer needed"],
  ["READ mode", "For reading data from the file"],
  ["WRITE mode", "Creates a new file; existing data is lost"]
] });

Lib.order($("#o1"), { prompt: "Put these lines in order to write 5 names to a file.", items: [
  "OPENFILE \"Names.txt\" FOR WRITE",
  "FOR Count ← 1 TO 5",
  "    INPUT Name",
  "    WRITEFILE \"Names.txt\", Name",
  "NEXT Count",
  "CLOSEFILE \"Names.txt\""
], done: "Open, loop, input, write, end loop, close." });

Lib.order($("#o2"), { prompt: "Put these lines in order to read 4 numbers from a file and output the total.", items: [
  "OPENFILE \"Nums.txt\" FOR READ",
  "Total ← 0",
  "FOR Count ← 1 TO 4",
  "    READFILE \"Nums.txt\", Number",
  "    Total ← Total + Number",
  "NEXT Count",
  "CLOSEFILE \"Nums.txt\"",
  "OUTPUT Total"
], done: "Open, total, loop reading and adding, close, output." });

Lib.calc($("#c1"), { qs: [
  { q: "A file holds the scores 72, 58 and 91. What is their total?", a: 221, sol: "72 + 58 + 91 = 221." },
  { q: "A loop reads one line each time from a file of 12 lines. How many times must the loop run to read the whole file?", a: 12, sol: "One READFILE per line: 12." },
  { q: "A program writes 3 names to an empty file. How many lines does the file hold?", a: 3, sol: "One line for each name: 3." },
  { q: "A file holds 5 lines. A program opens it FOR WRITE and writes 2 lines. How many lines does the file hold afterwards?", a: 2, sol: "WRITE mode erased the old data, so only the 2 new lines remain." },
  { q: "How many files are open in the program that copies a line from FileA.txt to FileB.txt (before closing)?", a: 2, sol: "FileA for READ and FileB for WRITE." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Why is data stored in a file?", opts: ["It is kept after the program ends", "It makes the program slower", "It uses less memory", "It needs no storage"], a: 0, why: "Files are permanent." },
  { q: "What does OPENFILE FOR WRITE do to existing data?", opts: ["Deletes it", "Adds to it", "Reads it", "Ignores the file"], a: 0, why: "A new file is created and existing data is lost." },
  { q: "Which command reads data from a file?", opts: ["READFILE", "WRITEFILE", "CLOSEFILE", "INPUT"], a: 0, why: "READFILE reads an item or line." },
  { q: "Why close a file?", opts: ["So data is saved and the file is freed", "To make it bigger", "To delete it", "To change its name"], a: 0, why: "Closing saves the data and frees the file." },
  { q: "How many modes can a file be open in at once?", opts: ["One", "Two", "Three", "As many as you like"], a: 0, why: "Only one mode at a time." },
  { q: "Which statement opens a file to read?", opts: ["OPENFILE \"A.txt\" FOR READ", "OPENFILE \"A.txt\" FOR WRITE", "READFILE \"A.txt\"", "CLOSEFILE \"A.txt\""], a: 0, why: "Mode READ." },
  { q: "A program reads before opening the file. What happens?", opts: ["An error: the file is not open", "It works", "The file is deleted", "The file is closed"], a: 0, why: "OPENFILE must come first." },
  { q: "Where is a file stored?", opts: ["Secondary storage", "Only in the CPU", "Only in the cache", "Only in the keyboard"], a: 0, why: "Files are kept on secondary storage." }
] });

Lib.cards($("#fc1"), { cards: [
  ["File", "A collection of data stored on secondary storage, kept after the program ends."],
  ["OPENFILE", "Opens a file in a stated mode (READ or WRITE)."],
  ["READFILE", "Reads a data item or line from an open file into a variable."],
  ["WRITEFILE", "Writes a value into an open file."],
  ["CLOSEFILE", "Closes a file when it is no longer needed."],
  ["READ mode", "The file is opened so data can be read from it."],
  ["WRITE mode", "The file is opened so data can be written; a new file is created and existing data is lost."],
  ["Persistent storage", "Data that is kept when a program ends or the power is switched off."]
] });
