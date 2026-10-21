---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# D2 | Sources And Teaching Decisions

This accompanies the proposed [script and embedded storyboard](D2_Notes.md). D2 sections 1–5 are implemented in D2_Animation.py. The NPR/public-goods script and storyboard have moved to [D3](../D3_Public_Goods_and_Voting/D3_Notes.md), where animation remains unbuilt. The original notes, storyboard stub, code stub, and October 30 PDF are preserved.

## What the previous materials establish

The [October 30 notes](Class_On_Oct_30.pdf) have PDF creation metadata dated October 30, **2024**, not 2025. This identifies the file date, not independent proof that every item was taught that day. Both handwritten pages were inspected.

Page 1 moves through the tuna/common-resource game, a lake labeled “20K Fish” and “Simulation,” then the NPR/public-good contribution game. It draws Firm 1′s **harvest over time**, not population over time. The three visible paths are L,L; H,L; and H,H, with the low harvester’s L,H path also sketched. Preserve that distinction when animating stocks and catches.

The tuna scenario list unambiguously gives this matrix, with Firm 1 first:

| Firm 1 / Firm 2 | L | H |
| --- | --- | --- |
| L | 10, 10 | 2, 12 |
| H | 12, 2 | 8, 8 |

The H,H cell is overwritten in the drawing; the separate Scenario 2 lists 8 for each firm. The source identifies L,L as socially efficient and H,H as Nash. Indeed, 12 > 10 and 8 > 2; totals are 20, 14, 14, 16. The notes do not give a growth equation, precise harvest rules, payoff units, costs, discount factor, or horizon from which those numbers can be calculated. Treat them as illustrative payoffs if retaining them verbatim.

Page 1 also gives the NPR two-player matrix (20,20), (10,25), (25,10), (15,15), and the three-player formula with endowment 15 and benefit factor 2/3. Page 2 continues the zero-contribution calculation, then moves to the Dobby memorial, voting, and the possibility of charging admission. The D3 script preserves the NPR numbers exactly. D2 now covers common resources only; memorial/voting material remains for later development.

## What happened in the schedule

The [working schedule](../../_Schedule.md) mixes dated 2023 teaching notes, 2024 annotations, and later headings. Its outer class dates are not a reliable dated account of one semester.

| Evidence | What it establishes |
| --- | --- |
| Class 15, “Simulation D” and “Notes” | Jar-and-pennies fishing activity, 20,000-fish capacity, three communication/visibility treatments. “I used groups of 5” is retrospective evidence that a version was run. The year of that run is unspecified. |
| Class 15, second simulation description | An older variant uses 16,000 fish. Do not silently mix the two capacities. |
| October 16, 2023 note | Externalities reminder → taxonomy → game theory. |
| October 23, 2023 note | Market game → tuna → parks → tragedy of the commons → free rider problem. It refers to a common-resource example students had seen in recitation. |
| October 25, 2023 note | Public goods/contribution game → voting → limits of voting. |
| October 30, 2023 note | MiniExam D → three-ballot voting → Condorcet cycles → Arrow. This is not the October 30, 2024 tuna PDF. |
| Class 17–19 “Fall 2024 says” annotations | The former episode labels map to D2, D3, D4 in that sequence. |

The archived [Fall 2024 calendar](../../Syllabus/_Past/24F/Calendar_Page.pdf), page 1, schedules taxonomy/game theory for October 21/23 and public goods/public choice for October 28/30. It supports the broad order, but does not explicitly list the fishing simulation or establish which activity happened on which day. The PDF’s lake sketch supports its inclusion in the October 30 teaching material, not proof of a completed live run.

**Fall 2024 remains unconfirmed.** Taylor confirms earlier runs in smaller classes, and the groups-of-five note appears in an archive named “Simulations pre24F.” A Fall 2024 lecture plan and Google Sheet shortcut show preparation for a simulation, but the linked sheet now reports that it has been deleted. The October 30, 2024 PDF contains a simulation sketch, not recorded outcomes. See [the simulation evidence and source links](D2_Simulation.md). The dated 2023 topic notes place game theory before commons/free riding, then public goods/voting; the Fall 2024 Lecture 15 plan puts the simulation before the D1 game-theory lecture.

## Why use the capped-doubling pond first?

Use K = 20, in thousands of fish, to match the 2024 sketch and the 20-token simulation. Harvest happens first. Survivors then double, limited to K:

