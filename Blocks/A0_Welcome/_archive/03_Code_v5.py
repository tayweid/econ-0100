# maniml 03_Code.py Episode0
#
# Episode 0 | Economics isn't about money
# One scene; beats follow 02_Storyboard.md (B01...B25). Talking-head beats
# (B06, B25) are not in the scene -- they're gaps between sections.

from manim import *
import numpy as np
import pandas as pd
import os
import sys
import warnings

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, beat(), title(), bumper(), ...
from style import axes as style_axes

warnings.filterwarnings('ignore')

# ---------------------------------------------------------------- data
# Loaded once at import so checkpoint restores never re-read CSVs.
HERE = os.path.dirname(os.path.abspath(__file__))
UNEMP = pd.read_csv(os.path.join(HERE, '00_Assets/unemployment.csv'))
RATES = UNEMP['rate'].to_numpy(dtype=float)
YEARS = UNEMP['date'].str.slice(0, 4).astype(int).to_numpy()
N_MONTHS = len(RATES)
MONTH_2008 = int(np.argmax(UNEMP['date'] == '2008-01'))   # Great Recession beat
WINDOW = 12 * 20                                             # 20-year visible window

WEALTH = pd.read_csv(os.path.join(HERE, '00_Assets/us_private_wealth_1870_2010.csv'))
WEALTH = WEALTH[(WEALTH.year >= 1920) & (WEALTH.year <= 1940)].reset_index(drop=True)
NIGHT_MAP = os.path.join(HERE, '00_Assets/nasa_black_marble_2016_5400x2700.jpg')
CITIES = pd.read_csv(os.path.join(HERE, '00_Assets/largest_cities_2018.csv'))



def centered(m, margin=0.8):
    if m.get_width() > FRAME_W - margin:
        m.scale((FRAME_W - margin) / m.get_width())
    return m.move_to([0, m.get_center()[1], 0])


# ---------------------------------------------------------------- the value line
# Choices are rungs at heights; higher is preferred. Episode-local choreography.
class ValueLine(VGroup):
    """A number line of value; items sit at positions driven by ValueTrackers, so
    reordering, rescaling and 'reading off' are continuous motions (the Part B
    price-line idiom). Horizontal by default: higher = further right."""

    def __init__(self, items, v_range=(0, 10), length=10, numbers=False, label_scale=0.7,
                 color=MUTED, stagger=True, **kwargs):
        super().__init__(**kwargs)
        self.v_min, self.v_max = v_range
        self.length = length
        self.label_scale = label_scale
        self.stagger = stagger
        self.line = NumberLine(x_range=[v_range[0], v_range[1], 1], length=length, color=color,
                               include_numbers=False, include_tip=False)
        self.add(self.line)
        self.t = {}
        self.marks = {}
        self.n_items = 0
        self.sides = {}
        for name, v in items.items():
            self._add_item(name, v)

    def v2p(self, v):
        left, right = self.line.get_left(), self.line.get_right()
        f = (v - self.v_min) / (self.v_max - self.v_min)
        return left + (right - left) * f

    def _add_item(self, name, v, color=INK, side=None):
        tr = ValueTracker(v)
        self.t[name] = tr
        if side is None:
            side = UP if (not self.stagger or self.n_items % 2 == 0) else DOWN
            self.n_items += 1
        self.sides[name] = side

        def make(name=name, tr=tr, side=side, color=color):
            p = self.v2p(tr.get_value())
            dot = Dot(p, color=GUIDE, z_index=10)
            lab = Tex(name).scale(self.label_scale).set_color(color).next_to(dot, side, buff=0.25 if side[1] > 0 else 0.6)
            return VGroup(dot, lab)

        m = always_redraw(make)
        self.marks[name] = m
        self.add(m)
        return m

    def values(self):
        return {k: tr.get_value() for k, tr in self.t.items()}

    def set_values(self, new):
        return [self.t[k].animate.set_value(v) for k, v in new.items() if k in self.t]

    def add_item(self, name, v, from_value=None, color=INK, side=None):
        start = v if from_value is None else from_value
        m = self._add_item(name, start, color=color, side=side)
        intro = FadeIn(m) if from_value is None else Succession(FadeIn(m, run_time=0.3), self.t[name].animate.set_value(v))
        return m, intro

    def remove_item(self, name):
        m = self.marks.pop(name); self.t.pop(name)
        self.remove(m)
        return FadeOut(m)

    def relabel(self, mapping):
        anims = []
        for old, new in mapping.items():
            v = self.t[old].get_value()
            side = self.sides[old]
            anims.append(self.remove_item(old))
            m, intro = self.add_item(new, v, side=side)
            anims.append(intro)
        return anims

    def number_labels(self, factor=1, step=1):
        nums = VGroup()
        for v in range(int(self.v_min), int(self.v_max) + 1, step):
            n = Integer(v * factor, group_with_commas=False).scale(0.5).set_color(self.line.get_color())
            n.next_to(self.v2p(v), DOWN, buff=0.2)
            nums.add(n)
        return nums

    def brace_to(self, name, text, color=INK, side=DOWN, buff=0.55):
        """Brace from the origin of the line to an item: its value as a length."""
        a, b = self.v2p(self.v_min), self.v2p(self.t[name].get_value())
        seg = Line(a, b).shift(side * buff)
        brace = Brace(seg, side, buff=0.05).set_color(color)
        lab = brace.get_text(text).scale(0.7).set_color(color)
        return VGroup(brace, lab)

    def reader(self, name, text, color=GUIDE, dy=1.3):
        """Tracker-driven vertical read line from an item up to a live number."""
        tr = self.t[name]

        def make():
            p = self.v2p(tr.get_value())
            end = p + UP * dy
            line = DashedLine(p, end, color=color)
            num = DecimalNumber(tr.get_value(), num_decimal_places=0, color=color).scale(0.7).next_to(end, UP, buff=0.1)
            lab = Tex(text).scale(0.6).set_color(color).next_to(num, UP, buff=0.08)
            return VGroup(line, num, lab)
        return always_redraw(make)

    def max_reader(self, text, exclude=(), color=GUIDE, dy=1.3):
        """Read line at the highest item (optionally excluding some)."""
        def make():
            best = max((v for k, v in self.values().items() if k not in exclude), default=self.v_min)
            p = self.v2p(best)
            end = p + UP * dy
            line = DashedLine(p, end, color=color)
            num = DecimalNumber(best, num_decimal_places=0, color=color).scale(0.7).next_to(end, UP, buff=0.1)
            lab = Tex(text).scale(0.6).set_color(color).next_to(num, UP, buff=0.08)
            return VGroup(line, num, lab)
        return always_redraw(make)

    def next_best_arrow(self, src, dst, color=GUIDE):
        a = self.marks[src][0].get_center() + DOWN * 0.15
        b = self.marks[dst][0].get_center() + DOWN * 0.15
        return CurvedArrow(a, b, angle=TAU / 5, color=color)


