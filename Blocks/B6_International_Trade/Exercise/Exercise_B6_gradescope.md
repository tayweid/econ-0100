# Exercise B6 | Gradescope

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

## Q1: `Unlocking the Magic`

```
Pumpkin pasties, $$P = 12 - Q_d/2$$ and $$P = 2 + Q_s/2$$, in galleons and pasties, with equilibrium at $$(10, 7)$$. The world price is $$5$$ galleons.
```

### Q1.1: `Does the market import or export pasties?`

```
(x) Imports
( ) Exports
```

### Q1.2: `How many pasties are imported?`

```
( ) $$4$$
( ) $$6$$
(x) $$8$$
( ) $$14$$
```

### Q1.3: `Consumer surplus after trade:`

```
( ) $$25$$
( ) $$36$$
(x) $$49$$
( ) $$64$$
```

### Q1.4: `Producer surplus after trade:`

```
(x) $$9$$
( ) $$16$$
( ) $$25$$
( ) $$36$$
```

### Q1.5: `Change in total surplus:`

```
( ) $$-8$$
( ) $$0$$
(x) $$+8$$
( ) $$+16$$
```

## Q2: `An Alternative World`

```
Now the world price is $$9$$ galleons.
```

### Q2.1: `Does the market import or export pasties?`

```
( ) Imports
(x) Exports
```

### Q2.2: `Who gains from opening the market?`

```
( ) Buyers
(x) Sellers
( ) Neither
```

