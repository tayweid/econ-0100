// Homework B2 with answers, for the teaching team. Questions mirror
// Homework_B2.md. The working follows the Fall 2024 handwritten guides in
// ../Practice_Bank (Vignette_B2_sols.pdf, Classwork_B1_sols.pdf): the
// substitution chain to a quantity, then area = h · b · 1/2. From the repo root:
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
  *Plot.* Vertical intercept, $Q = 0$: $P = 20$. Below $20$ galleons quantity supplied is zero, so the curve starts there and rises by $1$ galleon for every $2$ bottles.

  *a)* $40 = 20 + 1/2 Q arrow.r 20 = 1/2 Q arrow.r Q = 40$ #h(2em) *b)* $50 = 20 + 1/2 Q arrow.r 30 = 1/2 Q arrow.r Q = 60$

  *c)* $Delta Q_s = 40 - 60 = -20$: quantity supplied fell by $20$ bottles as the price fell, the law of supply.

  *d)* Quantity to price. The height of supply at $60$ bottles is the marginal cost of the sixtieth bottle: $P = 20 + 1/2 dot 60 = 50$ galleons. It matches b): $50$ galleons is the price at which $60$ bottles are supplied.
]

== Q2 | Producer Surplus

Then find and label the producer surplus at these prices.

a) PS at $40$ galleons: #ans[$400$ galleons]

b) PS at $50$ galleons: #ans[$900$ galleons]

c) How much did producer surplus change as the price dropped from $50$ to $40$? #ans[down by $500$ galleons]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Producer surplus is the triangle above supply and below the price, out to the quantity sold from Q1. Its height is the price minus the $20$-galleon intercept and its base is the quantity.

    $ P = 40: quad "PS" = h dot b dot 1/2 = (40 - 20) dot 40 dot 1/2 = 400 $
    $ P = 50: quad "PS"' = h dot b dot 1/2 = (50 - 20) dot 60 dot 1/2 = 900 $

    *c)* $Delta "PS" = "PS" - "PS"' = 400 - 900 = -500$: producer surplus fell by $500$ galleons, the strip between the two price lines. Revenue is the rectangle below the price: $40 dot 40 = 1600$ at $40$ galleons and $50 dot 60 = 3000$ at $50$; the rest of each rectangle covers marginal costs.],
    graph(110, 75, w: 200pt, h: 140pt, xlabel: [$Q$], ylabel: [$P$], xticks: (40, 60), yticks: (20, 40, 50),
      shade(((0, 20), (0, 50), (60, 50)), color: sol-color),
      shade(((0, 20), (0, 40), (40, 40)), color: sol-color),
      seg(0, 20, 100, 70, color: black, label: [$S$], at: (88, 68)),
      seg(0, 40, 40, 40, color: gray, dash: "dotted"),
      seg(0, 50, 60, 50, color: gray, dash: "dotted"),
      pt(40, 40, color: sol-color), pt(60, 50, color: sol-color),
      lbl(3, 38)[PS], lbl(20, 48)[$Delta$PS],
    ),
  )
]
