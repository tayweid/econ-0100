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
| 5–10 | Play `2.a.1` through `3.a` | The firm’s five steps, on a competitive firm and then the monopoly (the warmup’s answer); the monopoly handed to the market graph. |
| 10–16 | Resume through `4.b` | A second seller: price and marginal revenue depend on the other firm. |
| 16–20 | Hide projection; Q1 on board | Choose firm A’s quantity for a given quantity from firm B. |
| 20–29 | Resume through `5.c` | The best-response rule, its graph, and firm B’s by symmetry. |
| 29–33 | Hide projection; Q2 on board | Use a best response; test whether a pair is an equilibrium. |
| 33–42 | Resume through `6.b` | Nash equilibrium: 24 each, 48 together. |
| 42–47 | Hide projection; Q3 on board | Is the duopoly outcome efficient? |
| 47–50 | Resume to `7.a` | One, two, many sellers on one demand curve: 30 at 90, 48 at 72, 60 at 60. |

{++ This table is a proposal. It has not been timed against a run-through. ++}

<!--
|   |   |
| --- | --- |
| Model | Demand P = 120 − Q; every firm MC = 2q. Monopoly: 30 units at 90. BR_A: q_A = 30 − ¼q_B. Nash: 24 each, Q = 48, P\* = 72. |
| Matrix | 1.b to 1.l, added 2026-11-18, in D1’s diamond layout. Low = 20 is each firm’s share of the 40 units a cartel would make; High = 24 is the Nash quantity. The profits are given on screen, not derived there; they come from TC = 900 + q²: 300 each at Low, 252 each at High, 348 and 220 when one goes High. |
| Open | The matrix section has no minutes of its own yet: the rows after it in the timing table have not been moved. |
| Matrix | Only the 24 is derived later (6.b). The 20 is the cartel share, 120 − 2Q = Q so Q = 40; the holds that derived it were cut on 2026-11-18, so on screen it is simply the low option. |
| Open | 7.a’s competitive outcome, 60 units at 60, is exactly two firms at 30 each on this market read in units: two price takers would land there, where the two duopolists land at 48 units and 72. The ordering of the points is the lesson; “many” sellers needs the market read in thousands, as E2 does. |
| Costs | One cost curve for the whole episode since 2026-11-18: TC = 900 + q², so MC = 2q and ATC is lowest at 60, at 30 units. Monopoly: 30 at 90, ATC 60, profit 900. Duopoly: 24 each at 72, profit 252 each. Long-run competition: 30 per firm at 60, profit zero. E1 and E2 were taught with a fixed cost of 1,000 and E3 with 1,200, so the monopoly’s ATC and profit here (60 and 900) are not last class’s (70 and 600). At 1,200 the duopolists would lose money. |
| Open | In the review ATC is grey and MR pink; E3 itself draws demand grey and MR blue. |
| Open | MR_A = 120 − 2q_A − q_B is no longer shown in section 4; it first appears in 5.a’s algebra. The line “Your marginal revenue also depends on how much the other firm sells” left with the old 4.b.zero hold. |
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
| Warmup | Board only; this is E3’s problem, and 2.c.q and 2.c.p work it again. Answers: a) 2q = 120 − 2q, so q = 30; b) P = 120 − 30 = 90. |
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

{++ Same market as last time, with two firms in it. Each one makes either 20 units or 24. If we both make 20, the price is 80 and we each earn 300. If we both make 24, the price is 72 and we each earn 252. If only one of us makes 24, that firm earns 348 and the other earns 220. ++}

<!--
|   |   |
| --- | --- |
| 1.b | Title Duopoly; subtitle “Many buyers, two sellers, selling a homogeneous good, with no externalities.” The empty diamond matrix: firm A and firm B, Low: 20 and High: 24. No demand or cost on screen. “How does a firm pick its quantity from these two options?” |
| 1.c | Both Low: 300 each. |
| 1.d.a, 1.d.b | Only firm A High, then only firm B High: 348 for the firm that goes High, 220 for the other. |
| 1.d | Both High: 252 each. Each cell fades in with its own line. |
-->

{++ Now it’s Part D again. Hold firm B at Low: I’d rather make 24, since 348 beats 300. Hold firm B at High: I’d still rather make 24, since 252 beats 220. Firm B is the same firm, so it reasons the same way. ++}

<!--
|   |   |
| --- | --- |
| 1.e, 1.f | Firm B at Low: the question, then “Firm A’s best response to Low is High”, boxed. |
| 1.g, 1.h | Firm B at High: the question, then the answer. |
| 1.i | Firm B’s two best responses boxed. “The firms are symmetric.” |
-->

{++ So both choose High, and that’s the Nash equilibrium. Both would earn more at Low, but neither would stay there. ~~Where do 20 and 24 come from? That’s the rest of today: let each firm choose any quantity.~~ What if each firm can choose any quantity? That’s the rest of today. ++}

