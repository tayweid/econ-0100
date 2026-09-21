# maniml DragDemo.py DragDots
# maniml DragDemo.py DragDemand
#
# Two scratch scenes for trying drag interaction in the live viewer. Not an
# episode. Step to the end with RIGHT, then press on a dot and drag it.
#
# How it works, with nothing new in maniml: in development mode a left press
# grabs the topmost mobject under the pointer and a drag moves it. While the
# scene rests, the viewer still runs updaters every frame, so anything whose
# updater reads the dragged dot's position follows it.
#
# Three habits make that pleasant:
#   - Every draggable dot is its own top-level mobject, added LAST. The hit
#     test is a bounding box, topmost first; a dot inside a VGroup would drag
#     the whole group, and a line added after the dots would be grabbed
#     instead of the dot under it.
#   - Followers reshape themselves in place (put_start_and_end_on,
#     set_points_as_corners, move_to) rather than always_redraw, which builds
#     a new mobject every frame.
#   - A drag is never saved. Any arrow key restores the checkpoint, so the
#     dots go home.

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

        dots = [Dot(p, radius=0.16, color=c) for p, c in zip(spots, colors)]

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
        # One FadeIn per dot, so each lands in the scene as its own
        # top-level mobject, above the lines.
        self.play(*[FadeIn(d, scale=0.5) for d in dots])
        self.wait()


class DragDemand(Scene):
    """Drag the handle; demand shifts through it and the equilibrium follows.

    Demand is P = a - Q with the intercept a read from the handle, so the
    handle always sits on its curve. Supply is fixed at P = 2 + Q."""

    def construct(self):
        Q_MAX, P_MAX = 10, 10
        A_MIN, A_MAX = 3.0, 16.0

        ax = style_axes([0, Q_MAX], [0, P_MAX], x_length=7, y_length=5)
        ax.to_edge(DOWN, buff=0.9)
        p_cap = axis_caption(ax, 'Price')

        handle = Dot(ax.c2p(3, 7), radius=0.16, color=DEMAND)

        def intercept():
            q, p = ax.p2c(handle.get_center())[:2]
            return float(np.clip(q + p, A_MIN, A_MAX))

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
        # Last, so it is topmost for the hit test.
        self.play(FadeIn(handle, scale=0.5))
        self.wait()
