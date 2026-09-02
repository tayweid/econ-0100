"""ECON 0100 video series — shared style (see Blocks/_Style_Guide.md).

Episodes import this once and never re-declare colors, frame, or card idioms:

    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
    from style import *

Importing applies the frame config (2:1, 60 fps, dark background).
"""

from manim import *
import numpy as np
import os
import random
import seaborn as sns

from scene_helpers import Raster_Font

# ----------------------------------------------------------------- palette (Graphite)
# Guide §2. Three laws: every hue is a noun; azure is reserved for the course's
# voice (titles/links/wordmark — never a curve); marks and text are different
# jobs (gold is text, never a mark). Values are CVD-validated as a set on BG —
# don't retune one in isolation.

# Base / text tokens
BG = '#212121'           # the one ground, video and web (was #1f1f1f)
INK = WHITE
MUTED = '#696969'        # geometry only: axes, ticks, ghosts, DWL
CAPTION = '#9E9E9E'      # muted TEXT: subtitles, stored results, axis captions
TITLE = '#4A8FF0'        # the brand azure — titles only (was #0096FF)
DEFINITION = '#E5C044'   # only the defined term inside a definition line; question lines
FOCUS = '#FFE14D'        # transient attention; never a persistent curve color

# Marks — the six persistent colors. The names shadow manim's constants on
# import so even un-ported code drifts toward spec. BLUE's value is a deep
# teal: azure is reserved for TITLE.
BLUE = '#128A9B'
ORANGE = '#E2803A'
GREEN = '#34B57A'
RED = '#C63944'
PURPLE = '#A99CF2'
PINK = '#C95AC0'

# Market model (B–E)
DEMAND = BLUE            # also MPB, MSB
SUPPLY = ORANGE          # also MPC, MSC, MC
TOTAL = PURPLE
DWL = MUTED
GOV = GREEN
EXT = PINK
GUIDE = RED              # P*/Q* lines, equilibrium dot, readouts
AREA_OPACITY = 0.35
DWL_OPACITY = 0.5

# Part A world
MOLLY = BLUE
ANDREW = RED
CO_OP = PURPLE
GUILD = CO_OP            # deprecated alias (guild -> co-op rename, 2026-09-02); pre-rename episode code still references it
CARROTS = ORANGE
SPINACH = GREEN
TRADE = PINK             # exchange lines, post-trade bundles, gains-from-trade regions
# PPF regions: the attainable set takes the owner's color; what's lost is ghosted; what's gained is a gain
ATTAINABLE = MOLLY
LOST = MUTED
GAINED = TRADE
ON_FILL = BG             # text sitting on a solid token-colored fill (no white strokes)

# Games
ROW_PLAYER = PINK
COL_PLAYER = BLUE
NASH = RED
EFFICIENT = GREEN

# Consumer (F)
GOOD_A = BLUE
GOOD_B = GREEN
INCOME = RED
BUDGET = RED
INDIFFERENCE = BLUE

# ----------------------------------------------------------------- frame
PIXEL_HEIGHT = 1080
FPS = 60
config.background_color = BG
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT * 2
config.frame_rate = FPS

# Type scale by role (multiply a body-size Tex)
SCALE_EPISODE = 1.5
SCALE_TITLE = 1.2
SCALE_BODY = 1.0
SCALE_CAPTION = 0.8
SCALE_TICK = 0.7
SCALE_CARD = 3.0

# ----------------------------------------------------------------- beats
# Beats are maniml pausepoints: write `self.pause('B04_wealth')` directly in
# construct(). (A shim can't do it: maniml detects the literal `self.pause(`
# spelling in the file to switch to pause-anchored checkpoints.)


# ----------------------------------------------------------------- sound
SOUND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sound')
TICK = os.path.join(SOUND_DIR, 'tick-glass.wav')       # the default: something moved or arrived


def tick(scene, offset=0.0, variant=''):
    """One glass tick at `offset` seconds into the play that follows.
    variant '' | 'a' | 'b' for tiny pitch differences in a run of ticks."""
    name = 'tick-glass.wav' if not variant else f'tick-glass-{variant}.wav'
    scene.add_sound(os.path.join(SOUND_DIR, name), time_offset=offset)


