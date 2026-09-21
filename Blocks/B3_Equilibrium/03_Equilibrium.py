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
from discovery import simulate


class EpisodeB3(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        MB, MC, OFFER = 6, 2, 4
        BID_STEP = 0.25
        CROWD_MB = [6, 5, 4, 3, 6, 5, 4, 3, 2, 2]
        CROWD_MC = [2, 4, 3, 5, 4, 2, 6, 3, 5, 6]
        SEARCH_SEED = 268
        DOLLAR_HEIGHT, BAR_BASE = 0.55, 0.75
        BAR_WIDTH, CLOSE_WIDTH, CLOSE_GAP = 0.16, 1.10, 0.12
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        WORLD_CENTER = np.array([0.0, 0.0, 1.8])
        CLOSE_CENTER = np.array([0.0, 0.0, 2.05])

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
            ('buyer', -3.0, MB, DEMAND, 'Gary', 'MB'),
            ('seller', 3.0, MC, SUPPLY, 'Molly', 'MC'),
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
            name_label = fixed(Tex(name, color=INK).scale(0.8))
            name_label.anchor = body
            name_label.add_updater(lambda m: m.move_to(
                screen_point(self.camera.frame, m.anchor.get_center()) + DOWN * 0.6))
            name_label.update()
            value_label = fixed(Tex(rf'{term} $\${value:g}$', color=color).scale(0.7))
            value_label.anchor = bar
            value_label.value = value
            value_label.add_updater(lambda m: m.move_to(screen_point(
                self.camera.frame,
                [*m.anchor.get_center()[:2], BAR_BASE + m.value * DOLLAR_HEIGHT])
                + UP * 0.30))
            value_label.update()
            bodies[key], bars[key] = body, bar
            names[key], marginal_labels[key] = name_label, value_label
            self.play(FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))
        self.pause('2.a')

        # ---- 2.a.i · Same bars, now between the people and viewed from the side.
        self.play(
            self.camera.frame.animate.reorient(0, 90, center=CLOSE_CENTER, height=7.2),
            bodies['buyer'].animate.shift(RIGHT * 0.6),
            bodies['seller'].animate.shift(LEFT * 0.6),
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
        price_word = fixed(Tex(rf'Price $\${OFFER:g}$', color=GUIDE).scale(0.7))
        price_word.move_to(screen_point(self.camera.frame, [0, 0, price_z]) + UP * 0.3)
        zero_word = fixed(Tex('0', color=CAPTION).scale(0.7))
        zero_word.move_to(screen_point(self.camera.frame, [0, 0, BAR_BASE]) + DOWN * 0.25)
        question = fixed(Tex('Would they both accept this price?', color=DEFINITION)
                         .scale(DEFINITION_SCALE))
        question.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(zero), FadeIn(zero_word), FadeIn(price_line),
                  FadeIn(price_shadow), FadeIn(price_word))
        self.play(FadeIn(question))
        self.pause('2.a.i')

        # ---- 2.b · Accept first, then recall the two views of the same exchange.
        self.remove(question)
        accepted_line = Line([left_edge, -0.045, price_z],
                             [right_edge, -0.045, price_z], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([left_edge, 0, 0.04], [right_edge, 0, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        self.play(ReplacementTransform(price_line, accepted_line),
                  ReplacementTransform(price_shadow, accepted_shadow), run_time=0.6)
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
        expenditure_label = fixed(Tex(rf'Expenditure $\${OFFER:g}$', color=GOV).scale(0.7))
        expenditure_label.move_to(screen_point(self.camera.frame,
            [left_edge, 0, BAR_BASE + OFFER * DOLLAR_HEIGHT / 2]) + LEFT * 0.3,
            aligned_edge=RIGHT)
        self.play(bars['buyer'].animate.set_opacity(0.13), FadeIn(expenditure))
        self.play(FadeIn(expenditure_label))
        self.pause('2.b.i')

        # ---- 2.b.ii · Consumer surplus stays above the same price line.
        cs_label = fixed(Tex(rf'CS $\${MB - OFFER:g}$', color=DEMAND).scale(0.7))
        cs_label.move_to(screen_point(self.camera.frame,
            [left_edge, 0, BAR_BASE + (OFFER + MB) * DOLLAR_HEIGHT / 2]) + LEFT * 0.3,
            aligned_edge=RIGHT)
        self.play(FadeIn(buyer_cs))
        self.play(FadeIn(cs_label))
        self.pause('2.b.ii')

        # ---- 2.b.iii · B2's full revenue rectangle stays visible around cost and PS.
        revenue = Polygon(
            [CLOSE_GAP / 2, -0.03, BAR_BASE], [right_edge, -0.03, BAR_BASE],
            [right_edge, -0.03, price_z], [CLOSE_GAP / 2, -0.03, price_z],
            stroke_color=INK, stroke_width=2, fill_opacity=0)
        revenue_label = fixed(Tex(rf'Revenue $\${OFFER:g}$', color=INK).scale(0.7))
        revenue_label.move_to(screen_point(self.camera.frame,
            [right_edge, 0, price_z]) + RIGHT * 0.3 + UP * 0.2, aligned_edge=LEFT)
        self.play(FadeIn(revenue), FadeIn(revenue_label))
        self.pause('2.b.iii')

        # ---- 2.b.iv · Cost first, then producer surplus; no new definitions.
        seller_cost = Polygon(
            [CLOSE_GAP / 2, -0.025, BAR_BASE], [right_edge, -0.025, BAR_BASE],
            [right_edge, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            [CLOSE_GAP / 2, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            fill_color=GOV, fill_opacity=AREA_OPACITY, stroke_width=0)
        seller_ps = Polygon(
            [CLOSE_GAP / 2, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            [right_edge, -0.025, BAR_BASE + MC * DOLLAR_HEIGHT],
            [right_edge, -0.025, price_z], [CLOSE_GAP / 2, -0.025, price_z],
            fill_color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=0)
        cost_label = fixed(Tex(rf'Cost $\${MC:g}$', color=GOV).scale(0.7))
        cost_label.move_to(screen_point(self.camera.frame,
            [right_edge, 0, BAR_BASE + MC * DOLLAR_HEIGHT / 2]) + RIGHT * 0.3,
            aligned_edge=LEFT)
        ps_label = fixed(Tex(rf'PS $\${OFFER - MC:g}$', color=SUPPLY).scale(0.7))
        ps_label.move_to(screen_point(self.camera.frame,
            [right_edge, 0, BAR_BASE + (MC + OFFER) * DOLLAR_HEIGHT / 2]) + RIGHT * 0.3,
            aligned_edge=LEFT)
        self.play(bars['seller'].animate.set_opacity(0.13), FadeIn(seller_cost),
                  FadeOut(marginal_labels['seller']))
        self.play(FadeIn(cost_label))
        self.pause('2.b.iv')
        self.play(FadeIn(seller_ps))
        self.play(FadeIn(ps_label))
        self.pause('2.b.v')

        # ---- 2.b.vi · The one unit never changes size economically.
        unit = fixed(Tex('One unit', color=CAPTION).scale(0.7))
        unit.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(unit))
        self.pause('2.b.vi')

        # ---- 2.c · Pull back to the same people; two more join their market.
        self.remove(unit)
        self.play(FadeOut(expenditure), FadeOut(buyer_cs), FadeOut(revenue),
                  FadeOut(seller_cost), FadeOut(seller_ps), FadeOut(expenditure_label),
                  FadeOut(cs_label), FadeOut(revenue_label), FadeOut(cost_label),
                  FadeOut(ps_label), FadeOut(zero), FadeOut(zero_word), FadeOut(price_word))
        deal_price = ValueTracker(OFFER)
        accepted_line.buyer, accepted_line.seller = bars['buyer'], bars['seller']
        accepted_line.price = deal_price
        accepted_line.add_updater(lambda m: m.put_start_and_end_on(
            np.array([*m.buyer.get_center()[:2], BAR_BASE + m.price.get_value() * DOLLAR_HEIGHT]),
            np.array([*m.seller.get_center()[:2], BAR_BASE + m.price.get_value() * DOLLAR_HEIGHT])))
        accepted_shadow.buyer, accepted_shadow.seller = bars['buyer'], bars['seller']
        accepted_shadow.add_updater(lambda m: m.put_start_and_end_on(
            np.array([*m.buyer.get_center()[:2], 0.04]),
            np.array([*m.seller.get_center()[:2], 0.04])))
        self.play(
            self.camera.frame.animate.reorient(0, 58, center=WORLD_CENTER, height=8.8),
            bodies['buyer'].animate.move_to([-3.5, 1.5, bodies['buyer'].get_center()[2]]),
            bodies['seller'].animate.move_to([-0.3, 1.5, bodies['seller'].get_center()[2]]),
            bars['buyer'].animate.stretch_to_fit_width(BAR_WIDTH).set_x(-3.5).set_y(1.5).set_opacity(0.65),
            bars['seller'].animate.stretch_to_fit_width(BAR_WIDTH).set_x(-0.3).set_y(1.5).set_opacity(0.65),
            floor.animate.set_opacity(0.14), rim.animate.set_stroke(opacity=0.6),
            run_time=2)
        self.play(FadeIn(marginal_labels['seller']))
        for key in ('buyer', 'seller'):
            bars[key].anchor = bodies[key]
            bars[key].value = MB if key == 'buyer' else MC
            bars[key].add_updater(lambda m: m.move_to([
                *m.anchor.get_center()[:2], BAR_BASE + m.value * DOLLAR_HEIGHT / 2]))
        deal_number = fixed(DecimalNumber(OFFER, num_decimal_places=2, color=GUIDE).scale(0.7))
        deal_number.tracker = deal_price
        deal_number.buyer, deal_number.seller = bars['buyer'], bars['seller']
        deal_number.add_updater(lambda m: m.set_value(m.tracker.get_value())
                               if abs(m.get_value() - m.tracker.get_value()) > 1e-6 else m)
        deal_number.add_updater(lambda m: m.move_to(screen_point(self.camera.frame,
            [*(0.5 * (m.buyer.get_center() + m.seller.get_center()))[:2],
             BAR_BASE + m.tracker.get_value() * DOLLAR_HEIGHT]) + UP * 0.22))
        deal_number.update()
        for key, x, y, value, color, name, term in [
            ('challenger', -2.8, -1.5, 6, DEMAND, 'Amanda-Grace', 'MB'),
            ('other_seller', 3.0, -1.5, 4, SUPPLY, 'Andrew', 'MC'),
        ]:
            shadow = Disk3D(radius=0.28, resolution=(2, 24), shading=(0, 0, 0),
                            opacity=0.28).set_color(color).move_to([x, y, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(16, 10))
            orb.move_to([x, y, 0.32])
            body = Group(shadow, orb)
            bar = Rectangle3D(width=BAR_WIDTH, height=value * DOLLAR_HEIGHT,
                              resolution=(2, 2), opacity=0.65).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT)
            bar.anchor, bar.value = body, value
            bar.add_updater(lambda m: m.move_to([
                *m.anchor.get_center()[:2], BAR_BASE + m.value * DOLLAR_HEIGHT / 2]))
            bar.update()
            name_label = fixed(Tex(name, color=INK).scale(0.7))
            name_label.anchor = body
            name_label.add_updater(lambda m: m.move_to(
                screen_point(self.camera.frame, m.anchor.get_center()) + DOWN * 0.6))
            name_label.update()
            value_label = fixed(Tex(rf'{term} $\${value:g}$', color=color).scale(0.7))
            value_label.anchor, value_label.value = bar, value
            value_label.add_updater(lambda m: m.move_to(screen_point(self.camera.frame,
                [*m.anchor.get_center()[:2], BAR_BASE + m.value * DOLLAR_HEIGHT]) + UP * 0.3))
            value_label.update()
            bodies[key], bars[key] = body, bar
            names[key], marginal_labels[key] = name_label, value_label
            self.play(FadeIn(body), FadeIn(bar), FadeIn(name_label), FadeIn(value_label))
        other_ask = fixed(Tex(r'Ask $\$5$', color=GUIDE).scale(0.7))
        marginal_labels['challenger'].add_updater(lambda m: m.shift(LEFT * 0.75 + DOWN * 0.45))
        other_ask.move_to(screen_point(self.camera.frame,
            [3.0, -1.5, BAR_BASE + 5 * DOLLAR_HEIGHT]) + UP * 0.2)
        self.remove(head)
        head = fixed(title('Would they switch?'))
        self.play(FadeIn(head), FadeIn(deal_number), FadeIn(other_ask))
        self.pause('2.c')

        # ---- 2.c.i · Keep the incumbent while Amanda-Grace considers an offer.
        challenger_at = np.array([-1.0, -1.0, bodies['challenger'].get_center()[2]])
        challenge = DashedLine([*challenger_at[:2], BAR_BASE + 4.25 * DOLLAR_HEIGHT],
                              [-0.3, 1.5, BAR_BASE + 4.25 * DOLLAR_HEIGHT],
                              color=GUIDE, stroke_width=2.5)
        offer_label = fixed(Tex(r'Offer $\$4.25$', color=GUIDE).scale(0.7))
        offer_label.move_to(screen_point(self.camera.frame,
            [0.4, -1.0, BAR_BASE + 4.25 * DOLLAR_HEIGHT]) + RIGHT * 0.5)
        self.play(bodies['challenger'].animate.move_to(challenger_at),
                  bodies['other_seller'].animate.set_opacity(0.25),
                  bars['other_seller'].animate.set_opacity(0.15),
                  marginal_labels['other_seller'].animate.set_opacity(0.3),
                  names['other_seller'].animate.set_opacity(0.3), run_time=1.4)
        self.play(FadeIn(challenge), FadeIn(offer_label), FadeIn(question))
        self.pause('2.c.i')

        # ---- 2.c.ii · The accepted offer changes partners, not anybody's MB or MC.
        self.remove(question)
        accepted_line.clear_updaters()
        accepted_shadow.clear_updaters()
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow),
                  FadeOut(challenge), FadeOut(offer_label),
                  bodies['buyer'].animate.move_to([0.7, -0.1, bodies['buyer'].get_center()[2]]),
                  bodies['challenger'].animate.move_to([-2.3, 1.5, challenger_at[2]]),
                  deal_price.animate.set_value(OFFER + BID_STEP), run_time=1.2)
        accepted_line = Line([-2.3, 1.5, BAR_BASE + 4.25 * DOLLAR_HEIGHT],
                             [-0.3, 1.5, BAR_BASE + 4.25 * DOLLAR_HEIGHT], color=GUIDE, stroke_width=3)
        accepted_shadow = Line([-2.3, 1.5, 0.04], [-0.3, 1.5, 0.04],
                               color=GUIDE, stroke_width=2).set_opacity(0.3)
        deal_number.buyer = bars['challenger']
        self.play(FadeIn(accepted_line), FadeIn(accepted_shadow),
                  bodies['other_seller'].animate.set_opacity(1),
                  bars['other_seller'].animate.set_opacity(0.65),
                  names['other_seller'].animate.set_opacity(1),
                  marginal_labels['other_seller'].animate.set_opacity(1))
        self.play(bodies['buyer'].animate.move_to([1.6, -1.5, bodies['buyer'].get_center()[2]]),
                  run_time=1.4)
        other_line = Line([1.6, -1.5, BAR_BASE + 5 * DOLLAR_HEIGHT],
                          [3.0, -1.5, BAR_BASE + 5 * DOLLAR_HEIGHT], color=GUIDE, stroke_width=3)
        other_shadow = Line([1.6, -1.5, 0.04], [3.0, -1.5, 0.04],
                            color=GUIDE, stroke_width=2).set_opacity(0.3)
        self.play(FadeIn(other_line), FadeIn(other_shadow))
        self.pause('2.c.ii')

        # ---- 3.a · The same four people enter a larger market. No graph yet.
        crowd_asks = [4.25, 6, 6, 6, 5, 6, 6, 6, 6, 6]
        crowd_matches = [4, None, None, None, 0, None, None, None, None, None]
        market = simulate(CROWD_MB, CROWD_MC, crowd_asks, seed=SEARCH_SEED,
                          initial_sellers=crowd_matches, step=BID_STEP)
        assert market.settled
        assert len([s for s in market.final.sellers if s is not None]) == 6
        assert all(market.final.asks[s] == 4 for s in market.final.sellers if s is not None)
        self.play(FadeOut(accepted_line), FadeOut(accepted_shadow),
                  FadeOut(other_line), FadeOut(other_shadow), FadeOut(deal_number),
                  FadeOut(other_ask), *[FadeOut(m) for m in marginal_labels.values()],
                  *[FadeOut(m) for m in names.values()])
        for bar in bars.values():
            bar.clear_updaters()
        self.remove(head)
        head = fixed(title('Where do prices settle?'))
        self.play(FadeIn(head), self.camera.frame.animate.reorient(
            0, 48, center=[0, 0, 0.65], height=9), run_time=1.5)
        CROWD_SCALE, CROWD_BASE = 0.24, 0.52
        seller_spots = [3.6 * np.array([np.cos(a), np.sin(a), 0])
                        for a in np.radians(np.linspace(65, -65, 10))]
        buyer_spots = [3.7 * np.array([np.cos(a), np.sin(a), 0])
                       for a in np.radians(np.linspace(115, 245, 10))]
        crowd_bodies, crowd_bars, price_tags, price_trackers = {}, {}, {}, {}
        inherited = {('B', 0): 'buyer', ('B', 4): 'challenger',
                     ('S', 0): 'seller', ('S', 4): 'other_seller'}
        inherited_moves = []
        for side, values, spots, color in [('B', CROWD_MB, buyer_spots, DEMAND),
                                           ('S', CROWD_MC, seller_spots, SUPPLY)]:
            for i, value in enumerate(values):
                spot = spots[i].copy()
                if side == 'B' and market.initial.sellers[i] is not None:
                    seller_at = seller_spots[market.initial.sellers[i]]
                    spot = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                if (side, i) in inherited:
                    key = inherited[side, i]
                    body, bar = bodies[key], bars[key]
                    inherited_moves.extend([
                              body.animate.scale(0.7).move_to([*spot[:2], 0.19]),
                              bar.animate.stretch(CROWD_SCALE / DOLLAR_HEIGHT, 2)
                              .stretch_to_fit_width(0.075).move_to(
                                  [*spot[:2], CROWD_BASE + value * CROWD_SCALE / 2])])
                else:
                    shadow = Disk3D(radius=0.20, resolution=(2, 16), shading=(0, 0, 0),
                                    opacity=0.22).set_color(color).move_to([*spot[:2], 0.025])
                    orb = Sphere(radius=0.16, color=color, resolution=(12, 8))
                    orb.move_to([*spot[:2], 0.25])
                    body = Group(shadow, orb)
                    bar = Rectangle3D(width=0.075, height=value * CROWD_SCALE,
                                      resolution=(2, 2), opacity=0.65).set_color(color)
                    bar.rotate(90 * DEGREES, RIGHT).move_to(
                        [*spot[:2], CROWD_BASE + value * CROWD_SCALE / 2])
                bar.anchor, bar.value = body, value
                bar.add_updater(lambda m: m.move_to([
                    *m.anchor.get_center()[:2], CROWD_BASE + m.value * CROWD_SCALE / 2]))
                crowd_bodies[side, i], crowd_bars[side, i] = body, bar
                if side == 'S':
                    tracker = ValueTracker(market.initial.asks[i])
                    tag = fixed(DecimalNumber(market.initial.asks[i], num_decimal_places=2,
                                              color=GUIDE).scale(0.7))
                    tag.tracker, tag.anchor = tracker, body
                    tag.add_updater(lambda m: m.set_value(m.tracker.get_value())
                                    if abs(m.get_value() - m.tracker.get_value()) > 1e-6 else m)
                    tag.add_updater(lambda m: m.move_to(screen_point(self.camera.frame,
                        m.anchor.get_center()) + RIGHT * 0.45 + DOWN * 0.2))
                    tag.update()
                    price_tags[i], price_trackers[i] = tag, tracker
        self.play(*inherited_moves,
                  *[FadeIn(m) for k, m in crowd_bodies.items() if k not in inherited],
                  *[FadeIn(m) for k, m in crowd_bars.items() if k not in inherited],
                  *[FadeIn(m) for m in price_tags.values()], run_time=1.2)
        connections = VGroup()
        ground_connections = VGroup()
        for b, s in enumerate(market.initial.sellers):
            if s is not None:
                buyer_at = crowd_bodies['B', b].get_center()
                seller_at = seller_spots[s]
                height = CROWD_BASE + market.initial.asks[s] * CROWD_SCALE
                connections.add(Line([*buyer_at[:2], height], [*seller_at[:2], height],
                                     color=GUIDE, stroke_width=2.2))
                ground_connections.add(Line([*buyer_at[:2], 0.04], [*seller_at[:2], 0.04],
                                            color=GUIDE, stroke_width=1.6).set_opacity(0.3))
        self.add(connections, ground_connections)
        self.pause('3.a')

        # ---- 3.b · A round is compressed into one continuous market action.
        for round_ in market.rounds:
            rays = VGroup()
            for event in round_.events:
                if event.kind == 'check':
                    start = crowd_bodies['B', event.buyer].get_center()
                    end = seller_spots[event.seller]
                    rays.add(DashedLine([*start[:2], 0.04], [*end[:2], 0.04],
                                        color=MUTED, stroke_width=1).set_opacity(0.28))
            moves, prices = [], []
            price_arrows = VGroup()
            new_connections, new_ground = VGroup(), VGroup()
            for b, s in enumerate(round_.after.sellers):
                if s is None:
                    destination = buyer_spots[b]
                else:
                    seller_at = seller_spots[s]
                    destination = seller_at * (1 - 0.75 / np.linalg.norm(seller_at))
                    height = CROWD_BASE + round_.after.asks[s] * CROWD_SCALE
                    new_connections.add(Line([*destination[:2], height], [*seller_at[:2], height],
                                             color=GUIDE, stroke_width=2.2))
                    new_ground.add(Line([*destination[:2], 0.04], [*seller_at[:2], 0.04],
                                        color=GUIDE, stroke_width=1.6).set_opacity(0.3))
                body = crowd_bodies['B', b]
                moves.append(body.animate.move_to([*destination[:2], body.get_center()[2]]))
            for s, price in enumerate(round_.after.asks):
                if price != round_.before.asks[s]:
                    prices.append(price_trackers[s].animate.set_value(price))
                    direction = UP if price > round_.before.asks[s] else DOWN
                    origin = price_tags[s].get_center() + RIGHT * 0.45
                    price_arrows.add(fixed(Arrow(origin - direction * 0.2,
                        origin + direction * 0.2, color=GUIDE, buff=0,
                        thickness=1.2, tip_width_ratio=4)))
            # Assign the next state before the last play so checkpoint replay keeps it.
            self.play(FadeIn(rays), FadeIn(price_arrows), *prices, run_time=0.3)
            self.play(FadeOut(connections), FadeOut(ground_connections),
                      FadeOut(rays), FadeOut(price_arrows), *moves, run_time=0.6)
            connections, ground_connections = new_connections, new_ground
            self.play(FadeIn(connections), FadeIn(ground_connections), run_time=0.2)
        self.pause('3.b')

        # ---- 4.a · Name what has just happened; keep nontraders in the picture.
        for s, tag in price_tags.items():
            tag.set_color(GUIDE if s in market.final.sellers else CAPTION)
        equilibrium_def = fixed(Tex(
            r'\mbox{ {{Equilibrium}} is where no one wants to change.}',
            tex_to_color_map={'Equilibrium': DEFINITION}).scale(DEFINITION_SCALE))
        equilibrium_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        first_seller = max(s for s in market.final.sellers if s is not None)
        arrow_end = price_tags[first_seller].get_center() + DOWN * 0.17
        equilibrium_arrow = fixed(Arrow(equilibrium_def.get_top() + RIGHT * 2.6 + UP * 0.1,
                                         arrow_end, color=DEFINITION, thickness=1.2, tip_width_ratio=4, buff=0.1))
        self.play(FadeIn(equilibrium_def), FadeIn(equilibrium_arrow))
        self.pause('4.a')

        # ---- 4.b · Only now do the people's marginal bars become a graph.
        self.remove(equilibrium_def, equilibrium_arrow, head)
        head = fixed(title('What does the graph show?'))
        self.play(FadeIn(head), self.camera.frame.animate.reorient(
            0, 48, center=[4, 0, 0.65], height=11), run_time=1.8)
        unit_ax = style_axes([0, 10, 1], [0, 8, 2], x_length=4.8, y_length=4.6)
        unit_ax.shift(np.array([4, 0.1, 0]) -
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
        self.play(FadeIn(unit_graph))
        twins, stairs = {}, {}
        for side, values, color, reverse in [('B', CROWD_MB, DEMAND, True),
                                             ('S', CROWD_MC, SUPPLY, False)]:
            ranked = sorted(range(10), key=lambda i: values[i], reverse=reverse)
            for i, value in enumerate(values):
                top = screen_point(self.camera.frame,
                    [*crowd_bodies[side, i].get_center()[:2], CROWD_BASE + value * CROWD_SCALE])
                base = screen_point(self.camera.frame,
                    [*crowd_bodies[side, i].get_center()[:2], CROWD_BASE])
                twin = fixed(Rectangle(width=0.06, height=abs(top[1] - base[1]),
                    color=color, fill_color=color, fill_opacity=0.2, stroke_width=1))
                twin.move_to((top + base) / 2)
                twins[side, i] = twin
            self.play(*[FadeIn(twins[side, i]) for i in range(10)], run_time=0.3)
            self.play(LaggedStart(*[twins[side, i].animate.stretch_to_fit_width(0.45)
                .stretch_to_fit_height(value * 4.6 / 8)
                .move_to(unit_ax.c2p(i + 0.5, value / 2))
                for i, value in enumerate(values)], lag_ratio=0.04), run_time=1.5)
            self.play(*[twins[side, i].animate.move_to(
                unit_ax.c2p(rank + 0.5, values[i] / 2))
                for rank, i in enumerate(ranked)], run_time=1.4)
            steps = fixed(VGroup(*[Line(unit_ax.c2p(rank, values[i]),
                unit_ax.c2p(rank + 1, values[i]), color=color, stroke_width=3)
                for rank, i in enumerate(ranked)]))
            stairs[side] = steps
            self.play(FadeIn(steps))
        unit_price = fixed(DashedLine(unit_ax.c2p(0, 4), unit_ax.c2p(10, 4),
                                      color=GUIDE, stroke_width=2))
        unit_drop = fixed(DashedLine(unit_ax.c2p(6, 4), unit_ax.c2p(6, 0),
                                     color=GUIDE, stroke_width=2))
        unit_read = fixed(Tex(r'$Q_d=Q_s=6$', color=GUIDE).scale(0.7)
                          .next_to(unit_ax.c2p(6, 0), DOWN, buff=0.65))
        self.play(FadeIn(unit_price), FadeIn(unit_drop), FadeIn(unit_read))
        self.pause('4.b')

        # ---- 4.c · A new aggregate example, explicitly in thousands of pounds.
        self.play(*[FadeOut(m) for m in list(self.mobjects)])
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
            self.play(*[FadeOut(m) for m in list(self.mobjects)])
            self.set_camera_orientation(phi=48 * DEGREES, theta=0)
            self.camera.frame.move_to([4, 0, 0.65]).set_height(11)
            self.add(head)
            initial_matches = ([0, 2, 5, 7, None, None, None, None, None, None]
                               if test_price == 3 else
                               [4, None, None, None, 5, None, None, None, None, None])
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
                                         color=GUIDE, stroke_width=2.2))
                    ground_connections.add(Line([*spot[:2], 0.04], [*seller_at[:2], 0.04],
                                                color=GUIDE, stroke_width=1.6).set_opacity(0.3))
            for s in range(10):
                active = s in willing_sellers
                crowd_bodies['S', s].set_opacity(1 if active else 0.3)
                crowd_bars['S', s].set_opacity(0.65 if active else 0.15)
                price_trackers[s].set_value(test_price)
                price_tags[s].set_color(GUIDE).set_opacity(1 if active else 0)
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
                      *[FadeIn(m) for m in price_tags.values()],
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
            else:
                self.pause('5.d.i')
                self.remove(definition, definition_arrow)
                textbook_word = fixed(Tex('Surplus', color=INK).scale(0.8).move_to([-4, -2.6, 0]))
                strike = fixed(Line(textbook_word.get_left(), textbook_word.get_right(),
                                    color=MUTED, stroke_width=2))
                excess_word = fixed(Tex('Excess', color=DEFINITION).scale(0.8)
                                    .next_to(textbook_word, DOWN, buff=0.3))
                self.play(FadeIn(textbook_word))
                self.play(FadeIn(strike), FadeIn(excess_word))
                self.pause('5.e')
                self.remove(textbook_word, strike, excess_word)

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
                next_matches = [0, None, None, None, 5, None, None, None, None, None]
                next_asks = [5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
                seed = 249
                action_words = r'Molly $\longrightarrow$ Gary: $\$5$'
            action_caption = fixed(Tex(action_words, color=INK).scale(DEFINITION_SCALE))
            action_caption.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
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
                                               color=GUIDE, stroke_width=2.2))
                    replacement_ground.add(Line([*buyer_at[:2], 0.04], [*seller_at[:2], 0.04],
                                                color=GUIDE, stroke_width=1.6).set_opacity(0.3))
            self.play(FadeIn(action_caption), FadeOut(connections), FadeOut(ground_connections),
                      *moves, price_trackers[0].animate.set_value(offer), run_time=1.5)
            connections, ground_connections = replacement_lines, replacement_ground
            self.play(FadeIn(connections), FadeIn(ground_connections))
            if test_price == 3:
                self.pause('5.b.i')
            else:
                self.pause('5.f')
            self.remove(action_caption)
            adjustment = simulate(CROWD_MB, CROWD_MC, next_asks, seed=seed,
                                  initial_sellers=next_matches, step=BID_STEP)
            assert adjustment.settled
            assert sum(s is not None for s in adjustment.final.sellers) == 6
            assert all(adjustment.final.asks[s] == 4
                       for s in adjustment.final.sellers if s is not None)
            for s in range(10):
                price_trackers[s].set_value(next_asks[s])
                price_tags[s].set_opacity(1)
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
                                                 color=GUIDE, stroke_width=2.2))
                        new_ground.add(Line([*destination[:2], 0.04], [*seller_at[:2], 0.04],
                                            color=GUIDE, stroke_width=1.6).set_opacity(0.3))
                    body = crowd_bodies['B', b]
                    moves.append(body.animate.move_to([*destination[:2], body.get_center()[2]]))
                for s, price in enumerate(round_.after.asks):
                    if price != round_.before.asks[s]:
                        prices.append(price_trackers[s].animate.set_value(price))
                        direction = UP if price > round_.before.asks[s] else DOWN
                        origin = price_tags[s].get_center() + RIGHT * 0.45
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
            for s, tag in price_tags.items():
                tag.set_color(GUIDE if s in adjustment.final.sellers else CAPTION)
            self.play(FadeIn(unit_price), FadeIn(unit_quantities))
            if test_price == 3:
                self.pause('5.c')
            else:
                self.pause('5.g')

        # ---- 5.h · Restore the discovered allocation before testing one person.
        self.remove(head)
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
                                                color=GUIDE, stroke_width=2.2)
                restored_ground[b] = Line([*spot[:2], 0.04], [*seller_at[:2], 0.04],
                                          color=GUIDE, stroke_width=1.6).set_opacity(0.3)
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
        self.remove(refusal)
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
                               color=GUIDE, stroke_width=2)
        refusal = fixed(Tex(r'Offer $\$3.75$\quad MC $\$4$', color=INK).scale(DEFINITION_SCALE))
        refusal.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(low_offer), FadeIn(refusal))
        self.pause('5.h.ii')
        self.remove(refusal)
        self.play(FadeOut(low_offer))
        stable = fixed(Tex(r'\mbox{ {{Equilibrium}} is where no one wants to change.}',
                           tex_to_color_map={'Equilibrium': DEFINITION}).scale(DEFINITION_SCALE))
        stable.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(stable), FadeIn(unit_price), FadeIn(unit_quantities))
        self.pause('5.h.iii')
