// ECON 0100 solution guide for the teaching team. This file is the source; open and
// export it in Plass. Answers and working sit in red solution blocks; everything
// else is what students see.
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 2): set text(size: 14.375pt)
#show heading.where(level: 2): set block(above: 38.410pt, below: 18.473pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Vignette A2 | Advantages | Solutions

_Solution guide for the teaching team. Answers and working are in the red blocks; everything else is what students see._

Colin Creevey can bake $20$ cornish pasties ($P$) or $5$ cauldron cakes ($C$) in one day. Katie Bell also bakes cornish pasties and cauldron cakes at a neighboring bakery. She can bake $15$ pasties or $8$ cakes in one day.

== Q1 | Absolute Advantage

Set up a production table with both Colin and Katie's output per day. Who has the absolute advantage (AA) in pasties? In cakes?

AA in P: \_\_\_\_\_\_\_\_\_\_

AA in C: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *AA in P:* Colin. *AA in C:* Katie.

  #grid(
    columns: (1fr, 1fr),
    gutter: 1em,
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Production per day*], [*Pasties*], [*Cakes*]),
        [Colin], [$20$], [$5$],
        [Katie], [$15$], [$8$],
      ))
    ],
    [
      Absolute advantage is just "who makes more of it in a day": read straight down each column. Colin makes more pasties ($20 > 15$) and Katie makes more cakes ($8 > 5$).
    ],
  )
]

== Q2 | Comparative Advantage

Set up an opportunity cost table with Colin and Katie's opportunity costs for each good. Who has the comparative advantage (CA) in pasties? In cakes?

CA in P: \_\_\_\_\_\_\_\_\_\_

CA in C: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *CA in P:* Colin. *CA in C:* Katie.

  Each cell is "how much of the other good one unit costs," read off the production table: Colin's $20P = 5C$ gives $1C = 4P$ and $1P = \frac{1}{4} C$; Katie's $15P = 8C$ gives $1C = \frac{15}{8} P$ and $1P = \frac{8}{15} C$.

  #grid(
    columns: (1fr, 1fr),
    gutter: 1em,
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Opportunity cost*], [*of 1 pasty*], [*of 1 cake*]),
        [Colin], [$\frac{1}{4}$ C $= 0.25$ C], [$4$ P],
        [Katie], [$\frac{8}{15}$ C $\approx 0.53$ C], [$\frac{15}{8}$ P $= 1.875$ P],
      ))
    ],
    [
      Comparative advantage goes to the lower opportunity cost, again reading down each column. Pasties: $\frac{1}{4} < \frac{8}{15}$, so Colin. Cakes: $\frac{15}{8} < 4$, so Katie. Here AA and CA line up, which is why Q3 exists.
    ],
  )

  A useful check: the two entries in a row are reciprocals, so whoever has the lower cost in one good has the higher cost in the other. Nobody can have the comparative advantage in both.
]

== Q3 | Better at Both

Suppose Katie buys a new oven and can now bake $25$ pasties or $8$ cakes in one day. Update both tables. Who has the comparative advantage in each good?

CA in P: \_\_\_\_\_ CA in C: \_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *CA in P:* Colin. *CA in C:* Katie.

  #grid(
    columns: (1fr, 1fr),
    gutter: 1em,
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Production per day*], [*Pasties*], [*Cakes*]),
        [Colin], [$20$], [$5$],
        [Katie (new oven)], [$25$], [$8$],
      ))
    ],
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Opportunity cost*], [*of 1 pasty*], [*of 1 cake*]),
        [Colin], [$\frac{1}{4}$ C $= 0.25$ C], [$4$ P],
        [Katie (new oven)], [$\frac{8}{25}$ C $= 0.32$ C], [$\frac{25}{8}$ P $= 3.125$ P],
      ))
    ],
  )

  Katie now makes more of both goods, so she has the absolute advantage in both. Her opportunity costs change: $25P = 8C$ gives $1C = \frac{25}{8} P$ and $1P = \frac{8}{25} C$; Colin's row is unchanged. Pasties: $\frac{1}{4} < \frac{8}{25}$, so Colin still has the comparative advantage in pasties. Cakes: $\frac{25}{8} < 4$, so Katie keeps the comparative advantage in cakes.

  The point of the question: Katie is better at both, but _relatively_ much better at cakes ($\frac{8}{5}$ as many cakes as Colin, only $\frac{25}{20}$ as many pasties), so her cheap good is cakes and Colin's is pasties. Absolute advantage in both never means comparative advantage in both.
]
