---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# D2 | Commons Simulation

Collected simulation rules and teaching notes. The original material below is preserved from the working schedule; archived notebooks and slides remain in place. The final section contains proposed adaptations from the October 20, 2026 planning pass, not records of what happened in an earlier class.

## Did this run in Fall 2024?

**Not yet established.** Taylor confirms that he ran the simulation earlier in smaller classes. The groups-of-five teaching note also appears in the archive named [Simulations pre24F](../../../ECON_0100/Simulations/Simulations%20pre24F.ipynb), markdown cell 6 (zero-based). It is therefore not independent evidence of a Fall 2024 run.

There are specific Fall 2024 leads:

- The [Fall 2024 Lecture 15 plan](../../../ECON_0100/_Past_Future/24F/F24_Lectures/Lecture%2015%20\(D0\).md) lists “MiniExam C” followed by “Simulating The Commons.” It also includes explicitly dated 2023 notes and the older simulation text, so this establishes a plan filed with the 2024 materials, not a completed activity.
- The archive contains a [Simulation D | Common Resources Google Sheet shortcut](../../../ECON_0100/Simulations/24F/Simulation%20D%20%7C%20Common%20Resources.gsheet). Its [linked Google Sheet](https://docs.google.com/spreadsheets/d/1UxFLN_uNZGq9lLYmhLwDEji26Y_9Jfpj2zYR1uXUU40/edit) was checked on October 20, 2026; Google reported that the file had been deleted. No results or revision history could be inspected. The shortcut itself contains a document ID, not simulation data.
- The [October 30 handwritten notes](Class_On_Oct_30.pdf), with creation metadata dated October 30, 2024, include a lake labeled “20K Fish” and “Simulation.” This is evidence of simulation material in the dated notes, but not a record of students’ choices or a completed run.
- The [Fall 2024 calendar](../../Syllabus/_Past/24F/Calendar_Page.pdf) places taxonomy/game theory on October 21/23 and public goods/public choice on October 28/30. It does not name the commons simulation.

The remaining question is whether the planned Fall 2024 activity actually happened. A dated result sheet, recording, announcement describing a completed activity, or contemporaneous reflection would resolve it. The old small-class experience should remain separate from that question.

## Original schedule material

Moved from [the working schedule](../../_Schedule.md), Class 15. The source headings and wording below are preserved, including the two capacity variants. The original 20,000-fish heading says “Public Goods,” although the rival fish make this a common-resource simulation. The introductory “no private component” claim is also historical wording: the catch has a private benefit, while harvesting affects others.

### Simulation D | Public Goods

this is the one where students have to pull from the pond and there are various treatments with different visibilities

Let’s play a little game. So far in this class we’ve focused on Private Goods: goods that are rival (meaning my using them makes less available for you) but also excludable (meaning I can keep my goods away from you).

We talked about externalities, which were goods with some non-excludability: either 1) you couldn’t stop me from benefiting from your good, or 2) I couldn’t stop you from benefiting from mine. This was the externality.

Today we’re going to take this idea to the limit, by looking at goods which have no private component, which carry only externalities: Common Resources.

Here’s the game. You operate a small scale fishing operation with a few of your friends. The lake you fish on is big but has a finite space with a finite population of fish: Ramora, which is a magical fish native to the Indian Ocean but also is able to survive some fresh water lakes. Some facts about fishing the lake:

1. Every month the fish spawn, doubling in population.
2. Every month you operate your fishing operation, you have to pay for equipment maintenance: your monthly costs, equal to the revenue from 1000 fish. So to continue to operate, you need to catch at least one.
3. There isn’t much information about the number of fish in the lake.
4. The carrying capacity of the lake for fish is 20000 fish.

The lake is this jar. In the jar are pennies, each representing 1000 fish.

Mention Elinor Ostrom at some point.

Do three rounds:

1. No communication, no visibility
2. Communication, no visibility
3. Communication, visibility

### Notes

I used groups of 5, which was too small to demonstrate tragedy of the commons for many classes.

### Simulation | Common Resources and Game Theory

Let’s play a little game. So far in this class we’ve focused on Private Goods: goods that are rival (meaning my using them makes less available for you) but also excludable (meaning I can keep my goods away from you).

We talked about externalities, which were goods with some non-excludability: either 1) you couldn’t stop me from benefiting from your good, or 2) I couldn’t stop you from benefiting from mine. This was the externality.

Today we’re going to take this idea to the limit, by looking at goods which have no private component, which carry only externalities: Common Resources.

