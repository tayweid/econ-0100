---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# D1 Games

Public goods

This video does a simulation of public goods, and maps it into game theory, using a Lindhal equilibrium, and using voting.

Instead of rival and non-excludable, what if a good were non-rival and excludable?

Again markets don’t do well. But what if we tried another approach?

<!--
|   |   |
| --- | --- |
| Animation | D1_Animation.py, scene EpisodeD1, 86 holds: the taxonomy, the deadline simulation, the Prisoner’s Dilemma with its definitions, three Play Or Movie games, a sequential game, and two exercise cards. |
| Model | Prisoner’s Dilemma: both cooperate 3 and 3; one defects 5 and 0; both defect 1 and 1. Example 2: Play, Play 2 and 1; Movie, Movie 1 and 2; otherwise 0 and 0. Example 3: Play, Play 2 and 2; Play, Movie 1 and 0; Movie, Play 0 and 1; Movie, Movie 1 and 1. Example 4: Play, Play 1 and 0; Play, Movie 2 and 1; Movie, Play 2 and 1; Movie, Movie 1 and 1. Player 1’s payoff is first. |
| Open | There is no lecture prose of Taylor’s for D1. Every paragraph below is a marked addition by Claude, written from the animation. |
| Open | The four lines under the title are older text about public goods, kept as found. |
| Open | The deadline simulation’s details (Saturday, Sunday, 30 requests, Reattempt B) are this semester’s. |
| Archive | The single long storyboard comment this file used to hold is in _archive/2026-11-12_consolidation/D1_Notes_before_consolidation.md. |
-->

## {++ Where we are ++}

{++ So far the goods have been private: rival, and something you can keep other people from using. Parts A, B and C all lived in that one corner. Part D moves to goods that aren’t excludable, starting with common resources. ++}

<!--
|   |   |
| --- | --- |
| 0.a | Bumper: “Part D | Strategic Interaction”. |
| 1.a | The taxonomy of goods: Rival and Non-Rival across, Excludable and Non-Excludable down, with Private Goods, Club Goods, Common Resources and Public Goods in the cells. |
| 1.b | Part A, with a yellow box on Private Goods. |
| 1.c | Part B: the same box turns green. |
| 1.d | Part C: the box slides partway toward the non-excludable row and turns teal. |
| 1.e | The box moves to Common Resources and turns red. |
-->

## {++ A deadline decision ++}

{++ Before any theory, a decision for you. Recitations this week are for Reattempt B, so Vignette D1 will be recorded for you to do on your own. The usual deadline is Friday. Everyone starts with Saturday. ++}

<!--
|   |   |
| --- | --- |
| 2.a | Title “Vignette D1”; subtitle “A deadline decision”. Three lines of context about this week’s recitations and the recording. |
| 2.b | A table begins: keep the standard deadline, Saturday. “The usual deadline is Friday. Everyone starts with Saturday.” |
-->

{++ You can ask for one more day. Here’s the catch: if more than 30 of you ask, the standard deadline goes back to Friday, and the extra day is only Saturday. ++}

<!--
|   |   |
| --- | --- |
| 2.c | A second row: request one extra day, Sunday. “You can request one extra day: Sunday.” |
| 2.d | A second column, for 31 or more requests: Friday and Saturday. “With more than 30 requests, the standard deadline returns to Friday.” |
-->

{++ Raise your hand if you want the extra day. What’s best for you here depends on what everyone else does. That’s a game. ++}

<!--
|   |   |
| --- | --- |
| 2.e | “Raise your hand for one extra day; keep it raised while I count.” Hold for the count; no result is shown. |
-->

## {++ The Prisoner’s Dilemma ++}

{++ Here is the simplest version of that. Two players, and each chooses to Cooperate or Defect. ++}

<!--
|   |   |
| --- | --- |
| 3.a1 | Title “Prisoner's Dilemma”. The diamond grid and Player 1’s choices. “Player 1 can choose Cooperate or Defect.” |
| 3.a2 | “Player 2 has the same two choices.” |
-->

{++ The payoffs depend on both choices. Suppose Player 2 cooperates. If Player 1 cooperates too, each gets 3. If Player 1 defects instead, Player 1 gets 5 and Player 2 gets 0. ++}

<!--
|   |   |
| --- | --- |
| 3.a2r | What if Player 2 cooperates? Player 2’s Cooperate is shaded; no payoffs yet. |
| 3.a3q | If Player 1 also cooperates, what payoff do they receive? |
| 3.a3 | Player 1 receives 3. |
| 3.a4 | Player 2 receives 3. |
| 3.a5q | What if Player 1 defects? |
| 3.a5 | Player 1 receives 5. |
| 3.a6 | “If only Player 1 defects, Player 2 receives 0.” |
-->

