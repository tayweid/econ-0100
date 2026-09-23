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
        claim = fixed(Tex(r'$MC < P < MB$', color=DEFINITION).scale(0.95))
        claim.move_to([0, -2.75, 0])
        endpoint_note = fixed(Tex('At an endpoint, one person is indifferent.', color=CAPTION).scale(0.65))
        endpoint_note.move_to([0, -3.30, 0])
        unit = fixed(Tex('One pound', color=CAPTION).scale(0.65).move_to([0, -3.72, 0]))
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
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
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
            .set_x(0).to_edge(DOWN, buff=0.18))
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
                               color=DEFINITION).scale(0.85).move_to([0, -2.85, 0]))
        counts = fixed(Tex(r'At $\$6.25$: 1 willing buyer, 1 seller.', color=CAPTION)
                       .scale(0.75).move_to([0, -3.45, 0]))
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
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
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
        equal_prices = fixed(Tex(r'Both trades: $\$5.50$.', color=GUIDE).scale(0.8)
                             .move_to([0, -3.15, 0]))
        equal_counts = fixed(Tex('2 willing buyers; 2 sellers.', color=CAPTION).scale(0.7)
                             .move_to([0, -3.65, 0]))
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
        one_lot.scale(0.77).move_to([0, -3.40, 0])
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
        rule.scale(0.72).move_to([0, -3.40, 0])
        self.play(ReplacementTransform(one_lot, rule), full_people[29][1].animate.set_color(FOCUS))
        self.pause('1.c.buyers')
        self.play(full_people[29][1].animate.set_color(DEMAND), price.animate.set_value(3), run_time=2.0, rate_func=smooth)
        low = fixed(Tex(r'At $\$3$, 45 buyers are willing. We have not counted trades.', color=INK))
        low.scale(0.72).move_to([0, -3.40, 0])
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
        one_lot.scale(0.77).move_to([0, -3.40, 0])
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
        rule.scale(0.72).move_to([0, -3.40, 0])
        self.play(ReplacementTransform(one_lot, rule))
        self.pause('1.c.sellers')
        self.play(price.animate.set_value(6), run_time=2.0, rate_func=smooth)
        high = fixed(Tex(r'At $\$6$, 80 sellers are willing. A higher price brings more sellers.', color=INK))
        high.scale(0.72).move_to([0, -3.40, 0])
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

        # Both plots begin on the totem's price scale: merging needs only a move.
        totem_zero = screen_point(self.camera.frame, [4.8, 0, 0.035])
        totem_twelve = screen_point(self.camera.frame, [4.8, 0, 0.035 + 12 * 0.28])
        graph_price_height = (totem_twelve[1] - totem_zero[1]) * 13 / 12
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

        # Persistent quantity spans: match the counted people to their graph baselines.
        gap_count = ValueTracker(25)
        gap_count.price, gap_count.mb, gap_count.mc = price, BUYER_MB, SELLER_MC
        gap_count.add_updater(lambda m: m.set_value(abs(
            np.count_nonzero(m.mb + 1e-7 >= m.price.get_value())
            - np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))))
        self.add(gap_count)
        buyer_quantity = VGroup(VMobject(color=DEMAND, stroke_width=3), VMobject(color=DEMAND, stroke_width=3))
        seller_quantity = VGroup(VMobject(color=SUPPLY, stroke_width=3), VMobject(color=SUPPLY, stroke_width=3))
        waiting_gap = VMobject(color=FOCUS, stroke_width=4)
        for line in [*buyer_quantity, *seller_quantity, waiting_gap]:
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
            waiting_by_side = []
            for paths, people, quantity, side in [(m[0], m.buyers, qd, 1), (m[1], m.sellers, qs, -1)]:
                points = [person.get_center() for person in people[:quantity]]
                # Use actual positions, including the illustrative partner switch.
                paired = sorted([p for p in points if abs(p[1]) < 1], key=lambda p: p[0])
                waiting = sorted([p for p in points if abs(p[1]) >= 1], key=lambda p: p[0])
                waiting_by_side.append(waiting)
                for path, run in zip(paths, [paired, waiting]):
                    if run:
                        line_points = [p + np.array([0, -side * 0.18, 0.015]) for p in run]
                        if len(line_points) == 1:
                            line_points = [line_points[0] + LEFT * 0.05, line_points[0] + RIGHT * 0.05]
                        path.set_points_as_corners(line_points)
                    path.set_stroke(opacity=m.counts.get_value() if run else 0)
            side = 1 if qd > qs else -1
            waiting = waiting_by_side[0 if side == 1 else 1]
            visible = m.counts.get_value() if qd != qs and waiting and m.trades.get_value() > 0.999 else 0
            if waiting:
                gap_points = [p + np.array([0, -side * 0.38, 0.02]) for p in waiting]
                if len(gap_points) == 1:
                    gap_points = [gap_points[0] + LEFT * 0.05, gap_points[0] + RIGHT * 0.05]
                m[2].set_points_as_corners(gap_points)
                middle = gap_points[len(gap_points) // 2]
                m[5].move_to(middle + np.array([0.55, -side * 0.48, 0.12]))
                m[3].next_to(m[5], LEFT, buff=0.10)
                m[4].next_to(m[5], LEFT, buff=0.10)
            m[2].set_stroke(opacity=visible)
            m[3].set_opacity(visible if side == 1 else 0)
            m[4].set_opacity(visible if side == -1 else 0)
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
        head = fixed(title(r'At $\$3$, who can trade?'))
        self.add(head, crowd, crowd_marks, graphs)
        self.pause('1.d')

        # ---- 1.e · Willingness first, matching second.
        self.play(show_counts.animate.set_value(1), show_buyers.animate.set_value(1),
                  show_sellers.animate.set_value(1), run_time=0.8)
        # Keep quantity lines through matching; yellow marks the unserved remainder.
        self.play(show_trades.animate.set_value(1), run_time=1.1)
        shortage = fixed(Tex(r'20 pairs trade. 25 willing buyers are still waiting.', color=INK))
        shortage.scale(0.76).move_to([0, -3.65, 0])
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
        ag_head = fixed(title('What would this buyer do?'))
        self.play(ReplacementTransform(head, ag_head))
        head = ag_head
        ag_focus = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(buyer_circles[24].get_center())
        bid = DashedLine(buyer_circles[24].get_center(), seller_circles[19].get_center(), color=GUIDE, stroke_width=2)
        seller_gain = fixed(Tex(r'Seller receives $\$0.25$ more per lb', color=SUPPLY)).scale(0.52).move_to([-3.3, -1.35, 0])
        self.play(Create(ag_focus), Create(bid), FadeOut(units), FadeIn(seller_gain))

        self.play(FadeOut(ag_focus), FadeOut(bid), FadeOut(seller_gain))

        # B3 2.a.i: the same head-on camera, close bars, and material people.
        buy_person = buyer_people[24].copy().clear_updaters()
        buy_counterparty = seller_people[19].copy().clear_updaters()
        buy_mb = buyer_bars[24].copy().clear_updaters()
        buy_mc = seller_bars[19].copy().clear_updaters()
        buy_detail = Group(buy_person, buy_counterparty, buy_mb, buy_mc)
        self.add(buy_detail)
        buy_targets = []
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            shadow = Disk3D(radius=0.28, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(12, 8)).move_to([x, 0, 0.32])
            buy_targets.append(Group(shadow, orb))
        buy_mb_target = Rectangle3D(width=1.10, height=7 * 0.55, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        buy_mb_target.rotate(90 * DEGREES, RIGHT).move_to([-0.61, 0, 0.75 + 7 * 0.55 / 2])
        buy_mc_target = Rectangle3D(width=1.10, height=3 * 0.55, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        buy_mc_target.rotate(90 * DEGREES, RIGHT).move_to([0.61, 0, 0.75 + 3 * 0.55 / 2])
        crowd.suspend_updating()
        crowd_marks.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(graphs),
                  Transform(buy_person, buy_targets[0]), Transform(buy_counterparty, buy_targets[1]),
                  Transform(buy_mb, buy_mb_target), Transform(buy_mc, buy_mc_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        buy_zero = Line([-1.31, -0.02, 0.75], [1.31, -0.02, 0.75], color=MUTED, stroke_width=1.5)
        buy_price = Line([-1.16, -0.045, 0.75 + 3 * 0.55], [1.16, -0.045, 0.75 + 3 * 0.55], color=GUIDE, stroke_width=3)
        buy_proposal = DashedLine([-1.16, -0.055, 0.75 + 3.25 * 0.55], [1.16, -0.055, 0.75 + 3.25 * 0.55], color=GUIDE, stroke_width=3)
        buy_values = VGroup()
        for text, color, at, edge in [
                (r'MB $\$7$', DEMAND, [-1.34, 0, 0.75 + 7 * 0.55 - 0.09], RIGHT),
                (r'MC $\$3$', SUPPLY, [1.34, 0, 0.75 + 3 * 0.55], LEFT)]:
            label = Tex(text, color=color).scale(0.56)
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
            buy_values.add(label)
        # Choices live beside the price lines, in the same world plane as the bars.
        stay_text = Tex(r'Wait at $\$3$: gain $\$0$', color=CAPTION).scale(0.65)
        bid_text = Tex(r'Offer $\$3.25$: gain $\$3.75$/lb', color=INK).scale(0.65)
        for label, at, edge in [(stay_text, [-2.15, -0.07, 1.75], RIGHT),
                                (bid_text, [2.15, -0.07, 3.15], LEFT)]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
        wait_arrow = Arrow([-1.95, 1.75, 0], [-1.16, 0.75 + 3 * 0.55, 0],
                           buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        bid_arrow = Arrow([1.95, 3.15, 0], [1.16, 0.75 + 3.25 * 0.55, 0],
                          buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        for arrow in [wait_arrow, bid_arrow]:
            arrow.rotate(90 * DEGREES, RIGHT, about_point=ORIGIN).shift(DOWN * 0.07)
        self.play(Create(buy_zero), Create(buy_price), Create(buy_proposal), FadeIn(buy_values),
                  FadeIn(stay_text), FadeIn(bid_text), Create(wait_arrow), Create(bid_arrow))
        self.pause('1.f')
        self.play(buy_price.animate.set_z(0.75 + 3.25 * 0.55), FadeOut(buy_proposal),
                  FadeOut(stay_text), FadeOut(wait_arrow), bid_text.animate.set_color(GREEN), run_time=0.7)
        self.play(FadeOut(buy_detail), FadeOut(buy_zero), FadeOut(buy_price), FadeOut(buy_values),
                  FadeOut(bid_text), FadeOut(bid_arrow),
                  self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.3)
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_marks.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_marks, graphs)
        self.remove(units)
        seller_gain.move_to([-3.3, -1.35, 0])
        self.add(ag_focus, bid, seller_gain)
        # One illustrative switch is not an additional sale. Qx remains 20.
        for n in [19, 24]:
            buyer_people[n].suspend_updating()
            buyer_bars[n].suspend_updating()
            buyer_circles[n].suspend_updating()
        ag_pair = buyer_circles[19].pair_home.copy()
        accepted_bid = Line(ag_pair, seller_circles[19].get_center(), color=GREEN, stroke_width=2)
        self.play(ReplacementTransform(bid, accepted_bid),
                  ag_focus.animate.set_width(0.044).move_to(ag_pair),
                  buyer_people[19].animate.set_width(buyer_people[19].home_width).move_to(buyer_people[19].home),
                  buyer_bars[19].animate.set_width(buyer_bars[19].home_width, stretch=True).move_to(buyer_bars[19].home),
                  buyer_circles[19].animate.set_width(0.070).move_to(buyer_circles[19].home).set_stroke(opacity=0),
                  buyer_people[24].animate.set_width(buyer_people[24].paired_width).move_to([ag_pair[0], ag_pair[1], buyer_people[24].pair_home[2]]),
                  buyer_bars[24].animate.set_width(0.055, stretch=True).move_to([ag_pair[0], ag_pair[1], buyer_bars[24].home[2]]),
                  buyer_circles[24].animate.set_width(0.036).move_to(ag_pair).set_stroke(opacity=0), run_time=0.8)
        everyone = fixed(Tex('Other unserved buyers have the same incentive.', color=INK)).scale(0.79).move_to([0, -3.55, 0])
        self.play(FadeOut(accepted_bid), FadeOut(ag_focus), FadeOut(seller_gain), FadeIn(everyone))
        # Resume sorted common-price snapshots after the individual illustration.
        self.play(buyer_people[24].animate.set_width(buyer_people[24].home_width).move_to(buyer_people[24].home),
                  buyer_bars[24].animate.set_width(buyer_bars[24].home_width, stretch=True).move_to(buyer_bars[24].home),
                  buyer_circles[24].animate.set_width(0.070).move_to(buyer_circles[24].home).set_stroke(opacity=0),
                  buyer_people[19].animate.set_width(buyer_people[19].paired_width).move_to(buyer_people[19].pair_home),
                  buyer_bars[19].animate.set_width(0.055, stretch=True).move_to(buyer_bars[19].pair_home),
                  buyer_circles[19].animate.set_width(0.036).move_to(buyer_circles[19].pair_home).set_stroke(opacity=0), run_time=0.5)
        for n in [19, 24]:
            buyer_people[n].resume_updating()
            buyer_bars[n].resume_updating()
            buyer_circles[n].resume_updating()
        self.add(units)
        tried_low = VGroup(*[DashedLine(ax.c2p(0, 3), ax.c2p(q, 3), color=GUIDE, stroke_width=1).set_opacity(0.25) for ax, q in [(demand_axes, 45), (supply_axes, 20)]])
        fixed(tried_low)
        self.add(tried_low)
        self.play(price.animate.set_value(4), run_time=3.0, rate_func=linear)
        rising = fixed(Tex(r'Shortage $\longrightarrow$ price rises. The counts meet.', color=INK)).scale(0.8).move_to([0, -3.55, 0])
        self.play(ReplacementTransform(everyone, rising))

        # ---- 1.g · Predict the other direction before revealing its counts.
        self.play(FadeOut(rising), show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0), show_sellers.animate.set_value(0))
        self.play(price.animate.set_value(6), run_time=1.0)
        high_head = fixed(title(r'At $\$6$, who is left out?'))
        self.play(ReplacementTransform(head, high_head))
        head = high_head
        self.pause('1.g')

        # ---- 1.h · Andrew can attract a buyer by asking less.
        self.play(show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1))
        excess = fixed(Tex(r'Excess: 50,000 lb. This seller is willing, but has no buyer.', color=INK)).scale(0.65).move_to([-3.3, -1.35, 0])
        self.remove(units)
        andrew_focus = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(seller_circles[39].get_center())
        cut = DashedLine(seller_circles[39].get_center(), buyer_circles[29].get_center(), color=GUIDE, stroke_width=2)
        self.play(FadeIn(excess), Create(andrew_focus), Create(cut))

        andrew_head = fixed(title('What would this seller do?'))
        self.play(FadeOut(andrew_focus), FadeOut(cut), FadeOut(tried_low), ReplacementTransform(head, andrew_head))
        head = andrew_head

        # B3 2.a.i: the same head-on camera, close bars, and material people.
        sell_person = buyer_people[29].copy().clear_updaters()
        sell_counterparty = seller_people[39].copy().clear_updaters()
        sell_mb = buyer_bars[29].copy().clear_updaters()
        sell_mc = seller_bars[39].copy().clear_updaters()
        sell_detail = Group(sell_person, sell_counterparty, sell_mb, sell_mc)
        self.add(sell_detail)
        sell_targets = []
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            shadow = Disk3D(radius=0.28, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(12, 8)).move_to([x, 0, 0.32])
            sell_targets.append(Group(shadow, orb))
        sell_mb_target = Rectangle3D(width=1.10, height=6 * 0.55, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        sell_mb_target.rotate(90 * DEGREES, RIGHT).move_to([-0.61, 0, 0.75 + 6 * 0.55 / 2])
        sell_mc_target = Rectangle3D(width=1.10, height=4 * 0.55, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        sell_mc_target.rotate(90 * DEGREES, RIGHT).move_to([0.61, 0, 0.75 + 4 * 0.55 / 2])
        crowd.suspend_updating()
        crowd_marks.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(graphs), FadeOut(excess),
                  Transform(sell_person, sell_targets[0]), Transform(sell_counterparty, sell_targets[1]),
                  Transform(sell_mb, sell_mb_target), Transform(sell_mc, sell_mc_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        sell_zero = Line([-1.31, -0.02, 0.75], [1.31, -0.02, 0.75], color=MUTED, stroke_width=1.5)
        sell_price = Line([-1.16, -0.045, 0.75 + 6 * 0.55], [1.16, -0.045, 0.75 + 6 * 0.55], color=GUIDE, stroke_width=3)
        sell_proposal = DashedLine([-1.16, -0.055, 0.75 + 5.75 * 0.55], [1.16, -0.055, 0.75 + 5.75 * 0.55], color=GUIDE, stroke_width=3)
        sell_values = VGroup()
        for text, color, at, edge in [
                (r'MB $\$6$', DEMAND, [-1.34, 0, 0.75 + 6 * 0.55 - 0.09], RIGHT),
                (r'MC $\$4$', SUPPLY, [1.34, 0, 0.75 + 4 * 0.55], LEFT)]:
            label = Tex(text, color=color).scale(0.56)
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to(at, aligned_edge=edge)
            sell_values.add(label)
        # Separate the callouts vertically so the two nearby red levels stay legible.
        stay_text = Tex(r'Keep $\$6$: gain $\$0$', color=CAPTION).scale(0.65)
        cut_text = Tex(r'Ask $\$5.75$: gain $\$1.75$/lb', color=INK).scale(0.65)
        for label, height in [(stay_text, 4.65), (cut_text, 3.40)]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            label.move_to([2.15, -0.07, height], aligned_edge=LEFT)
        keep_arrow = Arrow([1.95, 4.65, 0], [1.16, 0.75 + 6 * 0.55, 0],
                           buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        cut_arrow = Arrow([1.95, 3.40, 0], [1.16, 0.75 + 5.75 * 0.55, 0],
                          buff=0, color=GUIDE, thickness=1.4, tip_width_ratio=4)
        for arrow in [keep_arrow, cut_arrow]:
            arrow.rotate(90 * DEGREES, RIGHT, about_point=ORIGIN).shift(DOWN * 0.07)
        self.play(Create(sell_zero), Create(sell_price), Create(sell_proposal), FadeIn(sell_values),
                  FadeIn(stay_text), FadeIn(cut_text), Create(keep_arrow), Create(cut_arrow))
        self.pause('1.h')
        self.play(sell_price.animate.set_z(0.75 + 5.75 * 0.55), FadeOut(sell_proposal),
                  FadeOut(stay_text), FadeOut(keep_arrow), cut_text.animate.set_color(GREEN), run_time=0.7)
        self.play(FadeOut(sell_detail), FadeOut(sell_zero), FadeOut(sell_price), FadeOut(sell_values),
                  FadeOut(cut_text), FadeOut(cut_arrow),
                  self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.3)
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_marks.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_marks, graphs)
        self.remove(units)
        self.remove(excess)
        self.add(andrew_focus, cut, tried_low)
        for mob in [buyer_people[29], buyer_bars[29], buyer_circles[29],
                    seller_people[29], seller_bars[29], seller_circles[29],
                    seller_people[39], seller_bars[39], seller_circles[39]]:
            mob.suspend_updating()
        gary_pair = buyer_circles[29].pair_home.copy()
        accepted_cut = Line(gary_pair, seller_circles[29].pair_home, color=GREEN, stroke_width=2)
        self.play(ReplacementTransform(cut, accepted_cut),
                  andrew_focus.animate.set_width(0.044).move_to(seller_circles[29].pair_home),
                  buyer_people[29].animate.move_to([gary_pair[0], gary_pair[1], buyer_people[29].pair_home[2]]),
                  buyer_bars[29].animate.move_to([gary_pair[0], gary_pair[1], buyer_bars[29].home[2]]),
                  buyer_circles[29].animate.move_to(gary_pair),
                  seller_people[29].animate.set_width(seller_people[29].home_width).move_to(seller_people[29].home),
                  seller_bars[29].animate.set_width(seller_bars[29].home_width, stretch=True).move_to(seller_bars[29].home),
                  seller_circles[29].animate.set_width(0.070).move_to(seller_circles[29].home).set_stroke(opacity=0),
                  seller_people[39].animate.set_width(seller_people[39].paired_width).move_to(seller_people[29].pair_home),
                  seller_bars[39].animate.set_width(0.055, stretch=True).move_to(
                      [seller_bars[29].pair_home[0], seller_bars[29].pair_home[1], seller_bars[39].home[2]]),
                  seller_circles[39].animate.set_width(0.036).move_to(seller_circles[29].pair_home).set_stroke(opacity=0), run_time=0.8)
        everyone = fixed(Tex('Other unserved sellers have the same incentive.', color=INK)).scale(0.79).move_to([0, -3.55, 0])
        self.play(FadeOut(andrew_focus), FadeOut(accepted_cut), FadeIn(everyone))
        self.play(buyer_people[29].animate.move_to(buyer_people[29].pair_home),
                  buyer_bars[29].animate.move_to(buyer_bars[29].pair_home),
                  buyer_circles[29].animate.move_to(buyer_circles[29].pair_home),
                  seller_people[29].animate.set_width(seller_people[29].paired_width).move_to(seller_people[29].pair_home),
                  seller_bars[29].animate.set_width(0.055, stretch=True).move_to(seller_bars[29].pair_home),
                  seller_circles[29].animate.set_width(0.036).move_to(seller_circles[29].pair_home).set_stroke(opacity=0),
                  seller_people[39].animate.set_width(seller_people[39].home_width).move_to(seller_people[39].home),
                  seller_bars[39].animate.set_width(seller_bars[39].home_width, stretch=True).move_to(seller_bars[39].home),
                  seller_circles[39].animate.set_width(0.070).move_to(seller_circles[39].home).set_stroke(opacity=0), run_time=0.5)
        for mob in [buyer_people[29], buyer_bars[29], buyer_circles[29],
                    seller_people[29], seller_bars[29], seller_circles[29],
                    seller_people[39], seller_bars[39], seller_circles[39]]:
            mob.resume_updating()
        self.add(units)
        tried_high = VGroup(*[DashedLine(ax.c2p(0, 6), ax.c2p(q, 6), color=GUIDE, stroke_width=1).set_opacity(0.25) for ax, q in [(demand_axes, 30), (supply_axes, 80)]])
        fixed(tried_high)
        self.add(tried_high)
        self.play(price.animate.set_value(4), run_time=3.0, rate_func=linear)

        # ---- 1.i · Counts and incentives are two views of the same condition.
        eq_head = fixed(title(r'Why does $\$4$ hold?'))
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
        test_question = fixed(Tex(r'Would $\$4.25$ hold?', color=DEFINITION)).scale(0.85).move_to([0, -3.55, 0])
        self.play(FadeOut(equilibrium), FadeIn(proposed), FadeIn(test_question))
        self.pause('1.i.stability')
        self.play(FadeOut(proposed), price.animate.set_value(4.25), run_time=1.0)
        excess_test = fixed(Tex('Seven willing sellers have no buyer. They can undercut.', color=INK)).scale(0.78).move_to([0, -3.55, 0])
        self.play(ReplacementTransform(test_question, excess_test))
        self.wait(0.8)
        self.play(price.animate.set_value(4), run_time=1.0)
        self.play(price.animate.set_value(3.75), run_time=1.0)
        shortage_test = fixed(Tex('Six willing buyers have no seller. They can offer more.', color=INK)).scale(0.78).move_to([0, -3.55, 0])
        self.play(ReplacementTransform(excess_test, shortage_test))
        self.wait(0.8)
        self.play(price.animate.set_value(4), run_time=1.0)
        stable = fixed(Tex(r'Above $\$4$: excess. Below $\$4$: shortage.', color=INK)).scale(0.83).move_to([0, -3.55, 0])
        self.play(ReplacementTransform(shortage_test, stable))
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

        # Both plots begin on the totem's price scale: merging needs only a move.
        totem_zero = screen_point(self.camera.frame, [4.8, 0, 0.035])
        totem_twelve = screen_point(self.camera.frame, [4.8, 0, 0.035 + 12 * 0.28])
        graph_price_height = (totem_twelve[1] - totem_zero[1]) * 13 / 12
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
        demand_shift = totem_zero - demand_axes.c2p(0, 0)
        supply_shift = totem_zero - supply_axes.c2p(0, 0)
        self.play(demand_plot.animate.shift(demand_shift),
                  supply_plot.animate.shift(supply_shift), run_time=2.0, rate_func=smooth)

        # The totem is the shared vertical price axis while the plaza is present.
        merged_axes, merged_demand, merged_supply = demand_axes, demand_steps, supply_steps
        merged_price, merged_drop = graph_prices[0], demand_guide
        self.play(FadeOut(supply_axes), FadeOut(supply_ticks), FadeOut(supply_guide),
                  FadeOut(graph_prices[1]), FadeOut(counts[1]),
                  demand_axes.y_axis.animate.set_opacity(0),
                  FadeOut(VGroup(*demand_ticks[6:])), FadeOut(current_price),
                  post_numbers[1].animate.set_color(GUIDE), run_time=0.35)
        counts[0].set_color(CAPTION)
        merged_ticks = fixed(VGroup(*demand_ticks[:6], counts[0]))
        merged_dot = fixed(Dot(merged_axes.c2p(40, 4), radius=0.055, color=GUIDE))
        merged_labels = fixed(VGroup(
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
        graph_price_ticks = fixed(VGroup(*[
            Tex(str(p), color=GUIDE if p == 4 else CAPTION).scale(0.40)
                .next_to(merged_axes.c2p(0, p), LEFT, buff=0.10) for p in [4, 8, 12]]))
        graph_price_heading = fixed(Tex(r'Price (\$/lb)', color=CAPTION)).scale(0.48)
        graph_price_heading.next_to(merged_axes.c2p(0, 13), UP, buff=0.16, aligned_edge=LEFT)
        crowd.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_marks), FadeOut(same),
                  merged_axes.y_axis.animate.set_opacity(1),
                  FadeIn(graph_price_ticks), FadeIn(graph_price_heading))
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
        final = fixed(Tex(r'40,000 pounds at $\$4$ per pound.', color=INK)).scale(0.9).move_to([0, -3.45, 0])
        self.play(FadeIn(final))
        self.pause('1.i.algebra')

        # ========== 8. Welfare ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(PLAZA_CENTER).set_height(11)
        MB = np.array([12 - n / 5 for n in range(1, 60)])
        MC = np.array([2 + n / 20 for n in range(1, 101)])
        LOT = 1000
        BOTTOM_SCALE = 0.7443
        PRICE, EQUILIBRIUM_Q = 4, 40
        BAR_BASE, DOLLAR_HEIGHT = 0.18, 0.19
        ROW_LEFT, ROW_WIDTH = -3.7, 7.4
        RANK_STEP = ROW_WIDTH / (max(len(MB), len(MC)) - 1)
        body_radii = {'B': 0.026, 'S': 0.026}
        ring_radii = {'B': 0.035, 'S': 0.035}

        # Independent opening: the same $4 market, already on merged axes.
        head = fixed(title('Could we do better?'))
        units = fixed(Tex(r'One person: 1,000 lb\quad Bars: dollars/lb', color=CAPTION))
        units.scale(0.55).move_to([-3.3, -2.90, 0])
        buyers_label = Tex('Buyers: highest MB first', color=DEMAND).scale(0.65 * self.camera.frame.get_scale())
        buyers_label.move_to(self.camera.frame.from_fixed_frame_point([-3.3, 2.65, 0]))
        sellers_label = Tex('Sellers: lowest MC first', color=SUPPLY).scale(0.65 * self.camera.frame.get_scale())
        sellers_label.move_to(self.camera.frame.from_fixed_frame_point([-3.3, -2.55, 0]))
        for label in [buyers_label, sellers_label]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        bodies, bars, rings, checks = {}, {}, {}, {}
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        crowd = Group(floor, rim)
        crowd_words = VGroup(buyers_label, sellers_label, units)
        market_checks = VGroup()
        home_positions = {}
        allocation = {n: n for n in range(1, 41)}
        for side, values, color, y, shadow_radius, body_z, bar_width, ring_width, check_width, check_points in [
                ('B', MB, DEMAND, 2.0, 0.037, 0.055, 0.058, 1.0, 1.1,
                 [[-0.015, 0, 0], [-0.003, -0.013, 0], [0.02, 0.02, 0]]),
                ('S', MC, SUPPLY, -1.7, 0.037, 0.055, 0.058, 1.0, 1.1,
                 [[-0.015, 0, 0], [-0.003, -0.013, 0], [0.02, 0.02, 0]])]:
            for i, value in enumerate(values):
                home_positions[side, i + 1] = np.array([ROW_LEFT + i * RANK_STEP, y, 0])
                matched = i + 1 in (allocation if side == 'B' else allocation.values())
                station = allocation.get(i + 1, i + 1) if side == 'B' else i + 1
                x = ROW_LEFT + (station - 1) * RANK_STEP + ((-0.019 if side == 'B' else 0.019) if matched else 0)
                pose_y = -1.7 if matched else y
                radius = 0.014 if matched else 0.026
                shadow = Disk3D(radius=shadow_radius * radius / 0.026, resolution=(2, 16), shading=(0, 0, 0),
                                opacity=0.28).set_color(color).move_to([x, pose_y, 0.025])
                orb = Sphere(radius=radius, color=color, resolution=(12, 8)).move_to([x, pose_y, 0.043 if matched else body_z])
                body = Group(shadow, orb)
                body.orb_unit_width = orb.get_width() / radius
                bar = Rectangle3D(width=0.030 if matched else bar_width, height=value * DOLLAR_HEIGHT,
                                  resolution=(2, 2), opacity=0.65).set_color(color)
                bar.rotate(90 * DEGREES, RIGHT).move_to([x, pose_y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
                ring = Circle(radius=0.018 if matched else ring_radii[side], color=GOV, stroke_width=ring_width).move_to([x, pose_y, 0.045])
                ring.set_stroke(opacity=1 if i < EQUILIBRIUM_Q else 0).set_fill(opacity=0)
                check = (VMobject(color=color, stroke_width=check_width).set_points_as_corners(check_points))
                check.anchor, check.value, check.dollar_height = bar, value, DOLLAR_HEIGHT
                check.scale(self.camera.frame.get_scale())
                check.face_mat = np.eye(3)
                check.add_updater(face_camera)
                check.add_updater(lambda m: m.move_to(
                    m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10)).set_fill(opacity=0))
                check.set_stroke(opacity=1 if i < EQUILIBRIUM_Q else 0).set_fill(opacity=0)
                bodies[side, i + 1], bars[side, i + 1] = body, bar
                rings[side, i + 1], checks[side, i + 1] = ring, check
                crowd.add(body, bar, ring)
                market_checks.add(check)
        ax = axes((0, 100, 20), (0, 13, 2), x_length=5.15, y_length=3.8)
        ax.move_to([4.48, 0.45, 0])
        p_label = fixed(Tex('Dollars per pound', color=CAPTION)).scale(0.48).next_to(ax.c2p(0, 13), UP, buff=0.16, aligned_edge=LEFT)
        q_label = fixed(VGroup())
        graph_units = fixed(Tex(r'$Q$: thousands of pounds', color=CAPTION)).scale(0.5)
        graph_units.next_to(ax.c2p(50, 0), DOWN, buff=0.32)
        ticks = VGroup()
        for q in [20, 40, 60, 80, 100]:
            ticks.add(fixed(Tex(str(q), color=CAPTION)).scale(0.43).next_to(ax.c2p(q, 0), DOWN, buff=0.09))
        for p in [8, 12]:
            ticks.add(fixed(Tex(str(p), color=CAPTION)).scale(0.43).next_to(ax.c2p(0, p), LEFT, buff=0.12))
        demand_points, supply_points = [], []
        for n, value in enumerate(MB, start=1):
            demand_points.extend([ax.c2p(n - 1, value), ax.c2p(n, value)])
        for n, value in enumerate(MC, start=1):
            supply_points.extend([ax.c2p(n - 1, value), ax.c2p(n, value)])
        demand = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=2.5)
        supply = Line(ax.c2p(0, 2), ax.c2p(100, 7), color=SUPPLY, stroke_width=2.5)
        fitted = VGroup()  # Exact lots remain visible in the area strips.
        curve_names = VGroup(fixed(Tex('D / MB', color=DEMAND)).scale(0.6).next_to(ax.c2p(10, 10), RIGHT, buff=0.14),
                             fixed(Tex('S / MC', color=SUPPLY)).scale(0.6).next_to(ax.c2p(84, 6.2), UP, buff=0.14))
        graph = VGroup(ax, p_label, q_label, graph_units, ticks, fitted, demand, supply, curve_names)
        price_line = DashedLine(ax.c2p(0, PRICE), ax.c2p(40, PRICE), color=GUIDE, stroke_width=2)
        price_line.put_start_and_end_on(ax.c2p(0, PRICE), ax.c2p(40, PRICE))
        price_read = fixed(Tex(r'\$4', color=GUIDE)).scale(0.65).next_to(ax.c2p(0, PRICE), LEFT, buff=0.3)
        quantity = ValueTracker(40)
        q_guide = DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=1.6).set_opacity(0.55)
        q_guide.add_updater(lambda m: set_dashed_endpoints(m,
            ax.c2p(quantity.get_value(), 0), ax.c2p(quantity.get_value(),
                max(12 - quantity.get_value() / 5, 2 + quantity.get_value() / 20))))
        cs_strips, ps_strips, gain_strips = VGroup(), VGroup(), VGroup()
        for n in range(1, 40):
            cs_strips.add(Polygon(ax.c2p(n - 1, 4), ax.c2p(n, 4),
                                  ax.c2p(n, MB[n - 1]), ax.c2p(n - 1, MB[n - 1]),
                                  stroke_width=0, fill_color=DEMAND, fill_opacity=AREA_OPACITY))
            ps_strips.add(Polygon(ax.c2p(n - 1, MC[n - 1]), ax.c2p(n, MC[n - 1]),
                                  ax.c2p(n, 4), ax.c2p(n - 1, 4),
                                  stroke_width=0, fill_color=SUPPLY, fill_opacity=AREA_OPACITY))
            gain_strips.add(Polygon(ax.c2p(n - 1, MC[n - 1]), ax.c2p(n, MC[n - 1]),
                                    ax.c2p(n, MB[n - 1]), ax.c2p(n - 1, MB[n - 1]),
                                    stroke_color=TOTAL, stroke_width=0.6,
                                    fill_color=TOTAL, fill_opacity=0))
        for mob in [graph, cs_strips, ps_strips, gain_strips, price_line, q_guide]:
            fixed(mob)
        self.add(head, crowd, crowd_words, market_checks, graph, cs_strips, ps_strips,
                 price_line, price_read, q_guide)

        # ---- 2.a · CS and PS are familiar; ask what could improve.
        self.play(cs_strips.animate.set_fill(opacity=0.55),
                  ps_strips.animate.set_fill(opacity=0.55), run_time=0.7)
        self.pause('2.a')

        # ---- 2.b · Total surplus is PS plus CS; keep this one trade fixed.
        self.play(*[mob.animate.set_opacity(0) for body in bodies.values() for mob in body],
                  *[bar.animate.set_opacity(0) for bar in bars.values()],
                  *[ring.animate.set_stroke(opacity=0).set_fill(opacity=0) for ring in rings.values()], FadeOut(crowd_words),
                  market_checks.animate.set_opacity(0),
                  FadeOut(graph), FadeOut(cs_strips), FadeOut(ps_strips), FadeOut(price_line), FadeOut(price_read),
                  FadeOut(q_guide), FadeOut(floor), FadeOut(rim), run_time=0.45)
        self.play(FadeOut(head), run_time=0.2)
        self.remove(*[mob for key in bodies if key not in [('B', 20), ('S', 20)]
                      for mob in [bodies[key], bars[key], rings[key]]])
        head = fixed(title('What is total surplus?'))
        self.play(FadeIn(head))
        self.play(self.camera.frame.animate.reorient(0, 90, center=[0, 0, 3.4], height=10.2), run_time=1.1)
        BASE, HEIGHT = 0.75, 0.55
        payment = ValueTracker(4)
        mb_bar, mc_bar = bars['B', 20], bars['S', 20]
        for mob in [mb_bar, mc_bar, bodies['B', 20], bodies['S', 20], rings['B', 20], rings['S', 20]]:
            mob.save_state()
        self.play(mb_bar.animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(8 * HEIGHT)
                  .move_to([-4.61, 0, BASE + 4 * HEIGHT]).set_opacity(0.13),
                  mc_bar.animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(3 * HEIGHT)
                  .move_to([-3.39, 0, BASE + 1.5 * HEIGHT]).set_opacity(0.13),
                  bodies['B', 20].animate.scale(0.23 * bodies['B', 20].orb_unit_width / bodies['B', 20][1].get_width()).move_to([-6, 0, 0.32]).set_opacity(1),
                  bodies['S', 20].animate.scale(0.23 * bodies['S', 20].orb_unit_width / bodies['S', 20][1].get_width()).move_to([-2, 0, 0.32]).set_opacity(1),
                  rings['B', 20].animate.scale(0.58 / rings['B', 20].get_width()).move_to([-6, 0, 0.045]).set_stroke(opacity=1).set_fill(opacity=0),
                  rings['S', 20].animate.scale(0.58 / rings['S', 20].get_width()).move_to([-2, 0, 0.045]).set_stroke(opacity=1).set_fill(opacity=0), run_time=1.2)
        cs_fill = Polygon([-5.16, -0.025, BASE + 4 * HEIGHT], [-4.06, -0.025, BASE + 4 * HEIGHT],
                          [-4.06, -0.025, BASE + 8 * HEIGHT], [-5.16, -0.025, BASE + 8 * HEIGHT],
                          stroke_width=0, fill_color=DEMAND, fill_opacity=0.55)
        cs_fill.add_updater(lambda m: m.set_points_as_corners([
            [-5.16, -0.025, BASE + payment.get_value() * HEIGHT],
            [-4.06, -0.025, BASE + payment.get_value() * HEIGHT],
            [-4.06, -0.025, BASE + 8 * HEIGHT], [-5.16, -0.025, BASE + 8 * HEIGHT],
            [-5.16, -0.025, BASE + payment.get_value() * HEIGHT]]))
        ps_fill = Polygon([-3.94, -0.025, BASE + 3 * HEIGHT], [-2.84, -0.025, BASE + 3 * HEIGHT],
                          [-2.84, -0.025, BASE + 4 * HEIGHT], [-3.94, -0.025, BASE + 4 * HEIGHT],
                          stroke_width=0, fill_color=SUPPLY, fill_opacity=0.55)
        ps_fill.add_updater(lambda m: m.set_points_as_corners([
            [-3.94, -0.025, BASE + 3 * HEIGHT], [-2.84, -0.025, BASE + 3 * HEIGHT],
            [-2.84, -0.025, BASE + payment.get_value() * HEIGHT],
            [-3.94, -0.025, BASE + payment.get_value() * HEIGHT], [-3.94, -0.025, BASE + 3 * HEIGHT]]))
        pair_price = Line([-5.16, -0.045, BASE + 4 * HEIGHT], [-2.84, -0.045, BASE + 4 * HEIGHT],
                          color=GUIDE, stroke_width=2.5).set_flat_stroke(False)
        pair_price.add_updater(lambda m: m.put_start_and_end_on(
            np.array([-5.16, -0.045, BASE + payment.get_value() * HEIGHT]),
            np.array([-2.84, -0.045, BASE + payment.get_value() * HEIGHT])))
        payment_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.62 * self.camera.frame.get_scale())
        payment_number.tracker, payment_number.face_mat = payment, np.eye(3)
        payment_number.add_updater(face_camera)
        payment_number.add_updater(lambda m: m.move_to([-2.4, -0.1, BASE + m.tracker.get_value() * HEIGHT]))
        payment_number.update()
        # Name the familiar regions directly; introduce only their sum.
        cs_label = Tex('CS', color=INK).scale(0.58 * self.camera.frame.get_scale())
        ps_label = Tex('PS', color=INK).scale(0.58 * self.camera.frame.get_scale())
        total_definition = Tex(r'Total surplus $= PS + CS$', color=INK,
                               tex_to_color_map={'PS': SUPPLY, 'CS': DEMAND})
        total_definition.scale(0.90 * self.camera.frame.get_scale())
        for label in [cs_label, ps_label, total_definition]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        cs_label.add_updater(lambda m: m.move_to([-4.61, -0.07, BASE + (8 + payment.get_value()) * HEIGHT / 2]))
        ps_label.add_updater(lambda m: m.move_to([-3.39, -0.07, BASE + (3 + payment.get_value()) * HEIGHT / 2]))
        cs_label.update()
        ps_label.update()
        total_definition.move_to([3.75, -0.07, 3.6])
        self.play(FadeIn(cs_fill), FadeIn(ps_fill), FadeIn(pair_price), FadeIn(payment_number),
                  FadeIn(cs_label), FadeIn(ps_label), FadeIn(total_definition))
        self.play(payment.animate.set_value(5), run_time=1.8, rate_func=smooth)
        self.pause('2.b')
        self.play(payment.animate.set_value(4), run_time=0.8, rate_func=smooth)
        for mob in [cs_fill, ps_fill, pair_price, payment_number, cs_label, ps_label]:
            mob.clear_updaters()
        self.play(*[FadeOut(m) for m in [cs_fill, ps_fill, pair_price, payment_number,
                                       cs_label, ps_label, total_definition]], run_time=0.45)
        self.play(Restore(mb_bar), Restore(mc_bar), Restore(bodies['B', 20]), Restore(bodies['S', 20]),
                  Restore(rings['B', 20]), Restore(rings['S', 20]), FadeIn(floor), FadeIn(rim),
                  self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.0)

        # ---- 2.c · The planner controls participants and quantity, not price.
        self.remove(cs_strips, ps_strips)
        for mob in checks.values():
            mob.set_opacity(0)
        for mob in bodies.values():
            mob.set_opacity(1)
            mob[0].set_opacity(0.28)
        for mob in bars.values():
            mob.set_opacity(0.65)
        for key, mob in rings.items():
            mob.set_stroke(opacity=1 if key[1] <= 40 else 0).set_fill(opacity=0)
        self.add(crowd)
        buyers_label.set_opacity(1)
        sellers_label.set_opacity(1)
        units.set_opacity(1)
        self.play(FadeOut(head), FadeIn(graph), run_time=0.25)
        fitted.set_opacity(0.17)
        head = fixed(title('The social planner'))
        q_word = fixed(Tex('Trades:', color=GUIDE)).scale(0.65).move_to([3.7, -2.97, 0])
        q_number = fixed(Integer(40, color=GUIDE)).scale(0.65).next_to(q_word, RIGHT, buff=0.15)
        q_number.add_updater(lambda m: m.set_value(int(quantity.get_value() + 1e-7)).next_to(q_word, RIGHT, buff=0.15))
        bottom = fixed(Tex(r'Who trades?\qquad How many trades?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(head), FadeIn(bottom), FadeIn(crowd_words), FadeIn(q_guide), FadeIn(q_word), FadeIn(q_number))
        self.pause('2.c')

        # ---- 3.a · Twenty trades; Gary occupies buyer 10's slot.
        self.play(FadeOut(bottom), FadeOut(head), run_time=0.2)
        quantity.set_value(20)
        allocation = {n: n for n in range(1, 21) if n != 10}
        allocation[30] = 10
        allocation_moves = []
        for key, body in bodies.items():
            side, n = key
            matched = n in (allocation if side == 'B' else allocation.values())
            station = allocation.get(n, n) if side == 'B' else n
            x = ROW_LEFT + (station - 1) * RANK_STEP + ((-0.019 if side == 'B' else 0.019) if matched else 0)
            y = -1.7 if matched else home_positions[key][1]
            radius = 0.014 if matched else 0.026
            value = MB[n - 1] if side == 'B' else MC[n - 1]
            allocation_moves.extend([
                body[0].animate.set_width(0.074 * radius / 0.026).move_to([x, y, 0.025]),
                body[1].animate.set_width(radius * body.orb_unit_width).move_to([x, y, 0.043 if matched else 0.055]),
                bars[key].animate.stretch_to_fit_width(0.030 if matched else 0.058)
                .move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2]),
                rings[key].animate.set_width(0.036 if matched else 0.070).move_to([x, y, 0.045])
                .set_stroke(opacity=1 if matched else 0).set_fill(opacity=0)])
        self.play(*allocation_moves, run_time=0.7)
        head = fixed(title('Who should get this lot?'))
        self.play(FadeIn(head), *[mob.animate.set_opacity(0) for body in bodies.values() for mob in body],
                  *[bar.animate.set_opacity(0) for bar in bars.values()],
                  *[ring.animate.set_stroke(opacity=0).set_fill(opacity=0) for ring in rings.values()], run_time=0.3)
        self.remove(*[mob for key in bodies if key not in [('B', 30), ('B', 10), ('S', 10)]
                      for mob in [bodies[key], bars[key], rings[key]]])
        self.play(self.camera.frame.animate.reorient(0, 90, center=[0, 0, 3.4], height=10.2),
                  FadeOut(crowd_words), run_time=1.0)
        # Actual B3 people and bars move into this head-on comparison.
        focus_keys = [('B', 30), ('B', 10), ('S', 10)]
        comparison_words = VGroup()
        focus_labels = []
        for key, x, value, color, text in [
                (('B', 30), -6.0, 6, DEMAND, r'MB \$6'),
                (('B', 10), -4.2, 10, DEMAND, r'Buyer 10: MB \$10'),
                (('S', 10), -2.25, 2.5, SUPPLY, r'Seller 10: MC \$2.50')]:
            rings[key].set_stroke(opacity=0).set_fill(opacity=0)
            bodies[key].save_state()
            bars[key].save_state()
            self.play(bodies[key].animate.scale(0.23 * bodies[key].orb_unit_width / bodies[key][1].get_width()).move_to([x, 0, 0.32]).set_opacity(1),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]).set_opacity(0.65), run_time=0.45)
            label = Tex(text, color=color).scale(0.53 * self.camera.frame.get_scale())
            label.move_to([x, -0.1, 0.75 + value * 0.55 + 0.3])
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            comparison_words.add(label)
            focus_labels.append(label)
        current_link = Line([-6, 0, 0.045], [-2.25, 0, 0.045], color=GOV, stroke_width=2)
        proposed_link = DashedLine([-4.2, -0.16, 0.045], [-2.25, -0.16, 0.045], color=TOTAL, stroke_width=2)
        current_ring = Circle(radius=0.29, color=GOV, stroke_width=2).move_to([-6, 0, 0.045])
        counterpart_ring = Circle(radius=0.29, color=GOV, stroke_width=2).move_to([-2.25, 0, 0.045])
        proposed_gain = Line([-6.7, -0.045, 0.75 + 2.5 * 0.55],
                             [-6.7, -0.045, 0.75 + 6 * 0.55], color=TOTAL, stroke_width=4)
        bottom = fixed(Tex('20 trades; the seller stays the same.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(comparison_words), FadeIn(current_link), FadeIn(proposed_link),
                  FadeIn(current_ring), FadeIn(counterpart_ring), FadeIn(proposed_gain), FadeIn(bottom))
        self.pause('3.a')

        # ---- 3.b · Replace one buyer; quantity and the seller are unchanged.
        self.play(FadeOut(bottom), FadeOut(current_link), FadeOut(proposed_link), run_time=0.2)
        allocation.pop(30)
        allocation[10] = 10
        rings['B', 30].set_stroke(opacity=0).set_fill(opacity=0)
        rings['B', 10].set_stroke(opacity=0).set_fill(opacity=0)
        current_link = Line([-6, 0, 0.045], [-2.25, 0, 0.045], color=GOV, stroke_width=2)
        self.play(Restore(bodies['B', 30]), Restore(bars['B', 30]), FadeOut(focus_labels[0]),
                  bodies['B', 10].animate.set_x(-6), bars['B', 10].animate.set_x(-6),
                  focus_labels[1].animate.set_x(-6),
                  FadeIn(current_link), proposed_gain.animate.put_start_and_end_on(
                      np.array([-6.7, -0.045, 0.75 + 2.5 * 0.55]), np.array([-6.7, -0.045, 0.75 + 10 * 0.55])), run_time=1.0)
        self.remove(bodies['B', 30], bars['B', 30])
        swap_result = fixed(Tex(r'Same cost; \$4,000 more benefit.', color=TOTAL)).scale(0.7)
        swap_result.move_to([-4.1, -2.95, 0])
        bottom = fixed(Tex('Highest-value buyers.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(swap_result), FadeIn(bottom))
        self.pause('3.b')

        # ---- 3.c · Start a separate counterfactual with Andrew producing.
        self.play(*[FadeOut(m) for m in [comparison_words, current_link, current_ring, counterpart_ring,
                                       proposed_gain, swap_result, bottom, head]], run_time=0.35)
        self.play(*[FadeOut(mob) for key in focus_keys for mob in [bodies[key], bars[key]]], run_time=0.25)
        for key in focus_keys:
            bodies[key].restore()
            bars[key].restore()
        self.remove(*[mob for key in bodies for mob in [bodies[key], bars[key], rings[key]]])
        allocation = {n: n for n in range(1, 21)}
        allocation[10] = 40
        for key, body in bodies.items():
            side, n = key
            matched = n in (allocation if side == 'B' else allocation.values())
            station = allocation.get(n, n) if side == 'B' else n
            x = ROW_LEFT + (station - 1) * RANK_STEP + ((-0.019 if side == 'B' else 0.019) if matched else 0)
            y = -1.7 if matched else home_positions[key][1]
            radius = 0.014 if matched else 0.026
            value = MB[n - 1] if side == 'B' else MC[n - 1]
            body[0].set_width(0.074 * radius / 0.026).move_to([x, y, 0.025])
            body[1].set_width(radius * body.orb_unit_width).move_to([x, y, 0.043 if matched else 0.055])
            bars[key].stretch_to_fit_width(0.030 if matched else 0.058).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            rings[key].set_width(0.036 if matched else 0.070).move_to([x, y, 0.045]).set_stroke(opacity=0).set_fill(opacity=0)
        head = fixed(title('Who should produce this lot?'))
        focus_keys = [('S', 40), ('S', 10), ('B', 10)]
        comparison_words = VGroup()
        focus_labels = []
        for key, x, value, color, text in [
                (('S', 40), -6.0, 4, SUPPLY, r'MC \$4'),
                (('S', 10), -4.2, 2.5, SUPPLY, r'Seller 10: MC \$2.50'),
                (('B', 10), -2.25, 10, DEMAND, r'Buyer 10: MB \$10')]:
            rings[key].set_stroke(opacity=0).set_fill(opacity=0)
            bodies[key].save_state()
            bars[key].save_state()
            self.play(bodies[key].animate.scale(0.23 * bodies[key].orb_unit_width / bodies[key][1].get_width()).move_to([x, 0, 0.32]).set_opacity(1),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]).set_opacity(0.65), run_time=0.45)
            label = Tex(text, color=color).scale(0.53 * self.camera.frame.get_scale())
            label.move_to([x, -0.1, 0.75 + value * 0.55 + 0.3])
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
            comparison_words.add(label)
            focus_labels.append(label)
        current_link = Line([-6, 0, 0.045], [-2.25, 0, 0.045], color=GOV, stroke_width=2)
        proposed_link = DashedLine([-4.2, -0.16, 0.045], [-2.25, -0.16, 0.045], color=TOTAL, stroke_width=2)
        current_ring = Circle(radius=0.29, color=GOV, stroke_width=2).move_to([-6, 0, 0.045])
        counterpart_ring = Circle(radius=0.29, color=GOV, stroke_width=2).move_to([-2.25, 0, 0.045])
        seller_gain = Line([-2.9, -0.045, 0.75 + 4 * 0.55], [-2.9, -0.045, 0.75 + 10 * 0.55],
                           color=TOTAL, stroke_width=4)
        bottom = fixed(Tex('20 trades; the buyer stays the same.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(head), FadeIn(comparison_words), FadeIn(current_link), FadeIn(proposed_link),
                  FadeIn(current_ring), FadeIn(counterpart_ring), FadeIn(seller_gain), FadeIn(bottom))
        self.pause('3.c')

        # ---- 3.d · The same benefit now costs $1,500 less.
        self.play(FadeOut(bottom), FadeOut(current_link), FadeOut(proposed_link), run_time=0.2)
        allocation[10] = 10
        rings['S', 40].set_stroke(opacity=0).set_fill(opacity=0)
        rings['S', 10].set_stroke(opacity=0).set_fill(opacity=0)
        current_link = Line([-6, 0, 0.045], [-2.25, 0, 0.045], color=GOV, stroke_width=2)
        self.play(Restore(bodies['S', 40]), Restore(bars['S', 40]), FadeOut(focus_labels[0]),
                  bodies['S', 10].animate.set_x(-6), bars['S', 10].animate.set_x(-6),
                  focus_labels[1].animate.set_x(-6),
                  FadeIn(current_link), seller_gain.animate.put_start_and_end_on(
                      np.array([-2.9, -0.045, 0.75 + 2.5 * 0.55]), np.array([-2.9, -0.045, 0.75 + 10 * 0.55])), run_time=1.0)
        self.remove(bodies['S', 40], bars['S', 40])
        swap_result = fixed(Tex(r'Same benefit; \$1,500 less cost.', color=TOTAL)).scale(0.7).move_to([-4.1, -2.95, 0])
        bottom = fixed(Tex('Lowest-cost sellers.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(swap_result), FadeIn(bottom))
        self.pause('3.d')

        # ---- 3.e · The participants are sorted; partner identities are bookkeeping.
        self.play(*[FadeOut(m) for m in [comparison_words, current_link, current_ring, counterpart_ring,
                                       seller_gain, swap_result, bottom, head]], run_time=0.35)
        self.play(*[FadeOut(mob) for key in focus_keys for mob in [bodies[key], bars[key]]], run_time=0.25)
        for key in focus_keys:
            bodies[key].restore()
            bars[key].restore()
        self.play(self.camera.frame.animate.reorient(0, 48, center=PLAZA_CENTER, height=11), run_time=1.0)
        allocation = {n: n for n in range(1, 21)}
        for key, body in bodies.items():
            side, n = key
            matched = n <= 20
            x = home_positions[key][0] + ((-0.019 if side == 'B' else 0.019) if matched else 0)
            y = -1.7 if matched else home_positions[key][1]
            radius = 0.014 if matched else 0.026
            value = MB[n - 1] if side == 'B' else MC[n - 1]
            body[0].set_width(0.074 * radius / 0.026).move_to([x, y, 0.025]).set_opacity(0.28)
            body[1].set_width(radius * body.orb_unit_width).move_to([x, y, 0.043 if matched else 0.055]).set_opacity(1)
            bars[key].stretch_to_fit_width(0.030 if matched else 0.058).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2]).set_opacity(0.65)
            checks[key].set_opacity(0)
            rings[key].set_width(0.036 if matched else 0.070).move_to([x, y, 0.045]).set_stroke(opacity=1 if matched else 0).set_fill(opacity=0)
        self.add(crowd)
        for mob in [buyers_label, sellers_label, units]:
            mob.set_opacity(1)
        self.add(gain_strips)
        for n, strip in enumerate(gain_strips, start=1):
            strip.set_fill(opacity=AREA_OPACITY if n <= 20 else 0)
            strip.set_stroke(opacity=1 if n <= 20 else 0)
        head = fixed(title('How many trades should happen?'))
        bottom = fixed(Tex('Now choose how many.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(head), FadeIn(bottom), FadeIn(crowd_words))
        self.pause('3.e')

        # ---- 4.a · Keep the plaza and graph fixed; inspect the next lot in place.
        self.play(FadeOut(bottom), run_time=0.2)
        # Quantity changes actual membership. It never changes a person's value.
        for key, body in bodies.items():
            side, n = key
            for mob, paired_width, stretch in [
                    (body[0], 0.074 * 0.014 / 0.026, False),
                    (body[1], 0.014 * body.orb_unit_width, False),
                    (bars[key], 0.030, True), (rings[key], 0.036, False)]:
                mob.quantity, mob.rank = quantity, n
                mob.waiting = np.array([*home_positions[key][:2], mob.get_center()[2]])
                mob.paired = np.array([home_positions[key][0] + (-0.019 if side == 'B' else 0.019), -1.7, mob.get_center()[2]])
                if mob is body[1]:
                    mob.waiting[2], mob.paired[2] = 0.055, 0.043
                mob.waiting_width = (0.074 if mob is body[0] else 0.026 * body.orb_unit_width
                                     if mob is body[1] else 0.058 if mob is bars[key] else 0.070)
                mob.paired_width, mob.stretch_width = paired_width, stretch
                mob.add_updater(lambda m: m.set_width(
                    m.paired_width if m.rank <= int(m.quantity.get_value() + 1e-7) else m.waiting_width,
                    stretch=m.stretch_width).move_to(
                    m.paired if m.rank <= int(m.quantity.get_value() + 1e-7) else m.waiting))
            rings[key].add_updater(lambda m: m.set_stroke(
                opacity=float(m.rank <= int(m.quantity.get_value() + 1e-7))).set_fill(opacity=0))
        for n, strip in enumerate(gain_strips, start=1):
            strip.rank, strip.quantity = n, quantity
            strip.add_updater(lambda m: m.set_fill(
                opacity=AREA_OPACITY if m.rank <= int(m.quantity.get_value() + 1e-7) else 0)
                .set_stroke(opacity=0.55 if m.rank <= int(m.quantity.get_value() + 1e-7) else 0))
        probe = ValueTracker(21)
        self.add(quantity, probe)
        # One highlighted graph slice connects the selected people's MB and MC.
        marginal_gap = fixed(Line(ax.c2p(21, MC[20]), ax.c2p(21, MB[20]), color=TOTAL, stroke_width=4))
        marginal_gap.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(probe.get_value(), MC[int(probe.get_value()) - 1]),
            ax.c2p(probe.get_value(), MB[int(probe.get_value()) - 1] + 1e-6)))
        mb_dot = fixed(Dot(ax.c2p(21, MB[20]), radius=0.045, color=DEMAND))
        mc_dot = fixed(Dot(ax.c2p(21, MC[20]), radius=0.045, color=SUPPLY))
        mb_dot.add_updater(lambda m: m.move_to(ax.c2p(probe.get_value(), MB[int(probe.get_value()) - 1])))
        mc_dot.add_updater(lambda m: m.move_to(ax.c2p(probe.get_value(), MC[int(probe.get_value()) - 1])))
        selected_words = fixed(VGroup(
            Tex(r'MB: \$7.80', color=DEMAND).scale(0.53).next_to(ax.c2p(21, 7.8), UR, buff=0.15),
            Tex(r'MC: \$3.05', color=SUPPLY).scale(0.53).next_to(ax.c2p(21, 3.05), DR, buff=0.15)))
        pair_focus = VGroup()
        for side, color in [('B', DEMAND), ('S', SUPPLY)]:
            outline = Circle(radius=0.055, color=color, stroke_width=2)
            outline.side = side
            outline.add_updater(lambda m: m.move_to(rings[m.side, int(probe.get_value())].get_center()))
            pair_focus.add(outline)
        bottom = fixed(Tex('Trade 21: should we add this lot?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(pair_focus), FadeIn(marginal_gap), FadeIn(mb_dot), FadeIn(mc_dot),
                  FadeIn(selected_words), FadeIn(bottom))
        self.pause('4.a')

        # ---- 4.b · Add the lot, then the other positive gains without reframing.
        self.play(FadeOut(bottom), quantity.animate.set_value(21), run_time=0.5)
        bottom = fixed(Tex(r'Trade 21 adds $(7.80-3.05)\times1{,}000=\$4{,}750$.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.wait(0.7)
        self.play(FadeOut(bottom), FadeOut(selected_words), FadeOut(pair_focus),
                  FadeOut(marginal_gap), FadeOut(mb_dot), FadeOut(mc_dot), run_time=0.3)
        self.play(quantity.animate.set_value(39), run_time=2.0, rate_func=linear)
        allocation = {n: n for n in range(1, 40)}
        probe.set_value(39)
        selected_words = fixed(VGroup(
            Tex(r'MB: \$4.20', color=DEMAND).scale(0.53).next_to(ax.c2p(39, 4.2), UL, buff=0.15),
            Tex(r'MC: \$3.95', color=SUPPLY).scale(0.53).next_to(ax.c2p(39, 3.95), DR, buff=0.15)))
        bottom = fixed(Tex(r'Trade 39 adds \$250. Another trade helps while $MB>MC$.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(pair_focus), FadeIn(marginal_gap), FadeIn(mb_dot), FadeIn(mc_dot),
                  FadeIn(selected_words), FadeIn(bottom))
        self.pause('4.b')

        # ---- 4.c · The next lot reaches the crossing, on the same axes.
        self.play(FadeOut(bottom), FadeOut(selected_words), run_time=0.2)
        probe.set_value(40)
        selected_words = fixed(VGroup(
            Tex(r'MB = MC = \$4', color=GUIDE).scale(0.56).next_to(ax.c2p(40, 4), UR, buff=0.18)))
        bottom = fixed(Tex('Trade 40: what does this lot add?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(bottom))
        self.pause('4.c')

        # ---- 4.d · Select the indifferent pair; the gain area does not grow.
        self.play(FadeOut(bottom), quantity.animate.set_value(40), run_time=0.5)
        allocation = {n: n for n in range(1, 41)}
        bottom = fixed(Tex(r'Trade 40 adds \$0. 39 or 40: the same total gain.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('4.d')

        # ---- 4.e · Inspect the next values; do not execute a harmful trade.
        self.play(FadeOut(bottom), FadeOut(selected_words), run_time=0.2)
        probe.set_value(41)
        selected_words = fixed(VGroup(
            Tex(r'MB: \$3.80', color=DEMAND).scale(0.53).next_to(ax.c2p(41, 3.8), DL, buff=0.15),
            Tex(r'MC: \$4.05', color=SUPPLY).scale(0.53).next_to(ax.c2p(41, 4.05), UR, buff=0.15)))
        bottom = fixed(Tex('Trade 41: would this lot help?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(bottom))
        self.pause('4.e')
        self.play(FadeOut(bottom), run_time=0.2)
        bottom = fixed(Tex(r'$MC>MB$: this trade would lose \$250.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.wait(0.7)

        # ---- 4.f · One quantity comparison; keep the same graph and plaza.
        self.play(FadeOut(selected_words), FadeOut(pair_focus), FadeOut(marginal_gap),
                  FadeOut(mb_dot), FadeOut(mc_dot), FadeOut(bottom), run_time=0.25)
        self.play(quantity.animate.set_value(30), run_time=1.0, rate_func=linear)
        for strip in gain_strips[30:]:
            strip.clear_updaters()
            strip.set_stroke(opacity=0.55)
        bottom = fixed(Tex('Fewer trades leave positive gains unrealized.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.wait(0.7)
        self.play(quantity.animate.set_value(40),
                  *[strip.animate.set_fill(opacity=AREA_OPACITY) for strip in gain_strips[30:]],
                  run_time=1.0, rate_func=linear)
        self.play(FadeOut(bottom), run_time=0.2)
        bottom = fixed(Tex('Take the gains; stop when additional cost exceeds benefit.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('4.f')
        for key, body in bodies.items():
            for mob in [body[0], body[1], bars[key], rings[key]]:
                mob.clear_updaters()
        for strip in gain_strips:
            strip.clear_updaters()

        # ---- 5.a · Release the planner's selection in the unchanged plaza view.
        self.play(FadeOut(bottom), FadeOut(head), FadeOut(q_word), FadeOut(q_number), FadeOut(q_guide), run_time=0.3)
        allocation = {}
        restore_people = []
        for key, body in bodies.items():
            side, n = key
            x, y = home_positions[key][:2]
            value = MB[n - 1] if side == 'B' else MC[n - 1]
            restore_people.extend([
                body[0].animate.set_width(0.074).move_to([x, y, 0.025]),
                body[1].animate.set_width(0.026 * body.orb_unit_width).move_to([x, y, 0.055]),
                bars[key].animate.stretch_to_fit_width(0.058).stretch_to_fit_depth(value * DOLLAR_HEIGHT)
                .move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2]),
                rings[key].animate.set_width(0.070).move_to([x, y, 0.045]).set_stroke(opacity=0).set_fill(opacity=0)])
        self.play(*restore_people, run_time=0.8)
        self.play(FadeIn(crowd_words), run_time=0.3)
        zero_dot = fixed(Dot(ax.c2p(40, 4), color=GUIDE, radius=0.065))
        planner_outlines = VGroup()
        for side in ['B', 'S']:
            for n in range(1, 41):
                outline = Circle(radius=0.0144, color=TOTAL, stroke_width=0.8).set_stroke(opacity=0.45)
                outline.anchor = rings[side, n]
                outline.add_updater(lambda m: m.move_to(m.anchor.get_center()))
                planner_outlines.add(outline)
        for ring in rings.values():
            ring.set_stroke(opacity=0).set_fill(opacity=0)
        for strip in gain_strips:
            strip.set_fill(opacity=0).set_stroke(opacity=0.3)
        head = fixed(title('Does the market choose these trades?'))
        bottom = fixed(Tex(r'At \$4, who is willing?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(head), FadeIn(bottom), FadeIn(planner_outlines), FadeIn(price_line), FadeIn(price_read))
        self.pause('5.a')

        # ---- 5.b · The price selects exactly the planner's prefixes.
        self.play(FadeOut(bottom), run_time=0.2)
        allocation = {n: n for n in range(1, 41)}
        market_pairs = []
        for side in ['B', 'S']:
            for n in range(1, 41):
                key = side, n
                x = home_positions[key][0] + (-0.019 if side == 'B' else 0.019)
                value = MB[n - 1] if side == 'B' else MC[n - 1]
                market_pairs.extend([
                    bodies[key][0].animate.set_width(0.074 * 0.014 / 0.026).move_to([x, -1.7, 0.025]),
                    bodies[key][1].animate.set_width(0.014 * bodies[key].orb_unit_width).move_to([x, -1.7, 0.043]),
                    bars[key].animate.stretch_to_fit_width(0.030).move_to([x, -1.7, BAR_BASE + value * DOLLAR_HEIGHT / 2]),
                    rings[key].animate.set_width(0.036).move_to([x, -1.7, 0.045]).set_stroke(opacity=1).set_fill(opacity=0)])
        self.play(*[checks[side, n].animate.set_opacity(1) for side in ['B', 'S'] for n in range(1, 41)],
                  *market_pairs,
                  *[strip.animate.set_fill(opacity=AREA_OPACITY).set_stroke(opacity=1) for strip in gain_strips],
                  run_time=0.9)
        thresholds = VGroup(fixed(Tex(r'Buyer 40: $MB=\$4$\quad Buyer 41: $MB<\$4$', color=DEMAND)).scale(0.58),
                            fixed(Tex(r'Seller 40: $MC=\$4$\quad Seller 41: $MC>\$4$', color=SUPPLY)).scale(0.58))
        fixed(thresholds)
        thresholds.arrange(DOWN, buff=0.18).move_to([-3.95, -2.6, 0])
        self.play(units.animate.set_opacity(0), sellers_label.animate.set_opacity(0), FadeIn(thresholds))
        bottom = fixed(Tex('The same people; the same gains.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('5.b')

        # ---- 5.c · Tie sorting and the marginal rule to the market outcome.
        self.play(FadeOut(bottom), FadeOut(thresholds), FadeOut(planner_outlines), run_time=0.25)
        self.play(Indicate(buyers_label, color=FOCUS), run_time=0.5)
        self.play(sellers_label.animate.set_opacity(1), run_time=0.2)
        self.play(Indicate(sellers_label, color=FOCUS), run_time=0.5)
        self.play(FadeIn(zero_dot), run_time=0.3)
        bottom = fixed(Tex('Total surplus = total benefit $-$ total cost.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.wait(0.6)
        self.play(FadeOut(bottom), run_time=0.2)
        bottom = fixed(Tex('Equilibrium maximizes total gains from trade.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('5.c')

        # ---- 5.d · Name this result, with its assumptions still on the model.
        self.play(FadeOut(bottom), sellers_label.animate.set_opacity(0), run_time=0.2)
        condition_a = fixed(Tex('Competitive market', color=CAPTION)).scale(0.65).move_to([-3.95, -2.2, 0])
        condition_b = fixed(Tex('All costs and benefits counted', color=CAPTION)).scale(0.65).move_to([-3.95, -2.65, 0])
        theorem = fixed(Tex('First Welfare Theorem', color=DEFINITION)).scale(BOTTOM_SCALE)
        theorem.move_to([0, -3.15, 0])
        statement = fixed(Tex('Competitive markets with no externalities maximize welfare.', color=INK)).scale(BOTTOM_SCALE)
        statement.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(condition_a), FadeIn(condition_b), FadeIn(theorem), FadeIn(statement))
        self.pause('5.d')

        # ========== 9. Controls ==========
        # Advance directly into the next stage on the same navigation rail.
        self.clear()
        self.camera.frame.clear_updaters()
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)

        self.camera.fps = 15

        # One person is one 1,000-lb lot. Bar height is dollars per pound.
        BUYER_MB = np.array([12 - n / 5 for n in range(1, 60)])
        SELLER_MC = np.array([2 + n / 20 for n in range(1, 101)])
        EPS = 1e-7
        DOLLAR_HEIGHT = 0.19
        price = ValueTracker(4)
        show_counts = ValueTracker(1)
        show_trades = ValueTracker(1)
        show_buyers = ValueTracker(1)
        show_sellers = ValueTracker(1)
        self.add(price, show_counts, show_trades, show_buyers, show_sellers)
        # B3's plaza and material objects, with the raised full-market framing.
        # One uninterrupted ranked line per side; the bars carry the values.
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to(PLAZA_CENTER).set_height(11)
        BAR_BASE = 0.18
        ROW_LEFT, ROW_WIDTH = -3.7, 7.4
        RANK_STEP = ROW_WIDTH / (max(len(BUYER_MB), len(SELLER_MC)) - 1)
        BUYER_Y, SELLER_Y = 2.0, -1.7
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        buyer_people, buyer_bars, buyer_checks, buyer_circles = Group(), Group(), VGroup(), VGroup()
        seller_people, seller_bars, seller_checks, seller_circles = Group(), Group(), VGroup(), VGroup()
        buyer_positions, seller_positions = [], []
        for n, value in enumerate(BUYER_MB):
            x, y = ROW_LEFT + n * RANK_STEP, BUYER_Y
            buyer_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.037, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(DEMAND).move_to([x, y, 0.025])
            orb = Sphere(radius=0.026, color=DEMAND, resolution=(12, 8)).move_to([x, y, 0.055])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.058, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = (VMobject(color=DEMAND, stroke_width=1.1).set_points_as_corners([[-0.015, 0, 0], [-0.003, -0.013, 0], [0.02, 0.02, 0]]))
            check.price, check.value, check.visibility = price, value, show_buyers
            check.anchor, check.dollar_height = bar, DOLLAR_HEIGHT
            check.scale(self.camera.frame.get_scale())
            check.face_mat = np.eye(3)
            check.add_updater(face_camera)
            check.add_updater(lambda m: m.move_to(m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10)).set_stroke(opacity=m.visibility.get_value() * float(m.value + 1e-7 >= m.price.get_value())).set_fill(opacity=0))
            circle = Circle(radius=0.035, color=GREEN, stroke_width=1.0).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            buyer_people.add(person)
            buyer_bars.add(bar)
            buyer_checks.add(check)
            buyer_circles.add(circle)
        for n, value in enumerate(SELLER_MC):
            x, y = ROW_LEFT + n * RANK_STEP, SELLER_Y
            seller_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.037, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(SUPPLY).move_to([x, y, 0.025])
            orb = Sphere(radius=0.026, color=SUPPLY, resolution=(12, 8)).move_to([x, y, 0.055])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.058, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = (VMobject(color=SUPPLY, stroke_width=1.1).set_points_as_corners([[-0.015, 0, 0], [-0.003, -0.013, 0], [0.02, 0.02, 0]]))
            check.price, check.value, check.visibility = price, value, show_sellers
            check.anchor, check.dollar_height = bar, DOLLAR_HEIGHT
            check.scale(self.camera.frame.get_scale())
            check.face_mat = np.eye(3)
            check.add_updater(face_camera)
            check.add_updater(lambda m: m.move_to(m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10)).set_stroke(opacity=m.visibility.get_value() * float(m.value <= m.price.get_value() + 1e-7)).set_fill(opacity=0))
            circle = Circle(radius=0.035, color=GREEN, stroke_width=1.0).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            seller_people.add(person)
            seller_bars.add(bar)
            seller_checks.add(check)
            seller_circles.add(circle)
        # Trading partners stand together at the seller's station.
        # Unmatched people keep their place in the ranked waiting lines.
        for people, bars, circles, side in [(buyer_people, buyer_bars, buyer_circles, -1),
                                            (seller_people, seller_bars, seller_circles, 1)]:
            for n, (person, bar, circle) in enumerate(zip(people, bars, circles)):
                for mob, paired_width, stretch_width in [(person, 0.074 * (0.014 / 0.026), False),
                                                          (bar, 0.030, True), (circle, 0.036, False)]:
                    mob.home = mob.get_center().copy()
                    paired_z = 0.025 + person.get_depth() * (paired_width / person.get_width()) / 2 if mob is person else mob.home[2]
                    mob.pair_home = np.array([seller_positions[n][0] + side * 0.019, SELLER_Y, paired_z])
                    mob.home_width, mob.paired_width, mob.stretch_width = mob.get_width(), paired_width, stretch_width
                    mob.price, mob.rank, mob.visibility = price, n + 1, show_trades
                    mob.mb, mob.mc = BUYER_MB, SELLER_MC
                    mob.add_updater(lambda m: setattr(m, 'pair_fraction', m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))))
                    mob.add_updater(lambda m: m.set_width(m.home_width + m.pair_fraction * (m.paired_width - m.home_width), stretch=m.stretch_width).move_to(m.home + m.pair_fraction * (m.pair_home - m.home)))
        buyer_label = Tex('Buyers: highest MB first', color=DEMAND).scale(0.56 * self.camera.frame.get_scale())
        buyer_label.move_to(self.camera.frame.from_fixed_frame_point([-3.3, 2.65, 0]))
        seller_label = Tex('Sellers: lowest MC first', color=SUPPLY).scale(0.56 * self.camera.frame.get_scale())
        seller_label.move_to(self.camera.frame.from_fixed_frame_point([-3.3, -2.55, 0]))
        for label in [buyer_label, seller_label]:
            label.face_mat = np.eye(3)
            label.add_updater(face_camera)
            label.update()
        units = fixed(fixed(Tex(r'One person = 1,000 lb', color=CAPTION)).scale(0.50).move_to([-3.3, -2.90, 0]))
        buyers = Group(buyer_bars, buyer_people, buyer_circles)
        sellers = Group(seller_bars, seller_people, seller_circles)
        crowd = Group(floor, rim, buyers, sellers, buyer_label, seller_label)
        crowd_marks = VGroup(buyer_checks, seller_checks)


        # Legal bounds and the actual price are different objects.
        # A ceiling above $4 or floor below $4 leaves the actual price at $4.
        ceiling = ValueTracker(13)
        floor_limit = ValueTracker(0)
        show_welfare = ValueTracker(1)
        show_totals = ValueTracker(1)
        show_loss = ValueTracker(0)
        loss_fill = ValueTracker(0)
        price.ceiling, price.floor_limit = ceiling, floor_limit
        price.add_updater(lambda m: m.set_value(min(m.ceiling.get_value(), max(4, m.floor_limit.get_value()))))
        self.add(ceiling, floor_limit, show_welfare, show_totals, show_loss, loss_fill)

        # Keep the same market graph still: straight equations, exact per-lot surplus below.
        ax = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=3.8)
        ax.move_to([4.48, 0.45, 0])
        ticks = VGroup()
        for q in [0, 20, 40, 60, 80, 100]:
            tick = fixed(Tex(str(q), color=CAPTION)).scale(0.40).next_to(ax.c2p(q, 0), DOWN, buff=0.10)
            tick.quantity, tick.price, tick.visibility = q, price, show_counts
            tick.mb, tick.mc = BUYER_MB, SELLER_MC
            tick.add_updater(lambda m: m.set_opacity(1 - m.visibility.get_value() * float(min(
                abs(m.quantity - np.count_nonzero(m.mb + 1e-7 >= m.price.get_value())),
                abs(m.quantity - np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))) < 7)))
            ticks.add(tick)
        for p in [8, 12]:
            ticks.add(Tex(str(p), color=CAPTION).scale(0.40).next_to(ax.c2p(0, p), LEFT, buff=0.10))
        graph_units = Tex(r'$Q$: thousands of pounds', color=CAPTION).scale(0.48).move_to([4.48, -2.07, 0])
        demand_curve = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=2.8)
        supply_curve = Line(ax.c2p(0, 2), ax.c2p(100, 7), color=SUPPLY, stroke_width=2.8)
        demand_word = Tex('D / MB', color=DEMAND).scale(0.60).next_to(ax.c2p(10, 10), RIGHT, buff=0.14)
        supply_word = Tex('S / MC', color=SUPPLY).scale(0.60).next_to(ax.c2p(84, 6.2), UP, buff=0.14)
        price_units = Tex('Dollars per pound', color=CAPTION).scale(0.48)
        price_units.next_to(ax.c2p(0, 13), UP, buff=0.16, aligned_edge=LEFT)
        graph = fixed(VGroup(ax, ticks, demand_curve, supply_curve,
                             graph_units, price_units, demand_word, supply_word))
        actual_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2.4))
        actual_line.axes, actual_line.price = ax, price
        # Preserve dash spacing through shrinking, zero trade, and regrowth.
        actual_line.level = price
        actual_line.add_updater(lambda m: set_dashed_endpoints(m,
            m.axes.c2p(0, m.level.get_value()),
            m.axes.c2p(max(0, min(60 - 5 * m.level.get_value(), 20 * (m.level.get_value() - 2), 100)), m.level.get_value())))
        trade_guide = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2))
        trade_guide.axes, trade_guide.price = ax, price
        trade_guide.mb, trade_guide.mc, trade_guide.visibility = BUYER_MB, SELLER_MC, show_counts
        trade_guide.add_updater(lambda m: set_dashed_endpoints(m,
            m.axes.c2p(min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)), 0),
            m.axes.c2p(min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)), m.price.get_value())).set_opacity(m.visibility.get_value()))

        # These are actual per-lot rectangles, not areas under the fitted lines.
        cs_cells, ps_cells, loss_cells = VGroup(), VGroup(), VGroup()
        for rank, (mb, mc) in enumerate(zip(BUYER_MB, SELLER_MC), start=1):
            cs = Polygon(ax.c2p(rank - 1, 4), ax.c2p(rank, 4), ax.c2p(rank, max(4, mb)), ax.c2p(rank - 1, max(4, mb)),
                         fill_color=DEMAND, fill_opacity=0.28, stroke_width=0)
            cs.axes, cs.rank, cs.mb, cs.mc, cs.price, cs.visibility = ax, rank, mb, mc, price, show_welfare
            cs.add_updater(lambda m: m.set_points_as_corners([
                m.axes.c2p(m.rank - 1, m.price.get_value()), m.axes.c2p(m.rank, m.price.get_value()),
                m.axes.c2p(m.rank, max(m.price.get_value(), m.mb)), m.axes.c2p(m.rank - 1, max(m.price.get_value(), m.mb)),
                m.axes.c2p(m.rank - 1, m.price.get_value())]).set_fill(opacity=0.28 * m.visibility.get_value() * float(m.mc <= m.price.get_value() + 1e-7 and m.mb + 1e-7 >= m.price.get_value())))
            ps = Polygon(ax.c2p(rank - 1, min(4, mc)), ax.c2p(rank, min(4, mc)), ax.c2p(rank, 4), ax.c2p(rank - 1, 4),
                         fill_color=SUPPLY, fill_opacity=0.28, stroke_width=0)
            ps.axes, ps.rank, ps.mb, ps.mc, ps.price, ps.visibility = ax, rank, mb, mc, price, show_welfare
            ps.add_updater(lambda m: m.set_points_as_corners([
                m.axes.c2p(m.rank - 1, min(m.price.get_value(), m.mc)), m.axes.c2p(m.rank, min(m.price.get_value(), m.mc)),
                m.axes.c2p(m.rank, m.price.get_value()), m.axes.c2p(m.rank - 1, m.price.get_value()),
                m.axes.c2p(m.rank - 1, min(m.price.get_value(), m.mc))]).set_fill(opacity=0.28 * m.visibility.get_value() * float(m.mc <= m.price.get_value() + 1e-7 and m.mb + 1e-7 >= m.price.get_value())))
            cs_cells.add(cs)
            ps_cells.add(ps)
            if rank < 40:
                loss = Polygon(ax.c2p(rank - 1, mc), ax.c2p(rank, mc), ax.c2p(rank, mb), ax.c2p(rank - 1, mb),
                               fill_color=MUTED, fill_opacity=0, stroke_color=MUTED, stroke_width=1.2)
                loss.rank, loss.price, loss.mb_values, loss.mc_values = rank, price, BUYER_MB, SELLER_MC
                loss.visibility, loss.shade = show_loss, loss_fill
                loss.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank > min(np.count_nonzero(m.mb_values + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc_values <= m.price.get_value() + 1e-7)))).set_fill(opacity=0.30 * m.shade.get_value() * m.visibility.get_value() * float(m.rank > min(np.count_nonzero(m.mb_values + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc_values <= m.price.get_value() + 1e-7)))))
                loss_cells.add(loss)
        fixed(cs_cells)
        fixed(ps_cells)
        fixed(loss_cells)

        counts = fixed(VGroup())
        for side, color in [('buyer', DEMAND), ('seller', SUPPLY)]:
            number = fixed(Integer(40, color=color)).scale(0.50)
            number.axes, number.price, number.mb, number.mc = ax, price, BUYER_MB, SELLER_MC
            number.side, number.visibility, number.side_color = side, show_counts, color
            number.add_updater(lambda m: m.set_value(int(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value())
                if m.side == 'buyer' else np.count_nonzero(m.mc <= m.price.get_value() + 1e-7))))
            number.add_updater(lambda m: setattr(m, 'equal', np.count_nonzero(m.mb + 1e-7 >= m.price.get_value())
                == np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))
            number.add_updater(lambda m: m.next_to(m.axes.c2p(m.get_value(), 0), DOWN, buff=0.10)
                .set_color(CAPTION if m.equal else m.side_color)
                .set_opacity(m.visibility.get_value() * float(m.side == 'buyer' or not m.equal)))
            counts.add(number)
        # Price stays beside its y-axis level. When a bound binds, its label is the price label.
        price_word = Tex(r'$P=$ \$', color=GUIDE).scale(0.58)
        price_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.58)
        price_number.price = price
        price_number.add_updater(lambda m: m.set_value(m.price.get_value()))
        price_readout = fixed(VGroup(price_word, price_number).arrange(RIGHT, buff=0.05))
        price_readout.axes, price_readout.price = ax, price
        price_readout.ceiling, price_readout.floor_limit = ceiling, floor_limit
        price_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.05).next_to(
            m.axes.c2p(0, m.price.get_value()), LEFT, buff=0.16).set_opacity(float(
            abs(m.price.get_value() - m.ceiling.get_value()) > 1e-7 and
            abs(m.price.get_value() - m.floor_limit.get_value()) > 1e-7)))

        # Dollar totals use only the selected whole lots, including the zero-gain 40th.
        totals = fixed(VGroup())
        for label, x, kind, color, initial in [('CS', -5.15, 'cs', DEMAND, 156000), ('PS', -1.75, 'ps', SUPPLY, 39000), ('TS', 1.70, 'ts', TOTAL, 195000), ('DWL', 5.2, 'dwl', CAPTION, 0)]:
            word = fixed(Tex(rf'{label}: \$', color=color).scale(0.55).move_to([x - 0.78, -3.15, 0]))
            number = fixed(Integer(initial, color=color, group_with_commas=True).scale(0.55).move_to([x + 0.57, -3.15, 0]))
            number.price, number.mb, number.mc, number.kind, number.visibility = price, BUYER_MB, SELLER_MC, kind, show_totals
            number.anchor = np.array([x + 0.57, -3.15, 0])
            number.add_updater(lambda m: m.set_value(int(round(
                sum((v - m.price.get_value()) * 1000 for i, v in enumerate(m.mb) if v + 1e-7 >= m.price.get_value() and m.mc[i] <= m.price.get_value() + 1e-7) if m.kind == 'cs' else
                sum((m.price.get_value() - c) * 1000 for i, c in enumerate(m.mc[:len(m.mb)]) if c <= m.price.get_value() + 1e-7 and m.mb[i] + 1e-7 >= m.price.get_value()) if m.kind == 'ps' else
                sum((v - m.mc[i]) * 1000 for i, v in enumerate(m.mb) if v + 1e-7 >= m.price.get_value() and m.mc[i] <= m.price.get_value() + 1e-7) if m.kind == 'ts' else
                195000 - sum((v - m.mc[i]) * 1000 for i, v in enumerate(m.mb) if v + 1e-7 >= m.price.get_value() and m.mc[i] <= m.price.get_value() + 1e-7)
            ))).move_to(m.anchor).set_opacity(m.visibility.get_value()))
            word.visibility = show_totals
            word.add_updater(lambda m: m.set_opacity(m.visibility.get_value()))
            totals.add(word, number)

        # ---- 6.a · Exact gains in the market just proved efficient.
        head = fixed(title('What changes when the price is controlled?'))
        caption = fixed(Tex('Each filled strip is the gain on one 1,000-lb trade.', color=INK).scale(0.74).move_to([0, -3.66, 0]))
        self.add(head, crowd, crowd_marks, cs_cells, ps_cells, loss_cells, graph, actual_line,
                 trade_guide, counts, price_readout, totals, caption)
        self.pause('6.a')

        # ---- 6.b · A legal maximum need not be the price people actually pay.
        ceiling.set_value(5)
        ceiling_line = fixed(DashedLine(ax.c2p(0, 5), ax.c2p(40, 5), color=GUIDE, stroke_width=2.2))
        ceiling_line.axes, ceiling_line.limit = ax, ceiling
        ceiling_line.level = ceiling
        ceiling_line.add_updater(lambda m: set_dashed_endpoints(m,
            m.axes.c2p(0, m.level.get_value()),
            m.axes.c2p(max(0, min(60 - 5 * m.level.get_value(), 20 * (m.level.get_value() - 2), 100)), m.level.get_value())))
        ceiling_word = Tex(r'Ceiling \$', color=GUIDE).scale(0.58)
        ceiling_number = DecimalNumber(5, num_decimal_places=2, color=GUIDE).scale(0.58)
        ceiling_number.limit = ceiling
        ceiling_number.add_updater(lambda m: m.set_value(m.limit.get_value()))
        ceiling_readout = fixed(VGroup(ceiling_word, ceiling_number).arrange(RIGHT, buff=0.05))
        ceiling_readout.axes, ceiling_readout.limit = ax, ceiling
        ceiling_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.05).next_to(
            m.axes.c2p(0, m.limit.get_value()), LEFT, buff=0.16))
        nonbinding = fixed(Tex(r'A $\$5$ ceiling allows the $\$4$ equilibrium price.', color=INK).scale(0.77).move_to([0, -3.66, 0]))
        self.play(FadeIn(ceiling_line), FadeIn(ceiling_readout), FadeOut(caption), FadeIn(nonbinding))
        self.pause('6.b')

        # ---- 6.c · Ask before the counts, trading circles and areas return.
        self.play(show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0),
                  show_sellers.animate.set_value(0), show_welfare.animate.set_value(0), show_totals.animate.set_value(0))
        self.play(ceiling.animate.set_value(3), run_time=2.0, rate_func=linear)
        prediction = fixed(Tex('At the legal maximum, who is willing? How much is exchanged?', color=DEFINITION).scale(0.73).move_to([0, -3.66, 0]))
        self.play(FadeOut(nonbinding), FadeIn(prediction))
        self.pause('6.c')
        self.play(show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1))
        ag_ring = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(buyer_positions[24])
        illegal_bid = DashedLine(buyer_circles[24].get_center(), seller_circles[19].get_center(), color=GUIDE, stroke_width=2)
        blocked_at = (buyer_circles[24].get_center() + seller_circles[19].get_center()) / 2
        blocked = VGroup(Line(blocked_at + [-0.13, -0.13, 0], blocked_at + [0.13, 0.13, 0], color=GUIDE, stroke_width=4),
                         Line(blocked_at + [-0.13, 0.13, 0], blocked_at + [0.13, -0.13, 0], color=GUIDE, stroke_width=4))
        blocked_caption = fixed(Tex(r'The buyer wants to offer $\$3.25$. The $\$3$ ceiling forbids it.', color=INK).scale(0.70).move_to([0, -3.66, 0]))
        rationing = fixed(Tex('Assume the highest-MB buyers and lowest-MC sellers trade.', color=CAPTION).scale(0.52).move_to([-3.50, -2.87, 0]))
        self.play(Create(ag_ring), Create(illegal_bid), Create(blocked), FadeIn(rationing), FadeOut(prediction), FadeIn(blocked_caption))
        self.pause('6.c.blocked')

        # ---- 6.d · The missing gains are exact pairs 21--39. Pair 40 adds zero.
        self.play(FadeOut(ag_ring), FadeOut(illegal_bid), FadeOut(blocked), show_welfare.animate.set_value(1), show_loss.animate.set_value(1))
        zero_pair = fixed(Circle(radius=0.10, color=MUTED, stroke_width=2).move_to(ax.c2p(40, 4)))
        lost_caption = fixed(Tex('Deadweight loss: total surplus lost from missing beneficial trades.', color=INK).scale(0.72).move_to([0, -3.66, 0]))
        self.play(Create(zero_pair), FadeOut(blocked_caption), FadeIn(lost_caption))
        self.pause('6.d')

        # ---- 6.e · Sum the crowd's rectangles, with no continuous approximation.
        self.play(loss_fill.animate.set_value(1), show_totals.animate.set_value(1))
        ceiling_result = fixed(Tex(r'20,000 lb traded. Lost gains: $\$47{,}500$.', color=INK).scale(0.78).move_to([0, -3.66, 0]))
        self.play(FadeOut(lost_caption), FadeIn(ceiling_result))
        self.pause('6.e')

        # Exercise wording is copied from the author-owned Exercise_B4.typ.
        exercise_cover = fixed(Rectangle(width=16, height=8, stroke_width=0, fill_color=BG, fill_opacity=1))
        exercise_title = fixed(title('Exercise B4 Q1 | A Price Ceiling'))
        exercise_equations = fixed(VGroup(
            Tex(r'$P=12-Q_d/2$', color=INK),
            Tex(r'$P=2+Q_s/2$', color=INK),
        ).scale(0.90).arrange(RIGHT, buff=0.90).move_to([0, 2.55, 0]))
        exercise_context = fixed(VGroup(
            Tex('Prices are in galleons and quantity is in pasties.'),
            Tex('The equilibrium you found is 10 pasties at 7 galleons.'),
            Tex('The government sets a maximum legal price of 5 galleons.'),
            Tex('From Exercise B3, at 5 galleons the quantity demanded is 14 and the quantity supplied is 6.'),
        ).scale(0.64).arrange(DOWN, buff=0.17).move_to([0, 1.20, 0]))
        exercise_questions = fixed(VGroup(
            Tex('a) How many pasties are exchanged?'),
            Tex('b) What is consumer surplus?'),
            Tex('c) What is producer surplus?'),
            Tex('d) What is deadweight loss?'),
            Tex('e) Plot the demand curve, the supply curve, and the ceiling, and shade'),
            Tex('consumer surplus, producer surplus, and deadweight loss.'),
        ).scale(0.73).arrange(DOWN, aligned_edge=LEFT, buff=0.20).move_to([0, -1.35, 0]))
        exercise = fixed(VGroup(exercise_cover, exercise_title, exercise_equations, exercise_context, exercise_questions))
        self.play(FadeIn(exercise))
        self.pause('6.exercise_ceiling')
        self.play(FadeOut(exercise))

        # ---- 6.f · Return to equilibrium, then compare a minimum legal price.
        self.play(ceiling.animate.set_value(13), show_loss.animate.set_value(0), run_time=1.3)
        self.play(FadeOut(ceiling_line), FadeOut(ceiling_readout), FadeOut(zero_pair), FadeOut(rationing))
        floor_limit.set_value(3)
        floor_line = fixed(DashedLine(ax.c2p(0, 3), ax.c2p(40, 3), color=GUIDE, stroke_width=2.2))
        floor_line.axes, floor_line.limit = ax, floor_limit
        floor_line.level = floor_limit
        floor_line.add_updater(lambda m: set_dashed_endpoints(m,
            m.axes.c2p(0, m.level.get_value()),
            m.axes.c2p(max(0, min(60 - 5 * m.level.get_value(), 20 * (m.level.get_value() - 2), 100)), m.level.get_value())))
        floor_word = Tex(r'Floor \$', color=GUIDE).scale(0.58)
        floor_number = DecimalNumber(3, num_decimal_places=2, color=GUIDE).scale(0.58)
        floor_number.limit = floor_limit
        floor_number.add_updater(lambda m: m.set_value(m.limit.get_value()))
        floor_readout = fixed(VGroup(floor_word, floor_number).arrange(RIGHT, buff=0.05))
        floor_readout.axes, floor_readout.limit = ax, floor_limit
        floor_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.05).next_to(
            m.axes.c2p(0, m.limit.get_value()), LEFT, buff=0.16))
        floor_nonbinding = fixed(Tex(r'A $\$3$ floor allows the $\$4$ equilibrium price.', color=INK).scale(0.77).move_to([0, -3.66, 0]))
        self.play(FadeIn(floor_line), FadeIn(floor_readout), FadeOut(ceiling_result), FadeIn(floor_nonbinding))
        self.pause('6.f.nonbinding')
        self.play(show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0),
                  show_sellers.animate.set_value(0), show_welfare.animate.set_value(0), show_totals.animate.set_value(0))
        self.play(floor_limit.animate.set_value(6), run_time=2.0, rate_func=linear)
        floor_question = fixed(Tex('At the legal minimum, who is willing? How much is exchanged?', color=DEFINITION).scale(0.73).move_to([0, -3.66, 0]))
        self.play(FadeOut(floor_nonbinding), FadeIn(floor_question))
        self.pause('6.f')

        # ---- 6.g · The incentive to undercut remains, but the legal bid cannot.
        self.play(show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1), show_welfare.animate.set_value(1))
        andrew_ring = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(seller_positions[39])
        illegal_cut = DashedLine(seller_circles[39].get_center(), buyer_circles[29].get_center(), color=GUIDE, stroke_width=2)
        blocked_at = (seller_circles[39].get_center() + buyer_circles[29].get_center()) / 2
        blocked_cut = VGroup(Line(blocked_at + [-0.13, -0.13, 0], blocked_at + [0.13, 0.13, 0], color=GUIDE, stroke_width=4),
                             Line(blocked_at + [-0.13, 0.13, 0], blocked_at + [0.13, -0.13, 0], color=GUIDE, stroke_width=4))
        cut_caption = fixed(Tex(r'The seller wants to ask $\$5.75$. The $\$6$ floor forbids it.', color=INK).scale(0.73).move_to([0, -3.66, 0]))
        no_purchases = fixed(Tex('No government purchases. Highest MB and lowest MC trade.', color=CAPTION).scale(0.52).move_to([-3.50, -2.87, 0]))
        self.play(Create(andrew_ring), Create(illegal_cut), Create(blocked_cut), FadeIn(no_purchases), FadeOut(floor_question), FadeIn(cut_caption))
        self.pause('6.g')

        # ---- 6.h · The efficient missing pairs are now 31--39, plus zero pair 40.
        self.play(FadeOut(andrew_ring), FadeOut(illegal_cut), FadeOut(blocked_cut), show_loss.animate.set_value(1), show_totals.animate.set_value(1))
        floor_result = fixed(Tex(r'30,000 lb traded. Lost gains: $\$11{,}250$.', color=INK).scale(0.78).move_to([0, -3.66, 0]))
        self.play(FadeOut(cut_caption), FadeIn(floor_result))
        self.pause('6.h')

        exercise_title = fixed(title('Exercise B4 Q2 | A Price Floor'))
        exercise_context = fixed(VGroup(
            Tex('Prices are in galleons and quantity is in pasties.'),
            Tex('The equilibrium you found is 10 pasties at 7 galleons.'),
            Tex('Suppose instead the government sets a minimum legal price of 9 galleons.'),
            Tex('Now the quantity demanded is 6 and the quantity supplied is 14.'),
        ).scale(0.67).arrange(DOWN, buff=0.20).move_to([0, 1.20, 0]))
        exercise_questions = fixed(VGroup(
            Tex('a) How many pasties are exchanged?'),
            Tex('b) What is producer surplus?'),
            Tex('c) What is deadweight loss?'),
            Tex('d) Would a floor of 6 galleons change the market?'),
        ).scale(0.79).arrange(DOWN, aligned_edge=LEFT, buff=0.34).move_to([0, -1.10, 0]))
        exercise = fixed(VGroup(exercise_cover, exercise_title, exercise_equations, exercise_context, exercise_questions))
        self.play(FadeIn(exercise))
        self.pause('6.exercise_floor')
        self.play(FadeOut(exercise))

        # ---- 7.a · Restore the maximum, without pretending efficiency is every goal.
        self.play(floor_limit.animate.set_value(0), show_loss.animate.set_value(0), run_time=1.4)
        self.play(FadeOut(floor_line), FadeOut(floor_readout), FadeOut(no_purchases))
        closing_head = fixed(title('What does the welfare result tell us?'))
        closing = fixed(Tex('Efficiency maximizes total gains. Distribution and other goals still matter.', color=INK).scale(0.70).move_to([0, -3.66, 0]))
        self.play(FadeOut(head), FadeIn(closing_head), FadeOut(floor_result), FadeIn(closing))
        self.pause('7.a')
