"""Shared pieces for the six IGCSE CS 8.1.4 pages (p814a..p814f): page skeleton, exam question helper, trace engine, recorder."""
import html as _h, json, pathlib

D = pathlib.Path(__file__).parent
# Style blocks and helper classes come from the 7.3 page so the look matches.
STYLES = (D / "p73.body.html").read_text().split('<div class="wrap">')[0]

CMD_WORDS = '''  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>State / Name / Identify</td><td>A short fact. No explanation.</td></tr>
    <tr><td>Describe</td><td>What happens, step by step, or the main features.</td></tr>
    <tr><td>Explain</td><td>What happens and why. Use because or so.</td></tr>
    <tr><td>Complete</td><td>Fill in the gaps, trace table or code you are given.</td></tr>
    <tr><td>Write / Give</td><td>Produce an algorithm, code or an example. Be precise.</td></tr>
  </table></div>
'''


def qc(lines):
    return '<pre class="cp" style="margin:8px 0">' + "".join(f'<span class="ln">{_h.escape(l) or " "}</span>' for l in lines) + "</pre>"


def ac(lines):
    """Pseudocode shown inside a model answer (no line numbers needed, kept compact)."""
    return '<pre class="cp" style="margin:6px 0">' + "".join(f'<span class="ln">{_h.escape(l) or " "}</span>' for l in lines) + "</pre>"


def mk(n, t):
    return f'<span class="mk k" data-t="{n}">{t}</span>'


def eq(n, cmd, marks, stem, reminder, answer, mistake, pre=""):
    """One exam-style question. answer is HTML (use mk() spans); pre is an optional code block shown under the question."""
    return (f'  <details class="eq"><summary>Q{n} <span class="cmd">{cmd}</span> <span class="mark">{marks} mark{"s" if marks != 1 else ""}</span> {stem}</summary><div class="body">\n'
            f'    {pre}\n    <div class="tip"><b class="h">Reminder</b>{reminder}</div>\n'
            f'    <div class="ans">{answer}</div>\n'
            f'    <div class="warn"><b class="h">Common mistake</b>{mistake}</div>\n  </div></details>\n')


def rw(title, text, use):
    return f'  <div class="rw"><h3>{title}</h3><p>{text}</p><div class="use"><b>Exam use:</b> {use}</div></div>\n'


def tips(items):
    return '  <h2>Top tips</h2>\n  <ul class="tips">\n' + "".join(f"    <li>{t}</li>\n" for t in items) + "  </ul>\n"


def table(heads, rows, cls="t"):
    h = f'<div class="tw"><table class="{cls}">\n    <tr>' + "".join(f"<th>{x}</th>" for x in heads) + "</tr>\n"
    h += "".join("    <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>\n" for r in rows)
    return h + "  </table></div>\n"


def page(num, title, lead, big, learn, watch, explore, practise, real, exam, tipshtml, name):
    """Writes <name>.body.html. Each section argument is an HTML string; watch/explore/practise already hold their own headings."""
    body = STYLES + f'''<div class="wrap">
<header class="top">
  <div class="eyebrow">IGCSE Computer Science · 0478 · Chapter 8 · {num}</div>
  <h1>{title}</h1>
  <p class="lead">{lead}</p>
</header>

<nav class="tablist" role="tablist" aria-label="Sections">
  <button role="tab" data-p="learn">Learn</button>
  <button role="tab" data-p="watch">Watch</button>
  <button role="tab" data-p="explore">Explore</button>
  <button role="tab" data-p="practise">Practise</button>
  <button role="tab" data-p="real">Real world</button>
  <button role="tab" data-p="exam">Exam questions</button>
  <button role="tab" data-p="tips">Tips &amp; keywords</button>
</nav>

<section id="learn" role="tabpanel">
  <div class="card big">
    <h3>The big idea</h3>
    <p>{big}</p>
  </div>
{learn}</section>

<section id="watch" role="tabpanel" hidden>
  <p>Press Play, or click the numbered steps. The code panel has a Pseudocode tab and a Python tab, and the highlighted line follows the animation.</p>
{watch}</section>

<section id="explore" role="tabpanel" hidden>
{explore}</section>

<section id="practise" role="tabpanel" hidden>
{practise}</section>

<section id="real" role="tabpanel" hidden>
  <p class="note">Descriptions are kept general. Check current details before quoting specifics.</p>
{real}</section>

<section id="exam" role="tabpanel" hidden>
  <h2>Exam-style questions</h2>
  <p>These are written for this page in the style of Paper 2 (pseudocode, trace and "write an algorithm" questions). They only use ideas up to and including this page. Open each one for reminders, a model answer and common mistakes. Each underlined phrase earns one mark; the number shows which mark point it is.</p>
{exam}</section>

<section id="tips" role="tabpanel" hidden>
{tipshtml}
{CMD_WORDS}  <h2>Keyword flashcards</h2>
  <div id="fc1"></div>
</section>
</div>
'''
    (D / f"{name}.body.html").write_text(body)