{++ Now look at it from Player 2’s side. If Player 1 is defecting and Player 2 defects too, each gets 1. And if Player 2 defects while Player 1 cooperates, Player 1 gets 0 and Player 2 gets 5. ++}

<!--
|   |   |
| --- | --- |
| 3.a6q | The shading switches to Player 1’s Defect. “Now consider Player 2 switching to Defect.” |
| 3.a6r | “If Player 2 also defects, what payoff do they receive?” |
| 3.a8 | “If both defect, Player 2 receives 1.” |
| 3.a7 | Player 1 receives 1 as well. |
| 3.a7q | Back to Player 1’s side. “If Player 2 defects, consider Player 1’s choice.” |
| 3.a9q | What if Player 1 cooperates? |
| 3.a9 | Player 1 receives 0. |
| 3.a | Player 2 receives 5. The matrix is complete. |
-->

## {++ Best responses ++}

{++ What should Player 1 do? Hold Player 2’s choice fixed and compare. If Player 2 cooperates, 5 beats 3: defect. If Player 2 defects, 1 beats 0: defect. ++}

<!--
|   |   |
| --- | --- |
| 3.b | “If Player 2 cooperates, which choice gives Player 1 more?” |
| 3.c | The 5 is boxed. “Player 1's best response is Defect: $5 > 3$.” |
| 3.d | “If Player 2 defects, which choice gives Player 1 more?” |
| 3.e | The 1 is boxed. “Player 1's best response is Defect: $1 > 0$.” |
-->

{++ Defect is best for Player 1 whatever Player 2 does. A choice that is best given what the other player does is a best response. A choice that is a best response to everything is a dominant strategy. ++}

<!--
|   |   |
| --- | --- |
| 3.e1 | “Defect is best for Player 1 against either choice.” |
| 3.e2 | The game slides left, and the definition of Best Response appears beside it. |
| 3.e3 | Dominant Strategy appears below it. |
-->

{++ Player 2 faces the same numbers, so the same two comparisons give the same answer. ++}

<!--
|   |   |
| --- | --- |
| 3.f | “If Player 1 cooperates, what is Player 2's best response?” |
| 3.g | “Player 2's best response is Defect: $5 > 3$.” |
| 3.h | “If Player 1 defects, what is Player 2's best response?” |
| 3.i | “Player 2's best response is Defect: $1 > 0$.” |
-->

## {++ Nash equilibrium and efficiency ++}

{++ So both defect. At that outcome neither player can do better by switching alone. That’s a Nash equilibrium. ++}

<!--
|   |   |
| --- | --- |
| 3.j | A red box on Defect, Defect. “At (Defect, Defect), neither player gains by switching alone.” |
| 3.j1 | The game slides left, and the definition of Nash Equilibrium appears beside it. |
-->

{++ But look at mutual cooperation. Each would get 3 instead of 1. Adding the two payoffs, it gives 6, more than any other outcome: it is socially efficient. The equilibrium is not. ++}

<!--
|   |   |
| --- | --- |
| 3.k | A green box on Cooperate, Cooperate, beside the red one. |
| 3.k1 | The definition of Social Efficiency appears below Nash: the outcome that maximizes the sum of the players’ payoffs. |
-->

### {++ Whiteboard | Exercise D1 Q1 ++}

{++ > Study Room Dynamics: parts a) to e) on the handout. ++}

<!--
|   |   |
| --- | --- |
| 3.exercise | The Exercise D1 Q1 card: the questions on the left and the study room game in the lecture’s diamond on the right. Students work it here. |
-->

## {++ Three more games ++}

{++ Same method, different payoffs. Two people choose between a play and a movie. They’d like to go together, but Player 1 prefers the play and Player 2 the movie. ++}

<!--
|   |   |
| --- | --- |
| 4.a | Title “Play Or Movie”; subtitle “Example 2”. The matrix. “Payoffs: Player 1 first, Player 2 second.” |
-->

{++ Hold one player fixed and find the other’s best response, four times. ++}

<!--
|   |   |
| --- | --- |
| 4.b | “If Player 2 chooses Play, what is Player 1's best response?” |
| 4.c | “Player 1's best response is Play: $2 > 0$.” |
| 4.d | “If Player 2 chooses Movie, what is Player 1's best response?” |
| 4.e | “Player 1's best response is Movie: $1 > 0$.” |
| 4.f | “If Player 1 chooses Play, what is Player 2's best response?” |
| 4.g | “Player 2's best response is Play: $1 > 0$.” |
| 4.h | “If Player 1 chooses Movie, what is Player 2's best response?” |
| 4.i | “Player 2's best response is Movie: $2 > 0$.” |
-->

