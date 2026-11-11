---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode E0 | Overview

*The nuances of the decisions of sellers behind the supply curve show us that market power breaks the efficiency of markets.*

<!--
Consolidated 2026-11-11. The beat tables below are the animation revision sheet (E0_Storyboard_Revision.md) folded into these notes, its text unchanged (a vertical bar inside a table cell is written ∣). The rows 2.c to 5.b are carried from the November 2 comments; they describe the optional debrief. The November 2 comments (the earlier beats, choices left for Taylor) are in _archive/2026-11-11_consolidation/E0_Notes_before_consolidation.md, and the revision sheet is beside it.
Animation: E0_Animation.py, scene EpisodeE0. Playback order: 0 the Checkpoint D report and hold screen, then the bumper; 1 the recap of Parts A to D and what comes next; 2 the simulation’s goods and instructions (22 holds). The default episode ends at 2.b.
Visual conventions. Retain the 2:1 graphite stage, 15 fps, serif model labels, azure topic title, and fixed gold teaching line. Restore D1′s red taxonomy headers, grey internal rules, white two-line goods names, and accumulating colored Part labels. Use D1′s original label size and tight leading, with a clear gap to the left of the table. Begin with the whole taxonomy composition large and centered. Scale the composition as one unit when making room for the PPF and market. The compact selection box fits the widest goods label with 0.15 units of padding at the opening scale, staying within the cell rules when centered on a good. The same box is yellow for A, green for B, teal for C, and red for D. It fades with the taxonomy when E begins. During A, shrink and move the taxonomy into a balanced left panel before revealing the PPF on the right. Measure panels including their labels, and leave a 1.2-unit gutter with a tall muted divider down its center. The PPF occupies the future market’s plotting area; change models in place when B arrives. For D, ease the camera out and reposition both existing panels into a centered game–taxonomy–market composition before revealing the game and matching left divider. Both dividers extend above and below the models, with space on each side. Reserve enough space for both games’ strategy labels so the public-goods swap leaves all panels stationary. Hold the topic title and bottom teaching text at their original screen size. The market geometry recedes, while the outcome markers remain legible. For E and F, clear the taxonomy and dividers and center the market together with its right-hand Sellers and Buyers labels. Align those labels with MC and MB, joined by light dashed connectors with clear end margins. For B and C, use grey $\hat Q$ for equilibrium and yellow $Q^*$ for the efficient outcome. For D, switch both models and the shared legend to red for equilibrium / NE and green for efficiency. Align the market quantity labels by their baselines. The game uses equal-sized colored boxes without quantity labels; the legend below the taxonomy supplies the meaning. Row-player payoffs are pink, column-player payoffs teal. Each game cell lists the row payoff first. The games illustrate quantities qualitatively; payoff numbers are not quantities. Return to the earlier market palette when leaving D. The market retains the draft’s equations: MB = 12 - Q/5; MC = 2 + Q/20. An external cost of 2 gives equilibrium quantity 40 and efficient quantity 32; an external benefit of 2 gives efficient quantity 48. Trackers move the social curve, efficient quantity, guides, and DWL together. Clear one externality through the competitive benchmark before introducing the other.
The four-quadrant PPF is a separate stub: E0_Four_Quadrant.py, scene FourQuadrantPPF, from the same ROUNDS.
-->

## Introduction

