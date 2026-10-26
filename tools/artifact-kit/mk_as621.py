"""AS CS 6.2.1: data validation. Run: python3 tools/artifact-kit/mk_as621.py"""
from ascs import *

def is_valid_trace(s):
    idx, dots, ats, others, valid = 1, 0, 0, 0, True; rows = [("", "", 0, 0, 0, "TRUE")]
    while True:
        c = s[idx - 1]
        if c == ".": dots += 1
        elif c == "@":
            ats += 1
            if ats > 1: valid = False
        else: others += 1
        if dots > 1 and ats == 0: valid = False
        else: idx += 1
        rows.append((idx - (0 if valid is False and False else 1) if False else None, c, dots, ats, others, "FALSE" if not valid else ""))
        if idx > len(s) or not valid: break
    final = not (dots >= 1 and ats == 1 and others > 8)
    if final: valid = False
    return rows, valid, (dots, ats, others)

def trace_rows(s):
    idx, dots, ats, others, valid = 1, 0, 0, 0, True; out = [(" ", " ", 0, 0, 0, "TRUE")]; prev = (0, 0, 0, True)
    while True:
        c = s[idx - 1]; cur = idx
        if c == ".": dots += 1
        elif c == "@":
            ats += 1
            if ats > 1: valid = False
        else: others += 1
        if dots > 1 and ats == 0: valid = False
        else: idx += 1
        out.append((cur, c, dots if dots != prev[0] else "", ats if ats != prev[1] else "", others if others != prev[2] else "", "FALSE" if (not valid and prev[3]) else ""))
        prev = (dots, ats, others, valid)
        if idx > len(s) or not valid: break
    if not (dots >= 1 and ats == 1 and others > 8): valid = False
    return out, valid

IV_ROWS, IV_RES = trace_rows("Liz.123@big@net")
assert IV_RES is False and IV_ROWS[-1][1] == "@" and IV_ROWS[-1][5] == "FALSE"
assert [r[4] for r in IV_ROWS if r[4] != ""][-1] == 9
IV_TABLE = '<div class="tw"><table class="t mono"><tr><th>Index</th><th>NextChar</th><th>Dots</th><th>Ats</th><th>Others</th><th>Valid</th></tr>' + "".join(f"<tr><td>{a}</td><td>{('&#39;' + b + '&#39;') if b.strip() else ''}</td><td>{c if c != 0 or i == 0 else ''}</td><td>{d if d != 0 or i == 0 else ''}</td><td>{e if e != 0 or i == 0 else ''}</td><td>{f}</td></tr>" for i, (a, b, c, d, e, f) in enumerate(IV_ROWS)) + "</table></div>"

def check_digit(n):
    return sum(int(x) for x in str(n)) % 10
