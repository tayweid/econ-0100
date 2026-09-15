# maniml 03_Code.py EpisodeB1
# Episode B1 | Demand
# Read top to bottom: each Bxx section builds the next pause in the lecture.
# Edit the coordinates, text, and self.play() calls in that section directly.
# Shared Graphite functions supply only the course's standard styling/cards.
# The small PPF functions below are retained from B0's opening animation.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes

def key_in(tex, time_per_char=0.05):
    """Letter-by-letter reveal: ShowIncreasingSubsets over the Tex's glyphs.
    (maniml's AddTextLetterByLetter is an unexported alias of the word-wise
    add, and Write is the stroke-drawing creation look — neither keys in.)"""
    glyphs = VGroup(*tex.family_members_with_points())
    return ShowIncreasingSubsets(glyphs, run_time=time_per_char * len(glyphs), rate_func=linear)


class EpisodeB1(Scene):
    """One continuous lecture, with an editable section at each pause."""

    default_camera_config = {'fps': 15}

    def construct(self):

        self.camera.fps = 15  # The viewer otherwise overrides the scene default to 30.

        # Layout: familiar 7-by-6 plot, uniformly scaled; math to its right.
        GRAPH_W, GRAPH_H = 7.0, 6.0
        GRAPH_SCALE = 0.8
        GRAPH_AT = np.array([-2.6, 0.15, 0])
        MATH_AT = np.array([1.1, 0.7, 0])
        REST_OPACITY = 0.10
        HER = [(0, 4), (1, 2), (2, 1), (4, 0.5), (6, 0.25)]

        # B01 ---------------------------------------------------------

        squares = bumper_raster(self)

        # B01b --------------------------------------------------------

        flicker(self, squares)

        # B01c --------------------------------------------------------

        label = bumper_title(self, squares, 'B', 1)
        thesis = (Tex('\\textit{Demand: a simple way to organize preferences.}')
                  .scale(1.1).set_color(CAPTION).next_to(label, DOWN, buff=0.5))
        self.play(FadeIn(thesis))
        self.pause()

        FadeAll(self)
        # B02 ---------------------------------------------------------
        # the Fall-2024 'Animation -1'

        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B02b ---------------------------------------------------------
        # the Part A stage: guide title with subtitle, the PPF close under it

        FadeAll(self)
        self.camera.frame.set(width=15).move_to(LEFT * 0.5)   # framed in a touch on Part A
        part_a = title('Part A')
        part_a_sub = subtitle(part_a, 'The core economic idea.')

        ppf_ax = style_axes(x_range=[0, 100, 100], y_range=[0, 100, 100],
                        x_length=7, y_length=7).scale(0.7).move_to(LEFT * 4.5 + DOWN * 0.3)
        y_label = Tex('A').set_color(INK).next_to(ppf_ax.c2p(0, 100), LEFT, buff=0.3)
        x_label = Tex('B').set_color(INK).next_to(ppf_ax.c2p(100, 0), DOWN, buff=0.35)

        alpha = ValueTracker(1)

        def Linear_PPF(x):
            return 100 - x

        def Bowed_PPF(x):
            a = alpha.get_value()
            return (100**a - x**a)**(1 / a)

        def PPF_Group():
            linear_ppf = ppf_ax.plot(Linear_PPF, color=MUTED, x_range=(0, 100))
            linear_ppf.z_index = -1
            # the frontier that bows past the line is the gain from coordinating
            bowed_ppf = ppf_ax.plot(Bowed_PPF, color=TRADE, x_range=(0, 100, 0.1))
            bowed_ppf.z_index = -1
            return VGroup(linear_ppf, bowed_ppf)

        # fade in a still copy — always_redraw would repaint at full opacity
        # mid-fade (the FadeAll gotcha) and snap in instead of fading
        ppf_static = PPF_Group()
        self.play(FadeIn(part_a), FadeIn(part_a_sub), FadeIn(ppf_ax),
                  FadeIn(y_label), FadeIn(x_label), FadeIn(ppf_static))
        self.pause()

        # B02c --------------------------------------------------------
        # Part A's core idea: coordination bows the frontier out; the arrow
        # sits in the opening gap, the thesis lands in gold under the graph

        ppf_group = always_redraw(PPF_Group)   # live from here; at alpha=1 it matches the still
        self.remove(ppf_static)
        self.add(ppf_group)
        arrow = Arrow(start=ppf_ax.c2p(45, 56), end=ppf_ax.c2p(57, 67), buff=0).set_color(FOCUS)
        core_line = (Tex('\\textit{Specialization and trade can benefit both parties.}')
                     .scale(0.7).set_color(DEFINITION).move_to(LEFT * 3.95 + DOWN * 3.5))
        self.play(FadeIn(arrow), FadeIn(core_line), alpha.animate.set_value(1.5))
        self.remove(alpha)   # an animated tracker sits in scene.mobjects; the closing card's stage grab wants only drawables
        self.pause()

        # B03 ---------------------------------------------------------
        # Part B fades in as the camera eases out, just enough to feel it

        part_b = (Tex('Part B').set_color(TITLE).scale(SCALE_TITLE)
                  .move_to(RIGHT * 1.85).align_to(part_a, UP))
        part_b_sub = (VGroup(Tex(narration('Competitive markets can efficiently')),
                             Tex(narration('coordinate our decisions.')))
                      .arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(SCALE_CAPTION)
                      .set_color(CAPTION).next_to(part_b, DOWN, buff=0.25).align_to(part_b, LEFT))
        self.play(FadeIn(part_b), FadeIn(part_b_sub),
                  self.camera.frame.animate.set(width=FRAME_W).move_to(ORIGIN))
        self.pause()

        # Part B's questions, keyed in one at a time under its title
        questions = [Tex('- Which point on the PPF?'),
                     Tex('- Coordinate large groups?'),
                     Tex('- Who benefits?')]
        for i, q in enumerate(questions):
            q.set_color(INK).align_to(part_b, LEFT).align_to(part_a, UP).shift(DOWN * (2.7 + 1.05 * i))

        # B03b ---------------------------------------------------------
        # first question: two options on the frontier, which do we like?

        x1 = 30
        p1 = ppf_ax.coords_to_point(x1, Bowed_PPF(x1))
        dot1 = Dot(p1).set_color(INK)
        dot1_l = Tex('Option 1').next_to(dot1, RIGHT).set_color(DEFINITION)

        x2 = 80
        p2 = ppf_ax.coords_to_point(x2, Bowed_PPF(x2))
        dot2 = Dot(p2).set_color(INK)
        dot2_l = Tex('Option 2').next_to(dot2, UP + RIGHT).set_color(DEFINITION)

        self.play(FadeIn(dot1), FadeIn(dot1_l), key_in(questions[0]))
        self.play(FadeIn(dot2), FadeIn(dot2_l))
        self.pause()

        # B03c ---------------------------------------------------------
        # second question: coordination at scale

        self.play(key_in(questions[1]))
        self.pause()

        # B03d --------------------------------------------------------
        # ...and its other face: who benefits

        self.play(key_in(questions[2]))
        self.pause()

        # B05 ---------------------------------------------------------
        # Notes: ask Amanda-Grace at $4, then $2, then $1, then lower.

        FadeAll(self)
        head = title('What would she buy?')
        ax = style_axes(
            x_range=[0, 7, 1], y_range=[0, 4.5, 0.5],
            x_length=GRAPH_W, y_length=GRAPH_H, ticks=True,
            x_axis_config={'numbers_to_include': list(range(1, 7)),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [1, 2, 4],
                           'numbers_with_elongated_ticks': [1, 2, 4],
                           'decimal_number_config': {'num_decimal_places': 2, 'color': MUTED}},
        ).scale(GRAPH_SCALE)
        ax.shift(GRAPH_AT - (ax.c2p(0, 0) + ax.c2p(7, 4.5)) / 2)
        p_lab = Tex('P').set_color(INK).next_to(ax.c2p(0, 4.5), LEFT, buff=0.25)
        q_lab = Tex('Q').set_color(INK).next_to(ax.c2p(7, 0), DOWN, buff=0.35)

        # The price is a number that changes continuously, not a Tex transform.
        asking_price = ValueTracker(4)
        asking_line = DashedLine(ax.c2p(0, 4), ax.c2p(7, 4),
                                 color=GUIDE).set_opacity(0.45)
        asking_number = DecimalNumber(4, num_decimal_places=2).scale(0.7).set_color(GUIDE)
        asking_number.next_to(ax.c2p(0, asking_price.get_value()), LEFT, buff=0.65)
        asking_dollar = Tex(r'Price \$').scale(0.7).set_color(GUIDE)
        asking_dollar.next_to(asking_number, LEFT, buff=0.03)
        asking = VGroup(asking_line, asking_number, asking_dollar)

        self.play(FadeIn(head), FadeIn(ax), FadeIn(p_lab), FadeIn(q_lab))
        self.play(FadeIn(asking))
        asking_line.add_updater(lambda line: line.set_y(ax.c2p(0, asking_price.get_value())[1]))
        asking_number.add_updater(lambda number: number.set_value(asking_price.get_value())
                                 .next_to(ax.c2p(0, asking_price.get_value()), LEFT, buff=0.65))
        asking_dollar.add_updater(lambda dollar: dollar.next_to(asking_number, LEFT, buff=0.03))
        self.pause()

        # B05b --------------------------------------------------------
        # her answer at $4, and the term for it

        dots = [Dot(ax.c2p(q, p), color=DEMAND, z_index=15) for q, p in HER]
        iqd_def = Tex(r'\mbox{ {{Individual Quantity Demanded}} is the quantity a buyer is willing and able to buy at a given price.}')
        iqd_def.set_color_by_tex_to_color_map({'Individual Quantity Demanded': DEFINITION})
        iqd_def.set_width(min(iqd_def.get_width(), FRAME_W - 1.2))
        iqd_def.to_edge(LEFT, buff=0.6).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(dots[0]))
        self.play(FadeIn(iqd_def))
        self.pause()

        # B05c --------------------------------------------------------
        # lower the price and ask again

        self.play(asking_price.animate.set_value(2), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[1]))
        self.pause()

        # B05d --------------------------------------------------------

        self.play(asking_price.animate.set_value(1), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[2]))
        self.pause()

        # B05e --------------------------------------------------------
        # keep going through a range of prices, then park on her data

        self.play(asking_price.animate.set_value(0.5), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[3]))
        self.play(asking_price.animate.set_value(0.25), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[4]))
        asking.clear_updaters()
        self.remove(asking_price)
        self.play(FadeOut(asking))
        self.pause()

        # B06 ---------------------------------------------------------
        # connect them, top-down; the jagged curve gets its name

        segs = VGroup(*[Line(ax.c2p(*HER[i - 1]), ax.c2p(*HER[i]), color=INK)
                        for i in range(1, len(HER))])
        idc_def = definition('Individual Demand Curve', 'is the full collection of quantity demanded.')
        idc_def.set_width(min(idc_def.get_width(), FRAME_W - 1.2))
        idc_def.to_edge(LEFT, buff=0.6).to_edge(DOWN, buff=0.25)
        self.play(LaggedStart(*[FadeIn(s) for s in segs], lag_ratio=0.4))
        self.bring_to_front(*dots)
        self.remove(iqd_def)
        self.play(FadeIn(idc_def))
        self.pause()

        # B07 ---------------------------------------------------------
        # the pattern in the answers

        law_def = definition('Law of Demand', "is a good's quantity demanded falling with its price.")
        law_def.set_width(min(law_def.get_width(), FRAME_W - 1.2))
        law_def.to_edge(LEFT, buff=0.6).to_edge(DOWN, buff=0.25)
        self.remove(idc_def)
        self.play(FadeIn(law_def))
        self.pause()

        # B08 ---------------------------------------------------------
        # the linear approximation, drawn from the intercept down; the data
        # fades the jagged observations into the background.

        demand = ax.plot(lambda q: 2.5 - q / 2, x_range=[0, 5], color=DEMAND)
        eqn = Tex('$P = 2.5 - Q/2$').scale(0.9).set_color(INK).move_to(ax.c2p(4.3, 2.0))
        d_lab = Tex('D').set_color(INK).next_to(ax.c2p(5, 0), UR, buff=0.15)
        self.play(FadeIn(demand),
                  segs.animate.set_stroke(MUTED, opacity=0.3),
                  *[d.animate.set_color(MUTED).set_opacity(0.35) for d in dots])
        self.play(FadeIn(eqn), FadeIn(d_lab))
        self.play(Indicate(dots[0], color=FOCUS, scale_factor=1.6))
        self.pause()

        # B08b --------------------------------------------------------
        # the data goes, the stage re-ranges, and the standing staircase
        # ghosts in under the line

        ax2 = style_axes(
            x_range=[0, 6, 1], y_range=[0, 2.5, 0.5],
            x_length=GRAPH_W, y_length=GRAPH_H, ticks=True,
            x_axis_config={'numbers_to_include': list(range(1, 6)),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [0.5, 1, 1.5, 2],
                           'numbers_with_elongated_ticks': [0.5, 1, 1.5, 2],
                           'decimal_number_config': {'num_decimal_places': 2, 'color': MUTED}},
        ).scale(GRAPH_SCALE)
        ax2.shift(GRAPH_AT - (ax2.c2p(0, 0) + ax2.c2p(6, 2.5)) / 2)
        demand2 = ax2.plot(lambda q: 2.5 - q / 2, x_range=[0, 5], color=DEMAND)
        eqn2 = Tex('$P = 2.5 - Q/2$').scale(0.9).set_color(INK).move_to(ax2.c2p(4.3, 2.0))
        p_lab2 = Tex('P').set_color(INK).next_to(ax2.c2p(0, 2.5), LEFT, buff=0.25)
        q_lab2 = Tex('Q').set_color(INK).next_to(ax2.c2p(6, 0), DOWN, buff=0.35)
        d_lab2 = Tex('D').set_color(INK).next_to(ax2.c2p(5, 0), UR, buff=0.15)

        # Every potential unit remains visible; each top-right corner is on D.
        rest_bars = VGroup()
        for quantity in range(1, 5):
            marginal_benefit = 2.5 - quantity / 2
            bar = Polygon(ax2.c2p(quantity - 1, 0), ax2.c2p(quantity, 0),
                          ax2.c2p(quantity, marginal_benefit),
                          ax2.c2p(quantity - 1, marginal_benefit))
            bar.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            rest_bars.add(bar)

        self.play(FadeOut(segs), *[FadeOut(d) for d in dots], FadeOut(law_def))
        self.play(ReplacementTransform(ax, ax2), ReplacementTransform(demand, demand2),
                  ReplacementTransform(eqn, eqn2), ReplacementTransform(p_lab, p_lab2),
                  ReplacementTransform(q_lab, q_lab2), ReplacementTransform(d_lab, d_lab2))
        self.play(FadeIn(rest_bars))
        self.pause()

        # B09 ---------------------------------------------------------
        # Pick a price, trace the graph, solve, then carry the answer back.

        read_price = ValueTracker(1.5)
        read_price_number = DecimalNumber(1.5, num_decimal_places=2).scale(0.7).set_color(GUIDE)
        read_price_number.next_to(ax2.c2p(0, 1.5), LEFT, buff=0.65)
        read_price_word = Tex(r'Price \$').scale(0.7).set_color(GUIDE)
        read_price_word.next_to(read_price_number, LEFT, buff=0.07)
        read_source = VGroup(read_price_number, read_price_word)
        self.play(FadeIn(read_source))
        read_price_number.add_updater(lambda number: number.set_value(read_price.get_value())
                                     .next_to(ax2.c2p(0, read_price.get_value()), LEFT, buff=0.65))
        read_price_word.add_updater(lambda word: word.next_to(read_price_number, LEFT, buff=0.07))

        read_a_first = DashedLine(ax2.c2p(0, 1.5), ax2.c2p(2, 1.5), color=GUIDE, z_index=10).set_opacity(0.3)
        read_a_second = DashedLine(ax2.c2p(2, 1.5), ax2.c2p(2, 0), color=GUIDE, z_index=10).set_opacity(0.3)
        read_a_dot = Dot(ax2.c2p(2, 1.5), color=GUIDE, z_index=11)
        read_a_question = Tex('$Q_d = ?$').scale(0.7).set_color(GUIDE)
        read_a_question.next_to(ax2.c2p(2, 0), DOWN, buff=0.7)
        ax2.get_x_axis().numbers[1].set_opacity(0)
        self.play(FadeIn(read_a_first))
        self.play(FadeIn(read_a_second), FadeIn(read_a_dot), FadeIn(read_a_question))
        self.bring_to_front(read_a_dot)
        # Keep the same guides and dot attached while the price tracker moves.
        read_a_first.add_updater(lambda line: line.become(DashedLine(
            ax2.c2p(0, read_price.get_value()),
            ax2.c2p(5 - 2 * read_price.get_value(), read_price.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_a_second.add_updater(lambda line: line.become(DashedLine(
            ax2.c2p(5 - 2 * read_price.get_value(), read_price.get_value()),
            ax2.c2p(5 - 2 * read_price.get_value(), 0),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_a_dot.add_updater(lambda dot: dot.move_to(
            ax2.c2p(5 - 2 * read_price.get_value(), read_price.get_value())))
        self.pause()

        substitute_a = VGroup(Tex('$1.50$').set_color(GUIDE), Tex('$= 2.5 - Q_d/2$', tex_to_color_map={'Q_d': GUIDE}))
        rearrange_a = VGroup(Tex('$Q_d/2 = 2.5 -$', tex_to_color_map={'Q_d': GUIDE}), Tex('$1.50$').set_color(GUIDE))
        answer_a = VGroup(Tex('$Q_d =$'), Tex('$2$')).set_color(GUIDE)
        work = VGroup(substitute_a, rearrange_a, answer_a)
        for row in work:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        work.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(TransformFromCopy(read_price_number.copy().clear_updaters(), substitute_a[0]), FadeIn(substitute_a[1]))
        self.play(FadeIn(rearrange_a))
        self.play(FadeIn(answer_a))
        read_a_answer = VGroup(Tex('$Q_d =$'), Tex('$2$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_a_answer.move_to(read_a_question)
        self.play(FadeOut(read_a_question), FadeIn(read_a_answer[0]),
                  TransformFromCopy(answer_a[1], read_a_answer[1]),
                  ax2.get_x_axis().numbers[1].animate.set_opacity(1))
        self.pause()

        # B09b --------------------------------------------------------
        # The same price tracker rolls to a question with a fractional answer.

        self.play(FadeOut(read_a_answer), FadeOut(work))
        self.play(read_price.animate.set_value(1.75), run_time=1.5)
        read_b_question = Tex('$Q_d = ?$').scale(0.7).set_color(GUIDE)
        read_b_question.next_to(ax2.c2p(1.5, 0), DOWN, buff=0.7)
        self.play(FadeIn(read_b_question))
        self.bring_to_front(read_a_dot)
        self.pause()

        substitute_b = VGroup(Tex('$1.75$').set_color(GUIDE), Tex('$= 2.5 - Q_d/2$', tex_to_color_map={'Q_d': GUIDE}))
        rearrange_b = VGroup(Tex('$Q_d/2 = 2.5 -$', tex_to_color_map={'Q_d': GUIDE}), Tex('$1.75$').set_color(GUIDE))
        answer_b = VGroup(Tex('$Q_d =$'), Tex('$1.5$')).set_color(GUIDE)
        work_b = VGroup(substitute_b, rearrange_b, answer_b)
        for row in work_b:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        work_b.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(TransformFromCopy(read_price_number.copy().clear_updaters(), substitute_b[0]), FadeIn(substitute_b[1]))
        self.play(FadeIn(rearrange_b))
        self.play(FadeIn(answer_b))
        read_b_answer = VGroup(Tex('$Q_d =$'), Tex('$1.5$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_b_answer.move_to(read_b_question)
        self.play(FadeOut(read_b_question), FadeIn(read_b_answer[0]),
                  TransformFromCopy(answer_b[1], read_b_answer[1]))
        read_b = VGroup(read_a_first, read_a_second, read_a_dot, read_b_answer)
        self.pause()

        # B10 ---------------------------------------------------------
        # Define marginal benefit BEFORE asking the inverse question.

        read_source.clear_updaters()
        read_b.clear_updaters()
        self.remove(read_price)
        self.remove(head)
        head = title('Which bars are worth buying?')
        self.play(FadeIn(head),
                  FadeOut(read_source), FadeOut(read_b), FadeOut(work_b))
        mb_def = definition('Marginal Benefit', 'is the value of one more unit.')
        mb_def.set_width(min(mb_def.get_width(), FRAME_W - 1.2))
        mb_def.to_edge(LEFT, buff=0.6).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(mb_def))
        self.pause()

        # B10b --------------------------------------------------------
        # Quantity is now the red input; marginal benefit is the unknown.

        read_quantity = ValueTracker(1)
        read_c_source = VGroup(Tex('$Q_d =$'), DecimalNumber(1, num_decimal_places=0))
        read_c_source.arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_c_source.next_to(ax2.c2p(1, 0), DOWN, buff=0.7)
        read_c_first = DashedLine(ax2.c2p(1, 0), ax2.c2p(1, 2), color=GUIDE, z_index=10).set_opacity(0.3)
        read_c_second = DashedLine(ax2.c2p(1, 2), ax2.c2p(0, 2), color=GUIDE, z_index=10).set_opacity(0.3)
        read_c_dot = Dot(ax2.c2p(1, 2), color=GUIDE, z_index=11)
        read_c_question = Tex('$MB = ?$').scale(0.7).set_color(GUIDE)
        read_c_question.next_to(ax2.c2p(0, 2), LEFT, buff=0.65)
        ax2.get_y_axis().numbers[3].set_opacity(0)
        self.play(FadeIn(read_c_source))
        self.play(FadeIn(read_c_first))
        self.play(FadeIn(read_c_second), FadeIn(read_c_dot), FadeIn(read_c_question))
        self.bring_to_front(read_c_dot)
        read_c_source[1].add_updater(lambda number: number.set_value(read_quantity.get_value()))
        read_c_source.add_updater(lambda group: group.arrange(RIGHT, buff=0.12)
                                 .next_to(ax2.c2p(read_quantity.get_value(), 0), DOWN, buff=0.7))
        read_c_first.add_updater(lambda line: line.become(DashedLine(
            ax2.c2p(read_quantity.get_value(), 0),
            ax2.c2p(read_quantity.get_value(), 2.5 - read_quantity.get_value() / 2),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_c_second.add_updater(lambda line: line.become(DashedLine(
            ax2.c2p(read_quantity.get_value(), 2.5 - read_quantity.get_value() / 2),
            ax2.c2p(0, 2.5 - read_quantity.get_value() / 2),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_c_dot.add_updater(lambda dot: dot.move_to(
            ax2.c2p(read_quantity.get_value(), 2.5 - read_quantity.get_value() / 2)))
        self.pause()

        substitute_c = VGroup(Tex('$P = 2.5 -$', tex_to_color_map={'P': GUIDE}), Tex('$1$').set_color(GUIDE), Tex('$/2$'))
        answer_c = VGroup(Tex('$P =$'), Tex(r'\$2.00')).set_color(GUIDE)
        work_c = VGroup(substitute_c, answer_c)
        for row in work_c:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        work_c.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(substitute_c[0]), FadeIn(substitute_c[2]),
                  TransformFromCopy(read_c_source[1].copy().clear_updaters(), substitute_c[1]))
        self.play(FadeIn(answer_c))
        read_c_answer = VGroup(Tex('$MB =$'), Tex(r'\$2.00')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_c_answer.next_to(ax2.c2p(0, 2), LEFT, buff=0.65)
        self.play(FadeOut(read_c_question), FadeIn(read_c_answer[0]),
                  TransformFromCopy(answer_c[1], read_c_answer[1]),
                  ax2.get_y_axis().numbers[3].animate.set_opacity(1))
        self.pause()

        # B10c --------------------------------------------------------
        # Move to the second bar with the same quantity tracker and guides.

        self.play(FadeOut(read_c_answer), FadeOut(work_c))
        ax2.get_y_axis().numbers[2].set_opacity(0)
        self.play(read_quantity.animate.set_value(2), run_time=1.5)
        read_c_question = Tex('$MB = ?$').scale(0.7).set_color(GUIDE)
        read_c_question.next_to(ax2.c2p(0, 1.5), LEFT, buff=0.65)
        self.play(FadeIn(read_c_question))
        self.pause()

        substitute_c = VGroup(Tex('$P = 2.5 -$', tex_to_color_map={'P': GUIDE}), Tex('$2$').set_color(GUIDE), Tex('$/2$'))
        answer_c = VGroup(Tex('$P =$'), Tex(r'\$1.50')).set_color(GUIDE)
        work_c = VGroup(substitute_c, answer_c)
        for row in work_c:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        work_c.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(substitute_c[0]), FadeIn(substitute_c[2]),
                  TransformFromCopy(read_c_source[1].copy().clear_updaters(), substitute_c[1]))
        self.play(FadeIn(answer_c))
        read_c_answer = VGroup(Tex('$MB =$'), Tex(r'\$1.50')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_c_answer.next_to(ax2.c2p(0, 1.5), LEFT, buff=0.65)
        self.play(FadeOut(read_c_question), FadeIn(read_c_answer[0]),
                  TransformFromCopy(answer_c[1], read_c_answer[1]),
                  ax2.get_y_axis().numbers[2].animate.set_opacity(1))
        read_c = VGroup(read_c_source, read_c_first, read_c_second, read_c_dot, read_c_answer)
        read_c.clear_updaters()
        self.remove(read_quantity)
        self.pause()

        # B11 ---------------------------------------------------------

        stage1, card1 = exercise_card(
            self, 'Exercise B1 $|$ Quantity Demanded',
            ['Pumpkin pasties sell along the demand curve $P=12-Q/2$, in galleons and '
             'thousands of pasties. (a) What is the quantity demanded at 10 galleons? '
             '(b) What is the marginal benefit at a quantity of 4 thousand?'])
        self.pause()

        # B12 ---------------------------------------------------------
        # Keep bar 1 on screen while its surroundings fade away.

        self.play(Restore(stage1), FadeOut(card1))
        self.play(FadeOut(mb_def), FadeOut(read_c), FadeOut(work_c),
                  FadeOut(VGroup(*rest_bars[1:])),
                  FadeOut(demand2), FadeOut(eqn2), FadeOut(d_lab2))

        price = ValueTracker(1)
        selected_unit = ValueTracker(1)  # set between examples, never animated
        expenditure_reveal = ValueTracker(0)
        cs_reveal = ValueTracker(0)

        grey_bar = rest_bars[0].copy()
        expenditure_box = grey_bar.copy()
        surplus_box = grey_bar.copy()
        expenditure_label = Tex('Expenditure').scale(0.7).set_color(GOV)
        surplus_label = Tex('Consumer Surplus').scale(0.7).set_color(DEMAND)
        expenditure_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(INK)
        surplus_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(INK)
        price_line = Line(ax2.c2p(0, 1), ax2.c2p(5.4, 1), color=GUIDE, stroke_width=2)
        price_word = Tex(r'Price \$').scale(0.7).set_color(GUIDE)
        price_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(GUIDE)
        price_label = VGroup(price_word, price_number)
        cs_group = VGroup(surplus_box, surplus_number, surplus_label)
        expenditure_group = VGroup(expenditure_box, expenditure_number, expenditure_label)
        exchange = VGroup(grey_bar, expenditure_group, cs_group, price_line, price_label)

        # The single updater keeps the boxes, price, and labels together.
        def update_exchange(group):
            q = int(selected_unit.get_value())
            mb = 2.5 - q / 2
            p = price.get_value()
            buys = p <= mb
            paid = min(p, mb)
            surplus = max(mb - p, 0)
            spent_reveal = expenditure_reveal.get_value() if buys else 0
            reveal = cs_reveal.get_value() if buys and surplus > 0 else 0

            grey_bar.set_points_as_corners([
                ax2.c2p(q - 1, 0), ax2.c2p(q, 0), ax2.c2p(q, mb),
                ax2.c2p(q - 1, mb), ax2.c2p(q - 1, 0)])
            grey_bar.set_stroke(MUTED, 2).set_fill(MUTED, 0.10 if buys else 0.45)

            expenditure_box.set_points_as_corners([
                ax2.c2p(q - 1, 0), ax2.c2p(q, 0), ax2.c2p(q, paid),
                ax2.c2p(q - 1, paid), ax2.c2p(q - 1, 0)])
            expenditure_box.set_stroke(GOV, 2, opacity=spent_reveal)
            expenditure_box.set_fill(GOV, AREA_OPACITY * spent_reveal)
            expenditure_number.set_value(p).move_to(ax2.c2p(q - 0.5, paid / 2))
            expenditure_number.set_opacity(spent_reveal if paid >= 0.18 else 0)
            expenditure_label.next_to(ax2.c2p(q, paid / 2), RIGHT, buff=0.3)
            expenditure_label.set_opacity(spent_reveal)

            surplus_box.set_points_as_corners([
                ax2.c2p(q - 1, paid), ax2.c2p(q, paid), ax2.c2p(q, mb),
                ax2.c2p(q - 1, mb), ax2.c2p(q - 1, paid)])
            surplus_box.set_stroke(DEMAND, 2, opacity=reveal)
            surplus_box.set_fill(DEMAND, AREA_OPACITY * reveal)
            surplus_number.set_value(surplus).move_to(ax2.c2p(q - 0.5, (paid + mb) / 2))
            surplus_number.set_opacity(reveal if surplus >= 0.18 else 0)
            surplus_label.next_to(ax2.c2p(q, (paid + mb) / 2), RIGHT, buff=0.3)
            surplus_label.set_opacity(reveal)

            price_line.put_start_and_end_on(ax2.c2p(0, p), ax2.c2p(5.4, p))
            price_line.set_opacity(0.6)
            price_number.set_value(p)
            price_label.arrange(RIGHT, buff=0.07)
            price_label.next_to(ax2.c2p(0, p), LEFT, buff=0.65)

        update_exchange(exchange)
        self.remove(rest_bars[0])
        self.add(grey_bar)  # identical geometry; the first bar never fades out
        self.play(FadeIn(price_line), FadeIn(price_label))
        self.remove(grey_bar, price_line, price_label)
        self.add(exchange)
        exchange.add_updater(update_exchange)
        self.pause()

        # B12a --------------------------------------------------------
        # Expenditure gets its own reveal and pause.

        self.remove(head)
        head = title('What does she gain?')
        self.play(FadeIn(head))
        self.play(expenditure_reveal.animate.set_value(1))
        self.pause()

        # B12b --------------------------------------------------------

        cs_def = definition('Consumer Surplus', "is the buyer's extra value from an exchange.")
        cs_def.set_width(min(cs_def.get_width(), FRAME_W - 1.2))
        cs_def.to_edge(LEFT, buff=0.6).to_edge(DOWN, buff=0.25)
        self.play(cs_reveal.animate.set_value(1), FadeIn(cs_def))
        self.pause()

        # B12c --------------------------------------------------------

        self.play(price.animate.set_value(2.4), run_time=2)
        self.pause()
        self.play(price.animate.set_value(0.5), run_time=2.5)
        self.pause()
        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12d --------------------------------------------------------
        # Restore the curve with the grey bars before choosing another unit.

        exchange.clear_updaters()
        self.remove(price, expenditure_reveal, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars),
                  FadeIn(demand2), FadeIn(eqn2), FadeIn(d_lab2))
        self.pause()

        # B12e --------------------------------------------------------
        # Keep bar 2, then reveal its expenditure and surplus in turn.

        self.play(FadeOut(VGroup(rest_bars[0], rest_bars[2], rest_bars[3])),
                  FadeOut(demand2), FadeOut(eqn2), FadeOut(d_lab2))
        selected_unit.set_value(2)
        expenditure_reveal.set_value(0)
        cs_reveal.set_value(0)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.remove(rest_bars)
        self.add(grey_bar)
        self.play(FadeIn(price_line), FadeIn(price_label))
        self.remove(grey_bar, price_line, price_label)
        self.add(exchange)
        exchange.add_updater(update_exchange)
        self.pause()
        self.play(expenditure_reveal.animate.set_value(1))
        self.pause()

        # B12f --------------------------------------------------------

        self.play(cs_reveal.animate.set_value(1))
        self.pause()

        # B12g --------------------------------------------------------

        self.play(price.animate.set_value(1.9), run_time=2)
        self.pause()
        self.play(price.animate.set_value(0.5), run_time=2.5)
        self.pause()
        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12h --------------------------------------------------------

        exchange.clear_updaters()
        self.remove(price, expenditure_reveal, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars),
                  FadeIn(demand2), FadeIn(eqn2), FadeIn(d_lab2))
        self.pause()
        self.play(FadeOut(VGroup(rest_bars[0], rest_bars[1], rest_bars[3])),
                  FadeOut(demand2), FadeOut(eqn2), FadeOut(d_lab2))
        selected_unit.set_value(3)
        expenditure_reveal.set_value(0)
        cs_reveal.set_value(0)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.remove(rest_bars)
        self.add(grey_bar)
        self.play(FadeIn(price_line), FadeIn(price_label))
        self.remove(grey_bar, price_line, price_label)
        self.add(exchange)
        exchange.add_updater(update_exchange)
        self.pause()
        self.play(expenditure_reveal.animate.set_value(1))
        self.pause()

        # B12i --------------------------------------------------------
        # At $1 this marginal unit has zero CS. A lower price creates CS.

        self.play(cs_reveal.animate.set_value(1), price.animate.set_value(0.5), run_time=2)
        self.pause()
        self.play(price.animate.set_value(1.4), run_time=2)
        self.pause()
        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12j --------------------------------------------------------
        # Bar 4 is initially unbought. Both areas respond as price falls.

        exchange.clear_updaters()
        self.remove(price, expenditure_reveal, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars),
                  FadeIn(demand2), FadeIn(eqn2), FadeIn(d_lab2))
        self.pause()
        self.play(FadeOut(VGroup(rest_bars[0], rest_bars[1], rest_bars[2])),
                  FadeOut(demand2), FadeOut(eqn2), FadeOut(d_lab2))
        selected_unit.set_value(4)
        expenditure_reveal.set_value(1)
        cs_reveal.set_value(1)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.remove(rest_bars)
        self.add(grey_bar)
        self.play(FadeIn(price_line), FadeIn(price_label))
        self.remove(grey_bar, price_line, price_label)
        self.add(exchange)
        exchange.add_updater(update_exchange)
        self.pause()

        # B12k --------------------------------------------------------

        self.play(price.animate.set_value(0.25), run_time=2)
        self.pause()
        self.play(price.animate.set_value(0.9), run_time=2)
        self.pause()
        self.play(price.animate.set_value(0.25), run_time=2)
        self.pause()
        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12l --------------------------------------------------------
        # Return to the whole demand curve at the lecture's $1 offer.

        exchange.clear_updaters()
        self.remove(price, expenditure_reveal, cs_reveal, selected_unit)
        self.play(FadeOut(exchange), FadeIn(rest_bars),
                  FadeIn(demand2), FadeIn(eqn2), FadeIn(d_lab2))
        price13 = VGroup(
            Line(ax2.c2p(0, 1), ax2.c2p(5.4, 1), color=GUIDE, stroke_width=2).set_opacity(0.8),
            Tex(r'Price $= \$1$').scale(0.7).set_color(GUIDE)
                .next_to(ax2.c2p(0, 1), LEFT, buff=0.65)).set_z_index(10)
        self.play(FadeIn(price13))
        all_expenditure = VGroup()
        all_cs = VGroup()
        for quantity in range(1, 4):
            mb = 2.5 - quantity / 2
            spent = Polygon(ax2.c2p(quantity - 1, 0), ax2.c2p(quantity, 0),
                            ax2.c2p(quantity, 1), ax2.c2p(quantity - 1, 1),
                            color=GOV, fill_opacity=AREA_OPACITY)
            all_expenditure.add(spent)
            self.play(FadeIn(spent), run_time=0.4)
            if mb > 1:
                gained = Polygon(ax2.c2p(quantity - 1, 1), ax2.c2p(quantity, 1),
                                 ax2.c2p(quantity, mb), ax2.c2p(quantity - 1, mb),
                                 color=DEMAND, fill_opacity=AREA_OPACITY)
                all_cs.add(gained)
                self.play(FadeIn(gained), run_time=0.4)
        self.play(rest_bars[3].animate.set_fill(MUTED, 0.45).set_stroke(MUTED, 2))
        tally = VGroup(
            Tex(r'CS $= 1.00 + 0.50 + 0.00 = \$1.50$', tex_to_color_map={'CS': DEMAND}),
            Tex(r'Expenditure $= 3 \times \$1 = \$3$', tex_to_color_map={'Expenditure': GOV}))
        tally.scale(0.7).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        tally.move_to(MATH_AT, aligned_edge=LEFT)
        qd_drop = DashedLine(ax2.c2p(3, 1), ax2.c2p(3, 0), color=GUIDE, z_index=10).set_opacity(0.8)
        qd_mark = Tex('$Q_d = 3$').scale(0.7).set_color(GUIDE)
        qd_mark.next_to(ax2.c2p(3, 0), DOWN, buff=0.65)
        self.play(FadeIn(tally), FadeIn(qd_drop), FadeIn(qd_mark))
        self.bring_to_front(price13, qd_drop)
        self.pause()

        # B13 ---------------------------------------------------------
        # Split every bar in half, then raise each new corner onto demand.

        self.play(FadeOut(tally), FadeOut(cs_def),
                  rest_bars[3].animate.set_fill(MUTED, REST_OPACITY).set_stroke(MUTED, 1))
        old_width = 1
        for width in [0.5, 0.25, 0.125, 0.0625]:
            finer_grey = VGroup()
            finer_spent = VGroup()
            finer_cs = VGroup()
            refinement = []
            for right in np.arange(width, 5, width):
                left = right - width
                old_right = np.ceil(right / old_width) * old_width
                old_top = 2.5 - old_right / 2
                new_top = 2.5 - right / 2
                bar = Polygon(ax2.c2p(left, 0), ax2.c2p(right, 0),
                              ax2.c2p(right, old_top), ax2.c2p(left, old_top))
                bar.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
                finer_grey.add(bar)
                refinement.append(bar.animate.set_points_as_corners([
                    ax2.c2p(left, 0), ax2.c2p(right, 0), ax2.c2p(right, new_top),
                    ax2.c2p(left, new_top), ax2.c2p(left, 0)]))
                if right <= 3:
                    spent = Polygon(ax2.c2p(left, 0), ax2.c2p(right, 0),
                                    ax2.c2p(right, 1), ax2.c2p(left, 1),
                                    color=GOV, stroke_width=1, fill_opacity=AREA_OPACITY)
                    finer_spent.add(spent)
                if right < 3:
                    gained = Polygon(ax2.c2p(left, 1), ax2.c2p(right, 1),
                                     ax2.c2p(right, old_top), ax2.c2p(left, old_top),
                                     color=DEMAND, stroke_width=1, fill_opacity=AREA_OPACITY)
                    finer_cs.add(gained)
                    refinement.append(gained.animate.set_points_as_corners([
                        ax2.c2p(left, 1), ax2.c2p(right, 1), ax2.c2p(right, new_top),
                        ax2.c2p(left, new_top), ax2.c2p(left, 1)]))
            # The children initially cover their parents exactly; only their
            # new top corners move. The expenditure below price stays put.
            self.remove(rest_bars, all_expenditure, all_cs)
            self.add(finer_grey, finer_spent, finer_cs)
            self.bring_to_front(demand2, price13, qd_drop)
            self.play(*refinement, run_time=1.5)
            rest_bars = finer_grey
            all_expenditure = finer_spent
            all_cs = finer_cs
            old_width = width
            self.pause()

        tri = Polygon(ax2.c2p(0, 1), ax2.c2p(3, 1), ax2.c2p(0, 2.5),
                      color=DEMAND, fill_opacity=AREA_OPACITY)
        spend_area = Polygon(ax2.c2p(0, 0), ax2.c2p(3, 0),
                             ax2.c2p(3, 1), ax2.c2p(0, 1),
                             color=GOV, fill_opacity=AREA_OPACITY)
        self.play(FadeOut(rest_bars), FadeOut(all_cs), FadeOut(all_expenditure),
                  FadeIn(tri), FadeIn(spend_area))
        self.bring_to_front(demand2, price13, qd_drop)
        self.pause()

        # B13b --------------------------------------------------------
        # Keep this formula on screen while h and b are measured and filled in.

        area = VGroup(Tex(r'Area $= \frac{1}{2}$', tex_to_color_map={'Area': DEMAND}), Tex('$h$'), Tex('$b$'))
        area.arrange(RIGHT, buff=0.15).scale(0.8)
        area.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(area[0]), FadeIn(area[1]), FadeIn(area[2]))
        self.pause()

        # B13c --------------------------------------------------------

        h_bar = Line(ax2.c2p(0, 1), ax2.c2p(0, 2.5), color=FOCUS, stroke_width=4, z_index=20)
        h_lab = VGroup(Tex('$h =$'), Tex(r'\$1.50'))
        h_lab.arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        h_lab.next_to(ax2.c2p(0, 1.75), LEFT, buff=0.55)
        self.play(FadeIn(h_bar), FadeIn(h_lab))
        self.pause()

        # B13d --------------------------------------------------------

        b_bar = Line(ax2.c2p(0, 0), ax2.c2p(3, 0), color=FOCUS, stroke_width=4, z_index=20)
        b_lab = VGroup(Tex('$b =$'), Tex('$3$'))
        b_lab.arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        b_lab.next_to(ax2.c2p(1.5, 0), UP, buff=0.15)
        self.play(FadeIn(b_bar), FadeIn(b_lab))
        self.pause()

        # B13e --------------------------------------------------------
        # Only the two symbols change; the formula's prefix stays in place.

        h_value = Tex('$(1.50)$').scale(0.8).set_color(FOCUS).next_to(area[0], RIGHT, buff=0.15)
        b_value = Tex('$(3)$').scale(0.8).set_color(FOCUS).next_to(h_value, RIGHT, buff=0.15)
        self.play(FadeOut(area[1]), area[2].animate.move_to(b_value),
                  TransformFromCopy(h_lab[1], h_value))
        self.play(FadeOut(area[2]), TransformFromCopy(b_lab[1], b_value))
        area_answer = Tex(r'$= \$2.25$').scale(0.8).set_color(INK)
        area_answer.next_to(area[0], DOWN, buff=0.35).align_to(area[0], LEFT)
        self.play(FadeIn(area_answer))
        solve = VGroup(area[0], h_value, b_value, area_answer)
        self.pause()

        # B14 ---------------------------------------------------------

        stage2, card2 = exercise_card(
            self, 'Exercise B1 $|$ Consumer Surplus',
            ['Pumpkin pasties again, $P=12-Q/2$. (a) What is the quantity demanded at '
             '5 galleons? (b) Find and label the consumer surplus at that price.'])
        self.pause()

        # B15 ---------------------------------------------------------
        # Introduce market demand before the class's market exercise.

        FadeAll(self)
        head = title('What happens when we consider everyone?')
        sum_def = definition('Market Demand',
                             "is the sum of everyone's individual quantity demanded.")
        sum_def.set_width(min(sum_def.get_width(), FRAME_W - 1.2))
        sum_def.to_edge(LEFT, buff=0.6)
        self.play(FadeIn(head), FadeIn(sum_def))
        self.pause()

        # B16 ---------------------------------------------------------
        # The live room tally; the future 3D sequence follows this exercise.

        stage3, card3 = exercise_card(
            self, 'Market Demand $|$ Simulation',
            ['Tally the room at a range of prices, building the market curve on the board.'])
        self.pause()

        # B17 ---------------------------------------------------------
        # the market curve, drawn from the top, over its own standing bars

        FadeAll(self)
        head = title('What happens when we consider everyone?')
        ax_m = style_axes(
            x_range=[0, 62, 10], y_range=[0, 13, 2],
            x_length=GRAPH_W, y_length=GRAPH_H, ticks=True,
            x_axis_config={'numbers_to_include': [10, 20, 30, 40, 50, 60],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [2, 4, 6, 8, 10, 12],
                           'numbers_with_elongated_ticks': [2, 4, 6, 8, 10, 12],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        ).scale(GRAPH_SCALE)
        ax_m.shift(GRAPH_AT - (ax_m.c2p(0, 0) + ax_m.c2p(62, 13)) / 2)
        m_q = Tex('Q').set_color(INK).next_to(ax_m.c2p(62, 0), DOWN, buff=0.35)
        m_p = Tex('P').set_color(INK).next_to(ax_m.c2p(0, 13), LEFT, buff=0.25)
        demand_m = ax_m.plot(lambda q: 12 - q / 5, x_range=[0, 60], color=DEMAND)
        eqn_m = Tex('$P = 12 - Q/5$').scale(0.9).set_color(INK).move_to(ax_m.c2p(40, 9))
        d_lab_m = Tex('D').set_color(INK).next_to(ax_m.c2p(60, 0), UR, buff=0.15)

        # Each thin rectangle stands for a small quantity interval (thousands
        # of chocolate bars), not a particular buyer.
        market_g = VGroup()
        market_cs = VGroup()
        for right in np.arange(2.5, 60.1, 2.5):
            left = right - 2.5
            top = 12 - right / 5
            bar = Polygon(ax_m.c2p(left, 0), ax_m.c2p(right, 0),
                          ax_m.c2p(right, top), ax_m.c2p(left, top))
            bar.set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY)
            market_g.add(bar)
            if right < 35:
                cs_bar = Polygon(ax_m.c2p(left, 5), ax_m.c2p(right, 5),
                                 ax_m.c2p(right, top), ax_m.c2p(left, top),
                                 color=DEMAND, fill_opacity=AREA_OPACITY)
                market_cs.add(cs_bar)

        self.play(FadeIn(head), FadeIn(ax_m), FadeIn(m_p), FadeIn(m_q),
                  FadeIn(demand_m))
        self.add(market_g)
        self.play(FadeIn(eqn_m), FadeIn(d_lab_m))
        self.pause()

        # B17b --------------------------------------------------------
        # Same price-to-graph-to-math sequence, now for market chocolate demand.

        market_price = ValueTracker(5)
        market_price_number = DecimalNumber(5, num_decimal_places=2).scale(0.7).set_color(GUIDE)
        market_price_number.next_to(ax_m.c2p(0, 5), LEFT, buff=0.65)
        market_price_word = Tex(r'Price \$').scale(0.7).set_color(GUIDE)
        market_price_word.next_to(market_price_number, LEFT, buff=0.07)
        market_source = VGroup(market_price_number, market_price_word)
        self.play(FadeIn(market_source))
        market_price_number.add_updater(lambda number: number.set_value(market_price.get_value())
                                       .next_to(ax_m.c2p(0, market_price.get_value()), LEFT, buff=0.65))
        market_price_word.add_updater(lambda word: word.next_to(market_price_number, LEFT, buff=0.07))

        read_m_first = DashedLine(ax_m.c2p(0, 5), ax_m.c2p(35, 5), color=GUIDE, z_index=10).set_opacity(0.3)
        read_m_second = DashedLine(ax_m.c2p(35, 5), ax_m.c2p(35, 0), color=GUIDE, z_index=10).set_opacity(0.3)
        read_m_dot = Dot(ax_m.c2p(35, 5), color=GUIDE, z_index=11)
        read_m_question = Tex('$Q_d = ?$').scale(0.7).set_color(GUIDE)
        read_m_question.next_to(ax_m.c2p(35, 0), DOWN, buff=0.85)
        self.play(FadeIn(read_m_first))
        self.play(FadeIn(read_m_second), FadeIn(read_m_dot), FadeIn(read_m_question))
        self.bring_to_front(read_m_dot)
        read_m_first.add_updater(lambda line: line.become(DashedLine(
            ax_m.c2p(0, market_price.get_value()),
            ax_m.c2p(60 - 5 * market_price.get_value(), market_price.get_value()),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_m_second.add_updater(lambda line: line.become(DashedLine(
            ax_m.c2p(60 - 5 * market_price.get_value(), market_price.get_value()),
            ax_m.c2p(60 - 5 * market_price.get_value(), 0),
            color=GUIDE, z_index=10).set_opacity(0.3)))
        read_m_dot.add_updater(lambda dot: dot.move_to(
            ax_m.c2p(60 - 5 * market_price.get_value(), market_price.get_value())))
        self.pause()

        substitute_m = VGroup(Tex('$5$').set_color(GUIDE), Tex('$= 12 - Q_d/5$', tex_to_color_map={'Q_d': GUIDE}))
        rearrange_m = VGroup(Tex('$Q_d/5 = 12 -$', tex_to_color_map={'Q_d': GUIDE}), Tex('$5$').set_color(GUIDE))
        answer_m = VGroup(Tex('$Q_d =$'), Tex('$35$')).set_color(GUIDE)
        mwork = VGroup(substitute_m, rearrange_m, answer_m)
        for row in mwork:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        mwork.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(TransformFromCopy(market_price_number.copy().clear_updaters(), substitute_m[0]), FadeIn(substitute_m[1]))
        self.play(FadeIn(rearrange_m))
        self.play(FadeIn(answer_m))
        read_m_answer = VGroup(Tex('$Q_d =$'), Tex('$35$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_m_answer.move_to(read_m_question)
        self.play(FadeOut(read_m_question), FadeIn(read_m_answer[0]),
                  TransformFromCopy(answer_m[1], read_m_answer[1]))
        self.pause()

        # B17c --------------------------------------------------------

        self.play(FadeOut(read_m_answer), FadeOut(mwork))
        self.play(market_price.animate.set_value(2), run_time=1.5)
        read_m2_question = Tex('$Q_d = ?$').scale(0.7).set_color(GUIDE)
        read_m2_question.next_to(ax_m.c2p(50, 0), DOWN, buff=0.85)
        ax_m.get_x_axis().numbers[4].set_opacity(0)
        self.play(FadeIn(read_m2_question))
        self.bring_to_front(read_m_dot)
        self.pause()

        substitute_m2 = VGroup(Tex('$2$').set_color(GUIDE), Tex('$= 12 - Q_d/5$', tex_to_color_map={'Q_d': GUIDE}))
        rearrange_m2 = VGroup(Tex('$Q_d/5 = 12 -$', tex_to_color_map={'Q_d': GUIDE}), Tex('$2$').set_color(GUIDE))
        answer_m2 = VGroup(Tex('$Q_d =$'), Tex('$50$')).set_color(GUIDE)
        mwork_b = VGroup(substitute_m2, rearrange_m2, answer_m2)
        for row in mwork_b:
            row.arrange(RIGHT, buff=0.12).scale(0.8)
        mwork_b.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(TransformFromCopy(market_price_number.copy().clear_updaters(), substitute_m2[0]), FadeIn(substitute_m2[1]))
        self.play(FadeIn(rearrange_m2))
        self.play(FadeIn(answer_m2))
        read_m2_answer = VGroup(Tex('$Q_d =$'), Tex('$50$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_m2_answer.move_to(read_m2_question)
        self.play(FadeOut(read_m2_question), FadeIn(read_m2_answer[0]),
                  TransformFromCopy(answer_m2[1], read_m2_answer[1]),
                  ax_m.get_x_axis().numbers[4].animate.set_opacity(1))
        self.pause()

        # B18 ---------------------------------------------------------
        # Return to the already-solved $5 offer to measure expenditure.

        self.play(FadeOut(read_m2_answer), FadeOut(mwork_b))
        self.play(market_price.animate.set_value(5), run_time=1.5)
        read_m_first.clear_updaters().set_opacity(0.8)
        read_m_second.clear_updaters().set_opacity(0.8)
        read_m_dot.clear_updaters()
        read_m5_answer = VGroup(Tex('$Q_d =$'), Tex('$35$')).arrange(RIGHT, buff=0.12).scale(0.7).set_color(GUIDE)
        read_m5_answer.next_to(ax_m.c2p(35, 0), DOWN, buff=0.85)
        self.play(FadeIn(read_m5_answer))
        self.bring_to_front(read_m_dot)

        spend_rect = Polygon(ax_m.c2p(0, 0), ax_m.c2p(35, 0), ax_m.c2p(35, 5), ax_m.c2p(0, 5),
                             color=GOV, fill_opacity=AREA_OPACITY)
        spend_lab = Tex('Expenditure').scale(0.7).set_color(INK).move_to(ax_m.c2p(17.5, 2.5))
        spend_formula = Tex('Expenditure $= P \\times Q_d$',
                            tex_to_color_map={'Expenditure': GOV, 'P': GUIDE, 'Q_d': GUIDE}).scale(0.8)
        spend_values = VGroup(Tex('$=$'), Tex(r'\$5').set_color(GUIDE),
                             Tex('$\\times$'), Tex('$35{,}000$').set_color(GUIDE))
        spend_values.arrange(RIGHT, buff=0.12).scale(0.8)
        spend_result = Tex(r'$= \$175{,}000$').scale(0.8).set_color(INK)
        spend_math = VGroup(spend_formula, spend_values, spend_result)
        spend_math.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(spend_rect), FadeIn(spend_lab))
        self.bring_to_front(read_m_first, read_m_second, read_m_dot)
        self.play(FadeIn(spend_formula))
        self.play(FadeIn(spend_values[0]), FadeIn(spend_values[2]),
                  TransformFromCopy(market_price_number.copy().clear_updaters(), spend_values[1]),
                  TransformFromCopy(read_m5_answer[1], spend_values[3]))
        self.play(FadeIn(spend_result))
        self.pause()

        # B18b --------------------------------------------------------
        # Height and base stay yellow from the graph into the area formula.

        self.play(FadeOut(spend_math))
        market_area = VGroup(Tex(r'CS $= \frac{1}{2}$', tex_to_color_map={'CS': DEMAND}), Tex('$h$'), Tex('$b$'))
        market_area.arrange(RIGHT, buff=0.15).scale(0.8)
        market_area.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(market_area[0]), FadeIn(market_area[1]), FadeIn(market_area[2]))
        h_bar_m = Line(ax_m.c2p(0, 5), ax_m.c2p(0, 12), color=FOCUS, stroke_width=4, z_index=20)
        h_lab_m = VGroup(Tex('$h =$'), Tex(r'\$7'))
        h_lab_m.arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        h_lab_m.next_to(ax_m.c2p(0, 8.5), LEFT, buff=0.55)
        self.play(FadeIn(h_bar_m), FadeIn(h_lab_m))

        base_bar = Line(ax_m.c2p(0, 0), ax_m.c2p(0.01, 0), color=FOCUS, stroke_width=4, z_index=20)
        self.add(base_bar)
        for index, cs_bar in enumerate(market_cs):
            right = (index + 1) * 2.5
            # Add the bar below the guides before its fade begins.
            self.add(cs_bar)
            self.bring_to_front(read_m_first, read_m_second, read_m_dot, h_bar_m, base_bar)
            self.play(FadeIn(cs_bar),
                      base_bar.animate.put_start_and_end_on(ax_m.c2p(0, 0), ax_m.c2p(right, 0)),
                      run_time=0.2)
        self.play(base_bar.animate.put_start_and_end_on(ax_m.c2p(0, 0), ax_m.c2p(35, 0)))
        market_triangle = Polygon(ax_m.c2p(0, 5), ax_m.c2p(35, 5), ax_m.c2p(0, 12),
                                  color=DEMAND, fill_opacity=AREA_OPACITY)
        self.play(FadeOut(market_cs), FadeIn(market_triangle))
        self.bring_to_front(read_m_first, read_m_second, read_m_dot, h_bar_m, base_bar)
        b_lab_m = VGroup(Tex('$b =$'), Tex('$35{,}000$'))
        b_lab_m.arrange(RIGHT, buff=0.1).scale(0.7).set_color(FOCUS)
        b_lab_m.next_to(ax_m.c2p(17.5, 0), UP, buff=0.15)
        cs_lab_m = VGroup(Tex('Consumer'), Tex('Surplus'))
        cs_lab_m.arrange(DOWN, buff=0.08).scale(0.7).set_color(INK).move_to(ax_m.c2p(12, 7.3))
        self.play(FadeIn(b_lab_m), FadeIn(cs_lab_m))
        self.pause()

        market_h_value = Tex('$(7)$').scale(0.8).set_color(FOCUS).next_to(market_area[0], RIGHT, buff=0.15)
        market_b_value = Tex('$(35{,}000)$').scale(0.8).set_color(FOCUS).next_to(market_h_value, RIGHT, buff=0.15)
        self.play(FadeOut(market_area[1]), market_area[2].animate.move_to(market_b_value),
                  TransformFromCopy(h_lab_m[1], market_h_value))
        self.play(FadeOut(market_area[2]), TransformFromCopy(b_lab_m[1], market_b_value))
        market_area_answer = Tex(r'$= \$122{,}500$').scale(0.8).set_color(INK)
        market_area_answer.next_to(market_area[0], DOWN, buff=0.35).align_to(market_area[0], LEFT)
        self.play(FadeIn(market_area_answer))
        self.pause()
        market_source.clear_updaters()
        self.remove(market_price)

        # B20 ---------------------------------------------------------

        FadeAll(self)
        head = title('Next Time $|$ Sellers', scale=1.5)
        topic = Tex('What does it cost them to say yes to a trade?').scale(1.2).set_color(INK)
        self.play(FadeIn(head), FadeIn(topic))
        self.pause()