<!--
0 · Checkpoint report and bumper, and 1 · Introduction. Beats, current build.
|   |   |
| --- | --- |
| 0.checkpoint.a | Before the bumper, title the stage “Checkpoint D”, with the grey subtitle “Strategic Interaction ∣ Example report”. Match `course.html` and `practice-demo.js`: a quiet shaded legend band, muted table rules, white skill names, blue filled practice circles, amber missed-practice circles, blue outlined skill squares for unlocked attempts, and grey squares with a white X for locked attempts. Unlocked does not mean passed; no passed squares appear in this access example. The legend distinguishes Practice from Skills. Practice lists E Exercise, V Vignette, H Homework, then Done (blue filled circle), Not done (grey open circle), and Closed until checkpoint (amber circle). Skills shows the same Unlocked and Locked squares used in the rows. Use separate columns for Skill, E / V / H, Checkpoint D (2 of 3), Makeups, and Reattempt (3 of 3). Show two actual skill names with illustrative practice records: D1.1 Best Responses has all three practices completed and both attempts unlocked; D2.1 Common Resources has E and V completed, H missed, the checkpoint unlocked, and the reattempt locked. Its grey H makeup circle is still empty. Bottom: “Two practices unlock a first attempt; three unlock a reattempt.” Hold. |
| 0.checkpoint.b | Add D3.1 Public Goods as a third row, with only E completed and amber V and H circles. Both attempt squares are grey with an X and labeled “Locked”. Show two empty makeup circles labeled V and H. Keep both earlier rows and the legend stationary. Bottom: “One completed practice: this skill is locked on both.” Hold. |
| 0.checkpoint.c | Keep the table and legend in place. Restore the compact horizontal makeup timeline below the table: an amber circle labeled “Complete missed practice”, a vertical check-in tick labeled “Office-hours check-in”, and a grey open endpoint labeled “Practice recorded”. Above it, place “After the checkpoint” at the left and “With Taylor or a TA” over the check-in. Trace the thin muted path to the check-in, then onward to the endpoint. Fill the endpoint and the third row’s V makeup circle blue together. The original practice and Checkpoint D columns remain historical; only makeup credit changes. With two total practice types completed, the reattempt remains locked. Bottom: “One makeup recorded. One practice still needed for the reattempt.” Hold. |
| 0.checkpoint.d | Keep the makeup timeline visible. Fill the third row’s H makeup circle blue, then remove the X from its Reattempt square, turn the outline blue, and change “Locked” to “Unlocked”. Leave the Checkpoint D record unchanged. Bottom: “All three practices are complete: the reattempt is unlocked.” Hold, then fade the complete report and timeline to the checkpoint hold screen. |
| 0.checkpoint.e | Center “CHECKPOINT D” in the bumper’s raster font, with its random blue pixel shading on CHECKPOINT and random yellow shading on D. Add “Strategic Interaction” in grey below, centering the complete composition. Keep this shaded screen still, with no movement or automatic advance. On advance, clear the card and begin the existing MICROECONOMICS bumper. |
| 0.a | Retain the shared raster bumper. Title: “Part E ∣ Sellers”, with Part E in azure and the rest in grey. Subtitle: “Market Power”, in grey italics. Hold, then fade to the recap. |
| 1.a | Title: “The Semester So Far”. Show the taxonomy and the yellow Part A label. Fade in the compact yellow box on Private Goods. Bottom: “Specializing and trading could bend out the PPF.” |
| 1.a.1 | Scale and move the full taxonomy composition into the left panel over two seconds, using the existing market layout. Reveal the tall divider and a PPF on the right, with axes running from 0 to 100, A vertically and B horizontally. Reuse the linear PPF from the opening of `Part_B/B0_Markets/03_Code.py`: A = 100 − B. Start with a static pink frontier over the grey straight line and hold before bending it. |
| 1.a.2 | Reuse B0’s continuous bend: $A = (100^\alpha - B^\alpha)^{1/\alpha}$, with $\alpha$ moving from 1 to 1.5 over one second. Leave the original straight line grey, and retain B0’s short gold arrow from (45, 56) to (57, 67) inside the opening gap. Swap the static frontier for its live version before the bend, then stop its updater afterward. Keep the Part A selection and teaching line. Hold. |
| 1.a.3 | Add the green Part B label below A and recolor the same selection box green, leaving the two-panel layout stationary. Remove the bottom teaching line. Beneath the taxonomy, key in B0’s first white question, “- Which point on the PPF?”. Reuse its white points at B = 30 and B = 80 on the bowed frontier, labeled “Option 1” and “Option 2” in gold. Reveal the first option with the question, then the second. Hold. |
| 1.a.4 | Keep both models still. Key in “- Coordinate large groups?” as the second line below the taxonomy. Hold. |
| 1.a.5 | Key in “- Who benefits?” as the third line. Keep B0’s order and letter-by-letter reveal, and hold before replacing the PPF with the market. |
| 1.b | Keep the green Part B label, taxonomy, divider, and questions stationary. Fade the PPF, its short gold arrow, and the two options. In the same plotting area, reveal the market axes and labels, then demand MB and supply MC, then the efficient marker at (40, 4). Bottom: “Markets facilitate specialization and trade.” |
| 1.c | Keep the layout and fade the three opening questions. Show the grey equilibrium and yellow efficient symbols in the equality $\hat Q = Q^*$ below the market. Bottom: “With competition and no externalities, equilibrium is efficient.” |
| 1.d | Add teal Part C. Move the same compact taxonomy box halfway toward Common Resources, keeping its size unchanged between the two rows. Remove the equality and add the grey equilibrium marker at (40, 4). Lift MSC continuously from MC to MC + 2; move the yellow efficient marker to (32, 5.6), with its guide and DWL updating throughout. Place “DWL” just above the grey welfare triangle, clear of the curves and without a pointer line. Bottom: “Negative externalities: the market delivers too much.” |
| 1.e | Return the external cost to zero and remove MSC and its welfare annotation. Then lift MSB from MB to MB + 2; move the efficient marker to (48, 4.4), with the new DWL growing on the right of equilibrium. Place “DWL” just above this triangle, clear of the curves and without a pointer line. Bottom: “Positive externalities: the market delivers too little.” |
| 1.f | First remove the positive externality, returning the market to its competitive benchmark. Fade the A/B/C labels, move the red taxonomy box to Common Resources, and widen the camera while repositioning the taxonomy and market into three balanced panels. Keep the title and teaching strip fixed. Fade the market curves and axes to 45%, preserving the quantity markers. Finish the layout move before introducing the game. Place “Part D ∣ Strategic Interaction” directly above the taxonomy, centered within its panel. Reveal a plain 2 by 2 game and the matching left divider: Fish less / Fish more for both players, payoffs (3,3), (0,5), (5,0), (1,1). Use equal-sized red and green boxes on (Fish more, Fish more) and (Fish less, Fish less), with no quantity labels on the matrix. Omit the redundant “Common resources” heading above the game. The shared legend below the taxonomy shows red $\hat Q$ with “Equilibrium” and green $Q^*$ with “Efficient”. The market has no externality and shows only its red equilibrium quantity; omit the equality beneath it. Bottom: “Common resources: individual incentives lead to over-extraction.” Pause before changing the market. |
| 1.f.1 | Keep the game and taxonomy still. Introduce the external cost to connect over-extraction with the negative-externality picture. The green efficient marker emerges as its quantity separates from the red equilibrium. Bottom: “Common resources: over-extraction, like negative externalities.” Hold. |
| 1.g | First remove the external cost while the commons game remains on screen. Then keep the camera and market steady as the taxonomy box moves to Public Goods. Replace the strategy labels with Contribute / Free ride; omit a game heading because Public Goods is already selected in the taxonomy. Keep the payoffs and colored boxes in the same cells. The market has no externality and shows only its red equilibrium quantity, with no equality beneath it. Bottom: “Public goods: individual incentives lead to under-provision.” Pause before changing the market. |
| 1.g.1 | Keep the game and taxonomy still. Introduce the external benefit; the green efficient marker emerges as its quantity separates from the red equilibrium. Bottom: “Public goods: under-provision, like positive externalities.” Hold. |
| 1.h | First return the external benefit to zero while the public-goods game remains visible. Then fade the game, taxonomy, selection box, both dividers, and the key, and remove the red market marker. Restore the market opacity and earlier yellow efficient marker, and ease the camera back while centering the complete graph-and-label composition in the body area, including space reserved for Buyers. Title: “What Comes Next”. Align “Part E ∣ Sellers” horizontally with MC, with Part E in azure, the separator grey, and Sellers orange. Link MC to the label with a thin muted dashed line, leaving 0.3 units clear at each end. Bottom: “How do sellers choose? Start with what they can make.” Hold before adding buyers. |
| 1.i | Keep the centered composition stationary. Add “Part F ∣ Buyers” aligned horizontally with MB, with the same left edge as Sellers. Part F is azure, the separator grey, and Buyers teal. Add the matching thin dashed connector from MB, with the same clear end margins. Remove the teaching line. Hold, then fade the recap. |
-->

