# Editing the ECON 0100 website

Course lessons and schedule data live in `course-content.yaml.js`.
Home-page office hours, the syllabus link, and logistics copy live in `checkpoints.html`. Edit the YAML between the two backtick
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

The course home is `checkpoints.html`; `index.html` redirects there. Setting
`course.home: index.html` makes MICRO ECON link home on every part page. Office hours
appear beside the page title and six linked part summaries on wide screens.
Each entry pairs a serif Part A–F label with its title in the course's light
sans-serif body font, on one line. These entries live in `checkpoints.html`, so keep them
in sync when editing part titles in the YAML.
The office-hours table starts level with Part A on wide screens. Names use serif
type, followed by · TA or · UTA (Taylor has no role suffix); times and rooms use
the light sans-serif body style. The office hours and summaries stack on smaller screens.
The syllabus uses the shared chip beside the page title;
neither appears in `course.nav`.
The home page has no sidebars or duplicate mobile navigation. Each part summary
is one keyboard-accessible link covering its label and title. Part pages
retain their existing navigation back to the course home.
Its timeline is rendered by `checkpoints.js` from the checkpoint dates,
reattempt dates, and logistics in the same YAML; do not copy dates into the HTML.
The course home shows only the full-semester timeline, with horizontal scrolling
on narrow screens. Dates are spaced about 130 pixels apart and part rows 32 pixels
apart; each event stacks its name, date, and location to avoid label collisions.
A yellow Today line uses the current date in America/New_York and interpolates
between surrounding event dates. It stays on a session's column throughout a
multi-day session, hides outside the dated timeline, and refreshes while the page
is open or when returning to the tab. On initial load, the timeline scrolls Today
near the left, just past the frozen Part A–F label column. Manual scrolling remains
free; the date refresh does not move the viewport. Reattempt eligibility is
cumulative by session letter (B offers A+B), not by which checkpoints have already
occurred. The final session includes Checkpoint F and reattempts for earlier parts;
only dated sessions appear in the timeline. Policy copy and diagram styling live in the
guide HTML. Each event heading sits above its date and regular-weight uppercase location
on separate lines; final-session details stay in a tooltip. The solid and dashed
legend rows below the timeline state “2 of 3 practice unlocks a skill on the
Checkpoint” and “3 of 3 practice unlocks a skill on the Reattempt.” Three compact
makeup steps sit beneath the reattempt row, after the note that practice can only
be made up after the checkpoint: complete missed practice, bring it to
Taylor’s or a TA’s office hours, then reattempt needed skills. Hover or keyboard-focus
the row headings to emphasize the corresponding paths. Hovering a path or its
markers also highlights its matching legend heading and dims the other heading
and route type; wider invisible targets make thin paths and dashed gaps easy to hover.
Solid practice paths begin with an open circle at the preceding checkpoint
(Part A begins before the first checkpoint), then turn dashed at their own checkpoint.
Phones use the same complete, horizontally scrollable timeline. Checkpoint bars and hollow reattempt diamonds distinguish the two kinds of
attempt without repeated part-letter labels. Matching keys sit to the left of the
compact legend sentences, with each attempt marker at the right end of its line.
Only the final session has a tooltip, with its time and session details; its heading
is underlined. Hover, keyboard focus, or tap reveals it; Escape and clicking outside
dismiss it. The legend has no full-width divider lines. The introduction compares checkpoints
to quizzes broken out by skills and explains that individual skills can be reattempted. Preview the complete timeline, its final-session
tooltip, and the narrow layout when changing the guide. Check home navigation
from a part page when changing course navigation.

`design/course-logistics-options.html` is a separate interactive mockup comparing
practice requirements in the legend below the timeline, in cards above it, and in
a compact timeline header. Use its three layout buttons to compare; it reuses the
current renderer and YAML dates and does not change the student-facing page.
