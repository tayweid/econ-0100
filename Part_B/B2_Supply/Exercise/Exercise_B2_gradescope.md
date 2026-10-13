# Exercise B2 | Gradescope

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

## Q1: `Quantity Supplied`

```
Pumpkin pasties are produced by many sellers according to the supply curve $$P = 2 + Q_s/10$$, in galleons and pasties.
```

### Q1.1: `What is quantity supplied at 10 galleons?`

```
( ) $$8$$ pasties
(x) $$80$$ pasties
( ) $$100$$ pasties
( ) $$120$$ pasties
```

### Q1.2: `What is marginal cost at 9 pasties?`

```
( ) $$0.9$$ galleons per pasty
(x) $$2.9$$ galleons per pasty
( ) $$9$$ galleons per pasty
( ) $$11$$ galleons per pasty
```

## Q2: `Producer Surplus`

```
Pumpkin pasties again, $$P = 2 + Q_s/10$$, in galleons and pasties.
```

### Q2.1: `Which area should be labeled producer surplus at 10 galleons, and what is its value?`

```
( ) The rectangle below the price of $$10$$, from $$Q = 0$$ to $$Q = 80$$: $$800$$ galleons
( ) The area below the supply curve, from $$Q = 0$$ to $$Q = 80$$: $$480$$ galleons
(x) The triangle above the supply curve and below the price of $$10$$, from $$Q = 0$$ to $$Q = 80$$: $$320$$ galleons
( ) The triangle above the supply curve and below the price of $$10$$, from $$Q = 0$$ to $$Q = 80$$: $$640$$ galleons
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Supply and quantity supplied
[ ] Marginal cost
[ ] Producer surplus
[ ] Market supply
[ ] Nothing: all clear
```
