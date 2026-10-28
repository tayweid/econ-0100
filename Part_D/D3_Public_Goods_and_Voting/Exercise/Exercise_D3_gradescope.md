# Exercise D3 | Gradescope

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

## Q1: `The Dumbledore Memorial`

```
See Q1 | The Dumbledore Memorial on the Exercise D3 handout. Marginal benefits: Aurelius 75, Aberforth 10, Ariana 20. The memorial costs 90 coins per year to operate and maintain.
```

### Q1.1: `How many of the three Dumbledores would visit the memorial if it were built?`

```
( ) $$0$$
( ) $$1$$
( ) $$2$$
(x) $$3$$
```

### Q1.2: `How many Dumbledores will contribute to the memorial's continued operation after the endowment runs out?`

```
(x) $$0$$
( ) $$1$$
( ) $$2$$
( ) $$3$$
```

### Q1.3: `Would the 30 coin referendum receive a majority vote?`

```
( ) Yes
(x) No
```

### Q1.4: `What is the marginal social benefit from the memorial?`

```
( ) $$75$$ coins
( ) $$90$$ coins
(x) $$105$$ coins
( ) $$135$$ coins
```

### Q1.5: `If the referendum passed, would it lead to an efficient outcome?`

```
(x) Yes
( ) No
```

## Q2: `A Memorial to Dobby`

```
See Q2 | A Memorial to Dobby on the Exercise D3 handout. Marginal benefits: Harry 34, Ron 29, Hermione 24, Ginny 19, Neville 14. The memorial costs 100 coins per year to operate and maintain.
```

### Q2.1: `How many of the five residents would visit the memorial if it were built?`

```
( ) $$0$$
( ) $$3$$
( ) $$4$$
(x) $$5$$
```

### Q2.2: `Would the 20 coin referendum receive a majority vote?`

```
(x) Yes
( ) No
```

### Q2.3: `What is the marginal social benefit from the memorial?`

```
( ) $$34$$ coins
( ) $$100$$ coins
(x) $$120$$ coins
( ) $$170$$ coins
```

### Q2.4: `Would the 20 coin referendum lead to an efficient outcome?`

```
(x) Yes
( ) No
```

### Q2.5: `Would the proposal receive a majority vote if the tax were 25 coins?`

```
( ) Yes
(x) No
```

### Q2.6: `Could a private company cover its costs with a single admission fee?`

```
( ) Yes
(x) No
```
