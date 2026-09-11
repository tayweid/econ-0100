# maniml 03_Code.py EpisodeB0
#
# Episode B0 | Coordination can be done through prices
# Graphite port (2026-09-08) of the Fall-2024 scenes; director's passes
# 2026-09-09: opens on the Last Time card; the PPF sits under a subtitled
# Part A title (guide title() idiom) and the bow-out lands as Part A's
# core idea with its thesis line in gold beneath the graph; no camera
# moves — the subtitled Part B column slides in from the right, then the
# questions key in (white, question-marked) in 01_Notes.md's finalized
# order: Which point -> Coordinate large groups -> Who benefits. The
# raster bumper closes the episode as the part-title reveal — label is
# just 'Part B' (no episode number), kept at the left edge of where the
# full label would sit — and the last card cues the demand simulation
# (no card text existed in the reference code; the chocolate-bar question
# is the fallback agreed in chat). Verbatim original:
# _archive/03_Code_fall2024.py.

from manim import *
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, bumper pieces, exercise_card(), FadeAll()
from style import axes as style_axes


def key_in(tex, time_per_char=0.05):
    """Letter-by-letter reveal: ShowIncreasingSubsets over the Tex's glyphs.
    (maniml's AddTextLetterByLetter is an unexported alias of the word-wise
    add, and Write is the stroke-drawing creation look — neither keys in.)"""
    glyphs = VGroup(*tex.family_members_with_points())
    return ShowIncreasingSubsets(glyphs, run_time=time_per_char * len(glyphs), rate_func=linear)


class EpisodeB0(Scene):
    """Episode B0 | Markets. One flat construct(); each `# Bxx` section is
    self-contained and ends at the pause() the viewer parks on."""

    def construct(self):

        # B01 ---------------------------------------------------------
        # the Fall-2024 'Animation -1'

        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B02 ---------------------------------------------------------
        # the Part A stage: guide title with subtitle, the PPF close under it

        FadeAll(self)
        self.camera.frame.set(width=15).move_to(LEFT * 0.5)   # framed in a touch on Part A
        part_a = title('Part A')
        part_a_sub = subtitle(part_a, 'The core economic idea.')

        ax = style_axes(x_range=[0, 100, 100], y_range=[0, 100, 100],
                        x_length=7, y_length=7).scale(0.7).move_to(LEFT * 4.5 + DOWN * 0.3)
        y_label = Tex('A').set_color(INK).next_to(ax.c2p(0, 100), LEFT, buff=0.3)
        x_label = Tex('B').set_color(INK).next_to(ax.c2p(100, 0), RIGHT, buff=0.3)

        alpha = ValueTracker(1)

        def Linear_PPF(x):
            return 100 - x

        def Bowed_PPF(x):
            a = alpha.get_value()
            return (100**a - x**a)**(1 / a)

        def PPF_Group():
            linear_ppf = ax.plot(Linear_PPF, color=MUTED, x_range=(0, 100))
            linear_ppf.z_index = -1
            # the frontier that bows past the line is the gain from coordinating
            bowed_ppf = ax.plot(Bowed_PPF, color=TRADE, x_range=(0, 100, 0.1))
            bowed_ppf.z_index = -1
            return VGroup(linear_ppf, bowed_ppf)

        # fade in a still copy — always_redraw would repaint at full opacity
        # mid-fade (the FadeAll gotcha) and snap in instead of fading
        ppf_static = PPF_Group()
        self.play(FadeIn(part_a), FadeIn(part_a_sub), FadeIn(ax),
                  FadeIn(y_label), FadeIn(x_label), FadeIn(ppf_static))
        self.pause()

        # B02b --------------------------------------------------------
        # Part A's core idea: coordination bows the frontier out; the arrow
        # sits in the opening gap, the thesis lands in gold under the graph

        ppf_group = always_redraw(PPF_Group)   # live from here; at alpha=1 it matches the still
        self.remove(ppf_static)
        self.add(ppf_group)
        arrow = Arrow(start=ax.c2p(45, 56), end=ax.c2p(57, 67), buff=0).set_color(FOCUS)
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

        # B04 ---------------------------------------------------------
        # first question: two options on the frontier, which do we like?

        x1 = 30
        p1 = ax.coords_to_point(x1, Bowed_PPF(x1))
        dot1 = Dot(p1).set_color(INK)
        dot1_l = Tex('Option 1').next_to(dot1, RIGHT).set_color(DEFINITION)

        x2 = 80
        p2 = ax.coords_to_point(x2, Bowed_PPF(x2))
        dot2 = Dot(p2).set_color(INK)
        dot2_l = Tex('Option 2').next_to(dot2, UP + RIGHT).set_color(DEFINITION)

        self.play(FadeIn(dot1), FadeIn(dot1_l), key_in(questions[0]))
        self.play(FadeIn(dot2), FadeIn(dot2_l))
        self.pause()

        # B05 ---------------------------------------------------------
        # second question: coordination at scale

        self.play(key_in(questions[1]))
        self.pause()

        # B05b --------------------------------------------------------
        # ...and its other face: who benefits

        self.play(key_in(questions[2]))
        self.pause()

        # B06 ---------------------------------------------------------
        # the raster bumper closes the episode as the part-title reveal

        FadeAll(self)
        squares = bumper_raster(self)

        # B06b --------------------------------------------------------

        flicker(self, squares)

        # B06c --------------------------------------------------------
        # the part label, written in: 'Part B | Competitive Markets',
        # centred under the wordmark with the thesis beneath

        label = (Tex('{{Part B}} $|$ Competitive Markets').set_color(CAPTION)
                 .set_color_by_tex_to_color_map({'Part B': TITLE}).scale(2.2)
                 .move_to(DOWN * 0.9))
        self.play(AddTextWordByWord(label), squares.animate.move_to(UP * 0.9))
        flicker(self, squares)
        thesis = (Tex('\\textit{Competitive markets can coordinate decisions.}')
                  .scale(1.1).set_color(CAPTION).next_to(label, DOWN, buff=0.5))
        self.play(AddTextWordByWord(thesis))
        self.pause()

        # B07 ---------------------------------------------------------
        # cut to the demand simulation

        exercise_card(self, 'Simulation B $|$ Demand',
                      ['How much are you willing to pay for a chocolate bar?'])
        self.wait(1 / 2)     # let the head's Write settle before the export's parked frame
        self.pause()
