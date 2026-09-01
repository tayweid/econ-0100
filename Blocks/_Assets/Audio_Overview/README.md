# Audio Overview — podcast-style intro animation source

Two versions of the render code are kept intentionally; they are NOT
duplicates — each has unique content:

- `main.py` / `scenes.py` — **Oct 2024**, the earlier single-intro
  version: one `Overview()` scene, hardcoded `string = 'MICROECONOMICS'`,
  and its own render config (media dirs, custom colors, 1080p/10fps).
  `scenes.py` carries the full inline `raster_font` letter-pixel dict.
- `main_v2.py` / `scenes_v2.py` — **Dec 2024**, the later batch
  version: a `part_chapter` list of 20 chapters, a loop that renders
  `{Chapter}_Intro` + `{Chapter}_Loop` for each, and a refactored
  `Raster_Font()` helper. This is the code that produced the rendered
  media.

`Audio_Overview.ipynb` is the notebook driver (the only git-tracked
copy). The "copy" filenames were renamed to `_v2` on 2026-08-19; `main_v2.py`
now imports from `scenes_v2.py` explicitly (its `Intro()`/`Loop()` methods
only exist there).
