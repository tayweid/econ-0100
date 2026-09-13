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

    def construct(self):

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
        x_label = Tex('B').set_color(INK).next_to(ppf_ax.c2p(100, 0), RIGHT, buff=0.3)

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
        head = title('Demand')
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
        q_lab = Tex('Q').set_color(INK).next_to(ax.c2p(7, 0), RIGHT, buff=0.25)

        # The price is a number that changes continuously, not a Tex transform.
        asking_price = ValueTracker(4)
        asking_line = DashedLine(ax.c2p(0, 4), ax.c2p(7, 4),
                                 color=GUIDE).set_opacity(0.45)
        asking_number = DecimalNumber(4, num_decimal_places=2).scale(0.7).set_color(INK)
        asking_number.next_to(asking_line.get_end(), RIGHT, buff=0.85)
        asking_dollar = Tex(r'\$').scale(0.7).set_color(INK)
        asking_dollar.next_to(asking_number, LEFT, buff=0.03)
        asking = VGroup(asking_line, asking_number, asking_dollar)

        self.play(FadeIn(head), FadeIn(ax), FadeIn(p_lab), FadeIn(q_lab))
        self.play(FadeIn(asking))
        asking_line.add_updater(lambda line: line.set_y(ax.c2p(0, asking_price.get_value())[1]))
        asking_number.add_updater(lambda number: number.set_value(asking_price.get_value())
                                 .next_to(asking_line.get_end(), RIGHT, buff=0.85))
        asking_dollar.add_updater(lambda dollar: dollar.next_to(asking_number, LEFT, buff=0.03))
        self.pause()

        # B05b --------------------------------------------------------
        # her answer at $4, and the term for it

        dots = [Dot(ax.c2p(q, p), color=DEMAND, z_index=15) for q, p in HER]
        iqd_def = definition('Individual Quantity Demanded', 'is the quantity a buyer is willing and able to buy at a given price.')
        iqd_def.scale(0.7).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(dots[0]))
        self.play(Write(iqd_def))
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
        idc_def.scale(0.7).to_edge(DOWN, buff=0.25)
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.4))
        self.bring_to_front(*dots)
        self.play(FadeOut(iqd_def), Write(idc_def))
        self.pause()

        # B07 ---------------------------------------------------------
        # the pattern in the answers

        law_def = definition('Law of Demand', "is a good's quantity demanded falling with its price.")
        law_def.scale(0.7).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(idc_def), Write(law_def))
        self.pause()

        # B08 ---------------------------------------------------------
        # the linear approximation, drawn from the intercept down; the data
        # fades the jagged observations into the background.

        demand = ax.plot(lambda q: 2.5 - q / 2, x_range=[0, 5], color=DEMAND)
        eqn = Tex('$P = 2.5 - Q/2$').scale(0.9).set_color(INK).move_to(ax.c2p(4.3, 2.0))
        d_lab = Tex('D').set_color(INK).next_to(ax.c2p(5, 0), UR, buff=0.15)
        self.play(Create(demand),
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
        q_lab2 = Tex('Q').set_color(INK).next_to(ax2.c2p(6, 0), RIGHT, buff=0.25)
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
        # a price gives a quantity: the directional read at $1.50

        # Trace the known value to the curve, then to the answer's axis.
        # Highlight the existing 1.50 tick; don't draw a second numeral over it.
        read_a_source = ax2.get_y_axis().numbers[2].copy().set_color(INK)
        read_a_first = DashedLine(ax2.c2p(0, 1.5), ax2.c2p(2, 1.5), color=GUIDE).set_opacity(0.3)
        read_a_second = DashedLine(ax2.c2p(2, 1.5), ax2.c2p(2, 0), color=GUIDE).set_opacity(0.3)
        read_a_dot = Dot(ax2.c2p(2, 1.5), color=GUIDE)
        read_a_answer = Tex('$Q_d = 2$').scale(0.7).set_color(INK)
        read_a_answer.next_to(ax2.c2p(2, 0), DOWN, buff=0.65)
        read_a = VGroup(read_a_source, read_a_first, read_a_second, read_a_dot, read_a_answer)
        work = VGroup(
            Tex('$1.50 = 2.5 - Q/2$'),
            Tex('$Q = 2$'))
        work.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        work.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(read_a_source), Create(read_a_first))
        self.play(FadeIn(read_a_dot), Create(read_a_second))
        self.play(Write(read_a_answer))
        self.play(LaggedStart(*[Write(r) for r in work], lag_ratio=0.6))
        self.pause()

        # B09b --------------------------------------------------------
        # ...and one that lands between two bars

        # Trace the known value to the curve, then to the answer's axis.
        read_b_source = Tex('$1.75$').scale(0.7).set_color(INK)
        read_b_source.next_to(ax2.c2p(0, 1.75), LEFT, buff=0.3)
        read_b_first = DashedLine(ax2.c2p(0, 1.75), ax2.c2p(1.5, 1.75), color=GUIDE).set_opacity(0.3)
        read_b_second = DashedLine(ax2.c2p(1.5, 1.75), ax2.c2p(1.5, 0), color=GUIDE).set_opacity(0.3)
        read_b_dot = Dot(ax2.c2p(1.5, 1.75), color=GUIDE)
        read_b_answer = Tex('$Q_d = 1.5$').scale(0.7).set_color(INK)
        read_b_answer.next_to(ax2.c2p(1.5, 0), DOWN, buff=0.65)
        read_b = VGroup(read_b_source, read_b_first, read_b_second, read_b_dot, read_b_answer)
        work_b = VGroup(
            Tex('$1.75 = 2.5 - Q/2$'),
            Tex('$Q = 1.5$'))
        work_b.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        work_b.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeOut(read_a), FadeOut(work))
        self.play(FadeIn(read_b_source), Create(read_b_first))
        self.play(FadeIn(read_b_dot), Create(read_b_second))
        self.play(Write(read_b_answer))
        self.play(LaggedStart(*[Write(r) for r in work_b], lag_ratio=0.6))
        self.pause()

        # B10 ---------------------------------------------------------
        # the reverse read: a quantity gives a price

        self.play(Transform(head, title('Marginal Benefit')),
                  FadeOut(read_b), FadeOut(work_b))
        # Trace the known value to the curve, then to the answer's axis.
        read_c_source = ax2.get_x_axis().numbers[2].copy().set_color(INK)
        read_c_first = DashedLine(ax2.c2p(3, 0), ax2.c2p(3, 1.0), color=GUIDE).set_opacity(0.3)
        read_c_second = DashedLine(ax2.c2p(3, 1.0), ax2.c2p(0, 1.0), color=GUIDE).set_opacity(0.3)
        read_c_dot = Dot(ax2.c2p(3, 1.0), color=GUIDE)
        read_c_answer = Tex('$MB = 1$').scale(0.7).set_color(INK)
        read_c_answer.next_to(ax2.c2p(0, 1.0), LEFT, buff=0.65)
        read_c = VGroup(read_c_source, read_c_first, read_c_second, read_c_dot, read_c_answer)
        work_c = VGroup(
            Tex('$P = 2.5 - 3/2$'),
            Tex('$P = \\$1.00$'))
        work_c.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        work_c.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(read_c_source), Create(read_c_first))
        self.play(FadeIn(read_c_dot), Create(read_c_second))
        self.play(Write(read_c_answer))
        self.play(LaggedStart(*[Write(r) for r in work_c], lag_ratio=0.6))
        self.pause()

        # B10b --------------------------------------------------------

        mb_def = definition('Marginal Benefit', 'is the value of one more unit.')
        mb_def.scale(0.7).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(work_c), Write(mb_def))
        self.pause()

        # B11 ---------------------------------------------------------

        stage1, card1 = exercise_card(
            self, 'Exercise B1 $|$ Quantity Demanded',
            ['Pumpkin pasties sell along the demand curve $P=12-Q/2$, in galleons and '
             'thousands of pasties. (a) What is the quantity demanded at 10 galleons? '
             '(b) What is the marginal benefit at a quantity of 4 thousand?'])
        self.pause()

        # B12 ---------------------------------------------------------
        # Isolate bar 1: no other bars and no demand curve. Expenditure first.

        self.play(Restore(stage1), FadeOut(card1))
        self.play(FadeOut(mb_def), FadeOut(read_c), FadeOut(rest_bars),
                  FadeOut(demand2), FadeOut(eqn2), FadeOut(d_lab2),
                  q_lab2.animate.shift(DOWN * 0.45))
        self.play(Transform(head, title('Consumer Surplus')))

        price = ValueTracker(1)
        selected_unit = ValueTracker(1)   # changed between examples, never animated
        cs_reveal = ValueTracker(0)       # fade CS in AFTER the expenditure pause

        grey_bar = Polygon(ax2.c2p(0, 0), ax2.c2p(1, 0),
                           ax2.c2p(1, 2), ax2.c2p(0, 2))
        expenditure_box = grey_bar.copy()
        surplus_box = grey_bar.copy()
        expenditure_label = Tex('Expenditure').scale(0.7).set_color(GOV)
        surplus_label = Tex('Consumer Surplus').scale(0.7).set_color(DEMAND)
        expenditure_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(INK)
        surplus_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(INK)
        price_line = Line(ax2.c2p(0, 1), ax2.c2p(5.4, 1), color=GUIDE, stroke_width=2)
        price_word = Tex(r'Price \$').scale(0.7).set_color(INK)
        price_number = DecimalNumber(1, num_decimal_places=2).scale(0.7).set_color(INK)
        price_label = VGroup(price_word, price_number)
        cs_group = VGroup(surplus_box, surplus_number, surplus_label)
        expenditure_group = VGroup(expenditure_box, expenditure_number, expenditure_label)
        exchange = VGroup(grey_bar, expenditure_group, cs_group, price_line, price_label)

        # One updater is needed for continuous price motion. It changes these
        # named objects only; all choreography remains in the beats below.
        def update_exchange(group):
            q = int(selected_unit.get_value())
            mb = 2.5 - q / 2
            p = price.get_value()
            buys = p <= mb
            paid = min(p, mb)
            surplus = max(mb - p, 0)
            reveal = cs_reveal.get_value() if buys and surplus > 0 else 0

            grey_bar.set_points_as_corners([
                ax2.c2p(q - 1, 0), ax2.c2p(q, 0), ax2.c2p(q, mb),
                ax2.c2p(q - 1, mb), ax2.c2p(q - 1, 0)])
            grey_bar.set_stroke(MUTED, 2).set_fill(MUTED, 0.10 if buys else 0.45)

            expenditure_box.set_points_as_corners([
                ax2.c2p(q - 1, 0), ax2.c2p(q, 0), ax2.c2p(q, paid),
                ax2.c2p(q - 1, paid), ax2.c2p(q - 1, 0)])
            expenditure_box.set_stroke(GOV, 2, opacity=1 if buys else 0)
            expenditure_box.set_fill(GOV, AREA_OPACITY if buys else 0)
            expenditure_number.set_value(p).move_to(ax2.c2p(q - 0.5, paid / 2))
            expenditure_number.set_opacity(1 if buys and paid >= 0.18 else 0)
            expenditure_label.next_to(ax2.c2p(q, paid / 2), RIGHT, buff=0.3)
            expenditure_label.set_opacity(1 if buys else 0)

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
        self.play(FadeIn(exchange))
        exchange.add_updater(update_exchange)
        self.pause()

        # B12b --------------------------------------------------------
        # Now introduce the extra value ABOVE the price, inside the same bar.

        cs_def = definition('Consumer Surplus', "is the buyer's extra value from an exchange.")
        cs_def.scale(0.7).to_edge(DOWN, buff=0.25)
        self.play(cs_reveal.animate.set_value(1), Write(cs_def))
        self.pause()

        # B12c --------------------------------------------------------
        # Above MB: the entire unit is grey; both transaction labels disappear.

        self.play(price.animate.set_value(2.4), run_time=2)
        self.pause()

        # B12c2 -------------------------------------------------------
        # A lower price: expenditure shrinks and consumer surplus grows.

        self.play(price.animate.set_value(0.5), run_time=2.5)
        self.pause()

        # B12c3 -------------------------------------------------------

        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12d --------------------------------------------------------
        # Reconnect to all potential units before isolating the second one.

        exchange.clear_updaters()
        self.remove(price, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars))
        self.pause()

        # B12e --------------------------------------------------------
        # Bar 2, expenditure only. Price remains $1; this bar's MB is $1.50.

        selected_unit.set_value(2)
        cs_reveal.set_value(0)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.play(FadeOut(rest_bars), FadeIn(exchange))
        exchange.add_updater(update_exchange)
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
        # The grey context returns; then bar 3 is the only unit on the axes.

        exchange.clear_updaters()
        self.remove(price, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars))
        self.pause()
        selected_unit.set_value(3)
        cs_reveal.set_value(0)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.play(FadeOut(rest_bars), FadeIn(exchange))
        exchange.add_updater(update_exchange)
        self.pause()

        # B12i --------------------------------------------------------
        # At $1 this marginal unit has zero CS. Lowering price makes CS visible.

        self.play(cs_reveal.animate.set_value(1), price.animate.set_value(0.5), run_time=2)
        self.pause()
        self.play(price.animate.set_value(1.4), run_time=2)
        self.pause()
        self.play(price.animate.set_value(1), run_time=1.5)
        self.pause()

        # B12j --------------------------------------------------------
        # Context again, then only bar 4. At $1 it stays grey: MB is $0.50.

        exchange.clear_updaters()
        self.remove(price, cs_reveal)
        self.play(FadeOut(exchange), FadeIn(rest_bars))
        self.pause()
        selected_unit.set_value(4)
        cs_reveal.set_value(0)
        exchange.set_opacity(1)
        update_exchange(exchange)
        self.play(FadeOut(rest_bars), FadeIn(exchange))
        exchange.add_updater(update_exchange)
        self.pause()

        # B12k --------------------------------------------------------
        # A price she will accept: expenditure first, pause, then its CS.

        self.play(price.animate.set_value(0.25), run_time=2)
        self.pause()
        self.play(cs_reveal.animate.set_value(1))
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
        self.remove(price, cs_reveal, selected_unit)
        self.play(FadeOut(exchange), FadeIn(rest_bars),
                  FadeIn(demand2), FadeIn(eqn2), FadeIn(d_lab2),
                  q_lab2.animate.shift(UP * 0.45))
        price13 = VGroup(
            Line(ax2.c2p(0, 1), ax2.c2p(5.4, 1), color=GUIDE, stroke_width=2).set_opacity(0.6),
            Tex(r'Price $= \$1$').scale(0.7).set_color(INK)
                .next_to(ax2.c2p(0, 1), LEFT, buff=0.65))
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
            Tex(r'CS $= 1.00 + 0.50 + 0.00 = \$1.50$'),
            Tex(r'Expenditure $= 3 \times \$1 = \$3$'))
        tally.scale(0.7).set_color(INK).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        tally.move_to(MATH_AT, aligned_edge=LEFT)
        qd_mark = Tex('$Q_d = 3$').scale(0.7).set_color(INK)
        qd_mark.next_to(ax2.c2p(3, 0), DOWN, buff=0.65)
        self.play(Write(tally), Write(qd_mark))
        self.pause()

        # B13 ---------------------------------------------------------
        # Compare the bar sum with the continuous triangle.

        tri = Polygon(ax2.c2p(0, 1), ax2.c2p(3, 1), ax2.c2p(0, 2.5),
                      color=DEMAND, fill_opacity=AREA_OPACITY)
        self.play(FadeOut(all_expenditure), FadeOut(tally), FadeOut(cs_def),
                  rest_bars[3].animate.set_fill(MUTED, REST_OPACITY).set_stroke(MUTED, 1),
                  ReplacementTransform(all_cs, tri))
        self.pause()

        # B13b --------------------------------------------------------

        area = VGroup(
            Tex('Area $= \\frac{1}{2} h b$'))
        area.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        area.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(Write(area[0]))
        self.pause()

        # B13c --------------------------------------------------------
        # the height, on the P axis

        h_bar = Line(ax2.c2p(0, 1), ax2.c2p(0, 2.5), color=GUIDE, stroke_width=4)
        h_lab = (Tex('$h = \\$1.50$').scale(0.7).set_color(INK)
                 .next_to(ax2.c2p(0, 1.75), LEFT, buff=0.55))
        self.play(Create(h_bar), FadeIn(h_lab))
        self.pause()

        # B13d --------------------------------------------------------
        # the base, on the Q axis

        b_bar = Line(ax2.c2p(0, 0), ax2.c2p(3, 0), color=GUIDE, stroke_width=4)
        b_lab = (Tex('$b = 3$').scale(0.7).set_color(INK)
                 .next_to(ax2.c2p(1.5, 0), UP, buff=0.15))
        self.play(Create(b_bar), FadeIn(b_lab))
        self.pause()

        # B13e --------------------------------------------------------
        # the two numbers fly into the equation; almost the bars' number

        solve = VGroup(
            Tex('Area $= \\frac{1}{2} h b$'),
            Tex('$= \\frac{1}{2} (1.50)(3)$'),
            Tex('$= \\$2.25$'))
        solve.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        solve.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeOut(area))
        self.play(Write(solve[0]))
        self.play(TransformFromCopy(VGroup(h_lab, b_lab), solve[1]))
        self.play(Write(solve[2]))
        self.pause()

        # B14 ---------------------------------------------------------

        stage2, card2 = exercise_card(
            self, 'Exercise B1 $|$ Consumer Surplus',
            ['Pumpkin pasties again, $P=12-Q/2$. (a) What is the quantity demanded at '
             '5 galleons? (b) Find and label the consumer surplus at that price.'])
        self.pause()

        # B15 ---------------------------------------------------------
        # the live room tally

        self.play(Restore(stage2), FadeOut(card2))
        self.play(FadeOut(VGroup(tri, solve, h_bar, h_lab, b_bar, b_lab,
                                 qd_mark, price13)))
        stage3, card3 = exercise_card(
            self, 'Market Demand $|$ Simulation',
            ['Tally the room at a range of prices, building the market curve on the board.'])
        self.pause()

        # B16 ---------------------------------------------------------
        # PLACEHOLDER -- the 3D Sim/ beat replaces this whole beat. Clean card.

        FadeAll(self)
        sum_def = definition('Market Demand',
                             "is the sum of everyone's individual quantity demanded.")
        self.play(Write(sum_def))
        self.pause()

        # B17 ---------------------------------------------------------
        # the market curve, drawn from the top, over its own standing bars

        FadeAll(self)
        head = title('Market Demand')
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
        m_q = Tex('Q').set_color(INK).next_to(ax_m.c2p(62, 0), RIGHT, buff=0.7)
        m_p = Tex('P').set_color(INK).next_to(ax_m.c2p(0, 13), LEFT, buff=0.25)
        m_cap = Tex(narration('spinach, thousands of lbs per month')).scale(0.7).set_color(CAPTION)
        m_cap.move_to([GRAPH_AT[0], -3.7, 0])
        demand_m = ax_m.plot(lambda q: 12 - q / 5, x_range=[0, 60], color=DEMAND)
        eqn_m = Tex('$P = 12 - Q/5$').scale(0.9).set_color(INK).move_to(ax_m.c2p(40, 9))
        d_lab_m = Tex('D').set_color(INK).next_to(ax_m.c2p(60, 0), UR, buff=0.15)

        # Each thin rectangle stands for a small quantity interval (thousands
        # of pounds), not a fabricated observation or a particular buyer.
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

        self.play(FadeIn(head), FadeIn(ax_m), FadeIn(m_p), FadeIn(m_q), FadeIn(m_cap),
                  Create(demand_m))
        self.add(market_g)
        self.play(FadeIn(eqn_m), FadeIn(d_lab_m))
        self.pause()

        # B17b --------------------------------------------------------
        # the market read at $5

        # Trace the known value to the curve, then to the answer's axis.
        read_m_source = Tex('$5$').scale(0.7).set_color(INK)
        read_m_source.next_to(ax_m.c2p(0, 5), LEFT, buff=0.3)
        read_m_first = DashedLine(ax_m.c2p(0, 5), ax_m.c2p(35, 5), color=GUIDE).set_opacity(0.3)
        read_m_second = DashedLine(ax_m.c2p(35, 5), ax_m.c2p(35, 0), color=GUIDE).set_opacity(0.3)
        read_m_dot = Dot(ax_m.c2p(35, 5), color=GUIDE)
        read_m_answer = Tex('$Q_d = 35$').scale(0.7).set_color(INK)
        read_m_answer.next_to(ax_m.c2p(35, 0), DOWN, buff=0.65)
        read_m = VGroup(read_m_source, read_m_first, read_m_second, read_m_dot, read_m_answer)
        self.play(FadeIn(read_m_source), Create(read_m_first))
        self.play(FadeIn(read_m_dot), Create(read_m_second))
        self.play(Write(read_m_answer))
        mwork = VGroup(
            Tex('$5 = 12 - Q/5$'),
            Tex('$Q = 35$ thousand lbs'))
        mwork.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        mwork.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(LaggedStart(*[Write(r) for r in mwork], lag_ratio=0.6))
        self.pause()

        # B17c --------------------------------------------------------
        # ...and at $2

        # Trace the known value to the curve, then to the answer's axis.
        read_m2_source = ax_m.get_y_axis().numbers[0].copy().set_color(INK)
        read_m2_first = DashedLine(ax_m.c2p(0, 2), ax_m.c2p(50, 2), color=GUIDE).set_opacity(0.3)
        read_m2_second = DashedLine(ax_m.c2p(50, 2), ax_m.c2p(50, 0), color=GUIDE).set_opacity(0.3)
        read_m2_dot = Dot(ax_m.c2p(50, 2), color=GUIDE)
        read_m2_answer = Tex('$Q_d = 50$').scale(0.7).set_color(INK)
        read_m2_answer.next_to(ax_m.c2p(50, 0), DOWN, buff=0.65)
        read_m2 = VGroup(read_m2_source, read_m2_first, read_m2_second, read_m2_dot, read_m2_answer)
        mwork_b = VGroup(
            Tex('$2 = 12 - Q/5$'),
            Tex('$Q = 50$ thousand lbs'))
        mwork_b.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        mwork_b.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeOut(read_m), FadeOut(mwork))
        self.play(FadeIn(read_m2_source), Create(read_m2_first))
        self.play(FadeIn(read_m2_dot), Create(read_m2_second))
        self.play(Write(read_m2_answer))
        self.play(LaggedStart(*[Write(r) for r in mwork_b], lag_ratio=0.6))
        self.pause()

        # B18 ---------------------------------------------------------
        # too many bars to walk, so expenditure arrives as ONE rectangle

        # Trace the known value to the curve, then to the answer's axis.
        read_m5_source = Tex('$5$').scale(0.7).set_color(INK)
        read_m5_source.next_to(ax_m.c2p(0, 5), LEFT, buff=0.3)
        read_m5_first = DashedLine(ax_m.c2p(0, 5), ax_m.c2p(35, 5), color=GUIDE).set_opacity(0.3)
        read_m5_second = DashedLine(ax_m.c2p(35, 5), ax_m.c2p(35, 0), color=GUIDE).set_opacity(0.3)
        read_m5_dot = Dot(ax_m.c2p(35, 5), color=GUIDE)
        read_m5_answer = Tex('$Q_d = 35$').scale(0.7).set_color(INK)
        read_m5_answer.next_to(ax_m.c2p(35, 0), DOWN, buff=0.65)
        read_m5 = VGroup(read_m5_source, read_m5_first, read_m5_second, read_m5_dot, read_m5_answer)
        self.play(FadeOut(read_m2), FadeOut(mwork_b))
        self.play(FadeIn(read_m5))
        spend_rect = Polygon(ax_m.c2p(0, 0), ax_m.c2p(35, 0), ax_m.c2p(35, 5), ax_m.c2p(0, 5),
                             color=GOV, fill_opacity=AREA_OPACITY)
        spend_rect.z_index = 1
        spend_lab = (Tex('Expenditure').scale(0.7).set_color(INK)
                     .move_to(ax_m.c2p(17.5, 2.5)))
        spend_math = VGroup(
            Tex('Expenditure $= P \\times Q_d$'),
            Tex('$= \\$5 \\times 35{,}000$'),
            Tex('$= \\$175{,}000$'))
        spend_math.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        spend_math.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(spend_rect), FadeIn(spend_lab))
        self.play(LaggedStart(*[Write(r) for r in spend_math], lag_ratio=0.6))
        self.pause()

        # B18b --------------------------------------------------------
        # the surplus IS the sweep: the height, then right through the bars
        # with the base extending under them

        self.play(FadeOut(spend_math))
        h_bar_m = Line(ax_m.c2p(0, 5), ax_m.c2p(0, 12), color=GUIDE, stroke_width=4)
        h_lab_m = (Tex('$h = \\$7$').scale(0.7).set_color(INK)
                   .next_to(ax_m.c2p(0, 8.5), LEFT, buff=0.55))
        self.play(Create(h_bar_m), FadeIn(h_lab_m))

        base_bar = Line(ax_m.c2p(0, 0), ax_m.c2p(0.01, 0),
                        color=GUIDE, stroke_width=4)
        self.add(base_bar)
        for index, cs_bar in enumerate(market_cs):
            right = (index + 1) * 2.5
            next_base = Line(ax_m.c2p(0, 0), ax_m.c2p(right, 0),
                             color=GUIDE, stroke_width=4)
            self.play(FadeIn(cs_bar), Transform(base_bar, next_base), run_time=0.2)
        self.play(Transform(base_bar, Line(ax_m.c2p(0, 0), ax_m.c2p(35, 0),
                                          color=GUIDE, stroke_width=4)))
        # The continuous triangle fills the small gaps above the steps before
        # its exact area is calculated. The unit grid remains visible.
        market_triangle = Polygon(ax_m.c2p(0, 5), ax_m.c2p(35, 5), ax_m.c2p(0, 12),
                                  color=DEMAND, fill_opacity=AREA_OPACITY)
        self.play(ReplacementTransform(market_cs, market_triangle))

        cs_lab_m = (Tex('Consumer Surplus').scale(0.65).set_color(INK)
                    .move_to(ax_m.c2p(14.5, 6.4)))
        cs_math = VGroup(
            Tex('CS $= \\frac{1}{2} h b$'),
            Tex('$= \\frac{1}{2}(7)(35{,}000)$'),
            Tex('$= \\$122{,}500$'))
        cs_math.scale(0.8).set_color(INK).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        cs_math.move_to(MATH_AT, aligned_edge=LEFT)
        self.play(FadeIn(cs_lab_m))
        self.play(LaggedStart(*[Write(r) for r in cs_math], lag_ratio=0.6))
        self.pause()

        # B19 ---------------------------------------------------------
        # the limitation: willing, but not always able

        FadeAll(self)

        # a schematic stage: bare axes, no numerals, no equations -- the
        # sentence's picture and nothing else
        ax_s = style_axes(x_range=[0, 10, 10], y_range=[0, 10, 10],
                          x_length=GRAPH_W, y_length=GRAPH_H).scale(GRAPH_SCALE)
        ax_s.shift(GRAPH_AT - (ax_s.c2p(0, 0) + ax_s.c2p(10, 10)) / 2)
        s_p = Tex('P').set_color(INK).next_to(ax_s.c2p(0, 10), RIGHT, buff=0.25)
        s_q = Tex('Q').set_color(INK).next_to(ax_s.c2p(10, 0), RIGHT, buff=0.25)
        head = title('Demand')
        rich = ax_s.plot(lambda q: 9 - 0.9 * q, x_range=[0, 10], color=DEMAND)
        poor = ax_s.plot(lambda q: 4.5 - 0.9 * q, x_range=[0, 5], color=DEMAND)
        rich_lab = (Tex('rich person').scale(0.6).set_color(INK)
                    .next_to(ax_s.c2p(7.5, 2.25), UR, buff=0.2))
        poor_lab = (Tex('poor person').scale(0.6).set_color(INK)
                    .next_to(ax_s.c2p(3.2, 1.62), UR, buff=0.2))
        self.play(FadeIn(head), FadeIn(ax_s), FadeIn(s_p), FadeIn(s_q))
        self.play(Create(rich), FadeIn(rich_lab))
        self.play(Create(poor), FadeIn(poor_lab))
        self.pause()

        # B20 ---------------------------------------------------------

        FadeAll(self)
        head = title('Next Time $|$ Sellers', scale=1.5)
        topic = Tex('What does it cost them to say yes to a trade?').scale(1.2).set_color(INK)
        self.play(FadeIn(head), Write(topic))
        self.pause()
