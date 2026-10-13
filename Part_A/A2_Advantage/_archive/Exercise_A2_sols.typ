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

= ECON 0100 | Exercise A2 | Advantages

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  = Solutions

]

_Answers and work are shown in the red blocks._

Professor McGonagall also bakes rock cakes and fruitcakes, up to 10R or 5F in one day.

== Q1 | Comparative and Absolute Advantage

Using Hagrid's original numbers, set up a production table with both Hagrid's and McGonagall's output per day. Who has the absolute advantage (AA) in rock cakes? Then set up an opportunity cost table with Hagrid's and McGonagall's opportunity costs for each good. Who has the comparative advantage (CA) in rock cakes?

AA in R: \_\_\_\_\_\_\_\_\_\_

CA in R: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *AA in R:* Hagrid. *CA in R:* McGonagall.

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

  Hagrid's row is Exercise A1: $20R = 30F$ gives $1R = \frac{3}{2} F$ and $1F = \frac{2}{3} R$. McGonagall's day is $10R = 5F$, so $1R = \frac{5}{10} F = \frac{1}{2} F$ and $1F = \frac{10}{5} R = 2R$. The two entries in a row are reciprocals.

  Absolute advantage is "who bakes more in a day," read down the rock cake column of the production table: $20 > 10$, so Hagrid. Comparative advantage goes to the lower opportunity cost, read down the "of 1R" column of the opportunity cost table: $\frac{1}{2} F < \frac{3}{2} F$, so McGonagall. Hagrid bakes more of both goods, yet McGonagall gives up less to bake a rock cake.
]

== Q2 | Specialization

In Exercise A1, we found that Hagrid can bake 20 rock cakes ($R$) or 30 fruitcakes ($F$) in one day and Professor McGonagall can bake 10 rock cakes or 5 fruitcakes in one day. Use the production table and opportunity cost table developed in Q1 to determine who should specialize in each good if they want to jointly produce more.

Specialize in R: \_\_\_\_\_\_\_\_\_\_

Specialize in F: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *R:* McGonagall. *F:* Hagrid.

  Each baker specializes in the good where they hold the comparative advantage. Rock cakes cost McGonagall $\frac{1}{2}$ F against Hagrid's $\frac{3}{2}$ F, so she bakes the rock cakes; fruitcakes cost Hagrid $\frac{2}{3}$ R against McGonagall's $2$ R, so he bakes the fruitcakes. Absolute advantage plays no part: Hagrid is the better baker of both, and still specializes in only one.
]

== Q3 | Self-Trade

What is the cost to McGonagall of baking 1 fruitcake ($F$) herself? What is an example of a trade with Hagrid that would be better for her?

Cost of 1F: \_\_\_\_\_\_\_\_\_\_

A better trade: \_\_\_\_\_\_\_\_\_\_

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  *Cost of 1F:* $2$ R. *A better trade:* $1$F for $1$R.

  Baking a fruitcake herself costs McGonagall $2$ rock cakes, her opportunity cost from the table. Any trade that gets her a fruitcake for fewer than $2$ rock cakes beats baking it, and Hagrid agrees to anything above his own cost of $\frac{2}{3}$ R per fruitcake. So any rate between $\frac{2}{3}$ R and $2$ R per fruitcake is better for both; $1$F for $1$R is the example on the Gradescope key.
]

== Q4 | Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?

#block(width: 100%, stroke: (left: 2pt + rgb("#c00000")), inset: (left: 1em))[
  #set text(fill: rgb("#c00000"))

  Completion only: any answer earns the point on Gradescope. Bring the concepts named here to recitation.
]
