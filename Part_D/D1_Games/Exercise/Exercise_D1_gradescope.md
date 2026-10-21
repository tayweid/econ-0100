# Exercise D1 | Gradescope

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

## Q1: `Study Room Dynamics`

```
See Q1 on the Exercise D1 handout. Ravenclaw and Hufflepuff share a study room, and each house chooses whether to clean. Payoffs are listed Ravenclaw first, Hufflepuff second.

$$\begin{array}{r|c|c} & \text{Hufflepuff: Clean} & \text{Hufflepuff: Don't Clean} \\ \hline \text{Ravenclaw: Clean} & 10,\ 10 & 6,\ 12 \\ \hline \text{Ravenclaw: Don't Clean} & 12,\ 6 & 8,\ 8 \end{array}$$
```

### Q1.1: `What is Ravenclaw’s best response?`

```
( ) Clean, whatever Hufflepuff does
(x) Don't Clean, whatever Hufflepuff does
( ) Clean if Hufflepuff cleans; Don't Clean if Hufflepuff doesn't
( ) Don't Clean if Hufflepuff cleans; Clean if Hufflepuff doesn't
```

### Q1.2: `What is Hufflepuff’s best response?`

```
( ) Clean, whatever Ravenclaw does
(x) Don't Clean, whatever Ravenclaw does
( ) Clean if Ravenclaw cleans; Don't Clean if Ravenclaw doesn't
( ) Don't Clean if Ravenclaw cleans; Clean if Ravenclaw doesn't
```

### Q1.3: `Identify each house’s dominant strategy if one exists.`

```
( ) Clean, for both houses
(x) Don't Clean, for both houses
( ) Clean for Ravenclaw; Don't Clean for Hufflepuff
( ) Neither house has a dominant strategy
```

### Q1.4: `Find all Nash Equilibrium.`

```
Select all that apply, Ravenclaw's choice first.

[ ] (Clean, Clean)
[ ] (Clean, Don't Clean)
[ ] (Don't Clean, Clean)
[x] (Don't Clean, Don't Clean)
```

### Q1.5: `Find the socially efficient strategies.`

```
Select all that apply, Ravenclaw's choice first.

[x] (Clean, Clean)
[ ] (Clean, Don't Clean)
[ ] (Don't Clean, Clean)
[ ] (Don't Clean, Don't Clean)
```

## Q2: `Date Night`

```
See Q2 on the Exercise D1 handout. Hagrid and McGonagall each choose the Leaky Cauldron or Hog's Head without talking first. Hagrid gets 2 if they are together at Hog's Head, 1 if they are together at the Leaky Cauldron, and 0 if he is alone. McGonagall gets 1 at Hog's Head with or without Hagrid, 1 at the Leaky Cauldron alone, and 0 at the Leaky Cauldron with Hagrid.

Write outcomes as (Hagrid's choice, McGonagall's choice), with LC for the Leaky Cauldron and HH for Hog's Head.
```

### Q2.1: `Hagrid’s payoffs`

```
Hagrid's payoffs at (LC, LC), (LC, HH), (HH, LC), (HH, HH), in that order:

(x) $$1, 0, 0, 2$$
( ) $$2, 0, 0, 1$$
( ) $$1, 1, 0, 2$$
( ) $$0, 1, 1, 2$$
```

### Q2.2: `McGonagall’s payoffs`

```
McGonagall's payoffs at (LC, LC), (LC, HH), (HH, LC), (HH, HH), in that order:

(x) $$0, 1, 1, 1$$
( ) $$1, 1, 0, 1$$
( ) $$0, 1, 0, 1$$
( ) $$1, 0, 0, 2$$
```

### Q2.3: `Hagrid’s best responses`

```
(x) LC if McGonagall goes to LC; HH if she goes to HH
( ) HH, wherever McGonagall goes
( ) LC, wherever McGonagall goes
( ) HH if McGonagall goes to LC; LC if she goes to HH
```

### Q2.4: `McGonagall’s best responses`

```
(x) HH if Hagrid goes to LC; either location if he goes to HH
( ) LC if Hagrid goes to LC; HH if he goes to HH
( ) HH if Hagrid goes to LC; LC if he goes to HH
( ) LC, wherever Hagrid goes
```

### Q2.5: `Find the Nash Equilibrium.`

```
Select all that apply.

[ ] (LC, LC)
[ ] (LC, HH)
[ ] (HH, LC)
[x] (HH, HH)
```

### Q2.6: `Since they couldn’t communicate, could they use this to figure out which location to go?`

```
(x) Yes: (HH, HH) is the only Nash equilibrium, so both go to Hog's Head
( ) Yes: both go to the Leaky Cauldron
( ) No: there are two Nash equilibria, so neither knows which to expect
( ) No: there is no Nash equilibrium
```

## Q3: `Which concepts?`

Gradescope-only: not on the printed exercise. Graded by hand for completion, so any response earns the point.

```
Which concepts (if any) from this block would you want explained in more detail in lecture or recitation?
```

### Q3.1: `Select all that apply.`

```
[ ] Best responses
[ ] Dominant strategies
[ ] Nash equilibrium
[ ] Social efficiency
[ ] Setting up a payoff matrix from a story
[ ] Nothing: all clear
```
