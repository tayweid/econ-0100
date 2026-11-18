---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Oligopoly | Episode E4

*When sellers play games with each other*

*The game theory of thin markets*

| Minutes | Animation or board work | Purpose |
| --- | --- | --- |
| Warmup | Exercise E4 Warmup on the board | Retrieve the monopolist’s problem on today’s market. |
| 0–5 | Bumper (`0.a`), then `1.a.last` and `1.a` | From one seller to a few. |
| 5–10 | Play `1.b` through `1.l` | The two-by-two game: Low 20 or High 24, best responses, both High. |
| 5–10 | Play `2.a` through `3.d` | The firm’s problem; the monopoly answer to the warmup. |
| 10–16 | Resume through `4.b` | A second seller: price and marginal revenue depend on the other firm. |
| 16–20 | Hide projection; Q1 on board | Choose firm A’s quantity for a given quantity from firm B. |
| 20–29 | Resume through `5.c` | The best-response rule, its graph, and firm B’s by symmetry. |
| 29–33 | Hide projection; Q2 on board | Use a best response; test whether a pair is an equilibrium. |
| 33–42 | Resume through `6.c` | Nash equilibrium, then the price beside the monopoly’s. |
| 42–47 | Hide projection; Q3 on board | Is the duopoly outcome efficient? |
| 47–50 | Resume to `7.a` | The cartel (`6.d.rule` to `6.e`), where the matrix’s 20 comes from; preview more sellers. |

{++ This table is a proposal. It has not been timed against a run-through. ++}

<!--
|   |   |
| --- | --- |
| Model | Demand P = 120 − Q; every firm MC = 2q. Monopoly: 30 units at 90. BR_A: q_A = 30 − ¼q_B. Nash: 24 each, Q = 48, P\* = 72. |
| Matrix | 1.b to 1.l, added 2026-11-18, in D1’s diamond layout. Low = 20 is each firm’s share of the 40 units a cartel would make; High = 24 is the Nash quantity. Profits use TC = 1000 + q²: 200 each at Low, 152 each at High, 248 and 120 when one goes High. |
| Open | The matrix section has no minutes of its own yet: the rows after it in the timing table have not been moved. |
| Matrix | Both matrix quantities are derived later: the 24 at 6.b, the 20 in the cartel holds 6.d.rule to 6.e (added 2026-11-18). |
| Open | The cartel’s 40 units is also E3’s efficient quantity for one firm, by coincidence of the numbers; and the cartel (40 at 80) is not E3’s monopoly (30 at 90), because two firms split the output. |
| Open | Taylor’s prose stops at “best response”. From the monopoly recap on, the paragraphs are Claude’s marked additions. |
| Open | Paragraphs three and four have sellers setting prices; on screen they choose quantities. |
| Open | The numbers no longer match the handwritten sheet, which still supplies the steps. |
| Open | The title says Oligopoly; the folder and the animation say Duopoly. Only the first thesis line is on the bumper. |
| Open | No opener or exercise cards: the warmup and Q1 to Q3 exist only here. The timing table is untested. |
| Marked | Everything inside addition marks is Claude’s: the warmup, Q1 to Q3, and the paragraphs for the holds Taylor’s prose does not reach. |

| Past notes | Taylor’s older oligopoly notes are placed at the top of the Oligopoly section, unmarked: the November 15, 2023 outline, the Week 12 introduction, and the older opening on cartels, the high and low quantity game, the advertising game and repeated games. None of that older material is in the animation. |
| Archive | Earlier notes, stubs and the sheet-market build are in _archive/2026-11-11_consolidation/. |
-->

## {++ Exercise E4 | Warmup ++}

{++ One seller faces demand $P = 120 - Q$, so $MR = 120 - 2Q$. Marginal cost is $MC = 2q$. ++}

{++ a\) What quantity does the monopolist choose? ++}

{++ b\) What price does it charge? ++}

<!--
|   |   |
| --- | --- |
| Warmup | Board only; this is E3’s problem, and 3.c and 3.d work it again. Answers: a) 2q = 120 − 2q, so q = 30; b) P = 120 − 30 = 90. |
-->

## Oligopoly

{++ From the November 15, 2023 class notes: ++}

- Monopoly Refresh
- Monopoly to Duopoly
- Solving the Duopolist’s Problem
- Implications

{++ From the Week 12 introduction in the 2022 and 2023 notebooks: ++}

On Thursday we'll introduce the Oligopoly market structure (ch. 17). The markets we've explored to this point have either had one or many sellers. What happens when there are a few firms? Similar to our model of Common Resources, firms in Oligopoly must consider strategic interaction between their market decisions. So to model Oligopolistic firms we need to turn back to Game Theory. Much of what we'll do here will remind you of Common Resources.

