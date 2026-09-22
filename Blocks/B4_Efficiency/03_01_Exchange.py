# maniml 03_01_Exchange.py B4Exchange
# B4: B3's actual plaza, camera move, and one-pound accounting geometry.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from scene_layers import fixed, add_market_objects


class B4Exchange(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
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
