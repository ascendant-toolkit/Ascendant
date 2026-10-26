"""A Level CS syllabus 16.2.1: interpreters and the stages of compilation. Run: python3 tools/artifact-kit/mk_ac1621.py"""
from ak16 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Programs written in a high-level language have to be translated before the processor can run them. An <b>interpreter</b> translates and executes the source code <b>one statement at a time</b>, never producing a translated copy of the whole program; if it finds an error it reports it and stops, and it must translate every statement again each time the program runs, including every pass round a loop. A <b>compiler</b> translates the whole program into object code in one go, in four stages: <b>lexical analysis</b> (source code to tokens), <b>syntax analysis</b> (tokens checked against the grammar to give a parse tree), <b>code generation</b> (the parse tree to executable code) and <b>optimisation</b> (making the code use fewer resources). The executable can then be run as often as needed without the source code or the translator.</p></div>

  <h2>1 · Interpreter</h2>
  <p>An interpreter executes a program <b>without producing a translated version</b> of it.</p>
  <ol>
    <li>It takes the next statement of the source code and <b>translates</b> it.</li>
    <li>It <b>checks the statement for errors</b>.</li>
    <li>If there is no error the statement is <b>executed</b> at once.</li>
    <li>If an error is found it is <b>reported and the interpreter halts</b>.</li>
    <li>It carries on to the next statement.</li>
  </ol>
  <p>Nothing is stored in executable form, so the translation is <b>repeated every time the program is run</b>, and repeated for each pass through a loop. Interpreters are good for <b>developing and testing</b> (an error is found as soon as that statement is reached, so the programmer can fix and re-run at once) but run more slowly than compiled code.</p>
  <div class="tw"><table class="t">
    <tr><th></th><th>Interpreter</th><th>Compiler</th></tr>
    <tr><td><b>Translates</b></td><td>One statement at a time</td><td>The whole program</td></tr>
    <tr><td><b>Output</b></td><td>No executable file; statements are executed directly</td><td>An executable (object code) file</td></tr>
    <tr><td><b>Errors</b></td><td>Reported when that statement is reached; execution stops</td><td>All errors reported after the analysis stages; nothing runs until they are fixed</td></tr>
    <tr><td><b>Running again</b></td><td>Translated again every time</td><td>Runs the stored executable with no further translation</td></tr>
    <tr><td><b>Speed</b></td><td>Slower, especially in loops</td><td>Faster</td></tr>
    <tr><td><b>Source needed</b></td><td>Yes, every time it runs</td><td>No; the executable can be distributed</td></tr>
  </table></div>

  <h2>2 · The stages of compilation</h2>
  <h3>Lexical analysis</h3>
  <p>The <b>first stage</b>. The source code is read and <b>white space and comments are removed</b>. The rest is broken into a series of <b>tokens</b>: keywords, identifiers, operators, constants and punctuation. Each token is <b>categorised</b> and assigned a type. <b>Identifiers</b> (variable and subroutine names) are stored in a <b>symbol table</b>. If the lexical analyser finds an <b>invalid token</b> it generates an error; acceptable output passes to the syntax analyser.</p>
  <p>The line ''' + bx("Total = Price * 2 + 5") + ''' becomes the tokens <b>Total</b> (identifier), <b>=</b> (operator), <b>Price</b> (identifier), <b>*</b>, <b>2</b> (constant), <b>+</b>, <b>5</b> (constant).</p>
  <h3>Syntax analysis</h3>
  <p>The <b>second stage</b>. The <b>token stream</b> from the lexical analyser is analysed (<b>parsed</b>) against the <b>grammar</b> of the language to detect errors: do the tokens conform to the rules of the language? <b>Syntax errors are reported.</b> The output is a <b>parse tree</b> (an abstract syntax tree), which shows the structure of the code, for example that in <span class="bx">a + 2 * c</span> the multiplication is done before the addition.</p>
  <h3>Code generation</h3>
  <p>The <b>parse tree</b> (or an intermediate representation) is converted into <b>executable code</b>: machine code or assembly for the target processor.</p>
  <h3>Optimisation</h3>
  <p>The code is improved so that it uses <b>minimum resources</b>: it identifies and removes <b>redundant code</b>, simplifies expressions and may reorder the code, so that <b>storage size, memory use, power consumption, CPU time or execution time</b> are minimised. For example, 2 * 60 * 60 can be worked out once during compilation as 7200, and an instruction whose result is never used can be deleted.</p>
  <div class="tw"><table class="t">
    <tr><th>Stage</th><th>Input</th><th>Output</th><th>Errors found</th></tr>
    <tr><td>Lexical analysis</td><td>Source code</td><td>Tokens and a symbol table</td><td>Invalid tokens</td></tr>
    <tr><td>Syntax analysis</td><td>Tokens</td><td>Parse tree</td><td>Syntax errors</td></tr>
    <tr><td>Code generation</td><td>Parse tree</td><td>Executable code</td><td></td></tr>
    <tr><td>Optimisation</td><td>Executable code</td><td>Improved executable code</td><td></td></tr>
  </table></div>

  <h2>3 · Common ways to lose marks</h2>
  <ul>
    <li>Describing a compiler when the question asks about an interpreter. An interpreter produces no translated version.</li>
    <li>Leaving out "one statement at a time", "checked for errors before execution" or "translated again every time".</li>
    <li>Putting the stages in the wrong order: lexical, syntax, code generation, optimisation.</li>
    <li>Writing that lexical analysis checks the grammar. That is syntax analysis; lexical analysis makes tokens and removes white space and comments.</li>
    <li>Writing that optimisation makes the program "better" or "faster" only. It uses fewer resources: storage, memory, CPU time.</li>
  </ul>
