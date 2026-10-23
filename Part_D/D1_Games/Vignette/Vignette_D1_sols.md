---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Vignette D1 | Game Theory

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due in Recitation. Vignettes are a certificate of the work done together in Recitation.*

~~Vignette D5 was given as a MinExam in a previous semester.~~

## Q1 | Keeping House: Gryffindor

Ron and Harry share a room in the Gryffindor tower during the school year. Neither student is partial to chores, and would prefer not to tidy up their shared space. But both enjoy when the room is clean, and are more than willing to tidy the room if it means the space is neat. Their payoffs are represented by the following payoff matrix:

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Harry** |   |
| ---: | ---: | :---: | :---: |
|   |   | Clean | Don’t |
| **Ron** | Clean | 2, 3 | 0, 3 |
|   | Don’t | 3, 0 | 1, 1 |

:::

### a) Best Response

Find Harry’s best response.

 

 

::: solution

$$
BR_H = \begin{cases} C, D & \text{if } \sigma_R = C \\ D & \text{if } \sigma_R = D \end{cases}
$$

:::

### b) Efficient Strategies

Which set of strategies is efficient for Ron and Harry?

 

 

::: solution

Efficient Strategies: $(C, C)$

:::

### c) Nash Equilibrium

What is the Nash equilibrium?

 

 

::::: solution

Nash Eq.: $(D, D)$

Best responses are boxed. The yellow cell is the Nash equilibrium, and the blue cell is socially efficient.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills="r2c2:blue r3c3:yellow" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Harry** |   |
| ---: | ---: | :---: | :---: |
|   |   | Clean | Don’t |
| **Ron** | Clean | 2, $\boxed{3}$ | 0, $\boxed{3}$ |
|   | Don’t | $\boxed{3}$, 0 | $\boxed{1}$, $\boxed{1}$ |

:::

:::::

## Q2 | Keeping House: Slytherin

Meanwhile in Slytherin, Malfoy and Crabbe face a similar situation. But due to their financial position, they may choose to hire a house elf to avoid the unpleasant chore of cleaning up, or avoid paying and leave their room messy. Their payoffs are given in the following table.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Malfoy** |   |
| ---: | ---: | :---: | :---: |
|   |   | Hire | Don’t |
| **Crabbe** | Hire | 5, 4 | 3, 3 |
|   | Don’t | 3, 4 | 2, 3 |

:::

### a) Best Response

Find Malfoy best response.

 

 

::: solution

$$
BR_M = \begin{cases} H & \text{if } \sigma_C = H \\ H & \text{if } \sigma_C = D \end{cases}
$$

:::

### b) Efficiency

Which set of strategies is efficient for Malfoy and Crabbe?

 

 

::: solution

Efficient Strategies: $(H, H)$

:::

### c) Nash Equilibrium

What is the Nash Equilibrium?

 

 

::::: solution

Nash Equilibrium: $(H, H)$

Best responses are boxed. The yellow cell is the Nash equilibrium, and it is also the efficient strategy pair.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" fills=r2c2:yellow borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Malfoy** |   |
| ---: | ---: | :---: | :---: |
|   |   | Hire | Don’t |
| **Crabbe** | Hire | $\boxed{5}$, $\boxed{4}$ | $\boxed{3}$, 3 |
|   | Don’t | 3, $\boxed{4}$ | 2, 3 |

:::

:::::
