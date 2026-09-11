# maniml part_b.py OneAgent
#
# Part B | A small market, built from individual decisions.
# Run OneAgent, OneTrade, MarketRound, or PolicyComparison.
# Each scene has one flat construct(), with literal pausepoints like A1–A3/B0.
# README.md describes the scene pieces; market_model.py contains the economics.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.dirname(__file__))
from style import *
from style import axes as style_axes
from market_model import Buyer, Seller, clear_market, efficient_quantity
from scene_layers import fixed, add_market_objects, camera_home, screen_point, attached_label


# All prices/values are dollars for one unit. Coordinates only arrange the view.
BUYERS = (Buyer('B1', 12), Buyer('B2', 10), Buyer('B3', 8), Buyer('B4', 6))
SELLERS = (Seller('S1', 2), Seller('S2', 4), Seller('S3', 7), Seller('S4', 9))
PRICE = 7.5
CEILING = 5
TAX = 3
DAMAGE = 3
TAX_BUYER_PRICE = 8.5

FLOOR_AT = np.array([-3.8, -0.35, 0])
BUYER_X, SELLER_X = -6.2, -1.5
ROWS = [1.7, 0.2, -1.3, -2.8]
MODEL_AT = RIGHT * 4.2 + DOWN * 0.2
BOTTOM_Y = -3.35


class Agent:
    """A colored token in the world, with an independent screen-facing label.

    Move body; label follows. An Agent carries no trading logic or money.
    """

    def __init__(self, scene, text, color, at):
        base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0)).set_color(color)
        head = Sphere(radius=0.16, color=color, resolution=(16, 9)).shift(OUT * 0.18)
        self.body = Group(base, head).move_to(np.array(at) + OUT * 0.18)
        self.label = attached_label(scene, self.body, text)


def market_floor():
    """A neutral plane; its coordinates do not represent price or quantity."""
    plane = Rectangle3D(width=7.5, height=5.8, color=MUTED,
                        opacity=0.18, resolution=(2, 2)).move_to(FLOOR_AT)
    edges = Rectangle(width=7.5, height=5.8, color=MUTED,
                      stroke_width=1.5).move_to(FLOOR_AT + OUT * 0.01)
    lanes = VGroup(*[
        Line([BUYER_X - 0.7, y, 0.02], [SELLER_X + 0.7, y, 0.02],
             color=MUTED, stroke_width=1).set_stroke(opacity=0.4)
        for y in ROWS
    ])
    return Group(plane, edges, lanes)


def heading(text, detail):
    head = fixed(title(text))
    sub = fixed(subtitle(head, detail))
    return head, sub


def bottom(text, color=DEFINITION):
    return fixed(Tex(text).scale(SCALE_CAPTION).set_color(color)
                 .move_to(UP * BOTTOM_Y))


def number_row(label, tracker, color=INK, at=ORIGIN, decimals=2):
    """Only the number rolls; the words and its right edge stay in place."""
    words = Tex(label).scale(SCALE_CAPTION).set_color(color)
    number = DecimalNumber(tracker.get_value(), num_decimal_places=decimals,
                           color=INK).scale(SCALE_CAPTION)
    row = fixed(VGroup(words, number).arrange(RIGHT, buff=0.25).move_to(at))
    number.tracker = tracker
    number.right_at = number.get_right().copy()

    def roll(mob):
        mob.set_value(mob.tracker.get_value())
        mob.move_to(mob.right_at, aligned_edge=RIGHT)
        fixed(mob)     # new numeral glyphs inherit the screen layer too

    number.add_updater(roll)
    return row


def level(ax, value, label, color, x_end=1):
    line = Line(ax.c2p(0, value), ax.c2p(x_end, value), color=color, stroke_width=3)
    text = Tex(label).scale(SCALE_TICK).set_color(INK).next_to(line, RIGHT, buff=0.15)
    return fixed(VGroup(line, text))


def gain_bar(ax, low, high, x0, x1, color):
    """A rectangle measured in the model's dollars, never in world coordinates."""
    return fixed(Polygon(ax.c2p(x0, low), ax.c2p(x1, low),
                         ax.c2p(x1, high), ax.c2p(x0, high),
                         fill_color=color, fill_opacity=AREA_OPACITY, stroke_width=0))


