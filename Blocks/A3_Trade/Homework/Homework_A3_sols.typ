// Homework A3 with answers, for the teaching team. Questions mirror
// Homework_A3.md. From the repo root:
//   typst compile --root . Blocks/A3_Trade/Homework/Homework_A3_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#heading(level: 1)[Homework A3 | ECON 0100 | Fall 2026 #sols-only[#text(fill: sol-color)[| Solutions]]]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see. Students answer on paper and submit selections on Gradescope, where the homework is completion-graded._]

== The Hogsmeade Candy Shop Saga

Honeydukes and Zonkos are two candy shops in Hogsmeade. Both shops make two types of popular candy, Chocolate Frogs ($F$) and Ice Mice ($M$). Devoting all their resources to one good, Honeydukes can make $100$ pounds of $F$ or $75$ pounds of $M$ each week, and Zonkos can make $200$ pounds of $F$ or $100$ pounds of $M$.

Use the production table and opportunity cost table you built in Homework A2.

#sol[
  #grid(columns: (auto, auto), gutter: 16pt, align: horizon,
    table(
      columns: 3, align: center,
      [*Production per week*], [*Frogs ($F$)*], [*Mice ($M$)*],
      [Honeydukes], [$100$], [$75$],
      [Zonkos], [$200$], [$100$],
    ),
    table(
      columns: 3, align: center,
      [*Opportunity cost*], [*of 1F*], [*of 1M*],
      [Honeydukes], [$3/4$ M], [$4/3$ F],
      [Zonkos], [$1/2$ M], [$2$ F],
    ),
  )
  PPFs, with $M$ on the vertical as in Homework A1: Honeydukes $M = 75 - 3/4 F$; Zonkos $M = 100 - 1/2 F$.
]

== Q1 | Specialization

a) If the two shops want to jointly produce more, which good should each shop specialize in? #ans[Zonkos in F, Honeydukes in M]

b) If each shop fully specializes, how many pounds of each candy do the two shops make in total each week? #ans[$200$F and $75$M]

#sol[
  Each shop specializes in its comparative advantage, the good it makes at lower opportunity cost. Frogs cost Zonkos $1/2$ M and Honeydukes $3/4$ M, so Zonkos makes Frogs; Mice cost Honeydukes $4/3$ F and Zonkos $2$ F, so Honeydukes makes Mice. Fully specialized, Zonkos makes $200$F and Honeydukes $75$M, so the pair makes $200$F and $75$M in total.
]

== Q2 | Terms of Trade

The two shops decide to specialize, trade, and sell each other's goods at their shops.

a) What's an exchange rate that would facilitate a trade of Ice Mice for Chocolate Frogs? Give it in pounds of $F$ per pound of $M$. #ans[e.g. $3/2$ F per M]

b) Explain why any exchange rate between the two shops' opportunity costs of Ice Mice would work.

#sol[
  *a)* Any rate strictly between the two opportunity costs of a pound of Mice works: $ 4/3 " F per M" < "rate" < 2 " F per M". $ $3/2$ or $5/3$ F per M are natural picks; $1$ and $3$ are outside the range and fail (see Q3).

  *b)* Honeydukes is selling Mice. Making a pound of Mice costs it $4/3$ F of forgone Frogs, so it accepts any price above $4/3$ F per M: it gets more Frogs by trading than by baking them. Zonkos is buying Mice. Making a pound itself costs $2$ F, so it accepts any price below $2$ F per M: it gets the Mice cheaper by trading than by making them. Between $4/3$ and $2$ both conditions hold at once, so both shops beat what they could do alone.
]

== Q3 | Accept or Reject

Suppose both shops specialize according to their comparative advantage: Zonkos makes only Chocolate Frogs and Honeydukes only Ice Mice.

a) Zonkos offers $1$F for each $1$M. Which shop rejects the offer, and why? #ans[Honeydukes]

b) Honeydukes counters with $1$M for $3$F. Which shop rejects the counteroffer, and why? #ans[Zonkos]

