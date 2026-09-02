# maniml 03_Code.py EpisodeA3
#
# Episode A3 | Specializing and trading can make both parties better off
# One scene; beats follow 02_Storyboard.md (B01...B21). The stage is A2's
# closing stage carried forward (two panels, under-axis rate lines, autarky
# markers); the new device is the TRADE-pink trade line, pivoting on the
# endowment, driven by a rate tracker. Staged offer rates are 1.5 / 5 / 3
# (see the storyboard's Numbers note — the notes' 2.5/3.5 contradict the
# window math and are flagged for the prose swap). The stage-1 verbatim
# merge of the old scenes is archived at _archive/03_Code_stage1_merge.py.

from manim import *
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, title(), bumper(), exercise_card(), ...
from style import axes as style_axes
from Video import PPF_Molly, PPF_Andrew

# The shared two-panel stage, verbatim from A2's B15 block so the recap is
# literally the screen A2 ended on (guide §1: peers share the band centre).
PANEL_KWARGS = dict(
    x_range=[0, 11, 1], y_range=[0, 45, 5], x_length=4.6, y_length=4.3, ticks=True,
)
PANEL_DROP = DOWN * 0.30
NAME_Y = -3.30                 # the under-axis band: names / stored rate lines


def molly_axes():
    return style_axes(
        x_axis_config={'numbers_to_include': [10],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        y_axis_config={'numbers_to_include': [40],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        **PANEL_KWARGS).shift(LEFT * 3.8 + PANEL_DROP)


def andrew_axes():
    return style_axes(
        x_axis_config={'numbers_to_include': [8],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        y_axis_config={'numbers_to_include': [16],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        **PANEL_KWARGS).shift(RIGHT * 3.2 + PANEL_DROP)


def panel_caps(ax_):
    return VGroup(
        Tex('Carrots').scale(SCALE_TICK).set_color(CARROTS).next_to(ax_.c2p(11, 0), RIGHT, buff=0.2),
        Tex('Spinach').scale(SCALE_TICK).set_color(SPINACH).next_to(ax_.c2p(0, 42), RIGHT, buff=0.2))


def under_axis(ax_, mob):
    """Park a line centred under a panel's x-axis (the A2 name/rate band)."""
    return mob.move_to(np.array([ax_.c2p(5.5, 0)[0], NAME_Y, 0]))


def rate_tex(name, s_num):
    """An under-axis stored-rate line: numerals INK, letters colored."""
    return Tex(f'{name}: {{{{1}}}} {{{{C}}}} $=$ {{{{{s_num}}}}} {{{{S}}}}').scale(0.9).set_color_by_tex_to_color_map({
        'C': CARROTS, 'S': SPINACH})


def autarky_marker(ax_, c, s):
    p = ax_.c2p(c, s)
    dot = Dot(p, color=INK, z_index=10)
    v = DashedLine(ax_.c2p(c, 0), p, color=MUTED)
    h = DashedLine(ax_.c2p(0, s), p, color=MUTED)
    lab = Tex(f'({c}, {s})').scale(SCALE_CAPTION).set_color(CAPTION).next_to(p, DL, buff=0.15)
    return VGroup(v, h, dot, lab)


class Derivation:
    """A one-line derivation whose LETTERS never move and never re-render
    (ported from A2). Layout is `[numeral] C  =  [numeral] S`; step() returns
    the two Transforms that touch only the numerals."""

    def __init__(self, at, left_num, left_letter, right_num, right_letter,
                 sep='=', scale=1.2, sep_gap=0.8, num_room=0.75, num_gap=0.2,
                 left_color=CARROTS, right_color=SPINACH):
        self.scale_f = scale
        self.num_gap = num_gap
        self.sep = Tex(sep).scale(scale).move_to(at)
        self.lL = (Tex(left_letter).scale(scale).set_color(left_color)
                   .next_to(self.sep, LEFT, buff=sep_gap))
        self.lR = (Tex(right_letter).scale(scale).set_color(right_color)
                   .next_to(self.sep, RIGHT, buff=sep_gap + num_room + num_gap))
        self.nL = self._num(left_num, self.lL)
        self.nR = self._num(right_num, self.lR)
        self.group = VGroup(self.nL, self.lL, self.sep, self.nR, self.lR)

    def _num(self, txt, letter):
        return (Tex(txt).scale(self.scale_f).set_color(INK)
                .next_to(letter, LEFT, buff=self.num_gap))

    def step(self, left_num, right_num):
        return [Transform(self.nL, self._num(left_num, self.lL)),
                Transform(self.nR, self._num(right_num, self.lR))]


def focus_box(*mobs, buff=0.2):
    return SurroundingRectangle(VGroup(*mobs), color=FOCUS, buff=buff, stroke_width=2.5)


class EpisodeA3(Scene):
    """Episode A3 | Trade. One flat construct(); each `# Bxx` section is
    self-contained and ends at the pause() the viewer parks on."""

    def reset_frame(self):
        """Camera home. Called before every FadeAll transition (A1's B10 idiom)."""
        self.camera.frame.move_to(ORIGIN).set(width=FRAME_W)
        self.drop_frame()

    def drop_frame(self):
        """Take camera frames (bare Mobjects maniml puts in scene.mobjects)
        back out, so exercise_card()'s VGroup(*mobjects) never chokes."""
        for m in list(self.mobjects):
            if not isinstance(m, (VMobject, ImageMobject)):
                self.remove(m)

    def construct(self):

        # B01 ---------------------------------------------------------

        squares = bumper_raster(self)

        # B01b --------------------------------------------------------

        flicker(self, squares)

        # B01c --------------------------------------------------------

        label = bumper_title(self, squares, 'A', 3)
        thesis = Tex('\\textit{Specializing and trading can make both parties better off.}').scale(1.1).set_color(CAPTION).next_to(label, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause()

        # B02 ---------------------------------------------------------

        FadeAll(self)
        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B03 ---------------------------------------------------------
        # the recap IS A2's closing stage: both panels, rates, autarky markers

        self.play(FadeOut(last_card), run_time=1 / 2)
        axm = molly_axes()
        axa = andrew_axes()
        caps_m, caps_a = panel_caps(axm), panel_caps(axa)
        ppf_m = axm.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        ppf_a = axa.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        rate_m = under_axis(axm, rate_tex('Molly', '4'))
        rate_a = under_axis(axa, rate_tex('Andrew', '2'))
        mark_m = autarky_marker(axm, 3, 28)
        mark_a = autarky_marker(axa, 4, 8)
        self.play(FadeIn(axm), FadeIn(caps_m), FadeIn(ppf_m), FadeIn(rate_m), FadeIn(mark_m),
                  FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(rate_a), FadeIn(mark_a))
        self.pause()

        # B03b --------------------------------------------------------

        tech_line = (Tex('The choices themselves ARE the technology.')
                     .scale(0.9).set_color(DEFINITION).to_edge(UP, buff=0.5).set_x(0))
        self.play(Write(tech_line))
        self.pause()

        # B04 ---------------------------------------------------------
        # the history detour (A1's promise, delivered): out of feudalism, into
        # mercantilism, into the industrial revolution -- then what?

        self.reset_frame()
        FadeAll(self)
        hist = Tex('If not feudalism, then what?').scale(1.2).set_color(DEFINITION)
        self.play(Write(hist))
        self.pause()

        # B04b --------------------------------------------------------
        # one of the first rigorous answers: the model we started last time

        ricardo = (Tex(narration('--- David Ricardo, 1817')).scale(SCALE_CAPTION)
                   .set_color(CAPTION).next_to(hist, DOWN, buff=0.6).align_to(hist, RIGHT).shift(RIGHT * 1.2))
        self.play(FadeIn(ricardo))
        self.pause()

        # B05 ---------------------------------------------------------
        # self-trade recap: the stage returns; the A2 arrows re-draw; the hook

        FadeAll(self)
        self.play(FadeIn(axm), FadeIn(caps_m), FadeIn(ppf_m), FadeIn(rate_m), FadeIn(mark_m),
                  FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(rate_a), FadeIn(mark_a))
        arrow_m = CurvedArrow(axm.c2p(0, 40), axm.c2p(3, 28), angle=-PI / 3, color=FOCUS)
        arrow_a = CurvedArrow(axa.c2p(8, 0), axa.c2p(4, 8), angle=PI / 3, color=FOCUS)
        self.play(Create(arrow_m), Create(arrow_a))
        hook = Tex("Molly will accept any trade that's a better deal than her self-trade.").scale(0.7).set_color(DEFINITION)
        if hook.get_width() > FRAME_W - 2:
            hook.scale((FRAME_W - 2) / hook.get_width())
        hook.to_edge(UP, buff=0.55).set_x(0)
        self.play(Write(hook))
        self.pause()

        # B06 ---------------------------------------------------------
        # the trade line: Molly's panel front and centre

        FadeAll(self)
        head = title('The Trade Line')
        axm = molly_axes()
        caps_m = panel_caps(axm)
        ppf_m = axm.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        rate_m = under_axis(axm, rate_tex('Molly', '4'))
        mark_m = autarky_marker(axm, 3, 28)
        endow_def = (definition('Initial Endowment', 'is how much of both goods Molly has.')
                     .scale(0.9).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(FadeIn(head), FadeIn(axm), FadeIn(caps_m), FadeIn(ppf_m),
                  FadeIn(rate_m), FadeIn(mark_m))
        self.play(Write(endow_def))

        rate = ValueTracker(1.5)
        endow_m = ValueTracker(0.0)

        def em_dot_draw():
            e = endow_m.get_value()
            return Dot(axm.c2p(e, PPF_Molly(e)), color=MOLLY, z_index=11)

        em_dot = always_redraw(em_dot_draw)
        self.add(em_dot)
        self.play(Indicate(em_dot, color=FOCUS, scale_factor=2))
        self.pause()

        # B06b --------------------------------------------------------
        # ONE specific trade first, as a point: give 6 S, get 4 C (rate 1.5)

        offer_q = (Tex('Would Molly accept this trade?').scale(0.9).set_color(DEFINITION)
                   .next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Transform(endow_def, offer_q))
        pt_m = Dot(axm.c2p(4, 34), color=TRADE, z_index=12)
        pt_m_lab = Tex('(4, 34)').scale(SCALE_TICK).set_color(CAPTION).next_to(axm.c2p(4, 34), UR, buff=0.15)
        vm = DashedLine(axm.c2p(4, 0), axm.c2p(4, 34), color=MUTED)
        hm = DashedLine(axm.c2p(0, 34), axm.c2p(4, 34), color=MUTED)
        gain_m = Line(axm.c2p(0, 0), axm.c2p(4, 0), color=CARROTS, stroke_width=6)
        give_m = Line(axm.c2p(0, 34), axm.c2p(0, 40), color=SPINACH, stroke_width=6)
        self.play(FadeIn(vm), FadeIn(hm), FadeIn(pt_m), FadeIn(pt_m_lab))
        self.play(Create(give_m), Create(gain_m))
        self.pause()

        # B06c --------------------------------------------------------
        # the exchange rate, derived on screen the op-cost way

        deal = Derivation(RIGHT * 3.9 + UP * 0.8, '4', 'C', '6', 'S')
        self.play(FadeIn(deal.group))
        self.play(*deal.step(r'$\frac{4}{4}$', r'$\frac{6}{4}$'))
        self.play(*deal.step('1', '1.5'))
        self.pause()

        # B06d --------------------------------------------------------
        # the same trade, from Andrew's side

        axa = andrew_axes()
        caps_a = panel_caps(axa)
        ppf_a = axa.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        rate_a = under_axis(axa, rate_tex('Andrew', '2'))
        mark_a = autarky_marker(axa, 4, 8)
        self.play(FadeOut(deal.group),
                  FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(rate_a), FadeIn(mark_a))
        offer_q_a = (Tex('Would Andrew accept the same trade?').scale(0.9).set_color(DEFINITION)
                     .next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Transform(endow_def, offer_q_a))
        ea_pt = Dot(axa.c2p(4, 6), color=TRADE, z_index=12)
        ea_pt_lab = Tex('(4, 6)').scale(SCALE_TICK).set_color(CAPTION).next_to(axa.c2p(4, 6), DR, buff=0.15)
        va = DashedLine(axa.c2p(4, 0), axa.c2p(4, 6), color=MUTED)
        ha = DashedLine(axa.c2p(0, 6), axa.c2p(4, 6), color=MUTED)
        give_a = Line(axa.c2p(4, 0), axa.c2p(8, 0), color=CARROTS, stroke_width=6)
        gain_a = Line(axa.c2p(0, 0), axa.c2p(0, 6), color=SPINACH, stroke_width=6)
        self.play(FadeIn(va), FadeIn(ha), FadeIn(ea_pt), FadeIn(ea_pt_lab))
        self.play(Create(give_a), Create(gain_a))
        self.pause()

        # B06e --------------------------------------------------------
        # the standing rate takes the top slot; back to Molly, one-unit steps

        rate_cap = (Tex('Exchange Rate: {{1}} {{C}} $=$ {{1.5}} {{S}}').scale(0.9)
                    .set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH})
                    .next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Transform(endow_def, rate_cap),
                  FadeOut(pt_m), FadeOut(pt_m_lab), FadeOut(vm), FadeOut(hm),
                  FadeOut(gain_m), FadeOut(give_m),
                  FadeOut(ea_pt), FadeOut(ea_pt_lab), FadeOut(va), FadeOut(ha),
                  FadeOut(give_a), FadeOut(gain_a))

        steps = VGroup(*[Dot(axm.c2p(k, 40 - 1.5 * k), color=TRADE, z_index=10) for k in range(1, 7)])
        step_cap = Tex('{{+1}} {{C}}, {{$-$1.5}} {{S}}').scale(SCALE_TICK).set_color_by_tex_to_color_map({
            'C': CARROTS, 'S': SPINACH}).next_to(axm.c2p(1, 38.5), UR, buff=0.15)
        self.play(FadeIn(steps[0]), FadeIn(step_cap))
        self.play(LaggedStart(*[FadeIn(d) for d in steps[1:]], lag_ratio=0.35), run_time=2)
        self.pause()

        # B06f --------------------------------------------------------
        # the line through the steps; from here it lives on the rate tracker

        def trade_line_m():
            r = rate.get_value()
            e = endow_m.get_value()
            es = PPF_Molly(e)
            return axm.plot(lambda c: es - r * (c - e), color=TRADE,
                            x_range=(0, min(10.8, e + es / r)))

        tl_static = trade_line_m()
        slope_cap = (Tex(narration('slope $=$ exchange rate')).scale(SCALE_TICK)
                     .set_color(CAPTION).next_to(axm.c2p(7, 22.5), UR, buff=0.15))
        self.play(Create(tl_static), FadeOut(steps), FadeOut(step_cap))
        self.play(FadeIn(slope_cap))
        tl_m = always_redraw(trade_line_m)
        self.remove(tl_static)
        self.add(tl_m)
        self.pause()

        # B07 ---------------------------------------------------------
        # the contrast: the PPF anchors to its intercepts; the trade line
        # pivots on the endowment

        anchor_1 = Dot(axm.c2p(10, 0), color=FOCUS, z_index=11)
        anchor_2 = Dot(axm.c2p(0, 40), color=FOCUS, z_index=11)
        self.play(FadeIn(anchor_1), FadeIn(anchor_2))
        self.play(FadeOut(anchor_1), FadeOut(anchor_2))
        pivot_ring = Circle(radius=0.22, color=FOCUS, stroke_width=3).move_to(axm.c2p(0, 40))
        self.play(FadeIn(pivot_ring))
        self.play(rate.animate.set_value(2.2), run_time=1.2)
        self.play(rate.animate.set_value(0.9), run_time=1.2)
        self.play(rate.animate.set_value(1.5), run_time=1.2)
        self.play(FadeOut(pivot_ring))
        self.pause()

        # B08 ---------------------------------------------------------
        # outside -> accept; inside -> reject

        self.play(rate.animate.set_value(4.5), run_time=2)
        m_lab = Tex('rejects').scale(0.8).set_color(NASH).next_to(rate_m, RIGHT, buff=0.35)
        self.play(FadeIn(m_lab))
        self.pause()

        # B08b --------------------------------------------------------

        self.play(rate.animate.set_value(1.5), run_time=2)
        self.play(Transform(m_lab, Tex('accepts').scale(0.8).set_color(EFFICIENT).next_to(rate_m, RIGHT, buff=0.35)),
                  FadeOut(slope_cap))
        self.pause()

        # B09 ---------------------------------------------------------
        # Andrew joins; a rate very nice for Molly (1.5) — he rejects

        endow_a = ValueTracker(8.0)      # Andrew's panel has been on stage since B06d

        def ea_dot_draw():
            e = endow_a.get_value()
            return Dot(axa.c2p(e, PPF_Andrew(e)), color=ANDREW, z_index=11)

        def trade_line_a():
            r = rate.get_value()
            e = endow_a.get_value()
            es = PPF_Andrew(e)
            return axa.plot(lambda c: es - r * (c - e), color=TRADE,
                            x_range=(0, min(10.8, e + es / r)))

        ea_dot = always_redraw(ea_dot_draw)
        tl_a = always_redraw(trade_line_a)
        self.play(FadeOut(endow_def))
        self.add(ea_dot, tl_a)      # the rate already sits at 1.5, Molly's dream deal
        a_lab = Tex('rejects').scale(0.8).set_color(NASH).next_to(rate_a, RIGHT, buff=0.35)
        self.play(FadeIn(a_lab))
        self.pause()

        # B09b --------------------------------------------------------
        # Andrew's counter (5) — Molly rejects

        self.play(rate.animate.set_value(5), run_time=3)
        self.play(Transform(a_lab, Tex('accepts').scale(0.8).set_color(EFFICIENT).next_to(rate_a, RIGHT, buff=0.35)),
                  Transform(m_lab, Tex('rejects').scale(0.8).set_color(NASH).next_to(rate_m, RIGHT, buff=0.35)))
        self.pause()

        # B09c --------------------------------------------------------
        # the middle (3) — both accept: a Pareto improvement

        self.play(rate.animate.set_value(3), run_time=2)
        self.play(Transform(m_lab, Tex('accepts').scale(0.8).set_color(EFFICIENT).next_to(rate_m, RIGHT, buff=0.35)))
        pareto_def = (definition('Pareto improvement', ': a trade that makes both parties better off.')
                      .scale(0.9).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Write(pareto_def))
        self.pause()

        # B10 ---------------------------------------------------------
        # the big trade at rate 3: 3.5 C for 10.5 S, both better in BOTH goods

        rider_m = Dot(axm.c2p(0, 40), color=TRADE, z_index=12)
        rider_a = Dot(axa.c2p(8, 0), color=TRADE, z_index=12)
        self.play(FadeIn(rider_m), FadeIn(rider_a))
        self.play(rider_m.animate.move_to(axm.c2p(3.5, 29.5)),
                  rider_a.animate.move_to(axa.c2p(4.5, 10.5)), run_time=3)
        lab_rm = Tex('(3.5, 29.5)').scale(SCALE_TICK).set_color(CAPTION).next_to(axm.c2p(3.5, 29.5), UR, buff=0.25)
        lab_ra = Tex('(4.5, 10.5)').scale(SCALE_TICK).set_color(CAPTION).next_to(axa.c2p(4.5, 10.5), UR, buff=0.25)
        self.play(FadeIn(lab_rm), FadeIn(lab_ra))
        self.play(Indicate(rider_m, color=FOCUS), Indicate(rider_a, color=FOCUS))
        coop_cap = (Tex(narration("No co-op required --- we've simply specialized and traded."))
                    .scale(0.8).set_color(CAPTION).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Transform(pareto_def, coop_cap))
        self.pause()

        # B10b --------------------------------------------------------

        pref_cap = (Tex(narration('Still no preferences --- just the frontier.'))
                    .scale(0.8).set_color(CAPTION).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Transform(pareto_def, pref_cap))
        self.pause()

        # B11 ---------------------------------------------------------
        # the window: any rate between the two self-trade rates works

        box_m = focus_box(rate_m)
        box_a = focus_box(rate_a)
        self.play(FadeIn(box_m), FadeIn(box_a), FadeOut(pareto_def),
                  FadeOut(rider_m), FadeOut(rider_a), FadeOut(lab_rm), FadeOut(lab_ra))

        def rate_read():
            return VGroup(Tex('exchange rate $=$').scale(0.8),
                          DecimalNumber(rate.get_value(), num_decimal_places=1, color=INK).scale(0.8)
                          ).arrange(RIGHT, buff=0.2).move_to(UP * 2.55)

        readout = always_redraw(rate_read)
        self.add(readout)
        self.play(rate.animate.set_value(4.3), run_time=2)
        self.play(Transform(m_lab, Tex('rejects').scale(0.8).set_color(NASH).next_to(rate_m, RIGHT, buff=0.35)))
        self.play(rate.animate.set_value(3), run_time=1.5)
        self.play(Transform(m_lab, Tex('accepts').scale(0.8).set_color(EFFICIENT).next_to(rate_m, RIGHT, buff=0.35)))
        self.play(rate.animate.set_value(1.7), run_time=2)
        self.play(Transform(a_lab, Tex('rejects').scale(0.8).set_color(NASH).next_to(rate_a, RIGHT, buff=0.35)))
        self.play(rate.animate.set_value(3), run_time=1.5)
        self.play(Transform(a_lab, Tex('accepts').scale(0.8).set_color(EFFICIENT).next_to(rate_a, RIGHT, buff=0.35)))
        readout.clear_updaters()
        window_line = Tex('{{2}} $<$ exchange rate $<$ {{4}}').scale(0.9).set_color(DEFINITION).move_to(UP * 2.55)
        self.play(Transform(readout, window_line), FadeOut(box_m), FadeOut(box_a))
        self.pause()

        # B12 ---------------------------------------------------------
        # buying beats growing: both farmers go to their corners

        grow_m = Tex('Grow({{1}} {{C}}) $=$ {{4}} {{S}}').scale(0.7).set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH})
        buy_m = Tex('Trade({{1}} {{C}}) $=$ {{3}} {{S}}').scale(0.7).set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH})
        pair_m = VGroup(grow_m, buy_m).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(axm.c2p(7, 33))
        grow_a = Tex('Grow({{1}} {{S}}) $=$ {{1/2}} {{C}}').scale(0.7).set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH})
        buy_a = Tex('Trade({{1}} {{S}}) $=$ {{1/3}} {{C}}').scale(0.7).set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH})
        pair_a = VGroup(grow_a, buy_a).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(axa.c2p(6.5, 33))

        def choice_boxes(a, b, buff=0.18):
            w = max(a.get_width(), b.get_width()) + 2 * buff
            h = max(a.get_height(), b.get_height()) + 2 * buff
            return (Rectangle(width=w, height=h, color=NASH, stroke_width=2.5).move_to(a),
                    Rectangle(width=w, height=h, color=EFFICIENT, stroke_width=2.5).move_to(b))

        no_m, yes_m = choice_boxes(grow_m, buy_m)
        no_a, yes_a = choice_boxes(grow_a, buy_a)
        self.play(FadeIn(pair_m))
        self.play(FadeIn(yes_m))
        self.play(FadeIn(no_m))
        self.play(FadeIn(pair_a))
        self.play(FadeIn(yes_a), FadeIn(no_a))
        self.pause()

        # B12b --------------------------------------------------------
        # Molly's endowment slides: the line pivots with it, furthest at the corner

        choices = VGroup(pair_m, pair_a, no_m, yes_m, no_a, yes_a)
        self.play(FadeOut(choices))
        self.play(endow_m.animate.set_value(3), run_time=2.5)
        self.play(endow_m.animate.set_value(0), run_time=2.5)
        self.pause()

        # B12c --------------------------------------------------------

        self.play(endow_a.animate.set_value(4), run_time=2.5)
        self.play(endow_a.animate.set_value(8), run_time=2.5)
        for live in (tl_m, tl_a, em_dot, ea_dot):
            live.clear_updaters()
        for tr in (rate, endow_m, endow_a):
            self.remove(tr)
        self.pause()

        # B13 ---------------------------------------------------------

        stage_q1, card_q1 = exercise_card(self, 'Exercise A3 $|$ Q1', [
            'Suppose Hagrid and McGonagall decide they want to specialize and trade goods.',
            'After they specialize, what is a trade that would make them both better off?',
            '1 $R$ for $\\underline{\\hspace{1.2cm}}$ $F$',
        ])
        self.pause()

        # B14 ---------------------------------------------------------

        self.play(FadeOut(card_q1), Restore(stage_q1))
        recip_cap = (Tex(narration('Opportunity costs are reciprocals --- a workable exchange rate always exists.'))
                     .scale(0.8).set_color(CAPTION).move_to(UP * 2.55))
        self.play(Transform(readout, recip_cap))
        self.pause()

        # B15 ---------------------------------------------------------

        stage_q2, card_q2 = exercise_card(self, 'Exercise A3 $|$ Q2', [
            'It turns out McGonagall receives great enjoyment from her side gig as a baker',
            'and wants to double her hours.',
            "Set up McGonagall's old and new PPF on the same graph.",
            'What is her new opportunity cost of rock cakes ($R$)?',
            'Write a short description of how this would impact the trade you found in Q1.',
        ])
        self.pause()

        # B16 ---------------------------------------------------------
        # nothing special about these numbers: nudge both frontiers, the
        # rate-3 trade still works

        self.play(FadeOut(card_q2), Restore(stage_q2))
        ppf_m_new = axm.plot(lambda c: 44 - 4.4 * c, color=MOLLY, x_range=(0, 10))
        ppf_a_new = axa.plot(lambda c: 20 - 2.5 * c, color=ANDREW, x_range=(0, 8))
        tl_m_new = axm.plot(lambda c: 44 - 3 * c, color=TRADE, x_range=(0, 10.8))
        tl_a_new = axa.plot(lambda c: 3 * (8 - c), color=TRADE, x_range=(0, 8))
        self.play(Transform(ppf_m, ppf_m_new), Transform(ppf_a, ppf_a_new),
                  Transform(tl_m, tl_m_new), Transform(tl_a, tl_a_new),
                  Transform(em_dot, Dot(axm.c2p(0, 44), color=MOLLY, z_index=11)),
                  Transform(rate_m, under_axis(axm, rate_tex('Molly', '4.4'))),
                  Transform(rate_a, under_axis(axa, rate_tex('Andrew', '2.5'))),
                  run_time=2)
        self.pause()

        # B17 (cam) ----------------------------------------------------
        # "We've done something extraordinary here..." — no code; stage holds.

        # B18 ---------------------------------------------------------
        # the corner rides the PPF with a ? — where should we live?

        qmark = VGroup(Dot(axm.c2p(0, 44), color=FOCUS, z_index=12),
                       Tex('?').scale(0.9).set_color(FOCUS))
        qmark[1].next_to(qmark[0], UR, buff=0.1)
        self.play(FadeIn(qmark))
        self.play(qmark.animate.move_to(axm.c2p(5, 22) + UP * 0.15 + RIGHT * 0.15), run_time=2)
        self.play(qmark.animate.move_to(axm.c2p(0, 44) + UP * 0.15 + RIGHT * 0.15), run_time=2)
        self.pause()

        # B18b --------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        head = title('Two Questions')
        q1 = Tex('1. Where on the PPF should we live?').scale(SCALE_TITLE)
        q2 = Tex('2. Who benefits? How do we decide what exchange rate to set?').scale(SCALE_TITLE)
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        if qs.get_width() > FRAME_W - 3:               # rows scale to fit, never wrap (guide S3)
            qs.scale((FRAME_W - 3) / qs.get_width())
        qs.move_to(UP * 0.8)
        self.play(FadeIn(head))
        self.play(Write(q1))
        self.pause()

        # B18c --------------------------------------------------------

        self.play(Write(q2))
        self.pause()

        # B18d --------------------------------------------------------
        # every rate in the window splits the gains differently

        gloss = (Tex(narration("Close to 2 is Molly's dream deal. Close to 4 is Andrew's."))
                 .scale(0.8).set_color(CAPTION).next_to(qs, DOWN, buff=0.6).set_x(0))
        self.play(FadeIn(gloss))
        self.pause()

        # B19 ---------------------------------------------------------

        yes = Tex('YES!').scale(1.4).set_color(FOCUS).next_to(gloss, DOWN, buff=0.9).set_x(0)
        self.play(Write(yes))
        self.pause()

        # B20 ---------------------------------------------------------
        # the notes end here: Welcome is Part A's last word (no next-time card)

        FadeAll(self)
        welcome = Tex('Welcome! We have a lot to do.').scale(1.2)
        self.play(Write(welcome))
        self.pause()

        FadeAll(self)
