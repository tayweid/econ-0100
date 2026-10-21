---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
Script and storyboard, drafted 2026-10-20; commons animation implemented 2026-10-21 in D2_Animation.py, scene EpisodeD2. Sequence: live simulation → brief common-resource definition → fishing model → derived 2×2 and its solution. Original beat IDs are retained for continuity; the separate section 2 demonstrations have been removed. Public-goods material moved to ../D3_Public_Goods_and_Voting/D3_Notes.md before implementation. This is a proposed new script, not a transcription of the 2024 class. The numbered legacy files remain untouched pending review.
Sources and teaching choices: D2_Planning.md. Primary source: Class_On_Oct_30.pdf, pp. 1–2, created October 30, 2024. D2 develops the tuna/commons game; the NPR donation game begins D3. The new pond model below generates its own payoff numbers; the original tuna matrix is retained in the planning notes and must not be represented as a calculation from this model.
Style references: ../../_Style_Guide.md, ../D1_Games/D1_Notes.md and D1_Animation.py, ../../Part_C/C1_Externalities/C1_Notes.md, ../../Part_C/C3_Corrective_Policy/C3_Notes.md, ../../Part_C/C4_Wrap_Up/C4_Notes.md. Use the current Notes-file convention: section comments index beats; quote blocks give detailed directions; ordinary paragraphs are proposed narration. No student beat links are introduced.
Stage: Graphite 2:1, 15 fps, CMU Serif teaching content, azure topic titles, optional grey CMU Sans subtitle, fixed 0.7443-scale gold teaching line centered 0.05 from the bottom. Body band y = −2.8 to 2.5, centered at −0.15. Import shared style tokens. No illustrated fishermen or decorative scenery: one INK pond outline, neutral fish tokens, and named catch trays. Firm 1 is ROW_PLAYER pink; Firm 2 is COL_PLAYER teal. Fish acquire a firm's color only when caught. A full dot represents 1,000 fish; circular sectors represent fractional thousands by area, with exact numeric readouts. Catch-ledger tokens use a smaller display scale than pond tokens. Keep a rounded pond boundary fixed, using B2’s neutral outline treatment. Pond center (−4, 0.85), width 5.4, height 2.8, corner radius 0.8. Dots have radius 0.16 and twenty fixed, scattered positions, not a grid. A single grey subtitle under the title reads “One dot = 1,000 fish. Survivors double after harvest, up to 20,000 fish.” It replaces the capacity label above the pond and the units caption below it, including during the three-month runs. During the first Low/Low month, the stock readout moves into a compact timeline below the pond: Month 1 → After catch → Month 2. Its final value becomes the stock readout for the rest of the run. Other months retain local Start, Survivors, and Next stock readouts. Survivors keep their exact positions and object identities. Only offspring copies move into vacant positions. At fractional catch boundaries, divide the existing dot into circular sectors in place; do not replace the population. A caught dot retains its identity as it moves and shrinks into the ledger. Fewer fish do not mean less water or a smaller carrying capacity.
Pacing follows C1/C3: quantities first, question and pause, calculation, answer and pause. Carry the same fish into catch trays and the same totals into matrix cells. D1's best-response boxes precede Nash and efficiency conclusions. Each dotted ID is a stopped beat unless its direction explicitly describes a continuous transition.
D2 opens with the original D0 simulation rules card (sim.a–sim.e), followed by the common-resource definition and the fishing game. Mechanics are taught within the first game run, without separate harvest or recovery demonstrations. Hold at sim.e to run the live activity. The separate optional two-firm prediction exercise can follow 3.a; see D2_Simulation.md.
-->

<!--
Simulation opening copied from ../D0_Strategic_Interaction/03_Code.py on 2026-10-21 at Taylor's request; reference notes: Sim.md and D2_Simulation.md. Preserve D0's wording, grey rules, yellow Rules label, red Part D label, positions, and one-at-a-time reveals. The simulation heading is placed independently at the top because D2 does not have D0's raster bumper to anchor it. Timed waits become named ManimLive holds. No new simulation mechanics added. This five-firm, four-round activity precedes the distinct two-firm, three-month model.
sim.a · Title “Part D | Common Resources Simulation”; “Rules”; reveal “- One lake, five firms”.
sim.b · Add “- Each round, choose your harvest”.
sim.c · Add “- Fish population doubles each round”.
sim.d · Add “- Carrying capacity is 20,000 fish”.
sim.e · Add “- Maximize harvest after 4 rounds”; hold the complete card for the live simulation, then fade and clear before 1.a.
-->

