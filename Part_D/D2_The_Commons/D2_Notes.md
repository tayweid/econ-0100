---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
Revised 2026-10-26 for 10–20 minutes AFTER the live simulation. Target: about 15 minutes. D2_Animation.py, scene EpisodeD2. Sequence: simulation → one worked High/Low month → harvest trends → calculated 2×2 → incentives and tragedy. No repeated three-month pond runs, fractional fish, catch ledger, or separate recovery demonstrations. The earlier three-path harvest graph is restored. External-cost arithmetic and institutional discussion below are optional spoken extensions, not extra animation scenes.
Sources: D2_Planning.md; Class_On_Oct_30.pdf, pp. 1–2, dated October 30, 2024. That source plots harvest, not population. Its illustrative payoff numbers differ from the new model’s calculated totals. NPR/public goods remain in D3.
Style: shared Graphite tokens, 2:1 frame, 15 fps, azure topic title, grey context subtitle, fixed 0.7443-scale gold teaching line centered 0.05 from the bottom. Keep the existing rounded white pond and scattered white dots. Firm 1 is pink; Firm 2 is teal. Each dot is 1,000 fish. Caught dots move into trays and acquire the firm's color; surviving parents stay fixed as offspring copies move into vacant positions. Use D1’s diamond matrix and best-response boxes.
Every listed beat is a literal top-level self.pause in construct, including each graph reveal and each question/answer. No pause lives inside a loop or helper; computational loops do not play animations. The simulation has five holds; the explanation has eighteen. There is no timed auto-advance.
-->

The simulation is outside this timing budget. A suggested pace for the explanation is:

| Segment | Minutes |
| --- | --- |
| Connect the simulation to a two-firm model | 2 |
| Work one month with the pond | 3 |
| Build and compare the harvest trends | 4 |
| Transfer payoffs and solve the matrix | 5 |
| State the tragedy of the commons | 1 |

For a ten-minute version, keep the graph discussion brief and use the symmetry of the firms. For twenty minutes, allow predictions at the existing holds; do not add more pond runs.

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
1.a · D1 taxonomy with Common Resources highlighted; “What changes when we cannot exclude other users?”
3.a · Pond and twenty dots on the left; “Two Strategies:” with “- Low Catch (L): ¼ of the Stock” and “- High Catch (H): ½ of the Stock” on the right; descriptions after the colons are grey; “Maximize total catch over 3 months.”
-->

> **1.a.** Briefly reconnect to D1’s taxonomy. The fish are rival, and neither firm can exclude the other from this pond. Hold, then move directly to the model.

A fish one firm catches is unavailable to the other. The catch is private, but the stock that produces future catches is shared.

> **3.a.** Keep the rounded pond at (−4, 0.15), width 5.4, height 2.8, corner radius 0.8, with twenty scattered dots and Stock: 20 placed 0.2 below the pond. The pond and readout together share the strategy panel’s vertical center; neither panel hugs the heading. Short subtitle: “One dot = 1,000 fish.” On the right, show “Two Strategies:” at scale 0.85 above “- Low Catch (L): ¼ of the Stock” and “- High Catch (H): ½ of the Stock” at scale 0.75. Keep the heading and strategy names white; everything after each strategy’s colon is CAPTION grey. Align the three lines on the left with 0.55 spacing, centered as a group at (4, −0.15), the midpoint of the main content band. Bottom: “Maximize total catch over 3 months.” Hold. Explain the shares of starting stock, simultaneous choices, fixed strategies, reproduction rule, and payoff assumptions aloud using the paragraph below; do not display a second rules list or an assumptions caption.

Both firms calculate their catch from the same starting stock. After harvest, survivors double, up to the carrying capacity of 20,000. We count all three months’ catches, with equal value per fish, no costs, and no value assigned to the final stock. This is a small commitment game we can solve, not a biological model of tuna.

## 3 | One month, then the full trend