def decision_axes():
    ax = style_axes(x_range=[0, 1, 1], y_range=[0, 12, 2],
                    x_length=2.2, y_length=4.1).move_to(RIGHT * 3.7 + DOWN * 0.2)
    cap = Tex(narration('Dollars per unit')).scale(SCALE_CAPTION).set_color(CAPTION)
    cap.next_to(ax.y_axis, UP, buff=0.2)
    return fixed(ax), fixed(cap)


def market_agents(scene):
    buyers = {b.id: Agent(scene, rf'{b.id}: \${b.value:g}', DEMAND,
                          [BUYER_X, y, 0]) for b, y in zip(BUYERS, ROWS)}
    sellers = {s.id: Agent(scene, rf'{s.id}: \${s.cost:g}', SUPPLY,
                           [SELLER_X, y, 0]) for s, y in zip(SELLERS, ROWS)}
    labels = fixed(VGroup(
        Tex('Buyers: WTP').scale(SCALE_TICK).set_color(DEMAND).move_to(LEFT * 5.8 + UP * 2),
        Tex('Sellers: cost').scale(SCALE_TICK).set_color(SUPPLY).move_to(LEFT * 1.5 + UP * 2)))
    return buyers, sellers, labels


def step_curve(ax, values, color):
    points = []
    for i, value in enumerate(values):
        points.extend([ax.c2p(i, value), ax.c2p(i + 1, value)])
    return fixed(VMobject(stroke_color=color, stroke_width=4).set_points_as_corners(points))