'''

watch = '''
  <h2>1 · Lexical analysis: source code to tokens</h2>
  <p>Press Play. Spaces and the comment are dropped; each piece becomes a token with a type.</p>
  <div id="stA"></div>
  <h2>2 · Syntax analysis: building the parse tree</h2>
  <div id="stB"></div>
  <h2>3 · Interpreter and compiler on a loop</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Tokeniser</h2>
  <p>Type a line of code. The lexical analyser removes the white space and any comment (after #) and lists the tokens.</p>
  <div class="card"><input id="lxI" type="text" value="Total = Price * 2 + 5  # add tax" style="width:100%;font:inherit;padding:8px"><div id="lxO"></div></div>

  <h2>Lab 2 · Optimisation</h2>
  <div class="card"><div id="opB" class="btnrow"></div><div id="opO"></div></div>

  <h2>Lab 3 · Translating a loop</h2>
  <p>A program has 5 lines and one of them is in a loop that runs several times. Count how many statements are translated.</p>
  <div class="card"><div id="lpS"></div><div id="lpO"></div></div>
'''

practise = '''
  <h2>1 · Which stage of compilation?</h2><div id="cl1" class="card"></div>
  <h2>2 · Interpreter or compiler?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the stage to its description</h2><div id="m1" class="card"></div>
  <h2>4 · Put the stages of compilation in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Python in a notebook", "Python normally runs through an interpreter: you type a line, it runs at once, and an error appears when that line is reached. This makes it good for trying things out.", "an interpreter executes statement by statement.") +
rw("A game you install", "The game is distributed as an executable. The developer compiled it once, so you do not need the source code and the game starts without any translation.", "a compiler produces an executable.") +
rw("The red wavy line in a code editor", "The editor runs a quick lexical and syntax check as you type and marks tokens or structures that break the rules of the language.", "lexical and syntax analysis report errors.") +
rw("A compiler making your program smaller", "When you turn on optimisation the compiler removes code that does nothing and works out constant calculations in advance, so the program uses less memory and time.", "optimisation uses minimum resources.") +
rw("A web page's JavaScript", "The browser interprets (or compiles just in time) the script each time the page loads, because the source is delivered as text.", "interpreted code is translated every time it runs.")
)

