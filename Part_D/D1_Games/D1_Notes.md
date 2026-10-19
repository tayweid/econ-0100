---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

<!--
Animation: D1_Animation.py · EpisodeD1
First day of Part D: Strategic Interaction. Taxonomy, then Baby Game Theory.
Sources: ../D0_Strategic_Interaction/03_Code.py (taxonomy and A/B/C map)
and _archive/03_Code_2026-10-19.py (definitions, four games, closing question).
The old D0 fishing-simulation rules are outside this requested combined sequence;
the original D0 source remains available. All four game matrices and all ties
are preserved. The old D1 notes below are unreconciled author prose; no new
lecture script has been substituted for them.

Layout: Graphite 2:1, 15 fps; shared palette and serif Tex. Azure topic titles,
optional grey context, 0.7443-scale gold bottom lines centered 0.05 from bottom.
Taxonomy retains the original D0 layout and color-changing box choreography;
the four game matrices use a 45-degree clockwise diamond layout. Each square
cell is 1.5 units on a side; the board center is (0, -0.5). The original
upper-left / upper-right / lower-left / lower-right outcomes now occupy the
top / right / left / bottom of the diamond. All payoffs, strategy labels, and
player names stay horizontal. Strategy labels use CMU Sans at scale 0.7 in
CAPTION grey; player names retain serif type at scale 0.8 and their payoff
colors, separating players from choices. Player 1's choices sit outside the upper-left
edge, Player 2's outside the upper-right edge. Player names share y=2.0.
During the Prisoner's Dilemma payoff reveals, background shading represents
only Player 2's fixed choice as Player 1's rival: a single teal column at 12%
opacity behind the grid and numbers. Both players retain colored choice
underlines. Establish Player 2's choice and pause; then show Player 1's choice
and ask for the payoff, pause again, and reveal Player 1's number. Reveal
Player 2's payoff on the following click. Repeat for CC, DC, DD, and CD.
During best-response analysis in all four games, only the choice held fixed
is underlined and shaded; remove both cues for the equilibrium summary.
Yellow row/column isolation rectangles follow the diagonal grid and span the
two relevant outcome cells. Individual best-response boxes remain upright.
Nash and efficiency outlines are equal 1.35-unit squares rotated with the
cells; their color and dashed overlay convention are unchanged. Payoff pairs
use an upright grey pipe separator stretched to 130% height, with a 0.3-unit
gap on each side before scaling to 0.85. Each line
below names a click-through pause. New prose fades in only after old prose leaves.

