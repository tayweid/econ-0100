# Editing the ECON 0100 website

All course content lives in `course-content.yaml.js`. It is YAML wrapped in a one-line
JavaScript assignment: edit the YAML between the two backtick lines and leave the wrapper
alone. Two things may not appear inside the YAML, a backtick and the pair `${`; the checker
refuses both. The file is JavaScript rather than plain YAML for one reason: a page opened by
double-clicking may load a neighbouring `<script>` and nothing else, so this is what lets the
site work straight from disk as well as when served.

There is no build step. `part-a.html` through `part-f.html` render in the browser from
`course-content.yaml.js`, and they behave the same whether double-clicked, served locally,
or deployed.

## Typical workflow

1. Edit `course-content.yaml.js`.
2. Open the affected `part-*.html` page and refresh. Double-click it, or run
   `scripts/preview.command` to serve the folder.
3. Run `scripts/check-course` before committing.

`scripts/check-course` validates the YAML (syntax, the wrapper, every field, YouTube IDs,
every local file the YAML names) and confirms each page shell still matches its part. It
changes nothing.

`scripts/preview.command` is optional. Serving reproduces the deployed behaviour exactly;
the one difference from disk is described under "How they find files".

## When the HTML needs an edit

Each `part-*.html` is a small shell: the navigation, one empty `<div>` per block, and a
checkpoint slot. Everything visible inside them comes from the YAML. The shell only needs
an edit when a block is added or removed, or a checkpoint appears or disappears. Then keep
these in step with the YAML, in order:

    <div class="block" id="part-a2" data-course-block="A2"></div>
    <li><a href="#part-a2" class="nav-link-right" data-nav-block="A2">A2</a></li>

The page refuses to render, with a message saying what is off, when the shell and the YAML
disagree; `scripts/check-course` reports the same thing before you commit.

## How they find files

Each block carries a `folder:` naming its directory under `Parts/<PART>/`, which is the one
fact a browser cannot derive, and conventional paths are built from it:

    Parts/<PART>/<folder>/Exercise/Exercise_<BLOCK>.pdf
    Parts/<PART>/<folder>/Vignette/Vignette_<BLOCK>.pdf
    Parts/<PART>/<folder>/Homework/Homework_<BLOCK>.pdf

Existence is settled by asking for each candidate. Drop a conventionally named PDF into the
right folder and its chip appears on the next load, with no YAML edit. Solutions remain
opt-in through `solutions: true`, so an answer key sitting on disk never surfaces by itself.

Served over http(s) the question is a HEAD request, which sees only what is actually
published. A page opened from disk has an opaque origin where every fetch is refused, but
the browser still lets it load a neighbouring `<link>` or `<script>`, and those report
whether the file was there; the page uses a stylesheet link for this, which executes nothing
and is removed as soon as it answers. The one difference is that from disk the probe sees
the working tree, untracked files included, while over HTTP it sees only what was served.

Demo and extra downloads are shown only when explicitly listed under `links:`. Explicit
links, including an empty list, override discovery. Chapter and homework links follow
their existing structured conventions.

## A normal block

```yaml
- block: A2
  folder: A2_Advantage
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

That is enough for the block heading, navigation link, Episode A2 title, YouTube thumbnail,
Chapter 2 reading link, Vignette A2 title, Homework A2 title, icons, and accessibility
markup.

## Useful conventions

- A block ID supplies the standard episode, vignette, homework, and navigation-anchor names.
- A reading `chapter` supplies its title and PDF path. Add `topic` for the descriptive title.
- A `video` is only the eleven-character YouTube ID; its thumbnail is automatic.
- `files: A1` overrides the base name used for conventional vignette links.
- `homework_defaults` at the part level supplies repeated due dates and assignment sets.
- Put words between `*asterisks*` when a short description should be italicized.
- Use `extras` for an unusual resource inside a standard block.

The pages render block and checkpoint sections. The old carousel, homework-notes, and
standalone section forms went with the generator and are no longer accepted.
