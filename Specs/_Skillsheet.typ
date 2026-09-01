// Full-course Skillsheet — DRAFT for F26
// Part A follows the current course numbering (blocks A1 PPF / A2 Advantage / A3 Trade,
// with Opportunity Cost as A1.1 though it's introduced in A0). Parts B-F still follow
// pipeline/config/skills.yaml, which uses the older numbering — reconcile when those parts firm up.
// Standards for each skill live on the part skillsheets (e.g., Parts/A/A_Skillsheet.typ).
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)

#let skilltable(..rows) = align(center, text(size: 10pt, table(
  columns: (auto, 1fr, auto, auto, auto, auto, auto),
  align: (center + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  inset: 7pt,
  fill: (x, y) => if y == 0 { luma(220) },
  table.header([*Code*], [*Skill*], [*Exercise*], [*Vignette*], [*HW*], [*Checkpoint*], [*Reattempt*]),
  ..rows
)))

#let row(code, name) = ([#code], [#name], [], [], [], [], [])

== Skillsheet | ECON 0100 | Fall 2026

This sheet lists every assessed skill in the class — the list your grade is built from. Your Final Grade is the percentage of these skills you pass on Checkpoints and Reattempts. Skills you pass stay passed. Each Part has its own skillsheet with the posted standard for each skill; use this sheet to track your progress across the semester.

Each skill has three types of practice: the *Exercise* (done together in class), the *Vignette* (done together in recitation), and the *Homework* (done on your own time, due Sundays). Practice is graded for completion, not correctness:

- Complete *2 of 3* practices for a skill to unlock the skill on the Checkpoint.
- Complete *3 of 3* practices for a skill to unlock the Reattempt.

=== Part A | The Core Economic Idea #h(1fr) #text(size: 11pt)[Checkpoint A: Wed. Sept. 9]

#skilltable(
  ..row([A1.1], [Opportunity Cost]),
  ..row([A1.2], [The PPF]),
  ..row([A2.1], [Absolute & Comparative Advantage]),
  ..row([A3.1], [Specialization & Trade]),
)

=== Part B | Markets coordinate cooperation #h(1fr) #text(size: 11pt)[Checkpoint B: Wed. Sept. 30]

#skilltable(
  ..row([B1.1], [Demand]),
  ..row([B1.2], [Supply]),
  ..row([B2.1], [Equilibrium]),
  ..row([B2.2], [Market Welfare]),
  ..row([B3.1], [Comparative Statics]),
  ..row([B3.2], [Elasticity]),
  ..row([B4.1], [Price Controls]),
)

=== Part C | When markets fail #h(1fr) #text(size: 11pt)[Checkpoint C: Wed. Oct. 14]

#skilltable(
  ..row([C1.1], [Taxes & Incidence]),
  ..row([C1.2], [Subsidies]),
  ..row([C2.1], [International Trade & Tariffs]),
  ..row([C3.1], [Negative Externalities]),
  ..row([C3.2], [Positive Externalities]),
  ..row([C4.1], [Corrective Policy]),
)

=== Part D | Strategic interaction #h(1fr) #text(size: 11pt)[Checkpoint D: Wed. Oct. 28]

#skilltable(
  ..row([D1.1], [Best Response]),
  ..row([D1.2], [Nash Equilibrium]),
  ..row([D2.1], [Goods & the Commons]),
  ..row([D3.1], [Public Goods]),
  ..row([D3.2], [Voting]),
  ..row([D4.1], [Sequential Games]),
)

=== Part E | Sellers #h(1fr) #text(size: 11pt)[Checkpoint E: Mon. Nov. 30]

#skilltable(
  ..row([E1.1], [Costs of Production]),
  ..row([E2.1], [Competitive Firms]),
  ..row([E3.1], [Monopoly]),
  ..row([E4.1], [Duopoly]),
  ..row([E5.1], [Policy & Market Power]),
)

=== Part F | Buyers #h(1fr) #text(size: 11pt)[Checkpoint F: Final Exam Period]

#skilltable(
  ..row([F1.1], [Budget Constraints]),
  ..row([F1.2], [Preferences & Optimization]),
  ..row([F2.1], [Factor Markets]),
  ..row([F3.1], [Linked Markets]),
)

If you no-pass a skill on a Checkpoint, complete all three practices and take the Reattempt — it can only help you. Reattempt timing and logistics will be announced on Canvas.
