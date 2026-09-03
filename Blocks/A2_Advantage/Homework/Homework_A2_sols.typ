// Homework A2 with answers, for the teaching team. Questions mirror
// Homework_A2.md. From the repo root:
//   typst compile --root . Blocks/A2_Advantage/Homework/Homework_A2_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#heading(level: 1)[Homework A2 | ECON 0100 | Fall 2026 #sols-only[#text(fill: sol-color)[| Solutions]]]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see. Students answer on paper and submit selections on Gradescope, where the homework is completion-graded._]

== The Hogsmeade Candy Shop Saga

Honeydukes and Zonkos are two candy shops in Hogsmeade. Both shops make two types of popular candy, Chocolate Frogs ($F$) and Ice Mice ($M$). Devoting all their resources to one good, Honeydukes can make $100$ pounds of $F$ or $75$ pounds of $M$ each week, and Zonkos can make $200$ pounds of $F$ or $100$ pounds of $M$.

Construct a production table and an opportunity cost table to keep track of your work as you move through the questions.

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

  Each opportunity cost comes from the shop's own trade-off: Honeydukes' $100F = 75M$ gives $1F = 3/4 M$ and $1M = 4/3 F$; Zonkos' $200F = 100M$ gives $1F = 1/2 M$ and $1M = 2F$. The two entries in a row are reciprocals.
]

== Q1 | Absolute Advantage

a) Which shop has the absolute advantage in Chocolate Frogs? #ans[Zonkos]

b) Which shop has the absolute advantage in Ice Mice? #ans[Zonkos]

#sol[
  Absolute advantage is "who makes more in a week," read down each column of the production table. Zonkos makes more of both: $200 > 100$ Frogs and $100 > 75$ Mice.
]

== Q2 | Opportunity Costs

In Homework A1 you found Honeydukes' opportunity cost of $1$F. Fill in the rest of the opportunity cost table.

a) What is Honeydukes' opportunity cost of $1$M? #ans[$4/3$ pounds of F]

b) What is Zonkos' opportunity cost of $1$F? #ans[$1/2$ pound of M]

c) What is Zonkos' opportunity cost of $1$M? #ans[$2$ pounds of F]

#sol[
  Honeydukes gives up $100$F to make $75$M, so each pound of Mice costs $100/75 = 4/3$ pounds of Frogs (the reciprocal of the $3/4$ M from Homework A1). Zonkos gives up $100$M to make $200$F, so a pound of Frogs costs $100/200 = 1/2$ pound of Mice, and a pound of Mice costs $200/100 = 2$ pounds of Frogs.
]

== Q3 | Comparative Advantage

a) Which shop has the comparative advantage in Chocolate Frogs? #ans[Zonkos]

b) Which shop has the comparative advantage in Ice Mice? #ans[Honeydukes]

c) Zonkos has the absolute advantage in both goods. Explain why it can't have the comparative advantage in both.

#sol[
  Comparative advantage goes to the lower opportunity cost, read down each column of the opportunity cost table. Frogs: $1/2 < 3/4$, so Zonkos. Mice: $4/3 < 2$, so Honeydukes.

  *c)* A shop's two opportunity costs are reciprocals of each other. Zonkos gives up less M per F than Honeydukes ($1/2 < 3/4$), which is the same fact as Zonkos giving up more F per M ($2 > 4/3$). Having the lower cost in one good forces the higher cost in the other, so the comparative advantages always split. Absolute advantage compares totals; comparative advantage compares ratios, and a ratio can only favor one side.
]

== Q4 | Changes in Labor and Technology

Gringotts decides to fund Zonkos' purchase of a more capable Ice Mice machine, doubling Zonkos' Ice Mice production. At the same time, Honeydukes triples their labor hours, tripling their productive capacity. Construct an updated production table and opportunity cost table before answering.

#sol[
  #grid(columns: (auto, auto), gutter: 16pt, align: horizon,
    table(
      columns: 3, align: center,
      [*Production per week*], [*Frogs ($F$)*], [*Mice ($M$)*],
      [Honeydukes ($3 times$ labor)], [$300$], [$225$],
      [Zonkos (new machine)], [$200$], [$200$],
    ),
    table(
      columns: 3, align: center,
      [*Opportunity cost*], [*of 1F*], [*of 1M*],
      [Honeydukes], [$3/4$ M], [$4/3$ F],
      [Zonkos], [$1$ M], [$1$ F],
    ),
  )

  #grid(columns: (auto, auto), gutter: 20pt, align: horizon,
    graph(360, 260, w: 200pt, h: 130pt, xlabel: [$F$], ylabel: [$M$], xticks: (100, 300), yticks: (75, 225),
      seg(0, 75, 100, 0, color: black, label: [old], at: (5, 20)),
      seg(0, 225, 300, 0, color: sol-color, label: [new: $3 times$ labor], at: (150, 130)),
    ),
    graph(240, 240, w: 200pt, h: 130pt, xlabel: [$F$], ylabel: [$M$], xticks: (200,), yticks: (100, 200),
      seg(0, 100, 200, 0, color: black, label: [old], at: (30, 45)),
      seg(0, 200, 200, 0, color: sol-color, label: [new: Mice machine], at: (95, 140)),
    ),
  )
  #text(size: 9pt)[Honeydukes (left): more labor scales both intercepts by $3$, a parallel shift out. Zonkos (right): the machine only raises the Mice intercept, so the PPF pivots and its slope changes.]
]

a) After both changes, which shop has the absolute advantage in each good? #ans[Honeydukes in both]

b) After both changes, what is Honeydukes' opportunity cost of $1$F? What is Zonkos'? #ans[Honeydukes $3/4$ M; Zonkos $1$ M]

c) After both changes, which shop has the comparative advantage in each good? #ans[Honeydukes in F, Zonkos in M]

#sol[
  *a)* Honeydukes now makes more of both: $300 > 200$ Frogs and $225 > 200$ Mice.

  *b)* Tripling labor scales both of Honeydukes' intercepts by the same factor, so its trade-off is unchanged: $300F = 225M$ still gives $1F = 3/4 M$. Zonkos' machine changes only Mice, so its trade-off does change: $200F = 200M$ gives $1F = 1M$ and $1M = 1F$.

  *c)* Frogs: $3/4 < 1$, so Honeydukes. Mice: $1 < 4/3$, so Zonkos. The advantages have flipped from Q3 even though Zonkos got better at Mice: comparative advantage is about ratios, and Zonkos' improvement in Mice made its Frogs relatively more expensive.
]
