# maniml 03_Code.py EpisodeA1
#
# Episode A1 | The space of what's possible
# One scene; beats follow 02_Storyboard.md (B01...B31). Talking-head beats
# (the pool-table paragraph, the closing) are gaps between sections.

from manim import *
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, title(), bumper(), ...
from style import axes as style_axes
from Video import PPF_Function, PPF_Function_New, PPF_Function_Tech

FARM_AT = LEFT * 4 + DOWN / 2
ALPHA = 4 / 5                # the 8-hour day: 4/5 of the farm planted


def choice_boxes(a, b, buff=0.3):
    """Green (chosen) and red (given up) boxes of the same size around two mobjects."""
    w = max(a.get_width(), b.get_width()) + 2 * buff
    h = max(a.get_height(), b.get_height()) + 2 * buff
    box_a = Rectangle(width=w, height=h, color=EFFICIENT).move_to(a)
    box_b = Rectangle(width=w, height=h, color=NASH).move_to(b)
    return box_a, box_b


def farm_plot():
    """The farm: outline and name. Crop fills hang from under the name so
    partial splits keep the planted band anchored at the top."""
    farm = Rectangle(height=5, width=4, color=INK).move_to(FARM_AT)
    farm.z_index = 2
    farm_name = Tex("Molly's Farm").scale(1.5).next_to(farm, UP, buff=1 / 2)
    return farm, farm_name


def exercise_card(scene, head_text, lines):
    """Cut-to-exercise: the stage itself fades to near-black and the question
    writes on a rounded panel. (Not a dim overlay: in the GL viewer strokes
    draw over translucent fills, so an overlay leaves the stage punching
    through.) The panel's top corners are fixed; its height follows the text,
    and lines wrap to the panel width (Tex has no paragraph wrapping).
    Returns (stage, card); Restore(stage) brings the stage back, or the next
    FadeAll clears it with everything else."""
    stage = VGroup(*scene.mobjects)
    stage.save_state()
    margin, pad = 1.5, 0.6                       # frame-to-panel, panel-to-text
    text_width = FRAME_W - 2 * (margin + pad)

    def rows(text, scale=0.9):
        whole = Tex(text).scale(scale)
        if whole.get_width() <= text_width:
            return [whole]
        out, current = [], ''
        for word in text.split():
            trial = (current + ' ' + word).strip()
            if current and Tex(trial).scale(scale).get_width() > text_width:
                out.append(current)
                current = word
            else:
                current = trial
        out.append(current)
        return [Tex(r).scale(scale) for r in out]

    head = Tex(head_text).scale(SCALE_TITLE).set_color(DEFINITION)
    body = VGroup(*rows(' '.join(lines)))        # one flowing paragraph, not a list
    body.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
    card = VGroup(head, body).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
    panel = RoundedRectangle(width=FRAME_W - 2 * margin, height=card.get_height() + 2 * pad,
                             corner_radius=0.25, color='#3a3a3a', stroke_width=2,
                             fill_color='#161616', fill_opacity=1).to_edge(UP, buff=0.8)
    card.align_to(panel, UL).shift(RIGHT * pad + DOWN * pad)
    scene.play(stage.animate.set_opacity(0.05), FadeIn(panel), Write(head), FadeIn(body))
    return stage, VGroup(panel, card)


