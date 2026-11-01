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

Outcomes are written (Hermione’s choice, Draco’s choice).

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
| Dominant Strategy: | $\square$ H1 $\quad\boxtimes$ **[H2]{.red}** $\quad\square$ none | $\square$ H1 $\quad\boxtimes$ **[H2]{.red}** $\quad\square$ none |

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
| Socially Efficient Outcome (*check all that apply*): | $\square$ (H1, H1) $\quad\boxtimes$ **[(H1, H2)]{.red}** $\quad\square$ (H2, H1) $\quad\square$ (H2, H2) |
| Total Payoff, Nash Equilibrium / Efficient Outcome: | **[16]{.red}** / **[21]{.red}** |
| An Outcome Both Prefer to the Nash Equilibrium: | $\boxtimes$ **[(H1, H1)]{.red}** $\quad\square$ (H1, H2) $\quad\square$ (H2, H1) $\quad\square$ none |

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
| The Moonflowers in the Plot Are: | $\boxtimes$ **[rival]{.red}** $\quad\square$ non-rival |
|   | $\square$ excludable $\quad\boxtimes$ **[non-excludable]{.red}** |
| If Hermione Switches From (H1, H2) to (H2, H2): | Hermione: **[+2]{.red}** $\quad$ Draco: **[−7]{.red}** |

:::

::::: {.columns gutter=1em}

:::: column

Professor Sprout begins checking the plot each week and fines anyone who harvests 2 flowers. The fine lowers that student’s payoff by 6. Fill in the payoff matrix with the fine.

::: {.table style=plain inset=4pt columns="auto 1fr" spans=r0c0:2x1 aligns=r0c0:default}

|   |   |
| :--- | :--- |
| Nash Equilibrium With the Fine: |   |
| $\boxtimes$ **[(H1, H1)]{.red}** | $\square$ (H1, H2) |
| $\square$ (H2, H1) | $\square$ (H2, H2) |

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

## End-of-Term Fireworks

Five prefects are planning the end-of-term celebration. A fireworks show over the lake would cost 60 coins, and it can be seen from anywhere on the grounds. The table shows each prefect’s benefit from the celebration (in coins), both without and with the fireworks.

::: {.table style=grid}

| **Benefits** (*in coins*) | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Without fireworks | 25 | 22 | 18 | 16 | 12 |
| With fireworks | 40 | 35 | 32 | 20 | 15 |

:::

### D3.1 | Public Goods

::: solution

**Pass (D3.1):** Classify the fireworks show as non-rival and non-excludable, see that no prefect contributes voluntarily, find each prefect’s marginal benefit as the rise in their benefit, add them to get a marginal social benefit of 49 coins, and compare it with the 60-coin cost.

:::

The prefects first try to raise the 60 coins by splitting the cost into voluntary contributions of 12 coins. Each prefect decides in their own interest whether to contribute or not.

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| The Fireworks Show Is: | $\square$ rival $\quad\boxtimes$ **[non-rival]{.red}** |
|   | $\square$ excludable $\quad\boxtimes$ **[non-excludable]{.red}** |
| Prefects Who Would Contribute Voluntarily: | **[None]{.red}** |

:::

::: {.table style=grid inset=8pt}

|   | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Marginal benefit of the fireworks | **[15]{.red}** | **[13]{.red}** | **[14]{.red}** | **[4]{.red}** | **[3]{.red}** |

:::

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| Marginal Social Benefit of the Fireworks: | **[49 coins]{.red}** |
| Providing the Fireworks Is: | $\square$ efficient $\quad\boxtimes$ **[not efficient]{.red}** |

:::

:::: solution

The fireworks show is non-rival: one prefect watching takes nothing away from another’s view. It is non-excludable: the show can be seen from anywhere on the grounds, so a prefect who pays nothing can’t be kept from watching. A non-rival, non-excludable good is a public good.

No prefect contributes. Every prefect sees the show whether or not they pay, so each would rather keep their 12 coins and let the others pay. This is the free rider problem. Cho and Padma would not pay even if their 12 coins were the only way to get the show, since it is worth just $4$ and $3$ to them. Without them the 60 coins can’t be raised, so a contribution from anyone else buys nothing.

Each prefect’s marginal benefit from the fireworks is the rise in their benefit, with the fireworks minus without:

::: {.table style=grid columns="auto auto auto auto auto auto auto"}

|   | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** | **Total** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Without fireworks | 25 | 22 | 18 | 16 | 12 | 93 |
| With fireworks | 40 | 35 | 32 | 20 | 15 | 142 |
| Marginal benefit | 15 | 13 | 14 | 4 | 3 | 49 |

:::

$$
MSB = 15 + 13 + 14 + 4 + 3 = 49 < 60 = MC
$$

The show costs $11$ coins more than it is worth to the prefects, so providing it is not efficient. Don’t compare the with-fireworks total, $142$, with the cost: the prefects get $93$ of that from the celebration without the fireworks.

::::

\newpage

### D3.2 | Voting on Public Goods

::: solution

**Pass (D3.2):** Compare Hermione’s 28 coins with the fireworks, after the fee, with her 25 without them to find her vote; count 3 for and 2 against; total 93 coins without and 82 with; and conclude that the fireworks pass but are not efficient.

:::

Instead, the prefects put the fireworks to a vote. If a majority votes for them, each prefect pays a fee of 12 coins (60 coins total).

::: {.table style=plain inset=4pt columns="auto 1fr"}

|   |   |
| :--- | :--- |
| Hermione’s Benefit Without Fireworks: | **[25 coins]{.red}** |
| Hermione’s Benefit With Fireworks (*after the fee*): | **[28 coins]{.red}** |
| Hermione’s Vote: | $\boxtimes$ **[for]{.red}** $\quad\square$ against |
| Prefects Voting For / Against: | **[3]{.red}** / **[2]{.red}** |
| Total Benefit Without Fireworks: | **[93 coins]{.red}** |
| Total Benefit With Fireworks (*after the fees*): | **[82 coins]{.red}** |
| Fireworks With a 12-Coin Fee: | $\square$ efficient $\quad\boxtimes$ **[not efficient]{.red}** |

:::

:::: solution

Each prefect votes for the fireworks if their benefit with them, after the 12-coin fee, is higher than their benefit without them. Hermione’s is $40 - 12 = 28 > 25$, so she votes for them.

::: {.table style=grid columns="auto auto auto auto auto auto auto"}

|   | **Hermione** | **Draco** | **Hannah** | **Cho** | **Padma** | **Total** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Without fireworks | 25 | 22 | 18 | 16 | 12 | 93 |
| With fireworks, after the fee | 28 | 23 | 20 | 8 | 3 | 82 |
| Vote | for | for | for | against | against | 3 to 2 |

:::

The fireworks pass 3 to 2, but total benefit falls from $93$ to $82$, so they are not efficient. The three prefects in favor gain $3 + 1 + 2 = 6$ coins, while Cho and Padma lose $8 + 9 = 17$. The vote makes Cho and Padma pay a 12-coin fee for a show worth only $4$ and $3$ to them. The $11$-coin loss is the same gap as between the show’s marginal social benefit, $49$, and its $60$-coin cost.

::::
