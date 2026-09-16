// Homework B2 with answers, for the teaching team. Questions mirror
// Homework_B2.md. From the repo root:
//   typst compile --root . Blocks/B2_Supply/Homework/Homework_B2_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#heading(level: 1)[Homework B2 | ECON 0100 | Fall 2026 #sols-only[#text(fill: sol-color)[| Solutions]]]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see. Students answer on paper and submit selections on Gradescope, where the homework is completion-graded._]

== Butterbeer

The supply curve for butter beer can be represented by the following equation:

$ P = 20 + 1/2 Q $

Prices are in galleons and quantity is in bottles.

== Q1 | Quantity Supplied

Use a graph to plot this supply curve, including the quantity supplied at both $40$ galleons and $50$ galleons.

a) Quantity supplied at $40$ galleons: #ans[$40$ bottles]

b) Quantity supplied at $50$ galleons: #ans[$60$ bottles]

c) How much did quantity supplied change as the price dropped from $50$ to $40$? #ans[down by $20$ bottles]

d) What is marginal cost at a quantity of $60$? #ans[$50$ galleons]

#sol[
  The vertical intercept is $20$ galleons: below that price nobody sells. Price to quantity: *a)* $40 = 20 + 1/2 Q$ gives $Q = 40$; *b)* $50 = 20 + 1/2 Q$ gives $Q = 60$; *c)* $40 - 60 = -20$, so quantity supplied fell by $20$ bottles, the law of supply. Quantity to price: *d)* the height of supply at $60$ bottles is $20 + 1/2 dot 60 = 50$ galleons, the marginal cost of the sixtieth bottle, which matches b).
]

== Q2 | Producer Surplus

Then find and label the producer surplus at these prices.

a) PS at $40$ galleons: #ans[$400$ galleons]

b) PS at $50$ galleons: #ans[$900$ galleons]

c) How much did producer surplus change as the price dropped from $50$ to $40$? #ans[down by $500$ galleons]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Producer surplus is the triangle above supply and below the price, out to the quantity sold; its height is the price minus the $20$-galleon intercept.

    *a)* $1/2 dot 40 dot (40 - 20) = 400$ galleons. Revenue is the rectangle $40 dot 40 = 1600$; the $1200$ under the curve covers marginal costs.

    *b)* $1/2 dot 60 dot (50 - 20) = 900$ galleons. Revenue is $50 dot 60 = 3000$.

    *c)* $400 - 900 = -500$: producer surplus fell by $500$ galleons, $10$ less on each of the $40$ bottles still sold ($400$) plus the triangle on the $20$ bottles no longer sold ($100$).],
    graph(110, 75, w: 200pt, h: 140pt, xlabel: [$Q$], ylabel: [$P$], xticks: (40, 60), yticks: (20, 40, 50),
      shade(((0, 20), (0, 50), (60, 50)), color: sol-color),
      shade(((0, 20), (0, 40), (40, 40)), color: sol-color),
      seg(0, 20, 100, 70, color: black, label: [$S$], at: (88, 68)),
      seg(0, 40, 40, 40, color: gray, dash: "dotted"),
      seg(0, 50, 60, 50, color: gray, dash: "dotted"),
      pt(40, 40, color: sol-color), pt(60, 50, color: sol-color),
    ),
  )
]
