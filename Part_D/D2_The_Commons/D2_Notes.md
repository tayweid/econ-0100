---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
Revised 2026-10-26 for 10–20 minutes AFTER the live simulation. Target: about 15 minutes. D2_Animation.py, scene EpisodeD2. Sequence: simulation → one worked High/Low month → quick remaining months and Low/Low and High/High runs beside the accumulating graph → calculated 2×2 → incentives and tragedy. Keep the later months brisk: roughly two seconds of movement per month, with a manual hold after each. No catch ledger or separate recovery demonstration. External-cost arithmetic and institutional discussion below are optional spoken extensions, not extra animation scenes.
Sources: D2_Planning.md; Class_On_Oct_30.pdf, pp. 1–2, dated October 30, 2024. That source plots harvest, not population. Its illustrative payoff numbers differ from the new model’s calculated totals. NPR/public goods remain in D3.
Style: shared Graphite tokens, 2:1 frame, 15 fps, azure topic title, grey context subtitle, fixed 0.7443-scale gold teaching line centered 0.05 from the bottom. Keep the existing rounded white pond and scattered white dots. Firm 1 is pink; Firm 2 is teal. Each full dot is 1,000 fish; half and quarter sectors preserve the area of fractional thousands. Caught dots move into trays and acquire the firm's color; surviving parents stay fixed as translucent offspring copies with dashed edges move into vacant positions. Pause on the newborns; when the next month begins, fill them solid white and remove their dashed outlines. Population arithmetic stays in the instructor notes, off screen. Use D1’s diamond matrix and best-response boxes.
Every listed beat is a literal top-level self.pause in construct, including each graph reveal and each question/answer. No pause lives inside a loop or helper; computational loops do not play animations. The simulation has five holds; the explanation has twenty-three. There is no timed auto-advance.
-->

The simulation is outside this timing budget. A suggested pace for the explanation is:

| Segment | Minutes |
| --- | --- |
| Connect the simulation to a two-firm model | 2 |
| Establish the rule with the first High/Low month | 3 |
| Quickly run the remaining months and compare all three paths | 4 |
| Transfer payoffs and solve the matrix | 5 |
| State the tragedy of the commons | 1 |

For a ten-minute version, keep the graph discussion brief and use the symmetry of the firms. For twenty minutes, allow predictions at the existing holds. The later months are quick visual repetitions, not additional derivations.

<!--
Simulation opening copied from ../D0_Strategic_Interaction/03_Code.py on 2026-10-21 at Taylor's request; reference notes: Sim.md and D2_Simulation.md. Preserve D0's wording, grey rules, yellow Rules label, red Part D label, positions, and one-at-a-time reveals. The simulation heading is placed independently at the top because D2 does not have D0's raster bumper to anchor it. Timed waits become named ManimLive holds. No new simulation mechanics added. This five-firm, four-round activity precedes the distinct two-firm, three-month model.
sim.a · Title “Part D | Common Resources Simulation”; “Rules”; reveal “- One lake, five firms”.
sim.b · Add “- Each round, choose your harvest”.
sim.c · Add “- Fish population doubles each round”.
sim.d · Add “- Carrying capacity is 20,000 fish”.
sim.e · Add “- Maximize harvest after 4 rounds”; hold the complete card for the live simulation, then fade and clear before 1.a.
-->

## 1 | From the simulation to the model

<!--
1.a · D1 taxonomy with Common Resources highlighted; grey subtitle “Goods that are rival and non-excludable.”; no yellow note.
3.a · Pond and twenty dots on the left; “Two Strategies:” with “- Low Catch (L): ¼ of the Stock” and “- High Catch (H): ½ of the Stock” on the right; descriptions after the colons are grey; “Maximize total catch over 3 months.”
-->

> **1.a.** Briefly reconnect to D1’s taxonomy. Under the title, show the grey subtitle “Goods that are rival and non-excludable.” Leave the bottom clear, with no yellow note. The fish are rival, and neither firm can exclude the other from this pond. Hold, then move directly to the model.

