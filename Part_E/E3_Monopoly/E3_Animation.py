# maniml E3_Animation.py EpisodeE3
# Storyboard: E3_Notes.md. All lesson choreography stays in construct().
# Monopoly on E1 and E2's firm: TC = 1000 + q^2, MC = 2q, ATC = q + 1000/q. Demand P = 120 - Q, MR = 120 - 2Q,
# the demand E4 uses too. MR = MC at q* = 30, P* = 90, ATC* = 63.33, profit 800; Q_sp = 40 where MC meets demand. (Until 2026-11-11 this
# ran on the old 5.3/5.4 model, MC = q and D: P = 100 - Q/2; that build is in _archive/2026-11-11_consolidation/.)
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


class EpisodeE3(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        PRICE_SCALE, CURVE_WORD_SCALE, AREA_WORD_SCALE = 0.62, 0.7, 0.6
        ROW_SCALE, ROW_GAP, PAIR_GAP = 0.62, 0.17, 0.3     # side-panel rows, as C2's side solve
        # The live profit row's gaps, piece to piece: parentheses hug their numbers, = and the dot get TeX-like room.
        ROW_GAPS = (0.03, 0.08, 0.08, 0.03, 0.08, 0.11, 0.11)
        POLICY_GAP = 0.03                                  # a policy row's $ to its rolling number
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS, FOCUS_RADIUS = 3, 2, 0.07, 0.085
        BAR_GAP = 0.08
        SURPLUS_OPACITY, DWL_STRIP_OPACITY = 0.65, 0.8
        PROFIT_OPACITY, GOV_OPACITY = AREA_OPACITY, SURPLUS_OPACITY
        # Firm theory palette (shared_E.md).
        MC_COLOR, MR_COLOR, ATC_COLOR = SUPPLY, PINK, TOTAL
        # Top-level z order (the engine sorts top-level mobjects by z_index): fills under curves, the government's
        # band over profit, then curves, words, guides and dots. A group's set_z_index does not set its children's.
        FILL_LAYER, GOV_LAYER, CURVE_LAYER, POLICY_LAYER, WORD_LAYER, GUIDE_LAYER, DOT_LAYER = -3, -2, 0, 1, 6, 10, 30
        # Layout: the market graph on the left, 0 to 120 units: demand runs to its foot at 120 and MR to its foot
        # at 60, half of demand's; the side panel right of C2's grey divider.
        GRAPH_ORIGIN = np.array([-5.5, BODY_MID - 2.15, 0])
        X_LENGTH, Y_LENGTH, X_END, Y_TOP = 6.8, 4.6, 120, 140
        DIVIDER_X, PANEL_LEFT, WORK_INDENT = 2.45, 2.75, 0.25
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Curve ends: MC to (60, 120); ATC from its 118 level to q = 85; the dashed policy MC runs up to 134, above
        # MC's own name, and the dashed policy ATC stops there too.
        MC_END, ATC_TO, POLICY_TOP = 60, 85, 134
        # Taxonomy grid (E4's object): a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4

        # The model (E1 and E2's firm, and this episode's demand), as one-line functions of quantity.
        FIXED_COST = 1000
        TOP_PRICE = 120                                 # demand's and MR's start on the price axis
        BASE_ALPHA = 1                                  # demand share: P = 120 - Q / alpha
        demand = lambda Q, a=BASE_ALPHA: TOP_PRICE - Q / a
        marginal_revenue = lambda Q, a=BASE_ALPHA: TOP_PRICE - 2 * Q / a
        mc = lambda q: 2 * q
        atc = lambda q: q + FIXED_COST / q
        ATC_FROM = 9.2                                  # ATC(9.2) = 118, just under demand's start
        FIRST_Q, STEP_Q, LAST_Q = 20, 10, 50           # section 2: the notes' two quantities; the sweep ends as MR nears 0
        LOW_ALPHA = 0.5                                 # section 4: demand pivots down to P = 120 - 2Q, q* 30 -> 20
        TAX, LUMP_SUM, SUBSIDY, LUMP_WITH_SUBSIDY = 20, 500, 40, 1800    # whole-number outcomes; 40 reaches Q_sp

        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        dashed = lambda start, end, color: DashedLine(start, end + UP * 1e-4, color=color, stroke_width=GUIDE_WIDTH)

        # ---- 0.a · The shared bumper with E3's thesis from the notes header.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 3)
        thesis = Tex(r'\textit{Market power breaks the efficiency of markets.}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a.last · The market-structures taxonomy (E4's object), last episode's cell boxed.
        head = title('Perfect Competition')
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
        box = SurroundingRectangle(perfect, buff=0.22, color=NASH)
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a.last')

        # ---- 1.a · The box moves to the one-seller cell: monopoly, defined in Taylor's words.
        self.remove(head)
        head = title('Monopoly')
        note = teaching('A monopolist operates in a market with many buyers and one seller.')
        self.play(Transform(box, SurroundingRectangle(monopoly, buff=0.22, color=NASH)), FadeIn(head), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('1.a')

        # ---- 1.b · The graph: MC and ATC from the production function, with their rows beside it.
        ax = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=X_LENGTH, y_length=Y_LENGTH)
        ax.shift(GRAPH_ORIGIN - ax.c2p(0, 0))
        axis_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, Y_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, Y_TOP), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(X_END, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(X_END, 0), DOWN, buff=0.73))
        mc_line = Line(ax.c2p(0, 0), ax.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        atc_curve = polyline([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, ATC_TO, 200)],
                             ATC_COLOR, CURVE_WIDTH).set_z_index(CURVE_LAYER)
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15)
        atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(ATC_TO, atc(ATC_TO)), RIGHT, buff=0.15)
        # One subtitle from 1.b to 6.d: it stays in place while the titles change around it.
        context = subtitle(head, 'One seller, many buyers.')
        divider = Line([DIVIDER_X, 2.3, 0], [DIVIDER_X, -3.0, 0], color=MUTED, stroke_width=1.5)
        # The model rows, one fixed slot each: costs first (1.b), then demand (1.c).
        mc_row = MathTex(r'\mathrm{MC} = 2q', color=MC_COLOR)
        atc_row = MathTex(r'\mathrm{ATC} = q + 1000/q', color=ATC_COLOR)
        demand_row = MathTex(r'\mathrm{D}\colon P = 120 - Q', color=DEMAND)
        model_rows = VGroup(mc_row, atc_row, demand_row).scale(ROW_SCALE).arrange(DOWN, buff=ROW_GAP + 0.1, aligned_edge=LEFT)
        model_rows.move_to([PANEL_LEFT, 1.2, 0], aligned_edge=LEFT)
        self.remove(note)
        self.play(FadeOut(taxonomy), FadeOut(box), run_time=0.8)
        note = teaching('As with competitive firms, the production function gives MC and ATC.')
        self.play(FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(mc_line), FadeIn(atc_curve),
                  FadeIn(mc_word), FadeIn(atc_word))
        self.play(FadeIn(divider), FadeIn(mc_row), FadeIn(atc_row), FadeIn(note))
        self.pause('1.b')

        # ---- 1.c · Demand: the monopolist faces the whole market's downward-sloping demand.
        demand_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * BASE_ALPHA, 0), color=DEMAND, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        # Demand's name rides just above its lower end, and rides with it when demand pivots (4.a).
        demand_word_at = lambda a=BASE_ALPHA: ax.c2p(0.85 * TOP_PRICE * a, demand(0.85 * TOP_PRICE * a, a))
        demand_word = Tex('D / MB', color=INK).scale(CURVE_WORD_SCALE).next_to(demand_word_at(), UR, buff=0.1)
        demand_start = Tex('$120$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, TOP_PRICE), LEFT, buff=0.15)
        self.remove(note)
        note = teaching('Unlike competitive firms, a monopolist faces downward-sloping demand.')
        self.play(FadeIn(demand_line), FadeIn(demand_word), FadeIn(demand_start), FadeIn(demand_row), FadeIn(note))
        self.pause('1.c')

        # ---- 2.a · Marginal revenue: its definition joins demand in the panel; the cost rows step aside.
        self.remove(head, note)
        head = title('Marginal Revenue')
        mr_row = MathTex(r'\mathrm{MR} = 120 - 2Q', color=MR_COLOR)
        mr_definition = MathTex(r'{{\mathrm{MR}}} = \Delta \mathrm{TR} \,/\, \Delta Q')
        mr_definition.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        tr_one_row = MathTex(r'{{\mathrm{TR}_1}} = 100 \times 20 = 2{,}000')
        tr_two_row = MathTex(r'{{\mathrm{TR}_2}} = 90 \times 30 = 2{,}700')
        change_row = MathTex(r'\Delta \mathrm{TR} = {{10 \times 90}} - {{20 \times 10}} = 700')
        mr_value_row = MathTex(r'{{\mathrm{MR}}} = 700 \,/\, 10 = {{70}}')
        change_row.get_part_by_tex(r'10 \times 90').set_color(DEMAND)
        change_row.get_part_by_tex(r'20 \times 10').set_color(GUIDE)
        mr_value_row.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        mr_value_row.get_part_by_tex('70').set_color(MR_COLOR)
        revenue_rows = VGroup(demand_row.copy(), mr_row, mr_definition, tr_one_row, tr_two_row, change_row, mr_value_row)
        for row in revenue_rows[1:]:
            row.scale(ROW_SCALE)
        revenue_rows.arrange(DOWN, buff=ROW_GAP + 0.1, aligned_edge=LEFT)
        revenue_rows[2:].shift(DOWN * 0.25)
        revenue_rows.move_to([PANEL_LEFT, BODY_MID, 0], aligned_edge=LEFT)
        revenue_slots = [row.get_left() for row in revenue_rows]
        note = teaching('Marginal revenue: the change in revenue over the change in quantity.')
        self.play(FadeIn(head), FadeOut(mc_row), FadeOut(atc_row),
                  demand_row.animate.move_to(revenue_slots[0], aligned_edge=LEFT))
        self.play(FadeIn(mr_definition), FadeIn(note))
        self.pause('2.a')

        # ---- 2.b.first · The first of the notes' two points on demand: 20 units at 100, and its revenue.
        first_q, step_q = ValueTracker(FIRST_Q), ValueTracker(0)
        q_one = lambda: first_q.get_value()
        q_two = lambda: first_q.get_value() + step_q.get_value()

        # Every area is one-unit strips; a strip group follows its trackers through span(), low() and high().
        def strip_group(count, color, opacity, z):
            strips = VGroup(*[Polygon(ax.c2p(k, 0), ax.c2p(k + 0.5, 0), ax.c2p(k + 0.5, 1), ax.c2p(k, 1),
                                      stroke_width=0, fill_color=color, fill_opacity=0).set_z_index(z)
                              for k in range(count)]).set_z_index(z)
            strips.opacity = opacity
            return strips

        def follow_strips(strips):
            start, end = strips.span()
            for k, strip in enumerate(strips):
                left, right = max(k + BAR_GAP / 2, start), min(k + 1 - BAR_GAP / 2, end)
                low_left, low_right = strips.low(left), strips.low(right)
                high_left, high_right = strips.high(left), strips.high(right)
                if right - left < 1e-3 or max(high_left - low_left, high_right - low_right) < 1e-3:
                    strip.set_fill(opacity=0)
                    continue
                strip.set_points_as_corners([ax.c2p(left, low_left), ax.c2p(right, low_right), ax.c2p(right, high_right),
                                             ax.c2p(left, high_left), ax.c2p(left, low_left)])
                strip.set_fill(opacity=strips.opacity)

        # Revenue at the first point is P1 x Q1; at the second it keeps the common part, loses the price cut on
        # the first Q1 units (red) and gains the new units at the new price (strong teal).
        revenue_common = strip_group(LAST_Q, DEMAND, PROFIT_OPACITY, FILL_LAYER)
        revenue_common.span = lambda: (0, q_one())
        revenue_common.low, revenue_common.high = (lambda x: 0), (lambda x: demand(q_two()))
        revenue_loss = strip_group(LAST_Q, GUIDE, SURPLUS_OPACITY, FILL_LAYER)
        revenue_loss.span = lambda: (0, q_one())
        revenue_loss.low, revenue_loss.high = (lambda x: demand(q_two())), (lambda x: demand(q_one()))
        revenue_gain = strip_group(LAST_Q + STEP_Q + 1, DEMAND, SURPLUS_OPACITY, FILL_LAYER)
        revenue_gain.span = lambda: (q_one(), q_two())
        revenue_gain.low, revenue_gain.high = (lambda x: 0), (lambda x: demand(q_two()))
        revenue_strips = [revenue_common, revenue_loss, revenue_gain]
        for strips in revenue_strips:
            strips.add_updater(follow_strips)
            strips.update()
        # Each point: a teal dot on demand, a red drop to its quantity, a teal guide to its price.
        dot_one = Dot(ax.c2p(FIRST_Q, demand(FIRST_Q)), radius=DOT_RADIUS, color=DEMAND).set_z_index(DOT_LAYER)
        dot_one.add_updater(lambda m: m.move_to(ax.c2p(q_one(), demand(q_one()))))
        drop_one = dashed(ax.c2p(FIRST_Q, 0), ax.c2p(FIRST_Q, demand(FIRST_Q)), GUIDE).set_z_index(GUIDE_LAYER)
        drop_one.add_updater(lambda m: m.become(dashed(ax.c2p(q_one(), 0), ax.c2p(q_one(), demand(q_one())), GUIDE))
                             .set_z_index(GUIDE_LAYER))
        across_one = dashed(ax.c2p(0, demand(FIRST_Q)), ax.c2p(FIRST_Q, demand(FIRST_Q)), DEMAND).set_z_index(GUIDE_LAYER)
        across_one.add_updater(lambda m: m.become(dashed(ax.c2p(0, demand(q_one())), ax.c2p(q_one(), demand(q_one())), DEMAND))
                               .set_z_index(GUIDE_LAYER))
        dot_two = dot_one.copy().clear_updaters()
        dot_two.add_updater(lambda m: m.move_to(ax.c2p(q_two(), demand(q_two()))))
        drop_two = drop_one.copy().clear_updaters()
        drop_two.add_updater(lambda m: m.become(dashed(ax.c2p(q_two(), 0), ax.c2p(q_two(), demand(q_two())), GUIDE))
                             .set_z_index(GUIDE_LAYER))
        across_two = across_one.copy().clear_updaters()
        across_two.add_updater(lambda m: m.become(dashed(ax.c2p(0, demand(q_two())), ax.c2p(q_two(), demand(q_two())), DEMAND))
                               .set_z_index(GUIDE_LAYER))
        # Readouts: prices on the price axis (the second nudged down when the two are close), quantities as two rows.
        price_gap = lambda: ax.c2p(0, demand(q_one()))[1] - ax.c2p(0, demand(q_two()))[1]
        price_one = VGroup(MathTex('P_1=', color=DEMAND), DecimalNumber(100, num_decimal_places=0, color=DEMAND)).scale(PRICE_SCALE)
        price_one.add_updater(lambda m: (m[1].set_value(round(demand(q_one()), 4)), m.arrange(RIGHT, buff=0.1),
                                         m.next_to(ax.c2p(0, demand(q_one())), LEFT, buff=0.2)))
        price_two = VGroup(MathTex('P_2=', color=DEMAND), DecimalNumber(100, num_decimal_places=0, color=DEMAND)).scale(PRICE_SCALE)
        price_two.add_updater(lambda m: (m[1].set_value(round(demand(q_two()), 4)), m.arrange(RIGHT, buff=0.1),
                                         m.next_to(ax.c2p(0, demand(q_two())), LEFT, buff=0.2)
                                         .shift(DOWN * max(0, 0.36 - price_gap()))))
        quantity_one = VGroup(DecimalNumber(FIRST_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE),
                              MathTex('Q_1', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        # The two quantity rows step apart (by at most 0.08 each) when the drops are too close for both.
        quantity_nudge = lambda: max(0, 0.5 - (ax.c2p(q_two(), 0)[0] - ax.c2p(q_one(), 0)[0])) / 2 * min(1, step_q.get_value() / STEP_Q)
        quantity_one.add_updater(lambda m: (m[0].set_value(round(q_one(), 4)).move_to(ax.c2p(q_one(), 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                                            m[1].move_to(ax.c2p(q_one(), 0) + DOWN * QUANTITY_LABEL_OFFSET),
                                            m.shift(LEFT * quantity_nudge())))
        quantity_two = VGroup(DecimalNumber(FIRST_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE),
                              MathTex('Q_2', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        quantity_two.add_updater(lambda m: (m[0].set_value(round(q_two(), 4)).move_to(ax.c2p(q_two(), 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                                            m[1].move_to(ax.c2p(q_two(), 0) + DOWN * QUANTITY_LABEL_OFFSET),
                                            m.shift(RIGHT * quantity_nudge())))
        point_one = [dot_one, drop_one, across_one, price_one, quantity_one]
        for m in point_one:
            m.update()
        tr_one_row.move_to(revenue_slots[3], aligned_edge=LEFT)
        tr_one_row.get_part_by_tex(r'\mathrm{TR}_1').set_color(DEMAND)
        self.remove(note)
        note = teaching("Here we're going from a quantity of 20 to a quantity of 30.")
        self.play(GrowFromCenter(dot_one), Create(drop_one), Create(across_one), FadeIn(price_one), FadeIn(quantity_one))
        self.play(LaggedStart(*[FadeIn(strip) for strip in revenue_common], lag_ratio=0.1),
                  FadeIn(tr_one_row), FadeIn(note), run_time=1.6)
        self.remove(*revenue_common)
        self.add(*revenue_strips)
        self.pause('2.b.first')

        # ---- 2.b.second · The second point rides demand from 20 to 30: the price falls from 100 to 90.
        tr_two_row.move_to(revenue_slots[4], aligned_edge=LEFT)
        tr_two_row.get_part_by_tex(r'\mathrm{TR}_2').set_color(DEMAND)
        for m in (dot_two, drop_two, across_two):
            m.update()
        self.add(dot_two, drop_two, across_two)
        self.remove(note)
        self.play(step_q.animate.set_value(STEP_Q), run_time=ROLL_TIME, rate_func=smooth)
        for m in (price_two, quantity_two):
            m.update()                       # Digits must already match before a number fades in.
        note = teaching('So we see the price go down, but the quantity go up.')
        self.play(FadeIn(price_two), FadeIn(quantity_two), FadeIn(tr_two_row), FadeIn(note))
        self.pause('2.b.second')

        # ---- 2.b.split · The change in revenue: the new units at the new price, less the price cut on the old ones.
        change_row.move_to(revenue_slots[5], aligned_edge=LEFT)
        self.remove(note)
        note = teaching('So these two factors are moving in opposite directions.')
        self.play(FadeIn(change_row), Indicate(revenue_loss, color=FOCUS, scale_factor=1.0), FadeIn(note))
        self.pause('2.b.split')

        # ---- 2.b · MR for this step: 700 over 10 units, a pink dot halfway between the two quantities.
        arc_mr = lambda: (marginal_revenue(q_one() + step_q.get_value() / 2))
        mr_dot = Dot(ax.c2p(25, 70), radius=DOT_RADIUS, color=MR_COLOR).set_z_index(DOT_LAYER)
        mr_dot.add_updater(lambda m: m.move_to(ax.c2p(q_one() + step_q.get_value() / 2, arc_mr())))
        mr_value_row.move_to(revenue_slots[6], aligned_edge=LEFT)
        self.remove(note)
        note = teaching('Monopolists are the only seller in the market, so they control the price.')
        self.play(FadeIn(mr_value_row), GrowFromCenter(mr_dot), FadeIn(note))
        self.pause('2.b')

        # ---- 2.c.trace · One sweep moves the pair along demand; the MR dot traces the marginal revenue curve.
        mr_trace = Line(ax.c2p(25, 70), ax.c2p(25, 70) + RIGHT * 1e-4, color=MR_COLOR, stroke_width=CURVE_WIDTH)
        mr_trace.set_z_index(CURVE_LAYER)
        mr_trace.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(25, 70), ax.c2p(q_one() + STEP_Q / 2, arc_mr()) + RIGHT * 1e-4))
        for m in (price_one, price_two, quantity_one, quantity_two):
            m.clear_updaters()
        self.remove(note)
        self.play(FadeOut(price_one), FadeOut(price_two), FadeOut(quantity_one), FadeOut(quantity_two),
                  FadeOut(tr_one_row), FadeOut(tr_two_row), FadeOut(change_row), FadeOut(mr_value_row), run_time=0.6)
        self.add(mr_trace)
        self.play(first_q.animate.set_value(LAST_Q), run_time=SWEEP_TIME, rate_func=smooth)
        note = teaching('Using this equation gives us the value for the marginal revenue curve.')
        self.play(FadeIn(note))
        self.pause('2.c.trace')

        # ---- 2.c · The whole MR curve: from demand's start at 120 down to zero at 60 units, half of demand's 120.
        mr_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2 * BASE_ALPHA, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        mr_word = Tex('MR', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(TOP_PRICE / 2 * BASE_ALPHA, 0), UR, buff=0.12)
        mr_row.move_to(revenue_slots[1], aligned_edge=LEFT)
        window = [dot_one, drop_one, across_one, dot_two, drop_two, across_two, mr_dot, *revenue_strips]
        for m in window + [mr_trace]:
            m.clear_updaters()
        self.remove(note)
        note = teaching('MR starts with demand at 120 and falls twice as fast.')
        self.play(*[FadeOut(m) for m in window], FadeIn(mr_line), FadeIn(mr_word), FadeIn(mr_row), run_time=1.2)
        self.remove(mr_trace)
        self.play(FadeIn(note))
        self.pause('2.c')

        # ---- 3.a · The monopolist's problem: the firm's card in the panel; step 1, MR = MC, gives q* = 30.
        # From here one set of trackers drives every mark: demand (alpha, the old code's demand share), the
        # per-unit tax, the subsidy, the lump-sum tax, and an offset from the best quantity (3.e).
        alpha, tax, subsidy, lump, offset = [ValueTracker(v) for v in (BASE_ALPHA, 0, 0, 0, 0)]
        rise = ValueTracker(0)                           # 3.b: the quantity guide rises from MR = MC to demand
        best_q = lambda: alpha.get_value() * (TOP_PRICE - tax.get_value() + subsidy.get_value()) / (2 * alpha.get_value() + 2)
        chosen_q = lambda: best_q() + offset.get_value()
        price_now = lambda: demand(chosen_q(), alpha.get_value())
        cost_shift = lambda q: tax.get_value() - subsidy.get_value() + lump.get_value() / q
        policy_mc = lambda q: mc(q) + tax.get_value() - subsidy.get_value()
        policy_atc = lambda q: atc(q) + cost_shift(q)
        profit_now = lambda: (price_now() - policy_atc(chosen_q())) * chosen_q()
        efficient_q = lambda: TOP_PRICE * alpha.get_value() / (2 * alpha.get_value() + 1)
        guide_top = lambda: policy_mc(best_q()) + rise.get_value() * (price_now() - policy_mc(best_q()))

        self.remove(head, note)
        head = title("The Monopolist's Problem")
        objective = MathTex(r'\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}')
        step_one = MathTex(r'1.\enspace {{\mathrm{MC}}} = {{\mathrm{MR}}} \rightarrow q^*')
        step_one.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        step_one.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        step_two = MathTex(r'2.\enspace q^* \rightarrow {{\mathrm{D}}} \rightarrow P^*')
        step_two.get_part_by_tex(r'\mathrm{D}').set_color(DEMAND)
        step_three = MathTex(r'3.\enspace q^* \rightarrow {{\mathrm{ATC}}} \rightarrow \mathrm{ATC}^*')
        step_three.get_part_by_tex(r'\mathrm{ATC}').set_color(ATC_COLOR)
        step_four = MathTex(r'4.\enspace \pi^* = (P^* - \mathrm{ATC}^*)\cdot q^*')
        work_one = MathTex(r'{{2q}} = {{120 - 2q}}, \text{ so } {{q^* = 30}}')
        work_one.get_part_by_tex('2q').set_color(MC_COLOR)
        work_one.get_part_by_tex('120 - 2q').set_color(MR_COLOR)
        work_one.get_part_by_tex('q^* = 30').set_color(GUIDE)
        work_two = MathTex(r'P^* = 120 - 30 = {{90}}')
        work_two.get_part_by_tex('90').set_color(DEMAND)
        work_three = MathTex(r'\mathrm{ATC}^* = 30 + 1000/30 = {{63.33}}')
        work_three.get_part_by_tex('63.33').set_color(ATC_COLOR)
        work_four = MathTex(r'\pi^* = (90 - 63.33)\cdot 30 = {{800}}')
        work_four.get_part_by_tex('800').set_color(SUPPLY)
        card = VGroup(objective, step_one, work_one, step_two, work_two, step_three, work_three, step_four, work_four)
        card.scale(ROW_SCALE).arrange(DOWN, buff=ROW_GAP, aligned_edge=LEFT)
        for work in (work_one, work_two, work_three, work_four):
            work.shift(RIGHT * WORK_INDENT)
        # A little more room under the objective and between the step pairs.
        VGroup(*card[1:]).shift(DOWN * 0.12)
        for k in (3, 5, 7):
            VGroup(*card[k:]).shift(DOWN * PAIR_GAP / 2)
        card.move_to([PANEL_LEFT, BODY_MID, 0], aligned_edge=LEFT)
        # The answer marks: a red dot where MR meets (policy) MC, its drop, and the two-row quantity readout.
        choice_dot = Dot(ax.c2p(30, 60), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        choice_dot.add_updater(lambda m: m.move_to(ax.c2p(best_q(), policy_mc(best_q()))))
        quantity_guide = dashed(ax.c2p(30, 0), ax.c2p(30, 60), GUIDE).set_z_index(GUIDE_LAYER)
        quantity_guide.add_updater(lambda m: m.become(dashed(ax.c2p(chosen_q(), 0), ax.c2p(chosen_q(), guide_top()), GUIDE))
                                   .set_z_index(GUIDE_LAYER))
        # The red quantity row steps aside where the yellow efficient quantity sits (6.c).
        near_efficient = lambda: smooth(np.clip((abs(efficient_q() - chosen_q()) - 4) / 4, 0, 1))
        quantity_number = DecimalNumber(30, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        quantity_number.add_updater(lambda m: m.set_value(round(chosen_q(), 4))
                                    .move_to(ax.c2p(chosen_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        quantity_star = MathTex('q^*', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        quantity_star.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        quantity_free = MathTex('q', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        quantity_free.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        for m in (choice_dot, quantity_guide, quantity_number, quantity_star):
            m.update()
        note = teaching("To solve any firm's problem, set marginal cost equal to marginal revenue.")
        self.play(FadeIn(head), FadeOut(demand_row), FadeOut(mr_row), FadeOut(mr_definition),
                  FadeIn(objective), FadeIn(step_one), run_time=1.0)
        self.play(GrowFromCenter(choice_dot), FadeIn(work_one), FadeIn(note))
        self.play(Create(quantity_guide), FadeIn(quantity_number), FadeIn(quantity_star))
        self.pause('3.a')

        # ---- 3.b · Step 2: up from q* to demand; P* = 90, dashed in demand's color.
        price_dot = Dot(ax.c2p(30, 90), radius=DOT_RADIUS, color=DEMAND).set_z_index(DOT_LAYER)
        price_dot.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), price_now())))
        price_guide = dashed(ax.c2p(0, 90), ax.c2p(30, 90), DEMAND).set_z_index(GUIDE_LAYER)
        price_guide.add_updater(lambda m: m.become(dashed(ax.c2p(0, price_now()), ax.c2p(chosen_q(), price_now()), DEMAND))
                                .set_z_index(GUIDE_LAYER))
        price_number = DecimalNumber(90, num_decimal_places=2, color=DEMAND).scale(PRICE_SCALE)
        price_number.add_updater(lambda m: m.set_value(price_now()).next_to(ax.c2p(0, price_now()), LEFT, buff=0.2))
        price_star = MathTex('P^*=', color=DEMAND).scale(PRICE_SCALE)
        price_star.add_updater(lambda m: m.next_to(price_number, LEFT, buff=0.08))
        price_free = MathTex('P=', color=DEMAND).scale(PRICE_SCALE)
        price_free.add_updater(lambda m: m.next_to(price_number, LEFT, buff=0.08))
        for m in (price_dot, price_guide, price_number, price_star):
            m.update()
        self.remove(note)
        note = teaching('Using quantity with the demand curve allows us to find price.')
        self.play(FadeIn(step_two), FadeIn(note))
        self.play(rise.animate.set_value(1), run_time=0.8)
        self.play(GrowFromCenter(price_dot), Create(price_guide), FadeIn(price_number), FadeIn(price_star), FadeIn(work_two))
        self.pause('3.b')

        # ---- 3.c · Step 3: q* meets ATC; ATC* = 63.33, dashed in ATC's color (kept clear of P* when the two are close).
        atc_y = lambda: min(ax.c2p(0, policy_atc(chosen_q()))[1], ax.c2p(0, price_now())[1] - 0.34)
        atc_dot = Dot(ax.c2p(30, atc(30)), radius=DOT_RADIUS, color=ATC_COLOR).set_z_index(DOT_LAYER)
        atc_dot.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), policy_atc(chosen_q()))))
        atc_guide = dashed(ax.c2p(0, atc(30)), ax.c2p(30, atc(30)), ATC_COLOR).set_z_index(GUIDE_LAYER)
        atc_guide.add_updater(lambda m: m.become(dashed(ax.c2p(0, policy_atc(chosen_q())),
                                                        ax.c2p(chosen_q(), policy_atc(chosen_q())), ATC_COLOR))
                              .set_z_index(GUIDE_LAYER))
        atc_number = DecimalNumber(atc(30), num_decimal_places=2, color=ATC_COLOR).scale(PRICE_SCALE)
        atc_number.add_updater(lambda m: m.set_value(policy_atc(chosen_q())).next_to(ax.c2p(0, 0), LEFT, buff=0.2).set_y(atc_y()))
        atc_star = MathTex(r'\mathrm{ATC}^*=', color=ATC_COLOR).scale(PRICE_SCALE)
        atc_star.add_updater(lambda m: m.next_to(atc_number, LEFT, buff=0.08))
        atc_free = MathTex(r'\mathrm{ATC}=', color=ATC_COLOR).scale(PRICE_SCALE)
        atc_free.add_updater(lambda m: m.next_to(atc_number, LEFT, buff=0.08))
        for m in (atc_dot, atc_guide, atc_number, atc_star):
            m.update()
        self.remove(note)
        note = teaching('Quantity with the average total cost curve gives the average total cost.')
        self.play(FadeIn(step_three), FadeIn(note))
        self.play(GrowFromCenter(atc_dot), Create(atc_guide), FadeIn(atc_number), FadeIn(atc_star), FadeIn(work_three))
        self.pause('3.c')

        # ---- 3.d · Step 4: profit, (90 - 63.33) x 30 = 800, as one-unit strips between ATC* and P*.
        profit_strips = strip_group(80, SUPPLY, PROFIT_OPACITY, FILL_LAYER)
        profit_strips.span = lambda: (0, chosen_q())
        profit_strips.low, profit_strips.high = (lambda x: policy_atc(chosen_q())), (lambda x: price_now())
        profit_strips.add_updater(follow_strips)
        profit_strips.update()
        # Area names sit on the part of their area that shows (a subsidy's green band lies inside the profit) and
        # carry a thin background-colored halo, since MR, MC and ATC all cross the profit rectangle.
        profit_floor = lambda: max(policy_atc(chosen_q()), atc(chosen_q()))
        profit_height = lambda: ax.c2p(0, price_now())[1] - ax.c2p(0, profit_floor())[1]
        profit_word = Tex('Profit', color=INK).scale(AREA_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        profit_word.natural_height = profit_word.get_height()
        profit_word.add_updater(lambda m: m.set_height(max(0.01, min(m.natural_height, 0.7 * profit_height())))
                                .move_to(ax.c2p(chosen_q() / 2, (price_now() + profit_floor()) / 2))
                                .set_opacity(np.clip((profit_height() - 0.12) / 0.1, 0, 1)))
        profit_word.update()
        self.remove(note)
        note = teaching("Price, average total cost and quantity give us the firm's profits.")
        self.play(FadeIn(step_four), FadeIn(note))
        self.play(LaggedStart(*[FadeIn(strip) for strip in profit_strips], lag_ratio=0.1), run_time=2)
        self.remove(*profit_strips)
        self.add(profit_strips)
        self.play(FadeIn(profit_word), FadeIn(work_four))
        self.pause('3.d')

        # ---- 3.e.sixty · Check the answer: one tracker moves the quantity to 40; profit falls to 600.
        # (The beat names 3.e.sixty and 3.e.forty are kept from the old model, where the quantities were 60 and 40;
        # they are now 40 and 20.)
        # The live profit row: (P - ATC) x q = profit, every number rolling with the trackers, at the anchor where
        # step 4's worked row was (the anchor moves when section 4 closes up the card).
        profit_anchor = VectorizedPoint(work_four.get_left())


        def profit_row(prefix, quantity_places=0):
            row = VGroup(MathTex(prefix), DecimalNumber(90, num_decimal_places=2, color=DEMAND), MathTex('-'),
                         DecimalNumber(atc(30), num_decimal_places=2, color=ATC_COLOR), MathTex(r')\hspace{2.5pt}\cdot'),
                         DecimalNumber(30, num_decimal_places=quantity_places, color=GUIDE), MathTex('='),
                         DecimalNumber(800, num_decimal_places=0, color=SUPPLY)).scale(ROW_SCALE)
            row.add_updater(lambda m: (m[1].set_value(price_now()), m[3].set_value(policy_atc(chosen_q())),
                                       m[5].set_value(round(chosen_q(), 4)), m[7].set_value(round(profit_now(), 4)),
                                       [m[k + 1].next_to(m[k], RIGHT, buff=ROW_GAPS[k]) for k in range(7)],
                                       m.move_to(profit_anchor.get_center(), aligned_edge=LEFT)))
            return row
        live_profit_free = profit_row(r'\pi = (')
        live_profit = profit_row(r'\pi^* = (')
        moving = [quantity_guide, quantity_number, quantity_free, price_dot, price_guide, price_number, price_free,
                  atc_dot, atc_guide, atc_number, atc_free, profit_strips, profit_word, live_profit_free]
        for m in moving:
            m.update()
        self.remove(note, quantity_star, price_star, atc_star, work_four)
        self.add(quantity_free, price_free, atc_free, live_profit_free)
        self.play(offset.animate.set_value(10), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('If we increase the quantity to 40, their profit goes down.')
        self.play(FadeIn(note))
        self.pause('3.e.sixty')

        # ---- 3.e.forty · Then to 20: profit is 600 again.
        self.remove(note)
        self.play(offset.animate.set_value(-10), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('If we lower the quantity to 20, their profit also goes down.')
        self.play(FadeIn(note))
        self.pause('3.e.forty')

        # ---- 3.e · Back to 30, where MR = MC: the highest profit, 800.
        self.remove(note)
        self.play(offset.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        live_profit.update()
        self.remove(quantity_free, price_free, atc_free, live_profit_free)
        self.add(quantity_star, price_star, atc_star, live_profit)
        note = teaching("MC = MR solves the firm's profit maximization problem.")
        self.play(FadeIn(note))
        self.pause('3.e')

        # ---- 4.a · Demand shifts down (the demand share alpha, 1 to 1/2: P = 120 - 2Q): D and MR pivot down from 120,
        # and q*, P*, ATC* and profit roll to 20, 80, 70 and 200. A grey ghost keeps the old demand.
        demand_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * alpha.get_value(), 0)))
        demand_word.add_updater(lambda m: m.next_to(demand_word_at(alpha.get_value()), UR, buff=0.1))
        mr_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2 * alpha.get_value(), 0)))
        mr_word.add_updater(lambda m: m.next_to(ax.c2p(TOP_PRICE / 2 * alpha.get_value(), 0), UR, buff=0.12))
        ghost_demand = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * BASE_ALPHA, 0), color=MUTED, stroke_width=2).set_opacity(0.55).set_z_index(-1)
        self.remove(head, note)
        head = title('Changes In Demand')
        # The card closes up: the worked rows for 30 leave and the four steps and the live profit row move together.
        compact = VGroup(objective.copy(), step_one.copy(), step_two.copy(), step_three.copy(), step_four.copy(),
                         work_four.copy()).arrange(DOWN, buff=ROW_GAP + 0.16, aligned_edge=LEFT)
        compact[1:].shift(DOWN * 0.12)
        compact[5].shift(RIGHT * WORK_INDENT)
        compact.move_to(card.get_corner(UL), aligned_edge=UL)
        self.play(FadeIn(head), FadeOut(work_one), FadeOut(work_two), FadeOut(work_three),
                  *[row.animate.move_to(target) for row, target in zip((objective, step_one, step_two, step_three, step_four),
                                                                       compact[:5])],
                  profit_anchor.animate.move_to(compact[5].get_left()))
        self.add(ghost_demand)
        self.play(alpha.animate.set_value(LOW_ALPHA), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching("When demand shifts down, the firm's quantity and profit go down.")
        self.play(FadeIn(note))
        self.pause('4.a')

        # ---- 5.a.efficient · Demand returns; the socially efficient quantity, where MC meets demand, in yellow.
        self.remove(note)
        self.play(alpha.animate.set_value(BASE_ALPHA), FadeOut(ghost_demand), run_time=ROLL_TIME, rate_func=smooth)
        self.remove(head)
        head = title('Deadweight Loss')
        efficient_dot = Dot(ax.c2p(40, 80), radius=FOCUS_RADIUS, color=FOCUS).set_z_index(DOT_LAYER - 1)
        efficient_drop = dashed(ax.c2p(40, 0), ax.c2p(40, 80), FOCUS).set_z_index(GUIDE_LAYER - 1)
        efficient_words = VGroup(
            Tex('40', color=FOCUS).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            MathTex('Q_{sp}', color=FOCUS).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        note = teaching('The socially efficient quantity: where the MC and MB curves intersect.')
        self.play(FadeIn(head), FadeIn(note))
        self.play(GrowFromCenter(efficient_dot), Create(efficient_drop), FadeIn(efficient_words))
        self.pause('5.a.efficient')

        # ---- 5.a · The grey deadweight loss: every unit from q* to Q_sp, from MC up to demand.
        dwl_strips = strip_group(70, DWL, DWL_STRIP_OPACITY, FILL_LAYER)
        dwl_strips.span = lambda: (chosen_q(), efficient_q())
        dwl_strips.low, dwl_strips.high = mc, (lambda x: demand(x, alpha.get_value()))
        dwl_strips.add_updater(follow_strips)
        dwl_strips.update()
        dwl_width = lambda: efficient_q() - chosen_q()
        dwl_word = Tex('DWL', color=INK).scale(AREA_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        # The name sits above a narrow triangle and moves inside it (to its centroid) once it is wide enough (6.a).
        dwl_above = lambda: np.array([chosen_q() + 0.6 * dwl_width(), demand(chosen_q() + 0.6 * dwl_width()) + 13])
        dwl_inside = lambda: np.array([(2 * chosen_q() + efficient_q()) / 3,
                                       (demand(chosen_q()) + mc(chosen_q()) + demand(efficient_q())) / 3])
        dwl_fit = lambda: smooth(np.clip((dwl_width() - 10) / 6, 0, 1))
        dwl_word.add_updater(lambda m: m.move_to(ax.c2p(*((1 - dwl_fit()) * dwl_above() + dwl_fit() * dwl_inside())))
                             .set_opacity(np.clip((dwl_width() - 3) / 4, 0, 1)))
        dwl_word.update()
        self.remove(note)
        note = teaching('Deadweight loss: the quantity not provided where MB exceeds MC.')
        self.play(LaggedStart(*[FadeIn(dwl_strips[k]) for k in range(30, 40)], lag_ratio=0.18), FadeIn(note), run_time=1.6)
        self.remove(*dwl_strips)
        self.add(dwl_strips)
        self.play(FadeIn(dwl_word))
        self.pause('5.a')

        # ---- 6.a.shift · A per-unit tax shifts MC and ATC up by the tax (dashed copies); q* falls, P* rises.
        policy_mc_line = dashed(ax.c2p(0, 0), ax.c2p(POLICY_TOP / 2, POLICY_TOP), MC_COLOR).set_stroke(width=CURVE_WIDTH).set_z_index(POLICY_LAYER)
        policy_mc_end = lambda: (POLICY_TOP - tax.get_value() + subsidy.get_value()) / 2   # where policy MC reaches the top
        policy_mc_line.add_updater(lambda m: m.become(DashedLine(
            ax.c2p(max(0, subsidy.get_value() - tax.get_value()) / 2, max(0, tax.get_value() - subsidy.get_value())),
            ax.c2p(policy_mc_end(), POLICY_TOP), color=MC_COLOR, stroke_width=CURVE_WIDTH))
            .set_z_index(POLICY_LAYER).set_opacity(np.clip(abs(tax.get_value() - subsidy.get_value()) / 3, 0, 1)))
        policy_atc_from = lambda: min([q for q in np.linspace(5, ATC_TO, 400) if policy_atc(q) <= POLICY_TOP])
        # Seeded with a real dashed ATC: an empty VMobject would align to its target by copying itself, updater and all.
        policy_atc_curve = DashedVMobject(polyline([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, ATC_TO, 160)], ATC_COLOR,
                                                   CURVE_WIDTH), num_dashes=44).set_z_index(POLICY_LAYER)
        policy_atc_curve.add_updater(lambda m: m.become(DashedVMobject(
            polyline([ax.c2p(q, policy_atc(q)) for q in np.geomspace(policy_atc_from(), ATC_TO, 160)], ATC_COLOR, CURVE_WIDTH),
            num_dashes=44)).set_z_index(POLICY_LAYER)
            .set_opacity(np.clip((tax.get_value() + subsidy.get_value() + lump.get_value() / 50) / 3, 0, 1)))
        # A policy ATC's name keeps clear of ATC's own name: above it when the dashed curve ends above ATC, else below.
        name_room = lambda m: (m.get_height() + atc_word.get_height()) / 2 + getattr(m, 'room', 0.14)
        policy_name_y = lambda m: (max(ax.c2p(ATC_TO, policy_atc(ATC_TO))[1], atc_word.get_y() + name_room(m))
                                   if policy_atc(ATC_TO) >= atc(ATC_TO) else
                                   min(ax.c2p(ATC_TO, policy_atc(ATC_TO))[1], atc_word.get_y() - name_room(m)))
        mc_tax_word = Tex(r'MC $+$ tax', color=INK).scale(CURVE_WORD_SCALE)
        mc_tax_word.add_updater(lambda m: m.next_to(ax.c2p(policy_mc_end(), POLICY_TOP), RIGHT, buff=0.15)
                                .set_opacity(np.clip((tax.get_value() - 4) / 4, 0, 1)))
        atc_tax_word = Tex(r'ATC $+$ tax', color=INK).scale(CURVE_WORD_SCALE)
        atc_tax_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                                 .set_opacity(np.clip((tax.get_value() - 4) / 4, 0, 1)))
        # The government's band: between the firm's true ATC and its ATC under the policy, over the q* units.
        gov_strips = strip_group(80, GOV, GOV_OPACITY, GOV_LAYER)
        gov_strips.span = lambda: (0, chosen_q())
        gov_strips.low = lambda x: min(atc(chosen_q()), policy_atc(chosen_q()))
        gov_strips.high = lambda x: max(atc(chosen_q()), policy_atc(chosen_q()))
        gov_strips.add_updater(follow_strips)
        gov_height = lambda: abs(ax.c2p(0, policy_atc(chosen_q()))[1] - ax.c2p(0, atc(chosen_q()))[1])
        gov_word = Tex('GOV', color=INK).scale(AREA_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        gov_word.natural_height = gov_word.get_height()
        gov_word.add_updater(lambda m: m.set_height(max(0.01, min(m.natural_height, 0.7 * gov_height())))
                             .move_to(ax.c2p(chosen_q() / 2, (atc(chosen_q()) + policy_atc(chosen_q())) / 2))
                             .set_opacity(np.clip((gov_height() - 0.12) / 0.1, 0, 1)))
        # The policy rows under the profit row: each policy's size rolls with its tracker.
        policy_left = profit_anchor.get_center() + DOWN * 0.75
        tax_row = VGroup(Tex(r'Tax per unit $=$ \$', color=GOV), DecimalNumber(0, num_decimal_places=0, color=GOV)).scale(ROW_SCALE)
        tax_row.add_updater(lambda m: (m[1].set_value(round(tax.get_value(), 4)), m.arrange(RIGHT, buff=POLICY_GAP),
                                       m.move_to(policy_left, aligned_edge=LEFT)))
        lump_row = VGroup(Tex(r'Lump-sum tax $=$ \$', color=GOV), DecimalNumber(0, num_decimal_places=0, color=GOV)).scale(ROW_SCALE)
        lump_row.add_updater(lambda m: (m[1].set_value(round(lump.get_value(), 4)), m.arrange(RIGHT, buff=POLICY_GAP),
                                        m.move_to(policy_left, aligned_edge=LEFT)))
        subsidy_row = VGroup(Tex(r'Subsidy per unit $=$ \$', color=GOV), DecimalNumber(0, num_decimal_places=0, color=GOV)).scale(ROW_SCALE)
        subsidy_row.add_updater(lambda m: (m[1].set_value(round(subsidy.get_value(), 4)), m.arrange(RIGHT, buff=POLICY_GAP),
                                           m.move_to(policy_left, aligned_edge=LEFT)))
        policy_marks = [policy_mc_line, policy_atc_curve, mc_tax_word, atc_tax_word, gov_strips, gov_word, tax_row]
        for m in policy_marks:
            m.update()
        self.remove(head, note)
        head = title('A Per-Unit Tax')
        note = teaching('We shift marginal cost and average total cost up by the tax.')
        self.add(policy_mc_line, policy_atc_curve, mc_tax_word, atc_tax_word, gov_strips)
        self.play(FadeIn(head), FadeIn(tax_row), FadeIn(note))
        self.play(tax.animate.set_value(TAX), run_time=ROLL_TIME + 0.8, rate_func=smooth)
        self.pause('6.a.shift')

        # ---- 6.a · The band between ATC and ATC + tax is the government's revenue; DWL has grown.
        self.remove(note)
        note = teaching('As the tax goes up, quantity goes down and deadweight loss goes up.')
        self.play(FadeIn(gov_word), FadeIn(note))
        self.pause('6.a')

        # ---- 6.b.shift · The tax comes off; a lump-sum tax of 500 is a fixed cost: only ATC shifts, q* stays 30.
        lump_word = Tex(r'ATC $+$ lump sum', color=INK).scale(CURVE_WORD_SCALE)
        lump_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                              .set_opacity(np.clip((lump.get_value() - 150) / 150, 0, 1)))
        self.remove(note)
        self.play(FadeOut(gov_word), run_time=0.4)
        self.play(tax.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        lump_row.update()
        lump_word.update()
        self.remove(head, tax_row, mc_tax_word, atc_tax_word)
        head = title('A Lump-Sum Tax')
        note = teaching('A lump-sum tax shifts only the average total cost.')
        self.add(lump_word)
        self.play(FadeIn(head), FadeIn(lump_row), FadeIn(note))
        self.play(lump.animate.set_value(LUMP_SUM), run_time=ROLL_TIME + 0.8, rate_func=smooth)
        self.pause('6.b.shift')

        # ---- 6.b · The band is the government's: the lump sum moves profit to the government.
        self.remove(note)
        note = teaching("This transfers some of the firm's profits to the government.")
        self.play(FadeIn(gov_word), FadeIn(note))
        self.pause('6.b')

        # ---- 6.c.shift · The lump sum comes off; a per-unit subsidy shifts MC and ATC down until q* reaches Q_sp.
        mc_subsidy_word = Tex(r'MC $-$ subsidy', color=INK).scale(CURVE_WORD_SCALE)
        mc_subsidy_word.add_updater(lambda m: m.next_to(ax.c2p(policy_mc_end(), POLICY_TOP), RIGHT, buff=0.15)
                                    .set_opacity(np.clip((subsidy.get_value() - 6) / 6, 0, 1)))
        atc_subsidy_word = Tex(r'ATC $-$ subsidy', color=INK).scale(CURVE_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        # It hands over to the two-line name once 6.d's lump sum starts. Demand runs behind both names, so they
        # carry the area names' halo.
        atc_subsidy_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                                     .set_opacity(np.clip((subsidy.get_value() - 6) / 6, 0, 1)
                                                  * (1 - np.clip((lump.get_value() - 100) / 200, 0, 1))))
        quantity_number.add_updater(lambda m: m.set_opacity(near_efficient()))
        quantity_star.add_updater(lambda m: m.set_opacity(near_efficient()))
        self.remove(note)
        self.play(FadeOut(gov_word), run_time=0.4)
        self.play(lump.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        subsidy_row.update()
        for m in (mc_subsidy_word, atc_subsidy_word):
            m.update()
        self.remove(head, lump_row, lump_word)
        head = title('A Per-Unit Subsidy')
        note = teaching('Subsidies tend to increase the quantity exchanged in the market.')
        self.add(mc_subsidy_word, atc_subsidy_word)
        self.play(FadeIn(head), FadeIn(subsidy_row), FadeIn(note))
        self.play(subsidy.animate.set_value(SUBSIDY), run_time=ROLL_TIME + 0.8, rate_func=smooth)
        self.remove(note)
        note = teaching('Quantity reaches the socially efficient quantity: zero deadweight loss.')
        self.play(FadeIn(note))
        self.pause('6.c.shift')

        # ---- 6.c · The band below ATC is what the government pays: a negative government revenue.
        self.remove(note)
        note = teaching('The green area represents a negative government revenue.')
        self.play(FadeIn(gov_word), FadeIn(note))
        self.pause('6.c')

        # ---- 6.d · Keep the subsidy and add a lump-sum tax of 1,800: profit shrinks and the band turns positive.
        both_word = Tex(r'ATC $-$ subsidy\\$+$ lump sum', color=INK).scale(CURVE_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        both_word.room = 0.3                 # two lines under ATC's name: more room so they don't read as one stack
        both_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                              .set_opacity(np.clip((lump.get_value() - 300) / 300, 0, 1)))
        both_lump_row = lump_row.copy().clear_updaters()
        both_lump_row.add_updater(lambda m: (m[1].set_value(round(lump.get_value(), 4)), m.arrange(RIGHT, buff=POLICY_GAP),
                                             m.move_to(policy_left + DOWN * 0.45, aligned_edge=LEFT)))
        both_lump_row.update()
        both_word.update()
        self.remove(head, note)
        head = title('A Subsidy And A Lump-Sum Tax')
        self.add(both_word)
        self.play(FadeIn(head), FadeIn(both_lump_row))
        self.play(lump.animate.set_value(LUMP_WITH_SUBSIDY), run_time=ROLL_TIME + 1.2, rate_func=smooth)
        note = teaching('No deadweight loss, positive government revenue, and less profit.')
        self.play(FadeIn(note))
        self.pause('6.d')

        # ---- 7.a · Next time: the taxonomy again, the box moving from Monopoly to the few-sellers cell (E4 opens there).
        for m in self.mobjects:
            m.update()                       # Digits current, then everything freezes before it fades.
            m.clear_updaters()
        self.remove(note)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        self.clear()
        head = title('Next Time')
        box = SurroundingRectangle(monopoly, buff=0.22, color=NASH)
        note = teaching('What happens with two sellers?')
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(box))
        self.play(Transform(box, SurroundingRectangle(oligopoly, buff=0.22, color=NASH)), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('7.a')
