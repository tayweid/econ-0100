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

== Episode A1 | Production Possibility Frontier

_The space of what’s possible_

_*Show: bumper — Part A | Episode 1, thesis line beneath. Then the “Last Time…” card.*_

Last time we talked about preferences and scarcity, and that together we need to make choices that carry tradeoffs, which we measure using opportunity cost. Since we usually have more than a couple of uses of our scarce resources, we define opportunity cost as the value of the next best use of your resources, where we find the value of the best thing we didn’t pick.

_*Show: A or B with the green/red choice boxes; Opportunity Cost(A) = B, then the boxes swap and it flips. On “next best use of your resources”: the definition card.*_

If you’ve ever taken a physics class, you may have used a toy model of a pool table to help build the framework for more complex problems later on. The pool table isn’t everything you care about and doesn’t capture anything close to the relevant features of the physical world. But it boils down important ideas in a tractable and concise way. We’re going to start economics in a similar way. As we work through the framework in which economics operates, you’ll likely find yourself having some sceptisism. Notice it and think about how you might improve the toy model. And if you have interest, you can try to go on and maybe even contribute to improving our current models.

=== Opportunity Cost

Let’s build up some intuition for opportunity cost with a little example. Imagine Molly, a small scale organic farmer, is good at growing spinach and carrots on her #mi(`100`) hectare farm. If she spends all her time growing spinach she can grow #mi(`40`) tons per year. If instead she spends all her time growing carrots, she can grow #mi(`10`) tons per year. If Molly were to switch from growing all carrots to all spinach, she would give up #mi(`10`) tons of carrots and instead get #mi(`40`) tons of spinach.

_*Show: the farm plot fills all-spinach — 40 S slides out. Flip to all-carrots — 10 C or 40 S.*_

What is Molly’s opportunity cost for 1 ton of carrots (1C)? To find it, we set those two production values equal and simplify. And that’s it. Molly’s opportunity cost of #mi(`1`) unit of carrots is #mi(`4`) units of spinach. For every #mi(`1`) unit of carrots she wants to grow, she’ll have to give up #mi(`4`) units of spinach. And we could simplify the other way and find that the opportunity cost of 1 ton of spinach is 1/4 tons of carrots. They’re just reciprocals.

_*Show: “or” becomes “=”; divide both sides by 10; 1 C = 4 S. Then: Opportunity Cost(1 C) = 4 S.*_

The reason we set them equal is because they are the two values that we can produce on the same amount of land.

=== Production Possibility Frontier

There is a more systematic way to think about Molly’s farm. Molly doesn’t need to not choose either carrots OR spinach. She can choose any combination of the two crops. So let’s examine a range of crop choices she can make.

Let’s use an #mi(`x,y`) graph to plot how much of each crop model is harvesting as we move through a few crop choices. Let’s use the horizontal axis to represent her carrot harvest and the vertical axis to represent her spinach harvest. We’ve already established that she can harvest #mi(`10`) tons of carrots and #mi(`0`) tons of spinach, or #mi(`0`) tons of carrots and #mi(`40`) tons of spinach.

_*Show: axes grow in next to the farm — carrots horizontal, spinach vertical; a dot with a live (C, S) readout tracks the farm split: (10, 0) all carrots, then (0, 40) all spinach, each leaving a mark.*_

Based on her productivity numbers, if Molly plants carrots on half her land and spinach on the other half, she would have half of #mi(`10`) tons of carrots and half of #mi(`40`) tons of spinach. Let’s also plot that on our #mi(`x,y`) graph.

_*Show: the farm splits half and half; the dot rides to (5, 20).*_

We can pick another point, splitting the land into #mi(`\frac{3}{5}`) carrots and #mi(`\frac{2}{5}`) spinach. We find this by dividing by 5 and multiplying by the numerator, so #mi(`10 \cdot\frac{3}{5} = 6`) carrots and #mi(`40 \cdot\frac{2}{5} = 16`) spinach.

_*Show: 3/5 carrots — the dot rides to (6, 16).*_

I’m going to run through a few more on screen. As as we do, we can more easily see that any carrot and spinach combination Molly chooses lies on a line which we call the Production Possibility Frontier (PPF).

_*Show: one more split — (3, 28) — then the frontier draws through the marks; the farm fills Molly-blue; title: “Molly’s Production Possibility Frontier.”*_

Lets say Molly starts by growing all spinach and no carrots. How many tons of spinach does she have to give up if she wanted to grow 1 ton of carrots? This is the same question as asking how much do we have to move on the vertical axis if we move one unit on the horizontal axis? But this is the same calculation as with opportunity cost. The slope of the PPF tells us her opportunity cost. To harvest #mi(`1`) more unit of carrots Molly must harvest #mi(`4`) fewer units of spinach. The slope here is negative since we’re giving one good up for the other, exactly what opportunity cost is capturing.

_*Show: the board moment — write S = 40 − 4C; the slope triangle on the line (+1 C across, −4 S down); box the −4; beneath it, Opportunity Cost(1 C) = 4 S.*_

