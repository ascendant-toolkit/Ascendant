"""Past paper questions for IGCSE Economics lessons that had only our own exam questions.

ig_past.json holds them: 0455 Paper 2 questions in our own words, with our answers marked up by skill. build.py calls
apply(), which puts them on the Exam tab above the practice questions.
"""
import json
import re
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "ig_past.json").read_text(encoding="utf-8"))
START = "<!-- past papers -->"
KEY = ('<div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span>'
       '<span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>')


# practice questions that ask the same thing as a past paper question added above them
SAME = {
    "ig-unemployment-definitions": ["What is meant by full employment?"],
    "ig-mixed-system": ["Define a mixed economic system."],
    "ig-money": ["Identify two functions of money.", "Explain two characteristics of good money."],
    "ig-banking": ["Identify two functions of a central bank."],
    "ig-division-of-labour": ["Define division of labour."],
    "ig-labour-capital-intensive": ["Explain two reasons why a firm may choose labour-intensive production."],
    "ig-revenue-definitions": ["Define total revenue."],
    "ig-monopoly-markets": ["Identify two characteristics of a monopoly market."],
    "ig-firm-objectives": ["Identify two objectives of firms."],
}


def _practice(page, slug):
    """Drop the repeats and number the practice questions again."""
    for q in SAME.get(slug, []):
        block = next(b for b in re.finditer(r'<details class="eq"[^>]*>.*?</details>\s*', page, re.S)
                     if q in re.sub(r"<[^>]+>", "", b[0].split("</summary>")[0]))
        page = page[:block.start()] + page[block.end():]
    if slug in SAME:
        n = iter(range(1, 100))
        page = re.sub(r"(<summary>)Q\d+\b", lambda m: f"{m[1]}Q{next(n)}", page)
    return page


def apply(page, slug):
    if slug not in DATA or START in page:
        return page
    block = (START + "\n  <h3>Past paper questions</h3>\n  <p>Real 0455 Paper 2 questions, put in our own words, each with its session and paper. "
             "Check the source paper and mark scheme for the full detail. Several also appear on related lessons.</p>\n  "
             + "\n\n  ".join(DATA[slug])
             + "\n\n  <h3>Practice questions</h3>\n  <p>The questions below are our own, written for practice.</p>\n")
    page = _practice(page, slug)
    # after the colour key, which serves both sets; the aims explorer fills its questions by script and has no key
    exam = re.search(r'<section id="exam"[^>]*>.*?</section>', page, re.S)
    m = re.search(r'<div class="key">.*?</div>', exam[0], re.S)
    if m:
        at = exam.start() + m.end()
    else:
        at = exam.start() + exam[0].index('<div id="exq">')
        block = block.replace(START, START + "\n  " + KEY, 1)
    return page[:at] + "\n  " + block + page[at:]