$$
S_t=N_t-h_{1t}-h_{2t},\qquad N_{t+1}=\min\{K,2S_t\}.
$$

This is an explicit classroom rule, not a fitted tuna model. It makes the visual cycle countable and uses the old simulation’s rule. It is **not logistic growth**. In this model a full pond can sustain a catch of K/2 per month; that result is model-specific. Below capacity, taking half the stock preserves the current stock but does not rebuild it to K. Recovery requires taking less than half until capacity is reached.

If a smoother biological extension is useful later, use post-harvest survivors in a logistic update:

$$
N_{t+1}=S_t+rS_t\left(1-\frac{S_t}{K}\right),\qquad 0<r\leq1.
$$

Here r is a per-month intrinsic growth parameter. For 0 ≤ S ≤ K and 0 < r ≤ 1 the next stock stays within [0,K]. Net reproduction is zero at 0 and K and highest at S = K/2. The familiar logistic idea is that crowding slows population growth near capacity; see [OpenStax’s population-growth discussion](https://openstax.org/books/concepts-biology/pages/19-2-population-growth-and-regulation). The timing convention and parameter restriction above are choices for this discrete classroom version. Changing to this law requires recalculating every trajectory and payoff; do not put a logistic curve behind capped-doubling arithmetic.

## A matrix actually derived from the pond

The proposed script changes the tuna payoff numbers explicitly. Let a Low firm take 1/4 of each month’s starting stock and a High firm take 1/2. Choices are simultaneous, and firms commit for three months. The initial stock is 20. Payoffs are undiscounted three-month catches, with equal value per fish, no costs, and no terminal-stock value.

| Profile | Starting stocks, months 1–3 | Firm 1 catches | Firm 2 catches | Next stock after month 3 | Payoffs |
| --- | --- | --- | --- | --- | --- |
| L,L | 20, 20, 20 | 5, 5, 5 | 5, 5, 5 | 20 | 15, 15 |
| H,L | 20, 10, 5 | 10, 5, 2.5 | 5, 2.5, 1.25 | 2.5 | 17.5, 8.75 |
| L,H | 20, 10, 5 | 5, 2.5, 1.25 | 10, 5, 2.5 | 2.5 | 8.75, 17.5 |
| H,H | 20, 0, 0 | 10, 0, 0 | 10, 0, 0 | 0 | 10, 10 |

The resulting game has the same strategic structure as the old tuna game: High strictly dominates Low, H,H is the unique Nash equilibrium, and L,L Pareto-dominates H,H and maximizes the sum among the four available profiles. The mixed profile depletes geometrically; it does not reach exactly zero in any finite month. H,H empties the pond immediately. The old sketch’s smooth paths are qualitative; the proposed chart uses discrete observations and straight connecting segments.

The three-month horizon matters. With four months, L,L gives each firm 20, while High against Low yields 18.75: High is no longer dominant. More concern for future fish, a terminal-stock value, costs, different harvest shares, or new decisions each month can change the game. Present the Nash result as a result of the specified two-strategy commitment game, not a theorem about every fishery or a solution to an unrestricted repeated game. “Socially efficient” here means highest combined payoff among these four profiles, not the solution to all possible dynamic fishing policies.

If retaining the exact 2024 tuna numbers is preferable, keep the pond to explain the mechanism, then label the old matrix “Illustrative lifetime payoffs.” Do not animate its 10/12/2/8 values as sums of the new catches. The draft chooses the calculated version because the requested teaching connection is pond math → matrix.

## Live simulation

The original rules, Fall 2024 evidence, and proposed live adaptations are collected in [D2 | Commons Simulation](D2_Simulation.md).

## Continuity with past parts

Use D1′s taxonomy, diamond matrix, player colors, one fixed-choice band at a time, persistent best-response boxes, and separate question/answer pauses. Use C1/C3′s sequence of concrete quantities → private comparison → effect on others → joint result. Use C4′s explicit editable beat directions, with exact on-screen wording. The script embeds its storyboard in section comments and quote blocks under the current style-guide convention.

Keep the economics distinction explicit: common resources are rival and difficult to exclude people from; public goods are non-rival and non-excludable. Overuse and underprovision can share a prisoner’s-dilemma structure without being the same physical problem. [OpenStax’s public-goods chapter](https://openstax.org/books/principles-economics-2e/pages/13-3-public-goods) supplies a terminology cross-check. The draft’s examples, numerical derivations, and staging are based on the local course materials and the stated new assumptions.
