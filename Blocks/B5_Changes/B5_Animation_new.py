# maniml B5_Animation_new.py B5
# B5 | Market Changes. Beat outlines live in B5_Notes_new.typ.
# Read construct top to bottom: the graph is the setting throughout.
# Only the shared bumper and style factories hide construction details.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes


class B5(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP = 2.45
        BODY_BOTTOM = -2.65
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE = 0.7443
        DEFINITION_BOTTOM = 0.05

        # ---- 0.a · The established bumper, with B5's short thesis.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'B', 5)
        thesis = Tex(r'\textit{How prices change.}', color=CAPTION)
        thesis.scale(1.1).next_to(episode, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · Resume the market at the B3/B4 equilibrium.
        # The same line equations and thousand-pound units survive the recap.
        # This is a continuous model; don't import B4's discrete welfare totals.
        head = title('Equilibrium')
        question = Tex(r'\textsf{No one has a reason to change.}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        ax = style_axes([0, 60, 10], [0, 13, 2], x_length=4.6, y_length=4.6)
        ax.shift(np.array([-2.3, -2.25, 0]) - ax.c2p(0, 0))
        axis_p = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 13), LEFT, buff=0.25)
        axis_q = Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.35)
        axes_words = VGroup(axis_p,
            Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5).next_to(axis_p, LEFT, buff=0.12),
            axis_q,
            Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(axis_q, DOWN, buff=0.08))
        demand = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3)
        supply = Line(ax.c2p(0, 2), ax.c2p(60, 5), color=SUPPLY, stroke_width=3)
        curve_words = VGroup(
            Tex('D', color=INK).scale(0.8).next_to(ax.c2p(55, 1), UR, buff=0.1),
            Tex('S', color=INK).scale(0.8).next_to(supply.get_end(), RIGHT, buff=0.15))
        point = Dot(ax.c2p(40, 4), color=GUIDE, radius=0.065, z_index=12)
        p_line = DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        q_line = DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        result_words = VGroup(
            Tex(r'$P^*=4$', color=GUIDE).scale(0.8).next_to(ax.c2p(0, 4), LEFT, buff=0.2),
            Tex(r'$Q^*=40$', color=GUIDE).scale(0.8).next_to(ax.c2p(40, 0), DOWN, buff=0.2))
        bottom = Tex(r'{{Equilibrium}}: quantity demanded equals quantity supplied.',
                     tex_to_color_map={'Equilibrium': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(ax), FadeIn(axes_words), FadeIn(demand), FadeIn(supply), FadeIn(curve_words))
        self.play(FadeIn(p_line), FadeIn(point), FadeIn(q_line), FadeIn(result_words), FadeIn(bottom))
        self.pause('1.a')

        # ---- 1.b · Add welfare to the equilibrium recap.
        self.remove(head)
        head = title('Equilibrium + Welfare')
        self.play(FadeIn(head))
        cs = Polygon(ax.c2p(0, 4), ax.c2p(0, 12), ax.c2p(40, 4),
                     stroke_width=0, fill_color=DEMAND, fill_opacity=AREA_OPACITY)
        ps = Polygon(ax.c2p(0, 2), ax.c2p(0, 4), ax.c2p(40, 4),
                     stroke_width=0, fill_color=SUPPLY, fill_opacity=AREA_OPACITY)
        welfare_words = VGroup(
            Tex('CS', color=DEMAND).scale(0.85).move_to(ax.c2p(12, 6.5)),
            Tex('PS', color=SUPPLY).scale(0.8).move_to(ax.c2p(12, 3.3)))
        self.remove(bottom)
        bottom = Tex(r'{{Total Surplus}} is the sum of the gains for buyers and sellers.',
                     tex_to_color_map={'Total Surplus': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(cs), FadeIn(ps), FadeIn(welfare_words), FadeIn(bottom))
        self.play(cs.animate.set_fill(TOTAL), ps.animate.set_fill(TOTAL), FadeOut(welfare_words))
        total_word = Tex('Total surplus', color=TOTAL).scale(0.65).move_to(ax.c2p(16, 6.5))
        self.play(FadeIn(total_word))
        self.pause('1.b')

        # The later return to equilibrium uses this same square graph.
        recap_market = VGroup(ax, demand, supply, axes_words, curve_words, point,
                              p_line, q_line, result_words).copy()

        # ---- 2.a · Compare two goods, with the question and values present.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        hook_head = title('Responsiveness to Price')
        hook_question = Tex(r'\textsf{Which buyers are hit harder?}', color=CAPTION).scale(0.75)
        hook_question.next_to(hook_head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        hook_price = ValueTracker(4)
        hook_panels, hook_numbers = VGroup(), VGroup()
        hook_buyer_groups, hook_dots, hook_guides = [], [], []
        for panel_x, good, max_q, max_p, coefficient, unit, price_unit, equation_text in [
                (-3.75, 'Spinach', 60, 12, 0.2, r'thousand lb', r'\$/lb', r'P=12-Q/5'),
                (3.75, 'Chocolate', 120, 6, 0.05, r'thousand bars', r'\$/bar', r'P=6-Q/20')]:
            hook_ax = style_axes([0, max_q, max_q / 6], [0, max_p, max_p / 6],
                                 x_length=3.4, y_length=3.4)
            hook_ax.shift(np.array([panel_x - 1.7, -2.1, 0]) - hook_ax.c2p(0, 0))
            hook_curve = Line(hook_ax.c2p(0, max_p), hook_ax.c2p(max_q, 0),
                              color=DEMAND, stroke_width=3, z_index=2)
            hook_bars = VGroup()
            for rank in range(1, max_q):
                mb = max_p - coefficient * rank
                bar = Polygon(hook_ax.c2p(rank - 0.93, 0), hook_ax.c2p(rank - 0.07, 0),
                              hook_ax.c2p(rank - 0.07, mb), hook_ax.c2p(rank - 0.93, mb),
                              stroke_width=0, fill_color=DEMAND if mb >= 4 - 1e-8 else MUTED,
                              fill_opacity=0.5 if mb >= 4 - 1e-8 else 0.14, z_index=-2)
                bar.source, bar.mb = hook_price, mb
                bar.add_updater(lambda m: m.set_fill(
                    DEMAND if m.mb >= m.source.get_value() - 1e-8 else MUTED,
                    opacity=0.5 if m.mb >= m.source.get_value() - 1e-8 else 0.14))
                hook_bars.add(bar)
            hook_dot = Dot(hook_ax.c2p(40, 4), color=GUIDE, radius=0.065, z_index=12)
            hook_dot.ax, hook_dot.source, hook_dot.intercept, hook_dot.coefficient = hook_ax, hook_price, max_p, coefficient
            hook_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
                (m.intercept - m.source.get_value()) / m.coefficient, m.source.get_value())))
            hook_h = DashedLine(hook_ax.c2p(0, 4), hook_ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
            hook_v = DashedLine(hook_ax.c2p(40, 0), hook_ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
            for guide in (hook_h, hook_v):
                guide.ax, guide.source, guide.intercept, guide.coefficient = hook_ax, hook_price, max_p, coefficient
            hook_h.add_updater(lambda m: m.become(DashedLine(
                m.ax.c2p(0, m.source.get_value()),
                m.ax.c2p((m.intercept - m.source.get_value()) / m.coefficient, m.source.get_value()),
                color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
            hook_v.add_updater(lambda m: m.become(DashedLine(
                m.ax.c2p((m.intercept - m.source.get_value()) / m.coefficient, 0),
                m.ax.c2p((m.intercept - m.source.get_value()) / m.coefficient, m.source.get_value()),
                color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
            hook_name = Tex(good, color=INK).scale(0.9).move_to([panel_x, 2.25, 0])
            hook_equation = MathTex(equation_text, color=TITLE).scale(0.8).next_to(hook_name, DOWN, buff=0.16)
            hook_p = Tex('P', color=INK).scale(0.8).next_to(hook_ax.c2p(0, max_p), UP, buff=0.16)
            hook_price_unit = Tex(r'\textsf{' + price_unit + '}', color=CAPTION).scale(0.5).next_to(hook_p, LEFT, buff=0.12)
            hook_q = Tex('Q', color=INK).scale(0.8).next_to(hook_ax.c2p(max_q, 0), RIGHT, buff=0.16)
            hook_unit = Tex(r'\textsf{' + unit + '}', color=CAPTION).scale(0.5).next_to(hook_q, RIGHT, buff=0.12)
            hook_pn = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(0.65)
            hook_pn.ax, hook_pn.source = hook_ax, hook_price
            hook_pn.add_updater(lambda m: m.set_value(m.source.get_value()).next_to(
                m.ax.c2p(0, m.source.get_value()), LEFT, buff=0.2))
            hook_qn = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.65)
            hook_qn.ax, hook_qn.source, hook_qn.intercept, hook_qn.coefficient = hook_ax, hook_price, max_p, coefficient
            hook_qn.add_updater(lambda m: m.set_value((m.intercept - m.source.get_value()) / m.coefficient).next_to(
                m.ax.c2p(m.get_value(), 0), DOWN, buff=0.2 + 0.3 * (m.source.get_value() - 4)))
            hook_pn.update(); hook_qn.update()
            panel = VGroup(hook_ax, hook_curve, hook_bars, hook_h, hook_v, hook_dot,
                           hook_name, hook_p, hook_q, hook_unit, hook_price_unit, hook_equation, hook_pn, hook_qn)
            panel.ax, panel.intercept, panel.coefficient = hook_ax, max_p, coefficient
            hook_panels.add(panel)
            hook_buyer_groups.append(hook_bars)
            hook_dots.append(hook_dot)
            hook_guides.extend([hook_h, hook_v])
            hook_numbers.add(VGroup(
                Tex(str(max_p), color=CAPTION).scale(0.6).next_to(hook_ax.c2p(0, max_p), LEFT, buff=0.2),
                Tex(str(max_q), color=CAPTION).scale(0.6).next_to(hook_ax.c2p(max_q, 0), DOWN, buff=0.2)))
        self.play(FadeIn(hook_head), FadeIn(hook_question), FadeIn(hook_panels), FadeIn(hook_numbers))
        self.pause('2.a')

        # ---- 2.c · Retain the initial coordinates as the live price rises.
        hook_old_choices = VGroup()
        for panel in hook_panels:
            ghost = VGroup(*[panel[i].copy().clear_updaters() for i in (3, 4, 5, 12, 13)])
            ghost.set_color(CAPTION).set_opacity(0.65)
            hook_old_choices.add(ghost)
        self.add(hook_old_choices)
        self.play(hook_price.animate.set_value(5), run_time=2.5, rate_func=smooth)
        self.pause('2.c')

        # ---- 2.d · Horizontal spans measure the quantities forgone.
        hook_changes = VGroup()
        for panel in hook_panels:
            final_q = (panel.intercept - 5) / panel.coefficient
            left_end = panel.ax.c2p(final_q, 0) + DOWN * 0.87
            right_end = panel.ax.c2p(40, 0) + DOWN * 0.87
            hook_changes.add(VGroup(
                Line(left_end, right_end, color=FOCUS, stroke_width=4),
                Line(left_end + DOWN * 0.07, left_end + UP * 0.07, color=FOCUS, stroke_width=2),
                Line(right_end + DOWN * 0.07, right_end + UP * 0.07, color=FOCUS, stroke_width=2)))
        self.play(FadeIn(hook_changes))
        self.pause('2.d')

        # ---- 2.g · Describe responsiveness directly under each comparison.
        hook_classes = VGroup(
            Tex(r'{{Inelastic}}: a relatively small change in quantity.', tex_to_color_map={'Inelastic': DEFINITION})
                .scale(0.62).move_to([-3.75, -3.4, 0]),
            Tex(r'{{Elastic}}: a relatively large change in quantity.', tex_to_color_map={'Elastic': DEFINITION})
                .scale(0.62).move_to([3.75, -3.4, 0]))
        self.play(FadeIn(hook_classes))
        hook_recall = VGroup(hook_head, hook_panels, hook_old_choices, hook_numbers).copy()
        self.pause('2.g')

        # ---- 3.a · Put the slope question in the bottom prompt strip.
        slope_question = Tex('Is it the slope?', color=FOCUS).scale(DEFINITION_SCALE)
        slope_question.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(slope_question))
        self.pause('3.a')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 3.b · Compare two price cuts on two copies of the same curve.
        # The scales and curve are identical; only the selected interval differs.
        self.clear()
        head = title('Price elasticity of demand')
        question = Tex(r'\textsf{Does the same price change mean the same response?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        self.play(FadeIn(head), FadeIn(question))
        elasticity_panels = VGroup()
        elasticity_prices = [ValueTracker(11), ValueTracker(2)]
        for panel_x, price_source in zip([-3.75, 3.75], elasticity_prices):
            ea = style_axes([0, 60, 10], [0, 12, 2], x_length=3.9, y_length=3.9)
            ea.shift(np.array([panel_x, BODY_MID + 0.15, 0])
                     - (ea.c2p(0, 0) + ea.c2p(60, 12)) / 2)
            ed = Line(ea.c2p(0, 12), ea.c2p(60, 0), color=DEMAND, stroke_width=4)
            es = Line(ea.c2p(0, 2), ea.c2p(60, 5), color=SUPPLY, stroke_width=4)
            ep = VGroup(Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5), Tex('P').scale(0.8)).arrange(RIGHT, buff=0.12).next_to(ea.c2p(0, 12), LEFT, buff=0.25)
            eq = Tex('Q').scale(0.8).next_to(ea.c2p(60, 0), DOWN, buff=0.35)
            eu = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5)
            eu.next_to(eq, DOWN, buff=0.08)
            ed_lab = Tex('D').scale(0.8).next_to(ea.c2p(60, 0), RIGHT, buff=0.15)
            equation = MathTex(r'P=12-Q/5', color=INK).scale(0.8)
            equation.move_to(ea.c2p(37, 11))
            eh = DashedLine(ea.c2p(0, price_source.get_value()),
                            ea.c2p(60 - 5 * price_source.get_value(), price_source.get_value()),
                            color=GUIDE, stroke_width=2).set_opacity(0.5)
            eh.ax, eh.source = ea, price_source
            eh.add_updater(lambda line: line.become(DashedLine(
                line.ax.c2p(0, line.source.get_value()),
                line.ax.c2p(60 - 5 * line.source.get_value(), line.source.get_value()),
                color=GUIDE, stroke_width=2).set_style(**line.get_style())))
            ev = DashedLine(ea.c2p(60 - 5 * price_source.get_value(), price_source.get_value()),
                            ea.c2p(60 - 5 * price_source.get_value(), 0),
                            color=GUIDE, stroke_width=2).set_opacity(0.5)
            ev.ax, ev.source = ea, price_source
            ev.add_updater(lambda line: line.become(DashedLine(
                line.ax.c2p(60 - 5 * line.source.get_value(), line.source.get_value()),
                line.ax.c2p(60 - 5 * line.source.get_value(), 0),
                color=GUIDE, stroke_width=2).set_style(**line.get_style())))
            point = Dot(ea.c2p(60 - 5 * price_source.get_value(), price_source.get_value()), color=GUIDE)
            point.ax, point.source = ea, price_source
            point.add_updater(lambda dot: dot.move_to(dot.ax.c2p(
                60 - 5 * dot.source.get_value(), dot.source.get_value())))
            p_number = DecimalNumber(price_source.get_value(), num_decimal_places=0, color=GUIDE).scale(0.7)
            p_number.ax, p_number.source = ea, price_source
            p_number.add_updater(lambda number: number.set_value(number.source.get_value()).next_to(
                number.ax.c2p(0, number.source.get_value()), LEFT, buff=0.25))
            p_number.update()
            q_number = DecimalNumber(60 - 5 * price_source.get_value(), num_decimal_places=0, color=GUIDE).scale(0.7)
            q_number.ax, q_number.source = ea, price_source
            q_number.add_updater(lambda number: number.set_value(60 - 5 * number.source.get_value()).next_to(
                number.ax.c2p(60 - 5 * number.source.get_value(), 0), DOWN, buff=0.25))
            q_number.update()
            panel = VGroup(ea, ed, ep, eq, eu, ed_lab, equation, eh, ev, point, p_number, q_number)
            panel.ax, panel.supply = ea, es
            elasticity_panels.add(panel)
            self.play(FadeIn(panel), FadeIn(es), run_time=0.7)
        self.play(*[FadeOut(panel.supply) for panel in elasticity_panels])
        self.pause('3.b')

        # ---- 3.c · Both cuts are one dollar; both quantities rise by five.
        # Leave a faint dot at each original choice before the live readouts roll.
        initial_choices = VGroup()
        for panel, source in zip(elasticity_panels, elasticity_prices):
            initial_choices.add(Dot(panel.ax.c2p(60 - 5 * source.get_value(), source.get_value()),
                                    color=MUTED, radius=0.06))
        self.add(initial_choices)
        self.play(elasticity_prices[0].animate.set_value(10),
                  elasticity_prices[1].animate.set_value(1), run_time=2, rate_func=smooth)
        changes_left = MathTex(r'\Delta P=-1,\quad\Delta Q=5', color=FOCUS).scale(0.8)
        changes_right = changes_left.copy()
        changes_left.move_to([-3.75, -2.75, 0])
        changes_right.move_to([3.75, -2.75, 0])
        first_observation = MathTex(r'5\longrightarrow10', color=GUIDE).scale(0.8).move_to([-3.75, 2.42, 0])
        second_observation = MathTex(r'50\longrightarrow55', color=GUIDE).scale(0.8).move_to([3.75, 2.42, 0])
        self.play(FadeIn(changes_left), FadeIn(changes_right),
                  FadeIn(first_observation), FadeIn(second_observation))
        self.pause('3.c')

        # ---- 3.d · Name responsiveness before computing it.
        elasticity_def = Tex(r'\mbox{ {{Elasticity}} measures responsiveness in percentage terms.}',
                             tex_to_color_map={'Elasticity': DEFINITION}).scale(DEFINITION_SCALE)
        elasticity_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(elasticity_def))
        self.pause('3.d')

        # ---- 4.a · Measure the quantity change and the midpoint separately.
        # The grey base starts at zero and ends at Q-bar, NOT at the first Q.
        # The short gold change joins the two endpoint quantities. Neither bar
        # is concatenated with the other: the denominator is visibly a midpoint.
        self.clear()
        head = title('Measuring elasticity')
        question = Tex(r'\textsf{How responsive are buyers?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        ea = style_axes([0, 60, 10], [0, 12, 2], x_length=4.3, y_length=4.3)
        ea.shift(np.array([-3.9, BODY_MID, 0]) - (ea.c2p(0, 0) + ea.c2p(60, 12)) / 2)
        ed = Line(ea.c2p(0, 12), ea.c2p(60, 0), color=DEMAND, stroke_width=4)
        ep = VGroup(Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5), Tex('P').scale(0.8)).arrange(RIGHT, buff=0.12).next_to(ea.c2p(0, 12), LEFT, buff=0.25)
        eq = Tex('Q').scale(0.8).next_to(ea.c2p(60, 0), DOWN, buff=0.35)
        eu = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(eq, DOWN, buff=0.08)
        ed_lab = Tex('D').scale(0.8).next_to(ea.c2p(60, 0), RIGHT, buff=0.15)
        equation = MathTex(r'P=12-Q/5').scale(0.8).move_to(ea.c2p(36, 11))
        e_divider = Line([0.2, -2.85, 0], [0.2, 2.55, 0], color=MUTED, stroke_width=1)
        e_divider.set_opacity(0.5)
        midpoint_price = ValueTracker(10.5)
        endpoints = VGroup()
        # sign +1 is the initial, higher price; sign -1 is the final price.
        for sign in [1, -1]:
            endpoint = VGroup()
            h = DashedLine(ea.c2p(0, 10.5 + sign / 2), ea.c2p(7.5 - 2.5 * sign, 10.5 + sign / 2),
                           color=GUIDE, stroke_width=2).set_opacity(0.35)
            h.ax, h.source, h.sign = ea, midpoint_price, sign
            h.add_updater(lambda line: line.become(DashedLine(
                line.ax.c2p(0, line.source.get_value() + line.sign / 2),
                line.ax.c2p(60 - 5 * (line.source.get_value() + line.sign / 2),
                            line.source.get_value() + line.sign / 2),
                color=GUIDE, stroke_width=2).set_style(**line.get_style())))
            v = DashedLine(ea.c2p(7.5 - 2.5 * sign, 10.5 + sign / 2), ea.c2p(7.5 - 2.5 * sign, 0),
                           color=GUIDE, stroke_width=2).set_opacity(0.35)
            v.ax, v.source, v.sign = ea, midpoint_price, sign
            v.add_updater(lambda line: line.become(DashedLine(
                line.ax.c2p(60 - 5 * (line.source.get_value() + line.sign / 2),
                            line.source.get_value() + line.sign / 2),
                line.ax.c2p(60 - 5 * (line.source.get_value() + line.sign / 2), 0),
                color=GUIDE, stroke_width=2).set_style(**line.get_style())))
            point = Dot(ea.c2p(7.5 - 2.5 * sign, 10.5 + sign / 2), color=GUIDE, radius=0.06)
            point.ax, point.source, point.sign = ea, midpoint_price, sign
            point.add_updater(lambda dot: dot.move_to(dot.ax.c2p(
                60 - 5 * (dot.source.get_value() + dot.sign / 2), dot.source.get_value() + dot.sign / 2)))
            pn = DecimalNumber(10.5 + sign / 2, num_decimal_places=1, color=GUIDE).scale(0.7)
            pn.ax, pn.source, pn.sign = ea, midpoint_price, sign
            pn.add_updater(lambda number: number.set_value(number.source.get_value() + number.sign / 2)
                          .next_to(number.ax.c2p(0, number.source.get_value() + number.sign / 2),
                                   LEFT, buff=0.25).shift(UP * number.sign * 0.1))
            pn.update()
            qn = DecimalNumber(7.5 - 2.5 * sign, num_decimal_places=1, color=GUIDE).scale(0.7)
            qn.ax, qn.source, qn.sign = ea, midpoint_price, sign
            qn.add_updater(lambda number: number.set_value(60 - 5 * (number.source.get_value() + number.sign / 2))
                          .next_to(number.ax.c2p(60 - 5 * (number.source.get_value() + number.sign / 2), 0),
                                   DOWN, buff=0.25).shift(LEFT * number.sign * 0.16))
            qn.update()
            endpoint.add(h, v, point, pn, qn)
            endpoints.add(endpoint)
        midpoint_dot = Dot(ea.c2p(7.5, 10.5), color=FOCUS, radius=0.055)
        midpoint_dot.ax, midpoint_dot.source = ea, midpoint_price
        midpoint_dot.add_updater(lambda dot: dot.move_to(dot.ax.c2p(
            60 - 5 * dot.source.get_value(), dot.source.get_value())))
        midpoint_note = Tex('Midpoint', color=DEFINITION).scale(0.7)
        midpoint_note.ax, midpoint_note.source = ea, midpoint_price
        midpoint_note.add_updater(lambda label: label.next_to(label.ax.c2p(
            60 - 5 * label.source.get_value(), label.source.get_value()), UP, buff=0.65))
        midpoint_note.update()
        q_delta = Line(ea.c2p(5, 10), ea.c2p(10, 10), color=FOCUS, stroke_width=6)
        q_delta.ax, q_delta.source = ea, midpoint_price
        q_delta.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(60 - 5 * (line.source.get_value() + 0.5), line.source.get_value() - 0.5),
            line.ax.c2p(60 - 5 * (line.source.get_value() - 0.5), line.source.get_value() - 0.5)))
        q_base = Line(ea.c2p(0, 0), ea.c2p(7.5, 0), color=MUTED, stroke_width=8)
        q_base.ax, q_base.source = ea, midpoint_price
        q_base.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(0, 0), line.ax.c2p(60 - 5 * line.source.get_value(), 0)))
        q_mid_tick = Line(ea.c2p(7.5, -0.16), ea.c2p(7.5, 0.16), color=FOCUS, stroke_width=3)
        q_mid_tick.ax, q_mid_tick.source = ea, midpoint_price
        q_mid_tick.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(60 - 5 * line.source.get_value(), -0.16),
            line.ax.c2p(60 - 5 * line.source.get_value(), 0.16)))
        formula = MathTex(r'\epsilon_D', '=', r'\frac{\Delta Q/\bar Q}{\Delta P/\bar P}').scale(0.95)
        formula.move_to([3.95, 2.0, 0])
        q_change_label = MathTex(r'\Delta Q=5', color=FOCUS).scale(0.8).move_to([2.15, 0.75, 0])
        q_average_label = MathTex(r'\bar Q=7.5', color=FOCUS).scale(0.8).move_to([2.15, 0.0, 0])
        q_change_bar = Line([4.35, 0.75, 0], [4.6, 0.75, 0], color=FOCUS, stroke_width=10)
        q_average_bar = Line([4.35, 0, 0], [4.725, 0, 0], color=MUTED, stroke_width=10)
        q_mid_formula = MathTex(r'\bar Q=\frac{5+10}{2}=7.5').scale(0.8).move_to([3.95, -1.55, 0])
        midpoint_def = Tex(r'\mbox{ {{Midpoint method}} divides each change by the average of its two values.}',
                           tex_to_color_map={'Midpoint method': DEFINITION}).scale(DEFINITION_SCALE)
        midpoint_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(ea), FadeIn(ed), FadeIn(ep), FadeIn(eq), FadeIn(eu),
                  FadeIn(ed_lab), FadeIn(equation), FadeIn(e_divider), FadeIn(endpoints))
        self.play(FadeIn(formula), FadeIn(midpoint_def))
        self.play(FadeIn(q_delta), FadeIn(q_base), FadeIn(q_mid_tick), FadeIn(midpoint_dot), FadeIn(midpoint_note))
        self.play(TransformFromCopy(q_delta.copy().clear_updaters(), q_change_bar), FadeIn(q_change_label),
                  TransformFromCopy(q_base.copy().clear_updaters(), q_average_bar), FadeIn(q_average_label))
        self.play(FadeIn(q_mid_formula))
        self.pause('4.a')

        # ---- 4.b · Repeat the same construction for price, with a negative change.
        p_delta = Line(ea.c2p(5, 11), ea.c2p(5, 10), color=FOCUS, stroke_width=6)
        p_delta.ax, p_delta.source = ea, midpoint_price
        p_delta.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(60 - 5 * (line.source.get_value() + 0.5), line.source.get_value() + 0.5),
            line.ax.c2p(60 - 5 * (line.source.get_value() + 0.5), line.source.get_value() - 0.5)))
        p_base = Line(ea.c2p(0, 0), ea.c2p(0, 10.5), color=MUTED, stroke_width=8)
        p_base.ax, p_base.source = ea, midpoint_price
        p_base.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(0, 0), line.ax.c2p(0, line.source.get_value())))
        p_mid_tick = Line(ea.c2p(-0.8, 10.5), ea.c2p(0.8, 10.5), color=FOCUS, stroke_width=3)
        p_mid_tick.ax, p_mid_tick.source = ea, midpoint_price
        p_mid_tick.add_updater(lambda line: line.put_start_and_end_on(
            line.ax.c2p(-0.8, line.source.get_value()), line.ax.c2p(0.8, line.source.get_value())))
        p_change_label = MathTex(r'\Delta P=-1', color=FOCUS).scale(0.8).move_to([2.15, -0.8, 0])
        p_average_label = MathTex(r'\bar P=10.5', color=FOCUS).scale(0.8).move_to([2.15, -1.55, 0])
        p_change_bar = Line([4.35, -0.8, 0], [4.55, -0.8, 0], color=FOCUS, stroke_width=10)
        p_average_bar = Line([4.35, -1.55, 0], [6.45, -1.55, 0], color=MUTED, stroke_width=10)
        p_mid_formula = MathTex(r'\bar P=\frac{11+10}{2}=10.5').scale(0.8).move_to([3.95, -2.55, 0])
        self.play(FadeOut(q_mid_formula), FadeIn(p_delta), FadeIn(p_base), FadeIn(p_mid_tick))
        self.play(TransformFromCopy(p_delta.copy().clear_updaters(), p_change_bar), FadeIn(p_change_label),
                  TransformFromCopy(p_base.copy().clear_updaters(), p_average_bar), FadeIn(p_average_label))
        self.play(FadeIn(p_mid_formula))
        self.bring_to_front(endpoints, midpoint_dot, q_mid_tick, p_mid_tick)
        self.pause('4.b')

        # ---- 4.c · Normalize the measurements before comparing their lengths.
        # A full grey bar is now 100% for BOTH rows. Gold shows the change as
        # a share of its midpoint. Raw pounds and dollars are never compared.
        self.play(FadeOut(p_mid_formula), FadeOut(q_change_label), FadeOut(q_average_label),
                  FadeOut(p_change_label), FadeOut(p_average_label))
        q_ratio_track = Line([3.1, 0.85, 0], [6.1, 0.85, 0], color=MUTED, stroke_width=10)
        p_ratio_track = Line([3.1, -0.45, 0], [6.1, -0.45, 0], color=MUTED, stroke_width=10)
        q_ratio_bar = Line([3.1, 0.85, 0], [5.1, 0.85, 0], color=FOCUS, stroke_width=10)
        q_ratio_bar.source = midpoint_price
        q_ratio_bar.add_updater(lambda line: line.put_start_and_end_on(
            np.array([3.1, 0.85, 0]), np.array([3.1 + 3 * 5 / (60 - 5 * line.source.get_value()), 0.85, 0])))
        p_ratio_bar = Line([3.1, -0.45, 0], [3.1 + 3 / 10.5, -0.45, 0], color=FOCUS, stroke_width=10)
        p_ratio_bar.source = midpoint_price
        p_ratio_bar.add_updater(lambda line: line.put_start_and_end_on(
            np.array([3.1, -0.45, 0]), np.array([3.1 + 3 / line.source.get_value(), -0.45, 0])))
        percent_basis = Tex(r'$100\%$', color=CAPTION).scale(0.7).move_to([6.65, 0.2, 0])
        q_ratio_label = MathTex(r'\frac{\Delta Q}{\bar Q}=\frac{5}{7.5}', color=FOCUS).scale(0.75)
        q_ratio_label.move_to([1.8, 0.85, 0])
        p_ratio_label = MathTex(r'\frac{\Delta P}{\bar P}=\frac{-1}{10.5}', color=FOCUS).scale(0.75)
        p_ratio_label.move_to([1.8, -0.45, 0])
        self.play(ReplacementTransform(q_average_bar, q_ratio_track), ReplacementTransform(p_average_bar, p_ratio_track),
                  ReplacementTransform(q_change_bar, q_ratio_bar), ReplacementTransform(p_change_bar, p_ratio_bar),
                  FadeIn(q_ratio_label), FadeIn(p_ratio_label), FadeIn(percent_basis))
        q_percent = VGroup(DecimalNumber(100 * 5 / 7.5, num_decimal_places=1, color=FOCUS),
                           MathTex(r'\%', color=FOCUS)).arrange(RIGHT, buff=0.04).scale(0.8)
        q_percent.move_to([4.6, 1.2, 0])
        q_percent[0].source = midpoint_price
        q_percent[0].add_updater(lambda number: number.set_value(100 * 5 / (60 - 5 * number.source.get_value())))
        q_percent.add_updater(lambda group: group.arrange(RIGHT, buff=0.04).move_to([4.6, 1.2, 0]))
        p_percent = VGroup(DecimalNumber(-100 / 10.5, num_decimal_places=1, color=FOCUS),
                           MathTex(r'\%', color=FOCUS)).arrange(RIGHT, buff=0.04).scale(0.8)
        p_percent.move_to([4.6, -0.1, 0])
        p_percent[0].source = midpoint_price
        p_percent[0].add_updater(lambda number: number.set_value(-100 / number.source.get_value()))
        p_percent.add_updater(lambda group: group.arrange(RIGHT, buff=0.04).move_to([4.6, -0.1, 0]))
        self.play(FadeIn(q_percent), FadeIn(p_percent))
        self.pause('4.c')

        # ---- 4.d · Divide the two percentages; preserve the demand sign.
        epsilon_prefix = MathTex(r'\epsilon_D=').scale(1.1)
        epsilon_number = DecimalNumber(-7, num_decimal_places=2, color=FOCUS).scale(1.1)
        epsilon_result = VGroup(epsilon_prefix, epsilon_number).arrange(RIGHT, buff=0.18)
        epsilon_result.move_to([3.95, -1.75, 0])
        epsilon_number.source = midpoint_price
        epsilon_number.add_updater(lambda number: number.set_value(
            -number.source.get_value() / (12 - number.source.get_value())))
        epsilon_result.add_updater(lambda group: group.arrange(RIGHT, buff=0.18).move_to([3.95, -1.75, 0]))
        elastic_word = Tex(r'Elastic: $|\epsilon_D|>1$', color=DEFINITION).scale(0.8).move_to([3.95, -2.55, 0])
        self.remove(midpoint_def)
        demand_sign_note = Tex('The sign gives direction; the magnitude measures responsiveness.', color=INK).scale(DEFINITION_SCALE)
        demand_sign_note.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(epsilon_result), FadeIn(elastic_word), FadeIn(demand_sign_note))
        self.pause('4.d')

        # ---- 4.e · Slide the SAME dollar-wide interval to the low-price example.
        # Remove the first example's literal fractions before the values roll.
        # The normalized bar lengths, percentages, guides and final result all
        # follow midpoint_price, so they cannot drift apart during the motion.
        self.remove(q_ratio_label, p_ratio_label, midpoint_note, elastic_word)
        q_ratio_label = MathTex(r'\Delta Q/\bar Q', color=FOCUS).scale(0.8).move_to([1.7, 0.85, 0])
        p_ratio_label = MathTex(r'\Delta P/\bar P', color=FOCUS).scale(0.8).move_to([1.7, -0.45, 0])
        self.play(FadeIn(q_ratio_label), FadeIn(p_ratio_label))
        self.play(midpoint_price.animate.set_value(1.5), run_time=3, rate_func=smooth)
        inelastic_word = Tex(r'Inelastic: $|\epsilon_D|=1/7<1$', color=DEFINITION).scale(0.8).move_to([3.95, -2.55, 0])
        self.play(FadeIn(inelastic_word))
        self.pause('4.e')

        # ---- 4.f · Return to the two goods with their measured elasticities.
        # Keep the measurement scene intact for the subsequent unit-elastic sweep.
        measurement_scene = list(self.mobjects)
        self.clear()
        hook_epsilon = VGroup(
            MathTex(r'\epsilon=-0.6', color=FOCUS).scale(0.95).move_to([-3.85, -3.1, 0]),
            MathTex(r'\epsilon=-3', color=FOCUS).scale(0.95).move_to([3.85, -3.1, 0]))
        self.play(FadeIn(hook_recall), FadeIn(hook_epsilon))
        self.pause('4.f')
        self.play(FadeOut(hook_recall), FadeOut(hook_epsilon))
        self.clear()
        self.add(*measurement_scene)

        # ---- 4.g · Sweep the fixed line and stop exactly at unit elasticity.
        # Its slope never changes. The interval remains symmetric about P-bar,
        # so at P-bar=6 and Q-bar=30 the midpoint elasticity is exactly -1.
        self.remove(inelastic_word, demand_sign_note)
        responsiveness_def = Tex(r'\mbox{ {{Unit elastic}}: quantity and price change by equal percentages in magnitude.}',
                                  tex_to_color_map={'Unit elastic': DEFINITION}).scale(DEFINITION_SCALE)
        responsiveness_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(midpoint_price.animate.set_value(10.5), run_time=3, rate_func=smooth)
        self.play(midpoint_price.animate.set_value(6), run_time=2.5, rate_func=smooth)
        unit_word = Tex(r'Unit elastic: $|\epsilon_D|=1$', color=DEFINITION).scale(0.8).move_to([3.95, -2.55, 0])
        self.play(FadeIn(unit_word), FadeIn(responsiveness_def))
        self.pause('4.g')

        # ---- 4.h · Label the regions without giving demand a second palette.
        # Both segments keep DEMAND. Neutral braces mark their spans; only the
        # terminology uses definition gold. Keep the unit midpoint visible.
        self.play(FadeOut(q_ratio_track), FadeOut(p_ratio_track), FadeOut(q_ratio_bar), FadeOut(p_ratio_bar),
                  FadeOut(q_ratio_label), FadeOut(p_ratio_label), FadeOut(q_percent), FadeOut(p_percent),
                  FadeOut(percent_basis), FadeOut(epsilon_result), FadeOut(formula), FadeOut(unit_word),
                  FadeOut(e_divider), FadeOut(q_delta), FadeOut(p_delta), FadeOut(q_base), FadeOut(p_base),
                  FadeOut(q_mid_tick), FadeOut(p_mid_tick), FadeOut(endpoints))
        upper_demand = Line(ea.c2p(0, 12), ea.c2p(30, 6), color=DEMAND, stroke_width=7)
        lower_demand = Line(ea.c2p(30, 6), ea.c2p(60, 0), color=DEMAND, stroke_width=7)
        upper_brace = Brace(upper_demand, direction=UR, color=MUTED, buff=0.15)
        lower_brace = Brace(lower_demand, direction=UR, color=MUTED, buff=0.15)
        elastic_region = VGroup(Tex('Elastic', color=DEFINITION), MathTex(r'|\epsilon_D|>1'))
        elastic_region.arrange(RIGHT, buff=0.3).scale(0.9).move_to([3.6, 1.5, 0])
        unit_region = VGroup(Tex('Unit elastic', color=DEFINITION), MathTex(r'|\epsilon_D|=1'))
        unit_region.arrange(RIGHT, buff=0.3).scale(0.9).move_to([3.6, 0.0, 0])
        inelastic_region = VGroup(Tex('Inelastic', color=DEFINITION), MathTex(r'|\epsilon_D|<1'))
        inelastic_region.arrange(RIGHT, buff=0.3).scale(0.9).move_to([3.6, -1.5, 0])
        slope_note = MathTex(r'\text{Slope}=-1/5', color=CAPTION).scale(0.8).move_to([3.6, -2.55, 0])
        self.remove(responsiveness_def)
        self.play(FadeIn(upper_demand), FadeIn(upper_brace), FadeIn(elastic_region))
        self.play(FadeIn(lower_demand), FadeIn(lower_brace), FadeIn(inelastic_region))
        unit_guides = VGroup(
            DashedLine(ea.c2p(0, 6), ea.c2p(30, 6), color=MUTED),
            DashedLine(ea.c2p(30, 0), ea.c2p(30, 6), color=MUTED))
        unit_coordinates = VGroup(
            Tex('6', color=GUIDE).scale(0.7).next_to(ea.c2p(0, 6), LEFT, buff=0.25),
            Tex('30', color=GUIDE).scale(0.7).next_to(ea.c2p(30, 0), DOWN, buff=0.25))
        self.play(FadeIn(unit_region), FadeIn(slope_note), FadeIn(unit_guides), FadeIn(unit_coordinates))
        self.bring_to_front(midpoint_dot)
        hook_baseline_dot = Dot(ea.c2p(40, 4), color=GUIDE, radius=0.07, z_index=12)
        hook_baseline_guides = VGroup(
            DashedLine(ea.c2p(0, 4), ea.c2p(40, 4), color=GUIDE, stroke_width=2),
            DashedLine(ea.c2p(40, 0), ea.c2p(40, 4), color=GUIDE, stroke_width=2))
        hook_baseline_coordinates = VGroup(
            Tex('4', color=GUIDE).scale(0.7).next_to(ea.c2p(0, 4), LEFT, buff=0.25),
            Tex('40', color=GUIDE).scale(0.7).next_to(ea.c2p(40, 0), DOWN, buff=0.25))
        self.play(FadeIn(hook_baseline_dot), FadeIn(hook_baseline_guides), FadeIn(hook_baseline_coordinates))
        self.pause('4.h')

        # ---- 5.a · At one extreme, quantity does not respond at all.
        self.clear()
        head = title('The extremes of elasticity')
        question = Tex(r'\textsf{How far can responsiveness go?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        ea = style_axes([0, 2, 1], [0, 12, 2], x_length=3.6, y_length=3.6)
        ea.shift(np.array([-3.7, BODY_MID, 0]) - (ea.c2p(0, 0) + ea.c2p(2, 12)) / 2)
        ep = VGroup(Tex(r'\textsf{\$/pack}', color=CAPTION).scale(0.5), Tex('P').scale(0.8)).arrange(RIGHT, buff=0.12).next_to(ea.c2p(0, 12), LEFT, buff=0.25)
        eq = VGroup(Tex('Q').scale(0.8), Tex(r'\textsf{packs/year}', color=CAPTION).scale(0.5)).arrange(DOWN, buff=0.08).next_to(ea.c2p(2, 0), DOWN, buff=0.35)
        vertical_demand = Line(ea.c2p(1, 0), ea.c2p(1, 12), color=DEMAND, stroke_width=4)
        vertical_label = Tex('D').scale(0.8).next_to(vertical_demand, RIGHT, buff=0.15).align_to(vertical_demand, UP)
        extreme_price = ValueTracker(9)
        extreme_dot = Dot(ea.c2p(1, 9), color=GUIDE)
        extreme_dot.ax, extreme_dot.source = ea, extreme_price
        extreme_dot.add_updater(lambda dot: dot.move_to(dot.ax.c2p(1, dot.source.get_value())))
        extreme_h = DashedLine(ea.c2p(0, 9), ea.c2p(1, 9), color=GUIDE).set_opacity(0.4)
        extreme_h.ax, extreme_h.source = ea, extreme_price
        extreme_h.add_updater(lambda line: line.become(DashedLine(line.ax.c2p(0, line.source.get_value()),
            line.ax.c2p(1, line.source.get_value()), color=GUIDE).set_style(**line.get_style())))
        zero_response = VGroup(Tex('Perfectly inelastic', color=DEFINITION), MathTex(r'\epsilon_D=0'))
        zero_response.arrange(DOWN, buff=0.2).scale(0.85).move_to([-3.7, -3.0, 0])
        self.play(FadeIn(head), FadeIn(question), FadeIn(ea), FadeIn(ep), FadeIn(eq), FadeIn(vertical_demand),
                  FadeIn(vertical_label), FadeIn(extreme_dot), FadeIn(extreme_h))
        self.play(extreme_price.animate.set_value(3), run_time=2, rate_func=smooth)
        extreme_note = Tex('Price changes; quantity stays fixed.', color=INK).scale(DEFINITION_SCALE)
        extreme_note.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(zero_response), FadeIn(extreme_note))
        gary_extreme_name = Tex(r"Gary's EpiPen", color=INK).scale(0.9).move_to([-3.7, 2.32, 0])
        gary_fixed_quantity = Tex('1', color=GUIDE).scale(0.7).next_to(ea.c2p(1, 0), DOWN, buff=0.25)
        self.play(FadeIn(gary_extreme_name), FadeIn(gary_fixed_quantity))
        self.pause('5.a')

        # ---- 5.b · At the other extreme, the curve is horizontal.
        right_ax = style_axes([0, 60, 10], [0, 12, 2], x_length=3.6, y_length=3.6)
        right_ax.shift(np.array([3.7, BODY_MID, 0]) - (right_ax.c2p(0, 0) + right_ax.c2p(60, 12)) / 2)
        right_p = VGroup(Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5), Tex('P').scale(0.8)).arrange(RIGHT, buff=0.12).next_to(right_ax.c2p(0, 12), LEFT, buff=0.25)
        right_q = VGroup(Tex('Q').scale(0.8), Tex(r'\textsf{lb}', color=CAPTION).scale(0.5)).arrange(DOWN, buff=0.08).next_to(right_ax.c2p(60, 0), DOWN, buff=0.35)
        horizontal_demand = Line(right_ax.c2p(0, 4), right_ax.c2p(60, 4), color=DEMAND, stroke_width=4)
        horizontal_label = Tex('D').scale(0.8).next_to(horizontal_demand, RIGHT, buff=0.15)
        extreme_quantity = ValueTracker(10)
        horizontal_dot = Dot(right_ax.c2p(10, 4), color=GUIDE)
        horizontal_dot.ax, horizontal_dot.source = right_ax, extreme_quantity
        horizontal_dot.add_updater(lambda dot: dot.move_to(dot.ax.c2p(dot.source.get_value(), 4)))
        horizontal_v = DashedLine(right_ax.c2p(10, 4), right_ax.c2p(10, 0), color=GUIDE).set_opacity(0.4)
        horizontal_v.ax, horizontal_v.source = right_ax, extreme_quantity
        horizontal_v.add_updater(lambda line: line.become(DashedLine(line.ax.c2p(line.source.get_value(), 4),
            line.ax.c2p(line.source.get_value(), 0), color=GUIDE).set_style(**line.get_style())))
        infinite_response = VGroup(Tex('Perfectly elastic', color=DEFINITION), MathTex(r'|\epsilon_D|\to\infty'))
        infinite_response.arrange(DOWN, buff=0.2).scale(0.85).move_to([3.7, -3.0, 0])
        self.play(FadeIn(right_ax), FadeIn(right_p), FadeIn(right_q), FadeIn(horizontal_demand),
                  FadeIn(horizontal_label), FadeIn(horizontal_dot), FadeIn(horizontal_v))
        self.play(extreme_quantity.animate.set_value(50), run_time=2, rate_func=smooth)
        self.remove(extreme_note)
        extreme_note = Tex('Quantity can change at the same price.', color=INK).scale(DEFINITION_SCALE)
        extreme_note.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(infinite_response), FadeIn(extreme_note))
        andrew_extreme_name = Tex(r"Andrew's spinach", color=INK).scale(0.9).move_to([3.7, 2.32, 0])
        andrew_market_price = Tex('4', color=GUIDE).scale(0.7).next_to(right_ax.c2p(0, 4), LEFT, buff=0.25)
        self.play(FadeIn(andrew_extreme_name), FadeIn(andrew_market_price))
        # At the market price quantity may vary; above it Andrew loses his buyers.
        andrew_ask = ValueTracker(4)
        andrew_no_buyers = Dot(right_ax.c2p(0, 4), color=GUIDE, radius=0.065)
        andrew_no_buyers.ax, andrew_no_buyers.source = right_ax, andrew_ask
        andrew_no_buyers.add_updater(lambda m: m.move_to(m.ax.c2p(0, m.source.get_value())))
        andrew_ask_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        andrew_ask_number.ax, andrew_ask_number.source = right_ax, andrew_ask
        andrew_ask_number.add_updater(lambda m: m.set_value(m.source.get_value()).next_to(
            m.ax.c2p(0, m.source.get_value()), LEFT, buff=0.25))
        self.play(extreme_quantity.animate.set_value(0), run_time=1.2)
        self.remove(horizontal_dot, horizontal_v, andrew_market_price)
        self.add(andrew_no_buyers, andrew_ask_number)
        andrew_zero = Tex('0', color=GUIDE).scale(0.7).next_to(right_ax.c2p(0, 0), DOWN, buff=0.25)
        self.add(andrew_zero)
        self.play(andrew_ask.animate.set_value(4.25), run_time=1.2)
        self.wait(1)
        self.play(andrew_ask.animate.set_value(4), run_time=1.2)
        self.remove(andrew_no_buyers, andrew_ask_number, andrew_zero)
        self.add(horizontal_dot, horizontal_v, andrew_market_price)
        self.play(extreme_quantity.animate.set_value(50), run_time=1.2)
        self.pause('5.b')

        # ---- 6.a · Apply the same percentage ratio to the familiar supply curve.
        # A rise from P=4 to P=5 moves Q_s from 40 to 60. The midpoint method
        # yields (20/50)/(1/4.5)=1.8; price and quantity move together.
        self.clear()
        head = title('Price elasticity of supply')
        question = Tex(r'\textsf{How responsive are sellers?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        sa = style_axes([0, 80, 20], [0, 8, 2], x_length=4.3, y_length=4.3)
        sa.shift(np.array([-3.9, BODY_MID, 0]) - (sa.c2p(0, 0) + sa.c2p(80, 8)) / 2)
        supply = Line(sa.c2p(0, 2), sa.c2p(80, 6), color=SUPPLY, stroke_width=4)
        sp = VGroup(Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5), Tex('P').scale(0.8)).arrange(RIGHT, buff=0.12).next_to(sa.c2p(0, 8), LEFT, buff=0.25)
        sq = Tex('Q').scale(0.8).next_to(sa.c2p(80, 0), DOWN, buff=0.35)
        su = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(sq, DOWN, buff=0.12)
        supply_label = Tex('S').scale(0.8).next_to(sa.c2p(80, 6), RIGHT, buff=0.15)
        supply_equation = MathTex(r'P=2+Q_s/20').scale(0.8).move_to(sa.c2p(39, 7.3))
        supply_price = ValueTracker(4)
        supply_h = DashedLine(sa.c2p(0, 4), sa.c2p(40, 4), color=GUIDE).set_opacity(0.4)
        supply_h.ax, supply_h.source = sa, supply_price
        supply_h.add_updater(lambda line: line.become(DashedLine(
            line.ax.c2p(0, line.source.get_value()), line.ax.c2p(20 * (line.source.get_value() - 2), line.source.get_value()),
            color=GUIDE).set_style(**line.get_style())))
        supply_v = DashedLine(sa.c2p(40, 4), sa.c2p(40, 0), color=GUIDE).set_opacity(0.4)
        supply_v.ax, supply_v.source = sa, supply_price
        supply_v.add_updater(lambda line: line.become(DashedLine(
            line.ax.c2p(20 * (line.source.get_value() - 2), line.source.get_value()),
            line.ax.c2p(20 * (line.source.get_value() - 2), 0), color=GUIDE).set_style(**line.get_style())))
        supply_dot = Dot(sa.c2p(40, 4), color=GUIDE)
        supply_dot.ax, supply_dot.source = sa, supply_price
        supply_dot.add_updater(lambda dot: dot.move_to(dot.ax.c2p(
            20 * (dot.source.get_value() - 2), dot.source.get_value())))
        supply_pn = DecimalNumber(4, num_decimal_places=1, color=GUIDE).scale(0.7)
        supply_pn.ax, supply_pn.source = sa, supply_price
        supply_pn.add_updater(lambda number: number.set_value(number.source.get_value()).next_to(
            number.ax.c2p(0, number.source.get_value()), LEFT, buff=0.25))
        supply_pn.update()
        supply_qn = VGroup(MathTex(r'Q_s=', color=GUIDE), DecimalNumber(40, num_decimal_places=0, color=GUIDE))
        supply_qn.arrange(RIGHT, buff=0.05).scale(0.7)
        supply_qn.ax, supply_qn.source = sa, supply_price
        supply_qn[1].source = supply_price
        supply_qn[1].add_updater(lambda number: number.set_value(20 * (number.source.get_value() - 2)))
        supply_qn.add_updater(lambda group: group.arrange(RIGHT, buff=0.05).next_to(
            group.ax.c2p(20 * (group.source.get_value() - 2), 0), DOWN, buff=0.3))
        supply_qn.update()
        supply_def = Tex(r'\mbox{ {{Elasticity of supply}} measures how quantity supplied responds to price.}',
                        tex_to_color_map={'Elasticity of supply': DEFINITION}).scale(DEFINITION_SCALE)
        supply_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(sa), FadeIn(supply), FadeIn(sp), FadeIn(sq), FadeIn(su),
                  FadeIn(supply_label), FadeIn(supply_equation), FadeIn(supply_h), FadeIn(supply_v),
                  FadeIn(supply_dot), FadeIn(supply_pn), FadeIn(supply_qn), FadeIn(supply_def))
        seller_bars = VGroup()
        for rank in range(1, 81):
            mc = 2 + rank / 20
            bar = Polygon(sa.c2p(rank - 0.93, 0), sa.c2p(rank - 0.07, 0),
                          sa.c2p(rank - 0.07, mc), sa.c2p(rank - 0.93, mc),
                          stroke_width=0, fill_color=SUPPLY if rank <= 40 else MUTED,
                          fill_opacity=0.5 if rank <= 40 else 0.14, z_index=-2)
            bar.source, bar.mc = supply_price, mc
            bar.add_updater(lambda m: m.set_fill(
                SUPPLY if m.mc <= m.source.get_value() + 1e-8 else MUTED,
                opacity=0.5 if m.mc <= m.source.get_value() + 1e-8 else 0.14))
            seller_bars.add(bar)
        self.play(FadeIn(seller_bars))
        self.pause('6.a')

        # ---- 6.b · Twenty additional sellers can cover their costs at $5.
        original_supply_point = Dot(sa.c2p(40, 4), color=MUTED, radius=0.06)
        self.add(original_supply_point)
        self.play(supply_price.animate.set_value(5), run_time=2, rate_func=smooth)
        seller_entry = Tex('20 more sellers', color=INK).scale(0.85).move_to([-3.9, -3.25, 0])
        self.play(FadeIn(seller_entry))
        self.pause('6.b')

        # ---- 6.c · Quantity's percentage response is positive and larger.
        supply_divider = Line([0.2, -2.85, 0], [0.2, 2.55, 0], color=MUTED, stroke_width=1).set_opacity(0.5)
        supply_formula = MathTex(r'\epsilon_S=\frac{\Delta Q_s/\bar Q_s}{\Delta P/\bar P}').scale(0.95)
        supply_substitution = MathTex(r'=\frac{(60-40)/50}{(5-4)/4.5}', color=FOCUS).scale(0.95)
        supply_result = MathTex(r'=\frac{40\%}{22.2\%}\approx1.8', color=FOCUS).scale(0.95)
        supply_work = VGroup(supply_formula, supply_substitution, supply_result)
        supply_work.arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to([3.9, BODY_MID + 0.3, 0])
        supply_elastic = Tex('Elastic supply', color=DEFINITION).scale(0.9).move_to([3.9, -2.2, 0])
        self.play(FadeIn(supply_divider), FadeIn(supply_formula))
        self.play(FadeIn(supply_substitution))
        self.play(FadeIn(supply_result), FadeIn(supply_elastic))
        self.pause('6.c')


        # ---- 7.a · Return to the same market before changing the curves.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        curve_question = Tex(r'\textsf{What if the curves move instead?}', color=CAPTION).scale(0.9)
        curve_question.to_edge(UP, buff=0.75)
        self.play(FadeIn(recap_market), FadeIn(curve_question))
        self.pause('7.a')
        self.play(FadeOut(recap_market), FadeOut(curve_question))
        self.clear()

        # ---- 7.b · Gary is a selected willingness-to-pay bar on the graph.
        # Selecting Q=30 gives MB=$6 in the market ordering. His bar is a
        # representative marginal lot, not an individual demand schedule.
        head = title('A change in preferences')
        question = Tex(r'\textsf{What if spinach is healthier than we thought?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        ax = style_axes([0, 90, 20], [0, 18, 4], x_length=4.6, y_length=4.6)
        ax.shift(np.array([-6.25, -2.25, 0]) - ax.c2p(0, 0))
        axis_p = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 18), LEFT, buff=0.25)
        axis_q = Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(90, 0), DOWN, buff=0.35)
        axes_words = VGroup(axis_p,
            Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5).next_to(axis_p, LEFT, buff=0.12),
            axis_q,
            Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(axis_q, DOWN, buff=0.08))
        demand = Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3)
        supply = Line(ax.c2p(0, 2), ax.c2p(90, 6.5), color=SUPPLY, stroke_width=3).set_opacity(0.3)
        demand_word = Tex('D', color=INK).scale(0.8).next_to(ax.c2p(60, 0), UR, buff=0.18)
        supply_word = Tex('S', color=CAPTION).scale(0.8).next_to(supply.get_end(), RIGHT, buff=0.15)
        selected_bar = Line(ax.c2p(30, 0), ax.c2p(30, 6), color=DEMAND, stroke_width=10)
        selected_word = Tex(r"Gary's next unit", color=INK).scale(0.8).next_to(selected_bar.get_end(), UR, buff=0.2)
        self.play(FadeIn(head), FadeIn(question), FadeIn(ax), FadeIn(axes_words), FadeIn(demand), FadeIn(supply),
                  FadeIn(demand_word), FadeIn(supply_word))
        self.play(FadeIn(selected_bar), FadeIn(selected_word))
        self.pause('7.b')

        # ---- 7.c · Bring that one bar forward; raise willingness to pay only.
        # The axes and supply stay still. The market-wide shift comes in 8.b.
        benefit = ValueTracker(6)
        gary_base = np.array([4.0, -1.8, 0])
        gary_bar = Line(gary_base, gary_base + UP * 2.0, color=DEMAND, stroke_width=20)
        gary_bar.base, gary_bar.benefit = gary_base, benefit
        gary_bar.add_updater(lambda m: m.put_start_and_end_on(m.base, m.base + UP * m.benefit.get_value() / 3))
        gary_name = Tex(r"Gary's next unit", color=INK).scale(0.8).next_to(gary_base, DOWN, buff=0.35)
        gary_number = DecimalNumber(6, num_decimal_places=0, color=GUIDE).scale(0.9)
        gary_number.bar, gary_number.benefit = gary_bar, benefit
        gary_number.add_updater(lambda m: m.set_value(m.benefit.get_value()).next_to(m.bar.get_end(), RIGHT, buff=0.3))
        gary_units = Tex(r'MB (\$/lb)', color=CAPTION).scale(0.7).move_to([4.4, 2.25, 0])
        old_top = DashedLine([3.4, 0.2, 0], [4.7, 0.2, 0], color=MUTED)
        old_six = Tex('6', color=CAPTION).scale(0.7).next_to(old_top, LEFT, buff=0.15)
        bottom = Tex('New information raises willingness to pay.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(TransformFromCopy(selected_bar, gary_bar), FadeIn(gary_name), FadeIn(gary_number), FadeIn(gary_units))
        self.play(FadeIn(old_top), FadeIn(old_six), FadeIn(bottom))
        self.play(benefit.animate.set_value(11), run_time=2)
        self.pause('7.c')
        gary_bar.clear_updaters()
        gary_number.clear_updaters()
        self.play(FadeOut(gary_bar), FadeOut(gary_name), FadeOut(gary_number), FadeOut(gary_units),
                  FadeOut(old_top), FadeOut(old_six), FadeOut(selected_bar), FadeOut(selected_word),
                  FadeOut(supply), FadeOut(supply_word), FadeOut(bottom))

        # ---- 8.a · Own price changes the selected point, never the curve.
        self.remove(head, question)
        head = title('Demand: movement and shift')
        question = Tex(r'\textsf{Did demand change, or did the price change?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        price = ValueTracker(4)
        shift = ValueTracker(0)
        demand_slope = ValueTracker(0.2)
        demand.ax, demand.shift_value, demand.slope = ax, shift, demand_slope
        demand.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.shift_value.get_value()),
            m.ax.c2p((12 + m.shift_value.get_value()) / m.slope.get_value(), 0)))
        demand_word.curve = demand
        demand_word.add_updater(lambda m: m.next_to(m.curve.get_end(), UR, buff=0.18))
        point = Dot(ax.c2p(40, 4), color=GUIDE, radius=0.065, z_index=12)
        point.ax, point.price, point.shift_value = ax, price, shift
        point.slope = demand_slope
        point.add_updater(lambda m: m.move_to(m.ax.c2p(
            (12 + m.shift_value.get_value() - m.price.get_value()) / m.slope.get_value(), m.price.get_value())))
        p_line = DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        p_line.ax, p_line.price, p_line.shift_value = ax, price, shift
        p_line.slope = demand_slope
        p_line.add_updater(lambda m: m.become(DashedLine(m.ax.c2p(0, m.price.get_value()),
            m.ax.c2p((12 + m.shift_value.get_value() - m.price.get_value()) / m.slope.get_value(), m.price.get_value()), color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
        q_line = DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        q_line.ax, q_line.price, q_line.shift_value = ax, price, shift
        q_line.slope = demand_slope
        q_line.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p((12 + m.shift_value.get_value() - m.price.get_value()) / m.slope.get_value(), 0),
            m.ax.c2p((12 + m.shift_value.get_value() - m.price.get_value()) / m.slope.get_value(), m.price.get_value()), color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
        p_number = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(0.8)
        p_number.ax, p_number.price = ax, price
        p_number.add_updater(lambda m: m.set_value(m.price.get_value()).next_to(m.ax.c2p(0, m.price.get_value()), LEFT, buff=0.2))
        q_number = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.8)
        q_number.ax, q_number.price, q_number.shift_value = ax, price, shift
        q_number.slope = demand_slope
        q_number.add_updater(lambda m: m.set_value((12 + m.shift_value.get_value() - m.price.get_value()) / m.slope.get_value())
            .next_to(m.ax.c2p(m.get_value(), 0), DOWN, buff=0.2))
        q_prefix = Tex('$Q_d=$', color=GUIDE).scale(0.8)
        q_prefix.number = q_number
        q_prefix.add_updater(lambda m: m.next_to(m.number, LEFT, buff=0.08))
        bottom = Tex(r'A change in {{quantity demanded}} moves along the curve.',
                     tex_to_color_map={'quantity demanded': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(p_line), FadeIn(point), FadeIn(p_number))
        self.play(FadeIn(q_line), FadeIn(q_number), FadeIn(q_prefix), FadeIn(bottom))
        # The parameter is present before the first market shift. Its gold
        # span measures vertical displacement from the original intercept 12.
        demand_equation = MathTex(r'P=12+', 'a', r'-Q/5',
                                  tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'a': DEFINITION}).scale(0.85)
        demand_equation.move_to([4.35, 2.0, 0])
        a_number = DecimalNumber(0, num_decimal_places=0, include_sign=True, color=DEFINITION).scale(0.8)
        a_number.source = shift
        a_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        a_readout = VGroup(MathTex('a=', color=DEFINITION).scale(0.8), a_number)
        a_readout.arrange(RIGHT, buff=0.1).move_to([4.35, 1.35, 0])
        a_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.1).move_to([4.35, 1.35, 0]))
        a_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        a_span.ax, a_span.source = ax, shift
        a_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 12) + LEFT * 0.85,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.85]))
        a_anchor = Line(ax.c2p(0, 12) + LEFT * 1.0, ax.c2p(0, 12) + LEFT * 0.7,
                        color=MUTED, stroke_width=2)
        a_cap = Line(ax.c2p(0, 12) + LEFT * 1.0, ax.c2p(0, 12) + LEFT * 0.7,
                     color=DEFINITION, stroke_width=2)
        a_cap.ax, a_cap.source = ax, shift
        a_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 1.0,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.7))
        a_label = MathTex('a', color=DEFINITION).scale(0.75)
        a_label.ax, a_label.source = ax, shift
        a_label.add_updater(lambda m: m.next_to(
            m.ax.c2p(0, 12 + m.source.get_value() / 2) + LEFT * 0.85, LEFT, buff=0.18))
        demand_divider = Line([1.55, -3.15, 0], [1.55, 2.45, 0], color=MUTED, stroke_width=1).set_opacity(0.5)
        demand_list_head = Tex('Scenarios', color=CAPTION).scale(0.75).move_to([2.1, 0.73, 0], aligned_edge=LEFT)
        demand_scenarios = VGroup()
        for label, sign, y in [
                ('Health study', 'a>0', 0.2),
                ('Less preference', 'a<0', -0.23),
                ('Income: normal good', 'a>0', -0.66),
                ('Income: inferior good', 'a<0', -1.09),
                ('Romaine price rises', 'a>0', -1.52),
                ('Dressing price rises', 'a<0', -1.95),
                ('More buyers', r'c\downarrow', -2.38)]:
            scenario = VGroup(Tex(label, color=INK).scale(0.72).move_to([2.1, y, 0], aligned_edge=LEFT),
                              MathTex(sign, color=DEFINITION).scale(0.72).move_to([6.7, y, 0]))
            demand_scenarios.add(scenario)
        self.play(FadeIn(demand_divider), FadeIn(demand_equation), FadeIn(a_readout),
                  FadeIn(a_span), FadeIn(a_anchor), FadeIn(a_cap), FadeIn(a_label))

        self.play(price.animate.set_value(3), run_time=1.6)
        self.pause('8.a')
        self.play(price.animate.set_value(4), run_time=1.3)

        # ---- 8.b · At fixed price, everyone's increased MB shifts demand.
        before_demand = demand.copy().clear_updaters().set_color(MUTED).set_opacity(0.55)
        before_word = Tex('$D_0$', color=CAPTION).scale(0.7).next_to(ax.c2p(54, 1.2), RIGHT, buff=0.16)
        self.add(before_demand)
        self.remove(bottom)
        bottom = Tex(r'A change in {{demand}} shifts the whole curve.',
                     tex_to_color_map={'demand': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bottom), FadeIn(demand_list_head), FadeIn(demand_scenarios[0]), FadeIn(before_word))
        self.play(shift.animate.set_value(5), run_time=2)
        self.pause('8.b')

        # ---- 8.c · The same shift can be read vertically at a fixed quantity.
        # Remove the price-input guides before measuring MB at Q=30.
        self.play(FadeOut(p_line), FadeOut(q_line), FadeOut(point), FadeOut(p_number), FadeOut(q_number), FadeOut(q_prefix))
        vertical_change = Line(ax.c2p(30, 6), ax.c2p(30, 11), color=FOCUS, stroke_width=5)
        endpoints = VGroup(Dot(ax.c2p(30, 6), color=CAPTION), Dot(ax.c2p(30, 11), color=GUIDE))
        mb_words = VGroup(Tex('6', color=CAPTION).scale(0.7).next_to(ax.c2p(30, 6), LEFT, buff=0.2),
                          Tex('11', color=GUIDE).scale(0.7).next_to(ax.c2p(30, 11), RIGHT, buff=0.2))
        self.remove(bottom)
        bottom = Tex('More at the same price; a higher willingness to pay for the same quantity.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(vertical_change), FadeIn(endpoints), FadeIn(mb_words), FadeIn(bottom))
        self.pause('8.c')
        self.play(FadeOut(vertical_change), FadeOut(endpoints), FadeOut(mb_words))
        self.play(shift.animate.set_value(0), run_time=1.2)
        for mob in (p_line, q_line, point, p_number, q_number, q_prefix):
            mob.update()
        self.play(FadeIn(p_line), FadeIn(q_line), FadeIn(point), FadeIn(p_number), FadeIn(q_number), FadeIn(q_prefix))

        # ---- 8.d · Reduced preference reverses the shift at the same price.
        self.play(demand_scenarios[0].animate.set_color(CAPTION), FadeIn(demand_scenarios[1]))
        self.remove(bottom)
        bottom = Tex('Less demand: less is wanted at every price.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bottom), shift.animate.set_value(-3), run_time=1.7)
        self.pause('8.d')
        self.play(shift.animate.set_value(0), run_time=1.2)

        # ---- 8.e · Income rises: normal goods move out.
        self.play(demand_scenarios[1].animate.set_color(CAPTION), FadeIn(demand_scenarios[2]))
        self.remove(head, question, bottom)
        head = title('Demand shifters')
        question = Tex(r'\textsf{What else changes demand for spinach?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        bottom = Tex(r'{{Normal goods}}: higher income increases demand.',
                     tex_to_color_map={'Normal goods': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(bottom))
        self.play(shift.animate.set_value(3), run_time=1.7)
        self.pause('8.e')
        self.play(shift.animate.set_value(0), run_time=1.2)

        # ---- 8.f · Reuse the schematic for noodles, explicitly naming the good.
        self.play(demand_scenarios[2].animate.set_color(CAPTION), FadeIn(demand_scenarios[3]))
        # The geometry illustrates direction only; these are not measured data.
        self.remove(bottom)
        self.remove(head, question)
        head = title('Demand shifters')
        question = Tex(r'\textsf{What if the good is instant noodles?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        self.play(FadeIn(head), FadeIn(question))
        bottom = Tex(r'{{Inferior goods}}: higher income decreases demand.',
                     tex_to_color_map={'Inferior goods': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bottom),
                  FadeOut(p_number), FadeOut(q_number), FadeOut(q_prefix),
                  FadeOut(axes_words[1]), FadeOut(axes_words[3]))
        self.play(shift.animate.set_value(-3), run_time=1.7)
        self.pause('8.f')
        self.play(shift.animate.set_value(0), run_time=1.2)
        self.play(FadeIn(p_number), FadeIn(q_number), FadeIn(q_prefix),
                  FadeIn(axes_words[1]), FadeIn(axes_words[3]))

        # ---- 8.g · Return to spinach: romaine is a substitute.
        self.play(demand_scenarios[3].animate.set_color(CAPTION), FadeIn(demand_scenarios[4]))
        self.remove(bottom)
        self.remove(head, question)
        head = title('Demand shifters')
        question = Tex(r'\textsf{What else changes demand for spinach?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        self.play(FadeIn(head), FadeIn(question))
        bottom = Tex(r'{{Substitutes}} can take each other\textquotesingle s place.',
                     tex_to_color_map={'Substitutes': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bottom))
        self.play(shift.animate.set_value(3), run_time=1.7)
        self.pause('8.g')
        self.play(shift.animate.set_value(0), run_time=1.2)

        # ---- 8.h · Dressing is a complement; its higher price reduces demand.
        self.play(demand_scenarios[4].animate.set_color(CAPTION), FadeIn(demand_scenarios[5]))
        self.remove(bottom)
        bottom = Tex(r'{{Complements}} are used together.',
                     tex_to_color_map={'Complements': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bottom))
        self.play(shift.animate.set_value(-3), run_time=1.7)
        self.pause('8.h')
        self.play(shift.animate.set_value(0), run_time=1.2)

        # ---- 8.i · Add identical buyers: quantities scale, the intercept stays.
        # With 25% more identical demand schedules, Q is 1.25 times as large
        # at every price: P=12-0.20Q becomes P=12-0.16Q. This is still a shift.
        self.play(demand_scenarios[5].animate.set_color(CAPTION), FadeIn(demand_scenarios[6]))
        self.remove(bottom, question, demand_equation)
        self.play(FadeOut(a_readout), FadeOut(a_span), FadeOut(a_anchor), FadeOut(a_cap), FadeOut(a_label))
        question = Tex(r'\textsf{What if we add 25\% more identical buyers?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        demand_entry_equation = MathTex(r'P=12-cQ',
            tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'c': DEFINITION}).scale(0.85).move_to([4.35, 2.0, 0])
        c_number = DecimalNumber(0.2, num_decimal_places=2, color=DEFINITION).scale(0.8)
        c_number.source = demand_slope
        c_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        c_readout = VGroup(Tex('Slope coefficient:', color=CAPTION).scale(0.7),
                          MathTex('c=', color=DEFINITION).scale(0.8), c_number)
        c_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.12).move_to([4.35, 1.35, 0]))
        c_readout.update()
        bottom = Tex('More buyers increase quantity demanded at each price.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(question), FadeIn(demand_entry_equation), FadeIn(c_readout), FadeIn(bottom))
        self.play(demand_slope.animate.set_value(0.16), run_time=1.7)
        self.pause('8.i')
        # No callbacks survive the cut into the supply construction.
        for mob in self.mobjects:
            mob.clear_updaters()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 9.a · Price alone moves along an unchanged supply curve.
        head = title('Supply: movement and shift')
        question = Tex(r'\textsf{Did supply change, or did the price change?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        ax = style_axes([0, 100, 20], [0, 9, 2], x_length=4.6, y_length=4.6)
        ax.shift(np.array([-6.25, -2.25, 0]) - ax.c2p(0, 0))
        axis_p = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 9), LEFT, buff=0.25)
        axis_q = Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(100, 0), DOWN, buff=0.35)
        axes_words = VGroup(axis_p,
            Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5).next_to(axis_p, LEFT, buff=0.12),
            axis_q,
            Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(axis_q, DOWN, buff=0.08))
        price = ValueTracker(4)
        cost_shift = ValueTracker(0)
        supply_slope = ValueTracker(0.05)
        supply = Line(ax.c2p(0, 2), ax.c2p(100, 7), color=SUPPLY, stroke_width=3)
        supply.ax, supply.shift_value, supply.slope = ax, cost_shift, supply_slope
        supply.add_updater(lambda m: m.put_start_and_end_on(m.ax.c2p(0, 2 + m.shift_value.get_value()),
            m.ax.c2p(100, 2 + m.shift_value.get_value() + 100 * m.slope.get_value())))
        supply_word = Tex('S', color=INK).scale(0.8)
        supply_word.curve = supply
        supply_word.add_updater(lambda m: m.next_to(m.curve.get_end(), RIGHT, buff=0.15))
        point = Dot(ax.c2p(40, 4), color=GUIDE, radius=0.065, z_index=12)
        point.ax, point.price, point.shift_value = ax, price, cost_shift
        point.slope = supply_slope
        point.add_updater(lambda m: m.move_to(m.ax.c2p(
            (m.price.get_value() - 2 - m.shift_value.get_value()) / m.slope.get_value(), m.price.get_value())))
        p_line = DashedLine(ax.c2p(0, 4), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        p_line.ax, p_line.price, p_line.shift_value = ax, price, cost_shift
        p_line.slope = supply_slope
        p_line.add_updater(lambda m: m.become(DashedLine(m.ax.c2p(0, m.price.get_value()),
            m.ax.c2p((m.price.get_value() - 2 - m.shift_value.get_value()) / m.slope.get_value(), m.price.get_value()), color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
        q_line = DashedLine(ax.c2p(40, 0), ax.c2p(40, 4), color=GUIDE, stroke_width=2, z_index=10)
        q_line.ax, q_line.price, q_line.shift_value = ax, price, cost_shift
        q_line.slope = supply_slope
        q_line.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p((m.price.get_value() - 2 - m.shift_value.get_value()) / m.slope.get_value(), 0),
            m.ax.c2p((m.price.get_value() - 2 - m.shift_value.get_value()) / m.slope.get_value(), m.price.get_value()), color=GUIDE, stroke_width=2, z_index=10).set_style(**m.get_style())))
        p_number = DecimalNumber(4, num_decimal_places=0, color=GUIDE).scale(0.8)
        p_number.ax, p_number.price = ax, price
        p_number.add_updater(lambda m: m.set_value(m.price.get_value()).next_to(m.ax.c2p(0, m.price.get_value()), LEFT, buff=0.2))
        q_number = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.8)
        q_number.ax, q_number.price, q_number.shift_value = ax, price, cost_shift
        q_number.slope = supply_slope
        q_number.add_updater(lambda m: m.set_value((m.price.get_value() - 2 - m.shift_value.get_value()) / m.slope.get_value())
            .next_to(m.ax.c2p(m.get_value(), 0), DOWN, buff=0.2))
        q_prefix = Tex('$Q_s=$', color=GUIDE).scale(0.8)
        q_prefix.number = q_number
        q_prefix.add_updater(lambda m: m.next_to(m.number, LEFT, buff=0.08))
        bottom = Tex(r'A change in {{quantity supplied}} moves along the curve.',
                     tex_to_color_map={'quantity supplied': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question), FadeIn(ax), FadeIn(axes_words), FadeIn(supply), FadeIn(supply_word))
        self.play(FadeIn(p_line), FadeIn(point), FadeIn(p_number))
        self.play(FadeIn(q_line), FadeIn(q_number), FadeIn(q_prefix), FadeIn(bottom))
        # Positive b raises marginal cost, so it means a decrease in supply.
        supply_equation = MathTex(r'P=2+', 'b', r'+Q/20',
                                  tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'b': DEFINITION}).scale(0.85)
        supply_equation.move_to([4.35, 2.0, 0])
        b_number = DecimalNumber(0, num_decimal_places=2, include_sign=True, color=DEFINITION).scale(0.8)
        b_number.source = cost_shift
        b_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        b_readout = VGroup(MathTex('b=', color=DEFINITION).scale(0.8), b_number)
        b_readout.arrange(RIGHT, buff=0.1).move_to([4.35, 1.35, 0])
        b_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.1).move_to([4.35, 1.35, 0]))
        b_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        b_span.ax, b_span.source = ax, cost_shift
        b_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 2) + LEFT * 0.85,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.85]))
        b_anchor = Line(ax.c2p(0, 2) + LEFT * 1.0, ax.c2p(0, 2) + LEFT * 0.7,
                        color=MUTED, stroke_width=2)
        b_cap = Line(ax.c2p(0, 2) + LEFT * 1.0, ax.c2p(0, 2) + LEFT * 0.7,
                     color=DEFINITION, stroke_width=2)
        b_cap.ax, b_cap.source = ax, cost_shift
        b_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 1.0,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.7))
        b_label = MathTex('b', color=DEFINITION).scale(0.75)
        b_label.ax, b_label.source = ax, cost_shift
        b_label.add_updater(lambda m: m.next_to(
            m.ax.c2p(0, 2 + m.source.get_value() / 2) + LEFT * 0.85, LEFT, buff=0.18))
        supply_divider = Line([1.55, -3.15, 0], [1.55, 2.45, 0], color=MUTED, stroke_width=1).set_opacity(0.5)
        supply_list_head = Tex('Scenarios', color=CAPTION).scale(0.75).move_to([2.1, 0.73, 0], aligned_edge=LEFT)
        supply_scenarios = VGroup()
        for label, sign, y in [
                ('Farmland costs more', 'b>0', 0.2),
                ('Fertilizer costs less', 'b<0', -0.35),
                ('Carrots pay more', 'b>0', -0.9),
                ('More sellers', r'd\downarrow', -1.45),
                ('Better technology', 'b<0', -2.0)]:
            scenario = VGroup(Tex(label, color=INK).scale(0.7).move_to([2.1, y, 0], aligned_edge=LEFT),
                              MathTex(sign, color=DEFINITION).scale(0.7).move_to([5.85, y, 0]))
            supply_scenarios.add(scenario)
        self.play(FadeIn(supply_divider), FadeIn(supply_equation), FadeIn(b_readout),
                  FadeIn(b_span), FadeIn(b_anchor), FadeIn(b_cap), FadeIn(b_label))

        self.play(price.animate.set_value(5), run_time=1.7)
        self.pause('9.a')
        self.play(price.animate.set_value(4), run_time=1.2)

        # ---- 9.b · Molly's costs rise; at the same price fewer lots pay.
        # A named cost bar is an enlarged marginal unit, not a second market.
        before_supply = supply.copy().clear_updaters().set_color(MUTED).set_opacity(0.55)
        before_word = Tex('$S_0$', color=CAPTION).scale(0.7).next_to(ax.c2p(85, 6.25), UP, buff=0.15)
        self.add(before_supply)
        self.remove(head, question, bottom)
        head = title('Supply shifters')
        question = Tex(r'\textsf{What changes the cost of growing spinach?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        bottom = Tex(r'A change in {{supply}} shifts the whole curve.',
                     tex_to_color_map={'supply': DEFINITION}).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        molly_selection = Line(ax.c2p(20, 0), ax.c2p(20, 3), color=SUPPLY, stroke_width=10)
        self.play(FadeIn(molly_selection))
        molly_bar = Line([6.5, -1.6, 0], [6.5, 0.2, 0], color=SUPPLY, stroke_width=20)
        molly_bar.shift_value = cost_shift
        molly_bar.add_updater(lambda m: m.put_start_and_end_on(np.array([6.5, -1.6, 0]),
            np.array([6.5, -1.6 + 0.6 * (3 + m.shift_value.get_value()), 0])))
        molly_name = Tex(r"\shortstack{Molly's\\next unit}", color=INK).scale(0.72).move_to([6.5, -2.05, 0])
        molly_price = DashedLine([6.0, 0.8, 0], [7.0, 0.8, 0], color=GUIDE)
        molly_price_word = Tex(r'$P=4$', color=GUIDE).scale(0.7).next_to(molly_price, UP, buff=0.15)
        self.play(FadeIn(head), FadeIn(question), FadeIn(bottom), FadeIn(before_word),
                  TransformFromCopy(molly_selection, molly_bar), FadeIn(molly_name),
                  FadeIn(molly_price), FadeIn(molly_price_word))
        self.play(FadeOut(molly_selection))
        self.play(FadeIn(supply_list_head), FadeIn(supply_scenarios[0]))
        self.play(cost_shift.animate.set_value(1.25), run_time=1.7)
        self.pause('9.b')
        self.play(cost_shift.animate.set_value(0), run_time=1.2)

        # ---- 9.c · Cheaper fertilizer lowers each marginal cost.
        self.play(supply_scenarios[0].animate.set_color(CAPTION), FadeIn(supply_scenarios[1]))
        self.play(cost_shift.animate.set_value(-1), run_time=1.7)
        self.pause('9.c')
        self.play(cost_shift.animate.set_value(0), run_time=1.2)

        # ---- 9.d · A better alternative use raises opportunity cost.
        self.play(supply_scenarios[1].animate.set_color(CAPTION), FadeIn(supply_scenarios[2]))
        self.play(cost_shift.animate.set_value(1.25), run_time=1.7)
        self.pause('9.d')
        self.play(cost_shift.animate.set_value(0), FadeOut(molly_bar), FadeOut(molly_name),
                  FadeOut(molly_price), FadeOut(molly_price_word), run_time=1.2)

        # ---- 9.e · Add identical sellers without changing individual costs.
        # Horizontal aggregation raises Q by 25% at every price above $2.
        # P=2+0.05Q becomes P=2+0.04Q; the cost intercept remains $2.
        self.play(supply_scenarios[2].animate.set_color(CAPTION), FadeIn(supply_scenarios[3]))
        self.remove(bottom, question, supply_equation)
        self.play(FadeOut(b_readout), FadeOut(b_span), FadeOut(b_anchor), FadeOut(b_cap), FadeOut(b_label))
        question = Tex(r'\textsf{What if we add 25\% more identical sellers?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        supply_entry_equation = MathTex(r'P=2+dQ',
            tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'd': DEFINITION}).scale(0.85).move_to([4.35, 2.0, 0])
        d_number = DecimalNumber(0.05, num_decimal_places=2, color=DEFINITION).scale(0.8)
        d_number.source = supply_slope
        d_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        d_readout = VGroup(Tex('Slope coefficient:', color=CAPTION).scale(0.7),
                          MathTex('d=', color=DEFINITION).scale(0.8), d_number)
        d_readout.add_updater(lambda m: m.arrange(RIGHT, buff=0.12).move_to([4.35, 1.35, 0]))
        d_readout.update()
        bottom = Tex('More sellers increase quantity supplied at each price.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(question), FadeIn(supply_entry_equation), FadeIn(d_readout), FadeIn(bottom))
        self.play(supply_slope.animate.set_value(0.04), run_time=1.7)
        self.pause('9.e')
        self.play(supply_slope.animate.set_value(0.05), run_time=1.2)

        # ---- 9.f · Technology lowers cost and expands supply.
        self.play(supply_scenarios[3].animate.set_color(CAPTION), FadeIn(supply_scenarios[4]))
        self.remove(bottom, question, supply_entry_equation, d_readout)
        question = Tex(r'\textsf{What changes the cost of growing spinach?}', color=CAPTION).scale(0.75)
        question.next_to(head, DOWN, buff=0.18, aligned_edge=LEFT).shift(RIGHT * 0.35)
        bottom = Tex('Lower costs increase supply at every price.', color=INK).scale(DEFINITION_SCALE)
        bottom.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(question), FadeIn(supply_equation), FadeIn(b_readout), FadeIn(b_span),
                  FadeIn(b_anchor), FadeIn(b_cap), FadeIn(b_label), FadeIn(bottom))
        self.play(cost_shift.animate.set_value(-1), run_time=1.7)
        self.pause('9.f')
        for mob in self.mobjects:
            mob.clear_updaters()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ========== 10. Comparative statics ==========
        # A shift is a change in the schedule. Price adjustment is a second,
        # separate motion on the schedules that now exist.
        self.clear()
        head = title('Comparative statics')
        cs_ax = style_axes([0, 90, 10], [0, 18, 2], x_length=4.5, y_length=4.5)
        cs_ax.shift(np.array([-2.25, BODY_MID + 0.18, 0])
                    - (cs_ax.c2p(0, 0) + cs_ax.c2p(90, 18)) / 2)
        cs_p_name = Tex('P', color=INK).scale(0.8).next_to(cs_ax.c2p(0, 18), LEFT, buff=0.18)
        cs_p_units = Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5)
        cs_p_units.next_to(cs_p_name, LEFT, buff=0.12)
        cs_q_name = Tex('Q', color=INK).scale(0.8).next_to(cs_ax.c2p(90, 0), DOWN, buff=0.2)
        cs_q_units = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5)
        cs_q_units.next_to(cs_q_name, DOWN, buff=0.08)
        cs_divider_x = max(cs_q_name.get_right()[0], cs_q_units.get_right()[0]) + 0.35
        cs_divider = Line([cs_divider_x, BODY_BOTTOM, 0], [cs_divider_x, BODY_TOP, 0],
                          color=MUTED, stroke_width=1).set_opacity(0.5)
        cs_a = ValueTracker(0)
        cs_price = ValueTracker(4)
        cs_demand_before = Line(cs_ax.c2p(0, 12), cs_ax.c2p(60, 0), color=MUTED, stroke_width=2)
        cs_demand = Line(cs_ax.c2p(0, 12), cs_ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        cs_demand.ax, cs_demand.shock = cs_ax, cs_a
        cs_demand.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.shock.get_value()),
            m.ax.c2p(60 + 5 * m.shock.get_value(), 0)))
        cs_d_label = Tex('D', color=INK).scale(0.8)
        cs_d_label.ax, cs_d_label.shock = cs_ax, cs_a
        cs_d_label.add_updater(lambda m: m.next_to(m.ax.c2p(
            5 * (12 + m.shock.get_value()), 0), UR, buff=0.15))
        cs_d_label.update()
        cs_d_equation = MathTex(r'P=12+a-\frac{Q}{5}',
                               tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'a': DEFINITION}).scale(0.85)
        cs_d_equation.move_to([4.55, 1.35, 0])
        cs_a_number = DecimalNumber(0, num_decimal_places=0, include_sign=True, color=DEFINITION).scale(0.8)
        cs_a_number.source = cs_a
        cs_a_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        cs_a_word = MathTex('a=', color=DEFINITION).scale(0.8)
        # Reuse the established a measure: baseline intercept to current intercept.
        # Coincident points make a zero shift vanish without changing opacity.
        cs_a_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        cs_a_span.ax, cs_a_span.source = cs_ax, cs_a
        cs_a_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 12) + LEFT * 0.8,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.8]))
        cs_a_anchor = Line(cs_ax.c2p(0, 12) + LEFT * 0.95,
                               cs_ax.c2p(0, 12) + LEFT * 0.65, color=MUTED, stroke_width=2)
        cs_a_cap = Line(cs_ax.c2p(0, 12) + LEFT * 0.95,
                            cs_ax.c2p(0, 12) + LEFT * 0.65, color=DEFINITION, stroke_width=2)
        cs_a_cap.ax, cs_a_cap.source = cs_ax, cs_a
        cs_a_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.95,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.65))
        cs_a_group = VGroup(cs_a_word, cs_a_number).arrange(RIGHT, buff=0.08)
        cs_a_group.ax, cs_a_group.source = cs_ax, cs_a
        cs_a_group.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).move_to(
            m.ax.c2p(0, min(12, 12 + m.source.get_value())) + LEFT * 0.8 + DOWN * 0.28))
        cs_a_group.update()
        cs_phase = Tex('Recall the demand shift', color=INK).scale(0.8).move_to([4.55, 2.25, 0])
        cs_prompt = Tex('How does the market respond to a change?', color=DEFINITION).scale(DEFINITION_SCALE)
        cs_prompt.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        # This case record remains in one place across the three experiments.
        # Results enter only after each market has reached its new equilibrium.
        cs_case_heading = Tex('Scenarios', color=CAPTION).scale(0.7).move_to([4.55, -1.22, 0])
        cs_case_up = Tex('Demand increases', color=CAPTION).scale(0.7).move_to([2.2, -1.67, 0], aligned_edge=LEFT)
        cs_case_down = Tex('Demand decreases', color=CAPTION).scale(0.7).move_to([2.2, -2.12, 0], aligned_edge=LEFT)
        cs_case_supply = Tex('Supply decreases', color=CAPTION).scale(0.7).move_to([2.2, -2.57, 0], aligned_edge=LEFT)
        cs_case_up_result = MathTex(r'P^*\uparrow,\;Q^*\uparrow', color=GUIDE).scale(0.7).move_to([6.35, -1.67, 0])
        cs_case_down_result = MathTex(r'P^*\downarrow,\;Q^*\downarrow', color=GUIDE).scale(0.7).move_to([6.35, -2.12, 0])
        cs_case_supply_result = MathTex(r'P^*\uparrow,\;Q^*\downarrow', color=GUIDE).scale(0.7).move_to([6.35, -2.57, 0])
        cs_case_objects = [cs_case_heading, cs_case_up, cs_case_down, cs_case_supply,
                           cs_case_up_result, cs_case_down_result, cs_case_supply_result]
        self.play(FadeIn(head), FadeIn(cs_ax), FadeIn(cs_p_name), FadeIn(cs_p_units),
                  FadeIn(cs_q_name), FadeIn(cs_q_units), FadeIn(cs_demand), FadeIn(cs_d_label),
                  FadeIn(cs_d_equation), FadeIn(cs_a_group), FadeIn(cs_a_span), FadeIn(cs_a_anchor), FadeIn(cs_a_cap), FadeIn(cs_divider),
                  FadeIn(cs_phase), FadeIn(cs_prompt), FadeIn(cs_case_heading),
                  FadeIn(cs_case_up), FadeIn(cs_case_down), FadeIn(cs_case_supply))
        self.pause('10.a')

        # ---- 10.b · Revisit a on demand alone, with its measured shift in gold.
        self.add(cs_demand_before)
        self.bring_to_front(cs_demand)
        self.play(cs_a.animate.set_value(5), run_time=1.8)
        self.pause('10.b')
        self.play(cs_a.animate.set_value(-3), run_time=2)
        self.pause('10.c')
        self.play(cs_a.animate.set_value(0), run_time=1.4)

        # ---- 10.d · Supply restores the familiar equilibrium: Q=40, P=4.
        cs_supply = Line(cs_ax.c2p(0, 2), cs_ax.c2p(90, 6.5), color=SUPPLY, stroke_width=4)
        cs_s_label = Tex('S', color=INK).scale(0.8).next_to(cs_ax.c2p(84, 6.2), UP, buff=0.12)
        cs_s_equation = MathTex(r'P=2+\frac{Q}{20}',
                               tex_to_color_map={'P': GUIDE, 'Q': GUIDE}).scale(0.85)
        cs_s_equation.move_to([4.55, 0.55, 0])
        cs_h = DashedLine(cs_ax.c2p(0, 4), cs_ax.c2p(40, 4), color=GUIDE, stroke_width=2)
        cs_h.ax, cs_h.price, cs_h.shock = cs_ax, cs_price, cs_a
        cs_h.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(0, m.price.get_value()),
            m.ax.c2p(max(20 * m.price.get_value() - 40,
                         60 + 5 * m.shock.get_value() - 5 * m.price.get_value()), m.price.get_value()),
            color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        cs_s_dot = Dot(cs_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        cs_s_dot.ax, cs_s_dot.price = cs_ax, cs_price
        cs_s_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            20 * m.price.get_value() - 40, m.price.get_value())))
        cs_d_dot = Dot(cs_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        cs_d_dot.ax, cs_d_dot.price, cs_d_dot.shock = cs_ax, cs_price, cs_a
        cs_d_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            60 + 5 * m.shock.get_value() - 5 * m.price.get_value(), m.price.get_value())))
        cs_s_drop = DashedLine(cs_ax.c2p(40, 4), cs_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        cs_s_drop.ax, cs_s_drop.price = cs_ax, cs_price
        cs_s_drop.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(20 * m.price.get_value() - 40, m.price.get_value()),
            m.ax.c2p(20 * m.price.get_value() - 40, 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        cs_d_drop = DashedLine(cs_ax.c2p(40, 4), cs_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        cs_d_drop.ax, cs_d_drop.price, cs_d_drop.shock = cs_ax, cs_price, cs_a
        cs_d_drop.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(60 + 5 * m.shock.get_value() - 5 * m.price.get_value(), m.price.get_value()),
            m.ax.c2p(60 + 5 * m.shock.get_value() - 5 * m.price.get_value(), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        cs_p_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        cs_p_number.ax, cs_p_number.source = cs_ax, cs_price
        cs_p_number.add_updater(lambda m: m.set_value(m.source.get_value())
                               .next_to(m.ax.c2p(0, m.source.get_value()), LEFT, buff=0.2))
        cs_p_number.update()
        cs_q_number = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7)
        cs_q_number.ax, cs_q_number.source = cs_ax, cs_price
        cs_q_number.add_updater(lambda m: m.set_value(20 * m.source.get_value() - 40)
                               .next_to(m.ax.c2p(20 * m.source.get_value() - 40, 0), DOWN, buff=0.2))
        cs_q_number.update()
        self.remove(cs_phase)
        cs_phase = Tex('Baseline equilibrium', color=INK).scale(0.8).move_to([4.55, 2.25, 0])
        self.play(FadeIn(cs_supply), FadeIn(cs_s_label), FadeIn(cs_s_equation), FadeIn(cs_phase))
        self.play(FadeIn(cs_p_number), FadeIn(cs_h), FadeIn(cs_s_dot), FadeIn(cs_d_dot))
        self.play(FadeIn(cs_s_drop), FadeIn(cs_d_drop), FadeIn(cs_q_number))
        cs_equilibrium = MathTex(r'(Q^*,P^*)', color=GUIDE).scale(0.7)
        cs_equilibrium.anchor = cs_s_dot
        cs_equilibrium.add_updater(lambda m: m.next_to(m.anchor, UP, buff=0.23))
        cs_equilibrium.update()
        self.play(FadeIn(cs_equilibrium))
        self.pause('10.d')

        # ---- 10.e · A positive demand shock arrives while the price stays $4.
        # The dots remain the two quantities at that price, never a moving
        # equilibrium. Separate quantity labels are staggered while they meet.
        self.remove(head)
        head = title('A change in demand')
        self.remove(cs_phase, cs_prompt)
        cs_phase = Tex('Demand rises; price fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        cs_prompt = Tex('What happens when demand increases?', color=DEFINITION).scale(DEFINITION_SCALE)
        cs_prompt.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(cs_phase), FadeIn(cs_prompt), cs_case_up.animate.set_color(INK))
        cs_s_q = VGroup(MathTex('Q_s=', color=GUIDE).scale(0.7),
                       DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7))
        cs_s_q.ax, cs_s_q.source = cs_ax, cs_price
        cs_s_q[1].source = cs_price
        cs_s_q[1].add_updater(lambda m: m.set_value(20 * m.source.get_value() - 40))
        cs_s_q.add_updater(lambda m: m.arrange(RIGHT, buff=0.08)
                          .next_to(m.ax.c2p(20 * m.source.get_value() - 40, 0), DOWN, buff=0.2))
        cs_s_q.update()
        cs_d_q = VGroup(MathTex('Q_d=', color=GUIDE).scale(0.7),
                       DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7))
        cs_d_q.ax, cs_d_q.price, cs_d_q.shock = cs_ax, cs_price, cs_a
        cs_d_q[1].price, cs_d_q[1].shock = cs_price, cs_a
        cs_d_q[1].add_updater(lambda m: m.set_value(60 + 5 * m.shock.get_value() - 5 * m.price.get_value()))
        cs_d_q.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).next_to(m.ax.c2p(
            60 + 5 * m.shock.get_value() - 5 * m.price.get_value(), 0), DOWN, buff=0.64))
        cs_d_q.update()
        self.remove(cs_q_number, cs_equilibrium)
        self.play(FadeIn(cs_s_q), FadeIn(cs_d_q))
        self.play(cs_a.animate.set_value(5), run_time=2)
        cs_shortage = Brace(Line(cs_ax.c2p(40, 4.3), cs_ax.c2p(65, 4.3)), direction=UP,
                                        color=INK, buff=0.1)
        cs_shortage_word = Tex('Shortage: 25', color=INK).scale(0.7).next_to(cs_shortage, UP, buff=0.12)
        self.play(FadeIn(cs_shortage), FadeIn(cs_shortage_word))
        self.pause('10.e')

        # ---- 10.f · Hold the shifted demand and supply still; raise only price.
        cs_old_dot = Dot(cs_ax.c2p(40, 4), color=MUTED, radius=0.055, z_index=5)
        cs_old_h = DashedLine(cs_ax.c2p(0, 4), cs_ax.c2p(40, 4), color=MUTED, stroke_width=1.5)
        cs_old_v = DashedLine(cs_ax.c2p(40, 0), cs_ax.c2p(40, 4), color=MUTED, stroke_width=1.5)
        self.play(FadeOut(cs_shortage), FadeOut(cs_shortage_word))
        self.add(cs_old_dot, cs_old_h, cs_old_v)
        self.remove(cs_phase)
        cs_phase = Tex('Price adjusts; curves stay fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        self.play(FadeIn(cs_phase))
        self.play(cs_price.animate.set_value(5), run_time=2.4)
        self.remove(cs_s_q, cs_d_q)
        cs_q_number.update()
        cs_equilibrium.update()
        self.play(FadeIn(cs_q_number), FadeIn(cs_equilibrium))
        cs_increase = MathTex(r'\Delta P=+1,\qquad\Delta Q=+20',
                             tex_to_color_map={'P': GUIDE, 'Q': GUIDE, '+1': GUIDE, '+20': GUIDE}).scale(0.8)
        cs_increase.move_to([4.55, -0.35, 0])
        self.play(FadeIn(cs_increase), FadeIn(cs_case_up_result))
        self.pause('10.f')

        # ---- 10.g · Equate the two schedules, then reveal each algebra step.
        # This is the calculation of the equilibrium just observed on the graph.
        self.play(FadeOut(cs_d_equation), FadeOut(cs_s_equation), FadeOut(cs_increase))
        self.remove(cs_phase)
        cs_phase = Tex('Solve for equilibrium', color=INK).scale(0.8).move_to([4.55, 2.25, 0])
        self.play(FadeIn(cs_phase))
        cs_equal = MathTex(r'12+a-\frac{Q}{5}=2+\frac{Q}{20}',
                          tex_to_color_map={'Q': GUIDE, 'a': DEFINITION}).scale(0.8).move_to([4.55, 1.5, 0])
        cs_collect = MathTex(r'10+a=\frac{Q}{4}', tex_to_color_map={'Q': GUIDE, 'a': DEFINITION}).scale(0.8)
        cs_collect.move_to([4.55, 0.9, 0])
        cs_q_solution = MathTex(r'Q^*=40+4a', tex_to_color_map={'Q^*': GUIDE, 'a': DEFINITION}).scale(0.85)
        cs_q_solution.move_to([4.55, 0.3, 0])
        cs_p_solution = MathTex(r'P^*=4+\frac{a}{5}', tex_to_color_map={'P^*': GUIDE, 'a': DEFINITION}).scale(0.85)
        cs_p_solution.move_to([4.55, -0.3, 0])
        self.play(FadeIn(cs_equal))
        self.play(FadeIn(cs_collect))
        self.play(FadeIn(cs_q_solution))
        self.play(FadeIn(cs_p_solution))
        self.pause('10.g')
        cs_concrete = MathTex(r'a=5:\quad Q^*=60,\quad P^*=5',
                             tex_to_color_map={'Q^*': GUIDE, 'P^*': GUIDE, '60': GUIDE, 'a': DEFINITION}).scale(0.8)
        cs_concrete.move_to([4.55, -0.8, 0])
        self.play(FadeIn(cs_concrete))
        self.pause('10.h')

        # ---- 10.i · Reset explicitly, then reduce normal-good demand at $4.
        self.play(FadeOut(cs_equal), FadeOut(cs_collect), FadeOut(cs_q_solution),
                  FadeOut(cs_p_solution), FadeOut(cs_concrete))
        self.remove(head)
        head = title('A change in demand')
        self.remove(cs_phase, cs_prompt)
        cs_phase = Tex('Income falls: reset the market', color=INK).scale(0.8).move_to([4.55, 2.25, 0])
        cs_prompt = Tex('What if income falls?', color=DEFINITION).scale(DEFINITION_SCALE)
        cs_prompt.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(cs_phase), FadeIn(cs_prompt),
                  cs_case_up.animate.set_color(CAPTION), cs_case_down.animate.set_color(INK),
                  cs_a.animate.set_value(0), cs_price.animate.set_value(4), run_time=1.6)
        self.pause('10.i')
        self.remove(cs_q_number, cs_equilibrium)
        cs_s_q.update()
        cs_d_q.update()
        self.play(FadeIn(cs_s_q), FadeIn(cs_d_q))
        self.remove(cs_phase)
        cs_phase = Tex('Demand falls; price fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        self.play(FadeIn(cs_phase))
        self.play(cs_a.animate.set_value(-5), run_time=2)
        cs_excess = Brace(Line(cs_ax.c2p(15, 4.3), cs_ax.c2p(40, 4.3)), direction=UP,
                                      color=INK, buff=0.1)
        cs_excess_word = Tex('Excess supply: 25', color=INK).scale(0.7).next_to(cs_excess, UP, buff=0.12)
        cs_low_equation = MathTex(r'P=7-\frac{Q}{5}',
                                 tex_to_color_map={'P': GUIDE, 'Q': GUIDE}).scale(0.85)
        cs_low_equation.move_to([4.55, 1.35, 0])
        self.play(FadeIn(cs_excess), FadeIn(cs_excess_word), FadeIn(cs_low_equation))
        self.pause('10.j')
        self.play(FadeOut(cs_excess), FadeOut(cs_excess_word))
        self.remove(cs_phase)
        cs_phase = Tex('Price adjusts; curves stay fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        self.play(FadeIn(cs_phase))
        self.play(cs_price.animate.set_value(3), run_time=2.4)
        self.remove(cs_s_q, cs_d_q)
        cs_q_number.update()
        cs_equilibrium.update()
        self.play(FadeIn(cs_q_number), FadeIn(cs_equilibrium))
        cs_low_result = MathTex(r'Q^*=20,\qquad P^*=3',
                               tex_to_color_map={'Q^*': GUIDE, 'P^*': GUIDE, '20': GUIDE, '3': GUIDE}).scale(0.85)
        cs_low_result.move_to([4.55, 0.55, 0])
        cs_low_delta = MathTex(r'\Delta P=-1,\qquad\Delta Q=-20',
                              tex_to_color_map={'P': GUIDE, 'Q': GUIDE, '-1': GUIDE, '-20': GUIDE}).scale(0.8)
        cs_low_delta.move_to([4.55, -0.35, 0])
        self.play(FadeIn(cs_low_result), FadeIn(cs_low_delta), FadeIn(cs_case_down_result))
        self.pause('10.k')
        # Keep the completed demand cases visible while replacing the market.
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in cs_case_objects])

        # ---- 10.l · Fertilizer starts on its own freshly restored market.
        head = title('A change in supply')
        ss_ax = style_axes([0, 90, 10], [0, 18, 2], x_length=4.5, y_length=4.5)
        ss_ax.shift(np.array([-2.25, BODY_MID + 0.18, 0])
                    - (ss_ax.c2p(0, 0) + ss_ax.c2p(90, 18)) / 2)
        ss_p_name = Tex('P', color=INK).scale(0.8).next_to(ss_ax.c2p(0, 18), LEFT, buff=0.18)
        ss_p_units = Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5)
        ss_p_units.next_to(ss_p_name, LEFT, buff=0.12)
        ss_q_name = Tex('Q', color=INK).scale(0.8).next_to(ss_ax.c2p(90, 0), DOWN, buff=0.2)
        ss_q_units = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5)
        ss_q_units.next_to(ss_q_name, DOWN, buff=0.08)
        ss_divider_x = max(ss_q_name.get_right()[0], ss_q_units.get_right()[0]) + 0.35
        ss_divider = Line([ss_divider_x, BODY_BOTTOM, 0], [ss_divider_x, BODY_TOP, 0],
                          color=MUTED, stroke_width=1).set_opacity(0.5)
        ss_phase = Tex('Fertilizer costs rise', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        ss_prompt = Tex('What happens when fertilizer costs more?', color=DEFINITION).scale(DEFINITION_SCALE)
        ss_prompt.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        ss_b = ValueTracker(0)
        ss_price = ValueTracker(4)
        ss_demand = Line(ss_ax.c2p(0, 12), ss_ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        ss_d_label = Tex('D', color=INK).scale(0.8).next_to(ss_ax.c2p(60, 0), UR, buff=0.15)
        ss_supply_before = Line(ss_ax.c2p(0, 2), ss_ax.c2p(90, 6.5), color=MUTED, stroke_width=2)
        ss_supply = Line(ss_ax.c2p(0, 2), ss_ax.c2p(90, 6.5), color=SUPPLY, stroke_width=4)
        ss_supply.ax, ss_supply.shock = ss_ax, ss_b
        ss_supply.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 2 + m.shock.get_value()), m.ax.c2p(90, 6.5 + m.shock.get_value())))
        ss_s_label = Tex('S', color=INK).scale(0.8)
        ss_s_label.ax, ss_s_label.shock = ss_ax, ss_b
        ss_s_label.add_updater(lambda m: m.next_to(m.ax.c2p(84, 6.2 + m.shock.get_value()), UP, buff=0.12))
        ss_s_label.update()
        ss_h = DashedLine(ss_ax.c2p(0, 4), ss_ax.c2p(40, 4), color=GUIDE, stroke_width=2)
        ss_h.ax, ss_h.price, ss_h.shock = ss_ax, ss_price, ss_b
        ss_h.add_updater(lambda m: m.become(DashedLine(m.ax.c2p(0, m.price.get_value()),
            m.ax.c2p(max(60 - 5 * m.price.get_value(),
                         20 * (m.price.get_value() - 2 - m.shock.get_value())), m.price.get_value()),
            color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        ss_d_dot = Dot(ss_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        ss_d_dot.ax, ss_d_dot.price = ss_ax, ss_price
        ss_d_dot.add_updater(lambda m: m.move_to(m.ax.c2p(60 - 5 * m.price.get_value(), m.price.get_value())))
        ss_s_dot = Dot(ss_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        ss_s_dot.ax, ss_s_dot.price, ss_s_dot.shock = ss_ax, ss_price, ss_b
        ss_s_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            20 * (m.price.get_value() - 2 - m.shock.get_value()), m.price.get_value())))
        ss_d_drop = DashedLine(ss_ax.c2p(40, 4), ss_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        ss_d_drop.ax, ss_d_drop.price = ss_ax, ss_price
        ss_d_drop.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(60 - 5 * m.price.get_value(), m.price.get_value()),
            m.ax.c2p(60 - 5 * m.price.get_value(), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        ss_s_drop = DashedLine(ss_ax.c2p(40, 4), ss_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        ss_s_drop.ax, ss_s_drop.price, ss_s_drop.shock = ss_ax, ss_price, ss_b
        ss_s_drop.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(20 * (m.price.get_value() - 2 - m.shock.get_value()), m.price.get_value()),
            m.ax.c2p(20 * (m.price.get_value() - 2 - m.shock.get_value()), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        ss_p_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        ss_p_number.ax, ss_p_number.source = ss_ax, ss_price
        ss_p_number.add_updater(lambda m: m.set_value(m.source.get_value())
                               .next_to(m.ax.c2p(0, m.source.get_value()), LEFT, buff=0.2))
        ss_p_number.update()
        ss_q_number = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7)
        ss_q_number.ax, ss_q_number.source = ss_ax, ss_price
        ss_q_number.add_updater(lambda m: m.set_value(60 - 5 * m.source.get_value())
                               .next_to(m.ax.c2p(60 - 5 * m.source.get_value(), 0), DOWN, buff=0.2))
        ss_q_number.update()
        ss_equation = MathTex(r'P=2+b+\frac{Q}{20}',
                             tex_to_color_map={'P': GUIDE, 'Q': GUIDE, 'b': DEFINITION}).scale(0.85).move_to([4.55, 1.35, 0])
        ss_b_number = DecimalNumber(0, num_decimal_places=2, include_sign=True, color=DEFINITION).scale(0.8)
        ss_b_number.source = ss_b
        ss_b_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        ss_b_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        ss_b_span.ax, ss_b_span.source = ss_ax, ss_b
        ss_b_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 2) + LEFT * 0.8,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.8]))
        ss_b_anchor = Line(ss_ax.c2p(0, 2) + LEFT * 0.95,
                               ss_ax.c2p(0, 2) + LEFT * 0.65, color=MUTED, stroke_width=2)
        ss_b_cap = Line(ss_ax.c2p(0, 2) + LEFT * 0.95,
                            ss_ax.c2p(0, 2) + LEFT * 0.65, color=DEFINITION, stroke_width=2)
        ss_b_cap.ax, ss_b_cap.source = ss_ax, ss_b
        ss_b_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.95,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.65))
        ss_b_group = VGroup(MathTex('b=', color=DEFINITION).scale(0.8), ss_b_number)
        ss_b_group.ax, ss_b_group.source = ss_ax, ss_b
        ss_b_group.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).move_to(
            m.ax.c2p(0, min(2, 2 + m.source.get_value())) + LEFT * 0.8 + DOWN * 0.3))
        ss_b_group.update()
        self.play(FadeIn(head), FadeIn(ss_ax), FadeIn(ss_p_name), FadeIn(ss_p_units), FadeIn(ss_q_name),
                  FadeIn(ss_q_units), FadeIn(ss_demand), FadeIn(ss_d_label), FadeIn(ss_supply), FadeIn(ss_s_label))
        self.play(FadeIn(ss_h), FadeIn(ss_d_dot), FadeIn(ss_s_dot), FadeIn(ss_d_drop), FadeIn(ss_s_drop),
                  FadeIn(ss_p_number), FadeIn(ss_q_number), FadeIn(ss_equation), FadeIn(ss_b_group),
                  FadeIn(ss_b_span), FadeIn(ss_b_anchor), FadeIn(ss_b_cap), FadeIn(ss_divider), FadeIn(ss_phase), FadeIn(ss_prompt),
                  cs_case_down.animate.set_color(CAPTION), cs_case_supply.animate.set_color(INK))
        ss_equilibrium = MathTex(r'(Q^*,P^*)', color=GUIDE).scale(0.7)
        ss_equilibrium.anchor = ss_d_dot
        ss_equilibrium.add_updater(lambda m: m.next_to(m.anchor, UP, buff=0.23))
        ss_equilibrium.update()
        self.play(FadeIn(ss_equilibrium))
        self.pause('10.l')

        # ---- 10.m · More costly supply leaves only 15 available at the old $4.
        self.add(ss_supply_before)
        self.bring_to_front(ss_supply)
        ss_s_q = VGroup(MathTex('Q_s=', color=GUIDE).scale(0.7),
                       DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7))
        ss_s_q.ax, ss_s_q.price, ss_s_q.shock = ss_ax, ss_price, ss_b
        ss_s_q[1].price, ss_s_q[1].shock = ss_price, ss_b
        ss_s_q[1].add_updater(lambda m: m.set_value(20 * (m.price.get_value() - 2 - m.shock.get_value())))
        ss_s_q.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).next_to(m.ax.c2p(
            20 * (m.price.get_value() - 2 - m.shock.get_value()), 0), DOWN, buff=0.64))
        ss_s_q.update()
        ss_d_q = VGroup(MathTex('Q_d=', color=GUIDE).scale(0.7),
                       DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7))
        ss_d_q.ax, ss_d_q.price = ss_ax, ss_price
        ss_d_q[1].price = ss_price
        ss_d_q[1].add_updater(lambda m: m.set_value(60 - 5 * m.price.get_value()))
        ss_d_q.add_updater(lambda m: m.arrange(RIGHT, buff=0.08)
                          .next_to(m.ax.c2p(60 - 5 * m.price.get_value(), 0), DOWN, buff=0.2))
        ss_d_q.update()
        self.remove(ss_q_number, ss_equilibrium)
        self.play(FadeIn(ss_s_q), FadeIn(ss_d_q))
        self.remove(ss_phase)
        ss_phase = Tex('Supply falls; price fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        self.play(FadeIn(ss_phase))
        self.play(ss_b.animate.set_value(1.25), run_time=2)
        ss_shortage = Brace(Line(ss_ax.c2p(15, 4.3), ss_ax.c2p(40, 4.3)), direction=UP,
                                        color=INK, buff=0.1)
        ss_shortage_word = Tex('Shortage: 25', color=INK).scale(0.7).next_to(ss_shortage, UP, buff=0.12)
        self.play(FadeIn(ss_shortage), FadeIn(ss_shortage_word))
        self.pause('10.m')

        # ---- 10.n · Price rises along the fixed schedules to Q=35, P=5.
        ss_old_dot = Dot(ss_ax.c2p(40, 4), color=MUTED, radius=0.055, z_index=5)
        ss_old_h = DashedLine(ss_ax.c2p(0, 4), ss_ax.c2p(40, 4), color=MUTED, stroke_width=1.5)
        ss_old_v = DashedLine(ss_ax.c2p(40, 0), ss_ax.c2p(40, 4), color=MUTED, stroke_width=1.5)
        self.play(FadeOut(ss_shortage), FadeOut(ss_shortage_word))
        self.add(ss_old_dot, ss_old_h, ss_old_v)
        self.remove(ss_phase)
        ss_phase = Tex('Price adjusts; curves stay fixed', color=INK).scale(0.7).move_to([4.55, 2.25, 0])
        self.play(FadeIn(ss_phase))
        self.play(ss_price.animate.set_value(5), run_time=2.4)
        self.remove(ss_s_q, ss_d_q)
        ss_q_number.update()
        ss_equilibrium.update()
        self.play(FadeIn(ss_q_number), FadeIn(ss_equilibrium))
        ss_solution = MathTex(r'Q^*=40-4b,\quad P^*=4+\frac{4b}{5}',
                             tex_to_color_map={'Q^*': GUIDE, 'P^*': GUIDE, 'b': DEFINITION}).scale(0.8)
        ss_solution.move_to([4.55, 0.55, 0])
        ss_result = MathTex(r'Q^*=35,\qquad P^*=5',
                           tex_to_color_map={'Q^*': GUIDE, 'P^*': GUIDE, '35': GUIDE, '5': GUIDE}).scale(0.85)
        ss_result.move_to([4.55, -0.35, 0])
        self.play(FadeIn(ss_solution))
        self.play(FadeIn(ss_result), FadeIn(cs_case_supply_result))
        comparative_def = Tex(r'{{Comparative statics}} compares equilibrium before and after a change.',
                              tex_to_color_map={'Comparative statics': DEFINITION}).scale(DEFINITION_SCALE)
        comparative_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(ss_prompt)
        self.play(FadeIn(comparative_def))
        self.pause('10.n')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ========== 7. Both curves shift ==========
        # Each target is a different possible pair of shocks from the same
        # baseline. These moving intersections compare equilibria; they do not
        # assert that a real market's adjustment follows this transition path.
        head = title('Both curves shift')
        both_ax = style_axes([0, 90, 10], [0, 18, 2], x_length=4.5, y_length=4.5)
        both_ax.shift(np.array([-1.2, BODY_MID + 0.18, 0])
                      - (both_ax.c2p(0, 0) + both_ax.c2p(90, 18)) / 2)
        both_p_name = Tex('P', color=INK).scale(0.8).next_to(both_ax.c2p(0, 18), LEFT, buff=0.18)
        both_p_units = Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5)
        both_p_units.next_to(both_p_name, LEFT, buff=0.12)
        both_q_name = Tex('Q', color=INK).scale(0.8).next_to(both_ax.c2p(90, 0), DOWN, buff=0.2)
        both_q_units = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5)
        both_q_units.next_to(both_q_name, DOWN, buff=0.08)
        both_a, both_b = ValueTracker(0), ValueTracker(0)
        # Keep both changes measurable while the outcome record accumulates.
        both_a_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        both_a_span.ax, both_a_span.source = both_ax, both_a
        both_a_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 12) + LEFT * 0.8,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.8]))
        both_a_anchor = Line(both_ax.c2p(0, 12) + LEFT * 0.95,
                               both_ax.c2p(0, 12) + LEFT * 0.65, color=MUTED, stroke_width=2)
        both_a_cap = Line(both_ax.c2p(0, 12) + LEFT * 0.95,
                            both_ax.c2p(0, 12) + LEFT * 0.65, color=DEFINITION, stroke_width=2)
        both_a_cap.ax, both_a_cap.source = both_ax, both_a
        both_a_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.95,
            m.ax.c2p(0, 12 + m.source.get_value()) + LEFT * 0.65))
        both_b_span = VMobject(stroke_color=DEFINITION, stroke_width=6)
        both_b_span.ax, both_b_span.source = both_ax, both_b
        both_b_span.add_updater(lambda m: m.set_points_as_corners([
            m.ax.c2p(0, 2) + LEFT * 0.8,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.8]))
        both_b_anchor = Line(both_ax.c2p(0, 2) + LEFT * 0.95,
                               both_ax.c2p(0, 2) + LEFT * 0.65, color=MUTED, stroke_width=2)
        both_b_cap = Line(both_ax.c2p(0, 2) + LEFT * 0.95,
                            both_ax.c2p(0, 2) + LEFT * 0.65, color=DEFINITION, stroke_width=2)
        both_b_cap.ax, both_b_cap.source = both_ax, both_b
        both_b_cap.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.95,
            m.ax.c2p(0, 2 + m.source.get_value()) + LEFT * 0.65))
        both_a_number = DecimalNumber(0, num_decimal_places=0, include_sign=True, color=DEFINITION).scale(0.7)
        both_a_number.source = both_a
        both_a_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        both_a_group = VGroup(MathTex('a=', color=DEFINITION).scale(0.7), both_a_number)
        both_a_group.ax, both_a_group.source = both_ax, both_a
        both_a_group.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).move_to(
            m.ax.c2p(0, min(12, 12 + m.source.get_value())) + LEFT * 0.8 + DOWN * 0.28))
        both_a_group.update()
        both_b_number = DecimalNumber(0, num_decimal_places=3, include_sign=True, color=DEFINITION).scale(0.7)
        both_b_number.source = both_b
        both_b_number.add_updater(lambda m: m.set_value(m.source.get_value()))
        both_b_group = VGroup(MathTex('b=', color=DEFINITION).scale(0.7), both_b_number)
        both_b_group.ax, both_b_group.source = both_ax, both_b
        both_b_group.add_updater(lambda m: m.arrange(RIGHT, buff=0.08).move_to(
            m.ax.c2p(0, min(2, 2 + m.source.get_value())) + LEFT * 0.8 + DOWN * 0.3))
        both_b_group.update()
        both_d_before = Line(both_ax.c2p(0, 12), both_ax.c2p(60, 0), color=MUTED, stroke_width=2)
        both_s_before = Line(both_ax.c2p(0, 2), both_ax.c2p(90, 6.5), color=MUTED, stroke_width=2)
        both_d = Line(both_ax.c2p(0, 12), both_ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        both_d.ax, both_d.source = both_ax, both_a
        both_d.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()), m.ax.c2p(60 + 5 * m.source.get_value(), 0)))
        both_s = Line(both_ax.c2p(0, 2), both_ax.c2p(90, 6.5), color=SUPPLY, stroke_width=4)
        both_s.ax, both_s.source = both_ax, both_b
        # Clip the supply curve at zero when b takes its intercept below zero.
        both_s.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(max(0, -20 * (2 + m.source.get_value())), max(0, 2 + m.source.get_value())),
            m.ax.c2p(90, 6.5 + m.source.get_value())))
        both_d_label = Tex('D', color=INK).scale(0.8)
        both_d_label.ax, both_d_label.source = both_ax, both_a
        both_d_label.add_updater(lambda m: m.next_to(m.ax.c2p(
            5 * (12 + m.source.get_value()), 0), UR, buff=0.15))
        both_d_label.update()
        both_s_label = Tex('S', color=INK).scale(0.8)
        both_s_label.ax, both_s_label.source = both_ax, both_b
        both_s_label.add_updater(lambda m: m.next_to(m.ax.c2p(84, 6.2 + m.source.get_value()), UP, buff=0.12))
        both_s_label.update()
        both_dot = Dot(both_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        both_dot.ax, both_dot.a, both_dot.b = both_ax, both_a, both_b
        both_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            40 + 4 * m.a.get_value() - 4 * m.b.get_value(),
            4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5)))
        both_h = DashedLine(both_ax.c2p(0, 4), both_ax.c2p(40, 4), color=GUIDE, stroke_width=2)
        both_h.ax, both_h.a, both_h.b = both_ax, both_a, both_b
        both_h.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(0, 4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5),
            m.ax.c2p(40 + 4 * m.a.get_value() - 4 * m.b.get_value(),
                     4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        both_v = DashedLine(both_ax.c2p(40, 4), both_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        both_v.ax, both_v.a, both_v.b = both_ax, both_a, both_b
        both_v.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(40 + 4 * m.a.get_value() - 4 * m.b.get_value(),
                     4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5),
            m.ax.c2p(40 + 4 * m.a.get_value() - 4 * m.b.get_value(), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        both_p_number = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        both_p_number.ax, both_p_number.a, both_p_number.b = both_ax, both_a, both_b
        both_p_number.add_updater(lambda m: m.set_value(4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5)
                                 .next_to(m.ax.c2p(0, 4 + m.a.get_value() / 5 + 4 * m.b.get_value() / 5),
                                          LEFT, buff=0.2))
        both_p_number.update()
        both_q_number = DecimalNumber(40, num_decimal_places=1, color=GUIDE).scale(0.7)
        both_q_number.ax, both_q_number.a, both_q_number.b = both_ax, both_a, both_b
        both_q_number.add_updater(lambda m: m.set_value(40 + 4 * m.a.get_value() - 4 * m.b.get_value())
                                 .next_to(m.ax.c2p(40 + 4 * m.a.get_value() - 4 * m.b.get_value(), 0), DOWN, buff=0.2))
        both_q_number.update()
        both_baseline = VGroup(
            Dot(both_ax.c2p(40, 4), color=MUTED, radius=0.055),
            DashedLine(both_ax.c2p(0, 4), both_ax.c2p(40, 4), color=MUTED, stroke_width=1.5),
            DashedLine(both_ax.c2p(40, 0), both_ax.c2p(40, 4), color=MUTED, stroke_width=1.5))
        both_causes = VGroup(Tex('Romaine costs more', color=INK),
                             Tex('Harvesting costs less', color=INK)).arrange(DOWN, buff=0.3).scale(0.8)
        both_causes.move_to([5.35, 1.6, 0])
        both_divider = Line([3.45, BODY_BOTTOM, 0], [3.45, BODY_TOP, 0],
                            color=MUTED, stroke_width=1).set_opacity(0.5)
        both_prompt = Tex('What if demand and supply both increase?', color=DEFINITION).scale(DEFINITION_SCALE)
        both_prompt.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        both_record_headers = VGroup(Tex('Price', color=CAPTION).scale(0.75).move_to([4.55, 0.55, 0]),
                                     Tex('Quantity', color=CAPTION).scale(0.75).move_to([6.55, 0.55, 0]))
        both_record_up = VGroup(Tex('Rises', color=INK).scale(0.75).move_to([4.55, -0.05, 0]),
                                Tex('Rises', color=INK).scale(0.75).move_to([6.55, -0.05, 0]))
        both_record_same = VGroup(Tex('Unchanged', color=INK).scale(0.75).move_to([4.55, -0.7, 0]),
                                  Tex('Rises', color=INK).scale(0.75).move_to([6.55, -0.7, 0]))
        both_record_down = VGroup(Tex('Falls', color=INK).scale(0.75).move_to([4.55, -1.35, 0]),
                                  Tex('Rises', color=INK).scale(0.75).move_to([6.55, -1.35, 0]))
        both_record_note = VGroup(Tex('Same starting market', color=CAPTION),
                                  Tex('Three possible outcomes', color=CAPTION))
        both_record_note.arrange(DOWN, buff=0.2).scale(0.7).move_to([5.35, -2.2, 0])
        self.play(FadeIn(head), FadeIn(both_ax), FadeIn(both_p_name), FadeIn(both_p_units),
                  FadeIn(both_q_name), FadeIn(both_q_units), FadeIn(both_d), FadeIn(both_s),
                  FadeIn(both_d_label), FadeIn(both_s_label), FadeIn(both_h), FadeIn(both_v),
                  FadeIn(both_dot), FadeIn(both_p_number), FadeIn(both_q_number), FadeIn(both_causes),
                  FadeIn(both_divider), FadeIn(both_record_headers), FadeIn(both_prompt), FadeIn(both_record_note),
                  FadeIn(both_a_span), FadeIn(both_a_anchor), FadeIn(both_a_cap), FadeIn(both_b_span), FadeIn(both_b_anchor), FadeIn(both_b_cap), FadeIn(both_a_group), FadeIn(both_b_group))
        both_equilibrium = MathTex(r'(Q^*,P^*)', color=GUIDE).scale(0.7)
        both_equilibrium.anchor = both_dot
        both_equilibrium.add_updater(lambda m: m.next_to(m.anchor, UP, buff=0.23))
        both_equilibrium.update()
        self.play(FadeIn(both_equilibrium))
        self.pause('11.a')
        self.add(both_d_before, both_s_before, both_baseline)
        self.bring_to_front(both_d, both_s, both_dot)
        self.play(both_a.animate.set_value(5), both_b.animate.set_value(-0.625), run_time=2.4)
        self.play(FadeIn(both_record_up))
        self.pause('11.b')

        # ---- 11.c · Same demand shift; a larger supply shift cancels the price rise.
        self.play(both_record_up.animate.set_color(CAPTION), both_b.animate.set_value(-1.25), run_time=1.8)
        self.play(FadeIn(both_record_same))
        self.pause('11.c')

        # ---- 11.d · A still larger supply shift lowers price; quantity rises again.
        self.play(both_record_same.animate.set_color(CAPTION), both_b.animate.set_value(-2.5), run_time=1.8)
        self.play(FadeIn(both_record_down))
        indeterminate_def = Tex(r'{{Indeterminate}}: the direction depends on the relative sizes of the shifts.',
                                tex_to_color_map={'Indeterminate': DEFINITION}).scale(DEFINITION_SCALE)
        indeterminate_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(both_prompt)
        self.play(FadeIn(indeterminate_def))
        self.pause('11.d')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ========== 8. How much price, how much quantity? ==========
        # Both plots use exactly the same scale, range, demand curve, and
        # starting equilibrium. Only the supply response differs.
        head = title('Elasticity and market changes')
        question = Tex('How much changes in price, and how much in quantity?', color=DEFINITION).scale(DEFINITION_SCALE)
        question.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        elastic_ax = style_axes([0, 90, 10], [0, 18, 2], x_length=4.2, y_length=4.2)
        elastic_ax.shift(np.array([-3.75, BODY_MID + 0.13, 0])
                         - (elastic_ax.c2p(0, 0) + elastic_ax.c2p(90, 18)) / 2)
        inelastic_ax = style_axes([0, 90, 10], [0, 18, 2], x_length=4.2, y_length=4.2)
        inelastic_ax.shift(np.array([3.75, BODY_MID + 0.13, 0])
                           - (inelastic_ax.c2p(0, 0) + inelastic_ax.c2p(90, 18)) / 2)
        elastic_name = Tex('More elastic supply', color=INK).scale(0.8).move_to([-3.75, 2.58, 0])
        inelastic_name = Tex('Less elastic supply', color=INK).scale(0.8).move_to([3.75, 2.58, 0])
        panel_axes_words = VGroup()
        # Repeated geometry only; all animation order remains below in construct.
        for panel_ax in (elastic_ax, inelastic_ax):
            panel_p = Tex('P', color=INK).scale(0.8).next_to(panel_ax.c2p(0, 18), LEFT, buff=0.16)
            panel_p_units = Tex(r'\textsf{\$/lb}', color=CAPTION).scale(0.5)
            panel_p_units.next_to(panel_p, LEFT, buff=0.12)
            panel_q = Tex('Q', color=INK).scale(0.8).next_to(panel_ax.c2p(90, 0), DOWN, buff=0.2)
            panel_q_units = Tex(r'\textsf{thousand lb}', color=CAPTION).scale(0.5).next_to(panel_q, DOWN, buff=0.08)
            panel_axes_words.add(panel_p, panel_p_units, panel_q, panel_q_units)
        panel_a = ValueTracker(0)
        elastic_d_before = Line(elastic_ax.c2p(0, 12), elastic_ax.c2p(60, 0), color=MUTED, stroke_width=2)
        inelastic_d_before = Line(inelastic_ax.c2p(0, 12), inelastic_ax.c2p(60, 0), color=MUTED, stroke_width=2)
        elastic_d = Line(elastic_ax.c2p(0, 12), elastic_ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        elastic_d.ax, elastic_d.source = elastic_ax, panel_a
        elastic_d.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()), m.ax.c2p(60 + 5 * m.source.get_value(), 0)))
        inelastic_d = Line(inelastic_ax.c2p(0, 12), inelastic_ax.c2p(60, 0), color=DEMAND, stroke_width=4)
        inelastic_d.ax, inelastic_d.source = inelastic_ax, panel_a
        inelastic_d.add_updater(lambda m: m.put_start_and_end_on(
            m.ax.c2p(0, 12 + m.source.get_value()), m.ax.c2p(60 + 5 * m.source.get_value(), 0)))
        elastic_s = Line(elastic_ax.c2p(0, 2), elastic_ax.c2p(90, 6.5), color=SUPPLY, stroke_width=4)
        # P=.8Q-28 is visible only from Q=35 through Q=57.5 (P=18).
        inelastic_s = Line(inelastic_ax.c2p(35, 0), inelastic_ax.c2p(57.5, 18), color=SUPPLY, stroke_width=4)
        elastic_s_word = Tex('S', color=INK).scale(0.8).next_to(elastic_ax.c2p(84, 6.2), UP, buff=0.1)
        inelastic_s_word = Tex('S', color=INK).scale(0.8).next_to(inelastic_ax.c2p(55, 16), RIGHT, buff=0.1)
        elastic_d_word = Tex('D', color=INK).scale(0.8)
        elastic_d_word.ax, elastic_d_word.source = elastic_ax, panel_a
        elastic_d_word.add_updater(lambda m: m.next_to(m.ax.c2p(
            5 * (12 + m.source.get_value()), 0), UR, buff=0.15))
        elastic_d_word.update()
        inelastic_d_word = Tex('D', color=INK).scale(0.8)
        inelastic_d_word.ax, inelastic_d_word.source = inelastic_ax, panel_a
        inelastic_d_word.add_updater(lambda m: m.next_to(m.ax.c2p(
            5 * (12 + m.source.get_value()), 0), UR, buff=0.15))
        inelastic_d_word.update()
        panel_baseline = VGroup()
        for panel_ax in (elastic_ax, inelastic_ax):
            panel_baseline.add(Dot(panel_ax.c2p(40, 4), color=MUTED, radius=0.055),
                               DashedLine(panel_ax.c2p(0, 4), panel_ax.c2p(40, 4), color=MUTED, stroke_width=1.5),
                               DashedLine(panel_ax.c2p(40, 4), panel_ax.c2p(40, 0), color=MUTED, stroke_width=1.5))
        elastic_dot = Dot(elastic_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        elastic_dot.ax, elastic_dot.source = elastic_ax, panel_a
        elastic_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            40 + 4 * m.source.get_value(), 4 + m.source.get_value() / 5)))
        inelastic_dot = Dot(inelastic_ax.c2p(40, 4), color=GUIDE, radius=0.07, z_index=6)
        inelastic_dot.ax, inelastic_dot.source = inelastic_ax, panel_a
        inelastic_dot.add_updater(lambda m: m.move_to(m.ax.c2p(
            40 + m.source.get_value(), 4 + 0.8 * m.source.get_value())))
        elastic_h = DashedLine(elastic_ax.c2p(0, 4), elastic_ax.c2p(40, 4), color=GUIDE, stroke_width=2)
        elastic_h.ax, elastic_h.source = elastic_ax, panel_a
        elastic_h.add_updater(lambda m: m.become(DashedLine(m.ax.c2p(0, 4 + m.source.get_value() / 5),
            m.ax.c2p(40 + 4 * m.source.get_value(), 4 + m.source.get_value() / 5), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        elastic_v = DashedLine(elastic_ax.c2p(40, 4), elastic_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        elastic_v.ax, elastic_v.source = elastic_ax, panel_a
        elastic_v.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(40 + 4 * m.source.get_value(), 4 + m.source.get_value() / 5),
            m.ax.c2p(40 + 4 * m.source.get_value(), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        inelastic_h = DashedLine(inelastic_ax.c2p(0, 4), inelastic_ax.c2p(40, 4), color=GUIDE, stroke_width=2)
        inelastic_h.ax, inelastic_h.source = inelastic_ax, panel_a
        inelastic_h.add_updater(lambda m: m.become(DashedLine(m.ax.c2p(0, 4 + 0.8 * m.source.get_value()),
            m.ax.c2p(40 + m.source.get_value(), 4 + 0.8 * m.source.get_value()), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        inelastic_v = DashedLine(inelastic_ax.c2p(40, 4), inelastic_ax.c2p(40, 0), color=GUIDE, stroke_width=2)
        inelastic_v.ax, inelastic_v.source = inelastic_ax, panel_a
        inelastic_v.add_updater(lambda m: m.become(DashedLine(
            m.ax.c2p(40 + m.source.get_value(), 4 + 0.8 * m.source.get_value()),
            m.ax.c2p(40 + m.source.get_value(), 0), color=GUIDE, stroke_width=2).set_style(**m.get_style())))
        elastic_p = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        elastic_p.ax, elastic_p.source = elastic_ax, panel_a
        elastic_p.add_updater(lambda m: m.set_value(4 + m.source.get_value() / 5)
                             .next_to(m.ax.c2p(0, 4 + m.source.get_value() / 5), LEFT, buff=0.16))
        elastic_p.update()
        inelastic_p = DecimalNumber(4, num_decimal_places=2, color=GUIDE).scale(0.7)
        inelastic_p.ax, inelastic_p.source = inelastic_ax, panel_a
        inelastic_p.add_updater(lambda m: m.set_value(4 + 0.8 * m.source.get_value())
                               .next_to(m.ax.c2p(0, 4 + 0.8 * m.source.get_value()), LEFT, buff=0.16))
        inelastic_p.update()
        elastic_q = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7)
        elastic_q.ax, elastic_q.source = elastic_ax, panel_a
        elastic_q.add_updater(lambda m: m.set_value(40 + 4 * m.source.get_value())
                             .next_to(m.ax.c2p(40 + 4 * m.source.get_value(), 0), DOWN, buff=0.2))
        elastic_q.update()
        inelastic_q = DecimalNumber(40, num_decimal_places=0, color=GUIDE).scale(0.7)
        inelastic_q.ax, inelastic_q.source = inelastic_ax, panel_a
        inelastic_q.add_updater(lambda m: m.set_value(40 + m.source.get_value())
                               .next_to(m.ax.c2p(40 + m.source.get_value(), 0), DOWN, buff=0.2))
        inelastic_q.update()
        self.play(FadeIn(head), FadeIn(question), FadeIn(elastic_ax), FadeIn(inelastic_ax), FadeIn(panel_axes_words),
                  FadeIn(elastic_name), FadeIn(inelastic_name), FadeIn(elastic_d), FadeIn(inelastic_d),
                  FadeIn(elastic_s), FadeIn(inelastic_s), FadeIn(elastic_s_word), FadeIn(inelastic_s_word),
                  FadeIn(elastic_d_word), FadeIn(inelastic_d_word))
        self.play(FadeIn(elastic_dot), FadeIn(inelastic_dot), FadeIn(elastic_h), FadeIn(elastic_v),
                  FadeIn(inelastic_h), FadeIn(inelastic_v), FadeIn(elastic_p), FadeIn(inelastic_p),
                  FadeIn(elastic_q), FadeIn(inelastic_q))
        elastic_equilibrium = MathTex(r'(Q^*,P^*)', color=GUIDE).scale(0.7)
        elastic_equilibrium.anchor = elastic_dot
        elastic_equilibrium.add_updater(lambda m: m.next_to(m.anchor, UP, buff=0.23))
        elastic_equilibrium.update()
        inelastic_equilibrium = MathTex(r'(Q^*,P^*)', color=GUIDE).scale(0.7)
        inelastic_equilibrium.anchor = inelastic_dot
        inelastic_equilibrium.add_updater(lambda m: m.next_to(m.anchor, RIGHT, buff=0.18))
        inelastic_equilibrium.update()
        self.play(FadeIn(elastic_equilibrium), FadeIn(inelastic_equilibrium))
        self.pause('12.a')

        # ---- 12.b · One shared tracker gives both demand curves the same shift.
        self.add(elastic_d_before, inelastic_d_before, panel_baseline)
        self.bring_to_front(elastic_d, inelastic_d, elastic_dot, inelastic_dot)
        self.play(panel_a.animate.set_value(5), run_time=3)
        self.pause('12.b')
        elastic_delta = MathTex(r'\Delta P=+1,\quad\Delta Q=+20',
                               tex_to_color_map={'P': GUIDE, 'Q': GUIDE, '+1': GUIDE, '+20': GUIDE}).scale(0.8)
        elastic_delta.move_to([-3.75, -3.03, 0])
        inelastic_delta = MathTex(r'\Delta P=+4,\quad\Delta Q=+5',
                                 tex_to_color_map={'P': GUIDE, 'Q': GUIDE, '+4': GUIDE, '+5': GUIDE}).scale(0.8)
        inelastic_delta.move_to([3.75, -3.03, 0])
        self.play(FadeIn(elastic_delta), FadeIn(inelastic_delta))
        response_def = Tex(r'{{Elasticity}} helps explain how a shift changes price and quantity.',
                           tex_to_color_map={'Elasticity': DEFINITION}).scale(DEFINITION_SCALE)
        response_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(question)
        self.play(FadeIn(response_def))
        self.pause('12.c')

        # ---- 13.a · Close on the comparison; the market picture earns the cue.
        self.remove(head, response_def)
        head = title('Market changes')
        question = Tex('How do markets respond to change?', color=DEFINITION).scale(DEFINITION_SCALE)
        question.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(head), FadeIn(question))
        self.pause('13.a')
        self.remove(question)
        next_time = Tex('Next time: international trade.', color=CAPTION).scale(DEFINITION_SCALE)
        next_time.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(next_time))
        self.pause('13.b')