{++ The older oligopoly notes, from _Schedule.md and the same notebooks: ++}

We’ve just finished dealing with Monopoly markets, where there is one firm. These are pretty rare, outside the few cases of Natural Monopolies like Comcast, where there are very high barriers to entry. Its very uncommon for markets to have one seller, but it’s much more likely that markets have few sellers.

And in a way, oligopoly is the most general form of market model.

The limited set of competitors in the market can behave in two general types of ways: Cooperatively and Non-Cooperatively. If they cooperate, they are forming what we call a ‘Cartel’. The most famous example is OPEC (Organization of Petroleum Exporting Countries). And if you can get all the competitors to cooperate, you can essentially operate like a monopoly.

But as we’ll see, it’s pretty difficult to get competitors to cooperate, difficult to sustain the cartel.

So we can think about competitive markets on one extreme and Monopoly on the other, Oligopoly lives somewhere in between. And part of the story is about where in between we end up.

And you’ve maybe already noticed there is strategic interaction between competitors.

And we can see it with Demand. If my competitor is producing very little, I can produce a lot, move the price down and make a bunch of revenue. But this is bad for them, since the price goes down.

We’ll talk about how we use the demand curve with this type of problem, but before we do, lets look at a simpler model. Instead of choosing any quantity, we’ll just think about a high and low quantity. And we’ll abstract away from the details of costs and revenue and construct a profit matrix.

If I choose a high

{++ Same market as last time, with two firms in it. Each one makes either 20 units or 24. If we both make 20, the price is 80 and we each earn 200. If we both make 24, the price is 72 and we each earn 152. If only one of us makes 24, that firm earns 248 and the other earns 120. ++}

<!--
|   |   |
| --- | --- |
| 1.b | Title Two Sellers; the market and cost in the subtitle. The empty diamond matrix: firm A and firm B, Low: 20 and High: 24. |
| 1.c | One cell worked from the market: both Low, price 80, profit 200 each. |
| 1.d | The other three cells fill in. |
-->

{++ Now it’s Part D again. Hold firm B at Low: I’d rather make 24, since 248 beats 200. Hold firm B at High: I’d still rather make 24, since 152 beats 120. Firm B is the same firm, so it reasons the same way. ++}

<!--
|   |   |
| --- | --- |
| 1.e, 1.f | Firm B at Low: the question, then firm A’s best response boxed. |
| 1.g, 1.h | Firm B at High: the question, then the answer. |
| 1.i | Firm B’s two best responses, by symmetry. |
-->

{++ So both choose High, and that’s the Nash equilibrium. Both would earn more at Low, but neither would stay there. Where do 20 and 24 come from? That’s the rest of today: let each firm choose any quantity. ++}

<!--
|   |   |
| --- | --- |
| 1.j | Red box on both High: the Nash equilibrium, 152 each. |
| 1.k | Green box on both Low: 200 each, and each firm would switch. |
| 1.l | The bridge: “Where do 20 and 24 come from? Let each firm choose any quantity.” |
-->

Advertising Game

Repeated Game with one player playing Grimm in infinitely repeated. This doesn’t work if there’s a known last period.

Terms:

- Residual Demand
- Response Function
- Nash Equilibrium

While markets can be great at organizing production and exchange, we’ve just shown that markets can start to break down when sellers have some influence on prices. We showed that competitive firms cannot benefit by moving their prices from market equilibrium prices, but that firms that do not have competitors actually can.

But neither the competitive seller nor the monopolist are all that common in our world. Most exchanges we make are with sellers who have some but not much influence on their prices.

<!--
|   |   |
| --- | --- |
| 0.a | Bumper with “When sellers play games with each other”. |
| 1.a.last | Title Monopoly; subtitle “One seller, many buyers.” The market-structures grid, with the red box on Monopoly. |
-->

One type of situation like this, where the seller has some but not complete market power, is what we call oligopoly. A seller cannot charge a price too high because buyers will simply switch to the seller down the road. They also don’t want to sell too low, because even though they would bring in buyers from their competitor down the road, they also don’t want to miss out on selling at nice high prices.

But each seller in this environment is thinking this way. And each seller knows the other sellers are thinking this way. If the seller down the road sets a high price, then I should set a high price. And if they set a low price, I better not set a high price, or they will undercut me.

This type of strategic interaction we call oligopoly, where there are a few sellers with some but not complete control of the price responding to the prices of other sellers nearby.

<!--
|   |   |
| --- | --- |
| 1.a | The box moves to Oligopoly; title Oligopoly. “Oligopoly: a few sellers with some but not complete control of the price.” |
-->

