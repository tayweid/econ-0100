# maniml 03_Code.py EpisodeA2
#
# Episode A2 | Better choices alone can increase what's possible
# One scene; beats follow 02_Storyboard.md (B00...B18). Every animation from
# the old animation_0..4 (and A3's pulled-forward gains/self-trade scenes)
# survives here, renumbered. The table-building and advantage stretches are
# ported beat-for-beat from the old animation_2 / animation_3 (same play
# order, same box travel, same camera moves) on the new numbers.

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

# Guide §1 (vertical centering): body content is centred in the band between the
# title and the reserved bottom strip, and peer objects — the farm-card column
# and the co-op graph — share that one centre.
BODY_TOP = 2.95        # clears a title at to_edge(UP, buff=0.4)
BODY_BOTTOM = -2.85    # top of the reserved bottom strip (math rows, stored lines)
BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2

# The farm column lives in the left margin: small enough that a title clears it
# at the top and a bottom-edge line clears it below. Its two cards straddle
# BODY_MID, so the column and the graph read as one body block.
FARM = 2.2
FARM_GAP = 0.55
FARM_X = LEFT * 5.75
MOLLY_AT = FARM_X + UP * (BODY_MID + (FARM + FARM_GAP) / 2)
ANDREW_AT = FARM_X + UP * (BODY_MID - (FARM + FARM_GAP) / 2)

# The office-hours photo: pre-rounded (alpha baked in) because maniml's
# ImageMobject cannot be masked. See _Assets/Max_Photos/.
OFFICE_PHOTO = os.path.join(os.path.dirname(__file__),
                            '../_Assets/Max_Photos/2026_08_31_rounded.png')


def farm_cards():
    """The two farm cards: outlines with rotated names along the outside-left edge."""
    molly = Rectangle(height=FARM, width=FARM, color=MOLLY).move_to(MOLLY_AT)
    molly.z_index = 2
    molly_name = Tex('Molly').scale(0.85).set_color(MOLLY).rotate(PI / 2).next_to(molly, LEFT, buff=0.12)
    andrew = Rectangle(height=FARM, width=FARM, color=ANDREW).move_to(ANDREW_AT)
    andrew.z_index = 2
    andrew_name = Tex('Andrew').scale(0.85).set_color(ANDREW).rotate(PI / 2).next_to(andrew, LEFT, buff=0.12)
    return VGroup(molly, molly_name), VGroup(andrew, andrew_name)


def split(anchor, frac_c):
    """Crop fill for a farm card: carrots on top, spinach below, split by the
    fraction of land planted in carrots."""
    c = Rectangle(height=max(FARM * frac_c, 0.002), width=FARM, color=CARROTS,
                  fill_opacity=1, stroke_width=0)
    s = Rectangle(height=max(FARM * (1 - frac_c), 0.002), width=FARM, color=SPINACH,
                  fill_opacity=1, stroke_width=0)
    return VGroup(c, s.next_to(c, DOWN, buff=0)).move_to(anchor)


def focus_box(*mobs, buff=0.2):
    return SurroundingRectangle(VGroup(*mobs), color=FOCUS, buff=buff, stroke_width=2.5)


def trail_behind(point_func, color, width=4):
    """A non-dissipating traced path (maniml has no `TracedPath`): a polyline
    that grows a corner per frame wherever `point_func` has been. Call
    `clear_updaters()` to freeze it before fading or swapping it out."""
    pts = [np.array(point_func(), dtype=float)]
    path = VMobject(stroke_color=color, stroke_width=width)
    path.set_points_as_corners([pts[0], pts[0]])

    def grow(mob, dt=0):
        p = np.array(point_func(), dtype=float)
        if np.linalg.norm(p - pts[-1]) > 1e-4:
            pts.append(p)
            mob.set_points_as_corners(pts)

    path.add_updater(grow)
    return path


class Derivation:
    """A one-line derivation whose LETTERS never move and never re-render.

    Layout is `[numeral] C  =  [numeral] S`: the separator sits at `at`, each
    good's letter is pinned a fixed distance from it, and each numeral hangs to
    the LEFT of its own letter with its right edge anchored — so a step that
    widens a numeral (`10` -> `10/10`) grows leftward and nothing else stirs.
    Guide §0 (words as glyphs): the numerals are INK, only the letters carry
    the goods' colors. `step()` returns the animations for one algebra move,
    which touch the numerals and nothing else."""

    def __init__(self, at, left_num, left_letter, right_num, right_letter,
                 sep='=', scale=1.2, sep_gap=0.8, num_room=0.75, num_gap=0.2,
                 left_color=CARROTS, right_color=SPINACH):
        self.scale_f = scale
        self.num_gap = num_gap
        self.sep = Tex(sep).scale(scale).move_to(at)
        self.lL = (Tex(left_letter).scale(scale).set_color(left_color)
                   .next_to(self.sep, LEFT, buff=sep_gap))
        # the right letter stands off far enough that its numeral fits between
        # it and the separator without either of them ever moving
        self.lR = (Tex(right_letter).scale(scale).set_color(right_color)
                   .next_to(self.sep, RIGHT, buff=sep_gap + num_room + num_gap))
        self.nL = self._num(left_num, self.lL)
        self.nR = self._num(right_num, self.lR)
        self.group = VGroup(self.nL, self.lL, self.sep, self.nR, self.lR)

    def _num(self, txt, letter):
        return (Tex(txt).scale(self.scale_f).set_color(INK)
                .next_to(letter, LEFT, buff=self.num_gap))

    def step(self, left_num, right_num):
        """Animations for one algebra step — only the numerals re-render."""
        return [Transform(self.nL, self._num(left_num, self.lL)),
                Transform(self.nR, self._num(right_num, self.lR))]