## 1 | A shared pond

<!-- 1.a · Title “Common Resources”; reuse D1's taxonomy and isolate Common Resources; bottom “What changes when we cannot exclude other users?” -->

> **1.a.** Start with D1′s existing taxonomy geometry. Highlight Common Resources, preserving the Rival and Non-Excludable labels, then fade the other categories. Pause before introducing the pond. Do not rerun the A/B/C tour or the deadline activity.

In D1, we learned how to ask what each player would choose, given what the other player does. Today we will build the payoffs from something we can see: two fishing firms using the same pond.

The fish are **rival**: catching one leaves one fewer for someone else. Access is **non-excludable in our setup**: neither firm can keep the other from fishing. These are the characteristics of a **common resource**.

The catch belongs to the firm that takes it. The remaining fish, and the fish they can produce, are shared. We will simplify the activity to two firms and two strategies so that we can explain the incentives with a 2×2 game.

## 3 | Two strategies, three months

<!--
3.a · Title “The Fishing Game”; pond and subtitle on the left, L/H rules and three-month payoff on the right; bottom “To explain the incentives: two firms, two strategies.”
3.b.choices · Both firms Low: show each 1/4 × 20 = 5 before moving the dots.
3.b.survivors · Catch five per firm; timeline moves to After catch; hold 20 − 5 − 5 = ?.
3.b.harvest · Stop after the first harvest at 10 survivors; bottom “What stock will these survivors produce?”
3.b.first · Stop after month 1 and predict the next catch.
3.b · L,L: three harvests of 5 each; bottom “Low harvests maintain the stock.”
3.c.harvest · Stop after the first harvest at 5 survivors; bottom “What stock will these survivors produce?”
3.c.first · Stop after month 1 and predict catches from a stock of 10.
3.c · H,L: Firm 1 catches 10, 5, 2.5; Firm 2 catches 5, 2.5, 1.25; bottom “A larger share today can leave fewer fish tomorrow.”
3.d.harvest · Stop after the first harvest at zero survivors; bottom “What stock will these survivors produce?”
3.d.first · Stop at the empty pond after month 1.
3.d · H,H: each catches 10, 0, 0; bottom “Both firms empty the pond in the first month.”
-->

We need to specify the game before solving it. Each firm chooses a fishing strategy at the beginning and keeps it for three months:

- **Low, L:** catch one-quarter of the stock each month.
- **High, H:** catch one-half of the stock each month.

Both firms fish simultaneously from that month’s starting stock. The percentages are not applied one after the other. Even two High choices take no more than the available fish.

The payoff is the firm’s **total catch over three months**, in thousands of fish. Every unit of catch has the same value, and we leave fishing costs out of this first model. We score only these three months; fish left at the end are not added to the score. We are comparing two committed strategies, not allowing a new decision each month.

> **3.a.** Introduce the rounded pond, twenty scattered dots, and the units-and-reproduction subtitle on the left. Place L/H rules, simultaneous choices, the three-month commitment, and payoff assumptions on the right. Pause before showing an outcome. Replace the rules with the catch ledger, keeping the same pond and twenty dots.

We keep the simulation’s simple population rule: harvest first, then survivors double, up to 20,000 fish. That is the pond’s **carrying capacity**, a limit on the stock rather than a promise of a fresh catch every month. These are model fish, not a biological estimate for tuna.

> **3.b.choices.** Label both firms Low. Show a pink and a teal 1/4 × 20 = 5 below the pond. Pause before moving any fish. Replace these calculations with a compact timeline below the pond: Month 1 → After catch → Month 2. Move the existing stock number into its first node, removing the Stock label; later values remain blank until calculated.

> **3.b.survivors.** Move five existing dots into each firm’s first-month ledger compartment, shrinking to 65% display scale and recoloring by firm. The timeline ring moves to After catch. Carry copies of the starting stock and the two catch readouts into 20 − 5 − 5 = ?. Ask how many remain, then pause. Reveal ten and copy the result into the timeline’s middle node. The ten surviving dots stay in their original positions.

