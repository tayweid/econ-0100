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
# prices separate as policy rises; the resulting wedge is then extracted to explain the gap.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../Part_B/Sim'))
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
        STRIP_OPACITY = 1.0
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.68
        BUYER_LEFT, SELLER_LEFT, BAR_WIDTH = -1.76, 0.66, 1.1
        TAX_LEFT, TAX_WIDTH = -0.40, 0.80
        detail_y = lambda value: DETAIL_BASE + DETAIL_SCALE * value
        ORIGIN_X, ORIGIN_Y = -3.2, -2.15
        AXIS_GAP_Q = -1.2  # Thin policy-size measurement just left of the price axis.
        DOT_LAYER = 30
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        QUANTITY_GAP_BAR_OFFSET, QUANTITY_GAP_CAPTION_BUFF = 1.0, 0.10

        # The model, as one-line functions of quantity or price.
        mb = lambda q: 12 - q / 5
        mc = lambda q: 2 + q / 20
        msc = lambda q: mc(q) + EXTERNAL
        msb = lambda q: mb(q) + EXTERNAL
        zero = lambda q: 0
        quantity_demanded = lambda p: (12 - p) * 5
        quantity_supplied = lambda p: (p - 2) * 20
        quantity_gap = lambda p: abs(quantity_demanded(p) - quantity_supplied(p))
        # Numbers sit nearest the axis; quantity names use a separate fixed row below.
        # Keep only the numbers when the two quantities are close; at their crossing,
        # show one number until there is room for both on the same axis row.
        quantity_label_opacity = lambda p: smooth(np.clip((quantity_gap(p) - 18) / 8, 0, 1))
        seller_quantity_opacity = lambda p: smooth(np.clip((quantity_gap(p) - 5) / 3, 0, 1))
        # Reveal the fixed 40 first; policy symbols need more room beside Q-hat.
        original_quantity_opacity = lambda q: smooth(np.clip((abs(q - MARKET_Q) - 3.8) / 0.2, 0, 1))
        policy_quantity_label_opacity = lambda q: smooth(np.clip(abs(q - MARKET_Q) - 7, 0, 1))
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
        context = fixed(subtitle(head, "Maximize society's total welfare."))
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
        social_cost = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(80, 8), color=SUPPLY, stroke_width=3))
        curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(ax.c2p(7, 10.6), UR, buff=0.12),
            Tex('MC', color=INK).scale(0.7).next_to(ax.c2p(80, 6), RIGHT, buff=0.12),
            Tex('MSC', color=INK).scale(0.7).next_to(ax.c2p(80, 8), RIGHT, buff=0.12)))
        market_dot = fixed(Dot(ax.c2p(40, 4), radius=0.065, color=MUTED).set_z_index(DOT_LAYER))
        market_quantity = fixed(VGroup(
            DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            VGroup(
                Tex('40', color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
                    .move_to(ax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                Tex(r'$\hat{Q}$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
                    .move_to(ax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))).set_z_index(10))
        market_price = fixed(VGroup(
            Tex(r'$\hat{P}=$', color=GUIDE).scale(0.7).next_to(msc_intercept, LEFT, buff=0.12),
            DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        efficient_marker = fixed(VGroup(
            DashedLine(ax.c2p(32, 0), ax.c2p(32, 5.6), color=FOCUS, stroke_width=2),
            Dot(ax.c2p(32, 5.6), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER + 1)).set_z_index(11))
        efficient_marker[1].set_z_index(DOT_LAYER + 1)
        efficient_word = fixed(VGroup(
            Tex('32', color=FOCUS).scale(QUANTITY_NUMBER_SCALE)
                .move_to(ax.c2p(32, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex(r'$Q^*$', color=FOCUS).scale(QUANTITY_LABEL_SCALE)
                .move_to(ax.c2p(32, 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        dwl_bars = fixed(VGroup(*[unit_slice(ax, q, mb, msc, DWL, 0.8) for q in range(EFFICIENT_Q, MARKET_Q)]).set_z_index(1))
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(40, 5.4), RIGHT, buff=0.3))
        recap = teaching('Last time: the market exchanges 40 units, but only 32 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(axis_words), FadeIn(msc_intercept),
                  FadeIn(demand), FadeIn(supply), FadeIn(social_cost),
                  FadeIn(curve_words), FadeIn(market_dot), FadeIn(market_quantity), FadeIn(market_price))
        self.play(FadeIn(efficient_marker), FadeIn(efficient_word), FadeIn(dwl_bars), FadeIn(dwl_word), FadeIn(recap))
        self.pause('1.a')

        original_guides = fixed(VGroup(
            DashedLine(ax.c2p(0, MARKET_P), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
            DashedLine(ax.c2p(MARKET_Q, 0), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2))).set_z_index(2)

        # ---- 2.a · The planner wants 32 units; which price gets both sides there?
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, "Maximize society's total welfare."))
        question = teaching('What price gets buyers and sellers to exchange 32 units?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(market_price), FadeOut(msc_intercept),
                  FadeOut(market_quantity[0]), FadeOut(dwl_bars), FadeOut(dwl_word), FadeIn(original_guides))
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
        # Keep the quantity-gap bar below both readout rows, aligned with the two drops.
        gap_line = fixed(Line(ax.c2p(40, 0), ax.c2p(40.001, 0), color=MUTED, stroke_width=4)
                         .shift(DOWN * QUANTITY_GAP_BAR_OFFSET).set_z_index(11))
        gap_line.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_GAP_BAR_OFFSET,
            ax.c2p(quantity_supplied(price.get_value()) + 1e-6, 0) + DOWN * QUANTITY_GAP_BAR_OFFSET))
        buyer_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        buyer_number.add_updater(lambda m: fixed(m.set_value(round(quantity_demanded(price.get_value()), 4)))
                                 .move_to(ax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        buyer_quantity_label = fixed(Tex('$Q_d$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        buyer_quantity_label.add_updater(lambda m: m.move_to(ax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)
                                 .set_opacity(quantity_label_opacity(price.get_value())))
        seller_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        seller_number.add_updater(lambda m: fixed(m.set_value(round(quantity_supplied(price.get_value()), 4)))
                                  .move_to(ax.c2p(quantity_supplied(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET)
                                  .set_opacity(seller_quantity_opacity(price.get_value())))
        seller_quantity_label = fixed(Tex('$Q_s$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        seller_quantity_label.add_updater(lambda m: m.move_to(ax.c2p(quantity_supplied(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)
                                 .set_opacity(quantity_label_opacity(price.get_value())))
        trial = [trial_line, trial_number, trial_prefix, buyer_dot, seller_dot, buyer_drop, seller_drop, gap_line]
        readouts = [buyer_number, buyer_quantity_label, seller_number, seller_quantity_label]
        for m in trial + readouts:
            m.update()
        self.add(*trial)
        self.play(FadeOut(market_quantity[1]), FadeOut(efficient_word),
                  price.animate.set_value(5.6), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{excess: 40 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=QUANTITY_GAP_CAPTION_BUFF))
        for m in readouts:
            m.update()   # Digits must already match before a number fades in.
        self.remove(question)
        question = teaching('The price that works for buyers creates excess supply.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_quantity_label), FadeIn(seller_number), FadeIn(seller_quantity_label),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('2.b')

        # ---- 2.c · Set the price at the sellers' willingness to sell unit 32: a shortage.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(3.6), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{shortage: 10 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=QUANTITY_GAP_CAPTION_BUFF))
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
            Line(ax.c2p(0, 3.6), ax.c2p(0, 5.6), color=FOCUS, stroke_width=4),
            Tex(r'$\$2$', color=FOCUS).scale(0.7).next_to(ax.c2p(0, 4.6), LEFT, buff=0.2)).set_z_index(13))
        takeaway = teaching('One price cannot get both sides to the efficient quantity.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_quantity_label),
                  FadeOut(seller_number), FadeOut(seller_quantity_label), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('2.d')

        # ---- 2.e · That gap is the external cost per unit.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external cost per unit.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('2.e')

        # ---- 3.a.start · Return to the market equilibrium before raising the tax.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Taxes'))
        context = fixed(subtitle(head, 'A tax equal to the external cost per unit.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        intro_tax = ValueTracker(0)
        intro_tax_q = lambda: taxed_quantity(intro_tax.get_value())
        intro_tax_seller_gets = lambda: mc(intro_tax_q())
        intro_tax_buyer_pays = lambda: mb(intro_tax_q())
        # One shared price initially; separate axis labels only once the gap is legible.
        intro_tax_price_opacity = lambda: smooth(np.clip((intro_tax.get_value() - 0.9) / 0.2, 0, 1))
        intro_tax_initial_price = fixed(Tex('$P=4.00$', color=GUIDE).scale(0.7)
            .next_to(ax.c2p(0, MARKET_P), LEFT, buff=0.2))
        intro_tax_initial_price.add_updater(lambda m: m.set_opacity(
            1 - smooth(np.clip(intro_tax.get_value() / 0.3, 0, 1))))
        intro_tax_top_dot = fixed(Dot(ax.c2p(40, 4), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        intro_tax_top_dot.add_updater(lambda m: m.move_to(ax.c2p(intro_tax_q(), intro_tax_buyer_pays())))
        intro_tax_bottom_dot = fixed(Dot(ax.c2p(40, 4), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        intro_tax_bottom_dot.add_updater(lambda m: m.move_to(ax.c2p(intro_tax_q(), intro_tax_seller_gets())))
        intro_tax_buyer_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        intro_tax_buyer_line.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(0, intro_tax_buyer_pays()), ax.c2p(intro_tax_q(), intro_tax_buyer_pays())))
        intro_tax_seller_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        intro_tax_seller_line.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(0, intro_tax_seller_gets()), ax.c2p(intro_tax_q(), intro_tax_seller_gets())))
        intro_tax_drop = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        intro_tax_drop.add_updater(lambda m: m.put_start_and_end_on(
            ax.c2p(intro_tax_q(), 0), ax.c2p(intro_tax_q(), intro_tax_buyer_pays())))
        intro_tax_buyer_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7))
        intro_tax_buyer_number.add_updater(lambda m: fixed(m.set_value(intro_tax_buyer_pays()))
            .next_to(ax.c2p(0, intro_tax_buyer_pays()), LEFT, buff=0.2).set_opacity(intro_tax_price_opacity()))
        intro_tax_buyer_prefix = fixed(Tex('$P_b=$', color=GUIDE).scale(0.7))
        intro_tax_buyer_prefix.add_updater(lambda m: m.next_to(intro_tax_buyer_number, LEFT, buff=0.1)
            .set_opacity(intro_tax_price_opacity()))
        intro_tax_seller_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7))
        intro_tax_seller_number.add_updater(lambda m: fixed(m.set_value(intro_tax_seller_gets()))
            .next_to(ax.c2p(0, intro_tax_seller_gets()), LEFT, buff=0.2).set_opacity(intro_tax_price_opacity()))
        intro_tax_seller_prefix = fixed(Tex('$P_s=$', color=GUIDE).scale(0.7))
        intro_tax_seller_prefix.add_updater(lambda m: m.next_to(intro_tax_seller_number, LEFT, buff=0.1)
            .set_opacity(intro_tax_price_opacity()))
        intro_tax_q_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        intro_tax_q_number.add_updater(lambda m: fixed(m.set_value(round(intro_tax_q(), 4)))
            .move_to(ax.c2p(intro_tax_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        intro_tax_q_label = fixed(Tex(r'$Q^{tax}$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        intro_tax_q_label.add_updater(lambda m: m.move_to(ax.c2p(intro_tax_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET)
            .set_opacity(policy_quantity_label_opacity(intro_tax_q())))
        tax_original_quantity = fixed(VGroup(
            Tex('40', color=CAPTION).scale(QUANTITY_NUMBER_SCALE)
                .move_to(ax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex(r'$\hat{Q}$', color=CAPTION).scale(QUANTITY_LABEL_SCALE)
                .move_to(ax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        tax_original_quantity.add_updater(lambda m: m.set_opacity(original_quantity_opacity(intro_tax_q())))
        tax_prices = fixed(VGroup(intro_tax_top_dot, intro_tax_bottom_dot,
            intro_tax_buyer_line, intro_tax_buyer_number, intro_tax_buyer_prefix,
            intro_tax_seller_line, intro_tax_seller_number, intro_tax_seller_prefix,
            intro_tax_drop, intro_tax_q_number, intro_tax_q_label))
        # The costly trades shrink continuously from Q-star to the current quantity.
        intro_tax_dwl = fixed(VGroup())
        for q in range(EFFICIENT_Q, MARKET_Q):
            bar = unit_slice(ax, q, mb, msc, DWL, 0.8).set_z_index(1)
            bar.add_updater(lambda m, q=q: m.become(unit_slice(
                ax, q, mb, msc, DWL, 0.8 if q + BAR_GAP / 2 < intro_tax_q() else 0,
                right=max(q + BAR_GAP / 2 + 1e-6, min(q + 1 - BAR_GAP / 2, intro_tax_q()))
            ).set_z_index(1)))
            intro_tax_dwl.add(bar)
        intro_tax_dwl_word = fixed(Tex('DWL', color=INK).scale(0.7)
            .next_to(ax.c2p((MARKET_Q + EFFICIENT_Q) / 2, msc(MARKET_Q)), UP, buff=0.3))
        intro_tax_dwl_word.add_updater(lambda m: m.set_opacity(
            smooth(np.clip((intro_tax_q() - EFFICIENT_Q) / 2, 0, 1))))
        for m in (tax_prices, intro_tax_dwl, intro_tax_dwl_word, intro_tax_initial_price, tax_original_quantity):
            m.update()
        self.add(tax_original_quantity)
        takeaway = teaching('Start at the market equilibrium, with no tax.')
        self.play(FadeIn(tax_prices), FadeIn(intro_tax_initial_price),
                  FadeIn(intro_tax_dwl), FadeIn(intro_tax_dwl_word), FadeIn(takeaway))
        self.pause('3.a.start')

        # ---- 3.a.prices · Raise the tax; price separation precedes the wedge explanation.
        self.remove(takeaway)
        takeaway = teaching('As the tax rises, prices separate and deadweight loss shrinks.')
        self.play(FadeIn(takeaway))
        self.play(intro_tax.animate.set_value(EXTERNAL), run_time=3.6, rate_func=smooth)
        for m in (tax_prices, intro_tax_dwl, intro_tax_dwl_word, intro_tax_initial_price, tax_original_quantity):
            m.clear_updaters()
        self.remove(intro_tax_dwl, *list(intro_tax_dwl), intro_tax_dwl_word, intro_tax_initial_price, takeaway)
        takeaway = teaching(r'A \$2 tax brings quantity to 32 and eliminates deadweight loss.')
        self.play(FadeIn(takeaway))
        self.pause('3.a.prices')

        # ---- 3.a · Slide a dashed measurement to the price axis to explain the resulting gap.
        self.remove(takeaway)
        wedge = fixed(Polygon(
            ax.c2p(EFFICIENT_Q - 0.42, 3.6), ax.c2p(EFFICIENT_Q + 0.42, 3.6),
            ax.c2p(EFFICIENT_Q + 0.42, 5.6), ax.c2p(EFFICIENT_Q - 0.42, 5.6),
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY).set_z_index(12))
        self.play(FadeIn(wedge), run_time=0.6)
        tax_axis_gap = fixed(DashedLine(ax.c2p(EFFICIENT_Q, 3.6), ax.c2p(EFFICIENT_Q, 5.6),
            color=GOV, stroke_width=2.5, dash_length=0.045)
            .put_start_and_end_on(ax.c2p(EFFICIENT_Q, 3.6), ax.c2p(EFFICIENT_Q, 5.6)).set_z_index(11))
        self.add(tax_axis_gap)
        self.play(tax_axis_gap.animate.shift(ax.c2p(AXIS_GAP_Q, 0) - ax.c2p(EFFICIENT_Q, 0)), run_time=1.6)
        wedge_word = fixed(Tex(r'Tax $=$ \$2', color=GOV).scale(0.6)
            .next_to(ax.c2p(0, 4.6), LEFT, buff=0.2).set_z_index(13))
        takeaway = teaching(r"The tax is the \$2 gap between the buyers' and sellers' prices.")
        self.play(FadeIn(wedge_word), FadeIn(takeaway))
        self.pause('3.a')

        # ---- 3.a.curve · The same tax also raises private cost onto social cost.
        # Keep MSC dashed, as in the rest of C3; only the policy overlay and names are temporary.
        self.remove(takeaway)
        tax_curve_external = fixed(VGroup(*[
            unit_slice(ax, q, mc, msc, EXT, BASE_OPACITY).set_z_index(-2) for q in range(EFFICIENT_Q)]).set_z_index(-2))
        tax_curve_strips = fixed(VGroup(*[
            unit_slice(ax, q, mc, msc, GOV, STRIP_OPACITY).set_z_index(-1) for q in range(EFFICIENT_Q)]).set_z_index(-1))
        tax_policy_curve = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(80, 8), color=SUPPLY, stroke_width=3))
        tax_policy_name = fixed(Tex(r'$\mathrm{MC}+\mathrm{tax}$', color=INK).scale(0.7)
            .next_to(ax.c2p(80, 8), UP, buff=0.24))
        tax_merged_name = fixed(Tex(r'$\mathrm{MSC}=\mathrm{MC}+\mathrm{tax}$', color=INK).scale(0.7)
            .next_to(ax.c2p(80, 8), RIGHT, buff=0.12))
        takeaway = teaching(r'A \$2 tax lifts MC onto MSC: private and social costs match.')
        self.play(FadeIn(tax_curve_external), FadeIn(takeaway))
        self.play(LaggedStart(*[FadeIn(bar) for bar in tax_curve_strips], lag_ratio=0.035),
                  FadeIn(tax_policy_curve), FadeIn(tax_policy_name), run_time=1.8)
        self.play(FadeOut(curve_words[2]), FadeOut(tax_policy_name), FadeIn(tax_merged_name))
        self.pause('3.a.curve')
        self.play(FadeOut(tax_curve_strips), FadeOut(tax_curve_external), FadeOut(tax_policy_curve),
                  FadeOut(tax_merged_name), FadeIn(curve_words[2]))

        # ---- 3.b · The exchanges past 32 stop, and their deadweight loss with them.
        self.remove(takeaway)
        takeaway = teaching('Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.')
        self.play(FadeIn(takeaway))
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
            Tex('GOV', color=INK).scale(0.58).move_to(ax.c2p(EFFICIENT_Q / 2, 4.6))).set_z_index(5))
        self.play(FadeIn(question))
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
                             market_dot, tax_original_quantity, efficient_marker, wedge, wedge_word, tax_axis_gap, tax_prices,
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

        # ---- 3.e.select · Carry the same unit into C2's spread welfare layout.
        stopped_pair = fixed(VGroup(
            unit_slice(ax, 35, zero, mb, DEMAND, 0),
            unit_slice(ax, 35, zero, mc, SUPPLY, 0),
            unit_slice(ax, 35, mc, msc, EXT, 0)))
        stopped_home = stopped_pair.copy()
        stopped_box = fixed(SurroundingRectangle(stopped_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        takeaway = teaching("Let's check an exchange that happened before the tax.")
        self.play(FadeIn(stopped_pair), FadeIn(stopped_box), FadeIn(takeaway))
        self.pause('3.e.select')

        # ---- 3.e.values · Real private values and the externality, before prices or verdicts.
        stopped_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 4.8, DEMAND), (SELLER_LEFT, 0, 3.8, SUPPLY),
                                       (SELLER_LEFT, 3.8, 5.8, EXT)]:
            stopped_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(context), FadeOut(stopped_box), FadeOut(takeaway),
                  Transform(stopped_pair, stopped_target), run_time=1.6)
        stopped_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(stopped_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED))).set_z_index(3)
        stopped_values = fixed(VGroup(
            Tex(r'\$4.80', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(4.8), 0], LEFT, buff=0.25),
            Tex(r'\$3.80', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(3.8), 0], RIGHT, buff=0.45),
            Tex(r'\$5.80', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(5.8), 0], RIGHT, buff=0.45),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(4.8), 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(3.6), 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(5.8), 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.55).move_to([1.21, detail_y(4.8), 0]))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'The 36th unit: an exchange the tax stops.'))
        stopped_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(stopped_edges), FadeIn(stopped_values), FadeIn(unit_context), FadeIn(stopped_questions[0]), FadeIn(stopped_questions[1]))
        self.pause('3.e.values')

        # ---- 3.e.prices · Government's transfer spans actual prices, not MB or MC.
        stopped_prices = fixed(VGroup(
            Line([-2.6, detail_y(5.6), 0], [1.9, detail_y(5.6), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(3.6), 0], [1.9, detail_y(3.6), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        stopped_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(5.6), 0], UP, buff=0.06),
            Tex(r'\$5.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(5.6), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(3.6), 0], DOWN, buff=0.06),
            Tex(r'\$3.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(3.6), 0], LEFT, buff=0.15))).set_z_index(4)
        stopped_transfer = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(3.6), 0], [TAX_LEFT + TAX_WIDTH, detail_y(3.6), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(5.6), 0], [TAX_LEFT, detail_y(5.6), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            Tex('tax', color=INK).scale(.55).move_to([0, detail_y(4.6), 0]))).set_z_index(3)
        self.play(FadeIn(stopped_prices), FadeIn(stopped_price_words), FadeIn(stopped_transfer))
        self.pause('3.e.prices')

        # ---- 3.e.buyer · First ask whether the buyer's value covers the buyer's price.
        stopped_buyer_guides = fixed(VGroup(
            DashedLine(stopped_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.8), 0], [-4.25, detail_y(5.6), 0], color=DEMAND, stroke_width=3)))
        takeaway = teaching(r'The buyer: value \$4.80 against a price of \$5.60.')
        self.play(FadeIn(stopped_buyer_guides), FadeIn(takeaway))
        self.pause('3.e.buyer')

        # ---- 3.e.buyer.answer · Finish the buyer's decision before moving to the seller.
        stopped_buyer_answer = fixed(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5),
            Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)
            .next_to(stopped_buyer_guides[-1], LEFT, buff=0.3))
        self.play(FadeIn(stopped_buyer_answer))
        self.pause('3.e.buyer.answer')

        # ---- 3.e.seller · Then compare the seller's cost with the amount the seller receives.
        self.remove(takeaway)
        stopped_seller_guides = fixed(VGroup(
            DashedLine([SELLER_LEFT, detail_y(3.8), 0], [TAX_LEFT + TAX_WIDTH + 0.10, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.10, detail_y(3.8), 0], [stopped_price_words[3].get_right()[0] + 0.12, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([stopped_price_words[3].get_left()[0] - 0.12, detail_y(3.8), 0], [-4.25, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(3.6), 0], [-4.25, detail_y(3.8), 0], color=SUPPLY, stroke_width=3)))
        takeaway = teaching(r'The seller: cost \$3.80 against a price of \$3.60.')
        self.play(FadeIn(stopped_seller_guides), FadeIn(takeaway))
        self.pause('3.e.seller')

        # ---- 3.e.private · Complete the seller's decision, keeping both individual verdicts.
        self.remove(takeaway)
        stopped_seller_answer = fixed(stopped_buyer_answer.copy()
            .next_to(stopped_seller_guides[-1], LEFT, buff=0.3))
        stopped_private_answer = fixed(VGroup(stopped_buyer_answer, stopped_seller_answer))
        takeaway = teaching('Neither side wants this trade at these prices.')
        self.play(FadeIn(stopped_seller_answer), FadeIn(takeaway))
        self.remove(stopped_buyer_answer, stopped_seller_answer)
        self.add(stopped_private_answer)
        self.pause('3.e.private')

        # ---- 3.e.social.compare · C1's real benefit/cost comparison excludes government transfers.
        self.remove(takeaway)
        stopped_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [TAX_LEFT - 0.12, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT + TAX_WIDTH + 0.12, detail_y(4.8), 0], [SELLER_LEFT, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([SELLER_LEFT + BAR_WIDTH + 0.12, detail_y(4.8), 0], [4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(stopped_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(5.8), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(4.8), 0], [4.25, detail_y(5.8), 0], color=TOTAL, stroke_width=3)))
        stopped_social_answer = fixed(VGroup(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5),
            Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)), Tex('DWL', color=INK))
            .arrange(DOWN, buff=0.16).scale(0.70)
            .next_to([4.25, detail_y(5.3), 0], RIGHT, buff=0.3))
        self.play(stopped_transfer.animate.set_opacity(0.20),
                  stopped_prices.animate.set_opacity(0.25), stopped_price_words.animate.set_opacity(0.25),
                  stopped_buyer_guides.animate.set_opacity(0.25), stopped_seller_guides.animate.set_opacity(0.25),
                  FadeIn(stopped_social_guides))
        self.pause('3.e.social.compare')

        # ---- 3.e.social · Same TS/DWL interval and verdict as C1.
        stopped_welfare = fixed(Polygon(
            [SELLER_LEFT, detail_y(4.8), 0], [SELLER_LEFT + BAR_WIDTH, detail_y(4.8), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(5.8), 0], [SELLER_LEFT, detail_y(5.8), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        takeaway = teaching(r'Good: this trade would have cost society \$1.')
        self.play(FadeIn(stopped_welfare), FadeIn(stopped_social_answer), FadeIn(takeaway))
        self.pause('3.e.social')

        # ---- 3.e.return · Remove every annotation and return the same three slices.
        self.remove(detail_people)
        self.play(FadeOut(stopped_edges), FadeOut(stopped_values), FadeOut(stopped_questions),
                  FadeOut(stopped_prices), FadeOut(stopped_price_words), FadeOut(stopped_transfer),
                  FadeOut(stopped_buyer_guides), FadeOut(stopped_seller_guides),
                  FadeOut(stopped_private_answer), FadeOut(stopped_social_guides), FadeOut(stopped_social_answer),
                  FadeOut(stopped_welfare),
                  FadeOut(takeaway), FadeOut(unit_context), run_time=0.4)
        self.play(Transform(stopped_pair, stopped_home), FadeIn(market), FadeIn(context), run_time=1.6)
        self.remove(stopped_pair)
        self.pause('3.e.return')

        # ---- 3.f.select · Carry the same unit into C2's spread welfare layout.
        kept_pair = fixed(VGroup(
            unit_slice(ax, 23, zero, mb, DEMAND, 0),
            unit_slice(ax, 23, zero, mc, SUPPLY, 0),
            unit_slice(ax, 23, mc, msc, EXT, 0)))
        kept_home = kept_pair.copy()
        kept_box = fixed(SurroundingRectangle(kept_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        takeaway = teaching("Let's check an exchange that still happens with the tax.")
        self.play(FadeIn(kept_pair), FadeIn(kept_box), FadeIn(takeaway))
        self.pause('3.f.select')

        # ---- 3.f.values · Real private values and the externality, before prices or verdicts.
        kept_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 7.2, DEMAND), (SELLER_LEFT, 0, 3.2, SUPPLY),
                                       (SELLER_LEFT, 3.2, 5.2, EXT)]:
            kept_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(context), FadeOut(kept_box), FadeOut(takeaway),
                  Transform(kept_pair, kept_target), run_time=1.6)
        kept_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(kept_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED))).set_z_index(3)
        kept_values = fixed(VGroup(
            Tex(r'\$7.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(7.2), 0], LEFT, buff=0.25),
            Tex(r'\$3.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(3.2), 0], RIGHT, buff=0.45),
            Tex(r'\$5.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(5.2), 0], RIGHT, buff=0.45),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(7.2), 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(3.2), 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.50).next_to([1.21, detail_y(5.2), 0], UP, buff=0.03),
            Tex('EXT', color=EXT).scale(0.55).move_to([1.21, detail_y(4.2), 0]))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'Unit 24: still exchanged.'))
        kept_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(kept_edges), FadeIn(kept_values), FadeIn(unit_context), FadeIn(kept_questions[0]), FadeIn(kept_questions[1]))
        self.pause('3.f.values')

        # ---- 3.f.prices · Government's transfer spans actual prices, not MB or MC.
        kept_prices = fixed(VGroup(
            Line([-2.6, detail_y(5.6), 0], [1.9, detail_y(5.6), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(3.6), 0], [1.9, detail_y(3.6), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        kept_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(5.6), 0], UP, buff=0.06),
            Tex(r'\$5.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(5.6), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(3.6), 0], DOWN, buff=0.06),
            Tex(r'\$3.60', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(3.6), 0], LEFT, buff=0.15))).set_z_index(4)
        kept_transfer = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(3.6), 0], [TAX_LEFT + TAX_WIDTH, detail_y(3.6), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(5.6), 0], [TAX_LEFT, detail_y(5.6), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            Tex('tax', color=INK).scale(.55).move_to([0, detail_y(4.6), 0]))).set_z_index(3)
        self.play(FadeIn(kept_prices), FadeIn(kept_price_words), FadeIn(kept_transfer))
        self.pause('3.f.prices')

        # ---- 3.f.buyer · First ask whether the buyer's value covers the buyer's price.
        kept_buyer_guides = fixed(VGroup(
            DashedLine(kept_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(7.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(5.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(5.6), 0], [-4.25, detail_y(7.2), 0], color=DEMAND, stroke_width=3)))
        kept_cs = fixed(Polygon(
            [BUYER_LEFT, detail_y(5.6), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(5.6), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(7.2), 0], [BUYER_LEFT, detail_y(7.2), 0],
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY).set_z_index(1))
        kept_cs_word = fixed(Tex('CS', color=INK).scale(0.55)
            .move_to([-1.21, detail_y(6.4), 0]).set_z_index(4))
        takeaway = teaching(r'The buyer: value \$7.20 against a price of \$5.60.')
        self.play(FadeIn(kept_buyer_guides), GrowFromEdge(kept_cs, DOWN), FadeIn(kept_cs_word), FadeIn(takeaway))
        self.pause('3.f.buyer')

        # ---- 3.f.buyer.answer · Finish the buyer's decision before moving to the seller.
        kept_buyer_answer = fixed(VMobject(color=EFFICIENT, stroke_width=5)
            .set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)
            .next_to(kept_buyer_guides[-1], LEFT, buff=0.3))
        self.play(FadeIn(kept_buyer_answer))
        self.pause('3.f.buyer.answer')

        # ---- 3.f.seller · Then compare the seller's cost with the amount the seller receives.
        self.remove(takeaway)
        kept_seller_guides = fixed(VGroup(
            DashedLine([SELLER_LEFT, detail_y(3.2), 0], [TAX_LEFT + TAX_WIDTH + 0.10, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.10, detail_y(3.2), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([kept_price_words[3].get_left()[0] - 0.12, detail_y(3.2), 0], [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(3.6), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(3.2), 0], [-4.25, detail_y(3.6), 0], color=SUPPLY, stroke_width=3)))
        kept_ps = fixed(Polygon(
            [SELLER_LEFT, detail_y(3.2), 0], [SELLER_LEFT + BAR_WIDTH, detail_y(3.2), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(3.6), 0], [SELLER_LEFT, detail_y(3.6), 0],
            stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY).set_z_index(1))
        kept_ps_word = fixed(Tex('PS', color=INK).scale(0.42)
            .move_to([1.21, detail_y(3.4), 0]).set_z_index(4))
        takeaway = teaching(r'The seller: cost \$3.20 against a price of \$3.60.')
        self.play(FadeIn(kept_seller_guides), GrowFromEdge(kept_ps, DOWN), FadeIn(kept_ps_word), FadeIn(takeaway))
        self.pause('3.f.seller')

        # ---- 3.f.private · Complete the seller's decision, keeping both individual verdicts.
        self.remove(takeaway)
        kept_seller_answer = fixed(kept_buyer_answer.copy()
            .next_to(kept_seller_guides[-1], LEFT, buff=0.3))
        kept_private_answer = fixed(VGroup(kept_buyer_answer, kept_seller_answer))
        takeaway = teaching('Both sides want this trade at these prices.')
        self.play(FadeIn(kept_seller_answer), FadeIn(takeaway))
        self.remove(kept_buyer_answer, kept_seller_answer)
        self.add(kept_private_answer)
        self.pause('3.f.private')

        # ---- 3.f.social.compare · C1's real benefit/cost comparison excludes government transfers.
        self.remove(takeaway)
        kept_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(7.2), 0], [4.25, detail_y(7.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(kept_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(7.2), 0], [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=3)))
        kept_social_answer = fixed(VGroup(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex('TS', color=TOTAL))
            .arrange(DOWN, buff=0.16).scale(0.70)
            .next_to([4.25, detail_y(6.2), 0], RIGHT, buff=0.3))
        self.play(kept_transfer.animate.set_opacity(0.20),
                  kept_prices.animate.set_opacity(0.25), kept_price_words.animate.set_opacity(0.25),
                  kept_buyer_guides.animate.set_opacity(0.25), kept_seller_guides.animate.set_opacity(0.25),
                  FadeOut(kept_cs), FadeOut(kept_ps),
                  FadeOut(kept_cs_word), FadeOut(kept_ps_word),
                  FadeIn(kept_social_guides))
        self.pause('3.f.social.compare')

        # ---- 3.f.social · Same TS/DWL interval and verdict as C1.
        takeaway = teaching(r'Good: this trade is worth \$2 to society.')
        self.play(FadeIn(kept_social_answer), FadeIn(takeaway))
        self.pause('3.f.social')

        # ---- 3.f.return · Remove every annotation and return the same three slices.
        self.remove(detail_people)
        self.play(FadeOut(kept_edges), FadeOut(kept_values), FadeOut(kept_questions),
                  FadeOut(kept_prices), FadeOut(kept_price_words), FadeOut(kept_transfer),
                  FadeOut(kept_buyer_guides), FadeOut(kept_seller_guides),
                  FadeOut(kept_private_answer), FadeOut(kept_social_guides), FadeOut(kept_social_answer),
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
        tax_original_quantity.add_updater(lambda m: m.set_opacity(original_quantity_opacity(taxed_q())))
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
        live_tax_number = fixed(DecimalNumber(EXTERNAL, num_decimal_places=0, color=GOV).scale(0.6).set_z_index(14))
        live_tax_number.axes, live_tax_number.tax = ax, tax
        live_tax_number.add_updater(lambda m: fixed(m.set_value(m.tax.get_value()))
            .next_to(m.axes.c2p(0, 4 + 0.3 * m.tax.get_value()), LEFT,
                     buff=0.2 + 1.8 * smooth(np.clip((1.9 - m.tax.get_value()) / 0.4, 0, 1))))
        live_tax_prefix = fixed(Tex(r'Tax $=$ \$', color=GOV).scale(0.6).set_z_index(14))
        live_tax_prefix.number = live_tax_number
        live_tax_prefix.add_updater(lambda m: m.next_to(m.number, LEFT, buff=0.02))
        live_tax_axis_gap = fixed(DashedLine(ax.c2p(AXIS_GAP_Q, 3.6), ax.c2p(AXIS_GAP_Q, 5.6),
            color=GOV, stroke_width=2.5, dash_length=0.045).set_z_index(11))
        live_tax_axis_gap.axes, live_tax_axis_gap.tax = ax, tax
        live_tax_axis_gap.add_updater(lambda m: fixed(m.become(DashedLine(
            m.axes.c2p(AXIS_GAP_Q, 4 - 0.2 * m.tax.get_value()),
            m.axes.c2p(AXIS_GAP_Q, 4 + 0.8 * m.tax.get_value()) + UP * 1e-6,
            color=GOV, stroke_width=2.5, dash_length=0.045)))
            .set_z_index(11)
            .set_opacity(1 if abs(m.tax.get_value()) > 1e-5 else 0))
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
        live_q_number = fixed(DecimalNumber(32, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        live_q_number.add_updater(lambda m: fixed(m.set_value(round(taxed_q(), 4)))
                                  .move_to(ax.c2p(taxed_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        live_q_label = fixed(Tex(r'$Q^{tax}$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        live_q_label.add_updater(lambda m: m.move_to(ax.c2p(taxed_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET)
            .set_opacity(policy_quantity_label_opacity(taxed_q())))
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
        live = [wedge, live_top_dot, live_bottom_dot, live_tax_number, live_tax_prefix, live_tax_axis_gap,
                live_buyer_line, live_seller_line, live_drop,
                live_buyer_number, live_buyer_prefix, live_seller_number, live_seller_prefix,
                live_q_number, live_q_label, live_ps, live_cs, live_gov, live_dwl, live_dwl_word]
        for m in live:
            m.update()
        market.remove(wedge, wedge_word, tax_axis_gap, tax_prices, ps_fill, cs_fill, gov_fill)
        self.remove(wedge_word, tax_axis_gap, tax_prices, ps_fill, cs_fill, gov_fill)
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
        # Return the fixed $2 label to the axis before moving the graph for the conclusion.
        for m in (live_tax_number, live_tax_prefix):
            self.remove(m)
            live.remove(m)
        negative_conclusion_graph = fixed(VGroup(market, *live, welfare_words, wedge_word))
        self.remove(market, *live, welfare_words)
        self.add(negative_conclusion_graph)
        self.play(negative_conclusion_graph.animate.shift(LEFT * 2.0), run_time=1.2)
        negative_equality = fixed(VGroup(
            Tex(r'$\mathrm{Tax}=\mathrm{EXT}$', color=DEFINITION).scale(1.10),
            Tex(r'$\Downarrow$', color=DEFINITION).scale(0.85),
            Tex('32 units', color=CAPTION).scale(0.65),
            Tex(r'$Q^{tax}=Q^*$', color=GUIDE).scale(1.10)
        ).arrange(DOWN, buff=0.22).move_to([4.2, 0.7, 0]))
        takeaway = teaching('A corrective tax prevents costly exchanges and preserves worthwhile ones.')
        self.play(FadeIn(negative_equality[0]))
        self.play(FadeIn(negative_equality[1:]), FadeIn(takeaway))
        self.pause('3.g.summary')

        # ---- 4.a · Last time: the positive-externality market and its deadweight loss.
        for m in self.mobjects:
            m.clear_updaters()
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        self.clear()
        head = fixed(title('Positive Externalities'))
        context = fixed(subtitle(head, "Maximize society's total welfare."))
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
        social_benefit = fixed(DashedLine(pax.c2p(0, 14), pax.c2p(70, 0), color=DEMAND, stroke_width=3))
        positive_curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(pax.c2p(8, 10.4), DOWN, buff=0.14),
            Tex('MC', color=INK).scale(0.7).next_to(pax.c2p(80, 6), RIGHT, buff=0.12),
            Tex('MSB', color=INK).scale(0.7).next_to(pax.c2p(8, 12.4), UR, buff=0.10)).set_z_index(6))
        positive_dot = fixed(Dot(pax.c2p(40, 4), radius=0.065, color=MUTED).set_z_index(DOT_LAYER))
        positive_quantity = fixed(VGroup(
            DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2),
            VGroup(
                Tex('40', color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
                    .move_to(pax.c2p(40, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                Tex(r'$\hat{Q}$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
                    .move_to(pax.c2p(40, 0) + DOWN * QUANTITY_LABEL_OFFSET))).set_z_index(10))
        positive_price = fixed(VGroup(
            Tex(r'$\hat{P}=4$', color=GUIDE).scale(0.7).next_to(pax.c2p(0, 4), LEFT, buff=0.2),
            DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2)).set_z_index(10))
        positive_efficient = fixed(VGroup(
            DashedLine(pax.c2p(48, 0), pax.c2p(48, 4.4), color=FOCUS, stroke_width=2),
            Dot(pax.c2p(48, 4.4), radius=0.085, color=FOCUS)).set_z_index(11))
        positive_efficient[1].set_z_index(DOT_LAYER + 1)
        positive_efficient_word = fixed(VGroup(
            Tex('48', color=FOCUS).scale(QUANTITY_NUMBER_SCALE)
                .move_to(pax.c2p(48, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex(r'$Q^*$', color=FOCUS).scale(QUANTITY_LABEL_SCALE)
                .move_to(pax.c2p(48, 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        positive_dwl = fixed(VGroup(*[unit_slice(pax, q, mc, msb, DWL, 0.8) for q in range(MARKET_Q, POSITIVE_Q)]).set_z_index(1))
        positive_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(positive_dwl, UP, buff=0.16))
        recap = teaching('Last time: the market exchanges 40 units, but 48 are efficient.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(pax), FadeIn(positive_axis_words),
                  FadeIn(positive_demand), FadeIn(positive_supply), FadeIn(social_benefit),
                  FadeIn(positive_curve_words), FadeIn(positive_dot), FadeIn(positive_quantity), FadeIn(positive_price))
        self.play(FadeIn(positive_efficient), FadeIn(positive_efficient_word), FadeIn(positive_dwl), FadeIn(positive_dwl_word), FadeIn(recap))
        self.pause('4.a')

        positive_original_guides = fixed(VGroup(
            DashedLine(pax.c2p(0, MARKET_P), pax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
            DashedLine(pax.c2p(MARKET_Q, 0), pax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2))).set_z_index(2)

        # ---- 4.b · The planner wants 48 units.
        self.remove(head, context, recap)
        head = fixed(title('The Social Planner'))
        context = fixed(subtitle(head, "Maximize society's total welfare."))
        question = teaching('What price gets buyers and sellers to exchange 48 units?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(question), FadeOut(positive_price), FadeOut(positive_axis_words[4]),
                  FadeOut(positive_quantity[0]), FadeOut(positive_dwl), FadeOut(positive_dwl_word), FadeIn(positive_original_guides))
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
        gap_line = fixed(Line(pax.c2p(40, 0), pax.c2p(40.001, 0), color=MUTED, stroke_width=4)
                         .shift(DOWN * QUANTITY_GAP_BAR_OFFSET).set_z_index(11))
        gap_line.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_GAP_BAR_OFFSET,
            pax.c2p(quantity_supplied(price.get_value()) + 1e-6, 0) + DOWN * QUANTITY_GAP_BAR_OFFSET))
        buyer_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        buyer_number.add_updater(lambda m: fixed(m.set_value(round(quantity_demanded(price.get_value()), 4)))
                                 .move_to(pax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        buyer_quantity_label = fixed(Tex('$Q_d$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        buyer_quantity_label.add_updater(lambda m: m.move_to(pax.c2p(quantity_demanded(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)
                                 .set_opacity(quantity_label_opacity(price.get_value())))
        seller_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        seller_number.add_updater(lambda m: fixed(m.set_value(round(quantity_supplied(price.get_value()), 4)))
                                  .move_to(pax.c2p(quantity_supplied(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET)
                                  .set_opacity(seller_quantity_opacity(price.get_value())))
        seller_quantity_label = fixed(Tex('$Q_s$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        seller_quantity_label.add_updater(lambda m: m.move_to(pax.c2p(quantity_supplied(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)
                                 .set_opacity(quantity_label_opacity(price.get_value())))
        trial = [trial_line, trial_number, trial_prefix, buyer_dot, seller_dot, buyer_drop, seller_drop, gap_line]
        readouts = [buyer_number, buyer_quantity_label, seller_number, seller_quantity_label]
        for m in trial + readouts:
            m.update()
        self.add(*trial)
        self.play(FadeOut(positive_quantity[1]), FadeOut(positive_efficient_word),
                  price.animate.set_value(2.4), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{shortage: 40 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=QUANTITY_GAP_CAPTION_BUFF))
        for m in readouts:
            m.update()
        self.remove(question)
        question = teaching('The price that works for buyers creates a shortage.')
        self.play(FadeIn(buyer_number), FadeIn(buyer_quantity_label), FadeIn(seller_number), FadeIn(seller_quantity_label),
                  FadeIn(gap_word), FadeIn(question))
        self.pause('4.c')

        # ---- 4.d · The sellers' willingness to sell unit 48: an excess.
        self.remove(question, gap_word)
        self.play(price.animate.set_value(4.4), run_time=2.4, rate_func=smooth)
        gap_word = fixed(Tex(r'\textsf{excess: 10 units}', color=CAPTION).scale(0.55).next_to(gap_line, DOWN, buff=QUANTITY_GAP_CAPTION_BUFF))
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
            Line(pax.c2p(0, 2.4), pax.c2p(0, 4.4), color=FOCUS, stroke_width=4),
            Tex(r'$\$2$', color=FOCUS).scale(0.7).next_to(pax.c2p(0, 3.4), LEFT, buff=0.2)).set_z_index(13))
        takeaway = teaching('One price cannot get both sides to the efficient quantity.')
        self.play(FadeOut(buyer_dot), FadeOut(seller_dot), FadeOut(buyer_drop), FadeOut(seller_drop),
                  FadeOut(gap_line), FadeOut(gap_word), FadeOut(buyer_number), FadeOut(buyer_quantity_label),
                  FadeOut(seller_number), FadeOut(seller_quantity_label), FadeOut(trial_number), FadeOut(trial_prefix),
                  FadeOut(trial_line),
                  FadeIn(seller_price), FadeIn(buyer_price),
                  FadeIn(gap_mark), FadeIn(takeaway))
        self.pause('4.e')

        # ---- 4.f · That gap is the external benefit per unit.
        self.remove(takeaway)
        takeaway = teaching(r'The $\$2$ gap between the prices is the external benefit per unit.')
        self.play(Indicate(gap_mark, color=FOCUS, scale_factor=1.25), FadeIn(takeaway), run_time=0.8)
        self.pause('4.f')

        # ---- 4.g.start · Return to the market equilibrium before raising the subsidy.
        self.remove(head, context, takeaway)
        head = fixed(title('Corrective Subsidies'))
        context = fixed(subtitle(head, 'A subsidy equal to the external benefit per unit.'))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_price), FadeOut(buyer_price), FadeOut(gap_mark))
        subsidy = ValueTracker(0)
        subsidized_q = lambda: MARKET_Q + 4 * subsidy.get_value()
        subsidy_buyer_pays = lambda: mb(subsidized_q())
        subsidy_seller_gets = lambda: mc(subsidized_q())
        # One shared price initially; separate axis labels only once the gap is legible.
        subsidy_price_opacity = lambda: smooth(np.clip((subsidy.get_value() - 0.9) / 0.2, 0, 1))
        subsidy_initial_price = fixed(Tex('$P=4.00$', color=GUIDE).scale(0.7)
            .next_to(pax.c2p(0, MARKET_P), LEFT, buff=0.2))
        subsidy_initial_price.add_updater(lambda m: m.set_opacity(
            1 - smooth(np.clip(subsidy.get_value() / 0.3, 0, 1))))
        subsidy_top_dot = fixed(Dot(pax.c2p(40, 4), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        subsidy_top_dot.add_updater(lambda m: m.move_to(pax.c2p(subsidized_q(), subsidy_seller_gets())))
        subsidy_bottom_dot = fixed(Dot(pax.c2p(40, 4), radius=0.07, color=GUIDE).set_z_index(DOT_LAYER))
        subsidy_bottom_dot.add_updater(lambda m: m.move_to(pax.c2p(subsidized_q(), subsidy_buyer_pays())))
        subsidy_seller_line = fixed(DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        subsidy_seller_line.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(0, subsidy_seller_gets()), pax.c2p(subsidized_q(), subsidy_seller_gets())))
        subsidy_buyer_line = fixed(DashedLine(pax.c2p(0, 4), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        subsidy_buyer_line.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(0, subsidy_buyer_pays()), pax.c2p(subsidized_q(), subsidy_buyer_pays())))
        subsidy_drop = fixed(DashedLine(pax.c2p(40, 0), pax.c2p(40, 4), color=GUIDE, stroke_width=2).set_z_index(10))
        subsidy_drop.add_updater(lambda m: m.put_start_and_end_on(
            pax.c2p(subsidized_q(), 0), pax.c2p(subsidized_q(), subsidy_seller_gets())))
        subsidy_seller_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7))
        subsidy_seller_number.add_updater(lambda m: fixed(m.set_value(subsidy_seller_gets()))
            .next_to(pax.c2p(0, subsidy_seller_gets()), LEFT, buff=0.2).set_opacity(subsidy_price_opacity()))
        subsidy_seller_prefix = fixed(Tex('$P_s=$', color=GUIDE).scale(0.7))
        subsidy_seller_prefix.add_updater(lambda m: m.next_to(subsidy_seller_number, LEFT, buff=0.1)
            .set_opacity(subsidy_price_opacity()))
        subsidy_buyer_number = fixed(DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7))
        subsidy_buyer_number.add_updater(lambda m: fixed(m.set_value(subsidy_buyer_pays()))
            .next_to(pax.c2p(0, subsidy_buyer_pays()), LEFT, buff=0.2).set_opacity(subsidy_price_opacity()))
        subsidy_buyer_prefix = fixed(Tex('$P_b=$', color=GUIDE).scale(0.7))
        subsidy_buyer_prefix.add_updater(lambda m: m.next_to(subsidy_buyer_number, LEFT, buff=0.1)
            .set_opacity(subsidy_price_opacity()))
        subsidy_q_number = fixed(DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE))
        subsidy_q_number.add_updater(lambda m: fixed(m.set_value(round(subsidized_q(), 4)))
            .move_to(pax.c2p(subsidized_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        subsidy_q_label = fixed(Tex(r'$Q^{subsidy}$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).set_max_width(0.86))
        subsidy_q_label.add_updater(lambda m: m.move_to(pax.c2p(subsidized_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET)
            .set_opacity(policy_quantity_label_opacity(subsidized_q())))
        subsidy_original_quantity = fixed(VGroup(
            Tex('40', color=CAPTION).scale(QUANTITY_NUMBER_SCALE)
                .move_to(pax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            Tex(r'$\hat{Q}$', color=CAPTION).scale(QUANTITY_LABEL_SCALE)
                .move_to(pax.c2p(MARKET_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        subsidy_original_quantity.add_updater(lambda m: m.set_opacity(original_quantity_opacity(subsidized_q())))
        subsidy_prices = fixed(VGroup(subsidy_top_dot, subsidy_bottom_dot,
            subsidy_seller_line, subsidy_seller_number, subsidy_seller_prefix,
            subsidy_buyer_line, subsidy_buyer_number, subsidy_buyer_prefix,
            subsidy_drop, subsidy_q_number, subsidy_q_label))
        # The lost trades shrink continuously from the current quantity to Q-star.
        subsidy_dwl = fixed(VGroup())
        for q in range(MARKET_Q, POSITIVE_Q):
            bar = unit_slice(pax, q, mc, msb, DWL, 0.8).set_z_index(1)
            bar.add_updater(lambda m, q=q: m.become(unit_slice(
                pax, q, mc, msb, DWL, 0.8 if q + 1 - BAR_GAP / 2 > subsidized_q() else 0,
                left=min(q + 1 - BAR_GAP / 2 - 1e-6, max(q + BAR_GAP / 2, subsidized_q()))
            ).set_z_index(1)))
            subsidy_dwl.add(bar)
        subsidy_dwl_word = fixed(Tex('DWL', color=INK).scale(0.7)
            .next_to(pax.c2p((MARKET_Q + POSITIVE_Q) / 2, msb(MARKET_Q)), UP, buff=0.3))
        subsidy_dwl_word.add_updater(lambda m: m.set_opacity(
            smooth(np.clip((POSITIVE_Q - subsidized_q()) / 2, 0, 1))))
        for m in (subsidy_prices, subsidy_dwl, subsidy_dwl_word, subsidy_initial_price, subsidy_original_quantity):
            m.update()
        self.add(subsidy_original_quantity)
        takeaway = teaching('Start at the market equilibrium, with no subsidy.')
        self.play(FadeIn(subsidy_prices), FadeIn(subsidy_initial_price),
                  FadeIn(subsidy_dwl), FadeIn(subsidy_dwl_word), FadeIn(takeaway))
        self.pause('4.g.start')

        # ---- 4.g.prices · Raise the subsidy; price separation precedes the wedge explanation.
        self.remove(takeaway)
        takeaway = teaching('As the subsidy rises, prices separate and deadweight loss shrinks.')
        self.play(FadeIn(takeaway))
        self.play(subsidy.animate.set_value(EXTERNAL), run_time=3.6, rate_func=smooth)
        for m in (subsidy_prices, subsidy_dwl, subsidy_dwl_word, subsidy_initial_price, subsidy_original_quantity):
            m.clear_updaters()
        self.remove(subsidy_dwl, *list(subsidy_dwl), subsidy_dwl_word, subsidy_initial_price, takeaway)
        takeaway = teaching(r'A \$2 subsidy brings quantity to 48 and eliminates deadweight loss.')
        self.play(FadeIn(takeaway))
        self.pause('4.g.prices')

        # ---- 4.g · Extract a dashed measurement to the right, then leave it at the price axis.
        self.remove(takeaway)
        subsidy_wedge = fixed(Polygon(
            pax.c2p(POSITIVE_Q - 0.42, 2.4), pax.c2p(POSITIVE_Q + 0.42, 2.4),
            pax.c2p(POSITIVE_Q + 0.42, 4.4), pax.c2p(POSITIVE_Q - 0.42, 4.4),
            stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY).set_z_index(12))
        self.play(FadeIn(subsidy_wedge), run_time=0.6)
        subsidy_wedge_copy = fixed(DashedLine(pax.c2p(POSITIVE_Q, 2.4), pax.c2p(POSITIVE_Q, 4.4),
            color=GOV, stroke_width=2.5, dash_length=0.045)
            .put_start_and_end_on(pax.c2p(POSITIVE_Q, 2.4), pax.c2p(POSITIVE_Q, 4.4)).set_z_index(11))
        self.add(subsidy_wedge_copy)
        self.play(subsidy_wedge_copy.animate.shift(pax.c2p(88, 0) - pax.c2p(POSITIVE_Q, 0)), run_time=1.6)
        subsidy_wedge_caption = fixed(Tex(r'\$2 subsidy', color=GOV).scale(0.6)
            .next_to(subsidy_wedge_copy, RIGHT, buff=0.18).set_z_index(13))
        takeaway = teaching(r"The subsidy is the \$2 gap between the sellers' and buyers' prices.")
        self.play(FadeIn(subsidy_wedge_caption), FadeIn(takeaway))
        subsidy_axis_gap = fixed(DashedLine(pax.c2p(AXIS_GAP_Q, 2.4), pax.c2p(AXIS_GAP_Q, 4.4),
            color=GOV, stroke_width=2.5, dash_length=0.045)
            .put_start_and_end_on(pax.c2p(AXIS_GAP_Q, 2.4), pax.c2p(AXIS_GAP_Q, 4.4)).set_z_index(11))
        subsidy_word = fixed(Tex(r'Subsidy $=$ \$2', color=GOV).scale(0.6)
            .next_to(pax.c2p(0, 3.4), LEFT, buff=0.2).set_z_index(13))
        self.play(FadeOut(subsidy_wedge_copy), FadeOut(subsidy_wedge_caption),
                  FadeIn(subsidy_axis_gap), FadeIn(subsidy_word))
        self.pause('4.g')

        # ---- 4.g.curve · The same subsidy raises private benefit onto social benefit.
        # Added benefit is above MB: it has the same height and position as the pink EXT strips.
        self.remove(takeaway)
        subsidy_curve_external = fixed(VGroup(*[
            unit_slice(pax, q, mb, msb, EXT, BASE_OPACITY).set_z_index(-2) for q in range(POSITIVE_Q)]).set_z_index(-2))
        subsidy_curve_strips = fixed(VGroup(*[
            unit_slice(pax, q, mb, msb, GOV, STRIP_OPACITY).set_z_index(-1) for q in range(POSITIVE_Q)]).set_z_index(-1))
        subsidy_policy_curve = fixed(DashedLine(pax.c2p(0, 14), pax.c2p(70, 0), color=DEMAND, stroke_width=3))
        subsidy_policy_name = fixed(Tex(r'$\mathrm{MB}+\mathrm{subsidy}$', color=INK).scale(0.7)
            .next_to(pax.c2p(28, 8.4), UR, buff=0.12))
        subsidy_merged_name = fixed(Tex(r'$\mathrm{MSB}=\mathrm{MB}+\mathrm{subsidy}$', color=INK).scale(0.7)
            .next_to(pax.c2p(8, 12.4), UR, buff=0.10))
        takeaway = teaching(r'A \$2 subsidy lifts MB onto MSB: private and social benefits match.')
        self.play(FadeIn(subsidy_curve_external), FadeIn(takeaway))
        self.play(LaggedStart(*[FadeIn(bar) for bar in subsidy_curve_strips], lag_ratio=0.035),
                  FadeIn(subsidy_policy_curve), FadeIn(subsidy_policy_name), run_time=1.8)
        self.play(FadeOut(positive_curve_words[2]), FadeOut(subsidy_policy_name), FadeIn(subsidy_merged_name))
        self.pause('4.g.curve')
        self.play(FadeOut(subsidy_curve_strips), FadeOut(subsidy_curve_external), FadeOut(subsidy_policy_curve),
                  FadeOut(subsidy_merged_name), FadeIn(positive_curve_words[2]))

        # ---- 4.h · Units 41 to 48 now happen, and their deadweight loss is gone.
        self.remove(takeaway)
        takeaway = teaching('The subsidy enables worthwhile trades that the market leaves out.')
        self.play(FadeIn(takeaway))
        self.pause('4.h')

        # Group the unchanged market before carrying its selected unit out and back.
        positive_market = fixed(VGroup(pax, positive_axis_words, positive_demand, positive_supply,
            social_benefit, positive_curve_words, positive_original_guides, positive_dot,
            positive_efficient, subsidy_original_quantity, subsidy_wedge, subsidy_word, subsidy_axis_gap, subsidy_prices))
        self.remove(*[m for m in self.mobjects if m not in (head, context, takeaway)])
        self.add(positive_market)
        # ---- 4.h.select · Carry the same unit into C2's spread welfare layout.
        added_pair = fixed(VGroup(
            unit_slice(pax, 43, zero, mb, DEMAND, 0),
            unit_slice(pax, 43, mb, msb, EXT, 0),
            unit_slice(pax, 43, zero, mc, SUPPLY, 0)))
        added_home = added_pair.copy()
        added_box = fixed(SurroundingRectangle(added_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(takeaway)
        takeaway = teaching("Let's check an exchange that would not have happened before the subsidy.")
        self.play(FadeIn(added_pair), FadeIn(added_box), FadeIn(takeaway))
        self.pause('4.h.select')

        # ---- 4.h.values · Real private values and the externality, before prices or verdicts.
        added_target = fixed(VGroup())
        for left, low, high, color in [(BUYER_LEFT, 0, 3.2, DEMAND), (BUYER_LEFT, 3.2, 5.2, EXT),
                                       (SELLER_LEFT, 0, 4.2, SUPPLY)]:
            added_target.add(fixed(Polygon([left, detail_y(low), 0], [left + BAR_WIDTH, detail_y(low), 0],
                [left + BAR_WIDTH, detail_y(high), 0], [left, detail_y(high), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(positive_market), FadeOut(context), FadeOut(added_box), FadeOut(takeaway),
                  Transform(added_pair, added_target), run_time=1.6)
        added_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(added_target, [DEMAND, DEMAND, SUPPLY])],
            Line([-1.9, DETAIL_BASE, 0], [1.9, DETAIL_BASE, 0], color=MUTED))).set_z_index(3)
        added_values = fixed(VGroup(
            Tex(r'\$3.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(3.2), 0], LEFT, buff=0.25),
            Tex(r'\$5.20', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(5.2), 0], LEFT, buff=0.25),
            Tex(r'\$4.20', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(4.2), 0], RIGHT, buff=0.45),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(3.2), 0], UP, buff=0.10),
            Tex('MSB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(5.2), 0], UP, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(4.2), 0], DOWN, buff=0.10),
            Tex('EXT', color=EXT).scale(0.55).move_to([-1.21, detail_y(4.2), 0]))).set_z_index(4)
        unit_context = fixed(subtitle(head, 'The 44th unit: an exchange the subsidy enables.'))
        added_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(detail_people)
        self.play(FadeIn(added_edges), FadeIn(added_values), FadeIn(unit_context), FadeIn(added_questions[0]), FadeIn(added_questions[1]))
        self.pause('4.h.values')

        # ---- 4.h.prices · Government's transfer spans actual prices, not MB or MC.
        added_prices = fixed(VGroup(
            Line([-2.6, detail_y(2.4), 0], [1.9, detail_y(2.4), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(4.4), 0], [1.9, detail_y(4.4), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        added_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(2.4), 0], DOWN, buff=0.06),
            Tex(r'\$2.40', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(2.4), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(4.4), 0], UP, buff=0.06),
            Tex(r'\$4.40', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(4.4), 0], LEFT, buff=0.15))).set_z_index(4)
        added_transfer = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(2.4), 0], [TAX_LEFT + TAX_WIDTH, detail_y(2.4), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(4.4), 0], [TAX_LEFT, detail_y(4.4), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=GOV_OPACITY),
            Tex('subsidy', color=INK).scale(.42).move_to([0, detail_y(3.4), 0]))).set_z_index(3)
        self.play(FadeIn(added_prices), FadeIn(added_price_words), FadeIn(added_transfer))
        self.pause('4.h.prices')

        # ---- 4.h.buyer · First ask whether the buyer's value covers the buyer's price.
        added_buyer_guides = fixed(VGroup(
            DashedLine(added_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(2.4), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(2.4), 0], [-4.25, detail_y(3.2), 0], color=DEMAND, stroke_width=3)))
        added_cs = fixed(Polygon(
            [BUYER_LEFT, detail_y(2.4), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(2.4), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(3.2), 0], [BUYER_LEFT, detail_y(3.2), 0],
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY).set_z_index(1))
        added_cs_word = fixed(Tex('CS', color=INK).scale(0.55)
            .move_to([-1.21, detail_y(2.8), 0]).set_z_index(4))
        takeaway = teaching(r'The buyer: value \$3.20 against a price of \$2.40.')
        self.play(FadeIn(added_buyer_guides), GrowFromEdge(added_cs, DOWN), FadeIn(added_cs_word), FadeIn(takeaway))
        self.pause('4.h.buyer')

        # ---- 4.h.buyer.answer · Finish the buyer's decision before moving to the seller.
        added_buyer_answer = fixed(VMobject(color=EFFICIENT, stroke_width=5)
            .set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)
            .next_to(added_buyer_guides[-1], LEFT, buff=0.3))
        self.play(FadeIn(added_buyer_answer))
        self.pause('4.h.buyer.answer')

        # ---- 4.h.seller · Then compare the seller's cost with the amount the seller receives.
        self.remove(takeaway)
        added_seller_guides = fixed(VGroup(
            DashedLine([SELLER_LEFT, detail_y(4.2), 0], [TAX_LEFT + TAX_WIDTH + 0.10, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.10, detail_y(4.2), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([BUYER_LEFT - 0.12, detail_y(4.2), 0], [added_price_words[3].get_right()[0] + 0.12, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([added_price_words[3].get_left()[0] - 0.12, detail_y(4.2), 0], [-4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(4.4), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.2), 0], [-4.25, detail_y(4.4), 0], color=SUPPLY, stroke_width=3)))
        added_ps = fixed(Polygon(
            [SELLER_LEFT, detail_y(4.2), 0], [SELLER_LEFT + BAR_WIDTH, detail_y(4.2), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(4.4), 0], [SELLER_LEFT, detail_y(4.4), 0],
            stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY).set_z_index(1))
        added_ps_word = fixed(Tex('PS', color=INK).scale(0.42)
            .next_to([1.21, detail_y(4.4), 0], UP, buff=0.08).set_z_index(4))
        takeaway = teaching(r'The seller: cost \$4.20 against a price of \$4.40.')
        self.play(FadeIn(added_seller_guides), GrowFromEdge(added_ps, DOWN), FadeIn(added_ps_word), FadeIn(takeaway))
        self.pause('4.h.seller')

        # ---- 4.h.private · Complete the seller's decision, keeping both individual verdicts.
        self.remove(takeaway)
        added_seller_answer = fixed(added_buyer_answer.copy()
            .next_to(added_seller_guides[-1], LEFT, buff=0.3))
        added_private_answer = fixed(VGroup(added_buyer_answer, added_seller_answer))
        takeaway = teaching('Both sides want this trade at these prices.')
        self.play(FadeIn(added_seller_answer), FadeIn(takeaway))
        self.remove(added_buyer_answer, added_seller_answer)
        self.add(added_private_answer)
        self.pause('4.h.private')

        # ---- 4.h.social.compare · C1's real benefit/cost comparison excludes government transfers.
        self.remove(takeaway)
        added_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(5.2), 0], [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(4.2), 0], [4.25, detail_y(5.2), 0], color=TOTAL, stroke_width=3)))
        added_social_answer = fixed(VGroup(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex('TS', color=TOTAL))
            .arrange(DOWN, buff=0.16).scale(0.70)
            .next_to([4.25, detail_y(4.7), 0], RIGHT, buff=0.3))
        self.play(added_transfer.animate.set_opacity(0.20),
                  added_prices.animate.set_opacity(0.25), added_price_words.animate.set_opacity(0.25),
                  added_buyer_guides.animate.set_opacity(0.25), added_seller_guides.animate.set_opacity(0.25),
                  FadeOut(added_cs), FadeOut(added_ps),
                  FadeOut(added_cs_word), FadeOut(added_ps_word),
                  FadeIn(added_social_guides))
        self.pause('4.h.social.compare')

        # ---- 4.h.social · Same TS/DWL interval and verdict as C1.
        takeaway = teaching(r'Good: this trade is worth \$1 to society.')
        self.play(FadeIn(added_social_answer), FadeIn(takeaway))
        self.pause('4.h.social')

        # ---- 4.h.return · Remove every annotation and return the same three slices.
        self.remove(detail_people)
        self.play(FadeOut(added_edges), FadeOut(added_values), FadeOut(added_questions),
                  FadeOut(added_prices), FadeOut(added_price_words), FadeOut(added_transfer),
                  FadeOut(added_buyer_guides), FadeOut(added_seller_guides),
                  FadeOut(added_private_answer), FadeOut(added_social_guides), FadeOut(added_social_answer),
                  FadeOut(takeaway), FadeOut(unit_context), run_time=0.4)
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
            Tex(r'$\mathrm{Subsidy}=\mathrm{EXT}$', color=DEFINITION).scale(1.10),
            Tex(r'$\Downarrow$', color=DEFINITION).scale(0.85),
            Tex('48 units', color=CAPTION).scale(0.65),
            Tex(r'$Q^{subsidy}=Q^*$', color=GUIDE).scale(1.10)
        ).arrange(DOWN, buff=0.22).move_to([4.2, 0.7, 0]))
        takeaway = teaching('A corrective subsidy enables worthwhile exchanges the market would miss.')
        self.play(FadeIn(positive_equality[0]))
        self.play(FadeIn(positive_equality[1:]), FadeIn(takeaway))
        self.pause('5.a')