assert check_digit(4162) == 3

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Data validation</b> is an automatic check that data entered is <b>reasonable and sensible</b>, within specified bounds, in the right format: it protects the <b>integrity</b> of data but does <b>not</b> prove the data is correct (a valid date of birth can still be the wrong date). The checks you need are <b>range</b>, <b>limit</b>, <b>length</b>, <b>type</b>, <b>presence</b>, <b>format</b>, <b>existence</b> (look-up) and <b>check digit</b>. For each check you must say <b>what it tests</b> and apply it to the data in the question, for example a date of birth. Validation is different from <b>verification</b> (checking that data matches the original): validation checks the data is sensible, verification checks it is the same as the source. A check digit is calculated from the other digits, appended to the number, and recalculated on entry to detect errors.</p></div>

  <h2>1 · Validation checks</h2>
  <div class="tw"><table class="t">
    <tr><th>Check</th><th>What it tests</th><th>Example: date of birth 05/07/2010</th></tr>
    <tr><td><b>Presence</b></td><td>Data has been entered (not left blank)</td><td>The field cannot be left empty</td></tr>
    <tr><td><b>Range</b></td><td>Value lies between a lower and an upper limit (both ends)</td><td>Between 1 January 1900 and today's date; month 1 to 12; day 1 to the month end</td></tr>
    <tr><td><b>Limit</b></td><td>Value is above or below one limit only</td><td>Not after today's date</td></tr>
    <tr><td><b>Length</b></td><td>The number of characters is correct (or within limits)</td><td>Exactly 10 characters (dd/mm/yyyy)</td></tr>
    <tr><td><b>Format</b></td><td>Characters follow a pattern of letters, numbers and symbols</td><td>Must be dd/mm/yyyy</td></tr>
    <tr><td><b>Type</b></td><td>Data is of the expected data type</td><td>The data type must be DATE (or numeric for a quantity)</td></tr>
    <tr><td><b>Existence (look-up)</b></td><td>Data is one of a list of possible values (or exists in the system)</td><td>Must be one of "Red", "Yellow", "Blue"; a customer ID that exists</td></tr>
    <tr><td><b>Check digit</b></td><td>An extra digit calculated from the others catches errors in data entry</td><td>See below</td></tr>
  </table></div>

  <h2>2 · A check digit</h2>
  <p>In the method used in the exam, the check digit is the <b>remainder when the sum of the digits is divided by 10</b>. For 4162: 4 + 1 + 6 + 2 = 13, remainder 3, so the new number is <b>41623</b>. On entry the computer recalculates the digit from the other digits and rejects the input if it does not match. This method detects <b>single-digit errors</b>: 41633 is rejected. It does <b>not</b> catch errors that keep the sum the same: two digits that swap, or changes whose effect cancel out.</p>

  <h2>3 · Validation does not mean correct</h2>
  <p>Validation checks that data is <b>reasonable</b> and within bounds; it does not check that accurate data was entered. Verification checks that the data matches what was given; it does not check that the original data was accurate. So data can still be wrong after validating and verifying, for example when the original document itself was wrong.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Describing a check without applying it to the data in the question. Say "the date of birth must be between 1900 and today", not "checks the range".</li>
    <li>Mixing range and limit: range has two ends, limit has one.</li>
    <li>Saying validation makes sure the data is correct. It makes sure it is sensible.</li>
    <li>Confusing validation with verification: double entry and visual checks are verification.</li>
    <li>Saying a check digit "makes sure the number is right". It detects most single-digit errors but not all errors.</li>
  </ul>
'''

watch = '''
  <h2>1 · A range check</h2>
  <div id="stA"></div>
  <h2>2 · Several checks on one field</h2>
  <div id="stB"></div>
  <h2>3 · Generating and checking a check digit</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Check a date of birth</h2>
  <p>Type a date and see which validation checks it passes.</p>
  <div class="card"><input id="vIn" type="text" value="05/07/2010" style="font:inherit;padding:6px 10px;border:1px solid var(--border);border-radius:8px"><div id="vOut"></div></div>
  <h2>Lab 2 · Check digit</h2>
  <div class="card"><div id="cS"></div><div id="cV" class="verdict"></div></div>
  <h2>Lab 3 · Which check?</h2>
  <div class="card"><div id="wB" class="btnrow"></div><div id="wO"></div></div>