> **3.b.harvest–3.b.first.** Ask what stock these survivors produce, then pause. Copy ten from the subtraction into min{20, 2 × 10} = 20. Keep parents stationary while ten offspring copies move to vacant positions. Move the ring to Month 2 and copy the growth result into that endpoint. Hold on the completed 20 → 10 → 20 timeline and ask what each firm catches next month. The endpoint then becomes the local stock readout as the timeline fades.

The catch leaves 10,000 fish. They reproduce, restoring the pond to 20,000. Next month each Low firm again takes one-quarter of that stock.

For reference, let $N_t$ be the starting stock, $h_{1t}$ and $h_{2t}$ the catches, and $S_t$ the survivors, all in thousands of fish. The arithmetic we just watched is

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{20,2S_t\}.
$$

> **3.b.** Continue the same population through months 2 and 3. Keep the pond and ledger fixed. Each month’s Start, Survivors, and Next stock readouts connect to the subtraction and reproduction equations. For each firm, carry copies of the ledger counts into 5 + 5 + 5 = 15 before revealing the total. Save copies of these actual totals for the matrix.

With two Low strategies, each firm catches 5,000 fish per month. Each collects 15,000 over three months, and the pond keeps returning to capacity.

> **3.c.** Keep the pond boundary and ledger grid fixed while fading the completed trial and resetting the population. Set Firm 1/High and Firm 2/Low. Pause at five survivors after month 1, then at the reproduced stock of ten. In later months, split only dots crossed by an exact catch boundary into proportional circular sectors; the pieces preserve the original area and position until caught. Never reconstruct or repack survivors. Run the catch sequences (10,5,2.5) and (5,2.5,1.25); copy their ledger counts into the totals 17.5 and 8.75. Save the total objects for comparison. Exchanging firms exchanges the payoffs; a fourth full run is unnecessary.

If Firm 1 switches to High while Firm 2 stays Low, Firm 1 catches more. But the combined catch leaves too few survivors to restore the pond. The starting stock halves each month: 20, then 10, then 5. Firm 1 gets 17,500 fish in total. Firm 2 gets 8,750.

> **3.d.** Reset the population inside the same pond. With both firms High, move ten existing dots into each firm’s first-month compartment. Stop at zero survivors, then show the growth equation yielding zero. Continue months 2 and 3 with zero catches and no offspring. Carry the ledger values into 10 + 0 + 0 = 10 for each firm. Save the totals for comparison.

If both choose High, they empty the pond in the first month. Each gets 10,000 fish, and nothing in months 2 and 3.

The first month’s biggest catch is not necessarily the best three-month outcome. Now we can put the whole consequence of each pair of strategies into a matrix.

## 4 | The pond becomes a payoff matrix

<!--
4.a · Title “The Fishing Game”; transfer calculated totals into D1's diamond matrix; bottom “Firm 1's payoff first; Firm 2's payoff second.”
4.b · Hold Firm 2 at L; bottom “If Firm 2 chooses Low, what is Firm 1's best response?”
4.c · Box 17.5 in pink; bottom “High: 17.5 > 15.”
4.d · Hold Firm 2 at H; bottom “If Firm 2 chooses High, what is Firm 1's best response?”
4.e · Box 10 in pink; bottom “High: 10 > 8.75.”
4.f · Hold Firm 1 at L; bottom “If Firm 1 chooses Low, what is Firm 2's best response?”
4.g · Box 17.5 in teal; bottom “High: 17.5 > 15.”
4.h · Hold Firm 1 at H; bottom “If Firm 1 chooses High, what is Firm 2's best response?”
4.i · Box 10 in teal; bottom “High: 10 > 8.75.”
4.j · Remove choice shading; outline H,H in NASH red; bottom “Neither firm gains by changing its strategy alone.”
4.k · Add totals 30, 26.25, 26.25, 20; outline L,L in EFFICIENT green; bottom “Both firms would catch more if both chose Low.”
-->

