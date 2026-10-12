# maniml C2_Animations.py C2
# Storyboard: C2_Notes.typ. All lesson choreography stays in construct().
# C1's spinach market, MB = 12 - Q/5 and MC = 2 + Q/20, Q in tons and values in dollars per ton.
# A $2 tax lands on C1's 32nd ton and a $2 subsidy on its 48th; the 36th ton is the exchange the tax removes.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects


def wedge_state(tax, demand_slope, supply_slope):
    """Quantity, buyers' price, and sellers' price when a wedge of size `tax`
    sits between linear curves that cross at (40, 4). A subsidy is a negative tax."""
    shortfall = tax / (demand_slope + supply_slope)
    return 40 - shortfall, 4 + demand_slope * shortfall, 4 - supply_slope * shortfall


class C2(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        MARKET_Q, MARKET_P = 40, 4
        TAX, TAX_Q, BUYER_PRICE, SELLER_PRICE = 2, 32, 5.6, 3.6
        SUBSIDY_Q, SUBSIDY_BUYER, SUBSIDY_SELLER = 48, 2.4, 4.4
        LOST_TON, ADDED_TON = 35, 47  # Ton 36 is removed by the tax; ton 48 is added by the subsidy.
        BAR_GAP = 0.08
        BASE_OPACITY, SURPLUS_OPACITY = 0.16, 0.65
        STRIP_OPACITY = 0.5
        # Close-ups: the first ton at 0.35 per dollar, C1's detail tons at 0.68 per dollar.
        DETAIL_BASE, DETAIL_SCALE, FIRST_SCALE = -2.05, 0.68, 0.35
        BUYER_LEFT, SELLER_LEFT, BAR_WIDTH, PRICE_LABEL_X = -1.16, 0.06, 1.1, -3.2
        first_y = lambda dollars: DETAIL_BASE + dollars * FIRST_SCALE
        detail_y = lambda dollars: DETAIL_BASE + dollars * DETAIL_SCALE
        # Updaters read the live model from attributes on the mobject, never from closures.
        state = lambda m: wedge_state(m.tax.get_value(), m.d.get_value(), m.s.get_value())

        # ---- 0.a · The shared bumper with C2's thesis.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'C', 2)
        thesis = Tex(r'\textit{Governments can change your behavior.}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.remove(squares, episode, thesis)

        # ---- 1.a · Last time: the full market with its surplus regions.
        head = fixed(title('Competitive Equilibrium'))
        context = fixed(subtitle(head, 'A market without externalities.'))
        ax = style_axes([0, 60, 10], [0, 13, 2], x_length=10, y_length=4.6)
        ax.shift(np.array([-5, BODY_MID - 2.15, 0]) - ax.c2p(0, 0))
        fixed(ax)
        # The unit caption sits beside P, as in B5, so the subtitles above the market never touch it.
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73)))
        intercepts = fixed(VGroup(
            Tex('$2$', color=SUPPLY).scale(0.65).next_to(ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('$12$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, 12), LEFT, buff=0.15)))
        demand = fixed(Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        supply = fixed(Line(ax.c2p(0, 2), ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        curve_words = fixed(VGroup(
            Tex('D / MB', color=INK).scale(0.7).next_to(ax.c2p(8, 10.4), UR, buff=0.12),
            Tex('S / MC', color=INK).scale(0.7).next_to(ax.c2p(60, 5), RIGHT, buff=0.15)))
        equilibrium = fixed(VGroup(
            Dot(ax.c2p(40, 4), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            Tex(r'$P^*=4$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 4), LEFT, buff=0.2),
            Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20)))
        costs, cs, ps = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            costs.add(fixed(Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY)))
            cs.add(fixed(Polygon(ax.c2p(left, 4), ax.c2p(right, 4),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY)))
            ps.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 4), ax.c2p(left, 4),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY)))
        surplus_words = fixed(VGroup(
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(MARKET_Q / 3, (12 + 2 * MARKET_P) / 3)),
            Tex('PS', color=INK).scale(0.72).move_to(ax.c2p(MARKET_Q / 3, (2 + 2 * MARKET_P) / 3))))
        self.play(FadeIn(head), FadeIn(context), FadeIn(costs), FadeIn(ax), FadeIn(axis_words), FadeIn(intercepts),
                  FadeIn(demand), FadeIn(supply), FadeIn(curve_words), FadeIn(equilibrium))
        self.play(FadeIn(ps), FadeIn(surplus_words[1]))
        self.play(FadeIn(cs), FadeIn(surplus_words[0]))
        # One group carries the whole market out of and back into every close-up.
        market = fixed(VGroup(ax, axis_words, intercepts, costs, cs, ps, demand, supply, curve_words,
                             equilibrium, surplus_words))
        self.remove(*[m for m in self.mobjects if m is not head and m is not context])
        self.add(market)
        self.pause('1.a')

        # The people of every close-up: C1's teal buyer and orange seller, plus a green government.
        people, government = fixed(Group()), fixed(Group())
        for x, color, name, group in [(-1.45, DEMAND, 'Buyer', people), (1.45, SUPPLY, 'Seller', people),
                                      (0, GOV, 'Government', government)]:
            group.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([x, DETAIL_BASE - 0.60, 0])))
            group.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            group.add(fixed(Tex(name, color=INK).scale(0.65).move_to([x, DETAIL_BASE - 0.94, 0])))

        # ---- 2.a.select · A per-unit tax, asked of the first exchange.
        self.remove(head, context)
        head = fixed(title('A Per-Unit Tax'))
        context = fixed(subtitle(head, r'The government collects \$2 on each ton exchanged.'))
        l0, r0 = BAR_GAP / 2, 1 - BAR_GAP / 2
        # Market slice and close-up share one structure: buyer base, CS, MB edge, cost, PS, MC edge, baseline, price.
        first_home = fixed(VGroup(
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 4), ax.c2p(l0, 4),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(ax.c2p(l0, 4), ax.c2p(r0, 4), ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 12 - l0 / 5), ax.c2p(r0, 12 - r0 / 5), color=DEMAND, stroke_width=3),
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 2 + r0 / 20), ax.c2p(l0, 2 + l0 / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
            Polygon(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), ax.c2p(r0, 4), ax.c2p(l0, 4),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), color=SUPPLY, stroke_width=3),
            Line(ax.c2p(l0, 0), ax.c2p(r0, 0), color=MUTED),
            Line(ax.c2p(l0, 4), ax.c2p(r0, 4), color=GUIDE, stroke_width=2)))
        first_target = fixed(VGroup(
            Polygon([BUYER_LEFT, first_y(0), 0], [BUYER_LEFT + BAR_WIDTH, first_y(0), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(4), 0], [BUYER_LEFT, first_y(4), 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=BASE_OPACITY),
            Polygon([BUYER_LEFT, first_y(4), 0], [BUYER_LEFT + BAR_WIDTH, first_y(4), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=BASE_OPACITY),
            Line([BUYER_LEFT, first_y(12), 0], [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], color=DEMAND, stroke_width=3),
            Polygon([SELLER_LEFT, first_y(0), 0], [SELLER_LEFT + BAR_WIDTH, first_y(0), 0],
                [SELLER_LEFT + BAR_WIDTH, first_y(2), 0], [SELLER_LEFT, first_y(2), 0],
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
            Polygon([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0],
                [SELLER_LEFT + BAR_WIDTH, first_y(4), 0], [SELLER_LEFT, first_y(4), 0],
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0),
            Line([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0], color=SUPPLY, stroke_width=3),
            Line([-1.3, first_y(0), 0], [1.3, first_y(0), 0], color=MUTED),
            Line([-1.3, first_y(4), 0], [1.3, first_y(4), 0], color=GUIDE, stroke_width=2).set_opacity(0)))
        first_words = fixed(VGroup(
            Tex(r'MB \$12', color=DEMAND).scale(0.7).next_to(first_target[2], LEFT, buff=0.22),
            Tex(r'MC \$2', color=SUPPLY).scale(0.7).next_to(first_target[5], RIGHT, buff=0.22),
            Tex(r'Price \$4', color=GUIDE).scale(0.7).next_to([PRICE_LABEL_X, first_y(4), 0], LEFT, buff=0.1),
            Tex(r'CS \$8', color=DEMAND).scale(0.7).next_to(first_target[1], LEFT, buff=0.22),
            Tex(r'PS \$2', color=SUPPLY).scale(0.7).next_to(first_target[4], RIGHT, buff=0.22)))
        first_pair = first_home.copy()
        first_selection = fixed(SurroundingRectangle(first_home, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(head), FadeIn(context), FadeIn(first_pair), FadeIn(first_selection))
        self.pause('2.a.select')

        # ---- 2.a.values · The review close-up: values first, then the price, then both surpluses.
        self.play(FadeOut(market), FadeOut(first_selection), Transform(first_pair, first_target), run_time=1.6)
        # Bind the value labels to the live bars so they follow the return zoom.
        first_words[0].bars = first_words[1].bars = first_pair
        first_words[0].add_updater(lambda m: m.next_to(m.bars[2], LEFT, buff=0.22))
        first_words[1].add_updater(lambda m: m.next_to(m.bars[5], RIGHT, buff=0.22))
        self.add(people)
        self.play(FadeIn(first_words[:2]))
        self.pause('2.a.values')
        self.play(first_pair[7].animate.set_opacity(1), FadeIn(first_words[2]))
        self.play(first_pair[1].animate.set_fill(opacity=SURPLUS_OPACITY), first_pair[4].animate.set_fill(opacity=SURPLUS_OPACITY),
                  FadeIn(first_words[3:]))

        # ---- 2.a · A third party arrives with a question.
        question = fixed(Tex(r'Who hands the \$2 to the government?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(government)
        self.play(FadeIn(question))
        self.pause('2.a')

        # ---- 2.b · The seller hands it over: the tax replaces the seller's surplus.
        tax_slice = fixed(VGroup(
            Polygon([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0],
                [SELLER_LEFT + BAR_WIDTH, first_y(4), 0], [SELLER_LEFT, first_y(4), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex(r'Tax \$2', color=INK).scale(0.6)))
        tax_slice[1].move_to(tax_slice[0])
        seller_note = fixed(Tex(r'If the seller hands it over, the seller collects \$4 but keeps only \$2.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(question)
        self.play(FadeOut(first_words[4]), run_time=0.4)
        self.play(first_pair[4].animate.set_fill(opacity=0), FadeIn(tax_slice), FadeIn(seller_note))
        self.pause('2.b')

        # ---- 2.c · The buyer hands it over: the same slice moves above the price.
        buyer_tax_target = fixed(VGroup(
            Polygon([BUYER_LEFT, first_y(4), 0], [BUYER_LEFT + BAR_WIDTH, first_y(4), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(6), 0], [BUYER_LEFT, first_y(6), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex(r'Tax \$2', color=INK).scale(0.6)))
        buyer_tax_target[1].move_to(buyer_tax_target[0])
        cs_after_tax = fixed(Polygon([BUYER_LEFT, first_y(6), 0], [BUYER_LEFT + BAR_WIDTH, first_y(6), 0],
            [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY))
        cs_six = fixed(Tex(r'CS \$6', color=DEMAND).scale(0.7).next_to(cs_after_tax, LEFT, buff=0.22))
        buyer_note = fixed(Tex(r'If the buyer hands it over, the buyer pays \$6 and the seller receives \$4.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(seller_note)
        self.play(FadeOut(first_words[3]), run_time=0.4)
        self.play(Transform(tax_slice, buyer_tax_target), Transform(first_pair[1], cs_after_tax),
                  first_pair[4].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(first_words[4]),
                  FadeIn(cs_six), FadeIn(buyer_note), run_time=1.2)
        self.pause('2.c')

        # ---- 2.d · Name the two prices; the gap between them is the tax either way.
        price_s = fixed(Tex(r'$P_s$ \$4', color=GUIDE).scale(0.7).next_to([PRICE_LABEL_X, first_y(4), 0], LEFT, buff=0.1))
        price_b = fixed(VGroup(
            Line([BUYER_LEFT - 0.14, first_y(6), 0], [BUYER_LEFT + BAR_WIDTH + 0.14, first_y(6), 0], color=GUIDE, stroke_width=2),
            Tex(r'$P_b$ \$6', color=GUIDE).scale(0.7).next_to([PRICE_LABEL_X, first_y(6), 0], LEFT, buff=0.1)))
        identity_note = fixed(Tex(r'Either way, the price buyers pay exceeds the price sellers receive by \$2.', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(buyer_note, first_words[2])
        self.play(FadeIn(price_s), FadeIn(price_b), FadeIn(identity_note))
        self.pause('2.d')

        # ---- 2.d.return · Back to the market, with the tax slice left behind.
        self.remove(people, government)
        self.play(FadeOut(first_words[4]), FadeOut(cs_six), FadeOut(price_s), FadeOut(price_b),
                  FadeOut(tax_slice), FadeOut(identity_note), run_time=0.4)
        self.play(FadeOut(first_words[0], suspend_mobject_updating=False), FadeOut(first_words[1], suspend_mobject_updating=False),
                  Transform(first_pair, first_home), FadeIn(market), run_time=1.6)
        self.play(FadeOut(first_pair))
        self.pause('2.d.return')

        # ---- 3.a · A tax on sellers: every cost bar carries a $2 strip, and supply shifts up.
        self.remove(head, context)
        head = fixed(title('A Tax On Sellers'))
        context = fixed(subtitle(head, r'Sellers hand \$2 per ton to the government.'))
        seller_note = fixed(Tex(r'Each ton now costs sellers \$2 more to bring to market.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        seller_strips, seller_potential = fixed(VGroup()), fixed(VGroup())
        for q in range(60):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            strip = fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 4 + right / 20), ax.c2p(left, 4 + left / 20),
                stroke_width=0, fill_color=GOV, fill_opacity=STRIP_OPACITY if q < MARKET_Q else 0.12))
            (seller_strips if q < MARKET_Q else seller_potential).add(strip)
        taxed_supply = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(60, 7), color=SUPPLY, stroke_width=3))
        taxed_supply_word = fixed(Tex('MC $+$ tax', color=INK).scale(0.7).next_to(ax.c2p(60, 7), RIGHT, buff=0.15))
        # The surplus fills rest while the curves move; welfare returns in section 6.
        market.remove(equilibrium, surplus_words)
        self.play(FadeIn(head), FadeIn(context), FadeIn(seller_note), FadeOut(equilibrium), FadeOut(surplus_words),
                  cs.animate.set_fill(opacity=0), ps.animate.set_fill(opacity=0))
        self.play(LaggedStart(*[FadeIn(strip) for strip in seller_strips], lag_ratio=0.05), run_time=2.4)
        self.play(FadeIn(seller_potential), FadeIn(taxed_supply), FadeIn(taxed_supply_word))
        self.pause('3.a')

        # ---- 3.b.quantity · Where the taxed supply meets demand.
        seller_question = fixed(Tex('Where does the taxed supply meet demand?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        taxed_point = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$Q=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20)))
        self.remove(seller_note)
        self.play(FadeIn(seller_question))
        self.play(FadeIn(taxed_point),
                  *[bar.animate.set_fill(opacity=0.05) for bar in list(costs)[TAX_Q:] + list(seller_strips)[TAX_Q:]])
        self.pause('3.b.quantity')

        # ---- 3.b · Buyers pay the demand price; sellers keep the original supply price.
        buyer_readout = fixed(VGroup(
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2)))
        seller_readout = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2)))
        seller_result = fixed(Tex(r'32 tons: buyers pay \$5.60, and sellers keep \$3.60 after the tax.', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(buyer_readout))
        self.play(FadeIn(seller_readout))
        self.remove(seller_question)
        self.play(FadeIn(seller_result))
        self.pause('3.b')

        # ---- 4.a · A tax on buyers: every buyer bar loses a $2 strip, and demand shifts down.
        self.remove(head, context, seller_result)
        head = fixed(title('A Tax On Buyers'))
        context = fixed(subtitle(head, r'Buyers hand \$2 per ton to the government.'))
        buyer_note = fixed(Tex(r'After the tax, buyers will pay sellers \$2 less for each ton.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        buyer_strips, buyer_potential = fixed(VGroup()), fixed(VGroup())
        for q in range(50):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            strip = fixed(Polygon(ax.c2p(left, 10 - left / 5), ax.c2p(right, 10 - right / 5),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=GOV, fill_opacity=STRIP_OPACITY if q < MARKET_Q else 0.12))
            (buyer_strips if q < MARKET_Q else buyer_potential).add(strip)
        taxed_demand = fixed(DashedLine(ax.c2p(0, 10), ax.c2p(50, 0), color=DEMAND, stroke_width=3))
        taxed_demand_word = fixed(Tex('MB $-$ tax', color=INK).scale(0.7).next_to(ax.c2p(50, 0), UR, buff=0.12))
        self.play(FadeIn(head), FadeIn(context), FadeIn(buyer_note), FadeIn(equilibrium),
                  FadeOut(seller_strips), FadeOut(seller_potential), FadeOut(taxed_supply), FadeOut(taxed_supply_word),
                  FadeOut(taxed_point), FadeOut(buyer_readout), FadeOut(seller_readout),
                  *[bar.animate.set_fill(opacity=BASE_OPACITY) for bar in list(costs)[TAX_Q:]])
        self.play(LaggedStart(*[FadeIn(strip) for strip in buyer_strips], lag_ratio=0.05), run_time=2.4)
        self.play(FadeIn(buyer_potential), FadeIn(taxed_demand), FadeIn(taxed_demand_word))
        self.pause('4.a')

        # ---- 4.b.quantity · Where the taxed demand meets supply.
        buyer_question = fixed(Tex('Where does the taxed demand meet supply?', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        taxed_point = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$Q=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20)))
        self.remove(buyer_note)
        self.play(FadeIn(buyer_question))
        self.play(FadeIn(taxed_point), FadeOut(equilibrium),
                  *[bar.animate.set_fill(opacity=0.05) for bar in list(costs)[TAX_Q:] + list(buyer_strips)[TAX_Q:]])
        self.pause('4.b.quantity')

        # ---- 4.b · Sellers receive the supply price; buyers pay it plus the tax, on the original demand.
        seller_readout = fixed(VGroup(
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2)))
        buyer_readout = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2)))
        buyer_result = fixed(Tex(r'32 tons again: sellers receive \$3.60, and buyers pay \$3.60 $+$ \$2 $=$ \$5.60.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(seller_readout))
        self.play(FadeIn(buyer_readout))
        self.remove(buyer_question)
        self.play(FadeIn(buyer_result))
        self.pause('4.b')

        # ---- 4.c · The same outcome from either side.
        equivalence = fixed(Tex("It doesn't matter who hands over the tax: same quantity, same two prices.", color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(buyer_result)
        self.play(FadeIn(equivalence))
        self.pause('4.c')

        # ---- 5.a · The tax wedge slides in from the left until it gets stuck.
        self.remove(head, context, equivalence)
        head = fixed(title('The Tax Wedge'))
        self.play(FadeIn(head), FadeOut(buyer_strips), FadeOut(buyer_potential), FadeOut(taxed_demand),
                  FadeOut(taxed_demand_word), FadeOut(taxed_point), FadeOut(seller_readout), FadeOut(buyer_readout),
                  *[bar.animate.set_fill(opacity=BASE_OPACITY) for bar in list(costs)[TAX_Q:]])
        slide_q = ValueTracker(-9)
        sliding_wedge = fixed(VGroup(
            Line(ax.c2p(-9, SELLER_PRICE), ax.c2p(-9, BUYER_PRICE), color=GOV, stroke_width=6),
            Line(ax.c2p(-9, SELLER_PRICE) + LEFT * 0.09, ax.c2p(-9, SELLER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(ax.c2p(-9, BUYER_PRICE) + LEFT * 0.09, ax.c2p(-9, BUYER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3)))
        sliding_word = fixed(Tex(r'\$2 tax', color=GOV).scale(0.6).next_to(ax.c2p(-9, 4.6), LEFT, buff=0.12))
        for part in [*sliding_wedge, sliding_word]:
            part.axes, part.quantity = ax, slide_q
        sliding_wedge[0].add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(m.quantity.get_value(), SELLER_PRICE), m.axes.c2p(m.quantity.get_value(), BUYER_PRICE)))
        sliding_wedge[1].add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), SELLER_PRICE)))
        sliding_wedge[2].add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), BUYER_PRICE)))
        sliding_word.add_updater(lambda m: m.next_to(m.axes.c2p(m.quantity.get_value(), 4.6), LEFT, buff=0.12))
        slide_note = fixed(Tex('Slide the tax in from the left until it gets stuck between the curves.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(sliding_wedge), FadeIn(sliding_word), FadeIn(slide_note))
        self.play(slide_q.animate.set_value(TAX_Q), run_time=2.6, rate_func=smooth)
        self.pause('5.a')

        # ---- 5.b · Stuck: both prices and the quantity follow from the wedge.
        sliding_wedge.clear_updaters()
        sliding_word.clear_updaters()
        wedge_marks = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2),
            Tex(r'$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2),
            Tex(r'$Q=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20)))
        wedge_marks.set_z_index(2)
        sliding_wedge.set_z_index(2)
        wedge_definition = fixed(Tex("The tax wedge: the buyers' price minus the sellers' price equals the tax.", color=DEFINITION)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(slide_note)
        self.play(FadeIn(wedge_marks), FadeIn(wedge_definition),
                  sliding_word.animate.next_to(ax.c2p(TAX_Q, BUYER_PRICE), UR, buff=0.12),
                  *[bar.animate.set_fill(opacity=0.05) for bar in list(costs)[TAX_Q:]])
        self.pause('5.b')

        # ---- 5.c.wedge · Make room, then solve the wedge equation line by line.
        graph_block = fixed(VGroup(market, sliding_wedge, sliding_word, wedge_marks))
        self.remove(market, sliding_wedge, sliding_word, wedge_marks)
        self.add(graph_block)
        solve_note = fixed(Tex('Use the wedge equation and the two curves to solve for the quantity.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(wedge_definition)
        self.play(graph_block.animate.scale(0.72, about_point=ax.c2p(0, 0)).shift(LEFT * 1.0), run_time=1.1)
        divider = fixed(Line([2.45, -3.0, 0], [2.45, 2.3, 0], color=MUTED, stroke_width=1.5))
        wedge_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$-$', color=INK), Tex('$P_s$', color=GUIDE),
            Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        substitute_line = fixed(VGroup(Tex('$(12 - Q/5)$', color=DEMAND), Tex('$-$', color=INK),
            Tex('$(2 + Q/20)$', color=SUPPLY), Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        simplify_line = fixed(VGroup(Tex('$10 - Q/4$', color=INK), Tex('$=$', color=INK), Tex('$2$', color=GOV))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        solve_line = fixed(VGroup(Tex('$Q$', color=GUIDE), Tex('$=$', color=INK), Tex('$32$', color=GUIDE))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        buyer_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$=$', color=INK), Tex('$12 - 32/5$', color=DEMAND),
            Tex('$=$', color=INK), Tex('$5.60$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        seller_line = fixed(VGroup(Tex('$P_s$', color=GUIDE), Tex('$=$', color=INK), Tex('$2 + 32/20$', color=SUPPLY),
            Tex('$=$', color=INK), Tex('$3.60$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        algebra = fixed(VGroup(wedge_line, substitute_line, simplify_line, solve_line, buyer_line, seller_line)
            .arrange(DOWN, buff=0.34).move_to([5.2, 0.15, 0]))
        self.play(FadeIn(divider), FadeIn(wedge_line), FadeIn(solve_note))
        self.pause('5.c.wedge')
        self.play(FadeIn(substitute_line))
        self.pause('5.c.substitute')
        self.play(FadeIn(simplify_line))
        self.pause('5.c.simplify')
        self.play(FadeIn(solve_line))
        self.pause('5.c.solve')
        price_note = fixed(Tex('Then read each price from its own curve.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(solve_note)
        self.play(FadeIn(buyer_line), FadeIn(price_note))
        self.play(FadeIn(seller_line))
        self.pause('5.c')
        self.play(FadeOut(algebra), FadeOut(divider), FadeOut(price_note), run_time=0.5)
        self.play(graph_block.animate.shift(RIGHT * 1.0).scale(1 / 0.72, about_point=ax.c2p(0, 0) + RIGHT * 1.0), run_time=1.1)
        self.remove(graph_block)
        self.add(market, sliding_wedge, sliding_word, wedge_marks)

        # ---- 6.a.select · Welfare with a tax, starting from the first exchange again.
        self.remove(head)
        head = fixed(title('Welfare With A Tax'))
        context = fixed(subtitle(head, r'32 tons exchanged: buyers pay \$5.60 and sellers receive \$3.60.'))
        # Market slice and close-up: buyer bar, tax, CS, MB edge, cost, PS, MC edge, baseline, P_b line, P_s line.
        taxed_first_home = fixed(VGroup(
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(ax.c2p(l0, SELLER_PRICE), ax.c2p(r0, SELLER_PRICE), ax.c2p(r0, BUYER_PRICE), ax.c2p(l0, BUYER_PRICE),
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Polygon(ax.c2p(l0, BUYER_PRICE), ax.c2p(r0, BUYER_PRICE), ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 12 - l0 / 5), ax.c2p(r0, 12 - r0 / 5), color=DEMAND, stroke_width=3),
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 2 + r0 / 20), ax.c2p(l0, 2 + l0 / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
            Polygon(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), ax.c2p(r0, SELLER_PRICE), ax.c2p(l0, SELLER_PRICE),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), color=SUPPLY, stroke_width=3),
            Line(ax.c2p(l0, 0), ax.c2p(r0, 0), color=MUTED),
            Line(ax.c2p(l0, BUYER_PRICE), ax.c2p(r0, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Line(ax.c2p(l0, SELLER_PRICE), ax.c2p(r0, SELLER_PRICE), color=GUIDE, stroke_width=2)))
        taxed_first_target = fixed(VGroup(
            Polygon([BUYER_LEFT, first_y(0), 0], [BUYER_LEFT + BAR_WIDTH, first_y(0), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=BASE_OPACITY),
            Polygon([BUYER_LEFT, first_y(SELLER_PRICE), 0], [BUYER_LEFT + BAR_WIDTH, first_y(SELLER_PRICE), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(BUYER_PRICE), 0], [BUYER_LEFT, first_y(BUYER_PRICE), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=0),
            Polygon([BUYER_LEFT, first_y(BUYER_PRICE), 0], [BUYER_LEFT + BAR_WIDTH, first_y(BUYER_PRICE), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Line([BUYER_LEFT, first_y(12), 0], [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], color=DEMAND, stroke_width=3),
            Polygon([SELLER_LEFT, first_y(0), 0], [SELLER_LEFT + BAR_WIDTH, first_y(0), 0],
                [SELLER_LEFT + BAR_WIDTH, first_y(2), 0], [SELLER_LEFT, first_y(2), 0],
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
            Polygon([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0],
                [SELLER_LEFT + BAR_WIDTH, first_y(SELLER_PRICE), 0], [SELLER_LEFT, first_y(SELLER_PRICE), 0],
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0),
            Line([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0], color=SUPPLY, stroke_width=3),
            Line([-1.3, first_y(0), 0], [1.3, first_y(0), 0], color=MUTED),
            Line([-1.3, first_y(BUYER_PRICE), 0], [1.3, first_y(BUYER_PRICE), 0], color=GUIDE, stroke_width=2).set_opacity(0),
            Line([-1.3, first_y(SELLER_PRICE), 0], [1.3, first_y(SELLER_PRICE), 0], color=GUIDE, stroke_width=2).set_opacity(0)))
        taxed_first_words = fixed(VGroup(
            Tex(r'MB \$12', color=DEMAND).scale(0.7).next_to(taxed_first_target[3], LEFT, buff=0.22),
            Tex(r'MC \$2', color=SUPPLY).scale(0.7).next_to(taxed_first_target[6], RIGHT, buff=0.22),
            Tex(r'$P_b$ \$5.60', color=GUIDE).scale(0.7).next_to([PRICE_LABEL_X, first_y(BUYER_PRICE), 0], LEFT, buff=0.1),
            Tex(r'$P_s$ \$3.60', color=GUIDE).scale(0.7).next_to([PRICE_LABEL_X, first_y(SELLER_PRICE), 0], LEFT, buff=0.1),
            Tex(r'PS \$1.60', color=SUPPLY).scale(0.7).next_to(taxed_first_target[5], RIGHT, buff=0.22).shift(UP * 0.1),
            Tex(r'Tax \$2', color=INK).scale(0.6).move_to(taxed_first_target[1]),
            Tex(r'CS \$6.40', color=DEMAND).scale(0.7).next_to(taxed_first_target[2], LEFT, buff=0.22)))
        # The selected slice shows no split yet: fills and price lines stay hidden until the close-up reveals them.
        taxed_first_pair = taxed_first_home.copy()
        for index in (1, 2, 5):
            taxed_first_pair[index].set_fill(opacity=0)
        for index in (8, 9):
            taxed_first_pair[index].set_opacity(0)
        first_selection = fixed(SurroundingRectangle(taxed_first_home, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxed_first_pair), FadeIn(first_selection))
        self.pause('6.a.select')

        # ---- 6.a.prices · Values first, then both market prices.
        self.play(FadeOut(market), FadeOut(sliding_wedge), FadeOut(sliding_word), FadeOut(wedge_marks),
                  FadeOut(first_selection), Transform(taxed_first_pair, taxed_first_target), run_time=1.6)
        taxed_first_words[0].bars = taxed_first_words[1].bars = taxed_first_pair
        taxed_first_words[0].add_updater(lambda m: m.next_to(m.bars[3], LEFT, buff=0.22))
        taxed_first_words[1].add_updater(lambda m: m.next_to(m.bars[6], RIGHT, buff=0.22))
        self.add(people, government)
        self.play(FadeIn(taxed_first_words[:2]))
        self.play(taxed_first_pair[8].animate.set_opacity(1), taxed_first_pair[9].animate.set_opacity(1),
                  FadeIn(taxed_first_words[2:4]))
        self.pause('6.a.prices')

        # ---- 6.a · The ton's surplus splits three ways and the exchange survives.
        split_note = fixed(Tex(r'The tax moves \$2 of surplus to the government; the exchange still happens.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(taxed_first_pair[5].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_words[4]))
        self.play(taxed_first_pair[1].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_words[5]))
        self.play(taxed_first_pair[2].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_words[6]),
                  FadeIn(split_note))
        self.pause('6.a')

        # ---- 6.b · Back to the market: every exchanged ton splits the same way.
        ps_taxed, tax_bars, cs_taxed = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(TAX_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            ps_taxed.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, SELLER_PRICE), ax.c2p(left, SELLER_PRICE),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY)))
            tax_bars.add(fixed(Polygon(ax.c2p(left, SELLER_PRICE), ax.c2p(right, SELLER_PRICE),
                ax.c2p(right, BUYER_PRICE), ax.c2p(left, BUYER_PRICE),
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY)))
            cs_taxed.add(fixed(Polygon(ax.c2p(left, BUYER_PRICE), ax.c2p(right, BUYER_PRICE),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY)))
        welfare_words = fixed(VGroup(
            Tex('PS', color=INK).scale(0.72).move_to(ax.c2p(TAX_Q / 3, (2 + 2 * SELLER_PRICE) / 3)),
            Tex('Tax revenue', color=INK).scale(0.72).move_to(ax.c2p(TAX_Q / 2, (BUYER_PRICE + SELLER_PRICE) / 2)),
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(TAX_Q / 3, (12 + 2 * BUYER_PRICE) / 3))))
        revenue_note = fixed(Tex(r'Tax revenue: \$2 $\times$ 32 tons $=$ \$64.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(people, government)
        self.play(FadeOut(taxed_first_words[2:]), FadeOut(split_note), run_time=0.4)
        self.play(FadeOut(taxed_first_words[0], suspend_mobject_updating=False),
                  FadeOut(taxed_first_words[1], suspend_mobject_updating=False),
                  Transform(taxed_first_pair, taxed_first_home),
                  FadeIn(market), FadeIn(sliding_wedge), FadeIn(sliding_word), FadeIn(wedge_marks), run_time=1.6)
        # Fills sit under the guides and dots: re-add the marks after every batch of bars.
        self.play(FadeOut(taxed_first_pair), FadeIn(ps_taxed[0]), FadeIn(tax_bars[0]), FadeIn(cs_taxed[0]), run_time=0.4)
        self.remove(sliding_wedge, sliding_word, wedge_marks)
        self.add(sliding_wedge, sliding_word, wedge_marks)
        self.play(LaggedStart(*[AnimationGroup(FadeIn(ps_taxed[q]), FadeIn(tax_bars[q]), FadeIn(cs_taxed[q]))
                                for q in range(1, TAX_Q)], lag_ratio=0.1), run_time=3)
        self.remove(*list(ps_taxed), *list(tax_bars), *list(cs_taxed), sliding_wedge, sliding_word, wedge_marks)
        self.add(ps_taxed, tax_bars, cs_taxed, sliding_wedge, sliding_word, wedge_marks)
        self.play(FadeIn(welfare_words), FadeIn(revenue_note))
        self.pause('6.b')

        # ---- 6.c.question · The tons the tax removes.
        lost_question = fixed(Tex('What about the tons no longer exchanged?', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        left, right = LOST_TON + BAR_GAP / 2, LOST_TON + 1 - BAR_GAP / 2
        lost_pair = fixed(VGroup(
            Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY)))
        lost_home = lost_pair.copy()
        lost_selection = fixed(SurroundingRectangle(lost_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(revenue_note)
        self.play(FadeIn(lost_question))
        self.pause('6.c.question')

        # ---- 6.c.select · Pick ton 36 from the existing bars.
        self.remove(lost_question)
        self.play(FadeIn(lost_pair), FadeIn(lost_selection))
        self.pause('6.c.select')

        # ---- 6.c.values · C1's 36th ton, with the tax's two prices around it.
        lost_target = fixed(VGroup())
        for bar_left, value, color in [(BUYER_LEFT, 4.8, DEMAND), (SELLER_LEFT, 3.8, SUPPLY)]:
            lost_target.add(fixed(Polygon([bar_left, detail_y(0), 0], [bar_left + BAR_WIDTH, detail_y(0), 0],
                [bar_left + BAR_WIDTH, detail_y(value), 0], [bar_left, detail_y(value), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.remove(context)
        context = fixed(subtitle(head, 'The 36th unit: exchanged before the tax, not after it.'))
        welfare_market = fixed(VGroup(market, ps_taxed, tax_bars, cs_taxed, welfare_words, sliding_wedge, sliding_word, wedge_marks))
        self.remove(market, sliding_wedge, sliding_word, wedge_marks, ps_taxed, tax_bars, cs_taxed, welfare_words)
        self.add(welfare_market)
        self.play(FadeOut(welfare_market), FadeOut(lost_selection), Transform(lost_pair, lost_target), run_time=1.6)
        lost_words = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(lost_target, [DEMAND, SUPPLY])],
            Line([-1.3, detail_y(0), 0], [1.3, detail_y(0), 0], color=MUTED),
            Tex(r'MB \$4.80', color=DEMAND).scale(0.72).next_to(lost_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC \$3.80', color=SUPPLY).scale(0.72).next_to(lost_target[1].get_corner(UR), RIGHT, buff=0.25)))
        lost_values_question = fixed(Tex('Does this exchange happen with the tax?', color=DEFINITION)
                                     .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(people, government)
        self.play(FadeIn(lost_words), FadeIn(context), FadeIn(lost_values_question))
        self.pause('6.c.values')

        # ---- 6.c.prices · Neither side can agree once the prices are $5.60 and $3.60.
        lost_prices = fixed(VGroup(
            Line([-1.3, detail_y(BUYER_PRICE), 0], [1.3, detail_y(BUYER_PRICE), 0], color=GUIDE, stroke_width=2),
            Line([-1.3, detail_y(SELLER_PRICE), 0], [1.3, detail_y(SELLER_PRICE), 0], color=GUIDE, stroke_width=2),
            Tex(r'$P_b$ \$5.60', color=GUIDE).scale(0.72).next_to([PRICE_LABEL_X, detail_y(BUYER_PRICE), 0], LEFT, buff=0.1),
            Tex(r'$P_s$ \$3.60', color=GUIDE).scale(0.72).next_to([PRICE_LABEL_X, detail_y(SELLER_PRICE), 0], LEFT, buff=0.1)))
        lost_prices_note = fixed(Tex('Buyers would pay more than MB, and sellers would get less than MC.', color=DEFINITION)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(lost_values_question)
        self.play(FadeIn(lost_prices), FadeIn(lost_prices_note))
        self.pause('6.c.prices')

        # ---- 6.c · The forgone surplus is deadweight loss.
        lost_dwl_bar = fixed(Polygon([BUYER_LEFT, detail_y(3.8), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(3.8), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [BUYER_LEFT, detail_y(4.8), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        lost_gap = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [3.8, detail_y(4.8), 0], color=DWL, stroke_width=1.6),
            DashedLine([3.25, detail_y(3.8), 0], [3.8, detail_y(3.8), 0], color=DWL, stroke_width=1.6),
            Line([3.8, detail_y(3.8), 0], [3.8, detail_y(4.8), 0], color=DWL, stroke_width=3),
            VGroup(Tex(r'TS $=+\$1$', color=TOTAL), Tex(r'DWL $=\$1$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=LEFT).scale(0.8)
                .next_to([3.8, detail_y(4.3), 0], RIGHT, buff=0.3),
            Tex(r'MB $>$ MC', color=INK).scale(0.8).move_to([4.3, -0.1, 0])))
        lost_note = fixed(Tex(r'The tax removes this ton, creating \$1 of deadweight loss.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(lost_prices_note)
        self.play(FadeIn(lost_dwl_bar), FadeIn(lost_gap), FadeIn(lost_note))
        self.pause('6.c')

        # ---- 6.d · Carry the loss back, then show all eight removed tons.
        lost_dwl_market = fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
            ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        self.remove(people, government, context)
        context = fixed(subtitle(head, r'32 tons exchanged: buyers pay \$5.60 and sellers receive \$3.60.'))
        self.play(FadeOut(lost_words), FadeOut(lost_prices), FadeOut(lost_gap), FadeOut(lost_note), run_time=0.4)
        self.play(Transform(lost_pair, lost_home), Transform(lost_dwl_bar, lost_dwl_market),
                  FadeIn(welfare_market), FadeIn(context), run_time=1.6)
        self.play(FadeOut(lost_pair))
        dwl_bars = fixed(VGroup())
        for q in range(TAX_Q, MARKET_Q):
            if q == LOST_TON:
                dwl_bars.add(lost_dwl_bar)
                continue
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            dwl_bars.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1)))
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(40, 4.6), RIGHT, buff=0.25))
        removed_note = fixed(Tex('The tax removes exchanges where MB exceeded MC: deadweight loss.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(LaggedStart(*[FadeIn(bar) for bar in dwl_bars if bar is not lost_dwl_bar], lag_ratio=0.18), run_time=1.6)
        self.remove(*[bar for bar in dwl_bars])
        self.add(dwl_bars)
        self.play(FadeIn(dwl_word), FadeIn(removed_note))
        self.pause('6.d')

        # ---- 7.a · Changing the tax: one tracker drives the wedge, the regions, and every readout.
        self.remove(head, context, removed_note)
        head = fixed(title('Changing The Tax'))
        self.remove(welfare_market)
        self.add(market, sliding_wedge, sliding_word, wedge_marks, ps_taxed, tax_bars, cs_taxed, welfare_words)
        tax, d_slope, s_slope = ValueTracker(TAX), ValueTracker(0.2), ValueTracker(0.05)
        cost_region = fixed(Polygon(ax.c2p(0, 0), ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(0, 2),
            stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY))
        ps_region = fixed(Polygon(ax.c2p(0, 2), ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(0, SELLER_PRICE),
            stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY))
        tax_region = fixed(Polygon(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), ax.c2p(0, BUYER_PRICE),
            stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY))
        cs_region = fixed(Polygon(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), ax.c2p(0, 12),
            stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY))
        dwl_region = fixed(Polygon(ax.c2p(TAX_Q, BUYER_PRICE), ax.c2p(MARKET_Q, MARKET_P), ax.c2p(TAX_Q, SELLER_PRICE),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        wedge = fixed(VGroup(
            Line(ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GOV, stroke_width=6),
            Line(ax.c2p(TAX_Q, SELLER_PRICE) + LEFT * 0.09, ax.c2p(TAX_Q, SELLER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(ax.c2p(TAX_Q, BUYER_PRICE) + LEFT * 0.09, ax.c2p(TAX_Q, BUYER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2)))
        wedge.set_z_index(2)
        wedge_word = fixed(VGroup(Tex(r'\$', color=GOV).scale(0.6), DecimalNumber(TAX, num_decimal_places=0, color=GOV).scale(0.6),
            Tex('tax', color=GOV).scale(0.6)).arrange(RIGHT, buff=0.06).next_to(ax.c2p(TAX_Q, BUYER_PRICE), UR, buff=0.12))
        buyer_price_readout = fixed(VGroup(Tex('$P_b=$', color=GUIDE).scale(0.7),
            DecimalNumber(BUYER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        seller_price_readout = fixed(VGroup(Tex('$P_s=$', color=GUIDE).scale(0.7),
            DecimalNumber(SELLER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        quantity_readout = fixed(VGroup(Tex('$Q=$', color=GUIDE).scale(0.7),
            DecimalNumber(TAX_Q, num_decimal_places=0, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        cs_label = fixed(VGroup(Tex(r'CS \$', color=INK).scale(0.62),
            DecimalNumber(102.4, num_decimal_places=2, color=INK).scale(0.62)).arrange(RIGHT, buff=0.05))
        ps_label = fixed(VGroup(Tex(r'PS \$', color=INK).scale(0.62),
            DecimalNumber(25.6, num_decimal_places=2, color=INK).scale(0.62)).arrange(RIGHT, buff=0.05))
        tax_label = fixed(VGroup(Tex(r'Tax \$', color=INK).scale(0.62),
            DecimalNumber(64, num_decimal_places=2, color=INK).scale(0.62)).arrange(RIGHT, buff=0.05))
        dwl_label = fixed(VGroup(Tex(r'DWL \$', color=INK).scale(0.62),
            DecimalNumber(8, num_decimal_places=2, color=INK).scale(0.62)).arrange(RIGHT, buff=0.05))
        driven = [cost_region, ps_region, tax_region, cs_region, dwl_region, *wedge, wedge_word,
                  buyer_price_readout, seller_price_readout, quantity_readout, cs_label, ps_label, tax_label, dwl_label]
        for m in driven:
            m.axes, m.tax, m.d, m.s = ax, tax, d_slope, s_slope
        cost_region.add_updater(lambda m: m.set_points_as_corners([m.axes.c2p(0, 0), m.axes.c2p(state(m)[0], 0),
            m.axes.c2p(state(m)[0], state(m)[2]), m.axes.c2p(0, 2), m.axes.c2p(0, 0)]))
        ps_region.add_updater(lambda m: m.set_points_as_corners([m.axes.c2p(0, 2), m.axes.c2p(state(m)[0], state(m)[2]),
            m.axes.c2p(0, state(m)[2]), m.axes.c2p(0, 2)]))
        tax_region.add_updater(lambda m: m.set_points_as_corners([m.axes.c2p(0, state(m)[2]), m.axes.c2p(state(m)[0], state(m)[2]),
            m.axes.c2p(state(m)[0], state(m)[1]), m.axes.c2p(0, state(m)[1]), m.axes.c2p(0, state(m)[2])]))
        cs_region.add_updater(lambda m: m.set_points_as_corners([m.axes.c2p(0, state(m)[1]), m.axes.c2p(state(m)[0], state(m)[1]),
            m.axes.c2p(0, 12), m.axes.c2p(0, state(m)[1])]))
        dwl_region.add_updater(lambda m: m.set_points_as_corners([m.axes.c2p(state(m)[0], state(m)[1]), m.axes.c2p(40, 4),
            m.axes.c2p(state(m)[0], state(m)[2]), m.axes.c2p(state(m)[0], state(m)[1])]))
        wedge[0].add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(state(m)[0], state(m)[2]), m.axes.c2p(state(m)[0], state(m)[1]) + UP * 1e-6))
        wedge[1].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[2])))
        wedge[2].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[1])))
        wedge[3].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[1])))
        wedge[4].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[2])))
        wedge[5].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[1]),
            m.axes.c2p(state(m)[0], state(m)[1]) + RIGHT * 1e-6, color=GUIDE, stroke_width=2))))
        wedge[6].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[2]),
            m.axes.c2p(state(m)[0], state(m)[2]) + RIGHT * 1e-6, color=GUIDE, stroke_width=2))))
        wedge[7].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(state(m)[0], 0),
            m.axes.c2p(state(m)[0], state(m)[2]) + UP * 1e-6, color=GUIDE, stroke_width=2))))
        wedge_word.add_updater(lambda m: (m[1].set_value(abs(m.tax.get_value())), fixed(m), m.arrange(RIGHT, buff=0.06),
            m[2].shift(RIGHT * 0.08), m.next_to(m.axes.c2p(state(m)[0], state(m)[1]), UR, buff=0.12)))
        # The readouts part vertically only when the wedge is nearly closed, so they never overprint.
        buyer_price_readout.add_updater(lambda m: (m[1].set_value(state(m)[1]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[1]), LEFT, buff=0.2)
            .shift(UP * 0.14 * max(0, 1 - (state(m)[1] - state(m)[2]) / 0.8))))
        seller_price_readout.add_updater(lambda m: (m[1].set_value(state(m)[2]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[2]), LEFT, buff=0.2)
            .shift(DOWN * 0.14 * max(0, 1 - (state(m)[1] - state(m)[2]) / 0.8))))
        quantity_readout.add_updater(lambda m: (m[1].set_value(state(m)[0]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(state(m)[0], 0), DOWN, buff=0.2)))
        cs_label.add_updater(lambda m: (m[1].set_value(state(m)[0] * (12 - state(m)[1]) / 2), fixed(m),
            m.arrange(RIGHT, buff=0.05), m.move_to(m.axes.c2p(state(m)[0] / 3, (12 + 2 * state(m)[1]) / 3))))
        ps_label.add_updater(lambda m: (m[1].set_value(state(m)[0] * (state(m)[2] - 2) / 2), fixed(m),
            m.arrange(RIGHT, buff=0.05), m.move_to(m.axes.c2p(state(m)[0] / 3, (2 + 2 * state(m)[2]) / 3))))
        tax_label.add_updater(lambda m: (m[1].set_value(m.tax.get_value() * state(m)[0]), fixed(m),
            m.arrange(RIGHT, buff=0.05), m.move_to(m.axes.c2p(state(m)[0] / 2, (state(m)[1] + state(m)[2]) / 2))))
        dwl_label.add_updater(lambda m: (m[1].set_value(m.tax.get_value() * (40 - state(m)[0]) / 2), fixed(m),
            m.arrange(RIGHT, buff=0.05), m.next_to(m.axes.c2p(40.5, (state(m)[1] + state(m)[2]) / 2), RIGHT, buff=0.2)))
        change_question = fixed(Tex('What happens as the tax changes?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # Crossfade the one-ton bars into the same shapes as continuous regions.
        self.play(FadeIn(head), FadeIn(change_question),
                  FadeOut(ps_taxed), FadeOut(tax_bars), FadeOut(cs_taxed), FadeOut(dwl_bars), FadeOut(welfare_words), FadeOut(dwl_word),
                  FadeOut(sliding_wedge), FadeOut(sliding_word), FadeOut(wedge_marks), costs.animate.set_fill(opacity=0),
                  FadeIn(cost_region), FadeIn(ps_region), FadeIn(tax_region), FadeIn(cs_region), FadeIn(dwl_region),
                  FadeIn(wedge), FadeIn(wedge_word), FadeIn(buyer_price_readout), FadeIn(seller_price_readout),
                  FadeIn(quantity_readout), FadeIn(cs_label), FadeIn(ps_label), FadeIn(tax_label), FadeIn(dwl_label), run_time=1.2)
        self.play(tax.animate.set_value(0), run_time=2.2, rate_func=smooth)
        zero_note = fixed(Tex('With no tax, buyers and sellers face the same price: the untaxed equilibrium.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(change_question)
        self.play(FadeIn(zero_note))
        self.pause('7.a.zero')
        self.remove(zero_note)
        self.play(FadeIn(change_question))
        self.play(tax.animate.set_value(5), run_time=3.2, rate_func=smooth)
        self.pause('7.a.five')
        growth_note = fixed(Tex('A larger tax raises more revenue, up to a point, but DWL grows faster.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(change_question)
        self.play(FadeIn(growth_note))
        self.play(tax.animate.set_value(TAX), run_time=2.2, rate_func=smooth)
        self.pause('7.a')

        # ---- 8.a · Tax incidence: how the $2 splits around the untaxed price.
        self.remove(head, growth_note)
        head = fixed(title('Tax Incidence'))
        context = fixed(subtitle(head, r'How the \$2 tax is split between buyers and sellers.'))
        reference = fixed(VGroup(
            DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=MUTED, stroke_width=2),
            Dot(ax.c2p(40, 4), radius=0.06, color=MUTED)))
        STACK_Q = -10.5
        buyer_share = fixed(Line(ax.c2p(STACK_Q, 4), ax.c2p(STACK_Q, BUYER_PRICE), color=DEMAND, stroke_width=7))
        seller_share = fixed(Line(ax.c2p(STACK_Q, SELLER_PRICE), ax.c2p(STACK_Q, 4), color=SUPPLY, stroke_width=7))
        buyer_share_number = fixed(DecimalNumber(1.6, num_decimal_places=2, color=DEMAND).scale(0.62))
        seller_share_number = fixed(DecimalNumber(0.4, num_decimal_places=2, color=SUPPLY).scale(0.62))
        for m in [buyer_share, seller_share, buyer_share_number, seller_share_number]:
            m.axes, m.tax, m.d, m.s = ax, tax, d_slope, s_slope
        buyer_share.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(STACK_Q, 4), m.axes.c2p(STACK_Q, state(m)[1]) + UP * 1e-6))
        seller_share.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(STACK_Q, state(m)[2]), m.axes.c2p(STACK_Q, 4) + UP * 1e-6))
        buyer_share_number.add_updater(lambda m: fixed(m.set_value(state(m)[1] - 4))
            .next_to(m.axes.c2p(STACK_Q, (4 + state(m)[1]) / 2), LEFT, buff=0.15))
        seller_share_number.add_updater(lambda m: fixed(m.set_value(4 - state(m)[2]))
            .next_to(m.axes.c2p(STACK_Q, (4 + state(m)[2]) / 2), LEFT, buff=0.15))
        incidence_note = fixed(Tex(r'Buyers pay \$1.60 more than before; sellers receive \$0.40 less.', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        for m in [cost_region, ps_region, tax_region, cs_region, dwl_region, cs_label, ps_label, tax_label, dwl_label]:
            m.clear_updaters()
        self.play(FadeIn(head), FadeIn(context),
                  FadeOut(cost_region), FadeOut(ps_region), FadeOut(tax_region), FadeOut(cs_region), FadeOut(dwl_region),
                  FadeOut(cs_label), FadeOut(ps_label), FadeOut(tax_label), FadeOut(dwl_label), FadeIn(reference))
        self.play(FadeIn(buyer_share), FadeIn(buyer_share_number))
        self.play(FadeIn(seller_share), FadeIn(seller_share_number), FadeIn(incidence_note))
        self.pause('8.a')

        # ---- 8.b · Flatter demand: buyers respond more and bear less.
        for m in [demand, supply, *curve_words]:
            m.axes, m.tax, m.d, m.s = ax, tax, d_slope, s_slope
        demand.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(0, 4 + 40 * m.d.get_value()),
            m.axes.c2p(min(60, 40 + 4 / m.d.get_value()), max(0, 4 - 20 * m.d.get_value()))))
        supply.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(max(0, 40 - 4 / m.s.get_value()), max(0, 4 - 40 * m.s.get_value())),
            m.axes.c2p(60, 4 + 20 * m.s.get_value())))
        curve_words[0].add_updater(lambda m: m.next_to(m.axes.c2p(8, 4 + 32 * m.d.get_value()), UR, buff=0.12))
        curve_words[1].add_updater(lambda m: m.next_to(m.axes.c2p(60, 4 + 20 * m.s.get_value()), RIGHT, buff=0.15))
        demand_question = fixed(Tex('What if buyers are more responsive to price?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(incidence_note)
        self.play(FadeIn(demand_question), intercepts.animate.set_opacity(0))
        self.play(d_slope.animate.set_value(0.05), run_time=2.4, rate_func=smooth)
        demand_note = fixed(Tex('More elastic demand: buyers bear less of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(demand_question)
        self.play(FadeIn(demand_note))
        self.pause('8.b')

        # ---- 8.c · Steeper supply: sellers respond less and bear more.
        supply_question = fixed(Tex('What if sellers are less responsive to price?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(demand_note)
        self.play(d_slope.animate.set_value(0.2), run_time=1.6, rate_func=smooth)
        self.play(FadeIn(supply_question))
        self.play(s_slope.animate.set_value(0.2), run_time=2.4, rate_func=smooth)
        supply_note = fixed(Tex('Less elastic supply: sellers bear more of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(supply_question)
        self.play(FadeIn(supply_note))
        self.pause('8.c')

        # ---- 8.d · The general rule, back on the original curves.
        burden_note = fixed(Tex('The side less responsive to price bears more of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(supply_note)
        self.play(s_slope.animate.set_value(0.05), run_time=1.6, rate_func=smooth)
        self.play(FadeIn(burden_note), intercepts.animate.set_opacity(1))
        self.pause('8.d')
        for m in [demand, supply, *curve_words]:
            m.clear_updaters()

        # ---- 9.a · A per-unit subsidy: the wedge reverses and slides in from the right.
        self.remove(head, context, burden_note)
        head = fixed(title('A Per-Unit Subsidy'))
        context = fixed(subtitle(head, r'The government pays \$2 on each ton exchanged.'))
        subsidy_slide = ValueTracker(66)
        subsidy_wedge = fixed(VGroup(
            Line(ax.c2p(66, SUBSIDY_BUYER), ax.c2p(66, SUBSIDY_SELLER), color=GOV, stroke_width=6),
            Line(ax.c2p(66, SUBSIDY_BUYER) + LEFT * 0.09, ax.c2p(66, SUBSIDY_BUYER) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(ax.c2p(66, SUBSIDY_SELLER) + LEFT * 0.09, ax.c2p(66, SUBSIDY_SELLER) + RIGHT * 0.09, color=GOV, stroke_width=3)))
        subsidy_word = fixed(Tex(r'\$2 subsidy', color=GOV).scale(0.6).next_to(ax.c2p(66, 3.4), RIGHT, buff=0.12))
        for part in [*subsidy_wedge, subsidy_word]:
            part.axes, part.quantity = ax, subsidy_slide
        subsidy_wedge[0].add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(m.quantity.get_value(), SUBSIDY_BUYER), m.axes.c2p(m.quantity.get_value(), SUBSIDY_SELLER)))
        subsidy_wedge[1].add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), SUBSIDY_BUYER)))
        subsidy_wedge[2].add_updater(lambda m: m.move_to(m.axes.c2p(m.quantity.get_value(), SUBSIDY_SELLER)))
        subsidy_word.add_updater(lambda m: m.next_to(m.axes.c2p(m.quantity.get_value(), 3.4), RIGHT, buff=0.12))
        subsidy_note = fixed(Tex(r'Sellers now receive \$2 more than buyers pay. Slide it in from the right.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        for m in [*wedge, wedge_word, buyer_price_readout, seller_price_readout, quantity_readout,
                  buyer_share, seller_share, buyer_share_number, seller_share_number]:
            m.clear_updaters()
        self.play(FadeIn(head), FadeIn(context), FadeIn(subsidy_note),
                  FadeOut(wedge), FadeOut(wedge_word), FadeOut(buyer_price_readout), FadeOut(seller_price_readout),
                  FadeOut(quantity_readout), FadeOut(reference), FadeOut(buyer_share), FadeOut(seller_share),
                  FadeOut(buyer_share_number), FadeOut(seller_share_number), costs.animate.set_fill(opacity=BASE_OPACITY))
        self.play(FadeIn(subsidy_wedge), FadeIn(subsidy_word))
        self.play(subsidy_slide.animate.set_value(SUBSIDY_Q), run_time=2.6, rate_func=smooth)
        self.pause('9.a')

        # ---- 9.b · Stuck at 48 tons: sellers' price above buyers' price, eight new one-ton bars.
        subsidy_wedge.clear_updaters()
        subsidy_word.clear_updaters()
        subsidy_marks = fixed(VGroup(
            Dot(ax.c2p(SUBSIDY_Q, SUBSIDY_SELLER), radius=0.07, color=GUIDE),
            Dot(ax.c2p(SUBSIDY_Q, SUBSIDY_BUYER), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, SUBSIDY_SELLER), ax.c2p(SUBSIDY_Q, SUBSIDY_SELLER), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(0, SUBSIDY_BUYER), ax.c2p(SUBSIDY_Q, SUBSIDY_BUYER), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(SUBSIDY_Q, 0), ax.c2p(SUBSIDY_Q, SUBSIDY_BUYER), color=GUIDE, stroke_width=2),
            Tex(r'$P_s=4.40$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SUBSIDY_SELLER), LEFT, buff=0.2),
            Tex(r'$P_b=2.40$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SUBSIDY_BUYER), LEFT, buff=0.2),
            Tex(r'$Q=48$', color=GUIDE).scale(0.7).next_to(ax.c2p(SUBSIDY_Q, 0), DOWN, buff=0.20)))
        subsidy_marks.set_z_index(2)
        subsidy_wedge.set_z_index(2)
        added_lots = fixed(VGroup())
        for q in range(MARKET_Q, SUBSIDY_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            added_lots.add(fixed(VGroup(
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY))))
        subsidy_definition = fixed(Tex("Subsidy wedge: the sellers' price minus the buyers' price equals the subsidy.", color=DEFINITION)
                                   .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(subsidy_note)
        self.play(FadeIn(subsidy_marks), FadeIn(subsidy_definition), intercepts[0].animate.set_opacity(0),
                  LaggedStart(*[FadeIn(lot) for lot in added_lots], lag_ratio=0.3), run_time=1.6)
        self.pause('9.b')

        # ---- 9.b.wedge · The same side solve for the subsidy, for skill C2.2.
        subsidy_block = fixed(VGroup(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots))
        self.remove(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_definition)
        self.add(subsidy_block)
        subsidy_solve_note = fixed(Tex('Use the subsidy wedge and the two curves to solve for the quantity.', color=DEFINITION)
                                   .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(subsidy_block.animate.scale(0.72, about_point=ax.c2p(0, 0)).shift(LEFT * 1.0), run_time=1.1)
        subsidy_divider = fixed(Line([2.45, -3.0, 0], [2.45, 2.3, 0], color=MUTED, stroke_width=1.5))
        subsidy_wedge_line = fixed(VGroup(Tex('$P_s$', color=GUIDE), Tex('$-$', color=INK), Tex('$P_b$', color=GUIDE),
            Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_substitute_line = fixed(VGroup(Tex('$(2 + Q/20)$', color=SUPPLY), Tex('$-$', color=INK),
            Tex('$(12 - Q/5)$', color=DEMAND), Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_simplify_line = fixed(VGroup(Tex('$Q/4 - 10$', color=INK), Tex('$=$', color=INK), Tex('$2$', color=GOV))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_solve_line = fixed(VGroup(Tex('$Q$', color=GUIDE), Tex('$=$', color=INK), Tex('$48$', color=GUIDE))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_seller_line = fixed(VGroup(Tex('$P_s$', color=GUIDE), Tex('$=$', color=INK), Tex('$2 + 48/20$', color=SUPPLY),
            Tex('$=$', color=INK), Tex('$4.40$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_buyer_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$=$', color=INK), Tex('$12 - 48/5$', color=DEMAND),
            Tex('$=$', color=INK), Tex('$2.40$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_algebra = fixed(VGroup(subsidy_wedge_line, subsidy_substitute_line, subsidy_simplify_line, subsidy_solve_line,
            subsidy_seller_line, subsidy_buyer_line).arrange(DOWN, buff=0.34).move_to([5.2, 0.15, 0]))
        self.play(FadeIn(subsidy_divider), FadeIn(subsidy_wedge_line), FadeIn(subsidy_solve_note))
        self.pause('9.b.wedge')
        self.play(FadeIn(subsidy_substitute_line))
        self.pause('9.b.substitute')
        self.play(FadeIn(subsidy_simplify_line))
        self.pause('9.b.simplify')
        self.play(FadeIn(subsidy_solve_line))
        self.pause('9.b.solve')
        subsidy_price_note = fixed(Tex('Then read each price from its own curve.', color=DEFINITION)
                                   .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(subsidy_solve_note)
        self.play(FadeIn(subsidy_seller_line), FadeIn(subsidy_price_note))
        self.play(FadeIn(subsidy_buyer_line))
        self.pause('9.b.prices')
        self.play(FadeOut(subsidy_algebra), FadeOut(subsidy_divider), FadeOut(subsidy_price_note), run_time=0.5)
        self.play(subsidy_block.animate.shift(RIGHT * 1.0).scale(1 / 0.72, about_point=ax.c2p(0, 0) + RIGHT * 1.0), run_time=1.1)
        self.remove(subsidy_block)
        self.add(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots)

        # ---- 9.c · The government pays the gap on every one of the 48 tons.
        subsidy_cost = fixed(VGroup(
            Polygon(ax.c2p(0, SUBSIDY_BUYER), ax.c2p(SUBSIDY_Q, SUBSIDY_BUYER), ax.c2p(SUBSIDY_Q, SUBSIDY_SELLER), ax.c2p(0, SUBSIDY_SELLER),
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex('Subsidy cost', color=INK).scale(0.72).move_to(ax.c2p(16, 3.8))))  # Above MC, which bisects the rectangle.
        cost_note = fixed(Tex(r'Government cost: \$2 $\times$ 48 tons $=$ \$96.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(subsidy_cost), FadeIn(cost_note))
        self.pause('9.c')

        # ---- 9.d.select · The 48th ton, exchanged only because of the subsidy.
        added_pair = fixed(VGroup(*list(added_lots[-1])))
        added_lots[-1].remove(*list(added_pair))
        added_home = added_pair.copy()
        self.add(added_pair)
        added_selection = fixed(SurroundingRectangle(added_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(cost_note)
        self.play(FadeIn(added_selection))
        self.pause('9.d.select')

        # ---- 9.d.values · C1's 48th ton: MB below MC.
        added_target = fixed(VGroup())
        for bar_left, value, color in [(BUYER_LEFT, 2.4, DEMAND), (SELLER_LEFT, 4.4, SUPPLY)]:
            added_target.add(fixed(Polygon([bar_left, detail_y(0), 0], [bar_left + BAR_WIDTH, detail_y(0), 0],
                [bar_left + BAR_WIDTH, detail_y(value), 0], [bar_left, detail_y(value), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        subsidy_market = fixed(VGroup(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_cost))
        self.remove(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_cost, context)
        self.add(subsidy_market)
        context = fixed(subtitle(head, 'The 48th unit: exchanged only with the subsidy.'))
        self.play(FadeOut(subsidy_market), FadeOut(added_selection), Transform(added_pair, added_target), run_time=1.6)
        added_words = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(added_target, [DEMAND, SUPPLY])],
            Line([-1.3, detail_y(0), 0], [1.3, detail_y(0), 0], color=MUTED),
            Tex(r'MB \$2.40', color=DEMAND).scale(0.72).next_to(added_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC \$4.40', color=SUPPLY).scale(0.72).next_to(added_target[1].get_corner(UR), RIGHT, buff=0.25)))
        added_question = fixed(Tex('Why does this exchange happen?', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(people, government)
        self.play(FadeIn(added_words), FadeIn(context), FadeIn(added_question))
        self.pause('9.d.values')

        # ---- 9.d.prices · The buyer pays MB, the government adds $2, the seller receives MC.
        added_prices = fixed(VGroup(
            Line([-1.3, detail_y(SUBSIDY_BUYER), 0], [1.3, detail_y(SUBSIDY_BUYER), 0], color=GUIDE, stroke_width=2),
            Line([-1.3, detail_y(SUBSIDY_SELLER), 0], [1.3, detail_y(SUBSIDY_SELLER), 0], color=GUIDE, stroke_width=2),
            Tex(r'$P_b$ \$2.40', color=GUIDE).scale(0.72).next_to([PRICE_LABEL_X, detail_y(SUBSIDY_BUYER), 0], LEFT, buff=0.1),
            Tex(r'$P_s$ \$4.40', color=GUIDE).scale(0.72).next_to([PRICE_LABEL_X, detail_y(SUBSIDY_SELLER), 0], LEFT, buff=0.1),
            Polygon([SELLER_LEFT, detail_y(SUBSIDY_BUYER), 0], [SELLER_LEFT + BAR_WIDTH, detail_y(SUBSIDY_BUYER), 0],
                [SELLER_LEFT + BAR_WIDTH, detail_y(SUBSIDY_SELLER), 0], [SELLER_LEFT, detail_y(SUBSIDY_SELLER), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex(r'Subsidy \$2', color=INK).scale(0.55)))
        added_prices[5].move_to(added_prices[4])
        added_prices_note = fixed(Tex(r'The buyer pays \$2.40, the government adds \$2, and the seller receives \$4.40.', color=DEFINITION)
                                  .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(added_question)
        self.play(FadeIn(added_prices[:4]))
        self.play(FadeIn(added_prices[4:]), FadeIn(added_prices_note))
        self.pause('9.d.prices')

        # ---- 9.d · The cost above the buyer's value is deadweight loss.
        added_dwl_bar = fixed(Polygon([BUYER_LEFT, detail_y(2.4), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(2.4), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(4.4), 0], [BUYER_LEFT, detail_y(4.4), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        added_gap = fixed(VGroup(
            DashedLine([1.3, detail_y(2.4), 0], [3.8, detail_y(2.4), 0], color=DWL, stroke_width=1.6),
            DashedLine([3.25, detail_y(4.4), 0], [3.8, detail_y(4.4), 0], color=DWL, stroke_width=1.6),
            Line([3.8, detail_y(2.4), 0], [3.8, detail_y(4.4), 0], color=DWL, stroke_width=3),
            VGroup(Tex(r'TS $=-\$2$', color=TOTAL), Tex(r'DWL $=\$2$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=LEFT).scale(0.8)
                .next_to([3.8, detail_y(3.4), 0], RIGHT, buff=0.3),
            Tex(r'MC $>$ MB', color=INK).scale(0.8)))
        added_gap[-1].next_to(added_gap[-2], DOWN, buff=0.2)
        added_note = fixed(Tex(r'This ton costs \$2 more than it is worth: deadweight loss.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(added_prices_note)
        self.play(FadeIn(added_dwl_bar), FadeIn(added_gap), FadeIn(added_note))
        self.pause('9.d')

        # ---- 9.e · Carry the loss back, then show all eight added tons.
        left, right = ADDED_TON + BAR_GAP / 2, ADDED_TON + 1 - BAR_GAP / 2
        added_dwl_market = fixed(Polygon(ax.c2p(left, 12 - left / 5), ax.c2p(right, 12 - right / 5),
            ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        self.remove(people, government, context)
        context = fixed(subtitle(head, r'The government pays \$2 on each ton exchanged.'))
        self.play(FadeOut(added_words), FadeOut(added_prices), FadeOut(added_gap), FadeOut(added_note), run_time=0.4)
        self.play(Transform(added_pair, added_home), Transform(added_dwl_bar, added_dwl_market),
                  FadeIn(subsidy_market), FadeIn(context), run_time=1.6)
        # The 48th lot rejoins its group so its faint cost bar stays with the other seven.
        self.remove(added_pair)
        added_lots[-1].add(*list(added_home))
        subsidy_losses = fixed(VGroup())
        for q in range(MARKET_Q, SUBSIDY_Q):
            if q == ADDED_TON:
                subsidy_losses.add(added_dwl_bar)
                continue
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            subsidy_losses.add(fixed(Polygon(ax.c2p(left, 12 - left / 5), ax.c2p(right, 12 - right / 5),
                ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1)))
        subsidy_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(44, 4.6), UP, buff=0.18))
        subsidy_loss_note = fixed(Tex('A subsidy adds exchanges where MC exceeds MB: deadweight loss.', color=DEFINITION)
                                  .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(LaggedStart(*[FadeIn(bar) for bar in subsidy_losses if bar is not added_dwl_bar], lag_ratio=0.18), run_time=1.6)
        self.remove(*[bar for bar in subsidy_losses])
        self.add(subsidy_losses)
        self.play(FadeIn(subsidy_dwl_word), FadeIn(subsidy_loss_note))
        self.pause('9.e')

        # ---- 10.a · Next time: the $2 tax lands on C1's efficient quantity.
        self.remove(head, context, subsidy_loss_note)
        head = fixed(title('Next Time'))
        context = fixed(subtitle(head, r'Last time, a \$2 external cost made 32 tons the efficient quantity.'))
        self.remove(subsidy_market)
        self.add(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_cost)
        closing_wedge = fixed(VGroup(
            Line(ax.c2p(TAX_Q, SELLER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GOV, stroke_width=6),
            Line(ax.c2p(TAX_Q, SELLER_PRICE) + LEFT * 0.09, ax.c2p(TAX_Q, SELLER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Line(ax.c2p(TAX_Q, BUYER_PRICE) + LEFT * 0.09, ax.c2p(TAX_Q, BUYER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
            Tex(r'\$2 tax', color=GOV).scale(0.6).next_to(ax.c2p(TAX_Q, BUYER_PRICE), UR, buff=0.12),
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2),
            Tex(r'$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2),
            Tex(r'$Q=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20)))
        closing_wedge.set_z_index(2)
        next_note = fixed(Tex('Next time: can a tax correct an externality?', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(context), FadeOut(subsidy_wedge), FadeOut(subsidy_word), FadeOut(subsidy_marks),
                  FadeOut(added_lots), FadeOut(subsidy_cost), FadeOut(subsidy_losses), FadeOut(subsidy_dwl_word),
                  intercepts[0].animate.set_opacity(1),
                  *[bar.animate.set_fill(opacity=0.05) for bar in list(costs)[TAX_Q:]])
        self.play(FadeIn(closing_wedge), FadeIn(next_note))
        self.pause('10.a')
