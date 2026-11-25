"""Whole lesson sections added to existing pages: moral hazard (7.4), negative income tax and universal basic income (8.2.5)
and monetary policy and the current account (6.5.2).

build.py calls apply(), which puts each part at the end of the matching tab and adds the activity code to the page script,
so rebuilding a page with its own builder keeps these sections. Past paper questions are reworded.
"""
import json
import re


def table(head, rows):
    return ('<div class="tw" style="overflow-x:auto"><table class="t" style="min-width:0"><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>")


def tip(title, body):
    return f'<div class="tip"><b class="h">{title}</b>{body}</div>'


def points(*texts, kind="k", start=1):
    return " ".join(f'<span class="mk {kind}" data-t="{start + i}">{t}</span>' for i, t in enumerate(texts))


def written(marks, command, question, plan, answer, warn):
    return (f'<details class="eq"><summary><span class="cmd">{command}</span> <span class="mark">{marks}</span> {question}</summary><div class="body">'
            + tip("Plan before writing", plan) + f'<div class="ans">{answer}</div><div class="warn"><b class="h">Common mistake</b>{warn}</div></div></details>')


def real(src, question, opts, a, why):
    return dict(q=f'<span class="src">{src}</span> {question}', opts=opts, a=a, why=why)


def classify(el, prompt, buckets, items, done):
    return f'Lib.classify($("#{el}"), {json.dumps(dict(prompt=prompt, buckets=[dict(label=b) for b in buckets], items=[dict(text=t, b=b) for t, b in items], done=done))});'


def quiz(el, qs):
    return f'Lib.quiz($("#{el}"), {json.dumps(dict(qs=qs), ensure_ascii=False)});'


def chain(el, label, nodes, caps):
    return f'xChain("#{el}", {json.dumps(label)}, {json.dumps(nodes)}, {json.dumps(caps)});'


CHAIN_JS = r'''function xChain(el, label, nodes, caps) {
  const draw = (s) => nodes.map((t, i) => {
    const v = Math.max(0, Math.min(1, s.k - i)); if (v <= 0) return "";
    const y = 8 + i * 56;
    return SV.rect(30, y, 700, 40, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) }) +
      (i ? SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v)) : "");
  }).join("");
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw, tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}'''

# ================================================================ 7.4.6 asymmetric information and moral hazard
MORAL = dict(
    learn='<h2>Asymmetric information and moral hazard</h2>'
    '<p><b>Asymmetric information</b> exists when one party to a transaction knows more than the other. <b>Moral hazard</b> occurs when a person or firm is likely to take more risk, or less care, because someone else bears some or all of the cost, and that other party cannot easily observe or control the behaviour.</p>'
    + table(["", "Moral hazard", "Adverse selection"], [
        ["When the problem arises", "<b>After</b> the agreement is made", "<b>Before</b> the agreement is made"],
        ["What is hidden", "How carefully someone behaves", "What type of customer or product it is"],
        ["Insurance example", "A driver with full theft cover may be less careful about where the car is parked", "People who know they are high risk may be the most likely to buy cover"]])
    + '<h3>Why it can cause market failure</h3><p>The person taking the decision pays less than the full cost of the risk, so they may take more of it than is socially efficient. Resources may be used to repair avoidable damage. Insurers may respond by raising premiums for everyone, or by refusing to offer cover, so some careful customers may be priced out of the market.</p>'
    + '<h3>Where to look for it</h3>'
    + table(["Setting", "Who may take more risk", "Who bears the cost"], [
        ["Insurance", "The policy holder", "The insurer and other policy holders"],
        ["Free or heavily subsidised healthcare", "A patient who takes less care of their health", "Taxpayers"],
        ["Bank rescues", "Banks that expect to be saved because they are very large", "Taxpayers"],
        ["Employment", "A worker whose effort is hard to monitor", "The employer"],
        ["Managers and shareholders", "Managers taking risks with owners' money (the principal-agent problem)", "Shareholders"]])
    + '<h3>Ways to reduce it</h3>'
    + table(["Response", "How it may help", "Limit"], [
        ["Excess or co-insurance", "The customer pays part of any loss, so has a reason to take care", "Poorer customers may be unable to pay their share"],
        ["No-claims discount", "Careful behaviour is rewarded with a lower premium", "Small claims may go unreported"],
        ["Monitoring, such as a black box in a car", "Behaviour becomes easier to observe", "Costs money and raises privacy concerns"],
        ["Conditions and regulation, such as capital rules for banks", "Limits the amount of risk that can be taken", "Rules may be costly to enforce or avoided"],
        ["Performance-related pay", "Aligns the agent's interest with the principal's", "May encourage short-term risk-taking"]])
    + tip("Real world, and how to use it", "During the 2008 financial crisis several governments rescued large banks. Critics argued that an expected rescue could encourage riskier lending in future. Use it to show that the same policy may prevent a collapse today and create moral hazard later."),
    watch='<h2>How moral hazard develops</h2><div id="x-mh-step"></div>',
    practise='<h2>Moral hazard or adverse selection?</h2><div id="x-mh-cl" class="card"></div>',
    exam='<h2>Moral hazard: past paper multiple choice (reworded)</h2><div id="x-mh-qz"></div><h2>Moral hazard: practice question (our own)</h2>'
    + written("8 marks", "Analyse", "Analyse how moral hazard may lead to an inefficient allocation of resources in an insurance market.",
        "Define moral hazard and link it to asymmetric information. Then follow one chain from the behaviour to the misallocation. Add a limit to each step.",
        "<p>" + points("Moral hazard can occur when one party takes greater risks because another party bears the cost.", "It is likely to arise where information is asymmetric, because an insurer may not easily observe how carefully a customer behaves once cover has been bought.") + "</p>"
        "<p>" + points("Moral hazard may lead to an inefficient allocation of resources because an insured driver is likely to face a lower private cost of carelessness than the full cost to society.", "The driver may therefore take less care, so thefts and accidents could become more frequent than is efficient.", "More resources may then be used on repairs and replacements that care could have avoided.", kind="k", start=3)
        + " <i>This may be less likely where a loss still brings inconvenience or injury that insurance may not cover.</i></p>"
        "<p>" + points("Moral hazard may also worsen resource allocation through higher premiums.", "As claims rise, insurers could charge all customers more, so some careful customers may leave although the cover was worth its true cost to them.", kind="a", start=6)
        + " <i>The effect is likely to be smaller if an excess or a no-claims discount gives customers a reason to take care.</i></p>"
        "<p>" + points("Overall, the misallocation is likely to be greatest when behaviour is hard to monitor and the customer bears very little of any loss.", kind="a", start=8) + "</p>",
        "Describing adverse selection instead. Moral hazard is about behaviour after the agreement."),
    tips='<h2>Moral hazard: top tips</h2><ul><li>Name all three parts: a change in behaviour, someone else bearing the cost, and information that is asymmetric.</li><li>Check the timing: after the agreement is moral hazard; before it is adverse selection.</li><li>For evaluation, ask how far the response changes the incentive, and what it costs to monitor.</li></ul>',
    js=[chain("x-mh-step", "How moral hazard develops", ["A driver buys full insurance", "The insurer cannot easily observe the driver's care", "The driver may now take less care", "Claims are likely to rise", "Premiums may rise and some careful drivers leave"],
              ["The agreement moves the cost of a loss from the driver to the insurer.", "Information is <b>asymmetric</b>: the driver knows more about their own behaviour.", "Bearing less of the cost, the driver may park or drive less carefully. This is <b>moral hazard</b>.", "More risk-taking is likely to mean more losses.", "Resources may be misallocated and the market may shrink."]),
        classify("x-mh-cl", "Does the problem come from behaviour after the deal, or hidden information before it?", ["Moral hazard (after)", "Adverse selection (before)"], [
            ("A cyclist locks their bike less carefully once it is insured", 0), ("People who expect to be ill are the keenest to buy health cover", 1),
            ("A bank lends more riskily because it expects to be rescued", 0), ("A seller knows a used car is faulty but the buyer does not", 1),
            ("A manager takes large risks with shareholders' money", 0), ("A lender attracts mainly high-risk borrowers when it raises its interest rate", 1)],
            "After the deal: moral hazard. Before it: adverse selection."),
        quiz("x-mh-qz", [
            real("May/June 2023 · 9708/32 · Q7", "Which could help to overcome moral hazard?", ["The same insurance premium for everyone in an age group", "Insurance contracts in which the insurer and the customer share any loss", "Unconditional financial support for banks to protect jobs", "Guaranteed jobs for bank managers"], 1, "Sharing the loss gives the customer a reason to take care. The other choices remove or leave unchanged the cost of taking risks."),
            real("Oct/Nov 2023 · 9708/32 · Q8", "Which is not an example of moral hazard?", ["People more likely to become unemployed are more likely to take training", "People with free dental care look after their teeth less well", "People insured against car theft park in higher-crime areas", "People receiving unemployment benefit are less likely to retrain"], 0, "Training reduces the risk. The others show less care because someone else carries part of the cost."),
            real("May/June 2025 · 9708/32 · Q4", "When might moral hazard occur?", ["A consumer lacks full information about a product", "A person's activity harms someone else", "A person takes a risk knowing that someone else bears it", "A seller has more information than a buyer"], 2, "Moral hazard is risk-taking when another party carries the cost.")])])

# ================================================================ 8.2.5 negative income tax and universal basic income
NIT = dict(
    learn='<h2>Negative income tax and universal basic income</h2><p>Both aim to give a minimum income. They differ in <b>who receives money</b> and in how it changes as earnings rise.</p>'
    '<h3>Negative income tax (NIT)</h3><p>The government sets a guaranteed income and a rate at which it is withdrawn. People earning below the <b>break-even income</b> receive a payment through the tax system. The payment falls as earnings rise.</p>'
    '<p><b>Payment = guaranteed amount − (withdrawal rate × earnings)</b>, while this is above zero.<br><b>Break-even income = guaranteed amount ÷ withdrawal rate.</b></p>'
    + table(["Earnings", "Payment (guarantee $6000, withdrawal rate 50%)", "Income after payment"], [["$0", "$6000", "$6000"], ["$4000", "$4000", "$8000"], ["$8000", "$2000", "$10 000"], ["$12 000 (break-even)", "$0", "$12 000"]])
    + '<h3>Universal basic income (UBI)</h3><p>A regular payment to <b>every</b> person, with <b>no means test</b> and <b>no work requirement</b>. It is not withdrawn as earnings rise, although higher taxes may be needed to pay for it.</p>'
    + table(["", "Negative income tax", "Universal basic income", "Means-tested benefit"], [
        ["Who receives it", "Those below break-even income", "Everyone", "Those who claim and qualify"],
        ["As earnings rise", "Payment falls gradually", "Payment unchanged", "Payment may be withdrawn quickly"],
        ["Likely cost", "Lower than a UBI with the same guarantee, if taxes are unchanged", "High", "Often the lowest, but costly to run for each claimant"],
        ["Poverty trap", "Weaker if the withdrawal rate is low", "No withdrawal, though taxes raise the marginal rate", "Can be severe"],
        ["Take-up and stigma", "Could be high if automatic", "Likely to be high, with little stigma", "Some people may not claim"]])
    + '<h3>Evaluation</h3><p>Either policy could reduce poverty and simplify a complicated benefit system. Against this, the guarantee may reduce the incentive to work (an income effect), and the taxes needed to fund it may reduce it further. A high guarantee with a low withdrawal rate helps work incentives at the margin but raises the break-even income, so more people receive payments and the cost is likely to rise. Neither may meet extra needs such as disability without further benefits.</p>'
    + tip("Real world, and how to use it", "Finland paid 2000 unemployed people €560 a month in 2017 and 2018 without withdrawing it when they found work. Reported wellbeing improved and the employment effect was small. Use it with care: it covered only unemployed people and ran for two years, so it may not show how a full UBI would work. Alaska's yearly dividend to residents is another partial example. Negative income tax experiments in the United States in the 1960s and 1970s found some fall in hours worked."),
    watch='<h2>What happens when someone earns more under a negative income tax</h2><div id="x-nit-step"></div>',
    explore='<h2>Lab: design a negative income tax</h2><p>Move the sliders. Watch the break-even income and how much of each extra dollar a worker keeps.</p><div class="card"><div id="x-nit-g"></div><div id="x-nit-t"></div><div id="x-nit-y"></div><div class="verdict" id="x-nit-v"></div></div>',
    practise='<h2>Which policy is it?</h2><div id="x-nit-cl" class="card"></div>',
    exam='<h2>Universal basic income: past paper multiple choice (reworded)</h2><p>We found no question naming negative income tax in the A Level papers searched.</p><div id="x-nit-qz"></div><h2>Practice question (our own)</h2>'
    + written("8 marks", "Assess", "Assess whether a negative income tax is likely to be better than a universal basic income at reducing poverty without large costs to work incentives.",
        "Define both. Compare them on targeting, cost and incentives. Judge, and say what the judgement depends on.",
        "<p>" + points("A negative income tax pays those below a break-even income, with the payment falling as earnings rise.", "A universal basic income pays everyone the same amount without a means test.") + "</p>"
        "<p>" + points("A negative income tax is likely to be better at reducing poverty at a given cost because payments go mainly to people with low incomes.", "Less tax revenue may then be needed than for a universal payment of the same size, so tax rates could be lower.", start=3)
        + " <i>This advantage may be smaller if incomes are hard to measure, as with a large informal economy, or if payments arrive late.</i></p>"
        "<p>" + points("A negative income tax may weaken work incentives for those receiving it because part of each extra dollar is lost as the payment is withdrawn.", "A universal basic income is not withdrawn, so it could create less of a poverty trap, although the higher taxes needed to fund it may discourage work elsewhere.", kind="a", start=5)
        + " <i>The size of both effects is likely to depend on the rates chosen and on how strongly people respond to them.</i></p>"
        "<p>" + points("A negative income tax is likely to be preferable where the government's budget is limited and incomes can be measured accurately.", "A universal basic income could be preferable where take-up and administration are the main problems and the extra tax can be raised without large damage to incentives.", kind="a", start=7) + "</p>",
        "Saying a universal basic income has no effect on incentives. The payment is not withdrawn, but it may still reduce the need to work and has to be funded."),
    tips='<h2>NIT and UBI: top tips</h2><ul><li>Universal means everyone: if there is an income test, it is not a UBI.</li><li>Calculate break-even income as guarantee ÷ withdrawal rate.</li><li>Evaluate three things: cost, targeting and work incentives. Improving one may worsen another.</li></ul>',
    js=[chain("x-nit-step", "Earning more under a negative income tax", ["Guarantee $6000, withdrawal rate 50%", "Earns $0: payment $6000, total $6000", "Earns $4000: payment $4000, total $8000", "Earns $8000: payment $2000, total $10 000", "Earns $12 000: payment $0, break-even"],
              ["The government sets a guaranteed income and a withdrawal rate.", "With no earnings, the person receives the full guarantee.", "Each extra dollar earned reduces the payment by 50 cents, so total income still rises.", "Work continues to pay, although only half of each extra dollar is kept.", "At <b>break-even income</b> the payment stops: $6000 ÷ 0.5."]),
        r'''(function () {
  let g = 6000, t = 50, y = 4000;
  const money = (v) => "$" + Math.round(v).toLocaleString("en-US");
  const paint = () => { const pay = Math.max(0, g - (t / 100) * y), even = g / (t / 100);
    $("#x-nit-v").textContent = `Break-even income ${money(even)}. Earning ${money(y)}, the payment is ${money(pay)} and total income is ${money(y + pay)}. ` + (y < even ? `The worker keeps ${100 - t} cents of the next dollar before other taxes.` : "Above break-even, no payment is made."); };
  Lib.slider($("#x-nit-g"), { id: "x-nit-gi", label: "Guaranteed income ", min: 2000, max: 12000, step: 500, value: g, fmt: money, onInput: (v) => { g = v; paint(); } });
  Lib.slider($("#x-nit-t"), { id: "x-nit-ti", label: "Withdrawal rate ", min: 20, max: 100, step: 5, value: t, fmt: (v) => v + "%", onInput: (v) => { t = v; paint(); } });
  Lib.slider($("#x-nit-y"), { id: "x-nit-yi", label: "Worker's earnings ", min: 0, max: 40000, step: 500, value: y, fmt: money, onInput: (v) => { y = v; paint(); } });
})();''',
        classify("x-nit-cl", "Which policy does each describe?", ["Negative income tax", "Universal basic income", "Means-tested benefit"], [
            ("Every adult receives the same monthly payment", 1), ("A payment through the tax system that falls gradually below a break-even income", 0), ("Households must apply and show their income is low", 2),
            ("No payment is withdrawn when someone takes a job", 1), ("Break-even income equals the guarantee divided by the withdrawal rate", 0), ("A housing allowance paid only to claimants who qualify", 2)],
            "Universal: everyone. NIT: tapered through the tax system. Means-tested: claim and qualify."),
        quiz("x-nit-qz", [
            real("Oct/Nov 2023 · 9708/32 · Q12", "What is the likely economic result of a universal basic income?", ["It neither reduces the incentive to work nor improves equality", "It does not reduce the incentive to work but improves equality", "It reduces the incentive to work but does not improve equality", "It reduces the incentive to work and improves equality"], 3, "The expected answer: an income paid without work may reduce the incentive to work, and a flat payment is a larger share of low incomes, so equality is likely to improve. How large each effect is would depend on the size of the payment and how it is funded.")])])

# ================================================================ 6.5.2 monetary policy and the current account
MONEY = dict(
    learn='<h2>Monetary policy and the current account</h2><p><b>Monetary policy</b> uses interest rates, the money supply and credit regulations to influence spending. It can change a current account balance in two ways that may work <b>against each other</b>.</p>'
    + table(["Contractionary monetary policy", "Likely effect on a deficit"], [
        ["<b>Expenditure-reducing:</b> higher interest rates, slower money supply growth or tighter credit rules reduce consumption and investment", "Spending on imports is likely to fall, which may reduce the deficit"],
        ["<b>Inflation:</b> lower total demand may slow the rise in prices", "Exports could become more price competitive over time"],
        ["<b>Exchange rate:</b> higher interest rates may attract money from abroad, so a floating currency may appreciate", "Exports become dearer and imports cheaper, which may widen the deficit"]])
    + '<p><b>Expansionary monetary policy</b> may lower the exchange rate and so switch spending towards domestic goods, but the extra spending is also likely to raise demand for imports.</p>'
    '<h3>The four policy types compared</h3>'
    + table(["Policy", "How it may reduce a deficit", "Type", "Main limit"], [
        ["Fiscal", "Higher taxes or lower government spending reduce spending on imports", "Expenditure-reducing", "Lower output and higher unemployment"],
        ["Monetary", "Higher interest rates and tighter credit reduce spending", "Expenditure-reducing", "The currency may appreciate"],
        ["Supply-side", "Higher productivity and quality make domestic goods more competitive", "Mainly expenditure-switching", "Slow and costly, with uncertain results"],
        ["Protectionist", "Tariffs and quotas make imports dearer or scarcer", "Expenditure-switching", "Retaliation and higher prices"]])
    + '<h3>How far could monetary policy work?</h3><p>It is likely to be more effective when imports rise strongly with income, and when export demand is price inelastic so that an appreciation does little harm. It may be weaker if consumers lack confidence already, if a central bank has to keep interest rates focused on inflation, or if the deficit comes from poor quality and low productivity.</p>'
    + tip("Real world, and how to use it", "Turkey cut interest rates in 2021 while inflation was high, and its currency fell sharply. A cheaper currency may help exports, but dearer imported energy and materials can offset the gain. Use it to show that the exchange rate effect does not guarantee a better current account."),
    watch='<h2>Higher interest rates: two effects on a deficit</h2><div id="x-mp-a"></div><div id="x-mp-b"></div>',
    practise='<h2>Which way does it push the deficit?</h2><div id="x-mp-cl" class="card"></div>',
    exam='<h2>Monetary policy: past paper multiple choice (reworded)</h2><div id="x-mp-qz"></div><h2>Practice question (our own)</h2>'
    + written("8 marks", "Explain and consider", "Explain how contractionary monetary policy might affect a deficit on the current account and consider whether it is likely to reduce the deficit.",
        "3 knowledge, 3 analysis, 2 evaluation. Define both terms, follow the spending chain, then the exchange rate chain, then judge.",
        "<p>" + points("Contractionary monetary policy uses higher interest rates, a slower growth of the money supply or tighter credit rules to reduce total demand.", "A current account deficit occurs when money flowing out on trade, income and transfers is greater than money flowing in.", "The policy is mainly expenditure-reducing.") + "</p>"
        "<p>" + points("Contractionary monetary policy might reduce the deficit because higher interest rates are likely to make borrowing dearer and saving more attractive.", "Households and firms may then spend less, including on imports.", "If exports are unchanged, lower import spending could reduce the deficit.", start=4)
        + " <i>The fall in imports may be small if demand for them depends little on income or credit.</i></p>"
        "<p>" + points("However, contractionary monetary policy might widen the deficit if higher interest rates attract money from abroad and the currency appreciates, making exports dearer and imports cheaper, which may lower export revenue where demand is price elastic.", kind="a", start=7) + "</p>"
        "<p>" + points("Overall, it is likely to reduce the deficit only if the fall in spending on imports outweighs the effect of a higher exchange rate, so it may work better alongside supply-side policies that improve competitiveness.", kind="a", start=8) + "</p>",
        "Giving only the fall in imports. The exchange rate may move the current account the other way."),
    tips='<h2>Monetary policy and the current account: top tips</h2><ul><li>Name the policy tool, then say whether it reduces or switches spending.</li><li>Higher interest rates have two chains: less spending, and a possibly higher exchange rate.</li><li>End with what the result depends on: price elasticities, import spending, confidence and the exchange rate system.</li></ul>',
    js=[chain("x-mp-a", "The spending effect of higher interest rates", ["Interest rates rise", "Borrowing is dearer and saving more attractive", "Consumption and investment may fall", "Spending on imports is likely to fall", "The deficit may narrow"],
              ["First chain: the <b>spending</b> effect.", "Households and firms face a higher cost of borrowing.", "Total demand is likely to fall.", "Some of the lost spending would have gone on imports.", "Taken alone, this chain is likely to improve the current account."]),
        chain("x-mp-b", "The exchange rate effect of higher interest rates", ["Interest rates rise", "Money may flow in from abroad", "The currency may appreciate", "Exports become dearer and imports cheaper", "The deficit may widen"],
              ["Second chain: the <b>exchange rate</b> effect.", "Savers abroad may seek the higher return.", "Demand for the currency is likely to rise.", "Price competitiveness may fall.", "This chain works against the first. The net effect depends on which is stronger."]),
        classify("x-mp-cl", "Taken on its own, which way does each push a current account deficit?", ["Narrows the deficit", "Widens the deficit"], [
            ("Tighter credit rules cut borrowing to buy imported cars", 0), ("Higher interest rates raise the value of the currency", 1), ("Lower interest rates raise consumer spending on imports", 1),
            ("Lower interest rates reduce the value of the currency and export demand is price elastic", 0), ("Higher interest rates reduce household spending", 0), ("A rapid growth of credit raises demand for imported goods", 1)],
            "Less spending or a more competitive currency tends to narrow the deficit; more spending or a stronger currency tends to widen it."),
        quiz("x-mp-qz", [
            real("May/June 2022 · 9708/13 · Q28", "Which measure to correct a current account deficit is expenditure-reducing?", ["A cut in interest rates", "A revaluation of the currency", "A rise in direct taxes", "The introduction of foreign exchange controls"], 2, "Higher direct taxes lower disposable income and so spending. A cut in interest rates is likely to raise spending.")])])

PAGES = {
    "causes-of-market-failure": [MORAL],
    "externalities-social-costs-benefits": [MORAL],
    "redistribution-policies-benefits": [NIT],
    "equity-and-redistribution": [NIT],
    "as-correcting-current-account-imbalances": [MONEY],
}

START = "<!-- extra lesson -->"


def tab_end(page, tab):
    """Index of the closing tag of the tab's <section>, allowing for sub-sections inside it."""
    a = page.index(f'<section id="{tab}"')
    depth = 0
    for t in re.finditer(r"<(/?)section\b", page[a:]):
        depth += -1 if t[1] else 1
        if depth == 0:
            return a + t.start()
    raise ValueError(tab)


def apply(page, slug):
    if slug not in PAGES or START in page:
        return page
    js = [CHAIN_JS]
    for topic in PAGES[slug]:
        for tab in ("learn", "watch", "explore", "practise", "exam", "tips"):
            if tab in topic:
                i = tab_end(page, tab)
                page = page[:i] + f'{START}<div class="kit">{topic[tab]}</div>\n' + page[i:]
        js += topic["js"]
    # the activities join the page's main script, so the Basic/Full splitter moves them with their panels
    main = max(re.finditer(r"<script>(.*?)</script>", page, re.S), key=lambda m: len(m[1]))
    return page[:main.end(1)] + "\n" + "\n".join(js) + "\n" + page[main.end(1):]
