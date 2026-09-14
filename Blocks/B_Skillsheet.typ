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

== Skillsheet B | ECON 0100 | Fall 2026

_Coordination Using Competitive Markets_

=== How to use this sheet

This sheet lists every assessed skill in Part B. Your grade is the percentage of skills you pass across the semester, so this sheet is the container for your studying: it tells you what each skill is, where we build it, what practice unlocks it, and the standard you must meet to pass it on Checkpoint B.

Each skill has three types of practice: the *Exercise* (done together in class), the *Vignette* (done together in recitation), and the *Homework* (done on your own time, due Sundays). Practice is graded for completion, not correctness. But you~will get feedback on which Homework questions you got right and wrong.~

- Complete *2 of 3* practices for a skill to unlock the skill on Checkpoint B.
- Complete *3 of 3* practices for a skill to unlock the Reattempt.

Skills you pass stay passed. If you no-pass a skill on Checkpoint B, complete all three practices and take the Reattempt.~

=== The skills at a glance

#align(center, table(
  columns: (auto, 1fr, auto),
  align: (center + horizon, left + horizon, center + horizon),
  inset: 9pt,
  fill: (x, y) => if y == 0 { luma(220) },
  table.header([*Code*], [*Skill*], [*Practice*]),
  [B1.1], [Demand], [Exercise B1 · Vignette B1 · HW B1],
  [B1.2], [Consumer Surplus], [Exercise B1 · Vignette B1 · HW B1],
  [B2.1], [Supply], [Exercise B2 · Vignette B2 · HW B2],
  [B2.2], [Producer Surplus], [Exercise B2 · Vignette B2 · HW B2],
  [B3.1], [Equilibrium], [Exercise B3 · Vignette B3 · HW B3],
  [B4.1], [Efficiency & Total Surplus], [Exercise B4 · Vignette B4 · HW B4],
  [B4.2], [Price Controls], [Exercise B4 · Vignette B4 · HW B4],
  [B5.1], [Supply & Demand Shifters], [Exercise B5 · Vignette B5 · HW B5],
  [B5.2], [Price Elasticity], [Exercise B5 · Vignette B5 · HW B5],
  [B5.3], [Comparative Statics], [Exercise B5 · Vignette B5 · HW B5],
  [B6.1], [International Trade], [Exercise B6 · Vignette B6 · HW B6],
))

=== B1.1 | Demand

Demand organizes buyers’ willingness and ability to pay. Each point tells us the quantity demanded at a price, or their marginal benefit at a quantity.

*Standard.* You pass this skill if you can:

- Set up a linear demand curve from an equation, with price on the vertical axis and quantity on the horizontal axis, and correctly label intercepts and units.
- Find quantity demanded at a given price and marginal benefit at a given quantity, using a graph or an equation.
- Use an equation or the law of demand to determine how quantity demanded changes when the good’s own price changes.

=== B1.2 | Consumer Surplus

A buyer’s marginal benefit may be than the price. Consumer surplus measures the benefit the buyer keeps after paying for the goods they buy.

*Standard.* You pass this skill if you can:

- Find consumer surplus on one unit as marginal benefit minus the price.
- Graph and calculate consumer surplus under a linear demand curve, above the price, and up to the quantity bought.
- Calculate expenditure as price times quantity bought, and distinguish its rectangle from the consumer surplus region.
- Calculate how consumer surplus changes as prices change.

=== B2.1 | Supply

Supply organizes sellers’ willingness and ability to sell. The height of the supply curve measures the marginal cost of providing one more unit.

*Standard.* You pass this skill if you can:

- Set up a linear supply curve from an equation, with correctly labeled axes, intercepts, and units.
- Find quantity supplied at a given price and marginal cost at a given quantity, using a graph or an equation.
- Use an equation or the law of supply to determine how quantity supplied changes when the good’s own price changes.

=== B2.2 | Producer Surplus

A seller may receive more than the marginal cost of providing a unit. Producer surplus adds up these gains across the units sold.

*Standard.* You pass this skill if you can:

- Find producer surplus of one unit as the price received minus marginal cost.
- Graph and calculate producer surplus above a linear supply curve, below the price, and up to the quantity sold.
- Calculate revenue as price times quantity sold, and distinguish its rectangle from the producer surplus region.
- Calculate how producer surplus changes as prices change.

=== B3.1 | Equilibrium

