"""Helpers for splitting a one-page chapter review into numbered part reviews (see mk_ch*.py).
Src(name) slices the old <name>.body.html / <name>.js by 1-based inclusive line ranges; page() wraps the seven tabs."""
import pathlib, subprocess
D = pathlib.Path(__file__).parent
TABS = [("learn", "Learn"), ("watch", "Watch"), ("explore", "Explore"), ("practise", "Practise"), ("real", "Real world"), ("exam", "Exam questions"), ("tips", "Tips &amp; keywords")]

class Src:
    def __init__(self, name):
        self.h = (D / f"{name}.body.html").read_text().split("\n")
        self.j = (D / f"{name}.js").read_text().split("\n")
    def b(self, *r): return "".join("\n".join(self.h[a - 1:z]) + "\n" for a, z in r)
    def j_(self, *r): return "".join("\n".join(self.j[a - 1:z]) + "\n" for a, z in r)

def page(eyebrow, h1, lead, learn_class="", explore_class="", **secs):
    nav = "\n".join(f'  <button role="tab" data-p="{k}">{v}</button>' for k, v in TABS)
    out = f'<div class="wrap">\n<header class="top">\n  <div class="eyebrow">{eyebrow}</div>\n  <h1>{h1}</h1>\n  <p class="lead">{lead}</p>\n</header>\n\n<nav class="tablist" role="tablist" aria-label="Sections">\n{nav}\n</nav>\n'
    for i, (k, _) in enumerate(TABS):
        cls = learn_class if k == "learn" else explore_class if k == "explore" else ""
        out += f'\n<section id="{k}" role="tabpanel"{"" if i == 0 else " hidden"}{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>\n{secs[k].strip(chr(10))}\n</section>\n'
    return out + "</div>\n"

def write(name, body, js, title=None, slug=None):
    (D / f"{name}.body.html").write_text(body)
    (D / f"{name}.js").write_text(js)
    if title:
        print(subprocess.run(["python3", str(D / "assemble.py"), name, title, slug], capture_output=True, text=True).stdout.strip())

def key(): return '<div class="key"><span class="k"><i></i>K</span><span class="a"><i></i>A</span><span class="n"><i></i>N</span><span class="e"><i></i>E</span></div>'

# ---- shared helpers used by the later mk_ch*.py files
def _lines(S, old): return S.j_(*[(i, i) for i in old])
def mcq(S, old=(), new=""): return 'Lib.quiz($("#qz2"), { qs: [\n' + _lines(S, old) + new + '] });\n'
def qz(S, old=(), new=""): return 'Lib.quiz($("#qz1"), { qs: [\n' + _lines(S, old) + new + '] });\n'
def cards(S, old=(), new=""): return 'Lib.cards($("#fc1"), { cards: [\n' + _lines(S, old) + new + '] });\n'
def calc(S, old=(), new=""): return 'Lib.calc($("#c1"), { qs: [\n' + _lines(S, old) + new + '] });\n'
def tips(S, lis=(), new="", rows=()):
    return '<h2>Top tips</h2>\n  <ul class="tips">\n' + (S.b(*[(i, i) for i in lis]) if lis else "") + new + '  </ul>\n  <h2>Sentences you can use</h2>\n  <div class="tw"><table class="t">\n    <tr><th>You want to say</th><th>Use this sentence</th></tr>\n' + (S.b(*[(i, i) for i in rows]) if rows else "") + '  </table></div>\n'
def newtips(items, sents):
    return '<h2>Top tips</h2>\n  <ul class="tips">\n' + "".join(f"    <li><b>{a}</b> {b}</li>\n" for a, b in items) + '  </ul>\n  <h2>Sentences you can use</h2>\n  <div class="tw"><table class="t">\n    <tr><th>You want to say</th><th>Use this sentence</th></tr>\n' + "".join(f'    <tr><td>{a}</td><td>"{b}"</td></tr>\n' for a, b in sents) + '  </table></div>\n'
def cmd(*r): return '<h2>Command words</h2>\n  <div class="tw"><table class="t">\n    <tr><th>Command word</th><th>What it asks for</th></tr>\n' + "".join(f"    <tr><td>{a}</td><td>{b}</td></tr>\n" for a, b in r) + '  </table></div>\n'
NOTE = '<p class="note">Examples are explained in general terms. The numbers are simple on purpose, to show the idea.</p>\n'
KEYL = '<div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>\n'
KEYS = key() + "\n"
FC = '<h2>Flashcards</h2><div id="fc1"></div>\n'
MCQTAIL = '  <h2>{}</h2>\n  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>\n  <div id="qz2"></div>\n'
CW = {"explain": ("Explain", "Give reasons, with a clear chain of cause and effect."), "evaluate": ("Evaluate", "Weigh the arguments and reach a supported conclusion."), "discuss": ("Discuss", "Arguments on both sides, then a judgement."), "consider": ("Consider", "Look at the issue from several sides and judge how strong each is."), "assess": ("Assess", "Judge how important or effective something is, with reasons."), "analyse": ("Analyse", "Break the effect down step by step, usually with a diagram.")}
