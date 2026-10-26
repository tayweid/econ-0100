---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
Revised 2026-10-26 for 10–20 minutes AFTER the live simulation. Target: about 15 minutes. D2_Animation.py, scene EpisodeD2. Sequence: simulation → one worked High/Low month → quick remaining months and Low/Low and High/High runs beside the accumulating graph → calculated 2×2 → incentives and tragedy. Keep the later months brisk: roughly two to three seconds of movement per month, with a brief manual hold on catches and another on newborns or the completed graph point. No catch ledger or separate recovery demonstration. External-cost arithmetic and institutional discussion below are optional spoken extensions, not extra animation scenes.
Sources: D2_Planning.md; Class_On_Oct_30.pdf, pp. 1–2, dated October 30, 2024. That source plots harvest, not population. Its illustrative payoff numbers differ from the new model’s calculated totals. NPR/public goods remain in D3.
Style: shared Graphite tokens, 2:1 frame, 15 fps, azure topic title, grey context subtitle, fixed 0.7443-scale gold teaching line centered 0.05 from the bottom. Keep the existing rounded white pond and scattered white dots. Firm 1 is pink; Firm 2 is teal. Each full dot is 1,000 fish; half and quarter sectors preserve the area of fractional thousands. Caught dots move into trays and acquire the firm's color. Only after they arrive, show “Catch: [number]” labels centered above the trays and pause. On advance, move only the number from Firm 1’s catch label into its graph label while its “Catch:” prefix, both firms’ caught dots and Firm 2’s count fade in the same animation. Keep the firm names and empty trays visible. No harvest equations appear. Surviving parents stay fixed as translucent offspring copies with dashed edges move into vacant positions. Pause on the newborns; when the next month begins, fill them solid white and remove their dashed outlines. Population arithmetic stays in the instructor notes, off screen. Use D1’s diamond matrix and best-response boxes.
Every listed beat is a literal top-level self.pause in construct, including each graph reveal and each question/answer. No pause lives inside a loop or helper; computational loops do not play animations. The simulation has five holds; the explanation has thirty-one; the added catch holds are brief visual beats, not extra derivations. There is no timed auto-advance.
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
3.b.choices · Centered Month 1 heading, pond, Stock readout and two firm boxes on the left; empty graph on the right; no harvest equations or premature counts.
3.b.harvest · Move ten pink and five teal dots into their boxes, then reveal counts 10 and 5; Stock: 5; pause with no graph point yet.
3.b.growth · Move 10 onto the graph while both catches and the teal count fade; five stationary survivors spawn translucent, dashed-edge offspring; Stock: 10; hold on newborns.
3.e.first.catch · Month 2, H,L: move fish, then reveal counts 5 and 2.5; Stock: 2.5; hold before plotting.
3.e.first · Transfer 5 while catches fade; add the first dashed segment; spawn offspring; Stock: 5; “Less stock, smaller catches.”
3.e.path.catch · Month 3, H,L: move fish, then reveal counts 2.5 and 1.25; Stock: 1.25; hold before plotting.
3.e.path · Transfer 2.5 while catches fade; complete 10 → 5 → 2.5; spawn offspring; Stock: 2.5; “High against Low: the stock halves, so the catch halves.”
3.e.total · Copy the three plotted catches into 10 + 5 + 2.5 = 17.5; show the Low firm's 5 + 2.5 + 1.25 = 8.75 beneath the graph; “Add the three catches to get each firm's payoff.”
3.e.low.first.catch · Reset to 20, both Low; move five fish into each box, reveal counts 5 and 5; Stock: 10; hold.
3.e.low.first · Transfer 5 while catches fade; start the solid line; ten reproduce to twenty; “Both Low: the stock returns to 20.”
3.e.low.second.catch · Month 2, both Low: mature newborns, move fish, reveal counts 5 and 5; Stock: 10; hold.
3.e.low.second · Transfer 5 while catches fade; extend the solid line; replenish; “The same catch, again.”
3.e.low.catch · Month 3, both Low: mature newborns, move fish, reveal counts 5 and 5; Stock: 10; hold.
3.e.low · Transfer 5 while catches fade; complete 5 → 5 → 5, replenish and show 15 | 15; “Both Low: 5 each month, 15 each in total.”
3.e.high.first.catch · Reset to 20, both High; move ten fish into each box, reveal counts 10 and 10; Stock: 0; hold.
3.e.high.first · Transfer 10 while catches fade; start the dotted line; “Both High: nothing left to reproduce.”
3.e.high.second.catch · Month 2: empty pond; show “Catch: 0” above each empty box; hold before plotting.
3.e.high.second · Transfer zero while the other zero fades; extend the dotted line; “No stock, no catch.”
3.e.high.catch · Month 3: still empty; show counts 0 and 0; hold before plotting.
3.e.high · Transfer zero while the other zero fades; complete 10 → 0 → 0 and show 10 | 10; “Both High: 10 now, then no fish left to catch.”
3.e.compare · Expand the same three paths and display all three total pairs; “Three paths, three payoff pairs.”
-->

