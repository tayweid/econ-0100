# maniml E5_Animation.py EpisodeE5
# Storyboard: E5_Notes.md. All lesson choreography stays in construct().
# The Part E wrap-up: Taylor's sheet "Example: Three Market Structures" (E4_Duopoly/04_Handwritten.pdf)
# solved with the firm's five steps for one seller, two and many, then the same market with n sellers.
# One market: D: P = 200 - Q/2; every firm MC = 20 + q; FC = 450 (inferred, not on the sheet), ATC = 450/q + 20 + q/2.
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
        ATC_FROM = 6                               # ATC starts at q = 6 (ATC 98), clear of the price axis.
        # Top-level z order (the engine sorts top-level mobjects by z_index).
        FILL_LAYER, WORD_LAYER, GUIDE_LAYER, DOT_LAYER = -1, 6, 10, 30

        # The model, as one-line functions (Q market output, q one firm's output).
        FC = 450
        d = lambda Q: 200 - Q / 2
        mr = lambda q: 200 - q
        mc = lambda q: 20 + q
        atc = lambda q: FC / q + 20 + q / 2
        supply = lambda Q: 20 + Q / 10
        # n similar sellers, each choosing q with MR_i = P - q/2 = MC = 20 + q.
        firm_q = lambda n: 360 / (n + 3)
        market_q = lambda n: n * firm_q(n)
        # Part E's firm palette (shared_E.md).
        MC_COLOR, ATC_COLOR, MR_COLOR = SUPPLY, TOTAL, PINK

        teaching = lambda text: (Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                 .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # One line of a side solve. Results are red and boxed, as on the sheet.
        work_line = lambda text, color=INK: Tex(text, color=color).scale(WORK_SCALE)

        # ---- 0.a · The shared bumper. Thesis line left for Taylor (E5 has no notes header; C4's precedent).
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 5)
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode))
        self.clear()

        # ---- 1.a · The sheet's header: one market, and every firm has the same marginal cost.
        head = title('Three Market Structures')
        context = subtitle(head, 'All firms are similar.')
        header = VGroup(Tex(r'$D$: $P = 200 - \tfrac{1}{2}Q$', color=DEMAND),
                        Tex(r'$MC = 20 + q$', color=MC_COLOR)).scale(0.95)
        header.arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, 1.0, 0])
        self.play(FadeIn(head), FadeIn(context), FadeIn(header))
        self.pause('1.a')

        # ---- 1.b · The sheet's three columns: monopoly, duopoly, competitive, with their MR or supply.
        column_x = (-4.9, 0, 4.9)
        heads = VGroup(*[Tex(word, color=INK).scale(0.85).move_to([x, -0.65, 0])
                         for word, x in zip(('Monopoly', 'Duopoly', 'Competitive'), column_x)])
        arrows = VGroup(*[Arrow(heads[k].get_right(), heads[k + 1].get_left(), buff=0.4, color=MUTED, thickness=2)
                          for k in range(2)])
        columns = VGroup(
            VGroup(Tex(r'$MR_A = 200 - q_A$', color=MR_COLOR), Tex(r'$Q = q_A$', color=INK)),
            VGroup(Tex(r'$MR_A = 200 - q_A - \tfrac{1}{2}q_B$', color=ROW_PLAYER),
                   Tex(r'$MR_B = 200 - q_B - \tfrac{1}{2}q_A$', color=COL_PLAYER)),
            VGroup(Tex(r'$S$: $P = 20 + \tfrac{1}{10}Q$', color=MC_COLOR)))
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

        # The market graph: the sheet's axes, P to 200 and Q to 400, with room above 200 for P.
        ax = style_axes([0, 400, 100], [0, 220, 50], x_length=7.4, y_length=4.6)
        ax.shift(np.array([MARKET_X, MARKET_Y, 0]) - ax.c2p(0, 0))
        axis_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 220), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 220), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(400, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(400, 0), DOWN, buff=0.73))
        demand_line = Line(ax.c2p(0, 200), ax.c2p(400, 0), color=DEMAND, stroke_width=3)
        demand_word = Tex('D', color=INK).scale(WORD_SCALE).next_to(ax.c2p(400, 0), UR, buff=0.12)
        demand_intercept = Tex('$200$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, 200), LEFT, buff=0.15)

        # ---- 3.a · Monopoly: the sheet's four curves on the market graph; the card moves beside it.
        mr_line = Line(ax.c2p(0, 200), ax.c2p(200, 0), color=MR_COLOR, stroke_width=3)
        mc_line = Line(ax.c2p(0, 20), ax.c2p(180, 200), color=MC_COLOR, stroke_width=3)
        atc_curve = polyline([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, 260, 240)], ATC_COLOR, 3)
        monopoly_words = VGroup(
            Tex('MR', color=INK).scale(WORD_SCALE).next_to(ax.c2p(200, 0), UR, buff=0.12),
            Tex('MC', color=INK).scale(WORD_SCALE).next_to(ax.c2p(180, 200), RIGHT, buff=0.15),
            Tex('ATC', color=INK).scale(WORD_SCALE).next_to(ax.c2p(260, atc(260)), RIGHT, buff=0.15))
        cost_intercept = Tex('$20$', color=MC_COLOR).scale(0.65).next_to(ax.c2p(0, 20), LEFT, buff=0.15)
        self.remove(head, note)
        head = title('Monopoly')
        context = subtitle(head, r'One seller: $Q = q_A$.')
        note = teaching("The monopolist faces the market's downward-sloping demand.")
        self.play(FadeIn(head), FadeIn(context), Transform(problem, side_problem), FadeIn(card_head), FadeIn(divider),
                  FadeIn(ax), FadeIn(axis_words), FadeIn(demand_line), FadeIn(demand_word), FadeIn(demand_intercept),
                  FadeIn(mr_line), FadeIn(mc_line), FadeIn(atc_curve), FadeIn(monopoly_words), FadeIn(cost_intercept),
                  FadeIn(note), run_time=1.6)
        self.pause('3.a')

        # ---- 3.b · Step 1: MR = MC at q* = 90, the sheet's side solve; the dot traces down to q*.
        work = VGroup(work_line(r'$20 + q = 200 - q$'), work_line(r'$2q = 180$'),
                      work_line(r'$q^* = 90$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        choice_dot = Dot(ax.c2p(90, 110), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        quantity_guide = DashedLine(ax.c2p(90, 110), ax.c2p(90, 0), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        quantity_word = VGroup(
            Tex('90', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(90, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(90, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(note)
        note = teaching(r'Every unit up to $q^*$ adds more to revenue than to cost.')
        self.play(*focus(1), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]), FadeIn(work_box), FadeIn(choice_dot))
        self.play(Create(quantity_guide), FadeIn(quantity_word))
        self.pause('3.b')

        # ---- 3.c · Step 2: up from q* to demand, P* = 155; each readout dashed in its own curve's color.
        up_guide = DashedLine(ax.c2p(90, 110), ax.c2p(90, 155), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        price_dot = Dot(ax.c2p(90, 155), radius=0.07, color=DEMAND).set_z_index(DOT_LAYER)
        price_guide = DashedLine(ax.c2p(90, 155), ax.c2p(0, 155), color=DEMAND, stroke_width=2).set_z_index(GUIDE_LAYER)
        price_word = Tex(r'$P^* = 155$', color=DEMAND).scale(PRICE_SCALE).next_to(ax.c2p(0, 155), LEFT, buff=0.2)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$P = 200 - \tfrac{1}{2}\cdot 90$'),
                      work_line(r'$P^* = 155$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'The price is what buyers will pay for $q^*$ units.')
        self.play(*focus(2), FadeIn(work[0]), FadeIn(note))
        self.play(Create(up_guide), FadeIn(price_dot))
        self.play(Create(price_guide), FadeIn(price_word), FadeIn(work[1]), FadeIn(work_box))
        self.pause('3.c')

        # ---- 3.d · Step 3: ATC* = 70, read from the graph where q* meets ATC.
        atc_dot = Dot(ax.c2p(90, 70), radius=0.07, color=ATC_COLOR).set_z_index(DOT_LAYER)
        atc_guide = DashedLine(ax.c2p(90, 70), ax.c2p(0, 70), color=ATC_COLOR, stroke_width=2).set_z_index(GUIDE_LAYER)
        atc_word = Tex(r'$ATC^* = 70$', color=ATC_COLOR).scale(PRICE_SCALE).next_to(ax.c2p(0, 70), LEFT, buff=0.2)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$ATC^* = 70$', GUIDE))
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[0], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Average total cost: the cost per unit of making $q^*$ units.')
        self.play(*focus(3), FadeIn(atc_dot), FadeIn(note))
        self.play(Create(atc_guide), FadeIn(atc_word), FadeIn(work), FadeIn(work_box))
        self.pause('3.d')

        # ---- 3.e · Step 4: profit, (155 - 70) x 90 = 7,650, as one-unit strips between ATC* and P*.
        profit = VGroup()
        for q in range(90):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            profit.add(Polygon(ax.c2p(left, 70), ax.c2p(right, 70), ax.c2p(right, 155), ax.c2p(left, 155),
                               stroke_width=0, fill_color=SUPPLY, fill_opacity=PROFIT_OPACITY))
        profit.set_z_index(FILL_LAYER)
        profit_word = Tex('Profit', color=INK).scale(0.72).move_to(ax.c2p(45, 112.5)).set_z_index(WORD_LAYER)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$\pi^* = (155 - 70)\cdot 90$'),
                      work_line(r'$\pi^* = 7{,}650$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
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

        # ---- 3.g.efficient · Q_sp = 120, where MC meets demand (yellow, as on the sheet).
        efficient_dot = Dot(ax.c2p(120, 140), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER)
        efficient_guide = DashedLine(ax.c2p(120, 140), ax.c2p(120, 0), color=FOCUS, stroke_width=2).set_z_index(GUIDE_LAYER)
        efficient_word = VGroup(
            Tex('120', color=FOCUS).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(120, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$Q_{sp}$', color=FOCUS).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(120, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(work, work_box)
        work = VGroup(work_line(r'$20 + Q = 200 - \tfrac{1}{2}Q$'), work_line(r'$\tfrac{3}{2}Q = 180$'),
                      work_line(r'$Q_{sp} = 120$', FOCUS)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        self.remove(note)
        note = teaching(r'$Q_{sp}$: the socially efficient quantity, where marginal cost meets demand.')
        self.play(*focus(), FadeIn(work[0]), FadeIn(work[1]), FadeIn(note))
        self.play(FadeIn(work[2]), FadeIn(efficient_dot))
        self.play(Create(efficient_guide), FadeIn(efficient_word))
        self.pause('3.g.efficient')

        # ---- 3.g · DWL: the units between q* and Q_sp, from MC up to demand, as grey strips.
        loss = VGroup()
        for q in range(90, 120):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            loss.add(Polygon(ax.c2p(left, mc(left)), ax.c2p(right, mc(right)), ax.c2p(right, d(right)), ax.c2p(left, d(left)),
                             stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY_STRIPS))
        loss.set_z_index(FILL_LAYER)
        # The triangle is too narrow for its name: DWL sits just above its top edge, left of MC.
        loss_word = Tex('DWL', color=INK).scale(0.6).move_to(ax.c2p(115, 167)).set_z_index(WORD_LAYER)
        self.remove(note)
        note = teaching(r'DWL: every unit between $q^*$ and $Q_{sp}$, from MC up to demand.')
        self.play(LaggedStart(*[FadeIn(strip) for strip in loss], lag_ratio=0.18), FadeIn(note), run_time=1.6)
        self.remove(*loss)
        self.add(loss)
        self.play(FadeIn(loss_word))
        self.pause('3.g')

        # ---- 4.a · Duopoly: the best-response graph from the sheet, and firm A's side solve.
        monopoly_picture = [ax, axis_words, demand_line, demand_word, demand_intercept, mr_line, mc_line, atc_curve,
                            monopoly_words, cost_intercept, choice_dot, quantity_guide, quantity_word, up_guide,
                            price_dot, price_guide, price_word, atc_dot, atc_guide, atc_word, profit, profit_word,
                            efficient_dot, efficient_guide, efficient_word, loss, loss_word]
        self.remove(head, context, note, work)
        self.play(*[FadeOut(m) for m in monopoly_picture], *focus(), run_time=0.8)
        head = title('Duopoly')
        context = subtitle(head, r'Two sellers: $Q = q_A + q_B$.')
        # E4's best-response graph: both axes to 400, so each best response runs from axis to axis as on the sheet.
        br_ax = style_axes([0, 400, 100], [0, 400, 100], x_length=4.4, y_length=4.4)
        br_ax.shift(np.array([BR_X, BR_Y, 0]) - br_ax.c2p(0, 0))
        # BR_A's name sits right of the q_B axis near its top, so that axis's caption sits under q_B (C4's form).
        q_b_word = Tex('$q_B$', color=INK).scale(0.8).next_to(br_ax.c2p(0, 400), LEFT, buff=0.23)
        br_words = VGroup(
            q_b_word,
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(q_b_word, DOWN, buff=0.08),
            Tex('$q_A$', color=INK).scale(0.8).next_to(br_ax.c2p(400, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(br_ax.c2p(400, 0), DOWN, buff=0.73))
        br_a = Line(br_ax.c2p(90, 0), br_ax.c2p(0, 360), color=ROW_PLAYER, stroke_width=3)
        br_a_word = Tex('$BR_A$', color=INK).scale(WORD_SCALE).next_to(br_ax.c2p(0, 360), RIGHT, buff=0.22)
        work = VGroup(work_line(r'$MR_A = MC_A$'),
                      work_line(r'$200 - q_A - \tfrac{1}{2}q_B = 20 + q_A$'),
                      work_line(r'$180 - \tfrac{1}{2}q_B = 2q_A$'),
                      work_line(r'$BR_A$: $q_A = 90 - \tfrac{1}{4}q_B$', ROW_PLAYER)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        note = teaching("Firm A's marginal revenue depends on how much firm B sells.")
        self.play(FadeIn(head), FadeIn(context), FadeIn(br_ax), FadeIn(br_words), *focus(1),
                  FadeIn(work[0]), FadeIn(work[1]), FadeIn(note))
        self.play(FadeIn(work[2]))
        self.play(FadeIn(work[3]), FadeIn(br_a), FadeIn(br_a_word))
        self.pause('4.a')

        # ---- 4.b.symmetry · Firm B's best response by symmetry, as the sheet does it.
        br_b = Line(br_ax.c2p(0, 90), br_ax.c2p(360, 0), color=COL_PLAYER, stroke_width=3)
        br_b_word = Tex('$BR_B$', color=INK).scale(WORD_SCALE).next_to(br_ax.c2p(360, 0), UR, buff=0.12)
        br_b_line = work_line(r'$BR_B$: $q_B = 90 - \tfrac{1}{4}q_A$', COL_PLAYER)
        br_b_line.next_to(work, DOWN, buff=WORK_GAP, aligned_edge=LEFT)
        symmetry_word = Tex(narration('symmetry'), color=CAPTION).scale(0.5).next_to(br_b_line, RIGHT, buff=0.25)
        self.remove(note)
        note = teaching("Firm B's problem is the same, with A and B swapped.")
        self.play(FadeIn(br_b_line), FadeIn(symmetry_word), FadeIn(br_b), FadeIn(br_b_word), FadeIn(note))
        self.pause('4.b.symmetry')

        # ---- 4.b · The crossing: Nash equilibrium at 72 each, the sheet's boxed result.
        nash_dot = Dot(br_ax.c2p(72, 72), radius=0.07, color=NASH).set_z_index(DOT_LAYER)
        nash_guides = VGroup(DashedLine(br_ax.c2p(72, 72), br_ax.c2p(72, 0), color=GUIDE, stroke_width=2),
                             DashedLine(br_ax.c2p(72, 72), br_ax.c2p(0, 72), color=GUIDE, stroke_width=2)).set_z_index(GUIDE_LAYER)
        nash_readouts = VGroup(
            Tex('72', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(br_ax.c2p(72, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(br_ax.c2p(72, 0) + DOWN * QUANTITY_LABEL_OFFSET),
            Tex(r'$q_B^* = 72$', color=GUIDE).scale(PRICE_SCALE).next_to(br_ax.c2p(0, 72), LEFT, buff=0.2))
        nash_word = Tex('Nash Equilibrium', color=NASH).scale(0.6).next_to(br_ax.c2p(72, 72), UR, buff=0.15)
        self.remove(work, br_b_line, symmetry_word)
        work = VGroup(work_line(r'$q_A^* = 90 - \tfrac{1}{4}q_A^*$'),
                      work_line(r'$\tfrac{5}{4}q_A^* = 90$'),
                      work_line(r'$q_A^* = q_B^* = 72$', GUIDE),
                      work_line(r'$Q = 144$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching('Neither firm can do better by changing its output alone.')
        self.play(FadeIn(nash_dot), FadeIn(nash_word), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(Create(nash_guides[0]), Create(nash_guides[1]), FadeIn(nash_readouts), FadeIn(work[2]), FadeIn(work_box))
        self.play(FadeIn(work[3]))
        self.pause('4.b')

        # ---- 4.c · Back on the market graph: Q = 144 up to demand, P* = 128, beside the monopoly in grey.
        duopoly_picture = [br_ax, br_words, br_a, br_a_word, br_b, br_b_word, nash_dot, nash_guides, nash_readouts, nash_word]
        monopoly_reference = VGroup(
            DashedLine(ax.c2p(90, 0), ax.c2p(90, 155), color=MUTED, stroke_width=2),
            DashedLine(ax.c2p(90, 155), ax.c2p(0, 155), color=MUTED, stroke_width=2),
            Dot(ax.c2p(90, 155), radius=0.065, color=MUTED),
            Tex('155', color=CAPTION).scale(PRICE_SCALE).next_to(ax.c2p(0, 155), LEFT, buff=0.2),
            Tex('90', color=CAPTION).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(90, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q^*$', color=CAPTION).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(90, 0) + DOWN * QUANTITY_LABEL_OFFSET)).set_z_index(1.5)
        duopoly_guide = DashedLine(ax.c2p(144, 0), ax.c2p(144, 128), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        duopoly_dot = Dot(ax.c2p(144, 128), radius=0.07, color=DEMAND).set_z_index(DOT_LAYER)
        duopoly_price = VGroup(
            DashedLine(ax.c2p(144, 128), ax.c2p(0, 128), color=DEMAND, stroke_width=2),
            Tex(r'$P^* = 128$', color=DEMAND).scale(PRICE_SCALE).next_to(ax.c2p(0, 128), LEFT, buff=0.2)).set_z_index(GUIDE_LAYER)
        duopoly_quantity = VGroup(
            Tex('144', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(144, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$Q$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(144, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(work, work_box, note)
        self.play(*[FadeOut(m) for m in duopoly_picture], run_time=0.6)
        work = VGroup(work_line(r'$P = 200 - \tfrac{1}{2}(72 + 72)$'),
                      work_line(r'$P = 200 - 72$'),
                      work_line(r'$P^* = 128$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2)
        note = teaching('Two sellers: more output, lower price.')
        self.play(FadeIn(ax), FadeIn(axis_words), FadeIn(demand_line), FadeIn(demand_word), FadeIn(demand_intercept),
                  FadeIn(monopoly_reference), FadeIn(duopoly_quantity), *focus(2), FadeIn(work[0]))
        self.play(Create(duopoly_guide), FadeIn(duopoly_dot), FadeIn(work[1]))
        self.play(Create(duopoly_price[0]), FadeIn(duopoly_price[1]), FadeIn(work[2]), FadeIn(work_box), FadeIn(note))
        self.pause('4.c')

        # ---- 5.a · Competitive: the sheet's firm graph left and market graph right, on one price scale.
        market_picture = [ax, axis_words, demand_line, demand_word, demand_intercept, monopoly_reference,
                          duopoly_guide, duopoly_dot, duopoly_price, duopoly_quantity]
        self.remove(head, context, note, work, work_box)
        self.play(*[FadeOut(m) for m in market_picture], *focus(), run_time=0.6)
        head = title('Perfect Competition')
        context = subtitle(head, 'Many sellers.')
        firm_ax = style_axes([0, 80, 10], [0, 220, 50], x_length=2.6, y_length=4.6)
        firm_ax.shift(np.array([FIRM_X, MARKET_Y, 0]) - firm_ax.c2p(0, 0))
        small_ax = style_axes([0, 400, 100], [0, 220, 50], x_length=3.8, y_length=4.6)
        small_ax.shift(np.array([SMALL_MARKET_X, MARKET_Y, 0]) - small_ax.c2p(0, 0))
        graph_words = VGroup()
        for graph, x_max, name, x_name, unit_name in [(firm_ax, 80, 'Firm', 'q', 'units'), (small_ax, 400, 'Market', 'Q', 'units')]:
            graph_words.add(
                Tex('P', color=INK).scale(0.8).next_to(graph.c2p(0, 220), LEFT, buff=0.23),
                Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(graph.c2p(0, 220), RIGHT, buff=0.22),
                Tex(x_name, color=INK).scale(0.8).next_to(graph.c2p(x_max, 0), DOWN, buff=0.23),
                Tex(r'\textsf{' + unit_name + '}', color=CAPTION).scale(0.55).next_to(graph.c2p(x_max, 0), DOWN, buff=0.73),
                Tex(narration(name), color=CAPTION).scale(0.6).move_to(graph.c2p(x_max, 220), aligned_edge=RIGHT))
        firm_mc = Line(firm_ax.c2p(0, 20), firm_ax.c2p(80, 100), color=MC_COLOR, stroke_width=3)
        firm_atc = polyline([firm_ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, 80, 200)], ATC_COLOR, 3)
        firm_words = VGroup(
            Tex('MC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(80, 100), RIGHT, buff=0.15),
            Tex('ATC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(80, atc(80)), UR, buff=0.08))
        small_demand = Line(small_ax.c2p(0, 200), small_ax.c2p(400, 0), color=DEMAND, stroke_width=3)
        small_supply = Line(small_ax.c2p(0, 20), small_ax.c2p(400, 60), color=MC_COLOR, stroke_width=3)
        small_words = VGroup(
            Tex('D', color=INK).scale(WORD_SCALE).next_to(small_ax.c2p(400, 0), UR, buff=0.12),
            Tex('S', color=INK).scale(WORD_SCALE).next_to(small_ax.c2p(400, 60), RIGHT, buff=0.15))
        note = teaching('Competitive firms are what we call price takers.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(firm_ax), FadeIn(small_ax), FadeIn(graph_words),
                  FadeIn(firm_mc), FadeIn(firm_atc), FadeIn(firm_words), FadeIn(small_demand), FadeIn(small_supply),
                  FadeIn(small_words), FadeIn(note))
        self.pause('5.a')

        # ---- 5.b · Step 0: supply meets demand at Q* = 300, P* = 50; the price carries across as the firm's MR.
        market_dot = Dot(small_ax.c2p(300, 50), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        market_marks = VGroup(
            DashedLine(small_ax.c2p(300, 50), small_ax.c2p(300, 0), color=GUIDE, stroke_width=2),
            DashedLine(small_ax.c2p(300, 50), small_ax.c2p(0, 50), color=GUIDE, stroke_width=2)).set_z_index(GUIDE_LAYER)
        market_readouts = VGroup(
            Tex('300', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(small_ax.c2p(300, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$Q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(small_ax.c2p(300, 0) + DOWN * QUANTITY_LABEL_OFFSET),
            Tex(r'$P^* = 50$', color=GUIDE).scale(PRICE_SCALE).next_to(small_ax.c2p(0, 50), LEFT, buff=0.2))
        firm_mr = Line(firm_ax.c2p(80, 50), firm_ax.c2p(0, 50), color=DEMAND, stroke_width=3)
        firm_mr_word = Tex('MR', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(80, 50), RIGHT, buff=0.15)
        work = VGroup(work_line(r'$200 - \tfrac{1}{2}Q = 20 + \tfrac{1}{10}Q$'),
                      work_line(r'$180 = \tfrac{3}{5}Q$'),
                      work_line(r'$Q^* = 300$', GUIDE),
                      work_line(r'$P^* = 20 + 30 = 50 = MR$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = VGroup(SurroundingRectangle(work[2], color=GUIDE, buff=0.08, stroke_width=2),
                          SurroundingRectangle(work[3], color=GUIDE, buff=0.08, stroke_width=2))
        self.remove(note)
        note = teaching('Step 0: supply and demand set the market price.')
        self.play(FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]), FadeIn(work_box[0]), FadeIn(market_dot), Create(market_marks[0]), FadeIn(market_readouts[:2]))
        self.play(FadeIn(work[3]), FadeIn(work_box[1]), Create(market_marks[1]), FadeIn(market_readouts[2]))
        self.play(Create(firm_mr), FadeIn(firm_mr_word))
        self.pause('5.b')

        # ---- 5.c · Step 1: MC = MR at q* = 30 on the firm graph.
        firm_dot = Dot(firm_ax.c2p(30, 50), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        firm_guide = DashedLine(firm_ax.c2p(30, 50), firm_ax.c2p(30, 0), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        firm_quantity = VGroup(
            Tex('30', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(firm_ax.c2p(30, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(firm_ax.c2p(30, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        self.remove(work, work_box)
        work = VGroup(work_line(r'$20 + q = 50$'),
                      work_line(r'$q^* = 30$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'Every unit up to $q^*$ adds more to revenue than to cost.')
        self.play(*focus(1), FadeIn(work[0]), FadeIn(firm_dot), FadeIn(note))
        self.play(Create(firm_guide), FadeIn(firm_quantity), FadeIn(work[1]), FadeIn(work_box))
        self.pause('5.c')

        # ---- 5.d · Step 2: the firm takes the market price, P* = 50.
        firm_price = Tex(r'$P^* = 50$', color=DEMAND).scale(PRICE_SCALE).next_to(firm_ax.c2p(0, 50), LEFT, buff=0.2)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$P^* = 50$', GUIDE))
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[0], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching('A price taker sells every unit at the market price.')
        self.play(*focus(2), FadeIn(firm_price), FadeIn(work), FadeIn(work_box), FadeIn(note))
        self.pause('5.d')

        # ---- 5.e · Step 3, "on the graph": q* lands on the bottom of ATC, ATC* = 50.
        atc_floor = Dot(firm_ax.c2p(30, 50), radius=0.12, color=ATC_COLOR).set_z_index(DOT_LAYER - 1)
        self.remove(work, work_box)
        work = VGroup(work_line(r'$ATC^* = 50$', GUIDE))
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[0], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching('Average total cost is at its lowest, right at the price.')
        self.play(*focus(3), FadeIn(atc_floor), FadeIn(work), FadeIn(work_box), FadeIn(note))
        self.pause('5.e')

        # ---- 5.f · Step 4: no profit, the long run equilibrium (the sheet's words).
        self.remove(work, work_box)
        work = VGroup(work_line(r'$\pi^* = (50 - 50)\cdot 30$'),
                      work_line(r'$\pi^* = 0$', GUIDE)).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
        work.move_to([PANEL_LEFT, WORK_TOP, 0], aligned_edge=UL)
        work_box = SurroundingRectangle(work[1], color=GUIDE, buff=0.08, stroke_width=2)
        self.remove(note)
        note = teaching(r'$\pi = 0$. Long run equilibrium.')
        self.play(*focus(4), FadeIn(work[0]), FadeIn(note))
        self.play(FadeIn(work[1]), FadeIn(work_box))
        self.pause('5.f')

        # ---- 5.g · Step 5 (the sheet's words).
        self.remove(note)
        note = teaching('No entry or exit.')
        self.play(*focus(5), FadeIn(note))
        self.pause('5.g')

        # ---- 6.a · More sellers: each seller's MR is the price less half its own output, so P - MC = q/2.
        competitive_picture = [firm_ax, small_ax, graph_words, firm_mc, firm_atc, firm_words, small_demand, small_supply,
                               small_words, market_dot, market_marks, market_readouts, firm_mr, firm_mr_word, firm_dot,
                               firm_guide, firm_quantity, firm_price, atc_floor, problem, card_head]
        self.remove(head, context, note, work, work_box)
        self.play(*[FadeOut(m) for m in competitive_picture], run_time=0.8)
        head = title('More Sellers')
        context = subtitle(head, r'$n$ similar sellers.')
        sellers = ValueTracker(1)
        outcome_q = lambda: market_q(sellers.get_value())
        outcome_p = lambda: d(outcome_q())
        outcome_mc = lambda: mc(firm_q(sellers.get_value()))
        outcome_dot = Dot(ax.c2p(90, 155), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER)
        outcome_dot.add_updater(lambda m: m.move_to(ax.c2p(outcome_q(), outcome_p())))
        cost_dot = Dot(ax.c2p(90, 110), radius=0.065, color=MC_COLOR).set_z_index(DOT_LAYER)
        cost_dot.add_updater(lambda m: m.move_to(ax.c2p(outcome_q(), outcome_mc())))
        outcome_drop = DashedLine(ax.c2p(90, 0), ax.c2p(90, 155), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        # Rebuilt each frame (B5's idiom) so the dashes keep their length as the guides grow and shrink.
        outcome_drop.add_updater(lambda m: m.become(DashedLine(ax.c2p(outcome_q(), 0), ax.c2p(outcome_q(), outcome_p()),
                                                               color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)))
        outcome_across = DashedLine(ax.c2p(0, 155), ax.c2p(90, 155), color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)
        outcome_across.add_updater(lambda m: m.become(DashedLine(ax.c2p(0, outcome_p()), ax.c2p(outcome_q(), outcome_p()),
                                                                 color=GUIDE, stroke_width=2).set_z_index(GUIDE_LAYER)))
        outcome_price = VGroup(Tex('$P=$', color=GUIDE), DecimalNumber(155, num_decimal_places=0, color=GUIDE))
        outcome_price.scale(PRICE_SCALE).arrange(RIGHT, buff=0.14)
        outcome_price.add_updater(lambda m: (m[1].set_value(round(outcome_p(), 4)), m.arrange(RIGHT, buff=0.14),
                                             m.next_to(ax.c2p(0, outcome_p()), LEFT, buff=0.2)))
        outcome_quantity = DecimalNumber(90, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
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
                                            m.move_to(ax.c2p(330, 185))))
        rolling = [outcome_dot, cost_dot, outcome_drop, outcome_across, outcome_price, outcome_quantity, outcome_symbol,
                   markup_bracket, markup_word, seller_count]
        for m in rolling:
            m.update()                       # Digits must already match before a number fades in.
        # The reason, from the sheet's MR: the duopolist's MR rewritten with the price.
        mr_lines = VGroup(work_line(r'$MR_A = 200 - q_A - \tfrac{1}{2}q_B$', MR_COLOR),
                          work_line(r'$= P - \tfrac{1}{2}q_A$', MR_COLOR),
                          work_line(r'$MR = MC$, so $P - MC = \tfrac{1}{2}q$')).arrange(DOWN, aligned_edge=LEFT, buff=WORK_GAP)
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
        for k, values in enumerate([(1, 90, 90, 155, 45), (2, 72, 144, 128, 36), (3, 60, 180, 110, 30),
                                    (6, 40, 240, 80, 20), (15, 20, 300, 50, 10)]):
            rows.add(VGroup(*[Tex(str(v), color=INK).scale(0.62).move_to([x, TABLE_TOP - 0.25 - ROW_STEP * (k + 0.6), 0])
                              for v, x in zip(values, TABLE_X)]))
        self.remove(*rolling)
        note = teaching(r"Each seller's MR is the price minus half its own output.")
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

        # ---- 6.b.six · n = 6.
        self.play(sellers.animate.set_value(6), run_time=2.6, rate_func=smooth)
        self.play(FadeIn(rows[3]), run_time=0.5)
        self.pause('6.b.six')

        # ---- 6.b · n = 15: more output, a lower price, a price closer to marginal cost.
        self.play(sellers.animate.set_value(15), run_time=3.0, rate_func=smooth)
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
        context = subtitle(head, 'One market, three outcomes.')
        outcomes = VGroup()
        for q_out, p_out, name in [(90, 155, 'Monopoly'), (144, 128, 'Duopoly'), (300, 50, 'Competitive')]:
            outcomes.add(VGroup(
                DashedLine(ax.c2p(q_out, 0), ax.c2p(q_out, p_out), color=GUIDE, stroke_width=2),
                DashedLine(ax.c2p(q_out, p_out), ax.c2p(0, p_out), color=GUIDE, stroke_width=2),
                Dot(ax.c2p(q_out, p_out), radius=0.07, color=GUIDE),
                Tex(str(p_out), color=GUIDE).scale(PRICE_SCALE).next_to(ax.c2p(0, p_out), LEFT, buff=0.2),
                Tex(str(q_out), color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(q_out, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                Tex(name, color=INK).scale(0.6).next_to(ax.c2p(q_out, p_out), UR, buff=0.12)).set_z_index(GUIDE_LAYER))
        problem.set_color(INK).set_opacity(1)
        card_head.set_opacity(1)
        note = teaching('Market power leads to inefficient markets.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(problem), FadeIn(card_head))
        self.play(LaggedStart(*[FadeIn(outcome) for outcome in outcomes], lag_ratio=0.5), FadeIn(note), run_time=2.2)
        self.pause('7.a')
