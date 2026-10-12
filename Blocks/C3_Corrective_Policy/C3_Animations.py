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
# C1's market, Q in tons and dollars per ton, joined to the tax wedge of the old C2 Taxes animation:
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
        STOPPED_TON, KEPT_TON = 36, 24              # Close-ups: one exchange the tax stops, one it keeps.
        BAR_GAP = 0.08
        BASE_OPACITY, SURPLUS_OPACITY, GOV_OPACITY = 0.16, 0.65, 0.5
        DETAIL_BASE, DETAIL_SCALE, KEPT_SCALE = -2.05, 0.68, 0.55
        EXCHANGE_X, CALCULATION_X = -1.9, 4.7
        ORIGIN_X, ORIGIN_Y = -4.6, -2.35

        # The model, as one-line functions of quantity or price.
        mb = lambda q: 12 - q / 5
        mc = lambda q: 2 + q / 20
        msc = lambda q: mc(q) + EXTERNAL
        msb = lambda q: mb(q) + EXTERNAL
        zero = lambda q: 0
        quantity_demanded = lambda p: (12 - p) * 5
        quantity_supplied = lambda p: (p - 2) * 20
        taxed_quantity = lambda t: 40 - 4 * t       # MB - MC = t  ->  10 - Q/4 = t.

        # The two object factories used throughout: the yellow bottom line and one one-ton slice.
        teaching = lambda text: fixed(Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                      .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))

        def ton_slice(axes, q, low, high, color, opacity, right=None):
            left = q + BAR_GAP / 2
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
        ax = style_axes([0, 80, 10], [0, 13, 2], x_length=8.4, y_length=4.3)
        ax.shift(np.array([ORIGIN_X, ORIGIN_Y, 0]) - ax.c2p(0, 0))
        fixed(ax)
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), UP, buff=0.18),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(80, 0), DOWN, buff=0.23),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(ax.c2p(80, 0), DOWN, buff=0.73),
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
        cost_bars, ext_bars = fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            cost_bars.add(ton_slice(ax, q, zero, mc, SUPPLY, BASE_OPACITY))
        for q in range(60):
            ext_bars.add(ton_slice(ax, q, mc, msc, EXT, SURPLUS_OPACITY if q < MARKET_Q else 0.12))
        market_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(10))
        market_quantity = fixed(VGroup(
            DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            Tex(r'$\hat{Q}=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20)).set_z_index(10))
        market_price = fixed(VGroup(
            Tex(r'$\hat{P}=$', color=GUIDE).scale(0.7).next_to(msc_intercept, LEFT, buff=0.12),
            DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        efficient_marker = fixed(VGroup(
            DashedLine(ax.c2p(32, 0), ax.c2p(32, 5.6), color=FOCUS, stroke_width=2),
            Dot(ax.c2p(32, 5.6), radius=0.085, color=FOCUS)).set_z_index(11))
        efficient_word = fixed(Tex(r'$Q^*=32$', color=FOCUS).scale(0.7).next_to(ax.c2p(32, 0), DOWN, buff=0.78))
        dwl_bars = fixed(VGroup(*[ton_slice(ax, q, mb, msc, DWL, 0.8) for q in range(EFFICIENT_Q, MARKET_Q)]).set_z_index(1))
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(40, 5.4), RIGHT, buff=0.3))
        recap = teaching('Last time: the market exchanges 40 tons, but only 32 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(msc_intercept),
                  FadeIn(cost_bars), FadeIn(ext_bars), FadeIn(demand), FadeIn(supply), FadeIn(social_cost),
                  FadeIn(curve_words), FadeIn(market_dot), FadeIn(market_quantity), FadeIn(market_price))
        self.play(FadeIn(efficient_marker), FadeIn(efficient_word), FadeIn(dwl_bars), FadeIn(dwl_word), FadeIn(recap))
        self.pause('1.a')

        # ---- 2.a · The planner wants 32 tons; which price gets both sides there?
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, 'Someone who wants the efficient quantity, 32 tons.'))
        question = teaching('What price gets buyers and sellers to exchange 32 tons?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(market_price), FadeOut(msc_intercept),
                  FadeOut(market_quantity), FadeOut(efficient_word), FadeOut(dwl_word))
        self.pause('2.a')

        # ---- 2.b · Set the price at the buyers' willingness to pay for ton 32: an excess.
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
        buyer_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(12))
        buyer_dot.add_updater(lambda m: m.move_to(ax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(12))
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
        gap_word = fixed(Tex(r'\textsf{excess: 40 tons}', color=CAPTION).scale(0.55).next_to(gap_line, UP, buff=0.12))
        for m in readouts:
            m.update()   # Digits must already match before a number fades in.
        self.remove(question)
        question = teaching(r'At $\$5.60$, buyers want 32 tons but sellers offer 72: an excess of 40.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_prefix), FadeIn(seller_number), FadeIn(seller_prefix),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('2.b')

        # ---- 2.c · Set the price at the sellers' willingness to sell ton 32: a shortage.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(3.6), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{shortage: 10 tons}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=0.12))
        question = teaching(r'At $\$3.60$, sellers offer 32 tons but buyers want 42: a shortage of 10.')
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
        takeaway = teaching(r'No single price works: buyers must pay $\$5.60$ while sellers receive $\$3.60$.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_prefix),
                  FadeOut(seller_number), FadeOut(seller_prefix), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price), FadeIn(market_dot), FadeIn(efficient_word),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('2.d')

        # ---- 2.e · That gap is the external cost per ton.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external cost per ton.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('2.e')

        # ---- 3.a · A $2 tax: the wedge slides in from the left until it is stuck between MC and MB.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Taxes'))
        context = fixed(subtitle(head, 'A tax equal to the external cost per ton.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        wedge_x = ValueTracker(-14)
        wedge = fixed(VGroup(
            Line(ax.c2p(-14, 3.6), ax.c2p(-14, 5.6), color=GOV, stroke_width=6),
            Line(ax.c2p(-14, 3.6) + LEFT * 0.09, ax.c2p(-14, 3.6) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(ax.c2p(-14, 5.6) + LEFT * 0.09, ax.c2p(-14, 5.6) + RIGHT * 0.09, color=GOV, stroke_width=3)).set_z_index(12))
        wedge.add_updater(lambda m: m.move_to(ax.c2p(wedge_x.get_value(), 4.6)))
        wedge_word = fixed(Tex(r'\$2 tax', color=GOV).scale(0.6))
        wedge_word.add_updater(lambda m: m.next_to(wedge, UP, buff=0.6))
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
            DashedLine(ax.c2p(32, 0), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2),
            Tex('$Q=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(32, 0), DOWN, buff=0.20)).set_z_index(10))
        self.remove(takeaway)
        takeaway = teaching('The wedge gets stuck at 32 tons, the efficient quantity.')
        self.play(FadeIn(tax_prices), FadeIn(takeaway))
        self.pause('3.a')

        # ---- 3.b · The exchanges past 32 stop, and their deadweight loss with them.
        self.remove(takeaway)
        takeaway = teaching('Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.')
        self.play(*[cost_bars[q].animate.set_fill(opacity=0.05) for q in range(EFFICIENT_Q, MARKET_Q)],
                  *[ext_bars[q].animate.set_fill(opacity=0.12) for q in range(EFFICIENT_Q, MARKET_Q)],
                  FadeOut(dwl_bars), FadeIn(takeaway))
        self.pause('3.b')

        # ---- 3.c · Welfare with the tax: PS, then CS, then the government's revenue.
        self.remove(takeaway)
        question = teaching('With the tax, who gains and who pays?')
        ps_fill = fixed(VGroup(*[ton_slice(ax, q, mc, lambda x: 3.6, SUPPLY, SURPLUS_OPACITY) for q in range(EFFICIENT_Q)]))
        cs_fill = fixed(VGroup(*[ton_slice(ax, q, lambda x: 5.6, mb, DEMAND, SURPLUS_OPACITY) for q in range(EFFICIENT_Q)]))
        gov_fill = fixed(VGroup(*[ton_slice(ax, q, lambda x: 3.6, lambda x: 5.6, GOV, GOV_OPACITY) for q in range(EFFICIENT_Q)]))
        # Each label sits at the centroid of its own region.
        welfare_words = fixed(VGroup(
            Tex('PS', color=INK).scale(0.72).move_to(ax.c2p(EFFICIENT_Q / 3, (2 + 3.6 + 3.6) / 3)),
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(EFFICIENT_Q / 3, (12 + 5.6 + 5.6) / 3)),
            Tex('Tax revenue', color=INK).scale(0.72).move_to(ax.c2p(EFFICIENT_Q / 2, 4.6))).set_z_index(5))
        self.play(*[ext_bars[q].animate.set_fill(opacity=0.12) for q in range(EFFICIENT_Q)], FadeIn(question))
        self.play(FadeIn(ps_fill), FadeIn(welfare_words[0]))
        self.play(FadeIn(cs_fill), FadeIn(welfare_words[1]))
        self.remove(question)
        takeaway = teaching(r'Buyers pay $\$5.60$, sellers receive $\$3.60$, and the government collects $\$2$ per ton.')
        self.play(FadeIn(gov_fill), FadeIn(welfare_words[2]), FadeIn(takeaway))
        self.pause('3.c')

        # ---- 3.d · The corrective result.
        self.remove(takeaway)
        takeaway = teaching('With a tax equal to the external cost, there is no deadweight loss.')
        self.play(FadeIn(takeaway))
        self.pause('3.d')
        # From here the market fades and returns as one group around the close-ups.
        market = fixed(VGroup(ax, axis_words, cost_bars, ext_bars, demand, supply, social_cost, curve_words,
                             market_dot, efficient_marker, efficient_word, wedge, wedge_word, tax_prices,
                             ps_fill, cs_fill, gov_fill, welfare_words))
        self.remove(*[m for m in self.mobjects if m not in (head, context, takeaway)])
        self.add(market)

        # The canonical close-up people: buyer and seller spheres, one grey bystander between them.
        detail_people = fixed(Group())
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            detail_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([x + EXCHANGE_X, DETAIL_BASE - 0.60, 0])))
            detail_people.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x + EXCHANGE_X, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            detail_people.add(fixed(Tex('Buyer' if color == DEMAND else 'Seller', color=INK)
                .scale(0.65).move_to([x + EXCHANGE_X, DETAIL_BASE - 0.94, 0])))
        bystander = fixed(Group(
            Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=MUTED, fill_opacity=0.28)
                .move_to([EXCHANGE_X, DETAIL_BASE - 0.60, 0]),
            Sphere(radius=0.18, color=MUTED, opacity=1, resolution=(32, 24))
                .move_to([EXCHANGE_X, DETAIL_BASE - 0.35, 0])))
        bystander[1].apply_depth_test()
        bystander_word = fixed(Tex('Bystanders', color=CAPTION).scale(0.65).move_to([EXCHANGE_X, DETAIL_BASE - 0.94, 0]))

        # ---- 3.e.select · Ton 36: an exchange the tax stops. Select it from the market slices.
        q = STOPPED_TON - 1
        stopped_pair = fixed(VGroup(
            ton_slice(ax, q, zero, mb, DEMAND, 0),
            ton_slice(ax, q, zero, mc, SUPPLY, BASE_OPACITY),
            ton_slice(ax, q, mc, msc, EXT, SURPLUS_OPACITY)))
        stopped_home = stopped_pair.copy()
        stopped_box = fixed(SurroundingRectangle(stopped_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        self.play(FadeIn(stopped_pair), FadeIn(stopped_box))
        self.pause('3.e.select')

        # ---- 3.e.values · The close-up: MB 4.80, MC 3.80, EXT 2 on top reaching MSC 5.80.
        stopped_target = fixed(VGroup())
        for left, low, high, color, opacity in [(-1.16, 0, 4.8, DEMAND, BASE_OPACITY),
                                               (0.06, 0, 3.8, SUPPLY, BASE_OPACITY),
                                               (0.06, 3.8, 5.8, EXT, SURPLUS_OPACITY)]:
            stopped_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=opacity)))
        stopped_target.shift(RIGHT * EXCHANGE_X)
        self.play(FadeOut(market), FadeOut(context), FadeOut(stopped_box),
                  Transform(stopped_pair, stopped_target), run_time=1.6)
        stopped_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(stopped_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([EXCHANGE_X - 1.3, DETAIL_BASE, 0], [EXCHANGE_X + 1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$4.80$', color=DEMAND).scale(0.72).next_to(stopped_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$3.80$', color=SUPPLY).scale(0.72).next_to(stopped_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'EXT $\$2$', color=EXT).scale(0.72).next_to(stopped_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$5.80$', color=SUPPLY).scale(0.72).next_to(stopped_target[2].get_corner(UR), RIGHT, buff=0.25)))
        stopped_labels[4].bars = stopped_labels[5].bars = stopped_pair
        stopped_labels[4].add_updater(lambda m: m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        stopped_labels[5].add_updater(lambda m: m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head, 'The 36th unit: an exchange the tax stops.'))
        self.add(detail_people, bystander, bystander_word)
        self.play(FadeIn(stopped_labels), FadeIn(unit_context))
        self.pause('3.e.values')

        # ---- 3.e.external · The bystanders' cost sits outside the private decision.
        private_note = teaching('Buyers and sellers only consider their private costs and benefits.')
        cost_heading = fixed(Tex('Externalized cost per ton', color=CAPTION).scale(0.65).move_to([CALCULATION_X, 1.45, 0]))
        cost_number = fixed(Tex(r'$\$2$', color=EXT).scale(0.75).move_to([CALCULATION_X, 0.85, 0]))
        self.play(FadeOut(stopped_labels[2]), FadeOut(stopped_labels[6]), FadeOut(stopped_labels[7]),
                  FadeOut(bystander_word), run_time=0.3)
        self.play(Transform(stopped_pair[2], stopped_pair[2].copy().move_to([CALCULATION_X, -0.72, 0]), path_arc=-PI / 2),
                  Transform(bystander, bystander.copy().shift(RIGHT * (CALCULATION_X - EXCHANGE_X)), path_arc=PI / 4),
                  FadeIn(private_note), run_time=1.4)
        bystander_word.shift(RIGHT * (CALCULATION_X - EXCHANGE_X))
        self.play(FadeIn(cost_heading), FadeIn(cost_number), FadeIn(bystander_word), run_time=0.4)
        self.pause('3.e.external')

        # ---- 3.e.tax · The seller now owes $2 on the sale: MC + Tax.
        stopped_tax = fixed(Polygon(
            [EXCHANGE_X + 0.06, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], [EXCHANGE_X + 1.16, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0],
            [EXCHANGE_X + 1.16, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], [EXCHANGE_X + 0.06, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY))
        stopped_tax_labels = fixed(VGroup(
            Line(stopped_tax.get_corner(UL), stopped_tax.get_corner(UR), color=SUPPLY, stroke_width=3),
            Tex(r'Tax $\$2$', color=GOV).scale(0.72).next_to(stopped_tax, RIGHT, buff=0.25),
            VGroup(Tex('MC', color=SUPPLY), Tex('$+$', color=INK), Tex('Tax', color=GOV), Tex(r'$\$5.80$', color=SUPPLY))
                .arrange(RIGHT, buff=0.1).scale(0.72).next_to(stopped_tax.get_corner(UR), RIGHT, buff=0.25)))
        self.remove(private_note)
        takeaway = teaching(r'With the tax, the seller needs at least $\$5.80$ to sell this ton.')
        self.play(FadeIn(stopped_tax), FadeIn(stopped_tax_labels), FadeIn(takeaway))
        self.pause('3.e.tax')

        # ---- 3.e.question · The C1 question, now with the tax in place.
        self.remove(takeaway)
        takeaway = teaching('Is there a price that would make this exchange work?')
        self.play(FadeIn(takeaway))
        self.pause('3.e.question')

        # ---- 3.e.answer · No price reaches from $5.80 down to $4.80.
        self.remove(takeaway)
        takeaway = teaching(r'No price works: the buyer pays at most $\$4.80$ but the seller needs $\$5.80$.')
        stopped_rule = fixed(VGroup(Tex('MB', color=DEMAND), Tex('$<$', color=INK), Tex('MC', color=SUPPLY),
                                    Tex('$+$', color=INK), Tex('Tax', color=GOV))
                             .arrange(RIGHT, buff=0.1).scale(0.8).move_to([EXCHANGE_X - 3.5, 0.2, 0]))
        self.play(FadeIn(stopped_rule), FadeIn(takeaway))
        self.pause('3.e.answer')

        # ---- 3.e · Stopping the exchange eliminates its deadweight loss.
        stopped_dwl = fixed(Polygon(
            [EXCHANGE_X + 0.06, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [EXCHANGE_X + 1.16, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
            [EXCHANGE_X + 1.16, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], [EXCHANGE_X + 0.06, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        GAP_X = EXCHANGE_X - 3.1
        stopped_gap = fixed(VGroup(
            DashedLine([GAP_X + 0.18, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [GAP_X, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                       color=DWL, stroke_width=1.6),
            DashedLine([EXCHANGE_X + 0.06, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], [GAP_X, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
                       color=DWL, stroke_width=1.6),
            Line([GAP_X, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [GAP_X, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
                 color=DWL, stroke_width=3),
            VGroup(Tex(r'TS $=-\$1$', color=TOTAL), Tex(r'DWL $=\$1$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=RIGHT).scale(0.8)
                .next_to([GAP_X, DETAIL_BASE + 5.3 * DETAIL_SCALE, 0], LEFT, buff=0.3)))
        self.remove(takeaway)
        takeaway = teaching(r'The tax stops this exchange and eliminates $\$1$ of deadweight loss.')
        self.play(FadeOut(stopped_rule), run_time=0.3)
        self.play(FadeIn(stopped_dwl), FadeIn(stopped_gap), FadeIn(takeaway))
        self.pause('3.e')

        # ---- 3.e.return · The same pair goes back to its market slice.
        self.remove(detail_people, bystander, bystander_word)
        self.play(FadeOut(stopped_labels, suspend_mobject_updating=False), FadeOut(stopped_tax), FadeOut(stopped_tax_labels),
                  FadeOut(stopped_dwl), FadeOut(stopped_gap), FadeOut(takeaway), FadeOut(unit_context),
                  FadeOut(cost_heading), FadeOut(cost_number),
                  Transform(stopped_pair, stopped_home), FadeIn(market), FadeIn(context), run_time=1.6)
        self.play(FadeOut(stopped_pair))
        self.pause('3.e.return')
        bystander.shift(LEFT * (CALCULATION_X - EXCHANGE_X))
        bystander_word.shift(LEFT * (CALCULATION_X - EXCHANGE_X))

        # ---- 3.f.select · Ton 24: an exchange the tax keeps.
        q = KEPT_TON - 1
        kept_pair = fixed(VGroup(
            ton_slice(ax, q, zero, mb, DEMAND, 0),
            ton_slice(ax, q, zero, mc, SUPPLY, BASE_OPACITY),
            ton_slice(ax, q, mc, msc, EXT, SURPLUS_OPACITY)))
        kept_home = kept_pair.copy()
        kept_box = fixed(SurroundingRectangle(kept_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(kept_pair), FadeIn(kept_box))
        self.pause('3.f.select')

        # ---- 3.f.values · MB 7.20, MC 3.20, EXT 2 reaching MSC 5.20, on the smaller common scale.
        kept_target = fixed(VGroup())
        for left, low, high, color, opacity in [(-1.16, 0, 7.2, DEMAND, BASE_OPACITY),
                                               (0.06, 0, 3.2, SUPPLY, BASE_OPACITY),
                                               (0.06, 3.2, 5.2, EXT, SURPLUS_OPACITY)]:
            kept_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * KEPT_SCALE, 0], [left + 1.1, DETAIL_BASE + low * KEPT_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * KEPT_SCALE, 0], [left, DETAIL_BASE + high * KEPT_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=opacity)))
        kept_target.shift(RIGHT * EXCHANGE_X)
        self.play(FadeOut(market), FadeOut(context), FadeOut(kept_box),
                  Transform(kept_pair, kept_target), run_time=1.6)
        kept_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(kept_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([EXCHANGE_X - 1.3, DETAIL_BASE, 0], [EXCHANGE_X + 1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$7.20$', color=DEMAND).scale(0.72).next_to(kept_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$3.20$', color=SUPPLY).scale(0.72).next_to(kept_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'EXT $\$2$', color=EXT).scale(0.72).next_to(kept_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$5.20$', color=SUPPLY).scale(0.72).next_to(kept_target[2].get_corner(UR), RIGHT, buff=0.25)))
        kept_labels[4].bars = kept_labels[5].bars = kept_pair
        kept_labels[4].add_updater(lambda m: m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        kept_labels[5].add_updater(lambda m: m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head, 'The 24th unit: an exchange the tax keeps.'))
        self.add(detail_people, bystander, bystander_word)
        self.play(FadeIn(kept_labels), FadeIn(unit_context))
        self.pause('3.f.values')

        # ---- 3.f.external · Set the bystanders' cost aside again.
        private_note = teaching('Buyers and sellers only consider their private costs and benefits.')
        self.play(FadeOut(kept_labels[2]), FadeOut(kept_labels[6]), FadeOut(kept_labels[7]),
                  FadeOut(bystander_word), run_time=0.3)
        self.play(Transform(kept_pair[2], kept_pair[2].copy().move_to([CALCULATION_X, -0.72, 0]), path_arc=-PI / 2),
                  Transform(bystander, bystander.copy().shift(RIGHT * (CALCULATION_X - EXCHANGE_X)), path_arc=PI / 4),
                  FadeIn(private_note), run_time=1.4)
        bystander_word.shift(RIGHT * (CALCULATION_X - EXCHANGE_X))
        self.play(FadeIn(cost_heading), FadeIn(cost_number), FadeIn(bystander_word), run_time=0.4)
        self.pause('3.f.external')

        # ---- 3.f.tax · MC + Tax = $5.20 for this seller.
        kept_tax = fixed(Polygon(
            [EXCHANGE_X + 0.06, DETAIL_BASE + 3.2 * KEPT_SCALE, 0], [EXCHANGE_X + 1.16, DETAIL_BASE + 3.2 * KEPT_SCALE, 0],
            [EXCHANGE_X + 1.16, DETAIL_BASE + 5.2 * KEPT_SCALE, 0], [EXCHANGE_X + 0.06, DETAIL_BASE + 5.2 * KEPT_SCALE, 0],
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY))
        kept_tax_labels = fixed(VGroup(
            Line(kept_tax.get_corner(UL), kept_tax.get_corner(UR), color=SUPPLY, stroke_width=3),
            Tex(r'Tax $\$2$', color=GOV).scale(0.72).next_to(kept_tax, RIGHT, buff=0.25),
            VGroup(Tex('MC', color=SUPPLY), Tex('$+$', color=INK), Tex('Tax', color=GOV), Tex(r'$\$5.20$', color=SUPPLY))
                .arrange(RIGHT, buff=0.1).scale(0.72).next_to(kept_tax.get_corner(UR), RIGHT, buff=0.25)))
        self.remove(private_note)
        takeaway = teaching(r'With the tax, the seller needs at least $\$5.20$ to sell this ton.')
        self.play(FadeIn(kept_tax), FadeIn(kept_tax_labels), FadeIn(takeaway))
        self.pause('3.f.tax')

        # ---- 3.f.question
        self.remove(takeaway)
        takeaway = teaching('Is there a price that would make this exchange work?')
        self.play(FadeIn(takeaway))
        self.pause('3.f.question')

        # ---- 3.f.answer · Any price between $5.20 and $7.20 works, so the exchange continues.
        self.remove(takeaway)
        takeaway = teaching(r"Yes: the buyer's $\$7.20$ covers the seller's $\$5.20$, so this exchange continues.")
        kept_rule = fixed(VGroup(Tex('MB', color=DEMAND), Tex('$>$', color=INK), Tex('MC', color=SUPPLY),
                                 Tex('$+$', color=INK), Tex('Tax', color=GOV))
                          .arrange(RIGHT, buff=0.1).scale(0.8).move_to([EXCHANGE_X - 3.5, 0.2, 0]))
        self.play(FadeIn(kept_rule), FadeIn(takeaway))
        self.pause('3.f.answer')

        # ---- 3.f.social · Count the bystanders again: MB still exceeds MSC.
        self.play(FadeOut(kept_rule), FadeOut(kept_tax), FadeOut(kept_tax_labels), FadeOut(takeaway),
                  FadeOut(cost_heading), FadeOut(cost_number), FadeOut(bystander_word), run_time=0.3)
        self.play(Transform(kept_pair[2], kept_target[2], path_arc=PI / 2),
                  Transform(bystander, bystander.copy().shift(LEFT * (CALCULATION_X - EXCHANGE_X)), path_arc=-PI / 4),
                  run_time=1.4)
        bystander_word.shift(LEFT * (CALCULATION_X - EXCHANGE_X))
        takeaway = teaching('Counting the bystanders, this exchange is still worthwhile: MB exceeds MSC.')
        self.play(FadeIn(kept_labels[2]), FadeIn(kept_labels[6]), FadeIn(kept_labels[7]), FadeIn(bystander_word),
                  FadeIn(takeaway), run_time=0.4)
        self.pause('3.f.social')

        # ---- 3.f · The exchange's gain to society: TS = $2, no deadweight loss.
        kept_gain = fixed(Polygon(
            [EXCHANGE_X - 1.16, DETAIL_BASE + 5.2 * KEPT_SCALE, 0], [EXCHANGE_X - 0.06, DETAIL_BASE + 5.2 * KEPT_SCALE, 0],
            [EXCHANGE_X - 0.06, DETAIL_BASE + 7.2 * KEPT_SCALE, 0], [EXCHANGE_X - 1.16, DETAIL_BASE + 7.2 * KEPT_SCALE, 0],
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY))
        kept_gap = fixed(VGroup(
            DashedLine([GAP_X + 0.18, DETAIL_BASE + 7.2 * KEPT_SCALE, 0], [GAP_X, DETAIL_BASE + 7.2 * KEPT_SCALE, 0],
                       color=TOTAL, stroke_width=1.6),
            DashedLine([EXCHANGE_X + 0.06, DETAIL_BASE + 5.2 * KEPT_SCALE, 0], [GAP_X, DETAIL_BASE + 5.2 * KEPT_SCALE, 0],
                       color=TOTAL, stroke_width=1.6),
            Line([GAP_X, DETAIL_BASE + 5.2 * KEPT_SCALE, 0], [GAP_X, DETAIL_BASE + 7.2 * KEPT_SCALE, 0],
                 color=TOTAL, stroke_width=3),
            VGroup(Tex(r'TS $=\$2$', color=TOTAL), Tex(r'DWL $=\$0$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=RIGHT).scale(0.8)
                .next_to([GAP_X, DETAIL_BASE + 6.2 * KEPT_SCALE, 0], LEFT, buff=0.3)))
        self.play(FadeIn(kept_gain), FadeIn(kept_gap))
        self.pause('3.f')

        # ---- 3.f.return
        self.remove(detail_people, bystander, bystander_word)
        self.play(FadeOut(kept_labels, suspend_mobject_updating=False), FadeOut(kept_gain), FadeOut(kept_gap),
                  FadeOut(takeaway), FadeOut(unit_context),
                  Transform(kept_pair, kept_home), FadeIn(market), FadeIn(context), run_time=1.6)
        self.play(FadeOut(kept_pair))
        self.pause('3.f.return')

        # ---- 3.g · Dial the tax: everything tax-dependent hangs on one tracker.
        tax = ValueTracker(EXTERNAL)
        taxed_q = lambda: taxed_quantity(tax.get_value())
        buyer_pays = lambda: mb(taxed_quantity(tax.get_value()))
        seller_gets = lambda: mc(taxed_quantity(tax.get_value()))
        wedge[0].add_updater(lambda m: m.put_start_and_end_on(ax.c2p(taxed_q(), seller_gets()), ax.c2p(taxed_q(), buyer_pays())))
        wedge[1].add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), seller_gets())))
        wedge[2].add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), buyer_pays())))
        live_top_dot = fixed(Dot(ax.c2p(32, 5.6), radius=0.07, color=GUIDE).set_z_index(10))
        live_top_dot.add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), buyer_pays())))
        live_bottom_dot = fixed(Dot(ax.c2p(32, 3.6), radius=0.07, color=GUIDE).set_z_index(10))
        live_bottom_dot.add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), seller_gets())))
        live_tax_number = fixed(DecimalNumber(EXTERNAL, num_decimal_places=2, color=GOV).scale(0.6))
        live_tax_number.add_updater(lambda m: fixed(m.set_value(tax.get_value())).next_to(wedge, UP, buff=0.6).shift(LEFT * 0.12))
        live_tax_prefix = fixed(Tex(r'\$', color=GOV).scale(0.6))
        live_tax_prefix.add_updater(lambda m: m.next_to(live_tax_number, LEFT, buff=0.02))
        live_tax_suffix = fixed(Tex('tax', color=GOV).scale(0.6))
        live_tax_suffix.add_updater(lambda m: m.next_to(live_tax_number, RIGHT, buff=0.08))
        live_buyer_line = fixed(DashedLine(ax.c2p(0, 5.6), ax.c2p(32, 5.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_buyer_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, buyer_pays()), ax.c2p(taxed_q(), buyer_pays())))
        live_seller_line = fixed(DashedLine(ax.c2p(0, 3.6), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_seller_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, seller_gets()), ax.c2p(taxed_q(), seller_gets())))
        live_drop = fixed(DashedLine(ax.c2p(32, 0), ax.c2p(32, 3.6), color=GUIDE, stroke_width=2).set_z_index(10))
        live_drop.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(taxed_q(), 0), ax.c2p(taxed_q(), seller_gets())))
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
        # Fills follow the traded tons, including a partial last ton while the tax rolls.
        live_ps, live_cs, live_gov = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            for group, low, high, color, opacity in [
                    (live_ps, mc, lambda x: seller_gets(), SUPPLY, SURPLUS_OPACITY),
                    (live_cs, lambda x: buyer_pays(), mb, DEMAND, SURPLUS_OPACITY),
                    (live_gov, lambda x: seller_gets(), lambda x: buyer_pays(), GOV, GOV_OPACITY)]:
                piece = ton_slice(ax, q, low, high, color, opacity if q < EFFICIENT_Q else 0)
                piece.add_updater(lambda m, q=q, low=low, high=high, color=color, opacity=opacity: m.become(
                    ton_slice(ax, q, low, high, color, opacity if q + BAR_GAP / 2 < taxed_q() else 0,
                              right=min(q + 1 - BAR_GAP / 2, max(taxed_q(), q + BAR_GAP / 2 + 1e-6)))))
                group.add(piece)
        for q in range(MARKET_Q):
            cost_bars[q].add_updater(lambda m, q=q: m.set_fill(opacity=BASE_OPACITY if q + 1 <= taxed_q() + 1e-6 else 0.05))
        # Grey one-ton losses: traded tons past 32 (MB below MSC) or forgone tons short of 32 (MB above MSC).
        live_dwl = fixed(VGroup())
        for q in range(taxed_quantity(4), MARKET_Q):
            bar = ton_slice(ax, q, mb, msc, DWL, 0).set_z_index(1)
            bar.add_updater(lambda m, q=q: m.set_fill(opacity=0.8 if (
                (q >= EFFICIENT_Q and q + 1 <= taxed_q() + 1e-6) or (q < EFFICIENT_Q and q >= taxed_q() - 1e-6)) else 0))
            live_dwl.add(bar)
        live_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8))
        # Right of the traded tons when the tax is small; above the curves past Q-star when it is large.
        live_dwl_word.add_updater(lambda m: m.move_to(
            ax.c2p(taxed_q() + 2.5, (mb(taxed_q()) + msc(taxed_q())) / 2) if taxed_q() >= EFFICIENT_Q
            else ax.c2p(EFFICIENT_Q + 2, mb(EFFICIENT_Q) + 0.9))
            .set_opacity(1 if abs(taxed_q() - EFFICIENT_Q) >= 1 else 0))
        live = [wedge, live_top_dot, live_bottom_dot, live_tax_number, live_tax_prefix, live_tax_suffix,
                live_buyer_line, live_seller_line, live_drop,
                live_buyer_number, live_buyer_prefix, live_seller_number, live_seller_prefix,
                live_q_number, live_q_prefix, live_ps, live_cs, live_gov, live_dwl, live_dwl_word]
        for m in live:
            m.update()
        market.remove(wedge_word, tax_prices, ps_fill, cs_fill, gov_fill)
        self.remove(wedge_word, tax_prices, ps_fill, cs_fill, gov_fill)
        self.add(*live)
        question = teaching('What if the tax is smaller than the external cost?')
        self.play(FadeIn(question))
        self.play(tax.animate.set_value(1), run_time=2.2, rate_func=smooth)
        self.remove(question)
        takeaway = teaching('A smaller tax leaves some harmful exchanges in place.')
        self.play(FadeIn(takeaway))
        self.pause('3.g.low')
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
        takeaway = teaching(r'The corrective tax equals the external cost: $\$2$ per ton.')
        self.play(FadeIn(takeaway))
        self.pause('3.g')

        # ---- 4.a · Last time: the positive-externality market and its deadweight loss.
        for m in self.mobjects:
            m.clear_updaters()
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        self.clear()
        head = fixed(title('Positive Externalities'))
        context = fixed(subtitle(head, 'A benefit received by others outside the market.'))
        pax = style_axes([0, 80, 10], [0, 15, 2], x_length=8.4, y_length=4.3)
        pax.shift(np.array([ORIGIN_X, ORIGIN_Y, 0]) - pax.c2p(0, 0))
        fixed(pax)
        positive_axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(pax.c2p(0, 15), LEFT, buff=0.23),
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(pax.c2p(0, 15), UP, buff=0.18),
            Tex('Q', color=INK).scale(0.8).next_to(pax.c2p(80, 0), DOWN, buff=0.23),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(pax.c2p(80, 0), DOWN, buff=0.73),
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
        positive_cost_bars, positive_ext_bars = fixed(VGroup()), fixed(VGroup())
        for q in range(60):
            positive_cost_bars.add(ton_slice(pax, q, zero, mc, SUPPLY, BASE_OPACITY if q < MARKET_Q else 0.04))
            positive_ext_bars.add(ton_slice(pax, q, mb, msb, EXT, SURPLUS_OPACITY if q < MARKET_Q else 0.12))
        positive_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(10))
        positive_quantity = fixed(VGroup(
            DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2),
            Tex(r'$\hat{Q}=40$', color=GUIDE).scale(0.7).next_to(pax.c2p(40, 0), DOWN, buff=0.20)).set_z_index(10))
        positive_price = fixed(VGroup(
            Tex(r'$\hat{P}=4$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 4), LEFT, buff=0.2),
            DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        positive_efficient = fixed(VGroup(
            DashedLine(pax.c2p(48, 0), pax.c2p(48, 4.4), color=FOCUS, stroke_width=2),
            Dot(pax.c2p(48, 4.4), radius=0.085, color=FOCUS)).set_z_index(11))
        positive_efficient_word = fixed(Tex(r'$Q^*=48$', color=FOCUS).scale(0.7).next_to(pax.c2p(48, 0), DOWN, buff=0.78))
        positive_dwl = fixed(VGroup(*[ton_slice(pax, q, mc, msb, DWL, 0.8) for q in range(MARKET_Q, POSITIVE_Q)]).set_z_index(1))
        positive_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(positive_dwl, UP, buff=0.16))
        recap = teaching('Last time: the market exchanges 40 tons, but 48 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(pax), FadeIn(positive_axis_words), FadeIn(positive_cost_bars),
                  FadeIn(positive_ext_bars), FadeIn(positive_demand), FadeIn(positive_supply), FadeIn(social_benefit),
                  FadeIn(positive_curve_words), FadeIn(positive_dot), FadeIn(positive_quantity), FadeIn(positive_price))
        self.play(FadeIn(positive_efficient), FadeIn(positive_efficient_word), FadeIn(positive_dwl), FadeIn(positive_dwl_word), FadeIn(recap))
        self.pause('4.a')

        # ---- 4.b · The planner wants 48 tons.
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, 'Someone who wants the efficient quantity, 48 tons.'))
        question = teaching('What price gets buyers and sellers to exchange 48 tons?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(positive_price), FadeOut(positive_axis_words[4]),
                  FadeOut(positive_quantity), FadeOut(positive_efficient_word), FadeOut(positive_dwl_word))
        positive_axis_words.remove(positive_axis_words[4])
        self.pause('4.b')

        # ---- 4.c · The buyers' willingness to pay for ton 48: a shortage.
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
        buyer_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(12))
        buyer_dot.add_updater(lambda m: m.move_to(pax.c2p(quantity_demanded(price.get_value()), price.get_value())))
        seller_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=GUIDE).set_z_index(12))
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
        gap_word = fixed(Tex(r'\textsf{shortage: 40 tons}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=0.12))
        for m in readouts:
            m.update()
        self.remove(question)
        question = teaching(r'At $\$2.40$, buyers want 48 tons but sellers offer 8: a shortage of 40.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_prefix), FadeIn(seller_number), FadeIn(seller_prefix),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('4.c')

        # ---- 4.d · The sellers' willingness to sell ton 48: an excess.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(4.4), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{excess: 10 tons}', color=CAPTION).scale(0.55).next_to(gap_line, UP, buff=0.12))
        question = teaching(r'At $\$4.40$, sellers offer 48 tons but buyers want 38: an excess of 10.')
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
        takeaway = teaching(r'No single price works: sellers must receive $\$4.40$ while buyers pay $\$2.40$.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_prefix),
                  FadeOut(seller_number), FadeOut(seller_prefix), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price), FadeIn(positive_dot), FadeIn(positive_efficient_word),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('4.e')

        # ---- 4.f · That gap is the external benefit per ton.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external benefit per ton.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('4.f')

        # ---- 4.g · A $2 subsidy: the wedge slides in from the right, as in C2, and is stuck at 48.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Subsidies'))
        context = fixed(subtitle(head, 'A subsidy equal to the external benefit per ton.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        wedge_x = ValueTracker(66)
        subsidy_wedge = fixed(VGroup(
            Line(pax.c2p(66, 2.4), pax.c2p(66, 4.4), color=GOV, stroke_width=6),
            Line(pax.c2p(66, 2.4) + LEFT * 0.09, pax.c2p(66, 2.4) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(pax.c2p(66, 4.4) + LEFT * 0.09, pax.c2p(66, 4.4) + RIGHT * 0.09, color=GOV, stroke_width=3)).set_z_index(12))
        subsidy_wedge.add_updater(lambda m: m.move_to(pax.c2p(wedge_x.get_value(), 3.4)))
        subsidy_word = fixed(Tex(r'\$2 subsidy', color=GOV).scale(0.6))
        subsidy_word.add_updater(lambda m: m.next_to(subsidy_wedge, UP, buff=0.6))
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
            DashedLine(pax.c2p(48, 0), pax.c2p(48, 2.4), color=GUIDE, stroke_width=2),
            Tex('$Q=48$', color=GUIDE).scale(0.7).next_to(pax.c2p(48, 0), DOWN, buff=0.20)).set_z_index(10))
        self.remove(takeaway)
        takeaway = teaching('The wedge gets stuck at 48 tons, the efficient quantity.')
        self.play(FadeIn(subsidy_prices), FadeIn(takeaway))
        self.pause('4.g')

        # ---- 4.h · Tons 41 to 48 now happen, and their deadweight loss is gone.
        self.remove(takeaway)
        takeaway = teaching('Exchanges 41 through 48 now happen, so their deadweight loss is gone.')
        self.play(*[positive_cost_bars[q].animate.set_fill(opacity=BASE_OPACITY) for q in range(MARKET_Q, POSITIVE_Q)],
                  *[positive_ext_bars[q].animate.set_fill(opacity=SURPLUS_OPACITY) for q in range(MARKET_Q, POSITIVE_Q)],
                  FadeOut(positive_dwl), FadeIn(takeaway))
        self.pause('4.h')

        # ---- 4.i · Welfare with the subsidy, one overlapping region at a time.
        self.remove(takeaway)
        question = teaching('With the subsidy, who gains and who pays?')
        subsidy_cs = fixed(VGroup(*[ton_slice(pax, q, lambda x: 2.4, mb, DEMAND, SURPLUS_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_ps = fixed(VGroup(*[ton_slice(pax, q, mc, lambda x: 4.4, SUPPLY, SURPLUS_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_gov = fixed(VGroup(*[ton_slice(pax, q, lambda x: 2.4, lambda x: 4.4, GOV, GOV_OPACITY) for q in range(POSITIVE_Q)]))
        subsidy_words = fixed(VGroup(
            Tex('CS', color=INK).scale(0.72).move_to(pax.c2p(POSITIVE_Q / 3, (12 + 2.4 + 2.4) / 3)),
            Tex('PS', color=INK).scale(0.72).move_to(pax.c2p(POSITIVE_Q / 3, (2 + 4.4 + 4.4) / 3)),
            Tex('Subsidy cost', color=INK).scale(0.72).move_to(pax.c2p(POSITIVE_Q / 2, 3.4))).set_z_index(5))
        self.play(*[positive_ext_bars[q].animate.set_fill(opacity=0.12) for q in range(POSITIVE_Q)], FadeIn(question))
        self.play(FadeIn(subsidy_cs), FadeIn(subsidy_words[0]))
        self.pause('4.i.cs')
        self.play(FadeOut(subsidy_cs), FadeOut(subsidy_words[0]), run_time=0.5)
        self.play(FadeIn(subsidy_ps), FadeIn(subsidy_words[1]))
        self.pause('4.i.ps')
        self.play(FadeOut(subsidy_ps), FadeOut(subsidy_words[1]), run_time=0.5)
        self.remove(question)
        takeaway = teaching(r'Buyers pay $\$2.40$, sellers receive $\$4.40$, and the government pays $\$2$ per ton.')
        self.play(FadeIn(subsidy_gov), FadeIn(subsidy_words[2]), FadeIn(takeaway))
        self.pause('4.i.gov')
        self.remove(takeaway)
        takeaway = teaching('With a subsidy equal to the external benefit, there is no deadweight loss.')
        self.play(FadeOut(subsidy_gov), FadeOut(subsidy_words[2]), FadeIn(takeaway))
        self.pause('4.i')

        # ---- 5.a · The principle, in the notes' own words.
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        self.clear()
        head = fixed(title('Corrective Policy'))
        principle_line = fixed(Tex('A tax or subsidy equal to the externality sets $Q_s = Q_d = Q^*$.', color=INK))
        self.play(FadeIn(head), FadeIn(principle_line))
        self.pause('5.a')
