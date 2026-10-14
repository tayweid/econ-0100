# Exercise C3 | Gradescope

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

## Q1: `Policy Proposal`

```
Smoked toffee, with demand $$P_B = 20 - \frac{1}{2} Q_D$$ and supply $$P_S = 2 + Q_S$$, in Galleons. Wood smoke from production imposes an external cost of 3 Galleons per unit of smoked toffee on Hogsmeade residents.

What type and size of policy would you propose to eliminate the deadweight loss from the wood smoke?
```

### Q1.1: `Policy Type:`

```
(x) Tax
( ) Subsidy
( ) Price ceiling
( ) Price floor
```

### Q1.2: `Policy Size:`

```
( ) $$1$$ Galleons
( ) $$2$$ Galleons
(x) $$3$$ Galleons
( ) $$6$$ Galleons
```

### Q1.3: `Buyer Price:`

```
( ) $$12$$ Galleons
( ) $$14$$ Galleons
(x) $$15$$ Galleons
( ) $$17$$ Galleons
```

### Q1.4: `Seller Price:`

```
( ) $$11$$ Galleons
(x) $$12$$ Galleons
( ) $$14$$ Galleons
( ) $$15$$ Galleons
```

### Q1.5: `Post-Policy Quantity:`

```
( ) $$8$$ toffees
(x) $$10$$ toffees
( ) $$12$$ toffees
( ) $$14$$ toffees
```

## Q2: `Deadweight Loss Intuition`

```
If the marginal cost of a gallon of gas is $$\$4.00$$, the negative externality is $$\$1.00$$, and the marginal benefit is $$\$4.50$$, what is the deadweight loss?
```

### Q2.1: `Deadweight Loss:`

```
( ) $$\$0$$
(x) $$\$0.50$$
( ) $$\$1.00$$
( ) $$\$1.50$$
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Choosing a corrective policy
[ ] Sizing a corrective tax
[ ] Buyer and seller prices with a corrective tax
[ ] Deadweight loss from a single exchange
[ ] Nothing: all clear
```
