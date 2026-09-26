# maniml DragDemo.py DragDots
# maniml DragDemo.py DragDemand
#
# Two scratch scenes for trying drag interaction in the live viewer. Not an
# episode. Step to the end with RIGHT, then press on a dot and drag it.
#
# How it works: a left press grabs the mobject under the pointer and a drag
# moves it. While the scene rests, the viewer still runs updaters every
# frame, so anything whose updater reads the dragged dot's position follows.
#
# `set_draggable()` marks a mobject as a handle: it is grabbed before
# anything else under the pointer (so it can sit inside a group or under a
# line), it works in a presentation too (which then presents from the live
# stage rather than the mp4), and the viewer names it in a chip on hover.
# In development every other mobject is still grabbable, as before.
#   along=  keeps the handle on a curve (a mobject) or a line (a direction)
#   on_drag= is called after each move — set a ValueTracker there
#
# Two habits:
#   - Followers reshape themselves in place (put_start_and_end_on,
#     set_points_as_corners, move_to, set_value) rather than always_redraw,
#     which builds a new mobject every frame.
#   - A drag is never saved. Any arrow key restores the checkpoint, so the
#     handles go home. A beat that should start from a moved handle animates
#     it there in source.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'Blocks/_Assets'))
from style import *
from style import axes as style_axes


class DragDots(Scene):
    def construct(self):
        spots = [LEFT * 4 + DOWN, LEFT * 2 + UP * 2, ORIGIN + DOWN * 2,
                 RIGHT * 2 + UP * 1.5, RIGHT * 4.5 + DOWN * 0.5]
        colors = [BLUE, GREEN, PINK, ORANGE, PURPLE]
        links = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 3), (0, 2)]

        dots = [Dot(p, radius=0.16, color=c).set_draggable()
                for p, c in zip(spots, colors)]

        def follow(i, j):
            def update(line):
                line.put_start_and_end_on(dots[i].get_center(), dots[j].get_center())
            return update

        lines = VGroup()
        for i, j in links:
            line = Line(spots[i], spots[j], color=MUTED, stroke_width=4)
            line.add_updater(follow(i, j))
            lines.add(line)

        # The centroid is one more follower: it reads every dot.
        centroid = Dot(radius=0.08, color=GUIDE)
        centroid.add_updater(
            lambda m: m.move_to(np.mean([d.get_center() for d in dots], axis=0)))

        head = title('Drag a dot')
        note = subtitle(head, 'the lines and the centroid follow')

        self.play(FadeIn(head), FadeIn(note), Create(lines), FadeIn(centroid))
        self.play(*[FadeIn(d, scale=0.5) for d in dots])
        self.pause()
        self.play(dots[2].animate.shift(RIGHT * 2 + UP), run_time=1.5)
        self.wait()


class DragDemand(Scene):
    """Drag the handle; demand shifts through it and the equilibrium follows.

    The handle is the one draggable thing. It slides vertically at Q = 3
    (along=UP), and on_drag writes the intercept a = Q + P into a
    ValueTracker; everything else reads the tracker. Demand is P = a - Q,
    supply P = 2 + Q."""

    def construct(self):
        Q_MAX, P_MAX = 10, 10
        A_MIN, A_MAX = 4.0, 13.0          # keeps the handle on the chart

        ax = style_axes([0, Q_MAX], [0, P_MAX], x_length=7, y_length=5)
        ax.to_edge(DOWN, buff=0.9)
        p_cap = axis_caption(ax, 'Price')

        a = ValueTracker(10.0)
        intercept = a.get_value

        def set_intercept(handle):
            q, p = ax.p2c(handle.get_center())[:2]
            a.set_value(float(np.clip(q + p, A_MIN, A_MAX)))
            handle.move_to(ax.c2p(3, intercept() - 3))   # clamp shows

        handle = Dot(ax.c2p(3, 7), radius=0.16, color=DEMAND)
        handle.set_draggable(along=UP, on_drag=set_intercept)

        def demand_ends(a):
            # P = a - Q clipped to the axes box
            q0, q1 = max(0.0, a - P_MAX), min(Q_MAX, a)
            return [ax.c2p(q0, a - q0), ax.c2p(q1, a - q1)]

        supply = polyline([ax.c2p(0, 2), ax.c2p(8, 10)], color=SUPPLY)
        demand = polyline(demand_ends(10), color=DEMAND)
        demand.add_updater(lambda m: m.set_points_as_corners(demand_ends(intercept())))

        def eq_point():
            q = (intercept() - 2) / 2
            return q, 2 + q

        eq_dot = Dot(ax.c2p(*eq_point()), color=GUIDE)
        h_line = Line(color=GUIDE, stroke_width=2).set_opacity(0.4)
        v_line = Line(color=GUIDE, stroke_width=2).set_opacity(0.4)

        def place_marker(_=None):
            q, p = eq_point()
            eq_dot.move_to(ax.c2p(q, p))
            h_line.put_start_and_end_on(ax.c2p(0, p), ax.c2p(q, p))
            v_line.put_start_and_end_on(ax.c2p(q, 0), ax.c2p(q, p))

        place_marker()
        eq_dot.add_updater(place_marker)

        price = DecimalNumber(eq_point()[1], num_decimal_places=2).scale(SCALE_CAPTION)
        price.set_color(GUIDE)

        def place_price(m):
            q, p = eq_point()
            m.set_value(p)
            m.next_to(ax.c2p(0, p), LEFT, buff=0.2)

        place_price(price)
        price.add_updater(place_price)

        head = title('Drag the demand handle')
        note = subtitle(head, 'the equilibrium follows')

        self.play(FadeIn(head), FadeIn(note), Create(ax), FadeIn(p_cap))
        self.play(Create(supply), Create(demand))
        self.play(FadeIn(h_line), FadeIn(v_line), FadeIn(eq_dot), FadeIn(price))
        self.play(FadeIn(handle, scale=0.5))
        self.pause()
        # A beat that starts from a shifted demand animates the tracker;
        # the handle follows it like everything else.
        handle.add_updater(lambda m: m.move_to(ax.c2p(3, intercept() - 3)))
        self.play(a.animate.set_value(12), run_time=1.5)
        self.wait()
