"""Past paper questions for Economics lessons that had only our own exam questions.

econ_past.json holds them: 9708 questions with mark points, mostly the same ones used on the narrower
topic lessons (price elasticity of supply was read from Papers 1 and 2 for this). build.py calls apply(), which puts
them at the top of the Exam questions tab and adds the multiple choice quiz to the page script.
"""
import json
import re
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "econ_past.json").read_text(encoding="utf-8"))
START = "<!-- past papers -->"
# this page headed its own questions "Past paper questions"
RENAME = ("<h2>Past paper questions on government spending and net exports</h2>", "<h2>Practice questions on government spending and net exports</h2>")


def apply(page, slug):
    if slug not in DATA or START in page:
        return page
    d = DATA[slug]
    paper = "Paper 1 and Paper 2" if slug.startswith("as-") else "Paper 3 and Paper 4"
    block = (START + '<div class="kit"><h2>Past paper questions</h2>'
             f'<p>Real 9708 {paper} questions, each with its source. Check the source paper and mark scheme for the full detail. '
             'Several also appear on the lessons for the individual topics.</p>')
    if d["written"]:
        block += '<h3>Written questions</h3>' + "".join(d["written"])
    if d["mcq"]:
        block += f'<h3>Multiple choice ({paper.split(" and ")[0] if slug.startswith("as-") else "Paper 3"})</h3><div id="x-pp-qz"></div>'
    block += '<h2>Practice questions</h2><p>The questions below are our own, written for practice.</p></div>\n'
    page = page.replace(*RENAME)
    m = re.search(r'<section id="exam"[^>]*>', page)
    page = page[:m.end()] + "\n" + block + page[m.end():]
    if d["mcq"]:
        js = f'Lib.quiz($("#x-pp-qz"), {json.dumps(dict(qs=d["mcq"]), ensure_ascii=False)});'
        main = max(re.finditer(r"<script>(.*?)</script>", page, re.S), key=lambda s: len(s[1]))
        page = page[:main.end(1)] + "\n" + js + "\n" + page[main.end(1):]
    return page
