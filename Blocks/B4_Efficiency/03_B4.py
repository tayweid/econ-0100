# maniml 03_B4.py B4
# Complete B4 lesson. Edit this file for the continuous classroom animation.
# The numbered 03_01–03_09 files retain the separate development scenes.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects, screen_point
import discovery
from importlib import reload

simulate = reload(discovery).simulate
PLAZA_NAME_INSET = 0.65


class B4(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        # Raise the full-market plaza in frame, leaving the caption strip clear.
        PLAZA_CENTER = [4, 0, -0.4]

        # Changing endpoints must reveal dashes, not stretch an existing pattern.
        # Keep one vector object so 3D/fixed placement and checkpoint identity survive.
        def set_dashed_endpoints(m, start, end):
            start, end = np.array(start, dtype=float), np.array(end, dtype=float)
            vector = end - start
            length = np.linalg.norm(vector)
            if m.submobjects:
                m.set_submobjects([])
            if length < 1e-8:
                return m.set_points(np.array([start, start, start]))
            dash_length, gap = 0.05, 0.05
            offsets = np.arange(0, length, dash_length + gap)
            starts = start + offsets[:, None] * vector / length
            ends = start + np.minimum(offsets + dash_length, length)[:, None] * vector / length
            # A repeated endpoint separates consecutive quadratic subpaths.
            points = np.stack([starts, (starts + ends) / 2, ends, ends], axis=1).reshape(-1, 3)[:-1]
            if np.linalg.norm(ends[-1] - end) > 1e-8:
                # Preserve the exact logical endpoint even when it lies in a gap.
                points = np.vstack([points, ends[-1], end])
            return m.set_points(points)

        # Pre-Q2 rehearsal budget: 8 minutes including bumper; hard ceiling 10.
        # Demonstrate a switch once, then compress settlement. No new material here.
        # ========== 1. Exchange ==========
        self.camera.fps = 15
        MB, MC, OFFER = 6, 2, 4
        DOLLAR_HEIGHT, BAR_BASE = 0.55, 0.75
        BAR_WIDTH, CLOSE_WIDTH, CLOSE_GAP = 0.16, 1.10, 0.12
        WIDTH, GAP = CLOSE_WIDTH, CLOSE_GAP
        WORLD_CENTER = np.array([0.0, 0.0, 1.8])
        CLOSE_CENTER = np.array([0.0, 0.0, 2.05])

        # Animate.py's world-text billboard: preserve 3D placement and scale.
        # Rebuild from flat glyphs, not cumulative float32 rotations, so camera
        # moves and backward seeks keep the letters planar and readable.
        def face_camera(m):
            if isinstance(m, DecimalNumber) and abs(m.get_value() - m.tracker.get_value()) > 1e-6:
                m.set_value(m.tracker.get_value())
                m.face_mat = np.eye(3)
                if hasattr(m, 'face_base'):
                    del m.face_base
            cur = self.camera.frame.get_orientation().as_matrix()
            if np.allclose(cur, m.face_mat, atol=1e-6):
                return
            if not hasattr(m, 'face_base'):
                m.face_base = [sub.get_points().astype(float).copy() for sub in m.get_family()]
            center = m.get_center().astype(float)
            for sub, base in zip(m.get_family(), m.face_base):
                if len(base):
                    sub.set_points(base @ cur.T)
                    sub.use_triangulated_fill = True
            m.move_to(center)
            m.face_mat = cur

        # ---- 0.a · B4 bumper; the camera then enters B3's real 3D plaza.
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'B', 4)
        thesis = Tex(r'\textit{Under some conditions, nothing can do better than markets.}',
                     color=CAPTION).scale(0.9).next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.set_camera_orientation(phi=58 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(WORLD_CENTER)

        # ---- 1.a · The approved plaza-to-head-on view, with no intermediate stop.
        # ---- 2.a · The first two people; no market price has been established.
        head = fixed(title('Which prices work?'))
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        self.play(FadeIn(head), FadeIn(floor), FadeIn(rim))

        bodies, bars, names, marginal_labels = {}, {}, {}, {}
        for key, x, value, color, name, term in [
            ('buyer', -1.65, MB, DEMAND, 'Gary', 'MB'),
            ('seller', 1.65, MC, SUPPLY, 'Molly', 'MC'),
        ]:
            shadow = Disk3D(radius=0.28, resolution=(2, 24), shading=(0, 0, 0),
                            opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(16, 10))
            orb.move_to([x, 0, 0.32])
            body = Group(shadow, orb)
            bar = Rectangle3D(width=BAR_WIDTH, height=value * DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT).move_to(
                [x, 0, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            name_label = Tex(name, color=INK).scale(0.65)
            name_label.face_mat = np.eye(3)
            name_label.add_updater(face_camera)
            name_label.anchor = body
            name_label.offset = LEFT * 0.75 if key == 'buyer' else RIGHT * 0.75
            name_label.add_updater(lambda m: m.move_to(
                np.array([m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.55, 0.13])
                + m.offset))
            name_label.update()
            value_label = Tex(rf'{term} $\${value:g}$', color=color).scale(0.62)
            value_label.face_mat = np.eye(3)
            value_label.add_updater(face_camera)
            value_label.anchor = bar
            value_label.value = value
            value_label.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.08,
                 BAR_BASE + m.value * DOLLAR_HEIGHT + 0.28]))
            value_label.update()
            bodies[key], bars[key] = body, bar
            names[key], marginal_labels[key] = name_label, value_label
            self.play(FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))

        # ---- 2.a.i · Same bars, now between the people and viewed from the side.
        self.play(
            self.camera.frame.animate.reorient(0, 90, center=CLOSE_CENTER, height=7.2),
            bodies['buyer'].animate.set_x(-1.45),
            bodies['seller'].animate.set_x(1.45),
            bars['buyer'].animate.stretch_to_fit_width(CLOSE_WIDTH).set_x(
                -(CLOSE_WIDTH + CLOSE_GAP) / 2),
            bars['seller'].animate.stretch_to_fit_width(CLOSE_WIDTH).set_x(
                (CLOSE_WIDTH + CLOSE_GAP) / 2),
            floor.animate.set_opacity(0.05), rim.animate.set_stroke(opacity=0.2),
            run_time=2.2)
        left_edge = -CLOSE_WIDTH - CLOSE_GAP / 2
        right_edge = CLOSE_WIDTH + CLOSE_GAP / 2
        price_z = BAR_BASE + OFFER * DOLLAR_HEIGHT
        zero = Line([left_edge - 0.15, -0.02, BAR_BASE],
                    [right_edge + 0.15, -0.02, BAR_BASE], color=MUTED, stroke_width=1.5)
        price_line = DashedLine([left_edge, -0.045, price_z],
                               [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        price_shadow = DashedLine([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                                 color=GUIDE, stroke_width=2).set_opacity(0.3)
        price_word = Tex(rf'Price $\${OFFER:g}$', color=GUIDE).scale(0.62)
        price_word.face_mat = np.eye(3)
        price_word.add_updater(face_camera)
        price_word.update()
        price_word.move_to([0, -0.10, price_z + 0.28])
        zero_word = Tex('0', color=CAPTION).scale(0.62)
        zero_word.face_mat = np.eye(3)
        zero_word.add_updater(face_camera)
        zero_word.update()
        zero_word.move_to([0, -0.10, BAR_BASE - 0.25])
        self.play(FadeIn(zero), FadeIn(zero_word), FadeIn(price_line),
                  FadeIn(price_shadow), FadeIn(price_word))

        accepted_line = Line([left_edge, -0.045, price_z],
                             [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        price_gaps = VGroup(*[Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3)
                              for a, b in zip(price_line, price_line[1:])])
        shadow_gaps = VGroup(*[Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=2).set_opacity(0.3)
                               for a, b in zip(price_shadow, price_shadow[1:])])
        self.play(FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.4)
        self.remove(price_line, price_shadow, price_gaps, shadow_gaps)
        self.add(accepted_line, accepted_shadow)
        # ---- 2.b.i · B1's expenditure rectangle, then its label.
        expenditure = Polygon(
            [left_edge, -0.025, BAR_BASE], [-CLOSE_GAP / 2, -0.025, BAR_BASE],
            [-CLOSE_GAP / 2, -0.025, price_z], [left_edge, -0.025, price_z],
            fill_color=GOV, fill_opacity=AREA_OPACITY, stroke_width=0)
        buyer_cs = Polygon(
            [left_edge, -0.025, price_z], [-CLOSE_GAP / 2, -0.025, price_z],
            [-CLOSE_GAP / 2, -0.025, BAR_BASE + MB * DOLLAR_HEIGHT],
            [left_edge, -0.025, BAR_BASE + MB * DOLLAR_HEIGHT],
            fill_color=DEMAND, fill_opacity=AREA_OPACITY, stroke_width=0)
        expenditure_label = Tex(rf'Expenditure $\${OFFER:g}$', color=GOV).scale(0.62)
        expenditure_label.face_mat = np.eye(3)
        expenditure_label.add_updater(face_camera)
        expenditure_label.update()
        expenditure_label.move_to(
            [left_edge - 0.3, -0.10, BAR_BASE + OFFER * DOLLAR_HEIGHT / 2], aligned_edge=RIGHT)

        # ---- 2.b.ii · Consumer surplus stays above the same price line.
        cs_label = Tex(rf'CS $\${MB - OFFER:g}$', color=DEMAND).scale(0.62)
        cs_label.face_mat = np.eye(3)
        cs_label.add_updater(face_camera)
        cs_label.update()
        cs_label.move_to(
            [left_edge - 0.3, -0.10, BAR_BASE + (OFFER + MB) * DOLLAR_HEIGHT / 2], aligned_edge=RIGHT)

        # ---- 2.b.iii · The same payment: carry expenditure's boundary to revenue.
        revenue = expenditure.copy().set_fill(opacity=0).set_stroke(GOV, width=2.5)
        revenue.shift([WIDTH + GAP, -0.005, 0])
        revenue_label = Tex(rf'Revenue $\${OFFER:g}$', color=GOV).scale(0.62)
        revenue_label.face_mat = np.eye(3)
        revenue_label.add_updater(face_camera)
        revenue_label.update()
        revenue_label.move_to([right_edge + 0.3, -0.10, price_z + 0.2], aligned_edge=LEFT)

        # ---- 2.b.iv · Carry the existing MC label beside the same orange area.
        seller_cost = Polygon(
            [CLOSE_GAP / 2, -0.025, BAR_BASE], [right_edge, -0.025, BAR_BASE],
            [right_edge, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            [CLOSE_GAP / 2, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            fill_color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=0)
        ps_inset = 0.045  # Highlight margin; the surplus remains price minus cost.
        seller_ps = Polygon(
            [CLOSE_GAP / 2 + ps_inset, -0.04, BAR_BASE + MC * DOLLAR_HEIGHT + ps_inset],
            [right_edge - ps_inset, -0.04, BAR_BASE + MC * DOLLAR_HEIGHT + ps_inset],
            [right_edge - ps_inset, -0.04, price_z - ps_inset],
            [CLOSE_GAP / 2 + ps_inset, -0.04, price_z - ps_inset],
            stroke_color=SUPPLY, stroke_width=2.5, fill_opacity=0)
        cost_label = marginal_labels['seller']
        cost_label.clear_updaters()
        cost_label.add_updater(face_camera)
        cost_at = [right_edge + 0.3, -0.10, BAR_BASE + MC * DOLLAR_HEIGHT / 2]
        ps_label = Tex(rf'PS $\${OFFER - MC:g}$', color=SUPPLY).scale(0.62)
        ps_label.face_mat = np.eye(3)
        ps_label.add_updater(face_camera)
        ps_label.update()
        ps_label.move_to(
            [right_edge + 0.3, -0.10, BAR_BASE + (MC + OFFER) * DOLLAR_HEIGHT / 2], aligned_edge=LEFT)
        # Recall both sides together rather than replaying their earlier lessons.
        self.play(bars['buyer'].animate.set_opacity(0.13),
                  bars['seller'].animate.set_opacity(0.13),
                  cost_label.animate.move_to(cost_at, aligned_edge=LEFT),
                  FadeIn(expenditure), FadeIn(buyer_cs), FadeIn(revenue),
                  FadeIn(seller_cost), FadeIn(seller_ps), FadeIn(expenditure_label),
                  FadeIn(cs_label), FadeIn(revenue_label), FadeIn(ps_label))
        window = Polygon([4.0, -0.03, BAR_BASE + MC * DOLLAR_HEIGHT],
                         [4.35, -0.03, BAR_BASE + MC * DOLLAR_HEIGHT],
                         [4.35, -0.03, BAR_BASE + MB * DOLLAR_HEIGHT],
                         [4.0, -0.03, BAR_BASE + MB * DOLLAR_HEIGHT],
                         fill_color=TOTAL, fill_opacity=0.15, stroke_width=0)
        window_line = Line([4.175, -0.045, BAR_BASE + MC * DOLLAR_HEIGHT],
                           [4.175, -0.045, BAR_BASE + MB * DOLLAR_HEIGHT], color=TOTAL, stroke_width=3)
        low_endpoint = Circle(radius=0.07, color=TOTAL, fill_color=BG, fill_opacity=1, stroke_width=2)
        low_endpoint.rotate(90 * DEGREES, RIGHT).move_to(window_line.get_start())
        high_endpoint = low_endpoint.copy().move_to(window_line.get_end())
        window_labels = VGroup()
        for value, color in [(2, SUPPLY), (4, GUIDE), (6, DEMAND)]:
            label = Tex(rf'\${value}', color=color).scale(0.62)
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to([4.6, -0.1, BAR_BASE + value * DOLLAR_HEIGHT])
            window_labels.add(label)
        chosen_price = Sphere(radius=0.055, color=GUIDE, resolution=(8, 6))
        chosen_price.move_to([4.175, -0.08, price_z])
        claim = fixed(Tex(r'$MC < P < MB$', color=DEFINITION).scale(DEFINITION_SCALE))
        endpoint_note = fixed(Tex('At an endpoint, one person is indifferent.', color=CAPTION).scale(DEFINITION_SCALE))
        unit = fixed(Tex('One pound', color=CAPTION).scale(DEFINITION_SCALE))
        VGroup(claim, endpoint_note, unit).arrange(DOWN, buff=0.10).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(window), ShowCreation(window_line), FadeIn(low_endpoint), FadeIn(high_endpoint),
                  FadeIn(window_labels), FadeIn(chosen_price), FadeIn(claim), FadeIn(endpoint_note), FadeIn(unit))
        self.pause('1.a')

        # ========== 2. Bidding ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15
        MB, MC, OFFER = 6, 2, 4
        BID_STEP = 0.25
        CROWD_MB = [6, 8, 4, 3, 7, 5, 4, 3, 2, 2]
        CROWD_MC = [2, 4, 3, 5, 4, 2, 6, 3, 5, 6]
        GROWTH_SEED = 6
        DOLLAR_HEIGHT, BAR_BASE = 0.55, 0.75
        BAR_WIDTH, CLOSE_WIDTH, CLOSE_GAP = 0.16, 1.10, 0.12
        WORLD_CENTER = np.array([0.0, 0.0, 1.8])
        CLOSE_CENTER = np.array([0.0, 0.0, 2.05])

        # Animate.py's world-text billboard: preserve 3D placement and scale.
        # Rebuild from flat glyphs, not cumulative float32 rotations, so camera
        # moves and backward seeks keep the letters planar and readable.
        def face_camera(m):
            if isinstance(m, DecimalNumber) and abs(m.get_value() - m.tracker.get_value()) > 1e-6:
                m.set_value(m.tracker.get_value())
                m.face_mat = np.eye(3)
                if hasattr(m, 'face_base'):
                    del m.face_base
            cur = self.camera.frame.get_orientation().as_matrix()
            if np.allclose(cur, m.face_mat, atol=1e-6):
                return
            if not hasattr(m, 'face_base'):
                m.face_base = [sub.get_points().astype(float).copy() for sub in m.get_family()]
            center = m.get_center().astype(float)
            for sub, base in zip(m.get_family(), m.face_base):
                if len(base):
                    sub.set_points(base @ cur.T)
                    sub.use_triangulated_fill = True
            m.move_to(center)
            m.face_mat = cur

        # Reconstruct B3's exact parked view without replaying its teaching stops.
        opening_skip = self.skip_animations
        self.skip_animations = True
        self.set_camera_orientation(phi=58 * DEGREES, theta=0,
                                    focal_distance=50)
        self.camera.frame.move_to(WORLD_CENTER)

        # ---- 2.a · The first two people; no market price has been established.
        head = fixed(title('Would they exchange?'))
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        self.play(FadeIn(head), FadeIn(floor), FadeIn(rim))

        bodies, bars, names, marginal_labels = {}, {}, {}, {}
        for key, x, value, color, name, term in [
            ('buyer', -1.65, MB, DEMAND, 'Gary', 'MB'),
            ('seller', 1.65, MC, SUPPLY, 'Molly', 'MC'),
        ]:
            shadow = Disk3D(radius=0.28, resolution=(2, 24), shading=(0, 0, 0),
                            opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(16, 10))
            orb.move_to([x, 0, 0.32])
            body = Group(shadow, orb)
            bar = Rectangle3D(width=BAR_WIDTH, height=value * DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT).move_to(
                [x, 0, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            name_label = Tex(name, color=INK).scale(0.65)
            name_label.face_mat = np.eye(3)
            name_label.add_updater(face_camera)
            name_label.anchor = body
            name_label.offset = LEFT * 0.75 if key == 'buyer' else RIGHT * 0.75
            name_label.add_updater(lambda m: m.move_to(
                np.array([m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.55, 0.13])
                + m.offset))
            name_label.update()
            value_label = Tex(rf'{term} $\${value:g}$', color=color).scale(0.62)
            value_label.face_mat = np.eye(3)
            value_label.add_updater(face_camera)
            value_label.anchor = bar
            value_label.value = value
            value_label.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.08,
                 BAR_BASE + m.value * DOLLAR_HEIGHT + 0.28]))
            value_label.update()
            bodies[key], bars[key] = body, bar
            names[key], marginal_labels[key] = name_label, value_label
            self.play(FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))

        # ---- 2.a.i · Same bars, now between the people and viewed from the side.
        self.play(
            self.camera.frame.animate.reorient(0, 90, center=CLOSE_CENTER, height=7.2),
            bodies['buyer'].animate.set_x(-1.45),
            bodies['seller'].animate.set_x(1.45),
            bars['buyer'].animate.stretch_to_fit_width(CLOSE_WIDTH).set_x(
                -(CLOSE_WIDTH + CLOSE_GAP) / 2),
            bars['seller'].animate.stretch_to_fit_width(CLOSE_WIDTH).set_x(
                (CLOSE_WIDTH + CLOSE_GAP) / 2),
            floor.animate.set_opacity(0.05), rim.animate.set_stroke(opacity=0.2),
            run_time=2.2)
        left_edge = -CLOSE_WIDTH - CLOSE_GAP / 2
        right_edge = CLOSE_WIDTH + CLOSE_GAP / 2
        price_z = BAR_BASE + OFFER * DOLLAR_HEIGHT
        zero = Line([left_edge - 0.15, -0.02, BAR_BASE],
                    [right_edge + 0.15, -0.02, BAR_BASE], color=MUTED, stroke_width=1.5)
        price_line = DashedLine([left_edge, -0.045, price_z],
                               [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        price_shadow = DashedLine([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                                 color=GUIDE, stroke_width=2).set_opacity(0.3)
        price_word = Tex(rf'Price $\${OFFER:g}$', color=GUIDE).scale(0.62)
        price_word.face_mat = np.eye(3)
        price_word.add_updater(face_camera)
        price_word.update()
        price_word.move_to([0, -0.10, price_z + 0.28])
        zero_word = Tex('0', color=CAPTION).scale(0.62)
        zero_word.face_mat = np.eye(3)
        zero_word.add_updater(face_camera)
        zero_word.update()
        zero_word.move_to([0, -0.10, BAR_BASE - 0.25])
        self.add(zero, zero_word)
        accepted_line = Line([left_edge, -0.045, price_z],
                             [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        self.add(accepted_line, accepted_shadow)

        # Keep the first pair's camera and plaza framing. Slide Gary and Molly
        # left together, then admit Amanda-Grace on the right of the center.
        BID_SCALE, ARC_RADIUS = 1.0, 3.7
        BID_BASE, BID_DOLLAR_HEIGHT = BAR_BASE * BID_SCALE, DOLLAR_HEIGHT * BID_SCALE
        BID_WIDTH = CLOSE_WIDTH * BID_SCALE
        bid_y = 0.0
        molly_x = 0.0
        bid_body_x = {'buyer': molly_x - 2.9 * BID_SCALE, 'seller': molly_x,
                      'challenger': molly_x + 2.9 * BID_SCALE}
        bid_mb_x = {'buyer': molly_x - 2.06 * BID_SCALE,
                    'challenger': molly_x + 2.06 * BID_SCALE}
        bid_mc_x = {'buyer': molly_x - 0.84 * BID_SCALE,
                    'challenger': molly_x + 0.84 * BID_SCALE}
        for label in [*names.values(), *marginal_labels.values()]:
            label.clear_updaters()
        tableau = [*bodies.values(), *names.values(),
                   marginal_labels['buyer'], accepted_line, accepted_shadow]
        tableau_moves = []
        for m in tableau:
            move = m.animate.scale(BID_SCALE, about_point=np.array([1.45, 0, 0]))
            move.shift([molly_x - 1.45, bid_y, 0])
            if isinstance(m, VMobject):
                move.set_stroke(width=m.get_stroke_width() * BID_SCALE)
                move.set_fill(border_width=0.5 * BID_SCALE)
            tableau_moves.append(move)
        self.play(
            self.camera.frame.animate.reorient(0, 90,
                center=[molly_x, bid_y, 2.05 * BID_SCALE], height=7.2 * BID_SCALE),
            *tableau_moves,
            *[bar.animate.scale(BID_SCALE, about_point=np.array([1.45, 0, 0]))
                .shift([molly_x - 1.45, bid_y, 0]).set_opacity(0.65)
                for bar in bars.values()], run_time=1.8)
        marginal_labels['seller'].scale(BID_SCALE).set_fill(border_width=0.5 * BID_SCALE)
        for label in marginal_labels.values():
            label.add_updater(face_camera)
            label.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.08 * BID_SCALE,
                 BID_BASE + m.value * BID_DOLLAR_HEIGHT + 0.28 * BID_SCALE]))
            label.update()
        for label in names.values():
            label.offset *= BID_SCALE
            label.add_updater(face_camera)
            label.add_updater(lambda m: m.move_to(
                np.array([m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.55 * BID_SCALE,
                          0.13 * BID_SCALE]) + m.offset))
            label.update()
        self.play(FadeIn(marginal_labels['seller']))
        deal_number = Tex(r'\$4.00', color=GUIDE).scale(0.62 * BID_SCALE)
        deal_number.set_fill(border_width=0.5 * BID_SCALE)
        deal_number.face_mat = np.eye(3)
        deal_number.add_updater(face_camera)
        deal_number.update()
        deal_number.move_to([molly_x - 1.45 * BID_SCALE, bid_y - 0.15 * BID_SCALE,
                             (price_z + 0.25) * BID_SCALE])

        shadow = Disk3D(radius=0.28 * BID_SCALE, resolution=(2, 24), shading=(0, 0, 0),
                        opacity=0.28).set_color(DEMAND).move_to(
                            [bid_body_x['challenger'], bid_y, 0.025 * BID_SCALE])
        orb = Sphere(radius=0.23 * BID_SCALE, color=DEMAND, resolution=(16, 10))
        orb.move_to([bid_body_x['challenger'], bid_y, 0.32 * BID_SCALE])
        body = Group(shadow, orb)
        bar = Rectangle3D(width=BID_WIDTH, height=7 * BID_DOLLAR_HEIGHT,
                          resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        bar.rotate(90 * DEGREES, RIGHT).move_to(
            [bid_mb_x['challenger'], bid_y, BID_BASE + 7 * BID_DOLLAR_HEIGHT / 2])
        name_label = Tex('Amanda-Grace', color=INK).scale(0.62 * BID_SCALE)
        name_label.set_fill(border_width=0.5 * BID_SCALE)
        name_label.face_mat = np.eye(3)
        name_label.add_updater(face_camera)
        name_label.anchor = body
        name_label.add_updater(lambda m: m.move_to(
            [m.anchor.get_center()[0] + 0.4 * BID_SCALE,
             m.anchor.get_center()[1] - 0.55 * BID_SCALE, 0.13 * BID_SCALE],
            aligned_edge=LEFT))
        name_label.update()
        value_label = Tex(r'MB $\$7$', color=DEMAND).scale(0.62 * BID_SCALE)
        value_label.set_fill(border_width=0.5 * BID_SCALE)
        value_label.face_mat = np.eye(3)
        value_label.add_updater(face_camera)
        value_label.anchor, value_label.value = bar, 7
        value_label.add_updater(lambda m: m.move_to(
            [m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.08 * BID_SCALE,
             BID_BASE + m.value * BID_DOLLAR_HEIGHT + 0.28 * BID_SCALE]))
        value_label.update()
        bodies['challenger'], bars['challenger'] = body, bar
        names['challenger'], marginal_labels['challenger'] = name_label, value_label
        self.remove(head)
        head = fixed(title('Would Molly switch?'))
        self.play(FadeIn(head), FadeIn(deal_number),
                  FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))
        self.remove(zero, zero_word)
        self.skip_animations = opening_skip

        # Amanda-Grace offers $4.25.
        bidder = 'challenger'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 4.25 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${4.25:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.45)
        # Molly compares the existing price with the proposed price above.
        seller_gain = fixed(Tex(r'Molly receives $\$0.25$ more.', color=SUPPLY).scale(0.7443)
            .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(seller_gain))
        self.pause('1.b')
        self.play(FadeOut(seller_gain),
                  Transform(head, fixed(title('Who gets the spinach?'))), run_time=0.3)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.75)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Gary offers $4.50.
        bidder = 'buyer'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 4.5 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${4.5:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.45)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.75)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Amanda-Grace offers $4.75.
        bidder = 'challenger'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 4.75 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${4.75:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Gary offers $5.00.
        bidder = 'buyer'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 5.0 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${5.0:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Amanda-Grace offers $5.25.
        bidder = 'challenger'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 5.25 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${5.25:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Gary offers $5.50.
        bidder = 'buyer'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 5.5 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${5.5:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Amanda-Grace offers $5.75.
        bidder = 'challenger'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 5.75 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${5.75:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Gary offers $6.00.
        bidder = 'buyer'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 6.0 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${6.0:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label

        # Amanda-Grace offers $6.25.
        bidder = 'challenger'
        mc_x = bid_mc_x[bidder]
        x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
        x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
        height = BID_BASE + 6.25 * BID_DOLLAR_HEIGHT
        challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                              [x1, bid_y - 0.045 * BID_SCALE, height],
                              dash_length=0.05 * BID_SCALE,
                              color=GUIDE, stroke_width=3 * BID_SCALE)
        challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                     [x1, bid_y, 0.04 * BID_SCALE],
                                     dash_length=0.05 * BID_SCALE,
                                     color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        offer_label = Tex(rf'\${6.25:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
        offer_label.set_fill(border_width=0.5 * BID_SCALE)
        offer_label.face_mat = np.eye(3)
        offer_label.add_updater(face_camera)
        offer_label.update()
        offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                             height + 0.25 * BID_SCALE])
        self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                  run_time=0.25)
        # Keep the old solid price and the new dashed price visible until
        # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
        self.play(bars['seller'].animate.set_x(mc_x),
                  run_time=0.45)
        new_line = Line([x0, bid_y - 0.045 * BID_SCALE, height],
                        [x1, bid_y - 0.045 * BID_SCALE, height],
                        color=GUIDE, stroke_width=3 * BID_SCALE)
        new_shadow = Line([x0, bid_y, 0.04 * BID_SCALE], [x1, bid_y, 0.04 * BID_SCALE],
                          color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
        # Keep every dash and the new price number anchored. Only the gaps
        # appear as the former deal fades; there is no dashed-to-line morph.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3 * BID_SCALE)
            for a, b in zip(challenge, challenge[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE,
                 stroke_width=2 * BID_SCALE).set_opacity(0.3)
            for a, b in zip(challenge_shadow, challenge_shadow[1:])])
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow), FadeOut(deal_number),
                  FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(challenge, challenge_shadow, price_gaps, shadow_gaps)
        self.add(new_line, new_shadow)
        accepted_line, accepted_shadow, deal_number = new_line, new_shadow, offer_label
        # ---- 1.b.settled · Buyer-side outbidding has stopped.
        self.play(Transform(head, fixed(title('Who still wants to bid?'))), run_time=0.4)
        stop_reason = fixed(Tex(r"Gary's next bid: $\$6.50 > \mathrm{MB}\ \$6$.",
                               color=DEFINITION).scale(DEFINITION_SCALE))
        counts = fixed(Tex(r'At $\$6.25$: 1 willing buyer, 1 seller.', color=CAPTION)
                       .scale(DEFINITION_SCALE))
        VGroup(stop_reason, counts).arrange(DOWN, buff=0.12).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(stop_reason), FadeIn(counts))
        self.pause('1.b.settled')

        # ========== 3. TwoTrades ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15
        MB, MC, OFFER = 6, 2, 4
        BID_STEP = 0.25
        CROWD_MB = [6, 8, 4, 3, 7, 5, 4, 3, 2, 2]
        CROWD_MC = [2, 4, 3, 5, 4, 2, 6, 3, 5, 6]
        GROWTH_SEED = 6
        DOLLAR_HEIGHT, BAR_BASE = 0.55, 0.75
        BAR_WIDTH, CLOSE_WIDTH, CLOSE_GAP = 0.16, 1.10, 0.12
        WORLD_CENTER = np.array([0.0, 0.0, 1.8])
        CLOSE_CENTER = np.array([0.0, 0.0, 2.05])

        # Animate.py's world-text billboard: preserve 3D placement and scale.
        # Rebuild from flat glyphs, not cumulative float32 rotations, so camera
        # moves and backward seeks keep the letters planar and readable.
        def face_camera(m):
            if isinstance(m, DecimalNumber) and abs(m.get_value() - m.tracker.get_value()) > 1e-6:
                m.set_value(m.tracker.get_value())
                m.face_mat = np.eye(3)
                if hasattr(m, 'face_base'):
                    del m.face_base
            cur = self.camera.frame.get_orientation().as_matrix()
            if np.allclose(cur, m.face_mat, atol=1e-6):
                return
            if not hasattr(m, 'face_base'):
                m.face_base = [sub.get_points().astype(float).copy() for sub in m.get_family()]
            center = m.get_center().astype(float)
            for sub, base in zip(m.get_family(), m.face_base):
                if len(base):
                    sub.set_points(base @ cur.T)
                    sub.use_triangulated_fill = True
            m.move_to(center)
            m.face_mat = cur

        # Reconstruct the exact end of B3's 2.c; do not replay its earlier lesson.
        opening_skip = self.skip_animations
        self.skip_animations = True
        BID_SCALE, ARC_RADIUS = 1.0, 3.7
        BID_DOLLAR_HEIGHT = DOLLAR_HEIGHT
        self.set_camera_orientation(phi=90 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(CLOSE_CENTER).set_height(7.2)
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.05).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.2)
        head = fixed(title('Who gets the spinach?'))
        bodies, bars, names, marginal_labels = {}, {}, {}, {}
        for key, body_x, bar_x, value, color, name, term, offset in [
            ('buyer', -2.9, -2.06, 6, DEMAND, 'Gary', 'MB', LEFT * 0.75),
            ('seller', 0.0, 0.84, 2, SUPPLY, 'Molly', 'MC', RIGHT * 0.75),
            ('challenger', 2.9, 2.06, 7, DEMAND, 'Amanda-Grace', 'MB', RIGHT * 0.75),
        ]:
            shadow = Disk3D(radius=0.28, resolution=(2, 24), shading=(0, 0, 0),
                            opacity=0.28).set_color(color).move_to([body_x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(16, 10))
            orb.move_to([body_x, 0, 0.32])
            body = Group(shadow, orb)
            bar = Rectangle3D(width=CLOSE_WIDTH, height=value * DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT).move_to([bar_x, 0, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            name_label = Tex(name, color=INK).scale(0.65)
            name_label.face_mat = np.eye(3)
            name_label.add_updater(face_camera)
            name_label.anchor, name_label.offset = body, offset
            name_label.add_updater(lambda m: m.move_to(np.array([
                m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.55, 0.13]) + m.offset))
            name_label.update()
            value_label = Tex(rf'{term} $\${value}$', color=color).scale(0.62)
            value_label.face_mat = np.eye(3)
            value_label.add_updater(face_camera)
            value_label.anchor, value_label.value = bar, value
            value_label.add_updater(lambda m: m.move_to([
                m.anchor.get_center()[0], m.anchor.get_center()[1] - 0.08,
                BAR_BASE + m.value * DOLLAR_HEIGHT + 0.28]))
            value_label.update()
            bodies[key], bars[key] = body, bar
            names[key], marginal_labels[key] = name_label, value_label
        accepted_line = Line([0.29, -0.045, BAR_BASE + 6.25 * DOLLAR_HEIGHT],
                             [2.61, -0.045, BAR_BASE + 6.25 * DOLLAR_HEIGHT], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([0.29, 0, 0.04], [2.61, 0, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        deal_number = Tex(r'\$6.25', color=GUIDE).scale(0.62).set_fill(border_width=0.5)
        deal_number.face_mat = np.eye(3)
        deal_number.add_updater(face_camera)
        deal_number.update()
        deal_number.move_to([1.45, -0.15, BAR_BASE + 6.25 * DOLLAR_HEIGHT + 0.25])
        self.add(floor, rim, head, *bodies.values(), *bars.values(),
                 *names.values(), *marginal_labels.values(), accepted_line, accepted_shadow, deal_number)

        # ---- 3.a · Reveal the arcs, with the unmatched buyer on the buyer side.
        self.play(*[FadeOut(m) for m in marginal_labels.values()],
                  *[FadeOut(m) for m in names.values()], run_time=0.35)
        crowd_asks = [6.25, 4.5, 6, 6, 4.25, 6, 6, 6, 6, 6]
        crowd_matches = [None, None, None, None, 0, None, None, None, None, None]
        for bar in bars.values():
            bar.clear_updaters()
        # This label changes scale with the tableau. Turn it with the camera
        # explicitly so the billboard updater cannot restore its close-up size.
        deal_number.clear_updaters()
        self.remove(head)
        head = fixed(title('Where do prices settle?'))
        CROWD_SCALE, CROWD_BASE = 0.24, 0.52
        MARKET_PRICE_WIDTH, MARKET_SHADOW_WIDTH = 4.5, 2.4
        PAIR_WIDTH, PAIR_GAP = 0.18, 0.035
        # Molly stays on the seller arc. Unmatched buyers wait on the buyer
        # arc; the center belongs only to the person currently deliberating.
        seller_ys = [1.2, 2.8, 2.0, 0.4, -1.2, -0.4, -2.0, -2.8, -3.6, 3.6]
        seller_spots = [np.array([np.sqrt(ARC_RADIUS ** 2 - y ** 2), y, 0])
                        for y in seller_ys]
        buyer_spots = [np.array([-np.sqrt(ARC_RADIUS ** 2 - y ** 2), y, 0])
                       for y in np.linspace(ARC_RADIUS * np.sin(65 * DEGREES),
                                            -ARC_RADIUS * np.sin(65 * DEGREES), 10)]
        buyer_spots[0], buyer_spots[3] = buyer_spots[3], buyer_spots[0]
        first_partner_spot = seller_spots[0] + np.array([0.6, -0.35, 0])
        first_pair_mid = (seller_spots[0] + first_partner_spot) / 2
        crowd_bodies, crowd_bars, price_tags, price_trackers = {}, {}, {}, {}
        inherited = {('B', 0): 'buyer', ('B', 4): 'challenger',
                     ('S', 0): 'seller'}
        inherited_moves = []
        for side, values, spots, color in [('B', CROWD_MB, buyer_spots, DEMAND),
                                           ('S', CROWD_MC, seller_spots, SUPPLY)]:
            for i, value in enumerate(values):
                spot = first_partner_spot.copy() if (side, i) == ('B', 4) else spots[i].copy()
                pair_side = -1 if side == 'B' else 1
                bar_at = spot.copy()
                if (side, i) in [('B', 4), ('S', 0)]:
                    # Keep MC on the left and MB on the right until this
                    # first partnership ends; no crossing through Molly.
                    pair_side *= -1
                    bar_at = first_pair_mid + RIGHT * pair_side * (PAIR_WIDTH + PAIR_GAP) / 2
                if (side, i) in inherited:
                    key = inherited[side, i]
                    body, bar = bodies[key], bars[key]
                    body[1].set_opacity(1)
                    body[0].set_opacity(0.28)
                    inherited_moves.append(body.animate.scale(0.7 / BID_SCALE)
                        .move_to([*spot[:2], 0.19]))
                    inherited_moves.append(bar.animate.stretch(CROWD_SCALE / BID_DOLLAR_HEIGHT, 2)
                        .stretch_to_fit_width(PAIR_WIDTH).set_opacity(0.65).move_to(
                            [*bar_at[:2], CROWD_BASE + value * CROWD_SCALE / 2]))
                else:
                    shadow = Disk3D(radius=0.20, resolution=(2, 16), shading=(0, 0, 0),
                                    opacity=0.22).set_color(color).move_to([*spot[:2], 0.025])
                    orb = Sphere(radius=0.16, color=color, resolution=(12, 8))
                    orb.move_to([*spot[:2], 0.25])
                    body = Group(shadow, orb)
                    bar = Rectangle3D(width=PAIR_WIDTH, height=value * CROWD_SCALE,
                                      resolution=(2, 2), opacity=0.65).set_color(color)
                    bar.rotate(90 * DEGREES, RIGHT).move_to(
                        [*spot[:2], CROWD_BASE + value * CROWD_SCALE / 2])
                bar.anchor, bar.value = body, value
                bar.partner, bar.pairing, bar.pair_side = body, ValueTracker(0), pair_side
                crowd_bodies[side, i], crowd_bars[side, i] = body, bar
                if side == 'S':
                    tracker = ValueTracker(crowd_asks[i])
                    tag = DecimalNumber(crowd_asks[i], num_decimal_places=2,
                                        color=GUIDE).scale(0.58)
                    tag.tracker, tag.anchor = tracker, bar if i == 0 else body
                    tag.face_mat = np.eye(3)
                    tag.add_updater(face_camera)
                    if i == 0:
                        # Carry Molly's winning-price readout through the pullback.
                        tag.add_updater(lambda m: m.move_to([
                            m.anchor.get_center()[0] + 0.65,
                            m.anchor.get_center()[1] - 0.12,
                            CROWD_BASE + m.tracker.get_value() * CROWD_SCALE + 0.25]))
                    else:
                        tag.add_updater(lambda m: m.move_to(
                            m.anchor.get_center() + RIGHT * 0.55 + DOWN * 0.15 + OUT * 0.45))
                    tag.update()
                    price_tags[i], price_trackers[i] = tag, tracker
        for key, partner in [(('B', 4), ('S', 0)), (('S', 0), ('B', 4))]:
            crowd_bars[key].partner = crowd_bodies[partner]
            crowd_bars[key].pairing.set_value(1)
        price_height = CROWD_BASE + crowd_asks[0] * CROWD_SCALE
        pair_left = first_pair_mid[:2] - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
        pair_right = first_pair_mid[:2] + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
        # One continuous rescaling: keep the same accepted line and shadow,
        # and finish directly at the compact pair (no second docking motion).
        self.play(FadeIn(head), self.camera.frame.animate.reorient(
            0, 48, center=[0, 0, 0.65], height=10.4), *inherited_moves,
            accepted_line.animate.put_start_and_end_on(
                np.append(pair_left, price_height), np.append(pair_right, price_height)).set_stroke(width=MARKET_PRICE_WIDTH),
            accepted_shadow.animate.put_start_and_end_on(
                np.append(pair_left, 0.04), np.append(pair_right, 0.04)).set_stroke(width=MARKET_SHADOW_WIDTH),
            deal_number.animate.scale(1 / BID_SCALE).rotate(-42 * DEGREES, RIGHT)
                .set_fill(border_width=0.5).move_to([
                    first_pair_mid[0] - (PAIR_WIDTH + PAIR_GAP) / 2 + 0.65,
                    first_pair_mid[1] - 0.12, price_height + 0.25]),
            floor.animate.set_opacity(0.14), rim.animate.set_stroke(opacity=0.6), run_time=2.2)
        # Start this independent reminder in B3's actual oblique plaza.
        # Andrew's arrival must be visible before the head-on decision view.
        self.skip_animations = opening_skip
        # Install following only after the authored transition has completed;
        # otherwise these updaters snap the bars to their bodies mid-resize.
        for bar in crowd_bars.values():
            bar.add_updater(lambda m: m.move_to(np.append(
                (1 - m.pairing.get_value()) * m.anchor.get_center()[:2]
                + m.pairing.get_value() * ((m.anchor.get_center()[:2]
                    + m.partner.get_center()[:2]) / 2
                    + np.array([m.pair_side * (PAIR_WIDTH + PAIR_GAP) / 2, 0])),
                CROWD_BASE + m.value * CROWD_SCALE / 2)))
        connection_by_buyer, ground_by_buyer = {4: accepted_line}, {4: accepted_shadow}
        hub = DashedVMobject(Circle(radius=0.35, color=MUTED, stroke_width=2),
                             num_dashes=12).set_stroke(opacity=0.6).shift(OUT * 0.035)
        self.play(FadeIn(hub), run_time=0.35)


        # ---- 3.a.overview · Reveal both curves in place, with the camera still.
        side_axes, side_frames, side_counts, panel_bars = {}, {}, {}, {}
        panel_ids = {'B': [4, 0], 'S': [0]}
        for side, x, word, term, values, color in [
            ('B', -5.9, 'Demand', 'MB', CROWD_MB, DEMAND),
            ('S', 5.9, 'Supply', 'MC', CROWD_MC, SUPPLY),
        ]:
            panel_ax = style_axes([0, 10, 1], [0, 8, 2], x_length=3, y_length=3.5)
            panel_ax.shift(np.array([x, 0.05, 0]) -
                           (panel_ax.c2p(0, 0) + panel_ax.c2p(10, 8)) / 2)
            panel_ticks = VGroup(*[Tex(str(p), color=CAPTION).scale(0.7).next_to(
                panel_ax.c2p(0, p), LEFT, buff=0.10) for p in (0, 2, 4, 6, 8)])
            count = len(panel_ids[side])
            count_label = DecimalNumber(count, num_decimal_places=0, color=MUTED).scale(0.7)
            count_label.move_to(panel_ax.c2p(10, 0) + DOWN * 0.32)
            panel_caps = VGroup(
                Tex(word, color=color).scale(0.8).move_to([x, 2.8, 0]),
                Tex(rf'{term} ($\$$)', color=color).scale(0.7).move_to([x, 2.3, 0]),
                Tex('0', color=MUTED).scale(0.7).move_to(panel_ax.c2p(0, 0) + DOWN * 0.32),
                Tex('Units', color=CAPTION).scale(0.7).move_to([x, -2.5, 0]))
            frame = fixed(VGroup(panel_ax, panel_ticks, panel_caps, count_label))
            side_axes[side], side_frames[side], side_counts[side] = panel_ax, frame, count_label
            for rank, i in enumerate(panel_ids[side]):
                x0, x1 = 10 * rank / count, 10 * (rank + 1) / count
                panel_bars[side, i] = fixed(Polygon(panel_ax.c2p(x0, 0), panel_ax.c2p(x1, 0),
                    panel_ax.c2p(x1, values[i]), panel_ax.c2p(x0, values[i]),
                    color=color, fill_color=color, fill_opacity=0.22, stroke_width=2))
        posted_marks = {}
        mark = fixed(DashedVMobject(Line(LEFT, RIGHT, color=GUIDE, stroke_width=3), num_dashes=4))
        mark.anchor, mark.axis, mark.tracker = panel_bars['S', 0], side_axes['S'], price_trackers[0]
        mark.add_updater(lambda m: m.stretch_to_fit_width(m.anchor.get_width() * 0.92)
            .move_to([m.anchor.get_center()[0], m.axis.c2p(0, m.tracker.get_value())[1], 0]))
        mark.update()
        posted_marks[0] = mark
        posted_caption = fixed(Tex('Posted prices', color=GUIDE).scale(0.7).move_to([5.9, -3.05, 0]))
        price_tags[0].update()
        self.play(*[FadeIn(m) for m in side_frames.values()],
            *[FadeIn(m) for m in panel_bars.values()],
            ReplacementTransform(deal_number, price_tags[0]), FadeIn(mark),
            FadeIn(posted_caption), run_time=0.45)
        # Buyers have separate circle-arrival and price-comparison holds.
        # The long buyer name stays toward the plaza interior on either arc.


        arrival_order = [('S', 4)]  # Only Andrew enters this independent reminder.
        present_buyers, present_sellers = 2, 1
        entry_caption = None
        for side, i in arrival_order:
            if entry_caption is not None:
                self.play(FadeOut(entry_caption), run_time=0.2)
            present_buyers += int(side == 'B')
            present_sellers += int(side == 'S')
            entry_caption = fixed(Tex(
                f'{present_buyers} buyers, {present_sellers} sellers',
                color=CAPTION).scale(DEFINITION_SCALE))
            entry_caption.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
            entrances = [FadeIn(crowd_bodies[side, i]), FadeIn(crowd_bars[side, i]),
                         FadeIn(entry_caption)]
            self.play(*entrances, run_time=0.5 if i in [1, 2, 4] else 0.5)
            values = CROWD_MB if side == 'B' else CROWD_MC
            color = DEMAND if side == 'B' else SUPPLY
            panel_ids[side].append(i)
            panel_ids[side].sort(key=lambda j: (-values[j] if side == 'B' else values[j], j))
            count = len(panel_ids[side])
            side_counts[side].set_value(count)
            side_counts[side].move_to(side_axes[side].c2p(10, 0) + DOWN * 0.32)
            top = screen_point(self.camera.frame,
                [*crowd_bodies[side, i].get_center()[:2], CROWD_BASE + values[i] * CROWD_SCALE])
            base = screen_point(self.camera.frame,
                [*crowd_bodies[side, i].get_center()[:2], CROWD_BASE])
            panel_bars[side, i] = fixed(Rectangle(width=0.06, height=abs(top[1] - base[1]),
                color=color, fill_color=color, fill_opacity=0.22, stroke_width=2)
                .move_to((top + base) / 2))
            self.add(panel_bars[side, i])
            rearrange = []
            for rank, j in enumerate(panel_ids[side]):
                panel_ax = side_axes[side]
                x0, x1 = 10 * rank / count, 10 * (rank + 1) / count
                target = fixed(Polygon(panel_ax.c2p(x0, 0), panel_ax.c2p(x1, 0),
                    panel_ax.c2p(x1, values[j]), panel_ax.c2p(x0, values[j]),
                    color=color, fill_color=color, fill_opacity=0.22, stroke_width=2))
                rearrange.append(Transform(panel_bars[side, j], target))
            self.play(*rearrange, run_time=0.45 if i in [1, 2, 4] else 0.4)
            if side == 'S':
                mark = fixed(DashedVMobject(Line(LEFT, RIGHT, color=GUIDE, stroke_width=3),
                                           num_dashes=4))
                mark.anchor, mark.axis = panel_bars['S', i], side_axes['S']
                mark.tracker = price_trackers[i]
                mark.add_updater(lambda m: m.stretch_to_fit_width(m.anchor.get_width() * 0.92)
                    .move_to([m.anchor.get_center()[0], m.axis.c2p(0, m.tracker.get_value())[1], 0]))
                mark.update()
                posted_marks[i] = mark
                if i != 4:
                    reveal = [FadeIn(mark)]
                    if present_sellers == 3:
                        reveal.extend([FadeOut(price_tags[0]), FadeOut(price_tags[4])])
                    self.play(*reveal, run_time=0.5)
            if side == 'S' and i == 4:
                entry_names = {}
                for key, word, offset in [
                    (('B', 0), 'Gary', DOWN * 0.55),
                    (('B', 4), 'Amanda-Grace', DOWN * 0.35),
                    (('S', 0), 'Molly', DOWN * 0.30 + LEFT * 0.85),
                    (('S', 4), 'Andrew', DOWN * 0.55 + RIGHT * 0.6),
                ]:
                    label = Tex(word, color=INK).scale(0.60)
                    label.face_mat = np.eye(3)
                    label.add_updater(face_camera)
                    label.anchor, label.offset = crowd_bodies[key], offset
                    # At entry Amanda-Grace stands to Molly's right. Keep her
                    # name beneath her own orb, with Molly's name left/below.
                    label.inward = False
                    label.add_updater(lambda m: m.move_to(
                        np.array([*m.anchor.get_center()[:2], 0.13]) + m.offset
                        + (LEFT * PLAZA_NAME_INSET * np.clip(m.anchor.get_x(), -1, 1) if m.inward else ORIGIN)))
                    label.update()
                    entry_names[key] = label
                self.play(*[FadeIn(label) for label in entry_names.values()], run_time=0.4)
                ask_height = CROWD_BASE + crowd_asks[4] * CROWD_SCALE
                ask_world = Line([seller_spots[4][0] - 0.22, seller_spots[4][1], ask_height],
                                 [seller_spots[4][0] + 0.22, seller_spots[4][1], ask_height],
                                 color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                ask_caption = fixed(Tex(r'$\$4.25$', color=GUIDE).scale(0.7)
                    .move_to([5.9, -3.05, 0]))
                self.remove(posted_caption)
                self.play(FadeIn(price_tags[4]), FadeIn(ask_world),
                          FadeIn(posted_marks[4]), FadeIn(ask_caption), run_time=0.7)
                # Establish all four actual people in the approved B3 frame.
                # The close-up below is only Amanda-Grace's deliberation.
                self.pause('1.b.two_trades.plaza')
                self.play(FadeOut(entry_caption), FadeOut(ask_world), FadeOut(ask_caption), run_time=0.3)
                entry_caption = None

                # One buyer deliberates; the remaining adjustment is compressed below.
                for chooser, offer, displaced in [(4, 4.25, None)]:
                    chooser_body = crowd_bodies['B', chooser]
                    if chooser in connection_by_buyer:
                        old_line = connection_by_buyer.pop(chooser)
                        old_ground = ground_by_buyer.pop(chooser)
                        self.play(FadeOut(old_line), FadeOut(old_ground),
                            crowd_bars['B', chooser].pairing.animate.set_value(0),
                            crowd_bars['S', crowd_matches[chooser]].pairing.animate.set_value(0),
                            run_time=0.25)
                        crowd_bars['B', chooser].pair_side = -1
                        crowd_bars['S', crowd_matches[chooser]].pair_side = 1
                    buyer_ring = Circle(radius=0.29, color=DEMAND, stroke_width=3)
                    buyer_ring.move_to([0, 0, 0.045])
                    buyer_focus = fixed(SurroundingRectangle(panel_bars['B', chooser],
                        color=DEMAND, buff=0.04, stroke_width=3))
                    self.play(chooser_body.animate.move_to([0, 0, chooser_body.get_center()[2]]),
                              FadeIn(buyer_focus),
                              FadeIn(buyer_ring, shift=-np.append(crowd_bodies['B', chooser].get_center()[:2], 0)),
                              hub.animate.set_stroke(opacity=1), run_time=0.65)
                    if chooser == 4:
                        # Once that first partnership separates, restore B3's
                        # established offsets for the later paired positions.
                        entry_names['B', 4].offset = DOWN * 0.55
                        entry_names['B', 4].inward = True
                        entry_names['S', 0].offset = DOWN * 0.55 + RIGHT * 0.6
                    value = CROWD_MB[chooser]
                    mb_guide = fixed(DashedLine(side_axes['S'].c2p(0, value),
                        side_axes['S'].c2p(10, value), color=DEMAND, stroke_width=2))
                    mb_read = fixed(Tex(rf'MB $\${value}$', color=DEMAND).scale(0.7)
                        .move_to(side_axes['S'].c2p(5, value) + UP * 0.35))
                    price_caption = fixed(Tex('Price to buy', color=GUIDE).scale(0.7)
                        .move_to([5.9, -3.05, 0]))
                    self.play(FadeIn(mb_guide), FadeIn(mb_read), FadeIn(price_caption), run_time=0.5)
                    option_rings, option_columns, option_prices = {}, {}, {}
                    for rank, seller in enumerate(panel_ids['S']):
                        needed = crowd_asks[seller] + (BID_STEP
                            if seller in crowd_matches and crowd_matches[chooser] != seller else 0)
                        ring = Circle(radius=0.29, color=SUPPLY, stroke_width=3)
                        ring.move_to([*seller_spots[seller][:2], 0.045])
                        column = fixed(SurroundingRectangle(panel_bars['S', seller],
                            color=SUPPLY, buff=0.035, stroke_width=3))
                        x0, x1 = rank * 5, (rank + 1) * 5
                        tick = Line(side_axes['S'].c2p(x0 + 0.15, needed),
                                    side_axes['S'].c2p(x1 - 0.15, needed), color=GUIDE, stroke_width=3)
                        number = Tex(rf'$\${needed:.2f}$', color=GUIDE).scale(0.7)
                        number.move_to(side_axes['S'].c2p((x0 + x1) / 2, needed) + DOWN * 0.36)
                        price_mark = fixed(VGroup(tick, number))
                        option_rings[seller], option_columns[seller] = ring, column
                        option_prices[seller] = price_mark
                        self.play(FadeIn(ring), FadeIn(column), FadeIn(price_mark), run_time=0.6)
                    words = (r'Would Amanda-Grace keep paying $\$6.25$?' if chooser == 4
                             else r'Could Gary gain by offering $\$4.50$?')
                    decision_question = fixed(Tex(words, color=DEFINITION).scale(DEFINITION_SCALE)
                        .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                    self.play(FadeIn(decision_question))

                    if chooser == 4:
                        # Preserve the actual B3 plaza and return to it after this view.
                        decision_stage = list(self.mobjects)
                        self.play(*[FadeOut(m) for m in decision_stage], run_time=0.3)
                        self.play(self.camera.frame.animate.reorient(0, 90,
                            center=CLOSE_CENTER, height=7.2), run_time=2.2)
                        close_floor = floor.copy().set_opacity(0.05)
                        close_rim = rim.copy().set_stroke(opacity=0.2)
                        close_head = fixed(title('Stay or switch?'))
                        close_people, close_bars, close_names, close_values = {}, {}, {}, {}
                        for who, body_x, bar_x, value, term, color, offset in [
                            ('Amanda-Grace', -2.9, -2.06, 7, 'MB', DEMAND, LEFT * 0.75),
                            ('Molly', 0.0, -0.84, 2, 'MC', SUPPLY, RIGHT * 0.75),
                            ('Andrew', 2.9, 2.06, 4, 'MC', SUPPLY, RIGHT * 0.75),
                        ]:
                            shadow = Disk3D(radius=0.28, resolution=(2, 24), shading=(0, 0, 0),
                                            opacity=0.28).set_color(color).move_to([body_x, 0, 0.025])
                            orb = Sphere(radius=0.23, color=color, resolution=(16, 10))
                            orb.move_to([body_x, 0, 0.32])
                            close_people[who] = Group(shadow, orb)
                            bar = Rectangle3D(width=1.10, height=value * 0.55,
                                              resolution=(2, 2), opacity=0.65).set_color(color)
                            bar.rotate(90 * DEGREES, RIGHT).move_to([bar_x, 0, 0.75 + value * 0.55 / 2])
                            close_bars[who] = bar
                            name = Tex(who, color=INK).scale(0.62 * self.camera.frame.get_scale())
                            name.face_mat = np.eye(3)
                            name.add_updater(face_camera)
                            name.update()
                            name.move_to(self.camera.frame.get_center() + self.camera.frame.get_orientation().as_matrix()
                                         @ (np.array([screen_point(self.camera.frame, [body_x, 0, 0.32])[0], -2.30, 0]) * self.camera.frame.get_scale()))
                            close_names[who] = name
                            value_label = Tex(rf'{term} $\${value}$', color=color).scale(0.62)
                            value_label.face_mat = np.eye(3)
                            value_label.add_updater(face_camera)
                            value_label.update()
                            value_label.move_to([bar_x, -0.08, 0.75 + value * 0.55 + 0.28])
                            if who == 'Andrew':
                                value_label.shift(OUT * 0.22)
                            close_values[who] = value_label
                        stay_price_line = Line([-2.61, -0.045, 0.75 + 6.25 * 0.55],
                                               [-0.29, -0.045, 0.75 + 6.25 * 0.55], color=GUIDE, stroke_width=3)
                        stay_shadow = Line([-2.61, 0, 0.04], [-0.29, 0, 0.04],
                                           color=GUIDE, stroke_width=2).set_opacity(0.3)
                        switch_price_line = DashedLine([1.51, -0.045, 0.75 + 4.25 * 0.55],
                            [2.61, -0.045, 0.75 + 4.25 * 0.55], color=GUIDE, stroke_width=3, dash_length=0.05)
                        mb_read_across = DashedLine([-2.61, -0.045, 0.75 + 7 * 0.55],
                            [2.61, -0.045, 0.75 + 7 * 0.55], color=DEMAND, stroke_width=1.5).set_opacity(0.6)
                        # Plain choice labels sit beneath their corresponding sellers.
                        stay_words = VGroup(Tex(r'Pay $\$6.25$', color=INK), Tex(r'Gain $\$0.75$', color=DEMAND))
                        switch_words = VGroup(Tex(r'Pay $\$4.25$', color=INK), Tex(r'Gain $\$2.75$', color=DEMAND))
                        for words, who in [(stay_words, 'Molly'), (switch_words, 'Andrew')]:
                            words.arrange(DOWN, buff=0.12).scale(0.62 * self.camera.frame.get_scale())
                            words.face_mat = np.eye(3)
                            words.add_updater(face_camera)
                            words.update()
                            words.move_to(self.camera.frame.get_center() + self.camera.frame.get_orientation().as_matrix()
                                          @ (np.array([screen_point(self.camera.frame, close_people[who].get_center())[0], -3.12, 0]) * self.camera.frame.get_scale()))
                        close_objects = [close_floor, close_rim, close_head, *close_people.values(), *close_bars.values(),
                            *close_names.values(), *close_values.values(), stay_price_line, stay_shadow,
                            switch_price_line, mb_read_across, stay_words, switch_words]
                        self.play(*[FadeIn(m) for m in close_objects], run_time=0.7)
                        self.remove(stay_price_line)
                        self.add(stay_price_line)
                        self.pause('1.b.two_trades')
                        self.play(*[FadeOut(m) for m in close_objects], run_time=0.3)
                        self.play(self.camera.frame.animate.reorient(0, 48, center=[0, 0, 0.65], height=10.4),
                                  *[FadeIn(m) for m in decision_stage], run_time=2.2)
                    self.play(FadeOut(decision_question), run_time=0.2)
                    seller_at = seller_spots[4]
                    destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                    route = DashedLine([0, 0, 0.045], [*destination[:2], 0.045],
                                       color=MUTED, stroke_width=2).set_opacity(0.7)
                    self.play(FadeOut(option_rings[0]), FadeOut(option_columns[0]),
                              FadeOut(option_prices[0]), FadeIn(route), run_time=0.4)
                    if displaced is not None:
                        old_line = connection_by_buyer.pop(displaced)
                        old_ground = ground_by_buyer.pop(displaced)
                        self.play(FadeOut(old_line), FadeOut(old_ground),
                            crowd_bars['B', displaced].pairing.animate.set_value(0),
                            crowd_bars['S', crowd_matches[displaced]].pairing.animate.set_value(0),
                            run_time=0.25)
                    moves = [chooser_body.animate.move_to(
                        [*destination[:2], chooser_body.get_center()[2]]),
                             buyer_ring.animate.move_to([*destination[:2], 0.045])]
                    if displaced is not None:
                        displaced_body = crowd_bodies['B', displaced]
                        moves.append(displaced_body.animate.move_to(
                            [*buyer_spots[displaced][:2], displaced_body.get_center()[2]]))
                        crowd_matches[displaced] = None
                    crowd_matches[chooser], crowd_asks[4] = 4, offer
                    self.play(*moves, price_trackers[4].animate.set_value(offer), run_time=0.65)
                    for key, partner in [(('B', chooser), ('S', 4)), (('S', 4), ('B', chooser))]:
                        crowd_bars[key].partner = crowd_bodies[partner]
                    self.play(crowd_bars['B', chooser].pairing.animate.set_value(1),
                              crowd_bars['S', 4].pairing.animate.set_value(1), run_time=0.4)
                    midpoint = (destination[:2] + seller_at[:2]) / 2
                    pair_left = midpoint - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                    pair_right = midpoint + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                    height = CROWD_BASE + offer * CROWD_SCALE
                    connection_by_buyer[chooser] = Line([*pair_left, height], [*pair_right, height],
                                                       color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                    ground_by_buyer[chooser] = Line([*pair_left, 0.04], [*pair_right, 0.04],
                                                   color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
                    self.play(FadeOut(route), FadeIn(connection_by_buyer[chooser]),
                              FadeIn(ground_by_buyer[chooser]), run_time=0.4)
                    self.play(FadeOut(buyer_focus), FadeOut(buyer_ring), FadeOut(mb_guide), FadeOut(mb_read),
                              FadeOut(price_caption), FadeOut(option_rings[4]),
                              FadeOut(option_columns[4]), FadeOut(option_prices[4]),
                              hub.animate.set_stroke(opacity=0.6), run_time=0.4)
                self.play(FadeIn(posted_caption), run_time=0.3)
            # After Amanda-Grace's single deliberation, let the whole market settle.
            # This verified run fixes both the final prices and the actual partners.
            local_buyers, local_sellers = [0, 4], [0, 4]
            small_run = simulate([6, 7], [2, 4], [6.25, 4.25],
                initial_sellers=[None, 1], seed=34, step=BID_STEP)
            assert small_run.final.asks == (5.5, 5.5)
            assert tuple(crowd_asks[s] for s in local_sellers) == small_run.initial.asks
            assert tuple(None if crowd_matches[b] is None else
                local_sellers.index(crowd_matches[b]) for b in local_buyers) == small_run.initial.sellers
            settlement_caption = fixed(Tex('The same incentives bring both prices together.',
                color=INK).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
            self.play(FadeIn(settlement_caption), run_time=0.35)
            settlement_moves, settled_bars, new_connections = [], [], []
            for local_s, s in enumerate(local_sellers):
                crowd_asks[s] = small_run.final.asks[local_s]
                settlement_moves.append(price_trackers[s].animate.set_value(crowd_asks[s]))
            for local_b, b in enumerate(local_buyers):
                s = local_sellers[small_run.final.sellers[local_b]]
                crowd_matches[b] = s
                body, seller_at = crowd_bodies['B', b], seller_spots[s]
                destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                settlement_moves.append(body.animate.move_to([*destination[:2], body.get_center()[2]]))
                midpoint = (destination[:2] + seller_at[:2]) / 2
                for key, partner, pair_side in [(('B', b), ('S', s), -1), (('S', s), ('B', b), 1)]:
                    bar = crowd_bars[key]
                    # Hold the current geometry while its partner changes, then move once.
                    bar.suspend_updating()
                    bar.partner, bar.pair_side = crowd_bodies[partner], pair_side
                    bar.pairing.set_value(1)
                    bar_position = np.append(midpoint + np.array([pair_side * (PAIR_WIDTH + PAIR_GAP) / 2, 0]),
                                             CROWD_BASE + bar.value * CROWD_SCALE / 2)
                    settlement_moves.append(bar.animate.move_to(bar_position))
                    settled_bars.append(bar)
                pair_left = midpoint - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                pair_right = midpoint + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                height = CROWD_BASE + crowd_asks[s] * CROWD_SCALE
                if b in connection_by_buyer:
                    settlement_moves.append(connection_by_buyer[b].animate.put_start_and_end_on(
                        np.append(pair_left, height), np.append(pair_right, height)))
                    settlement_moves.append(ground_by_buyer[b].animate.put_start_and_end_on(
                        np.append(pair_left, 0.04), np.append(pair_right, 0.04)))
                else:
                    connection_by_buyer[b] = Line([*pair_left, height], [*pair_right, height],
                        color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                    ground_by_buyer[b] = Line([*pair_left, 0.04], [*pair_right, 0.04],
                        color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
                    new_connections.extend([connection_by_buyer[b], ground_by_buyer[b]])
            self.play(*settlement_moves, *[FadeIn(m) for m in new_connections], run_time=1.8)
            for bar in settled_bars:
                bar.resume_updating()
            self.play(FadeOut(settlement_caption), run_time=0.25)
            assert tuple(crowd_asks[s] for s in local_sellers) == small_run.final.asks
            assert tuple(None if crowd_matches[b] is None else
                local_sellers.index(crowd_matches[b]) for b in local_buyers) == small_run.final.sellers
        # ---- 1.b.equal_prices · Keep the two actual B3 pairs and both posted asks.
        self.remove(posted_caption)
        equal_prices = fixed(Tex(r'Both trades: $\$5.50$.', color=GUIDE).scale(DEFINITION_SCALE))
        equal_counts = fixed(Tex('2 willing buyers; 2 sellers.', color=CAPTION).scale(DEFINITION_SCALE))
        VGroup(equal_prices, equal_counts).arrange(DOWN, buff=0.12).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(Transform(head, fixed(title('Would either buyer switch?'))), FadeIn(equal_prices), FadeIn(equal_counts))
        self.pause('1.b.equal_prices')

        # ========== 4. Buyers ==========
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=90 * DEGREES, theta=0, gamma=0, focal_distance=50)
        self.camera.frame.move_to([0, 0, 1.9]).set_height(8)
        self.camera.fps = 15

        # Keep the approved full-width row throughout this price comparison.
        # Rank n is Q=n thousand pounds, so the equation passes through each bar top.
        values = np.array([12 - n / 5 for n in range(1, 60)])
        ROW_WIDTH, ROW_COUNT = 13.6, 59
        Q_STEP = ROW_WIDTH / ROW_COUNT
        Q_ZERO = -ROW_WIDTH / 2 - Q_STEP / 2
        ROW_BASE, ROW_DOLLAR_HEIGHT = 0.75, 0.28
        price = ValueTracker(6)
        show_willing = ValueTracker(0)
        self.add(price, show_willing)
        head = fixed(title('How many would buy at this price?'))
        one_lot = fixed(Tex('One person = 1,000 lb. Bar height = dollars per pound.', color=CAPTION))
        one_lot.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        full_bars, full_people, full_checks = Group(), Group(), VGroup()
        for n, value in enumerate(values):
            x = Q_ZERO + (n + 1) * Q_STEP
            bar = Rectangle3D(width=0.17, height=value * ROW_DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(DEMAND)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, 0, ROW_BASE + value * ROW_DOLLAR_HEIGHT / 2])
            bar.price, bar.value, bar.visibility = price, value, show_willing
            bar.add_updater(lambda m: m.set_opacity(0.65 - 0.47 * m.visibility.get_value() * float(not (m.value + 1e-7 >= m.price.get_value()))))
            shadow = Disk3D(radius=0.07, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28)
            shadow.set_color(DEMAND).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.065, color=DEMAND, resolution=(12, 8)).move_to([x, 0, 0.16])
            orb.price, orb.value, orb.visibility = price, value, show_willing
            orb.add_updater(lambda m: m.set_opacity(1 - 0.65 * m.visibility.get_value() * float(not (m.value + 1e-7 >= m.price.get_value()))))
            person = Group(shadow, orb)
            check = (VMobject(color=DEMAND, stroke_width=1.5).set_points_as_corners(
                [[-0.025, 0, 0], [-0.005, -0.018, 0], [0.032, 0.032, 0]]))
            check.price, check.value, check.visibility = price, value, show_willing
            check.anchor, check.face_mat = orb, np.eye(3)
            check.add_updater(face_camera)
            check.add_updater(lambda m: m.move_to(m.anchor.get_center() + OUT * 0.27).set_stroke(
                opacity=m.visibility.get_value() * float(m.value + 1e-7 >= m.price.get_value())).set_fill(opacity=0))
            full_bars.add(bar)
            full_people.add(person)
            full_checks.add(check)
        # This is the equation line, not a staircase around the individual bars.
        full_profile = Line([Q_ZERO, -0.045, ROW_BASE + 12 * ROW_DOLLAR_HEIGHT],
                            [Q_ZERO + 60 * Q_STEP, -0.045, ROW_BASE + 0 * ROW_DOLLAR_HEIGHT],
                            color=DEMAND, stroke_width=2.6)
        equation = Tex(r'$P=12-Q_d/5$', color=DEMAND).scale(0.67)
        equation.face_mat = np.eye(3)
        equation.add_updater(face_camera)
        equation.update()
        equation.move_to([4.7, 0, 4.65])
        price_guide = DashedLine([Q_ZERO, -0.045, ROW_BASE + 6 * ROW_DOLLAR_HEIGHT],
                                [Q_ZERO + 30 * Q_STEP, -0.045, ROW_BASE + 6 * ROW_DOLLAR_HEIGHT],
                                color=GUIDE, stroke_width=2.2)
        price_guide.price, price_guide.x0, price_guide.dx = price, Q_ZERO, Q_STEP
        price_guide.base, price_guide.dollar_height = ROW_BASE, ROW_DOLLAR_HEIGHT
        price_guide.add_updater(lambda m: set_dashed_endpoints(m,
            np.array([m.x0, -0.045, m.base + m.price.get_value() * m.dollar_height]),
            np.array([m.x0 + (60 - 5 * m.price.get_value()) * m.dx, -0.045, m.base + m.price.get_value() * m.dollar_height])))
        # The dollar amount follows the left end of the guide in world space.
        price_number = DecimalNumber(6, num_decimal_places=2, color=GUIDE).scale(0.57)
        price_number.tracker, price_number.anchor = price, price_guide
        price_number.face_mat = np.eye(3)
        price_number.add_updater(face_camera)
        price_number.add_updater(lambda m: m.move_to(m.anchor.get_start() + LEFT * 0.12, aligned_edge=RIGHT))
        price_word = Tex(r'\$', color=GUIDE).scale(0.57)
        price_word.anchor, price_word.face_mat = price_number, np.eye(3)
        price_word.add_updater(face_camera)
        price_word.add_updater(lambda m: m.next_to(m.anchor, LEFT, buff=0.03))
        price_units = Tex('/lb', color=CAPTION).scale(0.34)
        price_units.anchor, price_units.face_mat = price_number, np.eye(3)
        price_units.add_updater(face_camera)
        price_units.add_updater(lambda m: m.move_to(m.anchor.get_center() + LEFT * 0.12 + IN * 0.24))
        price_readout = VGroup(price_number, price_word, price_units)
        price_readout.update()
        quantity_tracker = ValueTracker(30)
        quantity_tracker.price, quantity_tracker.values = price, values
        quantity_tracker.add_updater(lambda m: m.set_value(int(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()))))
        self.add(quantity_tracker)
        quantity_number = Integer(30, color=DEMAND).scale(0.70)
        quantity_number.tracker = quantity_tracker
        # Bare quantity number, directly below the curve's current intersection.
        quantity_number.anchor, quantity_number.face_mat = price_guide, np.eye(3)
        quantity_number.add_updater(face_camera)
        quantity_number.add_updater(lambda m: m.move_to([m.anchor.get_end()[0], 0, -0.70]))
        quantity_readout = VGroup(quantity_number)
        self.add(head)
        self.play(FadeIn(full_bars), FadeIn(full_people), FadeIn(one_lot), run_time=1.0)
        self.play(Create(full_profile), FadeIn(equation), run_time=0.8)
        self.play(Create(price_guide), FadeIn(price_readout), FadeIn(quantity_readout),
                  show_willing.animate.set_value(1), FadeIn(full_checks), run_time=0.7)
        rule = fixed(Tex(r'$MB\geq P$: willing to buy. The marginal buyer is indifferent at $\$6$.', color=INK))
        rule.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(ReplacementTransform(one_lot, rule), full_people[29][1].animate.set_color(FOCUS))
        self.pause('1.c.buyers')
        self.play(full_people[29][1].animate.set_color(DEMAND), price.animate.set_value(3), run_time=2.0, rate_func=smooth)
        low = fixed(Tex(r'At $\$3$, 45 buyers are willing. We have not counted trades.', color=INK))
        low.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(ReplacementTransform(rule, low))
        self.pause('1.c.buyers.low')

        # ========== 5. Sellers ==========
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=90 * DEGREES, theta=0, gamma=0, focal_distance=50)
        self.camera.frame.move_to([0, 0, 1.9]).set_height(8)
        self.camera.fps = 15

        # Keep the approved full-width row throughout this price comparison.
        # Rank n is Q=n thousand pounds, so the equation passes through each bar top.
        values = np.array([2 + n / 20 for n in range(1, 101)])
        ROW_WIDTH, ROW_COUNT = 13.8, 100
        Q_STEP = ROW_WIDTH / ROW_COUNT
        Q_ZERO = -ROW_WIDTH / 2 - Q_STEP / 2
        ROW_BASE, ROW_DOLLAR_HEIGHT = 0.75, 0.28
        price = ValueTracker(3)
        show_willing = ValueTracker(0)
        self.add(price, show_willing)
        head = fixed(title('How many would sell at this price?'))
        one_lot = fixed(Tex('One person = 1,000 lb. Bar height = dollars per pound.', color=CAPTION))
        one_lot.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        full_bars, full_people, full_checks = Group(), Group(), VGroup()
        for n, value in enumerate(values):
            x = Q_ZERO + (n + 1) * Q_STEP
            bar = Rectangle3D(width=0.105, height=value * ROW_DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, 0, ROW_BASE + value * ROW_DOLLAR_HEIGHT / 2])
            bar.price, bar.value, bar.visibility = price, value, show_willing
            bar.add_updater(lambda m: m.set_opacity(0.65 - 0.47 * m.visibility.get_value() * float(not (m.value <= m.price.get_value() + 1e-7))))
            shadow = Disk3D(radius=0.07, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28)
            shadow.set_color(SUPPLY).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.065, color=SUPPLY, resolution=(12, 8)).move_to([x, 0, 0.16])
            orb.price, orb.value, orb.visibility = price, value, show_willing
            orb.add_updater(lambda m: m.set_opacity(1 - 0.65 * m.visibility.get_value() * float(not (m.value <= m.price.get_value() + 1e-7))))
            person = Group(shadow, orb)
            check = (VMobject(color=SUPPLY, stroke_width=1.5).set_points_as_corners(
                [[-0.025, 0, 0], [-0.005, -0.018, 0], [0.032, 0.032, 0]]))
            check.price, check.value, check.visibility = price, value, show_willing
            check.anchor, check.face_mat = orb, np.eye(3)
            check.add_updater(face_camera)
            check.add_updater(lambda m: m.move_to(m.anchor.get_center() + OUT * 0.27).set_stroke(
                opacity=m.visibility.get_value() * float(m.value <= m.price.get_value() + 1e-7)).set_fill(opacity=0))
            full_bars.add(bar)
            full_people.add(person)
            full_checks.add(check)
        # This is the equation line, not a staircase around the individual bars.
        full_profile = Line([Q_ZERO, -0.045, ROW_BASE + 2 * ROW_DOLLAR_HEIGHT],
                            [Q_ZERO + 100 * Q_STEP, -0.045, ROW_BASE + 7 * ROW_DOLLAR_HEIGHT],
                            color=SUPPLY, stroke_width=2.6)
        equation = Tex(r'$P=2+Q_s/20$', color=SUPPLY).scale(0.67)
        equation.face_mat = np.eye(3)
        equation.add_updater(face_camera)
        equation.update()
        equation.move_to([4.7, 0, 4.65])
        price_guide = DashedLine([Q_ZERO, -0.045, ROW_BASE + 3 * ROW_DOLLAR_HEIGHT],
                                [Q_ZERO + 20 * Q_STEP, -0.045, ROW_BASE + 3 * ROW_DOLLAR_HEIGHT],
                                color=GUIDE, stroke_width=2.2)
        price_guide.price, price_guide.x0, price_guide.dx = price, Q_ZERO, Q_STEP
        price_guide.base, price_guide.dollar_height = ROW_BASE, ROW_DOLLAR_HEIGHT
        price_guide.add_updater(lambda m: set_dashed_endpoints(m,
            np.array([m.x0, -0.045, m.base + m.price.get_value() * m.dollar_height]),
            np.array([m.x0 + (20 * (m.price.get_value() - 2)) * m.dx, -0.045, m.base + m.price.get_value() * m.dollar_height])))
        # The dollar amount follows the left end of the guide in world space.
        price_number = DecimalNumber(3, num_decimal_places=2, color=GUIDE).scale(0.57)
        price_number.tracker, price_number.anchor = price, price_guide
        price_number.face_mat = np.eye(3)
        price_number.add_updater(face_camera)
        price_number.add_updater(lambda m: m.move_to(m.anchor.get_start() + LEFT * 0.12, aligned_edge=RIGHT))
        price_word = Tex(r'\$', color=GUIDE).scale(0.57)
        price_word.anchor, price_word.face_mat = price_number, np.eye(3)
        price_word.add_updater(face_camera)
        price_word.add_updater(lambda m: m.next_to(m.anchor, LEFT, buff=0.03))
        price_units = Tex('/lb', color=CAPTION).scale(0.34)
        price_units.anchor, price_units.face_mat = price_number, np.eye(3)
        price_units.add_updater(face_camera)
        price_units.add_updater(lambda m: m.move_to(m.anchor.get_center() + LEFT * 0.12 + IN * 0.24))
        price_readout = VGroup(price_number, price_word, price_units)
        price_readout.update()
        quantity_tracker = ValueTracker(20)
        quantity_tracker.price, quantity_tracker.values = price, values
        quantity_tracker.add_updater(lambda m: m.set_value(int(np.count_nonzero(m.values <= m.price.get_value() + 1e-7))))
        self.add(quantity_tracker)
        quantity_number = Integer(20, color=SUPPLY).scale(0.70)
        quantity_number.tracker = quantity_tracker
        # Bare quantity number, directly below the curve's current intersection.
        quantity_number.anchor, quantity_number.face_mat = price_guide, np.eye(3)
        quantity_number.add_updater(face_camera)
        quantity_number.add_updater(lambda m: m.move_to([m.anchor.get_end()[0], 0, -0.70]))
        quantity_readout = VGroup(quantity_number)
        self.add(head)
        self.play(FadeIn(full_bars), FadeIn(full_people), FadeIn(one_lot), run_time=1.0)
        self.play(Create(full_profile), FadeIn(equation), run_time=0.8)
        self.play(Create(price_guide), FadeIn(price_readout), FadeIn(quantity_readout),
                  show_willing.animate.set_value(1), FadeIn(full_checks), run_time=0.7)
        rule = fixed(Tex(r'$MC\leq P$: willing to sell. At $\$3$, 20 sellers are willing.', color=INK))
        rule.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(ReplacementTransform(one_lot, rule))
        self.pause('1.c.sellers')
        self.play(price.animate.set_value(6), run_time=2.0, rate_func=smooth)
        high = fixed(Tex(r'At $\$6$, 80 sellers are willing. A higher price brings more sellers.', color=INK))
        high.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(ReplacementTransform(rule, high))
        self.pause('1.c.sellers.high')
        self.play(FadeOut(high), price.animate.set_value(3), run_time=1.3, rate_func=smooth)

        # ========== 6. Equilibrium ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15
        self.camera.frame.set_height(8)


        # One person is one 1,000-lb lot. Bar height is dollars per pound.
        BUYER_MB = np.array([12 - n / 5 for n in range(1, 60)])
        SELLER_MC = np.array([2 + n / 20 for n in range(1, 101)])
        EPS = 1e-7
        DOLLAR_HEIGHT = 0.035
        price = ValueTracker(3)
        show_counts = ValueTracker(1)
        # Given a price, its graph quantities remain visible before plaza matching.
        show_graph_counts = ValueTracker(1)
        show_trades = ValueTracker(1)
        show_buyers = ValueTracker(1)
        show_sellers = ValueTracker(1)
        self.add(price, show_counts, show_graph_counts, show_trades, show_buyers, show_sellers)

        # B3's camera: buyers occupy the upper half, sellers the lower half.
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(PLAZA_CENTER).set_height(11)
        BAR_BASE, DOLLAR_HEIGHT = 0.17, 0.035
        ARC_RADIUS, STEP_IN = 4.35, 0.82
        PAIR_LEFT, PAIR_STEP, PAIR_OFFSET = -3.35, 6.7 / 39, 0.40
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        buyer_people, buyer_bars, buyer_checks, buyer_circles = Group(), Group(), VGroup(), VGroup()
        seller_people, seller_bars, seller_checks, seller_circles = Group(), Group(), VGroup(), VGroup()
        buyer_crosses, seller_crosses = VGroup(), VGroup()
        buyer_positions, seller_positions = [], []
        for side, values, color, people, bars, checks, crosses, circles, positions, visibility in [
                ('B', BUYER_MB, DEMAND, buyer_people, buyer_bars, buyer_checks, buyer_crosses,
                 buyer_circles, buyer_positions, show_buyers),
                ('S', SELLER_MC, SUPPLY, seller_people, seller_bars, seller_checks, seller_crosses,
                 seller_circles, seller_positions, show_sellers)]:
            for n, value in enumerate(values):
                angle = (-55 + 110 * n / (len(values) - 1)) * DEGREES
                x = ARC_RADIUS * np.sin(angle)
                y = (1 if side == 'B' else -1) * ARC_RADIUS * np.cos(angle)
                positions.append(np.array([x, y, 0.045]))
                shadow = Disk3D(radius=0.044, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28)
                shadow.set_color(color).move_to([x, y, 0.025])
                orb = Sphere(radius=0.034, color=color, resolution=(12, 8)).move_to([x, y, 0.064])
                person = Group(shadow, orb)
                bar = Rectangle3D(width=0.055, height=value * DOLLAR_HEIGHT,
                                  resolution=(2, 2), opacity=0.65).set_color(color)
                bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
                check = (VMobject(color=GOV, stroke_width=1.6).set_points_as_corners(
                    [[-0.022, 0, 0], [-0.006, -0.017, 0], [0.025, 0.025, 0]]))
                cross = (VGroup(
                    Line([-0.019, -0.019, 0], [0.019, 0.019, 0], color=GUIDE, stroke_width=1.2),
                    Line([-0.019, 0.019, 0], [0.019, -0.019, 0], color=GUIDE, stroke_width=1.2))).set_color(GUIDE)
                for mark, accepted in [(check, True), (cross, False)]:
                    mark.price, mark.value, mark.visibility, mark.side = price, value, visibility, side
                    mark.anchor, mark.dollar_height, mark.accepted = bar, DOLLAR_HEIGHT, accepted
                    mark.scale(self.camera.frame.get_scale())
                    mark.face_mat = np.eye(3)
                    mark.add_updater(face_camera)
                    mark.add_updater(lambda m: m.move_to(
                        m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.085))
                        .set_stroke(opacity=m.visibility.get_value() * (1 if m.accepted else 0.65) * float(
                            (m.value + 1e-7 >= m.price.get_value() if m.side == 'B' else m.value <= m.price.get_value() + 1e-7) == m.accepted))
                        .set_fill(opacity=0))
                # Invisible anchors retain the existing deliberation endpoints.
                circle = Circle(radius=0.035, color=GOV, stroke_width=0).move_to([x, y, 0.045])
                circle.set_stroke(opacity=0).set_fill(opacity=0)
                for mob in [person, bar, circle]:
                    mob.rim = mob.get_center().copy()
                    mob.home = np.array([x * STEP_IN, y * STEP_IN, mob.rim[2]])
                    mob.pair_home = np.array([PAIR_LEFT + n * PAIR_STEP, (PAIR_OFFSET if side == 'B' else -PAIR_OFFSET), mob.rim[2]])
                    mob.home_width = mob.paired_width = mob.get_width()
                    mob.price, mob.rank, mob.visibility = price, n + 1, show_trades
                    mob.mb, mob.mc = BUYER_MB, SELLER_MC
                    mob.side, mob.value, mob.willingness = side, value, visibility
                    mob.pair_step, mob.pair_offset = PAIR_STEP, (PAIR_OFFSET if side == 'B' else -PAIR_OFFSET)
                    mob.add_updater(lambda m: setattr(m, 'pair_home', np.array([
                        (m.rank - 1 - (min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()),
                                          np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)) - 1) / 2)
                        * m.pair_step, m.pair_offset, m.home[2]])))
                    mob.add_updater(lambda m: setattr(m, 'willing_fraction', m.willingness.get_value() * float(
                        m.value + 1e-7 >= m.price.get_value() if m.side == 'B' else m.value <= m.price.get_value() + 1e-7)))
                    mob.add_updater(lambda m: setattr(m, 'pair_fraction', m.visibility.get_value() * float(
                        m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()),
                                      np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))))
                    mob.add_updater(lambda m: m.move_to(
                        (m.rim + m.willing_fraction * (m.home - m.rim)) * (1 - m.pair_fraction)
                        + m.pair_home * m.pair_fraction))
                people.add(person)
                bars.add(bar)
                checks.add(check)
                crosses.add(cross)
                circles.add(circle)
        # B3 world text: labels belong to the plaza and face the moving camera.
        buyer_label = Tex('Buyers', color=DEMAND).scale(0.82).move_to([0, 4.65, 0.45])
        seller_label = Tex('Sellers', color=SUPPLY).scale(0.82).move_to([0, -5.25, 0.04])
        units = Tex('One person = 1,000 lb', color=CAPTION).scale(0.65).move_to([0, -5.95, 0.04])
        for label in [buyer_label, seller_label, units]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        buyers = Group(buyer_bars, buyer_people, buyer_circles)
        sellers = Group(seller_bars, seller_people, seller_circles)
        crowd = Group(floor, rim, buyers, sellers, buyer_label, seller_label, units)
        crowd_marks = VGroup(buyer_checks, seller_checks, buyer_crosses, seller_crosses)

        # Both graphs share their own price scale, independent of the 3D totem.
        graph_price_height = 2.0
        demand_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=graph_price_height)
        supply_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=graph_price_height)
        demand_axes.shift(np.array([1.90, 0.80, 0]) - demand_axes.c2p(0, 0))
        supply_axes.shift(np.array([1.90, -1.84, 0]) - supply_axes.c2p(0, 0))
        ticks = VGroup()
        demand_ticks, supply_ticks = VGroup(), VGroup()
        for ax, side_ticks in [(demand_axes, demand_ticks), (supply_axes, supply_ticks)]:
            for q in [0, 20, 40, 60, 80, 100]:
                tick = fixed(Tex(str(q), color=CAPTION)).scale(0.38).next_to(ax.c2p(q, 0), DOWN, buff=0.10)
                tick.quantity, tick.price, tick.visibility = q, price, show_graph_counts
                tick.values, tick.side = (BUYER_MB, 'buyer') if ax is demand_axes else (SELLER_MC, 'seller')
                tick.add_updater(lambda m: m.set_opacity(1 - m.visibility.get_value() * float(abs(
                    m.quantity - (np.count_nonzero(m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else
                                  np.count_nonzero(m.values <= m.price.get_value() + 1e-7))) < 7)))
                side_ticks.add(tick)
            for p in [4, 8, 12]:
                side_ticks.add(fixed(Tex(str(p), color=CAPTION)).scale(0.35).next_to(ax.c2p(0, p), LEFT, buff=0.10))
            ticks.add(side_ticks)
        # One narrow bar per lot. The two colors occupy adjacent slots when overlaid.
        demand_lot_bars, supply_lot_bars = VGroup(), VGroup()
        for ax, values, color, left, right, lot_bars in [
                (demand_axes, BUYER_MB, DEMAND, 0.12, 0.45, demand_lot_bars),
                (supply_axes, SELLER_MC, SUPPLY, 0.55, 0.88, supply_lot_bars)]:
            for n, value in enumerate(values):
                lot_bars.add(Polygon(ax.c2p(n + left, 0), ax.c2p(n + right, 0),
                    ax.c2p(n + right, value), ax.c2p(n + left, value),
                    stroke_width=0, fill_color=color, fill_opacity=0.50))
        demand_steps = Line(demand_axes.c2p(0, 12), demand_axes.c2p(60, 0), color=DEMAND, stroke_width=2.4)
        supply_steps = Line(supply_axes.c2p(0, 2), supply_axes.c2p(100, 7), color=SUPPLY, stroke_width=2.4)
        demand_fit = Line(demand_axes.c2p(0, 12), demand_axes.c2p(60, 0), color=DEMAND).set_opacity(0)
        supply_fit = Line(supply_axes.c2p(0, 2), supply_axes.c2p(100, 7), color=SUPPLY).set_opacity(0)
        demand_word = fixed(Tex(r'Demand: $P=12-Q_d/5$', color=DEMAND)).scale(0.59).move_to([4.45, 2.85, 0])
        supply_word = fixed(Tex(r'Supply: $P=2+Q_s/20$', color=SUPPLY)).scale(0.59).move_to([4.45, 0.18, 0])
        graph_units = fixed(Tex(r'$Q$: thousands of pounds', color=CAPTION)).scale(0.48).move_to([4.5, -2.25, 0])
        graph_prices = VGroup()
        for ax, values, side in [(demand_axes, BUYER_MB, 'buyer'), (supply_axes, SELLER_MC, 'seller')]:
            quantity = np.count_nonzero(values + EPS >= price.get_value()) if side == 'buyer' else np.count_nonzero(values <= price.get_value() + EPS)
            line = DashedLine(ax.c2p(0, price.get_value()), ax.c2p(quantity, price.get_value()), color=GUIDE, stroke_width=2.3)
            line.axes, line.price, line.values, line.side = ax, price, values, side
            line.add_updater(lambda m: set_dashed_endpoints(m, m.axes.c2p(0, m.price.get_value()), m.axes.c2p(max(0, min(100, 60 - 5 * m.price.get_value() if m.side == 'buyer' else 20 * (m.price.get_value() - 2))), m.price.get_value())))
            graph_prices.add(line)
        demand_guide = Line(demand_axes.c2p(45, 0), demand_axes.c2p(45, 3), color=DEMAND, stroke_width=2)
        demand_guide.axes, demand_guide.price, demand_guide.values, demand_guide.visibility = demand_axes, price, BUYER_MB, show_graph_counts
        demand_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), 0), m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), m.price.get_value())).set_opacity(m.visibility.get_value()))
        supply_guide = Line(supply_axes.c2p(20, 0), supply_axes.c2p(20, 3), color=SUPPLY, stroke_width=2)
        supply_guide.axes, supply_guide.price, supply_guide.values, supply_guide.visibility = supply_axes, price, SELLER_MC, show_graph_counts
        supply_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), 0), m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), m.price.get_value())).set_opacity(m.visibility.get_value()))
        # Each bare count sits at its quantity-axis position, in its curve's color.
        counts = VGroup()
        for ax, values, side, color in [(demand_axes, BUYER_MB, 'buyer', DEMAND),
                                         (supply_axes, SELLER_MC, 'seller', SUPPLY)]:
            number = fixed(Integer(0, color=color)).scale(0.50)
            number.axes, number.price, number.values = ax, price, values
            number.side, number.visibility = side, show_graph_counts
            number.add_updater(lambda m: m.set_value(int(np.count_nonzero(
                m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else
                np.count_nonzero(m.values <= m.price.get_value() + 1e-7)))
                .next_to(m.axes.c2p(m.get_value(), 0), DOWN, buff=0.10)
                .set_opacity(m.visibility.get_value()))
            counts.add(number)
        # The posted price is a height on the totem at the right end of the divider.
        TOTEM_X, TOTEM_BASE, TOTEM_DOLLAR_HEIGHT = 4.8, 0.035, 0.28
        plaza_divider = DashedLine([-4.8, 0, TOTEM_BASE], [4.8, 0, TOTEM_BASE],
                                  color=MUTED, stroke_width=2, dash_length=0.14)
        plaza_divider.put_start_and_end_on(np.array([-4.8, 0, TOTEM_BASE]), np.array([4.8, 0, TOTEM_BASE]))
        plaza_divider.set_stroke(opacity=0.8).set_flat_stroke(False)
        price_post = Line([TOTEM_X, 0, TOTEM_BASE], [TOTEM_X, 0, TOTEM_BASE + 12 * TOTEM_DOLLAR_HEIGHT],
                          color=CAPTION, stroke_width=3).set_flat_stroke(False)
        post_foot = Disk3D(radius=0.10, resolution=(2, 24), shading=(0, 0, 0), opacity=0.5)
        post_foot.set_color(MUTED).move_to([TOTEM_X, 0, TOTEM_BASE])
        post_ticks, post_numbers = VGroup(), VGroup()
        for level in range(0, 13, 2):
            z = TOTEM_BASE + level * TOTEM_DOLLAR_HEIGHT
            post_ticks.add(Line([TOTEM_X - 0.09, 0, z], [TOTEM_X + 0.09, 0, z],
                                color=MUTED, stroke_width=1.5).set_flat_stroke(False))
            if level in [0, 4, 8, 12]:
                number = Tex(str(level), color=CAPTION).scale(0.50)
                number.face_mat = np.eye(3)
                number.add_updater(face_camera)
                number.update()
                number.move_to([TOTEM_X - 0.20, -0.025, z], aligned_edge=RIGHT)
                post_numbers.add(number)
        price_marker = Line([TOTEM_X - 0.16, -0.025, TOTEM_BASE + price.get_value() * TOTEM_DOLLAR_HEIGHT],
                            [TOTEM_X + 0.16, -0.025, TOTEM_BASE + price.get_value() * TOTEM_DOLLAR_HEIGHT],
                            color=GUIDE, stroke_width=5).set_flat_stroke(False)
        price_marker.price, price_marker.base, price_marker.dollar_height = price, TOTEM_BASE, TOTEM_DOLLAR_HEIGHT
        price_marker.add_updater(lambda m: m.set_z(m.base + m.price.get_value() * m.dollar_height))
        price_heading = Tex(r'Price (\$/lb)', color=CAPTION).scale(0.63)
        price_heading.move_to([TOTEM_X, 0, TOTEM_BASE + 12 * TOTEM_DOLLAR_HEIGHT + 0.45])
        price_word = Tex(r'\$', color=GUIDE).scale(0.78)
        price_number = DecimalNumber(price.get_value(), num_decimal_places=2, color=GUIDE).scale(0.78)
        price_number.tracker = price
        for label in [price_heading, price_word, price_number]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
        price_word.anchor = price_marker
        price_word.add_updater(lambda m: m.move_to(m.anchor.get_end() + RIGHT * 0.15, aligned_edge=LEFT))
        price_number.anchor = price_word
        price_number.add_updater(lambda m: m.next_to(m.anchor, RIGHT, buff=0.06))
        current_price = VGroup(price_word, price_number)
        price_readout = VGroup(post_numbers, price_heading, current_price)
        price_readout.update()
        crowd.add(plaza_divider, post_foot, price_post, post_ticks, price_marker, price_readout)
        graphs = VGroup(demand_axes, supply_axes, ticks, demand_fit, supply_fit, demand_lot_bars, supply_lot_bars, demand_steps, supply_steps,
                        demand_word, supply_word, graph_prices, demand_guide, supply_guide, graph_units, counts)
        fixed(graphs)
        # World and fixed overlay objects are added separately, as in B3.

        # One short quantity segment follows each counted person on the ground.
        gap_count = ValueTracker(25)
        gap_count.price, gap_count.mb, gap_count.mc = price, BUYER_MB, SELLER_MC
        gap_count.add_updater(lambda m: m.set_value(abs(
            np.count_nonzero(m.mb + 1e-7 >= m.price.get_value())
            - np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))))
        self.add(gap_count)
        buyer_quantity = VGroup(*[Line(LEFT * 0.03, RIGHT * 0.03, color=DEMAND, stroke_width=3)
                                 for _ in buyer_circles])
        seller_quantity = VGroup(*[Line(LEFT * 0.03, RIGHT * 0.03, color=SUPPLY, stroke_width=3)
                                  for _ in seller_circles])
        waiting_gap = VGroup(*[VGroup(*[
            Line(LEFT * 0.03, RIGHT * 0.03, color=FOCUS, stroke_width=4) for _ in people])
            for people in [buyer_circles, seller_circles]])
        for line in [*buyer_quantity, *seller_quantity, *waiting_gap[0], *waiting_gap[1]]:
            line.set_flat_stroke(False)
        plaza_shortage = Tex('Shortage', color=FOCUS).scale(0.58)
        plaza_excess = Tex('Excess', color=FOCUS).scale(0.58)
        plaza_gap_number = Integer(25, color=FOCUS).scale(0.58)
        plaza_gap_number.tracker = gap_count
        for label in [plaza_shortage, plaza_excess, plaza_gap_number]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        plaza_quantities = VGroup(buyer_quantity, seller_quantity, waiting_gap,
                                  plaza_shortage, plaza_excess, plaza_gap_number)
        plaza_quantities.price, plaza_quantities.mb, plaza_quantities.mc = price, BUYER_MB, SELLER_MC
        plaza_quantities.buyers, plaza_quantities.sellers = buyer_circles, seller_circles
        plaza_quantities.counts, plaza_quantities.trades = show_counts, show_trades

        def update_plaza_quantities(m):
            qd = int(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()))
            qs = int(np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))
            excess_side = 1 if qd > qs else -1
            mark_waiting = qd != qs and m.trades.get_value() > 0.999
            waiting_by_side = []
            for segments, gap_segments, people, quantity, side in [
                    (m[0], m[2][0], m.buyers, qd, 1), (m[1], m[2][1], m.sellers, qs, -1)]:
                waiting = []
                for n, (segment, gap_segment, person) in enumerate(zip(segments, gap_segments, people)):
                    point = person.get_center()
                    center = point + np.array([0, -side * 0.18, 0.015])
                    gap_center = point + np.array([0, -side * 0.38, 0.02])
                    willing = n < quantity
                    unmatched = abs(point[1]) >= 1
                    # Endpoints belong to this actor only: relocation cannot
                    # create a diagonal bridge to another person's segment.
                    segment.set_points_as_corners([center + LEFT * 0.03, center + RIGHT * 0.03])
                    segment.set_stroke(opacity=m.counts.get_value() if willing else 0)
                    gap_segment.set_points_as_corners([gap_center + LEFT * 0.03, gap_center + RIGHT * 0.03])
                    gap_segment.set_stroke(opacity=m.counts.get_value()
                        if willing and unmatched and mark_waiting and side == excess_side else 0)
                    if willing and unmatched:
                        waiting.append(gap_center)
                waiting.sort(key=lambda p: p[0])
                waiting_by_side.append(waiting)
            waiting = waiting_by_side[0 if excess_side == 1 else 1]
            visible = m.counts.get_value() if mark_waiting and waiting else 0
            if waiting:
                middle = waiting[len(waiting) // 2]
                m[5].move_to(middle + np.array([0.55, -excess_side * 0.48, 0.12]))
                m[3].next_to(m[5], LEFT, buff=0.10)
                m[4].next_to(m[5], LEFT, buff=0.10)
            m[3].set_opacity(visible if excess_side == 1 else 0)
            m[4].set_opacity(visible if excess_side == -1 else 0)
            m[5].set_opacity(visible)

        plaza_quantities.add_updater(update_plaza_quantities)
        # Last in the crowd: its lines follow the updated actor positions.
        crowd.add(plaza_quantities)
        demand_span = Line(demand_axes.c2p(0, 0), demand_axes.c2p(45, 0), color=DEMAND, stroke_width=4)
        supply_span = Line(supply_axes.c2p(0, 0), supply_axes.c2p(20, 0), color=SUPPLY, stroke_width=4)
        graph_gap = VMobject(color=FOCUS, stroke_width=3)
        graph_shortage = Tex('Shortage', color=FOCUS).scale(0.40)
        graph_excess = Tex('Excess', color=FOCUS).scale(0.40)
        graph_gap_number = Integer(25, color=FOCUS).scale(0.40)
        graph_gap_number.tracker = gap_count
        graph_gap_number.add_updater(lambda m: m.set_value(int(m.tracker.get_value())))
        graph_quantities = fixed(VGroup(demand_span, supply_span, graph_gap,
                                       graph_shortage, graph_excess, graph_gap_number))
        graph_quantities.price, graph_quantities.mb, graph_quantities.mc = price, BUYER_MB, SELLER_MC
        graph_quantities.demand, graph_quantities.supply = demand_axes, supply_axes
        graph_quantities.counts, graph_quantities.trades = show_graph_counts, show_trades

        def update_graph_quantities(m):
            qd = int(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()))
            qs = int(np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))
            for line, ax, quantity in [(m[0], m.demand, qd), (m[1], m.supply, qs)]:
                line.set_points_as_corners([ax.c2p(0, 0), ax.c2p(quantity, 0)])
                line.set_stroke(opacity=m.counts.get_value())
            ax = m.demand if qd > qs else m.supply
            start = ax.c2p(min(qd, qs), 0) + UP * 0.18
            end = ax.c2p(max(qd, qs), 0) + UP * 0.18
            m[2].set_points_as_corners([start + DOWN * 0.06, start, end, end + DOWN * 0.06])
            visible = m.counts.get_value() if qd != qs and m.trades.get_value() > 0.999 else 0
            m[2].set_stroke(opacity=visible)
            m[5].move_to((start + end) / 2 + np.array([0.35, 0.23, 0]))
            m[3].next_to(m[5], LEFT, buff=0.07).set_opacity(visible if qd > qs else 0)
            m[4].next_to(m[5], LEFT, buff=0.07).set_opacity(visible if qs > qd else 0)
            m[5].set_opacity(visible)

        graph_quantities.add_updater(update_graph_quantities)
        graphs.add(graph_quantities)

        # ---- 1.c / 1.d · Off-equilibrium first. No $4 answer has appeared.
        show_counts.set_value(0)
        show_trades.set_value(0)
        show_buyers.set_value(0)
        show_sellers.set_value(0)
        head = fixed(title(r'A low price: $\$3$'))
        low_question = fixed(Tex('Who can trade?', color=DEFINITION).scale(DEFINITION_SCALE)
                             .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(head, crowd, crowd_marks, graphs, low_question)
        self.pause('1.d')

        # ---- 1.e · Willingness first, matching second.
        self.play(FadeOut(low_question), show_counts.animate.set_value(1), show_buyers.animate.set_value(1),
                  show_sellers.animate.set_value(1), run_time=0.8)
        # Keep quantity lines through matching; yellow marks the unserved remainder.
        self.play(show_trades.animate.set_value(1), run_time=1.1)
        shortage = fixed(Tex(r'20 pairs trade. 25 willing buyers are still waiting.', color=INK))
        shortage.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(shortage))
        unserved = VGroup()  # The checked buyers on the inner arc are the unserved group.
        self.pause('1.e')

        # ---- 1.j · The class tackles incentives BEFORE equilibrium resolves.
        # B2/B3 exercise reference: one rounded panel, gold heading, indented serif body.
        cover = fixed(Rectangle(width=16, height=8, stroke_width=0, fill_color=BG, fill_opacity=1))
        card_text = fixed(VGroup(
            Tex('Exercise B3 $|$ Q2', color=DEFINITION).scale(1.2),
            Tex(r'$P=12-\frac{Q_d}{2}\qquad\qquad P=2+\frac{Q_s}{2}$', color=INK).scale(0.95),
            Tex('Pumpkin pasties at a price of 5 galleons.', color=INK).scale(0.95),
            Tex('Find quantity demanded and quantity supplied.', color=INK).scale(0.95),
            Tex('Shortage or excess? How much?', color=INK).scale(0.95),
            Tex('Which way will price move?', color=INK).scale(0.95))
            .arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(ORIGIN))
        card_panel = fixed(RoundedRectangle(width=13, height=card_text.get_height() + 1.2,
            corner_radius=0.25, color=MUTED, stroke_width=2,
            fill_color=BG, fill_opacity=1).move_to(card_text))
        card_text.align_to(card_panel, LEFT).shift(RIGHT * 0.65)
        card_text[1].set_x(card_panel.get_x())
        for paragraph in card_text[2:]:
            paragraph.shift(RIGHT * 0.35)
        card_panel.set_z_index(50)
        for glyph in card_text.get_family():
            glyph.set_z_index(51)
        exercise = fixed(VGroup(cover, card_panel, card_text))
        self.play(FadeIn(exercise))
        self.pause('1.j')
        self.play(FadeOut(exercise), FadeOut(unserved), FadeOut(shortage))

        # ---- 1.f · Amanda-Grace compares waiting with an actual alternative.
        buyer_question = fixed(Tex('What would this buyer do?', color=DEFINITION).scale(DEFINITION_SCALE)
                               .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        ag_focus = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(buyer_circles[24].get_center())
        bid = DashedLine(buyer_circles[24].get_center(), seller_circles[19].get_center(), color=GUIDE, stroke_width=2)
        seller_gain = fixed(Tex(r'Seller receives $\$0.25$ more per lb', color=SUPPLY)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(Create(ag_focus), Create(bid), FadeOut(units), FadeIn(seller_gain))

        self.play(FadeOut(ag_focus), FadeOut(bid), FadeOut(seller_gain))

        # Three people, their own values, and two visible trading alternatives.
        buy_person = buyer_people[24].copy().clear_updaters()
        buy_counterparty = seller_people[19].copy().clear_updaters()
        buy_incumbent = buyer_people[19].copy().clear_updaters()
        buy_mb = buyer_bars[24].copy().clear_updaters()
        buy_mc = seller_bars[19].copy().clear_updaters()
        buy_incumbent_bar = buyer_bars[19].copy().clear_updaters()
        buy_detail = Group(buy_person, buy_counterparty, buy_incumbent, buy_mb, buy_mc, buy_incumbent_bar)
        self.add(buy_detail)
        buy_targets = []
        for x, color in [(-2.6, DEMAND), (0, SUPPLY), (2.6, DEMAND)]:
            shadow = Disk3D(radius=0.28, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(12, 8)).move_to([x, 0, 0.32])
            buy_targets.append(Group(shadow, orb))
        buy_mb_target = Rectangle3D(width=0.8, height=7 * 0.48, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        buy_mb_target.rotate(90 * DEGREES, RIGHT).move_to([-1.75, 0, 0.75 + 7 * 0.48 / 2])
        buy_mc_target = Rectangle3D(width=0.8, height=3 * 0.48, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        buy_mc_target.rotate(90 * DEGREES, RIGHT).move_to([0.85, 0, 0.75 + 3 * 0.48 / 2])
        buy_incumbent_bar_target = Rectangle3D(width=0.8, height=8 * 0.48, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        buy_incumbent_bar_target.rotate(90 * DEGREES, RIGHT).move_to([1.75, 0, 0.75 + 8 * 0.48 / 2])
        crowd.suspend_updating()
        crowd_marks.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(graphs),
                  Transform(buy_person, buy_targets[0]),
                  Transform(buy_counterparty, buy_targets[1]),
                  Transform(buy_incumbent, buy_targets[2]),
                  Transform(buy_mb, buy_mb_target),
                  Transform(buy_mc, buy_mc_target),
                  Transform(buy_incumbent_bar, buy_incumbent_bar_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        buy_ring = Circle(radius=0.31, color=FOCUS, stroke_width=2.5)
        buy_ring.rotate(90 * DEGREES, RIGHT).move_to([-2.6, -0.04, 0.32]).set_flat_stroke(False)
        buy_zero = VGroup(*[Line([x - 0.52, -0.02, 0.75], [x + 0.52, -0.02, 0.75],
            color=MUTED, stroke_width=1.5) for x in [-1.75, 0.85, 1.75]])
        buy_price = Line([0.45, -0.045, 0.75 + 3 * 0.48], [2.15, -0.045, 0.75 + 3 * 0.48], color=GUIDE, stroke_width=3)
        buy_proposal = DashedLine([-2.15, -0.055, 0.75 + 3.25 * 0.48], [1.25, -0.055, 0.75 + 3.25 * 0.48], color=GUIDE, stroke_width=3)
        buy_values = VGroup()
        for text, color, at, edge in [
                (r'MB $\$7$', DEMAND, [-2.33, 0, 4.11], RIGHT),
                (r'MC $\$3$', SUPPLY, [0.28, 0, 2.19], RIGHT),
                (r'MB $\$8$', DEMAND, [1.75, 0, 4.84], ORIGIN)]:
            label = Tex(text, color=color).scale(0.56)
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
            buy_values.add(label)
        stay_text = Tex(r'Wait at $\$3$: gain $\$0$', color=CAPTION).scale(0.60)
        offer_text = Tex(r'Offer $\$3.25$\\Gain $\$3.75$/lb', color=INK).scale(0.62)
        for label, at, edge in [(stay_text, [3.05, -0.07, 1.55], LEFT),
                                (offer_text, [-3.05, -0.07, 2.95], RIGHT)]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
        wait_arrow = Arrow([2.85, 1.55, 0], [2.15, 0.75 + 3 * 0.48, 0],
                           buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        offer_arrow = Arrow([-2.85, 2.95, 0], [-2.15, 0.75 + 3.25 * 0.48, 0],
                            buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        for arrow in [wait_arrow, offer_arrow]:
            arrow.rotate(90 * DEGREES, RIGHT, about_point=ORIGIN).shift(DOWN * 0.07)
        self.play(Create(buy_ring), Create(buy_zero), Create(buy_price),
                  Create(buy_proposal), FadeIn(buy_values), FadeIn(stay_text), FadeIn(offer_text),
                  Create(wait_arrow), Create(offer_arrow), FadeIn(buyer_question))
        self.pause('1.f')
        self.play(buy_price.animate.put_start_and_end_on(
                      np.array([-2.15, -0.045, 0.75 + 3.25 * 0.48]), np.array([-0.45, -0.045, 0.75 + 3.25 * 0.48])),
                  buy_mc.animate.shift(LEFT * 1.7), buy_zero[1].animate.shift(LEFT * 1.7),
                  buy_values[1].animate.move_to([-0.28, 0, 0.75 + 3 * 0.48], aligned_edge=LEFT),
                  buy_incumbent.animate.shift(RIGHT * 0.65),
                  buy_incumbent_bar.animate.shift(RIGHT * 0.65),
                  buy_zero[2].animate.shift(RIGHT * 0.65), buy_values[2].animate.shift(RIGHT * 0.65),
                  FadeOut(buyer_question), FadeOut(buy_proposal), FadeOut(stay_text), FadeOut(wait_arrow),
                  FadeOut(offer_arrow), offer_text.animate.set_color(GOV), run_time=0.9, rate_func=smooth)
        adjustment_head = fixed(title('Price adjustment'))
        self.remove(head)
        self.play(FadeOut(buy_detail), FadeOut(buy_zero), FadeOut(buy_price), FadeOut(buy_values),
                  FadeOut(offer_text), FadeOut(buy_ring), FadeIn(adjustment_head),
                  self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.3)
        head = adjustment_head
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_marks.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_marks, graphs)
        self.remove(units)
        # The three-person close-up has shown the switch. Keep every original
        # crowd member in its ranked snapshot and compress the common response.
        everyone = fixed(Tex('Other unserved buyers have the same incentive.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(everyone), run_time=0.3)
        self.add(units)
        tried_low = VGroup(*[DashedLine(ax.c2p(0, 3), ax.c2p(q, 3), color=GUIDE, stroke_width=1).set_opacity(0.25) for ax, q in [(demand_axes, 45), (supply_axes, 20)]])
        fixed(tried_low)
        self.add(tried_low)
        self.play(price.animate.set_value(4), run_time=3.0, rate_func=smooth)
        rising = fixed(Tex(r'Shortage $\longrightarrow$ price rises. The counts meet.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(ReplacementTransform(everyone, rising))

        # ---- 1.g · Predict the other direction before revealing its counts.
        self.play(FadeOut(rising), show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0), show_sellers.animate.set_value(0))
        self.play(price.animate.set_value(6), run_time=1.0)
        high_head = fixed(title(r'A high price: $\$6$'))
        high_question = fixed(Tex('Who is left out?', color=DEFINITION).scale(DEFINITION_SCALE)
                              .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(head)
        self.play(FadeIn(high_head), FadeIn(high_question))
        head = high_head
        self.pause('1.g')

        # ---- 1.h · Andrew can attract a buyer by asking less.
        self.play(FadeOut(high_question), show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1))
        excess = fixed(Tex(r'Excess: 50,000 lb. This seller is willing, but has no buyer.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(units)
        andrew_focus = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(seller_circles[39].get_center())
        cut = DashedLine(seller_circles[39].get_center(), buyer_circles[29].get_center(), color=GUIDE, stroke_width=2)
        self.play(FadeIn(excess), Create(andrew_focus), Create(cut))

        seller_question = fixed(Tex('What would this seller do?', color=DEFINITION).scale(DEFINITION_SCALE)
                                .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(andrew_focus), FadeOut(cut), FadeOut(tried_low))

        # Three people, their own values, and two visible trading alternatives.
        sell_incumbent = seller_people[29].copy().clear_updaters()
        sell_person = buyer_people[29].copy().clear_updaters()
        sell_counterparty = seller_people[39].copy().clear_updaters()
        sell_incumbent_bar = seller_bars[29].copy().clear_updaters()
        sell_mb = buyer_bars[29].copy().clear_updaters()
        sell_mc = seller_bars[39].copy().clear_updaters()
        sell_detail = Group(sell_incumbent, sell_person, sell_counterparty, sell_incumbent_bar, sell_mb, sell_mc)
        self.add(sell_detail)
        sell_targets = []
        for x, color in [(-2.6, SUPPLY), (0, DEMAND), (2.6, SUPPLY)]:
            shadow = Disk3D(radius=0.28, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(12, 8)).move_to([x, 0, 0.32])
            sell_targets.append(Group(shadow, orb))
        sell_incumbent_bar_target = Rectangle3D(width=0.8, height=3.5 * 0.55, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        sell_incumbent_bar_target.rotate(90 * DEGREES, RIGHT).move_to([-1.75, 0, 0.75 + 3.5 * 0.55 / 2])
        sell_mb_target = Rectangle3D(width=0.8, height=6 * 0.55, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        sell_mb_target.rotate(90 * DEGREES, RIGHT).move_to([-0.85, 0, 0.75 + 6 * 0.55 / 2])
        sell_mc_target = Rectangle3D(width=0.8, height=4 * 0.55, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        sell_mc_target.rotate(90 * DEGREES, RIGHT).move_to([1.75, 0, 0.75 + 4 * 0.55 / 2])
        crowd.suspend_updating()
        crowd_marks.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(graphs), FadeOut(excess),
                  Transform(sell_incumbent, sell_targets[0]),
                  Transform(sell_person, sell_targets[1]),
                  Transform(sell_counterparty, sell_targets[2]),
                  Transform(sell_incumbent_bar, sell_incumbent_bar_target),
                  Transform(sell_mb, sell_mb_target),
                  Transform(sell_mc, sell_mc_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        sell_ring = Circle(radius=0.31, color=FOCUS, stroke_width=2.5)
        sell_ring.rotate(90 * DEGREES, RIGHT).move_to([2.6, -0.04, 0.32]).set_flat_stroke(False)
        sell_zero = VGroup(*[Line([x - 0.52, -0.02, 0.75], [x + 0.52, -0.02, 0.75],
            color=MUTED, stroke_width=1.5) for x in [-1.75, -0.85, 1.75]])
        sell_price = Line([-2.15, -0.045, 0.75 + 6 * 0.55], [-0.45, -0.045, 0.75 + 6 * 0.55], color=GUIDE, stroke_width=3)
        sell_proposal = DashedLine([-1.25, -0.055, 0.75 + 5.75 * 0.55], [2.15, -0.055, 0.75 + 5.75 * 0.55], color=GUIDE, stroke_width=3)
        sell_values = VGroup()
        for text, color, at, edge in [
                (r'MC $\$3.50$', SUPPLY, [-1.75, 0, 2.9250000000000003], ORIGIN),
                (r'MB $\$6$', DEMAND, [-0.28, 0, 4.2700000000000005], LEFT),
                (r'MC $\$4$', SUPPLY, [2.33, 0, 2.95], LEFT)]:
            label = Tex(text, color=color).scale(0.56)
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
            sell_values.add(label)
        stay_text = Tex(r'Keep $\$6$: gain $\$0$', color=CAPTION).scale(0.60)
        offer_text = Tex(r'Ask $\$5.75$\\Gain $\$1.75$/lb', color=INK).scale(0.62)
        for label, at, edge in [(stay_text, [-3.05, -0.07, 4.7], RIGHT),
                                (offer_text, [3.05, -0.07, 3.65], LEFT)]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
        wait_arrow = Arrow([-2.85, 4.7, 0], [-2.15, 0.75 + 6 * 0.55, 0],
                           buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        offer_arrow = Arrow([2.85, 3.65, 0], [2.15, 0.75 + 5.75 * 0.55, 0],
                            buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        for arrow in [wait_arrow, offer_arrow]:
            arrow.rotate(90 * DEGREES, RIGHT, about_point=ORIGIN).shift(DOWN * 0.07)
        self.play(Create(sell_ring), Create(sell_zero), Create(sell_price),
                  Create(sell_proposal), FadeIn(sell_values), FadeIn(stay_text), FadeIn(offer_text),
                  Create(wait_arrow), Create(offer_arrow), FadeIn(seller_question))
        self.pause('1.h')
        self.play(sell_price.animate.put_start_and_end_on(
                      np.array([0.45, -0.045, 0.75 + 5.75 * 0.55]), np.array([2.15, -0.045, 0.75 + 5.75 * 0.55])),
                  sell_mb.animate.shift(RIGHT * 1.7), sell_zero[1].animate.shift(RIGHT * 1.7),
                  sell_values[1].animate.shift(RIGHT * 1.7),
                  sell_incumbent.animate.shift(LEFT * 0.65),
                  sell_incumbent_bar.animate.shift(LEFT * 0.65),
                  sell_zero[0].animate.shift(LEFT * 0.65), sell_values[0].animate.shift(LEFT * 0.65),
                  FadeOut(seller_question), FadeOut(sell_proposal), FadeOut(stay_text), FadeOut(wait_arrow),
                  FadeOut(offer_arrow), offer_text.animate.set_color(GOV), run_time=0.9, rate_func=smooth)
        adjustment_head = fixed(title('Price adjustment'))
        self.remove(head)
        self.play(FadeOut(sell_detail), FadeOut(sell_zero), FadeOut(sell_price), FadeOut(sell_values),
                  FadeOut(offer_text), FadeOut(sell_ring), FadeIn(adjustment_head),
                  self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.3)
        head = adjustment_head
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_marks.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_marks, graphs)
        self.remove(units)
        self.remove(excess)
        self.add(tried_low)
        everyone = fixed(Tex('Other unserved sellers have the same incentive.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(everyone), run_time=0.3)
        self.add(units)
        tried_high = VGroup(*[DashedLine(ax.c2p(0, 6), ax.c2p(q, 6), color=GUIDE, stroke_width=1).set_opacity(0.25) for ax, q in [(demand_axes, 30), (supply_axes, 80)]])
        fixed(tried_high)
        self.add(tried_high)
        self.play(price.animate.set_value(4), run_time=3.0, rate_func=smooth)

        # ---- 1.i · Counts and incentives are two views of the same condition.
        eq_head = fixed(title('Equilibrium'))
        equilibrium = fixed(Tex(
            r'Equilibrium: no willing buyer or seller is left without a trade. $Q_s=Q_d$.',
            color=INK, tex_to_color_map={'Equilibrium': DEFINITION}))
        equilibrium.scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        # A plain fade avoids aligning and morphing unrelated paragraphs of glyphs.
        self.play(FadeOut(head), FadeOut(everyone), FadeIn(eq_head), FadeIn(equilibrium), run_time=0.4)
        head = eq_head
        self.pause('1.i')

        # ---- 1.i.stability · Test a deviation; count the exact whole lots.
        proposed = VGroup(*[DashedLine(ax.c2p(0, 4.25), ax.c2p(q, 4.25), color=GUIDE, stroke_width=2) for ax, q in [(demand_axes, 38), (supply_axes, 45)]])
        fixed(proposed)
        proposed_prices = fixed(VGroup(*[
            Tex(r'\$4.25', color=GUIDE).scale(0.48).next_to(line.get_start(), LEFT, buff=0.12)
            for line in proposed]))
        # The attached price labels replace nearby $4 ticks during the comparison.
        four_dollar_ticks = fixed(VGroup(demand_ticks[6], supply_ticks[6]))
        self.play(FadeOut(equilibrium), FadeOut(four_dollar_ticks), FadeIn(proposed), FadeIn(proposed_prices))
        self.pause('1.i.stability')
        self.play(FadeOut(proposed), FadeOut(proposed_prices), FadeIn(four_dollar_ticks),
                  price.animate.set_value(4.25), run_time=1.0)
        excess_test = fixed(Tex('Seven willing sellers have no buyer. They can undercut.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(excess_test), run_time=0.3)
        self.wait(0.8)
        self.play(price.animate.set_value(4), run_time=1.0)
        self.play(price.animate.set_value(3.75), run_time=1.0)
        shortage_test = fixed(Tex('Six willing buyers have no seller. They can offer more.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeOut(excess_test), FadeIn(shortage_test), run_time=0.3)
        self.wait(0.8)
        self.play(price.animate.set_value(4), run_time=1.0)
        stable = fixed(Tex(r'Above $\$4$: excess. Below $\$4$: shortage.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeOut(shortage_test), FadeIn(stable), run_time=0.3)
        self.pause('1.i.stable')

        # ========== 7. Graph ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15
        self.camera.frame.set_height(8)


        # One person is one 1,000-lb lot. Bar height is dollars per pound.
        BUYER_MB = np.array([12 - n / 5 for n in range(1, 60)])
        SELLER_MC = np.array([2 + n / 20 for n in range(1, 101)])
        EPS = 1e-7
        DOLLAR_HEIGHT = 0.035
        price = ValueTracker(4)
        show_counts = ValueTracker(1)
        show_trades = ValueTracker(1)
        show_buyers = ValueTracker(1)
        show_sellers = ValueTracker(1)
        self.add(price, show_counts, show_trades, show_buyers, show_sellers)

        # B3's camera: buyers occupy the upper half, sellers the lower half.
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(PLAZA_CENTER).set_height(11)
        BAR_BASE, DOLLAR_HEIGHT = 0.17, 0.035
        ARC_RADIUS, STEP_IN = 4.35, 0.82
        PAIR_LEFT, PAIR_STEP, PAIR_OFFSET = -3.35, 6.7 / 39, 0.40
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        buyer_people, buyer_bars, buyer_checks, buyer_circles = Group(), Group(), VGroup(), VGroup()
        seller_people, seller_bars, seller_checks, seller_circles = Group(), Group(), VGroup(), VGroup()
        buyer_crosses, seller_crosses = VGroup(), VGroup()
        buyer_positions, seller_positions = [], []
        for side, values, color, people, bars, checks, crosses, circles, positions, visibility in [
                ('B', BUYER_MB, DEMAND, buyer_people, buyer_bars, buyer_checks, buyer_crosses,
                 buyer_circles, buyer_positions, show_buyers),
                ('S', SELLER_MC, SUPPLY, seller_people, seller_bars, seller_checks, seller_crosses,
                 seller_circles, seller_positions, show_sellers)]:
            for n, value in enumerate(values):
                angle = (-55 + 110 * n / (len(values) - 1)) * DEGREES
                x = ARC_RADIUS * np.sin(angle)
                y = (1 if side == 'B' else -1) * ARC_RADIUS * np.cos(angle)
                positions.append(np.array([x, y, 0.045]))
                shadow = Disk3D(radius=0.044, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28)
                shadow.set_color(color).move_to([x, y, 0.025])
                orb = Sphere(radius=0.034, color=color, resolution=(12, 8)).move_to([x, y, 0.064])
                person = Group(shadow, orb)
                bar = Rectangle3D(width=0.055, height=value * DOLLAR_HEIGHT,
                                  resolution=(2, 2), opacity=0.65).set_color(color)
                bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
                check = (VMobject(color=GOV, stroke_width=1.6).set_points_as_corners(
                    [[-0.022, 0, 0], [-0.006, -0.017, 0], [0.025, 0.025, 0]]))
                cross = (VGroup(
                    Line([-0.019, -0.019, 0], [0.019, 0.019, 0], color=GUIDE, stroke_width=1.2),
                    Line([-0.019, 0.019, 0], [0.019, -0.019, 0], color=GUIDE, stroke_width=1.2))).set_color(GUIDE)
                for mark, accepted in [(check, True), (cross, False)]:
                    mark.price, mark.value, mark.visibility, mark.side = price, value, visibility, side
                    mark.anchor, mark.dollar_height, mark.accepted = bar, DOLLAR_HEIGHT, accepted
                    mark.scale(self.camera.frame.get_scale())
                    mark.face_mat = np.eye(3)
                    mark.add_updater(face_camera)
                    mark.add_updater(lambda m: m.move_to(
                        m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.085))
                        .set_stroke(opacity=m.visibility.get_value() * (1 if m.accepted else 0.65) * float(
                            (m.value + 1e-7 >= m.price.get_value() if m.side == 'B' else m.value <= m.price.get_value() + 1e-7) == m.accepted))
                        .set_fill(opacity=0))
                # Invisible anchors retain the existing deliberation endpoints.
                circle = Circle(radius=0.035, color=GOV, stroke_width=0).move_to([x, y, 0.045])
                circle.set_stroke(opacity=0).set_fill(opacity=0)
                for mob in [person, bar, circle]:
                    mob.rim = mob.get_center().copy()
                    mob.home = np.array([x * STEP_IN, y * STEP_IN, mob.rim[2]])
                    mob.pair_home = np.array([PAIR_LEFT + n * PAIR_STEP, (PAIR_OFFSET if side == 'B' else -PAIR_OFFSET), mob.rim[2]])
                    mob.home_width = mob.paired_width = mob.get_width()
                    mob.price, mob.rank, mob.visibility = price, n + 1, show_trades
                    mob.mb, mob.mc = BUYER_MB, SELLER_MC
                    mob.side, mob.value, mob.willingness = side, value, visibility
                    mob.pair_step, mob.pair_offset = PAIR_STEP, (PAIR_OFFSET if side == 'B' else -PAIR_OFFSET)
                    mob.add_updater(lambda m: setattr(m, 'pair_home', np.array([
                        (m.rank - 1 - (min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()),
                                          np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)) - 1) / 2)
                        * m.pair_step, m.pair_offset, m.home[2]])))
                    mob.add_updater(lambda m: setattr(m, 'willing_fraction', m.willingness.get_value() * float(
                        m.value + 1e-7 >= m.price.get_value() if m.side == 'B' else m.value <= m.price.get_value() + 1e-7)))
                    mob.add_updater(lambda m: setattr(m, 'pair_fraction', m.visibility.get_value() * float(
                        m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()),
                                      np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))))
                    mob.add_updater(lambda m: m.move_to(
                        (m.rim + m.willing_fraction * (m.home - m.rim)) * (1 - m.pair_fraction)
                        + m.pair_home * m.pair_fraction))
                people.add(person)
                bars.add(bar)
                checks.add(check)
                crosses.add(cross)
                circles.add(circle)
        # B3 world text: labels belong to the plaza and face the moving camera.
        buyer_label = Tex('Buyers', color=DEMAND).scale(0.82).move_to([0, 4.65, 0.45])
        seller_label = Tex('Sellers', color=SUPPLY).scale(0.82).move_to([0, -5.25, 0.04])
        units = Tex('One person = 1,000 lb', color=CAPTION).scale(0.65).move_to([0, -5.95, 0.04])
        for label in [buyer_label, seller_label, units]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        buyers = Group(buyer_bars, buyer_people, buyer_circles)
        sellers = Group(seller_bars, seller_people, seller_circles)
        crowd = Group(floor, rim, buyers, sellers, buyer_label, seller_label, units)
        crowd_marks = VGroup(buyer_checks, seller_checks, buyer_crosses, seller_crosses)

        # Both graphs share their own price scale, independent of the 3D totem.
        graph_price_height = 2.0
        demand_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=graph_price_height)
        supply_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=graph_price_height)
        demand_axes.shift(np.array([1.90, 0.80, 0]) - demand_axes.c2p(0, 0))
        supply_axes.shift(np.array([1.90, -1.84, 0]) - supply_axes.c2p(0, 0))
        ticks = VGroup()
        demand_ticks, supply_ticks = VGroup(), VGroup()
        for ax, side_ticks in [(demand_axes, demand_ticks), (supply_axes, supply_ticks)]:
            for q in [0, 20, 40, 60, 80, 100]:
                tick = fixed(Tex(str(q), color=CAPTION)).scale(0.38).next_to(ax.c2p(q, 0), DOWN, buff=0.10)
                tick.quantity, tick.price, tick.visibility = q, price, show_counts
                tick.values, tick.side = (BUYER_MB, 'buyer') if ax is demand_axes else (SELLER_MC, 'seller')
                tick.add_updater(lambda m: m.set_opacity(1 - m.visibility.get_value() * float(abs(
                    m.quantity - (np.count_nonzero(m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else
                                  np.count_nonzero(m.values <= m.price.get_value() + 1e-7))) < 7)))
                side_ticks.add(tick)
            for p in [4, 8, 12]:
                side_ticks.add(fixed(Tex(str(p), color=CAPTION)).scale(0.35).next_to(ax.c2p(0, p), LEFT, buff=0.10))
            ticks.add(side_ticks)
        # One narrow bar per lot. The two colors occupy adjacent slots when overlaid.
        demand_lot_bars, supply_lot_bars = VGroup(), VGroup()
        for ax, values, color, left, right, lot_bars in [
                (demand_axes, BUYER_MB, DEMAND, 0.12, 0.45, demand_lot_bars),
                (supply_axes, SELLER_MC, SUPPLY, 0.55, 0.88, supply_lot_bars)]:
            for n, value in enumerate(values):
                lot_bars.add(Polygon(ax.c2p(n + left, 0), ax.c2p(n + right, 0),
                    ax.c2p(n + right, value), ax.c2p(n + left, value),
                    stroke_width=0, fill_color=color, fill_opacity=0.50))
        demand_steps = Line(demand_axes.c2p(0, 12), demand_axes.c2p(60, 0), color=DEMAND, stroke_width=2.4)
        supply_steps = Line(supply_axes.c2p(0, 2), supply_axes.c2p(100, 7), color=SUPPLY, stroke_width=2.4)
        demand_fit = Line(demand_axes.c2p(0, 12), demand_axes.c2p(60, 0), color=DEMAND).set_opacity(0)
        supply_fit = Line(supply_axes.c2p(0, 2), supply_axes.c2p(100, 7), color=SUPPLY).set_opacity(0)
        demand_word = fixed(Tex(r'Demand: $P=12-Q_d/5$', color=DEMAND)).scale(0.59).move_to([4.45, 2.85, 0])
        supply_word = fixed(Tex(r'Supply: $P=2+Q_s/20$', color=SUPPLY)).scale(0.59).move_to([4.45, 0.18, 0])
        graph_units = fixed(Tex(r'$Q$: thousands of pounds', color=CAPTION)).scale(0.48).move_to([4.5, -2.25, 0])
        graph_prices = VGroup()
        for ax, values, side in [(demand_axes, BUYER_MB, 'buyer'), (supply_axes, SELLER_MC, 'seller')]:
            quantity = np.count_nonzero(values + EPS >= price.get_value()) if side == 'buyer' else np.count_nonzero(values <= price.get_value() + EPS)
            line = DashedLine(ax.c2p(0, price.get_value()), ax.c2p(quantity, price.get_value()), color=GUIDE, stroke_width=2.3)
            line.axes, line.price, line.values, line.side = ax, price, values, side
            line.add_updater(lambda m: set_dashed_endpoints(m, m.axes.c2p(0, m.price.get_value()), m.axes.c2p(max(0, min(100, 60 - 5 * m.price.get_value() if m.side == 'buyer' else 20 * (m.price.get_value() - 2))), m.price.get_value())))
            graph_prices.add(line)
        demand_guide = Line(demand_axes.c2p(45, 0), demand_axes.c2p(45, 3), color=DEMAND, stroke_width=2)
        demand_guide.axes, demand_guide.price, demand_guide.values, demand_guide.visibility = demand_axes, price, BUYER_MB, show_counts
        demand_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), 0), m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), m.price.get_value())).set_opacity(m.visibility.get_value()))
        supply_guide = Line(supply_axes.c2p(20, 0), supply_axes.c2p(20, 3), color=SUPPLY, stroke_width=2)
        supply_guide.axes, supply_guide.price, supply_guide.values, supply_guide.visibility = supply_axes, price, SELLER_MC, show_counts
        supply_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), 0), m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), m.price.get_value())).set_opacity(m.visibility.get_value()))
        # Each bare count sits at its quantity-axis position, in its curve's color.
        counts = VGroup()
        for ax, values, side, color in [(demand_axes, BUYER_MB, 'buyer', DEMAND),
                                         (supply_axes, SELLER_MC, 'seller', SUPPLY)]:
            number = fixed(Integer(0, color=color)).scale(0.50)
            number.axes, number.price, number.values = ax, price, values
            number.side, number.visibility = side, show_counts
            number.add_updater(lambda m: m.set_value(int(np.count_nonzero(
                m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else
                np.count_nonzero(m.values <= m.price.get_value() + 1e-7)))
                .next_to(m.axes.c2p(m.get_value(), 0), DOWN, buff=0.10)
                .set_opacity(m.visibility.get_value()))
            counts.add(number)
        # The posted price is a height on the totem at the right end of the divider.
        TOTEM_X, TOTEM_BASE, TOTEM_DOLLAR_HEIGHT = 4.8, 0.035, 0.28
        plaza_divider = DashedLine([-4.8, 0, TOTEM_BASE], [4.8, 0, TOTEM_BASE],
                                  color=MUTED, stroke_width=2, dash_length=0.14)
        plaza_divider.put_start_and_end_on(np.array([-4.8, 0, TOTEM_BASE]), np.array([4.8, 0, TOTEM_BASE]))
        plaza_divider.set_stroke(opacity=0.8).set_flat_stroke(False)
        price_post = Line([TOTEM_X, 0, TOTEM_BASE], [TOTEM_X, 0, TOTEM_BASE + 12 * TOTEM_DOLLAR_HEIGHT],
                          color=CAPTION, stroke_width=3).set_flat_stroke(False)
        post_foot = Disk3D(radius=0.10, resolution=(2, 24), shading=(0, 0, 0), opacity=0.5)
        post_foot.set_color(MUTED).move_to([TOTEM_X, 0, TOTEM_BASE])
        post_ticks, post_numbers = VGroup(), VGroup()
        for level in range(0, 13, 2):
            z = TOTEM_BASE + level * TOTEM_DOLLAR_HEIGHT
            post_ticks.add(Line([TOTEM_X - 0.09, 0, z], [TOTEM_X + 0.09, 0, z],
                                color=MUTED, stroke_width=1.5).set_flat_stroke(False))
            if level in [0, 4, 8, 12]:
                number = Tex(str(level), color=CAPTION).scale(0.50)
                number.face_mat = np.eye(3)
                number.add_updater(face_camera)
                number.update()
                number.move_to([TOTEM_X - 0.20, -0.025, z], aligned_edge=RIGHT)
                post_numbers.add(number)
        price_marker = Line([TOTEM_X - 0.16, -0.025, TOTEM_BASE + price.get_value() * TOTEM_DOLLAR_HEIGHT],
                            [TOTEM_X + 0.16, -0.025, TOTEM_BASE + price.get_value() * TOTEM_DOLLAR_HEIGHT],
                            color=GUIDE, stroke_width=5).set_flat_stroke(False)
        price_marker.price, price_marker.base, price_marker.dollar_height = price, TOTEM_BASE, TOTEM_DOLLAR_HEIGHT
        price_marker.add_updater(lambda m: m.set_z(m.base + m.price.get_value() * m.dollar_height))
        price_heading = Tex(r'Price (\$/lb)', color=CAPTION).scale(0.63)
        price_heading.move_to([TOTEM_X, 0, TOTEM_BASE + 12 * TOTEM_DOLLAR_HEIGHT + 0.45])
        price_word = Tex(r'\$', color=GUIDE).scale(0.78)
        price_number = DecimalNumber(price.get_value(), num_decimal_places=2, color=GUIDE).scale(0.78)
        price_number.tracker = price
        for label in [price_heading, price_word, price_number]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
        price_word.anchor = price_marker
        price_word.add_updater(lambda m: m.move_to(m.anchor.get_end() + RIGHT * 0.15, aligned_edge=LEFT))
        price_number.anchor = price_word
        price_number.add_updater(lambda m: m.next_to(m.anchor, RIGHT, buff=0.06))
        current_price = VGroup(price_word, price_number)
        price_readout = VGroup(post_numbers, price_heading, current_price)
        price_readout.update()
        crowd.add(plaza_divider, post_foot, price_post, post_ticks, price_marker, price_readout)
        graphs = VGroup(demand_axes, supply_axes, ticks, demand_fit, supply_fit, demand_lot_bars, supply_lot_bars, demand_steps, supply_steps,
                        demand_word, supply_word, graph_prices, demand_guide, supply_guide, graph_units, counts)
        fixed(graphs)
        # World and fixed overlay objects are added separately, as in B3.

        # ---- 1.i.graph · Merge the two representations of the same market.
        price.set_value(4)
        head = fixed(title('Why does the crossing give equilibrium?'))
        self.add(head, crowd, crowd_marks, graphs)
        # Carry the original objects together. Their geometry and scale never morph.
        demand_plot = fixed(VGroup(demand_axes, demand_lot_bars, demand_steps,
            demand_ticks, graph_prices[0], demand_guide, counts[0]))
        supply_plot = fixed(VGroup(supply_axes, supply_lot_bars, supply_steps,
            supply_ticks, graph_prices[1], supply_guide, counts[1]))
        graphs.suspend_updating()
        self.remove(graphs)
        self.add(demand_plot, supply_plot, demand_word, supply_word, graph_units)
        self.play(FadeOut(demand_word), FadeOut(supply_word), FadeOut(graph_units),
                  FadeOut(units), run_time=0.35)
        merged_origin = np.array([1.90, -0.90, 0])
        demand_shift = merged_origin - demand_axes.c2p(0, 0)
        supply_shift = merged_origin - supply_axes.c2p(0, 0)
        self.play(demand_plot.animate.shift(demand_shift),
                  supply_plot.animate.shift(supply_shift), run_time=2.0, rate_func=smooth)

        # Keep one complete graph on the right; the plaza retains its own totem.
        merged_axes, merged_demand, merged_supply = demand_axes, demand_steps, supply_steps
        merged_price, merged_drop = graph_prices[0], demand_guide
        self.play(FadeOut(supply_axes), FadeOut(supply_ticks), FadeOut(supply_guide),
                  FadeOut(graph_prices[1]), FadeOut(counts[1]), run_time=0.35)
        counts[0].set_color(CAPTION)
        demand_ticks[6].set_color(GUIDE)
        merged_ticks = fixed(VGroup(demand_ticks, counts[0]))
        merged_dot = fixed(Dot(merged_axes.c2p(40, 4), radius=0.055, color=GUIDE))
        graph_price_heading = fixed(Tex(r'Price (\$/lb)', color=CAPTION)).scale(0.48)
        graph_price_heading.next_to(merged_axes.c2p(0, 13), UP, buff=0.16, aligned_edge=LEFT)
        merged_labels = fixed(VGroup(
            graph_price_heading,
            Tex(r'$Q$: thousands of pounds', color=CAPTION).scale(0.48)
                .next_to(merged_axes.c2p(50, 0), DOWN, buff=0.48),
            Tex('D / MB', color=DEMAND).scale(0.60)
                .next_to(merged_axes.c2p(12, 9.6), UP, buff=0.10),
            Tex('S / MC', color=SUPPLY).scale(0.60)
                .next_to(merged_axes.c2p(84, 6.2), UP, buff=0.10)))
        self.play(FadeIn(merged_labels), FadeIn(merged_dot), run_time=0.4)
        same = fixed(Tex('Same price, same quantity.', color=INK)).scale(0.7443)
        same.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(same))
        self.pause('1.i.graph')

        # ---- 1.i.algebra · Equality first, then solve. No exercise Q1 repeat.
        merged_graph = fixed(VGroup(merged_axes, demand_lot_bars, supply_lot_bars,
            merged_demand, merged_supply, merged_ticks, merged_labels, merged_price, merged_drop, merged_dot))
        crowd.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(same))
        algebra_head = fixed(title('What equation expresses equilibrium?'))
        self.play(ReplacementTransform(head, algebra_head))
        equality = fixed(Tex(r'$Q_d=Q_s=Q$', color=DEFINITION)).scale(1.1).move_to([-3.75, 2.10, 0])
        demand_equation = fixed(Tex(r'$P=12-Q_d/5$', color=DEMAND)).scale(0.82).move_to([-3.75, 1.20, 0])
        supply_equation = fixed(Tex(r'$P=2+Q_s/20$', color=SUPPLY)).scale(0.82).move_to([-3.75, 0.50, 0])
        self.play(FadeIn(equality), FadeIn(demand_equation), FadeIn(supply_equation))
        equation = fixed(Tex(r'$12-Q/5=2+Q/20$', color=INK)).scale(0.93).move_to([-3.75, -0.40, 0])
        self.play(FadeIn(equation))
        simplified = fixed(Tex(r'$10=Q/4$', color=INK)).scale(0.95).move_to([-3.75, -1.17, 0])
        result = fixed(Tex(r'$Q^*=40,\qquad P^*=2+40/20=4$', color=GUIDE)).scale(0.85).move_to([-3.75, -2.05, 0])
        self.play(FadeIn(simplified))
        self.play(FadeIn(result))
        final = fixed(Tex(r'40,000 pounds at $\$4$ per pound.', color=INK)).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(final))
        self.pause('1.i.algebra')

        # ========== 8. Welfare ==========
        # The plaza has established equilibrium. The welfare argument starts on
        # the graph; selected lost trades expand into the two-person comparison.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        price = ValueTracker(4)
        allocation_flags = Group(*[ValueTracker(float(n <= 40)) for n in range(1, 60)])
        market_state = ValueTracker(0)
        market_state.price, market_state.flags = price, allocation_flags
        market_state.mb, market_state.mc = BUYER_MB, SELLER_MC

        # Track actual lots internally; do not turn the graph into a dashboard.
        def update_welfare(m):
            p = m.price.get_value()
            m.weights = np.array([flag.get_value() for flag in m.flags])
            m.count = float(m.weights.sum())
            m.qd = int(np.count_nonzero(m.mb + 1e-7 >= p))
            m.qs = int(np.count_nonzero(m.mc <= p + 1e-7))
            costs = m.mc[:len(m.mb)]
            gains = m.mb - costs
            m.cs = float(np.dot(m.weights, m.mb - p) * 1000)
            m.ps = float(np.dot(m.weights, p - costs) * 1000)
            m.ts = float(np.dot(m.weights, gains) * 1000)
            missing = (1 - m.weights) * np.maximum(gains, 0)
            m.loss = float(missing.sum() * 1000)
            m.loss_rank = float(np.dot(missing, np.arange(1, len(m.mb) + 1)) / missing.sum()) if m.loss > 1e-7 else 40

        market_state.add_updater(update_welfare)
        market_state.update()
        show_total, show_loss, show_price = ValueTracker(0), ValueTracker(0), ValueTracker(1)
        self.add(price, allocation_flags, market_state, show_total, show_loss, show_price)
        ax = style_axes([0, 60, 20], [0, 12.5, 2], x_length=10, y_length=4.5)
        ax.shift(np.array([-5.2, -2.35, 0]) - ax.c2p(0, 0))
        demand = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3)
        supply = Line(ax.c2p(0, 2), ax.c2p(60, 5), color=SUPPLY, stroke_width=3)
        curve_labels = VGroup(
            Tex('D / MB', color=DEMAND).scale(0.62).next_to(ax.c2p(13, 9.4), UP, buff=0.16),
            Tex('S / MC', color=SUPPLY).scale(0.62).next_to(ax.c2p(55, 4.75), UP, buff=0.16))
        axis_labels = VGroup(
            Tex(r'Price (\$/lb)', color=CAPTION).scale(0.52).next_to(ax.c2p(0, 12.5), UP, buff=0.17),
            Tex('Quantity (thousand lb)', color=CAPTION).scale(0.52).next_to(ax.c2p(30, 0), DOWN, buff=0.48))
        ticks = VGroup()
        for q in [0, 20, 40, 60]:
            tick = Tex(str(q), color=CAPTION).scale(0.48).next_to(ax.c2p(q, 0), DOWN, buff=0.12)
            tick.state, tick.quantity, tick.visibility = market_state, q, show_price
            tick.add_updater(lambda m: m.set_opacity(float(m.visibility.get_value() < 0.01
                or abs(m.quantity - min(m.state.qd, m.state.qs)) > 3)))
            ticks.add(tick)
        ticks.add(Tex('12', color=CAPTION).scale(0.48).next_to(ax.c2p(0, 12), LEFT, buff=0.15))

        # The exact per-lot regions share edges, so the eye sees one area.
        # No floating bars, separate numerical totals, leaders or gap brackets.
        cs_area, ps_area, total_area, lost_area = VGroup(), VGroup(), VGroup(), VGroup()
        for n in range(39):
            benefit, cost = BUYER_MB[n], SELLER_MC[n]
            cs_area.add(Polygon(ax.c2p(n, 4), ax.c2p(n + 1, 4),
                ax.c2p(n + 1, benefit), ax.c2p(n, benefit),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.43))
            ps_area.add(Polygon(ax.c2p(n, cost), ax.c2p(n + 1, cost),
                ax.c2p(n + 1, 4), ax.c2p(n, 4),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.43))
            for group, color, realized in [(total_area, TOTAL, True), (lost_area, MUTED, False)]:
                cell = Polygon(ax.c2p(n, cost), ax.c2p(n + 1, cost),
                    ax.c2p(n + 1, benefit), ax.c2p(n, benefit),
                    stroke_width=0, fill_color=color, fill_opacity=0)
                cell.state, cell.rank, cell.realized = market_state, n, realized
                cell.visibility = show_total if realized else show_loss
                cell.add_updater(lambda m: m.set_fill(opacity=0.43 * m.visibility.get_value()
                    * (m.state.weights[m.rank] if m.realized else 1 - m.state.weights[m.rank])))
                group.add(cell)
        cs_label = Tex('CS', color=DEMAND).scale(0.9).move_to(ax.c2p(12, 7))
        ps_label = Tex('PS', color=SUPPLY).scale(0.72).move_to(ax.c2p(11, 3.22))
        total_label = Tex('Total surplus', color=TOTAL).scale(0.72).move_to(ax.c2p(12, 7.2))
        dwl_label = Tex('DWL', color=CAPTION).scale(0.53)
        dwl_label.axes, dwl_label.state = ax, market_state
        dwl_label.add_updater(lambda m: m.move_to(m.axes.c2p(m.state.loss_rank - 0.5,
            (14 - 0.15 * m.state.loss_rank) / 2)))
        price_guide = VMobject(color=GUIDE, stroke_width=2.3)
        price_guide.axes, price_guide.price, price_guide.visibility = ax, price, show_price
        price_guide.add_updater(lambda m: set_dashed_endpoints(m,
            m.axes.c2p(0, m.price.get_value()),
            m.axes.c2p(max(0, min(60 - 5 * m.price.get_value(), 20 * (m.price.get_value() - 2))), m.price.get_value()))
            .set_stroke(opacity=m.visibility.get_value()))
        price_number = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(0.58)
        price_number.axes, price_number.price, price_number.visibility = ax, price, show_price
        price_number.add_updater(lambda m: m.set_value(m.price.get_value())
            .next_to(m.axes.c2p(0, m.price.get_value()), LEFT, buff=0.17).set_opacity(m.visibility.get_value()))
        quantity_drop = VMobject(color=MUTED, stroke_width=1.3)
        quantity_drop.axes, quantity_drop.state, quantity_drop.visibility = ax, market_state, show_price
        quantity_drop.add_updater(lambda m: m.set_points_as_corners([
            m.axes.c2p(min(m.state.qd, m.state.qs), 0),
            m.axes.c2p(min(m.state.qd, m.state.qs), m.state.price.get_value())])
            .set_stroke(opacity=0.65 * m.visibility.get_value()))
        quantity_number = Integer(40, color=GUIDE).scale(0.52)
        quantity_number.axes, quantity_number.state, quantity_number.visibility = ax, market_state, show_price
        quantity_number.add_updater(lambda m: m.set_value(min(m.state.qd, m.state.qs))
            .next_to(m.axes.c2p(m.get_value(), 0), DOWN, buff=0.12).set_opacity(m.visibility.get_value()))
        graph = fixed(VGroup(ax, cs_area, ps_area, total_area, lost_area,
            demand, supply, curve_labels, axis_labels, ticks,
            price_guide, price_number, quantity_drop, quantity_number))
        head = fixed(title('The gains from trade'))
        self.add(head, graph)
        self.play(FadeIn(fixed(cs_label)), FadeIn(fixed(ps_label)), run_time=0.6)
        self.pause('2.a')

        # ---- 2.b · Join the two familiar benefits into one purple region.
        total_definition = fixed(Tex(r'Total surplus $=$ PS $+$ CS', color=TOTAL,
            tex_to_color_map={'PS': SUPPLY, 'CS': DEMAND}).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(cs_label), FadeOut(ps_label), FadeOut(cs_area), FadeOut(ps_area),
                  show_total.animate.set_value(1), show_price.animate.set_value(0),
                  FadeIn(fixed(total_label)), FadeIn(total_definition), run_time=0.9, rate_func=smooth)
        graph.remove(cs_area, ps_area)
        self.add(graph, total_label)
        self.pause('2.b')

        # Policy ranges are intervals on the price axis, not a single allowed price.
        floor_legal = fixed(VGroup(
            Line(ax.c2p(0, 6), ax.c2p(0, 12.5), color=GOV, stroke_width=6),
            Dot(ax.c2p(0, 6), radius=0.045, color=GOV),
            VMobject(color=GOV, stroke_width=3).set_points_as_corners([
                ax.c2p(0, 12.5) + LEFT * 0.075 + DOWN * 0.12,
                ax.c2p(0, 12.5), ax.c2p(0, 12.5) + RIGHT * 0.075 + DOWN * 0.12]),
            Tex('Legal prices', color=GOV).scale(0.48).next_to(ax.c2p(0, 9), LEFT, buff=0.30)))
        ceiling_legal = fixed(VGroup(
            Line(ax.c2p(0, 0), ax.c2p(0, 3), color=GOV, stroke_width=6),
            Dot(ax.c2p(0, 3), radius=0.045, color=GOV),
            Tex('Legal prices', color=GOV).scale(0.48).next_to(ax.c2p(0, 1.4), LEFT, buff=0.30)))
        equilibrium_reference = fixed(VGroup(
            Dot(ax.c2p(40, 4), radius=0.052, color=CAPTION),
            Tex(r'$P^*=4$', color=CAPTION).scale(0.48).next_to(ax.c2p(40, 4), UP + RIGHT, buff=0.13),
            Line(ax.c2p(40, 0), ax.c2p(40, 4), color=MUTED, stroke_width=1.3)))
        lost_trade_span = fixed(VMobject(color=FOCUS, stroke_width=2.3))
        lost_trade_span.axes, lost_trade_span.state = ax, market_state
        lost_trade_span.add_updater(lambda m: m.set_points_as_corners([
            m.axes.c2p(min(m.state.qd, m.state.qs), 0) + UP * 0.48,
            m.axes.c2p(min(m.state.qd, m.state.qs), 0) + UP * 0.40,
            m.axes.c2p(40, 0) + UP * 0.40, m.axes.c2p(40, 0) + UP * 0.48]))
        lost_trade_label = fixed(Tex('Lost trades', color=FOCUS).scale(0.43))
        lost_trade_label.axes, lost_trade_label.state = ax, market_state
        lost_trade_label.add_updater(lambda m: m.move_to(
            m.axes.c2p((min(m.state.qd, m.state.qs) + 40) / 2, 0) + UP * 0.66))
        lost_trade_reference = fixed(VGroup(equilibrium_reference, lost_trade_span, lost_trade_label))

        # ---- 3.a · A higher legal price removes beneficial trades.
        next_head = fixed(title('A price floor'))
        self.play(FadeOut(head), FadeIn(next_head), FadeOut(total_definition), run_time=0.35)
        head = next_head
        self.play(show_price.animate.set_value(1), run_time=0.3)
        self.play(price.animate.set_value(6),
            *[allocation_flags[n].animate.set_value(0) for n in range(30, 40)], run_time=1.8, rate_func=smooth)
        self.play(FadeIn(floor_legal), run_time=0.4)
        self.pause('3.a')

        # ---- 3.b · Grey is the surplus the missing trades could have created.
        loss_definition = fixed(Tex('Deadweight loss: gains from trade that are lost.', color=INK)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(show_loss.animate.set_value(1), FadeIn(fixed(dwl_label)), FadeIn(loss_definition),
                  FadeIn(lost_trade_reference), run_time=0.7)
        self.pause('3.b')

        # ---- 3.c · Select a pair inside the lost-equilibrium range, then enlarge it.
        floor_buyer_bar = fixed(Polygon(ax.c2p(34.04, 0), ax.c2p(34.47, 0),
            ax.c2p(34.47, 5), ax.c2p(34.04, 5),
            stroke_width=0, fill_color=DEMAND, fill_opacity=0.75))
        floor_seller_bar = fixed(Polygon(ax.c2p(34.53, 0), ax.c2p(34.96, 0),
            ax.c2p(34.96, 3.75), ax.c2p(34.53, 3.75),
            stroke_width=0, fill_color=SUPPLY, fill_opacity=0.75))
        floor_source = fixed(VGroup(floor_buyer_bar, floor_seller_bar))
        selected_caption = fixed(Tex('One of the trades lost from equilibrium.', color=INK)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(dwl_label), FadeOut(loss_definition),
                  FadeIn(floor_source), FadeIn(selected_caption), run_time=0.6)
        self.pause('3.c.select')

        # These rectangles are the chosen MB and MC bars from the graph, not new people.
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.56
        floor_bar_targets = fixed(VGroup(
            Polygon([-1.16, DETAIL_BASE, 0], [-0.06, DETAIL_BASE, 0],
                    [-0.06, DETAIL_BASE + 5 * DETAIL_SCALE, 0], [-1.16, DETAIL_BASE + 5 * DETAIL_SCALE, 0],
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0.55),
            Polygon([0.06, DETAIL_BASE, 0], [1.16, DETAIL_BASE, 0],
                    [1.16, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0],
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=0.55)))
        graph.suspend_updating()
        lost_trade_reference.suspend_updating()
        self.play(FadeOut(graph), FadeOut(total_label), FadeOut(floor_legal),
                  FadeOut(lost_trade_reference), FadeOut(selected_caption),
                  Transform(floor_buyer_bar, floor_bar_targets[0]),
                  Transform(floor_seller_bar, floor_bar_targets[1]), run_time=1.3, rate_func=smooth)
        floor_people = Group()
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            shadow = Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
            shadow.move_to([x, DETAIL_BASE - 0.60, 0])
            person = Sphere(radius=0.18, color=color, resolution=(12, 8)).move_to([x, DETAIL_BASE - 0.35, 0])
            floor_people.add(shadow, person)
        fixed(floor_people)
        floor_axis = fixed(VGroup(
            Line([-3.05, DETAIL_BASE, 0], [-3.05, DETAIL_BASE + 8 * DETAIL_SCALE, 0], color=MUTED, stroke_width=1.5),
            Line([-1.31, DETAIL_BASE, 0], [1.31, DETAIL_BASE, 0], color=MUTED, stroke_width=1.5),
            Tex(r'Price (\$/lb)', color=CAPTION).scale(0.49).move_to([-3.05, DETAIL_BASE + 8 * DETAIL_SCALE + 0.27, 0]),
            Tex('0', color=CAPTION).scale(0.44).next_to([-3.05, DETAIL_BASE, 0], LEFT, buff=0.16)))
        floor_labels = fixed(VGroup(
            Tex(r'MB $\$5$', color=DEMAND).scale(0.62).next_to([-1.16, DETAIL_BASE + 5 * DETAIL_SCALE, 0], LEFT, buff=0.17),
            Tex(r'MC $\$3.75$', color=SUPPLY).scale(0.62).next_to([1.16, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0], RIGHT, buff=0.17)))
        floor_limit = fixed(Line([-3.05, DETAIL_BASE + 6 * DETAIL_SCALE, 0],
            [1.16, DETAIL_BASE + 6 * DETAIL_SCALE, 0], color=GUIDE, stroke_width=2.5))
        floor_limit_label = fixed(Tex(r'Floor $\$6$', color=GUIDE).scale(0.57)
            .next_to([-3.05, DETAIL_BASE + 6 * DETAIL_SCALE, 0], LEFT, buff=0.16))
        floor_legal_detail = fixed(VGroup(
            Line([-3.05, DETAIL_BASE + 6 * DETAIL_SCALE, 0],
                 [-3.05, DETAIL_BASE + 8 * DETAIL_SCALE, 0], color=GOV, stroke_width=6),
            Dot([-3.05, DETAIL_BASE + 6 * DETAIL_SCALE, 0], radius=0.045, color=GOV),
            Tex('Legal prices', color=GOV).scale(0.56)
                .next_to([-3.05, DETAIL_BASE + 7.0 * DETAIL_SCALE, 0], LEFT, buff=0.38)))
        floor_mutual = fixed(VGroup(
            Line([-2.89, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0], [-2.89, DETAIL_BASE + 5 * DETAIL_SCALE, 0],
                 color=TOTAL, stroke_width=4),
            Circle(radius=0.038, color=TOTAL, stroke_width=2, fill_color=BG, fill_opacity=1)
                .move_to([-2.89, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0]),
            Circle(radius=0.038, color=TOTAL, stroke_width=2, fill_color=BG, fill_opacity=1)
                .move_to([-2.89, DETAIL_BASE + 5 * DETAIL_SCALE, 0]),
            Tex('Both gain', color=TOTAL).scale(0.56)
                .next_to([-3.05, DETAIL_BASE + 4.375 * DETAIL_SCALE, 0], LEFT, buff=1.1)))
        floor_proposal = fixed(VMobject(color=GUIDE, stroke_width=1.8))
        set_dashed_endpoints(floor_proposal, [-3.05, DETAIL_BASE + 4 * DETAIL_SCALE, 0],
                             [1.16, DETAIL_BASE + 4 * DETAIL_SCALE, 0])
        floor_proposal_label = fixed(Tex(r'\$4', color=GUIDE).scale(0.53)
            .next_to([-3.05, DETAIL_BASE + 4 * DETAIL_SCALE, 0], LEFT, buff=0.16))
        floor_gain_bracket = fixed(VMobject(color=MUTED, stroke_width=2.5).set_points_as_corners([
            [2.99, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0], [3.10, DETAIL_BASE + 3.75 * DETAIL_SCALE, 0],
            [3.10, DETAIL_BASE + 5 * DETAIL_SCALE, 0], [2.99, DETAIL_BASE + 5 * DETAIL_SCALE, 0]]))
        floor_gain_label = fixed(VGroup(Tex('Lost surplus', color=INK).scale(0.62),
            Tex(r'$\$1{,}250$', color=INK).scale(0.75)).arrange(DOWN, buff=0.12)
            .move_to([3.40, DETAIL_BASE + 4.375 * DETAIL_SCALE, 0], aligned_edge=LEFT))
        floor_reason = fixed(Tex(r'Both gain at $\$4$; that price is illegal.', color=INK)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        floor_detail = Group(floor_axis, floor_labels, floor_limit, floor_limit_label,
            floor_legal_detail, floor_mutual, floor_proposal, floor_proposal_label,
            floor_gain_bracket, floor_gain_label, floor_people)
        fixed(floor_detail)
        floor_legal_detail.add(VMobject(color=GOV, stroke_width=3).set_points_as_corners([
            [-3.13, DETAIL_BASE + 8 * DETAIL_SCALE - 0.13, 0], [-3.05, DETAIL_BASE + 8 * DETAIL_SCALE, 0],
            [-2.97, DETAIL_BASE + 8 * DETAIL_SCALE - 0.13, 0]]))
        fixed(floor_legal_detail)
        self.play(FadeIn(floor_detail), FadeIn(floor_reason), run_time=0.65)
        self.pause('3.c')

        self.play(FadeOut(floor_detail), FadeOut(floor_reason), run_time=0.35)
        self.play(Transform(floor_buyer_bar, fixed(Polygon(ax.c2p(34.04, 0), ax.c2p(34.47, 0),
            ax.c2p(34.47, 5), ax.c2p(34.04, 5), stroke_width=0, fill_color=DEMAND, fill_opacity=0.75))),
            Transform(floor_seller_bar, fixed(Polygon(ax.c2p(34.53, 0), ax.c2p(34.96, 0),
            ax.c2p(34.96, 3.75), ax.c2p(34.53, 3.75), stroke_width=0, fill_color=SUPPLY, fill_opacity=0.75))),
            FadeIn(graph), FadeIn(total_label), FadeIn(floor_legal), run_time=1.0, rate_func=smooth)
        graph.resume_updating()
        self.play(FadeOut(floor_source), FadeOut(floor_legal), run_time=0.3)

        # ---- 4.a · Remove the floor, then set a lower legal maximum.
        self.play(price.animate.set_value(4), show_loss.animate.set_value(0),
            *[allocation_flags[n].animate.set_value(1) for n in range(30, 40)], run_time=1.1, rate_func=smooth)
        next_head = fixed(title('A price ceiling'))
        self.play(FadeOut(head), FadeIn(next_head), run_time=0.35)
        head = next_head
        self.play(price.animate.set_value(3),
            *[allocation_flags[n].animate.set_value(0) for n in range(20, 40)], run_time=1.8, rate_func=smooth)
        self.play(FadeIn(ceiling_legal), run_time=0.4)
        self.pause('4.a')
        lost_trade_reference.resume_updating()
        self.play(show_loss.animate.set_value(1), FadeIn(dwl_label), FadeIn(lost_trade_reference), run_time=0.7)
        self.pause('4.b')

        # ---- 4.c · Select a pair inside the lost-equilibrium range, then enlarge it.
        ceiling_buyer_bar = fixed(Polygon(ax.c2p(24.04, 0), ax.c2p(24.47, 0),
            ax.c2p(24.47, 7), ax.c2p(24.04, 7),
            stroke_width=0, fill_color=DEMAND, fill_opacity=0.75))
        ceiling_seller_bar = fixed(Polygon(ax.c2p(24.53, 0), ax.c2p(24.96, 0),
            ax.c2p(24.96, 3.25), ax.c2p(24.53, 3.25),
            stroke_width=0, fill_color=SUPPLY, fill_opacity=0.75))
        ceiling_source = fixed(VGroup(ceiling_buyer_bar, ceiling_seller_bar))
        selected_caption = fixed(Tex('One of the trades lost from equilibrium.', color=INK)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(dwl_label),
                  FadeIn(ceiling_source), FadeIn(selected_caption), run_time=0.6)
        self.pause('4.c.select')

        # These rectangles are the chosen MB and MC bars from the graph, not new people.
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.56
        ceiling_bar_targets = fixed(VGroup(
            Polygon([-1.16, DETAIL_BASE, 0], [-0.06, DETAIL_BASE, 0],
                    [-0.06, DETAIL_BASE + 7 * DETAIL_SCALE, 0], [-1.16, DETAIL_BASE + 7 * DETAIL_SCALE, 0],
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0.55),
            Polygon([0.06, DETAIL_BASE, 0], [1.16, DETAIL_BASE, 0],
                    [1.16, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0],
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=0.55)))
        graph.suspend_updating()
        lost_trade_reference.suspend_updating()
        self.play(FadeOut(graph), FadeOut(total_label), FadeOut(ceiling_legal),
                  FadeOut(lost_trade_reference), FadeOut(selected_caption),
                  Transform(ceiling_buyer_bar, ceiling_bar_targets[0]),
                  Transform(ceiling_seller_bar, ceiling_bar_targets[1]), run_time=1.3, rate_func=smooth)
        ceiling_people = Group()
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            shadow = Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
            shadow.move_to([x, DETAIL_BASE - 0.60, 0])
            person = Sphere(radius=0.18, color=color, resolution=(12, 8)).move_to([x, DETAIL_BASE - 0.35, 0])
            ceiling_people.add(shadow, person)
        fixed(ceiling_people)
        ceiling_axis = fixed(VGroup(
            Line([-3.05, DETAIL_BASE, 0], [-3.05, DETAIL_BASE + 8 * DETAIL_SCALE, 0], color=MUTED, stroke_width=1.5),
            Line([-1.31, DETAIL_BASE, 0], [1.31, DETAIL_BASE, 0], color=MUTED, stroke_width=1.5),
            Tex(r'Price (\$/lb)', color=CAPTION).scale(0.49).move_to([-3.05, DETAIL_BASE + 8 * DETAIL_SCALE + 0.27, 0]),
            Tex('0', color=CAPTION).scale(0.44).next_to([-3.05, DETAIL_BASE, 0], LEFT, buff=0.16)))
        ceiling_labels = fixed(VGroup(
            Tex(r'MB $\$7$', color=DEMAND).scale(0.62).next_to([-1.16, DETAIL_BASE + 7 * DETAIL_SCALE, 0], LEFT, buff=0.17),
            Tex(r'MC $\$3.25$', color=SUPPLY).scale(0.62).next_to([1.16, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0], RIGHT, buff=0.17)))
        ceiling_limit = fixed(Line([-3.05, DETAIL_BASE + 3 * DETAIL_SCALE, 0],
            [1.16, DETAIL_BASE + 3 * DETAIL_SCALE, 0], color=GUIDE, stroke_width=2.5))
        ceiling_limit_label = fixed(Tex(r'Ceiling $\$3$', color=GUIDE).scale(0.57)
            .next_to([-3.05, DETAIL_BASE + 3 * DETAIL_SCALE, 0], LEFT, buff=0.16))
        ceiling_legal_detail = fixed(VGroup(
            Line([-3.05, DETAIL_BASE + 0 * DETAIL_SCALE, 0],
                 [-3.05, DETAIL_BASE + 3 * DETAIL_SCALE, 0], color=GOV, stroke_width=6),
            Dot([-3.05, DETAIL_BASE + 3 * DETAIL_SCALE, 0], radius=0.045, color=GOV),
            Tex('Legal prices', color=GOV).scale(0.56)
                .next_to([-3.05, DETAIL_BASE + 1.5 * DETAIL_SCALE, 0], LEFT, buff=0.38)))
        ceiling_mutual = fixed(VGroup(
            Line([-2.89, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0], [-2.89, DETAIL_BASE + 7 * DETAIL_SCALE, 0],
                 color=TOTAL, stroke_width=4),
            Circle(radius=0.038, color=TOTAL, stroke_width=2, fill_color=BG, fill_opacity=1)
                .move_to([-2.89, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0]),
            Circle(radius=0.038, color=TOTAL, stroke_width=2, fill_color=BG, fill_opacity=1)
                .move_to([-2.89, DETAIL_BASE + 7 * DETAIL_SCALE, 0]),
            Tex('Both gain', color=TOTAL).scale(0.56)
                .next_to([-3.05, DETAIL_BASE + 5.125 * DETAIL_SCALE, 0], LEFT, buff=1.1)))
        ceiling_proposal = fixed(VMobject(color=GUIDE, stroke_width=1.8))
        set_dashed_endpoints(ceiling_proposal, [-3.05, DETAIL_BASE + 4 * DETAIL_SCALE, 0],
                             [1.16, DETAIL_BASE + 4 * DETAIL_SCALE, 0])
        ceiling_proposal_label = fixed(Tex(r'\$4', color=GUIDE).scale(0.53)
            .next_to([-3.05, DETAIL_BASE + 4 * DETAIL_SCALE, 0], LEFT, buff=0.16))
        ceiling_gain_bracket = fixed(VMobject(color=MUTED, stroke_width=2.5).set_points_as_corners([
            [2.99, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0], [3.10, DETAIL_BASE + 3.25 * DETAIL_SCALE, 0],
            [3.10, DETAIL_BASE + 7 * DETAIL_SCALE, 0], [2.99, DETAIL_BASE + 7 * DETAIL_SCALE, 0]]))
        ceiling_gain_label = fixed(VGroup(Tex('Lost surplus', color=INK).scale(0.62),
            Tex(r'$\$3{,}750$', color=INK).scale(0.75)).arrange(DOWN, buff=0.12)
            .move_to([3.40, DETAIL_BASE + 5.125 * DETAIL_SCALE, 0], aligned_edge=LEFT))
        ceiling_reason = fixed(Tex(r'Both gain at $\$4$; that price is illegal.', color=INK)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        ceiling_detail = Group(ceiling_axis, ceiling_labels, ceiling_limit, ceiling_limit_label,
            ceiling_legal_detail, ceiling_mutual, ceiling_proposal, ceiling_proposal_label,
            ceiling_gain_bracket, ceiling_gain_label, ceiling_people)
        fixed(ceiling_detail)
        self.play(FadeIn(ceiling_detail), FadeIn(ceiling_reason), run_time=0.65)
        self.pause('4.c')

        # ---- 5.a · Lift the restriction; the same $4 exchange becomes possible.
        next_head = fixed(title('Allow the trade'))
        recovered = fixed(VGroup(Tex('Surplus gained', color=TOTAL).scale(0.62),
            Tex(r'$\$3{,}750$', color=TOTAL).scale(0.75)).arrange(DOWN, buff=0.12).move_to(ceiling_gain_label))
        self.play(FadeOut(head), FadeIn(next_head), FadeOut(ceiling_reason),
                  FadeOut(ceiling_limit), FadeOut(ceiling_limit_label), FadeOut(ceiling_legal_detail),
                  FadeOut(ceiling_gain_label), FadeIn(recovered), run_time=0.6)
        head = next_head
        ceiling_detail.remove(ceiling_limit, ceiling_limit_label, ceiling_legal_detail, ceiling_gain_label)
        price.set_value(4)
        show_price.set_value(0)
        self.play(allocation_flags[24].animate.set_value(1),
                  Group(*ceiling_people[:2]).animate.shift(RIGHT * 1.05),
                  Group(*ceiling_people[2:]).animate.shift(LEFT * 1.05),
                  ceiling_gain_bracket.animate.set_color(TOTAL), run_time=0.9, rate_func=smooth)
        self.pause('5.a')

        # ---- 5.b · Return to all beneficial trades, without an isolated gap.
        next_head = fixed(title('Allow all beneficial trades'))
        self.play(FadeOut(head), FadeIn(next_head),
                  FadeOut(ceiling_detail), FadeOut(recovered), run_time=0.35)
        head = next_head
        # Complete the allocation off-screen; reveal one continuous purple region.
        for n in range(20, 40):
            allocation_flags[n].set_value(1)
        show_loss.set_value(0)
        market_state.update(0)
        graph.resume_updating()
        graph.suspend_updating()
        self.play(Transform(ceiling_buyer_bar, fixed(Polygon(ax.c2p(24.04, 0), ax.c2p(24.47, 0),
            ax.c2p(24.47, 7), ax.c2p(24.04, 7), stroke_width=0, fill_color=DEMAND, fill_opacity=0.75))),
            Transform(ceiling_seller_bar, fixed(Polygon(ax.c2p(24.53, 0), ax.c2p(24.96, 0),
            ax.c2p(24.96, 3.25), ax.c2p(24.53, 3.25), stroke_width=0, fill_color=SUPPLY, fill_opacity=0.75))),
            FadeIn(graph), FadeIn(total_label), run_time=1.4, rate_func=smooth)
        graph.resume_updating()
        self.play(FadeOut(ceiling_source), run_time=0.3)
        self.pause('5.b')

        # ---- 5.c · The crossing is the zero-gain boundary.
        marginal = fixed(Dot(ax.c2p(40, 4), radius=0.075, color=FOCUS))
        boundary = fixed(Tex('At the boundary, benefit equals cost.', color=INK).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(marginal), FadeIn(boundary), run_time=0.5)
        self.pause('5.c')

        # ---- 5.d · Keep the negative strip at its true scale. Cost exceeds benefit.
        next_head = fixed(title('Force one trade too many'))
        negative_lot = fixed(Polygon(ax.c2p(40, 3.8), ax.c2p(41, 3.8), ax.c2p(41, 4.05), ax.c2p(40, 4.05),
            color=GUIDE, stroke_width=3, fill_color=GUIDE, fill_opacity=0.65))
        endpoint_dots = fixed(VGroup(Dot(ax.c2p(41, 3.8), radius=0.035, color=DEMAND),
                                    Dot(ax.c2p(41, 4.05), radius=0.035, color=SUPPLY)))
        negative_label = fixed(Tex(r'MC $>$ MB', color=INK,
            tex_to_color_map={'MC': SUPPLY, 'MB': DEMAND}).scale(0.60)
            .next_to(ax.c2p(41, 4.05), UP + RIGHT, buff=0.18))
        negative_caption = fixed(Tex('The next unit costs more than it is worth.', color=INK)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(head), FadeIn(next_head), FadeOut(marginal), FadeOut(boundary), run_time=0.35)
        head = next_head
        self.play(allocation_flags[40].animate.set_value(1), FadeIn(negative_lot),
                  FadeIn(endpoint_dots), FadeIn(negative_label), FadeIn(negative_caption), run_time=0.8)
        self.pause('5.d')

        # ---- 5.e · Undo that loss. The graph itself is the welfare argument.
        self.play(allocation_flags[40].animate.set_value(0), FadeOut(negative_lot), FadeOut(endpoint_dots),
                  FadeOut(negative_label), FadeOut(negative_caption), run_time=0.6)
        next_head = fixed(title('The First Welfare Theorem'))
        theorem = fixed(Tex('Competitive equilibrium maximizes total surplus.', color=DEFINITION)
                        .scale(DEFINITION_SCALE))
        conditions = fixed(Tex('Price-taking, voluntary trade, and all benefits and costs counted.', color=CAPTION)
                           .scale(DEFINITION_SCALE))
        VGroup(theorem, conditions).arrange(DOWN, buff=0.10).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeOut(head), FadeIn(next_head), FadeIn(theorem), FadeIn(conditions), run_time=0.7)
        head = next_head
        self.pause('5.e')

        # Exercises follow the completed argument. Reuse B3's reference-card style.
        cover = fixed(Rectangle(width=16, height=8, stroke_width=0, fill_color=BG, fill_opacity=1))
        card_text = fixed(VGroup(
            Tex('Exercise B4 $|$ Q2: A Price Floor', color=DEFINITION).scale(1.1),
            Tex(r'$P=12-Q_d/2\qquad\qquad P=2+Q_s/2$', color=INK).scale(0.95),
            Tex('Pumpkin pasties: equilibrium is 10 pasties at 7 galleons.', color=INK).scale(0.82),
            Tex('Minimum legal price: 9 galleons. Demand: 6; supply: 14.', color=INK).scale(0.82),
            Tex('a) How many pasties are exchanged?', color=INK).scale(0.88),
            Tex('b) What is producer surplus?', color=INK).scale(0.88),
            Tex('c) What is deadweight loss?', color=INK).scale(0.88),
            Tex('d) Would a floor of 6 galleons change the market?', color=INK).scale(0.88))
            .arrange(DOWN, buff=0.29, aligned_edge=LEFT).move_to(ORIGIN))
        card_panel = fixed(RoundedRectangle(width=13, height=card_text.get_height() + 1.2,
            corner_radius=0.25, color=MUTED, stroke_width=2, fill_color=BG, fill_opacity=1).move_to(card_text))
        card_text.align_to(card_panel, LEFT).shift(RIGHT * 0.65)
        card_text[1].set_x(card_panel.get_x())
        for paragraph in card_text[2:]:
            paragraph.shift(RIGHT * 0.35)
        card_panel.set_z_index(50)
        for glyph in card_text.get_family():
            glyph.set_z_index(51)
        exercise = fixed(VGroup(cover, card_panel, card_text))
        self.play(FadeIn(exercise), run_time=0.5)
        self.pause('6.exercise_floor')
        self.play(FadeOut(exercise), run_time=0.3)

        card_text = fixed(VGroup(
            Tex('Exercise B4 $|$ Q1: A Price Ceiling', color=DEFINITION).scale(1.1),
            Tex(r'$P=12-Q_d/2\qquad\qquad P=2+Q_s/2$', color=INK).scale(0.95),
            Tex('Pumpkin pasties: equilibrium is 10 pasties at 7 galleons.', color=INK).scale(0.82),
            Tex('Maximum legal price: 5 galleons. Demand: 14; supply: 6.', color=INK).scale(0.82),
            Tex('a) How many pasties are exchanged?', color=INK).scale(0.88),
            Tex('b) What is consumer surplus?', color=INK).scale(0.88),
            Tex('c) What is producer surplus?', color=INK).scale(0.88),
            Tex('d) What is deadweight loss?', color=INK).scale(0.88),
            Tex('e) Plot demand, supply, and the ceiling; shade CS, PS, and DWL.', color=INK).scale(0.82))
            .arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(ORIGIN))
        card_panel = fixed(RoundedRectangle(width=13, height=card_text.get_height() + 1.2,
            corner_radius=0.25, color=MUTED, stroke_width=2, fill_color=BG, fill_opacity=1).move_to(card_text))
        card_text.align_to(card_panel, LEFT).shift(RIGHT * 0.65)
        card_text[1].set_x(card_panel.get_x())
        for paragraph in card_text[2:]:
            paragraph.shift(RIGHT * 0.35)
        card_panel.set_z_index(50)
        for glyph in card_text.get_family():
            glyph.set_z_index(51)
        exercise = fixed(VGroup(cover, card_panel, card_text))
        self.play(FadeIn(exercise), run_time=0.5)
        self.pause('6.exercise_ceiling')
        self.play(FadeOut(exercise), run_time=0.3)

        # ---- 7.a · Efficiency is the sum, not a verdict on distribution.
        closing_head = fixed(title('Efficiency and distribution'))
        closing = fixed(Tex('The largest total gain does not settle how it should be shared.', color=INK)
                        .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeOut(head), FadeIn(closing_head), FadeOut(theorem), FadeOut(conditions), FadeIn(closing), run_time=0.6)
        self.pause('7.a')