In Part A we showed the core idea of economics, that specializing and trading could bend out the PPF, which is the technical way of saying that we can have more without needing more inputs of labor or resources and without needing better technology. Simply making better choices makes it possible to have more.

Then in Part B we showed that markets could facilitate the exchanges needed for specialization and trade. We also showed that this idea of social efficiency was maximized by markets, that anything more than what the market exchanged would be more costly than beneficial and anything less than what the market exchanged would be more beneficial than costly. So we actually want exactly what the market does.

But that was only in competitive markets, markets with many buyers and sellers, no externalities, and good information about the homogeneous good being exchanged.

In Part C we showed that externalities lead to misalignment between what the market delivers and what society would want. With negative externalities we want less than what the market delivers. With positive externalities we want more.

In Part D we just extended this idea of externalities a little further into markets with strategic interaction, where players’ actions depend on what others are doing. We showed that the non-excludability of common resources and public goods in this light leads to the problems of over-extraction of common resources, much like with negative externalities, and the under-provision of public goods, much like with positive externalities.

Next we’re turning to another way markets can succeed or fail, the market power of sellers. To do this, we need a more complete understanding of how sellers choose. How sellers choose starts with what they can make: how inputs like labor turn into output. I’ll warn you, the next class is about the least interesting class of the semester for me. But that should tell you something, that if we’re covering something as uninteresting as ‘Costs’, there’s an even better reason why we’re doing it. 

Today we’re going to run a simulation to collect data to build a more sophisticated model of the PPF, which will approach the bowed out nature of the PPF from another direction.

## Simulation