class EpisodeA1(Scene):
    """Episode A1 | The space of what's possible.

    One flat construct(). Each `# Bxx` section is self-contained: it clears
    the previous beat's objects, builds its own, and ends at the pause()
    the viewer parks on before the next section.
    """

    def construct(self):

        # B01 ---------------------------------------------------------

        squares = bumper_raster(self)

        # B01b --------------------------------------------------------

        flicker(self, squares)

        # B01c --------------------------------------------------------

        label = bumper_title(self, squares, 'A', 1)
        thesis = Tex("\\textit{The Production Possiblity Frontier}").scale(1.2).set_color(MUTED).next_to(label, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause()

        # B02 ---------------------------------------------------------

        FadeAll(self)
        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B03 ---------------------------------------------------------

        self.play(FadeOut(last_card), run_time=1 / 2)
        head = title('Opportunity Cost')
        OR = Tex(' or ').scale(1.5)
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(head))
        self.play(FadeIn(A))
        self.play(FadeIn(OR))
        self.play(FadeIn(B))
        box_a, box_b = choice_boxes(A, B)
        self.play(FadeIn(box_a))
        self.play(FadeIn(box_b))
        self.pause()

        # B03b --------------------------------------------------------

        cost = Tex('Opportunity Cost({{A}}) = {{B}}').scale(1.5).next_to(OR, DOWN, buff=1.2).set_color_by_tex_to_color_map({
            'A': EFFICIENT,
            'B': NASH,
        })
        self.play(Write(cost))
        self.pause()

        # B03c --------------------------------------------------------

        cost2 = Tex('Opportunity Cost({{B}}) = {{A}}').scale(1.5).move_to(cost).set_color_by_tex_to_color_map({
            'A': NASH,
            'B': EFFICIENT,
        })
        self.play(box_a.animate.move_to(B), box_b.animate.move_to(A), Transform(cost, cost2))
        self.pause()

        # B04 ---------------------------------------------------------

        oc_def = definition('Opportunity Cost', 'is the value of the next best use of your resources.').to_edge(DOWN, buff=0.4)
        self.play(Write(oc_def))
        self.pause()

        # B05 ---------------------------------------------------------

        FadeAll(self)
        farm, farm_name = farm_plot()
        self.play(FadeIn(farm), FadeIn(farm_name))
        self.pause()

        # B05b --------------------------------------------------------

        spinach = Rectangle(height=5, width=4, color=SPINACH, fill_opacity=1).move_to(FARM_AT)
        carrots = Rectangle(height=0, width=4, color=CARROTS, fill_opacity=1).next_to(spinach, UP, buff=0)
        spinach_harvest = Tex('{{40}} {{S}}').scale(1.5).move_to(RIGHT * 4).set_color_by_tex_to_color_map({
            'S': SPINACH,
        })
        self.play(FadeIn(carrots), FadeIn(spinach))
        self.play(FadeIn(spinach_harvest, shift=spinach_harvest.get_center() - FARM_AT))
        self.pause()

        # B05c --------------------------------------------------------

        carrots_full = Rectangle(height=5, width=4, color=CARROTS, fill_opacity=1).move_to(FARM_AT)
        spinach_empty = Rectangle(height=0, width=4, color=SPINACH, fill_opacity=1).next_to(carrots_full, DOWN, buff=0)
        self.play(Transform(spinach, spinach_empty), Transform(carrots, carrots_full))
        OR = Tex('or').scale(1.5).next_to(spinach_harvest, LEFT, buff=1)
        carrot_harvest = Tex('{{10}} {{C}}').scale(1.5).next_to(OR, LEFT, buff=1).set_color_by_tex_to_color_map({
            'C': CARROTS,
        })
        self.play(FadeIn(OR), FadeIn(carrot_harvest, shift=carrot_harvest.get_center() - FARM_AT))
        self.pause()

        # B06 ---------------------------------------------------------

        equal = Tex('=').scale(1.5).move_to(OR)
        self.play(Transform(OR, equal))
        self.play(self.camera.frame.animate.move_to(OR).set(width=OR.width * 15))
        self.pause()

        # B06b --------------------------------------------------------

        carrot_frac = Tex(r'$\frac{10}{10}$ {{C}}').scale(1.5).next_to(OR, LEFT, buff=1).set_color_by_tex_to_color_map({
            'C': CARROTS,
        })
        spinach_frac = Tex(r'$\frac{40}{10}$ {{S}}').scale(1.5).next_to(OR, RIGHT, buff=1).set_color_by_tex_to_color_map({
            'S': SPINACH,
        })
        self.play(Transform(carrot_harvest, carrot_frac), Transform(spinach_harvest, spinach_frac))
        self.pause()

        # B06c --------------------------------------------------------

        carrot_one = Tex('{{1}} {{C}}').scale(1.5).next_to(OR, LEFT, buff=1).set_color_by_tex_to_color_map({
            'C': CARROTS,
        })
        spinach_four = Tex('{{4}} {{S}}').scale(1.5).next_to(OR, RIGHT, buff=1).set_color_by_tex_to_color_map({
            'S': SPINACH,
        })
        self.play(Transform(carrot_harvest, carrot_one), Transform(spinach_harvest, spinach_four),
                  FadeOut(farm), FadeOut(farm_name), FadeOut(spinach), FadeOut(carrots))
        self.pause()

        # B07 ---------------------------------------------------------

        op_cost = Tex('Opportunity Cost(1 {{$C$}}) = 4 {{$S$}}').scale(1.5).next_to(OR, UP, buff=2).set_color_by_tex_to_color_map({
            '$C$': CARROTS,
            '$S$': SPINACH,
        })
        mid = (op_cost.get_center() + OR.get_center()) / 2   # keep the 1 C = 4 S line in frame too
        self.play(self.camera.frame.animate.move_to(mid).set(width=op_cost.width * 1.5))
        self.play(Write(op_cost))
        self.pause()

        # B10 ---------------------------------------------------------

        FadeAll(self)
        self.camera.frame.move_to(ORIGIN).set(width=FRAME_W)
        axes = style_axes(
            x_range=[0, 11, 1], y_range=[0, 45, 5], x_length=5.5, y_length=6, ticks=True,
            x_axis_config={'numbers_to_include': np.arange(0, 11, 2),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': CARROTS}},
            y_axis_config={'numbers_to_include': np.arange(10, 50, 10),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': SPINACH}},
        ).shift(RIGHT * 2 + DOWN / 2).scale(0.8)

        farm, farm_name = farm_plot()
        carrots = Rectangle(height=5, width=4, color=CARROTS, fill_opacity=1).next_to(farm_name, DOWN, buff=1 / 2)
        spinach = Rectangle(height=0, width=4, color=SPINACH, fill_opacity=1).next_to(carrots, DOWN, buff=0)
        self.play(FadeIn(farm), FadeIn(farm_name), FadeIn(carrots), FadeIn(spinach))

        dot = Dot(axes.c2p(10, 0), color=GUIDE, z_index=10)
        t1, c_num, comma, s_num, t2 = label = VGroup(
            Tex('(').scale(1.2),
            DecimalNumber(10, num_decimal_places=1, include_sign=False, color=CARROTS).scale(1.2),
            Tex(',').scale(1.2),
            DecimalNumber(0, num_decimal_places=1, include_sign=False, color=SPINACH).scale(1.2),
            Tex(')').scale(1.2),
        )
        label.arrange(RIGHT, buff=0.15)
        comma.align_to(c_num, DOWN)
        label.add_updater(lambda m: m.next_to(dot, UP + RIGHT))   # maniml's always() applies only once
        self.play(FadeIn(axes), FadeIn(label), FadeIn(dot))
        c_num.add_updater(lambda m: m.set_value(carrots.get_height() * 2).next_to(t1, RIGHT, buff=0.1))
        comma.add_updater(lambda m: m.next_to(c_num, RIGHT, buff=0.05).align_to(c_num, DOWN))
        s_num.add_updater(lambda m: m.set_value(spinach.get_height() * 8).next_to(comma, RIGHT, buff=0.15).align_to(c_num, DOWN))
        t2.add_updater(lambda m: m.next_to(s_num, RIGHT, buff=0.1).align_to(t1, DOWN))
        self.pause()

        # B10b --------------------------------------------------------

        marks = VGroup(Dot(axes.c2p(10, 0), color=INK))
        self.add(marks)

        def split_to(c_alpha):
            c_new = Rectangle(height=c_alpha * 5, width=4, color=CARROTS, fill_opacity=1).next_to(farm_name, DOWN, buff=1 / 2)
            s_new = Rectangle(height=(1 - c_alpha) * 5, width=4, color=SPINACH, fill_opacity=1).next_to(c_new, DOWN, buff=0)
            p = axes.c2p(c_alpha * 10, (1 - c_alpha) * 40)
            self.play(dot.animate.move_to(p), Transform(spinach, s_new), Transform(carrots, c_new))
            marks.add(Dot(p, color=INK))
            self.add(marks[-1])

        split_to(0)
        self.pause()

        # B11 ---------------------------------------------------------

        split_to(1 / 2)
        self.pause()

        # B11b --------------------------------------------------------

        split_to(3 / 5)
        self.pause()

        # B11c --------------------------------------------------------

        split_to(3 / 10)
        self.pause()

        # B12 ---------------------------------------------------------

        ppf_graph = axes.plot(PPF_Function, color=MOLLY, x_range=(0, 10), z_index=-1)
        ppf_title = title("Molly's Production Possibility Frontier")
        grow = Rectangle(height=5, width=4, color=MOLLY, fill_opacity=1).next_to(farm_name, DOWN, buff=1 / 2)
        for m in (label, c_num, comma, s_num, t2):
            m.clear_updaters()
        self.play(Create(ppf_graph), Transform(farm_name, ppf_title), FadeIn(grow),
                  FadeOut(carrots), FadeOut(spinach), FadeOut(marks), FadeOut(dot), FadeOut(label))
        self.pause()

        # B13 ---------------------------------------------------------

        eq = MathTex('S', '=', '40', '-', '4', 'C').scale(1.2).move_to(axes.c2p(7.5, 38))
        eq[0].set_color(SPINACH)
        eq[6].set_color(CARROTS)    # maniml indexes MathTex by glyph: S = 4 0 - 4 C
        self.play(Write(eq))
        self.pause()

        # B13b --------------------------------------------------------

        one_across = Line(axes.c2p(4, 24), axes.c2p(5, 24), color=CARROTS, stroke_width=6)
        four_down = Line(axes.c2p(5, 24), axes.c2p(5, 20), color=SPINACH, stroke_width=6)
        one_lab = Tex('$+1$ C').scale(0.6).set_color(CARROTS).next_to(one_across, UP, buff=0.1)
        four_lab = Tex('$-4$ S').scale(0.6).set_color(SPINACH).next_to(four_down, RIGHT, buff=0.1)
        slope_box = SurroundingRectangle(VGroup(eq[4], eq[5]), buff=0.15, color=FOCUS)
        self.play(Create(one_across), FadeIn(one_lab))
        self.play(Create(four_down), FadeIn(four_lab))
        self.play(FadeIn(slope_box))
        self.pause()

        # B13c --------------------------------------------------------

        oc_line = Tex('Opportunity Cost(1 {{$C$}}) = 4 {{$S$}}').scale(0.9).next_to(eq, DOWN, buff=0.4).align_to(eq, LEFT).set_color_by_tex_to_color_map({
            '$C$': CARROTS,
            '$S$': SPINACH,
        })
        self.play(Write(oc_line))
        self.pause()

        # B14 ---------------------------------------------------------

        exercise_card(self, 'Exercise A1 $|$ Q1', [
            'Hagrid can bake 20 rock cakes ($R$) or 30 fruitcakes ($F$) in one day.',
            "Set up Hagrid's PPF with $R$ on the vertical axis and $F$ on the horizontal.",
            'What is his opportunity cost of each good?',
        ])
        self.pause()

        # B20 ---------------------------------------------------------

        FadeAll(self)
        head = title('Attainability')
        axes = style_axes(
            x_range=[0, 17, 1], y_range=[0, 45, 5], x_length=6, y_length=7, ticks=True,
            x_axis_config={'numbers_to_include': np.arange(0, 18, 4),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': CARROTS}},
            y_axis_config={'numbers_to_include': np.arange(10, 50, 10),
                           'decimal_number_config': {'num_decimal_places': 0, 'color': SPINACH}},
        ).shift(RIGHT * 2 + DOWN * 0.2).scale(0.8)

        farm, farm_name = farm_plot()
        VGroup(farm, farm_name).shift(DOWN * 0.4)   # clear the Attainability title
        grow = Rectangle(height=5, width=4, color=MOLLY, fill_opacity=1).next_to(farm_name, DOWN, buff=1 / 2)
        ppf_ghost = axes.plot(PPF_Function, color=MUTED, x_range=(0, 10))
        ppf_graph = axes.plot(PPF_Function, color=MOLLY, x_range=(0, 10))
        ppf_graph.z_index = 1
        self.play(FadeIn(head), FadeIn(axes), FadeIn(farm), FadeIn(farm_name), FadeIn(grow),
                  FadeIn(ppf_ghost), FadeIn(ppf_graph))
        self.pause()

        o = axes.c2p(0, 0)
        c0 = axes.c2p(10, 0)     # original carrot intercept
        s0 = axes.c2p(0, 40)     # original spinach intercept
        c1 = axes.c2p(8, 0)      # after the labor cut
        s1 = axes.c2p(0, 32)
        c2 = axes.c2p(16, 0)     # after the carrot tech
        g = axes.c2p(4, 24)      # where the tech frontier crosses the original

        # B20b --------------------------------------------------------

        attainable = Polygon(o, c0, s0, color=ATTAINABLE, fill_opacity=AREA_OPACITY)
        attainable.z_index = 0
        self.play(FadeIn(attainable))
        self.pause()

        ineff_dot = Dot(axes.c2p(4, 16), color=MUTED, z_index=10)
        ineff_lab = Tex('Inefficient').scale(0.8).set_color(MUTED).next_to(ineff_dot, DOWN, buff=0.15).shift(LEFT * 0.3)
        self.play(FadeIn(ineff_dot), FadeIn(ineff_lab))
        self.pause()

        # B20c --------------------------------------------------------

        eff_dot = Dot(axes.c2p(6, 16), color=EFFICIENT, z_index=10)
        eff_lab = Tex('Efficient').scale(0.8).set_color(EFFICIENT).next_to(eff_dot, UR, buff=0.1)
        self.play(FadeIn(eff_dot), FadeIn(eff_lab))
        self.pause()

        # B20d --------------------------------------------------------

        unatt_dot = Dot(axes.c2p(8, 28), color=GUIDE, z_index=10)
        unatt_lab = Tex('Unattainable').scale(0.8).set_color(GUIDE).next_to(unatt_dot, UP, buff=0.15)
        self.play(FadeIn(unatt_dot))
        self.pause()
        
        self.play(FadeIn(unatt_lab))
        self.pause()

        # B21 ---------------------------------------------------------

        stage, q2 = exercise_card(self, 'Exercise A1 $|$ Q2', [
            'Hagrid wants to bake 30 $R$ and 20 $F$ in one day.',
            'Is this inefficient, efficient, or unattainable?',
            'Justify with a graph or algebra.',
        ])
        self.pause()

        # B22 ---------------------------------------------------------

        trio = VGroup(ineff_dot, ineff_lab, eff_dot, eff_lab, unatt_dot, unatt_lab)
        self.play(FadeOut(q2), Restore(stage))
        self.play(FadeOut(attainable), FadeOut(trio))
        grow_labor = Rectangle(height=5, width=4 * ALPHA, color=MOLLY, fill_opacity=1).next_to(farm_name, DOWN, buff=1 / 2).align_to(farm, LEFT)
        end_c = Dot(c0, color=GUIDE, z_index=10)
        end_s = Dot(s0, color=GUIDE, z_index=10)
        self.play(FadeIn(end_c), FadeIn(end_s))
        labor_cut = Tex('$-$ Labor Cut').rotate(PI / 2).set_color(ON_FILL).scale(0.9).move_to(grow_labor)
        self.play(Transform(grow, grow_labor), FadeIn(labor_cut), end_c.animate.move_to(c1), end_s.animate.move_to(s1))
        self.pause()

        # B22b --------------------------------------------------------

        ppf_labor = axes.plot(PPF_Function_New, color=MOLLY, x_range=(0, 8))
        self.play(Transform(ppf_graph, ppf_labor))
        self.pause()

        # B23 ---------------------------------------------------------

        carrot_tech = Tex('+ Better Carrot Tech').rotate(PI / 2).set_color(ON_FILL).scale(0.9).next_to(labor_cut, LEFT, buff=0.4)
        self.play(FadeIn(carrot_tech))
        self.pause()

        # B23b --------------------------------------------------------

        ppf_tech = axes.plot(PPF_Function_Tech, color=MOLLY, x_range=(0, 16))
        self.play(end_c.animate.move_to(c2))
        self.add(ppf_labor.set_color(MUTED))
        self.play(Transform(ppf_graph, ppf_tech))
        self.play(FadeOut(end_c), FadeOut(end_s))
        self.pause()

        # B24 ---------------------------------------------------------

        lost = Polygon(s1, s0, g, color=LOST, fill_opacity=DWL_OPACITY)
        lost.z_index = 0
        self.play(FadeIn(lost))
        self.pause()
        
        lost_lab = Tex('No longer attainable').scale(0.6).set_color(LOST).next_to(axes.c2p(2.5, 30), RIGHT, buff=0.15)
        self.play(FadeIn(lost_lab))
        self.pause()

        # B24b --------------------------------------------------------

        newly = Polygon(c0, c2, g, color=GAINED, fill_opacity=AREA_OPACITY)
        newly.z_index = 0
        self.play(FadeIn(newly))
        self.pause()
        
        newly_lab = Tex('Newly attainable').scale(0.6).set_color(GAINED).next_to(newly, RIGHT, buff=0.2)
        self.play(FadeIn(newly_lab))
        self.pause()

        # B24c --------------------------------------------------------

        # the sliver lost to the labor cut and regained by the tech — left up
        # as a question for the class
        sliver = Polygon(c0, c1, s1, g, color=FOCUS, fill_opacity=AREA_OPACITY)
        sliver.z_index = 0
        sliver_q = Tex('?').scale(1.2).set_color(FOCUS).move_to(sliver.get_center_of_mass())
        self.play(FadeIn(sliver), FadeIn(sliver_q))
        self.pause()

        # B25 ---------------------------------------------------------

        exercise_card(self, 'Exercise A1 $|$ Q3', [
            'Hagrid cuts his baking time in half.',
            "Then a baking revolution doubles everyone's efficiency.",
            "Show both changes to Hagrid's PPF.",
        ])
        self.pause()

        # B30 ---------------------------------------------------------

        FadeAll(self)
        punch = Tex('We can actually do better.').scale(1.2).set_color(DEFINITION)
        self.play(Write(punch))
        self.pause()

        # B31 ---------------------------------------------------------

        FadeAll(self)
        head = title('Next time...', scale=1.5)
        topic = Tex('A detour into 1800s economic history.').scale(1.2)
        self.add(head, topic)
        framebox_reveal(self, topic)
        FadeAll(self)
