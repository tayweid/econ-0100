// Exported from Plass
#set page(paper: "us-letter", margin: 0.6in, numbering: "1", number-align: center)
#set par(justify: true, leading: 8.172pt, spacing: 17.172pt)
#set list(spacing: 10.672pt)
#set enum(spacing: 10.672pt)
#show heading.where(level: 1): set text(size: 19.000pt)
#show heading.where(level: 1): set block(above: 21.113pt, below: 20.084pt)
#show heading.where(level: 1): set par(leading: 10.777pt)
#show heading.where(level: 2): set text(size: 14.000pt)
#show heading.where(level: 2): set block(above: 35.720pt, below: 15.950pt)
#show heading.where(level: 2): set par(leading: 7.941pt)
#show heading.where(level: 3): set text(size: 11.500pt)
#show heading.where(level: 3): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 3): set par(leading: 6.523pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 8.000pt)
#show math.equation.where(block: true): set block(above: 17.192pt, below: 18.962pt)
#set text(size: 10pt, font: "New Computer Modern", hyphenate: true)
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Demo A

Demos are similar to Checkpoints, often taken directly from past semesters. Work through the problems and check your work against mine. Practice answering clearly and completely. Show your work so someone else can understand your thought process. You are encouraged to work in small groups. Find a study room, grab some classmates, and work together on a whiteboard.

_This Demo is updated from the Fall 2024 Demo A in the walkthrough video: the story and numbers are the same, each question opens with the parts the video covers, and the parts that follow are new since then._

== Q1 | Opportunity Cost (A1.1)

Colin Creevey can bake #mi(`20`) cornish pasties or #mi(`5`) cauldron cakes in one day.

a) What is Colin's opportunity cost of producing #mi(`1`) cake?~\_\_\_\_\_\_\_\_\_\_

b) What is Colin's opportunity cost of producing #mi(`1`) pasty?~\_\_\_\_\_\_\_\_\_\_

c) Colin would rather bake than clean the kitchen. A food photography job comes up that he likes more than cleaning but less than baking. 

~(i) What is his opportunity cost of baking? \_\_\_\_\_\_\_\_\_\_

~(ii) What is his opportunity cost of this new food photography job?

== Q2 | Colin's PPF (A1.2)

Colin Creevey can bake #mi(`20`) cornish pasties or #mi(`5`) cauldron cakes in one day. There are two graphs, one for (a) and one for (b). For both graphs, draw Colin's PPF, pasties on the vertical axis and cakes on the horizontal. Label the intercepts.

~

a) For each daily output, write whether it is unattainable, inefficient, or efficient, and mark it on the first graph.

#quote(block: true)[
  (i) #mi(`20`) pasties \_\_\_\_\_\_\_\_\_\_

  (ii) #mi(`20`) pasties and #mi(`1`) cake \_\_\_\_\_\_\_\_\_\_

  (iii) #mi(`10`) pasties and #mi(`2`) cakes \_\_\_\_\_\_\_\_\_\_

  #align(center, grid(columns: (200pt, 200pt), gutter: 36pt,
  box(width: 100%, height: 150pt, inset: 6pt, stroke: (left: 0.5pt + luma(150), bottom: 0.5pt + luma(150))),
  box(width: 100%, height: 150pt, inset: 6pt, stroke: (left: 0.5pt + luma(150), bottom: 0.5pt + luma(150))),
))

]

~

~

b) Colin currently makes #mi(`8`) pasties and #mi(`3`) cakes. On the second graph, draw his PPF and mark this output. Is that output unattainable, inefficient, or efficient:

#quote(block: true)[
  (i) if he cuts back the labor he devotes to baking? \_\_\_\_\_\_\_\_\_\_

  (ii) if instead he discovers a spell that triples his daily output of pasties? \_\_\_\_\_\_\_\_\_\_

]

== Q3 | Absolute and Comparative Advantage (A2.1)

Colin Creevey can bake #mi(`20`) cornish pasties or #mi(`5`) cauldron cakes in one day. Katie Bell can bake #mi(`15`) cornish pasties or #mi(`8`) cauldron cakes in one day. Set up a Production Table with both Colin and Katie's output per day.~Then set up an opportunity cost table with Colin and Katie's opportunity costs for each good. Who has the~absolute advantage (AA) and comparative advantage (CA) in each good?

AA in Pasties: \_\_\_\_\_\_\_\_\_\_ #h(1fr) AA in Cakes: \_\_\_\_\_\_\_\_\_\_ #h(1fr)

CA in Pasties: \_\_\_\_\_\_\_\_\_\_ #h(1fr) CA in Cakes: \_\_\_\_\_\_\_\_\_\_ #h(1fr)

#v(40pt)

== Q4 | An Improving Trade (A3.1)

Colin Creevey can bake #mi(`20`) cornish pasties or #mi(`5`) cauldron cakes in one day. Katie Bell can bake #mi(`15`) pasties or #mi(`8`) cakes in one day. Their opportunity costs are listed in the following opportunity cost table.

#align(center, table(
  columns: 3,
  [], [*Pasty*], [*Cake*],
  [*Colin*], [1/4 Cake], [4 Pasties],
  [*Katie*], [8/15 Cake], [15/8 Pasties],
))

a) What is the range of exchange rates that would make both Colin and Katie better off?

Between \_\_\_\_\_\_\_\_\_\_ and \_\_\_\_\_\_\_\_\_\_ Pasties for~#mi(`1`) Cake

b) It turns out Colin wants to add hours to his job. So he increases from #mi(`5`) to #mi(`8`) hours per day. What is Colin's new opportunity cost of one cake?~\_\_\_\_\_\_\_\_\_\_

c) Select all the exchange rates which could facilitate a trade between the two bakers.

#quote(block: true)[
  #grid(columns: (1fr, 1fr, 1fr, 1fr),
[$square$ 1 Cake for 1 Pasty], 
[$square$ 1 Cake for 2 Pasties],
[$square$ 1 Cake for 3 Pasties], 
[$square$ 1 Cake for 5 Pasties],
)

]
