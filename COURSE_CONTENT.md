# Editing the ECON 0100 website

All course content lives in `course-content.yaml.js`. It is YAML wrapped in a one-line
JavaScript assignment: edit the YAML between the two backtick lines and leave the wrapper
alone. Two things may not appear inside the YAML, a backtick and the pair `${`; the builder
refuses both. The file is JavaScript rather than plain YAML for one reason: a page opened by
double-clicking may load a neighbouring `<script>` and nothing else, so this is what lets the
site work straight from disk as well as when served.

## Two kinds of page

`part-a-yaml.html` through `part-f-yaml.html` render in the browser from
`course-content.yaml.js`. Edit the YAML, refresh, done. There is no build step, and they
work the same whether double-clicked, served locally, or deployed. The HTML shell only
needs an edit when the page structure changes, such as adding or removing a block.

`part-a.html` through `part-f.html` are generated from the same file by
`scripts/build-course` and are the standard pages for now. They are the fallback each
`-yaml` page points at when something fails. Do not edit them directly.

## Typical workflow

1. Edit `course-content.yaml.js`.
2. Open the affected `-yaml` page (double-click it, or run `scripts/preview.command`) and refresh.
3. Run `scripts/build-course` to regenerate the standard pages, and `scripts/build-course --check` before committing.

`--check` does not rewrite anything. It validates the YAML and reports an error if the
generated pages are stale.

`scripts/preview.command` is optional. It serves the repository and opens Part A, which
reproduces the deployed behaviour exactly; see below for the one difference from disk.

### How they find files

Each block carries a `folder:` naming its directory under `Parts/<PART>/`, which is the one
fact a browser cannot derive, and conventional paths are built from it:

    Parts/<PART>/<folder>/Exercise/Exercise_<BLOCK>.pdf
    Parts/<PART>/<folder>/Vignette/Vignette_<BLOCK>.pdf
    Parts/<PART>/<folder>/Homework/Homework_<BLOCK>.pdf

Existence is settled by asking for each candidate, the runtime equivalent of the
`File.exist?` calls in `scripts/build-course`. Drop a conventionally named PDF into the
right folder and its chip appears on the next load, with no YAML edit and no build.
Solutions remain opt-in through `solutions: true`, so an answer key sitting on disk never
surfaces by itself.

Served over http(s) the question is a HEAD request, which sees only what is actually
published. A page opened from disk has an opaque origin where every fetch is refused, but
the browser still lets it load a neighbouring `<link>` or `<script>`, and those report
whether the file was there; the page uses a stylesheet link for this, which executes nothing
and is removed as soon as it answers. The one difference is that from disk the probe sees
the working tree, untracked files included, while over HTTP it sees only what was served.

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
