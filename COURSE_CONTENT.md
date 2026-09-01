# Editing the ECON 0100 website

All course content lives in `course-content.yaml.js`. Edit the YAML between the two backtick
lines, open the affected `part-*.html` page (double-click it, or run
`scripts/preview.command`), refresh, and run `scripts/check-course` before committing. There
is no build step.

The format, the renderer, and the checker are shared with every course site and live in
`tayweid.github.io/course-assets`; the format is documented in
[COURSE_CONTENT.md](https://github.com/tayweid/tayweid.github.io/blob/main/course-assets/COURSE_CONTENT.md)
there. `scripts/check-course` expects that repository to be cloned beside this one.

Local to this site: every block names its `folder` under `Blocks/`, and the conventional
Exercise, Vignette, and Homework PDFs are found there without a YAML edit; solutions stay
opt-in through `solutions: true`. Chapter readings resolve to `Reading/Ch_NN.pdf`. An extra
with no video may carry an `image` (a URL or a local path) as its thumbnail.
