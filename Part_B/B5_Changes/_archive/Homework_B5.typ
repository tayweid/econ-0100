// Exported from Plass
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show heading.where(level: 4): set text(size: 14.375pt)
#show heading.where(level: 4): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 4): set par(leading: 8.153pt)
#show heading.where(level: 5): set text(size: 14.375pt)
#show heading.where(level: 5): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 5): set par(leading: 8.153pt)
#show heading.where(level: 6): set text(size: 14.375pt)
#show heading.where(level: 6): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 6): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#import "@preview/mitex:0.2.5": mi, mitex

= ECON0100 | Homework B5 | Market Changes

_Due: Sunday, Oct. 4_

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely, and show your work so you can later understand your thought process. You are welcomed and encouraged to work in groups as long as your work is your own. Submit your answers on Gradescope when you’re finished: each answer there is a selection.

== Butterbeer

Preferences for butter beer can be represented by the following demand curve:

#mitex(`
P = 100 - \frac{1}{2} Q_D
`)

The marginal cost of butter beer can be represented by the following equation:

#mitex(`
P = 20 + \frac{1}{2} Q_S
`)

Prices are in galleons and quantity is in bottles.

== Q1 | Price Elasticity

a) What is the price elasticity of demand when the price changes from 10 to 30? \_\_\_\_\_\_\_\_\_\_

b) What is the price elasticity of demand when the price changes from 40 to 60? \_\_\_\_\_\_\_\_\_\_

c) What is the price elasticity of demand when the price changes from 70 to 90? \_\_\_\_\_\_\_\_\_\_

d) Is demand elastic, unit elastic, or inelastic in a), b), and c)?

e) What is the price elasticity of supply when the price changes from 40 to 60? \_\_\_\_\_\_\_\_\_\_

== Q2 | Supply & Demand Shifters

For each change below, which curve in the butter beer market shifts, and in which direction?

a) Wages rise across the wizarding world, and butter beer is a normal good.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

b) Wages rise across the wizarding world, and butter beer is an inferior good.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

c) The price of pumpkin juice, which wizards drink instead of butter beer, rises.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

d) The price of the pumpkin pasties that wizards eat with their butter beer rises.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

e) The rent on brewing cellars in Hogsmeade rises.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

f) A new brewing charm lets brewers make each batch in half the time.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

g) The price of firewhisky, which brewers could make instead, rises.

_#mi(`\hspace{1cm}`)demand shifts up · demand shifts down · supply shifts up · supply shifts down_

#pagebreak()

== Q3 | Comparative Statics

Butter beer has culturally been associated with a good time. This all changed when a high profile wizard went viral slamming the taste. At the same time an ingredient of the drink, butter extract, became incredibly difficult for butter beer makers to acquire. Use a graph to discuss the effect these two events had on the butter beer market.

a) Due to the viral post, the demand curve: _shifted up · stayed the same · shifted down_

b) Due to the butter extract shortage, the supply curve: _shifted up · stayed the same · shifted down_

c) Without using numbers, how did the two events together change the market?

#mi(`\hspace{1cm}`)Prices: _increased · stayed the same · decreased · indeterminate_

#mi(`\hspace{1cm}`)Quantity: _increased · stayed the same · decreased · indeterminate_

~

~

~

~

~

~

~

d) Use numbers to compare the new equilibrium to the original one. After both events, the supply and demand curves became:

#mitex(`
P = 30 + \frac{1}{2} Q_S \ \ \text{and} \ \ P = 80 - \frac{1}{2} Q_D
`)

~

What is the change in equilibrium price? \_\_\_\_\_\_\_\_\_\_ 

What is the change in equilibrium quantity? \_\_\_\_\_\_\_\_\_\_
