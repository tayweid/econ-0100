// Figure helpers for the solution guides. Each guide (Blocks/<block>/<kind>/
// <Name>_sols.typ, Recitations/Week_N_sols.typ) is one Plass-native Typst file, so
// it cannot call these directly; instead the Plass comment frame at the end of the
// guide imports this file and draws the graphs, one per page, and
// scripts/render-sols-figures compiles that frame and embeds each page in the guide
// as a data-URL #image. Render from anywhere:
//   scripts/render-sols-figures

#let sol-color = rgb("#b3261e")

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

// A shaded region, e.g. a surplus triangle: shade(((0, 12), (0, 10), (4, 10)))
// in data coordinates, drawn under the segments listed after it.
#let shade(pts, color: sol-color) = (px, py) => {
  place(polygon(fill: color.transparentize(78%), stroke: none,
    ..pts.map(p => (px(p.at(0)), py(p.at(1))))))
}

// A small label placed at data coordinates, e.g. lbl(1, 11)[CS].
#let lbl(x, y, body, color: sol-color) = (px, py) => {
  place(dx: px(x), dy: py(y), text(size: 8pt, fill: color, body))
}