## The Firm’s Problem and Monopoly

To get a handle on … lets set up the profits for the oligopolist. Like in every environment for the seller, we want to try to get a sense of the firm’s marginal costs and their marginal revenue. Their MC is similar to what we’ve done before. Since costs come from the production function and not the structure of the market, there’s nothing fundamentally different with the MC because we’re in a different environment.

<!--
|   |   |
| --- | --- |
| 2.a | Title The Firm’s Problem. The five-step card, one row per fade. |
| 3.a | Title Monopoly; subtitle “All firms are similar.” The market graph with D and MC; rows D: P = 120 − Q and MC = 2q. “Costs come from the production function, not the structure of the market.” |
-->

{++ Let’s warm up on the case we already know. With one seller, the firm’s demand is the whole market’s demand, so its marginal revenue starts at the same place and falls twice as fast. ++}

<!--
|   |   |
| --- | --- |
| 3.b | MR_A, from 120 down to 60 units; row MR_A = 120 − 2q_A. |
-->

{++ Step one: set marginal cost equal to marginal revenue. That gives 30 units. Step two: take that quantity up to the demand curve to find the price, 90. That’s the monopoly from last time. ++}

<!--
|   |   |
| --- | --- |
| 3.c | A red dot where MR_A meets MC. 2q_A = 120 − 2q_A; 4q_A = 120; q_A = 30 = q\*. “1. MC = MR → q\*” |
| 3.d | Up to demand at (30, 90). P\* = 120 − 30 = 90. “2. q\* → D → P\*” |
-->

## Duopoly

Since revenue is the product of price and quantity, however, it is very different in this environment. As always, prices are set by the demand curve and everyone can see the price. So as a seller, like both the monopolist and the competitive firm, you as the oligopolist will choose to set prices so that nothing you make goes unsold. But unlike the monopolist, you’re not the only seller. So the quantity that’s sold to buyers isn’t just what you make, but also includes what the other seller makes. Both of you are trying to sell into the same market. So if the other seller lowers their price, everyone will go to them until you lower your price as well. So just like in competitive markets, you don’t have any reason to switch prices from the price that sells everything for everyone.

<!--
|   |   |
| --- | --- |
| 4.a | Title Duopoly. The price marks fade; rows Q = q_A + q_B and P = 120 − (q_A + q_B). “Both of you are trying to sell into the same market.” |
-->

But because the *price* depends on how much the other firm sells, your *revenue* depends on how much the other firm sells, which means your *marginal revenue* *also* depends on how much the other firm sells.

<!--
|   |   |
| --- | --- |
| 4.b.zero | The graph becomes firm A’s (q_A, D_A, q_A\*), with a grey copy of market demand behind it; rows MR_A = 120 − 2q_A − q_B and q_B = 0. “The price depends on how much the other firm sells.” |
| 4.b.twenty_four | q_B rolls from 0 to 24: D_A and MR_A slide down (intercept 120 → 96) and q_A\* goes 30 → 24. “Your marginal revenue also depends on how much the other firm sells.” |
| 4.b | q_B rolls to 48: intercept 72, q_A\* 18. “The more the other firm sells, the less you want to sell.” |
-->

### {++ Whiteboard | Exercise Q1 ++}

{++ > Firm B sells 40 units, so firm A’s marginal revenue is $MR_A = 80 - 2q_A$. What quantity does firm A choose? ++}

<!--
|   |   |
| --- | --- |
| Q1 | Board only. Answer: 80 − 2q_A = 2q_A, so q_A = 20, which is 30 − ¼ · 40. |
-->

## Best Responses

When our payoff is liked with the decisions of others like this, we call this strategic interaction, which is the domain of game theory.

What we want to do is find a way to decide our best response to every decision the other seller might make.

<!--
|   |   |
| --- | --- |
| 5.a.rule | q_B rolls back to 0. Title Best Responses; subtitle “The strategies are quantities.” Row MR_A = MC_A. “Decide our best response to every decision the other seller might make.” |
-->

{++ Set firm A’s marginal revenue equal to its marginal cost, but leave firm B’s quantity as a letter. Solving for q_A gives a rule: for any quantity firm B might choose, here is firm A’s best quantity. We call that rule firm A’s best response. ++}

<!--
|   |   |
| --- | --- |
| 5.a.substitute | 120 − 2q_A − q_B = 2q_A. |
| 5.a.simplify | 120 − q_B = 4q_A. |
| 5.a | BR_A: q_A = 30 − ¼q_B. |
-->

