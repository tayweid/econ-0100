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

== Episode A2 | Specialization

_Better choices alone can increase what’s possible._

=== The Co-op

It turns out Molly isn’t the only farmer in the area. Another farmer, Andrew, operates another small scale organic farm next to Molly’s. He also is good at growing carrots and spinach. He can grow #mi(`8`) tons of carrots per year or~#mi(`16`) tons of spinach per year on a similar #mi(`100`) hectare farm. Molly is also able to produce more of both goods, so she has the _*absolute advantage*_ in both carrots and spinach.

_*Show: the production table — Molly’s and Andrew’s yearly capacities side by side; on “absolute advantage,” box Molly’s row.*_

Molly and Andrew decide to form a local farmers co-op, operating their respective farms but shipping their produce together. Let’s say the co-op decides that both farms will produce the same ratio of carrots and spinach. Dividing their farms equally between crops, Andrew will produce #mi(`4`) carrots and #mi(`8`) spinach, and Molly will produce #mi(`5`) carrots and #mi(`20`) spinach. This adds up to #mi(`9`) carrots and #mi(`28`) spinach. Under this regime, the co-op’s PPF is just a line running through the co-op’s extreme points #mi(`18`) carrots and #mi(`56`) spinach, just the extreme points for the two farms added together.

But Molly, having studied economics in college realizes that opportunity cost might be important to consider when choosing their crops. Like we did for Molly, Andrew’s opportunity cost of carrots is #mi(`2`) spinach. Again, this is visualized by Andrew’s flatter PPF, meaning he gives up more carrots for each ton of spinach relative to Molly.

_*Show: the opportunity cost table joins the production table — Andrew’s row derived the A1 way (the two capacities set equal, divided through), landing Opportunity Cost(1 C) = 2 S.*_

So Molly has a lower opportunity cost of carrots and Andrew has a lower opportunity cost of spinach. Molly has to give up #mi(`\frac{1}{4}`) units of carrots for every #mi(`1`) unit of spinach, and Andrew has to give up #mi(`\frac{1}{2}`) units of carrots for every #mi(`1`) unit of spinach. So Andrew is relatively less efficient at growing spinach because he’s giving up more carrots to grow it. And Andrew, therefore, is relatively more efficient at growing carrots since he’s giving up less spinach to grow it. This is the flip side of the opportunity cost equation we used at the beginning of the video. Andrew’s next best use of his land is less costly when growing carrots even though Molly is better at growing carrots. This is because she is _much_ better at growing spinach than Andrew. This is one of those important and somewhat unintuitive ideas you’ll run into periodically in economics.

Maybe pause here and convince yourself that even though Molly is better at growing both goods, Andrew has a lower opportunity cost of growing carrots than Molly. He gives up less than she does to grow carrots.

=== Specialization + Comparative Advantage

Having a lower opportunity cost is what we call *comparative advantage*. And here, Andrew has a comparative advantage in carrots, and Molly has a comparative advantage in spinach. As you might have seen before, there is an important mathematical realization here. When one farmer’s opportunity cost is lower in one crop, the other farmer’s opportunity cost will always be lower in the other.

_*Cut to Exercise A2 | Q1. Screen shows the question; class builds both tables on paper, then we do it on the board.*_

_Q1 | Comparative and Absolute Advantage — Professor McGonagall also bakes rock cakes and fruitcakes, up to 10R or 5F in one day. Using Hagrid’s original numbers, set up a production table with both Hagrid’s and McGonagall’s output per day. Who has the absolute advantage (AA) in rock cakes? Then set up an opportunity cost table with Hagrid’s and McGonagall’s opportunity costs for each good. Who has the comparative advantage (CA) in rock cakes?_

Molly realizes that maybe there’s something to this idea, that maybe the co-op should be minimizing their joint opportunity cost. So she and Andrew decide to specialize in what each farmer is relatively most efficient at growing, what they have a comparative advantage in. Molly grows only spinach, growing #mi(`40`). And Andrew grows only carrots, growing #mi(`8`).~