<!--
|   |   |
| --- | --- |
| 1.j | Red box on both High: the Nash equilibrium, 252 each. |
| 1.k | Green box on both Low: 300 each, and each firm would switch. |
| 1.l | The bridge: “What if each firm can choose any quantity?” |
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
| 1.a.last | Title Monopoly; subtitle “One seller, many buyers.” The three-row market-structures table from E3 (many, few, one seller), with the red box on Monopoly. |
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
| 2.a.1 to 2.a | Title The Firm’s Problem; subtitle “Every firm solves the same problem, in the same five steps.” The five steps centred, one hold each, in grey with red for the firm’s choices and green for profit. No yellow line. |
| 2.b.setup | The steps slide right of centre behind a divider; a competitive firm’s graph beside them, labelled above: a flat MR at the market price with the firm’s demand dashed in teal over it, and MC. |
| 2.b.q, 2.b.p, 2.b.atc, 2.b.profit | The competitive firm in the long run, one step per hold, the current step lit: 30 units, a price of 60, ATC 60, profit zero. |
| 2.b | Step 5: it stays; with zero profit no new firms enter. |
| 2.c.setup | The layout widens: competitive firm, a divider, the monopoly, a divider, the steps. |
| 2.c.q, 2.c.p, 2.c.atc, 2.c.profit | The monopoly, the same steps from the top: 30 units (the same), a price of 90 (higher), ATC 60 (the same), profit 900. |
| 2.c | Step 5: it stays; its profit would draw firms in, but no one can enter. |
-->

{++ Let’s warm up on the case we already know. With one seller, the firm’s demand is the whole market’s demand, so its marginal revenue starts at the same place and falls twice as fast. ++}

{++ Step one: set marginal cost equal to marginal revenue. That gives 30 units. Step two: take that quantity up to the demand curve to find the price, 90. That’s the monopoly from last time. ++}

<!--
|   |   |
| --- | --- |
| 3.a | The hand-off: the review’s monopoly becomes the market graph with one thing marked, where MR_A meets MC, at 30 units. Title Monopoly. No price, no algebra. “The monopoly produces where MR meets MC: 30 units.” |
-->

## Duopoly

Since revenue is the product of price and quantity, however, it is very different in this environment. As always, prices are set by the demand curve and everyone can see the price. So as a seller, like both the monopolist and the competitive firm, you as the oligopolist will choose to set prices so that nothing you make goes unsold. But unlike the monopolist, you’re not the only seller. So the quantity that’s sold to buyers isn’t just what you make, but also includes what the other seller makes. Both of you are trying to sell into the same market. So if the other seller lowers their price, everyone will go to them until you lower your price as well. So just like in competitive markets, you don’t have any reason to switch prices from the price that sells everything for everyone.

<!--
|   |   |
| --- | --- |
| 4.a | Title Duopoly, with firm B selling zero. Firm A’s demand, P = 120 − (q_A + 0), sits above a divider and straddles it, with Q bracketed over the sum and the 0 marked q_B. Right of the divider, centred, a short axis named “Firm B’s Quantity” with a grey 0 at its foot, left of the axis and behind the red 0 at the start, and a red tick with “q_B = 0”. The graph becomes firm A’s (q_A, D_A, q_A\*). Firm B is white throughout the episode. “Both of you are trying to sell into the same market.” |
-->

But because the *price* depends on how much the other firm sells, your *revenue* depends on how much the other firm sells, which means your *marginal revenue* *also* depends on how much the other firm sells.

<!--
|   |   |
| --- | --- |
| 4.b.twenty_four | q_B rolls from 0 to 24: the tick rises, the number in the equation rolls, D_A and MR_A slide down under a grey copy of market demand, and a red line just outside the price axis opens between 120 and 96. q_A\* goes 30 → 24. “The demand for your good depends on how much the other firm sells.” |
| 4.b | q_B rolls to 48: intercept 72, q_A\* 18. “The more the other firm sells, the less buyers need what you’re selling.” |
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
| 5.a.rule | q_B rolls back to 0; the demand math leaves, a second divider appears, and firm B’s axis slides right, leaving three columns: the market graph, the algebra in the middle, firm B’s axis on the right. Title Best Responses; subtitle “The strategies are quantities.” The middle column is headed “1. How much to produce?”, the review’s step 1, over the row MR_A = MC_A, whose two names fly in from the curves’ labels. “Decide our best response to every decision the other seller might make.” |
-->

{++ Set firm A’s marginal revenue equal to its marginal cost, but leave firm B’s quantity as a letter. Solving for q_A gives a rule: for any quantity firm B might choose, here is firm A’s best quantity. We call that rule firm A’s best response. ++}

