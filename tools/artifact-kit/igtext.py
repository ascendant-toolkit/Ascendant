"""Spec-driven builder for text-heavy IGCSE Economics 7-tab reviews.
review(slug, bundle, syl, title, desc, learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, cmd_names, real_items)
"""
import json
from igsy import *
F = Old("fisc"); M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

def jq(x): return json.dumps(x, ensure_ascii=False)

def review(slug, bundle, syl, title, desc, learn, steppers, lab1, lab2, cl, match, order, calcs, mcq, cards, exam_qs, tips_, cmd_names, real_items, prelude=''):
    """steppers: list of (title, color, [step html...]); lab1: dict(intro, sliders=[(label,min,max,step,val,fmt)], fn=js body using v array returning {r:[a,b,c], rl:[l1,l2,l3], t:text, bars:[[label,val,css var]]});
    lab2: dict(title, intro, items=[(button, line1, line2)], h1, h2) ; cl: [(prompt,[buckets],[(text,idx)],done)]"""
    js = HEAD + COMMON + prelude
    wl = []
    for i, st in enumerate(steppers):
        sid = f"st{i}"
        if isinstance(st, dict):
            js += f'Lib.stepper($("#{sid}"), {{ w: 760, h: st_h({st.get("h", 380)}), label: {jq(st["title"])}, base: {st["base"]}, draw: {st["draw"]}, steps: {st["steps"]} }});\n'.replace("st_h(", "(")
            wl.append((st["title"], sid)); continue
        ttl, col, steps = st
        chain = [re_strip(s) for s in steps]
        js += f'Lib.stepper($("#{sid}"), {{ w: 760, h: 380, label: {jq(ttl)}, base: {{ n: 0 }}, draw: mkChain({jq(chain)}, "{col}"), steps: chainSteps({jq(steps)}) }});\n'
        wl.append((ttl, sid))
    # Lab 1
    sl = lab1["sliders"]; n = len(sl)
    js += "function labA() {\n  const ids = [" + ",".join(f'"a{i}"' for i in range(n)) + "]; if (!ids.every((i) => $('#' + i))) return;\n  const v = ids.map((i) => +$('#' + i).value);\n  const R = (function(v) {" + lab1["fn"] + "})(v);\n"
    js += "  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;\n"
    js += "  if (R.svg) { $('#labA').innerHTML = R.svg; return; }\n  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);\n"
    js += "  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });\n"
    js += "  $('#labA').innerHTML = o;\n}\n"
    for i, (lab, mn, mx, st, val, fmt) in enumerate(sl):
        js += f'Lib.slider($("#ga{i}"), {{ id: "a{i}", label: {jq(lab)}, min: {mn}, max: {mx}, step: {st}, value: {val}, fmt: (v) => {fmt}, onInput: labA }});\n'
    items = lab2["items"]
    js += f"const L2 = {jq([{'n': a, 'a': b, 'b': c} for a, b, c in items])};\n"
    js += f'button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>{lab2["h1"]}</th><th>{lab2["h2"]}</th></tr><tr><td><b>${{p.a}}</b></td><td>${{p.b}}</td></tr></table></div>`);\n'
    # Practise
    for i, (pr, bks, its, done) in enumerate(cl):
        js += f'Lib.classify($("#cl{i+1}"), {{ prompt: {jq(pr)}, buckets: {jq([{"label": b} for b in bks])}, items: {jq([{"text": t, "b": b} for t, b in its])}, done: {jq(done)} }});\n'
    js += f'Lib.match($("#m1"), {{ prompt: "Match the term to its meaning.", pairs: {jq(match)}, done: "Learn these terms." }});\n'
    js += f'Lib.order($("#o1"), {{ prompt: {jq(order[0])}, items: {jq(order[1])}, done: {jq(order[2])} }});\n'
    js += calc_js(calcs) + mcq_js("qz1", mcq) + "\n" + cards_js(cards) + "labA(); \n"
    gl = "".join(f'<div id="ga{i}"></div>' for i in range(n))
    explore = f'''
  <h2>Lab 1 · {lab1["title"]}</h2>
  <p>{lab1["intro"]}</p>
  <div class="card"><div class="grid2"><div>{gl}</div>
    <div><div class="readout"><div><small>{lab1["rl"][0]}</small><strong id="ar0"></strong></div><div><small>{lab1["rl"][1]}</small><strong id="ar1"></strong></div><div><small>{lab1["rl"][2]}</small><strong id="ar2"></strong></div></div><div class="verdict" id="avv"></div></div></div>
    <svg id="labA" viewBox="0 0 760 345" role="img" aria-label="{lab1["title"]}"></svg>
  </div>

  <h2>Lab 2 · {lab2["title"]}</h2>
  <p>{lab2["intro"]}</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''
    pr_items = []
    names = ["Practice A", "Practice B"]
    for i, (pr, bks, its, done) in enumerate(cl):
        pr_items.append((cl_title(i, bks), f"cl{i+1}", "card"))
    pr_items += [("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")]
    ex = exam(*exam_qs)
    tp = tips(tips_, cmds(*cmd_names))
    body = page(CL(f"{syl} {title}"), title, desc, learn=learn, watch=watch(*wl), explore=explore,
        practise=practise(*pr_items), real=real(*[rw(a, b, c) for a, b, c in real_items]), exam=ex, tips=tp)
    write(bundle, body, js, title, slug)

def cl_title(i, bks): return " / ".join(bks[:3]) + "?"

def re_strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)
