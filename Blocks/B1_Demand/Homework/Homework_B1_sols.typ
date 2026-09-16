// Homework B1 with answers, for the teaching team. Questions mirror
// Homework_B1.md. The working follows the Fall 2022 handwritten guide in
// ../../B2_Supply/Practice_Bank/Homework_B_demo_sols_2.pdf: intercepts, the
// substitution chain to a quantity, then area = h · b · 1/2. From the repo root:
//   typst compile --root . Blocks/B1_Demand/Homework/Homework_B1_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#heading(level: 1)[Homework B1 | ECON 0100 | Fall 2026 #sols-only[#text(fill: sol-color)[| Solutions]]]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see. Students answer on paper and submit selections on Gradescope, where the homework is completion-graded._]

== Butterbeer

Preferences for butter beer can be represented by the following demand curve:

$ P_d = 100 - 1/2 Q_d $

Prices are in galleons and quantity is in bottles.

== Q1 | Quantity Demanded

Use a graph to plot this demand curve, including the quantity demanded at both $40$ galleons and $50$ galleons.

a) Quantity demanded at $40$ galleons: #ans[$120$ bottles]

b) Quantity demanded at $50$ galleons: #ans[$100$ bottles]

c) How much did quantity demanded change as the price dropped from $50$ to $40$? #ans[up by $20$ bottles]

d) What is the marginal benefit at a quantity of $100$? #ans[$50$ galleons]

#sol[
  *Plot.* Vertical intercept, $Q_d = 0$: $P_d = 100$. Horizontal intercept, $P_d = 0$: $0 = 100 - 1/2 Q_d arrow.r 1/2 Q_d = 100 arrow.r Q_d = 200$.

  *a)* $40 = 100 - 1/2 Q_d arrow.r 1/2 Q_d = 60 arrow.r Q_d = 120$ #h(2em) *b)* $50 = 100 - 1/2 Q_d arrow.r 1/2 Q_d = 50 arrow.r Q_d = 100$

  *c)* $Delta Q_d = 120 - 100 = 20$: quantity demanded rose by $20$ bottles as the price fell, the law of demand.

  *d)* Quantity to price. The height of demand at $100$ bottles is the marginal benefit of the hundredth bottle: $P_d = 100 - 1/2 dot 100 = 50$ galleons. It matches b): $50$ galleons is the price at which $100$ bottles are demanded.
]

== Q2 | Consumer Surplus

Then find and label the consumer surplus at these prices.

a) CS at $40$ galleons: #ans[$3600$ galleons]

b) CS at $50$ galleons: #ans[$2500$ galleons]

c) How much did consumer surplus change as the price dropped from $50$ to $40$? #ans[up by $1100$ galleons]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Consumer surplus is the triangle below demand and above the price, out to the quantity bought from Q1. Its height is the $100$-galleon intercept minus the price and its base is the quantity.

    $ P = 40: quad "CS" = h dot b dot 1/2 = (100 - 40) dot 120 dot 1/2 = 60 dot 60 = 3600 $
    $ P = 50: quad "CS"' = h dot b dot 1/2 = (100 - 50) dot 100 dot 1/2 = 50 dot 50 = 2500 $

    *c)* $Delta "CS" = "CS" - "CS"' = 3600 - 2500 = 1100$: consumer surplus rose by $1100$ galleons, the strip between the two price lines. Expenditure is the rectangle below the price: $40 dot 120 = 4800$ at $40$ galleons and $50 dot 100 = 5000$ at $50$.],
    graph(220, 110, w: 200pt, h: 140pt, xlabel: [$Q$], ylabel: [$P$], xticks: (100, 120, 200), yticks: (40, 50, 100),
      shade(((0, 100), (0, 40), (120, 40)), color: sol-color),
      shade(((0, 100), (0, 50), (100, 50)), color: sol-color),
      seg(0, 100, 200, 0, color: black, label: [$D$], at: (170, 18)),
      seg(0, 40, 120, 40, color: gray, dash: "dotted"),
      seg(0, 50, 100, 50, color: gray, dash: "dotted"),
      pt(120, 40, color: sol-color), pt(100, 50, color: sol-color),
      lbl(10, 82)[CS], lbl(30, 49)[$Delta$CS],
    ),
  )
]
