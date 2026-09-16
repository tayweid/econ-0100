# maniml 03_Code.py EpisodeB2
# Episode B2 | Supply
# Read top to bottom. Beat IDs match 02_Storyboard.md.
# The bumper uses shared helpers; all other choreography lives in construct.
# Flat midpoint bars keep each small production decision visible.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes


class EpisodeB2(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        GRAPH_AT = np.array([-2.6, 0.15, 0])
        REST_OPACITY = 0.10
        SLICE_WIDTH = 0.1  # Keep the existing picture: one supply slice now represents 1 kg.
        KG_PER_GRAPH_UNIT = 10  # c2p coordinates stay unchanged; Q labels are in kilograms.
        DEFINITION_BOTTOM = 0.05  # Tiny margin beneath the bottom definition line.
        DEFINITION_SCALE = 0.7443  # Same text size as the first Quantity Supplied definition.

        # ---- 0.a · Reuse B1's shared episode bumper.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'B', 2)
        thesis = Tex(r'\textit{Supply: a simple way to organize costs.}', color=CAPTION)
        thesis.scale(1.1).next_to(episode, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · B1's buyer, marginal benefit, and consumer surplus.
        head = title('Last time...')
        recap_ax = style_axes([0, 6, 1], [0, 2.5, 0.5], x_length=7, y_length=6).scale(0.8)
        recap_ax.shift(GRAPH_AT - (recap_ax.c2p(0, 0) + recap_ax.c2p(6, 2.5)) / 2)
        recap_curve = Line(recap_ax.c2p(0, 2.5), recap_ax.c2p(5, 0), color=DEMAND, z_index=3)
        recap_p = Tex('P').next_to(recap_ax.c2p(0, 2.5), LEFT, buff=0.25)
        recap_q = Tex('Q').next_to(recap_ax.c2p(6, 0), DOWN, buff=0.35)
        recap_grey = VGroup()
        recap_cs = VGroup()
        for left in np.arange(0, 5, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            grey = Polygon(recap_ax.c2p(left, 0), recap_ax.c2p(right, 0),
                           recap_ax.c2p(right, min(1, 2.5 - right / 2)),
                           recap_ax.c2p(left, min(1, 2.5 - left / 2)))
            grey.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            recap_grey.add(grey)
            if left < 3:
                cs = Polygon(recap_ax.c2p(left, 1), recap_ax.c2p(right, 1),
                             recap_ax.c2p(right, 2.5 - right / 2), recap_ax.c2p(left, 2.5 - left / 2),
                             color=DEMAND, fill_opacity=AREA_OPACITY, stroke_width=1)
                recap_cs.add(cs)
        recap_price = DashedLine(recap_ax.c2p(0, 1), recap_ax.c2p(3, 1), color=GUIDE, z_index=10)
        recap_drop = DashedLine(recap_ax.c2p(3, 1), recap_ax.c2p(3, 0), color=GUIDE, z_index=10)
        recap_point = Dot(recap_ax.c2p(3, 1), color=GUIDE, z_index=11)
        recap_price_label = Tex('Price', color=GUIDE).scale(0.7)
        recap_price_label.next_to(recap_ax.c2p(0, 1), LEFT, buff=0.6)
        recap_quantity = Tex('$Q_d$', color=GUIDE).scale(0.7).next_to(recap_ax.c2p(3, 0), DOWN, buff=0.6)
        recap = VGroup(
            VGroup(Tex('Preferences', color=DEFINITION), Tex('Rank the available choices.', color=INK)),
            VGroup(Tex('Quantity Demanded', color=DEFINITION),
                   Tex('The quantity a buyer is willing', color=INK),
                   Tex('and able to buy at a given price.', color=INK)),
            VGroup(Tex('Marginal Benefit', color=DEFINITION), Tex('Is another purchase worth making?', color=INK)),
            VGroup(Tex('Consumer Surplus', color=DEFINITION), Tex("The buyer's value above the price.", color=INK)))
        for item in recap:
            item.arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.8)
        recap.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        recap.move_to([1.1, GRAPH_AT[1], 0], aligned_edge=LEFT)
        self.play(FadeIn(head), FadeIn(recap_ax), FadeIn(recap_curve), FadeIn(recap_p), FadeIn(recap_q))
        self.play(FadeIn(recap_grey), FadeIn(recap_cs), FadeIn(recap_price), FadeIn(recap_drop),
                  FadeIn(recap_point), FadeIn(recap_price_label), FadeIn(recap_quantity))
        for line in recap:
            self.play(FadeIn(line))
        self.pause('1.a')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 2.a · Molly's fixed farm; more spinach displaces other uses.
        head = title('How much would Molly grow?')
        ax = style_axes(
            [0, 6, 1], [0, 8.5, 1], x_length=7, y_length=6, ticks=True,
            x_axis_config={'numbers_to_include': [1, 2, 3, 4, 5],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [2, 4, 6, 8],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}}).scale(0.8)
        ax.shift(GRAPH_AT - (ax.c2p(0, 0) + ax.c2p(6, 8.5)) / 2)
        for number in ax.x_axis.numbers:
            number_center = number.get_center()
            number.set_value(number.get_value() * KG_PER_GRAPH_UNIT).move_to(number_center)
        p_lab = Tex('P', color=INK).next_to(ax.c2p(0, 8.5), LEFT, buff=0.25)
        q_lab = Tex('Q', color=INK).next_to(ax.c2p(6, 0), DOWN, buff=0.35)
        p_units = Tex(r'\textsf{dollars per kg}', color=CAPTION).scale(0.7)
        p_units.next_to(p_lab, RIGHT, buff=0.35)
        q_units = Tex(r'\textsf{kilograms}', color=CAPTION).scale(0.7)
        q_units.next_to(q_lab, RIGHT, buff=0.3)
        farm = Rectangle(width=4.5, height=2.6, color=INK, stroke_width=2).move_to([4.15, 0.45, 0])
        farm_name = Tex("Molly's farm", color=INK).next_to(farm, UP, buff=0.3)
        farm_price = ValueTracker(4)
        spinach = Polygon([1.9, -0.85, 0], [3.4, -0.85, 0], [3.4, 1.75, 0], [1.9, 1.75, 0],
                          color=SPINACH, stroke_width=0, fill_opacity=0.55)
        spinach.add_updater(lambda area: area.set_points_as_corners([
            [1.9, -0.85, 0], [1.9 + 0.75 * max(0, farm_price.get_value() - 2), -0.85, 0],
            [1.9 + 0.75 * max(0, farm_price.get_value() - 2), 1.75, 0], [1.9, 1.75, 0], [1.9, -0.85, 0]]))
        spinach_label = Tex('Spinach', color=SPINACH).scale(0.8).next_to(spinach, DOWN, buff=0.25)
        farm_q = VGroup(Tex('$Q_s=$'), DecimalNumber(20, num_decimal_places=0))
        farm_q.arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE).next_to(ax.c2p(2, 0), DOWN, buff=0.6)
        asking_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        asking_number.next_to(ax.c2p(0, 4), LEFT, buff=0.6)
        asking_word = Tex(r'Price \$', color=GUIDE).scale(0.7).next_to(asking_number, LEFT, buff=0.04)
        asking = VGroup(asking_number, asking_word)
        self.play(FadeIn(head), FadeIn(ax), FadeIn(p_lab), FadeIn(q_lab), FadeIn(p_units), FadeIn(q_units))
        self.play(FadeIn(spinach), FadeIn(farm), FadeIn(farm_name), FadeIn(spinach_label))
        self.play(FadeIn(asking))
        asking_number.add_updater(lambda number: number.set_value(farm_price.get_value())
                                 .next_to(ax.c2p(0, farm_price.get_value()), LEFT, buff=0.6))
        asking_word.add_updater(lambda word: word.next_to(asking_number, LEFT, buff=0.04))
        farm_q[1].add_updater(lambda number: number.set_value(KG_PER_GRAPH_UNIT * max(0, farm_price.get_value() - 2)))
        farm_q.add_updater(lambda group: group.arrange(RIGHT, buff=0.12)
                           .next_to(ax.c2p(max(0, farm_price.get_value() - 2), 0), DOWN, buff=0.6))
        spinach_label.add_updater(lambda label: label.next_to(spinach, DOWN, buff=0.25)
                                  .set_opacity(min(1, max(0, farm_price.get_value() - 2))))
        self.pause('2.a')

        # ---- 2.b · Quantity supplied is an answer at one price.
        qs_def = Tex(r'\mbox{ {{Individual Quantity Supplied}} is the quantity a seller is willing and able to sell at a given price.}',
                     tex_to_color_map={'Individual Quantity Supplied': DEFINITION})
        qs_def.scale(DEFINITION_SCALE)
        qs_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        points = VGroup(Dot(ax.c2p(2, 4), color=SUPPLY, z_index=11))
        farm_h = DashedLine(ax.c2p(0, 4), ax.c2p(2, 4), color=GUIDE, z_index=10).set_opacity(0.5)
        farm_v = DashedLine(ax.c2p(2, 4), ax.c2p(2, 0), color=GUIDE, z_index=10).set_opacity(0.5)
        farm_dot = Dot(ax.c2p(2, 4), color=GUIDE, z_index=12)
        self.play(FadeIn(qs_def))
        self.play(FadeIn(farm_h), FadeIn(points), FadeIn(farm_dot))
        self.play(GrowFromPoint(farm_v, ax.c2p(2, 4)))
        self.play(FadeIn(farm_q))
        farm_h.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(0, farm_price.get_value()), ax.c2p(max(0, farm_price.get_value() - 2), farm_price.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        farm_v.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(max(0, farm_price.get_value() - 2), farm_price.get_value()),
            ax.c2p(max(0, farm_price.get_value() - 2), 0),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        farm_dot.add_updater(lambda dot: dot.move_to(ax.c2p(max(0, farm_price.get_value() - 2), farm_price.get_value())))
        self.pause('2.b')

        # ---- 2.d · $6 makes 40 kg worthwhile.
        self.play(farm_price.animate.set_value(6), run_time=1.5)
        point = Dot(ax.c2p(4, 6), color=SUPPLY, z_index=11)
        points.add(point)
        self.play(FadeIn(point))
        self.pause('2.d')

        # ---- 2.e · At $2, she supplies zero in this example.
        self.play(farm_price.animate.set_value(2), run_time=1.5)
        point = Dot(ax.c2p(0, 2), color=SUPPLY, z_index=11)
        points.add(point)
        self.play(FadeIn(point))
        self.pause('2.e')

        # ---- 2.f · Connect her answers.
        spinach.clear_updaters()
        spinach_label.clear_updaters()
        asking.clear_updaters()
        farm_q.clear_updaters()
        farm_h.clear_updaters()
        farm_v.clear_updaters()
        farm_dot.clear_updaters()
        self.remove(farm_price)
        self.play(FadeOut(asking), FadeOut(farm_q), FadeOut(farm_h), FadeOut(farm_v), FadeOut(farm_dot))
        supply = Line(ax.c2p(0, 2), ax.c2p(6, 8), color=SUPPLY, z_index=3)
        supply_def = Tex(r"\mbox{ {{Individual Supply Curve}} collects a seller's quantity supplied at every price.}",
                         tex_to_color_map={'Individual Supply Curve': DEFINITION})
        supply_def.scale(DEFINITION_SCALE)
        supply_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(qs_def)
        self.play(FadeIn(supply), FadeIn(supply_def))
        self.bring_to_front(points)
        self.pause('2.f')

        # ---- 2.g · Name the pattern after showing it.
        law_def = Tex(r'\mbox{ {{Law of Supply}} says the quantity supplied of a good rises with its price.}',
                      tex_to_color_map={'Law of Supply': DEFINITION})
        law_def.scale(DEFINITION_SCALE)
        law_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(supply_def)
        self.play(FadeIn(law_def))
        self.pause('2.g')

        # ---- 2.h · B1's standing quantities, now under increasing MC.
        self.play(FadeOut(farm), FadeOut(farm_name),
                  FadeOut(spinach), FadeOut(spinach_label), FadeOut(points))
        self.remove(law_def)
        equation = Tex('$P=2+Q_s/10$', isolate=['2']).scale(0.9).move_to(ax.c2p(2.9, 7.5))
        s_lab = Tex('S').next_to(ax.c2p(6, 8), RIGHT, buff=0.15)
        rest_bars = VGroup()
        for left in np.arange(0, 6, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            slice_mc = 2 + (left + right) / 2
            bar = Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                          ax.c2p(right, slice_mc), ax.c2p(left, slice_mc))
            bar.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            rest_bars.add(bar)
        self.play(FadeIn(equation), FadeIn(s_lab), FadeIn(rest_bars))
        self.bring_to_front(supply)
        self.pause('2.h')

        # ---- 3.a · Pick a price, trace the graph, leave the answer unknown.
        read_price = ValueTracker(5)
        price_number = DecimalNumber(5, num_decimal_places=2, color=GUIDE).scale(0.7)
        price_number.next_to(ax.c2p(0, 5), LEFT, buff=0.6)
        price_word = Tex(r'Price \$', color=GUIDE).scale(0.7).next_to(price_number, LEFT, buff=0.04)
        price_source = VGroup(price_number, price_word)
        h_guide = DashedLine(ax.c2p(0, 5), ax.c2p(3, 5), color=GUIDE, z_index=10).set_opacity(0.5)
        v_guide = DashedLine(ax.c2p(3, 5), ax.c2p(3, 0), color=GUIDE, z_index=10).set_opacity(0.5)
        read_dot = Dot(ax.c2p(3, 5), color=GUIDE, z_index=11)
        question = Tex('$Q_s=?$', color=GUIDE).scale(0.7).next_to(ax.c2p(3, 0), DOWN, buff=0.6)
        ax.x_axis.numbers[2].set_opacity(0)
        self.play(FadeIn(price_source))
        self.play(FadeIn(h_guide))
        self.play(FadeIn(v_guide), FadeIn(read_dot), FadeIn(question))
        price_number.add_updater(lambda number: number.set_value(read_price.get_value())
                                 .next_to(ax.c2p(0, read_price.get_value()), LEFT, buff=0.6))
        price_word.add_updater(lambda word: word.next_to(price_number, LEFT, buff=0.04))
        h_guide.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(0, read_price.get_value()), ax.c2p(read_price.get_value() - 2, read_price.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        v_guide.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(read_price.get_value() - 2, read_price.get_value()), ax.c2p(read_price.get_value() - 2, 0),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        read_dot.add_updater(lambda dot: dot.move_to(ax.c2p(read_price.get_value() - 2, read_price.get_value())))
        self.pause('3.a')

        # ---- 3.b · The answer enters the graph only after the calculation.
        # Leave the horizontal axis name and units entirely on the graph side.
        divider_x = max(q_lab.get_right()[0], q_units.get_right()[0]) + 0.35
        MATH_AT = np.array([(divider_x + FRAME_W / 2 - 0.6) / 2, 0.7, 0])
        math_divider = Line([divider_x, -3, 0], [divider_x, 3, 0], color=MUTED, stroke_width=1)
        math_divider.set_opacity(0.5)
        substitution = VGroup(Tex('$5$', color=GUIDE), Tex('$=2+Q_s/10$', tex_to_color_map={'Q_s': GUIDE}))
        rearrange = Tex('$Q_s=10(5-2)$', tex_to_color_map={'Q_s': GUIDE, '5': GUIDE})
        answer = VGroup(Tex('$Q_s=$'), Tex('$30$')).set_color(GUIDE)
        substitution.arrange(RIGHT, buff=0.12)
        answer.arrange(RIGHT, buff=0.12)
        work = VGroup(substitution, rearrange, answer).scale(0.8)
        work.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT)
        self.play(FadeIn(math_divider),
                  TransformFromCopy(price_number.copy().clear_updaters(), substitution[0]), FadeIn(substitution[1]))
        self.play(FadeIn(rearrange))
        self.play(FadeIn(answer))
        q_answer = VGroup(Tex('$Q_s=$'), Tex('$30$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        q_answer.move_to(question)
        self.play(FadeOut(question), FadeIn(q_answer[0]), TransformFromCopy(answer[1], q_answer[1]),
                  ax.x_axis.numbers[2].animate.set_opacity(1))
        self.pause('3.b')

        # ---- 3.c · Keep the same guides while the price rolls.
        self.play(FadeOut(work), FadeOut(q_answer))
        self.play(read_price.animate.set_value(4.5), run_time=1.5)
        question = Tex('$Q_s=?$', color=GUIDE).scale(0.7).next_to(ax.c2p(2.5, 0), DOWN, buff=0.6)
        self.play(FadeIn(question))
        self.pause('3.c')

        # ---- 3.d · $4.50 gives a quantity of 25 kg.
        substitution = VGroup(Tex('$4.50$', color=GUIDE), Tex('$=2+Q_s/10$', tex_to_color_map={'Q_s': GUIDE}))
        rearrange = Tex('$Q_s=10(4.50-2)$', tex_to_color_map={'Q_s': GUIDE, '4.50': GUIDE})
        answer = VGroup(Tex('$Q_s=$'), Tex('$25$')).set_color(GUIDE)
        substitution.arrange(RIGHT, buff=0.12)
        answer.arrange(RIGHT, buff=0.12)
        work = VGroup(substitution, rearrange, answer).scale(0.8)
        work.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT)
        self.play(TransformFromCopy(price_number.copy().clear_updaters(), substitution[0]), FadeIn(substitution[1]))
        self.play(FadeIn(rearrange))
        self.play(FadeIn(answer))
        q_answer = VGroup(Tex('$Q_s=$'), Tex('$25$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        q_answer.move_to(question)
        self.play(FadeOut(question), FadeIn(q_answer[0]), TransformFromCopy(answer[1], q_answer[1]))
        self.pause('3.d')
        price_source.clear_updaters()
        h_guide.clear_updaters()
        v_guide.clear_updaters()
        read_dot.clear_updaters()
        self.remove(read_price)
        self.play(FadeOut(price_source), FadeOut(h_guide), FadeOut(v_guide),
                  FadeOut(read_dot), FadeOut(q_answer), FadeOut(work), FadeOut(math_divider))

        # ---- 3.e · MC is a height for the next small addition, not total cost.
        self.remove(head)
        head = title('Which spinach is worth growing?')
        mc_def = Tex(r'\mbox{ {{Marginal Cost}} is the cost of producing one additional unit.}',
                     tex_to_color_map={'Marginal Cost': DEFINITION})
        mc_def.scale(DEFINITION_SCALE)
        mc_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        read_quantity = ValueTracker(1)  # Graph coordinate 1 represents 10 kg.
        q_source = VGroup(Tex('$Q_s=$'), DecimalNumber(10, num_decimal_places=0))
        q_source.arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE).next_to(ax.c2p(1, 0), DOWN, buff=0.6)
        mc_v = DashedLine(ax.c2p(1, 0), ax.c2p(1, 3), color=GUIDE, z_index=10).set_opacity(0.5)
        mc_h = DashedLine(ax.c2p(1, 3), ax.c2p(0, 3), color=GUIDE, z_index=10).set_opacity(0.5)
        mc_dot = Dot(ax.c2p(1, 3), color=GUIDE, z_index=11)
        mc_question = Tex('$MC=?$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 3), LEFT, buff=0.6)
        self.play(FadeIn(head), FadeIn(q_source))
        self.play(FadeIn(mc_v))
        self.play(FadeIn(mc_h), FadeIn(mc_dot), FadeIn(mc_question))
        self.play(FadeIn(mc_def))
        q_source[1].add_updater(lambda number: number.set_value(KG_PER_GRAPH_UNIT * read_quantity.get_value()))
        q_source.add_updater(lambda group: group.arrange(RIGHT, buff=0.12)
                             .next_to(ax.c2p(read_quantity.get_value(), 0), DOWN, buff=0.6))
        mc_v.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(read_quantity.get_value(), 0), ax.c2p(read_quantity.get_value(), 2 + read_quantity.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        mc_h.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(read_quantity.get_value(), 2 + read_quantity.get_value()), ax.c2p(0, 2 + read_quantity.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        mc_dot.add_updater(lambda dot: dot.move_to(ax.c2p(read_quantity.get_value(), 2 + read_quantity.get_value())))
        self.pause('3.e')

        # ---- 3.f · At Q=10 kg, MC is $3 per kg.
        substitution = VGroup(Tex('$P=2+$', tex_to_color_map={'P': GUIDE}),
                             Tex('$10$', color=GUIDE), Tex('$/10$'))
        answer = VGroup(Tex('$P=$'), Tex(r'\$3.00')).set_color(GUIDE)
        substitution.arrange(RIGHT, buff=0.12)
        answer.arrange(RIGHT, buff=0.12)
        work = VGroup(substitution, answer).scale(0.8)
        work.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT)
        math_divider.set_opacity(0.5)
        self.play(FadeIn(math_divider), FadeIn(substitution[0]),
                  TransformFromCopy(q_source[1].copy().clear_updaters(), substitution[1]), FadeIn(substitution[2]))
        self.play(FadeIn(answer))
        mc_answer = VGroup(Tex('$MC=$'), Tex(r'\$3.00')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        mc_answer.move_to(mc_question)
        self.play(FadeOut(mc_question), FadeIn(mc_answer[0]), TransformFromCopy(answer[1], mc_answer[1]))
        self.pause('3.f')

        # ---- 3.i · Compare MC with one fixed price.
        mc_h.clear_updaters()
        self.play(FadeOut(work), FadeOut(mc_answer), FadeOut(mc_h))
        offer_line = DashedLine(ax.c2p(0, 4), ax.c2p(6, 4), color=GUIDE, z_index=10).set_opacity(0.7)
        offer_label = Tex(r'Price $= \$4$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, 4), LEFT, buff=0.6)
        comparison = Tex('$MC<P$', color=GUIDE).scale(0.8).move_to(MATH_AT)
        self.play(FadeIn(offer_line), FadeIn(offer_label), read_quantity.animate.set_value(1), run_time=1.5)
        self.play(FadeIn(comparison))
        self.pause('3.i')

        # ---- 3.j · Price and marginal cost meet.
        self.play(FadeOut(comparison), read_quantity.animate.set_value(2), run_time=1.5)
        comparison = Tex(r'$MC=P=\$4$', color=GUIDE).scale(0.8).move_to(MATH_AT)
        self.play(FadeIn(comparison))
        self.pause('3.j')

        # ---- 3.k · Beyond Q=20 kg, adding more costs more than it brings in.
        self.play(FadeOut(comparison), read_quantity.animate.set_value(3), run_time=1.5)
        comparison = Tex('$MC>P$', color=GUIDE).scale(0.8).move_to(MATH_AT)
        self.play(FadeIn(comparison))
        self.pause('3.k')

        # ---- 3.l · Return to Molly's chosen quantity.
        self.play(FadeOut(comparison), read_quantity.animate.set_value(2), run_time=1.5)
        comparison = Tex(r'$MC=P=\$4$', color=GUIDE).scale(0.8).move_to(MATH_AT)
        self.play(FadeIn(comparison))
        self.pause('3.l')

        # ---- 3.m · Money measures opportunity cost, including her time.
        self.play(FadeOut(comparison), FadeOut(math_divider))
        curve_def = Tex(r'\mbox{ {{Marginal Cost Curve}} shows the cost of adding more at each quantity.}',
                        tex_to_color_map={'Marginal Cost Curve': DEFINITION})
        curve_def.scale(DEFINITION_SCALE)
        curve_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(mc_def)
        self.play(FadeIn(curve_def))
        q_source.clear_updaters()
        mc_v.clear_updaters()
        mc_dot.clear_updaters()
        self.remove(read_quantity)

        # Return to the same farm: more spinach leaves less land for other uses.
        farm = Rectangle(width=4.5, height=2.6, color=INK, stroke_width=2).move_to([4.15, 0.45, 0])
        farm_name = Tex("Molly's farm", color=INK).next_to(farm, UP, buff=0.3)
        spinach = Polygon([1.9, -0.85, 0], [3.4, -0.85, 0], [3.4, 1.75, 0], [1.9, 1.75, 0],
                          color=SPINACH, stroke_width=0, fill_opacity=0.55)
        spinach_label = Tex('Spinach', color=SPINACH).scale(0.8).next_to(spinach, DOWN, buff=0.25)
        opportunity_price = ValueTracker(4)
        self.remove(offer_label)
        opportunity_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        opportunity_number.next_to(ax.c2p(0, 4), LEFT, buff=0.6)
        opportunity_word = Tex(r'Price \$', color=GUIDE).scale(0.7).next_to(opportunity_number, LEFT, buff=0.04)
        offer_label = VGroup(opportunity_number, opportunity_word)
        self.play(FadeIn(spinach), FadeIn(farm), FadeIn(farm_name), FadeIn(spinach_label), FadeIn(offer_label))

        # One price drives the graph, its readouts, and the farm allocation.
        opportunity_number.add_updater(lambda number: number.set_value(opportunity_price.get_value())
                                       .next_to(ax.c2p(0, opportunity_price.get_value()), LEFT, buff=0.6))
        opportunity_word.add_updater(lambda word: word.next_to(opportunity_number, LEFT, buff=0.04))
        offer_line.add_updater(lambda line: line.set_y(ax.c2p(0, opportunity_price.get_value())[1]))
        q_source[1].num_decimal_places = 2
        q_source[1].add_updater(lambda number: number.set_value(KG_PER_GRAPH_UNIT * (opportunity_price.get_value() - 2)))
        q_source.add_updater(lambda group: group.arrange(RIGHT, buff=0.12)
                            .next_to(ax.c2p(opportunity_price.get_value() - 2, 0), DOWN, buff=0.6))
        mc_v.add_updater(lambda line: line.become(DashedLine(
            ax.c2p(opportunity_price.get_value() - 2, 0),
            ax.c2p(opportunity_price.get_value() - 2, opportunity_price.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.5)))
        mc_dot.add_updater(lambda dot: dot.move_to(ax.c2p(opportunity_price.get_value() - 2,
                                                        opportunity_price.get_value())))
        spinach.add_updater(lambda area: area.set_points_as_corners([
            [1.9, -0.85, 0], [1.9 + 0.75 * (opportunity_price.get_value() - 2), -0.85, 0],
            [1.9 + 0.75 * (opportunity_price.get_value() - 2), 1.75, 0],
            [1.9, 1.75, 0], [1.9, -0.85, 0]]))
        spinach_label.add_updater(lambda label: label.next_to(spinach, DOWN, buff=0.25))
        self.play(opportunity_price.animate.set_value(6), run_time=1.5)
        self.play(opportunity_price.animate.set_value(3), run_time=1.5)
        self.play(opportunity_price.animate.set_value(4), run_time=1.5)

        # Freeze both pictures before dimming them behind the exercise card.
        offer_label.clear_updaters()
        offer_line.clear_updaters()
        q_source.clear_updaters()
        mc_v.clear_updaters()
        mc_dot.clear_updaters()
        spinach.clear_updaters()
        spinach_label.clear_updaters()
        self.remove(opportunity_price)
        self.pause('3.m')

        # ---- 3.n · Exercise Q1, copied from the current exercise sheet.
        stage = VGroup(*self.mobjects)
        stage.save_state()
        card = VGroup(
            Tex('Exercise B2 $|$ Quantity Supplied', color=DEFINITION),
            Tex(r'$P=2+\frac{Q_s}{10}$').scale(0.9),
            Tex('What is quantity supplied at 10 galleons?').scale(0.9),
            Tex('What is marginal cost at 9 pasties?').scale(0.9))
        card[0].scale(1.2)
        card.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(ORIGIN)
        panel = RoundedRectangle(width=13, height=card.get_height() + 1.2,
                                 corner_radius=0.25, color=MUTED, stroke_width=2,
                                 fill_color=BG, fill_opacity=1).move_to(card).set_z_index(50)
        card.align_to(panel, LEFT).shift(RIGHT * 0.65)
        card[1].set_x(panel.get_x())
        for paragraph in card[2:]:
            paragraph.shift(RIGHT * 0.35)
        for glyph in card.get_family():
            glyph.set_z_index(51)  # ManimL does not inherit a group's z-index.
        card = VGroup(panel, card)
        self.play(stage.animate.set_opacity(0.05), FadeIn(card))
        self.pause('3.n')

        # ---- 4.a · Restore the graph and offer $5.
        self.play(Restore(stage), FadeOut(card))
        self.remove(stage)
        self.add(*stage.submobjects)
        self.remove(head, curve_def)
        head = title('What does Molly gain?')
        self.play(FadeOut(q_source), FadeOut(mc_v),
                  FadeOut(spinach), FadeOut(farm), FadeOut(farm_name), FadeOut(spinach_label),
                  FadeOut(mc_dot), FadeOut(offer_line), FadeOut(offer_label), FadeIn(head))
        ps_price = ValueTracker(4)
        ps_price_line = Line(ax.c2p(0, 4), ax.c2p(6, 4), color=GUIDE, stroke_width=2, z_index=10)
        ps_price_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        ps_price_number.next_to(ax.c2p(0, 4), LEFT, buff=0.6)
        ps_price_word = Tex(r'Price \$', color=GUIDE).scale(0.7).next_to(ps_price_number, LEFT, buff=0.04)
        ps_price_line.add_updater(lambda line: line.set_y(ax.c2p(0, ps_price.get_value())[1]))
        ps_price_number.add_updater(lambda number: number.set_value(ps_price.get_value())
                                   .next_to(ax.c2p(0, ps_price.get_value()), LEFT, buff=0.6))
        ps_price_word.add_updater(lambda word: word.next_to(ps_price_number, LEFT, buff=0.04))
        self.add(ps_price_line, ps_price_number, ps_price_word)
        self.play(ps_price.animate.set_value(5), run_time=1.5)
        ps_price_line.clear_updaters()
        ps_price_number.clear_updaters()
        ps_price_word.clear_updaters()
        self.remove(ps_price)
        self.pause('4.a')

        # ---- 4.b.1–4.d.10 · Isolate, widen, and explain one narrow bar at a time.
        revenue_bars = VGroup()
        cost_bars = VGroup()
        ps_bars = VGroup()
        ps_def = Tex(r"\mbox{ {{Producer Surplus}} is the seller's extra value from an exchange.}",
                     tex_to_color_map={'Producer Surplus': DEFINITION})
        ps_def.scale(DEFINITION_SCALE)
        ps_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        base_y = ax.c2p(0, 0)[1]
        price_y = ax.c2p(0, 5)[1]
        self.remove(ax, rest_bars)
        self.add(ax.x_axis, ax.y_axis, *rest_bars)

        for bar_index in range(round(1 / SLICE_WIDTH)):
            left = bar_index * SLICE_WIDTH
            right = left + SLICE_WIDTH
            close_left = ax.c2p(left, 0)[0]
            close_right = close_left + 3 * (ax.c2p(right, 0)[0] - close_left)
            # Use the same flat midpoint cost before, during, and after the close-up.
            slice_mc = 2 + (left + right) / 2
            cost_y = ax.c2p(0, slice_mc)[1]
            selected_bar = rest_bars[bar_index]
            selected_bar.save_state()
            surroundings = VGroup(ax.x_axis, q_lab, q_units, supply, equation, s_lab,
                                  *rest_bars[:bar_index], *rest_bars[bar_index + 1:],
                                  *revenue_bars, *cost_bars, *ps_bars)
            cost_line = Line(ax.c2p(left, slice_mc), ax.c2p(right, slice_mc),
                             color=SUPPLY, stroke_width=3, stroke_opacity=0, z_index=10)

            # One focus move: fade the surroundings as the bar and its MC line widen.
            wide_grey = Polygon([close_left, base_y, 0], [close_right, base_y, 0],
                                [close_right, cost_y, 0], [close_left, cost_y, 0],
                                color=MUTED, stroke_width=2, fill_opacity=0.2)
            wide_cost_line = Line([close_left, cost_y, 0], [close_right, cost_y, 0],
                                  color=SUPPLY, stroke_width=3, z_index=10)
            unit_label = Tex('1 kg', color=INK).scale(0.7).next_to(wide_grey, DOWN, buff=0.25)
            self.add(cost_line)
            self.play(FadeOut(surroundings), Transform(selected_bar, wide_grey),
                      Transform(cost_line, wide_cost_line), FadeIn(unit_label), run_time=0.8)

            # First show what this exchange brings in. Keep the 1 kg cue; omit dollar totals.
            single_revenue = Polygon([close_left, base_y, 0], [close_right, base_y, 0],
                                     [close_right, price_y, 0], [close_left, price_y, 0],
                                     color=INK, stroke_width=2, fill_opacity=0)
            single_cost = Polygon([close_left, base_y, 0], [close_right, base_y, 0],
                                  [close_right, cost_y, 0], [close_left, cost_y, 0],
                                  color=GOV, stroke_width=2, fill_opacity=AREA_OPACITY)
            single_ps = Polygon([close_left, cost_y, 0], [close_right, cost_y, 0],
                                [close_right, price_y, 0], [close_left, price_y, 0],
                                color=SUPPLY, stroke_width=2, fill_opacity=AREA_OPACITY)
            revenue_label = Tex('Revenue', color=INK).scale(0.8)
            revenue_label.next_to(single_revenue.get_corner(UR), RIGHT, buff=0.35).shift(UP * 0.3)
            cost_label = Tex('Cost', color=GOV).scale(0.8).next_to(single_cost, RIGHT, buff=0.35)
            surplus_label = Tex('PS', color=SUPPLY).scale(0.8).next_to(single_ps, RIGHT, buff=0.35)
            if bar_index == 0:
                # Whole-dollar readouts on this first bar only; keep the midpoint geometry.
                cost_label = Tex(r'Cost = \$2', color=GOV).scale(0.8).next_to(single_cost, RIGHT, buff=0.35)
                surplus_number = DecimalNumber(round(5 - slice_mc), num_decimal_places=0, color=SUPPLY)
                surplus_label = VGroup(Tex(r'PS = \$', color=SUPPLY), surplus_number)
                surplus_label.arrange(RIGHT, buff=0.04).scale(0.8).next_to(single_ps, RIGHT, buff=0.35)
            mc_label = Tex('$MC$', color=GUIDE).scale(0.7).next_to(ax.c2p(0, slice_mc), LEFT, buff=0.6)
            self.play(FadeIn(single_revenue), FadeIn(revenue_label), run_time=0.6)
            self.pause(f'4.b.{bar_index + 1}')

            # Cost first, with a teaching pause before surplus.
            self.play(FadeIn(single_cost), FadeIn(cost_label), FadeIn(mc_label), run_time=0.6)
            self.pause(f'4.c.{bar_index + 1}')
            self.play(FadeIn(single_ps), FadeIn(surplus_label), run_time=0.6)
            if bar_index == 0:
                self.play(FadeIn(ps_def))
            self.pause(f'4.d.{bar_index + 1}')

            # On the first bar, compare several prices with this fixed cost.
            if bar_index == 0:
                close_price = ValueTracker(5)
                surplus_number.add_updater(lambda number: number.set_value(round(max(0, close_price.get_value() - slice_mc))))
                ps_price_line.add_updater(lambda line: line.set_y(ax.c2p(0, close_price.get_value())[1]))
                ps_price_number.add_updater(lambda number: number.set_value(close_price.get_value())
                                           .next_to(ax.c2p(0, close_price.get_value()), LEFT, buff=0.6))
                ps_price_word.add_updater(lambda word: word.next_to(ps_price_number, LEFT, buff=0.04))
                single_revenue.add_updater(lambda box: box.set_points_as_corners([
                    [close_left, base_y, 0], [close_right, base_y, 0],
                    [close_right, ax.c2p(0, close_price.get_value())[1], 0],
                    [close_left, ax.c2p(0, close_price.get_value())[1], 0], [close_left, base_y, 0]])
                    .set_stroke(opacity=float(close_price.get_value() >= slice_mc)))
                revenue_label.add_updater(lambda label: label.next_to(single_revenue.get_corner(UR), RIGHT, buff=0.35).shift(UP * 0.3)
                                          .set_opacity(float(close_price.get_value() >= slice_mc)))
                single_cost.add_updater(lambda box: box.set_fill(opacity=AREA_OPACITY if close_price.get_value() >= slice_mc else 0)
                                        .set_stroke(opacity=float(close_price.get_value() >= slice_mc)))
                cost_label.add_updater(lambda label: label.set_opacity(float(close_price.get_value() >= slice_mc)))
                single_ps.add_updater(lambda box: box.set_points_as_corners([
                    [close_left, cost_y, 0], [close_right, cost_y, 0],
                    [close_right, ax.c2p(0, max(slice_mc, close_price.get_value()))[1], 0],
                    [close_left, ax.c2p(0, max(slice_mc, close_price.get_value()))[1], 0], [close_left, cost_y, 0]])
                    .set_fill(opacity=AREA_OPACITY if close_price.get_value() > slice_mc else 0)
                    .set_stroke(opacity=float(close_price.get_value() > slice_mc)))
                surplus_label.add_updater(lambda label: label.arrange(RIGHT, buff=0.04).next_to(single_ps, RIGHT, buff=0.35)
                                          .set_opacity(float(close_price.get_value() > slice_mc)))
                self.play(close_price.animate.set_value(3), run_time=1.5)
                self.pause('4.d.1.price-low')
                self.play(close_price.animate.set_value(1.5), run_time=1.5)
                self.pause('4.d.1.no-sale')
                self.play(close_price.animate.set_value(4), run_time=1.5)
                self.pause('4.d.1.price-high')
                self.play(close_price.animate.set_value(5), run_time=1.5)
                self.pause('4.d.1.price-reset')
                ps_price_line.clear_updaters()
                ps_price_number.clear_updaters()
                ps_price_word.clear_updaters()
                single_revenue.clear_updaters()
                revenue_label.clear_updaters()
                single_cost.clear_updaters()
                cost_label.clear_updaters()
                single_ps.clear_updaters()
                surplus_number.clear_updaters()
                surplus_label.clear_updaters()
                self.remove(close_price)

            # Return in one move: shrink the bar as the full graph fades back in.
            self.play(FadeOut(revenue_label), FadeOut(cost_label), FadeOut(surplus_label), FadeOut(mc_label), FadeOut(unit_label), run_time=0.4)
            narrow_revenue = Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 5), ax.c2p(left, 5),
                                     color=INK, fill_opacity=0, stroke_width=1)
            narrow_cost = Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                                  ax.c2p(right, slice_mc), ax.c2p(left, slice_mc),
                                  color=GOV, fill_opacity=AREA_OPACITY, stroke_width=1)
            narrow_ps = Polygon(ax.c2p(left, slice_mc), ax.c2p(right, slice_mc),
                                ax.c2p(right, 5), ax.c2p(left, 5),
                                color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=1)
            narrow_cost_line = Line(ax.c2p(left, slice_mc), ax.c2p(right, slice_mc),
                                    color=SUPPLY, stroke_width=1, stroke_opacity=0, z_index=10)
            revenue_bars.add(single_revenue)
            cost_bars.add(single_cost)
            ps_bars.add(single_ps)
            self.play(FadeIn(surroundings), Restore(selected_bar),
                      Transform(single_revenue, narrow_revenue), Transform(single_cost, narrow_cost),
                      Transform(single_ps, narrow_ps), Transform(cost_line, narrow_cost_line), run_time=0.8)
            self.remove(surroundings, cost_line)
            self.add(*surroundings.submobjects)
            self.bring_to_front(supply, ps_price_line)
            if bar_index < round(1 / SLICE_WIDTH) - 1:
                self.pause(f'4.return.{bar_index + 1}')

        # ---- 4.e · Continue directly: cost, then PS for each remaining bar.
        self.remove(ax.x_axis, ax.y_axis)
        self.add(ax)
        for left in np.arange(1, 3, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            slice_mc = 2 + (left + right) / 2
            revenue = Polygon(ax.c2p(left, 0), ax.c2p(right, 0), ax.c2p(right, 5), ax.c2p(left, 5),
                              color=INK, fill_opacity=0, stroke_width=1)
            cost = Polygon(ax.c2p(left, 0), ax.c2p(right, 0),
                           ax.c2p(right, slice_mc), ax.c2p(left, slice_mc),
                           color=GOV, fill_opacity=AREA_OPACITY, stroke_width=1)
            gained = Polygon(ax.c2p(left, slice_mc), ax.c2p(right, slice_mc),
                             ax.c2p(right, 5), ax.c2p(left, 5),
                             color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=1)
            # Record each slice before its animation so the viewer retains the last one.
            revenue_bars.add(revenue)
            cost_bars.add(cost)
            ps_bars.add(gained)
            self.play(FadeIn(revenue), FadeIn(cost), run_time=0.2)
            self.play(FadeIn(gained), run_time=0.2)
        self.bring_to_front(supply, ps_price_line)
        self.pause('4.e')

        # ---- 4.g · Trace the chosen price, leaving quantity to solve for.
        self.remove(ps_price_line)
        ps_price_line = DashedLine(ax.c2p(0, 5), ax.c2p(3, 5), color=GUIDE, z_index=10).set_opacity(0.8)
        ps_drop = DashedLine(ax.c2p(3, 5), ax.c2p(3, 0), color=GUIDE, z_index=10).set_opacity(0.8)
        ps_dot = Dot(ax.c2p(3, 5), color=GUIDE, z_index=11)
        ps_question = Tex('$Q_s=?$', color=GUIDE).scale(0.7).next_to(ax.c2p(3, 0), DOWN, buff=0.6)
        equality = Tex('$MC=P$', color=GUIDE).scale(0.7).next_to(ps_dot, UL, buff=0.3)
        for glyph in equality.get_family():
            glyph.set_z_index(20)
        ax.x_axis.numbers[2].set_opacity(0)
        self.play(FadeIn(ps_price_line), FadeIn(ps_dot))
        self.play(FadeIn(ps_drop))
        self.play(FadeIn(ps_question), FadeIn(equality))
        self.bring_to_front(ps_price_line, ps_drop, ps_dot)
        self.pause('4.g')

        # ---- 4.g.1 · Carry price into the equation, then quantity back to the graph.
        ps_substitution = VGroup(Tex('$5$', color=GUIDE), Tex('$=2+Q_s/10$', tex_to_color_map={'Q_s': GUIDE}))
        ps_substitution.arrange(RIGHT, buff=0.12)
        ps_rearrange = Tex('$Q_s=10(5-2)$', tex_to_color_map={'Q_s': GUIDE, '5': GUIDE})
        ps_answer = VGroup(Tex('$Q_s=$'), Tex('$30$')).arrange(RIGHT, buff=0.12).set_color(GUIDE)
        ps_work = VGroup(ps_substitution, ps_rearrange, ps_answer).scale(0.8)
        ps_work.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT)
        math_divider.set_opacity(0.5)
        self.play(FadeIn(math_divider), TransformFromCopy(ps_price_number, ps_substitution[0]),
                  FadeIn(ps_substitution[1]))
        self.play(FadeIn(ps_rearrange))
        self.play(FadeIn(ps_answer))
        ps_quantity = VGroup(Tex('$Q_s=$'), Tex('$30$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        ps_quantity.move_to(ps_question)
        self.play(FadeOut(ps_question), FadeIn(ps_quantity[0]), TransformFromCopy(ps_answer[1], ps_quantity[1]),
                  ax.x_axis.numbers[2].animate.set_opacity(1))
        self.pause('4.g.1')

        # ---- 4.h · Read the triangle traced by the narrow flat bars.
        triangle = Polygon(ax.c2p(0, 2), ax.c2p(0, 5), ax.c2p(3, 5),
                           color=SUPPLY, fill_opacity=0, stroke_width=4, z_index=5)
        self.play(FadeOut(ps_work), FadeOut(equality), FadeIn(triangle))
        self.pause('4.h')

        # ---- 4.i · Keep the same formula prefix through the calculation.
        area = VGroup(Tex(r'PS $=\frac12$', tex_to_color_map={'PS': SUPPLY}),
                      Tex('$h$', color=FOCUS), Tex('$b$', color=FOCUS))
        area.arrange(RIGHT, buff=0.15).scale(0.8).move_to(MATH_AT)
        self.play(FadeIn(area))
        self.pause('4.i')

        # ---- 4.j · The equation's constant is the supply intercept.
        intercept_term = equation.get_part_by_tex('2')
        intercept_label = Tex('$2$', color=FOCUS).scale(0.7).next_to(ax.c2p(0, 2), LEFT, buff=0.45)
        intercept_dot = Dot(ax.c2p(0, 2), color=FOCUS, z_index=21)
        ax.y_axis.numbers[0].set_opacity(0)
        self.play(intercept_term.animate.set_color(FOCUS))
        self.play(TransformFromCopy(intercept_term, intercept_label), FadeIn(intercept_dot))
        self.pause('4.j')

        # ---- 4.j.1 · Price minus the intercept measures the vertical gap.
        h_bar = Line(ax.c2p(0, 2), ax.c2p(0, 5), color=FOCUS, stroke_width=4, z_index=20)
        height_difference = VGroup(Tex('$h=$', color=FOCUS), Tex('$5$', color=GUIDE),
                                  Tex('$-$'), Tex('$2$', color=FOCUS))
        height_difference.arrange(RIGHT, buff=0.12).scale(0.8).move_to(MATH_AT + DOWN * 0.95)
        self.play(FadeIn(h_bar), FadeIn(height_difference[0]), FadeIn(height_difference[2]),
                  TransformFromCopy(ps_price_number, height_difference[1]),
                  TransformFromCopy(intercept_label, height_difference[3]))
        self.pause('4.j.1')

        # ---- 4.j.2 · Put the calculated height beside the triangle.
        height_answer = VGroup(Tex('$h=$'), Tex('$3$')).arrange(RIGHT, buff=0.12).scale(0.8).set_color(FOCUS)
        height_answer.next_to(height_difference, DOWN, buff=0.35)
        self.play(FadeIn(height_answer))
        h_label = VGroup(Tex('$h=$'), Tex('$3$')).arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        h_label.next_to(ax.c2p(0, 3.5), LEFT, buff=0.45)
        self.play(FadeIn(h_label[0]), TransformFromCopy(height_answer[1], h_label[1]))
        self.pause('4.j.2')

        # ---- 4.k · Base is the chosen quantity.
        self.play(FadeOut(height_difference), FadeOut(height_answer), FadeOut(intercept_label), FadeOut(intercept_dot),
                  intercept_term.animate.set_color(INK), ax.y_axis.numbers[0].animate.set_opacity(1))
        b_bar = Line(ax.c2p(0, 0), ax.c2p(3, 0), color=FOCUS, stroke_width=4, z_index=20)
        b_label = VGroup(Tex('$b=$'), Tex('$30$')).arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        b_label.next_to(ax.c2p(1.5, 0), UP, buff=0.15)
        self.play(FadeIn(b_bar), FadeIn(b_label[0]), TransformFromCopy(ps_quantity[1], b_label[1]))
        self.pause('4.k')

        # ---- 4.l · Fill the two slots; do not rewrite the prefix.
        h_value = Tex('$(3)$', color=FOCUS).scale(0.8)
        b_value = Tex('$(30)$', color=FOCUS).scale(0.8)
        # Lay out the longer equation, then slide the existing prefix into position.
        filled_area = VGroup(area[0].copy(), h_value, b_value).arrange(RIGHT, buff=0.15).move_to(MATH_AT)
        self.play(area[0].animate.move_to(filled_area[0]), FadeOut(area[1]),
                  area[2].animate.move_to(b_value), TransformFromCopy(h_label[1], h_value))
        self.play(FadeOut(area[2]), TransformFromCopy(b_label[1], b_value))
        area_answer = Tex(r'$=\$45.00$').scale(0.8).next_to(filled_area, DOWN, buff=0.35)
        self.play(FadeIn(area_answer))
        self.pause('4.l')

        # ---- 5.a · Exercise Q2, no answer revealed.
        stage = VGroup(*self.mobjects)
        stage.save_state()
        card = VGroup(Tex('Exercise B2 $|$ Producer Surplus', color=DEFINITION),
                      Tex(r'$P=2+\frac{Q_s}{10}$').scale(0.9),
                      Tex('What is producer surplus at 10 galleons?').scale(0.9))
        card[0].scale(1.2)
        card.arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(ORIGIN)
        panel = RoundedRectangle(width=13, height=card.get_height() + 1.2,
                                 corner_radius=0.25, color=MUTED, stroke_width=2,
                                 fill_color=BG, fill_opacity=1).move_to(card).set_z_index(50)
        card.align_to(panel, LEFT).shift(RIGHT * 0.65)
        card[1].set_x(panel.get_x())
        for paragraph in card[2:]:
            paragraph.shift(RIGHT * 0.35)
        for glyph in card.get_family():
            glyph.set_z_index(51)
        card = VGroup(panel, card)
        self.play(stage.animate.set_opacity(0.05), FadeIn(card))
        self.pause('5.a')
        self.play(FadeOut(stage), FadeOut(card))
        self.clear()

        # ---- 6.a · Two sellers face the same price; quantities add.
        head = title('What happens when we consider everyone?')
        sum_axes = VGroup()
        sum_names = VGroup()
        sum_labels = VGroup()
        for center, name, color in [(-5, 'Molly', MOLLY), (0, 'Andrew', ANDREW), (5, 'Molly + Andrew', INK)]:
            small_ax = style_axes(
                [0, 8, 2], [0, 8.5, 2], x_length=3.7, y_length=3.7, ticks=True,
                x_axis_config={'numbers_to_include': [2, 4, 6],
                               'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
                y_axis_config={'numbers_to_include': [2, 4, 6, 8],
                               'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}})
            small_ax.shift(np.array([center, -0.1, 0]) - (small_ax.c2p(0, 0) + small_ax.c2p(8, 8.5)) / 2)
            for number in small_ax.x_axis.numbers:
                number_center = number.get_center()
                number.set_value(number.get_value() * KG_PER_GRAPH_UNIT).move_to(number_center)
            sum_axes.add(small_ax)
            name_label = Tex(name, color=color).scale(0.8).move_to([center, 2.4, 0])
            sum_names.add(name_label)
            sum_labels.add(Tex('P', color=INK).scale(0.7).next_to(small_ax.c2p(0, 8.5), LEFT, buff=0.2),
                           Tex('Q', color=INK).scale(0.7).next_to(small_ax.c2p(8, 0), DOWN, buff=0.3))
        molly_ax, andrew_ax, pair_ax = sum_axes
        molly_curve = Line(molly_ax.c2p(0, 2), molly_ax.c2p(6, 8), color=MOLLY, z_index=3)
        andrew_curve = Line(andrew_ax.c2p(0, 2), andrew_ax.c2p(3, 8), color=ANDREW, z_index=3)
        molly_eq = Tex('$P=2+Q_s/10$').scale(0.7).move_to([-5, 1.9, 0])
        andrew_eq = Tex('$P=2+Q_s/5$').scale(0.7).move_to([0, 1.9, 0])
        sum_price = ValueTracker(4)
        common_price = DashedLine(molly_ax.c2p(0, 4), pair_ax.c2p(8, 4), color=GUIDE, z_index=10).set_opacity(0.45)
        common_number = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(0.7)
        common_number.next_to(molly_ax.c2p(0, 4), LEFT, buff=0.2)
        common_dollar = Tex(r'\$', color=GUIDE).scale(0.7).next_to(common_number, LEFT, buff=0.02)
        molly_dot = Dot(molly_ax.c2p(2, 4), color=GUIDE, z_index=11)
        andrew_dot = Dot(andrew_ax.c2p(1, 4), color=GUIDE, z_index=11)
        molly_drop = DashedLine(molly_ax.c2p(2, 4), molly_ax.c2p(2, 0), color=GUIDE, z_index=10).set_opacity(0.6)
        andrew_drop = DashedLine(andrew_ax.c2p(1, 4), andrew_ax.c2p(1, 0), color=GUIDE, z_index=10).set_opacity(0.6)
        molly_q = DecimalNumber(20, num_decimal_places=0, color=GUIDE).scale(0.8)
        molly_q.next_to(molly_ax.c2p(2, 0), DOWN, buff=0.6)
        andrew_q = DecimalNumber(10, num_decimal_places=0, color=GUIDE).scale(0.8)
        andrew_q.next_to(andrew_ax.c2p(1, 0), DOWN, buff=0.6)
        self.play(FadeIn(head), FadeIn(sum_axes), FadeIn(sum_names), FadeIn(sum_labels),
                  FadeIn(molly_curve), FadeIn(andrew_curve), FadeIn(molly_eq), FadeIn(andrew_eq))
        self.play(FadeIn(common_price), FadeIn(common_number), FadeIn(common_dollar), FadeIn(molly_dot), FadeIn(andrew_dot),
                  FadeIn(molly_drop), FadeIn(andrew_drop), FadeIn(molly_q), FadeIn(andrew_q))
        common_price.add_updater(lambda line: line.set_y(molly_ax.c2p(0, sum_price.get_value())[1]))
        common_number.add_updater(lambda number: number.set_value(sum_price.get_value())
                                 .next_to(molly_ax.c2p(0, sum_price.get_value()), LEFT, buff=0.2))
        common_dollar.add_updater(lambda dollar: dollar.next_to(common_number, LEFT, buff=0.02))
        molly_dot.add_updater(lambda dot: dot.move_to(molly_ax.c2p(sum_price.get_value() - 2, sum_price.get_value())))
        andrew_dot.add_updater(lambda dot: dot.move_to(andrew_ax.c2p((sum_price.get_value() - 2) / 2, sum_price.get_value())))
        molly_drop.add_updater(lambda line: line.become(DashedLine(
            molly_ax.c2p(sum_price.get_value() - 2, sum_price.get_value()), molly_ax.c2p(sum_price.get_value() - 2, 0),
            color=GUIDE, z_index=10).set_opacity(0.6)))
        andrew_drop.add_updater(lambda line: line.become(DashedLine(
            andrew_ax.c2p((sum_price.get_value() - 2) / 2, sum_price.get_value()),
            andrew_ax.c2p((sum_price.get_value() - 2) / 2, 0), color=GUIDE, z_index=10).set_opacity(0.6)))
        molly_q.add_updater(lambda number: number.set_value(KG_PER_GRAPH_UNIT * (sum_price.get_value() - 2))
                           .next_to(molly_ax.c2p(sum_price.get_value() - 2, 0), DOWN, buff=0.6))
        andrew_q.add_updater(lambda number: number.set_value(KG_PER_GRAPH_UNIT * (sum_price.get_value() - 2) / 2)
                            .next_to(andrew_ax.c2p((sum_price.get_value() - 2) / 2, 0), DOWN, buff=0.6))
        self.pause('6.a')

        # ---- 6.b · Put the addition at the combined quantity's axis position.
        addition = VGroup(Tex('$20$', color=GUIDE), Tex('$+$'), Tex('$10$', color=GUIDE))
        addition.arrange(RIGHT, buff=0.12).scale(0.7).next_to(pair_ax.c2p(3, 0), DOWN, buff=0.6)
        self.play(TransformFromCopy(molly_q.copy().clear_updaters(), addition[0]),
                  TransformFromCopy(andrew_q.copy().clear_updaters(), addition[2]),
                  FadeIn(addition[1]))
        self.pause('6.b')

        # ---- 6.b.1 · Reveal the first horizontal sum.
        pair_dot4 = Dot(pair_ax.c2p(3, 4), color=SUPPLY, z_index=11)
        pair_drop4 = DashedLine(pair_ax.c2p(3, 4), pair_ax.c2p(3, 0), color=GUIDE, z_index=10).set_opacity(0.6)
        pair_q4 = Tex('$Q_s=30$', color=GUIDE).scale(0.7).next_to(pair_ax.c2p(3, 0), DOWN, buff=0.6)
        self.play(ReplacementTransform(addition, pair_q4), FadeIn(pair_dot4), FadeIn(pair_drop4))
        self.pause('6.b.1')

        # ---- 6.c · The shared price moves; both sellers' guides remain.
        self.play(FadeOut(pair_drop4), FadeOut(pair_q4))
        self.play(sum_price.animate.set_value(6), run_time=1.5)
        addition = VGroup(Tex('$40$', color=GUIDE), Tex('$+$'), Tex('$20$', color=GUIDE))
        addition.arrange(RIGHT, buff=0.12).scale(0.7).next_to(pair_ax.c2p(6, 0), DOWN, buff=0.6)
        self.play(TransformFromCopy(molly_q.copy().clear_updaters(), addition[0]),
                  TransformFromCopy(andrew_q.copy().clear_updaters(), addition[2]),
                  FadeIn(addition[1]))
        self.pause('6.c')

        # ---- 6.d · This curve is the sum of these two sellers only.
        pair_dot6 = Dot(pair_ax.c2p(6, 6), color=SUPPLY, z_index=11)
        pair_drop6 = DashedLine(pair_ax.c2p(6, 6), pair_ax.c2p(6, 0), color=GUIDE, z_index=10).set_opacity(0.6)
        pair_q6 = Tex('$Q_s=60$', color=GUIDE).scale(0.7).next_to(pair_ax.c2p(6, 0), DOWN, buff=0.6)
        pair_curve = Line(pair_ax.c2p(0, 2), pair_ax.c2p(8, 2 + 16 / 3), color=SUPPLY)
        self.play(ReplacementTransform(addition, pair_q6), FadeIn(pair_dot6), FadeIn(pair_drop6))
        self.play(FadeIn(pair_curve))
        self.bring_to_front(pair_dot4, pair_dot6)
        self.pause('6.d')

        # ---- 6.e · Quantities, not prices, are added at each price.
        market_def = Tex(r"\mbox{ {{Market Supply}} sums sellers' individual quantities supplied at each price.}",
                         tex_to_color_map={'Market Supply': DEFINITION})
        market_def.scale(DEFINITION_SCALE)
        market_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(market_def))
        self.pause('6.e')
        # ---- 7.a · A brief PS reminder on the existing combined-sellers graph.
        self.play(FadeOut(pair_drop6), FadeOut(pair_q6))
        self.play(sum_price.animate.set_value(4), run_time=1.5)
        self.play(FadeIn(pair_drop4), FadeIn(pair_q4), pair_dot6.animate.set_opacity(0.35))
        combined_rest = VGroup()
        combined_ps = VGroup()
        for left in np.arange(0, 8, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            cost_slice = Polygon(pair_ax.c2p(left, 0), pair_ax.c2p(right, 0),
                                 pair_ax.c2p(right, 2 + 2 * right / 3),
                                 pair_ax.c2p(left, 2 + 2 * left / 3))
            cost_slice.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            combined_rest.add(cost_slice)
            if left < 3:
                ps_slice = Polygon(pair_ax.c2p(left, 2 + 2 * left / 3),
                                   pair_ax.c2p(right, 2 + 2 * right / 3),
                                   pair_ax.c2p(right, 4), pair_ax.c2p(left, 4),
                                   color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=1)
                combined_ps.add(ps_slice)
        self.remove(market_def)
        market_ps_def = Tex(r'\mbox{ {{Producer Surplus}} is above supply and below price, over the quantity sold.}',
                            tex_to_color_map={'Producer Surplus': DEFINITION})
        market_ps_def.scale(DEFINITION_SCALE)
        market_ps_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(combined_rest), FadeIn(combined_ps), FadeIn(market_ps_def))
        self.bring_to_front(pair_curve, common_price, pair_drop4, pair_dot4)
        self.pause('7.a')
        for mob in self.mobjects:
            mob.clear_updaters()
        self.remove(sum_price)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 8.a · Bring the two sides together next time.
        head = title('What determines the price?')
        closing_axes = VGroup()
        closing_axis_labels = VGroup()
        for center in [-3.7, 3.7]:
            closing_ax = style_axes([0, 8, 2], [0, 8, 2], x_length=5, y_length=4.3)
            closing_ax.shift(np.array([center, -0.2, 0])
                             - (closing_ax.c2p(0, 0) + closing_ax.c2p(8, 8)) / 2)
            closing_axes.add(closing_ax)
            closing_axis_labels.add(
                Tex('P', color=INK).scale(0.8).next_to(closing_ax.c2p(0, 8), LEFT, buff=0.25),
                Tex('Q', color=INK).scale(0.8).next_to(closing_ax.c2p(8, 0), DOWN, buff=0.35))
        demand_ax, supply_ax = closing_axes
        demand_name = Tex('Demand', color=INK).scale(0.8).move_to([-3.7, 2.5, 0])
        supply_name = Tex('Supply', color=INK).scale(0.8).move_to([3.7, 2.5, 0])
        demand_curve = Line(demand_ax.c2p(0, 8), demand_ax.c2p(8, 0), color=DEMAND, z_index=3)
        supply_curve = Line(supply_ax.c2p(0, 2), supply_ax.c2p(6, 8), color=SUPPLY, z_index=3)
        next_time = Tex('Next time...', color=DEFINITION).scale(0.9).to_edge(DOWN, buff=0.25)

        # One price moves both decisions; keep the closing teaser qualitative.
        closing_price = ValueTracker(4.5)
        closing_grey = VGroup()
        closing_cs = VGroup()
        closing_ps = VGroup()

        # Demand: grey below price; teal between price and willingness to pay.
        for left in np.arange(0, 8, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            edge = np.clip(8 - closing_price.get_value(), left, right)
            grey = Polygon(
                demand_ax.c2p(left, 0), demand_ax.c2p(right, 0),
                demand_ax.c2p(right, min(4.5, 8 - right)), demand_ax.c2p(edge, min(4.5, 8 - edge)),
                demand_ax.c2p(left, min(4.5, 8 - left)))
            grey.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            grey.add_updater(lambda bar, left=left, right=right: bar.set_points_as_corners([
                demand_ax.c2p(left, 0), demand_ax.c2p(right, 0),
                demand_ax.c2p(right, min(closing_price.get_value(), 8 - right)),
                demand_ax.c2p(np.clip(8 - closing_price.get_value(), left, right),
                              min(closing_price.get_value(), 8 - np.clip(8 - closing_price.get_value(), left, right))),
                demand_ax.c2p(left, min(closing_price.get_value(), 8 - left)), demand_ax.c2p(left, 0)]))
            closing_grey.add(grey)
            cs = Polygon(demand_ax.c2p(left, 4.5), demand_ax.c2p(edge, 4.5),
                         demand_ax.c2p(edge, max(4.5, 8 - edge)), demand_ax.c2p(left, max(4.5, 8 - left)),
                         color=DEMAND, fill_opacity=AREA_OPACITY, stroke_width=1, z_index=1)
            cs.add_updater(lambda bar, left=left, right=right: bar.set_points_as_corners([
                demand_ax.c2p(left, closing_price.get_value()),
                demand_ax.c2p(np.clip(8 - closing_price.get_value(), left, right), closing_price.get_value()),
                demand_ax.c2p(np.clip(8 - closing_price.get_value(), left, right),
                              max(closing_price.get_value(), 8 - np.clip(8 - closing_price.get_value(), left, right))),
                demand_ax.c2p(left, max(closing_price.get_value(), 8 - left)),
                demand_ax.c2p(left, closing_price.get_value())]))
            closing_cs.add(cs)

        # Supply: grey costs stay under the curve; orange PS reaches the price.
        for left in np.arange(0, 6, SLICE_WIDTH):
            right = left + SLICE_WIDTH
            edge = np.clip(closing_price.get_value() - 2, left, right)
            grey = Polygon(supply_ax.c2p(left, 0), supply_ax.c2p(right, 0),
                           supply_ax.c2p(right, 2 + right), supply_ax.c2p(left, 2 + left))
            grey.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            closing_grey.add(grey)
            ps = Polygon(supply_ax.c2p(left, min(4.5, 2 + left)), supply_ax.c2p(edge, min(4.5, 2 + edge)),
                         supply_ax.c2p(edge, 4.5), supply_ax.c2p(left, 4.5),
                         color=SUPPLY, fill_opacity=AREA_OPACITY, stroke_width=1, z_index=1)
            ps.add_updater(lambda bar, left=left, right=right: bar.set_points_as_corners([
                supply_ax.c2p(left, min(closing_price.get_value(), 2 + left)),
                supply_ax.c2p(np.clip(closing_price.get_value() - 2, left, right),
                              min(closing_price.get_value(), 2 + np.clip(closing_price.get_value() - 2, left, right))),
                supply_ax.c2p(np.clip(closing_price.get_value() - 2, left, right), closing_price.get_value()),
                supply_ax.c2p(left, closing_price.get_value()),
                supply_ax.c2p(left, min(closing_price.get_value(), 2 + left))]))
            closing_ps.add(ps)

        closing_price_line = DashedLine(demand_ax.c2p(0, 4.5), supply_ax.c2p(8, 4.5),
                                        color=GUIDE, z_index=10).set_opacity(0.6)
        closing_price_label = Tex('Price', color=GUIDE).scale(0.7)
        closing_price_label.next_to(demand_ax.c2p(0, 4.5), LEFT, buff=0.3)
        demand_dot = Dot(demand_ax.c2p(3.5, 4.5), color=GUIDE, z_index=11)
        supply_dot = Dot(supply_ax.c2p(2.5, 4.5), color=GUIDE, z_index=11)
        demand_drop = DashedLine(demand_ax.c2p(3.5, 4.5), demand_ax.c2p(3.5, 0),
                                 color=GUIDE, z_index=10).set_opacity(0.6)
        supply_drop = DashedLine(supply_ax.c2p(2.5, 4.5), supply_ax.c2p(2.5, 0),
                                 color=GUIDE, z_index=10).set_opacity(0.6)
        demand_quantity = Tex('$Q_d$', color=GUIDE).scale(0.8)
        demand_quantity.next_to(demand_ax.c2p(3.5, 0), DOWN, buff=0.45)
        supply_quantity = Tex('$Q_s$', color=GUIDE).scale(0.8)
        supply_quantity.next_to(supply_ax.c2p(2.5, 0), DOWN, buff=0.45)
        self.play(FadeIn(head), FadeIn(closing_axes), FadeIn(closing_axis_labels),
                  FadeIn(demand_name), FadeIn(supply_name), FadeIn(demand_curve), FadeIn(supply_curve),
                  FadeIn(next_time))
        self.play(FadeIn(closing_price_line), FadeIn(closing_price_label),
                  FadeIn(demand_dot), FadeIn(supply_dot), FadeIn(demand_drop), FadeIn(supply_drop),
                  FadeIn(demand_quantity), FadeIn(supply_quantity))
        self.play(FadeIn(closing_grey), FadeIn(closing_cs), FadeIn(closing_ps))
        closing_price_line.add_updater(lambda line: line.set_y(demand_ax.c2p(0, closing_price.get_value())[1]))
        closing_price_label.add_updater(lambda label: label.next_to(
            demand_ax.c2p(0, closing_price.get_value()), LEFT, buff=0.3))
        demand_dot.add_updater(lambda dot: dot.move_to(
            demand_ax.c2p(8 - closing_price.get_value(), closing_price.get_value())))
        supply_dot.add_updater(lambda dot: dot.move_to(
            supply_ax.c2p(closing_price.get_value() - 2, closing_price.get_value())))
        demand_drop.add_updater(lambda line: line.become(DashedLine(
            demand_ax.c2p(8 - closing_price.get_value(), closing_price.get_value()),
            demand_ax.c2p(8 - closing_price.get_value(), 0), color=GUIDE, z_index=10).set_opacity(0.6)))
        supply_drop.add_updater(lambda line: line.become(DashedLine(
            supply_ax.c2p(closing_price.get_value() - 2, closing_price.get_value()),
            supply_ax.c2p(closing_price.get_value() - 2, 0), color=GUIDE, z_index=10).set_opacity(0.6)))
        demand_quantity.add_updater(lambda label: label.next_to(
            demand_ax.c2p(8 - closing_price.get_value(), 0), DOWN, buff=0.45))
        supply_quantity.add_updater(lambda label: label.next_to(
            supply_ax.c2p(closing_price.get_value() - 2, 0), DOWN, buff=0.45))
        self.play(closing_price.animate.set_value(5.5), run_time=1.5)
        self.play(closing_price.animate.set_value(3.5), run_time=2)
        self.play(closing_price.animate.set_value(4.5), run_time=1.5)
        self.pause('8.a')
