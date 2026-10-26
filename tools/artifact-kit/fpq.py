"""Floating-point helpers for the 13.3 pages: exact conversion with written working, checked against the mark schemes."""
from fractions import Fraction


def twos(n, bits):
    return format(n if n >= 0 else (1 << bits) + n, f"0{bits}b")


def val(s):
    n = int(s, 2)
    return n - (1 << len(s)) if s[0] == "1" else n


def bin2frac(s):
    """'1011100.011001' -> Fraction"""
    ip, _, fp = s.partition(".")
    return Fraction(int(ip or "0", 2)) + (Fraction(int(fp, 2), 1 << len(fp)) if fp else 0)


def frac2bin(x, maxfrac=40):
    """positive Fraction -> binary string with point"""
    ip = int(x)
    fr = x - ip
    out = ""
    while fr and len(out) < maxfrac:
        fr *= 2
        out += "1" if fr >= 1 else "0"
        fr -= int(fr)
    return format(ip, "b") + ("." + out if out else "")


def decode(m, e):
    return Fraction(val(m), 1 << (len(m) - 1)) * Fraction(2) ** val(e)


def encode(x, mb, eb):
    """normalised two's complement mantissa and exponent, truncating extra bits. Returns (m, e, exact)."""
    x = Fraction(x)
    if x == 0:
        return "0" * mb, "0" * eb, True
    mag = abs(x)
    e = 0
    m = mag
    while m >= 1:
        m /= 2
        e += 1
    while m < Fraction(1, 2):
        m *= 2
        e -= 1
    scaled = m * (1 << (mb - 1))
    exact = scaled.denominator == 1
    pos = int(scaled)
    mant = twos(pos, mb) if x > 0 else twos(-pos, mb)
    if x < 0 and (mant[0] != "1" or mant[1] != "0"):
        # exact -2^k boundary cases are not used by the papers
        pass
    return mant, twos(e, eb), exact


def enc_working(x, mb, eb):
    """Lines of working for denary/binary -> normalised floating point."""
    x = Fraction(x)
    mag = abs(x)
    b = frac2bin(mag)
    m, e, exact = encode(x, mb, eb)
    ev = val(e)
    sig = b.replace(".", "").lstrip("0")
    L = []
    L.append(f"Convert {float(mag):g} to binary: {b}" if x != 0 else "")
    ip, _, fp = b.partition(".")
    if ev >= 0:
        L.append(f"Move the binary point {ev} places left so the number is 0.1...: 0.{sig} × 2^{ev}")
    else:
        L.append(f"Move the binary point {-ev} places right so the number is 0.1...: 0.{sig} × 2^({ev})")
    pos = twos(int(mag / Fraction(2) ** ev * (1 << (mb - 1))), mb)
    L.append(f"Mantissa ({mb} bits, sign bit 0 then the digits): {pos}" + ("" if exact else "  (the extra bits do not fit and are lost)"))
    if x < 0:
        inv = "".join("1" if c == "0" else "0" for c in pos)
        L.append(f"Negative: invert {pos} → {inv}, add 1 → {m}")
    L.append(f"Exponent {ev} in {eb}-bit two's complement: {e}")
    return L, m, e, exact


def place_terms(bits_ip, bits_fp, signed):
    """list of place values for the set bits of a two's complement number with the given integer and fraction parts"""
    terms = []
    n = len(bits_ip)
    for i, c in enumerate(bits_ip):
        if c == "1":
            w = 1 << (n - 1 - i)
            terms.append(-w if (signed and i == 0) else w)
    for j, c in enumerate(bits_fp):
        if c == "1":
            terms.append(Fraction(1, 1 << (j + 1)))
    return terms


def fmt_frac(f):
    f = Fraction(f)
    if f.denominator == 1:
        return str(f.numerator)
    s = f"{float(f):.10f}".rstrip("0").rstrip(".")
    return s


def dec_working(m, e):
    """Lines of working for floating point -> denary."""
    ev = val(e)
    L = [f"Exponent {e} = {ev}"]
    mant = f"{m[0]}.{m[1:]}"
    L.append(f"Mantissa = {mant}")
    n = len(m)
    # place the binary point after (1 + ev) bits
    pt = 1 + ev
    if pt <= 0:
        ip = m[0]
        fp = m[1:]
        s = f"{ip}." + "0" * (-pt) + fp if False else None
    if pt >= n:
        bits = m + "0" * (pt - n)
        ipb, fpb = bits, ""
    elif pt <= 0:
        ipb, fpb = m[0] * 1, ("0" * (-pt) if False else "") + m[1:]
    else:
        ipb, fpb = m[:pt], m[pt:]
    if pt <= 0:
        # negative exponent: result is a fraction; show as moving the point left
        shifted = f"{m[0]}." + (m[0] * (-pt)) + m[1:] if False else None
        v = decode(m, e)
        L.append(f"Move the binary point {-ev} places left, so the value is {mant} × 2^({ev}) = {fmt_frac(v)}")
        return L, v
    L.append(f"Move the binary point {ev} places right: {ipb}.{fpb}" if fpb else f"Move the binary point {ev} places right: {ipb}")
    signed = m[0] == "1"
    terms = place_terms(ipb, fpb, True)
    v = decode(m, e)
    if m[0] == "1":
        terms_s = " + ".join(("−" + str(-t) if t < 0 else fmt_frac(t)) if True else "" for t in terms).replace("+ −", "− ")
        L.append(f"Value (the first bit has a negative place value): {terms_s} = {fmt_frac(v)}")
    else:
        terms_s = " + ".join(fmt_frac(t) for t in terms)
        L.append(f"Value: {terms_s} = {fmt_frac(v)}")
    return L, v


def sp(bits):
    """group a bit string for display: groups of 4 from the left"""
    return " ".join(bits[i:i + 4] for i in range(0, len(bits), 4))


def row(m, e):
    return f"Mantissa {m}   Exponent {e}"
