# maniml E0_Animation.py EpisodeE0
# Working storyboard: E0_Storyboard_Revision.md (kept separate while the notes are edited).
# All lesson choreography stays in construct().
# The production simulation: eight workers make widgets and airplanes in 20-second rounds, two more workers
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

        # ---- The class's data. One row per round: (widget workers, airplane workers, widgets, airplanes).
        # Type each round in as it finishes and save; the viewer redraws. Leave a count as None until it is in.
        SHOW_DEBRIEF = False                    # default: recap + instructions; True restores the existing data debrief
        DATA_NOTE = 'Example numbers'           # change to the class's label, e.g. 'Our class, Nov. 2'
        ROUND_SECONDS = 20
        ROUNDS = [
            (8, 0, 22, 0),
            (6, 2, 19, 5),
            (4, 4, 15, 9),
            (2, 6, 9, 12),
            (0, 8, 0, 14),
        ]

        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        AXIS_NAME_SCALE, AXIS_CAPTION_SCALE, TICK_SCALE = 0.8, 0.55, 0.55
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS = 3, 2, 0.07
        GUIDE_LAYER, DOT_LAYER = 5, 10
        SIMULATION_BODY_SCALE = 0.75
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

        # ---- 0.checkpoint.a · Two example skills, read across like the course's skillsheet report.
        # Access only: outlined blue squares are unlocked, never passed.
        REPORT_BLUE, REPORT_AMBER = TITLE, '#D99A00'
        cp_head = title('Checkpoint D')
        cp_subtitle = subtitle(cp_head, r'Strategic Interaction $|$ Example report')
        cp_legend = VGroup(RoundedRectangle(width=14, height=1.18, corner_radius=0.07,
                                            stroke_width=0, fill_color='#2A2A2A',
                                            fill_opacity=1).move_to([0, 1.91, 0]))
        cp_legend.add(
            Tex(r'\textsf{PRACTICE}', color=INK).scale(0.42).move_to([-6.75, 2.25, 0], aligned_edge=LEFT),
            Tex(r'\textsf{E Exercise $\cdot$ V Vignette $\cdot$ H Homework}', color=CAPTION).scale(0.43)
                .move_to([-6.75, 1.93, 0], aligned_edge=LEFT),
            Tex(r'\textsf{SKILLS}', color=INK).scale(0.42).move_to([1.1, 2.25, 0], aligned_edge=LEFT))
        for x, word, color, filled in ((-6.65, 'Done', REPORT_BLUE, True),
                                       (-5.1, 'Not done', CAPTION, False),
                                       (-2.95, 'Closed until checkpoint', REPORT_AMBER, False)):
            mark = Circle(radius=0.09, stroke_color=color, stroke_width=2,
                          fill_color=color if filled or color == REPORT_AMBER else BG,
                          fill_opacity=1 if filled else 0.16 if color == REPORT_AMBER else 1).move_to([x, 1.57, 0])
            cp_legend.add(mark, Tex(r'\textsf{' + word + '}', color=CAPTION).scale(0.40).next_to(mark, RIGHT, buff=0.12))
        for x, word, unlocked in ((1.25, 'Unlocked', True), (4.2, 'Locked', False)):
            mark = RoundedRectangle(width=0.25, height=0.25, corner_radius=0.045,
                                    stroke_color=REPORT_BLUE if unlocked else CAPTION, stroke_width=2,
                                    fill_color=REPORT_BLUE if unlocked else BG,
                                    fill_opacity=0.18 if unlocked else 1).move_to([x, 1.82, 0])
            cp_legend.add(mark, Tex(r'\textsf{' + word + '}', color=CAPTION).scale(0.50).next_to(mark, RIGHT, buff=0.16))
            if not unlocked:
                cp_legend.add(Line([x - 0.06, 1.76, 0], [x + 0.06, 1.88, 0], color=INK, stroke_width=2),
                              Line([x - 0.06, 1.88, 0], [x + 0.06, 1.76, 0], color=INK, stroke_width=2))

        practice_x = [-2.9, -2.35, -1.8]
        cp_columns = VGroup(
            Tex(r'\textsf{SKILL}', color=CAPTION).scale(0.45).move_to([-7, 0.85, 0], aligned_edge=LEFT),
            Tex(r'\textsf{CHECKPOINT D}', color=CAPTION).scale(0.45).move_to([-0.65, 0.85, 0], aligned_edge=LEFT),
            Tex(r'\textsf{2 of 3}', color=CAPTION).scale(0.40).move_to([-0.65, 0.53, 0], aligned_edge=LEFT),
            Tex(r'\textsf{MAKEUPS}', color=CAPTION).scale(0.45).move_to([2.72, 0.85, 0]),
            Tex(r'\textsf{REATTEMPT}', color=CAPTION).scale(0.45).move_to([4.35, 0.85, 0], aligned_edge=LEFT),
            Tex(r'\textsf{3 of 3}', color=CAPTION).scale(0.40).move_to([4.35, 0.53, 0], aligned_edge=LEFT))
        for x, letter in zip(practice_x, ('E', 'V', 'H')):
            cp_columns.add(Tex(r'\textsf{' + letter + '}', color=INK).scale(0.5).move_to([x, 0.85, 0]))
        cp_top_rule = Line([-7, 0.30, 0], [7, 0.30, 0], color=CAPTION, stroke_width=1.5)
        cp_row_rule = Line([-7, -0.54, 0], [7, -0.54, 0], color=MUTED, stroke_width=1).set_opacity(0.5)
        cp_bottom_rule = Line([-7, -1.38, 0], [7, -1.38, 0], color=CAPTION, stroke_width=1.5)
        # Different blocks have different practice records; these are examples, not student data.
        cp_examples = [('D1.1', 'Best Responses', (True, True, True)),
                       ('D2.1', 'Common Resources', (True, True, False)),
                       ('D3.1', 'Public Goods', (True, False, False))]
        cp_rows, cp_dots, cp_access_squares, cp_access_crosses, cp_access_labels, cp_makeup_dots = [], [], [], [], [], []
        for row_index, (code, name, done) in enumerate(cp_examples):
            y = -0.12 - 0.84 * row_index
            row = VGroup(
                Tex(r'\textsf{' + code + '}', color=CAPTION).scale(0.48).move_to([-7, y, 0], aligned_edge=LEFT),
                Tex(name, color=INK).scale(0.65).move_to([-6.15, y, 0], aligned_edge=LEFT))
            dots = VGroup(*[Circle(radius=0.13, stroke_color=REPORT_BLUE if completed else REPORT_AMBER,
                                   stroke_width=2.5, fill_color=REPORT_BLUE if completed else REPORT_AMBER,
                                   fill_opacity=1 if completed else 0.16).move_to([x, y, 0])
                            for x, completed in zip(practice_x, done)])
            row.add(dots)
            access_squares, access_crosses, access_labels = [], [], []
            for x, threshold in ((-0.5, 2), (4.5, 3)):
                unlocked = sum(done) >= threshold
                square = RoundedRectangle(width=0.30, height=0.30, corner_radius=0.055,
                                          stroke_color=REPORT_BLUE if unlocked else CAPTION, stroke_width=2.5,
                                          fill_color=REPORT_BLUE if unlocked else BG,
                                          fill_opacity=0.18 if unlocked else 1).move_to([x, y, 0])
                cross = VGroup(Line([x - 0.07, y - 0.07, 0], [x + 0.07, y + 0.07, 0], color=INK, stroke_width=2),
                               Line([x - 0.07, y + 0.07, 0], [x + 0.07, y - 0.07, 0], color=INK, stroke_width=2))
                label = Tex(r'\textsf{' + ('Unlocked' if unlocked else 'Locked') + '}',
                            color=REPORT_BLUE if unlocked else CAPTION).scale(0.58).next_to(square, RIGHT, buff=0.18)
                row.add(square, label)
                if not unlocked:
                    row.add(cross)
                access_squares.append(square)
                access_crosses.append(cross)
                access_labels.append(label)
            makeups = {}
            for practice_index, x in ((1, 2.45), (2, 3.0)):
                if not done[practice_index]:
                    dot = Circle(radius=0.12, stroke_color=CAPTION, stroke_width=2.5,
                                 fill_color=BG, fill_opacity=1).move_to([x, y, 0])
                    letter = Tex(r'\textsf{' + ('V' if practice_index == 1 else 'H') + '}', color=CAPTION).scale(0.34)
                    letter.next_to(dot, DOWN, buff=0.09)
                    row.add(dot, letter)
                    makeups[practice_index] = dot
            if not makeups:
                row.add(Line([2.64, y, 0], [2.80, y, 0], color=CAPTION, stroke_width=1.5))
            cp_rows.append(row)
            cp_dots.append(dots)
            cp_access_squares.append(access_squares)
            cp_access_crosses.append(access_crosses)
            cp_access_labels.append(access_labels)
            cp_makeup_dots.append(makeups)
        cp_note = teaching('Two practices unlock a first attempt; three unlock a reattempt.')
        self.play(FadeIn(cp_head), FadeIn(cp_subtitle), FadeIn(cp_legend), run_time=0.7)
        self.play(FadeIn(cp_columns), FadeIn(cp_top_rule), FadeIn(cp_row_rule), FadeIn(cp_bottom_rule),
                  FadeIn(cp_rows[0]), FadeIn(cp_rows[1]), FadeIn(cp_note), run_time=0.7)
        self.pause('0.checkpoint.a')

        # ---- 0.checkpoint.b · A third skill has one practice, so both attempts are locked.
        self.play(FadeOut(cp_note), run_time=0.25)
        cp_note = teaching('One completed practice: this skill is locked on both.')
        cp_third_rule = Line([-7, -1.38, 0], [7, -1.38, 0], color=MUTED, stroke_width=1).set_opacity(0.5)
        self.play(cp_bottom_rule.animate.set_y(-2.22), FadeIn(cp_third_rule), FadeIn(cp_rows[2]), FadeIn(cp_note), run_time=0.7)
        self.pause('0.checkpoint.b')

        # ---- 0.checkpoint.c · Record V at a check-in; two practices still do not open a reattempt.
        self.play(FadeOut(cp_note), run_time=0.25)
        makeup_heading = Tex(r'\textsf{AFTER THE CHECKPOINT}', color=CAPTION).scale(0.38).move_to([-7, -2.48, 0], aligned_edge=LEFT)
        makeup_host = Tex(r'\textsf{With Taylor or a TA}', color=CAPTION).scale(0.40).move_to([0, -2.48, 0])
        missed = Circle(radius=0.12, stroke_color=REPORT_AMBER, stroke_width=2.5,
                        fill_color=REPORT_AMBER, fill_opacity=0.16).move_to([-5.5, -2.85, 0])
        recorded = Circle(radius=0.12, stroke_color=CAPTION, stroke_width=2.5,
                          fill_color=BG, fill_opacity=1).move_to([5.5, -2.85, 0])
        checkin_tick = Line([0, -2.72, 0], [0, -2.98, 0], color=CAPTION, stroke_width=2)
        makeup_path_in = Line(missed.get_right(), [0, -2.85, 0], color=MUTED, stroke_width=2)
        makeup_path_out = Line([0, -2.85, 0], recorded.get_left(), color=MUTED, stroke_width=2)
        makeup_words = VGroup(
            Tex(r'\textsf{Complete missed practice}', color=CAPTION).scale(0.48).move_to([-5.5, -3.25, 0]),
            Tex(r'\textsf{Office-hours check-in}', color=INK).scale(0.50).move_to([0, -3.25, 0]),
            Tex(r'\textsf{Practice recorded}', color=REPORT_BLUE).scale(0.48).move_to([5.5, -3.25, 0]))
        makeup_timeline = VGroup(makeup_heading, makeup_host, missed, recorded, checkin_tick,
                                makeup_path_in, makeup_path_out, makeup_words)
        cp_note = teaching('One makeup recorded. One practice still needed for the reattempt.')
        self.play(FadeIn(makeup_heading), FadeIn(missed), FadeIn(makeup_words[0]), run_time=0.6)
        self.play(Create(makeup_path_in), FadeIn(checkin_tick), FadeIn(makeup_host), FadeIn(makeup_words[1]), run_time=0.8)
        self.play(Create(makeup_path_out), FadeIn(recorded), run_time=0.8)
        self.play(recorded.animate.set_stroke(REPORT_BLUE).set_fill(REPORT_BLUE), FadeIn(makeup_words[2]),
                  cp_makeup_dots[2][1].animate.set_stroke(REPORT_BLUE).set_fill(REPORT_BLUE), FadeIn(cp_note), run_time=0.7)
        self.pause('0.checkpoint.c')

        # ---- 0.checkpoint.d · Record H, then unlock the reattempt. The original checkpoint stays historical.
        self.play(FadeOut(cp_note), run_time=0.25)
        cp_note = teaching('All three practices are complete: the reattempt is unlocked.')
        retry_unlocked = Tex(r'\textsf{Unlocked}', color=REPORT_BLUE).scale(0.58).next_to(cp_access_squares[2][1], RIGHT, buff=0.18)
        self.play(cp_makeup_dots[2][2].animate.set_stroke(REPORT_BLUE).set_fill(REPORT_BLUE), run_time=0.7)
        self.play(FadeOut(cp_access_crosses[2][1]), FadeOut(cp_access_labels[2][1]),
                  cp_access_squares[2][1].animate.set_stroke(REPORT_BLUE).set_fill(REPORT_BLUE, opacity=0.18),
                  FadeIn(retry_unlocked), FadeIn(cp_note), run_time=0.6)
        cp_access_labels[2][1] = retry_unlocked
        self.pause('0.checkpoint.d')
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)
        self.clear()

        # ---- 0.checkpoint.e · Static checkpoint hold before MICROECONOMICS.
        # Reuse the bumper's raster glyphs, adding only the letters its wordmark lacks.
        checkpoint_glyphs = {
            'H': ('10001', '10001', '10001', '11111', '10001', '10001', '10001'),
            'K': ('10001', '10010', '10100', '11000', '10100', '10010', '10001'),
            'P': ('11110', '10001', '10001', '11110', '10000', '10000', '10000'),
            'T': ('11111', '00100', '00100', '00100', '00100', '00100', '00100'),
            'D': ('11110', '10001', '10001', '10001', '10001', '10001', '11110'),
        }
        checkpoint_card = VGroup()
        checkpoint_blues = sns.color_palette('Blues', 50).as_hex()
        checkpoint_yellows = sns.light_palette(FOCUS, 50).as_hex()
        for slot, letter in enumerate('CHECKPOINT D'):
            if letter == ' ':
                continue
            glyph = VGroup(*Raster_Font(letter))
            if letter in checkpoint_glyphs:
                for row, pixels in enumerate(checkpoint_glyphs[letter]):
                    for col, pixel in enumerate(pixels):
                        if pixel == '1':
                            glyph.add(Square(side_length=1 / 6, color=BG)
                                      .move_to([(col - 2) / 6, (3 - row) / 6, 0]))
            for pixel in glyph:
                pixel.set_fill(random.choice(checkpoint_yellows if letter == 'D' else checkpoint_blues), opacity=1)
            checkpoint_card.add(glyph.move_to([slot, 0, 0]))
        checkpoint_card.set_width(13.2).move_to(ORIGIN)
        checkpoint_topic = Tex('Strategic Interaction', color=CAPTION).scale(0.9)
        checkpoint_topic.next_to(checkpoint_card, DOWN, buff=0.55)
        checkpoint_hold = VGroup(checkpoint_card, checkpoint_topic).move_to(ORIGIN)
        self.add(checkpoint_hold)
        self.pause('0.checkpoint.e')
        self.clear()

        # ---- 0.a · The shared raster bumper with the Part title and topic subtitle.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = Tex(r'{{Part E}} $|$ Sellers', color=CAPTION)
        episode.set_color_by_tex('Part E', TITLE).scale(SCALE_CARD).move_to(DOWN * 0.9)
        self.play(AddTextWordByWord(episode), squares.animate.move_to(UP * 0.9))
        flicker(self, squares)
        thesis = Tex(r'\textit{Market Power}', color=CAPTION).scale(0.8)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- Recap layout. D1's taxonomy and Part labels; one camera move opens room for D.
        TAXONOMY_WIDTH, PANEL_GAP = 7.55, 1.2
        DIM = 0.45
        HAT, STAR = CAPTION, FOCUS
        part_d_active = False
        MOVE_TIME, REVEAL_TIME = 1.6, 0.6
        self.camera.frame.save_state()
        m_ax = style_axes([0, 60, 10], [0, 14, 2], x_length=4.0, y_length=3.75)
        price_word = Tex('P').scale(0.8).next_to(m_ax.c2p(0, 14), LEFT, buff=0.20)
        m_words = VGroup(
            price_word,
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(price_word, DOWN, buff=0.12).align_to(price_word, RIGHT),
            Tex('Q').scale(0.8).next_to(m_ax.c2p(60, 0), DOWN, buff=0.20),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(m_ax.c2p(60, 0), DOWN, buff=0.65))
        demand = VGroup(Line(m_ax.c2p(0, 12), m_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH),
                        Tex('MB', color=DEMAND).scale(0.7).next_to(m_ax.c2p(60, 0), UR, buff=0.16))
        supply = VGroup(Line(m_ax.c2p(0, 2), m_ax.c2p(60, 5), color=SUPPLY, stroke_width=CURVE_WIDTH),
                        Tex('MC', color=SUPPLY).scale(0.7).next_to(m_ax.c2p(60, 5), RIGHT, buff=0.16))
        # Lay out complete panels, including labels, so each gutter has real breathing room.
        market_base = VGroup(m_ax, m_words, demand, supply)
        market_base.move_to([(TAXONOMY_WIDTH + PANEL_GAP) / 2, BODY_MID, 0])
        taxonomy_two_center = np.array([-(market_base.width + PANEL_GAP) / 2, BODY_MID, 0])
        # One source of truth: a changing external effect moves the curve, Q*, and DWL together.
        external_cost, external_benefit = ValueTracker(0), ValueTracker(0)
        market_alpha = ValueTracker(1)
        efficient_q = lambda: (10 + external_benefit.get_value() - external_cost.get_value()) / 0.25
        efficient_p = lambda: 2 + efficient_q() / 20 + external_cost.get_value()
        star_opacity = lambda: np.clip(abs(efficient_q() - 40) / 6, 0, 1) if part_d_active else 1
        social_cost = VGroup(
            Line(m_ax.c2p(0, 2), m_ax.c2p(60, 5), color=SUPPLY, stroke_width=CURVE_WIDTH),
            Tex('MSC', color=SUPPLY).scale(0.7))
        social_cost[0].add_updater(lambda m: m.put_start_and_end_on(
            m_ax.c2p(0, 2 + external_cost.get_value()), m_ax.c2p(60, 5 + external_cost.get_value())))
        social_cost[1].add_updater(lambda m: m.next_to(social_cost[0].get_end(), RIGHT, buff=0.16)
            .set_opacity(external_cost.get_value() / 2 * market_alpha.get_value()))
        social_benefit = VGroup(
            Line(m_ax.c2p(0, 12), m_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH),
            Tex('MSB', color=DEMAND).scale(0.7))
        social_benefit[0].add_updater(lambda m: m.put_start_and_end_on(
            m_ax.c2p(0, 12 + external_benefit.get_value()), m_ax.c2p(60, external_benefit.get_value())))
        social_benefit[1].add_updater(lambda m: m.next_to(social_benefit[0].get_end(), RIGHT, buff=0.16)
            .set_opacity(external_benefit.get_value() / 2 * market_alpha.get_value()))
        star = VGroup(
            DashedLine(m_ax.c2p(40, 0), m_ax.c2p(40, 4), color=STAR, stroke_width=GUIDE_WIDTH),
            Dot(m_ax.c2p(40, 4), radius=DOT_RADIUS, color=STAR),
            Tex('$Q^*$', color=STAR).scale(0.7).next_to(m_ax.c2p(40, 0), DOWN, buff=0.18))
        star[0].add_updater(lambda m: m.become(DashedLine(
            m_ax.c2p(efficient_q(), 0), m_ax.c2p(efficient_q(), efficient_p()),
            color=STAR, stroke_width=GUIDE_WIDTH, dash_length=0.10).set_opacity(star_opacity())))
        star[1].add_updater(lambda m: m.move_to(m_ax.c2p(efficient_q(), efficient_p())).set_color(STAR).set_opacity(star_opacity()))
        star[2].add_updater(lambda m: m.next_to(m_ax.c2p(efficient_q(), 0), DOWN, buff=0.18).set_color(STAR).set_opacity(star_opacity()))
        star.set_z_index(DOT_LAYER)
        hat = VGroup(
            DashedLine(m_ax.c2p(40, 0), m_ax.c2p(40, 4), color=HAT, stroke_width=GUIDE_WIDTH, dash_length=0.10),
            Dot(m_ax.c2p(40, 4), radius=DOT_RADIUS, color=HAT),
            Tex(r'$\hat Q$', color=HAT).scale(0.7).next_to(m_ax.c2p(40, 0), DOWN, buff=0.18)).set_z_index(DOT_LAYER)
        # Both Q glyphs share a baseline; aligning their tops would lower the hatted Q.
        hat[2].add_updater(lambda m: m.align_to(star[2], DOWN).set_color(HAT)
            .set_opacity(1 if part_d_active else np.clip(abs(efficient_q() - 40) / 6, 0, 1)))
        cost_loss = always_redraw(lambda: Polygon(
            m_ax.c2p(efficient_q(), efficient_p()), m_ax.c2p(40, 4 + external_cost.get_value()), m_ax.c2p(40, 4),
            stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY).set_z_index(-1))
        benefit_loss = always_redraw(lambda: Polygon(
            m_ax.c2p(40, 4 + external_benefit.get_value()), m_ax.c2p(efficient_q(), efficient_p()), m_ax.c2p(40, 4),
            stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY).set_z_index(-1))
        cost_dwl = Tex('DWL', color=CAPTION).scale(0.65).add_updater(lambda m: m.next_to(cost_loss, UP, buff=0.12))
        benefit_dwl = Tex('DWL', color=CAPTION).scale(0.65).add_updater(lambda m: m.next_to(benefit_loss, UP, buff=0.12))

        # ---- 1.a · D1's table, red headers, and accumulating Part labels.
        head = title('The Semester So Far').fix_in_frame()
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.7)
        private_cell = taxonomy.get_entries_without_labels((1, 1))
        common_cell = taxonomy.get_entries_without_labels((2, 1))
        public_cell = taxonomy.get_entries_without_labels((2, 2))
        part_a = Tex(r'Part~A', color=FOCUS).scale(1.6).to_corner(UL).shift(DOWN * 3)
        part_b = Tex(r'Part~B', color=GREEN).scale(1.6).to_corner(UL).shift(DOWN * 4)
        part_c = Tex(r'Part~C', color=BLUE).scale(1.6).to_corner(UL).shift(DOWN * 5)
        # D1's original lettering and leading. The full opening composition is centered.
        VGroup(part_a, part_b, part_c).next_to(taxonomy, LEFT, buff=0.40).set_y(taxonomy.get_y())
        part_b.set_opacity(0)
        part_c.set_opacity(0)
        # One compact frame fits every selected two-line label, inside the cell rules.
        box = Rectangle(
            width=max(cell.width for cell in (private_cell, common_cell, public_cell)) + 0.30,
            height=max(cell.height for cell in (private_cell, common_cell, public_cell)) + 0.30,
            color=FOCUS, stroke_width=3).move_to(private_cell)
        taxonomy_panel = VGroup(taxonomy, part_a, part_b, part_c, box).move_to([0, BODY_MID, 0])
        note = teaching('Specializing and trading could bend out the PPF.').fix_in_frame()
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(note), run_time=REVEAL_TIME)
        self.play(FadeIn(box), FadeIn(part_a), run_time=REVEAL_TIME)
        self.pause('1.a')

        # ---- 1.a.1 · Open the same right-hand panel for B0's PPF first.
        self.play(taxonomy_panel.animate.scale(TAXONOMY_WIDTH / taxonomy_panel.width).move_to(taxonomy_two_center),
                  run_time=2.0, rate_func=smooth)
        cell_box_height = box.height
        market_divider_x = (taxonomy.get_right()[0] + market_base.get_left()[0]) / 2
        market_divider = Line([market_divider_x, BODY_TOP + 0.2, 0], [market_divider_x, BODY_BOTTOM - 0.2, 0],
                              color=MUTED, stroke_width=1.5)
        ppf_ax = style_axes([0, 100, 100], [0, 100, 100], x_length=4.0, y_length=3.75).move_to(m_ax)
        ppf_words = VGroup(
            Tex('A', color=INK).scale(0.8).next_to(ppf_ax.c2p(0, 100), LEFT, buff=0.3),
            Tex('B', color=INK).scale(0.8).next_to(ppf_ax.c2p(100, 0), RIGHT, buff=0.3))
        # B0's original frontier and tracker: the intercepts stay fixed as alpha goes 1 -> 1.5.
        ppf_alpha = ValueTracker(1)
        ppf_value = lambda x: max(0, 100 ** ppf_alpha.get_value() - x ** ppf_alpha.get_value()) ** (1 / ppf_alpha.get_value())
        ppf_linear = ppf_ax.plot(lambda x: 100 - x, color=MUTED, x_range=(0, 100), stroke_width=CURVE_WIDTH).set_z_index(-1)
        ppf_static = ppf_ax.plot(ppf_value, color=TRADE, x_range=(0, 100, 0.1), stroke_width=CURVE_WIDTH).set_z_index(-1)
        self.play(FadeIn(market_divider), FadeIn(ppf_ax), FadeIn(ppf_words),
                  FadeIn(ppf_linear), FadeIn(ppf_static), run_time=REVEAL_TIME)
        self.pause('1.a.1')

        # ---- 1.a.2 · Copy B0's one-second bend, grey reference line, and short gold arrow.
        ppf_frontier = always_redraw(lambda: ppf_ax.plot(ppf_value, color=TRADE, x_range=(0, 100, 0.1),
                                                        stroke_width=CURVE_WIDTH).set_z_index(-1))
        self.remove(ppf_static)
        self.add(ppf_frontier)
        ppf_arrow = Arrow(ppf_ax.c2p(45, 56), ppf_ax.c2p(57, 67), buff=0, color=FOCUS)
        self.play(FadeIn(ppf_arrow), ppf_alpha.animate.set_value(1.5), run_time=1.0, rate_func=smooth)
        ppf_frontier.clear_updaters()
        self.remove(ppf_alpha)
        self.pause('1.a.2')

        # ---- 1.a.3 · B0's first question and its two points on the bowed frontier.
        self.play(FadeOut(note), box.animate.set_color(GREEN), part_b.animate.set_opacity(1), run_time=REVEAL_TIME)
        questions = VGroup(*[Tex(word, color=INK).scale(0.7) for word in (
            '- Which point on the PPF?', '- Coordinate large groups?', '- Who benefits?')])
        questions.arrange(DOWN, buff=0.20, aligned_edge=LEFT).next_to(taxonomy, DOWN, buff=0.45).align_to(taxonomy, LEFT)
        question_glyphs = [VGroup(*q.family_members_with_points()) for q in questions]
        option_1 = Dot(ppf_ax.c2p(30, ppf_value(30)), color=INK, radius=DOT_RADIUS)
        option_2 = Dot(ppf_ax.c2p(80, ppf_value(80)), color=INK, radius=DOT_RADIUS)
        option_1_label = Tex('Option 1', color=DEFINITION).scale(0.65).next_to(option_1, RIGHT, buff=0.18)
        option_2_label = Tex('Option 2', color=DEFINITION).scale(0.65).next_to(option_2, UR, buff=0.18)
        self.play(FadeIn(option_1), FadeIn(option_1_label),
                  ShowIncreasingSubsets(question_glyphs[0], run_time=0.05 * len(question_glyphs[0]), rate_func=linear))
        self.remove(question_glyphs[0])
        self.add(questions[0])
        self.play(FadeIn(option_2), FadeIn(option_2_label), run_time=REVEAL_TIME)
        self.pause('1.a.3')

        # ---- 1.a.4 · B0's coordination question, with both panels stationary.
        self.play(ShowIncreasingSubsets(question_glyphs[1], run_time=0.05 * len(question_glyphs[1]), rate_func=linear))
        self.remove(question_glyphs[1])
        self.add(questions[1])
        self.pause('1.a.4')

        # ---- 1.a.5 · B0's distribution question completes the opening agenda.
        self.play(ShowIncreasingSubsets(question_glyphs[2], run_time=0.05 * len(question_glyphs[2]), rate_func=linear))
        self.remove(question_glyphs[2])
        self.add(questions[2])
        self.pause('1.a.5')

        # ---- 1.b · Replace the PPF with the market; keep the panel and questions in place.
        self.play(FadeOut(ppf_ax), FadeOut(ppf_words), FadeOut(ppf_linear), FadeOut(ppf_frontier), FadeOut(ppf_arrow),
                  FadeOut(option_1), FadeOut(option_1_label), FadeOut(option_2), FadeOut(option_2_label), run_time=REVEAL_TIME)
        note = teaching('Markets facilitate specialization and trade.').fix_in_frame()
        self.play(FadeIn(m_ax), FadeIn(m_words), FadeIn(note), run_time=REVEAL_TIME)
        self.play(FadeIn(demand), FadeIn(supply), run_time=REVEAL_TIME)
        self.play(FadeIn(star), run_time=REVEAL_TIME)
        self.pause('1.b')

        # ---- 1.c · State the benchmark before breaking it.
        equality = Tex(r'{{ $\hat Q$ }} $=$ {{ $Q^*$ }}', color=HAT)
        equality.set_color_by_tex('$Q^*$', STAR).scale(0.75).move_to([market_base.get_x(), -3.15, 0])
        self.play(FadeOut(note), FadeOut(questions), run_time=0.25)
        note = teaching('With competition and no externalities, equilibrium is efficient.').fix_in_frame()
        self.play(FadeIn(equality), FadeIn(note), run_time=REVEAL_TIME)
        self.pause('1.c')

        # ---- 1.d · Partial non-excludability: MSC, Q*, and DWL move as one.
        self.play(FadeOut(note), FadeOut(equality), run_time=0.25)
        note = teaching('Negative externalities: the market delivers too much.').fix_in_frame()
        self.play(box.animate.move_to((private_cell.get_center() + common_cell.get_center()) / 2).set_color(BLUE),
                  part_c.animate.set_opacity(1), FadeIn(note), run_time=REVEAL_TIME)
        self.add(hat, social_cost, cost_loss)
        self.play(external_cost.animate.set_value(2), run_time=MOVE_TIME, rate_func=smooth)
        self.play(FadeIn(cost_dwl), run_time=REVEAL_TIME)
        self.pause('1.d')

        # ---- 1.e · Pass through the undistorted market; then introduce MSB.
        self.play(FadeOut(note), FadeOut(cost_dwl), run_time=0.25)
        self.play(external_cost.animate.set_value(0), run_time=MOVE_TIME, rate_func=smooth)
        self.remove(social_cost, cost_loss)
        note = teaching('Positive externalities: the market delivers too little.').fix_in_frame()
        self.add(social_benefit, benefit_loss)
        self.play(FadeIn(note), external_benefit.animate.set_value(2), run_time=MOVE_TIME, rate_func=smooth)
        self.play(FadeIn(benefit_dwl), run_time=REVEAL_TIME)
        self.pause('1.e')

        # ---- 1.f · Reset first, then recompose the whole stage as game | taxonomy | market.
        self.play(FadeOut(note), FadeOut(benefit_dwl), run_time=0.25)
        self.play(external_benefit.animate.set_value(0), run_time=MOVE_TIME, rate_func=smooth)
        self.remove(social_benefit, benefit_loss)
        # In D, the shared outcome colors identify market equilibrium / NE and efficiency.
        HAT, STAR = NASH, EFFICIENT
        part_d_active = True
        # The game uses D1's payoffs. Quantities are outcomes of choices, not payoff numbers.
        CELL = 1.65
        payoffs = [[VGroup(Tex(a, color=ROW_PLAYER), Tex(r'$|$', color=MUTED), Tex(b, color=COL_PLAYER))
                    .arrange(RIGHT, buff=0.18).scale(0.85)
                    for a, b in row] for row in [[('3', '3'), ('0', '5')], [('5', '0'), ('1', '1')]]]
        entries = [cell for row in payoffs for cell in row]
        game = Table(payoffs, h_buff=CELL - max(cell.width for cell in entries),
                     v_buff=CELL - max(cell.height for cell in entries), include_outer_lines=True,
                     line_config={'color': MUTED, 'stroke_width': 2})
        rows = VGroup(*[Tex(word, color=CAPTION).scale(0.75).next_to([game.get_left()[0], payoffs[i][0].get_y(), 0], LEFT, buff=0.25)
                        for i, word in enumerate([r'Fish\\less', r'Fish\\more'])])
        columns = VGroup(*[Tex(word, color=CAPTION).scale(0.75).next_to([payoffs[0][i].get_x(), game.get_top()[1], 0], UP, buff=0.25)
                           for i, word in enumerate([r'Fish\\less', r'Fish\\more'])])
        # Reserve the longer public-goods labels now, so swapping games never changes the layout.
        public_rows = VGroup(*[Tex(word, color=CAPTION).scale(0.65)
            .next_to([game.get_left()[0], payoffs[i][0].get_y(), 0], LEFT, buff=0.25)
            for i, word in enumerate(['Contribute', 'Free ride'])])
        public_columns = VGroup(*[Tex(word, color=CAPTION).scale(0.65)
            .next_to([payoffs[0][i].get_x(), game.get_top()[1], 0], UP, buff=0.25)
            for i, word in enumerate(['Contribute', 'Free ride'])])
        game_extent = VGroup(game, rows, columns, public_rows, public_columns)
        game_width, taxonomy_width, market_width = game_extent.width, taxonomy.width, market_base.width
        game_center = np.array([-(taxonomy_width + market_width + 2 * PANEL_GAP) / 2, BODY_MID, 0])
        taxonomy_three_center = np.array([(game_width - market_width) / 2, BODY_MID, 0])
        market_three_center = np.array([(game_width + taxonomy_width + 2 * PANEL_GAP) / 2, BODY_MID, 0])
        game_extent.move_to(game_center)
        taxonomy_shift = taxonomy_three_center - taxonomy.get_center()
        market_shift = market_three_center - market_base.get_center()
        divider_three_x = taxonomy_three_center[0] + taxonomy_width / 2 + PANEL_GAP / 2
        game_divider = market_divider.copy().set_x(taxonomy_three_center[0] - taxonomy_width / 2 - PANEL_GAP / 2)
        self.play(FadeOut(part_a), FadeOut(part_b), FadeOut(part_c), run_time=REVEAL_TIME)
        self.remove(taxonomy_panel)
        self.add(taxonomy, box)
        self.play(self.camera.frame.animate.scale(1.25),
                  taxonomy.animate.move_to(taxonomy_three_center),
                  box.animate.stretch_to_fit_height(cell_box_height)
                      .move_to(common_cell.get_center() + taxonomy_shift).set_color(RED),
                  market_base.animate.move_to(market_three_center).set_opacity(DIM),
                  hat.animate.shift(market_shift).set_color(HAT), star.animate.set_color(STAR),
                  market_divider.animate.set_x(divider_three_x), market_alpha.animate.set_value(DIM),
                  run_time=2.0, rate_func=smooth)
        part_d = Tex(r'{{Part D}} $|$ Strategic Interaction', color=CAPTION)
        part_d.set_color_by_tex('Part D', RED).set_width(taxonomy.width - 0.2).next_to(taxonomy, UP, buff=0.45)
        game_star = SurroundingRectangle(payoffs[0][0], buff=0.16, color=STAR, stroke_width=3)
        game_hat = game_star.copy().set_color(HAT).move_to(payoffs[1][1])
        game_marks = VGroup(game_hat, game_star)
        key = VGroup(
            VGroup(Tex(r'$\hat Q$', color=HAT), Tex(r'\textsf{Equilibrium}', color=CAPTION)).arrange(RIGHT, buff=0.22),
            VGroup(Tex('$Q^*$', color=STAR), Tex(r'\textsf{Efficient}', color=CAPTION)).arrange(RIGHT, buff=0.22),
        ).arrange(RIGHT, buff=0.6).scale(0.7).move_to([taxonomy.get_x(), -3.1, 0])
        note = teaching('Common resources: individual incentives lead to over-extraction.').fix_in_frame()
        self.play(FadeIn(part_d), FadeIn(game_divider), FadeIn(game),
                  FadeIn(columns), FadeIn(rows), FadeIn(note), run_time=REVEAL_TIME)
        self.play(FadeIn(game_marks), FadeIn(key), run_time=REVEAL_TIME)
        self.pause('1.f')

        # ---- 1.f.1 · After the game holds, connect over-extraction to the market model.
        self.play(FadeOut(note), run_time=0.25)
        note = teaching('Common resources: over-extraction, like negative externalities.').fix_in_frame()
        social_cost.set_opacity(DIM)
        self.add(social_cost, cost_loss)
        self.play(FadeIn(note), external_cost.animate.set_value(2), run_time=MOVE_TIME, rate_func=smooth)
        self.pause('1.f.1')

        # ---- 1.g · Remove the commons externality BEFORE changing the game.
        self.play(external_cost.animate.set_value(0), run_time=MOVE_TIME, rate_func=smooth)
        self.remove(social_cost, cost_loss)
        self.play(FadeOut(note), FadeOut(rows), FadeOut(columns), run_time=0.3)
        rows, columns = public_rows, public_columns
        note = teaching('Public goods: individual incentives lead to under-provision.').fix_in_frame()
        self.play(box.animate.move_to(public_cell), FadeIn(rows), FadeIn(columns), FadeIn(note),
                  run_time=MOVE_TIME, rate_func=smooth)
        self.pause('1.g')

        # ---- 1.g.1 · A separate advance connects under-provision to positive externalities.
        self.play(FadeOut(note), run_time=0.25)
        note = teaching('Public goods: under-provision, like positive externalities.').fix_in_frame()
        social_benefit.set_opacity(DIM)
        self.add(social_benefit, benefit_loss)
        self.play(FadeIn(note), external_benefit.animate.set_value(2), run_time=MOVE_TIME, rate_func=smooth)
        self.pause('1.g.1')

        # ---- 1.h · Center the whole market-and-label composition. Sellers first.
        self.play(external_benefit.animate.set_value(0), run_time=MOVE_TIME, rate_func=smooth)
        self.remove(social_benefit, benefit_loss, hat)
        self.play(FadeOut(note), FadeOut(part_d), FadeOut(game_divider), FadeOut(game), FadeOut(rows), FadeOut(columns),
                  FadeOut(game_marks), FadeOut(key), FadeOut(taxonomy), FadeOut(box), FadeOut(market_divider),
                  run_time=REVEAL_TIME)
        part_d_active = False
        HAT, STAR = CAPTION, FOCUS
        self.play(FadeOut(head), run_time=0.25)
        head = title('What Comes Next').fix_in_frame()
        note = teaching('How do sellers choose? Start with what they can make.').fix_in_frame()
        sellers = Tex(r'{{Part E}} $|$ {{Sellers}}', color=CAPTION).scale(0.85).next_to(market_base, RIGHT, buff=1.5).set_y(supply[1].get_y())
        sellers.set_color_by_tex('Part E', TITLE)
        sellers.set_color_by_tex('Sellers', SUPPLY)
        buyers = Tex(r'{{Part F}} $|$ {{Buyers}}', color=CAPTION).scale(0.85).align_to(sellers, LEFT).set_y(demand[1].get_y())
        buyers.set_color_by_tex('Part F', TITLE)
        buyers.set_color_by_tex('Buyers', DEMAND)
        # Reserve both labels before moving: adding Buyers must not recenter the graph again.
        next_composition = VGroup(market_base, sellers, buyers)
        next_shift = np.array([0, BODY_MID, 0]) - next_composition.get_center()
        sellers.shift(next_shift)
        buyers.shift(next_shift)
        self.play(Restore(self.camera.frame), market_base.animate.shift(next_shift).set_opacity(1),
                  star.animate.set_color(STAR), FadeIn(head), FadeIn(note), run_time=2.0, rate_func=smooth)
        seller_link = DashedLine(supply[1].get_right() + RIGHT * 0.3,
                                [sellers.get_left()[0] - 0.3, supply[1].get_y(), 0],
                                color=CAPTION, stroke_width=1.5, dash_length=0.10).set_opacity(0.65)
        buyer_link = DashedLine(demand[1].get_right() + RIGHT * 0.3,
                               [buyers.get_left()[0] - 0.3, demand[1].get_y(), 0],
                               color=CAPTION, stroke_width=1.5, dash_length=0.10).set_opacity(0.65)
        self.play(FadeIn(sellers), FadeIn(seller_link), run_time=REVEAL_TIME)
        self.pause('1.h')

        # ---- 1.i · A distinct hold before the buyers annotation joins.
        self.play(FadeOut(note), FadeIn(buyers), FadeIn(buyer_link), run_time=REVEAL_TIME)
        self.pause('1.i')

        # ---- 2.a · The two goods, each named in its own color.
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.clear()
        head = title('Simulation E')
        simulation_subtitle = subtitle(head, 'Production of Widgets and Airplanes')
        goods = VGroup(
            Tex(r'A {{Widget}} is made by stapling a piece of paper in half.'),
            Tex(r'An {{Airplane}} is a piece of paper that can be flown at least five feet.')
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).scale(SIMULATION_BODY_SCALE)
        goods[0].get_part_by_tex('Widget').set_color(WIDGET)
        goods[1].get_part_by_tex('Airplane').set_color(AIRPLANE)
        goods.move_to([0, 1.25, 0])
        self.play(FadeIn(head), FadeIn(simulation_subtitle), FadeIn(goods[0]))
        self.play(FadeIn(goods[1]))
        self.pause('2.a')

        # ---- 2.b · The rounds, one row per fade.
        rules = VGroup(
            Tex(r'1.\enspace A practice round: everyone learns to make both.'),
            Tex(rf'2.\enspace Round 1: all {NUMBER_WORDS[LABOR]} workers make widgets for {ROUND_SECONDS} seconds.'),
            Tex(rf'3.\enspace Each round after, {MOVE_WORDS} to airplanes.')
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).scale(SIMULATION_BODY_SCALE)
        rules.move_to([0, BODY_MID, 0])
        rules.next_to(goods, DOWN, buff=0.65).align_to(goods, LEFT)
        divider_y = (goods.get_bottom()[1] + rules.get_top()[1]) / 2
        simulation_divider = Line(
            [goods.get_left()[0], divider_y, 0],
            [max(goods.get_right()[0], rules.get_right()[0]), divider_y, 0],
            color=MUTED, stroke_width=1.5)
        self.play(FadeIn(simulation_divider), run_time=0.4)
        for row in rules:
            self.play(FadeIn(row), run_time=0.6)
        self.pause('2.b')

        # Keep the optional debrief in a branch: live play steps execute outside construct().
        if SHOW_DEBRIEF:
            # ---- 2.c · The data table: worker counts filled in, output cells empty.
            # D1's Table look: rules between rows and columns only, no outer frame.
            self.play(FadeOut(goods), FadeOut(rules), FadeOut(simulation_divider), FadeOut(simulation_subtitle))
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
