# maniml 03_Code.py EpisodeA3
#
# Episode A3 | Specializing and trading can make both parties better off
# One scene; beats follow 02_Storyboard.md (B01...B14c). Director's passes
# 2026-09-01/02: co-op recap opens after the history card; offers are POINTS
# with given-up/gained bars only (no trade lines, no connecting segment); the
# negotiation is one live tracker — the caption's decimals, the standing rate
# in the caption, and both offer points roll together as the deal changes
# (6 S -> 20 S -> 12 S for 4 C); Pareto improvement gets its own full-frame
# definition screen; the window inequality carries units (1 C for
# 2 S < x S < 4 S) and its bounds fly in from the boxed table entries. The
# stage-1 verbatim merge of the old scenes: _archive/03_Code_stage1_merge.py.

from manim import *
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, title(), bumper(), exercise_card(), ...
from style import axes as style_axes
from Video import PPF_Molly, PPF_Andrew, PPF_Coop

# The shared two-panel stage, from A2's B15 block (guide §1: shared centre).
PANEL_KWARGS = dict(
    x_range=[0, 11, 1], y_range=[0, 45, 5], x_length=4.6, y_length=4.3, ticks=True,
)
PANEL_DROP = DOWN * 0.45
NAME_Y = -3.20                 # the under-axis band: rate lines, accept/reject beneath


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
        Tex('Spinach').scale(SCALE_TICK).set_color(SPINACH).next_to(ax_.c2p(0, 45), UP, buff=0.15))


def under_axis(ax_, mob):
    """Park a line centred under a panel's x-axis (the A2 name/rate band)."""
    return mob.move_to(np.array([ax_.c2p(5.5, 0)[0], NAME_Y, 0]))


def rate_tex(name, s_num):
    """An under-axis stored-rate line: numerals INK, letters colored."""
    return Tex(f'{name}: {{{{1}}}} {{{{C}}}} $=$ {{{{{s_num}}}}} {{{{S}}}}').scale(0.9).set_color_by_tex_to_color_map({
        'C': CARROTS, 'S': SPINACH})


def autarky_marker(ax_, c, s):
    p = ax_.c2p(c, s)
    dot = Dot(p, color=INK, z_index=14)
    v = DashedLine(ax_.c2p(c, 0), p, color=MUTED)
    h = DashedLine(ax_.c2p(0, s), p, color=MUTED)
    lab = Tex(f'({c}, {s})').scale(SCALE_CAPTION).set_color(CAPTION).next_to(p, DL, buff=0.15)
    # the dot's z_index keeps it above the drop lines (maniml sorts
    # within groups, CE-style, since 2026-09-02)
    return VGroup(dot, lab, v, h)


def focus_box(*mobs, buff=0.2):
    return SurroundingRectangle(VGroup(*mobs), color=FOCUS, buff=buff, stroke_width=2.5)


