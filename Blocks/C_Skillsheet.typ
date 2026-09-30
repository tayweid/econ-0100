// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show heading.where(level: 4): set text(size: 14.375pt)
#show heading.where(level: 4): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 4): set par(leading: 8.153pt)
#show heading.where(level: 5): set text(size: 14.375pt)
#show heading.where(level: 5): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 5): set par(leading: 8.153pt)
#show heading.where(level: 6): set text(size: 14.375pt)
#show heading.where(level: 6): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 6): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)

== Skillsheet C | ECON 0100 | Fall 2026

_Market Failures_

=== How to use this sheet

This sheet lists every assessed skill in Part C. Your grade is the percentage of skills you pass across the semester, so this sheet is the container for your studying: it tells you what each skill is, where we build it, what practice unlocks it, and the standard you must meet to pass it on Checkpoint C.

Each skill has three types of practice: the *Exercise* (done together in class), the *Vignette* (done together in recitation), and the *Homework* (done on your own time, due Sundays). Practice is graded for completion, not correctness. But you~will get feedback on which Homework questions you got right and wrong.~

- Complete *2 of 3* practices for a skill to unlock the skill on Checkpoint C.
- Complete *3 of 3* practices for a skill to unlock the Reattempt.

Skills you pass stay passed. If you no-pass a skill on Checkpoint C, complete all three practices and take the Reattempt.~

=== The skills at a glance

#align(center, table(
  columns: (auto, 1fr, auto),
  inset: 9pt,
  align: (center + horizon, left + horizon, center + horizon),
  table.header(table.cell(fill: luma(220))[*Code*], table.cell(fill: luma(220))[*Skill*], table.cell(fill: luma(220))[*Practice*]),
  [C1.1], [International Trade], [Exercise C1 · Vignette C1 · HW C1],
  [C1.2], [Tariffs], [Exercise C1 · Vignette C1 · HW C1],
  [C2.1], [Taxes & Incidence], [Exercise C2 · Vignette C2 · HW C2],
  [C2.2], [Subsidies], [Exercise C2 · Vignette C2 · HW C2],
  [C3.1], [Negative Externalities], [Exercise C3 · Vignette C3 · HW C3],
  [C3.2], [Positive Externalities], [Exercise C3 · Vignette C3 · HW C3],
  [C4.1], [Corrective Taxes & Subsidies], [Exercise C4 · Vignette C4 · HW C4],
))

=== C1.1 | International Trade

Opening a market to trade can increase domestic total surplus while making some domestic participants worse off.

*Standard.* You pass this skill if you can:

- Find the domestic equilibrium without trade, compare its price with a given world price, and determine whether the country imports / exports.
- For a small country taking the world price as given, find domestic quantity demanded and quantity supplied at that price, then calculate imports.
- Shade and calculate domestic consumer and producer surplus before and after opening to trade.
- Calculate the change in domestic total surplus and identify the domestic winners and losers in both importing and exporting cases.
- Trace how a change in the world price changes domestic production, consumption, trade volume, and surplus.

=== C1.2 | Tariffs

A tariff is just a tax on imports.

*Standard.* You pass this skill if you can:

- {++Find the domestic price under an import tariff as the world price plus the tariff, and find domestic quantity demanded, quantity supplied, and imports at that price.++}
- {++Shade and calculate consumer surplus, producer surplus, tariff revenue, and deadweight loss under the tariff, and compare them with free trade.++}
- {++Identify who gains and who loses from a tariff, and find a tariff that meets a stated goal, such as raising a given amount of revenue or protecting domestic sellers.++}
- {++Do the same for an export subsidy, which raises the domestic price above the world price.++}

=== C2.1 | Taxes & Incidence

Taxes create deadweight loss by driving a wedge between what buyers pay and sellers receive, reducing total surplus.

*Standard.* You pass this skill if you can:

- {++Show that a tax on buyers and the same tax on sellers lead to the same outcome, and find the quantity exchanged, the buyers’ price, and the sellers’ price using the tax wedge: the buyers’ price minus the sellers’ price equals the tax.++}
- {++Shade and calculate consumer surplus, producer surplus, government revenue, and deadweight loss under a tax, and how each changed from equilibrium.++}
- {++Find the incidence of a tax on buyers and on sellers, and determine which side bears more of it when demand or supply is relatively more elastic.++}

=== C2.2 | Subsidies