def coop_axes():
    """The shared co-op graph: carrots horizontal, spinach vertical. The whole
    figure is then centred on BODY_MID, the band centre it shares with the
    farm-card column (guide §1)."""
    ax = style_axes(
        x_range=[0, 19, 1], y_range=[0, 60, 5], x_length=6.2, y_length=5.8, ticks=True,
        x_axis_config={'numbers_to_include': [8, 10, 18],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        y_axis_config={'numbers_to_include': [16, 40, 56],
                       'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
    ).scale(0.85).shift(RIGHT * 3.0)
    # captions sit off the ENDS of their axes so they never land on a tick numeral
    cap_c = Tex('Carrots').scale(SCALE_CAPTION).set_color(CARROTS).next_to(ax.c2p(19, 0), RIGHT, buff=0.25)
    cap_s = Tex('Spinach').scale(SCALE_CAPTION).set_color(SPINACH).next_to(ax.c2p(0, 60), RIGHT, buff=0.2)
    figure = VGroup(ax, cap_c, cap_s)
    figure.shift(UP * (BODY_MID - figure.get_center()[1]))
    return ax, VGroup(cap_c, cap_s)


def coop_curves(ax):
    ppf_m = ax.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
    ppf_a = ax.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
    lab_m = Tex('Molly').scale(SCALE_CAPTION).next_to(ax.c2p(0, 40), LEFT, buff=0.9)
    lab_a = Tex('Andrew').scale(SCALE_CAPTION).next_to(ax.c2p(0, 16), LEFT, buff=0.9)
    return ppf_m, ppf_a, lab_m, lab_a


def coop_label(ax):
    """`Co-op` + its qualifier, parked in the empty wedge above the co-op line."""
    lab_c = Tex('Co-op').scale(SCALE_CAPTION).next_to(ax.c2p(0, 56), LEFT, buff=0.9)
    lab_c_sub = (Tex(narration('(no specialization)')).scale(SCALE_TICK).set_color(CAPTION)
                 .next_to(lab_c, DOWN, buff=0.12).align_to(lab_c, RIGHT))
    return lab_c, lab_c_sub


def production_table(scale=0.7, head_scale=0.8):
    t = Table(
        [['10', '40'], ['8', '16']],
        row_labels=[Tex('Molly').set_color(MOLLY), Tex('Andrew').set_color(ANDREW)],
        col_labels=[Tex('Carrots').set_color(CARROTS), Tex('Spinach').set_color(SPINACH)],
        element_to_mobject=Tex, line_config={'color': MUTED},
    ).scale(scale)
    head = Tex("{{Production Table}}: Farmers' Capacities").set_color_by_tex_to_color_map({
        'Production Table': DEFINITION}).scale(head_scale).next_to(t, UP, buff=0.4)
    return t, VGroup(t, head)


GOOD_COLOR = {'C': CARROTS, 'S': SPINACH}


def cost_entry(spec):
    """One opportunity-cost entry, built as two mobjects: the numeral in INK and
    the good's letter in the good's color (guide §0 — the colored LETTER is the
    illustration; a numeral is never a good). `entry[0]` is the numeral and
    `entry[1]` the letter, which is what `light()` relies on."""
    num, letter = spec.split()
    return VGroup(Tex(num).set_color(INK),
                  Tex(letter).set_color(GOOD_COLOR[letter])).arrange(RIGHT, buff=0.15)


def light(entry, color):
    """Animations that bring a BG-painted cost entry back to its own colors:
    the numeral to INK, the letter to its good's color."""
    return [entry[0].animate.set_color(INK), entry[1].animate.set_color(color)]


def cost_table(scale=0.7, head_scale=0.8):
    """All four cost entries start painted BG and light up on their beat (the
    old animation_2 trick, kept)."""
    t = Table(
        [['4 S', '1/4 C'], ['2 S', '1/2 C']],
        row_labels=[Tex('Molly').set_color(MOLLY), Tex('Andrew').set_color(ANDREW)],
        col_labels=[Tex('Carrots').set_color(CARROTS), Tex('Spinach').set_color(SPINACH)],
        element_to_mobject=cost_entry, line_config={'color': MUTED},
    ).scale(scale)
    for e in (3, 4, 6, 7):
        t.get_entries()[e].set_color(BG)
    head = Tex("{{Op. Cost Table}}: Farmers' Costs").set_color_by_tex_to_color_map({
        'Op. Cost Table': DEFINITION}).scale(head_scale).next_to(t, UP, buff=0.4)
    return t, VGroup(t, head)


class EpisodeA2(Scene):
    """Episode A2 | Better choices alone can increase what's possible.

    One flat construct(). Each `# Bxx` section is self-contained: it clears
    the previous beat's objects, builds its own, and ends at the pause()
    the viewer parks on before the next section.
    """

    def reset_frame(self):
        """Camera home. Called before every FadeAll transition (A1's B10 idiom)."""
        self.camera.frame.move_to(ORIGIN).set(width=FRAME_W)
        self.drop_frame()

    def drop_frame(self):
        """Take camera frames back out of scene.mobjects.

        maniml seeds `scene.mobjects` with the CameraFrame and every
        `play(camera.frame.animate...)` puts one back (checkpoint replay can
        leave more than one identity behind). They are bare Mobjects, so a
        later `exercise_card()` — which wraps `VGroup(*scene.mobjects)` — would
        raise. Animating the camera still works: `play` re-adds as needed.
        `ImageMobject` is a bare Mobject too and is spared: B00's photo has to
        stay on stage long enough to be faded out."""
        for m in list(self.mobjects):
            if not isinstance(m, (VMobject, ImageMobject)):
                self.remove(m)

    def construct(self):

        # B00 ---------------------------------------------------------
        # housekeeping card before the bumper: the photo takes the right half
        # with equal top/right/bottom margins, so its height IS the frame's
        # minus two margins and it reads as belonging to the frame; the words
        # take the left half, vertically centred with it (guide §1)

        MARGIN = 0.6
        photo = ImageMobject(OFFICE_PHOTO, height=FRAME_HEIGHT - 2 * MARGIN)
        photo.move_to(np.array([FRAME_W / 2 - MARGIN - photo.get_width() / 2, 0, 0]))
        invite = Tex('Come to office hours :)').scale(SCALE_TITLE).set_color(TITLE)
        hours = Tex(narration('2:30 \\textendash\\ 3:30 Wed/Thurs')).scale(SCALE_BODY).set_color(CAPTION)
        card = VGroup(invite, hours).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        card.move_to(np.array([(-FRAME_W / 2 + photo.get_left()[0]) / 2, 0, 0]))
        self.play(FadeIn(photo), FadeIn(card))
        self.pause()

        # B01 ---------------------------------------------------------

        self.drop_frame()          # the camera frame only; the photo is spared
        FadeAll(self)
        squares = bumper_raster(self)

        # B01b --------------------------------------------------------

        flicker(self, squares)

        # B01c --------------------------------------------------------

        label = bumper_title(self, squares, 'A', 2)
        thesis = Tex("\\textit{Better choices alone can increase what's possible.}").scale(1.2).set_color(CAPTION).next_to(label, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause()

        # B02 ---------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B03 ---------------------------------------------------------

        self.play(FadeOut(last_card), run_time=1 / 2)
        molly_grp, andrew_grp = farm_cards()
        self.play(FadeIn(molly_grp))
        self.play(FadeIn(andrew_grp))
        self.pause()

        # B04 ---------------------------------------------------------

        prod, prod_grp = production_table()
        # centred on BODY_MID with the farm column, nudged up by half the space
        # the Absolute Advantage label takes below it at B04c (guide §1)
        prod_grp.move_to(RIGHT * 1.4 + UP * (BODY_MID + 0.45))
        self.play(FadeIn(prod_grp))
        self.pause()

        # B04b --------------------------------------------------------
        # animation_3's rhythm: the stage clears for a full-frame definition card

        aa_def = definition('Absolute Advantage', 'is having a higher productive capacity.')
        self.play(FadeOut(prod_grp), FadeOut(molly_grp), FadeOut(andrew_grp))
        self.play(Write(aa_def))
        self.pause()

        # B04c --------------------------------------------------------
        # her two entries get a beat each: carrots here, spinach at B04d

        self.play(FadeOut(aa_def))
        self.play(FadeIn(prod_grp), FadeIn(molly_grp), FadeIn(andrew_grp))
        aa_label = Tex('Absolute Advantage').scale(0.9).set_color(DEFINITION).next_to(prod, DOWN, buff=0.5)
        self.play(FadeIn(aa_label))
        box_c = focus_box(prod.get_entries()[3])
        box_s = focus_box(prod.get_entries()[4])
        self.play(FadeIn(box_c))
        self.pause()

        # B04d --------------------------------------------------------

        self.play(FadeIn(box_s))
        self.pause()

        # B05 ---------------------------------------------------------

        self.play(FadeOut(prod_grp), FadeOut(aa_label), FadeOut(box_c), FadeOut(box_s))
        head = title('The Co-op')
        ax, caps = coop_axes()
        ppf_m, ppf_a, lab_m, lab_a = coop_curves(ax)
        self.play(FadeIn(head), FadeIn(ax), FadeIn(caps))
        self.play(Create(ppf_m), FadeIn(lab_m))
        self.play(Create(ppf_a), FadeIn(lab_a))
        self.pause()

        # B05b --------------------------------------------------------

        molly_crops = split(MOLLY_AT, 1 / 2)
        andrew_crops = split(ANDREW_AT, 1 / 2)
        dm = Dot(ax.c2p(5, 20), color=MOLLY, z_index=10)
        da = Dot(ax.c2p(4, 8), color=ANDREW, z_index=10)
        self.play(FadeIn(molly_crops), FadeIn(dm))
        self.play(FadeIn(andrew_crops), FadeIn(da))
        self.pause()

        # B05c --------------------------------------------------------

        dc = Dot(ax.c2p(9, 28), color=GUILD, z_index=10)
        cm, ca = dm.copy(), da.copy()
        self.add(cm, ca)
        self.play(cm.animate.move_to(dc), ca.animate.move_to(dc))
        self.play(FadeOut(cm), FadeOut(ca), FadeIn(dc))
        self.pause()

        # B06 ---------------------------------------------------------
        # the co-op line is DRAWN BY the co-op dot: a GUILD trail follows it out
        # to (18, 0) and back up to (0, 56), which is the whole line

        coop_trail = trail_behind(dc.get_center, GUILD, width=4)
        coop_trail.z_index = -1
        self.add(coop_trail)
        self.play(dm.animate.move_to(ax.c2p(10, 0)), da.animate.move_to(ax.c2p(8, 0)),
                  dc.animate.move_to(ax.c2p(18, 0)),
                  Transform(molly_crops, split(MOLLY_AT, 1)), Transform(andrew_crops, split(ANDREW_AT, 1)),
                  run_time=3)
        self.pause()

        # B06b --------------------------------------------------------

        self.play(dm.animate.move_to(ax.c2p(0, 40)), da.animate.move_to(ax.c2p(0, 16)),
                  dc.animate.move_to(ax.c2p(0, 56)),
                  Transform(molly_crops, split(MOLLY_AT, 0)), Transform(andrew_crops, split(ANDREW_AT, 0)),
                  run_time=3)
        coop_trail.clear_updaters()
        coop_line = ax.plot(PPF_Coop, color=GUILD, x_range=(0, 18), z_index=-1)
        self.remove(coop_trail)        # same geometry: the swap is invisible
        self.add(coop_line)
        self.bring_to_front(dm, da, dc)
        lab_c, lab_c_sub = coop_label(ax)
        self.play(FadeIn(lab_c), FadeIn(lab_c_sub))
        self.pause()

        # B06c --------------------------------------------------------

        self.play(dm.animate.move_to(ax.c2p(5, 20)), da.animate.move_to(ax.c2p(4, 8)),
                  dc.animate.move_to(ax.c2p(9, 28)),
                  Transform(molly_crops, split(MOLLY_AT, 1 / 2)), Transform(andrew_crops, split(ANDREW_AT, 1 / 2)),
                  run_time=2)
        self.pause()

        # B07 ---------------------------------------------------------
        # the pulse is about the CURVE, so it stays on the graph screen; his
        # arithmetic moved to the table screen (B08c–B08e), where Molly's is

        self.play(Indicate(ppf_a, color=FOCUS, scale_factor=1.05))
        self.pause()

        # B07b --------------------------------------------------------
        # animation_2: the cost table joins, the camera frames the pair and the
        # farm cards step off; the box lands on MOLLY's production row

        prod, prod_grp = production_table()
        cost, cost_grp = cost_table()
        cost_grp.next_to(prod_grp, RIGHT, buff=0.7).align_to(prod_grp, UP)
        table_group = VGroup(prod_grp, cost_grp).move_to(UP * 0.9)
        self.play(FadeOut(head), FadeOut(ax), FadeOut(caps), FadeOut(ppf_m), FadeOut(ppf_a),
                  FadeOut(lab_m), FadeOut(lab_a), FadeOut(coop_line), FadeOut(lab_c), FadeOut(lab_c_sub),
                  FadeOut(dm), FadeOut(da), FadeOut(dc),
                  FadeOut(molly_crops), FadeOut(andrew_crops),
                  FadeOut(molly_grp), FadeOut(andrew_grp),
                  FadeIn(table_group),
                  self.camera.frame.animate.move_to(table_group).set(
                      width=table_group.width * 1.15).shift(DOWN * 1.0))
        self.drop_frame()
        box = focus_box(prod.get_rows()[1])
        self.play(FadeIn(box))
        self.pause()

        # B08 ---------------------------------------------------------
        # Molly's opportunity cost, derived the A1 way under the tables. The
        # letters and the `=` are placed once and never move again: every step
        # below re-renders the NUMERALS only (Derivation.step).

        MATH_AT = table_group.get_bottom() + DOWN * 1.1
        molly_math = Derivation(MATH_AT, '10', 'C', '40', 'S')
        self.play(Transform(box, focus_box(molly_math.group, buff=0.35)),
                  FadeIn(molly_math.group))
        self.play(*molly_math.step(r'$\frac{10}{10}$', r'$\frac{40}{10}$'))
        self.play(*molly_math.step('1', '4'))
        self.play(Transform(box, focus_box(cost.get_entries()[3])),
                  *light(cost.get_entries()[3], SPINACH))
        self.pause()

        # B08b --------------------------------------------------------
        # the reciprocal, same gesture reversed. The camera stays down: Andrew's
        # math lands in this same spot at B08c

        self.play(Transform(box, focus_box(molly_math.group, buff=0.35)))
        self.play(*molly_math.step(r'$\frac{1}{4}$', '1'))
        self.play(Transform(box, focus_box(cost.get_entries()[4])),
                  *light(cost.get_entries()[4], CARROTS),
                  FadeOut(molly_math.group))
        self.pause()

        # B08c --------------------------------------------------------
        # Andrew's ritual, mirroring Molly's — the arithmetic that used to run
        # under the co-op graph at B07 now runs here, in her spot

        andrew_math = Derivation(MATH_AT, '8', 'C', '16', 'S')
        self.play(Transform(box, focus_box(prod.get_rows()[2])))
        self.play(Transform(box, focus_box(andrew_math.group, buff=0.35)),
                  FadeIn(andrew_math.group))
        self.pause()

        # B08d --------------------------------------------------------

        self.play(*andrew_math.step(r'$\frac{8}{8}$', r'$\frac{16}{8}$'))
        self.play(*andrew_math.step('1', '2'))
        self.play(Transform(box, focus_box(cost.get_entries()[6])),
                  *light(cost.get_entries()[6], SPINACH))
        self.pause()

        # B08e --------------------------------------------------------
        # his reciprocal, then the math clears and the camera shifts back up

        self.play(Transform(box, focus_box(andrew_math.group, buff=0.35)))
        self.play(*andrew_math.step(r'$\frac{1}{2}$', '1'))
        self.play(Transform(box, focus_box(cost.get_entries()[7])),
                  *light(cost.get_entries()[7], CARROTS),
                  FadeOut(andrew_math.group),
                  self.camera.frame.animate.shift(UP * 1.0))
        self.drop_frame()
        self.play(FadeOut(box))
        self.pause()

        # B09 ---------------------------------------------------------

        ca_def = definition('Comparative Advantage', 'is having a lower opportunity cost.')
        self.play(FadeOut(table_group),
                  self.camera.frame.animate.move_to(ORIGIN).set(width=FRAME_W))
        self.drop_frame()
        self.play(Write(ca_def))
        self.pause()

        # B09b --------------------------------------------------------
        # the tables come back carrying the Absolute Advantage marks, so both
        # concepts are boxed on screen at once

        aa_label = Tex('Absolute Advantage').scale(0.85).set_color(DEFINITION).next_to(prod, DOWN, buff=0.5)
        aa_box_c = focus_box(prod.get_entries()[3])
        aa_box_s = focus_box(prod.get_entries()[4])
        ca_label = Tex('Comparative Advantage').scale(0.85).set_color(DEFINITION).next_to(cost, DOWN, buff=0.5)
        ca_box_a = focus_box(cost.get_entries()[6])     # Andrew's carrots: 2 S
        ca_box_m = focus_box(cost.get_entries()[4])     # Molly's spinach: 1/4 C
        self.play(FadeOut(ca_def))
        self.play(FadeIn(table_group), FadeIn(aa_label), FadeIn(aa_box_c), FadeIn(aa_box_s))
        self.play(FadeIn(ca_label))
        self.play(FadeIn(ca_box_a))
        self.pause()

        # B09c --------------------------------------------------------
        # her entry gets its own beat, as her two AA entries do at B04c/B04d

        self.play(FadeIn(ca_box_m))
        self.pause()

        # B09d --------------------------------------------------------

        recip = VGroup(
            Tex(narration("When one farmer's opportunity cost is lower in one crop,")).scale(SCALE_CAPTION),
            Tex(narration("the other's is always lower in the other.")).scale(SCALE_CAPTION),
        ).arrange(DOWN, buff=0.22).set_color(CAPTION).move_to(DOWN * 2.6)
        self.play(FadeIn(recip))
        self.pause()

        # B10 ---------------------------------------------------------

        exercise_card(self, 'Exercise A2 $|$ Q1', [
            'Professor McGonagall also bakes rock cakes and fruitcakes, up to 10 $R$ or 5 $F$ in one day.',
            "Using Hagrid's original numbers, set up a production table with both bakers' output per day.",
            'Who has the absolute advantage in rock cakes?',
            'Then set up an opportunity cost table. Who has the comparative advantage in rock cakes?',
        ])
        self.pause()

        # B11 ---------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        head = title('The Co-op')
        ax, caps = coop_axes()
        ppf_m, ppf_a, lab_m, lab_a = coop_curves(ax)
        coop_line = ax.plot(PPF_Coop, color=GUILD, x_range=(0, 18), z_index=-1)
        lab_c, lab_c_sub = coop_label(ax)
        molly_grp, andrew_grp = farm_cards()
        molly_cost = Tex('$1C=4S$').scale(SCALE_TICK).set_color(ON_FILL).rotate(PI / 2).next_to(molly_grp[0].get_right(), LEFT, buff=0.12)
        molly_cost.z_index = 3
        andrew_cost = Tex('$1C=2S$').scale(SCALE_TICK).set_color(ON_FILL).rotate(PI / 2).next_to(andrew_grp[0].get_right(), LEFT, buff=0.12)
        andrew_cost.z_index = 3
        molly_crops = split(MOLLY_AT, 1 / 2)
        andrew_crops = split(ANDREW_AT, 1 / 2)
        dm = Dot(ax.c2p(5, 20), color=MOLLY, z_index=10)
        da = Dot(ax.c2p(4, 8), color=ANDREW, z_index=10)
        dc = Dot(ax.c2p(9, 28), color=GUILD, z_index=10)
        self.play(FadeIn(head), FadeIn(ax), FadeIn(caps), FadeIn(ppf_m), FadeIn(ppf_a),
                  FadeIn(lab_m), FadeIn(lab_a), FadeIn(coop_line), FadeIn(lab_c), FadeIn(lab_c_sub),
                  FadeIn(molly_grp), FadeIn(andrew_grp), FadeIn(molly_cost), FadeIn(andrew_cost),
                  FadeIn(molly_crops), FadeIn(andrew_crops), FadeIn(dm), FadeIn(da), FadeIn(dc))
        self.pause()

        # B11b --------------------------------------------------------
        # corner one: Molly goes all spinach. The co-op dot rides to
        # (0,40)+(4,8) = (4,48). No trail — the path between corners is an
        # interior chord, not a frontier; the frontier itself is drawn at B11d.

        spinach_adv = Tex('Spinach').scale(0.85).set_color(SPINACH).rotate(PI / 2).next_to(molly_grp[0], RIGHT, buff=0.2)
        carrot_adv = Tex('Carrots').scale(0.85).set_color(CARROTS).rotate(PI / 2).next_to(andrew_grp[0], RIGHT, buff=0.2)
        self.play(Write(spinach_adv))
        self.play(dm.animate.move_to(ax.c2p(0, 40)), dc.animate.move_to(ax.c2p(4, 48)),
                  Transform(molly_crops, split(MOLLY_AT, 0)),
                  run_time=3)
        self.pause()

        # B11c --------------------------------------------------------
        # corner two: Andrew goes all carrots; the co-op dot lands on the kink.

        self.play(Write(carrot_adv))
        self.play(da.animate.move_to(ax.c2p(8, 0)), dc.animate.move_to(ax.c2p(8, 40)),
                  Transform(andrew_crops, split(ANDREW_AT, 1)),
                  run_time=3)
        self.pause()

        # B11d --------------------------------------------------------
        # the TRUE specialized frontier is DRAWN BY the co-op dot, exactly the
        # way the straight line was at B06/B06b — and what drives the dot is a
        # farmer switching crops. Andrew's leg first: he swings all the way to
        # his other crop and back, and a GUILD trail follows the co-op dot out
        # to (0, 56) and home to the kink at (8, 40), drawing the upper branch.
        # The old straight line ghosts to MUTED (A1's ppf_ghost idiom) and
        # `Co-op` sheds its qualifier as the outbound leg starts, so the new
        # line is legible against it and the name belongs to the kinked line
        # (the old 'Guild PPF (no specialization)' -> 'Guild PPF' rename).

        self.play(Indicate(dc, color=FOCUS))
        spec_trail = trail_behind(dc.get_center, GUILD, width=4)
        spec_trail.z_index = 1
        self.add(spec_trail)
        self.play(da.animate.move_to(ax.c2p(0, 16)), dc.animate.move_to(ax.c2p(0, 56)),
                  Transform(andrew_crops, split(ANDREW_AT, 0)),
                  coop_line.animate.set_color(MUTED), FadeOut(lab_c_sub),
                  run_time=3)
        self.play(da.animate.move_to(ax.c2p(8, 0)), dc.animate.move_to(ax.c2p(8, 40)),
                  Transform(andrew_crops, split(ANDREW_AT, 1)),
                  run_time=3)
        self.pause()

        # B11e --------------------------------------------------------
        # Molly's round trip draws the lower branch the same way: out to her
        # all-carrots corner and back. The finished trail then hands off to a
        # plotted polyline, as B06b hands off to PPF_Coop.

        self.play(dm.animate.move_to(ax.c2p(10, 0)), dc.animate.move_to(ax.c2p(18, 0)),
                  Transform(molly_crops, split(MOLLY_AT, 1)),
                  run_time=3)
        self.play(dm.animate.move_to(ax.c2p(0, 40)), dc.animate.move_to(ax.c2p(8, 40)),
                  Transform(molly_crops, split(MOLLY_AT, 0)),
                  run_time=3)
        spec_trail.clear_updaters()
        spec_line = polyline([ax.c2p(0, 56), ax.c2p(8, 40), ax.c2p(18, 0)], color=GUILD)
        spec_line.z_index = 1
        self.remove(spec_trail)        # same geometry: the swap is invisible
        self.add(spec_line)
        self.bring_to_front(dm, da, dc)
        self.pause()

        # B11f --------------------------------------------------------

        gains = Polygon(ax.c2p(18, 0), ax.c2p(8, 40), ax.c2p(0, 56),
                        color=TRADE, fill_opacity=AREA_OPACITY, stroke_width=0)
        gains.z_index = 0
        gains_lab = Tex('Gains From Specialization').scale(SCALE_CAPTION).set_color(TRADE).move_to(RIGHT * 3.0 + DOWN * 3.2)
        self.play(FadeIn(gains), FadeIn(gains_lab))
        self.pause()

        # B12 ---------------------------------------------------------

        exercise_card(self, 'Exercise A2 $|$ Q2', [
            'In Exercise A1, we found that Hagrid can bake 20 rock cakes ($R$) or 30 fruitcakes ($F$) in one day',
            'and Professor McGonagall can bake 10 rock cakes or 5 fruitcakes in one day.',
            'Use the production table and opportunity cost table from Q1 to determine',
            'who should specialize in each good if they want to jointly produce more.',
        ])
        self.pause()

        # B13 ---------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        head = title('Two Remaining Questions')
        # the numbered list is material, not narration: plain serif Tex in INK
        # (the sans/gold treatment was tried here and pulled — guide §9)
        q1 = Tex('1. But is a co-op necessary?').set_color(INK)
        q2 = Tex('2. Can both farmers be better off at the same time?').set_color(INK)
        qs = VGroup(q1, q2).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        qs.move_to(UP * 1.5).align_to(head, LEFT)
        self.play(FadeIn(head))
        self.play(Write(q1))
        self.pause()

        # B13b --------------------------------------------------------

        self.play(Write(q2))
        self.pause()

        # B13c --------------------------------------------------------

        yes = Tex('YES!').scale(1.4).set_color(FOCUS).move_to(DOWN * 1.1)
        self.play(Write(yes))
        self.pause()

        # B14 ---------------------------------------------------------
        # the attribution reads as a quotation credit: this optimistic YES is
        # roughly Ricardo's claim

        ricardo = Tex(r'\textemdash\ David Ricardo (1772 \textendash\ 1823)').scale(SCALE_CAPTION).set_color(CAPTION)
        ricardo.next_to(yes, DOWN, buff=0.5).align_to(yes, LEFT).shift(RIGHT * 0.8)
        self.play(Write(ricardo))
        self.pause()

        # B15 ---------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        # the panels sit low and a little short: the bottom band has to hold the
        # readout numerals AND each farmer's under-axis name line (which grows
        # into their stored rate at B16b/B16d), and the title above them carries
        # a centred subtitle line from B15b on
        panel_kwargs = dict(
            x_range=[0, 11, 1], y_range=[0, 45, 5], x_length=4.6, y_length=4.3, ticks=True,
        )
        PANEL_DROP = DOWN * 0.30
        NAME_Y = -3.30                 # the under-axis band: names, then rates
        axm = style_axes(
            x_axis_config={'numbers_to_include': [10],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [40],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            **panel_kwargs).shift(LEFT * 3.8 + PANEL_DROP)
        axa = style_axes(
            x_axis_config={'numbers_to_include': [8],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [16],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            **panel_kwargs).shift(RIGHT * 3.2 + PANEL_DROP)

        def panel_caps(ax_):
            return VGroup(
                Tex('Carrots').scale(SCALE_TICK).set_color(CARROTS).next_to(ax_.c2p(11, 0), RIGHT, buff=0.2),
                Tex('Spinach').scale(SCALE_TICK).set_color(SPINACH).next_to(ax_.c2p(0, 42), RIGHT, buff=0.2))

        def under_axis(ax_, mob):
            """Park a line centred under a panel's x-axis. The band holds the
            farmer's name from B15 and the same label — grown into their full
            self-trade rate — from B16b/B16d on. Nothing else identifies the
            panels: the owner-colored curve does the rest."""
            return mob.move_to(np.array([ax_.c2p(5.5, 0)[0], NAME_Y, 0]))

        caps_m = panel_caps(axm)
        caps_a = panel_caps(axa)
        ppf_m = axm.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        ppf_a = axa.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        name_m = under_axis(axm, Tex('Molly').scale(0.9))
        name_a = under_axis(axa, Tex('Andrew').scale(0.9))
        self.play(FadeIn(axm), FadeIn(caps_m), FadeIn(axa), FadeIn(caps_a))
        self.play(Create(ppf_m), FadeIn(name_m))
        self.play(Create(ppf_a), FadeIn(name_a))
        self.pause()

        # B15b --------------------------------------------------------

        head = title('Autarky')
        # the bottom band belongs to the under-axis name lines now, so the
        # definition takes the subtitle slot the B16e hook later occupies —
        # centred on the frame, like that hook
        aut_def = (definition('Autarky', "is when the farmers don't trade with each other.")
                   .scale(0.9).next_to(head, DOWN, buff=0.25).set_x(0))
        self.play(FadeIn(head), Write(aut_def))
        self.pause()

        # B15c --------------------------------------------------------

        def autarky_marker(ax_, c, s):
            p = ax_.c2p(c, s)
            dot = Dot(p, color=INK, z_index=10)
            v = DashedLine(ax_.c2p(c, 0), p, color=MUTED)
            h = DashedLine(ax_.c2p(0, s), p, color=MUTED)
            lab = Tex(f'({c}, {s})').scale(SCALE_CAPTION).set_color(CAPTION).next_to(p, UR, buff=0.1)
            return VGroup(v, h, dot, lab)

        mark_m = autarky_marker(axm, 3, 28)
        mark_a = autarky_marker(axa, 4, 8)
        self.play(FadeIn(mark_m))
        self.play(FadeIn(mark_a))
        self.pause()

        # B16 ---------------------------------------------------------

        self.play(FadeOut(axa), FadeOut(caps_a), FadeOut(ppf_a), FadeOut(name_a),
                  FadeOut(mark_a), FadeOut(aut_def))
        sweep = ValueTracker(0)

        def selftrade_readout():
            c = sweep.get_value()
            s = PPF_Molly(c)
            p = axm.c2p(c, s)
            dot = Dot(p, color=MOLLY, z_index=11)
            v = DashedLine(axm.c2p(c, 0), p, color=MUTED)
            h = DashedLine(axm.c2p(0, s), p, color=MUTED)
            c_num = DecimalNumber(c, num_decimal_places=1, color=CARROTS).scale(SCALE_TICK).next_to(axm.c2p(c, 0), DOWN, buff=0.2)
            s_num = DecimalNumber(s, num_decimal_places=1, color=SPINACH).scale(SCALE_TICK).next_to(axm.c2p(0, s), LEFT, buff=0.15)
            c_bar = Line(axm.c2p(0, 0), axm.c2p(c, 0), color=CARROTS, stroke_width=6)
            s_bar = Line(axm.c2p(0, s), axm.c2p(0, 40), color=SPINACH, stroke_width=6)
            return VGroup(v, h, c_bar, s_bar, dot, c_num, s_num)

        readout = always_redraw(selftrade_readout)
        self.add(readout)
        # FOCUS, not GUIDE: the mirror arrow on Andrew's panel would be red on red
        arrow = CurvedArrow(axm.c2p(0, 40), axm.c2p(3, 28), angle=-PI / 3, color=FOCUS)
        selftrade_lab = Tex('Self-Trade').scale(0.9).set_color(DEFINITION).next_to(axm.c2p(3.2, 37), RIGHT, buff=0.2)
        self.play(Create(arrow), FadeIn(selftrade_lab))
        self.play(sweep.animate.set_value(3), run_time=4)
        readout.clear_updaters()      # frozen: exercise_card's stage-dim must not fight a redraw
        self.remove(sweep)            # ValueTracker is a bare Mobject; a later exercise_card()'s
                                       # VGroup(*scene.mobjects) rejects non-VMobjects if it lingers
        self.pause()

        # B16b --------------------------------------------------------
        # the derivation gets the camera; it holds through B16c

        # the derivation is built where it ENDS up, then its two halves are sent
        # back out to the panel to fly in from the bars they read off — after
        # which the letters and the `=` are fixed and only the numerals move
        selftrade = Derivation(RIGHT * 3.9 + UP * 0.8, '3', 'C', '12', 'S')
        c_side = VGroup(selftrade.nL, selftrade.lL)
        s_side = VGroup(selftrade.nR, selftrade.lR)
        c_home, s_home = c_side.copy(), s_side.copy()
        c_side.scale(0.8 / 1.2).next_to(axm.c2p(1.5, 0), DOWN, buff=0.7)
        s_side.scale(0.8 / 1.2).next_to(axm.c2p(0, 34), LEFT, buff=0.7)
        self.play(FadeIn(c_side), FadeIn(s_side))
        self.play(Transform(c_side, c_home), Transform(s_side, s_home),
                  FadeIn(selftrade.sep))
        # a true push-in: the crop starts right of the panel's x caption, so
        # nothing is left half-in frame
        self.play(self.camera.frame.animate.move_to(RIGHT * 3.9 + UP * 0.05).set(width=7.8))
        self.drop_frame()
        self.play(*selftrade.step(r'$\frac{3}{3}$', r'$\frac{12}{3}$'))
        self.play(*selftrade.step('1', '4'))
        self.pause()

        # B16c --------------------------------------------------------

        rate_line = Tex('{{Exchange Rate}} $=$ {{Opportunity Cost}}').scale(0.75).set_color_by_tex_to_color_map({
            'Exchange Rate': DEFINITION,
            'Opportunity Cost': DEFINITION,
        }).next_to(selftrade.sep, DOWN, buff=1.4)
        self.play(Write(rate_line))
        self.pause()

        # B16d --------------------------------------------------------
        # Molly's math files itself under her panel — where her under-axis name
        # GROWS into the full rate line to receive it — the camera pulls back,
        # and Andrew's panel returns to play the mirror-image self-trade

        molly_rate = under_axis(axm, Tex('Molly: {{1}} {{C}} $=$ {{4}} {{S}}').scale(0.9)
                                .set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH}))
        eq_group = selftrade.group
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=FRAME_W),
                  Transform(eq_group, molly_rate.copy()),
                  Transform(name_m, molly_rate.copy()), FadeOut(rate_line))
        self.drop_frame()
        self.remove(eq_group)          # name_m IS the rate line from here on

        axa = style_axes(
            x_axis_config={'numbers_to_include': [8],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [16],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            **panel_kwargs).shift(RIGHT * 3.2 + PANEL_DROP)
        caps_a = panel_caps(axa)
        ppf_a = axa.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        name_a = under_axis(axa, Tex('Andrew').scale(0.9))
        mark_a = autarky_marker(axa, 4, 8)
        self.play(FadeIn(axa), FadeIn(caps_a), FadeIn(ppf_a), FadeIn(name_a), FadeIn(mark_a))

        sweep_a = ValueTracker(8)

        def selftrade_readout_a():
            c = sweep_a.get_value()
            s = PPF_Andrew(c)
            p = axa.c2p(c, s)
            dot = Dot(p, color=ANDREW, z_index=11)
            v = DashedLine(axa.c2p(c, 0), p, color=MUTED)
            h = DashedLine(axa.c2p(0, s), p, color=MUTED)
            c_num = DecimalNumber(c, num_decimal_places=1, color=CARROTS).scale(SCALE_TICK).next_to(axa.c2p(c, 0), DOWN, buff=0.2)
            s_num = DecimalNumber(s, num_decimal_places=1, color=SPINACH).scale(SCALE_TICK).next_to(axa.c2p(0, s), LEFT, buff=0.15)
            c_bar = Line(axa.c2p(c, 0), axa.c2p(8, 0), color=CARROTS, stroke_width=6)
            s_bar = Line(axa.c2p(0, 0), axa.c2p(0, s), color=SPINACH, stroke_width=6)
            return VGroup(v, h, c_bar, s_bar, dot, c_num, s_num)

        readout_a = always_redraw(selftrade_readout_a)
        self.add(readout_a)
        arrow_a = CurvedArrow(axa.c2p(8, 0), axa.c2p(4, 8), angle=PI / 3, color=FOCUS)
        # the same gold label as Molly's, hugging the arc off its outer corner —
        # clear of the (4, 8) label, the marker and his curve, all of which sit
        # left of it
        selftrade_lab_a = Tex('Self-Trade').scale(0.9).set_color(DEFINITION).next_to(arrow_a, UR, buff=0.15)
        self.play(Create(arrow_a), FadeIn(selftrade_lab_a))
        self.play(sweep_a.animate.set_value(4), run_time=4)
        readout_a.clear_updaters()
        self.remove(sweep_a)
        andrew_rate = under_axis(axa, Tex('Andrew: {{1}} {{C}} $=$ {{2}} {{S}}').scale(0.9)
                                 .set_color_by_tex_to_color_map({'C': CARROTS, 'S': SPINACH}))
        self.play(Transform(name_a, andrew_rate))
        self.pause()

        # B16e --------------------------------------------------------
        # the title turns the corner and the hook takes the subtitle slot,
        # CENTRED on the frame — left-aligned under the title it read as the
        # title's own subtitle rather than the beat's line

        head_trade = title('Autarky $\\rightarrow$ Trade')
        hook = (Tex('Molly is looking for a trade better than her self-trade.')
                .scale(0.9).set_color(DEFINITION)
                .next_to(head_trade, DOWN, buff=0.25).set_x(0))
        self.play(Transform(head, head_trade), Write(hook))
        self.pause()

        # B17 ---------------------------------------------------------

        exercise_card(self, 'Exercise A2 $|$ Q3', [
            'What is the cost to McGonagall of baking 1 fruitcake ($F$) herself?',
            'What is an example of a trade with Hagrid that would be better for her?',
        ])
        self.pause()

        # B18 ---------------------------------------------------------

        self.reset_frame()
        FadeAll(self)
        head = title('Next time...', scale=1.5)
        topic = Tex('Trade can make both parties better off.').scale(1.2)
        self.add(head, topic)
        framebox_reveal(self, topic)
        FadeAll(self)