\~ _The marginal christening beat is built in the code (the OC line transforms into Marginal Cost(1 C) = 4 S, gold) but the sentence isn’t in the script — say the word here, or cut the beat._

At this point you might wonder how Molly would choose how much of each to plant. Great question. That’s a great question we’ll return to. For now we’re just going to find what’s possible to set up the trade-offs involved in our later models.

_*Cut to Exercise A1 | Q1. Screen shows the question; class works it on paper, then we build it on the board.*_

_Q1 | Hagrid’s PPF_

_One of Hagrid’s unknown skills is that he’s great in the kitchen. He can bake 20 rock cakes (#mi(`R`)) or 30 fruitcakes (#mi(`F`)) in one day. Set up Hagrid’s PPF on an #mi(`x,y`) graph with rock cakes (#mi(`R`)) on the vertical and fruitcakes (#mi(`F`)) on the horizontal. What is Hagrid’s opportunity cost of each good?_

=== Attainability

Molly’s PPF shows us all the combinations of carrots and spinach that she can produce by using all the land and labor available to her. Is it ever possible to produce at a point just inside the PPF like this?

_*Show: the attainable region shades under the frontier; a harvest dot inside it — Inefficient.*_

This is what we call _*inefficient*_, since there’s productive land that’s gone unused. You might be thinking that maybe she had a good reason to leave it unused, like to make sure she gets her full 8 hours of sleep. We’ll get to how Molly chooses how much of each crop to plant later in this semester. But just for the moment all we can say is that there is missed potential harvest.

_*Show: a dot on the frontier — Efficient.*_

We call the points on the frontier _*efficient*_ since Molly is using all her land and labor to it’s fullest.

Now lets say Molly wishes to produce at this point. What do we know about _it_?

_*Show: a dot beyond the frontier — Unattainable.*_

If this were possible for Molly to produce with her labor and land it would be on her PPF. This point is what we call *unattainable* since is larger than what she is able to produce on her frontier.

_*Cut to Exercise A1 | Q2.*_

_Q2 | Feasibility_

_Suppose Hagrid wants to bake 30R and 20F in one day. Is this inefficient, efficient, or unattainable? Use a graph or algebra to justify your answer._

It turns out Molly has been working #mi(`10`) hours per day, but realizes she’s burnt out and needs to spend less time working. She decides to spend only #mi(`8`) hours per day on her farm, which means she is now only able to grow on #mi(`\frac{4}{5}`) of her #mi(`100`) hectare farm. With this new work schedule she can only farm #mi(`80`) hectares. Her productive capacity has dropped to either #mi(`8`) carrots or #mi(`32`) spinach.

_*Show: the planted band narrows to 4/5 of the farm; the endpoint dots slide in — 10 C to 8 C, 40 S to 32 S.*_

This is fine if this is her preference and she can still make her ends meet. The rest of the points along the PPF have shifted in with the extreme points. At this point I would recommend convincing yourself that any combination of crops lies on this new PPF.

_*Show: the frontier shifts in to the new endpoints; the old frontier stays ghosted.*_

This may seem like bad news for Molly’s wallet. And it could have been. But it turns out that later that winter she comes across a new carrot harvesting technology that would double her carrot harvest but not improve her spinach harvest.

What happens to Molly’s PPF after this new technology? We’ll with this technology she’s able to grow up to #mi(`16`) carrots while nothing has changed her productive capacity. We see a pivot out of the PPF.

_*Show: “+ Better Carrot Tech” stamps onto the farm — hold on the question — then the frontier pivots out on the carrot axis to 16 C.*_

So what’s happened here? A change in Molly’s labor input has changed the output of her farm. The frontier depends on the level of labor. The more labor, the more is possible. And in this case since there’s less labor, less is possible. And in addition to labor, the PPF also captures changes in technology.

These changes in the PPF aren’t purely mathematical. What we’ve found is a region that used to be inefficient that is now unattainable. And a region that used to be unattainable that is now on the frontier.

_*Show: shade the region that’s no longer attainable (grey), then the newly attainable region (pink); last, the gold sliver lost to the labor cut and regained by the tech — left up as a “?”.*_

_*Cut to Exercise A1 | Q3.*_

_Q3 | Dynamics_

_It turns out Hagrid wants to slow down his baking work, and cuts his time in half. Right after, the baking industry goes through a minor revolution and improves the efficiency of everyone’s baking by a factor of 2. Show both changes to his PPF._

=== In Closing

The story here is that what Molly has available to her depends on how much labor she puts into her farm and the efficiency of her technology. If she works more, she can have more produce. If her technology is better, she can have more produce. This relationship is what one person can do on their own. We also use this to model the productive capacities of countries.

If this were the best one could do, the story would be pretty boring. And we’d be pretty close to finished with this class. But some foundational insights in the 1800s give us our first counter-intuitive punchline: we can actually do better. This profound insight means we can exceed the frontier without changing inputs or technology. Showing how we do this requires some mathematics and a small detour into 1800s economic history. And that’s exactly where we’re going in the next few classes.

_*Show: “We can actually do better.” Then: Next time… — a detour into 1800s economic history, frameboxed, run to black.*_