{++ Each wants to be where the other is, so there are two Nash equilibria: both at the play, or both at the movie. The method doesn’t tell us which. ++}

<!--
|   |   |
| --- | --- |
| 4.j | Red boxes on both. “Two pure-strategy Nash equilibria: both Play or both Movie.” |
-->

{++ Change the payoffs. Now both like the play together best. But if the other player goes to the movie, you get 1 whichever you choose. A tie means both choices are best responses. ++}

<!--
|   |   |
| --- | --- |
| 5.a | Subtitle “Example 3”. The new matrix. |
| 5.b | “If Player 2 chooses Play, what is Player 1's best response?” |
| 5.c | “Player 1's best response is Play: $2 > 0$.” |
| 5.d | “If Player 2 chooses Movie, what is Player 1's best response?” |
| 5.e | Two boxes. “Player 1 receives 1 either way: both choices are best responses.” |
| 5.f | “If Player 1 chooses Play, what is Player 2's best response?” |
| 5.g | “Player 2's best response is Play: $2 > 0$.” |
| 5.h | “If Player 1 chooses Movie, what is Player 2's best response?” |
| 5.i | Two boxes. “Player 2 receives 1 either way: both choices are best responses.” |
-->

{++ Again two equilibria. This time they aren’t equally good: both at the play is efficient, and both at the movie is not. ++}

<!--
|   |   |
| --- | --- |
| 5.j | “Both Play and both Movie are Nash equilibria.” |
| 5.k | A dashed green box on Play, Play. “Both Play is socially efficient; both Movie is not.” |
-->

{++ One more. Here Player 1 would rather be at a different activity from Player 2. ++}

<!--
|   |   |
| --- | --- |
| 6.a | Subtitle “Example 4”. The new matrix. |
| 6.b | “If Player 2 chooses Play, what is Player 1's best response?” |
| 6.c | “Player 1's best response is Movie: $2 > 1$.” |
| 6.d | “If Player 2 chooses Movie, what is Player 1's best response?” |
| 6.e | “Player 1's best response is Play: $2 > 1$.” |
| 6.f | “If Player 1 chooses Play, what is Player 2's best response?” |
| 6.g | “Player 2's best response is Movie: $1 > 0$.” |
| 6.h | “If Player 1 chooses Movie, what is Player 2's best response?” |
| 6.i | Two boxes. “Player 2 receives 1 either way: both choices are best responses.” |
| 6.j | “Two pure-strategy Nash equilibria: different activities.” |
-->

## {++ Moving first ++}

{++ Back to Example 2, where we couldn’t say which equilibrium would happen. What if Player 1 chooses first, and Player 2 sees the choice? ++}

<!--
|   |   |
| --- | --- |
| 7.a | Subtitle “Example 2 again. Now Player 1 chooses first, and Player 2 sees the choice.” The matrix with its two Nash boxes. “At the same time: two Nash equilibria, and no way to say which.” |
| 7.b | A game tree beside it: Player 1, then Player 2, then four payoff pairs. “One at a time: Player 1 chooses, then Player 2 chooses knowing it.” |
-->

{++ Solve it backward. If Player 1 chose Play, Player 2 picks Play, 1 over 0. If Player 1 chose Movie, Player 2 picks Movie, 2 over 0. Knowing that, Player 1 compares 2 with 1 and chooses Play. ++}

<!--
|   |   |
| --- | --- |
| 7.c | “If Player 1 chose Play, what does Player 2 do?” |
| 7.d | “Player 2 plays Play: $1 > 0$.” |
| 7.e | “If Player 1 chose Movie, what does Player 2 do?” |
| 7.f | “Player 2 plays Movie: $2 > 0$.” |
| 7.g | “Player 1 works backward: Play leads to 2, Movie to 1. Play.” |
-->

{++ Moving first picks out one of the two equilibria: the first mover’s favorite. In the Prisoner’s Dilemma the order wouldn’t matter, because Defect is best either way. ++}

<!--
|   |   |
| --- | --- |
| 7.h | A red box on the Play, Play leaf; the other Nash box fades. “Moving first selects an equilibrium: the first mover’s favorite.” |
| 7.i | “In the Prisoner’s Dilemma the order would not matter: Defect is best either way.” |
| 7.j | “Sequential Game”: one player moves first and the other sees the choice; solve it backward. |
-->

### {++ Whiteboard | Exercise D1 Q2 ++}

{++ > Date Night: build the matrix from the setup in the exercise file, parts a) to c). ++}

<!--
|   |   |
| --- | --- |
| 7.exercise | The Exercise D1 Q2 card: the questions on the left and an empty diamond for Hagrid and McGonagall on the right. Students build the matrix. The animation ends here. |
-->
