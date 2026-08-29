# econ-0100.tayweid.io — Graphite Style Guide (web)

This site is the ECON 0100 **desk**: same world as the course's video stage
(graphite ground, CMU Serif voice, the same named colors), at reading
distance. A student moving between a video, this site, and the notes should
feel zero seam.

Authority chain: canonical values live in the **Graphite repo**
(`~/Projects/Graphite`, github.com/tayweid/Graphite — `tokens.json` +
palette checker) → `course.css`, served from
`https://tayweid.github.io/course-assets/course.css` → this site's pages.
The *animation* style guide (models, colors-in-context, motion, beats) is
`ECON_0100/Parts/_Style_Guide.md` in the course repo — animators read that;
this file covers only the website.

## The one rule for this repo

**Every page loads the shared `course.css` and nothing else.** The part
pages already do; `index.html` and anything still importing
`assets/styles/*` (the old Roboto Slab system: `variables.css`,
`typography.css`, …) are the remaining migration. When the migration is
done, delete `assets/styles/` entirely.

## Tokens

Same as the main site's guide (see `tayweid.github.io/_Style_Guide.md`):
ground `#212121`, body `#C8C8C8`, link/accent azure `#4A8FF0`, gold
`#E5C044` for defined terms, and the six course marks for any embedded
figure — teal `#128A9B` (demand), orange `#E2803A` (supply), green
`#34B57A`, red `#C63944` (guide), purple `#A99CF2`, pink `#C95AC0`. A
supply-and-demand figure on this site uses exactly the video's colors: that
continuity is the brand.

Type: CMU Serif headings, Source Sans 3 body — both come with `course.css`.
Roboto Slab is retired.

## Course-specific notes

- Video thumbnails and embeds sit on the graphite ground with no added
  chrome — the 2:1 stage frames are designed to butt cleanly against the
  page.
- The MICRO-ECON nameplate is the serif stacked-span pattern from
  `course.css`; don't restyle it per page.
- Defined terms in notes pages may use the gold, matching the videos'
  definition cards.

## Porting list (this repo)

- [ ] `index.html` (and any other page not yet on `course.css`) → shared
      stylesheet; then delete `assets/styles/`.
- [ ] Sweep inline styles for hard-coded colors; replace with the CSS
      variables once `course.css` exposes the mark tokens.