def ticks_lagged(scene, n, run_time=1.0, lag_ratio=0.1):
    """One tick per item of a LaggedStart / lag_ratio FadeIn of n items:
    item i begins at i * lag_ratio * run_time / (1 + lag_ratio * (n - 1))."""
    each = run_time / (1 + lag_ratio * (n - 1))
    for i in range(n):
        tick(scene, offset=i * lag_ratio * each, variant=('', 'a', 'b')[i % 3])


# ----------------------------------------------------------------- text
# Treatment D ("Narrator"), under test — see the Graphite type study.
# The frame has three speakers: the title is the course (CMU serif, azure);
# prose UNDER the title is the narrator (CMU Sans via \textsf) — subtitles,
# statement clauses, legend numbers; the material — math, model labels,
# definition/principle cards — is the book (CMU serif). Carve-out: an
# under-title line that is or becomes math (a stored OC result) is material —
# pass book=True or skip narration(). One flag, fully reversible.
NARRATOR_SANS = True


def narration(text):
    """Give a narrator line the sans voice (\\textsf) when NARRATOR_SANS is on.
    Never route math through this — material stays serif (the bakery rule)."""
    return f'\\textsf{{{text}}}' if NARRATOR_SANS else text


def title(text, scale=SCALE_TITLE, align=LEFT):
    """Screen title: blue, top of the frame, flush left (pass align=None to centre)."""
    t = Tex(text).scale(scale).to_edge(UP, buff=0.4).set_color(TITLE)
    if align is not None:
        t.to_edge(align, buff=0.6)
    return t


def subtitle(under, text, buff=0.25, align=None, book=False):
    """Muted caption line under a title (the guide's subtitle idiom: CAPTION,
    caption scale, left-aligned with the title — CAPTION, not MUTED: words get
    the text token, lines get the geometry one). `under` is what it stacks
    below; pass `align` when that differs from what it left-aligns to.
    Narrator voice by default; pass book=True for a line that is or becomes
    math (a stored OC result) so it stays serif."""
    s = (Tex(text if book else narration(text)).scale(SCALE_CAPTION)
         .set_color(CAPTION).next_to(under, DOWN, buff=buff))
    return s.align_to(under if align is None else align, LEFT)


def definition(term, rest):
    """One-line definition; only the term is gold. `rest` starts after the term."""
    return Tex(f'{{{{{term}}}}} {rest}').set_color_by_tex_to_color_map({term: DEFINITION})


def principle(text):
    """A principle line ('Preferences are rankings.'): body size, no title."""
    return Tex(text)


def tex_row(items, color=None, buff=0.25):
    row = VGroup(*[Tex(t) for t in items]).arrange(RIGHT, buff=buff)
    if color is not None:
        row.set_color(color)
    return row


def stack(items, buff=0.4, scale=SCALE_BODY):
    """Vertical list of Tex lines. Use instead of to_edge(vector) hacks."""
    return VGroup(*[Tex(t).scale(scale) for t in items]).arrange(DOWN, buff=buff)


def narr_stack(items, buff=0.4, scale=SCALE_BODY):
    """A stack in the narrator's voice — the statement-card idiom (the
    *Microeconomics tells us...* clauses under a title). Items with math in
    them belong in stack(), not here."""
    return stack([narration(t) for t in items], buff=buff, scale=scale)


# ----------------------------------------------------------------- axes
def axes(x_range, y_range, x_length=10, y_length=5, ticks=False, **kwargs):
    """Series-standard axes: muted grey, no tips, ticks only on request."""
    axis_config = {'color': MUTED, 'include_ticks': ticks}
    axis_config.update(kwargs.pop('axis_config', {}))
    return Axes(x_range=x_range, y_range=y_range, x_length=x_length, y_length=y_length,
                axis_config=axis_config, tips=False, **kwargs)


def axis_caption(ax, text, at_top=True):
    """Caption for the vertical axis, sitting to the right of its top."""
    y = ax.y_range[1] if at_top else ax.y_range[0]
    return (Tex(narration(text)).scale(SCALE_CAPTION).set_color(CAPTION)
            .next_to(ax.c2p(ax.x_range[0], y), RIGHT, buff=0.2))


