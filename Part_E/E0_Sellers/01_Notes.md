---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode E0 | Overview

*Introduction to how sellers make decisions and construct the supply curve.*

<!--
Animation storyboard for E0_Animation.py, scene EpisodeE0 (maniml E0_Animation.py EpisodeE0). Built 2026-11-02 from these notes and Taylor's animator brief (taxonomy and market through Parts A to D, then arrows to Part E and Part F). One comment per section lists its beats in playback order; every beat ends on a named self.pause.
Playback order: 0 bumper; 1 Introduction (the recap, 9 holds); 2 the simulation's goods, rules and data table; 3 production functions; 4 labor; 5 the PPF. 21 named pauses, plus one 2.d hold per round.
Recap market (C4's model): MB = 12 − Q/5, MC = 2 + Q/20, external cost or benefit 2. The market trades Q-hat = 40 at $4. MSC gives Q* = 32 at $5.60, MSB gives Q* = 48 at $4.40. Q-hat is red and Q* gold (C4's colors), on the graph and in the payoff matrix alike.
Simulation data: ROUNDS at the top of construct(), one row per round (widget workers, airplane workers, widgets, airplanes). The example rows are 4 workers, one moving per round: widgets 22, 19, 15, 9, 0 and airplanes 0, 5, 9, 12, 14. The table, both production functions, the labor line and the PPF are all drawn from ROUNDS. The rules screen's worker counts come from it too. DATA_NOTE is the grey subtitle, "Example numbers" until it is changed.
The four-quadrant PPF is a separate stub: E0_Four_Quadrant.py, scene FourQuadrantPPF, from the same ROUNDS.
Choices left for Taylor: (1) Each part's title is "Part X | Name" from _Parts.md; the E and F beat is titled What Comes Next. (2) The box colors copy D1 (yellow A, green B, blue C shifted half a cell down, red D); it turns yellow again for Part E. (3) The game is D1's Prisoner's Dilemma payoffs as a plain 2×2, not D1's diamond, with strategies Fish less / Fish more and then Contribute / Don't; no player names. (4) In Part D the taxonomy slides up and the game sits under it; the market fades to 35%. (5) Bottom lines written for this build from his recap: 1.a, 1.b, 1.f, 1.g, 1.h (shortened from his sentences), 3.c, 4.a (his, reworded), 5.b; 3.a and 3.b reuse E1's lines. (8) The data beats after the rules are the debrief with example numbers; the class's numbers replace them. (6) Widgets green and airplanes blue (Part F's good B and good A). (7) The better technology in 3.d multiplies widget output by 1.4.
-->

## Introduction

<!--
0 · Bumper and 1 · Introduction. Beats, as built.
0.a · The shared bumper, Part E | Episode 0, and the thesis in grey italic: “Introduction to how sellers make decisions and construct the supply curve”.
1.a · Title: Part A | The Landscape. D1's taxonomy (Rival / Non-Rival by Excludable / Non-Excludable), a yellow box around Private Goods. Bottom: “Specializing and trading could bend out the PPF.”
1.b · Title: Part B | Coordination Using Markets. The box turns green. The market fades in on the right (MB teal, MC orange), then Q* in gold at 40. Bottom: “Markets facilitate the exchanges needed for specialization and trade.”
1.c · Bottom only: “So we actually want exactly what the market does.”
1.d · Title: Part C | Externalities. The box turns blue and drops half a cell. MSC appears; Q-hat in red at 40; Q* slides to 32; the DWL triangle. Bottom: “With negative externalities we want less than what the market delivers.”
1.e · MSC and its DWL leave; MSB appears; Q* slides to 48; the DWL triangle on the other side. Bottom: “With positive externalities we want more.”
1.f · Title: Part D | Strategic Interaction. The taxonomy slides up; the box turns red on Common Resources; the market fades and shows the negative picture again. Under the taxonomy, the game (Fish less / Fish more), its Nash cell boxed red with Q-hat and the 3 | 3 cell boxed gold with Q*. Bottom: “Common resources: over-extraction, much like negative externalities.”
1.g · The box moves to Public Goods; the strategies become Contribute / Don't; the faded market shows the positive picture. Bottom: “Public goods: under-provision, much like positive externalities.”
1.h · Title: What Comes Next. The game, the externality and Q-hat leave; the taxonomy drops back with a yellow box on Private Goods; the plain market at full strength with Q* at 40; “Part E | Sellers” with an arrow to the supply curve. Bottom: “Another way markets can succeed or fail: the market power of sellers.”
1.i · “Part F | Buyers” with an arrow to the demand curve. No bottom line.
Not built: “But that was only in competitive markets…” has no beat of its own; the warning about costs being the least interesting class is spoken over 1.h.
-->

In Part A we showed the core idea of economics, that specializing and trading could bend out the PPF, which is the technical way of saying that we can have more without needing more inputs of labor or resources and without needing better technology. Simply making better choices makes it possible to have more.

Then in Part B we showed that markets could facilitate the exchanges needed for specialization and trade. We also showed that this idea of social efficiency was maximized by markets, that anything more than what the market exchanged would be more costly than beneficial and anything less than what the market exchanged would be more beneficial than costly. So we actually want exactly what the market does.

But that was only in competitive markets, markets with many buyers and sellers, no externalities, and good information about the homogeneous good being exchanged.

In Part C we showed that externalities lead to misalignment between what the market delivers and what society would want. With negative externalities we want less than what the market delivers. With positive externalities we want more.

