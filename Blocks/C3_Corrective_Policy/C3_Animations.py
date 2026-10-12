# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-02T23:47:58Z"
# ///

# maniml C3_Animations.py C3
# Storyboard: C3_Notes.md. All lesson choreography stays in construct().
# C1's market, Q in units and dollars per unit, joined to the tax wedge of the old C2 Taxes animation:
# the wedge slides in from the left until it is stuck between MC and MB at the efficient quantity.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects


class C3(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        EXTERNAL, MARKET_Q, MARKET_P = 2, 40, 4
        EFFICIENT_Q, POSITIVE_Q = 32, 48            # MB = MSC at 32; MSB = MC at 48.
        STOPPED_UNIT, KEPT_UNIT = 36, 24              # Close-ups: one exchange the tax stops, one it keeps.
        BAR_GAP = 0.08
        BASE_OPACITY, SURPLUS_OPACITY, GOV_OPACITY = 0.16, 0.65, 0.65
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.55
        BUYER_LEFT, SELLER_LEFT, BAR_WIDTH = -1.76, 0.66, 1.1
        TAX_LEFT, TAX_WIDTH = -0.40, 0.80
        detail_y = lambda value: DETAIL_BASE + DETAIL_SCALE * value
        ORIGIN_X, ORIGIN_Y = -3.2, -2.15
        DOT_LAYER = 30

        # The model, as one-line functions of quantity or price.
        mb = lambda q: 12 - q / 5
        mc = lambda q: 2 + q / 20
        msc = lambda q: mc(q) + EXTERNAL
        msb = lambda q: mb(q) + EXTERNAL
        zero = lambda q: 0
        quantity_demanded = lambda p: (12 - p) * 5
        quantity_supplied = lambda p: (p - 2) * 20
        taxed_quantity = lambda t: 40 - 4 * t       # MB - MC = t  ->  10 - Q/4 = t.

        # The two object factories used throughout: the yellow bottom line and one one-unit slice.
        teaching = lambda text: fixed(Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                      .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))

        def unit_slice(axes, q, low, high, color, opacity, right=None, left=None):
            left = q + BAR_GAP / 2 if left is None else left
            right = q + 1 - BAR_GAP / 2 if right is None else right
            return fixed(Polygon(axes.c2p(left, low(left)), axes.c2p(right, low(right)),
                                 axes.c2p(right, high(right)), axes.c2p(left, high(left)),
                                 stroke_width=0, fill_color=color, fill_opacity=opacity))

        # ---- 0.a · The shared bumper, with C3's thesis from the notes header.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'C', 3)
        thesis = Tex(r'\textit{We can offset the problems of externalities with the problems of taxes.}',
                     color=CAPTION).scale(0.9).next_to(episode, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · Last time: the negative-externality market and its deadweight loss.
        head = fixed(title('Negative Externalities'))
        context = fixed(subtitle(head, 'A cost paid by others outside the market.'))
        ax = style_axes([0, 80, 10], [0, 13, 2], x_length=6.4, y_length=4.6)
        ax.shift(np.array([ORIGIN_X, ORIGIN_Y, 0]) - ax.c2p(0, 0))
        fixed(ax)
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(80, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(80, 0), DOWN, buff=0.73),
            Tex('$2$', color=SUPPLY).scale(0.65).next_to(ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('$12$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, 12), LEFT, buff=0.15)))
        # The MSC intercept shares the market-price level; it leaves when P_s needs the axis.
        msc_intercept = fixed(Tex('$4$', color=SUPPLY).scale(0.65).next_to(ax.c2p(0, 4), LEFT, buff=0.15))
        demand = fixed(Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        supply = fixed(Line(ax.c2p(0, 2), ax.c2p(80, 6), color=SUPPLY, stroke_width=3))
        social_cost = fixed(Line(ax.c2p(0, 4), ax.c2p(80, 8), color=SUPPLY, stroke_width=3))
        curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(ax.c2p(7, 10.6), UR, buff=0.12),
            Tex('MC', color=INK).scale(0.7).next_to(ax.c2p(80, 6), RIGHT, buff=0.12),
            Tex('MSC', color=INK).scale(0.7).next_to(ax.c2p(80, 8), RIGHT, buff=0.12)))
        benefit_bars, cost_bars, ext_bars = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            benefit_bars.add(unit_slice(ax, q, zero, mb, DEMAND, BASE_OPACITY))
            cost_bars.add(unit_slice(ax, q, zero, mc, SUPPLY, BASE_OPACITY))
        for q in range(60):
            ext_bars.add(unit_slice(ax, q, mc, msc, EXT, BASE_OPACITY if q < MARKET_Q else 0))
        market_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        market_quantity = fixed(VGroup(
            DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            VGroup(Tex(r'$\hat{Q}$', color=GUIDE), Tex('40', color=GUIDE)).arrange(DOWN, buff=0.08).scale(0.64).next_to(ax.c2p(40, 0), DOWN, buff=0.20)).set_z_index(10))
        market_price = fixed(VGroup(
            Tex(r'$\hat{P}=$', color=GUIDE).scale(0.7).next_to(msc_intercept, LEFT, buff=0.12),
            DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        efficient_marker = fixed(VGroup(
            DashedLine(ax.c2p(32, 0), ax.c2p(32, 5.6), color=FOCUS, stroke_width=2),
            Dot(ax.c2p(32, 5.6), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER + 1)).set_z_index(11))
        efficient_marker[1].set_z_index(DOT_LAYER + 1)
        efficient_word = fixed(VGroup(Tex(r'$Q^*$', color=FOCUS), Tex('32', color=FOCUS)).arrange(DOWN, buff=0.08).scale(0.64).next_to(ax.c2p(32, 0), DOWN, buff=0.20))
        dwl_bars = fixed(VGroup(*[unit_slice(ax, q, mb, msc, DWL, 0.8) for q in range(EFFICIENT_Q, MARKET_Q)]).set_z_index(1))
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(40, 5.4), RIGHT, buff=0.3))
        recap = teaching('Last time: the market exchanges 40 units, but only 32 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(msc_intercept),
                  FadeIn(benefit_bars), FadeIn(cost_bars), FadeIn(ext_bars), FadeIn(demand), FadeIn(supply), FadeIn(social_cost),
                  FadeIn(curve_words), FadeIn(market_dot), FadeIn(market_quantity), FadeIn(market_price))
        self.play(FadeIn(efficient_marker), FadeIn(efficient_word), FadeIn(dwl_bars), FadeIn(dwl_word), FadeIn(recap))
        self.pause('1.a')

        original_guides = fixed(VGroup(
            DashedLine(ax.c2p(0, MARKET_P), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
            DashedLine(ax.c2p(MARKET_Q, 0), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2))).set_z_index(2)

        # ---- 2.a · The planner wants 32 units; which price gets both sides there?
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, 'Someone who wants the efficient quantity, 32 units.'))
        question = teaching('What price gets buyers and sellers to exchange 32 units?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(market_price), FadeOut(msc_intercept),
                  FadeOut(market_quantity), FadeOut(efficient_word), FadeOut(dwl_word),
                  FadeOut(benefit_bars), FadeOut(cost_bars), FadeOut(ext_bars), FadeIn(original_guides))
        self.pause('2.a')

        # ---- 2.b · Set the price at the buyers' willingness to pay for unit 32: an excess.
        price = ValueTracker(MARKET_P)
        trial_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        trial_line.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(0, price.get_value()),
            ax.c2p(max(quantity_demanded(price.get_value()), quantity_supplied(price.get_value())) + 1e-6,
                   price.get_value())))
        trial_number = fixed(DecimalNumber(MARKET_P, num_decimal_places=2, color=GUIDE).scale(0.7))
        trial_number.add_updater(lambda m: fixed(m.set_value(price.get_value()))
                                 .next_to(ax.c2p(0, price.get_value()), LEFT, buff=0.2))
        trial_prefix = fixed(Tex('$P=$', color=GUIDE).scale(0.7))
        trial_prefix.add_updater(lambda m: m.next_to(trial_number, LEFT, buff=0.1))
        buyer_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        buyer_dot.add_updater(lambda m: m.move_to(ax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        seller_dot.add_updater(lambda m: m.move_to(ax.c2p(quantity_supplied(price.get_value()), price.get_value())))
        buyer_drop = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        buyer_drop.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(quantity_demanded(price.get_value()), 0),
            ax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_drop = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        seller_drop.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(quantity_supplied(price.get_value()), 0),
            ax.c2p(quantity_supplied(price.get_value()), price.get_value())))
        # The solid grey stretch between the two dots is the excess or shortage.
        gap_line = fixed(Line(ax.c2p(40, 4), ax.c2p(40.001, 4), color=MUTED, stroke_width=4).set_z_index(11))
        gap_line.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(quantity_demanded(price.get_value()), price.get_value()),
            ax.c2p(quantity_supplied(price.get_value()) + 1e-6, price.get_value())))
        buyer_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.65))
        buyer_number.add_updater(lambda m: fixed(m.set_value(round(quantity_demanded(price.get_value()), 4)))
                                 .next_to(ax.c2p(quantity_demanded(price.get_value()), 0), DOWN, buff=0.2).shift(RIGHT * 0.3))
        buyer_prefix = fixed(Tex('$Q_d=$', color=GUIDE).scale(0.65))
        buyer_prefix.add_updater(lambda m: m.next_to(buyer_number, LEFT, buff=0.1))
        seller_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.65))
        seller_number.add_updater(lambda m: fixed(m.set_value(round(quantity_supplied(price.get_value()), 4)))
                                  .next_to(ax.c2p(quantity_supplied(price.get_value()), 0), DOWN, buff=0.55).shift(RIGHT * 0.3))
        seller_prefix = fixed(Tex('$Q_s=$', color=GUIDE).scale(0.65))
        seller_prefix.add_updater(lambda m: m.next_to(seller_number, LEFT, buff=0.1))
        trial = [trial_line, trial_number, trial_prefix, buyer_dot, seller_dot, buyer_drop, seller_drop, gap_line]
        readouts = [buyer_number, buyer_prefix, seller_number, seller_prefix]
        for m in trial + readouts:
            m.update()
        self.remove(market_dot)
        self.add(*trial)
        self.play(price.animate.set_value(5.6), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{excess: 40 units}', color=CAPTION).scale(0.55).next_to(gap_line, UP, buff=0.12))
        for m in readouts:
            m.update()   # Digits must already match before a number fades in.
        self.remove(question)
        question = teaching('The price that works for buyers creates excess supply.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_prefix), FadeIn(seller_number), FadeIn(seller_prefix),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('2.b')

        # ---- 2.c · Set the price at the sellers' willingness to sell unit 32: a shortage.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(3.6), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{shortage: 10 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=0.12))
        question = teaching('The price that works for sellers creates a shortage.')
        self.play(FadeIn(gap_word), FadeIn(question))
        self.pause('2.c')

        # ---- 2.d · Both prices at once: the gap between them at Q = 32.
        for m in trial + readouts:
            m.clear_updaters()
        self.remove(question)
        seller_price = fixed(VGroup(
            DashedLine(ax.c2p(0, 3.6), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2),
            Tex('$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 3.6), LEFT, buff=0.2)).set_z_index(10))
        buyer_price = fixed(VGroup(
            DashedLine(ax.c2p(0, 5.6), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2),
            Tex('$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 5.6), LEFT, buff=0.2)).set_z_index(10))
        gap_mark = fixed(VGroup(
            Line(ax.c2p(32, 3.6), ax.c2p(32, 5.6), color=FOCUS, stroke_width=4),
            Tex(r'$\$2$', color=FOCUS).scale(0.7).next_to(ax.c2p(32, 4.6), RIGHT, buff=0.12)).set_z_index(13))
        takeaway = teaching('One price cannot get both sides to the efficient quantity.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_prefix),
                  FadeOut(seller_number), FadeOut(seller_prefix), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price), FadeIn(market_dot),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('2.d')

        # ---- 2.e · That gap is the external cost per unit.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external cost per unit.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('2.e')

        # ---- 3.a · A $2 tax: the wedge slides in from the left until it is stuck between MC and MB.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Taxes'))
        context = fixed(subtitle(head, 'A tax equal to the external cost per unit.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        wedge_x = ValueTracker(-14)
        wedge = fixed(Polygon(
            ax.c2p(-14 - 0.42, 3.6), ax.c2p(-14 + 0.42, 3.6),
            ax.c2p(-14 + 0.42, 5.6), ax.c2p(-14 - 0.42, 5.6),
            stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY).set_z_index(12))
        wedge.quantity, wedge.axes = wedge_x, ax
        wedge.add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), 4.6)))
        wedge_word = fixed(Tex(r'\$2 tax', color=GOV).scale(0.6)
            .add_background_rectangle(color=BG, opacity=1, buff=0.04).set_z_index(13))
        wedge_word.wedge = wedge
        wedge_word.add_updater(lambda m: m.next_to(m.wedge, LEFT, buff=0.15))
        wedge.update(); wedge_word.update()
        takeaway = teaching(r"A $\$2$ tax separates the buyers' price from the sellers' price by $\$2$.")
        self.play(FadeIn(wedge), FadeIn(wedge_word), FadeIn(takeaway))
        self.play(wedge_x.animate.set_value(EFFICIENT_Q), run_time=2.6, rate_func=smooth)
        wedge.clear_updaters(); wedge_word.clear_updaters()
        tax_prices = fixed(VGroup(
            Dot(ax.c2p(32, 5.6), radius=0.07, color=GUIDE),
            Dot(ax.c2p(32, 3.6), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, 5.6), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2),
            Tex('$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 5.6), LEFT, buff=0.2),
            DashedLine(ax.c2p(0, 3.6), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2),
            Tex('$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 3.6), LEFT, buff=0.2),
            DashedLine(ax.c2p(32, 0), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2),
            VGroup(Tex(r'$Q^{tax}=Q^*$', color=GUIDE).scale(0.60), Tex('32', color=GUIDE).scale(0.64)).arrange(DOWN, buff=0.08).next_to(ax.c2p(32, 0), DOWN, buff=0.20)).set_z_index(10))
        for dot in tax_prices[:2]:
            dot.set_z_index(DOT_LAYER)
        efficient_marker[1].set_z_index(DOT_LAYER + 1)
        self.remove(takeaway)
        takeaway = teaching('The wedge gets stuck at 32 units, the efficient quantity.')
        self.play(FadeIn(tax_prices), FadeIn(takeaway))
        self.pause('3.a')

        # ---- 3.b · The exchanges past 32 stop, and their deadweight loss with them.
        self.remove(takeaway)
        takeaway = teaching('Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.')
        self.play(LaggedStart(*[FadeOut(bar) for bar in reversed(list(dwl_bars))], lag_ratio=0.15),
                  FadeIn(takeaway), run_time=1.6)
        self.remove(dwl_bars, *list(dwl_bars))
        self.pause('3.b')

        # ---- 3.c · Welfare with the tax: PS, then CS, then the government's revenue.
        self.remove(takeaway)
        question = teaching('With the tax, who gains and who pays?')
        ps_fill = fixed(VGroup(*[unit_slice(ax, q, mc, lambda x: 3.6, SUPPLY, SURPLUS_OPACITY) for q in range(EFFICIENT_Q)]))
        cs_fill = fixed(VGroup(*[unit_slice(ax, q, lambda x: 5.6, mb, DEMAND, SURPLUS_OPACITY) for q in range(EFFICIENT_Q)]))
        gov_fill = fixed(VGroup(*[unit_slice(ax, q, lambda x: 3.6, lambda x: 5.6, GOV, GOV_OPACITY) for q in range(EFFICIENT_Q)]))
        # Each label sits at the centroid of its own region.
        welfare_words = fixed(VGroup(
            Tex('PS', color=INK).scale(0.50).move_to(ax.c2p(EFFICIENT_Q / 3, (2 + 3.6 + 3.6) / 3)),
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(EFFICIENT_Q / 3, (12 + 5.6 + 5.6) / 3)),
            Tex('Tax revenue', color=INK).scale(0.58).move_to(ax.c2p(EFFICIENT_Q / 2, 4.6))).set_z_index(5))
        self.play(FadeIn(question), FadeOut(wedge_word))
        self.play(FadeIn(ps_fill), FadeIn(welfare_words[0]))
        self.play(FadeIn(cs_fill), FadeIn(welfare_words[1]))
        self.remove(question)
        takeaway = teaching(r'Buyers pay $\$5.60$, sellers receive $\$3.60$, and the government collects $\$2$ per unit.')
        self.play(FadeIn(gov_fill), FadeIn(welfare_words[2]), FadeIn(takeaway))
        self.pause('3.c')

        # ---- 3.d · The corrective result.
        self.remove(takeaway)
        takeaway = teaching('With a tax equal to the external cost, there is no deadweight loss.')
        self.play(FadeIn(takeaway))
        self.pause('3.d')
        # From here the market fades and returns as one group around the close-ups.
        market = fixed(VGroup(ax, axis_words, demand, supply, social_cost, curve_words, original_guides,
                             market_dot, efficient_marker, wedge, tax_prices,
                             ps_fill, cs_fill, gov_fill, welfare_words))
        self.remove(*[m for m in self.mobjects if m not in (head, context, takeaway)])
        self.add(market)

        # C2's centered columns, with the bystanders represented in pink.
        detail_people = fixed(Group())
        for x, color, name in [(-1.6, DEMAND, 'Buyer'), (0, EXT, 'Bystanders'), (1.6, SUPPLY, 'Seller')]:
            detail_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0,
                fill_color=color, fill_opacity=0.28).move_to([x, DETAIL_BASE - 0.60, 0])))
            detail_people.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            detail_people.add(fixed(Tex(name, color=CAPTION if name == 'Bystanders' else INK)
                .scale(0.60).move_to([x, DETAIL_BASE - 0.94, 0])))

        # ---- 3.e.select · Carry the selected unit into the same compact layout as C2.
        stopped_pair = fixed(VGroup(
            unit_slice(ax, 35, zero, mb, DEMAND, 0),
            unit_slice(ax, 35, zero, mc, SUPPLY, 0),
            unit_slice(ax, 35, mc, msc, EXT, 0)))
        stopped_home = stopped_pair.copy()
        stopped_box = fixed(SurroundingRectangle(stopped_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        self.play(FadeIn(stopped_pair), FadeIn(stopped_box))
        self.pause('3.e.select')

        # ---- 3.e.values · Names on the bars; values at their exact heights.
        stopped_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 4.8, DEMAND),
                                       (SELLER_LEFT, 0, 3.8, SUPPLY), (SELLER_LEFT, 3.8, 5.8, EXT)]:
            stopped_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(context), FadeOut(stopped_box),
                  Transform(stopped_pair, stopped_target), run_time=1.6)
        stopped_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(stopped_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED)))
        stopped_values = fixed(VGroup(
            Tex(r'\$4.80', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(4.8), 0], LEFT, buff=0.25),
            Tex(r'\$3.80', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(3.8), 0], RIGHT, buff=0.45),
            Tex(r'\$5.80', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(5.8), 0], RIGHT, buff=0.45),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(4.8), 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(3.8), 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(5.8), 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.55).move_to([1.21, detail_y(4.8), 0]))).set_z_index(4)
        stopped_external = fixed(VGroup(
            DashedLine([1.94, detail_y(3.8), 0], [1.94, detail_y(5.8), 0], color=EXT, stroke_width=2),
            Tex(r'\$2', color=EXT).scale(0.62).next_to([1.94, detail_y(4.8), 0], RIGHT, buff=0.15))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'The 36th unit: an exchange the tax stops.'))
        stopped_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(stopped_edges), FadeIn(stopped_values), FadeIn(stopped_external),
                  FadeIn(unit_context), FadeIn(stopped_questions))
        self.pause('3.e.values')

        # ---- 3.e.tax · Government's transfer has its own middle column, separate from real external cost.
        stopped_prices = fixed(VGroup(
            Line([-2.6, detail_y(5.6), 0], [1.9, detail_y(5.6), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(3.6), 0], [1.9, detail_y(3.6), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        stopped_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(5.6), 0], UP, buff=0.06),
            Tex(r'\$5.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(5.6), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(3.6), 0], DOWN, buff=0.06),
            Tex(r'\$3.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(3.6), 0], LEFT, buff=0.15))).set_z_index(4)
        stopped_tax = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(3.6), 0], [TAX_LEFT + TAX_WIDTH, detail_y(3.6), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(5.6), 0], [TAX_LEFT, detail_y(5.6), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            VGroup(Tex('tax', color=INK), Tex(r'\$2', color=INK)).arrange(DOWN, buff=0.06).scale(0.50)
                .move_to([0, detail_y(4.6), 0]))).set_z_index(3)
        self.play(FadeIn(stopped_prices), FadeIn(stopped_price_words), FadeIn(stopped_tax))
        self.pause('3.e.tax')

        # ---- 3.e.question · Compare each participant's value to their own price before revealing the answer.
        stopped_private_guides = fixed(VGroup(
            DashedLine(stopped_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.8), 0], [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=3),
            DashedLine([SELLER_LEFT, detail_y(3.8), 0], [TAX_LEFT + TAX_WIDTH + 0.12, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.12, detail_y(3.8), 0], [stopped_price_words[3].get_right()[0] + 0.12, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([stopped_price_words[3].get_left()[0] - 0.12, detail_y(3.8), 0], [-4.25, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(3.8), 0], [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=3)))
        stopped_private_answer = fixed(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5), Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)
            .next_to([-4.25, detail_y(4.3), 0], LEFT, buff=0.3))
        self.play(FadeIn(stopped_private_guides))
        self.pause('3.e.question')
        self.play(FadeIn(stopped_private_answer))
        self.pause('3.e.answer')

        # ---- 3.e.social · Real benefit versus real cost: tax revenue is a transfer, not another social cost.
        stopped_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [SELLER_LEFT, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([stopped_external[1].get_right()[0] + 0.12, detail_y(4.8), 0], [4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(5.8), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(4.8), 0], [4.25, detail_y(5.8), 0], color=TOTAL, stroke_width=3)))
        stopped_social_answer = fixed(VGroup(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5), Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)), Tex(r'DWL \$1', color=INK))
            .arrange(DOWN, buff=0.16).scale(0.70).next_to([4.25, detail_y(5.3), 0], RIGHT, buff=0.3))
        self.play(FadeOut(stopped_tax), FadeOut(stopped_private_guides),
                  stopped_prices.animate.set_opacity(0.25), stopped_price_words.animate.set_opacity(0.25),
                  FadeIn(stopped_social_guides))
        self.pause('3.e.social')
        stopped_welfare = fixed(Polygon(
            [SELLER_LEFT, detail_y(4.8), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(4.8), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(5.8), 0],
            [SELLER_LEFT, detail_y(5.8), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        takeaway = teaching(r'The tax prevents a trade that would create \$1 of deadweight loss.')
        self.play(FadeIn(stopped_welfare), FadeIn(stopped_social_answer), FadeIn(takeaway))
        self.pause('3.e')

        # ---- 3.e.return · Restore exactly the same market; the temporary selected slice disappears.
        self.remove(detail_people)
        self.play(FadeOut(stopped_edges), FadeOut(stopped_values), FadeOut(stopped_external), FadeOut(stopped_questions),
                  FadeOut(stopped_prices), FadeOut(stopped_price_words), FadeOut(stopped_private_answer),
                  FadeOut(stopped_social_guides), FadeOut(stopped_social_answer), FadeOut(stopped_welfare),
                  FadeOut(takeaway), FadeOut(unit_context), run_time=0.4)
        self.play(Transform(stopped_pair, stopped_home), FadeIn(market), FadeIn(context), run_time=1.6)
        self.remove(stopped_pair)
        self.pause('3.e.return')

        # ---- 3.f.select · Carry the selected unit into the same compact layout as C2.
        kept_pair = fixed(VGroup(
            unit_slice(ax, 23, zero, mb, DEMAND, 0),
            unit_slice(ax, 23, zero, mc, SUPPLY, 0),
            unit_slice(ax, 23, mc, msc, EXT, 0)))
        kept_home = kept_pair.copy()
        kept_box = fixed(SurroundingRectangle(kept_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        self.play(FadeIn(kept_pair), FadeIn(kept_box))
        self.pause('3.f.select')

        # ---- 3.f.values · Names on the bars; values at their exact heights.
        kept_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 7.2, DEMAND),
                                       (SELLER_LEFT, 0, 3.2, SUPPLY), (SELLER_LEFT, 3.2, 5.2, EXT)]:
            kept_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(context), FadeOut(kept_box),
                  Transform(kept_pair, kept_target), run_time=1.6)
        kept_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(kept_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED)))
        kept_values = fixed(VGroup(
            Tex(r'\$7.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(7.2), 0], LEFT, buff=0.25),
            Tex(r'\$3.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(3.2), 0], RIGHT, buff=0.45),
            Tex(r'\$5.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(5.2), 0], RIGHT, buff=0.45),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(7.2), 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(3.2), 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(5.2), 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.55).move_to([1.21, detail_y(4.2), 0]))).set_z_index(4)
        kept_external = fixed(VGroup(
            DashedLine([1.94, detail_y(3.2), 0], [1.94, detail_y(5.2), 0], color=EXT, stroke_width=2),
            Tex(r'\$2', color=EXT).scale(0.62).next_to([1.94, detail_y(4.2), 0], RIGHT, buff=0.15))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'The 24th unit: an exchange the tax keeps.'))
        kept_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(kept_edges), FadeIn(kept_values), FadeIn(kept_external),
                  FadeIn(unit_context), FadeIn(kept_questions))
        self.pause('3.f.values')

        # ---- 3.f.tax · Government's transfer has its own middle column, separate from real external cost.
        kept_prices = fixed(VGroup(
            Line([-2.6, detail_y(5.6), 0], [1.9, detail_y(5.6), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(3.6), 0], [1.9, detail_y(3.6), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        kept_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(5.6), 0], UP, buff=0.06),
            Tex(r'\$5.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(5.6), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(3.6), 0], DOWN, buff=0.06),
            Tex(r'\$3.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(3.6), 0], LEFT, buff=0.15))).set_z_index(4)
        kept_tax = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(3.6), 0], [TAX_LEFT + TAX_WIDTH, detail_y(3.6), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(5.6), 0], [TAX_LEFT, detail_y(5.6), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            VGroup(Tex('tax', color=INK), Tex(r'\$2', color=INK)).arrange(DOWN, buff=0.06).scale(0.50)
                .move_to([0, detail_y(4.6), 0]))).set_z_index(3)
        self.play(FadeIn(kept_prices), FadeIn(kept_price_words), FadeIn(kept_tax))
        self.pause('3.f.tax')

        # ---- 3.f.question · Compare each participant's value to their own price before revealing the answer.
        kept_private_guides = fixed(VGroup(
            DashedLine(kept_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(7.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(7.2), 0], [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=3),
            DashedLine([SELLER_LEFT, detail_y(3.2), 0], [TAX_LEFT + TAX_WIDTH + 0.12, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.12, detail_y(3.2), 0], [kept_price_words[3].get_right()[0] + 0.12, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([kept_price_words[3].get_left()[0] - 0.12, detail_y(3.2), 0], [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(3.2), 0], [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=3)))
        kept_private_answer = fixed(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)
            .next_to([-4.25, detail_y(5.2), 0], LEFT, buff=0.3))
        self.play(FadeIn(kept_private_guides))
        self.pause('3.f.question')
        self.play(FadeIn(kept_private_answer))
        self.pause('3.f.answer')

        # ---- 3.f.social · Real benefit versus real cost: tax revenue is a transfer, not another social cost.
        kept_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(7.2), 0], [4.25, detail_y(7.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(5.2), 0], [4.25, detail_y(7.2), 0], color=TOTAL, stroke_width=3)))
        kept_social_answer = fixed(VGroup(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex(r'TS \$2', color=TOTAL))
            .arrange(DOWN, buff=0.16).scale(0.70).next_to([4.25, detail_y(6.2), 0], RIGHT, buff=0.3))
        self.play(FadeOut(kept_tax), FadeOut(kept_private_guides),
                  kept_prices.animate.set_opacity(0.25), kept_price_words.animate.set_opacity(0.25),
                  FadeIn(kept_social_guides))
        self.pause('3.f.social')
        kept_welfare = fixed(Polygon(
            [BUYER_LEFT, detail_y(5.2), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(5.2), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(7.2), 0],
            [BUYER_LEFT, detail_y(7.2), 0],
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY).set_z_index(1))
        takeaway = teaching(r'This trade generates \$2 of social surplus.')
        self.play(FadeIn(kept_welfare), FadeIn(kept_social_answer), FadeIn(takeaway))
        self.pause('3.f')

        # ---- 3.f.return · Restore exactly the same market; the temporary selected slice disappears.
        self.remove(detail_people)
        self.play(FadeOut(kept_edges), FadeOut(kept_values), FadeOut(kept_external), FadeOut(kept_questions),
                  FadeOut(kept_prices), FadeOut(kept_price_words), FadeOut(kept_private_answer),
                  FadeOut(kept_social_guides), FadeOut(kept_social_answer), FadeOut(kept_welfare),
                  FadeOut(takeaway), FadeOut(unit_context), run_time=0.4)
        self.play(Transform(kept_pair, kept_home), FadeIn(market), FadeIn(context), run_time=1.6)
        self.remove(kept_pair)
        self.pause('3.f.return')

        # ---- 3.g · Dial the tax: everything tax-dependent hangs on one tracker.
        self.remove(context)
        context = fixed(subtitle(head, r'Adjusting the tax around the \$2 external cost.'))
        self.add(context)
        tax = ValueTracker(EXTERNAL)
        taxed_q = lambda: taxed_quantity(tax.get_value())
        buyer_pays = lambda: mb(taxed_quantity(tax.get_value()))
        seller_gets = lambda: mc(taxed_quantity(tax.get_value()))
        wedge.add_updater(lambda m: m.become(fixed(Polygon(
            ax.c2p(taxed_q() - 0.42, seller_gets()), ax.c2p(taxed_q() + 0.42, seller_gets()),
            ax.c2p(taxed_q() + 0.42, buyer_pays()), ax.c2p(taxed_q() - 0.42, buyer_pays()),
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY).set_z_index(12))))
        live_top_dot = fixed(Dot(ax.c2p(32, 5.6), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        live_top_dot.add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), buyer_pays())))
        live_bottom_dot = fixed(Dot(ax.c2p(32, 3.6), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        live_bottom_dot.add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), seller_gets())))
        live_tax_number = fixed(DecimalNumber(EXTERNAL, num_decimal_places=2, color=GOV).scale(0.6).set_z_index(14))
        live_tax_number.add_updater(lambda m: fixed(m.set_value(tax.get_value())).next_to(ax.c2p(taxed_q(), buyer_pays()), UL, buff=0.18).shift(LEFT * 0.62))
        live_tax_prefix = fixed(Tex(r'\$', color=GOV).scale(0.6).set_z_index(14))
        live_tax_prefix.add_updater(lambda m: m.next_to(live_tax_number, LEFT, buff=0.02))
        live_tax_suffix = fixed(Tex('tax', color=GOV).scale(0.6).set_z_index(14))
        live_tax_suffix.add_updater(lambda m: m.next_to(live_tax_number, RIGHT, buff=0.08))
        live_tax_background = fixed(BackgroundRectangle(VGroup(live_tax_prefix, live_tax_number, live_tax_suffix),
            color=BG, fill_opacity=1, buff=0.04)).set_z_index(13)
        live_tax_background.add_updater(lambda m: m.become(fixed(BackgroundRectangle(
            VGroup(live_tax_prefix, live_tax_number, live_tax_suffix), color=BG, fill_opacity=1, buff=0.04)).set_z_index(13)))
        live_buyer_line = fixed(DashedLine(ax.c2p(0, 5.6), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_buyer_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, buyer_pays()), ax.c2p(taxed_q(), buyer_pays())))
        live_seller_line = fixed(DashedLine(ax.c2p(0, 3.6), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_seller_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, seller_gets()), ax.c2p(taxed_q(), seller_gets())))
        live_drop = fixed(DashedLine(ax.c2p(32, 0), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_drop.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(taxed_q(), 0), ax.c2p(taxed_q(), buyer_pays())))
        live_buyer_number = fixed(DecimalNumber(5.6, num_decimal_places=2, color=GUIDE).scale(0.7))
        live_buyer_number.add_updater(lambda m: fixed(m.set_value(buyer_pays())).next_to(ax.c2p(0, buyer_pays()), LEFT, buff=0.2))
        live_buyer_prefix = fixed(Tex('$P_b=$', color=GUIDE).scale(0.7))
        live_buyer_prefix.add_updater(lambda m: m.next_to(live_buyer_number, LEFT, buff=0.1))
        live_seller_number = fixed(DecimalNumber(3.6, num_decimal_places=2, color=GUIDE).scale(0.7))
        live_seller_number.add_updater(lambda m: fixed(m.set_value(seller_gets())).next_to(ax.c2p(0, seller_gets()), LEFT, buff=0.2))
        live_seller_prefix = fixed(Tex('$P_s=$', color=GUIDE).scale(0.7))
        live_seller_prefix.add_updater(lambda m: m.next_to(live_seller_number, LEFT, buff=0.1))
        live_q_number = fixed(DecimalNumber(32, num_decimal_places=0, color=GUIDE).scale(0.7))
        live_q_number.add_updater(lambda m: fixed(m.set_value(round(taxed_q(), 4))).next_to(ax.c2p(taxed_q(), 0), DOWN, buff=0.2).shift(RIGHT * 0.33))
        live_q_prefix = fixed(Tex('$Q=$', color=GUIDE).scale(0.7))
        live_q_prefix.add_updater(lambda m: m.next_to(live_q_number, LEFT, buff=0.1))
        # Fills follow the traded units, including a partial last unit while the tax rolls.
        live_ps, live_cs, live_gov = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            for group, low, high, color, opacity in [
                    (live_ps, mc, lambda x: seller_gets(), SUPPLY, SURPLUS_OPACITY),
                    (live_cs, lambda x: buyer_pays(), mb, DEMAND, SURPLUS_OPACITY),
                    (live_gov, lambda x: seller_gets(), lambda x: buyer_pays(), GOV, GOV_OPACITY)]:
                piece = unit_slice(ax, q, low, high, color, opacity if q < EFFICIENT_Q else 0)
                piece.add_updater(lambda m, q=q, low=low, high=high, color=color, opacity=opacity: m.become(
                    unit_slice(ax, q, low, high, color, opacity if q + BAR_GAP / 2 < taxed_q() else 0,
                              right=min(q + 1 - BAR_GAP / 2, max(taxed_q(), q + BAR_GAP / 2 + 1e-6)))))
                group.add(piece)
        # Clip each grey slice at the moving quantity; never pre-grey a whole unit.
        live_dwl = fixed(VGroup())
        for q in range(taxed_quantity(4), MARKET_Q):
            bar = unit_slice(ax, q, mb if q >= EFFICIENT_Q else msc,
                             msc if q >= EFFICIENT_Q else mb, DWL, 0).set_z_index(1)
            bar.add_updater(lambda m, q=q: m.become(unit_slice(
                ax, q, mb if q >= EFFICIENT_Q else msc, msc if q >= EFFICIENT_Q else mb, DWL,
                0.8 if (q >= EFFICIENT_Q and q + BAR_GAP / 2 < taxed_q()) or
                       (q < EFFICIENT_Q and q + 1 - BAR_GAP / 2 > taxed_q()) else 0,
                left=q + BAR_GAP / 2 if q >= EFFICIENT_Q else min(q + 1 - BAR_GAP / 2 - 1e-6, max(q + BAR_GAP / 2, taxed_q())),
                right=max(q + BAR_GAP / 2 + 1e-6, min(q + 1 - BAR_GAP / 2, taxed_q())) if q >= EFFICIENT_Q else q + 1 - BAR_GAP / 2
            ).set_z_index(1)))
            live_dwl.add(bar)
        welfare_words[0].add_updater(lambda m: m.move_to(ax.c2p(taxed_q() / 3, (2 + 2 * seller_gets()) / 3)))
        welfare_words[1].add_updater(lambda m: m.move_to(ax.c2p(taxed_q() / 3, (12 + 2 * buyer_pays()) / 3)))
        welfare_words[2].add_updater(lambda m: m.move_to(ax.c2p(taxed_q() / 2, (buyer_pays() + seller_gets()) / 2)))
        live_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8))
        # Right of the traded units when the tax is small; above the curves past Q-star when it is large.
        live_dwl_word.add_updater(lambda m: m.next_to(
            ax.c2p(taxed_q() + 1.5, (mb(taxed_q()) + msc(taxed_q())) / 2) if taxed_q() >= EFFICIENT_Q
            else ax.c2p(EFFICIENT_Q, mb(EFFICIENT_Q) + 0.9), RIGHT, buff=0.15)
            .set_opacity(1 if abs(taxed_q() - EFFICIENT_Q) >= 1 else 0))
        live = [wedge, live_top_dot, live_bottom_dot, live_tax_number, live_tax_prefix, live_tax_suffix, live_tax_background,
                live_buyer_line, live_seller_line, live_drop,
                live_buyer_number, live_buyer_prefix, live_seller_number, live_seller_prefix,
                live_q_number, live_q_prefix, live_ps, live_cs, live_gov, live_dwl, live_dwl_word]
        for m in live:
            m.update()
        market.remove(wedge, wedge_word, tax_prices, ps_fill, cs_fill, gov_fill)
        self.remove(wedge_word, tax_prices, ps_fill, cs_fill, gov_fill)
        market.remove(welfare_words)
        self.add(*live, welfare_words)
        question = teaching('What if the tax is smaller than the external cost?')
        self.play(FadeIn(question))
        self.play(tax.animate.set_value(1), run_time=2.2, rate_func=smooth)
        self.remove(question)
        takeaway = teaching('A smaller tax leaves some harmful exchanges in place.')
        self.play(FadeIn(takeaway))
        self.pause('3.g.low')
        self.remove(takeaway)
        self.play(tax.animate.set_value(EXTERNAL), run_time=2.0, rate_func=smooth)
        takeaway = teaching(r'Back to the corrective tax: \$2 per unit.')
        self.play(FadeIn(takeaway))
        self.pause('3.g.reset')
        self.remove(takeaway)
        question = teaching('What if the tax is larger than the external cost?')
        self.play(FadeIn(question))
        self.play(tax.animate.set_value(4), run_time=2.6, rate_func=smooth)
        self.remove(question)
        takeaway = teaching('A larger tax removes exchanges that were worth making.')
        self.play(FadeIn(takeaway))
        self.pause('3.g.high')
        self.remove(takeaway)
        self.play(tax.animate.set_value(EXTERNAL), run_time=2.2, rate_func=smooth)
        takeaway = teaching(r'The corrective tax equals the external cost: $\$2$ per unit.')
        self.play(FadeIn(takeaway))
        self.pause('3.g')

        for m in self.mobjects:
            m.clear_updaters()
        self.remove(takeaway, context)
        context = fixed(subtitle(head, 'A tax equal to the external cost per unit.'))
        self.add(context)
        negative_conclusion_graph = fixed(VGroup(market, *live, welfare_words))
        self.remove(market, *live, welfare_words)
        self.add(negative_conclusion_graph)
        self.play(negative_conclusion_graph.animate.shift(LEFT * 2.0), run_time=1.2)
        negative_equality = fixed(VGroup(
            Tex(r'$Q^{tax}=Q^*$', color=FOCUS).scale(1.10),
            Tex('32 units', color=CAPTION).scale(0.65),
            Tex('Tax = external cost', color=INK).scale(0.68)
        ).arrange(DOWN, buff=0.28).move_to([4.2, 0.7, 0]))
        takeaway = teaching('A corrective tax prevents harmful trades and preserves worthwhile ones.')
        self.play(FadeIn(negative_equality), FadeIn(takeaway))
        self.pause('3.g.summary')

        # ---- 4.a · Last time: the positive-externality market and its deadweight loss.
        for m in self.mobjects:
            m.clear_updaters()
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        self.clear()
        head = fixed(title('Positive Externalities'))
        context = fixed(subtitle(head, 'A benefit received by others outside the market.'))
        pax = style_axes([0, 80, 10], [0, 15, 2], x_length=6.4, y_length=4.6)
        pax.shift(np.array([ORIGIN_X, ORIGIN_Y, 0]) - pax.c2p(0, 0))
        fixed(pax)
        positive_axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(pax.c2p(0, 15), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(pax.c2p(0, 15), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(pax.c2p(80, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(pax.c2p(80, 0), DOWN, buff=0.73),
            Tex('$2$', color=SUPPLY).scale(0.65).next_to(pax.c2p(0, 2), LEFT, buff=0.15),
            Tex('$12$', color=DEMAND).scale(0.65).next_to(pax.c2p(0, 12), LEFT, buff=0.15),
            Tex('$14$', color=DEMAND).scale(0.65).next_to(pax.c2p(0, 14), LEFT, buff=0.15)))
        positive_demand = fixed(Line(pax.c2p(0, 12), pax.c2p(60, 0), color=DEMAND, stroke_width=3))
        positive_supply = fixed(Line(pax.c2p(0, 2), pax.c2p(80, 6), color=SUPPLY, stroke_width=3))
        social_benefit = fixed(Line(pax.c2p(0, 14), pax.c2p(70, 0), color=DEMAND, stroke_width=3))
        positive_curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(pax.c2p(8, 10.4), DOWN, buff=0.14),
            Tex('MC', color=INK).scale(0.7).next_to(pax.c2p(80, 6), RIGHT, buff=0.12),
            Tex('MSB', color=INK).scale(0.7).next_to(pax.c2p(8, 12.4), UR, buff=0.10)).set_z_index(6))
        positive_benefit_bars, positive_cost_bars, positive_ext_bars = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(60):
            positive_benefit_bars.add(unit_slice(pax, q, zero, mb, DEMAND, BASE_OPACITY if q < MARKET_Q else 0))
            positive_cost_bars.add(unit_slice(pax, q, zero, mc, SUPPLY, BASE_OPACITY if q < MARKET_Q else 0))
            positive_ext_bars.add(unit_slice(pax, q, mb, msb, EXT, BASE_OPACITY if q < MARKET_Q else 0))
        positive_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        positive_quantity = fixed(VGroup(
            DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2),
            VGroup(Tex(r'$\hat{Q}$', color=GUIDE), Tex('40', color=GUIDE)).arrange(DOWN, buff=0.08).scale(0.64).next_to(pax.c2p(40, 0), DOWN, buff=0.20)).set_z_index(10))
        positive_price = fixed(VGroup(
            Tex(r'$\hat{P}=4$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 4), LEFT, buff=0.2),
            DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        positive_efficient = fixed(VGroup(
            DashedLine(pax.c2p(48, 0), pax.c2p(48, 4.4), color=FOCUS, stroke_width=2),
            Dot(pax.c2p(48, 4.4), radius=0.085, color=FOCUS)).set_z_index(11))
        positive_efficient[1].set_z_index(DOT_LAYER + 1)
        positive_efficient_word = fixed(VGroup(Tex(r'$Q^*$', color=FOCUS), Tex('48', color=FOCUS)).arrange(DOWN, buff=0.08).scale(0.64).next_to(pax.c2p(48, 0), DOWN, buff=0.20))
        positive_dwl = fixed(VGroup(*[unit_slice(pax, q, mc, msb, DWL, 0.8) for q in range(MARKET_Q, POSITIVE_Q)]).set_z_index(1))
        positive_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(positive_dwl, UP, buff=0.16))
        recap = teaching('Last time: the market exchanges 40 units, but 48 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(pax), FadeIn(positive_axis_words), FadeIn(positive_benefit_bars), FadeIn(positive_cost_bars),
                  FadeIn(positive_ext_bars), FadeIn(positive_demand), FadeIn(positive_supply), FadeIn(social_benefit),
                  FadeIn(positive_curve_words), FadeIn(positive_dot), FadeIn(positive_quantity), FadeIn(positive_price))
        self.play(FadeIn(positive_efficient), FadeIn(positive_efficient_word), FadeIn(positive_dwl), FadeIn(positive_dwl_word), FadeIn(recap))
        self.pause('4.a')

        positive_original_guides = fixed(VGroup(
            DashedLine(pax.c2p(0, MARKET_P), pax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
            DashedLine(pax.c2p(MARKET_Q, 0), pax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2))).set_z_index(2)

        # ---- 4.b · The planner wants 48 units.
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, 'Someone who wants the efficient quantity, 48 units.'))
        question = teaching('What price gets buyers and sellers to exchange 48 units?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(positive_price), FadeOut(positive_axis_words[4]),
                  FadeOut(positive_quantity), FadeOut(positive_efficient_word), FadeOut(positive_dwl_word),
                  FadeOut(positive_benefit_bars), FadeOut(positive_cost_bars), FadeOut(positive_ext_bars), FadeIn(positive_original_guides))
        positive_axis_words.remove(positive_axis_words[4])
        self.pause('4.b')

        # ---- 4.c · The buyers' willingness to pay for unit 48: a shortage.
        price = ValueTracker(MARKET_P)
        trial_line = fixed(DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        trial_line.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(0, price.get_value()),
            pax.c2p(max(quantity_demanded(price.get_value()), quantity_supplied(price.get_value())) + 1e-6,
                    price.get_value())))
        trial_number = fixed(DecimalNumber(MARKET_P, num_decimal_places=2, color=GUIDE).scale(0.7))
        trial_number.add_updater(lambda m: fixed(m.set_value(price.get_value()))
                                 .next_to(pax.c2p(0, price.get_value()), LEFT, buff=0.2))
        trial_prefix = fixed(Tex('$P=$', color=GUIDE).scale(0.7))
        trial_prefix.add_updater(lambda m: m.next_to(trial_number, LEFT, buff=0.1))
        buyer_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        buyer_dot.add_updater(lambda m: m.move_to(pax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(DOT_LAYER))
        seller_dot.add_updater(lambda m: m.move_to(pax.c2p(quantity_supplied(price.get_value()), price.get_value())))
        buyer_drop = fixed(DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        buyer_drop.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(quantity_demanded(price.get_value()), 0),
            pax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_drop = fixed(DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        seller_drop.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(quantity_supplied(price.get_value()), 0),
            pax.c2p(quantity_supplied(price.get_value()), price.get_value())))
        gap_line = fixed(Line(pax.c2p(40, 4), pax.c2p(40.001, 4), color=MUTED, stroke_width=4).set_z_index(11))
        gap_line.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(quantity_demanded(price.get_value()), price.get_value()),
            pax.c2p(quantity_supplied(price.get_value()) + 1e-6, price.get_value())))
        buyer_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.65))
        buyer_number.add_updater(lambda m: fixed(m.set_value(round(quantity_demanded(price.get_value()), 4)))
                                 .next_to(pax.c2p(quantity_demanded(price.get_value()), 0), DOWN, buff=0.2).shift(RIGHT * 0.3))
        buyer_prefix = fixed(Tex('$Q_d=$', color=GUIDE).scale(0.65))
        buyer_prefix.add_updater(lambda m: m.next_to(buyer_number, LEFT, buff=0.1))
        seller_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.65))
        seller_number.add_updater(lambda m: fixed(m.set_value(round(quantity_supplied(price.get_value()), 4)))
                                  .next_to(pax.c2p(quantity_supplied(price.get_value()), 0), DOWN, buff=0.55).shift(RIGHT * 0.3))
        seller_prefix = fixed(Tex('$Q_s=$', color=GUIDE).scale(0.65))
        seller_prefix.add_updater(lambda m: m.next_to(seller_number, LEFT, buff=0.1))
        trial = [trial_line, trial_number, trial_prefix, buyer_dot, seller_dot, buyer_drop, seller_drop, gap_line]
        readouts = [buyer_number, buyer_prefix, seller_number, seller_prefix]
        for m in trial + readouts:
            m.update()
        self.remove(positive_dot)
        self.add(*trial)
        self.play(price.animate.set_value(2.4), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{shortage: 40 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=0.12))
        for m in readouts:
            m.update()
        self.remove(question)
        question = teaching('The price that works for buyers creates a shortage.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_prefix), FadeIn(seller_number), FadeIn(seller_prefix),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('4.c')

        # ---- 4.d · The sellers' willingness to sell unit 48: an excess.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(4.4), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{excess: 10 units}', color=CAPTION).scale(0.55).next_to(gap_line, UP, buff=0.12))
        question = teaching('The price that works for sellers creates excess supply.')
        self.play(FadeIn(gap_word), FadeIn(question))
        self.pause('4.d')

        # ---- 4.e · Both prices at once: the gap at Q = 48.
        for m in trial + readouts:
            m.clear_updaters()
        self.remove(question)
        seller_price = fixed(VGroup(
            DashedLine(pax.c2p(0, 4.4), pax.c2p(48, 4.4), color=GUIDE, stroke_width=2),
            Tex('$P_s=4.40$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 4.4), LEFT, buff=0.2)).set_z_index(10))
        buyer_price = fixed(VGroup(
            DashedLine(pax.c2p(0, 2.4), pax.c2p(48, 2.4), color=GUIDE, stroke_width=2),
            Tex('$P_b=2.40$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 2.4), LEFT, buff=0.2)).set_z_index(10))
        gap_mark = fixed(VGroup(
            Line(pax.c2p(48, 2.4), pax.c2p(48, 4.4), color=FOCUS, stroke_width=4),
            Tex(r'$\$2$', color=FOCUS).scale(0.7).next_to(pax.c2p(48, 3.4), RIGHT, buff=0.12)).set_z_index(13))
        takeaway = teaching('One price cannot get both sides to the efficient quantity.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_prefix),
                  FadeOut(seller_number), FadeOut(seller_prefix), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price), FadeIn(positive_dot),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('4.e')

        # ---- 4.f · That gap is the external benefit per unit.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external benefit per unit.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('4.f')

        # ---- 4.g · A $2 subsidy: the wedge slides in from the right, as in C2, and is stuck at 48.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Subsidies'))
        context = fixed(subtitle(head, 'A subsidy equal to the external benefit per unit.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        wedge_x = ValueTracker(66)
        subsidy_wedge = fixed(Polygon(
            pax.c2p(66 - 0.42, 2.4), pax.c2p(66 + 0.42, 2.4),
            pax.c2p(66 + 0.42, 4.4), pax.c2p(66 - 0.42, 4.4),
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY).set_z_index(12))
        subsidy_wedge.quantity, subsidy_wedge.axes = wedge_x, pax
        subsidy_wedge.add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), 3.4)))
        subsidy_word = fixed(Tex(r'\$2 subsidy', color=GOV).scale(0.6)
            .add_background_rectangle(color=BG, opacity=1, buff=0.04).set_z_index(13))
        subsidy_word.wedge = subsidy_wedge
        subsidy_word.add_updater(lambda m: m.next_to(m.wedge, LEFT, buff=0.15))
        subsidy_wedge.update(); subsidy_word.update()
        takeaway = teaching(r"A $\$2$ subsidy puts the sellers' price $\$2$ above the buyers' price.")
        self.play(FadeIn(subsidy_wedge), FadeIn(subsidy_word), FadeIn(takeaway))
        self.play(wedge_x.animate.set_value(POSITIVE_Q), run_time=2.8, rate_func=smooth)
        subsidy_wedge.clear_updaters(); subsidy_word.clear_updaters()
        subsidy_prices = fixed(VGroup(
            Dot(pax.c2p(48, 4.4), radius=0.07, color=GUIDE),
            Dot(pax.c2p(48, 2.4), radius=0.07, color=GUIDE),
            DashedLine(pax.c2p(0, 4.4), pax.c2p(48, 4.4), color=GUIDE, stroke_width=2),
            Tex('$P_s=4.40$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 4.4), LEFT, buff=0.2),
            DashedLine(pax.c2p(0, 2.4), pax.c2p(48, 2.4), color=GUIDE, stroke_width=2),
            Tex('$P_b=2.40$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 2.4), LEFT, buff=0.2),
            DashedLine(pax.c2p(48, 0), pax.c2p(48, 4.4), color=GUIDE, stroke_width=2),
            VGroup(Tex(r'$Q^{subsidy}=Q^*$', color=GUIDE).scale(0.60), Tex('48', color=GUIDE).scale(0.64)).arrange(DOWN, buff=0.08).next_to(pax.c2p(48, 0), DOWN, buff=0.20)).set_z_index(10))
        self.remove(takeaway)
        for dot in subsidy_prices[:2]:
            dot.set_z_index(DOT_LAYER)
        takeaway = teaching('The wedge gets stuck at 48 units, the efficient quantity.')
        self.play(FadeIn(subsidy_prices), FadeIn(takeaway))
        self.pause('4.g')

        # ---- 4.h · Units 41 to 48 now happen, and their deadweight loss is gone.
        self.remove(takeaway)
        takeaway = teaching('The subsidy enables worthwhile trades that the market leaves out.')
        self.play(LaggedStart(*[FadeOut(bar) for bar in positive_dwl], lag_ratio=0.15),
                  FadeIn(takeaway), run_time=1.6)
        self.remove(positive_dwl, *list(positive_dwl))
        self.pause('4.h')

        # ---- 4.h.select · The 44th unit is worthwhile but would be missed without the subsidy.
        positive_market = fixed(VGroup(pax, positive_axis_words, positive_demand, positive_supply,
            social_benefit, positive_curve_words, positive_original_guides, positive_dot,
            positive_efficient, subsidy_wedge, subsidy_word, subsidy_prices))
        self.remove(*[m for m in self.mobjects if m not in (head, context, takeaway)])
        self.add(positive_market)
        added_pair = fixed(VGroup(
            unit_slice(pax, 43, zero, mb, DEMAND, 0),
            unit_slice(pax, 43, mb, msb, EXT, 0),
            unit_slice(pax, 43, zero, mc, SUPPLY, 0)))
        added_home = added_pair.copy()
        added_box = fixed(SurroundingRectangle(added_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        self.play(FadeIn(added_pair), FadeIn(added_box))
        self.pause('4.h.select')

        added_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 3.2, DEMAND),
                                       (BUYER_LEFT, 3.2, 5.2, EXT), (SELLER_LEFT, 0, 4.2, SUPPLY)]:
            added_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(positive_market), FadeOut(context), FadeOut(added_box),
                  Transform(added_pair, added_target), run_time=1.6)
        added_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(added_target, [DEMAND, DEMAND, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED)))
        added_values = fixed(VGroup(
            Tex(r'\$3.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(3.2), 0], LEFT, buff=0.45),
            Tex(r'\$5.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(5.2), 0], LEFT, buff=0.45),
            Tex(r'\$4.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(4.2), 0], RIGHT, buff=0.25),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(3.2), 0], DOWN, buff=0.10),
            Tex('MSB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(5.2), 0], UP, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(4.2), 0], DOWN, buff=0.10),
            Tex('EXT', color=EXT).scale(0.55).move_to([-1.21, detail_y(4.2), 0]))).set_z_index(4)
        added_external = fixed(VGroup(
            DashedLine([-1.94, detail_y(3.2), 0], [-1.94, detail_y(5.2), 0], color=EXT, stroke_width=2),
            Tex(r'\$2', color=EXT).scale(0.62).next_to([-1.94, detail_y(4.2), 0], LEFT, buff=0.15))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'The 44th unit: an exchange the subsidy enables.'))
        added_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(added_edges), FadeIn(added_values), FadeIn(added_external),
                  FadeIn(unit_context), FadeIn(added_questions))
        self.pause('4.h.values')

        # First, without the subsidy: MC is above MB. The missing trade still benefits society.
        added_private_guides = fixed(VGroup(
            DashedLine(added_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([SELLER_LEFT, detail_y(4.2), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-3.30, detail_y(4.2), 0], [-4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(3.2), 0], [-4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=3)))
        added_no = fixed(VGroup(
            Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5),
            Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)
            .next_to([-4.25, detail_y(3.7), 0], LEFT, buff=0.3))
        takeaway = teaching('Without the subsidy, this trade does not happen.')
        self.play(FadeIn(added_private_guides))
        self.pause('4.h.question')
        self.play(FadeIn(added_no), FadeIn(takeaway))
        self.pause('4.h.answer')

        added_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(5.2), 0], [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(4.2), 0], [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=3)))
        added_social_answer = fixed(VGroup(
            VMobject().set_points_as_corners([[-0.26, 0, 0], [-0.07, -0.18, 0], [0.30, 0.26, 0]])
                .set_stroke(GOV, 5), Tex(r'TS \$1', color=TOTAL)).arrange(DOWN, buff=0.16)
            .scale(0.70).next_to([4.25, detail_y(4.7), 0], RIGHT, buff=0.3))
        self.remove(takeaway)
        self.play(FadeIn(added_social_guides))
        self.pause('4.h.social')
        takeaway = teaching(r'This trade would generate \$1 of social surplus.')
        self.play(FadeIn(added_social_answer), FadeIn(takeaway))
        self.pause('4.h.surplus')

        # With the subsidy each side gets a price at which the trade is worthwhile privately.
        added_prices = fixed(VGroup(
            Line([-2.6, detail_y(2.4), 0], [1.9, detail_y(2.4), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(4.4), 0], [1.9, detail_y(4.4), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        added_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(2.4), 0], DOWN, buff=0.06),
            Tex(r'\$2.40', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(2.4), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(4.4), 0], UP, buff=0.06),
            Tex(r'\$4.40', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(4.4), 0], LEFT, buff=0.15))).set_z_index(4)
        added_subsidy = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(2.4), 0], [TAX_LEFT + TAX_WIDTH, detail_y(2.4), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(4.4), 0], [TAX_LEFT, detail_y(4.4), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            VGroup(Tex('subsidy', color=INK).scale(0.42), Tex(r'\$2', color=INK).scale(0.50))
                .arrange(DOWN, buff=0.06).move_to([0, detail_y(3.4), 0]))).set_z_index(3)
        added_policy_guides = fixed(VGroup(
            DashedLine(added_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(2.4), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(2.4), 0], [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=3),
            DashedLine([SELLER_LEFT, detail_y(4.2), 0], [TAX_LEFT + TAX_WIDTH + 0.10, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-3.95, detail_y(4.2), 0], [-4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(4.4), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.2), 0], [-4.25, detail_y(4.4), 0], color=TOTAL, stroke_width=3)))
        added_yes = fixed(VMobject().set_points_as_corners([[-0.26, 0, 0], [-0.07, -0.18, 0], [0.30, 0.26, 0]])
            .set_stroke(GOV, 5).scale(0.85).move_to(added_no))
        self.remove(takeaway)
        self.play(FadeOut(added_private_guides), FadeOut(added_no), FadeOut(added_external), FadeIn(added_prices),
                  FadeIn(added_price_words), FadeIn(added_subsidy), FadeIn(added_policy_guides))
        self.pause('4.h.subsidy')
        takeaway = teaching(r'The \$2 subsidy makes this worthwhile trade happen.')
        self.play(FadeIn(added_yes), FadeIn(takeaway))
        self.pause('4.h.enabled')

        self.remove(detail_people)
        self.play(FadeOut(added_edges), FadeOut(added_values), FadeOut(added_questions),
                  FadeOut(added_prices), FadeOut(added_price_words), FadeOut(added_subsidy), FadeOut(added_policy_guides),
                  FadeOut(added_yes), FadeOut(added_social_guides), FadeOut(added_social_answer),
                  FadeOut(unit_context), FadeOut(takeaway), run_time=0.4)
        self.play(Transform(added_pair, added_home), FadeIn(positive_market), FadeIn(context), run_time=1.6)
        self.remove(added_pair)
        self.pause('4.h.return')

        # ---- 4.i · Welfare with the subsidy, one overlapping region at a time.
        self.remove(takeaway)
        question = teaching('With the subsidy, who gains and who pays?')
        subsidy_cs = fixed(VGroup(*[unit_slice(pax, q, lambda x: 2.4, mb, DEMAND, SURPLUS_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_ps = fixed(VGroup(*[unit_slice(pax, q, mc, lambda x: 4.4, SUPPLY, SURPLUS_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_gov = fixed(VGroup(*[unit_slice(pax, q, lambda x: 2.4, lambda x: 4.4, GOV, GOV_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_words = fixed(VGroup(
            Tex('CS', color=INK).scale(0.72).move_to(pax.c2p(POSITIVE_Q / 3, (12 + 2.4 + 2.4) / 3)),
            Tex('PS', color=INK).scale(0.50).move_to(pax.c2p(POSITIVE_Q / 3, (2 + 4.4 + 4.4) / 3)),
            Tex('Subsidy cost', color=INK).scale(0.58).move_to(pax.c2p(POSITIVE_Q / 2, 3.4))).set_z_index(5))
        self.play(FadeIn(question))
        self.play(FadeIn(subsidy_cs), FadeIn(subsidy_words[0]))
        self.pause('4.i.cs')
        self.play(FadeOut(subsidy_cs), FadeOut(subsidy_words[0]), run_time=0.5)
        self.play(FadeIn(subsidy_ps), FadeIn(subsidy_words[1]))
        self.pause('4.i.ps')
        self.play(FadeOut(subsidy_ps), FadeOut(subsidy_words[1]), run_time=0.5)
        self.remove(question)
        takeaway = teaching(r'Buyers pay $\$2.40$, sellers receive $\$4.40$, and the government pays $\$2$ per unit.')
        self.play(FadeIn(subsidy_gov), FadeIn(subsidy_words[2]), FadeIn(takeaway))
        self.pause('4.i.gov')
        self.remove(takeaway)
        takeaway = teaching('With a subsidy equal to the external benefit, there is no deadweight loss.')
        self.play(FadeOut(subsidy_gov), FadeOut(subsidy_words[2]), FadeIn(takeaway))
        self.pause('4.i')

        # ---- 5.a · End on the corrected market and the same quantity equality as the tax.
        self.remove(takeaway)
        positive_final_graph = fixed(VGroup(*[m for m in self.mobjects if m not in (head, context)]))
        self.remove(*[m for m in self.mobjects if m not in (head, context)])
        self.add(positive_final_graph)
        self.play(positive_final_graph.animate.shift(LEFT * 2.0), run_time=1.2)
        positive_equality = fixed(VGroup(
            Tex(r'$Q^{subsidy}=Q^*$', color=FOCUS).scale(1.05),
            Tex('48 units', color=CAPTION).scale(0.65),
            Tex('Subsidy = external benefit', color=INK).scale(0.65)
        ).arrange(DOWN, buff=0.28).move_to([4.2, 0.7, 0]))
        takeaway = teaching('A corrective subsidy enables worthwhile trades the market would miss.')
        self.play(FadeIn(positive_equality), FadeIn(takeaway))
        self.pause('5.a')
