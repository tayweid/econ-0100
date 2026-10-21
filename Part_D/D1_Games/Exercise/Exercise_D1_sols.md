---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Exercise D1 | Game Theory

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

## Q1 | Study Room Dynamics

Students in Ravenclaw and Hufflepuff share a secondary study room, which is open to all students from both houses at all hours. Every year the heads of house from both houses organize the sharing of cleaning duties. Cleaning improves the quality of the study room for members of both houses, but the chore is inconvenient. If both houses clean, the study room is a fantastic resource. But cleaning takes precious time away from studying, so neither house prefers doing it. The following matrix represents the benefits of each possible strategy combination.

::: {.table style=grid inset=9pt fills="r0:gray r1c0:gray r2c0:gray" valign=middle}

|   | **Hufflepuff:** Clean | **Hufflepuff:** Don’t Clean |
| :---: | :---: | :---: |
| **Ravenclaw:** Clean | 10, 10 | 6, 12 |
| **Ravenclaw:** Don’t Clean | 12, 6 | 8, 8 |

:::

a\) What is Ravenclaw’s best response?

b\) What is Hufflepuff’s best response?

c\) Identify each house’s dominant strategy if one exists.

d\) Find all Nash Equilibrium.

e\) Find the socially efficient strategies.

:::: solution

**a)** Don’t Clean, whatever Hufflepuff does. **b)** Don’t Clean, whatever Ravenclaw does. **c)** Don’t Clean is a dominant strategy for both houses. **d)** (Don’t Clean, Don’t Clean), with payoffs $(8, 8)$. **e)** (Clean, Clean), with payoffs $(10, 10)$.

Best responses are boxed. The yellow cell is the Nash equilibrium; the blue cell is socially efficient.

::: {.table style=grid inset=9pt fills="r0:gray r1c0:gray r1c1:blue r2c0:gray r2c2:yellow" valign=middle}

|   | **Hufflepuff:** Clean | **Hufflepuff:** Don’t Clean |
| :---: | :---: | :---: |
| **Ravenclaw:** Clean | 10, 10 | 6, $\boxed{12}$ |
| **Ravenclaw:** Don’t Clean | $\boxed{12}$, 6 | $\boxed{8}$, $\boxed{8}$ |

:::

**a)** Hold Hufflepuff’s choice fixed and compare Ravenclaw’s payoffs (the first number) down that column. If Hufflepuff cleans, Ravenclaw gets $12$ from Don’t Clean and $10$ from Clean: $12 > 10$. If Hufflepuff doesn’t clean, Ravenclaw gets $8$ from Don’t Clean and $6$ from Clean: $8 > 6$.

**b)** Hold Ravenclaw’s choice fixed and compare Hufflepuff’s payoffs (the second number) across that row. If Ravenclaw cleans: $12 > 10$. If Ravenclaw doesn’t clean: $8 > 6$. Don’t Clean again.

**c)** A dominant strategy is a best response to every choice the other player could make. Don’t Clean is each house’s best response whether the other house cleans or not, so it is dominant for both.

**d)** A Nash equilibrium is a cell where both payoffs are boxed. Only (Don’t Clean, Don’t Clean) qualifies: at $(8, 8)$, a house that switches to Clean on its own drops to $6$.

**e)** Total payoffs are $20$ for (Clean, Clean), $18$ for each one-house outcome, and $16$ for (Don’t Clean, Don’t Clean). Both cleaning is efficient, yet each house’s own interest leads to the outcome with the smallest total. This is a Prisoner’s Dilemma.

::::

\newpage

## Q2 | Date Night

Hagrid and McGonagall planned a date night, but had forgotten to decide between two locations: the Leaky Cauldron or Hog’s Head Pub. The time for the date was quickly approaching but neither knew where the other was going and didn’t have an owl with which to communicate. McGonagall knew Hagrid likes going out with McGonagall ($\Pi$ = 1) more than going out alone ($\Pi$ = 0), but that he likes going out with her to Hog’s head the best ($\Pi$ = 2). Hagrid knew McGonagall likes going out to Hog’s Head equally whether with or without Hagrid ($\Pi$ = 1), but that she only likes going to the Leaky Cauldron alone ($\Pi$ = 0,1).

a\) First, use the information about their preferences to setup the payoff matrix.

b\) Second, use the boxing method to find both players best responses above.

c\) Third, find the Nash Equilibrium. Since they couldn’t communicate, could they use this to figure out which location to go?

:::: solution

**a)** The matrix is below, Hagrid’s payoff first. **b)** Best responses are boxed. **c)** (Hog’s Head, Hog’s Head), with payoffs $(2, 1)$. Yes: it is the only Nash equilibrium.

::: {.table style=grid inset=9pt fills="r0:gray r1c0:gray r2c0:gray r2c2:yellow" valign=middle}

|   | **McGonagall:** Leaky Cauldron | **McGonagall:** Hog’s Head |
| :---: | :---: | :---: |
| **Hagrid:** Leaky Cauldron | $\boxed{1}$, 0 | 0, $\boxed{1}$ |
| **Hagrid:** Hog’s Head | 0, $\boxed{1}$ | $\boxed{2}$, $\boxed{1}$ |

:::

**a)** Hagrid gets $2$ when they are together at Hog’s Head, $1$ when they are together at the Leaky Cauldron, and $0$ whenever he is alone. McGonagall gets $1$ at Hog’s Head whether or not Hagrid is there. At the Leaky Cauldron she gets $1$ alone and $0$ with Hagrid.

**b)** Hagrid: if McGonagall goes to the Leaky Cauldron, Leaky Cauldron ($1 > 0$); if she goes to Hog’s Head, Hog’s Head ($2 > 0$). McGonagall: if Hagrid goes to the Leaky Cauldron, Hog’s Head ($1 > 0$); if he goes to Hog’s Head, she gets $1$ either way, so both choices are best responses and both payoffs are boxed.

**c)** (Hog’s Head, Hog’s Head) is the only cell with both payoffs boxed. Hog’s Head is never worse for McGonagall, so Hagrid can expect her there and go too.

::::