{++A subsidy is a tax run in reverse: the government pays the difference between what sellers receive and what buyers pay.++}

*Standard.* You pass this skill if you can:

- {++Find the quantity exchanged, the buyers’ price, and the sellers’ price under a per-unit subsidy, using the wedge: the sellers’ price minus the buyers’ price equals the subsidy.++}
- {++Shade and calculate consumer surplus, producer surplus, government spending, and deadweight loss under a subsidy, and show that the added trades cost more than they are worth.++}
- {++Determine how the gain from a subsidy splits between buyers and sellers.++}
- {++Analyze a price support in which the government buys the excess at the supported price, including the cost to the government.++}

=== C3.1 | Negative Externalities

When private costs don’t equal social costs, markets produce too much or too little, creating inefficiency.

*Standard.* You pass this skill if you can:

- {++Identify a negative externality, and add the external cost to the marginal private cost to get the marginal social cost.++}
- {++Find the market equilibrium from the marginal private benefit and cost curves, and the socially efficient quantity from the marginal social benefit and cost curves, and show that the market produces too much.++}
- {++Shade and calculate the deadweight loss from overproduction: the area where marginal social cost exceeds marginal social benefit between the efficient and the market quantity.++}
- {++For a single exchange, find its deadweight loss from its marginal benefit, marginal cost, and external cost.++}

=== C3.2 | Positive Externalities

If I get vaccinated or plant trees in my front yard I’m positively influencing the well-being of bystanders again without being compensated.

*Standard.* You pass this skill if you can:

- {++Identify a positive externality, and add the external benefit to the marginal private benefit to get the marginal social benefit.++}
- {++Find the market equilibrium and the socially efficient quantity, and show that the market produces too little.++}
- {++Shade and calculate the deadweight loss from underproduction: the area where marginal social benefit exceeds marginal social cost between the market and the efficient quantity.++}
- {++For a single exchange that doesn’t happen, find its deadweight loss from its marginal benefit, marginal cost, and external benefit.++}

=== C4.1 | Corrective Taxes & Subsidies

We can offset the problems of externalities with the problems of taxes.

*Standard.* You pass this skill if you can:

- {++Propose the type (tax or subsidy) and size of a corrective policy that moves the market to the socially efficient quantity: a per-unit tax equal to the external cost, or a subsidy equal to the external benefit.++}
- {++Find the buyers’ price, the sellers’ price, and the quantity after the policy, and show that the deadweight loss is gone.++}
- {++Calculate the government’s revenue from a corrective tax or its spending on a corrective subsidy.++}
- {++Show that setting the price at the buyers’ or the sellers’ value at the efficient quantity creates an excess or a shortage, while a tax or subsidy equal to the externality clears the market at that quantity.++}

// plass:comment
// | Editor. Draft for Skillsheet C, laid out like Skillsheet B. Taylor's words, unmarked: the intro (Skillsheet B's, with B changed to C); the subtitle (C_Outline.typ, "Part C | Market Failures"); C1.1, which is Skillsheet B's B6.1 standard moved here because trade folds into C1; and the one-line framings for C1.2 (C1 notes), C2.1 and C3.1 (C_Outline.typ episode summaries), C3.2 (C3 notes), and C4.1 (C4 notes). Everything in {++ ++} is mine: every other standard and the C2.2 framing.
// | Decisions for Taylor: (1) seven skills; trade and tariffs could merge into one C1.1 if C1 has to move fast. (2) C1.2's export-subsidy bullet comes from the International Pumpkin Pasties demos (Checkpoints/C/24F_Demo_X3); cut it if export subsidies aren't taught. (3) C2.2's price-support bullet comes from Government Cheese (Skillsheet B's B4.2 says "without government purchases," so purchases land here); cut it if it isn't taught. (4) C3.1 and C3.2 each end with the single-exchange "Deadweight Loss Intuition" from the 23F–24F MiniExam C; it could instead be one bullet in C4.1. (5) C4.1's last bullet is the C4 storyboard's opening ("If the price is set at buyers WTP, excess. If … sellers WTS, shortage.") in do-form.
// | What practice already covers each skill (from the Part C stubs): C1.1 and C1.2 have Vignette and Homework sources, and the Exercise and the Demo are gaps. C2.1 is covered by all three series. C2.2 is a gap in all three series. C3.1 is covered by all three, and C3.2 is a gap in all three (the positive-externality stories are on the checkpoint list). C4.1 is covered by all three.
// /plass:comment
