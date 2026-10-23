---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | HW D1 | Game Theory

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due: Sunday, Oct. 25*

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. You are welcomed and encouraged to work in groups as long as your work is your own. Submit your answers on Gradescope when you’re finished: each answer there is a selection.

## Q1 | Dorm Room Kitchen

Harry and Ron share a dorm at Hogwarts and like to keep their kitchen stocked with snacks. They each have the option to contribute or not contribute to the kitchen snacks every week. They both like having the kitchen stocked even if they don’t eat the snacks but neither likes the chore of buying the snacks. If they both contribute, the kitchen will be fully stocked and they both receive a payoff equivalent to 6 galleons. If only one of them contributes, the contributor is able to enjoy the partially stocked kitchen but also had to do the shopping, receiving a payoff equivalent to 2 galleons, while the other receives a payoff equivalent to 10 galleons. If neither of them contributes, the kitchen is empty and they both receive a payoff of 0 galleons.

::: {.table style=plain inset=8pt columns="auto auto 112pt 112pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Ron** |   |
| ---: | ---: | :---: | :---: |
|   |   | Contribute | Don’t Contribute |
| **Harry** | Contribute | 6, 6 | 2, 10 |
|   | Don’t Contribute | 10, 2 | 0, 0 |

:::

::: solution

*No solution notes exist for this question. These answers are Claude's, worked from the payoff matrix.*

:::

a) Identify Ron's best response.

 

 

::: solution

$$
BR_{Ron} = \begin{cases} \text{Don't Contribute} & \text{if Harry contributes } (10 > 6) \\ \text{Contribute} & \text{if Harry doesn't } (2 > 0) \end{cases}
$$

:::

b) Identify Ron's dominant strategy if one exists.

 

 

::: solution

None. Ron's best response depends on what Harry does.

:::

c) Identify a Nash Equilibrium in this game if one exists.

 

 

::::: solution

There are two: (Harry Contributes, Ron Doesn't) and (Harry Doesn't, Ron Contributes). Harry's best responses mirror Ron's, so in each one the player who doesn't contribute is best responding to the other's contribution, and the contributor is best responding to the other's not contributing.

Best responses are boxed. The yellow cells are the two Nash equilibria; they and the blue cell are socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 112pt 112pt" fills="r2c2:blue r2c3:yellow r3c2:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Ron** |   |
| ---: | ---: | :---: | :---: |
|   |   | Contribute | Don’t Contribute |
| **Harry** | Contribute | 6, 6 | $\boxed{2}$, $\boxed{10}$ |
|   | Don’t Contribute | $\boxed{10}$, $\boxed{2}$ | 0, 0 |

:::

:::::

d) ~~What well known phenomenon results from this game?~~ {++Find the socially efficient strategies.++}

 

 

::: solution

Any outcome where at least one of them contributes: (Contribute, Contribute), (Contribute, Don't Contribute) and (Don't Contribute, Contribute) each total 12 galleons. Only (Don't Contribute, Don't Contribute), at 0, is inefficient.

:::

## Q2 | Late-Night Wireless

{++Seamus and Dean share a dorm at Hogwarts. Each night, each chooses whether to play his wireless late or keep quiet so the other can sleep. Each enjoys his own music, but both value a good night’s sleep, and they don’t value them equally. Their payoffs, in galleons, are below.++}

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Dean** |   |
| ---: | ---: | :---: | :---: |
|   |   | Quiet | Play |
| **Seamus** | Quiet | 6, 5 | 1, 7 |
|   | Play | 8, 2 | 4, 3 |

:::

::: solution

*Q2 and Q3 are new questions, drafted by Claude in the format of Q1. The answers are Claude's, worked from the payoff matrices.*

:::

a) {++Identify Dean's best response.++}

 

 

::: solution

$$
BR_{Dean} = \begin{cases} \text{Play} & \text{if Seamus keeps quiet } (7 > 5) \\ \text{Play} & \text{if Seamus plays } (3 > 2) \end{cases}
$$

:::

b) {++Identify Dean's dominant strategy if one exists.++}

 

 

::: solution

Play. It is Dean's best response whatever Seamus does.

:::

c) {++Identify a Nash Equilibrium in this game if one exists.++}

 

 

::::: solution

(Play, Play). Play is dominant for Seamus too: $8 > 6$ if Dean keeps quiet and $4 > 1$ if Dean plays.

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Dean** |   |
| ---: | ---: | :---: | :---: |
|   |   | Quiet | Play |
| **Seamus** | Quiet | 6, 5 | 1, $\boxed{7}$ |
|   | Play | $\boxed{8}$, 2 | $\boxed{4}$, $\boxed{3}$ |

:::

:::::

d) {++Find the socially efficient strategies.++}

 

 

::: solution

(Quiet, Quiet). It totals 11 galleons, against 8 at (Quiet, Play), 10 at (Play, Quiet) and 7 at (Play, Play).

:::

## Q3 | Sunday Breakfast

{++Fred and George like a big breakfast at the Burrow on Sunday mornings, but it takes two cooks. Each twin chooses whether to get up early to cook or to sleep in and make toast later. Their payoffs, in galleons, are below.++}

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **George** |   |
| ---: | ---: | :---: | :---: |
|   |   | Cook | Sleep In |
| **Fred** | Cook | 8, 8 | 0, 4 |
|   | Sleep In | 4, 0 | 4, 4 |

:::

a) {++Identify George's best response.++}

 

 

::: solution

$$
BR_{George} = \begin{cases} \text{Cook} & \text{if Fred cooks } (8 > 4) \\ \text{Sleep In} & \text{if Fred sleeps in } (4 > 0) \end{cases}
$$

:::

b) {++Identify George's dominant strategy if one exists.++}

 

 

::: solution

None. George's best response depends on what Fred does.

:::

c) {++Identify a Nash Equilibrium in this game if one exists.++}

 

 

::::: solution

There are two: (Cook, Cook) and (Sleep In, Sleep In). In each, neither twin wants to change his choice alone.

Best responses are boxed. The yellow cells are the two Nash equilibria; (Cook, Cook) is also socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:yellow r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **George** |   |
| ---: | ---: | :---: | :---: |
|   |   | Cook | Sleep In |
| **Fred** | Cook | $\boxed{8}$, $\boxed{8}$ | 0, 4 |
|   | Sleep In | 4, 0 | $\boxed{4}$, $\boxed{4}$ |

:::

:::::

d) {++Find the socially efficient strategies.++}

 

 

::: solution

(Cook, Cook). It totals 16 galleons, against 4 at (Cook, Sleep In) and at (Sleep In, Cook), and 8 at (Sleep In, Sleep In).

:::