A fish one firm catches is unavailable to the other. The catch is private, but the stock that produces future catches is shared.

> **3.a.** Keep the rounded pond at (−4, 0.15), width 5.4, height 2.8, corner radius 0.8, with twenty scattered dots and Stock: 20 placed 0.2 below the pond. The pond and readout together share the strategy panel’s vertical center; neither panel hugs the heading. Short subtitle: “One full dot = 1,000 fish.” On the right, show “Two Strategies:” at scale 0.85 above “- Low Catch (L): ¼ of the Stock” and “- High Catch (H): ½ of the Stock” at scale 0.75. Keep the heading and strategy names white; everything after each strategy’s colon is CAPTION grey. Align the three lines on the left with 0.55 spacing, centered as a group at (4, −0.15), the midpoint of the main content band. Bottom: “Maximize total catch over 3 months.” Hold. Explain the shares of starting stock, simultaneous choices, fixed strategies, reproduction rule, and payoff assumptions aloud using the paragraph below; do not display a second rules list or an assumptions caption.

Both firms calculate their catch from the same starting stock. After harvest, survivors double, up to the carrying capacity of 20,000. We count all three months’ catches, with equal value per fish, no costs, and no value assigned to the final stock. This is a small commitment game we can solve, not a biological model of tuna.

## 3 | Build all three paths beside the pond

<!--
3.b.choices · Compact pond and catch trays on the left; empty catch graph on the right; Month 1, Firm 1 High, Firm 2 Low; 1/2 × 20 = 10 and 1/4 × 20 = 5; pause before moving fish.
3.b.harvest · Move ten pink and five teal dots into their trays and plot Firm 1’s ten at month 1; Stock: 5; “Five thousand survive. How many fish next month?”
3.b.growth · Five stationary survivors each spawn a translucent, dashed-edge offspring; Stock: 10; “Each fish spawns one new fish.”; hold before newborns become solid white next month.
3.e.first · Month 2, H,L: catch 5 and 2.5, stock 2.5 grows to 5; add the first dashed segment; “Less stock, smaller catches.”
3.e.path · Month 3, H,L: catch 2.5 and 1.25, stock 1.25 grows to 2.5; complete 10 → 5 → 2.5; “High against Low: the stock halves, so the catch halves.”
3.e.total · Copy the three plotted catches into 10 + 5 + 2.5 = 17.5; show the Low firm's 5 + 2.5 + 1.25 = 8.75 beneath the graph; “Add the three catches to get each firm's payoff.”
3.e.low.first · Reset the pond to 20, both Low; Month 1: catch five each, ten reproduce to twenty; start the solid line; “Both Low: the stock returns to 20.”
3.e.low.second · Month 2, both Low: catch five each and replenish; extend the solid line; “The same catch, again.”
3.e.low · Month 3, both Low: repeat, complete 5 → 5 → 5 and show 15 | 15; “Both Low: 5 each month, 15 each in total.”
3.e.high.first · Reset to 20, both High; Month 1: catch ten each, Stock: 0; start the dotted line; “Both High: nothing left to reproduce.”
3.e.high.second · Month 2: empty pond, zero catch, extend the dotted line; “No stock, no catch.”
3.e.high · Month 3: still empty; complete 10 → 0 → 0 and show 10 | 10; “Both High: 10 now, then no fish left to catch.”
3.e.compare · Expand the same three paths and display all three total pairs; “Three paths, three payoff pairs.”
-->

