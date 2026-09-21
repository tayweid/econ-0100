# maniml 03_Equilibrium.py EpisodeB3
# B3 | Equilibrium. Flat scene; current beat map is in 02_Storyboard.md.

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


class EpisodeB3(ThreeDScene):
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

        # ---- 0.a · Shared B1/B2 bumper, before turning into the 3D world.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'B', 3)
        thesis = Tex(r'\textit{Equilibrium: when no one wants to change}',
                     color=CAPTION).scale(1.1).next_to(episode, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
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
        self.pause('2.a')

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
        question = fixed(Tex('Would they both accept this price?', color=DEFINITION)
                         .scale(DEFINITION_SCALE))
        question.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(zero), FadeIn(zero_word), FadeIn(price_line),
                  FadeIn(price_shadow), FadeIn(price_word))
        self.play(FadeIn(question))
        self.pause('2.a.i')

        # ---- 2.b · Accept first, then recall the two views of the same exchange.
        # Fade after a teaching pause: the movie player parks at the next frame.
        self.play(FadeOut(question), run_time=0.2)
        accepted_line = Line([left_edge, -0.045, price_z],
                             [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        # Acceptance fills the gaps without stretching or moving the dashes.
        price_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=3)
            for a, b in zip(price_line, price_line[1:])])
        shadow_gaps = VGroup(*[
            Line(a.get_end(), b.get_start(), color=GUIDE, stroke_width=2).set_opacity(0.3)
            for a, b in zip(price_shadow, price_shadow[1:])])
        self.play(FadeIn(price_gaps), FadeIn(shadow_gaps), run_time=0.45)
        self.remove(price_line, price_shadow, price_gaps, shadow_gaps)
        self.add(accepted_line, accepted_shadow)
        self.pause('2.b')

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
        self.play(bars['buyer'].animate.set_opacity(0.13), FadeIn(expenditure))
        self.play(FadeIn(expenditure_label))
        self.pause('2.b.i')

        # ---- 2.b.ii · Consumer surplus stays above the same price line.
        cs_label = Tex(rf'CS $\${MB - OFFER:g}$', color=DEMAND).scale(0.62)
        cs_label.face_mat = np.eye(3)
        cs_label.add_updater(face_camera)
        cs_label.update()
        cs_label.move_to(
            [left_edge - 0.3, -0.10, BAR_BASE + (OFFER + MB) * DOLLAR_HEIGHT / 2], aligned_edge=RIGHT)
        self.play(FadeIn(buyer_cs))
        self.play(FadeIn(cs_label))
        self.pause('2.b.ii')

        # ---- 2.b.iii · The same payment: carry expenditure's boundary to revenue.
        revenue = expenditure.copy().set_fill(opacity=0).set_stroke(GOV, width=2.5)
        revenue.shift([0, -0.005, 0])
        revenue_label = Tex(rf'Revenue $\${OFFER:g}$', color=GOV).scale(0.62)
        revenue_label.face_mat = np.eye(3)
        revenue_label.add_updater(face_camera)
        revenue_label.update()
        revenue_label.move_to([right_edge + 0.3, -0.10, price_z + 0.2], aligned_edge=LEFT)
        self.play(ShowCreation(revenue), run_time=0.6)
        self.play(revenue.animate.shift(RIGHT * (CLOSE_WIDTH + CLOSE_GAP)), run_time=1.4)
        self.play(FadeIn(revenue_label))
        self.pause('2.b.iii')

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
        self.play(bars['seller'].animate.set_opacity(0.13), FadeIn(seller_cost),
                  cost_label.animate.move_to(cost_at, aligned_edge=LEFT), run_time=1.2)
        self.pause('2.b.iv')
        self.play(ShowCreation(seller_ps))
        self.play(FadeIn(ps_label))
        self.pause('2.b.v')

        # ---- 2.b.vi · The one unit never changes size economically.
        unit = fixed(Tex('One unit', color=CAPTION).scale(0.7))
        unit.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(unit))
        self.pause('2.b.vi')

        # ---- 2.c · Stay close: Gary / Molly / Amanda-Grace, viewed head-on.
        self.play(FadeOut(unit), run_time=0.2)
        self.play(FadeOut(expenditure), FadeOut(buyer_cs), FadeOut(revenue),
                  FadeOut(seller_cost), FadeOut(seller_ps), FadeOut(expenditure_label),
                  FadeOut(cs_label), FadeOut(revenue_label), FadeOut(cost_label),
                  FadeOut(ps_label), FadeOut(zero), FadeOut(zero_word), FadeOut(price_word))
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
        head = fixed(title('What would Amanda-Grace gain?'))
        self.play(FadeIn(head), FadeIn(deal_number),
                  FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))
        self.pause('2.c')

        # ---- 2.c.i–iii · See both prices; move MC; fill the accepted offer's gaps.
        bidding = simulate([MB, 7], [MC], [OFFER], seed=0, initial_sellers=[0, None])
        bids = [event for round_ in bidding.rounds for event in round_.events
                if event.kind == 'match']
        assert bidding.final.asks == (6.25,) and bidding.final.sellers == (None, 0)
        for bid in bids:
            bidder = 'buyer' if bid.buyer == 0 else 'challenger'
            mc_x = bid_mc_x[bidder]
            x0 = min(bid_mb_x[bidder], mc_x) - BID_WIDTH / 2
            x1 = max(bid_mb_x[bidder], mc_x) + BID_WIDTH / 2
            height = BID_BASE + bid.price * BID_DOLLAR_HEIGHT
            challenge = DashedLine([x0, bid_y - 0.045 * BID_SCALE, height],
                                  [x1, bid_y - 0.045 * BID_SCALE, height],
                                  dash_length=0.05 * BID_SCALE,
                                  color=GUIDE, stroke_width=3 * BID_SCALE)
            challenge_shadow = DashedLine([x0, bid_y, 0.04 * BID_SCALE],
                                         [x1, bid_y, 0.04 * BID_SCALE],
                                         dash_length=0.05 * BID_SCALE,
                                         color=GUIDE, stroke_width=2 * BID_SCALE).set_opacity(0.3)
            offer_label = Tex(rf'\${bid.price:.2f}', color=GUIDE).scale(0.62 * BID_SCALE)
            offer_label.set_fill(border_width=0.5 * BID_SCALE)
            offer_label.face_mat = np.eye(3)
            offer_label.add_updater(face_camera)
            offer_label.update()
            offer_label.move_to([(x0 + x1) / 2, bid_y - 0.15 * BID_SCALE,
                                 height + 0.25 * BID_SCALE])
            self.play(FadeIn(challenge), FadeIn(challenge_shadow), FadeIn(offer_label),
                      run_time=0.6 if bid.price <= 4.5 else 0.35)
            if bid.price == 4.25:
                bid_question = fixed(Tex(r'Would Amanda-Grace gain by offering $\$4.25$?',
                    color=DEFINITION).scale(DEFINITION_SCALE)
                    .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                self.play(FadeIn(bid_question))
                self.pause('2.c.i')
                self.play(FadeOut(bid_question), run_time=0.2)
            if bid.price == 4.5:
                self.pause('2.c.ii')
            # Keep the old solid price and the new dashed price visible until
            # Molly's unchanged MC-$2 bar reaches the newly preferred buyer.
            self.play(bars['seller'].animate.set_x(mc_x),
                      run_time=1.2 if bid.price <= 4.5 else 0.7)
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
            if bid.price == 4.25:
                gain_read = fixed(Tex(r'Amanda-Grace gains $\$7-\$4.25=\$2.75$.',
                    color=DEMAND).scale(DEFINITION_SCALE)
                    .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                self.play(FadeIn(gain_read))
                self.pause('2.c.accepted')
                self.play(FadeOut(gain_read), run_time=0.2)
        stop_reason = fixed(Tex(r'Gary: next bid $\$6.50 > \mathrm{MB}\ \$6$.',
                               color=DEFINITION).scale(DEFINITION_SCALE))
        stop_reason.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(stop_reason))
        self.pause('2.c.iii')

        # ---- 3.a · Reveal the arcs, with the unmatched buyer on the buyer side.
        self.play(FadeOut(stop_reason), *[FadeOut(m) for m in marginal_labels.values()],
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
        self.pause('3.a.plaza')

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
            panel_ticks = VGroup(*[Tex(str(p), color=MUTED).scale(0.7).next_to(
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
            FadeIn(posted_caption), run_time=0.8)
        # Buyers have separate circle-arrival and price-comparison holds.
        # The long buyer name stays toward the plaza interior on either arc.
        self.pause('3.a.overview')

        arrival_order = [('S', 4)] + [(side, i) for i in [1, 2, 3, 5, 6, 7, 8, 9] for side in ['B', 'S']]
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
            self.play(*entrances, run_time=0.9 if i in [1, 2, 4] else 0.5)
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
            self.play(*rearrange, run_time=0.8 if i in [1, 2, 4] else 0.4)
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
                self.play(FadeOut(entry_caption), run_time=0.2)
                entry_caption = None
                entry_names = {}
                for key, word, offset in [
                    (('B', 0), 'Gary', DOWN * 0.55),
                    (('B', 4), 'Amanda-Grace', DOWN * 0.55),
                    (('S', 0), 'Molly', DOWN * 0.55 + RIGHT * 0.6),
                    (('S', 4), 'Andrew', DOWN * 0.55 + RIGHT * 0.6),
                ]:
                    label = Tex(word, color=INK).scale(0.60)
                    label.face_mat = np.eye(3)
                    label.add_updater(face_camera)
                    label.anchor, label.offset = crowd_bodies[key], offset
                    label.inward = key == ('B', 4)
                    label.add_updater(lambda m: m.move_to(
                        np.array([*m.anchor.get_center()[:2], 0.13]) + m.offset
                        + (LEFT * 1.8 * np.clip(m.anchor.get_x(), -1, 1) if m.inward else ORIGIN)))
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
                self.pause('3.a.entry')
                self.play(FadeOut(ask_world), FadeOut(ask_caption), run_time=0.3)

                # Both buyers revisit the lookout; neither seller changes station.
                for chooser, offer, displaced in [(4, 4.25, None), (0, 4.5, 4)]:
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
                              hub.animate.set_stroke(opacity=1), run_time=1.2)
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
                        self.pause('3.a.switch.options')
                    else:
                        self.pause('3.a.counter.options')
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
                    self.play(*moves, price_trackers[4].animate.set_value(offer), run_time=1.2)
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
                    if chooser == 4:
                        self.pause('3.a.switch.accepted')
                    else:
                        self.pause('3.a.counter.accepted')
                    self.play(FadeOut(buyer_focus), FadeOut(buyer_ring), FadeOut(mb_guide), FadeOut(mb_read),
                              FadeOut(price_caption), FadeOut(option_rings[4]),
                              FadeOut(option_columns[4]), FadeOut(option_prices[4]),
                              hub.animate.set_stroke(opacity=0.6), run_time=0.4)
                self.play(FadeIn(posted_caption), run_time=0.3)
            # ---- 3.a.two_pairs / third_buyer · Finish each small market first.
            if (side, i) in [('S', 4), ('B', 1)]:
                two_by_two = side == 'S'
                if two_by_two:
                    local_buyers = [0, 4]
                    small_run = simulate([6, 7], [2, 4], [6.25, 4.5],
                        initial_sellers=[1, None], seed=54, step=BID_STEP)
                    assert small_run.final.asks == (5.5, 5.5)
                else:
                    self.play(FadeOut(entry_caption), run_time=0.2)
                    entry_caption = None
                    new_name = Tex('New buyer', color=INK).scale(0.60)
                    new_name.face_mat = np.eye(3)
                    new_name.add_updater(face_camera)
                    new_name.anchor = crowd_bodies['B', 1]
                    new_name.add_updater(lambda m: m.move_to(
                        [m.anchor.get_center()[0] - 0.3, m.anchor.get_center()[1] - 0.55, 0.13]))
                    new_name.update()
                    entry_names['B', 1] = new_name
                    third_caption = fixed(Tex('Three buyers. Two units.', color=DEFINITION)
                        .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                    self.play(FadeIn(new_name), FadeIn(third_caption))
                    self.pause('3.a.third_buyer')
                    self.play(FadeOut(third_caption), run_time=0.2)
                    local_buyers = [0, 4, 1]
                    small_run = simulate([6, 7, 8], [2, 4], [5.5, 5.5],
                        initial_sellers=[1, 0, None], seed=6, step=BID_STEP)
                    assert small_run.final.asks == (6.25, 6.25)
                    assert small_run.final.sellers == (None, 1, 0)
                local_sellers = [0, 4]
                assert tuple(crowd_asks[s] for s in local_sellers) == small_run.initial.asks
                assert tuple(None if crowd_matches[b] is None else
                    local_sellers.index(crowd_matches[b]) for b in local_buyers) == small_run.initial.sellers
                for small_round in small_run.rounds:
                    for event in small_round.events:
                        if event.kind == 'check':
                            continue
                        s = local_sellers[event.seller]
                        if event.kind == 'cut':
                            if two_by_two and event.price == 6:
                                cut_question = fixed(Tex('Would Molly lower her price?',
                                    color=DEFINITION).scale(DEFINITION_SCALE)
                                    .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                                self.play(FadeIn(cut_question))
                                self.pause('3.a.seller.cut')
                                self.play(FadeOut(cut_question), run_time=0.2)
                            seller_focus = fixed(SurroundingRectangle(panel_bars['S', s],
                                color=SUPPLY, buff=0.035, stroke_width=3))
                            origin = posted_marks[s].get_center() + UP * 0.22
                            cut_arrow = fixed(Arrow(origin + UP * 0.2, origin + DOWN * 0.2,
                                color=GUIDE, buff=0, thickness=1.2, tip_width_ratio=4))
                            crowd_asks[s] = event.price
                            self.play(FadeIn(seller_focus), FadeIn(cut_arrow),
                                price_trackers[s].animate.set_value(event.price), run_time=0.8)
                            self.play(FadeOut(seller_focus), FadeOut(cut_arrow), run_time=0.25)
                            continue
                        b = local_buyers[event.buyer]
                        displaced = (None if event.displaced is None
                                     else local_buyers[event.displaced])
                        body = crowd_bodies['B', b]
                        if b in connection_by_buyer:
                            old_line = connection_by_buyer.pop(b)
                            old_ground = ground_by_buyer.pop(b)
                            self.play(FadeOut(old_line), FadeOut(old_ground),
                                crowd_bars['B', b].pairing.animate.set_value(0),
                                crowd_bars['S', crowd_matches[b]].pairing.animate.set_value(0),
                                run_time=0.2)
                        buyer_ring = Circle(radius=0.29, color=DEMAND, stroke_width=3)
                        buyer_ring.move_to([0, 0, 0.045])
                        buyer_focus = fixed(SurroundingRectangle(panel_bars['B', b],
                            color=DEMAND, buff=0.035, stroke_width=3))
                        mb_guide = fixed(DashedLine(side_axes['S'].c2p(0, CROWD_MB[b]),
                            side_axes['S'].c2p(10, CROWD_MB[b]), color=DEMAND, stroke_width=2))
                        self.play(body.animate.move_to([0, 0, body.get_center()[2]]),
                            FadeIn(buyer_focus),
                            FadeIn(buyer_ring, shift=-np.append(crowd_bodies['B', b].get_center()[:2], 0)),
                            FadeIn(mb_guide),
                            hub.animate.set_stroke(opacity=1), run_time=0.9)
                        if not two_by_two and small_round.number == 1 and b == i:
                            self.pause('3.a.third.lookout')
                        mb_read = fixed(Tex(rf'MB $\${CROWD_MB[b]}$', color=DEMAND).scale(0.7)
                            .move_to(side_axes['S'].c2p(5, CROWD_MB[b])
                                     + (DOWN if CROWD_MB[b] >= 7 else UP) * 0.35))
                        option_columns, option_prices, option_rings = {}, {}, {}
                        for rank, seller in enumerate(panel_ids['S']):
                            needed = crowd_asks[seller] + (BID_STEP
                                if seller in crowd_matches and crowd_matches[b] != seller else 0)
                            option_columns[seller] = fixed(SurroundingRectangle(panel_bars['S', seller],
                                color=SUPPLY, buff=0.035, stroke_width=3))
                            option_rings[seller] = Circle(radius=0.29, color=SUPPLY, stroke_width=3)
                            option_rings[seller].move_to([*seller_spots[seller][:2], 0.045])
                            tick = Line(side_axes['S'].c2p(rank * 5 + 0.15, needed),
                                side_axes['S'].c2p((rank + 1) * 5 - 0.15, needed),
                                color=GUIDE, stroke_width=3)
                            number = Tex(rf'$\${needed:.2f}$', color=GUIDE).scale(0.7)
                            number.move_to(side_axes['S'].c2p(rank * 5 + 2.5, needed) + DOWN * 0.36)
                            option_prices[seller] = fixed(VGroup(tick, number))
                        offer_read = fixed(Tex(rf'Buy for $\${event.price:.2f}$', color=GUIDE)
                            .scale(0.7).move_to([5.9, -3.05, 0]))
                        self.remove(posted_caption)
                        self.play(FadeIn(mb_read),
                            *[FadeIn(m) for m in option_columns.values()],
                            *[FadeIn(m) for m in option_rings.values()],
                            *[FadeIn(m) for m in option_prices.values()], run_time=0.6)
                        self.wait(0.5)
                        if not two_by_two and small_round.number == 1:
                            third_question = fixed(Tex(r'Would the new buyer offer $\$5.75$?',
                                color=DEFINITION).scale(DEFINITION_SCALE)
                                .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                            self.play(FadeIn(third_question))
                            self.pause('3.a.third.options')
                            self.play(FadeOut(third_question), run_time=0.2)
                        self.play(FadeIn(offer_read),
                            *[m.animate.set_stroke(opacity=0.25) for seller, m in option_columns.items() if seller != s],
                            *[m.animate.set_stroke(opacity=0.25) for seller, m in option_rings.items() if seller != s],
                            *[m.animate.set_opacity(0.25) for seller, m in option_prices.items() if seller != s], run_time=0.35)
                        if displaced is not None:
                            old_line = connection_by_buyer.pop(displaced)
                            old_ground = ground_by_buyer.pop(displaced)
                            self.play(FadeOut(old_line), FadeOut(old_ground),
                                crowd_bars['B', displaced].pairing.animate.set_value(0),
                                crowd_bars['S', crowd_matches[displaced]].pairing.animate.set_value(0),
                                run_time=0.2)
                        seller_at = seller_spots[s]
                        destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                        route = DashedLine([0, 0, 0.045], [*destination[:2], 0.045],
                            color=MUTED, stroke_width=2).set_opacity(0.7)
                        moves = [body.animate.move_to([*destination[:2], body.get_center()[2]]),
                                 buyer_ring.animate.move_to([*destination[:2], 0.045])]
                        if displaced is not None:
                            displaced_body = crowd_bodies['B', displaced]
                            moves.append(displaced_body.animate.move_to(
                                [*buyer_spots[displaced][:2], displaced_body.get_center()[2]]))
                            crowd_matches[displaced] = None
                        crowd_matches[b], crowd_asks[s] = s, event.price
                        self.play(FadeIn(route), run_time=0.2)
                        self.play(*moves, price_trackers[s].animate.set_value(event.price), run_time=0.9)
                        for key, partner in [(('B', b), ('S', s)), (('S', s), ('B', b))]:
                            crowd_bars[key].partner = crowd_bodies[partner]
                        self.play(crowd_bars['B', b].pairing.animate.set_value(1),
                                  crowd_bars['S', s].pairing.animate.set_value(1), run_time=0.4)
                        midpoint = (destination[:2] + seller_at[:2]) / 2
                        pair_left = midpoint - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                        pair_right = midpoint + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                        height = CROWD_BASE + event.price * CROWD_SCALE
                        connection_by_buyer[b] = Line([*pair_left, height], [*pair_right, height],
                            color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                        ground_by_buyer[b] = Line([*pair_left, 0.04], [*pair_right, 0.04],
                            color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
                        self.play(FadeOut(route), FadeIn(connection_by_buyer[b]),
                            FadeIn(ground_by_buyer[b]), run_time=0.3)
                        self.play(FadeOut(buyer_focus), FadeOut(buyer_ring), FadeOut(mb_guide), FadeOut(mb_read),
                            *[FadeOut(m) for m in option_columns.values()],
                            *[FadeOut(m) for m in option_rings.values()],
                            *[FadeOut(m) for m in option_prices.values()], FadeOut(offer_read),
                            hub.animate.set_stroke(opacity=0.6), run_time=0.3)
                        self.add(posted_caption)
                    assert tuple(crowd_asks[s] for s in local_sellers) == small_round.after.asks
                    assert tuple(None if crowd_matches[b] is None else
                        local_sellers.index(crowd_matches[b]) for b in local_buyers) == small_round.after.sellers
                if two_by_two:
                    same_price = fixed(Tex(r"Both trades: $\$5.50$.\quad Gary's gain: $\$0.50$.",
                        color=DEFINITION).scale(DEFINITION_SCALE)
                        .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                    self.play(FadeIn(same_price))
                    self.pause('3.a.two_pairs')
                    self.play(FadeOut(same_price), run_time=0.2)
                else:
                    gary_ring = Circle(radius=0.29, color=DEMAND, stroke_width=3)
                    gary_ring.move_to([*crowd_bodies['B', 0].get_center()[:2], 0.045])
                    gary_focus = fixed(SurroundingRectangle(panel_bars['B', 0],
                        color=DEMAND, buff=0.035, stroke_width=3))
                    gary_mb = fixed(DashedLine(side_axes['S'].c2p(0, 6),
                        side_axes['S'].c2p(10, 6), color=DEMAND, stroke_width=2))
                    excluded_question = fixed(Tex('Why is Gary left out?', color=DEFINITION)
                        .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                    self.play(FadeIn(gary_focus), FadeIn(gary_ring), FadeIn(gary_mb), FadeIn(excluded_question))
                    self.pause('3.a.excluded')
                    self.play(FadeOut(excluded_question), run_time=0.2)
                    excluded_reason = fixed(Tex(
                        r'Gary traded at $\$5.50$. Now $\$6.25>\mathrm{MB}\ \$6$.',
                        color=DEFINITION).scale(DEFINITION_SCALE)
                        .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                    self.play(FadeIn(excluded_reason))
                    self.pause('3.a.excluded.reason')
                    self.play(FadeOut(excluded_reason), FadeOut(gary_focus), FadeOut(gary_ring), FadeOut(gary_mb), run_time=0.3)
            if side == 'S' and i == 1:
                self.pause('3.a')
                self.play(FadeOut(entry_caption), run_time=0.2)
                entry_caption = None
                # One unhurried survey teaches what the center circle means.
                buyer_ring = Circle(radius=0.29, color=DEMAND, stroke_width=3)
                buyer_ring.move_to([0, 0, 0.045])
                buyer_focus = fixed(SurroundingRectangle(panel_bars['B', 0],
                    color=DEMAND, buff=0.04, stroke_width=3))
                self.play(
                    *[crowd_bodies['B', b][1].animate.set_opacity(0.2) for b in (1, 4)],
                    *[crowd_bodies['B', b][0].animate.set_opacity(0.06) for b in (1, 4)],
                    *[crowd_bars['B', b].animate.set_opacity(0.12) for b in (1, 4)],
                    *[connection_by_buyer[b].animate.set_opacity(0.2) for b in (1, 4)],
                    *[ground_by_buyer[b].animate.set_opacity(0.06) for b in (1, 4)],
                    FadeIn(buyer_focus),
                    FadeIn(buyer_ring, shift=-np.append(crowd_bodies['B', 0].get_center()[:2], 0)),
                    hub.animate.set_stroke(opacity=1),
                    crowd_bodies['B', 0].animate.move_to(
                        [0, 0, crowd_bodies['B', 0].get_center()[2]]), run_time=1.4)
                self.pause('3.a.lookout')
                supply_ax = side_axes['S']
                mb_guide = fixed(DashedLine(supply_ax.c2p(0, 6), supply_ax.c2p(10, 6),
                    color=DEMAND, stroke_width=2))
                mb_read = fixed(Tex(r'MB $\$6$', color=DEMAND).scale(0.7)
                    .move_to(supply_ax.c2p(5, 6) + UP * 0.7))
                price_caption = fixed(Tex('Price to buy', color=GUIDE).scale(0.7)
                    .move_to([5.9, -3.05, 0]))
                self.remove(posted_caption)
                self.play(FadeIn(mb_guide), FadeIn(mb_read), FadeIn(price_caption))
                option_rings, option_columns, option_prices = {}, {}, {}
                for seller in panel_ids['S']:
                    rank = panel_ids['S'].index(seller)
                    needed = crowd_asks[seller] + (BID_STEP if seller in crowd_matches else 0)
                    ring = Circle(radius=0.29, color=SUPPLY, stroke_width=3)
                    ring.move_to([*seller_spots[seller][:2], 0.045])
                    column = fixed(SurroundingRectangle(panel_bars['S', seller],
                        color=SUPPLY, buff=0.035, stroke_width=3))
                    x0, x1 = 10 * rank / 3, 10 * (rank + 1) / 3
                    tick = Line(supply_ax.c2p(x0 + 0.15, needed),
                                supply_ax.c2p(x1 - 0.15, needed), color=GUIDE, stroke_width=3)
                    number = Tex(rf'$\${needed:.2f}$', color=GUIDE).scale(0.7)
                    number.move_to(supply_ax.c2p((x0 + x1) / 2, needed)
                                   + (DOWN * 0.7))
                    price_mark = fixed(VGroup(tick, number))
                    option_rings[seller], option_columns[seller] = ring, column
                    option_prices[seller] = price_mark
                    self.play(FadeIn(ring), FadeIn(column), FadeIn(price_mark), run_time=0.8)
                choose_question = fixed(Tex('Would Gary trade with the new seller?', color=DEFINITION)
                    .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                self.play(FadeIn(choose_question))
                self.pause('3.a.options')
                self.play(FadeOut(choose_question), run_time=0.2)
                seller_at = seller_spots[1]
                destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                route = DashedLine([0, 0, 0.045], [*destination[:2], 0.045],
                                   color=MUTED, stroke_width=2).set_opacity(0.7)
                self.play(*[FadeOut(option_rings[s]) for s in (0, 4)],
                          *[FadeOut(option_columns[s]) for s in (0, 4)],
                          *[FadeOut(option_prices[s]) for s in (0, 4)],
                          FadeIn(route), run_time=0.5)
                self.play(crowd_bodies['B', 0].animate.move_to(
                    [*destination[:2], crowd_bodies['B', 0].get_center()[2]]),
                    buyer_ring.animate.move_to([*destination[:2], 0.045]), run_time=1.2)
                for key, partner in [(('B', 0), ('S', 1)), (('S', 1), ('B', 0))]:
                    crowd_bars[key].partner = crowd_bodies[partner]
                self.play(crowd_bars['B', 0].pairing.animate.set_value(1),
                          crowd_bars['S', 1].pairing.animate.set_value(1), run_time=0.4)
                midpoint = (destination[:2] + seller_at[:2]) / 2
                pair_left = midpoint - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                pair_right = midpoint + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                height = CROWD_BASE + crowd_asks[1] * CROWD_SCALE
                connection_by_buyer[0] = Line([*pair_left, height], [*pair_right, height],
                                               color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                ground_by_buyer[0] = Line([*pair_left, 0.04], [*pair_right, 0.04],
                                           color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
                crowd_matches[0] = 1
                self.play(FadeOut(route), FadeIn(connection_by_buyer[0]),
                          FadeIn(ground_by_buyer[0]), run_time=0.5)
                self.pause('3.a.chosen')
                self.play(FadeOut(buyer_focus), FadeOut(buyer_ring), FadeOut(mb_guide), FadeOut(mb_read),
                    FadeOut(price_caption), FadeOut(option_rings[1]),
                    FadeOut(option_columns[1]), FadeOut(option_prices[1]),
                    *[crowd_bodies['B', b][1].animate.set_opacity(1) for b in (1, 4)],
                    *[crowd_bodies['B', b][0].animate.set_opacity(0.28 if b == 4 else 0.22) for b in (1, 4)],
                    *[crowd_bars['B', b].animate.set_opacity(0.65) for b in (1, 4)],
                    *[connection_by_buyer[b].animate.set_opacity(1) for b in (1, 4)],
                    *[ground_by_buyer[b].animate.set_opacity(0.3) for b in (1, 4)],
                    hub.animate.set_stroke(opacity=0.6), run_time=0.6)
                self.play(*[FadeOut(label) for label in entry_names.values()], run_time=0.3)
                self.play(FadeIn(posted_caption), run_time=0.3)
            # ---- 3.a.growth · One arrival, its decisions, then the next arrival.
            if i in [2, 3, 5, 6, 7, 8, 9]:
                self.play(FadeOut(entry_caption), run_time=0.2)
                entry_caption = None
                local_buyers, local_sellers = sorted(panel_ids['B']), sorted(panel_ids['S'])
                growth = simulate([CROWD_MB[b] for b in local_buyers],
                    [CROWD_MC[s] for s in local_sellers], [crowd_asks[s] for s in local_sellers],
                    initial_sellers=[None if crowd_matches[b] is None else
                        local_sellers.index(crowd_matches[b]) for b in local_buyers],
                    survey=True, first_buyer=local_buyers.index(i) if side == 'B' else None,
                    seed=GROWTH_SEED, step=BID_STEP)
                assert growth.settled
                for round_ in growth.rounds:
                    for event_index, event in enumerate(round_.events):
                        if event.kind == 'check':
                            # Show an unsuccessful newcomer's first comparison;
                            # successful checks are shown by their match event.
                            following = (round_.events[event_index + 1]
                                if event_index + 1 < len(round_.events) else None)
                            if not (side == 'B' and round_.number == 1 and event_index == 0
                                    and (following is None or following.kind != 'match')):
                                continue
                        s = local_sellers[event.seller]
                        if event.kind == 'cut':
                            origin = posted_marks[s].get_center() + UP * 0.22
                            cut_arrow = fixed(Arrow(origin + UP * 0.2, origin + DOWN * 0.2,
                                color=GUIDE, buff=0, thickness=1.2, tip_width_ratio=4))
                            crowd_asks[s] = event.price
                            self.play(FadeIn(cut_arrow), price_trackers[s].animate.set_value(event.price),
                                      run_time=0.3)
                            self.play(FadeOut(cut_arrow), run_time=0.15)
                            continue
                        b = local_buyers[event.buyer]
                        body = crowd_bodies['B', b]
                        if b in connection_by_buyer:
                            self.play(FadeOut(connection_by_buyer.pop(b)),
                                FadeOut(ground_by_buyer.pop(b)),
                                crowd_bars['B', b].pairing.animate.set_value(0),
                                crowd_bars['S', crowd_matches[b]].pairing.animate.set_value(0), run_time=0.25)
                        buyer_ring = Circle(radius=0.29, color=DEMAND, stroke_width=3)
                        buyer_ring.move_to([0, 0, 0.045])
                        buyer_focus = fixed(SurroundingRectangle(panel_bars['B', b],
                            color=DEMAND, buff=0.035, stroke_width=3))
                        self.play(body.animate.move_to([0, 0, body.get_center()[2]]),
                            FadeIn(buyer_focus),
                            FadeIn(buyer_ring, shift=-np.append(crowd_bodies['B', b].get_center()[:2], 0)),
                            hub.animate.set_stroke(opacity=1), run_time=0.65)
                        if side == 'B' and round_.number == 1 and b == i:
                            self.pause(f'3.a.growth.B{i}.lookout')
                        value = CROWD_MB[b]
                        mb_guide = fixed(DashedLine(side_axes['S'].c2p(0, value),
                            side_axes['S'].c2p(10, value), color=DEMAND, stroke_width=2.5))
                        mb_read = fixed(Tex(rf'MB $\${value}$', color=DEMAND).scale(0.7)
                            .move_to(side_axes['S'].c2p(5, value)
                                     + (DOWN if value >= 7 else UP) * 0.35))
                        price_caption = fixed(Tex('Price to buy', color=GUIDE).scale(0.7)
                            .move_to([5.9, -3.05, 0]))
                        self.remove(posted_caption)
                        self.play(FadeIn(mb_guide), FadeIn(mb_read), FadeIn(price_caption), run_time=0.4)
                        option_columns, option_prices, option_rings = {}, {}, {}
                        for rank, seller in enumerate(panel_ids['S']):
                            needed = crowd_asks[seller] + (BID_STEP
                                if seller in crowd_matches and crowd_matches[b] != seller else 0)
                            x0 = 10 * rank / len(local_sellers)
                            x1 = 10 * (rank + 1) / len(local_sellers)
                            option_prices[seller] = fixed(Line(side_axes['S'].c2p(x0 + 0.1, needed),
                                side_axes['S'].c2p(x1 - 0.1, needed), color=GUIDE, stroke_width=4))
                            option_columns[seller] = fixed(SurroundingRectangle(panel_bars['S', seller],
                                color=SUPPLY, buff=0.02, stroke_width=2).set_stroke(opacity=0.45))
                            option_rings[seller] = Circle(radius=0.27, color=SUPPLY, stroke_width=2)
                            option_rings[seller].move_to([*seller_spots[seller][:2], 0.045]).set_stroke(opacity=0.45)
                        self.play(*[FadeIn(m) for m in option_columns.values()],
                            *[FadeIn(m) for m in option_rings.values()],
                            *[FadeIn(m) for m in option_prices.values()],
                            *[m.animate.set_opacity(0.3) for m in posted_marks.values()], run_time=0.5)
                        self.add(mb_guide, *option_prices.values(), mb_read)
                        self.pause(f'3.a.growth.{side}{i}.r{round_.number}.b{b}.options')
                        if event.kind == 'check':
                            assert all(crowd_asks[seller] + (BID_STEP if seller in crowd_matches else 0)
                                       > value for seller in local_sellers)
                            decision_caption = fixed(Tex("Every offer exceeds this buyer's MB.",
                                color=DEFINITION).scale(DEFINITION_SCALE)
                                .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
                            self.play(FadeIn(decision_caption), run_time=0.4)
                            self.play(body.animate.move_to([*buyer_spots[b][:2], body.get_center()[2]]),
                                buyer_ring.animate.move_to([*buyer_spots[b][:2], 0.045]), run_time=0.65)
                            self.pause(f'3.a.growth.{side}{i}.declined')
                            self.play(FadeOut(decision_caption), run_time=0.2)
                        else:
                            self.remove(price_caption)
                            chosen_price = fixed(Tex(rf'Buy for $\${event.price:.2f}$', color=GUIDE)
                                .scale(0.7).move_to([5.9, -3.05, 0]))
                            self.play(FadeIn(chosen_price), option_columns[s].animate.set_stroke(opacity=1),
                                option_rings[s].animate.set_stroke(opacity=1),
                                *[m.animate.set_opacity(0.25) for seller, m in option_prices.items() if seller != s],
                                run_time=0.35)
                            displaced = (None if event.displaced is None else local_buyers[event.displaced])
                            if displaced is not None:
                                self.play(FadeOut(connection_by_buyer.pop(displaced)),
                                    FadeOut(ground_by_buyer.pop(displaced)),
                                    crowd_bars['B', displaced].pairing.animate.set_value(0),
                                    crowd_bars['S', s].pairing.animate.set_value(0), run_time=0.25)
                            seller_at = seller_spots[s]
                            destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                            route = DashedLine([0, 0, 0.045], [*destination[:2], 0.045],
                                color=MUTED, stroke_width=1.5).set_opacity(0.6)
                            moves = [body.animate.move_to([*destination[:2], body.get_center()[2]]),
                                     buyer_ring.animate.move_to([*destination[:2], 0.045])]
                            if displaced is not None:
                                displaced_body = crowd_bodies['B', displaced]
                                moves.append(displaced_body.animate.move_to(
                                    [*buyer_spots[displaced][:2], displaced_body.get_center()[2]]))
                                crowd_matches[displaced] = None
                            crowd_matches[b], crowd_asks[s] = s, event.price
                            self.play(FadeIn(route), run_time=0.2)
                            self.play(*moves, price_trackers[s].animate.set_value(event.price), run_time=0.65)
                            for key, partner in [(('B', b), ('S', s)), (('S', s), ('B', b))]:
                                crowd_bars[key].partner = crowd_bodies[partner]
                            self.play(crowd_bars['B', b].pairing.animate.set_value(1),
                                      crowd_bars['S', s].pairing.animate.set_value(1), run_time=0.35)
                            midpoint = (destination[:2] + seller_at[:2]) / 2
                            pair_left = midpoint - np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                            pair_right = midpoint + np.array([PAIR_WIDTH + PAIR_GAP / 2, 0])
                            height = CROWD_BASE + event.price * CROWD_SCALE
                            connection_by_buyer[b] = Line([*pair_left, height], [*pair_right, height],
                                color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                            ground_by_buyer[b] = Line([*pair_left, 0.04], [*pair_right, 0.04],
                                color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
                            self.play(FadeOut(route), FadeIn(connection_by_buyer[b]),
                                FadeIn(ground_by_buyer[b]), run_time=0.3)
                            self.pause(f'3.a.growth.{side}{i}.r{round_.number}.b{b}.accepted')
                            self.play(FadeOut(chosen_price), run_time=0.2)
                        self.play(FadeOut(buyer_focus), FadeOut(buyer_ring), FadeOut(mb_guide), FadeOut(mb_read),
                            FadeOut(price_caption), *[FadeOut(m) for m in option_columns.values()],
                            *[FadeOut(m) for m in option_rings.values()],
                            *[FadeOut(m) for m in option_prices.values()],
                            *[m.animate.set_opacity(1) for m in posted_marks.values()],
                            hub.animate.set_stroke(opacity=0.6), run_time=0.3)
                        self.add(posted_caption)
                    assert tuple(crowd_asks[s] for s in local_sellers) == round_.after.asks
                    assert tuple(None if crowd_matches[b] is None else
                        local_sellers.index(crowd_matches[b]) for b in local_buyers) == round_.after.sellers
                self.pause(f'3.a.growth.{side}{i}.settled')
            if side == 'S' and i == 2:
                self.pause('3.a.i')
        self.pause('3.a.ii')

        # ---- 3.b · Arrival responses already produced the final market.
        market = simulate(CROWD_MB, CROWD_MC, crowd_asks, initial_sellers=crowd_matches,
                          max_rounds=0, step=BID_STEP)
        assert market.settled
        assert sum(s is not None for s in market.final.sellers) == 6
        assert all(market.final.asks[s] == 4 for s in market.final.sellers if s is not None)
        connections = VGroup(*connection_by_buyer.values())
        ground_connections = VGroup(*ground_by_buyer.values())
        self.pause('3.b')


        # ---- 4.a · Name what has just happened; keep nontraders in the picture.
        equilibrium_def = fixed(Tex(
            r'\mbox{ {{Equilibrium}} is where no one wants to change.}',
            tex_to_color_map={'Equilibrium': DEFINITION}).scale(DEFINITION_SCALE))
        equilibrium_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        first_seller = max(s for s in market.final.sellers if s is not None)
        arrow_end = posted_marks[first_seller].get_center() + DOWN * 0.1
        equilibrium_arrow = fixed(Arrow(equilibrium_def.get_top() + RIGHT * 2.6 + UP * 0.1,
                                         arrow_end, color=DEFINITION, thickness=1.2, tip_width_ratio=4, buff=0.1))
        self.play(FadeIn(equilibrium_def), FadeIn(equilibrium_arrow))
        self.pause('4.a')

        # ---- 4.b · Bring the existing sorted curves onto a shared unit graph.
        self.play(FadeOut(equilibrium_def), FadeOut(equilibrium_arrow), FadeOut(head), run_time=0.2)
        head = fixed(title('What does the graph show?'))
        # Clear the world while its two graph panels remain intact.
        self.play(FadeIn(head), FadeOut(floor), FadeOut(rim), FadeOut(hub),
                  *[FadeOut(m) for m in crowd_bodies.values()],
                  *[FadeOut(m) for m in crowd_bars.values()],
                  *[FadeOut(m) for m in connection_by_buyer.values()],
                  *[FadeOut(m) for m in ground_by_buyer.values()], run_time=0.8)
        self.set_camera_orientation(phi=0, theta=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        unit_ax = style_axes([0, 10, 1], [0, 8, 2], x_length=4.8, y_length=4.6)
        unit_ax.shift(np.array([0, 0.1, 0]) -
                      (unit_ax.c2p(0, 0) + unit_ax.c2p(10, 8)) / 2)
        unit_ticks = VGroup(
            *[Tex(str(q), color=MUTED).scale(0.7).next_to(
                unit_ax.c2p(q, 0), DOWN, buff=0.15) for q in (2, 4, 6, 8, 10)],
            *[Tex(str(p), color=MUTED).scale(0.7).next_to(
                unit_ax.c2p(0, p), LEFT, buff=0.15) for p in (0, 2, 4, 6, 8)])
        unit_caps = VGroup(
            Tex(r'\textsf{Dollars per unit}', color=CAPTION).scale(0.7)
                .next_to(unit_ax.c2p(0, 8), UP, buff=0.25, aligned_edge=LEFT),
            Tex(r'\textsf{Units}', color=CAPTION).scale(0.7)
                .next_to(unit_ax.c2p(10, 0), RIGHT, buff=0.2))
        unit_graph = fixed(VGroup(unit_ax, unit_ticks, unit_caps))
        twins, stairs, rearrange = panel_bars, {}, []
        for side, values, color in [('B', CROWD_MB, DEMAND), ('S', CROWD_MC, SUPPLY)]:
            for rank, i in enumerate(panel_ids[side]):
                value = values[i]
                target = fixed(Polygon(unit_ax.c2p(rank, 0), unit_ax.c2p(rank + 1, 0),
                    unit_ax.c2p(rank + 1, value), unit_ax.c2p(rank, value),
                    color=color, fill_color=color, fill_opacity=0.2, stroke_width=1))
                rearrange.append(Transform(twins[side, i], target))
            steps = fixed(VGroup(*[Line(unit_ax.c2p(rank, values[i]),
                unit_ax.c2p(rank + 1, values[i]), color=color, stroke_width=3)
                for rank, i in enumerate(panel_ids[side])]))
            stairs[side] = steps
        # Both sorted curves arrive together; no detached bars over the plaza.
        self.play(FadeIn(unit_graph), FadeOut(side_frames['B']), FadeOut(side_frames['S']),
                  *[FadeOut(m) for m in posted_marks.values()], FadeOut(posted_caption),
                  *rearrange, run_time=1.8)
        self.play(*[FadeIn(m) for m in stairs.values()], run_time=0.5)
        unit_price = fixed(DashedLine(unit_ax.c2p(0, 4), unit_ax.c2p(10, 4),
                                      color=GUIDE, stroke_width=2))
        unit_drop = fixed(DashedLine(unit_ax.c2p(6, 4), unit_ax.c2p(6, 0),
                                     color=GUIDE, stroke_width=2))
        unit_read = fixed(Tex(r'$Q_d=Q_s=6$', color=GUIDE).scale(0.7)
                          .next_to(unit_ax.c2p(6, 0), DOWN, buff=0.65))
        unit_price_read = fixed(Tex(r'$P=\$4$', color=GUIDE).scale(0.7)
                                .next_to(unit_ax.c2p(0, 4), LEFT, buff=0.25))
        # The five quantity ticks precede the price ticks 0, 2, 4, 6, 8.
        unit_price_tick = unit_ticks[7]
        self.play(FadeIn(unit_price), FadeIn(unit_drop), FadeIn(unit_read),
                  unit_price_tick.animate.set_opacity(0), FadeIn(unit_price_read))
        self.pause('4.b')

        # ---- 4.c · A new aggregate example, explicitly in thousands of pounds.
        self.play(*[FadeOut(m) for m in list(self.mobjects)])
        unit_price_tick.set_opacity(1)
        # Reserve the original right-hand layout for the later plaza returns.
        # Move the entire unit graph while hidden, including the bars that the
        # posted-price markers follow. New guides use this relocated axis.
        VGroup(unit_graph, *twins.values(), *stairs.values()).shift(RIGHT * 4)
        self.set_camera_orientation(phi=0, theta=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        head = fixed(title('Where do supply and demand meet?'))
        ax = style_axes([0, 90, 10], [0, 13, 2], x_length=6.4, y_length=4.8)
        ax.shift(np.array([-2.7, 0.05, 0]) - (ax.c2p(0, 0) + ax.c2p(90, 13)) / 2)
        ticks = VGroup(
            *[Tex(str(q), color=MUTED).scale(0.7).next_to(ax.c2p(q, 0), DOWN, buff=0.14)
              for q in (0, 20, 60, 80)],
            *[Tex(str(p), color=MUTED).scale(0.7).next_to(ax.c2p(0, p), LEFT, buff=0.14)
              for p in (2, 6, 8, 10, 12)])
        p_units = Tex(r'\textsf{Dollars per pound}', color=CAPTION).scale(0.7)
        p_units.next_to(ax.c2p(0, 13), UP, buff=0.2, aligned_edge=LEFT)
        q_units = Tex(r'\textsf{Q in thousands of pounds}', color=CAPTION).scale(0.7)
        q_units.next_to(ax.c2p(45, 0), DOWN, buff=0.85)
        demand = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        supply = Line(ax.c2p(0, 2), ax.c2p(90, 6.5), color=SUPPLY, stroke_width=4)
        eq_d = Tex(r'$P=12-\frac{Q}{5}$', color=DEMAND).scale(0.8).move_to(ax.c2p(43, 10))
        eq_s = Tex(r'$P=2+\frac{Q}{20}$', color=SUPPLY).scale(0.8).move_to(ax.c2p(73, 8))
        aggregate_graph = fixed(VGroup(ax, ticks, p_units, q_units, demand, supply, eq_d, eq_s))
        divider = fixed(Line([1.2, -3, 0], [1.2, 3, 0],
                             color=MUTED, stroke_width=1).set_opacity(0.5))
        self.play(FadeIn(head), FadeIn(aggregate_graph), FadeIn(divider))
        unknown_q = fixed(Tex(r'$Q^*=?$', color=GUIDE).scale(0.7)
                          .next_to(ax.c2p(40, 0), DOWN, buff=0.42))
        unknown_p = fixed(Tex(r'$P^*=?$', color=GUIDE).scale(0.7)
                          .next_to(ax.c2p(0, 4), LEFT, buff=0.25))
        h_eq = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2))
        v_eq = fixed(DashedLine(ax.c2p(40, 4), ax.c2p(40, 0), color=GUIDE, stroke_width=2))
        eq_dot = fixed(Dot(ax.c2p(40, 4), color=GUIDE, radius=0.07))
        self.play(FadeIn(eq_dot), FadeIn(h_eq), FadeIn(unknown_p))
        self.play(FadeIn(v_eq), FadeIn(unknown_q))
        self.pause('4.c')

        # ---- 4.d · The same algebra as the source, with visible intermediate steps.
        work = fixed(VGroup(
            Tex(r'$2+\frac{Q}{20}=12-\frac{Q}{5}$'),
            Tex(r'$\frac{Q}{20}+\frac{Q}{5}=10$'),
            Tex(r'$\frac{Q}{4}=10$'),
            Tex(r'$Q^*=40$', color=GUIDE),
            Tex(r'$P^*=2+\frac{40}{20}$'),
            Tex(r'$P^*=\$4$', color=GUIDE)).scale(0.8)
            .arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([4.5, 0.4, 0]))
        self.play(FadeIn(work[0]))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]))
        self.play(FadeIn(work[3]))
        self.pause('4.d')
        self.play(FadeIn(work[4]))
        self.play(FadeIn(work[5]))
        self.pause('4.d.i')

        # ---- 4.e · Carry the calculated pair to the graph, keeping the stars.
        p_star = fixed(Tex(r'$P^*=\$4$', color=GUIDE).scale(0.7).move_to(unknown_p))
        q_star = fixed(Tex(r'$Q^*=40$', color=GUIDE).scale(0.7).move_to(unknown_q))
        self.remove(unknown_p, unknown_q)
        self.play(TransformFromCopy(work[3], q_star), TransformFromCopy(work[5], p_star))
        self.pause('4.e')

        # ---- 5.a–5.g · Same two tests: arithmetic, then people responding.
        for test_price in (3, 6):
            self.play(*[FadeOut(m) for m in list(self.mobjects)])
            self.set_camera_orientation(phi=0, theta=0)
            self.camera.frame.move_to(ORIGIN).set_height(8)
            head = fixed(title(rf'What happens at $\${test_price}$?'))
            ticks.set_opacity(0)
            self.play(FadeIn(head), FadeIn(aggregate_graph), FadeIn(divider))
            p_input = fixed(Tex(rf'$\${test_price}$', color=GUIDE).scale(0.7)
                            .next_to(ax.c2p(0, test_price), LEFT, buff=0.25))
            self.play(FadeIn(p_input))
            traces, calculations, answers = [], [], []
            for side, quantity, equation, rearranged, y in [
                ('s', 20 * (test_price - 2), r'=2+Q_s/20',
                 rf'$Q_s=20({test_price}-2)$', 1.5),
                ('d', 5 * (12 - test_price), r'=12-Q_d/5',
                 rf'$Q_d=5(12-{test_price})$', -1.3),
            ]:
                h = fixed(DashedLine(ax.c2p(0, test_price), ax.c2p(quantity, test_price),
                                     color=GUIDE, stroke_width=2))
                v = fixed(DashedLine(ax.c2p(quantity, test_price), ax.c2p(quantity, 0),
                                     color=GUIDE, stroke_width=2))
                point = fixed(Dot(ax.c2p(quantity, test_price), color=GUIDE, radius=0.065))
                unknown = fixed(Tex(rf'$Q_{side}=?$', color=GUIDE).scale(0.7)
                                .next_to(ax.c2p(quantity, 0), DOWN, buff=0.4))
                substitution = VGroup(Tex(rf'${test_price}$', color=GUIDE),
                                     Tex(f'${equation}$')).arrange(RIGHT, buff=0.08)
                calculation = fixed(VGroup(substitution, Tex(rearranged),
                    Tex(rf'$Q_{side}={quantity}$', color=GUIDE)).scale(0.8)
                    .arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([4.5, y, 0]))
                answer = fixed(Tex(rf'$Q_{side}={quantity}$', color=GUIDE).scale(0.7)
                               .move_to(unknown))
                traces.extend([h, v, point])
                calculations.append(calculation)
                answers.append(answer)
                self.play(FadeIn(h))
                self.play(FadeIn(v), FadeIn(point), FadeIn(unknown))
                self.play(TransformFromCopy(p_input, substitution[0]), FadeIn(substitution[1]))
                self.play(FadeIn(calculation[1]))
                self.play(FadeIn(calculation[2]))
                self.remove(unknown)
                self.play(TransformFromCopy(calculation[2], answer))
            if test_price == 3:
                self.pause('5.a')
            else:
                self.pause('5.d')

            # Return to the one-unit world; its counts have their own graph.
            for bar in crowd_bars.values():
                bar.pairing.set_value(0)
            self.play(*[FadeOut(m) for m in list(self.mobjects)])
            self.set_camera_orientation(phi=48 * DEGREES, theta=0)
            self.camera.frame.move_to([4, 0, 0.65]).set_height(11)
            self.add(head)
            initial_matches = ([0, 2, 5, 7, None, None, None, None, None, None]
                               if test_price == 3 else
                               [4, 1, None, None, 5, None, None, None, None, None])
            willing_buyers = [b for b, value in enumerate(CROWD_MB) if value >= test_price]
            willing_sellers = [s for s, cost in enumerate(CROWD_MC) if cost <= test_price]
            queued = [b for b in willing_buyers if initial_matches[b] is None]
            connections, ground_connections, leftovers = VGroup(), VGroup(), Group()
            for b, s in enumerate(initial_matches):
                if s is not None:
                    spot = seller_spots[s] * (1 - 0.75 / np.linalg.norm(seller_spots[s]))
                elif b in queued:
                    spot = np.array([-0.8 - 0.45 * queued.index(b), 0, 0])
                else:
                    spot = buyer_spots[b]
                body = crowd_bodies['B', b]
                body.move_to([*spot[:2], body.get_center()[2]])
                body.set_opacity(1 if b in willing_buyers else 0.3)
                crowd_bars['B', b].set_opacity(0.65 if b in willing_buyers else 0.15)
                if s is not None:
                    seller_at = seller_spots[s]
                    height = CROWD_BASE + test_price * CROWD_SCALE
                    connections.add(Line([*spot[:2], height], [*seller_at[:2], height],
                                         color=GUIDE, stroke_width=MARKET_PRICE_WIDTH))
                    ground_connections.add(Line([*spot[:2], 0.04], [*seller_at[:2], 0.04],
                                                color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3))
            for s in range(10):
                active = s in willing_sellers
                crowd_bodies['S', s].set_opacity(1 if active else 0.3)
                crowd_bars['S', s].set_opacity(0.65 if active else 0.15)
                price_trackers[s].set_value(test_price)
                if active and s not in initial_matches:
                    unit_box = Cube(side_length=0.22, color=SUPPLY).move_to(
                        seller_spots[s] + LEFT * 0.40 + DOWN * 0.22 + OUT * 0.12)
                    leftovers.add(unit_box)
            unit_price = fixed(DashedLine(unit_ax.c2p(0, test_price), unit_ax.c2p(10, test_price),
                                          color=GUIDE, stroke_width=2))
            unit_quantities = fixed(Tex(rf'$Q_d={len(willing_buyers)},\quad Q_s={len(willing_sellers)}$',
                color=GUIDE).scale(0.7).next_to(unit_ax.c2p(5, 0), DOWN, buff=0.65))
            self.play(FadeIn(floor), FadeIn(rim),
                      *[FadeIn(m) for m in crowd_bodies.values()],
                      *[FadeIn(m) for m in crowd_bars.values()],
                      FadeIn(connections), FadeIn(ground_connections), FadeIn(leftovers),
                      FadeIn(unit_graph), *[FadeIn(m) for m in twins.values()],
                      *[FadeIn(m) for m in stairs.values()],
                      FadeIn(unit_price), FadeIn(unit_quantities))
            if test_price == 3:
                definition = fixed(Tex(
                    r'\mbox{ {{Shortage}}: quantity demanded is greater than quantity supplied.}',
                    tex_to_color_map={'Shortage': DEFINITION}).scale(DEFINITION_SCALE))
                definition.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
                target = screen_point(self.camera.frame, crowd_bodies['B', 4].get_center())
            else:
                definition = fixed(Tex(
                    r'\mbox{ {{Excess}}: quantity supplied is greater than quantity demanded.}',
                    tex_to_color_map={'Excess': DEFINITION}).scale(DEFINITION_SCALE))
                definition.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
                target = screen_point(self.camera.frame, leftovers[-1].get_center())
            definition_arrow = fixed(Arrow(definition.get_top() + LEFT * 2 + UP * 0.1,
                target, color=DEFINITION, thickness=1.2, tip_width_ratio=4, buff=0.18))
            self.play(FadeIn(definition), FadeIn(definition_arrow))
            if test_price == 3:
                self.pause('5.b')
                self.play(FadeOut(definition), FadeOut(definition_arrow), run_time=0.2)
            else:
                self.pause('5.d.i')
                self.play(FadeOut(definition), FadeOut(definition_arrow), run_time=0.2)
                textbook_word = fixed(Tex('Surplus', color=INK).scale(0.8).move_to([-4, -2.6, 0]))
                strike = fixed(Line(textbook_word.get_left(), textbook_word.get_right(),
                                    color=MUTED, stroke_width=2))
                excess_word = fixed(Tex('Excess', color=DEFINITION).scale(0.8)
                                    .next_to(textbook_word, DOWN, buff=0.3))
                self.play(FadeIn(textbook_word))
                self.play(FadeIn(strike), FadeIn(excess_word))
                self.pause('5.e')
                self.play(FadeOut(textbook_word), FadeOut(strike), FadeOut(excess_word), run_time=0.2)

            # One named move, then let the crowd run without deliberation holds.
            self.remove(definition, definition_arrow)
            self.play(FadeOut(unit_price), FadeOut(unit_quantities), FadeOut(leftovers))
            if test_price == 3:
                offer, mover, displaced = 3.25, 4, 0
                next_matches = [None, 2, 5, 7, 0, None, None, None, None, None]
                next_asks = [3.25, 4, 3, 5, 4, 3, 6, 3, 5, 6]
                seed = 473
                action_words = r'Amanda-Grace $\longrightarrow$ Molly: $\$3.25$'
            else:
                offer, mover, displaced = 5, 0, None
                next_matches = [0, 1, None, None, 5, None, None, None, None, None]
                next_asks = [5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
                seed = 361
                action_words = r'Molly $\longrightarrow$ Gary: $\$5$'
            action_caption = fixed(Tex(action_words, color=INK).scale(DEFINITION_SCALE))
            action_caption.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
            # Preserve the supply-column price record when the common price breaks.
            for s, mark in posted_marks.items():
                if s != 0:
                    price_trackers[s].set_value(next_asks[s])
                mark.axis = unit_ax
                mark.update()
            spot = seller_spots[0] * (1 - 0.75 / np.linalg.norm(seller_spots[0]))
            moves = [crowd_bodies['B', mover].animate.move_to(
                [*spot[:2], crowd_bodies['B', mover].get_center()[2]])]
            if displaced is not None:
                moves.append(crowd_bodies['B', displaced].animate.move_to(
                    [-0.8, 0, crowd_bodies['B', displaced].get_center()[2]]))
            replacement_lines, replacement_ground = VGroup(), VGroup()
            for b, s in enumerate(next_matches):
                if s is not None:
                    seller_at = seller_spots[s]
                    buyer_at = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                    height = CROWD_BASE + next_asks[s] * CROWD_SCALE
                    replacement_lines.add(Line([*buyer_at[:2], height], [*seller_at[:2], height],
                                               color=GUIDE, stroke_width=MARKET_PRICE_WIDTH))
                    replacement_ground.add(Line([*buyer_at[:2], 0.04], [*seller_at[:2], 0.04],
                                                color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3))
            self.play(FadeIn(action_caption), FadeOut(connections), FadeOut(ground_connections),
                      *[FadeIn(m) for m in posted_marks.values()],
                      *moves, price_trackers[0].animate.set_value(offer), run_time=1.5)
            connections, ground_connections = replacement_lines, replacement_ground
            self.play(FadeIn(connections), FadeIn(ground_connections))
            if test_price == 3:
                self.pause('5.b.i')
            else:
                self.pause('5.f')
            self.play(FadeOut(action_caption), run_time=0.2)
            adjustment = simulate(CROWD_MB, CROWD_MC, next_asks, seed=seed,
                                  initial_sellers=next_matches, step=BID_STEP)
            assert adjustment.settled
            assert sum(s is not None for s in adjustment.final.sellers) == 6
            assert all(adjustment.final.asks[s] == 4
                       for s in adjustment.final.sellers if s is not None)
            for s in range(10):
                price_trackers[s].set_value(next_asks[s])
            for m in crowd_bodies.values():
                m.set_opacity(1)
            for m in crowd_bars.values():
                m.set_opacity(0.65)
            for round_ in adjustment.rounds:
                moves, prices = [], []
                new_connections, new_ground, price_arrows = VGroup(), VGroup(), VGroup()
                for b, s in enumerate(round_.after.sellers):
                    if s is None:
                        destination = buyer_spots[b]
                    else:
                        seller_at = seller_spots[s]
                        destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                        height = CROWD_BASE + round_.after.asks[s] * CROWD_SCALE
                        new_connections.add(Line([*destination[:2], height], [*seller_at[:2], height],
                                                 color=GUIDE, stroke_width=MARKET_PRICE_WIDTH))
                        new_ground.add(Line([*destination[:2], 0.04], [*seller_at[:2], 0.04],
                                            color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3))
                    body = crowd_bodies['B', b]
                    moves.append(body.animate.move_to([*destination[:2], body.get_center()[2]]))
                for s, price in enumerate(round_.after.asks):
                    if price != round_.before.asks[s]:
                        prices.append(price_trackers[s].animate.set_value(price))
                        direction = UP if price > round_.before.asks[s] else DOWN
                        origin = posted_marks[s].get_center() + UP * 0.22
                        price_arrows.add(fixed(Arrow(origin - direction * 0.2,
                            origin + direction * 0.2, color=GUIDE, buff=0,
                            thickness=1.2, tip_width_ratio=4)))
                self.play(FadeOut(connections), FadeOut(ground_connections),
                          *moves, *prices, FadeIn(price_arrows), run_time=0.45)
                connections, ground_connections = new_connections, new_ground
                self.play(FadeIn(connections), FadeIn(ground_connections),
                          FadeOut(price_arrows), run_time=0.2)
            unit_price = fixed(DashedLine(unit_ax.c2p(0, 4), unit_ax.c2p(10, 4),
                                          color=GUIDE, stroke_width=2))
            unit_quantities = fixed(Tex(r'$Q_d=Q_s=6$', color=GUIDE).scale(0.7)
                                   .next_to(unit_ax.c2p(5, 0), DOWN, buff=0.65))
            self.play(FadeIn(unit_price), FadeIn(unit_quantities))
            if test_price == 3:
                self.pause('5.c')
            else:
                self.pause('5.g')

        # ---- 5.h · Restore the discovered allocation before testing one person.
        self.play(FadeOut(head), run_time=0.2)
        head = fixed(title('Would anyone gain by changing?'))
        restore_moves = []
        restored_connections, restored_ground = {}, {}
        for b, s in enumerate(market.final.sellers):
            if s is None:
                spot = buyer_spots[b]
            else:
                seller_at = seller_spots[s]
                spot = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                height = CROWD_BASE + 4 * CROWD_SCALE
                restored_connections[b] = Line([*spot[:2], height], [*seller_at[:2], height],
                                                color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
                restored_ground[b] = Line([*spot[:2], 0.04], [*seller_at[:2], 0.04],
                                          color=GUIDE, stroke_width=MARKET_SHADOW_WIDTH).set_opacity(0.3)
            body = crowd_bodies['B', b]
            restore_moves.append(body.animate.move_to([*spot[:2], body.get_center()[2]]))
        for s, price in enumerate(market.final.asks):
            price_trackers[s].set_value(price)
        self.play(FadeOut(connections), FadeOut(ground_connections), *restore_moves, FadeIn(head))
        self.play(*[FadeIn(m) for m in restored_connections.values()],
                  *[FadeIn(m) for m in restored_ground.values()])
        self.pause('5.h')

        # ---- 5.h.i · This actual MB-$4 customer rejects a $4.25 price.
        marginal_buyer = next(b for b, s in enumerate(market.final.sellers)
                              if s is not None and CROWD_MB[b] == 4)
        marginal_seller = market.final.sellers[marginal_buyer]
        self.play(FadeOut(unit_price), FadeOut(unit_quantities))
        refusal = fixed(Tex(r'MB $\$4$\quad Price $\$4.25$', color=INK).scale(DEFINITION_SCALE))
        refusal.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(price_trackers[marginal_seller].animate.set_value(4.25), FadeIn(refusal))
        self.play(FadeOut(restored_connections[marginal_buyer]),
                  FadeOut(restored_ground[marginal_buyer]),
                  crowd_bodies['B', marginal_buyer].animate.move_to(
                      [*buyer_spots[marginal_buyer][:2], crowd_bodies['B', marginal_buyer].get_center()[2]]))
        self.pause('5.h.i')
        self.play(FadeOut(refusal), run_time=0.2)
        spot = seller_spots[marginal_seller] * (1 - 0.75 / np.linalg.norm(seller_spots[marginal_seller]))
        self.play(price_trackers[marginal_seller].animate.set_value(4),
                  crowd_bodies['B', marginal_buyer].animate.move_to(
                      [*spot[:2], crowd_bodies['B', marginal_buyer].get_center()[2]]))
        self.play(FadeIn(restored_connections[marginal_buyer]),
                  FadeIn(restored_ground[marginal_buyer]))

        # ---- 5.h.ii · A different actual pair: a $3.75 bid is below this MC.
        cost_seller = next(s for s in market.final.sellers if s is not None and CROWD_MC[s] == 4)
        cost_buyer = market.final.sellers.index(cost_seller)
        low_height = CROWD_BASE + 3.75 * CROWD_SCALE
        low_offer = DashedLine([*crowd_bodies['B', cost_buyer].get_center()[:2], low_height],
                               [*seller_spots[cost_seller][:2], low_height],
                               color=GUIDE, stroke_width=MARKET_PRICE_WIDTH)
        refusal = fixed(Tex(r'Offer $\$3.75$\quad MC $\$4$', color=INK).scale(DEFINITION_SCALE))
        refusal.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(low_offer), FadeIn(refusal))
        self.pause('5.h.ii')
        self.play(FadeOut(refusal), run_time=0.2)
        self.play(FadeOut(low_offer))
        stable = fixed(Tex(r'\mbox{ {{Equilibrium}} is where no one wants to change.}',
                           tex_to_color_map={'Equilibrium': DEFINITION}).scale(DEFINITION_SCALE))
        stable.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(stable), FadeIn(unit_price), FadeIn(unit_quantities))
        self.pause('5.h.iii')
