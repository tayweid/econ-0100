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

        # Prepare the first lot and the exact marginal boundary on a common scale.
        head = fixed(title('Competitive equilibrium'))
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
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73)))
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
                [3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([3.25, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0], [3.8, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0],
                color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$2$', color=TOTAL).scale(0.8)
                .next_to([3.8, DETAIL_BASE + 3.4 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MC $>$ MB', color=INK).scale(0.8)))
        extra_detail[-1].next_to(extra_detail[-2], DOWN, buff=0.2)
        conclusion = fixed(Tex('This added ton costs more than it benefits.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('Can any price make this trade worthwhile?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        extra_detail[3].bars = extra_detail[4].bars = extra_pair
        extra_detail[3].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        extra_detail[4].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head,
            'The 48th unit: a quantity larger than in equilibrium.', book=True))
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
                [3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([3.25, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0],
                [3.8, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([3.8, DETAIL_BASE + 3.8 * DETAIL_SCALE, 0], [3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                color=TOTAL, stroke_width=3),
            Tex(r'TS $=+\$1$', color=TOTAL).scale(0.8)
                .next_to([3.8, DETAIL_BASE + 4.3 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MB $>$ MC', color=INK).scale(0.8).move_to([4.3, -0.1, 0])))
        conclusion = fixed(Tex('Removing this ton loses more benefit than it saves in cost.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('Would removing this ton improve welfare?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        removed_detail[3].bars = removed_detail[4].bars = removed_pair
        removed_detail[3].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        removed_detail[4].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        unit_context = fixed(subtitle(head,
            'The 36th unit: a quantity exchanged in equilibrium.', book=True))
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
        head = fixed(title('Negative externalities'))
        negative_context = fixed(subtitle(head, 'A cost paid by others outside the market.', book=True))
        PAIR_BASE, PAIR_SCALE, PAIR_WIDTH = -1.65, 0.58, 0.95
        # Exact averages for the representative market interval 29–30.
        PAIR_MB, PAIR_MC = 6.1, 3.475
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

        # ---- 2.b · A single external-cost piece belongs to one grey bystander.
        BYSTANDER_CENTER, BYSTANDER_GAP = 3.7, 0.61
        bystanders = fixed(Group())
        individual_costs, external_stack = fixed(VGroup()), fixed(VGroup())
        for i in range(8):
            x = BYSTANDER_CENTER
            person = fixed(Group(
                Ellipse(width=0.27, height=0.04, stroke_width=0, fill_color=MUTED, fill_opacity=0.35).move_to([x, -2.28, 0]),
                Sphere(radius=0.12, color=MUTED, opacity=1, resolution=(24, 16)).move_to([x, -2.10, 0])))
            person[1].apply_depth_test()
            bystanders.add(person)
            lower = PAIR_BASE + i * 0.25 * PAIR_SCALE
            external_stack.add(fixed(Polygon([3.05, lower, 0], [4.35, lower, 0],
                [4.35, lower + 0.25 * PAIR_SCALE, 0], [3.05, lower + 0.25 * PAIR_SCALE, 0],
                stroke_width=1, stroke_color=BG, fill_color=EXT, fill_opacity=0.65)))
            individual_costs.add(external_stack[-1].copy().stretch_to_fit_width(0.46)
                .move_to([x, PAIR_BASE + 0.125 * PAIR_SCALE, 0]))
        bystander_word = fixed(Tex('Bystander', color=CAPTION).scale(0.7).move_to([BYSTANDER_CENTER, -2.8, 0]))
        small_word = fixed(Tex(r'External cost: $\$0.25$/ton', color=EXT).scale(0.7).move_to([BYSTANDER_CENTER, 0.55, 0]))
        self.add(bystanders[0])
        self.play(FadeIn(bystander_word), FadeIn(individual_costs[0]), FadeIn(small_word))
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
        stack_word = fixed(Tex(r'$8\times\$0.25=\$2$/ton', color=EXT).scale(0.8).move_to([3.7, 0.55, 0]))
        conclusion = fixed(VGroup(
            Tex('Exchanges between buyer and seller in the market', color=DEFINITION).scale(DEFINITION_SCALE),
            Tex('can impose a cost on others.', color=DEFINITION).scale(DEFINITION_SCALE))
            .arrange(DOWN, buff=0.12).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(stack_word), FadeIn(conclusion))
        self.pause('2.c')

        # ---- 2.d · The stack becomes the external-cost area of one trade.
        ext_ax = fixed(style_axes([0, 2.5, 1], [0, 3, 1], x_length=4.3, y_length=2.2))
        ext_ax.shift(np.array([1.3, -1.5, 0]) - ext_ax.c2p(0, 0))
        ext_words = fixed(VGroup(
            Tex('External cost per ton', color=CAPTION).scale(0.65).next_to(ext_ax, UP, buff=0.20),
            Tex(r'$\$2$', color=EXT).scale(0.7).next_to(ext_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('1', color=GUIDE).scale(0.7).next_to(ext_ax.c2p(1, 0), DOWN, buff=0.18),
            Tex('Tons', color=CAPTION).scale(0.60).next_to(ext_ax, DOWN, buff=0.65)))
        ext_parts = fixed(VGroup())
        for i in range(8):
            ext_parts.add(fixed(Polygon(ext_ax.c2p(0, i * 0.25), ext_ax.c2p(1, i * 0.25),
                ext_ax.c2p(1, (i + 1) * 0.25), ext_ax.c2p(0, (i + 1) * 0.25),
                stroke_width=1, stroke_color=BG, fill_color=EXT, fill_opacity=0.65)))
        self.play(FadeOut(stack_word), FadeOut(bystander_word), FadeOut(conclusion),
                  bystanders.animate.scale(0.8).move_to([3.45, -2.85, 0]), FadeIn(ext_ax), FadeIn(ext_words),
                  *[Transform(external_stack[i], ext_parts[i]) for i in range(8)], run_time=1.5)
        ext_area_word = fixed(Tex(r'$\$2$', color=INK).scale(0.8).move_to(ext_ax.c2p(0.5, 1)))
        self.play(FadeIn(ext_area_word))
        self.pause('2.d')

        # ---- 2.e · Two actual bar pairs, two external-cost rectangles.
        first_small = pair.copy().scale(0.66).move_to([-5.25, BODY_MID, 0])
        second_pair = first_small.copy().shift(RIGHT * 2.9)
        # Same geometry and units, next market interval 30–31.
        second_bars = second_pair[0]
        for index, value, color in [(0, 5.9, DEMAND), (1, 3.525, SUPPLY)]:
            left = second_bars[index].get_left()[0]
            right = second_bars[index].get_right()[0]
            base = second_bars[index].get_bottom()[1]
            lower, upper = (MARKET_P, value) if index == 0 else (value, MARKET_P)
            second_bars[index].stretch_to_fit_height(PAIR_SCALE * 0.66 * lower, about_edge=DOWN)
            second_bars[index + 2].become(fixed(Polygon(
                [left, base + lower * PAIR_SCALE * 0.66, 0], [right, base + lower * PAIR_SCALE * 0.66, 0],
                [right, base + upper * PAIR_SCALE * 0.66, 0], [left, base + upper * PAIR_SCALE * 0.66, 0],
                stroke_width=0, fill_color=color, fill_opacity=SURPLUS_OPACITY)))
            second_bars[index + 4].become(fixed(Line(
                [left, base + value * PAIR_SCALE * 0.66, 0], [right, base + value * PAIR_SCALE * 0.66, 0],
                color=color, stroke_width=3)))
        second_words = second_pair[2]
        for index, text_value in [(0, 'Buyer'), (1, r'MB $\$5.90$'), (2, 'Seller'), (3, r'MC $\$3.525$')]:
            replacement = fixed(Tex(text_value, color=INK if index % 2 == 0 else (DEMAND if index == 1 else SUPPLY))
                                .scale((0.7 if index % 2 == 0 else 0.65) * 0.66).move_to(second_words[index]))
            second_words[index].become(replacement)
        second_words[1].next_to(second_bars[4], LEFT, buff=0.22 * 0.66)
        second_words[3].next_to(second_bars[5], RIGHT, buff=0.22 * 0.66)
        second_ext = fixed(Polygon(ext_ax.c2p(1, 0), ext_ax.c2p(2, 0), ext_ax.c2p(2, 2), ext_ax.c2p(1, 2),
            stroke_width=1.5, stroke_color=BG, fill_color=EXT, fill_opacity=0.65))
        second_ext_word = fixed(Tex(r'$\$2$', color=INK).scale(0.8).move_to(ext_ax.c2p(1.5, 1)))
        second_tick = fixed(Tex('2', color=GUIDE).scale(0.7).next_to(ext_ax.c2p(2, 0), DOWN, buff=0.18))
        second_material = fixed(Group(second_pair[0], *list(second_pair)[2:]))
        self.add(second_pair[1])
        self.play(Transform(pair, first_small), FadeIn(second_material), FadeIn(second_ext),
                  FadeIn(second_ext_word), FadeIn(second_tick), run_time=1.6)
        self.remove(second_pair[1], second_material)
        self.add(second_pair)
        self.pause('2.e')

        # ---- 2.f · Both trades land at their own ranks in the complete market.
        left_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        left_ax.shift(np.array([-6.45, -2.15, 0]) - left_ax.c2p(0, 0))
        right_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        right_ax.shift(np.array([1.25, -2.15, 0]) - right_ax.c2p(0, 0))
        left_words = fixed(VGroup(
            Tex(r'\textsf{\$/ton}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(0, 13), UP, buff=0.16),
            Tex('Q', color=INK).scale(0.7).next_to(left_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(45, 0), DOWN, buff=0.7)))
        right_words = fixed(VGroup(
            Tex('External cost per ton', color=CAPTION).scale(0.65).next_to(right_ax.c2p(30, 13), UP, buff=0.16),
            Tex(r'$\$2$', color=EXT).scale(0.65).next_to(right_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('Q', color=INK).scale(0.7).next_to(right_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{tons}', color=CAPTION).scale(0.55).next_to(right_ax.c2p(45, 0), DOWN, buff=0.7),
            Tex(r'$Q=40$', color=GUIDE).scale(0.65).next_to(right_ax.c2p(40, 0), DOWN, buff=0.18)))
        left_demand = fixed(Line(left_ax.c2p(0, 12), left_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        left_supply = fixed(Line(left_ax.c2p(0, 2), left_ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        left_curve_words = fixed(VGroup(
            Tex('MB', color=INK).scale(0.7).next_to(left_ax.c2p(8, 10.4), UR, buff=0.1),
            Tex('MC', color=INK).scale(0.7).next_to(left_ax.c2p(60, 5), RIGHT, buff=0.12)))
        left_eq = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.06, color=GUIDE),
            DashedLine(left_ax.c2p(0, 4), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            Tex(r'$Q_m=40$', color=GUIDE).scale(0.65).next_to(left_ax.c2p(40, 0), DOWN, buff=0.18)))
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
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        landing_pairs = []
        for q in [29, 30]:
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            # Match all six pieces to the existing stacked market geometry.
            landing_pairs.append(fixed(VGroup(
                Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                    left_ax.c2p(right, 4), left_ax.c2p(left, 4),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0),
                private_bars[q].copy(), benefit_bars[q].copy(), producer_surplus[q].copy(),
                Line(left_ax.c2p(left, 12 - left / 5), left_ax.c2p(right, 12 - right / 5),
                    color=DEMAND, stroke_width=3),
                Line(left_ax.c2p(left, 2 + left / 20), left_ax.c2p(right, 2 + right / 20),
                    color=SUPPLY, stroke_width=3))))
        # Separate bars from their departing people so the bars survive the pullback.
        first_flying, second_flying = pair[0].copy(), second_pair[0].copy()
        self.add(first_flying, second_flying)
        # The topic is unchanged as the two trades become the full market.
        pair_material = fixed(Group(pair[0], *list(pair)[2:]))
        self.remove(pair, second_pair, bystanders)
        self.add(pair_material, second_material)
        self.play(FadeOut(pair_material), FadeOut(second_material),
                  FadeOut(ext_ax), FadeOut(ext_words), FadeOut(ext_area_word), FadeOut(second_ext_word), FadeOut(second_tick),
                  Transform(first_flying, landing_pairs[0]), Transform(second_flying, landing_pairs[1]),
                  Transform(external_stack, fixed(VGroup(external_bars[29].copy()))),
                  Transform(second_ext, external_bars[30]),
                  FadeIn(left_ax), FadeIn(right_ax), FadeIn(left_words), FadeIn(right_words),
                  FadeIn(left_demand), FadeIn(left_supply), FadeIn(left_curve_words), FadeIn(left_eq), run_time=2)
        self.play(FadeIn(private_bars), FadeIn(benefit_bars), FadeIn(producer_surplus),
                  LaggedStart(*[FadeIn(bar) for bar in external_bars], lag_ratio=0.02), run_time=1.4)
        self.remove(first_flying, second_flying, external_stack, second_ext)
        ext_total_word = fixed(Tex(r'Total external cost: $\$80$', color=EXT).scale(0.75)
                               .move_to([3.9, 0.3, 0]))
        self.play(FadeIn(ext_total_word))
        self.pause('2.f')

        # ---- 3.a · Strip away benefit to account for every cost.
        self.remove(head, negative_context)
        head = fixed(title('Marginal social cost'))
        cost_question = fixed(Tex('What is the full cost of a trade?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(cost_question), FadeOut(left_demand), FadeOut(benefit_bars), FadeOut(producer_surplus),
                  FadeOut(left_curve_words[0]), FadeOut(left_eq), FadeOut(ext_total_word))
        self.pause('3.a')

        # ---- 3.b · Transfer the actual external-cost strips onto private cost.
        stacked_targets = fixed(VGroup())
        for q in range(40):
            l, r = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            stacked_targets.add(fixed(Polygon(left_ax.c2p(l, 2 + l / 20), left_ax.c2p(r, 2 + r / 20),
                left_ax.c2p(r, 4 + r / 20), left_ax.c2p(l, 4 + l / 20),
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        self.play(LaggedStart(*[Transform(external_bars[q], stacked_targets[q]) for q in range(40)],
                            lag_ratio=0.045), run_time=3)
        potential_ext = fixed(VGroup())
        for q in range(40, 60):
            l, r = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            potential_ext.add(fixed(Polygon(left_ax.c2p(l, 2 + l / 20), left_ax.c2p(r, 2 + r / 20),
                left_ax.c2p(r, 4 + r / 20), left_ax.c2p(l, 4 + l / 20),
                stroke_width=0, fill_color=EXT, fill_opacity=0.12)))
        social_cost = fixed(DashedLine(left_ax.c2p(0, 4), left_ax.c2p(60, 7), color=SUPPLY, stroke_width=3))
        social_word = fixed(Tex('MSC', color=INK).scale(0.7).next_to(left_ax.c2p(60, 7), RIGHT, buff=0.12))
        cost_definition = fixed(Tex('MSC $=$ MC $+$ Ext.', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(cost_question)
        self.play(FadeOut(right_ax), FadeOut(right_words), FadeIn(potential_ext),
                  FadeIn(social_cost), FadeIn(social_word), FadeIn(cost_definition))
        self.pause('3.b')

        # ---- 3.c · Recenter, restore demand, and mark the unchanged market outcome.
        cost_graph = fixed(VGroup(left_ax, left_words, private_bars, external_bars, potential_ext,
                                 left_supply, left_curve_words[1], social_cost, social_word))
        self.remove(*[m for m in self.mobjects if m is not head and m is not cost_definition])
        self.add(cost_graph, head, cost_definition)
        self.play(cost_graph.animate.shift(RIGHT * 3.7), run_time=1.1)
        self.play(cost_graph.animate.scale(1.15, about_point=left_ax.c2p(30, 6.5)), run_time=0.8)
        # Keep the axes' numerical mappings live after the group moves.
        full_demand = fixed(Line(left_ax.c2p(0, 12), left_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        demand_word = fixed(Tex('MB', color=INK).scale(0.7).next_to(left_ax.c2p(7, 10.6), UR, buff=0.12))
        market_reference = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.065, color=GUIDE),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            Tex(r'$Q_m=40$', color=GUIDE).scale(0.7).next_to(left_ax.c2p(40, 0), DOWN, buff=0.20),
            Tex(r'$P_m=4$', color=GUIDE).scale(0.7).next_to(left_ax.c2p(40, 4), DOWN + RIGHT, buff=0.14)))
        self.remove(head, cost_definition)
        head = fixed(title('Social welfare'))
        question = fixed(Tex('Would increasing or decreasing quantity improve welfare?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(full_demand), FadeIn(demand_word), FadeIn(market_reference), FadeIn(question))
        social_graph = fixed(VGroup(cost_graph, full_demand, demand_word, market_reference))
        self.remove(cost_graph, full_demand, demand_word, market_reference)
        self.add(social_graph)
        self.pause('3.c')

        # ---- 3.d · Revisit the same added ton, with external cost stacked on MC.
        left, right = COMPARE_HIGH - 1 + BAR_GAP / 2, COMPARE_HIGH - BAR_GAP / 2
        extra_social_pair = fixed(VGroup(
            Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                left_ax.c2p(right, 12 - right / 5), left_ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            Polygon(left_ax.c2p(left, 0), left_ax.c2p(right, 0),
                left_ax.c2p(right, 2 + right / 20), left_ax.c2p(left, 2 + left / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=BASE_OPACITY),
            Polygon(left_ax.c2p(left, 2 + left / 20), left_ax.c2p(right, 2 + right / 20),
                left_ax.c2p(right, 4 + right / 20), left_ax.c2p(left, 4 + left / 20),
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        extra_social_home = extra_social_pair.copy()
        selected_ton = fixed(SurroundingRectangle(extra_social_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(question)
        self.play(FadeIn(extra_social_pair), FadeIn(selected_ton))
        self.pause('3.d.select')
        extra_social_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 2.4, DEMAND), (0.06, 0, 4.4, SUPPLY),
                                      (0.06, 4.4, 6.4, EXT)]:
            extra_social_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65 if color == EXT else BASE_OPACITY)))
        private_target = extra_social_target.copy()
        private_target[2].set_opacity(0)
        self.play(FadeOut(social_graph), FadeOut(selected_ton),
                  Transform(extra_social_pair, private_target), run_time=1.6)
        extra_social_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(extra_social_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$2.40$', color=DEMAND).scale(0.72).next_to(extra_social_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$4.40$', color=SUPPLY).scale(0.72).next_to(extra_social_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'External cost $\$2$', color=EXT).scale(0.72).next_to(extra_social_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$6.40$', color=SUPPLY).scale(0.72).next_to(extra_social_target[2].get_corner(UR), RIGHT, buff=0.25)))
        social_gap = fixed(VGroup(
            DashedLine([-3.55, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([0.06, DETAIL_BASE + 6.4 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 6.4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([-3.8, DETAIL_BASE + 2.4 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 6.4 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$4$', color=TOTAL).scale(0.8)
                .next_to([-3.8, DETAIL_BASE + 4.4 * DETAIL_SCALE, 0], LEFT, buff=0.3)))
        conclusion = fixed(Tex('Adding this ton reduces social welfare.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('What do the buyer and seller count?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        extra_social_labels[4].bars = extra_social_labels[5].bars = extra_social_pair
        extra_social_labels[4].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        extra_social_labels[5].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        private_labels = fixed(VGroup(*[extra_social_labels[i] for i in [0, 1, 3, 4, 5]]))
        external_labels = fixed(VGroup(*[extra_social_labels[i] for i in [2, 6, 7]]))
        unit_context = fixed(subtitle(head,
            'The 48th unit: a quantity larger than in equilibrium.', book=True))
        self.add(detail_people)
        self.play(FadeIn(private_labels), FadeIn(value_question), FadeIn(unit_context))
        self.pause('3.d.values')
        self.remove(value_question)
        value_question = fixed(Tex('What changes when we count the external cost?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(Transform(extra_social_pair, extra_social_target), FadeIn(external_labels), FadeIn(value_question))
        self.pause('3.d.costs')
        self.play(FadeOut(value_question))
        self.play(FadeIn(social_gap), FadeIn(conclusion))
        self.pause('3.d')
        self.remove(detail_people)
        self.play(FadeOut(extra_social_labels, suspend_mobject_updating=False), FadeOut(social_gap), FadeOut(conclusion), FadeOut(unit_context),
                  Transform(extra_social_pair, extra_social_home), FadeIn(social_graph), run_time=1.6)
        self.play(FadeOut(extra_social_pair))
        self.pause('3.d.return')

        # ---- 3.e · Revisit the same removed ton, with external cost stacked on MC.
        removed_social_pair = fixed(VGroup(
            Polygon(*private_bars[COMPARE_LOW].get_vertices()[:2],
                left_ax.c2p(COMPARE_LOW + 1 - BAR_GAP / 2, 12 - (COMPARE_LOW + 1 - BAR_GAP / 2) / 5),
                left_ax.c2p(COMPARE_LOW + BAR_GAP / 2, 12 - (COMPARE_LOW + BAR_GAP / 2) / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0),
            private_bars[COMPARE_LOW].copy(), external_bars[COMPARE_LOW].copy()))
        removed_social_home = removed_social_pair.copy()
        selected_ton = fixed(SurroundingRectangle(removed_social_pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(question)
        self.play(FadeIn(removed_social_pair), FadeIn(selected_ton))
        self.pause('3.e.select')
        removed_social_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 4.8, DEMAND), (0.06, 0, 3.8, SUPPLY),
                                      (0.06, 3.8, 5.8, EXT)]:
            removed_social_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65 if color == EXT else BASE_OPACITY)))
        private_target = removed_social_target.copy()
        private_target[2].set_opacity(0)
        self.play(FadeOut(social_graph), FadeOut(selected_ton),
                  Transform(removed_social_pair, private_target), run_time=1.6)
        removed_social_labels = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(removed_social_target, [DEMAND, SUPPLY, SUPPLY])],
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$4.80$', color=DEMAND).scale(0.72).next_to(removed_social_target[0].get_corner(UL), LEFT, buff=0.25),
            Tex(r'MC $\$3.80$', color=SUPPLY).scale(0.72).next_to(removed_social_target[1].get_corner(UR), RIGHT, buff=0.25),
            Tex(r'External cost $\$2$', color=EXT).scale(0.72).next_to(removed_social_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$5.80$', color=SUPPLY).scale(0.72).next_to(removed_social_target[2].get_corner(UR), RIGHT, buff=0.25)))
        social_gap = fixed(VGroup(
            DashedLine([-3.55, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([0.06, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([-3.8, DETAIL_BASE + 4.8 * DETAIL_SCALE, 0],
                [-3.8, DETAIL_BASE + 5.8 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$1$', color=TOTAL).scale(0.8)
                .next_to([-3.8, DETAIL_BASE + 5.3 * DETAIL_SCALE, 0], LEFT, buff=0.3)))
        conclusion = fixed(Tex('Removing this ton increases social welfare.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        value_question = fixed(Tex('What do the buyer and seller count?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        removed_social_labels[4].bars = removed_social_labels[5].bars = removed_social_pair
        removed_social_labels[4].add_updater(lambda m:
            m.next_to(m.bars[0].get_corner(UL), LEFT, buff=0.25))
        removed_social_labels[5].add_updater(lambda m:
            m.next_to(m.bars[1].get_corner(UR), RIGHT, buff=0.25))
        private_labels = fixed(VGroup(*[removed_social_labels[i] for i in [0, 1, 3, 4, 5]]))
        external_labels = fixed(VGroup(*[removed_social_labels[i] for i in [2, 6, 7]]))
        unit_context = fixed(subtitle(head,
            'The 36th unit: a quantity exchanged in equilibrium.', book=True))
        self.add(detail_people)
        self.play(FadeIn(private_labels), FadeIn(value_question), FadeIn(unit_context))
        self.pause('3.e.values')
        self.remove(value_question)
        value_question = fixed(Tex('What changes when we count the external cost?', color=DEFINITION)
            .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(Transform(removed_social_pair, removed_social_target), FadeIn(external_labels), FadeIn(value_question))
        self.pause('3.e.costs')
        self.play(FadeOut(value_question))
        self.play(FadeIn(social_gap), FadeIn(conclusion))
        self.pause('3.e')
        self.remove(detail_people)
        self.play(FadeOut(removed_social_labels, suspend_mobject_updating=False), FadeOut(social_gap), FadeOut(conclusion), FadeOut(unit_context),
                  Transform(removed_social_pair, removed_social_home), FadeIn(social_graph), run_time=1.6)
        self.play(FadeOut(removed_social_pair))
        self.pause('3.e.return')

        # ---- 4.a · Legacy social-planner sequence: change the evaluated Q only.
        self.remove(head)
        head = fixed(title('Efficient quantity'))
        evaluation_q = ValueTracker(40)
        evaluation_line = fixed(Line(left_ax.c2p(40, 0), left_ax.c2p(40, 6), color=FOCUS, stroke_width=2))
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
        self.play(FadeIn(head), FadeIn(evaluation_line), FadeIn(marginal_gap))
        self.play(evaluation_q.animate.set_value(EFFICIENT_Q), run_time=2.4, rate_func=smooth)
        efficient_dot = fixed(Dot(left_ax.c2p(32, 5.6), radius=0.085, color=FOCUS))
        efficient_word = fixed(Tex(r'$Q_e=32$', color=FOCUS).scale(0.7)
                               .next_to(left_ax.c2p(32, 0), DOWN, buff=0.78))
        # Vertically stagger quantity labels so 32 and 40 are both readable.
        condition = fixed(Tex('Social welfare is maximized where MB $=$ MSC.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(efficient_dot), FadeIn(efficient_word), FadeIn(condition), FadeOut(marginal_gap))
        self.pause('4.a')

        # ---- 4.b · The losses from excessive trades; not all external damage.
        self.remove(head)
        head = fixed(title('Deadweight loss'))
        self.play(FadeIn(head))
        loss_slices = fixed(VGroup())
        for q in range(32, 40):
            loss_slices.add(fixed(Polygon(left_ax.c2p(q, 12 - q / 5), left_ax.c2p(q + 1, 12 - (q + 1) / 5),
                left_ax.c2p(q + 1, 4 + (q + 1) / 20), left_ax.c2p(q, 4 + q / 20),
                stroke_width=1, stroke_color=BG, fill_color=DWL, fill_opacity=0.8)))
        self.remove(condition)
        self.play(external_bars.animate.set_fill(opacity=0.18),
                  LaggedStart(*[FadeIn(bar) for bar in loss_slices], lag_ratio=0.18), run_time=2)
        dwl_triangle = fixed(Polygon(left_ax.c2p(32, 5.6), left_ax.c2p(40, 4), left_ax.c2p(40, 6),
            stroke_width=0, fill_color=DWL, fill_opacity=0.8))
        self.play(Transform(loss_slices, fixed(VGroup(dwl_triangle))), run_time=0.8)
        dwl_word = fixed(Tex('DWL', color=INK).scale(0.8).next_to(left_ax.c2p(40, 5.4), RIGHT, buff=0.3))
        conclusion = fixed(Tex('These trades cost society more than they benefit society.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(dwl_word), FadeIn(conclusion))
        self.pause('4.b')

        # ---- 4.c · The efficient quantity is positive despite the remaining harm.
        self.remove(head, conclusion)
        head = fixed(title('Efficient quantity'))
        self.play(FadeIn(head))
        conclusion = fixed(Tex('Some production is worthwhile even when it causes harm.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(evaluation_q.animate.set_value(24), FadeIn(conclusion), run_time=1.8)
        benefit_gap = fixed(Line(left_ax.c2p(24, 5.2), left_ax.c2p(24, 7.2), color=TOTAL, stroke_width=7))
        benefit_word = fixed(Tex('MB $>$ MSC', color=TOTAL).scale(0.72).next_to(benefit_gap, LEFT, buff=0.25))
        self.play(FadeIn(benefit_gap), FadeIn(benefit_word))
        self.pause('4.c.beneficial')
        self.play(FadeOut(benefit_gap), FadeOut(benefit_word), evaluation_q.animate.set_value(32), run_time=1.8)
        self.pause('4.c')
