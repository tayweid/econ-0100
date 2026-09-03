// Vignette A3 with answers, for the teaching team. Questions mirror
// Vignette_A3.md. Compiled alone this is the A3 solution guide; the
// Recitations/ files include it. From the repo root:
//   typst compile --root . Blocks/A3_Trade/Vignette/Vignette_A3_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#vtitle[Vignette A3][Trade]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see._]

Colin Creevey can bake $20$ cornish pasties ($P$) or $5$ cauldron cakes ($C$) in one day, and Katie Bell, back on her original oven, can bake $15$ pasties or $8$ cakes.

== Q1 | Trade

Suppose Colin and Katie realize they can specialize and trade goods. After they specialize, what is a trade that would make them both better off?

$1$ $C$ for #ans[$3$] $P$ #sols-only[#h(1em) _(any rate strictly between $15/8$ and $4$ pasties per cake is correct)_]

#sol[
  Opportunity cost of a cake: Colin $4P$, Katie $15/8 P$. Katie has the comparative advantage in cakes and Colin in pasties, so Katie bakes cakes all day ($8C$) and Colin bakes pasties all day ($20P$). A price for cakes works when it sits between the two opportunity costs, $15/8 < "price of 1 cake" < 4$ pasties. Below $4$, Colin pays less for a cake than baking one costs him; above $15/8$, Katie gets more for a cake than baking one costs her. Any number in the range is correct; $2$ or $3$ are the natural answers.

  *Worked check at $1C$ for $3P$*, trading $2$ cakes for $6$ pasties. Colin ends with $14P$ and $2C$; his own PPF only allows $12P$ at $C = 2$, so he consumes beyond his frontier. Katie ends with $6C$ and $6P$; her PPF allows only $3.75P$ at $C = 6$, so she does too. Common wrong answers: a rate outside the range, or specializing in the wrong goods.
]

== Q2 | Accept or Reject

Katie offers Colin $1$ cake for $5$ pasties. Does Colin accept? Why or why not?

Accept or Reject: #ans[Reject]

#sol[
  Colin's own cost of a cake is $4$ pasties. Paying $5$ pasties for a cake is worse than baking it himself, so he rejects; the price is above the top of the range from Q1. Katie would love this trade ($5 > 15/8$), but a trade needs both sides. The rule students should be able to state: each party accepts only prices better than their own opportunity cost.
]

== Q3 | Changing Labor

It turns out Colin wants to add hours to his job, so he increases from $5$ to $8$ hours per day. Set up Colin's old and new PPF on the same graph. What is Colin's new opportunity cost of cake? Write a short description of how this increase in hours would impact the trade with Katie you found in Q1.

New opportunity cost of 1C: #ans[still $4$ pasties]

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Hours scale by $8/5$, and so does everything Colin can make: $20 dot 8/5 = 32$ pasties or $5 dot 8/5 = 8$ cakes. The new PPF is $P = 32 - 4C$, a parallel shift out of the old one. Both intercepts grow by the same factor, so the slope is unchanged: a cake still costs Colin $4$ pasties. More time changes how much he can make, not the rate at which one good trades for the other inside his own bakery.],
    graph(10, 36, w: 190pt, h: 140pt, xlabel: [$C$], ylabel: [$P$], xticks: (5, 8), yticks: (20, 32),
      seg(0, 20, 5, 0, color: black, label: [old, 5 hrs], at: (0.3, 4)),
      seg(0, 32, 8, 0, color: sol-color, label: [new, 8 hrs], at: (5.2, 14)),
    ),
  )

  *Effect on the trade:* since neither opportunity cost moved, the range of prices both accept is still $15/8$ to $4$ pasties per cake, and the trade from Q1 still works at the same rate. What changes is the volume: Colin now has $32$ pasties to work with instead of $20$, so he can buy more of Katie's cakes. The size of the trade can grow; the terms do not have to.

  Grading note: the key idea is "opportunity cost unchanged, so the exchange rate range is unchanged." Credit "the trade gets bigger" or "Colin has more to trade" without insisting on a specific quantity.
]
