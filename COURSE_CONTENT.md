# Editing the ECON 0100 website

Edit `course-content.yml`. The six `part-*.html` pages are generated and should not be edited directly.

## Typical workflow

1. Edit `course-content.yml`.
2. Run `scripts/build-course`.
3. Open the affected page and verify it visually.
4. Run `scripts/build-course --check` before committing.

The `--check` command does not rewrite anything. It reports an error if the generated pages are stale.

## Experimental no-build pages

`part-a-yaml.html` through `part-f-yaml.html` are a parallel pilot set. Each keeps its current page frame but reads the visible content directly from `course-content.yml` in the browser. The existing `part-a.html` through `part-f.html` remain the standard pages and their corresponding fallbacks.

To preview the pilot, serve the repository over HTTP and open `http://127.0.0.1:8765/part-a-yaml.html`:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

While the server is running, an edit to any part in `course-content.yml` appears after a browser refresh; there is no build step. The HTML shell only needs an edit when the page structure changes, such as adding or removing a block. Because browsers do not allow a local HTML file to fetch a neighboring YAML file safely, these pilots will not work by double-clicking them; use the local server or the deployed site.

### How they find files

Each block carries a `folder:` naming its directory under `Parts/<PART>/`, which is the one
fact a browser cannot derive, and conventional paths are built from it:

    Parts/<PART>/<folder>/Exercise/Exercise_<BLOCK>.pdf
    Parts/<PART>/<folder>/Vignette/Vignette_<BLOCK>.pdf
    Parts/<PART>/<folder>/Homework/Homework_<BLOCK>.pdf

Existence is settled with a HEAD request per candidate, the runtime equivalent of the
`File.exist?` calls in `scripts/build-course`. Drop a conventionally named PDF into the
right folder and its chip appears on the next load, with no YAML edit and no build.
Solutions remain opt-in through `solutions: true`, so an answer key sitting on disk never
surfaces by itself.

A HEAD probe asks the server, so it sees only what is actually published -- more accurate
than a local `File.exist?`, which also counts untracked files that never reached the site.

Probing needs HTTP, though, and a page opened by double-clicking has an opaque origin where
every fetch is refused. For that case `scripts/build-course` still writes
`window.COURSE_BLOCK_FILES` into `course-content.js`, holding the same paths resolved at
build time. Served over http(s) it is ignored entirely in favour of the live probe; it is
consulted only over `file://`, or when a probe cannot be answered at all, so a dropped
connection falls back to the build-time answer instead of quietly hiding a link. Run
`scripts/build-course` if you want a newly added PDF to show up when double-clicking; over
HTTP and on the deployed site it appears on its own.

Runtime pages discover conventional exercise, vignette, and homework PDFs as described above. Demo and extra downloads are still shown only when explicitly listed under `links:` in the YAML, because the builder resolves those through the `files:` shorthand, which names a base rather than a path. Explicit links—including an empty list—override discovery in both the builder and the runtime pages. Chapter and homework links continue to follow their existing structured conventions.

## A normal block

```yaml
- block: A2
  nav: PPF
  title: The production possibility frontier
  description: The PPF shows us what's attainable as individuals and as a society.
  episode:
    video: po4kip5m_QY
    description: The landscape of what's possible
  reading:
    chapter: 2
    topic: Thinking like an economist
  vignette:
    description: PPF practice problems
  homework:
    due: Sunday, September 4
```

That is enough to generate the block heading, navigation link, Episode A2 title, YouTube thumbnail, Chapter 2 reading link, Vignette A2 title, Homework A2 title, practice link, icons, card types, and accessibility markup.

## Useful conventions

- A block ID supplies the standard episode, vignette, homework, navigation-anchor, and practice names.
- A reading `chapter` supplies its title and PDF path. Add `topic` for the descriptive title.
- A `video` is only the eleven-character YouTube ID; its thumbnail is automatic.
- `files: A1` overrides the base name used for conventional vignette links; runtime pages honour it too. For demo and extra downloads it remains builder-only, so list those under `links:` if the runtime pages should show them.
- `homework_defaults` at the part level supplies repeated due dates and assignment sets.
- Put words between `*asterisks*` when a short description should be italicized.
- Use `extras` for an unusual resource inside a standard block.

The current runtime pilot supports the block and checkpoint sections used by Parts A–F. Legacy carousel, homework-notes, and standalone section forms remain builder-only unless runtime support is added later.

The builder validates YAML syntax, YouTube IDs, duplicate section IDs, generated-page freshness, and local file links. The six already-known missing PDFs remain warnings so they do not block unrelated updates.
