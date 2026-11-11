# maniml E1_Animation.py EpisodeE1
# Teaching notes and current hold references: E1_Notes.md. Earlier storyboards are archived. All choreography stays in construct().
# Costs of Production: the market structures ahead, costs from the production function, the cost curves, MC = MR.
# One firm throughout: Q = F(L) = 10 sqrt(L) worker hours to units, a $100 wage and a $1,000 fixed cost, so VC = Q^2,
# TC = 1000 + Q^2, MC = 2Q, AVC = Q, AFC = 1000/Q, ATC = Q + 1000/Q (lowest at Q = sqrt(1000), about 31.6).
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


class EpisodeE1(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        READOUT_SCALE, CURVE_WORD_SCALE = 0.7, 0.7
        CURVE_WIDTH, GUIDE_WIDTH, BAR_STROKE, DOT_RADIUS = 3, 2, 7, 0.07
        GUIDE_LAYER, DOT_LAYER = 5, 10
        LIST_SCALE, LIST_STEP = 0.9, 0.78       # list rows: scale and baseline-to-baseline step
        ROW_SCALE, ROW_GAP = 0.9, 0.5
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Firm theory palette (shared_E.md). FC and AFC are MUTED lines; as words in equations they take CAPTION,
        # the text step of the same grey.
        MC_COLOR, MR_COLOR = SUPPLY, PINK
        TC_COLOR = ATC_COLOR = TOTAL
        VC_COLOR = AVC_COLOR = PINK
        FC_COLOR = AFC_COLOR = MUTED
        FC_WORD = CAPTION
        F_COLOR = INK
        # Layout: two square graphs side by side, production function left and cost graph right (guide §5).
        # The pan in 3.a slides both left by PAN, so the cost graph lands where the production function was.
        GRAPH_SIZE = 4.2
        LEFT_ORIGIN = np.array([-5.8, BODY_MID - 2.1, 0])
        RIGHT_ORIGIN = np.array([1.8, BODY_MID - 2.1, 0])
        PAN = RIGHT_ORIGIN[0] - LEFT_ORIGIN[0]
        DIVIDER_X = -0.55                      # grey divider right of the cost graph's curve words (3.d, 3.e)
        STEP_GAP, STEP_OFFSET, STEP_WIDTH = 0.04, 0.14, 3  # scene units; slim interval marks outside the axes
        MAX_BARS, BAR_OUTLINE = 60, 1.0         # B2 polygons: adjoining edges, colored outline, 35% fill
        # Taxonomy grid, E4's object: a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4
        BOX_BUFF = 0.12                          # keep each selection clear of the table rules

        # The model, as one-line functions. shape is the production function's exponent: 0.5 gives
        # F(L) = 10 sqrt(L). Keep that same technology throughout the production and cost views.
        WAGE, FIXED = 100, 1000
        shape = ValueTracker(0.5)
        output = lambda L: 100 * (L / 100) ** shape.get_value()             # Q = F(L)
        labor_for = lambda Q: 100 * (Q / 100) ** (1 / shape.get_value())    # the workers Q needs
        total = lambda Q: FIXED + WAGE * labor_for(Q)                       # TC = FC + w L
        COST_ALPHA = WAGE / 100
        variable = lambda Q: WAGE * labor_for(Q)
        mc = lambda Q: 2 * COST_ALPHA * Q
        avc = lambda Q: COST_ALPHA * Q
        atc = lambda Q: avc(Q) + FIXED / Q
        MIN_Q = np.sqrt(FIXED / COST_ALPHA)
        COST_Q_MAX, COST_X_MAX = 60, 70
        TOTAL_MAX, AVERAGE_MAX = 5000, 1.2 * mc(COST_Q_MAX)
        AVERAGE_TOP = 0.875 * AVERAGE_MAX
        ATC_START = (AVERAGE_TOP - np.sqrt(AVERAGE_TOP**2 - 4*COST_ALPHA*FIXED)) / (2*COST_ALPHA)
        AFC_START = FIXED / AVERAGE_TOP

        # The two object factories: the yellow bottom line, and a numbered list whose rows sit on evenly spaced
        # baselines (arrange spaces bounding boxes, so a descender would widen one gap).
        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        def numbered(*items):
            rows = VGroup()
            for i, item in enumerate(items):
                row = Tex(rf'{i + 1}.\enspace {item}').scale(LIST_SCALE).align_to(ORIGIN, LEFT)
                row.shift(UP * (-i * LIST_STEP - row.family_members_with_points()[0].get_bottom()[1]))  # the digit's baseline
                rows.add(row)
            return rows.move_to([0, BODY_MID, 0])

        # ---- 0.a · The shared bumper with E1's subtitle, Costs of Production (Taylor, 2026-11-04).
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 1)
        thesis = Tex(r'\textit{Costs of Production}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · The three questions, each on screen in turn, in his words.
        head = title('How Sellers Choose')
        questions = numbered('How much to make?', 'How many workers to hire?', 'How to set prices?').align_to(head, LEFT)
        self.play(FadeIn(head), FadeIn(questions[0]))
        self.play(FadeIn(questions[1]))
        self.play(FadeIn(questions[2]))
        self.pause('1.a')

        # ---- 1.b · The supply curve we have relied on, labeled S / MC.
        supply_ax = style_axes([0, 10, 1], [0, 10, 1], x_length=3.6, y_length=3.6)
        supply_ax.shift(np.array([1.0, BODY_MID - 1.8, 0]) - supply_ax.c2p(0, 0))
        supply_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(supply_ax.c2p(0, 10), LEFT, buff=0.25),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(0, 10), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.35),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.73))
        supply_words[1].next_to(supply_words[0], RIGHT, buff=0.35)
        supply_words[3].next_to(supply_words[2], RIGHT, buff=0.3)
        supply_line = Line(supply_ax.c2p(0, 2), supply_ax.c2p(10, 8), color=SUPPLY, stroke_width=CURVE_WIDTH)
        supply_word = Tex('S / MC', color=INK).scale(CURVE_WORD_SCALE).next_to(supply_ax.c2p(10, 8), RIGHT, buff=0.15)
        note = teaching('What are the incentives that give rise to the supply curve?')
        self.play(FadeIn(supply_ax), FadeIn(supply_words), FadeIn(supply_line), FadeIn(supply_word))
        self.play(FadeIn(note))
        self.pause('1.b')

        # ---- 1.c · The market-structures taxonomy (E4's object), its four cells still empty.
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])   # trackers join the scene when animated
        FadeAll(self)
        self.clear()
        head = title('Market Structures')
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
        grid = VGroup(taxonomy_rules, column_words, row_words)
        cells = VGroup(perfect, monopolistic, oligopoly, monopoly)
        self.play(FadeIn(head), FadeIn(grid))
        self.pause('1.c')

        # ---- 1.d · Keep the full-size matrix and its title; fill and select perfect competition.
        box = SurroundingRectangle(perfect, buff=BOX_BUFF, color=NASH)
        self.play(FadeIn(perfect), FadeIn(box), run_time=0.8)
        self.pause('1.d')

        # ---- 1.e · Reveal monopoly in the one-seller row and move the same selection box.
        self.play(FadeIn(monopoly), Transform(box, SurroundingRectangle(monopoly, buff=BOX_BUFF, color=NASH)),
                  run_time=0.8, rate_func=smooth)
        self.pause('1.e')

        # ---- 1.f · Reveal monopolistic competition; earlier entries remain in the matrix.
        self.play(FadeIn(monopolistic), Transform(box, SurroundingRectangle(monopolistic, buff=BOX_BUFF, color=NASH)),
                  run_time=0.8, rate_func=smooth)
        self.pause('1.f')

        # ---- 1.g · Complete the matrix with oligopoly, keeping the same frame and title.
        self.play(FadeIn(oligopoly), Transform(box, SurroundingRectangle(oligopoly, buff=BOX_BUFF, color=NASH)),
                  run_time=0.8, rate_func=smooth)
        self.pause('1.g')

        # ---- 2.a · The production function on the left: workers across, units up, F(L) in white.
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])   # trackers join the scene when animated
        FadeAll(self)
        self.clear()
        head = title('Costs From The Production Function')
        production_subtitle = subtitle(head, 'One example of a production function with diminishing marginal product.')
        f_ax = style_axes([0, 100, 10], [0, 100, 10], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        f_ax.shift(LEFT_ORIGIN - f_ax.c2p(0, 0))
        f_words = VGroup(
            Tex('Q', color=INK).scale(0.8).next_to(f_ax.c2p(0, 100), LEFT, buff=0.25),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(0, 100), RIGHT, buff=0.22).shift(UP * 0.30),
            Tex('L', color=INK).scale(0.8).next_to(f_ax.c2p(100, 0), DOWN, buff=0.35),
            Tex(r'\textsf{worker hours}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(100, 0), DOWN, buff=0.73))
        f_words[1].next_to(f_words[0], RIGHT, buff=0.35)
        f_words[3].next_to(f_words[2], RIGHT, buff=0.3)
        # Sampled densely near zero, where the square root is steep; redrawn from shape every frame.
        f_curve = polyline([f_ax.c2p(100 * t ** 2, output(100 * t ** 2)) for t in np.linspace(0, 1, 121)], F_COLOR, CURVE_WIDTH)
        f_curve.add_updater(lambda m: m.set_points_as_corners(
            [f_ax.c2p(100 * t ** 2, output(100 * t ** 2)) for t in np.linspace(0, 1, 121)]))
        f_word = Tex('$F(L)$', color=INK).scale(CURVE_WORD_SCALE).next_to(f_ax.c2p(100, 100), RIGHT, buff=0.15)
        self.play(FadeIn(head), FadeIn(production_subtitle), FadeIn(f_ax), FadeIn(f_words), FadeIn(f_curve), FadeIn(f_word))
        self.pause('2.a')

        # ---- 2.b · Choose 20 units of output, trace across to F, then down to the 4 labor hours required.
        output_level = ValueTracker(20)
        work_across = DashedLine(f_ax.c2p(0, 20), f_ax.c2p(4, 20), color=GUIDE, stroke_width=GUIDE_WIDTH)
        work_across.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(0, output_level.get_value()), f_ax.c2p(labor_for(output_level.get_value()), output_level.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        work_dot = Dot(f_ax.c2p(4, 20), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        work_dot.add_updater(lambda m: m.move_to(f_ax.c2p(labor_for(output_level.get_value()), output_level.get_value())))
        work_up = DashedLine(f_ax.c2p(4, 20), f_ax.c2p(4, 0), color=GUIDE, stroke_width=GUIDE_WIDTH)
        work_up.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(labor_for(output_level.get_value()), output_level.get_value()), f_ax.c2p(labor_for(output_level.get_value()), 0),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        work_number = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        work_number.add_updater(lambda m: m.set_value(round(labor_for(output_level.get_value()), 4))
                                .move_to(f_ax.c2p(labor_for(output_level.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        made_number = DecimalNumber(20, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        made_number.add_updater(lambda m: m.set_value(round(output_level.get_value(), 4))
                                .next_to(f_ax.c2p(0, output_level.get_value()), LEFT, buff=0.2))
        labor_marks = [work_up, work_dot, work_across, work_number, made_number]
        for m in labor_marks:
            m.update()
        note = teaching('Choose an output quantity; find the labor hours it requires.')
        self.play(FadeIn(made_number), FadeIn(note))
        self.play(Create(work_across), FadeIn(work_dot))
        self.play(Create(work_up), FadeIn(work_number))
        self.pause('2.b')

        # ---- 2.c · Output drives the motion; both readouts remain attached to the same point.
        self.remove(note)
        note = teaching('Increasing output means we need more inputs, either from labor or capital.')
        self.play(FadeIn(note), output_level.animate.set_value(30), run_time=ROLL_TIME, rate_func=smooth)
        self.play(output_level.animate.set_value(20), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.c')

        output_steps, input_steps = [(20, 40), (40, 60)], [(4, 16), (16, 36)]
        input_braces = VGroup(*[Line(f_ax.c2p(a, 0) + RIGHT * STEP_GAP + DOWN * STEP_OFFSET,
                                     f_ax.c2p(b, 0) + LEFT * STEP_GAP + DOWN * STEP_OFFSET,
                                     color=CAPTION, stroke_width=STEP_WIDTH) for a, b in input_steps])
        output_braces = VGroup(*[Line(f_ax.c2p(0, a) + UP * STEP_GAP + LEFT * STEP_OFFSET,
                                      f_ax.c2p(0, b) + DOWN * STEP_GAP + LEFT * STEP_OFFSET,
                                      color=CAPTION, stroke_width=STEP_WIDTH) for a, b in output_steps])
        input_differences = VGroup(*[Tex(f'+{b-a}', color=CAPTION).scale(0.55)
            .move_to(f_ax.c2p((a+b)/2, 0) + DOWN * 0.75) for a, b in input_steps])
        output_differences = VGroup(*[Tex(f'+{b-a}', color=CAPTION).scale(0.55)
            .next_to(output_braces[i], LEFT, buff=0.18) for i, (a, b) in enumerate(output_steps)])

        # ---- 2.d · Double output to 40: across first, then down to 16 labor hours.
        for m in labor_marks:
            m.update()
            m.clear_updaters()
        double_across = DashedLine(f_ax.c2p(0, 40), f_ax.c2p(16, 40), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        double_dot = Dot(f_ax.c2p(16, 40), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        double_up = DashedLine(f_ax.c2p(16, 40), f_ax.c2p(16, 0), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        double_work = Tex('16', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(f_ax.c2p(16, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        double_made = Tex('40', color=GUIDE).scale(READOUT_SCALE).next_to(f_ax.c2p(0, 40), LEFT, buff=0.2)
        self.remove(note)
        note = teaching('Doubling output from 20 to 40 requires four times the labor.')
        self.play(FadeIn(double_made), Create(double_across), FadeIn(double_dot), FadeIn(note),
                  FadeIn(output_braces[0]), FadeIn(output_differences[0]))
        self.play(Create(double_up), FadeIn(double_work), FadeIn(input_braces[0]), FadeIn(input_differences[0]))
        self.pause('2.d')

        # ---- 2.e · Add another 20 units: 60 output units require 36 labor hours.
        triple_across = DashedLine(f_ax.c2p(0, 60), f_ax.c2p(36, 60), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        triple_dot = Dot(f_ax.c2p(36, 60), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        triple_up = DashedLine(f_ax.c2p(36, 60), f_ax.c2p(36, 0), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        triple_work = Tex('36', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(f_ax.c2p(36, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        triple_made = Tex('60', color=GUIDE).scale(READOUT_SCALE).next_to(f_ax.c2p(0, 60), LEFT, buff=0.2)
        self.remove(note)
        note = teaching('Another 20 units require 20 more labor hours.')
        self.play(FadeIn(triple_made), Create(triple_across), FadeIn(triple_dot), FadeIn(note),
                  FadeIn(output_braces[1]), FadeIn(output_differences[1]))
        self.play(Create(triple_up), FadeIn(triple_work), FadeIn(input_braces[1]), FadeIn(input_differences[1]))
        self.pause('2.e')

        # ---- 2.f · Keep both interval pairs, already revealed with their corresponding output/labor steps.
        self.remove(note)
        note = teaching('More output requires increasingly large additions to labor.')
        self.play(FadeIn(note))
        self.pause('2.f')

        # ---- 2.g · Revisit each output/labor pair without moving or resizing the interval marks.
        self.remove(note)
        note = teaching('Equal additions to output require increasingly more labor.')
        self.play(FadeIn(note))
        for i in range(2):
            self.play(Indicate(input_braces[i], color=FOCUS, scale_factor=1),
                      Indicate(output_braces[i], color=FOCUS, scale_factor=1), run_time=0.8)
        self.pause('2.g')

        # ---- 2.h · Wages: variable cost is the labor hours times the wage, on the right where the cost graph will go.
        wage_equation = MathTex(r'{{\mathrm{VC}}} = L \cdot w').scale(1.1)
        wage_equation.get_part_by_tex(r'\mathrm{VC}').set_color(VC_COLOR)
        wage_equation.move_to([3.9, BODY_MID, 0])
        self.remove(note)
        note = teaching('The costs going to wages: just the labor hours times the wages.')
        self.play(FadeIn(wage_equation), FadeIn(note))
        self.pause('2.h')

        # ---- 2.i.capital · Capital's cost joins the equation...
        capital = MathTex(r'+\, K \cdot r').scale(1.1).next_to(wage_equation, RIGHT, buff=0.2).align_to(wage_equation, DOWN)
        self.remove(note)
        note = teaching("There's also capital cost we need to think about in practice.")
        self.play(FadeIn(capital), FadeIn(note))
        self.pause('2.i.capital')

        # ---- 2.i · ...and fades out again: labor costs only.
        self.remove(note)
        note = teaching("To keep things simple here, we're going to focus on labor costs.")
        self.play(FadeOut(capital), FadeIn(note))
        self.pause('2.i')

        # ---- 2.j · Keep the production scale. Start the cost graph with the first unit's fixed-cost base.
        step_marks = VGroup(*labor_marks, double_up, double_dot, double_across, double_work, double_made,
                            triple_up, triple_dot, triple_across, triple_work, triple_made, input_braces, output_braces,
                            input_differences, output_differences)
        f_curve.clear_updaters()
        f_curve.set_z_index(GUIDE_LAYER)
        BUILD_UNITS, BUILD_X_MAX, BUILD_COST_MAX = COST_Q_MAX, COST_X_MAX, TOTAL_MAX
        shown = ValueTracker(1)
        cost_x_span, cost_y_span = ValueTracker(1.2), ValueTracker(1200)
        vc_reveal = ValueTracker(0)
        cost_ax = style_axes([0, COST_X_MAX, 10], [0, TOTAL_MAX, 1000], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        cost_ax.shift(RIGHT_ORIGIN - cost_ax.c2p(0, 0))
        cp = lambda Q, C: cost_ax.c2p(COST_X_MAX*Q/cost_x_span.get_value(), TOTAL_MAX*C/cost_y_span.get_value())
        cost_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(cost_ax.c2p(0, TOTAL_MAX), LEFT, buff=0.25),
            Tex(r'\textsf{dollars}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(0, TOTAL_MAX), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(cost_ax.c2p(COST_X_MAX, 0), DOWN, buff=0.35),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(COST_X_MAX, 0), DOWN, buff=0.73))
        cost_words[1].next_to(cost_words[0], RIGHT, buff=0.35)
        cost_words[3].next_to(cost_words[2], RIGHT, buff=0.3)
        stored_wage = subtitle(head, rf'Wage: \${WAGE} per hour', book=True)
        first_heading = Tex('First unit', color=CAPTION).scale(0.65).move_to([3.9, 2.5, 0])
        hour_bars = VGroup(*[Polygon(f_ax.c2p(0, Q-1), f_ax.c2p(labor_for(Q), Q-1),
            f_ax.c2p(labor_for(Q), Q), f_ax.c2p(0, Q),
            color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            for Q in range(1, BUILD_UNITS+1)])
        fixed_bars, cost_bars = VGroup(), VGroup()
        for Q in range(1, BUILD_UNITS+1):
            fixed = Polygon(ORIGIN, RIGHT, UR, UP, color=FC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            fixed.add_updater(lambda m, Q=Q: m.set_points_as_corners([
                cp(Q-1, 0), cp(Q, 0), cp(Q, FIXED), cp(Q-1, FIXED), cp(Q-1, 0)])
                .set_stroke(FC_COLOR, BAR_OUTLINE, opacity=float(Q <= shown.get_value()+1e-6))
                .set_fill(FC_COLOR, AREA_OPACITY if Q <= shown.get_value()+1e-6 else 0))
            costs = Polygon(ORIGIN, RIGHT, UR, UP, color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            costs.add_updater(lambda m, Q=Q: m.set_points_as_corners([
                cp(Q-1, FIXED), cp(Q, FIXED), cp(Q, total(Q)), cp(Q-1, total(Q)), cp(Q-1, FIXED)])
                .set_stroke(VC_COLOR, BAR_OUTLINE, opacity=vc_reveal.get_value()*float(Q <= shown.get_value()+1e-6))
                .set_fill(VC_COLOR, AREA_OPACITY*vc_reveal.get_value() if Q <= shown.get_value()+1e-6 else 0))
            fixed_bars.add(fixed)
            cost_bars.add(costs)
        fc_line = Line(cp(0, FIXED), cp(cost_x_span.get_value(), FIXED), color=FC_COLOR, stroke_width=CURVE_WIDTH).set_z_index(GUIDE_LAYER)
        fc_line.add_updater(lambda m: m.put_start_and_end_on(cp(0, FIXED), cp(cost_x_span.get_value(), FIXED)))
        fc_word = Tex('FC', color=INK).scale(CURVE_WORD_SCALE)
        fc_word.add_updater(lambda m: m.next_to(cp(cost_x_span.get_value(), FIXED), RIGHT, buff=0.15))
        fc_number = Tex('1,000', color=CAPTION).scale(READOUT_SCALE)
        fc_number.add_updater(lambda m: m.next_to(cp(0, FIXED), LEFT, buff=0.2))
        first_fixed = Tex(r'FC: \$1,000', color=CAPTION).scale(0.62).next_to(cp(1, FIXED/2), RIGHT, buff=0.15)
        first_variable = Tex(r'VC: \$1', color=VC_COLOR).scale(0.62).next_to(cp(1, total(1)), RIGHT, buff=0.15).shift(UP*0.25)

        # One quantity drives both graphs. Fixed dash pools remain safe at tiny labor quantities.
        trace_labor = lambda: labor_for(shown.get_value())
        production_point = lambda: f_ax.c2p(trace_labor(), shown.get_value())
        cost_point = lambda: cp(shown.get_value(), total(shown.get_value()))
        trace_dot = Dot(production_point(), radius=DOT_RADIUS, color=GUIDE)
        trace_dot.add_updater(lambda m: m.move_to(production_point()))
        trace_output = DecimalNumber(1, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        trace_output.add_updater(lambda m: m.set_value(round(shown.get_value(), 4))
            .next_to(f_ax.c2p(0, shown.get_value()), LEFT, buff=0.2))
        trace_hours = DecimalNumber(0.01, num_decimal_places=2, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        trace_hours.add_updater(lambda m: m.set_value(round(trace_labor(), 4))
            .move_to(f_ax.c2p(trace_labor(), 0)+DOWN*QUANTITY_NUMBER_OFFSET))
        cost_dot = Dot(cost_point(), radius=DOT_RADIUS, color=GUIDE)
        cost_dot.add_updater(lambda m: m.move_to(cost_point()))
        trace_quantity = DecimalNumber(1, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        trace_quantity.add_updater(lambda m: m.set_value(round(shown.get_value(), 4))
            .move_to(cp(shown.get_value(), 0)+DOWN*QUANTITY_NUMBER_OFFSET))
        trace_total = DecimalNumber(total(1), num_decimal_places=0, group_with_commas=True, color=GUIDE).scale(READOUT_SCALE)
        trace_total.add_updater(lambda m: m.set_value(round(total(shown.get_value()), 4))
            .next_to(cp(0, total(shown.get_value())), LEFT, buff=0.2)
            .shift(UP*max(0, 0.35-(cp(0, total(shown.get_value()))[1]-cp(0, FIXED)[1]))))
        trace_guides = []
        for start, length, direction in (
            (lambda: f_ax.c2p(0, shown.get_value()), lambda: GRAPH_SIZE*trace_labor()/100, RIGHT),
            (lambda: f_ax.c2p(trace_labor(), 0), lambda: GRAPH_SIZE*shown.get_value()/100, UP),
            (lambda: cp(0, total(shown.get_value())), lambda: GRAPH_SIZE*shown.get_value()/cost_x_span.get_value(), RIGHT),
            (lambda: cp(shown.get_value(), 0), lambda: GRAPH_SIZE*total(shown.get_value())/cost_y_span.get_value(), UP)):
            guide = VGroup(*[Line(ORIGIN, direction, color=GUIDE, stroke_width=GUIDE_WIDTH)
                for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
            guide.add_updater(lambda group, start=start, length=length, direction=direction: [dash.set_points_as_corners([
                start()+direction*min(i*0.1, length()), start()+direction*min(i*0.1+0.05, length())])
                .set_opacity(float(i*0.1 < length())) for i, dash in enumerate(group)])
            trace_guides.append(guide)
        production_marks = VGroup(*trace_guides[:2], trace_dot, trace_output, trace_hours).set_z_index(DOT_LAYER)
        cost_marks = VGroup(*trace_guides[2:], cost_dot, trace_quantity, trace_total).set_z_index(DOT_LAYER)
        for group in (fixed_bars, cost_bars, production_marks, cost_marks, fc_line, fc_word, fc_number):
            group.update()
        self.remove(note)
        note = teaching(r'Even the first unit includes \$1,000 in fixed cost.')
        self.play(FadeOut(step_marks), FadeOut(wage_equation), FadeOut(production_subtitle),
                  FadeIn(stored_wage), FadeIn(cost_ax), FadeIn(cost_words), FadeIn(first_heading), FadeIn(note), run_time=0.7)
        self.add(fixed_bars, cost_bars, hour_bars[0])
        self.play(FadeIn(production_marks), FadeIn(first_fixed), FadeIn(fc_number), Create(fc_line), run_time=0.7)
        self.pause('2.j')

        # ---- 2.k · The first unit's labor becomes its variable-cost cap; keep the numerical sum explicit.
        self.remove(note)
        note = teaching(r'One unit: \$1 in labor cost, plus \$1,000 in fixed cost.')
        self.play(vc_reveal.animate.set_value(1), TransformFromCopy(trace_hours, first_variable),
                  FadeIn(cost_marks), FadeIn(note), run_time=1.0, rate_func=smooth)
        self.pause('2.k')

        # ---- 2.l · Settle the cost scale once. The production graph never changes scale.
        self.play(FadeOut(first_heading), FadeOut(first_fixed), FadeOut(first_variable), run_time=0.4)
        self.remove(note)
        note = teaching('Now follow the same output quantities: 20, 40, and 60.')
        self.play(cost_x_span.animate.set_value(BUILD_X_MAX), cost_y_span.animate.set_value(BUILD_COST_MAX),
                  FadeIn(note), run_time=1.8, rate_func=smooth)
        self.play(FadeIn(fc_word), run_time=0.4)
        self.pause('2.l')

        # Freeze the mapping before adding units. Each completed bar stays at its own quantity.
        for group in (fixed_bars, cost_bars):
            group.update()
            group.clear_updaters(recurse=True)
        self.remove(fixed_bars, cost_bars)
        self.add(fixed_bars[0], cost_bars[0])
        for bar in fixed_bars:
            bar.set_stroke(FC_COLOR, BAR_OUTLINE, opacity=1).set_fill(FC_COLOR, AREA_OPACITY)
        for bar in cost_bars:
            bar.set_stroke(VC_COLOR, BAR_OUTLINE, opacity=1).set_fill(VC_COLOR, AREA_OPACITY)

        # ---- 2.l.five · Finish the first five units individually before continuing the same transfer.
        self.remove(note)
        note = teaching('Labor hours become variable cost at the same wage.')
        self.play(FadeIn(note))
        for Q in range(2, 6):
            self.play(shown.animate.set_value(Q), FadeIn(hour_bars[Q-1]),
                      hour_bars[Q-2].animate.set_stroke(MUTED, opacity=0.35).set_fill(MUTED, 0.10),
                      run_time=0.45, rate_func=smooth)
            self.play(FadeIn(fixed_bars[Q-1]), TransformFromCopy(hour_bars[Q-1], cost_bars[Q-1]),
                      run_time=0.65, rate_func=smooth)
        self.pause('2.l.five')

        # ---- 2.m · Transfer every unit, not a handful of representative bars. Both scales stay fixed.
        for Q in range(6, 21):
            self.play(shown.animate.set_value(Q), FadeIn(hour_bars[Q-1]),
                      hour_bars[Q-2].animate.set_stroke(MUTED, opacity=0.35).set_fill(MUTED, 0.10),
                      run_time=0.2, rate_func=smooth)
            self.play(FadeIn(fixed_bars[Q-1]), TransformFromCopy(hour_bars[Q-1], cost_bars[Q-1]),
                      run_time=0.3, rate_func=smooth)
        self.remove(note)
        note = teaching(r'20 units need 4 labor hours: \$400 in variable cost.')
        self.play(FadeIn(note))
        self.pause('2.m')

        # ---- 2.n · Continue unit by unit to the second familiar output level.
        self.remove(note)
        note = teaching('Each additional unit requires more labor than the one before.')
        self.play(FadeIn(note))
        for Q in range(21, 41):
            self.play(shown.animate.set_value(Q), FadeIn(hour_bars[Q-1]),
                      hour_bars[Q-2].animate.set_stroke(MUTED, opacity=0.35).set_fill(MUTED, 0.10),
                      run_time=0.2, rate_func=smooth)
            self.play(FadeIn(fixed_bars[Q-1]), TransformFromCopy(hour_bars[Q-1], cost_bars[Q-1]),
                      run_time=0.3, rate_func=smooth)
        self.remove(note)
        note = teaching(r'The next 20 units need 12 more hours: \$1,200 more cost.')
        self.play(FadeIn(note))
        self.pause('2.n')

        # ---- 2.o · Sixty adjoining one-unit bars, with no zoom or regrouping during the buildup.
        self.remove(note)
        note = teaching('More labor for the next unit means a higher cost of producing it.')
        self.play(FadeIn(note))
        for Q in range(41, BUILD_UNITS+1):
            self.play(shown.animate.set_value(Q), FadeIn(hour_bars[Q-1]),
                      hour_bars[Q-2].animate.set_stroke(MUTED, opacity=0.35).set_fill(MUTED, 0.10),
                      run_time=0.2, rate_func=smooth)
            self.play(FadeIn(fixed_bars[Q-1]), TransformFromCopy(hour_bars[Q-1], cost_bars[Q-1]),
                      run_time=0.3, rate_func=smooth)
        for group in (production_marks, cost_marks, fc_line, fc_word, fc_number):
            group.update()
            group.clear_updaters(recurse=True)
        self.add(hour_bars, fixed_bars, cost_bars)
        self.remove(note)
        note = teaching(r'The next 20 units need 20 more hours: \$2,000 more cost.')
        self.play(FadeIn(note))
        self.pause('2.o')

        # ---- 2.p · Draw TC along the settled bar tops. FC has been present since the first unit.
        self.remove(note)
        note = teaching('More labor for each additional unit means increasing marginal cost.')
        tc_curve = polyline([cp(q, total(q)) for q in np.linspace(0, BUILD_UNITS, 121)], TC_COLOR, CURVE_WIDTH).set_z_index(DOT_LAYER)
        tc_word = Tex('TC', color=INK).scale(CURVE_WORD_SCALE).next_to(cp(BUILD_UNITS, total(BUILD_UNITS)), RIGHT, buff=0.15)
        self.play(FadeOut(production_marks), FadeOut(cost_marks), FadeIn(note), run_time=0.5)
        self.play(Create(tc_curve), FadeIn(tc_word), run_time=1.5)
        self.pause('2.p')

        # ---- 3.a · A translation only: preserve the scale, curve, FC height, and all sixty cost bars.
        self.remove(head, stored_wage, note)
        head = title('Cost Curves')
        production = VGroup(f_ax, f_words, f_curve, f_word, hour_bars)
        costs = VGroup(cost_ax, cost_words, tc_curve, tc_word, fc_line, fc_word, fc_number)
        self.play(FadeIn(head), production.animate.shift(LEFT*PAN), costs.animate.shift(LEFT*PAN),
                  cost_bars.animate.shift(LEFT*PAN).set_stroke(MUTED, opacity=0.25).set_fill(MUTED, 0.08),
                  fixed_bars.animate.shift(LEFT*PAN).set_stroke(MUTED, opacity=0.25).set_fill(MUTED, 0.08),
                  run_time=2, rate_func=smooth)
        self.remove(production, *[m for m in self.mobjects if isinstance(m, ValueTracker)])
        self.pause('3.a')

        # ---- 3.b · FC is already present; only its teaching line enters.
        note = teaching("Fixed costs, like rent, don't vary with inputs.")
        self.play(FadeIn(note))
        self.pause('3.b')

        # ---- 3.c · Stationary cost bands; only the active highlight switches while the dot and guides move.
        rest_cost_bars = VGroup(*[Polygon(cost_ax.c2p(q-1, 0), cost_ax.c2p(q, 0),
            cost_ax.c2p(q, total(q)), cost_ax.c2p(q-1, total(q)),
            color=MUTED, stroke_width=1, stroke_opacity=0.25, fill_color=MUTED, fill_opacity=0.08)
            for q in range(1, MAX_BARS+1)])
        self.remove(cost_bars, fixed_bars)
        bar_q = ValueTracker(50)
        selected_bar = lambda: max(0, min(MAX_BARS-1, int(np.ceil(bar_q.get_value()))-1))
        bar_fixed, bar_variable = VGroup(), VGroup()
        for i, right in enumerate(range(1, MAX_BARS+1)):
            fixed = Polygon(cost_ax.c2p(right-1, 0), cost_ax.c2p(right, 0),
                cost_ax.c2p(right, FIXED), cost_ax.c2p(right-1, FIXED),
                color=FC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            fixed.add_updater(lambda m, i=i: m.set_stroke(FC_COLOR, BAR_OUTLINE, opacity=float(i == selected_bar()))
                .set_fill(FC_COLOR, AREA_OPACITY if i == selected_bar() else 0))
            variable_bar = Polygon(cost_ax.c2p(right-1, FIXED), cost_ax.c2p(right, FIXED),
                cost_ax.c2p(right, total(right)), cost_ax.c2p(right-1, total(right)),
                color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            variable_bar.add_updater(lambda m, i=i: m.set_stroke(VC_COLOR, BAR_OUTLINE, opacity=float(i == selected_bar()))
                .set_fill(VC_COLOR, AREA_OPACITY if i == selected_bar() else 0))
            bar_fixed.add(fixed)
            bar_variable.add(variable_bar)
        bar_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE)
        bar_word.add_updater(lambda m: m.next_to(bar_variable[selected_bar()], RIGHT, buff=0.12))
        bar_across = DashedLine(cost_ax.c2p(50, total(50)), cost_ax.c2p(0, total(50)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        bar_across.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(bar_q.get_value(), total(bar_q.get_value())), cost_ax.c2p(0, total(bar_q.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        bar_dot = Dot(cost_ax.c2p(50, total(50)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        bar_dot.add_updater(lambda m: m.move_to(cost_ax.c2p(bar_q.get_value(), total(bar_q.get_value()))))
        bar_total = DecimalNumber(total(50), num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        bar_total.add_updater(lambda m: m.set_value(round(total(bar_q.get_value()), 4))
            .next_to(cost_ax.c2p(0, total(bar_q.get_value())), LEFT, buff=0.2))
        bar_quantity = DecimalNumber(50, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        bar_quantity.add_updater(lambda m: m.set_value(round(bar_q.get_value(), 4))
            .move_to(cost_ax.c2p(bar_q.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        bar_guides = VGroup(bar_across, bar_dot, bar_total, bar_quantity)
        bar_marks = [bar_fixed, bar_variable, bar_word, bar_across, bar_dot, bar_total, bar_quantity]
        for m in bar_marks:
            m.update()
        self.remove(note)
        note = teaching('Variable costs are the costs that do change with inputs.')
        self.play(FadeIn(rest_cost_bars), *[FadeIn(m) for m in bar_marks], FadeIn(note))
        self.play(bar_q.animate.set_value(58), run_time=ROLL_TIME, rate_func=smooth)
        self.play(bar_q.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.c')

        # ---- 3.d · Keep the cost bands; the pink portion above FC explains TC = VC + FC.
        for m in bar_marks:
            m.update()
            m.clear_updaters(recurse=True)
        vc_curve = polyline([cost_ax.c2p(q, variable(q)) for q in np.linspace(0, COST_Q_MAX, 121)], VC_COLOR, CURVE_WIDTH)
        vc_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(COST_Q_MAX, variable(COST_Q_MAX)), RIGHT, buff=0.15)
        divider = Line([DIVIDER_X, -3.0, 0], [DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        sum_row = MathTex(r'{{\mathrm{TC}}} = {{\mathrm{VC}}} + {{\mathrm{FC}}}')
        divided_row = MathTex(r'{{\frac{\mathrm{TC}}{Q}}} = {{\frac{\mathrm{VC}}{Q}}} + {{\frac{\mathrm{FC}}{Q}}}')
        average_row = MathTex(r'{{\mathrm{ATC}}} = {{\mathrm{AVC}}} + {{\mathrm{AFC}}}')
        for row, parts in [(sum_row, (r'\mathrm{FC}', r'\mathrm{VC}', r'\mathrm{TC}')),
                           (divided_row, (r'\frac{\mathrm{FC}}{Q}', r'\frac{\mathrm{VC}}{Q}', r'\frac{\mathrm{TC}}{Q}')),
                           (average_row, (r'\mathrm{AFC}', r'\mathrm{AVC}', r'\mathrm{ATC}'))]:
            for part, color in zip(parts, (FC_WORD, VC_COLOR, TC_COLOR)):
                row.get_part_by_tex(part).set_color(color)
        accounting = VGroup(sum_row, divided_row, average_row).scale(ROW_SCALE).arrange(DOWN, buff=ROW_GAP)
        accounting.move_to([(DIVIDER_X + 7.4) / 2, BODY_MID, 0])
        self.remove(note)
        note = teaching('Total cost is the sum of fixed and variable costs.')
        self.play(FadeOut(bar_word), FadeOut(bar_guides), FadeIn(divider), FadeIn(sum_row), FadeIn(note))
        self.pause('3.d')

        # ---- 3.e.divide · Divide every cost by the quantity...
        self.remove(note)
        note = teaching('We find average costs simply by dividing these costs by the quantity.')
        self.play(FadeIn(divided_row), FadeIn(note))
        self.pause('3.e.divide')

        # ---- 3.e · ...to get the three average costs.
        self.play(FadeIn(average_row))
        self.pause('3.e')

        # ---- 3.f.setup · Place both identities above their graphs, then pause.
        # Teach AVC, AFC, then ATC, retaining each concept's existing pause ID.
        # One quantity tracker drives both points, their guides, and the curve endpoint.
        avg_ax = style_axes([0, COST_X_MAX, 10], [0, AVERAGE_MAX, 20], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        avg_ax.shift(RIGHT_ORIGIN - avg_ax.c2p(0, 0))
        avg_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(avg_ax.c2p(0, AVERAGE_MAX), LEFT, buff=0.25),
            Tex(r'\textsf{dollars per unit}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(0, AVERAGE_MAX), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(avg_ax.c2p(COST_X_MAX, 0), DOWN, buff=0.35),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(COST_X_MAX, 0), DOWN, buff=0.73))
        avg_words[1].next_to(avg_words[0], RIGHT, buff=0.35)
        avg_words[3].next_to(avg_words[2], RIGHT, buff=0.3)
        stored_total = sum_row.copy().scale(0.72/ROW_SCALE).move_to(cost_ax.c2p(COST_X_MAX/2, TOTAL_MAX)+UP*0.58)
        stored_average = average_row.copy().scale(0.72/ROW_SCALE).move_to(avg_ax.c2p(COST_X_MAX/2, AVERAGE_MAX)+UP*0.58)
        self.remove(note)
        self.play(FadeOut(divider), Transform(sum_row, stored_total), FadeOut(divided_row), FadeOut(bar_fixed), FadeOut(bar_variable),
                  Transform(average_row, stored_average), FadeIn(avg_ax), FadeIn(avg_words), run_time=1.2)
        self.remove(sum_row, average_row)
        self.add(stored_total, stored_average)
        self.pause('3.f.setup')
        divided = {'cost': variable, 'average': avc}
        per_unit = ValueTracker(0)
        cost_now = lambda: divided['cost'](per_unit.get_value())            # the cost being divided, at the point
        # Average cost is undefined at Q=0 and above the visible range for very small quantities.
        fc_number.add_updater(lambda m: m.set_opacity(0.22*float(abs(cost_now()-FIXED) > TOTAL_MAX*0.07)))
        self.add(fc_number)
        average_now = lambda: divided['average'](per_unit.get_value()) if per_unit.get_value() > 0 else AVERAGE_TOP
        average_visible = lambda: per_unit.get_value() > 0 and average_now() <= AVERAGE_TOP
        average_display = lambda: min(AVERAGE_TOP, max(0, average_now()))
        div_up = VGroup(*[Line(ORIGIN, UP, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        div_up.add_updater(lambda group: [dash.set_points_as_corners([
            cost_ax.c2p(per_unit.get_value(), 0)+UP*min(i*0.1, GRAPH_SIZE*cost_now()/TOTAL_MAX),
            cost_ax.c2p(per_unit.get_value(), 0)+UP*min(i*0.1+0.05, GRAPH_SIZE*cost_now()/TOTAL_MAX)])
            .set_opacity(float(i*0.1 < GRAPH_SIZE*cost_now()/TOTAL_MAX)) for i, dash in enumerate(group)])
        div_point = Dot(cost_ax.c2p(0, total(0)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        div_point.add_updater(lambda m: m.move_to(cost_ax.c2p(per_unit.get_value(), cost_now())))
        div_across = VGroup(*[Line(ORIGIN, RIGHT, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        div_across.add_updater(lambda group: [dash.set_points_as_corners([
            cost_ax.c2p(0, cost_now())+RIGHT*min(i*0.1, GRAPH_SIZE*per_unit.get_value()/COST_X_MAX),
            cost_ax.c2p(0, cost_now())+RIGHT*min(i*0.1+0.05, GRAPH_SIZE*per_unit.get_value()/COST_X_MAX)])
            .set_opacity(float(i*0.1 < GRAPH_SIZE*per_unit.get_value()/COST_X_MAX)) for i, dash in enumerate(group)])
        div_cost = DecimalNumber(total(0), num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        div_cost.add_updater(lambda m: m.set_value(round(cost_now(), 4))
                             .next_to(cost_ax.c2p(0, cost_now()), LEFT, buff=0.2))
        div_units = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        div_units.add_updater(lambda m: m.set_value(round(per_unit.get_value(), 4))
                              .move_to(cost_ax.c2p(per_unit.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        avg_up = VGroup(*[Line(ORIGIN, UP, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        avg_up.add_updater(lambda group: [dash.set_points_as_corners([
            avg_ax.c2p(per_unit.get_value(), 0)+UP*min(i*0.1, GRAPH_SIZE*average_display()/AVERAGE_MAX),
            avg_ax.c2p(per_unit.get_value(), 0)+UP*min(i*0.1+0.05, GRAPH_SIZE*average_display()/AVERAGE_MAX)])
            .set_opacity(float(average_visible() and i*0.1 < GRAPH_SIZE*average_display()/AVERAGE_MAX))
            for i, dash in enumerate(group)])
        avg_point = Dot(avg_ax.c2p(0, AVERAGE_TOP), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        avg_point.add_updater(lambda m: m.move_to(avg_ax.c2p(per_unit.get_value(), average_display()))
            .set_opacity(float(average_visible())))
        avg_across = VGroup(*[Line(ORIGIN, RIGHT, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        avg_across.add_updater(lambda group: [dash.set_points_as_corners([
            avg_ax.c2p(0, average_display())+RIGHT*min(i*0.1, GRAPH_SIZE*per_unit.get_value()/COST_X_MAX),
            avg_ax.c2p(0, average_display())+RIGHT*min(i*0.1+0.05, GRAPH_SIZE*per_unit.get_value()/COST_X_MAX)])
            .set_opacity(float(average_visible() and i*0.1 < GRAPH_SIZE*per_unit.get_value()/COST_X_MAX))
            for i, dash in enumerate(group)])
        avg_cost = DecimalNumber(atc(10), num_decimal_places=1, color=GUIDE).scale(READOUT_SCALE)
        avg_cost.add_updater(lambda m: m.set_value(round(average_now(), 4))
                             .next_to(avg_ax.c2p(0, average_display()), LEFT, buff=0.2).set_opacity(float(average_visible())))
        avg_units = DecimalNumber(10, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        avg_units.add_updater(lambda m: m.set_value(round(per_unit.get_value(), 4))
                              .move_to(avg_ax.c2p(per_unit.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET).set_opacity(float(average_visible())))
        division_marks = [div_up, div_point, div_across, div_cost, div_units, avg_up, avg_point, avg_across, avg_cost, avg_units]

        # ---- 3.g · Start with VC and AVC. Dim the other costs and retain the stationary grey TC bars.
        # Keep averages uncluttered while tracing; their one stacked bar enters only at the sum.
        avc_curve = polyline([avg_ax.c2p(0, 0), avg_ax.c2p(0, 0)], AVC_COLOR, CURVE_WIDTH)
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, avc(q)) for q in np.linspace(0, per_unit.get_value(), 121)]))
        avc_word = Tex('AVC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(COST_Q_MAX, avc(COST_Q_MAX)), RIGHT, buff=0.15).shift(DOWN * 0.10)
        avc_word.add_updater(lambda m: m.set_opacity(smooth(np.clip((per_unit.get_value()-(COST_Q_MAX-10))/10, 0, 1))))
        for m in [*division_marks, avc_curve, avc_word]:
            m.update()
        note = teaching('Average variable cost: variable cost divided by output.')
        self.play(tc_curve.animate.set_stroke(opacity=0.22), tc_word.animate.set_opacity(0.22),
                  fc_line.animate.set_stroke(opacity=0.22), fc_word.animate.set_opacity(0.22),
                  stored_total.get_part_by_tex(r'\mathrm{TC}').animate.set_opacity(0.22),
                  stored_total.get_part_by_tex(r'\mathrm{FC}').animate.set_opacity(0.22),
                  stored_average.get_part_by_tex(r'\mathrm{ATC}').animate.set_opacity(0.22),
                  stored_average.get_part_by_tex(r'\mathrm{AFC}').animate.set_opacity(0.22),
                  Create(vc_curve), FadeIn(vc_word), FadeIn(note), run_time=1.0)
        self.play(*[FadeIn(m) for m in division_marks], FadeIn(avc_curve))
        self.add(avc_word)
        self.play(per_unit.animate.set_value(COST_Q_MAX), run_time=SWEEP_TIME, rate_func=smooth)
        for m in (avc_curve, avc_word):
            m.update()
            m.clear_updaters(recurse=True)
        self.pause('3.g')

        # ---- 3.h · VC leaves; FC is the source for AFC. The completed AVC stays subdued.
        self.play(*[FadeOut(m) for m in division_marks], FadeOut(note), FadeOut(vc_curve), FadeOut(vc_word), run_time=0.5)
        divided['cost'], divided['average'] = lambda Q: FIXED, lambda Q: FIXED / Q
        per_unit.set_value(0)
        afc_curve = polyline([avg_ax.c2p(AFC_START, AVERAGE_TOP), avg_ax.c2p(AFC_START, AVERAGE_TOP)], AFC_COLOR, CURVE_WIDTH)
        afc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, FIXED / q) for q in np.linspace(AFC_START, max(AFC_START, per_unit.get_value()), 121)])
            .set_stroke(opacity=float(per_unit.get_value() >= AFC_START)))
        afc_word = Tex('AFC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(COST_Q_MAX, FIXED / COST_Q_MAX), RIGHT, buff=0.15)
        afc_word.add_updater(lambda m: m.set_opacity(smooth(np.clip((per_unit.get_value()-(COST_Q_MAX-10))/10, 0, 1))))
        for m in [*division_marks, afc_curve, afc_word]:
            m.update()
        note = teaching('Average fixed cost: the same fixed cost spread over more units.')
        self.play(avc_curve.animate.set_stroke(opacity=0.22), avc_word.animate.set_opacity(0.22),
                  fc_line.animate.set_stroke(opacity=1), fc_word.animate.set_opacity(1),
                  stored_total.get_part_by_tex(r'\mathrm{VC}').animate.set_opacity(0.22),
                  stored_total.get_part_by_tex(r'\mathrm{FC}').animate.set_opacity(1),
                  stored_average.get_part_by_tex(r'\mathrm{AVC}').animate.set_opacity(0.22),
                  stored_average.get_part_by_tex(r'\mathrm{AFC}').animate.set_opacity(1),
                  *[FadeIn(m) for m in division_marks], FadeIn(afc_curve), FadeIn(note))
        self.add(afc_word)
        self.play(per_unit.animate.set_value(COST_Q_MAX), run_time=SWEEP_TIME, rate_func=smooth)
        for m in (afc_curve, afc_word):
            m.update()
            m.clear_updaters(recurse=True)
        self.pause('3.h')

        # ---- 3.f · TC now gives ATC. The two previously traced averages remain as dim context.
        self.play(*[FadeOut(m) for m in division_marks], FadeOut(note), run_time=0.5)
        divided['cost'], divided['average'] = total, atc
        per_unit.set_value(0)
        atc_curve = polyline([avg_ax.c2p(ATC_START, atc(ATC_START)), avg_ax.c2p(ATC_START, atc(ATC_START))], ATC_COLOR, CURVE_WIDTH)
        atc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, atc(q)) for q in np.linspace(ATC_START, max(ATC_START, per_unit.get_value()), 121)])
            .set_stroke(opacity=float(per_unit.get_value() >= ATC_START)))
        atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(COST_Q_MAX, atc(COST_Q_MAX)), RIGHT, buff=0.15).shift(UP * 0.10)
        atc_word.add_updater(lambda m: m.set_opacity(smooth(np.clip((per_unit.get_value()-(COST_Q_MAX-10))/10, 0, 1))))
        for m in [*division_marks, atc_curve, atc_word]:
            m.update()
        note = teaching('Average total cost: total cost divided by output.')
        self.play(tc_curve.animate.set_stroke(opacity=1), tc_word.animate.set_opacity(1),
                  fc_line.animate.set_stroke(opacity=0.22), fc_word.animate.set_opacity(0.22),
                  afc_curve.animate.set_stroke(opacity=0.22), afc_word.animate.set_opacity(0.22),
                  stored_total.get_part_by_tex(r'\mathrm{FC}').animate.set_opacity(0.22),
                  stored_total.get_part_by_tex(r'\mathrm{TC}').animate.set_opacity(1),
                  stored_average.get_part_by_tex(r'\mathrm{AFC}').animate.set_opacity(0.22),
                  stored_average.get_part_by_tex(r'\mathrm{ATC}').animate.set_opacity(1),
                  *[FadeIn(m) for m in division_marks], FadeIn(atc_curve), FadeIn(note))
        self.add(atc_word)
        # Curve, point, and label finish together; no separate extension or backward settling motion.
        self.play(per_unit.animate.set_value(COST_Q_MAX), run_time=SWEEP_TIME, rate_func=smooth)
        for m in (atc_curve, atc_word):
            m.update()
            m.clear_updaters(recurse=True)
        self.pause('3.f')

        # ---- 3.i · The heights add: AVC plus the AFC gap reaches ATC at the same quantity.
        for m in division_marks:
            m.update()
            m.clear_updaters()
        fc_number.clear_updaters()
        sum_avc = Polygon(avg_ax.c2p(COST_Q_MAX-1, 0), avg_ax.c2p(COST_Q_MAX, 0),
            avg_ax.c2p(COST_Q_MAX, avc(COST_Q_MAX)), avg_ax.c2p(COST_Q_MAX-1, avc(COST_Q_MAX)),
            color=AVC_COLOR, stroke_width=BAR_OUTLINE, fill_color=AVC_COLOR, fill_opacity=AREA_OPACITY).set_z_index(GUIDE_LAYER)
        sum_afc = Polygon(avg_ax.c2p(COST_Q_MAX-1, avc(COST_Q_MAX)), avg_ax.c2p(COST_Q_MAX, avc(COST_Q_MAX)),
            avg_ax.c2p(COST_Q_MAX, atc(COST_Q_MAX)), avg_ax.c2p(COST_Q_MAX-1, atc(COST_Q_MAX)),
            color=CAPTION, stroke_width=BAR_OUTLINE, fill_color=AFC_COLOR, fill_opacity=AREA_OPACITY).set_z_index(GUIDE_LAYER)
        sum_afc_word = Tex('AFC', color=CAPTION).scale(0.55).next_to(sum_afc, LEFT, buff=0.15).shift(DOWN*0.08)
        sum_quantity = DecimalNumber(COST_Q_MAX, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        sum_quantity.move_to(avg_ax.c2p(COST_Q_MAX, 0)+DOWN*QUANTITY_NUMBER_OFFSET)
        average_sum = VGroup(sum_avc, sum_afc, sum_afc_word, sum_quantity)
        self.remove(note)
        note = teaching('Average total cost is average variable cost plus average fixed cost.')
        self.play(*[FadeOut(m) for m in division_marks],
                  avc_curve.animate.set_stroke(opacity=1), avc_word.animate.set_opacity(1),
                  afc_curve.animate.set_stroke(opacity=1), afc_word.animate.set_opacity(1),
                  fc_line.animate.set_stroke(opacity=1), fc_word.animate.set_opacity(1), fc_number.animate.set_opacity(1),
                  stored_total.animate.set_opacity(1), stored_average.animate.set_opacity(1), FadeIn(note),
                  GrowFromEdge(sum_avc, DOWN), FadeIn(sum_quantity))
        self.play(GrowFromEdge(sum_afc, DOWN), FadeIn(sum_afc_word), run_time=0.7)
        self.pause('3.i')

        # ---- 3.j · Read the increase between adjacent TC bars. Other curves recede.
        # Adjacent bars differ by one unit; the finite increment equals MC at the interval midpoint.
        marginal_q = ValueTracker(40.5)
        marginal_index = lambda: max(0, min(MAX_BARS-1, int(marginal_q.get_value())))
        marginal_left = lambda: marginal_index()
        marginal_right = lambda: marginal_left()+1
        marginal_middle = lambda: marginal_left()+0.5
        marginal_extra = lambda: total(marginal_right())-total(marginal_left())
        marginal_unit_cost = lambda: marginal_extra()
        tc_steps = VGroup()
        for i, right in enumerate(range(1, MAX_BARS+1)):
            bar = Polygon(cost_ax.c2p(right-1, 0), cost_ax.c2p(right, 0),
                cost_ax.c2p(right, total(right)), cost_ax.c2p(right-1, total(right)),
                color=MUTED, stroke_width=BAR_OUTLINE, fill_opacity=0.08)
            bar.add_updater(lambda m, i=i: m.set_stroke(MUTED, BAR_OUTLINE,
                opacity=0.9 if i in (marginal_index()-1, marginal_index()) else 0.25)
                .set_fill(MUTED, 0.28 if i in (marginal_index()-1, marginal_index()) else 0.08))
            tc_steps.add(bar)
        marginal_quantities = lambda: (marginal_left(), marginal_right())
        cost_pair, quantity_pair, cost_pair_guides, pair_dots = VGroup(), VGroup(), VGroup(), VGroup()
        cost_label_leaders, quantity_leaders = VGroup(), VGroup()
        for side in range(2):
            # Separate close labels with leaders, while keeping their guide endpoints at the true values.
            price = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(0.60)
            price.add_updater(lambda m, side=side: m.set_value(round(total(marginal_quantities()[side])))
                .next_to(cost_ax.c2p(0, total(marginal_quantities()[side])), LEFT, buff=0.95)
                .shift(UP*(0.24 if side else -0.24))
                .set_y(min(m.get_y(), cost_words[0].get_bottom()[1]-0.08)))
            cost_pair.add(price)
            number = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
            number.add_updater(lambda m, side=side: m.set_value(marginal_quantities()[side])
                .move_to(cost_ax.c2p(marginal_quantities()[side], 0)
                    +RIGHT*(0.22 if side else -0.22)+DOWN*QUANTITY_NUMBER_OFFSET))
            quantity_pair.add(number)
            dot = Dot(ORIGIN, radius=0.045, color=GUIDE).set_z_index(DOT_LAYER)
            dot.add_updater(lambda m, side=side: m.move_to(cost_ax.c2p(marginal_quantities()[side], total(marginal_quantities()[side]))))
            pair_dots.add(dot)
            guide = VGroup(*[Line(ORIGIN, RIGHT, color=GUIDE, stroke_width=1.5)
                for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
            guide.add_updater(lambda group, side=side: [dash.set_points_as_corners([
                cost_ax.c2p(0, total(marginal_quantities()[side]))+RIGHT*min(i*0.1, GRAPH_SIZE*marginal_quantities()[side]/COST_X_MAX),
                cost_ax.c2p(0, total(marginal_quantities()[side]))+RIGHT*min(i*0.1+0.05, GRAPH_SIZE*marginal_quantities()[side]/COST_X_MAX)])
                .set_stroke(opacity=float(i*0.1 < GRAPH_SIZE*marginal_quantities()[side]/COST_X_MAX))
                for i, dash in enumerate(group)])
            cost_pair_guides.add(guide)
            price_leader = Line(ORIGIN, LEFT, color=MUTED, stroke_width=1)
            price_leader.add_updater(lambda m, side=side: m.set_points_as_corners([
                cost_ax.c2p(0, total(marginal_quantities()[side]))+LEFT*0.025,
                np.array([cost_ax.c2p(0, 0)[0]-0.10, cost_pair[side].get_center()[1], 0]),
                cost_pair[side].get_right()+RIGHT*0.06]))
            cost_label_leaders.add(price_leader)
            quantity_leader = Line(ORIGIN, DOWN, color=MUTED, stroke_width=1)
            quantity_leader.add_updater(lambda m, side=side: m.set_points_as_corners([
                cost_ax.c2p(marginal_quantities()[side], 0)+DOWN*0.04,
                quantity_pair[side].get_top()+UP*0.04]))
            quantity_leaders.add(quantity_leader)
        cost_step = Line(ORIGIN, UP, color=MC_COLOR, stroke_width=STEP_WIDTH)
        cost_step.add_updater(lambda m: m.set_points_as_corners([
            cost_ax.c2p(0, total(marginal_left()))+LEFT*STEP_OFFSET,
            cost_ax.c2p(0, total(marginal_right()))+LEFT*STEP_OFFSET]))
        extra_cost = DecimalNumber(81, num_decimal_places=0, include_sign=True, color=MC_COLOR).scale(0.55)
        extra_cost.add_updater(lambda m: m.set_value(round(marginal_extra(), 4)).next_to(cost_step, LEFT, buff=0.12))
        tc_probe = VGroup(cost_pair, quantity_pair, cost_pair_guides, pair_dots,
            cost_label_leaders, quantity_leaders, cost_step, extra_cost).set_z_index(GUIDE_LAYER)
        for m in (tc_steps, tc_probe):
            m.update()
        self.remove(note)
        note = teaching(r'One more unit adds \$81 to total cost.')
        self.play(FadeOut(average_sum), FadeOut(afc_curve), FadeOut(afc_word),
                  FadeOut(tc_curve), FadeOut(tc_word), FadeOut(fc_line), FadeOut(fc_word), FadeOut(fc_number),
                  FadeOut(stored_total), FadeOut(stored_average),
                  atc_curve.animate.set_stroke(opacity=0.22), atc_word.animate.set_opacity(0.22),
                  avc_curve.animate.set_stroke(opacity=0.22), avc_word.animate.set_opacity(0.22),
                  FadeOut(rest_cost_bars), FadeIn(tc_steps), FadeIn(tc_probe), FadeIn(note), run_time=0.8)
        self.pause('3.j')

        # ---- 3.k · Transfer only the extra cost per unit to the right; no bars over the average curves.
        marginal_dot = Dot(avg_ax.c2p(40.5, 81), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        marginal_dot.add_updater(lambda m: m.move_to(avg_ax.c2p(marginal_middle(), marginal_unit_cost())))
        marginal_price = DecimalNumber(81, num_decimal_places=0, color=MC_COLOR).scale(READOUT_SCALE)
        marginal_price.add_updater(lambda m: m.set_value(round(marginal_unit_cost(), 4))
            .next_to(avg_ax.c2p(0, marginal_unit_cost()), LEFT, buff=0.2))
        marginal_across = VGroup(*[Line(ORIGIN, RIGHT, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        marginal_across.add_updater(lambda group: [dash.set_points_as_corners([
            avg_ax.c2p(0, marginal_unit_cost())+RIGHT*min(i*0.1, GRAPH_SIZE*marginal_middle()/COST_X_MAX),
            avg_ax.c2p(0, marginal_unit_cost())+RIGHT*min(i*0.1+0.05, GRAPH_SIZE*marginal_middle()/COST_X_MAX)])
            .set_stroke(opacity=float(i*0.1 < GRAPH_SIZE*marginal_middle()/COST_X_MAX)) for i, dash in enumerate(group)])
        marginal_down = VGroup(*[Line(ORIGIN, UP, color=GUIDE, stroke_width=GUIDE_WIDTH)
            for _ in range(int(np.ceil(GRAPH_SIZE/0.1)))])
        marginal_down.add_updater(lambda group: [dash.set_points_as_corners([
            avg_ax.c2p(marginal_middle(), 0)+UP*min(i*0.1, GRAPH_SIZE*marginal_unit_cost()/AVERAGE_MAX),
            avg_ax.c2p(marginal_middle(), 0)+UP*min(i*0.1+0.05, GRAPH_SIZE*marginal_unit_cost()/AVERAGE_MAX)])
            .set_stroke(opacity=float(i*0.1 < GRAPH_SIZE*marginal_unit_cost()/AVERAGE_MAX)) for i, dash in enumerate(group)])
        marginal_marks = VGroup(marginal_across, marginal_down, marginal_dot, marginal_price).set_z_index(DOT_LAYER)
        marginal_marks.update()
        self.remove(note)
        note = teaching('Marginal cost is the cost of producing one more unit.')
        self.play(FadeIn(marginal_marks), FadeIn(note), run_time=0.8)
        self.pause('3.k')

        # ---- 3.m · Trace MC in both directions, retaining every interval already visited.
        self.remove(note)
        note = teaching('At higher output, each increase costs more per unit.')
        mc_start = marginal_middle()
        mc_trace = Line(avg_ax.c2p(mc_start, mc(mc_start)), avg_ax.c2p(mc_start, mc(mc_start)),
            color=MC_COLOR, stroke_width=CURVE_WIDTH)
        mc_trace.add_updater(lambda m: m.set_points_as_corners([
            avg_ax.c2p(marginal_middle(), marginal_unit_cost()), avg_ax.c2p(mc_start, mc(mc_start))]))
        mc_trace.set_z_index(GUIDE_LAYER)
        self.add(mc_trace)
        self.play(FadeIn(note), marginal_q.animate.set_value(0.5), run_time=ROLL_TIME, rate_func=smooth)
        mc_trace.update()
        mc_trace.clear_updaters()
        mc_trace.add_updater(lambda m: m.set_points_as_corners([
            avg_ax.c2p(0.5, mc(0.5)),
            avg_ax.c2p(max(mc_start, marginal_middle()), mc(max(mc_start, marginal_middle())))]))
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(
            avg_ax.c2p(COST_Q_MAX-0.5, mc(COST_Q_MAX-0.5)), RIGHT, buff=0.15)
        mc_word.add_updater(lambda m: m.set_opacity(smooth(np.clip((marginal_middle()-(COST_Q_MAX-10.5))/10, 0, 1))))
        mc_word.update()
        self.add(mc_word)
        self.play(marginal_q.animate.set_value(COST_Q_MAX-0.5), run_time=SWEEP_TIME, rate_func=smooth)
        for m in (tc_steps, tc_probe, marginal_marks, mc_trace, mc_word):
            m.update()
            m.clear_updaters(recurse=True)
        self.pause('3.m')

        # ---- 3.n.below · Movement: one tracker moves a point along ATC with the MC point at the same quantity.
        # The construction is finished: keep only the average-cost graph, centered at the same scale.
        AVERAGE_PAN = RIGHT_ORIGIN[0] + GRAPH_SIZE/2
        self.play(FadeOut(tc_steps), FadeOut(tc_probe), FadeOut(marginal_marks),
                  FadeOut(cost_ax), FadeOut(cost_words),
                  avg_ax.animate.shift(LEFT*AVERAGE_PAN), avg_words.animate.shift(LEFT*AVERAGE_PAN),
                  atc_curve.animate.shift(LEFT*AVERAGE_PAN).set_stroke(opacity=1),
                  atc_word.animate.shift(LEFT*AVERAGE_PAN).set_opacity(1),
                  avc_curve.animate.shift(LEFT*AVERAGE_PAN).set_stroke(opacity=1),
                  avc_word.animate.shift(LEFT*AVERAGE_PAN).set_opacity(1),
                  mc_trace.animate.shift(LEFT*AVERAGE_PAN), mc_word.animate.shift(LEFT*AVERAGE_PAN),
                  run_time=1.2, rate_func=smooth)
        # Below the lowest point MC lies under ATC and ATC falls. The hold is at 20 units, where the gap is plain.
        moving_q = ValueTracker(15)
        move_up = DashedLine(avg_ax.c2p(15, 0), avg_ax.c2p(15, atc(15)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        move_up.add_updater(lambda m: m.become(DashedLine(
            avg_ax.c2p(moving_q.get_value(), 0),
            avg_ax.c2p(moving_q.get_value(), max(atc(moving_q.get_value()), mc(moving_q.get_value()))),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        move_atc = Dot(avg_ax.c2p(15, atc(15)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        move_atc.add_updater(lambda m: m.move_to(avg_ax.c2p(moving_q.get_value(), atc(moving_q.get_value()))))
        move_mc = Dot(avg_ax.c2p(15, mc(15)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        move_mc.add_updater(lambda m: m.move_to(avg_ax.c2p(moving_q.get_value(), mc(moving_q.get_value()))))
        move_across, move_labels = VGroup(), VGroup()
        # Fade the separate labels as their levels meet; the minimum gets one equality label.
        comparison_label_opacity = lambda: smooth(np.clip(
            (GRAPH_SIZE*abs(atc(moving_q.get_value())-mc(moving_q.get_value()))/AVERAGE_MAX-0.16)/0.20, 0, 1))
        for label, function in [(r'\mathrm{ATC}_q', atc), (r'\mathrm{MC}_q', mc)]:
            across = DashedLine(avg_ax.c2p(0, function(15)), avg_ax.c2p(15, function(15)),
                color=GUIDE, stroke_width=GUIDE_WIDTH)
            across.add_updater(lambda m, function=function: m.become(DashedLine(
                avg_ax.c2p(0, function(moving_q.get_value())),
                avg_ax.c2p(moving_q.get_value(), function(moving_q.get_value())),
                color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
            move_across.add(across)
            word = MathTex(label, color=GUIDE).scale(READOUT_SCALE)
            word.add_updater(lambda m, function=function: m.next_to(
                avg_ax.c2p(0, function(moving_q.get_value())), LEFT, buff=0.2)
                .set_opacity(comparison_label_opacity()))
            move_labels.add(word)
        move_quantity = MathTex('q', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        move_quantity.add_updater(lambda m: m.move_to(
            avg_ax.c2p(moving_q.get_value(), 0)+DOWN*QUANTITY_NUMBER_OFFSET))
        move_marks = [move_up, move_atc, move_mc, move_across, move_labels, move_quantity]
        for m in move_marks:
            m.update()
        self.remove(note)
        note = teaching('When MC lies below ATC, ATC bends downward.')
        self.play(*[FadeIn(m) for m in move_marks], FadeIn(note))
        self.play(moving_q.animate.set_value(20), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.n.below')

        # ---- 3.n · Past the lowest point MC lies above ATC and ATC rises.
        self.remove(note)
        note = teaching('When MC lies above ATC, ATC bends upward.')
        self.play(FadeIn(note), moving_q.animate.set_value(55), run_time=SWEEP_TIME, rate_func=smooth)
        self.pause('3.n')

        # ---- 3.o · Back to where they meet: a red point at ATC's lowest point, on MC.
        lowest = Dot(avg_ax.c2p(MIN_Q, atc(MIN_Q)), radius=0.085, color=GUIDE).set_z_index(DOT_LAYER + 1)
        self.remove(note)
        note = teaching('The marginal cost curve runs through the minimum of ATC.')
        self.play(moving_q.animate.set_value(MIN_Q), run_time=ROLL_TIME, rate_func=smooth)
        for m in move_marks:
            m.update()
            m.clear_updaters(recurse=True)
        minimum_across = DashedLine(avg_ax.c2p(0, atc(MIN_Q)), avg_ax.c2p(MIN_Q, atc(MIN_Q)),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        minimum_label = MathTex(r'\mathrm{ATC}_q = \mathrm{MC}_q', color=GUIDE).scale(READOUT_SCALE)
        minimum_label.next_to(avg_ax.c2p(0, atc(MIN_Q)), LEFT, buff=0.2)
        minimum_marks = VGroup(move_up, move_quantity, minimum_across, minimum_label)
        self.play(FadeOut(move_atc), FadeOut(move_mc), FadeOut(move_across), FadeOut(move_labels),
                  FadeIn(minimum_across), FadeIn(minimum_label), FadeIn(lowest), FadeIn(note))
        self.pause('3.o')

        # ---- 3.p · Keep the focus on the gap between ATC and AVC; AFC stays off the graph.
        self.remove(note)
        note = teaching('ATC is higher than AVC in the short run because we have fixed costs like rent.')
        self.play(FadeOut(lowest), FadeOut(minimum_marks), FadeIn(note))
        self.pause('3.p')

        # ---- 3.q · The long-run line.
        self.remove(note)
        note = teaching('In the long run, all costs are variable.')
        # Fade the small-output tail before the rise, so the 1/q term never shoots up at zero.
        avc_tail = polyline([avg_ax.c2p(q, avc(q)) for q in np.linspace(0, ATC_START, 41)], AVC_COLOR, CURVE_WIDTH)
        avc_curve.set_points_as_corners([avg_ax.c2p(q, avc(q)) for q in np.linspace(ATC_START, COST_Q_MAX, 121)])
        self.add(avc_tail)
        self.play(FadeIn(note), FadeOut(avc_tail))
        self.pause('3.q')

        # ---- 3.r · AVC rises onto ATC at fixed quantities, on the same centered graph.
        fixed_part = ValueTracker(FIXED)
        # Preserve each point's quantity throughout the transition, over ATC's visible domain.
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, avc(q) + (FIXED - fixed_part.get_value()) / q)
             for q in np.linspace(ATC_START, COST_Q_MAX, 121)]))
        avc_word.add_updater(lambda m: m.next_to(avg_ax.c2p(COST_Q_MAX, avc(COST_Q_MAX)), RIGHT, buff=0.15)
                             .set_y(min(avg_ax.c2p(COST_Q_MAX, avc(COST_Q_MAX) + (FIXED - fixed_part.get_value()) / COST_Q_MAX)[1], atc_word.get_y() - 0.32)))
        long_run = [avc_curve, avc_word]
        for m in long_run:
            m.update()
        self.remove(note)
        note = teaching('With all costs variable, average variable cost equals average total cost.')
        self.play(FadeIn(note), fixed_part.animate.set_value(0), run_time=SWEEP_TIME, rate_func=smooth)
        for m in long_run:
            m.update()
            m.clear_updaters()
        # The two averages now share a curve, so use one label.
        atc_avc = MathTex(r'\mathrm{ATC} = \mathrm{AVC}').scale(CURVE_WORD_SCALE)
        atc_avc.next_to(avg_ax.c2p(COST_Q_MAX, atc(COST_Q_MAX)), RIGHT, buff=0.15)
        self.play(FadeOut(avc_word), FadeOut(atc_word), FadeIn(atc_avc),
                  run_time=0.6)
        self.pause('3.r')

        # ---- 4.a · The firm's objective, with revenue minus cost identified as profit.
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])   # trackers join the scene when animated
        FadeAll(self)
        self.clear()
        head = title('Marginal Revenue')
        objective = MathTex(r'\max_{q}\ {{\mathrm{TR} - \mathrm{TC}}}').move_to([0, BODY_MID + 0.5, 0])
        profit_brace = Brace(objective.get_part_by_tex(r'\mathrm{TR} - \mathrm{TC}'), UP, buff=0.12, color=INK)
        profit_word = Tex('Profit', color=CAPTION).scale(0.65).next_to(profit_brace, UP, buff=0.12)
        note = teaching('In this class, firms aim to maximize profit.')
        self.play(FadeIn(head), FadeIn(objective), FadeIn(profit_brace), FadeIn(profit_word), FadeIn(note))
        self.pause('4.a')

        # ---- 4.b · End on the solution to the maximization problem: MC = MR.
        rule = MathTex(r'\Longrightarrow\quad {{\mathrm{MC}}} = {{\mathrm{MR}}}').move_to([0, BODY_MID - 0.9, 0])
        rule.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        rule.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        self.remove(note)
        note = teaching('A firm maximizes profit by choosing quantity where marginal cost equals marginal revenue.')
        self.play(FadeIn(rule), FadeIn(note))
        self.pause('4.b')