So without changing any technology, simply by choosing their crop according to their comparative advantage, the local farmers co-op was able to exceed the frontier. It’s a more general truth that so long as we’re not too close to the edges, we can exceed any point on the PPF with specialization.

_*Cut to Exercise A2 | Q2.*_

_Q2 | Specialization — In Exercise A1, we found that Hagrid can bake #mi(`20`) rock cakes (#mi(`R`)) or #mi(`30`) fruitcakes (#mi(`F`)) in one day and Professor McGonagall can bake #mi(`10`) rock cakes or~#mi(`5`) fruitcakes in one day.~Use the production table and opportunity cost table developed in Q1 to determine who should specialize in each good if they want to jointly produce more._

This tells us something deep and extraordinary: specializing in the lower opportunity cost crop makes the co-op do better than a simple split. Making choices together that minimize opportunity cost can make Molly and Andrew better off jointly.

This is nice, but we’re left with two large remaining questions. First, a co-op as I’ve called it could be a lot of work. Think about it. I don’t grow my groceries. Someone else grows my food and brings it to my grocery store. This is truly very nice. I don’t want to form a co-op with my grocer. It would be a lot of work. Second, can we organize specialization like we’ve done in the co-op in a way that not just makes the co-op better off, but makes both farmers better off at the same time? Those are our remaining questions, to which the answer is an optimistic YES!

So let’s turn to the model proposed by David Ricardo in 1817 to explain how specialization and trade can make two countries better off.

Molly and Andrew have operated as a co-op, but from here on out, they’ve decided that even though they appreciate working together, they might want to try to coordinate in a different way. Instead, they’re going to aim to maximize their own harvests individually. This is where the real magic happens.

To model this environment, we’ll set up two PPFs, one for Molly and one for Andrew. We know it’s possible to exceed their co-op PPF with specialization. But can we exceed the frontier of both farms individually at the same time?

We’ll start with autarky, where the farmers don’t trade with each other. In autarky Molly can grow #mi(`10`) tons of carrots OR #mi(`40`) tons of spinach while Andrew can grow #mi(`8`) tons of carrots OR #mi(`16`) tons of spinach. One way of asking the question we’re after is whether through a combination of specialization using comparative advantage and trade between the farmers, can we arrive at a point that’s on the outside of both farmers’ PPFs at the same time. At first we’ll keep things simple. Let’s pick a point in autarky and see if we can do better with trade. Remember, the PPF represents all possible production choices that use all our resources, so there are many options we could choose from. To start, I’m going to pick the production point of #mi(`3`) tons of carrots and #mi(`28`) tons of spinach for Molly, and #mi(`4`) tons of carrots and #mi(`8`) tons of spinach for Andrew.

Like before, we have a hunch that we might be best off by trying to minimize opportunity cost by specializing according to comparative advantage. Let’s follow a similar program for improving both farmers beyond this point in autarky. However, here we have one extra layer. If we’re trying to exceed these points while specializing, the farmers also need to trade with each other.

Before we actually try to find a trade of spinach for carrots between the farmers, let’s think about how both farmers might effectively perform a trade with themself. Each farmer could, if they wanted to, switch part of their farm from growing their comparative advantaged crop to growing the other good. This *self-trade* has an *exchange rate* that’s exactly equal to their opportunity cost. As we move away from pure specialization to something that’s less specialized, we’ve given up some of our comparative advantaged good and gained some of the other good. The slope of the PPF tells us exactly what opportunity cost tells us. Molly on her own can perform a *self-trade* for #mi(`1`) carrot at an exchange rate of #mi(`4`) spinach for #mi(`1`) carrot. Therefore, Molly would need to receive a better deal than this from Andrew for her to want to specialize according to her comparative advantage and trade with Andrew for the other good. Essentially, Molly is looking for a trade that is a better deal than her PPF.

_*Cut to Exercise A2 | Q3.*_

_Q3 | Self-Trade — What is the cost to McGonagall of baking #mi(`1`) fruitcake (#mi(`F`)) herself? What is an example of a trade with Hagrid that would be better for her?_

Next time…