def polyline(points, color=INK, width=4):
    """Corner-connected path: use for data and tracker-driven curves (no resampling wobble)."""
    return VMobject(stroke_color=color, stroke_width=width).set_points_as_corners(points)


def equilibrium_marker(ax, x, y, color=GUIDE):
    """Dot plus dashed drop-lines to both axes. Returns VGroup(dot, hline, vline)."""
    p = ax.c2p(x, y)
    dot = Dot(p, color=color, z_index=10)
    h = ax.get_horizontal_line(p, color=color, line_config={'dashed_ratio': 0.85}).set_opacity(0.3)
    v = ax.get_vertical_line(p, color=color, line_config={'dashed_ratio': 0.85}).set_opacity(0.3)
    return VGroup(dot, h, v)


# ----------------------------------------------------------------- cards
def part_label(part, episode):
    """'Part A | Episode 0' — part in TITLE azure, rest CAPTION, card scale."""
    return (Tex(f'{{{{Part {part}}}}} $|$ Episode {episode}').set_color(CAPTION)
            .set_color_by_tex_to_color_map({f'Part {part}': TITLE}).scale(SCALE_CARD))


def flicker(scene, squares, rounds=4):
    """Raster squares flicker through blues."""
    colors = sns.color_palette('Blues', 50).as_hex()
    for _ in range(rounds):
        scene.play(*[s.animate.set_fill(random.choice(colors), opacity=1) for s in squares],
                   run_time=1 / 10)
        scene.wait(4 / 10)


def bumper_raster(scene, word='MICROECONOMICS'):
    """Bumper part 1: the raster wordmark fades in, centred. Returns the
    squares; follow with flicker() and pause(loop=True) for a seamless hold."""
    squares = VGroup(*Raster_Font(word))
    scene.play(FadeIn(squares))
    return squares


def bumper_title(scene, squares, part, episode, rounds=4):
    """Bumper part 2: the part label joins under the wordmark, which keeps
    flickering. Leaves everything on screen — clear with FadeAll(scene)."""
    label = part_label(part, episode).move_to(DOWN * 0.9)
    scene.play(AddTextWordByWord(label), squares.animate.move_to(UP * 0.9))
    flicker(scene, squares, rounds)
    return label


def bumper(scene, part, episode, rounds=4, word='MICROECONOMICS'):
    """The full episode bumper in one shot, clearing after itself. (A/A0_Welcome
    uses the split bumper_raster / flicker / bumper_title with FadeAll instead.)"""
    squares = bumper_raster(scene, word)
    flicker(scene, squares, rounds)
    label = bumper_title(scene, squares, part, episode, rounds)
    scene.wait()
    scene.play(FadeOut(squares), FadeOut(label))


def last_time(scene):
    card = Tex('Last Time...').scale(SCALE_CARD)
    scene.play(FadeIn(card), run_time=1 / 2)
    scene.wait()
    scene.play(FadeOut(card), run_time=1 / 2)


def framebox_reveal(scene, mobject, buff=0.5, run_time=2):
    """Create a box around `mobject`, then unwind it — the single-line emphasis idiom."""
    box = SurroundingRectangle(mobject, buff=buff)
    scene.play(Create(box), run_time=run_time)
    scene.play(Uncreate(box.flip(RIGHT)), run_time=run_time)


def dim_overlay(opacity=0.8):
    """Full-frame dimmer for definition cards only."""
    return Rectangle(height=50, width=50, stroke_width=0).set_fill(BG, opacity=opacity)


def exercise_card(scene, head_text, lines):
    """Cut-to-exercise: the stage itself fades to near-black and the question
    writes on a rounded panel. (Not a dim overlay: in the GL viewer strokes
    draw over translucent fills, so an overlay leaves the stage punching
    through.) The panel's top corners are fixed; its height follows the text,
    and lines wrap to the panel width (Tex has no paragraph wrapping).
    Returns (stage, card); Restore(stage) brings the stage back, or the next
    FadeAll clears it with everything else.
    (Promoted from A/A1_The_PPF/03_Code.py, which keeps a local copy.)"""
    stage = VGroup(*scene.mobjects)
    stage.save_state()
    margin, pad = 1.5, 0.6                       # frame-to-panel, panel-to-text
    text_width = FRAME_W - 2 * (margin + pad)

    def rows(text, scale=0.9):
        """Wrap the body to the panel width, in the narrator's sans voice.

        The body is prose under a title, so it takes `narration()`; the gold
        head stays serif. Inline math (`$R$`, `$F$`) is untouched by `\\textsf`
        and still typesets as math. The measurement has to be taken on the
        SAME wrapped Tex that gets rendered — sans is wider than serif, so
        measuring the bare string would break the lines in the wrong places."""
        def row(t):
            return Tex(narration(t)).scale(scale)

        whole = row(text)
        if whole.get_width() <= text_width:
            return [whole]
        out, current = [], ''
        for word in text.split():
            trial = (current + ' ' + word).strip()
            if current and row(trial).get_width() > text_width:
                out.append(current)
                current = word
            else:
                current = trial
        out.append(current)
        return [row(r) for r in out]

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


