"""Shared helpers for the syllabus-numbered A Level Economics reviews (mk_sy92.py, mk_sy93.py).
Each page is written from scratch with page()/write() from splitter.py; this module holds the repeated HTML and JS."""
import json
from splitter import page, write, newtips, cmd, FC, KEYL

def jq(x): return json.dumps(x, ensure_ascii=False)

def mc(q, opts, a, why): return "  { q: " + jq(q) + ", opts: " + jq(opts) + ", a: " + str(a) + ", why: " + jq(why) + " },\n"
def MCQ(items, el="qz2"): return f'Lib.quiz($("#{el}"), {{ qs: [\n' + "".join(mc(*i) for i in items) + '] });\n'
def CALC(items): return 'Lib.calc($("#c1"), { qs: [\n' + "".join("  " + jq(i) + ",\n" for i in items) + '] });\n'
def CARDS(pairs): return 'Lib.cards($("#fc1"), { cards: [\n' + "".join("  " + jq(list(p)) + ",\n" for p in pairs) + '] });\n'
def CLASSIFY(el, prompt, buckets, items, done):
    return f'Lib.classify($("#{el}"), {{ prompt: {jq(prompt)}, buckets: {jq([{"label": b} for b in buckets])}, items: {jq([{"text": t, "b": b} for t, b in items])}, done: {jq(done)} }});\n'
def MATCH(pairs, done="Learn these terms."): return f'Lib.match($("#m1"), {{ prompt: "Match the term to its meaning.", pairs: {jq(pairs)}, done: {jq(done)} }});\n'
def ORDER(prompt, items, done): return f'Lib.order($("#o1"), {{ prompt: {jq(prompt)}, items: {jq(items)}, done: {jq(done)} }});\n'

HEAD = '''const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}
'''

def rw(title, body, use): return f'  <div class="rw"><h3>{title}</h3><p>{body}</p><div class="use"><b>Exam use:</b> {use}</div></div>\n'
RWNOTE = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'

def eq(src, marks, q, bullets, plan, ans=None):
    """One reworded exam question. bullets: mark scheme points in our own words. ans: list of (kind, text) paragraph runs, or None."""
    h = f'  <details class="eq"><summary>{src} <span class="mark">{marks}</span> {q}</summary><div class="body">\n'
    h += '    <div class="tip"><b class="h">What the mark scheme wants</b>\n      <ul>\n' + "".join(f"        <li>{b}</li>\n" for b in bullets) + '      </ul></div>\n'
    h += f'    <div class="tip"><b class="h">Plan</b>{plan}</div>\n'
    if ans:
        h += "    " + KEYL + '    <div class="ans">\n'
        for para in ans:
            h += "    <p>" + " ".join(f'<span class="mk {k}" data-t="{k.upper()}">{t}</span>' for k, t in para) + "</p>\n"
        h += "    </div>\n"
    return h + "  </div></details>\n"

def exam_page(title, intro, rows, qs, mcq_h="Multiple choice questions (Paper 3)", pre=""):
    t = f'  <h2>Past paper questions on {title}</h2>\n  <p>{intro}</p>\n  <div class="tw"><table class="t">\n    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>\n'
    t += "".join(f"    <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>\n" for a, b, c in rows) + '  </table></div>\n'
    t += pre + '  <h2>A · Written questions (reworded)</h2>\n  <p>The wording, context and figures are our own, so they are safe to set as practice. The source paper is named for reference. Mark scheme points are in our own words.</p>\n' + "".join(qs)
    t += f'  <h2>B · {mcq_h}</h2>\n  <p>Choose an answer, then read the reason. Reworded from the paper and question number shown.</p>\n  <div id="qz2"></div>\n'
    return t

def tips_html(items, sents, words):
    return newtips(items, sents) + cmd(*words)

CW = {
 "define": ("Define / State", "Give the exact meaning, briefly. No explanation needed."),
 "explain": ("Explain", "Give reasons, with a clear chain of cause and effect."),
 "analyse": ("Analyse", "Break the issue into steps of cause and effect, using a diagram where it helps."),
 "consider": ("Consider", "Look at the issue from several sides and judge how strong each is."),
 "discuss": ("Discuss", "Arguments on both sides, then a judgement."),
 "assess": ("Assess", "Judge how important or effective something is, with reasons."),
 "evaluate": ("Evaluate", "Weigh the arguments and reach a supported conclusion."),
}

def tabs(learn, watch, explore, practise, real, exam, tips): return dict(learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips)

def build(bundle, slug, title, eyebrow, lead, secs, js):
    body = page(eyebrow, title, lead, **secs)
    write(bundle, body, HEAD + js, title, slug)
