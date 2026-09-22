# maniml 03_02_Bidding.py B4Bidding
# B4 | B3's approved 2.c stage, camera, bars, and accepted-price treatment.

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

# Refresh the pure model when ManimLive reloads this scene.
simulate = reload(discovery).simulate

# A modest inset keeps Amanda-Grace's long plaza label close to her orb.
PLAZA_NAME_INSET = 0.65


class B4Bidding(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
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
        stay_box = fixed(RoundedRectangle(width=5.5, height=1.0, corner_radius=0.12,
            color=MUTED, fill_color=BG, fill_opacity=1, stroke_width=1.5).move_to([-3.05, -2.85, 0]))
        offer_box = fixed(stay_box.copy().move_to([3.05, -2.85, 0]))
        stay_text = fixed(VGroup(Tex('Stay out', color=INK), Tex(r'Gain $\$0$', color=DEMAND))
            .arrange(DOWN, buff=0.10).scale(0.68).move_to(stay_box))
        offer_text = fixed(VGroup(Tex(r'Offer $\$4.25$', color=INK), Tex(r'Gain $\$2.75$', color=DEMAND))
            .arrange(DOWN, buff=0.10).scale(0.68).move_to(offer_box))
        seller_gain = fixed(Tex(r'Molly receives $\$0.25$ more.', color=SUPPLY).scale(0.7)
            .move_to([0, -3.62, 0]))
        self.play(FadeIn(stay_box), FadeIn(offer_box), FadeIn(stay_text), FadeIn(offer_text), FadeIn(seller_gain))
        self.pause('1.b')
        self.play(FadeOut(stay_box), FadeOut(offer_box), FadeOut(stay_text), FadeOut(offer_text),
                  FadeOut(seller_gain), Transform(head, fixed(title('Who gets the spinach?'))), run_time=0.3)
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
