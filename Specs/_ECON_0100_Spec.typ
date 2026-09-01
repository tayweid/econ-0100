// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#set math.equation(numbering: "(1)")

= ECON 0100 - Fall 2026

- Full Spec Conversion
- Topic List
- Syllabus
- Prep first week
- First video

New Structure: start class with a recap of the episode, then do a vignette from a crafted list, recitations do the next one in the list, just add a semester in the label for grading purposes. homework is automated, preferably multiple choice.

== Econ 0100 - Spec Conversion

Your final grade comes solely from the number of skills you pass on MiniExams. Learning is done through study and practice. This class is set up to guide you through practice to be fully prepared for the MiniExams. Each~skill has three types of~practice: 1) exercises (in class), 3) vignettes (in recitation), and 3) homework (on your own time).

You unlock a MiniExam _*attempt*_ by completing 2/3 types of practice. You unlock a MiniExam _*reattempt*_ by completing 3/3 types of practice. MiniExam reattempts replace your first attempt in your favor. So you only need to reattempt the questions you haven’t yet passed. This means your study of a topic need not end after a MiniExam. If you did not pass a topic, you’re encouraged to~continue to study it to prepare for a reattempt.~

Final grades breaks are based on the fraction of topics passed. If you pass 94% of the topics on the MiniExams, you get a 94% for your final grade _(grade breaks below)_. If you pass 84% of the topics on the MiniExams, you get a 84% for your final grade~_(grade breaks below)_.

=== Reattempts

I need another time outside class time for people to come and do makeups for any of these three they missed.~Students who missed the in-class exercise can make it up by completing it with a TA during office hours before the next miniexam reattempt window.

The TA works through the exercise with the student and submits the grade to \
Gradescope. This keeps the 2-of-3 gate flexible for first attempts while ensuring \
students who need a second shot have fully engaged with all the material, without permanently penalizing anyone for missing a single class.

I need a reattempt MiniExam for each MiniExam, and maybe more than one reattempt MiniExam.~

And when do they take them? It can’t be in class unless I give more time, but I~don’t have enough time for that. Could do reassessments in Recitation. Or I could just have a time outside of class time to do them. But I don’t know how many people need to do that so it’s harder to plan.

=== Backend

Assessment scores sync automatically from Gradescope to Canvas via the LTI integration. A Python script then reads those scores through the Canvas API, checks each student against skill-specific thresholds, and updates corresponding pass/fail skill assignments accordingly.

Then I also need a program to generate questions. I’ll use some stems and then~have the program create different versions.

== Topics

33 skills. Each is one individually assessed item: practice materials and pass/fail MiniExam questions are built per skill.

=== Part A | The Landscape

A1. Opportunity Cost

A2. The PPF (construct; classify bundles; shifts)

A3. Absolute and Comparative Advantage

A4. Specialization and Trade (exchange rates; post-trade consumption)

A5. Marginal Reasoning (marginal cost/benefit; Pareto improvement)

=== Part B | Markets

B1. Demand (curve; Qd; consumer surplus; shifters)

B2. Supply (curve; Qs; producer surplus; shifters)

B3. Equilibrium (solve P and Q; shortage/surplus incentives)

B4. Market Welfare (total CS and PS; efficiency of the competitive quantity)

B5. Comparative Statics

B6. Price Controls (ceiling/floor; quantities; welfare; DWL)

B7. Elasticity (midpoint; interpretation; cross-price and income)

=== Part C | Market Failure

C1. Taxes and Incidence

C2. Subsidies

C3. International Trade and Tariffs

C4. Negative Externalities (market vs efficient quantity; DWL)

C5. Positive Externalities

C6. Corrective Policy (instrument choice and size)

=== Part D | Strategic Interaction

D1. Games and Best Response (dominant strategies)

D2. Nash Equilibrium (vs socially efficient outcome)

D3. Goods and the Commons (rivalry × excludability; overuse as a game)

D4. Public Goods (WTP aggregation; efficient provision; free-riding)

D5. Voting (majority outcome vs efficiency; cycles)

D6. Sequential Games (game trees; backward induction)

=== Part E | Sellers

E1. Costs of Production (production function to cost curves)

E2. Competitive Firms (P = MC; entry/exit; long-run zero profit)

E3. Monopoly (MR = MC; price; DWL of market power)

E4. Duopoly (Cournot best responses; vs competitive benchmark)

E5. Policy and Market Power (taxes/subsidies across market structures)

=== Part F | Buyers

F1. Budget Constraints (shifts and pivots)

F2. Preferences and Optimization (indifference curves; MRS; optimal bundle)

F3. Factor Markets (labor supply/demand; wages to income)

F4. Linked Markets (capstone: trace a shock to the consumer's bundle)

~

== Material / Practice

=== Lectures and Episodes

Lectures introduce the concepts and move students quickly to practice. Practice in Lecture is limited to small skills, leaving the bigger questions to recitation. Skillsheets organize the basic skills done in Lecture and Recitation. The idea is to build progressively, starting with small skills in lecture.

Episodes are intended to tell a cohesive story of Microeconomics using animated visualizations. Episodes follow the same structure as Lectures. Some animations will be used in Lecture alongside the skills being developed in class. Animations cannot replace work on the board so I have both Lecture Notes and Episode Scripts. Eventually these two may converge, but it's difficult to get as much information on the screen as a whiteboard. So the Animations used in class will likely be different from those used in Episodes.

Every Part ends with a MiniExam that is followed by a Simulation introducing some of the ideas in the next Part.

=== Recitations

Recitations are primarily aimed at having students work on bigger skills, done in a structured way in Vignettes. The smaller skills are introduced in lecture then used as part of larger skills practiced in recitation. The TAs will guide students through the work, giving out all the solutions along the way after having them practice in groups. The grading is almost entirely completion based.

=== Skillsheets

Skillsheets are a structured way of organizing the core concepts and skills developed in the class. The idea is not to replace one's notes but to offer a container for the skills we develop in Lecture and the Vignettes done in Recitation. Each Part starts with the smaller skills in Lecture and extends to the larger skills developed in Vignettes. The aim is to show all the basic skills broken out in a structured way.

=== Homework

Homework is a set of questions that looks similar to what will be on the MiniExams, which is less structured than what's done on Skillsheets. Students are strongly encouraged to work together. Homework is submitted to be automatically graded on Gradescope on the Wednesdays that do not have a MiniExam.

=== Demos

Demos are essentially example MiniExams I do on camera.

=== MiniExams

MiniExams happen in lecture roughly every other Wednesday. I also want to organize the MEs so they are easier to have standards through time. I value having a bar and if students reach it, they get the grade. The way I'm grading right now feels a little to squishy. I'm not sure how to do this but it's something I'm thinking about.

I might ask a question on the ME about how difficult it was and how much time studying.

=== Vignettes and Homework
