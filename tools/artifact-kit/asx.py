"""Helpers for the AS Level (9708) syllabus-numbered pages."""
from syl import *

_M = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}

def L(code, n, tail=", reworded"):
    """Label for a past paper question: L('m21_12', 1) -> 'Feb/March 2021 · 12 · Q1, reworded'."""
    ser, var = code.split("_")
    return f"{_M[ser[0]]} 20{ser[1:]} · {var} · Q{n}{tail}"

def P(code, q):
    """Source line for a written question: P('s20_21', '2(a)') -> 'Based on May/June 2020 · 9708/21 · Q2(a)'."""
    ser, var = code.split("_")
    return f"Based on {_M[ser[0]]} 20{ser[1:]} · 9708/{var} · Q{q}"

def mcq(code, n, q, opts, a, why):
    """One reworded Paper 1 question with its source in the stem."""
    return (f"{q} ({L(code, n)})", opts, a, why)

EYAS = lambda sub: f"AS Level Economics · 9708 · Syllabus {sub}"
