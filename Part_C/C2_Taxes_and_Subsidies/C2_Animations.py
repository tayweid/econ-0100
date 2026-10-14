# maniml C2_Animations.py C2
# Storyboard: C2_Notes.md. All lesson choreography stays in construct().
# C1's spinach market, MB = 12 - Q/5 and MC = 2 + Q/20, Q in units and values in dollars per unit.
# A $2 tax lands on C1's 32nd unit and a $2 subsidy on its 48th; the 36th unit is the exchange the tax removes, the 44th the one the subsidy adds.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../Part_B/Sim'))
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
        LOST_TON, ADDED_TON = 35, 43  # Unit 36 is the exchange the tax removes; unit 44 is one the subsidy adds.
        BAR_GAP = 0.08
        BASE_OPACITY, SURPLUS_OPACITY = 0.16, 0.65
        STRIP_OPACITY = 1.0  # The tax is introduced opaque; from section 6 on its revenue takes SURPLUS_OPACITY like CS and PS.
        TAX_INTRO_OPACITY = 1.0  # The close-up tax bar while the tax is introduced (2.b-4.a); from 6.a on it takes SURPLUS_OPACITY.
        # Close-ups: the first unit at 0.35 per dollar, C1's detail units at 0.68 per dollar.
        DETAIL_BASE, DETAIL_SCALE, FIRST_SCALE = -2.05, 0.68, 0.35
        # Spread layout: the buyer column, a narrower tax bar in the middle, the seller column.
        BUYER_LEFT, SELLER_LEFT, BAR_WIDTH = -1.76, 0.66, 1.1
        TAX_LEFT, TAX_WIDTH = -0.40, 0.80
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
        ax = style_axes([0, 60, 10], [0, 13, 2], x_length=4.6, y_length=4.6)
        ax.shift(np.array([-2.3, BODY_MID - 2.15, 0]) - ax.c2p(0, 0))
        fixed(ax)
        # The unit caption sits beside P, as in B5, so the subtitles above the market never touch it.
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), RIGHT, buff=0.22),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73)))
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
        for x, color, name, group in [(-1.6, DEMAND, 'Buyer', people), (1.6, SUPPLY, 'Seller', people),
                                      (0, GOV, 'Government', government)]:
            group.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([x, DETAIL_BASE - 0.60, 0])))
            group.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            group.add(fixed(Tex(name, color=INK).scale(0.65).move_to([x, DETAIL_BASE - 0.94, 0])))

        # ---- 2.a.select · A per-unit tax, asked of the first exchange.
        self.remove(head, context)
        head = fixed(title('A Per-Unit Tax'))
        context = fixed(subtitle(head, 'The first unit: introducing a per-unit tax.'))
        l0, r0 = BAR_GAP / 2, 1 - BAR_GAP / 2
        # Market slice and close-up share one structure: buyer base, CS, MB edge, cost, PS, MC edge, baseline.
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
            Line(ax.c2p(l0, 0), ax.c2p(r0, 0), color=MUTED)))
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
            Line([-1.9, first_y(0), 0], [1.9, first_y(0), 0], color=MUTED)))
        # Compact labels: numbers outside the bars at their boundary heights, names on the bars.
        first_values = fixed(VGroup(
            Tex(r'$\$12$', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, first_y(12), 0], LEFT, buff=0.25),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, first_y(12), 0], UP, buff=0.10),
            Tex(r'$\$2$', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, first_y(2), 0], RIGHT, buff=0.25),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, first_y(2), 0], DOWN, buff=0.10)).set_z_index(3))
        first_pair = first_home.copy()
        first_selection = fixed(SurroundingRectangle(first_home, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(head), FadeIn(context), FadeIn(first_pair), FadeIn(first_selection))
        self.pause('2.a.select')

        # ---- 2.a.values · The close-up: values first, then the price, then both surpluses.
        self.play(FadeOut(market), FadeOut(first_selection), Transform(first_pair, first_target), run_time=1.6)
        self.add(people)
        self.play(FadeIn(first_values))
        self.pause('2.a.values')
        # ---- 2.a · The government arrives: its $2 is on the table. No price, CS or PS here, so prices stay unambiguous.
        self.add(government)
        self.pause('2.a')

        # ---- 2.b · The tax as a $2 bar between the two: one narrow bar carries it through every close-up. It sits under
        # the columns (z -1) so the solid MB and MC edges stay whole when it is stacked on them in 2.c and 4.a; its
        # label rides above everything (z 3).
        tax_bar = fixed(Polygon([TAX_LEFT, first_y(0), 0], [TAX_LEFT + TAX_WIDTH, first_y(0), 0],
            [TAX_LEFT + TAX_WIDTH, first_y(2), 0], [TAX_LEFT, first_y(2), 0],
            stroke_width=0, fill_color=GOV, fill_opacity=TAX_INTRO_OPACITY)).set_z_index(-1)
        tax_word = fixed(VGroup(Tex('tax', color=INK), Tex(r'\$2', color=INK)).arrange(DOWN, buff=0.06).scale(0.55)
                         .move_to(tax_bar)).set_z_index(3)
        hand_question = fixed(Tex('Should the seller or the buyer hand it over?', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(tax_bar), FadeIn(tax_word), FadeIn(hand_question))
        self.pause('2.b')

        # ---- 2.c · The tax as the seller's cost: the same $2 stacks on MC, measured beside the seller column as C1 draws EXT.
        seller_stack = fixed(Polygon([SELLER_LEFT, first_y(2), 0], [SELLER_LEFT + BAR_WIDTH, first_y(2), 0],
            [SELLER_LEFT + BAR_WIDTH, first_y(4), 0], [SELLER_LEFT, first_y(4), 0],
            stroke_width=0, fill_color=GOV, fill_opacity=TAX_INTRO_OPACITY)).set_z_index(-1)
        stack_word = fixed(Tex('tax', color=INK).scale(0.58).move_to(seller_stack)).set_z_index(3)
        # The stack's top edge, dashed in the seller's orange, named just above it inside the column; the number at 4
        # steps out to buff 0.45 beside the measure.
        seller_edge = fixed(VGroup(
            DashedLine([SELLER_LEFT, first_y(4), 0], [SELLER_LEFT + BAR_WIDTH, first_y(4), 0], color=SUPPLY, stroke_width=3),
            Tex('MC $+$ tax', color=SUPPLY).scale(0.58).next_to([1.21, first_y(4), 0], UP, buff=0.10),
            Tex(r'$\$4$', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, first_y(4), 0], RIGHT, buff=0.25))).set_z_index(3)
        # C1's measure: a green dashed line beside the column with the amount beside it.
        measure = fixed(DashedLine([0.46, first_y(2), 0], [0.46, first_y(4), 0], color=GOV, stroke_width=2.5))
        measure_word = fixed(Tex(r'\$2 tax', color=GOV).scale(0.6).next_to([0.46, first_y(3), 0], LEFT, buff=0.15))
        seller_note = fixed(Tex(r'A \$2 higher cost to the seller.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(hand_question)
        self.play(Transform(tax_bar, seller_stack), FadeOut(tax_word), FadeIn(stack_word),
                  FadeIn(seller_edge), FadeIn(measure), FadeIn(measure_word), FadeIn(seller_note), run_time=1.2)
        self.pause('2.c')

        # ---- 2.d · The buyer alternative, previewed on the same exchange: the tax slides up, carved out of the buyer's value.
        buyer_stack = fixed(Polygon([BUYER_LEFT, first_y(10), 0], [BUYER_LEFT + BAR_WIDTH, first_y(10), 0],
            [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
            stroke_width=0, fill_color=GOV, fill_opacity=TAX_INTRO_OPACITY)).set_z_index(-1)
        # The carve-out's bottom edge, dashed in the buyer's teal, named just below it inside the column; the number at
        # 10 sits outside at buff 0.45 beside the measure, under the $12 that steps out to match.
        buyer_edge = fixed(VGroup(
            DashedLine([BUYER_LEFT, first_y(10), 0], [BUYER_LEFT + BAR_WIDTH, first_y(10), 0], color=DEMAND, stroke_width=3),
            Tex('MB $-$ tax', color=DEMAND).scale(0.58).next_to([-1.21, first_y(10), 0], DOWN, buff=0.10),
            Tex(r'$\$10$', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, first_y(10), 0], LEFT, buff=0.25))).set_z_index(3)
        buyer_note = fixed(Tex(r'A \$2 lower benefit to the buyer.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(seller_note)
        # One play: the stack and its word slide up and across, the measure crosses to the buyer's side, the seller's
        # edge goes and the buyer's comes, and the seller's number steps back in now that nothing sits beside it.
        self.play(Transform(tax_bar, buyer_stack), stack_word.animate.move_to(buyer_stack),
                  measure.animate.move_to([-0.46, first_y(11), 0]),
                  measure_word.animate.next_to([-0.46, first_y(11), 0], RIGHT, buff=0.15),
                  FadeOut(seller_edge), FadeIn(buyer_edge), FadeIn(buyer_note), run_time=1.2)
        self.pause('2.d')

        # ---- 2.d.return · Sellers first: the bar slides back onto the seller's column, then the pair carries back to its slice.
        self.play(Transform(tax_bar, seller_stack), stack_word.animate.move_to(seller_stack),
                  measure.animate.move_to([0.46, first_y(3), 0]),
                  measure_word.animate.next_to([0.46, first_y(3), 0], LEFT, buff=0.15),
                  FadeIn(seller_edge), FadeOut(buyer_edge), FadeOut(buyer_note), run_time=0.8)
        # The stack travels to the strip it will become and fades on the way. The market comes back already taxed, in
        # the same play: no frame of the untaxed market between the close-up and the seller's view.
        first_strip_home = fixed(Polygon(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20),
            ax.c2p(r0, 4 + r0 / 20), ax.c2p(l0, 4 + l0 / 20),
            stroke_width=0, fill_color=GOV, fill_opacity=0)).set_z_index(-1)
        first_home[1].set_fill(opacity=0)
        first_home[4].set_fill(opacity=0)
        self.remove(people, government)
        self.play(FadeOut(first_values), FadeOut(stack_word), FadeOut(seller_edge), FadeOut(measure), FadeOut(measure_word),
                  run_time=0.4)

        # ---- 3.a · A tax on sellers: the market returns with a $2 strip on every cost bar and supply shifted up.
        self.remove(head, context)
        head = fixed(title('A Tax On Sellers'))
        context = fixed(subtitle(head, r'Sellers hand \$2 per unit to the government.'))
        seller_note = fixed(Tex(r'A \$2 higher cost on every unit.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # Strips only on the 40 exchanged units, under the curves (z -1) so the solid S / MC stays whole over them;
        # beyond the market the dashed curve alone carries the taxed supply.
        seller_strips = fixed(VGroup()).set_z_index(-1)
        for q in range(MARKET_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            seller_strips.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 4 + right / 20), ax.c2p(left, 4 + left / 20),
                stroke_width=0, fill_color=GOV, fill_opacity=STRIP_OPACITY)).set_z_index(-1))
        taxed_supply = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(60, 7), color=SUPPLY, stroke_width=3))
        taxed_supply_word = fixed(Tex('MC $+$ tax', color=INK).scale(0.7).next_to(ax.c2p(60, 7), RIGHT, buff=0.15))
        # The surplus fills rest while the curves move; welfare returns in section 6. The market was off screen, so
        # its marker and surplus words simply leave the group before it comes back.
        market.remove(equilibrium, surplus_words)
        # Keep the untaxed price and quantity as unlabeled references in every later market view.
        # Traveling with market preserves them through panel copies, resizes and close-up returns.
        original_guides = fixed(VGroup(
            DashedLine(ax.c2p(0, MARKET_P), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
            DashedLine(ax.c2p(MARKET_Q, 0), ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2)
        )).set_z_index(1.5)
        market.add(original_guides)
        cs.set_fill(opacity=0)
        ps.set_fill(opacity=0)
        self.play(FadeIn(head), FadeIn(context), Transform(first_pair, first_home), Transform(tax_bar, first_strip_home),
                  FadeIn(market), FadeIn(seller_strips), FadeIn(taxed_supply), FadeIn(taxed_supply_word), run_time=1.6)
        self.remove(first_pair, tax_bar)
        self.play(FadeIn(seller_note))
        self.pause('3.a')

        # ---- 3.b · Where the taxed supply meets demand: only the quantity; the prices wait for the close-up.
        seller_question = fixed(Tex('With these new higher costs, the tax equilibrium quantity decreases.', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        taxed_point = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$Q^{tax}=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20))).set_z_index(2)
        self.remove(seller_note)
        self.play(FadeIn(seller_question))
        # Units 33-40 leave the picture entirely: no bars beyond the taxed quantity.
        self.play(FadeIn(taxed_point),
                  *[bar.animate.set_fill(opacity=0) for bar in list(costs)[TAX_Q:] + list(seller_strips)[TAX_Q:]])
        self.pause('3.b')

        # ---- 3.c · The new price, then the seller's price after the tax: a second dot on MC at the same unit.
        # Price readouts sit close to the axis, aligned with the tax measurement label introduced in 5.a.
        collect_note = fixed(Tex(r'Sellers collect \$5.60, hand over \$2, keep \$3.60.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        taxed_prices = fixed(VGroup(
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2))).set_z_index(2)
        price_readout = fixed(Tex(r'$P=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2))
        after_tax_readout = fixed(Tex(r'$P-\mathrm{tax}=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2))
        self.remove(seller_question)
        self.play(FadeIn(taxed_prices[0]), FadeIn(price_readout), FadeIn(collect_note))
        self.play(FadeIn(taxed_prices[1]), FadeIn(taxed_prices[2]), FadeIn(after_tax_readout))
        # Regroup the guides so the close-up carries them out and back as one.
        self.remove(*taxed_prices)
        self.add(taxed_prices)
        self.pause('3.c')

        # ---- 4.a.select · A tax on buyers: back to the first exchange, its strip on its cost bar.
        self.remove(head, context, collect_note)
        head = fixed(title('A Tax On Buyers'))
        context = fixed(subtitle(head, 'The first unit: the same tax paid by the buyer.'))
        # The slice as the market shows it now: no surplus fills, the cost bar, and the strip the tax bar becomes again.
        second_pair = first_home.copy()
        second_pair[1].set_fill(opacity=0)
        second_pair[4].set_fill(opacity=0)
        second_home = second_pair.copy()
        tax_bar.set_fill(opacity=TAX_INTRO_OPACITY)
        self.play(FadeIn(head), FadeIn(context), FadeIn(second_pair), FadeIn(tax_bar), FadeIn(first_selection))
        self.pause('4.a.select')

        # ---- 4.a.values · The close-up exactly as 2.c left it: the stacked tax on the seller, measured.
        self.play(FadeOut(market), FadeOut(seller_strips), FadeOut(taxed_supply), FadeOut(taxed_supply_word), FadeOut(taxed_point),
                  FadeOut(taxed_prices), FadeOut(price_readout), FadeOut(after_tax_readout),
                  FadeOut(first_selection), Transform(second_pair, first_target), Transform(tax_bar, seller_stack), run_time=1.6)
        self.add(people, government)
        self.play(FadeIn(first_values), FadeIn(stack_word), FadeIn(seller_edge), FadeIn(measure), FadeIn(measure_word))
        self.pause('4.a.values')

        # ---- 4.a · The same tax slides up, as 2.d previewed it: carved out of the buyer's value, measured beside the buyer column.
        self.play(Transform(tax_bar, buyer_stack), stack_word.animate.move_to(buyer_stack),
                  measure.animate.move_to([-0.46, first_y(11), 0]),
                  measure_word.animate.next_to([-0.46, first_y(11), 0], RIGHT, buff=0.15),
                  FadeOut(seller_edge), FadeIn(buyer_edge), FadeIn(buyer_note), run_time=1.2)
        self.pause('4.a')

        # ---- 4.a.return · One animation: the pair carries back as the market returns, and every seller strip moves up
        # from the cost bars to hang under demand, the way the tax just moved in the close-up.
        buyer_strip_home = fixed(Polygon(ax.c2p(l0, 10 - l0 / 5), ax.c2p(r0, 10 - r0 / 5),
            ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
            stroke_width=0, fill_color=GOV, fill_opacity=0)).set_z_index(-1)
        market_buyer_note = fixed(Tex(r'A \$2 lower benefit on every unit.', color=DEFINITION)
                                  .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # Each buyer strip takes its seller strip's opacity: opaque to 32, hidden for 33-40, so the flight shows
        # nothing beyond the taxed quantity; past the market the dashed curve alone carries the taxed demand.
        buyer_strips = fixed(VGroup()).set_z_index(-1)
        for q in range(MARKET_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            buyer_strips.add(fixed(Polygon(ax.c2p(left, 10 - left / 5), ax.c2p(right, 10 - right / 5),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=GOV, fill_opacity=seller_strips[q].get_fill_opacity())).set_z_index(-1))
        taxed_demand = fixed(DashedLine(ax.c2p(0, 10), ax.c2p(50, 0), color=DEMAND, stroke_width=3))
        # The name tucks under the dashed curve's upper stretch: at its foot the solid D / MB would run through it.
        taxed_demand_word = fixed(Tex('MB $-$ tax', color=INK).scale(0.7).next_to(ax.c2p(12, 10 - 12 / 5), DL, buff=0.15))
        taxed_demand_word.set_opacity(0)  # Appears at the end of the flight.
        self.remove(people, government)
        self.play(FadeOut(first_values), FadeOut(stack_word), FadeOut(buyer_edge), FadeOut(measure), FadeOut(measure_word),
                  FadeOut(buyer_note), run_time=0.4)
        self.remove(context)
        context = fixed(subtitle(head, r'Buyers hand \$2 per unit to the government.'))
        self.add(context)
        # From this market return onward, MC is carried by its curve alone. Close-up cost columns stay faint.
        costs.set_fill(opacity=0)
        second_home[3].set_fill(opacity=0)
        # The seller strips come back where they were and fly in the same play as the zoom-out.
        self.add(*seller_strips)
        self.play(Transform(second_pair, second_home), Transform(tax_bar, buyer_strip_home), FadeIn(market),
                  *[ReplacementTransform(seller_strips[q], buyer_strips[q]) for q in range(MARKET_Q)],
                  FadeIn(taxed_demand),
                  Succession(Animation(taxed_demand_word), Animation(taxed_demand_word), Animation(taxed_demand_word),
                             Animation(taxed_demand_word), taxed_demand_word.animate.set_opacity(1)),
                  FadeIn(market_buyer_note), run_time=2.6, rate_func=smooth)
        self.remove(second_pair, tax_bar)
        self.remove(*buyer_strips)
        self.add(buyer_strips)
        self.pause('4.b')

        # ---- 4.c · With these lower benefits, the taxed demand meets supply: the quantity is found again.
        quantity_note = fixed(Tex('With these new lower benefits, the tax equilibrium quantity decreases.', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        buyer_point = fixed(VGroup(
            Dot(ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(TAX_Q, 0), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Tex(r'$Q^{tax}=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20))).set_z_index(2)
        self.remove(market_buyer_note)
        self.play(FadeIn(quantity_note))
        self.play(FadeIn(buyer_point))
        self.pause('4.c')

        # ---- 4.d · The new price, then the buyer's price after the tax: a second dot on MB at the same unit.
        pay_note = fixed(Tex(r'Buyers pay \$3.60 plus \$2: \$5.60. Sellers keep \$3.60.', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        buyer_prices = fixed(VGroup(
            DashedLine(ax.c2p(0, SELLER_PRICE), ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
            Dot(ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
            DashedLine(ax.c2p(0, BUYER_PRICE), ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2))).set_z_index(2)
        new_price_readout = fixed(Tex(r'$P=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2))
        plus_tax_readout = fixed(Tex(r'$P+\mathrm{tax}=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2))
        self.remove(quantity_note)
        self.play(FadeIn(buyer_prices[0]), FadeIn(new_price_readout), FadeIn(pay_note))
        self.play(FadeIn(buyer_prices[1]), FadeIn(buyer_prices[2]), FadeIn(plus_tax_readout))
        self.remove(*buyer_prices)
        self.add(buyer_prices)
        self.pause('4.d')

        # ---- 4.e · Both ways to model the tax, with the same two prices and quantity side by side.
        buyer_readout = fixed(Tex(r'$P_b=5.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2))
        seller_readout = fixed(Tex(r'$P_s=3.60$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2))
        either_note = fixed(Tex(r'Either way: buyers pay \$5.60, sellers receive \$3.60.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(pay_note)
        self.play(FadeOut(plus_tax_readout), FadeOut(new_price_readout), FadeIn(buyer_readout), FadeIn(seller_readout))
        seller_comparison_head = fixed(title('A Tax On Sellers', align=RIGHT))
        seller_comparison_context = fixed(subtitle(seller_comparison_head, r'Sellers hand \$2 per unit to the government.')
                                          .align_to(seller_comparison_head, RIGHT).set_y(context.get_y()))
        # Keep the buyer graph intact: both panels use the opening square plot, uniformly scaled.
        buyer_comparison_graph = fixed(VGroup(market, buyer_strips, taxed_demand, taxed_demand_word,
                                              buyer_point, buyer_prices, buyer_readout, seller_readout))
        # The old seller strips became buyer strips in 4.b; rebuild only that distinct tax model.
        seller_comparison_strips = fixed(VGroup()).set_z_index(-1)
        for q in range(TAX_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            seller_comparison_strips.add(fixed(Polygon(
                ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 2 + right / 20 + TAX), ax.c2p(left, 2 + left / 20 + TAX),
                stroke_width=0, fill_color=GOV, fill_opacity=STRIP_OPACITY).set_z_index(-1)))
        seller_comparison_marks = fixed(VGroup(
            buyer_prices[1].copy(), buyer_point[0].copy(), buyer_prices[2].copy(), buyer_prices[0].copy(),
            buyer_point[1].copy(), buyer_readout.copy(), seller_readout.copy(), buyer_point[2].copy()))
        # Deep-copy the axes too, so their c2p lookup follows this panel when it moves.
        seller_comparison_graph = fixed(VGroup(market.copy(deep=True), seller_comparison_strips,
            taxed_supply.copy(), taxed_supply_word.copy(), seller_comparison_marks))
        # A shared bounding box gives the plots identical sizes and aligned axes despite different labels.
        comparison_bounds = VGroup(buyer_comparison_graph, seller_comparison_graph)
        comparison_anchor = comparison_bounds.get_center()
        comparison_scale = min(0.88, 7.2 / comparison_bounds.width)
        comparison_shift = np.array([0, BODY_MID, 0]) - comparison_anchor
        seller_comparison_graph.scale(comparison_scale, about_point=comparison_anchor).shift(comparison_shift + RIGHT * 4)
        self.remove(*buyer_comparison_graph)
        self.add(buyer_comparison_graph)
        self.play(buyer_comparison_graph.animate.scale(comparison_scale, about_point=comparison_anchor)
                      .shift(comparison_shift + LEFT * 4),
                  FadeIn(seller_comparison_graph), FadeIn(seller_comparison_head), FadeIn(seller_comparison_context),
                  FadeIn(either_note), run_time=1.4)
        self.play(*[Indicate(marks[index], color=FOCUS, scale_factor=1.4 if index < 2 else 1.2)
                    for marks in [(buyer_prices[1], buyer_point[0], buyer_point[2]),
                                  (seller_comparison_marks[0], seller_comparison_marks[1], seller_comparison_marks[7])]
                    for index in (0, 1, 2)], run_time=0.5)
        self.pause('4.e')

        # ---- 5.a · Keep both models while introducing the same $2 wedge on each price axis.
        self.remove(head, context, either_note)
        head = fixed(title('The Tax Wedge'))
        context = fixed(subtitle(head, 'What buyers pay and what sellers receive.'))
        # Ungroup the panels without moving their contents; later beats retain the original buyer objects.
        self.remove(buyer_comparison_graph, seller_comparison_graph)
        self.add(*buyer_comparison_graph, *seller_comparison_graph)
        seller_market = seller_comparison_graph[0]
        seller_ax = seller_market[0]
        seller_taxed_supply, seller_taxed_supply_word = seller_comparison_graph[2:4]
        wedge_marks = fixed(VGroup(
            buyer_prices[1], buyer_point[0], buyer_prices[2], buyer_prices[0],
            buyer_point[1], buyer_readout, seller_readout, buyer_point[2]))
        self.remove(buyer_point, buyer_prices, buyer_readout, seller_readout)
        self.add(wedge_marks)
        for marks in (wedge_marks, seller_comparison_marks):
            marks[0].set_z_index(10)
            marks[1].set_z_index(10)
        quantity_guides = [fixed(DashedLine(graph_ax.c2p(TAX_Q, 0), graph_ax.c2p(TAX_Q, BUYER_PRICE),
                           color=GUIDE, stroke_width=2 * comparison_scale)).set_z_index(2)
                           for graph_ax in (ax, seller_ax)]
        # Each axis keeps its labeled measurement; a filled tax strip will slide between the original curves.
        AXIS_Q = -1.2
        axis_wedge = fixed(DashedLine(
            ax.c2p(AXIS_Q, SELLER_PRICE), ax.c2p(AXIS_Q, BUYER_PRICE),
            color=GOV, stroke_width=2.5 * comparison_scale,
            dash_length=0.045 * comparison_scale)).set_z_index(2)
        # The label carries a rolling number so section 7 can drive it in place, without a crossfade.
        sliding_word = fixed(VGroup(Tex(r'Tax $=$ \$', color=GOV).scale(0.6),
            DecimalNumber(TAX, num_decimal_places=0, color=GOV).scale(0.6)).arrange(RIGHT, buff=0.06))
        sliding_word.next_to(axis_wedge, LEFT, buff=0.10)
        sliding_word.scale(comparison_scale).next_to(axis_wedge, LEFT, buff=0.10 * comparison_scale)
        seller_axis_wedge = axis_wedge.copy().shift(RIGHT * 8)
        seller_sliding_word = sliding_word.copy().shift(RIGHT * 8)
        wedge_definition = fixed(Tex("The tax wedge: the buyers' price minus the sellers' price equals the tax.", color=DEFINITION)
                                 .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(context), FadeOut(seller_comparison_head), FadeOut(seller_comparison_context),
                  FadeOut(buyer_strips), FadeOut(seller_comparison_strips),
                  Transform(wedge_marks[4], quantity_guides[0]), Transform(seller_comparison_marks[4], quantity_guides[1]),
                  FadeIn(axis_wedge), FadeIn(sliding_word), FadeIn(seller_axis_wedge), FadeIn(seller_sliding_word),
                  FadeIn(wedge_definition))
        self.pause('5.a')

        # ---- 5.b · Slide one filled tax strip into each model, stopping between MB and MC at Q = 32.
        moving_tax_bars = []
        for graph_ax in (ax, seller_ax):
            # Match the width, color and fill of the one-unit strips from the two tax models.
            left, right = AXIS_Q - 1 + BAR_GAP / 2, AXIS_Q - BAR_GAP / 2
            moving_tax_bars.append(fixed(Polygon(
                graph_ax.c2p(left, SELLER_PRICE), graph_ax.c2p(right, SELLER_PRICE),
                graph_ax.c2p(right, BUYER_PRICE), graph_ax.c2p(left, BUYER_PRICE),
                stroke_width=0, fill_color=GOV, fill_opacity=STRIP_OPACITY)).set_z_index(2))
        sliding_wedge, seller_sliding_wedge = moving_tax_bars
        slide_note = fixed(Tex('Slide the tax in from the left until it gets stuck between the curves.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(wedge_definition)
        self.play(FadeIn(slide_note), FadeIn(sliding_wedge), FadeIn(seller_sliding_wedge))
        self.play(sliding_wedge.animate.shift(ax.c2p(TAX_Q, 0) - ax.c2p(AXIS_Q, 0)),
                  seller_sliding_wedge.animate.shift(seller_ax.c2p(TAX_Q, 0) - seller_ax.c2p(AXIS_Q, 0)),
                  run_time=2.6, rate_func=smooth)
        # The adjusted curves have done their job only once both wedges are stuck in place.
        self.play(FadeOut(taxed_demand), FadeOut(taxed_demand_word),
                  FadeOut(seller_taxed_supply), FadeOut(seller_taxed_supply_word), run_time=0.5)
        self.pause('5.b')

        # ---- 5.c.wedge · Keep the buyer graph intact as the duplicate gives way to the shared calculation.
        graph_block = fixed(VGroup(market, sliding_wedge, axis_wedge, sliding_word, wedge_marks))
        self.remove(market, sliding_wedge, axis_wedge, sliding_word, wedge_marks)
        self.add(graph_block)
        seller_wedge_graph = fixed(VGroup(seller_market, seller_comparison_marks,
                                         seller_axis_wedge, seller_sliding_word, seller_sliding_wedge))
        self.remove(*seller_wedge_graph)
        self.add(seller_wedge_graph)
        # Undo the panel's uniform transform, then apply the established algebra layout in one motion.
        algebra_graph_target = graph_block.copy(deep=True).shift(-comparison_shift - LEFT * 4)
        algebra_graph_target.scale(1 / comparison_scale, about_point=comparison_anchor)
        algebra_graph_target.scale(0.72, about_point=algebra_graph_target[0][0].c2p(0, 0)).shift(LEFT * 1.0)
        solve_note = fixed(Tex('Use the wedge equation and the two curves to solve for the quantity.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(slide_note)
        self.play(Transform(graph_block, algebra_graph_target), FadeOut(seller_wedge_graph), run_time=1.1)
        divider = fixed(Line([2.45, -3.0, 0], [2.45, 2.3, 0], color=MUTED, stroke_width=1.5))
        wedge_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$-$', color=INK), Tex('$P_s$', color=GUIDE),
            Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        substitute_line = fixed(VGroup(Tex('$(12 - Q/5)$', color=DEMAND), Tex('$-$', color=INK),
            Tex('$(2 + Q/20)$', color=SUPPLY), Tex('$=$', color=INK), Tex('$2$', color=GOV)).arrange(RIGHT, buff=0.14).scale(0.78))
        simplify_line = fixed(VGroup(Tex('$10 - Q/4$', color=INK), Tex('$=$', color=INK), Tex('$2$', color=GOV))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        solve_line = fixed(VGroup(Tex('$Q^{tax}$', color=GUIDE), Tex('$=$', color=INK), Tex('$32$', color=GUIDE))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        buyer_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$=$', color=INK), Tex('$12 - 32/5$', color=DEMAND),
            Tex('$=$', color=INK), Tex('$5.60$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        seller_line = fixed(VGroup(Tex('$P_s$', color=GUIDE), Tex('$=$', color=INK), Tex('$2 + 32/20$', color=SUPPLY),
            Tex('$=$', color=INK), Tex('$3.60$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        step_one = fixed(Tex(narration('Step 1: find the quantity'), color=CAPTION).scale(0.6))
        step_two = fixed(Tex(narration('Step 2: find the prices'), color=CAPTION).scale(0.6))
        for line in (wedge_line, substitute_line, simplify_line, solve_line, buyer_line, seller_line):
            line.scale(0.72 / 0.78)
        algebra = fixed(VGroup(step_one, wedge_line, substitute_line, simplify_line, solve_line, step_two, buyer_line, seller_line)
            .arrange(DOWN, buff=0.24).move_to([5.2, 0.05, 0]))
        step_two.shift(DOWN * 0.08)
        self.play(FadeIn(divider), FadeIn(step_one), FadeIn(wedge_line), FadeIn(solve_note))
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
        self.play(FadeIn(step_two), FadeIn(buyer_line), FadeIn(price_note))
        self.play(FadeIn(seller_line))
        self.pause('5.c')
        self.play(FadeOut(algebra), FadeOut(divider), FadeOut(price_note), run_time=0.5)
        self.play(graph_block.animate.shift(RIGHT * 1.0).scale(1 / 0.72, about_point=ax.c2p(0, 0) + RIGHT * 1.0), run_time=1.1)
        self.remove(graph_block)
        self.add(market, sliding_wedge, axis_wedge, sliding_word, wedge_marks)

        # ---- 6.a.select · Welfare with a tax, starting from the first exchange again.
        self.remove(head, context)
        head = fixed(title('Welfare With A Tax'))
        context = fixed(subtitle(head, 'The first unit: still exchanged with the tax.'))
        # Market slice and close-up share one structure: buyer base, tax band, CS, MB edge, cost, PS, MC edge, baseline.
        taxed_first_home = fixed(VGroup(
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(ax.c2p(l0, SELLER_PRICE), ax.c2p(r0, SELLER_PRICE), ax.c2p(r0, BUYER_PRICE), ax.c2p(l0, BUYER_PRICE),
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Polygon(ax.c2p(l0, BUYER_PRICE), ax.c2p(r0, BUYER_PRICE), ax.c2p(r0, 12 - r0 / 5), ax.c2p(l0, 12 - l0 / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 12 - l0 / 5), ax.c2p(r0, 12 - r0 / 5), color=DEMAND, stroke_width=3),
            Polygon(ax.c2p(l0, 0), ax.c2p(r0, 0), ax.c2p(r0, 2 + r0 / 20), ax.c2p(l0, 2 + l0 / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0),
            Polygon(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), ax.c2p(r0, SELLER_PRICE), ax.c2p(l0, SELLER_PRICE),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY),
            Line(ax.c2p(l0, 2 + l0 / 20), ax.c2p(r0, 2 + r0 / 20), color=SUPPLY, stroke_width=3),
            Line(ax.c2p(l0, 0), ax.c2p(r0, 0), color=MUTED)))
        # In the close-up the tax is the narrow middle bar between the two prices, where 2.d left it; its share of
        # welfare takes SURPLUS_OPACITY like CS and PS, and on the carry-back it becomes the slice's revenue band.
        taxed_first_target = fixed(VGroup(
            Polygon([BUYER_LEFT, first_y(0), 0], [BUYER_LEFT + BAR_WIDTH, first_y(0), 0],
                [BUYER_LEFT + BAR_WIDTH, first_y(12), 0], [BUYER_LEFT, first_y(12), 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=BASE_OPACITY),
            Polygon([TAX_LEFT, first_y(SELLER_PRICE), 0], [TAX_LEFT + TAX_WIDTH, first_y(SELLER_PRICE), 0],
                [TAX_LEFT + TAX_WIDTH, first_y(BUYER_PRICE), 0], [TAX_LEFT, first_y(BUYER_PRICE), 0],
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
            Line([-1.9, first_y(0), 0], [1.9, first_y(0), 0], color=MUTED)))
        # Compact labels as in 2.a: numbers outside the bars at their boundary heights, names on the bars.
        taxed_first_values = fixed(VGroup(
            Tex(r'$\$12$', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, first_y(12), 0], LEFT, buff=0.25),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, first_y(12), 0], UP, buff=0.10),
            Tex(r'$\$2$', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, first_y(2), 0], RIGHT, buff=0.25),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, first_y(2), 0], DOWN, buff=0.10))).set_z_index(3)
        # The two market prices: red lines with their names on them and their numbers at the left ends.
        # Both names sit outside the pair of lines, as in 2.d, 6.c and 9.d: P_b above the upper line, P_s under the lower.
        taxed_first_prices = fixed(VGroup(
            Line([-2.6, first_y(BUYER_PRICE), 0], [1.9, first_y(BUYER_PRICE), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, first_y(SELLER_PRICE), 0], [1.9, first_y(SELLER_PRICE), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        taxed_first_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, first_y(BUYER_PRICE), 0], UP, buff=0.06),
            Tex(r'$\$5.60$', color=GUIDE).scale(0.72).next_to([-2.6, first_y(BUYER_PRICE), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, first_y(SELLER_PRICE), 0], DOWN, buff=0.06),
            Tex(r'$\$3.60$', color=GUIDE).scale(0.72).next_to([-2.6, first_y(SELLER_PRICE), 0], LEFT, buff=0.15))).set_z_index(3)
        taxed_first_labels = fixed(VGroup(
            Tex('PS', color=INK).scale(0.58).move_to([1.21, first_y((2 + SELLER_PRICE) / 2), 0]),
            Tex('tax', color=INK).scale(0.55)
                .move_to([TAX_LEFT + TAX_WIDTH / 2, first_y((SELLER_PRICE + BUYER_PRICE) / 2), 0]),
            Tex('CS', color=INK).scale(0.58).move_to([-1.21, first_y((BUYER_PRICE + 12) / 2), 0]))).set_z_index(3)
        # The selected slice shows no split yet: the fills stay hidden until the close-up reveals them.
        taxed_first_pair = taxed_first_home.copy()
        for index in (1, 2, 5):
            taxed_first_pair[index].set_fill(opacity=0)
        first_selection = fixed(SurroundingRectangle(taxed_first_home, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxed_first_pair), FadeIn(first_selection))
        self.pause('6.a.select')

        # ---- 6.a.prices · Values first, then both market prices.
        self.play(FadeOut(market), FadeOut(sliding_wedge), FadeOut(axis_wedge), FadeOut(sliding_word), FadeOut(wedge_marks),
                  FadeOut(first_selection), Transform(taxed_first_pair, taxed_first_target), run_time=1.6)
        self.add(people, government)
        self.play(FadeIn(taxed_first_values))
        self.play(FadeIn(taxed_first_prices), FadeIn(taxed_first_price_words))
        self.pause('6.a.prices')

        # ---- 6.a · The unit's surplus splits three ways and the exchange survives.
        split_note = fixed(Tex(r'Still exchanged: MB above $P_b$, MC below $P_s$.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(taxed_first_pair[5].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_labels[0]))
        self.play(taxed_first_pair[1].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_labels[1]))
        self.play(taxed_first_pair[2].animate.set_fill(opacity=SURPLUS_OPACITY), FadeIn(taxed_first_labels[2]),
                  FadeIn(split_note))
        self.pause('6.a')

        # ---- 6.b · Back to the market: every exchanged unit splits the same way.
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
            Tex('GOV', color=INK).scale(0.72).move_to(ax.c2p(TAX_Q / 2, (BUYER_PRICE + SELLER_PRICE) / 2)),
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(TAX_Q / 3, (12 + 2 * BUYER_PRICE) / 3))))
        revenue_note = fixed(Tex(r'Tax revenue: \$2 $\times$ 32 units $=$ \$64.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(people, government)
        self.play(FadeOut(taxed_first_values), FadeOut(taxed_first_prices), FadeOut(taxed_first_price_words),
                  FadeOut(taxed_first_labels), FadeOut(split_note), run_time=0.4)
        self.remove(context)
        context = fixed(subtitle(head, '32 units exchanged with the tax.'))
        self.add(context)
        self.play(Transform(taxed_first_pair, taxed_first_home),
                  FadeIn(market), FadeIn(sliding_wedge), FadeIn(axis_wedge), FadeIn(sliding_word), FadeIn(wedge_marks), run_time=1.6)
        # Fills sit under the guides and dots: re-add the marks after every batch of bars.
        self.play(FadeOut(taxed_first_pair), FadeIn(ps_taxed[0]), FadeIn(tax_bars[0]), FadeIn(cs_taxed[0]), run_time=0.4)
        self.remove(sliding_wedge, axis_wedge, sliding_word, wedge_marks)
        self.add(sliding_wedge, axis_wedge, sliding_word, wedge_marks)
        self.play(LaggedStart(*[AnimationGroup(FadeIn(ps_taxed[q]), FadeIn(tax_bars[q]), FadeIn(cs_taxed[q]))
                                for q in range(1, TAX_Q)], lag_ratio=0.1), run_time=3)
        self.remove(*list(ps_taxed), *list(tax_bars), *list(cs_taxed), sliding_wedge, axis_wedge, sliding_word, wedge_marks)
        self.add(ps_taxed, tax_bars, cs_taxed, sliding_wedge, axis_wedge, sliding_word, wedge_marks)
        self.play(FadeIn(welfare_words), FadeIn(revenue_note))
        self.pause('6.b')

        # ---- 6.c.question · The units the tax removes.
        lost_question = fixed(Tex('What about the units no longer exchanged?', color=DEFINITION)
                              .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        left, right = LOST_TON + BAR_GAP / 2, LOST_TON + 1 - BAR_GAP / 2
        lost_pair = fixed(VGroup(
            Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0)))
        lost_home = lost_pair.copy()
        lost_selection = fixed(SurroundingRectangle(lost_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(revenue_note)
        self.play(FadeIn(lost_question))
        self.pause('6.c.question')

        # ---- 6.c.select · Pick unit 36 from the existing bars.
        self.remove(lost_question)
        self.play(FadeIn(lost_pair), FadeIn(lost_selection))
        self.pause('6.c.select')

        # ---- 6.c.values · C1's 36th unit in the compact close-up, with C1's two questions.
        lost_target = fixed(VGroup())
        for bar_left, value, color in [(BUYER_LEFT, 4.8, DEMAND), (SELLER_LEFT, 3.8, SUPPLY)]:
            lost_target.add(fixed(Polygon([bar_left, detail_y(0), 0], [bar_left + BAR_WIDTH, detail_y(0), 0],
                [bar_left + BAR_WIDTH, detail_y(value), 0], [bar_left, detail_y(value), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        welfare_market = fixed(VGroup(market, ps_taxed, tax_bars, cs_taxed, welfare_words, sliding_wedge, axis_wedge, sliding_word, wedge_marks))
        self.remove(market, sliding_wedge, axis_wedge, sliding_word, wedge_marks, ps_taxed, tax_bars, cs_taxed, welfare_words)
        self.add(welfare_market)
        self.play(FadeOut(welfare_market), FadeOut(lost_selection), FadeOut(context), Transform(lost_pair, lost_target), run_time=1.6)
        context = fixed(subtitle(head, 'The 36th unit: exchanged before the tax.'))
        lost_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(lost_target, [DEMAND, SUPPLY])],
            Line([-1.9, detail_y(0), 0], [1.9, detail_y(0), 0], color=MUTED)))
        # Compact labels: numbers outside at their boundary heights, both names above their edges (clear of the price lines).
        lost_values = fixed(VGroup(
            Tex(r'$\$4.80$', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(4.8), 0], LEFT, buff=0.25),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(4.8), 0], UP, buff=0.10),
            Tex(r'$\$3.80$', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(3.8), 0], RIGHT, buff=0.25),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(3.8), 0], UP, buff=0.10))).set_z_index(3)
        # Private willingness and social value are separate questions.
        lost_questions = fixed(VGroup(
            Tex('Will the buyer buy?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(people, government)
        self.play(FadeIn(lost_edges), FadeIn(lost_values), FadeIn(context), run_time=0.4)
        self.play(FadeIn(lost_questions[0]), FadeIn(lost_questions[1]))
        self.pause('6.c.values')

        # ---- 6.c.private.compare · The tax's two prices around the unit, then each side against its own price.
        lost_prices = fixed(VGroup(
            Line([-2.6, detail_y(BUYER_PRICE), 0], [1.9, detail_y(BUYER_PRICE), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(SELLER_PRICE), 0], [1.9, detail_y(SELLER_PRICE), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        # P_s sits under its line: MC is only 0.20 above it, and the MC guide would cross the name.
        lost_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(BUYER_PRICE), 0], UP, buff=0.06),
            Tex(r'$\$5.60$', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(BUYER_PRICE), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(SELLER_PRICE), 0], DOWN, buff=0.06),
            Tex(r'$\$3.60$', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(SELLER_PRICE), 0], LEFT, buff=0.15))).set_z_index(3)
        # The tax: the narrow middle bar between the two prices, where 2.d and 6.a put it. Read left to right, the buyer
        # pays P_b, the tax is the step in the middle, and the seller receives P_s. In welfare it takes SURPLUS_OPACITY.
        lost_tax = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(SELLER_PRICE), 0], [TAX_LEFT + TAX_WIDTH, detail_y(SELLER_PRICE), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(BUYER_PRICE), 0], [TAX_LEFT, detail_y(BUYER_PRICE), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex('tax', color=INK).scale(0.55))).set_z_index(1)
        lost_tax[1].move_to(lost_tax[0]).set_z_index(3)
        # Buyer pair: MB against P_b. Seller pair: MC projected leftward across the gap and the buyer column against P_s,
        # in segments that skip the tax bar (0.12 clear on either side) and the P_s number, which sits at nearly the same height.
        lost_private_guides = fixed(VGroup(
            DashedLine(lost_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(lost_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(BUYER_PRICE), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.8), 0], [-4.25, detail_y(BUYER_PRICE), 0], color=DEMAND, stroke_width=3),
            DashedLine([SELLER_LEFT, detail_y(3.8), 0], [TAX_LEFT + TAX_WIDTH + 0.12, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.12, detail_y(3.8), 0], [lost_price_words[3].get_right()[0] + 0.12, detail_y(3.8), 0],
                       color=TOTAL, stroke_width=1.4),
            DashedLine([lost_price_words[3].get_left()[0] - 0.12, detail_y(3.8), 0], [-4.25, detail_y(3.8), 0],
                       color=TOTAL, stroke_width=1.4),
            DashedLine(lost_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(SELLER_PRICE), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(SELLER_PRICE), 0], [-4.25, detail_y(3.8), 0], color=SUPPLY, stroke_width=3)))
        # The market's answer: one red cross, centered in the gap between the two brackets.
        lost_private_answer = fixed(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5), Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)
            .next_to([-4.25, detail_y((3.8 + 4.8) / 2), 0], LEFT, buff=0.3))
        self.play(FadeIn(lost_prices), FadeIn(lost_price_words), FadeIn(lost_tax))
        # Read the buyer's decision first, then the seller's, with a separate question and pause.
        lost_buyer_guides = fixed(VGroup(*list(lost_private_guides)[:3]))
        lost_seller_guides = fixed(VGroup(*list(lost_private_guides)[3:]))
        self.play(FadeIn(lost_buyer_guides))
        self.pause('6.c.private.buyer')
        lost_seller_question = fixed(Tex('Will the seller sell?', color=DEFINITION)
            .scale(0.60).move_to([-4.8, -3.05, 0]))
        self.play(FadeOut(lost_questions[0]), FadeIn(lost_seller_question), FadeIn(lost_seller_guides))
        lost_questions = fixed(VGroup(lost_seller_question, lost_questions[1]))
        self.remove(lost_buyer_guides, lost_seller_guides)
        self.add(lost_private_guides)
        self.pause('6.c.private.compare')

        # ---- 6.c.private · Neither side will: not exchanged.
        lost_exchange_question = fixed(Tex('Will they exchange?', color=DEFINITION)
            .scale(0.60).move_to([-4.8, -3.05, 0]))
        self.play(FadeOut(lost_questions[0]), FadeIn(lost_exchange_question), FadeIn(lost_private_answer))
        lost_questions = fixed(VGroup(lost_exchange_question, lost_questions[1]))
        self.pause('6.c.private')

        # ---- 6.c.social.compare · The tax bar's job is done; society compares MB with MC, as in C1.
        # MB crosses the empty gap, then runs from the seller column's right edge to the bracket.
        lost_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [SELLER_LEFT, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([SELLER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(lost_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(3.8), 0], [4.25, detail_y(4.8), 0], color=TOTAL, stroke_width=3)))
        # Society's answer: a green check over the TS label.
        lost_social_answer = fixed(VGroup(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex('TS', color=TOTAL)).arrange(DOWN, buff=0.16).scale(0.70)
            .next_to([4.25, detail_y((3.8 + 4.8) / 2), 0], RIGHT, buff=0.3))
        self.play(FadeOut(lost_tax), FadeIn(lost_social_guides))
        self.pause('6.c.social.compare')

        # ---- 6.c.loss · Yes for society: the surplus this unit would have made is deadweight loss.
        lost_dwl_bar = fixed(Polygon([BUYER_LEFT, detail_y(3.8), 0], [BUYER_LEFT + BAR_WIDTH, detail_y(3.8), 0],
            [BUYER_LEFT + BAR_WIDTH, detail_y(4.8), 0], [BUYER_LEFT, detail_y(4.8), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        lost_note = fixed(Tex(r'The tax removes this trade, losing \$1 of surplus.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(lost_dwl_bar), FadeIn(lost_social_answer), FadeIn(lost_note), run_time=0.5)
        self.pause('6.c.loss')

        # ---- 6.c.return · The unit and its loss carry back to the 36th slice.
        lost_dwl_market = fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
            ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        self.remove(people, government)
        self.play(FadeOut(lost_edges), FadeOut(lost_values), FadeOut(lost_questions), FadeOut(lost_prices), FadeOut(lost_price_words),
                  FadeOut(lost_private_guides), FadeOut(lost_private_answer),
                  FadeOut(lost_social_guides), FadeOut(lost_social_answer), FadeOut(lost_note), FadeOut(context), run_time=0.4)
        context = fixed(subtitle(head, '32 units exchanged with the tax.'))
        self.play(Transform(lost_pair, lost_home), Transform(lost_dwl_bar, lost_dwl_market),
                  FadeIn(welfare_market), FadeIn(context), run_time=1.6)
        self.play(FadeOut(lost_pair))
        self.pause('6.c.return')

        # ---- 6.d · The other seven removed units.
        dwl_bars = fixed(VGroup())
        for q in range(TAX_Q, MARKET_Q):
            if q == LOST_TON:
                dwl_bars.add(lost_dwl_bar)
                continue
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            dwl_bars.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1)))
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(ax.c2p(40, 5.1), RIGHT, buff=0.25))  # Clear of S / MC.
        removed_note = fixed(Tex('Deadweight loss: the surplus of the units no longer exchanged.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(LaggedStart(*[FadeIn(bar) for bar in dwl_bars if bar is not lost_dwl_bar], lag_ratio=0.18), run_time=1.6)
        self.remove(*[bar for bar in dwl_bars])
        self.add(dwl_bars)
        self.play(FadeIn(dwl_word), FadeIn(removed_note))
        self.pause('6.d')

        # ---- 7.a · Change the tax in the same bar-by-bar market, with its existing labels and axis wedge.
        self.remove(head, context, removed_note)
        head = fixed(title('Changing The Tax'))
        self.remove(welfare_market, welfare_words, wedge_marks, axis_wedge)
        self.add(market, sliding_wedge, sliding_word, ps_taxed, tax_bars, cs_taxed)
        tax, d_slope, s_slope = ValueTracker(TAX), ValueTracker(0.2), ValueTracker(0.05)
        cost_region = fixed(VGroup())  # MC base fills remain hidden.
        ps_region, tax_region, cs_region, dwl_region = ps_taxed, tax_bars, cs_taxed, dwl_bars
        # Keep the displayed bars themselves. Hidden slots let individual units enter and leave smoothly.
        for bars in (ps_region, tax_region, cs_region):
            for q in range(TAX_Q, MARKET_Q):
                bars.add(bars[0].copy().set_fill(opacity=0))
        dwl_region.set_submobjects([dwl_bars[0].copy().set_fill(opacity=0)
                                   for q in range(TAX_Q)] + list(dwl_bars))

        def update_tax_bars(bars):
            quantity, buyer_price, seller_price = wedge_state(bars.tax.get_value(), bars.d.get_value(), bars.s.get_value())
            for q, bar in enumerate(bars):
                left, right = q + bars.gap / 2, q + 1 - bars.gap / 2
                if bars.kind == 'dwl':
                    left = max(left, quantity)
                else:
                    right = min(right, quantity)
                if right <= left:
                    bar.set_fill(opacity=0)
                    continue
                if bars.kind == 'ps':
                    low_left, low_right, high_left, high_right = 2 + left / 20, 2 + right / 20, seller_price, seller_price
                elif bars.kind == 'tax':
                    low_left = low_right = seller_price
                    high_left = high_right = buyer_price
                elif bars.kind == 'cs':
                    low_left = low_right = buyer_price
                    high_left, high_right = 12 - left / 5, 12 - right / 5
                else:
                    low_left, low_right = 2 + left / 20, 2 + right / 20
                    high_left, high_right = 12 - left / 5, 12 - right / 5
                bar.set_points_as_corners([
                    bars.axes.c2p(left, low_left), bars.axes.c2p(right, low_right),
                    bars.axes.c2p(right, high_right), bars.axes.c2p(left, high_left), bars.axes.c2p(left, low_left)])
                bar.set_fill(opacity=bars.bar_opacity if high_left > low_left or high_right > low_right else 0)

        for bars, kind in [(ps_region, 'ps'), (tax_region, 'tax'), (cs_region, 'cs'), (dwl_region, 'dwl')]:
            bars.axes, bars.tax, bars.d, bars.s = ax, tax, d_slope, s_slope
            bars.kind, bars.gap, bars.bar_opacity = kind, BAR_GAP, 0.8 if kind == 'dwl' else SURPLUS_OPACITY
            bars.add_updater(update_tax_bars)

        # Retain the filled wedge at the quantity and the separate measurement on the price axis.
        wedge = fixed(VGroup(sliding_wedge, wedge_marks[0], wedge_marks[1],
                             wedge_marks[2], wedge_marks[3], wedge_marks[4], axis_wedge))
        wedge_word = fixed(VGroup(Tex(r'Tax $=$ \$', color=GOV).scale(0.6),
            DecimalNumber(TAX, num_decimal_places=0, color=GOV).scale(0.6)).arrange(RIGHT, buff=0.06))
        wedge_word.set_height(sliding_word.get_height()).move_to(sliding_word)
        buyer_price_readout = fixed(VGroup(Tex('$P_b=$', color=GUIDE).scale(0.7),
            DecimalNumber(BUYER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        seller_price_readout = fixed(VGroup(Tex('$P_s=$', color=GUIDE).scale(0.7),
            DecimalNumber(SELLER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        quantity_readout = fixed(VGroup(Tex('$Q^{tax}=$', color=GUIDE).scale(0.7),
            DecimalNumber(TAX_Q, num_decimal_places=0, color=GUIDE).scale(0.7)).arrange(RIGHT, buff=0.06))
        ps_label, tax_label, cs_label = welfare_words
        dwl_label = dwl_word
        driven = [*wedge, wedge_word, buyer_price_readout, seller_price_readout, quantity_readout,
                  cs_label, ps_label, tax_label, dwl_label]
        for m in driven:
            m.axes, m.tax, m.d, m.s = ax, tax, d_slope, s_slope
        wedge[0].gap = BAR_GAP
        wedge[0].add_updater(lambda m: m.set_points_as_corners([
            m.axes.c2p(state(m)[0] - 1 + m.gap / 2, state(m)[2]),
            m.axes.c2p(state(m)[0] - m.gap / 2, state(m)[2]),
            m.axes.c2p(state(m)[0] - m.gap / 2, state(m)[1]),
            m.axes.c2p(state(m)[0] - 1 + m.gap / 2, state(m)[1]),
            m.axes.c2p(state(m)[0] - 1 + m.gap / 2, state(m)[2])]))
        wedge[1].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[1])))
        wedge[2].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[2])))
        wedge[3].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[1]),
            m.axes.c2p(state(m)[0], state(m)[1]), color=GUIDE, stroke_width=2))).set_z_index(2))
        wedge[4].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[2]),
            m.axes.c2p(state(m)[0], state(m)[2]), color=GUIDE, stroke_width=2))).set_z_index(2))
        wedge[5].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(state(m)[0], 0),
            m.axes.c2p(state(m)[0], state(m)[1]), color=GUIDE, stroke_width=2))).set_z_index(2))
        wedge[6].axis_q = AXIS_Q
        wedge[6].add_updater(lambda m: fixed(m.become(DashedLine(
            m.axes.c2p(m.axis_q, state(m)[2]), m.axes.c2p(m.axis_q, state(m)[1]) + UP * 1e-6,
            color=GOV, stroke_width=2.5, dash_length=0.045)))
            .set_z_index(2).set_opacity(1 if abs(m.tax.get_value()) > 1e-5 else 0))
        wedge_word.axis_q = AXIS_Q
        wedge_word.add_updater(lambda m: (m[1].set_value(abs(m.tax.get_value())), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(m.axis_q, (state(m)[1] + state(m)[2]) / 2), LEFT, buff=0.10)))
        # Separate only the readouts when the two prices approach one another.
        buyer_price_readout.add_updater(lambda m: (m[1].set_value(state(m)[1]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[1]), LEFT, buff=0.2)
            .shift(UP * 0.27 * max(0, 1 - (state(m)[1] - state(m)[2]) / 1.2))))
        seller_price_readout.add_updater(lambda m: (m[1].set_value(state(m)[2]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[2]), LEFT, buff=0.2)
            .shift(DOWN * 0.27 * max(0, 1 - (state(m)[1] - state(m)[2]) / 1.2))))
        quantity_readout.add_updater(lambda m: (m[1].set_value(state(m)[0]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(state(m)[0], 0), DOWN, buff=0.2)))
        cs_label.add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0] / 3, (12 + 2 * state(m)[1]) / 3)))
        ps_label.natural_height = ps_label.get_height()
        ps_label.add_updater(lambda m: m.set_height(min(m.natural_height,
            0.55 * (m.axes.c2p(0, state(m)[2])[1] - m.axes.c2p(0, 2 + state(m)[0] / 60)[1])))
            .move_to(m.axes.c2p(state(m)[0] / 3, (2 + 2 * state(m)[2]) / 3)))
        tax_label.natural_width = tax_label.get_width()
        tax_label.add_updater(lambda m: m.set_width(min(m.natural_width,
            0.85 * (m.axes.c2p(state(m)[0], 0)[0] - m.axes.c2p(0, 0)[0])))
            .move_to(m.axes.c2p(state(m)[0] / 2, (state(m)[1] + state(m)[2]) / 2))
            .set_opacity(min(1, abs(m.tax.get_value()) / 0.8)))
        dwl_label.add_updater(lambda m: m.set_opacity(min(1, abs(m.tax.get_value()) / 0.8)))
        change_question = fixed(Tex('What happens as the tax changes?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # Hand off to live geometry without fading or replacing the bar fills or their labels.
        self.remove(sliding_wedge, sliding_word)
        self.add(wedge, wedge_word, buyer_price_readout, seller_price_readout, quantity_readout,
                 ps_label, tax_label, cs_label, dwl_label)
        for m in [ps_region, tax_region, cs_region, dwl_region, *driven]:
            m.update()
        self.play(FadeIn(head), FadeIn(change_question), run_time=1.2)
        self.play(tax.animate.set_value(0), run_time=2.2, rate_func=smooth)
        zero_note = fixed(Tex('No tax: one price, the untaxed equilibrium.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(change_question)
        self.play(FadeIn(zero_note))
        self.pause('7.a.zero')
        self.remove(zero_note)
        self.play(FadeIn(change_question))
        self.play(tax.animate.set_value(5), run_time=3.2, rate_func=smooth)
        self.pause('7.a.five')
        growth_note = fixed(Tex('A larger tax: more revenue, but DWL grows faster.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(change_question)
        self.play(FadeIn(growth_note))
        self.play(tax.animate.set_value(TAX), run_time=2.2, rate_func=smooth)
        self.pause('7.a')

        # ---- 8.a · Tax incidence: the same $2 wedge on two small graphs, the left fixed, the right about to change slope.
        self.remove(head, growth_note)
        head = fixed(title('Tax Incidence'))
        context = fixed(subtitle(head, r'How the \$2 tax is split between buyers and sellers.'))
        # Section 7's trackers have settled: freeze every rolling number before anything fades.
        for m in [wedge_word, buyer_price_readout, seller_price_readout, quantity_readout, cs_label, ps_label, tax_label, dwl_label]:
            m.update()
        for m in [cost_region, ps_region, tax_region, cs_region, dwl_region, *wedge, wedge_word,
                  buyer_price_readout, seller_price_readout, quantity_readout, cs_label, ps_label, tax_label, dwl_label]:
            m.clear_updaters()
        # Both graphs keep unlabeled grey guides at the untaxed price and quantity, alongside the wedge
        # and the incidence stack off the axis (buyers' share above 4, sellers' share below).
        STACK_Q = -20
        incidence_graphs = fixed(VGroup())
        for origin_x in (-5.3, 2.5):
            small_ax = style_axes([0, 60, 10], [0, 13, 2], x_length=4.8, y_length=4.0)
            small_ax.shift(np.array([origin_x, -2.15, 0]) - small_ax.c2p(0, 0))
            incidence_graphs.add(fixed(VGroup(
                small_ax,
                Line(small_ax.c2p(0, 12), small_ax.c2p(60, 0), color=DEMAND, stroke_width=3),
                Line(small_ax.c2p(0, 2), small_ax.c2p(60, 5), color=SUPPLY, stroke_width=3),
                VGroup(Tex('D / MB', color=INK).scale(0.65).next_to(small_ax.c2p(1, 11.8), UR, buff=0.12),
                       Tex('S / MC', color=INK).scale(0.65).next_to(small_ax.c2p(60, 5), UP, buff=0.10, aligned_edge=RIGHT)),
                VGroup(Tex('$2$', color=SUPPLY).scale(0.65).next_to(small_ax.c2p(0, 2), LEFT, buff=0.15),
                       Tex('$12$', color=DEMAND).scale(0.65).next_to(small_ax.c2p(0, 12), LEFT, buff=0.15)),
                VGroup(DashedLine(small_ax.c2p(0, MARKET_P), small_ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
                       DashedLine(small_ax.c2p(MARKET_Q, 0), small_ax.c2p(MARKET_Q, MARKET_P), color=MUTED, stroke_width=2),
                       Dot(small_ax.c2p(MARKET_Q, MARKET_P), radius=0.06, color=MUTED)).set_z_index(1.5),
                VGroup(Line(small_ax.c2p(TAX_Q, SELLER_PRICE), small_ax.c2p(TAX_Q, BUYER_PRICE), color=GOV, stroke_width=6),
                       Line(small_ax.c2p(TAX_Q, SELLER_PRICE) + LEFT * 0.09, small_ax.c2p(TAX_Q, SELLER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
                       Line(small_ax.c2p(TAX_Q, BUYER_PRICE) + LEFT * 0.09, small_ax.c2p(TAX_Q, BUYER_PRICE) + RIGHT * 0.09, color=GOV, stroke_width=3),
                       Dot(small_ax.c2p(TAX_Q, BUYER_PRICE), radius=0.07, color=GUIDE),
                       Dot(small_ax.c2p(TAX_Q, SELLER_PRICE), radius=0.07, color=GUIDE),
                       DashedLine(small_ax.c2p(0, BUYER_PRICE), small_ax.c2p(TAX_Q, BUYER_PRICE), color=GUIDE, stroke_width=2),
                       DashedLine(small_ax.c2p(0, SELLER_PRICE), small_ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2),
                       DashedLine(small_ax.c2p(TAX_Q, 0), small_ax.c2p(TAX_Q, SELLER_PRICE), color=GUIDE, stroke_width=2)).set_z_index(2),
                # Keep the label left of the wedge; its background clears the grey price reference behind it.
                Tex(r'\$2 tax', color=GOV).scale(0.6).add_background_rectangle(color=BG, opacity=1, buff=0.04)
                    .next_to(small_ax.c2p(TAX_Q, (BUYER_PRICE + SELLER_PRICE) / 2), LEFT, buff=0.18).set_z_index(3),
                VGroup(Tex('$P_b=$', color=GUIDE).scale(0.6), DecimalNumber(BUYER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.6))
                    .arrange(RIGHT, buff=0.06).next_to(small_ax.c2p(0, BUYER_PRICE), LEFT, buff=0.2),
                VGroup(Tex('$P_s=$', color=GUIDE).scale(0.6), DecimalNumber(SELLER_PRICE, num_decimal_places=2, color=GUIDE).scale(0.6))
                    .arrange(RIGHT, buff=0.06).next_to(small_ax.c2p(0, SELLER_PRICE), LEFT, buff=0.2),
                VGroup(Tex('$Q^{tax}=$', color=GUIDE).scale(0.6), DecimalNumber(TAX_Q, num_decimal_places=0, color=GUIDE).scale(0.6))
                    .arrange(RIGHT, buff=0.06).next_to(small_ax.c2p(TAX_Q, 0), DOWN, buff=0.2),
                Line(small_ax.c2p(STACK_Q, 4), small_ax.c2p(STACK_Q, BUYER_PRICE), color=DEMAND, stroke_width=7),
                Line(small_ax.c2p(STACK_Q, SELLER_PRICE), small_ax.c2p(STACK_Q, 4), color=SUPPLY, stroke_width=7),
                DecimalNumber(BUYER_PRICE - 4, num_decimal_places=2, color=DEMAND).scale(0.62)
                    .next_to(small_ax.c2p(STACK_Q, (4 + BUYER_PRICE) / 2), LEFT, buff=0.15),
                DecimalNumber(4 - SELLER_PRICE, num_decimal_places=2, color=SUPPLY).scale(0.62)
                    .next_to(small_ax.c2p(STACK_Q, (4 + SELLER_PRICE) / 2), LEFT, buff=0.15))))
        left_graph, right_graph = incidence_graphs
        (right_ax, right_demand, right_supply, right_words, right_intercepts, right_reference, right_wedge, right_tax_word,
         right_buyer_readout, right_seller_readout, right_quantity_readout,
         right_buyer_share, right_seller_share, right_buyer_number, right_seller_number) = right_graph
        # The right graph's intercepts leave on their own in 8.b, so they ride outside the group.
        right_graph.remove(right_intercepts)
        # The right graph follows its own two slope trackers; the $2 tax is the same tracker section 7 settled at 2.
        right_d, right_s = ValueTracker(0.2), ValueTracker(0.05)
        for m in [right_demand, right_supply, *right_words, *right_wedge, right_tax_word, right_buyer_readout,
                  right_seller_readout, right_quantity_readout, right_buyer_share, right_seller_share,
                  right_buyer_number, right_seller_number]:
            m.axes, m.tax, m.d, m.s = right_ax, tax, right_d, right_s
        right_demand.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(0, 4 + 40 * m.d.get_value()),
            m.axes.c2p(min(60, 40 + 4 / m.d.get_value()), max(0, 4 - 20 * m.d.get_value()))))
        right_supply.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(max(0, 40 - 4 / m.s.get_value()), max(0, 4 - 40 * m.s.get_value())),
            m.axes.c2p(60, 4 + 20 * m.s.get_value())))
        right_words[0].add_updater(lambda m: m.next_to(m.axes.c2p(1, 4 + 39 * m.d.get_value()), UR, buff=0.12))
        right_words[1].add_updater(lambda m: m.next_to(m.axes.c2p(60, 4 + 20 * m.s.get_value()), UP, buff=0.10, aligned_edge=RIGHT))
        right_wedge[0].add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(state(m)[0], state(m)[2]), m.axes.c2p(state(m)[0], state(m)[1]) + UP * 1e-6))
        right_wedge[1].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[2])))
        right_wedge[2].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[1])))
        right_wedge[3].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[1])))
        right_wedge[4].add_updater(lambda m: m.move_to(m.axes.c2p(state(m)[0], state(m)[2])))
        right_wedge[5].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[1]),
            m.axes.c2p(state(m)[0], state(m)[1]) + RIGHT * 1e-6, color=GUIDE, stroke_width=2))))
        right_wedge[6].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(0, state(m)[2]),
            m.axes.c2p(state(m)[0], state(m)[2]) + RIGHT * 1e-6, color=GUIDE, stroke_width=2))))
        right_wedge[7].add_updater(lambda m: fixed(m.become(DashedLine(m.axes.c2p(state(m)[0], 0),
            m.axes.c2p(state(m)[0], state(m)[2]) + UP * 1e-6, color=GUIDE, stroke_width=2))))
        right_tax_word.add_updater(lambda m: m.next_to(
            m.axes.c2p(state(m)[0], (state(m)[1] + state(m)[2]) / 2), LEFT, buff=0.18))
        right_buyer_readout.add_updater(lambda m: (m[1].set_value(state(m)[1]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[1]), LEFT, buff=0.2)))
        right_seller_readout.add_updater(lambda m: (m[1].set_value(state(m)[2]), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(0, state(m)[2]), LEFT, buff=0.2)))
        right_quantity_readout.add_updater(lambda m: (m[1].set_value(round(state(m)[0], 4)), fixed(m), m.arrange(RIGHT, buff=0.06),
            m.next_to(m.axes.c2p(state(m)[0], 0), DOWN, buff=0.2)))
        right_buyer_share.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(STACK_Q, 4), m.axes.c2p(STACK_Q, state(m)[1]) + UP * 1e-6))
        right_seller_share.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(STACK_Q, state(m)[2]), m.axes.c2p(STACK_Q, 4) + UP * 1e-6))
        right_buyer_number.add_updater(lambda m: fixed(m.set_value(state(m)[1] - 4))
            .next_to(m.axes.c2p(STACK_Q, (4 + state(m)[1]) / 2), LEFT, buff=0.15))
        right_seller_number.add_updater(lambda m: fixed(m.set_value(4 - state(m)[2]))
            .next_to(m.axes.c2p(STACK_Q, (4 + state(m)[2]) / 2), LEFT, buff=0.15))
        incidence_note = fixed(Tex(r'Buyers pay \$1.60 more; sellers receive \$0.40 less.', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(context), FadeOut(market),
                  FadeOut(cost_region), FadeOut(ps_region), FadeOut(tax_region), FadeOut(cs_region), FadeOut(dwl_region),
                  FadeOut(wedge), FadeOut(wedge_word), FadeOut(buyer_price_readout), FadeOut(seller_price_readout),
                  FadeOut(quantity_readout), FadeOut(cs_label), FadeOut(ps_label), FadeOut(tax_label), FadeOut(dwl_label),
                  FadeIn(left_graph), FadeIn(right_graph), FadeIn(right_intercepts))
        self.play(FadeIn(incidence_note))
        self.pause('8.a')

        # ---- 8.b · Flatter demand on the right: a grey ghost keeps the old curve while demand turns about (40, 4).
        demand_question = fixed(Tex('What if buyers are more responsive to price?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        demand_ghost = fixed(DashedLine(right_ax.c2p(0, 12), right_ax.c2p(60, 0), color=MUTED, stroke_width=2)).set_z_index(-1)
        self.remove(incidence_note)
        self.play(FadeIn(demand_question), FadeOut(right_intercepts), FadeIn(demand_ghost))
        self.play(right_d.animate.set_value(0.05), run_time=2.4, rate_func=smooth)
        demand_note = fixed(Tex('Buyers more responsive to price bear less of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(demand_question)
        self.play(FadeIn(demand_note))
        self.pause('8.b')

        # Return to the original market before changing the other side.
        self.remove(demand_note)
        reset_note = fixed(Tex('Back to the original market.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(reset_note), right_d.animate.set_value(0.2), run_time=2.4, rate_func=smooth)
        self.play(FadeOut(demand_ghost), FadeIn(right_intercepts))
        self.pause('8.b.reset')

        # ---- 8.c · Flatter supply on the right, with demand back at its original slope.
        supply_question = fixed(Tex('What if sellers are more responsive to price?', color=DEFINITION)
                                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        supply_ghost = fixed(DashedLine(right_ax.c2p(0, 2), right_ax.c2p(60, 5), color=MUTED, stroke_width=2)).set_z_index(-1)
        self.remove(reset_note)
        self.play(FadeOut(right_intercepts), FadeIn(supply_question), FadeIn(supply_ghost))
        self.play(right_s.animate.set_value(1 / 45), run_time=2.4, rate_func=smooth)
        supply_note = fixed(Tex('Sellers more responsive to price bear less of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(supply_question)
        self.play(FadeIn(supply_note))
        self.pause('8.c')

        # ---- 8.d · The general rule, with the two graphs as its evidence.
        burden_note = fixed(Tex('The side less responsive to price bears more of the tax.', color=DEFINITION)
                            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(supply_note)
        self.play(FadeOut(supply_ghost), FadeIn(burden_note))
        self.pause('8.d')

        # ---- 9.a · A per-unit subsidy: the wedge reverses and slides in from the right.
        self.remove(head, context, burden_note)
        head = fixed(title('A Per-Unit Subsidy'))
        context = fixed(subtitle(head, r'The government pays \$2 on each unit exchanged.'))
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
        subsidy_note = fixed(Tex('Slide the subsidy in from the right until it gets stuck.', color=DEFINITION)
                             .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        # The right graph's numbers are current: freeze them, then both graphs leave as the full market returns.
        for m in [right_buyer_readout, right_seller_readout, right_quantity_readout, right_buyer_number, right_seller_number]:
            m.update()
        for m in [right_demand, right_supply, *right_words, *right_wedge, right_tax_word, right_buyer_readout,
                  right_seller_readout, right_quantity_readout, right_buyer_share, right_seller_share,
                  right_buyer_number, right_seller_number]:
            m.clear_updaters()
        self.play(FadeIn(head), FadeIn(context), FadeIn(subsidy_note),
                  FadeOut(left_graph), FadeOut(right_graph), FadeIn(market))
        self.play(FadeIn(subsidy_wedge), FadeIn(subsidy_word))
        self.play(subsidy_slide.animate.set_value(SUBSIDY_Q), run_time=2.6, rate_func=smooth)
        self.pause('9.a')

        # ---- 9.b · Stuck at 48 units: sellers' price above buyers' price; invisible slices locate later close-ups.
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
            Tex(r'$Q^{subsidy}=48$', color=GUIDE).scale(0.7).next_to(ax.c2p(SUBSIDY_Q, 0), DOWN, buff=0.20)))
        subsidy_marks.set_z_index(2)
        subsidy_wedge.set_z_index(2)
        added_lots = fixed(VGroup())
        for q in range(MARKET_Q, SUBSIDY_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            added_lots.add(fixed(VGroup(
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=0))))
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
        subsidy_solve_line = fixed(VGroup(Tex('$Q^{tax}$', color=GUIDE), Tex('$=$', color=INK), Tex('$48$', color=GUIDE))
            .arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_seller_line = fixed(VGroup(Tex('$P_s$', color=GUIDE), Tex('$=$', color=INK), Tex('$2 + 48/20$', color=SUPPLY),
            Tex('$=$', color=INK), Tex('$4.40$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_buyer_line = fixed(VGroup(Tex('$P_b$', color=GUIDE), Tex('$=$', color=INK), Tex('$12 - 48/5$', color=DEMAND),
            Tex('$=$', color=INK), Tex('$2.40$', color=GUIDE)).arrange(RIGHT, buff=0.14).scale(0.78))
        subsidy_step_one = fixed(Tex(narration('Step 1: find the quantity'), color=CAPTION).scale(0.6))
        subsidy_step_two = fixed(Tex(narration('Step 2: find the prices'), color=CAPTION).scale(0.6))
        for line in (subsidy_wedge_line, subsidy_substitute_line, subsidy_simplify_line, subsidy_solve_line,
            subsidy_seller_line, subsidy_buyer_line):
            line.scale(0.72 / 0.78)
        subsidy_algebra = fixed(VGroup(subsidy_step_one, subsidy_wedge_line, subsidy_substitute_line, subsidy_simplify_line, subsidy_solve_line,
            subsidy_step_two, subsidy_seller_line, subsidy_buyer_line)
            .arrange(DOWN, buff=0.24).move_to([5.2, 0.05, 0]))
        subsidy_step_two.shift(DOWN * 0.08)
        self.play(FadeIn(subsidy_divider), FadeIn(subsidy_step_one), FadeIn(subsidy_wedge_line), FadeIn(subsidy_solve_note))
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
        self.play(FadeIn(subsidy_step_two), FadeIn(subsidy_seller_line), FadeIn(subsidy_price_note))
        self.play(FadeIn(subsidy_buyer_line))
        self.pause('9.b.prices')
        self.play(FadeOut(subsidy_algebra), FadeOut(subsidy_divider), FadeOut(subsidy_price_note), run_time=0.5)
        self.play(subsidy_block.animate.shift(RIGHT * 1.0).scale(1 / 0.72, about_point=ax.c2p(0, 0) + RIGHT * 1.0), run_time=1.1)
        self.remove(subsidy_block)
        self.add(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots)

        # ---- 9.c · The government pays the gap on every one of the 48 units.
        subsidy_bars = fixed(VGroup())
        for q in range(SUBSIDY_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            subsidy_bars.add(fixed(Polygon(
                ax.c2p(left, SUBSIDY_BUYER), ax.c2p(right, SUBSIDY_BUYER),
                ax.c2p(right, SUBSIDY_SELLER), ax.c2p(left, SUBSIDY_SELLER),
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY)))
        subsidy_cost_word = fixed(Tex('Subsidy cost', color=INK).scale(0.72).move_to(ax.c2p(16, 3.8)))
        subsidy_cost = fixed(VGroup(subsidy_bars, subsidy_cost_word))
        cost_note = fixed(Tex(r'Government cost: \$2 $\times$ 48 units $=$ \$96.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(LaggedStart(*[FadeIn(bar) for bar in subsidy_bars], lag_ratio=0.025),
                  FadeIn(subsidy_cost_word), FadeIn(cost_note), run_time=1.6)
        self.remove(*list(subsidy_bars), subsidy_cost_word)
        self.add(subsidy_cost)
        self.pause('9.c')

        # ---- 9.d.select · The 44th unit, exchanged only because of the subsidy.
        added_lot = added_lots[ADDED_TON - MARKET_Q]
        added_pair = fixed(VGroup(*list(added_lot)))
        added_lot.remove(*list(added_pair))
        added_home = added_pair.copy()
        self.add(added_pair)
        added_selection = fixed(SurroundingRectangle(added_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(cost_note)
        self.play(FadeIn(added_selection))
        self.pause('9.d.select')

        # ---- 9.d.values · C1's 44th unit: MB below MC, with C1's two questions.
        added_target = fixed(VGroup())
        for bar_left, value, color in [(BUYER_LEFT, 3.2, DEMAND), (SELLER_LEFT, 4.2, SUPPLY)]:
            added_target.add(fixed(Polygon([bar_left, detail_y(0), 0], [bar_left + BAR_WIDTH, detail_y(0), 0],
                [bar_left + BAR_WIDTH, detail_y(value), 0], [bar_left, detail_y(value), 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        subsidy_market = fixed(VGroup(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_cost))
        self.remove(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots, subsidy_cost)
        self.add(subsidy_market)
        self.play(FadeOut(subsidy_market), FadeOut(added_selection), FadeOut(context), Transform(added_pair, added_target), run_time=1.6)
        context = fixed(subtitle(head, 'The 44th unit: exchanged only with the subsidy.'))
        added_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(added_target, [DEMAND, SUPPLY])],
            Line([-1.9, detail_y(0), 0], [1.9, detail_y(0), 0], color=MUTED)))
        # Compact labels: both names below their edges, clear of the price lines; MC will sit inside the grey bar.
        added_values = fixed(VGroup(
            Tex(r'$\$3.20$', color=DEMAND).scale(0.72).next_to([BUYER_LEFT, detail_y(3.2), 0], LEFT, buff=0.25),
            Tex('MB', color=DEMAND).scale(0.58).next_to([-1.21, detail_y(3.2), 0], DOWN, buff=0.10),
            Tex(r'$\$4.20$', color=SUPPLY).scale(0.72).next_to([SELLER_LEFT + BAR_WIDTH, detail_y(4.2), 0], RIGHT, buff=0.25),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([1.21, detail_y(4.2), 0], DOWN, buff=0.10))).set_z_index(3)
        added_questions = fixed(VGroup(
            Tex('Will the buyer buy?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])))
        self.add(people, government)
        self.play(FadeIn(added_edges), FadeIn(added_values), FadeIn(context), run_time=0.4)
        self.play(FadeIn(added_questions[0]), FadeIn(added_questions[1]))
        self.pause('9.d.values')

        # ---- 9.d.private.compare · The subsidy's two prices around the unit, then each side against its own price.
        added_prices = fixed(VGroup(
            Line([-2.6, detail_y(SUBSIDY_BUYER), 0], [1.9, detail_y(SUBSIDY_BUYER), 0], color=GUIDE, stroke_width=2),
            Line([-2.6, detail_y(SUBSIDY_SELLER), 0], [1.9, detail_y(SUBSIDY_SELLER), 0], color=GUIDE, stroke_width=2))).set_z_index(2)
        # P_b sits under its line, clear of the MB number just above: both names sit outside the pair of lines, as in 6.c.
        added_price_words = fixed(VGroup(
            Tex(r'$P_b$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(SUBSIDY_BUYER), 0], DOWN, buff=0.06),
            Tex(r'$\$2.40$', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(SUBSIDY_BUYER), 0], LEFT, buff=0.15),
            Tex(r'$P_s$', color=GUIDE).scale(0.58).next_to([-2.25, detail_y(SUBSIDY_SELLER), 0], UP, buff=0.06),
            Tex(r'$\$4.40$', color=GUIDE).scale(0.72).next_to([-2.6, detail_y(SUBSIDY_SELLER), 0], LEFT, buff=0.15))).set_z_index(3)
        # The subsidy: the narrow middle bar between the two prices, top on P_s and bottom on P_b. Read left to right,
        # the buyer pays P_b, the subsidy is the step up in the middle, and the seller receives P_s. SURPLUS_OPACITY, as in welfare.
        added_subsidy = fixed(VGroup(
            Polygon([TAX_LEFT, detail_y(SUBSIDY_BUYER), 0], [TAX_LEFT + TAX_WIDTH, detail_y(SUBSIDY_BUYER), 0],
                [TAX_LEFT + TAX_WIDTH, detail_y(SUBSIDY_SELLER), 0], [TAX_LEFT, detail_y(SUBSIDY_SELLER), 0],
                stroke_width=0, fill_color=GOV, fill_opacity=SURPLUS_OPACITY),
            Tex('subsidy', color=INK).scale(0.55))).set_z_index(1)
        added_subsidy[1].move_to(added_subsidy[0]).set_z_index(3)
        # Buyer pair: MB against P_b. Seller pair: MC projected leftward across the gap and the buyer column against P_s,
        # in segments that skip the subsidy bar (0.12 clear on either side) and the P_s number, which sits at nearly the same height.
        added_private_guides = fixed(VGroup(
            DashedLine(added_values[0].get_left() + LEFT * 0.12, [-4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[1].get_left() + LEFT * 0.12, [-4.25, detail_y(SUBSIDY_BUYER), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(SUBSIDY_BUYER), 0], [-4.25, detail_y(3.2), 0], color=DEMAND, stroke_width=3),
            DashedLine([SELLER_LEFT, detail_y(4.2), 0], [TAX_LEFT + TAX_WIDTH + 0.12, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([TAX_LEFT - 0.12, detail_y(4.2), 0], [added_price_words[3].get_right()[0] + 0.12, detail_y(4.2), 0],
                       color=TOTAL, stroke_width=1.4),
            DashedLine([added_price_words[3].get_left()[0] - 0.12, detail_y(4.2), 0], [-4.25, detail_y(4.2), 0],
                       color=TOTAL, stroke_width=1.4),
            DashedLine(added_price_words[3].get_left() + LEFT * 0.12, [-4.25, detail_y(SUBSIDY_SELLER), 0], color=TOTAL, stroke_width=1.4),
            Line([-4.25, detail_y(4.2), 0], [-4.25, detail_y(SUBSIDY_SELLER), 0], color=SUPPLY, stroke_width=3)))
        # The market's answer: one green check, centered in the gap between the two brackets.
        added_private_answer = fixed(VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)
            .next_to([-4.25, detail_y((3.2 + 4.2) / 2), 0], LEFT, buff=0.3))
        self.play(FadeIn(added_prices), FadeIn(added_price_words), FadeIn(added_subsidy))
        # Read the buyer's decision first, then the seller's, with a separate question and pause.
        added_buyer_guides = fixed(VGroup(*list(added_private_guides)[:3]))
        added_seller_guides = fixed(VGroup(*list(added_private_guides)[3:]))
        self.play(FadeIn(added_buyer_guides))
        self.pause('9.d.private.buyer')
        added_seller_question = fixed(Tex('Will the seller sell?', color=DEFINITION)
            .scale(0.60).move_to([-4.8, -3.05, 0]))
        self.play(FadeOut(added_questions[0]), FadeIn(added_seller_question), FadeIn(added_seller_guides))
        added_questions = fixed(VGroup(added_seller_question, added_questions[1]))
        self.remove(added_buyer_guides, added_seller_guides)
        self.add(added_private_guides)
        self.pause('9.d.private.compare')

        # ---- 9.d.private · Both sides will: exchanged.
        added_exchange_question = fixed(Tex('Will they exchange?', color=DEFINITION)
            .scale(0.60).move_to([-4.8, -3.05, 0]))
        self.play(FadeOut(added_questions[0]), FadeIn(added_exchange_question), FadeIn(added_private_answer))
        added_questions = fixed(VGroup(added_exchange_question, added_questions[1]))
        self.pause('9.d.private')

        # ---- 9.d.social.compare · The subsidy bar's job is done; society compares MB with MC, as in C1.
        # MB crosses the empty gap, then runs from the seller column's right edge to the bracket.
        added_social_guides = fixed(VGroup(
            DashedLine([BUYER_LEFT + BAR_WIDTH, detail_y(3.2), 0], [SELLER_LEFT, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([SELLER_LEFT + BAR_WIDTH, detail_y(3.2), 0], [4.25, detail_y(3.2), 0], color=TOTAL, stroke_width=1.4),
            DashedLine(added_values[2].get_right() + RIGHT * 0.12, [4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=1.4),
            Line([4.25, detail_y(3.2), 0], [4.25, detail_y(4.2), 0], color=TOTAL, stroke_width=3)))
        # Society's answer: a red cross over the DWL label.
        added_social_answer = fixed(VGroup(VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5), Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)), Tex('DWL', color=INK)).arrange(DOWN, buff=0.16).scale(0.70)
            .next_to([4.25, detail_y((3.2 + 4.2) / 2), 0], RIGHT, buff=0.3))
        self.play(FadeOut(added_subsidy), FadeIn(added_social_guides))
        self.pause('9.d.social.compare')

        # ---- 9.d.loss · No for society: the cost above the unit's value is deadweight loss.
        added_dwl_bar = fixed(Polygon([SELLER_LEFT, detail_y(3.2), 0], [SELLER_LEFT + BAR_WIDTH, detail_y(3.2), 0],
            [SELLER_LEFT + BAR_WIDTH, detail_y(4.2), 0], [SELLER_LEFT, detail_y(4.2), 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        added_note = fixed(Tex(r'The subsidy adds this trade, creating \$1 of deadweight loss.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(added_dwl_bar), FadeIn(added_social_answer), FadeIn(added_note), run_time=0.5)
        self.pause('9.d.loss')

        # ---- 9.d.return · The unit and its loss carry back to the 44th slice.
        left, right = ADDED_TON + BAR_GAP / 2, ADDED_TON + 1 - BAR_GAP / 2
        added_dwl_market = fixed(Polygon(ax.c2p(left, 12 - left / 5), ax.c2p(right, 12 - right / 5),
            ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        self.remove(people, government)
        self.play(FadeOut(added_edges), FadeOut(added_values), FadeOut(added_questions), FadeOut(added_prices), FadeOut(added_price_words),
                  FadeOut(added_private_guides), FadeOut(added_private_answer),
                  FadeOut(added_social_guides), FadeOut(added_social_answer), FadeOut(added_note), FadeOut(context), run_time=0.4)
        context = fixed(subtitle(head, r'The government pays \$2 on each unit exchanged.'))
        # The subsidy bars have explained spending; keep the returning DWL view clear.
        subsidy_market.remove(subsidy_cost)
        self.play(Transform(added_pair, added_home), Transform(added_dwl_bar, added_dwl_market),
                  FadeIn(subsidy_market), FadeIn(context), run_time=1.6)
        # The 44th lot rejoins its group so its faint cost bar stays with the other seven.
        self.remove(added_pair)
        added_lot.add(*list(added_home))
        self.pause('9.d.return')

        # ---- 9.e · The other seven added units.
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
        subsidy_loss_note = fixed(Tex('Deadweight loss: the added units cost more than they are worth.', color=DEFINITION)
                                  .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(LaggedStart(*[FadeIn(bar) for bar in subsidy_losses if bar is not added_dwl_bar], lag_ratio=0.18), run_time=1.6)
        self.remove(*[bar for bar in subsidy_losses])
        self.add(subsidy_losses)
        self.play(FadeIn(subsidy_dwl_word), FadeIn(subsidy_loss_note))
        self.pause('9.e')

        # ---- 10.a · Next time: the $2 tax lands on C1's efficient quantity.
        self.remove(head, context, subsidy_loss_note)
        head = fixed(title('Next Time'))
        context = fixed(subtitle(head, r'Last time, a \$2 external cost made 32 units the efficient quantity.'))
        self.remove(subsidy_market)
        self.add(market, subsidy_wedge, subsidy_word, subsidy_marks, added_lots)
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
            Tex(r'$Q^{tax}=32$', color=GUIDE).scale(0.7).next_to(ax.c2p(TAX_Q, 0), DOWN, buff=0.20)))
        closing_wedge.set_z_index(2)
        next_note = fixed(Tex('Next time: can a tax correct an externality?', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(context), FadeOut(subsidy_wedge), FadeOut(subsidy_word), FadeOut(subsidy_marks),
                  FadeOut(added_lots), FadeOut(subsidy_losses), FadeOut(subsidy_dwl_word),
                  intercepts[0].animate.set_opacity(1),
                  *[bar.animate.set_fill(opacity=0) for bar in list(costs)[TAX_Q:]])
        self.play(FadeIn(closing_wedge), FadeIn(next_note))
        self.pause('10.a')
