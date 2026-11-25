"""Past paper questions for IGCSE Computer Science lessons that had only our own exam questions.

igcs_past.json holds them: 0478 questions in our own words, with our answers split into mark points. build.py calls
apply(), which puts them at the top of the Exam tab. The two's complement page has no Exam tab, so they end its
Question types tab; pages that write their Exam tab by script get them added by script afterwards.
"""
import json
import re
from pathlib import Path

DATA = json.loads((Path(__file__).parent / "igcs_past.json").read_text(encoding="utf-8"))
START = "<!-- past papers -->"
OTHER_TAB = {"twos-complement-questions": "types"}
# a practice question, one line of the page script, that asks the same thing as a past paper question
REPEATS = {"ig-cs-assembly-languages": 'q: "Give two disadvantages of writing in assembly language."'}


def apply(page, slug):
    if slug not in DATA or START in page:
        return page
    block = (START + '<div class="kit"><h2>Past paper questions</h2>'
             "<p>Real 0478 questions, put in our own words, each with its session and paper. Each underlined phrase is "
             "a mark point. Check the source paper and mark scheme for the full detail.</p>\n"
             + "\n".join(DATA[slug]) + "</div>\n")
    if slug in REPEATS:
        page = "\n".join(line for line in page.split("\n") if REPEATS[slug] not in line)
    if slug in OTHER_TAB:
        tab = re.search(rf'<section id="{OTHER_TAB[slug]}"[^>]*>.*?(?=</section>)', page, re.S)
        return page[:tab.end()] + block + page[tab.end():]
    tab = re.search(r'<section id="exam"[^>]*>', page)
    if not page[tab.end():].lstrip().startswith("</section>"):
        return page[:tab.end()] + "\n" + block + page[tab.end():]
    # the empty tab is filled with innerHTML, so add ours once that has run
    text = json.dumps(block, ensure_ascii=False).replace("</", "<\\/")
    js = f'document.getElementById("exam").insertAdjacentHTML("afterbegin", {text});'
    main = max(re.finditer(r"<script>(.*?)</script>", page, re.S), key=lambda s: len(s[1]))
    return page[:main.end(1)] + "\n" + js + "\n" + page[main.end(1):]
