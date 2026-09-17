# Exercise B1 | Gradescope

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

## Q1: `Quantity Demanded`

```
Pumpkin pasties sell along the demand curve $$P = 12 - Q/2$$, in galleons and pasties.
```

### Q1.1: `What is the quantity demanded at 10 galleons?`

```
( ) $$2$$ pasties
(x) $$4$$ pasties
( ) $$7$$ pasties
( ) $$10$$ pasties
```

### Q1.2: `What is the marginal benefit at a quantity of 4?`

```
( ) $$4$$ galleons per pasty
( ) $$8$$ galleons per pasty
(x) $$10$$ galleons per pasty
( ) $$12$$ galleons per pasty
```

## Q2: `Consumer Surplus`

```
Pumpkin pasties again, $$P = 12 - Q/2$$, in galleons and pasties.
```

### Q2.1: `What is the quantity demanded at 5 galleons?`

```
( ) $$7$$ pasties
( ) $$9.5$$ pasties
(x) $$14$$ pasties
( ) $$24$$ pasties
```

### Q2.2: `Which area should be labeled consumer surplus at that price, and what is its value?`

```
( ) The rectangle below the price of $$5$$, from $$Q = 0$$ to $$Q = 14$$: $$70$$ galleons
( ) The entire area below demand, from $$Q = 0$$ to $$Q = 14$$: $$119$$ galleons
(x) The triangle below demand and above the price of $$5$$, from $$Q = 0$$ to $$Q = 14$$: $$49$$ galleons
( ) The triangle below demand and above the price of $$5$$, from $$Q = 0$$ to $$Q = 14$$: $$98$$ galleons
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Demand and quantity demanded
[ ] Marginal benefit
[ ] Consumer surplus
[ ] Market demand
[ ] Nothing: all clear
```