> **3.b.choices.** Keep the existing pond and fish; shrink them to 80% and move the pond to (−4, 0.9). Place Month and Stock: on one header row above the pond, centered at (−5.35, 2.5) and (−2.95, 2.5), respectively. Keep the stock number’s anchor fixed as its value changes. Leave the space immediately beneath the pond clear. Place the firm names at y = −0.75 and the two catch trays at (−5.45, −1.45) and (−2.55, −1.45). Center the share calculations below them at y = −2.2. Leave the area beneath the catch calculations clear; show no population subtraction or growth formula. This separates the shared pond from the two catch columns without reducing type or dot sizes. Introduce an empty graph on the right, center (3.5, 0.2), width 5.8, height 3.4; months 1–3 and catches 0, 5, 10. Heading: “Firm 1′s catch (thousands)”. The grey month label and white stock readout stay above the pond throughout every run. Hold before the catch.

High takes 10,000 fish; Low takes 5,000. High gets more now. What happens to the stock they both depend on?

> **3.b.harvest.** Move the actual ten and five dots into the corresponding trays, shrinking slightly to fit. Keep the remaining five in place. Carry a copy of Firm 1’s catch of ten into the graph’s first point label. Keep Stock: fixed and change only its number to 5. Hold on the reproduction question.

> **3.b.growth.** Keep each of the five parents fixed. Give each a newborn copy with 30% white fill and a dashed white edge; move the copy into a vacant position while Stock: changes from 5 to 10. Hold with those five newborns still visibly distinct. At the start of month 2, fill them solid white and remove their dashed edges as the month label changes. Use this same birth → pause → maturity sequence in every growing month. Do not display subtraction, doubling, or min/max formulas. The empty pond in High/High produces no newborns.

The stock has fallen from 20,000 to 10,000. Keeping the same strategies now means smaller catches. For instructor reference only (not displayed), in thousands of fish the rule is

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{20,2S_t\}.
$$

> **3.e.first–3.e.path.** Keep both panels throughout months 2 and 3. Begin each month by turning the previous newborns solid white and removing their dashed edges. Clear the previous catches from the trays, advance the month label, and update the two share calculations. Move the actual catch portions from the pond as the corresponding graph point and segment appear. Then each survivor spawns one translucent, dashed-edge copy; parents stay fixed. Use half and quarter sectors when a catch divides a thousand-fish dot, preserving total area. Month 2 ends with Stock: 5; month 3 ends with Stock: 2.5. Use a 0.6-second catch move and 0.8-second birth move, followed by a top-level manual pause with newborns still translucent. Keep all three plotted numeric catches until they supply the sum. No population arithmetic appears below the trays.

High’s catches fall from ten to five to two and a half. Low takes half as much along the same stock path.

> **3.e.total.** Keep the pond and graph. Beneath the graph, copy the three pink point values into 10 + 5 + 2.5 = 17.5. Underneath show the teal sum 5 + 2.5 + 1.25 = 8.75. Hold, then carry those sums into a stored H,L payoff pair. Remove that pair and the point numerals when the next scenario starts, retaining the curve and its direct H,L label.

Our payoff is the sum of the three catches, not the last point on the graph. High earns 17.5; Low earns 8.75.

> **3.e.low.first–3.e.low.** Reset the pond once: show twenty solid fish, Month 1, and both firms Low. Keep the earlier H,L path in place. Update Firm 1 to Low and both share calculations to ¼ × 20 = 5. Run three quick months: five dots into each tray, ten survivors stay fixed, ten translucent newborn copies with dashed edges refill the pond. Each catch adds the next point and solid segment at five; each growth returns Stock: to 20. Clear old tray catches and turn the previous newborns solid white when advancing to the next month. Pause once per month with the new offspring still translucent without repeating the introductory explanation. At month 3, label L,L and show 15 | 15 beneath the graph.

When both choose Low, ten thousand fish survive each month and reproduce back to twenty thousand. Each firm keeps catching five thousand: fifteen thousand in total.

> **3.e.high.first–3.e.high.** Reset once to twenty solid fish and Month 1, and change both firms to High. In month 1 move ten dots into each tray and set Stock: 0. Leave the pond empty, with no offspring and no population formula. Plot ten at month 1. For months 2 and 3 keep the pond empty and update the month label; plot zero and draw each dotted segment as the empty trays and zero share calculations remain visible. Pause once per month. End with H,H and 10 | 10 beneath the graph. Preserve the earlier paths throughout.

