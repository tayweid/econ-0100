# Exercise A3 | Gradescope

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

## Q1: `Specialization`

```
Hagrid can bake $$20$$ rock cakes ($$R$$) or $$30$$ fruitcakes ($$F$$) in one day and Professor McGonagall can bake $$10$$ rock cakes or $$5$$ fruitcakes in one day. Like we found in Exercise A2, Hagrid has the comparative advantage in fruitcakes and McGonagall in rock cakes. How much does each baker produce in one day if they specialize accordingly?
```

### Q1.1: `Hagrid`

```
( ) $$20$$ rock cakes
(x) $$30$$ fruitcakes
( ) $$20$$ rock cakes and $$30$$ fruitcakes
( ) $$15$$ fruitcakes
```

### Q1.2: `McGonagall`

```
(x) $$10$$ rock cakes
( ) $$5$$ fruitcakes
( ) $$10$$ rock cakes and $$5$$ fruitcakes
( ) $$20$$ rock cakes
```

## Q2: `Trade`

```
Suppose Hagrid and McGonagall decide they want to specialize and trade goods.
```

### Q2.1: `After they specialize, what is a trade that would make them both better off? 1 R for:`

```
( ) $$1/4$$ fruitcake
(x) $$1$$ fruitcake
( ) $$3/2$$ fruitcakes
( ) $$2$$ fruitcakes
```

## Q3: `Workable Rates`

```
Not every exchange rate works for both bakers.
```

### Q3.1: `What is the range of exchange rates that would make both Hagrid and McGonagall better off?`

```
( ) Between $$2/3$$ and $$2$$ fruitcakes per rock cake
(x) Between $$1/2$$ and $$3/2$$ fruitcakes per rock cake
( ) Between $$5$$ and $$30$$ fruitcakes per rock cake
( ) Any rate: trade always makes both better off
```

## Q4: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q4.1: `Select all that apply.`

```
[ ] Pareto improvement
[ ] Initial endowment
[ ] The trade line
[ ] Workable exchange rates
[ ] Specialization
[ ] Nothing: all clear
```
