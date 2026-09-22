# maniml 03_05_Sellers.py B4Sellers
# B4: exact people, one common price. See 02_Storyboard.md.
from manim import *
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from scene_layers import fixed, add_market_objects, screen_point


class B4Sellers(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.camera.frame.set_height(8)


        # One person is one 1,000-lb lot. Bar height is dollars per pound.
        BUYER_MB = np.array([12 - n / 5 for n in range(1, 60)])
        SELLER_MC = np.array([2 + n / 20 for n in range(1, 101)])
        EPS = 1e-7
        DOLLAR_HEIGHT = 0.035
        price = ValueTracker(3)
        show_counts = ValueTracker(1)
        show_trades = ValueTracker(1)
        show_buyers = ValueTracker(1)
        show_sellers = ValueTracker(1)
        self.add(price, show_counts, show_trades, show_buyers, show_sellers)

        # B3's plaza, material objects and camera are retained literally.
        # Only crowd density changes: 59 buyers / 100 sellers replace 10 / 10.
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to([4, 0, 0.65]).set_height(11)
        BAR_BASE = 0.38
        DOLLAR_HEIGHT = 0.05
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        buyer_people, buyer_bars, buyer_checks, buyer_circles = Group(), Group(), VGroup(), VGroup()
        seller_people, seller_bars, seller_checks, seller_circles = Group(), Group(), VGroup(), VGroup()
        buyer_positions, seller_positions = [], []
        buyer_prices, seller_prices = VGroup(), VGroup()
        for n, value in enumerate(BUYER_MB):
            x, y = -3.6 + (n % 20) * 0.38, 3.2 - (n // 20) * 0.9
            buyer_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.13, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(DEMAND).move_to([x, y, 0.025])
            orb = Sphere(radius=0.10, color=DEMAND, resolution=(12, 8)).move_to([x, y, 0.16])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.09, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = fixed(VMobject(color=DEMAND, stroke_width=2.0).set_points_as_corners([[-0.035, 0, 0], [-0.005, -0.03, 0], [0.05, 0.045, 0]]))
            check.price, check.value, check.visibility = price, value, show_buyers
            check.anchor, check.frame = bar, self.camera.frame
            check.add_updater(lambda m: m.move_to(screen_point(m.frame, m.anchor.get_center() + OUT * (m.value * 0.05 / 2 + 0.13))).set_stroke(opacity=m.visibility.get_value() * float(m.value + 1e-7 >= m.price.get_value())).set_fill(opacity=0))
            circle = Circle(radius=0.16, color=GREEN, stroke_width=2).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            buyer_people.add(person)
            buyer_bars.add(bar)
            buyer_checks.add(check)
            buyer_circles.add(circle)
        for n, value in enumerate(SELLER_MC):
            x, y = -3.6 + (n % 20) * 0.38, 0.15 - (n // 20) * 0.70
            seller_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.13, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(SUPPLY).move_to([x, y, 0.025])
            orb = Sphere(radius=0.10, color=SUPPLY, resolution=(12, 8)).move_to([x, y, 0.16])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.09, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = fixed(VMobject(color=SUPPLY, stroke_width=2.0).set_points_as_corners([[-0.035, 0, 0], [-0.005, -0.03, 0], [0.05, 0.045, 0]]))
            check.price, check.value, check.visibility = price, value, show_sellers
            check.anchor, check.frame = bar, self.camera.frame
            check.add_updater(lambda m: m.move_to(screen_point(m.frame, m.anchor.get_center() + OUT * (m.value * 0.05 / 2 + 0.13))).set_stroke(opacity=m.visibility.get_value() * float(m.value <= m.price.get_value() + 1e-7)).set_fill(opacity=0))
            circle = Circle(radius=0.16, color=GREEN, stroke_width=2).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            seller_people.add(person)
            seller_bars.add(bar)
            seller_checks.add(check)
            seller_circles.add(circle)
        for row in range(3):
            line = Line([-3.78, 3.2-row*0.9, BAR_BASE + 3*DOLLAR_HEIGHT], [3.80, 3.2-row*0.9, BAR_BASE + 3*DOLLAR_HEIGHT], color=GUIDE, stroke_width=1.3)
            line.price = price
            line.add_updater(lambda m: m.set_z(0.38 + 0.05 * m.price.get_value()))
            buyer_prices.add(line)
        for row in range(5):
            line = Line([-3.78, 0.15-row*0.7, BAR_BASE + 3*DOLLAR_HEIGHT], [3.80, 0.15-row*0.7, BAR_BASE + 3*DOLLAR_HEIGHT], color=GUIDE, stroke_width=1.3)
            line.price = price
            line.add_updater(lambda m: m.set_z(0.38 + 0.05 * m.price.get_value()))
            seller_prices.add(line)
        buyer_label = fixed(fixed(Tex('Buyers: highest MB first', color=DEMAND)).scale(0.56).move_to([-3.3, 2.65, 0]))
        seller_label = fixed(fixed(Tex('Sellers: lowest MC first', color=SUPPLY)).scale(0.56).move_to([-3.3, -2.55, 0]))
        units = fixed(fixed(Tex(r'One person = 1,000 lb', color=CAPTION)).scale(0.50).move_to([-3.3, -2.90, 0]))
        buyers = Group(buyer_bars, buyer_people, buyer_prices, buyer_circles)
        sellers = Group(seller_bars, seller_people, seller_prices, seller_circles)
        crowd = Group(floor, rim, buyers, sellers)
        crowd_hud = fixed(VGroup(buyer_checks, seller_checks, buyer_label, seller_label, units))

        # Same Q and P scales in both graphs. Exact staircases, faint fitted lines.
        demand_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=1.55)
        supply_axes = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=1.55)
        demand_axes.move_to([4.48, 1.75, 0])
        supply_axes.move_to([4.48, -0.89, 0])
        ticks = VGroup()
        for ax in [demand_axes, supply_axes]:
            for q in [0, 20, 40, 60, 80, 100]:
                ticks.add(fixed(Tex(str(q), color=CAPTION)).scale(0.38).next_to(ax.c2p(q, 0), DOWN, buff=0.10))
            for p in [4, 8, 12]:
                ticks.add(fixed(Tex(str(p), color=CAPTION)).scale(0.35).next_to(ax.c2p(0, p), LEFT, buff=0.10))
        demand_points, supply_points = [], []
        for n, value in enumerate(BUYER_MB):
            demand_points.extend([demand_axes.c2p(n, value), demand_axes.c2p(n + 1, value)])
        for n, value in enumerate(SELLER_MC):
            supply_points.extend([supply_axes.c2p(n, value), supply_axes.c2p(n + 1, value)])
        demand_steps = VMobject(color=DEMAND, stroke_width=2.4).set_points_as_corners(demand_points)
        supply_steps = VMobject(color=SUPPLY, stroke_width=2.4).set_points_as_corners(supply_points)
        demand_fit = Line(demand_axes.c2p(0, 12), demand_axes.c2p(60, 0), color=DEMAND).set_opacity(0.30)
        supply_fit = Line(supply_axes.c2p(0, 2), supply_axes.c2p(100, 7), color=SUPPLY).set_opacity(0.30)
        demand_word = fixed(Tex(r'Demand: $P=12-Q_d/5$', color=DEMAND)).scale(0.59).move_to([4.45, 2.85, 0])
        supply_word = fixed(Tex(r'Supply: $P=2+Q_s/20$', color=SUPPLY)).scale(0.59).move_to([4.45, 0.18, 0])
        graph_units = fixed(Tex(r'$Q$: thousands of pounds', color=CAPTION)).scale(0.48).move_to([4.5, -2.25, 0])
        graph_prices = VGroup()
        for ax in [demand_axes, supply_axes]:
            line = Line(ax.c2p(0, 3), ax.c2p(100, 3), color=GUIDE, stroke_width=2.3)
            line.axes, line.price = ax, price
            line.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(0, m.price.get_value()), m.axes.c2p(100, m.price.get_value())))
            graph_prices.add(line)
        demand_guide = Line(demand_axes.c2p(45, 0), demand_axes.c2p(45, 3), color=DEMAND, stroke_width=2)
        demand_guide.axes, demand_guide.price, demand_guide.values, demand_guide.visibility = demand_axes, price, BUYER_MB, show_counts
        demand_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), 0), m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()), m.price.get_value())).set_opacity(m.visibility.get_value()))
        supply_guide = Line(supply_axes.c2p(20, 0), supply_axes.c2p(20, 3), color=SUPPLY, stroke_width=2)
        supply_guide.axes, supply_guide.price, supply_guide.values, supply_guide.visibility = supply_axes, price, SELLER_MC, show_counts
        supply_guide.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), 0), m.axes.c2p(np.count_nonzero(m.values <= m.price.get_value() + 1e-7), m.price.get_value())).set_opacity(m.visibility.get_value()))
        # Readouts are computed from exactly the same predicates as the marks.
        counts = VGroup()
        for label, x, values, side in [('Q_d', 2.30, BUYER_MB, 'buyer'), ('Q_s', 4.10, SELLER_MC, 'seller'), ('Q_x', 5.90, BUYER_MB, 'trade')]:
            word = fixed(Tex(rf'${label}=$', color=DEMAND if side == 'buyer' else SUPPLY if side == 'seller' else GREEN)).scale(0.65).move_to([x, -2.85, 0])
            number = Integer(0, color=word.get_color()).scale(0.65).move_to([x + 0.77, -2.85, 0])
            number.price, number.values, number.mb, number.mc, number.side = price, values, BUYER_MB, SELLER_MC, side
            number.anchor, number.visibility = np.array([x + 0.77, -2.85, 0]), show_counts
            number.add_updater(lambda m: m.set_value(int(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else np.count_nonzero(m.values <= m.price.get_value() + 1e-7) if m.side == 'seller' else min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).move_to(m.anchor).set_opacity(m.visibility.get_value()))
            counts.add(word, number)
        price_word = fixed(Tex(r'Price: \$', color=GUIDE)).scale(0.57).move_to([-0.23, 2.89, 0])
        price_number = DecimalNumber(3, num_decimal_places=2, color=GUIDE).scale(0.57).move_to([0.78, 2.89, 0])
        price_number.price = price
        price_number.add_updater(lambda m: m.set_value(m.price.get_value()).move_to([0.78, 2.89, 0]))
        price_units = fixed(Tex(r'/lb', color=CAPTION)).scale(0.42).move_to([1.37, 2.89, 0])
        price_readout = VGroup(price_word, price_number, price_units)
        graphs = VGroup(demand_axes, supply_axes, ticks, demand_fit, supply_fit, demand_steps, supply_steps,
                        demand_word, supply_word, graph_prices, demand_guide, supply_guide, graph_units, counts, price_readout)
        fixed(graphs)
        # World and fixed overlay objects are added separately, as in B3.

        # ---- 1.c.sellers · Willingness to sell, before any allocation of trades.
        show_trades.set_value(0)
        head = fixed(title('How many would sell at this price?'))
        demand_ticks = VGroup(*list(ticks)[:9])
        demand_graph = fixed(VGroup(demand_axes, demand_ticks, demand_fit, demand_steps, demand_word, graph_prices[0], demand_guide))
        self.add(head, demand_graph, price_readout)
        self.set_camera_orientation(phi=90 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to([0, 0, 1.9]).set_height(8)
        full_bars, full_people = Group(), Group()
        full_points = []
        for n, value in enumerate(SELLER_MC):
            x = -6.90 + (n + 0.5) * 13.8 / 100
            bar = Rectangle3D(width=0.105, height=value * 0.24, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, 0, 0.75 + value * 0.24 / 2])
            full_bars.add(bar)
            shadow = Disk3D(radius=0.07, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(SUPPLY).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.065, color=SUPPLY, resolution=(12, 8)).move_to([x, 0, 0.16])
            full_people.add(Group(shadow, orb))
            full_points.extend([[x - 0.0525, 0, 0.75 + value * 0.24], [x + 0.0525, 0, 0.75 + value * 0.24]])
        full_profile = VMobject(color=SUPPLY, stroke_width=2.6).set_points_as_corners(full_points)
        one_lot = fixed(Tex(r'One person = 1,000 lb. Lowest cost first.', color=CAPTION)).scale(0.8).move_to([0, -3.45, 0])
        self.play(FadeIn(full_bars), FadeIn(full_people), FadeIn(one_lot))
        self.play(Create(full_profile), run_time=0.8)
        # B3's screen_point copy connects the actual world bars to the graph.
        projected_profile = fixed(VMobject(color=SUPPLY, stroke_width=2.6).set_points_as_corners(
            [screen_point(self.camera.frame, point) for point in full_points]))
        self.remove(full_profile)
        self.add(projected_profile)
        self.add(floor, rim)
        supply_ticks = VGroup(*list(ticks)[9:])
        supply_graph = fixed(VGroup(supply_axes, supply_ticks, supply_fit, supply_word))
        self.play(ReplacementTransform(full_bars, seller_bars), ReplacementTransform(full_people, seller_people),
                  ReplacementTransform(projected_profile, supply_steps), FadeIn(supply_graph), FadeIn(seller_label), self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11), run_time=1.7)
        self.play(FadeIn(seller_prices), FadeIn(graph_prices[1]))
        self.add(seller_checks, supply_guide, fixed(VGroup(*list(counts)[:4])), graph_units)
        rule = fixed(Tex(r'$MC\leq P$: willing to sell. At $\$3$, 20 sellers are willing.', color=INK)).scale(0.78).move_to([0, -3.45, 0])
        self.play(ReplacementTransform(one_lot, rule))
        boundary = fixed(Tex(r'The next seller needs $\$3.05$/lb.', color=CAPTION)).scale(0.68).move_to([-3.8, 1.2, 0])
        self.play(FadeIn(boundary))
        self.pause('1.c.sellers')