When both choose High, they exhaust the pond immediately. Each catches ten, then nothing. A large first catch is not the same as a large three-month payoff.

> **3.e.compare.** Fade the pond and its labels, trays, and catch calculations. Expand the same axes, all nine point objects, three paths, and their direct labels into the full graph layout (center −2.3, −0.2; width 7, height 3.5). Change the title to “Catch Over Time.” Put the three stored result pairs in the right-hand column beneath “Three-month totals”. Hold before transferring them to the matrix. All curves show Firm 1’s catch: solid L,L; dashed H,L; dotted H,H. Reversing the firms supplies L,H by symmetry; no fourth run is needed.

## 4 | Put the payoffs in a game and solve it

<!--
4.a · Carry the graph’s result pairs into D1’s diamond matrix; reflect H,L to obtain L,H; “Firm 1's payoff first; Firm 2's payoff second.”
4.b · Hold Firm 2 Low; ask Firm 1’s best response.
4.c · Box 17.5 in pink; “High: 17.5 > 15.”
4.d · Hold Firm 2 High; ask Firm 1’s best response.
4.e · Box 10 in pink; “High: 10 > 8.75.”
4.f · Add Firm 2’s two teal best-response boxes by symmetry; “The same comparisons hold for Firm 2. Both prefer High.”
4.j · Red outline around H,H; “Neither firm gains by changing its strategy alone.”
4.k · Green outline around L,L, retain red H,H, show 15 > 10 for each firm; “Tragedy of the commons: both would do better with Low.” End.
-->

> **4.a.** Retain the result pairs while the graph fades, move them above D1’s diamond matrix, and copy their values into its cells. Reversing the firms reverses the H,L payoffs; no fourth run is needed. Fade the source pairs and hold on the complete unmarked matrix. Preserve D1 geometry, horizontal numbers, and player colors.

| Firm 1 / Firm 2 | Low | High |
| --- | --- | --- |
| Low | 15, 15 | 8.75, 17.5 |
| High | 17.5, 8.75 | 10, 10 |

> **4.b–4.e.** Two separate question/answer pairs. Shade only Firm 2’s fixed column teal and underline its choice; pause on each question before boxing Firm 1’s better payoff in pink. Keep its previous response box when switching columns.

If Firm 2 chooses Low, Firm 1 prefers 17.5 to 15. If Firm 2 chooses High, Firm 1 prefers 10 to 8.75. High is a **strictly dominant strategy**.

> **4.f.** Remove the column shading and underline. Add Firm 2’s teal response boxes together, using symmetry instead of repeating all four questions. Pause before identifying the equilibrium.

> **4.j.** Retain response boxes and outline High, High in red. Hold on the unilateral-deviation test: neither firm can improve by changing alone. This is the **Nash equilibrium**.

> **4.k.** Add the matching green outline around Low, Low, and “15 > 10 for each firm” beside the matrix. Hold and finish the core explanation here.

Both would do better if both chose Low. But each prefers High given either choice by the other firm. That conflict between individual incentives and the shared outcome is the **tragedy of the commons**.

## Optional discussion | Beyond the short lesson

Return to the question from Part C: what does the decision maker count, and what happens to everyone affected? When Firm 1 switches to High against Low, it gains 2,500 fish. Firm 2 loses 6,250. The combined catch falls by 3,750.

This is an external cost. Firm 1 bears some of the effect of reducing the stock, but it does not bear Firm 2′s loss. Knowing that cooperation would help both firms is not enough to make cooperation a best response.

An agreement can work if the rules and incentives support it. We could limit harvests, observe catches, and enforce the limits. We could also ask how communication and future dealings affect behavior. Shared use does not guarantee failure; this particular game explains why cooperation needs support.