where = [
  ("M/J 2021", "31, 32, 33", "3(b)", "4", "Explain how an interpreter executes a program without producing a complete translated version"),
  ("O/N 2022", "31, 33", "4", "4", "Connect four stages of compilation to descriptions"),
  ("O/N 2022", "32", "2", "2 + 2", "Identify two other stages of compilation; the purpose of syntax analysis"),
  ("M/J 2025", "31", "6", "4", "Describe the process of executing a program using an interpreter"),
  ("M/J 2025", "32", "8", "4", "Explain what is meant by lexical analysis"),
  ("M/J 2025", "33", "8", "4", "Explain the process of syntax analysis"),
  ("O/N 2025", "31", "8(a)", "2", "Purpose of lexical analysis"),
  ("O/N 2025", "32", "8(a)", "1", "Purpose of the optimisation stage"),
  ("O/N 2025", "33", "7(a)", "2", "Outline the process of optimisation")]

past = '''  <p class="note">Translation questions appear in Paper 3 nearly every series. In 2025 each stage of compilation was asked in a different paper; the interpreter has been asked in 2021 and 2025. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "31/32/33", "Q3(b)"), "4 marks", "Explain",
  "Explain how an interpreter executes a program without producing a complete translated version of it.",
  "One statement at a time: examine, check, execute, repeat for each loop and each run.",
  "<p>Any four: " + mks(["An interpreter examines the source code one statement at a time", "It checks each statement for errors", "If no error is found the statement is executed", "If an error is found it is reported and the interpreter halts", "Interpretation is repeated for every iteration in repeated sections of code (loops)", "Interpretation has to be repeated every time the program is run"]) + "</p>", "Describing the output as 'machine code'. An interpreter does not produce a translated version of the program at all.") + peq(SRC("s25", "31", "Q6"), "4 marks", "Describe",
  "Describe the process of executing a program using an interpreter.",
  "Line by line, no executable stored, errors halt it, repeated every time.",
  "<p>Any four: " + mks(["The interpreter translates the source code one line at a time", "If the line is free of syntax errors it is executed", "It is not stored in executable format", "If an error is found, the program halts with an error message", "Each line must be translated every time it is run, including lines run many times, for example in loops"]) + "</p>", None) + peq(SRC("w22", "31/33", "Q4"), "4 marks", "Match",
  "Draw one line to connect each stage of compilation to its most appropriate description. Stages: lexical analysis; syntax analysis; code generation; optimisation. Descriptions: (A) minimising a program's execution time and memory requirement; (B) converting an intermediate representation of source code into an executable form; (C) converting a sequence of characters into a sequence of tokens; (D) directly executing instructions written in a scripting language; (E) using parsing algorithms to interpret the meaning of a sequence of tokens.",
  "One description is a distractor.",
  "<p>" + mks(["Lexical analysis → C", "Syntax analysis → E", "Code generation → B", "Optimisation → A"]) + "</p><p>Description D is the distractor: it describes an interpreter.</p>", "Joining syntax analysis to 'converting characters to tokens'. That is lexical analysis; syntax analysis checks the tokens against the grammar.") + peq(SRC("w22", "32", "Q2"), "2 + 2 marks", "Identify / Outline",
  "Lexical analysis and syntax analysis are stages in the compilation of a program. (a) Identify two other stages that take place during the compilation of a program. (b) Outline the purpose of syntax analysis.",
  "Code generation and optimisation.",
  "<p><b>(a)</b> " + mks(["Code generation", "Optimisation"]) + "</p><p><b>(b)</b> Any two: " + mks(["It checks that the code matches the grammar of the language (the tokens conform to the rules of the programming language)", "Syntax errors are reported", "A parse tree is produced"]) + "</p>", None) + peq(SRC("s25", "32", "Q8"), "4 marks", "Explain",
  "Explain what is meant by lexical analysis during program compilation.",
  "First stage; remove white space and comments; tokens; symbol table.",
  "<p>Any four: " + mks(["It is the first stage of compilation", "White space and comments are removed", "It takes the modified source code and breaks it into a series of tokens", "Each token is categorised and assigned a type", "Identifiers are stored in a symbol table", "If the lexical analyser finds invalid tokens it generates an error", "Acceptable data from the lexical analyser passes to the syntax analyser"]) + "</p>", None) + peq(SRC("w25", "31", "Q8(a)"), "2 marks", "Outline",
  "Outline the purpose of lexical analysis during the compilation of a program.",
  "Tokens, parser, symbol table, remove white space.",
  "<p>Any two: " + mks(["To convert the high-level source code into a sequence of tokens", "that can be sent to the parser for syntax analysis", "To create a symbol table", "To remove the unnecessary white space and comments from the code"]) + "</p>", None) + peq(SRC("s25", "33", "Q8"), "4 marks", "Explain",
  "Explain the process of syntax analysis during program compilation.",
  "Second stage; takes tokens; parse against the rules; parse tree; errors reported.",
  "<p>Any four: " + mks(["It is the second stage of compilation, after lexical analysis", "It takes input from the lexical analyser in the form of token streams", "The source code is analysed (parsed) against the rules of the language to detect any errors in the code", "The output from this phase is a parse tree", "Syntax errors are reported"]) + "</p>", None) + peq(SRC("w25", "32", "Q8(a)"), "1 mark", "State",
  "State the purpose of the optimisation stage in the compilation of a program.",
  "Minimum resources.",
  "<p>" + mks(["To improve the code by making it use minimum resources (CPU, memory or storage, time): minimising program storage, CPU time, memory use or program execution time"]) + "</p>", None) + peq(SRC("w25", "33", "Q7(a)"), "2 marks", "Outline",
  "Outline the process of optimisation during the compilation of a program.",
  "Identify and remove redundant code, then the benefit.",
  "<p>" + mks(["To identify and remove redundant code, to simplify expressions, or to reorder the code", "so that storage size, memory use, power consumption, program execution time or CPU time is minimised"]) + "</p>", None)

review = req("3 marks", "Describe", "Give three reasons why a programmer may use an interpreter while developing a program but a compiler for the finished program.", "Errors, repetition, speed.", "<p>" + mks(["An interpreter stops at an error, so the programmer can fix it and re-run straight away", "No whole-program translation is needed before each test", "The compiled version runs faster and can be distributed without the source code"]) + "</p>", None) + req("3 marks", "State", "The statement Count = Count + 1  # add one is lexically analysed. State the tokens produced and what happens to the comment.", "The comment is not a token.", "<p>" + mks(["Tokens: Count (identifier), =, Count (identifier), +, 1 (constant)", "The comment is removed", "The identifier Count is stored in the symbol table"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a compiler can report syntax errors before the program runs but an interpreter may not.", "When does each check?", "<p>" + mks(["A compiler analyses the whole program before producing any executable code", "An interpreter only checks a statement when it reaches it, so errors later in the program are not found until then"]) + "</p>", None) + req("2 marks", "Identify", "A compiler replaces 3 * 60 * 60 with 10800. Name the stage and state its purpose.", "Reducing the work at run time.", "<p>" + mks(["Optimisation", "The calculation is done once at compile time, so the program uses less CPU time when it runs"]) + "</p>", None) + req("3 marks", "Explain", "Explain what a parse tree shows.", "Structure.", "<p>" + mks(["It is produced by syntax analysis from the tokens", "It shows how the tokens are grouped by the rules of the language", "For example, that multiplication is carried out before addition in a + 2 * c"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on interpreters and the stages of compilation (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Interpreter: one statement at a time.", "Check, execute, halt on error, repeat every run and every loop."),
  ("No translated version.", "That is the point of an interpreter."),
  ("Four stages in order.", "Lexical, syntax, code generation, optimisation."),
  ("Lexical: tokens.", "Remove white space and comments, create tokens and the symbol table."),
  ("Syntax: grammar and parse tree.", "Syntax errors reported."),
  ("Optimisation: minimum resources.", "Remove redundant code; less memory, storage, CPU time."),
], [
  ("an interpreter", "Translates and executes a program one statement at a time without producing a translated copy."),
  ("lexical analysis", "Converts source code into tokens and removes white space and comments."),
  ("syntax analysis", "Checks tokens against the grammar and produces a parse tree."),
  ("optimisation", "Improves the code so it uses minimum resources."),
], [("Explain", "Give the process and the reasons."), ("Describe", "Say what happens, in several points."), ("Outline", "Main points only."), ("State", "One short answer.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const toks = [["Total", "identifier"], ["=", "operator"], ["Price", "identifier"], ["*", "operator"], ["2", "constant"], ["+", "operator"], ["5", "constant"]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "source code", "sm") + SV.rect(20, 30, 600, 40, "cell", { rx: 6 }) + SV.text(34, 56, "Total = Price * 2 + 5   # add tax", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(20, 100, "after removing the comment and white space: Total=Price*2+5", "sm");
    if (k >= 2) { o += SV.text(20, 126, "tokens", "sm"); toks.slice(0, k - 1).forEach(([t, ty], i) => { const x = 20 + i * 86; o += SV.rect(x, 134, 78, 40, "f" + (ty === "identifier" ? 1 : ty === "operator" ? 2 : 3), { rx: 6 }) + SV.rect(x, 134, 78, 40, "ax", { rx: 6, fill: "none" }) + SV.text(x + 39, 158, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" }) + SV.text(x + 39, 190, ty, "sm", { "text-anchor": "middle", style: "font-size:10px" }); }); }
    if (k >= 9) { o += SV.text(20, 224, "symbol table", "sm") + SV.rect(20, 232, 240, 26, "cell", { rx: 4 }) + SV.text(30, 250, "Total, Price (identifiers)", "lbl", { style: "font-size:12.5px" }); }
    return o; };
  Lib.stepper($("#stA"), { w: 640, h: 270, label: "Lexical analysis", base: { i: 0 }, draw, tween: 140, dwell: 2600, steps: [{ cap: "The source code contains spaces and a comment.", s: { i: 0 } }, { cap: "<b>White space and the comment are removed</b>: they are not needed to run the program.", s: { i: 1 } }, { cap: "The rest is broken into <b>tokens</b> and each is categorised: identifier, operator or constant. There are seven: <b>Total</b>, <b>=</b>, <b>Price</b>, <b>*</b>, <b>2</b>, <b>+</b>, <b>5</b>.", s: { i: 8 } }, { cap: "The identifiers are stored in the <b>symbol table</b>. An invalid token would produce an error here. The tokens go on to syntax analysis.", s: { i: 9 } }] });
})();
(function () {
  const nodes = [{ t: "=", x: 300, y: 36 }, { t: "Total", x: 170, y: 104 }, { t: "+", x: 430, y: 104 }, { t: "*", x: 350, y: 172 }, { t: "5", x: 510, y: 172 }, { t: "Price", x: 290, y: 240 }, { t: "2", x: 410, y: 240 }];
  const edges = [[0, 1], [0, 2], [2, 3], [2, 4], [3, 5], [3, 6]]; const show = [1, 2, 3, 5, 7];
  const draw = (s) => { const k = Math.round(s.i), n = show[k]; let o = "";
    edges.forEach(([a, b]) => { if (a < n && b < n) o += SV.line(nodes[a].x, nodes[a].y, nodes[b].x, nodes[b].y, "edge"); });
    nodes.slice(0, n).forEach((nd) => (o += SV.circle(nd.x, nd.y, 26, "nd", {}) + SV.text(nd.x, nd.y + 5, nd.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (nd.t.length > 3 ? 12 : 16) + "px" })));
    o += SV.text(20, 22, "Total = Price * 2 + 5", "lbl bd", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stB"), { w: 600, h: 280, label: "Parse tree", base: { i: 0 }, draw, tween: 120, dwell: 2800, steps: [{ cap: "The parser reads the tokens against the grammar. This is an <b>assignment</b>: the root is =.", s: { i: 0 } }, { cap: "On the left is the variable being assigned to, <b>Total</b>.", s: { i: 1 } }, { cap: "The expression on the right is an addition, so <b>+</b> is the other child of =. The grammar says + binds less tightly than *, so + is higher in the tree.", s: { i: 2 } }, { cap: "The addition has two children: the multiplication, which is lower down and so worked out first, and the constant <b>5</b>.", s: { i: 3 } }, { cap: "Every token is placed. The <b>parse tree</b> is the output of syntax analysis. A token in the wrong place would give a syntax error.", s: { i: 4 } }] });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "Interpreter", "lbl bd") + SV.text(20, 128, "Compiler", "lbl bd");
    const prog = ["a", "b", "c"]; let x = 20; const iters = 3;
    for (let r = 0; r < iters; r++) prog.forEach((p, i) => { const idx = r * 3 + i, on = idx < k * 3 / 1; if (r * 3 + i < Math.min(9, k * 3)) o += SV.rect(20 + idx * 52, 34, 46, 34, "f1", { rx: 4 }) + SV.text(43 + idx * 52, 56, "T+R", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(20, 92, "T+R = translate then run, for every line, every time round the loop", "sm");
    if (k >= 1) o += SV.rect(20, 140, 150, 34, "f2", { rx: 4 }) + SV.text(95, 162, "translate once", "lbl bd", { "text-anchor": "middle", style: "font-size:12px" });
    if (k >= 2) for (let r = 0; r < Math.min(3, k - 1); r++) o += SV.rect(190 + r * 130, 140, 120, 34, "f3", { rx: 4 }) + SV.text(250 + r * 130, 162, "run loop pass " + (r + 1), "lbl", { "text-anchor": "middle", style: "font-size:12px" });
    o += SV.text(20, 206, k >= 3 ? "Interpreter translated 9 times; compiler translated once, then only ran." : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 640, h: 224, label: "Interpreter and compiler", base: { i: 0 }, draw, tween: 140, dwell: 2800, steps: [{ cap: "A three-line loop runs three times. The <b>interpreter</b> translates and runs each line as it reaches it.", s: { i: 0 } }, { cap: "First pass: three lines translated and run. Meanwhile the <b>compiler</b> translates the whole program once, before anything runs.", s: { i: 1 } }, { cap: "The interpreter has to <b>translate the same lines again</b> on pass two. The compiled program just runs.", s: { i: 2 } }, { cap: "After pass three the interpreter has translated nine lines. The compiler translated once, and the executable can be run again without translating.", s: { i: 3 } }] });
})();

(function () {
  const inp = $("#lxI"), out = $("#lxO");
  const KW = ["IF", "THEN", "ELSE", "ENDIF", "FOR", "TO", "NEXT", "WHILE", "ENDWHILE", "PRINT", "OUTPUT", "INPUT", "DECLARE", "if", "else", "for", "while", "print", "input", "def", "return"];
  const paint = () => { let src = inp.value; const cm = src.indexOf("#"); const comment = cm >= 0 ? src.slice(cm) : ""; if (cm >= 0) src = src.slice(0, cm);
    const re = /\s*([A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|"[^"]*"|==|<=|>=|<>|[-+*\/=<>()\[\],:^]|\S)/g; const t = []; let m; const ids = new Set();
    while ((m = re.exec(src))) { const x = m[1]; let ty = /^[A-Za-z_]/.test(x) ? (KW.includes(x) ? "keyword" : "identifier") : /^\d/.test(x) ? "constant" : /^"/.test(x) ? "string" : /^[-+*\/=<>^]|==|<=|>=|<>$/.test(x) ? "operator" : /^[()\[\],:]$/.test(x) ? "punctuation" : "INVALID"; if (ty === "identifier") ids.add(x); t.push([x, ty]); }
    let h = '<div class="tw"><table class="t mono"><tr><th>Token</th><th>Type</th></tr>' + t.map(([x, ty]) => `<tr><td>${x.replace(/</g, "&lt;")}</td><td style="${ty === "INVALID" ? "color:var(--bad);font-weight:700" : ""}">${ty}</td></tr>`).join("") + "</table></div>";
    out.innerHTML = h + `<div class="verdict">${t.length} token${t.length === 1 ? "" : "s"}. ${comment ? "The comment <b>" + comment.replace(/</g, "&lt;") + "</b> and the white space were removed. " : "White space is removed. "}Symbol table: <b>${ids.size ? [...ids].join(", ") : "empty"}</b>.${t.some((x) => x[1] === "INVALID") ? ' <b style="color:var(--bad)">Invalid token: the lexical analyser reports an error.</b>' : ""}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  const O = [
    ["Constant folding", "Seconds = 2 * 60 * 60", "Seconds = 7200", "A calculation on constants is done once at compile time, not every time the program runs."],
    ["Redundant code", "X = 5\nX = 10\nPRINT X", "X = 10\nPRINT X", "An assignment whose value is never used is removed, saving storage and time."],
    ["Unused variable", "Temp = A + B\nPRINT A", "PRINT A", "Code whose result is never used is removed."],
    ["Same calculation twice", "P = A * B + 1\nQ = A * B + 2", "T = A * B\nP = T + 1\nQ = T + 2", "A repeated calculation is done once, then re-used."]];
  const b = $("#opB"); const show = (i) => { const [n, a, c, why] = O[i]; $("#opO").innerHTML = `<h3>${n}</h3><div class="grid2"><div class="card"><b>Before</b><pre class="plain">${a}</pre></div><div class="card"><b>After optimisation</b><pre class="plain">${c}</pre></div></div><div class="verdict">${why}</div>`; b.querySelectorAll("button").forEach((x, j) => (x.className = j === i ? "on" : "")); };
  O.forEach((o, i) => { const x = document.createElement("button"); x.textContent = o[0]; x.onclick = () => show(i); b.appendChild(x); }); show(0);
})();
(function () {
  let n = 3;
  const paint = () => { const interp = 4 + n, comp = 5; $("#lpO").innerHTML = '<div class="tw"><table class="t mono"><tr><th></th><th>Statements translated</th></tr>' + `<tr><td>Interpreter (4 lines once + 1 line ${n} times)</td><td>${interp}</td></tr><tr><td>Compiler (all 5 lines once)</td><td>${comp}</td></tr>` + `<tr><td>Interpreter, run the program again</td><td>${interp * 2} so far</td></tr><tr><td>Compiler, run the program again</td><td>${comp} (no further translation)</td></tr></table></div>`; };
  Lib.slider($("#lpS"), { id: "lps", label: "Times the loop runs ", min: 1, max: 20, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Which stage of compilation?", ["Lexical analysis", "Syntax analysis", "Code generation", "Optimisation"],
  [("Removes white space and comments", 0), ("Produces a parse tree", 1), ("Creates executable code from the parse tree", 2), ("Removes redundant code", 3), ("Stores identifiers in a symbol table", 0), ("Checks that tokens obey the grammar", 1), ("Minimises memory use and execution time", 3), ("Breaks the source into tokens", 0)],
  "Lexical tokens, syntax grammar, generate code, optimise resources.") + CLASSIFY("cl2", "Interpreter or compiler?", ["Interpreter", "Compiler"],
  [("Translates and executes one statement at a time", 0), ("Produces an executable file", 1), ("Translation is repeated every time the program is run", 0), ("The program can run without the source code", 1), ("Halts at the first error it reaches", 0), ("Translates the whole program first", 1)],
  "Interpreter: statement by statement. Compiler: whole program, executable.") + MATCH([
  ["Lexical analysis", "Converting a sequence of characters into a sequence of tokens"], ["Syntax analysis", "Using parsing algorithms to interpret the meaning of tokens"], ["Code generation", "Converting an intermediate representation into an executable form"], ["Optimisation", "Minimising execution time and memory requirements"], ["Interpreter", "Directly executing instructions, one statement at a time"]]) + ORDER(
  "Put the stages of compilation in order.",
  ["Lexical analysis", "Syntax analysis", "Code generation", "Optimisation"],
  "Lexical, syntax, code generation, optimisation.") + CALC([
  {"q": "How many tokens does Total = Price * 2 + 5 contain?", "a": 7, "unit": "", "tol": 0.01, "hint": "Count each name, operator and number.", "sol": "<b>7</b>."},
  {"q": "How many identifiers (for the symbol table) are in Total = Price * 2 + 5?", "a": 2, "unit": "", "tol": 0.01, "hint": "Total and Price.", "sol": "<b>2</b>."},
  {"q": "A program has 4 lines run once, and 1 line that runs 6 times in a loop. How many statements does an interpreter translate?", "a": 10, "unit": "", "tol": 0.01, "hint": "4 + 6.", "sol": "<b>10</b>."},
  {"q": "The same program with a compiler: how many statements are translated?", "a": 5, "unit": "", "tol": 0.01, "hint": "Each line once.", "sol": "<b>5</b>."},
  {"q": "How many stages of compilation are named in the syllabus?", "a": 4, "unit": "", "tol": 0.01, "hint": "Lexical, syntax, code generation, optimisation.", "sol": "<b>4</b>."}]) + MCQ([
  ("Which stage produces a parse tree?", ["Lexical analysis", "Syntax analysis", "Code generation", "Optimisation"], 1, "Syntax analysis."),
  ("An interpreter:", ["Produces an executable file", "Executes one statement at a time", "Optimises the code", "Needs no source code"], 1, "One statement at a time."),
  ("What does the lexical analyser create?", ["A symbol table and tokens", "Machine code", "A parse tree", "A network"], 0, "Tokens and a symbol table."),
  ("Which stage minimises memory use?", ["Optimisation", "Lexical analysis", "Syntax analysis", "Linking"], 0, "Optimisation."),
  ("A syntax error is reported by:", ["Syntax analysis", "Code generation", "The CPU", "The printer"], 0, "The parser."),
  ("An interpreter finds an error. It:", ["Ignores it", "Reports it and halts", "Fixes it", "Restarts"], 1, "Reports and halts.")], "qz1") + CARDS([
  ("Interpreter", "One statement at a time; no translated version; repeated every run."), ("Compiler", "Translates the whole program into an executable."), ("Lexical analysis", "Tokens, symbol table, remove white space and comments."), ("Syntax analysis", "Grammar check, parse tree, syntax errors."),
  ("Code generation", "Parse tree to executable code."), ("Optimisation", "Remove redundant code; minimum resources."), ("Token", "Keyword, identifier, operator, constant."), ("Symbol table", "Stores the identifiers.")])

build("ac1621", "ac-16-2-1-interpreters-compilation-stages", "Interpreters and the Stages of Compilation", EYA("16.2.1"),
  "How an interpreter executes a program, and the four stages of compilation (lexical analysis, syntax analysis, code generation, optimisation); animations, a tokeniser lab and the real Paper 3 questions from 2021 to 2025.",
  dict(sub=CBK("Chapter 16 · System software, section 16.2 Translation software"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
