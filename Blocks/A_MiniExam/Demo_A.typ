// Exported from Plass
#set page(paper: "us-letter", margin: 0.6in)
#set par(justify: true, leading: 8.172pt, spacing: 17.172pt)
#set list(spacing: 10.672pt)
#set enum(spacing: 10.672pt)
#show heading.where(level: 1): set text(size: 19.000pt)
#show heading.where(level: 1): set block(above: 21.113pt, below: 20.084pt)
#show heading.where(level: 1): set par(leading: 10.777pt)
#show heading.where(level: 2): set text(size: 14.000pt)
#show heading.where(level: 2): set block(above: 35.720pt, below: 15.950pt)
#show heading.where(level: 2): set par(leading: 7.941pt)
#show heading.where(level: 3): set text(size: 11.500pt)
#show heading.where(level: 3): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 3): set par(leading: 6.523pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 8.000pt)
#show math.equation.where(block: true): set block(above: 17.192pt, below: 18.962pt)
#set text(size: 10pt, font: "New Computer Modern", hyphenate: true)

// ---------------------------------------------------------------------------
// EDITOR'S NOTES (Claude, 2026-09-07). Plass deletes these comments on save:
// read them before editing in Plass, or edit this file in a text editor.
//
// SOURCE. The F24 Demo A (Colin Creevey 20 pasties or 5 cakes; Katie Bell 15
// or 8), from ECON_0100/Checkpoints/A/_Archive/24F_Demo_A.md, in the Checkpoint
// page layout. Q2 and Q3 wording taken from the exam versions because the F24
// Demo's Q2 asked yes/no attainability and its Q3 sentence was garbled.
// Solutions to the unsplit original: _Archive/Demo_A_sols.pdf ("Taylor's
// Version" scan). Note: this Demo is Vignettes A1-A3 word for word.
//
// SPLIT along skill lines, one question per skill, skill code in the heading:
// old Q1 -> Q1 and Q2(a); old Q2 -> Q2(b); old Q3 -> Q3; old Q4 -> Q4(b);
// old Q5 -> Q2(h) and Q4(d). Stems restated so each question stands alone.
//
// TAYLOR'S TEXT: everything not tagged. Boilerplate is the Checkpoint's with
// "Checkpoint" and "20 minutes" substituted, plus the Demo paragraph with the
// email dropped and "classmakes" corrected. The sentence "Each question is
// labeled with the skill it practices from Skillsheet A" is Claude's, kept at
// Taylor's request.
//
// CLAUDE'S ADDITIONS, each tagged *[Claude]* in the text for Taylor to rewrite
// and untag. They give the Demo every question type that appears on Checkpoint
// A, copying the Arthur exam's wording with Colin's numbers:
//   Q2(c)-(e)  yes/no attainability: 20P yes (efficient); 20P and 1C no;
//              19P yes (inefficient).
//   Q2(f)-(g)  shift vs pivot. Lead-in point 8P and 3C is efficient
//              (20 - 4*3 = 8). Pasty spell x3 -> pivot out -> inefficient.
//              Labor cut -> shift in -> unattainable.
//   Q4 table   given OC table so Q4 stands alone and shows the read-a-table
//              type: Colin 1/4 C per P, 4 P per C; Katie 8/15 C per P,
//              15/8 P per C.
//   Q4(a)      who specializes in cakes: Katie (15/8 < 4).
//   Q4(c)      select-all for 1 cake: 2 and 3 pasties work (range 15/8 to 4);
//              1 and 5 do not. Two correct options where F24 lists had one.
//
// ANSWERS to the original items. Q1: 4 P. Q2(b): inefficient (frontier 12 P
// at 2 C). Q2(h): 8-hour PPF has intercepts 32 P and 8 C, parallel. Q3: AA in
// pasties Colin, CA in pasties Colin (OC of a pasty 1/4 C vs 8/15 C).
// Q4(b): any rate between 15/8 and 4 P per cake. Q4(d): still 4 P; hours
// shift the PPF without changing its slope.
//
// SKILLSHEET BULLETS STILL UNCOVERED, for Taylor to write: A1.1 next best
// alternative, reciprocals; A1.2 slope as the OC of the horizontal good;
// A2.1 AA and CA in cakes, and AA-in-both (the numbers can't show it: Colin
// has AA in pasties, Katie in cakes); A3.1 range of rates as a range, beyond
// autarky and who rejects, effect of the capacity change on the trade.
//
// LAYOUT. Graph padding removed so the Demo fits one sheet front and back;
// Q2 flows onto the back. The website link in course-content.yaml.js points
// at Blocks/A_MiniExam/Demo_A.pdf, exported from Plass; scripts/check-course
// reports it missing until that export exists.
// ---------------------------------------------------------------------------

#align(center, text(size: 1.55em, weight: 700)[ECON 0100 | Fall 2026 | Demo A])

#align(center, line(length: 96pt, stroke: 0.5pt))