def FadeAll(scene, run_time=1):
    """Fade out everything on screen in one play. Clears updaters first (an
    always_redraw mobject would repaint itself at full opacity mid-fade), and
    skips mobjects already covered by a group (bring_to_front leaves the same
    mark at top level and inside its ValueLine)."""
    mobs, seen = [], set()
    for m in scene.mobjects:
        if id(m) not in seen:
            mobs.append(m)
            seen.update(id(x) for x in m.get_family())
    for m in mobs:
        m.clear_updaters()
    if mobs:
        scene.play(*[FadeOut(m) for m in mobs], run_time=run_time)


__all__ = [n for n in dir() if not n.startswith('_')]


# ----------------------------------------------------------------- avatars (placeholder)
def avatar(label, color=INK, radius=0.4):
    """Placeholder character: a circle in the party's token color with a label
    beneath. Stand-in until the stylized avatar design exists (see guide §9)."""
    body = Circle(radius=radius, color=color, stroke_width=4)
    name = Tex(label).scale(SCALE_CAPTION).next_to(body, DOWN, buff=0.15)
    return VGroup(body, name)


def speech(avatar_group, text, direction=UR):
    """Speech line for an avatar: boxed Tex off one shoulder."""
    line = Tex(text).scale(SCALE_CAPTION)
    box = SurroundingRectangle(line, buff=0.2, color=MUTED)
    return VGroup(box, line).next_to(avatar_group[0], direction, buff=0.2)


# ----------------------------------------------------------------- layout: notes panel
# 2:1 frame (16 x 8 units). The notes panel owns the right third; the model
# lives in the left two-thirds, separated by a vertical bar (guide §1, §9).
FRAME_W = config.frame_width            # follows the 2:1 pixel config (maniml syncs the camera frame to it)
PANEL_X = -FRAME_W / 2 + FRAME_W * 2 / 3        # x of the bar (= +2.667)
MODEL_CENTER = np.array([(-FRAME_W / 2 + PANEL_X) / 2, 0, 0])   # centre of the model region
MODEL_WIDTH = PANEL_X + FRAME_W / 2
PANEL_PAD = 0.45
PANEL_WIDTH = FRAME_W / 2 - PANEL_X - 2 * PANEL_PAD


def on_model(mobject, margin=0.6):
    """Centre a mobject horizontally in the model region (keeps its y), shrinking
    it if it is wider than the region."""
    if mobject.get_width() > MODEL_WIDTH - margin:
        mobject.scale((MODEL_WIDTH - margin) / mobject.get_width())
    return mobject.move_to([MODEL_CENTER[0], mobject.get_center()[1], 0])


