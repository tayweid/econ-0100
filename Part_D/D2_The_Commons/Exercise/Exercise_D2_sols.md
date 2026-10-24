---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Exercise D2 | Common Resources

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

## Q1 | Shrake Fishery

The Shrake is a powerfully magical fish with significant interest as a potent ingredient in potions. Since their spines easily damage fishing nets, only two massive ~~cooporate~~{++corporate++} firms (confidentially called Firm A and Firm B) remain in the market after independently developing highly secretive technology for harvesting Shrake. Both firms have the ability to harvest vast quantities of Shrake but can make substantial profit even with low harvests. At low capacities ($L$) the fishery could support both firms, but at high capacities ($H$) overfishing would lead to population collapse in future years. Following these two fishing strategies, the lifetime profits (in Galleons) for the {++firms++} are summarized by the following payoff matrix.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm B** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm A** | L | 10, 6 | 2, 10 |
|   | H | 18, 1 | 3, 3 |

:::

### a) Firm A's Best Response

What is Firm A's best response?

 

 

::: solution

$$
BR_A = \begin{cases} H & \text{if } L \\ H & \text{if } H \end{cases}
$$

:::

### b) Firm B's Best Response

What is Firm B's best response?

 

 

::: solution

$$
BR_B = \begin{cases} H & \text{if } L \\ H & \text{if } H \end{cases}
$$

:::

### c) Nash Equilibrium

Find all Nash ~~Equilibium~~{++Equilibrium++}.

 

 

::: solution

$(H, H)$

:::

### d) Socially Efficient

Find the socially efficient strategies.

 

 

::::: solution

$(H, L)$. Total lifetime profits are $16$ at $(L, L)$, $12$ at $(L, H)$, $19$ at $(H, L)$ and $6$ at $(H, H)$.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r3c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm B** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm A** | L | 10, 6 | 2, $\boxed{10}$ |
|   | H | $\boxed{18}$, 1 | $\boxed{3}$, $\boxed{3}$ |

:::

:::::

## Q2 | Shrake Fishery, Firm A Moves First

{++Now suppose Firm A’s fleet sets out first each season, and Firm B sees how much Firm A is harvesting before choosing its own capacity. Lifetime profits are the same as in Q1. Each row of the table below is one path through the game tree: Firm A’s choice, then Firm B’s.++}

::: {.table style=plain inset=8pt columns="auto auto 112pt" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm A chooses** | **Then Firm B chooses** | **Profits (A, B)** |
| :---: | :---: | :---: |
| L | L | 10, 6 |
|   | H | 2, 10 |
| H | L | 18, 1 |
|   | H | 3, 3 |

:::

::: solution

*Q2 is a new question, drafted by Claude for skill D2.2 (Sequential Games). The answers are Claude’s, worked from the Q1 profits.*

:::

### a) Firm B’s Responses

{++If Firm A chooses $L$, what does Firm B choose? If Firm A chooses $H$?++}

 

 

::: solution

If Firm A chooses $L$, Firm B chooses $H$: $10 > 6$. If Firm A chooses $H$, Firm B chooses $H$: $3 > 1$.

:::

### b) Firm A’s Choice

{++Firm A knows how Firm B will respond. Which capacity does Firm A choose?++}

 

 

::: solution

$H$. Choosing $L$ leads to $(L, H)$ and $2$ for Firm A; choosing $H$ leads to $(H, H)$ and $3$. Since $3 > 2$, Firm A chooses $H$.

:::

### c) The Outcome

{++What is the outcome of the game, and what does each firm earn?++}

 

 

::: solution

$(H, H)$: Firm A earns $3$ and Firm B earns $3$.

:::

### d) Moving First

{++Compare this outcome with the Nash Equilibrium you found in Q1. Does moving first change the outcome? Why or why not?++}

 

 

:::: solution

No. The outcome is $(H, H)$, the same as the Nash Equilibrium in Q1. Firm B harvests high whatever Firm A does, so Firm A has no way to lead Firm B toward low harvests, and the fishery is still overused.

Firm B’s best response on each branch is boxed. The yellow path is the outcome of the game.

::: {.table style=plain inset=8pt columns="auto auto 112pt" fills=r4:yellow borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm A chooses** | **Then Firm B chooses** | **Profits (A, B)** |
| :---: | :---: | :---: |
| L | L | 10, 6 |
|   | H | 2, $\boxed{10}$ |
| H | L | 18, 1 |
|   | H | 3, $\boxed{3}$ |

:::

::::
