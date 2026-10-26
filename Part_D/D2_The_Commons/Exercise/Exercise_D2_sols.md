---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Exercise D2 | Commons

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

## Q1 | The Fishing Game

Two firms (Firm 1 and Firm 2) share a pond that initially contains 20,000 fish. Each firm simultaneously commits to Low Catch ($L$), taking one quarter of each month’s starting stock, or High Catch ($H$), taking one half, for all three months. Both firms calculate their catches from the same starting stock. After each harvest, the surviving fish double, up to a carrying capacity of 20,000 fish. Each firm aims to maximize its total catch over three months. Following these two fishing strategies, the total catches (in thousands of fish) for the firms are summarized by the following payoff matrix.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm 2** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm 1** | L | 15, 15 | 8.75, 17.5 |
|   | H | 17.5, 8.75 | 10, 10 |

:::

a\) What is Firm 1’s best response?

::: solution

$H$ regardless of Firm 2’s choice. If Firm 2 chooses $L$, Firm 1 prefers $17.5 > 15$; if Firm 2 chooses $H$, Firm 1 prefers $10 > 8.75$.

:::

b\) What is Firm 2’s best response?

::: solution

$H$ regardless of Firm 1’s choice. If Firm 1 chooses $L$, Firm 2 prefers $17.5 > 15$; if Firm 1 chooses $H$, Firm 2 prefers $10 > 8.75$.

:::

c\) Find all Nash Equilibrium.

::: solution

$(H, H)$ is the only Nash equilibrium. Each firm catches $10$ thousand fish.

:::

d\) Find the socially efficient strategies.

:::: solution

$(L, L)$. Total catches are $30$ at $(L, L)$, $26.25$ at $(L, H)$, $26.25$ at $(H, L)$ and $20$ at $(H, H)$, all in thousands of fish. Both choosing Low maximizes the combined catch among these four strategy profiles.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Firm 2** |   |
| ---: | ---: | :---: | :---: |
|   |   | L | H |
| **Firm 1** | L | 15, 15 | 8.75, $\boxed{17.5}$ |
|   | H | $\boxed{17.5}$, 8.75 | $\boxed{10}$, $\boxed{10}$ |

:::

::::

## Q2 | The Fishing Game, Firm 1 Moves First

Now suppose Firm 1 commits to its three-month fishing strategy first, and Firm 2 sees Firm 1’s choice before committing to its own strategy. Both firms still harvest from the same starting stock each month. Total catches are the same as in Q1. Each row of the table below is one path through the game tree: Firm 1’s choice, then Firm 2’s.

::: {.table style=plain inset=8pt columns="auto auto 112pt" borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm 1 chooses** | **Then Firm 2 chooses** | **Total catches (1, 2)** |
| :---: | :---: | :---: |
| L | L | 15, 15 |
|   | H | 8.75, 17.5 |
| H | L | 17.5, 8.75 |
|   | H | 10, 10 |

:::

a\) If Firm 1 chooses $L$, what does Firm 2 choose?

::: solution

Firm 2 chooses $H$: $17.5 > 15$.

:::

b\) If Firm 1 chooses $H$, what does Firm 2 choose?

::: solution

Firm 2 chooses $H$: $10 > 8.75$.

:::

c\) Knowing how Firm 2 will respond in each case, which strategy does Firm 1 choose?

::: solution

$H$. Choosing $L$ leads to $(L, H)$ and $8.75$ for Firm 1; choosing $H$ leads to $(H, H)$ and $10$. Since $10 > 8.75$, Firm 1 chooses $H$.

:::

d\) What is the outcome of the game, and what does each firm catch?

::: solution

$(H, H)$: Firm 1 catches $10$ thousand fish and Firm 2 catches $10$ thousand fish over the three months.

:::

e\) Does moving first change the outcome? Which firm has the higher payoff?

:::: solution

No. The outcome is $(H, H)$, the same as the Nash equilibrium in Q1. Firm 2 chooses High whatever Firm 1 does, so Firm 1 also chooses High. Neither firm has a higher payoff: both catch $10$ thousand fish.

Firm 2’s best response on each branch is boxed. The yellow path is the outcome of the game.

::: {.table style=plain inset=8pt columns="auto auto 112pt" fills=r4:yellow borders="r1c0:all r1-4c1-2:all r3c0:all" valign=middle spans="r1c0:1x2 r3c0:1x2"}

| **Firm 1 chooses** | **Then Firm 2 chooses** | **Total catches (1, 2)** |
| :---: | :---: | :---: |
| L | L | 15, 15 |
|   | H | 8.75, $\boxed{17.5}$ |
| H | L | 17.5, 8.75 |
|   | H | 10, $\boxed{10}$ |

:::

::::
