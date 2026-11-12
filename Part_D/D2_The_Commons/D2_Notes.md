---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
|   |   |
| --- | --- |
| Animation | D2_Animation.py, scene EpisodeD2, 41 holds: five for the simulation rules, thirty-six for the explanation. It plays after the live simulation. |
| Model | Two firms share a pond of 20,000 fish for three months. Low takes ¼ of the starting stock and High takes ½; survivors double, up to 20,000. Three-month totals in thousands: both Low 15 and 15; High against Low 17.5 and 8.75; both High 10 and 10. |
| Open | The simulation is five firms over four rounds; the model is two firms over three months. Simulation rules and teaching notes are in D2_Simulation.md. |
| Open | The payoffs are calculated from the model and differ from the illustrative numbers in the October 30, 2024 handwritten notes (../D_Class_On_Oct_30_Dobby_plus_Tuna.pdf). |
| Marked | Everything inside addition marks is Claude’s: three short paragraphs where holds had no prose. |
| Archive | The earlier notes, planning document, stubs and the direction blocks that used to sit in this file are in _archive/2026-11-12_consolidation/. |
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
|   |   |
| --- | --- |
| sim.a | Title “Part D | Common Resources Simulation”. “Rules”, then “- One lake, five firms”. |
| sim.b | “- Each round, choose your harvest” |
| sim.c | “- Fish population doubles each round” |
| sim.d | “- Carrying capacity is 20,000 fish” |
| sim.e | “- Maximize harvest after 4 rounds”. Hold the full card for the live simulation. |
-->

## 1 | From the simulation to the model

A fish one firm catches is unavailable to the other. The catch is private, but the stock that produces future catches is shared.

<!--
|   |   |
| --- | --- |
| 1.a | D1’s taxonomy with Common Resources highlighted. Subtitle: “Goods that are rival and non-excludable.” |
-->

Both firms calculate their catch from the same starting stock. After harvest, survivors double, up to the carrying capacity of 20,000. We count all three months’ catches, with equal value per fish, no costs, and no value assigned to the final stock. This is a small commitment game we can solve, not a biological model of tuna.

<!--
|   |   |
| --- | --- |
| 3.a | The pond with twenty dots, each 1,000 fish, and the two strategies: Low Catch, ¼ of the stock; High Catch, ½ of the stock. “Maximize total catch over 3 months.” |
-->

## 3 | Build all three paths beside the pond

High takes 10,000 fish; Low takes 5,000. High gets more now. What happens to the stock they both depend on?

<!--
|   |   |
| --- | --- |
| 3.b.choices | Month 1. The pond and two firm boxes on the left; an empty graph of Firm 1’s catch on the right. |
| 3.b.harvest | High against Low: ten fish move to Firm 1’s box and five to Firm 2’s. Stock: 5. |
| 3.b.plot | Firm 1’s 10 moves onto the graph as the catches clear. |
| 3.b.growth | Month 2: the five survivors spawn five newborns. Stock: 10. |
-->

The stock has fallen from 20,000 to 10,000. Keeping the same strategies now means smaller catches. For instructor reference only (not displayed), in thousands of fish the rule is

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{20,2S_t\}.
$$

<!--
|   |   |
| --- | --- |
| 3.e.first.catch | Month 2, same strategies: catches 5 and 2.5. Stock: 2.5. |
| 3.e.first.plot | The 5 joins the graph. |
| 3.e.first | Month 3: spawning. Stock: 5. “Less stock, smaller catches.” |
-->

High’s catches fall from ten to five to two and a half. Low takes half as much along the same stock path.

<!--
|   |   |
| --- | --- |
| 3.e.path.catch | Month 3: catches 2.5 and 1.25. Stock: 1.25. |
| 3.e.path.plot | The 2.5 completes the dashed path, and its totals appear beside it: H,L 17.5 and 8.75. |
-->

The completed line now displays its final payoff pair: 17.5 | 8.75. Keep it attached to the H,L endpoint when starting L,L; no sum equations or additional sum pause appear beneath the graph.

Our payoff is the sum of the three catches, not the last point on the graph. High earns 17.5; Low earns 8.75.

<!--
|   |   |
| --- | --- |
| 3.e.path | Closing stock 2.5. “High against Low: the stock halves, so the catch halves.” |
-->

When both choose Low, ten thousand fish survive each month and reproduce back to twenty thousand. Each firm keeps catching five thousand: fifteen thousand in total.

