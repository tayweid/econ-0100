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

Best responses are boxed. The yellow cells are the two Nash equilibria.

::: {.table style=plain inset=8pt columns="auto auto 112pt 112pt" fills="r2c3:yellow r3c2:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Ron** |   |
| ---: | ---: | :---: | :---: |
|   |   | Contribute | Don’t Contribute |
| **Harry** | Contribute | 6, 6 | $\boxed{2}$, $\boxed{10}$ |
|   | Don’t Contribute | $\boxed{10}$, $\boxed{2}$ | 0, 0 |

:::

:::::

d) What well known phenomenon results from this game?

 

 

::: solution

The free rider problem: in either equilibrium one roommate does the shopping and the other enjoys the stocked kitchen without paying for it.

:::
