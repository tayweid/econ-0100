# maniml C1_Animations.py C1
# Storyboard: C1_Notes.typ. All lesson choreography stays in construct().
# Part B's continuous market shape, with Q in tons and values in dollars per ton.
# Each comparison selects one one-ton exchange; its marginal values come from its quantity rank.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects


class C1(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        MARKET_Q, MARKET_P, EXTERNAL_COST, EFFICIENT_Q = 40, 4, 2, 32
        COMPARE_LOW, COMPARE_HIGH = 35, 48  # Select ton 36 when reducing, ton 48 when increasing.
        BAR_GAP = 0.08
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.68

        BASE_OPACITY, SURPLUS_OPACITY = 0.16, 0.65
        GRAPH_EXT_OPACITY = 0.8

        # Prepare the first lot and the exact marginal boundary on a common scale.
        head = fixed(title('Competitive Equilibrium'))
        INTRO_BASE, INTRO_SCALE, INTRO_WIDTH = -2.0, 0.34, 1.15
        # Opaque spheres enter directly; transparency exposes their rear surface.
        intro_people = fixed(Group())
        for x, color in [(-0.725, DEMAND), (0.725, SUPPLY)]:
            intro_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0,
                fill_color=color, fill_opacity=0.28).move_to([x, -2.63, 0])))
            intro_people.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, -2.4, 0])).apply_depth_test())
        intro_states, intro_value_states = [], []
        for q, mb, mc, message in [
            (0, 12, 2, 'First exchange: both the buyer and seller gain.'),
            (40, 4, 4, r'At equilibrium, MB $=$ MC $=\$4$.')]:
            next_pair = fixed(VGroup())
            for left, value, color, lower, upper in [
                (-1.3, mb, DEMAND, MARKET_P, mb),
                (0.15, mc, SUPPLY, mc, MARKET_P)]:
                # Faint base and strong surplus share a hue; the hard edge is MB/MC.
                next_pair.add(fixed(Polygon(
                    [left, INTRO_BASE, 0], [left + INTRO_WIDTH, INTRO_BASE, 0],
                    [left + INTRO_WIDTH, INTRO_BASE + lower * INTRO_SCALE, 0],
                    [left, INTRO_BASE + lower * INTRO_SCALE, 0],
                    stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
                next_pair.add(fixed(Polygon(
                    [left, INTRO_BASE + lower * INTRO_SCALE, 0],
                    [left + INTRO_WIDTH, INTRO_BASE + lower * INTRO_SCALE, 0],
                    [left + INTRO_WIDTH, INTRO_BASE + upper * INTRO_SCALE, 0],
                    [left, INTRO_BASE + upper * INTRO_SCALE, 0],
                    stroke_width=0, fill_color=color, fill_opacity=SURPLUS_OPACITY if upper > lower else 0)))
                next_pair.add(fixed(Line(
                    [left, INTRO_BASE + value * INTRO_SCALE, 0],
                    [left + INTRO_WIDTH, INTRO_BASE + value * INTRO_SCALE, 0],
                    color=color, stroke_width=3)))
            next_pair.add(fixed(Line([-1.45, INTRO_BASE, 0], [1.45, INTRO_BASE, 0], color=MUTED)))
            next_pair.add(fixed(Line([-1.45, INTRO_BASE + 4 * INTRO_SCALE, 0],
                [1.45, INTRO_BASE + 4 * INTRO_SCALE, 0], color=GUIDE, stroke_width=2)))
            intro_words = fixed(VGroup(
                Tex(rf'MB $\${mb:g}$', color=DEMAND).scale(0.7)
                    .next_to(next_pair[2], LEFT, buff=0.22),
                Tex(rf'MC $\${mc:g}$', color=SUPPLY).scale(0.7)
                    .next_to(next_pair[5], RIGHT, buff=0.22),
                Tex(r'Price $\$4$', color=GUIDE).scale(0.7).move_to(
                    [-3.0, INTRO_BASE + 4 * INTRO_SCALE, 0] if q == 0 else [0, INTRO_BASE + 4 * INTRO_SCALE + 0.35, 0]),
                Tex(rf'CS $\${mb - 4:g}$', color=DEMAND).scale(0.7)
                    .next_to(next_pair[1], LEFT, buff=0.22),
                Tex(rf'PS $\${4 - mc:g}$', color=SUPPLY).scale(0.7)
                    .next_to(next_pair[4], RIGHT, buff=0.22),
                Tex('Buyer', color=INK).scale(0.7).move_to([-0.725, -2.95, 0]),
                Tex('Seller', color=INK).scale(0.7).move_to([0.725, -2.95, 0])))
            intro_message = fixed(Tex(message, color=DEFINITION)
                .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
            # No surplus area or surplus labels at the exact MB=MC boundary.
            if q == MARKET_Q:
                intro_words.remove(*list(intro_words)[3:5])
            intro_states.append((next_pair, intro_words, intro_message))
            values_pair = next_pair.copy()
            for index, left, value, color in [(0, -1.3, mb, DEMAND), (3, 0.15, mc, SUPPLY)]:
                values_pair[index].become(fixed(Polygon(
                    [left, INTRO_BASE, 0], [left + INTRO_WIDTH, INTRO_BASE, 0],
                    [left + INTRO_WIDTH, INTRO_BASE + value * INTRO_SCALE, 0],
                    [left, INTRO_BASE + value * INTRO_SCALE, 0],
                    stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
                values_pair[index + 1].set_opacity(0)
            values_pair[-1].set_opacity(0)  # Values first, then the established market price.
            value_words = fixed(VGroup(*[intro_words[i] for i in [0, 1]],
                *list(intro_words)[-2:]))
            intro_value_states.append((values_pair, value_words))

        # ---- 1.a · Start with the full market and its surplus regions.
        ax = style_axes([0, 60, 10], [0, 13, 2], x_length=10, y_length=4.6)
        ax.shift(np.array([-5, BODY_MID - 2.15, 0]) - ax.c2p(0, 0))
        fixed(ax)
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), UP, buff=0.18),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73),
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
            Tex(r'$P^*=4$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 4), LEFT, buff=0.2)))
        quantity_guide = fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2))
        quantity_label = fixed(Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20))
        cs, ps, costs = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
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
        # Place each short label at the centroid of its own surplus triangle.
        surplus_words = fixed(VGroup(
            Tex('CS', color=INK).scale(0.72).move_to(ax.c2p(MARKET_Q / 3, (12 + 2 * MARKET_P) / 3)),
            Tex('PS', color=INK).scale(0.72).move_to(ax.c2p(MARKET_Q / 3, (2 + 2 * MARKET_P) / 3))))
        self.play(FadeIn(head), FadeIn(costs), FadeIn(ax), FadeIn(axis_words), FadeIn(demand), FadeIn(supply),
                  FadeIn(curve_words), FadeIn(equilibrium), FadeIn(quantity_guide), FadeIn(quantity_label))
        self.play(FadeIn(ps), FadeIn(surplus_words[1]))
        self.play(FadeIn(cs), FadeIn(surplus_words[0]))
        market = fixed(VGroup(ax, axis_words, costs, cs, ps, demand, supply, curve_words,
                             equilibrium, quantity_guide, quantity_label, surplus_words))
        self.remove(*[m for m in self.mobjects if m is not head])
        self.add(market, head)
        self.pause('1.a')

        # Market pieces share one quantity slice; only the close-up separates them.
        # At Q=40 both values converge on the exact equilibrium point.
        intro_homes = []
        for q in [0, MARKET_Q]:
            left, right = (BAR_GAP / 2, 1 - BAR_GAP / 2) if q == 0 else (q - 0.0001, q + 0.0001)
            mb_left, mb_right = (12 - left / 5, 12 - right / 5) if q == 0 else (4, 4)
            mc_left, mc_right = (2 + left / 20, 2 + right / 20) if q == 0 else (4, 4)
            home_pair = fixed(VGroup(
                # Expenditure disappears as the buyer and seller columns merge.
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 4), ax.c2p(left, 4),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                Polygon(ax.c2p(left, 4), ax.c2p(right, 4),
                    ax.c2p(right, mb_right), ax.c2p(left, mb_left),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY if q == 0 else 0),
                Line(ax.c2p(left, mb_left), ax.c2p(right, mb_right), color=DEMAND, stroke_width=3),
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                    ax.c2p(right, mc_right), ax.c2p(left, mc_left),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
                Polygon(ax.c2p(left, mc_left), ax.c2p(right, mc_right),
                    ax.c2p(right, 4), ax.c2p(left, 4),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY if q == 0 else 0),
                Line(ax.c2p(left, mc_left), ax.c2p(right, mc_right), color=SUPPLY, stroke_width=3),
                Line(ax.c2p(left, 0), ax.c2p(right, 0), color=MUTED),
                Line(ax.c2p(left, 4), ax.c2p(right, 4), color=GUIDE, stroke_width=2)))
            intro_homes.append(home_pair)

        # ---- 1.a.first · Carry the first selected pair out of the market.
        intro_pair = intro_homes[0].copy()
        intro_words, intro_message = intro_states[0][1:]
        first_selection = fixed(SurroundingRectangle(intro_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(first_selection), FadeIn(intro_pair))
        self.pause('1.a.first.select')
        self.play(FadeOut(market), FadeOut(first_selection),
                  Transform(intro_pair, intro_value_states[0][0]), run_time=1.6)
        value_words = intro_value_states[0][1]
        # Bind visible values to the live bars, including during the return zoom.
        intro_words[0].bars = intro_words[1].bars = intro_pair
        intro_words[0].add_updater(lambda m:
            m.next_to(m.bars[2], LEFT, buff=0.22))
        intro_words[1].add_updater(lambda m:
            m.next_to(m.bars[5], RIGHT, buff=0.22))
        value_question = fixed(Tex('Is there a price that would make this exchange work?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(intro_people)
        self.play(FadeIn(value_words), FadeIn(value_question))
        self.pause('1.a.first.values')
        # Split the faint buyer fill at price without changing its appearance.
        intro_pair[0].become(intro_states[0][0][0])
        intro_pair[1].set_fill(opacity=BASE_OPACITY)
        self.play(intro_pair[-1].animate.set_opacity(1), FadeIn(intro_words[2]), FadeOut(value_question))
        surplus_labels = fixed(VGroup(intro_words[3], intro_words[4]))
        self.play(intro_pair[1].animate.set_fill(opacity=SURPLUS_OPACITY),
                  intro_pair[4].animate.set_fill(opacity=SURPLUS_OPACITY),
                  FadeIn(surplus_labels), FadeIn(intro_message))
        self.remove(value_words, intro_words[2], surplus_labels)
        self.add(intro_words)
        self.pause('1.a.first')

        # ---- 1.a.first.return · Restore the same pair to the same market location.
        self.remove(intro_people)
        self.play(FadeOut(intro_words, suspend_mobject_updating=False), FadeOut(intro_message),
                  Transform(intro_pair, intro_homes[0]), FadeIn(market), run_time=1.6)
        self.play(FadeOut(intro_pair))
        self.pause('1.a.first.return')

        # ---- 1.a.last · The exact marginal exchange at the intersection.
        intro_pair = intro_homes[1].copy()
        intro_words, intro_message = intro_states[1][1:]
        marginal_selection = fixed(SurroundingRectangle(
            VGroup(costs[-1], cs[-1], ps[-1]), color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(marginal_selection), FadeIn(intro_pair))
        self.pause('1.a.last.select')
        self.play(FadeOut(market), FadeOut(marginal_selection),
                  Transform(intro_pair, intro_value_states[1][0]), run_time=1.6)
        value_words = intro_value_states[1][1]
        # Bind visible values to the live bars, including during the return zoom.
        intro_words[0].bars = intro_words[1].bars = intro_pair
        intro_words[0].add_updater(lambda m:
            m.next_to(m.bars[2], LEFT, buff=0.22))
        intro_words[1].add_updater(lambda m:
            m.next_to(m.bars[5], RIGHT, buff=0.22))
        self.add(intro_people)
        self.play(FadeIn(value_words))
        self.pause('1.a.last.values')
        self.play(intro_pair[-1].animate.set_opacity(1), FadeIn(intro_words[2]))
        self.play(FadeIn(intro_message))
        self.remove(value_words, intro_words[2])
        self.add(intro_words)
        self.pause('1.a.last')

        # ---- 1.a.last.return · Full market again before asking about the next lot.
        self.remove(intro_people)
        self.play(FadeOut(intro_words, suspend_mobject_updating=False), FadeOut(intro_message),
                  Transform(intro_pair, intro_homes[1]), FadeIn(market), run_time=1.6)
        self.play(FadeOut(intro_pair))
        self.pause('1.a.last.return')

        # ---- 1.b · Add separate one-ton exchanges, then select ton 48.
        extra_lots = fixed(VGroup())
        for q in range(MARKET_Q, COMPARE_HIGH):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            extra_lots.add(fixed(VGroup(
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                    ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                    ax.c2p(right, 2 + right / 20), ax.c2p(left, 2 + left / 20),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY))))
        question = fixed(Tex('What happens if we increase quantity?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(question))
        self.play(LaggedStart(*[FadeIn(lot) for lot in extra_lots], lag_ratio=0.4),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(48, 0), ax.c2p(48, 4.4), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=48$', color=GUIDE).scale(0.7).next_to(ax.c2p(48, 0), DOWN, buff=0.20))),
                  run_time=2)
        self.pause('1.b')
        extra_pair = fixed(VGroup(*list(extra_lots[-1])))
        extra_lots[-1].remove(*list(extra_pair))
        extra_home = extra_pair.copy()
        self.add(extra_pair)
        selected_ton = fixed(SurroundingRectangle(extra_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(question)
        self.play(FadeIn(selected_ton))
        self.pause('1.b.select')

        # ---- 1.c · Carry the selected pair into B4's head-on bar comparison.
        extra_target = fixed(VGroup())
        for left, value, color in [(-1.16, 2.4, DEMAND), (0.06, 4.4, SUPPLY)]:
            extra_target.add(fixed(Polygon([left, DETAIL_BASE, 0], [left + 1.1, DETAIL_BASE, 0],
                [left + 1.1, DETAIL_BASE + value * DETAIL_SCALE, 0], [left, DETAIL_BASE + value * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(extra_lots), FadeOut(selected_ton),
                  Transform(extra_pair, extra_target), run_time=1.6, rate_func=smooth)
        detail_people = fixed(Group())
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            detail_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([x, DETAIL_BASE - 0.60, 0])))
            detail_people.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            detail_people.add(fixed(Tex('Buyer' if color == DEMAND else 'Seller', color=INK)
                .scale(0.65).move_to([x, DETAIL_BASE - 0.94, 0])))
        extra_detail = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(extra_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$2.40$', color=DEMAND).scale(0.72).next_to(extra_pair[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$4.40$', color=SUPPLY).scale(0.72).next_to(extra_pair[1].get_corner(UR), RIGHT, buff=0.25),
            DashedLine([-0.06, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0], color=DWL, stroke_width=1.6),
            DashedLine([3.25, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0], color=DWL, stroke_width=1.6),
            Line([3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0], [3.8, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0],
                color=DWL, stroke_width=3),
            VGroup(Tex(r'TS $=-\$2$', color=TOTAL), Tex(r'DWL $=\$2$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=LEFT).scale(0.8)
                .next_to([3.8, DETAIL_BASE + 3.4 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MC $>$ MB', color=INK).scale(0.8)))
        extra_detail[-1].next_to(extra_detail[-2], DOWN, buff=0.2)
        conclusion = fixed(Tex('Negative TS means deadweight loss: a reduction in total surplus.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('Can any price make this trade worthwhile?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        extra_detail[3].bars = extra_detail[4].bars = extra_pair
        extra_detail[3].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        extra_detail[4].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head,
            'The 48th unit: a quantity larger than in equilibrium.'))
        self.add(detail_people)
        self.play(FadeIn(extra_detail[:5]), FadeIn(value_question), FadeIn(unit_context))
        self.pause('1.c.values')
        self.play(FadeOut(value_question))
        self.play(FadeIn(extra_detail[5:]), FadeIn(conclusion))
        self.pause('1.c')

        # ---- 1.d · Return the exact same pair to its original quantity interval.
        self.remove(detail_people)
        self.play(FadeOut(extra_detail, suspend_mobject_updating=False), FadeOut(conclusion), FadeOut(unit_context),
                  Transform(extra_pair, extra_home), FadeIn(market), FadeIn(extra_lots), run_time=1.6)
        self.play(FadeOut(extra_pair), FadeOut(extra_lots),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20))))
        self.pause('1.d')

        # ---- 1.e · Reduce quantity, then pick one existing exchange: ton 36.
        removed_pair = fixed(VGroup(
            Polygon(*costs[COMPARE_LOW].get_vertices()[:2], *cs[COMPARE_LOW].get_vertices()[2:4],
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            costs[COMPARE_LOW].copy()))
        removed_home = removed_pair.copy()
        question = fixed(Tex('What happens if we decrease quantity?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(question))
        self.play(LaggedStart(*[VGroup(costs[q], cs[q], ps[q]).animate.set_opacity(0.05)
                               for q in range(MARKET_Q - 1, COMPARE_LOW - 1, -1)], lag_ratio=0.3),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(35, 0), ax.c2p(35, 5), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=35$', color=GUIDE).scale(0.7).next_to(ax.c2p(35, 0), DOWN, buff=0.20))),
                  run_time=2)
        self.pause('1.e')
        selected_ton = fixed(SurroundingRectangle(removed_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(question)
        self.play(FadeIn(removed_pair), FadeIn(selected_ton))
        self.pause('1.e.select')

        # ---- 1.f · The same bar-pair zoom, now examining a forgone gain.
        removed_target = fixed(VGroup())
        for left, value, color in [(-1.16, 4.8, DEMAND), (0.06, 3.8, SUPPLY)]:
            removed_target.add(fixed(Polygon([left, DETAIL_BASE, 0], [left + 1.1, DETAIL_BASE, 0],
                [left + 1.1, DETAIL_BASE + value * DETAIL_SCALE, 0], [left, DETAIL_BASE + value * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(market), FadeOut(selected_ton),
                  Transform(removed_pair, removed_target), run_time=1.6)
        removed_detail = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(removed_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$4.80$', color=DEMAND).scale(0.72).next_to(removed_pair[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$3.80$', color=SUPPLY).scale(0.72).next_to(removed_pair[1].get_corner(UR), RIGHT, buff=0.25),
            DashedLine([-0.06, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=DWL, stroke_width=1.6),
            DashedLine([3.25, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], color=DWL, stroke_width=1.6),
            Line([3.8, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], [3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                color=DWL, stroke_width=3),
            VGroup(Tex(r'TS $=+\$1$', color=TOTAL), Tex(r'DWL $=\$1$', color=INK))
                .arrange(DOWN, buff=0.16, aligned_edge=LEFT).scale(0.8)
                .next_to([3.8, DETAIL_BASE + 4.3 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MB $>$ MC', color=INK).scale(0.8).move_to([4.3, -0.1, 0])))
        conclusion = fixed(Tex(r'Removing this ton creates $\$1$ of deadweight loss.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('Would removing this ton improve welfare?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        removed_detail[3].bars = removed_detail[4].bars = removed_pair
        removed_detail[3].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        removed_detail[4].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head,
            'The 36th unit: a quantity exchanged in equilibrium.'))
        self.add(detail_people)
        self.play(FadeIn(removed_detail[:5]), FadeIn(value_question), FadeIn(unit_context))
        self.pause('1.f.values')
        self.play(FadeOut(value_question))
        self.play(FadeIn(removed_detail[5:]), FadeIn(conclusion))
        self.pause('1.f')

        # ---- 1.g · The exact marginal boundary, rather than an average bar height.
        self.remove(detail_people)
        self.play(FadeOut(removed_detail, suspend_mobject_updating=False), FadeOut(conclusion), FadeOut(unit_context),
                  Transform(removed_pair, removed_home), FadeIn(market), run_time=1.6)
        self.play(FadeOut(removed_pair),
                  *[bar.animate.set_fill(opacity=SURPLUS_OPACITY) for bars in (cs, ps) for bar in list(bars)[COMPARE_LOW:]],
                  *[bar.animate.set_fill(opacity=BASE_OPACITY) for bar in list(costs)[COMPARE_LOW:]],
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20))))
        boundary = fixed(Tex(r'At equilibrium, MB $=$ MC.', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(boundary))
        self.pause('1.g.boundary')
        self.remove(head, boundary)
        head = fixed(title('The First Welfare Theorem'))
        theorem = fixed(VGroup(
            Tex('When all benefits and costs are counted,', color=DEFINITION).scale(DEFINITION_SCALE),
            Tex('competitive equilibrium maximizes total surplus.', color=DEFINITION).scale(DEFINITION_SCALE))
            .arrange(DOWN, buff=0.12).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(theorem))
        self.pause('1.g')

        # ---- 2.a · Part B's head-on Gary/Molly deliberation, room for bystanders.
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.clear()
        head = fixed(title('Negative Externalities'))
        negative_context = fixed(subtitle(head, 'A cost paid by others outside the market.'))
        PAIR_BASE, PAIR_SCALE, PAIR_WIDTH = -1.65, 0.44, 0.95
        PAIR_Q = 20
        PAIR_MB, PAIR_MC = 12 - PAIR_Q / 5, 2 + PAIR_Q / 20
        pair_bars, pair_people, pair_words = fixed(VGroup()), fixed(Group()), fixed(VGroup())
        for left, value, color, name, person_x, term in [
            (-4.55, PAIR_MB, DEMAND, 'Gary', -4.9, 'MB'),
            (-3.48, PAIR_MC, SUPPLY, 'Molly', -2.15, 'MC')]:
            pair_bars.add(fixed(Polygon([left, PAIR_BASE, 0], [left + PAIR_WIDTH, PAIR_BASE, 0],
                [left + PAIR_WIDTH, PAIR_BASE + min(value, MARKET_P) * PAIR_SCALE, 0],
                [left, PAIR_BASE + min(value, MARKET_P) * PAIR_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
            pair_people.add(fixed(Ellipse(width=0.48, height=0.06, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([person_x, PAIR_BASE - 0.70, 0])))
            pair_people.add(fixed(Sphere(radius=0.23, color=color, opacity=1, resolution=(32, 24))
                .move_to([person_x, PAIR_BASE - 0.40, 0])))
            pair_words.add(fixed(Tex(name, color=INK).scale(0.7).move_to([person_x, PAIR_BASE - 1.05, 0])))
            pair_words.add(fixed(Tex(rf'{term} $\${value:g}$', color=color).scale(0.65)
                .move_to([left + PAIR_WIDTH / 2, PAIR_BASE + value * PAIR_SCALE + 0.35, 0])))
            if name == 'Molly':
                pair_words[-1].next_to(pair_bars[-1], RIGHT, buff=0.25)
        for left, lower, upper, color in [
            (-4.55, MARKET_P, PAIR_MB, DEMAND), (-3.48, PAIR_MC, MARKET_P, SUPPLY)]:
            pair_bars.add(fixed(Polygon(
                [left, PAIR_BASE + lower * PAIR_SCALE, 0],
                [left + PAIR_WIDTH, PAIR_BASE + lower * PAIR_SCALE, 0],
                [left + PAIR_WIDTH, PAIR_BASE + upper * PAIR_SCALE, 0],
                [left, PAIR_BASE + upper * PAIR_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=SURPLUS_OPACITY)))
        for left, value, color in [(-4.55, PAIR_MB, DEMAND), (-3.48, PAIR_MC, SUPPLY)]:
            pair_bars.add(fixed(Line([left, PAIR_BASE + value * PAIR_SCALE, 0],
                [left + PAIR_WIDTH, PAIR_BASE + value * PAIR_SCALE, 0], color=color, stroke_width=3)))
        pair_words[1].next_to(pair_bars[4], LEFT, buff=0.22)
        pair_words[3].next_to(pair_bars[5], RIGHT, buff=0.22)
        pair_price = fixed(VGroup(
            Line([-4.7, PAIR_BASE + 4 * PAIR_SCALE, 0], [-2.38, PAIR_BASE + 4 * PAIR_SCALE, 0], color=GUIDE, stroke_width=2.5),
            Tex(r'Price $\$4$', color=GUIDE).scale(0.65).move_to([-5.7, PAIR_BASE + 4 * PAIR_SCALE, 0])))
        pair_baseline = fixed(Line([-4.7, PAIR_BASE, 0], [-2.38, PAIR_BASE, 0], color=MUTED))
        pair = fixed(Group(pair_bars, pair_people, pair_words, pair_price, pair_baseline))
        # Keep sphere front faces in front; fixed() disables depth for flat labels.
        for mob in pair_people.get_family():
            if isinstance(mob, Sphere):
                mob.apply_depth_test()
        pair_material = fixed(Group(pair_bars, pair_words, pair_price, pair_baseline))
        self.add(pair_people)
        self.play(FadeIn(head), FadeIn(negative_context), FadeIn(pair_material))
        self.remove(pair_people, pair_material)
        self.add(pair)
        self.pause('2.a')

        # ---- 2.b · A single external-cost piece belongs to one pink bystander.
        BYSTANDER_CENTER, BYSTANDER_GAP = 3.7, 0.61
        bystanders = fixed(Group())
        individual_costs, external_stack = fixed(VGroup()), fixed(VGroup())
        for i in range(8):
            x = BYSTANDER_CENTER
            person = fixed(Group(
                Ellipse(width=0.27, height=0.04, stroke_width=0, fill_color=EXT, fill_opacity=0.35).move_to([x, -2.28, 0]),
                Sphere(radius=0.12, color=EXT, opacity=1, resolution=(24, 16)).move_to([x, -2.10, 0])))
            person[1].apply_depth_test()
            bystanders.add(person)
            lower = PAIR_BASE + i * 0.25 * PAIR_SCALE
            external_stack.add(fixed(Polygon([3.05, lower, 0], [4.35, lower, 0],
                [4.35, lower + 0.25 * PAIR_SCALE, 0], [3.05, lower + 0.25 * PAIR_SCALE, 0],
                stroke_width=1, stroke_color=BG, fill_color=EXT, fill_opacity=0.65)))
            individual_costs.add(external_stack[-1].copy().stretch_to_fit_width(0.46)
                .move_to([x, PAIR_BASE + 0.125 * PAIR_SCALE, 0]))
        bystander_word = fixed(Tex('Bystander', color=CAPTION).scale(0.7).move_to([BYSTANDER_CENTER, -2.8, 0]))
        cost_heading = fixed(Tex('Externalized cost per ton', color=CAPTION).scale(0.65)
            .move_to([BYSTANDER_CENTER, 1.15, 0]))
        small_word = fixed(Tex(r'$\$0.25$', color=EXT).scale(0.7).move_to([BYSTANDER_CENTER, 0.55, 0]))
        self.add(bystanders[0])
        self.play(FadeIn(bystander_word), FadeIn(individual_costs[0]), FadeIn(cost_heading), FadeIn(small_word))
        self.pause('2.b')

        # ---- 2.c.people · Each person's cost stays above them until all eight appear.
        for i in range(1, 8):
            x = BYSTANDER_CENTER + i * BYSTANDER_GAP / 2
            bystanders[i].set_x(x)
            individual_costs[i].set_x(x)
            self.add(bystanders[i])
            additions = [FadeIn(individual_costs[i]),
                *[bystanders[j].animate.set_x(BYSTANDER_CENTER + (j - i / 2) * BYSTANDER_GAP) for j in range(i)],
                *[individual_costs[j].animate.set_x(BYSTANDER_CENTER + (j - i / 2) * BYSTANDER_GAP) for j in range(i)]]
            if i == 1:
                additions.append(Transform(bystander_word,
                    fixed(Tex('Bystanders', color=CAPTION).scale(0.7).move_to(bystander_word))))
            self.play(*additions, run_time=0.5)
        self.pause('2.c.people')

        # ---- 2.c · Only now combine those eight costs into one stack.
        self.play(FadeOut(small_word),
                  LaggedStart(*[Transform(individual_costs[i], external_stack[i]) for i in range(8)],
                              lag_ratio=0.15), run_time=2)
        self.remove(*list(individual_costs))
        self.add(external_stack)
        stack_word = fixed(Tex(r'$8\times\$0.25=\$2$', color=EXT).scale(0.8).move_to([3.7, 0.55, 0]))
        conclusion = fixed(Tex('Exchanges between buyer and seller in the market can impose a cost on others.',
            color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(stack_word), FadeIn(conclusion))
        self.pause('2.c')

        # ---- 2.d · Carry Gary and Molly directly into the two full-market graphs.
        left_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        left_ax.shift(np.array([-6.45, -2.15, 0]) - left_ax.c2p(0, 0))
        right_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        right_ax.shift(np.array([1.25, -2.15, 0]) - right_ax.c2p(0, 0))
        left_words = fixed(VGroup(
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(0, 13), UP, buff=0.16),
            Tex('Q', color=INK).scale(0.7).next_to(left_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(60, 0), DOWN, buff=0.7),
            Tex('$2$', color=SUPPLY).scale(0.65).next_to(left_ax.c2p(0, 2), LEFT, buff=0.15)))
        right_words = fixed(VGroup(
            Tex('Externalized cost per ton', color=CAPTION).scale(0.65)
                .next_to(right_ax.c2p(0, 13), UP, buff=0.16, aligned_edge=LEFT),
            Tex(r'$\$2$', color=EXT).scale(0.65).next_to(right_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('Q', color=INK).scale(0.7).next_to(right_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(right_ax.c2p(60, 0), DOWN, buff=0.7),
            Tex(r'$\hat{Q}=40$', color=GUIDE).scale(0.65).next_to(right_ax.c2p(40, 0), DOWN, buff=0.18)))
        left_demand = fixed(Line(left_ax.c2p(0, 12), left_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        left_demand_intercept = fixed(Tex('$12$', color=DEMAND).scale(0.65)
            .next_to(left_ax.c2p(0, 12), LEFT, buff=0.15))
        left_supply = fixed(Line(left_ax.c2p(0, 2), left_ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        left_curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(left_ax.c2p(8, 10.4), UR, buff=0.1),
            Tex('MC', color=INK).scale(0.7).next_to(left_ax.c2p(60, 5), RIGHT, buff=0.12)))
        left_eq = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.06, color=GUIDE),
            DashedLine(left_ax.c2p(0, 4), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            Tex(r'$\hat{Q}=40$', color=GUIDE).scale(0.65).next_to(left_ax.c2p(40, 0), DOWN, buff=0.18)))
        private_bars, benefit_bars, external_bars = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        producer_surplus = fixed(VGroup())
        for q in range(40):
            l, r = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            private_bars.add(fixed(Polygon(left_ax.c2p(l, 0), left_ax.c2p(r, 0),
                left_ax.c2p(r, 2 + r / 20), left_ax.c2p(l, 2 + l / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY)))
            benefit_bars.add(fixed(Polygon(left_ax.c2p(l, 4), left_ax.c2p(r, 4),
                left_ax.c2p(r, 12 - r / 5), left_ax.c2p(l, 12 - l / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY)))
            producer_surplus.add(fixed(Polygon(left_ax.c2p(l, 2 + l / 20), left_ax.c2p(r, 2 + r / 20),
                left_ax.c2p(r, 4), left_ax.c2p(l, 4),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=SURPLUS_OPACITY)))
            external_bars.add(fixed(Polygon(right_ax.c2p(l, 0), right_ax.c2p(r, 0),
                right_ax.c2p(r, 2), right_ax.c2p(l, 2),
                stroke_width=0, fill_color=EXT, fill_opacity=GRAPH_EXT_OPACITY)))
        q = PAIR_Q - 1
        left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
        landing_pair = fixed(VGroup(
            Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                left_ax.c2p(right, 4), left_ax.c2p(left, 4),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            private_bars[q].copy(), benefit_bars[q].copy(), producer_surplus[q].copy(),
            Line(left_ax.c2p(left, 12 - left / 5), left_ax.c2p(right, 12 - right / 5),
                color=DEMAND, stroke_width=3),
            Line(left_ax.c2p(left, 2 + left / 20), left_ax.c2p(right, 2 + right / 20),
                color=SUPPLY, stroke_width=3)))
        first_flying = pair_bars.copy()
        pair_annotations = fixed(VGroup(pair_words, pair_price, pair_baseline))
        right_axis_words = fixed(VGroup(*list(right_words)[:4]))
        self.remove(pair, *list(bystanders))
        self.add(first_flying, pair_annotations)
        self.play(FadeOut(pair_annotations), FadeOut(stack_word), FadeOut(cost_heading),
                  FadeOut(bystander_word), FadeOut(conclusion),
                  Transform(first_flying, landing_pair),
                  Transform(external_stack, fixed(VGroup(external_bars[q].copy()))),
                  FadeIn(left_ax), FadeIn(right_ax), FadeIn(left_words), FadeIn(right_axis_words),
                  FadeIn(left_demand), FadeIn(left_demand_intercept), FadeIn(left_supply), FadeIn(left_curve_words), FadeIn(left_eq), run_time=2)
        self.remove(first_flying, external_stack)
        self.add(private_bars[q], benefit_bars[q], producer_surplus[q], external_bars[q])
        self.pause('2.d')

        # ---- 2.f · Sweep across corresponding exchanges and their external costs.
        self.play(LaggedStart(*[
            AnimationGroup(FadeIn(private_bars[q]), FadeIn(benefit_bars[q]),
                           FadeIn(producer_surplus[q]), FadeIn(external_bars[q]))
            for q in range(40) if q != PAIR_Q - 1], lag_ratio=0.12), run_time=4)
        self.remove(*list(private_bars), *list(benefit_bars), *list(producer_surplus), *list(external_bars))
        self.add(private_bars, benefit_bars, producer_surplus, external_bars)
        self.remove(right_axis_words)
        self.add(right_words)
        ext_total_word = fixed(Tex(r'Total external cost: $\$80$', color=EXT).scale(0.75)
                               .move_to([3.9, 0.3, 0]))
        self.play(FadeIn(ext_total_word))
        self.pause('2.f')

        # ---- 3.a · Strip away benefit to account for every cost.
        self.remove(head, negative_context)
        head = fixed(title('Marginal Social Cost'))
        social_cost_context = fixed(subtitle(head,
            'All the costs to society of one more unit of the good.'))
        cost_question = fixed(Tex('What is the full cost of a trade?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(social_cost_context), FadeIn(cost_question), FadeOut(left_demand), FadeOut(benefit_bars), FadeOut(producer_surplus),
                  FadeOut(left_demand_intercept), FadeOut(left_curve_words[0]), FadeOut(left_eq), FadeOut(ext_total_word))
        self.pause('3.a')

        # ---- 3.b · Transfer the actual external-cost strips onto private cost.
        stacked_targets = fixed(VGroup())
        for q in range(40):
            l, r = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            stacked_targets.add(fixed(Polygon(left_ax.c2p(l, 2 + l / 20), left_ax.c2p(r, 2 + r / 20),
                left_ax.c2p(r, 4 + r / 20), left_ax.c2p(l, 4 + l / 20),
                stroke_width=0, fill_color=EXT, fill_opacity=GRAPH_EXT_OPACITY)))
        self.play(LaggedStart(*[Transform(external_bars[q], stacked_targets[q]) for q in range(40)],
                            lag_ratio=0.045), run_time=3)
        social_cost = fixed(Line(left_ax.c2p(0, 4), left_ax.c2p(60, 7), color=SUPPLY, stroke_width=3))
        social_cost_intercept = fixed(Tex('$4$', color=SUPPLY).scale(0.65)
            .next_to(left_ax.c2p(0, 4), LEFT, buff=0.15))
        social_word = fixed(Tex('MSC', color=INK).scale(0.7).next_to(left_ax.c2p(60, 7), RIGHT, buff=0.12))
        cost_terms = fixed(VGroup(
            Tex('Marginal social cost', color=SUPPLY), Tex('$=$', color=INK),
            Tex('Marginal cost', color=SUPPLY), Tex('$+$', color=INK),
            Tex('External cost', color=EXT)).scale(0.72))
        cost_terms[0].move_to([3.8, 0.65, 0])
        VGroup(*list(cost_terms)[1:]).arrange(RIGHT, buff=0.16).next_to(cost_terms[0], DOWN, buff=0.25)
        cost_definition = fixed(VGroup(
            Tex('MSC', color=SUPPLY), Tex('$=$', color=INK), Tex('MC', color=SUPPLY),
            Tex('$+$', color=INK), Tex('EXT', color=EXT))
            .arrange(RIGHT, buff=0.16).scale(0.8).move_to(cost_terms))
        cost_divider = fixed(Line([0.25, -3, 0], [0.25, 2, 0], color=MUTED,
                                 stroke_width=1, stroke_opacity=0.45))
        self.remove(cost_question)
        self.play(FadeOut(right_ax), FadeOut(right_words),
                  FadeIn(social_cost), FadeIn(social_cost_intercept), FadeIn(social_word))
        self.play(FadeIn(cost_terms), FadeIn(cost_divider))
        self.pause('3.b.words')
        self.play(ReplacementTransform(cost_terms, cost_definition), run_time=1.2)
        self.pause('3.b')

        # ---- 3.c · Recenter, restore demand, and mark the unchanged market outcome.
        self.play(FadeOut(cost_definition), FadeOut(cost_divider))
        cost_graph = fixed(VGroup(left_ax, left_words, private_bars, external_bars,
                                 left_supply, left_curve_words[1], social_cost, social_cost_intercept, social_word))
        self.remove(*[m for m in self.mobjects if m is not head and m is not social_cost_context])
        self.add(cost_graph, head)
        self.play(cost_graph.animate.shift(RIGHT * 3.7), run_time=1.1)
        self.play(cost_graph.animate.scale(1.15, about_point=left_ax.c2p(30, 6.5)), run_time=0.8)
        # Keep the axes' numerical mappings live after the group moves.
        full_demand = fixed(Line(left_ax.c2p(0, 12), left_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        demand_intercept = fixed(Tex('$12$', color=DEMAND).scale(0.65 * 1.15)
            .next_to(left_ax.c2p(0, 12), LEFT, buff=0.15 * 1.15))
        demand_word = fixed(Tex('MB', color=INK).scale(0.7).next_to(left_ax.c2p(7, 10.6), UR, buff=0.12))
        market_reference = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.065, color=GUIDE),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            VGroup(Tex(r'$\hat{Q}$', color=GUIDE), Tex('$40$', color=GUIDE))
                .arrange(DOWN, buff=0.06).scale(0.65).next_to(left_ax.c2p(40, 0), DOWN, buff=0.18),
            Tex(r'$\hat{P}=$', color=GUIDE).scale(0.7).next_to(social_cost_intercept, LEFT, buff=0.12),
            DashedLine(left_ax.c2p(0, 4), left_ax.c2p(40, 4), color=GUIDE, stroke_width=2)))
        self.remove(head, social_cost_context)
        head = fixed(title('Social Welfare'))
        welfare_context = fixed(subtitle(head,
            'The welfare of everyone, not just buyers and sellers in the market.'))
        question = fixed(Tex('Would reducing quantity improve welfare?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(welfare_context), FadeIn(full_demand),
                  FadeIn(demand_intercept), FadeIn(demand_word), FadeIn(market_reference), FadeIn(question))
        social_graph = fixed(VGroup(cost_graph, full_demand, demand_intercept, demand_word, market_reference))
        self.remove(cost_graph, full_demand, demand_intercept, demand_word, market_reference)
        self.add(social_graph)
        self.pause('3.c')

        # ---- 3.e · Work through one traded ton, including external cost and deadweight loss.
        removed_social_pair = fixed(VGroup(
            Polygon(*private_bars[(MARKET_Q - 1)].get_vertices()[:2],
                left_ax.c2p((MARKET_Q - 1) + 1 - BAR_GAP / 2, 12 - ((MARKET_Q - 1) + 1 - BAR_GAP / 2) / 5),
                left_ax.c2p((MARKET_Q - 1) + BAR_GAP / 2, 12 - ((MARKET_Q - 1) + BAR_GAP / 2) / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            private_bars[(MARKET_Q - 1)].copy(), external_bars[(MARKET_Q - 1)].copy()))
        removed_social_home = removed_social_pair.copy()
        selected_ton = fixed(SurroundingRectangle(removed_social_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(question)
        self.play(FadeIn(removed_social_pair), FadeIn(selected_ton))
        self.pause('3.e.select')
        # Keep the exchange centered between the two decisions.
        EXCHANGE_X = 0
        removed_social_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 4.0, DEMAND), (0.06, 0, 4.0, SUPPLY),
                                      (0.06, 4.0, 6.0, EXT)]:
            removed_social_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        removed_social_target.shift(RIGHT * EXCHANGE_X)
        self.play(FadeOut(social_graph), FadeOut(welfare_context), FadeOut(selected_ton),
                  Transform(removed_social_pair, removed_social_target), run_time=1.6)
        removed_social_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(removed_social_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([EXCHANGE_X - 1.3, DETAIL_BASE, 0], [EXCHANGE_X + 1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$4.00$', color=DEMAND).scale(0.72).next_to(removed_social_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$4.00$', color=SUPPLY).scale(0.72).next_to(removed_social_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'EXT $\$2$', color=EXT).scale(0.72).next_to(removed_social_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$6.00$', color=SUPPLY).scale(0.72).next_to(removed_social_target[2].get_corner(UR), RIGHT, buff=0.25)))
        conclusion = fixed(Tex(r'Removing this ton eliminates $\$2$ of deadweight loss.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        unit_context = fixed(subtitle(head,
            'The 40th unit: a quantity exchanged in equilibrium.'))
        unit_bystander = fixed(Group(
            Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=EXT, fill_opacity=0.28)
                .move_to([0, DETAIL_BASE - 0.60, 0]),
            Sphere(radius=0.18, color=EXT, opacity=1, resolution=(32, 24))
                .move_to([0, DETAIL_BASE - 0.35, 0])))
        unit_bystander[1].apply_depth_test()
        unit_bystander_word = fixed(Tex('Bystanders', color=CAPTION).scale(0.65)
            .move_to([0, DETAIL_BASE - 0.94, 0]))
        detail_people.shift(RIGHT * EXCHANGE_X)
        unit_bystander.shift(RIGHT * EXCHANGE_X)
        unit_bystander_word.shift(RIGHT * EXCHANGE_X)
        self.add(detail_people, unit_bystander, unit_bystander_word)
        # Compact externality labels: names on bars, numbers at boundary heights.
        for label in [removed_social_labels[4], removed_social_labels[5], removed_social_labels[6], removed_social_labels[7]]:
            label.clear_updaters()
        removed_social_labels[4].become(fixed(Tex(r'$\$4.00$', color=DEMAND).scale(0.72)
            .next_to([-1.16, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], LEFT, buff=0.25)))
        removed_social_labels[5].become(fixed(Tex(r'$\$4.00$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        removed_social_labels[7].become(fixed(Tex(r'$\$6.00$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        removed_social_labels[6].set_opacity(0)
        compact_external_labels = fixed(VGroup(
            Tex('MB', color=DEMAND).scale(0.58)
                .next_to([-0.61, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.58)
                .move_to([0.61, DETAIL_BASE + 5.0 * DETAIL_SCALE, 0]),
            DashedLine([1.35, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0],
                       [1.35, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0], color=EXT, stroke_width=2.5, stroke_opacity=1),
            Tex(r'$\$2$', color=EXT).scale(0.72)
                .next_to([1.35, DETAIL_BASE + 5.0 * DETAIL_SCALE, 0], RIGHT, buff=0.25)
        ).set_z_index(3))
        self.play(FadeIn(removed_social_labels), FadeIn(compact_external_labels), FadeIn(unit_context), run_time=0.4)
        # Measure this ton's loss only in the close-up; the sweep will shade the market.
        removed_dwl_bar = fixed(Polygon(
            [0.06, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0],
            [1.16, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0],
            [1.16, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0],
            [0.06, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        left, right = (MARKET_Q - 1) + BAR_GAP / 2, (MARKET_Q - 1) + 1 - BAR_GAP / 2
        removed_dwl_market = fixed(Polygon(
            left_ax.c2p(left, 12 - left / 5), left_ax.c2p(right, 12 - right / 5),
            left_ax.c2p(right, 4 + right / 20), left_ax.c2p(left, 4 + left / 20),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        # Private willingness and social value are separate comparisons.
        exchange_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.65).move_to([-5.0, 2.45, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.65).move_to([5.0, 2.45, 0])))
        exchange_private_guides = fixed(VGroup(
            DashedLine(removed_social_labels[4].get_left() + LEFT * 0.12,
                       [-3.65, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4)))
        exchange_private_answer = fixed(VGroup(
            Tex('Indifferent', color=INK), Tex(r'MB $=$ MC', color=TOTAL))
            .arrange(DOWN, buff=0.12).scale(0.65)
            .next_to([-3.65, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], LEFT, buff=0.3))
        exchange_social_guides = fixed(VGroup(
            DashedLine(removed_social_labels[7].get_right() + RIGHT * 0.12, [3.65, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-0.06, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([1.16, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], [1.3, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([3.3, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            Line([3.65, DETAIL_BASE + 4.0 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 6.0 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3)))
        exchange_social_answer = fixed(VGroup(
            Tex('No', color=INK), Tex(r'MB $<$ MSC', color=TOTAL),
            Tex(r'TS $=-\$2$', color=TOTAL), Tex(r'DWL $=\$2$', color=INK))
            .arrange(DOWN, buff=0.10, aligned_edge=LEFT).scale(0.60)
            .next_to([3.65, DETAIL_BASE + 5.0 * DETAIL_SCALE, 0], RIGHT, buff=0.3))
        self.play(FadeIn(exchange_questions))
        self.pause('3.e.values')
        self.play(FadeIn(exchange_private_guides), FadeIn(exchange_private_answer[1:]))
        self.pause('3.e.private.compare')
        self.play(FadeIn(exchange_private_answer[0]))
        self.pause('3.e.private')
        self.play(FadeIn(exchange_social_guides), FadeIn(exchange_social_answer[1]))
        self.pause('3.e.social.compare')
        self.play(FadeIn(removed_dwl_bar),
                  FadeIn(exchange_social_answer[0]), FadeIn(exchange_social_answer[2:]), FadeIn(conclusion))
        self.pause('3.e')
        self.remove(detail_people, unit_bystander, unit_bystander_word)
        self.play(FadeOut(compact_external_labels), FadeOut(removed_social_labels, suspend_mobject_updating=False), FadeOut(exchange_questions), FadeOut(exchange_private_guides), FadeOut(exchange_private_answer),
                  FadeOut(exchange_social_guides), FadeOut(exchange_social_answer), FadeOut(conclusion), FadeOut(unit_context),
                  Transform(removed_social_pair, removed_social_home), FadeIn(social_graph), FadeIn(welfare_context),
                  FadeOut(removed_dwl_bar), run_time=1.6)
        # Clear the selected ton's loss before holding on the full market.
        self.play(FadeOut(removed_social_pair))
        self.remove(removed_dwl_bar, removed_dwl_market)
        self.pause('3.e.return')


        # ---- Sweep from equilibrium to unit 36, then continue to efficiency.
        self.remove(head, welfare_context)
        head = fixed(title('Negative Externality'))
        evaluation_q = ValueTracker(40)
        evaluation_line = fixed(DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 6), color=FOCUS, stroke_width=2).set_z_index(2))
        evaluation_line.axes, evaluation_line.quantity = left_ax, evaluation_q
        evaluation_line.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(m.quantity.get_value(), 0),
            m.axes.c2p(m.quantity.get_value(), max(12 - m.quantity.get_value() / 5, 4 + m.quantity.get_value() / 20))))
        marginal_gap = fixed(Line(left_ax.c2p(40, 4), left_ax.c2p(40, 6), color=DWL, stroke_width=7))
        marginal_gap.axes, marginal_gap.quantity = left_ax, evaluation_q
        # Tiny geometric length at equality avoids an undefined zero-length Line.
        marginal_gap.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(m.quantity.get_value(), 12 - m.quantity.get_value() / 5),
            m.axes.c2p(m.quantity.get_value(), 4 + m.quantity.get_value() / 20 + 1e-6)))
        # Reveal each remaining loss slice as the guide passes its actual width.
        loss_slices = fixed(VGroup())
        for q in range(EFFICIENT_Q, MARKET_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            loss_bar = fixed(Polygon(
                left_ax.c2p(left, 12 - left / 5), left_ax.c2p(right, 12 - right / 5),
                left_ax.c2p(right, 4 + right / 20), left_ax.c2p(left, 4 + left / 20),
                stroke_width=0, fill_color=DWL, fill_opacity=0).set_z_index(1))
            loss_bar.quantity = evaluation_q
            loss_bar.slice_left, loss_bar.slice_right = left, right
            loss_bar.add_updater(lambda m: m.set_fill(opacity=0.8 * np.clip(
                (m.slice_right - m.quantity.get_value()) / (m.slice_right - m.slice_left), 0, 1)))
            loss_slices.add(loss_bar)
        social_graph.add(loss_slices)
        self.play(FadeIn(head), FadeIn(evaluation_line), FadeIn(marginal_gap))
        self.play(evaluation_q.animate.set_value(36), run_time=1.2, rate_func=smooth)
        for loss_bar in loss_slices:
            loss_bar.clear_updaters()

        # ---- 3.f.36 · Inspect another exchanged unit with MSC above MB.
        left, right = 36 - 1 + BAR_GAP / 2, 36 - BAR_GAP / 2
        dwl_example_pair = fixed(VGroup(
            Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                left_ax.c2p(right, 12 - right / 5), left_ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            private_bars[36 - 1].copy(), external_bars[36 - 1].copy()))
        dwl_example_home = dwl_example_pair.copy()
        next_dwl_selection = fixed(SurroundingRectangle(dwl_example_pair, color=FOCUS, buff=0.025, stroke_width=2))
        dwl_selection = next_dwl_selection
        self.play(FadeIn(dwl_selection), run_time=0.3)
        self.play(FadeIn(dwl_example_pair), run_time=0.3)
        self.pause('3.f.36.select')
        dwl_example_target = fixed(VGroup())
        for x, low, high, color in [(-1.16, 0, 4.8, DEMAND), (0.06, 0, 3.8, SUPPLY),
                                   (0.06, 3.8, 5.8, EXT)]:
            dwl_example_target.add(fixed(Polygon(
                [x, DETAIL_BASE + low * DETAIL_SCALE, 0], [x + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [x + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [x, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(social_graph), FadeOut(evaluation_line), FadeOut(marginal_gap), FadeOut(welfare_context), FadeOut(dwl_selection),
                  Transform(dwl_example_pair, dwl_example_target), run_time=1.0)
        dwl_example_context = fixed(subtitle(head, 'The 36th unit: an exchange with MSC above MB.'))
        dwl_example_labels = fixed(VGroup(
            Tex(r'MB $\$4.80$', color=DEMAND).scale(0.72),
            Tex(r'MSC $\$5.80$', color=SUPPLY).scale(0.72),
            Tex(r'MC $\$3.80$', color=SUPPLY).scale(0.72).set_opacity(0.25),
            Tex(r'EXT $\$2$', color=EXT).scale(0.72).set_opacity(0.25)))
        for label in dwl_example_labels:
            label.bars = dwl_example_pair
        dwl_example_labels[0].add_updater(lambda m: m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        dwl_example_labels[1].add_updater(lambda m: m.next_to(m.bars[2].get_corner(UR), RIGHT, buff=0.25))
        dwl_example_labels[2].add_updater(lambda m: m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        dwl_example_labels[3].add_updater(lambda m: m.next_to(m.bars[2], RIGHT, buff=0.25))
        dwl_example_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(dwl_example_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED)))
        self.add(detail_people, unit_bystander, unit_bystander_word)
        # Compact externality labels: names on bars, numbers at boundary heights.
        for label in [dwl_example_labels[0], dwl_example_labels[2], dwl_example_labels[3], dwl_example_labels[1]]:
            label.clear_updaters()
        dwl_example_labels[0].become(fixed(Tex(r'$\$4.80$', color=DEMAND).scale(0.72)
            .next_to([-1.16, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], LEFT, buff=0.25)))
        dwl_example_labels[2].become(fixed(Tex(r'$\$3.80$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        dwl_example_labels[1].become(fixed(Tex(r'$\$5.80$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        dwl_example_labels[3].set_opacity(0)
        compact_external_labels = fixed(VGroup(
            Tex('MB', color=DEMAND).scale(0.58)
                .next_to([-0.61, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.58)
                .move_to([0.61, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0]),
            DashedLine([1.35, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0],
                       [1.35, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], color=EXT, stroke_width=2.5, stroke_opacity=1),
            Tex(r'$\$2$', color=EXT).scale(0.72)
                .next_to([1.35, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], RIGHT, buff=0.25)
        ).set_z_index(3))
        self.play(FadeIn(compact_external_labels), FadeIn(dwl_example_labels), FadeIn(dwl_example_edges), FadeIn(dwl_example_context), run_time=0.4)
        # Private willingness and social value are separate comparisons.
        exchange_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.65).move_to([-5.0, 2.45, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.65).move_to([5.0, 2.45, 0])))
        exchange_private_guides = fixed(VGroup(
            DashedLine(dwl_example_labels[0].get_left() + LEFT * 0.12, [-3.65, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([0.06, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], [-3.65, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            Line([-3.65, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], [-3.65, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3)))
        exchange_private_answer = fixed(VGroup(
            VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex(r'MB $>$ MC', color=TOTAL))
            .arrange(DOWN, buff=0.12).scale(0.65)
            .next_to([-3.65, DETAIL_BASE + 4.3 * DETAIL_SCALE, 0], LEFT, buff=0.3))
        exchange_social_guides = fixed(VGroup(
            DashedLine(dwl_example_labels[1].get_right() + RIGHT * 0.12, [3.65, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-0.06, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([1.16, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [1.3, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([3.3, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            Line([3.65, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3)))
        exchange_social_answer = fixed(VGroup(
            Tex('No', color=INK), Tex(r'MB $<$ MSC', color=TOTAL),
            Tex(r'TS $=-\$1$', color=TOTAL), Tex(r'DWL $=\$1$', color=INK))
            .arrange(DOWN, buff=0.10, aligned_edge=LEFT).scale(0.60)
            .next_to([3.65, DETAIL_BASE + 5.3 * DETAIL_SCALE, 0], RIGHT, buff=0.3))
        self.play(FadeIn(exchange_questions))
        self.pause('3.f.36.values')
        self.play(FadeIn(exchange_private_guides), FadeIn(exchange_private_answer[1:]))
        self.pause('3.f.36.private.compare')
        self.play(FadeIn(exchange_private_answer[0]))
        self.pause('3.f.36.private')
        dwl_example_loss = fixed(Polygon(
            [0.06, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], [1.16, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
            [1.16, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        dwl_example_note = fixed(Tex(r'Every unit exchanged where MSC $>$ MB carries DWL.', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(exchange_social_guides), FadeIn(exchange_social_answer[1]))
        self.pause('3.f.36.social.compare')
        self.play(FadeIn(dwl_example_loss), FadeIn(exchange_social_answer[0]), FadeIn(exchange_social_answer[2:]), FadeIn(dwl_example_note), run_time=0.5)
        self.pause('3.f.36.loss')
        dwl_example_loss_home = fixed(Polygon(
            left_ax.c2p(left, 12 - left / 5), left_ax.c2p(right, 12 - right / 5),
            left_ax.c2p(right, 4 + right / 20), left_ax.c2p(left, 4 + left / 20),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8).set_z_index(1))
        self.remove(detail_people, unit_bystander, unit_bystander_word)
        self.play(FadeOut(compact_external_labels), FadeOut(exchange_questions), FadeOut(exchange_private_guides), FadeOut(exchange_private_answer),
                  FadeOut(exchange_social_guides), FadeOut(exchange_social_answer), FadeOut(dwl_example_edges), FadeOut(dwl_example_context),
                  FadeOut(dwl_example_note), FadeOut(dwl_example_labels, suspend_mobject_updating=False),
                  Transform(dwl_example_pair, dwl_example_home), FadeOut(dwl_example_loss),
                  FadeIn(social_graph), FadeIn(evaluation_line), FadeIn(marginal_gap), run_time=1.0)
        self.remove(dwl_example_loss, dwl_example_loss_home)
        self.play(FadeOut(dwl_example_pair), run_time=0.4)
        self.pause('3.f.36.return')


        # Continue the same guide from unit 36 to social efficiency.
        for loss_bar in loss_slices:
            loss_bar.add_updater(lambda m: m.set_fill(opacity=0.8 * np.clip(
                (m.slice_right - m.quantity.get_value()) / (m.slice_right - m.slice_left), 0, 1)))
        self.play(evaluation_q.animate.set_value(EFFICIENT_Q), run_time=1.2, rate_func=smooth)
        for loss_bar in loss_slices:
            loss_bar.clear_updaters()
        efficient_dot = fixed(Dot(left_ax.c2p(32, 5.6), radius=0.085, color=FOCUS))
        # Compact symbol/value stacks share a row, centered on their own guides.
        efficient_word = fixed(VGroup(Tex(r'$Q^*$', color=FOCUS), Tex('$32$', color=FOCUS))
            .arrange(DOWN, buff=0.06).scale(0.65).next_to(left_ax.c2p(32, 0), DOWN, buff=0.18))
        efficient_word[1].set_y(market_reference[2][1].get_y())
        condition = fixed(Tex('Social welfare is maximized where MB $=$ MSC.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(efficient_dot), FadeIn(efficient_word), FadeIn(condition), FadeOut(marginal_gap))
        self.pause('4.a')

        # ---- 4.a.exchange · Zoom into the last unit at the efficient quantity.
        left, right = EFFICIENT_Q - 1 + BAR_GAP / 2, EFFICIENT_Q - BAR_GAP / 2
        efficient_pair = fixed(VGroup(
            Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                left_ax.c2p(right, 12 - right / 5), left_ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            private_bars[EFFICIENT_Q - 1].copy(), external_bars[EFFICIENT_Q - 1].copy()))
        efficient_home = efficient_pair.copy()
        efficient_selection = fixed(SurroundingRectangle(efficient_pair,
            color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(condition)
        self.play(FadeIn(efficient_pair), FadeIn(efficient_selection))
        efficient_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 5.6, DEMAND), (0.06, 0, 3.6, SUPPLY),
                                      (0.06, 3.6, 5.6, EXT)]:
            efficient_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(social_graph), FadeOut(efficient_word), FadeOut(evaluation_line), FadeOut(efficient_dot),
                  FadeOut(efficient_selection),
                  Transform(efficient_pair, efficient_target), run_time=1.6)
        efficient_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(efficient_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$5.60$', color=DEMAND).scale(0.72).next_to(efficient_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$3.60$', color=SUPPLY).scale(0.72).next_to(efficient_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'$\$2$', color=EXT).scale(0.72).move_to(efficient_target[2]),
            Tex(r'MSC $\$5.60$', color=SUPPLY).scale(0.72).next_to(efficient_target[2].get_corner(UR), RIGHT, buff=0.25)))
        efficient_context = fixed(subtitle(head, 'The 32nd unit: the efficient quantity.'))
        efficient_note = fixed(Tex(r'For this exchange, MB $=$ MSC and there is no deadweight loss.', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(detail_people, unit_bystander, unit_bystander_word)
        # Compact externality labels: names on bars, numbers at boundary heights.
        for label in [efficient_labels[4], efficient_labels[5], efficient_labels[6], efficient_labels[7]]:
            label.clear_updaters()
        efficient_labels[4].become(fixed(Tex(r'$\$5.60$', color=DEMAND).scale(0.72)
            .next_to([-1.16, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], LEFT, buff=0.25)))
        efficient_labels[5].become(fixed(Tex(r'$\$3.60$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        efficient_labels[7].become(fixed(Tex(r'$\$5.60$', color=SUPPLY).scale(0.72)
            .next_to([1.16, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], RIGHT, buff=0.45)))
        efficient_labels[6].set_opacity(0)
        compact_external_labels = fixed(VGroup(
            Tex('MB', color=DEMAND).scale(0.58)
                .next_to([-0.61, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58)
                .next_to([0.61, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.58)
                .move_to([0.61, DETAIL_BASE + 4.6 * DETAIL_SCALE, 0]),
            DashedLine([1.35, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0],
                       [1.35, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], color=EXT, stroke_width=2.5, stroke_opacity=1),
            Tex(r'$\$2$', color=EXT).scale(0.72)
                .next_to([1.35, DETAIL_BASE + 4.6 * DETAIL_SCALE, 0], RIGHT, buff=0.25)
        ).set_z_index(3))
        self.play(FadeIn(compact_external_labels), FadeIn(efficient_labels), FadeIn(efficient_context))
        # Private willingness and social value are separate comparisons.
        exchange_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.65).move_to([-5.0, 2.45, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.65).move_to([5.0, 2.45, 0])))
        exchange_private_guides = fixed(VGroup(
            DashedLine(efficient_labels[4].get_left() + LEFT * 0.12, [-3.65, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([0.06, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0], [-3.65, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            Line([-3.65, DETAIL_BASE + 3.6 * DETAIL_SCALE, 0], [-3.65, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3)))
        exchange_private_answer = fixed(VGroup(
            VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex(r'MB $>$ MC', color=TOTAL))
            .arrange(DOWN, buff=0.12).scale(0.65)
            .next_to([-3.65, DETAIL_BASE + 4.6 * DETAIL_SCALE, 0], LEFT, buff=0.3))
        exchange_social_guides = fixed(VGroup(
            DashedLine(efficient_labels[7].get_right() + RIGHT * 0.12, [3.65, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-0.06, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], [0.06, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4)))
        exchange_social_answer = fixed(VGroup(
            Tex('Neutral', color=INK), Tex(r'MB $=$ MSC', color=TOTAL),
            Tex(r'TS $=\$0$', color=TOTAL), Tex(r'DWL $=\$0$', color=INK))
            .arrange(DOWN, buff=0.10, aligned_edge=LEFT).scale(0.60)
            .next_to([3.65, DETAIL_BASE + 5.6 * DETAIL_SCALE, 0], RIGHT, buff=0.3))
        self.play(FadeIn(exchange_questions))
        self.play(FadeIn(exchange_private_guides), FadeIn(exchange_private_answer[1:]))
        self.pause('4.a.private.compare')
        self.play(FadeIn(exchange_private_answer[0]))
        self.pause('4.a.private')
        self.play(FadeIn(exchange_social_guides), FadeIn(exchange_social_answer[1]))
        self.pause('4.a.social.compare')
        self.play(FadeIn(exchange_social_answer[0]), FadeIn(exchange_social_answer[2:]), FadeIn(efficient_note))
        self.pause('4.a.exchange')
        self.remove(detail_people, unit_bystander, unit_bystander_word)
        self.play(FadeOut(compact_external_labels), FadeOut(efficient_labels), FadeOut(efficient_context), FadeOut(exchange_questions), FadeOut(exchange_private_guides), FadeOut(exchange_private_answer),
                  FadeOut(exchange_social_guides), FadeOut(exchange_social_answer),
                  FadeOut(efficient_note), run_time=0.4)
        self.play(Transform(efficient_pair, efficient_home), FadeIn(social_graph), FadeIn(evaluation_line),
                  FadeIn(efficient_dot), FadeIn(efficient_word), run_time=1.6)
        self.play(FadeOut(efficient_pair), FadeIn(condition))
        self.pause('4.a.return')

        # ---- 4.b · The losses from excessive trades; not all external damage.
        # Retitle: only ': DWL' fades in; the words that stay, stay put.
        new_head = fixed(title('Negative Externality: DWL'))
        dwl_context = fixed(subtitle(new_head,
            'Overproduction of goods that are too costly to society.'))
        self.play(TransformMatchingTex(head, new_head), FadeIn(dwl_context))
        head = new_head
        # The sweep already revealed all eight bars; keep them for the DWL explanation.
        social_graph.remove(loss_slices)
        self.add(loss_slices)
        self.remove(condition)
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(left_ax.c2p(40, 5.4), RIGHT, buff=0.3))
        conclusion = fixed(Tex('These trades create deadweight loss because social cost exceeds benefit.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(dwl_word), FadeIn(conclusion))
        self.pause('4.b')

        # ---- 4.c · Final comparison: the market produces too much.
        self.remove(conclusion, dwl_context)
        new_head = fixed(title('Negative Externality'))   # retitle: only ': DWL' fades out
        evaluation_line.clear_updaters()
        final_market = fixed(VGroup(social_graph, loss_slices, dwl_word,
                                    evaluation_line, efficient_dot, efficient_word))
        self.play(TransformMatchingTex(head, new_head), final_market.animate.shift(LEFT * 2.5), run_time=1.2)
        head = new_head
        quantity_result = fixed(VGroup(
            Tex(r'$Q^*$', color=FOCUS), Tex('$<$', color=INK),
            Tex(r'$\hat{Q}$', color=GUIDE)).scale(1.3)
            .arrange(RIGHT, buff=1.0).move_to([3.5, 1.9, 0]))
        quantity_comparison = fixed(VGroup(quantity_result,
            Tex('Efficient quantity', color=CAPTION).scale(0.7)
                .next_to(quantity_result, DOWN, buff=0.22).set_x(quantity_result[0].get_x()),
            Tex('Market quantity', color=CAPTION).scale(0.7)
                .next_to(quantity_result, DOWN, buff=0.22).set_x(quantity_result[2].get_x())))
        market_takeaway = fixed(Tex('Markets for goods with negative externalities produce too much.', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(quantity_comparison), FadeIn(market_takeaway))
        self.pause('4.c.comparison')
        # Keep the optional beneficial-exchange detour inactive before positive externalities.
        if False:  # Retained optional detour; continue to positive externalities below.
            self.play(FadeOut(quantity_comparison), run_time=0.4)
            conclusion = fixed(Tex('Are some exchanges worthwhile even with externalities on others?', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
            self.play(FadeIn(conclusion))
            left, right = 23 + BAR_GAP / 2, 24 - BAR_GAP / 2
            beneficial_pair = fixed(VGroup(
                Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                    left_ax.c2p(right, 12 - right / 5), left_ax.c2p(left, 12 - left / 5),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                private_bars[23].copy(), external_bars[23].copy()))
            beneficial_home = beneficial_pair.copy()
            beneficial_selection = fixed(SurroundingRectangle(beneficial_pair,
                color=FOCUS, buff=0.025, stroke_width=2))
            self.play(FadeIn(beneficial_pair), FadeIn(beneficial_selection))
            self.pause('4.c.beneficial')
            # Keep the higher MB bar below the subtitle while retaining a common value scale.
            BENEFICIAL_SCALE = 0.55
            beneficial_target = fixed(VGroup())
            for left, low, high, color in [(-1.16, 0, 7.2, DEMAND), (0.06, 0, 3.2, SUPPLY),
                                          (0.06, 3.2, 5.2, EXT)]:
                beneficial_target.add(fixed(Polygon(
                    [left, DETAIL_BASE + low * BENEFICIAL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * BENEFICIAL_SCALE, 0],
                    [left + 1.1, DETAIL_BASE + high * BENEFICIAL_SCALE, 0], [left, DETAIL_BASE + high * BENEFICIAL_SCALE, 0],
                    stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
            self.remove(*list(loss_slices))
            self.add(loss_slices)
            self.play(FadeOut(social_graph), FadeOut(loss_slices), FadeOut(dwl_word),
                      FadeOut(evaluation_line), FadeOut(efficient_dot), FadeOut(efficient_word), FadeOut(beneficial_selection),
                      Transform(beneficial_pair, beneficial_target), run_time=1.6)
            beneficial_labels = fixed(VGroup(
                *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
                  for bar, color in zip(beneficial_target, [DEMAND, SUPPLY, SUPPLY])],
                Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
                Tex(r'MB $\$7.20$', color=DEMAND).scale(0.72).next_to(beneficial_target[0].get_corner(UL), LEFT, buff=0.25),
                Tex(r'MC $\$3.20$', color=SUPPLY).scale(0.72).next_to(beneficial_target[1].get_corner(UR), RIGHT, buff=0.25),
                Tex(r'EXT $\$2$', color=EXT).scale(0.72).next_to(beneficial_target[2], RIGHT, buff=0.25),
                Tex(r'MSC $\$5.20$', color=SUPPLY).scale(0.72).next_to(beneficial_target[2].get_corner(UR), RIGHT, buff=0.25)))
            beneficial_context = fixed(subtitle(head, 'The 24th unit: a quantity below the efficient quantity.'))
            self.add(detail_people, unit_bystander, unit_bystander_word)
            # Compact externality labels: names on bars, numbers at boundary heights.
            for label in [beneficial_labels[4], beneficial_labels[5], beneficial_labels[6], beneficial_labels[7]]:
                label.clear_updaters()
            beneficial_labels[4].become(fixed(Tex(r'$\$7.20$', color=DEMAND).scale(0.72)
                .next_to([-1.16, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], LEFT, buff=0.25)))
            beneficial_labels[5].become(fixed(Tex(r'$\$3.20$', color=SUPPLY).scale(0.72)
                .next_to([1.16, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0], RIGHT, buff=0.45)))
            beneficial_labels[7].become(fixed(Tex(r'$\$5.20$', color=SUPPLY).scale(0.72)
                .next_to([1.16, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], RIGHT, buff=0.45)))
            beneficial_labels[6].set_opacity(0)
            compact_external_labels = fixed(VGroup(
                Tex('MB', color=DEMAND).scale(0.58)
                    .next_to([-0.61, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], DOWN, buff=0.10),
                Tex('MC', color=SUPPLY).scale(0.58)
                    .next_to([0.61, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0], DOWN, buff=0.10),
                Tex('MSC', color=SUPPLY).scale(0.58)
                    .next_to([0.61, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], UP, buff=0.10),
                Tex('EXT', color=EXT).scale(0.58)
                    .move_to([0.61, DETAIL_BASE + 4.2 * BENEFICIAL_SCALE, 0]),
                DashedLine([1.35, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0],
                           [1.35, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], color=EXT, stroke_width=2.5, stroke_opacity=1),
                Tex(r'$\$2$', color=EXT).scale(0.72)
                    .next_to([1.35, DETAIL_BASE + 4.2 * BENEFICIAL_SCALE, 0], RIGHT, buff=0.25)
            ).set_z_index(3))
            self.play(FadeIn(compact_external_labels), FadeIn(beneficial_labels), FadeIn(beneficial_context))
            # Private willingness and social value are separate comparisons.
            exchange_questions = fixed(VGroup(
                Tex('Will they exchange?', color=DEFINITION).scale(0.65).move_to([-5.0, 2.45, 0]),
                Tex('Is it good for society?', color=DEFINITION).scale(0.65).move_to([5.0, 2.45, 0])))
            exchange_private_guides = fixed(VGroup(
                DashedLine(beneficial_labels[4].get_left() + LEFT * 0.12, [-3.65, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=1.4),
                DashedLine([0.06, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0], [-3.65, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=1.4),
                Line([-3.65, DETAIL_BASE + 3.2 * BENEFICIAL_SCALE, 0], [-3.65, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=3)))
            exchange_private_answer = fixed(VGroup(
                VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex(r'MB $>$ MC', color=TOTAL))
                .arrange(DOWN, buff=0.12).scale(0.65)
                .next_to([-3.65, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], LEFT, buff=0.3))
            exchange_social_guides = fixed(VGroup(
                DashedLine(beneficial_labels[7].get_right() + RIGHT * 0.12, [3.65, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=1.4),
                DashedLine([-0.06, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], [3.65, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=1.4),
                Line([3.65, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], [3.65, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], color=TOTAL, stroke_width=3)))
            exchange_social_answer = fixed(VGroup(
                VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]), Tex(r'MB $>$ MSC', color=TOTAL),
                Tex(r'TS $=\$2$', color=TOTAL), Tex(r'DWL $=\$0$', color=INK))
                .arrange(DOWN, buff=0.10, aligned_edge=LEFT).scale(0.60)
                .next_to([3.65, DETAIL_BASE + 6.2 * BENEFICIAL_SCALE, 0], RIGHT, buff=0.3))
            self.play(FadeIn(exchange_questions))
            self.pause('4.c.values')
            self.play(FadeIn(exchange_private_guides), FadeIn(exchange_private_answer[1:]))
            self.pause('4.c.private.compare')
            self.play(FadeIn(exchange_private_answer[0]))
            self.pause('4.c.private')
            beneficial_surplus = fixed(Polygon(
                [-1.16, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0], [-0.06, DETAIL_BASE + 5.2 * BENEFICIAL_SCALE, 0],
                [-0.06, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0], [-1.16, DETAIL_BASE + 7.2 * BENEFICIAL_SCALE, 0],
                stroke_width=0, fill_color=DEMAND, fill_opacity=SURPLUS_OPACITY))
            self.play(FadeIn(exchange_social_guides), FadeIn(exchange_social_answer[1]))
            self.pause('4.c.social.compare')
            self.play(FadeIn(beneficial_surplus), FadeIn(exchange_social_answer[0]), FadeIn(exchange_social_answer[2:]))
            self.pause('4.c.exchange')
            self.remove(detail_people, unit_bystander, unit_bystander_word)
            self.play(FadeOut(compact_external_labels), FadeOut(beneficial_labels), FadeOut(beneficial_context), FadeOut(beneficial_surplus),
                      FadeOut(exchange_questions), FadeOut(exchange_private_guides), FadeOut(exchange_private_answer),
                      FadeOut(exchange_social_guides), FadeOut(exchange_social_answer), run_time=0.4)
            self.play(Transform(beneficial_pair, beneficial_home), FadeIn(social_graph), FadeIn(loss_slices),
                      FadeIn(dwl_word), FadeIn(evaluation_line), FadeIn(efficient_dot), FadeIn(efficient_word), run_time=1.6)
            self.play(FadeOut(beneficial_pair))
            self.pause('4.c')

        # ---- 5.a · Bystander benefits join the buyer's private benefit.
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.7)
        head = fixed(title('Positive Externalities'))
        positive_context = fixed(subtitle(head, 'A benefit received by others outside the market.'))
        benefit_pair = fixed(VGroup())
        for x, low, high, color in [(-1.16, 0, 4, DEMAND), (0.06, 0, 4, SUPPLY), (-1.16, 4, 6, EXT)]:
            benefit_pair.add(fixed(Polygon(
                [x, DETAIL_BASE + low * DETAIL_SCALE, 0], [x + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [x + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [x, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        benefit_target = benefit_pair.copy()
        benefit_pair[2].move_to([3.8, -0.6, 0]).set_fill(opacity=SURPLUS_OPACITY)
        benefit_edges = fixed(VGroup(
            Line(benefit_pair[0].get_corner(UL), benefit_pair[0].get_corner(UR), color=DEMAND, stroke_width=3),
            Line(benefit_pair[1].get_corner(UL), benefit_pair[1].get_corner(UR), color=SUPPLY, stroke_width=3),
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED)))
        benefit_names = fixed(VGroup(
            Tex('MB', color=DEMAND).scale(0.58).next_to(benefit_pair[0].get_top(), DOWN, buff=0.1),
            Tex('MC', color=SUPPLY).scale(0.58).next_to(benefit_pair[1].get_top(), DOWN, buff=0.1)))
        detached_name = fixed(Tex('EXT', color=EXT).scale(0.58).move_to(benefit_pair[2]))
        unit_bystander.move_to([3.8, DETAIL_BASE - 0.42, 0])
        unit_bystander_word.set_x(3.8)
        self.play(FadeIn(head), FadeIn(positive_context), FadeIn(benefit_pair), FadeIn(benefit_edges),
                  FadeIn(benefit_names), FadeIn(detached_name), FadeIn(detail_people),
                  FadeIn(unit_bystander), FadeIn(unit_bystander_word))
        self.pause('5.a.bystanders')
        self.play(Transform(benefit_pair[2], benefit_target[2], path_arc=PI / 2),
                  detached_name.animate.move_to(benefit_target[2]),
                  unit_bystander.animate.set_x(0), unit_bystander_word.animate.set_x(0), run_time=1.4)
        benefit_top = fixed(Line(benefit_target[2].get_corner(UL), benefit_target[2].get_corner(UR), color=DEMAND, stroke_width=3))
        benefit_top_name = fixed(Tex('MSB', color=DEMAND).scale(0.58).next_to(benefit_target[2].get_top(), UP, buff=0.1))
        benefit_definition = fixed(VGroup(Tex('MSB', color=DEMAND), Tex('$=$', color=INK),
            Tex('MB', color=DEMAND), Tex('$+$', color=INK), Tex('EXT', color=EXT))
            .arrange(RIGHT, buff=0.16).scale(0.8).move_to([3.8, 0.7, 0]))
        self.play(FadeIn(benefit_top), FadeIn(benefit_top_name), FadeIn(benefit_definition))
        self.pause('5.a')

        positive_ax = fixed(style_axes([0, 60, 10], [0, 15, 2], x_length=5.5, y_length=3.9))
        positive_ax.shift(np.array([-6.45, -2.15, 0]) - positive_ax.c2p(0, 0))
        positive_axis_words = fixed(VGroup(
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(positive_ax.c2p(0, 15), UP, buff=0.16),
            Tex('Q', color=INK).scale(0.7).next_to(positive_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(positive_ax.c2p(60, 0), DOWN, buff=0.7),
            Tex('$2$', color=SUPPLY).scale(0.65).next_to(positive_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('$12$', color=DEMAND).scale(0.65).next_to(positive_ax.c2p(0, 12), LEFT, buff=0.15)))
        positive_demand = fixed(Line(positive_ax.c2p(0, 12), positive_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        positive_supply = fixed(Line(positive_ax.c2p(0, 2), positive_ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        positive_social_benefit = fixed(Line(positive_ax.c2p(0, 14), positive_ax.c2p(60, 2), color=DEMAND, stroke_width=3))
        social_benefit_intercept = fixed(Tex('$14$', color=DEMAND).scale(0.65)
            .next_to(positive_ax.c2p(0, 14), LEFT, buff=0.15))
        positive_curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(positive_ax.c2p(8, 10.4), DOWN, buff=0.14),
            Tex('MC', color=INK).scale(0.7).next_to(positive_ax.c2p(60, 5), RIGHT, buff=0.12),
            Tex('MSB', color=INK).scale(0.7).next_to(positive_ax.c2p(8, 12.4), UR, buff=0.10)))
        positive_cost_bars, positive_ext_bars = fixed(VGroup()), fixed(VGroup())
        for q in range(60):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            positive_cost_bars.add(fixed(Polygon(
                positive_ax.c2p(left, 0), positive_ax.c2p(right, 0),
                positive_ax.c2p(right, 2 + right / 20), positive_ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY if q < MARKET_Q else 0)))
            positive_ext_bars.add(fixed(Polygon(
                positive_ax.c2p(left, 12 - left / 5), positive_ax.c2p(right, 12 - right / 5),
                positive_ax.c2p(right, 14 - right / 5), positive_ax.c2p(left, 14 - left / 5),
                stroke_width=0, fill_color=EXT, fill_opacity=GRAPH_EXT_OPACITY if q < MARKET_Q else 0)))
        positive_market = fixed(VGroup(
            Dot(positive_ax.c2p(40, 4), radius=0.06, color=GUIDE),
            DashedLine(positive_ax.c2p(40, 0), positive_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            VGroup(Tex(r'$\hat{Q}$', color=GUIDE), Tex('$40$', color=GUIDE)).arrange(DOWN, buff=0.06).scale(0.65).next_to(positive_ax.c2p(40, 0), DOWN, buff=0.20),
            Tex(r'$\hat{P}=4$', color=GUIDE).scale(0.65).next_to(positive_ax.c2p(0, 4), LEFT, buff=0.20),
            DashedLine(positive_ax.c2p(0, 4), positive_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5)))
        # ---- 5.b · The same benefit appears above MB across the market.
        positive_graph = fixed(VGroup(positive_ax, positive_axis_words, positive_cost_bars, positive_ext_bars,
            positive_demand, positive_supply, positive_social_benefit, social_benefit_intercept, positive_curve_words, positive_market))
        positive_graph.shift(RIGHT * 3.7)
        positive_graph.scale(1.15, about_point=positive_ax.c2p(30, 7.5))
        left, right = 39 + BAR_GAP / 2, 40 - BAR_GAP / 2
        benefit_home = fixed(VGroup(
            Polygon(positive_ax.c2p(left, 0), positive_ax.c2p(right, 0),
                positive_ax.c2p(right, 12 - right / 5), positive_ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            positive_cost_bars[39].copy(), positive_ext_bars[39].copy()))
        self.play(FadeOut(benefit_edges), FadeOut(benefit_names), FadeOut(detached_name),
                  FadeOut(benefit_top), FadeOut(benefit_top_name), FadeOut(benefit_definition),
                  FadeOut(detail_people), FadeOut(unit_bystander), FadeOut(unit_bystander_word),
                  Transform(benefit_pair, benefit_home), FadeIn(positive_graph), run_time=1.6)
        self.remove(benefit_pair)
        self.pause('5.b')

        # ---- 5.c · Inspect private equilibrium with the two compact decisions.
        benefit_pair = benefit_home.copy()
        benefit_selection = fixed(SurroundingRectangle(benefit_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.play(FadeIn(benefit_pair), FadeIn(benefit_selection))
        self.play(FadeOut(positive_graph), FadeOut(positive_context), FadeOut(benefit_selection),
                  Transform(benefit_pair, benefit_target), run_time=1.4)
        benefit_context = fixed(subtitle(head, 'The 40th unit: the market equilibrium.'))
        benefit_numbers = fixed(VGroup(
            Tex(r'$\$4$', color=DEMAND).scale(0.72).next_to([-1.16, DETAIL_BASE + 4 * DETAIL_SCALE, 0], LEFT, buff=0.45),
            Tex(r'$\$6$', color=DEMAND).scale(0.72).next_to([-1.16, DETAIL_BASE + 6 * DETAIL_SCALE, 0], LEFT, buff=0.45),
            Tex(r'$\$4$', color=SUPPLY).scale(0.72).next_to([1.16, DETAIL_BASE + 4 * DETAIL_SCALE, 0], RIGHT, buff=0.25),
            DashedLine([-1.35, DETAIL_BASE + 4 * DETAIL_SCALE, 0], [-1.35, DETAIL_BASE + 6 * DETAIL_SCALE, 0], color=EXT, stroke_width=2.5),
            Tex(r'$\$2$', color=EXT).scale(0.72).next_to([-1.35, DETAIL_BASE + 5 * DETAIL_SCALE, 0], LEFT, buff=0.25)))
        detached_name.move_to(benefit_target[2])
        benefit_questions = fixed(VGroup(
            Tex('Will they exchange?', color=DEFINITION).scale(0.65).move_to([-5, 2.45, 0]),
            Tex('Is it good for society?', color=DEFINITION).scale(0.65).move_to([5, 2.45, 0])))
        self.play(FadeIn(benefit_edges), FadeIn(benefit_names), FadeIn(benefit_top), FadeIn(benefit_top_name),
                  FadeIn(detached_name), FadeIn(benefit_numbers), FadeIn(benefit_questions), FadeIn(benefit_context),
                  FadeIn(detail_people), FadeIn(unit_bystander), FadeIn(unit_bystander_word))
        self.pause('5.c.values')
        benefit_private_guides = fixed(DashedLine(benefit_numbers[0].get_left() + LEFT * 0.12,
            [-3.65, DETAIL_BASE + 4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4))
        benefit_private_answer = fixed(VGroup(Tex('Indifferent', color=INK), Tex(r'MB $=$ MC', color=TOTAL))
            .arrange(DOWN, buff=0.12).scale(0.65).next_to([-3.65, DETAIL_BASE + 4 * DETAIL_SCALE, 0], LEFT, buff=0.3))
        self.play(FadeIn(benefit_private_guides), FadeIn(benefit_private_answer[1]))
        self.pause('5.c.private.compare')
        self.play(FadeIn(benefit_private_answer[0]))
        self.pause('5.c.private')
        benefit_social_guides = fixed(VGroup(
            DashedLine([-0.06, DETAIL_BASE + 6 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            DashedLine(benefit_numbers[2].get_right() + RIGHT * 0.12, [3.65, DETAIL_BASE + 4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.4),
            Line([3.65, DETAIL_BASE + 4 * DETAIL_SCALE, 0], [3.65, DETAIL_BASE + 6 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3)))
        benefit_social_answer = fixed(VGroup(
            VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]),
            Tex(r'MSB $>$ MC', color=TOTAL), Tex(r'TS $=\$2$', color=TOTAL), Tex(r'DWL $=\$0$', color=INK))
            .arrange(DOWN, buff=0.1, aligned_edge=LEFT).scale(0.60)
            .next_to([3.65, DETAIL_BASE + 5 * DETAIL_SCALE, 0], RIGHT, buff=0.3))
        self.play(FadeIn(benefit_social_guides), FadeIn(benefit_social_answer[1]))
        self.pause('5.c.social.compare')
        self.play(FadeIn(benefit_social_answer[0]), FadeIn(benefit_social_answer[2:]))
        self.pause('5.c.social')
        self.play(FadeOut(benefit_edges), FadeOut(benefit_names), FadeOut(benefit_top), FadeOut(benefit_top_name),
                  FadeOut(detached_name), FadeOut(benefit_numbers), FadeOut(benefit_questions), FadeOut(benefit_context),
                  FadeOut(benefit_private_guides), FadeOut(benefit_private_answer), FadeOut(benefit_social_guides), FadeOut(benefit_social_answer),
                  FadeOut(detail_people), FadeOut(unit_bystander), FadeOut(unit_bystander_word),
                  Transform(benefit_pair, benefit_home), FadeIn(positive_graph), FadeIn(positive_context), run_time=1.4)
        self.remove(benefit_pair)

        # ---- 5.d · Sweep through forgone social gains, then conclude with quantities.
        positive_q = ValueTracker(40)
        positive_guide = fixed(DashedLine(positive_ax.c2p(40, 0), positive_ax.c2p(40, 6), color=FOCUS, stroke_width=2).set_z_index(2))
        positive_guide.axes, positive_guide.quantity = positive_ax, positive_q
        positive_guide.add_updater(lambda m: m.put_start_and_end_on(
            m.axes.c2p(m.quantity.get_value(), 0), m.axes.c2p(m.quantity.get_value(), 14 - m.quantity.get_value() / 5)))
        positive_losses = fixed(VGroup())
        for q in range(40, 48):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            loss_bar = fixed(Polygon(positive_ax.c2p(left, 2 + left / 20), positive_ax.c2p(right, 2 + right / 20),
                positive_ax.c2p(right, 14 - right / 5), positive_ax.c2p(left, 14 - left / 5),
                stroke_width=0, fill_color=DWL, fill_opacity=0).set_z_index(1))
            loss_bar.quantity, loss_bar.slice_left, loss_bar.slice_right = positive_q, left, right
            loss_bar.add_updater(lambda m: m.set_fill(opacity=0.8 * np.clip(
                (m.quantity.get_value() - m.slice_left) / (m.slice_right - m.slice_left), 0, 1)))
            positive_losses.add(loss_bar)
        positive_note = fixed(Tex('The market leaves out worthwhile exchanges, creating deadweight loss.', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.add(positive_losses)
        self.play(FadeIn(positive_guide), FadeIn(positive_note))
        self.play(positive_q.animate.set_value(48), run_time=2.4, rate_func=smooth)
        positive_guide.clear_updaters()
        for loss_bar in positive_losses:
            loss_bar.clear_updaters()
        positive_efficient = fixed(VGroup(Dot(positive_ax.c2p(48, 4.4), radius=0.085, color=FOCUS),
            VGroup(Tex(r'$Q^*$', color=FOCUS), Tex('$48$', color=FOCUS)).arrange(DOWN, buff=0.06).scale(0.65)
                .next_to(positive_ax.c2p(48, 0), DOWN, buff=0.20)))
        positive_efficient[1][1].set_y(positive_market[2][1].get_y())
        positive_dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(positive_losses, UP, buff=0.16))
        self.play(FadeIn(positive_efficient), FadeIn(positive_dwl_word))
        self.pause('5.d')
        positive_final_graph = fixed(VGroup(positive_graph, positive_losses, positive_guide, positive_efficient, positive_dwl_word))
        self.play(positive_final_graph.animate.shift(LEFT * 2.5), FadeOut(positive_note), run_time=1.2)
        positive_quantity_result = fixed(VGroup(Tex(r'$\hat{Q}$', color=GUIDE), Tex('$<$', color=INK), Tex(r'$Q^*$', color=FOCUS))
            .scale(1.3).arrange(RIGHT, buff=1.0).move_to([3.5, 1.9, 0]))
        positive_comparison = fixed(VGroup(positive_quantity_result,
            Tex('Market quantity', color=CAPTION).scale(0.7).next_to(positive_quantity_result, DOWN, buff=0.22).set_x(positive_quantity_result[0].get_x()),
            Tex('Efficient quantity', color=CAPTION).scale(0.7).next_to(positive_quantity_result, DOWN, buff=0.22).set_x(positive_quantity_result[2].get_x())))
        positive_conclusion = fixed(Tex('Markets for goods with positive externalities produce too little.', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(positive_comparison), FadeIn(positive_conclusion))
        self.pause('5.conclusion')
