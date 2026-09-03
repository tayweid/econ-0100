// Vignette A2 with answers, for the teaching team. Questions mirror
// Vignette_A2.md. Compiled alone this is the A2 solution guide; the
// Recitations/ files include it. From the repo root:
//   typst compile --root . Blocks/A2_Advantage/Vignette/Vignette_A2_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#vtitle[Vignette A2][Advantages]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see._]

Colin Creevey can bake $20$ cornish pasties ($P$) or $5$ cauldron cakes ($C$) in one day. Katie Bell also bakes cornish pasties and cauldron cakes at a neighboring bakery. She can bake $15$ pasties or $8$ cakes in one day.

== Q1 | Absolute Advantage

Set up a production table with both Colin and Katie's output per day. Who has the absolute advantage (AA) in pasties? In cakes?

AA in P: #ans[Colin]

AA in C: #ans[Katie]

#sol[
  #grid(columns: (auto, 1fr), gutter: 14pt, align: horizon,
    table(
      columns: 3, align: center,
      [*Production per day*], [*Pasties*], [*Cakes*],
      [Colin], [$20$], [$5$],
      [Katie], [$15$], [$8$],
    ),
    [Absolute advantage is just "who makes more of it in a day": read straight down each column. Colin makes more pasties ($20 > 15$) and Katie makes more cakes ($8 > 5$).],
  )
]

== Q2 | Comparative Advantage

Set up an opportunity cost table with Colin and Katie's opportunity costs for each good. Who has the comparative advantage (CA) in pasties? In cakes?

CA in P: #ans[Colin]

CA in C: #ans[Katie]

#sol[
  Each cell is "how much of the other good one unit costs," read off the production table: Colin's $20P = 5C$ gives $1C = 4P$ and $1P = 1/4 C$; Katie's $15P = 8C$ gives $1C = 15/8 P$ and $1P = 8/15 C$.

  #grid(columns: (auto, 1fr), gutter: 14pt, align: horizon,
    table(
      columns: 3, align: center,
      [*Opportunity cost*], [*of 1 pasty*], [*of 1 cake*],
      [Colin], [$1/4$ C $= 0.25$ C], [$4$ P],
      [Katie], [$8/15$ C $approx 0.53$ C], [$15/8$ P $= 1.875$ P],
    ),
    [Comparative advantage goes to the lower opportunity cost, again reading down each column. Pasties: $1/4 < 8/15$, so Colin. Cakes: $15/8 < 4$, so Katie. Here AA and CA line up, which is why Q3 exists.],
  )

  A useful check: the two entries in a row are reciprocals, so whoever has the lower cost in one good has the higher cost in the other. Nobody can have the comparative advantage in both.
]

== Q3 | Better at Both

Suppose Katie buys a new oven and can now bake $25$ pasties or $8$ cakes in one day. Update both tables. Who has the comparative advantage in each good?

CA in P: #ans(width: 4em)[Colin] #h(1em) CA in C: #ans(width: 4em)[Katie]

#sol[
  #grid(columns: (auto, auto), gutter: 14pt, align: horizon,
    table(
      columns: 3, align: center,
      [*Production per day*], [*Pasties*], [*Cakes*],
      [Colin], [$20$], [$5$],
      [Katie (new oven)], [$25$], [$8$],
    ),
    table(
      columns: 3, align: center,
      [*Opportunity cost*], [*of 1 pasty*], [*of 1 cake*],
      [Colin], [$1/4$ C $= 0.25$ C], [$4$ P],
      [Katie (new oven)], [$8/25$ C $= 0.32$ C], [$25/8$ P $= 3.125$ P],
    ),
  )

  Katie now makes more of both goods, so she has the absolute advantage in both. Her opportunity costs change: $25P = 8C$ gives $1C = 25/8 P$ and $1P = 8/25 C$; Colin's row is unchanged. Pasties: $1/4 < 8/25$, so Colin still has the comparative advantage in pasties. Cakes: $25/8 < 4$, so Katie keeps the comparative advantage in cakes.

  The point of the question: Katie is better at both, but *relatively* much better at cakes ($8/5$ as many cakes as Colin, only $25/20$ as many pasties), so her cheap good is cakes and Colin's is pasties. Absolute advantage in both never means comparative advantage in both.
]
