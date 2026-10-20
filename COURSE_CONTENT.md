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

The student-facing Course Logistics page is `checkpoints.html`, linked from `course.nav`.
Its timeline is rendered by `checkpoints.js` from the checkpoint dates,
reattempt dates, and logistics in the same YAML; do not copy dates into the HTML.
The guide starts with A/B and offers a full-semester view. Reattempt eligibility is
cumulative by session letter (B offers A+B), not by which checkpoints have already
occurred. The final session includes Checkpoint F and reattempts for earlier parts;
only dated sessions appear in the timeline. Policy copy and diagram styling live in the
guide HTML. Each event heading sits above its date and regular-weight uppercase location,
separated by a middle dot; final-session details stay in a tooltip. The solid and dashed
legend rows below the timeline state “2 of 3 practice unlocks a skill on the
Checkpoint” and “3 of 3 practice unlocks a skill on the Reattempt.” Three compact
makeup steps sit beneath the reattempt row, after the note that practice can only
be made up after the checkpoint: complete missed practice, bring it to
Taylor or a TA to be recorded, then reattempt needed skills. Hover or keyboard-focus
the row headings to emphasize the corresponding paths. Solid practice paths begin with an open circle at the preceding checkpoint
(Part A begins before the first checkpoint), then turn dashed at their own checkpoint.
On phones, the A/B diagram turns vertically so all four opportunities
remain visible together. Checkpoint bars and hollow reattempt diamonds distinguish the two kinds of
attempt without repeated part-letter labels. Matching keys sit to the left of the
compact legend sentences, with each attempt marker at the right end of its line.
Only the final session has a tooltip, with its time and session details; its heading
is underlined. Hover, keyboard focus, or tap reveals it; Escape and clicking outside
dismiss it. The legend has no full-width divider lines. The introduction compares checkpoints
to quizzes broken out by skills and explains that individual skills can be reattempted. The sidebar
reads office hours and the syllabus link from the course YAML. Preview both timeline
views, tooltips, and the narrow layout when changing the guide.
The course home (`index.html`) still opens the current part.

`design/course-logistics-options.html` is a separate interactive mockup comparing
practice requirements in the legend below the timeline, in cards above it, and in
a compact timeline header. Use its three layout buttons to compare; it reuses the
current renderer and YAML dates and does not change the student-facing page.