'''

_pr, _prjs = PR(["Which validation check?", "Validation or verification?", "Match the check to its description", "Put the check digit steps in order", "Working out", "Multiple choice"],
  ("Which validation check does it describe?", ["Range", "Presence", "Length", "Format", "Existence"], [("The date of birth must be between 1900 and today", 0), ("The name field cannot be left blank", 1), ("The password must be exactly 8 characters", 2), ("A code must be two letters, a number then a symbol", 3), ("The colour must be Red, Yellow or Blue", 4), ("A mark must be from 0 to 100", 0)], "Range, presence, length, format, existence."),
  ("Validation or verification?", ["Validation", "Verification"], [("Presence check", 0), ("Double entry", 1), ("Range check", 0), ("Visual check", 1), ("Format check", 0), ("Comparing entered data with the original document", 1)], "Validation: sensible. Verification: same as the original."),
  [["Range check", "Between a lower and an upper limit"], ["Limit check", "Above or below one limit only"], ["Length check", "Correct number of characters"], ["Presence check", "Data has been entered"], ["Check digit", "A digit calculated from the others"]],
  ("Put the check digit steps in order.", ["Add the digits of the original number", "Divide the sum by 10 and take the remainder", "Append the remainder to the number", "On entry, recalculate from the original digits", "Reject the input if the digits do not match"], "Sum, remainder, append, recalculate, compare."),
  [{"q": "Find the check digit for 5384 (sum of digits, remainder when divided by 10).", "a": 0, "unit": "", "tol": 0.01, "hint": "5 + 3 + 8 + 4 = 20.", "sol": "<b>0</b>: the new number is 53840."}, {"q": "Find the check digit for 4162 (the worked example).", "a": 3, "unit": "", "tol": 0.01, "hint": "13 mod 10.", "sol": "<b>3</b>."}, {"q": "A range check allows ages 5 to 18 inclusive. How many whole-number ages are allowed?", "a": 14, "unit": "", "tol": 0.01, "hint": "18 − 5 + 1.", "sol": "<b>14</b>."}, {"q": "A length check requires exactly 10 characters. How many of 'dd/mm/yyyy' characters is that?", "a": 10, "unit": "", "tol": 0.01, "hint": "2 + 1 + 2 + 1 + 4.", "sol": "<b>10</b>."}, {"q": "The number 41633 is entered. Its first four digits are 4163. What check digit should it have (and is 41633 accepted? Answer the correct check digit).", "a": 4, "unit": "", "tol": 0.01, "hint": "4 + 1 + 6 + 3 = 14.", "sol": "<b>4</b>: 41633 has 3, so it is rejected."}],
  [("A range check tests:", ["Between two limits", "Blank fields", "Data type only", "Spelling"], 0, "Between limits."), ("A presence check ensures:", ["Data has been entered", "The data is correct", "The data matches the paper", "A back-up exists"], 0, "Entered."), ("Validation checks the data is:", ["Reasonable", "The same as the original", "Encrypted", "Copied"], 0, "Reasonable."), ("A check digit detects:", ["Single-digit errors", "All errors", "Viruses", "Copying"], 0, "Single-digit errors."), ("A format check tests:", ["The pattern of characters", "The number of rows", "The speed", "The author"], 0, "Pattern."), ("Valid data can still be:", ["Wrong", "Impossible", "Blank", "Encrypted"], 0, "Wrong.")],
  [("Presence", "Not left blank."), ("Range", "Between two limits."), ("Limit", "One limit only."), ("Length", "Number of characters."), ("Format", "Pattern of characters."), ("Type", "Right data type."), ("Existence", "In a list of values."), ("Check digit", "Sum of digits mod 10, appended.")])

real = RWNOTE + (
rw("A sign-up form", "The form refuses to continue if the email is blank (presence), has no @ (format) or the password is too short (length).", "validation protects integrity.") +
rw("A bar code", "The last digit of a bar code is a check digit; a scanner recalculates it and beeps if a digit was misread.", "check digit.") +
rw("Entering a date of birth", "The system rejects 31/02/2010 (not a valid date) but cannot know whether 05/07/2010 is really your birthday.", "validation does not prove accuracy.") +
rw("A drop-down for country", "You can only choose from a list, so you cannot make a spelling mistake: an existence (look-up) check.", "existence check.") +
rw("A mark entry screen", "A teacher cannot type 150 for a test out of 100: a range check.", "range check.")
)

where = [
  ("M/J 2021", "11, 13", "6", "3", "Name the validation check performed by three algorithms"),
  ("O/N 2021", "11, 13", "2(b)(i)", "2", "How data validation helps to protect integrity, with an example"),
  ("O/N 2022", "12", "4(a), (c)", "1 + 2", "Verification against validation; two validation methods for non-numeric data"),
  ("M/J 2022", "13", "5(b)(ii), (iii)", "3 + 2", "Range, presence and length checks for a date of birth; why data may still be wrong"),
  ("O/N 2022", "21", "6", "1 + 5 + 1", "The condition in an email validation function; trace table; the returned value (Paper 2)"),
  ("O/N 2023", "13", "8(a)", "2", "A method other than verification of protecting integrity"),
  ("O/N 2025", "21, 23", "6", "2 + 7", "Why a check digit method accepts an incorrect number; write the module Generate() (Paper 2)"),
  ("M/J 2026", "12", "2(b)", "3", "Two validation methods for a date of birth"),
  ("M/J 2026", "13", "1", "5", "Complete a description of verification and validation methods")]

past = '''  <p class="note">Validation checks are asked in Paper 1 every year in one of three forms: name the check from an algorithm, apply a named check to some data, or explain what validation can and cannot do. The Paper 2 questions need a trace and pseudocode. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q6"), "3 marks", "State",
  "Each of the following algorithms performs data validation. State the type of validation check that each performs. (a) INPUT x; IF x < 0 OR x > 10 THEN OUTPUT \"Invalid\" ENDIF. (b) INPUT x; IF x = \"\" THEN OUTPUT \"Invalid\" ENDIF. (c) INPUT x; IF NOT(x = \"Red\" OR x = \"Yellow\" OR x = \"Blue\") THEN OUTPUT \"Invalid\" ENDIF.", "Two ends; blank; a list of allowed values.",
  "<p>" + mks(["(a) Range (check)", "(b) Presence (check)", "(c) Existence (check)"]) + "</p>", "Calling (a) a limit check. It has two ends, so it is a range check.") + peq(SRC("w21", "11/13", "Q2(b)(i)"), "2 marks", "Describe",
  "Describe how data validation helps to protect the integrity of the data. Give an example in your answer.", "Checks the data is reasonable; example.",
  "<p>" + mks(["Validation checks that data is reasonable or sensible", "Example: checking the data is the right number or type of characters"]) + "</p>", None) + peq(SRC("w22", "12", "Q4(a)(c)"), "1 + 2 marks", "State / Describe",
  "(a) State the difference between data verification and data validation. (c) One validation method is a presence check. Describe two other validation methods that can be used to validate non-numeric data.", "Same as original against reasonable. Format, existence, length, type.",
  "<p><b>(a)</b> " + mks(["Verification checks that input data is the same as the original, whereas validation checks that the data is reasonable or sensible"]) + "</p><p><b>(c)</b> Any two: " + mks(["To make sure data is in the required format (only expected characters allowed)", "To make sure the data is already present in the system", "To make sure the data contains the correct number of characters", "To ensure that non-numeric data is entered"], "a") + "</p>", None) + peq(SRC("s22", "13", "Q5(b)(ii)(iii)"), "3 + 2 marks", "Give / Explain",
  "The company transfers each employee's date of birth into the computer. (ii) Give one example of how each of the following validation rules can be used to validate the date of birth: range check, presence check, length check. (iii) Explain why the data in the system may not be correct even after validating and verifying the data.", "Between two dates; not blank; right number of characters. Validation: reasonable only. Verification: matches the original only.",
  "<p><b>(ii)</b> " + mks(["Range: it must be after and before specific dates, for example between 1900 and today's date, or the month between 1 and 12", "Presence: make sure the date of birth has been entered", "Length: make sure it has the right number of characters, for example 8 characters"]) + "</p><p><b>(iii)</b> Any two: " + mks(["Validation checks the data is reasonable or within bounds; it does not check that accurate data has been entered", "Verification checks the data matches the data given; it does not check that the original data is accurate"], "a") + "</p>", "Answering 'a range check is between two numbers' with no date of birth. Apply the check to the data.") + peq(SRC("w22", "21", "Q6"), "1 + 5 + 1 marks", "State / Complete",
  "The function IsValid(InString) checks whether a string is a valid email address. It counts Dots ('.'), Ats ('@') and Others in InString; if Ats becomes greater than 1, Valid becomes FALSE; and at the end IF NOT (Dots >= 1 AND Ats = 1 AND Others > 8) THEN Valid ← FALSE. (a) State the values that would result in the condition evaluating to TRUE. (b) Complete the trace table for IsValid(\"Liz.123@big@net\") and state the value returned.", "The bracket must evaluate to FALSE: one of the three tests fails.",
  "<p><b>(a)</b> Any one: " + mks(["Dots is zero (less than one), or Ats is not equal to one, or Others is less than nine"]) + "</p><p><b>(b)(i)</b> " + mks(["Initial values: Dots 0, Ats 0, Others 0, Valid TRUE", "Others rises to 3 for L, i, z; Dots becomes 1 at '.'", "Others rises to 6 for 1, 2, 3; Ats becomes 1 at the first '@'", "Others rises to 9 for b, i, g", "At the second '@' Ats becomes 2 and Valid becomes FALSE"]) + "</p>" + IV_TABLE + "<p><b>(ii)</b> " + mks(["FALSE"]) + "</p>", None) + peq(SRC("w23", "13", "Q8(a)"), "2 marks", "Describe",
  "Data verification is one method of protecting the integrity of data. Describe one other method of protecting the integrity of data.", "Validation: reasonable, within bounds.",
  "<p>" + mks(["Validation (a named or described validation method)", "protects the data by ensuring it is reasonable or sensible and within specified bounds"]) + "</p>", None) + peq(SRC("w25", "21", "Q6"), "2 + 7 marks", "Identify / Write",
  "A check digit method sums all the digits of the original number, uses integer division to find the remainder when the sum is divided by 10, uses the remainder as the check digit and appends it, so 4162 becomes 41623. (a) An incorrect attempt was made to enter 41623: the first two digits were entered incorrectly and the last three correctly. The check digit was found to be correct and the input was accepted. Identify an example of the incorrect attempt and explain why it was not rejected. (b) Write pseudocode for a module Generate() that takes an integer (at least three digits) and returns the new number including the check digit.", "(a) The first two digits must still sum to 5 (or 15). (b) Sum the digits, MOD 10, append.",
  "<p><b>(a)</b> " + mks(["Number: any number where the first two digits sum to 5 or 15 and the last three digits are 623, for example 32623", "Explanation: the remainder is the same, or the sum of the digits is the same"]) + "</p><p><b>(b)</b> One answer:</p>" + code('''FUNCTION Generate(Number : INTEGER) RETURNS INTEGER
   DECLARE Total, Index, CheckDigit : INTEGER
   DECLARE NumString : STRING
   Total ← 0
   NumString ← NUM_TO_STR(Number)
   FOR Index ← 1 TO LENGTH(NumString)
      Total ← Total + STR_TO_NUM(MID(NumString, Index, 1))
   NEXT Index
   CheckDigit ← Total MOD 10
   Number ← Number * 10 + CheckDigit
   RETURN Number
ENDFUNCTION'''.split("\n")) + "<p>" + mks(["Function heading, parameter, return type and ending", "Initialise Total", "Convert Number to a string and loop for its length", "Attempt to sum the digits in a loop", "Completely correct sum of digits", "Calculate CheckDigit", "Add CheckDigit to the original number multiplied by 10 and return it"]) + "</p>", "Writing a check digit method that cannot be failed. A digit swap or two errors that cancel out gives the same sum.") + peq(SRC("s26", "12", "Q2(b)"), "3 marks", "Identify",
  "The personal data includes the date of birth, for example 05/07/2010. Complete the table by identifying two methods of validation that can be used on the date of birth. State how each validation method will be used for the date of birth.", "Presence, range, limit, format, length or type; apply to the date.",
  "<p>One mark for two correct names and one for each matching use (max 2): " + mks(["Presence check: the date of birth cannot be left blank", "Range check: it must be after one date and before another date (both ends)", "Limit check: it must be before or after a specific date (one end only)", "Format check: it must be dd/mm/yyyy", "Length check: it must be exactly 10 characters", "Type check: the data type must be DATE or DATE/TIME"]) + "</p>", None) + peq(SRC("s26", "13", "Q1"), "5 marks", "Complete",
  "Complete the description by writing the missing terms. ... is a method of verification where the data is entered by a user and then manually compared to the original data. A verification method used during data transfer calculates a value from the data which is transferred with the data; the receiver performs the same calculation and compares the result. This method is ... . ... check compares the data entered to a list of possible values. ... check makes sure data has the correct combination of letters, numbers and symbols. ... check makes sure the correct quantity of characters has been entered.", "Visual check; checksum; existence; format; length.",
  "<p>" + mks(["Visual check", "checksum", "Existence", "Format", "Length"]) + "</p>", None)

