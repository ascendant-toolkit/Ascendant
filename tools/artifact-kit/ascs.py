"""Shared builder for the AS Level Computer Science (9618 chapters 2-12) pages: the practise tab and the closing build call."""
from ak16 import *


def PR(heads, cl1, cl2, match, order, calc, mcq, cards):
    """heads = six headings for the practise tab; cl1/cl2 = (title, categories, items, tip); order = (title, steps, tip).
    Returns (practise html, js for the practise tab)."""
    h = [f'<h2>1 · {heads[0]}</h2><div id="cl1" class="card"></div>', f'<h2>2 · {heads[1]}</h2><div id="cl2" class="card"></div>', f'<h2>3 · {heads[2]}</h2><div id="m1" class="card"></div>',
         f'<h2>4 · {heads[3]}</h2><div id="o1" class="card"></div>', f'<h2>5 · {heads[4]}</h2><div id="c1"></div>', f'<h2>6 · {heads[5]}</h2><div id="qz1"></div>']
    js = CLASSIFY("cl1", *cl1) + CLASSIFY("cl2", *cl2) + MATCH(match) + ORDER(*order) + CALC(calc) + MCQ(mcq, "qz1") + CARDS(cards)
    return "\n  " + "\n  ".join(h) + "\n", js


def finish(slug, key, title, desc, ident, ch, sec, learn, watch, explore, practise, real, where, past, review, intro, tips, js):
    exam = exam20(intro, where, past, review)
    build(key, slug, title, EYA(ident), desc, dict(sub=CBK(f"Chapter {ch} · {sec}"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