class NotesPanel:
    """The running notes column: principle lines and definitions accumulate
    top-down, 'like someone following along taking notes.'

        panel = NotesPanel()
        panel.show(scene)
        panel.add(scene, 'Preferences are rankings.')
        panel.add(scene, definition('Autarky', 'is economic self-sufficiency.'))
        panel.hide(scene)

    Lines auto-scale to the column width (down to `min_scale`); pass a list of
    strings to break a long line by hand.
    """

    def __init__(self, line_scale=0.6, min_scale=0.45, gap=0.28):
        self.bar = Line([PANEL_X, FRAME_HEIGHT / 2 - 0.6, 0], [PANEL_X, -FRAME_HEIGHT / 2 + 0.6, 0],
                        color=MUTED, stroke_width=2)
        self.lines = VGroup()
        self.line_scale = line_scale
        self.min_scale = min_scale
        self.gap = gap
        self.visible = False

    # -- geometry
    def _top_left(self):
        return np.array([PANEL_X + PANEL_PAD, FRAME_HEIGHT / 2 - 1, 0])

    def _fit(self, mob):
        mob.scale(self.line_scale)
        if mob.get_width() > PANEL_WIDTH:
            mob.scale(max(PANEL_WIDTH / mob.get_width(), self.min_scale / self.line_scale))
        return mob

    def _bottom(self):
        return -FRAME_HEIGHT / 2 + 0.7

    def _place(self, mob):
        if len(self.lines) == 0:
            mob.move_to(self._top_left(), aligned_edge=UL)
        else:
            mob.next_to(self.lines[-1], DOWN, buff=self.gap, aligned_edge=LEFT)
        return mob

    def _make_room(self, scene, incoming):
        """If `incoming` would run past the bottom, shrink the existing stack so
        the column always fits (the notebook page filling up)."""
        if len(self.lines) == 0:
            return
        available = self._top_left()[1] - self._bottom()
        need = self.lines.get_height() + self.gap + incoming.get_height()
        if need <= available:
            return
        factor = (available - incoming.get_height() - self.gap) / self.lines.get_height()
        shrunk = self.lines.copy().scale(factor)
        top = self._top_left()
        shrunk[0].move_to(top, aligned_edge=UL)
        for prev, cur in zip(shrunk[:-1], shrunk[1:]):
            cur.next_to(prev, DOWN, buff=self.gap * factor, aligned_edge=LEFT)
        scene.play(Transform(self.lines, shrunk), run_time=0.6)

    def _line(self, text, term=None):
        if term and term in text:
            return Tex(text.replace(term, f'{{{{{term}}}}}')).set_color_by_tex_to_color_map({term: DEFINITION})
        return Tex(text)

    def _wrap(self, text, term=None):
        """Greedy word-wrap to the column width at line_scale. Returns a VGroup of lines."""
        words, lines, current = text.split(), [], ''
        for w in words:
            trial = (current + ' ' + w).strip()
            if Tex(trial).scale(self.line_scale).get_width() > PANEL_WIDTH and current:
                lines.append(current)
                current = w
            else:
                current = trial
        if current:
            lines.append(current)
        rows = VGroup(*[self._line(l, term).scale(self.line_scale) for l in lines])
        return rows.arrange(DOWN, buff=0.12, aligned_edge=LEFT)

    def _make(self, item, term=None):
        if isinstance(item, Mobject):
            return self._fit(item)
        if isinstance(item, (list, tuple)):
            rows = VGroup(*[self._line(t, term) for t in item]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            return self._fit(rows)
        return self._wrap(item, term)

    # -- animation
    def show(self, scene, run_time=1):
        if not self.visible:
            scene.play(Create(self.bar), run_time=run_time)
            self.visible = True
        return self

    def add(self, scene, item, term=None, run_time=1):
        """Add a note. `item`: a string (auto-wrapped), a list of lines, or a Mobject.
        `term` marks the defined word in DEFINITION gold."""
        mob = self._make(item, term)
        self._make_room(scene, mob)
        self._place(mob)
        self.lines.add(mob)
        if not self.visible:
            self.show(scene)
        scene.play(FadeIn(mob, shift=0.2 * DOWN), run_time=run_time)
        return mob

    def file(self, scene, mob, text=None, term=None, run_time=1):
        """Move an on-screen line into the panel: the 'write it down' gesture.
        `mob` is consumed. Pass `text` so the panel copy is re-wrapped to the
        column (a Transform between the card and its wrapped version)."""
        target = self._make(text if text is not None else mob.copy(), term)
        self._make_room(scene, target)
        self._place(target)
        self.lines.add(target)
        if not self.visible:
            self.show(scene)
        scene.play(Transform(mob, target), run_time=run_time)
        scene.remove(mob)
        scene.add(target)
        return target

    def hide(self, scene, run_time=1):
        scene.play(FadeOut(self.lines), FadeOut(self.bar), run_time=run_time)
        self.lines = VGroup()
        self.visible = False
        return self


__all__ = [n for n in dir() if not n.startswith('_')]
