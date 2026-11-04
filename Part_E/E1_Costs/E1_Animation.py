# maniml E1_Animation.py EpisodeE1
# Storyboard: E1_Notes.md; current review overrides in E1_Storyboard_Revision.md. All choreography stays in construct().
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
        MAX_BARS, BAR_OUTLINE = 20, 1.0         # B2 polygons: adjoining edges, colored outline, 35% fill
        # Taxonomy grid, E4's object: a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4
        TAXONOMY_SIDE_SCALE, CHECKLIST_LEFT = 0.72, 0.6
        BOX_BUFF = 0.12                          # E2-E4's 0.22 would meet the cell rules on the shrunk grid

        # The model, as one-line functions. shape is the production function's exponent: 0.5 gives
        # F(L) = 10 sqrt(L); 1 gives the straight line of 2.p.linear. Every other section has shape = 0.5.
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
        TOTAL_MAX, AVERAGE_MAX = total(100), 1.2 * mc(100)
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
            Tex('P', color=INK).scale(0.8).next_to(supply_ax.c2p(0, 10), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(0, 10), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.73))
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

        # ---- 1.d · Competitive firms: the grid steps left, its first cell fills and is boxed, then his three conditions.
        # The grid and its (unseen) cells take the same scale about the grid's left edge, then the same shift.
        side_about = np.array([grid_left, BODY_MID, 0])
        side_shift = LEFT * (grid_left + 7.4)
        cells.scale(TAXONOMY_SIDE_SCALE, about_point=side_about).shift(side_shift)
        self.remove(head)
        head = title('Competitive Firms')
        self.play(FadeIn(head), grid.animate.scale(TAXONOMY_SIDE_SCALE, about_point=side_about).shift(side_shift), run_time=1.2)
        box = SurroundingRectangle(perfect, buff=BOX_BUFF, color=NASH)
        checklist = numbered('Many sellers', 'Many buyers', 'Homogeneous goods').align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        self.play(FadeIn(perfect), FadeIn(box))
        self.play(FadeIn(checklist[0]), run_time=0.6)
        self.play(FadeIn(checklist[1]), run_time=0.6)
        self.play(FadeIn(checklist[2]), run_time=0.6)
        self.pause('1.d')

        # ---- 1.e · Monopoly: the one-seller row, the box moves, the three conditions from his sentence.
        self.remove(head, checklist)
        head = title('Monopoly')
        checklist = numbered('One seller', 'Many buyers', "Differentiation isn't important").align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        self.play(FadeIn(head), FadeIn(monopoly), Transform(box, SurroundingRectangle(monopoly, buff=BOX_BUFF, color=NASH)),
                  FadeIn(checklist), run_time=0.8)
        self.pause('1.e')

        # ---- 1.f · Monopolistic competition: many sellers, slightly differentiated goods.
        self.remove(head, checklist)
        head = title('Monopolistic Competition')
        checklist = numbered('Many sellers', 'Many buyers', 'Slightly differentiated goods').align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        self.play(FadeIn(head), FadeIn(monopolistic), Transform(box, SurroundingRectangle(monopolistic, buff=BOX_BUFF, color=NASH)),
                  FadeIn(checklist), run_time=0.8)
        self.pause('1.f')

        # ---- 1.g · Oligopoly: few sellers, homogeneous goods.
        self.remove(head, checklist)
        head = title('Oligopoly')
        checklist = numbered('Few sellers', 'Many buyers', 'Homogeneous goods').align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        self.play(FadeIn(head), FadeIn(oligopoly), Transform(box, SurroundingRectangle(oligopoly, buff=BOX_BUFF, color=NASH)),
                  FadeIn(checklist), run_time=0.8)
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
            Tex('Q', color=INK).scale(0.8).next_to(f_ax.c2p(0, 100), LEFT, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(0, 100), RIGHT, buff=0.22).shift(UP * 0.30),
            Tex('L', color=INK).scale(0.8).next_to(f_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{worker hours}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(100, 0), DOWN, buff=0.73))
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

        # ---- 2.j · Five touching one-unit rectangles, as in B2's cost slices, viewed close up.
        # Each upper-right corner lies on F. At wider scales a band groups adjacent units (never more than 20).
        step_marks = VGroup(*labor_marks, double_up, double_dot, double_across, double_work, double_made,
                            triple_up, triple_dot, triple_across, triple_work, triple_made, input_braces, output_braces,
                            input_differences, output_differences)
        q_span, shown = ValueTracker(100), ValueTracker(0)
        zp = lambda L, Q: f_ax.c2p(100 * L / labor_for(q_span.get_value()), 100 * Q / q_span.get_value())
        band_step = lambda: max(1, q_span.get_value() / MAX_BARS)
        band_low = lambda i: min(i * band_step(), q_span.get_value())
        band_high = lambda i: min((i+1) * band_step(), q_span.get_value())
        band_visible = lambda i: band_high(i) <= shown.get_value() + 1e-6 and band_low(i) < q_span.get_value()
        zoom_curve = f_curve
        zoom_curve.clear_updaters()  # the normalized power function has the same shape at each scale
        zoom_curve.set_z_index(GUIDE_LAYER)
        hour_bars = VGroup()
        for i in range(MAX_BARS):
            bar = Polygon(ORIGIN, RIGHT, UR, UP, color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            bar.add_updater(lambda m, i=i: m.set_points_as_corners([
                zp(0, band_low(i)), zp(labor_for(band_high(i)), band_low(i)),
                zp(labor_for(band_high(i)), band_high(i)), zp(0, band_high(i)), zp(0, band_low(i))])
                .set_stroke(VC_COLOR, BAR_OUTLINE, opacity=float(band_visible(i)))
                .set_fill(VC_COLOR, AREA_OPACITY if band_visible(i) else 0))
            hour_bars.add(bar)
        current_quantity = lambda: max(min(shown.get_value(), q_span.get_value()), 0.01)
        newest_dot = Dot(zp(labor_for(0.01), 0.01), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        newest_dot.add_updater(lambda m: m.move_to(zp(labor_for(current_quantity()), current_quantity())))
        newest_quantity = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        newest_quantity.add_updater(lambda m: m.set_value(round(current_quantity(), 4)).next_to(newest_dot, RIGHT, buff=0.15))
        newest_labor = DecimalNumber(0, num_decimal_places=2, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        newest_labor.add_updater(lambda m: m.set_value(round(labor_for(current_quantity()), 4))
            .move_to(zp(labor_for(current_quantity()), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        newest_down = DashedLine(zp(labor_for(0.01), 0.01), zp(labor_for(0.01), 0), color=GUIDE, stroke_width=GUIDE_WIDTH)
        newest_down.add_updater(lambda m: m.become(DashedLine(
            zp(labor_for(current_quantity()), current_quantity()), zp(labor_for(current_quantity()), 0),
            color=GUIDE, stroke_width=GUIDE_WIDTH)))
        newest_across = DashedLine(zp(labor_for(0.01), 0.01), zp(0, 0.01), color=GUIDE, stroke_width=GUIDE_WIDTH)
        newest_across.add_updater(lambda m: m.become(DashedLine(
            zp(labor_for(current_quantity()), current_quantity()), zp(0, current_quantity()),
            color=GUIDE, stroke_width=GUIDE_WIDTH)))
        newest_marks = VGroup(newest_down, newest_across, newest_dot, newest_quantity, newest_labor).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('Start small: how much labor does each output level require?')
        self.play(FadeOut(step_marks), FadeIn(note), run_time=0.5)
        q_span.set_value(6)
        hour_bars.update()
        self.add(hour_bars)
        newest_marks.update()
        self.play(FadeIn(newest_marks), run_time=0.4)
        self.play(shown.animate.set_value(5), run_time=3.5, rate_func=smooth)
        self.pause('2.j')

        # ---- 2.k · Expand the window. Geometry updates in place; only 20 bands are ever allocated.
        self.remove(note)
        note = teaching('Each additional unit takes more hours than the last.')
        self.play(FadeOut(f_word), FadeIn(note), run_time=0.4)
        self.play(q_span.animate.set_value(100), run_time=2, rate_func=smooth)
        self.play(shown.animate.set_value(100), run_time=SWEEP_TIME, rate_func=smooth)
        self.play(FadeOut(newest_marks), FadeIn(f_word), run_time=0.4)
        newest_marks.clear_updaters(recurse=True)
        self.pause('2.k')

        # ---- 2.l · Return to the first five units to map hours into variable cost at a legible scale.
        # The only stored text is the wage; fixed cost joins the bars later, at 2.p.
        cost_ax = style_axes([0, 100, 10], [0, TOTAL_MAX, 1000], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        cost_ax.shift(RIGHT_ORIGIN - cost_ax.c2p(0, 0))
        cost_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(cost_ax.c2p(0, TOTAL_MAX), LEFT, buff=0.23),
            Tex(r'\textsf{dollars}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(0, TOTAL_MAX), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(cost_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(100, 0), DOWN, buff=0.73))
        stored_wage = subtitle(head, rf'Wage: \${WAGE} per hour', book=True)
        self.remove(note)
        note = teaching(f'The same labor hours become variable cost at ${WAGE} per hour.'.replace('$', r'\$'))
        self.play(FadeOut(wage_equation), FadeOut(production_subtitle), FadeIn(stored_wage), FadeIn(note), run_time=0.6)
        self.play(q_span.animate.set_value(6), shown.animate.set_value(5), run_time=2, rate_func=smooth)
        shown.set_value(5)
        hour_bars.update()
        for bar in hour_bars:
            bar.clear_updaters()
        hour_bars.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, 0.10)
        for bar in hour_bars[5:]:
            bar.set_opacity(0)
        self.play(FadeIn(cost_ax), FadeIn(cost_words), run_time=0.6)
        self.pause('2.l')

        # ---- 2.m · Unit 1 stays visible as a horizontal labor bar and a vertical VC bar.
        # No algebra row: just the matching red output, hours, and dollar readouts with dashed guides.
        cost_span, fixed_amount = ValueTracker(variable(6)), ValueTracker(0)
        cp = lambda Q, C: cost_ax.c2p(100 * Q / q_span.get_value(), TOTAL_MAX * C / cost_span.get_value())
        cost_bars, mapped_hours = VGroup(), VGroup()
        for Q in range(1, 6):
            mapped_hours.add(Polygon(zp(0, Q-1), zp(labor_for(Q), Q-1), zp(labor_for(Q), Q), zp(0, Q),
                color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY))
            cost_bars.add(Polygon(cp(Q-1, 0), cp(Q, 0), cp(Q, variable(Q)), cp(Q-1, variable(Q)),
                color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY))
        unit_marks = VGroup(
            Tex('1', color=GUIDE).scale(READOUT_SCALE).next_to(zp(0, 1), LEFT, buff=0.2),
            DashedLine(zp(labor_for(1), 1), zp(labor_for(1), 0), color=GUIDE, stroke_width=GUIDE_WIDTH),
            Tex('0.01', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(zp(labor_for(1), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        cost_marks = VGroup(
            Tex('1', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(cp(1, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            DashedLine(cp(1, variable(1)), cp(0, variable(1)), color=GUIDE, stroke_width=GUIDE_WIDTH),
            Tex(f'{variable(1):.0f}', color=GUIDE).scale(READOUT_SCALE).next_to(cp(0, variable(1)), LEFT, buff=0.2))
        unit_marks.set_z_index(DOT_LAYER)
        cost_marks.set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('One unit: 0.01 labor hours, one dollar in variable cost.')
        self.play(FadeIn(mapped_hours[0]), FadeIn(unit_marks), FadeIn(note), run_time=0.6)
        self.play(TransformFromCopy(mapped_hours[0], cost_bars[0]), FadeIn(cost_marks), run_time=1.0)
        self.pause('2.m')

        # ---- 2.n · Add unit 2 beside unit 1; both outlined rectangles remain on both graphs.
        second_units = VGroup(
            Tex('2', color=GUIDE).scale(READOUT_SCALE).next_to(zp(0, 2), LEFT, buff=0.2),
            DashedLine(zp(labor_for(2), 2), zp(labor_for(2), 0), color=GUIDE, stroke_width=GUIDE_WIDTH),
            Tex('0.04', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(zp(labor_for(2), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        second_costs = VGroup(
            Tex('2', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(cp(2, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            DashedLine(cp(2, variable(2)), cp(0, variable(2)), color=GUIDE, stroke_width=GUIDE_WIDTH),
            Tex(f'{variable(2):.0f}', color=GUIDE).scale(READOUT_SCALE).next_to(cp(0, variable(2)), LEFT, buff=0.2))
        self.remove(note)
        note = teaching('Two units: 0.04 labor hours, four dollars in variable cost.')
        self.play(FadeIn(mapped_hours[1]), Transform(unit_marks, second_units), FadeIn(note), run_time=0.6)
        self.play(TransformFromCopy(mapped_hours[1], cost_bars[1]), Transform(cost_marks, second_costs), run_time=1.0)
        self.pause('2.n')

        # ---- 2.o · Finish the five units before opening the view to 100; larger bands group five units each.
        self.remove(note)
        note = teaching('More output needs more labor, so variable cost rises.')
        self.play(FadeOut(unit_marks), FadeOut(cost_marks), FadeIn(note), run_time=0.4)
        for Q in range(3, 6):
            self.play(FadeIn(mapped_hours[Q-1]), run_time=0.25)
            self.play(TransformFromCopy(mapped_hours[Q-1], cost_bars[Q-1]), run_time=0.45)
        self.wait(0.5)
        self.remove(hour_bars, mapped_hours, cost_bars)
        shown.set_value(5)
        # Allocate a fixed pool once; update points rather than rebuilding bars or TeX on every frame.
        hour_bars, cost_bars, fixed_bars = VGroup(), VGroup(), VGroup()
        for i in range(MAX_BARS):
            hours = Polygon(ORIGIN, RIGHT, UR, UP, color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            hours.add_updater(lambda m, i=i: m.set_points_as_corners([
                zp(0, band_low(i)), zp(labor_for(band_high(i)), band_low(i)),
                zp(labor_for(band_high(i)), band_high(i)), zp(0, band_high(i)), zp(0, band_low(i))])
                .set_stroke(VC_COLOR, BAR_OUTLINE, opacity=float(band_visible(i)))
                .set_fill(VC_COLOR, AREA_OPACITY if band_visible(i) else 0))
            costs = Polygon(ORIGIN, RIGHT, UR, UP, color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            costs.add_updater(lambda m, i=i: m.set_points_as_corners([
                cp(band_low(i), fixed_amount.get_value()), cp(band_high(i), fixed_amount.get_value()),
                cp(band_high(i), fixed_amount.get_value()+variable(band_high(i))),
                cp(band_low(i), fixed_amount.get_value()+variable(band_high(i))), cp(band_low(i), fixed_amount.get_value())])
                .set_stroke(VC_COLOR, BAR_OUTLINE, opacity=float(band_visible(i)))
                .set_fill(VC_COLOR, AREA_OPACITY if band_visible(i) else 0))
            fixed = Polygon(ORIGIN, RIGHT, UR, UP, color=FC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            fixed.add_updater(lambda m, i=i: m.set_points_as_corners([
                cp(band_low(i), 0), cp(band_high(i), 0), cp(band_high(i), fixed_amount.get_value()),
                cp(band_low(i), fixed_amount.get_value()), cp(band_low(i), 0)]))
            hour_bars.add(hours)
            cost_bars.add(costs)
            fixed_bars.add(fixed)
        self.add(hour_bars, cost_bars)
        self.play(q_span.animate.set_value(100), shown.animate.set_value(100), cost_span.animate.set_value(TOTAL_MAX), run_time=3, rate_func=smooth)
        for bar in hour_bars:
            bar.clear_updaters()
        self.pause('2.o')

        # ---- 2.p · Fixed cost supplies the grey base; TC joins the upper-right corners of the stacked bars.
        self.remove(note)
        note = teaching('Add fixed cost to variable cost to get total cost.')
        self.add(fixed_bars)
        self.play(fixed_amount.animate.set_value(FIXED), FadeIn(note), run_time=1.5)
        for bar in (*cost_bars, *fixed_bars):
            bar.clear_updaters()
        tc_curve = polyline([cost_ax.c2p(q, total(q)) for q in np.linspace(0, 100, 121)], TC_COLOR, CURVE_WIDTH).set_z_index(DOT_LAYER)
        tc_word = Tex('TC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(100, total(100)), RIGHT, buff=0.15)
        fc_line = Line(cost_ax.c2p(0, FIXED), cost_ax.c2p(100, FIXED), color=FC_COLOR, stroke_width=CURVE_WIDTH).set_z_index(GUIDE_LAYER)
        fc_word = Tex('FC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(100, FIXED), RIGHT, buff=0.15)
        self.play(Create(tc_curve), FadeIn(tc_word), Create(fc_line), FadeIn(fc_word), run_time=1.5)
        self.pause('2.p')

        # ---- 3.a · Keep the pan; fade and translate the bars during the same movement. TC and FC travel together.
        zoom_curve.clear_updaters()
        f_curve = zoom_curve
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])
        self.remove(head, stored_wage, note)
        head = title('Cost Curves')
        production = VGroup(f_ax, f_words, f_curve, f_word)
        costs = VGroup(cost_ax, cost_words, tc_curve, tc_word, fc_line, fc_word)
        self.play(FadeIn(head), production.animate.shift(LEFT * PAN), costs.animate.shift(LEFT * PAN),
                  FadeOut(hour_bars, shift=LEFT * PAN), FadeOut(cost_bars, shift=LEFT * PAN), FadeOut(fixed_bars, shift=LEFT * PAN),
                  run_time=2, rate_func=smooth)
        self.remove(production)
        self.pause('3.a')

        # ---- 3.b · FC is already present; only its teaching line enters.
        note = teaching("Fixed costs, like rent, don't vary with inputs.")
        self.play(FadeIn(note))
        self.pause('3.b')

        # ---- 3.c · Stationary cost bands; only the active highlight switches while the dot and guides move.
        rest_cost_bars = VGroup(*[Polygon(cost_ax.c2p(q-5, 0), cost_ax.c2p(q, 0),
            cost_ax.c2p(q, total(q)), cost_ax.c2p(q-5, total(q)),
            color=MUTED, stroke_width=1, stroke_opacity=0.35, fill_color=MUTED, fill_opacity=0.10)
            for q in range(5, 101, 5)])
        bar_q = ValueTracker(70)
        selected_bar = lambda: max(0, min(MAX_BARS-1, int(np.ceil(bar_q.get_value()/5))-1))
        bar_fixed, bar_variable = VGroup(), VGroup()
        for i, right in enumerate(range(5, 101, 5)):
            fixed = Polygon(cost_ax.c2p(right-5, 0), cost_ax.c2p(right, 0),
                cost_ax.c2p(right, FIXED), cost_ax.c2p(right-5, FIXED),
                color=FC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            fixed.add_updater(lambda m, i=i: m.set_stroke(FC_COLOR, BAR_OUTLINE, opacity=float(i == selected_bar()))
                .set_fill(FC_COLOR, AREA_OPACITY if i == selected_bar() else 0))
            variable_bar = Polygon(cost_ax.c2p(right-5, FIXED), cost_ax.c2p(right, FIXED),
                cost_ax.c2p(right, total(right)), cost_ax.c2p(right-5, total(right)),
                color=VC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            variable_bar.add_updater(lambda m, i=i: m.set_stroke(VC_COLOR, BAR_OUTLINE, opacity=float(i == selected_bar()))
                .set_fill(VC_COLOR, AREA_OPACITY if i == selected_bar() else 0))
            bar_fixed.add(fixed)
            bar_variable.add(variable_bar)
        bar_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE)
        bar_word.add_updater(lambda m: m.next_to(bar_variable[selected_bar()], RIGHT, buff=0.12))
        bar_across = DashedLine(cost_ax.c2p(70, total(70)), cost_ax.c2p(0, total(70)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        bar_across.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(bar_q.get_value(), total(bar_q.get_value())), cost_ax.c2p(0, total(bar_q.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        bar_dot = Dot(cost_ax.c2p(70, total(70)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        bar_dot.add_updater(lambda m: m.move_to(cost_ax.c2p(bar_q.get_value(), total(bar_q.get_value()))))
        bar_total = DecimalNumber(total(70), num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        bar_total.add_updater(lambda m: m.set_value(round(total(bar_q.get_value()), 4))
            .next_to(cost_ax.c2p(0, total(bar_q.get_value())), LEFT, buff=0.2))
        bar_quantity = DecimalNumber(70, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        bar_quantity.add_updater(lambda m: m.set_value(round(bar_q.get_value(), 4))
            .move_to(cost_ax.c2p(bar_q.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        bar_guides = VGroup(bar_across, bar_dot, bar_total, bar_quantity)
        bar_marks = [bar_fixed, bar_variable, bar_word, bar_across, bar_dot, bar_total, bar_quantity]
        for m in bar_marks:
            m.update()
        self.remove(note)
        note = teaching('Variable costs are the costs that do change with inputs.')
        self.play(FadeIn(rest_cost_bars), *[FadeIn(m) for m in bar_marks], FadeIn(note))
        self.play(bar_q.animate.set_value(95), run_time=ROLL_TIME, rate_func=smooth)
        self.play(bar_q.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.c')

        # ---- 3.d · Keep the cost bands; the pink portion above FC explains TC = FC + VC.
        for m in bar_marks:
            m.update()
            m.clear_updaters(recurse=True)
        vc_curve = polyline([cost_ax.c2p(q, variable(q)) for q in np.linspace(0, 100, 121)], VC_COLOR, CURVE_WIDTH)
        vc_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(100, variable(100)), RIGHT, buff=0.15)
        divider = Line([DIVIDER_X, -3.0, 0], [DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        sum_row = MathTex(r'{{\mathrm{TC}}} = {{\mathrm{FC}}} + {{\mathrm{VC}}}')
        divided_row = MathTex(r'{{\frac{\mathrm{TC}}{Q}}} = {{\frac{\mathrm{FC}}{Q}}} + {{\frac{\mathrm{VC}}{Q}}}')
        average_row = MathTex(r'{{\mathrm{ATC}}} = {{\mathrm{AFC}}} + {{\mathrm{AVC}}}')
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

        # ---- 3.f · A second graph on the right for the averages. The average equation moves under the title as a
        # stored result, and ATC is traced as one tracker moves a point along TC: each cost divided by its quantity.
        # The same marks divide VC in 3.g and FC in 3.h: they read the cost being divided, and its average, from
        # `divided`.
        avg_ax = style_axes([0, 100, 10], [0, AVERAGE_MAX, 20], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        avg_ax.shift(RIGHT_ORIGIN - avg_ax.c2p(0, 0))
        avg_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(avg_ax.c2p(0, AVERAGE_MAX), LEFT, buff=0.23),
            Tex(r'\textsf{dollars per unit}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(0, AVERAGE_MAX), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(avg_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(100, 0), DOWN, buff=0.73))
        stored_average = subtitle(head, r'$\mathrm{ATC} = \mathrm{AFC} + \mathrm{AVC}$', book=True)
        self.remove(note)
        self.play(FadeOut(divider), FadeOut(sum_row), FadeOut(divided_row), FadeOut(bar_fixed), FadeOut(bar_variable), FadeOut(rest_cost_bars),
                  Transform(average_row, stored_average), FadeIn(avg_ax), FadeIn(avg_words), run_time=1.2)
        self.remove(average_row)
        self.add(stored_average)
        divided = {'cost': total, 'average': atc}
        per_unit = ValueTracker(10)
        average_reach = ValueTracker(10)   # how far along Q the average curve being traced is drawn
        cost_now = lambda: divided['cost'](per_unit.get_value())            # the cost being divided, at the point
        average_now = lambda: divided['average'](per_unit.get_value())      # and that cost per unit
        div_up = DashedLine(cost_ax.c2p(10, 0), cost_ax.c2p(10, total(10)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        div_up.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(per_unit.get_value(), 0), cost_ax.c2p(per_unit.get_value(), cost_now()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        div_point = Dot(cost_ax.c2p(10, total(10)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        div_point.add_updater(lambda m: m.move_to(cost_ax.c2p(per_unit.get_value(), cost_now())))
        div_across = DashedLine(cost_ax.c2p(10, total(10)), cost_ax.c2p(0, total(10)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        div_across.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(per_unit.get_value(), cost_now()), cost_ax.c2p(0, cost_now()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        div_cost = DecimalNumber(total(10), num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        div_cost.add_updater(lambda m: m.set_value(round(cost_now(), 4))
                             .next_to(cost_ax.c2p(0, cost_now()), LEFT, buff=0.2))
        div_units = DecimalNumber(10, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        div_units.add_updater(lambda m: m.set_value(round(per_unit.get_value(), 4))
                              .move_to(cost_ax.c2p(per_unit.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        avg_up = DashedLine(avg_ax.c2p(10, 0), avg_ax.c2p(10, atc(10)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        avg_up.add_updater(lambda m: m.become(DashedLine(
            avg_ax.c2p(per_unit.get_value(), 0), avg_ax.c2p(per_unit.get_value(), average_now()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        avg_point = Dot(avg_ax.c2p(10, atc(10)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        avg_point.add_updater(lambda m: m.move_to(avg_ax.c2p(per_unit.get_value(), average_now())))
        avg_across = DashedLine(avg_ax.c2p(10, atc(10)), avg_ax.c2p(0, atc(10)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        avg_across.add_updater(lambda m: m.become(DashedLine(
            avg_ax.c2p(per_unit.get_value(), average_now()), avg_ax.c2p(0, average_now()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        avg_cost = DecimalNumber(atc(10), num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        avg_cost.add_updater(lambda m: m.set_value(round(average_now(), 4))
                             .next_to(avg_ax.c2p(0, average_now()), LEFT, buff=0.2))
        avg_units = DecimalNumber(10, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        avg_units.add_updater(lambda m: m.set_value(round(per_unit.get_value(), 4))
                              .move_to(avg_ax.c2p(per_unit.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        atc_curve = polyline([avg_ax.c2p(ATC_START, atc(ATC_START)), avg_ax.c2p(10, atc(10))], ATC_COLOR, CURVE_WIDTH)
        atc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, atc(q)) for q in np.linspace(ATC_START, max(average_reach.get_value(), per_unit.get_value()), 121)]))
        atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, atc(100)), RIGHT, buff=0.15).shift(UP * 0.10)
        division_marks = [div_up, div_point, div_across, div_cost, div_units, avg_up, avg_point, avg_across, avg_cost, avg_units]
        for m in [*division_marks, atc_curve]:
            m.update()
        note = teaching('Average total cost: the cost associated with each unit of output.')
        self.play(*[FadeIn(m) for m in division_marks], FadeIn(atc_curve), FadeIn(note))
        self.play(per_unit.animate.set_value(90), run_time=SWEEP_TIME, rate_func=smooth)
        average_reach.set_value(90)
        self.play(per_unit.animate.set_value(50), average_reach.animate.set_value(100), FadeIn(atc_word),
                  run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.f')

        # ---- 3.g · AVC traced the same way: the point moves along VC and each variable cost is divided by its quantity.
        atc_curve.update()
        atc_curve.clear_updaters()
        avc_curve = polyline([avg_ax.c2p(q, avc(q)) for q in np.linspace(0, 10, 121)], AVC_COLOR, CURVE_WIDTH)
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, avc(q)) for q in np.linspace(0, max(average_reach.get_value(), per_unit.get_value()), 121)]))
        avc_word = Tex('AVC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, avc(100)), RIGHT, buff=0.15).shift(DOWN * 0.10)
        self.remove(note)
        note = teaching('Average variable cost: the costs from variable inputs for each unit of output.')
        self.play(*[FadeOut(m) for m in division_marks], run_time=0.5)
        divided['cost'], divided['average'] = variable, avc
        per_unit.set_value(10)
        average_reach.set_value(10)
        for m in [*division_marks, avc_curve]:
            m.update()
        self.play(Create(vc_curve), FadeIn(vc_word), run_time=1.0)
        self.play(*[FadeIn(m) for m in division_marks], FadeIn(avc_curve), FadeIn(note))
        self.play(per_unit.animate.set_value(90), run_time=SWEEP_TIME, rate_func=smooth)
        average_reach.set_value(90)
        self.play(per_unit.animate.set_value(50), average_reach.animate.set_value(100), FadeIn(avc_word),
                  run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.g')

        # ---- 3.h · AFC traced the same way, from the FC line: $1,000 divided by each quantity.
        avc_curve.update()
        avc_curve.clear_updaters()
        afc_curve = polyline([avg_ax.c2p(q, FIXED / q) for q in np.linspace(AFC_START, 10, 121)], AFC_COLOR, CURVE_WIDTH)
        afc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, FIXED / q) for q in np.linspace(AFC_START, max(average_reach.get_value(), per_unit.get_value()), 121)]))
        afc_word = Tex('AFC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, FIXED / 100), RIGHT, buff=0.15)
        self.remove(note)
        note = teaching('And the less important average fixed cost.')
        self.play(*[FadeOut(m) for m in division_marks], run_time=0.5)
        divided['cost'], divided['average'] = lambda Q: FIXED, lambda Q: FIXED / Q
        per_unit.set_value(10)
        average_reach.set_value(10)
        for m in [*division_marks, afc_curve]:
            m.update()
        self.play(*[FadeIn(m) for m in division_marks], FadeIn(afc_curve), FadeIn(note))
        self.play(per_unit.animate.set_value(90), run_time=SWEEP_TIME, rate_func=smooth)
        average_reach.set_value(90)
        self.play(per_unit.animate.set_value(50), average_reach.animate.set_value(100), FadeIn(afc_word),
                  run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.h')

        # ---- 3.i · The division marks and AFC fade out.
        for m in [*division_marks, afc_curve]:
            m.update()
            m.clear_updaters()
        self.remove(note)
        note = teaching("We'll focus on average total cost and average variable cost.")
        self.play(*[FadeOut(m) for m in division_marks], FadeOut(afc_curve), FadeOut(afc_word), FadeIn(note))
        self.pause('3.i')

        # ---- 3.j · The MC equation in the open space above the TC curve.
        mc_equation = MathTex(r'{{\mathrm{MC}}} = {{\frac{\Delta \mathrm{TC}}{\Delta Q}}}')
        mc_equation.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        mc_equation.move_to(cost_ax.c2p(27, TOTAL_MAX * 47/60))
        self.remove(note)
        note = teaching('Marginal cost: the cost of adding another unit.')
        self.play(FadeIn(mc_equation), FadeIn(note))
        self.pause('3.j')

        # ---- 3.k · Twenty adjoining outlined bands; each height is the average extra cost per unit
        # over its five-unit interval. With quadratic TC, that equals MC at the interval midpoint.
        swept = ValueTracker(0)
        strips = VGroup()
        for left in range(0, 100, 5):
            right = left + 5
            strip = Polygon(avg_ax.c2p(left, 0), avg_ax.c2p(right, 0),
                avg_ax.c2p(right, (total(right)-total(left))/5), avg_ax.c2p(left, (total(right)-total(left))/5),
                color=MC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
            strip.add_updater(lambda m, right=right: m.set_stroke(MC_COLOR, BAR_OUTLINE, opacity=float(swept.get_value() >= right))
                .set_fill(MC_COLOR, AREA_OPACITY if swept.get_value() >= right else 0))
            strips.add(strip)
        tc_rider = Dot(cost_ax.c2p(0, total(0)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        tc_rider.add_updater(lambda m: m.move_to(cost_ax.c2p(swept.get_value(), total(swept.get_value()))))
        self.remove(note)
        note = teaching('How much does total cost rise per additional unit?')
        strips.update()
        self.add(strips)
        self.play(FadeIn(tc_rider), FadeIn(note))
        self.play(swept.animate.set_value(100), run_time=SWEEP_TIME, rate_func=linear)
        self.pause('3.k')

        # ---- 3.m · MC passes through the band midpoints; the rider clears, then the bands fade.
        for m in (strips, tc_rider):
            m.clear_updaters(recurse=True)
        mc_trace = Line(avg_ax.c2p(0, 0), avg_ax.c2p(100, mc(100)), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, mc(100)), RIGHT, buff=0.15)
        self.remove(note)
        note = teaching('The cost of one more unit lands right on MC.')
        self.play(FadeOut(tc_rider), run_time=0.4)
        self.play(Create(mc_trace), FadeIn(mc_word), FadeIn(note), run_time=1.5)
        self.pause('3.m')
        self.play(FadeOut(strips), run_time=0.6)

        # ---- 3.n.below · Movement: one tracker moves a point along ATC with the MC point at the same quantity.
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
        move_marks = [move_up, move_atc, move_mc]
        for m in move_marks:
            m.update()
        self.remove(note)
        note = teaching('When MC lies below ATC, ATC bends downward.')
        self.play(FadeOut(mc_equation), *[FadeIn(m) for m in move_marks], FadeIn(note))
        self.play(moving_q.animate.set_value(20), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.n.below')

        # ---- 3.n · Past the lowest point MC lies above ATC and ATC rises.
        self.remove(note)
        note = teaching('When MC lies above ATC, ATC bends upward.')
        self.play(FadeIn(note), moving_q.animate.set_value(90), run_time=SWEEP_TIME, rate_func=smooth)
        self.pause('3.n')

        # ---- 3.o · Back to where they meet: a yellow point at ATC's lowest point, on MC.
        lowest = Dot(avg_ax.c2p(MIN_Q, atc(MIN_Q)), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER + 1)
        self.remove(note)
        note = teaching('The marginal cost curve runs through the minimum of ATC.')
        self.play(moving_q.animate.set_value(MIN_Q), run_time=ROLL_TIME, rate_func=smooth)
        for m in move_marks:
            m.update()
            m.clear_updaters()
        self.play(*[FadeOut(m) for m in move_marks], FadeIn(lowest), FadeIn(note))
        self.pause('3.o')

        # ---- 3.p · AFC fades back in: the fixed cost is the gap between ATC and AVC.
        self.remove(note)
        note = teaching('ATC is higher than AVC in the short run because we have fixed costs like rent.')
        self.play(FadeOut(lowest), FadeIn(afc_curve), FadeIn(afc_word), FadeIn(note))
        self.pause('3.p')

        # ---- 3.q · The long-run line.
        self.remove(note)
        note = teaching('In the long run, all costs are variable.')
        self.play(FadeIn(note))
        self.pause('3.q')

        # ---- 3.r · One tracker (the fixed part of cost) rolls from $1,000 to zero: FC drops to the axis and VC rises
        # onto TC; AFC drops to the axis and AVC rises onto ATC. Total cost is unchanged. VC's and AVC's words stop
        # just under TC's and ATC's; FC's and AFC's fade.
        fixed_part = ValueTracker(FIXED)
        fc_line.add_updater(lambda m: m.put_start_and_end_on(cost_ax.c2p(0, fixed_part.get_value()),
                                                             cost_ax.c2p(100, fixed_part.get_value())))
        fc_word.add_updater(lambda m: m.next_to(cost_ax.c2p(100, fixed_part.get_value()), RIGHT, buff=0.15)
                            .set_opacity(fixed_part.get_value() / FIXED))
        vc_curve.add_updater(lambda m: m.set_points_as_corners(
            [cost_ax.c2p(q, variable(q) + FIXED - fixed_part.get_value()) for q in np.linspace(0, 100, 121)]))
        vc_word.add_updater(lambda m: m.next_to(cost_ax.c2p(100, variable(100) + FIXED - fixed_part.get_value()), RIGHT, buff=0.15)
                            .set_y(min(cost_ax.c2p(100, variable(100) + FIXED - fixed_part.get_value())[1], tc_word.get_y() - 0.32)))
        afc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, fixed_part.get_value() / q) for q in np.linspace(max(fixed_part.get_value() / AVERAGE_TOP, 0.01), 100, 121)]))
        afc_word.add_updater(lambda m: m.next_to(avg_ax.c2p(100, fixed_part.get_value() / 100), RIGHT, buff=0.15)
                             .set_opacity(fixed_part.get_value() / FIXED))
        # AVC = (w/100)Q + (the part of the fixed cost now counted as variable)/Q; it starts where that reaches AVERAGE_TOP.
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, avc(q) + (FIXED - fixed_part.get_value()) / q)
             for q in np.linspace(max((AVERAGE_TOP - np.sqrt(AVERAGE_TOP**2 - 4*COST_ALPHA*(FIXED-fixed_part.get_value()))) / (2*COST_ALPHA),
                                       0.01), 100, 121)]))
        avc_word.add_updater(lambda m: m.next_to(avg_ax.c2p(100, avc(100)), RIGHT, buff=0.15)
                             .set_y(min(avg_ax.c2p(100, avc(100) + (FIXED - fixed_part.get_value()) / 100)[1], atc_word.get_y() - 0.32)))
        long_run = [fc_line, fc_word, vc_curve, vc_word, afc_curve, afc_word, avc_curve, avc_word]
        for m in long_run:
            m.update()
        self.remove(note)
        note = teaching('Fixed cost, and therefore average fixed cost as well, go to zero.')
        self.play(FadeIn(note), fixed_part.animate.set_value(0), run_time=SWEEP_TIME, rate_func=smooth)
        for m in long_run:
            m.update()
            m.clear_updaters()
        # The two pairs now share a curve, so each pair takes one word instead of two stacked ones.
        tc_vc = MathTex(r'\mathrm{TC} = \mathrm{VC}').scale(CURVE_WORD_SCALE).move_to(tc_word, aligned_edge=LEFT)
        atc_avc = MathTex(r'\mathrm{ATC} = \mathrm{AVC}').scale(CURVE_WORD_SCALE)
        atc_avc.next_to(avg_ax.c2p(100, atc(100)), UP, buff=0.2).set_x(7.35 - atc_avc.width / 2)   # inside the safe margin
        self.play(FadeOut(vc_word), FadeOut(avc_word), FadeOut(tc_word), FadeOut(atc_word), FadeIn(tc_vc), FadeIn(atc_avc),
                  run_time=0.6)
        self.pause('3.r')

        # ---- 4.a · The firm's objective, the first line of the firm's-problem card.
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])   # trackers join the scene when animated
        FadeAll(self)
        self.clear()
        head = title('Marginal Revenue')
        objective = MathTex(r'\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}').move_to([0, BODY_MID + 0.5, 0])
        note = teaching('In this class, firms aim to maximize profit.')
        self.play(FadeIn(head), FadeIn(objective), FadeIn(note))
        self.pause('4.a')

        # ---- 4.b · The punch line under it: MC = MR.
        rule = MathTex(r'{{\mathrm{MC}}} = {{\mathrm{MR}}}').move_to([0, BODY_MID - 0.6, 0])
        rule.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        rule.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        self.remove(note)
        note = teaching('A firm maximizes profit where marginal cost equals marginal revenue.')
        self.play(FadeIn(rule), FadeIn(note))
        self.pause('4.b')

        # ---- 4.c · Both lines move under the title as stored results. On the firm's cost graph (MC, ATC; AVC left out
        # because MR shares its pink), MR is an illustrative line whose slope one tracker tilts:
        # flat, steep, and back. The red point where MC = MR and its quantity follow.
        stored_objective = subtitle(head, r'$\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}$', book=True)
        stored_rule = Tex(r'$\mathrm{MC} = \mathrm{MR}$', color=CAPTION).scale(SCALE_CAPTION)
        stored_rule.next_to(stored_objective, RIGHT, buff=0.6)
        stored_rule.shift(UP * (stored_objective.family_members_with_points()[-1].get_bottom()[1]
                                - stored_rule.family_members_with_points()[0].get_bottom()[1]))
        firm_ax = style_axes([0, 100, 10], [0, AVERAGE_MAX, 20], x_length=5.6, y_length=GRAPH_SIZE)
        firm_ax.shift(np.array([-2.8, LEFT_ORIGIN[1], 0]) - firm_ax.c2p(0, 0))
        firm_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(firm_ax.c2p(0, AVERAGE_MAX), LEFT, buff=0.23),
            Tex(r'\textsf{dollars per unit}', color=CAPTION).scale(0.55).next_to(firm_ax.c2p(0, AVERAGE_MAX), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(firm_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(firm_ax.c2p(100, 0), DOWN, buff=0.73))
        firm_mc = Line(firm_ax.c2p(0, 0), firm_ax.c2p(100, mc(100)), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        firm_mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(100, mc(100)), RIGHT, buff=0.15)
        firm_atc = polyline([firm_ax.c2p(q, atc(q)) for q in np.linspace(ATC_START, 100, 121)], ATC_COLOR, CURVE_WIDTH)
        firm_atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(100, atc(100)), RIGHT, buff=0.15)
        MR_INTERCEPT = 0.8 * mc(100)
        tilt = ValueTracker(2 * COST_ALPHA)
        mr_end = lambda: 100 if tilt.get_value() <= MR_INTERCEPT/100 else MR_INTERCEPT / tilt.get_value()
        best_q = lambda: MR_INTERCEPT / (2 * COST_ALPHA + tilt.get_value())
        mr_line = Line(firm_ax.c2p(0, MR_INTERCEPT), firm_ax.c2p(80, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH)
        mr_line.add_updater(lambda m: m.put_start_and_end_on(
            firm_ax.c2p(0, MR_INTERCEPT), firm_ax.c2p(mr_end(), MR_INTERCEPT - tilt.get_value() * mr_end())))
        mr_word = Tex('MR', color=INK).scale(CURVE_WORD_SCALE)
        mr_word.add_updater(lambda m: m.next_to(firm_ax.c2p(mr_end(), MR_INTERCEPT - tilt.get_value() * mr_end()),
                                                RIGHT if mr_end() == 100 else UR, buff=0.12))
        best_point = Dot(firm_ax.c2p(40, mc(40)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        best_point.add_updater(lambda m: m.move_to(firm_ax.c2p(best_q(), mc(best_q()))))
        best_drop = DashedLine(firm_ax.c2p(40, 0), firm_ax.c2p(40, mc(40)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        best_drop.add_updater(lambda m: m.become(DashedLine(firm_ax.c2p(best_q(), 0), firm_ax.c2p(best_q(), mc(best_q())),
                                                            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        best_number = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        best_number.add_updater(lambda m: m.set_value(round(best_q(), 4))
                                .move_to(firm_ax.c2p(best_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        best_symbol = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        best_symbol.add_updater(lambda m: m.move_to(firm_ax.c2p(best_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        tilt_marks = [mr_line, mr_word, best_point, best_drop, best_number, best_symbol]
        for m in tilt_marks:
            m.update()
        self.remove(note)
        self.play(Transform(objective, stored_objective), Transform(rule, stored_rule), run_time=1.0)
        self.remove(objective, rule)
        self.add(stored_objective, stored_rule)
        note = teaching('Think of marginal revenue as some abstract curve that can take many shapes.')
        self.play(FadeIn(firm_ax), FadeIn(firm_words), FadeIn(firm_mc), FadeIn(firm_mc_word), FadeIn(firm_atc),
                  FadeIn(firm_atc_word), FadeIn(note))
        self.play(*[FadeIn(m) for m in tilt_marks])
        self.play(tilt.animate.set_value(0), run_time=ROLL_TIME, rate_func=smooth)
        self.play(tilt.animate.set_value(6 * COST_ALPHA), run_time=SWEEP_TIME, rate_func=smooth)
        self.play(tilt.animate.set_value(2 * COST_ALPHA), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('4.c')

        # ---- 4.d.market · Back to buyers and sellers: Part C's market, supply and demand, MB = 12 - Q/5 and
        # MC = 2 + Q/20, crossing at 40 units and $4 (a red point).
        for m in tilt_marks:
            m.update()
            m.clear_updaters()
        market_ax = style_axes([0, 60, 10], [0, 13, 2], x_length=5.0, y_length=GRAPH_SIZE)
        market_ax.shift(np.array([-5.4, LEFT_ORIGIN[1], 0]) - market_ax.c2p(0, 0))
        market_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(market_ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(market_ax.c2p(0, 13), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(market_ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(market_ax.c2p(60, 0), DOWN, buff=0.73))
        mb = lambda q: 12 - q / 5
        market_mc = lambda q: 2 + q / 20
        demand = Line(market_ax.c2p(0, 12), market_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        supply = Line(market_ax.c2p(0, 2), market_ax.c2p(60, 5), color=SUPPLY, stroke_width=CURVE_WIDTH)
        demand_word = Tex('D / MB', color=INK).scale(CURVE_WORD_SCALE).next_to(market_ax.c2p(60, 0), UR, buff=0.12)
        supply_word = Tex('S / MC', color=INK).scale(CURVE_WORD_SCALE).next_to(market_ax.c2p(60, 5), RIGHT, buff=0.15)
        # The crossing sits above the unit's two dots, so it stays red when the unit reaches it in 4.d.
        crossing = Dot(market_ax.c2p(40, 4), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER + 1)
        self.remove(note)
        note = teaching('Markets set quantity where marginal benefits equal marginal costs.')
        self.play(FadeOut(firm_ax), FadeOut(firm_words), FadeOut(firm_mc), FadeOut(firm_mc_word), FadeOut(firm_atc),
                  FadeOut(firm_atc_word), *[FadeOut(m) for m in tilt_marks], run_time=0.6)
        self.play(FadeIn(market_ax), FadeIn(market_words), FadeIn(demand), FadeIn(supply), FadeIn(demand_word),
                  FadeIn(supply_word), FadeIn(note))
        self.play(FadeIn(crossing), run_time=0.5)
        self.pause('4.d.market')

        # ---- 4.d.unit · One unit, the 10th: a white line up from Q = 10 with its benefit and cost marked on the
        # curves, and alongside the graph two columns at the same price scale: MB ($10.00) above MC ($2.50).
        unit = ValueTracker(10)
        price_y = lambda p: market_ax.c2p(0, p)[1]
        unit_line = Line(market_ax.c2p(10, 0), market_ax.c2p(10, 10), color=INK, stroke_width=2.5)
        unit_line.add_updater(lambda m: m.put_start_and_end_on(market_ax.c2p(unit.get_value(), 0),
                                                               market_ax.c2p(unit.get_value(), mb(unit.get_value()))))
        unit_dots = VGroup(Dot(radius=0.065, color=DEMAND), Dot(radius=0.065, color=SUPPLY)).set_z_index(DOT_LAYER)
        unit_dots.add_updater(lambda m: (m[0].move_to(market_ax.c2p(unit.get_value(), mb(unit.get_value()))),
                                         m[1].move_to(market_ax.c2p(unit.get_value(), market_mc(unit.get_value())))))
        unit_number = DecimalNumber(10, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        unit_number.add_updater(lambda m: m.set_value(round(unit.get_value(), 4))
                                .move_to(market_ax.c2p(unit.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        # The two columns: faint fill, a solid value edge on top, value outside, name under the base.
        BENEFIT_LEFT, COST_LEFT, COLUMN_W = 1.9, 2.6, 0.5
        base_y = market_ax.c2p(0, 0)[1]
        COLUMN_FILL = 0.4
        benefit_column = Polygon([0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], stroke_width=0, fill_color=DEMAND, fill_opacity=COLUMN_FILL)
        benefit_column.add_updater(lambda m: m.set_points_as_corners([
            [BENEFIT_LEFT, base_y, 0], [BENEFIT_LEFT + COLUMN_W, base_y, 0],
            [BENEFIT_LEFT + COLUMN_W, price_y(mb(unit.get_value())), 0], [BENEFIT_LEFT, price_y(mb(unit.get_value())), 0],
            [BENEFIT_LEFT, base_y, 0]]))
        cost_column = Polygon([0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], stroke_width=0, fill_color=SUPPLY, fill_opacity=COLUMN_FILL)
        cost_column.add_updater(lambda m: m.set_points_as_corners([
            [COST_LEFT, base_y, 0], [COST_LEFT + COLUMN_W, base_y, 0],
            [COST_LEFT + COLUMN_W, price_y(market_mc(unit.get_value())), 0], [COST_LEFT, price_y(market_mc(unit.get_value())), 0],
            [COST_LEFT, base_y, 0]]))
        benefit_edge = Line([BENEFIT_LEFT, 0, 0], [BENEFIT_LEFT + COLUMN_W, 0, 0], color=DEMAND, stroke_width=CURVE_WIDTH)
        benefit_edge.add_updater(lambda m: m.set_y(price_y(mb(unit.get_value()))))
        cost_edge = Line([COST_LEFT, 0, 0], [COST_LEFT + COLUMN_W, 0, 0], color=SUPPLY, stroke_width=CURVE_WIDTH)
        cost_edge.add_updater(lambda m: m.set_y(price_y(market_mc(unit.get_value()))))
        column_base = Line([BENEFIT_LEFT - 0.15, base_y, 0], [COST_LEFT + COLUMN_W + 0.15, base_y, 0], color=MUTED)
        column_names = VGroup(
            Tex('MB', color=DEMAND).scale(0.6).move_to([BENEFIT_LEFT + COLUMN_W / 2, base_y - 0.3, 0]),
            Tex('MC', color=SUPPLY).scale(0.6).move_to([COST_LEFT + COLUMN_W / 2, base_y - 0.3, 0]))
        benefit_value = VGroup(Tex(r'\$', color=DEMAND), DecimalNumber(10, num_decimal_places=2, color=DEMAND)).scale(0.6)
        benefit_value.add_updater(lambda m: (m[1].set_value(mb(unit.get_value())), m.arrange(RIGHT, buff=0.04),
                                             m.next_to([BENEFIT_LEFT, price_y(mb(unit.get_value())), 0], LEFT, buff=0.15)))
        cost_value = VGroup(Tex(r'\$', color=SUPPLY), DecimalNumber(2.5, num_decimal_places=2, color=SUPPLY)).scale(0.6)
        cost_value.add_updater(lambda m: (m[1].set_value(market_mc(unit.get_value())), m.arrange(RIGHT, buff=0.04),
                                          m.next_to([COST_LEFT + COLUMN_W, price_y(market_mc(unit.get_value())), 0], RIGHT, buff=0.15)))
        unit_marks = [unit_line, unit_dots, unit_number, benefit_column, cost_column, benefit_edge, cost_edge,
                      benefit_value, cost_value]
        for m in unit_marks:
            m.update()
        self.remove(note)
        note = teaching('Sellers make one more unit while the benefits exceed the cost of adding it.')
        self.play(FadeIn(unit_line), FadeIn(unit_dots), FadeIn(unit_number))
        self.play(FadeIn(column_base), FadeIn(column_names), FadeIn(benefit_column), FadeIn(cost_column),
                  FadeIn(benefit_edge), FadeIn(cost_edge), FadeIn(benefit_value), FadeIn(cost_value), FadeIn(note))
        self.pause('4.d.unit')

        # ---- 4.d · Units are added until the columns are equal: the 40th unit breaks even at $4.00.
        self.remove(note)
        note = teaching('Keep adding units until an additional unit breaks even.')
        self.play(FadeIn(note), unit.animate.set_value(40), run_time=SWEEP_TIME, rate_func=smooth)
        self.pause('4.d')

        # ---- 4.e · MC = MR on the screen, right of the equal columns.
        for m in unit_marks:
            m.update()
            m.clear_updaters()
        big_rule = MathTex(r'{{\mathrm{MC}}} = {{\mathrm{MR}}}').scale(1.3).move_to([5.6, BODY_MID + 0.3, 0])
        big_rule.get_part_by_tex(r'\mathrm{MC}').set_color(MC_COLOR)
        big_rule.get_part_by_tex(r'\mathrm{MR}').set_color(MR_COLOR)
        self.remove(note)
        note = teaching('The best decision is the quantity where marginal cost equals marginal revenue.')
        self.play(FadeIn(big_rule), FadeIn(note))
        self.pause('4.e')

        # ---- 4.f · Next time: the two models side by side, the competitive firm's flat P = MR and the monopolist's
        # sloped MR, each with MC and the red point where MC = MR. No numbers.
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])   # trackers join the scene when animated
        FadeAll(self)
        self.clear()
        head = title('Next Time')
        pc_ax = style_axes([0, 100, 10], [0, AVERAGE_MAX, 20], x_length=4.6, y_length=3.6)
        pc_ax.shift(np.array([-6.6, BODY_MID - 1.95, 0]) - pc_ax.c2p(0, 0))
        mono_ax = style_axes([0, 100, 10], [0, AVERAGE_MAX, 20], x_length=4.6, y_length=3.6)
        mono_ax.shift(np.array([1.4, BODY_MID - 1.95, 0]) - mono_ax.c2p(0, 0))
        pc_panel = VGroup(
            pc_ax,
            Tex('Perfect Competition', color=INK).scale(0.8).next_to(pc_ax.c2p(50, AVERAGE_MAX), UP, buff=0.35),
            Tex(r'\$', color=INK).scale(0.8).next_to(pc_ax.c2p(0, AVERAGE_MAX), LEFT, buff=0.23),
            Tex('Q', color=INK).scale(0.8).next_to(pc_ax.c2p(100, 0), DOWN, buff=0.23),
            Line(pc_ax.c2p(0, 0), pc_ax.c2p(100, mc(100)), color=MC_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(pc_ax.c2p(100, mc(100)), RIGHT, buff=0.15),
            Line(pc_ax.c2p(0, mc(60)), pc_ax.c2p(100, mc(60)), color=DEMAND, stroke_width=CURVE_WIDTH),
            Tex('P = MR', color=INK).scale(CURVE_WORD_SCALE).next_to(pc_ax.c2p(100, mc(60)), RIGHT, buff=0.15),
            Dot(pc_ax.c2p(60, mc(60)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER))
        mono_panel = VGroup(
            mono_ax,
            Tex('Monopoly', color=INK).scale(0.8).next_to(mono_ax.c2p(50, AVERAGE_MAX), UP, buff=0.35),
            Tex(r'\$', color=INK).scale(0.8).next_to(mono_ax.c2p(0, AVERAGE_MAX), LEFT, buff=0.23),
            Tex('Q', color=INK).scale(0.8).next_to(mono_ax.c2p(100, 0), DOWN, buff=0.23),
            Line(mono_ax.c2p(0, 0), mono_ax.c2p(100, mc(100)), color=MC_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(100, mc(100)), RIGHT, buff=0.15),
            Line(mono_ax.c2p(0, AVERAGE_MAX), mono_ax.c2p(100, mc(20)), color=DEMAND, stroke_width=CURVE_WIDTH),
            Tex('D', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(100, mc(20)), RIGHT, buff=0.15),
            Line(mono_ax.c2p(0, AVERAGE_MAX), mono_ax.c2p(60, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MR', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(60, 0), UR, buff=0.12),
            Dot(mono_ax.c2p(40, mc(40)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER))
        note = teaching('Marginal revenue in monopoly and perfect competition.')
        self.play(FadeIn(head), FadeIn(pc_panel), FadeIn(mono_panel), FadeIn(note))
        self.pause('4.f')