This Checkpoint will take 20 minutes with quick break to follow. Checkpoints are designed to both test your knowledge and challenge you to apply familiar concepts in new environments. Treat it as if you're trying to show me that you understand the material. Answer clearly and completely.

Demos are similar to Checkpoints, often taken directly from past semesters. The goal is to both test your knowledge and provide a venue for practice. Work through the problems and check your work against mine. Practice answering clearly and completely. Show your work so someone else can understand your thought process. You are encouraged to work in small groups. Find a study room, grab some classmates, and work together on a whiteboard. Each question is labeled with the skill it practices from Skillsheet A.

== Academic Conduct Code

The following academic conduct code is designed to protect the integrity of your work. Print your name/initials beside the three academic honesty agreements. I pledge to my fellow students, the university, and the instructor, that:

\_\_\_\_ I will complete this Checkpoint solely using my own work.

\_\_\_\_ I will not use any digital resources unless explicitly allowed by the instructor.

\_\_\_\_ I will not communicate directly or indirectly with others during the Checkpoint.

== Q1 | A1.1 | Opportunity Cost

Colin Creevey can bake $20$ cornish pasties or $5$ cauldron cakes in one day. What is Colin's opportunity cost of producing $1$ cake?

Colin's opportunity cost of one cake: \_\_\_\_\_\_\_\_\_\_

== Q2 | A1.2 | The PPF

Colin Creevey can bake $20$ cornish pasties or $5$ cauldron cakes in one day.

a) Set up Colin's PPF on an $x$,$y$ graph with pasties on the vertical and cakes on the horizontal.

b) Suppose Colin bakes $10$ pasties and $2$ cakes in one day. Is this inefficient, efficient, or unattainable? Use the graph above or algebra to justify your answer.

Inefficient, Efficient, or Unattainable: \_\_\_\_\_\_\_\_\_\_

c) *[Claude]* Is a daily output of $20$ pasties attainable for him? \_\_\_\_\_\_\_\_\_\_

d) *[Claude]* Is a daily output of $20$ pasties and $1$ cake attainable for him? \_\_\_\_\_\_\_\_\_\_

e) *[Claude]* Is a daily output of $19$ pasties attainable for him? \_\_\_\_\_\_\_\_\_\_

*[Claude]* For the following two subquestions, suppose a daily output of $8$ pasties and $3$ cakes is efficient for Colin.

f) *[Claude]* If Colin discovers a new pasty baking spell which triples his daily output of pasties, is $8$ pasties and $3$ cakes unattainable, efficient, or inefficient? \_\_\_\_\_\_\_\_\_\_

g) *[Claude]* If Colin decides to cut back how much labor he devotes to baking, is $8$ pasties and $3$ cakes unattainable, efficient, or inefficient? \_\_\_\_\_\_\_\_\_\_

h) It turns out Colin wants to add hours to his job. So he increases from $5$ to $8$ hours per day. Set up Colin's old and new PPF on the same graph.

== Q3 | A2.1 | Absolute & Comparative Advantage

Colin Creevey can bake $20$ cornish pasties or $5$ cauldron cakes in one day. Katie Bell also bakes cornish pasties and cauldron cakes at a neighboring bakery. She can bake $15$ pasties or $8$ cakes in one day. Set up a production table with both Colin and Katie's output per day. Who has the absolute advantage (AA) in pasties? Then set up an opportunity cost table with Colin and Katie's opportunity costs for each good. Who has the comparative advantage (CA) in pasties?

AA in Pasties: \_\_\_\_\_\_\_\_\_\_

CA in Pasties: \_\_\_\_\_\_\_\_\_\_

== Q4 | A3.1 | Specialization & Trade

Colin Creevey can bake $20$ cornish pasties or $5$ cauldron cakes in one day. Katie Bell can bake $15$ pasties or $8$ cakes in one day. *[Claude]* Their opportunity costs are listed in the following opportunity cost table.

#align(center, table(
  columns: 3,
  [], [*Pasty*], [*Cake*],
  [*Colin*], [1/4 Cake], [4 Pasties],
  [*Katie*], [8/15 Cake], [15/8 Pasties],
))

a) *[Claude]* If Colin and Katie were to specialize and trade with each other, which baker should specialize in cakes? \_\_\_\_\_\_\_\_\_\_

b) Suppose Colin and Katie realize they can specialize and trade goods. After they specialize, what is a trade that would make them both better off?

$1$ Cake for \_\_\_\_\_\_\_\_\_\_ Pasties

c) *[Claude]* Select all the exchange rates which could facilitate a trade between the two bakers.

#quote(block: true)[
  $square$ 1 Cake for 1 Pasty

  $square$ 1 Cake for 2 Pasties

  $square$ 1 Cake for 3 Pasties

  $square$ 1 Cake for 5 Pasties
]

d) It turns out Colin wants to add hours to his job. So he increases from $5$ to $8$ hours per day. What is Colin's new opportunity cost of cake?

Colin's _new_ opportunity cost of one cake: \_\_\_\_\_\_\_\_\_\_
