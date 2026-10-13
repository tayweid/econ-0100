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
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

== Episode A0 | _Economics isn’t_ about _money_

_Economics from scratch._

Often when I hear about economics in popular culture or on the news it has to do with prices, stocks, market indicators, unemployment, maybe with a ticker tracking something financial. This figure shows unemployment on the vertical axis with time passing on the horizontal axis.

_*Show a time series of unemployment ending in 2008*_

It is necessary that we measure and communicate these things. Unemployment, people looking for but not finding jobs, measures something important about the state of our world. This view makes it easy to see when things are going wrong for people. You can see the Great Recession in this one measure.

_*Continue the time series to 2020*_

And as we reach 2020, unemployment figures like this can also communicate big events like Covid. You likely have seen figures like these on TV. Economics at base, however, isn’t _about_ money or unemployment.

In my early years I had a question. Look at this graph of wealth during the Great Depression. Where did all that wealth go? Remember, wealth is made up of things like houses and iPads and food. What happened here that it seemed to vanish? It was a mystery to me.

And take a look at this map, showing where people live in the world. Why are people crammed into cities together, especially right on the oceans?

_*Map of Earth at night, then the title “The 30 largest cities in the world.” and the cities grow in, ports in gold; under the title: “20 of the 30 are ports.” A hidden force draws humans together in space; a discovery that explains why we as a species tend to clump together.*_

I’ve been motivated by a common feeling of frustration about why things can’t work better. I came to the field by observing political violence, graduating high school into the Great Recession, seeing our failure as a planet on climate change. If you’re anything like me you likely want to understand the big why’s of our world. Some of the biggest ones have to do with how 8 billion of us get what we want all at the same time.

I discovered economics as a field in this class actually, when I realized I could use my love for math to guide these kinds of questions. You don’t need to care about math to care about economics. But if you’ve ever wondered why kale has nearly the same price at every farmer’s stand or that the phone in your pocket was designed in California, assembled in China, with parts sourced from many other countries, you’ve found a field with something substantial to say.

My suspicion is that despite their power, the ideas in economics are poorly understood to such an extent that it’s impacting the functioning of society.

You don’t want to hear me, an economist in the ivory tower, complaining about being misunderstood. But you may want to hear how you can improve your own thinking in powerful and potentially subversive ways.

Many have written excellent books about economic principles, published news stories about current economic issues, and spoken in every area of society about particular economic policies. But while it’s important to talk about what the models tell us, the models themselves have not been widely accessible outside the academy’s lecture halls. Today there is considerable misunderstanding, confusion, skepticism, and distrust of economic models and what they mean. It is understandable that we become distrustful of powerful tools when they are misused by powerful interests, especially when the tools are not well understood.

Economics is part of the power structure. The ideas in this course are powerful. My view is that economics when used with humility and clarity is a powerful tool to move the needle on human well-being, on many of the world’s most urgent problems. When I look at my field, I do not see a straw man built on flimsy assumptions but a well founded framework based on careful observations about human behavior. And I believe the problems created by both misusing and neglecting powerful ideas can be made better with clear communication of the ideas that make up what we call economics.

For most of the history of the field, good communication has taken place in lecture halls and seminar rooms. That is where I’m coming to you. You may even be my student. But today we have new tools which allow us to open these doors even just a crack, to communicate more effectively, in a simple and clear way. Economics need not be difficult to understand and should not be only understood by a few.

You, _dear viewer_, are more than capable of understanding the models directly, not just their conclusions. You can understand and wield economics. With some work and attention, you can understand how they work and when they don’t.

For the challenges in front of us on this planet we share together, I believe an informed citizenry is our best bet. Call me naive or overly optimistic, but I’m interested in running this experiment.

Developed from my lectures, inspired by those who have come before, this series is an attempt to do just that, to show you the wonder at the heart of social science and specifically economics. I want to provide you with the understanding in your bones of some of the most foundational ideas we have as a society.

Lets start at the beginning.

=== Preferences

Each of us has preferences. I prefer carrot cake to chocolate cake.

_*Show “Chocolate Cake ≺ Carrot Cake”: less preferred on the left, as on the number line to come.*_

I know I know. Send your hate mail to econ\@hatemail.org. I also prefer dark roast coffee to medium roast coffee.

_*Show “Light Roast ≺ Dark Roast”.*_

I prefer medium roast coffee to light roast coffee.

_*The pair opens in the middle and “Medium Roast ≺” inserts: Light ≺ Medium ≺ Dark.*_

In this model of preferences, my preference relations are transitive. Here because I prefer dark roast to medium roast, and I prefer medium roast to light roast, this also means that I like dark roast more than light roast. I could keep going, listing out all the different types of coffee.

_*The chain dissolves onto a horizontal number line: dots at positions, further right is preferred, no symbols. Espresso slides in to the right, decaf to the left.*_

