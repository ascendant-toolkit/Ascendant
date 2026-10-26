"""AS CS 5.1.2: utility software and program libraries (including DLLs). Run: python3 tools/artifact-kit/mk_as512.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Utility software</b> is system software that performs housekeeping and maintenance tasks to keep the computer running well; examples are the <b>disk formatter</b>, <b>virus checker</b> (anti-malware), <b>defragmentation</b> software, <b>disk contents analysis</b>/<b>disk repair</b> software, <b>file compression</b> software and <b>back-up</b> software. A <b>program library</b> is a set of pre-written, pre-compiled and pre-tested routines that can be imported or called by other programs. Using library routines saves programming and testing time and gives access to complex routines; a drawback is that a routine may not match the needs exactly or may not work with the current program. A <b>Dynamic Link Library (DLL)</b> file is loaded into memory only when a program needs it, is shared by several programs and can be updated without recompiling the main program. Every exam answer pairs a utility or a library benefit with its reason.</p></div>

  <h2>1 · Utility software</h2>
  <div class="tw"><table class="t">
    <tr><th>Utility</th><th>Purpose</th><th>How it helps</th></tr>
    <tr><td><b>Disk formatter</b></td><td>Prepares a disk for first use: initialises it, sets up a file system (file allocation table, directory structure), creates partitions, a boot sector, a volume label, and checks the disk for errors; erases all data</td><td>A new disk cannot store files until it has been formatted</td></tr>
    <tr><td><b>Defragmentation</b></td><td>Rearranges the blocks of each file so that they are <b>contiguous</b>, and collects the free space together</td><td>Over time saving and deleting files splits them into fragments. Contiguous files need less head movement, so the files are accessed faster (a magnetic hard disk benefit)</td></tr>
    <tr><td><b>Virus checker</b> (anti-malware)</td><td>Scans for malicious program code and deletes or quarantines it</td><td>Protects data; can free memory taken by replicating malware</td></tr>
    <tr><td><b>Disk contents analysis / disk repair</b></td><td>Scans the disk for errors, marks bad sectors so they are not used, and corrects inconsistencies or restores corrupted files</td><td>Prevents data loss and improves reliability</td></tr>
    <tr><td><b>File compression</b></td><td>Reduces the size of files</td><td>Saves storage space and reduces transmission time and bandwidth</td></tr>
    <tr><td><b>Back-up</b></td><td>Makes copies of files at regular intervals, often automatically</td><td>If the data is lost or corrupted it can be restored</td></tr>
  </table></div>

  <h2>2 · Program libraries</h2>
  <p>A <b>program library</b> is a set of pre-written, pre-compiled (pre-tested) subroutines that can be called by other programs by installing or importing the library.</p>
  <div class="tw"><table class="t">
    <tr><th>Benefits</th><th>Drawbacks</th></tr>
    <tr><td>Saves development time because the code is already written; saves testing time because it is already tested and documented, so it is more likely to work; the programmer can use complex routines they could not write themselves; the source code is more readable (the routine is just called); team members can share and reuse routines</td><td>The routine may not be compatible with the current program; it may not be thoroughly tested; it may not match the needs exactly, so it must be edited and tested; if someone else changes the library, unexpected errors may appear</td></tr>
  </table></div>

  <h2>3 · Dynamic Link Libraries (DLLs)</h2>
  <ul>
    <li>The DLL is <b>separate</b> from the program and is <b>loaded into memory only when needed</b> (and only once), so the program uses less memory and its executable file is smaller.</li>
    <li>A single DLL file can be <b>shared by several programs</b>, which saves memory and disk space.</li>
    <li>The DLL can be <b>updated, fixed or improved independently</b>: the calling program does not need to be recompiled, and all programs that use the DLL get the update.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Saying defragmentation "makes the computer faster" with no reason. Say the file is contiguous, so there is less head movement.</li>
    <li>Describing a formatter as "deleting everything". It prepares a disk by creating a file system, partitions and a boot sector.</li>
    <li>Saying a library "contains code". It contains pre-written, pre-tested routines that are imported.</li>
    <li>Listing a DLL benefit that is really a library benefit. A DLL is separate, loaded when needed and updatable on its own.</li>
    <li>Giving a drawback with no consequence, such as "might have bugs". Add "so it needs to be tested".</li>
  </ul>
'''

watch = '''
  <h2>1 · Defragmentation</h2>
  <div id="stA"></div>
  <h2>2 · Formatting a new disk</h2>
  <div id="stB"></div>
  <h2>3 · Two programs share one DLL</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Defragment the disk</h2>
  <p>The blocks of files A, B and C are scattered. Press Defragment to make each file contiguous.</p>
  <div class="card"><div class="btnrow"><button id="df_go">Defragment</button><button id="df_reset">Reset</button></div><div id="dfG"></div><div id="dfV" class="verdict"></div></div>
  <h2>Lab 2 · Which utility?</h2>
  <div class="card"><div id="uB" class="btnrow"></div><div id="uO"></div></div>
  <h2>Lab 3 · Compression saving</h2>
  <div class="card"><div id="cS"></div><div id="cV" class="verdict"></div></div>
'''

_pr, _prjs = PR(["Which utility?", "Library or DLL?", "Match the utility to its purpose", "Put the formatting steps in order", "Working out", "Multiple choice"],
  ("Which utility does it describe?", ["Defragmentation", "Back-up", "Disk formatter", "Virus checker", "Compression"], [("Moves file parts so each file is contiguous", 0), ("Makes a copy in case the original is lost", 1), ("Sets up a new disk to store files", 2), ("Scans for malicious program code", 3), ("Decreases the file size", 4), ("Reduces head movement when reading files", 0)], "Match the purpose."),
  ("Is the point a general library point or specific to a DLL?", ["Program library", "DLL"], [("Pre-written and pre-tested routines", 0), ("Loaded into memory only when needed", 1), ("Saves time writing code from scratch", 0), ("Updated without recompiling the main program", 1), ("Shared by several programs at once", 1), ("Makes the source code easier to read", 0)], "DLL: separate, loaded when needed, shared, updatable."),
  [["Disk formatter", "Prepares a disk for use by setting up the file system"], ["Defragmentation", "Makes files contiguous"], ["Virus checker", "Scans for and removes malicious code"], ["Back-up", "Copies files in case the original is lost"], ["Disk repair", "Checks for and fixes inconsistencies on a disk"]],
  ("Put the steps of formatting a new disk in order.", ["The disk is checked for errors", "Partitions are created", "A file system (allocation table) is set up", "A boot sector and volume label are created", "The disk is ready to store files"], "Check, partition, file system, boot sector, ready."),
  [{"q": "A 24 MB file is compressed by 75%. How many MB is the compressed file?", "a": 6, "unit": "MB", "tol": 0.01, "hint": "25% of 24.", "sol": "<b>6</b> MB."}, {"q": "A 12 MB file is sent at 2 MB per second. How many seconds? Then compressed to a third of the size: how many seconds now? Give the saving in seconds.", "a": 4, "unit": "s", "tol": 0.01, "hint": "6 − 2.", "sol": "<b>4</b> s (6 s down to 2 s)."}, {"q": "A backup is made every 6 hours. How many backups in a week (7 days)?", "a": 28, "unit": "", "tol": 0.01, "hint": "4 per day × 7.", "sol": "<b>28</b>."}, {"q": "Three programs each load a 5 MB library. With a shared DLL loaded once, how many MB are saved?", "a": 10, "unit": "MB", "tol": 0.01, "hint": "15 − 5.", "sol": "<b>10</b> MB."}, {"q": "A file is stored in 6 fragments. After defragmentation it is stored in 1 contiguous block. How many fewer head movements to find the file's parts (assume one per fragment gap)?", "a": 5, "unit": "", "tol": 0.01, "hint": "6 − 1.", "sol": "<b>5</b>."}],
  [("Defragmentation improves performance by:", ["Making files contiguous, so less head movement", "Compressing files", "Deleting files", "Adding RAM"], 0, "Contiguous files."), ("A back-up is used to:", ["Restore lost data", "Scan for viruses", "Format a disk", "Speed up the CPU"], 0, "Restore."), ("A program library is:", ["Pre-written, pre-tested routines", "A building", "A text file", "A type of RAM"], 0, "Pre-written routines."), ("A DLL is:", ["Loaded only when needed", "Always in RAM", "A compiler", "A utility"], 0, "Loaded when needed."), ("A disk formatter:", ["Prepares a disk for use", "Defragments", "Repairs viruses", "Compiles"], 0, "Prepares."), ("A drawback of library routines:", ["May not match the needs exactly", "Take longer to write", "Are untested by definition", "Cannot be imported"], 0, "May not match.")],
  [("Utility software", "Housekeeping and maintenance tasks."), ("Disk formatter", "Initialises a disk; file system, partitions."), ("Defragmentation", "Contiguous files; less head movement."), ("Back-up", "Regular copies; restore if lost."), ("Compression", "Smaller files; less storage and time."), ("Virus checker", "Scans, deletes or quarantines malware."), ("Program library", "Pre-written, pre-tested routines."), ("DLL", "Loaded when needed; shared; updated alone.")])

real = RWNOTE + (
rw("A phone's automatic back-up", "Your photos are copied to cloud storage on a schedule so they are not lost if the phone breaks.", "back-up software.") +
rw("Sending photos by email", "Compressing a folder into a zip file makes it smaller so it uploads faster and fits under the attachment limit.", "file compression.") +
rw("Why old laptops slow down", "A hard disk fills with fragmented files; defragmenting puts the pieces together so the disk head moves less.", "defragmentation.") +
rw("Using maths functions in a program", "A programmer calls a ready-made routine to calculate a square root instead of writing it, because the routine is already tested.", "program library.") +
rw("A game update", "A game patch replaces one DLL file; the main program is not rebuilt, yet every part of the game gets the fix.", "DLLs can be updated independently.")
)

where = [
  ("M/J 2021", "11, 13", "2(a)", "4", "Match utility software to its description"),
  ("O/N 2021", "12", "7(c)", "4", "Two utility programs that improve performance and how"),
  ("M/J 2022", "13", "4(b)", "4 + 1", "The purpose of back-up and defragmentation software; another utility"),
  ("O/N 2022", "12", "1(a)", "5", "Match utility software to its purpose"),
  ("M/J 2023", "11", "3(c)", "3", "How defragmentation improves performance"),
  ("M/J 2023", "12", "7(a)", "2 + 4", "Define a program library; benefits of a DLL"),
  ("O/N 2022", "21", "1(a)", "3", "Three benefits of using library routines (Paper 2)"),
  ("O/N 2023", "12", "8(b)", "3", "A utility that is not for security and why it is needed"),
  ("O/N 2023", "13", "5(b)", "2 + 3", "Why compress program files; why a new disk needs a formatter"),
  ("M/J 2024", "13", "7(e)", "1 + 4", "What a program library is; the benefits of DLL files"),
  ("O/N 2024", "11", "4(a)(ii), (c)", "2 + 3", "The need for back-up software; the benefits of library files"),
  ("O/N 2024", "12", "4(b)", "3", "The benefits of creating a program library"),
  ("O/N 2025", "11", "5(b)", "2 + 2", "A benefit and a drawback of library routines"),
  ("O/N 2025", "13", "8(b)", "3", "How a programmer benefits from program libraries"),
  ("M/J 2026", "12", "7(a)(iii)", "3", "Why defragmentation improves performance"),
  ("M/J 2026", "13", "5(b), (c)", "1 + 2 + 1 + 2", "The purpose of utility software and of a disk formatter; a program library and a DLL benefit")]

past = '''  <p class="note">Utility software appears in Paper 1 every series, most often defragmentation and back-up, and the library and DLL questions follow the same pattern: a benefit plus its reason. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q2(a)"), "4 marks", "Match",
  "Draw one line from each utility software to its correct description. Utilities: disk formatter, defragmentation, back-up, disk repair. Descriptions: scans software for errors and repairs the problems; moves parts of files so that each file is contiguous in memory; creates a copy of data that is no longer required; sets up a disk so it is ready to store files; scans for errors in a disk and corrects them; creates a copy of data in case the original is lost.", "Some descriptions are distractors.",
  "<p>" + mks(["Disk formatter: sets up a disk so it is ready to store files", "Defragmentation: moves parts of files so that each file is contiguous", "Back-up: creates a copy of data in case the original is lost", "Disk repair: scans for errors in a disk and corrects them"]) + "</p>", None) + peq(SRC("w21", "12", "Q7(c)"), "4 marks", "Identify / State",
  "Identify two utility programs that can be used to improve the performance of a computer and state how they improve the performance.", "Defragmentation and virus checker; disk clean-up.",
  "<p>One mark for the program and one for the description, for each of two: " + mks(["Defragmentation: less time is taken to access files because each one is contiguous, so there is less head movement", "Virus checker: makes more RAM available for programs to run, because it removes software that might be taking up memory or replicating", "Disk repair or disk contents analysis: prevents bad sectors being used because it identifies and marks them", "Disk or system clean-up: releases storage by removing unwanted or temporary files"]) + "</p>", "Naming a utility with no effect on performance.") + peq(SRC("s22", "13", "Q4(b)"), "4 + 1 marks", "Describe / Give",
  "(i) Describe the purpose of back-up software and defragmentation software. (ii) Give one other example of utility software.", "Back-up: copy at intervals so it can be retrieved. Defrag: contiguous, faster access.",
  "<p><b>(i)</b> " + mks(["Back-up: to make a copy of data at regular intervals", "so that if it is lost or corrupted it can be retrieved", "Defragmentation: makes individual files occupy contiguous blocks (or moves the free space together)", "to improve disk access times, so data and files load faster"]) + "</p><p><b>(ii)</b> " + mks(["Compression software, hard disk formatter, virus checker, disk analysis or disk repair software"], "a") + "</p>", None) + peq(SRC("w22", "12", "Q1(a)"), "5 marks", "Match",
  "Draw one line from each utility software to its most appropriate purpose. Utilities: virus checker, disk formatter, backup, disk repair, defragmentation. Purposes: to reorganise files so they are contiguous; to scan for malicious program code; to decrease the file size; to initialise a disk; to create copies of files in case the original is lost; to check for and fix inconsistencies on a disk.", "Five lines; one purpose is for compression, not in the list.",
  "<p>" + mks(["Virus checker: to scan for malicious program code", "Disk formatter: to initialise a disk", "Backup: to create copies of files in case the original is lost", "Disk repair: to check for and fix inconsistencies on a disk", "Defragmentation: to reorganise files so they are contiguous"]) + "</p>", None) + peq(SRC("s23", "11", "Q3(c)"), "3 marks", "Explain",
  "The Operating System has utility software including defragmentation software. Explain how defragmentation can improve the performance of the computer.", "Contiguous; faster access; less head movement.",
  "<p>Any three: " + mks(["Rearranges the blocks of individual files so they are contiguous (moves the free space together)", "Accessing each file is faster", "because there is no need to search for the next fragment or block of the file", "so less head movement is needed"]) + "</p>", None) + peq(SRC("s23", "12", "Q7(a)"), "2 + 4 marks", "Define / Explain",
  "(i) Define the term program library. (ii) Explain two benefits to the developer of choosing to create a Dynamic Link Library (DLL).", "Pre-written subroutines called by other programs. Memory, file size, maintenance, recompile, sharing.",
  "<p><b>(i)</b> Any two: " + mks(["A set of pre-written, pre-compiled or pre-tested subroutines", "which can be called in other programs", "by installing or importing the library"]) + "</p><p><b>(ii)</b> Two benefits, each with an expansion: " + mks(["The main memory requirement of the program is reduced, as the DLL is loaded only once or when required", "The executable file of the program is smaller, because it does not contain all the library routines", "Maintenance does not need to be done by the programmer, because the DLL is separate from the program", "There is no need to recompile the main program when the DLL is changed", "A single DLL file can be made available to several application programs, saving space in memory"], "a") + "</p>", "Giving a general library benefit (saves time) when the question asks about a DLL.") + peq(SRC("w22", "21", "Q1(a)"), "3 marks", "State",
  "An algorithm includes a number of complex calculations. A programmer decides to use library routines to provide part of the solution. State three possible benefits of using library routines in the development of the program.", "Tested, complex functions, faster development.",
  "<p>" + mks(["They are tried and tested, so free from errors", "They perform a function that the programmer may not be able to program themselves (for example encryption)", "They are readily available, which speeds up development time"]) + "</p>", None) + peq(SRC("w23", "12", "Q8(b)"), "3 marks", "Identify / Explain",
  "The purpose of some utility software is to improve security. Identify one example of utility software that is not intended to improve security. Explain why this software is needed.", "Defragmentation, disk repair, compression or formatter, with a reason.",
  "<p>One mark for the name and two for the explanation: " + mks(["Defragmentation: over time saving and deleting small files fragments the disk; the software makes the files contiguous, so access time is improved because head movement is reduced", "Disk repair: to identify and mark bad sectors; to restore corrupted files", "File compression: to reduce the size of files, which saves storage and memory space and reduces transmission time", "Disk formatter: to prepare a disk for use; to set up the file system; to partition the disc"]) + "</p>", None) + peq(SRC("w23", "13", "Q5(b)"), "2 + 3 marks", "Explain / Describe",
  "Program files are downloaded from a web server and stored on a new hard disk. (i) Explain the reasons for compressing the files. (ii) Describe the reasons why a hard disk formatter is needed for the new hard disk.", "Time and space. Prepare, check, file system, allocation table.",
  "<p><b>(i)</b> Any two: " + mks(["To reduce the time it takes to download the files from the web server", "To reduce the amount of storage space used on the web server or the user's device"]) + "</p><p><b>(ii)</b> Any three: " + mks(["The disk needs to be prepared for initial use", "The disk needs to be checked for errors", "A new file system needs to be generated on the disk", "The file allocation table needs to be set up"], "a") + "</p>", None) + peq(SRC("s24", "13", "Q7(e)"), "1 + 4 marks", "State / Describe",
  "(i) State what is meant by a program library. (ii) Some program libraries include DLL files. Describe the benefits of a programmer using a library with DLL files instead of a library that does not include DLL files.", "Pre-written code imported; DLL separate and updated independently.",
  "<p><b>(i)</b> " + mks(["Pre-written code, functions or routines that can be imported or called in another program"]) + "</p><p><b>(ii)</b> Any four: " + mks(["Maintenance does not need to be done by the programmer, because the DLL is separate from the program", "The calling program does not need recompilation when a DLL file changes", "because the DLL file can be updated independently of the calling program", "Updates will apply to all programs that use the DLL file"], "a") + "</p>", None) + peq(SRC("w24", "11", "Q4(a)(ii), (c)"), "2 + 3 marks", "Explain",
  "(a)(ii) Explain the need for back-up software. (c) The student used a program library when writing their program. Explain the benefits to the student of using library files.", "Restore data; automatic copies. Saves time, tested, more robust, skills.",
  "<p><b>(a)(ii)</b> Any two: " + mks(["To allow data to be retrieved or restored when lost", "To automatically make a duplicate copy of data, so the user does not have to remember to back up", "To make regular duplicate copies of data"]) + "</p><p><b>(c)</b> Any three: " + mks(["It saves development time by using pre-written code", "There is less testing to do because the routines have already been tested and are more likely to work correctly", "It results in a more robust program", "Subroutines can be used that they do not have the skill to write, which enables a more complex program to be written"], "a") + "</p>", None) + peq(SRC("w24", "12", "Q4(b)"), "3 marks", "Describe",
  "The programmers created a new program library whilst developing the program. Describe the benefits to the programmers of creating a program library.", "Shared, reused, no rewriting or re-testing; specialisms.",
  "<p>Any three: " + mks(["Subroutines can be shared and reused between team members who are working independently", "without having to rewrite or re-test them, which saves the programmers' time", "A program library provides continuity between programs and programmers", "Individual programmers can contribute their specialisms to the library, or use the specialisms of others"]) + "</p>", None) + peq(SRC("w25", "11", "Q5(b)"), "2 + 2 marks", "Describe",
  "(i) Describe one benefit of using library routines when developing software. (ii) Describe one drawback.", "Benefit with expansion; drawback with expansion.",
  "<p><b>(i)</b> " + mks(["Less code needs to be developed as code is pre-written, reducing the time to write a program", "The routine is pre-tested and documented, reducing the testing time and giving confidence that it works", "The code can be written in a different language, allowing use of its special features", "The source code is more readable as the routine is simply called", "The library could contain complex routines the programmer might not be able to code"]) + " (one benefit and its expansion)</p><p><b>(ii)</b> " + mks(["Compatibility issues: the routine may not work with the current program", "Not guaranteed to be thoroughly tested: there could be unexpected problems", "The routine may not match the needs exactly, so it will need to be edited and tested", "If the routine is later changed by someone else there could be unexpected errors"], "a") + " (one drawback and its expansion)</p>", None) + peq(SRC("w25", "13", "Q8(b)"), "3 marks", "Explain",
  "Explain how a programmer benefits from using program libraries during program development.", "Time saved, tested, updates, complex routines.",
  "<p>Any three: " + mks(["Programming time is saved as code does not have to be written from scratch", "Testing time is saved as the code is already tested and documented", "A library routine is more likely to work, as the code is already tested", "Library routines automatically update if they are changed or improved", "The programmer can use routines for complex functions they may not be able to write themselves"]) + "</p>", None) + peq(SRC("s26", "12", "Q7(a)(iii)"), "3 marks", "Explain",
  "Explain the reasons why defragmentation software improves the performance of a computer.", "Files split over time; contiguous; head moves less; faster access.",
  "<p>Any three: " + mks(["With continued use files can be split and stored in different locations on the disk, so time is spent by the disk head moving between locations", "Defragmentation moves split files into contiguous blocks, or collects the free space into a contiguous block", "which means the disk head does not need to move as much", "After defragmentation data access, read and write take less time"]) + "</p>", "Describing the process only. The question asks how it improves performance.") + peq(SRC("s26", "13", "Q5(b)(c)"), "1 + 2 + 1 + 2 marks", "State / Describe / Define",
  "(b)(i) State the purpose of utility software in a computer. (ii) Describe the purpose of a disk formatter. (c)(i) Define the term program library. (ii) Describe a benefit of a library with DLL files (benefit and expansion).", "Housekeeping; prepare a disk; pre-written routines; DLL separate.",
  "<p><b>(b)(i)</b> " + mks(["To perform housekeeping or maintenance tasks, or to improve overall performance"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Prepares a disk for future use by initialising it", "changing or setting the file system, directory structure or allocation tables", "naming the disk (volume label)", "creating a boot sector", "erasing all data", "creating partitions"], "a") + "</p><p><b>(c)(i)</b> " + mks(["A set of pre-written, pre-compiled or pre-tested routines"], "b") + "</p><p><b>(ii)</b> " + mks(["Maintenance does not need to be done by the programmer, because the DLL is separate and updated independently"], "c") + "</p>", None)

review = req("2 marks", "Explain", "Explain why a user would run defragmentation software on a magnetic hard disk but not on an SSD.", "Moving parts.", "<p>" + mks(["A magnetic disk has a read/write head that moves, so contiguous files reduce head movement", "An SSD has no moving parts, so fragmentation does not slow it"]) + "</p>", None) + req("2 marks", "Describe", "Describe how back-up software protects a school's data.", "Copies, restore.", "<p>" + mks(["It makes copies of the data at regular intervals", "so that if the data is lost or corrupted it can be restored"]) + "</p>", None) + req("2 marks", "State", "State two benefits of file compression when emailing a large file.", "Time, space.", "<p>" + mks(["The file takes less time to send", "It uses less storage space or bandwidth"]) + "</p>", None) + req("3 marks", "Explain", "Explain why a game that uses a DLL can be patched without reinstalling the whole game.", "Separate, independent update.", "<p>" + mks(["The DLL is a separate file from the main program", "so it can be replaced or updated independently", "and the main program does not need to be recompiled"]) + "</p>", None) + req("2 marks", "Describe", "Describe one drawback of using a library routine.", "Not matching needs.", "<p>" + mks(["The routine may not match the needs exactly", "so it will need to be edited and tested, or may give unexpected results"]) + "</p>", None)

tips = tips_html([
  ("Utility plus reason.", "Defrag: contiguous, less head movement."),
  ("Formatter: prepare, file system, partitions.", "It also erases data."),
  ("Library: pre-written and pre-tested.", "Time saved on writing and on testing."),
  ("DLL: separate, loaded when needed, shared.", "Updated without recompiling."),
  ("Drawbacks need a consequence.", "Not matching needs, so it must be edited."),
  ("Describe means more than name.", "Always give what it does."),
], [("utility software", "System software that does housekeeping and maintenance."), ("defragmentation", "Making each file occupy contiguous blocks."), ("a program library", "Pre-written, pre-tested routines for other programs."), ("a DLL", "A library file loaded only when needed and shared.")],
  [("Identify", "Name it."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Match", "Link each utility to its purpose.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const scattered = "ABACBCAB".split(""), tidy = "AAABBBCC".split(""), arr = k >= 2 ? tidy : scattered; const col = { A: "f1", B: "f2", C: "f3" }; let o = ""; arr.forEach((c, i) => { o += SV.rect(30 + i * 60, 40, 54, 40, col[c], { rx: 4 }) + SV.text(57 + i * 60, 65, c, "lbl bd", { "text-anchor": "middle" }); });
    o += SV.text(30, 110, ["Files A, B and C are split into fragments around the disk", "To read file A the head must jump between three separate places", "Defragmentation moves the fragments so each file is contiguous", "Now each file is read in one go: less head movement"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 130, label: "Defragmentation", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["After a lot of saving and deleting, files are fragmented.", "Reading file A means moving the read/write head to three places.", "<b>Defragmentation</b> makes each file contiguous.", "Access is faster because there is less head movement."][i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const items = ["check for errors", "partitions", "file system", "boot sector", "ready"]; let o = ""; items.forEach((t, i) => { o += SV.rect(20 + i * 108, 40, 100, 44, i <= k ? "f1" : "cell", { rx: 6 }) + SV.text(70 + i * 108, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); }); return o; };
  Lib.stepper($("#stB"), { w: 560, h: 110, label: "Formatting", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["The formatter checks the new disk for errors.", "It creates partitions.", "It sets up the file system and allocation table.", "It writes a boot sector and a volume label.", "The disk is now ready to store files."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 120, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 60, y + 25, t, "lbl bd", { "text-anchor": "middle", style: "font-size:13px" }); let o = B(20, 20, "Program 1", k >= 1) + B(20, 80, "Program 2", k >= 2) + B(300, 50, "graphics.dll", k >= 1);
    if (k >= 1) o += SV.path("M140,40 H300", "ax"); if (k >= 2) o += SV.path("M140,100 L300,80", "ax"); o += SV.text(20, 150, ["", "Program 1 needs the DLL: it is loaded into memory", "Program 2 uses the same copy: loaded only once", "The DLL is updated: both programs benefit with no recompile"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 170, label: "DLL", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: [0, 1, 2, 3].map((i) => ({ cap: ["A DLL is a library file kept separate from programs.", "Program 1 needs it, so it is <b>loaded when needed</b>.", "Program 2 <b>shares</b> the same copy in memory.", "An update to the DLL applies to every program that uses it, with no recompile."][i], s: { i } })) });
})();

(function () {
  const colors = ["f1", "f2", "f3"]; const init = "ABACBCAB".split(""); let arr, done;
  const reset = () => { arr = init.slice(); done = false; paint(); };
  const paint = () => { let o = '<svg viewBox="0 0 500 70" style="width:500px;max-width:100%;display:block">'; arr.forEach((c, i) => { o += `<rect x="${10 + i * 60}" y="10" width="54" height="40" rx="4" class="${colors[c.charCodeAt(0) - 65]}"/><text x="${37 + i * 60}" y="35" text-anchor="middle" class="lbl bd">${c}</text>`; }); $("#dfG").innerHTML = o + "</svg>";
    const jumps = (f) => { let n = 0; for (let i = 1; i < arr.length; i++) if (arr[i] === f && arr[i - 1] !== f) n++; return n + (arr[0] === f ? 1 : 0); };
    $("#dfV").innerHTML = `Starts of separate fragments: file A <b>${jumps("A")}</b>, B <b>${jumps("B")}</b>, C <b>${jumps("C")}</b>.` + (done ? " After defragmentation each file is in one contiguous run, so the head moves less." : " Press Defragment."); };
  $("#df_go").onclick = () => { arr = arr.slice().sort(); done = true; paint(); }; $("#df_reset").onclick = reset; reset();
})();
btnTable("uB", "uO", [
  ["A new USB drive that Windows cannot use yet", "Disk formatter", "Sets up the file system"],
  ["A disk that takes a long time to open files", "Defragmentation", "Makes files contiguous"],
  ["Copy homework to a cloud drive every night", "Back-up software", "Restore if lost"],
  ["Remove a trojan from a laptop", "Virus checker", "Deletes or quarantines malware"],
  ["Fit a big folder in an email attachment limit", "File compression", "Smaller file"],
  ["A disk with unreadable areas", "Disk repair", "Marks bad sectors"]
], ["Situation", "Utility", "Why"]);
(function () {
  let mb = 48, pct = 60; const paint = () => { const c = mb * (1 - pct / 100); $("#cV").innerHTML = `A <b>${mb} MB</b> file compressed by <b>${pct}%</b> becomes <b>${c.toFixed(1)} MB</b>. At 4 MB per second it uploads in <b>${(c / 4).toFixed(1)} s</b> instead of <b>${(mb / 4).toFixed(1)} s</b>: it saves storage space and transmission time.`; };
  Lib.slider($("#cS").appendChild(document.createElement("div")), { id: "c1", label: "File size (MB) ", min: 4, max: 200, value: mb, fmt: (x) => x, onInput: (v) => { mb = v; paint(); } });
  Lib.slider($("#cS").appendChild(document.createElement("div")), { id: "c2", label: "Compression ", min: 0, max: 95, value: pct, fmt: (x) => x + "%", onInput: (v) => { pct = v; paint(); } }); paint();
})();
''' + _prjs

finish("as-5-1-2-utility-software-libraries", "as512", "Utility Software and Program Libraries",
  "Disk formatters, defragmentation, virus checkers, back-up and compression, and program libraries and DLLs with their benefits and drawbacks, with animations, a defragmentation lab and the real Paper 1 questions from 2021 to 2026.",
  "5.1.2", "5 · System software", "section 5.1 Operating systems", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on utility software and program libraries (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
