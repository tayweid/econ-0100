# maniml 03_Code.py EpisodeB1
#
# Episode B1 | Demand
# Round-3 pass, 2026-09-13, written directly (no subagents) against
# 02_Storyboard.md, which is the beat record; its Pausepoints table carries the
# beat-to-notes mapping.
#
# The round-3 corrections, in Taylor's order:
#   1. Act 1 centres the solo Part A column in the camera (B0's render leaves
#      the right 60% empty; deliberate improvement over the copy), and the
#      part titles sit a touch lower.
#   2. Act 1 subtitles are smaller than the subtitle() default.
#   3. The recitation-recap slide is cut; the B0 block hands straight to
#      Amanda-Grace.
#   4. Graph scenes: axes centred left-of-centre, math in the right half,
#      definitions small along the bottom edge.
#   5. Demand lines are DRAWN from the top intercept downward, and the
#      connecting segments run top-down too.
#   6. The jagged data drops to a faint background opacity under the line.
#   7. Axis reads are directional: the KNOWN value marks its own axis, dashes
#      run axis -> curve -> other axis (never past the curve), and the answer
#      is the axis's own numeral circled, prefixed `Q_d =` / `MB =`. No boxes,
#      no duplicate numerals, math in the right half.
#   8. The single-exchange scene is the ORIGINAL code's design: no camera
#      zoom -- everything but bar 1 fades, the price moves (raise: she stops;
#      lower: she buys) with CS/expenditure stretching live, readouts to the
#      left of the graph.
#   9. The bar walk is clean: no floating per-bar labels; the tally is two
#      math rows on the right.
#
# B16 is a placeholder card; the 3D `Sim/` beat replaces it later.
# Verbatim original: _archive/03_Code_fall2024.py.

from manim import *
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # tokens, frame config, title(), definition(), axes(), bumper pieces
from style import axes as style_axes


# ----------------------------------------------------------------- layout
# Round-3 stage: the axes sit centred LEFT of centre (the P axis clears the
# frame's left margin by ~2.6 units -- room for the height label and the
# single-exchange readouts), the RIGHT half carries the worked math, and
# definitions run small along the bottom edge.
GRAPH_W, GRAPH_H = 7.0, 6.0
GRAPH_SCALE = 0.8
GRAPH_AT = np.array([-2.6, 0.15, 0])     # low enough that the plot clears the title
MATH_AT = np.array([2.1, 0.7, 0])            # left edge of the math stack
STRIP_BUFF = 0.18                            # definitions: bottom edge + padding
REST_OPACITY = 0.10                          # the standing bars at rest


def place(ax, x_range, y_range):
    """Centre an axes by its PLOT, not its bounding box."""
    lo, hi = ax.c2p(x_range[0], y_range[0]), ax.c2p(x_range[1], y_range[1])
    return ax.shift(GRAPH_AT - (lo + hi) / 2)


def key_in(tex, time_per_char=0.05):
    """Letter-by-letter reveal, B0's helper, copied with B0's opening act."""
    glyphs = VGroup(*tex.family_members_with_points())
    return ShowIncreasingSubsets(glyphs, run_time=time_per_char * len(glyphs), rate_func=linear)


def strip(mob):
    """A definition line at the bottom edge: smaller than body, squished to
    the edge with a bit of padding (round-3 item 4)."""
    mob.scale(0.75)
    if mob.get_width() > FRAME_W - 1.6:
        mob.scale((FRAME_W - 1.6) / mob.get_width())
    return mob.to_edge(DOWN, buff=STRIP_BUFF).set_x(0)


def math_rows(lines, scale=0.85):
    """Worked steps: white serif, one scale, stacked left-aligned in the
    right half of the frame (round-3 item 4/7)."""
    rows = VGroup(*[Tex(t).scale(scale).set_color(INK) for t in lines])
    rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    return rows.move_to(MATH_AT, aligned_edge=LEFT)


def num(value, decimals=2):
    """A GUIDE readout numeral; whole values print as integers."""
    v = float(value)
    r = round(v)
    if abs(v - r) < 1e-3:
        return Integer(int(r), color=GUIDE).scale(SCALE_TICK)
    return DecimalNumber(v, num_decimal_places=decimals, color=GUIDE).scale(SCALE_TICK)