I have preferences for most things in my life. And if you’re human, you do too. I could ask you about most things and you’d be able to tell me which you prefer. You’d be able to rank them.

_*One group fades out, the next fades in with its own positions: seasons, then pizza toppings, then back to coffees.*_

This is how we think about preferences, as rankings.

_*Show “Preferences are rankings.”*_

Then a magical step is to turn preference relations into math. All we have to do is list the choices from best to worst, assign them numbers, with larger numbers being more preferred, and this ordering represents our preferences. This is one way economists think about preferences, as points on a number line, doing the ranking for us. These numbers are what we call ‘Utility’.

_*Tick numbers (1, 5, 10) appear on the number line. Then define Utility on screen.*_

We can like different things and like the same things differently. How much we like something is what we call a benefit. We can measure benefits with utility if we want, but often we’ll just talk about benefits and not worry about the units so much.

_*A second number line below, “You”, same coffees in a different order with different numbers; then fade the numbers and label the axis “benefit” with an arrow.*_

On the vertical axis, higher means we like it better. The specific numbers don’t matter here. There are fancy terms here for this property. But all that matters here is that higher numbers are better. We can multiply the numbers by 100 and higher things would still be higher.

_*Relabel the ticks with every number multiplied by 100. No item moves.*_

And we can change our preferences. I used to like coffee more than tea but now I like tea more than coffee.

_*Everything but Espresso fades; Tea comes in to the left; as my preferences change the two slide past each other.*_

=== Scarcity

Sorry if I’m the one to break it to you, we can’t always have what we want most.

_*Show “We can’t always have what we want most.”*_

Most people prefer a nice house near the park to a single bedroom apartment with a long commute. But for many reasons not everyone can have the nicest house in the city. And while we face financial constraints it’s important to realize that scarcity like this is more basic than money.

_*Show “Scarcity is more basic than money.”*_

I could give everyone in Pittsburgh the price of the nicest house in the city, and it would still not be possible for everyone to have that nicest house. Its scarcity isn’t simply because of its price tag. We’ve always faced scarcity, even before money was invented.

This tension between getting one thing or another happens at both the individual and societal levels. You may ask yourself whether you want a nice house near the park but spend less on the movies or to have a small house far from the park but you get to go to the movies more often.

_*Two bundles side by side with OR between them: big house + two movie tickets vs small house + six movie tickets.*_

But we are also asking from a societal perspective _*who*_ gets that nice house near the park.

_*Two houses with OR between them, labelled “Taylor gets the house” and “Andrew gets the house”; green and red boxes pick one, then swap.*_

=== Preferences + Scarcity = Choices

Society faces all sorts of choices like this precisely because we have preferences AND we face scarcity. With preferences in the face of scarcity, we must make choices.

_*Show “We make choices because of preferences and scarcity.” and keep it up.*_

I like to boil this down into a pseudomathematical relationship like this. When we like some things more than others but can’t have everything, we have to pick the things we like the best, which involves giving up things that we like less.

_*Fade in Preferences + Scarcity = Choices underneath.*_

This is the world economics lives in. Given that we are making choices to maximize our preferences amidst scarcity, everything we do requires us to give up something. In some ways this is a dismal place to start. But the big point here is that seeing the landscape clearly allows us to solve our challenges effectively.

=== Tradeoffs

With the table squarely set with preferences and scarcity, we’re going to start building a model of choices, of decision making, in a way that might feel elementary. Every decision we face has a cost and a benefit. If the decision’s benefit is greater than its cost then we do it.

Lets say I give you the choice of #mi(`A`) OR #mi(`B`).

_*Show A or B*_

If you choose #mi(`A`), you can’t have #mi(`B`). If you choose #mi(`B`), you can’t have #mi(`A`). That’s the scarcity.

_*Green box on the one chosen, red on the other; they swap back and forth: one or the other, never both.*_

If you like #mi(`A`) more than #mi(`B`), you’ll choose #mi(`A`). That’s the preference.

_*Show choosing A and not choosing B*_

Your benefit is the value #mi(`A`) gives you.

_*A and B on a number line below; A turns green: the benefit is where A sits.*_

But because you chose #mi(`A`) you gave up the opportunity to have #mi(`B`). This is the other side, due to scarcity. This is the cost, the value of all the things you gave up to get it.

_*B turns red: the cost is where B sits. A green bracket spans the gap between them: “A beats B”. Write Opportunity Cost(A) = B.*_

This is what economists call opportunity cost, the value of the next best alternative.

_*Define Opportunity Cost on screen.*_

If you choose #mi(`A`), your next best alternative is #mi(`B`). So your opportunity cost of #mi(`A`) is #mi(`B`). And if you like #mi(`B`) more than #mi(`A`), you would pick #mi(`B`) and the opportunity cost of #mi(`B`) is #mi(`A`).

