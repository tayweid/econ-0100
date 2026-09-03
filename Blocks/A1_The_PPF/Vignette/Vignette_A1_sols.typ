// Vignette A1 with answers, for the teaching team. Questions mirror
// Vignette_A1.md. Compiled alone this is the A1 solution guide; the
// Recitations/ files include it. From the repo root:
//   typst compile --root . Blocks/A1_The_PPF/Vignette/Vignette_A1_sols.typ
#import "../../_Assets/sols.typ": *
#show: vignette-setup

#vtitle[Vignette A1][PPF]

#sols-only[_Solution guide for the teaching team. Answers and working are in red; everything in black is what students see._]

Colin Creevey can bake $20$ cornish pasties ($P$) or $5$ cauldron cakes ($C$) in one day. Set up Colin's PPF on an $x,y$ graph with pasties ($P$) on the vertical and cakes ($C$) on the horizontal. Label the axes and the intercepts.

#sol[
  #grid(columns: (1fr, auto), gutter: 12pt, align: horizon,
    [Intercepts: $20$ pasties on the vertical axis (a full day on pasties) and $5$ cakes on the horizontal (a full day on cakes). The PPF is the line between them, $P = 20 - 4C$. The Q2 bundle $(2, 10)$ is marked below the frontier.],
    graph(6, 24, w: 180pt, h: 118pt, xlabel: [$C$], ylabel: [$P$], xticks: (2, 5), yticks: (10, 12, 20),
      seg(0, 20, 5, 0, color: sol-color, label: [$P = 20 - 4C$], at: (4.4, 3)),
      pt(2, 12, color: sol-color, label: [efficient], dy: -13pt),
      pt(2, 10, color: black, label: [inefficient], dx: -42pt, dy: 3pt),
    ),
  )
]

== Q1 | Opportunity Cost

What is Colin's opportunity cost of producing $1$ cake? Of $1$ pasty?

Opportunity cost of 1C: #ans[$4$ pasties]

Opportunity cost of 1P: #ans[$1/4$ cake]

#sol[
  A full day is $20P$ or $5C$, so $5C = 20P$ and $1C = 4P$: one cake costs four pasties. Flip it for the other direction: $1P = 1/4 C$. The two opportunity costs are always reciprocals. The $4$ is also the absolute slope of the PPF: pasties given up per extra cake.
]

== Q2 | Feasibility

Suppose Colin bakes $10$ pasties and $2$ cakes in one day. Is this inefficient, efficient, or unattainable? Use a graph or algebra to justify your answer.

Inefficient, Efficient, Unattainable: #ans[Inefficient]

#sol[
  *Graph:* at $C = 2$ the frontier allows $P = 20 - 4(2) = 12$, and $(2, 10)$ sits below it, so inefficient: Colin could bake two more pasties without giving up a cake.

  *Algebra (time check):* $2$ cakes take $2/5$ of the day and $10$ pasties take $10/20 = 1/2$ of the day, so the bundle uses $2/5 + 1/2 = 9/10$ of a day. Under a full day is inefficient, exactly one day efficient, over one day unattainable. Either justification earns full credit.
]

== Q3 | Next Best Alternative

In his free afternoon Colin would rather bake for the Gryffindor party than photograph the Quidditch match, and both of which he'd prefer over taking a nap. What is Colin's opportunity cost of baking?

Opportunity cost of baking before the invitation: #ans[Photographing the Quidditch match]

Then Dennis invites him to Hogsmeade, which Colin likes more than photographing the match but less than baking. What is his opportunity cost of baking now?

Opportunity cost of baking after the invitation: #ans[The trip to Hogsmeade]

#sol[
  Opportunity cost is the single next-best alternative, not the sum of everything forgone. Before the invitation the ranking is baking $>$ photographing $>$ napping, so the cost of baking is the photography he gives up; the nap is not part of it, since he would not have napped anyway. Hogsmeade slots in between: baking $>$ Hogsmeade $>$ photographing $>$ napping. Baking is still his best option, but it now costs more: the best thing he gives up is the Hogsmeade trip. The common mistake is "the match and Hogsmeade"; only one alternative can be next best.
]