# ---------------------------------------------------------------- simple glyphs (placeholder style: INK outlines)
def apple(r=0.3):
    body = Circle(radius=r, color=INK, stroke_width=3)
    stem = Line(body.get_top(), body.get_top() + UP * 0.15 + RIGHT * 0.05, color=INK, stroke_width=3)
    return VGroup(body, stem)


def banana():
    return Arc(radius=0.45, start_angle=-PI * 0.15, angle=-PI * 0.7, color=INK, stroke_width=4)


def house(size=1.0):
    w, h = size, size * 0.8
    body = Rectangle(width=w, height=h, color=INK, stroke_width=3)
    roof = Polygon(body.get_corner(UL) + LEFT * 0.08, body.get_corner(UR) + RIGHT * 0.08,
                   body.get_top() + UP * h * 0.55, color=INK, stroke_width=3)
    door = Rectangle(width=w * 0.22, height=h * 0.45, color=INK, stroke_width=2).move_to(body.get_bottom() + UP * h * 0.225)
    return VGroup(body, roof, door)


def tickets(n):
    return VGroup(*[RoundedRectangle(width=0.55, height=0.3, corner_radius=0.06, color=INK, stroke_width=2)
                    for _ in range(n)]).arrange_in_grid(n_rows=2 if n > 3 else 1, buff=0.1)


def coin():
    c = Circle(radius=0.32, color=FOCUS, stroke_width=3)
    t = Tex('\\$1').scale(0.6).set_color(FOCUS).move_to(c)
    return VGroup(c, t)


