---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# ECON 0100 | Vignette E4 | Duopoly

::: solution

# Solutions

:::

*Answers and work are shown in the red blocks.*

*Due in Recitation. Vignettes are a certificate of the work done together in Recitation.*

<!-- Editor. Answers are mine: (Low, Low); q_O = 45 - q_G/2 and q_G = 45 - q_O/2; 30 each, Q = 60, P = 40. No key for this Vignette is in the bank. In the bank’s table the firm choosing High against Low earns less (500) than its rival (1,500), the reverse of the usual output game; the numbers are kept as printed. -->

## Q1 | The Wandmaker’s Dilemma

Suppose the demand for wands is given by

$$
P = 100 - Q
$$

and there are two main wand sellers, Olivander and Gregorovitch. Olivander and Gregorovitch can make wands at a constant marginal cost of $10$. The marginal revenue for Olivander is

$$
MR_O = 100 - 2q_O - q_G
$$

and for Gregorovitch it is

$$
MR_G = 100 - 2q_G - q_O
$$

Units are in galleons and stones.

### Two Choice Game

The following table represents the profits for the two firms at a high and low output. Find the Nash equilibrium.

::: {.table style=plain inset=8pt columns="auto auto 84pt 84pt" borders=r2-3c2-3:all valign=middle spans="r0c2:2x1 r2c0:1x2"}

|   |   | **Gregorovitch** |   |
| ---: | ---: | :---: | :---: |
|   |   | High | Low |
| **Olivander** | High | 900, 900 | 500, 1500 |
|   | Low | 1500, 500 | 700, 700 |

:::

::: solution

Hold Gregorovitch’s choice fixed and compare Olivander’s profits. If Gregorovitch plays High, Olivander earns $900$ from High and $1500$ from Low, so Low. If Gregorovitch plays Low, Olivander earns $500$ from High and $700$ from Low, so Low. Low is Olivander’s best response either way, and the game is symmetric, so the same holds for Gregorovitch.

**Nash equilibrium: (Low, Low), with profits $700, 700$.** Both would earn more at (High, High), $900$ each, but each has a reason to switch to Low.

:::

### Many Choice Game

a\) Olivander’s Best Response. What is Olivander’s best response?

::: solution

Olivander sets $MR_O = MC$: $100 - 2q_O - q_G = 10$, so $q_O = 45 - \frac{1}{2} q_G$.

:::

b\) Gregorovitch’s Best Response. What is Gregorovitch’s best response?

::: solution

By the same steps, $100 - 2q_G - q_O = 10$, so $q_G = 45 - \frac{1}{2} q_O$.

:::

c\) Equilibrium Price and Quantity. What is the Nash equilibrium price and quantity in this market?

::: solution

In a Nash equilibrium both best responses hold at once. The firms are identical, so $q_O = q_G = q$: $q = 45 - \frac{1}{2} q$, so $q = 30$ each and $Q = 60$. The price comes from demand: $P = 100 - 60 = 40$.

:::