> **3.b.choices.** Keep the existing pond and fish; shrink them to 80% and move the pond to (−4, 0.85). Center Month 1 at (−4, 2.35), level with the graph heading. Put Stock: directly beneath the pond at (−4, −0.65), with its number’s anchor fixed throughout. Below the stock, arrange two firm columns centered at x = −5.45 and −2.55: names at y = −1.25, rounded boxes 2.3 wide by 0.9 high at y = −2.5, and “Catch: [number]” labels at y = −1.8 only after the fish arrive. This gives each row its own space and keeps the footer separate. Introduce an empty graph on the right, center (3.5, 0.2), width 5.8, height 3.4; months 1–3 and catches 0, 5, 10. Heading: “Firm 1’s catch (thousands)”. Hold before the catch. No harvest or population equations appear.

High takes 10,000 fish; Low takes 5,000. High gets more now. What happens to the stock they both depend on?

> **3.b.harvest.** Move the actual ten and five dots into the corresponding boxes, shrinking slightly to fit. Keep the remaining five in place and change only the stock number to 5. After the fish arrive, fade in the labels “Catch: 10” and “Catch: 5” above the boxes. Pause with fish and counts visible; the graph is still empty.

> **3.b.growth.** On advance, use one 0.7-second animation to carry the pink 10 into the first graph point label while both firms’ caught dots and the teal count fade out. Then keep each of the five parents fixed and spawn a copy with 30% white fill and a dashed white edge; move each copy into a vacant position while Stock: changes from 5 to 10. Hold with newborns still visibly distinct. At the start of month 2, fill them solid white and remove their dashed edges as the month label changes. Use this same catch → counts → pause → plot-and-clear → birth → pause → maturity sequence throughout. The empty pond in High/High produces no newborns.

The stock has fallen from 20,000 to 10,000. Keeping the same strategies now means smaller catches. For instructor reference only (not displayed), in thousands of fish the rule is

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{20,2S_t\}.
$$

> **3.e.first.catch–3.e.path.** Keep both panels throughout months 2 and 3. Begin each month by turning the previous newborns solid white and removing their dashed edges. Advance the month label. Move actual catch portions from the pond in 0.6 seconds, then reveal catch labels in 0.3 seconds and pause. On advance, transfer the pink count to its graph point label and add the segment while fading both catches and the teal count in the same 0.7-second play. Then each survivor spawns one translucent, dashed-edge copy in 0.8 seconds; parents stay fixed. Use half and quarter sectors when a catch divides a thousand-fish dot, preserving area. Month 2 ends with Stock: 5; month 3 with Stock: 2.5. Pause with newborns still translucent. Keep all three plotted numeric catches until they supply the sum.

High’s catches fall from ten to five to two and a half. Low takes half as much along the same stock path.

> **3.e.total.** Keep the pond and graph. Beneath the graph, copy the three pink point values into 10 + 5 + 2.5 = 17.5. Underneath show the teal sum 5 + 2.5 + 1.25 = 8.75. Hold, then carry those sums into a stored H,L payoff pair. Remove that pair and the point numerals when the next scenario starts, retaining the curve and its direct H,L label.

Our payoff is the sum of the three catches, not the last point on the graph. High earns 17.5; Low earns 8.75.

> **3.e.low.first.catch–3.e.low.** Reset once to twenty solid fish, Month 1, and both firms Low. Keep the earlier H,L curve, dots, and direct label at 25% opacity; the new L,L curve stays at full opacity. Run three quick months: move five dots into each box, reveal counts 5 and 5, and pause. On advance, transfer the pink count into its graph label while both catches and the teal count fade together; add the next point and solid segment at five. Ten survivors stay fixed as ten translucent newborns refill the pond and Stock: returns to 20; pause. Mature the newborns when the next month begins. These are brief visual holds, without repeating the introductory explanation. At month 3, label L,L and show 15 | 15 beneath the graph.

When both choose Low, ten thousand fish survive each month and reproduce back to twenty thousand. Each firm keeps catching five thousand: fifteen thousand in total.

> **3.e.high.first.catch–3.e.high.** Reset once to twenty solid fish and Month 1, both High. Dim the completed L,L curve, dots, numeric labels and direct label to 25% opacity alongside H,L; keep the new H,H path at full opacity. In month 1 move ten dots into each box and set Stock: 0. Reveal counts 10 and 10, then pause. On advance transfer the pink 10 onto the graph while both catches and the teal count fade together; hold with the pond empty. In months 2 and 3, advance the month label and reveal “Catch: 0” above each empty box, pause, then transfer the pink zero and fade the teal zero while extending the dotted line. Hold on the completed point. End with H,H and 10 | 10 beneath the graph. No newborns or equations appear.