class Episode0(Scene):
    """Episode 0 | Economics isn't about money."""

    def construct(self):
        self.b01_title()
        self.b02_unemployment()
        self.b04_wealth()
        self.b05_cities()
        self.b10_preferences()
        self.b16_utility()
        self.b22_scarcity()
        self.b26_choices()
        self.b28_tradeoffs()
        self.b33_grocery()
        self.b35_bakery()
        self.b37_marginal()
        self.b38_social()
        self.b42_what_is_micro()
        self.b44_six_parts()
        self.b43_next_time()

    # ------------------------------------------------------------ B01
    def b01_title(self):
        beat(self, 'B01_title')
        bumper(self, 'A', 0)

    # ------------------------------------------------------------ B02-B03
    def b02_unemployment(self):
        """Unemployment time series scrolling right. Continuous: one ValueTracker,
        linear rate, polyline rebuilt from the data window each frame (no
        curve-to-curve Transform, so no resampling wobble or per-step easing)."""
        beat(self, 'B02_unemployment_to_2008')
        y_max = float(np.ceil(RATES.max()))
        ax = style_axes([0, WINDOW], [0, y_max]).move_to(DOWN * 0.3)
        labels = title('Unemployment rate (\\%)')

        t = ValueTracker(400)   # month index of the right edge (starts ~1981)

        def window():
            tt = t.get_value()
            x0 = max(0.0, tt - WINDOW)
            return tt, x0

        def rate_at(m):
            i = int(np.floor(m))
            if i >= N_MONTHS - 1:
                return RATES[-1]
            f = m - i
            return RATES[i] + f * (RATES[i + 1] - RATES[i])

        def line():
            tt, x0 = window()
            lo, hi = int(np.ceil(x0)), int(np.floor(tt))
            pts = [ax.c2p(x0 - x0, rate_at(x0))]
            pts += [ax.c2p(i - x0, RATES[i]) for i in range(lo, hi + 1)]
            if tt > hi:
                pts.append(ax.c2p(tt - x0, rate_at(tt)))
            return polyline(pts, color=DEMAND)

        def tip_point():
            tt, x0 = window()
            return ax.c2p(tt - x0, rate_at(tt))

        series = always_redraw(line)
        dot = always_redraw(lambda: Dot(tip_point(), color=GUIDE, z_index=10))
        hline = always_redraw(lambda: ax.get_horizontal_line(
            tip_point(), color=GUIDE, line_config={'dashed_ratio': 0.85}).set_opacity(0.3))

        rate_label = DecimalNumber(0, num_decimal_places=1, color=GUIDE)
        rate_label.add_updater(lambda m: m.set_value(rate_at(t.get_value()))
                               .next_to(ax.c2p(0, rate_at(t.get_value())), LEFT))

        year_r = Integer(0, group_with_commas=False)
        year_r.add_updater(lambda m: m.set_value(YEARS[min(int(t.get_value()), N_MONTHS - 1)])
                           .next_to(ax.c2p(WINDOW, 0), DOWN))
        year_l = Integer(0, group_with_commas=False)
        year_l.add_updater(lambda m: m.set_value(YEARS[int(window()[1])])
                           .next_to(ax.c2p(0, 0), DOWN))

        self.add(ax, labels, year_l, year_r, rate_label, hline, dot)
        self.play(FadeIn(series), run_time=1 / 2)
        self.play(t.animate.set_value(MONTH_2008), run_time=8, rate_func=linear)
        self.wait()

        beat(self, 'B03_unemployment_to_2020')
        self.play(t.animate.set_value(N_MONTHS - 1), run_time=4.5, rate_func=linear)
        self.wait(2)

        for m in (series, dot, hline, rate_label, year_l, year_r):
            m.clear_updaters()
        self.play(FadeOut(VGroup(ax, labels, series, dot, hline, rate_label, year_l, year_r)))

    # ------------------------------------------------------------ B04 [new]
    def b04_wealth(self):
        """US private wealth, nominal $bn (Piketty-Zucman Table US.1). Climbs to
        1929, then collapses: $464bn -> $268bn by 1932."""
        beat(self, 'B04_wealth')
        yrs = WEALTH.year.to_numpy()
        w = WEALTH.private_wealth_nominal_bn.to_numpy()
        axes = style_axes([1920, 1940, 5], [0, 600, 100]).move_to(DOWN * 0.3)
        x_nums = VGroup(*[Integer(y, group_with_commas=False).scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(y, 0), DOWN) for y in range(1920, 1941, 5)])
        y_nums = VGroup(*[Tex(f'\\${v}').scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(1920, v), LEFT) for v in (100, 200, 300, 400, 500, 600)])
        ylab = title('U.S. private wealth (billions)')

        def segment(i0, i1):
            pts = [axes.c2p(yrs[i], w[i]) for i in range(i0, i1 + 1)]
            return polyline(pts, color=DEMAND)

        i29 = int(np.where(yrs == 1929)[0][0])
        i33 = int(np.where(yrs == 1933)[0][0])
        rise = segment(0, i29)
        fall = segment(i29, i33).set_stroke(GUIDE)
        after = segment(i33, len(yrs) - 1)

        self.play(FadeIn(axes), FadeIn(x_nums), FadeIn(y_nums), FadeIn(ylab))
        self.play(Create(rise), run_time=3, rate_func=linear)
        peak = Dot(axes.c2p(1929, w[i29]), color=GUIDE, z_index=10)
        peak_label = Tex(f'1929: \\${w[i29]:.0f}bn').scale(0.8).next_to(peak, UR, buff=0.15)
        self.play(FadeIn(peak), FadeIn(peak_label))
        self.wait()
        self.play(Create(fall), run_time=2.5, rate_func=linear)
        self.bring_to_front(peak)
        trough = Dot(axes.c2p(1933, w[i33]), color=GUIDE, z_index=10)
        trough_label = Tex(f'1933: \\${w[i33]:.0f}bn').scale(0.8).next_to(trough, DOWN)
        self.play(FadeIn(trough), FadeIn(trough_label))
        self.wait()
        self.play(Create(after), run_time=2, rate_func=linear)
        self.bring_to_front(peak, trough)
        q = Tex('Where did all that wealth go?').set_color(DEFINITION).to_edge(DOWN, buff=0.5)
        self.play(AddTextWordByWord(q))
        self.wait(2)
        self.play(FadeOut(VGroup(axes, x_nums, y_nums, ylab, rise, fall, after,
                                 peak, peak_label, trough, trough_label, q)))

    # ------------------------------------------------------------ B05 [new]
    def b05_cities(self):
        """NASA Black Marble with the 30 largest cities overlaid; ports vs inland."""
        beat(self, 'B05_cities')
        earth = ImageMobject(NIGHT_MAP)
        earth.set_height(FRAME_HEIGHT * 1.02)   # full bleed; 2:1 image, slight overscan so no background shows
        self.play(FadeIn(earth), run_time=2)
        self.wait()

        def lonlat_to_point(lon, lat):
            # equirectangular: linear in both axes, centred on (0, 0)
            x = earth.get_center()[0] + (lon / 180) * earth.get_width() / 2
            y = earth.get_center()[1] + (lat / 90) * earth.get_height() / 2
            return np.array([x, y, 0])

        port_color, inland_color = FOCUS, DEMAND
        dots = VGroup()
        for row in CITIES.itertuples():
            r = 0.035 * np.sqrt(row.pop_millions_2018)
            dots.add(Dot(lonlat_to_point(row.lon, row.lat), radius=r,
                         color=port_color if row.port else inland_color,
                         fill_opacity=0.85, z_index=10))
        beat(self, 'B05b_cities_appear')
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08), run_time=4)
        self.wait()

        n_port = int(CITIES.port.sum())
        n = len(CITIES)
        key = VGroup(
            VGroup(Dot(color=port_color), Tex('port').scale(0.8)).arrange(RIGHT, buff=0.15),
            VGroup(Dot(color=inland_color), Tex('inland').scale(0.8)).arrange(RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.6).to_corner(DL, buff=0.5)
        self.play(FadeIn(key))
        tally = Tex(f'{n_port} of the {n} largest cities are ports.').set_color(DEFINITION).to_edge(DOWN, buff=0.5).shift(RIGHT * 2)
        self.play(AddTextWordByWord(tally))
        self.wait(2)
        self.play(FadeOut(tally), FadeOut(key), FadeOut(dots), FadeOut(earth))


    # ------------------------------------------------------------ B10-B15  preferences
    def b10_preferences(self):
        beat(self, 'B10_cakes')
        self.behavior_title = (title('This class is about behavior.'))
        self.play(FadeIn(self.behavior_title))

        cakes = centered(tex_row(['Carrot Cake', '$\\succ$', 'Chocolate Cake']))
        self.play(FadeIn(cakes, lag_ratio=0.3))
        self.wait()
        self.play(FadeOut(cakes))

        beat(self, 'B11_coffee')
        coffee = centered(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast']))
        self.play(FadeIn(coffee, lag_ratio=0.3))
        self.wait()

        beat(self, 'B12_transitivity')
        coffee3 = centered(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast', '$\\succ$', 'Light Roast']))
        self.play(Transform(coffee, coffee3))
        self.wait()

        beat(self, 'B13_chain_onto_number_line')
        # the coffees dissolve onto a number line: ranking with numbers
        V = ValueLine({'Dark Roast': 8, 'Medium Roast': 5, 'Light Roast': 2}, stagger=True).move_to(DOWN * 0.3)
        self.play(
            Transform(coffee[0], V.marks['Dark Roast'][1].copy()),
            Transform(coffee[2], V.marks['Medium Roast'][1].copy()),
            Transform(coffee[4], V.marks['Light Roast'][1].copy()),
            FadeOut(coffee[1]), FadeOut(coffee[3]),
            Create(V.line), run_time=1.5,
        )
        self.remove(coffee)
        self.add(V)
        self.wait()
        m1, a1 = V.add_item('Espresso', 9.5, from_value=8)
        m2, a2 = V.add_item('Decaf', 0.5, from_value=2)
        self.play(a1, a2)
        self.wait()
        self.V = V

        beat(self, 'B14_rank_anything')
        self.play(*V.relabel({'Espresso': 'Fall', 'Dark Roast': 'Spring', 'Medium Roast': 'Summer', 'Light Roast': 'Winter', 'Decaf': 'Slush'}))
        self.wait()
        self.play(*V.relabel({'Fall': 'Mushroom', 'Spring': 'Pepperoni', 'Summer': 'Plain', 'Winter': 'Olive', 'Slush': 'Pineapple'}))
        self.wait()
        self.play(*V.relabel({'Mushroom': 'Espresso', 'Pepperoni': 'Dark Roast', 'Plain': 'Medium Roast', 'Olive': 'Light Roast', 'Pineapple': 'Decaf'}))

        beat(self, 'B15_preferences_are_rankings')
        card = centered(definition('Preferences', 'are rankings.')).to_edge(DOWN, buff=0.6)
        self.play(AddTextWordByWord(card))
        self.wait()
        self.play(FadeOut(card))

    # ------------------------------------------------------------ B16-B21  utility
    def b16_utility(self):
        beat(self, 'B16_numbers')
        V = self.V
        nums = V.number_labels()
        self.play(FadeIn(nums, lag_ratio=0.05))
        self.wait()

        beat(self, 'B17_utility_definition')
        card = centered(definition('Utility', 'is a number that does the ranking for us.')).to_edge(DOWN, buff=0.6)
        self.play(AddTextWordByWord(card))
        self.wait()
        self.play(FadeOut(card))

        beat(self, 'B18_mine_and_yours')
        self.play(V.animate.shift(UP * 1.2), nums.animate.shift(UP * 1.2))
        me = Tex('Me').scale(0.8).set_color(MUTED).next_to(V.line, LEFT, buff=0.4)
        Y = ValueLine({'Light Roast': 8.5, 'Decaf': 6.5, 'Medium Roast': 5, 'Espresso': 2.5, 'Dark Roast': 1}, stagger=True).move_to(DOWN * 1.8)
        ynums = Y.number_labels()
        you = Tex('You').scale(0.8).set_color(MUTED).next_to(Y.line, LEFT, buff=0.4)
        self.play(FadeIn(me), FadeIn(Y), FadeIn(ynums), FadeIn(you))
        self.wait()

        beat(self, 'B19_benefits')
        arrow = Arrow(Y.line.get_left() + DOWN * 0.9, Y.line.get_right() + DOWN * 0.9, color=MUTED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.03)
        cap = Tex('benefit').scale(0.7).set_color(MUTED).next_to(arrow, DOWN, buff=0.15)
        self.play(FadeOut(nums), FadeOut(ynums), FadeIn(arrow), FadeIn(cap))
        self.wait()
        self.play(FadeOut(arrow), FadeOut(cap), FadeIn(nums), FadeIn(ynums))

        beat(self, 'B20_times_100')
        self.play(Transform(nums, V.number_labels(100)), Transform(ynums, Y.number_labels(100)))
        self.wait()
        self.play(Transform(nums, V.number_labels()), Transform(ynums, Y.number_labels()))
        self.wait()

        beat(self, 'B21_preferences_change')
        self.play(FadeOut(Y), FadeOut(you), FadeOut(me), FadeOut(nums), FadeOut(ynums))
        self.play(*[V.remove_item(k) for k in list(V.t)], V.animate.move_to(DOWN * 0.3))
        V.n_items = 0
        mc, ac = V.add_item('Coffee', 7); mt, at = V.add_item('Tea', 3)
        self.play(ac, at)
        self.wait()
        self.play(*V.set_values({'Coffee': 3, 'Tea': 7}), run_time=1.5)
        self.wait()
        self.play(FadeOut(V), FadeOut(self.behavior_title))
        self.V = None

    # ------------------------------------------------------------ B22-B25  scarcity
    def b22_scarcity(self):
        beat(self, 'B22_cant_always')
        self.scarcity_title = (title('This class is about scarcity.'))
        self.play(FadeIn(self.scarcity_title))
        q1 = centered(Tex("We can't always have what we want most."))
        self.play(AddTextWordByWord(q1))
        self.wait()
        self.play(FadeOut(q1))

        beat(self, 'B23_scarcity_basic')
        q2 = centered(definition('Scarcity', 'is more basic than money.'))
        self.play(Write(q2))
        self.wait()
        self.play(FadeOut(q2))

        beat(self, 'B24_house_or_movies')
        big = VGroup(house(1.6), tickets(2)).arrange(DOWN, buff=0.35)
        big_lab = Tex('near the park, fewer movies').scale(0.6).set_color(MUTED).next_to(big, DOWN, buff=0.25)
        small = VGroup(house(0.9), tickets(6)).arrange(DOWN, buff=0.35)
        small_lab = Tex('far from the park, more movies').scale(0.6).set_color(MUTED).next_to(small, DOWN, buff=0.25)
        OR = Tex('or').scale(1.2)
        A = VGroup(big, big_lab); B = VGroup(small, small_lab)
        row = VGroup(A, OR, B).arrange(RIGHT, buff=1.2)
        centered(row).shift(DOWN * 0.2)
        self.play(FadeIn(A))
        self.play(FadeIn(OR))
        self.play(FadeIn(B))
        self.wait()
        box_a = SurroundingRectangle(A, buff=0.3).set_color(EFFICIENT)
        box_b = SurroundingRectangle(B, buff=0.3).set_color(NASH)
        self.play(Create(box_a), Create(box_b))
        self.wait()
        self.play(box_a.animate.move_to(B), box_b.animate.move_to(A))
        self.wait()
        self.play(FadeOut(row), FadeOut(box_a), FadeOut(box_b))

        beat(self, 'B25_who_gets_the_house')
        h1 = VGroup(house(1.6), Tex('Taylor gets the house').scale(0.7)).arrange(DOWN, buff=0.3)
        h2 = VGroup(house(1.6), Tex('Andrew gets the house').scale(0.7)).arrange(DOWN, buff=0.3)
        OR = Tex('or').scale(1.2)
        row = centered(VGroup(h1, OR, h2).arrange(RIGHT, buff=1.2)).shift(DOWN * 0.2)
        self.play(FadeIn(h1)); self.play(FadeIn(OR)); self.play(FadeIn(h2))
        self.wait()
        box_a = SurroundingRectangle(h1, buff=0.3).set_color(EFFICIENT)
        box_b = SurroundingRectangle(h2, buff=0.3).set_color(NASH)
        self.play(Create(box_a), Create(box_b))
        self.wait()
        self.play(box_a.animate.move_to(h2), box_b.animate.move_to(h1))
        self.wait()
        self.play(FadeOut(row), FadeOut(box_a), FadeOut(box_b), FadeOut(self.scarcity_title))

    # ------------------------------------------------------------ B26-B27  choices
    def b26_choices(self):
        beat(self, 'B26_choices_because')
        q = centered(Tex('We make choices because of preferences and scarcity.')).shift(UP * 0.6)
        self.play(AddTextWordByWord(q))
        self.wait()

        beat(self, 'B27_choices_equation')
        eq = centered(tex_row(['Preferences', '$+$', 'Scarcity', '$=$', 'Choices'], color=DEFINITION, buff=0.4)).next_to(q, DOWN, buff=0.8)
        for piece in eq:
            self.play(FadeIn(piece), run_time=0.6)
        self.wait()
        self.play(FadeOut(q), FadeOut(eq))

    # ------------------------------------------------------------ B28-B32  tradeoffs
    def b28_tradeoffs(self):
        beat(self, 'B28_A_or_B')
        self.tradeoff_title = title('This class is about tradeoffs.')
        self.play(FadeIn(self.tradeoff_title))
        OR = Tex(' or ').scale(1.5).shift(UP * 1.4)
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(A)); self.wait()
        self.play(FadeIn(OR)); self.wait()
        self.play(FadeIn(B)); self.wait()
        # one or the other: the green box picks, the red box is what's given up
        box_a = SurroundingRectangle(A, buff=0.3).set_color(EFFICIENT)
        box_b = SurroundingRectangle(B, buff=0.3).set_color(NASH)
        self.play(Create(box_a), Create(box_b))
        for _ in range(2):
            self.play(box_a.animate.move_to(B), box_b.animate.move_to(A), run_time=0.6); self.wait(0.3)
            self.play(box_a.animate.move_to(A), box_b.animate.move_to(B), run_time=0.6); self.wait(0.3)

        beat(self, 'B29_benefit')
        # A and B on a number line: benefit is A's value
        V = ValueLine({'A': 7, 'B': 4}, length=8, stagger=False, label_scale=1.0).move_to(DOWN * 1.4)
        self.play(Create(V.line), FadeIn(VGroup(*V.marks.values())))
        ben = V.brace_to('A', 'benefit of A', color=EFFICIENT, side=DOWN, buff=0.55)
        self.play(FadeIn(ben))
        self.wait()

        beat(self, 'B30_cost')
        cost = V.brace_to('B', 'cost of A = value of B', color=NASH, side=DOWN, buff=1.45)
        self.play(FadeIn(cost))
        self.wait()

        beat(self, 'B31_opportunity_cost_definition')
        eq = (Tex('Opportunity Cost({{A}}) = {{B}}').scale(1.2).next_to(OR, DOWN, buff=0.6)
              .set_color_by_tex_to_color_map({'A': EFFICIENT, 'B': NASH}))
        self.play(Write(eq))
        self.wait()
        oc = centered(definition('Opportunity Cost', 'is the value of the next best alternative.')).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(ben), FadeOut(cost), AddTextWordByWord(oc))
        self.wait()

        beat(self, 'B32_switch')
        eq2 = (Tex('Opportunity Cost({{B}}) = {{A}}').scale(1.2).move_to(eq)
               .set_color_by_tex_to_color_map({'A': NASH, 'B': EFFICIENT}))
        self.play(box_a.animate.move_to(B), box_b.animate.move_to(A), Transform(eq, eq2),
                  *V.set_values({'A': 4, 'B': 7}), run_time=1.2)
        ben2 = V.brace_to('B', 'benefit of B', color=EFFICIENT, side=DOWN, buff=0.55)
        cost2 = V.brace_to('A', 'cost of B = value of A', color=NASH, side=DOWN, buff=1.45)
        self.play(FadeOut(oc), FadeIn(ben2), FadeIn(cost2))
        self.wait()
        self.play(FadeOut(VGroup(A, OR, B, box_a, box_b, eq, V, ben2, cost2, self.tradeoff_title)))

    # ------------------------------------------------------------ B33-B34  grocery
    def b33_grocery(self):
        beat(self, 'B33_apple_or_banana')
        head = title('Forbes Ave Grocery')
        self.play(FadeIn(head))
        ap = Tex('Apple \\$1').scale(1.2).set_color(SPINACH)
        ba = Tex('Banana \\$1').scale(1.2).set_color(FOCUS)
        OR = Tex('or').scale(1.2)
        row = centered(VGroup(ap, OR, ba).arrange(RIGHT, buff=1.5)).shift(UP * 0.5)
        self.play(FadeIn(row))
        self.wait()
        box_a = SurroundingRectangle(ap, buff=0.3).set_color(EFFICIENT)
        box_b = SurroundingRectangle(ba, buff=0.3).set_color(NASH)
        self.play(Create(box_a), Create(box_b))
        oc = Tex('Opportunity Cost(apple) = banana').scale(0.9).next_to(row, DOWN, buff=0.9)
        self.play(Write(oc))
        self.wait()
        self.play(FadeOut(row), FadeOut(box_a), FadeOut(box_b), FadeOut(oc))

        beat(self, 'B34_cost_of_a_dollar')
        V = ValueLine({'Apple': 7, 'Orange': 5, 'Chocolate': 3.5, 'Bike share': 1.5}, stagger=True).move_to(DOWN * 0.6)
        c = coin().next_to(V.line, LEFT, buff=0.5)
        q = Tex('what can a dollar get?').scale(0.8).set_color(MUTED).move_to(UP * 2.2)
        self.play(FadeIn(c), FadeIn(q), Create(V.line))
        self.play(FadeIn(VGroup(*V.marks.values()), lag_ratio=0.2))
        self.wait()
        oc = V.max_reader('OC(\\$1) = the max', dy=1.0)
        self.play(FadeIn(oc))
        self.wait()
        # chocolate climbs past apple; the read line follows; the choice flips
        self.play(*V.set_values({'Chocolate': 8.5}), run_time=2, rate_func=linear)
        flip = Tex('the choice flips').scale(0.8).set_color(FOCUS).next_to(V.line, DOWN, buff=1.2)
        self.play(FadeIn(flip))
        self.wait()
        self.play(FadeOut(V), FadeOut(c), FadeOut(q), FadeOut(oc), FadeOut(flip), FadeOut(head))

    # ------------------------------------------------------------ B35-B36  bakery
    def b35_bakery(self):
        beat(self, 'B35_pie_or_bread')
        head = title('The bakery')
        self.play(FadeIn(head))
        V = ValueLine({'Banana bread': 3, 'Apple pie': 6}, stagger=False).move_to(DOWN * 0.2)
        self.play(Create(V.line), FadeIn(VGroup(*V.marks.values())))
        table = VGroup().to_edge(DOWN, buff=0.7)
        # find one opportunity cost: from the choice to the next best
        arr = V.next_best_arrow('Apple pie', 'Banana bread')
        self.play(Create(arr))
        line = Tex('OC(pie) = bread').scale(0.8).to_edge(DOWN, buff=0.7).shift(LEFT * 4)
        self.play(Write(line))
        table.add(line)
        self.wait()
        self.play(FadeOut(arr))

        beat(self, 'B36_carrot_cake')
        m, intro = V.add_item('Carrot cake', 9, from_value=0)
        self.play(intro, run_time=1.5)
        self.wait()
        # redo pie: the next best is now the cake
        arr = V.next_best_arrow('Apple pie', 'Carrot cake')
        self.play(Create(arr))
        new_line = Tex('OC(pie) = cake').scale(0.8).move_to(line)
        self.play(Transform(line, new_line))
        self.wait()
        self.play(FadeOut(arr))
        # then the cake, then the bread, one at a time
        for src, dst, text, dx in [('Carrot cake', 'Apple pie', 'OC(cake) = pie', 0), ('Banana bread', 'Carrot cake', 'OC(bread) = cake', 4)]:
            arr = V.next_best_arrow(src, dst)
            self.play(Create(arr))
            t = Tex(text).scale(0.8).to_edge(DOWN, buff=0.7).shift(RIGHT * dx)
            self.play(Write(t))
            table.add(t)
            self.wait(0.5)
            self.play(FadeOut(arr))
        self.wait()
        self.play(FadeOut(V), FadeOut(table), FadeOut(head))

    # ------------------------------------------------------------ B37  marginal
    def b37_marginal(self):
        beat(self, 'B37_one_more_apple')
        head = (title('One more apple?'))
        self.play(FadeIn(head))
        benefits = [9, 7, 5, 3, 1]
        cost = 4
        unit = 0.32
        base_y = ORIGIN[1] - 1.6
        cols = VGroup()
        for i, b in enumerate(benefits):
            bar = Rectangle(width=0.7, height=b * unit, color=EFFICIENT, fill_color=EFFICIENT, fill_opacity=AREA_OPACITY, stroke_width=2)
            bar.move_to([0, base_y + b * unit / 2, 0])
            glyph = Tex(str(i + 1)).scale(0.8).next_to(bar, DOWN, buff=0.15)
            cols.add(VGroup(bar, glyph))
        cols.arrange(RIGHT, buff=0.45, aligned_edge=DOWN)
        cols.move_to([ORIGIN[0], cols.get_center()[1], 0])
        for i, col in enumerate(cols):
            col[0].align_to([0, base_y, 0], DOWN)
            col[1].next_to(col[0], DOWN, buff=0.15)
        cost_line = DashedLine(cols.get_left() + LEFT * 0.4, cols.get_right() + RIGHT * 0.4, color=NASH).move_to([cols.get_center()[0], base_y + cost * unit, 0])
        cost_lab = Tex('marginal cost').scale(0.6).set_color(NASH).next_to(cost_line, RIGHT, buff=0.15)
        mb_lab = Tex('marginal benefit').scale(0.6).set_color(EFFICIENT).next_to(cols[0][0], LEFT, buff=0.25).shift(UP * 0.4)
        self.play(LaggedStart(*[FadeIn(c[1]) for c in cols], lag_ratio=0.2))
        self.play(LaggedStart(*[GrowFromEdge(c[0], DOWN) for c in cols], lag_ratio=0.25), FadeIn(mb_lab))
        self.wait()
        self.play(Create(cost_line), FadeIn(cost_lab))
        self.wait()
        marks = VGroup()
        for b, col in zip(benefits, cols):
            ok = b > cost
            m = Tex('\\checkmark' if ok else '$\\times$').scale(0.9).set_color(EFFICIENT if ok else NASH).next_to(col[0], UP, buff=0.15)
            marks.add(m)
            self.play(FadeIn(m), run_time=0.5)
            self.wait(0.3)
        line = centered(Tex('{{Marginal}} means one more.').set_color_by_tex_to_color_map({'Marginal': DEFINITION})).to_edge(DOWN, buff=0.5)
        self.play(Write(line))
        self.wait()
        self.play(FadeOut(line))
        self.play(FadeOut(cols), FadeOut(cost_line), FadeOut(cost_lab), FadeOut(mb_lab), FadeOut(marks), FadeOut(head))

    # ------------------------------------------------------------ B38-B41
    def b38_social(self):
        beat(self, 'B38_autarky')
        social_title = (title('This class is about social environments.'))
        self.play(FadeIn(social_title))
        aut = centered(definition('Autarky', 'is a state of economic self-sufficiency.'))
        self.play(AddTextWordByWord(aut))
        self.wait()
        self.play(FadeOut(aut))

        beat(self, 'B39_dating_game')
        # rows = you, columns = your love interest
        table = Table(
            [['10', '$-1$'],
             ['$-1$', '8']],
            row_labels=[Tex('Movie'), Tex('Theater')],
            col_labels=[Tex('Movie').set_color(COL_PLAYER), Tex('Theater').set_color(COL_PLAYER)],
            element_to_mobject=Tex,
        ).scale(0.8).move_to(ORIGIN)
        you = Tex('You').next_to(table.get_rows()[1:], LEFT, buff=0.6)
        them = Tex('Love interest').set_color(COL_PLAYER).next_to(table.get_columns()[1:], UP, buff=0.4)
        self.play(FadeIn(table), FadeIn(you), FadeIn(them))
        self.wait()

        beat(self, 'B40_their_choices_your_choices')
        col_box = SurroundingRectangle(table.get_columns()[1], buff=0.2).set_color(COL_PLAYER)
        self.play(Create(col_box))
        col_box2 = SurroundingRectangle(table.get_columns()[2], buff=0.2).set_color(COL_PLAYER)
        self.play(Transform(col_box, col_box2))
        self.wait()
        self.play(FadeOut(col_box))
        row_box = SurroundingRectangle(table.get_rows()[1], buff=0.2).set_color(ROW_PLAYER)
        self.play(Create(row_box))
        row_box2 = SurroundingRectangle(table.get_rows()[2], buff=0.2).set_color(ROW_PLAYER)
        self.play(Transform(row_box, row_box2))
        self.wait()
        self.play(FadeOut(row_box))

        beat(self, 'B41_walk_the_cells')
        # love interest at the movie: go with them (10) beats not (-1)
        cell = SurroundingRectangle(table.get_entries((2, 2)), buff=0.25).set_color(EFFICIENT)
        self.play(Create(cell))
        self.wait()
        self.play(Transform(cell, SurroundingRectangle(table.get_entries((3, 2)), buff=0.25).set_color(NASH)))
        self.wait()
        # love interest at the theater: don't leave them hanging (-1); go with them (8)
        self.play(Transform(cell, SurroundingRectangle(table.get_entries((2, 3)), buff=0.25).set_color(NASH)))
        self.wait()
        self.play(Transform(cell, SurroundingRectangle(table.get_entries((3, 3)), buff=0.25).set_color(EFFICIENT)))
        self.wait()
        self.play(FadeOut(cell), FadeOut(table), FadeOut(you), FadeOut(them), FadeOut(social_title))

    # ------------------------------------------------------------ B42
    def b42_what_is_micro(self):
        beat(self, 'B42_what_is_micro')
        head = title('Microeconomics tells us...')
        bullets = [
            "there's a deep fundamental reason why it pays to coordinate with each other,",
            'that markets can serve as an effective coordination device sometimes,',
            'that markets often fail,',
            'gives us a framework for when,',
            'and provides some alternatives for doing better.',
        ]
        lines = VGroup(*[Tex('$\\bullet$ ' + b).scale(0.9) for b in bullets]).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        lines.next_to(head, DOWN, buff=0.8).align_to(head, LEFT)
        self.play(FadeIn(head))
        for l in lines:
            self.play(AddTextWordByWord(l))
        self.wait(2)
        self.play(FadeOut(head), FadeOut(lines))

    # ------------------------------------------------------------ B43
    def b43_next_time(self):
        beat(self, 'B43_next_time')
        head = title('Next time...', scale=1.5)
        topic = Tex('A trip back to 1800s British philosophy.').scale(1.2)
        self.add(head, topic)
        framebox_reveal(self, topic)
        self.wait()
        self.play(FadeOut(head), FadeOut(topic))

    # ------------------------------------------------------------ B44
    def b44_six_parts(self):
        beat(self, 'B44_six_parts')
        head = title('This class contains six parts.', scale=1.5)
        self.play(FadeIn(head))
        parts = [
            '{{Part A}}. A history changing question.',
            '{{Part B}}. Markets can coordinate our choices.',
            '{{Part C}}. Externalities break markets; governments can help.',
            '{{Part D}}. Some markets are not easily fixable.',
            "{{Part E}}. Sellers' decisions shape how markets behave.",
            "{{Part F}}. Buyers' decisions shape the demand curve.",
        ]
        cmap = {f'Part {p}': GUIDE for p in 'ABCDEF'}
        tiles = VGroup()
        for i, p in enumerate(parts):
            t = Tex(p).to_edge(LEFT, buff=0.8).shift(UP + DOWN * i * 2 / 3).set_color_by_tex_to_color_map(cmap)
            tiles.add(t)
            self.play(FadeIn(t))
            self.wait()
        self.wait(2)
        self.play(FadeOut(tiles), FadeOut(head))