0.a · Original D0 opening: raster MICROECONOMICS, five flicker rounds; “Part D | Strategic Interaction” below it. Move this group to the top with a 1-unit margin and retain it through the taxonomy. The Part D label uses current title azure and the remaining title caption grey.
1.a · Reveal the complete taxonomy Table in one fade, scale 0.7, directly below the retained opening and shifted 1 unit right. Preserve Rival / Non-Rival columns and Excludable / Non-Excludable rows, with red labels; Private Goods / Club Goods / Common Resources / Public Goods in white serif, grey rules. No separate taxonomy heading.
1.b · Part A appears at the original upper-left anchor shifted 3 units down, scale 1.6, yellow. A yellow box with 0.5-unit padding surrounds Private Goods.
1.c · The same box turns green without moving; green Part B appears one unit below Part A.
1.d · The same box shifts DOWN exactly 0.5 units and turns teal; teal Part C appears one unit below Part B. This original offset is intentional and is not a new cell selection.
1.e · Move the same box, without resizing, to Common Resources and turn it red. No added Part D label at left. After this pause, fade out the table, box, and A/B/C labels, then the retained opening, and continue directly to Baby Game Theory instead of the old fishing-simulation rules.
2.a · “Baby Game Theory”: Best Response definition fades in.
2.b · Dominant Strategy definition joins below.
2.c · Nash Equilibrium definition joins below; clear the definition card before the first matrix.
3.a1 · Prisoner's Dilemma: reveal the diamond grid, then Player 1's two choices. Gold caption: “Player 1 chooses Cooperate or Defect.”
3.a2 · Reveal Player 2's two choices. Gold caption: “Player 2 also chooses Cooperate or Defect.”
3.a2r · Player 2 chooses Cooperate. Underline Cooperate in teal and shade only Player 2’s corresponding column. Pause before Player 1 chooses; no payoffs yet.
3.a3q · Player 1 chooses Cooperate. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a3 · Both cooperate: Player 1 receives 3. Reveal only Player 1’s payoff at cell (0, 0) and its grey pipe. Keep earlier numbers visible.
3.a4 · Both cooperate: Player 2 receives 3. Reveal only Player 2’s payoff at cell (0, 0). Keep earlier numbers visible.
3.a5q · Player 1 chooses Defect. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a5 · Only Player 1 defects: Player 1 receives 5. Reveal only Player 1’s payoff at cell (1, 0) and its grey pipe. Keep earlier numbers visible.
3.a6 · Only Player 1 defects: Player 2 receives 0. Reveal only Player 2’s payoff at cell (1, 0). Keep earlier numbers visible.
3.a6r · Player 2 now chooses Defect. Move the teal underline and the single shaded column to Defect; remove Player 1’s underline and pause.
3.a7q · Player 1 chooses Defect. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a7 · Both defect: Player 1 receives 1. Reveal only Player 1’s payoff at cell (1, 1) and its grey pipe. Keep earlier numbers visible.
3.a8 · Both defect: Player 2 receives 1. Reveal only Player 2’s payoff at cell (1, 1). Keep earlier numbers visible.
3.a9q · Player 1 chooses Cooperate. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a9 · Only Player 2 defects: Player 1 receives 0. Reveal only Player 1’s payoff at cell (0, 1) and its grey pipe. Keep earlier numbers visible.
3.a · Only Player 2 defects: Player 2 receives 5. Reveal only Player 2’s payoff at cell (0, 1). Keep earlier numbers visible.
3.b · Yellow outline isolates Player 2 choosing Cooperate; “If Player 2 chooses Cooperate, what is your best response?”
3.c · Add pink boxes to best-response payoffs at zero-based cells [(1, 0)]. Keep earlier response boxes visible; ties receive two boxes.
3.d · Yellow outline isolates Player 2 choosing Defect; “If Player 2 chooses Defect, what is your best response?”
3.e · Add pink boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.f · Yellow outline isolates Player 1 choosing Cooperate; “If Player 1 chooses Cooperate, what is your best response?”
3.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.h · Yellow outline isolates Player 1 choosing Defect; “If Player 1 chooses Defect, what is your best response?”
3.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.j · Remove isolation outline; red equal-size boxes mark pure Nash cells [(1, 1)]. “Both players have a dominant strategy: Defect.”
3.k · Green box, same dimensions as Nash boxes, marks [(0, 0)]. “Both players prefer (3, 3) to (1, 1).”
4.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(2, 1), (0, 0)], [(0, 0), (1, 2)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
4.b · Yellow outline isolates Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
4.c · Add pink boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
4.d · Yellow outline isolates Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
4.e · Add pink boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
4.f · Yellow outline isolates Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
4.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
4.h · Yellow outline isolates Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
4.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
4.j · Remove isolation outline; red equal-size boxes mark pure Nash cells [(0, 0), (1, 1)]. “Two pure-strategy Nash equilibria: both Play or both Movie.”
5.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(2, 2), (1, 0)], [(0, 1), (1, 1)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
5.b · Yellow outline isolates Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
5.c · Add pink boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
5.d · Yellow outline isolates Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
5.e · Add pink boxes to best-response payoffs at zero-based cells [(0, 1), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
5.f · Yellow outline isolates Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
5.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
5.h · Yellow outline isolates Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
5.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 0), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
5.j · Remove isolation outline; red equal-size boxes mark pure Nash cells [(0, 0), (1, 1)]. “A tie means that both strategies are best responses.”
5.k · Retain both red Nash boxes; overlay a same-size dashed green box on (Play, Play). “Both Play is Pareto efficient; both Movie is not.”
6.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(1, 0), (2, 1)], [(2, 1), (1, 1)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
6.b · Yellow outline isolates Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
6.c · Add pink boxes to best-response payoffs at zero-based cells [(1, 0)]. Keep earlier response boxes visible; ties receive two boxes.
6.d · Yellow outline isolates Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
6.e · Add pink boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.f · Yellow outline isolates Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
6.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.h · Yellow outline isolates Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
6.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 0), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.j · Remove isolation outline; red equal-size boxes mark pure Nash cells [(0, 1), (1, 0)]. “Two pure-strategy Nash equilibria: different activities.”
7.a · Gold “Question” heading and serif Ron-and-Harry room-cleaning prompt, copied verbatim from the old closing card.
-->

# D1 Games

Public goods

This video does a simulation of public goods, and maps it into game theory, using a Lindhal equilibrium, and using voting.

Instead of rival and non-excludable, what if a good were non-rival and excludable?

Again markets don’t do well. But what if we tried another approach?
