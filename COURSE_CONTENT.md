# Editing the ECON 0100 website

All course content lives in `course-content.yaml.js`. Edit the YAML between the two backtick
lines, open the affected `part-*.html` page (double-click it), refresh, and run
`scripts/check-course` before committing. There
is no build step.

To edit through forms instead, double-click `Edit ECON 0100.app` here (it needs the
`../tayweid.github.io` checkout beside this one): it shows the course outline, a form per block with a
live preview of the page, and runs the checker on save.

The format, the renderer, and the checker are shared with every course site and live in
`tayweid.github.io/course-assets`; the format is documented in
[COURSE_CONTENT.md](https://github.com/tayweid/tayweid.github.io/blob/main/course-assets/COURSE_CONTENT.md)
there. `scripts/check-course` expects that repository to be cloned beside this one.

Local to this site: every block names its `folder` (e.g. `Part_A/A1_The_PPF`), and the conventional
Exercise, Vignette, and Homework PDFs are found there without a YAML edit; solutions stay
opt-in through `solutions: true`. Chapter readings resolve to `Reading/Ch_NN.pdf`. An extra
with no video may carry an `image` (a URL or a local path) as its thumbnail.

The student-facing checkpoint guide is `checkpoints.html`, linked from `course.nav`.
Its timeline and date list are rendered by `checkpoints.js` from the checkpoint dates,
reattempt dates, and logistics in the same YAML; do not copy dates into the HTML.
The guide starts with A/B and offers a full-semester view. Reattempt eligibility is
cumulative by session letter (B offers A+B), not by which checkpoints have already
occurred. The final session includes Checkpoint F and reattempts for earlier parts;
undated reattempts remain explicitly TBA. Policy copy and diagram styling live in the
guide HTML. On phones, the A/B diagram turns vertically so all four opportunities
remain visible together. Preview both timeline views and the narrow layout when
changing the guide.
