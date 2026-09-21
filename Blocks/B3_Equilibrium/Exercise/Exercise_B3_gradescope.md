# Exercise B3 | Gradescope

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

## Q1: `Equilibrium`

```
Pumpkin pasties are bought and sold in a market with demand curve $$P = 12 - Q_d/2$$ and supply curve $$P = 2 + Q_s/2$$, in galleons and pasties.
```

### Q1.1: `What is the equilibrium quantity?`

```
( ) $$5$$ pasties
(x) $$10$$ pasties
( ) $$14$$ pasties
( ) $$20$$ pasties
```

### Q1.2: `What is the equilibrium price?`

```
( ) $$5$$ galleons
( ) $$6$$ galleons
(x) $$7$$ galleons
( ) $$12$$ galleons
```

### Q1.3: `Where does the star go on your graph?`

```
( ) A star at $$(7, 10)$$
(x) A star at $$(10, 7)$$, where the two curves cross
( ) Two stars, at the intercepts $$(0, 12)$$ and $$(0, 2)$$
( ) A star at $$(20, 12)$$, where the two curves end
```

## Q2: `A Price Away from Equilibrium`

```
Pumpkin pasties again, $$P = 12 - Q_d/2$$ and $$P = 2 + Q_s/2$$. Suppose the price is 5 galleons.
```

### Q2.1: `What is the quantity demanded?`

```
( ) $$6$$ pasties
( ) $$7$$ pasties
(x) $$14$$ pasties
( ) $$24$$ pasties
```

### Q2.2: `What is the quantity supplied?`

```
( ) $$3$$ pasties
(x) $$6$$ pasties
( ) $$10$$ pasties
( ) $$14$$ pasties
```

### Q2.3: `Is this a shortage or an excess, and how large?`

```
(x) A shortage of $$8$$ pasties
( ) An excess of $$8$$ pasties
( ) A shortage of $$14$$ pasties
( ) An excess of $$6$$ pasties
```

### Q2.4: `Which way will the price move?`

```
(x) It will rise: buyers who can’t get pasties and sellers with willing buyers both push it up
( ) It will fall: sellers can’t sell everything they’ve baked
( ) It will stay at 5 galleons: prices only move when the curves shift
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Equilibrium price and quantity
[ ] Solving supply equals demand
[ ] Shortage
[ ] Excess
[ ] Why the price returns (stability)
[ ] Nothing: all clear
```
