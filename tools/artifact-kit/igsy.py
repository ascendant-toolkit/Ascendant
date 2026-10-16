"""Helpers for the IGCSE Economics reviews that follow the syllabus numbering (4.2.1, 4.3.2 ...).
Pages are assembled from slices of the old whole-chapter pages (fisc, mon) plus new content."""
import re, pathlib
from splitter import page, write, D, TABS

KEYL = '<div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>\n'
RWNOTE = '<p class="note">Examples are described in general terms so they stay accurate. Check current details before quoting figures.</p>\n'

class Old:
    """An old page, sliced by 1-based inclusive line ranges."""
    def __init__(self, name):
        self.h = (D / f"{name}.body.html").read_text().split("\n")
        self.j = (D / f"{name}.js").read_text().split("\n")
    def b(self, *r):
        t = "".join("\n".join(self.h[a - 1:z]) + "\n" for a, z in r)
        return re.sub(r"\b\d\d\.\d · ", "", t)
    def j_(self, *r): return "".join("\n".join(self.j[a - 1:z]) + "\n" for a, z in r)
    def jl(self, *lines): return "".join(self.j[i - 1] + "\n" for i in lines)

def mk(text):
    """[K|text] -> colour-coded mark span"""
    return re.sub(r"\[([KANE])\|(.*?)\]", lambda m: f'<span class="mk {m.group(1).lower()}" data-t="{m.group(1)}">{m.group(2)}</span>', text, flags=re.S)

def Q(n, cmd, marks, text, tip, ans, warn=None, key=False):
    out = f'  <details class="eq"><summary>Q{n} <span class="cmd">{cmd}</span> <span class="mark">{marks} marks</span> {text}</summary><div class="body">\n'
    out += f'    <div class="tip"><b class="h">Reminder</b>{tip}</div>\n'
    if key: out += '    ' + KEYL
    out += '    <div class="ans">' + mk(ans) + '</div>\n'
    if warn: out += f'    <div class="warn"><b class="h">Common mistake</b>{warn}</div>\n'
    return out + '  </div></details>\n\n'

def exam(*parts, intro=True):
    s = '<h2>Exam-style questions</h2>\n'
    if intro:
        s += '  <p>Open each question for the reminders, a model answer and common mistakes. Answers are colour-coded to the mark scheme. Past-paper questions show the session.</p>\n  ' + KEYL.replace('(K)', '(K)') + '\n'
    body = "".join(parts); n = [0]
    def ren(m): n[0] += 1; return f'<summary>Q{n[0]} '
    return s + re.sub(r'<summary>Q\d+ ', ren, body)

def tips(items, cmds):
    s = '<h2>Top tips</h2>\n  <ul class="tips">\n' + "".join(f"    <li><b>{a}</b> {b}</li>\n" for a, b in items) + '  </ul>\n'
    s += '  <h2>Command words</h2>\n  <div class="tw"><table class="t">\n    <tr><th>Command word</th><th>What it asks for</th></tr>\n' + "".join(f"    <tr><td>{a}</td><td>{b}</td></tr>\n" for a, b in cmds) + '  </table></div>\n'
    return s + '  <h2>Keyword flashcards</h2>\n  <div id="fc1"></div>\n'

CMD = {
    "Define": ("Define", "A precise meaning, in a sentence."),
    "Identify": ("Identify", "Name it. No explanation needed."),
    "Calculate": ("Calculate", "Working, answer, units."),
    "Explain": ("Explain", "Reasons with a developed link."),
    "Analyse": ("Analyse", "A chain of cause and effect, applied to the context."),
    "Discuss": ("Discuss", "Both sides, then a justified judgement."),
}
def cmds(*names): return [CMD[n] for n in names]

def watch(*pairs, intro="Press Play, or click the numbered steps."):
    return f"<p>{intro}</p>\n" + "".join(f'  <h2>{i + 1} · {t}</h2><div id="{d}"></div>\n' for i, (t, d) in enumerate(pairs))

def practise(*items):
    """items: (title, id, kind) with kind 'card' or ''"""
    return "".join(f'  <h2>{i + 1} · {t}</h2>\n  <div id="{d}"{" class=" + chr(34) + "card" + chr(34) if k else ""}></div>\n\n' for i, (t, d, k) in enumerate(items))

def real(*blocks): return RWNOTE + "".join(blocks)
def rw(title, text, use): return f'  <div class="rw"><h3>{title}</h3><p>{text}</p><div class="use"><b>Exam use:</b> {use}</div></div>\n'

def mcq_js(var_id, items):
    """items: (q, [opts], answer index, why)"""
    def js(x): return '"' + x.replace('"', '\\"') + '"'
    return f'Lib.quiz($("#{var_id}"), {{ qs: [\n' + "".join(f'  {{ q: {js(q)}, opts: [{", ".join(js(o) for o in opts)}], a: {a}, why: {js(w)} }},\n' for q, opts, a, w in items) + '] });\n'

def calc_js(items, extra_old=""):
    """items: (q, answer, solution, hint or None, tol or None)"""
    def js(x): return '"' + x.replace('"', '\\"') + '"'
    out = 'Lib.calc($("#c1"), { qs: [\n' + extra_old
    for q, a, sol, hint, tol in items:
        out += f'  {{ q: {js(q)}, a: {a}' + (f', tol: {tol}' if tol else '') + (f', hint: {js(hint)}' if hint else '') + f', sol: {js(sol)} }},\n'
    return out + '] });\n'

def cards_js(pairs):
    def js(x): return '"' + x.replace('"', '\\"') + '"'
    return 'Lib.cards($("#fc1"), { cards: [\n' + "".join(f'  [{js(a)}, {js(b)}],\n' for a, b in pairs) + '] });\n'

def pick_cards(old, names):
    """cards from an old page's Lib.cards block, chosen by term"""
    got = []
    for ln in old.j:
        m = re.match(r'\s*\["([^"]+)", "(.*)"\],?\s*$', ln)
        if m and m.group(1) in names: got.append((m.group(1), m.group(2)))
    order = {n: i for i, n in enumerate(names)}
    got.sort(key=lambda x: order[x[0]])
    return got

def seg(old, start, end=None):
    """lines of old.j from the first line starting with `start` up to (not including) the next line starting with `end`"""
    i = next(k for k, l in enumerate(old.j) if l.startswith(start))
    j = len(old.j)
    if end:
        j = next(k for k in range(i + 1, len(old.j)) if old.j[k].startswith(end))
    return "\n".join(old.j[i:j]) + "\n"

def blk(old, start):
    """a Lib.* block: from the line starting with `start` to just before the next top-level statement"""
    i = next(k for k, l in enumerate(old.j) if l.startswith(start))
    j = next(k for k in range(i + 1, len(old.j)) if re.match(r"(Lib\.|lab[A-Z]\(|/\*|const |function )", old.j[k]))
    return "\n".join(old.j[i:j]).rstrip("\n") + "\n"

def items(old, start, *idx):
    """chosen item lines (0-based) from a Lib.calc / Lib.quiz block"""
    lines = blk(old, start).split("\n")[1:]
    lines = [l for l in lines if l.strip().startswith("{")]
    return "".join(lines[i] + "\n" for i in idx)

def details(old):
    return re.findall(r'  <details class="eq">.*?</details>\n', "\n".join(old.h), flags=re.S)

def rws(old):
    return re.findall(r'  <div class="rw">.*?</div></div>\n', "\n".join(old.h))