Here’s the game. You operate a small scale fishing operation with a few of your friends. The lake you fish on is big but has a finite space with a finite population of fish: Ramora, which is a magical fish native to the Indian Ocean but also is able to survive some fresh water lakes. Some facts about fishing the lake:

1. Every month the fish spawn, doubling in population.
2. Every month you operate your fishing operation, you have to pay for equipment maintenance: your monthly costs, equal to the revenue from 1000 fish. So to continue to operate, you need to catch at least one.
3. There isn’t much information about the number of fish in the lake.
4. The carrying capacity of the lake for fish is 16000 fish.

The lake is this jar. In the jar are pennies, each representing 1000 fish.

Mention Elenor Ostrom at some point.

## Rules shown in the old D0 animation

Source: [D0 animation](../D0_Strategic_Interaction/03_Code.py), the Common Resources Simulation rules card. Its on-screen rules are:

- One lake, five firms
- Each round, choose your harvest
- Fish population doubles each round
- Carrying capacity is 20,000 fish
- Maximize harvest after 4 rounds

The slide specifies four harvest rounds. The schedule’s “Do three rounds” lists three communication/visibility conditions. These may be different levels of the activity, but the sources do not explicitly say whether there were four harvest rounds within each condition. Keep the distinction visible rather than silently resolving it.

## Other copies and unresolved mechanics

The 16,000-fish version is also in [Week 08, 23S](_archive/Week_08_23S.ipynb), [Week 08, 23F](_archive/Week_08_23F.ipynb), and the corresponding [D3 archived notebook](../D3_Public_Goods_and_Voting/_archive/Week_08.ipynb). The relevant prose formerly in [\_Unplaced.md](_Unplaced.md) is now represented by the 16,000-fish version above. The separate course archive also retains [Simulations 23S](../../../ECON_0100/Simulations/Simulations%2023S.ipynb) and [Simulations](../../../ECON_0100/Simulations/Simulations.ipynb).

The original text establishes the jar, pennies, fish units, doubling rule, maintenance cost, capacity variants, visibility treatments, the Ostrom reminder, and the small-group experience. It does not fully specify initial stock, simultaneous versus sequential withdrawals, oversubscribed requests, what “visibility” reveals, treatment resets, or how costs affect continuation. The cost is revenue from 1,000 fish, equivalent to one penny in the stated units; the original “catch at least one” should be clarified when presenting the rules.

The old slides maximize harvest over four rounds; the new two-firm animation scores three months and omits costs. These are different games. The following adaptations were proposed in 2026 and should not be used to infer what happened in 2024.

## Proposed adaptations from the 2026 draft

### Optional live simulation, before revealing the matrix

The old simulation uses pennies representing 1,000 fish, costs equivalent to one penny per participant per month, and three treatments: no communication/no visibility; communication/no visibility; communication/visibility. The schedule labels one version “Public Goods,” but rival fish make this a common-resource activity. Its claim that commons have “no private component” should not be repeated: the catch provides a private benefit while extraction affects others.

For a first use with the new animation, a short **two-firm prediction game** fits better than adding a second set of mechanics. Pause after beat 3.a, before showing the outcomes. Split the room into pairs of teams. Each team privately commits to L or H for three months. Collect both choices before revealing either; run the chosen path, tally the catch, then compare with the unchosen profiles. This uses precisely the script’s model. The outcome is evidence for discussion, not a requirement that students must choose H,H.

To revisit the original open-harvest simulation instead, reserve 12–15 minutes and state that its strategy space differs from the two-firm matrix. Use teams of six as a tentative adjustment to the old groups-of-five note, with 20 tokens per pond. In each month participants submit integer requests from 0 to 20 privately and simultaneously. If total requests exceed stock, allocate remaining tokens by a publicly stated random draw among requested units, without replacement; never allow negative stock. Charge one token-equivalent operating cost per participant per month in the score, including a zero-catch month. One actual token covers this cost; it is not 1,000 tokens. Reproduce only after all catches, doubling remaining tokens to a maximum of 20.

Use three treatments of three months each, resetting to 20 and resetting scores each time: no communication/private catches; communication/private catches; communication/public catches. Private-stock rounds use a covered jar and a facilitator who privately updates stock; public rounds reveal both stock and catches. Log initial stock, aggregate actual catch, survivors, next stock, and scores. Fixed treatment order also introduces learning, so do not interpret differences as a clean causal estimate of communication or visibility. Let the results be what they are: cooperation is a useful outcome too. Debrief who benefits from restraint, who can observe deviations, and what rules participants would choose.
