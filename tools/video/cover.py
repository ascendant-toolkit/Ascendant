#!/usr/bin/env python3
"""Make matching Ascendant covers: one layout, with only the category, title and subject changing.

    tools/video/.venv/bin/python tools/video/cover.py explain "Why $100m grows to $500m" "A-Level Economics"

Writes vertical (TikTok, Reels, Shorts), square (feed posts) and wide (YouTube, X) PNGs to
'Media/Social Videos/Covers'. Categories and colours are in brand.json. Use | in a title to force a line break.
"""
import re, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
from make import B, ROOT, font

HEADING_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
# Everything sits in a centred column no taller than the width, so grid crops (1:1, 4:5, 3:4) never cut text.
SIZES = {"vertical": (1080, 1920), "square": (1080, 1080), "wide": (1280, 720)}


def background(W, H):
    g = Image.open(ROOT / "Brand" / "globe.png").convert("RGB")
    s = max(W / g.width, H / g.height)
    g = g.resize((int(g.width * s) + 1, int(g.height * s) + 1))
    x, y = (g.width - W) // 2, (g.height - H) // 2
    g = g.crop((x, y, x + W, y + H)).filter(ImageFilter.GaussianBlur(5))
    return ImageEnhance.Brightness(g).enhance(.5).convert("RGBA")


def logo(d, x, y, s):
    """The site's mark (assets/logo.svg), drawn s pixels square."""
    k = s / 32
    d.rounded_rectangle((x, y, x + s, y + s), radius=8 * k, fill=(15, 23, 42, 255), outline=(255, 255, 255, 60), width=2)
    pts = [(x + a * k, y + b * k) for a, b in ((8, 20), (14, 14), (18, 18), (24, 10))]
    d.line(pts, fill=(0, 230, 118, 255), width=int(3 * k), joint="curve")
    for px, py in pts[:1]:
        d.ellipse((px - 1.5 * k, py - 1.5 * k, px + 1.5 * k, py + 1.5 * k), fill=(0, 230, 118, 255))
    cx, cy = pts[-1]
    d.ellipse((cx - 2.5 * k, cy - 2.5 * k, cx + 2.5 * k, cy + 2.5 * k), fill=(0, 176, 255, 255))


def wrap(text, ft, width):
    lines = []
    for part in text.split("|"):
        line = ""
        for word in part.split():
            trial = f"{line} {word}".strip()
            if line and ft.getlength(trial) > width:
                lines.append(line); line = word
            else:
                line = trial
        lines.append(line)
    return lines


def cover(category, title, subject, name):
    W, H = SIZES[name]
    label, colour = B["categories"][category]
    k = min(W, H) / 1080
    im = background(W, H); d = ImageDraw.Draw(im)
    cx = W / 2
    max_w = min(W - 140 * k, 940 * k if name != "wide" else 1120)
    # largest title size that fits the title area in no more than three lines
    size = int(128 * k)
    while True:
        ft = ImageFont.truetype(HEADING_BOLD, size); lines = wrap(title, ft, max_w)
        fits = len(lines) <= 3 and all(ft.getlength(l) <= max_w for l in lines) and len(lines) * size * 1.18 <= 460 * k
        if fits or size <= 40:
            break
        size -= 4
    lh = size * 1.18
    # Fixed positions, measured from the top of the centred square: only the title's own size and wrapping change.
    at = lambda v: (H - min(W, H)) / 2 + v * k

    brand = font("heading", int(52 * k))
    mark = 86 * k
    bw = mark + 24 * k + brand.getlength("Ascendant")
    logo(d, cx - bw / 2, at(80), mark)
    d.text((cx - bw / 2 + mark + 24 * k, at(80) + mark / 2), "Ascendant", font=brand, fill="white", anchor="lm")
    chip = font("body", int(36 * k), True); text = label.upper()
    cw = chip.getlength(text) + 70 * k
    d.rounded_rectangle((cx - cw / 2, at(220), cx + cw / 2, at(298)), radius=39 * k, fill=colour)
    d.text((cx, at(259)), text, font=chip, fill=(10, 22, 34), anchor="mm")
    top = at(565) - lh * len(lines) / 2
    for i, line in enumerate(lines):
        d.text((cx, top + lh * (i + .5)), line, font=ft, fill="white", anchor="mm")
    if subject:
        d.text((cx, at(845)), subject, font=font("body", int(44 * k)), fill=tuple(B["colors"]["soft"]), anchor="mm")
    d.rounded_rectangle((cx - 70 * k, at(905), cx + 70 * k, at(913)), radius=4 * k, fill=colour)
    d.text((cx, at(970)), B["url"], font=font("body", int(42 * k), True), fill=tuple(B["colors"]["green"]), anchor="mm")
    return im.convert("RGB")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in B["categories"]:
        raise SystemExit(f'usage: cover.py <{"|".join(B["categories"])}> "Title" ["Subject"]')
    category, title = sys.argv[1], sys.argv[2]
    subject = sys.argv[3] if len(sys.argv) > 3 else ""
    out = ROOT / "Covers"; out.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:48]
    for name in SIZES:
        p = out / f"{category}-{slug}-{name}.png"; cover(category, title, subject, name).save(p); print(p)