def axis_number(ax, axis, v):
    """The axis's own numeral at value v, or None if it doesn't draw one."""
    axis_mob = ax.get_x_axis() if axis == 'x' else ax.get_y_axis()
    for n in getattr(axis_mob, 'numbers', []):
        if abs(n.get_value() - v) < 1e-6:
            return n
    return None


def mark_value(ax, axis, v, decimals=2):
    """The value marked ON its axis without duplicating numerals: where the
    axis already draws this number, a GUIDE copy covers it exactly; where it
    doesn't, a GUIDE numeral takes the same seat (round-3 item 7)."""
    existing = axis_number(ax, axis, v)
    if existing is not None:
        return existing.copy().set_color(GUIDE)
    m = num(v, decimals)
    if axis == 'x':
        m.next_to(ax.c2p(v, 0), DOWN, buff=0.3)
    else:
        m.next_to(ax.c2p(0, v), LEFT, buff=0.3)
    return m


def read(ax, q, p, from_price, label):
    """A directional axis read (round-3 item 7). from_price=True: the known
    price marks the P axis, dashes run P axis -> curve -> Q axis, and the
    answer is the circled quantity labeled `Q_d =`. from_price=False is the
    reverse read, labeled `MB =`. Dashes never pass the curve.
    Returns (source, dash1, dash2, dot, answer) for sequenced plays."""
    at = ax.c2p(q, p)
    if from_price:
        source = mark_value(ax, 'y', p)
        d1 = DashedLine(ax.c2p(0, p), at, color=GUIDE).set_opacity(0.6)
        d2 = DashedLine(at, ax.c2p(q, 0), color=GUIDE).set_opacity(0.6)
        target = mark_value(ax, 'x', q, decimals=1)
    else:
        source = mark_value(ax, 'x', q, decimals=1)
        d1 = DashedLine(ax.c2p(q, 0), at, color=GUIDE).set_opacity(0.6)
        d2 = DashedLine(at, ax.c2p(0, p), color=GUIDE).set_opacity(0.6)
        target = mark_value(ax, 'y', p)
    dot = Dot(at, color=GUIDE, z_index=15)
    if from_price and axis_number(ax, 'x', q) is None:
        # a fractional answer gets its own row below the axis numerals, so
        # the ring never crowds the neighbouring numbers
        target.next_to(ax.c2p(q, 0), DOWN, buff=0.52)
    ring = Ellipse(width=target.get_width() + 0.4, height=target.get_height() + 0.32,
                   color=GUIDE, stroke_width=2.5).move_to(target)
    tag = Tex(f'${label} =$').scale(0.6).set_color(GUIDE)
    if from_price and axis_number(ax, 'x', q) is not None:
        tag.next_to(ring, DOWN, buff=0.08)   # under the circle, clear of the numeral row
    else:
        tag.next_to(ring, LEFT, buff=0.15)
    answer = VGroup(target, ring, tag)
    return VGroup(source, d1, d2, dot, answer)


# ----------------------------------------------------------------- the data
# Her five answers, (q, p). $2 and $0.50 sit exactly on the line; $4 sits
# clearly above it and $1 and $0.25 just off it -- the curvature.
HER = [(0, 4), (1, 2), (2, 1), (4, 0.5), (6, 0.25)]

# Staircase bars: bar i's flat top is the line's value at Q = i, so the
# top-right corner of every bar is on the line.
BAR_MB = [2.00, 1.50, 1.00, 0.50]


def Demand(q):
    return 2.5 - q / 2


def Inv_Demand(p):
    return (2.5 - p) * 2


def MDemand(q):
    return 12 - q / 5


def Inv_MDemand(p):
    return (12 - p) * 5


