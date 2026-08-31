# Editing the ECON 0100 website

Edit `course-content.yml`. The six `part-*.html` pages are generated and should not be edited directly.

## Typical workflow

1. Edit `course-content.yml`.
2. Run `scripts/build-course`.
3. Open the affected page and verify it visually.
4. Run `scripts/build-course --check` before committing.

The `--check` command does not rewrite anything. It reports an error if the generated pages are stale.

## Experimental no-build Part A

`part-a-yaml.html` is a parallel pilot that keeps the current page frame but reads the visible Part A content directly from `course-content.yml` in the browser. The existing `part-a.html` remains the standard page and is the pilot's fallback.

To preview the pilot, serve the repository over HTTP and open `http://127.0.0.1:8765/part-a-yaml.html`:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

While the server is running, an edit to Part A in `course-content.yml` appears after a browser refresh; there is no build step. The HTML shell only needs an edit when the page structure changes, such as adding or removing a block. Because browsers do not allow a local HTML file to fetch a neighboring YAML file safely, this pilot will not work by double-clicking it; use the local server or the deployed site.

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
- `files: A1` adds the conventional vignette/demo PDF and solutions links.
- `homework_defaults` at the part level supplies repeated due dates and assignment sets.
- Put words between `*asterisks*` when a short description should be italicized.
- Use `extras` for an unusual resource inside a standard block.

Recitations, MiniExams, past-demo collections, the Part F FAQ, and standalone resources also have compact structured forms in the same file. None require embedded HTML.

The builder validates YAML syntax, YouTube IDs, duplicate section IDs, generated-page freshness, and local file links. The six already-known missing PDFs remain warnings so they do not block unrelated updates.