> **4.a.** Collect the three calculated payoff pairs as result cards and carry them directly into D1′s matrix layout. This is a continuous transition, without a separate harvest plot or comparison pause. Use 1.5-unit square cells rotated clockwise 45 degrees; board center (0, −0.5); keep text horizontal and player names at y = 2.0. Firm 1 is the row player, Firm 2 the column player. Original upper-left L,L is the top diamond cell; L,H right; H,L left; H,H bottom. Fill L,L, H,L, its reflected L,H, then H,H, completing each payoff pair before the next. Strategy labels are grey CMU Sans; payoffs use player colors. No best-response, Nash, or efficiency boxes yet.

| Firm 1 / Firm 2 | Low | High |
| --- | --- | --- |
| Low | 15, 15 | 8.75, 17.5 |
| High | 17.5, 8.75 | 10, 10 |

> **4.b–4.i.** Follow the eight separate question/answer pauses indexed above. For Firm 1, shade only Firm 2′s fixed column teal at 12% opacity and underline its fixed strategy. On each answer add the pink box around Firm 1′s best-response payoff. Then switch perspective: remove the teal band and underline, shade only Firm 1′s fixed row pink, and add teal boxes around Firm 2′s answers. Keep earlier payoff boxes. Never show both background bands at once. Use the existing D1 geometry rather than a new matrix treatment.

If Firm 2 chooses Low, Firm 1 compares 15 with 17.5 and chooses High. If Firm 2 chooses High, Firm 1 compares 8.75 with 10 and again chooses High. High is a **strictly dominant strategy** for Firm 1. The same comparisons apply to Firm 2.

> **4.j.** Remove fixed-choice underlines and background bands. Retain payoff boxes and add D1′s equal-size red Nash outline around H,H. Pause on the unilateral-deviation test before saying “Nash equilibrium.”

The **Nash equilibrium** is High, High. Given the other firm’s strategy, neither firm can improve its payoff by changing alone.

> **4.k.** Reveal the sum of the two payoffs for each outcome outside its cell, then a green efficiency outline around L,L, equal in size to the red outline. Retain both outcomes for comparison. Do not confuse an outcome’s total with either player’s individual payoff.

But both firms would get 15 instead of 10 if they both chose Low. Low, Low also produces the largest combined catch among the four strategy pairs: 30,000 fish. The equilibrium and the jointly best outcome differ.

This is the **tragedy of the commons**: individual incentives can lead to overuse of a shared resource. The problem is not that the fish cannot reproduce. It is that neither firm has an incentive to choose the strategy that works best when both follow it.

## 5 | The incentive we are missing

<!--
5.a.private · Reveal Firm 1’s private gain, +2.5.
5.a.external · Reveal Firm 2’s loss, −6.25.
5.a · Title “Private And Shared Consequences”; reopen L,L → H,L; bottom “The extra catch benefits one firm and reduces the other's catch.”
5.b · Title “Changing The Game”; return to the unmarked matrix; bottom “What would make Low a best response?”
5.b.rules · After discussion, reveal harvest rules, monitoring, and consequences for violations.
-->

> **5.a.** Carry the L,L and H,L payoff pairs out of the matrix into two side-by-side comparisons. Reveal Firm 1′s change, 17.5 − 15 = +2.5, then pause. Reveal Firm 2′s change, 8.75 − 15 = −6.25, then the combined change, −3.75. Keep the comparison on one common baseline, using the firms’ colors and TOTAL purple for the combined result. Reveal only one calculation at a time; clear each question before its answer.

Return to the question from Part C: what does the decision maker count, and what happens to everyone affected? When Firm 1 switches to High against Low, it gains 2,500 fish. Firm 2 loses 6,250. The combined catch falls by 3,750.

This is an external cost. Firm 1 bears some of the effect of reducing the stock, but it does not bear Firm 2′s loss. Knowing that cooperation would help both firms is not enough to make cooperation a best response.

> **5.b.** Restore the original calculated matrix without Nash/efficiency outlines. Hold on the question. After discussion, reveal three short grey labels beside it, one at a time: “Harvest rules”, “Monitoring”, “Consequences for violations”. Do not display an altered numerical matrix without specifying an actual enforcement rule.

An agreement can work if the rules and incentives support it. We could limit harvests, observe catches, and enforce the limits. We could also ask how communication and future dealings affect behavior. Shared use does not guarantee failure; this particular game explains why cooperation needs support.
