# maniml E0_Four_Quadrant.py FourQuadrantPPF
# Stub, not part of any episode yet: the four-quadrant PPF from the production simulation's data.
# Moved out of E0_Animation.py on 2026-11-02 (E0 ends at the PPF). Same ROUNDS as E0; the widget production
# function (top left), labor (bottom left), the airplane production function (bottom right) and the PPF (top right).
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


class FourQuadrantPPF(Scene):
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
        # Four-quadrant PPF: one cross centered in the body band; the arms run QUADRANT_X across and QUADRANT_Y up and down.
        CENTER = np.array([0.4, BODY_MID, 0])
        QUADRANT_X, QUADRANT_Y = 3.4, 2.05
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

        # The object factories: the yellow bottom line, and muted tick numbers along an axis.
        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        tick_numbers = lambda ax, xs, ys: VGroup(
            *[Tex(str(int(x)), color=MUTED).scale(TICK_SCALE).next_to(ax.c2p(x, 0), DOWN, buff=0.15) for x in xs],
            *[Tex(str(int(y)), color=MUTED).scale(TICK_SCALE).next_to(ax.c2p(0, y), LEFT, buff=0.15) for y in ys])


        # ---- 1.a · The Four Quadrant PPF: one cross; each quadrant one graph, built in turn.
        head = title('Four Quadrant PPF')
        # Signed positions from the center: up is widgets, right is airplanes, left is widget workers,
        # down is airplane workers. Each of the four graphs reads two of these.
        up = lambda w: UP * QUADRANT_Y * w / W_TOP
        right = lambda a: RIGHT * QUADRANT_X * a / A_TOP
        left = lambda lw: LEFT * QUADRANT_X * lw / L_TOP
        down = lambda la: DOWN * QUADRANT_Y * la / L_TOP
        cross = VGroup(Line(CENTER + LEFT * QUADRANT_X, CENTER + RIGHT * QUADRANT_X, color=MUTED, stroke_width=2),
                       Line(CENTER + DOWN * QUADRANT_Y, CENTER + UP * QUADRANT_Y, color=MUTED, stroke_width=2))
        # Each axis caption sits just past the end of its arm.
        q_words = VGroup(
            Tex(r'\textsf{widgets}', color=WIDGET).scale(AXIS_CAPTION_SCALE).next_to(CENTER + UP * QUADRANT_Y, UP, buff=0.12),
            Tex(r'\textsf{airplanes}', color=AIRPLANE).scale(AXIS_CAPTION_SCALE).next_to(CENTER + RIGHT * QUADRANT_X, RIGHT, buff=0.15),
            Tex(r'\textsf{widget workers}', color=WIDGET).scale(AXIS_CAPTION_SCALE).next_to(CENTER + LEFT * QUADRANT_X, LEFT, buff=0.15),
            Tex(r'\textsf{airplane workers}', color=AIRPLANE).scale(AXIS_CAPTION_SCALE).next_to(CENTER + DOWN * QUADRANT_Y, DOWN, buff=0.12))
        tech = ValueTracker(1)
        sample = np.linspace(0, LABOR, 41)
        q_widgets = always_redraw(lambda: polyline(
            [CENTER + left(lw) + up(tech.get_value() * widgets_from(lw)) for lw in sample], CURVE, CURVE_WIDTH))
        q_airplanes = polyline([CENTER + right(airplanes_from(la)) + down(la) for la in sample], CURVE, CURVE_WIDTH)
        q_labor = Line(CENTER + left(LABOR), CENTER + down(LABOR), color=CURVE, stroke_width=CURVE_WIDTH)
        q_ppf = always_redraw(lambda: polyline(
            [CENTER + right(airplanes_from(la)) + up(tech.get_value() * widgets_from(LABOR - la)) for la in sample],
            CURVE, CURVE_WIDTH))
        # Each curve's name rides beside it: the production functions at their far ends, labor and the PPF at their middles.
        half = LABOR / 2
        q_names = VGroup(
            Tex(r'\textsf{production function}', color=CAPTION).scale(AXIS_CAPTION_SCALE)
            .next_to(CENTER + left(LABOR) + up(widgets_from(LABOR)), UP, buff=0.15),
            Tex(r'\textsf{production function}', color=CAPTION).scale(AXIS_CAPTION_SCALE)
            .next_to(CENTER + right(airplanes_from(LABOR)) + down(LABOR), RIGHT, buff=0.15),
            Tex(r'\textsf{labor}', color=CAPTION).scale(AXIS_CAPTION_SCALE).next_to(CENTER + left(half) + down(half), DL, buff=0.1),
            Tex(r'\textsf{PPF}', color=CAPTION).scale(AXIS_CAPTION_SCALE)
            .next_to(CENTER + right(airplanes_from(half)) + up(widgets_from(half)), UR, buff=0.1))
        note = teaching('Working with all four at the same time: the Four Quadrant PPF.')
        self.play(FadeIn(head), FadeIn(cross), FadeIn(q_words))
        self.play(FadeIn(q_widgets), FadeIn(q_names[0]))
        self.play(FadeIn(q_labor), FadeIn(q_names[2]))
        self.play(FadeIn(q_airplanes), FadeIn(q_names[1]))
        self.play(FadeIn(q_ppf), FadeIn(q_names[3]), FadeIn(note))
        self.pause('1.a')

        # ---- 1.b · Move workers to airplanes: one tracker drives a point in every quadrant and the dashed loop joining them.
        movers = ValueTracker(0)                # airplane workers; the rest make widgets
        corners = lambda: [CENTER + left(LABOR - movers.get_value()) + down(movers.get_value()),
                           CENTER + left(LABOR - movers.get_value()) + up(tech.get_value() * widgets_from(LABOR - movers.get_value())),
                           CENTER + right(airplanes_from(movers.get_value())) + up(tech.get_value() * widgets_from(LABOR - movers.get_value())),
                           CENTER + right(airplanes_from(movers.get_value())) + down(movers.get_value())]
        loop = always_redraw(lambda: VGroup(*[DashedLine(a, b, color=GUIDE, stroke_width=GUIDE_WIDTH, dashed_ratio=0.85)
                                              .set_opacity(0.6) for a, b in zip(corners(), corners()[1:] + corners()[:1])])
                             .set_z_index(GUIDE_LAYER))
        dots = always_redraw(lambda: VGroup(*[Dot(c, radius=DOT_RADIUS, color=GUIDE) for c in corners()]).set_z_index(DOT_LAYER))
        self.remove(note)
        note = teaching('Each worker we move to airplanes traces out the PPF.')
        self.play(FadeIn(loop), FadeIn(dots), FadeIn(note))
        self.play(movers.animate.set_value(LABOR), run_time=SWEEP_TIME, rate_func=smooth)
        self.play(movers.animate.set_value(LABOR / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('1.b')

        # ---- 1.c · Better widget technology: the widget production function stretches and the PPF with it.
        q_ghost = q_ppf.copy().clear_updaters().set_stroke(MUTED)
        self.remove(note)
        note = teaching('What happens when technology changes?')
        self.add(q_ghost)
        self.play(FadeIn(note))
        self.play(tech.animate.set_value(TECH_UP), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('1.c')
