# maniml C1_Animations.py C1
# Storyboard: C1_Notes.typ. All lesson choreography stays in construct().
# Part B's continuous spinach market; one Q step is a 1,000-pound lot.
# Close-up MB/MC rectangles use exact interval averages, not endpoint samples.

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
        LOT_POUNDS = 1000
        BAR_GAP = 0.08
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.68

        # ---- 1.a · B4/B5 market, then consumer surplus, then producer surplus.
        head = fixed(title('Could one more trade improve welfare?'))
        ax = style_axes([0, 60, 10], [0, 13, 2], x_length=10, y_length=4.6)
        ax.shift(np.array([-5, BODY_MID - 2.15, 0]) - ax.c2p(0, 0))
        fixed(ax)
        axis_words = fixed(VGroup(
            Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.23),
            Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, 13), UP, buff=0.18),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{1,000 lb}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73)))
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
        cs, ps = fixed(VGroup()), fixed(VGroup())
        for q in range(MARKET_Q):
            left, right = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            cs.add(fixed(Polygon(ax.c2p(left, 4), ax.c2p(right, 4),
                ax.c2p(right, 12 - right / 5), ax.c2p(left, 12 - left / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=AREA_OPACITY)))
            ps.add(fixed(Polygon(ax.c2p(left, 2 + left / 20), ax.c2p(right, 2 + right / 20),
                ax.c2p(right, 4), ax.c2p(left, 4),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=AREA_OPACITY)))
        surplus_words = fixed(VGroup(
            Tex('Consumer surplus', color=DEMAND).scale(0.72).move_to(ax.c2p(13, 6.3)),
            Tex('Producer surplus', color=SUPPLY).scale(0.72).move_to(ax.c2p(14, 3.25))))
        self.play(FadeIn(head), FadeIn(ax), FadeIn(axis_words), FadeIn(demand), FadeIn(supply),
                  FadeIn(curve_words), FadeIn(equilibrium), FadeIn(quantity_guide), FadeIn(quantity_label))
        self.play(FadeIn(cs), FadeIn(surplus_words[0]))
        self.play(FadeIn(ps), FadeIn(surplus_words[1]))
        market = fixed(VGroup(ax, axis_words, cs, ps, demand, supply, curve_words,
                             equilibrium, quantity_guide, quantity_label, surplus_words))
        self.remove(*[m for m in self.mobjects if m is not head])
        self.add(market, head)
        self.pause('1.a')

        # ---- 1.b · Add one full interval, 40–41. This is a quantity experiment.
        extra_loss = fixed(Polygon(ax.c2p(40, 4), ax.c2p(41, 3.8), ax.c2p(41, 4.05),
            stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY))
        extra_pair = fixed(VGroup(
            Polygon(ax.c2p(40.04, 0), ax.c2p(40.47, 0), ax.c2p(40.47, 3.9), ax.c2p(40.04, 3.9),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.65),
            Polygon(ax.c2p(40.53, 0), ax.c2p(40.96, 0), ax.c2p(40.96, 4.025), ax.c2p(40.53, 4.025),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.65)))
        extra_home = extra_pair.copy()
        question = fixed(Tex('What happens if we increase quantity by one?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(Transform(quantity_guide, fixed(DashedLine(ax.c2p(41, 0), ax.c2p(41, 4.05), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=41$', color=GUIDE).scale(0.7).next_to(ax.c2p(41, 0), DOWN, buff=0.20))),
                  FadeIn(extra_loss), FadeIn(extra_pair), FadeIn(question))
        self.pause('1.b')

        # ---- 1.c · Carry the selected pair into B4's head-on bar comparison.
        extra_target = fixed(VGroup())
        for left, value, color in [(-1.16, 3.9, DEMAND), (0.06, 4.025, SUPPLY)]:
            extra_target.add(fixed(Polygon([left, DETAIL_BASE, 0], [left + 1.1, DETAIL_BASE, 0],
                [left + 1.1, DETAIL_BASE + value * DETAIL_SCALE, 0], [left, DETAIL_BASE + value * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65)))
        self.play(FadeOut(market), FadeOut(extra_loss), FadeOut(question),
                  Transform(extra_pair, extra_target), run_time=1.6, rate_func=smooth)
        detail_people = fixed(Group())
        for x, color in [(-1.45, DEMAND), (1.45, SUPPLY)]:
            detail_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([x, DETAIL_BASE - 0.60, 0])))
            detail_people.add(fixed(Sphere(radius=0.18, color=color, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
        extra_detail = fixed(VGroup(
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$3.90$', color=DEMAND).scale(0.72).next_to(extra_target[0], UP, buff=0.2).shift(LEFT * 0.3),
            Tex(r'MC $\$4.025$', color=SUPPLY).scale(0.72).next_to(extra_target[1], UP, buff=0.2).shift(RIGHT * 0.4),
            Tex('Average values per pound', color=CAPTION).scale(0.6).move_to([0, 1.75, 0]),
            Tex('One additional 1,000-pound lot', color=CAPTION).scale(0.65).move_to([0, -3.05, 0]),
            DashedLine([-0.06, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0],
                [2.1, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([1.16, DETAIL_BASE + 4.025 * DETAIL_SCALE, 0],
                [2.1, DETAIL_BASE + 4.025 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([2.1, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0], [2.1, DETAIL_BASE + 4.025 * DETAIL_SCALE, 0],
                color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$125$', color=TOTAL).scale(0.8)
                .next_to([2.1, DETAIL_BASE + 3.9625 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MC $>$ MB', color=INK).scale(0.8).move_to([4.3, -0.2, 0])))
        conclusion = fixed(Tex('One more trade adds more cost than benefit.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(extra_detail), FadeIn(detail_people), FadeIn(conclusion))
        self.pause('1.c')

        # ---- 1.d · Return the exact same pair to its original quantity interval.
        self.play(FadeOut(extra_detail), FadeOut(detail_people), FadeOut(conclusion),
                  Transform(extra_pair, extra_home), FadeIn(market), FadeIn(extra_loss), run_time=1.6)
        self.play(FadeOut(extra_pair), FadeOut(extra_loss),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20))))
        self.pause('1.d')

        # ---- 1.e · Remove the interval 39–40, whose integrated gain is positive.
        self.remove(head)
        head = fixed(title('Could one fewer trade improve welfare?'))
        self.play(FadeIn(head))
        lost_gain = fixed(Polygon(ax.c2p(39, 3.95), ax.c2p(40, 4), ax.c2p(39, 4.2),
            stroke_width=0, fill_color=DWL, fill_opacity=DWL_OPACITY))
        removed_pair = fixed(VGroup(
            Polygon(ax.c2p(39.04, 0), ax.c2p(39.47, 0), ax.c2p(39.47, 4.1), ax.c2p(39.04, 4.1),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.65),
            Polygon(ax.c2p(39.53, 0), ax.c2p(39.96, 0), ax.c2p(39.96, 3.975), ax.c2p(39.53, 3.975),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.65)))
        removed_home = removed_pair.copy()
        question = fixed(Tex('What happens if we decrease quantity by one?', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(cs[-1].animate.set_opacity(0.05), ps[-1].animate.set_opacity(0.05),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(39, 0), ax.c2p(39, 4.2), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=39$', color=GUIDE).scale(0.7).next_to(ax.c2p(39, 0), DOWN, buff=0.20))),
                  FadeIn(lost_gain), FadeIn(removed_pair), FadeIn(question))
        self.pause('1.e')

        # ---- 1.f · The same bar-pair zoom, now examining a forgone gain.
        removed_target = fixed(VGroup())
        for left, value, color in [(-1.16, 4.1, DEMAND), (0.06, 3.975, SUPPLY)]:
            removed_target.add(fixed(Polygon([left, DETAIL_BASE, 0], [left + 1.1, DETAIL_BASE, 0],
                [left + 1.1, DETAIL_BASE + value * DETAIL_SCALE, 0], [left, DETAIL_BASE + value * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65)))
        self.play(FadeOut(market), FadeOut(lost_gain), FadeOut(question),
                  Transform(removed_pair, removed_target), run_time=1.6)
        removed_detail = fixed(VGroup(
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MB $\$4.10$', color=DEMAND).scale(0.72).next_to(removed_target[0], UP, buff=0.2).shift(LEFT * 0.3),
            Tex(r'MC $\$3.975$', color=SUPPLY).scale(0.72).next_to(removed_target[1], UP, buff=0.2).shift(RIGHT * 0.4),
            Tex('Average values per pound', color=CAPTION).scale(0.6).move_to([0, 1.75, 0]),
            Tex('One removed 1,000-pound lot', color=CAPTION).scale(0.65).move_to([0, -3.05, 0]),
            DashedLine([-0.06, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0],
                [2.1, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([1.16, DETAIL_BASE + 3.975 * DETAIL_SCALE, 0],
                [2.1, DETAIL_BASE + 3.975 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([2.1, DETAIL_BASE + 3.975 * DETAIL_SCALE, 0], [2.1, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0],
                color=TOTAL, stroke_width=3),
            Tex(r'TS $=+\$125$', color=TOTAL).scale(0.8)
                .next_to([2.1, DETAIL_BASE + 4.0375 * DETAIL_SCALE, 0], RIGHT, buff=0.3),
            Tex(r'MB $>$ MC', color=INK).scale(0.8).move_to([4.3, -0.1, 0]),
            Tex(r'Removing it loses $\$125$.', color=CAPTION).scale(0.7).move_to([4.3, -0.75, 0])))
        conclusion = fixed(Tex('One fewer trade removes more benefit than cost.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(removed_detail), FadeIn(detail_people), FadeIn(conclusion))
        self.pause('1.f')

        # ---- 1.g · The exact marginal boundary, rather than an average bar height.
        self.play(FadeOut(removed_detail), FadeOut(detail_people), FadeOut(conclusion),
                  Transform(removed_pair, removed_home), FadeIn(market), FadeIn(lost_gain), run_time=1.6)
        self.play(FadeOut(removed_pair), FadeOut(lost_gain),
                  cs[-1].animate.set_fill(opacity=AREA_OPACITY), ps[-1].animate.set_fill(opacity=AREA_OPACITY),
                  Transform(quantity_guide, fixed(DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE))),
                  Transform(quantity_label, fixed(Tex(r'$Q=40$', color=GUIDE).scale(0.7).next_to(ax.c2p(40, 0), DOWN, buff=0.20))))
        boundary_dot = fixed(Dot(ax.c2p(40, 4), radius=0.09, color=FOCUS))
        boundary = fixed(Tex(r'At equilibrium, MB $=$ MC.', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(boundary_dot), FadeIn(boundary))
        self.pause('1.g.boundary')
        self.remove(head, boundary)
        head = fixed(title('The First Welfare Theorem'))
        theorem = fixed(VGroup(
            Tex('Competitive equilibrium maximizes total surplus.', color=DEFINITION).scale(DEFINITION_SCALE),
            Tex('All benefits and costs must be counted.', color=DEFINITION).scale(DEFINITION_SCALE))
            .arrange(DOWN, buff=0.12).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(theorem))
        self.pause('1.g')

        # ---- 2.a · Part B's head-on Gary/Molly deliberation, room for bystanders.
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.clear()
        head = fixed(title('Who else is affected by this trade?'))
        PAIR_BASE, PAIR_SCALE, PAIR_WIDTH = -1.65, 0.58, 0.95
        # Exact averages for the representative market interval 29–30.
        PAIR_MB, PAIR_MC = 6.1, 3.475
        pair_bars, pair_people, pair_words = fixed(VGroup()), fixed(Group()), fixed(VGroup())
        for left, value, color, name, person_x, term in [
            (-4.55, PAIR_MB, DEMAND, 'Gary', -4.9, 'MB'),
            (-3.48, PAIR_MC, SUPPLY, 'Molly', -2.15, 'MPC')]:
            pair_bars.add(fixed(Polygon([left, PAIR_BASE, 0], [left + PAIR_WIDTH, PAIR_BASE, 0],
                [left + PAIR_WIDTH, PAIR_BASE + value * PAIR_SCALE, 0], [left, PAIR_BASE + value * PAIR_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65)))
            pair_people.add(fixed(Ellipse(width=0.48, height=0.06, stroke_width=0, fill_color=color, fill_opacity=0.28)
                .move_to([person_x, PAIR_BASE - 0.70, 0])))
            pair_people.add(fixed(Sphere(radius=0.23, color=color, resolution=(32, 24))
                .move_to([person_x, PAIR_BASE - 0.40, 0])))
            pair_words.add(fixed(Tex(name, color=INK).scale(0.7).move_to([person_x, PAIR_BASE - 1.05, 0])))
            pair_words.add(fixed(Tex(rf'{term} $\${value:g}$', color=color).scale(0.65)
                .next_to(pair_bars[-1], UP, buff=0.2)))
            if name == 'Molly':
                pair_words[-1].next_to(pair_bars[-1], RIGHT, buff=0.25)
        pair_price = fixed(VGroup(
            Line([-4.7, PAIR_BASE + 4 * PAIR_SCALE, 0], [-2.38, PAIR_BASE + 4 * PAIR_SCALE, 0], color=GUIDE, stroke_width=2.5),
            Tex(r'Price $\$4$', color=GUIDE).scale(0.65).move_to([-5.7, PAIR_BASE + 4 * PAIR_SCALE, 0])))
        pair_baseline = fixed(Line([-4.7, PAIR_BASE, 0], [-2.38, PAIR_BASE, 0], color=MUTED))
        pair_units = fixed(Tex('One 1,000-pound trade', color=CAPTION).scale(0.65).move_to([-3.6, -3.18, 0]))
        pair = fixed(Group(pair_bars, pair_people, pair_words, pair_price, pair_baseline, pair_units))
        # Keep sphere front faces in front; fixed() disables depth for flat labels.
        for mob in pair_people.get_family():
            if isinstance(mob, Sphere):
                mob.apply_depth_test()
        self.play(FadeIn(head), FadeIn(pair))
        self.pause('2.a')

        # ---- 2.b · A single external-cost piece belongs to one grey bystander.
        bystanders = fixed(Group())
        external_stack = fixed(VGroup())
        for i in range(8):
            x = 1.4 + i * 0.61
            person = fixed(Group(
                Ellipse(width=0.27, height=0.04, stroke_width=0, fill_color=MUTED, fill_opacity=0.35).move_to([x, -2.28, 0]),
                Sphere(radius=0.12, color=MUTED, resolution=(24, 16)).move_to([x, -2.10, 0])))
            person[1].apply_depth_test()
            bystanders.add(person)
            lower = PAIR_BASE + i * 0.25 * PAIR_SCALE
            external_stack.add(fixed(Polygon([3.05, lower, 0], [4.35, lower, 0],
                [4.35, lower + 0.25 * PAIR_SCALE, 0], [3.05, lower + 0.25 * PAIR_SCALE, 0],
                stroke_width=1, stroke_color=BG, fill_color=EXT, fill_opacity=0.65)))
        bystander_word = fixed(Tex('A bystander', color=CAPTION).scale(0.7).move_to([2.0, -2.8, 0]))
        small_cost = external_stack[0].copy().move_to([1.4, PAIR_BASE + 0.125 * PAIR_SCALE, 0])
        small_word = fixed(Tex(r'External cost: $\$0.25$/lb', color=EXT).scale(0.7).move_to([3.7, 0.55, 0]))
        self.play(FadeIn(bystanders[0]), FadeIn(bystander_word), FadeIn(small_cost), FadeIn(small_word))
        self.pause('2.b')

        # ---- 2.c · Stack the small harms; the eight grey people stay underneath.
        self.play(Transform(small_cost, external_stack[0]), run_time=0.7)
        self.remove(small_cost)
        self.add(external_stack[0])
        for i in range(1, 8):
            incoming = external_stack[i].copy().move_to([1.4 + i * 0.61, PAIR_BASE + 0.125 * PAIR_SCALE, 0])
            self.play(FadeIn(bystanders[i]), FadeIn(incoming), run_time=0.18)
            self.play(Transform(incoming, external_stack[i]), run_time=0.35)
            self.remove(incoming)
            self.add(external_stack[i])
        self.remove(small_word, bystander_word)
        stack_word = fixed(Tex(r'$8\times\$0.25=\$2$/lb', color=EXT).scale(0.8).move_to([3.7, 0.55, 0]))
        many_word = fixed(Tex('People outside the trade', color=CAPTION).scale(0.7).move_to([3.55, -2.8, 0]))
        conclusion = fixed(Tex('One trade can impose small costs on many other people.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(stack_word), FadeIn(many_word), FadeIn(conclusion))
        self.pause('2.c')

        # ---- 2.d · The stack becomes the external-cost area of one trade.
        ext_ax = fixed(style_axes([0, 2.5, 1], [0, 3, 1], x_length=4.3, y_length=2.2))
        ext_ax.shift(np.array([1.3, -1.5, 0]) - ext_ax.c2p(0, 0))
        ext_words = fixed(VGroup(
            Tex('External cost per pound', color=CAPTION).scale(0.65).next_to(ext_ax, UP, buff=0.20),
            Tex(r'$\$2$', color=EXT).scale(0.7).next_to(ext_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('1', color=GUIDE).scale(0.7).next_to(ext_ax.c2p(1, 0), DOWN, buff=0.18),
            Tex('1,000-pound trades', color=CAPTION).scale(0.60).next_to(ext_ax, DOWN, buff=0.65)))
        ext_parts = fixed(VGroup())
        for i in range(8):
            ext_parts.add(fixed(Polygon(ext_ax.c2p(0, i * 0.25), ext_ax.c2p(1, i * 0.25),
                ext_ax.c2p(1, (i + 1) * 0.25), ext_ax.c2p(0, (i + 1) * 0.25),
                stroke_width=1, stroke_color=BG, fill_color=EXT, fill_opacity=0.65)))
        self.play(FadeOut(stack_word), FadeOut(many_word), FadeOut(conclusion),
                  bystanders.animate.scale(0.8).move_to([3.45, -2.85, 0]), FadeIn(ext_ax), FadeIn(ext_words),
                  *[Transform(external_stack[i], ext_parts[i]) for i in range(8)], run_time=1.5)
        ext_area_word = fixed(Tex(r'$\$2{,}000$', color=INK).scale(0.8).move_to(ext_ax.c2p(0.5, 1)))
        self.play(FadeIn(ext_area_word))
        self.pause('2.d')

        # ---- 2.e · Two actual bar pairs, two external-cost rectangles.
        first_small = pair.copy().scale(0.66).move_to([-5.25, BODY_MID, 0])
        second_pair = first_small.copy().shift(RIGHT * 2.9)
        # Same geometry and units, next market interval 30–31.
        second_bars = second_pair[0]
        for index, value, previous in [(0, 5.9, PAIR_MB), (1, 3.525, PAIR_MC)]:
            second_bars[index].stretch_to_fit_height(PAIR_SCALE * 0.66 * value, about_edge=DOWN)
        second_words = second_pair[2]
        for index, text_value in [(0, 'Buyer'), (1, r'MB $\$5.90$'), (2, 'Seller'), (3, r'MPC $\$3.525$')]:
            replacement = fixed(Tex(text_value, color=INK if index % 2 == 0 else (DEMAND if index == 1 else SUPPLY))
                                .scale((0.7 if index % 2 == 0 else 0.65) * 0.66).move_to(second_words[index]))
            second_words[index].become(replacement)
        second_ext = fixed(Polygon(ext_ax.c2p(1, 0), ext_ax.c2p(2, 0), ext_ax.c2p(2, 2), ext_ax.c2p(1, 2),
            stroke_width=1.5, stroke_color=BG, fill_color=EXT, fill_opacity=0.65))
        second_ext_word = fixed(Tex(r'$\$2{,}000$', color=INK).scale(0.8).move_to(ext_ax.c2p(1.5, 1)))
        second_tick = fixed(Tex('2', color=GUIDE).scale(0.7).next_to(ext_ax.c2p(2, 0), DOWN, buff=0.18))
        self.play(Transform(pair, first_small), FadeIn(second_pair), FadeIn(second_ext),
                  FadeIn(second_ext_word), FadeIn(second_tick), run_time=1.6)
        self.pause('2.e')

        # ---- 2.f · Both trades land at their own ranks in the complete market.
        left_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        left_ax.shift(np.array([-6.45, -2.15, 0]) - left_ax.c2p(0, 0))
        right_ax = fixed(style_axes([0, 60, 10], [0, 13, 2], x_length=5.5, y_length=3.9))
        right_ax.shift(np.array([1.25, -2.15, 0]) - right_ax.c2p(0, 0))
        left_words = fixed(VGroup(
            Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(0, 13), UP, buff=0.16),
            Tex('Q', color=INK).scale(0.7).next_to(left_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{1,000 lb}', color=CAPTION).scale(0.55).next_to(left_ax.c2p(45, 0), DOWN, buff=0.7)))
        right_words = fixed(VGroup(
            Tex('External cost per pound', color=CAPTION).scale(0.65).next_to(right_ax.c2p(30, 13), UP, buff=0.16),
            Tex(r'$\$2$', color=EXT).scale(0.65).next_to(right_ax.c2p(0, 2), LEFT, buff=0.15),
            Tex('Q', color=INK).scale(0.7).next_to(right_ax.c2p(60, 0), DOWN, buff=0.18),
            Tex(r'\textsf{1,000 lb}', color=CAPTION).scale(0.55).next_to(right_ax.c2p(45, 0), DOWN, buff=0.7),
            Tex(r'$Q=40$', color=GUIDE).scale(0.65).next_to(right_ax.c2p(40, 0), DOWN, buff=0.18)))
        left_demand = fixed(Line(left_ax.c2p(0, 12), left_ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        left_supply = fixed(Line(left_ax.c2p(0, 2), left_ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        left_curve_words = fixed(VGroup(
            Tex('MPB', color=INK).scale(0.7).next_to(left_ax.c2p(8, 10.4), UR, buff=0.1),
            Tex('MPC', color=INK).scale(0.7).next_to(left_ax.c2p(60, 5), RIGHT, buff=0.12)))
        left_eq = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.06, color=GUIDE),
            DashedLine(left_ax.c2p(0, 4), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=1.5),
            Tex(r'$Q_m=40$', color=GUIDE).scale(0.65).next_to(left_ax.c2p(40, 0), DOWN, buff=0.18)))
        private_bars, benefit_bars, external_bars = fixed(VGroup()), fixed(VGroup()), fixed(VGroup())
        for q in range(40):
            l, r = q + BAR_GAP / 2, q + 1 - BAR_GAP / 2
            private_bars.add(fixed(Polygon(left_ax.c2p(l, 0), left_ax.c2p(r, 0),
                left_ax.c2p(r, 2 + r / 20), left_ax.c2p(l, 2 + l / 20),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.45)))
            benefit_bars.add(fixed(Polygon(left_ax.c2p(l, 4), left_ax.c2p(r, 4),
                left_ax.c2p(r, 12 - r / 5), left_ax.c2p(l, 12 - l / 5),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.25)))
            external_bars.add(fixed(Polygon(right_ax.c2p(l, 0), right_ax.c2p(r, 0),
                right_ax.c2p(r, 2), right_ax.c2p(l, 2),
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        landing_pairs = []
        for q in [29, 30]:
            landing_pairs.append(fixed(VGroup(
                Polygon(left_ax.c2p(q + 0.04, 0), left_ax.c2p(q + 0.47, 0),
                    left_ax.c2p(q + 0.47, 12 - (q + 0.5) / 5), left_ax.c2p(q + 0.04, 12 - (q + 0.5) / 5),
                    stroke_width=0, fill_color=DEMAND, fill_opacity=0.65),
                Polygon(left_ax.c2p(q + 0.53, 0), left_ax.c2p(q + 0.96, 0),
                    left_ax.c2p(q + 0.96, 2 + (q + 0.5) / 20), left_ax.c2p(q + 0.53, 2 + (q + 0.5) / 20),
                    stroke_width=0, fill_color=SUPPLY, fill_opacity=0.65))))
        # Separate bars from their departing people so the bars survive the pullback.
        first_flying, second_flying = pair[0].copy(), second_pair[0].copy()
        self.add(first_flying, second_flying)
        self.remove(head)
        head = fixed(title('Every trade affects people outside the market'))
        self.play(FadeIn(head), FadeOut(pair), FadeOut(second_pair), FadeOut(bystanders),
                  FadeOut(ext_ax), FadeOut(ext_words), FadeOut(ext_area_word), FadeOut(second_ext_word), FadeOut(second_tick),
                  Transform(first_flying, landing_pairs[0]), Transform(second_flying, landing_pairs[1]),
                  Transform(external_stack, fixed(VGroup(external_bars[29].copy()))),
                  Transform(second_ext, external_bars[30]),
                  FadeIn(left_ax), FadeIn(right_ax), FadeIn(left_words), FadeIn(right_words),
                  FadeIn(left_demand), FadeIn(left_supply), FadeIn(left_curve_words), FadeIn(left_eq), run_time=2)
        self.play(FadeIn(private_bars), FadeIn(benefit_bars),
                  LaggedStart(*[FadeIn(bar) for bar in external_bars], lag_ratio=0.02), run_time=1.4)
        self.remove(first_flying, second_flying, external_stack, second_ext)
        ext_total_word = fixed(Tex(r'Total external cost: $\$80{,}000$', color=EXT).scale(0.75)
                               .move_to([3.9, 0.3, 0]))
        self.play(FadeIn(ext_total_word))
        self.pause('2.f')

        # ---- 3.a · Strip away benefit to account for every cost.
        self.remove(head)
        head = fixed(title('What is the full cost of a trade?'))
        self.play(FadeIn(head), FadeOut(left_demand), FadeOut(benefit_bars),
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
        cost_definition = fixed(Tex('Marginal social cost $=$ private cost $+$ external cost.', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
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
        demand_word = fixed(Tex('MPB = MSB', color=INK).scale(0.7).next_to(left_ax.c2p(7, 10.6), UR, buff=0.12))
        market_reference = fixed(VGroup(
            Dot(left_ax.c2p(40, 4), radius=0.065, color=GUIDE),
            DashedLine(left_ax.c2p(40, 0), left_ax.c2p(40, 4), color=GUIDE, stroke_width=2),
            Tex(r'$Q_m=40$', color=GUIDE).scale(0.7).next_to(left_ax.c2p(40, 0), DOWN, buff=0.20),
            Tex(r'$P_m=4$', color=GUIDE).scale(0.7).next_to(left_ax.c2p(40, 4), DOWN + RIGHT, buff=0.14)))
        self.remove(head, cost_definition)
        head = fixed(title('Would one more trade or one fewer trade help?'))
        question = fixed(Tex('The market still chooses MPB $=$ MPC.', color=DEFINITION)
                         .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(head), FadeIn(full_demand), FadeIn(demand_word), FadeIn(market_reference), FadeIn(question))
        social_graph = fixed(VGroup(cost_graph, full_demand, demand_word, market_reference))
        self.remove(cost_graph, full_demand, demand_word, market_reference)
        self.add(social_graph)
        self.pause('3.c')

        # ---- 3.d · The added unit, with external cost stacked on MPC.
        extra_social_pair = fixed(VGroup(
            Polygon(left_ax.c2p(40.04, 0), left_ax.c2p(40.47, 0),
                left_ax.c2p(40.47, 3.9), left_ax.c2p(40.04, 3.9),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.65),
            Polygon(left_ax.c2p(40.53, 0), left_ax.c2p(40.96, 0),
                left_ax.c2p(40.96, 4.025), left_ax.c2p(40.53, 4.025),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.65),
            Polygon(left_ax.c2p(40.53, 4.025), left_ax.c2p(40.96, 4.025),
                left_ax.c2p(40.96, 6.025), left_ax.c2p(40.53, 6.025),
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        extra_social_home = extra_social_pair.copy()
        selection_word = fixed(Tex('One added 1,000-pound lot', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(question)
        self.play(FadeIn(extra_social_pair), FadeIn(selection_word))
        self.pause('3.d.select')
        extra_social_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 3.9, DEMAND), (0.06, 0, 4.025, SUPPLY),
                                      (0.06, 4.025, 6.025, EXT)]:
            extra_social_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65)))
        self.play(FadeOut(social_graph), FadeOut(selection_word),
                  Transform(extra_social_pair, extra_social_target), run_time=1.6)
        extra_social_labels = fixed(VGroup(
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MSB $\$3.90$', color=DEMAND).scale(0.72).next_to(extra_social_target[0], LEFT, buff=0.25),
            Tex(r'MPC $\$4.025$', color=SUPPLY).scale(0.72).next_to(extra_social_target[1], RIGHT, buff=0.25),
            Tex(r'External cost $\$2$', color=EXT).scale(0.72).next_to(extra_social_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$6.025$', color=SUPPLY).scale(0.72).next_to(extra_social_target[2], UP, buff=0.18),
            Tex('Average values per pound', color=CAPTION).scale(0.6).move_to([-4.2, 2.45, 0]),
            Tex('One added 1,000-pound lot', color=CAPTION).scale(0.65).move_to([0, -3.05, 0])))
        social_gap = fixed(VGroup(
            DashedLine([-1.16, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([0.06, DETAIL_BASE + 6.025 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 6.025 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([-2.0, DETAIL_BASE + 3.9 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 6.025 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$2{,}125$', color=TOTAL).scale(0.8)
                .next_to([-2.0, DETAIL_BASE + 4.9625 * DETAIL_SCALE, 0], LEFT, buff=0.3)))
        conclusion = fixed(Tex('One more trade reduces social welfare.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(extra_social_labels), FadeIn(detail_people), FadeIn(social_gap), FadeIn(conclusion))
        self.pause('3.d')
        self.play(FadeOut(extra_social_labels), FadeOut(detail_people), FadeOut(social_gap), FadeOut(conclusion),
                  Transform(extra_social_pair, extra_social_home), FadeIn(social_graph), run_time=1.6)
        self.play(FadeOut(extra_social_pair))
        self.pause('3.d.return')

        # ---- 3.e · The removed unit, with external cost stacked on MPC.
        removed_social_pair = fixed(VGroup(
            Polygon(left_ax.c2p(39.04, 0), left_ax.c2p(39.47, 0),
                left_ax.c2p(39.47, 4.1), left_ax.c2p(39.04, 4.1),
                stroke_width=0, fill_color=DEMAND, fill_opacity=0.65),
            Polygon(left_ax.c2p(39.53, 0), left_ax.c2p(39.96, 0),
                left_ax.c2p(39.96, 3.975), left_ax.c2p(39.53, 3.975),
                stroke_width=0, fill_color=SUPPLY, fill_opacity=0.65),
            Polygon(left_ax.c2p(39.53, 3.975), left_ax.c2p(39.96, 3.975),
                left_ax.c2p(39.96, 5.975), left_ax.c2p(39.53, 5.975),
                stroke_width=0, fill_color=EXT, fill_opacity=0.65)))
        removed_social_home = removed_social_pair.copy()
        selection_word = fixed(Tex('One removed 1,000-pound lot', color=DEFINITION)
                               .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.remove(question)
        self.play(FadeIn(removed_social_pair), FadeIn(selection_word))
        self.pause('3.e.select')
        removed_social_target = fixed(VGroup())
        for left, low, high, color in [(-1.16, 0, 4.1, DEMAND), (0.06, 0, 3.975, SUPPLY),
                                      (0.06, 3.975, 5.975, EXT)]:
            removed_social_target.add(fixed(Polygon(
                [left, DETAIL_BASE + low * DETAIL_SCALE, 0], [left + 1.1, DETAIL_BASE + low * DETAIL_SCALE, 0],
                [left + 1.1, DETAIL_BASE + high * DETAIL_SCALE, 0], [left, DETAIL_BASE + high * DETAIL_SCALE, 0],
                stroke_width=0, fill_color=color, fill_opacity=0.65)))
        self.play(FadeOut(social_graph), FadeOut(selection_word),
                  Transform(removed_social_pair, removed_social_target), run_time=1.6)
        removed_social_labels = fixed(VGroup(
            Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED),
            Tex(r'MSB $\$4.10$', color=DEMAND).scale(0.72).next_to(removed_social_target[0], LEFT, buff=0.25),
            Tex(r'MPC $\$3.975$', color=SUPPLY).scale(0.72).next_to(removed_social_target[1], RIGHT, buff=0.25),
            Tex(r'External cost $\$2$', color=EXT).scale(0.72).next_to(removed_social_target[2], RIGHT, buff=0.25),
            Tex(r'MSC $\$5.975$', color=SUPPLY).scale(0.72).next_to(removed_social_target[2], UP, buff=0.18),
            Tex('Average values per pound', color=CAPTION).scale(0.6).move_to([-4.2, 2.45, 0]),
            Tex('One removed 1,000-pound lot', color=CAPTION).scale(0.65).move_to([0, -3.05, 0])))
        social_gap = fixed(VGroup(
            DashedLine([-1.16, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            DashedLine([0.06, DETAIL_BASE + 5.975 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 5.975 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=1.6),
            Line([-2.0, DETAIL_BASE + 4.1 * DETAIL_SCALE, 0],
                [-2.0, DETAIL_BASE + 5.975 * DETAIL_SCALE, 0], color=TOTAL, stroke_width=3),
            Tex(r'TS $=-\$1{,}875$', color=TOTAL).scale(0.8)
                .next_to([-2.0, DETAIL_BASE + 5.0375 * DETAIL_SCALE, 0], LEFT, buff=0.3)))
        conclusion = fixed(Tex('One fewer trade increases social welfare.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(removed_social_labels), FadeIn(detail_people), FadeIn(social_gap), FadeIn(conclusion))
        self.pause('3.e')
        self.play(FadeOut(removed_social_labels), FadeOut(detail_people), FadeOut(social_gap), FadeOut(conclusion),
                  Transform(removed_social_pair, removed_social_home), FadeIn(social_graph), run_time=1.6)
        self.play(FadeOut(removed_social_pair))
        self.pause('3.e.return')

        # ---- 4.a · Legacy social-planner sequence: change the evaluated Q only.
        self.remove(head)
        head = fixed(title('Which quantity maximizes social welfare?'))
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
        condition = fixed(Tex('Social welfare is maximized where MSB $=$ MSC.', color=DEFINITION)
                          .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(FadeIn(efficient_dot), FadeIn(efficient_word), FadeIn(condition), FadeOut(marginal_gap))
        self.pause('4.a')

        # ---- 4.b · The losses from excessive trades; not all external damage.
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
        self.remove(conclusion)
        conclusion = fixed(Tex('Some production is worthwhile even when it causes harm.', color=DEFINITION)
                           .scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))
        self.play(evaluation_q.animate.set_value(24), FadeIn(conclusion), run_time=1.8)
        benefit_gap = fixed(Line(left_ax.c2p(24, 5.2), left_ax.c2p(24, 7.2), color=TOTAL, stroke_width=7))
        benefit_word = fixed(Tex('MSB $>$ MSC', color=TOTAL).scale(0.72).next_to(benefit_gap, LEFT, buff=0.25))
        self.play(FadeIn(benefit_gap), FadeIn(benefit_word))
        self.pause('4.c.beneficial')
        self.play(FadeOut(benefit_gap), FadeOut(benefit_word), evaluation_q.animate.set_value(32), run_time=1.8)
        self.pause('4.c')
