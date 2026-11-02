# maniml E0_Animation.py EpisodeE0
# Storyboard: the comments in 01_Notes.md. All lesson choreography stays in construct().
# The production simulation: four workers make widgets and airplanes in 30-second rounds, one more worker
# moving to airplanes each round. The class's numbers go in ROUNDS at the top of construct(); the table,
# both production functions, the labor line and the PPF are all drawn from them. The four-quadrant PPF
# is a separate stub, E0_Four_Quadrant.py.
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


class EpisodeE0(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15

        # ---- The class's data. One row per 30-second round: (widget workers, airplane workers, widgets, airplanes).
        # Type each round in as it finishes and save; the viewer redraws. Leave a count as None until it is in.
        DATA_NOTE = 'Example numbers'           # change to the class's label, e.g. 'Our class, Nov. 2'
        ROUNDS = [
            (4, 0, 22, 0),
            (3, 1, 19, 5),
            (2, 2, 15, 9),
            (1, 3, 9, 12),
            (0, 4, 0, 14),
        ]

        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        AXIS_NAME_SCALE, AXIS_CAPTION_SCALE, TICK_SCALE = 0.8, 0.55, 0.55
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS = 3, 2, 0.07
        GUIDE_LAYER, DOT_LAYER = 5, 10
        LIST_SCALE = 0.9
        SWEEP_TIME, ROLL_TIME = 4.0, 2.4
        # Words as glyphs: each good's own color names it (Part F's goods tokens: good A across, good B up).
        WIDGET, AIRPLANE = GOOD_B, GOOD_A
        CURVE = INK
        # Side-by-side graphs, as E1's production function and cost graph.
        GRAPH_SIZE = 4.2
        LEFT_ORIGIN = np.array([-5.8, BODY_MID - 2.1, 0])
        RIGHT_ORIGIN = np.array([1.8, BODY_MID - 2.1, 0])
        TECH_UP = 1.4                           # the better widget technology multiplies widget output by this

        # ---- The model, read from ROUNDS. Rows still waiting for a count are left out of the graphs.
        done = [r for r in ROUNDS if r[2] is not None and r[3] is not None]
        LABOR = max(r[0] + r[1] for r in ROUNDS)
        widget_points = sorted({(0, 0)} | {(r[0], r[2]) for r in done})        # (widget workers, widgets)
        airplane_points = sorted({(0, 0)} | {(r[1], r[3]) for r in done})      # (airplane workers, airplanes)
        widgets_from = lambda workers: np.interp(workers, [p[0] for p in widget_points], [p[1] for p in widget_points])
        airplanes_from = lambda workers: np.interp(workers, [p[0] for p in airplane_points], [p[1] for p in airplane_points])
        W_MAX = max(p[1] for p in widget_points) * TECH_UP
        A_MAX = max(p[1] for p in airplane_points)
        W_STEP = 5 if W_MAX <= 40 else 10
        A_STEP = 5 if A_MAX <= 40 else 10
        W_TOP = (np.ceil(W_MAX / W_STEP) + 1) * W_STEP        # the axis runs a step past its last tick, clear of the axis name
        A_TOP = (np.ceil(A_MAX / A_STEP) + 1) * A_STEP
        L_TOP = LABOR + 1
        # The rules screen reads its counts from ROUNDS: how many workers, and how many move each round.
        NUMBER_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
        STEP = ROUNDS[1][1] - ROUNDS[0][1]
        MOVE_WORDS = 'one more worker switches' if STEP == 1 else f'{NUMBER_WORDS[STEP]} more workers switch'

        # The object factories: the yellow bottom line, and muted tick numbers along an axis.
        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        tick_numbers = lambda ax, xs, ys: VGroup(
            *[Tex(str(int(x)), color=MUTED).scale(TICK_SCALE).next_to(ax.c2p(x, 0), DOWN, buff=0.15) for x in xs],
            *[Tex(str(int(y)), color=MUTED).scale(TICK_SCALE).next_to(ax.c2p(0, y), LEFT, buff=0.15) for y in ys])

        # ---- 0.a · The shared bumper with E0's thesis, the line under the notes' heading.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 0)
        thesis = Tex(r'\textit{Introduction to how sellers make decisions and construct the supply curve}', color=CAPTION).scale(0.8)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- The recap's market: C4's model. MB = 12 - Q/5, MC = 2 + Q/20, and an external cost or benefit of 2.
        # The market trades Q-hat = 40 at $4; society wants Q* = 32 with the cost (MSC) or 48 with the benefit (MSB).
        # Q-hat is red and Q* gold, on the graph and in the payoff matrix alike.
        MARKET_ORIGIN = np.array([2.5, BODY_MID - 2.1, 0])
        TAXONOMY_CENTER = np.array([-2.6, BODY_MID + 0.1, 0])
        TAXONOMY_LIFT = UP * 1.25                # Part D: the taxonomy slides up and the game sits under it
        MATRIX_CENTER = np.array([-2.6, BODY_MID - 1.45, 0])
        DIM = 0.35                               # the market's opacity while Part D's game is on screen
        HAT, STAR = GUIDE, FOCUS
        m_ax = style_axes([0, 60, 10], [0, 14, 2], x_length=4.3, y_length=4.2)
        m_ax.shift(MARKET_ORIGIN - m_ax.c2p(0, 0))
        price_word = Tex('P').scale(AXIS_NAME_SCALE).next_to(m_ax.c2p(0, 14), LEFT, buff=0.23)
        m_words = VGroup(
            price_word,
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(AXIS_CAPTION_SCALE).next_to(price_word, DOWN, buff=0.08),
            Tex('Q').scale(AXIS_NAME_SCALE).next_to(m_ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(AXIS_CAPTION_SCALE).next_to(m_ax.c2p(60, 0), DOWN, buff=0.73))
        demand = VGroup(Line(m_ax.c2p(0, 12), m_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH),
                        Tex('MB').scale(0.7).next_to(m_ax.c2p(60, 0), UR, buff=0.12))
        supply = VGroup(Line(m_ax.c2p(0, 2), m_ax.c2p(60, 5), color=SUPPLY, stroke_width=CURVE_WIDTH),
                        Tex('MC').scale(0.7).next_to(m_ax.c2p(60, 5), RIGHT, buff=0.12))
        social_cost = VGroup(Line(m_ax.c2p(0, 4), m_ax.c2p(60, 7), color=SUPPLY, stroke_width=CURVE_WIDTH),
                             Tex('MSC').scale(0.7).next_to(m_ax.c2p(60, 7), RIGHT, buff=0.12))
        social_benefit = VGroup(Line(m_ax.c2p(0, 14), m_ax.c2p(60, 2), color=DEMAND, stroke_width=CURVE_WIDTH),
                                Tex('MSB').scale(0.7).next_to(m_ax.c2p(60, 2), RIGHT, buff=0.12))
        # A quantity's mark: its dot on the curves, the dashed drop, and its symbol under the axis.
        mark = lambda q, p, symbol, color: VGroup(
            DashedLine(m_ax.c2p(q, 0), m_ax.c2p(q, p), color=color, stroke_width=GUIDE_WIDTH, dashed_ratio=0.85),
            Dot(m_ax.c2p(q, p), radius=DOT_RADIUS, color=color),
            Tex(symbol, color=color).scale(0.6).next_to(m_ax.c2p(q, 0), DOWN, buff=0.18)).set_z_index(DOT_LAYER)
        loss = lambda *points: Polygon(*[m_ax.c2p(*p) for p in points], stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY)

        # ---- 1.a · Part A: D1's taxonomy, the box around private goods.
        head = title(r'Part A $|$ The Landscape')
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex, h_buff=0.6, v_buff=0.45,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.6).move_to(TAXONOMY_CENTER)
        private_cell = taxonomy.get_entries_without_labels((1, 1))
        box = SurroundingRectangle(private_cell, buff=0.35, color=FOCUS)
        note = teaching('Specializing and trading could bend out the PPF.')
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(note))
        self.play(FadeIn(box))
        self.pause('1.a')

        # ---- 1.b · Part B: the box turns green (D1); the market joins on the right, trading Q* where MB meets MC.
        self.remove(head, note)
        head = title(r'Part B $|$ Coordination Using Markets')
        star = mark(40, 4, '$Q^*$', STAR)
        note = teaching('Markets facilitate the exchanges needed for specialization and trade.')
        self.play(FadeIn(head), box.animate.set_color(GREEN), FadeIn(note))
        self.play(FadeIn(m_ax), FadeIn(m_words), FadeIn(demand), FadeIn(supply))
        self.play(FadeIn(star))
        self.pause('1.b')

        # ---- 1.c · Exactly what the market does.
        self.remove(note)
        note = teaching('So we actually want exactly what the market does.')
        self.play(FadeIn(note))
        self.pause('1.c')

        # ---- 1.d · Part C: the box drops half a cell (D1's partial non-excludability); MSC, the market's Q-hat, Q* at 32, DWL.
        self.remove(head, note)
        head = title(r'Part C $|$ Externalities')
        hat = mark(40, 4, r'$\hat{Q}$', HAT)
        cost_loss = loss((32, 5.6), (40, 6), (40, 4))
        note = teaching('With negative externalities we want less than what the market delivers.')
        self.play(FadeIn(head), box.animate.shift(DOWN * 0.5).set_color(BLUE), FadeIn(note))
        self.play(FadeIn(social_cost))
        self.add(hat)
        self.play(Transform(star, mark(32, 5.6, '$Q^*$', STAR)))
        self.play(FadeIn(cost_loss))
        self.pause('1.d')

        # ---- 1.e · A positive externality: MSB above MB, Q* moves to 48, DWL on the other side.
        benefit_loss = loss((40, 6), (48, 4.4), (40, 4))
        self.remove(note)
        note = teaching('With positive externalities we want more.')
        self.play(FadeOut(social_cost), FadeOut(cost_loss), FadeIn(note))
        self.play(FadeIn(social_benefit))
        self.play(Transform(star, mark(48, 4.4, '$Q^*$', STAR)))
        self.play(FadeIn(benefit_loss))
        self.pause('1.e')

        # ---- 1.f · Part D: the box (red) moves to common resources; the market fades back to the negative picture;
        # a game on the left, its Nash equilibrium marked Q-hat and the outcome society wants marked Q*.
        self.remove(head, note)
        head = title(r'Part D $|$ Strategic Interaction')
        cost_loss = loss((32, 5.6), (40, 6), (40, 4))
        market = VGroup(m_ax, m_words, demand, supply, star, hat)
        self.play(FadeIn(head), taxonomy.animate.shift(TAXONOMY_LIFT),
                  box.animate.move_to(taxonomy.get_entries_without_labels((2, 1)).get_center() + TAXONOMY_LIFT).set_color(RED),
                  FadeOut(social_benefit), FadeOut(benefit_loss), market.animate.set_opacity(DIM))
        self.play(FadeIn(social_cost.set_opacity(DIM)), FadeIn(cost_loss.set_fill(opacity=DWL_OPACITY * DIM)),
                  Transform(star, mark(32, 5.6, '$Q^*$', STAR).set_opacity(DIM)))
        # D1's Prisoner's Dilemma payoffs, row player first.
        payoffs = [[VGroup(Tex(a, color=ROW_PLAYER), Tex(r'$|$', color=MUTED), Tex(b, color=COL_PLAYER)).arrange(RIGHT, buff=0.2)
                    for a, b in row] for row in [[('3', '3'), ('0', '5')], [('5', '0'), ('1', '1')]]]
        game = Table(
            payoffs,
            row_labels=[Tex(r'\textsf{Fish less}', color=CAPTION), Tex(r'\textsf{Fish more}', color=CAPTION)],
            col_labels=[Tex(r'\textsf{Fish less}', color=CAPTION), Tex(r'\textsf{Fish more}', color=CAPTION)],
            h_buff=0.6, v_buff=0.9, line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.6).move_to(MATRIX_CENTER)
        game_hat = SurroundingRectangle(game.get_entries_without_labels((2, 2)), buff=0.12, color=HAT)
        game_star = SurroundingRectangle(game.get_entries_without_labels((1, 1)), buff=0.12, color=STAR)
        game_marks = VGroup(game_hat, game_star,
                            Tex(r'$\hat{Q}$', color=HAT).scale(0.6).next_to(game_hat, DOWN, buff=0.12),
                            Tex('$Q^*$', color=STAR).scale(0.6).next_to(game_star, UP, buff=0.12))
        note = teaching('Common resources: over-extraction, much like negative externalities.')
        self.play(FadeIn(game), FadeIn(note))
        self.play(FadeIn(game_marks))
        self.pause('1.f')

        # ---- 1.g · Public goods: the box moves across; the market shows the positive picture; the game's choices change.
        self.remove(note)
        benefit_loss = loss((40, 6), (48, 4.4), (40, 4))
        new_rows = VGroup(*[Tex(word, color=CAPTION).scale(0.6).move_to(old) for word, old in
                            zip([r'\textsf{Contribute}', r"\textsf{Don't}"], game.get_row_labels())])
        new_columns = VGroup(*[Tex(word, color=CAPTION).scale(0.6).move_to(old) for word, old in
                               zip([r'\textsf{Contribute}', r"\textsf{Don't}"], game.get_col_labels())])
        note = teaching('Public goods: under-provision, much like positive externalities.')
        self.play(box.animate.move_to(taxonomy.get_entries_without_labels((2, 2))),
                  FadeOut(game.get_row_labels()), FadeOut(game.get_col_labels()), FadeIn(new_rows), FadeIn(new_columns),
                  FadeOut(social_cost), FadeOut(cost_loss), FadeIn(note))
        self.play(FadeIn(social_benefit.set_opacity(DIM)), FadeIn(benefit_loss.set_fill(opacity=DWL_OPACITY * DIM)),
                  Transform(star, mark(48, 4.4, '$Q^*$', STAR).set_opacity(DIM)))
        self.pause('1.g')

        # ---- 1.h · Part E: the game leaves, the box returns to private goods, the plain market comes back,
        # and an arrow points at the supply curve.
        self.remove(head, note)
        head = title('What Comes Next')
        sellers = Tex(r'{{Part E}} $|$ Sellers', color=CAPTION).scale(0.8)
        sellers.set_color_by_tex('Part E', TITLE).move_to(m_ax.c2p(48, 9.5))
        to_supply = Arrow(sellers.get_bottom(), m_ax.c2p(50, 4.5), buff=0.15, color=CAPTION, stroke_width=3)
        note = teaching('Another way markets can succeed or fail: the market power of sellers.')
        self.play(FadeOut(game), FadeOut(game_marks), FadeOut(new_rows), FadeOut(new_columns),
                  FadeOut(social_benefit), FadeOut(benefit_loss), FadeOut(hat),
                  taxonomy.animate.shift(-TAXONOMY_LIFT),
                  box.animate.move_to(private_cell.get_center() - TAXONOMY_LIFT).set_color(FOCUS), FadeIn(head), FadeIn(note))
        self.play(VGroup(m_ax, m_words, demand, supply).animate.set_opacity(1), Transform(star, mark(40, 4, '$Q^*$', STAR)))
        self.play(FadeIn(sellers), GrowArrow(to_supply))
        self.pause('1.h')

        # ---- 1.i · Part F: a second arrow at the demand curve.
        buyers = Tex(r'{{Part F}} $|$ Buyers', color=CAPTION).scale(0.8)
        buyers.set_color_by_tex('Part F', TITLE).move_to(m_ax.c2p(27, 12.8))
        to_demand = Arrow(buyers.get_bottom(), m_ax.c2p(13, 9.4), buff=0.15, color=CAPTION, stroke_width=3)
        self.remove(note)
        self.play(FadeIn(buyers), GrowArrow(to_demand))
        self.pause('1.i')

        # ---- 2.a · The two goods, each named in its own color.
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.clear()
        head = title('Widgets And Airplanes')
        goods = VGroup(
            Tex(r'A {{Widget}} is made by stapling a piece of paper in half.'),
            Tex(r'An {{Airplane}} is a piece of paper that can be flown at least five feet.')
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        goods[0].get_part_by_tex('Widget').set_color(WIDGET)
        goods[1].get_part_by_tex('Airplane').set_color(AIRPLANE)
        goods.move_to([0, BODY_MID, 0])
        self.play(FadeIn(head), FadeIn(goods[0]))
        self.play(FadeIn(goods[1]))
        self.pause('2.a')

        # ---- 2.b · The rounds, one row per fade.
        rules = VGroup(
            Tex(r'1.\enspace A practice round: everyone learns to make both.'),
            Tex(rf'2.\enspace Round 1: all {NUMBER_WORDS[LABOR]} workers make widgets for 30 seconds.'),
            Tex(rf'3.\enspace Each round after, {MOVE_WORDS} to airplanes.')
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).scale(LIST_SCALE)
        rules.move_to([0, BODY_MID, 0])
        self.play(goods.animate.next_to(head, DOWN, buff=0.55).align_to(head, LEFT).scale(0.8, about_edge=LEFT))
        rules.next_to(goods, DOWN, buff=0.75).align_to(goods, LEFT)
        for row in rules:
            self.play(FadeIn(row), run_time=0.6)
        self.pause('2.b')

        # ---- 2.c · The data table: worker counts filled in, output cells empty.
        # D1's Table look: rules between rows and columns only, no outer frame.
        self.play(FadeOut(goods), FadeOut(rules))
        source = subtitle(head, DATA_NOTE)
        COLUMN_W = [1.5, 2.5, 2.5, 2.2, 2.2]
        HEADER_H, ROW_H = 1.0, 0.55
        table_w, table_h = sum(COLUMN_W), HEADER_H + ROW_H * len(ROUNDS)
        table_left, table_top = -table_w / 2, BODY_MID + table_h / 2
        column_x = [table_left + sum(COLUMN_W[:i]) + COLUMN_W[i] / 2 for i in range(len(COLUMN_W))]
        row_y = [table_top - HEADER_H - ROW_H * (i + 0.5) for i in range(len(ROUNDS))]
        table_rules = VGroup(
            Line([table_left, table_top - HEADER_H, 0], [table_left + table_w, table_top - HEADER_H, 0], color=MUTED, stroke_width=2),
            *[Line([table_left + sum(COLUMN_W[:i]), table_top, 0], [table_left + sum(COLUMN_W[:i]), table_top - table_h, 0],
                   color=MUTED, stroke_width=2) for i in range(1, len(COLUMN_W))])
        headers = VGroup(Tex('Round'), Tex(r'Widget\\workers', color=WIDGET), Tex(r'Airplane\\workers', color=AIRPLANE),
                         Tex('Widgets', color=WIDGET), Tex('Airplanes', color=AIRPLANE)).scale(0.7)
        for word, x in zip(headers, column_x):
            word.move_to([x, table_top - HEADER_H / 2, 0])
        counts = VGroup(*[VGroup(*[Tex(str(v)).scale(0.75).move_to([column_x[j], y, 0]) for j, v in
                                   enumerate([i + 1, r[0], r[1]])]) for i, (r, y) in enumerate(zip(ROUNDS, row_y))])
        note = teaching('Set up a table to store the data.')
        self.play(FadeIn(source), FadeIn(table_rules), FadeIn(headers), FadeIn(counts), FadeIn(note))
        self.pause('2.c')

        # ---- 2.d.1 onward · One hold per round: its widgets and airplanes fill in.
        self.remove(note)
        outputs = VGroup()
        for i, (r, y) in enumerate(zip(ROUNDS, row_y)):
            made = VGroup(*[Tex('' if v is None else str(v)).scale(0.75).move_to([column_x[3 + j], y, 0])
                            for j, v in enumerate([r[2], r[3]])])
            outputs.add(made)
            self.play(FadeIn(made), run_time=0.6)
            self.pause(f'2.d.{i + 1}')

        # ---- 3.a · The widget production function: one dot per round, widget workers across.
        self.play(FadeOut(table_rules), FadeOut(headers), FadeOut(counts), FadeOut(outputs))
        self.remove(head)
        head = title('Production Function')
        source.next_to(head, DOWN, buff=0.10).align_to(head, LEFT)
        w_ax = style_axes([0, L_TOP, 1], [0, W_TOP, W_STEP], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        w_ax.shift(LEFT_ORIGIN - w_ax.c2p(0, 0))
        w_words = VGroup(
            Tex('$W$').scale(AXIS_NAME_SCALE).next_to(w_ax.c2p(0, W_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{widgets}', color=WIDGET).scale(AXIS_CAPTION_SCALE).next_to(w_ax.c2p(0, W_TOP), RIGHT, buff=0.22),
            Tex('$L_W$').scale(AXIS_NAME_SCALE).next_to(w_ax.c2p(L_TOP, 0), DOWN, buff=0.23),
            Tex(r'\textsf{widget workers}', color=CAPTION).scale(AXIS_CAPTION_SCALE).next_to(w_ax.c2p(L_TOP, 0), DOWN, buff=0.73))
        w_ticks = tick_numbers(w_ax, range(1, LABOR + 1), np.arange(W_STEP, W_TOP, W_STEP))
        w_dots = VGroup(*[Dot(w_ax.c2p(*p), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER) for p in widget_points])
        note = teaching('The production function takes inputs and gives us some output quantity.')
        self.play(FadeIn(head), FadeIn(w_ax), FadeIn(w_words), FadeIn(w_ticks), FadeIn(note))
        for dot in w_dots:
            self.play(FadeIn(dot), run_time=0.4)
        self.pause('3.a')

        # ---- 3.b · Join the dots; each worker's added widgets sit above that worker's dot.
        w_curve = polyline([w_ax.c2p(*p) for p in widget_points], CURVE, CURVE_WIDTH)
        w_added = VGroup(*[Tex(f'+{b[1] - a[1]}', color=GUIDE).scale(0.55).next_to(w_dots[i + 1], UL, buff=0.08)
                           for i, (a, b) in enumerate(zip(widget_points, widget_points[1:]))])
        self.remove(note)
        note = teaching('Diminishing marginal return: more inputs lead to increasingly small increases.')
        self.play(Create(w_curve), FadeIn(note))
        for label in w_added:
            self.play(FadeIn(label), run_time=0.4)
        self.pause('3.b')

        # ---- 3.c · The airplane production function on the right, built the same way.
        a_ax = style_axes([0, L_TOP, 1], [0, A_TOP, A_STEP], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        a_ax.shift(RIGHT_ORIGIN - a_ax.c2p(0, 0))
        a_words = VGroup(
            Tex('$A$').scale(AXIS_NAME_SCALE).next_to(a_ax.c2p(0, A_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{airplanes}', color=AIRPLANE).scale(AXIS_CAPTION_SCALE).next_to(a_ax.c2p(0, A_TOP), RIGHT, buff=0.22),
            Tex('$L_A$').scale(AXIS_NAME_SCALE).next_to(a_ax.c2p(L_TOP, 0), DOWN, buff=0.23),
            Tex(r'\textsf{airplane workers}', color=CAPTION).scale(AXIS_CAPTION_SCALE).next_to(a_ax.c2p(L_TOP, 0), DOWN, buff=0.73))
        a_ticks = tick_numbers(a_ax, range(1, LABOR + 1), np.arange(A_STEP, A_TOP, A_STEP))
        a_dots = VGroup(*[Dot(a_ax.c2p(*p), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER) for p in airplane_points])
        a_curve = polyline([a_ax.c2p(*p) for p in airplane_points], CURVE, CURVE_WIDTH)
        a_added = VGroup(*[Tex(f'+{b[1] - a[1]}', color=GUIDE).scale(0.55).next_to(a_dots[i + 1], UL, buff=0.08)
                           for i, (a, b) in enumerate(zip(airplane_points, airplane_points[1:]))])
        self.remove(note)
        note = teaching('Airplanes have a production function of their own.')
        self.play(FadeIn(a_ax), FadeIn(a_words), FadeIn(a_ticks), FadeIn(note))
        for dot in a_dots:
            self.play(FadeIn(dot), run_time=0.4)
        self.play(Create(a_curve))
        self.play(FadeIn(a_added))
        self.pause('3.c')

        # ---- 3.d · Better widget technology: the widget production function stretches up; the old one stays as a ghost.
        tech = ValueTracker(1)
        w_ghost = w_curve.copy().set_stroke(MUTED)
        w_curve.add_updater(lambda m: m.set_points_as_corners([w_ax.c2p(p[0], tech.get_value() * p[1]) for p in widget_points]))
        for dot, p in zip(w_dots, widget_points):
            dot.add_updater(lambda m, p=p: m.move_to(w_ax.c2p(p[0], tech.get_value() * p[1])))
        self.remove(note)
        note = teaching('What happens when technology changes?')
        self.add(w_ghost)
        self.play(FadeOut(w_added), FadeIn(note))
        self.play(tech.animate.set_value(TECH_UP), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d')

        # ---- 4.a · Labor: widget workers up, airplane workers across; every round sits on one line.
        self.play(tech.animate.set_value(1), run_time=ROLL_TIME / 2, rate_func=smooth)
        w_curve.clear_updaters()
        for dot in w_dots:
            dot.clear_updaters()
        self.remove(*[m for m in self.mobjects if isinstance(m, ValueTracker)])
        self.play(*[FadeOut(m) for m in [w_ax, w_words, w_ticks, w_dots, w_curve, w_ghost,
                                         a_ax, a_words, a_ticks, a_dots, a_curve, a_added, note]])
        self.remove(head)
        head = title('Labor')
        l_ax = style_axes([0, L_TOP, 1], [0, L_TOP, 1], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        l_ax.shift(LEFT_ORIGIN - l_ax.c2p(0, 0))
        l_words = VGroup(
            Tex('$L_W$').scale(AXIS_NAME_SCALE).next_to(l_ax.c2p(0, L_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{widget workers}', color=WIDGET).scale(AXIS_CAPTION_SCALE).next_to(l_ax.c2p(0, L_TOP), RIGHT, buff=0.22),
            Tex('$L_A$').scale(AXIS_NAME_SCALE).next_to(l_ax.c2p(L_TOP, 0), DOWN, buff=0.23),
            Tex(r'\textsf{airplane workers}', color=AIRPLANE).scale(AXIS_CAPTION_SCALE).next_to(l_ax.c2p(L_TOP, 0), DOWN, buff=0.73))
        l_ticks = tick_numbers(l_ax, range(1, LABOR + 1), range(1, LABOR + 1))
        l_dots = VGroup(*[Dot(l_ax.c2p(r[1], r[0]), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER) for r in ROUNDS])
        l_line = Line(l_ax.c2p(0, LABOR), l_ax.c2p(LABOR, 0), color=CURVE, stroke_width=CURVE_WIDTH)
        l_equation = MathTex(r'L_W + L_A = ' + str(LABOR)).scale(0.7).next_to(l_ax.c2p(LABOR / 2, LABOR / 2), UR, buff=0.15)
        note = teaching('We are fundamentally constrained by the total labor.')
        self.play(FadeIn(head), FadeIn(l_ax), FadeIn(l_words), FadeIn(l_ticks), FadeIn(note))
        for dot in l_dots:
            self.play(FadeIn(dot), run_time=0.4)
        self.play(Create(l_line), FadeIn(l_equation))
        self.pause('4.a')

        # ---- 5.a · The PPF on the right: airplanes across, widgets up, one dot per round.
        self.remove(head)
        head = title('Production Possibilities Frontier')
        ppf_points = sorted((r[3], r[2]) for r in done)                     # (airplanes, widgets)
        P_TOP = (np.ceil(max(p[1] for p in ppf_points) / W_STEP) + 1) * W_STEP     # no technology headroom here
        p_ax = style_axes([0, A_TOP, A_STEP], [0, P_TOP, W_STEP], x_length=GRAPH_SIZE, y_length=GRAPH_SIZE)
        p_ax.shift(RIGHT_ORIGIN - p_ax.c2p(0, 0))
        p_words = VGroup(
            Tex('$W$').scale(AXIS_NAME_SCALE).next_to(p_ax.c2p(0, P_TOP), LEFT, buff=0.23),
            Tex(r'\textsf{widgets}', color=WIDGET).scale(AXIS_CAPTION_SCALE).next_to(p_ax.c2p(0, P_TOP), RIGHT, buff=0.22),
            Tex('$A$').scale(AXIS_NAME_SCALE).next_to(p_ax.c2p(A_TOP, 0), DOWN, buff=0.23),
            Tex(r'\textsf{airplanes}', color=AIRPLANE).scale(AXIS_CAPTION_SCALE).next_to(p_ax.c2p(A_TOP, 0), DOWN, buff=0.73))
        p_ticks = tick_numbers(p_ax, np.arange(A_STEP, A_TOP, A_STEP), np.arange(W_STEP, P_TOP, W_STEP))
        p_dots = VGroup(*[Dot(p_ax.c2p(*p), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER) for p in ppf_points])
        p_curve = polyline([p_ax.c2p(*p) for p in ppf_points], CURVE, CURVE_WIDTH)
        self.remove(note)
        note = teaching('And we have the PPF!')
        self.play(FadeIn(head), FadeIn(p_ax), FadeIn(p_words), FadeIn(p_ticks))
        for dot in p_dots:
            self.play(FadeIn(dot), run_time=0.4)
        self.play(Create(p_curve), FadeIn(note))
        self.pause('5.a')

        # ---- 5.b · Part A's straight-line PPF between the same two ends, dashed: ours bows out past it.
        straight = DashedLine(p_ax.c2p(*ppf_points[0]), p_ax.c2p(*ppf_points[-1]), color=MUTED, stroke_width=CURVE_WIDTH)
        self.remove(note)
        note = teaching('The PPF bows out, from another direction.')
        self.play(Create(straight), FadeIn(note))
        self.pause('5.b')
