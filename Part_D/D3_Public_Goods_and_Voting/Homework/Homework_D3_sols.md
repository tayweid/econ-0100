---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | HW D3 | Public Goods

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due: Sunday, Nov. 1*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. You are welcomed and encouraged to work in groups as long as your work is your own. Submit your answers on Gradescope when you’re finished: each answer there is a selection.

## Q1 | Annual Yule Ball

Due to budget cuts, Hogwarts has decided not to hold the annual Yule Ball, which costs 1000 coins to host. In response, the student administration has come up with two proposals to fund the event. The first proposal is to raise everyone’s tuition to cover the cost of the ball, and the second proposal is to sell tickets to students.

To evaluate these proposals, the student administration has collected data on each student’s willingness to pay for a ticket to the Yule Ball by house. This data is presented in the table below. There are 100 students per house.

::: {.table style=grid}

|   | **Gryffindor** | **Hufflepuff** | **Ravenclaw** | **Slytherin** |
| :---: | :---: | :---: | :---: | :---: |
| **WTP** | 2 | 3 | 3 | 4 |

:::

a\) **Social Efficiency** Would the social planner choose to hold the Yule Ball? Remember, each house has 100 students, with each student’s willingness to pay represented in the table. So for example, Gryffindor’s total willingness to pay is 200 coins.

::: solution

Yes. Total willingness to pay is $200 + 300 + 300 + 400 = 1200$ coins, more than the $1000$ coin cost.

:::

b\) **Evaluating a Tuition Rise** The first proposal would raise everyone’s tuition by 2.5 coins to cover the cost of the Yule Ball. If this proposal were voted on by the student body, would it receive a majority vote? Would you consider it fair?

::: solution

Yes, it passes. The 300 students in Hufflepuff, Ravenclaw and Slytherin value the ball above 2.5 coins and vote for it; the 100 Gryffindors vote against. Fairness is a judgment call: each Gryffindor pays 2.5 coins for a ball worth 2 to them, so they are made worse off by 0.5 each while the other houses gain.

:::

c\) **Evaluating Tickets** Instead, could the student administration generate enough ticket sales to cover their costs if they sold tickets to the Yule Ball? If so, what price would work?

::: solution

No. At 4 coins only Slytherin buys: $400$. At 3, Hufflepuff, Ravenclaw and Slytherin buy: $900$. At 2, everyone buys: $800$. No single price raises the $1000$ coins.

:::

<!-- Q1 is the Fall 2024 Yule Ball question; its answers are Claude’s, worked from the table. Q2 and Q3 are Taylor’s (pulled 2026-10-29). -->

## Q2 | Lighting the High Street

Madam Rosmerta of the Three Broomsticks and Ambrosius Flume of Honeydukes have each set aside 12 coins this winter for lighting Hogsmeade’s high street. Each chooses to contribute all 12 coins (C) or nothing (DC). The Hogsmeade Village Council asks each shop to send its contribution in a sealed envelope and opens both envelopes together at its next meeting, so neither shop knows what the other gave until it’s too late to change. Every 12 coins contributed lights lamps worth 8 coins to each shop, whether or not that shop contributed. Each shop’s payoff is the coins it keeps plus the value of the lamps.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Flume** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Rosmerta** | C |   |   |
|   | DC |   |   |

:::

a\) **Payoff Matrix** Fill in the payoff matrix above.

:::: solution

Payoff = coins kept + 8 for every 12 coins contributed. Both contribute: $0 + 16 = 16$ each. Only Rosmerta contributes: she gets $0 + 8 = 8$ and Flume gets $12 + 8 = 20$ (and the reverse when only Flume contributes). Neither contributes: $12 + 0 = 12$ each.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Flume** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Rosmerta** | C | 16, 16 | 8, $\boxed{20}$ |
|   | DC | $\boxed{20}$, 8 | $\boxed{12}$, $\boxed{12}$ |

:::

::::

b\) **Best Response** Identify Rosmerta’s best response.

::: solution

$$
BR_{Rosmerta} = \begin{cases} DC & \text{if Flume contributes } (20 > 16) \\ DC & \text{if Flume doesn't } (12 > 8) \end{cases}
$$

:::

c\) **Dominant Strategy** Identify Rosmerta’s dominant strategy if one exists.

::: solution

$DC$. Not contributing is her best response whatever Flume does: contributing costs her 12 coins and brings her only 8 back.

:::

d\) **Nash Equilibrium** Identify a Nash Equilibrium in this game if one exists.

::: solution

$(DC, DC)$. Flume faces the same payoffs, so DC is dominant for him too. Neither contributes and the street stays dark: the free rider problem.

:::

e\) **Social Efficiency** Find the socially efficient strategies.

::: solution

$(C, C)$. It totals 32 coins, against 28 when only one contributes and 24 when neither does.

:::

\newpage

## Q3 | All or Nothing

The council learns that the old lamps cannot be lit one at a time. A new lighting charm for the whole street costs 24 coins, and it only works if it is paid in full. If only one shop contributes, its 12 coins are spent on a charm that fails and the street stays dark. If both contribute, the whole street is lit, worth 16 coins to each shop. As before, each shop chooses to contribute all 12 coins (C) or nothing (DC), and the council opens both sealed envelopes together. Each shop’s payoff is the coins it keeps plus the value of the lights.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Flume** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Rosmerta** | C |   |   |
|   | DC |   |   |

:::

a\) **Payoff Matrix** Fill in the payoff matrix above.

:::: solution

Both contribute: $0 + 16 = 16$ each. Only Rosmerta contributes: her 12 coins are spent and nothing is lit, so she gets $0 + 0 = 0$ and Flume keeps $12 + 0 = 12$ (and the reverse when only Flume contributes). Neither contributes: $12 + 0 = 12$ each.

Best responses are boxed. The yellow cells are the two Nash equilibria; (C, C) is also socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:yellow r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Flume** |   |
| ---: | ---: | :---: | :---: |
|   |   | C | DC |
| **Rosmerta** | C | $\boxed{16}$, $\boxed{16}$ | 0, 12 |
|   | DC | 12, 0 | $\boxed{12}$, $\boxed{12}$ |

:::

::::

b\) **Best Responses** Identify the best responses of Rosmerta and Flume.

::: solution

$$
BR_{Rosmerta} = \begin{cases} C & \text{if Flume contributes } (16 > 12) \\ DC & \text{if Flume doesn't } (12 > 0) \end{cases}
$$

Flume faces the same payoffs, so his best responses mirror hers. Neither shop has a dominant strategy: each wants to contribute only if the other does.

:::

c\) **Nash Equilibrium** Find all Nash Equilibria in this game.

::: solution

There are two: $(C, C)$, where the street is lit, and $(DC, DC)$, where it stays dark. In each, neither shop wants to change its choice alone.

:::

d\) **Social Efficiency** Find the socially efficient strategies.

::: solution

$(C, C)$. It totals 32 coins, against 12 when only one contributes and 24 when neither does. Unlike Q2, the efficient outcome is an equilibrium, but so is the dark street: the free rider problem has become a coordination problem.

:::
