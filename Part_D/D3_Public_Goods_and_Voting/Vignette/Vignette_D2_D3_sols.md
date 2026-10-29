---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
linestretch: 1
plass:
  number-equations: false
---

# ECON 0100 | Vignette D2 | Commons

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due in Recitation. Vignettes are a certificate of the work done together in Recitation.*

### Late Night Ingredients

Two skilled potion makers, Slughorn and Snape, can each brew different types of potions. They share access to a garden where they gather rare ingredients for their potions. The ingredients can only be harvested late at night, making it difficult to know who else uses the garden. Each must decide how much of the ingredients to harvest. The payoff matrix shows their monthly profits in Coins:

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Snape** |   |
| ---: | ---: | :---: | :---: |
|   |   | S | OH |
| **Slughorn** | Sustainable (S) | 8, 8 | 2, 12 |
|   | Over-Harvest (OH) | 12, 2 | 4, 4 |

:::

::: solution

*No solution notes exist for this question. These answers are Claude's, worked from the payoff matrix.*

:::

a\) What is Slughorn’s best response when Snape chooses Sustainable? \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest: $12 > 8$.

:::

b\) What is Slughorn’s best response when Snape chooses Over-harvest? \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest: $4 > 2$.

:::

c\) What is *(are)* the Nash Equilibrium? \_\_\_\_\_\_\_\_\_\_

::: solution

$(OH, OH)$. Over-harvesting is each brewer's best response whatever the other does (the game is symmetric), so both over-harvest.

:::

d\) What is the socially efficient outcome? \_\_\_\_\_\_\_\_\_\_

 



::::: solution

$(S, S)$. Total monthly profits are $16$ at $(S, S)$, $14$ at $(S, OH)$ and $(OH, S)$, and $8$ at $(OH, OH)$.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Snape** |   |
| ---: | ---: | :---: | :---: |
|   |   | S | OH |
| **Slughorn** | Sustainable (S) | 8, 8 | 2, $\boxed{12}$ |
|   | Over-Harvest (OH) | $\boxed{12}$, 2 | $\boxed{4}$, $\boxed{4}$ |

:::

:::::

\newpage

## ECON 0100 | Vignette D3 | Public Goods

### The Broom Shed Roof

Oliver Wood and Cedric Diggory, the Gryffindor and Hufflepuff Quidditch captains, each have 10 coins in their team fund. The broom shed the two teams share needs a new roof. Each captain chooses to contribute all 10 coins (C) or nothing (DC). Madam Hooch collects the money by owl over the holidays: each captain sends a sealed pledge, and she opens both on the first day of term, so neither knows what the other gave until it’s too late to change. Every 10 coins contributed buys repairs worth 6 coins to each team, whether or not that team contributed. Each team’s payoff is the coins it keeps plus the value of the repairs. Fill in the payoff matrix below.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Diggory** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Wood** | C |   |   |
|   | DC |   |   |

:::

::::: solution

Payoff = coins kept + 6 for every 10 coins contributed. Both contribute: $0 + 12 = 12$ each. Only Wood contributes: he gets $0 + 6 = 6$ and Diggory gets $10 + 6 = 16$ (and the reverse when only Diggory contributes). Neither contributes: $10 + 0 = 10$ each.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Diggory** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Wood** | C | 12, 12 | 6, $\boxed{16}$ |
|   | DC | $\boxed{16}$, 6 | $\boxed{10}$, $\boxed{10}$ |

:::

:::::

a\) Identify the best responses of Wood and Diggory.

 

::: solution

$$
BR_{Wood} = \begin{cases} DC & \text{if Diggory contributes } (16 > 12) \\ DC & \text{if Diggory doesn't } (10 > 6) \end{cases}
$$

Diggory faces the same payoffs, so his best response is also DC whatever Wood does.

:::

b\) Identify a Nash Equilibrium in this game if one exists.

 

::: solution

$(DC, DC)$. Diggory faces the same payoffs, so DC is dominant for him too. Neither contributes and the roof stays broken: the free rider problem.

:::

c\) Find the socially efficient strategies.

 

::: solution

$(C, C)$. It totals 24 coins, against 22 when only one contributes and 20 when neither does.

:::

The pledges fall short, so Madam Hooch puts the roof to a vote of the two captains and the Head of School, Professor Dumbledore, whose budget also pays for the shed. A full new roof costs 21 coins, paid by a levy of 7 coins each on Gryffindor, Hufflepuff, and the school if a majority votes yes. Each voter’s value of a new roof is below.

::: {.table style=grid}

| **Wood** | **Diggory** | **Dumbledore** |
| :---: | :---: | :---: |
| 9 | 8 | 1 |

:::

d\) Would the levy receive a majority vote?

 

::: solution

Yes, 2–1. Wood (9 > 7) and Diggory (8 > 7) vote yes; Dumbledore (1 < 7) votes no.

:::

e\) What is the marginal social benefit of the new roof?

 

::: solution

$MSB = 9 + 8 + 1 = 18$

:::

f\) Would building the roof be efficient?


::: solution

No. The marginal social benefit of 18 is below the cost of 21, so the vote builds a roof that is not worth its cost. Majority voting counts how many voters gain, not how much each gains or loses.

:::
