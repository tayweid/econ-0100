# maniml E4_Animation.py EpisodeE4
# Storyboard: E4_Notes.md. All lesson choreography stays in construct().
# Duopoly from Taylor's handwritten sheet (04_Handwritten.pdf): market demand P = 200 - Q/2, every firm MC = 20 + q.
# Monopoly MR = 200 - q, q* = 90, P* = 155; duopoly MR_A = 200 - q_A - q_B/2, BR_A: q_A = 90 - q_B/4,
# Nash q_A* = q_B* = 72, Q = 144, P* = 128.
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


class EpisodeE4(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        PRICE_SCALE, CURVE_WORD_SCALE = 0.7, 0.7
        ROW_SCALE, ROW_GAP = 0.72, 0.26          # side-panel algebra rows, as C2's side solve
        EQUATION_SCALE = 0.6                     # standing equations in open graph space
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS = 3, 2, 0.07
        # Firm theory palette (shared_E.md); firm A and firm B keep Part D's player colors.
        MC_COLOR, MR_COLOR, ATC_COLOR = SUPPLY, PINK, TOTAL
        FIRM_A, FIRM_B = ROW_PLAYER, COL_PLAYER
        # Layout: the market graph on the left; right of it either the algebra panel (divider at 2.45, as C2)
        # or the best-response graph. Beside a definition the best-response graph moves left (D1's divider at 0.3).
        # The best-response graph's origin keeps its right-hand words (firm A, BR_B) inside the 0.6 safe margin.
        MARKET_ORIGIN = np.array([-5.4, BODY_MID - 2.15, 0])
        BR_ORIGIN = np.array([2.45, BODY_MID - 2.15, 0])
        BR_SHIFT = LEFT * 8.05
        PANEL_X, SOLVE_X = 5.2, 3.95
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Taxonomy grid: a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4

        # The model (the sheet), as one-line functions.
        demand = lambda Q: 200 - Q / 2
        mc = lambda q: 20 + q
        start_a = lambda q_b: 200 - q_b / 2           # where firm A's demand and MR_A meet the price axis
        best_a = lambda q_b: 90 - q_b / 4             # BR_A: MR_A = MC_A
        MONOPOLY_Q, NASH_Q = 90, 72                   # the sheet's boxed answers
        MARKET_Q = 2 * NASH_Q                         # 144
        MONOPOLY_P, MARKET_P = demand(MONOPOLY_Q), demand(MARKET_Q)   # 155 and 128, read from demand

        # The one object factory: the yellow bottom line.
        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)

        # ---- 0.a · The shared bumper with E4's thesis from the notes header.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 4)
        thesis = Tex(r'\textit{When sellers play games with each other}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a.last · The market-structures taxonomy, last episode's cell boxed.
        head = title('Monopoly')
        context = subtitle(head, 'One seller, many buyers.')
        grid_left = TAXONOMY_X - (LABEL_W + 2 * CELL_W) / 2
        grid_right = grid_left + LABEL_W + 2 * CELL_W
        grid_top = BODY_MID + (HEADER_H + 3 * CELL_H) / 2
        column_x = [grid_left + LABEL_W + CELL_W * (i + 0.5) for i in range(2)]
        row_y = [grid_top - HEADER_H - CELL_H * (i + 0.5) for i in range(3)]
        # D1's Table look: rules between rows and columns only, no outer frame. The one-seller row has no
        # column rule: differentiation does not matter with one seller.
        taxonomy_rules = VGroup(
            *[Line([grid_left, grid_top - HEADER_H - CELL_H * i, 0], [grid_right, grid_top - HEADER_H - CELL_H * i, 0],
                   color=MUTED, stroke_width=2) for i in range(3)],
            Line([grid_left + LABEL_W, grid_top, 0], [grid_left + LABEL_W, grid_top - HEADER_H - 3 * CELL_H, 0],
                 color=MUTED, stroke_width=2),
            Line([grid_left + LABEL_W + CELL_W, grid_top, 0], [grid_left + LABEL_W + CELL_W, grid_top - HEADER_H - 2 * CELL_H, 0],
                 color=MUTED, stroke_width=2))
        column_words = VGroup(Tex('Homogeneous', color=GUIDE), Tex('Differentiated', color=GUIDE)).scale(0.75)
        for word, x in zip(column_words, column_x):
            word.move_to([x, grid_top - HEADER_H / 2, 0])
        column_words[1].align_to(column_words[0], UP)
        row_words = VGroup(Tex('Many Sellers', color=GUIDE), Tex('Few Sellers', color=GUIDE),
                           Tex('One Seller', color=GUIDE)).scale(0.75)
        for word, y in zip(row_words, row_y):
            word.move_to([grid_left + LABEL_W / 2, y, 0])
        perfect = Tex(r'Perfect\\Competition').scale(0.75).move_to([column_x[0], row_y[0], 0])
        monopolistic = Tex(r'Monopolistic\\Competition').scale(0.75).move_to([column_x[1], row_y[0], 0])
        oligopoly = Tex('Oligopoly').scale(0.75).move_to([column_x[0], row_y[1], 0])
        monopoly = Tex('Monopoly').scale(0.75).move_to([(column_x[0] + column_x[1]) / 2, row_y[2], 0])
        taxonomy = VGroup(taxonomy_rules, column_words, row_words, perfect, monopolistic, oligopoly, monopoly)
        box = SurroundingRectangle(monopoly, buff=0.22, color=NASH)
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a.last')

        # ---- 1.a · The box moves to the few-sellers cell: oligopoly, defined in Taylor's words.
        self.remove(head, context)
        head = title('Oligopoly')
        note = teaching('Oligopoly: a few sellers with some but not complete control of the price.')
        self.play(Transform(box, SurroundingRectangle(oligopoly, buff=0.22, color=NASH)), FadeIn(head), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('1.a')

        # ---- 2.a · The firm's problem from the sheet, one row per fade.
        self.play(FadeOut(taxonomy), FadeOut(box), FadeOut(head), FadeOut(note))
        head = title("The Firm's Problem")
        objective = MathTex(r'\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}')
        step_one = MathTex(r'1.\enspace {{\mathrm{MC}}} = {{\mathrm{MR}}} \rightarrow q^*')
        step_one.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        step_one.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        step_two = MathTex(r'2.\enspace q^* \rightarrow {{\mathrm{D}}} \rightarrow P^*')
        step_two.get_part_by_tex(r'\mathrm{D}').set_color(DEMAND)
        step_three = MathTex(r'3.\enspace q^* \rightarrow {{\mathrm{ATC}}} \rightarrow \mathrm{ATC}^*')
        step_three.get_part_by_tex(r'\mathrm{ATC}').set_color(ATC_COLOR)
        step_four = MathTex(r'4.\enspace \pi^* = (P^* - \mathrm{ATC}^*)\cdot q^*')
        step_five = Tex(r'5.\enspace {{If}} $\pi^* \geq 0$ stay/enter')
        step_five_exit = Tex(r'If $\pi^* < 0$ exit')
        card = VGroup(objective, step_one, step_two, step_three, step_four, step_five).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        step_five_exit.next_to(step_five, DOWN, buff=0.2).align_to(step_five.get_part_by_tex('If'), LEFT)
        card.add(step_five_exit)
        objective.shift(UP * 0.15)
        card.scale(0.9).move_to([0, BODY_MID, 0])
        self.play(FadeIn(head), FadeIn(objective))
        self.play(FadeIn(step_one), run_time=0.6)
        self.play(FadeIn(step_two), run_time=0.6)
        self.play(FadeIn(step_three), run_time=0.6)
        self.play(FadeIn(step_four), run_time=0.6)
        self.play(FadeIn(step_five), FadeIn(step_five_exit), run_time=0.6)
        self.pause('2.a')

        # ---- 3.a · The sheet's market: demand and every firm's marginal cost, with the model rows beside it.
        self.play(FadeOut(card), FadeOut(head))
        head = title('Monopoly')
        context = subtitle(head, 'All firms are similar.')
        ax = style_axes([0, 400, 100], [0, 220, 50], x_length=5.6, y_length=4.6)
        ax.shift(MARKET_ORIGIN - ax.c2p(0, 0))
        price_word = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 220), LEFT, buff=0.23)
        price_unit = Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 220), RIGHT, buff=0.22)
        quantity_word = Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(400, 0), DOWN, buff=0.23)
        quantity_unit = Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(400, 0), DOWN, buff=0.73)
        demand_start = Tex('$200$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, 200), LEFT, buff=0.15)
        cost_start = Tex('$20$', color=MC_COLOR).scale(0.65).next_to(ax.c2p(0, 20), LEFT, buff=0.15)
        demand_line = Line(ax.c2p(0, 200), ax.c2p(400, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        mc_line = Line(ax.c2p(0, 20), ax.c2p(200, 220), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        demand_word = Tex('D', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(400, 0), UR, buff=0.12)
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(200, 220), RIGHT, buff=0.15)
        divider = Line([2.45, 2.3, 0], [2.45, -3.0, 0], color=MUTED, stroke_width=1.5)
        # The panel's rows are arranged once so each row has a fixed slot; later phases reuse the slots.
        panel_rows = VGroup(
            MathTex(r'\mathrm{D}\colon P = 200 - \tfrac{1}{2}Q', color=DEMAND),
            MathTex(r'\mathrm{MC} = 20 + q', color=MC_COLOR),
            MathTex(r'{{\mathrm{MR}_A = 200 - q_A}} \qquad {{Q = q_A}}'),
            MathTex(r'{{20 + q_A}} = {{200 - q_A}}'),
            MathTex(r'2q_A = 180'),
            MathTex(r'q_A = {{90}} = {{q^*}}'),
            MathTex(r'{{P^*}} = {{200 - \tfrac{1}{2}\cdot 90}} = {{155}}'))
        panel_rows[2].get_part_by_tex(r'\mathrm{MR}_A = 200 - q_A').set_color(MR_COLOR)
        panel_rows[3].get_part_by_tex('20 + q_A').set_color(MC_COLOR)
        panel_rows[3].get_part_by_tex('200 - q_A').set_color(MR_COLOR)
        panel_rows[5].get_part_by_tex('90').set_color(GUIDE)
        panel_rows[5].get_part_by_tex('q^*').set_color(GUIDE)
        panel_rows[6].get_part_by_tex('P^*').set_color(GUIDE)
        panel_rows[6].get_part_by_tex(r'200 - \tfrac{1}{2}\cdot 90').set_color(DEMAND)
        panel_rows[6].get_part_by_tex('155').set_color(GUIDE)
        panel_rows.arrange(DOWN, buff=ROW_GAP).scale(ROW_SCALE)
        panel_rows[2:].shift(DOWN * 0.15)
        panel_rows.move_to([PANEL_X, BODY_MID, 0])
        slots = [row.get_center() for row in panel_rows]
        model_rows, monopoly_rows = panel_rows[:2], panel_rows[2:]
        note = teaching('Costs come from the production function, not the structure of the market.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(price_word), FadeIn(price_unit),
                  FadeIn(quantity_word), FadeIn(quantity_unit), FadeIn(demand_start), FadeIn(cost_start),
                  FadeIn(demand_line), FadeIn(mc_line), FadeIn(demand_word), FadeIn(mc_word))
        self.play(FadeIn(divider), FadeIn(model_rows), FadeIn(note))
        self.pause('3.a')

        # ---- 3.b · One seller: firm A's marginal revenue, half of demand's quantity.
        mr_line = Line(ax.c2p(0, 200), ax.c2p(200, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH)
        mr_word = Tex('MR$_A$', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(200, 0), UR, buff=0.12)
        self.remove(note)
        self.play(FadeIn(mr_line), FadeIn(mr_word), FadeIn(monopoly_rows[0]))
        self.pause('3.b')

        # ---- 3.c · Step 1: MR = MC. The crossing first, then the algebra, then 90 carried to the axis.
        mono_dot = Dot(ax.c2p(MONOPOLY_Q, mc(MONOPOLY_Q)), radius=DOT_RADIUS, color=GUIDE).set_z_index(30)
        mono_drop = DashedLine(ax.c2p(MONOPOLY_Q, mc(MONOPOLY_Q)), ax.c2p(MONOPOLY_Q, 0),
                               color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        mono_number = DecimalNumber(MONOPOLY_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        mono_number.move_to(ax.c2p(MONOPOLY_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        mono_symbol = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(MONOPOLY_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
        note = teaching(r'1. $\mathrm{MC} = \mathrm{MR} \rightarrow q^*$')
        self.play(GrowFromCenter(mono_dot), FadeIn(monopoly_rows[1]), FadeIn(note))
        self.play(FadeIn(monopoly_rows[2]))
        self.play(FadeIn(monopoly_rows[3]))
        self.play(Create(mono_drop), TransformFromCopy(monopoly_rows[3].get_part_by_tex('90'), mono_number),
                  FadeIn(mono_symbol), run_time=1.2)
        self.pause('3.c')

        # ---- 3.d · Step 2: up from q* to demand, across to the price axis.
        mono_rise = DashedLine(ax.c2p(MONOPOLY_Q, mc(MONOPOLY_Q)), ax.c2p(MONOPOLY_Q, MONOPOLY_P),
                               color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        mono_price_dot = Dot(ax.c2p(MONOPOLY_Q, MONOPOLY_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(30)
        mono_across = DashedLine(ax.c2p(MONOPOLY_Q, MONOPOLY_P), ax.c2p(0, MONOPOLY_P),
                                 color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        mono_price_number = Tex('155', color=GUIDE).scale(PRICE_SCALE).next_to(ax.c2p(0, MONOPOLY_P), LEFT, buff=0.2)
        mono_price_prefix = Tex('$P^*=$', color=GUIDE).scale(PRICE_SCALE).next_to(mono_price_number, LEFT, buff=0.12)
        self.remove(note)
        note = teaching(r'2. $q^* \rightarrow \mathrm{D} \rightarrow P^*$')
        self.play(Create(mono_rise), FadeIn(note))
        self.play(GrowFromCenter(mono_price_dot), FadeIn(monopoly_rows[4]))
        self.play(Create(mono_across), TransformFromCopy(monopoly_rows[4].get_part_by_tex('155'), mono_price_number),
                  FadeIn(mono_price_prefix), run_time=1.2)
        self.pause('3.d')

        # ---- 4.a · Duopoly: a second seller in the same market. The monopoly price leaves; MR = MC stays.
        self.remove(head, note)
        head = title('Duopoly')
        duopoly_rows = VGroup(
            MathTex(r'Q = q_A + q_B'),
            MathTex(r'P = 200 - \tfrac{1}{2}(q_A + q_B)', color=DEMAND),
            MathTex(r'\mathrm{MR}_A = 200 - q_A - \tfrac{1}{2}q_B', color=MR_COLOR))
        for row, slot in zip(duopoly_rows, slots[2:5]):
            row.scale(ROW_SCALE).move_to([PANEL_X, slot[1], 0])
        note = teaching('Both of you are trying to sell into the same market.')
        self.play(FadeIn(head), FadeOut(monopoly_rows), FadeOut(mono_rise), FadeOut(mono_price_dot),
                  FadeOut(mono_across), FadeOut(mono_price_number), FadeOut(mono_price_prefix))
        self.play(FadeIn(duopoly_rows[0]), FadeIn(duopoly_rows[1]), FadeIn(note))
        self.pause('4.a')

        # ---- 4.b.zero · Firm A's graph: one tracker, q_B, moves firm A's demand, its MR and its choice.
        q_b = ValueTracker(0)
        firm_q = lambda: best_a(q_b.get_value())
        top = lambda: start_a(q_b.get_value())
        # Labels near the origin collide at the end of the 5.b sweep: firm A's D and MR names fade there.
        name_fade = lambda: smooth(np.clip((320 - q_b.get_value()) / 40, 0, 1))
        ghost_fade = lambda: smooth(np.clip((q_b.get_value() - 15) / 30, 0, 1))
        ghost_demand = Line(ax.c2p(0, 200), ax.c2p(400, 0), color=MUTED, stroke_width=2).set_z_index(-1)
        ghost_word = Tex('D', color=CAPTION).scale(CURVE_WORD_SCALE).next_to(ax.c2p(400, 0), UR, buff=0.12)
        ghost_word.add_updater(lambda m: m.set_opacity(ghost_fade()))
        firm_demand = Line(ax.c2p(0, 200), ax.c2p(400, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        firm_demand.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, top()), ax.c2p(2 * top(), 0)))
        firm_demand_word = Tex('D$_A$', color=INK).scale(CURVE_WORD_SCALE)
        firm_demand_word.add_updater(lambda m: m.next_to(ax.c2p(2 * top(), 0), UR, buff=0.12).set_opacity(name_fade()))
        mr_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, top()), ax.c2p(top(), 0)))
        mr_word.add_updater(lambda m: m.next_to(ax.c2p(top(), 0), UR, buff=0.12).set_opacity(name_fade()))
        mono_dot.add_updater(lambda m: m.move_to(ax.c2p(firm_q(), mc(firm_q()))))
        mono_drop.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(firm_q(), mc(firm_q())), ax.c2p(firm_q(), 0) + DOWN * 1e-4))
        mono_number.add_updater(lambda m: m.set_value(round(firm_q(), 4))
                                .move_to(ax.c2p(firm_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        firm_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        firm_symbol.add_updater(lambda m: m.move_to(ax.c2p(firm_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        firm_quantity_word = Tex('$q_A$', color=INK).scale(0.8).next_to(ax.c2p(400, 0), DOWN, buff=0.23)
        # Firm A's demand starts at 200 - q_B/2: its teal intercept rolls with q_B (and fades where it would meet
        # MC's 20 at the end of the 5.b sweep); the market's 200 turns grey with the ghost demand and shows once
        # firm A's intercept has moved off it.
        firm_start = DecimalNumber(200, num_decimal_places=0, color=DEMAND).scale(0.65)
        firm_start.add_updater(lambda m: m.set_value(round(top(), 4)).next_to(ax.c2p(0, top()), LEFT, buff=0.15)
                               .set_opacity(name_fade()))
        demand_start.set_color(CAPTION)
        demand_start.add_updater(lambda m: m.set_opacity(ghost_fade()))
        # The live row: firm B's quantity, the one input of sections 4 and 5.
        q_b_prefix = MathTex(r'q_B =', color=GUIDE).scale(ROW_SCALE).move_to([PANEL_X - 0.25, slots[5][1], 0])
        q_b_value = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(ROW_SCALE)
        q_b_value.add_updater(lambda m: m.set_value(round(q_b.get_value(), 4)).next_to(q_b_prefix, RIGHT, buff=0.12)
                              .set_y(q_b_prefix[-1].get_y()))
        live = [ghost_word, firm_demand, firm_demand_word, mr_line, mr_word, mono_dot, mono_drop, mono_number,
                firm_symbol, q_b_value, firm_start, demand_start]
        for m in live:
            m.update()
        self.remove(demand_line, demand_word, quantity_word, mono_symbol, note)
        self.add(ghost_demand, firm_demand, firm_start)
        note = teaching('The price depends on how much the other firm sells.')
        self.play(FadeIn(firm_demand_word), FadeIn(firm_quantity_word), FadeIn(firm_symbol),
                  FadeIn(duopoly_rows[2]), FadeIn(q_b_prefix), FadeIn(q_b_value), FadeIn(note))
        self.add(ghost_word)
        self.pause('4.b.zero')

        # ---- 4.b.seventy_two · Firm B sells 72: firm A's demand and MR slide down; its best quantity falls to 72.
        self.remove(note)
        self.play(q_b.animate.set_value(72), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('Your marginal revenue also depends on how much the other firm sells.')
        self.play(FadeIn(note))
        self.pause('4.b.seventy_two')

        # ---- 4.b · Firm B sells 144: firm A's best quantity falls to 54.
        self.remove(note)
        self.play(q_b.animate.set_value(144), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('The more the other firm sells, the less you want to sell.')
        self.play(FadeIn(note))
        self.pause('4.b')

        # ---- 5.a.rule · Best responses: back to q_B = 0, then MR_A = MC_A for any q_B.
        self.remove(note)
        self.play(q_b.animate.set_value(0), run_time=1.6, rate_func=smooth)
        for m in live:
            m.update()                       # Digits must already match before a number fades.
        self.remove(head, context)
        head = title('Best Responses')
        context = subtitle(head, 'The strategies are quantities.')
        br_rows = VGroup(
            MathTex(r'{{\mathrm{MR}_A}} = {{\mathrm{MC}_A}}'),
            MathTex(r'{{200 - q_A - \tfrac{1}{2}q_B}} = {{20 + q_A}}'),
            MathTex(r'180 - \tfrac{1}{2}q_B = 2q_A'),
            MathTex(r'\mathrm{BR}_A:\ q_A = 90 - \tfrac{1}{4}q_B', color=FIRM_A))
        br_rows[0].get_part_by_tex(r'\mathrm{MR}_A').set_color(MR_COLOR)
        br_rows[0].get_part_by_tex(r'\mathrm{MC}_A').set_color(MC_COLOR)
        br_rows[1].get_part_by_tex(r'200 - q_A - \tfrac{1}{2}q_B').set_color(MR_COLOR)
        br_rows[1].get_part_by_tex('20 + q_A').set_color(MC_COLOR)
        for row, slot in zip(br_rows, slots[2:6]):
            row.scale(ROW_SCALE).move_to([PANEL_X, slot[1], 0])
        q_b_value.clear_updaters()
        note = teaching('Decide our best response to every decision the other seller might make.')
        self.play(FadeOut(duopoly_rows), FadeOut(q_b_prefix), FadeOut(q_b_value), FadeIn(head), FadeIn(context))
        self.play(FadeIn(br_rows[0]), FadeIn(note))
        self.pause('5.a.rule')

        # ---- 5.a.substitute · Substitute the two curves.
        self.play(FadeIn(br_rows[1]))
        self.pause('5.a.substitute')

        # ---- 5.a.simplify · Collect the terms.
        self.play(FadeIn(br_rows[2]))
        self.pause('5.a.simplify')

        # ---- 5.a · Firm A's best response to any q_B.
        self.play(FadeIn(br_rows[3]))
        self.pause('5.a')

        # ---- 5.b.trace · The best-response graph replaces the algebra; one sweep of q_B traces BR_A.
        br_ax = style_axes([0, 400, 100], [0, 400, 100], x_length=4.6, y_length=4.6)
        br_ax.shift(BR_ORIGIN - br_ax.c2p(0, 0))
        br_words = VGroup(
            Tex('$q_A$', color=INK).scale(0.8).next_to(br_ax.c2p(400, 0), DOWN, buff=0.23),
            Tex(r'\textsf{firm A}', color=FIRM_A).scale(0.55).next_to(br_ax.c2p(400, 0), DOWN, buff=0.73),
            Tex('$q_B$', color=INK).scale(0.8).next_to(br_ax.c2p(0, 400), LEFT, buff=0.23),
            Tex(r'\textsf{firm B}', color=FIRM_B).scale(0.55).next_to(br_ax.c2p(0, 400), RIGHT, buff=0.22))
        br_a_equation = MathTex(r'\mathrm{BR}_A:\ q_A = 90 - \tfrac{1}{4}q_B', color=FIRM_A).scale(EQUATION_SCALE)
        br_a_equation.move_to(br_ax.c2p(265, 370))
        br_point = Dot(br_ax.c2p(90, 0), radius=0.08, color=FIRM_A).set_z_index(31)
        br_point.add_updater(lambda m: m.move_to(br_ax.c2p(firm_q(), q_b.get_value())))
        br_across = DashedLine(br_ax.c2p(0, 0), br_ax.c2p(90, 0), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        br_across.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(0, q_b.get_value()),
                                                               br_ax.c2p(firm_q(), q_b.get_value()) + RIGHT * 1e-4))
        br_down = DashedLine(br_ax.c2p(90, 0), br_ax.c2p(90, 0) + UP * 1e-4, color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        br_down.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(firm_q(), 0),
                                                             br_ax.c2p(firm_q(), q_b.get_value()) + UP * 1e-4))
        br_trace = Line(br_ax.c2p(90, 0), br_ax.c2p(90, 0) + UP * 1e-4, color=FIRM_A, stroke_width=CURVE_WIDTH).set_z_index(5)
        br_trace.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(90, 0),
                                                              br_ax.c2p(firm_q(), q_b.get_value()) + UP * 1e-4))
        br_q_b_number = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(PRICE_SCALE)
        br_q_b_number.add_updater(lambda m: m.set_value(round(q_b.get_value(), 4))
                                  .next_to(br_ax.c2p(0, q_b.get_value()), LEFT, buff=0.2))
        br_q_b_prefix = MathTex(r'q_B =', color=GUIDE).scale(PRICE_SCALE)
        br_q_b_prefix.add_updater(lambda m: m.next_to(br_q_b_number, LEFT, buff=0.12)
                                  .shift(UP * (br_q_b_number.get_y() - m[-1].get_y())))
        br_q_a_number = DecimalNumber(90, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        br_q_a_number.add_updater(lambda m: m.set_value(round(firm_q(), 4))
                                  .move_to(br_ax.c2p(firm_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        br_q_a_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        br_q_a_symbol.add_updater(lambda m: m.move_to(br_ax.c2p(firm_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        tracing = [br_point, br_across, br_down, br_trace, br_q_b_number, br_q_b_prefix, br_q_a_number, br_q_a_symbol]
        for m in tracing:
            m.update()
        self.remove(note)
        self.play(FadeOut(model_rows), FadeOut(br_rows[:3]), FadeOut(divider),
                  ReplacementTransform(br_rows[3], br_a_equation), FadeIn(br_ax), FadeIn(br_words), run_time=1.2)
        self.add(br_trace)
        self.play(FadeIn(br_point), FadeIn(br_across), FadeIn(br_down), FadeIn(br_q_b_number), FadeIn(br_q_b_prefix),
                  FadeIn(br_q_a_number), FadeIn(br_q_a_symbol))
        self.play(q_b.animate.set_value(360), run_time=SWEEP_TIME, rate_func=smooth)
        br_a_word = Tex('BR$_A$', color=INK).scale(CURVE_WORD_SCALE).next_to(br_ax.c2p(0, 360), RIGHT, buff=0.22)
        for m in tracing:
            m.update()
            m.clear_updaters()
        # The point and its readouts stay through the hold, so q_B = 360 explains the market graph's q_A* = 0.
        self.play(FadeIn(br_a_word))
        self.pause('5.b.trace')

        # ---- 5.b · The definition, in D1's words: the market graph and the tracing marks leave, the best-response
        # graph slides left.
        for m in live:
            m.update()
            m.clear_updaters()
        market_view = [ax, price_word, price_unit, firm_quantity_word, quantity_unit, demand_start, firm_start,
                       cost_start, ghost_demand, ghost_word, firm_demand, firm_demand_word, mc_line, mc_word, mr_line,
                       mr_word, mono_dot, mono_drop, mono_number, firm_symbol]
        br_graph = VGroup(br_ax, br_words, br_trace, br_a_word, br_a_equation)
        self.remove(*br_graph)
        self.add(br_graph)
        definition_divider = Line([0.3, 2.5, 0], [0.3, -3.0, 0], color=MUTED, stroke_width=1.5)
        best_response = VGroup(
            Tex('Best Response', color=DEFINITION),
            Tex('The strategy that gives a player', color=INK),
            Tex('the highest payoff, given the strategies', color=INK),
            Tex('chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        best_response.move_to([0.85, 1.65, 0], aligned_edge=UL)
        self.play(*[FadeOut(m) for m in market_view + tracing], run_time=0.6)
        self.play(br_graph.animate.shift(BR_SHIFT), GrowFromEdge(definition_divider, UP), run_time=1.0)
        self.play(FadeIn(best_response))
        self.pause('5.b')

        # ---- 5.c · Symmetry: firm B's best response is firm A's mirrored across the 45-degree line.
        diagonal = DashedLine(br_ax.c2p(0, 0), br_ax.c2p(250, 250), color=MUTED, stroke_width=1.5)
        symmetry_word = Tex(r'\textsf{symmetry}', color=CAPTION).scale(0.55).next_to(br_ax.c2p(250, 250), RIGHT, buff=0.1)
        br_b_line = Line(br_ax.c2p(0, 90), br_ax.c2p(360, 0), color=FIRM_B, stroke_width=CURVE_WIDTH).set_z_index(5)
        br_b_word = Tex('BR$_B$', color=INK).scale(CURVE_WORD_SCALE).next_to(br_ax.c2p(360, 0), UR, buff=0.12)
        br_b_equation = MathTex(r'\mathrm{BR}_B:\ q_B = 90 - \tfrac{1}{4}q_A', color=FIRM_B).scale(EQUATION_SCALE)
        br_b_equation.next_to(br_a_equation, DOWN, buff=0.22, aligned_edge=LEFT)
        self.play(FadeIn(diagonal), FadeIn(symmetry_word))
        self.play(TransformFromCopy(br_trace, br_b_line), run_time=1.4)
        self.play(FadeIn(br_b_word), FadeIn(br_b_equation))
        self.pause('5.c')

        # ---- 6.a · Where the best responses cross: the Nash equilibrium, values withheld.
        self.remove(head)
        head = title('Nash Equilibrium')
        nash_definition = VGroup(
            Tex('Nash Equilibrium', color=DEFINITION),
            Tex('A set of strategies such that no player', color=INK),
            Tex('can improve their payoff by unilaterally', color=INK),
            Tex('changing strategy.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        nash_definition.move_to([0.85, 1.65, 0], aligned_edge=UL)
        nash_dot = Dot(br_ax.c2p(NASH_Q, NASH_Q), radius=0.08, color=NASH).set_z_index(31)
        nash_guides = VGroup(
            DashedLine(br_ax.c2p(NASH_Q, NASH_Q), br_ax.c2p(NASH_Q, 0), color=GUIDE, stroke_width=GUIDE_WIDTH),
            DashedLine(br_ax.c2p(NASH_Q, NASH_Q), br_ax.c2p(0, NASH_Q), color=GUIDE, stroke_width=GUIDE_WIDTH)).set_z_index(10)
        nash_word = Tex('Nash Equilibrium', color=NASH).scale(0.6).next_to(nash_dot, UR, buff=0.12)
        # Values withheld: question marks hold the number slots until the algebra fills them.
        q_a_slot = br_ax.c2p(NASH_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET
        q_a_unknown = Tex('?', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(q_a_slot)
        q_a_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(br_ax.c2p(NASH_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
        q_a_value = Tex('72', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(q_a_slot)
        q_b_value_slot = Tex('72', color=GUIDE).scale(PRICE_SCALE).next_to(br_ax.c2p(0, NASH_Q), LEFT, buff=0.2)
        q_b_unknown = Tex('?', color=GUIDE).scale(PRICE_SCALE).move_to(q_b_value_slot)
        q_b_star = MathTex(r'q_B^* =', color=GUIDE).scale(PRICE_SCALE).next_to(q_b_value_slot, LEFT, buff=0.12)
        q_b_star.shift(UP * (q_b_value_slot.get_y() - q_b_star[-1].get_y()))
        self.play(FadeOut(best_response), FadeOut(diagonal), FadeOut(symmetry_word), FadeIn(head))
        self.play(FadeIn(nash_definition), GrowFromCenter(nash_dot), FadeIn(nash_word))
        self.play(Create(nash_guides[0]), Create(nash_guides[1]), FadeIn(q_a_unknown), FadeIn(q_a_symbol),
                  FadeIn(q_b_unknown), FadeIn(q_b_star))
        self.pause('6.a')

        # ---- 6.b.substitute · The sheet's solve: symmetric firms, so substitute q_B* = q_A* into BR_A.
        solve_rows = VGroup(
            VGroup(Tex(r'\textsf{symmetric}', color=CAPTION), MathTex(r'\rightarrow\ q_A^* = q_B^*')).arrange(RIGHT, buff=0.18),
            MathTex(r'q_A^* = 90 - \tfrac{1}{4}q_A^*'),
            MathTex(r'\tfrac{5}{4}\,q_A^* = 90'),
            MathTex(r'q_A^* = 90\cdot\tfrac{4}{5} = {{72}} = q_B^*'),
            MathTex(r'Q = q_A^* + q_B^* = {{144}}'))
        solve_rows[3].get_part_by_tex('72').set_color(GUIDE)
        solve_rows[4].get_part_by_tex('144').set_color(GUIDE)
        solve_rows.arrange(DOWN, buff=ROW_GAP + 0.08).scale(ROW_SCALE).move_to([SOLVE_X, BODY_MID, 0])
        self.play(FadeOut(nash_definition))
        self.play(FadeIn(solve_rows[0]))
        self.play(FadeIn(solve_rows[1]))
        self.pause('6.b.substitute')

        # ---- 6.b.solve · Collect and solve.
        self.play(FadeIn(solve_rows[2]))
        self.play(FadeIn(solve_rows[3]))
        self.pause('6.b.solve')

        # ---- 6.b · The 72 goes to both axes; both firms together sell 144.
        self.play(TransformFromCopy(solve_rows[3].get_part_by_tex('72'), q_a_value),
                  TransformFromCopy(solve_rows[3].get_part_by_tex('72'), q_b_value_slot),
                  FadeOut(q_a_unknown), FadeOut(q_b_unknown), run_time=1.2)
        self.play(FadeIn(solve_rows[4]))
        self.pause('6.b')

        # ---- 6.c.price · Back in the market: 144 units, up to demand, across to the price axis.
        self.remove(head, context)
        head = title('Duopoly')
        context = subtitle(head, 'All firms are similar.')
        br_graph.add(br_b_line, br_b_word, br_b_equation, nash_dot, nash_guides, nash_word, q_a_symbol, q_a_value,
                     q_b_value_slot, q_b_star)
        self.remove(*br_graph)
        self.add(br_graph)
        market_demand = Line(ax.c2p(0, 200), ax.c2p(400, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        demand_start.set_color(DEMAND)
        monopoly_reference = VGroup(
            DashedLine(ax.c2p(MONOPOLY_Q, MONOPOLY_P), ax.c2p(MONOPOLY_Q, 0), color=MUTED, stroke_width=GUIDE_WIDTH),
            DashedLine(ax.c2p(MONOPOLY_Q, MONOPOLY_P), ax.c2p(0, MONOPOLY_P), color=MUTED, stroke_width=GUIDE_WIDTH),
            Dot(ax.c2p(MONOPOLY_Q, MONOPOLY_P), radius=DOT_RADIUS, color=MUTED),
            Tex('155', color=CAPTION).scale(PRICE_SCALE).next_to(ax.c2p(0, MONOPOLY_P), LEFT, buff=0.2),
            Tex('90', color=CAPTION).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(MONOPOLY_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex(r'\textsf{Monopoly}', color=CAPTION).scale(0.55).next_to(ax.c2p(MONOPOLY_Q, MONOPOLY_P), UR, buff=0.08))
        monopoly_reference.set_z_index(2)
        market_number = Tex('144', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        market_symbol = Tex('$Q$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
        market_rise = DashedLine(ax.c2p(MARKET_Q, 0), ax.c2p(MARKET_Q, MARKET_P), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        market_dot = Dot(ax.c2p(MARKET_Q, MARKET_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(30)
        market_across = DashedLine(ax.c2p(MARKET_Q, MARKET_P), ax.c2p(0, MARKET_P), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        market_price = Tex('$P^*=128$', color=GUIDE).scale(PRICE_SCALE).next_to(ax.c2p(0, MARKET_P), LEFT, buff=0.2)
        self.play(FadeOut(solve_rows), FadeOut(definition_divider), br_graph.animate.shift(-BR_SHIFT),
                  FadeIn(head), FadeIn(context), run_time=1.2)
        self.play(FadeIn(ax), FadeIn(price_word), FadeIn(price_unit), FadeIn(quantity_word), FadeIn(quantity_unit),
                  FadeIn(demand_start), FadeIn(market_demand), FadeIn(demand_word), FadeIn(monopoly_reference))
        self.play(FadeIn(market_number), FadeIn(market_symbol))
        note = teaching(r'$P = 200 - \tfrac{1}{2}(72 + 72) = 200 - 72 = 128$')
        self.play(Create(market_rise), GrowFromCenter(market_dot), FadeIn(note))
        self.play(Create(market_across), FadeIn(market_price))
        self.pause('6.c.price')

        # ---- 6.c · The comparison with one seller.
        self.remove(note)
        note = teaching('Two sellers: more output, lower price.')
        self.play(FadeIn(note))
        self.pause('6.c')

        # ---- 7.a · Next time: more sellers, further down the demand curve.
        self.remove(head, context, note)
        head = title('Next Time')
        along = (ax.c2p(400, 0) - ax.c2p(0, 200)) / np.linalg.norm(ax.c2p(400, 0) - ax.c2p(0, 200))
        above = np.array([-along[1], along[0], 0])
        hint = Arrow(ax.c2p(MARKET_Q, MARKET_P) + along * 0.35 + above * 0.28,
                     ax.c2p(MARKET_Q, MARKET_P) + along * 1.9 + above * 0.28,
                     buff=0, thickness=2.0, color=MUTED)
        note = teaching('What happens with more sellers?')
        self.play(FadeIn(head), FadeIn(hint), FadeIn(note))
        self.pause('7.a')
