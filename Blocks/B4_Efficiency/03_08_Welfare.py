# maniml 03_08_Welfare.py B4Welfare
# B4 | Planner and First Welfare Theorem. Storyboard beats 2.a through 5.d.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from scene_layers import fixed, add_market_objects, screen_point


class B4Welfare(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to([4, 0, 0.65]).set_height(11)
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
        bottom = fixed(Tex('Could we make the total gain larger?', color=DEFINITION))
        bottom.scale(BOTTOM_SCALE).set_x(0).to_edge(DOWN, buff=0.05)
        units = fixed(Tex(r'One person: 1,000 lb\quad Bars: dollars/lb', color=CAPTION))
        units.scale(0.55).move_to([-3.3, -2.90, 0])
        buyers_label = fixed(Tex('Buyers: highest MB first', color=DEMAND)).scale(0.65)
        buyers_label.move_to([-3.3, 2.65, 0])
        sellers_label = fixed(Tex('Sellers: lowest MC first', color=SUPPLY)).scale(0.65)
        sellers_label.move_to([-3.3, -2.55, 0])
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
                check = fixed(VMobject(color=color, stroke_width=check_width).set_points_as_corners(check_points))
                check.anchor, check.value, check.dollar_height = bar, value, DOLLAR_HEIGHT
                check.add_updater(lambda m: m.move_to(screen_point(self.camera.frame,
                    m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10))).set_fill(opacity=0))
                check.set_stroke(opacity=1 if i < EQUILIBRIUM_Q else 0).set_fill(opacity=0)
                bodies[side, i + 1], bars[side, i + 1] = body, bar
                rings[side, i + 1], checks[side, i + 1] = ring, check
                crowd.add(body, bar, ring)
                market_checks.add(check)
        ax = axes((0, 100, 20), (0, 13, 2), x_length=5.8, y_length=4.8)
        ax.shift(np.array([1.15, -2.15, 0]) - ax.c2p(0, 0))
        p_label = fixed(Tex('P', color=INK)).scale(0.65).next_to(ax.c2p(0, 13), LEFT, buff=0.18)
        q_label = fixed(Tex('Q', color=INK)).scale(0.65).next_to(ax.c2p(100, 0), DOWN, buff=0.22)
        graph_units = fixed(Tex('Thousands of pounds', color=CAPTION)).scale(0.5)
        graph_units.next_to(ax.c2p(50, 0), DOWN, buff=0.32)
        ticks = VGroup()
        for q in [20, 40, 60, 80, 100]:
            ticks.add(fixed(Tex(str(q), color=MUTED)).scale(0.43).next_to(ax.c2p(q, 0), DOWN, buff=0.09))
        for p in [8, 12]:
            ticks.add(fixed(Tex(str(p), color=MUTED)).scale(0.43).next_to(ax.c2p(0, p), LEFT, buff=0.12))
        demand_points, supply_points = [], []
        for n, value in enumerate(MB, start=1):
            demand_points.extend([ax.c2p(n - 1, value), ax.c2p(n, value)])
        for n, value in enumerate(MC, start=1):
            supply_points.extend([ax.c2p(n - 1, value), ax.c2p(n, value)])
        demand = polyline(demand_points, color=DEMAND, width=2.5)
        supply = polyline(supply_points, color=SUPPLY, width=2.5)
        fitted = VGroup(Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND),
                        Line(ax.c2p(0, 2), ax.c2p(100, 7), color=SUPPLY)).set_opacity(0.17)
        curve_names = VGroup(fixed(Tex('MB', color=DEMAND)).scale(0.6).move_to(ax.c2p(13, 11.3)),
                             fixed(Tex('MC', color=SUPPLY)).scale(0.6).move_to(ax.c2p(88, 7.5)))
        graph = VGroup(ax, p_label, q_label, graph_units, ticks, fitted, demand, supply, curve_names)
        price_line = DashedLine(ax.c2p(0, PRICE), ax.c2p(40, PRICE), color=GUIDE, stroke_width=2)
        price_line.put_start_and_end_on(ax.c2p(0, PRICE), ax.c2p(40, PRICE))
        price_read = fixed(Tex(r'\$4', color=GUIDE)).scale(0.65).next_to(ax.c2p(0, PRICE), LEFT, buff=0.3)
        quantity = ValueTracker(40)
        q_guide = DashedLine(ax.c2p(40, 0), ax.c2p(40, 12), color=GUIDE, stroke_width=1.6).set_opacity(0.55)
        q_guide.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(quantity.get_value(), 0), ax.c2p(quantity.get_value(), 12)))
        counts = fixed(Tex(r'$Q_d=Q_s=Q_x=40$', color=GUIDE)).scale(0.65).move_to([4.1, -2.98, 0])
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
        fixed(crowd_words)
        fixed(market_checks)
        for mob in [graph, cs_strips, ps_strips, gain_strips, price_line, q_guide]:
            fixed(mob)
        self.add(head, crowd, crowd_words, market_checks, graph, cs_strips, ps_strips,
                 price_line, price_read, q_guide, counts)

        # ---- 2.a · CS and PS are familiar; ask what could improve.
        self.play(FadeIn(bottom), cs_strips.animate.set_fill(opacity=0.55),
                  ps_strips.animate.set_fill(opacity=0.55), run_time=0.7)
        self.pause('2.a')

        # ---- 2.b · Move only this pair's payment, holding the trade fixed.
        self.play(FadeOut(bottom), *[mob.animate.set_opacity(0) for body in bodies.values() for mob in body],
                  *[bar.animate.set_opacity(0) for bar in bars.values()],
                  *[ring.animate.set_stroke(opacity=0).set_fill(opacity=0) for ring in rings.values()], FadeOut(crowd_words),
                  market_checks.animate.set_opacity(0),
                  graph.animate.set_opacity(0.2), cs_strips.animate.set_opacity(0.1),
                  ps_strips.animate.set_opacity(0.1), FadeOut(price_line), FadeOut(price_read),
                  FadeOut(q_guide), FadeOut(counts), run_time=0.45)
        self.play(FadeOut(head), run_time=0.2)
        self.remove(*[mob for key in bodies if key not in [('B', 20), ('S', 20)]
                      for mob in [bodies[key], bars[key], rings[key]]])
        head = fixed(title('What does the price change?'))
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
        mb_word = fixed(Tex(r'Buyer 20: MB \$8', color=DEMAND)).scale(0.62).move_to(screen_point(self.camera.frame, [-4.61, -0.1, BASE + 8 * HEIGHT + 0.4]))
        mc_word = fixed(Tex(r'Seller 20: MC \$3', color=SUPPLY)).scale(0.62).move_to([-1, -0.85, 0])
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
                          color=GOV, stroke_width=2.5).set_flat_stroke(False)
        pair_price.add_updater(lambda m: m.put_start_and_end_on(
            np.array([-5.16, -0.045, BASE + payment.get_value() * HEIGHT]),
            np.array([-2.84, -0.045, BASE + payment.get_value() * HEIGHT])))
        payment_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GOV)).scale(0.62)
        payment_number.add_updater(lambda m: m.set_value(payment.get_value()).move_to(
            screen_point(self.camera.frame, [-2.4, -0.1, BASE + payment.get_value() * HEIGHT])))
        fixed_gap = Line([-5.6, -0.045, BASE + 3 * HEIGHT], [-5.6, -0.045, BASE + 8 * HEIGHT],
                         color=TOTAL, stroke_width=5)
        gain_label = fixed(Tex(r'\$5/lb\quad $\times$ 1,000 lb = \$5,000', color=TOTAL)).scale(0.65)
        gain_label.move_to([-4.0, -2.95, 0])
        formulas = VGroup(fixed(Tex(r'$CS=MB-P$', color=DEMAND)), fixed(Tex(r'$PS=P-MC$', color=SUPPLY)))
        fixed(formulas)
        formulas.arrange(RIGHT, buff=0.5).scale(0.65).move_to([-4, 2.65, 0])
        cancellation = fixed(Tex(r'$(MB-P)+(P-MC)=MB-MC$', color=INK)).scale(0.74)
        cancellation.move_to([3.75, 0.7, 0])
        pair_units = fixed(Tex('One 1,000-lb lot', color=CAPTION)).scale(0.65).move_to([3.75, -0.05, 0])
        self.play(FadeIn(mb_word), FadeIn(mc_word),
                  FadeIn(cs_fill), FadeIn(ps_fill), FadeIn(pair_price), FadeIn(payment_number),
                  FadeIn(formulas), FadeIn(fixed_gap), FadeIn(gain_label))
        self.play(FadeIn(cancellation), FadeIn(pair_units))
        self.play(payment.animate.set_value(5), run_time=1.8)
        bottom = fixed(Tex('The price divides the gain.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('2.b')
        self.play(payment.animate.set_value(4), run_time=0.8)
        for mob in [cs_fill, ps_fill, pair_price, payment_number]:
            mob.clear_updaters()
        self.play(*[FadeOut(m) for m in [mb_word, mc_word, cs_fill, ps_fill,
                                       pair_price, payment_number, fixed_gap, gain_label, formulas,
                                       cancellation, pair_units, bottom]], run_time=0.45)
        self.play(Restore(mb_bar), Restore(mc_bar), Restore(bodies['B', 20]), Restore(bodies['S', 20]),
                  Restore(rings['B', 20]), Restore(rings['S', 20]),
                  self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11), run_time=1.0)

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
        self.play(FadeOut(head), graph.animate.set_opacity(1), run_time=0.25)
        fitted.set_opacity(0.17)
        head = fixed(title('Which trades should happen?'))
        q_word = fixed(Tex('Trades:', color=GUIDE)).scale(0.65).move_to([3.7, -2.97, 0])
        q_number = fixed(Integer(40, color=GUIDE)).scale(0.65).next_to(q_word, RIGHT, buff=0.15)
        q_number.add_updater(lambda m: m.set_value(round(quantity.get_value())).next_to(q_word, RIGHT, buff=0.15))
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
        comparison_words = fixed(VGroup())
        focus_labels = []
        for key, x, value, color, text in [
                (('B', 30), -6.0, 6, DEMAND, r'Gary: MB \$6'),
                (('B', 10), -4.2, 10, DEMAND, r'Buyer 10: MB \$10'),
                (('S', 10), -2.25, 2.5, SUPPLY, r'Seller 10: MC \$2.50')]:
            rings[key].set_stroke(opacity=0).set_fill(opacity=0)
            bodies[key].save_state()
            bars[key].save_state()
            self.play(bodies[key].animate.scale(0.23 * bodies[key].orb_unit_width / bodies[key][1].get_width()).move_to([x, 0, 0.32]).set_opacity(1),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]).set_opacity(0.65), run_time=0.45)
            label = fixed(Tex(text, color=color).scale(0.53))
            label.move_to(screen_point(self.camera.frame, [x, -0.1, 0.75 + value * 0.55 + 0.3]))
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
                  focus_labels[1].animate.set_x(screen_point(self.camera.frame, [-6, 0, 0])[0]),
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
        for key in focus_keys:
            self.play(Restore(bodies[key]), Restore(bars[key]), run_time=0.2)
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
        comparison_words = fixed(VGroup())
        focus_labels = []
        for key, x, value, color, text in [
                (('S', 40), -6.0, 4, SUPPLY, r'Andrew: MC \$4'),
                (('S', 10), -4.2, 2.5, SUPPLY, r'Seller 10: MC \$2.50'),
                (('B', 10), -2.25, 10, DEMAND, r'Buyer 10: MB \$10')]:
            rings[key].set_stroke(opacity=0).set_fill(opacity=0)
            bodies[key].save_state()
            bars[key].save_state()
            self.play(bodies[key].animate.scale(0.23 * bodies[key].orb_unit_width / bodies[key][1].get_width()).move_to([x, 0, 0.32]).set_opacity(1),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]).set_opacity(0.65), run_time=0.45)
            label = fixed(Tex(text, color=color).scale(0.53))
            label.move_to(screen_point(self.camera.frame, [x, -0.1, 0.75 + value * 0.55 + 0.3]))
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
                  focus_labels[1].animate.set_x(screen_point(self.camera.frame, [-6, 0, 0])[0]),
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
        for key in focus_keys:
            self.play(Restore(bodies[key]), Restore(bars[key]), run_time=0.2)
        self.play(self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11), run_time=1.0)
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

        # ---- 4.a · Park the graph; unfold the SAME people into ranked pairs.
        self.play(FadeOut(bottom), FadeOut(crowd_words), FadeOut(q_guide),
                  graph.animate.shift(RIGHT * 16), gain_strips.animate.shift(RIGHT * 16),
                  floor.animate.set_opacity(0.03), rim.animate.set_opacity(0.1),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.3)
        row_targets, row_gains = {}, VGroup()
        row_moves = []
        for key, body in bodies.items():
            side, n = key
            value = MB[n - 1] if side == 'B' else MC[n - 1]
            x = -6.6 + (n - 1) * 0.13 + (-0.027 if side == 'B' else 0.027)
            row_targets[key] = [x, 0, 0.75 + value * 0.35 / 2]
            row_moves.extend([body.animate.scale(0.025 * body.orb_unit_width / body[1].get_width()).move_to([x, 0, 0.42]),
                              bars[key].animate.stretch_to_fit_width(0.045).stretch_to_fit_depth(value * 0.35)
                              .move_to(row_targets[key]),
                              rings[key].animate.scale(0.08 / rings[key].get_width()).move_to([x, 0, 0.32])])
        self.play(*row_moves, run_time=1.4)
        for n in range(1, 40):
            x = -6.6 + (n - 1) * 0.13
            strip = Polygon([x - 0.025, -0.035, 0.75 + MC[n - 1] * 0.35],
                            [x + 0.025, -0.035, 0.75 + MC[n - 1] * 0.35],
                            [x + 0.025, -0.035, 0.75 + MB[n - 1] * 0.35],
                            [x - 0.025, -0.035, 0.75 + MB[n - 1] * 0.35],
                            stroke_color=TOTAL, stroke_width=0.6, fill_color=TOTAL,
                            fill_opacity=AREA_OPACITY if n <= 20 else 0)
            strip.set_stroke(opacity=1 if n <= 20 else 0)
            row_gains.add(strip)
        self.add(row_gains)
        row_quantity = Line([-6.6 + 19.5 * 0.13, 0, 0.5], [-6.6 + 19.5 * 0.13, 0, 4.75],
                            color=GUIDE, stroke_width=1.5)
        self.add(row_quantity)
        # The proposed pair uses B3's close-up dimensions. No circle is added.
        selected_pair = [('B', 21), ('S', 21)]
        selected_words = fixed(VGroup())
        for key, x, value, color, text in [
                (('B', 21), -0.61, 7.8, DEMAND, r'MB $\$7.80$'),
                (('S', 21), 0.61, 3.05, SUPPLY, r'MC $\$3.05$')]:
            self.play(bodies[key].animate.scale(9.2).move_to([x * 2.5, 0, 0.32]),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]),
                      rings[key].animate.scale(7.25).move_to([x * 2.5, 0, 0.045]), run_time=0.45)
            selected_words.add(fixed(Tex(text, color=color).scale(0.7)).move_to([x * 3, 2.7, 0]))
        self.play(self.camera.frame.animate.reorient(0, 90, center=[0, 0, 3.4], height=10.2),
                  row_gains.animate.fade(0.8), run_time=0.6)
        proposed_link = DashedLine([-1.525, 0, 0.045], [1.525, 0, 0.045], color=TOTAL, stroke_width=2)
        marginal_gap = Line([-1.4, -0.045, 0.75 + 3.05 * 0.55],
                            [-1.4, -0.045, 0.75 + 7.8 * 0.55], color=TOTAL, stroke_width=4).set_opacity(0.5)
        bottom = fixed(Tex('Should we add this trade?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(proposed_link), FadeIn(marginal_gap), FadeIn(bottom))
        self.pause('4.a')

        # ---- 4.b · An actual trade adds only its own positive gain.
        self.play(FadeOut(bottom), FadeOut(proposed_link), run_time=0.2)
        accepted_link = Line([-1.525, 0, 0.045], [1.525, 0, 0.045], color=GOV, stroke_width=2)
        marginal_read = fixed(Tex(r'Pair 21 adds $\$4,750$.', color=TOTAL)).scale(0.7).move_to([0, -2.9, 0])
        self.play(FadeIn(accepted_link), FadeIn(marginal_read), marginal_gap.animate.set_opacity(1),
                  rings['B', 21].animate.set_stroke(opacity=1).set_fill(opacity=0), rings['S', 21].animate.set_stroke(opacity=1).set_fill(opacity=0),
                  quantity.animate.set_value(21), run_time=0.6)
        self.play(*[FadeOut(m) for m in [selected_words, accepted_link, marginal_gap, marginal_read]], run_time=0.3)
        for key in selected_pair:
            x = row_targets[key][0]
            value = MB[key[1] - 1] if key[0] == 'B' else MC[key[1] - 1]
            self.play(bodies[key].animate.scale(1 / 9.2).move_to([x, 0, 0.42]),
                      bars[key].animate.stretch_to_fit_width(0.045).stretch_to_fit_depth(value * 0.35)
                      .move_to(row_targets[key]),
                      rings[key].animate.scale(1 / 7.25).move_to([x, 0, 0.32]).set_stroke(opacity=1).set_fill(opacity=0), run_time=0.3)
        self.play(self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=0.7)
        for n, strip in enumerate(row_gains, start=1):
            strip.set_fill(opacity=AREA_OPACITY if n <= 21 else 0).set_stroke(opacity=1 if n <= 21 else 0)
        for n in range(22, 40):
            self.play(quantity.animate.set_value(n), rings['B', n].animate.set_stroke(opacity=1).set_fill(opacity=0),
                      rings['S', n].animate.set_stroke(opacity=1).set_fill(opacity=0), row_quantity.animate.set_x(-6.6 + (n - 0.5) * 0.13),
                      row_gains[n - 1].animate.set_fill(opacity=AREA_OPACITY).set_stroke(opacity=1),
                      run_time=0.11, rate_func=linear)
        selected_words = fixed(VGroup())
        # Pair 39's original bars enlarge; there is still only one such trade.
        for key, x, value, color in [(('B', 39), -0.61, 4.2, DEMAND), (('S', 39), 0.61, 3.95, SUPPLY)]:
            self.play(bodies[key].animate.scale(9.2).move_to([x, 0, 0.32]),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]),
                      rings[key].animate.scale(7.25).move_to([x, 0, 0.045]), run_time=0.35)
            selected_words.add(fixed(Tex(rf'$\${value:.2f}$', color=color).scale(0.7))
                               .move_to(screen_point(self.camera.frame, [x, 0, 0.75 + value * 0.55 + 0.35])))
        boundary_read = fixed(Tex(r'Pair 39 adds $\$250$.', color=TOTAL)).scale(0.7).move_to([0, -2.95, 0])
        bottom = fixed(Tex(r'Another trade helps while $MB>MC$.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(boundary_read), FadeIn(bottom))
        self.pause('4.b')

        # ---- 4.c · Return pair 39; inspect only pair 40 on the same baseline.
        self.play(FadeOut(bottom), FadeOut(boundary_read), FadeOut(selected_words), run_time=0.2)
        for side in ['B', 'S']:
            key = (side, 39)
            value = MB[38] if side == 'B' else MC[38]
            self.play(bodies[key].animate.scale(1 / 9.2).move_to([row_targets[key][0], 0, 0.42]),
                      bars[key].animate.stretch_to_fit_width(0.045).stretch_to_fit_depth(value * 0.35)
                      .move_to(row_targets[key]),
                      rings[key].animate.scale(1 / 7.25).move_to([row_targets[key][0], 0, 0.32]), run_time=0.2)
        selected_words = fixed(VGroup())
        for key, x, color in [(('B', 40), -0.61, DEMAND), (('S', 40), 0.61, SUPPLY)]:
            self.play(bodies[key].animate.scale(9.2).move_to([x * 2.5, 0, 0.32]),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(4 * 0.55)
                      .move_to([x, 0, 0.75 + 4 * 0.55 / 2]),
                      rings[key].animate.scale(7.25).move_to([x * 2.5, 0, 0.045]), run_time=0.35)
            selected_words.add(fixed(Tex(r'$\$4$', color=color).scale(0.7))
                               .move_to(screen_point(self.camera.frame, [x, 0, 0.75 + 4 * 0.55 + 0.35])))
        boundary_read = fixed(Tex(r'Pair 40: MB $\$4$ = MC $\$4$', color=TOTAL)).scale(0.7).move_to([0, -2.95, 0])
        bottom = fixed(Tex('What does this trade add?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(boundary_read), FadeIn(bottom))
        self.pause('4.c')

        # ---- 4.d · The last selected pair adds zero area.
        self.play(FadeOut(bottom), FadeOut(boundary_read), run_time=0.2)
        self.play(quantity.animate.set_value(40), rings['B', 40].animate.set_stroke(opacity=1).set_fill(opacity=0),
                  rings['S', 40].animate.set_stroke(opacity=1).set_fill(opacity=0), run_time=0.5)
        boundary_read = fixed(Tex(r'The last trade adds $\$0$.', color=TOTAL)).scale(0.7).move_to([0, -2.95, 0])
        bottom = fixed(Tex('39 or 40: the same total gain.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(boundary_read), FadeIn(bottom))
        self.pause('4.d')

        # ---- 4.e · Pair 41 remains a proposal; no price can satisfy both.
        self.play(FadeOut(bottom), FadeOut(boundary_read), FadeOut(selected_words), run_time=0.25)
        for n in [40]:
            for side in ['B', 'S']:
                key = (side, n)
                value = MB[n - 1] if side == 'B' else MC[n - 1]
                self.play(bodies[key].animate.scale(1 / 9.2).move_to([row_targets[key][0], 0, 0.42]),
                          bars[key].animate.stretch_to_fit_width(0.045).stretch_to_fit_depth(value * 0.35)
                          .move_to(row_targets[key]),
                          rings[key].animate.scale(1 / 7.25).move_to([row_targets[key][0], 0, 0.32]), run_time=0.2)
        selected_words = fixed(VGroup())
        for key, x, value, color, text in [(('B', 41), -0.61, 3.8, DEMAND, r'Buyer needs $P\leq\$3.80$'),
                                          (('S', 41), 0.61, 4.05, SUPPLY, r'Seller needs $P\geq\$4.05$')]:
            self.play(bodies[key].animate.scale(9.2).move_to([x * 2.5, 0, 0.32]),
                      bars[key].animate.stretch_to_fit_width(1.1).stretch_to_fit_depth(value * 0.55)
                      .move_to([x, 0, 0.75 + value * 0.55 / 2]), run_time=0.35)
            selected_words.add(fixed(Tex(text, color=color).scale(0.65)).move_to([x * 3, 2.2, 0]))
        proposed_link = DashedLine([-1.525, 0, 0.045], [1.525, 0, 0.045], color=TOTAL, stroke_width=2)
        bottom = fixed(Tex('Would this trade help?', color=DEFINITION)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(selected_words), FadeIn(proposed_link), FadeIn(bottom))
        self.pause('4.e')
        self.play(FadeOut(bottom), run_time=0.2)
        bottom = fixed(Tex(r'$MC>MB$: this trade would lose $\$250$.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.wait(0.7)

        # ---- 4.f · The quantity changes membership and gains together.
        self.play(FadeOut(selected_words), FadeOut(proposed_link), FadeOut(bottom), run_time=0.25)
        for side in ['B', 'S']:
            key = (side, 41)
            value = MB[40] if side == 'B' else MC[40]
            self.play(bodies[key].animate.scale(1 / 9.2).move_to([row_targets[key][0], 0, 0.42]),
                      bars[key].animate.stretch_to_fit_width(0.045).stretch_to_fit_depth(value * 0.35)
                      .move_to(row_targets[key]), run_time=0.3)
        for n in range(40, 30, -1):
            animations = [quantity.animate.set_value(n - 1), rings['B', n].animate.set_stroke(opacity=0).set_fill(opacity=0),
                          rings['S', n].animate.set_stroke(opacity=0).set_fill(opacity=0),
                          row_quantity.animate.set_x(-6.6 + (n - 1.5) * 0.13)]
            if n < 40:
                animations.append(row_gains[n - 1].animate.set_fill(opacity=0))
            self.play(*animations, run_time=0.10, rate_func=linear)
        missing = fixed(Tex('Positive gains left unrealized', color=TOTAL)).scale(0.7).move_to([0, -2.95, 0])
        self.play(FadeIn(missing))
        for n in range(31, 41):
            animations = [quantity.animate.set_value(n), rings['B', n].animate.set_stroke(opacity=1).set_fill(opacity=0),
                          rings['S', n].animate.set_stroke(opacity=1).set_fill(opacity=0),
                          row_quantity.animate.set_x(-6.6 + (n - 0.5) * 0.13)]
            if n < 40:
                animations.append(row_gains[n - 1].animate.set_fill(opacity=AREA_OPACITY))
            self.play(*animations, run_time=0.10, rate_func=linear)
        self.play(FadeOut(missing), run_time=0.2)
        bottom = fixed(Tex('Take the gains; stop when additional cost exceeds benefit.', color=INK)).scale(BOTTOM_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=0.05)
        self.play(FadeIn(bottom))
        self.pause('4.f')

        # ---- 5.a · Return the SAME people and graph to B3's plaza view.
        self.play(FadeOut(bottom), FadeOut(head), FadeOut(q_word), FadeOut(q_number),
                  FadeOut(row_quantity), FadeOut(row_gains), run_time=0.3)
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
        self.play(*restore_people, graph.animate.shift(LEFT * 16), gain_strips.animate.shift(LEFT * 16),
                  self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11),
                  floor.animate.set_opacity(0.14), rim.animate.set_stroke(opacity=0.6), run_time=1.4)
        self.play(FadeIn(crowd_words), run_time=0.3)
        zero_dot = fixed(Dot(ax.c2p(40, 4), color=TOTAL, radius=0.065))
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
                  FadeIn(counts), run_time=0.9)
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
