// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#import "@preview/mitex:0.2.5": mi, mitex

== Skillsheet A | ECON 0100 | Fall 2026

_The Core Economic Idea_

=== How to use this sheet

This sheet lists every assessed skill in Part A. Your grade is the percentage of skills you pass across the semester, so this sheet is the container for your studying: it tells you what each skill is, where we build it, what practice unlocks it, and the standard you must meet to pass it on Checkpoint A.

Each skill has three types of practice: the *Exercise* (done together in class), the *Vignette* (done together in recitation), and the *Homework* (done on your own time, due Sundays). Practice is graded for completion, not correctness. But you~will get feedback on which Homework questions you got right and wrong.~

- Complete *2 of 3* practices for a skill to unlock the skill on Checkpoint A.
- Complete *3 of 3* practices for a skill to unlock the Reattempt.

=== The skills at a glance

#align(center, table(
  columns: (auto, 1fr, auto),
  align: (center + horizon, left + horizon, center + horizon),
  inset: 9pt,
  fill: (x, y) => if y == 0 { luma(220) },
  table.header([*Code*], [*Skill*], [*Practice*]),
  [A1.1], [Opportunity Cost], [Exercise A1 · Vignette A1 · HW A1],
  [A1.2], [The PPF], [Exercise A1 · Vignette A1 · HW A1],
  [A2.1], [Absolute & Comparative Advantage], [Exercise A2 · Vignette A2 · HW A2],
  [A3.1], [Specialization & Trade], [Exercise A3 · Vignette A3 · HW A3],
))

=== A1.1 | Opportunity Cost

Preferences are rankings; scarcity means we can't have everything. Together they force choices, and every choice carries a tradeoff. Opportunity cost measures that tradeoff as the value of the next best use of your resources.

*Standard.* You pass this skill if you can:

- Define opportunity cost as the value of the next best alternative given up, and explain why choices carry costs even when no money changes hands.
- Identify the next best alternative in a list of ranked options, and update the opportunity cost of a choice when a new alternative is added.
- Compute the opportunity cost of one unit of a good from productivity numbers (e.g., a producer who can make #mi(`20 R`) or #mi(`30 F`) per day), in both directions, and recognize that the two rates are reciprocals.

=== A1.2 | The PPF

The Production Possibility Frontier organizes tradeoffs systematically: it draws the boundary of what's attainable with the resources and technology at hand.

*Standard.* You pass this skill if you can:

- Set up a PPF on an #mi(`x, y`) graph from a producer's productivity numbers, with correctly labeled axes, intercepts, and slope.
- Interpret the slope of the PPF as the opportunity cost of the good on the horizontal axis.
- Classify any point as inefficient (inside), efficient (on the frontier), or unattainable (outside), and justify the classification with a graph or algebra.
- Show how the PPF responds to a change: a shift from a change in resources (e.g., working fewer hours) and a pivot from a technology change affecting one good.

=== A2.1 | Absolute & Comparative Advantage

With two producers, we can compare who is better at producing (absolute advantage) and who gives up less to produce (comparative advantage). These can disagree, and it's comparative advantage that matters for how a group should divide its work.

*Standard.* You pass this skill if you can:

- Build a production table for two producers and identify who has the absolute advantage in each good.
- Build an opportunity cost table from the production table and identify who has the comparative advantage in each good.
- Explain the difference between absolute and comparative advantage, including how one producer can hold the absolute advantage in both goods while each producer holds exactly one comparative advantage.

=== A3.1 | Specialization & Trade

Specializing in a comparative advantage and trading can end up with more of both goods for both individuals, points outside their individual PPFs, without any new resources or technology.

*Standard.* You pass this skill if you can:

- Determine, from an opportunity cost table, who should specialize in which good for the pair to jointly produce more.
- Find terms of trade that make both parties better off, and explain why any exchange rate between the two producers' opportunity costs works.
- Show, with a graph or with numbers, that a proposed trade leaves both parties beyond their autarky production points and explain why a proposed trade would be rejected by one side.
- Describe how a change to one producer's capacity (e.g., doubling hours) changes the PPF but not the opportunity costs, and what that means for the range and volume of possible trades.

=== Tracking your progress

#align(center, text(size: 10pt, table(
  columns: (auto, 1fr, auto, auto, auto, auto, auto),
  inset: 7pt,
  align: (center + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  fill: (x, y) => if y == 0 { luma(220) },
  table.header([*Code*], [*Skill*], [*Exercise*], [*Vignette*], [*HW*], [*Checkpoint*], [*Reattempt*]),
  [A1.1], [Opportunity Cost], [], [], [], [], [],
  [A1.2], [The PPF], [], [], [], [], [],
  [A2.1], [Absolute & Comparative Advantage], [], [], [], [], [],
  [A3.1], [Specialization & Trade], [], [], [], [], [],
)))

Skills you pass stay passed. If you no-pass a skill on Checkpoint A, complete all three practices and take the Reattempt. It can only help.
