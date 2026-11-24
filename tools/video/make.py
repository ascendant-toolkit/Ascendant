#!/usr/bin/env python3
"""Render an Ascendant social video from a spec in wide, square and vertical formats.

    tools/video/.venv/bin/python tools/video/make.py tools/video/specs/<spec>.json [wide square vertical]

Paths in a spec are relative to the 'Social Videos' folder (git-ignored). The contact
email lives in 'Social Videos/local.json' ({"email": "..."}), never in the repo.
"""
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "Social Videos"
B = json.loads((HERE / "brand.json").read_text())
LOCAL = json.loads((ROOT / "local.json").read_text()) if (ROOT / "local.json").exists() else {}
C = {k: tuple(v) if isinstance(v, list) else v for k, v in B["colors"].items()}
FPS = B["fps"]

# box = area a screen recording is fitted into (w, h, top); cap = caption pill (font, y, height)
FORMATS = {
    "wide":     dict(W=1920, H=1080, box=(1840, 950, 20),  cap=(44, 934, 96), fg_dy=0),
    "square":   dict(W=1080, H=1080, box=(1040, 880, 20),  cap=(38, 956, 84), fg_dy=0),
    "vertical": dict(W=1080, H=1920, box=(1040, 900, 410), cap=(38, 1340, 84), fg_dy=-100),
}


def sh(*cmd):
    subprocess.run([str(c) for c in cmd], check=True)


def dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout)


def font(kind, size, bold=False):
    return ImageFont.truetype(B["fonts"][kind], size, index=1 if bold else 0) if kind == "body" else ImageFont.truetype(B["fonts"][kind], size)