In Part D we just extended this idea of externalities a little further into markets with strategic interaction, where players’ actions depend on what others are doing. We showed that the non-excludability of common resources and public goods in this light leads to the problems of over-extraction of common resources, much like with negative externalities, and the under-provision of public goods, much like with positive externalities.

Next we’re turning to another way markets can succeed or fail, the market power of sellers. To do this, we need a more complete understanding of how sellers choose. How sellers choose starts with what they can make: how inputs like labor turn into output. I’ll warn you, the next class is about the least interesting class for me. But that should tell you something, that if we’re covering something as uninteresting as ‘Costs’, there’s an even better reason why we’re doing it. 

Today we’re going to run a simulation to collect data to build a more sophisticated model of the PPF, which will approach the bowed out nature of the PPF from another direction.

## Simulation

<!--
2 · The simulation, 3 · Production functions, 4 · Labor, 5 · The PPF. Beats, as built. Every count comes from ROUNDS.
2.a · Title: Widgets And Airplanes. “A Widget is made by stapling a piece of paper in half.” then “An Airplane is a piece of paper that can be flown at least five feet.”, Widget green and Airplane blue.
2.b · The two lines move up; the rules, one row per fade: “1. A practice round: everyone learns to make both.” “2. Round 1: all four workers make widgets for 30 seconds.” “3. Each round after, one more worker switches to airplanes.” (four and one more come from ROUNDS).
2.c · Grey subtitle DATA_NOTE. The table: Round, Widget workers, Airplane workers, Widgets, Airplanes; worker counts filled, output cells empty. Bottom: “Set up a table to store the data.”
2.d.1, 2.d.2, … · One hold per round: that round's widgets and airplanes fill in.
3.a · Title: Production Function. Widgets up, widget workers across; one red dot per round. Bottom: “The production function takes inputs and gives us some output quantity.” (E1's line, 2.b).
3.b · The dots join; each worker's added widgets (+9, +6, +4, +3) above its dot. Bottom: “Diminishing marginal return: more inputs lead to increasingly small increases.” (E1's line, 2.f).
3.c · The airplane production function on the right, built the same way. Bottom: “Airplanes have a production function of their own.”
3.d · The widget production function stretches up by 1.4, the old one left in grey. Bottom: “What happens when technology changes?”
4.a · Title: Labor. Widget workers up, airplane workers across; one dot per round, then the line and L_W + L_A = 4. Bottom: “We are fundamentally constrained by the total labor.”
5.a · Title: Production Possibilities Frontier. The labor graph stays on the left; on the right, airplanes across and widgets up, one dot per round, then the PPF. Bottom: “And we have the PPF!”
5.b · A grey dashed straight line between the PPF's two ends. Bottom: “The PPF bows out, from another direction.”
Not built here: the Four Quadrant PPF (his last paragraph) is the stub E0_Four_Quadrant.py.
-->

Have four volunteers and two goods, Widgets (W) and Airplanes (A). A Widget is made by stapling a piece of paper in half. An Airplane is a piece of paper that can be flown at least five feet. Start with a trial period where each gets a chance to learn how to make both. Then start with all four making W and none making A for 30 seconds. Then one by one switch one to making A.

Set up a table to store the data.

When everyone is done plot both Production Functions. Talk about diminishing marginal returns. Talk about what happens when technology changes.

Then plot the Labor curve, the relationship between inputs. Talk about being fundamentally constrained by the total labor.

And we have the PPF!

You can see now that we have a relationship between four different variables. Working with all four at the same time is what we call the Four Quadrant PPF. Plot the data on the Four Quadrant PPF. Talk about the different shapes of the production functions.

{++Materials: a stack of scrap paper, one stapler for the whole widget line, a five-foot line taped on the floor, and a timer. The single stapler is the fixed input. As more workers share it, each extra worker adds fewer widgets, which should make the flattening easier to see. It is also the capital that comes back in E1.++}

{++Roles: the workers, one inspector for each good, and a recorder at the board. Only finished items count: a widget is stapled, and an airplane crosses the tape line. The inspectors' counts are the ones that go in the table, which keeps the counting out of the workers' hands.++}

{++Make the practice round long enough that airplane times settle, about a minute on each good, so the counted rounds measure the switch and not the learning.++}

{++After each round, type it into ROUNDS at the top of E0_Animation.py and save; the table and every graph redraw in the viewer. Change DATA_NOTE from “Example numbers” to the class's label. With 8 workers moved 2 at a time, the rows change and the rules screen follows.++}

{++Next class opens from these numbers.++}

## Post-Class Notes

This became sort of competitive and rowdy in the last class. It might have been just one student, but it kind of got in the way. Maybe I was just tired…. But if there’s a way to calm things down I think that’d be good.

Also it might be better to have more widget makers. There were two issues with data collection. The first is learning effects for airplanes. The second is we couldn’t quite see the flattening out with widgets. So it might be better to start with 8 instead of 4 workers and switch 2 at a time, starting with widgets…. Not sure.

### Part E | Production Simulation

this requires understanding what goes into the sellers incentives in a more nuanced way

this means understanding where costs come from

simulation

make the connection to Molly’s supply curve

it depends on what we call the production function

in the basic setup for the class, her production function for both goods was linear

but it isn’t always the case

marginal product of labor

### Class on March 23

start with production data from last time

show the marginal product of labor

talk about Cobb Douglas

do the thing on the board with the increase in labor and the increase in output

show how this relates to costs through wages and fixed costs

talk about TC and VC and FC

then do averages

then do marginal cost
