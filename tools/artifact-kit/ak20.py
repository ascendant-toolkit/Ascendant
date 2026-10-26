"""Shared pieces for the A Level Computer Science (9618) section 20 pages (Further programming): real past paper question blocks, numbered code blocks and a few drawing helpers.
Run a page with: python3 tools/artifact-kit/mk_ac2011.py"""
import html as _h
import re as _re
from ak import *

_SER = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}


def SRC(*parts):
    """Source chip: SRC('s21', '31/32/33', 'Q9(a)') -> 'M/J 2021 · 9618/31/32/33 · Q9(a)'."""
    ser, paper, q = parts
    short = {"s": "M/J", "w": "O/N", "m": "F/M"}[ser[0]]
    return f"{short} 20{ser[1:]} · 9618/{paper} · {q}"


def pc(text, start=1):
    """Numbered code block. Marks: {{k:text}} (technical) or {{a:text}} (applied) wrap a mark-scheme point."""
    out = []
    for l in text.strip("\n").split("\n"):
        e = _h.escape(l) or " "
        e = _re.sub(r"\{\{([kan]):(.*?)\}\}", lambda m: f'<span class="mk {m.group(1)}">{m.group(2)}</span>', e)
        out.append(f'<span class="ln">{e}</span>')
    return f'<pre class="cp" style="counter-reset:l {start - 1}">' + "".join(out) + "</pre>"


def qcode(text):
    """Code shown inside a question: monospace lines, no line numbers (the paper does not number them)."""
    return '<pre class="plain">' + _h.escape(text.strip("\n")) + "</pre>"


def mks(items, kind="k"):
    """Mark points as coloured spans, numbered: mks(['a', 'b']) -> one span per point with [1], [2]."""
    return " ".join(f'<span class="mk {kind}" data-t="{i + 1}">{t}</span>' for i, t in enumerate(items))


def peq(src, marks, command, question, tip, answer, warn=None):
    """One real past paper question. src is the chip text, question may contain code from qcode(), answer is HTML."""
    h = f'  <details class="eq"><summary><span class="src">{src}</span> <span class="cmd">{command}</span> <span class="mark">{marks}</span> {question}</summary><div class="body">\n'
    h += f'    <div class="tip"><b class="h">Reminder</b>{tip}</div>\n'
    h += f'    <div class="ans">{answer}</div>\n'
    if warn:
        h += f'    <div class="warn"><b class="h">Common mistake</b>{warn}</div>\n'
    return h + "  </div></details>\n"


def req(marks, command, question, tip, answer, warn=None):
    """One review question (not from a past paper): same layout, no source chip."""
    h = f'  <details class="eq"><summary><span class="cmd">{command}</span> <span class="mark">{marks}</span> {question}</summary><div class="body">\n'
    h += f'    <div class="tip"><b class="h">Reminder</b>{tip}</div>\n'
    h += f'    <div class="ans">{answer}</div>\n'
    if warn:
        h += f'    <div class="warn"><b class="h">Common mistake</b>{warn}</div>\n'
    return h + "  </div></details>\n"


def exam20(intro, where, past, review, note=""):
    """Exam tab: where = list of (session, paper, question, marks, what it asks) rows for the summary table."""
    t = '  <h2>Exam questions</h2>\n'
    t += f'  <p>{intro} Open each question for a reminder, a model answer and a common mistake. Each coloured phrase earns one mark; the number shows which mark point it is.</p>\n'
    t += '  <div class="key"><span class="k"><i></i> mark-scheme point</span><span class="a"><i></i> second part or applied point</span></div>\n'
    t += '  <h2>1. Past paper questions</h2>\n'
    if where:
        t += '  <div class="tw"><table class="t">\n    <tr><th>Session</th><th>Paper</th><th>Question</th><th>Marks</th><th>What it asks</th></tr>\n'
        t += "".join(f"    <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>\n" for a, b, c, d, e in where)
        t += "  </table></div>\n"
    if note:
        t += f'  <p class="note">{note}</p>\n'
    t += past
    t += '  <h2>2. Review questions</h2>\n  <p>Written for practice and revision, not taken from past papers. Use them to check your understanding before attempting the real questions above.</p>\n'
    return t + review


# Shared JS for the section 20 diagrams.
AK20JS = r'''
/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}
'''