_*The two dots cross; the bracket turns red, “B beats A”; the boxes swap and the equation becomes Opportunity Cost(B) = A.*_

For example, you walk into Forbes Ave Grocery to get a snack. They have lots of snacks there. But let’s keep it simple and say they only sell apples and bananas, each for \$1. If you buy an apple, you give up what else you could do with that \$1, like buy a banana. The opportunity cost of the apple is the next best use of your \$1, which in this simplified example is the value of the banana to you. Costs are more basic than money.

Similarly, if your friendly neighborhood bakery was generous enough to give you an apple pie OR a loaf of banana bread, but only one, if you choose the apple pie, you would give up the banana bread. So the opportunity cost of choosing the apple pie is how much you like the banana bread.

_*Number line: banana bread, apple pie. One red arrow from pie to its next best, bread; store OC(pie) = bread; the arrow fades.*_

What about if the bakery throws in the option for carrot cake? We now pick one out of the three things.

_*Carrot cake slides in from zero to the right end.*_

Opportunity cost is the value of the next best alternative. And it turns out I love carrot cake. I like it more than apple pie and banana bread.

_*Carrot cake settles to the right of both.*_

Before the carrot cake, the opportunity cost of apple pie was the value of the banana bread. After the carrot cake, the opportunity cost of the apple pie is the carrot cake. That’s what I would have chosen if I didn’t choose apple pie.

_*Re-find OC(pie) with one arrow, now pointing to the cake; then one arrow at a time for the cake and the bread, storing each as a line of the opportunity-cost table.*_

With this in mind we can write down the opportunity cost of each of the three alternatives, each being the thing we like the best of all the things leftover.

=== Social Environments

We have to make individual choices that require tradeoffs in this way. But the choices available to us aren’t always our own making. If I lived in a cabin in the woods and grew all my own food and chopped all my own wood, my social environment is pretty simple. This is what we call Autarky, a state of self-sufficiency.

_*Show the definition of Autarky*_

We talk about this mainly with countries and international trade. Autarky is uninteresting and unrealistic. We all rely on each other in many ways every day. I would go hungry if not for my grocer.

Interdependence makes social environments more complicated. For example, let’s say you and your love interest are planning a date. You’ll go either to the movie or the theater. This is an example of a payoff matrix.

_*Show the dating game*_

Your love interest can either choose to go to the movie or the theater.

_*Circle both*_

And you can choose to either go to the movie or the theater.

_*Circle both*_

The numbers in the boxes represent the value to you of each set of choices. If your love interest is going to the movie, and you go with them you get a better payoff than if you don’t go with them. But if your love interest is going to the theater, in this case you shouldn’t go to the movie and leave them hanging, you should go with them to the theater!

_*Circle everything that’s relevant as it’s said*_

Your preferences depend on the choices of others in your social environment.

Microeconomics, what we’re doing in this course, is about individual decisions inside social environments with preferences and constraints. Where did all that wealth go during the Great Depression? Why are people crammed into cities together? Economics is the framework that we have discovered over hundreds of years to think about these kinds of questions.

Microeconomics is not about money or capitalism and is only about politics in so much as politics is one way in which we have decided to coordinate.

_*Show “Microeconomics tells us there’s a deep fundamental reason why it pays to coordinate with each other, that markets can serve as an effective coordination device sometimes, that markets often fail, gives us a framework for when, and provides some alternatives for doing better.”*_

Microeconomics tells us there’s a deep fundamental reason why it pays to coordinate with each other, that markets can serve as an effective coordination device sometimes, that markets often fail, gives us a framework for when, and provides some alternatives for doing better.

=== Six Parts

This class is made up of six parts.

_*First video shows all six parts as animations and their conclusions*_

=== A History Changing Idea

This is the starting point for a long and interesting journey to build up some big ideas for how we organize society. You may be familiar with some of the ideas in economics, but I can almost guarantee you that unless you know the field already, many of the results will surprise you.

Next time, we’re going to take a trip back to 1800s British philosophy at the dawn of the industrial revolution as Feudalism gave way to Mercantilism, opening big questions about how we might best organize society. These questions birthed the field of modern economics we know today and is where we’ll start next time.

=== Who these videos are for

Some of you will be coming from your college Econ class, maybe even mine, some from high school Econ, and for some of you this will be all new. No matter your background, these videos can be for you. All you’ll need is a basic familiarity in algebra and a curiosity for how our social world works.

These videos are not aimed at preparing you for an exam. If you’re in my class, we’re doing lots of practice alongside these videos, which is where the preparation truly comes from. And if you’re studying for some other Economics exams, this video series may be helpful there too, but that’s not the point of these videos. There are probably better resources for exam preparation.

Videos are intended to inform but they cannot educate. That’s what we’re going to do in the room.
