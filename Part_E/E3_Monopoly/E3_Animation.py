# maniml E3_Animation.py EpisodeE3
# Storyboard: E3_Notes.md. All lesson choreography stays in construct().
# Monopoly: TC = 1200 + q^2, MC = 2q, ATC = q + 1200/q. E3 uses a higher fixed cost for a whole-number ATC readout.
# Demand P = 120 - Q, MR = 120 - 2Q. MR = MC at q* = 30, P* = 90, ATC* = 70, profit 600; Q_sp = 40. (Until 2026-11-11 this
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
        BAR_GAP, BAR_OUTLINE = 0.08, 1.0
        SURPLUS_OPACITY, DWL_STRIP_OPACITY = 0.65, 0.8
        PROFIT_OPACITY, GOV_OPACITY = AREA_OPACITY, SURPLUS_OPACITY
        # Firm theory palette (shared_E.md).
        MC_COLOR, MR_COLOR, ATC_COLOR = SUPPLY, DEMAND, TOTAL
        PROFIT_COLOR = GREEN                            # E2's profit green; orange remains MC's color
        # Demand stays grey throughout; blue identifies marginal revenue.
        TR_COLOR, CONTEXT_CURVE_COLOR = CAPTION, MUTED
        # Top-level z order (the engine sorts top-level mobjects by z_index): fills under curves, the government's
        # band over profit, then curves, words, guides and dots. A group's set_z_index does not set its children's.
        FILL_LAYER, GOV_LAYER, CURVE_LAYER, POLICY_LAYER, WORD_LAYER, GUIDE_LAYER, DOT_LAYER = -3, -2, 0, 1, 6, 10, 30
        # Layout: the market graph on the left, 0 to 120 units: demand runs to its foot at 120 and MR to its foot
        # at 60, half of demand's; the side panel right of C2's grey divider.
        GRAPH_ORIGIN = np.array([-5.5, BODY_MID - 2.15, 0])
        X_LENGTH, Y_LENGTH, X_END, Y_TOP = 6.8, 4.6, 120, 140
        DIVIDER_X, PANEL_LEFT, WORK_INDENT = 2.45, 2.75, 0.25
        ROLL_TIME = 2.4
        # Curve ends: MC to (60, 120); ATC from its 118 level to q = 85; the dashed policy MC runs up to 134, above
        # MC's own name, and the dashed policy ATC stops there too.
        MC_END, ATC_TO, POLICY_TOP = 60, 85, 134
        # Taxonomy: three seller rows with horizontal separators and no header.
        LABEL_W, CELL_W, CELL_H, TAXONOMY_X = 2.9, 3.3, 1.25, 0.4
        BOX_BUFF = 0.12                          # keep each selection clear of the row separators
        # Exercise cards match E2: gold heading, muted setup, white indented questions on graphite.
        EXERCISE_SCALE, EXERCISE_HEADING_Y, EXERCISE_LEFT = 0.95, 2.95, 1.5
        EXERCISE_CONTEXT_SCALE, EXERCISE_CONTEXT_TOP = 0.84, 2.25
        EXERCISE_SETUP_GAP, EXERCISE_ITEM_INDENT = 0.65, 0.8
        EXERCISE_QUESTION_GAP, EXERCISE_MARKER_GAP = 0.22, 0.18

        # E3's fixed cost is 1,200; MC and demand stay unchanged. E1 and E2 keep their own fixed costs.
        FIXED_COST = 1200
        TOP_PRICE = 120                                 # demand's and MR's start on the price axis
        BASE_ALPHA = 1                                  # demand share: P = 120 - Q / alpha
        demand = lambda Q, a=BASE_ALPHA: TOP_PRICE - Q / a
        marginal_revenue = lambda Q, a=BASE_ALPHA: TOP_PRICE - 2 * Q / a
        mc = lambda q: 2 * q
        atc = lambda q: q + FIXED_COST / q
        ATC_FROM = 11.3                                 # ATC(11.3) is about 118, below demand's intercept
        FIRST_Q, SECOND_Q, STEP_Q = 1, 25, 1             # two one-unit comparisons, at distinct places on demand
        LOW_ALPHA = 5 / 7                               # section 4: P = 120 - 1.4Q; q* 25, P* 85, ATC* 73, profit 300
        TAX, LUMP_SUM, SUBSIDY, LUMP_WITH_SUBSIDY = 20, 500, 40, 1800    # whole-number outcomes; 40 reaches Q_sp

        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        dashed = lambda start, end, color: DashedLine(start, end + UP * 1e-4, color=color, stroke_width=GUIDE_WIDTH)

        # ---- 0.warmup · The exercise's one-price-for-everyone question, before the bumper.
        warmup_label = Tex(r'Exercise E3 \textbar{} Warmup', color=DEFINITION).scale(EXERCISE_SCALE)
        warmup_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        warmup_context = Tex(
            r'\begin{minipage}{32em}\sffamily\raggedright '
            r'You sell 20 units at \$100 each. To sell 30 units,\\'
            r'you must lower the price to \$90 on every unit.\end{minipage}', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        warmup_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        warmup_questions = VGroup(
            Tex('What is total revenue at 20 units? At 30 units?', color=INK),
            Tex(r'\begin{minipage}{27em}\raggedright '
                r'How much additional revenue do the 10 extra units\\'
                r'bring in, on average, per unit?\end{minipage}', color=INK),
            Tex(r'Why is your answer to b less than \$90?', color=INK),
        ).scale(EXERCISE_SCALE).arrange(DOWN, buff=EXERCISE_QUESTION_GAP, aligned_edge=LEFT)
        warmup_questions.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
            warmup_context.get_bottom()[1] - EXERCISE_SETUP_GAP, direction=UP)
        warmup_markers = VGroup(*[Tex(letter, color=INK).scale(EXERCISE_SCALE) for letter in ('a)', 'b)', 'c)')])
        for marker, question in zip(warmup_markers, warmup_questions):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP, aligned_edge=UP)
        warmup_text = VGroup(warmup_label, warmup_context, warmup_questions, warmup_markers)
        self.play(FadeIn(warmup_text), run_time=0.4)
        self.pause('0.warmup')
        self.play(FadeOut(warmup_text), run_time=0.4)

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

        # ---- 1.a.last · The three-row market-structures table, last episode's cell boxed.
        head = title('Monopoly')
        grid_left = TAXONOMY_X - (LABEL_W + CELL_W) / 2
        grid_right = grid_left + LABEL_W + CELL_W
        grid_top = BODY_MID + 3 * CELL_H / 2
        column_x = grid_left + LABEL_W + CELL_W / 2
        row_y = [grid_top - CELL_H * (i + 0.5) for i in range(3)]
        # Only the two separators between seller rows; no top, bottom, or vertical rules.
        taxonomy_rules = VGroup(
            *[Line([grid_left, grid_top - CELL_H * i, 0], [grid_right, grid_top - CELL_H * i, 0],
                   color=MUTED, stroke_width=2) for i in range(1, 3)])
        row_words = VGroup(Tex('Many Sellers', color=GUIDE), Tex('Few Sellers', color=GUIDE),
                           Tex('One Seller', color=GUIDE)).scale(0.75)
        for word, y in zip(row_words, row_y):
            word.move_to([grid_left + LABEL_W / 2, y, 0])
        perfect = Tex(r'Perfect\\Competition').scale(0.75).move_to([column_x, row_y[0], 0])
        oligopoly = Tex('Oligopoly').scale(0.75).move_to([column_x, row_y[1], 0])
        monopoly = Tex('Monopoly').scale(0.75).move_to([column_x, row_y[2], 0])
        taxonomy = VGroup(taxonomy_rules, row_words, perfect, oligopoly, monopoly)
        box = SurroundingRectangle(perfect, buff=BOX_BUFF, color=NASH)
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a.last')

        # ---- 1.a · The box moves to the one-seller cell: monopoly, defined in Taylor's words.
        note = teaching('A monopolist operates in a market with many buyers and one seller.')
        self.play(Transform(box, SurroundingRectangle(monopoly, buff=BOX_BUFF, color=NASH)), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('1.a')

        # ---- 1.b · Start with demand alone and the monopolist's quantity-and-price question.
        ax = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=X_LENGTH, y_length=Y_LENGTH)
        ax.shift(GRAPH_ORIGIN - ax.c2p(0, 0))
        axis_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, Y_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, Y_TOP), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(X_END, 0), DOWN, buff=0.23))
        # Mark 25 on the full graph, then carry that tick to the edge of the closer view.
        CLOSEUP_Q = 25
        graph_q_max = ValueTracker(X_END)
        plot_point = lambda q, p: ax.c2p(q * X_END / graph_q_max.get_value(), p)
        graph_extent = MathTex(str(CLOSEUP_Q), color=MUTED).scale(QUANTITY_NUMBER_SCALE)
        graph_extent.add_updater(lambda m: m.move_to(plot_point(CLOSEUP_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        graph_extent.update()
        # One subtitle from 1.b to 6.d: it stays in place while the titles change around it.
        context = subtitle(head, 'One seller, many buyers.')
        demand_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * BASE_ALPHA, 0), color=CONTEXT_CURVE_COLOR, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        demand_line.add_updater(lambda m: m.put_start_and_end_on(
            plot_point(0, TOP_PRICE), plot_point(graph_q_max.get_value(), demand(graph_q_max.get_value()))))
        # Demand's name rides just above its lower end, and rides with it when demand pivots (4.a).
        demand_word_at = lambda a=BASE_ALPHA: ax.c2p(0.78 * TOP_PRICE * a, demand(0.78 * TOP_PRICE * a, a))
        demand_word = Tex('D/MB', color=CONTEXT_CURVE_COLOR).scale(CURVE_WORD_SCALE).next_to(demand_word_at(), UR, buff=0.1)
        demand_start = Tex('$120$', color=TR_COLOR).scale(0.65).next_to(ax.c2p(0, TOP_PRICE), LEFT, buff=0.15)
        demand_row = MathTex(r'\mathrm{D}\colon P = 120 - Q', color=TR_COLOR).scale(ROW_SCALE)
        demand_row.move_to(ax.c2p(30, 126), aligned_edge=LEFT)
        self.remove(note)
        self.play(FadeOut(taxonomy), FadeOut(box), run_time=0.8)
        note = teaching('How much should we produce, and at what price?')
        self.play(FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(graph_extent), FadeIn(demand_line),
                  FadeIn(demand_row), FadeIn(demand_start), FadeIn(note))
        self.pause('1.b')

        # ---- 1.c · Choose one unit first; leave its price unanswered until the next hold.
        self.play(graph_q_max.animate.set_value(CLOSEUP_Q), axis_words[2].animate.shift(RIGHT * 0.55), run_time=1.8)
        first_q, step_q = ValueTracker(FIRST_Q), ValueTracker(0)
        q_one = lambda: first_q.get_value()
        q_two = lambda: first_q.get_value() + step_q.get_value()

        # Every area is one-unit strips. Pass current bounds through the updater so checkpoint replay
        # follows the restored trackers rather than callbacks stored on an older copy of the group.
        def strip_group(count, color, opacity, z):
            strips = VGroup(*[Polygon(plot_point(k, 0), plot_point(k + 0.5, 0), plot_point(k + 0.5, 1), plot_point(k, 1),
                                      color=color, stroke_width=BAR_OUTLINE, stroke_opacity=0, fill_color=color, fill_opacity=0).set_z_index(z)
                              for k in range(count)]).set_z_index(z)
            strips.opacity = opacity
            return strips

        def follow_strips(strips, start, end, low, high):
            for k, strip in enumerate(strips):
                left, right = max(k + BAR_GAP / 2, start), min(k + 1 - BAR_GAP / 2, end)
                low_left, low_right = low(left), low(right)
                high_left, high_right = high(left), high(right)
                if right - left < 1e-3 or max(high_left - low_left, high_right - low_right) < 1e-3:
                    strip.set_fill(opacity=0).set_stroke(opacity=0)
                    continue
                strip.set_points_as_corners([plot_point(left, low_left), plot_point(right, low_right), plot_point(right, high_right),
                                             plot_point(left, high_left), plot_point(left, low_left)])
                strip.set_fill(opacity=strips.opacity).set_stroke(width=BAR_OUTLINE, opacity=1)

        # E2's persistent TR bars: each follows the current quantity and its demand price, including fractional steps.
        revenue_area = VGroup(*[Polygon(plot_point(u, 0), plot_point(u + 1, 0), plot_point(u + 1, demand(FIRST_Q)),
                                        plot_point(u, demand(FIRST_Q)), color=CONTEXT_CURVE_COLOR, stroke_width=BAR_OUTLINE, stroke_opacity=0,
                                        fill_color=CONTEXT_CURVE_COLOR, fill_opacity=0).set_z_index(FILL_LAYER)
                               for u in range(int(TOP_PRICE / 2))])
        for u, bar in enumerate(revenue_area):
            bar.add_updater(lambda m, u=u: m.set_points_as_corners([
                plot_point(u + BAR_GAP / 2, 0), plot_point(max(u + BAR_GAP / 2 + 0.001, min(u + 1 - BAR_GAP / 2, q_two())), 0),
                plot_point(max(u + BAR_GAP / 2 + 0.001, min(u + 1 - BAR_GAP / 2, q_two())), demand(q_two())),
                plot_point(u + BAR_GAP / 2, demand(q_two())), plot_point(u + BAR_GAP / 2, 0)])
                .set_fill(CONTEXT_CURVE_COLOR, PROFIT_OPACITY * float(q_two() > u + BAR_GAP / 2))
                .set_stroke(CONTEXT_CURVE_COLOR, BAR_OUTLINE, opacity=float(q_two() > u + BAR_GAP / 2)).set_z_index(FILL_LAYER))
            bar.update()
        # Both coordinates and their point are red. Read quantity upward, then price leftward from demand.
        dot_one = Dot(plot_point(FIRST_Q, demand(FIRST_Q)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        dot_one.add_updater(lambda m: m.move_to(plot_point(q_one(), demand(q_one()))))
        drop_one = dashed(plot_point(FIRST_Q, 0), plot_point(FIRST_Q, demand(FIRST_Q)), GUIDE).set_z_index(GUIDE_LAYER)
        drop_one.add_updater(lambda m: m.become(dashed(plot_point(q_one(), 0), plot_point(q_one(), demand(q_one())), GUIDE))
                             .set_z_index(GUIDE_LAYER))
        across_one = dashed(plot_point(FIRST_Q, demand(FIRST_Q)), plot_point(0, demand(FIRST_Q)), GUIDE).set_z_index(GUIDE_LAYER)
        across_one.add_updater(lambda m: m.become(dashed(plot_point(q_one(), demand(q_one())), plot_point(0, demand(q_one())), GUIDE))
                               .set_z_index(GUIDE_LAYER))
        dot_two = dot_one.copy().clear_updaters()
        dot_two.add_updater(lambda m: m.move_to(plot_point(q_two(), demand(q_two()))))
        drop_two = drop_one.copy().clear_updaters()
        drop_two.add_updater(lambda m: m.become(dashed(plot_point(q_two(), 0), plot_point(q_two(), demand(q_two())), GUIDE))
                             .set_z_index(GUIDE_LAYER))
        across_two = across_one.copy().clear_updaters()
        across_two.add_updater(lambda m: m.become(dashed(plot_point(q_two(), demand(q_two())), plot_point(0, demand(q_two())), GUIDE))
                               .set_z_index(GUIDE_LAYER))
        # E1's short leaders separate close readouts without moving the axes, intercept, or guide endpoints.
        price_one_y = lambda: min(plot_point(0, demand(q_one()))[1], demand_start.get_bottom()[1] - 0.25)
        price_two_y = lambda: min(plot_point(0, demand(q_two()))[1], price_one_y() - 0.4)
        price_one = DecimalNumber(demand(FIRST_Q), num_decimal_places=0, color=GUIDE).scale(PRICE_SCALE)
        price_one.add_updater(lambda m: m.set_value(round(demand(q_one()), 4))
                              .next_to(plot_point(0, demand(q_one())), LEFT, buff=0.75).set_y(price_one_y()))
        price_two = DecimalNumber(demand(FIRST_Q), num_decimal_places=0, color=GUIDE).scale(PRICE_SCALE)
        price_two.add_updater(lambda m: m.set_value(round(demand(q_two()), 4))
                              .next_to(plot_point(0, demand(q_two())), LEFT, buff=0.75).set_y(price_two_y()))
        quantity_one = DecimalNumber(FIRST_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        # Fan the quantity labels apart when adjacent units are too close for two numbers.
        quantity_nudge = lambda: max(0, 0.5 - (plot_point(q_two(), 0)[0] - plot_point(q_one(), 0)[0])) / 2 * min(1, step_q.get_value() / STEP_Q)
        quantity_one.add_updater(lambda m: m.set_value(round(q_one(), 4))
                                 .move_to(plot_point(q_one(), 0) + DOWN * QUANTITY_NUMBER_OFFSET)
                                 .shift(LEFT * quantity_nudge()))
        quantity_two = DecimalNumber(FIRST_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        quantity_two.add_updater(lambda m: m.set_value(round(q_two(), 4))
                                 .move_to(plot_point(q_two(), 0) + DOWN * QUANTITY_NUMBER_OFFSET)
                                 .shift(RIGHT * quantity_nudge()))
        price_leaders, quantity_leaders = VGroup(), VGroup()
        for q_read, price_readout, quantity_readout in ((q_one, price_one, quantity_one), (q_two, price_two, quantity_two)):
            price_leader = Line(ORIGIN, LEFT, color=MUTED, stroke_width=1).set_z_index(GUIDE_LAYER)
            price_leader.add_updater(lambda m, q_read=q_read, readout=price_readout: m.set_points_as_corners([
                plot_point(0, demand(q_read())) + LEFT * 0.025,
                np.array([plot_point(0, 0)[0] - 0.10, readout.get_y(), 0]),
                readout.get_right() + RIGHT * 0.06]))
            price_leaders.add(price_leader)
            quantity_leader = Line(ORIGIN, DOWN, color=MUTED, stroke_width=1).set_z_index(GUIDE_LAYER)
            quantity_leader.add_updater(lambda m, q_read=q_read, readout=quantity_readout: m.set_points_as_corners([
                plot_point(q_read(), 0) + DOWN * 0.04, readout.get_top() + UP * 0.04]))
            quantity_leaders.add(quantity_leader)
        point_one = [dot_one, drop_one, across_one, price_one, quantity_one, price_leaders[0], quantity_leaders[0]]
        point_two = [dot_two, drop_two, across_two, price_two, quantity_two, price_leaders[1], quantity_leaders[1]]
        for m in point_one:
            m.update()
        trial_quantity = Dot(plot_point(FIRST_Q, 0), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('If we produce one unit, what price lets us sell it?')
        self.play(FadeIn(quantity_one), FadeIn(quantity_leaders[0]), GrowFromCenter(trial_quantity), FadeIn(note))
        self.pause('1.c')

        # ---- 2.a · Demand answers the price question: up from Q = 1, then across to P = 119.
        self.remove(note)
        note = teaching(r'Demand tells us: one unit sells for \$119.')
        self.play(Create(drop_one), GrowFromCenter(dot_one), FadeOut(trial_quantity))
        self.play(Create(across_one), run_time=1.0)
        self.play(FadeIn(price_one), FadeIn(price_leaders[0]), FadeIn(note))
        self.pause('2.a')

        # ---- 2.b.question · E2's TR-to-MR panel; keep the demand equation above its own curve.
        divider = Line([DIVIDER_X, 2.3, 0], [DIVIDER_X, -3.0, 0], color=MUTED, stroke_width=1.5)
        MR_MATH_LEFT, MR_MATH_SCALE = PANEL_LEFT + WORK_INDENT, 0.64
        tr_heading = Tex('Total Revenue', color=TR_COLOR).scale(0.8)
        tr_heading.set_x(PANEL_LEFT, direction=LEFT).set_y(2.15)
        mr_heading = Tex('Marginal Revenue', color=MR_COLOR).scale(0.8)
        mr_heading.set_x(PANEL_LEFT, direction=LEFT).set_y(-0.05)
        mr_examples = []
        for before in (FIRST_Q, SECOND_Q):
            after = before + STEP_Q
            revenue_rows = VGroup()
            for q, y in ((before, 1.5), (after, 0.8)):
                total_text = f'{demand(q) * q:,.0f}'.replace(',', '{,}')
                row = VGroup(MathTex(rf'\mathrm{{TR}}_{{{q}}}', color=TR_COLOR), MathTex('=', color=INK),
                             MathTex(f'{demand(q):.0f}', color=GUIDE), MathTex(r'\times', color=INK),
                             MathTex(str(q), color=GUIDE), MathTex('=', color=INK), MathTex(total_text, color=TR_COLOR))
                row.arrange(RIGHT, buff=0.10).scale(MR_MATH_SCALE).set_x(MR_MATH_LEFT, direction=LEFT).set_y(y)
                revenue_rows.add(row)
            definition = VGroup(MathTex(r'\mathrm{MR}', color=MR_COLOR), MathTex('=', color=INK),
                                MathTex(rf'\mathrm{{TR}}_{{{after}}}', color=TR_COLOR), MathTex('-', color=INK),
                                MathTex(rf'\mathrm{{TR}}_{{{before}}}', color=TR_COLOR))
            definition.arrange(RIGHT, buff=0.10).scale(MR_MATH_SCALE).set_x(MR_MATH_LEFT, direction=LEFT).set_y(-0.7)
            difference = VGroup(MathTex('=').scale(MR_MATH_SCALE), revenue_rows[1][6].copy(),
                                MathTex('-').scale(MR_MATH_SCALE), revenue_rows[0][6].copy())
            difference.arrange(RIGHT, buff=0.10).set_y(-1.35)
            difference.shift(RIGHT * (definition[1].get_x() - difference[0].get_x()))
            marginal = (demand(after) * after - demand(before) * before) / STEP_Q
            result = VGroup(MathTex('='), MathTex(f'{marginal:.0f}', color=MR_COLOR))
            result.arrange(RIGHT, buff=0.10).scale(MR_MATH_SCALE).set_y(-2.0)
            result.shift(RIGHT * (definition[1].get_x() - result[0].get_x()))
            mr_examples.append(VGroup(*revenue_rows, definition, difference, result))
        tr_before, tr_after, mr_definition, mr_difference, mr_result = mr_examples[0]
        self.remove(note)
        note = teaching(r'Total Revenue is price times quantity: $TR = P \times Q$.')
        self.play(FadeIn(divider), FadeIn(tr_heading),
                  FadeIn(VGroup(*tr_before[:2])), FadeIn(note), run_time=1.4)
        self.pause('2.b.question')

        # ---- 2.b.first.inputs · As in E2, carry the graph's red inputs into TR before evaluating it.
        self.play(TransformFromCopy(price_one.copy().clear_updaters(), tr_before[2]), FadeIn(tr_before[3]),
                  TransformFromCopy(quantity_one.copy().clear_updaters(), tr_before[4]), run_time=1.2)
        self.pause('2.b.first.inputs')

        # ---- 2.b.first · Evaluate the first total only after its inputs have arrived.
        self.play(FadeIn(VGroup(*tr_before[5:])), FadeIn(revenue_area), run_time=0.5)
        self.add(tr_before)
        self.pause('2.b.first')

        # ---- 2.b.more · Keep TR visible while asking what one more unit adds.
        self.remove(note)
        note = teaching('How does Total Revenue change when we increase quantity by one?')
        self.play(FadeIn(note))
        self.pause('2.b.more')

        # ---- 2.b.price · Roll quantity from 1 to 2; price, guides, and the TR area move together.
        for m in point_two:
            m.update()
        self.add(*point_two)
        self.play(step_q.animate.set_value(STEP_Q), run_time=1.2, rate_func=smooth)
        self.remove(note)
        note = teaching(r'To sell two units, the price falls to \$118 on each unit.')
        self.play(FadeIn(note))
        self.pause('2.b.price')

        # ---- 2.b.second.inputs · Carry the new graph inputs to the second TR row, as in E2.
        self.play(FadeIn(VGroup(*tr_after[:2])), run_time=0.4)
        self.play(TransformFromCopy(price_two.copy().clear_updaters(), tr_after[2]), FadeIn(tr_after[3]),
                  TransformFromCopy(quantity_two.copy().clear_updaters(), tr_after[4]), run_time=1.2)
        self.pause('2.b.second.inputs')

        # ---- 2.b.second · Keep both completed totals visible for the comparison.
        self.remove(note)
        note = teaching(r'At the new price and quantity, total revenue is \$236.')
        self.play(FadeIn(VGroup(*tr_after[5:])), FadeIn(note), run_time=0.5)
        self.add(tr_after)
        self.pause('2.b.second')

        # ---- 2.b.definition · Copy the TR labels into MR: with a one-unit increase, MR is their difference.
        self.remove(note)
        note = teaching('Marginal Revenue is the change in revenue per additional unit.')
        self.play(FadeIn(mr_heading), FadeIn(VGroup(*mr_definition[:2], mr_definition[3])),
                  FadeIn(note), run_time=0.5)
        self.play(TransformFromCopy(tr_after[0], mr_definition[2]),
                  TransformFromCopy(tr_before[0], mr_definition[4]), run_time=1.0)
        self.add(mr_definition)
        self.pause('2.b.definition')

        # ---- 2.b.split · Fly the two grey totals into the subtraction, as in E2.
        self.play(FadeIn(VGroup(mr_difference[0], mr_difference[2])),
                  TransformFromCopy(tr_after[6], mr_difference[1]),
                  TransformFromCopy(tr_before[6], mr_difference[3]), run_time=1.2)
        self.add(mr_difference)
        self.pause('2.b.split')

        # ---- 2.b · Evaluate MR, then mark the midpoint of this one-unit interval.
        mr_dot = Dot(plot_point(FIRST_Q + STEP_Q / 2, marginal_revenue(FIRST_Q + STEP_Q / 2)), radius=DOT_RADIUS, color=MR_COLOR).set_z_index(DOT_LAYER)
        mr_dot.add_updater(lambda m: m.move_to(plot_point(FIRST_Q + STEP_Q / 2, marginal_revenue(FIRST_Q + STEP_Q / 2))))
        self.remove(note)
        note = teaching(r'One more unit adds \$117 to Total Revenue.')
        self.play(FadeIn(mr_result), run_time=0.5)
        self.play(GrowFromCenter(mr_dot), FadeIn(note))
        self.pause('2.b')

        # ---- 2.b.repeat.second · Repeat once, farther along demand: 25 to 26 units.
        # Keep the first MR dot while restoring the full graph and moving the current TR bars to 25.
        self.remove(note)
        self.play(FadeOut(tr_before), FadeOut(tr_after), FadeOut(mr_definition),
                  FadeOut(mr_difference), FadeOut(mr_result),
                  *[FadeOut(m) for m in point_one], FadeOut(price_two), FadeOut(quantity_two),
                  FadeOut(price_leaders[1]), FadeOut(quantity_leaders[1]), run_time=0.6)
        first_q.set_value(FIRST_Q + STEP_Q)
        step_q.set_value(0)
        note = teaching('Now repeat the one-unit increase farther along demand.')
        self.play(graph_q_max.animate.set_value(X_END), first_q.animate.set_value(SECOND_Q),
                  axis_words[2].animate.shift(LEFT * 0.55), FadeOut(graph_extent), FadeIn(note), run_time=1.8)
        demand_line.clear_updaters()
        mr_dot.clear_updaters()
        graph_extent.clear_updaters()
        self.remove(dot_two, drop_two, across_two)
        for m in point_one:
            m.update()
        self.add(dot_one, drop_one, across_one)
        tr_before, tr_after, mr_definition, mr_difference, mr_result = mr_examples[1]
        self.play(FadeIn(price_one), FadeIn(quantity_one), FadeIn(price_leaders[0]), FadeIn(quantity_leaders[0]),
                  FadeIn(VGroup(*tr_before[:2])), run_time=0.5)
        self.play(TransformFromCopy(price_one.copy().clear_updaters(), tr_before[2]), FadeIn(tr_before[3]),
                  TransformFromCopy(quantity_one.copy().clear_updaters(), tr_before[4]), run_time=1.0)
        self.play(FadeIn(VGroup(*tr_before[5:])), run_time=0.5)
        self.add(tr_before)
        # Retain the original dashed guides; use just one moving demand dot at the full scale.
        self.remove(dot_one)
        for m in point_two:
            m.update()
        self.add(*point_two)
        self.play(step_q.animate.set_value(STEP_Q), run_time=1.2, rate_func=smooth)
        self.play(FadeIn(VGroup(*tr_after[:2])), run_time=0.4)
        self.play(TransformFromCopy(price_two.copy().clear_updaters(), tr_after[2]), FadeIn(tr_after[3]),
                  TransformFromCopy(quantity_two.copy().clear_updaters(), tr_after[4]), run_time=1.0)
        self.play(FadeIn(VGroup(*tr_after[5:])), run_time=0.5)
        self.add(tr_after)
        self.play(FadeIn(VGroup(*mr_definition[:2], mr_definition[3])),
                  TransformFromCopy(tr_after[0], mr_definition[2]),
                  TransformFromCopy(tr_before[0], mr_definition[4]), run_time=1.0)
        self.add(mr_definition)
        self.play(FadeIn(VGroup(mr_difference[0], mr_difference[2])),
                  TransformFromCopy(tr_after[6], mr_difference[1]),
                  TransformFromCopy(tr_before[6], mr_difference[3]), run_time=1.0)
        self.add(mr_difference)
        mr_second_dot = Dot(ax.c2p(SECOND_Q + STEP_Q / 2, marginal_revenue(SECOND_Q + STEP_Q / 2)),
                            radius=DOT_RADIUS, color=MR_COLOR).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching(r'One more unit here adds \$69 to Total Revenue.')
        self.play(FadeIn(mr_result), run_time=0.5)
        self.play(GrowFromCenter(mr_second_dot), FadeIn(note))
        self.pause('2.b.repeat.second')

        # ---- 2.c · Connect the two calculated MR points, then extend that straight line to the axes.
        mr_line = Line(mr_dot.get_center(), mr_second_dot.get_center(),
                       color=MR_COLOR, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        mr_word = Tex('MR', color=MR_COLOR).scale(CURVE_WORD_SCALE).next_to(ax.c2p(TOP_PRICE / 2 * BASE_ALPHA, 0), UR, buff=0.12)
        mr_row = MathTex(r'\mathrm{MR} = 120 - 2Q', color=MR_COLOR, tex_to_color_map={'Q': GUIDE}).scale(ROW_SCALE)
        mr_row.move_to([PANEL_LEFT, 1.5, 0], aligned_edge=LEFT)
        demand_marks = [*point_one[1:], price_two, quantity_two, price_leaders[1], quantity_leaders[1]]
        for m in demand_marks:
            m.clear_updaters()
        self.remove(note)
        note = teaching('Two points give us the marginal revenue line.')
        self.play(*[FadeOut(m) for m in demand_marks],
                  FadeOut(tr_heading), FadeOut(tr_before), FadeOut(tr_after), FadeOut(mr_heading),
                  FadeOut(mr_definition), FadeOut(mr_difference), FadeOut(mr_result), FadeIn(note), run_time=0.6)
        self.play(Create(mr_line), run_time=1.0)
        self.play(mr_line.animate.put_start_and_end_on(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2 * BASE_ALPHA, 0)),
                  FadeIn(mr_word), FadeIn(mr_row), run_time=1.0)
        self.pause('2.c')

        # ---- 2.c.trace · Only after the two examples and their line, show quantity moving along it.
        mr_sweep_dot = mr_second_dot.copy()
        mr_sweep_dot.add_updater(lambda m: m.move_to(ax.c2p(q_one() + STEP_Q / 2,
                                                            marginal_revenue(q_one() + STEP_Q / 2))))
        self.add(mr_sweep_dot)
        self.remove(note)
        note = teaching('As quantity rises, each additional unit adds less revenue.')
        self.play(FadeIn(note))
        self.play(first_q.animate.set_value(TOP_PRICE / 2 - STEP_Q), run_time=3.0, rate_func=smooth)
        self.pause('2.c.trace')

        # ---- 2.c.exercise · Q1 practices MR at two new quantities before introducing costs.
        # Cover the lecture graph while students work; keep its state ready to resume.
        exercise_ground = Rectangle(width=config.frame_width, height=config.frame_height,
                                    stroke_width=0, fill_color=BG, fill_opacity=1).set_z_index(100)
        exercise_q1_label = Tex(r'Exercise E3 \textbar{} Q1', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_q1_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_q1_context = Tex(
            r'\begin{minipage}{32em}\sffamily\raggedright '
            r'Demand is $P = 120 - Q$, and the firm charges\\'
            r'the same price for every unit.\end{minipage}', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        exercise_q1_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        exercise_q1_questions = VGroup(
            Tex(r'\begin{minipage}{27em}\raggedright '
                r'Find the price and total revenue at $Q = 40$\\'
                r'and at $Q = 50$.\end{minipage}', color=INK),
            Tex(r'\begin{minipage}{27em}\raggedright '
                r'Calculate the change in total revenue, then marginal\\'
                r'revenue averaged over these 10 additional units.\end{minipage}', color=INK),
        ).scale(EXERCISE_SCALE).arrange(DOWN, buff=EXERCISE_QUESTION_GAP, aligned_edge=LEFT)
        exercise_q1_questions.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
            exercise_q1_context.get_bottom()[1] - EXERCISE_SETUP_GAP, direction=UP)
        exercise_q1_markers = VGroup(*[Tex(letter, color=INK).scale(EXERCISE_SCALE) for letter in ('a)', 'b)')])
        for marker, question in zip(exercise_q1_markers, exercise_q1_questions):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP, aligned_edge=UP)
        exercise_q1_text = VGroup(exercise_q1_label, exercise_q1_context, exercise_q1_questions,
                                 exercise_q1_markers).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_q1_text), run_time=0.4)
        self.pause('2.c.exercise')
        self.play(FadeOut(exercise_q1_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 2.d · Introduce the objective, then MC alone; ATC waits for the third decision.
        mc_line = Line(ax.c2p(0, 0), ax.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=CURVE_WIDTH).set_z_index(CURVE_LAYER)
        mc_word = Tex('MC', color=MC_COLOR).scale(CURVE_WORD_SCALE).next_to(ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15)
        profit_heading = Tex('Maximize Profit').scale(0.8).move_to([PANEL_LEFT, 2.15, 0], aligned_edge=LEFT)
        objective = MathTex(r'\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}', tex_to_color_map={'q': GUIDE, r'\pi': PROFIT_COLOR}).scale(ROW_SCALE)
        objective.move_to([PANEL_LEFT, 1.57, 0], aligned_edge=LEFT)
        revenue_marks = [dot_two, drop_two, across_two, mr_sweep_dot, *revenue_area]
        for m in revenue_marks:
            m.clear_updaters()
        self.remove(note)
        note = teaching('Now bring in costs to choose the most profitable quantity.')
        self.play(FadeIn(note), FadeOut(mr_dot), FadeOut(mr_second_dot), FadeOut(mr_sweep_dot),
                  FadeOut(dot_two), FadeOut(drop_two), FadeOut(across_two), FadeOut(revenue_area),
                  FadeOut(demand_row), FadeOut(mr_row), FadeIn(demand_word), FadeIn(profit_heading), run_time=1.0)
        self.play(FadeIn(objective), run_time=0.8)
        self.play(Create(mc_line), FadeIn(mc_word), run_time=1.0)
        self.pause('2.d')

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

        self.remove(note)
        step_one = Tex('1. How much to produce?')
        step_two = Tex('2. What price sells it all?')
        step_three = Tex('3. What is the average cost?')
        step_four = MathTex(r'4.\enspace \pi^* = (P^* - \mathrm{ATC}^*)\cdot q^*',
                            tex_to_color_map={'P^*': GUIDE, 'q^*': GUIDE, r'\pi^*': PROFIT_COLOR})
        work_one = MathTex(r'{{q^*}} = {{30}}', color=CAPTION, tex_to_color_map={'q^*': GUIDE, '30': GUIDE})
        work_two = MathTex(r'{{P^*}} = 120 - {{30}} = {{90}}', color=CAPTION,
                           tex_to_color_map={'P^*': GUIDE, '30': GUIDE, '90': GUIDE})
        work_three = MathTex(r'\mathrm{ATC}^* = 70', color=ATC_COLOR)
        work_four = MathTex(r'\pi^* = (90 - {{70}})\cdot 30 = {{600}}',
                            tex_to_color_map={'90': GUIDE, '30': GUIDE, r'\pi^*': PROFIT_COLOR})
        work_four.get_part_by_tex('70').set_color(ATC_COLOR)
        work_four.get_part_by_tex('600').set_color(PROFIT_COLOR)
        for row, y in zip((step_one, work_one, step_two, work_two, step_three, work_three, step_four, work_four),
                          (0.87, 0.49, -0.10, -0.48, -1.07, -1.45, -2.04, -2.42)):
            row.scale(ROW_SCALE).move_to([PANEL_LEFT, y, 0], aligned_edge=LEFT)
        for work in (work_one, work_two, work_three, work_four):
            work.shift(RIGHT * WORK_INDENT)
        card = VGroup(profit_heading, objective, step_one, work_one, step_two, work_two,
                      step_three, work_three, step_four, work_four)
        # Separate source equations become one equality before any numerical answer appears.
        mr_name = MathTex(r'\mathrm{MR}', color=MR_COLOR).scale(ROW_SCALE)
        mc_name = MathTex(r'\mathrm{MC}', color=MC_COLOR).scale(ROW_SCALE)
        mr_equals, mc_equals = [MathTex('=', color=CAPTION).scale(ROW_SCALE) for _ in range(2)]
        mr_expression = MathTex(r'120 - 2{{q}}', color=MR_COLOR, tex_to_color_map={'q': GUIDE}).scale(ROW_SCALE)
        mc_expression = MathTex(r'2{{q}}', color=MC_COLOR, tex_to_color_map={'q': GUIDE}).scale(ROW_SCALE)
        mr_equation = VGroup(mr_name, mr_equals, mr_expression).arrange(RIGHT, buff=0.10)
        mc_equation = VGroup(mc_name, mc_equals, mc_expression).arrange(RIGHT, buff=0.10)
        mr_equation.move_to(work_one.get_left(), aligned_edge=LEFT)
        mc_equation.next_to(mr_equation, DOWN, buff=0.28, aligned_edge=LEFT)
        equal_sign = MathTex('=', color=CAPTION).scale(ROW_SCALE)
        equal_targets = VGroup(mr_expression.copy(), equal_sign, mc_expression.copy()).arrange(RIGHT, buff=0.12)
        equal_targets.move_to(work_one.get_left(), aligned_edge=LEFT)
        collected = MathTex(r'4{{q}} = 120', color=CAPTION, tex_to_color_map={'q': GUIDE}).scale(ROW_SCALE)
        collected.move_to(work_one.get_left(), aligned_edge=LEFT)
        # The answer marks: a red dot where MR meets (policy) MC, its drop, and the two-row quantity readout.
        choice_dot = Dot(ax.c2p(30, 60), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        choice_dot.add_updater(lambda m: m.move_to(ax.c2p(best_q(), policy_mc(best_q()))))
        quantity_guide = dashed(ax.c2p(30, 60), ax.c2p(30, 0), GUIDE).set_z_index(GUIDE_LAYER)
        # The chosen quantity row steps aside where the efficient quantity sits (6.c).
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
        note = teaching('How much should we produce? Find where MR equals MC.')
        self.play(FadeIn(step_one), FadeIn(note))
        self.play(GrowFromCenter(choice_dot))
        self.play(Create(quantity_guide), FadeIn(quantity_star))
        self.play(FadeIn(mr_equation), FadeIn(mc_equation))
        self.play(FadeOut(mr_name), FadeOut(mc_name), FadeOut(mr_equals), FadeOut(mc_equals),
                  mr_expression.animate.move_to(equal_targets[0]), mc_expression.animate.move_to(equal_targets[2]),
                  FadeIn(equal_sign), run_time=1.2)
        self.play(ReplacementTransform(VGroup(mr_expression, equal_sign, mc_expression), collected))
        self.play(ReplacementTransform(collected, work_one), FadeIn(quantity_number))
        self.pause('3.a')

        # ---- 3.b · Step 2: up from q* to demand, then left to P* = 90; all coordinate marks are red.
        price_dot = Dot(ax.c2p(30, 90), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        price_dot.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), price_now())))
        price_guide = dashed(ax.c2p(30, 90), ax.c2p(0, 90), GUIDE).set_z_index(GUIDE_LAYER)
        price_guide.add_updater(lambda m: m.become(dashed(ax.c2p(chosen_q(), price_now()), ax.c2p(0, price_now()), GUIDE))
                                .set_z_index(GUIDE_LAYER))
        price_number = DecimalNumber(90, num_decimal_places=2, color=GUIDE).scale(PRICE_SCALE)
        price_number.add_updater(lambda m: m.set_value(price_now()).next_to(ax.c2p(0, price_now()), LEFT, buff=0.2))
        price_star = MathTex('P^*=', color=GUIDE).scale(PRICE_SCALE)
        price_star.add_updater(lambda m: m.next_to(price_number, LEFT, buff=0.08))
        price_free = MathTex('P=', color=GUIDE).scale(PRICE_SCALE)
        price_free.add_updater(lambda m: m.next_to(price_number, LEFT, buff=0.08))
        for m in (price_dot, price_guide, price_number, price_star):
            m.update()
        self.remove(note)
        note = teaching('Find the highest price that sells all 30 units.')
        self.play(FadeIn(step_two), FadeIn(note))
        quantity_extension = dashed(ax.c2p(30, 60), ax.c2p(30, 90), GUIDE).set_z_index(GUIDE_LAYER)
        self.play(Create(quantity_extension), run_time=0.8)
        self.play(GrowFromCenter(price_dot))
        demand_substitution = MathTex(r'{{P^*}} = 120 - {{q^*}}', color=CAPTION,
                                     tex_to_color_map={'P^*': GUIDE, 'q^*': GUIDE}).scale(ROW_SCALE)
        demand_substitution.move_to(work_two.get_left(), aligned_edge=LEFT)
        substituted_price = MathTex(r'{{P^*}} = 120 - {{30}}', color=CAPTION,
                                   tex_to_color_map={'P^*': GUIDE, '30': GUIDE}).scale(ROW_SCALE)
        substituted_price.move_to(work_two.get_left(), aligned_edge=LEFT)
        self.play(FadeIn(demand_substitution))
        self.play(ReplacementTransform(demand_substitution, substituted_price))
        self.play(ReplacementTransform(substituted_price, work_two))
        self.play(Create(price_guide), run_time=0.8)
        self.play(FadeIn(price_number), FadeIn(price_star))
        rise.set_value(1)
        self.remove(quantity_extension)
        quantity_guide.add_updater(lambda m: m.become(dashed(ax.c2p(chosen_q(), 0), ax.c2p(chosen_q(), guide_top()), GUIDE))
                                   .set_z_index(GUIDE_LAYER))
        quantity_guide.update()
        self.pause('3.b')

        # ---- 3.c · Only now introduce ATC and read the cost at the already-chosen quantity.
        atc_curve = polyline([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, ATC_TO, 200)],
                             ATC_COLOR, CURVE_WIDTH).set_z_index(CURVE_LAYER)
        atc_word = Tex('ATC', color=ATC_COLOR).scale(CURVE_WORD_SCALE).next_to(ax.c2p(ATC_TO, atc(ATC_TO)), RIGHT, buff=0.15)
        atc_y = lambda: min(ax.c2p(0, policy_atc(chosen_q()))[1], ax.c2p(0, price_now())[1] - 0.34)
        atc_dot = Dot(ax.c2p(30, atc(30)), radius=DOT_RADIUS, color=ATC_COLOR).set_z_index(DOT_LAYER)
        atc_dot.add_updater(lambda m: m.move_to(ax.c2p(chosen_q(), policy_atc(chosen_q()))))
        atc_guide = dashed(ax.c2p(30, atc(30)), ax.c2p(0, atc(30)), GUIDE).set_z_index(GUIDE_LAYER)
        atc_guide.add_updater(lambda m: m.become(dashed(ax.c2p(chosen_q(), policy_atc(chosen_q())),
                                                        ax.c2p(0, policy_atc(chosen_q())), GUIDE))
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
        note = teaching('Read average total cost from the curve at this quantity.')
        self.play(FadeIn(step_three), FadeIn(note))
        self.play(FadeIn(atc_curve), FadeIn(atc_word))
        self.play(GrowFromCenter(atc_dot))
        self.play(Create(atc_guide), run_time=0.8)
        self.play(FadeIn(atc_number), FadeIn(atc_star), FadeIn(work_three))
        self.pause('3.c')

        # ---- 3.d · Step 4: profit, (90 - 70) x 30 = 600, as one-unit strips between ATC* and P*.
        profit_strips = strip_group(80, PROFIT_COLOR, PROFIT_OPACITY, FILL_LAYER)
        profit_strips.add_updater(lambda m: follow_strips(m, 0, chosen_q(),
                                                        lambda x: policy_atc(chosen_q()), lambda x: price_now()))
        profit_strips.update()
        # Keep the plain white name in the visible part of profit, above a subsidy's government band.
        profit_floor = lambda: max(policy_atc(chosen_q()), atc(chosen_q()))
        profit_height = lambda: ax.c2p(0, price_now())[1] - ax.c2p(0, profit_floor())[1]
        profit_word = Tex('Profit', color=INK).scale(AREA_WORD_SCALE).set_z_index(WORD_LAYER)
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

        # ---- 3.e.setup · After calculating profit, replace the math with a second graph for the quantity experiment.
        # Keep the live profit row ready for the later demand and policy examples, after this separate sequence.
        profit_anchor = VectorizedPoint(work_four.get_left())


        def profit_row(prefix, quantity_places=0):
            row = VGroup(MathTex(prefix, tex_to_color_map={r'\pi': PROFIT_COLOR}), DecimalNumber(90, num_decimal_places=2, color=GUIDE), MathTex('-'),
                         DecimalNumber(atc(30), num_decimal_places=2, color=ATC_COLOR), MathTex(r')\hspace{2.5pt}\cdot'),
                         DecimalNumber(30, num_decimal_places=quantity_places, color=GUIDE), MathTex('='),
                         DecimalNumber(600, num_decimal_places=0, color=PROFIT_COLOR)).scale(ROW_SCALE)
            row.add_updater(lambda m: (m[1].set_value(price_now()), m[3].set_value(policy_atc(chosen_q())),
                                       m[5].set_value(round(chosen_q(), 4)), m[7].set_value(round(profit_now(), 4)),
                                       [m[k + 1].next_to(m[k], RIGHT, buff=ROW_GAPS[k]) for k in range(7)],
                                       m.move_to(profit_anchor.get_center(), aligned_edge=LEFT)))
            return row
        live_profit = profit_row(r'\pi^* = (')
        moving = [quantity_guide, quantity_number, quantity_free, price_dot, price_guide, price_number, price_free,
                  atc_dot, atc_guide, atc_number, atc_free, profit_strips, profit_word]
        for m in moving:
            m.update()

        # Curves and labels follow the axes as the monopoly graph becomes narrower; type stays full size.
        ax.save_state()
        demand_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * alpha.get_value(), 0)))
        demand_word.add_updater(lambda m: m.next_to(demand_word_at(alpha.get_value()), UR, buff=0.1))
        demand_start.add_updater(lambda m: m.next_to(ax.c2p(0, TOP_PRICE), LEFT, buff=0.15))
        mr_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2 * alpha.get_value(), 0)))
        mr_word.add_updater(lambda m: m.next_to(ax.c2p(TOP_PRICE / 2 * alpha.get_value(), 0), UR, buff=0.12))
        mc_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, 0), ax.c2p(MC_END, mc(MC_END))))
        mc_word.add_updater(lambda m: m.next_to(ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15))
        atc_curve.add_updater(lambda m: m.set_points_as_corners([ax.c2p(q, atc(q)) for q in np.geomspace(ATC_FROM, ATC_TO, 200)]))
        atc_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, atc(ATC_TO)), RIGHT, buff=0.15))
        axis_words[0].add_updater(lambda m: m.next_to(ax.c2p(0, Y_TOP), LEFT, buff=0.23))
        axis_words[1].add_updater(lambda m: m.next_to(ax.c2p(0, Y_TOP), RIGHT, buff=0.22))
        axis_words[2].add_updater(lambda m: m.next_to(ax.c2p(X_END, 0), DOWN, buff=0.23))
        self.remove(note)
        self.play(FadeOut(card), ax.animate.stretch(5.3 / X_LENGTH, dim=0, about_point=GRAPH_ORIGIN),
                  divider.animate.set_x(0.25), run_time=1.4)
        self.remove(quantity_star, price_star, atc_star)
        self.add(quantity_free, price_free, atc_free)

        # The new vertical axis is total profit, not price. Only the quantities we visit are traced.
        profit_ax = style_axes([0, 60, 10], [0, 700, 100], x_length=5.25, y_length=4.2)
        profit_ax.shift(np.array([1.5, GRAPH_ORIGIN[1], 0]) - profit_ax.c2p(0, 0))
        profit_axis_words = VGroup(
            Tex('Profit', color=PROFIT_COLOR).scale(0.8).next_to(profit_ax.c2p(0, 700), UP, buff=0.18),
            Tex('Q', color=INK).scale(0.8).next_to(profit_ax.c2p(60, 0), RIGHT, buff=0.22),
            MathTex('0', color=MUTED).scale(PRICE_SCALE).next_to(profit_ax.c2p(0, 0), DL, buff=0.15),
            MathTex('60', color=MUTED).scale(QUANTITY_NUMBER_SCALE).next_to(profit_ax.c2p(60, 0), DOWN, buff=QUANTITY_NUMBER_OFFSET))
        profit_at = lambda q: demand(q) * q - (FIXED_COST + q ** 2)
        profit_curve = polyline([profit_ax.c2p(q, profit_at(q)) for q in np.linspace(30, 30.001, 100)],
                                PROFIT_COLOR, CURVE_WIDTH).set_z_index(CURVE_LAYER)
        profit_curve.add_updater(lambda m: m.set_points_as_corners([
            profit_ax.c2p(q, profit_at(q)) for q in np.linspace(30, max(30.001, chosen_q()), 100)]))
        profit_dot = Dot(profit_ax.c2p(30, 600), radius=FOCUS_RADIUS, color=PROFIT_COLOR).set_z_index(DOT_LAYER)
        profit_dot.add_updater(lambda m: m.move_to(profit_ax.c2p(chosen_q(), profit_now())))
        profit_q_guide = dashed(profit_ax.c2p(30, 600), profit_ax.c2p(30, 0), GUIDE).set_z_index(GUIDE_LAYER)
        profit_q_guide.add_updater(lambda m: m.become(dashed(
            profit_ax.c2p(chosen_q(), profit_now()), profit_ax.c2p(chosen_q(), 0), GUIDE)).set_z_index(GUIDE_LAYER))
        profit_value_guide = dashed(profit_ax.c2p(30, 600), profit_ax.c2p(0, 600), PROFIT_COLOR).set_z_index(GUIDE_LAYER)
        profit_value_guide.add_updater(lambda m: m.become(dashed(
            profit_ax.c2p(chosen_q(), profit_now()), profit_ax.c2p(0, profit_now()), PROFIT_COLOR)).set_z_index(GUIDE_LAYER))
        profit_q_number = DecimalNumber(30, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        profit_q_number.move_to(profit_ax.c2p(30, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        profit_value = DecimalNumber(600, num_decimal_places=0, color=PROFIT_COLOR).scale(QUANTITY_NUMBER_SCALE)
        profit_value.next_to(profit_ax.c2p(0, 600), LEFT, buff=0.18)
        profit_panel = VGroup(profit_ax, profit_axis_words, profit_curve, profit_dot,
                              profit_q_guide, profit_value_guide, profit_q_number, profit_value)
        profit_panel.update()
        note = teaching("MC = MR solves the firm's profit maximization problem.")
        self.play(FadeIn(profit_ax), FadeIn(profit_axis_words), FadeIn(note))
        self.play(TransformFromCopy(quantity_number.copy().clear_updaters(), profit_q_number),
                  TransformFromCopy(work_four.get_part_by_tex('600').copy().clear_updaters(), profit_value),
                  GrowFromCenter(profit_dot))
        profit_q_number.add_updater(lambda m: m.set_value(round(chosen_q(), 4))
                                   .move_to(profit_ax.c2p(chosen_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        profit_value.add_updater(lambda m: m.set_value(round(profit_now(), 4)).next_to(profit_ax.c2p(0, profit_now()), LEFT, buff=0.18))
        self.play(Create(profit_q_guide), Create(profit_value_guide))
        self.add(profit_curve)
        self.pause('3.e.setup')

        # ---- 3.e.more · Both graphs follow one quantity: at 40, profit falls to 400.
        self.remove(note)
        self.play(offset.animate.set_value(10), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('If we increase the quantity to 40, their profit goes down.')
        self.play(FadeIn(note))
        self.pause('3.e.more')

        # ---- 3.e.less · Then to 20: profit is 400 again.
        self.remove(note)
        profit_curve.clear_updaters()
        profit_curve.add_updater(lambda m: m.set_points_as_corners([
            profit_ax.c2p(q, profit_at(q)) for q in np.linspace(min(30, chosen_q()), 40, 100)]))
        self.play(offset.animate.set_value(-10), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('If we lower the quantity to 20, their profit also goes down.')
        self.play(FadeIn(note))
        self.pause('3.e.less')

        # ---- 3.e · Back to 30, where MR = MC: the highest profit, 600.
        self.remove(note)
        profit_curve.clear_updaters()                    # keep the traced curve while the dot returns to its peak
        self.play(offset.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        self.remove(quantity_free, price_free, atc_free)
        self.add(quantity_star, price_star, atc_star)
        note = teaching("MC = MR solves the firm's profit maximization problem.")
        self.play(FadeIn(note))
        self.pause('3.e')

        # ---- 3.e.exercise · Q2 repeats the three decisions under the handout's higher demand.
        exercise_q2_label = Tex(r'Exercise E3 \textbar{} Q2', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_q2_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_q2_context = Tex(
            r'\begin{minipage}{32em}\sffamily\raggedright '
            r'Suppose demand rises to $P = 160 - Q$, so $MR = 160 - 2Q$.\\'
            r'The monopolist\textquotesingle s marginal cost is still $MC = 2Q$,\\'
            r'with fixed cost of 1,200.\end{minipage}', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        exercise_q2_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        exercise_q2_questions = VGroup(
            Tex('Calculate and graph the profit-maximizing quantity.', color=INK),
            Tex(r'\begin{minipage}{27em}\raggedright '
                r'Calculate and graph the price that lets the firm\\'
                r'sell that quantity.\end{minipage}', color=INK),
            Tex(r'Calculate and graph the firm\textquotesingle s maximum profit.', color=INK),
        ).scale(EXERCISE_SCALE).arrange(DOWN, buff=EXERCISE_QUESTION_GAP, aligned_edge=LEFT)
        exercise_q2_questions.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
            exercise_q2_context.get_bottom()[1] - EXERCISE_SETUP_GAP, direction=UP)
        exercise_q2_markers = VGroup(*[Tex(letter, color=INK).scale(EXERCISE_SCALE) for letter in ('a)', 'b)', 'c)')])
        for marker, question in zip(exercise_q2_markers, exercise_q2_questions):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP, aligned_edge=UP)
        exercise_q2_hint = Tex(r'\sffamily Hint: $ATC$ at the profit-maximizing quantity is 70.', color=CAPTION).scale(EXERCISE_CONTEXT_SCALE)
        exercise_q2_hint.next_to(exercise_q2_questions, DOWN, buff=EXERCISE_QUESTION_GAP, aligned_edge=LEFT)
        exercise_q2_text = VGroup(exercise_q2_label, exercise_q2_context, exercise_q2_questions,
                                 exercise_q2_markers, exercise_q2_hint).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_q2_text), run_time=0.4)
        self.pause('3.e.exercise')
        self.play(FadeOut(exercise_q2_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 4.a · A smaller demand shift: q*, P*, ATC* and profit roll to 25, 85, 73 and 300.
        # The monopoly graph stands alone; keep the positive profit bars and a grey ghost of the old demand.
        self.remove(note)
        profit_panel.clear_updaters()
        self.play(FadeOut(profit_panel), FadeOut(divider),
                  ax.animate.stretch(X_LENGTH / 5.3, dim=0, about_point=GRAPH_ORIGIN).shift(RIGHT * 1.8), run_time=1.4)
        ghost_demand = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE * BASE_ALPHA, 0), color=MUTED, stroke_width=2).set_opacity(0.55).set_z_index(-1)
        self.add(ghost_demand)
        self.play(alpha.animate.set_value(LOW_ALPHA), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching("When demand shifts down, the firm's quantity and profit go down.")
        self.play(FadeIn(note))
        self.pause('4.a')

        # ---- 5.a.efficient · Demand returns; the socially efficient quantity, where MC meets demand, in red.
        self.remove(note)
        self.play(alpha.animate.set_value(BASE_ALPHA), FadeOut(ghost_demand), run_time=ROLL_TIME, rate_func=smooth)
        efficient_dot = Dot(ax.c2p(40, 80), radius=FOCUS_RADIUS, color=GUIDE).set_z_index(DOT_LAYER - 1)
        efficient_drop = dashed(ax.c2p(40, 0), ax.c2p(40, 80), GUIDE).set_z_index(GUIDE_LAYER - 1)
        efficient_words = VGroup(
            Tex('40', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            MathTex('Q_{sp}', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        efficient_dot.add_updater(lambda m: m.move_to(ax.c2p(40, 80)))
        efficient_drop.add_updater(lambda m: m.become(dashed(ax.c2p(40, 0), ax.c2p(40, 80), GUIDE)).set_z_index(GUIDE_LAYER - 1))
        efficient_words[0].add_updater(lambda m: m.move_to(ax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        efficient_words[1].add_updater(lambda m: m.move_to(ax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))
        note = teaching('The socially efficient quantity: where the MC and MB curves intersect.')
        self.play(FadeIn(note))
        self.play(GrowFromCenter(efficient_dot), Create(efficient_drop), FadeIn(efficient_words))
        self.pause('5.a.efficient')

        # ---- 5.a · The grey deadweight loss: every unit from q* to Q_sp, from MC up to demand.
        dwl_strips = strip_group(70, DWL, DWL_STRIP_OPACITY, FILL_LAYER)
        dwl_strips.add_updater(lambda m: follow_strips(m, chosen_q(), efficient_q(), mc,
                                                     lambda x: demand(x, alpha.get_value())))
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

        # ---- 5.a.exercise · Q3 distinguishes the firm's choice from the missing socially valuable trades.
        exercise_q3_label = Tex(r'Exercise E3 \textbar{} Q3', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_q3_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_q3_context = Tex(
            r'\begin{minipage}{32em}\sffamily\raggedright '
            r'Return to the original demand: $P = 120 - Q$,\\'
            r'with $MR = 120 - 2Q$ and $MC = 2Q$. The monopolist chooses\\'
            r'$Q = 30$ and $P = 90$. There are no externalities.\end{minipage}', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        exercise_q3_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        exercise_q3_questions = VGroup(
            Tex(r'\begin{minipage}{27em}\raggedright '
                r'At $Q = 30$, buyers\textquotesingle\ willingness to pay is 90 and marginal\\'
                r'cost is 60. Why does the monopolist stop here instead\\'
                r'of producing where $P = MC$?\end{minipage}', color=INK),
            Tex('Calculate and mark the socially efficient quantity.', color=INK),
            Tex('Calculate and shade the deadweight loss from monopoly.', color=INK),
        ).scale(EXERCISE_SCALE).arrange(DOWN, buff=EXERCISE_QUESTION_GAP, aligned_edge=LEFT)
        exercise_q3_questions.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
            exercise_q3_context.get_bottom()[1] - EXERCISE_SETUP_GAP, direction=UP)
        exercise_q3_markers = VGroup(*[Tex(letter, color=INK).scale(EXERCISE_SCALE) for letter in ('a)', 'b)', 'c)')])
        for marker, question in zip(exercise_q3_markers, exercise_q3_questions):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP, aligned_edge=UP)
        exercise_q3_text = VGroup(exercise_q3_label, exercise_q3_context, exercise_q3_questions,
                                 exercise_q3_markers).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_q3_text), run_time=0.4)
        self.pause('5.a.exercise')
        self.play(FadeOut(exercise_q3_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 6.a.shift · A per-unit tax shifts MC and ATC up by the tax (dashed copies); q* falls, P* rises.
        # Bring back the calculation panel only when the policy comparison begins.
        self.remove(note)
        divider.set_x(DIVIDER_X)
        self.play(Restore(ax), FadeIn(divider), run_time=1.2)
        compact = VGroup(profit_heading.copy(), objective.copy(), step_one.copy(), step_two.copy(), step_three.copy(), step_four.copy(),
                         work_four.copy()).arrange(DOWN, buff=ROW_GAP + 0.16, aligned_edge=LEFT)
        compact[2:].shift(DOWN * 0.12)
        compact[6].shift(RIGHT * WORK_INDENT)
        compact.move_to(card.get_corner(UL), aligned_edge=UL)
        for row, target in zip((profit_heading, objective, step_one, step_two, step_three, step_four), compact[:6]):
            row.move_to(target)
        profit_anchor.move_to(compact[6].get_left())
        live_profit.update()
        self.play(*[FadeIn(row) for row in (profit_heading, objective, step_one, step_two, step_three, step_four, live_profit)])
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
        mc_tax_word = Tex(r'MC $+$ tax', color=MC_COLOR).scale(CURVE_WORD_SCALE)
        mc_tax_word.add_updater(lambda m: m.next_to(ax.c2p(policy_mc_end(), POLICY_TOP), RIGHT, buff=0.15)
                                .set_opacity(np.clip((tax.get_value() - 4) / 4, 0, 1)))
        atc_tax_word = Tex(r'ATC $+$ tax', color=ATC_COLOR).scale(CURVE_WORD_SCALE)
        atc_tax_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                                 .set_opacity(np.clip((tax.get_value() - 4) / 4, 0, 1)))
        # The government's band: between the firm's true ATC and its ATC under the policy, over the q* units.
        gov_strips = strip_group(80, GOV, GOV_OPACITY, GOV_LAYER)
        gov_strips.add_updater(lambda m: follow_strips(m, 0, chosen_q(),
            lambda x: min(atc(chosen_q()), policy_atc(chosen_q())),
            lambda x: max(atc(chosen_q()), policy_atc(chosen_q()))))
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
        self.remove(note)
        note = teaching('We shift marginal cost and average total cost up by the tax.')
        self.add(policy_mc_line, policy_atc_curve, mc_tax_word, atc_tax_word, gov_strips)
        self.play(FadeIn(tax_row), FadeIn(note))
        self.play(tax.animate.set_value(TAX), run_time=ROLL_TIME + 0.8, rate_func=smooth)
        self.pause('6.a.shift')

        # ---- 6.a · The band between ATC and ATC + tax is the government's revenue; DWL has grown.
        self.remove(note)
        note = teaching('As the tax goes up, quantity goes down and deadweight loss goes up.')
        self.play(FadeIn(gov_word), FadeIn(note))
        self.pause('6.a')

        # ---- 6.b.shift · The tax comes off; a lump-sum tax of 500 is a fixed cost: only ATC shifts, q* stays 30.
        lump_word = Tex(r'ATC $+$ lump sum', color=ATC_COLOR).scale(CURVE_WORD_SCALE)
        lump_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                              .set_opacity(np.clip((lump.get_value() - 150) / 150, 0, 1)))
        self.remove(note)
        self.play(FadeOut(gov_word), run_time=0.4)
        self.play(tax.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        lump_row.update()
        lump_word.update()
        self.remove(tax_row, mc_tax_word, atc_tax_word)
        note = teaching('A lump-sum tax shifts only the average total cost.')
        self.add(lump_word)
        self.play(FadeIn(lump_row), FadeIn(note))
        self.play(lump.animate.set_value(LUMP_SUM), run_time=ROLL_TIME + 0.8, rate_func=smooth)
        self.pause('6.b.shift')

        # ---- 6.b · The band is the government's: the lump sum moves profit to the government.
        self.remove(note)
        note = teaching("This transfers some of the firm's profits to the government.")
        self.play(FadeIn(gov_word), FadeIn(note))
        self.pause('6.b')

        # ---- 6.c.shift · The lump sum comes off; a per-unit subsidy shifts MC and ATC down until q* reaches Q_sp.
        mc_subsidy_word = Tex(r'MC $-$ subsidy', color=MC_COLOR).scale(CURVE_WORD_SCALE)
        mc_subsidy_word.add_updater(lambda m: m.next_to(ax.c2p(policy_mc_end(), POLICY_TOP), RIGHT, buff=0.15)
                                    .set_opacity(np.clip((subsidy.get_value() - 6) / 6, 0, 1)))
        atc_subsidy_word = Tex(r'ATC $-$ subsidy', color=ATC_COLOR).scale(CURVE_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
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
        self.remove(lump_row, lump_word)
        note = teaching('Subsidies tend to increase the quantity exchanged in the market.')
        self.add(mc_subsidy_word, atc_subsidy_word)
        self.play(FadeIn(subsidy_row), FadeIn(note))
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
        both_word = Tex(r'ATC $-$ subsidy\\$+$ lump sum', color=ATC_COLOR).scale(CURVE_WORD_SCALE).set_backstroke(BG, 5).set_z_index(WORD_LAYER)
        both_word.room = 0.3                 # two lines under ATC's name: more room so they don't read as one stack
        both_word.add_updater(lambda m: m.next_to(ax.c2p(ATC_TO, policy_atc(ATC_TO)), RIGHT, buff=0.15).set_y(policy_name_y(m))
                              .set_opacity(np.clip((lump.get_value() - 300) / 300, 0, 1)))
        both_lump_row = lump_row.copy().clear_updaters()
        both_lump_row.add_updater(lambda m: (m[1].set_value(round(lump.get_value(), 4)), m.arrange(RIGHT, buff=POLICY_GAP),
                                             m.move_to(policy_left + DOWN * 0.45, aligned_edge=LEFT)))
        both_lump_row.update()
        both_word.update()
        self.remove(note)
        self.add(both_word)
        self.play(FadeIn(both_lump_row))
        self.play(lump.animate.set_value(LUMP_WITH_SUBSIDY), run_time=ROLL_TIME + 1.2, rate_func=smooth)
        note = teaching('No deadweight loss, positive government revenue, and less profit.')
        self.play(FadeIn(note))
        self.pause('6.d')

        # ---- 7.a · Next time: the taxonomy again, the box moving from Monopoly to the few-sellers cell (E4 opens there).
        for m in self.mobjects:
            m.update()                       # Digits current, then everything freezes before it fades.
            m.clear_updaters()
        self.remove(note)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not head], run_time=0.8)
        self.clear()
        self.add(head)
        box = SurroundingRectangle(monopoly, buff=BOX_BUFF, color=NASH)
        note = teaching('What happens with two sellers?')
        self.play(FadeIn(taxonomy), FadeIn(box))
        self.play(Transform(box, SurroundingRectangle(oligopoly, buff=BOX_BUFF, color=NASH)), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('7.a')