<!--
|   |   |
| --- | --- |
| 5.a.substitute | 120 − 2q_A − q_B = 2q_A: each side travels from its own curve on the graph into the row. |
| 5.a.simplify | 120 − q_B = 4q_A: the terms move down from the row above, the two 2q_A joining on the right as 4q_A. |
| 5.a.solved | q_A = 30 − ¼q_B, with the terms moving again; no name yet. |
| 5.a.depends | A yellow box around q_B: the answer depends on the other firm’s quantity. |
| 5.a | The name arrives: BR_A. |
-->

{++ A rule like this is easier to see as a picture. Put firm A’s quantity across and firm B’s up. If B sells nothing, A acts like a monopolist and sells 30. As B sells more, A’s best quantity shrinks, until at 120 A wouldn’t sell anything at all. ++}

<!--
|   |   |
| --- | --- |
| 5.b.graph | The algebra and both dividers leave; firm B’s axis slides into their space and becomes the vertical axis of an empty best-response graph, q_A across and q_B up. |
| 5.b.zero | The first point: q_B = 0 and firm A’s best response, 30. |
| 5.b.part | q_B rises to 48: firm A’s demand and MR slide down on the market graph while the point traces BR_A as far as (18, 48). No red line beside the price axis in this section. |
| 5.b.trace | The rest of the sweep, to q_B = 120: firm A’s demand and MR shrink to nothing and the point reaches (0, 120). |
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
| 5.c | BR_B appears by symmetry, mirrored across a dashed 45° line, with BR_B: q_B = 30 − ¼q_A. Firm B’s line and equation are grey. |
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
| 6.a | Title Nash Equilibrium. D1’s definition appears under the best-response definition, which stays; a red dot where the lines cross, with question marks on both axes. |
-->

{++ To find it, use the symmetry. At the crossing the two quantities are equal, so put q_A in for q_B in firm A’s best response and solve. Each firm sells 24, and together they sell 48. ++}

<!--
|   |   |
| --- | --- |
| 6.b.symmetric | Both definitions leave. The symmetry idea: “symmetric: q_A = q_B”. |
| 6.b.equation | Firm A’s best-response equation flies in from the graph: q_A = 30 − ¼q_B. |
| 6.b.swap | Symmetry in use: a q_A from the symmetry row takes q_B’s place, giving q_A = 30 − ¼q_A. |
| 6.b.collect | The terms move: q_A + ¼q_A = 30, then (5/4)q_A = 30. |
| 6.b.solve | q_A = 24. |
| 6.b.both | Symmetry again: q_B = 24, the q_B coming from the symmetry row. |
| 6.b | The two 24s fly back onto the graph’s axes, replacing the question marks. No Q = 48 row; 48 first appears on the closing graph. |
-->

{++ Take 48 back to the market’s demand curve and the price is 72. One seller sold 30 at a price of 90. Two sellers sell more, at a lower price. ++}

<!--
|   |   |
| --- | --- |
| 6.c.monopoly | Title One, Two, Many Sellers. The market graph returns beside the best-response graph, which loses its two equations. First point on demand: Monopoly, with 30 on the quantity axis and 90 on the price axis. “One seller sells 30 units at a price of 90.” |
| 6.c | Second point: Duopoly, 48 and 72. “Two sellers sell 48 units at a price of 72.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ > With two sellers the price is \$72 and each firm’s marginal cost at 24 units is \$48. Is this outcome efficient? Which way would a third seller move it? ++}

<!--
|   |   |
| --- | --- |
| Q3 | Board only. Answer: no. Buyers value the next unit at about \$72 and it costs about \$48, so there is still deadweight loss, less than under monopoly. A third seller adds output and lowers the price. |
-->

## {++ ~~Cartel~~ ++}

{++ ~~Back to the matrix from the start of class. We found the 24. Where does the 20 come from? Suppose the two firms act as one seller and split the output evenly. Together they face the whole demand curve, so marginal revenue is 120 − 2Q. Each makes half, so the marginal cost of one more unit is Q. Setting them equal gives 40 units, 20 each, at a price of 80.~~ ++}

{++ ~~That’s the cartel, and it’s the Low, Low cell. It doesn’t hold: if the other firm makes 20, my best response is 25, not 20. Each of us wants to sell more, and we end up back at 24.~~ ++}

<!--
|   |   |
| --- | --- |
| Cut | The cartel holds (6.d.rule, 6.d, 6.e) were removed from the animation on 2026-11-18; the paragraphs above are struck, not deleted. |
-->

## {++ Many sellers ++}

{++ ~~Next time: what happens with more sellers?~~ ++}

{++ And we already know what happens with many sellers. Firms enter until profit is zero, so the price falls to the lowest average total cost, 60. On this demand curve that’s 60 units. One seller, ~~a cartel,~~ two sellers, many sellers: each step moves further down the same demand curve, with more output and a lower price. ++}

<!--
|   |   |
| --- | --- |
| 7.a | Third point: Competition, 60 and 60. “Many sellers sell 60 units at a price of 60.” Each point has only its name; the numbers are on the axes. |
-->