Buyers and sellers respond to the incentives pushing prices up in shortage and down in excess. At equilibrium, quantity demanded equals quantity supplied.

*Standard.* You pass this skill if you can:

- Plot supply and demand together and solve for equilibrium price and quantity by setting quantity demanded equal to quantity supplied.
- Calculate quantity demanded and quantity supplied at a given price and identify whether it’s a shortage or an excess and measure its size.
- Find the quantity exchanged as the smaller of quantity demanded and quantity supplied in a closed market without government purchases.
- Determine the direction of price adjustment from a shortage or an excess, and identify the incentives of buyers and sellers that move the market toward equilibrium.

=== B4.1 | Efficiency & Total Surplus

In the competitive market model, with all costs and benefits captured by supply and demand, equilibrium maximizes the sum of producer surplus and consumer surplus.

*Standard.* You pass this skill if you can:

- Graph and calculate total surplus at equilibrium.
- Compare marginal benefit and marginal cost to identify it’s impact on total surplus, and locate the efficient quantity.
- For a specified quantity exchanged, with the highest-value buyers and lowest-cost sellers trading, calculate total surplus and deadweight loss relative to the efficient outcome.

=== B4.2 | Price Controls

A price ceiling limits how high the price can go; a price floor limits how low it can go. A binding control changes both the price of a trade and how many trades take place.

*Standard.* You pass this skill if you can:

- Classify a policy as a price ceiling or a price floor, draw the legal range of prices, and determine whether the control is binding relative to equilibrium.
- Find the price, quantity demanded, quantity supplied, quantity exchanged, and size of the shortage or excess under a price control without government purchases.
- Graph and calculate consumer surplus, producer surplus, total surplus, and deadweight loss under a price control assuming the highest-value buyers and lowest-cost sellers make the available trades.
- Compare the outcome with the uncontrolled equilibrium to identify who gains and who loses using welfare.

=== B5.1 | Supply & Demand Shifters

A change in the good’s own price moves along a curve. A change in preferences, production costs, or another condition of the market can move the entire curve.

*Standard.* You pass this skill if you can:

- Distinguish a movement along a supply or demand curve from a shift of the curve, and label a change in quantity demanded or supplied separately from a change in demand or supply.
- Given a change in tastes, income, the price of a substitute or complement, or the number of buyers, identify the direction of the demand shift; use whether the good is normal or inferior when income changes.
- Given a change in input costs, technology, the opportunity cost of production, or the number of sellers, identify the direction of the supply shift.
- Draw the shifted curve and show how the quantity demanded or supplied differs at the same price.

=== B5.2 | Price Elasticity

Elasticity is a normalized measure of how responsive quantities are to changes in prices. 

*Standard.* You pass this skill if you can:

- Calculate price elasticity of demand or supply between two price-quantity points.
- Classify a response as elastic, inelastic, or unit elastic by comparing the magnitude of elasticity with one; use the absolute value when classifying demand.
- Calculate elasticity over different portions of a straight-line demand curve and distinguish its changing elasticity from its constant slope.
- Compare elastic and inelastic responses, including the perfectly elastic and perfectly inelastic cases, using graphs and changes in quantity.

=== B5.3 | Comparative Statics

Comparative statics compares the equilibrium before a change to the equilibrium after the change.

*Standard.* You pass this skill if you can:

- For a single supply or demand shift, graph the old and new equilibria and determine the directions of change in equilibrium price and quantity.
- Solve for the old and new equilibria from linear supply and demand equations, and calculate the changes in price and quantity.
- When both curves shift, identify which change in price or quantity can be determined and which depends on the relative sizes of the shifts; resolve both when equations are supplied.
- _Compare how the same shift affects equilibrium price and quantity when the other curve is more or less price-responsive._

=== B6.1 | International Trade

Opening a market to trade can increase domestic total surplus while making some domestic participants worse off.

*Standard.* You pass this skill if you can:

- Find the domestic equilibrium without trade, compare its price with a given world price, and determine whether the country imports / exports.
- For a small country taking the world price as given, find domestic quantity demanded and quantity supplied at that price, then calculate imports.
- Shade and calculate domestic consumer and producer surplus before and after opening to trade.
- Calculate the change in domestic total surplus and identify the domestic winners and losers in both importing and exporting cases.
- Trace how a change in the world price changes domestic production, consumption, trade volume, and surplus.
