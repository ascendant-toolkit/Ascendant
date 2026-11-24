# Ascendant social videos

Every video is built from a small JSON spec by `make.py`, so they all share the same intro, captions, outro, colours and music treatment.

```
python3 -m venv tools/video/.venv && tools/video/.venv/bin/pip install pillow   # once; ffmpeg must be installed
tools/video/.venv/bin/python tools/video/make.py tools/video/specs/<spec>.json [wide square vertical]
```

Media lives in `Social Videos/` (git-ignored: large, and the music licence is not ours to publish). Spec paths are relative to that folder. The contact email sits in `Social Videos/local.json` as `{"email": "..."}`. It never goes in the repo.

Outputs: `wide` 1920x1080 (X, YouTube), `square` 1080x1080 (Instagram feed), `vertical` 1080x1920 (TikTok, Reels, YouTube Shorts).

## House style

- **Structure:** 5-10 s branded intro (`Brand/` has the full intro, a 3 s Shorts cut `intro-3s.mp4` and a clean `globe.png`), then the lesson footage, then the free-lessons card with "Try a free lesson now", then the 5 s outro. For Shorts under 30 s use `specs/_short-template.json` (3 s intro, one clip, outro).
- **Footage:** screen recordings of the real lessons. Speed up dead time (1.5-2x), cut to the interesting half, one idea per clip, 10-20 s each.
- **Captions:** one pill at the bottom of every clip, Georgia, sentence case, no full stop, plain description of what the viewer sees ("Practise with drag-and-drop questions"). No emoji.
- **Look:** warm paper background (#f5f3ee) behind clips, dark navy pill, green (#34d37a) for the link, globe backdrop for intro and outro. Colours, fonts and handles are in `brand.json`; change them there only.
- **Music:** one calm instrumental bed at 0.4 volume, fading in under the intro and out with the outro. Licence-check every track.
- **Safe zones (vertical):** keep text out of the bottom ~250 px and right ~120 px, where TikTok and Reels put their buttons. The layout already does this.
- **Tone:** educational, no hype, no exam-result promises.
- **Posting:** same caption structure every time (hook line, what the lesson covers, `ascendant.academy`), same handles across platforms.

## Ideas for a repeatable Shorts series

A fixed format makes videos recognisable: "One diagram in 30 seconds" (step-through of a single diagram), "Exam question, mark scheme" (the model-answer reveal), "Spot the mistake" (the common-mistake boxes). Reuse the same intro sting and caption style each time and rotate the subject accent colours.
