// Shared helpers for the typst vignette files.
//
// Each Blocks/<folder>/Vignette/Vignette_<BLOCK>_sols.typ holds one vignette's
// questions with the answers written in. Compiled on its own it is that block's
// solution guide. Recitations/Recitation_Week_N.typ and _sols.typ #include
// several of them, and set the two states below so the same content renders
// either as the student handout (answers hidden, blanks shown) or as the
// teaching-team guide (answers and working in red).
//
// Compile from the repo root so the imports resolve:
//   typst compile --root . Blocks/A1_The_PPF/Vignette/Vignette_A1_sols.typ
//   typst compile --root . Recitations/Recitation_Week_2.typ

// true while a vignette file is compiled by itself; a wrapper sets it false so
// the vignette's own page setup steps aside.
#let standalone = state("standalone", true)
// true shows answers and working; a student wrapper sets it false.
#let solutions = state("solutions", true)

#let sol-color = rgb("#b3261e")

// Compact layout for the solution guides.
#let sols-setup(doc) = {
  set page(paper: "us-letter", margin: 0.6in)
  set par(justify: true, leading: 8.172pt, spacing: 10pt)
  set list(spacing: 10.672pt)
  set enum(spacing: 10.672pt)
  show heading.where(level: 1): set text(size: 19.000pt)
  show heading.where(level: 1): set block(above: 21.113pt, below: 12pt)
  show heading.where(level: 2): set text(size: 14.000pt)
  show heading.where(level: 2): set block(above: 16pt, below: 9pt)
  set text(size: 10pt, font: "New Computer Modern", hyphenate: true)
  set table(stroke: 0.5pt, inset: 5pt)
  doc
}

// Student handout layout, close to the Plass export of the Vignette_<BLOCK>.md files.
#let student-setup(doc) = {
  set page(paper: "us-letter", margin: (x: 1.25in, y: 1in), numbering: "1")
  set par(justify: true, leading: 8.172pt, spacing: 17.172pt)
  set list(spacing: 10.672pt)
  set enum(spacing: 10.672pt)
  show heading.where(level: 1): set text(size: 19.000pt)
  show heading.where(level: 1): set block(above: 21.113pt, below: 20.084pt)
  show heading.where(level: 2): set text(size: 14.000pt)
  show heading.where(level: 2): set block(above: 35.720pt, below: 15.950pt)
  set text(size: 11pt, font: "New Computer Modern", hyphenate: true)
  doc
}

// What a vignette file applies to itself: the solutions layout when compiled
// alone, nothing when a wrapper has already set the page up.
#let vignette-setup(doc) = context { if standalone.get() { sols-setup(doc) } else { doc } }

// Title line, e.g. #vtitle[Vignette A1][PPF]; tagged "Solutions" in solutions mode.
#let vtitle(name, topic) = heading(level: 1)[
  ECON 0100 | #name | #topic
  #context if solutions.get() { text(fill: sol-color)[| Solutions] }
]

// Content that only appears in the solution guide.
#let sols-only(body) = context { if solutions.get() { body } }

// A blank for the student; the answer, red and underlined, in the guide.
#let ans(body, width: 7em) = context {
  if solutions.get() {
    text(fill: sol-color, underline(offset: 2pt, body))
  } else {
    box(width: width, stroke: (bottom: 0.6pt), inset: (bottom: 1pt))[~]
  }
}

// The worked solution under a question; nothing in student mode.
#let sol(body) = context {
  if solutions.get() {
    block(width: 100%, inset: (left: 10pt, top: 3pt, bottom: 3pt),
          stroke: (left: 1.5pt + sol-color), {
      set par(spacing: 7pt)
      text(fill: sol-color, body)
    })
  }
}

// ---- graphs -------------------------------------------------------------
// graph(xmax, ymax, ...items) draws axes in a box; each item is a closure
// (px, py) => content produced by seg / pt below, where px and py map data
// coordinates to positions inside the box.

#let graph(xmax, ymax, xlabel: "", ylabel: "", w: 210pt, h: 160pt,
           xticks: (), yticks: (), ..items) = {
  let m = 26pt
  let px(x) = m + (w - 2 * m) * x / xmax
  let py(y) = h - m - (h - 2 * m) * y / ymax
  box(width: w, height: h, {
    place(line(start: (px(0), py(0)), end: (px(xmax) + 10pt, py(0)), stroke: 0.8pt))
    place(line(start: (px(0), py(0)), end: (px(0), py(ymax) - 10pt), stroke: 0.8pt))
    place(dx: px(xmax) + 13pt, dy: py(0) - 5pt, text(size: 9pt, xlabel))
    place(dx: px(0) - 4pt, dy: py(ymax) - 24pt, text(size: 9pt, ylabel))
    for t in xticks {
      place(line(start: (px(t), py(0) - 2pt), end: (px(t), py(0) + 2pt), stroke: 0.8pt))
      place(dx: px(t) - 5pt, dy: py(0) + 4pt, text(size: 8pt, str(t)))
    }
    for t in yticks {
      place(line(start: (px(0) - 2pt, py(t)), end: (px(0) + 2pt, py(t)), stroke: 0.8pt))
      place(dx: px(0) - 18pt, dy: py(t) - 5pt, text(size: 8pt, str(t)))
    }
    for it in items.pos() { it(px, py) }
  })
}

#let seg(x1, y1, x2, y2, color: black, dash: none, label: none, at: none) = (px, py) => {
  place(line(start: (px(x1), py(y1)), end: (px(x2), py(y2)),
             stroke: (paint: color, thickness: 1.2pt, dash: dash)))
  if label != none {
    let a = if at == none { ((x1 + x2) / 2, (y1 + y2) / 2) } else { at }
    place(dx: px(a.at(0)) + 4pt, dy: py(a.at(1)) - 5pt, text(size: 8pt, fill: color, label))
  }
}

#let pt(x, y, color: black, label: none, dx: 5pt, dy: -11pt) = (px, py) => {
  place(dx: px(x) - 2.5pt, dy: py(y) - 2.5pt, circle(radius: 2.5pt, fill: color, stroke: none))
  if label != none {
    place(dx: px(x) + dx, dy: py(y) + dy, text(size: 8pt, fill: color, label))
  }
}
