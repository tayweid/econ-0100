---
margin: {top: 0.45in, right: 0.45in, bottom: 0.45in, left: 0.45in}
fontsize: 10pt
linestretch: 1
plass:
  number-equations: false
---

# ECON 0100 | Demo D

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks. Each skill earns **Pass** or **Not Yet**; the first red block under each skill says what a Pass shows.*

## Hermione’s Potion Ingredients

Hermione and Draco share a garden plot growing moonflowers for their potions project. Each can harvest 1 or 2 flowers weekly. More harvesting reduces future growth. The payoff matrix shows their utility from different harvesting choices.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Draco** |   |
| ---: | ---: | :---: | :---: |
|   |   | H1 | H2 |
| **Hermione** | Harvest 1 (H1) | 10, 10 | 6, 15 |
|   | Harvest 2 (H2) | 14, 6 | 8, 8 |

:::

{++Outcomes are written (Hermione’s choice, Draco’s choice).++}

### D1.1 | Best Responses

::: solution

**Pass (D1.1):** Find all four best responses, H2 each time, by comparing a player’s own payoffs with the other player’s choice held fixed, and identify H2 as each player’s dominant strategy.

:::

::: {.table style=plain inset=4pt columns="auto 1fr 1fr"}

|   |   |   |
| :--- | :--- | :--- |
|   | **Hermione** | **Draco** |
| Best Response When the Other Harvests 1: | **[H2]{.red}** | **[H2]{.red}** |
| Best Response When the Other Harvests 2: | **[H2]{.red}** | **[H2]{.red}** |
| {++Dominant Strategy:++} | {++$\square$ H1 $\quad\boxtimes$ **[H2]{.red}** $\quad\square$ none++} | {++$\square$ H1 $\quad\boxtimes$ **[H2]{.red}** $\quad\square$ none++} |

:::

:::::: solution

::::: {.columns gutter=1em}

:::: column

Hold Draco’s choice fixed and compare Hermione’s payoffs, the first number in each cell, down his column. When Draco harvests 1, $14 > 10$, so she harvests 2. When Draco harvests 2, $8 > 6$, so she harvests 2.

Hold Hermione’s choice fixed and compare Draco’s payoffs, the second number, across her row. When Hermione harvests 1, $15 > 10$, so he harvests 2. When she harvests 2, $8 > 6$, so he harvests 2.

H2 is each player’s best response to everything the other could do, so H2 is a dominant strategy for both. Best responses are boxed.

::::

:::: column

