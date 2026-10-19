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
only the rival's fixed choice: a single band at 12% opacity behind the grid
and numbers. Both players retain colored choice underlines. Start from
Player 1's perspective with Player 2's Cooperate column shaded teal. Once
Player 1 defects, switch to Player 2's perspective: replace the teal shading
with Player 1's Defect row in pink, ask what Player 2 should do, and reveal
Player 2's payoffs from Cooperate (0) and Defect (1) sequentially. At mutual
Defect, return to Player 1's perspective by replacing pink with Player 2's
Defect column in teal; reveal Player 1's payoff of 1, then consider Cooperate.
Keep choice/question pauses separate from payoff answers. Never retain both
players' background bands at a pause.
During best-response analysis in all four games, only the choice held fixed
is underlined and shaded; remove both cues for the equilibrium summary.
The background band and choice underline identify the fixed strategy.
Individual best-response boxes remain upright.
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
2.c · “Baby Game Theory”: show the Nash Equilibrium definition alone; clear it before the first matrix. Best Response and Dominant Strategy now follow Player 1’s worked example at 3.e2–3.e3.
3.a1 · Prisoner's Dilemma: reveal the diamond grid, then Player 1's two choices. Gold caption: “Player 1 chooses Cooperate or Defect.”
3.a2 · Reveal Player 2's two choices. Gold caption: “Player 2 also chooses Cooperate or Defect.”
3.a2r · Player 2 chooses Cooperate. Underline Cooperate in teal and shade only Player 2’s corresponding column. Pause before Player 1 chooses; no payoffs yet.
3.a3q · Player 1 chooses Cooperate. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a3 · Both cooperate: Player 1 receives 3. Reveal only Player 1’s payoff at cell (0, 0) and its grey pipe. Keep earlier numbers visible.
3.a4 · Both cooperate: Player 2 receives 3. Reveal only Player 2’s payoff at cell (0, 0). Keep earlier numbers visible.
3.a5q · Player 1 chooses Defect. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a5 · Only Player 1 defects: Player 1 receives 5. Reveal only Player 1’s payoff at cell (1, 0) and its grey pipe. Keep earlier numbers visible.
3.a6q · Switch to Player 2's perspective: fade out Player 2's teal column shading and shade only Player 1's Defect row pink. Keep both choice underlines. Gold caption: “Player 1 defects. What should Player 2 do?” Pause before revealing Player 2's payoff.
3.a6 · Gold caption: “Cooperating gives Player 2 a payoff of 0.” Reveal Player 2's 0 at cell (1, 0); keep Player 1's Defect row shaded.
3.a6r · Move Player 2's teal underline to Defect, retaining Player 1's pink Defect underline and row shading. Gold caption: “What if Player 2 defects instead?” Pause with the new payoff hidden.
3.a8 · Reveal Player 2's 1 and the grey pipe at cell (1, 1), before Player 1's payoff. Gold caption: “Defecting raises Player 2's payoff from 0 to 1.” Retain only Player 1's Defect row shading.
3.a7q · Switch back to Player 1's perspective: fade out the pink row shading and shade Player 2's Defect column teal. Keep both Defect underlines. Gold caption: “Back to Player 1: what is the payoff from Defect?” Pause with Player 1's payoff hidden.
3.a7 · Both defect: Player 1 receives 1. Reveal only Player 1's payoff at cell (1, 1); the pipe and Player 2's 1 are already visible.
3.a9q · Player 1 chooses Cooperate. What is their payoff? Show Player 1’s pink choice underline; retain only Player 2’s background shading. Pause with the new payoff hidden.
3.a9 · Only Player 2 defects: Player 1 receives 0. Reveal only Player 1’s payoff at cell (0, 1) and its grey pipe. Keep earlier numbers visible.
3.a · Only Player 2 defects: Player 2 receives 5. Reveal only Player 2’s payoff at cell (0, 1). Keep earlier numbers visible.
3.b · Teal shading and underline identify Player 2 choosing Cooperate; “If Player 2 chooses Cooperate, what is your best response?”
3.c · Add pink boxes to best-response payoffs at zero-based cells [(1, 0)]. Keep earlier response boxes visible; ties receive two boxes.
3.d · Teal shading and underline identify Player 2 choosing Defect; “If Player 2 chooses Defect, what is your best response?”
3.e · Add pink boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.e1 · Remove Player 2's fixed-choice shading and underline; retain both pink best-response payoff boxes. Gold caption: “Player 1's dominant strategy is Defect.” Pause to establish the result before defining it.
3.e2 · Slide all visible game objects 3.7 units left at their existing size, retaining the title and bottom caption. Draw the familiar subtle grey vertical divider downward at x=0.3, from y=2.5 to -3.0 (MUTED, width 1, opacity 0.5). Fade in Best Response on the right: original definition wording reflowed at scale 0.7, gold term and white serif body. Pause.
3.e3 · Fade in Dominant Strategy below Best Response, matching its typography, with a 0.65-unit gap. Pause with both definitions and the worked game visible. Then fade out the definitions/divider and return the game to its original centered position before continuing Player 2's best-response analysis.
3.f · Pink shading and underline identify Player 1 choosing Cooperate; “If Player 1 chooses Cooperate, what is your best response?”
3.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.h · Pink shading and underline identify Player 1 choosing Defect; “If Player 1 chooses Defect, what is your best response?”
3.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
3.j · Remove choice shading and underline; red equal-size boxes mark pure Nash cells [(1, 1)]. “Both players have a dominant strategy: Defect.”
3.k · Green box, same dimensions as Nash boxes, marks [(0, 0)]. “Both players prefer (3, 3) to (1, 1).”
4.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(2, 1), (0, 0)], [(0, 0), (1, 2)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
4.b · Teal shading and underline identify Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
4.c · Add pink boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
4.d · Teal shading and underline identify Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
4.e · Add pink boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
4.f · Pink shading and underline identify Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
4.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
4.h · Pink shading and underline identify Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
4.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
4.j · Remove choice shading and underline; red equal-size boxes mark pure Nash cells [(0, 0), (1, 1)]. “Two pure-strategy Nash equilibria: both Play or both Movie.”
5.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(2, 2), (1, 0)], [(0, 1), (1, 1)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
5.b · Teal shading and underline identify Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
5.c · Add pink boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
5.d · Teal shading and underline identify Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
5.e · Add pink boxes to best-response payoffs at zero-based cells [(0, 1), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
5.f · Pink shading and underline identify Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
5.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 0)]. Keep earlier response boxes visible; ties receive two boxes.
5.h · Pink shading and underline identify Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
5.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 0), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
5.j · Remove choice shading and underline; red equal-size boxes mark pure Nash cells [(0, 0), (1, 1)]. “A tie means that both strategies are best responses.”
5.k · Retain both red Nash boxes; overlay a same-size dashed green box on (Play, Play). “Both Play is Pareto efficient; both Movie is not.”
6.a · Diamond layout (45 degrees clockwise, upright text). “Play Or Movie”: Player 2 column headers, then Player 1 row headers, then payoff cells in row order: [[(1, 0), (2, 1)], [(2, 1), (1, 1)]]. Row payoff is pink, column payoff teal. “Payoffs: Player 1 first, Player 2 second.”
6.b · Teal shading and underline identify Player 2 choosing Play; “If Player 2 chooses Play, what is your best response?”
6.c · Add pink boxes to best-response payoffs at zero-based cells [(1, 0)]. Keep earlier response boxes visible; ties receive two boxes.
6.d · Teal shading and underline identify Player 2 choosing Movie; “If Player 2 chooses Movie, what is your best response?”
6.e · Add pink boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.f · Pink shading and underline identify Player 1 choosing Play; “If Player 1 chooses Play, what is your best response?”
6.g · Add teal boxes to best-response payoffs at zero-based cells [(0, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.h · Pink shading and underline identify Player 1 choosing Movie; “If Player 1 chooses Movie, what is your best response?”
6.i · Add teal boxes to best-response payoffs at zero-based cells [(1, 0), (1, 1)]. Keep earlier response boxes visible; ties receive two boxes.
6.j · Remove choice shading and underline; red equal-size boxes mark pure Nash cells [(0, 1), (1, 0)]. “Two pure-strategy Nash equilibria: different activities.”
7.a · Gold “Question” heading and serif Ron-and-Harry room-cleaning prompt, copied verbatim from the old closing card.
-->

# D1 Games

Public goods

This video does a simulation of public goods, and maps it into game theory, using a Lindhal equilibrium, and using voting.

Instead of rival and non-excludable, what if a good were non-rival and excludable?

Again markets don’t do well. But what if we tried another approach?