def caption_png(text, f, out):
    size, y0, h = f["cap"]; W, H = f["W"], f["H"]
    ft = font("heading", size)
    while ft.getlength(text) + 80 > W - 40:
        size -= 2; ft = font("heading", size)
    w = int(ft.getlength(text)) + 80
    im = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(im)
    d.rounded_rectangle(((W - w) // 2, y0, (W + w) // 2, y0 + h), radius=h // 2, fill=C["pill"])
    d.text((W / 2, y0 + h / 2), text, font=ft, fill=C["white"], anchor="mm")
    im.save(out)


def outro_pngs(name, tmp, minimal=False):
    W, H = name_f = FORMATS[name]["W"], FORMATS[name]["H"]
    o = B["outro"]; email = LOCAL.get("email", "")
    layers = [Image.new("RGBA", (W, H)) for _ in range(3)]
    d = [ImageDraw.Draw(i) for i in layers]
    cx = W / 2
    if name == "wide":
        y_head, y_sub, y_url, sub_lines = 330, [430], 580, [" ".join(o["sub"])]
        hs, ss, us, rows_y, email_y, cols = 104, 42, 100, [790, 850], 930, 2
    else:
        vert = name == "vertical"
        y_head, y_sub, y_url = (560, [650, 700], 850) if vert else (290, [375, 425], 550)
        sub_lines = o["sub"]; hs, ss, us = 78, 38, 82
        rows_y = [1000 + 66 * i for i in range(4)] if vert else [700 + 58 * i for i in range(4)]
        email_y = 1290 if vert else 950; cols = 1
    d[0].text((cx, y_head), o["headline"], font=font("heading", hs), fill=C["white"], anchor="mm")
    for y, t in zip(y_sub, sub_lines):
        d[0].text((cx, y), t, font=font("body", ss), fill=C["soft"], anchor="mm")
    fu = font("body", us, True)
    l, t, r, b = d[1].textbbox((cx, y_url), B["url"], font=fu, anchor="mm")
    d[1].rounded_rectangle((l - 50, t - 34, r + 50, b + 34), radius=24, outline=C["green"], width=4, fill=(10, 22, 34, 170))
    d[1].text((cx, y_url), B["url"], font=fu, fill=C["green"], anchor="mm")
    fb, fr = font("body", 38, True), font("body", 38)
    socials = [] if minimal else B["socials"]
    groups = [socials[i:i + cols] for i in range(0, len(socials), cols)]
    for y, grp in zip(rows_y, groups):
        widths = [d[2].textlength(p + "  ", font=fb) + d[2].textlength(h, font=fr) for p, h in grp]
        x = (W - (sum(widths) + 70 * (len(grp) - 1))) / 2
        for (p, h), w in zip(grp, widths):
            d[2].text((x, y), p + "  ", font=fb, fill=C["white"], anchor="lm")
            d[2].text((x + d[2].textlength(p + "  ", font=fb), y), h, font=fr, fill=C["soft"], anchor="lm")
            x += w + 70
    if email and not minimal:
        d[2].text((cx, email_y), email, font=fr, fill=C["white"], anchor="mm")
    paths = []
    for i, im in enumerate(layers):
        p = tmp / f"outro_{name}_{i}.png"; im.save(p); paths.append(p)
    return paths


def render(spec, name, out_dir, tmp):
    f = FORMATS[name]; W, H = f["W"], f["H"]; paper = "0x" + C["paper"][1:]
    bw, bh, top = f["box"]
    fit = (f"scale={bw}:{bh}:force_original_aspect_ratio=decrease,"
           f"pad={W}:{H}:(ow-iw)/2:{top}+({bh}-ih)/2:{paper},fps={FPS},format=yuv420p")
    segs, intro = [], None
    if spec.get("intro"):
        intro = ROOT / spec["intro"]
        # clean globe frame for backgrounds: a still from the spec ("globe": png) or the intro's first frames
        if spec.get("globe"):
            globe = ROOT / spec["globe"]
        else:
            globe = tmp / "globe.png"
            sh("ffmpeg", "-y", "-v", "error", "-ss", "0.1", "-i", intro, "-frames:v", "1", globe)
    if intro:
        s = tmp / f"{name}_intro.mp4"
        if name == "wide":
            fc = f"[0:v]scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p"
        else:
            fc = (f"[1:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=25,eq=brightness=-0.25,"
                  f"loop=loop=400:size=1,fps={FPS}[bg];[0:v]scale={W}:-1[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2+({f['fg_dy']}):shortest=1,fps={FPS},format=yuv420p")
        sh("ffmpeg", "-y", "-v", "error", "-i", intro, "-i", globe, "-filter_complex", fc, "-an", "-c:v", "libx264", "-crf", "18", s)
        segs.append(s)
    for i, c in enumerate(spec["clips"]):
        s = tmp / f"{name}_clip{i}.mp4"; cap = tmp / f"{name}_cap{i}.png"
        caption_png(c["caption"], f, cap)
        trim = f"trim=start={c.get('trim_start', 0)},setpts=(PTS-STARTPTS)/{c.get('speed', 1)}"
        sh("ffmpeg", "-y", "-v", "error", "-i", ROOT / c["file"], "-loop", "1", "-i", cap, "-filter_complex",
           f"[0:v]{trim},{fit}[v];[v][1:v]overlay=shortest=1,format=yuv420p", "-an", "-c:v", "libx264", "-crf", "18", s)
        segs.append(s)
    card = spec.get("card")
    if card:
        s = tmp / f"{name}_card.mp4"; cap = tmp / f"{name}_capcard.png"
        caption_png(card["caption"], f, cap)
        m = card.get("trim_margin", 0.0)
        im = Image.open(ROOT / card["image"]); iw, ih = im.size
        crop = f"crop={int(iw * (1 - 2 * m))}:{ih}:{int(iw * m)}:0"
        sh("ffmpeg", "-y", "-v", "error", "-loop", "1", "-t", card.get("seconds", 6), "-i", ROOT / card["image"], "-loop", "1", "-i", cap,
           "-filter_complex", f"[0:v]{crop},scale={W if name != 'wide' else 1760}:-1,"
           f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2+({f['fg_dy']}):{paper},fps={FPS},format=yuv420p[a];"
           f"[1:v]format=rgba,fade=t=in:st=1:d=0.6:alpha=1[c];[a][c]overlay=shortest=1,format=yuv420p",
           "-t", card.get("seconds", 6), "-an", "-c:v", "libx264", "-crf", "18", s)
        segs.append(s)
    if spec.get("outro", True):
        s = tmp / f"{name}_outro.mp4"; l1, l2, l3 = outro_pngs(name, tmp, spec.get("outro_minimal", False))
        sec = spec.get("outro_seconds", B["outro"]["seconds"]); k = sec / 5  # fade timings scale with length
        bgsrc = globe if intro else None
        if bgsrc is None:
            raise SystemExit("outro needs an intro file to take the globe frame from")
        sh("ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", bgsrc, "-loop", "1", "-t", sec, "-i", l1, "-loop", "1", "-t", sec, "-i", l2, "-loop", "1", "-t", sec, "-i", l3,
           "-filter_complex",
           f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=22,eq=brightness=-0.2,"
           f"zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(sec * FPS)}:s={W}x{H}:fps={FPS},format=yuv420p[bg];"
           f"[1:v]format=rgba,fade=t=in:st={0.3*k:.2f}:d={0.6*k:.2f}:alpha=1[a];[2:v]format=rgba,fade=t=in:st={1.1*k:.2f}:d={0.6*k:.2f}:alpha=1[b];"
           f"[3:v]format=rgba,fade=t=in:st={1.9*k:.2f}:d={0.6*k:.2f}:alpha=1[c];[bg][a]overlay[x];[x][b]overlay[y];[y][c]overlay,fade=t=out:st={sec - 0.7 * k:.2f}:d={0.7 * k:.2f},format=yuv420p",
           "-t", sec, "-an", "-c:v", "libx264", "-crf", "18", s)
        segs.append(s)
    # chain crossfades with exact offsets
    ds = [dur(s) for s in segs]; fades = [B["xfade"]] * (len(segs) - 1)
    if spec.get("outro", True) and fades:
        fades[-1] = B["outro_xfade"]
    inputs, fc, cur, acc = [], [], "[0:v]", ds[0]
    for i, s in enumerate(segs):
        inputs += ["-i", s]
    for i in range(1, len(segs)):
        fc.append(f"{cur}[{i}:v]xfade=transition=fade:duration={fades[i-1]}:offset={acc - fades[i-1]:.3f}[x{i}]")
        cur = f"[x{i}]"; acc += ds[i] - fades[i - 1]
    total = acc
    fc = ";".join(fc) if fc else "[0:v]null[x1]"; cur = cur if len(segs) > 1 else "[x1]"
    # audio: intro's own sound, then music bed
    ai = len(segs); m = B["music"]; maps = ["-map", cur]
    ain = []
    if intro:
        ain += ["-i", intro]
    if spec.get("music"):
        ain += ["-i", ROOT / spec["music"]]
    audio = []; k = ai; labels = []
    if intro:
        audio.append(f"[{k}:a]afade=t=out:st={ds[0] - B['xfade']}:d={B['xfade']},apad[ia]"); labels.append("[ia]"); k += 1
    if spec.get("music"):
        start = spec.get("music_start", m["start"]); L = total - start
        audio.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=0:{L:.2f},asetpts=PTS-STARTPTS,volume={m['volume']},"
                     f"afade=t=in:st=0:d={m['fade_in']},afade=t=out:st={L - m['fade_out']:.2f}:d={m['fade_out']},adelay={int(start * 1000)}|{int(start * 1000)}[mu]")
        labels.append("[mu]")
    if audio:
        audio.append("".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0[au]")
        maps += ["-map", "[au]"]
    out = out_dir / f"{spec['name']}-{name}.mp4"
    sh("ffmpeg", "-y", "-v", "error", *inputs, *ain, "-filter_complex", ";".join([fc] + audio), *maps,
       "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.2f}", "-movflags", "+faststart", out)
    print(out, f"{total:.1f}s")


if __name__ == "__main__":
    spec = json.loads(Path(sys.argv[1]).read_text())
    names = sys.argv[2:] or ["wide", "square", "vertical"]
    out_dir = ROOT / spec.get("out", "out"); out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        for n in names:
            render(spec, n, out_dir, Path(t))
