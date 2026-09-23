# Exercise B4 | Gradescope

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

## Q1: `A Price Ceiling`

```
Pumpkin pasties again, $$P = 12 - Q_d/2$$ and $$P = 2 + Q_s/2$$, in galleons and pasties, with equilibrium at $$(10, 7)$$. The government sets a maximum legal price of 5 galleons. From Exercise B3: at 5 galleons, quantity demanded is $$14$$ and quantity supplied is $$6$$.
```

### Q1.1: `How many pasties are exchanged?`

```
( ) $$14$$ pasties
(x) $$6$$ pasties
( ) $$10$$ pasties
( ) $$8$$ pasties
```

### Q1.2: `What is consumer surplus?`

```
( ) $$25$$ galleons
(x) $$33$$ galleons
( ) $$21$$ galleons
( ) $$49$$ galleons
```

### Q1.3: `What is producer surplus?`

```
(x) $$9$$ galleons
( ) $$25$$ galleons
( ) $$33$$ galleons
( ) $$18$$ galleons
```

### Q1.4: `What is deadweight loss?`

```
(x) $$8$$ galleons
( ) $$2$$ galleons
( ) $$4$$ galleons
( ) $$16$$ galleons
```

### Q1.5: `Which shading matches your graph?`

```
(x) CS between the demand curve and the 5-galleon line out to $$Q = 6$$; PS between the 5-galleon line and the supply curve out to $$Q = 6$$; DWL between the two curves from $$Q = 6$$ to $$Q = 10$$
( ) CS and PS split at the 7-galleon equilibrium price, out to $$Q = 10$$, with no deadweight loss
( ) CS out to $$Q = 14$$, since that is the quantity demanded at 5 galleons
( ) DWL between the two curves from $$Q = 0$$ to $$Q = 6$$
```

## Q2: `A Price Floor`

```
Same pasty market. Suppose instead the government sets a minimum legal price of 9 galleons. Now quantity demanded is $$6$$ and quantity supplied is $$14$$.
```

### Q2.1: `How many pasties are exchanged?`

```
(x) $$6$$ pasties
( ) $$14$$ pasties
( ) $$10$$ pasties
( ) $$8$$ pasties
```

### Q2.2: `What is producer surplus?`

```
(x) $$33$$ galleons
( ) $$9$$ galleons
( ) $$25$$ galleons
( ) $$49$$ galleons
```

### Q2.3: `What is deadweight loss?`

```
(x) $$8$$ galleons
( ) $$0$$ galleons
( ) $$4$$ galleons
( ) $$16$$ galleons
```

### Q2.4: `Would a floor of 6 galleons change the market?`

```
(x) No: 6 galleons is below the equilibrium price of 7, so the market still reaches equilibrium — the floor is not binding
( ) Yes: the price would fall to 6 galleons
( ) Yes: an excess would appear
( ) Yes: the quantity exchanged would rise
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Binding vs. non-binding price controls
[ ] Quantity exchanged (the short side)
[ ] Consumer and producer surplus under a control
[ ] Deadweight loss
[ ] The First Welfare Theorem
[ ] Nothing: all clear
```
