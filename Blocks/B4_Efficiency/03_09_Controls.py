# maniml 03_09_Controls.py B4Controls
# Exact crowd welfare and price controls. See 02_Storyboard.md.
from manim import *
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from scene_layers import fixed, add_market_objects, screen_point


class B4Controls(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
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

        # B3's plaza, material objects and camera are retained literally.
        # One uninterrupted ranked line per side; the bars carry the values.
        self.set_camera_orientation(phi=48 * DEGREES, theta=0, focal_distance=50)
        self.camera.frame.move_to([4, 0, 0.65]).set_height(11)
        BAR_BASE = 0.18
        ROW_LEFT, ROW_WIDTH = -3.7, 7.4
        BUYER_Y, SELLER_Y = 2.0, -1.7
        floor = Disk3D(radius=4.8, resolution=(2, 64), shading=(0, 0, 0),
                       opacity=0.14).set_color(MUTED)
        rim = Circle(radius=4.8, color=MUTED, stroke_width=1.2)
        rim.shift(OUT * 0.015).set_stroke(opacity=0.6)
        buyer_people, buyer_bars, buyer_checks, buyer_circles = Group(), Group(), VGroup(), VGroup()
        seller_people, seller_bars, seller_checks, seller_circles = Group(), Group(), VGroup(), VGroup()
        buyer_positions, seller_positions = [], []
        buyer_prices, seller_prices = VGroup(), VGroup()
        for n, value in enumerate(BUYER_MB):
            x, y = ROW_LEFT + n * ROW_WIDTH / (len(BUYER_MB) - 1), BUYER_Y
            buyer_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.055, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(DEMAND).move_to([x, y, 0.025])
            orb = Sphere(radius=0.042, color=DEMAND, resolution=(12, 8)).move_to([x, y, 0.075])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.095, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(DEMAND)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = fixed(VMobject(color=DEMAND, stroke_width=1.4).set_points_as_corners([[-0.022, 0, 0], [-0.004, -0.02, 0], [0.03, 0.03, 0]]))
            check.price, check.value, check.visibility = price, value, show_buyers
            check.anchor, check.frame, check.dollar_height = bar, self.camera.frame, DOLLAR_HEIGHT
            check.add_updater(lambda m: m.move_to(screen_point(m.frame, m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10))).set_stroke(opacity=m.visibility.get_value() * float(m.value + 1e-7 >= m.price.get_value())).set_fill(opacity=0))
            circle = Circle(radius=0.056, color=GREEN, stroke_width=1.2).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            buyer_people.add(person)
            buyer_bars.add(bar)
            buyer_checks.add(check)
            buyer_circles.add(circle)
        for n, value in enumerate(SELLER_MC):
            x, y = ROW_LEFT + n * ROW_WIDTH / (len(SELLER_MC) - 1), SELLER_Y
            seller_positions.append(np.array([x, y, 0.045]))
            shadow = Disk3D(radius=0.037, resolution=(2, 16), shading=(0, 0, 0), opacity=0.28).set_color(SUPPLY).move_to([x, y, 0.025])
            orb = Sphere(radius=0.026, color=SUPPLY, resolution=(12, 8)).move_to([x, y, 0.055])
            person = Group(shadow, orb)
            bar = Rectangle3D(width=0.058, height=value * DOLLAR_HEIGHT, resolution=(2, 2), opacity=0.65).set_color(SUPPLY)
            bar.rotate(90 * DEGREES, RIGHT).move_to([x, y, BAR_BASE + value * DOLLAR_HEIGHT / 2])
            check = fixed(VMobject(color=SUPPLY, stroke_width=1.1).set_points_as_corners([[-0.015, 0, 0], [-0.003, -0.013, 0], [0.02, 0.02, 0]]))
            check.price, check.value, check.visibility = price, value, show_sellers
            check.anchor, check.frame, check.dollar_height = bar, self.camera.frame, DOLLAR_HEIGHT
            check.add_updater(lambda m: m.move_to(screen_point(m.frame, m.anchor.get_center() + OUT * (m.value * m.dollar_height / 2 + 0.10))).set_stroke(opacity=m.visibility.get_value() * float(m.value <= m.price.get_value() + 1e-7)).set_fill(opacity=0))
            circle = Circle(radius=0.035, color=GREEN, stroke_width=1.0).move_to([x, y, 0.045])
            circle.price, circle.rank, circle.visibility = price, n + 1, show_trades
            circle.mb, circle.mc = BUYER_MB, SELLER_MC
            circle.add_updater(lambda m: m.set_stroke(opacity=m.visibility.get_value() * float(m.rank <= min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).set_fill(opacity=0))
            seller_people.add(person)
            seller_bars.add(bar)
            seller_checks.add(check)
            seller_circles.add(circle)
        for y, row_prices in [(BUYER_Y, buyer_prices), (SELLER_Y, seller_prices)]:
            line = Line([ROW_LEFT - 0.06, y, BAR_BASE + 3*DOLLAR_HEIGHT], [ROW_LEFT + ROW_WIDTH + 0.06, y, BAR_BASE + 3*DOLLAR_HEIGHT], color=GUIDE, stroke_width=1.3)
            line.price, line.base, line.dollar_height = price, BAR_BASE, DOLLAR_HEIGHT
            line.add_updater(lambda m: m.set_z(m.base + m.dollar_height * m.price.get_value()))
            row_prices.add(line)
        buyer_label = fixed(fixed(Tex('Buyers: highest MB first', color=DEMAND)).scale(0.56).move_to([-3.3, 2.65, 0]))
        seller_label = fixed(fixed(Tex('Sellers: lowest MC first', color=SUPPLY)).scale(0.56).move_to([-3.3, -2.55, 0]))
        units = fixed(fixed(Tex(r'One person = 1,000 lb', color=CAPTION)).scale(0.50).move_to([-3.3, -2.90, 0]))
        buyers = Group(buyer_bars, buyer_people, buyer_prices, buyer_circles)
        sellers = Group(seller_bars, seller_people, seller_prices, seller_circles)
        crowd = Group(floor, rim, buyers, sellers)
        crowd_hud = fixed(VGroup(buyer_checks, seller_checks, buyer_label, seller_label))


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

        # The same exact ranked lots now share one graph, as in the graph bridge.
        ax = style_axes([0, 100, 20], [0, 13, 2], x_length=5.15, y_length=3.8)
        ax.move_to([4.48, 0.45, 0])
        ticks = VGroup()
        for q in [0, 20, 40, 60, 80, 100]:
            ticks.add(Tex(str(q), color=CAPTION).scale(0.40).next_to(ax.c2p(q, 0), DOWN, buff=0.10))
        for p in [4, 8, 12]:
            ticks.add(Tex(str(p), color=CAPTION).scale(0.40).next_to(ax.c2p(0, p), LEFT, buff=0.10))
        graph_units = Tex(r'$Q$: thousands of pounds', color=CAPTION).scale(0.48).move_to([4.48, -2.07, 0])
        demand_points, supply_points = [], []
        for n, value in enumerate(BUYER_MB):
            demand_points.extend([ax.c2p(n, value), ax.c2p(n + 1, value)])
        for n, value in enumerate(SELLER_MC):
            supply_points.extend([ax.c2p(n, value), ax.c2p(n + 1, value)])
        demand_steps = VMobject(color=DEMAND, stroke_width=2.4).set_points_as_corners(demand_points)
        supply_steps = VMobject(color=SUPPLY, stroke_width=2.4).set_points_as_corners(supply_points)
        demand_fit = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND).set_opacity(0.20)
        supply_fit = Line(ax.c2p(0, 2), ax.c2p(100, 7), color=SUPPLY).set_opacity(0.20)
        demand_word = Tex(r'$P_D=12-Q_d/5$', color=DEMAND).scale(0.54).move_to([3.35, 2.71, 0])
        supply_word = Tex(r'$P_S=2+Q_s/20$', color=SUPPLY).scale(0.54).move_to([5.85, 2.71, 0])
        graph = fixed(VGroup(ax, ticks, demand_fit, supply_fit, demand_steps, supply_steps,
                             graph_units, demand_word, supply_word))
        actual_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2.4))
        actual_line.axes, actual_line.price = ax, price
        # Update individual dashes so even a zero-quantity guide remains dashed.
        guide_start_x = actual_line.get_start()[0]
        guide_span = actual_line.get_end()[0] - guide_start_x
        for dash in actual_line:
            dash.first = (dash.get_start()[0] - guide_start_x) / guide_span
            dash.last = (dash.get_end()[0] - guide_start_x) / guide_span
            dash.axes, dash.level, dash.mb, dash.mc = ax, price, BUYER_MB, SELLER_MC
            dash.add_updater(lambda m: m.put_start_and_end_on(
                m.axes.c2p(m.first * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value()),
                m.axes.c2p(m.last * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value())))
        trade_guide = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GREEN, stroke_width=2))
        trade_guide.axes, trade_guide.price = ax, price
        trade_guide.mb, trade_guide.mc, trade_guide.visibility = BUYER_MB, SELLER_MC, show_counts
        trade_guide.add_updater(lambda m: m.put_start_and_end_on(
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
        for label, x, side, color in [('Q_d', 2.30, 'buyer', DEMAND), ('Q_s', 4.10, 'seller', SUPPLY), ('Q_x', 5.90, 'trade', GREEN)]:
            word = fixed(Tex(rf'${label}=$', color=color).scale(0.63).move_to([x, -2.62, 0]))
            number = fixed(Integer(40, color=color).scale(0.63).move_to([x + 0.77, -2.62, 0]))
            number.price, number.mb, number.mc, number.side, number.visibility = price, BUYER_MB, SELLER_MC, side, show_counts
            number.anchor = np.array([x + 0.77, -2.62, 0])
            number.add_updater(lambda m: m.set_value(int(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()) if m.side == 'buyer' else np.count_nonzero(m.mc <= m.price.get_value() + 1e-7) if m.side == 'seller' else min(np.count_nonzero(m.mb + 1e-7 >= m.price.get_value()), np.count_nonzero(m.mc <= m.price.get_value() + 1e-7)))).move_to(m.anchor).set_opacity(m.visibility.get_value()))
            counts.add(word, number)
        price_word = fixed(Tex(r'Actual price: \$', color=GUIDE).scale(0.55).move_to([-0.37, 2.96, 0]))
        price_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.55).move_to([0.85, 2.96, 0]))
        price_number.price = price
        price_number.add_updater(lambda m: m.set_value(m.price.get_value()).move_to([0.85, 2.96, 0]))
        price_units = fixed(Tex(r'/lb', color=CAPTION).scale(0.42).move_to([1.43, 2.96, 0]))
        price_readout = fixed(VGroup(price_word, price_number, price_units))

        # Dollar totals use only the selected whole lots, including the zero-gain 40th.
        totals = fixed(VGroup())
        for label, x, kind, color, initial in [('CS', -5.15, 'cs', DEMAND, 156000), ('PS', -1.75, 'ps', SUPPLY, 39000), ('TS', 1.70, 'ts', TOTAL, 195000), ('DWL', 5.2, 'dwl', MUTED, 0)]:
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
            totals.add(word, number)

        # ---- 6.a · Exact gains in the market just proved efficient.
        head = fixed(title('What changes when the price is controlled?'))
        caption = fixed(Tex('Each filled strip is the gain on one 1,000-lb trade.', color=INK).scale(0.74).move_to([0, -3.66, 0]))
        self.add(head, crowd, crowd_hud, cs_cells, ps_cells, loss_cells, graph, actual_line,
                 trade_guide, counts, price_readout, totals, caption)
        self.pause('6.a')

        # ---- 6.b · A legal maximum need not be the price people actually pay.
        ceiling.set_value(5)
        ceiling_line = fixed(DashedLine(ax.c2p(0, 5), ax.c2p(40, 5), color=DEFINITION, stroke_width=2.2))
        ceiling_line.axes, ceiling_line.limit = ax, ceiling
        guide_start_x = ceiling_line.get_start()[0]
        guide_span = ceiling_line.get_end()[0] - guide_start_x
        for dash in ceiling_line:
            dash.first = (dash.get_start()[0] - guide_start_x) / guide_span
            dash.last = (dash.get_end()[0] - guide_start_x) / guide_span
            dash.axes, dash.level, dash.mb, dash.mc = ax, ceiling, BUYER_MB, SELLER_MC
            dash.add_updater(lambda m: m.put_start_and_end_on(
                m.axes.c2p(m.first * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value()),
                m.axes.c2p(m.last * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value())))
        ceiling_word = fixed(Tex(r'Ceiling: \$', color=DEFINITION).scale(0.63).move_to([-4.25, 3.04, 0]))
        ceiling_number = fixed(DecimalNumber(5, num_decimal_places=2, color=DEFINITION).scale(0.63).move_to([-2.86, 3.04, 0]))
        ceiling_number.limit = ceiling
        ceiling_number.add_updater(lambda m: m.set_value(m.limit.get_value()).move_to([-2.86, 3.04, 0]))
        ceiling_readout = fixed(VGroup(ceiling_word, ceiling_number))
        nonbinding = fixed(Tex(r'A $\$5$ ceiling allows the $\$4$ equilibrium price.', color=INK).scale(0.77).move_to([0, -3.66, 0]))
        self.play(FadeIn(ceiling_line), FadeIn(ceiling_readout), ReplacementTransform(caption, nonbinding))
        self.pause('6.b')

        # ---- 6.c · Ask before the counts, trading circles and areas return.
        self.play(show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0),
                  show_sellers.animate.set_value(0), show_welfare.animate.set_value(0), show_totals.animate.set_value(0))
        self.play(ceiling.animate.set_value(3), run_time=2.0, rate_func=linear)
        prediction = fixed(Tex('At the legal maximum, who is willing? How much is exchanged?', color=DEFINITION).scale(0.73).move_to([0, -3.66, 0]))
        self.play(ReplacementTransform(nonbinding, prediction))
        self.pause('6.c')
        self.play(show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1))
        ag_ring = Circle(radius=0.075, color=FOCUS, stroke_width=2).move_to(buyer_positions[24])
        illegal_bid = DashedLine(buyer_positions[24], seller_positions[0], color=GUIDE, stroke_width=2)
        blocked_at = (buyer_positions[24] + seller_positions[0]) / 2
        blocked = VGroup(Line(blocked_at + [-0.13, -0.13, 0], blocked_at + [0.13, 0.13, 0], color=GUIDE, stroke_width=4),
                         Line(blocked_at + [-0.13, 0.13, 0], blocked_at + [0.13, -0.13, 0], color=GUIDE, stroke_width=4))
        blocked_caption = fixed(Tex(r'Amanda-Grace wants to offer $\$3.25$. The $\$3$ ceiling forbids it.', color=INK).scale(0.70).move_to([0, -3.66, 0]))
        rationing = fixed(Tex('Assume the highest-MB buyers and lowest-MC sellers trade.', color=CAPTION).scale(0.52).move_to([-3.50, -2.87, 0]))
        self.play(Create(ag_ring), Create(illegal_bid), Create(blocked), FadeIn(rationing), ReplacementTransform(prediction, blocked_caption))
        self.pause('6.c.blocked')

        # ---- 6.d · The missing gains are exact pairs 21--39. Pair 40 adds zero.
        self.play(FadeOut(ag_ring), FadeOut(illegal_bid), FadeOut(blocked), show_welfare.animate.set_value(1), show_loss.animate.set_value(1))
        zero_pair = fixed(Circle(radius=0.10, color=MUTED, stroke_width=2).move_to(ax.c2p(40, 4)))
        lost_caption = fixed(Tex('Deadweight loss: total surplus lost from missing beneficial trades.', color=INK).scale(0.72).move_to([0, -3.66, 0]))
        self.play(Create(zero_pair), ReplacementTransform(blocked_caption, lost_caption))
        self.pause('6.d')

        # ---- 6.e · Sum the crowd's rectangles, with no continuous approximation.
        self.play(loss_fill.animate.set_value(1), show_totals.animate.set_value(1))
        ceiling_result = fixed(Tex(r'20,000 lb traded. Lost gains: $\$47{,}500$.', color=INK).scale(0.78).move_to([0, -3.66, 0]))
        self.play(ReplacementTransform(lost_caption, ceiling_result))
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
        floor_line = fixed(DashedLine(ax.c2p(0, 3), ax.c2p(40, 3), color=DEFINITION, stroke_width=2.2))
        floor_line.axes, floor_line.limit = ax, floor_limit
        guide_start_x = floor_line.get_start()[0]
        guide_span = floor_line.get_end()[0] - guide_start_x
        for dash in floor_line:
            dash.first = (dash.get_start()[0] - guide_start_x) / guide_span
            dash.last = (dash.get_end()[0] - guide_start_x) / guide_span
            dash.axes, dash.level, dash.mb, dash.mc = ax, floor_limit, BUYER_MB, SELLER_MC
            dash.add_updater(lambda m: m.put_start_and_end_on(
                m.axes.c2p(m.first * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value()),
                m.axes.c2p(m.last * min(np.count_nonzero(m.mb + 1e-7 >= m.level.get_value()), np.count_nonzero(m.mc <= m.level.get_value() + 1e-7)), m.level.get_value())))
        floor_word = fixed(Tex(r'Floor: \$', color=DEFINITION).scale(0.63).move_to([-4.25, 3.04, 0]))
        floor_number = fixed(DecimalNumber(3, num_decimal_places=2, color=DEFINITION).scale(0.63).move_to([-2.86, 3.04, 0]))
        floor_number.limit = floor_limit
        floor_number.add_updater(lambda m: m.set_value(m.limit.get_value()).move_to([-2.86, 3.04, 0]))
        floor_readout = fixed(VGroup(floor_word, floor_number))
        floor_nonbinding = fixed(Tex(r'A $\$3$ floor allows the $\$4$ equilibrium price.', color=INK).scale(0.77).move_to([0, -3.66, 0]))
        self.play(FadeIn(floor_line), FadeIn(floor_readout), ReplacementTransform(ceiling_result, floor_nonbinding))
        self.pause('6.f.nonbinding')
        self.play(show_counts.animate.set_value(0), show_trades.animate.set_value(0), show_buyers.animate.set_value(0),
                  show_sellers.animate.set_value(0), show_welfare.animate.set_value(0), show_totals.animate.set_value(0))
        self.play(floor_limit.animate.set_value(6), run_time=2.0, rate_func=linear)
        floor_question = fixed(Tex('At the legal minimum, who is willing? How much is exchanged?', color=DEFINITION).scale(0.73).move_to([0, -3.66, 0]))
        self.play(ReplacementTransform(floor_nonbinding, floor_question))
        self.pause('6.f')

        # ---- 6.g · The incentive to undercut remains, but the legal bid cannot.
        self.play(show_counts.animate.set_value(1), show_trades.animate.set_value(1), show_buyers.animate.set_value(1), show_sellers.animate.set_value(1), show_welfare.animate.set_value(1))
        andrew_ring = Circle(radius=0.05, color=FOCUS, stroke_width=2).move_to(seller_positions[39])
        illegal_cut = DashedLine(seller_positions[39], buyer_positions[29], color=GUIDE, stroke_width=2)
        blocked_at = (seller_positions[39] + buyer_positions[29]) / 2
        blocked_cut = VGroup(Line(blocked_at + [-0.13, -0.13, 0], blocked_at + [0.13, 0.13, 0], color=GUIDE, stroke_width=4),
                             Line(blocked_at + [-0.13, 0.13, 0], blocked_at + [0.13, -0.13, 0], color=GUIDE, stroke_width=4))
        cut_caption = fixed(Tex(r'Andrew wants to ask $\$5.75$. The $\$6$ floor forbids it.', color=INK).scale(0.73).move_to([0, -3.66, 0]))
        no_purchases = fixed(Tex('No government purchases. Highest MB and lowest MC trade.', color=CAPTION).scale(0.52).move_to([-3.50, -2.87, 0]))
        self.play(Create(andrew_ring), Create(illegal_cut), Create(blocked_cut), FadeIn(no_purchases), ReplacementTransform(floor_question, cut_caption))
        self.pause('6.g')

        # ---- 6.h · The efficient missing pairs are now 31--39, plus zero pair 40.
        self.play(FadeOut(andrew_ring), FadeOut(illegal_cut), FadeOut(blocked_cut), show_loss.animate.set_value(1), show_totals.animate.set_value(1))
        floor_result = fixed(Tex(r'30,000 lb traded. Lost gains: $\$11{,}250$.', color=INK).scale(0.78).move_to([0, -3.66, 0]))
        self.play(ReplacementTransform(cut_caption, floor_result))
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
        self.play(ReplacementTransform(head, closing_head), ReplacementTransform(floor_result, closing))
        self.pause('7.a')
