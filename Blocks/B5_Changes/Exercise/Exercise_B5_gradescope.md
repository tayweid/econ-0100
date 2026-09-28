# Exercise B5 | Gradescope

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

## Q1: `Price Elasticity`

```
Pumpkin pasties again, $$P = 12 - Q_d/2$$ and $$P = 2 + Q_s/2$$, in galleons and pasties, with equilibrium at $$(10, 7)$$.
```

### Q1.1: `Use the midpoint method to find the elasticity of demand when the price changes from 8 to 10 galleons.`

```
(x) $$-3$$
( ) $$-1/3$$
( ) $$-2$$
( ) $$-1/2$$
```

### Q1.2: `Is demand elastic, unit elastic, or inelastic in a)?`

```
(x) Elastic
( ) Unit elastic
( ) Inelastic
```

## Q2: `Supply & Demand Shifters`

```
A subcommittee of the Ministry published a story in the Daily Profit establishing a link between the consumption of pumpkin pasties and accidental magical spell casting by wizards and witches in public areas.
```

### Q2.1: `The demand curve:`

```
(x) Shifted in
( ) Stayed the same
( ) Shifted out
```

### Q2.2: `The supply curve:`

```
( ) Shifted in
(x) Stayed the same
( ) Shifted out
```

## Q3: `Comparative Statics`

```
Pumpkin growers suddenly discover a miracle fertilizer that significantly increases harvests.
```

### Q3.1: `The equilibrium price:`

```
( ) Increased
( ) Stayed the same
(x) Decreased
```

### Q3.2: `The equilibrium quantity:`

```
(x) Increased
( ) Stayed the same
( ) Decreased
```

### Q3.3: `Without using numbers, how have these two changes together, the study and the fertilizer, impacted equilibrium price?`

```
( ) Increased
( ) Stayed the same
(x) Decreased
( ) Indeterminate
```

### Q3.4: `Without using numbers, how have these two changes together, the study and the fertilizer, impacted equilibrium quantity?`

```
( ) Increased
( ) Stayed the same
( ) Decreased
(x) Indeterminate
```

## Q4: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q4.1: `Select all that apply.`

```
[ ] The midpoint method
[ ] Elastic vs. inelastic
[ ] A movement along a curve vs. a shift of the curve
[ ] What shifts demand and supply
[ ] How a shift moves the equilibrium
[ ] Both curves shifting (indeterminate changes)
[ ] Nothing: all clear
```
