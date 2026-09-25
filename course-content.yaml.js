// ECON 0100 course content. Edit the YAML between the two backtick lines and leave the
// wrapper alone. This is a .js file rather than a .yml for one reason: a page opened by
// double-clicking may load a neighbouring <script> and nothing else, so this is what lets
// the site work straight from disk as well as when served. Two things are off limits
// inside the YAML, a backtick and the pair ${ -- scripts/check-course refuses both.
window.COURSE_CONTENT_YAML = String.raw`
# ECON 0100 course content. The part-*.html pages read this in the browser, so an edit
# shows up on the next refresh with no build. scripts/check-course validates it; run it
# before committing. The format is documented in tayweid.github.io/course-assets/COURSE_CONTENT.md.
#
# Each block renders as the episode (+ reading) on the left and the practice
# path on the right: exercise in class, vignette in recitation, homework at
# home. Titles, thumbnails, icons, navigation anchors, and conventional
# filenames are generated automatically.
#
# Per block (folder is required once the block has a directory under Blocks/):
#   folder: A1_The_PPF     # the block's directory under Blocks/. It is the one thing a
#                          # browser cannot work out for itself, and the runtime pages
#                          # build conventional paths from it:
#                          #   Blocks/<folder>/Exercise/Exercise_<BLOCK>.pdf
#                          #   Blocks/<folder>/Vignette/Vignette_<BLOCK>.pdf
#                          #   Blocks/<folder>/Homework/Homework_<BLOCK>.pdf
#                          # Drop a conventionally named PDF in and it appears on its own;
#                          # solutions stay opt-in via solutions: true.
#
# Optional per block:
#   dates:                 # yyyy-mm-dd; a step's dot turns blue once its date has passed
#     class: '2026-08-31'
#     recitation: '2026-09-04'
#     homework: '2026-09-06'
#   exercise:              # only if the in-class exercise has downloads or a video
#     links: [{label: Exercise, file: Classwork/Classwork_A1.pdf}]
#     video: <youtube id>  # also allowed on vignette: and homework: — shows a small thumbnail on the step
#   extras:                # optional material; sits on the path above the episode
#     - name: Simulating a Market
#       video: <youtube id>
#     - name: A podcast    # no video: give it links, and an image for the thumbnail,
#       description: one short line under the name
#       links: [{label: Episode, file: https://...}]   # which opens the first link
#       image: https://... or Blocks/<folder>/media/<file>

course:
  code: ECON 0100
  title: Microeconomics
  brand: [MICRO, ECON]
  nav:
    - label: Office Hours
      lines:
        - '*Taylor* · Posvar 4702'
        - 'Wed & Thu 2:30–3:30'
        - '*Zoe* · Posvar 4925'
        - 'Tue & Thu 11–12'
        - 'Tue & Thu 2:30–3:30'
    - label: Syllabus
      file: Syllabus/Syllabus.pdf
      button: true
  checkpoint: Checkpoint
  reading: Reading/Ch_{nn}.pdf    # reading.chapter: 3 links Reading/Ch_03.pdf
  materials: Blocks               # conventional PDFs live under Blocks/<folder>/
  solutions: after_due            # a pushed ..._sols.pdf appears the day after its recitation or homework date

parts:
  A:
    title: The Core Economic Idea
    tagline: better choices can benefit everyone
    links: [{label: Skillsheet, file: Blocks/A_Skillsheet.pdf}]
    introduction: >-
      Part A explores one of the most profound insights in all of social science: we have both preferences and scarcity which means every choice requires giving something up, and that measuring the cost of a choice by the value of what we give up, there turns out to be a fundamental reason to coordinate with others. These concepts explain why we specialize, why cities flourish, and how strangers working together can create prosperity that benefits everyone. To show this, we’ll build the models that show the invisible forces that make civilization possible.
    sections:
      - block: A0
        folder: A0_Welcome
        nav: Econ
        steps:
          - name: Syllabus Quiz
            where: home
            date: '2026-08-30'
            links: [{label: Syllabus, file: Syllabus/Syllabus.pdf}]
        title: What is microeconomics?
        description: >-
          Microeconomics is about how we make decisions under constraints that arise from having both preferences and scarcity.
        episode:
          video: qMDU1QYKYss
          links: [{label: Animations, file: Blocks/A0_Welcome/media/EpisodeA0_present/, icon: fa fa-desktop}]
          description: Economics is not *about* money.
        reading:
          chapter: 1
          topic: Welcome to economics

      - block: A1
        folder: A1_The_PPF
        nav: PPF
        title: The production possibility frontier
        description: The PPF shows us what's attainable as individuals and as a society.
        episode:
          video: po4kip5m_QY
          links: [{label: Animations, file: Blocks/A1_The_PPF/media/EpisodeA1_present/, icon: fa fa-desktop}]
          description: The landscape of what's possible
        reading:
          chapter: 2
          topic: Choice in a world of scarcity
        exercise:
        vignette:
          description: PPF practice problems
        homework:
          file: A1
        dates:
          class: '2026-08-26'
          recitation: '2026-09-04'
          homework: '2026-08-30'

      - block: A2
        folder: A2_Advantage
        nav: Specialization
        title: Comparative advantage and specialization
        description: >-
          Minimizing opportunity cost by specializing in one's comparative advantage can bend out the PPF.
        episode:
          video: nclNGfY-3eA
          links: [{label: Animations, file: Blocks/A2_Advantage/media/EpisodeA2_present/, icon: fa fa-desktop}]
          description: Specialization
        reading:
          chapter: 19
          topic: International trade
        exercise:
        vignette:
          description: Specialization practice problems
        homework:
          file: A2
        dates:
          class: '2026-08-31'
          recitation: '2026-09-04'
          homework: '2026-09-06'

      - block: A3
        folder: A3_Trade
        nav: Trade
        title: Trade
        description: Trade based on comparative advantage makes both parties better off simultaneously.
        episode:
          video: v_s4dO1AD5Y
          links: [{label: Animations, file: Blocks/A3_Trade/media/EpisodeA3_present/, icon: fa fa-desktop}]
          description: Trade can make both parities better off.
        reading:
          name: Reading A3
          description: No reading in this block
        vignette:
          description: Trade practice problems
        homework:
          file: A3
        dates:
          class: '2026-09-02'
          recitation: '2026-09-04'
          homework: '2026-09-06'

      - checkpoint:
          reattempt: sign up on Canvas
          reattempt_when: Thu Oct 8, 2:30–4:30 PM, room TBA
          date: '2026-09-09'
          links:
            - {label: Solutions V1, file: Blocks/A_MiniExam/Checkpoint_A_1_sols.pdf}
            - {label: Solutions V2, file: Blocks/A_MiniExam/Checkpoint_A_2_sols.pdf}
            - {label: Solutions V3, file: Blocks/A_MiniExam/Checkpoint_A_3_sols.pdf}
            - {label: Solutions V4, file: Blocks/A_MiniExam/Checkpoint_A_4_sols.pdf}
          description: >-
            Checkpoint A covers everything in Part A. You will begin to learn that if you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            name: Demo A Walkthrough (Fall 2024)
            video: KH0MkPxWsig
            description: >-
              Attempt Demo A first, then walk through with me. The video is the Fall 2024 Demo A, with the same story and numbers. It walks through the first parts of each question; the later parts are new this year and use the same skills. Where the video answers "attainable? yes" in Q2, this year's sheet asks you to say "inefficient."
            links: [{label: Demo A, file: Blocks/A_MiniExam/Demo_A.pdf}]

  B:
    title: How Competitive Markets Work
    tagline: prices can coordinate buyers and sellers
    links: [{label: Skillsheet, file: Blocks/B_Skillsheet.pdf}]
    introduction: >-
      In Part A we set up the landscape of what’s possible but didn’t choose *which* point is best. Part B introduces preferences within competitive markets as a coordination device, allowing large groups to efficiently produce and distribute the things we want. This efficiency is amazing, but as we’ll show in Part C, it doesn’t work in every environment.
    sections:
      - block: B1
        folder: B1_Demand
        nav: Demand
        title: Demand
        description: Demand curves show how much consumers are willing to buy at each price.
        episode:
          video: 9HUh9qWDSr4
          links: [{label: Animations, file: Blocks/B1_Demand/media/EpisodeB1_present/, icon: fa fa-desktop}]
          description: "*This video introduces the demand curve as a way of organizing buyers' preferences.*"
        reading:
          chapter: 3
          topic: Demand and supply
        vignette:
          description: "*Demand practice problems*"
          files: B1
        homework:
          file: B1
        dates:
          class: '2026-09-14'
          recitation: '2026-09-11'
          homework: '2026-09-20'

      - block: B2
        folder: B2_Supply
        nav: Supply
        title: Supply
        description: Supply curves show how much producers are willing to sell at each price.
        episode:
          video: 0WoBKpFMLwo
          links: [{label: Animations, file: Blocks/B2_Supply/media/EpisodeB2_present/, icon: fa fa-desktop}]
          description: "*This video introduces the supply curve and how it helps answer Part B's questions.*"
        reading:
          name: Chapter (continued)
          description: Continues Chapter 3 from Block B1
        vignette:
          description: "*Supply practice problems*"
          files: B2
        homework:
          file: B2
        dates:
          class: '2026-09-16'
          recitation: '2026-09-18'
          homework: '2026-09-20'

      - block: B3
        folder: B3_Equilibrium
        nav: Equilibrium
        title: Equilibrium
        description: Markets find the equilibrium price where quantity supplied equals quantity demanded.
        episode:
          video: 8CQ3D2Kv2i0
          links: [{label: Animations, file: Blocks/B3_Equilibrium/media/EpisodeB3_present/, icon: fa fa-desktop}]
          description: >-
            *This video introduces shortage and surplus and the incentives of buyers and sellers to move prices toward equilibrium.*
        reading:
          chapter: 3
          topic: Price ceilings and price floors
        vignette:
          description: "*Markets practice problems*"
          files: B3
        homework:
          file: B3
        extras:
          - name: Simulating a Market
            video: PNtKXWNKGN8
            description: Excellent video from one of my favorite Youtube channels!
        dates:
          class: '2026-09-21'
          recitation: '2026-09-25'
          homework: '2026-09-27'

      - block: B4
        folder: B4_Efficiency
        nav: Efficiency
        title: Efficiency
        description: Competitive markets maximize total surplus, achieving social efficiency.
        episode:
          video: RC9vcoqQm-U
          links: [{label: Animations, file: Blocks/B4_Efficiency/media/B4_present/, icon: fa fa-desktop}]
          description: >-
            *This video introduces government price controls to show that the market maximizes total surplus in some environments.*
        reading:
          chapter: 3
          topic: Demand, supply, and efficiency
        vignette:
          description: "*Efficiency practice problems*"
        homework:
          file: B4
        dates:
          class: '2026-09-23'
          recitation: '2026-09-25'
          homework: '2026-09-27'

      - block: B5
        folder: B5_Changes
        nav: Changes
        title: Market Changes
        description: >-
          Elasticity measures how responsive quantity is to changes in price, income, or other factors. Comparative statics analyzes how equilibrium changes when supply or demand conditions shift.
        episode:
          description: "*How markets respond to changes*"
        reading:
          name: Reading B5
        vignette:
          description: "*Elasticity and comparative statics practice problems*"
        dates:
          class: '2026-09-28'
          recitation: '2026-10-02'
          homework: '2026-10-04'

      - block: B6
        folder: B6_Trade
        nav: Trade
        title: International Trade
        description: >-
          International trade improves welfare but also creates winners and losers, which can lead to political pressure for protectionist policies like tariffs.
        episode:
          video: Kxq2E69dpCA
          description: "*International Trade*"
        reading:
          chapter: 20
          topic: Globalization and protectionism
        vignette:
          description: "*International trade practice problems*"
        dates:
          class: '2026-09-30'
          recitation: '2026-10-02'
          homework: '2026-10-04'

      - checkpoint:
          reattempt: TBA
          date: '2026-10-05'
          description: >-
            Checkpoint B covers everything in Part B. If you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            video: yG7ahMJe8iA

  C:
    title: Externalities
    tagline: externalized costs and benefits lead to inefficient markets
    introduction: >-
      In Part A we set up the landscape of what’s possible and in Part B we introduced competitive markets as a coordination device to efficiently arbitrate which point on the PPF we should choose. But not every market is competitive or without externalities. Part C shows how private incentives can misalign with social welfare, creating externalities and market failures that require government intervention to improve efficiency. We’ll build the models to show how pollution, taxes, and corrective policies can either harm or correct market behavior.
    sections:
      - block: C1
        folder: C1_Tariffs
        nav: Tariffs
        title: Tariffs
        description: Political pressure to close the border, tariffs, inefficiency.
        episode:
          description: "*Tariffs*"
        vignette:
          description: "*Tariffs practice problems*"

      - block: C2
        folder: C2_Taxes_and_Subsidies
        nav: Taxes
        title: Taxes
        description: Taxes create deadweight loss by driving a wedge between what buyers pay and sellers receive, reducing total surplus.
        episode:
          video: R2NctbU80y0
          description: "*Taxes and Welfare*"
        reading:
          chapter: 5
          topic: Elasticity and tax incidence
          video: AYJh3NefuUM
        vignette:
          description: "*Taxes practice problems*"
          files: C2
          solutions: false
        dates:
          class: '2026-10-07'
          recitation: '2026-10-09'
          homework: '2026-10-11'

      - block: C3
        folder: C3_Externalities
        nav: Externalities
        title: Externalities
        description: When private costs don't equal social costs, markets produce too much or too little, creating inefficiency.
        episode:
          video: uxPoYbtzYbM
          description: "*Externalities*"
        reading:
          chapter: 12
          topic: Environmental protection and negative externalities
          video: prohFxS0E1I
        vignette:
          video: xKK5JBPXGsg
          description: "*Externalities practice problems*"
        homework:
          practice: hwc
        extras:
          - name: Planet Money
            description: Tax carbon, fix the climate
            image: 'https://media.npr.org/assets/img/2013/07/12/ross-sea-iceberg_wide-aa15abc1c67c120ac22f22f29ba3ffbebfdefb3f.jpg?s=600&c=85&f=jpeg'
            links:
              - {label: Episode 472, file: 'https://www.npr.org/sections/money/2013/07/12/201502003/episode-472-the-one-page-plan-to-fix-global-warming'}
              - {label: Revisited, file: 'https://www.npr.org/sections/money/2018/07/18/630267782/episode-472-the-one-page-plan-to-fix-global-warming-revisited'}
        dates:
          class: '2026-10-05'
          recitation: '2026-10-09'
          homework: '2026-10-11'

      - block: C4
        folder: C4_Corrective_Policy
        nav: Corrective Taxes
        title: Corrective Taxes
        description: Pigouvian taxes can internalize externalities and restore market efficiency by aligning private and social costs.
        episode:
          video: W0eAtssLxmk
          description: "*Corrective Taxes*"
        reading:
          chapter: 12
          topic: Environmental protection and negative externalities
          video: prohFxS0E1I
        vignette:
          description: "*Corrective taxes practice problems*"
        dates:
          class: '2026-10-12'
          recitation: '2026-10-16'
          homework: '2026-10-18'

      - checkpoint:
          reattempt: TBA
          date: '2026-10-19'
          description: >-
            Checkpoint C covers everything in Part C. You will begin to learn that if you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            video: lna7UhNOOro

  D:
    title: Strategic Interaction
    tagline: strategic interaction often leads to inefficient markets
    introduction: >-
      Part A set up the landscape of what’s possible. Part B introduced competitive markets as a coordination device to efficiently arbitrate which point on the PPF we should choose. And Part C showed that externalities break the efficiency of markets. In Part D we take this idea even further, into settings with strategic interaction, which we call game theory.
    sections:
      - block: D1
        folder: D1_Games
        nav: Common Resources
        title: Common Resources
        description: >-
          Common resources create market failures through the tragedy of the commons—when shared resources are overused because private incentives don't align with social benefits.
        episode:
          video: wd8LSB8nF7o
          description: "*Introducing non-excludable goods*"
        reading:
          chapter: 13
          topic: Positive externalities and public goods
        vignette:
          description: "*Non-excludable goods practice problems*"
          files: D1
        dates:
          class: '2026-10-19'
          recitation: '2026-10-23'
          homework: '2026-10-25'

      - block: D2
        folder: D2_The_Commons
        nav: Public Goods
        title: Public Goods
        description: >-
          Public goods create free-rider problems because they are non-excludable and non-rivalrous, leading to under-provision by private markets and the need for government intervention.
        episode:
          video: Is0CQbUM-j8
          description: "*Baby game theory*"
        reading:
          chapter: 13
          topic: Positive externalities and public goods
        vignette:
          description: "*Game theory practice problems*"
          files: D2
        dates:
          class: '2026-10-21'
          recitation: '2026-10-23'
          homework: '2026-10-25'

      - block: D3
        folder: D3_Public_Goods_and_Voting
        nav: Game Theory
        title: Game Theory
        description: >-
          Strategic interaction and Nash equilibrium provide a framework for analyzing decisions when outcomes depend on what others do, revealing why cooperation often fails even when it would benefit everyone.
        episode:
          video: s_ed6uwHOQI
          description: "*Baby game theory*"
        reading:
          name: Reading D3
        vignette:
          description: "*Game theory practice problems*"
          files: D3
        dates:
          class: '2026-10-26'
          recitation: '2026-10-30'
          homework: '2026-11-01'

        extras:
          - name: Veritasium Game Theory
            video: mScpHTIi-kM
      - block: D4
        folder: D4_Sequential_Games
        nav: Voting
        title: Voting
        description: >-
          Voting systems and collective choice reveal how individual preferences aggregate into social decisions, often leading to paradoxes and inefficiencies in democratic decision-making.
        episode:
          description: "*Voting and collective choice*"
        reading:
          name: Reading D4
        vignette:
          description: "*Voting systems practice problems*"
          files: D4
        dates:
          class: '2026-10-28'
          recitation: '2026-10-30'
          homework: '2026-11-01'

      - checkpoint:
          reattempt: TBA
          date: '2026-11-02'
          description: >-
            Checkpoint D covers everything in Part D. You will begin to learn that if you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            video: BYrsSbLdJuQ
            file: D1

  E:
    title: Sellers
    tagline: market power leads to inefficient markets
    introduction: >-
      In Part A through Part D we’ve explored why we would want to coordinate and how to make coordination possible. Markets can organize economic activity efficiently in some contexts and fail in other contexts. In Part E build a model of sellers that shows how markets are not efficient when sellers have Market Power, the ability to impact the market for their own gain. 
    sections:
      - block: E1
        folder: E1_Costs
        nav: Costs
        title: Costs of Production
        description: Firms transform inputs into outputs through production functions and minimize costs to determine their supply decisions.
        episode:
          video: J0Y6XzwSfls
          description: "*The costs of production*"
        reading:
          chapter: 7
          topic: Production, costs, and industry structure
        vignette:
          description: "*Production costs practice problems*"
          files: E1
        dates:
          class: '2026-11-02'
          recitation: '2026-11-06'
          homework: '2026-11-08'

      - block: E2
        folder: E2_Competition
        nav: Competition
        title: Competitive Firms
        description: Perfect competition emerges when firms are price-takers with no individual market power over the equilibrium price.
        episode:
          video: YN4ZkPBS_O8
          description: "*Competitive firms*"
        reading:
          chapter: 8
          topic: Perfect competition
        vignette:
          description: "*Competitive firms practice problems*"
          files: E2
        dates:
          class: '2026-11-04'
          recitation: '2026-11-06'
          homework: '2026-11-08'

      - block: E3
        folder: E3_Monopoly
        nav: Monopoly
        title: Monopoly
        description: Market power allows firms to influence prices and capture profits at the expense of consumer welfare and economic efficiency.
        episode:
          video: N0mbUXYMwdw
          description: "*Monopoly firms*"
        reading:
          chapter: 9
          topic: Monopoly
        vignette:
          description: "*Monopoly practice problems*"
        dates:
          class: '2026-11-09'
          recitation: '2026-11-13'
          homework: '2026-11-15'

      - block: E4
        folder: E4_Duopoly
        nav: Market Structures
        title: Market Structures
        description: Comparing perfect competition, monopolistic competition, oligopoly, and monopoly reveals how market structure determines economic outcomes.
        episode:
          video: UIXf362W-rU
          description: "*Comparing market structures*"
          links:
            - label: Notes
              file: Blocks/E4_Duopoly/04_Handwritten.pdf
        reading:
          chapter: 10
          topic: Monopolistic competition and oligopoly
        vignette:
          description: "*Market structures practice problems*"
        dates:
          class: '2026-11-11'
          recitation: '2026-11-13'
          homework: '2026-11-15'

      - checkpoint:
          reattempt: TBA
          date: '2026-11-30'
          description: >-
            Checkpoint E covers everything in Part E. You will begin to learn that if you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            video: UZDvSTNbv0w
          extras:
            - name: Demo E3
              video: jwxiRNAPBLc
              files: E3


  F:
    title: Buyers
    tagline: people respond to many interacting incentives
    introduction: >-
      Part F brings us full circle, exploring what to do when we can’t have everything. We start by connecting Factor Markets and the Labor Market to buyer’s income in Final Goods markets, which shapes their Budget Constraint. To understand choices within this constraint, we rank preferences using Utility and map Indifference Curves. The Consumer’s Problem is solved at the highest attainable indifference curve within the budget constraint, where the Marginal Rate of Substitution equals the Marginal Rate of Transformation. 
    sections:
      - block: F1
        folder: F1_The_Consumers_Problem
        nav: Factor Markets
        title: Factor Markets
        description: Factor markets determine the income that households earn from selling their labor and capital, which becomes the budget constraint for consumer choice.
        episode:
          description: "*Factor markets*"
        reading:
          chapter: 4
          topic: Labor and financial markets
        vignette:
          video: n3LpswjCp6w
          description: "*Factor markets practice problems with video walkthrough*"
          files: F1
        dates:
          class: '2026-11-30'
          recitation: '2026-12-04'
          homework: '2026-12-06'

      - block: F2
        folder: F2_Factor_Markets
        nav: Consumer Choice
        title: Consumer Choice
        description: Given their budget constraint from factor markets, consumers maximize utility by choosing the optimal combination of goods where marginal utility per dollar is equal across all goods.
        episode:
          description: "*Consumer choice*"
        reading:
          chapter: 6
          topic: Consumer choices
        vignette:
          video: l2uq30_Cg10
          description: "*Consumer choice practice problems with video walkthrough*"
          files: F2
          solution_file: Vignettes/Vignette_F2_sols_new.pdf
        dates:
          class: '2026-12-02'
          recitation: '2026-12-04'
          homework: '2026-12-06'

      - checkpoint:
          reattempt: TBA
          when: Final Exam Period
          description: >-
            You will begin to learn that if you understand the concepts and do the work in the Vignettes, Homework, and Demo, you're going to be in good shape on the Checkpoint.
          demo:
            video: zkn0CXaNOJY
            file: F1
          extras:
            - name: Demo F2
              video: DVHvgb_kJDY
              files: F2
`;