{++ A rule like this is easier to see as a picture. Put firm A’s quantity across and firm B’s up. If B sells nothing, A acts like a monopolist and sells 30. As B sells more, A’s best quantity shrinks, until at 120 A wouldn’t sell anything at all. ++}

<!--
|   |   |
| --- | --- |
| 5.b.trace | The algebra gives way to a best-response graph, q_A across and q_B up. One sweep takes q_B from 0 to 120: firm A’s demand and MR shrink to nothing on the market graph while a point traces BR_A from (30, 0) to (0, 120). |
-->

{++ That line is firm A’s best response: the strategy that gives A the highest payoff, given what B is doing. It’s the same idea as in Part D, with quantities as the strategies. ++}

<!--
|   |   |
| --- | --- |
| 5.b | The market graph fades and the best-response graph slides left, beside D1’s Best Response definition. |
-->

{++ Firm B has the same costs and faces the same market, so its best response is the mirror image. ++}

<!--
|   |   |
| --- | --- |
| 5.c | BR_B appears by symmetry, mirrored across a dashed 45° line, with BR_B: q_B = 30 − ¼q_A. |
-->

### {++ Whiteboard | Exercise Q2 ++}

{++ > Suppose firm B sells 40 units. What is firm A’s best response? If firm A sells that quantity, what is firm B’s best response? Is this pair a Nash equilibrium? ++}

<!--
|   |   |
| --- | --- |
| Q2 | Board only. Answer: A’s best response to 40 is 20; B’s best response to 20 is 25, not 40, so (20, 40) is not a Nash equilibrium. |
-->

## Nash Equilibrium

{++ Where the two lines cross, each firm is choosing its best quantity given what the other is choosing. Neither wants to change. That’s a Nash equilibrium. ++}

<!--
|   |   |
| --- | --- |
| 6.a | Title Nash Equilibrium. D1’s definition; a red dot where the lines cross, with question marks on both axes. |
-->

{++ To find it, use the symmetry. At the crossing the two quantities are equal, so put q_A in for q_B in firm A’s best response and solve. Each firm sells 24, and together they sell 48. ++}

<!--
|   |   |
| --- | --- |
| 6.b.substitute | symmetric → q_A\* = q_B\*; q_A\* = 30 − ¼q_A\*. |
| 6.b.solve | (5/4) q_A\* = 30; q_A\* = 30 · (4/5) = 24 = q_B\*. |
| 6.b | The 24 is carried to both axes. Q = q_A\* + q_B\* = 48. |
-->

{++ Take 48 back to the market’s demand curve and the price is 72. One seller sold 30 at a price of 90. Two sellers sell more, at a lower price. ++}

<!--
|   |   |
| --- | --- |
| 6.c.price | Title Duopoly. The market graph returns with the monopoly outcome (30, 90) in grey, then 48 units up to demand at 72. “P = 120 − (24 + 24) = 120 − 48 = 72” |
| 6.c | “Two sellers: more output, lower price.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ > With two sellers the price is \$72 and each firm’s marginal cost at 24 units is \$48. Is this outcome efficient? Which way would a third seller move it? ++}

<!--
|   |   |
| --- | --- |
| Q3 | Board only. Answer: no. Buyers value the next unit at about \$72 and it costs about \$48, so there is still deadweight loss, less than under monopoly. A third seller adds output and lowers the price. |
-->

## {++ Cartel ++}

{++ Back to the matrix from the start of class. We found the 24. Where does the 20 come from? Suppose the two firms act as one seller and split the output evenly. Together they face the whole demand curve, so marginal revenue is 120 − 2Q. Each makes half, so the marginal cost of one more unit is Q. Setting them equal gives 40 units, 20 each, at a price of 80. ++}

<!--
|   |   |
| --- | --- |
| 6.d.rule | Title Cartel; subtitle “The two firms act as one seller.” The rule for acting as one: MR = 120 − 2Q and MC = Q. |
| 6.d | A green point on demand between the monopoly’s and the duopoly’s: 40 units, price 80. “That is Low in the matrix.” |
-->

{++ That’s the cartel, and it’s the Low, Low cell. It doesn’t hold: if the other firm makes 20, my best response is 25, not 20. Each of us wants to sell more, and we end up back at 24. ++}

<!--
|   |   |
| --- | --- |
| 6.e | The best-response rule at 20: 30 − ¼ · 20 = 25. “Each wants to sell more.” |
-->

## {++ Next time ++}

{++ Next time: what happens with more sellers? ++}

<!--
|   |   |
| --- | --- |
| 7.a | Title Next Time. A grey arrow points on down demand from the duopoly dot. “What happens with more sellers?” |
-->

