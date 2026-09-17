// Vignette B2 with answers, for the teaching team. Questions mirror
// Vignette_B2.typ. The working follows the Fall 2024 handwritten guides in
// ../Practice_Bank (Vignette_B1_sols.pdf, Vignette_B2_sols.pdf,
// Classwork_B1_sols.pdf): intercepts, the substitution chain to a quantity,
// then area = h · b · 1/2. Compiled alone this is the B2 solution guide; the
// Recitations/ files include it. From the repo root:
//   typst compile --root . Blocks/B2_Supply/Vignette/Vignette_B2_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#vtitle[Vignette B2][Supply]

_Due in Recitation._

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see. Q1 is the consumer surplus practice Vignette B1 did not reach._]

== Q1 | Consumer Surplus

Members of the wizarding world have preferences for pumpkin pasties according to the following demand curve:

$ P_d = 12 - 1/2 Q_d $

Prices are in galleons and quantity is in pasties.

a) Plot and find the consumer surplus at a price of $10$ galleons. #ans[$4$ galleons]

b) Plot and find the consumer surplus at a price of $5$ galleons. #ans[$49$ galleons]

c) How much did consumer surplus change from (a) to (b)? #ans[up by $45$ galleons]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [*Plot.* Vertical intercept, $Q_d = 0$: $P_d = 12$. Horizontal intercept, $P_d = 0$: $0 = 12 - 1/2 Q_d arrow.r Q_d = 24$.

    *a)* Price to quantity, then the triangle below demand and above the price:
    $ 10 = 12 - 1/2 Q_d arrow.r 1/2 Q_d = 2 arrow.r Q_d = 4 $
    $ "CS" = h dot b dot 1/2 = (12 - 10) dot 4 dot 1/2 = 4 $

    *b)* The same steps at the lower price:
    $ 5 = 12 - 1/2 Q_d arrow.r 1/2 Q_d = 7 arrow.r Q_d = 14 $
    $ "CS"' = h dot b dot 1/2 = (12 - 5) dot 14 dot 1/2 = 49 $

    *c)* The change is the new area minus the old, the strip between the two price lines:
    $ Delta "CS" = "CS"' - "CS" = 49 - 4 = 45 $],
    graph(28, 14, w: 200pt, h: 140pt, xlabel: [$Q$], ylabel: [$P$], xticks: (4, 14, 24), yticks: (5, 10, 12),
      shade(((0, 12), (0, 5), (14, 5)), color: sol-color),
      shade(((0, 12), (0, 10), (4, 10)), color: sol-color),
      seg(0, 12, 24, 0, color: black, label: [$D$], at: (20, 2)),
      seg(0, 10, 4, 10, color: gray, dash: "dotted"),
      seg(0, 5, 14, 5, color: gray, dash: "dotted"),
      pt(4, 10, color: sol-color), pt(14, 5, color: sol-color),
      lbl(0.3, 11.95)[CS], lbl(3, 8.4)[$Delta$CS],
    ),
  )
]

== Q2 | Quantity Supplied

Pumpkin pasties are produced by many sellers according to the following supply curve:

$ P = 2 + 1/2 Q_s $

Plot the supply curve below.

a) Find and plot the quantity supplied at a price of $10$ galleons. #ans[$16$ pasties]

b) Find and plot the quantity supplied at a price of $5$ galleons. #ans[$6$ pasties]

c) How much did quantity supplied change from (a) to (b)? #ans[down by $10$ pasties]

d) What is marginal cost at $8$ pasties? #ans[$6$ galleons]

#sol[
  *Plot.* Vertical intercept, $Q_s = 0$: $P = 2$. Below $2$ galleons quantity supplied is zero, so the curve starts there and rises by $1$ galleon for every $2$ pasties.

  *a)* $10 = 2 + 1/2 Q_s arrow.r 8 = 1/2 Q_s arrow.r Q_s = 16$ #h(2em) *b)* $5 = 2 + 1/2 Q_s arrow.r 3 = 1/2 Q_s arrow.r Q_s = 6$

  *c)* $Delta Q_s = 6 - 16 = -10$: quantity supplied fell by $10$ pasties as the price fell, the law of supply.

  *d)* Quantity to price. The height of the supply curve at $8$ pasties is the marginal cost of the eighth pasty: $P = 2 + 1/2 dot 8 = 6$ galleons.
]

== Q3 | Producer Surplus

Plot and calculate the producer surplus at both $5$ galleons and $10$ galleons.

a) PS at $5$ galleons: #ans[$9$ galleons]

b) PS at $10$ galleons: #ans[$64$ galleons]

c) How much did producer surplus change from (a) to (b)? #ans[up by $55$ galleons]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Producer surplus is the triangle above supply and below the price, out to the quantity sold from Q2. Its height is the price minus the $2$-galleon intercept and its base is the quantity.

    $ P = 5: quad "PS" = h dot b dot 1/2 = (5 - 2) dot 6 dot 1/2 = 9 $
    $ P = 10: quad "PS"' = h dot b dot 1/2 = (10 - 2) dot 16 dot 1/2 = 64 $

    *c)* $Delta "PS" = "PS"' - "PS" = 64 - 9 = 55$: producer surplus rose by $55$ galleons as the price rose from $5$ to $10$. Revenue at $10$ galleons is the rectangle $10 dot 16 = 160$; the $64$ above the curve is surplus and the $96$ below it covers marginal costs.],
    graph(22, 13, w: 200pt, h: 140pt, xlabel: [$Q$], ylabel: [$P$], xticks: (6, 16), yticks: (2, 5, 10),
      shade(((0, 2), (0, 10), (16, 10)), color: sol-color),
      shade(((0, 2), (0, 5), (6, 5)), color: sol-color),
      seg(0, 2, 20, 12, color: black, label: [$S$], at: (17, 11)),
      seg(0, 10, 16, 10, color: gray, dash: "dotted"),
      seg(0, 5, 6, 5, color: gray, dash: "dotted"),
      pt(16, 10, color: sol-color), pt(6, 5, color: sol-color),
      lbl(0.6, 4.6)[PS], lbl(3, 9.2)[$Delta$PS],
    ),
  )
]
