# maniml E5_Animation.py EpisodeE5
# Storyboard: E5_Notes.md. All lesson choreography stays in construct().
# The Part E wrap-up: the steps of Taylor's sheet "Example: Three Market Structures" (E5_Handwritten_Three_Markets.pdf),
# the firm's five steps for one seller, two and many, then n sellers, on the market E2, E3 and E4 share.
# D: P = 120 - Q; every firm is E1 and E2's: TC = 1000 + q^2, MC = 2q, ATC = q + 1000/q. Monopoly 30 at 90, profit 800;
# duopoly 24 each at 72; competitive (the same line read in thousands) E2's example: P = 100, q = 50, profit 1,500, then
# entry to the long run, P = 63.25. (Until 2026-11-11 this used the sheet's own market, P = 200 - Q/2 and MC = 20 + q;
# that build is _archive/2026-11-11_consolidation/E5_Animation_handwritten_sheet_market.py.)
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-02T23:47:58Z"
# ///

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *
from style import axes as style_axes

config.frame_rate = 15


class EpisodeE5(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.45, -2.65
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        PRICE_SCALE = 0.62                         # Price readouts on the vertical axis.
        WORD_SCALE = 0.7                           # Curve names at the curve ends.
        BAR_GAP = 0.08
        PROFIT_OPACITY, DWL_OPACITY_STRIPS = AREA_OPACITY, 0.8
        # Layout: the graph left, a grey divider, the firm's-problem card and the side solve right.
        DIVIDER_X = 2.95
        PANEL_LEFT, PANEL_TOP, PANEL_WIDTH = 3.25, 2.45, 4.45
        CARD_HEIGHT = 2.55                         # The card's steps, under its head, in the panel.
        # The side solve under the card; 4.b.symmetry's five lines must clear the bottom strip.
        WORK_SCALE, WORK_GAP, CARD_TO_WORK = 0.62, 0.16, 0.3
        # The market graph (sections 3, 4.c, 6, 7) and the two graphs of section 5.
        MARKET_X, MARKET_Y = -6.1, -2.25
        BR_X, BR_Y = -5.0, -2.25
        # The firm's MR name and the market's P* readout share a line in section 5: keep them apart.
        FIRM_X, SMALL_MARKET_X = -6.5, -1.45
        ATC_FROM = 9.2                             # ATC starts at q = 9.2 (ATC 118), clear of the price axis.
        # Top-level z order (the engine sorts top-level mobjects by z_index).
        FILL_LAYER, WORD_LAYER, GUIDE_LAYER, DOT_LAYER = -1, 6, 10, 30

        # The model, as one-line functions (Q market output, q one firm's output).
        FC = 1000
        TOP_PRICE, X_END, Y_TOP = 120, 120, 140     # demand's start and foot; the market graph's axes (E3's and E4's)
        MC_END, ATC_END, BR_END = 60, 85, 140       # MC is drawn to (60, 120), ATC to q = 85; the best-response axes
        d = lambda Q: TOP_PRICE - Q
        mr = lambda q: TOP_PRICE - 2 * q
        mc = lambda q: 2 * q
        atc = lambda q: q + FC / q
        # n similar sellers, each choosing q with MR_i = P - q = MC = 2q.
        firm_q = lambda n: 120 / (n + 3)
        market_q = lambda n: n * firm_q(n)
        # Part E's firm palette (shared_E.md).
        MC_COLOR, ATC_COLOR, MR_COLOR = SUPPLY, TOTAL, PINK

        teaching = lambda text: (Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                 .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # One line of a side solve. Results are red and boxed, as on the sheet.
        work_line = lambda text, color=INK: Tex(text, color=color).scale(WORK_SCALE)

        # ---- 0.a · The shared bumper, with the thesis line the notes offer (Taylor's earlier line from E3).
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 5)
        thesis = Tex(r'\textit{The fewer sellers, the worse.}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · The sheet's header: one market, and every firm has the same marginal cost.
        head = title('Three Market Structures')
        context = subtitle(head, 'All firms are similar.')
        header = VGroup(Tex(r'$D$: $P = 120 - Q$', color=DEMAND),
                        Tex(r'$MC = 2q$', color=MC_COLOR)).scale(0.95)
        header.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, 1.0, 0])
        self.play(FadeIn(head), FadeIn(context), FadeIn(header))
        self.pause('1.a')

        # ---- 1.b · The sheet's three columns: monopoly, duopoly, competitive, each with its marginal revenue.
        column_x = (-4.9, 0, 4.9)
        heads = VGroup(*[Tex(word, color=INK).scale(0.85).move_to([x, -0.65, 0])
                         for word, x in zip(('Monopoly', 'Duopoly', 'Competitive'), column_x)])
        arrows = VGroup(*[Arrow(heads[k].get_right(), heads[k + 1].get_left(), buff=0.4, color=MUTED, thickness=2)
                          for k in range(2)])
        columns = VGroup(
            VGroup(Tex(r'$MR_A = 120 - 2q_A$', color=MR_COLOR), Tex(r'$Q = q_A$', color=INK)),
            VGroup(Tex(r'$MR_A = 120 - 2q_A - q_B$', color=ROW_PLAYER),
                   Tex(r'$MR_B = 120 - 2q_B - q_A$', color=COL_PLAYER)),
            VGroup(Tex(r'$MR = P$', color=DEMAND)))
        for column, column_head in zip(columns, heads):
            column.scale(0.68).arrange(DOWN, buff=0.28).next_to(column_head, DOWN, buff=0.45)
        note = teaching('What happens to price and quantity as sellers are added?')
        self.play(LaggedStart(*[FadeIn(VGroup(column_head, column)) for column_head, column in zip(heads, columns)],
                              lag_ratio=0.6), FadeIn(arrows), FadeIn(note), run_time=2.4)
        self.pause('1.b')

        # ---- 2.a · The firm's problem, as the sheet writes it, one step at a time.
        self.remove(head, context, note)
        self.play(FadeOut(header), FadeOut(heads), FadeOut(arrows), FadeOut(columns), run_time=0.6)
        head = title("The Firm's Problem")
        # The card's wording matches E4_Animation.py's (the sheet's, upright curve names, no added punctuation).
        objective = Tex(r'$\max\limits_{q}\ \pi = \mathrm{TR} - \mathrm{TC}$', color=INK)
        steps = VGroup(
            Tex(r'1. $\mathrm{MC} = \mathrm{MR} \rightarrow q^*$', color=INK),
            Tex(r'2. $q^* \rightarrow \mathrm{D} \rightarrow P^*$', color=INK),
            Tex(r'3. $q^* \rightarrow \mathrm{ATC} \rightarrow \mathrm{ATC}^*$', color=INK),
            Tex(r'4. $\pi^* = (P^* - \mathrm{ATC}^*)\cdot q^*$', color=INK),
            VGroup(Tex(r'5. If $\pi^* \geq 0$ stay/enter', color=INK),
                   Tex(r'If $\pi^* < 0$ exit', color=INK)).arrange(DOWN, aligned_edge=LEFT, buff=0.16))
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        # The second line of step 5 hangs under the first line's "If".
        steps[4][1].shift(RIGHT * (Tex('5.').width + 0.2))
        problem = VGroup(objective, steps).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        problem.scale(0.85).move_to([0, BODY_MID + 0.15, 0])
        note = teaching('Every seller solves the same problem.')
        self.play(FadeIn(head), FadeIn(objective), FadeIn(note))
        self.play(LaggedStart(*[FadeIn(step, shift=RIGHT * 0.2) for step in steps], lag_ratio=0.5), run_time=2.5)
        self.pause('2.a')

        # The card's place beside every graph: a small head, then the problem in grey, the current step gold.
        card_head = Tex(r"\textsf{The Firm's Problem}", color=TITLE).scale(0.62)
        card_head.move_to([PANEL_LEFT, PANEL_TOP, 0], aligned_edge=UL)
        side_problem = problem.copy().set_color(CAPTION)
        side_problem.scale(min(PANEL_WIDTH / side_problem.width, CARD_HEIGHT / side_problem.height))
        side_problem.next_to(card_head, DOWN, buff=0.25, aligned_edge=LEFT)
        WORK_TOP = side_problem.get_bottom()[1] - CARD_TO_WORK
        divider = Line([DIVIDER_X, -3.0, 0], [DIVIDER_X, 2.45, 0], color=MUTED, stroke_width=1.5)
        focus = lambda *active: [step.animate.set_color(DEFINITION if k + 1 in active else CAPTION)
                                 for k, step in enumerate(steps)]

        # The market graph: E3's and E4's axes, Q to 120 and P to 140, with room above 120 for P.
        ax = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=7.4, y_length=4.6)
        ax.shift(np.array([MARKET_X, MARKET_Y, 0]) - ax.c2p(0, 0))
        axis_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, Y_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, Y_TOP), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(X_END, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(X_END, 0), DOWN, buff=0.73))
        demand_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE, 0), color=DEMAND, stroke_width=3)
        demand_word = Tex('D', color=INK).scale(WORD_SCALE).next_to(ax.c2p(TOP_PRICE, 0), UR, buff=0.12)
        demand_intercept = Tex('$120$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, TOP_PRICE), LEFT, buff=0.15)

        # ---- 3.a · Monopoly: the sheet's four curves on the market graph; the card moves beside it.
        mr_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2, 0), color=MR_COLOR, stroke_width=3)
        mc_line = Line(ax.c2p(0, 0), ax.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=3)
        atc_curve = polyline([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, ATC_END, 240)], ATC_COLOR, 3)
        monopoly_words = VGroup(
            Tex('MR', color=INK).scale(WORD_SCALE).next_to(ax.c2p(TOP_PRICE / 2, 0), UR, buff=0.12),
            Tex('MC', color=INK).scale(WORD_SCALE).next_to(ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15),
            Tex('ATC', color=INK).scale(WORD_SCALE).next_to(ax.c2p(ATC_END, atc(ATC_END)), RIGHT, buff=0.15))
        self.remove(head, note)
        head = title('Monopoly')
        context = subtitle(head, r'One seller: $Q = q_A$.')
        note = teaching("The monopolist faces the market's downward-sloping demand.")
        self.play(FadeIn(head), FadeIn(context), Transform(problem, side_problem), FadeIn(card_head), FadeIn(divider),
                  FadeIn(ax), FadeIn(axis_words), FadeIn(demand_line), FadeIn(demand_word), FadeIn(demand_intercept),
                  FadeIn(mr_line), FadeIn(mc_line), FadeIn(atc_curve), FadeIn(monopoly_words),
                  FadeIn(note), run_time=1.6)
        self.pause('3.a')

        # ---- 3.b · Step 1: MR = MC at q* = 30, the sheet's side solve; the dot traces down to q*.
        work = VGroup(work_line(r'$2q = 120 - 2q$'), work_line(r'$4q = 120$'),
                      work_line(r'$q^* = 30$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        choice_dot = Dot(ax.c2p(30, 60), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        quantity_guide = DashedLine(ax.c2p(30, 60), ax.c2p(30, 0), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        quantity_word = VGroup(
            Tex('30', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(30, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(30, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(note)
        note = teaching(r'Every unit up to $q^*$ adds more to revenue than to cost.')
        self.play(*focus(1), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]), FadeIn(work_box), FadeIn(choice_dot))
        self.play(Create(quantity_guide), FadeIn(quantity_word))
        self.pause('3.b')

        # ---- 3.c · Step 2: up from q* to demand, P* = 90; each readout dashed in its own curve's color.
        up_guide = DashedLine(ax.c2p(30, 60), ax.c2p(30, 90), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        price_dot = Dot(ax.c2p(30, 90), radius=0.07, color=DEMAND).set_z_index(DOT_LAYER)
        price_guide = DashedLine(ax.c2p(30, 90), ax.c2p(0, 90), color=DEMAND, stroke_width=2).set_z_index(GUIDE_LAYER)
        price_word = Tex(r'$P^* = 90$', color=DEMAND).scale(PRICE_SCALE).next_to(ax.c2p(0, 90), LEFT, buff=0.2)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$P = 120 - 30$'),
                      work_line(r'$P^* = 90$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'The price is what buyers will pay for $q^*$ units.')
        self.play(*focus(2), FadeIn(work[0]), FadeIn(note))
        self.play(Create(up_guide), FadeIn(price_dot))
        self.play(Create(price_guide), FadeIn(price_word), FadeIn(work[1]), FadeIn(work_box))
        self.pause('3.c')

        # ---- 3.d · Step 3: ATC* = 63.33, where q* meets ATC.
        atc_dot = Dot(ax.c2p(30, atc(30)), radius=0.07, color=ATC_COLOR).set_z_index(DOT_LAYER)
        atc_guide = DashedLine(ax.c2p(30, atc(30)), ax.c2p(0, atc(30)), color=ATC_COLOR, stroke_width=2).set_z_index(GUIDE_LAYER)
        # The number alone: the full ATC* = 63.33 would run off the left edge of the frame.
        atc_word = Tex(r'$63.33$', color=ATC_COLOR).scale(PRICE_SCALE).next_to(ax.c2p(0, atc(30)), LEFT, buff=0.2)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$ATC^* = 30 + 1000/30$'),
                      work_line(r'$ATC^* = 63.33$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Average total cost: the cost per unit of making $q^*$ units.')
        self.play(*focus(3), FadeIn(atc_dot), FadeIn(note))
        self.play(Create(atc_guide), FadeIn(atc_word), FadeIn(work), FadeIn(work_box))
        self.pause('3.d')

        # ---- 3.e · Step 4: profit, (90 - 63.33) x 30 = 800, as one-unit strips between ATC* and P*.
        profit = VGroup()
        for q in range(30):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            profit.add(Polygon(ax.c2p(left, atc(30)), ax.c2p(right, atc(30)), ax.c2p(right, 90), ax.c2p(left, 90),
                               stroke_width=0, fill_color=SUPPLY, fill_opacity=PROFIT_OPACITY))
        profit.set_z_index(FILL_LAYER)
        profit_word = Tex('Profit', color=INK).scale(0.72).move_to(ax.c2p(15, (90 + atc(30)) / 2)).set_z_index(WORD_LAYER)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$\pi^* = (90 - 63.33)\cdot 30$'),
                      work_line(r'$\pi^* = 800$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Profit: the price minus the cost per unit, on each of the $q^*$ units.')
        self.play(*focus(4), FadeIn(work[0]), FadeIn(note))
        self.play(LaggedStart(*[FadeIn(strip) for strip in profit], lag_ratio=0.1), run_time=2)
        self.remove(*profit)
        self.add(profit)
        self.play(FadeIn(profit_word), FadeIn(work[1]), FadeIn(work_box))
        self.pause('3.e')

        # ---- 3.f · Step 5, in the sheet's words.
        self.remove(note)
        note = teaching(r"No entry, because it's a monopoly.")
        self.play(*focus(5), FadeIn(note))
        self.pause('3.f')

        # ---- 3.g.efficient · Q_sp = 40, where MC meets demand (yellow, as on the sheet).
        efficient_dot = Dot(ax.c2p(40, 80), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER)
        efficient_guide = DashedLine(ax.c2p(40, 80), ax.c2p(40, 0), color=FOCUS, stroke_width=2).set_z_index(GUIDE_LAYER)
        efficient_word = VGroup(
            Tex('40', color=FOCUS).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$Q_{sp}$', color=FOCUS).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(work, work_box)
        work = VGroup(work_line(r'$2Q = 120 - Q$'), work_line(r'$3Q = 120$'),
                      work_line(r'$Q_{sp} = 40$', FOCUS)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        self.remove(note)
        note = teaching(r'$Q_{sp}$: the socially efficient quantity, where marginal cost meets demand.')
        self.play(*focus(), FadeIn(work[0]), FadeIn(work[1]), FadeIn(note))
        self.play(FadeIn(work[2]), FadeIn(efficient_dot))
        self.play(Create(efficient_guide), FadeIn(efficient_word))
        self.pause('3.g.efficient')

        # ---- 3.g · DWL: the units between q* and Q_sp, from MC up to demand, as grey strips.
        loss = VGroup()
        for q in range(30, 40):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            loss.add(Polygon(ax.c2p(left, mc(left)), ax.c2p(right, mc(right)), ax.c2p(right, d(right)), ax.c2p(left, d(left)),
                             stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY_STRIPS))
        loss.set_z_index(FILL_LAYER)
        # The triangle is too narrow for its name: DWL sits just above its top edge, left of MC.
        loss_word = Tex('DWL', color=INK).scale(0.6).move_to(ax.c2p(37, 99)).set_z_index(WORD_LAYER)
        self.remove(note)
        note = teaching(r'DWL: every unit between $q^*$ and $Q_{sp}$, from MC up to demand.')
        self.play(LaggedStart(*[FadeIn(strip) for strip in loss], lag_ratio=0.18), FadeIn(note), run_time=1.6)
        self.remove(*loss)
        self.add(loss)
        self.play(FadeIn(loss_word))
        self.pause('3.g')

        # ---- 4.a · Duopoly: the best-response graph from the sheet, and firm A's side solve.
        monopoly_picture = [ax, axis_words, demand_line, demand_word, demand_intercept, mr_line, mc_line, atc_curve,
                            monopoly_words, choice_dot, quantity_guide, quantity_word, up_guide,
                            price_dot, price_guide, price_word, atc_dot, atc_guide, atc_word, profit, profit_word,
                            efficient_dot, efficient_guide, efficient_word, loss, loss_word]
        self.remove(head, context, note, work)
        self.play(*[FadeOut(m) for m in monopoly_picture], *focus(), run_time=0.8)
        head = title('Duopoly')
        context = subtitle(head, r'Two sellers: $Q = q_A + q_B$.')
        # E4's best-response graph: both axes to 140, so each best response runs from axis to axis as on the sheet.
        br_ax = style_axes([0, BR_END, 20], [0, BR_END, 20], x_length=4.4, y_length=4.4)
        br_ax.shift(np.array([BR_X, BR_Y, 0]) - br_ax.c2p(0, 0))
        # BR_A's name sits right of the q_B axis near its top, so that axis's caption sits under q_B (C4's form).
        q_b_word = Tex('$q_B$', color=INK).scale(0.8).next_to(br_ax.c2p(0, BR_END), LEFT, buff=0.23)
        br_words = VGroup(
            q_b_word,
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(q_b_word, DOWN, buff=0.08),
            Tex('$q_A$', color=INK).scale(0.8).next_to(br_ax.c2p(BR_END, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(br_ax.c2p(BR_END, 0), DOWN, buff=0.73))
        br_a = Line(br_ax.c2p(30, 0), br_ax.c2p(0, 120), color=ROW_PLAYER, stroke_width=3)
        br_a_word = Tex('$BR_A$', color=INK).scale(WORD_SCALE).next_to(br_ax.c2p(0, 120), RIGHT, buff=0.22)
        work = VGroup(work_line(r'$MR_A = MC_A$'),
                      work_line(r'$120 - 2q_A - q_B = 2q_A$'),
                      work_line(r'$120 - q_B = 4q_A$'),
                      work_line(r'$BR_A$: $q_A = 30 - \tfrac{1}{4}q_B$', ROW_PLAYER)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        note = teaching("Firm A's marginal revenue depends on how much firm B sells.")
        self.play(FadeIn(head), FadeIn(context), FadeIn(br_ax), FadeIn(br_words), *focus(1),
                  FadeIn(work[0]), FadeIn(work[1]), FadeIn(note))
        self.play(FadeIn(work[2]))
        self.play(FadeIn(work[3]), FadeIn(br_a), FadeIn(br_a_word))
        self.pause('4.a')

        # ---- 4.b.symmetry · Firm B's best response by symmetry, as the sheet does it.
        br_b = Line(br_ax.c2p(0, 30), br_ax.c2p(120, 0), color=COL_PLAYER, stroke_width=3)
        br_b_word = Tex('$BR_B$', color=INK).scale(WORD_SCALE).next_to(br_ax.c2p(120, 0), UR, buff=0.12)
        br_b_line = work_line(r'$BR_B$: $q_B = 30 - \tfrac{1}{4}q_A$', COL_PLAYER)
        br_b_line.next_to(work, DOWN, buff=WORK_GAP, aligned_edge=LEFT)
        symmetry_word = Tex(narration('symmetry'), color=CAPTION).scale(0.5).next_to(br_b_line, RIGHT, buff=0.25)
        self.remove(note)
        note = teaching("Firm B's problem is the same, with A and B swapped.")
        self.play(FadeIn(br_b_line), FadeIn(symmetry_word), FadeIn(br_b), FadeIn(br_b_word), FadeIn(note))
        self.pause('4.b.symmetry')

        # ---- 4.b · The crossing: Nash equilibrium at 24 each, the sheet's boxed result on this market.
        nash_dot = Dot(br_ax.c2p(24, 24), radius=0.07, color=NASH).set_z_index(DOT_LAYER)
        nash_guides = VGroup(DashedLine(br_ax.c2p(24, 24), br_ax.c2p(24, 0), color=GUIDE, stroke_width=2),
                             DashedLine(br_ax.c2p(24, 24), br_ax.c2p(0, 24), color=GUIDE, stroke_width=2)).set_z_index(GUIDE_LAYER)
        nash_readouts = VGroup(
            Tex('24', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(br_ax.c2p(24, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(br_ax.c2p(24, 0) + DOWN * QUANTITY_LABEL_OFFSET),
            Tex(r'$q_B^* = 24$', color=GUIDE).scale(PRICE_SCALE).next_to(br_ax.c2p(0, 24), LEFT, buff=0.2))
        nash_word = Tex('Nash Equilibrium', color=NASH).scale(0.6).next_to(br_ax.c2p(24, 24), UR, buff=0.15)
        self.remove(work, br_b_line, symmetry_word)
        work = VGroup(work_line(r'$q_A^* = 30 - \tfrac{1}{4}q_A^*$'),
                      work_line(r'$\tfrac{5}{4}q_A^* = 30$'),
                      work_line(r'$q_A^* = q_B^* = 24$', GUIDE),
                      work_line(r'$Q = 48$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching('Neither firm can do better by changing its output alone.')
        self.play(FadeIn(nash_dot), FadeIn(nash_word), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(Create(nash_guides[0]), Create(nash_guides[1]), FadeIn(nash_readouts), FadeIn(work[2]), FadeIn(work_box))
        self.play(FadeIn(work[3]))
        self.pause('4.b')

        # ---- 4.c · Back on the market graph: Q = 48 up to demand, P* = 72, beside the monopoly in grey.
        duopoly_picture = [br_ax, br_words, br_a, br_a_word, br_b, br_b_word, nash_dot, nash_guides, nash_readouts, nash_word]
        monopoly_reference = VGroup(
            DashedLine(ax.c2p(30, 0), ax.c2p(30, 90), color=MUTED, stroke_width=2),
            DashedLine(ax.c2p(30, 90), ax.c2p(0, 90), color=MUTED, stroke_width=2),
            Dot(ax.c2p(30, 90), radius=0.065, color=MUTED),
            Tex('90', color=CAPTION).scale(PRICE_SCALE).next_to(ax.c2p(0, 90), LEFT, buff=0.2),
            Tex('30', color=CAPTION).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(30, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q^*$', color=CAPTION).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(30, 0) + DOWN * QUANTITY_LABEL_OFFSET)).set_z_index(1.5)
        duopoly_guide = DashedLine(ax.c2p(48, 0), ax.c2p(48, 72), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        duopoly_dot = Dot(ax.c2p(48, 72), radius=0.07, color=DEMAND).set_z_index(DOT_LAYER)
        duopoly_price = VGroup(
            DashedLine(ax.c2p(48, 72), ax.c2p(0, 72), color=DEMAND, stroke_width=2),
            Tex(r'$P^* = 72$', color=DEMAND).scale(PRICE_SCALE).next_to(ax.c2p(0, 72), LEFT, buff=0.2)).set_z_index(GUIDE_LAYER)
        duopoly_quantity = VGroup(
            Tex('48', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(48, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$Q$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(48, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(work, work_box, note)
        self.play(*[FadeOut(m) for m in duopoly_picture], run_time=0.6)
        work = VGroup(work_line(r'$P = 120 - (24 + 24)$'),
                      work_line(r'$P = 120 - 48$'),
                      work_line(r'$P^* = 72$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        note = teaching('Two sellers: more output, lower price.')
        self.play(FadeIn(ax), FadeIn(axis_words), FadeIn(demand_line), FadeIn(demand_word), FadeIn(demand_intercept),
                  FadeIn(monopoly_reference), FadeIn(duopoly_quantity), *focus(2), FadeIn(work[0]))
        self.play(Create(duopoly_guide), FadeIn(duopoly_dot), FadeIn(work[1]))
        self.play(Create(duopoly_price[0]), FadeIn(duopoly_price[1]), FadeIn(work[2]), FadeIn(work_box), FadeIn(note))
        self.pause('4.c')

        # ---- 5.a · Competitive: E2's firm graph left and the market graph right, on one price scale. The market is
        # the same demand line read in thousands of units: many sellers need a market many times the size.
        market_picture = [ax, axis_words, demand_line, demand_word, demand_intercept, monopoly_reference,
                          duopoly_guide, duopoly_dot, duopoly_price, duopoly_quantity]
        self.remove(head, context, note, work, work_box)
        self.play(*[FadeOut(m) for m in market_picture], *focus(), run_time=0.6)
        head = title('Perfect Competition')
        context = subtitle(head, 'Many sellers.')
        FIRM_END, SUPPLY_TOP = 70, 130
        START_P, LONG_RUN_P = 100, 2 * np.sqrt(FC)     # E2's opening price; its long-run price, 63.25 (lowest ATC)
        # Readouts here are whole numbers, as in E2 (the long run is 63.25, 31.6 units and 56.75 thousand).
        # One tracker, the market price, drives every mark of this section: supply pivots through the origin
        # (entry), the firm takes the price, and its quantity, ATC and profit follow.
        price = ValueTracker(START_P)
        p_now = lambda: price.get_value()
        big_q = lambda: TOP_PRICE - p_now()            # the market's quantity, in thousands
        firm_q_now = lambda: p_now() / 2               # the firm's MC = MR
        firm_ax = style_axes([0, FIRM_END, 10], [0, Y_TOP, 20], x_length=2.6, y_length=4.6)
        firm_ax.shift(np.array([FIRM_X, MARKET_Y, 0]) - firm_ax.c2p(0, 0))
        small_ax = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=3.8, y_length=4.6)
        small_ax.shift(np.array([SMALL_MARKET_X, MARKET_Y, 0]) - small_ax.c2p(0, 0))
        graph_words = VGroup()
        for graph, x_max, name, x_name, unit_name in [(firm_ax, FIRM_END, 'Firm', 'q', 'units'),
                                                      (small_ax, X_END, 'Market', 'Q', 'thousands')]:
            graph_words.add(
                Tex('P', color=INK).scale(0.8).next_to(graph.c2p(0, Y_TOP), LEFT, buff=0.23),
                Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(graph.c2p(0, Y_TOP), RIGHT, buff=0.22),
                Tex(x_name, color=INK).scale(0.8).next_to(graph.c2p(x_max, 0), DOWN, buff=0.23),
                Tex(r'\textsf{' + unit_name + '}', color=CAPTION).scale(0.55).next_to(graph.c2p(x_max, 0), DOWN, buff=0.73),
                Tex(narration(name), color=CAPTION).scale(0.6).move_to(graph.c2p(x_max, Y_TOP), aligned_edge=RIGHT))
        firm_mc = Line(firm_ax.c2p(0, 0), firm_ax.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=3)
        firm_atc = polyline([firm_ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, FIRM_END, 200)], ATC_COLOR, 3)
        firm_words = VGroup(
            Tex('MC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15),
            Tex('ATC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(FIRM_END, atc(FIRM_END)), RIGHT, buff=0.15))
        small_demand = Line(small_ax.c2p(0, TOP_PRICE), small_ax.c2p(TOP_PRICE, 0), color=DEMAND, stroke_width=3)
        supply_end = lambda: small_ax.c2p(SUPPLY_TOP * big_q() / p_now(), SUPPLY_TOP)
        small_supply = Line(small_ax.c2p(0, 0), supply_end(), color=MC_COLOR, stroke_width=3)
        small_supply.add_updater(lambda m: m.put_start_and_end_on(small_ax.c2p(0, 0), supply_end()))
        supply_word = Tex('S', color=INK).scale(WORD_SCALE)
        supply_word.add_updater(lambda m: m.next_to(supply_end(), RIGHT, buff=0.15))
        supply_word.update()
        small_words = VGroup(Tex('D', color=INK).scale(WORD_SCALE).next_to(small_ax.c2p(TOP_PRICE, 0), UR, buff=0.12), supply_word)
        note = teaching('Competitive firms are what we call price takers.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(firm_ax), FadeIn(small_ax), FadeIn(graph_words),
                  FadeIn(firm_mc), FadeIn(firm_atc), FadeIn(firm_words), FadeIn(small_demand), FadeIn(small_supply),
                  FadeIn(small_words), FadeIn(note))
        self.pause('5.a')

        # ---- 5.b · Step 0: supply meets demand at Q* = 20 thousand, P* = 100; the price carries across as the firm's MR.
        guide_line = lambda start, end, color=GUIDE: DashedLine(start, end, color=color, stroke_width=2).set_z_index(GUIDE_LAYER)
        market_dot = Dot(small_ax.c2p(big_q(), p_now()), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        market_dot.add_updater(lambda m: m.move_to(small_ax.c2p(big_q(), p_now())))
        market_drop = guide_line(small_ax.c2p(big_q(), p_now()), small_ax.c2p(big_q(), 0))
        market_drop.add_updater(lambda m: m.become(guide_line(small_ax.c2p(big_q(), p_now()), small_ax.c2p(big_q(), 0))))
        market_across = guide_line(small_ax.c2p(big_q(), p_now()), small_ax.c2p(0, p_now()))
        market_across.add_updater(lambda m: m.become(guide_line(small_ax.c2p(big_q(), p_now()), small_ax.c2p(0, p_now()))))
        market_marks = VGroup(market_drop, market_across)
        market_number = DecimalNumber(big_q(), num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        market_number.add_updater(lambda m: m.set_value(round(big_q()))
                                  .move_to(small_ax.c2p(big_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        market_symbol = Tex('$Q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        market_symbol.add_updater(lambda m: m.move_to(small_ax.c2p(big_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))

        def price_readout(graph, color):
            readout = VGroup(Tex('$P^* =$', color=color), DecimalNumber(START_P, num_decimal_places=0, color=color)).scale(PRICE_SCALE)
            readout.add_updater(lambda m: (m[1].set_value(round(p_now())), m.arrange(RIGHT, buff=0.12),
                                           m.next_to(graph.c2p(0, p_now()), LEFT, buff=0.2)))
            return readout
        market_price = price_readout(small_ax, GUIDE)
        market_readouts = VGroup(market_number, market_symbol, market_price)
        firm_mr = Line(firm_ax.c2p(FIRM_END, START_P), firm_ax.c2p(0, START_P), color=DEMAND, stroke_width=3)
        firm_mr.add_updater(lambda m: m.put_start_and_end_on(firm_ax.c2p(FIRM_END, p_now()), firm_ax.c2p(0, p_now())))
        firm_mr_word = Tex('MR', color=INK).scale(WORD_SCALE)
        firm_mr_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_END, p_now()), RIGHT, buff=0.15))
        for m in (market_number, market_symbol, market_price, firm_mr_word):
            m.update()
        work = VGroup(work_line(r'$120 - Q = 5Q$'),
                      work_line(r'$120 = 6Q$'),
                      work_line(r'$Q^* = 20$', GUIDE),
                      work_line(r'$P^* = 5\cdot 20 = 100 = MR$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = VGroup(SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2),
                          SurroundingRectangle(work[3], color=GUIDE, buff=0.08, stroke_width=2))
        supply_row = Tex(r'$S$: $P = 5Q$', color=MC_COLOR).scale(0.6).next_to(small_ax.c2p(40, 122), RIGHT, buff=0)
        self.remove(note)
        note = teaching('Step 0: supply and demand set the market price.')
        self.play(FadeIn(supply_row), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]), FadeIn(work_box[0]), FadeIn(market_dot), Create(market_drop), FadeIn(market_number), FadeIn(market_symbol))
        self.play(FadeIn(work[3]), FadeIn(work_box[1]), Create(market_across), FadeIn(market_price))
        self.play(Create(firm_mr), FadeIn(firm_mr_word))
        self.pause('5.b')

        # ---- 5.c · Step 1: MC = MR at q* = 50 on the firm graph.
        firm_dot = Dot(firm_ax.c2p(firm_q_now(), p_now()), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        firm_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(firm_q_now(), p_now())))
        firm_guide = guide_line(firm_ax.c2p(firm_q_now(), p_now()), firm_ax.c2p(firm_q_now(), 0))
        firm_guide.add_updater(lambda m: m.become(guide_line(firm_ax.c2p(firm_q_now(), p_now()), firm_ax.c2p(firm_q_now(), 0))))
        firm_number = DecimalNumber(firm_q_now(), num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        firm_number.add_updater(lambda m: m.set_value(round(firm_q_now()))
                                .move_to(firm_ax.c2p(firm_q_now(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        firm_symbol = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        firm_symbol.add_updater(lambda m: m.move_to(firm_ax.c2p(firm_q_now(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        firm_quantity = VGroup(firm_number, firm_symbol)
        for m in (firm_number, firm_symbol):
            m.update()
        self.remove(work, work_box)
        work = VGroup(work_line(r'$2q = 100$'),
                      work_line(r'$q^* = 50$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Every unit up to $q^*$ adds more to revenue than to cost.')
        self.play(*focus(1), FadeIn(work[0]), FadeIn(firm_dot), FadeIn(note))
        self.play(Create(firm_guide), FadeIn(firm_number), FadeIn(firm_symbol), FadeIn(work[1]), FadeIn(work_box))
        self.pause('5.c')

        # ---- 5.d · Step 2: the firm takes the market price, P* = 100.
        firm_price = price_readout(firm_ax, DEMAND)
        firm_price.update()
        self.remove(work, work_box)
        work = VGroup(work_line(r'$P^* = 100$', GUIDE))
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[0], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching('A price taker sells every unit at the market price.')
        self.play(*focus(2), FadeIn(firm_price), FadeIn(work), FadeIn(work_box), FadeIn(note))
        self.pause('5.d')

        # ---- 5.e · Step 3: ATC* = 70, where q* meets ATC. Its readout fades as the price comes down to it (5.g).
        cost_now = lambda: atc(firm_q_now())
        cost_gap = lambda: np.clip((p_now() - cost_now()) / 8, 0, 1)
        atc_floor = Dot(firm_ax.c2p(firm_q_now(), cost_now()), radius=0.07, color=ATC_COLOR).set_z_index(DOT_LAYER - 1)
        atc_floor.add_updater(lambda m: m.move_to(firm_ax.c2p(firm_q_now(), cost_now())))
        firm_cost_guide = guide_line(firm_ax.c2p(firm_q_now(), cost_now()), firm_ax.c2p(0, cost_now()), ATC_COLOR)
        firm_cost_guide.add_updater(lambda m: m.become(guide_line(firm_ax.c2p(firm_q_now(), cost_now()),
                                                                  firm_ax.c2p(0, cost_now()), ATC_COLOR)))
        firm_cost_number = DecimalNumber(cost_now(), num_decimal_places=0, color=ATC_COLOR).scale(PRICE_SCALE)
        firm_cost_number.add_updater(lambda m: m.set_value(round(cost_now()))
                                     .next_to(firm_ax.c2p(0, cost_now()), LEFT, buff=0.2).set_opacity(cost_gap()))
        firm_cost_number.update()
        self.remove(work, work_box)
        work = VGroup(work_line(r'$ATC^* = 50 + 1000/50$'),
                      work_line(r'$ATC^* = 70$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Average total cost: the cost per unit of making $q^*$ units.')
        self.play(*focus(3), FadeIn(atc_floor), FadeIn(work[0]), FadeIn(note))
        self.play(Create(firm_cost_guide), FadeIn(firm_cost_number), FadeIn(work[1]), FadeIn(work_box))
        self.pause('5.e')

        # ---- 5.f · Step 4: profit, (100 - 70) x 50 = 1,500, as one-unit strips between ATC* and P* on the firm graph.
        firm_profit = VGroup(*[Polygon(firm_ax.c2p(k, 0), firm_ax.c2p(k + 0.5, 0), firm_ax.c2p(k + 0.5, 1), firm_ax.c2p(k, 1),
                                       stroke_width=0, fill_color=SUPPLY, fill_opacity=0).set_z_index(FILL_LAYER)
                               for k in range(60)]).set_z_index(FILL_LAYER)

        def follow_profit(strips):
            for k, strip in enumerate(strips):
                left, right = k + BAR_GAP / 2, min(k + 1 - BAR_GAP / 2, firm_q_now())
                if right - left < 1e-3 or p_now() - cost_now() < 1e-3:
                    strip.set_fill(opacity=0)
                    continue
                strip.set_points_as_corners([firm_ax.c2p(left, cost_now()), firm_ax.c2p(right, cost_now()),
                                             firm_ax.c2p(right, p_now()), firm_ax.c2p(left, p_now()), firm_ax.c2p(left, cost_now())])
                strip.set_fill(opacity=PROFIT_OPACITY)
        firm_profit.add_updater(follow_profit)
        firm_profit.update()
        firm_profit_word = Tex('Profit', color=INK).scale(0.6).set_z_index(WORD_LAYER)
        firm_profit_word.add_updater(lambda m: m.move_to(firm_ax.c2p(firm_q_now() / 2, (p_now() + cost_now()) / 2))
                                     .set_opacity(np.clip((p_now() - cost_now() - 8) / 8, 0, 1)))
        firm_profit_word.update()
        self.remove(work, work_box)
        work = VGroup(work_line(r'$\pi^* = (100 - 70)\cdot 50$'),
                      work_line(r'$\pi^* = 1{,}500$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Profit: the price minus the cost per unit, on each of the $q^*$ units.')
        self.play(*focus(4), FadeIn(work[0]), FadeIn(note))
        self.play(LaggedStart(*[FadeIn(strip) for strip in firm_profit[:50]], lag_ratio=0.1), run_time=1.6)
        self.remove(*firm_profit)
        self.add(firm_profit)
        self.play(FadeIn(firm_profit_word), FadeIn(work[1]), FadeIn(work_box))
        self.pause('5.f')

        # ---- 5.g · Step 5: profit brings entry. Supply pivots out, the price falls to the bottom of ATC (63.25, shown
        # rounded as E2 does), and profit closes to zero: the long run.
        self.remove(work, work_box)
        self.remove(note)
        note = teaching('With profit, more firms enter and the price falls.')
        self.play(*focus(5), FadeOut(supply_row), FadeIn(note))
        self.play(price.animate.set_value(LONG_RUN_P), run_time=3.2, rate_func=smooth)
        work = VGroup(work_line(r'Long run: $P^* = ATC^*$'),
                      work_line(r'$\pi^* = 0$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'$\pi = 0$. Long run equilibrium: no entry or exit.')
        self.play(FadeIn(work), FadeIn(work_box), FadeIn(note))
        self.pause('5.g')

        # ---- 6.a · More sellers: each seller's MR is the price less its own output, so P - MC = q. (The sweep ignores
        # the fixed cost: on this market sellers beyond the second would lose money. See E5_Notes.md.)
        competitive_picture = [firm_ax, small_ax, graph_words, firm_mc, firm_atc, firm_words, small_demand, small_supply,
                               small_words, market_dot, market_marks, market_readouts, firm_mr, firm_mr_word, firm_dot,
                               firm_guide, firm_quantity, firm_price, atc_floor, firm_cost_guide, firm_cost_number,
                               firm_profit, firm_profit_word, problem, card_head]
        for m in competitive_picture[7:23]:
            m.update()
            m.clear_updaters()               # Digits current, then the section's marks freeze before they fade.
        self.remove(head, context, note, work, work_box)
        self.play(*[FadeOut(m) for m in competitive_picture], run_time=0.8)
        head = title('More Sellers')
        context = subtitle(head, r'$n$ similar sellers.')
        sellers = ValueTracker(1)
        outcome_q = lambda: market_q(sellers.get_value())
        outcome_p = lambda: d(outcome_q())
        outcome_mc = lambda: mc(firm_q(sellers.get_value()))
        outcome_dot = Dot(ax.c2p(30, 90), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        outcome_dot.add_updater(lambda m: m.move_to(ax.c2p(outcome_q(), outcome_p())))
        cost_dot = Dot(ax.c2p(30, 60), radius=0.065, color=MC_COLOR).set_z_index(DOT_LAYER)
        cost_dot.add_updater(lambda m: m.move_to(ax.c2p(outcome_q(), outcome_mc())))
        outcome_drop = DashedLine(ax.c2p(30, 0), ax.c2p(30, 90), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        # Rebuilt each frame (B5's idiom) so the dashes keep their length as the guides grow and shrink.
        outcome_drop.add_updater(lambda m: m.become(DashedLine(ax.c2p(outcome_q(), 0), ax.c2p(outcome_q(), outcome_p()),
                                                               color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)))
        outcome_across = DashedLine(ax.c2p(0, 90), ax.c2p(30, 90), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        outcome_across.add_updater(lambda m: m.become(DashedLine(ax.c2p(0, outcome_p()), ax.c2p(outcome_q(), outcome_p()),
                                                                 color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)))
        outcome_price = VGroup(Tex('$P=$', color=GUIDE), DecimalNumber(90, num_decimal_places=0, color=GUIDE))
        outcome_price.scale(PRICE_SCALE).arrange(RIGHT, buff=0.14)
        outcome_price.add_updater(lambda m: (m[1].set_value(round(outcome_p(), 4)), m.arrange(RIGHT, buff=0.14),
                                             m.next_to(ax.c2p(0, outcome_p()), LEFT, buff=0.2)))
        outcome_quantity = DecimalNumber(30, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        outcome_quantity.add_updater(lambda m: m.set_value(round(outcome_q(), 4))
                                     .move_to(ax.c2p(outcome_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        outcome_symbol = Tex('$Q$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        outcome_symbol.add_updater(lambda m: m.move_to(ax.c2p(outcome_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        # The gap between price and marginal cost: a bracket just left of the drop, named at its foot.
        markup_bracket = VGroup(*[Line(LEFT, RIGHT, color=INK, stroke_width=2) for _ in range(3)])
        markup_bracket.add_updater(lambda m: (
            m[0].put_start_and_end_on(ax.c2p(outcome_q(), outcome_mc()) + LEFT * 0.16,
                                      ax.c2p(outcome_q(), outcome_p()) + LEFT * 0.16),
            m[1].put_start_and_end_on(ax.c2p(outcome_q(), outcome_mc()) + LEFT * 0.16,
                                      ax.c2p(outcome_q(), outcome_mc()) + LEFT * 0.09),
            m[2].put_start_and_end_on(ax.c2p(outcome_q(), outcome_p()) + LEFT * 0.16,
                                      ax.c2p(outcome_q(), outcome_p()) + LEFT * 0.09)))
        markup_word = Tex('$P - MC$', color=INK).scale(0.55)
        markup_word.add_updater(lambda m: m.next_to(ax.c2p(outcome_q(), outcome_mc()) + LEFT * 0.16, LEFT, buff=0.1))
        seller_count = VGroup(Tex('$n =$', color=INK), DecimalNumber(1, num_decimal_places=0, color=INK))
        seller_count.scale(0.8).arrange(RIGHT, buff=0.18)
        seller_count.add_updater(lambda m: (m[1].set_value(round(sellers.get_value(), 4)), m.arrange(RIGHT, buff=0.18),
                                            m.move_to(ax.c2p(98, 118))))
        rolling = [outcome_dot, cost_dot, outcome_drop, outcome_across, outcome_price, outcome_quantity, outcome_symbol,
                   markup_bracket, markup_word, seller_count]
        for m in rolling:
            m.update()                       # Digits must already match before a number fades in.
        # The reason, from the sheet's MR: the duopolist's MR rewritten with the price.
        mr_lines = VGroup(work_line(r'$MR_A = 120 - 2q_A - q_B$', MR_COLOR),
                          work_line(r'$= P - q_A$', MR_COLOR),
                          work_line(r'$MR = MC$, so $P - MC = q$')).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        mr_lines[1].shift(RIGHT * (work_line('$MR_A$').width + 0.12))
        mr_lines.move_to([PANEL_LEFT, PANEL_TOP, 0], aligned_edge=UL)
        # The table grows one row per stop of n.
        TABLE_X = (3.5, 4.3, 5.15, 6.05, 7.05)
        TABLE_TOP, ROW_STEP = mr_lines.get_bottom()[1] - 0.55, 0.46
        table_head = VGroup(*[Tex(text, color=CAPTION).scale(0.62).move_to([x, TABLE_TOP, 0])
                              for text, x in zip(('$n$', '$q$', '$Q$', '$P$', '$P - MC$'), TABLE_X)])
        table_rule = Line([PANEL_LEFT, TABLE_TOP - 0.25, 0], [PANEL_LEFT + PANEL_WIDTH, TABLE_TOP - 0.25, 0],
                          color=MUTED, stroke_width=1.5)
        rows = VGroup()
        for k, values in enumerate([(1, 30, 30, 90, 30), (2, 24, 48, 72, 24), (3, 20, 60, 60, 20),
                                    (7, 12, 84, 36, 12), (17, 6, 102, 18, 6)]):
            rows.add(VGroup(*[Tex(str(v), color=INK).scale(0.62).move_to([x, TABLE_TOP - 0.25 - ROW_STEP * (k + 0.6), 0])
                              for v, x in zip(values, TABLE_X)]))
        self.remove(*rolling)
        note = teaching(r"Each seller's MR is the price minus its own output.")
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(demand_line),
                  FadeIn(demand_word), FadeIn(demand_intercept), FadeIn(mr_lines), FadeIn(note))
        self.play(*[FadeIn(m) for m in rolling], FadeIn(table_head), FadeIn(table_rule), FadeIn(rows[0]))
        self.pause('6.a')

        # ---- 6.b.two · n rolls from 1 to 2: the duopoly.
        self.play(sellers.animate.set_value(2), run_time=2.2, rate_func=smooth)
        self.play(FadeIn(rows[1]), run_time=0.5)
        self.pause('6.b.two')

        # ---- 6.b.three · n = 3.
        self.play(sellers.animate.set_value(3), run_time=2.2, rate_func=smooth)
        self.play(FadeIn(rows[2]), run_time=0.5)
        self.pause('6.b.three')

        # ---- 6.b.seven · n = 7. (Named 6.b.six until 2026-11-12, for the sheet's market, where this stop was n = 6.)
        self.play(sellers.animate.set_value(7), run_time=2.6, rate_func=smooth)
        self.play(FadeIn(rows[3]), run_time=0.5)
        self.pause('6.b.seven')

        # ---- 6.b · n = 17: more output, a lower price, a price closer to marginal cost.
        self.play(sellers.animate.set_value(17), run_time=3.0, rate_func=smooth)
        self.remove(note)
        note = teaching('More sellers: more output, a lower price, a price closer to marginal cost.')
        self.play(FadeIn(rows[4]), FadeIn(note), run_time=0.5)
        self.pause('6.b')

        # ---- 6.c · The limit: each seller is too small to move the price, so MR comes to the price.
        limit_line = work_line(r'Many sellers: $MR \approx P$', MR_COLOR)
        limit_line.move_to([PANEL_LEFT, rows[4].get_bottom()[1] - 0.45, 0], aligned_edge=UL)
        self.remove(note)
        note = teaching('A firm changing its quantity has no real effect on the price.')
        self.play(FadeIn(limit_line), FadeIn(note))
        self.pause('6.c')

        # ---- 7.a · The three structures on one market, the card back in white, and Part E's line.
        for m in rolling:
            m.update()
            m.clear_updaters()
        self.remove(head, context, note)
        self.play(*[FadeOut(m) for m in rolling], FadeOut(mr_lines), FadeOut(table_head), FadeOut(table_rule),
                  FadeOut(rows), FadeOut(limit_line), run_time=0.6)
        head = title('Three Market Structures')
        context = subtitle(head, 'One demand curve, three outcomes.')
        # Monopoly and duopoly sit where they were solved. The competitive long run is a price, 63.25 (shown as 63):
        # its market is this demand line read in thousands, so its point is marked on the line without a quantity.
        outcomes = VGroup()
        for q_out, p_out, name, q_text, name_gap in [(30, 90, 'Monopoly', '30', 0.12), (48, 72, 'Duopoly', '48', 0.12),
                                                     (TOP_PRICE - LONG_RUN_P, LONG_RUN_P, 'Competitive', '', 0.9)]:
            outcome = VGroup(
                DashedLine(ax.c2p(q_out, p_out), ax.c2p(0, p_out), color=GUIDE, stroke_width=2),
                Dot(ax.c2p(q_out, p_out), radius=0.07, color=GUIDE),
                Tex(str(round(p_out)), color=GUIDE).scale(PRICE_SCALE).next_to(ax.c2p(0, p_out), LEFT, buff=0.2),
                Tex(name, color=INK).scale(0.6).next_to(ax.c2p(q_out, p_out), UR if q_text else RIGHT, buff=name_gap))
            if q_text:
                outcome.add(DashedLine(ax.c2p(q_out, 0), ax.c2p(q_out, p_out), color=GUIDE, stroke_width=2),
                            Tex(q_text, color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(q_out, 0) + DOWN * QUANTITY_NUMBER_OFFSET))
            outcomes.add(outcome.set_z_index(GUIDE_LAYER))
        problem.set_color(INK).set_opacity(1)
        card_head.set_opacity(1)
        note = teaching('Market power leads to inefficient markets.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(problem), FadeIn(card_head))
        self.play(LaggedStart(*[FadeIn(outcome) for outcome in outcomes], lag_ratio=0.5), FadeIn(note), run_time=2.2)
        self.pause('7.a')