review = req("3 marks", "Apply", "A form asks for a student's year group, which must be 7 to 13. Describe a range check and a presence check for this field, and one validation check that is not suitable.", "Two ends; not blank.", "<p>" + mks(["Range check: the year group must be between 7 and 13 inclusive", "Presence check: the field cannot be left blank", "A format check on dd/mm/yyyy would not be suitable for a year group"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a check digit cannot detect every error.", "Same sum.", "<p>" + mks(["The check digit is calculated from the sum of the digits", "so errors that keep the sum the same, such as swapped digits, are not detected"]) + "</p>", None) + req("2 marks", "State", "State two differences between validation and verification.", "Sensible against same as original.", "<p>" + mks(["Validation checks the data is reasonable; verification checks it is the same as the original", "Validation is done by the computer using rules; verification compares two copies of the data"]) + "</p>", None) + req("2 marks", "Calculate", "Calculate the check digit for 7281 using the sum-of-digits method and write the new number.", "7 + 2 + 8 + 1 = 18.", "<p>" + mks(["Sum 18, remainder 8 when divided by 10", "New number 72818"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a drop-down list is an example of an existence check.", "List of values.", "<p>" + mks(["The user can only choose from a list of possible values", "so no value that is not on the list can be entered"]) + "</p>", None)

tips = tips_html([
  ("Apply the check to the data.", "Not just 'checks the range'."),
  ("Range: two ends. Limit: one.", "Know which one you mean."),
  ("Validation: reasonable.", "Not correct."),
  ("Check digit: sum, MOD 10, append.", "Detects single-digit errors."),
  ("Existence: a list of values.", "Also called look-up."),
  ("Verification is a different mark.", "Double entry, visual check."),
], [("validation", "An automatic check that data is reasonable and in the right format."), ("a check digit", "A digit calculated from the other digits to detect errors."), ("an existence check", "Data must be one of a list of possible values."), ("a format check", "Data must follow a pattern.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Write", "Give the pseudocode.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const v = [4, 12, 25][k]; const ok = v >= 5 && v <= 18; let o = SV.rect(30, 40, 360, 30, "cell", { rx: 4 }) + SV.rect(30 + (5 - 0) * 12, 40, 13 * 12, 30, "f1", { rx: 4 }) + SV.text(30 + 5 * 12, 34, "5", "sm", { "text-anchor": "middle" }) + SV.text(30 + 18 * 12, 34, "18", "sm", { "text-anchor": "middle" }) + SV.circle(30 + v * 12, 55, 8, ok ? "f2" : "f3");
    o += SV.text(30, 105, ["age entered: 4", "age entered: 12", "age entered: 25"][k] + (ok ? " → accepted" : " → rejected: outside the range 5 to 18"), "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 130, label: "Range check", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A range check accepts ages from 5 to 18 inclusive. 4 is below the range: <b>rejected</b>.", "12 is inside the range: <b>accepted</b>.", "25 is above the range: <b>rejected</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const checks = ["presence", "format", "length", "range", "type"]; let o = SV.rect(20, 20, 200, 30, "cell", { rx: 4 }) + SV.text(30, 40, "05/07/2010", "lbl bd"); checks.forEach((c, i) => { o += SV.rect(260, 14 + i * 28, 240, 24, i < k ? "f1" : "cell", { rx: 4 }) + SV.text(270, 31 + i * 28, c + " check" + (i < k ? " ✓" : ""), "lbl", { style: "font-size:12px" }); }); o += SV.text(20, 160, k >= 5 ? "Valid: reasonable and in the right format (not proof it is correct)" : "", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 175, label: "Several checks", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The date of birth 05/07/2010 is entered.", "Presence: it is not blank.", "Format: it matches dd/mm/yyyy.", "Length: exactly 10 characters.", "Range: between 1900 and today.", "Type: it is a valid DATE."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lines = ["4 1 6 2", "sum: 4 + 1 + 6 + 2 = 13", "13 MOD 10 = 3: check digit 3", "new number 41623", "entered as 41633: recalculated digit 4 ≠ 3: rejected"]; let o = ""; lines.slice(0, k + 1).forEach((l, i) => { o += SV.text(30, 30 + i * 28, l, i === k ? "lbl bd t3" : "lbl", { style: "font-size:14px" }); }); return o; };
  Lib.stepper($("#stC"), { w: 480, h: 160, label: "Check digit", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The original number is 4162.", "Sum the digits.", "Take the remainder when divided by 10.", "Append it to get the new number.", "A single-digit error changes the sum, so the number is rejected."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#vIn"); const paint = () => { const t = inp.value; const m = t.match(/^(\d\d)\/(\d\d)\/(\d{4})$/); const d = m ? new Date(+m[3], +m[2] - 1, +m[1]) : null; const real = d && d.getDate() === +m[1] && d.getMonth() === +m[2] - 1;
    const rows = [["Presence", t.length > 0], ["Length (10 characters)", t.length === 10], ["Format (dd/mm/yyyy)", !!m], ["Type (a real date)", !!real], ["Range (1900 to today)", !!real && d.getFullYear() >= 1900 && d <= new Date()]];
    $("#vOut").innerHTML = '<div class="tw"><table class="t"><tr><th>Check</th><th>Result</th></tr>' + rows.map(([n, ok]) => `<tr><td>${n}</td><td style="color:var(${ok ? "--good" : "--bad"})"><b>${ok ? "pass" : "fail"}</b></td></tr>`).join("") + "</table></div>" + `<div class="verdict">${rows.every((r) => r[1]) ? "Valid: it passes every check, but validation cannot tell whether it is the person's real date of birth." : "Rejected by at least one check."}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  let n = 4162; const paint = () => { const dg = String(n).split("").map(Number), sum = dg.reduce((a, b) => a + b, 0), cd = sum % 10; $("#cV").innerHTML = `Original <b>${n}</b>: digits sum to <b>${dg.join(" + ")} = ${sum}</b>; ${sum} MOD 10 = <b>${cd}</b>, so the new number is <b>${n}${cd}</b>. If a single digit is mistyped the sum changes, so the recalculated check digit will not match and the entry is rejected.`; };
  Lib.slider($("#cS"), { id: "c1", label: "Original number ", min: 100, max: 9999, value: n, fmt: (x) => x, onInput: (v) => { n = v; paint(); } }); paint();
})();
btnTable("wB", "wO", [
  ["The password must be at least 8 characters", "Length check", "Counts characters"],
  ["Percentage must be 0 to 100", "Range check", "Two limits"],
  ["Email must contain @", "Format check", "Pattern of characters"],
  ["A name must not be left empty", "Presence check", "Entered or not"],
  ["Choose from Mon, Tue, Wed...", "Existence check", "List of allowed values"],
  ["Last digit of a barcode", "Check digit", "Calculated from the others"]
], ["Rule", "Check", "Why"]);
''' + _prjs

finish("as-6-2-1-data-validation", "as621", "Data Validation",
  "Range, limit, length, type, presence, format, existence and check digit validation applied to real data, and why valid data is not always correct, with animations, a date-of-birth checker and the real Paper 1 and Paper 2 questions from 2021 to 2026.",
  "6.2.1", "6 · Security, privacy and data integrity", "section 6.2 Data integrity", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on data validation (Papers 1 and 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
