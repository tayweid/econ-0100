---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | HW D2 | Common Resources

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due: Sunday, Nov. 1*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. You are welcomed and encouraged to work in groups as long as your work is your own. Submit your answers on Gradescope when you’re finished: each answer there is a selection.

## Q1 | Enforceable Permits

Fearing a total collapse of the Shrake fishery, the Ministry of Magic hired Remus Lupin to develop a policy solution to the looming issue. Remus offered a few proposals but the policy chosen by the Ministry was to distribute a fishing permit to both Firm A and Firm B to harvest at low capacity ($L$) each season. This would lead to a sustainable population of Shrake into future seasons. Since there are only two firms supplying Shrake, the market is highly visible to regulators making the permits very enforceable. Any firm in violation, choosing a high capacity ($H$), would be required to pay a fine equal to half their seasonal profit. The following matrix summarizes the two firms' lifetime profits after the enforceable permits.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm B** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm A** | L | 10, 6 | 2, 5 |
|   | H | 9, 0.5 | 1.5, 1.5 |

:::

### a) Firm A's Best Response

What is Firm A's best response?

 

 

::: solution

$$
BR_A = \begin{cases} L & \text{if } L \\ L & \text{if } H \end{cases}
$$

:::

### b) Firm B's Best Response

What is Firm B's best response?

 

 

::: solution

$$
BR_B = \begin{cases} L & \text{if } L \\ H & \text{if } H \end{cases}
$$

:::

### c) Nash Equilibrium

Find all Nash ~~Equilibium~~{++Equilibrium++}.

 

 

::::: solution

$(L, L)$

Best responses are boxed. The yellow cell is the Nash equilibrium.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills=r2c2:yellow borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm B** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm A** | L | $\boxed{10}$, $\boxed{6}$ | $\boxed{2}$, 5 |
|   | H | 9, 0.5 | 1.5, $\boxed{1.5}$ |

:::

:::::

## Q2 | Plimpies in the Black Lake

{++*Optional. This question is about sequential games, which we are not covering this semester. It is here for anyone who wants to try it; it does not count toward the homework.*++}

{++Two firms, Firm A and Firm B, fish for plimpies in the Black Lake. Firm A’s fleet sets out first each season, and Firm B’s scouts see Firm A’s nets before Firm B chooses low ($L$) or high ($H$) capacity. If Firm A fishes low, the stock stays healthy and Firm B prefers to keep it that way. If Firm A fishes high, the stock will collapse anyway, so Firm B harvests all it can. Each row of the table below is one path through the game tree. Lifetime profits are in coins.++}

::: {.table style=plain inset=8pt columns="auto auto 112pt" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm A chooses** | **Then Firm B chooses** | **Profits (A, B)** |
| :---: | :---: | :---: |
| L | L | 9, 9 |
|   | H | 2, 7 |
| H | L | 12, 1 |
|   | H | 4, 4 |

:::

::: solution

*Q2 is a new question, drafted by Claude for skill D2.2 (Sequential Games). The answers are Claude’s, worked from the table.*

:::

### a) Firm B’s Responses

{++If Firm A chooses $L$, what does Firm B choose? If Firm A chooses $H$?++}

 

 

::: solution

If Firm A chooses $L$, Firm B chooses $L$: $9 > 7$. If Firm A chooses $H$, Firm B chooses $H$: $4 > 1$.

:::

### b) Firm A’s Choice

{++Working backward, which capacity does Firm A choose?++}

 

 

::: solution

$L$. Choosing $L$ leads to $(L, L)$ and $9$ for Firm A; choosing $H$ leads to $(H, H)$ and $4$. Since $9 > 4$, Firm A chooses $L$.

:::

### c) The Outcome

{++What is the outcome of the game? Is it socially efficient?++}

 

 

:::: solution

$(L, L)$, with $9$ for each firm. It is efficient: total profits are $18$ at $(L, L)$, $9$ at $(L, H)$, $13$ at $(H, L)$ and $8$ at $(H, H)$.

Firm B’s best response on each branch is boxed. The yellow path is the outcome of the game.

::: {.table style=plain inset=8pt columns="auto auto 112pt" fills="r1c1:yellow r1c2:yellow" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm A chooses** | **Then Firm B chooses** | **Profits (A, B)** |
| :---: | :---: | :---: |
| L | L | 9, $\boxed{9}$ |
|   | H | 2, 7 |
| H | L | 12, 1 |
|   | H | 4, $\boxed{4}$ |

:::

::::

### d) Choosing at the Same Time

{++Suppose instead the firms chose at the same time, without seeing each other’s nets. Write the same profits as a payoff matrix and find all Nash Equilibrium.++}

 

 

:::: solution

$(H, H)$. Without seeing Firm B’s choice, Firm A harvests high whatever Firm B does ($12 > 9$ and $4 > 2$), and Firm B’s best response to $H$ is $H$. Moving first helps here: Firm A knows that fishing low keeps Firm B fishing low, which is worth more to Firm A than the extra catch.

Best responses are boxed. The yellow cell is the Nash Equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm B** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm A** | L | 9, $\boxed{9}$ | 2, 7 |
|   | H | $\boxed{12}$, 1 | $\boxed{4}$, $\boxed{4}$ |

:::

::::
