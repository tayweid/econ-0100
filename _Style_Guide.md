# Style

This repo follows **Graphite**, the visual system shared by the video series and every
course site: `~/Projects/Graphite`, github.com/tayweid/Graphite.

- Values live in `tokens.json` there. Change a color there first, run the checker, then
  propagate.
- The web surface (tokens, type, layout, figures in pages, slides) is `docs/web.md` there.
- This site takes all of it from the shared stylesheet, `https://tayweid.github.io/course-assets/course.css`, and loads nothing else.

Local to this repo: the animation guide, `Parts/_Style_Guide.md`, is the full system applied to the ECON 0100 video series. Animators read that. `Parts/_Assets/style.py` is the same system as code, and episodes import it.