# ---------- JS shared by all six pages ----------
SHARED_JS = r'''const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const fv = (v) => (v === null || v === undefined ? "?" : v === true ? "TRUE" : v === false ? "FALSE" : typeof v === "string" ? '"' + v + '"' : v);
/* One animation frame: variable boxes, optional character cells or input queue, a condition result, and the output so far. */
function trSvg(f, o) {
  const W = 640; let s = SV.text(14, 24, f.title || o.title || "", "lbl bd", { "text-anchor": "start" });
  if (f.right) s += SV.text(W - 14, 24, f.right, "lbl bd t4", { "text-anchor": "end" });
  const vs = f.vars || [], n = vs.length;
  if (n) {
    const gap = 10, w = Math.min(150, Math.floor((W - 28 - (n - 1) * gap) / n)), tot = n * w + (n - 1) * gap, x0 = (W - tot) / 2;
    vs.forEach(([k, v], i) => {
      const x = x0 + i * (w + gap), hi = (f.hl || []).includes(k), t = String(fv(v));
      s += SV.rect(x, 38, w, 58, "", { rx: 10, style: `fill:var(--surface);stroke:${hi ? ACC : MUT};stroke-width:${hi ? 4 : 2}` });
      s += SV.text(x + w / 2, 56, k, "sm", { "text-anchor": "middle" });
      s += SV.text(x + w / 2, 84, t, "lbl bd", { "text-anchor": "middle", style: `font-size:${t.length > 9 ? 13 : t.length > 6 ? 16 : 20}px;font-family:var(--mono)` });
    });
  }
  if (f.cells) {
    const a = f.cells, m = a.length, g = 5, w = Math.min(44, Math.floor((W - 28 - (m - 1) * g) / m)), tot = m * w + (m - 1) * g, x0 = (W - tot) / 2;
    s += Lib.cells(a, { x0, y: 112, w, h: 38, gap: g, cls: f.cc || {}, idx: false });
    a.forEach((_, i) => (s += SV.text(x0 + i * (w + g) + w / 2, 166, i + 1, "sm", { "text-anchor": "middle" })));
  } else if (f.inp) {
    const t = f.inp.length ? "Waiting to be typed in:   " + f.inp.map(fv).join("    ") : "Nothing left to input";
    s += SV.rect(14, 114, W - 28, 36, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
    s += SV.text(W / 2, 138, t, "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
  }
  if (f.cond) s += SV.text(W / 2, 196, `${f.cond[0]}   is   ${f.cond[1] ? "TRUE" : "FALSE"}`, "lbl bd " + (f.cond[1] ? "t3" : "t2"), { "text-anchor": "middle", style: "font-family:var(--mono)" });
  else if (f.note) s += SV.text(W / 2, 196, f.note, "lbl bd " + (f.nc || ""), { "text-anchor": "middle" });
  let ot = (f.out || []).join("   "); if (ot.length > 62) ot = "…" + ot.slice(-61);
  s += SV.rect(14, 212, W - 28, 44, "", { rx: 10, style: "fill:var(--soft);stroke:var(--line);stroke-width:2" });
  s += SV.text(26, 229, "Output", "sm", { "text-anchor": "start" });
  s += SV.text(26, 249, ot, "lbl bd", { "text-anchor": "start", style: "font-family:var(--mono);font-size:15px" });
  return s;
}
function tr(el, o) {
  Lib.algo(el, { w: 640, h: 270, label: o.label, pseudo: o.pseudo, py: o.py, dwell: o.dwell || 2000, frames: o.frames.map((f) => ({ cap: f.cap, ps: f.ps, py: f.py, svg: trSvg(f, o) })) });
}
const nums = (v, k = 20) => v.trim().split(/[\s,]+/).filter(Boolean).map(Number).filter((x) => !isNaN(x)).slice(0, k);
'''


class R:
    """Records animation frames from real Python values, so captions and variables are always correct."""

    def __init__(s, names):
        s.v = {k: None for k in names}
        s.out = []
        s.fr = []

    def f(s, cap, ps, py, hl=(), **kw):
        d = dict(cap=cap, ps=ps, py=py, vars=[[k, v] for k, v in s.v.items()], hl=list(hl), out=list(s.out))
        d.update(kw)
        s.fr.append(d)

    def js(s):
        return json.dumps(s.fr, ensure_ascii=False)


def write_js(name, parts):
    (D / f"{name}.js").write_text(SHARED_JS + "\n".join(parts) + "\n")