<!--
|   |   |
| --- | --- |
| 3.e.low.first.catch | Reset to 20, both Low: catches 5 and 5. Stock: 10. |
| 3.e.low.first.plot | The 5 joins the graph. |
| 3.e.low.first | Spawning restores the stock. “Both Low: the stock returns to 20.” |
| 3.e.low.second.catch | Month 2: 5 and 5 again. |
| 3.e.low.second.plot | The line extends at 5. |
| 3.e.low.second | “The same catch, again.” |
| 3.e.low.catch | Month 3: 5 and 5. |
| 3.e.low.plot | The solid line is complete; totals L,L 15 and 15. |
| 3.e.low | “Both Low: 5 each month, 15 each in total.” |
-->

When both choose High, they exhaust the pond immediately. Each catches ten, then nothing. A large first catch is not the same as a large three-month payoff.

<!--
|   |   |
| --- | --- |
| 3.e.high.first.catch | Reset to 20, both High: catches 10 and 10. Stock: 0. |
| 3.e.high.first | The 10 joins the graph. “Both High: nothing left to reproduce.” |
| 3.e.high.second.catch | Month 2: an empty pond, and a catch of 0 for each. |
| 3.e.high.second | “No stock, no catch.” |
| 3.e.high.catch | Month 3: still empty. |
| 3.e.high | The dotted line is complete, 10 then 0 then 0; totals H,H 10 and 10. “Both High: 10 now, then no fish left to catch.” |
-->

{++ Here are all three paths together, each with its three-month total. We only ran Firm 1’s side; swapping the firms gives the fourth case. ++}

<!--
|   |   |
| --- | --- |
| 3.e.compare | The pond leaves and the graph expands; title “Catch Over Time”. All three paths with their totals. “Three paths, three payoff pairs.” |
-->

## 4 | Put the payoffs in a game and solve it

{++ Those totals are the payoffs of a game. Put them in a matrix, Firm 1’s payoff first. ++}

| Firm 1 / Firm 2 | Low | High |
| --- | --- | --- |
| Low | 15, 15 | 8.75, 17.5 |
| High | 17.5, 8.75 | 10, 10 |

<!--
|   |   |
| --- | --- |
| 4.a | The graph shrinks to the left; D1’s diamond matrix appears on the right and the totals move into its cells, with High against Low mirrored to fill the fourth. “Firm 1's payoff first; Firm 2's payoff second.” |
-->

If Firm 2 chooses Low, Firm 1 prefers 17.5 to 15. If Firm 2 chooses High, Firm 1 prefers 10 to 8.75. High is a **strictly dominant strategy**.

<!--
|   |   |
| --- | --- |
| 4.b | Firm 2 held at Low: what is Firm 1’s best response? |
| 4.c | 17.5 is boxed. “High: 17.5 > 15.” |
| 4.d | Firm 2 held at High: what is Firm 1’s best response? |
| 4.e | 10 is boxed. “High: 10 > 8.75.” |
-->

{++ The same holds for Firm 2. With both choosing High, neither can do better by changing alone: that’s the Nash equilibrium. ++}

<!--
|   |   |
| --- | --- |
| 4.f | Firm 2’s two boxes, by symmetry. “The same comparisons hold for Firm 2. Both prefer High.” |
| 4.j | A red outline on High, High. “Neither firm gains by changing its strategy alone.” |
-->

Both would do better if both chose Low. But each prefers High given either choice by the other firm. The **tragedy of the commons** occurs when individual incentives lead to overuse of a rival, non-excludable resource: each user benefits from extra use but bears only part of its total cost. Here, a firm gets the fish it catches, while the depleted stock reduces future catches for both firms. The Nash outcome therefore leaves both worse off than restrained use.

<!--
|   |   |
| --- | --- |
| 4.k | A green outline on Low, Low, with “15 > 10 for each firm”. “Tragedy of the commons” in gold, with its definition. The animation ends here. |
-->

## Optional discussion | Beyond the short lesson

Return to the question from Part C: what does the decision maker count, and what happens to everyone affected? When Firm 1 switches to High against Low, it gains 2,500 fish. Firm 2 loses 6,250. The combined catch falls by 3,750.

This is an external cost. Firm 1 bears some of the effect of reducing the stock, but it does not bear Firm 2′s loss. Knowing that cooperation would help both firms is not enough to make cooperation a best response.

An agreement can work if the rules and incentives support it. We could limit harvests, observe catches, and enforce the limits. We could also ask how communication and future dealings affect behavior. Shared use does not guarantee failure; this particular game explains why cooperation needs support.
