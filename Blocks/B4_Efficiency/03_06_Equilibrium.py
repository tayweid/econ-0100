# maniml 03_06_Equilibrium.py B4Equilibrium
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


class B4Equilibrium(ThreeDScene):
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
        for ax, values, side in [(demand_axes, BUYER_MB, 'buyer'), (supply_axes, SELLER_MC, 'seller')]:
            quantity = np.count_nonzero(values + EPS >= price.get_value()) if side == 'buyer' else np.count_nonzero(values <= price.get_value() + EPS)
            line = DashedLine(ax.c2p(0, price.get_value()), ax.c2p(quantity, price.get_value()), color=GUIDE, stroke_width=2.3)
            line.axes, line.price, line.values, line.side = ax, price, values, side
            line.add_updater(lambda m: m.put_start_and_end_on(m.axes.c2p(0, m.price.get_value()), m.axes.c2p(np.count_nonzero(m.values + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else np.count_nonzero(m.values <= m.price.get_value() + 1e-7), m.price.get_value())))
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

        # ---- 1.c / 1.d · Off-equilibrium first. No $4 answer has appeared.
        show_counts.set_value(0)
        show_trades.set_value(0)
        show_buyers.set_value(0)
        show_sellers.set_value(0)
        head = fixed(title(r'At $\$3$, who can trade?'))
        question = fixed(Tex('How much would each side trade?', color=DEFINITION)).scale(0.82).move_to([0, -3.65, 0])
        self.add(head, crowd, crowd_hud, graphs, question)
        self.pause('1.d')

        # ---- 1.e · Willing people and actual trades are different counts.
        self.play(show_counts.animate.set_value(1), show_buyers.animate.set_value(1),
                  show_sellers.animate.set_value(1), show_trades.animate.set_value(1))
        shortage = fixed(Tex(r'Shortage: 25,000 lb. A check means willing; a circle means trading.', color=INK)).scale(0.64).move_to([0, -3.65, 0])
        self.play(ReplacementTransform(question, shortage))
        unserved = VGroup(*[Circle(radius=0.19, color=FOCUS, stroke_width=2).move_to(buyer_positions[n]) for n in range(20, 45)])
        self.play(Create(unserved))
        self.pause('1.e')

        # ---- 1.j · The class tackles incentives BEFORE equilibrium resolves.
        cover = fixed(Rectangle(width=16, height=8, stroke_width=0, fill_color=BG, fill_opacity=1))
        exercise_head = fixed(title('Exercise B3 Q2: a price away from equilibrium'))
        equations = fixed(Tex(r'$P=12-Q_d/2 \qquad P=2+Q_s/2$', color=INK)).scale(1.0).move_to([0, 2.18, 0])
        exercise_units = fixed(Tex('Pumpkin pasties. Price: 5 galleons.', color=CAPTION)).scale(0.8).move_to([0, 1.44, 0])
        prompts = VGroup(
            fixed(Tex('a) What is the quantity demanded?')),
            fixed(Tex('b) What is the quantity supplied?')),
            fixed(Tex('c) Is this a shortage or an excess, and how large?')),
            fixed(Tex('d) Which way will the price move?')),
        ).scale(0.82).arrange(DOWN, aligned_edge=LEFT, buff=0.40).move_to([0, -0.32, 0])
        incentive_question = fixed(Tex('What would buyers and sellers want to do?', color=DEFINITION)).scale(0.85).move_to([0, -2.65, 0])
        exercise = fixed(VGroup(cover, exercise_head, equations, exercise_units, prompts, incentive_question))
        self.play(FadeIn(exercise))
        self.pause('1.j')
        self.play(FadeOut(exercise), FadeOut(unserved), FadeOut(shortage))

        # ---- 1.f · Amanda-Grace compares waiting with an actual alternative.
        ag_head = fixed(title('What would Amanda-Grace do?'))
        self.play(ReplacementTransform(head, ag_head))
        head = ag_head
        ag_focus = Circle(radius=0.22, color=FOCUS, stroke_width=3).move_to(buyer_positions[24])
        ag_name = fixed(Tex('Amanda-Grace', color=INK)).scale(0.56).move_to([-4.55, 0.40, 0])
        stay_box = fixed(Rectangle(width=6.35, height=0.73, color=MUTED).move_to([-3.72, -3.53, 0]))
        bid_box = fixed(Rectangle(width=6.35, height=0.73, color=MUTED).move_to([3.32, -3.53, 0]))
        stay_text = fixed(Tex(r'Wait at $\$3$: no trade; gain $\$0$', color=INK)).scale(0.62).move_to(stay_box)
        bid_text = fixed(Tex(r'Offer $\$3.25$: gain $\$3.75$/lb', color=INK)).scale(0.62).move_to(bid_box)
        bid = DashedLine(buyer_positions[24], seller_positions[0], color=GUIDE, stroke_width=2)
        seller_gain = fixed(Tex(r'Seller receives $\$0.25$ more per lb', color=SUPPLY)).scale(0.52).move_to([-3.1, -2.91, 0])
        self.play(Create(ag_focus), FadeIn(ag_name), Create(bid), FadeIn(stay_box), FadeIn(bid_box), FadeIn(stay_text), FadeIn(bid_text), FadeOut(units), FadeIn(seller_gain))

        self.play(FadeOut(ag_focus), FadeOut(bid), ag_name.animate.move_to([-2.9, -2.45, 0]))

        # B3 2.a.i: the same head-on camera, close bars, and material people.
        buy_person = buyer_people[24].copy()
        buy_counterparty = seller_people[0].copy()
        buy_mb = buyer_bars[24].copy()
        buy_mc = seller_bars[0].copy()
        buy_detail = Group(buy_person, buy_counterparty, buy_mb, buy_mc)
        self.add(buy_detail)
        buy_targets = []
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            shadow = Disk3D(radius=0.28, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(color).move_to([x, 0, 0.025])
            orb = Sphere(radius=0.23, color=color, resolution=(12, 8)).move_to([x, 0, 0.32])
            buy_targets.append(Group(shadow, orb))
        buy_mb_target = Rectangle3D(width=1.10, height=7 * 0.55, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
        buy_mb_target.rotate(90 * DEGREES, RIGHT).move_to([-0.61, 0, 0.75 + 7 * 0.55 / 2])
        buy_mc_target = Rectangle3D(width=1.10, height=2.05 * 0.55, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
        buy_mc_target.rotate(90 * DEGREES, RIGHT).move_to([0.61, 0, 0.75 + 2.05 * 0.55 / 2])
        crowd.suspend_updating()
        crowd_hud.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_hud), FadeOut(graphs),
                  Transform(buy_person, buy_targets[0]), Transform(buy_counterparty, buy_targets[1]),
                  Transform(buy_mb, buy_mb_target), Transform(buy_mc, buy_mc_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        buy_zero = Line([-1.31, -0.02, 0.75], [1.31, -0.02, 0.75], color=MUTED, stroke_width=1.5)
        buy_price = Line([-1.16, -0.045, 0.75 + 3 * 0.55], [1.16, -0.045, 0.75 + 3 * 0.55], color=GUIDE, stroke_width=3)
        buy_proposal = DashedLine([-1.16, -0.055, 0.75 + 3.25 * 0.55], [1.16, -0.055, 0.75 + 3.25 * 0.55], color=GUIDE, stroke_width=3)
        buy_values = fixed(VGroup(
            Tex(r'MB $\$7$', color=DEMAND).scale(0.75).move_to([-2.80, 1.7, 0]),
            Tex(r'MC $\$2.05$', color=SUPPLY).scale(0.75).move_to([2.80, 0.3, 0])))
        self.play(Create(buy_zero), Create(buy_price), Create(buy_proposal), FadeIn(buy_values))
        self.pause('1.f')
        self.play(buy_price.animate.set_z(0.75 + 3.25 * 0.55), FadeOut(buy_proposal), bid_box.animate.set_color(GREEN), run_time=0.7)
        self.play(FadeOut(buy_detail), FadeOut(buy_zero), FadeOut(buy_price), FadeOut(buy_values),
                  self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11), run_time=1.3)
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_hud.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_hud, graphs)
        self.add(ag_focus, bid)
        # One illustrative switch is not an additional sale. Qx remains 20.
        buyer_circles[19].suspend_updating()
        buyer_circles[24].suspend_updating()
        ag_start_body = buyer_people[24].get_center().copy()
        ag_start_bar = buyer_bars[24].get_center().copy()
        ag_move = seller_positions[0] - buyer_positions[24] + LEFT * 0.34
        accepted_bid = Line(seller_positions[0] + LEFT * 0.34, seller_positions[0], color=GREEN, stroke_width=2)
        self.play(ReplacementTransform(bid, accepted_bid), bid_box.animate.set_color(GREEN),
                  buyer_people[24].animate.shift(ag_move), buyer_bars[24].animate.shift(ag_move),
                  buyer_circles[19].animate.set_stroke(opacity=0), buyer_circles[24].animate.move_to(seller_positions[0] + LEFT * 0.34).set_stroke(opacity=1), run_time=0.8)
        everyone = fixed(Tex('Other unserved buyers have the same incentive.', color=INK)).scale(0.79).move_to([0, -3.55, 0])
        self.play(FadeOut(stay_box), FadeOut(bid_box), FadeOut(stay_text), FadeOut(bid_text),
                  FadeOut(accepted_bid), FadeOut(ag_focus), FadeOut(ag_name), FadeOut(seller_gain), FadeIn(everyone))
        # Resume sorted common-price snapshots after the individual illustration.
        self.play(buyer_people[24].animate.move_to(ag_start_body), buyer_bars[24].animate.move_to(ag_start_bar),
                  buyer_circles[24].animate.move_to(buyer_positions[24]), run_time=0.5)
        buyer_circles[19].resume_updating()
        buyer_circles[24].resume_updating()
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
        high_question = fixed(Tex('Who would buy? Who would sell? Who actually trades?', color=DEFINITION)).scale(0.76).move_to([0, -3.55, 0])
        self.play(FadeIn(high_question))
        self.pause('1.g')

        # ---- 1.h · Andrew can attract a buyer by asking less.
        self.play(FadeOut(high_question), show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1))
        excess = fixed(Tex(r'Excess: 50,000 lb. Andrew is willing, but has no buyer.', color=INK)).scale(0.65).move_to([0, -2.91, 0])
        self.remove(units)
        andrew_focus = Circle(radius=0.22, color=FOCUS, stroke_width=3).move_to(seller_positions[39])
        stay_text = fixed(Tex(r'Keep $\$6$: no buyer; gain $\$0$', color=INK)).scale(0.62).move_to(stay_box)
        cut_text = fixed(Tex(r'Ask $\$5.75$: gain $\$1.75$/lb', color=INK)).scale(0.62).move_to(bid_box)
        bid_box.set_color(MUTED)
        cut = DashedLine(seller_positions[39], buyer_positions[29], color=GUIDE, stroke_width=2)
        self.play(FadeIn(excess), Create(andrew_focus), Create(cut), FadeIn(stay_box), FadeIn(bid_box), FadeIn(stay_text), FadeIn(cut_text))

        andrew_head = fixed(title('What would Andrew do?'))
        self.play(FadeOut(andrew_focus), FadeOut(cut), FadeOut(tried_low), ReplacementTransform(head, andrew_head))
        head = andrew_head

        # B3 2.a.i: the same head-on camera, close bars, and material people.
        sell_person = buyer_people[29].copy()
        sell_counterparty = seller_people[39].copy()
        sell_mb = buyer_bars[29].copy()
        sell_mc = seller_bars[39].copy()
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
        crowd_hud.suspend_updating()
        graphs.suspend_updating()
        self.play(FadeOut(crowd), FadeOut(crowd_hud), FadeOut(graphs),
                  Transform(sell_person, sell_targets[0]), Transform(sell_counterparty, sell_targets[1]),
                  Transform(sell_mb, sell_mb_target), Transform(sell_mc, sell_mc_target),
                  self.camera.frame.animate.reorient(0, 90, center=[0, 0, 2.05], height=7.2), run_time=1.8)
        sell_zero = Line([-1.31, -0.02, 0.75], [1.31, -0.02, 0.75], color=MUTED, stroke_width=1.5)
        sell_price = Line([-1.16, -0.045, 0.75 + 6 * 0.55], [1.16, -0.045, 0.75 + 6 * 0.55], color=GUIDE, stroke_width=3)
        sell_proposal = DashedLine([-1.16, -0.055, 0.75 + 5.75 * 0.55], [1.16, -0.055, 0.75 + 5.75 * 0.55], color=GUIDE, stroke_width=3)
        sell_values = fixed(VGroup(
            Tex(r'MB $\$6$', color=DEMAND).scale(0.75).move_to([-2.80, 1.7, 0]),
            Tex(r'MC $\$4$', color=SUPPLY).scale(0.75).move_to([2.80, 0.3, 0]),
            Tex('Gary', color=INK).scale(0.65).move_to([-2.5, -2.45, 0]),
            Tex('Andrew', color=INK).scale(0.65).move_to([2.5, -2.45, 0])))
        self.play(Create(sell_zero), Create(sell_price), Create(sell_proposal), FadeIn(sell_values))
        self.pause('1.h')
        self.play(sell_price.animate.set_z(0.75 + 5.75 * 0.55), FadeOut(sell_proposal), bid_box.animate.set_color(GREEN), run_time=0.7)
        self.play(FadeOut(sell_detail), FadeOut(sell_zero), FadeOut(sell_price), FadeOut(sell_values),
                  self.camera.frame.animate.reorient(0, 48, center=[4, 0, 0.65], height=11), run_time=1.3)
        # Return to the exact B3 plaza before compressing everyone's adjustment.
        crowd.resume_updating()
        crowd_hud.resume_updating()
        graphs.resume_updating()
        self.add(crowd, crowd_hud, graphs)
        self.add(andrew_focus, cut, tried_low)
        seller_circles[29].suspend_updating()
        seller_circles[39].suspend_updating()
        gary_start_body = buyer_people[29].get_center().copy()
        gary_start_bar = buyer_bars[29].get_center().copy()
        gary_move = seller_positions[39] - buyer_positions[29] + LEFT * 0.34
        accepted_cut = Line(seller_positions[39] + LEFT * 0.34, seller_positions[39], color=GREEN, stroke_width=2)
        self.play(ReplacementTransform(cut, accepted_cut), bid_box.animate.set_color(GREEN),
                  buyer_people[29].animate.shift(gary_move), buyer_bars[29].animate.shift(gary_move),
                  seller_circles[29].animate.set_stroke(opacity=0), seller_circles[39].animate.set_stroke(opacity=1), run_time=0.8)
        everyone = fixed(Tex('Other unserved sellers have the same incentive.', color=INK)).scale(0.79).move_to([0, -3.55, 0])
        self.play(FadeOut(excess), FadeOut(andrew_focus), FadeOut(accepted_cut), FadeOut(stay_box), FadeOut(bid_box), FadeOut(stay_text), FadeOut(cut_text), FadeIn(everyone))
        self.play(buyer_people[29].animate.move_to(gary_start_body), buyer_bars[29].animate.move_to(gary_start_bar), run_time=0.5)
        seller_circles[29].resume_updating()
        seller_circles[39].resume_updating()
        self.add(units)
        tried_high = VGroup(*[DashedLine(ax.c2p(0, 6), ax.c2p(q, 6), color=GUIDE, stroke_width=1).set_opacity(0.25) for ax, q in [(demand_axes, 30), (supply_axes, 80)]])
        fixed(tried_high)
        self.add(tried_high)
        self.play(price.animate.set_value(4), run_time=3.0, rate_func=linear)

        # ---- 1.i · Counts and incentives are two views of the same condition.
        eq_head = fixed(title(r'Why does $\$4$ hold?'))
        equilibrium = fixed(VGroup(
            fixed(Tex(r'Equilibrium: $Q_d=Q_s=40$', color=DEFINITION)),
            fixed(Tex('No willing buyer or seller is left without a trade.', color=INK)),
        )).scale(0.72).arrange(DOWN, buff=0.13).move_to([0, -3.49, 0])
        self.play(ReplacementTransform(head, eq_head), ReplacementTransform(everyone, equilibrium))
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