When both choose High, they exhaust the pond immediately. Each catches ten, then nothing. A large first catch is not the same as a large three-month payoff.

> **3.e.compare.** Fade the pond and its labels, trays, and numeric point labels. Restore all three curves, dots, and direct labels to full opacity while expanding the same axes and graph objects into the full graph layout (center −2.3, −0.2; width 7, height 3.5). Change the title to “Catch Over Time.” Put the three stored result pairs in the right-hand column beneath “Three-month totals”. Hold before transferring them to the matrix. All curves show Firm 1’s catch: solid L,L; dashed H,L; dotted H,H. Reversing the firms supplies L,H by symmetry; no fourth run is needed.

## 4 | Put the payoffs in a game and solve it

<!--
4.a · Move the graph’s result pairs directly into D1’s diamond matrix as its grid appears; reflect H,L to obtain L,H; “Firm 1's payoff first; Firm 2's payoff second.”
4.b · Hold Firm 2 Low; ask Firm 1’s best response.
4.c · Box 17.5 in pink; “High: 17.5 > 15.”
4.d · Hold Firm 2 High; ask Firm 1’s best response.
4.e · Box 10 in pink; “High: 10 > 8.75.”
4.f · Add Firm 2’s two teal best-response boxes by symmetry; “The same comparisons hold for Firm 2. Both prefer High.”
4.j · Red outline around H,H; “Neither firm gains by changing its strategy alone.”
4.k · Green outline around L,L, retain red H,H, show 15 > 10 for each firm; Gold heading “Tragedy of the commons”; white definition “Individual incentives lead to overuse of a rival, non-excludable resource: each user benefits from extra use but bears only part of its total cost.” End.
-->

> **4.a.** In one continuous 1.2-second transition, fade the graph, its subtitle, and the totals heading while the grid and labels of D1’s diamond matrix appear. Move the three payoff pairs directly from their positions beside the graph into their matrix cells. Simultaneously copy the H,L numbers, exchanging firms and colors, into L,H. Fade the three profile labels. Do not stage payoff cards above the matrix or reveal a separate empty matrix. Pause only on the complete unmarked matrix. Preserve D1 geometry, horizontal numbers, and player colors.

| Firm 1 / Firm 2 | Low | High |
| --- | --- | --- |
| Low | 15, 15 | 8.75, 17.5 |
| High | 17.5, 8.75 | 10, 10 |

> **4.b–4.e.** Two separate question/answer pairs. Shade only Firm 2’s fixed column teal and underline its choice; pause on each question before boxing Firm 1’s better payoff in pink. Keep its previous response box when switching columns.

If Firm 2 chooses Low, Firm 1 prefers 17.5 to 15. If Firm 2 chooses High, Firm 1 prefers 10 to 8.75. High is a **strictly dominant strategy**.

> **4.f.** Remove the column shading and underline. Add Firm 2’s teal response boxes together, using symmetry instead of repeating all four questions. Pause before identifying the equilibrium.

> **4.j.** Retain response boxes and outline High, High in red. Hold on the unilateral-deviation test: neither firm can improve by changing alone. This is the **Nash equilibrium**.

> **4.k.** Add the matching green outline around Low, Low, and “15 > 10 for each firm” beside the matrix. At the bottom, show “Tragedy of the commons” in gold at the standard teaching scale, followed by two white lines at scale 0.65: “Individual incentives lead to overuse of a rival, non-excludable resource:” and “each user benefits from extra use but bears only part of its total cost.” Keep 0.12 spacing and the existing bottom margin, with clearance below the diamond. Hold and finish the core explanation here.

Both would do better if both chose Low. But each prefers High given either choice by the other firm. The **tragedy of the commons** occurs when individual incentives lead to overuse of a rival, non-excludable resource: each user benefits from extra use but bears only part of its total cost. Here, a firm gets the fish it catches, while the depleted stock reduces future catches for both firms. The Nash outcome therefore leaves both worse off than restrained use.

## Optional discussion | Beyond the short lesson

Return to the question from Part C: what does the decision maker count, and what happens to everyone affected? When Firm 1 switches to High against Low, it gains 2,500 fish. Firm 2 loses 6,250. The combined catch falls by 3,750.

This is an external cost. Firm 1 bears some of the effect of reducing the stock, but it does not bear Firm 2′s loss. Knowing that cooperation would help both firms is not enough to make cooperation a best response.

An agreement can work if the rules and incentives support it. We could limit harvests, observe catches, and enforce the limits. We could also ask how communication and future dealings affect behavior. Shared use does not guarantee failure; this particular game explains why cooperation needs support.
