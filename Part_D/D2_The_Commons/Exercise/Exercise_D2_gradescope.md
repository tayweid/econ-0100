# Exercise D2 | Gradescope

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

## Q1: `The Fishing Game`

```
See Q1 | The Fishing Game on the Exercise D2 handout. Firm 1 and Firm 2 each commit to Low Catch (L), one quarter of each month’s starting stock, or High Catch (H), one half, for three months. Both harvest from the same starting stock, initially 20,000 fish; survivors double after each harvest, up to 20,000 fish. Total three-month catches in thousands of fish, listed (Firm 1, Firm 2): (L, L) 15, 15; (L, H) 8.75, 17.5; (H, L) 17.5, 8.75; (H, H) 10, 10.
```

### Q1.1: `Firm 1's best response if Firm 2 chooses L:`

```
( ) L
(x) H
```

### Q1.2: `Firm 1's best response if Firm 2 chooses H:`

```
( ) L
(x) H
```

### Q1.3: `Firm 2's best response if Firm 1 chooses L:`

```
( ) L
(x) H
```

### Q1.4: `Firm 2's best response if Firm 1 chooses H:`

```
( ) L
(x) H
```

### Q1.5: `Find all Nash Equilibrium (Firm 1, Firm 2). Select all that apply.`

```
[ ] (L, L)
[ ] (L, H)
[ ] (H, L)
[x] (H, H)
```

### Q1.6: `Find the socially efficient strategies (Firm 1, Firm 2).`

```
(x) (L, L)
( ) (L, H)
( ) (H, L)
( ) (H, H)
```

## Q2: `The Fishing Game, Firm 1 Moves First`

```
See Q2 | The Fishing Game, Firm 1 Moves First on the Exercise D2 handout. Firm 1 commits to its three-month strategy first and Firm 2 sees that choice before committing. Both firms still harvest from the same starting stock each month. Total three-month catches in thousands of fish are the same as in Q1, listed (Firm 1, Firm 2): (L, L) 15, 15; (L, H) 8.75, 17.5; (H, L) 17.5, 8.75; (H, H) 10, 10.
```

### Q2.1: `If Firm 1 chooses L, Firm 2 chooses:`

```
( ) L
(x) H
```

### Q2.2: `If Firm 1 chooses H, Firm 2 chooses:`

```
( ) L
(x) H
```

### Q2.3: `Working backward, Firm 1 chooses:`

```
( ) L
(x) H
```

### Q2.4: `The outcome of the game (Firm 1, Firm 2):`

```
( ) (L, L)
( ) (L, H)
( ) (H, L)
(x) (H, H)
```

### Q2.5: `What does each firm catch over the three months (in thousands of fish)?`

```
Firm 1:
[____](=10+-0)

Firm 2:
[____](=10+-0)
```

### Q2.6: `Does moving first change the outcome from the Nash Equilibrium in Q1?`

```
( ) Yes
(x) No
```

### Q2.7: `Which firm has the higher payoff?`

```
( ) Firm 1
( ) Firm 2
(x) Neither; both have the same payoff
```