c) They settle on $1$M for $3/2$F and trade $40$M for $60$F. How much of each candy does each shop end up with? #ans[Honeydukes $60$F and $35$M; Zonkos $140$F and $40$M]

d) Use a graph or algebra to show whether each shop ends up beyond its own PPF. #ans[Both do]

#sol[
  *a)* $1$ F per M is below Honeydukes' own cost of $4/3$ F per M. Honeydukes can turn a pound of Mice into $4/3$ pounds of Frogs by shifting its own production, so selling a pound for only $1$ F is a bad deal, and it rejects. (Zonkos would love it: $1 < 2$.)

  *b)* $3$ F per M is above Zonkos' own cost of $2$ F per M. Zonkos can make a pound of Mice itself for $2$ F, so paying $3$ F is worse than staying home, and it rejects. (Honeydukes would love it: $3 > 4/3$.)

  *c)* Honeydukes starts with $75$M, sends $40$M and receives $60$F: it ends with $60$F and $35$M. Zonkos starts with $200$F, sends $60$F and receives $40$M: it ends with $140$F and $40$M. The rate checks out, $60/40 = 3/2$ F per M.

  *d)* *Algebra:* Honeydukes' PPF at $F = 60$ allows $M = 75 - 3/4 (60) = 30$, and it has $35 > 30$. Zonkos' PPF at $F = 140$ allows $M = 100 - 1/2 (140) = 30$, and it has $40 > 30$. Both consumption bundles lie beyond their own frontiers, which is what a trade inside the Q2 range delivers.

  #grid(columns: (auto, auto), gutter: 20pt, align: horizon,
    graph(120, 90, w: 200pt, h: 130pt, xlabel: [$F$], ylabel: [$M$], xticks: (60, 100), yticks: (35, 75),
      seg(0, 75, 100, 0, color: black, label: [Honeydukes' PPF], at: (62, 62)),
      seg(60, 0, 60, 35, color: gray, dash: "dotted"),
      pt(60, 35, color: sol-color, label: [$(60, 35)$ with trade], dx: 6pt, dy: -9pt),
    ),
    graph(240, 120, w: 200pt, h: 130pt, xlabel: [$F$], ylabel: [$M$], xticks: (140, 200), yticks: (40, 100),
      seg(0, 100, 200, 0, color: black, label: [Zonkos' PPF], at: (120, 80)),
      seg(140, 0, 140, 40, color: gray, dash: "dotted"),
      pt(140, 40, color: sol-color, label: [$(140, 40)$ with trade], dx: 6pt, dy: -9pt),
    ),
  )
]

== Q4 | Changing Labor

Zonkos' owner decides to go half-time, cutting Zonkos' labor in half.

a) Set up Zonkos' old and new PPF on the same graph. What are Zonkos' new maximum weekly outputs, and what is its new opportunity cost of $1$F? #ans[$100$F or $50$M; still $1/2$ M]

b) Write a short description of how this change affects the trade with Honeydukes.

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [*a)* Half the labor halves both intercepts: $100$F or $50$M, so the new PPF is $M = 50 - 1/2 F$, a parallel shift in. Both intercepts fell by the same factor, so the slope, and with it the opportunity cost of a pound of Frogs, is unchanged at $1/2$ M. Less time changes how much Zonkos can make, not the rate at which its two candies trade off.

    *b)* Neither shop's opportunity cost moved, so the range of exchange rates both accept is still $4/3$ to $2$ F per M, and the $3/2$ deal from Q3 still works. What changes is the volume: Zonkos now has at most $100$F to trade away instead of $200$, so the most trade the pair can do falls. (The Q3 trade of $60$F is still feasible, but it now takes most of Zonkos' output.)],
    graph(240, 120, w: 190pt, h: 130pt, xlabel: [$F$], ylabel: [$M$], xticks: (100, 200), yticks: (50, 100),
      seg(0, 100, 200, 0, color: black, label: [old], at: (150, 30)),
      seg(0, 50, 100, 0, color: sol-color, label: [new], at: (30, 55)),
    ),
  )
]
