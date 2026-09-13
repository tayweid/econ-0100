<!-- renamed from 21F_Homework_2.md -->
<!-- from extract-past-semester-assessments: Part_B/Homework_B/21F_Homework_2.md | filed by: high: doc+topic agree on Q1 -->
## ECON 0100 | Fall 2021

### Homework 2

Homework is designed to both test your knowlege and challenge you to apply familiar concepts in new applications. Send me your questions at taylorjweidman@pitt.edu. Answer clearly and completely; show your work so I can understand your thought process for partial credit; you are welcomed and encouraged to work in groups as long as your work is your own.

#### Act 1

Wizards and witches tend to enjoy pumpkin pasties for the nostalgic taste, with preferences represented by the following demand curve:

$$ P_b = 17 - \frac{ 1 }{ 6 } Q_d $$

Use the midpoint method to find the elasticity of demanded when the price changes from $5$ to $10$ galleons.

*(figure: graph_paper.png)*

Elasticity of Demand:__________

##### Solution

First lets find the following pieces:

$$\Delta Q =  Q_1 - Q_2 = 72.0 - 42.0 = 30.0$$

$$\bar{Q} = \frac{Q_1 - Q_2}{2} = \frac{ 72.0 + 42.0 }{2} = 57.0$$

$$\Delta P =  P_1 - P_2 = 5 - 10 = -5$$

$$\bar{P} = \frac{P_1 - P_2}{2} = \frac{ 5 + 10 }{2} = 7.5$$

Combining, we can find elasticity of demand:

$$\epsilon_D = \frac{ \Delta Q / \bar{Q} }{ \Delta P / \bar{P} } \approx -0.7895 $$


---


#### Act 2

Use a graph to plot this demand curve, including the quandity demanded at both $5$ galleons and $10$ galleons. Then find and label the consumer surplus at these prices.

```python
Markdown(
    f'CS at $5$ galleons = ',(D_int - P_1)*Q_d(P_1)/2

print('CS at 10 =',(D_int - P_2)*Q_d(P_2)/2)
```

*(figure: graph_paper.png)*

CS at $5$ galleons:__________

CS at $10$ galleons:__________


---


#### Act 3

The supply curve for pumpkin pasties can be represented by the equation:

$$P = 2 + \frac{2}{3} Q$$ 

Use a graph to plot this supply curve, and find and label the producer surplus at both $5$ galleons and $10$ galleons.

*(figure: graph_paper.png)*

PS at $5$ galleons:__________

PS at $10$ galleons:__________


---


#### Act 4

The Ministry of Magic decided to institute a price ceiling of $10$ galleons to allow many more to afford the treat. Use a graph of the demand curve and the supply curve to evaluate the welfare effects this policy had on the pumpkin pastie market.

*(figure: graph_paper.png)*

CS:__________

$\Delta$ CS:__________

PS:__________

$\Delta$ PS:__________

DWL:__________

Shortage/Excess:__________


---


#### Act 5

After years of careful epidemiological analysis, a subcommittee of the Ministry tasked with improving the health and wellbeing of the wizarding community published a story in the Daily Profit establishing a link between the consumption of pumpkin pasties and accidental magical spell casting by wizards and witches in public areas, with many cases of innocent muggles nearly being injured. To address these obvious public health concerns, the fiscal arm of the Ministry removed the price ceiling, instead imposing a $2$ galleon tax on the sale of pumpkin pasties while reinvesting the revenues into researching a magical remedy for this diet-driven ailment.* Use a graph to illustrate the impact this tax had on the market.

```python
print('P_s =',2 + )
```

*(figure: graph_paper.png)*

CS (post-tax):__________

$\Delta$ CS:__________

PS (post-tax):__________

$\Delta$ PS:__________

DWL:__________

*Note: assume there are no externalities, which we’ll cover next week; pumpkin pasties are a private good; the market is competitive.


---


#### Act 6

Economic historians in the wizarding world remember a time before the Ministry had begun meddling with the domestic market. In those earlier days, trade barriers had been lifted for exports of pumpkin pasties to international magical markets with a world price of $12$ galleons. At the time, the Ministry of Magic used this opportunity to pad its coffers without facing the political backlash associated with a domestic tax, instead imposing an import tariff of $2$ galleons. Use a graph to illustrate what happened to the market after the tariff was imposed. Remember the supply and demand curves:

$$P = 17 - \frac{1}{6} Q$$
$$P = 2 + \frac{2}{3} Q$$

```python
sympy.Eq(P, 17 - sympy.Rational(1,6)*Q)
```

```python
P, Q = sympy.symbols('P, Q', real=True)
[(p,q)] = sympy.nonlinsolve([P - 17 + Q/6, P - 2 - 2*Q/3], [P, Q])
sympy.Eq(P,p)
#sympy.Eq(Q,q)
```

*(figure: graph_paper.png)*

What is the area of the deadweight loss from the tariff?__________