class MarketGraph:
    """The same marginal units, sorted into flat demand and supply steps."""

    def __init__(self):
        self.ax = style_axes(x_range=[0, 4, 1], y_range=[0, 14, 2],
                             x_length=4.3, y_length=4.1).move_to(MODEL_AT)
        values = sorted([b.value for b in BUYERS], reverse=True)
        costs = sorted([s.cost for s in SELLERS])
        self.demand = step_curve(self.ax, values, DEMAND)
        self.supply = step_curve(self.ax, costs, SUPPLY)
        caps = VGroup(
            Tex(narration('Dollars / unit')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(self.ax.y_axis, UP, buff=0.2),
            Tex(narration('Units')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(self.ax.c2p(4, 0), RIGHT, buff=0.18),
            Tex('D').scale(SCALE_TICK).set_color(INK)
                .next_to(self.ax.c2p(4, values[-1]), RIGHT, buff=0.15),
            Tex('S').scale(SCALE_TICK).set_color(INK)
                .next_to(self.ax.c2p(4, costs[-1]), RIGHT, buff=0.15))
        ticks = VGroup(*[Tex(str(i)).scale(SCALE_TICK).set_color(MUTED)
                        .next_to(self.ax.c2p(i, 0), DOWN, buff=0.1) for i in range(1, 5)])
        ticks.add(*[Tex(str(p)).scale(SCALE_TICK).set_color(MUTED)
                    .next_to(self.ax.c2p(0, p), LEFT, buff=0.13) for p in [0, 4, 8, 12]])
        self.group = fixed(VGroup(self.ax, caps, ticks, self.demand, self.supply))

    def price_line(self, price):
        line = DashedLine(self.ax.c2p(0, price), self.ax.c2p(4, price),
                          color=GUIDE, stroke_width=2)
        return fixed(line)

    def trade_area(self, trade, index):
        return fixed(VGroup(
            gain_bar(self.ax, trade.buyer_price, trade.value, index, index + 1, DEMAND),
            gain_bar(self.ax, trade.cost, trade.seller_price, index, index + 1, SUPPLY)))


class OneAgent(ThreeDScene):
    """A world token, an attached WTP label, and a fixed decision model."""
    add = add_market_objects

    def construct(self):
        # ---- 1.a | One person and one marginal value
        camera_home(self)
        head, sub = heading('One buyer', r'One unit. A willingness to pay of \$10.')
        floor = market_floor()
        buyer = Agent(self, r'Buyer | WTP \$10', DEMAND, [-4.5, 0, 0])
        self.play(FadeIn(head), FadeIn(sub), FadeIn(floor))
        self.play(FadeIn(buyer.body), FadeIn(buyer.label))
        self.pause('1.a')

        # ---- 1.b | A label belongs to a person, not to a screen position
        self.play(buyer.body.animate.shift(RIGHT * 1.8 + DOWN * 0.6), run_time=2)
        self.pause('1.b')

        # ---- 1.c | The same value, in a flat model
        ax, cap = decision_axes()
        value = level(ax, 10, r'WTP = \$10', DEMAND)
        self.play(FadeIn(ax), FadeIn(cap), FadeIn(value))
        self.pause('1.c')

        # ---- 1.d | Price can change while value stays fixed
        price = ValueTracker(12)
        price_row = number_row(r'Price: \$', price, at=RIGHT * 4.25 + DOWN * 2.8)
        price_line = fixed(Line(ax.c2p(0, 12), ax.c2p(1, 12), color=GUIDE))
        price_line.tracker, price_line.axes = price, ax
        price_line.add_updater(lambda m: m.set_points_as_corners([
            m.axes.c2p(0, m.tracker.get_value()), m.axes.c2p(1, m.tracker.get_value())]))
        decision = bottom('At this price, the buyer declines.')
        self.play(FadeIn(price_row), FadeIn(price_line), Write(decision))
        self.pause('1.d')

        # ---- 1.e | The gap is a potential gain, before any trade occurs
        self.play(price.animate.set_value(6), FadeOut(decision), run_time=3)
        gain = gain_bar(ax, 6, 10, 0.2, 0.75, DEMAND)
        gain_text = fixed(Tex(r'Potential gain: \$4').scale(SCALE_CAPTION)
                          .set_color(DEMAND).move_to(LEFT * 3.6 + DOWN * 2.6))
        decision = bottom('The price changed. Willingness to pay did not.')
        self.play(FadeIn(gain), Write(gain_text), Write(decision))
        self.pause('1.e')


class OneTrade(ThreeDScene):
    """Approach, settle one exchange, and account for its two gains."""
    add = add_market_objects

    def construct(self):
        # ---- 1.a | Value, price, and cost are different quantities
        camera_home(self)
        head, sub = heading('One exchange', r'One unit is offered at a price of \$6.')
        floor = market_floor()
        buyer = Agent(self, r'Buyer | WTP \$10', DEMAND, [-5.7, -0.2, 0])
        seller = Agent(self, r'Seller | cost \$4', SUPPLY, [-1.6, -0.2, 0])
        ax, cap = decision_axes()
        value = level(ax, 10, r'WTP = \$10', DEMAND)
        cost = level(ax, 4, r'Cost = \$4', SUPPLY)
        price = level(ax, 6, r'Price = \$6', GUIDE)
        self.play(FadeIn(head), FadeIn(sub), FadeIn(floor))
        self.play(FadeIn(buyer.body), FadeIn(seller.body),
                  FadeIn(buyer.label), FadeIn(seller.label),
                  FadeIn(ax), FadeIn(cap), FadeIn(value), FadeIn(cost), FadeIn(price))
        self.pause('1.a')

        # ---- 1.b | A visit alone does not count as an exchange
        approach = seller.body.get_center() + LEFT * 1.8
        self.play(buyer.body.animate.move_to(approach), run_time=2.5)
        agreement = bottom('Both are willing to exchange at this price.')
        self.play(Write(agreement))
        self.pause('1.b')

        # ---- 1.c | Settlement: one good goes to the buyer, payment to the seller
        result = clear_market((Buyer('B1', 10),), (Seller('S1', 4),), 6)
        trade = result.trades[0]
        buyer_at = screen_point(self.camera.frame, buyer.body.get_center())
        seller_at = screen_point(self.camera.frame, seller.body.get_center())
        good = fixed(Tex('1 unit').scale(SCALE_TICK).set_color(INK)
                     .move_to(seller_at + DOWN * 0.5))
        money = fixed(Tex(r'\$6').scale(SCALE_TICK).set_color(GUIDE)
                      .move_to(buyer_at + DOWN * 0.9))
        self.play(FadeIn(good), FadeIn(money), FadeOut(agreement))
        self.play(good.animate.move_to(buyer_at + DOWN * 0.5),
                  money.animate.move_to(seller_at + DOWN * 0.9), run_time=2)
        self.play(FadeOut(good), FadeOut(money))
        self.pause('1.c')

        # ---- 1.d | The completed trade produces consumer and producer surplus
        cs = gain_bar(ax, trade.buyer_price, trade.value, 0.1, 0.8, DEMAND)
        ps = gain_bar(ax, trade.cost, trade.seller_price, 0.1, 0.8, SUPPLY)
        gains = fixed(VGroup(
            Tex(rf'CS = 10 - 6 = \${result.consumer_surplus:g}').set_color(DEMAND),
            Tex(rf'PS = 6 - 4 = \${result.producer_surplus:g}').set_color(SUPPLY))
            .arrange(DOWN, buff=0.3).scale(SCALE_CAPTION).move_to(LEFT * 3.9 + DOWN * 2.4))
        total = bottom(r'Total gains: $10 - 4 = 6$. The price divides those gains.')
        self.play(FadeIn(cs), FadeIn(ps), Write(gains), Write(total))
        self.pause('1.d')


class MarketRound(ThreeDScene):
    """Four buyers and four sellers; a competitive allocation at a given price."""
    add = add_market_objects

    def construct(self):
        # ---- 1.a | Same world, several one-unit decisions
        camera_home(self)
        head, sub = heading('A market round', 'Each buyer and seller can trade one unit.')
        floor = market_floor()
        buyers, sellers, roles = market_agents(self)
        agents = list(buyers.values()) + list(sellers.values())
        graph = MarketGraph()
        result = clear_market(BUYERS, SELLERS, PRICE)
        self.play(FadeIn(head), FadeIn(sub), FadeIn(floor))
        self.play(*[FadeIn(a.body) for a in agents],
                  *[FadeIn(a.label) for a in agents], FadeIn(roles))
        self.pause('1.a')

        # ---- 1.b | Individual values and costs become demand and supply
        self.play(FadeIn(graph.group))
        price_line = graph.price_line(PRICE)
        price_text = fixed(Tex(rf'Posted price: \${PRICE:.2f}').scale(SCALE_CAPTION)
                           .set_color(INK).move_to(LEFT * 3.7 + DOWN * 2.8))
        rule = bottom('A common price; highest values and lowest costs trade first.')
        self.play(Create(price_line), Write(price_text), Write(rule))
        self.pause('1.b')

        # ---- 1.c | Watch the first visit and settlement
        quantity, cs_total, ps_total = ValueTracker(0), ValueTracker(0), ValueTracker(0)
        ledger = fixed(VGroup(
            number_row('Trades:', quantity, decimals=0),
            number_row(r'CS: \$', cs_total, DEMAND),
            number_row(r'PS: \$', ps_total, SUPPLY))
            .arrange(RIGHT, buff=0.55).move_to(RIGHT * 3.7 + DOWN * 2.85))
        # Re-anchor numerals after arranging the whole ledger.
        for row in ledger:
            row[1].right_at = row[1].get_right().copy()
        self.play(FadeIn(ledger), FadeOut(rule))
        if result.trades:
            first = result.trades[0]
            self.play(buyers[first.buyer_id].body.animate.move_to(
                sellers[first.seller_id].body.get_center() + LEFT * 1.8), run_time=2.5)
            area = graph.trade_area(first, 0)
            self.play(FadeIn(area), quantity.animate.set_value(1),
                      cs_total.animate.set_value(first.value - first.buyer_price),
                      ps_total.animate.set_value(first.seller_price - first.cost))
        self.pause('1.c')

        # ---- 1.d | Remaining visits; a ledger counts each exchange once
        for index, trade in enumerate(result.trades[1:], start=1):
            self.play(buyers[trade.buyer_id].body.animate.move_to(
                sellers[trade.seller_id].body.get_center() + LEFT * 1.8), run_time=1.5)
            area = graph.trade_area(trade, index)
            self.play(FadeIn(area), quantity.animate.set_value(index + 1),
                      cs_total.animate.set_value(cs_total.get_value() + trade.value - trade.buyer_price),
                      ps_total.animate.set_value(ps_total.get_value() + trade.seller_price - trade.cost))
        self.pause('1.d')

        # ---- 1.e | Nontraders stay visible; quantity and allocation both matter
        conclusion = bottom(rf'{result.quantity} exchanges. Total gains: \${result.total_welfare:g}. Nontraders remain visible.')
        self.play(Write(conclusion))
        self.pause('1.e')


class PolicyComparison(ThreeDScene):
    """Replay one population: baseline, ceiling, external damage, corrective tax."""
    add = add_market_objects

    def construct(self):
        # ---- 1.a | The population is held fixed across cases
        camera_home(self)
        head, sub = heading('The same market, different rules', 'Four buyers. Four sellers. One unit each.')
        floor = market_floor()
        buyers, sellers, roles = market_agents(self)
        agents = list(buyers.values()) + list(sellers.values())
        home = {key: a.body.get_center().copy() for key, a in buyers.items()}
        q, cs, ps, gov, damage, welfare = [ValueTracker(0) for _ in range(6)]
        rows = [number_row(label, tracker, color, decimals=decimals) for label, tracker, color, decimals in [
            ('Trades:', q, INK, 0), (r'CS: \$', cs, DEMAND, 2),
            (r'PS: \$', ps, SUPPLY, 2), (r'Government: \$', gov, GOV, 2),
            (r'External damage: \$', damage, EXT, 2), (r'Social gains: \$', welfare, TOTAL, 2)]]
        ledger = fixed(VGroup(*rows).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
                       .move_to(RIGHT * 4 + DOWN * 0.35))
        for row in rows:
            row[1].right_at = row[1].get_right().copy()
        self.play(FadeIn(head), FadeIn(sub), FadeIn(floor))
        self.play(*[FadeIn(a.body) for a in agents],
                  *[FadeIn(a.label) for a in agents], FadeIn(roles), FadeIn(ledger))
        self.pause('1.a')

        # ---- 1.b | Given competitive price; three trades
        baseline = clear_market(BUYERS, SELLERS, PRICE)
        case = fixed(Tex(rf'Price: \${PRICE:.2f}').scale(SCALE_CAPTION).set_color(INK)
                     .move_to(RIGHT * 4 + UP * 2.2))
        self.play(Write(case))
        self.play(*[buyers[t.buyer_id].body.animate.move_to(
            sellers[t.seller_id].body.get_center() + LEFT * 1.8) for t in baseline.trades], run_time=2)
        self.play(q.animate.set_value(baseline.quantity), cs.animate.set_value(baseline.consumer_surplus),
                  ps.animate.set_value(baseline.producer_surplus), welfare.animate.set_value(baseline.total_welfare))
        note = bottom(rf'Baseline: {baseline.quantity} exchanges, with total gains of \${baseline.total_welfare:g}.')
        self.play(Write(note))
        self.pause('1.b')

        # ---- 2.a | Fresh period, same values and costs; impose a ceiling
        ceiling = clear_market(BUYERS, SELLERS, CEILING, price_ceiling=CEILING)
        self.play(*[a.body.animate.move_to(home[key]) for key, a in buyers.items()],
                  q.animate.set_value(0), cs.animate.set_value(0), ps.animate.set_value(0),
                  welfare.animate.set_value(0), FadeOut(note), FadeOut(case), run_time=1.5)
        case = fixed(Tex(rf'Price ceiling: \${CEILING:g}').scale(SCALE_CAPTION).set_color(INK)
                     .move_to(RIGHT * 4 + UP * 2.2))
        note = bottom(f'{len(ceiling.willing_buyers)} willing buyers; {len(ceiling.willing_sellers)} willing sellers. Highest WTP receives priority.')
        self.play(Write(case), Write(note))
        self.pause('2.a')

        # ---- 2.b | Only two units exchange under this allocation rule
        self.play(*[buyers[t.buyer_id].body.animate.move_to(
            sellers[t.seller_id].body.get_center() + LEFT * 1.8) for t in ceiling.trades], run_time=2)
        self.play(q.animate.set_value(ceiling.quantity), cs.animate.set_value(ceiling.consumer_surplus),
                  ps.animate.set_value(ceiling.producer_surplus), welfare.animate.set_value(ceiling.total_welfare))
        self.pause('2.b')

        # ---- 3.a | Remove the ceiling. Add someone outside the exchange.
        private = clear_market(BUYERS, SELLERS, PRICE, external_cost=DAMAGE)
        self.play(*[a.body.animate.move_to(home[key]) for key, a in buyers.items()],
                  q.animate.set_value(0), cs.animate.set_value(0), ps.animate.set_value(0),
                  welfare.animate.set_value(0), FadeOut(note), FadeOut(case), run_time=1.5)
        bystander = Agent(self, 'Bystander', EXT, [0.1, -3.5, 0])
        case = fixed(Tex(rf'Price: \${PRICE:.2f}').scale(SCALE_CAPTION).set_color(INK)
                     .move_to(RIGHT * 4 + UP * 2.2))
        note = bottom(rf'Each exchange now imposes \${DAMAGE:g} of damage on someone else.')
        self.play(FadeIn(bystander.body), FadeIn(bystander.label), Write(case), Write(note))
        self.pause('3.a')

        # ---- 3.b | Private gains still motivate three trades; social gains differ
        self.play(*[buyers[t.buyer_id].body.animate.move_to(
            sellers[t.seller_id].body.get_center() + LEFT * 1.8) for t in private.trades], run_time=2)
        spillovers = VGroup(*[Line(sellers[t.seller_id].body.get_center(),
                                  bystander.body.get_center(), color=EXT, stroke_width=2)
                              for t in private.trades])
        self.play(Create(spillovers), q.animate.set_value(private.quantity),
                  cs.animate.set_value(private.consumer_surplus), ps.animate.set_value(private.producer_surplus),
                  damage.animate.set_value(private.external_damage), welfare.animate.set_value(private.total_welfare))
        self.pause('3.b')

        # ---- 4.a | Fresh period: a tax equal to marginal external damage
        taxed = clear_market(BUYERS, SELLERS, TAX_BUYER_PRICE, TAX_BUYER_PRICE - TAX,
                             external_cost=DAMAGE)
        self.play(*[a.body.animate.move_to(home[key]) for key, a in buyers.items()],
                  q.animate.set_value(0), cs.animate.set_value(0), ps.animate.set_value(0),
                  damage.animate.set_value(0), welfare.animate.set_value(0),
                  FadeOut(spillovers), FadeOut(note), FadeOut(case), run_time=1.5)
        case = fixed(VGroup(Tex(rf'Buyer pays: \${TAX_BUYER_PRICE:.2f}'),
                            Tex(rf'Seller receives: \${TAX_BUYER_PRICE - TAX:.2f}'))
                     .arrange(DOWN, buff=0.2).scale(SCALE_CAPTION).set_color(INK)
                     .move_to(RIGHT * 4 + UP * 2.2))
        note = bottom(rf'A \${TAX:g} tax changes which exchanges are privately worthwhile.')
        self.play(Write(case), Write(note))
        self.pause('4.a')

        # ---- 4.b | Government receipts are a transfer; remaining damage persists
        self.play(*[buyers[t.buyer_id].body.animate.move_to(
            sellers[t.seller_id].body.get_center() + LEFT * 1.8) for t in taxed.trades], run_time=2)
        spillovers = VGroup(*[Line(sellers[t.seller_id].body.get_center(),
                                  bystander.body.get_center(), color=EXT, stroke_width=2)
                              for t in taxed.trades])
        self.play(Create(spillovers), q.animate.set_value(taxed.quantity),
                  cs.animate.set_value(taxed.consumer_surplus), ps.animate.set_value(taxed.producer_surplus),
                  gov.animate.set_value(taxed.government_revenue), damage.animate.set_value(taxed.external_damage),
                  welfare.animate.set_value(taxed.total_welfare), FadeOut(note))
        efficient = efficient_quantity([b.value for b in BUYERS], [s.cost for s in SELLERS], DAMAGE)
        note = bottom(rf'{efficient} socially efficient trades. Damage: \${taxed.external_damage:g}. Social gains: \${taxed.total_welfare:g}.')
        self.play(Write(note))
        self.pause('4.b')
