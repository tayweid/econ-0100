# Exercise C2 | Gradescope

This is an instructor-facing document to make it easy to enter questions into Gradescope. This sheet is the selection form students submit on Gradescope after completing their work in class, taken from the Exercise file (the .typ handout).

- Each `## QN` is a parent question. Put its title in the title field and paste its block into the Description box. A parent question can only hold description text; students answer the sub-questions.

- Each `### QN.M` under it is a sub-question. Put its title in the sub-question’s title field and paste its block into the **Problem** box.

- Ignore points. Each sub-question is worth 1 point by default on Gradescope.

Gradescope parses the code directly. Every input field must sit on its own line with no text before or after it, and a question can hold several fields:

- Text is Markdown, and LaTeX goes between `$$`. Images can be inserted with **Insert Image** or as a Markdown link `![alt](url)` to a file on the course site.
- Multiple choice: consecutive `( )` lines become a multiple-choice field, with `(x)` marking the correct answer. A blank line between choices starts a new group.
- Select all: consecutive `[ ]` lines become a select-all field, with `[x]` marking each correct answer. Students must mark every correct answer to get the point.
- Short answer: `[____](answer)` gives a one-line text box, autograded against the answer in parentheses. For numbers, `[____](=2+-0)` accepts any equivalent of 2 and `[____](=2+-0.2)` accepts anything from 1.8 to 2.2. Leave the parentheses empty to grade by hand.
- Free response: `|____|` gives a multi-paragraph text box. Any question with one is graded by hand.
- File uploads: `|files|` lets students upload any file type (a PNG of a figure, a notebook, a PDF). Uploads can be viewed and graded but not annotated.

## Q1: `One Toffee Exchange`

```
Smoked toffee, with demand $$P_B = 20 - \frac{1}{2} Q_D$$ and supply $$P_S = 2 + Q_S$$, in Galleons. The Ministry of Magic imposes a 3 Galleon tax on the sale of smoked toffee.

A buyer values one smoked toffee at 16 Galleons. It costs the seller 12 Galleons to make.
```

### Q1.1: `Without the tax, will the buyer and seller make this exchange?`

```
(x) Yes
( ) No
```

### Q1.2: `With the tax, will the buyer and seller make this exchange?`

```
(x) Yes
( ) No
```

### Q1.3: `Total Surplus to the buyer and seller, with the tax:`

```
( ) $$0$$ Galleons
(x) $$1$$ Galleons
( ) $$3$$ Galleons
( ) $$4$$ Galleons
```

### Q1.4: `Tax paid to the Ministry of Magic:`

```
( ) $$0$$ Galleons
( ) $$1$$ Galleons
(x) $$3$$ Galleons
( ) $$4$$ Galleons
```

### Q1.5: `Total Surplus, including the Ministry of Magic:`

```
( ) $$1$$ Galleons
( ) $$3$$ Galleons
(x) $$4$$ Galleons
( ) $$7$$ Galleons
```

## Q2: `Another Exchange`

```
Smoked toffee, with demand $$P_B = 20 - \frac{1}{2} Q_D$$ and supply $$P_S = 2 + Q_S$$, in Galleons. The Ministry of Magic imposes a 3 Galleon tax on the sale of smoked toffee.

Another buyer values one smoked toffee at 14 Galleons. It costs the seller 12 Galleons to make.
```

### Q2.1: `Without the tax, will the buyer and seller make this exchange?`

```
(x) Yes
( ) No
```

### Q2.2: `With the tax, will the buyer and seller make this exchange?`

```
( ) Yes
(x) No
```

### Q2.3: `Deadweight Loss from losing this exchange:`

```
( ) $$0$$ Galleons
( ) $$1$$ Galleons
(x) $$2$$ Galleons
( ) $$3$$ Galleons
```

## Q3: `Tax Equilibrium`

```
Smoked toffee, with demand $$P_B = 20 - \frac{1}{2} Q_D$$ and supply $$P_S = 2 + Q_S$$, in Galleons. The Ministry of Magic imposes a 3 Galleon tax on the sale of smoked toffee.
```

### Q3.1: `Pre-Tax Price:`

```
( ) $$12$$ Galleons
(x) $$14$$ Galleons
( ) $$15$$ Galleons
( ) $$16$$ Galleons
```

### Q3.2: `Pre-Tax Quantity:`

```
( ) $$10$$ toffees
(x) $$12$$ toffees
( ) $$14$$ toffees
( ) $$16$$ toffees
```

### Q3.3: `Post-Tax Quantity:`

```
( ) $$8$$ toffees
(x) $$10$$ toffees
( ) $$12$$ toffees
( ) $$14$$ toffees
```

### Q3.4: `DWL:`

```
( ) $$1$$ Galleons
( ) $$2$$ Galleons
(x) $$3$$ Galleons
( ) $$4$$ Galleons
```

### Q3.5: `Buyer Price:`

```
( ) $$12$$ Galleons
( ) $$14$$ Galleons
(x) $$15$$ Galleons
( ) $$17$$ Galleons
```

### Q3.6: `Seller Price:`

```
( ) $$11$$ Galleons
(x) $$12$$ Galleons
( ) $$14$$ Galleons
( ) $$15$$ Galleons
```

### Q3.7: `Tax Incidence on Buyers:`

```
( ) $$0$$ Galleons
(x) $$1$$ Galleons
( ) $$2$$ Galleons
( ) $$3$$ Galleons
```

### Q3.8: `Tax Incidence on Sellers:`

```
( ) $$1$$ Galleons
(x) $$2$$ Galleons
( ) $$3$$ Galleons
( ) $$4$$ Galleons
```

### Q3.9: `Who bears more of the tax?`

```
( ) Buyers
(x) Sellers
( ) Equal
```

## Q4: `Subsidy Equilibrium`

```
Smoked toffee, with demand $$P_B = 20 - \frac{1}{2} Q_D$$ and supply $$P_S = 2 + Q_S$$, in Galleons. There is no tax. Instead, the Ministry of Magic pays a 3 Galleon subsidy on every smoked toffee sold.
```

### Q4.1: `Post-Subsidy Quantity:`

```
( ) $$10$$ toffees
( ) $$12$$ toffees
(x) $$14$$ toffees
( ) $$16$$ toffees
```

### Q4.2: `DWL:`

```
( ) $$1$$ Galleons
(x) $$3$$ Galleons
( ) $$6$$ Galleons
( ) $$9$$ Galleons
```

### Q4.3: `Buyer Price:`

```
( ) $$11$$ Galleons
( ) $$12$$ Galleons
(x) $$13$$ Galleons
( ) $$14$$ Galleons
```

### Q4.4: `Seller Price:`

```
( ) $$13$$ Galleons
( ) $$14$$ Galleons
(x) $$16$$ Galleons
( ) $$17$$ Galleons
```

## Q5: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q5.1: `Select all that apply.`

```
[ ] Surplus and DWL of a single exchange with a tax
[ ] Buyer and seller prices with a tax
[ ] Tax incidence
[ ] Buyer and seller prices with a subsidy
[ ] DWL from a subsidy
[ ] Nothing: all clear
```