class EpisodeB1(Scene):
    """Episode B1 | Demand. One flat construct(); each `# Bxx` section is
    self-contained and ends at the pause() the viewer parks on."""

    def construct(self):

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

        # B02 ---------------------------------------------------------
        # Act 1 is B0's opening (B0_Markets/03_Code.py B01-B05b): same plays,
        # same texts, same pause placement. Round-3 departures, on Taylor's
        # notes: the solo Part A column is CENTRED in the camera (B0's render
        # leaves the right 60% empty), the part titles sit lower, and the
        # subtitles are smaller.

        FadeAll(self)
        last_card = Tex('Last Time...').scale(SCALE_CARD)
        self.play(FadeIn(last_card), run_time=1 / 2)
        self.pause()

        # B02b --------------------------------------------------------
        # the Part A stage, centred while it is alone on screen

        FadeAll(self)
        part_a = title('Part A')
        part_a_sub = subtitle(part_a, 'The core economic idea.').scale(0.75, about_edge=UL)

        ppf_ax = style_axes(x_range=[0, 100, 100], y_range=[0, 100, 100],
                            x_length=7, y_length=7).scale(0.6).move_to(LEFT * 4.5 + DOWN * 0.5)
        ppf_y = Tex('A').set_color(INK).next_to(ppf_ax.c2p(0, 100), UP, buff=0.3)
        ppf_x = Tex('B').set_color(INK).next_to(ppf_ax.c2p(100, 0), RIGHT, buff=0.3)

        alpha = ValueTracker(1)

        def Linear_PPF(x):
            return 100 - x

        def Bowed_PPF(x):
            a = alpha.get_value()
            return (100**a - x**a)**(1 / a)

        def PPF_Group():
            linear_ppf = ppf_ax.plot(Linear_PPF, color=MUTED, x_range=(0, 100))
            linear_ppf.z_index = -1
            bowed_ppf = ppf_ax.plot(Bowed_PPF, color=TRADE, x_range=(0, 100, 0.1))
            bowed_ppf.z_index = -1
            return VGroup(linear_ppf, bowed_ppf)

        # fade in a still copy -- always_redraw would repaint at full opacity
        # mid-fade (the FadeAll gotcha) and snap in instead of fading
        ppf_static = PPF_Group()
        self.play(FadeIn(part_a), FadeIn(part_a_sub), FadeIn(ppf_ax),
                  FadeIn(ppf_y), FadeIn(ppf_x), FadeIn(ppf_static))
        self.pause()

        # B02c --------------------------------------------------------
        # Part A's core idea: coordination bows the frontier out

        ppf_group = always_redraw(PPF_Group)   # live from here; at alpha=1 it matches the still
        self.remove(ppf_static)
        self.add(ppf_group)
        arrow = Arrow(start=ppf_ax.c2p(45, 56), end=ppf_ax.c2p(57, 67), buff=0).set_color(FOCUS)
        core_line = (Tex('\\textit{Specialization and trade can benefit both parties.}')
                     .scale(0.7).set_color(DEFINITION).move_to(LEFT * 3.95 + DOWN * 3.5))
        self.play(FadeIn(arrow), FadeIn(core_line), alpha.animate.set_value(1.5))
        self.remove(alpha)   # a bare tracker in scene.mobjects breaks later stage grabs
        self.pause()

        # B03 ---------------------------------------------------------
        # Part B fades in as the camera eases home

        part_b = (Tex('Part B').set_color(TITLE).scale(SCALE_TITLE)
                  .move_to(RIGHT * 1.85).align_to(part_a, UP))
        part_b_sub = (VGroup(Tex(narration('Competitive markets can efficiently')),
                             Tex(narration('coordinate our decisions.')))
                      .arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(SCALE_CAPTION)
                      .set_color(CAPTION).next_to(part_b, DOWN, buff=0.25).align_to(part_b, LEFT))
        part_b_sub.scale(0.75, about_edge=UL)
        self.play(FadeIn(part_b), FadeIn(part_b_sub),
                  self.camera.frame.animate.set(width=FRAME_W).move_to(ORIGIN))
        self.pause()

        # Part B's questions, keyed in one at a time under its title
        questions = [Tex('- Which point on the PPF?'),
                     Tex('- Coordinate large groups?'),
                     Tex('- Who benefits?')]
        for i, q in enumerate(questions):
            q.set_color(INK).align_to(part_b, LEFT).align_to(part_a, UP).shift(DOWN * (2.7 + 1.05 * i))

        # B03b --------------------------------------------------------
        # first question: two options on the frontier

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

        # B03c --------------------------------------------------------

        self.play(key_in(questions[1]))
        self.pause()

        # B03d --------------------------------------------------------

        self.play(key_in(questions[2]))
        self.pause()

        # B05 ---------------------------------------------------------
        # straight to the chocolate stage (the recap slide is cut, round-3
        # item 3): the asking price arrives high

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
        place(ax, [0, 7], [0, 4.5])
        p_lab = Tex('P').set_color(INK).next_to(ax.c2p(0, 4.5), LEFT, buff=0.25)
        q_lab = Tex('Q').set_color(INK).next_to(ax.c2p(7, 0), RIGHT, buff=0.25)

        ask = ValueTracker(4)

        def asking_mark():
            p = ask.get_value()
            line = (DashedLine(ax.c2p(0, p), ax.c2p(7, p), color=GUIDE)
                    .set_opacity(0.45))
            return VGroup(line, mark_value(ax, 'y', p))

        asking = always_redraw(asking_mark)

        self.play(FadeIn(head), FadeIn(ax), FadeIn(p_lab), FadeIn(q_lab))
        self.play(FadeIn(asking))
        self.pause()

        # B05b --------------------------------------------------------
        # her answer at $4, and the term for it

        dots = [Dot(ax.c2p(q, p), color=DEMAND, z_index=15) for q, p in HER]
        iqd_def = strip(definition(
            'Individual Quantity Demanded',
            'is the quantity a buyer is willing / able to buy.'))
        self.play(FadeIn(dots[0]))
        self.play(Write(iqd_def))
        self.pause()

        # B05c --------------------------------------------------------
        # lower the price and ask again

        self.play(ask.animate.set_value(2), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[1]))
        self.pause()

        # B05d --------------------------------------------------------

        self.play(ask.animate.set_value(1), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[2]))
        self.pause()

        # B05e --------------------------------------------------------
        # keep going through a range of prices, then park on her data

        self.play(ask.animate.set_value(0.5), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[3]))
        self.play(ask.animate.set_value(0.25), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(dots[4]))
        self.play(FadeOut(asking))
        self.pause()

        # B06 ---------------------------------------------------------
        # connect them, top-down; the jagged curve gets its name

        segs = VGroup(*[Line(ax.c2p(*HER[i - 1]), ax.c2p(*HER[i]), color=INK)
                        for i in range(1, len(HER))])
        idc_def = strip(definition(
            'Individual Demand Curve',
            'is the full collection of quantity demanded.'))
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.4))
        self.bring_to_front(*dots)
        self.play(FadeOut(iqd_def), Write(idc_def))
        self.pause()

        # B07 ---------------------------------------------------------
        # the pattern in the answers

        law_def = strip(definition(
            'Law of Demand', "is a good's quantity demanded falling with its price."))
        self.play(FadeOut(idc_def), Write(law_def))
        self.pause()

        # B08 ---------------------------------------------------------
        # the linear approximation, drawn from the intercept down; the data
        # drops to a faint background (round-3 items 5, 6)

        demand = ax.plot(Demand, x_range=[0, 5], color=DEMAND)
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
        place(ax2, [0, 6], [0, 2.5])
        demand2 = ax2.plot(Demand, x_range=[0, 5], color=DEMAND)
        eqn2 = Tex('$P = 2.5 - Q/2$').scale(0.9).set_color(INK).move_to(ax2.c2p(4.3, 2.0))
        p_lab2 = Tex('P').set_color(INK).next_to(ax2.c2p(0, 2.5), LEFT, buff=0.25)
        q_lab2 = Tex('Q').set_color(INK).next_to(ax2.c2p(6, 0), RIGHT, buff=0.25)
        d_lab2 = Tex('D').set_color(INK).next_to(ax2.c2p(5, 0), UR, buff=0.15)

        def stair(i, lo, hi):
            """Bar i between two heights (staircase: flat top at Demand(i))."""
            return Polygon(ax2.c2p(i - 1, lo), ax2.c2p(i, lo),
                           ax2.c2p(i, hi), ax2.c2p(i - 1, hi))

        def resting_bar(i):
            return (stair(i, 0, BAR_MB[i - 1])
                    .set_stroke(MUTED, 1, opacity=0.35).set_fill(MUTED, REST_OPACITY))

        rest_bars = VGroup(*[resting_bar(i) for i in range(1, 5)])
        rest_bars.z_index = 0

        self.play(FadeOut(segs), *[FadeOut(d) for d in dots], FadeOut(law_def))
        self.play(ReplacementTransform(ax, ax2), ReplacementTransform(demand, demand2),
                  ReplacementTransform(eqn, eqn2), ReplacementTransform(p_lab, p_lab2),
                  ReplacementTransform(q_lab, q_lab2), ReplacementTransform(d_lab, d_lab2))
        self.play(FadeIn(rest_bars))
        self.pause()

        # B09 ---------------------------------------------------------
        # a price gives a quantity: the directional read at $1.50

        read_a = read(ax2, 2, 1.5, from_price=True, label='Q_d')
        work = math_rows(['$1.50 = 2.5 - Q/2$', '$Q = 2$'])
        self.play(LaggedStart(*[Write(r) for r in work], lag_ratio=0.6))
        self.pause()

        # B09b --------------------------------------------------------
        # ...and one that lands between two bars

        read_b = read(ax2, 1.5, 1.75, from_price=True, label='Q_d')
        work_b = math_rows(['$1.75 = 2.5 - Q/2$', '$Q = 1.5$'])
        self.play(FadeOut(read_a), FadeOut(work))
        self.play(LaggedStart(*[Write(r) for r in work_b], lag_ratio=0.6))
        self.pause()

        # B10 ---------------------------------------------------------
        # the reverse read: a quantity gives a price

        self.play(Transform(head, title('Marginal Benefit')),
                  FadeOut(read_b), FadeOut(work_b))
        read_c = read(ax2, 3, 1.0, from_price=False, label='MB')
        work_c = math_rows(['$P = 2.5 - 3/2$', '$P = \\$1.00$'])
        self.play(LaggedStart(*[Write(r) for r in work_c], lag_ratio=0.6))
        self.pause()

        # B10b --------------------------------------------------------

        mb_def = strip(definition('Marginal Benefit', 'is the value of one more unit.'))
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
        # the offer of $1 -- then the single exchange ALONE: one bar, no
        # demand curve, nothing else on the plane (round-4)

        self.play(Restore(stage1), FadeOut(card1))
        pv = ValueTracker(1)
        bars_n = ValueTracker(1)

        def price_group(p, x_end=3.0):
            """The price line, ON TOP of the bars, its label riding the right
            end at one constant size -- it never shrinks after a move."""
            line = Line(ax2.c2p(0, p), ax2.c2p(x_end, p), color=GUIDE, stroke_width=3)
            tag = VGroup(Tex('Price').scale(0.6),
                         DecimalNumber(p, num_decimal_places=2).scale(0.6))
            tag.arrange(RIGHT, buff=0.18).set_color(GUIDE)
            tag.next_to(line.get_end(), RIGHT, buff=0.25)
            g = VGroup(line, tag)
            g.z_index = 10
            return g

        def exchange_pieces():
            """Bars 1..n against the current price. A bar the price defeats
            keeps only its DEMAND top edge -- her value stands, no exchange,
            no labels. Numbers sit ON the boxes; the word labels ride to the
            right of the rightmost buying bar, centred on its boxes."""
            p = pv.get_value()
            n = int(round(bars_n.get_value()))
            out = [price_group(p)]
            buying = None
            for i in range(1, n + 1):
                mb = BAR_MB[i - 1]
                if p <= mb + 1e-9:
                    out.append(stair(i, p, mb).set_stroke(DEMAND, 2)
                               .set_fill(DEMAND, AREA_OPACITY))
                    out.append(stair(i, 0, p).set_stroke(GOV, 2).set_fill(GOV, AREA_OPACITY))
                    if mb - p > 0.24:
                        out.append(Tex(f'{mb - p:.2f}').scale(0.5).set_color(INK)
                                   .move_to(ax2.c2p(i - 0.5, (p + mb) / 2)))
                    if p > 0.24:
                        out.append(Tex(f'{p:.2f}').scale(0.5).set_color(INK)
                                   .move_to(ax2.c2p(i - 0.5, p / 2)))
                    buying = (i, mb)
                else:
                    out.append(Line(ax2.c2p(i - 1, mb), ax2.c2p(i, mb),
                                    color=DEMAND, stroke_width=3))
            if buying is not None:
                i, mb = buying
                out.append(Tex('Consumer Surplus').scale(0.55).set_color(DEMAND)
                           .next_to(ax2.c2p(i, (p + mb) / 2), RIGHT, buff=0.3))
                out.append(Tex('Expenditure').scale(0.55).set_color(GOV)
                           .next_to(ax2.c2p(i, p / 2), RIGHT, buff=0.3))
            return VGroup(*out)

        price0 = price_group(1)
        self.play(FadeOut(mb_def), FadeOut(read_c))
        self.play(Create(price0[0]), FadeIn(price0[1]),
                  FadeOut(VGroup(*rest_bars[1:])), FadeOut(eqn2),
                  FadeOut(demand2), FadeOut(d_lab2))
        self.pause()

        # B12b --------------------------------------------------------
        # the bar splits at the price: numbers ON the boxes, the words to
        # the right of them; the concept lands at the bottom edge

        cs_def = strip(definition('Consumer Surplus',
                                  "is the buyer's extra value from an exchange."))
        split0 = exchange_pieces()
        self.play(Transform(head, title('Consumer Surplus')),
                  FadeOut(rest_bars[0]), FadeOut(price0), FadeIn(split0))
        rig = always_redraw(exchange_pieces)
        self.remove(split0)
        self.add(rig)
        self.play(Write(cs_def))
        self.pause()

        # B12c --------------------------------------------------------
        # the price experiments, the original choreography: raise it -- the
        # exchange disappears and only her value's top edge stays; lower it
        # -- she buys eagerly; settle back at $1

        self.play(pv.animate.set_value(2.4), run_time=2, rate_func=smooth)
        self.play(pv.animate.set_value(0.5), run_time=2.5, rate_func=smooth)
        self.play(pv.animate.set_value(1.0), run_time=1.5, rate_func=smooth)
        self.pause()

        # B12c2 -------------------------------------------------------
        # the second bar, the exact same way: it joins, the price runs the
        # same experiment over both, and settles

        self.play(bars_n.animate.set_value(2), run_time=0.4)
        self.play(pv.animate.set_value(2.4), run_time=2, rate_func=smooth)
        self.play(pv.animate.set_value(0.5), run_time=2.5, rate_func=smooth)
        self.play(pv.animate.set_value(1.0), run_time=1.5, rate_func=smooth)
        self.pause()

        # B12d --------------------------------------------------------
        # the walk continues: bar 3 is the zero-surplus marginal unit, bar 4
        # is worth less than the price -- only its value's edge remains

        unhook(rig)
        only_drawables(self)
        s_bars = exchange_pieces()     # frozen p=1, n=2 state as statics:
        self.remove(rig)               # [price, b1cs, b1sp, num, num,
        self.add(s_bars)               #  b2cs, b2sp, num, num, csword, spword]
        cs_word3 = (Tex('Consumer Surplus').scale(0.55).set_color(DEMAND)
                    .next_to(ax2.c2p(4, 1.25), RIGHT, buff=0.3))
        sp_word3 = (Tex('Expenditure').scale(0.55).set_color(GOV)
                    .next_to(ax2.c2p(4, 0.5), RIGHT, buff=0.3))
        b3_sp = stair(3, 0, 1).set_stroke(GOV, 2).set_fill(GOV, AREA_OPACITY)
        b3_num = Tex('1.00').scale(0.5).set_color(INK).move_to(ax2.c2p(2.5, 0.5))
        b4_top = Line(ax2.c2p(3, 0.5), ax2.c2p(4, 0.5), color=DEMAND, stroke_width=3)
        self.play(FadeIn(b3_sp), FadeIn(b3_num),
                  Transform(s_bars[9], cs_word3), Transform(s_bars[10], sp_word3))
        self.play(FadeIn(b4_top))
        tally = math_rows(['CS $= 1.00 + 0.50 + 0.00 = \\$1.50$',
                           'Expenditure $= 3 \\times \\$1.00 = \\$3.00$'])
        qd_target = mark_value(ax2, 'x', 3, decimals=0)
        qd_ring = Ellipse(width=qd_target.get_width() + 0.4,
                          height=qd_target.get_height() + 0.32,
                          color=GUIDE, stroke_width=2.5).move_to(qd_target)
        qd_tag = Tex('$Q_d =$').scale(0.6).set_color(GUIDE).next_to(qd_ring, DOWN, buff=0.08)
        qd_mark = VGroup(qd_target, qd_ring, qd_tag)
        self.play(LaggedStart(*[Write(r) for r in tally], lag_ratio=0.6))
        self.play(FadeIn(qd_mark))
        self.pause()

        # B13 ---------------------------------------------------------
        # the surplus pieces merge into the triangle; the demand line
        # returns to hold the area's upper edge

        price13 = s_bars[0]
        b1_cs, b1_sp = s_bars[1], s_bars[2]
        b2_cs, b2_sp = s_bars[5], s_bars[6]
        others = VGroup(s_bars[3], s_bars[4], s_bars[7], s_bars[8],
                        s_bars[9], s_bars[10])
        tri = Polygon(ax2.c2p(0, 1), ax2.c2p(3, 1), ax2.c2p(0, 2.5),
                      color=DEMAND, fill_opacity=AREA_OPACITY)
        tri.z_index = 1
        self.play(FadeIn(demand2), FadeIn(d_lab2),
                  FadeOut(VGroup(b1_sp, b2_sp, b3_sp, b3_num, b4_top)),
                  FadeOut(others), FadeOut(tally),
                  ReplacementTransform(VGroup(b1_cs, b2_cs), tri))
        self.pause()

        # B13b --------------------------------------------------------

        area = math_rows(['Area $= \\frac{1}{2} h b$'])
        self.play(Write(area[0]))
        self.pause()

        # B13c --------------------------------------------------------
        # the height, on the P axis

        h_bar = Line(ax2.c2p(0, 1), ax2.c2p(0, 2.5), color=FOCUS, stroke_width=6)
        h_lab = (Tex('$h = \\$1.50$').scale(0.6).set_color(FOCUS)
                 .next_to(ax2.c2p(0, 1.75), LEFT, buff=0.55))
        self.play(Create(h_bar), FadeIn(h_lab))
        self.pause()

        # B13d --------------------------------------------------------
        # the base, on the Q axis

        b_bar = Line(ax2.c2p(0, 0), ax2.c2p(3, 0), color=FOCUS, stroke_width=6)
        b_lab = (Tex('$b = 3$').scale(0.6).set_color(FOCUS)
                 .next_to(ax2.c2p(1.5, 0), UP, buff=0.15))
        self.play(Create(b_bar), FadeIn(b_lab))
        self.pause()

        # B13e --------------------------------------------------------
        # the two numbers fly into the equation; almost the bars' number

        solve = math_rows(['Area $= \\frac{1}{2} h b$',
                           '$= \\frac{1}{2} (1.50)(3)$',
                           '$= \\$2.25$'])
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

        only_drawables(self)
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
        place(ax_m, [0, 62], [0, 13])
        m_q = Tex('Q').set_color(INK).next_to(ax_m.c2p(62, 0), RIGHT, buff=0.7)
        m_cap = axis_caption(ax_m, 'spinach, thousands of lbs per month')
        demand_m = ax_m.plot(MDemand, x_range=[0, 60], color=DEMAND)
        eqn_m = Tex('$P = 12 - Q/5$').scale(0.9).set_color(INK).move_to(ax_m.c2p(40, 9))
        d_lab_m = Tex('D').set_color(INK).next_to(ax_m.c2p(60, 0), UR, buff=0.15)

        STEP = 2.5                                   # one thin bar per decision
        cs_to = ValueTracker(0)

        def m_stair(x, r, lo, hi):
            return Polygon(ax_m.c2p(x, lo), ax_m.c2p(r, lo),
                           ax_m.c2p(r, hi), ax_m.c2p(x, hi))

        def market_bars():
            ct = cs_to.get_value()
            out, x = [], 0.0
            while x < 60 - 1e-6:
                r = min(x + STEP, 60)
                top = MDemand(r)                     # staircase: top-right corner on the line
                out.append(m_stair(x, r, 0, top).set_stroke(MUTED, 1, opacity=0.3)
                           .set_fill(MUTED, REST_OPACITY))
                if top >= 5 - 1e-6 and r <= ct + 1e-6:
                    out.append(m_stair(x, r, 5, top).set_stroke(DEMAND, 1)
                               .set_fill(DEMAND, AREA_OPACITY))
                x += STEP
            g = VGroup(*out)
            g.z_index = 0
            return g

        market_g = always_redraw(market_bars)

        self.play(FadeIn(head), FadeIn(ax_m), FadeIn(m_q), FadeIn(m_cap),
                  Create(demand_m))
        self.add(market_g)
        self.play(FadeIn(eqn_m), FadeIn(d_lab_m))
        self.pause()

        # B17b --------------------------------------------------------
        # the market read at $5

        read_m = read(ax_m, 35, 5, from_price=True, label='Q_d')
        play_read(self, read_m)
        mwork = math_rows(['$5 = 12 - Q/5$', '$Q = 35$ thousand lbs'])
        self.play(LaggedStart(*[Write(r) for r in mwork], lag_ratio=0.6))
        self.pause()

        # B17c --------------------------------------------------------
        # ...and at $2

        read_m2 = read(ax_m, 50, 2, from_price=True, label='Q_d')
        mwork_b = math_rows(['$2 = 12 - Q/5$', '$Q = 50$ thousand lbs'])
        self.play(FadeOut(read_m), FadeOut(mwork))
        play_read(self, read_m2)
        self.play(LaggedStart(*[Write(r) for r in mwork_b], lag_ratio=0.6))
        self.pause()

        # B18 ---------------------------------------------------------
        # too many bars to walk, so expenditure arrives as ONE rectangle

        read_m5 = read(ax_m, 35, 5, from_price=True, label='Q_d')
        self.play(FadeOut(read_m2), FadeOut(mwork_b))
        self.play(FadeIn(read_m5))
        spend_rect = Polygon(ax_m.c2p(0, 0), ax_m.c2p(35, 0), ax_m.c2p(35, 5), ax_m.c2p(0, 5),
                             color=GOV, fill_opacity=AREA_OPACITY)
        spend_rect.z_index = 1
        spend_lab = (Tex('Expenditure').scale(0.6).set_color(GOV)
                     .move_to(ax_m.c2p(17.5, 2.5)))
        spend_math = math_rows(['Expenditure $= P \\times Q_d$',
                                '$= \\$5 \\times 35{,}000$',
                                '$= \\$175{,}000$'])
        self.play(FadeIn(spend_rect), FadeIn(spend_lab))
        self.play(LaggedStart(*[Write(r) for r in spend_math], lag_ratio=0.6))
        self.pause()

        # B18b --------------------------------------------------------
        # the surplus IS the sweep: the height, then right through the bars
        # with the base extending under them

        self.play(FadeOut(spend_math))
        h_bar_m = Line(ax_m.c2p(0, 5), ax_m.c2p(0, 12), color=FOCUS, stroke_width=6)
        h_lab_m = (Tex('$h = \\$7$').scale(0.6).set_color(FOCUS)
                   .next_to(ax_m.c2p(0, 8.5), LEFT, buff=0.55))
        self.play(Create(h_bar_m), FadeIn(h_lab_m))

        base_bar = always_redraw(lambda: Line(
            ax_m.c2p(0, 0), ax_m.c2p(max(cs_to.get_value(), 0.001), 0),
            color=FOCUS, stroke_width=6))
        self.add(base_bar)
        self.play(cs_to.animate.set_value(35), run_time=5, rate_func=smooth)
        cs_lab_m = (Tex('Consumer Surplus').scale(0.55).set_color(DEMAND)
                    .move_to(ax_m.c2p(14.5, 6.4)))
        cs_math = math_rows(['CS $= \\frac{1}{2} h b$',
                             '$= \\frac{1}{2}(7)(35{,}000)$',
                             '$= \\$122{,}500$'])
        self.play(FadeIn(cs_lab_m))
        self.play(LaggedStart(*[Write(r) for r in cs_math], lag_ratio=0.6))
        self.pause()

        # B19 ---------------------------------------------------------
        # the limitation: willing, but not always able

        unhook(market_g, base_bar)
        only_drawables(self)
        FadeAll(self)

        # a schematic stage: bare axes, no numerals, no equations -- the
        # sentence's picture and nothing else
        ax_s = style_axes(x_range=[0, 10, 10], y_range=[0, 10, 10],
                          x_length=GRAPH_W, y_length=GRAPH_H).scale(GRAPH_SCALE)
        place(ax_s, [0, 10], [0, 10])
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

        only_drawables(self)
        FadeAll(self)
        head = title('Next Time $|$ Sellers', scale=1.5)
        topic = Tex('What does it cost them to say yes to a trade?').scale(1.2).set_color(INK)
        self.play(FadeIn(head), Write(topic))
        self.wait(1 / 2)     # let the Write settle before the export's parked frame
        self.pause()
