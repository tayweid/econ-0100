# maniml E1_Animation.py EpisodeE1
# Storyboard: E1_Notes.md. All lesson choreography stays in construct().
# How sellers choose: the market structures ahead, costs from the production function, the cost curves, MC = MR.
# One firm throughout: Q = F(L) = 10 sqrt(L) workers to units, a $50 wage and a $1,000 fixed cost, so VC = Q^2/2,
# TC = 1000 + Q^2/2, MC = Q, AVC = Q/2, AFC = 1000/Q, ATC = Q/2 + 1000/Q (lowest at Q = sqrt(2000), about 44.7).
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
from style import avatar, speech        # the guide's placeholder seller (style.py leaves these out of *)

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
        BRACE_GAP = 1.2                        # units of L or Q left open between neighbouring step braces
        # Taxonomy grid, E4's object: a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4
        TAXONOMY_SIDE_SCALE, CHECKLIST_LEFT = 0.72, 0.6
        BOX_BUFF = 0.12                          # E2-E4's 0.22 would meet the cell rules on the shrunk grid

        # The model, as one-line functions. shape is the production function's exponent: 0.5 gives
        # F(L) = 10 sqrt(L); 1 gives the straight line of 2.p.linear. Every other section has shape = 0.5.
        WAGE, FIXED = 50, 1000
        shape = ValueTracker(0.5)
        output = lambda L: 100 * (L / 100) ** shape.get_value()             # Q = F(L)
        labor_for = lambda Q: 100 * (Q / 100) ** (1 / shape.get_value())    # the workers Q needs
        total = lambda Q: FIXED + WAGE * labor_for(Q)                       # TC = FC + w L
        variable = lambda Q: Q ** 2 / 2
        mc = lambda Q: Q
        atc = lambda Q: Q / 2 + FIXED / Q
        MIN_Q = np.sqrt(2 * FIXED)                                          # 44.72: MC = ATC at ATC's lowest point
        AVERAGE_TOP = 105                  # average curves stop at $105, clear of the axis caption above them
        ATC_START = (2 * AVERAGE_TOP - np.sqrt((2 * AVERAGE_TOP) ** 2 - 8 * FIXED)) / 2   # 10: where ATC = 105
        AFC_START = FIXED / AVERAGE_TOP                                                   # 9.5: where AFC = 105

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

        # ---- 0.a · The shared bumper with E1's thesis, the line under the notes' heading.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 1)
        thesis = Tex(r'\textit{How sellers choose}', color=CAPTION).scale(0.9)
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

        # ---- 1.b · The supply curve we have relied on, and the seller with a question (the guide's avatar placeholder).
        supply_ax = style_axes([0, 10, 1], [0, 10, 1], x_length=3.6, y_length=3.6)
        supply_ax.shift(np.array([1.0, BODY_MID - 1.8, 0]) - supply_ax.c2p(0, 0))
        supply_words = VGroup(
            Tex('P', color=INK).scale(0.8).next_to(supply_ax.c2p(0, 10), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(0, 10), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(supply_ax.c2p(10, 0), DOWN, buff=0.73))
        supply_line = Line(supply_ax.c2p(0, 2), supply_ax.c2p(10, 8), color=SUPPLY, stroke_width=CURVE_WIDTH)
        supply_word = Tex('S', color=INK).scale(CURVE_WORD_SCALE).next_to(supply_ax.c2p(10, 8), RIGHT, buff=0.15)
        seller = avatar('Seller', color=SUPPLY).move_to([5.7, BODY_MID - 0.5, 0])
        question_mark = speech(seller, '?')
        note = teaching('What are the incentives that give rise to the supply curve?')
        self.play(FadeIn(supply_ax), FadeIn(supply_words), FadeIn(supply_line), FadeIn(supply_word))
        self.play(FadeIn(seller), FadeIn(question_mark), FadeIn(note))
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
        f_ax = style_axes([0, 100, 10], [0, 100, 10], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        f_ax.shift(LEFT_ORIGIN - f_ax.c2p(0, 0))
        f_words = VGroup(
            Tex('Q', color=INK).scale(0.8).next_to(f_ax.c2p(0, 100), LEFT, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(0, 100), RIGHT, buff=0.22),
            Tex('L', color=INK).scale(0.8).next_to(f_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{workers}', color=CAPTION).scale(0.55).next_to(f_ax.c2p(100, 0), DOWN, buff=0.73))
        # Sampled densely near zero, where the square root is steep; redrawn from shape every frame.
        f_curve = polyline([f_ax.c2p(100 * t ** 2, output(100 * t ** 2)) for t in np.linspace(0, 1, 121)], F_COLOR, CURVE_WIDTH)
        f_curve.add_updater(lambda m: m.set_points_as_corners(
            [f_ax.c2p(100 * t ** 2, output(100 * t ** 2)) for t in np.linspace(0, 1, 121)]))
        f_word = Tex('$F(L)$', color=INK).scale(CURVE_WORD_SCALE).next_to(f_ax.c2p(100, 100), RIGHT, buff=0.15)
        self.play(FadeIn(head), FadeIn(f_ax), FadeIn(f_words), FadeIn(f_curve), FadeIn(f_word))
        self.pause('2.a')

        # ---- 2.b · A line from labor to quantity: up from 25 workers to F, then across to 50 units.
        # One tracker (workers) drives the dot, both guides and both numbers.
        workers = ValueTracker(25)
        work_up = DashedLine(f_ax.c2p(25, 0), f_ax.c2p(25, 50), color=GUIDE, stroke_width=GUIDE_WIDTH)
        work_up.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(workers.get_value(), 0), f_ax.c2p(workers.get_value(), output(workers.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        work_dot = Dot(f_ax.c2p(25, 50), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        work_dot.add_updater(lambda m: m.move_to(f_ax.c2p(workers.get_value(), output(workers.get_value()))))
        work_across = DashedLine(f_ax.c2p(25, 50), f_ax.c2p(0, 50), color=GUIDE, stroke_width=GUIDE_WIDTH)
        work_across.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(workers.get_value(), output(workers.get_value())), f_ax.c2p(0, output(workers.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        work_number = DecimalNumber(25, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        work_number.add_updater(lambda m: m.set_value(round(workers.get_value(), 4))
                                .move_to(f_ax.c2p(workers.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        made_number = DecimalNumber(50, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        made_number.add_updater(lambda m: m.set_value(round(output(workers.get_value()), 4))
                                .next_to(f_ax.c2p(0, output(workers.get_value())), LEFT, buff=0.2))
        labor_marks = [work_up, work_dot, work_across, work_number, made_number]
        for m in labor_marks:
            m.update()                     # digits and dashes current before anything fades in
        note = teaching('The production function takes inputs and gives us some output quantity.')
        self.play(Create(work_up), FadeIn(work_number), FadeIn(note))
        self.play(FadeIn(work_dot), run_time=0.4)
        self.play(Create(work_across), FadeIn(made_number))
        self.pause('2.b')

        # ---- 2.c · Labor up to 81 workers (90 units), then back down to 25 (50 units).
        self.remove(note)
        note = teaching('Increasing output means we need more inputs, either from labor or capital.')
        self.play(FadeIn(note), workers.animate.set_value(81), run_time=ROLL_TIME, rate_func=smooth)
        self.play(workers.animate.set_value(25), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.c')

        # ---- 2.d · Double the labor: a second line at 50 workers, then its quantity, 71 units (70.7).
        for m in labor_marks:
            m.update()
            m.clear_updaters()             # the tracked line stays behind as the first labor line
        double_up = DashedLine(f_ax.c2p(50, 0), f_ax.c2p(50, output(50)), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        double_dot = Dot(f_ax.c2p(50, output(50)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        double_across = DashedLine(f_ax.c2p(50, output(50)), f_ax.c2p(0, output(50)), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        double_work = Tex('50', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(f_ax.c2p(50, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        double_made = Tex('71', color=GUIDE).scale(READOUT_SCALE).next_to(f_ax.c2p(0, output(50)), LEFT, buff=0.2)
        self.remove(note)
        note = teaching("If we double labor input, quantity goes up but doesn't quite double.")
        self.play(Create(double_up), FadeIn(double_work), FadeIn(note))
        self.play(FadeIn(double_dot), Create(double_across), FadeIn(double_made))
        self.pause('2.d')

        # ---- 2.e · Triple: a third line at 75 workers, the same step in labor, then its quantity, 87 units (86.6).
        triple_up = DashedLine(f_ax.c2p(75, 0), f_ax.c2p(75, output(75)), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        triple_dot = Dot(f_ax.c2p(75, output(75)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        triple_across = DashedLine(f_ax.c2p(75, output(75)), f_ax.c2p(0, output(75)), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        triple_work = Tex('75', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(f_ax.c2p(75, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        triple_made = Tex('87', color=GUIDE).scale(READOUT_SCALE).next_to(f_ax.c2p(0, output(75)), LEFT, buff=0.2)
        self.remove(note)
        note = teaching('A third labor input with the same increase in labor.')
        self.play(Create(triple_up), FadeIn(triple_work), FadeIn(note))
        self.play(FadeIn(triple_dot), Create(triple_across), FadeIn(triple_made))
        self.pause('2.e')

        # ---- 2.f · A brace under each labor step and beside each output step, one pair at a time:
        # equal steps of 25 workers, output steps of 50, 21 and 16 units.
        steps = [(0, 25), (25, 50), (50, 75)]
        input_braces = VGroup(*[Brace(Line(f_ax.c2p(a + BRACE_GAP, 0), f_ax.c2p(b - BRACE_GAP, 0)), DOWN, buff=0.55,
                                      color=CAPTION) for a, b in steps])
        output_braces = VGroup(*[Brace(Line(f_ax.c2p(0, output(a) + BRACE_GAP), f_ax.c2p(0, output(b) - BRACE_GAP)), LEFT,
                                       buff=0.72, color=CAPTION) for a, b in steps])
        self.remove(note)
        note = teaching('Diminishing marginal return: more inputs lead to increasingly small increases.')
        self.play(FadeIn(input_braces[0]), FadeIn(output_braces[0]), FadeIn(note))
        self.play(FadeIn(input_braces[1]), FadeIn(output_braces[1]))
        self.play(FadeIn(input_braces[2]), FadeIn(output_braces[2]))
        self.pause('2.f')

        # ---- 2.g · Run through the three pairs again, each pair pulsing in turn.
        self.remove(note)
        note = teaching('As it becomes flatter, more inputs lead to more output but less efficiently.')
        self.play(FadeIn(note))
        for i in range(3):
            self.play(Indicate(input_braces[i], color=FOCUS, scale_factor=1.2),
                      Indicate(output_braces[i], color=FOCUS, scale_factor=1.2), run_time=0.8)
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

        # ---- 2.j · The cost graph to the right of the production function; the labor lines and braces clear, and the
        # wage equation moves under the title as a stored result with the wage.
        cost_ax = style_axes([0, 100, 10], [0, 6000, 1000], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        cost_ax.shift(RIGHT_ORIGIN - cost_ax.c2p(0, 0))
        cost_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(cost_ax.c2p(0, 6000), LEFT, buff=0.23),
            Tex(r'\textsf{dollars}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(0, 6000), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(cost_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(cost_ax.c2p(100, 0), DOWN, buff=0.73))
        stored_equation = subtitle(head, r'$\mathrm{VC} = L \cdot w$', book=True)
        stored_wage = Tex(r'$w = \$50$ per worker', color=CAPTION).scale(SCALE_CAPTION)
        stored_wage.next_to(stored_equation, RIGHT, buff=0.5)
        stored_wage.shift(UP * (stored_equation.family_members_with_points()[-1].get_bottom()[1]
                                - stored_wage.family_members_with_points()[0].get_bottom()[1]))
        step_marks = VGroup(*labor_marks, double_up, double_dot, double_across, double_work, double_made,
                            triple_up, triple_dot, triple_across, triple_work, triple_made, input_braces, output_braces)
        self.remove(note)
        note = teaching('Quantity of output on the horizontal and value on the vertical.')
        self.play(FadeOut(step_marks), Transform(wage_equation, stored_equation), run_time=1.0)
        self.remove(wage_equation)
        self.add(stored_equation)
        self.play(FadeIn(stored_wage), FadeIn(cost_ax), FadeIn(cost_words), FadeIn(note))
        self.pause('2.j')

        # ---- 2.k · Zero output: no workers, yet $1,000 of cost. One tracker (quantity, the output) drives every mark
        # of 2.k to 2.q on both graphs: the workers it needs and what they cost.
        quantity = ValueTracker(0)
        reach = ValueTracker(0)            # how far along Q the TC curve has been traced
        level_axis_dot = Dot(f_ax.c2p(0, 0), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        level_axis_dot.add_updater(lambda m: m.move_to(f_ax.c2p(0, quantity.get_value())))
        level_made = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        level_made.add_updater(lambda m: m.set_value(round(quantity.get_value(), 4))
                               .next_to(f_ax.c2p(0, quantity.get_value()), LEFT, buff=0.2))
        level_across = DashedLine(f_ax.c2p(0, 20), f_ax.c2p(4, 20), color=GUIDE, stroke_width=GUIDE_WIDTH)
        level_across.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(0, quantity.get_value()), f_ax.c2p(labor_for(quantity.get_value()), quantity.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        level_point = Dot(f_ax.c2p(0, 0), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        level_point.add_updater(lambda m: m.move_to(f_ax.c2p(labor_for(quantity.get_value()), quantity.get_value())))
        level_down = DashedLine(f_ax.c2p(4, 20), f_ax.c2p(4, 0), color=GUIDE, stroke_width=GUIDE_WIDTH)
        level_down.add_updater(lambda m: m.become(DashedLine(
            f_ax.c2p(labor_for(quantity.get_value()), quantity.get_value()), f_ax.c2p(labor_for(quantity.get_value()), 0),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        level_workers = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        level_workers.add_updater(lambda m: m.set_value(round(labor_for(quantity.get_value()), 4))
                                  .move_to(f_ax.c2p(labor_for(quantity.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        level_units = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        level_units.add_updater(lambda m: m.set_value(round(quantity.get_value(), 4))
                                .move_to(cost_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        level_up = DashedLine(cost_ax.c2p(20, 0), cost_ax.c2p(20, 1200), color=GUIDE, stroke_width=GUIDE_WIDTH)
        level_up.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(quantity.get_value(), 0), cost_ax.c2p(quantity.get_value(), total(quantity.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        level_cost_point = Dot(cost_ax.c2p(0, FIXED), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        level_cost_point.add_updater(lambda m: m.move_to(cost_ax.c2p(quantity.get_value(), total(quantity.get_value()))))
        level_cost_across = DashedLine(cost_ax.c2p(20, 1200), cost_ax.c2p(0, 1200), color=GUIDE, stroke_width=GUIDE_WIDTH)
        level_cost_across.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(quantity.get_value(), total(quantity.get_value())), cost_ax.c2p(0, total(quantity.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        level_cost = DecimalNumber(FIXED, num_decimal_places=0, color=GUIDE).scale(READOUT_SCALE)
        level_cost.add_updater(lambda m: m.set_value(round(total(quantity.get_value()), 4))
                               .next_to(cost_ax.c2p(0, total(quantity.get_value())), LEFT, buff=0.2))
        tc_curve = polyline([cost_ax.c2p(0, FIXED), cost_ax.c2p(0.01, total(0.01))], TC_COLOR, CURVE_WIDTH)
        tc_curve.add_updater(lambda m: m.set_points_as_corners(
            [cost_ax.c2p(q, total(q)) for q in np.linspace(0, max(reach.get_value(), 0.01), 121)]))
        tc_word = Tex('TC', color=INK).scale(CURVE_WORD_SCALE)
        tc_word.add_updater(lambda m: m.next_to(cost_ax.c2p(max(reach.get_value(), 0.01), total(max(reach.get_value(), 0.01))),
                                                RIGHT, buff=0.15))
        level_marks = [level_axis_dot, level_made, level_across, level_point, level_down, level_workers,
                       level_units, level_up, level_cost_point, level_cost_across, level_cost]
        for m in level_marks:
            m.update()
        self.remove(note)
        note = teaching('With zero output we still have some costs, like maintenance and rent.')
        self.play(FadeIn(level_axis_dot), FadeIn(level_made), FadeIn(note))
        self.play(FadeIn(level_workers))
        self.play(TransformFromCopy(level_made, level_units))
        self.play(FadeIn(level_cost_point), FadeIn(level_cost))
        self.pause('2.k')

        # ---- 2.l · A brace left of the cost graph's axis, from zero up to $1,000: Fixed Costs.
        fixed_brace = Brace(Line(cost_ax.c2p(0, 0), cost_ax.c2p(0, FIXED)), LEFT, buff=1.05, color=CAPTION)
        fixed_word = Tex('Fixed Costs', color=INK).scale(0.6).next_to(fixed_brace, LEFT, buff=0.12)
        self.remove(note)
        note = teaching('Even with zero inputs and zero outputs, we still have fixed costs.')
        self.play(FadeIn(fixed_brace), FadeIn(fixed_word), FadeIn(note))
        self.pause('2.l')

        # ---- 2.m · Low output, 20 units: point to it, map it to the 4 workers it needs, then to its cost, $1,200.
        # TC grows from $1,000 to the new cost point.
        self.play(*[FadeOut(m) for m in (level_axis_dot, level_made, level_workers, level_units, level_cost_point, level_cost)],
                  run_time=0.4)
        quantity.set_value(20)
        for m in level_marks:
            m.update()
        self.add(tc_curve)
        self.remove(note)
        note = teaching('With low outputs we have higher costs.')
        self.play(FadeIn(level_axis_dot), FadeIn(level_made), FadeIn(note))
        self.play(Create(level_across), run_time=0.6)
        self.play(FadeIn(level_point), Create(level_down), FadeIn(level_workers), run_time=0.8)
        self.play(TransformFromCopy(level_made, level_units), Create(level_up), run_time=1.0)
        self.play(FadeIn(level_cost_point), reach.animate.set_value(20), run_time=0.8)
        tc_word.update()
        self.play(Create(level_cost_across), FadeIn(level_cost), FadeIn(tc_word), run_time=0.8)
        self.pause('2.m')

        # ---- 2.n · Medium output, 50 units: 25 workers, $2,250.
        for m in level_marks:
            m.update()
        self.play(*[FadeOut(m) for m in level_marks], run_time=0.4)
        quantity.set_value(50)
        for m in level_marks:
            m.update()
        self.remove(note)
        note = teaching('With medium outputs, our costs increase again.')
        self.play(FadeIn(level_axis_dot), FadeIn(level_made), FadeIn(note))
        self.play(Create(level_across), run_time=0.6)
        self.play(FadeIn(level_point), Create(level_down), FadeIn(level_workers), run_time=0.8)
        self.play(TransformFromCopy(level_made, level_units), Create(level_up), run_time=1.0)
        self.play(FadeIn(level_cost_point), reach.animate.set_value(50), run_time=0.8)
        self.play(Create(level_cost_across), FadeIn(level_cost), run_time=0.8)
        self.pause('2.n')

        # ---- 2.o · High output, 80 units: 64 workers, $4,200.
        for m in level_marks:
            m.update()
        self.play(*[FadeOut(m) for m in level_marks], run_time=0.4)
        quantity.set_value(80)
        for m in level_marks:
            m.update()
        self.remove(note)
        note = teaching('With high outputs, our costs are higher again.')
        self.play(FadeIn(level_axis_dot), FadeIn(level_made), FadeIn(note))
        self.play(Create(level_across), run_time=0.6)
        self.play(FadeIn(level_point), Create(level_down), FadeIn(level_workers), run_time=0.8)
        self.play(TransformFromCopy(level_made, level_units), Create(level_up), run_time=1.0)
        self.play(FadeIn(level_cost_point), reach.animate.set_value(80), run_time=0.8)
        self.play(Create(level_cost_across), FadeIn(level_cost), run_time=0.8)
        self.pause('2.o')

        # ---- 2.p.linear · F straightens into a line: the same 80 units now need 80 workers and cost $5,000,
        # and the traced TC straightens with it.
        self.remove(note)
        note = teaching('Different production functions tell very different stories about costs.')
        self.play(FadeIn(note), shape.animate.set_value(1), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.p.linear')

        # ---- 2.p · And back to diminishing marginal return: 64 workers, $4,200.
        self.play(shape.animate.set_value(0.5), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.p')

        # ---- 2.q · Move the output around, down to 30 units and up to 90: the workers and total cost follow, and TC
        # is traced out as far as the point goes. (At 100 the readouts would sit on the axis words.)
        reach.add_updater(lambda m: m.set_value(max(m.get_value(), quantity.get_value())))
        self.add(reach)
        self.remove(note)
        note = teaching('With diminishing marginal return, the total cost curve becomes steeper.')
        self.play(FadeIn(note), quantity.animate.set_value(30), run_time=ROLL_TIME, rate_func=smooth)
        self.play(quantity.animate.set_value(90), run_time=SWEEP_TIME, rate_func=smooth)
        self.pause('2.q')

        # ---- 3.a · The pan: the marks clear while TC finishes its last stretch to 100 units, then the production
        # function slides off to the left and the cost graph takes its place, leaving room on the right.
        for m in [*level_marks, f_curve]:
            m.update()
            m.clear_updaters()
        reach.clear_updaters()
        self.play(*[FadeOut(m) for m in level_marks], FadeOut(fixed_brace), FadeOut(fixed_word),
                  reach.animate.set_value(100), run_time=0.8)
        for m in (tc_curve, tc_word):
            m.update()
            m.clear_updaters()
        self.remove(reach)
        self.remove(head, stored_equation, stored_wage, note)
        head = title('Cost Curves')
        production = VGroup(f_ax, f_words, f_curve, f_word)
        costs = VGroup(cost_ax, cost_words, tc_curve, tc_word)
        self.play(FadeIn(head), production.animate.shift(LEFT * PAN), costs.animate.shift(LEFT * PAN),
                  run_time=2, rate_func=smooth)
        self.remove(production)
        self.pause('3.a')

        # ---- 3.b · The FC line across the cost graph at $1,000.
        fc_line = Line(cost_ax.c2p(0, FIXED), cost_ax.c2p(100, FIXED), color=FC_COLOR, stroke_width=CURVE_WIDTH)
        fc_word = Tex('FC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(100, FIXED), RIGHT, buff=0.15)
        note = teaching("Fixed costs, like rent, don't vary with inputs.")
        self.play(FadeIn(fc_line), FadeIn(fc_word), FadeIn(note))
        self.pause('3.b')

        # ---- 3.c · A vertical bar from the axis to TC: grey up to FC, pink above it (VC). One tracker moves it.
        bar_q = ValueTracker(70)
        bar_fixed = Line(cost_ax.c2p(70, 0), cost_ax.c2p(70, FIXED), color=FC_COLOR, stroke_width=BAR_STROKE)
        bar_fixed.add_updater(lambda m: m.put_start_and_end_on(cost_ax.c2p(bar_q.get_value(), 0),
                                                               cost_ax.c2p(bar_q.get_value(), FIXED)))
        bar_variable = Line(cost_ax.c2p(70, FIXED), cost_ax.c2p(70, total(70)), color=VC_COLOR, stroke_width=BAR_STROKE)
        bar_variable.add_updater(lambda m: m.put_start_and_end_on(cost_ax.c2p(bar_q.get_value(), FIXED),
                                                                  cost_ax.c2p(bar_q.get_value(), total(bar_q.get_value()))))
        bar_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE)
        bar_word.add_updater(lambda m: m.next_to(bar_variable, RIGHT, buff=0.12))
        bar_marks = [bar_fixed, bar_variable, bar_word]
        for m in bar_marks:
            m.update()
        self.remove(note)
        note = teaching('Variable costs are the costs that do change with inputs.')
        self.play(FadeIn(bar_fixed), FadeIn(bar_variable), FadeIn(bar_word), FadeIn(note))
        self.play(bar_q.animate.set_value(95), run_time=ROLL_TIME, rate_func=smooth)
        self.play(bar_q.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.c')

        # ---- 3.d · The VC curve from the origin, and the accounting right of a grey divider: FC + VC = TC.
        for m in bar_marks:
            m.update()
            m.clear_updaters()
        vc_curve = polyline([cost_ax.c2p(q, variable(q)) for q in np.linspace(0, 100, 121)], VC_COLOR, CURVE_WIDTH)
        vc_word = Tex('VC', color=INK).scale(CURVE_WORD_SCALE).next_to(cost_ax.c2p(100, variable(100)), RIGHT, buff=0.15)
        divider = Line([DIVIDER_X, -3.0, 0], [DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        sum_row = MathTex(r'{{\mathrm{FC}}} + {{\mathrm{VC}}} = {{\mathrm{TC}}}')
        divided_row = MathTex(r'{{\frac{\mathrm{FC}}{Q}}} + {{\frac{\mathrm{VC}}{Q}}} = {{\frac{\mathrm{TC}}{Q}}}')
        average_row = MathTex(r'{{\mathrm{AFC}}} + {{\mathrm{AVC}}} = {{\mathrm{ATC}}}')
        for row, parts in [(sum_row, (r'\mathrm{FC}', r'\mathrm{VC}', r'\mathrm{TC}')),
                           (divided_row, (r'\frac{\mathrm{FC}}{Q}', r'\frac{\mathrm{VC}}{Q}', r'\frac{\mathrm{TC}}{Q}')),
                           (average_row, (r'\mathrm{AFC}', r'\mathrm{AVC}', r'\mathrm{ATC}'))]:
            for part, color in zip(parts, (FC_WORD, VC_COLOR, TC_COLOR)):
                row.get_part_by_tex(part).set_color(color)
        accounting = VGroup(sum_row, divided_row, average_row).scale(ROW_SCALE).arrange(DOWN, buff=ROW_GAP)
        accounting.move_to([(DIVIDER_X + 7.4) / 2, BODY_MID, 0])
        self.remove(note)
        note = teaching('Total cost is the sum of fixed and variable costs.')
        self.play(FadeOut(bar_word), FadeIn(vc_curve), FadeIn(vc_word), FadeIn(divider), FadeIn(sum_row), FadeIn(note))
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
        avg_ax = style_axes([0, 100, 10], [0, 120, 20], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        avg_ax.shift(RIGHT_ORIGIN - avg_ax.c2p(0, 0))
        avg_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(avg_ax.c2p(0, 120), LEFT, buff=0.23),
            Tex(r'\textsf{dollars per unit}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(0, 120), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(avg_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(avg_ax.c2p(100, 0), DOWN, buff=0.73))
        stored_average = subtitle(head, r'$\mathrm{AFC} + \mathrm{AVC} = \mathrm{ATC}$', book=True)
        self.remove(note)
        self.play(FadeOut(divider), FadeOut(sum_row), FadeOut(divided_row), FadeOut(bar_fixed), FadeOut(bar_variable),
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
        atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, atc(100)), RIGHT, buff=0.15)
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
        avc_curve = polyline([avg_ax.c2p(q, q / 2) for q in np.linspace(0, 10, 121)], AVC_COLOR, CURVE_WIDTH)
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, q / 2) for q in np.linspace(0, max(average_reach.get_value(), per_unit.get_value()), 121)]))
        avc_word = Tex('AVC', color=INK).scale(CURVE_WORD_SCALE).next_to(avg_ax.c2p(100, 50), RIGHT, buff=0.15)
        self.remove(note)
        note = teaching('Average variable cost: the costs from variable inputs for each unit of output.')
        self.play(*[FadeOut(m) for m in division_marks], run_time=0.5)
        divided['cost'], divided['average'] = variable, lambda Q: Q / 2
        per_unit.set_value(10)
        average_reach.set_value(10)
        for m in [*division_marks, avc_curve]:
            m.update()
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
        mc_equation.move_to(cost_ax.c2p(27, 4700))
        self.remove(note)
        note = teaching('Marginal cost: the cost of adding another unit.')
        self.play(FadeIn(mc_equation), FadeIn(note))
        self.pause('3.j')

        # ---- 3.k.first · Rise over run on TC (the old CostsB sweep, on this model): two dots 20 units apart around
        # Q = 55, a run (Delta Q) and a rise (Delta TC) in yellow, the chord through them in MC's orange, and the
        # chord's slope as a red dot on the averages graph, where MC starts to grow. For this TC the chord's slope
        # is exactly MC at the midpoint. VC steps aside while TC is measured (its labels would sit on VC).
        slope_q = ValueTracker(55)
        half = ValueTracker(10)
        mc_low, mc_high = ValueTracker(55), ValueTracker(55)
        chord_left = lambda: slope_q.get_value() - half.get_value()
        chord_right = lambda: slope_q.get_value() + half.get_value()
        measure_opacity = lambda: float(np.clip((half.get_value() - 2) / 4, 0, 1))
        # The chord runs a little past both dots and stays inside the graph; its slope is MC at the midpoint.
        chord_line = lambda q, h, e: Line(
            cost_ax.c2p(max(q - e, 0), total(q - h) + q * (max(q - e, 0) - q + h)),
            cost_ax.c2p(min(q + e, 100), total(q - h) + q * (min(q + e, 100) - q + h)),
            color=MC_COLOR, stroke_width=CURVE_WIDTH)
        chord = chord_line(55, 10, 15)
        chord.add_updater(lambda m: m.become(chord_line(slope_q.get_value(), half.get_value(), max(half.get_value() + 5, 12))))
        chord_dots = VGroup(Dot(radius=DOT_RADIUS, color=GUIDE), Dot(radius=DOT_RADIUS, color=GUIDE)).set_z_index(DOT_LAYER)
        chord_dots.add_updater(lambda m: (m[0].move_to(cost_ax.c2p(chord_left(), total(chord_left()))),
                                          m[1].move_to(cost_ax.c2p(chord_right(), total(chord_right())))))
        run = DashedLine(cost_ax.c2p(45, total(45)), cost_ax.c2p(65, total(45)), color=FOCUS, stroke_width=GUIDE_WIDTH)
        run.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(chord_left(), total(chord_left())), cost_ax.c2p(chord_right(), total(chord_left())),
            color=FOCUS, stroke_width=GUIDE_WIDTH).set_opacity(measure_opacity()).set_z_index(GUIDE_LAYER)))
        rise = DashedLine(cost_ax.c2p(65, total(45)), cost_ax.c2p(65, total(65)), color=FOCUS, stroke_width=GUIDE_WIDTH)
        rise.add_updater(lambda m: m.become(DashedLine(
            cost_ax.c2p(chord_right(), total(chord_left())), cost_ax.c2p(chord_right(), total(chord_right())),
            color=FOCUS, stroke_width=GUIDE_WIDTH).set_opacity(measure_opacity()).set_z_index(GUIDE_LAYER)))
        run_word = MathTex(r'\Delta Q', color=FOCUS).scale(0.6)
        run_word.add_updater(lambda m: m.next_to(run, DOWN, buff=0.1).set_opacity(measure_opacity()))
        rise_word = MathTex(r'\Delta \mathrm{TC}', color=FOCUS).scale(0.6)
        rise_word.add_updater(lambda m: m.next_to(rise, RIGHT, buff=0.1).set_opacity(measure_opacity()))
        slope_point = Dot(avg_ax.c2p(55, 55), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        slope_point.add_updater(lambda m: m.move_to(avg_ax.c2p(slope_q.get_value(), mc(slope_q.get_value()))))
        # MC is traced between the lowest and highest slope points so far.
        mc_trace = Line(avg_ax.c2p(54.9, 54.9), avg_ax.c2p(55, 55), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        mc_trace.add_updater(lambda m: m.put_start_and_end_on(
            avg_ax.c2p(min(mc_low.get_value(), slope_q.get_value()), min(mc_low.get_value(), slope_q.get_value())),
            avg_ax.c2p(max(mc_high.get_value(), slope_q.get_value(), min(mc_low.get_value(), slope_q.get_value()) + 0.1),
                       max(mc_high.get_value(), slope_q.get_value(), min(mc_low.get_value(), slope_q.get_value()) + 0.1))))
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE)
        mc_word.add_updater(lambda m: m.next_to(avg_ax.c2p(max(mc_high.get_value(), slope_q.get_value()),
                                                           max(mc_high.get_value(), slope_q.get_value())), RIGHT, buff=0.15))
        slope_marks = [chord, chord_dots, run, rise, run_word, rise_word, slope_point, mc_trace, mc_word]
        for m in slope_marks:
            m.update()
        self.remove(note)
        note = teaching('Divide the change in total cost by the change in quantity.')
        self.play(FadeOut(vc_curve), FadeOut(vc_word), *[FadeIn(m) for m in slope_marks], FadeIn(note))
        self.pause('3.k.first')

        # ---- 3.k · The pair slides up TC to Q = 85; MC grows behind it on the averages graph.
        self.play(slope_q.animate.set_value(85), run_time=SWEEP_TIME, rate_func=smooth)
        mc_high.set_value(85)
        self.pause('3.k')

        # ---- 3.l · The run shrinks to nothing: the chord becomes the tangent. VC returns with a parallel tangent at the
        # same quantity, and both run down the curves to Q = 30 while the MC point follows. Once the run is gone, the
        # two chord dots (0.6 units of Q apart) give way to one point of tangency.
        vc_tangent_line = lambda q: Line(
            cost_ax.c2p(max(q - 12, q / 2), variable(q) + q * (max(q - 12, q / 2) - q)),
            cost_ax.c2p(min(q + 12, 100), variable(q) + q * (min(q + 12, 100) - q)),
            color=MC_COLOR, stroke_width=CURVE_WIDTH)
        vc_tangent = vc_tangent_line(85)
        vc_tangent.add_updater(lambda m: m.become(vc_tangent_line(slope_q.get_value())))
        vc_point = Dot(cost_ax.c2p(85, variable(85)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        vc_point.add_updater(lambda m: m.move_to(cost_ax.c2p(slope_q.get_value(), variable(slope_q.get_value()))))
        tc_point = Dot(cost_ax.c2p(85, total(85)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        tc_point.add_updater(lambda m: m.move_to(cost_ax.c2p(slope_q.get_value(), total(slope_q.get_value()))))
        self.remove(note)
        note = teaching('For very small changes, marginal cost is the slope of the TC and VC curves.')
        self.play(half.animate.set_value(0.3), FadeIn(note), run_time=ROLL_TIME, rate_func=smooth)
        for m in (run, rise, run_word, rise_word, chord_dots):
            m.clear_updaters()
        self.remove(run, rise, run_word, rise_word, chord_dots)
        tc_point.update()
        self.add(tc_point)
        vc_tangent.update()
        vc_point.update()
        self.play(FadeIn(vc_curve), FadeIn(vc_word), FadeIn(vc_tangent), FadeIn(vc_point), run_time=0.8)
        self.play(slope_q.animate.set_value(30), run_time=SWEEP_TIME, rate_func=smooth)
        mc_low.set_value(30)
        self.pause('3.l')

        # ---- 3.m · The tangents and points clear; MC is drawn across the whole graph.
        for m in [chord, tc_point, slope_point, vc_tangent, vc_point]:
            m.update()
            m.clear_updaters()
        self.remove(note)
        note = teaching('If I add one more unit, how much will my cost go up?')
        self.play(FadeOut(chord), FadeOut(tc_point), FadeOut(slope_point), FadeOut(vc_tangent), FadeOut(vc_point),
                  run_time=0.5)
        self.play(mc_low.animate.set_value(0), mc_high.animate.set_value(100), FadeIn(note), run_time=1.0)
        for m in (mc_trace, mc_word):
            m.update()
            m.clear_updaters()
        self.pause('3.m')

        # ---- 3.n.below · Movement: one tracker moves a point along ATC with the MC point at the same quantity.
        # Below the lowest point MC lies under ATC and ATC falls. The hold is at 30 units, where the gap is plain.
        moving_q = ValueTracker(15)
        move_up = DashedLine(avg_ax.c2p(15, 0), avg_ax.c2p(15, atc(15)), color=GUIDE, stroke_width=GUIDE_WIDTH)
        move_up.add_updater(lambda m: m.become(DashedLine(
            avg_ax.c2p(moving_q.get_value(), 0),
            avg_ax.c2p(moving_q.get_value(), max(atc(moving_q.get_value()), mc(moving_q.get_value()))),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        move_atc = Dot(avg_ax.c2p(15, atc(15)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        move_atc.add_updater(lambda m: m.move_to(avg_ax.c2p(moving_q.get_value(), atc(moving_q.get_value()))))
        move_mc = Dot(avg_ax.c2p(15, 15), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        move_mc.add_updater(lambda m: m.move_to(avg_ax.c2p(moving_q.get_value(), mc(moving_q.get_value()))))
        move_marks = [move_up, move_atc, move_mc]
        for m in move_marks:
            m.update()
        self.remove(note)
        note = teaching('When MC lies below ATC, ATC bends downward.')
        self.play(FadeOut(mc_equation), *[FadeIn(m) for m in move_marks], FadeIn(note))
        self.play(moving_q.animate.set_value(30), run_time=ROLL_TIME, rate_func=smooth)
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
        # AVC = Q/2 + (the part of the fixed cost now counted as variable)/Q; it starts where that reaches AVERAGE_TOP.
        avc_curve.add_updater(lambda m: m.set_points_as_corners(
            [avg_ax.c2p(q, q / 2 + (FIXED - fixed_part.get_value()) / q)
             for q in np.linspace(max((2 * AVERAGE_TOP - np.sqrt((2 * AVERAGE_TOP) ** 2 - 8 * (FIXED - fixed_part.get_value()))) / 2,
                                       0.01), 100, 121)]))
        avc_word.add_updater(lambda m: m.next_to(avg_ax.c2p(100, 50), RIGHT, buff=0.15)
                             .set_y(min(avg_ax.c2p(100, 50 + (FIXED - fixed_part.get_value()) / 100)[1], atc_word.get_y() - 0.32)))
        long_run = [fc_line, fc_word, vc_curve, vc_word, afc_curve, afc_word, avc_curve, avc_word]
        for m in long_run:
            m.update()
        self.remove(note)
        note = teaching('Fixed cost, and therefore average fixed cost as well, go to zero.')
        self.play(FadeIn(note), fixed_part.animate.set_value(0), run_time=SWEEP_TIME, rate_func=smooth)
        for m in long_run:
            m.update()
            m.clear_updaters()
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
        # because MR shares its pink), MR is some abstract line through $80 whose slope one tracker tilts:
        # flat, steep, and back. The red point where MC = MR and its quantity follow.
        stored_objective = subtitle(head, r'$\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}$', book=True)
        stored_rule = Tex(r'$\mathrm{MC} = \mathrm{MR}$', color=CAPTION).scale(SCALE_CAPTION)
        stored_rule.next_to(stored_objective, RIGHT, buff=0.6)
        stored_rule.shift(UP * (stored_objective.family_members_with_points()[-1].get_bottom()[1]
                                - stored_rule.family_members_with_points()[0].get_bottom()[1]))
        firm_ax = style_axes([0, 100, 10], [0, 120, 20], x_length=5.6, y_length=GRAPH_SIZE)
        firm_ax.shift(np.array([-2.8, LEFT_ORIGIN[1], 0]) - firm_ax.c2p(0, 0))
        firm_words = VGroup(
            Tex(r'\$', color=INK).scale(0.8).next_to(firm_ax.c2p(0, 120), LEFT, buff=0.23),
            Tex(r'\textsf{dollars per unit}', color=CAPTION).scale(0.55).next_to(firm_ax.c2p(0, 120), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(firm_ax.c2p(100, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(firm_ax.c2p(100, 0), DOWN, buff=0.73))
        firm_mc = Line(firm_ax.c2p(0, 0), firm_ax.c2p(100, 100), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        firm_mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(100, 100), RIGHT, buff=0.15)
        firm_atc = polyline([firm_ax.c2p(q, atc(q)) for q in np.linspace(ATC_START, 100, 121)], ATC_COLOR, CURVE_WIDTH)
        firm_atc_word = Tex('ATC', color=INK).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(100, atc(100)), RIGHT, buff=0.15)
        tilt = ValueTracker(1)             # MR = 80 - tilt * Q, so MC = MR at Q = 80 / (1 + tilt)
        mr_end = lambda: 100 if tilt.get_value() <= 0.8 else 80 / tilt.get_value()
        best_q = lambda: 80 / (1 + tilt.get_value())
        mr_line = Line(firm_ax.c2p(0, 80), firm_ax.c2p(80, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH)
        mr_line.add_updater(lambda m: m.put_start_and_end_on(
            firm_ax.c2p(0, 80), firm_ax.c2p(mr_end(), 80 - tilt.get_value() * mr_end())))
        mr_word = Tex('MR', color=INK).scale(CURVE_WORD_SCALE)
        mr_word.add_updater(lambda m: m.next_to(firm_ax.c2p(mr_end(), 80 - tilt.get_value() * mr_end()),
                                                RIGHT if mr_end() == 100 else UR, buff=0.12))
        best_point = Dot(firm_ax.c2p(40, 40), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        best_point.add_updater(lambda m: m.move_to(firm_ax.c2p(best_q(), best_q())))
        best_drop = DashedLine(firm_ax.c2p(40, 0), firm_ax.c2p(40, 40), color=GUIDE, stroke_width=GUIDE_WIDTH)
        best_drop.add_updater(lambda m: m.become(DashedLine(firm_ax.c2p(best_q(), 0), firm_ax.c2p(best_q(), best_q()),
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
        self.play(tilt.animate.set_value(3), run_time=SWEEP_TIME, rate_func=smooth)
        self.play(tilt.animate.set_value(1), run_time=ROLL_TIME, rate_func=smooth)
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
        benefit_column = Polygon([0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], stroke_width=0, fill_color=DEMAND, fill_opacity=0.16)
        benefit_column.add_updater(lambda m: m.set_points_as_corners([
            [BENEFIT_LEFT, base_y, 0], [BENEFIT_LEFT + COLUMN_W, base_y, 0],
            [BENEFIT_LEFT + COLUMN_W, price_y(mb(unit.get_value())), 0], [BENEFIT_LEFT, price_y(mb(unit.get_value())), 0],
            [BENEFIT_LEFT, base_y, 0]]))
        cost_column = Polygon([0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], stroke_width=0, fill_color=SUPPLY, fill_opacity=0.16)
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
        pc_ax = style_axes([0, 100, 10], [0, 120, 20], x_length=4.6, y_length=3.6)
        pc_ax.shift(np.array([-6.6, BODY_MID - 1.95, 0]) - pc_ax.c2p(0, 0))
        mono_ax = style_axes([0, 100, 10], [0, 120, 20], x_length=4.6, y_length=3.6)
        mono_ax.shift(np.array([1.4, BODY_MID - 1.95, 0]) - mono_ax.c2p(0, 0))
        pc_panel = VGroup(
            pc_ax,
            Tex('Perfect Competition', color=INK).scale(0.8).next_to(pc_ax.c2p(50, 120), UP, buff=0.35),
            Tex(r'\$', color=INK).scale(0.8).next_to(pc_ax.c2p(0, 120), LEFT, buff=0.23),
            Tex('Q', color=INK).scale(0.8).next_to(pc_ax.c2p(100, 0), DOWN, buff=0.23),
            Line(pc_ax.c2p(0, 0), pc_ax.c2p(100, 100), color=MC_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(pc_ax.c2p(100, 100), RIGHT, buff=0.15),
            Line(pc_ax.c2p(0, 60), pc_ax.c2p(100, 60), color=DEMAND, stroke_width=CURVE_WIDTH),
            Tex('P = MR', color=INK).scale(CURVE_WORD_SCALE).next_to(pc_ax.c2p(100, 60), RIGHT, buff=0.15),
            Dot(pc_ax.c2p(60, 60), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER))
        mono_panel = VGroup(
            mono_ax,
            Tex('Monopoly', color=INK).scale(0.8).next_to(mono_ax.c2p(50, 120), UP, buff=0.35),
            Tex(r'\$', color=INK).scale(0.8).next_to(mono_ax.c2p(0, 120), LEFT, buff=0.23),
            Tex('Q', color=INK).scale(0.8).next_to(mono_ax.c2p(100, 0), DOWN, buff=0.23),
            Line(mono_ax.c2p(0, 0), mono_ax.c2p(100, 100), color=MC_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(100, 100), RIGHT, buff=0.15),
            Line(mono_ax.c2p(0, 120), mono_ax.c2p(100, 20), color=DEMAND, stroke_width=CURVE_WIDTH),
            Tex('D', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(100, 20), RIGHT, buff=0.15),
            Line(mono_ax.c2p(0, 120), mono_ax.c2p(60, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH),
            Tex('MR', color=INK).scale(CURVE_WORD_SCALE).next_to(mono_ax.c2p(60, 0), UR, buff=0.12),
            Dot(mono_ax.c2p(40, 40), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER))
        note = teaching('Marginal revenue in monopoly and perfect competition.')
        self.play(FadeIn(head), FadeIn(pc_panel), FadeIn(mono_panel), FadeIn(note))
        self.pause('4.f')
