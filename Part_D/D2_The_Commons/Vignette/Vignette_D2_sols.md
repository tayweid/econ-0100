---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Vignette D2 | Common Resources

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due in Recitation. Vignettes are a certificate of the work done together in Recitation.*

## Q1 | Common Resource Problem

Two skilled potion makers, Slughorn and Snape, can each brew different types of potions.

The two brewers share access to a magical garden where they gather rare ingredients. Each must decide whether to harvest sustainably or over-harvest. The payoff matrix shows their daily profits in Galleons:

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

a) What is Slughorn's best response when Snape chooses Sustainable? \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest: $12 > 8$.

:::

 

b) What is Slughorn's best response when Snape chooses Over-harvest? \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest: $4 > 2$.

:::

 

c) What is/are the Nash Equilibrium/Equilibria? \_\_\_\_\_\_\_\_\_\_

::: solution

$(OH, OH)$. Over-harvesting is each brewer's best response whatever the other does (the game is symmetric), so both over-harvest.

:::

 

d) What is the socially efficient outcome? \_\_\_\_\_\_\_\_\_\_

::::: solution

$(S, S)$. Total daily profits are $16$ at $(S, S)$, $14$ at $(S, OH)$ and $(OH, S)$, and $8$ at $(OH, OH)$.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Snape** |   |
| ---: | ---: | :---: | :---: |
|   |   | S | OH |
| **Slughorn** | Sustainable (S) | 8, 8 | 2, $\boxed{12}$ |
|   | Over-Harvest (OH) | $\boxed{12}$, 2 | $\boxed{4}$, $\boxed{4}$ |

:::

:::::

## Q2 | The Garden at Dawn

{++Late in the term the garden is nearly picked over, and if both brewers over-harvest it will be ruined. Snape now arrives at dawn and harvests first; Slughorn arrives at noon and sees what Snape left before he chooses. Each row of the table below is one path through the game tree. Daily profits are in Galleons, with Snape’s listed first.++}

::: {.table style=plain inset=8pt columns="auto auto 112pt" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Snape chooses** | **Then Slughorn chooses** | **Profits (Snape, Slughorn)** |
| :---: | :---: | :---: |
| S | S | 8, 8 |
|   | OH | 3, 10 |
| OH | S | 10, 4 |
|   | OH | 2, 2 |

:::

::: solution

*Q2 is a new question, drafted by Claude for skill D2.2 (Sequential Games). The answers are Claude’s, worked from the table.*

:::

a\) {++If Snape harvests sustainably, what is Slughorn’s best response?++} \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest: $10 > 8$.

:::

 

b\) {++If Snape over-harvests, what is Slughorn’s best response?++} \_\_\_\_\_\_\_\_\_\_

::: solution

Sustainable: $4 > 2$. With the garden nearly ruined, Slughorn does better leaving what is left to regrow.

:::

 

c\) {++Working backward, what does Snape choose?++} \_\_\_\_\_\_\_\_\_\_

::: solution

Over-Harvest. Harvesting sustainably leads to $(S, OH)$ and $3$ for Snape; over-harvesting leads to $(OH, S)$ and $10$. Since $10 > 3$, Snape over-harvests.

:::

 

d\) {++What is the outcome of the game? Is it socially efficient?++} \_\_\_\_\_\_\_\_\_\_

:::: solution

$(OH, S)$: Snape earns $10$ and Slughorn earns $4$, a total of $14$. It is not efficient: $(S, S)$ totals $16$. Moving first lets Snape take the larger share, and the garden is still over-harvested.

Slughorn’s best response on each branch is boxed. The yellow path is the outcome of the game.

::: {.table style=plain inset=8pt columns="auto auto 112pt" fills="r3c1:yellow r3c2:yellow" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Snape chooses** | **Then Slughorn chooses** | **Profits (Snape, Slughorn)** |
| :---: | :---: | :---: |
| S | S | 8, 8 |
|   | OH | 3, $\boxed{10}$ |
| OH | S | 10, $\boxed{4}$ |
|   | OH | 2, 2 |

:::

::::

 