<!--
3.b.choices · Firm 1 High, Firm 2 Low; 1/2 × 20 = 10 and 1/4 × 20 = 5; pause before moving fish.
3.b.harvest · Move ten pink and five teal dots into their trays; 20 − 10 − 5 = 5; “Five thousand survive. How many fish next month?”
3.b.growth · Five stationary survivors produce five offspring; min{20, 2 × 5} = 10; “A smaller stock means a smaller catch next month.”
3.e.first · The worked catch of ten becomes month 1’s point; “The first catch is the first point: 10.”
3.e.path · Complete the High/Low harvest path 10 → 5 → 2.5; “High against Low: the stock halves, so the catch halves.”
3.e.total · Copy the three plotted catches into 10 + 5 + 2.5 = 17.5; show the Low firm's 5 + 2.5 + 1.25 = 8.75; “Add the three catches to get each firm's payoff.”
3.e.low · Add the Low/Low path 5 → 5 → 5 and total pair 15 | 15; “Both Low: 5 each month, 15 each in total.”
3.e.high · Add the High/High path 10 → 0 → 0 and total pair 10 | 10; “Both High: 10 now, then no fish left to catch.”
-->

> **3.b.choices.** Replace the rules with two catch trays on the right, labeled Firm 1: High and Firm 2: Low. Show each share calculation underneath. Hold before the catch.

High takes 10,000 fish; Low takes 5,000. High gets more now. What happens to the stock they both depend on?

> **3.b.harvest.** Move the actual ten and five dots into the corresponding trays, shrinking slightly to fit. Keep the remaining five in place. Copy the start and catch numbers into the subtraction below the trays. Keep the Stock: label fixed and change only its number to 5 and hold on the reproduction question.

> **3.b.growth.** Copy the survivor count into the growth calculation. Leave the five parents fixed while five newborn copies move to vacant positions. Change only the stock number from 5 to 10; the label remains Stock: in the same position. Hold. This ends the pond animation: no reset, no second or third month of fish movement, and no other strategy trials.

The stock has fallen from 20,000 to 10,000. Keeping the same fishing strategies now means smaller catches. In thousands of fish, the rule is

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{20,2S_t\}.
$$

> **3.e.first.** Fade the pond into “Catch Over Time.” Reuse the earlier graph treatment: grey axes, three labeled months, vertical ticks 0, 5, 10. Plot center (−2.3, −0.2), width 7, height 3.5. The grey subtitle identifies Firm 1’s monthly catch and the units. Carry the worked pink ten into the first point’s value label. Hold with only this point visible.

> **3.e.path.** Reveal the remaining two observations and their numeric labels together, connected with dashed pink segments. Label the endpoint H,L. Hold on the complete 10 → 5 → 2.5 path. These are monthly observations connected by straight segments, not a smooth population curve.

High takes half the stock each month, but the stock halves each month. Its catches therefore fall from ten to five to two and a half. Low takes half as much as High along the same stock path.

> **3.e.total.** Keep the graph. On the right, carry copies of the three pink point values into the sum 10 + 5 + 2.5 = 17.5. Underneath, show the teal catch sum 5 + 2.5 + 1.25 = 8.75. Hold before adding another strategy pair.

Our payoff is the sum of the three catches, not the last point on the graph. High earns 17.5; Low earns 8.75.

> **3.e.low.** Replace the sums with their stored H,L payoff pair. Add one solid pink horizontal path at five, labeled L,L, and its 15 | 15 pair in the right-hand totals column. Remove numeric point labels once they have done their job. Hold.

When both choose Low, ten fish survive each month and reproduce back to twenty. Each firm can keep catching five: fifteen in total.

> **3.e.high.** Add the dotted pink path 10 → 0 → 0, labeled H,H, and its 10 | 10 pair. Hold on all three trends and all three total pairs. Direct labels and solid/dashed/dotted strokes distinguish the scenarios; every curve remains Firm 1’s catch. Do not introduce new colors for strategy profiles.

When both choose High, they exhaust the pond immediately. Each catches ten, then nothing. A large first catch is not the same as a large three-month payoff.

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
