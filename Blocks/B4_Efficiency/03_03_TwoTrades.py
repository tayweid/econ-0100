# maniml 03_03_TwoTrades.py B4TwoTrades
# B4 | B3's approved 3.a plaza and recorded seed-54 trade sequence.

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


class B4TwoTrades(ThreeDScene):
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

                self.skip_animations = opening_skip
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
                              hub.animate.set_stroke(opacity=1), run_time=0.65)
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
                            name = Tex(who, color=INK).scale(0.65)
                            name.face_mat = np.eye(3)
                            name.add_updater(face_camera)
                            name.update()
                            name.move_to(np.array([body_x, -0.55, 0.13]) + offset)
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
                        stay_box = fixed(RoundedRectangle(width=5.5, height=1.0, corner_radius=0.12,
                            color=MUTED, fill_color=BG, fill_opacity=1, stroke_width=1.5).move_to([-3.05, -2.85, 0]))
                        switch_box = fixed(stay_box.copy().move_to([3.05, -2.85, 0]))
                        stay_words = fixed(VGroup(Tex(r'Molly: $\$6.25$', color=INK), Tex(r'Gain $\$0.75$', color=DEMAND))
                            .arrange(DOWN, buff=0.10).scale(0.68).move_to(stay_box))
                        switch_words = fixed(VGroup(Tex(r'Andrew: $\$4.25$', color=INK), Tex(r'Gain $\$2.75$', color=DEMAND))
                            .arrange(DOWN, buff=0.10).scale(0.68).move_to(switch_box))
                        close_objects = [close_floor, close_rim, close_head, *close_people.values(), *close_bars.values(),
                            *close_names.values(), *close_values.values(), stay_price_line, stay_shadow,
                            switch_price_line, mb_read_across, stay_box, switch_box, stay_words, switch_words]
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
            # The exact seed-54 path begins after Gary's $4.50 outbid.
            two_by_two = True
            local_buyers = [0, 4]
            small_run = simulate([6, 7], [2, 4], [6.25, 4.5],
                initial_sellers=[1, None], seed=54, step=BID_STEP)
            assert small_run.final.asks == (5.5, 5.5)
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

                            self.play(FadeOut(cut_question), run_time=0.2)
                        seller_focus = fixed(SurroundingRectangle(panel_bars['S', s],
                            color=SUPPLY, buff=0.035, stroke_width=3))
                        origin = posted_marks[s].get_center() + UP * 0.22
                        cut_arrow = fixed(Arrow(origin + UP * 0.2, origin + DOWN * 0.2,
                            color=GUIDE, buff=0, thickness=1.2, tip_width_ratio=4))
                        crowd_asks[s] = event.price
                        self.play(FadeIn(seller_focus), FadeIn(cut_arrow),
                            price_trackers[s].animate.set_value(event.price), run_time=0.45)
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
                        hub.animate.set_stroke(opacity=1), run_time=0.5)
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
                    self.wait(0.15)
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
                    self.play(*moves, price_trackers[s].animate.set_value(event.price), run_time=0.5)
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
        # ---- 1.b.equal_prices · Keep the two actual B3 pairs and both posted asks.
        self.remove(posted_caption)
        equal_prices = fixed(Tex(r'Both trades: $\$5.50$.', color=GUIDE).scale(0.8)
                             .move_to([0, -3.15, 0]))
        equal_counts = fixed(Tex('2 willing buyers; 2 sellers.', color=CAPTION).scale(0.7)
                             .move_to([0, -3.65, 0]))
        self.play(Transform(head, fixed(title('Would either buyer switch?'))), FadeIn(equal_prices), FadeIn(equal_counts))
        self.pause('1.b.equal_prices')