def cost_entry(num, letter, color, scale=1.0):
    """Op-cost cell: numeral INK, letter colored (guide §0)."""
    return VGroup(Tex(num).set_color(INK), Tex(letter).set_color(color)).arrange(RIGHT, buff=0.15).scale(scale)


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
        # the history detour: out of feudalism, into mercantilism -- then what?

        FadeAll(self)
        hist = Tex('If not feudalism, then what?').scale(1.2).set_color(DEFINITION)
        self.play(Write(hist))
        self.pause()

        # B02b --------------------------------------------------------

        ricardo = (Tex(narration('--- David Ricardo, 1817')).scale(SCALE_CAPTION)
                   .set_color(CAPTION).next_to(hist, DOWN, buff=0.6).align_to(hist, RIGHT).shift(RIGHT * 1.2))
        self.play(FadeIn(ricardo))
        self.pause()

        # B03 ---------------------------------------------------------

        FadeAll(self)
        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B04 ---------------------------------------------------------
        # the co-op recap: the specialization point steps outside the line

        FadeAll(self)
        tech_line = (Tex('The choices themselves ARE the technology.')
                     .scale(0.9).set_color(DEFINITION).to_edge(UP, buff=0.5).set_x(0))
        axc = style_axes(
            x_range=[0, 19, 1], y_range=[0, 60, 5], x_length=6.2, y_length=5.2, ticks=True,
            x_axis_config={'numbers_to_include': [8, 10, 18],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [16, 40, 56],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        ).scale(0.9).move_to(RIGHT * 0.8 + DOWN * 0.5)
        cap_c = Tex('Carrots').scale(SCALE_CAPTION).set_color(CARROTS).next_to(axc.c2p(19, 0), RIGHT, buff=0.25)
        cap_s = Tex('Spinach').scale(SCALE_CAPTION).set_color(SPINACH).next_to(axc.c2p(0, 60), UP, buff=0.15)
        ppf_cm = axc.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        ppf_ca = axc.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        coop_line = axc.plot(PPF_Coop, color=GUILD, x_range=(0, 18))
        lab_cm = Tex('Molly').scale(SCALE_CAPTION).next_to(axc.c2p(0, 40), LEFT, buff=0.9)
        lab_ca = Tex('Andrew').scale(SCALE_CAPTION).next_to(axc.c2p(0, 16), LEFT, buff=0.9)
        lab_cc = Tex('Co-op').scale(SCALE_CAPTION).next_to(axc.c2p(0, 56), LEFT, buff=0.9)
        dm = Dot(axc.c2p(5, 20), color=MOLLY, z_index=10)
        da = Dot(axc.c2p(4, 8), color=ANDREW, z_index=10)
        dc = Dot(axc.c2p(9, 28), color=GUILD, z_index=10)
        glow_cm = Dot(axc.c2p(0, 40), radius=0.14, color=MOLLY).set_opacity(0.5)
        glow_ca = Dot(axc.c2p(8, 0), radius=0.14, color=ANDREW).set_opacity(0.5)
        self.play(Write(tech_line), FadeIn(axc), FadeIn(cap_c), FadeIn(cap_s),
                  FadeIn(ppf_cm), FadeIn(ppf_ca), FadeIn(coop_line),
                  FadeIn(lab_cm), FadeIn(lab_ca), FadeIn(lab_cc),
                  FadeIn(glow_cm), FadeIn(glow_ca),
                  FadeIn(dm), FadeIn(da), FadeIn(dc))
        self.pause()

        # B04b --------------------------------------------------------

        self.play(dm.animate.move_to(axc.c2p(0, 40)), da.animate.move_to(axc.c2p(8, 0)),
                  dc.animate.move_to(axc.c2p(8, 40)), run_time=3)
        self.play(Indicate(dc, color=FOCUS))
        self.pause()

        # B05 ---------------------------------------------------------
        # self-trade recap; the section title is Trade. The subtitle: the PPF
        # defines the terms of the self-trade. The specialization points glow.

        self.reset_frame()
        FadeAll(self)
        head = title('Trade')
        axm = molly_axes()
        axa = andrew_axes()
        caps_m, caps_a = panel_caps(axm), panel_caps(axa)
        ppf_m = axm.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        ppf_a = axa.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        rate_m = under_axis(axm, rate_tex('Molly', '4'))
        rate_a = under_axis(axa, rate_tex('Andrew', '2'))
        mark_m = autarky_marker(axm, 3, 28)
        mark_a = autarky_marker(axa, 4, 8)
        em_glow = Dot(axm.c2p(0, 40), radius=0.14, color=MOLLY, z_index=11).set_opacity(0.5)
        ea_glow = Dot(axa.c2p(8, 0), radius=0.14, color=ANDREW, z_index=11).set_opacity(0.5)
        self.play(FadeIn(head),
                  FadeIn(axm), FadeIn(caps_m), FadeIn(ppf_m), FadeIn(rate_m), FadeIn(mark_m),
                  FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(rate_a), FadeIn(mark_a),
                  FadeIn(em_glow), FadeIn(ea_glow))
        arrow_m = CurvedArrow(axm.c2p(0, 40), axm.c2p(3, 28), angle=-PI / 3, color=FOCUS)
        arrow_a = CurvedArrow(axa.c2p(8, 0), axa.c2p(4, 8), angle=PI / 3, color=FOCUS)
        self.play(Create(arrow_m), Create(arrow_a))
        terms = (Tex('The PPF defines the terms of the self-trade.')
                 .scale(0.85).set_color(DEFINITION).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Write(terms))
        self.pause()

        # B06 ---------------------------------------------------------
        # initial endowment: the QUIET white dot leaves its self-trade spot,
        # tries a few endowments along the PPF, returns to the specialization
        # point, and fades into the glow

        self.play(FadeOut(arrow_m), FadeOut(arrow_a), FadeOut(terms),
                  FadeOut(axa), FadeOut(caps_a), FadeOut(ppf_a), FadeOut(rate_a),
                  FadeOut(mark_a), FadeOut(ea_glow))
        cap = (definition('Initial Endowment', 'is how much of both goods Molly has.')
               .scale(0.9).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(Write(cap))

        def point_readout(ax_, c, sp, color=TRADE):
            p = ax_.c2p(c, sp)
            v = DashedLine(ax_.c2p(c, 0), p, color=MUTED)
            h = DashedLine(ax_.c2p(0, sp), p, color=MUTED)
            lab = VGroup(Tex('(').scale(SCALE_TICK),
                         DecimalNumber(c, num_decimal_places=1).scale(SCALE_TICK),
                         Tex(',').scale(SCALE_TICK),
                         DecimalNumber(sp, num_decimal_places=1).scale(SCALE_TICK),
                         Tex(')').scale(SCALE_TICK)).set_color(CAPTION)
            lab.arrange(RIGHT, buff=0.06).next_to(p, UR, buff=0.12)
            lab[2].align_to(lab[1], DOWN).shift(DOWN * 0.07)   # commas descend below the baseline
            # the dot's z_index keeps it above the drop lines
            return VGroup(Dot(p, radius=0.09, color=color, z_index=15), lab, v, h)

        e_tr = ValueTracker(3.0)

        def wander_draw():
            e = e_tr.get_value()
            return point_readout(axm, e, PPF_Molly(e), color=INK)

        wander = always_redraw(wander_draw)
        self.remove(mark_m)          # the readout takes over in the same frame:
        self.add(wander)             # same dot, same dashes -- no crossfade
        self.play(e_tr.animate.set_value(6), run_time=1.4)
        self.play(e_tr.animate.set_value(1), run_time=1.2)
        self.play(e_tr.animate.set_value(0), run_time=1.2)
        wander.clear_updaters()
        self.remove(e_tr)
        self.play(FadeOut(wander))
        self.pause()

        # B06b --------------------------------------------------------
        # the criterion, saved from the recap: a better deal than her self-trade

        hook = Tex("Molly will accept any trade that's a better deal than her self-trade.").scale(0.7).set_color(DEFINITION)
        if hook.get_width() > FRAME_W - 2:
            hook.scale((FRAME_W - 2) / hook.get_width())
        hook.next_to(head, DOWN, buff=0.28).set_x(0)
        self.play(FadeOut(cap), FadeIn(hook))
        self.pause()

        # B06c --------------------------------------------------------
        # Molly proposes ONE trade; the offer POINT grows out of her glow
        # with the given-up/gained bars -- no line, just point and bars

        prop_cap = Tex("{{Molly's proposal:}} {{6}} {{S}} for {{4}} {{C}}").scale(0.9).set_color_by_tex_to_color_map({
            "Molly's proposal:": DEFINITION, 'S': SPINACH, 'C': CARROTS,
        }).next_to(head, DOWN, buff=0.25).set_x(-1.2)
        self.play(FadeOut(hook), FadeIn(prop_cap))

        grow_t = ValueTracker(0.0)

        def molly_bars(c, sp):
            gain = Line(axm.c2p(0, 0), axm.c2p(max(c, 0.001), 0), color=CARROTS, stroke_width=6)
            give = Line(axm.c2p(0, sp), axm.c2p(0, 40), color=SPINACH, stroke_width=6)
            gain_n = (DecimalNumber(c, num_decimal_places=1, color=CARROTS).scale(SCALE_TICK)
                      .next_to(axm.c2p(c / 2, 0), DOWN, buff=0.25))
            give_n = (DecimalNumber(40 - sp, num_decimal_places=1, color=SPINACH).scale(SCALE_TICK)
                      .next_to(axm.c2p(0, (sp + 40) / 2), LEFT, buff=0.25))
            return VGroup(gain, give, gain_n, give_n)

        def molly_offer_draw():
            t = grow_t.get_value()
            c, sp = 4 * t, 40 - 6 * t
            return VGroup(point_readout(axm, c, sp), molly_bars(c, sp))

        offer_m = always_redraw(molly_offer_draw)
        self.add(offer_m)
        self.bring_to_front(em_glow)
        self.play(grow_t.animate.set_value(1), run_time=3)
        offer_m.clear_updaters()
        self.remove(grow_t)
        self.pause()

        # B06d --------------------------------------------------------
        # the exchange rate: set the sides equal, solve on screen; the result
        # files into the caption -- and the point is outside her PPF: accepts

        equal = Tex('=').scale(1.2).move_to(RIGHT * 3.9 + UP * 0.8)

        def c_tex(t):
            return Tex(f'{{{{{t}}}}} {{{{C}}}}').scale(1.2).next_to(equal, LEFT, buff=0.6).set_color_by_tex_to_color_map({'C': CARROTS})

        def s_tex(t):
            return Tex(f'{{{{{t}}}}} {{{{S}}}}').scale(1.2).next_to(equal, RIGHT, buff=0.6).set_color_by_tex_to_color_map({'S': SPINACH})

        c_side = c_tex('4')
        s_side = s_tex('6')
        self.play(FadeIn(c_side), FadeIn(equal), FadeIn(s_side))
        self.play(Transform(c_side, c_tex(r'$\frac{4}{4}$')), Transform(s_side, s_tex(r'$\frac{6}{4}$')))
        self.play(Transform(c_side, c_tex('1')), Transform(s_side, s_tex('1.5')))
        eq_group = VGroup(c_side, equal, s_side)
        cap_par = (Tex('(Rate: {{1}} {{C}} $=$ {{1.5}} {{S}})').scale(0.65)
                   .set_color_by_tex_to_color_map({'S': SPINACH, 'C': CARROTS})
                   .next_to(prop_cap, RIGHT, buff=0.25).align_to(prop_cap, DOWN).shift(UP * 0.05))
        self.play(Transform(eq_group, cap_par))
        cap = VGroup(prop_cap, eq_group)
        # -- predict beat: would Molly accept this deal? --
        self.pause()
        m_lab = Tex('accepts').scale(0.7).set_color(EFFICIENT).next_to(rate_m, DOWN, buff=0.15)
        self.play(FadeIn(m_lab))
        self.pause()

        # B06e --------------------------------------------------------
        # the same offer from Andrew's side: Molly's panel steps back, the
        # caption stays; only his GLOWING red specialization point -- and the
        # offer point grows in, landing INSIDE his PPF

        molly_stage = VGroup(axm, caps_m, ppf_m, rate_m, em_glow, offer_m, m_lab)
        self.play(FadeOut(molly_stage),
                  FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(rate_a), FadeIn(ea_glow))

        grow_ta = ValueTracker(0.0)

        def andrew_bars(c, sp):
            give = Line(axa.c2p(c, 0), axa.c2p(8, 0), color=CARROTS, stroke_width=6)
            gain = Line(axa.c2p(0, 0), axa.c2p(0, max(sp, 0.001)), color=SPINACH, stroke_width=6)
            give_n = (DecimalNumber(8 - c, num_decimal_places=1, color=CARROTS).scale(SCALE_TICK)
                      .next_to(axa.c2p((c + 8) / 2, 0), DOWN, buff=0.25))
            gain_n = (DecimalNumber(sp, num_decimal_places=1, color=SPINACH).scale(SCALE_TICK)
                      .next_to(axa.c2p(0, sp / 2), LEFT, buff=0.25))
            return VGroup(give, gain, give_n, gain_n)

        def andrew_offer_draw():
            t = grow_ta.get_value()
            c, sp = 8 - 4 * t, 6 * t
            return VGroup(point_readout(axa, c, sp), andrew_bars(c, sp))

        offer_a = always_redraw(andrew_offer_draw)
        self.add(offer_a)
        self.bring_to_front(ea_glow)
        self.play(grow_ta.animate.set_value(1), run_time=3)
        offer_a.clear_updaters()
        self.remove(grow_ta)
        # -- predict beat: would Andrew accept the same deal? --
        self.pause()
        a_lab = Tex('rejects').scale(0.7).set_color(NASH).next_to(rate_a, DOWN, buff=0.15)
        self.play(FadeIn(a_lab))
        self.pause()

        # B07 ---------------------------------------------------------
        # Andrew counters. ONE live tracker: the caption's decimals and both
        # offer points roll together from 6 S to 24 S (rate 1.5 -> 6; at rate 5
        # both offer points would coincide at (4, 20) -- notes swap flagged)

        self.play(FadeIn(molly_stage))

        s_amt = ValueTracker(6.0)
        live_lab = Tex("Andrew's counter:").scale(0.9).set_color(DEFINITION)
        live_amt = DecimalNumber(6, num_decimal_places=1, color=INK).scale(0.9)
        live_mid = Tex('{{S}} for {{4}} {{C}}').scale(0.9).set_color_by_tex_to_color_map({'S': SPINACH, 'C': CARROTS})
        live_par = Tex('(Rate: {{1}} {{C}} $=$').scale(0.65).set_color_by_tex_to_color_map({'C': CARROTS})
        live_rate = DecimalNumber(1.5, num_decimal_places=1, color=INK).scale(0.65)
        live_tail = Tex('{{S}})').scale(0.65).set_color_by_tex_to_color_map({'S': SPINACH})
        live_cap = VGroup(live_lab, live_amt, live_mid, live_par, live_rate, live_tail)
        live_cap.arrange(RIGHT, buff=0.2).next_to(head, DOWN, buff=0.25).set_x(0)
        baseline = live_mid.get_bottom()[1]

        def sit(m, dy=0.0):
            m.shift(UP * (baseline - m.get_bottom()[1] + dy))
            return m

        for piece in (live_amt, live_par, live_rate, live_tail):
            sit(piece, -0.03 if piece in (live_par, live_tail) else 0.0)
        live_amt.add_updater(lambda m: sit(m.set_value(s_amt.get_value()).next_to(live_lab, RIGHT, buff=0.2)))
        live_mid.add_updater(lambda m: sit(m.next_to(live_amt, RIGHT, buff=0.2)))
        live_par.add_updater(lambda m: sit(m.next_to(live_mid, RIGHT, buff=0.3), -0.03))
        live_rate.add_updater(lambda m: sit(m.set_value(s_amt.get_value() / 4).next_to(live_par, RIGHT, buff=0.18), 0.02))
        live_tail.add_updater(lambda m: sit(m.next_to(live_rate, RIGHT, buff=0.12), -0.03))

        def molly_live_draw():
            s = s_amt.get_value()
            return VGroup(point_readout(axm, 4, 40 - s), molly_bars(4, 40 - s))

        def andrew_live_draw():
            s = s_amt.get_value()
            return VGroup(point_readout(axa, 4, s), andrew_bars(4, s))

        self.remove(offer_m, offer_a)
        molly_stage.remove(offer_m)
        live_m = always_redraw(molly_live_draw)
        live_a = always_redraw(andrew_live_draw)
        self.add(live_m, live_a)
        self.bring_to_front(em_glow, ea_glow)
        self.play(FadeOut(cap), FadeIn(live_cap))
        self.play(s_amt.animate.set_value(24), run_time=3)
        # -- predict beat: who accepts at this rate? --
        self.pause()
        self.play(Transform(a_lab, Tex('accepts').scale(0.7).set_color(EFFICIENT).next_to(rate_a, DOWN, buff=0.15)),
                  Transform(m_lab, Tex('rejects').scale(0.7).set_color(NASH).next_to(rate_m, DOWN, buff=0.15)))
        self.pause()

        # B08 ---------------------------------------------------------
        # Molly counters in the middle: the numbers roll to 12 S (rate 3)

        self.play(Transform(live_lab, Tex("Molly's counter:").scale(0.9).set_color(DEFINITION)
                            .align_to(live_lab, RIGHT).align_to(live_lab, DOWN).shift(DOWN * 0.08)))
        self.play(s_amt.animate.set_value(12), run_time=3)
        # -- predict beat: and now? --
        self.pause()
        self.play(Transform(m_lab, Tex('accepts').scale(0.7).set_color(EFFICIENT).next_to(rate_m, DOWN, buff=0.15)))
        self.pause()

        # B08b --------------------------------------------------------
        # both accept -> the offer points retire to the specialization points
        # and the definition gets its own screen

        for piece in (live_amt, live_mid, live_par, live_rate, live_tail):
            piece.clear_updaters()
        live_m.clear_updaters()
        live_a.clear_updaters()
        self.remove(s_amt)
        self.play(FadeOut(live_m), FadeOut(live_a))
        scene_stage = VGroup(*[m for m in self.mobjects if isinstance(m, VMobject)])
        scene_stage.save_state()
        self.play(FadeOut(scene_stage))
        pareto = definition('Pareto improvement', 'is a trade that makes both parties better off.')
        self.play(Write(pareto))
        self.pause()

        # B08c --------------------------------------------------------
        # back in at the specialization points; the deal is now named

        self.play(FadeOut(pareto))
        self.play(Restore(scene_stage))
        self.play(Transform(live_lab, Tex('Pareto Improvement:').scale(0.9).set_color(DEFINITION)
                            .align_to(live_lab, RIGHT).align_to(live_lab, DOWN).shift(DOWN * 0.02)))
        self.pause()

        # B09 ---------------------------------------------------------
        # the big trade at rate 3: the autarky benchmarks return, and the
        # riders run from the specialization points -- better in BOTH goods

        mark_m = autarky_marker(axm, 3, 28)
        mark_a = autarky_marker(axa, 4, 8)
        self.play(FadeIn(mark_m), FadeIn(mark_a))
        self.pause()

        # B09b --------------------------------------------------------
        # the riders run the big trade from the specialization points, with
        # dashes, live readouts, and the traded amounts on the axes

        bt = ValueTracker(0.0)

        def rider_m_draw():
            t = bt.get_value()
            return VGroup(point_readout(axm, 3.5 * t, 40 - 10.5 * t), molly_bars(3.5 * t, 40 - 10.5 * t))

        def rider_a_draw():
            t = bt.get_value()
            return VGroup(point_readout(axa, 8 - 3.5 * t, 10.5 * t), andrew_bars(8 - 3.5 * t, 10.5 * t))

        rider_m = always_redraw(rider_m_draw)
        rider_a = always_redraw(rider_a_draw)
        self.add(rider_m, rider_a)
        self.bring_to_front(em_glow, ea_glow)
        self.play(bt.animate.set_value(1), run_time=3)
        rider_m.clear_updaters()
        rider_a.clear_updaters()
        self.remove(bt)
        self.play(Indicate(rider_m[0][0], color=FOCUS), Indicate(rider_a[0][0], color=FOCUS))
        noco = (Tex("We've specialized, traded, and improved with no co-op!")
                .scale(0.85).set_color(DEFINITION).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(FadeOut(live_cap), FadeIn(noco))
        self.pause()

        # B10 ---------------------------------------------------------

        self.drop_frame()            # trackers and camera frames would break the card's stage grab
        stage_q2, card_q2 = exercise_card(self, 'Exercise A3 $|$ Q2', [
            'Suppose Hagrid and McGonagall decide they want to specialize and trade goods.',
            'After they specialize, what is a trade that would make them both better off?',
            '1 $R$ for $\\underline{\\hspace{1.2cm}}$ $F$',
        ])
        self.pause()

        # B11 ---------------------------------------------------------
        # finding rates that improve both sides: the op-cost table, centred

        self.play(FadeOut(card_q2), Restore(stage_q2))
        self.reset_frame()
        FadeAll(self)
        head = title('Trade')
        table_q = (Tex('How do we find exchange rates that improve both sides?')
                   .scale(0.85).set_color(DEFINITION).next_to(head, DOWN, buff=0.25).set_x(0))
        cost = Table(
            [[cost_entry('4', 'S', SPINACH), cost_entry('1/4', 'C', CARROTS)],
             [cost_entry('2', 'S', SPINACH), cost_entry('1/2', 'C', CARROTS)]],
            row_labels=[Tex('Molly').set_color(MOLLY), Tex('Andrew').set_color(ANDREW)],
            col_labels=[Tex('Carrots').set_color(CARROTS), Tex('Spinach').set_color(SPINACH)],
            line_config={'color': MUTED},
        ).scale(0.8).move_to(UP * 0.4)
        self.play(FadeIn(head), Write(table_q))
        self.play(FadeIn(cost))
        self.pause()

        # B11b --------------------------------------------------------
        # the bounds fly in from the boxed entries, one piece at a time:
        # 1 C   for   2 S < x S < 4 S

        box_m = focus_box(cost.get_entries()[3])
        box_a = focus_box(cost.get_entries()[6])
        self.play(FadeIn(box_m))
        self.play(FadeIn(box_a))
        lead_c = Tex('{{1}} {{C}}').set_color_by_tex_to_color_map({'C': CARROTS})
        lead_for = Tex('for')
        lo = cost_entry('2', 'S', SPINACH)
        lt1 = Tex('$<$')
        mid_x = VGroup(Tex('$x$').set_color(INK), Tex('S').set_color(SPINACH)).arrange(RIGHT, buff=0.15)
        lt2 = Tex('$<$')
        hi = cost_entry('4', 'S', SPINACH)
        ineq = VGroup(lead_c, lead_for, lo, lt1, mid_x, lt2, hi).arrange(RIGHT, buff=0.5).next_to(cost, DOWN, buff=0.9)
        self.play(FadeIn(lead_c))
        self.play(FadeIn(lead_for))
        fly_lo = cost.get_entries()[6].copy()
        self.play(Transform(fly_lo, lo), run_time=1.2)
        self.play(FadeIn(lt1))
        self.play(FadeIn(mid_x))
        self.play(FadeIn(lt2))
        fly_hi = cost.get_entries()[3].copy()
        self.play(Transform(fly_hi, hi), run_time=1.2)
        self.pause()

        # B12 ---------------------------------------------------------

        recip_cap = (Tex(narration('Opportunity costs are always reciprocals. A workable exchange rate always exists.'))
                     .scale(0.8).set_color(CAPTION).to_edge(DOWN, buff=0.45).set_x(0))
        self.play(Write(recip_cap))
        self.pause()

        # B13 ---------------------------------------------------------

        stage_q3, card_q3 = exercise_card(self, 'Exercise A3 $|$ Q3', [
            'Not every exchange rate works for both bakers.',
            'What is the range of exchange rates that would make both Hagrid and McGonagall better off?',
            'Between $\\underline{\\hspace{1.2cm}}$ and $\\underline{\\hspace{1.2cm}}$ $F$ per $1$ $R$',
        ])
        self.pause()

        # B14 ---------------------------------------------------------
        # the two questions; Welcome is Part A's last word, same screen

        self.play(FadeOut(card_q3), Restore(stage_q3))
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

        # B14b --------------------------------------------------------

        self.play(Write(q2))
        self.pause()

        # B14c --------------------------------------------------------

        welcome = (Tex('Welcome! We have a lot to do.').scale(1.1)
                   .set_color(DEFINITION).next_to(qs, DOWN, buff=1.1).set_x(0))
        self.play(Write(welcome))
        self.pause()

        FadeAll(self)