::: {.table style=plain inset=8pt columns="auto auto 72pt 72pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Draco** |   |
| ---: | ---: | :---: | :---: |
|   |   | H1 | H2 |
| **Hermione** | H1 | 10, 10 | 6, $\boxed{15}$ |
|   | H2 | $\boxed{14}$, 6 | $\boxed{8}$, $\boxed{8}$ |

:::

::::

:::::

::::::

### D1.2 | Nash Equilibrium & Efficiency

::: solution

**Pass (D1.2):** Check only (H2, H2) as the Nash equilibrium, identify (H1, H2) as efficient by comparing totals (16 at the equilibrium against 21), and identify (H1, H1) as the outcome both prefer to the equilibrium.

:::

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| Nash Equilibrium (*check all that apply*): | $\square$ (H1, H1) $\quad\square$ (H1, H2) $\quad\square$ (H2, H1) $\quad\boxtimes$ **[(H2, H2)]{.red}** |
| Socially Efficient Outcome ({++*check all that apply*++}): | $\square$ (H1, H1) $\quad\boxtimes$ **[(H1, H2)]{.red}** $\quad\square$ (H2, H1) $\quad\square$ (H2, H2) |
| {++Total Payoff, Nash Equilibrium / Efficient Outcome:++} | {++**[16]{.red}** / **[21]{.red}**++} |
| {++An Outcome Both Prefer to the Nash Equilibrium:++} | {++$\boxtimes$ **[(H1, H1)]{.red}** $\quad\square$ (H1, H2) $\quad\square$ (H2, H1) $\quad\square$ none++} |

:::

:::::: solution

::::: {.columns gutter=1em}

:::: column

A Nash equilibrium is a cell where both payoffs are best responses, both boxed. Only (H2, H2) qualifies, so it is the one Nash equilibrium (yellow).

Efficiency compares total payoffs: (H1, H1) totals $20$, (H1, H2) totals $6 + 15 = 21$, (H2, H1) totals $14 + 6 = 20$, and (H2, H2) totals $16$. The efficient outcome is (H1, H2) (blue): Hermione harvests 1 and Draco harvests 2. Read the pair as (row, column); (H2, H1) totals only $20$.

::::

:::: column

::: {.table style=plain inset=8pt columns="auto auto 72pt 72pt" fills="r2c3:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Draco** |   |
| ---: | ---: | :---: | :---: |
|   |   | H1 | H2 |
| **Hermione** | H1 | 10, 10 | 6, $\boxed{15}$ |
|   | H2 | $\boxed{14}$, 6 | $\boxed{8}$, $\boxed{8}$ |

:::

::::

:::::

The Nash equilibrium is not efficient: its total of $16$ is $5$ below $21$. Both students would do better at (H1, H1), with $10$ each instead of $8$, but harvesting 2 is each one’s dominant strategy, so neither holds back alone. This is a Prisoner’s Dilemma. Neither (H1, H2) nor (H2, H1) is better for both: each leaves one student with $6$, below the $8$ of the equilibrium.

::::::

### D2.1 | Common Resources

::: solution

**Pass (D2.1):** Classify the moonflowers as rival and non-excludable, show that Hermione’s switch gains her 2 while costing Draco 7, subtract the fine of 6 from every payoff for harvesting 2, and find the new equilibrium (H1, H1).

:::

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| {++The Moonflowers in the Plot Are:++} | {++$\boxtimes$ **[rival]{.red}** $\quad\square$ non-rival++} |
|   | {++$\square$ excludable $\quad\boxtimes$ **[non-excludable]{.red}**++} |
| {++If Hermione Switches From (H1, H2) to (H2, H2):++} | {++Hermione: + **[2]{.red}** $\quad$ Draco: − **[7]{.red}**++} |

:::

::::: {.columns gutter=1em}

:::: column

{++Professor Sprout begins checking the plot each week and fines anyone who harvests 2 flowers. The fine lowers that student’s payoff by 6. Fill in the payoff matrix with the fine.++}

::: {.table style=plain inset=4pt columns="auto 1fr" spans=r0c0:2x1 aligns=r0c0:default}

|   |   |
| :--- | :--- |
| {++Nash Equilibrium With the Fine:++} |   |
| {++$\boxtimes$ **[(H1, H1)]{.red}**++} | {++$\square$ (H1, H2)++} |
| {++$\square$ (H2, H1)++} | {++$\square$ (H2, H2)++} |

:::

::::

:::: column

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Draco** |   |
| ---: | ---: | :---: | :---: |
|   |   | H1 | H2 |
| **Hermione** | H1 | **[10, 10]{.red}** | **[6, 9]{.red}** |
|   | H2 | **[8, 6]{.red}** | **[2, 2]{.red}** |

:::

::::

:::::

:::::: solution

The moonflowers are rival: a flower one student harvests is a flower the other can’t, and harvesting more reduces future growth for both. They are non-excludable: the plot is shared, so neither can keep the other out. A rival, non-excludable good is a common resource.

Start at (H1, H2), where Draco harvests 2. If Hermione switches to 2, her payoff rises from $6$ to $8$, a gain of $2$, but Draco’s falls from $15$ to $8$, a loss of $7$. Hermione counts her own gain and not Draco’s loss, so she switches even though the total falls by $5$. Draco reasons the same way, and the plot is overharvested.

::::: {.columns gutter=1em}

:::: column

The fine comes off Hermione’s payoff in her H2 row and off Draco’s payoff in his H2 column; at (H2, H2) both are fined. Now harvesting 1 is each student’s best response to either choice: for Hermione $10 > 8$ and $6 > 2$, for Draco $10 > 9$ and $6 > 2$. The only Nash equilibrium is (H1, H1) (yellow), the sustainable harvest.

::::

:::: column

::: {.table style=plain inset=8pt columns="auto auto 72pt 72pt" fills=r2c2:yellow borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Draco** |   |
| ---: | ---: | :---: | :---: |
|   |   | H1 | H2 |
| **Hermione** | H1 | $\boxed{10}$, $\boxed{10}$ | $\boxed{6}$, 9 |
|   | H2 | 8, $\boxed{6}$ | 2, 2 |

:::

::::

:::::

When the other harvests 1, harvesting 2 is still worth $4$ more to Hermione ($14 - 10$) and $5$ more to Draco ($15 - 10$). The fine of $6$ takes away more than that, so the rule makes the sustainable harvest each student’s best response.

::::::

\newpage

## Moonflower Management

In this question we will consider whether to impose a harvesting restriction. Five prefects harvest moonflowers from the Forbidden Forest. Without restrictions, the flowers will go extinct after this year. The table shows each prefect’s annual benefits (in coins), both under current harvesting and with proposed restrictions that would prevent extinction. The restrictions cost 60 coins yearly, split equally (12 coins each).

::: {.table style=grid columns="auto auto auto auto auto auto"}

| **Benefits** (*in coins*) | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Without restrictions | 25 | 22 | 18 | 16 | 12 |
| With restrictions (*not including fee*) | 40 | 35 | 32 | 20 | 15 |

:::

### D3.1 | Public Goods

::: solution

**Pass (D3.1):** Classify keeping the flowers from extinction as non-rival and non-excludable, see that no prefect pays voluntarily, add the five prefects’ gains to get a marginal social benefit of 49 coins, and compare it with the 60-coin cost.

:::

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| {++Keeping the Moonflowers From Extinction Is:++} | {++$\square$ rival $\quad\boxtimes$ **[non-rival]{.red}**++} |
|   | {++$\square$ excludable $\quad\boxtimes$ **[non-excludable]{.red}**++} |
| {++Prefects Who Would Pay Voluntarily, With No Fee:++} | {++**[None]{.red}**++} |
| {++Marginal Social Benefit of the Restrictions:++} | {++**[49 coins]{.red}**++} |
| {++Providing the Restrictions Is:++} | {++$\square$ efficient $\quad\boxtimes$ **[not efficient]{.red}**++} |

:::

:::: solution

Keeping the flowers alive is non-rival: one prefect’s benefit from the flowers surviving takes nothing from another’s. It is non-excludable: a prefect who pays nothing can’t be kept from that benefit. So it is a public good. The flowers themselves, picked one at a time, are rival: a common resource.

Every prefect enjoys the restrictions whether or not they pay, and no prefect’s own gain, at most $15$, comes close to the $60$ cost. Simply considering their own interests, none pays. This is a classic free rider problem.

Each prefect’s marginal benefit from the restrictions is the rise in their benefit:

::: {.table style=grid columns="auto auto auto auto auto auto auto"}

|   | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** | **Total** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Without restrictions | 25 | 22 | 18 | 16 | 12 | 93 |
| With restrictions, before the fee | 40 | 35 | 32 | 20 | 15 | 142 |
| Marginal benefit | 15 | 13 | 14 | 4 | 3 | 49 |

:::

$$
MSB = 15 + 13 + 14 + 4 + 3 = 49 < 60 = MC
$$

The restrictions cost $11$ coins more than they are worth to the prefects, so providing them is not efficient. Don’t compare the with-restrictions total, $142$, with the cost: the prefects get most of that benefit without the restrictions.

::::

\newpage

### D3.2 | Voting on Public Goods

::: solution

**Pass (D3.2):** Compare Hermione’s 28 coins with the restrictions, after the fee, with her 25 without them to find her vote; count 3 for and 2 against; total 93 coins without and 82 with; and conclude that the restrictions pass but are not efficient.

:::

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| Hermione’s Benefit Without Restrictions: | **[25 coins]{.red}** |
| Hermione’s Benefit With Restrictions (*after the fee*): | **[28 coins]{.red}** |
| Hermione’s Vote: | $\boxtimes$ **[for]{.red}** $\quad\square$ against |
| Prefects Voting For / Against: | **[3]{.red}** / **[2]{.red}** |
| Total Benefit Without Restrictions: | **[93 coins]{.red}** |
| Total Benefit With Restrictions (*after the fees*): | **[82 coins]{.red}** |
| Restrictions With a 12-Coin Fee: | $\square$ efficient $\quad\boxtimes$ **[not efficient]{.red}** |

:::

:::: solution

Each prefect votes for the restrictions if their benefit with them, after the 12-coin fee, is higher than their benefit without them. Hermione’s is $40 - 12 = 28 > 25$, so she votes for them.

::: {.table style=grid columns="auto auto auto auto auto auto auto"}

|   | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** | **Total** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Without restrictions | 25 | 22 | 18 | 16 | 12 | 93 |
| With restrictions, after the fee | 28 | 23 | 20 | 8 | 3 | 82 |
| Vote | for | for | for | against | against | 3 to 2 |

:::

The restrictions pass 3 to 2, but total benefit falls from $93$ to $82$, so they are not efficient. The three prefects in favor gain $3 + 1 + 2 = 6$ coins, while Cho and Padma lose $8 + 9 = 17$. The vote makes Cho and Padma pay a 12-coin fee for restrictions worth only $4$ and $3$ to them. The $11$-coin loss is the same gap as between the restrictions’ marginal social benefit, $49$, and their $60$-coin cost.

::::
