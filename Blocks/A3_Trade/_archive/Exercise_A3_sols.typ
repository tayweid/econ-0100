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

= ECON 0100 | Exercise A3 | Trade

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  = Solutions

]

_Answers and work are shown in the red blocks._

Hagrid can bake 20 rock cakes ($R$) or 30 fruitcakes ($F$) in one day and Professor McGonagall can bake 10 rock cakes or 5 fruitcakes in one day _(from Exercise A2)_.

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  The tables from Exercise A2, which every question below reads from:

  #grid(
    columns: (1fr, 1fr),
    gutter: 1em,
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Production per day*], [*Rock cakes* ($R$)], [*Fruitcakes* ($F$)]),
        [Hagrid], [$20$], [$30$],
        [McGonagall], [$10$], [$5$],
      ))
    ],
    [
      #align(center, table(
        columns: 3,
        align: (center, center, center),
        table.header([*Opportunity cost*], [*of 1R*], [*of 1F*]),
        [Hagrid], [$\frac{3}{2}$ F], [$\frac{2}{3}$ R],
        [McGonagall], [$\frac{1}{2}$ F], [$2$ R],
      ))
    ],
  )
]

== Q1 | Specialization

Like we found in Exercise A2, Hagrid has the comparative advantage in fruitcakes and McGonagall in rock cakes. How much does each baker produce in one day if they specialize accordingly?

Hagrid: \_\_\_\_\_\_\_\_\_\_

McGonagall: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *Hagrid:* $30$ fruitcakes. *McGonagall:* $10$ rock cakes.

  Specializing means a full day on the good with the comparative advantage and none of the other: Hagrid spends his day at the fruitcake end of his PPF, $30$F, and McGonagall at the rock cake end of hers, $10$R. Between them that is $10$R and $30$F, and the trade in Q2 is what lets each of them end up with some of both.
]

== Q2 | Trade

Suppose Hagrid and McGonagall decide they want to specialize and trade goods. After they specialize, what is a trade that would make them both better off?

1 $R$ for \_\_\_\_\_\_\_\_\_\_ $F$

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  $1$R for $1$F.

  Find any ratio between their opportunity costs of a rock cake, McGonagall's $\frac{1}{2}$ F and Hagrid's $\frac{3}{2}$ F:

  #mitex(`
  \tfrac{1}{2} F < x F < \tfrac{3}{2} F
  `)

  For example $1$R for $1$F works. McGonagall gives up a rock cake that cost her half a fruitcake and gets a whole fruitcake back, and Hagrid gets a rock cake for one fruitcake when baking it himself would cost him $\frac{3}{2}$. Any rate inside the range earns full credit.
]

== Q3 | Workable Rates

Not every exchange rate works for both bakers. What is the range of exchange rates that would make both Hagrid and McGonagall better off?

Between \_\_\_\_\_\_\_\_\_\_ and \_\_\_\_\_\_\_\_\_\_ $F$ per $1$ $R$

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  Between $\frac{1}{2}$ and $\frac{3}{2}$ F per $1$R.

  The two opportunity costs of a rock cake are the bounds. McGonagall sells rock cakes, and a rock cake costs her $\frac{1}{2}$ F to bake, so she needs more than $\frac{1}{2}$ F for each one or she would rather keep it. Hagrid buys rock cakes, and a rock cake costs him $\frac{3}{2}$ F to bake, so he pays less than $\frac{3}{2}$ F for each one or he would rather bake it himself. Rates below $\frac{1}{2}$ leave McGonagall worse off and rates above $\frac{3}{2}$ leave Hagrid worse off; at either bound one baker is exactly indifferent and nobody gains.
]
