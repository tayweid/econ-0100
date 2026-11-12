# Exercise E2 | Gradescope

This is an instructor-facing document to make it easy to enter questions into Gradescope. This sheet is the selection form students submit on Gradescope after completing their work in class, taken from the Exercise file (the .md handout).

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

## Q1: `Choosing Quantity`

```
Use Q1 on the handout. The animation’s competitive firm has cost functions TC = 1000 + q^2 and MC = 2q. The market price is P = 80. Hint: ATC at the profit-maximizing quantity is 65.
```

### Q1.1: `a) Total Revenue from selling 20 units:`

```
[____](=1600+-0)
```

### Q1.2: `a) Total Revenue selling 21 units:`

```
[____](=1680+-0)
```

### Q1.3: `a) Marginal Revenue:`

```
[____](=80+-0)
```

### Q1.4: `b) The firm’s best quantity at P = 80:`

```
[____](=40+-0)
```

### Q1.5: `c) The firm’s maximal profit:`

```
[____](=600+-0)
```

## Q2: `Operating or Leaving`

```
Use Q2 on the handout. At a price of 40, the firm’s best positive output is 20 units. Fixed cost of 1,000 is unavoidable this period but avoidable in future periods by leaving the industry. Hint: ATC at the profit-maximizing quantity is 70. Enter a loss as a negative number.
```

### Q2.1: `a) Profit from operating this period (a loss is negative):`

```
[____](=-600+-0)
```

### Q2.2: `b) Profit from shutting down this period (a loss is negative):`

```
[____](=-1000+-0)
```

### Q2.3: `c) Should the firm operate or shut down this period?`

```
(x) Operate: lose 600 instead of losing 1000 by shutting down
( ) Shut down: any loss means the firm should stop producing
( ) Operate: the firm earns a profit of 600
```

### Q2.4: `d) In the long run at this price, should the firm exit?`

```
(x) Yes: exit once future fixed costs can be avoided
( ) No: stay because price covers variable costs
( ) No: stay because fixed costs can never be avoided
```

### Q2.5: `e) In the long run, how does supply and price change?`

```
( ) Entry increases market supply and lowers price
(x) Exit decreases market supply and raises price
( ) Entry decreases market supply and raises price
```

## Q3: `A Higher Marginal Cost`

```
Use Q3 and your graphs. After being in long run equilibrium, suppose every firm’s marginal costs go up. Every unit now costs the same additional amount to produce.
```

### Q3.1: `a) What happens to price, each firm’s output, and profit after the new cost?`

```
(x) Market supply shifts in; price rises, output per firm falls, and firms make losses
( ) Price and output stay unchanged; only fixed cost rises
( ) Price rises by the full extra cost per unit, so profit immediately stays zero
```

### Q3.2: `b) What happens to the long run price, each firm’s output, market output, and the number of firms? Select all that apply.`

```
[x] The market price is higher
[ ] Each surviving firm produces more than before the cost increase
[x] Each surviving firm returns to its original output
[x] Total market output is lower
[x] There are fewer firms
```