<!--
2 · The simulation. Beats, current build.
|   |   |
| --- | --- |
| 2.a | Title: “Simulation E”. Subtitle: “Production of Widgets and Airplanes”. Reveal the two existing definitions at 75% body scale, with Widget green and Airplane teal. Keep the definitions in their final positions so they do not shrink and jump when the rules arrive. |
| 2.b | Add a thin muted horizontal divider between the two goods’ definitions and the rules, spanning the text block with equal vertical margins. Reveal the three rules at the same 75% body scale, in order: a practice round; all eight workers make widgets for 20 seconds; two more workers switch to airplanes each round. Worker counts come from ROUNDS, with allocations of 8/0, 6/2, 4/4, 2/6, and 0/8; the duration comes from ROUND_SECONDS. Hold and end the default episode here while the author revises the instructions. |

Optional existing debrief, 2.c through 5.b. Preserve the draft’s table, round counts, production functions, technology shift, labor line, and PPF behind `SHOW_DEBRIEF = False` at the top of `construct()`. Setting it to True restores these existing beats and their IDs. Example data remain explicitly labeled. The separate four-quadrant stub is unchanged.
|   |   |
| --- | --- |
| 2.c | Grey subtitle DATA_NOTE. The table: Round, Widget workers, Airplane workers, Widgets, Airplanes; worker counts filled, output cells empty. Bottom: “Set up a table to store the data.” |
| 2.d.1, 2.d.2, … | One hold per round: that round's widgets and airplanes fill in. |
| 3.a | Title: Production Function. Widgets up, widget workers across; one red dot per round. Bottom: “The production function takes inputs and gives us some output quantity.” (E1's line, 2.b). |
| 3.b | The dots join; each worker's added widgets (+9, +6, +4, +3) above its dot. Bottom: “Diminishing marginal return: more inputs lead to increasingly small increases.” (E1's line, 2.f). |
| 3.c | The airplane production function on the right, built the same way. Bottom: “Airplanes have a production function of their own.” |
| 3.d | The widget production function stretches up by 1.4, the old one left in grey. Bottom: “What happens when technology changes?” |
| 4.a | Title: Labor. Widget workers up, airplane workers across; one dot per round, then the line and L_W + L_A = 4. Bottom: “We are fundamentally constrained by the total labor.” |
| 5.a | Title: Production Possibilities Frontier. The labor graph stays on the left; on the right, airplanes across and widgets up, one dot per round, then the PPF. Bottom: “And we have the PPF!” |
| 5.b | A grey dashed straight line between the PPF's two ends. Bottom: “The PPF bows out, from another direction.” |

Not built here: the Four Quadrant PPF (his last paragraph) is the stub E0_Four_Quadrant.py.
-->

We’re going to make two goods in class today, Widgets (W) and Airplanes (A). We’ll talk about the technical specifications for the two goods. To make these two goods I need 8 volunteers. You job will be turning these pieces of paper into the two goods. 

- A Widget is made by stapling a piece of paper in half.
- An Airplane is a piece of paper that can be flown at least five feet.

As you’re thinking about whether to volunteer, let me tell you a bit about the data we’re about to collect. We’re going to measure how many of each of these two goods we make with different levels of Labor (L) input into the production lines for Widgets (W) and Airplanes (A). 

The table for this data will be a column for Labor for Widgets, then Quantity of Widgets, then the same for Airplanes. 

 

| $L_W$ | $Q_W$ | $L_A$ | $Q_A$ |
| --- | --- | --- | --- |
| 8 |   | 0 |   |
| 6 |   | 2 |   |
| 4 |   | 4 |   |
| 2 |   | 6 |   |
| 0 |   | 8 |   |

We’ll start with a trial period where each gets a chance to learn how to make both W and A. Then start with all four making W and none making A for 20 seconds. Then two by two we’ll switch to making A.

When everyone is done:

Plot both Production Functions. Talk about diminishing marginal returns. Talk about what happens when technology changes.

 

Plot the Labor curve, the relationship between inputs. Talk about being fundamentally constrained by the total labor.

Plot the PPF, the relationship between outputs.[^1] Talk about the how the constraint on labor inputs gives us the frontier, and how the technology bends it out. And sometimes students will switch groups because they’re good at airplanes, so that’s specialization at work.

Next class we’ll open with these numbers.

Materials: a stack of scrap paper, one stapler for the whole widget line, a five-foot line taped on the floor, and a timer. The single stapler is the fixed input. As more workers share it, each extra worker adds fewer widgets, which should make the flattening easier to see. It is also the capital that comes back in E1.

[^1]: This is where I’ve talked about the four quadrant PPF in the past. It gives a picture of the relationship between four different variables. 
